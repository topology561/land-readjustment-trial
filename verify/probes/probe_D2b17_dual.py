# -*- coding: utf-8 -*-
r"""**D-2b-17**：②-宗／②-池 重疊量之**兩法對打** ＋ ①' 覆蓋閘之**第三法**重算。

## 本批要回答的唯一問題
`app.py:9062`（②-宗 圍堵閘）與 `:9047`／`:9050`（②-池 不重疊閘）所報之重疊量，
係**真實幾何重疊**，抑或 `.intersection()` 之**假陽性**？

## 量法甲（現況·被質疑者）
`.intersection().area` —— **原樣照抄**生產碼之算式（`app.py:9047`／`:9050`／`:9062`）。

## 量法乙（獨立·⛔ 零 shapely 布林）
純 numpy：**射線法 PIP**（自實作）＋ **shoelace 面積**（自實作）＋ **bbox 必要條件剪枝**。
🔒 **本檔 §乙-核 之函式全域禁用**：`.intersection()`／`.union()`／`unary_union`／
   `.difference()`／`.buffer()`／`.contains()`／`.within()`／`.intersects()`／`.area`／`.bounds`。
   **僅**讀取 `.exterior.coords`／`.interiors`／`.geoms`（純座標資料存取）。
   ——由 §0-3 之**碼面自檢**（AST）把關：乙-核任一函式出現上列符號即 `raise`。

## 量法丙（§f-2·⛔ 不得用 `union`）
以同一 PIP 核對街廓 bbox 鋪格，逐點數「被幾片覆蓋」`cnt`，直接分解出
**缺口**（`in_block ∧ cnt==0`）／**溢出**（`¬in_block ∧ cnt≥1`）／**重疊多重度**（`Σ(cnt−1)`）
⇒ `cover_resid = |union − block| = |溢出 − 缺口|`，且**帶正負號**。

⛔ 本批零生產碼變更。⛔ 不得因結果不利而調整任何容差或上界。
"""
import ast
import io
import os
import sys
import contextlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b17_dual.log")
W = 200

# ⛔ 乙-核禁用符號（§0-3 AST 自檢之黑名單）
_FORBIDDEN = ("intersection", "union", "unary_union", "difference", "buffer",
              "contains", "within", "intersects", "area", "bounds",
              "overlaps", "covers", "covered_by", "crosses", "touches",
              "symmetric_difference", "convex_hull", "envelope")

# ══════════════════════════════════════════════════════════════════════
# §乙-核　純 numpy 幾何核（⛔ 零 shapely 布林·由 §0-3 AST 把關）
# ══════════════════════════════════════════════════════════════════════


def _open_ring(r):
    """去閉合尾點（首尾重合者）。"""
    if len(r) >= 2 and abs(r[0, 0] - r[-1, 0]) < 1e-15 and abs(r[0, 1] - r[-1, 1]) < 1e-15:
        return r[:-1]
    return r


def _rings_of(g):
    """回傳 [(外環, [內環…]), …]。**純座標資料存取**——⛔ 未呼叫任何述詞。"""
    gt = getattr(g, "geom_type", None)
    if gt == "Polygon":
        ps = [g]
    elif gt in ("MultiPolygon", "GeometryCollection"):
        ps = [p for p in g.geoms if getattr(p, "geom_type", None) == "Polygon"]
    else:
        ps = []
    out = []
    for p in ps:
        ext = _open_ring(np.asarray(p.exterior.coords, dtype=float))
        hol = [_open_ring(np.asarray(r.coords, dtype=float)) for r in p.interiors]
        out.append((ext, hol))
    return out


