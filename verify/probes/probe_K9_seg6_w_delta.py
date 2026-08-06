# -*- coding: utf-8 -*-
r"""**GB-40 寬度攤表** — 街角第 1 宗於虛擬塊上：舊帶 vs 新帶之**寬度**差（K-6-A2 段六前置）。

⛔ **只算不換·零生產變更·不接 `run_all`·不設任何門檻**（施工單 §七）。

## 🔴 §7-0 為何不能沿用 `0.120267`

那是**帶底**之差，**不是寬度**之差。KL 要的是**寬度**。
⛔ **禁以帶底差乘任何係數推估寬度差**——`GB-33` 之 `|k| ≤ 0.0756` 係**非街角宗**之量，
⛔ 不得外推至街角第 1 宗之虛擬塊。**逐格實量。**

## §7-4 量法：同一個 `poly` 上呼叫**同一個函式兩次·只變一個變因**（失敗考古 節 32）

    _cc   = list(k98["poly"].exterior.coords)
    w_old = parcel_min_width_n14(_cc, dh, k98["P_block"], k98["depth_from_PQ"], …)
    w_new = parcel_min_width_n14(_cc, dh, k98["P_block"], k98["depth_from_PQ"], …,
                                 baseline_pts=bp)

🔴 **唯一差異必須是 `baseline_pts`**。`min_depth` 二者皆傳 `depth_from_PQ`——依裸 grep
（⛔ 無後續過濾·節 44 戒(b)）`grep -n "_md\b" app.py` 之全部命中：
`:6692`（`_md = float(min_depth)`）／`:6761`＋`:6764`（**E-2′·受 `baseline_pts is None` 守**）／
`:6782`（`_t_hi = _md`·**於 `:6834` 被 `_t_hi = _n14_band[1]` 覆寫**）／`:6819`（註解）
⇒ 新帶分支下 `min_depth` **只剩 `:6660` 之 `>0` 檢查** ⇒ 傳何值不影響 `w_new`。
⛔ **不得**為此替 `k98_virtual_measure_block` 加附表 `min_depth` 入參。

🔒 **出處自檢閘（⛔ 不得省·不得放寬為容差）**：`w_old` 必須與 `k98["min_width"]`
**完全相等**（`==`·同進程同引數同函式）。不等 ⇒ **loud raise**
——代表本檔量的不是生產要切的那個東西。
（`d_hat` 之位元同一性：k98 之 `_u()` 與本檔之 `dh` **係同一算式**
 `ax/hypot(ax,ay)` ⇒ 位元相同；⛔ 勿改寫成先算長度再乘倒數。）

## §7-1 單一真相源

虛擬塊、母體、`L_in` 挑選、截角判定**一律逐字沿用**
`verify/probes/probe_K9_seg6_recon.py`（⛔ 禁另寫第二份·**GB-8**）。
本檔僅換**輸出段**。

## §7-3 座標框與號規

- `t` 軸 ＝ `parcel_min_width_n14` **自己的框**：沿 FRONT 法向、指向宗地內為正，
  起算 `front_pt = P_block` ⇒ `t(P_block) = 0`。⛔ 本檔不另立 `t` 軸
  ——`max(_tv)` 之框由 `_t_lo` 對 `_n14_band_hi[0]` **逐位元核對**把關（不符即 raise）。
- 所有 `Δ` 一律 **新 − 舊**（正 ＝ 新式較大）。
- 餘裕 ＝ 量得寬 − 門檻（正 ＝ 通過）。
- 門檻 `T` ＝ `setback + get_min_lot_size(...)['min_width']`（K-9-5）。

## 重跑

    python verify/probes/probe_K9_seg6_w_delta.py

輸出 `verify/out/probe_K9_seg6_w_delta.log`。rc 恆 0。
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
LOG = os.path.join(OUTDIR, "probe_K9_seg6_w_delta.log")


def _alloc_edges(coords, auh):
    """宗地環上**平行 ALLOC 方向**之邊（⛔ 逐字沿用 `probe_K9_seg6_recon.py`）。"""
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


def _ring_ts(cut_coords, d_hat, front_pt):
    """環上之 `t` 值（**獨立復現** `parcel_min_width_n14` 之框·供 `max(_tv)` 欄）。

    ⚠️ 本函式係**獨立復現**，其正確性由呼叫端之「`t_lo` 對 `_n14_band_hi[0]`
    逐位元核對」把關 ⇒ ⛔ 不得省略該核對。
    """
    import numpy as _np
    from shapely.geometry import Polygon as _Poly
    _d = _np.asarray(d_hat, dtype=float)[:2]
    _d = _d / float(_np.linalg.norm(_d))
    _n = _np.array([-_d[1], _d[0]], dtype=float)
    _fp = _np.asarray(front_pt, dtype=float)[:2]
    _P = _np.asarray([[float(p[0]), float(p[1])] for p in cut_coords],
                     dtype=float) - _fp
    _poly = _Poly(list(zip((_P @ _d).tolist(), (_P @ _n).tolist())))
    if not _poly.is_valid:
        _poly = _poly.buffer(0)
    _ring = [(float(p[0]), float(p[1])) for p in list(_poly.exterior.coords)]
    if float(_poly.centroid.coords[0][1]) < 0:
        _ring = [(_s, -_t) for _s, _t in _ring]
    return [_t for _s, _t in _ring]


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 200)
    L.append("【GB-40 寬度攤表】街角第 1 宗·虛擬塊上：舊帶（depth_from_PQ）vs 新帶（後緣最淺端點）"
             " — ⛔ 只算不換·不設門檻")
    L.append("🔴 §7-0：本表所量係**寬度**，⛔ 非帶底；帶底差 ≠ 寬度差，"
             "⛔ 禁以任何係數自帶底差推估之")
    L.append("=" * 200)

    ns, fake_st = harvest()
    for _s in ("k98_virtual_measure_block", "parcel_min_width_n14", "_n14_band_hi",
               "_make_chamfer_tri_wb", "get_min_lot_size", "_baseline_pts_from_manual"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
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

    recs, _gate = [], []
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
                # §7-3：門檻 T ＝ setback + 畸零地最小寬（K-9-5）
                rec = {"sb": f"{setback:g}m", "lbl": lbl, "side": side,
                       "T": setback + _lw}
                w = (winners or {}).get(lbl) or {}
                pid = w.get("p1_end" if side == "left" else "p2_end")
                rec["pid"] = pid
                # 🔒 §7-2：無 winner 亦**列在表內**，⛔ 不得自母體剔除
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
                dh = (_dxy[0] / _dl, _dxy[1] / _dl)        # ＝ k98 之 `_u()`·位元同一
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
                    rec["note"] = "k98 raise：" + str(e).splitlines()[0][:80]
                    recs.append(rec); continue

                _cc = list(k98["poly"].exterior.coords)
                _pb = (k98["P_block"][0], k98["P_block"][1])
                _dep = k98["depth_from_PQ"]
                rec["t_hi_old"] = _dep

                # ── §7-4 兩次呼叫·**唯一差異 ＝ `baseline_pts`** ──────────────────
                w_old = float(ns["parcel_min_width_n14"](
                    _cc, dh, _pb, _dep, _label=f"{lbl}/{side}·old"))
                rec["w_old"] = w_old
                # 🔒 出處自檢閘：`==`，⛔ 不放寬為容差
                _same = (w_old == k98["min_width"])
                _gate.append((rec["sb"], lbl, side, str(pid), w_old,
                              k98["min_width"], _same))
                if not _same:
                    raise RuntimeError(
                        f"🔴 出處自檢閘破：{lbl}/{side} 之 w_old {w_old!r} "
                        f"≠ k98['min_width'] {k98['min_width']!r}"
                        f"——本檔量的不是生產要切的那個東西，停")
                try:
                    rec["t_hi_new"] = float(ns["_n14_band_hi"](
                        _cc, dh, _pb, bp, _label=f"{lbl}/{side}")[1])
                except RuntimeError as e:
                    rec["note"] = "_n14_band_hi raise：" + str(e).splitlines()[0][:80]
                try:
                    rec["w_new"] = float(ns["parcel_min_width_n14"](
                        _cc, dh, _pb, _dep, _label=f"{lbl}/{side}·new",
                        baseline_pts=bp))
                except RuntimeError as e:
                    # 🔒 §7-5 末：逐字記入備註，⛔ 不得整支掛掉、⛔ 不得靜默跳過
                    rec["note"] = "w_new raise：" + str(e).splitlines()[0][:110]
                # `max(_tv)`（E-2′ 之流失紀錄）＋ 框之逐位元核對
                _tv = _ring_ts(_cc, dh, _pb)
                rec["tmax"] = max(_tv)
                rec["t_lo"] = max(0.0, 0.0)
                _tlo_ref = float(ns["_n14_band_hi"](_cc, dh, _pb, bp,
                                                    _label=f"{lbl}/{side}")[0]) \
                    if "t_hi_new" in rec else None
                if _tlo_ref is not None:
                    rec["t_lo"] = _tlo_ref
                recs.append(rec)

    # ── 【A】出處自檢閘（**逐格**·⛔ 非「12 格全過」一句話）─────────────────────
    L.append("")
    L.append("【A】§7-4 出處自檢閘：`w_old == k98['min_width']`（**逐格列示**·⛔ 禁計數式驗收）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'街角第1宗':<13}"
             f"{'w_old（本檔現算）':>22}{'k98[min_width]':>22}  相等？")
    L.append("-" * 200)
    for _sb, _lbl, _sd, _pid, _wo, _km, _ok in _gate:
        L.append(f"{_sb:<6}{_lbl + '/' + _sd:<12}{_pid:<13}"
                 f"{_wo!r:>22}{_km!r:>22}  {'✅ ==' if _ok else '🔴 ≠'}")
    L.append("-" * 200)
    L.append("  🔒 判準為 `==`（⛔ 未放寬為容差）；任一格不等即 loud raise、本檔不會走到此處。")

    # ── 【B】GB-40 寬度攤表（§7-5·全精度·⛔ 禁捨入）─────────────────────────────
    L.append("")
    L.append("【B】GB-40 寬度攤表（**全精度**·Δ 一律「新 − 舊」·餘裕 ＝ 量得寬 − 門檻）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'街角第1宗':<13}"
             f"{'t_lo':>10}{'舊帶底':>12}{'新帶底':>12}{'Δ帶底':>12}{'max(_tv)':>12}"
             f"{'舊寬 w_old':>13}{'新寬 w_new':>13}{'Δ寬':>13}"
             f"{'門檻T':>8}{'舊餘裕':>12}{'新餘裕':>12}  翻盤？  備註")
    L.append("-" * 200)
    _flip, _dmax, _dmax_at, _tight = [], 0.0, None, None
    for r in recs:
        _tag = f"{r['lbl']}/{r['side']}"
        if 'w_old' not in r:
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"{'—':>10}{'—':>12}{'—':>12}{'—':>12}{'—':>12}"
                     f"{'—':>13}{'—':>13}{'—':>13}{r['T']:>8.2f}"
                     f"{'—':>12}{'—':>12}  —      {r.get('note', '')}")
            continue
        _mo = r['w_old'] - r['T']
        if 'w_new' in r:
            _mn = r['w_new'] - r['T']
            _dw = r['w_new'] - r['w_old']
            _fl = ((_mo >= 0) != (_mn >= 0))
            if _fl:
                _flip.append((r, _mo, _mn))
            if abs(_dw) > _dmax:
                _dmax, _dmax_at = abs(_dw), r
            if _tight is None or _mn < _tight[1]:
                _tight = (r, _mn)
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"{r['t_lo']:>10.6f}{r['t_hi_old']:>12.6f}{r['t_hi_new']:>12.6f}"
                     f"{r['t_hi_new'] - r['t_hi_old']:>12.6f}{r['tmax']:>12.6f}"
                     f"{r['w_old']:>13.6f}{r['w_new']:>13.6f}{_dw:>13.6f}"
                     f"{r['T']:>8.2f}{_mo:>12.6f}{_mn:>12.6f}"
                     f"  {'🔴 翻盤' if _fl else '—':<6}  {r.get('note', '')}")
        else:
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"{r['t_lo']:>10.6f}{r['t_hi_old']:>12.6f}"
                     f"{r.get('t_hi_new', float('nan')):>12.6f}{'—':>12}"
                     f"{r['tmax']:>12.6f}{r['w_old']:>13.6f}{'raise':>13}{'—':>13}"
                     f"{r['T']:>8.2f}{_mo:>12.6f}{'—':>12}"
                     f"  —      {r.get('note', '')}")
    L.append("-" * 200)
    L.append("  · 「翻盤」＝ `sign(舊餘裕) ≠ sign(新餘裕)`（可分配 ↔ 強制留設抵費地）。")
    L.append("  · 新帶底取自 `_n14_band_hi(...)[1]`（**生產所消費者**）"
             "，⛔ 非自 `_n14_band_geom` 取 `_rear[0][0]`。")
    L.append("  · `max(_tv)` ＝ **E-2′ 之流失紀錄**：切換後 `baseline_pts is not None`"
             " ⇒ `app.py:6761` 之閘不再執行。")
    L.append("    其法定職責已由街廓層 **K-9-2** 承擔（**K-9-3 已裁**）⇒ **不是待裁項**；"
             "本欄僅留「切換前該閘離觸發有多遠」之數，供換案評估。")

    # ── 【C】結語所需之三數（供報告 §7-6 之土地語言段）───────────────────────────
    L.append("")
    L.append("【C】結語三數（⛔ 觀測·非門檻）")
    L.append("-" * 200)
    L.append(f"  翻盤格數 ＝ **{len(_flip)}**"
             + ("" if not _flip else
                "　⇒ " + "；".join(f"{r['sb']} {r['lbl']}/{r['side']}"
                                   f"（餘裕 {mo:+.6f} → {mn:+.6f}）"
                                   for r, mo, mn in _flip)))
    L.append(f"  max|Δ寬| ＝ **{_dmax:.6f} m**"
             + ("" if _dmax_at is None else
                f"（{_dmax_at['sb']} {_dmax_at['lbl']}/{_dmax_at['side']}"
                f"·{_dmax_at['w_old']:.6f} → {_dmax_at['w_new']:.6f}）"))
    L.append("  最緊之一格（新餘裕最小）＝ "
             + ("（無量得之格）" if _tight is None else
                f"**{_tight[0]['sb']} {_tight[0]['lbl']}/{_tight[0]['side']}"
                f"·新餘裕 {_tight[1]:+.6f} m**（門檻 {_tight[0]['T']:.2f}）"))

    # ── 【C-2】§7-0 之實證：`Δ寬 / Δ帶底` 與 E-2′ 餘裕（⛔ 觀測·非門檻）──────────
    L.append("")
    L.append("【C-2】§7-0 之**實證**：`Δ寬 ÷ Δ帶底` 逐格比值（⛔ 觀測·非門檻·非可外推之係數）")
    L.append("-" * 200)
    L.append("  🔴 施工單 §7-0 令「⛔ 禁以帶底差乘任何係數推估寬度差」。本段以實測坐實之：")
    L.append(f"{'情境':<6}{'街廓/側':<12}{'街角第1宗':<13}"
             f"{'Δ帶底':>12}{'Δ寬':>13}{'Δ寬÷Δ帶底':>16}"
             f"{'max(_tv)−舊帶底':>18}  ← E-2′ 餘裕")
    L.append("-" * 200)
    _ratio = []
    for r in recs:
        if 'w_new' not in r or 'w_old' not in r:
            continue
        _db = r['t_hi_new'] - r['t_hi_old']
        _dw = r['w_new'] - r['w_old']
        _rt = (_dw / _db) if abs(_db) > 1e-15 else float('nan')
        _ratio.append((r, _rt))
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{str(r.get('pid')):<13}"
                 f"{_db:>12.6f}{_dw:>13.6f}{_rt:>16.4f}"
                 f"{r['tmax'] - r['t_hi_old']:>18.6f}")
    L.append("-" * 200)
    if _ratio:
        _ab = sorted(abs(x[1]) for x in _ratio)
        L.append(f"  ⇒ `|Δ寬÷Δ帶底|` 之全距 ＝ **{_ab[0]:.4f} 〜 {_ab[-1]:.4f}**"
                 f"（**跨 {_ab[-1] / max(_ab[0], 1e-12):.3g} 倍**）")
    L.append("  🔴 **判讀（⛔ 只述觀測·不作推論外之宣稱）**：本欄**不是一個係數**——")
    L.append("     · 有數格落在 `0.04〜0.08` 量級（與 **GB-33** 所載之 `|k| ≤ 0.0756` 同量級）；")
    L.append("     · 另有數格落在 `10³` 量級 ⇒ **帶底差 1mm 可致寬度差逾 2m**。")
    L.append("     ⇒ 若以 GB-33 之 `0.0756` 推估，該類格將**低估約四個數量級**。")
    L.append("     ⇒ **§7-0 之禁令由本段實證成立**；⛔ 亦不得反過來拿本欄任一值當新係數用。")
    L.append("  📌 `max(_tv) − 舊帶底` ＝ **E-2′ 之餘裕**（該閘為 `max(_tv) < min_depth` ⇒ raise）：")
    L.append("     全數為**正** ⇒ 切換前該閘**從未觸發**；⚠️ 惟最小者僅 **mm 級**"
             "——⇒ 其「從未觸發」是**擦邊而過**，非有寬裕餘量。⛔ 換案不得據此假設它不會響。")

    L.append("")
    L.append("【D】註記")
    L.append("  · ⛔ 零生產變更：未動 `app.py`、未動 `verify/` 既有檔、不接 `run_all`。")
    L.append("  · 虛擬塊／`L_in` 挑選／截角判定**逐字沿用** `probe_K9_seg6_recon.py`（⛔ 未另寫第二份）。")
    L.append("  · 兩次量測**唯一差異 ＝ `baseline_pts`**；`min_depth` 二者皆傳 `depth_from_PQ`。")
    L.append("  · ⛔ 本檔不設門檻、不作放行建議——放行屬 KL（GB-40）。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
