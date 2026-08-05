# -*- coding: utf-8 -*-
r"""K-9-7-d **第二層分支** — 第一層 vs 第二層 對照（K-6-A2 段四(c)-2(a) 立·**段四(c) 已切換**）。

## 定位

(c)-2 分三步，**(b) 為強制停機點**：

- **(a)** 第二層以 `k97_solve_alloc_t(..., block_vertices=…)` **opt-in** 求解（只算不換）。
- **(b)** 攤表呈 KL。
- **(c)** ✅ **已切換**（`_build_corner_range_v3` 已傳 `block_vertices`·KL 放行 2026-08-05）
  ⇒ 🔄 **本檔之「一層／二層」二欄語意隨之反轉**（見下）。

## 兩層之差別（＝ **GB-19**）

| | 帶深 `D(t)` 之臨街段 | 起算線 |
|---|---|---|
| **第一層**（🗄️ 段四(c) 前之生產） | `Q0 → P_front(t)`（`Q0`＝FRONT ∩ SIDE、`P_front`＝ALLOC ∩ FRONT） | **FRONT_LINE** |
| **第二層**（✅ **現行生產**·乙式） | `P_block(t) → PQ(t) ∩ SIDE` | **`PQ`**＝過 `P_block(t)` 平行 FRONT 之直線 |

`P_block(t)` ＝ `L_in(t) ∩ **BLOCK 邊界**`之**臨街側**者（K-9-8 (2)）。
`P_block` 落 FRONT 重疊段時 `PQ ≡ FRONT` ⇒ **自然退化回第一層**（K-9-8 (6)）。

⛔ **禁二分／禁取樣／禁迭代**：切換點 `t_C = (C − F1)·ân − c0` 為**一次減法**；
每條邊給一個 `t` 區間、區間內每支**一次除法**（推導 §二〜§四·
`docs/reports/W-G.5_K6-A2-段四c2a_第二層分支推導.md`）。

## 記號警語

⚠️ `P_front`（K-9-7）與 `P_block`（K-9-8）**同名異物**（正典 K-9-7-a 衝突二）——本檔一律用全名。
⚠️ `_build_corner_range_v3` 之區域變數 `k` 係正典之 `c`（衝突一）；本檔用正典記號。

## 面積對照之手法（**同一條多邊形構造路徑·只換 `t`**）

🔄 **段四(c) 切換後**：「**二層**」＝生產原樣呼叫 `_build_corner_range_v3`；
「**一層**」＝同一支、只多傳 `_t_override=<第一層 t*>`（段三(a) 已入庫之純加性參數）。
⇒ 兩欄之**唯一變因是 `t*`**，不摻構造差異。
⛔ 若沿用切換前之寫法（一層＝生產），兩欄同源 ⇒ `Δ面積` 恆 `0.000`（同型缺陷已登記）。

## 落點欄一律**量得**

`P_block` 之內縮量／落 FRONT 重疊段與否／落截角三角形與否，
**全部取自 `k97_solve_alloc_t` 之回傳**（判準 `|inset| <= _EPS_TOUCH_FRONT`），
⛔ **禁手寫進報告**、⛔ 禁由他處結論引入。

## 重跑

    python verify/probes/probe_K9_7d_layer2.py                     # 生產圖 V6
    python verify/probes/probe_K9_7d_layer2.py --dxf data/V6_1.dxf # GB-26 之可證偽檢驗

**rc 恆 0**（診斷·不作為閘）。輸出：
`verify/out/probe_K9_7d_layer2[_V6_1].log`（摘要）＋ `….full.log`（**同一次跑**之全量）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")


# ── DXF 路徑之參數化（**預設一律不變**）──────────────────────────────────────
#   體例逐字沿用 `verify/probes/probe_ruling_K9_corner_width.py` 之 `_resolve_dxf`
#   （`grep -n "def _resolve_dxf" verify/probes/probe_ruling_K9_corner_width.py`）：
#   ⛔ **生產路徑不動**——只在本探針行程內覆寫 `rv.V6DXF`，不寫回任何檔案。
#   ⛔ **這不是「換 V6_1 為生產圖」**（施工單 §七 之紅線）；是既有之診斷作法。
def _resolve_dxf():
    _p = None
    if "--dxf" in sys.argv:
        _i = sys.argv.index("--dxf")
        if _i + 1 >= len(sys.argv):
            raise RuntimeError("🔴 --dxf 未帶路徑（no-silent-fallback）")
        _p = sys.argv[_i + 1]
    _p = _p or os.environ.get("WV_K9_DXF") or None
    if _p is None:
        return rv.V6DXF, ""
    _p = os.path.abspath(_p)
    if not os.path.exists(_p):
        raise RuntimeError(f"🔴 --dxf 指定之檔不存在：{_p}（no-silent-fallback）")
    _tag = "_" + os.path.splitext(os.path.basename(_p))[0]
    return _p, ("" if os.path.abspath(_p) == os.path.abspath(rv.V6DXF) else _tag)


DXF_PATH, _SFX = _resolve_dxf()
rv.V6DXF = DXF_PATH

LOG = os.path.join(OUTDIR, f"probe_K9_7d_layer2{_SFX}.log")
FULL = os.path.join(OUTDIR, f"probe_K9_7d_layer2{_SFX}.full.log")

# 正典 K-9-7-c 表（`grep -n "^#### K-9-7-c " docs/rulings/K-6_街角地分配程序與可分配判準.md`）
#   ——**獨立真相源**（⛔ 非由本碼回填）。GB-26 之對照靶即此表之 `m`。
CANON_M = {
    ("R1", "left"): None,      ("R1", "right"): -0.000000,
    ("R2", "left"): +0.009750, ("R3", "right"): None,
    ("R4", "left"): +0.000266, ("R4", "right"): 0.000000,
    ("R5", "left"): -0.000000, ("R6", "right"): 0.000000,
}


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []          # 摘要（.log）
    F = []          # 全量（.full.log·**同一次跑**）

    def _both(s):
        L.append(s)
        F.append(s)

    _both("=" * 138)
    _both("【K-9-7-d 第二層分支】第一層 vs 第二層 t* 對照 —— "
          "🔴 **段四(c) 已切換：第二層即現行生產**")
    _both("第一層＝帶 `[0, D]`、`D` 自 FRONT 之臨街段（Q0→P_front(t)）量；")
    _both("第二層（🆕 **乙式**·K-9-6-b-2·KL 裁 2026-08-05）＝帶 **`[δ_P, δ_P+D_new]`**、"
          "`D_new` 自 PQ 之臨街段（P_block(t)→PQ∩SIDE）量（GB-19／GB-36）")
    _both(f"DXF：{os.path.relpath(DXF_PATH, REPO)}"
          + ("（**生產圖**）" if not _SFX else "（**平行對照·非生產圖**）"))
    _both("=" * 138)

    ns, fake_st = harvest()
    for _s in ("k97_solve_alloc_t", "_build_corner_range_v3", "_make_chamfer_tri_wb",
               "_baseline_pts_from_manual", "_EPS_TOUCH_FRONT"):
        if _s not in ns:
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    _EPS_TF = float(ns["_EPS_TOUCH_FRONT"])
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    rows = []
    for setback in (0.0, 3.5):
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            for side in ("left", "right"):
                if side not in (sd_by.get(lbl) or {}):
                    continue
                fl = fl_by.get(lbl) or {}
                if not (fl.get("p1") and fl.get("p2")):
                    continue
                _fp = [fl["p1"], fl["p2"]]
                _bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
                _sp = [sd_by[lbl][side]["p1"], sd_by[lbl][side]["p2"]]
                _chi = ns["_make_chamfer_tri_wb"](b, side)
                _depth = float(snapshot["blocks"][lbl]["街廓分配深度_m"])
                _q = ((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected")
                rec = {"sb": setback, "lbl": lbl, "side": side,
                       "new": None, "err": None, "a_old": None, "a_new": None}
                # 第二層（opt-in：傳 `block_vertices`）——同一支求解器亦回第一層之解
                try:
                    rec["new"] = ns["k97_solve_alloc_t"](
                        b.get("centroid"), _fp, _bp, _sp, al_by.get(lbl),
                        setback, legal_w, chamfer_tri=_chi, block_depth=_depth,
                        _label=lbl, _side=side, block_vertices=b.get("vertices"))
                except RuntimeError as e:
                    rec["err"] = str(e)
                # 面積：**同一條多邊形構造路徑**，只換 `t`。
                # 🔴 **K-6-A2 段四(c) 語意反轉**（切換後）：生產 `_build_corner_range_v3`
                #   **已走第二層** ⇒
                #     「二層」欄 ＝ **不傳 `_t_override`**（生產原樣）；
                #     「一層」欄 ＝ 以 `_t_override` 注入 **`t_star_layer1`**。
                #   ⛔ 若沿用切換前之寫法（一層＝生產、二層＝注入 `t_star`），
                #     兩欄將**同源** ⇒ `Δ面積` 恆 `0.000`——即上批登記之同型缺陷
                #     （`probe_ruling_K9_7_alloc_t` 之 `a_old`）。**不得重蹈。**
                if rec["new"] is not None:
                    try:
                        _r_old = ns["_build_corner_range_v3"](
                            b.get("vertices"), b.get("centroid"), _fp, _bp, _sp,
                            al_by.get(lbl), _depth, setback, legal_w, _chi,
                            dxf_quantum=_q, _label=lbl, _side=side,
                            _t_override=rec["new"]["t_star_layer1"])
                        rec["a_old"] = float(_r_old.area)
                    except RuntimeError as e:
                        rec["err"] = (rec["err"] or "") + f"｜第一層 t* 構造 raise：{e}"
                try:
                    _r_new = ns["_build_corner_range_v3"](
                        b.get("vertices"), b.get("centroid"), _fp, _bp, _sp,
                        al_by.get(lbl), _depth, setback, legal_w, _chi,
                        dxf_quantum=_q, _label=lbl, _side=side)
                    rec["a_new"] = float(_r_new.area)
                except RuntimeError as e:
                    rec["err"] = (rec["err"] or "") + f"｜生產（第二層）構造 raise：{e}"
                rows.append(rec)

    # ── 【A】t* 位移 ＋ 帶深 ─────────────────────────────────────────────────
    _both("")
    _both("【A】`t*` 位移（第一層 → 第二層）＋ 帶深 `D(t*)` — **(b) 攤表之主表**")
    _both("-" * 138)
    _both(f"{'情境':<6}{'街廓/側':<11}{'支(一層)':>9}{'支(二層)':>13}"
          f"{'t*(一層)':>13}{'t*(二層)':>13}{'Δt*(cm)':>10}"
          f"{'D(一層)':>11}{'D(二層)':>11}{'ΔD(m)':>12}  斷言")
    _both("-" * 138)
    _moved, _nerr = [], 0
    for r in rows:
        tag = f"{r['sb']:g}m"
        key = f"{r['lbl']}/{r['side']}"
        n = r["new"]
        if n is None:
            _nerr += 1
            _both(f"{tag:<6}{key:<11}  🔴 第二層 raise（見【E】）")
            continue
        _dt_cm = (n["t_star"] - n["t_star_layer1"]) * 100.0
        _dD = n["depth_at_t_star"] - n["depth_at_t_star_layer1"]
        if abs(_dt_cm) > 1e-9:
            _moved.append((tag, key, _dt_cm,
                           (None if (r["a_new"] is None or r["a_old"] is None)
                            else r["a_new"] - r["a_old"])))
        _both(f"{tag:<6}{key:<11}{n['branch_layer1']:>9}{n['branch']:>13}"
              f"{n['t_star_layer1']:>13.6f}{n['t_star']:>13.6f}{_dt_cm:>10.4f}"
              f"{n['depth_at_t_star_layer1']:>11.6f}{n['depth_at_t_star']:>11.6f}"
              f"{_dD:>12.2e}"
              f"  {'✅' if n['W_at_t_star'] >= n['T'] - 1e-6 else '🔴'}")
    _both("-" * 138)
    _both(f"  ⇒ `t*` 有位移之格：**{len(_moved)}** / {len([r for r in rows if r['new']])}"
          f"（第二層 raise {_nerr} 格）")
    for _t, _k, _d, _a in _moved:
        _both(f"     {_t} {_k}：Δt* {_d:+.6f} cm"
              + (f"／Δ面積 {_a:+.6f} ㎡" if _a is not None else ""))
    if not _moved:
        _both("     （無——本圖上第二層與第一層同解）")

    # ── 【B】街角規定範圍面積 ────────────────────────────────────────────────
    _both("")
    _both("【B】街角規定範圍**面積**（同一構造路徑·只換 `t*`）")
    _both("-" * 138)
    _both(f"{'情境':<6}{'街廓/側':<11}{'面積(一層)㎡':>16}{'面積(二層)㎡':>16}"
          f"{'Δ面積(㎡)':>14}{'Δ相對':>12}")
    _both("-" * 138)
    for r in rows:
        tag = f"{r['sb']:g}m"
        key = f"{r['lbl']}/{r['side']}"
        if r["a_old"] is None or r["a_new"] is None:
            _both(f"{tag:<6}{key:<11}  🔴 面積不可構造（見【E】）")
            continue
        _da = r["a_new"] - r["a_old"]
        _rel = (_da / r["a_old"]) if r["a_old"] else float("nan")
        _both(f"{tag:<6}{key:<11}{r['a_old']:>16.6f}{r['a_new']:>16.6f}"
              f"{_da:>14.6f}{_rel:>12.2e}")
    _both("-" * 138)

    # ── 【C】`P_block` 落點（**量得**·⛔ 禁手寫）──────────────────────────────
    _both("")
    _both("【C】`P_block(t*)` 之落點 — **量得**"
          f"（判準 `|inset| <= _EPS_TOUCH_FRONT = {_EPS_TF}`·⛔ 禁手寫進報告）"
          "｜🆕 乙式之 `δ_P` 與帶之二端")
    _both("-" * 138)
    _both(f"{'情境':<6}{'街廓/側':<11}{'內縮(m)':>12}{'δ_P(m)':>12}"
          f"{'帶上緣d':>11}{'帶下緣d':>11}{'落FRONT段':>10}{'落截角內':>9}"
          f"{'邊#':>4}{'dep(P_block)':>14}{'dep(PQ∩SIDE)':>14}")
    _both("-" * 138)
    _n_cham, _n_front, _n_other = 0, 0, 0
    for r in rows:
        n = r["new"]
        if n is None:
            continue
        tag = f"{r['sb']:g}m"
        key = f"{r['lbl']}/{r['side']}"
        _of = n["P_block_on_front"]
        _oc = n["P_block_on_chamfer"]
        if _of:
            _n_front += 1
        elif _oc:
            _n_cham += 1
        else:
            _n_other += 1
        _both(f"{tag:<6}{key:<11}{n['P_block_inset_from_front']:>12.6f}"
              f"{n['delta_P']:>12.6f}{n['band_d_top']:>11.6f}{n['band_d_bot']:>11.6f}"
              f"{('是' if _of else '否'):>10}"
              f"{('—' if _oc is None else ('是' if _oc else '否')):>9}"
              f"{n['P_block_edge']:>4}"
              f"{n['P_block_dep']:>14.6f}{n['Q_pq_dep']:>14.6f}")
        F.append(f"      {tag} {key} P_block ＝ "
                 f"({n['P_block'][0]:.4f}, {n['P_block'][1]:.4f})"
                 f"｜Q_pq ＝ ({n['Q_pq'][0]:.4f}, {n['Q_pq'][1]:.4f})")
    _both("-" * 138)
    _both(f"  ⇒ 落 FRONT 重疊段 **{_n_front}** 格／落截角（非 FRONT 段且在截角三角形內）"
          f"**{_n_cham}** 格／二者皆非 **{_n_other}** 格")

    # ── 【D】分支切換點（正典 K-9-7-d：**須明列**）────────────────────────────
    _both("")
    _both("【D】分支**切換點**明列（頂點界 `t_C = (C − F1)·ân − c0` ＋ 深度端界 `dep_P = dep_Q`）")
    _both("-" * 138)
    for r in rows:
        n = r["new"]
        if n is None:
            continue
        _sw = n["switch_points"]
        _near = [s for s in _sw if abs(s - n["t_star"]) <= 5.0]
        _both(f"  {r['sb']:g}m {r['lbl']}/{r['side']}：共 {len(_sw)} 個；"
              f"t*={n['t_star']:.6f}；|t−t*|≤5m 者 ＝ "
              + (", ".join(f"{s:.6f}" for s in sorted(_near)) or "（無）"))
        F.append("      全部切換點：" + ", ".join(f"{s:.6f}" for s in _sw))

    # ── 【E】第二層 raise 之格 ───────────────────────────────────────────────
    _both("")
    _err = [r for r in rows if r["new"] is None or r["err"]]
    _both(f"【E】第二層 raise／構造異常之格：{len(_err)}")
    for r in _err:
        _both(f"  {r['sb']:g}m {r['lbl']}/{r['side']}：{(r['err'] or '')[:220]}")
    if not _err:
        _both("  （無）")

    # ── 【F】GB-26 之可證偽檢驗：`m` vs 正典 K-9-7-c 表 ─────────────────────
    _both("")
    _both("【F】GB-26 可證偽檢驗：解析 `m` vs **正典 K-9-7-c 表**（獨立真相源）")
    _both(f"     本輪 DXF ＝ {os.path.relpath(DXF_PATH, REPO)}")
    _both("-" * 138)
    _both(f"{'街廓/側':<11}{'m(解析)':>15}{'m(正典表)':>15}{'Δ':>15}{'相對差':>12}"
          f"{'支(一層)':>9}  註")
    _both("-" * 138)
    for r in [x for x in rows if x["sb"] == 0.0]:
        n = r["new"]
        if n is None:
            continue
        key = (r["lbl"], r["side"])
        cm = CANON_M.get(key, "?")
        if cm is None or cm == "?":
            _both(f"{r['lbl']+'/'+r['side']:<11}{n['m']:>15.9f}"
                  f"{'（表未載）':>15}{'—':>15}{'—':>12}{n['branch_layer1']:>9}")
            continue
        _d = n["m"] - cm
        _rel = (abs(_d) / abs(cm)) if abs(cm) > 1e-12 else float("nan")
        _both(f"{r['lbl']+'/'+r['side']:<11}{n['m']:>15.9f}{cm:>15.9f}"
              f"{_d:>15.2e}{_rel:>12.2%}{n['branch_layer1']:>9}"
              + ("  ← GB-26 之格" if key == ("R4", "left") else ""))
    _both("-" * 138)
    _both("  ⚠️ **只列 Δ、不設閘、不結案**——GB-26 依 KL 明令維持開啟；")
    _both("     ⛔ 不得與 `R2/left` 一併結案（`R2/left` 之一致**不能外推**）。")

    # ── 【G】逐邊分支列舉（**全量·僅 .full.log**）────────────────────────────
    F.append("")
    F.append("【G】逐邊分支之**全量列舉**（每邊之 t 區間／仿射係數／退化支／駁回理由）")
    F.append("-" * 138)
    for r in rows:
        n = r["new"]
        if n is None:
            continue
        F.append(f"  ── {r['sb']:g}m {r['lbl']}/{r['side']}｜"
                 f"c={n['c']:.9g} k={n['k']:.9g} m={n['m']:.9g} w0={n['w0']:.9g} "
                 f"T={n['T']:.4f}｜採 {n['branch']}｜t*={n['t_star']:.9f}")
        for e in (n["l2_edges"] or []):
            _teq = e.get("t_eq")
            _teq_s = "—" if _teq is None else ("%+.6f" % _teq)
            F.append(f"      邊{e['edge']:>3}  t∈[{e['lo']:+.6f}, {e['hi']:+.6f}]  "
                     f"dep_P={e['AP']:+.6f}{e['BP']:+.6f}·t  "
                     f"dep_Q={e['AQ']:+.6f}{e['BQ']:+.6f}·t  t_eq={_teq_s}"
                     + (f"  ⚠️退化支 {e['degenerate']}" if e["degenerate"] else ""))
        F.append(f"      跳過之邊：{n['l2_skipped_edges']}")
        F.append(f"      有效根：{[(x['br'], round(x['t'], 9)) for x in (n['l2_roots'] or [])]}")
        for _br, _t, _why in (n["l2_rejected"] or []):
            F.append(f"      駁回 {_br}  t={_t:+.6f}  ⇒ {_why}")
        for _nt in (n["notes"] or []):
            F.append(f"      note：{_nt}")

    # ── 【H】註記 ────────────────────────────────────────────────────────────
    _both("")
    _both("【H】註記")
    _both("  · 🔴 **段四(c) 已切換**：生產 `_build_corner_range_v3` **已傳** `block_vertices`")
    _both("    （`grep -n -A4 \"_k97 = k97_solve_alloc_t\" app.py` 之四行內含之）"
          " ⇒ 本表「二層」欄即**生產實算**。")
    _both("  · ⛔ **禁二分／取樣／迭代**：切換點為一次減法、每支一次除法（推導 §二〜§四）；")
    _both("    退化（邊平行 ALLOC／斜率為零／無支落區間／多根）一律 **loud raise**。")
    _both("  · ⛔ **K-9-8 紅線**：求 `P_block` 全程只逐邊求「線段 ∩ 無限直線」，")
    _both("    **從不與街廓多邊形取「面」交集**；虛擬量測之面積**未進入任何面積帳**。")
    _both("  · 面積兩欄之**唯一變因是 `t*`**（同一支 `_build_corner_range_v3`、只多傳 "
          "`_t_override`）。")
    _both("  · ⛔ **不得以 `R4/right` 當回歸靶**——其內縮僅比 `_EPS_TOUCH_FRONT` 高約 3mm，"
          "且該 3mm 來自 GB-15 之 R4 圖面誤差；換 `V6_1` 後該實例消失。")
    _both(f"  · 摘要 → {os.path.relpath(LOG, REPO)}；全量 → "
          f"{os.path.relpath(FULL, REPO)}（**同一次跑**）")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    with open(FULL, "w", encoding="utf-8") as f:
        f.write("\n".join(F) + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}\n→ {os.path.relpath(FULL, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
