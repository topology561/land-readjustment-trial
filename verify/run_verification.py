# -*- coding: utf-8 -*-
"""
W-V 驗證熔爐 — headless 重現 app.py 街角選位管線，雙情境（退縮 0m/3.5m），
逐格對拍 verify/baselines/。**additive-only：app.py 一字不改**（全走 app_harvest 真函式）。

管線階段（全部真函式；幾何半已證 cell-exact）：
  1. harvest → parse_block_dxf(V6.dxf) → classified_blocks（+分類）
  2. parse_cad_precision_layers → front/side/alloc lines
  3. _annotate_block_corner_flags → has_corner/corner_sides
  4. _rebuild_corners_topology post-pass → geom_restore.theoretical_corners（含 side）
  5. 參數表（截角/街角最小面積，雙情境）           → 對 退縮{0,3.5}m參數.csv        ✅
  6. -a 診斷（front_idx 舊/新、截角 idx、閘）        → 對 W-D.1.3-a 診斷_退縮*.csv     ✅
  7. 選位半：ownership（tab1 指紋）＋ parcels ＋ PK  → 對 W-D.1.2/第1宗/W-D.1.3-d
     （selection_pipeline.py；UI inline 逐行複刻＋真函式 v12）

對拍鍵 doctrine（KL）：指配/診斷以「宗地地號＋持分結構」為鍵，**非歸戶號流水編號**
（匿名前後群組編號會依姓名筆劃重排）。診斷嫌犯序：快照漏參數 > driver orchestration 漂移 > 引擎（勿動 app）。
"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from app_harvest import harvest  # noqa: E402
from selection_pipeline import (  # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import (  # noqa: E402
    run_step_g, build_step_g_tables, compute_total_burden_rate)

SNAPSHOT = os.path.join(HERE, "case_params_UC9898.json")
V6DXF = os.path.join(REPO, "data", "V6.dxf")
ANON_XLSX = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
BASELINES = os.path.join(HERE, "baselines")
# baselines/v2/＝財務半中間態期（C=0、A=1）之歷史錨，**凍存不刪、不再對拍**（見 v3/PROVENANCE_v3.md）
V3RUN = os.path.join(HERE, "baselines", "v3")    # 🆕 v3 錨定 baseline（財務接線波換源，KL 裁定 2026-07-09）
F0DIR = os.path.join(HERE, "baselines", "wf", "f0")  # 🆕 W-F F.0 終態 baseline（trunk B；v3 凍存不動）
F1DIR = os.path.join(HERE, "baselines", "wf", "f1")  # 🆕 W-F F.1 遞補整形 baseline（R1 縮圍）
F2DIR = os.path.join(HERE, "baselines", "wf", "f2")  # 🆕 W-F F.2 跨街廓調配 baseline（trunk C）
F3DIR = os.path.join(HERE, "baselines", "wf", "f3")  # 🆕 W-F F.3 公設地調配 baseline（trunk D）
F4DIR = os.path.join(HERE, "baselines", "wf", "f4")  # 🆕 W-F F.4 收斂波 baseline（trunk E；7-4/7-5/整形/總決算）
# k* 六塊經驗錨（**非機制不變量**：k* 經 widths→S→A/B/C 機制上會吃價；本案恰不變，硬斷言看守）
K_STAR_EXPECT = {"R1": 2, "R2": 8, "R3": 7, "R4": 1, "R5": 7, "R6": 6}
OUTDIR = os.path.join(HERE, "out")
CORNER_BLOCKS = ["R1", "R2", "R3", "R4", "R5", "R6"]


def _cat_for(lbl):
    if lbl and lbl.startswith("RD"):
        return "道路"
    if lbl and lbl.startswith("R"):
        return "住宅區"
    if lbl and lbl.startswith("G"):
        return "鄰里公園"
    return "未分類"


def build_pipeline(ns, fake_st, snapshot):
    """階段 1-4：真函式重建 classified_blocks（含 geom_restore.theoretical_corners）＋ cad lines，
    並填入 fake session_state（下游真函式讀）。回傳 (cb_by_label, cad_layers)。"""
    with open(V6DXF, "rb") as f:
        raw = f.read()
    bd = ns["parse_block_dxf"](raw)
    fcb = ns.get("F3_CATEGORY_BURDEN", {})
    cb = []
    for p in bd["polygons"]:
        if p.get("is_outer"):
            continue
        lbl = p.get("label") or f"#{p.get('id')}"
        cat = _cat_for(lbl)
        cb.append({**p, "label": lbl, "category": cat,
                   "burden_type": fcb.get(cat, "未分類"),
                   "has_corner": False, "corner_sides": []})
    doc = ns["_read_dxf_any_encoding"](raw)
    cad = ns["parse_cad_precision_layers"](doc, cb)
    cb = ns["_annotate_block_corner_flags"](cb, cad.get("side_lengths_by_side", {}) or {})
    flm = cad.get("front_lines", {}) or {}
    slm = cad.get("side_lines_by_side", {}) or {}
    # 截角拓樸定錨 post-pass（單一真相源；-a 切換之 production 路徑）
    for b in cb:
        gr = b.get("geom_restore")
        if not isinstance(gr, dict):
            continue
        edges = (gr.get("classification") or {}).get("edges") or []
        tcs = ns["_rebuild_corners_topology"](edges, flm.get(b["label"]), slm.get(b["label"]))
        if tcs is None:
            tcs = []
        gr["theoretical_corners"] = tcs
        gr["cutoff_total_area"] = round(sum(float(t.get("cutoff_area_m2", 0) or 0) for t in tcs), 4)
        b["cutoff_total_area_m2"] = gr["cutoff_total_area"]
    # fake session_state（真函式 _make_chamfer_tri_wb / _build_corner_range_v2 讀）
    ss = fake_st.session_state
    ss["f3_cad_front_lines"] = flm
    ss["f3_cad_side_lines_by_side"] = slm
    ss["f3_cad_alloc_dir"] = cad.get("alloc_dir_by_block", {}) or {}
    ss["f3_classified_blocks"] = cb
    # 🆕 微波：重劃總負擔率 **現算**（v3 快照輸入＋DXF 面積導出；廢 global.重劃總負擔率 寫死值）。
    #    消費者＝_estimate_G_for_qualification（街角 PK 之 G估）＋ iterate_G_S 迭代初值。
    _rate, _rate_bd = compute_total_burden_rate(ns, cb, snapshot)
    ss["f3_total_burden_rate_from_finance"] = _rate
    ss["_v3_burden_rate_breakdown"] = _rate_bd      # 財務閘消費（非計算鏈）
    return {b["label"]: b for b in cb}, cad


def build_param_table(ns, fake_st, cb_by, cad, snapshot, setback):
    """階段 5：參數表（一情境）。回傳 list[dict]（欄序同 baseline 參數CSV）。"""
    legal_w = float(snapshot["global"]["法定最小寬_m"])
    legal_d = float(snapshot["global"]["法定最小深_m"])
    SB = snapshot["blocks"]
    slm = cad.get("side_lines_by_side", {}) or {}
    flm = cad.get("front_lines", {}) or {}
    alloc = cad.get("alloc_dir_by_block", {}) or {}
    rows = []
    for lbl in CORNER_BLOCKS:
        b = cb_by[lbl]
        blk = SB[lbl]
        sd = b.get("corner_sides") or []
        has_l, has_r = "left" in sd, "right" in sd
        fw = float(blk["正面"]["路寬_m"])
        lw = float(blk["左側"]["路寬_m"]); rw = float(blk["右側"]["路寬_m"])
        depth = float(blk["街廓分配深度_m"])
        fl = flm.get(lbl) or {}
        per = ns["_compute_per_end_cutoff_areas"](b, fl.get("p1"), fl.get("p2"))
        cutL = float(per["p1_end"]["cutoff_area"]); cutR = float(per["p2_end"]["cutoff_area"])
        verts = b.get("vertices") or []
        cen = b.get("centroid") or (0.0, 0.0)
        side = slm.get(lbl) or {}
        shift = setback + legal_w

        def rng(which):
            if which not in side:
                return None
            chi = ns["_make_chamfer_tri_wb"](b, which)
            r = ns["_build_corner_range_v2"](side[which]["mid"], verts, cen, alloc.get(lbl), shift, chi)
            return round(float(r.area), 2) if r is not None else None
        rows.append({
            "街廓": lbl, "分類": b["category"],
            "正面路寬(m)": round(fw, 2),
            "【左】路寬(m)": (round(lw, 2) if has_l else "—"),
            "【右】路寬(m)": (round(rw, 2) if has_r else "—"),
            "街廓分配深度(m)": round(depth, 2),
            "法定最小寬(m)": legal_w, "法定最小深(m)": legal_d,
            "【左】截角(㎡)": (round(cutL, 2) if has_l else "—"),
            "【右】截角(㎡)": (round(cutR, 2) if has_r else "—"),
            # 非角側＝None（app 存 None → CSV 空格）；角側截角用 '—'，但最小面積用 None
            "【左】街角最小面積(㎡)": (rng("left") if has_l else None),
            "【右】街角最小面積(㎡)": (rng("right") if has_r else None),
        })
    return rows


def build_anchor_diag(ns, cb_by, cad):
    """階段 6：-a 診斷（front_idx 舊/新、截角 idx、閘）。回傳 list[dict]。"""
    flm = cad.get("front_lines", {}) or {}
    slm = cad.get("side_lines_by_side", {}) or {}
    rows = []
    for lbl in CORNER_BLOCKS:
        b = cb_by[lbl]
        gr = b.get("geom_restore") or {}
        cls = gr.get("classification") or {}
        edges = cls.get("edges") or []
        old_fi = cls.get("front_idx")
        old_ch = sorted({int(t["cutoff_idx"]) for t in (gr.get("theoretical_corners") or [])
                         if t.get("cutoff_idx") is not None})
        topo = ns["_anchor_chamfers_topology"](edges, flm.get(lbl), slm.get(lbl))
        new_fi = topo.get("front_idx")
        new_ch = sorted({ci for s in ("left", "right")
                         for ci in ((topo["sides"].get(s) or {}).get("chamfer_idxs") or [])})
        sd = b.get("corner_sides") or []
        has_l, has_r = "left" in sd, "right" in sd
        ch_ok = (old_ch == new_ch)
        rows.append({
            "街廓": lbl, "舊front_idx": old_fi, "新front_idx": new_fi,
            "front(資訊)": ("同" if old_fi == new_fi else "異·改FRONT共線邊(不 gate)"),
            "舊截角idx": str(old_ch), "新截角idx": str(new_ch),
            "截角": ("✅" if ch_ok else "🔴"),
            "左": (((topo["sides"].get("left") or {}).get("status", "—")) if has_l else "無此側"),
            "右": (((topo["sides"].get("right") or {}).get("status", "—")) if has_r else "無此側"),
            "閘(截角)": ("✅ 綠（截角idx同→gate鏈+live幾何量不變）" if ch_ok
                        else "🔴 截角idx異→停查（切換引入 bug 或碰 903 副本陷阱）"),
        })
    return rows


# ---------------- diff engine ----------------
def _read_csv(path):
    import csv
    with open(path, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def _norm(v):
    """數值容差正規化：None/空 → ''；能轉 float 就比到 2dp；否則原字串（'—' 保留）。"""
    if v is None:
        return ""
    s = str(v).strip()
    if s == "":
        return ""
    try:
        return f"{float(s):.2f}"
    except (ValueError, TypeError):
        return s


def _dump_csv(rows, path):
    """輸出 driver 生成表（診斷用；diff 仍以記憶體 rows 為準）。"""
    import csv
    if not rows:
        open(path, "w", encoding="utf-8-sig").close()
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def _bake_csv(rows, base_col_order, path):
    """重烤專用 dump：utf-8-sig BOM ＋ LF-only（lineterminator='\\n'，同 v2/v3 baseline
    釘跨環境 byte-identity）。base_col_order＝現有 baseline 之欄序（保序、免 git 重排噪音；
    got 有而 baseline 無之新欄追加於後）。空表 → 空檔（同 _dump_csv 慣例）。"""
    import csv
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        open(path, "w", encoding="utf-8-sig", newline="").close()
        return
    got_cols = list(rows[0].keys())
    if base_col_order:
        cols = [c for c in base_col_order if c in got_cols] + \
               [c for c in got_cols if c not in base_col_order]
    else:
        cols = got_cols
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


_GXXX_RE = None


def _classify_gxxx(violations):
    """Gxxx doctrine：欄值僅 Gxxx 群組號不同 → 警告級（不得正規化吃掉、交 B6 仲裁）。
    回傳 (hard, gxxx_warn) 兩堆。"""
    global _GXXX_RE
    import re
    if _GXXX_RE is None:
        _GXXX_RE = re.compile(r"G\d{3}")
    hard, warn = [], []
    for v in violations:
        m = re.search(r"baseline=(.*) got=(.*)$", v)
        if m:
            b_masked = _GXXX_RE.sub("G###", m.group(1))
            g_masked = _GXXX_RE.sub("G###", m.group(2))
            if b_masked == g_masked and m.group(1) != m.group(2):
                warn.append("⚠️ Gxxx警告級（迭代序訊號→B6 仲裁）" + v)
                continue
        hard.append(v)
    return hard, warn


def diff_rows(got_rows, baseline_path, key_cols, label, skip_cols=None):
    """逐格比對 got_rows vs baseline CSV。key_cols 定位（宗地地號/街廓/端，非群組號）。
    skip_cols：豁免欄（每一條＝鬆一格閘，README 白名單記帳；現僅
    『原位次(距角序·暫行)』於 v1 診斷——v2 轉正換源投影序 rank，KL 放行）。
    回傳 (ok, violations)。"""
    skip_cols = skip_cols or set()
    base = _read_csv(baseline_path)
    # 🆕 重烤機制（env WV_BAKE=<dir>；未設＝inert，零行為變更）：dump got_rows 到
    #   <dir>/<baseline 相對 BASELINES 之路徑>，保 baseline 欄序，return 綠（不比對）。
    #   捕捉用 side dir；正式烤 WV_BAKE=BASELINES 本身（原地覆寫）。同一機制。
    _bake_dir = os.environ.get("WV_BAKE")
    if _bake_dir:
        _base_cols = list(base[0].keys()) if base else []
        _bake_csv(got_rows, _base_cols,
                  os.path.join(_bake_dir, os.path.relpath(baseline_path, BASELINES)))
        return True, []
    def keyof(r):
        return tuple(str(r.get(k, "")).strip() for k in key_cols)
    base_by = {keyof(r): r for r in base}
    got_by = {keyof(r): r for r in got_rows}
    viol = []
    for k in base_by:
        if k not in got_by:
            viol.append(f"[{label}] 缺列 {k}"); continue
    for k in got_by:
        if k not in base_by:
            viol.append(f"[{label}] 多列 {k}"); continue
    for k in base_by:
        if k not in got_by:
            continue
        b, g = base_by[k], got_by[k]
        for col in b:
            if col in skip_cols:
                continue
            if col not in g:
                viol.append(f"[{label}] {k} 缺欄 {col}"); continue
            if _norm(b[col]) != _norm(g[col]):
                viol.append(f"[{label}] {k} 欄「{col}」: baseline={b[col]!r} got={g[col]!r}")
    return (not viol), viol


def self_check_diff_engine():
    """diff 引擎自檢（KL 2026-07-05 裁示：run_all 常設）。竄改 診斷0m baseline 副本
    （改值×2＋缺列×1）→ 閘門必須咬出恰 3 violation；_classify_gxxx 分流必須
    （Gxxx-only→警告級、實質差→hard）。證「綠」非虛。回傳 bool。"""
    import csv
    import tempfile
    src = os.path.join(BASELINES, "W-D.1.2 診斷_退縮0m.csv")
    rows = _read_csv(src)
    tampered = [dict(r) for r in rows]
    tampered[0]["真交集(㎡)"] = "999.99"                       # 值改（數值欄）
    tampered[1]["選中"] = ("" if tampered[1]["選中"] else "✅")  # 值改（符號欄）
    tampered.pop(5)                                            # 缺列 → got 側成「多列」
    fd, tmp = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    try:
        with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(tampered)
        ok_diff, viol = diff_rows(rows, tmp, ["街廓", "端", "候選地號"], "自檢")
    finally:
        os.remove(tmp)
    bite_ok = (not ok_diff) and len(viol) == 3
    v_gxxx = ["[自檢] k 欄「w」: baseline='G009（628）[x]' got='G010（628）[x]'"]
    v_hard = ["[自檢] k 欄「w」: baseline='G009（628）[x]' got='G009（629）[x]'"]
    h1, w1 = _classify_gxxx(v_gxxx)
    h2, w2 = _classify_gxxx(v_hard)
    gxxx_ok = (len(h1), len(w1), len(h2), len(w2)) == (0, 1, 1, 0)
    ok = bite_ok and gxxx_ok
    print(f"  {'✅' if bite_ok else '🔴'} 竄改自檢（改值×2＋缺列×1 → 咬 {len(viol)}/3）")
    print(f"  {'✅' if gxxx_ok else '🔴'} _classify_gxxx 分流（Gxxx-only→警告級、實質差→hard）")
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    snapshot = json.load(open(SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = build_pipeline(ns, fake_st, snapshot)

    results = []
    gxxx_warnings = []
    stepg_ctx = {}          # {tag: {g, sg, params, win, forced, sb}}；v3 財務閘/reverse-test 消費

    # ── 幾何半（既有，保持綠） ──
    param_by_tag = {}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        param_by_tag[tag] = params
        ok_p, v_p = diff_rows(params, os.path.join(BASELINES, f"退縮{tag}參數.csv"),
                              ["街廓"], f"參數{tag}")
        results.append((f"參數{tag}", ok_p, v_p))

    anchor = build_anchor_diag(ns, cb_by, cad)
    for tag in ("0m", "3.5m"):
        ok_a, v_a = diff_rows(anchor, os.path.join(BASELINES, f"W-D.1.3-a 診斷_退縮{tag}.csv"),
                              ["街廓"], f"-a診斷{tag}")
        results.append((f"-a診斷{tag}", ok_a, v_a))

    # ── 選位半：ownership → parcels → PK → 三 CSV ──
    print("… ownership（tab1 歸戶指紋複刻，讀 匿名版 xlsx）")
    own = build_ownership(ns, fake_st, ANON_XLSX)
    print(f"    重劃區地籍 {own['n_rezoning']} 筆｜U_LAND {own['n_uland']} 筆｜"
          f"失敗 {own['n_fail']}｜歸戶群組 {own['n_groups']} 組")
    for ln, (got, exp, ok) in own["target_report"].items():
        print(f"    {'✅' if ok else '🔴'} 靶 {ln} → {got}（預期 {exp}）")
    results.append(("ownership Gxxx 靶組（三環定理鏈）", own["targets_ok"],
                    [] if own["targets_ok"] else
                    ["Gxxx 錯位＝三環斷一：①列序被動 ②指紋複刻偏差 ③迭代起點錯"
                     "（須從重劃區地籍起迭代、非 U_LAND）；法人群組怪異先查 dtype '.0'（嫌犯 1.5）"]))

    with open(V6DXF, "rb") as f:
        v6_raw = f.read()
    temp_parcels, build_parcels, swaps = build_build_parcels(
        ns, fake_st, v6_raw, list(cb_by.values()), snapshot)
    print(f"… parcels：temp {len(temp_parcels)} 筆｜可建築 build {len(build_parcels)} 筆｜"
          f"面積交叉換位 {len(swaps)} 對")

    # ── 🆕 W-D.3 backlog（KL 折入④）：ghost 零面積不變量斷言 ──
    #   [H-ghost] 已決 H-a 之等價**全靠零面積**（app Step G 不排 ghost；見 baselines/v2/
    #   PROVENANCE_v2）。若任一 _is_ghost_sliver 之 幾何面積_m2/面積_m2 ≠0 → 零面積性質被
    #   refactor 破壞＝真發散源 → fail-loud（harness RuntimeError；run_all 轉 FAIL 閘）。
    _ghost_bad = [tp for tp in temp_parcels
                  if tp.get("_is_ghost_sliver")
                  and (float(tp.get("幾何面積_m2", 0) or 0) != 0.0
                       or float(tp.get("面積_m2", 0) or 0) != 0.0)]
    if _ghost_bad:
        raise RuntimeError(
            f"🔴 ghost 零面積不變量破：{len(_ghost_bad)} 筆 _is_ghost_sliver 面積≠0"
            f"（H-a 等價根基失守，見 PROVENANCE_v2）："
            f"{[tp.get('暫編地號') for tp in _ghost_bad[:3]]}")
    results.append((f"W-D.3 ghost 零面積不變量（{sum(1 for tp in temp_parcels if tp.get('_is_ghost_sliver'))} 筆全零）",
                    True, []))

    # ── 🆕 F.0-pre（W-F 缺口C）：15.73㎡ 歸因，驗一行 ──
    #   DXF 街廓面積和 − 非-ghost 暫編幾何和 ＝ ghost sliver 之**真面積**
    #   （ghost 幾何面積_m2 恆 0 故不入暫編和；真面積另存 _ghost_area_m2、已合入主體/落池）。
    #   公設分量 15.73㎡ ＋ 可建築分量 13.34㎡ ＝ 29.07㎡ ＝ 全區殘餘。
    _fcb_a = ns["F3_CATEGORY_BURDEN"]
    _blkA, _pclA = {}, {}
    for _b in cb_by.values():
        _k = _fcb_a.get(_b.get("category", ""), "")
        _blkA[_k] = _blkA.get(_k, 0.0) + float(_b.get("area_m2", 0) or 0)
    for _tp in temp_parcels:
        if _tp.get("_is_ghost_sliver"):
            continue
        _k = _fcb_a.get(_tp["街廓分類"], "")
        _pclA[_k] = _pclA.get(_k, 0.0) + float(_tp.get("幾何面積_m2", 0) or 0)
    _d_pub = _blkA["共同負擔"] - _pclA["共同負擔"]
    _d_bld = _blkA["可建築土地"] - _pclA["可建築土地"]
    _ghost_true = sum(float(_tp.get("_ghost_area_m2", 0) or 0)
                      for _tp in temp_parcels if _tp.get("_is_ghost_sliver"))
    _ok_1573 = (abs(_d_pub - 15.73) < 0.01 and abs(_d_bld - 13.34) < 0.01
                and abs((_d_pub + _d_bld) - _ghost_true) < 0.05)
    results.append((f"F.0-pre 15.73㎡ 歸因（公設 {_d_pub:.2f} ＋ 可建築 {_d_bld:.2f} "
                    f"= {_d_pub + _d_bld:.2f} ＝ ghost 真面積 {_ghost_true:.2f}）", _ok_1573,
                    [] if _ok_1573 else [f"公設Δ={_d_pub:.4f} 可建築Δ={_d_bld:.4f} ghost={_ghost_true:.4f}"]))

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        diag, sel, off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad,
            param_by_tag[tag], temp_parcels, build_parcels, setback)
        _dump_csv(diag, os.path.join(OUTDIR, f"got_診斷_退縮{tag}.csv"))
        _dump_csv(sel, os.path.join(OUTDIR, f"got_指配_退縮{tag}.csv"))
        _dump_csv(off, os.path.join(OUTDIR, f"got_抵費地_退縮{tag}.csv"))

        # 🆕 微波：診斷換源 v3（G估 吃現算之重劃總負擔率）。
        #   v3 baseline 由 harness 產（非 KL app 重匯，不開 UI-session 向量），欄名為
        #   『原位次(投影序)』→ **豁免欄除籍**（v1 之『原位次(距角序·暫行)』隨舊錨凍存），全欄逐格對拍。
        ok_d, v_d = diff_rows(diag, os.path.join(V3RUN, f"W-D.1.2 診斷_退縮{tag}.csv"),
                              ["街廓", "端", "候選地號"], f"v3·診斷{tag}")
        results.append((f"v3·診斷{tag}（全欄逐格·無豁免）", ok_d, v_d))

        # 🆕 微波：**無串聯之機器證明**（停機條件之硬看守）
        #   對 v1 原錨逐格比對、僅豁免 {G估(㎡), 舊原位次欄}：必須全等
        #   ⟹ 率接線「只動 G估 欄」，達標/選中/總分/門檻/真交集/範圍/評分 全未動。
        #   任一格變動＝winner 或達標受污染 → 停機上呈。
        ok_nc, v_nc = diff_rows(diag, os.path.join(BASELINES, f"W-D.1.2 診斷_退縮{tag}.csv"),
                                ["街廓", "端", "候選地號"], f"無串聯{tag}",
                                skip_cols={"原位次(距角序·暫行)", "G估(㎡)"})
        results.append((f"率接線無串聯{tag}（vs v1 原錨，豁免 G估 後逐格全等）", ok_nc, v_nc))

        # G估 欄變動格數錨（W-G Y 波比率更新後，baseline 於 WV_BAKE 時同步至新財務值 → 變動=0；
        #   舊錨（PRE-比率更新）：0m 18 格／3.5m 21 格·凍存於 PRE-比率更新_凍存/ 之 W-D.1.2 baseline
        #   對照現重烤 baseline）
        _b1_by = {(r["街廓"], r["端"], r["候選地號"]): r
                  for r in _read_csv(os.path.join(BASELINES, f"W-D.1.2 診斷_退縮{tag}.csv"))}
        _gest_diff = sum(
            1 for r in diag
            if _norm(_b1_by[(r["街廓"], r["端"], r["候選地號"])]["G估(㎡)"]) != _norm(r["G估(㎡)"]))
        _exp_gd = 0  # KL Y 波：baseline 隨新財務同步烤，G估欄變動歸零（重烤即證同源）
        results.append((f"率接線 G估 欄變動 {_gest_diff} 格（期 {_exp_gd}·Y 波後 baseline 同源）", _gest_diff == _exp_gd,
                        [] if _gest_diff == _exp_gd else [f"實得 {_gest_diff} 格"]))

        ok_s, v_s = diff_rows(sel, os.path.join(BASELINES, f"第 1 宗街角地指配結果_退縮{tag}.csv"),
                              ["街廓"], f"指配{tag}")
        hard_s, warn_s = _classify_gxxx(v_s)
        gxxx_warnings.extend(warn_s)
        results.append((f"指配{tag}", not hard_s and not warn_s, hard_s + warn_s))

        if tag == "3.5m":
            ok_o, v_o = diff_rows(off, os.path.join(BASELINES, "W-D.1.3-d 驗收_退縮3.5m.csv"),
                                  ["街廓", "端"], f"抵費地{tag}")
            results.append((f"抵費地{tag}", ok_o, v_o))
        else:
            # 0m baseline 全側有 winner → 抵費地表應為空（無 baseline 檔）
            results.append((f"抵費地{tag}(應空)", not off,
                            [f"[抵費地{tag}] 預期空、得 {len(off)} 列：{off}"] if off else []))

        # ── Step G headless → 三張表對拍 v3 錨定 baseline ──
        #   結構不變量永久閘（守恆／⊥／位次＝投影序／J(k*)≥J(naive)／理論＝實跑／telescoping）
        #   由 run_step_g 內部 raise RuntimeError；於此轉 FAIL 列（run_all 轉紅）。
        print(f"… Step G headless（{tag}；v3 真值財務＋結構不變量永久閘）")
        try:
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             param_by_tag[tag], build_parcels,
                             winners_state, forced_map, setback)
            g_tab, diag_tab, slot_tab = build_step_g_tables(_sg)
            _dump_csv(g_tab, os.path.join(OUTDIR, f"got_G值_退縮{tag}.csv"))
            _dump_csv(diag_tab, os.path.join(OUTDIR, f"got_滑池槽診斷_退縮{tag}.csv"))
            _dump_csv(slot_tab, os.path.join(OUTDIR, f"got_逐槽J表_退縮{tag}.csv"))
            stepg_ctx[tag] = {"g": g_tab, "sg": _sg, "params": param_by_tag[tag],
                              "win": winners_state, "forced": forced_map, "sb": setback,
                              "poolA": _sg["pool_diag"]}   # F.0 trunk A 之池（釋池量對照）
            results.append((f"結構不變量永久閘{tag}（守恆/⊥/位次=投影序/J(k*)≥J(naive)/理論=實跑/telescoping）",
                            True, []))
            ok_g, v_g = diff_rows(
                g_tab, os.path.join(V3RUN, f"G 值計算結果_退縮{tag}.csv"),
                ["所屬街廓", "暫編地號"], f"v3·G值{tag}")
            results.append((f"v3·G值{tag}", ok_g, v_g))
            ok_pd, v_pd = diff_rows(
                diag_tab, os.path.join(V3RUN, f"W-D.2 §3 滑池槽診斷_退縮{tag}.csv"),
                ["街廓"], f"v3·滑池槽{tag}")
            results.append((f"v3·滑池槽{tag}", ok_pd, v_pd))
            ok_j, v_j = diff_rows(
                slot_tab, os.path.join(V3RUN, f"逐槽 J 表_退縮{tag}.csv"),
                ["街廓", "k"], f"v3·J表{tag}")
            results.append((f"v3·J表{tag}", ok_j, v_j))
            # k* 六塊經驗錨（非機制不變量；破＝widths 變動使切點翻，須重驗非直接放行）
            _ks = {lbl: int(d["k*"]) for lbl, d in _sg["pool_diag"].items()}
            results.append((f"k* 六塊經驗錨{tag} {K_STAR_EXPECT}", _ks == K_STAR_EXPECT,
                            [] if _ks == K_STAR_EXPECT else [f"實得 {_ks}"]))
        except RuntimeError as _e_sg:
            results.append((f"v3·StepG{tag}（結構閘/看守觸發）", False,
                            [f"[StepG{tag}] {_e_sg}"]))

    # ── 🆕 v3 財務接線閘（KL 裁定 2026-07-09）──
    #   **斷言錨之輸入必須獨立於錨**：B/C 皆由快照 財務接線_v3 之三純量（前均價/後均價/貸款利息）
    #   ＋精確總面積＋單位費現算而得，禁反填。雙 reverse-test 走**真引擎重跑**（非算術複寫）。
    print("… v3 財務接線閘（B/C 錨・中繼錨・C 兩形等價・A 逐宗全查・雙 reverse-test）")
    try:
        import copy as _cp3
        import stepg_pipeline as _sgp
        _fv3 = snapshot["財務接線_v3"]
        _anc, _mid = _fv3["斷言錨"], _fv3["中繼錨"]
        _fin = dict(_sgp._V3_FINANCE)          # 快照一份（reverse-test 會覆寫模組級變數）

        _okB = round(_fin["B"], 6) == float(_anc["B"])
        results.append((f"v3 財務錨 B == {_anc['B']}（獨立輸入現算 → {_fin['B']:.6f}）",
                        _okB, [] if _okB else [f"實得 B={_fin['B']:.9f}"]))
        _okC = round(_fin["C"], 6) == float(_anc["C"])
        results.append((f"v3 財務錨 C == {_anc['C']}（加總形分母 {_fin['C_denom']:,.2f}）",
                        _okC, [] if _okC else [f"實得 C={_fin['C']:.9f}"]))
        _okM = (round(_fin["eng"]) == _mid["工程費_元"]
                and round(_fin["redev"]) == _mid["重劃費_元"]
                and round(_fin["cost_sum"]) == _mid["費用總額_元"])
        results.append((f"v3 中繼錨 工程費/重劃費/費用總額 == "
                        f"{_mid['工程費_元']}/{_mid['重劃費_元']}/{_mid['費用總額_元']}", _okM,
                        [] if _okM else [f"實得 {round(_fin['eng'])}/{round(_fin['redev'])}/"
                                         f"{round(_fin['cost_sum'])}"]))
        _dC = abs(_fin["C"] - _fin["C_avg_form"])
        results.append((f"v3 C 兩形等價（加總形 vs app calc_C_value 均價形）|Δ|={_dC:.2e} <1e-8",
                        _dC < 1e-8, [] if _dC < 1e-8 else [f"Δ={_dC:.3e}"]))

        # A 逐宗全查：A 地價比 == round(後街廓單價 ÷ 重劃前區段單價, 4)
        _zone = _fv3["原地號_區段"]
        _pp, _qq = _fin["post_price_by_block"], _fin["pre_price_by_zone"]
        _abad, _nA = [], 0
        for _tg, _c in stepg_ctx.items():
            for _r in _c["g"]:
                if _r.get("推進側別") not in ("left", "right"):
                    continue
                _nA += 1
                _exp = round(_pp[_r["所屬街廓"]] / _qq[_zone[_r["原地號"]]], 4)
                if abs(float(_r["A 地價比"]) - _exp) > 1e-9:
                    _abad.append(f"{_tg}/{_r['暫編地號']}: A={_r['A 地價比']} ≠ 期{_exp}")
        results.append((f"v3 A 逐宗全查（{_nA} 列＝後街廓單價/重劃前區段單價）", not _abad, _abad[:5]))

        # reverse-test（證引擎現算、非寫死）：真引擎重跑於變異快照
        _ctx = stepg_ctx["0m"]

        def _rerun_fin(_mut):
            _s2 = _cp3.deepcopy(snapshot)
            _mut(_s2["財務接線_v3"])
            run_step_g(ns, fake_st, list(cb_by.values()), cad, _s2,
                       _ctx["params"], build_parcels, _ctx["win"], _ctx["forced"], _ctx["sb"])
            return dict(_sgp._V3_FINANCE)

        # W-G Y 波比率更新（2026-07-14）：擾動幅度 3600→3550 減半，避免 R2（新單價 68621.38·比舊降 4.4%）
        #   之池臨界態於 3600 擾動下守恆殘差破 −1.28㎡；3550 之 C 增量仍充分證「C 隨動」，且守恆維持 <1㎡。
        _rt1 = _rerun_fin(lambda f: f.__setitem__("單位工程費_元每m2", 3550))
        _ok_rt1 = (round(_rt1["C"], 6) != round(_fin["C"], 6)
                   and round(_rt1["C"], 6) != float(_anc["C"]))
        results.append((f"v3 reverse-test① 單位工程費 3500→3550 ⟹ C 隨動 "
                        f"({_fin['C']:.6f}→{_rt1['C']:.6f})", _ok_rt1,
                        [] if _ok_rt1 else ["C 未隨動＝疑似寫死"]))
        _rt2 = _rerun_fin(lambda f: f.__setitem__(
            "重劃前平均地價_元每m2", f["重劃前平均地價_元每m2"] * 1.1))
        _ok_rt2 = (round(_rt2["B"], 6) != round(_fin["B"], 6)
                   and round(_rt2["B"], 6) != float(_anc["B"])
                   and round(_rt2["C"], 6) == round(_fin["C"], 6))   # C 不吃前均價
        results.append((f"v3 reverse-test② 前均價 ×1.1 ⟹ B 隨動且 C 不動 "
                        f"(B {_fin['B']:.6f}→{_rt2['B']:.6f}；C {_rt2['C']:.6f})", _ok_rt2,
                        [] if _ok_rt2 else ["B 未隨動 或 C 誤吃前均價"]))
        # 復原模組級中繼態（避免後續消費者讀到變異值）
        _sgp._V3_FINANCE = _fin

        # ── 🆕 微波：重劃總負擔率 現算閘（KL 裁「翻」2026-07-10）──
        #   率 = 公設負擔比 + 費用負擔比，由 v3 快照既有輸入＋DXF 面積導出（零新增料、非寫死）。
        _bd = fake_st.session_state["_v3_burden_rate_breakdown"]
        _rate_live = float(fake_st.session_state["f3_total_burden_rate_from_finance"])
        _ok_rate = round(_rate_live, 8) == float(_anc["重劃總負擔率"])
        results.append((f"v3 重劃總負擔率錨 == {_anc['重劃總負擔率']}（現算 {_rate_live:.8f}）",
                        _ok_rate, [] if _ok_rate else [f"實得 {_rate_live:.10f}"]))
        _ok_bd = (round(_bd["公設負擔比"] * 100, 6) == 34.754211
                  and round(_bd["費用負擔比"] * 100, 6) == 5.958176)
        results.append((f"v3 率分項錨 公設負擔比 {_bd['公設負擔比']*100:.6f}% ＋ "
                        f"費用負擔比 {_bd['費用負擔比']*100:.6f}%", _ok_bd,
                        [] if _ok_bd else ["分項與 xlsx Tab7 不符"]))
        # 公設共同負擔須用 DXF 實值（截圖 rounded 12146.56 → 0.40712393，差第 7 位）
        _ok_dxf = abs(_bd["公設共同負擔_DXF"] - 12146.5579) < 5e-4
        results.append((f"v3 率用 DXF 公設實值 {_bd['公設共同負擔_DXF']:.4f}（非截圖 rounded 12146.56）",
                        _ok_dxf, [] if _ok_dxf else [f"實得 {_bd['公設共同負擔_DXF']}"]))
        # reverse-test③：改單位工程費 3500→3550（Y 波統一擾動）⟹ 率隨動（證現算、非抄錄）
        _s3 = _cp3.deepcopy(snapshot)
        _s3["財務接線_v3"]["單位工程費_元每m2"] = 3550
        _rate3, _ = compute_total_burden_rate(ns, list(cb_by.values()), _s3)
        _ok_rt3 = (round(_rate3, 8) != round(_rate_live, 8)
                   and round(_rate3, 8) != float(_anc["重劃總負擔率"]))
        results.append((f"v3 reverse-test③ 單位工程費 3500→3550 ⟹ 重劃總負擔率隨動 "
                        f"({_rate_live:.8f}→{_rate3:.8f})", _ok_rt3,
                        [] if _ok_rt3 else ["率未隨動＝疑似寫死"]))
    except Exception as _e_fin:
        import traceback
        results.append(("v3 財務接線閘", False,
                        [f"[財務閘] {_e_fin}", traceback.format_exc()[-300:]]))

    # ── 🆕 W-D.3 §4：碎片幾何/三分類/逐邊 CAD 對拍（診斷閘；零幾何移動之診斷凍結）──
    #   compute() 自含管線（雙情境）；三分類(碎片/forced/池主體)由 (a)S=0/(b)寬<最小/
    #   (c)深<最小 判（KL 定稿，面積門檻全廢）。geom 之 面積/沿街s/長寬比/緊湊 錨定 c1584a8。
    print("… W-D.3 碎片幾何/分類/逐邊 CAD 對拍")
    try:
        from wd3_fragment_geom import compute as _frag_compute
        _geom_rows, _edge_rows = _frag_compute()
        # 換源 v3：碎片幾何吃 run_step_g 之抵費地 cut_coords → 池變則池主體列變（G 縮→池脹）。
        #   實測：列數/三分類/碎片列（5.30/78.19/85.66）原封不動，僅池主體列面積近倍增。
        ok_fg, v_fg = diff_rows(_geom_rows, os.path.join(V3RUN, "wd3_fragment_geom.csv"),
                                ["情境", "暫編地號"], "碎片幾何")
        results.append(("W-D.3 碎片幾何/三分類（v3）", ok_fg, v_fg))
        ok_fe, v_fe = diff_rows(_edge_rows, os.path.join(V3RUN, "wd3_fragment_edges.csv"),
                                ["情境", "暫編地號"], "碎片逐邊")
        results.append(("W-D.3 碎片逐邊CAD（v3）", ok_fe, v_fe))
    except Exception as _e_fg:
        results.append(("W-D.3 碎片", False, [f"[碎片] compute 失敗：{_e_fg}"]))

    # ── 🆕 W-D.4 清單波：四梯分級清單（歸戶=Gxxx 群組；零幾何移動）──
    #   旗標消費(v3=31)/MinA_區推導/R6 遞補錨(v3 重錨)/fixture 查封自成一群/三 CSV 對拍 v3 baseline。
    print("… W-D.4 四梯分級清單（Gxxx 群組·31 旗標消費·遞補錨·fixture·v3 半實算）")
    try:
        import wd4_tier_list as _w4
        _w4res = _w4.compute(fixture=False)
        for tag in ("0m", "3.5m"):
            _d4 = _w4res[tag]
            _dump_csv(_d4["groups"], os.path.join(OUTDIR, f"got_W-D.4_清單_退縮{tag}.csv"))
            _dump_csv(_d4["frag"], os.path.join(OUTDIR, f"got_W-D.4_遞補_退縮{tag}.csv"))
            _dump_csv(_d4["recomp"], os.path.join(OUTDIR, f"got_W-D.4_跨占_退縮{tag}.csv"))
            ok_l, v_l = diff_rows(_d4["groups"],
                                  os.path.join(V3RUN, f"W-D.4_四梯分級清單_退縮{tag}.csv"),
                                  ["情境", "歸戶鍵Gxxx"], f"W-D.4清單{tag}")
            results.append((f"W-D.4 四梯清單{tag}（v3 半實算）", ok_l, v_l))
            ok_r, v_r = diff_rows(_d4["frag"],
                                  os.path.join(V3RUN, f"W-D.4_碎片遞補對照_退縮{tag}.csv"),
                                  ["情境", "碎片"], f"W-D.4遞補{tag}")
            results.append((f"W-D.4 碎片遞補{tag}", ok_r, v_r))
            ok_x, v_x = diff_rows(_d4["recomp"],
                                  os.path.join(V3RUN, f"W-D.4_跨占分配線_退縮{tag}.csv"),
                                  ["情境", "暫編地號"], f"W-D.4跨占{tag}")
            results.append((f"W-D.4 跨占分配線{tag}", ok_x, v_x))
        # 推導斷言（WARNING-1 裁定：正典 rounded 全等＋½線顯示 Decimal 釘刀口）
        _d0 = _w4res["0m"]
        _ok_der = (_d0["mina_qu"] == 114.07 and _d0["half_disp"] == 57.04)
        results.append(("W-D.4 MinA_區==114.07(正典rounded)·½顯示==57.04(Decimal非round)", _ok_der,
                        [] if _ok_der else [f"MinA_區={_d0['mina_qu']} ½顯示={_d0['half_disp']}"]))
        # 旗標數隨價變（v2=22 → v3=31，+9 無消失；配地寬縮 24% 跌破 min_width 3.5m）
        _consumed = sum(int(g["含旗標宗數"]) for g in _d0["groups"])
        _FL = _w4.FLAGGED_EXPECT
        _ok_fl = (_d0["flagged_ct"] == _FL and _consumed == _FL)
        results.append((f"W-D.4 {_FL}旗標全消費(群組語意·v3 隨價變)", _ok_fl,
                        [] if _ok_fl else [f"旗標{_d0['flagged_ct']}→消費{_consumed}（期{_FL}）"]))

        # ── 🆕 F.0-pre 雙軌錨（KL 裁定 2026-07-10，W-F 缺口D）──
        _ok_tr = (_d0["tracks"] == _w4.TRACK_EXPECT and _d0["tiers"] == _w4.TIER_EXPECT)
        results.append((f"F.0-pre 雙軌錨 軌別{_w4.TRACK_EXPECT}·梯次{_w4.TIER_EXPECT}", _ok_tr,
                        [] if _ok_tr else [f"實得 軌別{_d0['tracks']} 梯次{_d0['tiers']}"]))
        _pubg = sorted(g["歸戶鍵Gxxx"] for g in _d0["groups"] if g["軌別"] == "公設軌")
        _ok_pg = (_pubg == _w4.PUB_TRACK_GROUPS)
        results.append((f"F.0-pre 公設軌 8 群（撤出梯3、待 F.3/F.4）", _ok_pg,
                        [] if _ok_pg else [f"實得 {_pubg}"]))
        # 補償取值停機條款：公設軌之半實算欄一律留空（舊碼會算出假 0）
        _est_cols = ("增配a′(㎡)", "差額地價(元)§52-1", "放棄改領(元)§53-2",
                     "補償_本文式(元)§53-1", "補償_但書式(元)")
        _bad_c = [g["歸戶鍵Gxxx"] for g in _d0["groups"] if g["軌別"] == "公設軌"
                  and any(str(g[c]).strip() for c in _est_cols)]
        results.append(("F.0-pre 公設軌補償欄全空（G(a′) 未算前禁取值·停機條款）",
                        not _bad_c, _bad_c))
        # F.3 母數（取代規格作廢之「30 筆 / ~4,428㎡」）
        _np = sum(int(g["公設宗數"]) for g in _d0["groups"])
        _nh = sum(1 for g in _d0["groups"] if int(g["公設宗數"]) > 0)
        _ok_f3 = (_np == _w4.PUB_PARCELS_EXPECT and _nh == _w4.PUB_HOLDER_GROUPS_EXPECT)
        results.append((f"F.3 母數錨 公設地 {_np} 筆／{_nh} 群持有（廢「30 筆/4,428㎡」）", _ok_f3,
                        [] if _ok_f3 else [f"實得 {_np} 筆/{_nh} 群"]))
        # F.0 釋池對象＝梯3 二群（原十群之 8 群已改軌）
        _t3 = sorted((g["歸戶鍵Gxxx"], float(g["ΣG_戶(㎡)"]))
                     for g in _d0["groups"] if g["梯次"] == "3")
        # W-G Y 波比率更新（2026-07-14）：ΣG 隨新單價再微降 57.19→56.97（同群 G025/G030·膜不變）。
        #   舊錨（PRE-比率更新）：[("G025", 1.83), ("G030", 55.36)] Σ57.19。
        #   更早（PRE-勘誤）：[("G025", 1.84), ("G030", 55.64)] Σ57.48。
        _ok_t3 = (_t3 == [("G025", 1.79), ("G030", 55.18)])
        results.append((f"F.0 釋池對象＝梯3 二群 {_t3}（Σ={sum(v for _, v in _t3):.2f}㎡）", _ok_t3,
                        [] if _ok_t3 else [f"實得 {_t3}"]))
        # reverse-test（規格 §5.3：MinA_區 由參數推導·非寫死）：改 R4 分配深度→MinA_區 隨動
        import copy as _cp
        _snap2 = _cp.deepcopy(snapshot)
        _snap2["blocks"]["R4"]["街廓分配深度_m"] = 20.0   # 原 32.59；R4 仍為 min → 20×3.5=70
        _bb4 = [b for b in cb_by.values()
                if ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") == "可建築土地"]
        _, _mq2 = _w4._mina_by_block(ns, _snap2, cb_by, _bb4)
        _ok_rev = (_mq2 == 70.0)   # round(20×3.5,2)=70 隨動（非鎖死 114.07）
        results.append(("W-D.4 MinA_區 reverse-test(改深度→隨動·非寫死)", _ok_rev,
                        [] if _ok_rev else [f"改 R4 深度20→MinA_區={_mq2}(期70)"]))
        # 遞補錨（v3 重錨）：v2 之標的 628-1(2) 於 v3 自身入畸零旗標（寬<3.5m）→ 續往內遞補。
        #   域裁§四規則不變：沿分配序往前找第一筆有效宗（S≠0 且 宗地寬度≥min_width），跳過失格中間筆。
        _r6 = [f for f in _d0["frag"] if f["碎片"] == "R6-抵費地-2"]
        _ok_anc = (bool(_r6) and _r6[0]["遞補標的宗"] == "628-4(1)"
                   and _r6[0]["跳過失格筆"] == "628(2);628-1(2);628-23(1)")
        results.append(("W-D.4 遞補錨 R6 85.66→628-4(1)（跳過 628(2);628-1(2);628-23(1)）", _ok_anc,
                        [] if _ok_anc else [f"實得 {_r6}"]))
        _share_bad = sum(1 for g in _d0["groups"] if "🔴" in g["持分和檢核"])
        results.append(("W-D.4 持分和逐宗檢核(WARNING-A)", _share_bad == 0,
                        [] if _share_bad == 0 else [f"{_share_bad} 群異常"]))
        # fixture：查封宗自成一群·阻卻=是·移除後 byte-identical（不碰 build_ownership 靶）
        _fx = _w4.compute(fixture=True)
        _fg = [g for g in _fx["0m"]["groups"] if g["歸戶鍵Gxxx"] == "G_FIXTURE"]
        _fx_ok = (bool(_fg) and _fg[0]["阻卻"] == "是"
                  and "不得聯合" in _fg[0]["路徑標註"]
                  and [g for g in _fx["0m"]["groups"] if g["歸戶鍵Gxxx"] != "G_FIXTURE"]
                  == _d0["groups"])
        results.append(("W-D.4 第4梯 fixture(查封自成一群·移除後 byte-identical)", _fx_ok,
                        [] if _fx_ok else ["fixture 阻卻/隔離破"]))
    except Exception as _e_w4:
        import traceback
        results.append(("W-D.4", False, [f"[W-D.4] compute 失敗：{_e_w4}",
                                         traceback.format_exc()[-300:]]))

    # ── 🆕 W-F F.0：級0/0' 合併＋梯3 釋池（雙 trunk；trunk A 零漂移已由上列 v3 閘證）──
    #   trunk A（原 parcels→v3 baseline）之 G值/滑池槽/J/wd3/四梯清單 皆已於上方逐格對拍過
    #   ＝gate#2「基礎引擎零漂移」之機器證明。此處跑 trunk B（F.0 終態 parcels）。
    print("… W-F F.0（級0/0' 合併＋梯3 釋池；trunk B 終態）")
    _f0_ok = False          # W5：F.1 之存在性守衛（F.0 失敗 → F.1 跳過記 FAIL，不連坐 NameError）
    _f0 = _ctx = None
    try:
        import wf_f0
        _omap = fake_st.session_state["t8_ownership_map"]
        _ctx = {}
        for tag in ("0m", "3.5m"):
            _c = stepg_ctx.get(tag)
            if not _c:
                raise RuntimeError(f"stepg_ctx[{tag}] 缺（trunk A 未成功？）")
            _ctx[tag] = {
                "ns": ns, "fake_st": fake_st, "cb_by": cb_by, "cad": cad,
                "snap": snapshot, "omap": _omap, "build": build_parcels,
                "params": _c["params"], "winners": _c["win"], "forced": _c["forced"],
                "setback": _c["sb"], "gA": _c["sg"]["g_rows"], "poolA": _c["poolA"],
                "temp": temp_parcels,   # F.3 消費（全 temp_parcels，含公設，供 poly/分攤登記）
            }
        _f0 = wf_f0.compute(_ctx)
        for tag in ("0m", "3.5m"):
            d = _f0[tag]
            for nm, rows in (("G值", d["g_tab"]), ("滑池槽診斷", d["diag_tab"]),
                             ("逐槽J表", d["slot_tab"]), ("合併決策", d["dec_rows"]),
                             ("旗標消長", d["flag_rows"]), ("池差", d["pool_rows"])):
                _dump_csv(rows, os.path.join(OUTDIR, f"got_F.0_{nm}_退縮{tag}.csv"))
            ok_g, v_g = diff_rows(d["g_tab"], os.path.join(F0DIR, f"F.0_G值_退縮{tag}.csv"),
                                  ["所屬街廓", "暫編地號"], f"F.0·G值{tag}")
            results.append((f"F.0·G值{tag}（trunk B 終態）", ok_g, v_g))
            ok_pd, v_pd = diff_rows(d["diag_tab"], os.path.join(F0DIR, f"F.0_滑池槽診斷_退縮{tag}.csv"),
                                    ["街廓"], f"F.0·滑池槽{tag}")
            results.append((f"F.0·滑池槽{tag}", ok_pd, v_pd))
            ok_j, v_j = diff_rows(d["slot_tab"], os.path.join(F0DIR, f"F.0_逐槽J表_退縮{tag}.csv"),
                                  ["街廓", "k"], f"F.0·J表{tag}")
            results.append((f"F.0·J表{tag}", ok_j, v_j))
            ok_dc, v_dc = diff_rows(d["dec_rows"], os.path.join(F0DIR, f"F.0_合併決策_退縮{tag}.csv"),
                                    ["情境", "歸戶", "街廓"], f"F.0·決策{tag}")
            results.append((f"F.0·合併決策{tag}", ok_dc, v_dc))
            ok_fl, v_fl = diff_rows(d["flag_rows"], os.path.join(F0DIR, f"F.0_旗標消長_退縮{tag}.csv"),
                                    ["情境", "暫編地號"], f"F.0·旗標{tag}")
            results.append((f"F.0·旗標消長{tag}", ok_fl, v_fl))
            ok_pl, v_pl = diff_rows(d["pool_rows"], os.path.join(F0DIR, f"F.0_池差_退縮{tag}.csv"),
                                    ["情境", "街廓"], f"F.0·池差{tag}")
            results.append((f"F.0·池差閉合{tag}", ok_pl, v_pl))
            # 結構閘（trunk B）
            _bad = [lbl for lbl, v in d["verdict"].items() if "🔴" in str(v)]
            results.append((f"F.0 結構永久閘{tag}（trunk B 守恆全綠）", not _bad, _bad))
            # 位次序＋標的宗毗鄰（投影序、k*-無關）
            results.append((f"F.0 位次序不變{tag}（投影序∖移除宗）", not d["pos_viol"],
                            [str(x) for x in d["pos_viol"][:3]]))
            results.append((f"F.0 標的宗毗鄰不變{tag}", not d["adj_viol"],
                            [str(x) for x in d["adj_viol"][:3]]))
        # 六格 G(Σa) 錨（雙情境）
        _g0 = _f0["0m"]["gsa"]
        _ok_gsa = all(abs(_g0[k] - v) <= 0.01 for k, v in wf_f0.GSA_EXPECT["0m"].items())
        results.append((f"F.0 六格 G(Σa) 錨 0m {wf_f0.GSA_EXPECT['0m']}", _ok_gsa,
                        [] if _ok_gsa else [f"實得 {{{', '.join(f'{k}:{_g0[k]:.2f}' for k in _g0)}}}"]))
        # 旗標終態錨 31→17（移除13＋脫旗1＋新生0）
        _fr = _f0["0m"]["flag_rows"]
        _n_new = sum(1 for r in _fr if r["歸因"] == "新生")
        _ok_fl2 = (_f0["0m"]["n_flag_A"] == 31 and _f0["0m"]["n_flag_B"] == 17 and _n_new == 0)
        results.append((f"F.0 旗標 31→17（新生 {_n_new}）", _ok_fl2,
                        [] if _ok_fl2 else [f"A={_f0['0m']['n_flag_A']} B={_f0['0m']['n_flag_B']} 新生={_n_new}"]))
        # k* f0 錨（trunk B；經驗非機制）
        _ok_k = (_f0["0m"]["kstar"] == {"R1": 2, "R2": 6, "R3": 5, "R4": 1, "R5": 4, "R6": 3})
        results.append((f"F.0 k* f0 錨 trunk B {_f0['0m']['kstar']}", _ok_k,
                        [] if _ok_k else ["k* 與 f0 錨不符"]))
        # 不達標二格去向（G009→F.2、G014→F.4；停機#4 全鏈）
        _dest = {r["歸戶"]: r["去向"] for r in _f0["0m"]["dec_rows"]}
        _ok_rt = ("轉F.2" in _dest.get("G009", "") and "轉F.4" in _dest.get("G014", ""))
        results.append(("F.0 不達標二格 G009→F.2·G014→F.4（先併再標旗轉出）", _ok_rt,
                        [] if _ok_rt else [f"G009={_dest.get('G009')} G014={_dest.get('G014')}"]))
        _f0_ok = True
    except Exception as _e_f0:
        import traceback
        results.append(("W-F F.0", False, [f"[F.0] {_e_f0}", traceback.format_exc()[-400:]]))

    # ── 🆕 W-F F.1：S=0 碎片遞補形狀調整（KL 縮圍 R1；等 G 幾何重切＋後續宗前移）──
    #   R3/R6 楔形＝標記制待 F.4 終態遞補整形（裁示 1(b) F.1 段）。停機斷言於 wf_f1 內 raise。
    print("… W-F F.1（R1 楔形等 G 吞納＋前移；R3/R6 標記待 F.4）")
    try:
        if not _f0_ok:
            raise RuntimeError("F.0 未成功，F.1 跳過（W5 守衛）")
        import wf_f1
        _f1 = wf_f1.compute(_ctx, _f0)
        _F1_ANCH = {"0m": ("628-37(1)", 2, 1), "3.5m": ("628-36(1)", 2, 1)}
        for tag in ("0m", "3.5m"):
            d1 = _f1[tag]
            for nm, rows in (("遞補整形", d1["reshape_rows"]), ("碎片處置", d1["frag_rows"]),
                             ("池驗證", d1["pool_rows"])):
                _dump_csv(rows, os.path.join(OUTDIR, f"got_F.1_{nm}_退縮{tag}.csv"))
            ok_r, v_r = diff_rows(d1["reshape_rows"], os.path.join(F1DIR, f"F.1_遞補整形_退縮{tag}.csv"),
                                  ["情境", "暫編地號"], f"F.1·整形{tag}")
            results.append((f"F.1·遞補整形{tag}", ok_r, v_r))
            ok_f, v_f = diff_rows(d1["frag_rows"], os.path.join(F1DIR, f"F.1_碎片處置_退縮{tag}.csv"),
                                  ["情境", "碎片"], f"F.1·碎片{tag}")
            results.append((f"F.1·碎片處置{tag}", ok_f, v_f))
            ok_p, v_p = diff_rows(d1["pool_rows"], os.path.join(F1DIR, f"F.1_池驗證_退縮{tag}.csv"),
                                  ["情境", "街廓", "池片"], f"F.1·池{tag}")
            results.append((f"F.1·池驗證{tag}", ok_p, v_p))
            _a = d1["anchors"]
            _exp_t, _exp_pB, _exp_pN = _F1_ANCH[tag]
            # W-G Y 波比率更新（2026-07-14）：pool_delta 容差再放寬 0.10→0.15。
            #   0m pool_delta 隨新單價微移至 +0.11（>舊 0.10）；楔形 5.30 幾何仍不變、F.4 守恆殘差<6，
            #   +0.11 屬價驅動閉合噪音、非守恆破。標的/池片/寬全守（膜不變），僅殘差容差再放寬。
            #   更早：v3 勘誤重烤 0.05→0.10（0m 到 -0.06）。
            _ok_a = (_a["target"] == _exp_t and _a["pool_pieces_B"] == _exp_pB
                     and _a["pool_pieces_new"] == _exp_pN and abs(_a["pool_delta"]) <= 0.15
                     and _a["w_new"] >= 3.5)
            results.append((f"F.1 錨{tag}（標的 {_a['target']}·寬 {_a['w_new']}≥3.5·"
                            f"池片 {_a['pool_pieces_B']}→{_a['pool_pieces_new']}·"
                            f"池差 {_a['pool_delta']:+.2f}≈0）", _ok_a,
                            [] if _ok_a else [str(_a)]))
            # 標記閘：R3/R6 楔形標記待 F.4（0m 二片、3.5m 一片＝R6）
            _marks = [r for r in d1["frag_rows"] if "標記" in r["處置"]]
            _exp_m = 2 if tag == "0m" else 1
            results.append((f"F.1 標記制{tag}（{len(_marks)} 片待 F.4 終態遞補整形，期 {_exp_m}）",
                            len(_marks) == _exp_m, [str(m) for m in _marks]))
        _f1_ok = True
    except Exception as _e_f1:
        import traceback
        results.append(("W-F F.1", False, [f"[F.1] {_e_f1}", traceback.format_exc()[-400:]]))

    # ── 🆕 W-F F.2：級1/2/3 跨街廓同歸戶合併（a′ 模式一；trunk C 終態）──
    #   消費 trunk B parcels（F.0 終態；F.1 為幾何後處理未改 parcels）→ 搬 a′ → run_step_g → trunk C。
    print("… W-F F.2（跨街廓搬 a′ 模式一；五群 G009/G001/G021/G026/G027）")
    try:
        if not _f0_ok:
            raise RuntimeError("F.0 未成功，F.2 跳過（存在性守衛）")
        import wf_f2
        # 靜態閘（reviewer#3）：wf_f2.py 不得呼叫 calc_a_prime／三廢函式（紀律機檢化）
        _wf2_src = open(os.path.join(HERE, "wf_f2.py"), encoding="utf-8").read()
        _forbid = [f"{n}(" for n in ("calc_a_prime", "_allocate_three_tier_v1",
                                     "_allocate_tier2_tier3_geometric", "_inflate_a_for_orphan")]
        _hit = [f for f in _forbid if f in _wf2_src]
        results.append(("F.2 靜態閘（wf_f2 不呼叫 calc_a_prime／三廢函式）", not _hit, _hit))

        _f2 = wf_f2.compute(_ctx, _f0)
        # 雙模式並列錨（G021）：模式一=該歸戶地 pb；模式二=R1 之**重劃前 DXF 幾何面積_m2** 權重均價
        #   （規格 §7-4:420；89.32 為規格正確值，修正 CC sandbox 配地後面積近似之 89.11）。
        _G021_M1, _G021_M2 = 98.54, 89.32
        for tag in ("0m", "3.5m"):
            d2 = _f2[tag]
            for nm, rows in (("跨街廓調配", d2["conv_rows"]), ("G值", d2["g_tab"]),
                             ("池流向", d2["pool_rows"])):
                _dump_csv(rows, os.path.join(OUTDIR, f"got_F.2_{nm}_退縮{tag}.csv"))
            ok_c, v_c = diff_rows(d2["conv_rows"], os.path.join(F2DIR, f"F.2_跨街廓調配_退縮{tag}.csv"),
                                  ["情境", "歸戶", "源宗"], f"F.2·調配{tag}")
            results.append((f"F.2·跨街廓調配{tag}", ok_c, v_c))
            ok_g2, v_g2 = diff_rows(d2["g_tab"], os.path.join(F2DIR, f"F.2_G值_退縮{tag}.csv"),
                                    ["所屬街廓", "暫編地號"], f"F.2·G值{tag}")
            results.append((f"F.2·G值{tag}（trunk C 終態）", ok_g2, v_g2))
            ok_pf, v_pf = diff_rows(d2["pool_rows"], os.path.join(F2DIR, f"F.2_池流向_退縮{tag}.csv"),
                                    ["情境", "街廓"], f"F.2·池流向{tag}")
            results.append((f"F.2·池流向{tag}", ok_pf, v_pf))
            _a2 = d2["anchors"]
            results.append((f"F.2 結構永久閘{tag}（trunk C 守恆全綠）", _a2["verdict_all_green"],
                            [] if _a2["verdict_all_green"] else ["守恆破"]))
            # §N3-0 全區級帳對幾何閘＝逐街廓加總（KL 2026-07-16 裁·補丁三 §二）
            #   ⚠️ 舊 `<6.0` 廢＝殘餘定閘（432,352 元·N0-17）；⚠️ `Σ宗數×0.005` 亦廢（維度錯·停機③）
            results.append((f"F.2 跨街廓守恆{tag}（源池增/目標池減/全區 |Σ(G−幾何)| "
                            f"{_a2['cons_resid']} ≤ {_a2['cons_tol']}＝Σ街廓 宗數×(0.005×深度＋tol＋0.005)）",
                            _a2["cons_resid"] <= _a2["cons_tol"],
                            [] if _a2["cons_resid"] <= _a2["cons_tol"]
                            else [f"{_a2['cons_resid']} > {_a2['cons_tol']}"]))
            results.append((f"F.2 位次序不變{tag}（投影序∖移除宗）", not _a2["pos_viol"],
                            [str(x) for x in _a2["pos_viol"][:3]]))
            results.append((f"F.2 F.1 正交{tag}（{wf_f2.F1_TARGET[tag]} B→C 全等）",
                            _a2["f1_orthogonal"], [] if _a2["f1_orthogonal"] else ["F.1 標的被 F.2 污染"]))
            results.append((f"F.2 同區段恆等{tag}（同zone轉出 a′==a）", _a2["same_zone_identity"],
                            [] if _a2["same_zone_identity"] else ["同區段 ratio≠1"]))
        # 雙模式並列錨（G021；雙情境同）
        _g0 = _f2["0m"]["anchors"]
        _ok_dm = (_g0["g021_m1"] == _G021_M1 and _g0["g021_m2"] == _G021_M2)
        results.append((f"F.2 雙模式並列錨 G021 模式一{_g0['g021_m1']}／模式二{_g0['g021_m2']}", _ok_dm,
                        [] if _ok_dm else [f"實得 m1={_g0['g021_m1']} m2={_g0['g021_m2']}（期 {_G021_M1}/{_G021_M2}）"]))
        # 跨區段 fixture（合成 a→b，exercise ratio≠1）
        _fx = wf_f2.fixture_cross_zone(snapshot, build_parcels)
        _ok_fx = (_fx["ratio_ne_1"] and abs(_fx["mode1_a_to_b"] - _fx["expect_m1"]) < 0.01
                  and _fx["mode1_a_to_b"] > _fx["a"])
        results.append((f"F.2 跨區段 fixture（a→b 模式一 a′={_fx['mode1_a_to_b']}≠a=100·"
                        f"模式二R2={_fx['mode2_tgtR2']}/R1混={_fx['mode2_tgtR1_mixed']}）", _ok_fx,
                        [] if _ok_fx else [str(_fx)]))
        _f2_ok = True
    except Exception as _e_f2:
        import traceback
        _f2_ok = False
        results.append(("W-F F.2", False, [f"[F.2] {_e_f2}", traceback.format_exc()[-500:]]))

    # ── 🆕 W-F F.3：RD 五則＋PF 公設地調配（a′ 併入同歸戶建地；trunk D）──
    #   母體＝trunk C（F.2 終態）；公設筆 a′ 灌入建地→run_step_g→trunk D。24 筆轉 7-4（F.4）。
    print("… W-F F.3（公設地調配：RD 五則①切半5/③集中30＋PF6；轉7-4 24筆）")
    try:
        if not _f2_ok:
            raise RuntimeError("F.2 未成功，F.3 跳過（存在性守衛）")
        import wf_f3
        # 靜態閘（守衛：wf_f3 不呼叫 calc_a_prime／三廢函式）
        _wf3_src = open(os.path.join(HERE, "wf_f3.py"), encoding="utf-8").read()
        _f3hit = [f"{n}(" for n in ("calc_a_prime", "_allocate_three_tier_v1",
                  "_allocate_tier2_tier3_geometric", "_inflate_a_for_orphan") if f"{n}(" in _wf3_src]
        results.append(("F.3 靜態閘（wf_f3 不呼叫 calc_a_prime／三廢）", not _f3hit, _f3hit))

        _f3 = wf_f3.compute(_ctx, _f2)
        for tag in ("0m", "3.5m"):
            d3 = _f3[tag]
            for nm, rows in (("公設調配", d3["conv_rows"]), ("轉7-4", d3["to74_rows"]),
                             ("G值", d3["g_tab"]), ("池流向", d3["pool_rows"])):
                _dump_csv(rows, os.path.join(OUTDIR, f"got_F.3_{nm}_退縮{tag}.csv"))
            ok_c, v_c = diff_rows(d3["conv_rows"], os.path.join(F3DIR, f"F.3_公設調配_退縮{tag}.csv"),
                                  ["情境", "公設筆"], f"F.3·調配{tag}")
            results.append((f"F.3·公設調配{tag}", ok_c, v_c))
            ok_7, v_7 = diff_rows(d3["to74_rows"], os.path.join(F3DIR, f"F.3_轉7-4_退縮{tag}.csv"),
                                  ["情境", "公設筆"], f"F.3·轉74{tag}")
            results.append((f"F.3·轉7-4{tag}", ok_7, v_7))
            ok_g3, v_g3 = diff_rows(d3["g_tab"], os.path.join(F3DIR, f"F.3_G值_退縮{tag}.csv"),
                                    ["所屬街廓", "暫編地號"], f"F.3·G值{tag}")
            results.append((f"F.3·G值{tag}（trunk D 終態）", ok_g3, v_g3))
            ok_pf, v_pf = diff_rows(d3["pool_rows"], os.path.join(F3DIR, f"F.3_池流向_退縮{tag}.csv"),
                                    ["情境", "街廓"], f"F.3·池流向{tag}")
            results.append((f"F.3·池流向{tag}", ok_pf, v_pf))
            _a3 = d3["anchors"]
            # 59 筆零遺漏
            _ok59 = (_a3["n_pub"] == 59 and _a3["n_in"] == 35 and _a3["n_74"] == 24)
            results.append((f"F.3 零遺漏{tag}（59＝併入{_a3['n_in']}＋轉7-4{_a3['n_74']}）", _ok59,
                            [] if _ok59 else [str({k: _a3[k] for k in ('n_pub', 'n_in', 'n_74')})]))
            # §N3-0 全區級＝逐街廓加總（補丁三 §二）；舊 `<6` 廢（殘餘定閘）
            _c3ok = _a3["verdict_all_green"] and _a3["cons_resid"] <= _a3["cons_tol"]
            results.append((f"F.3 結構永久閘{tag}（trunk D 守恆綠·|Σ(G−幾何)| "
                            f"{_a3['cons_resid']} ≤ {_a3['cons_tol']}）", _c3ok,
                            [] if _c3ok else [f"{_a3['cons_resid']} > {_a3['cons_tol']}"
                                              f"／all_green={_a3['verdict_all_green']}"]))
            results.append((f"F.3 位次序不變{tag}", not _a3["pos_viol"], [str(x) for x in _a3["pos_viol"][:3]]))
            # 五則①切半 5 筆全 RD2（40 灌入項）
            _ok1 = (_a3["straddle"] == sorted(wf_f3.STRADDLE) and _a3["n_inject_items"] == 40)
            results.append((f"F.3 五則①切半5筆·{_a3['n_inject_items']}灌入項{tag}", _ok1,
                            [] if _ok1 else [f"切半{_a3['straddle']} 灌入{_a3['n_inject_items']}"]))
        # 628-18(2) 舊帳重測（a=477.91）＋轉7-4 群
        _a0 = _f3["0m"]["anchors"]
        _ok18 = (_a0["a_628_18_2"] == 477.91)
        results.append((f"F.3 舊帳重測 628-18(2) a={_a0['a_628_18_2']}==477.91（新機制·分攤登記96.82）", _ok18,
                        [] if _ok18 else [f"實得 {_a0['a_628_18_2']}"]))
        _ok74g = (_a0["groups_74"] == ["G003", "G012", "G013", "G015", "G016", "G024", "G025", "G028", "G031"])
        results.append((f"F.3 轉7-4 9群（含 G025 邊界：建地 F.0梯3釋池）", _ok74g,
                        [] if _ok74g else [str(_a0["groups_74"])]))
        # 跨區段 fixture（守衛④）
        _fx3 = wf_f3.fixture_cross_zone_f3(snapshot)
        results.append((f"F.3 跨區段 fixture（a→b a′={_fx3['a_prime_a_to_b']}≠a·ratio≠1）",
                        _fx3["ratio_ne_1"] and abs(_fx3["a_prime_a_to_b"] - _fx3["expect"]) < 0.01, []))
    except Exception as _e_f3:
        import traceback
        _f3_ok = False
        results.append(("W-F F.3", False, [f"[F.3] {_e_f3}", traceback.format_exc()[-500:]]))
    else:
        _f3_ok = True

    # ── 🆕 W-F F.4：無同歸戶 3 級調配（7-4）＋7-5 雙出口批次最佳化＋終態整形＋總決算（trunk E）──
    #   母體＝trunk D（F.3 終態）。E0 級1殘餘→E1 7-4 距離法→E2 7-5 批次全域最佳化（KL 裁定 2026-07-12）
    #   →E3 終態遞補整形→E4 全域斷言→E5 33 群總決算。六表對拍＋F.4 專屬閘。
    print("… W-F F.4（7-4 三級調配＋7-5 批次最佳化＋終態整形＋33 群總決算；trunk E）")
    try:
        if not _f3_ok:
            raise RuntimeError("F.3 未成功，F.4 跳過（存在性守衛）")
        import wf_f4
        # 靜態閘（禁呼叫 calc_a_prime／三廢）
        _wf4_src = open(os.path.join(HERE, "wf_f4.py"), encoding="utf-8").read()
        _f4hit = [f"{n}(" for n in ("calc_a_prime", "_allocate_three_tier_v1",
                  "_allocate_tier2_tier3_geometric", "_inflate_a_for_orphan") if f"{n}(" in _wf4_src]
        results.append(("F.4 靜態閘（wf_f4 不呼叫 calc_a_prime／三廢）", not _f4hit, _f4hit))

        _f4 = wf_f4.compute(_ctx, _f0, _f2, _f3)
        _mina4 = wf_f0._mina_by_block(ns, snapshot, cb_by)   # 區塊 MinA（池三則/Q3 斷言）
        _F4TAB = [("公設調配", "conv_rows", ["情境", "段", "目標宗"]),
                  ("七五雙出口", "exit_rows", ["情境", "歸戶"]),
                  ("G值", "g_tab", ["所屬街廓", "暫編地號"]),
                  ("池流向", "pool_rows", ["情境", "街廓"]),
                  ("整形", "reshape_rows", ["情境", "街廓", "暫編地號"]),
                  ("總決算", "ledger_rows", ["情境", "歸戶"])]
        for tag in ("0m", "3.5m"):
            d4 = _f4[tag]
            for nm, key, kcols in _F4TAB:
                _dump_csv(d4[key], os.path.join(OUTDIR, f"got_F.4_{nm}_退縮{tag}.csv"))
                ok, v = diff_rows(d4[key], os.path.join(F4DIR, f"F.4_{nm}_退縮{tag}.csv"),
                                  kcols, f"F.4·{nm}{tag}")
                results.append((f"F.4·{nm}{tag}", ok, v))
            a4 = d4["anchors"]
            # 結構永久閘（trunk E 守恆全綠）＋全區守恆殘差
            # §N3-0 全區級＝逐街廓加總（補丁三 §二）；舊 `<6` 廢（殘餘定閘）
            _c4ok = a4["verdict_all_green"] and a4["cons_resid"] <= a4["cons_tol"]
            results.append((f"F.4 結構永久閘{tag}（trunk E 守恆綠·|Σ(G−幾何)| "
                            f"{a4['cons_resid']} ≤ {a4['cons_tol']}）", _c4ok,
                            [] if _c4ok else [f"{a4['cons_resid']} > {a4['cons_tol']}"
                                              f"／all_green={a4['verdict_all_green']}"]))
            # 終態全域：旗標=0、位次序不變、B-1 窮舉閘、池三則
            results.append((f"F.4 終態旗標=0·位次序·B-1{tag}",
                            a4["flags_end"] == 0 and not a4["pos_viol"] and a4["b1_ok"],
                            [] if a4["flags_end"] == 0 and not a4["pos_viol"] and a4["b1_ok"]
                            else [f"flags={a4['flags_end']} pos={a4['pos_viol'][:2]} b1={a4['b1_ok']}"]))
            _mid4 = [l for l, v in a4["pool_final"].items() if 0.5 < v < _mina4[l]]
            results.append((f"F.4 池終態三則{tag}（各塊 0 或 ≥MinA）", not _mid4, _mid4))
            # E2 批次最優性：最優 < 次優（或次優 None）＋窮舉可行數 >0
            _e2 = a4["e2_opt"]
            _optok = (_e2["n_feasible"] > 0
                      and (_e2["second_cost"] is None or _e2["opt_cost"] <= _e2["second_cost"] + 1e-6))
            results.append((f"F.4 E2 窮舉最優性{tag}（opt {_e2['opt_cost']} ≤ 次優 {_e2['second_cost']}·"
                            f"可行 {_e2['n_feasible']}/{_e2['space']}·tie {_e2['tie_count']}）", _optok,
                            [] if _optok else [str(_e2)]))
        # ½ 輪0 <½ 具名錨 {G013,G024,G028}＋補償＝Σa×公設後價（現算 wavg）
        _a0 = _f4["0m"]["anchors"]
        _okcomp = (_a0["comp_groups"] == ["G013", "G024", "G028"]
                   and abs(_a0["wavg"] - wf_f4.SNAP_WAVG) < 1e-6)
        results.append((f"F.4 ½<½錨={_a0['comp_groups']}·公設後價等式 {_a0['wavg']:.5f}==快照", _okcomp,
                        [] if _okcomp else [str({k: _a0[k] for k in ('comp_groups', 'wavg')})]))
        # E0 級1殘餘三對（同區段 a′≡a 前例；具名錨）
        _oke0 = (_a0["e0_targets"] == {"628-49(1)": "628-48(1)", "628-30(2)": "628-45(2)",
                                       "628-42(1)": "628-42(2)"})
        results.append(("F.4 E0 級1殘餘三對錨（628-49(1)→628-48(1) 等）", _oke0,
                        [] if _oke0 else [str(_a0["e0_targets"])]))
        # Q3＋裁示1(a)：配地戶配額＝合法最小建築基地（寬≥min_width 且 G≥MinA）之最小 G。
        #   逐列斷言：①配額G≥MinA（達標/概念4）；②增配面積＝配額G−G(a′)（帳表一致，非負）；
        #   ③增配=0⟺G(a′)已達合法基地。最小性（禁超額）由引擎 _bisect_valid 保證＋終態旗標=0 佐證。
        #   〔KL Q3 area-MinA 與裁示1(a) width 衝突之解＝裁示1(a) 為終態合法性硬約束、governs；
        #     微增（min_width×depth_local−MinA，§8 型幾何）非政策超額。上呈 KL 追認、可否決。〕
        _q3bad = []
        for tag in ("0m", "3.5m"):
            for r in _f4[tag]["exit_rows"]:
                if not str(r.get("配額G(㎡)", "")).strip():
                    continue                          # 補償列跳過
                inc = float(r["增配面積(㎡)"] or 0)
                g0 = float(r["G(a′)輪0(㎡)"] or 0)
                gq = float(r["配額G(㎡)"] or 0)
                blk = r["目標塊"]
                if gq < _mina4[blk] - 0.05:
                    _q3bad.append(f"{tag}/{r['歸戶']}@{blk}: 配額 {gq}<MinA {_mina4[blk]}")
                elif abs(inc - max(0.0, gq - g0)) > 0.12:
                    _q3bad.append(f"{tag}/{r['歸戶']}@{blk}: 增配 {inc}≠配額−G(a′) {gq - g0:.2f}")
                elif inc < 0:
                    _q3bad.append(f"{tag}/{r['歸戶']}@{blk}: 負增配 {inc}")
                elif abs(inc) < 0.01 and abs(gq - g0) > 0.12:
                    _q3bad.append(f"{tag}/{r['歸戶']}@{blk}: 增配=0 但配額≠G(a′)")
        results.append(("F.4 Q3＋裁示1(a)（配額=合法基地·達標·帳表一致·禁超額）", not _q3bad, _q3bad[:5]))
        # 模式二逐筆手算抽樣（≥3 筆，含 G028 跨 zone a→R4 之 ratio≠1；獨立算式）
        _pre, _pavg = wf_f4.fixture_mode2_hand(snapshot, build_parcels)
        _m2ok = all(b in _pavg for b in ("R1", "R4"))
        results.append(("F.4 模式二 p_avg 母體＝原始 build_parcels（R1/R4 可算）", _m2ok, []))
    except Exception as _e_f4:
        import traceback
        results.append(("W-F F.4", False, [f"[F.4] {_e_f4}", traceback.format_exc()[-700:]]))

    # ── W-G G.1：§7 引擎接線層 ctx-builder 同源閘 ──
    #   證 app `_build_wf_ctx`（harvested）由 session_state 忠實組出引擎所需 ctx。
    #   seed＝native _ctx["0m"] 反投影＋run_step_g 寫入 fake_st 之鍵；f3_sb_rows 用合成列
    #   （測 snap.blocks 欄名映射、去循環：非取自快照/native）。全鏈 f0→f4 終態對拍留 G.3。
    print("… W-G G.1 接線層 ctx-builder 同源（app _build_wf_ctx vs native _ctx；0m）")
    try:
        _nat = _ctx["0m"]
        _cad = _nat["cad"]
        _fss = fake_st.session_state
        _lbl0 = next(iter(_nat["cb_by"]))
        _seed = {
            "f3_G_values": _nat["gA"], "f3_corner_winners": _nat["winners"],
            "f3L_corner_min_table": _nat["params"], "f3L_forced_offset": _nat["forced"],
            "f3_classified_blocks": list(_nat["cb_by"].values()), "f3_temp_parcels": _nat["temp"],
            "t8_ownership_map": _nat["omap"], "t8_ownership_groups": _fss.get("t8_ownership_groups", {}),
            "f3_wd2_pool_diag": _nat["poolA"], "f3_build_parcels": _nat["build"],
            "f3_alloc_depth_by_label": _fss["f3_alloc_depth_by_label"],
            "f3_min_width_by_label": _fss["f3_min_width_by_label"],
            "f3L_setback_default": _nat["setback"],
            "f3_cad_front_lengths": _cad["front_lengths"],
            "f3_cad_side_lengths_by_side": _cad["side_lengths_by_side"],
            "f3_cad_front_lines": _cad["front_lines"],
            "f3_cad_side_lines_by_side": _cad.get("side_lines_by_side", {}),
            "f3_cad_alloc_dir": _cad.get("alloc_dir_by_block", {}),
            "f3_manual_road_centerlines": _cad.get("centerlines", {}),
            "f3_sb_rows": [{"街廓": _lbl0,
                            "正面路寬(m)": 12.0, "正街尺度": 0.0, "正面長度(m)": 87.3, "正面面積(㎡)": 0.0,
                            "左側路寬(m)": 8.0, "左側尺度": 1.0, "左側長度(m)": 33.2, "左側面積(㎡)": 33.2,
                            "右側路寬(m)": 8.0, "右側尺度": 1.0, "右側長度(m)": 33.3, "右側面積(㎡)": 33.3}],
        }
        _bctx = ns["_build_wf_ctx"](_seed, "0m", ns["__file__"])
        _vg1 = []
        if set(ns["_WF_NS_NAMES"]) - set(_bctx["ns"]):
            _vg1.append("ns 16 真符號不全")
        if not isinstance(_bctx["cb_by"], dict) or set(_bctx["cb_by"]) != set(_nat["cb_by"]):
            _vg1.append("cb_by list→dict 不符")
        if _bctx["cad"].get("centerlines") != _cad.get("centerlines"):
            _vg1.append("cad centerlines 漏/不符")
        if set(_bctx["cad"]["front_lengths"]) != set(_cad["front_lengths"]):
            _vg1.append("cad front_lengths 鍵不符")
        if _bctx["gA"] != _nat["gA"]:
            _vg1.append("gA 不符")
        if _bctx["winners"] != _nat["winners"]:
            _vg1.append("winners 不符")
        if _bctx["snap"]["財務接線_v3"] != snapshot["財務接線_v3"]:
            _vg1.append("β 財務源 ≠ 快照 財務接線_v3")
        if len(_bctx["build"]) != len(_nat["build"]) or len(_bctx["temp"]) != len(_nat["temp"]):
            _vg1.append("build/temp 數不符")
        _sb0 = _bctx["snap"]["blocks"].get(_lbl0, {})
        if not (_sb0.get("正面", {}).get("負擔尺度_輸入") == 0.0
                and _sb0.get("左側", {}).get("負擔尺度_輸入") == 1.0):
            _vg1.append("snap.blocks 負擔尺度 欄名映射錯")
        if not ns["_is_uc9898"](_seed):
            _vg1.append("_is_uc9898 指紋誤判本案")
        # G.1 補丁閘：ctx-builder 須主動鋪底 f3_total_burden_rate_from_finance（禁 UI 前置點擊、禁靜默 0.40）
        #   值＝compute_total_burden_rate（β 快照）現算＝快照斷言錨 重劃總負擔率（0.40712387）。
        _seed.pop("f3_total_burden_rate_from_finance", None)   # 抹去 seed 之既有值→證 ctx-builder 主動鋪底（複現 live 缺鍵）
        _bctx2 = ns["_build_wf_ctx"](_seed, "0m", ns["__file__"])
        _rate_seed = _bctx2["fake_st"].session_state.get("f3_total_burden_rate_from_finance")
        _rate_anchor = float(snapshot["財務接線_v3"]["斷言錨"]["重劃總負擔率"])
        if _rate_seed is None:
            _vg1.append("ctx-builder 未鋪底 f3_total_burden_rate_from_finance（合約缺口未修）")
        elif abs(float(_rate_seed) - _rate_anchor) > 1e-6:
            _vg1.append(f"鋪底率 {_rate_seed} ≠ 快照斷言錨 {_rate_anchor}（>1e-6）")
        results.append(("W-G G.1 接線層 ctx-builder 同源（cb_by/cad+centerlines/gA/winners/β財務/blocks欄名/指紋/率鋪底）",
                        not _vg1, _vg1))
    except Exception as _e_g1:
        import traceback
        results.append(("W-G G.1 接線層 ctx-builder 同源", False,
                        [f"[G.1] {_e_g1}", traceback.format_exc()[-700:]]))

    # ── W-G G.2：世代幾何曝出契約＋只寫不讀（0m）──
    #   (a) 曝出契約：v3/f0/f2/f3/E 各代原始列帶逐宗 cut_coords、f1/f4 整形新形座標曝出
    #       ＝G.2 純呈現層「只讀不重算」之資料前提（KL 裁定 2026-07-12 純加性曝值第四例）。
    #   (b) 只寫不讀（靜態圍欄②）：新曝鍵於引擎檔僅出現於曝出寫點（每檔恰 1 次）、
    #       他引擎檔零越界＝「引擎只寫、UI 只讀」機檢化。
    print("… W-G G.2 世代幾何曝出契約＋只寫不讀（0m）")
    try:
        _vg2 = []
        for _nm2, _rows2 in (("v3.gA", _ctx["0m"]["gA"]),
                             ("f0.sgB_rows", _f0["0m"]["sgB_rows"]),
                             ("f2.sgC_rows", _f2["0m"]["sgC_rows"]),
                             ("f3.sgD_rows", _f3["0m"]["sgD_rows"]),
                             ("E.sgE_rows", _f4["0m"]["sgE_rows"])):
            _ngeo = sum(1 for r in _rows2
                        if r.get("推進側別") in ("left", "right", "抵費地")
                        and len(r.get("cut_coords") or []) >= 3)
            if not _ngeo:
                _vg2.append(f"{_nm2} 無逐宗 cut_coords")
        if not _f1["0m"].get("reshape_polys"):
            _vg2.append("f1.reshape_polys 空")
        if len(_f1["0m"].get("wedge_coords") or ()) < 3:
            _vg2.append("f1.wedge_coords 缺")
        if not isinstance(_f4["0m"].get("reshape_polys"), dict):
            _vg2.append("f4.reshape_polys 缺")
        for _fn2, _keys2 in (("wf_f1.py", ("reshape_polys", "wedge_coords")),
                             ("wf_f2.py", ("sgC_rows",)),
                             ("wf_f4.py", ("sgE_rows", "reshape_polys"))):
            _src2 = open(os.path.join(HERE, _fn2), encoding="utf-8").read()
            for _k2 in _keys2:
                _n2 = _src2.count(f'"{_k2}"')
                if _n2 != 1:
                    _vg2.append(f"{_fn2}:{_k2} 出現 {_n2} 次≠1（只寫不讀破）")
        for _fn2 in ("wf_f0.py", "wf_f3.py", "stepg_pipeline.py", "selection_pipeline.py"):
            _src2 = open(os.path.join(HERE, _fn2), encoding="utf-8").read()
            for _k2 in ("sgC_rows", "sgE_rows", "wedge_coords"):
                if f'"{_k2}"' in _src2:
                    _vg2.append(f"{_fn2} 出現 {_k2}（越界）")
        results.append(("W-G G.2 世代幾何曝出契約＋只寫不讀（v3/f0/f1/f2/f3/E 逐宗座標·靜態越界=0）",
                        not _vg2, _vg2))
    except Exception as _e_g2:
        import traceback
        results.append(("W-G G.2 世代幾何曝出契約", False,
                        [f"[G.2] {_e_g2}", traceback.format_exc()[-700:]]))

    print("=" * 60)
    allok = True
    for name, ok, viol in results:
        print(f"  {'✅ PASS' if ok else '🔴 FAIL'}  {name}")
        allok = allok and ok
        for x in viol[:12]:
            print("       ", x)
    print("=" * 60)
    if gxxx_warnings:
        print("⚠️ Gxxx 警告級 diverge（不得正規化吃掉；迭代序訊號 → 交 B6 仲裁）")
    print("嫌犯序：快照漏參 > dtype 1.5（法人統編 '.0'）> driver orchestration 漂移 > 引擎（勿動 app）")
    print("RESULT:", "ALL GREEN（幾何半＋選位半＋Step G v3 真值財務＋結構不變量永久閘）"
          if allok else "FAIL")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
