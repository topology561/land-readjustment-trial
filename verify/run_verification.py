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
from stepg_pipeline import run_step_g, build_step_g_tables  # noqa: E402

SNAPSHOT = os.path.join(HERE, "case_params_UC9898.json")
V6DXF = os.path.join(REPO, "data", "V6.dxf")
ANON_XLSX = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
BASELINES = os.path.join(HERE, "baselines")
WD2RUN = os.path.join(HERE, "baselines", "v2")   # v2 baselines（KL 2026-07-06 乾淨雙參數輪轉正）
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
    ss["f3_total_burden_rate_from_finance"] = float(snapshot["global"]["重劃總負擔率"])
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
        ns, fake_st, v6_raw, list(cb_by.values()))
    print(f"… parcels：temp {len(temp_parcels)} 筆｜可建築 build {len(build_parcels)} 筆｜"
          f"面積交叉換位 {len(swaps)} 對")

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        diag, sel, off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad,
            param_by_tag[tag], temp_parcels, build_parcels, setback)
        _dump_csv(diag, os.path.join(OUTDIR, f"got_診斷_退縮{tag}.csv"))
        _dump_csv(sel, os.path.join(OUTDIR, f"got_指配_退縮{tag}.csv"))
        _dump_csv(off, os.path.join(OUTDIR, f"got_抵費地_退縮{tag}.csv"))

        # v1 診斷豁免欄記帳：『原位次(距角序·暫行)』——W-D.2 v2 轉正換源投影序 rank
        # （KL 放行三件套 2026-07-06；新欄由 v2 段＋pool-slot 單測看守，README 白名單 #3）
        ok_d, v_d = diff_rows(diag, os.path.join(BASELINES, f"W-D.1.2 診斷_退縮{tag}.csv"),
                              ["街廓", "端", "候選地號"], f"診斷{tag}",
                              skip_cols={"原位次(距角序·暫行)"})
        results.append((f"診斷{tag}(v1·原位次欄豁免)", ok_d, v_d))

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

        # ── 🆕 W-D.2 P6：Step G headless → 三張表對拍 v2 準源（wd2_run/） ──
        print(f"… Step G headless（{tag}；快照尺度輸入消費＋J 非零看守）")
        try:
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             param_by_tag[tag], build_parcels,
                             winners_state, forced_map, setback)
            g_tab, diag_tab, slot_tab = build_step_g_tables(_sg)
            _dump_csv(g_tab, os.path.join(OUTDIR, f"got_G值_退縮{tag}.csv"))
            _dump_csv(diag_tab, os.path.join(OUTDIR, f"got_滑池槽診斷_退縮{tag}.csv"))
            _dump_csv(slot_tab, os.path.join(OUTDIR, f"got_逐槽J表_退縮{tag}.csv"))
            ok_g, v_g = diff_rows(
                g_tab, os.path.join(WD2RUN, f"G 值計算結果_退縮{tag}.csv"),
                ["所屬街廓", "暫編地號"], f"v2·G值{tag}")
            results.append((f"v2·G值{tag}", ok_g, v_g))
            ok_pd, v_pd = diff_rows(
                diag_tab, os.path.join(WD2RUN, f"W-D.2 §3 滑池槽診斷_退縮{tag}.csv"),
                ["街廓"], f"v2·滑池槽{tag}")
            results.append((f"v2·滑池槽{tag}", ok_pd, v_pd))
            ok_j, v_j = diff_rows(
                slot_tab, os.path.join(WD2RUN, f"逐槽 J 表_退縮{tag}.csv"),
                ["街廓", "k"], f"v2·J表{tag}")
            results.append((f"v2·J表{tag}", ok_j, v_j))
        except RuntimeError as _e_sg:
            results.append((f"v2·StepG{tag}", False, [f"[StepG{tag}] 看守觸發：{_e_sg}"]))

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
    print("RESULT:", "ALL GREEN（幾何半＋選位半＋Step G v2）" if allok else "FAIL")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
