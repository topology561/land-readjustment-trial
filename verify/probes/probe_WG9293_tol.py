#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-293` `§三`：`ns` 通道之**實查** ／ 殘差之**成因**（`tol`） —— 🛑 **出艙即止**。

🛑 **⛔ 改生產碼一字、⛔ 替身（本器之包裹一律<u>純委派</u>）、⛔ 開分支、⛔ 為達任何期值而擇 `tol`。**
🔒 **底本** ＝ `verify/probes/probe_WG9292_pathC.py` 之 `drive`（⛔ 另寫第三份驅動）。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**（旗標未設）·`SB ∈ {0.0, 3.5}`。

🔑 **款 `1`–`4`（`ns` 通道）**：以**執行期 `in` 比對**實查（⛔ AST／字樣推定）；
   `ns` 之取得 ＝ 於 `_corner_buffer_S` 之包裹內**上溯呼叫框**取其名為 `ns` 之區域（**⛔ 以假說充**），
   並與 `harvest()` 所回傳之物件以 `is` 對拍。

🔑 **款 `5`–`9`（`tol`）**：`tol` 係**實參**（簽章預設 `0.01`）⇒ 設計驗算於**探針內傳入**更緊之值，
   **⛔ 改碼一字**。其出艙一律冠 `【設計驗算·⛔ 實測】`。

🔒 **自我驗證閘（四重·任一不過即器紅 `rc = 5`）——逐閘出艙其<u>執行次數</u>**（`W-G.9-293 §零` 附款 `(a)`）
   `(i)`   `_build_corner_range_v3` 之閉式回代 `|S1_par·sinθ − S1_perp| ≤ 1e-9`。
   `(ii)`  **帶之重建**：以當場之 `allocation_dir`／`buf` 重建之帶，面積須 ＝ `range_area`（`|Δ| ≤ tol`）。
   `(iii)` **`W_0` 之重建**須與包裹所錄之 `k956_W_from_mp` 實際回傳**逐位相同**。
   `(iv)`  **`ns` 之同一性**：包裹上溯所得之 `ns` 須 `is` `harvest()` 之回傳物件。

