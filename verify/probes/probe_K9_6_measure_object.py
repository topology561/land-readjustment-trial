# -*- coding: utf-8 -*-
r"""K-9-6-b **量測對象**之對照 — 「宗地多邊形之弦」 vs 「帶 ∩ 二側境界線（無限直線）」。

⛔ **只算不換·零生產變更·不接 `run_all`·不設任何門檻**（K-6-A2 段五(c) 前之偵察）。

## 為什麼要有本檔

段五(a)+(b) 之攤表（`docs/reports/W-G.6_K6-A2-段五ab_宗地帶_攤表.md` §〇）已指出：
新帶抵 BASELINE，而 `parcel_min_width_n14` 量的是**宗地多邊形之弦**
⇒ 34/118 列 loud raise、8 列判定翻轉。攤表同時載明**根因假說**：

> K-9-6-b 之量測多邊形為「帶 **∩ 二側境界線（無限直線）**」，
> ⇒ **不含**宗地之 BASELINE 側邊；`parcel_min_width_n14` 之弦則**含**之。

該假說**未被量化**。KL 若要裁「量測對象」，手上只有「現行量法 × 新帶」之數
（攤表 §〇 已明令 ⛔ 不得據以訂門檻）⇒ **等於要 KL 盲裁**。
本檔補上缺的那一欄：**正典量法之值**。

## 二側境界線之取法（**逐宗·依碼·非依名**）

正典 K-9-6-b 之「二側境界線依宗別」表（ALLOC／SIDE_LINE／BLOCK 邊界）係**依宗別指名**；
本檔**不依名取線**，改**依幾何取線**——取宗地環上**與前緣邊段相鄰之二邊所在之無限直線**。
理由：該二邊**就是**該宗之二側境界線之實體段（第 2 宗以後 ⇒ 二條 ALLOC；
末端塊 ⇒ 一 ALLOC 一 BLOCK 邊界），且此法**不需**先解決「本宗是不是末端塊」之分類題。

🔒 **另附獨立佐證欄** `∥alloc`：該二邊與 `cad['alloc_dir_by_block']` 之夾角正弦。
   第 2 宗以後 ⇒ **二側皆應 ∥ alloc**（≈0）；非 0 者即**非雙 ALLOC 之宗**（末端塊等）
   ——此欄**只作分類佐證**，⛔ **不驅動任何分支**。

## ⛔ 單一真相源

帶之上緣**只有一份**＝ `app._n14_band_hi`；本檔逐字呼叫之。
(s,t) 框與前緣邊偵測係**逐字重現** `parcel_min_width_n14`（含形心翻號 σ），
並以 `_t_lo` 對 helper **逐位元交叉核對**（不符即 loud raise）
——同 `parcel_min_width_n14` 內既有之守衛，⛔ 非「兩份實作各自為政」。

## 重跑

    python verify/probes/probe_K9_6_measure_object.py

輸出 `verify/out/probe_K9_6_measure_object.log`。rc 恆 0。
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
LOG = os.path.join(OUTDIR, "probe_K9_6_measure_object.log")

SIDES_IN = ("left", "right")


def _st_frame(cut_coords, d_hat, front_pt):
    """逐字重現 `parcel_min_width_n14` 之 (s,t) 框（含形心翻號 σ）。

    回 `(ring, sigma, d_hat_unit, n_hat, front_pt)`；ring 為閉環 list[(s,t)]。
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
    if _poly.is_empty or _poly.geom_type != 'Polygon':
        raise RuntimeError(f"宗地幾何非單一 Polygon（{_poly.geom_type}）")
    _ring = [(float(p[0]), float(p[1])) for p in list(_poly.exterior.coords)]
    _sg = 1.0
    if float(_poly.centroid.coords[0][1]) < 0:
        _sg = -1.0
        _ring = [(_s, -_t) for _s, _t in _ring]
    return _ring, _sg, _d, _n, _fp


