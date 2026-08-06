# -*- coding: utf-8 -*-
r"""K-6-A2 **段六開工偵察**之實料 — GB-18 接線前提／GB-39 可觸發性／兩門檻分流量級。

⛔ **只查不改·零生產變更·不接 `run_all`·不設任何門檻**（施工單 §四·§六-2）。

## 本檔回答（施工單 §四）

| 題 | 本檔之段 |
|---|---|
| **4-4** 虛擬塊上 `_n14_band_geom` 是否仍適用 | 【A】——逐格實跑，⛔ 非以推理宣稱 |
| **4-5** GB-39 之可觸發性（`P_block` 落截角邊者幾列） | 【B】——**取既有契約旗標 `on_chamfer`**，⛔ 未新造判定 |
| **4-6** 兩門檻分流之土地後果量級 | 【C】——⛔ **只鋪數字·不設門檻**（門檻屬 KL·S6-1 已在待裁清單） |

## ⛔ 單一真相源

虛擬塊由 `app.k98_virtual_measure_block` 建（⛔ 本檔未另寫第二份）；
帶之幾何由 `app._n14_band_geom` 算（同上）。
本檔**自算者僅有** `L_in` 之挑選與截角三角形之判定——二者**逐字沿用**
`verify/probes/probe_k98_virtual_block.py` 之既有作法（該檔為其出處），
⛔ 未改其式；⇒ 二檔於 `w3`／`on_chamfer` 欄應逐格相符（**可交叉複驗**）。

## 🔴 4-4 之所以必須實跑

虛擬塊之前緣是 **`PQ`（非 FRONT_LINE）**、且**伸出街廓多邊形之外**（K-9-8 實作紅線）。
`_n14_band_geom` 之二個判準皆以「臨接容差 `_EPS_TOUCH_FRONT`」界定：
`_fe`（前緣連續段·`|t| ≤ ε`）與 `_re`（後緣連續段·`|dep| ≤ ε`）。
**二者在虛擬塊上是否仍成立，是碼面事實、不是推論** ⇒ 逐格跑、逐格印。

## 重跑

    python verify/probes/probe_K9_seg6_recon.py

輸出 `verify/out/probe_K9_seg6_recon.log`。rc 恆 0。
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_seg6_recon.log")


def _alloc_edges(coords, auh):
    """宗地環上**平行 ALLOC 方向**之邊（沿用 `probe_k98_virtual_block.py` 之式）。"""
    _out = []
    for _i in range(len(coords) - 1):
        _a, _b = coords[_i], coords[_i + 1]
        _dx, _dy = float(_b[0]) - float(_a[0]), float(_b[1]) - float(_a[1])
        _n = math.hypot(_dx, _dy)
        if _n < 1e-9:
            continue
        if abs((_dx / _n) * auh[1] - (_dy / _n) * auh[0]) < 1e-3:
            _out.append((_a, _b))
    return _out


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 150)
    L.append("【K-6-A2 段六 開工偵察】GB-18 接線前提／GB-39 可觸發性／兩門檻分流量級"
             " — ⛔ 只查不改·不設門檻")
    L.append("=" * 150)

    ns, fake_st = harvest()
    for _s in ("k98_virtual_measure_block", "_n14_band_geom", "parcel_min_width_n14",
               "_make_chamfer_tri_wb", "get_min_lot_size", "_baseline_pts_from_manual",
               "_EPS_TOUCH_FRONT"):
        if _s not in ns:
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    _EPS = float(ns["_EPS_TOUCH_FRONT"])
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}

    recs = []
    for setback in (0.0, 3.5):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s2, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, winners, forced, setback)
        by_pid = {str(r.get("暫編地號")): r for r in sg["g_rows"]}
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
            au = al_by.get(lbl)
            if not au:
                continue
            _nrm = math.hypot(float(au[0]), float(au[1]))
            auh = (float(au[0]) / _nrm, float(au[1]) / _nrm)
            _mw = ns["get_min_lot_size"](
                b["category"], float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
            _lw = float(_mw.get("min_width", 0.0) or 0.0)
            for side in ("left", "right"):
                if side not in (sd_by.get(lbl) or {}):
                    continue
                rec = {"sb": f"{setback:g}m", "lbl": lbl, "side": side,
                       "lw": _lw, "thr_corner": setback + _lw}
                w = (winners or {}).get(lbl) or {}
                pid = w.get("p1_end" if side == "left" else "p2_end")
                rec["pid"] = pid
                if not pid:
                    rec["note"] = "無 winner（強制留設抵費地）"
                    recs.append(rec); continue
                row = by_pid.get(str(pid))
                cc = (row or {}).get("cut_coords") or []
                if len(cc) < 3:
                    rec["note"] = f"cut_coords 不足（{len(cc)}）"
                    recs.append(rec); continue
                sd = sd_by[lbl][side]
                F1, F2 = fl["p1"], fl["p2"]
                _dxy = (float(F2[0]) - float(F1[0]), float(F2[1]) - float(F1[1]))
                _dl = math.hypot(*_dxy)
                dh = (_dxy[0] / _dl, _dxy[1] / _dl)
                _edges = _alloc_edges(cc, auh)
                if not _edges:
                    rec["note"] = "無平行 ALLOC 之邊 ⇒ L_in 不可定"
                    recs.append(rec); continue

                def _s_of(p, _F1=F1, _dh=dh):
                    return ((p[0] - float(_F1[0])) * _dh[0]
                            + (p[1] - float(_F1[1])) * _dh[1])
                _sx = _s_of((float(sd["p1"][0]), float(sd["p1"][1])))
                _edges.sort(key=lambda e: abs((_s_of(e[0]) + _s_of(e[1])) / 2.0 - _sx))
                _lin = _edges[-1]
                _cham = ns["_make_chamfer_tri_wb"](b, side)
                _oc = None
                if _cham is not None and not _cham.is_empty:
                    from shapely.geometry import Point as _PT
                    _oc = (lambda _p, _t=_cham:
                           bool(_t.buffer(1e-9).contains(_PT(_p[0], _p[1]))))
                try:
                    k98 = ns["k98_virtual_measure_block"](
                        b.get("vertices"), [F1, F2], bp, [_lin[0], _lin[1]],
                        [sd["p1"], sd["p2"]], _label=lbl, _pid=str(pid),
                        _lot_kind="corner_first", on_chamfer=_oc)
                except RuntimeError as e:
                    rec["note"] = "k98 raise：" + str(e).splitlines()[0][:70]
                    recs.append(rec); continue
                rec["w3"] = k98["min_width"]
                rec["dep3"] = k98["depth_from_PQ"]
                rec["cham"] = k98["on_chamfer"]
                rec["onfront"] = k98["on_front"]
                rec["inset"] = k98["inset_from_front"]
                # ── 4-4 之核心：於**虛擬塊**上實跑 `_n14_band_geom` ──────────────
                _poly = k98["poly"]
                _pb = k98["P_block"]
                try:
                    _tlo, _rear, _g, _bdn = ns["_n14_band_geom"](
                        list(_poly.exterior.coords), dh, (_pb[0], _pb[1]), bp,
                        _label=f"{lbl}/{side}·k98")
                    rec["bg"] = (_tlo, _rear[0][0], len(_rear), abs(_rear[0][1]), _g, _bdn)
                except RuntimeError as e:
                    rec["bgerr"] = str(e).splitlines()[0][:110]
                recs.append(rec)

    # ── 【A】4-4 虛擬塊上 `_n14_band_geom` 之適用性（**逐格實跑**）────────────────
    L.append("")
    L.append("【A】4-4 虛擬塊上 `_n14_band_geom` 是否仍適用（**逐格實跑·⛔ 非推理**）")
    L.append("-" * 150)
    L.append(f"  容差 `_EPS_TOUCH_FRONT` ＝ {_EPS}（`_fe` 與 `_re` 共用同一把尺）")
    L.append(f"{'情境':<6}{'街廓/側':<12}{'街角第1宗':<13}"
             f"{'t_lo':>11}{'帶底t_hi':>12}{'n後緣':>6}{'後緣|dep|':>12}"
             f"{'g':>11}{'(b̂n·n̂)':>12}{'k98深度':>11}{'Δ(帶底−k98深)':>14}  適用？")
    L.append("-" * 150)
    _ok_bg, _bad_bg, _skip, _dmax = 0, [], [], 0.0
    for r in recs:
        _tag = f"{r['lbl']}/{r['side']}"
        if 'bg' in r:
            _tlo, _thi, _nre, _dep0, _g, _bdn = r['bg']
            _ok_bg += 1
            _dd = _thi - r['dep3']
            _dmax = max(_dmax, abs(_dd))
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"{_tlo:>11.6f}{_thi:>12.6f}{_nre:>6}{_dep0:>12.3e}"
                     f"{_g:>11.6f}{_bdn:>12.9f}{r['dep3']:>11.6f}{_dd:>14.6f}  ✅ 成立")
        elif 'bgerr' in r:
            _bad_bg.append(r)
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"  🔴 raise：{r['bgerr']}")
        else:
            _skip.append(r)
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"  ⏭️ 未達 k98：{r.get('note', '')}")
    L.append("-" * 150)
    L.append(f"  ⇒ `_n14_band_geom` 於虛擬塊上**成立 {_ok_bg} 格**／raise {len(_bad_bg)} 格"
             f"／未達 k98 {len(_skip)} 格")
    L.append("  🔒 判讀：`_fe` 以 `PQ` 為 `t=0`（`front_pt` 傳 `P_block`）、"
             "`_re` 以 BASELINE 為據（K-9-8 (4) 之虛擬塊遠側界即 BASELINE）")
    L.append("  ⚠️ 「成立」僅指**二判準可辨**；其值是否為 K-9-5 所欲之量，屬段六之題、本檔不判。")
    L.append("")
    L.append(f"  🔴 **A-2 段六之前置決策項**：`帶底 t_hi` 與 k98 之 `depth_from_PQ`"
             f" **不是同一個量**——逐格 max|Δ| ＝ **{_dmax:.6f} m**（⚠️ **＞ 法定粒度 0.01**）。")
    L.append("     · `depth_from_PQ` ＝ `_dep()` 之**沿 BASELINE 法向**距離（k98 (5)）；")
    L.append("     · `帶底 t_hi` ＝ **後緣連續段最淺端點之 `t`**（K-9-6-b·(c)-1 更正後）。")
    L.append("     ⇒ 二者為「同名不同量」之又一例（體例同 K-9-6-a）。**段六接線前須先定用哪一個**；")
    L.append("       ⛔ 本檔**不代判**——現行 k98 係把 `depth_from_PQ` 當 `min_depth` 餵給"
             "`parcel_min_width_n14`（走**舊帶**分支），切換為新帶即改由 `_n14_band_geom` 定帶底。")

    # ── 【B】4-5 GB-39 可觸發性（**取既有契約旗標**·⛔ 未新造判定）─────────────
    L.append("")
    L.append("【B】4-5 GB-39 可觸發性：`P_block` 是否落在**道路截角邊**上")
    L.append("-" * 150)
    L.append("  🔒 資料源 ＝ k98 之契約旗標 `on_chamfer`（⛔ 本檔未新造判定式）；"
             "`None` ＝ **該側無截角可判**（≠ 判定為否）")
    _cnt = {}
    for r in recs:
        _k = ('—' if 'cham' not in r else str(r['cham']))
        _cnt[_k] = _cnt.get(_k, 0) + 1
        if 'cham' in r:
            L.append(f"  {r['sb']:<6}{r['lbl']}/{r['side']:<6}{str(r.get('pid')):<13}"
                     f"on_chamfer={str(r['cham']):<6}"
                     f"on_front={str(r['onfront']):<6}inset={r['inset']:+.6f}")
    L.append(f"  ⇒ 分布：{_cnt}")
    L.append("  ⚠️ **契約旗標之存活**：本檔係**直接呼叫** `k98_virtual_measure_block` 取得之；")
    L.append("     其於生產路徑（`_build_corner_range_v3`）是否被丟棄，**本檔未查**"
             "——⛔ 不得以本段之有值推斷生產路徑亦有值。")

    # ── 【C】4-6 兩門檻分流之量級（⛔ 只鋪數字·不設門檻）───────────────────────
    L.append("")
    L.append("【C】4-6 兩門檻之量級對照（⛔ **不設門檻·不作判定**·門檻屬 KL）")
    L.append("-" * 150)
    L.append("  正典 K-9-5：街角第 1 宗門檻 ＝ **退縮寬 ＋ 畸零地最小寬**；其餘 ＝ 畸零地最小寬")
    L.append(f"{'情境':<6}{'街廓/側':<12}{'街角第1宗':<13}"
             f"{'k98量得寬':>12}{'畸零最小寬':>12}{'退縮+最小寬':>13}{'差(量−街角門檻)':>16}")
    L.append("-" * 150)
    for r in recs:
        if 'w3' not in r:
            continue
        _d = r['w3'] - r['thr_corner']
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{str(r.get('pid')):<13}"
                 f"{r['w3']:>12.6f}{r['lw']:>12.2f}{r['thr_corner']:>13.2f}{_d:>16.6f}")
    L.append("-" * 150)
    L.append("  ⛔ 上表**不是判定表**：K-9-5 尚未上閘、街角宗現走 K-4 面積門檻豁免；")
    L.append("     `S6-1` 已在待裁清單（交接文 §二），本檔僅補其**量**。")

    L.append("")
    L.append("【D】註記")
    L.append("  · ⛔ 零生產變更：本檔未動 `app.py`、未動 `verify/` 既有檔、不接 `run_all`。")
    L.append("  · 虛擬塊與帶幾何**皆由 app 真符號產出**；本檔自算者僅 `L_in` 挑選與截角判定，"
             "二者逐字沿用 `verify/probes/probe_k98_virtual_block.py` ⇒ `w3`／`on_chamfer` 可交叉複驗。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