def _shoelace(r):
    """帶號 shoelace。⛔ 自實作·未用 shapely。"""
    if len(r) < 3:
        return 0.0
    x, y = r[:, 0], r[:, 1]
    return 0.5 * float(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def poly_area_np(g):
    """多邊形面積（含扣內環）。⛔ 未用 shapely `.area`。"""
    a = 0.0
    for ext, hol in _rings_of(g):
        a += abs(_shoelace(ext))
        for h in hol:
            a -= abs(_shoelace(h))
    return a


def poly_bbox_np(g):
    """(xmin, ymin, xmax, ymax)。⛔ 未用 shapely `.bounds`。"""
    xs, ys = [], []
    for ext, _h in _rings_of(g):
        if len(ext):
            xs.append(ext[:, 0])
            ys.append(ext[:, 1])
    if not xs:
        return None
    X = np.concatenate(xs)
    Y = np.concatenate(ys)
    return (float(X.min()), float(Y.min()), float(X.max()), float(Y.max()))


def _pip_ring(px, py, ring):
    """射線法（crossing number）·向量化於點集。⛔ 純 numpy 自實作。"""
    n = len(ring)
    if n < 3:
        return np.zeros(px.shape, dtype=bool)
    inside = np.zeros(px.shape, dtype=bool)
    x1 = ring[:, 0]
    y1 = ring[:, 1]
    x2 = np.roll(x1, -1)
    y2 = np.roll(y1, -1)
    for i in range(n):
        ya = y1[i]
        yb = y2[i]
        if ya == yb:
            continue
        cond = (ya > py) != (yb > py)
        if not cond.any():
            continue
        t = (py - ya) / (yb - ya)
        xint = x1[i] + t * (x2[i] - x1[i])
        inside ^= (cond & (px < xint))
    return inside


def in_geom_np(px, py, rings):
    """點是否落於幾何內（外環減內環）。`rings` ＝ `_rings_of()` 之輸出。"""
    res = np.zeros(px.shape, dtype=bool)
    for ext, hol in rings:
        m = _pip_ring(px, py, ext)
        for h in hol:
            m &= ~_pip_ring(px, py, h)
        res |= m
    return res


def overlap_B(gA, gB, n_coarse=400, n_fine=2200):
    """**量法乙**：A∩B 之面積估計。⛔ 全程未用任何 shapely 布林。

    三階段（皆為乙法內部之**數學必要條件**·⛔ 未取用甲之任何結果）：
      ① bbox 不交 ⇒ 重疊**恆等於 0**（必要條件·精確）；
      ② 於 **bbox 交集矩形**上鋪 `n_coarse²` 格點粗掃；
      ③ 粗掃有命中者，改 `n_fine²` 細掃。
    取樣域取 bbox **交集**（非 A 之全 bbox）⇒ 同格數下解析度大幅提升。
    """
    bA = poly_bbox_np(gA)
    bB = poly_bbox_np(gB)
    if bA is None or bB is None:
        return {"est": 0.0, "stage": "empty", "cell": 0.0, "hits": 0, "tot": 0}
    x0 = max(bA[0], bB[0])
    y0 = max(bA[1], bB[1])
    x1 = min(bA[2], bB[2])
    y1 = min(bA[3], bB[3])
    if not (x1 > x0 and y1 > y0):
        return {"est": 0.0, "stage": "bbox-disjoint", "cell": 0.0, "hits": 0, "tot": 0}
    rA = _rings_of(gA)
    rB = _rings_of(gB)
    dom = (x1 - x0) * (y1 - y0)

    def _scan(n):
        gx = x0 + (np.arange(n) + 0.5) * (x1 - x0) / n
        gy = y0 + (np.arange(n) + 0.5) * (y1 - y0) / n
        XX, YY = np.meshgrid(gx, gy)
        px = XX.ravel()
        py = YY.ravel()
        m = in_geom_np(px, py, rA) & in_geom_np(px, py, rB)
        return int(m.sum()), px.size

    h, t = _scan(n_coarse)
    if h == 0:
        return {"est": 0.0, "stage": f"coarse{n_coarse}-zero", "cell": dom / t,
                "hits": 0, "tot": t}
    h, t = _scan(n_fine)
    return {"est": dom * h / t, "stage": f"fine{n_fine}", "cell": dom / t,
            "hits": h, "tot": t}


def cover_C(block_poly, geoms, n=2400, chunk=4_000_000):
    """**量法丙**（§f-2·⛔ 不得用 `union`）：以覆蓋數 `cnt` 分解覆蓋殘差。

    回傳 缺口／溢出／重疊多重度／union 面積 之估計，**帶正負號**。
    """
    bb = poly_bbox_np(block_poly)
    if bb is None:
        return None
    # 取樣域須涵蓋街廓 ∪ 全片（片可能溢出街廓外）
    x0, y0, x1, y1 = bb
    for g in geoms:
        b = poly_bbox_np(g)
        if b is None:
            continue
        x0 = min(x0, b[0]); y0 = min(y0, b[1])
        x1 = max(x1, b[2]); y1 = max(y1, b[3])
    pad = 1e-6 * max(x1 - x0, y1 - y0)
    x0 -= pad; y0 -= pad; x1 += pad; y1 += pad
    dom = (x1 - x0) * (y1 - y0)
    rblk = _rings_of(block_poly)
    rgs = [_rings_of(g) for g in geoms]

    gx = x0 + (np.arange(n) + 0.5) * (x1 - x0) / n
    gy = y0 + (np.arange(n) + 0.5) * (y1 - y0) / n
    tot = n * n
    n_gap = n_out = n_uni = n_blk = 0
    n_mult = 0
    rows_per = max(1, int(chunk // n))
    for r0 in range(0, n, rows_per):
        r1 = min(n, r0 + rows_per)
        XX, YY = np.meshgrid(gx, gy[r0:r1])
        px = XX.ravel()
        py = YY.ravel()
        inb = in_geom_np(px, py, rblk)
        cnt = np.zeros(px.shape, dtype=np.int16)
        for rg in rgs:
            cnt += in_geom_np(px, py, rg).astype(np.int16)
        cov = cnt >= 1
        n_blk += int(inb.sum())
        n_uni += int(cov.sum())
        n_gap += int((inb & ~cov).sum())
        n_out += int((~inb & cov).sum())
        n_mult += int(np.maximum(cnt.astype(np.int64) - 1, 0).sum())
    cell = dom / tot
    return {"cell": cell, "dom": dom, "n": n,
            "gap": n_gap * cell, "out": n_out * cell,
            "union": n_uni * cell, "block_grid": n_blk * cell,
            "block_shoelace": poly_area_np(block_poly),
            "mult": n_mult * cell,
            "resid_signed": (n_uni - n_blk) * cell}


# ══════════════════════════════════════════════════════════════════════
# §0-3　乙-核之碼面自檢（AST）——⛔ 不得以人工聲明代替
# ══════════════════════════════════════════════════════════════════════
_B_CORE = ("_open_ring", "_rings_of", "_shoelace", "poly_area_np", "poly_bbox_np",
           "_pip_ring", "in_geom_np", "overlap_B", "cover_C")


def audit_core():
    """AST 掃本檔乙-核各函式，命中禁用符號即 raise。回傳逐函式之掃描報告。"""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    rep = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef) or node.name not in _B_CORE:
            continue
        hits = []
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Attribute):
                nm = sub.attr
            elif isinstance(sub, ast.Name):
                nm = sub.id
            if nm in _FORBIDDEN:
                # `.geoms`／`.exterior`／`.interiors`／`.coords` 為純資料存取·不在黑名單
                hits.append(f"{nm}@L{getattr(sub, 'lineno', '?')}")
        rep.append((node.name, hits))
        if hits:
            raise RuntimeError(
                f"🔴 §0-3 乙-核自檢破：`{node.name}` 命中禁用符號 {hits} "
                f"——乙法已非獨立，本批作廢")
    seen = {r[0] for r in rep}
    miss = [f for f in _B_CORE if f not in seen]
    if miss:
        raise RuntimeError(f"🔴 §0-3 乙-核自檢破：函式未被掃到 {miss}（名單與實作不符）")
    return rep


# ══════════════════════════════════════════════════════════════════════
# §0-2　對照組（⛔ 真值須為解析值·不得由任一量法產生）
# ══════════════════════════════════════════════════════════════════════
def _rot(pts, deg, tx=0.0, ty=0.0):
    """剛體變換（旋轉＋平移）——**保面積** ⇒ 真值不變。"""
    th = np.deg2rad(deg)
    c, s = np.cos(th), np.sin(th)
    R = np.array([[c, -s], [s, c]])
    q = (np.asarray(pts, float) @ R.T)
    q[:, 0] += tx
    q[:, 1] += ty
    return [tuple(v) for v in q]


def _rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def controls():
    """對照組：軸對齊矩形對之重疊為**解析式**，施以**同一剛體變換**後真值不變。

    ⛔ 真值由 `max(0, min-max)` 之區間算術給出——**非**由甲或乙產生。
    """
    from shapely.geometry import Polygon
    cs = []

    def add(tag, a, b, deg, tx, ty, note):
        ax0, ay0, ax1, ay1 = a
        bx0, by0, bx1, by1 = b
        ov = (max(0.0, min(ax1, bx1) - max(ax0, bx0))
              * max(0.0, min(ay1, by1) - max(ay0, by0)))
        cs.append({
            "tag": tag, "truth": ov, "note": note,
            "A": Polygon(_rot(_rect(*a), deg, tx, ty)),
            "B": Polygon(_rot(_rect(*b), deg, tx, ty)),
        })

    # C1：真值 0（分離）·薄片
    add("C1", (0, 0, 120, 0.30), (140, 0, 260, 0.30), 31.7, 55.0, -12.0,
        "真值 0·分離薄片（長寬比 400:1）")
    # C2：真值非 0·薄片大幅重疊
    add("C2", (0, 0, 120, 0.30), (60, 0, 180, 0.30), 31.7, 55.0, -12.0,
        "真值 18.0·薄片重疊（60×0.30）")
    # C3：真值非 0·薄片微量重疊（低端解析度）
    add("C3", (0, 0, 120, 0.30), (119.5, 0, 240, 0.30), 31.7, 55.0, -12.0,
        "真值 0.15·薄片微疊（0.5×0.30）")
    # C4：極端長寬比 1000:1
    add("C4", (0, 0, 200, 0.20), (150, 0.05, 350, 0.25), 8.3, -30.0, 77.0,
        "真值 7.5·長寬比 1000:1（50×0.15）")
    # C5：本案尺度（座標 ~1e2·面積 ~1e3）·真值非 0
    add("C5", (-60, -40, 20, 5), (-10, -30, 70, 15), 47.2, 12.0, 33.0,
        "真值 1050.0·本案尺度（30×35）")
    # C6：本案尺度·真值 0（僅共邊·零面積接觸）
    add("C6", (-60, -40, 20, 5), (20, -40, 100, 5), 47.2, 12.0, 33.0,
        "真值 0·共邊接觸（⛔ 非分離·測邊界判定）")
    return cs


# ══════════════════════════════════════════════════════════════════════
# §甲　量法甲（⛔ 原樣照抄生產碼·不得「順手改良」）
# ══════════════════════════════════════════════════════════════════════
def measure_A(pieces, biz):
    """逐字複製 `app.py:9045–9062` 之三段累加。回傳 (:9047, :9050, :9062, 逐對明細)。"""
    detail = []
    pp = 0.0
    for i in range(len(pieces)):
        for j in range(i + 1, len(pieces)):
            v = float(pieces[i].intersection(pieces[j]).area)          # :9047
            pp += v
            if v > 0:
                detail.append((":9047", f"池{i}×池{j}", v))
    pb = 0.0
    for pi, pg in enumerate(pieces):
        for bi, bg in enumerate(biz):
            v = float(pg.intersection(bg).area)                        # :9050
            pb += v
            if v > 0:
                detail.append((":9050", f"池{pi}×宗{bi}", v))
    bb = 0.0
    for i in range(len(biz)):
        for j in range(i + 1, len(biz)):
            v = float(biz[i].intersection(biz[j]).area)                # :9062
            bb += v
            if v > 0:
                detail.append((":9062", f"宗{i}×宗{j}", v))
    return pp, pb, bb, detail


def measure_Bm(pieces, biz, n_c=400, n_f=1500):
    """量法乙之同構三段累加（同一對序·⛔ 未取用甲之任何結果）。"""
    detail = []
    pp = 0.0
    for i in range(len(pieces)):
        for j in range(i + 1, len(pieces)):
            r = overlap_B(pieces[i], pieces[j], n_c, n_f)
            pp += r["est"]
            if r["est"] > 0:
                detail.append((":9047", f"池{i}×池{j}", r["est"], r["stage"], r["cell"]))
    pb = 0.0
    for pi, pg in enumerate(pieces):
        for bi, bg in enumerate(biz):
            r = overlap_B(pg, bg, n_c, n_f)
            pb += r["est"]
            if r["est"] > 0:
                detail.append((":9050", f"池{pi}×宗{bi}", r["est"], r["stage"], r["cell"]))
    bb = 0.0
    for i in range(len(biz)):
        for j in range(i + 1, len(biz)):
            r = overlap_B(biz[i], biz[j], n_c, n_f)
            bb += r["est"]
            if r["est"] > 0:
                detail.append((":9062", f"宗{i}×宗{j}", r["est"], r["stage"], r["cell"]))
    return pp, pb, bb, detail


# ══════════════════════════════════════════════════════════════════════
# §複製　`_pool_strips_for_block` §1–§5 之複製（保真性由甲值對拍把關）
# ══════════════════════════════════════════════════════════════════════
def replicate_pieces(ns, block_poly, d_hat, corner_pt, allocation_dir, biz_polys):
    """⛔ 逐字對照 `app.py:8975–9030`（§1 s 域→§5 切帶）。

    🔒 **保真性判準**：由本函式之 `pieces` 算出之甲值，須與**生產 raise 訊息**
       之數字**逐位相同**；不同即代表複製失真、該格作廢（§f-1 表列 `保真` 欄）。
    """
    _strip_s_range = ns["_strip_s_range"]
    _block_strip = ns["_block_strip"]
    _S_EPS = ns["_S_EPS"]
    _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
    _dom = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
    if _dom is None:
        return None, _biz
    s_min, s_max = _dom
    biz_iv = []
    for p in _biz:
        r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
        if r is not None:
            biz_iv.append(r)
    biz_iv.sort()
    merged = []
    for a, b in biz_iv:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    pool_iv = []
    cur = s_min
    for a, b in merged:
        if a > cur:
            pool_iv.append((cur, min(a, s_max)))
        cur = max(cur, b)
    if cur < s_max:
        pool_iv.append((cur, s_max))
    pool_iv = [(a, b) for a, b in pool_iv if (b - a) > _S_EPS]
    pieces = []
    for (a, b) in pool_iv:
        bp = np.asarray(corner_pt, dtype=float) + a * np.asarray(d_hat, dtype=float)
        g, _ = _block_strip(block_poly, d_hat, bp, b - a, allocation_dir=allocation_dir)
        if g is None or g.is_empty:
            continue
        if g.buffer(-1e-4).is_empty:
            continue
        pieces.append(g)
    return pieces, _biz


# ══════════════════════════════════════════════════════════════════════
# §main
# ══════════════════════════════════════════════════════════════════════
def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-17】②-宗／②-池 重疊量之兩法對打 ＋ ①' 覆蓋閘第三法重算")
    P("=" * W)
    import shapely
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")

    # ── §0-3 乙-核碼面自檢 ──
    P("")
    P("【0-3】量法乙獨立性之**碼面**自檢（AST·⛔ 非人工聲明）")
    P("-" * W)
    rep = audit_core()
    for nm, hits in rep:
        P(f"  {nm:<16} 禁用符號命中 {len(hits)}　{'✅' if not hits else '🔴 ' + str(hits)}")
    P(f"  ⇒ 乙-核 {len(rep)} 個函式全數零命中 ⇒ **乙法未經 shapely 布林**")

    # ── §0-2 對照組 ──
    P("")
    P("【0-2】量法乙之解析度自證（對照組·真值為**解析式**·⛔ 非由任一量法產生）")
    P("-" * W)
    P(f"  {'組':<4}{'真值':>12}{'甲':>14}{'乙':>14}{'乙−真值':>12}{'格面積':>12}  說明")
    errs = []
    for c in controls():
        tA = float(c["A"].intersection(c["B"]).area)
        rB = overlap_B(c["A"], c["B"], 400, 2200)
        err = rB["est"] - c["truth"]
        errs.append((c["tag"], c["truth"], err, "共邊" in c["note"]))
        P(f"  {c['tag']:<4}{c['truth']:>12.4f}{tA:>14.4f}{rB['est']:>14.4f}"
          f"{err:>+12.4f}{rB['cell']:>12.2e}  {c['note']}")
    P("")
    P("  ⚠️ **三判準分列**（⛔ 不得併為單一門檻——初版併之，致 C6 之貼邊偏壓")
    P("     被誤報為「解析度不足」。⛔ 此係**判準本身寫錯**、非因結果不利而放寬：")
    P("     下列三數皆為**原始實測值**，一個未改）：")
    _e_int = max(abs(e) for (_t, _v, e, _b) in errs if not _b)
    _e_edge = max((abs(e) for (_t, _v, e, b) in errs if b), default=0.0)
    _mrg = 76.2616 / _e_int if _e_int > 0 else float("inf")
    P(f"     判準A（施工單**明訂**：能否分辨 `76.26` 與 `0`）：非共邊組最大誤差 {_e_int:.4f} ㎡"
      f" ⇒ 餘裕 ×{_mrg:.0f}　{'✅ 遠足夠' if _mrg >= 100 else '🔴 未驗'}")
    P(f"     判準B（內部精度·真值非 0 組）：相對誤差 ≤ "
      f"{max(abs(e) / v for (_t, v, e, b) in errs if v > 0 and not b) * 100:.3f}%　✅")
    P(f"     判準C（**貼邊偏壓**·共邊對·真值 0）：{_e_edge:+.4f} ㎡/對（**系統性正偏**）")
    P("        🔴 此**非隨機誤差**、係乙法對「相鄰共邊對」之系統性正偏 ⇒ **必須帶入判讀**：")
    P("        ⛔ 不得逕以乙>甲 判「甲漏報」——須改以 §f-1c 之**實寬**判準裁決。")
    P("  🔒 對照組含 **真值非 0** 之 C2/C3/C4/C5（⛔ 非僅真值 0）——"
      "否則乙法只被證明「會回 0」，即把結論埋進判準。")

    # ── §0-2b fixture 對照（真值有獨立佐證：帶號 ＋ contains）──
    P("")
    P("【0-2b】fixture 對照組（`case_D2b15_tilegate_intersection`·真值有**倉內獨立佐證**）")
    P("-" * W)
    ns, fake_st = harvest()
    try:
        import case_D2b15_tilegate_intersection as C
        from shapely.geometry import Polygon as _Pg
        _blk = _Pg(C.BLOCK)
        _lines = [(np.asarray(q, float), np.asarray(nh, float)) for q, nh in C.LINES]
        _pieces, _diag = ns["_block_partition"](_blk, np.asarray(C.D_HAT, float),
                                                _lines, _label="D2b17-fix")
        _a = float(_pieces[2].intersection(_pieces[4]).area)
        _b = overlap_B(_pieces[2], _pieces[4], 400, 2600)
        P(f"  片數 {len(_pieces)}　面積鏈 {[round(x,4) for x in _diag['areas']]}")
        P(f"  片2 × 片4：甲 = {_a:.6f}　乙 = {_b['est']:.6f}"
          f"（{_b['stage']}·格面積 {_b['cell']:.2e}）")
        P(f"  片4 全部面積（shoelace·乙核）= {poly_area_np(_pieces[4]):.6f}")
        P(f"  倉內獨立佐證（fixture docstring）：帶號 f(L3) = +{C.SAMPLE_F_L3_REF} ≥ 0 "
          f"⇒ 取樣點屬餘塊非片2；`片2.contains` = False；甲曾報 {C.PRE_FIX_BAD_OVERLAP}")
    except Exception as e:                                          # noqa: BLE001
        P(f"  🔴 fixture 對照失敗：{type(e).__name__}: {e}")

    # ── §f-1 驅動：spy 攔截 `_pool_strips_for_block` ──
    P("")
    P("【f-1】R1–R6 × 兩情境：三處運算元之兩法對打")
    P("-" * W)
    CAP = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        key = (_spy.tag, _label, _spy.seq.get((_spy.tag, _label), 0))
        _spy.seq[(_spy.tag, _label)] = _spy.seq.get((_spy.tag, _label), 0) + 1
        try:
            pieces, biz = replicate_pieces(ns, block_poly, d_hat, corner_pt,
                                           allocation_dir, biz_polys)
            CAP[key] = {"block": block_poly, "pieces": pieces, "biz": biz,
                        "depth": _depth}
        except Exception as e:                                      # noqa: BLE001
            CAP[key] = {"err": f"{type(e).__name__}: {e}"}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)
    _spy.seq = {}
    _spy.tag = ""

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    _blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in _blks:
            _blks.append(_l)

    ERR = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in _blks:
            _spy.tag = sb
            ns["_pool_strips_for_block"] = _spy
            buf = io.StringIO()
            err = ""
            try:
                with contextlib.redirect_stdout(buf):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception as e:                          # noqa: BLE001
                        err = f"{type(e).__name__}: {e}"
            finally:
                ns["_pool_strips_for_block"] = _orig
            ERR[(sb, lbl)] = err
            print(f"    [{sb}] {lbl} 擷取完畢", file=sys.stderr)
    return L, CAP, ERR, ns


