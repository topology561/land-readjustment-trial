# -*- coding: utf-8 -*-
r"""**W-G.9-76 §二 A 組**：`GB-67` — `②-宗` 圍堵閘破量之**逐對拆解**（⛔ **只量不修**）。

## 受詞（施工單 `W-G.9-76` §二）
- **A-2** 逐對分解：`i`／`j`／序距 `|i−j|`／地號／**交集面積**，並與生產端所報之
  `biz_x` 對拍（`R2` `0m` ＝ **45.9766**·來源＝生產碼自身之 raise 訊息）。
- **A-3** `Σ_相鄰`（`|i−j|==1`）／`Σ_不相鄰`（`|i−j|≥2`）／`bound=(n−1)×0.005×depth`。
- **A-4** 每一交集面積 > 0 之對，其交集之 `minimum_rotated_rectangle` 短邊／長邊／短邊÷0.005。
- **A-5** 注入式標定：取一宗沿 `d_hat` 平移 `+0.005 m`（**探針記憶體內**·⛔ 不動倉內任何檔），
  重算 `biz_x` ⇒ `Δbiz_x` 與理論值 `0.005 × depth` 對照。

## 🔒 A-0　錯誤方向之**事前選定**（施工單 §二 A-0·節 98·⛔ 寫碼前先寫下）
本探針係**歸因**工具 ⇒ 其瑕疵若往「**少報重疊對**」錯，會使成因看起來比實際單純。
⇒ 🔒 **事前選定：偏向「多報」** —— **凡交集面積 > 0 者一律列入**，
   **⛔ 探針不設任何下限門檻、⛔ 不先行過濾**；分層（`>1e-9`／`>1e-6`／`>1e-3`／`>0.1`）
   **僅為呈現**，母體恆為全部 `C(n,2)` 對，且**逐塊出艙分母**（節 95）。

## 🔒 A-5 之受詞**事前選定**（⛔ 看到結果之前寫下·否則等同挑樣本）
- **選宗規則**：取該塊 **s 序第一個宗**（`s_min` 最小者）。
  🔒 **理由**：它**無 s-前驅** ⇒ 沿 `+d_hat` 平移**只會增加**其與後繼之重疊、
  **⛔ 不會同時減少**與前驅之重疊 ⇒ `Δbiz_x` 之歸因乾淨（⛔ 非淨額相消）。
- **理論對照值**：`0.005 × depth`（施工單所令）。
- **判別力（⛔ 二項全附）**：① `δ=0` ⇒ `Δbiz_x == 0`（**逐位**·證量測器無漂移）；
  ② `δ=0.005` ⇒ `Δbiz_x > 0` 且**同量級於** `0.005×depth`
  （🔒 「同量級」**事前定義** ＝ 比值落在 `[0.1, 10]`）。
  ⚠️ ② 不成立 ⇒ 上界公式之機制**未被實證** ⇒ **具名**，⛔ 不得推定。

## 🔒 索引語意（承 `W-G.9-37` A-1 實得·本批 §C 已重新現查）
`biz[i]` 之序 ＝ 生產端 `for _entry, _res in (left_results + right_results)` ⇒ **分組串接序**
（左組推進序 → 右組推進序），⛔ **非**沿正街之空間位置。
⇒ 🔒 故本檔於 A-3 除施工單所令之 `|i−j|` 欄外，**另附 `s 序相鄰` 補充欄**
（⛔ **非施工單所令**·具名為補充），以區辨「**編號相鄰**」與「**空間相鄰**」兩個母體。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修 `GB-67`、⛔ 不調上界、⛔ 不繞過該閘、⛔ 不改任何容差；
⛔ 不接入 `run_all`；⛔ 不覆寫任何既有 log（檔名含產生它之 commit 短碼）。

## ⚠️ 具名偏差（施工單 §二 指定 log 名為 `..._18959e1.log`）
本批實際基座 ＝ `e0be937`（＝ `18959e1` ＋ 純追加 docs commit；`app.py` blob 相同
`a9e5671d64d254907a0396f898f046d9d85e8283`）。檔名須含**真正產生它之 commit**
（`GB-68` 失效條件方向）⇒ 本檔輸出 `..._<實際 HEAD 短碼>.log`，**⛔ 不冒用 `18959e1`**。
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

from shapely.geometry import Polygon as SPoly                       # noqa: E402
from shapely.affinity import translate as SPtranslate               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 200
QUANTUM = 0.005          # 2dp 捨入半量子（生產碼 app.py:9172 之常數·⛔ 本檔不改它）
DELTA = 0.005            # A-5 之注入平移量（施工單所令）
SAME_ORDER_LO = 0.1      # 🔒 「同量級」之事前定義（下界）
SAME_ORDER_HI = 10.0     # 🔒 「同量級」之事前定義（上界）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception:                                               # noqa: BLE001
        return "UNKNOWN"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG976_biz_overlap_%s.log" % COMMIT)


# ─────────────────────────────────────────────────────────────────────────
# 量測原語（⛔ 面積另以 shoelace 自算·不單靠 `.area`）
# ─────────────────────────────────────────────────────────────────────────
def _polys_of(g):
    gt = getattr(g, "geom_type", None)
    if gt == "Polygon":
        return [g]
    if gt in ("MultiPolygon", "GeometryCollection"):
        return [p for p in getattr(g, "geoms", [])
                if getattr(p, "geom_type", None) == "Polygon"]
    return []


def _shoelace(g):
    """交集之面積·**自算**（含扣內環）⇒ 與 `.area` 互為對照。"""
    tot = 0.0
    for p in _polys_of(g):
        rings = [p.exterior] + list(p.interiors)
        for k, r in enumerate(rings):
            c = np.asarray(r.coords, dtype=float)
            if len(c) >= 2 and abs(c[0, 0] - c[-1, 0]) < 1e-15 and abs(c[0, 1] - c[-1, 1]) < 1e-15:
                c = c[:-1]
            if len(c) < 3:
                continue
            x, y = c[:, 0], c[:, 1]
            a = abs(0.5 * float(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))))
            tot += a if k == 0 else -a
    return tot


def _mrr_sides(g):
    """`minimum_rotated_rectangle` 之 (短邊, 長邊)。不可得 → (nan, nan)。"""
    try:
        r = g.minimum_rotated_rectangle
        c = np.asarray(r.exterior.coords, dtype=float)
    except Exception:                                               # noqa: BLE001
        return (float("nan"), float("nan"))
    if len(c) < 4:
        return (float("nan"), float("nan"))
    d = np.diff(c, axis=0)
    L = np.hypot(d[:, 0], d[:, 1])
    L = sorted(set(round(float(x), 9) for x in L if x > 0))
    if not L:
        return (float("nan"), float("nan"))
    return (L[0], L[-1])


def _nverts(g):
    n = 0
    for p in _polys_of(g):
        n += max(0, len(p.exterior.coords) - 1)
    return n


# ─────────────────────────────────────────────────────────────────────────
# 【0】量測器自檢（⛔ 先自檢後量測·每項附對照組）
# ─────────────────────────────────────────────────────────────────────────
def selfcheck(P, srange):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·各項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    # ① 交集面積：已知真（10×4 與其 +5 平移 ⇒ 交集 5×4 = 20）／已知偽（+20 平移 ⇒ 0）
    A = SPoly([(0, 0), (10, 0), (10, 4), (0, 4)])
    B = SPoly([(5, 0), (15, 0), (15, 4), (5, 4)])
    C = SPoly([(20, 0), (30, 0), (30, 4), (20, 4)])
    a1 = float(A.intersection(B).area)
    s1 = _shoelace(A.intersection(B))
    a0 = float(A.intersection(C).area)
    r1 = (abs(a1 - 20.0) < 1e-12) and (abs(s1 - 20.0) < 1e-12) and (abs(a0) < 1e-15)
    ok &= r1
    P("  ① 交集面積  已知真 shapely=%.9f／shoelace=%.9f（期望 20）　已知偽=%.9f（期望 0）⇒ %s"
      % (a1, s1, a0, "PASS" if r1 else "🔴 FAIL"))

    # ② MRR 短/長邊：以**傾斜**矩形自檢（⛔ 不以軸向矩形自檢一個須處理斜交之量測器）
    th = math.radians(23.0)
    ct, st_ = math.cos(th), math.sin(th)
    W0, H0 = 7.0, 2.5
    pts = [(0, 0), (W0, 0), (W0, H0), (0, H0)]
    rot = SPoly([(x * ct - y * st_, x * st_ + y * ct) for x, y in pts])
    sh, lo = _mrr_sides(rot)
    r2 = abs(sh - H0) < 1e-9 and abs(lo - W0) < 1e-9
    ok &= r2
    P("  ② MRR（傾斜 23°·7.0×2.5）短邊=%.9f（期望 2.5）／長邊=%.9f（期望 7.0）⇒ %s"
      % (sh, lo, "PASS" if r2 else "🔴 FAIL"))
    #    對照組（已知偽）：若誤以**軸向外接框**量，同一傾斜矩形之短邊會變大
    bx = rot.bounds
    r2b = (bx[3] - bx[1]) > H0 + 0.5
    P("     對照（已知偽·軸向外接框）：高=%.6f ≠ 2.5 ⇒ 判別力 %s"
      % (bx[3] - bx[1], "PASS" if r2b else "🔴 FAIL"))
    ok &= r2b

    # ③ s 軸平移恆等：平移 δ·d_hat ⇒ s 區間恰移 δ（＝ A-5 之機制於合成資料上先證）
    d_hat = np.array([0.675686, 0.737190])
    d_hat = d_hat / np.linalg.norm(d_hat)
    alloc = np.array([0.726019, 0.687675])
    cp = np.array([0.0, 0.0])
    base = srange(rot, d_hat, cp, alloc)
    mv = SPtranslate(rot, xoff=DELTA * float(d_hat[0]), yoff=DELTA * float(d_hat[1]))
    aft = srange(mv, d_hat, cp, alloc)
    d_lo = aft[0] - base[0]
    d_hi = aft[1] - base[1]
    r3 = abs(d_lo - DELTA) < 1e-12 and abs(d_hi - DELTA) < 1e-12
    ok &= r3
    P("  ③ s 平移恆等（斜交軸·δ=%.4f）Δs_min=%.12f／Δs_max=%.12f（期望 %.4f）⇒ %s"
      % (DELTA, d_lo, d_hi, DELTA, "PASS" if r3 else "🔴 FAIL"))
    mv0 = SPtranslate(rot, xoff=0.0, yoff=0.0)
    b0 = srange(mv0, d_hat, cp, alloc)
    r3b = abs(b0[0] - base[0]) < 1e-15 and abs(b0[1] - base[1]) < 1e-15
    ok &= r3b
    P("     對照（已知偽·δ=0 須零漂移）Δs=%.15e ⇒ 判別力 %s"
      % (b0[0] - base[0], "PASS" if r3b else "🔴 FAIL"))

    P("  ⇒ 量測器自檢：%s" % ("PASS" if ok else "🔴 FAIL（⛔ 以下量測結果不得採信）"))
    return ok


# ─────────────────────────────────────────────────────────────────────────
# 攔截：`_pool_strips_for_block`（⛔ 於呼叫 orig **之前**存檔 ⇒ raise 亦有資料）
# ─────────────────────────────────────────────────────────────────────────
CAP = []
CUR = {"setback": None}


def make_spy(orig):
    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        # ── 地號對齊：自呼叫端 frame 取 `left_results`／`right_results`（⛔ 非猜測）
        names, align = None, "🔴 未對上"
        try:
            lv = sys._getframe(1).f_locals
            lr, rr = lv.get('left_results'), lv.get('right_results')
            ap = lv.get('allocated_polys')
            if isinstance(lr, list) and isinstance(rr, list):
                nm = []
                for _entry, _res in (lr + rr):
                    _coords = (_res or {}).get('cut_coords') or []
                    _p = None
                    if len(_coords) >= 3:
                        try:
                            _p = SPoly(_coords)
                            if not _p.is_valid:
                                _p = _p.buffer(0)
                        except Exception:                           # noqa: BLE001
                            _p = None
                    if _p is not None and not _p.is_empty:
                        nm.append(((_entry or {}).get('tp') or {}).get('暫編地號', '?'))
                if ap is biz_polys and len(nm) == len(list(biz_polys or [])):
                    names, align = nm, "✅ 逐位對齊"
                elif len(nm) == len(list(biz_polys or [])):
                    names, align = nm, "⚠️ 數相等但非同一物件"
        except Exception as e:                                      # noqa: BLE001
            align = "🔴 未對上（%s）" % type(e).__name__
        rec = {
            "setback": CUR["setback"], "label": _label,
            "biz": list(biz_polys or []), "depth": _depth,
            "d_hat": d_hat, "corner_pt": corner_pt, "alloc": allocation_dir,
            "block": block_poly, "names": names, "align": align, "prod_exc": None,
        }
        CAP.append(rec)
        try:
            return orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                        _label=_label, _depth=_depth, _verbose=_verbose)
        except Exception as e:                                      # noqa: BLE001
            rec["prod_exc"] = "%s: %s" % (type(e).__name__, e)
            raise
    return _spy


def _prod_bizx(rec):
    """自生產碼**自身之 raise 訊息**取其所報 `biz_x`／`bound`（⛔ 獨立於本探針之算）。"""
    t = rec.get("prod_exc") or ""
    if "②-宗 圍堵閘破" not in t:
        return (None, None)
    try:
        seg = t.split("宗-宗重疊 =", 1)[1]
        bx = float(seg.split(">", 1)[0].strip())
        bd = float(seg.split("上界", 1)[1].split("（", 1)[0].strip())
        return (bx, bd)
    except Exception:                                               # noqa: BLE001
        return (None, None)


# ─────────────────────────────────────────────────────────────────────────
def analyse(rec, srange):
    """逐塊：全對 C(n,2) 之交集（⛔ 無門檻）＋ 相鄰／不相鄰分解 ＋ 形狀。"""
    biz = rec["biz"]
    n = len(biz)
    depth = float(rec["depth"]) if rec["depth"] else float("nan")
    bound = max(0, n - 1) * QUANTUM * depth
    pairs = []
    total = 0.0
    for i, j in itertools.combinations(range(n), 2):
        g = biz[i].intersection(biz[j])
        a = float(g.area)
        total += a
        if a > 0.0:
            sh_, lo_ = _mrr_sides(g)
            pairs.append({"i": i, "j": j, "d": j - i, "a": a, "sl": _shoelace(g),
                          "type": getattr(g, "geom_type", "?"), "nv": _nverts(g),
                          "short": sh_, "long": lo_})
    # s 序（補充欄·⛔ 非施工單所令）
    sr = []
    for k, p in enumerate(biz):
        r = srange(p, rec["d_hat"], rec["corner_pt"], rec["alloc"])
        sr.append((r[0] if r else float("inf"), r[1] if r else float("inf"), k))
    order = [k for _, _, k in sorted(sr)]
    rank = {k: q for q, k in enumerate(order)}
    return {"n": n, "depth": depth, "bound": bound, "total": total,
            "pairs": pairs, "npair": n * (n - 1) // 2,
            "srange": {k: (sr[k][0], sr[k][1]) for k in range(n)},
            "order": order, "rank": rank}


def a5_calibrate(rec, res):
    """A-5 注入式標定：s 序第一個宗沿 +d_hat 平移 δ ⇒ Δbiz_x。"""
    biz, n = rec["biz"], res["n"]
    if n < 2:
        return None
    i0 = res["order"][0]
    d = np.asarray(rec["d_hat"], dtype=float)
    d = d / float(np.linalg.norm(d))
    out = {}
    for tag, delta in (("δ=0", 0.0), ("δ=%.3f" % DELTA, DELTA)):
        mv = list(biz)
        mv[i0] = SPtranslate(biz[i0], xoff=delta * float(d[0]), yoff=delta * float(d[1]))
        tot = 0.0
        for i, j in itertools.combinations(range(n), 2):
            tot += float(mv[i].intersection(mv[j]).area)
        out[tag] = tot
    base = res["total"]
    # 🔒 A-5-a：i* 至其 **s-後繼** 之間隙（⇒ 若 gap ≥ δ，平移 δ 造不出重疊 ＝ **量測所得**，
    #    ⛔ 非推定）。next_ = s 序之次一宗。
    nxt = res["order"][1] if len(res["order"]) > 1 else None
    gap = float("nan")
    if nxt is not None:
        gap = res["srange"][nxt][0] - res["srange"][i0][1]
    return {"i0": i0, "d0": out["δ=0"] - base,
            "d1": out["δ=%.3f" % DELTA] - base,
            "theory": QUANTUM * res["depth"], "nxt": nxt, "gap": gap}


# ─────────────────────────────────────────────────────────────────────────
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
    P("【W-G.9-76 §二 A 組】`GB-67`：`②-宗` 破量之逐對拆解（⛔ 只量不修）")
    P("=" * W)
    import shapely
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s" % (shapely.__version__, shapely.geos_version))
    P("  🔒 A-0 錯誤方向**事前選定**：偏向**多報** ⇒ 凡交集面積 > 0 一律列入、⛔ 無下限門檻。")
    P("  🔒 A-5 選宗規則**事前選定**：s 序**第一個**宗（無 s-前驅 ⇒ 平移只增不減·歸因乾淨）。")
    P("  🔒 「同量級」**事前定義** ＝ 比值 ∈ [%.1f, %.1f]。" % (SAME_ORDER_LO, SAME_ORDER_HI))
    P("  🔒 索引語意：`biz[i]` 序 ＝ `left_results + right_results` 分組串接，⛔ 非空間位置。")

    ns, fake_st = harvest()
    srange = ns["_strip_s_range"]

    if not selfcheck(P, srange):
        P("")
        P("🔴 量測器自檢未全綠 ⇒ ⛔ 停止量測（⛔ 不得以未自檢之器出艙數字）。")
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    snapshot = rv.load_snapshot()
    _orig = ns["_pool_strips_for_block"]
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

    P("")
    P("【驅動】R1–R6 × 兩情境之實跑（⛔ 六塊全跑·⛔ 不只跑 R2）——街廓母體 = %s" % blks)
    P("-" * W)
    ns["_pool_strips_for_block"] = make_spy(_orig)
    try:
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
                        pass
                print("    [%gm] %s 完畢" % (setback, lbl), file=sys.stderr)
    finally:
        ns["_pool_strips_for_block"] = _orig

    P("  攔截筆數 = %d（＝ 情境 × 街廓 之呼叫次數）" % len(CAP))

    RES = []
    for rec in CAP:
        RES.append((rec, analyse(rec, srange)))

    # ── §D  A-2 逐對分解 ────────────────────────────────────────────────
    P("")
    P("【A-2】逐對分解（⛔ 無下限門檻·⛔ 不得只報總和）")
    P("-" * W)
    P("  🔒 母體 ＝ 每塊全部 `C(n,2)` 對；下表列**交集面積 > 0** 之全部對，")
    P("     面積 == 0 之對僅計數（其對 Σ 之貢獻恆為 0）⇒ **分母逐塊出艙**（節 95）。")
    for rec, r in RES:
        bx, bd = _prod_bizx(rec)
        P("")
        P("  ── [%gm] %s ── n_biz=%d　分母 C(n,2)=%d　depth=%.4f　bound=(n−1)×%.3f×depth=%.4f"
          % (rec["setback"], rec["label"], r["n"], r["npair"], r["depth"], QUANTUM, r["bound"]))
        P("     地號對齊：%s" % rec["align"])
        P("     Σ 全對（本探針）= %.6f　｜　面積>0 之對數 = %d ／ %d　（面積==0 之對 = %d）"
          % (r["total"], len(r["pairs"]), r["npair"], r["npair"] - len(r["pairs"])))
        if bx is not None:
            dd = abs(r["total"] - bx)
            P("     🔒 **生產端所報** biz_x = %.4f（來源＝`app.py:9175` 之 raise 訊息·⛔ 獨立於本探針）"
              "　｜上界 %.4f　｜對拍 |Δ| = %.6f ⇒ %s"
              % (bx, bd, dd, "✅ 相符（容差 1e-4）" if dd <= 1e-4 else "🔴 不符"))
        else:
            P("     ⚠️ 生產端**未報** biz_x（本塊未破閘 ⇒ 無 raise 訊息）⇒ 對拍**不可行**·具名。")
        # 分層（A-0：僅呈現·⛔ 非過濾）
        for lo in (1e-9, 1e-6, 1e-3, 0.1):
            sub = [p for p in r["pairs"] if p["a"] > lo]
            P("       分層 >%-6g：對數 %3d　Σ = %.6f" % (lo, len(sub), sum(p["a"] for p in sub)))
        if r["pairs"]:
            P("     %-4s %-4s %-6s %-16s %-16s %14s %14s" %
              ("i", "j", "|i−j|", "宗 i 地號", "宗 j 地號", "交集面積", "shoelace"))
            nm = rec["names"]
            for p in sorted(r["pairs"], key=lambda x: -x["a"]):
                ni = nm[p["i"]] if nm else "未對上"
                nj = nm[p["j"]] if nm else "未對上"
                P("     %-4d %-4d %-6d %-16s %-16s %14.6f %14.6f"
                  % (p["i"], p["j"], p["d"], ni, nj, p["a"], p["sl"]))

    # ── §E  A-3 相鄰／不相鄰 ────────────────────────────────────────────
    P("")
    P("【A-3】相鄰／不相鄰之分解（`|i−j|` ＝ 施工單所令；`s 序` ＝ 🔒 **補充欄·⛔ 非施工單所令**）")
    P("-" * W)
    P("  %-6s %-5s %4s %10s %12s %12s %12s %9s %12s %12s"
      % ("情境", "街廓", "n", "bound", "Σ全對", "Σ_相鄰", "Σ_不相鄰", "不相鄰佔比",
         "Σ_s序相鄰", "Σ_s序不相鄰"))
    for rec, r in RES:
        adj = sum(p["a"] for p in r["pairs"] if p["d"] == 1)
        non = sum(p["a"] for p in r["pairs"] if p["d"] >= 2)
        sa = sum(p["a"] for p in r["pairs"]
                 if abs(r["rank"][p["i"]] - r["rank"][p["j"]]) == 1)
        sn = r["total"] - sa
        frac = ("%8.2f%%" % (non / r["total"] * 100.0)) if r["total"] > 0 else "       —"
        P("  %-6s %-5s %4d %10.4f %12.6f %12.6f %12.6f %9s %12.6f %12.6f"
          % ("%gm" % rec["setback"], rec["label"], r["n"], r["bound"],
             r["total"], adj, non, frac, sa, sn))
    P("")
    P("  判（⛔ 只判不改）：`Σ_相鄰 ≤ bound`？")
    for rec, r in RES:
        adj = sum(p["a"] for p in r["pairs"] if p["d"] == 1)
        P("    [%gm] %-4s Σ_相鄰 = %.6f　vs bound = %.4f ⇒ %s"
          % (rec["setback"], rec["label"], adj, r["bound"],
             "✅ ≤ bound" if adj <= r["bound"] + 1e-9 else "🔴 > bound"))

    # ── A-3-a  破量塊之 s 位置與「中間隔了哪幾宗」（🔒 補充·⛔ 非施工單所令）────
    P("")
    P("【A-3-a】🔒 **補充（⛔ 非施工單所令）**：破量塊之逐宗 s 位置 ＋ 破量對之「中間隔了哪幾宗」")
    P("-" * W)
    P("  🔒 目的：`GB-67` 之新受詞為「**不相鄰**之宗之間為何會重疊」⇒ 須先坐實「不相鄰」")
    P("     **⛔ 不只是編號不相鄰**（`|i−j|`），**空間上（s 序）亦不相鄰**。")
    P("  🔒 「中間隔了哪幾宗」＝ s 序 rank 嚴格介於二者之間之宗（⛔ 非編號減法）。")
    for rec, r in RES:
        if r["total"] <= 1e-6:
            continue
        P("")
        P("  ── [%gm] %s ── s 序（由小而大）＝ %s" % (rec["setback"], rec["label"], r["order"]))
        nm = rec["names"]
        P("     %-4s %-6s %-16s %14s %14s %10s" % ("i", "s序rank", "地號", "s_min", "s_max", "s 寬"))
        for k in r["order"]:
            lo_, hi_ = r["srange"][k]
            P("     %-4d %-6d %-16s %14.4f %14.4f %10.4f"
              % (k, r["rank"][k], (nm[k] if nm else "未對上"), lo_, hi_, hi_ - lo_))
        P("     %-10s %-8s %-10s %-24s %s"
          % ("對", "|i−j|", "s序rank差", "中間隔了哪幾宗(s序)", "交集面積"))
        for p in sorted(r["pairs"], key=lambda x: -x["a"]):
            ri, rj = r["rank"][p["i"]], r["rank"][p["j"]]
            lo_, hi_ = min(ri, rj), max(ri, rj)
            btw = [k for k in r["order"] if lo_ < r["rank"][k] < hi_]
            P("     宗%-3d×宗%-3d %-8d %-10d %-24s %.6f"
              % (p["i"], p["j"], p["d"], abs(ri - rj),
                 (str(btw) if btw else "（無）"), p["a"]))

    # ── §F  A-4 形狀 ────────────────────────────────────────────────────
    P("")
    P("【A-4】重疊之**形狀**判別（⛔ 只判不修·判準＝ MRR 短邊 ÷ %.3f）" % QUANTUM)
    P("-" * W)
    P("  判準：短邊/%.3f ≲ 1 ⇒ **捨入相容**；≫ 1 ⇒ 🔴 **構造塊**；"
      "非單一 Polygon ⇒ ⚠️ **不可判**（具名·⛔ 不推定）。" % QUANTUM)
    P("  🔒 「≲ 1」**事前定義** ＝ 短邊/%.3f ≤ 2.0；「≫ 1」＝ ≥ 10.0；"
      "落於 (2.0, 10.0) 者判 ⚠️ **不可判·具名**。" % QUANTUM)
    P("  %-6s %-5s %-4s %-4s %-6s %13s %11s %11s %11s %-10s %-14s"
      % ("情境", "街廓", "i", "j", "|i−j|", "交集面積", "MRR短邊", "MRR長邊",
         "短邊/%.3f" % QUANTUM, "幾何型", "判"))
    ncnt = {"捨入相容": 0, "構造塊": 0, "不可判": 0}
    for rec, r in RES:
        for p in sorted(r["pairs"], key=lambda x: -x["a"]):
            ratio = p["short"] / QUANTUM if p["short"] == p["short"] else float("nan")
            if p["type"] != "Polygon" or ratio != ratio:
                v = "⚠️ 不可判"
                ncnt["不可判"] += 1
            elif ratio <= 2.0:
                v = "捨入相容"
                ncnt["捨入相容"] += 1
            elif ratio >= 10.0:
                v = "🔴 構造塊"
                ncnt["構造塊"] += 1
            else:
                v = "⚠️ 不可判(帶間)"
                ncnt["不可判"] += 1
            P("  %-6s %-5s %-4d %-4d %-6d %13.6f %11.6f %11.6f %11.2f %-10s %-14s"
              % ("%gm" % rec["setback"], rec["label"], p["i"], p["j"], p["d"],
                 p["a"], p["short"], p["long"], ratio, p["type"], v))
    tot_pairs = sum(len(r["pairs"]) for _, r in RES)
    P("  ⇒ 分母 = %d 對（全部交集面積>0 者）：捨入相容 %d／🔴 構造塊 %d／⚠️ 不可判 %d"
      % (tot_pairs, ncnt["捨入相容"], ncnt["構造塊"], ncnt["不可判"]))

    # ── §G  A-5 注入式標定 ──────────────────────────────────────────────
    P("")
    P("【A-5】注入式標定（⛔ 於探針記憶體內平移·⛔ 不動倉內任何檔）")
    P("-" * W)
    P("  🔒 A-5-a（補充·⛔ 非施工單所令）：另量 `i*` 至其 **s-後繼** 之間隙 `gap`——")
    P("     若 `gap ≥ δ`，平移 δ **在幾何上造不出新重疊** ⇒ ② 之紅係**受詞選樣所致**；")
    P("     ⛔ **此係量測所得、非推定**（施工單：② 不成立須具名·⛔ 不得推定）。")
    P("  %-6s %-5s %-7s %-7s %10s %16s %16s %14s %8s %-16s"
      % ("情境", "街廓", "選宗 i*", "s-後繼", "gap", "Δbiz_x(δ=0)", "Δbiz_x(δ=0.005)",
         "理論 0.005×depth", "比值", "判別力"))
    a5n = {"j1": 0, "j2": 0, "tot": 0, "gap_ge": 0}
    for rec, r in RES:
        c = a5_calibrate(rec, r)
        if c is None:
            P("  %-6s %-5s %-7s %-7s %10s %16s %16s %14s %8s %-16s"
              % ("%gm" % rec["setback"], rec["label"], "—", "—", "—", "—", "—", "—", "—",
                 "⚠️ n<2 ⇒ 不適用·具名"))
            continue
        a5n["tot"] += 1
        ratio = (c["d1"] / c["theory"]) if c["theory"] else float("nan")
        j1 = abs(c["d0"]) < 1e-12
        j2 = (c["d1"] > 0) and (SAME_ORDER_LO <= ratio <= SAME_ORDER_HI)
        a5n["j1"] += int(j1)
        a5n["j2"] += int(j2)
        if c["gap"] == c["gap"] and c["gap"] >= DELTA:
            a5n["gap_ge"] += 1
        P("  %-6s %-5s %-7d %-7s %10.4f %16.9f %16.6f %14.6f %8.3f %-16s"
          % ("%gm" % rec["setback"], rec["label"], c["i0"],
             ("宗%d" % c["nxt"]) if c["nxt"] is not None else "—", c["gap"],
             c["d0"], c["d1"], c["theory"], ratio,
             ("①%s ②%s" % ("✅" if j1 else "🔴", "✅" if j2 else "🔴"))))
    P("  ⇒ 分母 %d 格：判別力 ① %d／%d　判別力 ② %d／%d　其中 `gap ≥ δ(%.3f)` 者 %d 格"
      % (a5n["tot"], a5n["j1"], a5n["tot"], a5n["j2"], a5n["tot"], DELTA, a5n["gap_ge"]))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
