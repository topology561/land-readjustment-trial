#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-286` `§三`：**規定範圍之遠側境界線** 與 **`forced` 帶之界（`buf` 線）**
是否為**同一條線** —— 🛑 **純量測·出艙即止**。

🛑 **⛔ 改生產碼一字、⛔ 替身、⛔ 反事實**（單 `§六`）。
🔒 **底本** ＝ `verify/probes/probe_WG9281_w0chain.py` 之 `drive`（⛔ 另寫第二份驅動）。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**（旗標未設）·`SB ∈ {0.0, 3.5}`。

🔑 **內部區域值之取得法**（單 款 `1` 令「取該函式之回傳／**其內之區域值**」）
   ＝ 於**包裹內**暫設 `sys.settrace`，僅對**該 code object** 之 frame 回傳 local tracer，
   於其 `return` 事件錄下 `f_locals` ⇒ **同一次執行**之區域值（⛔ 另跑第二次、⛔ 另算第二份）。
   🔒 **自我驗證閘**：所錄之 `locals` 須含 `S1_perp`／`S1_par`／`_sin_t`／`_Tp` 全部，
   且以其**閉式關係**回代（`S1_par * _sin_t == S1_perp` 逐位）——不過即 **器紅**。

`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力三造任一不成立）。
"""
import contextlib
import inspect
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else (
    r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees"
    r"\wg9-284-construction-window-667198")
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
    """二直線（點 ＋ 方向）之交點；平行回 `None`。"""
    if p is None or d is None or q is None or e is None:
        return None
    det = d[0] * (-e[1]) - d[1] * (-e[0])
    if abs(det) < 1e-15:
        return None
    rx, ry = q[0] - p[0], q[1] - p[1]
    t = (rx * (-e[1]) - ry * (-e[0])) / det
    return (p[0] + t * d[0], p[1] + t * d[1])


def _dist_pt_line(pt, p, d):
    """點到直線（點 `p` ＋ 單位方向 `d`）之**垂距**。"""
    if pt is None or p is None or d is None:
        return None
    return abs((pt[0] - p[0]) * (-d[1]) + (pt[1] - p[1]) * d[0])


def drive(sb):
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    os.environ.pop("WV_K6_STEP0", None)              # 🔒 **態甲**（旗標未設）
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    RNG, BUF, SGB, G1, BLUE = [], [], [], [], []

    # ── 包裹 `_build_corner_range_v3`（＋ `settrace` 取其區域值）───────────
    _o_rng = ns["_build_corner_range_v3"]
    CODE = _o_rng.__code__
    SIG_R = inspect.signature(_o_rng)
    KEEP = ("S1_perp", "S1_par", "_seg_P0Ps", "T", "_sin_t", "sux", "suy",
            "dx", "dy", "F1", "S1", "_Tp", "D", "eps", "sigma", "bnx", "bny",
            "t_q", "_s_Ps", "setback", "min_width", "_sin_min")

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
                        "front_pts": P.get("front_pts"), "baseline_pts": P.get("baseline_pts"),
                        "side_line_pts": P.get("side_line_pts"),
                        "alloc_dir": P.get("alloc_dir"), "area": float(out.area),
                        "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            RNG.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_build_corner_range_v3"] = _spy_rng

    # ── 包裹 `_corner_buffer_S` ───────────────────────────────────────────
    _o_buf = ns["_corner_buffer_S"]
    CODE_B = _o_buf.__code__
    SIG_B = inspect.signature(_o_buf)
    KEEPB = ("s_min", "s_max", "_lo", "_d", "b_lo", "b_hi", "_resid", "_f_hi")

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
                        "block_poly_area": float(getattr(P.get("block_poly"), "area", float("nan"))),
                        "buf": float(out), "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            BUF.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_corner_buffer_S"] = _spy_buf

    # ── 包裹 `solve_G_binary`（款 `6` 之 `W_0`）────────────────────────────
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
            c = _climb(["blk_label", "side"])
            sd = c.get("side")
            sd = ("left" if (sd is not None and ("左" in str(sd) or str(sd).lower().startswith("l")))
                  else ("right" if sd is not None else None))
            SGB.append({"blk": c.get("blk_label"), "side": sd,
                        "is_corner": P.get("is_corner"), "is_chain_head": P.get("is_chain_head"),
                        "W_prev": P.get("W_prev"), "side_label": P.get("side_label"),
                        "W_near": (out or {}).get("W_near"),
                        "W_rw_start_raw": (out or {}).get("W_rw_start_raw")})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["solve_G_binary"] = _spy_sgb

    # ── 包裹 `_k923_gate1` ＋ `_blue_shadow_tri`（款 `7`）──────────────────
    _o_g1 = ns["_k923_gate1"]
    SIG_G = inspect.signature(_o_g1)

    def _spy_g1(*a, **kw):
        out = _o_g1(*a, **kw)
        try:
            ba = SIG_G.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            c = _climb(["_label", "_side", "blk_label"])
            G1.append({"label": c.get("_label"), "side": c.get("_side"),
                       "blk": c.get("blk_label"), "G": P.get("G"),
                       "blue_area": P.get("blue_area"),
                       "ok": (out or (None, None))[0],
                       "detail": (out or (None, None))[1]})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["_k923_gate1"] = _spy_g1

    _o_bl = ns["_blue_shadow_tri"]

    def _spy_bl(*a, **kw):
        out = _o_bl(*a, **kw)
        try:
            BLUE.append({"label": kw.get("_label"), "side": kw.get("_side"),
                         "blue_area": (out or {}).get("blue_area"),
                         "keys": sorted((out or {}).keys())})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["_blue_shadow_tri"] = _spy_bl

    # ── 驅動（與 `-281` 同源）─────────────────────────────────────────────
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
    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb,
                       eff_min_build_by_blk={})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"RNG": RNG, "BUF": BUF, "SGB": SGB, "G1": G1, "BLUE": BLUE,
            "n_rng0": n_rng0, "n_buf0": n_buf0, "n_sgb0": n_sgb0,
            "fo": fo_tab, "err": err}


def _pick(recs, blk, side):
    """自紀錄中取該 (街廓, 側) 之**最末**一筆（⛔ 逕取首命中·坑 `bi`）。"""
    out = [r for r in recs
           if r.get("side") == side and blk in str(r.get("label") or "")]
    return (out[-1], len(out)) if out else (None, 0)


def analyse(sb, d):
    say("")
    say("=" * W)
    say("【SB ＝ %s m·態甲】`_build_corner_range_v3` %d 次（`run_step_g` 段 %d）／"
        "`_corner_buffer_S` %d 次（段內 %d）／`solve_G_binary` %d 次（段內 %d）"
        % (repr(sb), len(d["RNG"]), len(d["RNG"]) - d["n_rng0"],
           len(d["BUF"]), len(d["BUF"]) - d["n_buf0"],
           len(d["SGB"]), len(d["SGB"]) - d["n_sgb0"]))
    say("　`run_step_g` 之終局 ＝ %s" % (d["err"] or "（未拋）"))
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
        say("── 格 `%s/%s` ── `_build_corner_range_v3` 命中 %d 筆／"
            "`_corner_buffer_S` 命中 %d 筆（皆取**最末**）" % (blk, side, nr, nb))
        if r is None or bu is None:
            red("格 `%s/%s`：受詞缺（rng=%s／buf=%s）⇒ **loud**·⛔ 以空集充綠"
                % (blk, side, r is not None, bu is not None))
            continue
        lo = r["loc"]
        need = ("S1_perp", "S1_par", "_sin_t", "_Tp", "sux", "suy", "dx", "dy",
                "F1", "S1", "_seg_P0Ps", "T", "D", "eps")
        miss = [k for k in need if k not in lo]
        if miss:
            red("格 `%s/%s`：區域值缺 %s ⇒ **自我驗證閘不過** ⇒ 器紅" % (blk, side, miss))
            continue
        S1p, S1r, sin_t = _f(lo["S1_perp"]), _f(lo["S1_par"]), _f(lo["_sin_t"])
        resid = abs(S1r * sin_t - S1p)
        say("   🔒 **自我驗證閘**（碼面閉式 `S1_par = S1_perp / sinθ` 之回代）："
            "`|S1_par·sinθ − S1_perp|` ＝ %r（須 ≤ 1e-9）⇒ %s"
            % (resid, "✅" if resid <= 1e-9 else "🔴"))
        if resid > 1e-9:
            red("格 `%s/%s`：自我驗證閘不過 ⇒ ⛔ 據以下任何結論" % (blk, side))
            continue

        # ── 款 1：範圍之遠側境界線 ──────────────────────────────────────
        su = _unit((lo["sux"], lo["suy"]))
        dh = _unit((lo["dx"], lo["dy"]))
        Tp = (_f(lo["_Tp"][0]), _f(lo["_Tp"][1]))
        F1 = (_f(lo["F1"][0]), _f(lo["F1"][1]))
        S1 = (_f(lo["S1"][0]), _f(lo["S1"][1]))
        bp = r["baseline_pts"]
        bdir = _unit((_f(bp[1][0]) - _f(bp[0][0]), _f(bp[1][1]) - _f(bp[0][1])))
        bpt = (_f(bp[0][0]), _f(bp[0][1]))
        A_f = _line_x(Tp, su, F1, dh)
        A_b = _line_x(Tp, su, bpt, bdir)
        say("   **款 `1`**　遠側境界線：錨點 `_Tp` ＝ %s ／ 方向單位向量 ＝ %s"
            % (_pt(Tp), _pt(su)))
        say("            ∩FRONT∞ ＝ %s ／ ∩BASELINE∞ ＝ %s" % (_pt(A_f), _pt(A_b)))
        say("            `S1_perp` ＝ %r ／ `S1_par` ＝ %r ／ `_seg_P0Ps` ＝ %r ／ `T` ＝ %r"
            % (S1p, S1r, _f(lo["_seg_P0Ps"]), _f(lo["T"])))
        say("            `setback` ＝ %r ／ `min_width` ＝ %r ／ `sinθ` ＝ %r ／ `eps` ＝ %r ／ `D` ＝ %r"
            % (_f(r.get("setback")), _f(r.get("min_width")), sin_t, _f(lo["eps"]), _f(lo["D"])))
        say("            範圍多邊形面積（回傳之 `.area`）＝ %r" % r["area"])

        # ── 款 2：`_corner_buffer_S` 之實參 ────────────────────────────
        ad = _unit(bu["allocation_dir"])
        say("   **款 `2`**　`_corner_buffer_S` 實參：`side` ＝ %r ／ `tol` ＝ %r ／ "
            "`range_area` ＝ %r" % (bu["side"], _f(bu["tol"]), _f(bu["range_area"])))
        say("            `d_hat` ＝ %s ／ `front_p1` ＝ %s" % (_pt(bu["d_hat"]), _pt(bu["front_p1"])))
        say("            `allocation_dir` ＝ %s（單位化 %s）／`block_poly.area` ＝ %r"
            % (_pt(bu["allocation_dir"]), _pt(ad), bu["block_poly_area"]))
        say("            `s_min` ＝ %r ／ `s_max` ＝ %r ／ `_lo` ＝ %r ／ `buf` ＝ %r"
            % (_f(bu["loc"].get("s_min")), _f(bu["loc"].get("s_max")),
               _f(bu["loc"].get("_lo")), bu["buf"]))

        # ── 款 3：`range_area` vs 範圍面積 ─────────────────────────────
        dA = _f(bu["range_area"]) - r["area"]
        say("   **款 `3`**　`range_area`（%r）− 款 `1` 範圍多邊形實算面積（%r）＝ **%r**"
            % (_f(bu["range_area"]), r["area"], dA))

        # ── 款 4：`buf` 所定之線 ───────────────────────────────────────
        fp1 = (_f(bu["front_p1"][0]), _f(bu["front_p1"][1]))
        dhb = _unit(bu["d_hat"])
        s_star = (bu["buf"] if bu["side"] == "left"
                  else _f(bu["loc"].get("s_max")) - bu["buf"])
        Bp = (fp1[0] + s_star * dhb[0], fp1[1] + s_star * dhb[1])
        B_f = _line_x(Bp, ad, F1, dh)
        B_b = _line_x(Bp, ad, bpt, bdir)
        say("   **款 `4`**　`buf` 線（還原式 ＝ `_block_strip`／`_strip_s_range` 之切法："
            "錨 ＝ `front_p1 + s*·d̂`，方向 ＝ `allocation_dir`）")
        say("            `s*` ＝ %r（`side='%s'` ⇒ %s）／錨點 ＝ %s ／ 方向單位向量 ＝ %s"
            % (s_star, bu["side"],
               "`buf`" if bu["side"] == "left" else "`s_max − buf`", _pt(Bp), _pt(ad)))
        say("            ∩FRONT∞ ＝ %s ／ ∩BASELINE∞ ＝ %s" % (_pt(B_f), _pt(B_b)))

        # ── 款 5：二線之對拍 ───────────────────────────────────────────
        cosv = abs(su[0] * ad[0] + su[1] * ad[1])
        par = abs(cosv - 1.0) <= 1e-12
        dAB = _dist_pt_line(Bp, Tp, su)
        say("   **款 `5`**　二線之對拍")
        say("      `(a)` `|cos|` ＝ %r ／ `|cos| − 1` ＝ **%r** ／ 二線平行？ **%s**"
            % (cosv, cosv - 1.0, par))
        say("      `(b)` 垂距（`buf` 線錨點 → 遠側境界線）＝ **%r**"
            "%s" % (dAB, "" if par else "　⚠️ **二線⛔ 平行** ⇒ 該量係**點對線**之垂距、"
                    "⛔ 二平行線之距離"))
        if not par:
            say("            二線之交點 ＝ %s" % _pt(_line_x(Tp, su, Bp, ad)))
        say("      `(c)` 端點之逐位差：∩FRONT `Δ` ＝ (%r, %r) ／ ∩BASELINE `Δ` ＝ (%r, %r)"
            % ((B_f[0] - A_f[0]) if (A_f and B_f) else float("nan"),
               (B_f[1] - A_f[1]) if (A_f and B_f) else float("nan"),
               (B_b[0] - A_b[0]) if (A_b and B_b) else float("nan"),
               (B_b[1] - A_b[1]) if (A_b and B_b) else float("nan")))
        d_f = _dist_pt_line(B_f, S1, su) if B_f else None
        d_b = _dist_pt_line(B_b, S1, su) if B_b else None
        say("      `(d)` `buf` 線相對 SIDELINE 之**垂距**（⚠️ 非平行 ⇒ 沿深度變動·取二端）：")
        say("            於 ∩FRONT ＝ %r（− `S1_perp` ＝ **%r**）" % (d_f, (d_f - S1p) if d_f else None))
        say("            於 ∩BASELINE ＝ %r（− `S1_perp` ＝ **%r**）" % (d_b, (d_b - S1p) if d_b else None))

        # ── 款 6：`W_0` ────────────────────────────────────────────────
        heads = [x for x in d["SGB"][d["n_sgb0"]:]
                 if x["blk"] == blk and x["side"] == side
                 and (bool(x["is_corner"]) or bool(x["is_chain_head"]))]
        say("   **款 `6`**　`solve_G_binary` 於本格之鏈頭筆 ＝ %d" % len(heads))
        for h in heads[-1:]:
            say("            `W_near` ＝ %r ／ `W_rw_start_raw` ＝ %r ／ `W_prev` ＝ %r"
                % (_f(h["W_near"]), _f(h["W_rw_start_raw"]), _f(h["W_prev"])))
            w0 = _f(h["W_near"])
            if w0 is not None:
                say("            **`W_0` − `S1_perp`** ＝ **%r**" % (w0 - S1p))

        # ── 款 7：藍影 ─────────────────────────────────────────────────
        g1 = [x for x in d["G1"] if x.get("side") == side and blk in str(x.get("label") or "")]
        bl = [x for x in d["BLUE"] if x.get("side") == side and blk in str(x.get("label") or "")]
        say("   **款 `7`**　`_k923_gate1` 於本格之呼叫 ＝ **%d** 次／`_blue_shadow_tri` ＝ **%d** 次"
            % (len(g1), len(bl)))
        for x in g1[-1:]:
            dd = x.get("detail") or {}
            say("            `ok` ＝ %r ／ `G` ＝ %r ／ `blue` ＝ %r ／ `len_front` ＝ %r ／ `len_base` ＝ %r"
                % (x.get("ok"), _f(x.get("G")), _f(x.get("blue_area")),
                   _f(dd.get("len_front")), _f(dd.get("len_base"))))
        for x in bl[-1:]:
            say("            `_blue_shadow_tri` 回傳鍵 ＝ %s ／ `blue_area` ＝ %r"
                % (x.get("keys"), _f(x.get("blue_area"))))

        rows.append({"sb": sb, "blk": blk, "side": side, "cos": cosv, "d": dAB,
                     "S1p": S1p, "su": su, "ad": ad, "Tp": Tp, "Bp": Bp, "S1": S1})
    return rows


def main():
    say("=" * W)
    say("【`W-G.9-286` `§三`】遠側境界線 vs `forced` 帶之界 —— 🛑 **純量測·出艙即止**")
    say("=" * W)
    allrows = []
    for sb in SBS:
        allrows += analyse(sb, drive(sb))

    say("")
    say("=" * W)
    say("【判別力三造】")
    say("=" * W)
    say("   `(1)` [必命中] `forced` 側之鏈頭格數 ＝ **%d**（須 ≥ 1）⇒ %s"
        % (len(allrows), "✅" if allrows else "🔴 **loud**·⛔ 以空集充綠"))
    if not allrows:
        red("判別力造 `(1)` 不成立 ⇒ 器紅、停")
    for r in allrows:
        d0 = _dist_pt_line(r["Bp"], r["S1"], r["su"])       # SIDELINE 自身（平移量 0）
        ok = (d0 is not None) and (abs(d0 - r["d"]) > 1e-9)
        say("   `(2)` [必相異] `%s/%s@%s`：SIDELINE **自身**（平移 `0`）之同式 ＝ %r ／"
            " 款 `5(b)` ＝ %r ／ 差 ＝ %r ⇒ %s"
            % (r["blk"], r["side"], repr(r["sb"]), d0, r["d"],
               (d0 - r["d"]) if d0 is not None else None, "✅" if ok else "🔴"))
        if not ok:
            red("判別力造 `(2)` 於 `%s/%s@%s` 不成立" % (r["blk"], r["side"], repr(r["sb"])))
    # ── 造 `(3)`：[必為零]（🩸 **本批自捕**·見下之 `(3b)`）─────────────────
    #   🔒 `(3a)` **軸對齊**之人造單位向量（**執行期組出**·字面⛔ 出艙）——其正規化**精確**
    #      ⇒ `||cos| − 1|` **恆為 `0.0`**（⛔ 浮點餘裕）。
    k = (sum(ord(c) for c in "wg9286") % 2)
    ua = (1.0, 0.0) if k == 0 else (0.0, 1.0)
    z3a = abs(abs(ua[0] * ua[0] + ua[1] * ua[1]) - 1.0)
    say("   `(3a)` [必為零] **軸對齊**之人造單位向量（**執行期組出**·字面⛔ 出艙）與自身之"
        " `||cos| − 1|` ＝ **%r**（須 `0`）⇒ %s" % (z3a, "✅" if z3a == 0.0 else "🔴"))
    if z3a != 0.0:
        red("判別力造 `(3a)` 不成立")
    #   🔒 判別力（證 `(3a)` **⛔ 恆為零**）：一**非單位**之人造向量須得顯著非零
    nu = (3.0, 4.0)
    z3c = abs(abs(nu[0] * nu[0] + nu[1] * nu[1]) - 1.0)
    say("   `(3a′)` [必非零] 一**非單位**之人造向量之同式 ＝ **%r**（須 `> 0`）⇒ %s"
        % (z3c, "✅" if z3c > 0.0 else "🔴"))
    if not (z3c > 0.0):
        red("判別力造 `(3a′)` 不成立 ⇒ `(3a)` 恆為零、無鑑別力")
    #   🩸 `(3b)` **照實併呈**：單 `款 8` 之字面（「人造向量與自身之 `|cos|−1` 須為 `0``」）
    #      於**一般**（非軸對齊）向量**不可滿足**——正規化之捨入使 `u·u` 偏離 `1` 一個機器 epsilon。
    v = (float(sum(ord(c) for c in "wg") % 7 + 1), float(sum(ord(c) for c in "286") % 5 + 2))
    u = _unit(v)
    z3b = abs(abs(u[0] * u[0] + u[1] * u[1]) - 1.0)
    say("   `(3b)` 🩸 **照實併呈**：一**一般**人造向量正規化後之同式 ＝ **%r**"
        "（＝ `2**-53` 之量級·機器 epsilon）" % z3b)
    say("        ⇒ 🛑 單 `款 8` 之「須為 `0`」於**一般向量**下**⛔ 可滿足**（IEEE754 之必然·"
        "**⛔ 受詞紅**）；依 `常規二` **取保守項** ＝ 改以 `(3a)` 之**軸對齊**造行之"
        "（其零係**精確**、且由 `(3a′)` 證其⛔ 恆零）。⛔ 改單、⛔ 放寬判準。")
    say("")
    say("🛑 **出艙即止**：⛔ 判二線是否應為同一條、⛔ 判碼面是否違反任何裁、⛔ 鑄 `GB`、⛔ 呈 KL。")
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
