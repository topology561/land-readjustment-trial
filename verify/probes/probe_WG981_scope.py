# -*- coding: utf-8 -*-
r"""**W-G.9-81 §二 A 組**：閉式之**射程**——凸性／補 `s` 軸／`34` 列歸因／`α` 相消之充要條件。

## 受詞（施工單 `W-G.9-81` §二）
- **A-1** 六街廓 × 兩情境之**凸性**（`block.equals(convex_hull)`）＋ 凹陷佔比；🔒 附 **L 形**負對照。
- **A-2** 補 `s` 軸（🔒 **母體 ＝ 86**·⛔ 非 67）——必答「`越界量_s > 0` 者 ＝ ?」。
- **A-3** `P6` 之 **34 列**逐列歸因（**甲**＝`s` 越界／**乙**＝外接盒 ⊋ 真多邊形／**丙**＝其他）。
- **A-4** `α` 相消之**充要條件**：`⟨û_j,m̂⟩ / sinα = ±1 ⟺ û_k ∥ n̂`（🔒 母體三項更正）。
- **A-5** **二軸閉式**之重測（`s` ∧ `t`）＋ 🔒 **負對照**（只有 `t` 條件·須仍為 34）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫下）
本探針之受詞是「**閉式為何多判 34 列**」。
其瑕若偏向歸因於「**街廓非凸**」⇒ 閉式本身無過 ⇒ 結論**安靜**、閉式續用。
其瑕若偏向歸因於「**閉式漏了 `s` 軸**」⇒ **要求改式** ⇒ **會吵**。
⇒ 🔒 **事前選定：偏向判「閉式不足」**——凡一列之不一致可由二因並解者，
   **一律先歸「甲（`s` 越界）」並具名**，⛔ 不先歸「乙（非凸）」。

## 🔒 恆等式（承 `W-G.9-80`·`VR-039` 二判為**坐實**·⛔ 中途不換）
```
s*   = d_signed / sinα          d_signed = cross(p_k − p_j, û_k)   sinα = cross(û_j, û_k)
t_X  = t(p_j) + s* · ⟨û_j, n̂⟩                    n̂ = rot90(m̂)   （⛔ 不除 denom）
s_X  = s(p_j) + s* · ⟨û_j, m̂⟩ / denom            m̂, denom = _strip_axis(d_hat, alloc)
```

## 🔒 常設第 9 條（`自誤 82`·施工單 §七-9）：**門檻須先出艙被測量之量級與其 `ulp`**
本檔之殘差一律併印 **`殘差 / math.ulp(|量|)`**；⛔ 不設低於機器解析度之絕對門檻。

## 🔒 常設第 10 條（`自誤 81`·節 105·施工單 §七-10）：**表尾須印機器可讀之母體行**
每一表末印 `POPULATION= / PRINTED= / SUPPRESSED=`；`PRINTED ≠ POPULATION` 而結論採 `PRINTED` 者，
**本探針自身應紅**（⛔ 不留給讀者對帳）。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修任何生產碼；⛔ 不重烤／不換圖；⛔ 不以擬合代替恆等式；
⛔ 不 shim `S`；⛔ 不接入 `run_all`；⛔ 不下「這是 bug」之結論。
"""
import contextlib
import io
import itertools
import math
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

from shapely.geometry import Polygon as SPoly, Point as SPoint      # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210
SWEEP_DEG = [-8, -6, -4, -2, 0, 2, 4, 6, 8, 12, 16, 20]
TOL_PAR = 1e-12          # A-4：`|cross(û_k, n̂)|` 之平行門檻（施工單所令）
TOL_RATIO = 1e-9         # A-4：`| |比值| − 1 |` 之門檻（施工單所令）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG981_scope_%s.log" % COMMIT)


def _u(v):
    a = np.asarray(v, dtype=float)[:2]
    n = float(np.linalg.norm(a))
    return None if n < 1e-15 else a / n


def _rot90(v):
    a = np.asarray(v, dtype=float)[:2]
    return np.array([-a[1], a[0]])


def _cross(a, b):
    return float(a[0] * b[1] - a[1] * b[0])


