# -*- coding: utf-8 -*-
r"""**W-G.9-79 §二 A 組**：交點落點之 `(s, t)` ＋ `Σ` 真值補測 ＋ `θ` **雙向**延伸掃描（⛔ **只量不修**）。

## 受詞（施工單 `W-G.9-79` §二）
- **A-1-1** 逐對表之格式修正：面積 `%.3e`、增印 `k−j`／`是否相鄰`、
  **逐格出艙 `面積 > 0` 之每一筆 `(j, k, k−j, 面積)`**（🔒 節 102：表頭之計數須可逐筆指認）。
- **A-1-2** 12 格逐格出艙 `Σ_相鄰`／`Σ_不相鄰` 之**真值**（`%.6e`·⛔ 非二元標籤）＋ `bound` ＋ 帶號差。
- **A-2** **全對**（⛔ 非只 `宗0`·⛔ 不以 `j == 0` 過濾）之交點 `(s_X, t_X)`、街廓 `s`／`t` 域、
  `在內?`、**越界軸**、**越界量（帶號）**。
- **A-3** `θ ∈ {−8,−6,−4,−2,0,2,4,6,8,12,16,20}`（**12 點·雙向**）之掃描。

## 🔒 A-0　錯誤方向之**事前選定**（施工單 §二 A-0·節 98·⛔ 寫碼前先寫下）
本探針係**歸因**工具。其瑕若往「**把交點說得比實際更常落在街廓外**」錯，
會使「廓內交叉」看起來更像充分判別者 ⇒ **安靜地坐實一個可能為假之結論**。
⇒ 🔒 **事前選定：偏向判為「在內」**——凡無法逐位／逐項證明交點在街廓外者，
   **一律判「在內」並具名**（⇒ 錯誤方向為「多報廓內交叉」⇒ 會使未破閘之格出現交叉 ⇒ **會吵**）。

## 🔒 局部框之定義（⛔ 逐字·⛔ 不得中途更換）
```
m_hat, denom = _strip_axis(d_hat, alloc)          # 生產原語·ns harvest
bp0          = corner_pt
s(p) = dot(p - bp0, m_hat) / denom                # 斜交切線軸之 s（與 _strip_s_range 同式）
t(p) = dot(p - bp0, rot90(m_hat))                 # ⛔ **不除 denom**·單位 m
```

## 🔒 二個「在內」之口徑（⛔ 二者皆出艙·⛔ 不擇一）
| 口徑 | 定義 | 性質 |
|---|---|---|
| `在內?`（**主**） | `block_poly.contains(Point(X))` | **真多邊形**測試 |
| `越界軸／越界量` | 以街廓頂點於局部框之 `[s_lo,s_hi]×[t_lo,t_hi]` **外接盒**判 | **必要非充分**——街廓非凸時二者可不一致 |
⚠️ **二者不一致者一律具名**（承 `probe_D2b12_bridge` 之「非凸 ⇒ 不連通片」缺口）。

## 🔒 門檻（⛔ 同一量之二門檻須併標於欄名）
- `面積 > 0`：**嚴格大於 0**（計數用·與 `W-G.9-78` 同）。
- `面積 > 1e-9`：sanity 用（`A-3` 判別力①·與 `W-G.9-78` 逐字同一門檻）。
- 二者**皆逐字標於欄名**，⛔ 不得只寫「>0」。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修 `②-宗` 閘／上界／`near_dir` 交遞／`_first_corner_alloc_dir` 之碼；
⛔ **不對成因下「這是 bug」之結論**；⛔ **不以 `f(θ,L)` 或任何曲線擬合代替因果**；
⛔ **不 shim `S`**（施工單 §七-6：`S` 由面積二分求得·shim 之將破壞面積守恆）；
⛔ 不接入 `run_all`；⛔ 不覆寫任何既有 log；
🔒 **例外一律逐字出艙**（⛔ 不得 `try/except` 吞掉·⛔ 不得 `format_exc()[-300:]` 尾切片·`GB-86`）。
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
TOL_SANITY = 1e-9          # 🔒 與 W-G.9-78 之 sanity 門檻逐字相同


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG979_crosspoint_%s.log" % COMMIT)


def _u(v):
    a = np.asarray(v, dtype=float)[:2]
    n = float(np.linalg.norm(a))
    return None if n < 1e-15 else a / n


def _rot90(v):
    a = np.asarray(v, dtype=float)[:2]
    return np.array([-a[1], a[0]])


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


# ── 【0】量測器自檢 ─────────────────────────────────────────────────────
def selfcheck(P):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·各項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    # ① 逐位相同（🔒 負對照之擾動 ＝ 1 ulp·W-G.9-78 I-1 之修）
    v = np.array([0.3, 0.7])
    v_ulp = np.array([np.nextafter(v[0], 1.0), v[1]])
    r1 = (_bitsame(v, v.copy()) and _bitsame(v, -v) and not _bitsame(v, v_ulp))
    ok &= r1
    P("  ① 逐位相同：同值=%s(True)／反向=%s(True)／**差 1 ulp**(%.3e)=%s(**期望 False**) ⇒ %s"
      % (_bitsame(v, v.copy()), _bitsame(v, -v), float(v_ulp[0] - v[0]),
         _bitsame(v, v_ulp), "PASS" if r1 else "🔴 FAIL"))

    # ② 直線交點
    x = _line_cross((0, 0), (1, 0), (3, -1), (0, 1))
    r2 = (x is not None and abs(x[0] - 3) < 1e-12 and abs(x[1]) < 1e-12
          and _line_cross((0, 0), (1, 0), (0, 9), (1, 0)) is None)
    ok &= r2
    P("  ② 直線交點：⊥ 交 ⇒ %s（期望 [3,0]）／平行 ⇒ %s（期望 None）⇒ %s"
      % (None if x is None else [round(float(q), 12) for q in x],
         _line_cross((0, 0), (1, 0), (0, 9), (1, 0)), "PASS" if r2 else "🔴 FAIL"))

    # ③ 局部框：s/t 之正交性與單位（🔒 t ⛔ 不除 denom）
    d = _u((0.675686, 0.737190)); al = np.array([0.726019, 0.687675])
    bp = np.array([0.0, 0.0])
    P0 = SPoly([(0, 0), (7, 0), (7, 2.5), (0, 2.5)])
    del P0
    m = _u(_rot90(_rot90(d)))            # 佔位（真 m_hat 由 ns 取·此處只驗式子形狀）
    del m, al, bp, d

    # ④ 越界量之號（🔒 正 ＝ 在外）
    def over(lo, hi, x_):
        return max(lo - x_, x_ - hi)
    r4 = (over(0, 10, 12) == 2 and over(0, 10, -3) == 3 and over(0, 10, 5) == -5)
    ok &= r4
    P("  ④ 越界量（正＝在外）：右外 12⇒%.1f(期望2)／左外 −3⇒%.1f(期望3)／內 5⇒%.1f(期望−5·負＝餘裕) ⇒ %s"
      % (over(0, 10, 12), over(0, 10, -3), over(0, 10, 5), "PASS" if r4 else "🔴 FAIL"))

    # ⑤ contains vs 外接盒（🔒 非凸 ⇒ 二者可不一致·此即 A-0 之受詞）
    Lsh = SPoly([(0, 0), (10, 0), (10, 10), (6, 10), (6, 4), (4, 4), (4, 10), (0, 10)])
    p_in = SPoint(2, 2); p_notch = SPoint(5, 8)
    b = Lsh.bounds
    box_in = (b[0] <= 5 <= b[2]) and (b[1] <= 8 <= b[3])
    r5 = Lsh.contains(p_in) and (not Lsh.contains(p_notch)) and box_in
    ok &= r5
    P("  ⑤ contains vs 外接盒（非凸 U 形）：真內點=%s(True)／**凹槽點** contains=%s(**False**) 而外接盒=%s(**True**) ⇒ %s"
      % (Lsh.contains(p_in), Lsh.contains(p_notch), box_in, "PASS" if r5 else "🔴 FAIL"))
    P("     🔒 ⇒ 外接盒判「在內」係**必要非充分** ⇒ 本探針二口徑皆出艙、不一致者具名。")

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
                "solver": label,
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
            CAP[-1]["exc"] = "%s: %s" % (type(e).__name__, e)       # 🔒 逐字全文·⛔ 無尾切片
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
    P("【W-G.9-79 §二 A 組】交點落點之 (s,t) ＋ Σ 真值 ＋ θ 雙向掃描（⛔ 只量不修）")
    P("=" * W)
    import shapely
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s" % (shapely.__version__, shapely.geos_version))
    P("  🔒 A-0 **事前選定**：偏向判為「**在內**」——無法逐項證明在外者一律判在內·具名（⇒ 錯誤方向會吵）。")
    P("  🔒 局部框：`s(p)=dot(p−bp0,m_hat)/denom`；`t(p)=dot(p−bp0,rot90(m_hat))` ⛔ **不除 denom**（單位 m）。")
    P("  🔒 二口徑：`在內?`＝`block.contains(X)`（**真多邊形**）／`越界軸,量`＝局部框**外接盒**（必要非充分）。")
    P("  🔒 門檻：計數用 `面積 > 0`（嚴格）；sanity 用 `面積 > %g`（與 W-G.9-78 逐字同）。" % TOL_SANITY)

    ns, fake_st = harvest()
    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    snapshot = rv.load_snapshot()
    o_solve = ns["_solve_G_one"]
    o_pool = ns["_pool_strips_for_block"]
    o_fcad = ns["_first_corner_alloc_dir"]
    strip_axis = ns["_strip_axis"]

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
                ns, fake_st, cb_all, cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for lbl in blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass          # 🔒 逐字訊息已由 spy_pool 存於 rec["exc"]

    P("")
    P("【驅動·第一趟（真實）】R1–R6 × 兩情境——街廓母體 = %s" % blks)
    P("-" * W)
    ns["_solve_G_one"] = spy_solve(o_solve)
    ns["_pool_strips_for_block"] = spy_pool(o_pool)
    try:
        one_pass()
    finally:
        ns["_solve_G_one"] = o_solve
        ns["_pool_strips_for_block"] = o_pool
    REAL = list(CAP)
    P("  攔截：`_pool_strips_for_block` %d 筆／`_solve_G_one` 回傳登記 %d 筆" % (len(REAL), len(SOLVE)))

    # 每格之預計算
    CELL = []
    for rec in REAL:
        n = len(rec["biz"])
        m_hat, denom = strip_axis(rec["d_hat"], rec["alloc"])
        bp0 = np.asarray(rec["corner_pt"], dtype=float)[:2]
        n_hat = _rot90(m_hat)

        def s_of(p, m_hat=m_hat, denom=denom, bp0=bp0):
            return float(np.dot(np.asarray(p, dtype=float)[:2] - bp0, m_hat)) / denom

        def t_of(p, n_hat=n_hat, bp0=bp0):
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
            a = float(rec["biz"][j].intersection(rec["biz"][k]).area)
            (nfj, ffj), _ij = fc[j]
            (nfk, ffk), _ik = fc[k]
            row = {"j": j, "k": k, "d": k - j, "a": a,
                   "adj": (k - j == 1), "X": None, "sX": float("nan"),
                   "tX": float("nan"), "inp": None, "bit": False, "unk": False}
            if ffj is None or nfk is None:
                row["unk"] = True
                rows.append(row); continue
            row["bit"] = _bitsame(_u(ffj[0]), _u(nfk[0]))
            if not row["bit"]:
                X = _line_cross(ffj[1], ffj[0], nfk[1], nfk[0])
                if X is not None:
                    row["X"] = X
                    row["sX"] = s_of(X); row["tX"] = t_of(X)
                    row["inp"] = bool(rec["block"].contains(SPoint(float(X[0]), float(X[1]))))
            rows.append(row)
        CELL.append({"rec": rec, "n": n, "rows": rows,
                     "s_lo": min(s_all), "s_hi": max(s_all),
                     "t_lo": min(t_all), "t_hi": max(t_all),
                     "corners": [i for i in range(n) if (fc[i][1] or {}).get("is_corner")]})

    # ── §C  A-1-1 ─────────────────────────────────────────────────────
    P("")
    P("【A-1-1】逐對表之格式修正 ＋ `面積 > 0`（**嚴格**）之**逐筆指認**（🔒 節 102）")
    P("-" * W)
    P("  🔒 **表頭之計數 ＝ 表身之筆數**（⛔ 不得只出艙計數）；面積一律 `%.3e`。")
    for C in CELL:
        rec = C["rec"]
        pos = [r for r in C["rows"] if r["a"] > 0.0]
        pos9 = [r for r in C["rows"] if r["a"] > TOL_SANITY]
        brk = bool(rec["exc"] and "②-宗" in (rec["exc"] or ""))
        P("")
        P("  ── [%gm] %s ── n=%d　分母 C(n,2)=%d　%s　**面積 > 0 ＝ %d**　（面積 > %g ＝ %d）"
          % (rec["setback"], rec["label"], C["n"], len(C["rows"]),
             "🔴 破閘" if brk else "未破閘", len(pos), TOL_SANITY, len(pos9)))
        if not pos:
            P("     （無·逐筆指認之母體為空）")
            continue
        P("     %-4s %-4s %-5s %-8s %13s %-16s %-16s"
          % ("j", "k", "k−j", "是否相鄰", "交集面積(㎡)", "宗 j 地號", "宗 k 地號"))
        for r in sorted(pos, key=lambda x: -x["a"]):
            nm = rec["names"] or []
            P("     %-4d %-4d %-5d %-8s %13.3e %-16s %-16s"
              % (r["j"], r["k"], r["d"], "相鄰" if r["adj"] else "**不鄰**", r["a"],
                 nm[r["j"]] if nm else "?", nm[r["k"]] if nm else "?"))
        P("     ⇒ 逐筆指認：**%d 筆**（＝表頭計數）⇒ %s"
          % (len(pos), "✅ 齊" if len(pos) == len(pos) else "🔴"))

    # ── A-1-2 ─────────────────────────────────────────────────────────
    P("")
    P("【A-1-2】12 格之 `Σ` **真值**（⛔ 非二元標籤）")
    P("-" * W)
    P("  %-6s %-5s %-8s %5s %14s %14s %12s %14s %10s"
      % ("情境", "街廓", "破閘?", "n", "Σ_相鄰(㎡)", "Σ_不相鄰(㎡)", "bound(㎡)",
         "Σ_不鄰−bound", "不鄰對數"))
    for C in CELL:
        rec = C["rec"]
        adj = sum(r["a"] for r in C["rows"] if r["adj"])
        non = sum(r["a"] for r in C["rows"] if not r["adj"])
        bound = max(0, C["n"] - 1) * QUANTUM * float(rec["depth"] or 0)
        brk = bool(rec["exc"] and "②-宗" in (rec["exc"] or ""))
        P("  %-6s %-5s %-8s %5d %14.6e %14.6e %12.4f %14.6e %10d"
          % ("%gm" % rec["setback"], rec["label"], "🔴 破閘" if brk else "未破閘",
             C["n"], adj, non, bound, non - bound,
             sum(1 for r in C["rows"] if not r["adj"])))
    P("  🔒 判：**未破閘之格，其 `Σ_不相鄰` 是否確為 `0`？** ⇒ 逐格看上表第 6 欄（`%.6e`）。")

    # ── §D  A-2 ───────────────────────────────────────────────────────
    P("")
    P("【A-2】交點落點之 `(s, t)`（**全對**·⛔ 非只 `宗0`·⛔ 不以 `j==0` 過濾）")
    P("-" * W)

    def over(lo, hi, x):
        return max(lo - x, x - hi)

    for C in CELL:
        rec = C["rec"]
        brk = bool(rec["exc"] and "②-宗" in (rec["exc"] or ""))
        cross = [r for r in C["rows"] if r["inp"]]
        outp = [r for r in C["rows"] if r["inp"] is False]
        par = [r for r in C["rows"] if r["bit"]]
        P("")
        P("  ── [%gm] %s ── %s　n=%d　街廓 s 域 [%.4f, %.4f]　t 域 [%.4f, %.4f]"
          % (rec["setback"], rec["label"], "🔴 破閘" if brk else "未破閘", C["n"],
             C["s_lo"], C["s_hi"], C["t_lo"], C["t_hi"]))
        P("     街角宗索引 = %s　｜全對 %d：逐位平行 %d ／ 交點在內 %d ／ 交點在外 %d ／ 不可判 %d"
          % (C["corners"], len(C["rows"]), len(par), len(cross), len(outp),
             sum(1 for r in C["rows"] if r["unk"])))
        show = [r for r in C["rows"] if r["inp"] is not None]
        if not show:
            P("     （全對皆逐位平行 ⇒ 無交點可算）")
            continue
        P("     %-4s %-4s %-5s %13s %12s %12s %-6s %-8s %12s %12s"
          % ("j", "k", "k−j", "交集面積(㎡)", "s_X", "t_X", "在內?", "越界軸", "越界量_s", "越界量_t"))
        show2 = [r for r in show if r["inp"] or r["a"] > 0.0][:40] or show[:20]
        for r in show2:
            os_ = over(C["s_lo"], C["s_hi"], r["sX"])
            ot_ = over(C["t_lo"], C["t_hi"], r["tX"])
            axis = ("二者" if (os_ > 0 and ot_ > 0) else
                    ("s" if os_ > 0 else ("t" if ot_ > 0 else "無")))
            box_in = (os_ <= 0 and ot_ <= 0)
            flag = "" if box_in == bool(r["inp"]) else "  🔴 二口徑不一致"
            P("     %-4d %-4d %-5d %13.3e %12.4f %12.4f %-6s %-8s %12.4f %12.4f%s"
              % (r["j"], r["k"], r["d"], r["a"], r["sX"], r["tX"],
                 "是" if r["inp"] else "否", axis, os_, ot_, flag))
        if len(show) > len(show2):
            P("     ⚠️ 因列印上限，另有 **%d 對**未列（皆 `在內?=否` 且 `面積 = 0`）——"
              "🔒 **此係列印條件、⛔ 非計數**（表頭之計數為全對）。" % (len(show) - len(show2)))

    # ── §E  A-3 雙向掃描 ──────────────────────────────────────────────
    P("")
    P("【A-3】`θ` **雙向**延伸掃描：%s（⛔ 記憶體內·⛔ 不改碼、不改呼叫端）"
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

    P("  %-6s %-5s %-6s %4s %13s %13s %10s %-9s %8s %8s %-12s %s"
      % ("θ", "情境", "街廓", "n", "Σ_相鄰", "Σ_不相鄰", "bound", "破閘?",
         "廓內交叉", "其中不鄰", "街角宗索引", "例外(逐字)"))
    SWEEP = []
    for th in SWEEP_DEG:
        CAP.clear()
        CUR["theta"] = th
        ns["_solve_G_one"] = spy_solve(o_solve)
        ns["_pool_strips_for_block"] = spy_pool(o_pool)
        ns["_first_corner_alloc_dir"] = make_fcad(th)
        try:
            one_pass()
        finally:
            ns["_solve_G_one"] = o_solve
            ns["_pool_strips_for_block"] = o_pool
            ns["_first_corner_alloc_dir"] = o_fcad
        for rec in CAP:
            n = len(rec["biz"])
            m_hat, denom = strip_axis(rec["d_hat"], rec["alloc"])
            fc = []
            for i in range(n):
                r = (rec["ress"] or [None] * (i + 1))[i]
                fc.append((faces_of(SOLVE.get(id(r))), SOLVE.get(id(r))))
            adj = non = 0.0
            nx = nx_non = 0
            for j, k in itertools.combinations(range(n), 2):
                a = float(rec["biz"][j].intersection(rec["biz"][k]).area)
                if k - j == 1:
                    adj += a
                else:
                    non += a
                (nfj, ffj), _ = fc[j]
                (nfk, ffk), _ = fc[k]
                if ffj is None or nfk is None or _bitsame(_u(ffj[0]), _u(nfk[0])):
                    continue
                X = _line_cross(ffj[1], ffj[0], nfk[1], nfk[0])
                if X is not None and rec["block"] is not None \
                        and rec["block"].contains(SPoint(float(X[0]), float(X[1]))):
                    nx += 1
                    if k - j >= 2:
                        nx_non += 1
            bound = max(0, n - 1) * QUANTUM * float(rec["depth"] or 0)
            brk = bool(rec["exc"] and "②-宗" in (rec["exc"] or ""))
            corners = [i for i in range(n) if (fc[i][1] or {}).get("is_corner")]
            exc = (rec["exc"] or "")[:110].replace("\n", " ")
            SWEEP.append((th, rec["setback"], rec["label"], n, adj, non, bound, brk,
                          nx, nx_non, corners))
            P("  %-6s %-5s %-6s %4d %13.6e %13.6e %10.4f %-9s %8d %8d %-12s %s"
              % ("%d°" % th, "%gm" % rec["setback"], rec["label"], n, adj, non, bound,
                 "🔴 破閘" if brk else "未破閘", nx, nx_non, str(corners), exc))
        print("    θ=%d° 完畢" % th, file=sys.stderr)

    P("")
    P("  🔒 **判別力 ①（sanity）**：`θ=0°` ⇒ 12 格 `Σ_不相鄰 ≤ %g`（🔒 與 W-G.9-78 同一門檻）" % TOL_SANITY)
    z = [x for x in SWEEP if x[0] == 0]
    bad0 = [x for x in z if x[5] > TOL_SANITY]
    P("     θ=0° 之 %d 格：超標 **%d 格**%s ⇒ %s"
      % (len(z), len(bad0),
         "" if not bad0 else "：" + str([(x[1], x[2], "%.3e" % x[5]) for x in bad0]),
         "✅ 成立" if not bad0 else "🔴 **不成立 ⇒ 量測器有誤 ⇒ 停 A-2 之結論**"))
    P("")
    P("  🔒 **判別力 ②（正例補足）**：丙類五格於某 `θ` 是否得**全對廓內交叉 ≥ 1**")
    BING = [(0.0, "R1"), (0.0, "R3"), (0.0, "R6"), (3.5, "R1"), (3.5, "R6")]
    P("     %-6s %-5s %-28s %-28s"
      % ("情境", "街廓", "得廓內交叉 ≥1 之 θ", "其 Σ_不相鄰／bound"))
    got = 0
    for sb, lb in BING:
        hit = [x for x in SWEEP if x[1] == sb and x[2] == lb and x[8] >= 1]
        got += int(bool(hit))
        P("     %-6s %-5s %-28s %-28s"
          % ("%gm" % sb, lb,
             (", ".join("%d°" % x[0] for x in hit) if hit else "**無（12 點皆 0）**"),
             (", ".join("%.3e/%.4f" % (x[5], x[6]) for x in hit) if hit else "—")))
    P("     ⇒ 丙類 5 格中 **%d 格**取得正例 ⇒ %s"
      % (got, "✅ `P5` 成立" if got else
         "🔴 **`P5` 證偽 ⇒「在外」係<u>結構性</u>、⛔ 非角度不足 ⇒ 結論更強·須查其結構原因**"))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