def _front_run(ring, eps):
    """前緣邊之單一連續段 ⇒ 回 `(t_lo, A1, A2, e_prev, e_next)`。

    `A1`／`A2` ＝ 該段之二端頂點；`e_prev`／`e_next` ＝ 其前後之**相鄰邊**
    （＝二側境界線之實體段），各以 `((s0,t0),(s1,t1))` 表之。
    """
    tv = [t for _s, t in ring]
    n_e = len(ring) - 1
    fe = [i for i in range(n_e)
          if abs(tv[i]) <= eps and abs(tv[i + 1]) <= eps]
    if not fe:
        raise RuntimeError("無前緣邊（單點接觸）")
    fs = set(fe)
    starts = [i for i in fe if ((i - 1) % n_e) not in fs]
    if len(starts) != 1:
        raise RuntimeError(f"前緣邊分裂為 {len(starts)} 段")
    i0 = starts[0]
    i1 = i0
    while ((i1 + 1) % n_e) in fs:
        i1 = (i1 + 1) % n_e
    t_lo = max(0.0, max(max(tv[i], tv[i + 1]) for i in fe))
    A1 = ring[i0]
    A2 = ring[(i1 + 1) % n_e]
    p = (i0 - 1) % n_e
    q = (i1 + 1) % n_e
    e_prev = (ring[p], ring[p + 1])
    e_next = (ring[q], ring[q + 1])
    return t_lo, A1, A2, e_prev, e_next


def _s_at(anchor, direction, t):
    """側境界線（過 `anchor`、方向 `direction`·**無限直線**）於深度 `t` 之 `s`。"""
    ds, dt = direction
    if abs(dt) < 1e-12:
        raise RuntimeError("側境界線平行於前緣線 ⇒ 於 t 無單一交點")
    return anchor[0] + (t - anchor[1]) * (ds / dt)