def _bitsame(u, v):
    if u is None or v is None:
        return False
    a = np.asarray(u, dtype=float)[:2]
    b = np.asarray(v, dtype=float)[:2]
    return bool(np.array_equal(a, b) or np.array_equal(a, -b))


def _line_cross(q1, d1, q2, d2):
    a, b = _u(d1), _u(d2)
    if a is None or b is None:
        return None
    den = _cross(a, b)
    if abs(den) < 1e-15:
        return None
    w = np.asarray(q2, dtype=float)[:2] - np.asarray(q1, dtype=float)[:2]
    return np.asarray(q1, dtype=float)[:2] + (_cross(w, b) / den) * a


def _poly(coords):
    try:
        if coords is None or len(coords) < 3:
            return None
        p = SPoly([(float(c[0]), float(c[1])) for c in coords])
        if not p.is_valid:
            p = p.buffer(0)
        return None if (p is None or p.is_empty) else p
    except Exception:                                               # noqa: BLE001
        return None


def _ulp_ratio(res, val):
    u = math.ulp(abs(val)) if abs(val) > 0 else math.ulp(1.0)
    return abs(res) / u if u > 0 else float("inf")


# ── 【0】量測器自檢 ─────────────────────────────────────────────────────
def selfcheck(P):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·各項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    v = np.array([0.3, 0.7])
    v_ulp = np.array([np.nextafter(v[0], 1.0), v[1]])
    r1 = _bitsame(v, v.copy()) and _bitsame(v, -v) and not _bitsame(v, v_ulp)
    ok &= r1
    P("  ① 逐位相同：同值/反向=True／**差 1 ulp**(%.3e)=%s(期望 False) ⇒ %s"
      % (float(v_ulp[0] - v[0]), _bitsame(v, v_ulp), "PASS" if r1 else "🔴 FAIL"))

    # ② 🔒 凸性判定之**負對照**（人工 L 形·施工單 A-1 所令）
    Lsh = SPoly([(0, 0), (10, 0), (10, 4), (4, 4), (4, 10), (0, 10)])
    sq = SPoly([(0, 0), (10, 0), (10, 10), (0, 10)])
    e_L = Lsh.equals(Lsh.convex_hull)
    e_sq = sq.equals(sq.convex_hull)
    dent = 1.0 - Lsh.area / Lsh.convex_hull.area
    r2 = (not e_L) and e_sq and dent > 0
    ok &= r2
    P("  ② 凸性判定：**L 形** equals(hull)=%s(**期望 False**)·凹陷佔比=%.6f(>0)／方形 equals=%s(期望 True) ⇒ %s"
      % (e_L, dent, e_sq, "PASS" if r2 else "🔴 FAIL"))

    # ③ ⟨û,m̂⟩ 與 cross(û,n̂) 之恆等（A-4 之代數前提·先於合成證）
    m = np.array([0.6, 0.8]); n = _rot90(m); uj = _u((0.3, -0.9))
    lhs = float(np.dot(uj, m)); rhs = _cross(uj, n)
    r3 = abs(lhs - rhs) < 1e-15
    ok &= r3
    P("  ③ `⟨û,m̂⟩ == cross(û,n̂)`（`n̂=rot90(m̂)`·單位 m̂）：%.15f vs %.15f ⇒ %s"
      % (lhs, rhs, "PASS" if r3 else "🔴 FAIL"))
    m2 = np.array([1.2, 1.6])                    # 非單位 m̂ ⇒ 二者仍相等（線性）
    r3b = abs(float(np.dot(uj, m2)) - _cross(uj, _rot90(m2))) < 1e-15
    ok &= r3b
    P("     對照（非單位 m̂·|m̂|=2）：仍相等 ⇒ %s（⇒ 該恆等⛔ 不依賴 m̂ 之長度）"
      % ("PASS" if r3b else "🔴 FAIL"))

    # ④ ulp 之機制（常設第 9 條）
    r4 = abs(math.ulp(1.585110e+09) - 2.384185791015625e-07) < 1e-20
    ok &= r4
    P("  ④ `math.ulp(1.585110e+09)` = %.6e（期望 2.384186e-07·＝`VR-039` 二所載）⇒ %s"
      % (math.ulp(1.585110e+09), "PASS" if r4 else "🔴 FAIL"))

    P("  ⇒ 量測器自檢：%s" % ("PASS" if ok else "🔴 FAIL（⛔ 以下量測結果不得採信）"))
    return ok


