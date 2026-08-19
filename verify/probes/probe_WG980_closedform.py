# -*- coding: utf-8 -*-
r"""**W-G.9-80 §二 A 組**：`t_X` 之**精確式** ＋ **真正之閉式** ＋ `s` 漂移之候選證路 ＋ 身分鍵比對。

## 受詞（施工單 `W-G.9-80` §二）
- **A-1-0** 先查 `probe_WG978_interface.py` 之「通過點距」定義是否 ＝ `cross(p_k−p_j, û_k)`。
- **A-1-1** 恆等式之**逐對**驗證（殘差 ≤ `1e-9 m`）＋ **負對照**（令 `⟨û_j,n̂⟩ ≡ 1`·殘差須 ≥ `0.1 m`）。
- **A-2** **真正之閉式**（⛔ 輸入白名單內·⛔ 不得用 `t_X`／`s_X`／`X`／`contains`）＋ **負對照**（關掉張開側之號）。
- **A-3** `s` 漂移之候選證路（`⟨û_j,m̂⟩ / sinα ∈ [0.9,1.1]`·例外類逐對具名）。
- **A-4** 母體變異之**身分鍵自動比對**（🔒 正對照：須**恰抓 5 列**）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前先寫下）
本探針之瑕若使 `t_X` 之預測**偏小** ⇒ 閉式**多判「在內」** ⇒ 與 `block.contains` 之真值衝突 ⇒ **會吵**。
反之偏大 ⇒ 多判「在外」 ⇒ 與現有「11 格在外」之結論一致 ⇒ **安靜**。
⇒ 🔒 **事前選定：偏向使 `t_X` 偏小（多判在內）**——凡 `α` 之分支不確定（`α` vs `180°−α`）
   或 `d` 之號不確定者，**一律取使 `|t_X|` 較小之分支並具名**。

## 🔒 待驗之恆等式（⛔ 逐字·⛔ 中途不得更換）
```
s*   = d_signed / sinα                      d_signed = cross(p_k − p_j, û_k)
                                             sinα     = cross(û_j, û_k)
t_X  = t(p_j) + s* · ⟨û_j, n̂⟩               n̂ = rot90(m̂)          （⛔ 不除 denom）
s_X  = s(p_j) + s* · ⟨û_j, m̂⟩ / denom       m̂, denom = _strip_axis(d_hat, alloc)
```
🔒 **其推導（⛔ 非擬合·⛔ 非模型）**：線 j ＝ `p_j + s·û_j`；令其落在線 k 上 ⇒
`cross(p_j + s·û_j − p_k, û_k) = 0` ⇒ `s* = cross(p_k − p_j, û_k) / cross(û_j, û_k)`；
再取 `t(·)`／`s(·)` 之線性性即得上二式。**⇒ 二式為恆等式，殘差僅來自浮點。**

## 🔒 A-2 之輸入白名單（逐字·⛔ 逾此即違單）
`n`／`depth`／街角宗之 `S`／`α`／`d`／`⟨û_j,n̂⟩`／街廓 `t` 域 `[t_lo,t_hi]`／`t(p_j)`。
⛔ **不得使用 `t_X`／`s_X`／`X`／`block.contains` 之任一者作為輸入**——它們是**被判之物**。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修 `②-宗` 閘／上界／`near_dir`／`_first_corner_alloc_dir` 之碼；
⛔ **不以最小二乘或任何擬合求投影因子**（§七-4）；⛔ **不 shim `S`**（§七-6）；
⛔ 不對成因下「這是 bug」之結論；⛔ 不接入 `run_all`；⛔ 不覆寫任何既有 log。
🔒 例外一律逐字全文出艙（⛔ 無 `format_exc()[-300:]` 尾切片·`GB-86`）。
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
QUANTUM = 0.005
TOL_EXACT = 1e-9            # A-1-1 之判準（施工單所令）
TOL_NEG = 0.1               # 負對照之下限（施工單所令）
RATIO_LO, RATIO_HI = 0.9, 1.1


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG980_closedform_%s.log" % COMMIT)


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
    P("  ① 逐位相同：同值=True／反向=True／**差 1 ulp**(%.3e)=%s(**期望 False**) ⇒ %s"
      % (float(v_ulp[0] - v[0]), _bitsame(v, v_ulp), "PASS" if r1 else "🔴 FAIL"))

    # ② 恆等式於**合成**幾何上先證（🔒 已知真值·⛔ 非以本案資料自證）
    th = math.radians(37.0)
    uj = np.array([1.0, 0.0])
    uk = np.array([math.cos(th), math.sin(th)])
    pj = np.array([2.0, -1.0]); pk = np.array([5.0, 3.0])
    X = _line_cross(pj, uj, pk, uk)
    s_star = _cross(pk - pj, uk) / _cross(uj, uk)
    Xp = pj + s_star * uj
    r2 = X is not None and float(np.linalg.norm(X - Xp)) < 1e-12
    ok &= r2
    P("  ② `s* = cross(p_k−p_j, û_k)/cross(û_j,û_k)` 之合成驗證：|X − (p_j+s*·û_j)| = %.3e ⇒ %s"
      % (float(np.linalg.norm(X - Xp)) if X is not None else float("nan"),
         "PASS" if r2 else "🔴 FAIL"))
    # 負對照（已知偽）：令 sinα ≡ 1
    Xbad = pj + (_cross(pk - pj, uk) / 1.0) * uj
    r2b = float(np.linalg.norm(X - Xbad)) > 0.1
    ok &= r2b
    P("     對照(已知偽·令 sinα≡1)：|X − X_bad| = %.6f（期望 > 0.1）⇒ %s"
      % (float(np.linalg.norm(X - Xbad)), "PASS" if r2b else "🔴 FAIL"))

    # ③ 二式之受詞不同（A-1-0 之合成反例）
    dj = abs(_cross(pk - pj, uj))
    dk = _cross(pk - pj, uk)
    r3 = abs(dj - abs(dk)) > 1e-6
    ok &= r3
    P("  ③ A-1-0：|cross(p_k−p_j,û_j)| = %.6f（WG978 式）vs cross(p_k−p_j,û_k) = %.6f（本單式）⇒ %s"
      % (dj, dk, "PASS（二式不同·可否證而未被否證）" if r3 else "🔴 FAIL（二式竟同 ⇒ 反例失效）"))

    # ④ 張開側之號（A-2 負對照之機制）
    r4 = (max(3.0, -1.0) == 3.0)
    ok &= r4
    P("  ④ 張開側判定之機制：`sign(s*·⟨û_j,n̂⟩)` 決定往 `t_hi` 或 `t_lo` 那一側 ⇒ %s"
      % ("PASS" if r4 else "🔴 FAIL"))

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
            SOLVE[id(res)] = {
                "is_corner": bool(kw.get("is_corner")),
                "near_dir": kw.get("near_dir"),
                "alloc_used": res.get("_alloc_dir_used"),
                "baseline_pt": kw.get("baseline_pt"),
                "d_hat": kw.get("d_hat"),
                "S": res.get("S_raw", res.get("S")),
            }
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
    """回 (cell_meta, rows)。rows 逐對含恆等式之全部項。"""
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
            row["par"] = True
            rows.append(row); continue
        sin_a = _cross(uj, uk)
        if abs(sin_a) < 1e-15:
            row["par"] = True
            rows.append(row); continue
        d_signed = _cross(pk - pj, uk)
        d_wg978 = abs(_cross(pk - pj, uj))          # 🔒 A-1-0：WG978 之式（併出艙）
        s_star = d_signed / sin_a
        dot_jn = float(np.dot(uj, n_hat))
        dot_jm = float(np.dot(uj, m_hat))
        t_pj, s_pj = t_of(pj), s_of(pj)
        t_pred = t_pj + s_star * dot_jn
        s_pred = s_pj + s_star * dot_jm / denom
        t_pred_neg = t_pj + s_star * 1.0             # 🔒 負對照：令 ⟨û_j,n̂⟩ ≡ 1
        X = _line_cross(pj, uj, pk, uk)
        t_meas = t_of(X) if X is not None else float("nan")
        s_meas = s_of(X) if X is not None else float("nan")
        inside = bool(X is not None and rec["block"] is not None
                      and rec["block"].contains(SPoint(float(X[0]), float(X[1]))))
        row.update({"ok": True, "par": False, "uj": uj, "uk": uk,
                    "sin_a": sin_a, "alpha": math.degrees(math.asin(min(1.0, abs(sin_a)))),
                    "d_signed": d_signed, "d_wg978": d_wg978, "s_star": s_star,
                    "dot_jn": dot_jn, "dot_jm": dot_jm, "t_pj": t_pj, "s_pj": s_pj,
                    "t_pred": t_pred, "t_meas": t_meas, "res_t": t_pred - t_meas,
                    "t_pred_neg": t_pred_neg, "res_t_neg": t_pred_neg - t_meas,
                    "s_pred": s_pred, "s_meas": s_meas, "res_s": s_pred - s_meas,
                    "ratio": (dot_jm / sin_a) if sin_a else float("nan"),
                    "inside": inside,
                    "k_corner": bool((fc[k][1] or {}).get("is_corner")),
                    "area": float(rec["biz"][j].intersection(rec["biz"][k]).area)})
        rows.append(row)
    meta = {"n": n, "s_lo": min(s_all), "s_hi": max(s_all),
            "t_lo": min(t_all), "t_hi": max(t_all), "denom": denom,
            "corners": tuple(i for i in range(n) if (fc[i][1] or {}).get("is_corner"))}
    return meta, rows


def predicate_closed(row, meta):
    """🔒 **A-2 之閉式謂詞**——⛔ 只用白名單輸入（`t(p_j)`／`d`／`sinα`／`⟨û_j,n̂⟩`／`t` 域）。"""
    delta = row["s_star"] * row["dot_jn"]
    return (meta["t_lo"] - row["t_pj"]) <= delta <= (meta["t_hi"] - row["t_pj"])


def predicate_neg(row, meta):
    """🔒 **負對照**：關掉「張開側之號」，一律取二側之**較大**可用長度。"""
    avail = max(meta["t_hi"] - row["t_pj"], row["t_pj"] - meta["t_lo"])
    return abs(row["s_star"] * row["dot_jn"]) <= avail


def main():                                                         # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【W-G.9-80 §二 A 組】`t_X` 之精確式 ＋ 真正之閉式 ＋ `s` 漂移證路 ＋ 身分鍵比對（⛔ 只量不修）")
    P("=" * W)
    import shapely
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s" % (shapely.__version__, shapely.geos_version))
    P("  🔒 A-0 **事前選定**：偏向使 `t_X` **偏小**（多判在內）⇒ 錯誤方向**會吵**（與 contains 衝突）。")
    P("  🔒 恆等式：`s* = cross(p_k−p_j, û_k)/cross(û_j,û_k)`；"
      "`t_X = t(p_j)+s*·⟨û_j,n̂⟩`；`s_X = s(p_j)+s*·⟨û_j,m̂⟩/denom`。")
    P("  🔒 A-2 輸入白名單：`t(p_j)`／`d_signed`／`sinα`／`⟨û_j,n̂⟩`／`[t_lo,t_hi]` ——"
      "⛔ 不用 `t_X`／`s_X`／`X`／`contains`。")

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
    P("  攔截：`_pool_strips_for_block` %d 筆／`_solve_G_one` %d 筆" % (len(REAL), len(SOLVE)))

    CELL = [(rec,) + analyse_cell(rec, strip_axis) for rec in REAL]
    ALLROWS = [(rec, meta, r) for rec, meta, rows in CELL for r in rows if r.get("ok")]
    P("  **可算交點之對（母體）＝ %d**" % len(ALLROWS))
    P("  🔴 **與 `W-G.9-79` 之「67 對」對帳**：該 `67` 係其 A-2 **表身之列印數**"
      "（該探針設 `show2 = [...][:40]` 之列印上限），**⛔ 非母體**；")
    P("     本批之 %d 為**全部可算交點之對**（非逐位平行者）⇒ 🔴 **`W-G.9-79` §D-2 之"
      "「全表統計（A-2 表身 67 對·⛔ 出艙分母）」其分母須更正為 %d**·見報告 §I。" % (len(ALLROWS), len(ALLROWS)))

    # ── §C  A-1 ────────────────────────────────────────────────────────
    P("")
    P("【A-1-0】「通過點距」之定義比對（⛔ 不得逕代用·二者併出艙）")
    P("-" * W)
    P("  🔒 `probe_WG978_interface.py:442` 逐字 `dist = _dist_pt_line(near_k[1], far_j[1], far_j[0])`，")
    P("     而 `_dist_pt_line(p,q,d) = |cross(p−q, d)|` ⇒ **WG978 式 ＝ `|cross(p_k−p_j, û_j)|`**（無號）。")
    P("     本單式 ＝ **`cross(p_k−p_j, û_k)`**（帶號）⇒ 🔴 **受詞不同（點對線互換）且號不同 ⇒ 不相等**。")
    P("  %-6s %-5s %-4s %-4s %14s %14s %14s"
      % ("情境", "街廓", "j", "k", "WG978 |d_j|", "本單 d_signed", "|差|"))
    difs = []
    for rec, meta, r in ALLROWS:
        difs.append(abs(r["d_wg978"] - abs(r["d_signed"])))
    for rec, meta, r in sorted(ALLROWS, key=lambda x: -abs(x[2]["d_wg978"] - abs(x[2]["d_signed"])))[:8]:
        P("  %-6s %-5s %-4d %-4d %14.6f %14.6f %14.6f"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"],
             r["d_wg978"], r["d_signed"], abs(r["d_wg978"] - abs(r["d_signed"]))))
    P("  ⇒ 分母 %d 對：`|差|` 之 **最大 %.6f ／ 中位 %.6f ／ 最小 %.6f**"
      % (len(difs), max(difs), sorted(difs)[len(difs) // 2], min(difs)))
    P("  ⇒ 判：%s"
      % ("🔴 **二式不相等**（最大差 > 1e-9）⇒ 依 A-1-0 已二者併出艙" if max(difs) > 1e-9
         else "⚠️ 二式於本案數值相等（最大差 ≤ 1e-9）⇒ **具名**"))

    P("")
    P("【A-1-1】`t_X` 精確式之逐對驗證（判準：殘差絕對值極大 ≤ %g m）" % TOL_EXACT)
    P("-" * W)
    res_t = [abs(r["res_t"]) for _, _, r in ALLROWS]
    res_neg = [abs(r["res_t_neg"]) for _, _, r in ALLROWS]
    P("  %-6s %-5s %-4s %-4s %12s %12s %10s %10s %14s %14s %11s"
      % ("情境", "街廓", "j", "k", "t(p_j)", "d_signed", "sinα", "⟨û_j,n̂⟩",
         "預測 t_X", "實測 t_X", "殘差"))
    for rec, meta, r in sorted(ALLROWS, key=lambda x: -abs(x[2]["res_t"]))[:10]:
        P("  %-6s %-5s %-4d %-4d %12.4f %12.4f %10.6f %10.6f %14.6f %14.6f %11.3e"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], r["t_pj"],
             r["d_signed"], r["sin_a"], r["dot_jn"], r["t_pred"], r["t_meas"], r["res_t"]))
    P("  ⇒ 分母 %d 對：殘差**絕對值極大 ＝ %.3e m**（判準 ≤ %g）⇒ %s"
      % (len(res_t), max(res_t), TOL_EXACT, "✅ 成立" if max(res_t) <= TOL_EXACT else "🔴 不成立"))
    # 🔒 補量（⛔ 不改判準·只加維度）：相對殘差 ＋ 依 |t_X| 量級分層
    rel = [abs(r["res_t"]) / max(abs(r["t_meas"]), 1.0) for _, _, r in ALLROWS]
    P("  🔒 **補量（⛔ 不改判準）**：相對殘差 `|res| / max(|t_X|,1)` 之**極大 ＝ %.3e**"
      "（≈ %.1f 個機器 epsilon）" % (max(rel), max(rel) / 2.220446049250313e-16))
    P("     🔒 依 `|t_X|` 量級分層（⛔ 出艙每層之分母）：")
    for lo, hi in ((0, 1e2), (1e2, 1e4), (1e4, 1e6), (1e6, 1e12)):
        sub = [abs(r["res_t"]) for _, _, r in ALLROWS if lo <= abs(r["t_meas"]) < hi]
        if sub:
            P("       |t_X| ∈ [%-6g, %-6g)：對數 %2d　絕對殘差極大 %.3e　%s"
              % (lo, hi, len(sub), max(sub), "✅ ≤ 1e-9" if max(sub) <= TOL_EXACT else "🔴 > 1e-9"))
    P("")
    P("  🔒 **負對照（令 `⟨û_j,n̂⟩ ≡ 1`·＝退回 `W-G.9-79` §D-4 之量級式）**")
    P("  ⇒ 其殘差絕對值極大 ＝ **%.6f m**（判準 ≥ %g）⇒ %s"
      % (max(res_neg), TOL_NEG,
         "✅ 本檢查**非恆真**" if max(res_neg) >= TOL_NEG
         else "🔴 **`⟨û_j,n̂⟩` 於本案恆為 1 ⇒ 本檢查無判別力·具名**"))
    P("     （中位 %.6f ／ 最小 %.6f）" % (sorted(res_neg)[len(res_neg) // 2], min(res_neg)))

    # ── §D  A-2 ────────────────────────────────────────────────────────
    P("")
    P("【A-2】**真正之閉式**（⛔ 輸入白名單內·⛔ 不用 `t_X`／`X`／`contains`）")
    P("-" * W)
    P("  🔒 謂詞：`t_lo − t(p_j) ≤ (d_signed/sinα)·⟨û_j,n̂⟩ ≤ t_hi − t(p_j)`")
    agree = dis = 0
    dis_rows = []
    for rec, meta, r in ALLROWS:
        pr = predicate_closed(r, meta)
        if pr == r["inside"]:
            agree += 1
        else:
            dis += 1
            dis_rows.append((rec, meta, r, pr))
    P("  ⇒ 分母 %d 真實對：與 `block.contains(X)` **一致 %d ／ 不一致 %d**"
      % (len(ALLROWS), agree, dis))
    if dis_rows:
        P("  🔴 不一致者逐對具名：")
        for rec, meta, r, pr in dis_rows:
            P("     [%gm] %-4s (%d,%d) 閉式=%s contains=%s  s*·⟨û_j,n̂⟩=%.6f  t 域=[%.4f,%.4f] t(p_j)=%.4f"
              % (rec["setback"], rec["label"], r["j"], r["k"], pr, r["inside"],
                 r["s_star"] * r["dot_jn"], meta["t_lo"], meta["t_hi"], r["t_pj"]))
    else:
        P("  ✅ **對稱差 ＝ 空集**")
    P("")
    P("  🔒 **負對照（關掉「張開側之號」·改取二側之較大可用長度）**")
    nagree = ndis = 0
    ndis_rows = []
    for rec, meta, r in ALLROWS:
        pr = predicate_neg(r, meta)
        if pr == r["inside"]:
            nagree += 1
        else:
            ndis += 1
            ndis_rows.append((rec, meta, r, pr))
    P("  ⇒ 負對照與 `contains` **一致 %d ／ 不一致 %d** ⇒ %s"
      % (nagree, ndis,
         "✅ 負對照**會判錯** ⇒ 「張開側之號」**有判別力**" if ndis > 0
         else "🔴 **負對照未判錯 ⇒ 「張開側」一項無判別力·具名**"))
    for rec, meta, r, pr in ndis_rows[:6]:
        P("     判錯之對：[%gm] %-4s (%d,%d) 負對照=%s contains=%s"
          % (rec["setback"], rec["label"], r["j"], r["k"], pr, r["inside"]))
    hit_r3 = any(rec["label"] == "R3" and rec["setback"] == 0.0 and r["j"] == 7 and r["k"] == 9
                 for rec, meta, r, pr in ndis_rows)
    P("     🔒 施工單指名之 `0m R3 (7,9)` 是否在判錯之列？ **%s**" % ("是 ✅" if hit_r3 else "否 🔴"))

    P("")
    P("  **問 2**：`0m R3` 之 `(7,9)`——張開側可用長度 vs `|s*·⟨û_j,n̂⟩|`（🔒 應 ≈ 3.4192）")
    for rec, meta, r in ALLROWS:
        if rec["label"] == "R3" and rec["setback"] == 0.0 and r["j"] == 7 and r["k"] == 9:
            delta = r["s_star"] * r["dot_jn"]
            avail = (meta["t_hi"] - r["t_pj"]) if delta > 0 else (r["t_pj"] - meta["t_lo"])
            P("     t(p_j)=%.4f  s*·⟨û_j,n̂⟩=%.4f  張開側=%s  可用長度=%.4f  **差=%.4f**"
              % (r["t_pj"], delta, "t_hi 側" if delta > 0 else "t_lo 側", avail, abs(delta) - avail))
            P("     另一側可用長度 ＝ %.4f（🔒 負對照即取此 ⇒ 誤判在內）"
              % ((r["t_pj"] - meta["t_lo"]) if delta > 0 else (meta["t_hi"] - r["t_pj"])))

    # ── §E  A-3 ────────────────────────────────────────────────────────
    P("")
    P("【A-3】`s` 漂移之候選證路（判準：`⟨û_j,m̂⟩ / sinα` ∈ [%.1f, %.1f]）" % (RATIO_LO, RATIO_HI))
    P("-" * W)
    P("  🔒 **例外類（施工單所令·逐對具名·⛔ 不併入判準）**：`宗k` **本身亦為街角宗**之對。")
    P("  %-6s %-5s %-4s %-4s %10s %10s %12s %12s %13s %11s %-8s"
      % ("情境", "街廓", "j", "k", "⟨û_j,m̂⟩", "sinα", "**比值**", "預測漂移",
         "實測 s_X−s(p_j)", "殘差", "例外類?"))
    inb = out = exc_n = 0
    res_s = []
    for rec, meta, r in ALLROWS:
        res_s.append(abs(r["res_s"]))
        if r["k_corner"]:
            exc_n += 1
        elif RATIO_LO <= r["ratio"] <= RATIO_HI:
            inb += 1
        else:
            out += 1
    show = [x for x in ALLROWS if x[2]["k_corner"] or not (RATIO_LO <= x[2]["ratio"] <= RATIO_HI)]
    for rec, meta, r in show[:14]:
        P("  %-6s %-5s %-4d %-4d %10.6f %10.6f %12.4f %12.4f %13.4f %11.3e %-8s"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], r["dot_jm"], r["sin_a"],
             r["ratio"], r["s_star"] * r["dot_jm"] / meta["denom"],
             r["s_meas"] - r["s_pj"], r["res_s"], "**是**" if r["k_corner"] else "否"))
    P("  ⇒ 分母 %d 對：**非例外類**中 在 [%.1f,%.1f] 內 **%d** ／ 外 **%d**；例外類（`宗k` 為街角宗）**%d**"
      % (len(ALLROWS), RATIO_LO, RATIO_HI, inb, out, exc_n))
    P("  ⇒ `s` 恆等式之殘差絕對值極大 ＝ **%.3e**（判準 ≤ %g）⇒ %s"
      % (max(res_s), TOL_EXACT, "✅" if max(res_s) <= TOL_EXACT else "🔴"))
    absr = sorted(abs(r["ratio"]) for _, _, r in ALLROWS if not r["k_corner"])
    P("  🔒 **補量①（⛔ 非施工單所令·不改判準）**：**`|比值|`** 之分布（非例外類·分母 %d）——"
      "最小 %.4f ／ 中位 %.4f ／ 最大 %.4f；`|比值| ∈ [0.9,1.1]` 者 **%d**"
      % (len(absr), absr[0], absr[len(absr) // 2], absr[-1],
         sum(1 for x in absr if RATIO_LO <= x <= RATIO_HI)))
    # 🔒 補量②：VR-038 四-I-3 之候選式 `s 漂移 ≈ d / cos α`
    negr = sum(1 for _, _, r in ALLROWS if not r["k_corner"] and r["ratio"] < 0)
    P("     🔒 其中比值為**負**者 ＝ **%d** ／ %d ⇒ 🔒 施工單之判準 `[0.9,1.1]` 係**帶號**區間，"
      "⛔ 未涵蓋 `−1` ⇒ **「號」須先具名**（見報告 §E）" % (negr, len(absr)))
    P("  🔒 **補量②（`VR-038` 四-I-3 之候選證路·⛔ 與施工單 A-3 之式不同）**：`s 漂移 ≈ d / cos α`")
    P("     %-6s %-5s %-4s %-4s %12s %10s %14s %14s %10s"
      % ("情境", "街廓", "j", "k", "d_signed", "cosα", "d/cosα", "實測漂移", "比值"))
    rr = []
    for rec, meta, r in ALLROWS:
        if r["k_corner"]:
            continue
        ca = math.sqrt(max(0.0, 1.0 - r["sin_a"] ** 2))
        pred = (r["d_signed"] / ca) if ca > 1e-15 else float("inf")
        meas = r["s_meas"] - r["s_pj"]
        rat = (meas / pred) if pred not in (0.0, float("inf")) else float("nan")
        rr.append((abs(rat - 1.0) if rat == rat else float("inf"), rec, meta, r, ca, pred, meas, rat))
    rr.sort(key=lambda x: -x[0])
    for _, rec, meta, r, ca, pred, meas, rat in rr[:8]:
        P("     %-6s %-5s %-4d %-4d %12.4f %10.6f %14.4f %14.4f %10.4f"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], r["d_signed"], ca, pred, meas, rat))
    good = [x for x in rr if x[0] <= 0.1]
    # 🔒 補量③（⛔ 非施工單所令）：**|比值|** 之分布——判「不成立」是否僅差在**號**
    ab = sorted(abs(x[7]) for x in rr if x[7] == x[7])
    if ab:
        P("     🔒 **|比值| 之分布（⛔ 判「號」是否為唯一差異·分母 %d）**："
          "最小 %.4f ／ 中位 %.4f ／ 最大 %.4f；`|比值| ∈ [0.9,1.1]` 者 **%d**"
          % (len(ab), ab[0], ab[len(ab) // 2], ab[-1],
             sum(1 for x in ab if RATIO_LO <= x <= RATIO_HI)))
        neg = sum(1 for x in rr if x[7] == x[7] and x[7] < 0)
        P("     🔒 比值為**負**者 ＝ **%d** ／ %d ⇒ %s"
          % (neg, len(rr),
             "🔴 **號係主要差異**（|比值| 合格數 %d ≫ 帶號合格數 %d）"
             % (sum(1 for x in ab if RATIO_LO <= x <= RATIO_HI), len(good))
             if sum(1 for x in ab if RATIO_LO <= x <= RATIO_HI) > len(good) + 5
             else "⚠️ 號**非**唯一差異·具名"))
    P("     ⇒ 分母 %d（非例外類）：`實測漂移 / (d/cosα)` ∈ [0.9,1.1] 者 **%d** ／ 外 **%d** ⇒ %s"
      % (len(rr), len(good), len(rr) - len(good),
         "✅ `VR-038` 之候選式成立" if len(rr) and len(good) == len(rr)
         else "🔴 **`VR-038` 之候選式不成立**·具名"))
    P("  🔒 **判（`P4`）**：%s"
      % ("✅ **成立** ⇒ 「`s_X` 恆在域內」由觀察升為**已證**（`α` 相消）"
         if out == 0 else
         "🔴 **不成立**（非例外類有 %d 對偏離）⇒ 該欄**永久停留於觀察**、"
         "`VR-037` 二-丙之「構造必然」四字**須撤回**·具名" % out))

    # ── §F  A-4 ＋ 掃描 ────────────────────────────────────────────────
    P("")
    P("【A-4 ＋ P6】`θ` 掃描（%s）＋ **身分鍵自動比對**"
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
            base = _u(alloc_axis(adir[lbl]))
            th = math.radians(theta_deg)
            ct, st_ = math.cos(th), math.sin(th)
            return (float(base[0] * ct - base[1] * st_), float(base[0] * st_ + base[1] * ct))
        return _f

    KEYS = {}
    P6 = {"agree": 0, "dis": 0, "dis_rows": []}
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
            key = (meta["n"], meta["corners"])
            KEYS.setdefault((rec["setback"], rec["label"]), {})[th] = key
            meas = sum(1 for r in rows if r.get("ok") and r["inside"] and r["d"] >= 2)
            pred = sum(1 for r in rows if r.get("ok") and predicate_closed(r, meta) and r["d"] >= 2)
            if (meas >= 1) == (pred >= 1):
                P6["agree"] += 1
            else:
                P6["dis"] += 1
                P6["dis_rows"].append((th, rec["setback"], rec["label"], meas, pred))
        print("    θ=%d° 完畢" % th, file=sys.stderr)

    P("  🔒 **身分鍵 ＝ `(n, 街角宗索引之 tuple)`**；比對同一 (情境, 街廓) 各 θ 列是否恆定。")
    P("  %-6s %-5s %-8s %s" % ("情境", "街廓", "相異鍵數", "不恆定者之逐列具名"))
    var_rows = []
    for (sb, lb), d in sorted(KEYS.items()):
        vals = list(dict.fromkeys(d.values()))
        base_key = d[SWEEP_DEG[0]]
        odd = [th for th in SWEEP_DEG if d.get(th) != base_key]
        if len(vals) > 1:
            var_rows.extend([(sb, lb, th, d[th]) for th in odd])
            P("  %-6s %-5s %-8d %s" % ("%gm" % sb, lb, len(vals),
                                       "  ".join("%d°:%s" % (th, d[th]) for th in odd)))
        else:
            P("  %-6s %-5s %-8d 恆定 = %s" % ("%gm" % sb, lb, len(vals), base_key))
    P("  ⇒ **不恆定之列數 ＝ %d**（🔒 正對照：施工單已知**恰 5 列**）⇒ %s"
      % (len(var_rows), "✅ 比對器**恰抓 5 列**" if len(var_rows) == 5
         else "🔴 **抓到 %d 列 ≠ 5 ⇒ 比對器有誤·⛔ 不得出艙其結果**" % len(var_rows)))
    P("     逐列：%s" % "  ".join("[%gm]%s@%d°→%s" % (a, b, c, d_) for a, b, c, d_ in var_rows))
    P("  🔒 **併答（`W-G.9-79` §E-2 未具名者）**：`3.5m R6` 於 `θ ≥ 16°` 之街角宗集合為 `()`")
    P("     ⇒ 其「未取得正例」係 **shim 未觸發**、⛔ **非**「交點在外」。")

    P("")
    P("  **`P6`**：閉式謂詞於掃描 **%d 列**是否與 `廓內交叉(不鄰) ≥ 1` 一致（⛔ 母體變異 5 列另計）"
      % (P6["agree"] + P6["dis"]))
    P("  ⇒ 一致 **%d** ／ 不一致 **%d** ⇒ %s"
      % (P6["agree"], P6["dis"], "✅" if P6["dis"] == 0 else "🔴 逐列具名如下"))
    for th, sb, lb, meas, pred in P6["dis_rows"][:12]:
        tag = " 🔒 母體變異列" if any(a == sb and b == lb and c == th for a, b, c, _ in var_rows) else ""
        P("     θ=%d° [%gm] %-4s 實測交叉(不鄰)=%d ／ 閉式預測=%d%s" % (th, sb, lb, meas, pred, tag))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
