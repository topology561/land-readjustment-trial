#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-287` `§三`／`§四`：二線分歧之**土地後果**（對稱差 ＋ 負擔率）／
藍影於 `R4/left` **求值 `0` 次**之成因 —— 🛑 **純量測·出艙即止**。

🛑 **⛔ 改生產碼一字、⛔ 替身、⛔ 反事實**（單 `§七`）。
🔒 **底本** ＝ `verify/probes/probe_WG9286_twolines.py` 之 `drive`（⛔ 另寫第二份驅動）。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**（旗標未設）·`SB ∈ {0.0, 3.5}`。

🔑 **多邊形甲之取法（款 `1`·「取碼面之同一物·⛔ 另建第二份」）**
   ＝ `_lot_gate` 之實參 `blk_ctx['corner_range_polys'][chain_side]` —— 即單所稱之
   `corner_range_polys[_side]` **本身**（`verify/stepg_pipeline.py` `_lg_crp_sg` 所鋪）。
   🔒 **同一物之機驗**：以 `is` 對拍 `_build_corner_range_v3` 之回傳物件。

🔑 **多邊形乙之還原式（款 `2`·逐字具名）** ＝ `_corner_buffer_S` 內 `_band_area` 之逐字：
       a, b = (_lo, float(buf)) if side == 'left' else (s_max - float(buf), s_max)
       w = b - a
       bp = np.asarray(front_p1, dtype=float) + a * _d
       _g, _ar = _block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)
   ⇒ 本器以**同一組實參**呼叫**同一個** `_block_strip`（`ns` 內之生產函式）取其 `_g`。

🔒 **自我驗證閘（三重·任一不過即器紅）**
   `(i)`  `_build_corner_range_v3` 之閉式回代 `|S1_par·sinθ − S1_perp| ≤ 1e-9`（承 `-286`）。
   `(ii)` 多邊形甲 `is` 碼面之 `corner_range_polys[_side]`（⛔ 另建第二份之機驗）。
   `(iii)`工項二之分項重建須**預測**得中 `_k923_gate1` 之**實際呼叫次數**（逐格）。