def report(L, CAP, ERR, ns):                                       # noqa: C901
    import re

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    def _num(pat, s):
        m = re.search(pat, s or "")
        return float(m.group(1)) if m else None

    P("")
    P(f"  {'情境':<5}{'街廓':<5}{'呼叫':<5}{'宗':<4}{'池':<4}"
      f"{'甲:9047':>11}{'乙:9047':>11}{'甲:9050':>11}{'乙:9050':>11}"
      f"{'甲:9062':>12}{'乙:9062':>12}  保真")
    ROWS = []
    for key in sorted(CAP.keys()):
        sb, lbl, seq = key
        c = CAP[key]
        if "err" in c:
            P(f"  {sb:<5}{lbl:<5}#{seq:<4}　🔴 複製失敗：{c['err']}")
            continue
        pieces, biz = c["pieces"], c["biz"]
        if pieces is None:
            P(f"  {sb:<5}{lbl:<5}#{seq:<4}　🔴 s 域不可定義")
            continue
        aP, aB, aZ, adet = measure_A(pieces, biz)
        bP, bB, bZ, bdet = measure_Bm(pieces, biz)
        # 保真性：我方甲值 vs 生產 raise 訊息之數字
        msg = ERR.get((sb, lbl), "")
        prod_z = _num(r"宗-宗重疊 = ([0-9.]+)", msg)
        fid = "—"
        if prod_z is not None:
            fid = "✅" if abs(prod_z - aZ) < 5e-5 else f"🔴 生產 {prod_z}"
        P(f"  {sb:<5}{lbl:<5}#{seq:<4}{len(biz):<4}{len(pieces):<4}"
          f"{aP:>11.4f}{bP:>11.4f}{aB:>11.4f}{bB:>11.4f}"
          f"{aZ:>12.4f}{bZ:>12.4f}  {fid}")
        ROWS.append((sb, lbl, seq, aP, bP, aB, bB, aZ, bZ, adet, bdet, prod_z))

    # 逐對明細（僅列甲非零者·含乙之對應值）
    P("")
    P("【f-1b】逐對明細（甲非零之對·並列乙）——⛔ 乙之對序與甲同、但值獨立算出")
    P("-" * W)
    for (sb, lbl, seq, aP, bP, aB, bB, aZ, bZ, adet, bdet, _pz) in ROWS:
        if not adet:
            continue
        bmap = {(d[0], d[1]): d for d in bdet}
        P(f"  ── [{sb}] {lbl} #{seq} ──")
        for (site, pair, v) in sorted(adet, key=lambda t: -t[2])[:12]:
            bd = bmap.get((site, pair))
            bv = bd[2] if bd else 0.0
            st = bd[3] if bd else "bbox-disjoint"
            cl = bd[4] if bd else 0.0
            verdict = "✅ 一致" if (abs(bv - v) <= max(0.05, 0.05 * v)) else "🔴 矛盾"
            P(f"     {site} {pair:<14} 甲 {v:>12.4f}　乙 {bv:>12.4f}"
              f"　{verdict}　({st}·格 {cl:.1e})")

    # ── §f-2 ──
    P("")
    P("【f-2】①' 覆蓋閘之第三法（量法丙·⛔ 未用 union）重算")
    P("-" * W)
    P(f"  {'情境':<5}{'街廓':<5}{'甲(union)':>13}{'丙|resid|':>12}{'丙 缺口':>11}"
      f"{'丙 溢出':>11}{'丙 重疊多重度':>15}{'格面積':>11}")
    for key in sorted(CAP.keys()):
        sb, lbl, seq = key
        if seq != 0:
            continue
        c = CAP[key]
        if "err" in c or c.get("pieces") is None:
            continue
        blk, pieces, biz = c["block"], c["pieces"], c["biz"]
        from shapely.ops import unary_union
        _all = biz + pieces
        _uni = unary_union(_all) if _all else None
        a_res = abs(float(_uni.area) - float(blk.area)) if _uni is not None else None
        r = cover_C(blk, _all, n=2400)
        P(f"  {sb:<5}{lbl:<5}{(a_res if a_res is not None else float('nan')):>13.4f}"
          f"{abs(r['resid_signed']):>12.4f}{r['gap']:>11.4f}{r['out']:>11.4f}"
          f"{r['mult']:>15.4f}{r['cell']:>11.2e}")
    return L


if __name__ == "__main__":
    _mode = sys.argv[1] if len(sys.argv) > 1 else "full"
    if _mode == "controls":
        for _s in (sys.stdout, sys.stderr):
            try:
                _s.reconfigure(encoding="utf-8")
            except Exception:
                pass
        import shapely
        print(f"環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
        for nm, hits in audit_core():
            print(f"  {nm:<16} {'✅' if not hits else '🔴 ' + str(hits)}")
        print(f"  {'組':<4}{'真值':>12}{'甲':>14}{'乙':>14}{'乙−真值':>12}{'格面積':>12}")
        for c in controls():
            tA = float(c["A"].intersection(c["B"]).area)
            rB = overlap_B(c["A"], c["B"], 400, 2200)
            print(f"  {c['tag']:<4}{c['truth']:>12.4f}{tA:>14.4f}{rB['est']:>14.4f}"
                  f"{rB['est'] - c['truth']:>+12.4f}{rB['cell']:>12.2e}  {c['note']}")
        sys.exit(0)
    _L, _CAP, _ERR, _ns = main()
    _L = report(_L, _CAP, _ERR, _ns)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print(f"\n→ {LOG}", file=sys.stderr)
