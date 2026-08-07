# -*- coding: utf-8 -*-
"""W-G.4 T1 探針 — 街角資格閘改「**真 G**」之前後對照（Q-M1 裁 (b) 先量後裁）。

## 為何（KL/claude.ai 裁決 2026-07-24）

Q1 裁「改真 G」，惟 reviewer 實測 13 候選 `G真 − G估` **全負** ⇒ 閘一律變嚴，
而現行 winner 餘裕最薄者僅 **+0.84㎡**（R1右 628(5)）⇒ **Q1 可能反而新增 forced 端**，
與本波「forced 街角解鎖 → 面積回歸中央調配池 918.50㎡」之目的相反。故裁 **(b) 先量後裁**：本探針先量，再定 plan v2 骨架。

## 口徑（**Q-M2 裁樂觀假設第 1 宗**·技術補注·KL 可否決）

| 量 | 值 | 依據 |
|---|---|---|
| `baseline_pt` | 左＝`corner_pt`；右＝`corner_pt + s_max_R·d̂` | 假設第 1 宗·**兩端皆不預設 forced** ⇒ buf=0 |
| `d_hat` | 左＝`+d̂`；右＝`−d̂` | 同 stepg 左右組 |
| `S_max_limit` | 左＝**`S_block_max`**；右＝**`_oblique_s_max`** | reviewer B-6 更正：**左右不同源**（左非 oblique） |
| | **不扣對端 buffer** | 「樂觀」之定義（兩端皆不預設 forced） |
| `is_corner` / `W_prev` | `True` / `0.0` | 第 1 宗 |
| `a` | `round(分攤登記面積_m2 + 面積_m2, 2)`·源 **`temp_parcels`** | reviewer **R3** 修正（PK 現用 `幾何面積_m2`＝口徑分岔） |
| 深度／最小寬 | **顯式自 snapshot** `街廓分配深度_m`／`get_min_lot_size`·缺值 **loud** | reviewer **W-5**（PK 時段 session 未鋪底·fallback 差 R6 6.05㎡） |
| B／C／price | `stepg._V3_FINANCE`（run_step_g 外拋·**非複刻**） | 單一真相源·避第三份抄寫（#20） |

**三指數分數與 G 無關**（僅截角長／側街長／真交集）⇒ 本探針**不重跑三指數**，
改讀既有診斷之 `總分`，只**重判達標**、再取達標中 `總分` 最大者為新 winner
（tie → `原位次(投影序)` 小者·同 skill 正典）。

## 輸出（KL 指定四項）
1. 各端 winner 前後對照　2. forced 端前後對照　3. **918.50㎡ 回歸中央調配池之量預估**
4. **R1右刀口敏感度**（含 `Δa ∈ [−2.53, +0.72]` 擾動）　＋ 0m 同跑對照

## 重跑
    WV_CORNER_TRUEG=1 python verify/probes/probe_corner_trueG.py

⚠️ **零治理碼改動**（本檔為獨立 script·不注入、不改 app/verify 引擎）。
⚠️ **基線波前產物·待重烤**：B/C/price 源自 snapshot、F.0 六格錨過期（§11.3）⇒
絕對數值待波末複核；**前後對照之結構性結論**（是否翻盤）穩健。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon                                # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import (                                    # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g                               # noqa: E402
import stepg_pipeline                                               # noqa: E402
from wg_g1_smoke import _reconstruct_sb_rows                        # noqa: E402

OUT_LOG = os.path.join(VERIFY, "out", "probe_corner_trueG.log")
SIDE_CN = {"左": "左側", "右": "右側"}
DA_PERTURB = (-2.53, 0.0, +0.72)      # reviewer R3 實測 Δa 區間端點＋0


def _fail(msg):
    raise RuntimeError(f"🔴 probe_corner_trueG：{msg}（no-silent-fallback）")


def _true_G(ns, *, a_m2, A_ratio, B, C, l_front, l_side, F, blk_poly, d_hat,
            corner_pt, s_max_L, s_max_R, side, alloc_axis, side_mid, avg_depth,
            tab6_burden, front_p2, _label):
    """假設第 1 宗之真 G（樂觀口徑）。**P-A 起改呼生產函式 `_corner_first_lot_G`**
    （內呼 `_solve_G_one`＝與實配同一 solve 路徑·左右 S_max 不同源之映射內建）——
    此即 A-1（同一路徑）＋A-2（左右 S_max 不同源）之**真幾何**驗證：本探針輸出與 T1
    committed log 對拍不變 ＝ `_corner_first_lot_G` 與舊 inline solve_G_binary 逐位同值。"""
    return ns["_corner_first_lot_G"](
        a_m2=a_m2, A_ratio=A_ratio, B=B, C=C, l_front=l_front, l_side=l_side, F=F,
        block_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt,
        s_max_left=s_max_L, s_max_right=s_max_R, side=side,
        allocation_dir=alloc_axis, side_mid=side_mid, avg_depth=avg_depth,
        tab6_burden=tab6_burden, front_p2=front_p2, _label=_label)


def _run_tag(ns, fake_st, snapshot, setback, tag, L):
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    diag, sel, off, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback, snapshot=snapshot)
    # run_step_g 以取 _V3_FINANCE（B/C/price·單一真相源）＋ sb 尺度
    run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
               params, build, winners, forced, setback)
    fin3 = getattr(stepg_pipeline, "_V3_FINANCE", None) or _fail("_V3_FINANCE 未外拋")
    B, C = float(fin3["B"]), float(fin3["C"])
    # P-A：`_corner_first_lot_G` 之 fallback（iterate_G_S）需 tab6_burden；run_step_g 後 session 已鋪底。
    _tab6 = float(fake_st.session_state.get("f3_total_burden_rate_from_finance") or 0) \
        or _fail("f3_total_burden_rate_from_finance 未鋪底（run_step_g 應已設）")
    post_p, pre_p = fin3["post_price_by_block"], fin3["pre_price_by_zone"]
    sb_rows = {r["街廓"]: r for r in _reconstruct_sb_rows(ns, cad, snapshot)}
    SB = snapshot["blocks"]
    zof = snapshot["財務接線_v3"]["原地號_區段"]
    tp_by = {t["暫編地號"]: t for t in temp}
    bp_by = {b["暫編地號"]: b for b in build}

    L.append("=" * 104)
    L.append(f"[T1·{tag}] 街角資格閘 G估 → 真G（樂觀假設第1宗）｜B={B:.9f} C={C:.9f}")
    L.append("-" * 104)
    L.append(f"{'塊':4}{'端':3}{'候選':14}{'門檻':>9}{'G估':>10}{'真G':>10}"
             f"{'ΔG':>9}{'總分':>8} 舊達標 新達標")

    by_end = {}
    for r in diag:
        blk, end = r["街廓"], r["端"]
        pid = r["候選地號"]
        tp = tp_by.get(pid) or _fail(f"{pid} 不在 temp_parcels")
        bpr = bp_by.get(pid) or _fail(f"{pid} 不在 build_parcels")
        # R3：a 口徑＝實配（分攤登記＋面積_m2）·**if-in 形**（reviewer B-4：
        #   `.get(A, .get(B,0))+B` 於鍵缺席時重複計面積_m2；實配 7 處皆 if-in·此處同構）。
        if "分攤登記面積_m2" in tp:
            a_m2 = round(float(tp.get("分攤登記面積_m2", 0) or 0)
                         + float(tp.get("面積_m2", 0) or 0), 2)
        else:
            a_m2 = round(float(tp.get("面積_m2", 0) or 0), 2)
        # W-5：深度/最小寬顯式自 snapshot·缺值 loud
        if blk not in SB:
            _fail(f"{blk} 不在 snapshot.blocks")
        depth = float(SB[blk]["街廓分配深度_m"])
        road_w = float(SB[blk]["正面"]["路寬_m"])
        cat = cb_by[blk]["category"]
        mw = float(ns["get_min_lot_size"](cat, road_w).get("min_width", 0) or 0)
        if depth <= 0 or mw <= 0:
            _fail(f"{blk} 深度={depth} 最小寬={mw}")
        fl = (cad.get("front_lines") or {}).get(blk) or _fail(f"{blk} 缺 FRONT_LINE")
        p1 = np.array(fl["p1"], float); p2 = np.array(fl["p2"], float)
        s_max_L = float(np.linalg.norm(p2 - p1))          # 左端＝S_block_max
        d_hat = (p2 - p1) / (s_max_L or 1.0)
        verts = cb_by[blk]["vertices"]
        blk_poly = Polygon(verts)
        if not blk_poly.is_valid:
            blk_poly = blk_poly.buffer(0)
        alloc_cad = (cad.get("alloc_dir_by_block") or {}).get(blk) \
            or _fail(f"{blk} 缺 ALLOC")
        alloc_axis = ns["alloc_normal_axis"](alloc_cad)
        s_max_R = ns["_oblique_s_max"](verts, d_hat, p1, alloc_axis) or s_max_L
        sbr = sb_rows.get(blk) or _fail(f"{blk} 缺 sb row")
        l_front = float(sbr.get("正街尺度", 0) or 0)
        l_side = float(sbr.get("左側尺度" if end == "左" else "右側尺度", 0) or 0)
        # 🔧 **更正（D-2b-2 §七-1·CC 自查）**：原式 `SB[blk][側]["路寬_m"]` 係 **F 槽餵錯量**
        #   ——正典明訂 **F ＝ SIDE_LINE 全長**，非側街路寬（`GB-41`）。本處為 GB-41 所載
        #   「誤用之二處」**之外的第三處**（該登記之「二處」係**列舉、非窮舉**·已加具名更正註）。
        #   改源為 `sbr`（＝`sb_rows_by_label` 之列）——與 D-1 落地之
        #   `app.py:18030-18031`／`verify/selection_pipeline.py:436-437` **同一 dict、同一欄名**。
        F = float(sbr.get("左側長度(m)" if end == "左" else "右側長度(m)", 0) or 0)
        slb = ((cad.get("side_lines_by_side") or {}).get(blk) or {})
        side_mid = (slb.get("left" if end == "左" else "right") or {}).get("mid")
        zone = zof.get(bpr.get("原地號", ""), "")
        A_ratio = ((post_p.get(blk, 0.0) / pre_p[zone])
                   if (zone in pre_p and pre_p[zone] > 0 and post_p.get(blk, 0) > 0)
                   else 1.0)
        Gt = _true_G(ns, a_m2=a_m2, A_ratio=A_ratio, B=B, C=C, l_front=l_front,
                     l_side=l_side, F=F, blk_poly=blk_poly, d_hat=d_hat,
                     corner_pt=p1, s_max_L=s_max_L, s_max_R=s_max_R, side=end,
                     alloc_axis=alloc_axis, side_mid=side_mid, avg_depth=depth,
                     tab6_burden=_tab6, front_p2=p2, _label=f"{blk}{end}·{pid}")
        thr = float(r["門檻(㎡)"]); ge = float(r["G估(㎡)"])
        # 🔴 欄值以**倉檔實查**為準（首版誤猜 '✅' 致舊達標全 ❌·結論全錯）：
        #    『達標』∈{'達標','未達標'}；『選中』∈{'✅',''}＝**舊 winner 標記**（不自行推導）。
        _dz = str(r.get("達標", "")).strip()
        if _dz not in ("達標", "未達標"):
            _fail(f"{pid} 『達標』欄非預期值 {_dz!r}（欄語意已變·禁猜）")
        old_ok = (_dz == "達標")
        old_sel = str(r.get("選中", "")).strip() == "✅"
        new_ok = Gt >= thr

        def _num(v, dflt=None):
            """診斷表對**未達標**候選之 `總分`／`原位次` 為 `—`（G-gate 淘汰後不算三指數）。"""
            s = str(v if v is not None else "").strip()
            try:
                return float(s)
            except ValueError:
                return dflt
        score = _num(r.get("總分"))          # None ＝ 該候選原未達標·無三指數分數
        # 🚩 「原未達標 → 新達標」＝真 G **高於** G估者。reviewer 實測 13 筆 G真−G估 全負
        #    ⇒ 此情形應不出現；**不假設**、顯式偵測並 loud 標記（出現則探針無法定 winner）。
        need_rescore = bool(new_ok and score is None)
        _sc = f"{score:8.4f}" if score is not None else f"{'—':>8}"
        L.append(f"{blk:4}{end:3}{pid:14}{thr:9.2f}{ge:10.2f}{Gt:10.2f}"
                 f"{Gt - ge:+9.2f}{_sc}"
                 f"{('✅' if old_ok else '❌'):>6}{('✅' if new_ok else '❌'):>6}"
                 f"{'  🚩新達標但無三指數分數·需重算' if need_rescore else ''}")
        by_end.setdefault((blk, end), []).append({
            "pid": pid, "thr": thr, "Gt": Gt, "ge": ge, "old_ok": old_ok,
            "old_sel": old_sel,
            "new_ok": new_ok, "score": score, "need_rescore": need_rescore,
            "rank": _num(r.get("原位次(投影序)"), 1e9),
            "a": a_m2, "A": A_ratio, "l_front": l_front, "l_side": l_side, "F": F,
            "geom": (blk_poly, d_hat, p1, s_max_L, s_max_R, alloc_axis, side_mid, depth),
            "p2": p2,          # 🔒 K-4 第 5 條前提（front_p2·獨立自 CAD 讀）
            "BC": (B, C),
        })

    # ── winner／forced 前後對照 ────────────────────────────────────────────────
    L.append("-" * 104)
    L.append("端別 winner／forced 前後對照：")
    # 舊 winner **直讀診斷之『選中』欄**（倉內既有判定·不自行推導·防誤猜）；
    #   以指配表 `sel` 之「⚠️強制抵費地」交叉核對，不一致即 loud。
    sel_by = {(r["街廓"], k): str(r.get(f"【{k}】第1宗指配", "")).strip()
              for r in sel for k in ("左", "右")}
    flip, forced_before, forced_after, release = [], [], [], 0.0
    for (blk, end), cands in sorted(by_end.items()):
        _sw = [c["pid"] for c in cands if c["old_sel"]]
        old_w = _sw[0] if _sw else None
        _assign = sel_by.get((blk, end), "")
        _is_forced_doc = "強制抵費地" in _assign
        if (old_w is None) != _is_forced_doc:
            _fail(f"{blk}{end}：診斷『選中』(={old_w}) 與指配表(={_assign!r}) 不一致")
        _qn = [c for c in cands if c["new_ok"]]
        if any(c["need_rescore"] for c in _qn):
            # 🚩 有「新達標但無三指數分數」者 ⇒ 本端 winner **不可由本探針判定**（禁猜）
            L.append(f"  {blk} {end}：🚩 **無法判定**——新達標集合含未算三指數者 "
                     f"{[c['pid'] for c in _qn if c['need_rescore']]}·需重跑 v12 三指數")
            new_w = "🚩需重算"
        else:
            new_w = (sorted(_qn, key=lambda c: (-c["score"], c["rank"]))[0]["pid"]
                     if _qn else None)
        thr = cands[0]["thr"]
        if old_w is None:
            forced_before.append((blk, end, thr))
        if new_w is None:
            forced_after.append((blk, end, thr))
        if old_w is None and new_w is not None:
            release += thr
        mark = "" if old_w == new_w else "  🚩翻盤"
        L.append(f"  {blk} {end}：{str(old_w or '⚠️強制抵費地'):>16} → "
                 f"{str(new_w or '⚠️強制抵費地'):<16} 門檻={thr:8.2f}{mark}")
        if old_w != new_w:
            flip.append((blk, end, old_w, new_w, thr, cands))
    L.append(f"  forced 端：前 {[(b, e) for b, e, _ in forced_before]} → "
             f"後 {[(b, e) for b, e, _ in forced_after]}")
    L.append(f"  forced 面積：前 Σ={sum(t for _, _, t in forced_before):.2f}㎡ → "
             f"後 Σ={sum(t for _, _, t in forced_after):.2f}㎡"
             f"｜**回歸中央調配池={release:.2f}㎡**"
             f"｜新增={sum(t for b, e, t in forced_after if (b, e) not in [(x, y) for x, y, _ in forced_before]):.2f}㎡")

    # ── 刀口敏感度（Δa 擾動·對所有「新達標且餘裕最薄」者）──────────────────────
    L.append("-" * 104)
    L.append(f"刀口敏感度（Δa 擾動 {DA_PERTURB}·僅列餘裕 <20㎡ 者）：")
    thin = sorted((c for cs in by_end.values() for c in cs
                   if c["new_ok"] and (c["Gt"] - c["thr"]) < 20.0),
                  key=lambda c: c["Gt"] - c["thr"])
    if not thin:
        L.append("  （無餘裕 <20㎡ 之新達標候選）")
    for c in thin:
        bp_, dh_, p1_, sL_, sR_, ax_, sm_, dep_ = c["geom"]
        B_, C_ = c["BC"]
        row = []
        for da in DA_PERTURB:
            g = _true_G(ns, a_m2=round(c["a"] + da, 2), A_ratio=c["A"], B=B_, C=C_,
                        l_front=c["l_front"], l_side=c["l_side"], F=c["F"],
                        blk_poly=bp_, d_hat=dh_, corner_pt=p1_, s_max_L=sL_,
                        s_max_R=sR_, side=[e for (b, e), cs in by_end.items()
                                           if c in cs][0],
                        alloc_axis=ax_, side_mid=sm_, avg_depth=dep_,
                        tab6_burden=_tab6, front_p2=c["p2"], _label=c["pid"])
            row.append(f"Δa{da:+.2f}→G {g:.2f}（餘裕{g - c['thr']:+.2f}）"
                       f"{'❌翻' if g < c['thr'] else ''}")
        L.append(f"  {c['pid']:14} 門檻={c['thr']:.2f}｜" + "｜".join(row))
    return flip, forced_before, forced_after, release


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.environ.get("WV_CORNER_TRUEG") != "1":
        print("🔴 本探針須 WV_CORNER_TRUEG=1 明示啟用。"
              "\n   例：WV_CORNER_TRUEG=1 python verify/probes/probe_corner_trueG.py")
        return 2
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    snapshot = rv.load_snapshot()   # 🆕 K-8 §三 A-2：現算 N-19′ 深度注入（檔案零修改）
    L = []
    summary = {}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        ns, fake_st = harvest()          # 每情境重新 harvest（session 隔離）
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        flip, fb, fa, rel = _run_tag(ns, fake_st, snapshot, setback, tag, L)
        summary[tag] = (flip, fb, fa, rel)
    L.append("=" * 104)
    L.append("【T1 結論】")
    for tag, (flip, fb, fa, rel) in summary.items():
        L.append(f"  {tag}：winner 翻盤 {len(flip)} 端"
                 f"｜forced 前 {len(fb)} 端 → 後 {len(fa)} 端｜回歸中央調配池 {rel:.2f}㎡")
        for blk, end, ow, nw, thr, _ in flip:
            L.append(f"      🚩 {blk}{end}：{ow or '強制抵費地'} → "
                     f"{nw or '強制抵費地'}（門檻 {thr:.2f}）")
    _z = all(len(f) == 0 for f, _, _, _ in summary.values())
    L.append(f"  ⇒ **winner 集合{'零翻盤' if _z else '有翻盤'}** ⇒ "
             f"{'plan v2 全做（Q1+M 同波）' if _z else 'plan v2 翻盤案標 🚩上呈段·push 後停等'}")
    L.append("=" * 104)
    out = "\n".join(L)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write(out + "\n")
    print(out)
    print(f"\n📄 {OUT_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
