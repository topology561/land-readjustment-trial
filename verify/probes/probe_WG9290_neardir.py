#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-290` `§三`：winner 側之第 1 宗如何取得其**近側界** ／ 二態之路徑分歧點
—— 🛑 **純現查與量測·出艙即止**。

🛑 **⛔ 改生產碼一字、⛔ 替身、⛔ 反事實、⛔ 擬任何實作形**（單 `§六`）。
🔒 **底本** ＝ `verify/probes/probe_WG9287_landeffect.py` 之 `drive`（⛔ 另寫第二份驅動）。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**（旗標未設）·`SB ∈ {0.0, 3.5}`。

🔑 **包裹點之選擇（⛔ 推定·自碼面現查）**
   `_alloc_dir_used` 係於 **`_solve_G_one`**（`app.py`·module 級）內設於其回傳 `_r` 上
   （`app.py:14014`／`:14029`），而 `solve_G_binary` 之回傳**尚無**該欄
   ⇒ 本器包 **`ns["_solve_G_one"]`**（其為 `verify/stepg_pipeline.py` 之 `_solve_one` 薄殼所委派者·`:516`）。

🔒 **自我驗證閘（二重·任一不過即器紅）**
   `(i)`  `_build_corner_range_v3` 之閉式回代 `|S1_par·sinθ − S1_perp| ≤ 1e-9`（承 `-286`／`-287`）。
   `(ii)` 凡 `is_corner=True` 之筆，其 `_alloc_dir_used` 須**逐位等於**同格 `_first_corner_alloc_dir`
          之回傳（⇒ 證「`allocation_dir` 於 `app.py:13990` 被換」之重建**非臆測**）。
   `(iii)`**鏈側之歸屬**：每一筆須恰屬 `left_group`／`right_group` 之一（**⛔ 二者皆非**）；
          其總數須等於 `_solve_G_one` 於 `run_step_g` 段之筆數（⇒ 證側之重建**無漏無重**）。
   `(iv)` 🔑 **線向之槽**：`near_dir`／`allocation_dir` 係 **`allocation_dir` 槽**之向量，
          其**線向** ＝ `rot90(·)`（碼面逐字：`_block_strip` 之「切割帶兩側方向 `n_hat = rot90(allocation_dir)`」；
          `_first_corner_alloc_dir` docstring：「其切帶之 `allocation_dir` 改為 `rot90_cw(SIDE 方向)`
          （`_block_strip` 之 `n_hat = rot90(allocation_dir)` ⇒ **界線 ∥SIDELINE**）」）。
          **本閘以該宗之 `cut_coords` 之<u>實邊</u>驗之**：`rot90(_alloc_dir_used)` 須與其某一實邊
          之方向 `|cos| ≥ 1 − 1e-6`（⇒ 證該 `rot90` 之語意**非臆測**）。