# ── spy ────────────────────────────────────────────────────────────────
SOLVE = {}
CAP = []
CUR = {"setback": None, "theta": None}


def spy_solve(orig):
    def _s(**kw):
        res, label = orig(**kw)
        try:
            SOLVE[id(res)] = {"is_corner": bool(kw.get("is_corner")),
                              "near_dir": kw.get("near_dir"),
                              "alloc_used": res.get("_alloc_dir_used"),
                              "baseline_pt": kw.get("baseline_pt"),
                              "d_hat": kw.get("d_hat"),
                              "S": res.get("S_raw", res.get("S"))}
        except Exception as e:                                      # noqa: BLE001
            SOLVE[id(res)] = {"err": "%s: %s" % (type(e).__name__, e)}
        return res, label
    return _s


def spy_pool(orig):
    def _s(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
           _label='', _depth=None, _verbose=True):
        names, ress, align = None, None, "🔴 未對上"
        try:
            lv = sys._getframe(1).f_locals
            lr, rr = lv.get('left_results'), lv.get('right_results')
            ap = lv.get('allocated_polys')
            if isinstance(lr, list) and isinstance(rr, list):
                nm, rs = [], []
                for _entry, _res in (lr + rr):
                    if _poly((_res or {}).get('cut_coords') or []) is not None:
                        nm.append(((_entry or {}).get('tp') or {}).get('暫編地號', '?'))
                        rs.append(_res)
                if len(nm) == len(list(biz_polys or [])):
                    names, ress = nm, rs
                    align = "✅ 逐位對齊" if ap is biz_polys else "⚠️ 數相等但非同一物件"
        except Exception as e:                                      # noqa: BLE001
            align = "🔴 未對上（%s: %s）" % (type(e).__name__, e)
        CAP.append({"setback": CUR["setback"], "theta": CUR["theta"], "label": _label,
                    "biz": list(biz_polys or []), "depth": _depth, "d_hat": d_hat,
                    "corner_pt": corner_pt, "alloc": allocation_dir, "block": block_poly,
                    "names": names, "ress": ress, "align": align, "exc": None})
        try:
            return orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                        _label=_label, _depth=_depth, _verbose=_verbose)
        except Exception as e:                                      # noqa: BLE001
            CAP[-1]["exc"] = "%s: %s" % (type(e).__name__, e)
            raise
    return _s


def faces_of(info):
    if not info or info.get("err"):
        return (None, None)
    au, nd = info.get("alloc_used"), info.get("near_dir")
    bp, dh, S = info.get("baseline_pt"), info.get("d_hat"), info.get("S")
    if au is None or bp is None or dh is None or S is None:
        return (None, None)
    n_pt = np.asarray(bp, dtype=float)[:2]
    return ((_rot90(nd if nd is not None else au), n_pt),
            (_rot90(au), n_pt + float(S) * _u(dh)))


