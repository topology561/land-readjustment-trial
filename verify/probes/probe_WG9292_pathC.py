#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-292` `§三`：**路丙**之設計驗算 —— 🛑 **出艙即止**。

🛑 **⛔ 改生產碼一字、⛔ 替身（本器之包裹一律<u>純委派</u>·⛔ 改其回傳）、⛔ 開分支。**
🔒 **底本** ＝ `verify/probes/probe_WG9287_landeffect.py` 之 `drive`（⛔ 另寫第二份驅動）。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**（旗標未設）·`SB ∈ {0.0, 3.5}`。

🔑 **路丙之形（單 `§三-1` 明定·⛔ CC 擴之）**
   於 `forced` 消費端，`_corner_buffer_S` 之 **`allocation_dir` 實參**改取
   `_first_corner_alloc_dir(side_mid)`；**⛔ 改** `_corner_buffer_S`／`_build_corner_range_v3` 一字。

🔑 **設計驗算之界定（單 `§三-2`）**
   ＝ 於**探針內**以**純幾何**複算一個**假設之輸入**所生之結果；**⛔ 改生產碼**、**⛔ 驅動替身**、
   **⛔ 入倉為生產態之數**。其出艙一律冠 `【設計驗算·⛔ 實測】`。

🔒 **複算所用之幾何原語一律取自 `ns`（碼面同一物·⛔ 自寫第二套）**：
   `_corner_buffer_S`（含其內之 bisect 容差 `tol`·由當場值帶入）／`_strip_s_range`／`_block_strip`／
   `k956_W_from_mp`。**帶之構造式逐字複刻** `app.py` `_corner_buffer_S._band_area`：
       a, b = (_lo, float(buf)) if side == 'left' else (s_max - float(buf), s_max)
       w = b - a
       bp = np.asarray(front_p1, dtype=float) + a * _d
       _g, _ar = _block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)

🔒 **自我驗證閘（三重·任一不過即器紅 `rc = 5`）**
   `(i)`   `_build_corner_range_v3` 之閉式回代 `|S1_par·sinθ − S1_perp| ≤ 1e-9`（承 `-286`／`-289`）。
   `(ii)`  **帶之重建**：以**當場之** `allocation_dir` 與**當場之** `buf` 重建之帶，其面積須 ＝ `range_area`
           （`|Δ| ≤ tol`）⇒ 證本器之 `_band_area` 複刻與碼面一致（⛔ 以閉式自證）。
   `(iii)` **`W_0` 之重建**：以當場之 `buf`／`allocation_dir` 依 `_mp_base_W0` 之**純委派式**重算，
           須與包裹所錄之 `k956_W_from_mp` 之**實際回傳**逐位相同（有錄者逐格檢）。

🔒 **實邊之取法（恆常附款「向量夾角須釘槽並以實邊機驗」）**：一切方向皆自**多邊形之實邊**取，
   並先以其**期望槽向**自檢 `|cos| ≥ 1 − 1e-6`；不過即 loud 拒測該格。