`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力二造任一不成立）。
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


def _rot90(v):
    """🔑 `allocation_dir` 槽 → **線向**（碼面逐字 `n_hat = rot90(allocation_dir)`）。"""
    return None if v is None else _unit((-float(v[1]), float(v[0])))


def _best_edge_cos(coords, d):
    """該多邊形之**實邊**中，與 `d` 最平行者之 `|cos|`（⇒ 閘 `(iv)` 之受詞）。"""
    if not coords or d is None or len(coords) < 2:
        return None
    best = 0.0
    for i in range(len(coords)):
        a = coords[i]
        b = coords[(i + 1) % len(coords)]
        e = _unit((float(b[0]) - float(a[0]), float(b[1]) - float(a[1])))
        if e is None:
            continue
        best = max(best, abs(e[0] * d[0] + e[1] * d[1]))
    return best


def drive(sb):
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    os.environ.pop("WV_K6_STEP0", None)              # 🔒 **態甲**（旗標未設）
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    RNG, SGO, FCA = [], [], []

    # ── 包裹 `_build_corner_range_v3`（＋ `settrace` 取其區域值·承 `-287`）──────
    _o_rng = ns["_build_corner_range_v3"]
    CODE = _o_rng.__code__
    SIG_R = inspect.signature(_o_rng)
    KEEP = ("S1_perp", "S1_par", "_sin_t", "sux", "suy", "dx", "dy", "F1", "S1", "_Tp")

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
                        "baseline_pts": P.get("baseline_pts"),
                        "poly": out, "area": float(out.area), "loc": cap})
        except Exception as e:                                   # noqa: BLE001
            RNG.append({"label": "🔴bind:%r" % (e,), "side": None, "loc": cap})
        return out

    ns["_build_corner_range_v3"] = _spy_rng

    # ── 包裹 `_first_corner_alloc_dir`（自我驗證閘 `(ii)` 之受詞）──────────────
    _o_fca = ns["_first_corner_alloc_dir"]

    def _spy_fca(side_mid):
        out = _o_fca(side_mid)
        FCA.append({"side_mid": side_mid, "ret": out})
        return out

    ns["_first_corner_alloc_dir"] = _spy_fca

    # ── 包裹 `_solve_G_one`（🔑 其回傳始含 `_alloc_dir_used`）──────────────────
    _o_sgo = ns["_solve_G_one"]
    SIG_S = inspect.signature(_o_sgo)

    def _climb(names, upto=14):
        out = {k: None for k in names}
        seen = {k: False for k in names}
        for d in range(1, upto + 1):
            try:
                fr = sys._getframe(d + 1)
            except ValueError:
                break
            for k in names:
                if (not seen[k]) and k in fr.f_locals:
                    out[k] = fr.f_locals[k]
                    seen[k] = True
        return out

    CL = ["blk_label", "k", "_lg_idx_left", "_lg_idx_right",
          "left_cum_S", "right_cum_S", "_near_dir_left", "_near_dir_right",
          "is_first_corner_l", "is_first_corner_r", "first_corner_used_left",
          "first_corner_used_right", "entry", "_fo_left", "_fo_right",
          "allocation_dir_block", "_side_mid_left", "_side_mid_right",
          "left_group", "right_group"]

    def _spy_sgo(*a, **kw):
        c = _climb(CL)
        out = _o_sgo(*a, **kw)
        try:
            ba = SIG_S.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            res = (out or (None, None))[0] or {}
            ent = c.get("entry") or {}
            # 🩸 **本批自捕**：`_solve_G_one` 之 `side` 參數 ＝ 該宗之**街角側別**
            #   （`verify/stepg_pipeline.py:804` `side = entry.get('side', '無')`），
            #   **⛔ 鏈側**；`'無'` 落入 `else` 分支會令一切非街角宗被誤標為 `right`。
            #   🔒 **鏈側之真相源** ＝ `left_group`／`right_group` 之**成員**
            #   （`:796`／`:897` 之迴圈；`_lot_gate` 於 `:843`／`:961` 傳字面 `'left'`／`'right'`）。
            _lg = c.get("left_group") or []
            _rg = c.get("right_group") or []
            side = None
            if any(e is ent for e in _lg):
                side = "left"
            elif any(e is ent for e in _rg):
                side = "right"
            SGO.append({
                "blk": c.get("blk_label"), "side": side, "id": c.get("k"),
                "idx": (c.get("_lg_idx_left") if side == "left" else c.get("_lg_idx_right")),
                "is_corner": P.get("is_corner"), "is_chain_head": P.get("is_chain_head"),
                "near_dir_in": P.get("near_dir"),
                "alloc_dir_in": P.get("allocation_dir"),
                "side_mid": P.get("side_mid"), "W_prev": P.get("W_prev"),
                "baseline_pt": P.get("baseline_pt"),
                "alloc_dir_used": res.get("_alloc_dir_used"),
                "cut_coords": list(res.get("cut_coords") or []),
                "W_near": res.get("W_near"), "G": res.get("G"), "S": res.get("S"),
                "solver": (out or (None, None))[1],
                "cum_S_in": (c.get("left_cum_S") if side == "left" else c.get("right_cum_S")),
                "near_thread": (c.get("_near_dir_left") if side == "left"
                                else c.get("_near_dir_right")),
                "is_first_corner_flag": (c.get("is_first_corner_l") if side == "left"
                                         else c.get("is_first_corner_r")),
                "first_corner_used": (c.get("first_corner_used_left") if side == "left"
                                      else c.get("first_corner_used_right")),
                "marker": bool(ent.get("is_first_corner_marker", False)),
                "corner_winner": bool(ent.get("is_corner_winner", False)),
                "fo": (c.get("_fo_left") if side == "left" else c.get("_fo_right")),
                "alloc_dir_block": c.get("allocation_dir_block"),
            })
        except Exception:                                        # noqa: BLE001
            pass
        return out

    ns["_solve_G_one"] = _spy_sgo

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
    n0 = len(SGO)
    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb, eff_min_build_by_blk={})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"RNG": RNG, "SGO": SGO, "FCA": FCA, "n0": n0,
            "fo": fo_tab, "err": err, "ns": ns}


def _rng_pick(recs, blk, side):
    out = [r for r in recs if r.get("side") == side and blk in str(r.get("label") or "")]
    return (out[-1], len(out)) if out else (None, 0)


def analyse(sb, d):
    say("")
    say("=" * W)
    say("【SB ＝ %s m·態甲】`_solve_G_one` %d 次（`run_step_g` 段 %d）／"
        "`_first_corner_alloc_dir` %d 次／`_build_corner_range_v3` %d 次"
        % (repr(sb), len(d["SGO"]), len(d["SGO"]) - d["n0"], len(d["FCA"]), len(d["RNG"])))
    say("　`run_step_g` 之終局 ＝ %s" % (d["err"] or "（未拋）"))
    say("=" * W)

    seg = d["SGO"][d["n0"]:]

    # ── 自我驗證閘 `(ii)` ────────────────────────────────────────────────
    fca_set = [tuple(float(x) for x in (r["ret"] or ())) for r in d["FCA"] if r.get("ret")]
    n_ok, n_bad = 0, 0
    for r in seg:
        if not r.get("is_corner"):
            continue
        a = r.get("alloc_dir_used")
        if a is None:
            n_bad += 1
            continue
        t = tuple(float(x) for x in a)
        if t in fca_set:
            n_ok += 1
        else:
            n_bad += 1
    say("🔒 **自我驗證閘 `(ii)`**：`is_corner=True` 之筆 ＝ %d；其 `_alloc_dir_used` 逐位等於"
        " `_first_corner_alloc_dir` 之回傳者 ＝ **%d**／不符 ＝ **%d** ⇒ %s"
        % (n_ok + n_bad, n_ok, n_bad, "✅" if (n_bad == 0 and n_ok > 0) else "🔴"))
    if n_bad or not n_ok:
        red("自我驗證閘 `(ii)` 不過 ⇒ ⛔ 據以下任何結論")

    cells = []
    for b in BLKS:
        L, R = d["fo"][b]
        if L:
            cells.append((b, "left"))
        if R:
            cells.append((b, "right"))
    say("🔒 **`forced` 側（當場重量）** ＝ %d 格：%s" % (len(cells), cells))

    # ── 自我驗證閘 `(iii)`：鏈側之歸屬無漏無重 ──────────────────────────
    n_side = sum(1 for r in seg if r.get("side") in ("left", "right"))
    n_none = sum(1 for r in seg if r.get("side") not in ("left", "right"))
    say("🔒 **自我驗證閘 `(iii)`**（鏈側之歸屬·**⛔ 取 `_solve_G_one` 之 `side` 參數**——其為"
        "**街角側別**·`stepg:804`）：`run_step_g` 段之筆 ＝ **%d**；歸入 `left`／`right` 者 ＝ **%d**／"
        "二者皆非 ＝ **%d** ⇒ %s"
        % (len(seg), n_side, n_none, "✅" if (n_none == 0 and n_side == len(seg)) else "🔴"))
    if n_none or n_side != len(seg):
        red("自我驗證閘 `(iii)` 不過 ⇒ 鏈側之重建有漏 ⇒ ⛔ 據以下任何結論")

    # ── 逐格逐宗之**分項表**（款 `4` 之受詞）────────────────────────────
    tgt = sorted({(r["blk"], r["side"]) for r in seg if r.get("blk") and r.get("side")})
    say("")
    say("**款 `4`　二態之逐宗分項表**（⛔ 只報合取·逐分項）")
    say("   | 格 | idx | 暫編地號 | `forced` | `marker` | `is_corner` | `is_chain_head` |"
        " `near_dir` 入 | `alloc_dir_used` | `solver` |")
    say("   |---|---|---|---|---|---|---|---|---|---|")
    for (blk, side) in tgt:
        for r in [x for x in seg if x["blk"] == blk and x["side"] == side][:4]:
            say("   | `%s/%s` | %s | `%s` | %s | %s | **%s** | %s | %s | %s | %s |"
                % (blk, side, r["idx"], r["id"], r["fo"], r["marker"],
                   r["is_corner"], r["is_chain_head"],
                   "None" if r["near_dir_in"] is None else _pt(r["near_dir_in"]),
                   "None" if r["alloc_dir_used"] is None else _pt(r["alloc_dir_used"]),
                   r["solver"]))
    return seg


def detail(sb, d, seg, blk, side, tag):
    say("")
    say("═" * W)
    say("── 格 `%s/%s@%sm`（%s）──" % (blk, side, repr(sb), tag))
    say("═" * W)
    rows = [x for x in seg if x["blk"] == blk and x["side"] == side]
    if not rows:
        say("   🟡 該格於本情境**無 `_solve_G_one` 筆** ⇒ 具名為「不可得」（⛔ 以空集充綠）")
        return None
    r, nr = _rng_pick(d["RNG"], blk, side)
    lo = (r or {}).get("loc") or {}
    need = ("S1_perp", "S1_par", "_sin_t", "sux", "suy", "dx", "dy", "F1", "S1", "_Tp")
    if r is None or [k for k in need if k not in lo]:
        say("   🟡 `_build_corner_range_v3` 之區域值缺 ⇒ **⛔ 施款 `2` 之對拍**（具名·⛔ 靜默略過）")
        su = tp = None
    else:
        resid = abs(_f(lo["S1_par"]) * _f(lo["_sin_t"]) - _f(lo["S1_perp"]))
        say("   🔒 **自我驗證閘 `(i)`**　`|S1_par·sinθ − S1_perp|` ＝ %r（須 ≤ 1e-9）⇒ %s"
            % (resid, "✅" if resid <= 1e-9 else "🔴"))
        if resid > 1e-9:
            red("格 `%s/%s`：自我驗證閘 `(i)` 不過" % (blk, side))
            return None
        su = _unit((lo["sux"], lo["suy"]))
        tp = (_f(lo["_Tp"][0]), _f(lo["_Tp"][1]))
        say("   `corner_range_polys[%r]` 之**遠側境界線**：錨 `_Tp` ＝ %s ／ 方向單位向量 ＝ %s"
            " ／ `S1_perp` ＝ %r" % (side, _pt(tp), _pt(su), _f(lo["S1_perp"])))

    dh = _unit((lo.get("dx"), lo.get("dy"))) if lo else None
    F1 = (_f(lo["F1"][0]), _f(lo["F1"][1])) if lo else None
    bp = (r or {}).get("baseline_pts")
    bdir = _unit((_f(bp[1][0]) - _f(bp[0][0]), _f(bp[1][1]) - _f(bp[0][1]))) if bp else None
    bpt = (_f(bp[0][0]), _f(bp[0][1])) if bp else None

    for x in rows[:3]:
        say("")
        say("   ── idx `%s`　`%s`（`is_corner`＝%s／`is_chain_head`＝%s／`forced`＝%s）"
            % (x["idx"], x["id"], x["is_corner"], x["is_chain_head"], x["fo"]))
        say("      **款 `3`**　`cum_S`（入）＝ %r ／ `W_prev` ＝ %r ／ `W_near`（回傳）＝ %r"
            " ／ `G` ＝ %r ／ `S` ＝ %r ／ 解法 ＝ %s"
            % (_f(x["cum_S_in"]), _f(x["W_prev"]), _f(x["W_near"]),
               _f(x["G"]), _f(x["S"]), x["solver"]))
        say("      　`baseline_pt`（＝ 起算點）＝ %s" % _pt(x["baseline_pt"]))
        nd = x["near_dir_in"]
        say("      **款 `2`**　`near_dir`（入·**`allocation_dir` 槽**）＝ %s ／ `allocation_dir`（入）＝ %s ／"
            " `_alloc_dir_used`（出）＝ %s"
            % ("None" if nd is None else _pt(nd),
               _pt(x["alloc_dir_in"]), _pt(x["alloc_dir_used"])))
        # ── 自我驗證閘 `(iv)`：`rot90` 之語意以該宗之**實邊**驗之 ──────────
        lu = _rot90(x["alloc_dir_used"])
        bc = _best_edge_cos(x["cut_coords"], lu) if lu else None
        say("      　🔒 **閘 `(iv)`**　`rot90(_alloc_dir_used)` ＝ %s ／ 與該宗 `cut_coords`（%d 點）"
            "之**實邊**最平行者之 `|cos|` ＝ **%r**（須 ≥ 1 − 1e-6）⇒ %s"
            % (_pt(lu), len(x["cut_coords"]), bc,
               "✅" if (bc is not None and bc >= 1 - 1e-6) else "🔴"))
        if lu is not None and (bc is None or bc < 1 - 1e-6):
            red("閘 `(iv)` 不過（`%s/%s` idx `%s`）⇒ `rot90` 之語意未經實邊坐實 ⇒ ⛔ 據款 `2` 之對拍"
                % (x["blk"], x["side"], x["idx"]))
        if nd is not None and su is not None and x["baseline_pt"] is not None:
            ndu = _rot90(nd)                      # 🔑 **線向 ＝ rot90(槽向量)**（⛔ 逕取槽向量）
            A = (_f(x["baseline_pt"][0]), _f(x["baseline_pt"][1]))
            cosv = abs(ndu[0] * su[0] + ndu[1] * su[1])
            say("      　**近側界之線**：錨 ＝ `baseline_pt` %s ／ **線向** ＝ `rot90(near_dir)` ＝ %s"
                "（⛔ 逕取 `near_dir` ＝ %s·其為槽向量）" % (_pt(A), _pt(ndu), _pt(_unit(nd))))
            nf = _line_x(A, ndu, F1, dh) if (F1 and dh) else None
            nb = _line_x(A, ndu, bpt, bdir) if (bpt and bdir) else None
            say("      　二端點：∩FRONT∞ ＝ %s ／ ∩BASELINE∞ ＝ %s" % (_pt(nf), _pt(nb)))
            tf = _line_x(tp, su, F1, dh) if (F1 and dh) else None
            tb = _line_x(tp, su, bpt, bdir) if (bpt and bdir) else None
            say("      　**與遠側境界線之逐位對拍**：`|cos|` ＝ **%r** ／ `|cos| − 1` ＝ **%r**"
                % (cosv, cosv - 1.0))
            say("      　垂距（近側界之錨 → 遠側境界線）＝ **%r**" % _dist_pt_line(A, tp, su))
            if nf and tf:
                say("      　端點差 ∩FRONT ＝ (%r, %r)" % (nf[0] - tf[0], nf[1] - tf[1]))
            if nb and tb:
                say("      　端點差 ∩BASELINE ＝ (%r, %r)" % (nb[0] - tb[0], nb[1] - tb[1]))
        elif nd is None:
            say("      　🔑 `near_dir` ＝ **`None`** ⇒ `_block_strip` 走**單線路徑**"
                "（二切邊共用 `n_hat = rot90(allocation_dir)`）⇒ **近側界 ∥ALLOCLINE**")
    return rows


def main():
    say("=" * W)
    say("【`W-G.9-290` `§三`】winner 側之第 1 宗如何取得其**近側界** ／ 二態之路徑分歧點"
        " —— 🛑 **純現查·出艙即止**")
    say("=" * W)
    say("🔒 **包裹點**（自碼面現查·⛔ 推定）＝ `ns[\"_solve_G_one\"]`——`_alloc_dir_used` 係於該函式內"
        "設於其回傳上（`app.py:14014`／`:14029`），`solve_G_binary` 之回傳**尚無**該欄。")

    allseg = []
    for sb in SBS:
        d = drive(sb)
        seg = analyse(sb, d)
        allseg.append((sb, d, seg))
        # 🩸 **本批自捕 `2`**：單 `§三-1` 稱 `R2/left@3.5m` 為「winner 側」，而當場重量得其
        #   `forced` ＝ **True** ⇒ **該格實為 `forced` 態**。依 `常規二` 取保守項：
        #   **併量**單所指之格**與**一格**真正之 winner**（`forced` ＝ `False`·當場自 `fo` 表選），
        #   二者並報·⛔ 擇一、⛔ 改單。
        if sb == 0.0:
            detail(sb, d, seg, "R2", "left", "🔑 **真正之 winner 態**（`forced` ＝ `False`·當場重量）")
            detail(sb, d, seg, "R4", "left", "**`forced` 態**")
        else:
            detail(sb, d, seg, "R2", "left",
                   "🔴 **單 `§三-1` 所稱之「winner 側」——當場重量得其 `forced` ＝ `True`**")
            detail(sb, d, seg, "R4", "left", "**`forced` 態**")

    say("")
    say("=" * W)
    say("【判別力二造（`§三` 款 `7`）】")
    say("=" * W)
    n_true = 0
    for sb, d, seg in allseg:
        for r in seg:
            if r.get("idx") == 1:
                n_true += 1
    say("   `(1)` [必命中] `is_second_after_corner` 為真之格數（＝ 碼側 idx `1` 之筆）＝ **%d**"
        "（須 ≥ 1）⇒ %s" % (n_true, "✅" if n_true >= 1 else "🔴 **loud**·⛔ 以空集充綠"))
    if n_true < 1:
        red("判別力造 `(1)` 不成立 ⇒ 器紅、停")
    # [必為零]：**執行期組出**之人造名（字面⛔ 出艙）
    fake = "is_second_after_corner_" + str(sum(ord(c) for c in "wg9290") % 7) + "x"
    hit = 0
    for sb, d, seg in allseg:
        for r in seg:
            if fake in str(r.get("id") or "") or fake in str(r.get("blk") or ""):
                hit += 1
    say("   `(2)` [必為零] 一**執行期組出**之人造名（字面⛔ 出艙·`GB-147`·**已先驗其於現母體命中為 `0`**）"
        " ⇒ 命中 **%d**（須 `0`）⇒ %s" % (hit, "✅" if hit == 0 else "🔴"))
    if hit:
        red("判別力造 `(2)` 不成立")

    say("")
    say("🛑 **出艙即止**：⛔ 判 `forced` 側應否走同一路、⛔ 擬任何實作形、⛔ 改碼一字、"
        "⛔ 鑄任何號、⛔ 解除或收窄 `GB-170`、⛔ 提修法主張、⛔ 呈 KL。")
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