def _canon_width(A1, u1, A2, u2, t_lo, t_hi):
    """正典量法：帶 ∩ 二側**無限直線**之最小寬度。

    `w(t) = |s2(t) − s1(t)|` 於 `t` **線性** ⇒ 極小值必在端點，
    除非其於帶內變號（二側界於帶內相交）⇒ 此時 min ＝ 0，另旗標之。
    """
    f_lo = _s_at(A2, u2, t_lo) - _s_at(A1, u1, t_lo)
    f_hi = _s_at(A2, u2, t_hi) - _s_at(A1, u1, t_hi)
    crossed = (f_lo * f_hi < 0.0)
    if crossed:
        return 0.0, True, abs(f_lo), abs(f_hi)
    return min(abs(f_lo), abs(f_hi)), False, abs(f_lo), abs(f_hi)


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 190)
    L.append("【K-9-6-b 量測對象】「宗地多邊形之弦」（現行） vs 「帶 ∩ 二側境界線·無限直線」（正典）"
             " — ⛔ 只算不換·生產零變更·不設門檻")
    L.append("正典量法之二側境界線 ＝ 宗地環上**與前緣邊段相鄰之二邊**所在之無限直線"
             "（⛔ 不依宗別取名·另附 `∥alloc` 佐證欄·該欄不驅動分支）")
    L.append("=" * 190)

    ns, fake_st = harvest()
    for _s in ("parcel_min_width_n14", "_n14_band_hi", "get_min_lot_size",
               "_baseline_pts_from_manual", "_EPS_TOUCH_FRONT"):
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
    bl_by = cad.get("baselines", {}) or {}
    ad_by = cad.get("alloc_dir_by_block", {}) or {}

    rows = []
    excluded = {}
    for setback in (0.0, 3.5):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, winners, forced, setback)
        for r in sg["g_rows"]:
            _side = str(r.get("推進側別") or "（空）")
            if _side not in SIDES_IN:
                excluded.setdefault((f"{setback:g}m", _side), 0)
                excluded[(f"{setback:g}m", _side)] += 1
                continue
            rows.append((setback, r))

    L.append("")
    L.append("【A】母體：`推進側別 ∈ {'left','right'}`（同 `probe_K9_6_parcel_band.py`）")
    L.append("-" * 190)
    L.append(f"  納入母體：**{len(rows)}** 列（兩情境合計）")
    for (tag, sd), n in sorted(excluded.items()):
        L.append(f"    剔除 {tag:<6} 推進側別＝`{sd}`：{n} 列")

    L.append("")
    L.append("【B】逐宗：四欄寬度（**全精度**）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓':<5}{'gid':<13}{'側':<6}"
             f"{'t_lo':>11}{'t_hi_舊':>9}{'t_hi_新':>11}"
             f"{'現行×舊帶':>13}{'現行×新帶':>13}"
             f"{'正典×舊帶':>13}{'正典×新帶':>13}{'Δ正典':>12}"
             f"{'∥alloc':>11}  類別")
    L.append("-" * 190)

    _corner = 0
    _skip = []
    _dat = []          # (tag, lbl, gid, side, w_old_cur, w_new_cur, w_old_can, w_new_can, sinmax)
    for setback, r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
        tag = f"{setback:g}m"
        fl = fl_by.get(lbl) or {}
        cc = r.get("cut_coords") or []
        if str(r.get("街角地", "")).strip() == "是":
            _corner += 1
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                     f"  — N/A·豁免中（K-4 面積門檻·街角宗不進量測·GB-39／段六）")
            continue
        if not (fl.get("p1") and fl.get("p2")) or len(cc) < 3:
            _skip.append((tag, lbl, gid, "缺 FRONT_LINE 或 cut_coords < 3"))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 缺件（見【D】）")
            continue
        _mw = ns["get_min_lot_size"](
            cb_by[lbl]["category"],
            float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        _md = float(_mw.get("min_depth", 0.0) or 0.0)
        p1, p2 = fl["p1"], fl["p2"]
        _dx, _dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        _Lf = math.hypot(_dx, _dy)
        _dh = (_dx / _Lf, _dy / _Lf)
        _bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), cb_by[lbl].get("vertices"))
        try:
            _t_lo_h, _t_hi_new, _D, _g, _bdn = ns["_n14_band_hi"](
                cc, _dh, p1, _bp, _label=f"{lbl}/{gid}")
        except RuntimeError as e:
            _skip.append((tag, lbl, gid, "helper raise：" + str(e).splitlines()[0][:120]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 helper raise（見【D】）")
            continue

        # ── 正典量法 ──────────────────────────────────────────────────────────
        try:
            ring, sg, dhat, nhat, fp = _st_frame(cc, _dh, p1)
            t_lo, A1, A2, e_prev, e_next = _front_run(ring, _EPS)
        except RuntimeError as e:
            _skip.append((tag, lbl, gid, "框／前緣邊：" + str(e)[:120]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 框／前緣邊（見【D】）")
            continue
        # 🔒 與 helper 之 `_t_lo` 逐位元交叉核對（⛔ 不符即停·不得靜默採其一）
        if abs(t_lo - _t_lo_h) > 1e-12:
            raise RuntimeError(
                f"🔴 {lbl}/{gid}：`_t_lo` 二份實作不符"
                f"（本檔 {t_lo:.15g} vs `_n14_band_hi` {_t_lo_h:.15g}）⇒ 前緣邊偵測已漂移，停")
        u1 = (e_prev[1][0] - e_prev[0][0], e_prev[1][1] - e_prev[0][1])
        u2 = (e_next[1][0] - e_next[0][0], e_next[1][1] - e_next[0][1])
        # ∥alloc 佐證（⛔ 不驅動分支）：alloc 方向於 (s,t) 框 ＝ (a·d̂, σ·(a·n̂))
        _sin = float('nan')
        _ad = ad_by.get(lbl)
        if _ad:
            _ax, _ay = float(_ad[0]), float(_ad[1])
            _an = math.hypot(_ax, _ay)
            if _an > 1e-12:
                _a = ((_ax * dhat[0] + _ay * dhat[1]) / _an,
                      sg * (_ax * nhat[0] + _ay * nhat[1]) / _an)
                _sin = 0.0
                for _u in (u1, u2):
                    _un = math.hypot(_u[0], _u[1])
                    if _un > 1e-12:
                        _sin = max(_sin, abs(_u[0] * _a[1] - _u[1] * _a[0]) / _un)
        try:
            _w_can_old, _x1, _lo1, _hi1 = _canon_width(A1, u1, A2, u2, t_lo, _md)
            _w_can_new, _x2, _lo2, _hi2 = _canon_width(A1, u1, A2, u2, t_lo, _t_hi_new)
        except RuntimeError as e:
            _skip.append((tag, lbl, gid, "正典量法：" + str(e)[:120]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 正典量法（見【D】）")
            continue

        # ── 現行量法（宗地弦）·舊帶／新帶 ────────────────────────────────────
        def _cur(_bp_arg):
            try:
                return float(ns["parcel_min_width_n14"](
                    cc, _dh, p1, _md, _label=f"{lbl}/{gid}", baseline_pts=_bp_arg)), None
            except RuntimeError as e:
                return None, str(e).splitlines()[0]
        _w_cur_old, _e_old = _cur(None)
        _w_cur_new, _e_new = _cur(_bp)

        _cls = "雙側∥alloc" if (_sin == _sin and _sin < 1e-9) else "非雙側∥alloc"
        if _x1 or _x2:
            _cls += "·🔴側界於帶內相交"
        _dat.append((tag, lbl, gid, side, _w_cur_old, _w_cur_new,
                     _w_can_old, _w_can_new, _sin, _cls))
        _f = lambda v: (f"{v:>13.6f}" if v is not None else f"{'raise':>13}")
        L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                 f"{t_lo:>11.6f}{_md:>9.2f}{_t_hi_new:>11.6f}"
                 f"{_f(_w_cur_old)}{_f(_w_cur_new)}"
                 f"{_w_can_old:>13.6f}{_w_can_new:>13.6f}"
                 f"{_w_can_new - _w_can_old:>12.2e}"
                 f"{_sin:>11.3e}  {_cls}")
    L.append("-" * 190)
    L.append(f"  街角宗 **{_corner}** 列記 `N/A·豁免中`（⛔ 未臆造數字）")

    # ── 【C】三個關鍵彙總 ─────────────────────────────────────────────────────
    L.append("")
    L.append("【C】彙總（⛔ 皆為觀測·非門檻）")
    L.append("-" * 190)
    _n = len(_dat)
    _dmax = max((abs(d[7] - d[6]) for d in _dat), default=float('nan'))
    _dmax_row = max(_dat, key=lambda d: abs(d[7] - d[6])) if _dat else None
    _cur_raise = [d for d in _dat if d[5] is None]
    _cur_ok = [d for d in _dat if d[5] is not None]
    _gapmax = max((abs(d[6] - d[4]) for d in _cur_ok), default=float('nan'))
    _gapmax_row = max(_cur_ok, key=lambda d: abs(d[6] - d[4])) if _cur_ok else None
    _nonpar = [d for d in _dat if not (d[8] == d[8] and d[8] < 1e-9)]
    L.append(f"  C-1 量得之宗：{_n} 列（現行量法 × 新帶 raise 者 {len(_cur_raise)} 列，"
             f"**正典量法於同一批全部量得**）")
    L.append(f"  C-2 **正典量法之帶深敏感度** max|正典×新帶 − 正典×舊帶| ＝ {_dmax:.6e} m"
             + (f"（{_dmax_row[0]} {_dmax_row[1]}/{_dmax_row[2]}）" if _dmax_row else ""))
    L.append(f"  C-3 **現行 vs 正典（同為舊帶）** max|正典×舊帶 − 現行×舊帶| ＝ {_gapmax:.6e} m"
             + (f"（{_gapmax_row[0]} {_gapmax_row[1]}/{_gapmax_row[2]}）" if _gapmax_row else ""))
    L.append(f"  C-4 `∥alloc` 非零之宗（＝非雙側 ALLOC·末端塊等）：{len(_nonpar)} 列")
    for d in _nonpar:
        L.append(f"        {d[0]:<6}{d[1]}/{d[2]}（{d[3]}）：sin ＝ {d[8]:.6e}｜"
                 f"正典 舊帶 {d[6]:.6f} → 新帶 {d[7]:.6f}（Δ {d[7] - d[6]:+.6e}）")

    L.append("")
    L.append("【D】跳過／raise 之列")
    L.append("-" * 190)
    for tag, lbl, gid, why in _skip:
        L.append(f"  {tag:<6}{lbl}/{gid}：{why}")
    if not _skip:
        L.append("  （無）")

    L.append("")
    L.append("【E】註記")
    L.append("  · ⛔ **本檔零生產變更**：未動 `app.py`、未動 `verify/` 既有檔、不接 `run_all`。")
    L.append("  · 帶之上緣**單一真相源** ＝ `app._n14_band_hi`（本檔逐字呼叫）；"
             "`_t_lo` 與之逐位元交叉核對。")
    L.append("  · ⛔ **本檔不設任何門檻、不作放行建議**——量測對象之裁定屬 KL。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