def analyse_cell(rec, strip_axis):
    n = len(rec["biz"])
    m_hat, denom = strip_axis(rec["d_hat"], rec["alloc"])
    m_hat = np.asarray(m_hat, dtype=float)[:2]
    n_hat = _rot90(m_hat)
    bp0 = np.asarray(rec["corner_pt"], dtype=float)[:2]

    def s_of(p):
        return float(np.dot(np.asarray(p, dtype=float)[:2] - bp0, m_hat)) / denom

    def t_of(p):
        return float(np.dot(np.asarray(p, dtype=float)[:2] - bp0, n_hat))

    bx = list(rec["block"].exterior.coords) if rec["block"] is not None else []
    s_all = [s_of(c) for c in bx] or [float("nan")]
    t_all = [t_of(c) for c in bx] or [float("nan")]
    fc = []
    for i in range(n):
        r = (rec["ress"] or [None] * (i + 1))[i]
        fc.append((faces_of(SOLVE.get(id(r))), SOLVE.get(id(r))))
    rows = []
    for j, k in itertools.combinations(range(n), 2):
        (nfj, ffj), _ = fc[j]
        (nfk, ffk), _ = fc[k]
        row = {"j": j, "k": k, "d": k - j, "ok": False}
        if ffj is None or nfk is None:
            rows.append(row); continue
        uj, uk = _u(ffj[0]), _u(nfk[0])
        pj, pk = np.asarray(ffj[1], float)[:2], np.asarray(nfk[1], float)[:2]
        if uj is None or uk is None or _bitsame(uj, uk):
            rows.append(row); continue
        sin_a = _cross(uj, uk)
        if abs(sin_a) < 1e-15:
            rows.append(row); continue
        d_signed = _cross(pk - pj, uk)
        s_star = d_signed / sin_a
        dot_jn = float(np.dot(uj, n_hat))
        dot_jm = float(np.dot(uj, m_hat))
        cr_jn = _cross(uj, n_hat)                    # 🔒 A-4：應 == dot_jm
        cr_kn = _cross(uk, n_hat)                    # 🔒 A-4：û_k 偏離 n̂ 之量
        t_pj, s_pj = t_of(pj), s_of(pj)
        t_pred = t_pj + s_star * dot_jn
        s_pred = s_pj + s_star * dot_jm / denom
        X = _line_cross(pj, uj, pk, uk)
        t_meas = t_of(X) if X is not None else float("nan")
        s_meas = s_of(X) if X is not None else float("nan")
        inside = bool(X is not None and rec["block"] is not None
                      and rec["block"].contains(SPoint(float(X[0]), float(X[1]))))
        row.update({"ok": True, "uj": uj, "uk": uk, "sin_a": sin_a,
                    "d_signed": d_signed, "s_star": s_star,
                    "dot_jn": dot_jn, "dot_jm": dot_jm, "cr_jn": cr_jn, "cr_kn": cr_kn,
                    "t_pj": t_pj, "s_pj": s_pj, "t_pred": t_pred, "t_meas": t_meas,
                    "s_pred": s_pred, "s_meas": s_meas,
                    "res_t": t_pred - t_meas, "res_s": s_pred - s_meas,
                    "ratio": dot_jm / sin_a, "inside": inside, "X": X,
                    "area": float(rec["biz"][j].intersection(rec["biz"][k]).area)})
        rows.append(row)
    meta = {"n": n, "s_lo": min(s_all), "s_hi": max(s_all),
            "t_lo": min(t_all), "t_hi": max(t_all), "denom": denom,
            "corners": tuple(i for i in range(n) if (fc[i][1] or {}).get("is_corner"))}
    return meta, rows


def pred_t(row, meta):
    """`W-G.9-80` 之單軸（`t`）謂詞。"""
    return (meta["t_lo"] - row["t_pj"]) <= row["s_star"] * row["dot_jn"] <= (meta["t_hi"] - row["t_pj"])


def pred_s(row, meta):
    """🆕 `s` 條件（⛔ 輸入仍在白名單內）。"""
    sx = row["s_pj"] + row["s_star"] * row["dot_jm"] / meta["denom"]
    return meta["s_lo"] <= sx <= meta["s_hi"]


def pred_2ax(row, meta):
    return pred_s(row, meta) and pred_t(row, meta)


def over_s(row, meta):
    """`越界量_s`（帶號·正 ＝ 在外）。"""
    sx = row["s_pj"] + row["s_star"] * row["dot_jm"] / meta["denom"]
    return max(meta["s_lo"] - sx, sx - meta["s_hi"])


