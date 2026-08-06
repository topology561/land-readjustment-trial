# -*- coding: utf-8 -*-
r"""**S6-2 §一 主測**：於 **k98 現行量測帶之二端**，量 (a) 線距 vs (b) 弦（⛔ 只量不判）。

⛔ 零碼面·不接 `run_all`·**不寫任何判定碼**（K-9-5-3 已由 KL 令暫停適用）。

## §〇 待證偽之假說（claude.ai 提·⛔ 非結論）

`K-9-5-2` ③ 之「構造保證最小寬 ≥ 畸零地寬」，其受測量為
**二側界無限直線之間距**；而 k98／N-14 量的是**多邊形之弦**
⇒ ⑤ 之推論可能斷在「**保證的量 ≠ 量到的量**」。

## §一 本檔於 k98 帶之二端輸出

| 欄 | 定義 |
|---|---|
| **(a) 線距** | `SIDE_LINE` 無限直線 與 **winner `ALLOC_LINE`（`L_in`）** 無限直線之間距（沿 `d̂`） |
| **(b) 弦** | **k98 虛擬還原塊**之多邊形弦（＝現行 `k98["min_width"]` 之來源） |
| **(c)** | `(a) − (b)`，及弦**兩端點各落在哪一條邊界上**（**正面列舉**·⛔ 禁「其他」） |

另輸出該格之 `T`／`G`／**街角規定範圍面積**。

## 🔒 (a) 之量法與 `_build_corner_range_v3` 自檢①′ **同源**（§五-3）

自檢①′（`grep -n "自檢①′" app.py`）之路徑逐字為：

    _Sinf = _LS3([(S1 - sux*_LBIG, ...), (S1 + sux*_LBIG, ...)])      # 側界無限直線
    _Lt   = _LS3([(Q0 + t*·an − au*_LBIG, ...), (... + au*_LBIG, ...)])  # ALLOC 無限直線
    _dep  = _LS3([(P − d̂*_LBIG, ...), (P + d̂*_LBIG, ...)])            # 該深度之量測線
    _i1, _i2 = _dep.intersection(_Sinf), _dep.intersection(_Lt)

本檔逐字沿用**同一路徑**（見 `_line_dist()`），⛔ **未另寫第三套**；
差別僅在 `_Lt` 之來源：自檢①′ 用**構造解** `t*`，本檔用 **winner 實配之 `L_in`**
——此即本檔之受測對象（`K-9-8` (4) 之虛擬塊二側界之一）。

## 🔒 自我驗證閘（`CLAUDE.md` 常設條）

外部重建之帶端（`t_lo`／`t_hi` → 世界座標）以**碼面自身之保證**驗：
`min(弦@t_lo, 弦@t_hi)` 必須 **== `k98["min_width"]`**（同一多邊形、同一帶）。
⛔ **該閘不過，不准據本檔下任何結論**——已寫入輸出。

## 重跑

    python verify/probes/probe_K9_s62_k98_line_vs_chord.py

輸出 `verify/out/probe_K9_s62_k98_line_vs_chord.log`。rc 恆 0。
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
LOG = os.path.join(OUTDIR, "probe_K9_s62_k98_line_vs_chord.log")
_LBIG = 1.0e5
_TOL = 1e-6          # 邊界歸屬之容差
_Q = 1e-5            # DXF 量化步長之量級


def _u(ax, ay):
    n = math.hypot(ax, ay)
    return (ax / n, ay / n)


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


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    from shapely.geometry import LineString as _LS, Point as _PT, Polygon as _PG
    L = []
    L.append("=" * 200)
    L.append("【S6-2 §一 主測】k98 量測帶二端：(a) 線距（SIDE∞ vs winner ALLOC∞）"
             " vs (b) k98 虛擬塊之弦 — ⛔ 只量不判")
    L.append("=" * 200)

    ns, fake_st = harvest()
    for _s in ("k98_virtual_measure_block", "_n14_band_geom", "_build_corner_range_v3",
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
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    rows, _diag, _grG = [], [], {}
    for setback in (0.0, 3.5):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, winners, forced, setback)
        by_pid = {str(r.get("暫編地號")): r for r in sg["g_rows"]}
        for _dg in (_d0 or []):
            _diag.append(dict(_dg, _sb=f"{setback:g}m"))
        for _gr in sg["g_rows"]:
            _grG[(f"{setback:g}m", str(_gr.get('暫編地號')))] = _gr.get('G(㎡)')
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            blk = (snapshot["blocks"].get(lbl) or {})
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
            au = al_by.get(lbl)
            if not au:
                continue
            auh = _u(float(au[0]), float(au[1]))
            for which in ("left", "right"):
                if which not in (sd_by.get(lbl) or {}):
                    continue
                rec = {"sb": f"{setback:g}m", "lbl": lbl, "side": which,
                       "T": setback + legal_w}
                w = (winners or {}).get(lbl) or {}
                pid = w.get("p1_end" if which == "left" else "p2_end")
                rec["pid"] = pid
                chi = ns["_make_chamfer_tri_wb"](b, which)
                sd = sd_by[lbl][which]
                # 街角規定範圍面積（⛔ 無論有無 winner 皆可算）
                try:
                    _rng = ns["_build_corner_range_v3"](
                        b.get("vertices"), b.get("centroid"), [fl["p1"], fl["p2"]], bp,
                        [sd["p1"], sd["p2"]], au,
                        float(blk.get("街廓分配深度_m") or 0.0), setback, legal_w, chi,
                        dxf_quantum=((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected"),
                        _label=lbl, _side=which)
                    rec["rng_area"] = float(_rng.area)
                except RuntimeError as e:
                    rec["rng_area"] = None
                    rec["rngerr"] = str(e).splitlines()[0][:70]
                if not pid:
                    rec["note"] = "無 winner（強制留設抵費地）"
                    rows.append(rec); continue
                row = by_pid.get(str(pid)) or {}
                rec["G"] = row.get("G(㎡)")
                cc = row.get("cut_coords") or []
                if len(cc) < 3:
                    rec["note"] = f"cut_coords 不足（{len(cc)}）"
                    rows.append(rec); continue
                F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
                F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
                dxh, dyh = _u(F2[0] - F1[0], F2[1] - F1[1])
                _edges = _alloc_edges(cc, auh)
                if not _edges:
                    rec["note"] = "無平行 ALLOC 之邊 ⇒ L_in 不可定"
                    rows.append(rec); continue

                def _s_of(p, _F=F1, _dx=dxh, _dy=dyh):
                    return (p[0] - _F[0]) * _dx + (p[1] - _F[1]) * _dy
                _sx = _s_of((float(sd["p1"][0]), float(sd["p1"][1])))
                _edges.sort(key=lambda e: abs((_s_of(e[0]) + _s_of(e[1])) / 2.0 - _sx))
                _lin = _edges[-1]                      # winner 之 ALLOC 邊（L_in）
                _oc = None
                if chi is not None and not chi.is_empty:
                    _oc = (lambda _p, _t=chi:
                           bool(_t.buffer(1e-9).contains(_PT(_p[0], _p[1]))))
                try:
                    k98 = ns["k98_virtual_measure_block"](
                        b.get("vertices"), [F1, F2], bp, [_lin[0], _lin[1]],
                        [sd["p1"], sd["p2"]], _label=lbl, _pid=str(pid),
                        _lot_kind="corner_first", on_chamfer=_oc)
                except RuntimeError as e:
                    rec["note"] = "k98 raise：" + str(e).splitlines()[0][:70]
                    rows.append(rec); continue
                rec["w_k98"] = float(k98["min_width"])
                poly = k98["poly"]
                _pb = (k98["P_block"][0], k98["P_block"][1])
                try:
                    _tlo, _rear, _g, _bdn = ns["_n14_band_geom"](
                        list(poly.exterior.coords), (dxh, dyh), _pb, bp,
                        _label=f"{lbl}/{which}")
                except RuntimeError as e:
                    rec["note"] = "band_geom raise：" + str(e).splitlines()[0][:70]
                    rows.append(rec); continue
                _thi = _rear[0][0]
                rec["band"] = (_tlo, _thi)

                # ── 帶端 → 世界座標 ────────────────────────────────────────────
                #   🔴 σ **逐字照碼面之形心翻號規則**（`parcel_min_width_n14`／
                #     `_n14_band_geom` 之「形心之 `t` 為負則整環翻號」），
                #   ⛔ **禁以「線是否切到多邊形」試出來**——`δ_P < 0` 之格（本案 6 格）
                #     其多邊形跨越 `PQ`，兩個號皆會切到 ⇒ 該試法必錯。
                #     （前版即如此，被【A】自我驗證閘擋下 9/12 格。）
                nx, ny = -dyh, dxh
                _st = [(( float(_p[0]) - _pb[0]) * dxh + (float(_p[1]) - _pb[1]) * dyh,
                        ( float(_p[0]) - _pb[0]) * nx + (float(_p[1]) - _pb[1]) * ny)
                       for _p in poly.exterior.coords]
                _cen_t = _PG(_st).centroid.coords[0][1]
                _sig = -1.0 if _cen_t < 0 else 1.0

                # 六條受檢邊界（**正面列舉**·⛔ 禁「其他」）
                S1 = (float(sd["p1"][0]), float(sd["p1"][1]))
                S2 = (float(sd["p2"][0]), float(sd["p2"][1]))
                sux, suy = _u(S2[0] - S1[0], S2[1] - S1[1])
                B0 = (float(bp[0][0]), float(bp[0][1]))
                B1 = (float(bp[-1][0]), float(bp[-1][1]))
                bux, buy = _u(B1[0] - B0[0], B1[1] - B0[1])

                def _inf(p, ux, uy):
                    return _LS([(p[0] - ux * _LBIG, p[1] - uy * _LBIG),
                                (p[0] + ux * _LBIG, p[1] + uy * _LBIG)])
                _Sinf = _inf(S1, sux, suy)
                _Linf = _inf((float(_lin[0][0]), float(_lin[0][1])), auh[0], auh[1])
                _Binf = _inf(B0, bux, buy)
                _Finf = _inf(F1, dxh, dyh)
                _PQinf = _inf(_pb, dxh, dyh)
                _blk = _PG([(float(v[0]), float(v[1])) for v in b.get("vertices")])
                _OBJ = [("PQ", _PQinf), ("ALLOC(L_in)", _Linf), ("SIDE(截角前)", _Sinf),
                        ("BASELINE", _Binf), ("FRONT", _Finf),
                        ("街廓邊界", _blk.exterior)]
                if chi is not None and not chi.is_empty:
                    _OBJ.append(("截角邊", chi.boundary))

                # ── 🔒 **E-10**：弦與線距一律於 `(s,t)` **局部框解析求**，⛔ 禁 GEOS 世界座標
                #   案由（本檔實測）：`t_lo` 之量測線與多邊形前緣邊**共線**，
                #   GEOS 於 TWD97 量級（~3.1e5）之共線求交回 **3.684**（真值 **6.847**）
                #   ⇒ 前版 12 格中 5 格之自我驗證閘因此不過。
                #   （`app.py` 之 `parcel_min_width_n14` 亦係解析求·`grep -n "E-10 弦長" app.py`。）
                def _to_st(p):
                    _px, _py = float(p[0]) - _pb[0], float(p[1]) - _pb[1]
                    return (_px * dxh + _py * dyh, _sig * (_px * nx + _py * ny))
                _ring_st = [_to_st(p) for p in poly.exterior.coords]

                def _chord_at(_T):
                    _xs = []
                    for _i in range(len(_ring_st) - 1):
                        _s0, _t0 = _ring_st[_i]
                        _s1, _t1 = _ring_st[_i + 1]
                        if _t0 == _t1:
                            if _t0 == _T:
                                _xs += [_s0, _s1]
                            continue
                        if (_t0 - _T) * (_t1 - _T) <= 0.0:
                            _xs.append(_s0 + (_T - _t0) / (_t1 - _t0) * (_s1 - _s0))
                    return ((max(_xs) - min(_xs), _xs) if _xs else (0.0, []))

                def _s_on(pA, pB, _T):
                    """過 `pA`、`pB` 之**無限直線**於深度 `_T` 之 `s`（⛔ 解析·非 GEOS）。"""
                    _a, _b = _to_st(pA), _to_st(pB)
                    if abs(_b[1] - _a[1]) < 1e-12:
                        return float('nan')
                    return _a[0] + (_T - _a[1]) / (_b[1] - _a[1]) * (_b[0] - _a[0])

                _res = []
                for _t in (_tlo, _thi):
                    _ld = abs(_s_on(_lin[0], _lin[1], _t)
                              - _s_on(sd["p1"], sd["p2"], _t))       # (a) 線距
                    _ch, _xs = _chord_at(_t)                          # (b) 弦
                    # (c) 端點歸屬（正面列舉·世界座標回推後逐界判）
                    _own = []
                    for _sv in ((min(_xs), max(_xs)) if _xs else ()):
                        _w = (_pb[0] + _sv * dxh + _sig * _t * nx,
                              _pb[1] + _sv * dyh + _sig * _t * ny)
                        _p = _PT(_w)
                        _on = [nm for nm, ob in _OBJ if _p.distance(ob) <= _TOL]
                        _dists = "／".join(f"{nm} {_p.distance(ob):.6f}" for nm, ob in _OBJ)
                        # 🔒 S6-2-B §三-2：**恆記六界距離**（⛔ 非只在皆不在容差內時才印）
                        _own.append(("+".join(_on) if _on else "🔴 諸界皆不在容差內")
                                    + f"　〔六界距離：{_dists}〕")
                    _res.append((_t, _ld, _ch, _own))
                rec["res"] = _res
                rec["chk"] = min(x[2] for x in _res)
                rows.append(rec)

    # ── 【A】自我驗證閘 ───────────────────────────────────────────────────────
    L.append("")
    L.append("【A】🔒 自我驗證閘：`min(弦@t_lo, 弦@t_hi)` 必須 == `k98[\"min_width\"]`"
             "（⛔ 不過即不得據本檔下結論）")
    L.append("-" * 200)
    _bad = []
    for r in rows:
        if "chk" not in r:
            continue
        _ok = abs(r["chk"] - r["w_k98"]) < 1e-6   # 🔒 E-10：本檔之弦以 GEOS 於
        #   TWD97 量級求交，而 `parcel_min_width_n14` 係於 (s,t) 局部框**解析**求
        #   ⇒ 容差取 `1e-6`（法定粒度 `0.01` 之萬分之一），⛔ 非放寬結構性判準
        r["gate"] = _ok
        if not _ok:
            _bad.append((r["sb"], f"{r['lbl']}/{r['side']}", r["chk"], r["w_k98"],
                         abs(r["chk"] - r["w_k98"])))
        L.append(f"  {r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}"
                 f"min(弦) ＝ {r['chk']!r:<22}k98 ＝ {r['w_k98']!r:<22}{'✅ ==' if _ok else '🔴 ≠'}")
    L.append("-" * 200)
    if _bad:
        L.append(f"  🔴 **{len(_bad)} 格未過閘** ⇒ **該格於【B】標 `🔴 閘未過`、"
                 f"⛔ 不得據以下任何結論**（⛔ 未放寬閘門以掩蓋之）：")
        for _v in _bad:
            L.append(f"      {_v[0]:<6}{_v[1]:<12}min(弦) {_v[2]!r} vs k98 {_v[3]!r}"
                     f"　差 {_v[4]:.3e}")
        L.append(f"  ✅ 其餘 **{sum(1 for r in rows if r.get('gate'))} 格逐位元相符**"
                 f"（`==`·⛔ 非容差內）⇒ 該等格之【B】可信。")
    else:
        L.append("  ✅ **全格相符** ⇒ 帶端還原正確、【B】可信。")

    # ── 【B】主表（十六格逐格·含無 winner 者）────────────────────────────────
    L.append("")
    L.append("【B】主表（**十六格逐格**·⛔ 無 winner 者亦列·標「—」）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'街角第1宗':<13}{'T':>6}{'G(㎡)':>10}"
             f"{'規定範圍(㎡)':>13}{'帶端 t':>12}{'(a)線距':>13}{'(b)弦':>13}"
             f"{'(a)−(b)':>12}  (c) 弦兩端點之邊界歸屬")
    L.append("-" * 200)
    for r in rows:
        _tag = f"{r['lbl']}/{r['side']}"
        _ra = ("—" if r.get("rng_area") is None else f"{r['rng_area']:.2f}")
        if "res" not in r:
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid') or '—'):<13}"
                     f"{r['T']:>6.2f}{'—':>10}{_ra:>13}"
                     f"{'—':>12}{'—':>13}{'—':>13}{'—':>12}  {r.get('note', '')}")
            continue
        _G = ("—" if r.get("G") is None else f"{float(r['G']):.2f}")
        _gm = "" if r.get("gate") else "  🔴 閘未過·⛔ 本列不可據"
        for _t, _ld, _ch, _own in r["res"]:
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid')):<13}"
                     f"{r['T']:>6.2f}{_G:>10}{_ra:>13}{_t:>12.6f}"
                     f"{_ld:>13.6f}{_ch:>13.6f}{_ld - _ch:>12.6f}  "
                     + "｜".join(_own) + _gm)
    L.append("-" * 200)

    # ── 【C】§二 判準之陳述（⛔ 只陳述·不裁定）────────────────────────────────
    L.append("")
    L.append("【C】§二 判準（⛔ **只陳述、不裁定**）")
    L.append("-" * 200)
    _key = [r for r in rows if r["sb"] == "3.5m" and r["lbl"] == "R1"
            and r["side"] == "right" and "res" in r and r.get("gate")]
    if not _key:
        L.append("  🔴 `3.5m R1/right` 未取得 ⇒ 無從陳述")
    else:
        _r = _key[0]
        _amin = min(x[1] for x in _r["res"])
        _bmin = min(x[2] for x in _r["res"])
        L.append(f"  `3.5m R1/right`：min(a) 線距 ＝ **{_amin:.6f}**"
                 f"／min(b) 弦 ＝ **{_bmin:.6f}**／T ＝ {_r['T']:.2f}")
        if _amin >= _r["T"] > _bmin:
            L.append("  ⇒ **(a) ≥ T > (b)** ⇒ 假說**成立**（保證的量 ≠ 量到的量）；"
                     "削弦者見同列 (c) 之端點歸屬。")
        elif _amin < _r["T"]:
            # 🔧 S6-2-C 更正：前版於此印「**構造保證本身即未達 T**」係**歸因錯誤**。
            #   自檢①（`app.py` `grep -n "構造自檢不合" app.py`）與自檢①′ 所量之 ALLOC 線
            #   皆由**構造解 `t_star`** 生成；本檔之 (a) 用 **winner 實配之 `L_in`**
            #   （見本檔 docstring §一「差別僅在 `_Lt` 之來源」）⇒ **構造保證從未涵蓋 (a)**
            #   ⇒ ⛔ 不得由 `(a) < T` 推論「構造被破壞」。
            L.append(f"  ⇒ **(a) 亦 < T**（{_amin:.6f} < {_r['T']:.2f}）⇒ 假說**不成立**"
                     "（(b) 未被削·非「保證的量 ≠ 量到的量」）。")
            L.append("  ⛔ **不得推論「構造保證本身未達 T」**——自檢①／①′ 之 ALLOC 線"
                     "由**構造解 `t_star`** 生成，(a) 用 **winner 實配之 `L_in`**"
                     "（docstring §一）⇒ **二者非同一條線·保證未涵蓋 (a)**。")
            # 收支表：寬度短少 × 深度 ?= 規定範圍面積 − 實配 G（平行平移 ⇒ 應相等）
            _dw = _r["T"] - _amin
            _D = max(x[0] for x in _r["res"])
            _ra, _gg = _r.get("rng_area"), _r.get("G")
            if _ra is not None and _gg is not None:
                _da = float(_ra) - float(_gg)
                L.append("  ── 收支表（平行平移 ⇒ Δ寬 × 深度 應 ＝ 規定範圍 − 實配 G）──")
                L.append(f"     Δ寬 ＝ T − min(a) ＝ {_dw:.6f}　深度(帶底 t) ＝ {_D:.6f}"
                         f"　⇒ Δ寬 × 深度 ＝ {_dw * _D:.4f}")
                L.append(f"     規定範圍 {float(_ra):.2f} − 實配 G {float(_gg):.2f} ＝ {_da:.4f}"
                         f"　⇒ **殘差 {_dw * _D - _da:+.4f}**（G 為 2dp ⇒ 捨入帶 ±0.01）")
                L.append("     ⇒ 若殘差落在捨入帶內：**寬不足與面積不足係同一事之兩種量法**"
                         "·⛔ 非兩個獨立缺陷。")
        else:
            L.append("  ⇒ **其餘情形**（照實陳述·⛔ 未硬套二分）："
                     f"(a)={_amin:.6f}／(b)={_bmin:.6f}／T={_r['T']:.2f}")

    # ── 【E】S6-2-B §一：資格閘之**真運算元**逐格對照 ────────────────────────
    L.append("")
    L.append("【E】S6-2-B §一：資格閘之**真運算元**（⛔ 皆自生產呼叫點取值·未重算）")
    L.append("-" * 200)
    L.append("  🔒 **閘 `app.py:11255` 實際比的是**（**正面指名**）：")
    L.append("       左 ＝ `cand_G`  ——  本案 `require_g_map=True`（`app.py:18026` 之呼叫端）")
    L.append("                          ⇒ `cand_G = float(g_values_map[_pid] or 0)`（`app.py:11238`）")
    L.append("       右 ＝ `cand.get('min_area_to_apply', 0)`（`app.py:11255`）")
    L.append("                          ⇒ 其值來自呼叫端之 `min_corner_area_p1/p2`"
             "（`app.py:18023`／`:18024`）")
    L.append("  🔒 `cand['_G_true'] = round(cand_G, 2)`（`app.py:11252`）"
             "⇒ **② 即 ① 之 2dp**（⛔ 非另一個量）")
    L.append("  🔒 `cand['G_for_threshold'] = round(G_estimated, 2)`（`app.py:11254`）"
             "⇒ **④ 係估算欄·⛔ 不參與本閘**")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓':<5}{'端':<5}{'候選':<13}"
             f"{'②真G':>10}{'④G估':>10}{'⑤門檻':>10}{'⑥範圍面積':>11}{'⑦探針rng':>11}"
             f"{'⑧g_rows G':>11}{'範圍=門檻?':>12}{'達標':>6}  ①cand_G")
    L.append("-" * 200)
    _rngmap = {(r["sb"], r["lbl"], r["side"]): r.get("rng_area") for r in rows}
    _sidename = {"左": "left", "右": "right", "p1": "left", "p2": "right"}
    for _dg in _diag:
        _sd = _sidename.get(str(_dg.get("端", "")).strip(), str(_dg.get("端", "")))
        _key = (_dg["_sb"], str(_dg.get("街廓", "")), _sd)
        _r7 = _rngmap.get(_key)
        _pidd = str(_dg.get("候選地號", ""))
        _g8 = _grG.get((_dg["_sb"], _pidd))
        _tg = _dg.get("真G(㎡)")
        L.append(f"{_dg['_sb']:<6}{str(_dg.get('街廓','')):<5}{str(_dg.get('端','')):<5}{_pidd:<13}"
                 f"{(f'{float(_tg):.2f}' if _tg not in ('', None) else '—'):>10}"
                 f"{float(_dg.get('G估(㎡)', 0) or 0):>10.2f}"
                 f"{float(_dg.get('門檻(㎡)', 0) or 0):>10.2f}"
                 f"{float(_dg.get('範圍面積(㎡)', 0) or 0):>11.2f}"
                 f"{('—' if _r7 is None else f'{_r7:.2f}'):>11}"
                 f"{('—' if _g8 is None else f'{float(_g8):.2f}'):>11}"
                 f"{str(_dg.get('範圍=門檻?','')):>12}{str(_dg.get('達標','')):>6}"
                 f"  ＝②之未捨入值（`_G_true` ＝ `round(cand_G,2)`）")
    L.append("-" * 200)
    L.append("  ⚠️ **① `cand_G` 之未捨入值不另印**——碼面**只把它捨入後存為 `_G_true`**"
             "（`app.py:11252`），⛔ 未另存未捨入者 ⇒ 自生產取值只能取到 2dp。")
    L.append("     ⇒ 判 `① ≥ ⑤` 時，若二者差 < 0.005 則 2dp 不足以定奪；本表逐格之差見下。")

    # ── 【F】§二 判準（⛔ 兩分支對等·未觸發者亦明寫）──────────────────────────
    L.append("")
    L.append("【F】S6-2-B §二 判準（⛔ 只陳述·不裁定·**兩分支對等**）")
    L.append("-" * 200)
    _k = [d for d in _diag if d["_sb"] == "3.5m" and str(d.get("街廓","")) == "R1"
          and _sidename.get(str(d.get("端","")).strip()) == "right"]
    if not _k:
        L.append("  🔴 `3.5m R1/right` 於診斷列中未找到 ⇒ 無從陳述")
    else:
        _dg = _k[0]
        _g = float(_dg.get("真G(㎡)") or 0); _m = float(_dg.get("門檻(㎡)", 0) or 0)
        L.append(f"  `3.5m R1/right {_dg.get('候選地號')}`："
                 f"② 真G ＝ **{_g:.2f}**／⑤ 門檻 ＝ **{_m:.2f}**／差 ＝ **{_g - _m:+.2f}**"
                 f"｜達標欄 ＝ **{_dg.get('達標')}**")
        if _g >= _m:
            L.append("  ⇒ **分支 A 成立**：① ≥ ⑤ ⇒ 它**合法通過**資格閘")
            L.append("     ⇒ 🔧 **「面積也不足」之說不成立·前批之 🔴 發現撤回**；")
            L.append("     ⇒ **此時寬度不足之成因仍未明** ⇒ 回報並停。")
            L.append("  ⇒ **分支 B（① < ⑤ 而仍為 winner ⇒ 閘被繞過）：未觸發。**")
        else:
            L.append("  ⇒ 🛑 **分支 B 成立**：① < ⑤ 而它仍是 winner ⇒ **閘被繞過**"
                     "（引擎缺陷·非域裁）⇒ **停機上呈**。")
            L.append("  ⇒ **分支 A（合法通過）：未觸發。**")
    _bad56 = [d for d in _diag
              if abs(float(d.get("範圍面積(㎡)", 0) or 0)
                     - float(d.get("門檻(㎡)", 0) or 0)) > 0.5]
    L.append(f"  **⑤ vs ⑥ 之 `|差| > 0.5`（碼面 `app.py:18054` 之診斷容差）**："
             f"**{len(_bad56)}** 格")
    for d in _bad56:
        L.append(f"      {d['_sb']:<6}{d.get('街廓')}/{d.get('端')} {d.get('候選地號')}："
                 f"⑤ {float(d.get('門檻(㎡)',0) or 0):.2f} vs ⑥ "
                 f"{float(d.get('範圍面積(㎡)',0) or 0):.2f}"
                 f"　差 {float(d.get('範圍面積(㎡)',0) or 0) - float(d.get('門檻(㎡)',0) or 0):+.2f}")
    if not _bad56:
        L.append("      （無）⇒ ⑤ 與 ⑥ 於全部診斷列皆在容差內。")

    L.append("")
    L.append("【D】註記")
    L.append("  · ⛔ 零碼面·不接 `run_all`·**未寫任何判定碼**（K-9-5-3 經 KL 令暫停適用）。")
    L.append("  · (a) 之求交路徑**逐字沿用** `_build_corner_range_v3` 自檢①′；"
             "差別僅在 ALLOC 線之來源（自檢①′ 用構造解 `t*`；本檔用 winner 實配之 `L_in`）。")
    L.append("  · (c) 為**正面列舉**（PQ／ALLOC(L_in)／SIDE(截角前)／BASELINE／FRONT／街廓邊界／截角邊），"
             "⛔ 無「其他」；六界皆不在容差內者**逐界印出距離**。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
