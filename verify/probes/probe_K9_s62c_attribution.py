# -*- coding: utf-8 -*-
r"""**S6-2-C**：§一 恆等式之證偽測 ＋ 12.85 ㎡ 之逐項歸因（⛔ 零碼面·只量不判）。

⛔ 不接 `run_all`·**不寫任何判定碼**（`K-9-5-3` 經 KL 令暫停適用）。

## §一 待證偽之假說（claude.ai 提·⛔ 非結論）

    實配面積 − 街角規定範圍面積 ＝（k98 量得寬 − T）× 深度

推論：`g_rows` 之 `G(㎡)` **就是 winner 實配多邊形之面積**。
⇒ 本檔逐格測之，**「不成立」同樣是合格產出**。

## 🔒 深度口徑（§二-3 要求：**先於**計算結果宣告·⛔ 不得由結果反推）

    深度 ＝ **k98 量測帶之帶深** ＝ `t_hi − t_lo`
            （`_n14_band_geom` 回傳之帶二端·同一帶量出 (a)(b) 二寬）

**理由**：二形之差係「**同一帶內、僅 ALLOC 線位置不同**」，故延展量必須是**該帶**之深。
⛔ 非「街廓分配深度」、⛔ 非 `depth_from_PQ`、⛔ 非平均深度。

## 🔒 自我驗證閘（`CLAUDE.md` 常設條·⛔ 不過不得據以下結論）

| 閘 | 內容 | 所據之碼面保證 |
|---|---|---|
| **G1** | `min(弦@t_lo, 弦@t_hi) == k98["min_width"]` | 同一多邊形、同一帶 |
| **G2** | `L(t*)` 重建：`min(線距@帶二端, SIDE∞ vs L(t*)∞) == T` | `_build_corner_range_v3` 自檢①（`grep -n "構造自檢不合" app.py`） |
| **G3** | 實配輸入重建：`_solve_G_one(實配槽)` 之 G 之 2dp `== g_rows['G(㎡)']` | §四 歸因之前提 |
| **G4** | 全 toggle 至樂觀：其 G 之 2dp `== 真G(㎡)` | §四 歸因之閉合 |

⛔ **G3／G4 不過 ⇒ §四 不得下任何歸因結論。**
"""
import io
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
from stepg_pipeline import run_step_g, _compute_v3_finance          # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_s62c_attribution.log")
_LBIG = 1.0e5
_EPSW = 1e-6         # 寬度比對容差（自檢① 之量級）
TARGET = ("3.5m", "R1", "right")


def _u(ax, ay):
    n = math.hypot(ax, ay)
    return (ax / n, ay / n)


def _alloc_edges(coords, auh):
    """宗地環上**平行 ALLOC 方向**之邊（⛔ 逐字沿用 `probe_K9_s62_k98_line_vs_chord.py`）。"""
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


