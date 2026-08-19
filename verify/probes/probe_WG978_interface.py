# -*- coding: utf-8 -*-
r"""**W-G.9-78 §二 A 組**：**界面之同一性** —— `宗0×宗1` 為何為 `0`（⛔ **只量不修**）。

## 受詞（施工單 `W-G.9-78` §二）
- **A-1** 六塊 × 兩情境，逐宗出艙**近側界**／**遠側界**之（方向單位向量, 通過點）
  ＋ `is_corner` ＋ `_alloc_dir_used`（**生產路徑之輸出**·⛔ 不由 harness 重算·`fixture-provenance`）。
- **A-2** **全對** `(宗 j, 宗 k)`：`方向夾角`／`是否同一條線`／`是否於街廓內交叉`（含交點與其 s）／`交集面積`。
- **A-3** 合成掃描：於**探針記憶體內**令 `∠(用, ALLOC)` ＝ `0°..8°`，逐塊逐角出艙 `Σ_不相鄰` 與 `是否破閘`。

## 🔒 A-0　錯誤方向之**事前選定**（施工單 §二 A-0·節 98·⛔ 寫碼前先寫下）
本探針係**歸因**工具 ⇒ 其瑕疵若往「**把界面說得比實際更同一**」錯，會使成因看起來已被解釋。
⇒ 🔒 **事前選定：偏向判為「<u>不同一</u>」**——凡方向或位置之比對**無法逐位證明其同一**者，
   一律判「**不同一**」並具名；⛔ 不得以「差很小」為由判為同一。

### 🔒 同一性門檻之**由來**（⛔ 不得憑感覺取 `1e-9`）
| 門檻 | 值 | 由來（逐字） |
|---|---|---|
| `TOL_ANG_BIT` | **逐位相同** | 生產碼中，`宗k` 之 `near_dir` **就是** `宗j` 之 `_alloc_dir_used` **同一個 tuple**（`stepg_pipeline.py:670` `_near_dir_left = res.get('_alloc_dir_used')`）⇒ 若界面同一，二方向應**逐位（bit-for-bit）相同**，⛔ 非「近似相等」。**本欄為主判準。** |
| `TOL_ANG_DEG` | `1e-9` 度 | 副判準。TWD97 座標量級 ~`3.1e6`；double 相對精度 `2^-52 ≈ 2.22e-16` ⇒ 單位向量分量絕對誤差 ~`1e-15`，經 `norm`／`rot90` 數步累積 ~`1e-14` rad ≈ `6e-13` 度 ⇒ 取其 ~`1600` 倍為門檻。⚠️ 該值**遠小於** `R6` 之退化角 `3e-6` 度 ⇒ **連 `R6` 亦會判「不平行」**（符 A-0 之保守方向）。 |
| `TOL_DIST_M` | `1e-9` m | 「通過點共線」之門檻。同上量級推導：座標絕對誤差 ~`3.1e6 × 2.22e-16 ≈ 7e-10` m ⇒ 取 `1e-9`。⚠️ **另併列** DXF 量子口徑 `q/10 = 1e-6 m`（`_cad_dxf_quantum` ＝ `1e-5`）之判，**二判皆出艙**（⛔ 不擇一）。 |

## 🔒 界之取得方式（施工單 A-1 明令須具名·**二法並用且對拍**）
- **甲法（構造式·主）**：自生產路徑之實參／輸出重建——
  近側界 ＝ `(方向 rot90(near_dir 或 allocation_dir), 通過點 baseline_pt)`；
  遠側界 ＝ `(方向 rot90(_alloc_dir_used), 通過點 baseline_pt + S·d̂)`。
  🔒 依據：`solve_G_binary` `@9707-9740`——`_near_ad = near_dir` 入 `_block_strip` 之
  `allocation_dir` 槽（⇒ 其 `n_hat = rot90` ＝ **近**側邊方向）；`_far_nhat = rot90(allocation_dir)`
  （⇒ **遠**側邊方向）。`near_dir is None` ⇒ 走單線路徑，二界同方向。
- **乙法（反推式·對拍）**：以 `cut_coords` 之頂點**驗證**甲法之線——
  ① 全部頂點須落在該線之**同一側**（容差 `TOL_DIST_M`）；② **至少 2 個**頂點須落在線上。
  ⛔ 乙法**不獨立產生**方向（避免「以形狀回推」·`W-G.9-42` §C-2 明令）；**只驗證**。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修 `_first_corner_alloc_dir`／`near_dir` 交遞／`_solve_G_one`；
⛔ 不修 `②-宗` 閘、不調上界；⛔ **不對成因下「這是 bug」之結論**（施工單 §七-2）；
⛔ **不以 `f(θ, L)` 擬合**（正例僅 2·合成正例係人工·§七-4）；
⛔ 不接入 `run_all`；⛔ 不覆寫任何既有 log（檔名含產生它之 commit 短碼）。
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
W = 200
TOL_ANG_DEG = 1e-9
TOL_DIST_M = 1e-9
TOL_DIST_Q10 = 1e-6            # DXF 量子 1e-5 之 1/10（併列口徑）
SWEEP_DEG = list(range(0, 9))  # 0°..8°
QUANTUM = 0.005                # ②-宗 上界之半量子（⛔ 本檔不改）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception:                                               # noqa: BLE001
        return "UNKNOWN"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG978_interface_%s.log" % COMMIT)


# ── 原語 ────────────────────────────────────────────────────────────────
def _u(v):
    a = np.asarray(v, dtype=float)[:2]
    n = float(np.linalg.norm(a))
    return None if n < 1e-15 else a / n


def _rot90(v):
    a = np.asarray(v, dtype=float)[:2]
    return np.array([-a[1], a[0]])


def _ang(u, v):
    """無向夾角（度）·0〜90。"""
    a, b = _u(u), _u(v)
    if a is None or b is None:
        return float("nan")
    return math.degrees(math.acos(min(1.0, abs(float(np.dot(a, b))))))


def _bitsame(u, v):
    """🔒 **逐位**相同（含反向：`rot90` 之號差不改「同一條線」）。"""
    if u is None or v is None:
        return False
    a = np.asarray(u, dtype=float)[:2]
    b = np.asarray(v, dtype=float)[:2]
    return bool(np.array_equal(a, b) or np.array_equal(a, -b))


def _dist_pt_line(p, q, d):
    """點 p 到「過 q、方向 d」之無限直線之垂距。"""
    dd = _u(d)
    if dd is None:
        return float("nan")
    w = np.asarray(p, dtype=float)[:2] - np.asarray(q, dtype=float)[:2]
    return abs(float(w[0] * (-dd[1]) + w[1] * dd[0]))


def _line_cross(q1, d1, q2, d2):
    """兩無限直線之交點。平行 ⇒ None。"""
    a, b = _u(d1), _u(d2)
    if a is None or b is None:
        return None
    den = a[0] * b[1] - a[1] * b[0]
    if abs(den) < 1e-15:
        return None
    w = np.asarray(q2, dtype=float)[:2] - np.asarray(q1, dtype=float)[:2]
    t = (w[0] * b[1] - w[1] * b[0]) / den
    return np.asarray(q1, dtype=float)[:2] + t * a


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


def _verify_line_against_poly(coords, q, d, tol):
    """🔒 **乙法**：以 `cut_coords` 驗證甲法之線。回 (同側?, 線上頂點數, 最大越界量)。"""
    dd = _u(d)
    if dd is None or not coords:
        return (False, 0, float("nan"))
    sgn, on, worst = 0, 0, 0.0
    for c in coords:
        w = np.asarray(c, dtype=float)[:2] - np.asarray(q, dtype=float)[:2]
        s = float(w[0] * (-dd[1]) + w[1] * dd[0])
        if abs(s) <= tol:
            on += 1
            continue
        if sgn == 0:
            sgn = 1 if s > 0 else -1
        elif (s > 0) != (sgn > 0):
            worst = max(worst, abs(s))
    return (worst == 0.0, on, worst)


# ── 【0】量測器自檢 ─────────────────────────────────────────────────────
def selfcheck(P):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·各項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True
    a = _ang((1, 0), (0, 1)); b = _ang((1, 0), (1, 0)); c = _ang((1, 0), (-1, 0))
    r1 = abs(a - 90) < 1e-12 and abs(b) < 1e-12 and abs(c) < 1e-12
    ok &= r1
    P("  ① 夾角(無向) ⊥=%.12f(期望90)／同向=%.12f(0)／反向=%.12f(0) ⇒ %s"
      % (a, b, c, "PASS" if r1 else "🔴 FAIL"))
    P("     對照(已知偽)：45° ⇒ %.9f（期望 45）" % _ang((1, 0), (1, 1)))

    # 🔒 **負對照之擾動量須 ≥ 1 ulp**——⛔ 不得小於被測量之解析度，否則**對照組本身無判別力**。
    #    （首版取 `+1e-18`，而 `0.3` 之 ulp ＝ `5.55e-17` ⇒ `0.3+1e-18 == 0.3` ⇒ 對照恆 True·
    #      該紅係**對照組之誤**、⛔ 非 `_bitsame` 之誤。本批自誤·見報告 §I。）
    v = np.array([0.3, 0.7])
    v_ulp = np.array([np.nextafter(v[0], 1.0), v[1]])   # 恰差 1 ulp
    r2 = (_bitsame(v, v.copy()) and _bitsame(v, -v) and not _bitsame(v, v_ulp)
          and float(v_ulp[0] - v[0]) > 0.0)
    ok &= r2
    P("  ② 逐位相同：同值=%s(期望True)／反向=%s(期望True·同一條線)／**差 1 ulp**(%.3e)=%s(期望False) ⇒ %s"
      % (_bitsame(v, v.copy()), _bitsame(v, -v), float(v_ulp[0] - v[0]),
         _bitsame(v, v_ulp), "PASS" if r2 else "🔴 FAIL"))
    P("     🔒 負對照之擾動 ＝ **1 ulp**（`np.nextafter`）——⛔ 小於解析度之擾動使對照組恆真、無判別力。")

    d1 = _dist_pt_line((0, 5), (0, 0), (1, 0))
    d0 = _dist_pt_line((7, 0), (0, 0), (1, 0))
    r3 = abs(d1 - 5) < 1e-12 and abs(d0) < 1e-12
    ok &= r3
    P("  ③ 點到線垂距：離線 5 ⇒ %.12f(期望5)／線上 ⇒ %.12f(期望0) ⇒ %s"
      % (d1, d0, "PASS" if r3 else "🔴 FAIL"))

    x = _line_cross((0, 0), (1, 0), (3, -1), (0, 1))
    r4 = x is not None and abs(x[0] - 3) < 1e-12 and abs(x[1]) < 1e-12 \
        and _line_cross((0, 0), (1, 0), (0, 9), (1, 0)) is None
    ok &= r4
    P("  ④ 直線交點：⊥ 交 ⇒ %s（期望 [3,0]）／平行 ⇒ %s（期望 None）⇒ %s"
      % (None if x is None else [round(float(t), 9) for t in x],
         _line_cross((0, 0), (1, 0), (0, 9), (1, 0)), "PASS" if r4 else "🔴 FAIL"))

    sq = [(0, 0), (10, 0), (10, 4), (0, 4)]
    same, on, worst = _verify_line_against_poly(sq, (0, 0), (1, 0), TOL_DIST_M)
    same2, on2, worst2 = _verify_line_against_poly(sq, (0, 2), (1, 0), TOL_DIST_M)
    r5 = same and on == 2 and (not same2) and worst2 > 0
    ok &= r5
    P("  ⑤ 乙法驗線：邊線 ⇒ 同側=%s 線上頂點=%d(期望2)／**穿心線** ⇒ 同側=%s 越界=%.4f(期望>0) ⇒ %s"
      % (same, on, same2, worst2, "PASS" if r5 else "🔴 FAIL"))

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
                "alloc_in": kw.get("allocation_dir"),
                "alloc_used": res.get("_alloc_dir_used"),
                "baseline_pt": kw.get("baseline_pt"),
                "d_hat": kw.get("d_hat"),
                "S": res.get("S_raw", res.get("S")),
                "solver": label,
                "cut": res.get("cut_coords") or [],
            }
        except Exception:                                           # noqa: BLE001
            pass
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
                    _p = _poly((_res or {}).get('cut_coords') or [])
                    if _p is not None:
                        nm.append(((_entry or {}).get('tp') or {}).get('暫編地號', '?'))
                        rs.append(_res)
                if len(nm) == len(list(biz_polys or [])):
                    names, ress = nm, rs
                    align = "✅ 逐位對齊" if ap is biz_polys else "⚠️ 數相等但非同一物件"
        except Exception as e:                                      # noqa: BLE001
            align = "🔴 未對上（%s）" % type(e).__name__
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


# ── 界之重建（甲法）────────────────────────────────────────────────────
def faces_of(info):
    """回 (近側界(dir,pt), 遠側界(dir,pt))；資料不全 ⇒ (None, None)。"""
    if not info:
        return (None, None)
    au = info.get("alloc_used")
    nd = info.get("near_dir")
    bp = info.get("baseline_pt")
    dh = info.get("d_hat")
    S = info.get("S")
    if au is None or bp is None or dh is None or S is None:
        return (None, None)
    near_src = nd if nd is not None else au
    n_dir = _rot90(near_src)
    f_dir = _rot90(au)
    n_pt = np.asarray(bp, dtype=float)[:2]
    f_pt = n_pt + float(S) * _u(dh)
    return ((n_dir, n_pt), (f_dir, f_pt))


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
    P("【W-G.9-78 §二 A 組】界面之同一性——`宗0×宗1` 為何為 `0`（⛔ 只量不修）")
    P("=" * W)
    import shapely
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s" % (shapely.__version__, shapely.geos_version))
    P("  🔒 A-0 **事前選定**：偏向判為「**不同一**」——無法逐位證明同一者一律判不同一·具名。")
    P("  🔒 門檻：主判準 ＝ **方向逐位相同**；副 `TOL_ANG_DEG=%g°`／`TOL_DIST_M=%g m`；"
      "併列 DXF 量子口徑 `q/10=%g m`。由來見 docstring。" % (TOL_ANG_DEG, TOL_DIST_M, TOL_DIST_Q10))
    P("  🔒 界之取得：**甲法**（生產實參重建）為主、**乙法**（`cut_coords` 驗線）對拍。⛔ 乙法不產生方向。")

    ns, fake_st = harvest()
    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    snapshot = rv.load_snapshot()
    o_solve = ns["_solve_G_one"]
    o_pool = ns["_pool_strips_for_block"]
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

    def one_pass(setback_list):
        for setback in setback_list:
            CUR["setback"] = setback
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, wins, forced = run_corner_pk(
                ns, fake_st, cb_all, cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for lbl in blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass

    P("")
    P("【驅動·第一趟（真實）】R1–R6 × 兩情境（⛔ 不只破閘二格）——街廓母體 = %s" % blks)
    P("-" * W)
    ns["_solve_G_one"] = spy_solve(o_solve)
    ns["_pool_strips_for_block"] = spy_pool(o_pool)
    try:
        one_pass((0.0, 3.5))
    finally:
        ns["_solve_G_one"] = o_solve
        ns["_pool_strips_for_block"] = o_pool
    REAL = list(CAP)
    P("  攔截：`_pool_strips_for_block` %d 筆／`_solve_G_one` 回傳登記 %d 筆" % (len(REAL), len(SOLVE)))

    # ── §C  A-1 ────────────────────────────────────────────────────────
    P("")
    P("【A-1】逐宗之近側界／遠側界（甲法重建 ＋ 乙法驗線）")
    P("-" * W)
    P("  🔒 甲法之依據：`solve_G_binary @9707-9740`——`_near_ad = near_dir`（⇒近側邊方向 `rot90`）／")
    P("     `_far_nhat = rot90(allocation_dir)`（⇒遠側邊方向）；`near_dir is None` ⇒ 單線、二界同方向。")
    P("  %-6s %-5s %-4s %-15s %-7s %-8s %-26s %-26s %-22s"
      % ("情境", "街廓", "i", "暫編地號", "corner", "near_dir", "近側界方向(單位)", "遠側界方向(單位)", "乙法驗線"))
    FACE = {}
    nb_ok = nb_bad = nb_unk = 0
    for rec in REAL:
        for i, nm in enumerate(rec["names"] or []):
            r = (rec["ress"] or [None] * (i + 1))[i]
            info = SOLVE.get(id(r)) if r is not None else None
            nf, ff = faces_of(info)
            FACE[(rec["setback"], rec["label"], i)] = (nf, ff, info, nm)
            if nf is None:
                nb_unk += 1
                P("  %-6s %-5s %-4d %-15s %-7s %-8s %-26s %-26s %-22s"
                  % ("%gm" % rec["setback"], rec["label"], i, nm, "?", "?", "🔴 不可判", "", "—"))
                continue
            cut = (info or {}).get("cut", [])
            v_n = _verify_line_against_poly(cut, nf[1], nf[0], TOL_DIST_Q10)
            v_f = _verify_line_against_poly(cut, ff[1], ff[0], TOL_DIST_Q10)
            good = v_n[0] and v_n[1] >= 2 and v_f[0] and v_f[1] >= 2
            nb_ok += int(good); nb_bad += int(not good)
            if i <= 3 or info.get("is_corner"):     # A-0 多報：前 4 宗 ＋ 街角宗全列
                P("  %-6s %-5s %-4d %-15s %-7s %-8s (%9.6f,%9.6f)      (%9.6f,%9.6f)      %s"
                  % ("%gm" % rec["setback"], rec["label"], i, nm,
                     "是" if info.get("is_corner") else "否",
                     "有" if info.get("near_dir") is not None else "無(單線)",
                     *_u(nf[0]), *_u(ff[0]),
                     ("✅ 近%d/遠%d 頂點在線" % (v_n[1], v_f[1])) if good
                     else ("🔴 近(同側%s,在線%d,越界%.2e) 遠(同側%s,在線%d,越界%.2e)"
                           % (v_n[0], v_n[1], v_n[2], v_f[0], v_f[1], v_f[2]))))
    P("  ⇒ 分母 %d 宗：乙法驗線 **通過 %d ／ 不通過 %d ／ 不可判 %d**（容差 %g m）"
      % (nb_ok + nb_bad + nb_unk, nb_ok, nb_bad, nb_unk, TOL_DIST_Q10))

    # ── §D  A-2 ────────────────────────────────────────────────────────
    P("")
    P("【A-2】界面同一性表（**全對**·⛔ 非取樣）")
    P("-" * W)
    P("  🔒 `是否同一條線` ＝ **方向逐位相同（或反向）** ∧ **通過點距 ≤ %g m**（A-0：無法逐位證明 ⇒ 判否）。"
      % TOL_DIST_M)
    SUMMARY = []
    for rec in REAL:
        n = len(rec["biz"])
        if n < 2:
            P("")
            P("  ── [%gm] %s ── n=%d ⇒ ⚠️ 無對可比·具名" % (rec["setback"], rec["label"], n))
            continue
        broke = bool(rec["exc"] and "②-宗" in (rec["exc"] or ""))
        m_hat, denom = ns["_strip_axis"](rec["d_hat"], rec["alloc"])
        bp0 = np.asarray(rec["corner_pt"], dtype=float)[:2]

        def s_of(p):
            return float(np.dot(np.asarray(p, dtype=float)[:2] - bp0, m_hat)) / denom

        rows = []
        for j, k in itertools.combinations(range(n), 2):
            fj = FACE.get((rec["setback"], rec["label"], j))
            fk = FACE.get((rec["setback"], rec["label"], k))
            if not fj or not fk or fj[1] is None or fk[0] is None:
                rows.append({"j": j, "k": k, "unk": True})
                continue
            far_j, near_k = fj[1], fk[0]
            ang = _ang(far_j[0], near_k[0])
            bit = _bitsame(_u(far_j[0]), _u(near_k[0]))
            dist = _dist_pt_line(near_k[1], far_j[1], far_j[0])
            same = bool(bit and dist <= TOL_DIST_M)
            same_q = bool((bit or ang <= TOL_ANG_DEG) and dist <= TOL_DIST_Q10)
            X = None if bit else _line_cross(far_j[1], far_j[0], near_k[1], near_k[0])
            inside = bool(X is not None and rec["block"] is not None
                          and rec["block"].contains(SPoint(float(X[0]), float(X[1]))))
            area = float(rec["biz"][j].intersection(rec["biz"][k]).area)
            rows.append({"j": j, "k": k, "ang": ang, "bit": bit, "dist": dist,
                         "same": same, "same_q": same_q, "X": X, "in": inside,
                         "sX": (s_of(X) if X is not None else float("nan")),
                         "area": area, "unk": False})
        nsame = sum(1 for r in rows if not r.get("unk") and r["same"])
        ncross = sum(1 for r in rows if not r.get("unk") and r["in"])
        npos = sum(1 for r in rows if not r.get("unk") and r["area"] > 0)
        P("")
        P("  ── [%gm] %s ── n=%d　分母 C(n,2)=%d　%s　同一條線 %d ／ 街廓內交叉 %d ／ 面積>0 %d"
          % (rec["setback"], rec["label"], n, len(rows),
             "🔴 破閘" if broke else "未破閘", nsame, ncross, npos))
        show = [r for r in rows if r.get("unk") or r["same"] or r["in"] or r["area"] > 0
                or r["j"] == 0]
        P("     %-4s %-4s %12s %-8s %12s %-10s %-8s %12s %12s"
          % ("j", "k", "方向夾角°", "逐位同", "通過點距m", "同一條線?", "廓內交叉", "交點 s", "交集面積"))
        for r in show:
            if r.get("unk"):
                P("     %-4d %-4d %12s %-8s %12s %-10s %-8s %12s %12s"
                  % (r["j"], r["k"], "—", "—", "—", "🔴 不可判", "—", "—", "—"))
                continue
            P("     %-4d %-4d %12.9f %-8s %12.3e %-10s %-8s %12.4f %12.6f"
              % (r["j"], r["k"], r["ang"], "是" if r["bit"] else "否", r["dist"],
                 "**是**" if r["same"] else "否", "是" if r["in"] else "否",
                 r["sX"], r["area"]))
        SUMMARY.append((rec["setback"], rec["label"], broke, n, len(rows),
                        nsame, ncross, npos, rows, rec))

    # A-2 之三問
    P("")
    P("【A-2 三問】（⛔ 逐對作答）")
    P("-" * W)
    P("  **問 1**：`宗0×宗1` 之 `是否同一條線` ＝ ?（`P2`）")
    for sb, lb, br, n, npair, nsame, ncross, npos, rows, rec in SUMMARY:
        r01 = next((r for r in rows if r["j"] == 0 and r["k"] == 1 and not r.get("unk")), None)
        if r01 is None:
            P("     [%gm] %-4s ⇒ ⚠️ 不可判·具名" % (sb, lb))
            continue
        P("     [%gm] %-4s %s ⇒ **%s**（逐位同=%s·點距=%.3e m·夾角=%.9f°）｜交集面積 = %.6f"
          % (sb, lb, "🔴破閘" if br else "未破閘",
             "同一條線" if r01["same"] else "**不同一**",
             r01["bit"], r01["dist"], r01["ang"], r01["area"]))
    P("")
    P("  **問 2**：`宗0×宗2`／`宗0×宗3` 之楔形面積 vs 實測交集面積（`P4`）")
    P("     🔒 **楔形之定義**：`宗j` 之遠側界與 `宗k` 之近側界二**無限直線**所夾之角域，"
      "與**街廓**及二宗之其餘界之交 ⇒ 此處以 `宗j ∩ 宗k` 之**實體**為準，")
    P("     另出艙**二線交點以後**（`s > s_X`）之部分佔該交集之比例——⛔ 不另造第二個楔形定義。")
    P("     %-6s %-5s %-6s %12s %12s %12s %10s"
      % ("情境", "街廓", "對", "交集面積", "交點 s", "交集之 s 上界", "交點以後佔比"))
    for sb, lb, br, n, npair, nsame, ncross, npos, rows, rec in SUMMARY:
        m_hat, denom = ns["_strip_axis"](rec["d_hat"], rec["alloc"])
        bp0 = np.asarray(rec["corner_pt"], dtype=float)[:2]
        for r in rows:
            if r.get("unk") or r["j"] != 0 or r["k"] not in (2, 3) or r["area"] <= 1e-9:
                continue
            g = rec["biz"][0].intersection(rec["biz"][r["k"]])
            ss = [float(np.dot(np.asarray(c, dtype=float)[:2] - bp0, m_hat)) / denom
                  for c in list(g.exterior.coords)] if g.geom_type == "Polygon" else []
            hi = max(ss) if ss else float("nan")
            frac = float("nan")
            if r["X"] is not None and ss:
                try:
                    from shapely.ops import split as _sp        # noqa: F401
                except Exception:                               # noqa: BLE001
                    pass
                lo_ = min(ss)
                frac = ((hi - r["sX"]) / (hi - lo_)) if hi > lo_ else float("nan")
            P("     %-6s %-5s 宗0×宗%-2d %12.6f %12.4f %12.4f %9.2f%%"
              % ("%gm" % sb, lb, r["k"], r["area"], r["sX"], hi, 100.0 * frac))
    P("")
    P("  **問 3**：未破閘之塊，其 `宗0` 與後續各宗之界面同一性（🔒 **判別力**）")
    P("     %-6s %-5s %-8s %6s %12s %14s %14s %14s"
      % ("情境", "街廓", "破閘?", "n", "同一條線數", "宗0 之對數", "宗0 同一條線", "宗0 廓內交叉"))
    for sb, lb, br, n, npair, nsame, ncross, npos, rows, rec in SUMMARY:
        z0 = [r for r in rows if r["j"] == 0 and not r.get("unk")]
        P("     %-6s %-5s %-8s %6d %12d %14d %14d %14d"
          % ("%gm" % sb, lb, "🔴 破閘" if br else "未破閘", n, nsame, len(z0),
             sum(1 for r in z0 if r["same"]), sum(1 for r in z0 if r["in"])))

    # ── §E  A-3 合成掃描 ───────────────────────────────────────────────
    P("")
    P("【A-3】合成掃描：`∠(用, ALLOC)` ＝ %s（⛔ 探針記憶體內·⛔ 不動倉內任何檔）"
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

    P("  🔒 shim 之受詞 ＝ `_first_corner_alloc_dir` 之**回值**（⛔ 不改其碼、⛔ 不改呼叫端）；")
    P("     回 `rotate(alloc_normal_axis(ALLOC_blk), θ)` ⇒ `∠(用, ALLOC) ≡ θ`（構造上恆等）。")
    P("  %-6s %-5s %-6s %5s %12s %12s %-10s %10s %8s %8s %8s %-14s"
      % ("θ", "情境", "街廓", "n", "Σ全對", "Σ_不相鄰", "破閘?", "bound",
         "廓內交叉", "其中不鄰", "不鄰對數", "街角宗索引"))
    SWEEP = []
    for th in SWEEP_DEG:
        CAP.clear()
        CUR["theta"] = th
        ns["_solve_G_one"] = spy_solve(o_solve)
        ns["_pool_strips_for_block"] = spy_pool(o_pool)
        ns["_first_corner_alloc_dir"] = make_fcad(th)
        try:
            one_pass((0.0, 3.5))
        finally:
            ns["_solve_G_one"] = o_solve
            ns["_pool_strips_for_block"] = o_pool
            ns["_first_corner_alloc_dir"] = o_fcad
        for rec in CAP:
            n = len(rec["biz"])
            # 🔒 逐宗之界（同 A-1 之甲法·⛔ 不另立第二種）
            fc = []
            for i in range(n):
                r = (rec["ress"] or [None] * (i + 1))[i]
                info = SOLVE.get(id(r)) if r is not None else None
                fc.append((faces_of(info), info))
            tot = non = 0.0
            ncross = ncross_nonadj = 0
            npair_nonadj = 0
            for j, k in itertools.combinations(range(n), 2):
                a = float(rec["biz"][j].intersection(rec["biz"][k]).area)
                tot += a
                if k - j >= 2:
                    non += a
                    npair_nonadj += 1
                (nfj, ffj), _ = fc[j]
                (nfk, ffk), _ = fc[k]
                if ffj is None or nfk is None:
                    continue
                if _bitsame(_u(ffj[0]), _u(nfk[0])):
                    continue                       # 同方向 ⇒ 不交叉
                X = _line_cross(ffj[1], ffj[0], nfk[1], nfk[0])
                if X is not None and rec["block"] is not None \
                        and rec["block"].contains(SPoint(float(X[0]), float(X[1]))):
                    ncross += 1
                    if k - j >= 2:
                        ncross_nonadj += 1
            corners = [i for i in range(n) if (fc[i][1] or {}).get("is_corner")]
            bound = max(0, n - 1) * QUANTUM * float(rec["depth"] or 0)
            brk = bool(rec["exc"] and "②-宗" in (rec["exc"] or ""))
            SWEEP.append((th, rec["setback"], rec["label"], n, tot, non, brk, bound,
                          ncross, ncross_nonadj, npair_nonadj, corners))
            P("  %-6s %-5s %-6s %5d %12.6f %12.6f %-10s %10.4f %8d %8d %8d %-14s"
              % ("%d°" % th, "%gm" % rec["setback"], rec["label"], n, tot, non,
                 "🔴 破閘" if brk else "未破閘", bound, ncross, ncross_nonadj,
                 npair_nonadj, str(corners)))
        print("    θ=%d° 完畢" % th, file=sys.stderr)

    P("")
    P("  🔒 **判別力 ①（`P3`·sanity）**：`θ=0°` ⇒ 逐塊 `Σ_不相鄰` 須為 `0`")
    z = [x for x in SWEEP if x[0] == 0]
    bad0 = [x for x in z if x[5] > 1e-9]
    P("     θ=0° 之 %d 格：`Σ_不相鄰 > 1e-9` 者 **%d 格**%s ⇒ %s"
      % (len(z), len(bad0),
         "" if not bad0 else "：" + str([(x[1], x[2], round(x[5], 6)) for x in bad0]),
         "✅ 成立" if not bad0 else "🔴 **不成立 ⇒ 量測器有誤 ⇒ 停 A-2 之結論**"))
    P("")
    P("  🔒 **判別力 ②**：逐塊之**破閘門檻角度**（首個判破之 θ；無 ⇒ 「未破」）")
    P("     🔒 併出艙**結構前提**：若該塊之 `不相鄰對數 == 0`，則 `Σ_不相鄰` **恆為 0**"
      "——⛔ 此係<u>構造必然</u>、⛔ 不得讀為「該塊不受角度影響」。")
    P("     %-6s %-5s %-14s %6s %10s %10s %12s %-14s"
      % ("情境", "街廓", "破閘門檻 θ", "n", "depth", "不鄰對數", "θ=8° 廓內交叉", "街角宗索引"))
    keys = sorted({(x[1], x[2]) for x in SWEEP})
    for sb, lb in keys:
        seq = sorted([x for x in SWEEP if x[1] == sb and x[2] == lb])
        thr = next((x[0] for x in seq if x[6]), None)
        n_ = seq[0][3] if seq else 0
        dep = next((r["depth"] for r in REAL if r["setback"] == sb and r["label"] == lb), None)
        last = [x for x in seq if x[0] == max(SWEEP_DEG)]
        P("     %-6s %-5s %-14s %6d %10.4f %10d %12d %-14s"
          % ("%gm" % sb, lb, ("%d°" % thr) if thr is not None else "**未破（0..8°）**",
             n_, float(dep or 0), (last[0][10] if last else -1),
             (last[0][8] if last else -1), str(last[0][11]) if last else "—"))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