`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力三造不成立）。
用法：python verify/probes/probe_WG9292_pathC.py
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
_LOG = []
TAG = "【設計驗算·⛔ 實測】"


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
    """多邊形（含 Multi）之**外環實邊**（相鄰頂點對·⛔ 捨入）。"""
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


def _edir(e):
    return _unit((e[1][0] - e[0][0], e[1][1] - e[0][1]))


def _emid(e):
    return ((e[0][0] + e[1][0]) / 2.0, (e[0][1] + e[1][1]) / 2.0)


def _elen(e):
    return math.hypot(e[1][0] - e[0][0], e[1][1] - e[0][1])


def _cos(u, v):
    if u is None or v is None:
        return None
    return abs(u[0] * v[0] + u[1] * v[1])


def _proj_s(pt, base, d):
    return (pt[0] - base[0]) * d[0] + (pt[1] - base[1]) * d[1]


# ══════════════════════════════════════════════════════════════════════════════
def drive(sb):
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    os.environ.pop("WV_K6_STEP0", None)              # 🔒 **態甲**（旗標未設）
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    RNG, BUF, K956 = [], [], []

    # ── 包裹 `_build_corner_range_v3`（settrace 取其區域值·純委派）──────────
    _o_rng = ns["_build_corner_range_v3"]
    CODE = _o_rng.__code__
    SIG_R = inspect.signature(_o_rng)
    KEEP = ("S1_perp", "S1_par", "_sin_t", "sux", "suy", "dx", "dy",
            "F1", "S1", "_Tp", "D", "T", "eps")

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
                        "poly": out, "area": float(out.area), "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            RNG.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_build_corner_range_v3"] = _spy_rng

    # ── 包裹 `_corner_buffer_S`（取其**當場實參**·純委派）────────────────────
    _o_buf = ns["_corner_buffer_S"]
    CODE_B = _o_buf.__code__
    SIG_B = inspect.signature(_o_buf)
    KEEPB = ("s_min", "s_max", "_lo")

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
                        "block_poly": P.get("block_poly"), "d_hat": P.get("d_hat"),
                        "front_p1": P.get("front_p1"),
                        "allocation_dir": P.get("allocation_dir"),
                        "range_area": P.get("range_area"), "tol": P.get("tol"),
                        "buf": float(out), "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            BUF.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_corner_buffer_S"] = _spy_buf

    # ── 包裹 `k956_W_from_mp`（款 `6` 自我驗證閘之錨·純委派）────────────────
    _o_k = ns["k956_W_from_mp"]
    SIG_K = inspect.signature(_o_k)

    def _spy_k(*a, **kw):
        out = _o_k(*a, **kw)
        try:
            ba = SIG_K.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            K956.append({"point": P.get("point"), "side_mid": P.get("side_mid"),
                         "allocation_dir": P.get("allocation_dir"),
                         "d_hat": P.get("d_hat"), "out": float(out)})
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["k956_W_from_mp"] = _spy_k

    # ── 驅動（與 `-287` 同源）────────────────────────────────────────────
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
    n_rng0, n_buf0 = len(RNG), len(BUF)
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
    return {"RNG": RNG, "BUF": BUF, "K956": K956, "crp": crp,
            "n_rng0": n_rng0, "n_buf0": n_buf0,
            "fo": fo_tab, "err": err, "ns": ns, "st": fake_st}


def _pick(recs, blk, side):
    """自紀錄中取該 (街廓, 側) 之**最末**一筆（⛔ 逕取首命中·坑 `bi`）。"""
    out = [r for r in recs
           if r.get("side") == side and blk in str(r.get("label") or "")]
    return (out[-1], len(out)) if out else (None, 0)


def band_poly(ns, block_poly, d_hat, front_p1, allocation_dir, buf, side):
    """帶之構造 —— **逐字複刻** `app.py` `_corner_buffer_S._band_area`（⛔ 自寫第二套）。"""
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


def far_cut_edge(g, d_hat, front_p1, allocation_dir, side):
    """帶之**實切邊**：方向 ∥ `rot90(allocation_dir)` 之邊中，`s` 最大（左）／最小（右）者。"""
    want = _unit(_rot90(_unit(allocation_dir)))
    cand = [e for e in _edges(g) if (_cos(_edir(e), want) or 0.0) >= 1.0 - 1e-6]
    if not cand:
        return None, None, len(_edges(g))
    d = _unit(d_hat)
    key = (lambda e: _proj_s(_emid(e), front_p1, d))
    e = max(cand, key=key) if side == "left" else min(cand, key=key)
    return e, _cos(_edir(e), want), len(cand)


def far_range_edge(g, Tp, su):
    """規定範圍之**遠側境界線**：過 `_Tp` 且方向 ∥ `su` 之實邊（二端點之線距皆 ≤ tol）。"""
    su = _unit(su)
    best, bad = None, None
    for e in _edges(g):
        if (_cos(_edir(e), su) or 0.0) < 1.0 - 1e-6:
            continue
        d0 = abs((e[0][0] - Tp[0]) * (-su[1]) + (e[0][1] - Tp[1]) * su[0])
        d1 = abs((e[1][0] - Tp[0]) * (-su[1]) + (e[1][1] - Tp[1]) * su[0])
        m = max(d0, d1)
        if best is None or m < best[1]:
            best, bad = (e, m), m
    if best is None:
        return None, None
    return best[0], bad


# ══════════════════════════════════════════════════════════════════════════════
def analyse(sb, d):
    ns = d["ns"]
    crp = d["crp"]
    say("")
    say("=" * W)
    say("【SB ＝ %s m·態甲】`_build_corner_range_v3` %d 次（`run_step_g` 段 %d）／"
        "`_corner_buffer_S` %d 次（段內 %d）／`k956_W_from_mp` %d 次"
        % (repr(sb), len(d["RNG"]), len(d["RNG"]) - d["n_rng0"],
           len(d["BUF"]), len(d["BUF"]) - d["n_buf0"], len(d["K956"])))
    say("　`run_step_g` 之終局 ＝ %s" % (d["err"] or "（未拋）"))
    say("　`corner_range_polys` 之鍵 ＝ %d 個：%s"
        % (len(crp), sorted("%s/%s" % k for k in crp)))
    say("=" * W)

    say("🔒 **`forced` 側之全部成員（當場重量·⛔ 轉引）**")
    say("   | 街廓 | left_forced | right_forced |")
    say("   |---|---|---|")
    grids = []
    for b in BLKS:
        L, R = d["fo"][b]
        say("   | `%s` | %s | %s |" % (b, L, R))
        if L:
            grids.append((b, "left"))
        if R:
            grids.append((b, "right"))
    say("   ⇒ `forced` 格 ＝ **%d**（%s）"
        % (len(grids), "、".join("%s/%s" % g for g in grids)))
    say("")

    rows = []
    for blk, side in grids:
        say("─" * W)
        say("### `%s`／`%s`＠`SB = %s`" % (blk, side, repr(sb)))
        br, nb = _pick(d["BUF"], blk, side)
        rr, nr = _pick(d["RNG"], blk, side)
        if br is None or rr is None:
            red("`%s/%s`：`_corner_buffer_S` 紀錄 %d 筆／`_build_corner_range_v3` %d 筆 ⇒ **loud 拒測**"
                % (blk, side, nb, nr))
            continue
        cp = crp.get((blk, side))
        if cp is None:
            red("`%s/%s`：`corner_range_polys[(%r, %r)]` ⇒ `None` ⇒ **loud 拒測**" % (blk, side, blk, side))
            continue

        loc = rr["loc"]
        S1_perp = float(loc.get("S1_perp"))
        S1_par = float(loc.get("S1_par"))
        sin_t = float(loc.get("_sin_t"))
        Tp = tuple(float(x) for x in loc.get("_Tp"))
        su = (float(loc.get("sux")), float(loc.get("suy")))

        # ── 自我驗證閘 (i) ──
        g_i = abs(S1_par * sin_t - S1_perp)
        say("  **自我驗證閘 `(i)`**　`|S1_par·sinθ − S1_perp|` ＝ `%r` ⇒ %s"
            % (g_i, "✅" if g_i <= 1e-9 else "🔴"))
        if g_i > 1e-9:
            red("`%s/%s`：閘 `(i)` 不過 ⇒ 該格之數⛔ 出艙" % (blk, side))
            continue

        bp_, dh_, fp_ = br["block_poly"], br["d_hat"], br["front_p1"]
        ad1, ra, tol, buf1 = br["allocation_dir"], float(br["range_area"]), br["tol"], br["buf"]

        # ── 款 2：當場實參 ──
        sl = ((d["st"].session_state.get("f3_cad_side_lines_by_side", {}) or {})
              .get(blk, {}) or {}).get(side, {}) or {}
        side_mid = sl.get("mid")
        say("  **款 `2`**　`_corner_buffer_S` 之當場實參（`repr` 全位）")
        say("      `allocation_dir` ＝ `%r`" % (tuple(float(x) for x in ad1),))
        say("      `range_area` ＝ `%r`／`tol` ＝ `%r`／`side` ＝ `%r`／現行 `buf` ＝ `%r`"
            % (ra, tol, side, buf1))
        say("      `side_mid`（`f3_cad_side_lines_by_side[%r][%r]['mid']`）＝ `%s`"
            % (blk, side, "可達 " + repr(tuple(float(x) for x in side_mid))
               if side_mid is not None else "🔴 **⛔ 可達**"))
        if side_mid is None:
            red("`%s/%s`：`side_mid` ⛔ 可達 ⇒ 路丙之輸入不存在 ⇒ **loud 拒測**" % (blk, side))
            continue

        # ── 自我驗證閘 (ii)：以當場之 ad1／buf1 重建帶，面積須 ＝ range_area ──
        g1, dom1, ar1 = band_poly(ns, bp_, dh_, fp_, ad1, buf1, side)
        ok_ii = (ar1 is not None) and abs(ar1 - ra) <= float(tol)
        say("  **自我驗證閘 `(ii)`**　以**當場之** `allocation_dir`／`buf` 重建之帶：面積 ＝ `%r`／"
            "`range_area` ＝ `%r`／`|Δ|` ＝ `%r`（`tol` ＝ `%r`）⇒ %s"
            % (ar1, ra, (None if ar1 is None else abs(ar1 - ra)), tol, "✅" if ok_ii else "🔴"))
        if not ok_ii:
            red("`%s/%s`：閘 `(ii)` 不過（本器之 `_band_area` 複刻與碼面不一致）⇒ 該格之數⛔ 出艙"
                % (blk, side))
            continue

        # ── 路丙之輸入 ──
        ad2 = ns["_first_corner_alloc_dir"](side_mid)
        say("  %s **路丙之輸入**　`_first_corner_alloc_dir(side_mid)` ＝ `%r`"
            % (TAG, tuple(float(x) for x in ad2)))
        say("      其與現行 `allocation_dir` 之 `|cos|`（**槽 ＝ 二者皆 `allocation_dir` 槽**）＝ `%r`"
            % _cos(_unit(ad1), _unit(ad2)))

        # ── 款 3：設計驗算之帶 ──
        try:
            buf2 = ns["_corner_buffer_S"](bp_, dh_, fp_, ad2, ra, side,
                                          tol=tol, _label="WG9292設計驗算·" + blk)
        except Exception as e:                                   # noqa: BLE001
            red("`%s/%s`：%s `_corner_buffer_S` 以路丙之輸入拋出 ⇒ %s" % (blk, side, TAG, e))
            continue
        g2, dom2, ar2 = band_poly(ns, bp_, dh_, fp_, ad2, buf2, side)
        say("  **款 `3`**　%s 帶之複算（原語皆取自 `ns`·構造式逐字複刻 `_band_area`）" % TAG)
        say("      `s` 域：現行 ＝ `%r`／路丙 ＝ `%r`" % (dom1, dom2))
        say("      帶面積：現行 ＝ `%r`／路丙 ＝ `%r`（`range_area` ＝ `%r`）" % (ar1, ar2, ra))

        # ── 款 4：對稱差 ──
        def _sym(a, b):
            if a is None or b is None:
                return None, None, None
            ab = a.difference(b)
            ba = b.difference(a)
            return float(ab.area), float(ba.area), float(ab.area) + float(ba.area)
        d21, d12, sym2 = _sym(g2, cp)
        d11, d1c, sym1 = _sym(g1, cp)
        d00, d0c, sym0 = _sym(cp, cp)
        say("  **款 `4`**　與 `corner_range_polys[(%r, %r)]` 之**對稱差**（面積·㎡）" % (blk, side))
        say("      | 甲（帶） | `甲∖乙` | `乙∖甲` | **對稱差** |")
        say("      |---|---|---|---|")
        say("      | %s 路丙之帶 | `%r` | `%r` | **`%r`** |" % (TAG, d21, d12, sym2))
        say("      | 現行之帶（判別力[必相異]） | `%r` | `%r` | **`%r`** |" % (d11, d1c, sym1))
        say("      | 規定範圍自身（判別力[必為零]） | `%r` | `%r` | **`%r`** |" % (d00, d0c, sym0))

        # ── 款 5：實切邊 vs 遠側境界線 ──
        e2, c2, n2 = far_cut_edge(g2, dh_, fp_, ad2, side)
        er, dr = far_range_edge(cp, Tp, su)
        say("  **款 `5`**　實切邊 vs 遠側境界線（**釘槽**·皆取**實邊**）")
        if e2 is None:
            red("`%s/%s`：帶上無 ∥`rot90(allocation_dir)` 之實邊（候選 %d）⇒ loud 拒測" % (blk, side, n2))
            cos5 = None
        elif er is None:
            red("`%s/%s`：規定範圍上無 ∥`su` 且過 `_Tp` 之實邊 ⇒ loud 拒測" % (blk, side))
            cos5 = None
        else:
            say("      帶之實切邊　　：`%r` → `%r`（長 `%r`）" % (e2[0], e2[1], _elen(e2)))
            say("        其與期望槽 `rot90(allocation_dir)` 之 `|cos|` ＝ `%r`（自檢·須 ≥ 1−1e-6）" % c2)
            say("      範圍之遠側境界線：`%r` → `%r`（長 `%r`·二端至過 `_Tp` 之線之最大距 ＝ `%r`）"
                % (er[0], er[1], _elen(er), dr))
            say("        其與期望槽 `su`（SIDE 之**線向**）之 `|cos|` ＝ `%r`" % _cos(_edir(er), su))
            cos5 = _cos(_edir(e2), _edir(er))
            say("      🔑 **二實邊之 `\\|cos\\|` ＝ `%r`**（與 `1` 之差 ＝ `%r`·期 `≥ 1 − 1e-6`）"
                % (cos5, None if cos5 is None else abs(cos5 - 1.0)))

        # ── 款 6：buf′ 與 W_0′ ──
        import numpy as np

        def _w0(gs, buf, dv, mp, adir):
            """`_mp_base_W0` 之**純委派式**逐字複刻（`verify/stepg_pipeline.py` 之該閉包）。"""
            if gs is None or mp is None or adir is None or dv is None:
                return 0.0
            dv2 = np.asarray(dv, dtype=float)
            dn = float(np.linalg.norm(dv2))
            du = dv2 / dn if dn > 1e-9 else dv2
            bp0 = np.asarray(gs, dtype=float) + float(buf) * du
            return float(ns["k956_W_from_mp"](bp0, mp, adir, dv))

        w0_cur = _w0(fp_, buf1, dh_, side_mid, ad1)
        w0_new = _w0(fp_, buf2, dh_, side_mid, ad2)

        # ── 自我驗證閘 (iii)：`W_0` 之重建須對拍**包裹所錄**之 `k956_W_from_mp` 實際回傳 ──
        #    🔒 錄之來源 ＝ 生產路徑之 `_mp_base_W0`（其 `_gs` ＝ `corner_pt` ＝ 本函式之 `front_p1`）。
        #    🛑 無錄可比者一律 **loud 具名為「不可驗」**——「無從回測」⛔ 等同「回測不過」。
        import numpy as _np3
        _bp0 = _np3.asarray(fp_, dtype=float) + float(buf1) * (
            _np3.asarray(dh_, dtype=float) / float(_np3.linalg.norm(_np3.asarray(dh_, dtype=float))))
        _hit = []
        for r in d["K956"]:
            try:
                p = _np3.asarray(r["point"], dtype=float)[:2]
                if float(_np3.max(_np3.abs(p - _bp0[:2]))) <= 1e-12:
                    _hit.append(r)
            except Exception:                                    # noqa: BLE001
                continue
        if not _hit:
            say("  **自我驗證閘 `(iii)`**　🟡 **不可驗（loud）**——`k956_W_from_mp` 之包裹於本格"
                "**無對應之錄**（本 `SB` 之總錄數 ＝ %d）⇒ 該格之 `W_0` 係**本器之重建**、⛔ 經對拍"
                % len(d["K956"]))
            ok_iii = None
        else:
            _dv = min(abs(float(r["out"]) - w0_cur) for r in _hit)
            ok_iii = _dv == 0.0
            say("  **自我驗證閘 `(iii)`**　`W_0` 之重建 vs 包裹所錄之 `k956_W_from_mp` 實際回傳："
                "錄 %d 筆·最小差 ＝ `%r` ⇒ %s" % (len(_hit), _dv, "✅ 逐位相同" if ok_iii else "🔴"))
            if not ok_iii:
                red("`%s/%s`：閘 `(iii)` 不過（本器之 `_mp_base_W0` 複刻與碼面不一致）⇒ 該格之 `W_0` ⛔ 出艙"
                    % (blk, side))
                continue

        say("  **款 `6`**　`buf` 與 `W_0`")
        say("      現行 `buf` ＝ `%r`" % buf1)
        say("      %s 路丙 `buf′` ＝ `%r`（差 ＝ `%r`）" % (TAG, buf2, buf2 - buf1))
        say("      現行 `W_0`（本器以 `_mp_base_W0` 之純委派式重算·**起點 ＝ `front_p1`**）＝ `%r`" % w0_cur)
        say("      %s 路丙 `W_0′` ＝ `%r`／`S1_perp` ＝ `%r`／**`|W_0′ − S1_perp|` ＝ `%r`**（期 ≤ `1e-9`）"
            % (TAG, w0_new, S1_perp, abs(w0_new - S1_perp)))
        rows.append({"sb": sb, "blk": blk, "side": side, "buf1": buf1, "buf2": buf2,
                     "sym2": sym2, "sym1": sym1, "sym0": sym0, "cos5": cos5,
                     "w0_new": w0_new, "S1_perp": S1_perp, "g_iii": ok_iii,
                     "dw": abs(w0_new - S1_perp)})
        say("")
    return rows


FORCED_CONSUMERS = [("app.py", "main"),
                    ("verify/stepg_pipeline.py", "_run_step_g_impl"),
                    ("verify/wf_f1.py", "compute"),
                    ("verify/wf_f4.py", "_reshape_block")]


def _scope(rel, fname):
    """(函式節點, scope 內全部名, **`t.body` 頂層**全域名)　⛔ 以 `ast.walk` 取頂層（`-289R` 自捕二）。"""
    import ast
    txt = open(os.path.join(REPO, rel), encoding="utf-8").read()
    tree = ast.parse(txt)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == fname:
            fn = node
            break
    names = set()
    if fn is not None:
        for node in ast.walk(fn):
            if isinstance(node, ast.Name):
                names.add(node.id)
            elif isinstance(node, ast.arg):
                names.add(node.arg)
    top = set()
    for node in tree.body:                              # 🔒 **`t.body` 頂層**·⛔ `ast.walk`
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            top.add(node.name)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    top.add(t.id)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for al in node.names:
                top.add(al.asname or al.name.split(".")[0])
    return fn, names, top, tree


def static():
    """款 `1`：`_first_corner_alloc_dir` 之**定義層級**與其於四個 `forced` 消費端之**可達性**（三態）。"""
    import ast
    NAME = "_first_corner_alloc_dir"
    say("=" * W)
    say("## 款 `1`　`%s` 之定義層級與可達性（**靜態·AST**·⛔ 文字層）" % NAME)
    say("=" * W)

    txt = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
    tree = ast.parse(txt)
    top_def = [n for n in tree.body
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == NAME]
    nested = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == NAME and n not in top_def:
            nested.append(n)
    say("   **定義層級**（框 ＝ `app.py` 之 `t.body` 頂層 vs `ast.walk` 之差）")
    say("      `t.body` 頂層之 `FunctionDef` 命中 ＝ **%d**%s"
        % (len(top_def), ("（`app.py:%d`–`%d`）" % (top_def[0].lineno, top_def[0].end_lineno))
           if top_def else ""))
    say("      `ast.walk` 之**巢狀**命中 ＝ **%d**%s"
        % (len(nested), ("（%s）" % [n.lineno for n in nested]) if nested else ""))
    say("      ⇒ **%s**" % ("模組頂層（⛔ 巢狀）" if (top_def and not nested) else "🔴 非單純頂層·見上數"))

    say("")
    say("   **可達性（三態·框同 `W-G.9-289 §三`）**")
    say("   | `forced` 消費端所在 scope | AST 區間 | scope 名數 | `t.body` 頂層全域數 | `%s` | **判** |" % NAME)
    say("   |---|---|---|---|---|---|")
    for rel, fname in FORCED_CONSUMERS:
        fn, names, top, _t = _scope(rel, fname)
        if fn is None:
            red("`%s` `%s`：**查無該函式** ⇒ loud 拒測" % (rel, fname))
            continue
        a = NAME in names
        b = NAME in top
        v = ("✅ `(i)` 同一 scope 可達" if a
             else ("🟡 `(ii)` 頂層全域可達" if b else "🔴 `(iii)` ⛔ 可達"))
        say("   | `%s` `%s` | `%d`–`%d` | `%d` | `%d` | scope `%s`／頂層全域 `%s` | %s |"
            % (rel, fname, fn.lineno, fn.end_lineno, len(names), len(top), a, b, v))
    _fn, _nm, _tp, _ = _scope("app.py", "main")
    Z = NAME + "_nosuch" + str(146 * 2)                  # 執行期組出·字面⛔ 出艙
    say("   🔑 **判別力二造**：[必可達] `_corner_buffer_S` 於 `app.py` 頂層全域 ＝ **%s**（須 True）／"
        "[必⛔ 可達] 一人造名（執行期組出·字面⛔ 出艙）＝ **%s**（須 False）⇒ %s"
        % ("_corner_buffer_S" in _tp, Z in _tp,
           "✅ 器非紅" if ("_corner_buffer_S" in _tp and Z not in _tp) else "🔴 器紅"))
    say("")

    say("   **`_corner_buffer_S` 之簽章逐字**（款 `2`·AST `unparse` 之 `args`）")
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name == "_corner_buffer_S":
            say("      `app.py:%d`  `def _corner_buffer_S(%s)`" % (n.lineno, ast.unparse(n.args)))
    say("")


def main():
    static()
    allrows = []
    for sb in SBS:
        allrows += analyse(sb, drive(sb))

    say("=" * W)
    say("## 款 `7`　判別力三造之判（母體 ＝ 上開全部 `forced` 格）")
    say("=" * W)
    n = len(allrows)
    say("   | 造 | 判準 | 實測 | 判 |")
    say("   |---|---|---|---|")
    ok1 = n >= 1
    say("   | [必命中] | `forced` 格數 `≥ 1` | **%d** | %s |" % (n, "✅" if ok1 else "🔴"))
    bad2 = [r for r in allrows if not (r["sym1"] is not None and r["sym1"] > 0)]
    ok2 = (n >= 1) and not bad2
    say("   | [必相異] | **現行** `buf` 所生之帶與規定範圍之對稱差須 `> 0`（證款 `4` 非恆零） | %s | %s |"
        % ("／".join(repr(r["sym1"]) for r in allrows), "✅" if ok2 else "🔴"))
    bad3 = [r for r in allrows if not (r["sym0"] == 0.0)]
    ok3 = (n >= 1) and not bad3
    say("   | [必為零] | 規定範圍與其自身之對稱差須 `0`（先自證可滿足） | %s | %s |"
        % ("／".join(repr(r["sym0"]) for r in allrows), "✅" if ok3 else "🔴"))
    if not (ok1 and ok2 and ok3):
        red("判別力三造未全數成立 ⇒ **判器紅、停、上呈**")

    say("")
    say("=" * W)
    say("## 總表（%s·⛔ 與實測之數同表混列）" % TAG)
    say("=" * W)
    say("   | `SB` | 格 | 現行 `buf` | 路丙 `buf′` | **對稱差（路丙）** | 對稱差（現行） | 二實邊 `\\|cos\\|` | `\\|W_0′ − S1_perp\\|` | 閘 `(iii)` |")
    say("   |---|---|---|---|---|---|---|---|---|")
    for r in allrows:
        say("   | `%s` | `%s/%s` | `%r` | `%r` | **`%r`** | `%r` | `%r` | `%r` | %s |"
            % (repr(r["sb"]), r["blk"], r["side"], r["buf1"], r["buf2"],
               r["sym2"], r["sym1"], r["cos5"], r["dw"],
               {True: "✅ 逐位相同", False: "🔴", None: "🟡 不可驗（無錄）"}[r["g_iii"]]))
    say("")
    say("🛑 **出艙即止**：本器⛔ 判路丙成立與否、⛔ 改碼一字、⛔ 開分支、⛔ 動用 KL 之放行、")
    say("   ⛔ 鑄 `GB`、⛔ 解除或收窄 `GB-170`、⛔ 提修法主張、⛔ 呈 KL。")
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9292R_pathC.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
