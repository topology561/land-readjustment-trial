# -*- coding: utf-8 -*-
r"""K-9-6-b-2 乙式 — **階段 A**：以**甲式夾具**對拍**乙式引擎**（K-6-A2 段四(c)-2(a′)）。

## 為何要有這一階段（施工單 §三·⛔ 不得與階段 B 合併）

乙式同時改**引擎**（`k97_solve_alloc_t` 第二層）與**夾具**
（`fixture_corner_range_k8._band_min_width`）。若兩邊一起改，對拍恆綠 ⇒ **驗不到東西**。
⇒ 先只改引擎、夾具**逐字不動**，此時夾具（甲式）量得之最小寬應偏離靶 `T`，
且偏離量有**閉式預測**：

```
殘差 = W_甲(t*_乙) − T = −k · δ_P(t*_乙)
```

（引擎已令 `W_乙(t*_乙) = T`；甲式帶 ＝ `[0, D_new]`、乙式帶 ＝ `[δ_P, δ_P+D_new]`，
二者只差把帶整體平移 `δ_P` ⇒ `W` 差 `k·δ_P`。推導見
`docs/reports/W-G.5_K6-A2-段四c2a2_乙式八支推導.md` §六。）

🔴 **`k` 取解析 `∂w/∂d`**（`k97_solve_alloc_t` 回傳之 `k`），
⛔ **不得取正典 K-9-7-c 表之 `k` 欄**——該欄係擾動觀測 `∂W/∂D`、`k ≥ 0` 時恆觀測為 0。

## ⭐ 最具鑑別力之一條

`R3/right 0m` 與 `R1/left 0m` 於**甲式**下殘差為 **0**（分支 ①·上緣釘 FRONT ⇒ 深度不影響）。
**乙式**下上緣改為 `PQ(t)` ⇒ 該二格應躍為**最大與次大**。
**若殘差排序不是這樣、或該二格仍為 0 ⇒ 乙式推導 §五 之「分支 ① 失去與邊無關性質」沒做到、實作錯。**

## 手法

「乙式引擎」之幾何以 `_t_override` 注入第二層 `t*` 取得（段三(a) 已入庫之純加性參數）
⇒ **生產碼一字未改、第二層維持零生產呼叫點**。
夾具側**逐字呼叫其自身之** `_alloc_edge_of`／`_range_min_depth`／`_band_min_width`
（⛔ 不在本檔重寫第四份量測），並另**整支跑一次** `fixture_corner_range_k8.main()`
以取其**自身之判定與 rc**。

## 重跑

    python verify/probes/probe_K9_7d_stageA.py

**rc 恆 0**（診斷·不作為閘）。輸出 `verify/out/probe_K9_7d_stageA.log`。
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
import fixture_corner_range_k8 as fx                                # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_7d_stageA.log")

# 施工單 §三 階段 A 之**預先登記**預測（量級·m）——⛔ 判準為同號＋同量級，
#   ⛔ 不得要求逐位元相等（`δ_P` 隨 `t` 變動、`t*` 亦重解）。
PREDICT = {
    ("0m", "R3/right"): 4.53e-03,
    ("0m", "R1/left"): 1.63e-03,
    ("0m", "R4/right"): 7.30e-04,
    ("3.5m", "R4/right"): 7.02e-04,
    ("3.5m", "R4/left"): 5.26e-05,
    ("0m", "R4/left"): 2.63e-05,
}
PREDICT_REST = 3.13e-06        # 其餘 10 格之上界


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 132)
    L.append("【K-9-6-b-2 乙式·階段 A】甲式夾具 × 乙式引擎 —— **只算不換**"
             "（K-6-A2 段四(c)-2(a′)）")
    L.append("預測：殘差 ＝ −k·δ_P（k ＝ 解析 ∂w/∂d·⛔ 非正典 K-9-7-c 表之觀測 k）")
    L.append("=" * 132)

    ns, fake_st = harvest()
    for _s in ("k97_solve_alloc_t", "_build_corner_range_v3", "_make_chamfer_tri_wb",
               "_corner_range_eps"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    sd_by = cad.get("side_lines_by_side", {}) or {}
    fl_by = cad.get("front_lines", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}

    T_NEW = {}
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
                mw = float(ns["get_min_lot_size"](
                    b["category"],
                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
                _fp = [fl["p1"], fl["p2"]]
                _bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
                _sp = [sd_by[lbl][side]["p1"], sd_by[lbl][side]["p2"]]
                _chi = ns["_make_chamfer_tri_wb"](b, side)
                _depth = float(snapshot["blocks"][lbl]["街廓分配深度_m"])
                _q = ((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected")
                r = ns["k97_solve_alloc_t"](
                    b.get("centroid"), _fp, _bp, _sp, al_by.get(lbl),
                    setback, mw, chamfer_tri=_chi, block_depth=_depth,
                    _label=lbl, _side=side, block_vertices=b.get("vertices"))
                # 🔒 key **含 `min_width`**：夾具之 T3（`min_width=1e4`）與 T4（缺件）
                #   須落在**注入不到**之路徑上，否則會把「判別力反例」餵成正常解、
                #   使 T3／T4 假綠（⛔ 那等於把夾具的牙拔掉）。
                T_NEW[(lbl, side, setback, round(mw, 9))] = r["t_star"]
                # 乙式引擎之幾何（以 `_t_override` 注入·生產碼一字未改）
                poly = ns["_build_corner_range_v3"](
                    b.get("vertices"), b.get("centroid"), _fp, _bp, _sp,
                    al_by.get(lbl), _depth, setback, mw, _chi,
                    dxf_quantum=_q, _label=lbl, _side=side,
                    _t_override=r["t_star"])
                # ── 夾具之量測（**逐字呼叫夾具自身之函式**·⛔ 不重寫第四份）────────
                #   甲式 ＝ `delta_p=0.0`（帶 `[0, D]`）；乙式 ＝ `delta_p=δ_P`（帶 `[δ_P, δ_P+D]`）。
                #   ⇒ 階段 A／B **由同一支夾具函式**產出，⛔ 本檔未另寫一套甲式量測。
                edge = fx._alloc_edge_of(poly, cad, lbl)
                _rmd = (None if edge is None
                        else fx._range_min_depth(cad, cb_by, lbl, side, edge))
                Dt, dP_fx = (None, None) if _rmd is None else _rmd
                w_a = w_b = None
                if _rmd is not None:
                    w_a = fx._band_min_width(cad, cb_by, lbl, side, Dt, edge,
                                             delta_p=0.0)
                    w_b = fx._band_min_width(cad, cb_by, lbl, side, Dt, edge,
                                             delta_p=dP_fx)
                T = setback + mw
                rows.append({
                    "tag": f"{setback:g}m", "key": f"{lbl}/{side}",
                    "k": r["k"], "dP": r["delta_P"], "dP_fx": dP_fx, "T": T,
                    "w": w_a, "res": (None if w_a is None else w_a - T),
                    "resB": (None if w_b is None else w_b - T),
                    "pred": (None if w_a is None else -r["k"] * r["delta_P"]),
                    "br": r["branch"], "br1": r["branch_layer1"],
                    "eps": float(ns["_corner_range_eps"](_q)),
                })

    # ── 【A】逐格：夾具（甲式）殘差 vs 閉式預測 ────────────────────────────────
    L.append("")
    L.append("【A】**階段 A**（甲式帶 `[0, D]`）之殘差 vs 閉式預測 `−k·δ_P`"
             "｜末欄為**階段 B**（乙式帶 `[δ_P, δ_P+D]`）（依 |階段 A 殘差| 由大到小）")
    L.append("-" * 132)
    L.append(f"{'情境':<6}{'街廓/側':<11}{'支(一層)':>9}{'支(乙式)':>13}"
             f"{'k(解析)':>14}{'δ_P(引擎)':>12}{'δ_P(夾具)':>12}{'A殘差(m)':>12}"
             f"{'預測−k·δ_P':>13}{'施工單預告':>11}{'B殘差(m)':>12}  判")
    L.append("-" * 132)
    _bad = []
    for r in sorted(rows, key=lambda x: -(abs(x["res"] or 0.0))):
        if r["res"] is None:
            L.append(f"{r['tag']:<6}{r['key']:<11}  🔴 夾具量不出（ALLOC 邊／D(t*) 缺）")
            _bad.append((r["tag"], r["key"], "夾具量不出"))
            continue
        _d = r["res"] - r["pred"]
        _sheet = PREDICT.get((r["tag"], r["key"]))
        _sh = ("%.2e" % _sheet) if _sheet is not None else f"≤{PREDICT_REST:.2e}"
        # 判準：與閉式預測**同號且同量級**（相對差 < 5%，或二者皆 < 1e-9）
        _ok = (abs(_d) < 1e-9) or (abs(r["pred"]) > 0
                                   and abs(_d) / abs(r["pred"]) < 0.05)
        # 🔒 引擎與夾具**各自**算出之 `δ_P` 須相符（二份獨立實作·⛔ 非互相取值）
        _dok = abs(r["dP"] - (r["dP_fx"] if r["dP_fx"] is not None else 1e9)) < 1e-9
        if not _ok:
            _bad.append((r["tag"], r["key"], f"殘差 {r['res']:.3e} vs 預測 {r['pred']:.3e}"))
        if not _dok:
            _bad.append((r["tag"], r["key"],
                         f"δ_P 引擎 {r['dP']:.9f} ≠ 夾具 {r['dP_fx']:.9f}"))
        L.append(f"{r['tag']:<6}{r['key']:<11}{r['br1']:>9}{r['br']:>13}"
                 f"{r['k']:>14.9f}{r['dP']:>12.6f}{(r['dP_fx'] or 0.0):>12.6f}"
                 f"{r['res']:>12.3e}{r['pred']:>13.3e}{_sh:>11}{r['resB']:>12.2e}"
                 f"  {'✅' if (_ok and _dok) else '🔴'}")
    L.append("-" * 132)
    L.append(f"  ⇒ 與閉式預測（或 δ_P 二份實作）不符之格：**{len(_bad)}**"
             + ("（**須停機上呈**）" if _bad else "（逐格相符 ✅）"))
    for t_, k_, why in _bad:
        L.append(f"     🔴 {t_} {k_}：{why}")
    _mxB = max(abs(r["resB"]) for r in rows if r["resB"] is not None)
    L.append(f"  ⇒ **階段 B** 之最大 |殘差| ＝ {_mxB:.3e} m"
             f"（{'✅ ~1e-10 量級' if _mxB < 1e-8 else '🔴 未回到 ~1e-10'}）")

    # ── 【B】⭐ 鑑別力：分支 ① 之二格是否由 0 躍為最大／次大 ──────────────────
    L.append("")
    L.append("【B】⭐ 鑑別力（施工單 §三 階段 A）：分支 ① 之二格於甲式下殘差為 0，"
             "乙式下應為最大與次大")
    L.append("-" * 132)
    _rank = [r for r in sorted(rows, key=lambda x: -(abs(x["res"] or 0.0)))
             if r["res"] is not None]
    for _i, r in enumerate(_rank[:4], 1):
        L.append(f"  第 {_i} 名：{r['tag']} {r['key']}"
                 f"（支(一層) {r['br1']}）｜|殘差| {abs(r['res']):.3e} m")
    _top2 = {(r["tag"], r["key"]) for r in _rank[:2]}
    _want = {("0m", "R3/right"), ("0m", "R1/left")}
    _disc = (_top2 == _want)
    L.append(f"  ⇒ 前二名 ＝ {sorted(_top2)}；施工單預告 ＝ {sorted(_want)}"
             f"  {'✅ 相符' if _disc else '🔴 不符 ⇒ 分支 ① 未併入逐邊通式，實作錯'}")

    # ── 【C】夾具**整支跑一次**之自身判定（patch 注入乙式 t*）──────────────────
    L.append("")
    L.append("【C】`fixture_corner_range_k8.main()` 之自身判定（patch 注入乙式 `t*`）")
    L.append("    ⚠️ **本節之判定隨夾具之世代而異**：")
    L.append("      · 夾具為**甲式**（§二-2 施工前）⇒ 這是**階段 A** ⇒ 預期 **rc=1 / FAIL**")
    L.append("        （as-run 存證：`verify/out/probe_K9_7d_stageA_asrun.log`）")
    L.append("      · 夾具為**乙式**（§二-2 施工後）⇒ 這是**階段 B** ⇒ 預期 **rc=0 / PASS**")
    L.append("-" * 132)
    _orig = ns["_build_corner_range_v3"]
    _hit = {"n": 0}

    def _patched(*a, **kw):
        if kw.get("_t_override") is None:
            try:
                key = (kw.get("_label"), kw.get("_side"),
                       float(kw.get("setback")), round(float(kw.get("min_width")), 9))
            except (TypeError, ValueError):
                key = None                      # 缺件（T4）⇒ 不注入、讓夾具照常 raise
            if key in T_NEW:
                kw = dict(kw)
                kw["_t_override"] = T_NEW[key]
                _hit["n"] += 1
        return _orig(*a, **kw)

    ns["_build_corner_range_v3"] = _patched
    _buf = io.StringIO()
    _save = sys.stdout
    try:
        sys.stdout = _buf
        _rc = fx.main()
    finally:
        sys.stdout = _save
        ns["_build_corner_range_v3"] = _orig
    _txt = _buf.getvalue()
    for _ln in _txt.splitlines():
        if re.match(r"^\s{2}R\d\s+(left|right)\s+\d", _ln) or _ln.startswith("RESULT:"):
            L.append("  " + _ln.strip())
    L.append(f"  ⇒ patch 命中 {_hit['n']} 次｜**夾具 rc ＝ {_rc}**"
             f"（{'FAIL' if _rc else 'PASS'}）"
             f"　⇒ 本次所跑之夾具世代 ＝ **{'甲式（階段 A）' if _rc else '乙式（階段 B）'}**")
    L.append("  ⚠️ ⛔ **本節之 rc 不是「生產已切換」之證據**——它跑的是"
             "**注入乙式 `t*` 之幾何**；生產 `_build_corner_range_v3` 仍走第一層。")

    L.append("")
    L.append("【D】註記")
    L.append("  · **只算不換**：第二層維持零生產呼叫點；patch 僅存在於本行程。")
    L.append("  · 夾具側之量測**逐字呼叫夾具自身之** `_alloc_edge_of`／`_range_min_depth`／"
             "`_band_min_width`，")
    L.append("    ⛔ 本檔未重寫第四份量測——否則對拍就變成「本檔 vs 引擎」而非「夾具 vs 引擎」。")
    L.append("  · ⛔ 判準為**同號 ＋ 同量級**，不得要求逐位元相等"
             "（`δ_P` 隨 `t` 變動、`t*` 亦重解）。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