`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力造不成立）。
用法：python verify/probes/probe_WG9293_tol.py
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
TOLS = (1e-4, 1e-6, 1e-8)
RED = [0]
_LOG = []
TAG = "【設計驗算·⛔ 實測】"
GATE_N = {"i": 0, "ii": 0, "iii": 0, "iv": 0}       # 🔒 逐閘之**執行次數**


def say(s=""):
    print(s)
    _LOG.append(s)


def red(s):
    say("🔴 " + s)
    RED[0] = 5


def _unit(v):
    if v is None:
        return None
    x, y = float(v[0]), float(v[1])
    n = math.hypot(x, y)
    return None if n <= 1e-15 else (x / n, y / n)


def _rot90(v):
    return (-float(v[1]), float(v[0]))


def _edges(g):
    if g is None or getattr(g, "is_empty", True):
        return []
    out = []
    for p in (list(g.geoms) if hasattr(g, "geoms") else [g]):
        ext = getattr(p, "exterior", None)
        if ext is None:
            continue
        cs = [(float(c[0]), float(c[1])) for c in ext.coords]
        for i in range(len(cs) - 1):
            a, b = cs[i], cs[i + 1]
            if math.hypot(b[0] - a[0], b[1] - a[1]) > 1e-9:
                out.append((a, b))
    return out


def _verts(g):
    out = []
    for e in _edges(g):
        out.append(e[0])
        out.append(e[1])
    return out


def _edir(e):
    return _unit((e[1][0] - e[0][0], e[1][1] - e[0][1]))


def _emid(e):
    return ((e[0][0] + e[1][0]) / 2.0, (e[0][1] + e[1][1]) / 2.0)


def _cos(u, v):
    if u is None or v is None:
        return None
    return abs(u[0] * v[0] + u[1] * v[1])


def _span(g, d):
    """多邊形沿單位向量 `d` 之跨距（`max − min` 之投影）。"""
    vs = _verts(g)
    if not vs:
        return None
    ps = [v[0] * d[0] + v[1] * d[1] for v in vs]
    return max(ps) - min(ps)


# ══════════════════════════════════════════════════════════════════════════════
def drive(sb):
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    os.environ.pop("WV_K6_STEP0", None)              # 🔒 **態甲**
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    RNG, BUF, K956, NSCAP = [], [], [], []

    _o_rng = ns["_build_corner_range_v3"]
    CODE = _o_rng.__code__
    SIG_R = inspect.signature(_o_rng)
    KEEP = ("S1_perp", "S1_par", "_sin_t", "sux", "suy", "_Tp")

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
                        "poly": out, "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            RNG.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_build_corner_range_v3"] = _spy_rng

    _o_buf = ns["_corner_buffer_S"]
    CODE_B = _o_buf.__code__
    SIG_B = inspect.signature(_o_buf)
    KEEPB = ("s_min", "s_max", "_lo", "b_lo", "b_hi", "_resid")

    def _climb_ns(upto=24):
        """🔒 **上溯呼叫框**取其名為 `ns` 之區域（⛔ 以「`ns` 即 `__globals__`」之舊假說充）。"""
        for dep in range(1, upto + 1):
            try:
                fr = sys._getframe(dep + 1)
            except ValueError:
                return None, None
            v = fr.f_locals.get("ns")
            if isinstance(v, dict):
                return v, "%s@%s:%d" % (fr.f_code.co_name,
                                        os.path.basename(fr.f_code.co_filename),
                                        fr.f_lineno)
        return None, None

    def _spy_buf(*a, **kw):
        cap = {}
        _ns_seen, _where = _climb_ns()

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
                        "block_poly": P.get("block_poly"), "d_hat": P.get("d_hat"),
                        "front_p1": P.get("front_p1"),
                        "allocation_dir": P.get("allocation_dir"),
                        "range_area": P.get("range_area"), "tol": P.get("tol"),
                        "buf": float(out), "loc": cap,
                        "ns_seen": _ns_seen, "ns_where": _where})
            NSCAP.append({"label": P.get("_label"), "side": P.get("side"),
                          "ns": _ns_seen, "where": _where})
        except Exception as e:                                   # noqa: BLE001
            BUF.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_corner_buffer_S"] = _spy_buf

    _o_k = ns["k956_W_from_mp"]
    SIG_K = inspect.signature(_o_k)

    def _spy_k(*a, **kw):
        out = _o_k(*a, **kw)
        try:
            ba = SIG_K.bind(*a, **kw)
            ba.apply_defaults()
            K956.append({"point": ba.arguments.get("point"), "out": float(out)})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["k956_W_from_mp"] = _spy_k

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
    err, crp = None, {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        crp = dict((_sg or {}).get("corner_range_polys") or {})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
        crp = dict((getattr(e, "partial", None) or {}).get("corner_range_polys") or {})
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"RNG": RNG, "BUF": BUF, "K956": K956, "NSCAP": NSCAP, "crp": crp,
            "fo": fo_tab, "err": err, "ns": ns, "st": fake_st,
            "ns_harvest": ns}


def _pick(recs, blk, side):
    out = [r for r in recs
           if r.get("side") == side and blk in str(r.get("label") or "")]
    return (out[-1], len(out)) if out else (None, 0)


def band_poly(ns, block_poly, d_hat, front_p1, allocation_dir, buf, side):
    """帶之構造 —— **逐字複刻** `app.py` `_corner_buffer_S._band_area`。"""
    import numpy as np
    dom = ns["_strip_s_range"](block_poly, d_hat, front_p1, allocation_dir)
    if dom is None:
        return None, None, None
    s_min, s_max = float(dom[0]), float(dom[1])
    _lo = max(s_min, 0.0)
    _d = np.asarray(d_hat, dtype=float)
    a, b = (_lo, float(buf)) if side == "left" else (s_max - float(buf), s_max)
    w = b - a
    if w <= 0:
        return None, (s_min, s_max), None
    bp = np.asarray(front_p1, dtype=float) + a * _d
    _g, _ar = ns["_block_strip"](block_poly, d_hat, bp, w, allocation_dir=allocation_dir)
    return _g, (s_min, s_max), float(_ar or 0.0)


def _sym(a, b):
    if a is None or b is None:
        return None, None, None
    ab, ba = a.difference(b), b.difference(a)
    return float(ab.area), float(ba.area), float(ab.area) + float(ba.area)


# ══════════════════════════════════════════════════════════════════════════════
def section_A(sb, d):
    """款 `1`–`4`：`ns` 通道之實查。"""
    say("")
    say("=" * W)
    say("## `§A`（`SB = %s`）　款 `1`–`4`：`ns` 通道之**實查**（🛑 執行期 `in` 比對·⛔ 靜態推定）" % repr(sb))
    say("=" * W)
    nsh = d["ns_harvest"]
    Z = "_first_corner_alloc_dir" + "_nosuch" + str(97 * 3)        # 執行期組出·字面⛔ 出艙
    say("   🔒 `harvest()` 所回傳之 `ns`：`type` ＝ `%s`／`len(ns)` ＝ **`%d`**／`id` ＝ `%s`"
        % (type(nsh).__name__, len(nsh), hex(id(nsh))))
    say("")
    say("   | `forced` 消費端（**執行期實查**） | 上溯所得之 `ns` 之出處 | `len(ns)` | `is` `harvest()` 之物件 | `'_first_corner_alloc_dir' in ns` | 對照組[必真] `'_corner_buffer_S' in ns` | 對照組[必偽] 人造名 |")
    say("   |---|---|---|---|---|---|---|")
    okA = True
    for r in d["NSCAP"]:
        nsv = r["ns"]
        if nsv is None:
            red("`%s/%s`：上溯 `24` 層**未見**名為 `ns` 之區域 dict ⇒ **loud 拒測**"
                % (r["label"], r["side"]))
            okA = False
            continue
        GATE_N["iv"] += 1
        same = nsv is nsh
        if not same:
            red("`%s/%s`：閘 `(iv)` 不過——上溯所得之 `ns` **⛔ `is`** `harvest()` 之回傳物件"
                % (r["label"], r["side"]))
            okA = False
        a = "_first_corner_alloc_dir" in nsv
        b = "_corner_buffer_S" in nsv
        c = Z in nsv
        if not b or c:
            red("`%s/%s`：款 `4` 判別力二造不成立（[必真] ＝ %s／[必偽] ＝ %s）⇒ **判器紅、停**"
                % (r["label"], r["side"], b, c))
            okA = False
        say("   | `%s`／`%s` | `%s` | `%d` | **%s** | **%s** | %s | %s |"
            % (r["label"], r["side"], r["where"], len(nsv), same, a, b, c))
    say("")
    say("   🔒 **閘 `(iv)` 之執行次數 ＝ %d**（⛔ 以 `rc = 0` 充其已跑）" % GATE_N["iv"])
    return okA


def section_B(sb, d):
    """款 `5`–`9`：殘差之成因（`tol`）。"""
    ns = d["ns"]
    crp = d["crp"]
    say("")
    say("=" * W)
    say("## `§B`（`SB = %s`）　款 `5`–`9`：殘差之**成因**（`tol`）" % repr(sb))
    say("=" * W)
    say("   `run_step_g` 之終局 ＝ %s｜`corner_range_polys` 鍵 ＝ %d 個"
        % (d["err"] or "（未拋）", len(crp)))
    grids = []
    for b in BLKS:
        L, R = d["fo"][b]
        if L:
            grids.append((b, "left"))
        if R:
            grids.append((b, "right"))
    say("   `forced` 格 ＝ **%d**（%s）" % (len(grids), "、".join("%s/%s" % g for g in grids)))
    say("")
    rows = []
    for blk, side in grids:
        say("─" * W)
        say("### `%s`／`%s`＠`SB = %s`" % (blk, side, repr(sb)))
        br, nb = _pick(d["BUF"], blk, side)
        rr, nr = _pick(d["RNG"], blk, side)
        cp = crp.get((blk, side))
        if br is None or rr is None or cp is None:
            red("`%s/%s`：紀錄不全（`BUF` %d／`RNG` %d／`cp` %s）⇒ **loud 拒測**"
                % (blk, side, nb, nr, cp is not None))
            continue
        loc = rr["loc"]
        S1_perp = float(loc["S1_perp"])
        GATE_N["i"] += 1
        g_i = abs(float(loc["S1_par"]) * float(loc["_sin_t"]) - S1_perp)
        say("  **閘 `(i)`**（第 `%d` 次執行）`|S1_par·sinθ − S1_perp|` ＝ `%r` ⇒ %s"
            % (GATE_N["i"], g_i, "✅" if g_i <= 1e-9 else "🔴"))
        if g_i > 1e-9:
            red("`%s/%s`：閘 `(i)` 不過 ⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        bp_, dh_, fp_ = br["block_poly"], br["d_hat"], br["front_p1"]
        ad1, ra, tol1, buf1 = br["allocation_dir"], float(br["range_area"]), br["tol"], br["buf"]
        blo, bhi = br["loc"].get("b_lo"), br["loc"].get("b_hi")
        resid = br["loc"].get("_resid")

        # ── 款 5：tol 之當場值與 bisect 之收斂實況 ──
        say("  **款 `5`**　`tol` 之當場值 ＝ `%r`（**⛔ 被呼叫端覆寫**·四消費端之呼叫式皆未傳 `tol`）"
            % tol1)
        say("      `bisect` 之收斂實況（包裹所錄之區域值）：`b_lo` ＝ `%r`／`b_hi` ＝ `%r`／"
            "`b_hi − b_lo` ＝ `%r`／`_resid`（＝ `|band − range|`）＝ `%r`"
            % (blo, bhi, (None if (blo is None or bhi is None) else bhi - blo), resid))

        # ── 閘 (ii) ──
        g1, dom1, ar1 = band_poly(ns, bp_, dh_, fp_, ad1, buf1, side)
        GATE_N["ii"] += 1
        ok_ii = (ar1 is not None) and abs(ar1 - ra) <= float(tol1)
        say("  **閘 `(ii)`**（第 `%d` 次執行）帶之重建：面積 `%r`／`range_area` `%r`／`|Δ|` `%r` ⇒ %s"
            % (GATE_N["ii"], ar1, ra, (None if ar1 is None else abs(ar1 - ra)),
               "✅" if ok_ii else "🔴"))
        if not ok_ii:
            red("`%s/%s`：閘 `(ii)` 不過 ⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        sm = ((d["st"].session_state.get("f3_cad_side_lines_by_side", {}) or {})
              .get(blk, {}) or {}).get(side, {}).get("mid")
        if sm is None:
            red("`%s/%s`：`side_mid` ⛔ 可達 ⇒ loud 拒測" % (blk, side))
            continue
        ad2 = ns["_first_corner_alloc_dir"](sm)

        import numpy as np

        def _w0(gs, buf, dv, mp, adir):
            dv2 = np.asarray(dv, dtype=float)
            du = dv2 / float(np.linalg.norm(dv2))
            return float(ns["k956_W_from_mp"](
                np.asarray(gs, dtype=float) + float(buf) * du, mp, adir, dv))

        # ── 閘 (iii) ──
        w0_cur = _w0(fp_, buf1, dh_, sm, ad1)
        _bp0 = np.asarray(fp_, dtype=float) + float(buf1) * (
            np.asarray(dh_, dtype=float) / float(np.linalg.norm(np.asarray(dh_, dtype=float))))
        _hit = [r for r in d["K956"]
                if float(np.max(np.abs(np.asarray(r["point"], dtype=float)[:2] - _bp0[:2]))) <= 1e-12]
        GATE_N["iii"] += 1
        if not _hit:
            say("  **閘 `(iii)`**（第 `%d` 次執行）🟡 **不可驗（loud）**——本格無對應之 `k956` 錄"
                % GATE_N["iii"])
            g_iii = None
        else:
            dv3 = min(abs(float(r["out"]) - w0_cur) for r in _hit)
            g_iii = (dv3 == 0.0)
            say("  **閘 `(iii)`**（第 `%d` 次執行）`W_0` 之重建 vs 包裹所錄：錄 %d 筆·最小差 `%r` ⇒ %s"
                % (GATE_N["iii"], len(_hit), dv3, "✅ 逐位相同" if g_iii else "🔴"))
            if not g_iii:
                red("`%s/%s`：閘 `(iii)` 不過 ⇒ 該格之 `W_0` ⛔ 出艙" % (blk, side))
                continue

        # ── 款 6：帶長度與由 tol 導出之界 ──
        cutdir = _unit(_rot90(_unit(ad2)))
        g2_ref, _, _ = band_poly(ns, bp_, dh_, fp_, ad2,
                                 ns["_corner_buffer_S"](bp_, dh_, fp_, ad2, ra, side,
                                                        tol=tol1, _label="WG9293·" + blk),
                                 side)
        span = _span(g2_ref, cutdir)
        bound = (float(tol1) / span) if span else None
        say("  **款 `6`**　帶之**跨距**（沿切向 `rot90(_first_corner_alloc_dir)`）＝ `%r` m；"
            "由 `tol` 導出之**起算殘差之界** ＝ `tol ÷ 跨距` ＝ `%r ÷ %r` ＝ **`%r`** m"
            % (span, tol1, span, bound))

        # ── 款 8：設計驗算（逐 tol）──
        say("  **款 `8`**　%s 逐 `tol` 之複算" % TAG)
        say("      | `tol` | `buf′` | 帶面積 | **對稱差** | `甲∖乙` | `乙∖甲` | `\\|W_0′ − S1_perp\\|` |")
        say("      |---|---|---|---|---|---|---|")
        per_tol = {}
        for t in (tol1,) + TOLS:
            try:
                b2 = ns["_corner_buffer_S"](bp_, dh_, fp_, ad2, ra, side,
                                            tol=t, _label="WG9293·%s·tol=%r" % (blk, t))
            except Exception as e:                               # noqa: BLE001
                say("      | `%r` | 🔴 **拋出** | — | — | — | — | %s |"
                    % (t, str(e).split("\n")[0][:60]))
                per_tol[t] = None
                continue
            gg, _, aa = band_poly(ns, bp_, dh_, fp_, ad2, b2, side)
            ab, ba, sy = _sym(gg, cp)
            w2 = _w0(fp_, b2, dh_, sm, ad2)
            say("      | `%r`%s | `%r` | `%r` | **`%r`** | `%r` | `%r` | `%r` |"
                % (t, "（＝當場值）" if t == tol1 else "", b2, aa, sy, ab, ba,
                   abs(w2 - S1_perp)))
            per_tol[t] = {"buf": b2, "sym": sy, "dw": abs(w2 - S1_perp)}

        # ── 款 7：並列 ──
        cur = per_tol.get(tol1) or {}
        d11, d1c, sym1 = _sym(g1, cp)
        d00, d0c, sym0 = _sym(cp, cp)
        say("  **款 `7`**　實測與 `tol` 之並列")
        say("      對稱差（路丙·`tol` ＝ 當場值）＝ `%r` ㎡／`tol` ＝ `%r` ㎡ ⇒ **比值** ＝ `%r`"
            % (cur.get("sym"), tol1,
               (None if not cur.get("sym") else cur["sym"] / float(tol1))))
        say("      `|W_0′ − S1_perp|` ＝ `%r` m／款 `6` 之界 ＝ `%r` m ⇒ **比值** ＝ `%r`"
            % (cur.get("dw"), bound,
               (None if (not cur.get("dw") or not bound) else cur["dw"] / bound)))
        say("      判別力：現行 `buf` 之對稱差 ＝ `%r`（[必非零]）／規定範圍與自身 ＝ `%r`（[必為零]）"
            % (sym1, sym0))
        rows.append({"sb": sb, "blk": blk, "side": side, "tol1": tol1, "span": span,
                     "bound": bound, "per_tol": per_tol, "sym1": sym1, "sym0": sym0,
                     "S1_perp": S1_perp})
        say("")
    return rows


FORCED_CONSUMERS = [("app.py", "main"),
                    ("verify/stepg_pipeline.py", "_run_step_g_impl"),
                    ("verify/wf_f1.py", "compute"),
                    ("verify/wf_f4.py", "_reshape_block")]


def section_C():
    """款 `3`：四態框（`(i)` 同一 scope／`(ii)` 模組頂層全域／**`(iv)` 經既有注入通道**／`(iii)` ⛔ 可達）。
    🛑 **靜態**——其**執行期**之實查僅 `stepg` 一端可得（見 `§A`）；餘三端於本 harness 路徑**未被執行**
       ⇒ **loud 具名為「本批⛔ 可執行期實查」**，⛔ 以靜態充執行期（`序 11` 之一般化 款 `三`）。"""
    import ast
    NAME = "_first_corner_alloc_dir"
    say("")
    say("=" * W)
    say("## `§C`　款 `3`：四態框（**靜態**·⛔ 充執行期實查）")
    say("=" * W)
    say("   | 消費端 | `(i)` scope | `(ii)` `t.body` 頂層全域 | **注入通道之名** | **`_corner_buffer_S` 之取式逐字** | **判** | 執行期實查 |")
    say("   |---|---|---|---|---|---|---|")
    for rel, fname in FORCED_CONSUMERS:
        txt = open(os.path.join(REPO, rel), encoding="utf-8").read()
        tree = ast.parse(txt)
        fn = None
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == fname:
                fn = node
                break
        if fn is None:
            red("`%s` `%s`：查無該函式 ⇒ loud 拒測" % (rel, fname))
            continue
        names = set()
        for node in ast.walk(fn):
            if isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, ast.arg):
                names.add(node.arg)
        top = set()
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                top.add(node.name)
            elif isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        top.add(t.id)
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                for al in node.names:
                    top.add(al.asname or al.name.split(".")[0])
        # `_corner_buffer_S` 之取式（AST·⛔ 文字層）
        getexpr, chan = [], None
        for node in ast.walk(fn):
            if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) \
                    and isinstance(node.slice, ast.Constant) and node.slice.value == "_corner_buffer_S":
                getexpr.append(ast.unparse(node))
                chan = node.value.id
            elif isinstance(node, ast.Name) and node.id == "_corner_buffer_S" \
                    and isinstance(getattr(node, "ctx", None), ast.Load):
                getexpr.append("_corner_buffer_S（**直呼**·模組全域）")
        # 其所在模組之頂層取式（如 stepg `:389` `_corner_buffer_S = ns["_corner_buffer_S"]`）
        if chan is None:
            for node in ast.walk(fn):
                if isinstance(node, ast.Assign) and isinstance(node.value, ast.Subscript) \
                        and isinstance(node.value.value, ast.Name) \
                        and isinstance(node.value.slice, ast.Constant) \
                        and node.value.slice.value == "_corner_buffer_S":
                    chan = node.value.value.id
        i_ = NAME in names
        ii_ = NAME in top
        iv_ = chan is not None
        v = ("✅ `(i)` 同一 scope" if i_ else
             ("🟡 `(ii)` 模組頂層全域" if ii_ else
              ("🟢 **`(iv)` 經既有注入通道**" if iv_ else "🔴 `(iii)` ⛔ 可達")))
        rt = ("✅ 已實查（`§A`：`in ns` ＝ `True`）"
              if rel.endswith("stepg_pipeline.py")
              else "🟡 **本批⛔ 可執行期實查**（該端於本 harness 路徑未被執行）")
        say("   | `%s` `%s` | %s | %s | `%s` | `%s` | %s | %s |"
            % (rel, fname, i_, ii_, chan or "—",
               "／".join(sorted(set(getexpr))[:2]) or "—", v, rt))
    Z = "_corner_buffer_S" + "_nosuch" + str(29 * 11)
    _t = ast.parse(open(os.path.join(REPO, "app.py"), encoding="utf-8").read())
    _tp = set()
    for node in _t.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            _tp.add(node.name)
    say("   🔑 **判別力二造**：[必真] `%s` 於 `app.py` 頂層全域 ＝ **%s**／"
        "[必偽] 一人造名（執行期組出·字面⛔ 出艙）＝ **%s** ⇒ %s"
        % (NAME, NAME in _tp, Z in _tp,
           "✅ 器非紅" if (NAME in _tp and Z not in _tp) else "🔴 器紅"))
    say("")


def main():
    section_C()
    okA_all, allrows = True, []
    for sb in SBS:
        d = drive(sb)
        okA_all = section_A(sb, d) and okA_all
        allrows += section_B(sb, d)

    say("=" * W)
    say("## 款 `9`　判別力三造之判")
    say("=" * W)
    say("   | 造 | 判準 | 實測 | 判 |")
    say("   |---|---|---|---|")
    pairs = []
    for r in allrows:
        a = (r["per_tol"].get(r["tol1"]) or {}).get("sym")
        b = (r["per_tol"].get(1e-8) or {}).get("sym")
        pairs.append((r["blk"] + "/" + r["side"] + "@" + repr(r["sb"]), a, b,
                      (a is not None and b is not None and a != b)))
    ok1 = all(p[3] for p in pairs) and pairs
    say("   | [必相異] | `tol = 0.01` 與 `tol = 1e-8` 之對稱差須**相異**（證款 `8` 非恆值） | %s | %s |"
        % ("／".join("%s: %r vs %r ⇒ %s" % p for p in pairs), "✅" if ok1 else "🔴"))
    ok2 = all((r["sym1"] or 0) > 0 for r in allrows) and allrows
    say("   | [必非零] | 現行 `buf` 之對稱差須 `> 0` | %s | %s |"
        % ("／".join(repr(r["sym1"]) for r in allrows), "✅" if ok2 else "🔴"))
    ok3 = all(r["sym0"] == 0.0 for r in allrows) and allrows
    say("   | [必為零] | 規定範圍與其自身之對稱差 ＝ `0` | %s | %s |"
        % ("／".join(repr(r["sym0"]) for r in allrows), "✅" if ok3 else "🔴"))
    if not (ok1 and ok2 and ok3):
        red("判別力三造**未全數成立** ⇒ 依單 `§三-2` 款 `9`：**判器紅、停、上呈**")

    say("")
    say("=" * W)
    say("## 🔒 自我驗證閘之**執行次數**（`§零` 附款 `(a)`·⛔ 以 `rc = 0` 充其已跑）")
    say("=" * W)
    for k in ("i", "ii", "iii", "iv"):
        say("   閘 `(%s)` ⇒ **%d** 次" % (k, GATE_N[k]))
    say("")
    say("🛑 **出艙即止**：⛔ 判殘差之成因是否即 `tol`、⛔ 判路丙成立與否、⛔ 訂任何取代之準據界、")
    say("   ⛔ 擬路丁、⛔ 改碼一字、⛔ 開分支、⛔ 動用 KL 之放行、⛔ 鑄 `GB`、⛔ 解除或收窄 `GB-170`、⛔ 呈 KL。")
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9293R_tol.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