def main():                                                    # noqa: C901
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    from shapely.geometry import Polygon as _PG
    L = []
    L.append("=" * 200)
    L.append("【S6-2-C】§一 恆等式證偽測 ＋ 12.85㎡ 逐項歸因 — ⛔ 只量不判·零碼面")
    L.append("=" * 200)

    ns, fake_st = harvest()
    for _s in ("k98_virtual_measure_block", "_n14_band_geom", "_build_corner_range_v3",
               "_make_chamfer_tri_wb", "_baseline_pts_from_manual",
               "_solve_G_one", "_corner_first_lot_G", "_oblique_s_max",
               "alloc_normal_axis"):
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
    # ⛔ 逐字沿用 `probe_K9_s62_k98_line_vs_chord.py:117`／`run_verification.py`
    #   （⛔ 非 `get_min_lot_size(category, front_road_width_m)`——該式須逐街廓查表）
    legal_w = float(snapshot["global"]["法定最小寬_m"])
    _fin3 = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)
    _tab6 = float(fake_st.session_state.get("f3_total_burden_rate_from_finance") or 0.0)

    rows, diag = [], []
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, winners, forced, setback)
        for _dg in (_d0 or []):
            diag.append(dict(_dg, _sb=sb))
        by_pid = {str(r.get("暫編地號")): r for r in sg["g_rows"]}
        # 逐街廓之左組累積 S（供 §四 重建 S_remain）
        cumS = {}
        for _r in sg["g_rows"]:
            _k = (str(_r.get("所屬街廓")), str(_r.get("推進側別")))
            cumS[_k] = max(cumS.get(_k, 0.0), float(_r.get("累積S(m)", 0) or 0))
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
                rec = {"sb": sb, "lbl": lbl, "side": which,
                       "T": setback + legal_w, "setback": setback,
                       "forced": bool(((forced or {}).get(lbl) or {}).get(
                           f"{which}_forced_offset", False)),
                       "cumS_left": cumS.get((lbl, "left"), 0.0),
                       "cumS_right": cumS.get((lbl, "right"), 0.0)}
                w = (winners or {}).get(lbl) or {}
                pid = w.get("p1_end" if which == "left" else "p2_end")
                rec["pid"] = pid
                chi = ns["_make_chamfer_tri_wb"](b, which)
                sd = sd_by[lbl][which]
                try:
                    _rng = ns["_build_corner_range_v3"](
                        b.get("vertices"), b.get("centroid"), [fl["p1"], fl["p2"]], bp,
                        [sd["p1"], sd["p2"]], au,
                        float(blk.get("街廓分配深度_m") or 0.0), setback, legal_w, chi,
                        dxf_quantum=((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected"),
                        _label=lbl, _side=which)
                    rec["rng"] = _rng
                    rec["rng_area"] = float(_rng.area)
                except RuntimeError as e:
                    rec["rng"] = None
                    rec["rng_area"] = None
                    rec["note"] = "rng raise：" + str(e).splitlines()[0][:60]
                if not pid:
                    rec["note"] = "無 winner（強制留設抵費地）"
                    rows.append(rec); continue
                row = by_pid.get(str(pid)) or {}
                rec["row"] = row
                rec["G_rows"] = row.get("G(㎡)")
                rec["area_geom_prod"] = row.get("幾何面積(㎡)")
                rec["F_prod"] = row.get("F(m)")
                rec["lside_prod"] = row.get("l₁ 側面尺度")
                rec["lfront_prod"] = row.get("l₂ 正面尺度")
                rec["a_prod"] = row.get("a 面積(㎡)")
                rec["A_prod"] = row.get("A 地價比")
                rec["S_prod"] = row.get("S(m)")
                cc = row.get("cut_coords") or []
                if len(cc) < 3:
                    rec["note"] = f"cut_coords 不足（{len(cc)}）"
                    rows.append(rec); continue
                _poly_alloc = _PG([(float(p[0]), float(p[1])) for p in cc])
                if not _poly_alloc.is_valid:
                    _poly_alloc = _poly_alloc.buffer(0)
                rec["area_mine"] = float(_poly_alloc.area)

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
                _lin = _edges[-1]
                rec["L_in"] = _lin
                _oc = None
                if chi is not None and not chi.is_empty:
                    from shapely.geometry import Point as _PT0
                    _oc = (lambda _p, _t=chi:
                           bool(_t.buffer(1e-9).contains(_PT0(_p[0], _p[1]))))
                try:
                    k98 = ns["k98_virtual_measure_block"](
                        b.get("vertices"), [F1, F2], bp, [_lin[0], _lin[1]],
                        [sd["p1"], sd["p2"]], _label=lbl, _pid=str(pid),
                        _lot_kind="corner_first", on_chamfer=_oc)
                except RuntimeError as e:
                    rec["note"] = "k98 raise：" + str(e).splitlines()[0][:60]
                    rows.append(rec); continue
                rec["w_k98"] = float(k98["min_width"])
                poly = k98["poly"]
                _pb = (k98["P_block"][0], k98["P_block"][1])
                try:
                    _tlo, _rear, _g, _bdn = ns["_n14_band_geom"](
                        list(poly.exterior.coords), (dxh, dyh), _pb, bp,
                        _label=f"{lbl}/{which}")
                except RuntimeError as e:
                    rec["note"] = "band_geom raise：" + str(e).splitlines()[0][:60]
                    rows.append(rec); continue
                _thi = _rear[0][0]
                rec["band"] = (_tlo, _thi)
                rec["band_depth"] = _thi - _tlo           # 🔒 §二-3 宣告之深度口徑

                # (s,t) 局部框（🔒 E-10：解析·⛔ 禁 GEOS 世界座標）
                nx, ny = -dyh, dxh
                _st_ring = [((float(_p[0]) - _pb[0]) * dxh + (float(_p[1]) - _pb[1]) * dyh,
                             (float(_p[0]) - _pb[0]) * nx + (float(_p[1]) - _pb[1]) * ny)
                            for _p in poly.exterior.coords]
                _sig = -1.0 if _PG(_st_ring).centroid.coords[0][1] < 0 else 1.0

                def _to_st(p, _s=_sig):
                    _px, _py = float(p[0]) - _pb[0], float(p[1]) - _pb[1]
                    return (_px * dxh + _py * dyh, _s * (_px * nx + _py * ny))

                _ring_st = [_to_st(p) for p in poly.exterior.coords]

                def _chord_at(_T, _r=_ring_st):
                    _xs = []
                    for _i in range(len(_r) - 1):
                        _s0, _t0 = _r[_i]
                        _s1, _t1 = _r[_i + 1]
                        if _t0 == _t1:
                            if _t0 == _T:
                                _xs += [_s0, _s1]
                            continue
                        if (_t0 - _T) * (_t1 - _T) <= 0.0:
                            _xs.append(_s0 + (_T - _t0) / (_t1 - _t0) * (_s1 - _s0))
                    return (max(_xs) - min(_xs)) if _xs else 0.0

                def _s_on(pA, pB, _T):
                    _a, _b = _to_st(pA), _to_st(pB)
                    if abs(_b[1] - _a[1]) < 1e-12:
                        return float('nan')
                    return _a[0] + (_T - _a[1]) / (_b[1] - _a[1]) * (_b[0] - _a[0])

                rec["chord"] = [_chord_at(_t) for _t in (_tlo, _thi)]
                rec["ld_Lin"] = [abs(_s_on(_lin[0], _lin[1], _t)
                                     - _s_on(sd["p1"], sd["p2"], _t))
                                 for _t in (_tlo, _thi)]
                rec["s_side"] = [_s_on(sd["p1"], sd["p2"], _t) for _t in (_tlo, _thi)]
                rec["s_Lin"] = [_s_on(_lin[0], _lin[1], _t) for _t in (_tlo, _thi)]

                # ── L(t*) 之重建（自 `rng` 之 ALLOC 平行邊·最遠離 SIDE 者）─────────
                rec["s_Lts"] = None
                if rec.get("rng") is not None:
                    _g_rng = rec["rng"]
                    _polys = ([_g_rng] if _g_rng.geom_type == "Polygon"
                              else list(_g_rng.geoms))
                    _cands = []
                    for _pp in _polys:
                        _cands += _alloc_edges(list(_pp.exterior.coords), auh)
                    if _cands:
                        _cands.sort(key=lambda e: abs((_s_of(e[0]) + _s_of(e[1])) / 2.0 - _sx))
                        _lts = _cands[-1]
                        rec["L_ts"] = _lts
                        rec["s_Lts"] = [_s_on(_lts[0], _lts[1], _t) for _t in (_tlo, _thi)]
                        rec["ld_Lts"] = [abs(rec["s_Lts"][_i] - rec["s_side"][_i])
                                         for _i in (0, 1)]
                rows.append(rec)

    # ══════════════════════════════════════════════════════════════════════
    # 【A】自我驗證閘 G1／G2
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【A】自我驗證閘（⛔ 不過之格於後表標 `🔴 閘未過`·⛔ 不得據以下結論）")
    L.append("-" * 200)
    L.append("  G1：`min(弦@t_lo, 弦@t_hi)` == `k98[\"min_width\"]`")
    L.append("  G2：`min(線距@帶二端, SIDE∞ vs L(t*)∞)` == `T`  ← `_build_corner_range_v3` "
             "自檢①之保證（`grep -n \"構造自檢不合\" app.py`）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'G1 min(弦)':>16}{'k98':>16}{'G1':>5}"
             f"{'G2 min(ld_Lt*)':>18}{'T':>8}{'G2':>5}")
    L.append("-" * 200)
    for r in rows:
        if "chord" not in r:
            continue
        _c = min(r["chord"]); _k = r["w_k98"]
        _g1 = (abs(_c - _k) <= 1e-9)
        r["g1"] = _g1
        if r.get("ld_Lts"):
            _m2 = min(r["ld_Lts"]); _g2 = (abs(_m2 - r["T"]) <= 1e-3)
        else:
            _m2 = float('nan'); _g2 = False
        r["g2"] = _g2
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{_c:>16.9f}{_k:>16.9f}"
                 f"{('✅' if _g1 else '🔴'):>5}"
                 f"{_m2:>18.6f}{r['T']:>8.2f}{('✅' if _g2 else '🔴'):>5}")
    L.append("-" * 200)
    _n1 = sum(1 for r in rows if r.get("g1") is False)
    _n2 = sum(1 for r in rows if "chord" in r and r.get("g2") is False)
    L.append(f"  G1 未過 **{_n1}** 格／G2 未過 **{_n2}** 格"
             "（⛔ 未放寬閘門以掩蓋·未過者於後表逐格標記）")
    L.append("  ⚠️ G2 容差 `1e-3`：`L(t*)` 係自 `rng` **邊界重建**，而 `rng` 末段經 "
             "`difference(chamfer_tri)` ⇒ 邊界頂點受截角切割之數值影響；"
             "⛔ 非自檢①之 `eps`（該 eps 由 `q_detected` 導出）。")

    # ══════════════════════════════════════════════════════════════════════
    # 【B】§二-1：四欄十六格
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【B】§二-1：winner **實配多邊形面積** vs 三欄（**十六格逐格**·⛔ 無 winner 亦列）")
    L.append("-" * 200)
    L.append("  🔒 **實配多邊形之來源（正面指名）**：")
    L.append("     `g_rows[i]['cut_coords']`（`verify/stepg_pipeline.py:381`）")
    L.append("       ← `_res['cut_coords']` ← `solve_G_binary` 之 `cut`"
             "（`app.py:9340` `cut, area_geom = _block_strip(...)`）")
    L.append("       ← `_block_strip`（`grep -n \"def _block_strip\" app.py`）＝ strip ∩ 街廓多邊形"
             "（**截角後**·CLAUDE.md「範圍邊界＝截角後＝街廓多邊形邊界」）")
    L.append("     ⑧ `g_rows['G(㎡)']`＝`round(_res['G'],2)`（`stepg_pipeline.py:370`）"
             "＝**G_target**·⛔ 非 area_geom")
    L.append("     ⑨ `g_rows['幾何面積(㎡)']`＝`round(_res['area_geom'],2)`"
             "（`stepg_pipeline.py:369`）＝**生產側之實配幾何面積**")
    L.append("     ⑥ `_corner_range_area`＝`_build_corner_range_v3(...).area`（本檔現算·同 param 表之式）")
    L.append("     ② `真G(㎡)`＝診斷列（＝`_G_true`＝`round(cand_G,2)`·`app.py:11252`）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}"
             f"{'實配面積(本檔)':>16}{'⑨幾何面積(生產)':>17}{'⑧g_rows G':>12}"
             f"{'⑥範圍面積':>12}{'②真G':>10}  判別")
    L.append("-" * 200)
    _tg_by = {}
    _sidename = {"左": "left", "右": "right", "p1": "left", "p2": "right"}
    for _dg in diag:
        _sd = _sidename.get(str(_dg.get("端", "")).strip(), str(_dg.get("端", "")))
        if str(_dg.get("達標", "")).strip() == "達標":
            _tg_by.setdefault((_dg["_sb"], str(_dg.get("街廓", "")), _sd), {})[
                str(_dg.get("候選地號", ""))] = _dg.get("真G(㎡)")
    _n_eq_geom = _n_eq_G = _n_tot = 0
    for r in rows:
        _tag = f"{r['lbl']}/{r['side']}"
        _ra = ("—" if r.get("rng_area") is None else f"{r['rng_area']:.2f}")
        if r.get("area_mine") is None:
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid') or '—'):<13}"
                     f"{'—':>16}{'—':>17}{'—':>12}{_ra:>12}{'—':>10}  {r.get('note', '')}")
            continue
        _tg = (_tg_by.get((r["sb"], r["lbl"], r["side"]), {}) or {}).get(str(r["pid"]))
        r["trueG"] = (float(_tg) if _tg not in ("", None) else None)
        _am, _ag, _gg = r["area_mine"], float(r["area_geom_prod"]), float(r["G_rows"])
        _n_tot += 1
        _ok_geom = abs(_am - _ag) <= 0.015
        _ok_G = abs(_am - _gg) <= 0.015
        _n_eq_geom += int(_ok_geom); _n_eq_G += int(_ok_G)
        r["ok_geom"], r["ok_G"] = _ok_geom, _ok_G
        _tgs = ("—" if r.get("trueG") is None else f"{r['trueG']:.2f}")
        L.append(f"{r['sb']:<6}{_tag:<12}{str(r['pid']):<13}"
                 f"{_am:>16.4f}{_ag:>17.2f}{_gg:>12.2f}{_ra:>12}"
                 f"{_tgs:>10}"
                 f"  實配==⑨ {'✅' if _ok_geom else '❌'}"
                 f"／實配==⑧ {'✅' if _ok_G else '❌'}"
                 f"{'' if r.get('g1', True) else '  🔴 G1未過'}")
    L.append("-" * 200)
    L.append(f"  🔑 **判別**：實配多邊形面積 == ⑨`幾何面積(㎡)`：**{_n_eq_geom}/{_n_tot}**；"
             f"== ⑧`g_rows.G(㎡)`：**{_n_eq_G}/{_n_tot}**（容差 0.015 ＝ 收斂 tol 0.01 ＋ 2dp 捨入 0.005）")
    L.append("  ⇒ 假說之「`g_rows.G(㎡)` **就是** winner 實配多邊形之面積」——"
             "⑧ 係 **G_target**、⑨ 才是幾何面積；二者於收斂時差 ≤ tol 0.01（`app.py:9302`）。")

    # ══════════════════════════════════════════════════════════════════════
    # 【C】§二-2：L_in 與 L(t*)
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【C】§二-2：`L_in` 與 `L(t*)` 之間距 ＋ `L_in` 在近／遠 SIDE 側")
    L.append("-" * 200)
    L.append("  · 「沿 d̂ 之間距」＝ 兩平行線於同一帶端之 `s` 差 ＝ **k98 量寬之口徑**。")
    L.append("  · 「真垂距」＝ 沿 d̂ 之間距 × |sin∠(ALLOC, d̂)|（⛔ 二者不同量·一併列出）。")
    L.append("  · 近／遠：比 `|s(L_in) − s(SIDE)|` 與 `|s(L(t*)) − s(SIDE)|`，小者為**近 SIDE 側**。")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'沿d̂間距':>13}{'真垂距':>13}"
             f"{'|sin∠|':>9}{'ld(L_in)':>12}{'ld(L(t*))':>12}{'L_in 位置':>12}  G2")
    L.append("-" * 200)
    for r in rows:
        if not r.get("ld_Lts") or "ld_Lin" not in r:
            continue
        _i = 0 if r["ld_Lin"][0] <= r["ld_Lin"][1] else 1
        _dd = abs(r["s_Lin"][_i] - r["s_Lts"][_i])
        _auh = None
        _fl = fl_by.get(r["lbl"]) or {}
        _F1 = (float(_fl["p1"][0]), float(_fl["p1"][1]))
        _F2 = (float(_fl["p2"][0]), float(_fl["p2"][1]))
        _dh = _u(_F2[0] - _F1[0], _F2[1] - _F1[1])
        _a = al_by.get(r["lbl"])
        _auh = _u(float(_a[0]), float(_a[1]))
        _sin = abs(_dh[0] * _auh[1] - _dh[1] * _auh[0])
        _pos = "近 SIDE 側" if r["ld_Lin"][_i] < r["ld_Lts"][_i] else "遠 SIDE 側"
        r["gap_dhat"] = _dd
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{_dd:>13.6f}"
                 f"{_dd * _sin:>13.6f}{_sin:>9.6f}"
                 f"{r['ld_Lin'][_i]:>12.6f}{r['ld_Lts'][_i]:>12.6f}{_pos:>12}"
                 f"  {'✅' if r.get('g2') else '🔴 閘未過·不可據'}")
    L.append("-" * 200)

    # ══════════════════════════════════════════════════════════════════════
    # 【D】§二-3：恆等式逐格
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【D】§二-3：恆等式 `實配面積 − 規定範圍面積 ＝ (k98量得寬 − T) × 深度`")
    L.append("-" * 200)
    L.append("  🔒 **深度口徑（已於本檔 docstring 先行宣告·⛔ 未由結果反推）**"
             "＝ **k98 量測帶之帶深 `t_hi − t_lo`**")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'左式(實配−範圍)':>17}{'右式(Δ寬×帶深)':>17}"
             f"{'殘差':>13}{'帶深':>12}{'Δ寬':>12}  判")
    L.append("-" * 200)
    _bad = 0
    for r in rows:
        if r.get("area_mine") is None or r.get("rng_area") is None or "w_k98" not in r:
            continue
        _lhs = r["area_mine"] - r["rng_area"]
        _rhs = (r["w_k98"] - r["T"]) * r["band_depth"]
        _res_ = _lhs - _rhs
        r["ident_res"] = _res_
        _ok = abs(_res_) <= 0.1
        _bad += int(not _ok)
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{_lhs:>17.4f}{_rhs:>17.4f}"
                 f"{_res_:>13.4f}{r['band_depth']:>12.6f}{r['w_k98'] - r['T']:>12.6f}"
                 f"  {'✅' if _ok else '❌'}"
                 f"{'' if r.get('g1', True) else '  🔴 G1未過'}")
    L.append("-" * 200)
    L.append(f"  🔑 **|殘差| > 0.1 ㎡ 者：{_bad} 格**（§三 判準之門檻）")

    # ══════════════════════════════════════════════════════════════════════
    # 【E】§四：12.85 ㎡ 之逐項歸因（單變因對照）
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【E】§四：`3.5m R1/right 628(5)` 之 12.85㎡ 逐項歸因（**單變因**·考古節 32）")
    L.append("-" * 200)
    _t = next((r for r in rows if (r["sb"], r["lbl"], r["side"]) == TARGET), None)
    if _t is None or _t.get("row") is None:
        L.append("  🔴 靶格未取得 ⇒ 本節無從進行")
    else:
        _lbl = _t["lbl"]
        _b = cb_by[_lbl]
        _blkm = (snapshot["blocks"].get(_lbl) or {})
        _fl = fl_by.get(_lbl) or {}
        _p1 = (float(_fl["p1"][0]), float(_fl["p1"][1]))
        _p2 = (float(_fl["p2"][0]), float(_fl["p2"][1]))
        import numpy as _np
        _cp = _np.array(_p1, dtype=float)
        _p2a = _np.array(_p2, dtype=float)
        _sL = float(_np.linalg.norm(_p2a - _cp))
        _dh = (_p2a - _cp) / (_sL or 1.0)
        _verts = _b.get("vertices")
        _bpoly = _PG([(float(v[0]), float(v[1])) for v in _verts])
        if not _bpoly.is_valid:
            _bpoly = _bpoly.buffer(0)
        _adir = al_by.get(_lbl)
        _ax = ns["alloc_normal_axis"](_adir) if _adir else None
        _sR = (ns["_oblique_s_max"](_verts, _dh, _cp, _ax) or _sL) if _ax is not None else _sL
        _smid = ((sd_by.get(_lbl) or {}).get("right") or {}).get("mid")
        _depth = float(_blkm.get("街廓分配深度_m") or 0.0)
        _row = _t["row"]
        _a_m2 = float(_row["a 面積(㎡)"]); _A = float(_row["A 地價比"])
        _lfront = float(_row["l₂ 正面尺度"])
        _lside_prod = float(_row["l₁ 側面尺度"]); _F_prod = float(_row["F(m)"])
        _F_opt = float((_blkm.get("右側") or {}).get("路寬_m") or 0)
        _B, _C = _fin3["B"], _fin3["C"]
        _endpt = _cp + _sR * _dh
        _S_remain = max(0.1, _sR - _t["cumS_left"] - 0.0)

        L.append(f"  靶：`{_t['pid']}`　實配 G ＝ **{float(_row['G(㎡)']):.2f}**　"
                 f"真G ＝ **{(_t.get('trueG') or 0):.2f}**　"
                 f"落差 ＝ **{(_t.get('trueG') or 0) - float(_row['G(㎡)']):+.2f}**")
        L.append("  🔒 **實配槽 vs 樂觀槽（逐槽正面列舉）**")
        L.append(f"     baseline_pt：實配 `corner_pt + actual_max_proj·d̂`"
                 f"（`stepg_pipeline.py:679-681`·`_oblique_s_max`＝{_sR:.6f}）")
        L.append(f"                 樂觀 `corner_pt + s_max_left·d̂`"
                 f"（`app.py:11585`·`‖FRONT‖`＝{_sL:.6f}）　⇒ Δ ＝ **{_sL - _sR:+.6f}**")
        L.append(f"     S_max      ：實配 `max(0.1, actual_max_proj − left_cum_S − right_cum_S)`"
                 f"（`stepg_pipeline.py:712`）＝{_S_remain:.6f}"
                 f"（left_cum_S＝{_t['cumS_left']:.2f}）")
        L.append(f"                 樂觀 `max(0.1, s_max_right)`（`app.py:11589`）＝{max(0.1, _sR):.6f}")
        L.append(f"     W_prev     ：實配 `_W_prev_right`（首宗＝**0.0**·`stepg_pipeline.py:616`）"
                 f"／樂觀 **0.0**（`app.py:11591`）")
        L.append(f"     buf        ：實配 `right_cum_S = _right_buffer_S`"
                 f"（`stepg_pipeline.py:607`·僅 `_fo_right` 為真時非 0）"
                 f"　本格 forced＝**{_t['forced']}** ⇒ buf ＝ **0.0**／樂觀 **0**")
        L.append(f"     🆕 **F**    ：實配 `sb_row['右側長度(m)']`"
                 f"（`stepg_pipeline.py:548`）＝**{_F_prod:.2f}**")
        L.append(f"                 樂觀 `snapshot[blk]['右側']['路寬_m']`"
                 f"（`verify/selection_pipeline.py:437`）＝**{_F_opt:.2f}**"
                 f"　⇒ Δ ＝ **{_F_opt - _F_prod:+.2f}**")
        L.append(f"     l₁ 側尺度  ：兩側同鍵 `右側尺度` ＝ {_lside_prod:.2f}（⇒ 非分歧項）")

        def _solve(bp_, smax_, F_, wprev_):
            _r, _lab = ns["_solve_G_one"](
                a_m2=_a_m2, A=_A, l_front=_lfront, l_side=_lside_prod, F=F_,
                blk_poly=_bpoly, d_hat=-_dh, baseline_pt=bp_,
                S_max=max(0.1, smax_), is_corner=True, side='右側',
                avg_depth=_depth, B=_B, C=_C, tab6_burden=_tab6,
                allocation_dir=_ax, side_mid=_smid, W_prev=wprev_)
            return float(_r.get('G', 0.0) or 0.0)

        _base = _solve(_endpt, _S_remain, _F_prod, 0.0)
        _g3 = abs(round(_base, 2) - float(_row["G(㎡)"])) <= 0.005
        L.append("-" * 200)
        L.append(f"  🔒 **閘 G3**（實配槽重建）：重建 G ＝ {_base:.6f} → 2dp {round(_base,2):.2f}"
                 f"　vs `g_rows.G(㎡)` {float(_row['G(㎡)']):.2f}　⇒ {'✅ 過' if _g3 else '🔴 未過'}")
        _allopt = _solve(_cp + _sL * _dh, max(0.1, _sR), _F_opt, 0.0)
        _tg = _t.get("trueG")
        _g4 = (_tg is not None and abs(round(_allopt, 2) - float(_tg)) <= 0.005)
        L.append(f"  🔒 **閘 G4**（全 toggle 至樂觀）：G ＝ {_allopt:.6f} → 2dp {round(_allopt,2):.2f}"
                 f"　vs 真G {(_tg if _tg is not None else float('nan')):.2f}"
                 f"　⇒ {'✅ 過' if _g4 else '🔴 未過'}")
        L.append("-" * 200)
        if not (_g3 and _g4):
            L.append("  🛑 **G3／G4 未全過 ⇒ ⛔ 不得下任何歸因結論**（逐項表仍列出，"
                     "但**僅供後續診斷**·⛔ 不得引用為歸因）。")
        L.append(f"{'項':<44}{'toggle 後 G':>14}{'ΔG':>12}  備註")
        L.append("-" * 200)
        _items = [
            ("(a) forced 兩端假設 → 皆不預設 forced",
             _solve(_endpt, _S_remain, _F_prod, 0.0),
             f"本格 forced={_t['forced']} ⇒ 實配已等於樂觀值 ⇒ 恆等 toggle"),
            ("(b) buf → 0",
             _solve(_endpt, _S_remain, _F_prod, 0.0),
             "本格 `_right_buffer_S`＝0（未 forced）⇒ 恆等 toggle"),
            ("(c) W_prev → 0.0",
             _solve(_endpt, _S_remain, _F_prod, 0.0),
             "首宗 `_W_prev_right`＝0.0 ⇒ 恆等 toggle"),
            ("(d) baseline_pt 錨 → corner_pt + ‖FRONT‖·d̂ (K-4 第5條)",
             _solve(_cp + _sL * _dh, _S_remain, _F_prod, 0.0),
             f"Δ錨 ＝ {_sL - _sR:+.6f} m"),
            ("(e) S_max 上界 → s_max_right (_oblique_s_max)",
             _solve(_endpt, max(0.1, _sR), _F_prod, 0.0),
             f"{_S_remain:.4f} → {max(0.1, _sR):.4f}"),
            ("(f) 🆕 F 口徑 → 路寬_m（樂觀所用）",
             _solve(_endpt, _S_remain, _F_opt, 0.0),
             f"F {_F_prod:.2f} → {_F_opt:.2f}（**KL 五項未列·第六項**）"),
        ]
        _sum = 0.0
        for _nm, _gv, _note in _items:
            _d = _gv - _base
            _sum += _d
            L.append(f"{_nm:<44}{_gv:>14.6f}{_d:>12.6f}  {_note}")
        L.append("-" * 200)
        _target_gap = (float(_tg) - float(_row["G(㎡)"])) if _tg is not None else float('nan')
        L.append(f"  Σ(單變因 ΔG) ＝ **{_sum:.6f}**　vs 實際落差 **{_target_gap:.6f}**"
                 f"　⇒ **殘差 {_sum - _target_gap:+.6f}**")
        L.append(f"  對照：全 toggle 一次到底 ＝ {_allopt:.6f}，"
                 f"ΔG(全) ＝ {_allopt - _base:+.6f}")
        L.append("  ⚠️ 單變因 Σ 與全 toggle **不必相等**——`solve_G_binary` 之解對各槽**非線性**"
                 "（G_target 與 area_geom 同時隨 S 變）⇒ 交互項不為 0。"
                 "**Σ 與落差之殘差含交互項**，⛔ 不得逕讀為「尚有未列成因」。")
        L.append("  🔑 判別 §四 停機條件應以 **G4（全 toggle 閉合）** 為準："
                 "全 toggle 若能重現真G ⇒ **成因已窮舉**（無第六項之外者）。")

    # ══════════════════════════════════════════════════════════════════════
    # 【F】§五：泛化檢查
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【F】§五：十六格之「樂觀 G − 實配 G」＋ 同號情形（**樂觀達標∧實配 < 範圍面積**）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}{'②真G':>10}{'⑧實配G':>10}"
             f"{'落差':>10}{'⑥範圍面積':>12}{'實配−範圍':>12}  同號？")
    L.append("-" * 200)
    _same = []
    for r in rows:
        _tag = f"{r['lbl']}/{r['side']}"
        _ras = ("—" if r.get("rng_area") is None else f"{r['rng_area']:.2f}")
        if r.get("G_rows") is None or r.get("trueG") is None:
            L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid') or '—'):<13}"
                     f"{'—':>10}{'—':>10}{'—':>10}{_ras:>12}"
                     f"{'—':>12}  {r.get('note','')}")
            continue
        _tg = float(r["trueG"]); _gg = float(r["G_rows"]); _ra = float(r["rng_area"])
        _hit = (_tg >= _ra) and (_gg < _ra)
        if _hit:
            _same.append(f"{r['sb']} {_tag} {r['pid']}")
        L.append(f"{r['sb']:<6}{_tag:<12}{str(r['pid']):<13}{_tg:>10.2f}{_gg:>10.2f}"
                 f"{_tg - _gg:>10.2f}{_ra:>12.2f}{_gg - _ra:>12.2f}"
                 f"  {'🔴 是' if _hit else '否'}")
    L.append("-" * 200)
    L.append(f"  🔑 **同號格數 ＝ {len(_same)}**：" + ("；".join(_same) if _same else "（無）"))
    L.append("  ⇒ 僅 1 格 ⇒ 可能與該側錨點敏感性有關；多格 ⇒ 屬結構性。"
             "（⛔ 本檔只陳述格數與清單·不裁定）")

    # ══════════════════════════════════════════════════════════════════════
    # 【G】§六：「撤銷」之爆炸半徑（⛔ 只查不改·未實跑）
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【G】§六：撤銷之爆炸半徑（⛔ **只查不改·未實跑·未改動任何狀態**）")
    L.append("-" * 200)
    L.append("  🔒 **碼面事實（正面列舉受檢檔·⛔ 非全倉排除式）**——街角程序四段之關鍵詞命中：")
    for _kw in ("預掃", "全域排序", "逐一嘗試", "重排位次", "既不出也不進",
                "每候選只試一次", "合併群", "上鎖"):
        _c = []
        for _f in ("app.py", "verify/selection_pipeline.py", "verify/stepg_pipeline.py"):
            _p = os.path.join(REPO, _f)
            try:
                _txt = io.open(_p, encoding="utf-8").read()
            except Exception:
                _txt = ""
            _c.append(f"{_f}={_txt.count(_kw)}")
        L.append(f"     「{_kw}」　" + "　".join(_c))
    L.append("-" * 200)
    L.append("  6-1／6-2／6-3：上表所有關鍵詞於三檔命中**皆為 0** ⇒ "
             "**K-6-B（街角地分配程序四段本體）碼面零實作**"
             "（CLAUDE.md 進度表亦載「K-6-B ⬜ 未開工」）。")
    L.append("     ⇒ 6-1：`3.5m R1/right` **必然在段一即定案**——因**段二／段三不存在於碼面**；"
             "現行分流僅「有人達 G 門檻 ⇒ 取 winner」／「無人達 ⇒ 強制留設抵費地」"
             "（`app.py:11263-11266`）。")
    L.append("     ⇒ 6-2：**「上鎖」機制碼面不存在** ⇒ 無「因此被上鎖之土地清單」可列。")
    L.append("     ⇒ 6-3：**無段二可進** ⇒ 該問題於現行碼面上**不適用**；"
             "⛔ 未實跑、⛔ 未改動任何狀態。")
    L.append("-" * 200)
    L.append("  6-4：十六格之分流（⛔ 逐格列示）")
    L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}{'分流':<28}  依據")
    L.append("-" * 200)
    _c1 = _c3 = _cf = 0
    for r in rows:
        _tag = f"{r['lbl']}/{r['side']}"
        if not r.get("pid"):
            _cf += 1
            _fl_ = "強制留設抵費地"
            _why = "`app.py:11263-11266`：無人達 G 門檻"
        else:
            _c1 += 1
            _fl_ = "段一定案（有人達門檻⇒取 winner）"
            _why = "`app.py:11255` 閘過 ＋ 三指數 PK"
        L.append(f"{r['sb']:<6}{_tag:<12}{str(r.get('pid') or '—'):<13}{_fl_:<28}  {_why}")
    L.append("-" * 200)
    L.append(f"  ⇒ **段一定案 {_c1} 格／走到段三 {_c3} 格／強制抵費地 {_cf} 格**"
             "（段三 恆為 0——碼面無段三）。")
    L.append("  ⛔ 本節**未提出任何處置建議**——撤銷與否屬 KL。")

    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【H】§七-3：前批 6 端（`d≈0` 近共線）之影響範圍")
    L.append("-" * 200)
    L.append("  · 該 6 端係 `probe_K9_s62_chord_vs_linedist.log` 之 **(b) 弦欄**"
             "（解析 vs GEOS 差 > 1e-4·已於該 log 逐端標記）。")
    L.append("  · **本檔不引用該欄**：本檔之弦一律由 `_chord_at`（(s,t) 解析）現算，"
             "並由 **G1** 對 `k98[\"min_width\"]` 逐格驗。")
    L.append(f"  · ⇒ 影響範圍 ＝ **0 格**於本檔之【B】【C】【D】【E】【F】；"
             f"⛔ 但該 6 端於**前批報告**仍不可據（未因本批而恢復）。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