`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力造不成立）。
"""
import contextlib
import inspect
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(REPO)

W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
RED = [0]


def say(s=""):
    print(s)


def red(s):
    say("🔴 " + s)
    RED[0] = 5


def _f(x):
    try:
        return float(x)
    except Exception:                                            # noqa: BLE001
        return None


def _pt(p):
    if p is None:
        return "None"
    try:
        return "(" + ", ".join(repr(float(c)) for c in list(p)[:2]) + ")"
    except Exception:                                            # noqa: BLE001
        return repr(p)


def _unit(v):
    if v is None:
        return None
    x, y = float(v[0]), float(v[1])
    n = math.hypot(x, y)
    return None if n <= 1e-15 else (x / n, y / n)


def _line_x(p, d, q, e):
    if p is None or d is None or q is None or e is None:
        return None
    det = d[0] * (-e[1]) - d[1] * (-e[0])
    if abs(det) < 1e-15:
        return None
    rx, ry = q[0] - p[0], q[1] - p[1]
    t = (rx * (-e[1]) - ry * (-e[0])) / det
    return (p[0] + t * d[0], p[1] + t * d[1])


def _dist_pt_line(pt, p, d):
    if pt is None or p is None or d is None:
        return None
    return abs((pt[0] - p[0]) * (-d[1]) + (pt[1] - p[1]) * d[0])


def _ext_coords(g):
    """多邊形（含 Multi）之**全部外環頂點**（逐點·⛔ 捨入）。"""
    if g is None or getattr(g, "is_empty", True):
        return []
    out = []
    for p in (list(g.geoms) if hasattr(g, "geoms") else [g]):
        ext = getattr(p, "exterior", None)
        if ext is not None:
            out.extend([(float(c[0]), float(c[1])) for c in ext.coords])
    return out


def _max_vert_dist(a, b):
    """`a` 之**外環頂點**至 `b` 之**邊界**之最大距離（有向·離散）。"""
    cs = _ext_coords(a)
    if not cs or b is None or getattr(b, "is_empty", True):
        return None
    from shapely.geometry import Point
    bd = b.boundary
    return max(float(Point(c).distance(bd)) for c in cs)


def drive(sb):
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    os.environ.pop("WV_K6_STEP0", None)              # 🔒 **態甲**（旗標未設）
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    RNG, BUF, SGB, G1, BLUE, LG = [], [], [], [], [], []

    # ── 包裹 `_build_corner_range_v3`（＋ `settrace` 取其區域值·承 `-286`）──────
    _o_rng = ns["_build_corner_range_v3"]
    CODE = _o_rng.__code__
    SIG_R = inspect.signature(_o_rng)
    KEEP = ("S1_perp", "S1_par", "_seg_P0Ps", "T", "_sin_t", "sux", "suy",
            "dx", "dy", "F1", "S1", "_Tp", "D", "eps")

    def _spy_rng(*a, **kw):
        cap = {}

        def _loc(frame, event, arg):
            if event == "return" and frame.f_code is CODE:
                for k in KEEP:
                    if k in frame.f_locals:
                        cap[k] = frame.f_locals[k]
            return _loc

        def _glob(frame, event, arg):
            return _loc if (event == "call" and frame.f_code is CODE) else None

        old = sys.gettrace()
        sys.settrace(_glob)
        try:
            out = _o_rng(*a, **kw)
        finally:
            sys.settrace(old)
        try:
            ba = SIG_R.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            RNG.append({"label": P.get("_label"), "side": P.get("_side"),
                        "setback": P.get("setback"), "min_width": P.get("min_width"),
                        "baseline_pts": P.get("baseline_pts"),
                        "poly": out, "area": float(out.area), "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            RNG.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_build_corner_range_v3"] = _spy_rng

    # ── 包裹 `_corner_buffer_S`（🔑 本批**另存 `block_poly` 物件本身**）───────
    _o_buf = ns["_corner_buffer_S"]
    CODE_B = _o_buf.__code__
    SIG_B = inspect.signature(_o_buf)
    KEEPB = ("s_min", "s_max", "_lo", "b_lo", "b_hi", "_resid", "_f_hi")

    def _spy_buf(*a, **kw):
        cap = {}

        def _loc(frame, event, arg):
            if event == "return" and frame.f_code is CODE_B:
                for k in KEEPB:
                    if k in frame.f_locals:
                        cap[k] = frame.f_locals[k]
            return _loc

        def _glob(frame, event, arg):
            return _loc if (event == "call" and frame.f_code is CODE_B) else None

        old = sys.gettrace()
        sys.settrace(_glob)
        try:
            out = _o_buf(*a, **kw)
        finally:
            sys.settrace(old)
        try:
            ba = SIG_B.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            BUF.append({"label": P.get("_label"), "side": P.get("side"),
                        "d_hat": P.get("d_hat"), "front_p1": P.get("front_p1"),
                        "allocation_dir": P.get("allocation_dir"),
                        "range_area": P.get("range_area"), "tol": P.get("tol"),
                        "block_poly": P.get("block_poly"),
                        "buf": float(out), "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            BUF.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_corner_buffer_S"] = _spy_buf

    # ── 包裹 `solve_G_binary`（款 `6` 之 `W_0`·承 `-286`）──────────────────
    _o_sgb = ns["solve_G_binary"]
    SIG_S = inspect.signature(_o_sgb)

    def _climb(names, upto=16):
        out = {k: None for k in names}
        for d in range(1, upto + 1):
            try:
                fr = sys._getframe(d + 1)
            except ValueError:
                break
            for k in names:
                if out[k] is None and k in fr.f_locals:
                    out[k] = fr.f_locals[k]
        return out

    def _spy_sgb(*a, **kw):
        out = _o_sgb(*a, **kw)
        try:
            ba = SIG_S.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            c = _climb(["blk_label", "side", "k"])
            sd = c.get("side")
            sd = ("left" if (sd is not None and ("左" in str(sd) or str(sd).lower().startswith("l")))
                  else ("right" if sd is not None else None))
            SGB.append({"blk": c.get("blk_label"), "side": sd, "k": c.get("k"),
                        "is_corner": P.get("is_corner"), "is_chain_head": P.get("is_chain_head"),
                        "W_prev": P.get("W_prev"),
                        "W_near": (out or {}).get("W_near"),
                        "G": (out or {}).get("G")})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["solve_G_binary"] = _spy_sgb

    # ── 包裹 `_lot_gate`（🔑 工項二：分項重建 ＋ 多邊形甲之取得）────────────
    _o_lg = ns["_lot_gate"]
    SIG_L = inspect.signature(_o_lg)

    def _spy_lg(*a, **kw):
        rec = {}
        try:
            ba = SIG_L.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            ctx = P.get("blk_ctx") or {}
            side = str(P.get("chain_side") or "")
            res = P.get("res") or {}
            tp = P.get("tp") or {}
            cp = (ctx.get("corner_range_polys") or {}).get(side)
            sp = (ctx.get("side_pts") or {}).get(side)
            sm = (ctx.get("side_mid") or {}).get(side)
            bp = list(ctx.get("baseline_pts") or [])
            coords = list(res.get("cut_coords") or [])
            # 🔒 `_miss` 之重建 ＝ `app.py` 內該列表之**逐字同序**
            miss = [n for n, v in (("corner_range_poly", cp), ("side_pts", sp),
                                   ("side_mid", sm), ("front_p1", ctx.get("front_p1")),
                                   ("front_p2", ctx.get("front_p2")),
                                   ("alloc_dir", ctx.get("alloc_dir")),
                                   ("block_centroid", ctx.get("block_centroid")))
                    if v is None]
            if len(bp) < 2:
                miss.append("baseline_pts")
            if len(coords) < 3:
                miss.append("res.cut_coords")
            c1 = bool(P.get("is_second_after_corner"))
            c2 = bool((ctx.get("has_side") or {}).get(side))
            rec = {"blk": ctx.get("blk_label"), "side": side,
                   "id": tp.get("暫編地號"),
                   "is_corner_first": bool(P.get("is_corner_first")),
                   "c1_is_second_after_corner": c1,
                   "c2_has_side": c2,
                   "c3_miss": miss, "c3_ok": (not miss),
                   "n_cut_coords": len(coords), "n_baseline_pts": len(bp),
                   "cp_is_none": cp is None, "cp": cp,
                   "predict_gate1": bool(c1 and c2 and (not miss)),
                   "G": _f(res.get("G")),
                   "range_area_ctx": _f((ctx.get("corner_range_areas") or {}).get(side))}
        except Exception as e:                                   # noqa: BLE001
            rec = {"blk": "🔴bind:%r" % (e,), "side": None, "predict_gate1": False}
        out = _o_lg(*a, **kw)
        try:
            rec["驗_B藍影"] = (out or {}).get("驗_B藍影")
            rec["驗_不可判輸入"] = (out or {}).get("驗_不可判輸入")
            rec["驗_宗序"] = (out or {}).get("驗_宗序")
        except Exception:                                        # noqa: BLE001
            pass
        LG.append(rec)
        return out

    ns["_lot_gate"] = _spy_lg

    # ── 包裹 `_k923_gate1` ＋ `_blue_shadow_tri`（承 `-286`）────────────────
    _o_g1 = ns["_k923_gate1"]
    SIG_G = inspect.signature(_o_g1)

    def _spy_g1(*a, **kw):
        out = _o_g1(*a, **kw)
        try:
            ba = SIG_G.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            c = _climb(["_label", "_side", "blk_label", "chain_side"])
            G1.append({"label": c.get("_label"), "blk": c.get("blk_label"),
                       "side": (c.get("_side") or c.get("chain_side")),
                       "G": P.get("G"), "blue_area": P.get("blue_area"),
                       "ok": (out or (None, None))[0]})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["_k923_gate1"] = _spy_g1

    _o_bl = ns["_blue_shadow_tri"]

    def _spy_bl(*a, **kw):
        out = _o_bl(*a, **kw)
        try:
            BLUE.append({"label": kw.get("_label"), "side": kw.get("_side"),
                         "blue_area": (out or {}).get("blue_area")})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["_blue_shadow_tri"] = _spy_bl

    # ── 驅動（與 `-286`／`-281` 同源）─────────────────────────────────────
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    n_rng0, n_buf0, n_sgb0 = len(RNG), len(BUF), len(SGB)
    err, g_rows = None, []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = list((_sg or {}).get("g_rows") or [])
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
        g_rows = list((getattr(e, "partial", None) or {}).get("g_rows") or [])
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"RNG": RNG, "BUF": BUF, "SGB": SGB, "G1": G1, "BLUE": BLUE, "LG": LG,
            "n_rng0": n_rng0, "n_buf0": n_buf0, "n_sgb0": n_sgb0,
            "fo": fo_tab, "err": err, "g_rows": g_rows, "ns": ns}


def _pick(recs, blk, side):
    """自紀錄中取該 (街廓, 側) 之**最末**一筆（⛔ 逕取首命中·坑 `bi`）。"""
    out = [r for r in recs
           if r.get("side") == side and blk in str(r.get("label") or "")]
    return (out[-1], len(out)) if out else (None, 0)


def analyse(sb, d):
    from shapely.geometry import Polygon as SPoly
    import shapely

    ns = d["ns"]
    rw = ns["rw_from_width"]
    _block_strip = ns["_block_strip"]
    import numpy as np

    say("")
    say("=" * W)
    say("【SB ＝ %s m·態甲】`_build_corner_range_v3` %d 次（`run_step_g` 段 %d）／"
        "`_corner_buffer_S` %d 次（段內 %d）／`_lot_gate` %d 次／`_k923_gate1` %d 次"
        % (repr(sb), len(d["RNG"]), len(d["RNG"]) - d["n_rng0"],
           len(d["BUF"]), len(d["BUF"]) - d["n_buf0"], len(d["LG"]), len(d["G1"])))
    say("　`run_step_g` 之終局 ＝ %s" % (d["err"] or "（未拋）"))
    say("　`g_rows` ＝ %d 列（拋出時取 `e.partial`）／`shapely` ＝ %s／`GEOS` ＝ %s"
        % (len(d["g_rows"]), shapely.__version__,
           getattr(shapely, "geos_version_string", "?")))
    say("=" * W)

    say("🔒 **`forced` 側之全部成員（當場重量·⛔ 轉引）**　框 ＝ "
        "`fake_st.session_state['f3L_forced_offset']`")
    cells = []
    for b in BLKS:
        L, R = d["fo"][b]
        say("   %s ⇒ left_forced_offset ＝ %-5s ／ right_forced_offset ＝ %-5s" % (b, L, R))
        if L:
            cells.append((b, "left"))
        if R:
            cells.append((b, "right"))
    say("   ⇒ **`forced` 側 ＝ %d 格**：%s" % (len(cells), cells))

    rows = []
    for (blk, side) in cells:
        r, nr = _pick(d["RNG"], blk, side)
        bu, nb = _pick(d["BUF"], blk, side)
        say("")
        say("═" * W)
        say("── 格 `%s/%s@%sm` ── `_build_corner_range_v3` 命中 %d 筆／"
            "`_corner_buffer_S` 命中 %d 筆（皆取**最末**·坑 `bi`）"
            % (blk, side, repr(sb), nr, nb))
        say("═" * W)
        if r is None or bu is None:
            red("格 `%s/%s`：受詞缺（rng=%s／buf=%s）⇒ **loud**·⛔ 以空集充綠"
                % (blk, side, r is not None, bu is not None))
            continue
        lo = r["loc"]
        need = ("S1_perp", "S1_par", "_sin_t", "sux", "suy", "dx", "dy", "F1", "S1")
        miss = [k for k in need if k not in lo]
        if miss:
            red("格 `%s/%s`：區域值缺 %s ⇒ **自我驗證閘 (i) 不過** ⇒ 器紅" % (blk, side, miss))
            continue
        S1p = _f(lo["S1_perp"])
        resid = abs(_f(lo["S1_par"]) * _f(lo["_sin_t"]) - S1p)
        say("🔒 **自我驗證閘 (i)**（碼面閉式回代）`|S1_par·sinθ − S1_perp|` ＝ %r（須 ≤ 1e-9）⇒ %s"
            % (resid, "✅" if resid <= 1e-9 else "🔴"))
        if resid > 1e-9:
            red("格 `%s/%s`：自我驗證閘 (i) 不過 ⇒ ⛔ 據以下任何結論" % (blk, side))
            continue

        # ── 自我驗證閘 (ii)：多邊形甲 ＝ 碼面之 `corner_range_polys[_side]` ──
        lgs = [x for x in d["LG"] if x.get("blk") == blk and x.get("side") == side]
        cp = next((x["cp"] for x in lgs if x.get("cp") is not None), None)
        say("🔒 **自我驗證閘 (ii)**　`_lot_gate` 於本格 %d 筆；"
            "`blk_ctx['corner_range_polys'][%r]` `is` `_build_corner_range_v3` 之回傳 ⇒ **%s**"
            % (len(lgs), side, (cp is r["poly"]) if cp is not None else "（無 `_lot_gate` 筆·取回傳物件）"))
        A = cp if cp is not None else r["poly"]
        if cp is not None and cp is not r["poly"]:
            red("格 `%s/%s`：多邊形甲之二源**非同一物** ⇒ 器紅（⛔ 另建第二份之戒）" % (blk, side))
            continue

        # ── 款 1：多邊形甲 ────────────────────────────────────────────────
        say("")
        say("**款 `1`　多邊形甲 ＝ `corner_range_polys[%r]`（規定範圍）**" % side)
        say("   `setback` ＝ %r ／ `min_width` ＝ %r ／ `S1_perp` ＝ %r"
            % (_f(r.get("setback")), _f(r.get("min_width")), S1p))
        say("   面積 ＝ **%r** ／ 外環頂點 %d 點（`repr` 全位·⛔ 捨入）："
            % (float(A.area), len(_ext_coords(A))))
        for i, c in enumerate(_ext_coords(A)):
            say("      甲[%d] ＝ (%r, %r)" % (i, c[0], c[1]))

        # ── 款 2：多邊形乙（以碼面 `_band_area` 之逐字還原式）──────────────
        s_min = _f(bu["loc"].get("s_min"))
        s_max = _f(bu["loc"].get("s_max"))
        _lo_ = _f(bu["loc"].get("_lo"))
        buf = bu["buf"]
        _d_ = np.asarray(bu["d_hat"], dtype=float)
        a_, b_ = ((_lo_, float(buf)) if bu["side"] == "left"
                  else (s_max - float(buf), s_max))
        w_ = b_ - a_
        bp_ = np.asarray(bu["front_p1"], dtype=float) + a_ * _d_
        B, B_area = _block_strip(bu["block_poly"], bu["d_hat"], bp_, w_,
                                 allocation_dir=bu["allocation_dir"])
        say("")
        say("**款 `2`　多邊形乙 ＝ `buf` 帶（`s ∈ [max(s_min,0), buf]`）**")
        say("   還原式（逐字 ＝ `_corner_buffer_S._band_area`）：")
        say("      a, b = (_lo, float(buf)) if side == 'left' else (s_max - float(buf), s_max)")
        say("      w = b - a ；bp = front_p1 + a * d̂ ；"
            "_block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)")
        say("   `s_min` ＝ %r ／ `s_max` ＝ %r ／ `_lo` ＝ %r ／ `buf` ＝ %r"
            % (s_min, s_max, _lo_, buf))
        say("   ⇒ `a` ＝ %r ／ `b` ＝ %r ／ `w` ＝ %r ／ `bp` ＝ (%r, %r)"
            % (a_, b_, w_, float(bp_[0]), float(bp_[1])))
        say("   面積（`_block_strip` 之第二回傳）＝ **%r** ／ `.area` ＝ %r"
            % (float(B_area), float(B.area) if B is not None else None))
        if B is None:
            red("格 `%s/%s`：多邊形乙為 `None` ⇒ **loud**" % (blk, side))
            continue
        say("   外環頂點 %d 點：" % len(_ext_coords(B)))
        for i, c in enumerate(_ext_coords(B)):
            say("      乙[%d] ＝ (%r, %r)" % (i, c[0], c[1]))

        # ── 款 3：面積差 vs tol ──────────────────────────────────────────
        tol = _f(bu.get("tol"))
        dA = abs(float(A.area) - float(B.area))
        say("")
        say("**款 `3`　二者之面積差**")
        say("   `tol` 之來源（逐字）＝ `_corner_buffer_S(…, tol=0.01, _label='')` 之**預設值**；"
            "本格之實際繫結值 ＝ **%r**（`inspect` 綁定所得·⛔ 憑記憶）" % tol)
        say("   `|A甲 − A乙|` ＝ **%r**（`A甲` ＝ %r ／ `A乙` ＝ %r）⇒ %s"
            % (dA, float(A.area), float(B.area),
               "✅ ≤ tol" if (tol is not None and dA <= tol) else "🔴 **逾 tol** ⇒ loud"))
        say("   （併記：`range_area` 實參 ＝ %r ／ `|range_area − A甲|` ＝ %r）"
            % (_f(bu.get("range_area")), abs(_f(bu.get("range_area")) - float(A.area))))
        if tol is None or dA > tol:
            red("格 `%s/%s`：款 `3` 面積差逾 `tol` ⇒ **loud**·⛔ 逕續" % (blk, side))

        # ── 款 4：對稱差 ────────────────────────────────────────────────
        AB = A.difference(B)
        BA = B.difference(A)
        SD = A.symmetric_difference(B)
        say("")
        say("**款 `4`　對稱差之面積（＝「位置錯開了多少地」）**")
        say("   幾何庫 ＝ `shapely` **%s**（`GEOS` %s）"
            % (shapely.__version__, getattr(shapely, "geos_version_string", "?")))
        say("   `(甲∖乙)` ＝ **%r** ㎡　（幾何型別 %s）" % (float(AB.area), AB.geom_type))
        say("   `(乙∖甲)` ＝ **%r** ㎡　（幾何型別 %s）" % (float(BA.area), BA.geom_type))
        say("   `對稱差`  ＝ **%r** ㎡　（幾何型別 %s）" % (float(SD.area), SD.geom_type))
        say("   自洽驗算：`(甲∖乙) + (乙∖甲) − 對稱差` ＝ %r"
            % (float(AB.area) + float(BA.area) - float(SD.area)))
        say("   併記：`甲∩乙` ＝ %r ㎡ ／ `甲∪乙` ＝ %r ㎡"
            % (float(A.intersection(B).area), float(A.union(B).area)))

        # ── 款 5：最大偏離距離 ──────────────────────────────────────────
        m_ab = _max_vert_dist(A, B)
        m_ba = _max_vert_dist(B, A)
        say("")
        say("**款 `5`　對稱差之最大偏離距離**（有向·離散·母體 ＝ 外環頂點）")
        say("   甲之頂點 → 乙之邊界　最大 ＝ **%r** m" % m_ab)
        say("   乙之頂點 → 甲之邊界　最大 ＝ **%r** m" % m_ba)
        say("   （併記 `shapely.hausdorff_distance(甲, 乙)` ＝ %r）"
            % float(A.hausdorff_distance(B)))
        say("   前批同族之實測出處 ＝ `verify/out/WG9286R_twolines.log`【倉】")

        # ── 款 6：負擔率 ────────────────────────────────────────────────
        su = _unit((lo["sux"], lo["suy"]))
        ad = _unit(bu["allocation_dir"])
        dh = _unit((lo["dx"], lo["dy"]))
        F1 = (_f(lo["F1"][0]), _f(lo["F1"][1]))
        S1 = (_f(lo["S1"][0]), _f(lo["S1"][1]))
        bpn = r["baseline_pts"]
        bdir = _unit((_f(bpn[1][0]) - _f(bpn[0][0]), _f(bpn[1][1]) - _f(bpn[0][1])))
        bpt0 = (_f(bpn[0][0]), _f(bpn[0][1]))
        fp1 = (_f(bu["front_p1"][0]), _f(bu["front_p1"][1]))
        dhb = _unit(bu["d_hat"])
        s_star = (buf if bu["side"] == "left" else s_max - buf)
        Bp = (fp1[0] + s_star * dhb[0], fp1[1] + s_star * dhb[1])
        B_f = _line_x(Bp, ad, F1, dh)
        B_b = _line_x(Bp, ad, bpt0, bdir)
        d_f = _dist_pt_line(B_f, S1, su) if B_f else None
        d_b = _dist_pt_line(B_b, S1, su) if B_b else None
        heads = [x for x in d["SGB"][d["n_sgb0"]:]
                 if x["blk"] == blk and x["side"] == side
                 and (bool(x["is_corner"]) or bool(x["is_chain_head"]))]
        w0 = _f(heads[-1]["W_near"]) if heads else None
        say("")
        say("**款 `6`　負擔率**（純函式求值·⛔ 重跑分配·一律 `ns['rw_from_width']`·⛔ 器內另算）")
        say("   | 輸入 | **來源（逐格具名）** | 值 (m) | `R(·)` (%) |")
        say("   |---|---|---|---|")
        tab = [
            ("W_0", "`solve_G_binary` 鏈頭筆之回傳 `W_near`（碼面實際所用）", w0),
            ("buf線垂距@∩FRONT", "`buf` 線（錨 `front_p1 + s*·d̂`·向 `allocation_dir`）"
                                 "與 FRONT∞ 之交點 → SIDELINE 之垂距", d_f),
            ("buf線垂距@∩BASELINE", "同上·與 BASELINE∞ 之交點 → SIDELINE 之垂距", d_b),
            ("S1_perp", "`_build_corner_range_v3` 之區域值（規定範圍遠側界之垂距）", S1p),
        ]
        vals = {}
        for k, src, v in tab:
            rv_ = None if v is None else float(rw(float(v)))
            vals[k] = rv_
            say("   | `%s` | %s | %r | **%r** |" % (k, src, v, rv_))
        for k in ("W_0", "buf線垂距@∩FRONT", "buf線垂距@∩BASELINE"):
            if vals.get(k) is not None and vals.get("S1_perp") is not None:
                say("   ⇒ `R(%s) − R(S1_perp)` ＝ **%r** 個百分點" % (k, vals[k] - vals["S1_perp"]))
        say("   （併記：`|cos|`（遠側界向 vs `allocation_dir`）＝ %r ⇒ 二線**⛔ 平行**）"
            % abs(su[0] * ad[0] + su[1] * ad[1]))

        # ── 款 7：抵費地面積 ／ 第 2 宗 ──────────────────────────────────
        gr = [x for x in d["g_rows"] if x.get("所屬街廓") == blk]
        side_rows = [x for x in gr if x.get("推進側別") == side]
        off_rows = [x for x in gr if x.get("推進側別") == "抵費地"]
        say("")
        say("**款 `7`　該側之抵費地面積與第 2 宗**")
        say("   `range_area`（`_corner_buffer_S` 實參）＝ **%r** ㎡" % _f(bu.get("range_area")))
        say("   🔒 **「第 2 宗」之識別規則（具名·⛔ 推定）** ＝ 該側**強制抵費地為第 1 宗**"
            "（其 `推進側別` 欄為 `'抵費地'`·⛔ 該側之側標）⇒ **第 2 宗 ＝ 該側 `g_rows` 之首列**"
            "（＝ `is_chain_head` 之宗）。")
        if side_rows:
            r2 = side_rows[0]
            say("   ⇒ **第 2 宗之暫編地號 ＝ `%s`** ／ `G(㎡)` ＝ **%r** ／ `W(m)` ＝ %r ／"
                " `Rw(%%)` ＝ %r ／ `負擔比率` ＝ %r"
                % (r2.get("暫編地號"), r2.get("G(㎡)"), r2.get("W(m)"),
                   r2.get("Rw(%)"), r2.get("負擔比率")))
        else:
            say("   🟡 該側 `g_rows` **無列** ⇒ 具名為「不可得」（⛔ 以空集充綠）")
        say("   該側 `g_rows` 全列（序 ＝ 產生序）：")
        for i, x in enumerate(side_rows):
            say("      [%d] %s ｜G ＝ %r ｜W ＝ %r ｜Rw ＝ %r ｜街角地 ＝ %s"
                % (i, x.get("暫編地號"), x.get("G(㎡)"), x.get("W(m)"),
                   x.get("Rw(%)"), x.get("街角地")))
        say("   該街廓之 `推進側別=='抵費地'` 列：%s"
            % ([(x.get("暫編地號"), x.get("幾何面積(㎡)")) for x in off_rows] or "（無）"))

        rows.append({"sb": sb, "blk": blk, "side": side, "A": A, "B": B,
                     "sd": float(SD.area), "ab": float(AB.area), "ba": float(BA.area)})
    return rows


def item2(sb, d):
    """`§四` 工項二：藍影於各格之求值次數與其**分項**真值。"""
    say("")
    say("=" * W)
    say("【`§四` 工項二·SB ＝ %s m】`_k923_gate1` 之呼叫端與守衛分項" % repr(sb))
    say("=" * W)
    cells = {}
    for x in d["LG"]:
        cells.setdefault((x.get("blk"), x.get("side")), []).append(x)
    say("   `_lot_gate` 之筆數 ＝ %d／`_k923_gate1` ＝ %d／`_blue_shadow_tri` ＝ %d"
        % (len(d["LG"]), len(d["G1"]), len(d["BLUE"])))
    out = []
    for (blk, side) in sorted(cells, key=lambda t: (str(t[0]), str(t[1]))):
        recs = cells[(blk, side)]
        pred = sum(1 for x in recs if x.get("predict_gate1"))
        act = sum(1 for x in d["G1"]
                  if (x.get("blk") == blk or blk in str(x.get("label") or ""))
                  and x.get("side") == side)
        out.append((blk, side, pred, act, recs))
    for (blk, side, pred, act, recs) in out:
        say("")
        say("── 格 `%s/%s@%sm` ── `_lot_gate` %d 筆／**預測** `_k923_gate1` %d 次／"
            "**實際** %d 次 ⇒ 自我驗證閘 (iii) %s"
            % (blk, side, repr(sb), len(recs), pred, act,
               "✅" if pred == act else "🔴 **不符**"))
        if pred != act:
            red("格 `%s/%s@%s`：分項重建**預測不中** ⇒ 器紅（⛔ 據以下結論）"
                % (blk, side, repr(sb)))
        for i, x in enumerate(recs):
            say("   [%d] `%s`｜`驗_宗序` ＝ %s｜**分項**： "
                "`is_second_after_corner` ＝ %-5s ∧ `has_side[%r]` ＝ %-5s ∧ `_miss == []` ＝ %-5s"
                % (i, x.get("id"), x.get("驗_宗序"),
                   x.get("c1_is_second_after_corner"), side, x.get("c2_has_side"),
                   x.get("c3_ok")))
            say("       `_miss` ＝ %s｜`len(cut_coords)` ＝ %s｜`len(baseline_pts)` ＝ %s"
                "｜`驗_B藍影` ＝ %r｜`驗_不可判輸入` ＝ %r"
                % (x.get("c3_miss"), x.get("n_cut_coords"), x.get("n_baseline_pts"),
                   x.get("驗_B藍影"), x.get("驗_不可判輸入")))
    return out


def main():
    say("=" * W)
    say("【`W-G.9-287` `§三`／`§四`】二線分歧之**土地後果** ／ 藍影未求值之成因"
        " —— 🛑 **純量測·出艙即止**")
    say("=" * W)
    say("🔒 `_k923_gate1` 之**唯一呼叫端**（字樣錨·唯一性已於報告內具名）＝ `app.py` 之"
        " `_lot_gate` 內；其守衛逐字 ＝")
    say("      if is_second_after_corner and bool((_ctx.get('has_side') or {}).get(_side)):")
    say("      …  _miss = [名 for 名, 值 in ((corner_range_poly, _cp), (side_pts, _sp),"
        " (side_mid, _sm), (front_p1), (front_p2), (alloc_dir), (block_centroid)) if 值 is None]")
    say("      …  if len(_bp) < 2: _miss.append('baseline_pts')；"
        "if len(_coords) < 3: _miss.append('res.cut_coords')")
    say("      …  if _miss: _B = None  else: try: _bl = _blue_shadow_tri(...); "
        "_B, _Bd = _k923_gate1(...)")

    allrows, all2 = [], []
    for sb in SBS:
        d = drive(sb)
        allrows += analyse(sb, d)
        all2 += item2(sb, d)

    say("")
    say("=" * W)
    say("【判別力三造（`§三` 款 `8`）】")
    say("=" * W)
    say("   `(1)` [必命中] `forced` 側之鏈頭格數 ＝ **%d**（須 ≥ 1）⇒ %s"
        % (len(allrows), "✅" if allrows else "🔴 **loud**·⛔ 以空集充綠"))
    if not allrows:
        red("判別力造 `(1)` 不成立 ⇒ 器紅、停")
    for r in allrows:
        ok = r["sd"] > 0.0
        say("   `(2)` [必非零] `%s/%s@%s` 之對稱差面積 ＝ %r ⇒ %s"
            % (r["blk"], r["side"], repr(r["sb"]), r["sd"],
               "✅" if ok else "🔴 **與前批之「⛔ 平行」相斥 ⇒ 器紅、停**"))
        if not ok:
            red("判別力造 `(2)` 於 `%s/%s@%s` 不成立" % (r["blk"], r["side"], repr(r["sb"])))
    # ── 造 `(3)`：[必為零]（🔒 **先自證其可滿足**·單 `§零` 之新附款）──────────
    say("   `(3)` [必為零] **多邊形甲與其自身**之對稱差")
    say("        🔒 **可滿足性之先證**：`X.symmetric_difference(X)` 於 GEOS 之疊合"
        "回傳**空幾何**，其 `.area` ＝ `0.0` 係**精確**（⛔ 浮點餘裕）——"
        "⛔ 同 `-286` 之「一般向量正規化」型（該型於 IEEE754 下結構上不可滿足）。")
    for r in allrows:
        z = float(r["A"].symmetric_difference(r["A"]).area)
        say("        `%s/%s@%s`：甲⊖甲 ＝ **%r** ⇒ %s"
            % (r["blk"], r["side"], repr(r["sb"]), z, "✅" if z == 0.0 else "🔴"))
        if z != 0.0:
            red("判別力造 `(3)` 於 `%s/%s@%s` 不成立" % (r["blk"], r["side"], repr(r["sb"])))
    if allrows:
        r0 = allrows[0]
        nz = float(r0["A"].symmetric_difference(r0["B"]).area)
        say("   `(3')` [必非零·證 `(3)` ⛔ 恆為零] 同一運算子施於**甲與乙** ＝ **%r**（須 `> 0`）⇒ %s"
            % (nz, "✅" if nz > 0.0 else "🔴"))
        if not (nz > 0.0):
            red("判別力造 `(3')` 不成立 ⇒ `(3)` 恆為零、無鑑別力")

    say("")
    say("=" * W)
    say("【判別力二造（`§四` 款 `4`）】")
    say("=" * W)
    r2 = [t for t in all2 if t[0] == "R2" and t[1] == "left"]
    n_r2 = sum(t[3] for t in r2)
    say("   `(1)` [必非零] `R2/left` 之 `_k923_gate1` 求值次數（二情境合計）＝ **%d**（須 > 0）⇒ %s"
        % (n_r2, "✅" if n_r2 > 0 else "🔴 器無效"))
    if not (n_r2 > 0):
        red("`§四` 判別力造 `(1)` 不成立 ⇒ 器紅")
    _fake_blk = "R" + str(sum(ord(c) for c in "wg9287") % 3 + 7)   # 執行期組出·字面⛔ 出艙
    n_fake = sum(t[3] for t in all2 if t[0] == _fake_blk)
    say("   `(2)` [必為零] 一**執行期組出**之人造街廓（字面⛔ 出艙·`GB-147`）之求值次數 ＝ **%d**"
        "（須 `0`）⇒ %s" % (n_fake, "✅" if n_fake == 0 else "🔴"))
    if n_fake != 0:
        red("`§四` 判別力造 `(2)` 不成立")

    say("")
    say("🛑 **出艙即止**：⛔ 判碼面是否違反任何裁、⛔ 判藍影為缺陷、⛔ 鑄 `GB`、"
        "⛔ 提修法主張、⛔ 呈 KL。")
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