def main():                                                         # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    RED = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    def POP(pop, printed, tag):
        """🔒 常設第 10 條：機器可讀之母體行；採 PRINTED 為結論者本探針應紅。"""
        P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # %s" % (pop, printed, pop - printed, tag))
        if printed != pop:
            P("     ⚠️ `PRINTED ≠ POPULATION` ⇒ 🔒 **本表之結論一律以 `POPULATION` 為分母**"
              "（⛔ 表身列數不得作為母體·節 105）")

    P("=" * W)
    P("【W-G.9-81 §二 A 組】閉式之射程——凸性／補 s 軸／34 列歸因／α 相消充要條件（⛔ 只量不修）")
    P("=" * W)
    import shapely
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s" % (shapely.__version__, shapely.geos_version))
    P("  🔒 A-0 **事前選定：偏向判「閉式不足」**（可二解者先歸甲）⇒ 錯誤方向**會吵**。")
    P("  🔒 常設 9：殘差一律併印 `殘差/ulp`；常設 10：每表末印 POPULATION/PRINTED/SUPPRESSED。")

    ns, fake_st = harvest()
    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    strip_axis = ns["_strip_axis"]
    snapshot = rv.load_snapshot()
    o_solve, o_pool = ns["_solve_G_one"], ns["_pool_strips_for_block"]
    o_fcad = ns["_first_corner_alloc_dir"]

    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)

    def one_pass():
        for setback in (0.0, 3.5):
            CUR["setback"] = setback
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, wins, forced = run_corner_pk(
                ns, fake_st, cb_all, cad, params, temp_p, build_p, setback, snapshot=snapshot)
            for lbl in blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass

    P("")
    P("【驅動·第一趟（真實）】R1–R6 × 兩情境——街廓母體 = %s" % blks)
    P("-" * W)
    ns["_solve_G_one"], ns["_pool_strips_for_block"] = spy_solve(o_solve), spy_pool(o_pool)
    try:
        one_pass()
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(CAP)
    CELL = [(rec,) + analyse_cell(rec, strip_axis) for rec in REAL]
    ALL = [(rec, meta, r) for rec, meta, rows in CELL for r in rows if r.get("ok")]
    P("  攔截 %d 格；**可算交點之對（母體）＝ %d**（🔒 承 `W-G.9-80`·⛔ 非 67）" % (len(REAL), len(ALL)))

    # ── §C  A-1 凸性 ───────────────────────────────────────────────────
    P("")
    P("【A-1】六街廓 × 兩情境之**凸性**")
    P("-" * W)
    P("  %-6s %-5s %8s %8s %14s %14s %14s %-10s"
      % ("情境", "街廓", "頂點數", "is_valid", "block.area", "hull.area", "凹陷佔比", "equals(hull)"))
    ncvx = 0
    for rec, meta, rows in CELL:
        b = rec["block"]
        if b is None:
            P("  %-6s %-5s  🔴 block 缺" % ("%gm" % rec["setback"], rec["label"]))
            continue
        h = b.convex_hull
        dent = 1.0 - float(b.area) / float(h.area) if h.area > 0 else float("nan")
        eq = bool(b.equals(h))
        ncvx += int(not eq)
        P("  %-6s %-5s %8d %8s %14.4f %14.4f %14.6e %-10s"
          % ("%gm" % rec["setback"], rec["label"], len(b.exterior.coords) - 1,
             b.is_valid, float(b.area), float(h.area), dent, "**是（凸）**" if eq else "🔴 **否（非凸）**"))
    POP(len(CELL), len(CELL), "A-1 凸性（12 格全列）")
    P("  ⇒ **非凸之格數 ＝ %d ／ %d**" % (ncvx, len(CELL)))

    # ── §D  A-2 補 s 軸 ────────────────────────────────────────────────
    P("")
    P("【A-2】補 `s` 軸（🔒 母體 ＝ %d·⛔ 非 67）——必答：`越界量_s > 0` 者 ＝ ?" % len(ALL))
    P("-" * W)
    P("  %-6s %-5s %-4s %-4s %11s %11s %12s %12s %10s %-22s %11s"
      % ("情境", "街廓", "j", "k", "s(p_j)", "⟨û_j,m̂⟩", "預測 s_X", "實測 s_X", "殘差/ulp",
         "街廓 s 域", "**越界量_s**"))
    outs = [(rec, meta, r, over_s(r, meta)) for rec, meta, r in ALL]
    pos = [x for x in outs if x[3] > 0]
    shown = sorted(outs, key=lambda x: -x[3])[:16]
    for rec, meta, r, ov in shown:
        P("  %-6s %-5s %-4d %-4d %11.4f %11.6f %12.4f %12.4f %10.2f [%8.3f,%8.3f] %11.4f"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], r["s_pj"], r["dot_jm"],
             r["s_pred"], r["s_meas"], _ulp_ratio(r["res_s"], r["s_meas"]),
             meta["s_lo"], meta["s_hi"], ov))
    POP(len(outs), len(shown), "A-2 逐對（依 `越界量_s` 遞減·僅列前 16）")
    P("  🔴 **必答：`越界量_s > 0` 者 ＝ %d ／ %d**" % (len(pos), len(outs)))
    if pos:
        P("     逐對具名（全列·⛔ 非取樣）：")
        for rec, meta, r, ov in sorted(pos, key=lambda x: -x[3]):
            P("       [%gm] %-4s (%d,%d)  s_X=%.4f  s 域=[%.3f,%.3f]  越界量_s=%.4f  contains=%s"
              % (rec["setback"], rec["label"], r["j"], r["k"], r["s_meas"],
                 meta["s_lo"], meta["s_hi"], ov, r["inside"]))
    ru = [_ulp_ratio(r["res_s"], r["s_meas"]) for _, _, r in ALL]
    P("  🔒 `s` 恆等式之 **`殘差/ulp`**：極大 %.2f ／ 中位 %.2f ／ 最小 %.2f（🔒 常設 9）"
      % (max(ru), sorted(ru)[len(ru) // 2], min(ru)))

    # ── §F  A-4 α 相消之充要條件 ───────────────────────────────────────
    P("")
    P("【A-4】`α` 相消之**充要條件**：`⟨û_j,m̂⟩ / sinα = ±1　⟺　û_k ∥ n̂`")
    P("-" * W)
    P("  🔒 **母體之三項更正（施工單所令）**：① 取 `|比值|`（原 `[0.9,1.1]` 係帶號區間·發單側之過）")
    P("     ② 例外類改為「`û_k` 不 ∥ `n̂`」（⛔ 非「`宗k` 亦為街角宗」）③ **排除 `⟨û_j,m̂⟩ = 0` 之對**")
    zero_jm = [(rec, meta, r) for rec, meta, r in ALL if abs(r["dot_jm"]) < 1e-15]
    base = [(rec, meta, r) for rec, meta, r in ALL if abs(r["dot_jm"]) >= 1e-15]
    P("  🔒 ③ 之排除：`⟨û_j,m̂⟩ = 0` 之對 ＝ **%d**（逐對具名·⛔ 自始不屬母體）：" % len(zero_jm))
    for rec, meta, r in zero_jm:
        P("       [%gm] %-4s (%d,%d)  ⟨û_j,m̂⟩=%.3e" % (rec["setback"], rec["label"], r["j"], r["k"], r["dot_jm"]))
    P("  🔒 ⟨û_j,m̂⟩ == cross(û_j,n̂) 之逐對複驗：|差| 極大 = %.3e（自檢 ③ 已先證其代數）"
      % max(abs(r["dot_jm"] - r["cr_jn"]) for _, _, r in ALL))
    P("  %-6s %-5s %-4s %-4s %13s %13s %12s %-10s %-10s"
      % ("情境", "街廓", "j", "k", "|cross(û_k,n̂)|", "**|比值|**", "||比值|−1|", "∥n̂?", "判"))
    agree = dis = 0
    dis_rows = []
    for rec, meta, r in base:
        par = abs(r["cr_kn"]) <= TOL_PAR
        one = abs(abs(r["ratio"]) - 1.0) <= TOL_RATIO
        if par == one:
            agree += 1
        else:
            dis += 1
            dis_rows.append((rec, meta, r, par, one))
    show = dis_rows[:10] if dis_rows else [(rec, meta, r, abs(r["cr_kn"]) <= TOL_PAR,
                                            abs(abs(r["ratio"]) - 1.0) <= TOL_RATIO)
                                           for rec, meta, r in base[:10]]
    for rec, meta, r, par, one in show:
        P("  %-6s %-5s %-4d %-4d %13.3e %13.9f %12.3e %-10s %-10s"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], abs(r["cr_kn"]),
             abs(r["ratio"]), abs(abs(r["ratio"]) - 1.0), "是" if par else "否",
             "✅ 一致" if par == one else "🔴 **不一致**"))
    POP(len(base), len(show), "A-4 逐對（更正後母體·僅列不一致者或前 10）")
    P("  ⇒ 更正後母體 **%d**（＝ %d − %d 之 `⟨û_j,m̂⟩=0`）：**一致 %d ／ 不一致 %d** ⇒ %s"
      % (len(base), len(ALL), len(zero_jm), agree, dis,
         "✅ **對稱差 ＝ 空集**（`P5` 成立）" if dis == 0 else "🔴 **不成立**·逐對已具名"))
    npar = sum(1 for rec, meta, r in base if abs(r["cr_kn"]) <= TOL_PAR)
    P("  🔒 其中 `û_k ∥ n̂` 者 **%d** ／ 不 ∥ 者 **%d**（＝ 更正後之**例外類**）" % (npar, len(base) - npar))

    # ── §G  A-5 二軸閉式 ＋ 掃描（含 A-3 歸因）─────────────────────────
    P("")
    P("【A-5】**二軸閉式**（`s` ∧ `t`）於 %d 真實對之重測" % len(ALL))
    P("-" * W)
    a2 = sum(1 for rec, meta, r in ALL if pred_2ax(r, meta) == r["inside"])
    a1 = sum(1 for rec, meta, r in ALL if pred_t(r, meta) == r["inside"])
    P("  二軸式（`s ∧ t`）：一致 **%d** ／ 不一致 **%d**" % (a2, len(ALL) - a2))
    P("  單軸式（僅 `t`·＝ `W-G.9-80`）：一致 **%d** ／ 不一致 **%d**（🔒 負對照）" % (a1, len(ALL) - a1))
    POP(len(ALL), len(ALL), "A-5 真實對（全量計入·⛔ 無列印濾網）")

    P("")
    P("【A-3 ＋ A-5】`θ` 掃描 %s ——34 列歸因 ＋ 二軸式重測"
      % ", ".join("%d°" % t for t in SWEEP_DEG))
    P("-" * W)
    ss_ = fake_st.session_state
    slbs = (ss_.get('f3_cad_side_lines_by_side', {}) or {})
    adir = (ss_.get('f3_cad_alloc_dir', {}) or {})
    alloc_axis = ns["alloc_normal_axis"]

    def blk_of_mid(mid):
        m = np.asarray(mid, dtype=float)[:2]
        for lbl in slbs:
            for w in ('left', 'right'):
                sd = (slbs.get(lbl) or {}).get(w)
                if sd and sd.get('mid') is not None:
                    if float(np.linalg.norm(np.asarray(sd['mid'], dtype=float)[:2] - m)) < 1e-6:
                        return lbl
        return None

    def make_fcad(theta_deg):
        def _f(side_mid):
            lbl = blk_of_mid(side_mid)
            if lbl is None or adir.get(lbl) is None:
                raise RuntimeError("🔴 掃描 shim：side_mid 查無街廓／該塊無 ALLOC（no-silent）")
            b = _u(alloc_axis(adir[lbl]))
            th = math.radians(theta_deg)
            ct, st_ = math.cos(th), math.sin(th)
            return (float(b[0] * ct - b[1] * st_), float(b[0] * st_ + b[1] * ct))
        return _f

    SW = {"t_ag": 0, "t_dis": 0, "x_ag": 0, "x_dis": 0}
    ATTR = {"甲": 0, "乙": 0, "丙": 0}
    attr_rows = []
    dis_t_rows = []
    for th in SWEEP_DEG:
        CAP.clear()
        CUR["theta"] = th
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = spy_solve(o_solve), spy_pool(o_pool)
        ns["_first_corner_alloc_dir"] = make_fcad(th)
        try:
            one_pass()
        finally:
            ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
            ns["_first_corner_alloc_dir"] = o_fcad
        for rec in CAP:
            meta, rows = analyse_cell(rec, strip_axis)
            ok = [r for r in rows if r.get("ok")]
            meas = sum(1 for r in ok if r["inside"] and r["d"] >= 2)
            p_t = sum(1 for r in ok if pred_t(r, meta) and r["d"] >= 2)
            p_x = sum(1 for r in ok if pred_2ax(r, meta) and r["d"] >= 2)
            if (meas >= 1) == (p_t >= 1):
                SW["t_ag"] += 1
            else:
                SW["t_dis"] += 1
                dis_t_rows.append((th, rec["setback"], rec["label"], meas, p_t, p_x))
                # 🔒 A-3 歸因：對該列每一個「單軸判在內」之對逐對歸類
                for r in ok:
                    if not (pred_t(r, meta) and r["d"] >= 2):
                        continue
                    ov = over_s(r, meta)
                    bbox_in = (ov <= 0) and pred_t(r, meta)
                    if ov > 0:
                        cls = "甲"                       # A-0：可二解者先歸甲
                    elif bbox_in and not r["inside"]:
                        cls = "乙"
                    else:
                        cls = "丙"
                    ATTR[cls] += 1
                    attr_rows.append((th, rec["setback"], rec["label"], r["j"], r["k"],
                                      r["s_meas"], r["t_meas"], meta, ov, bbox_in, r["inside"], cls))
            if (meas >= 1) == (p_x >= 1):
                SW["x_ag"] += 1
            else:
                SW["x_dis"] += 1
        print("    θ=%d° 完畢" % th, file=sys.stderr)

    P("  🔒 **負對照（單軸·僅 `t`）**：掃描不一致 ＝ **%d**（🔒 施工單期望 **34** ⇒ %s）"
      % (SW["t_dis"], "✅ 相符" if SW["t_dis"] == 34 else "🔴 **不符·具名**"))
    P("  🆕 **二軸式（`s ∧ t`）**：掃描不一致 ＝ **%d** ⇒ %s"
      % (SW["x_dis"],
         "✅ **由 %d 降至 %d**" % (SW["t_dis"], SW["x_dis"]) if SW["x_dis"] < SW["t_dis"]
         else "🔴 **未降低 ⇒ `s` 軸無判別力·具名**"))
    POP(SW["t_ag"] + SW["t_dis"], SW["t_ag"] + SW["t_dis"], "掃描列（12θ × 12 格）")

    P("")
    P("  🔴 **A-3 之逐列歸因**（🔒 三類互斥·和須 ＝ 單軸判在內之對數）")
    P("  %-6s %-6s %-5s %-4s %-4s %11s %13s %11s %-8s %-9s %-6s"
      % ("θ", "情境", "街廓", "j", "k", "s_X", "t_X", "越界量_s", "bbox_in", "contains", "歸類"))
    for th, sb, lb, j, k, sx, tx, meta, ov, bb, ins, cls in attr_rows[:24]:
        P("  %-6s %-6s %-5s %-4d %-4d %11.4f %13.4f %11.4f %-8s %-9s %-6s"
          % ("%d°" % th, "%gm" % sb, lb, j, k, sx, tx, ov, bb, ins, "**%s**" % cls))
    POP(len(attr_rows), min(24, len(attr_rows)), "A-3 歸因（逐對·僅列前 24）")
    tot = ATTR["甲"] + ATTR["乙"] + ATTR["丙"]
    P("  ⇒ **甲（`s` 越界）＝ %d ／ 乙（外接盒 ⊋ 真多邊形）＝ %d ／ 丙（其他）＝ %d**；"
      "和 ＝ %d ／ 逐對母體 ＝ %d ⇒ %s"
      % (ATTR["甲"], ATTR["乙"], ATTR["丙"], tot, len(attr_rows),
         "✅ 相等（`P3` 成立）" if tot == len(attr_rows) else "🔴 **不等 ⇒ 量測器有誤·⛔ 不得出艙歸因**"))
    if ATTR["丙"]:
        P("  🔴 **丙類逐對具名**（⛔ 不得歸入甲乙）：")
        for th, sb, lb, j, k, sx, tx, meta, ov, bb, ins, cls in attr_rows:
            if cls == "丙":
                P("     θ=%d° [%gm] %-4s (%d,%d) s_X=%.4f t_X=%.4f 越界_s=%.4f bbox_in=%s contains=%s"
                  % (th, sb, lb, j, k, sx, tx, ov, bb, ins))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
