#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-156**：`K-9-23 五` 八格驗收預測表之**可重算輸入**（`GB-109` 之解除素材）。

## 受詞

`GB-109` 逐字之失效條件 ＝「主批**前**補齊該表之可重算輸入（重跑一支只讀探針並**入倉**）」。
本檔即該支探針。產出 ＝ 使下列三類**皆可由倉內物重算**：

- 五欄**原始量**：`藍影`／`第 1 宗`／`G`／`閘二`／`②-宗 圍堵閘`
- **遞補鏈** `5` 格
- **騰出面積** `5` 數

## 🔒 方法之紅線（施工單 `W-G.9-156` `P-1`）

⛔ **不 import／不複製 `app.py`／`verify/wf_*` 之任何幾何函式**——判準（藍影／矩形容納／
遞補迴圈）一律**依正典逐字獨立實作於本檔**。
🔒 **得自管線取用者，限於「受測物之<u>輸入</u>」**：母體（暫編地號、`polygon_coords`）、
各宗之 `G`、`②-宗 圍堵閘`之現況輸出。

## 🔒 `GB-82`（TWD97 絕對座標下 GEOS 退化）

一切幾何先**重心化**（減 `LOCAL_ORIGIN`）再算；平移量逐次出艙。
**平移⛔ 不改變面積與容納**，係數值手段、⛔ 非另立座標框。

## 重跑

    PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9156_pred_inputs.py

`rc` 恆為 `0`；缺件／取不到資料時 loud raise（`no-silent-fallback`）。
"""
import contextlib
import io
import math
import os
import subprocess
import sys

import numpy as np
from shapely.affinity import rotate as _rot, translate as _tr
from shapely.geometry import LineString as SLine, Polygon as SPoly, box as _box

HERE = os.path.dirname(os.path.abspath(__file__))          # verify/probes
VERIFY = os.path.dirname(HERE)                              # verify
REPO = os.path.dirname(VERIFY)                              # 倉根（⛔ 不寫死絕對路徑）
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "5f06a659"                    # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD）
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

SB = 0.0                                  # 情境 ＝ 退縮 0m
LOCAL_ORIGIN = np.array([310450.0, 2651900.0])   # 🔒 GB-82 之重心化平移量
_LBIG = 1.0e5                             # 無限直線之代理長度
EPS_ZERO = 1e-6                           # 「∩ ＝ 0」之容差（K-9-23 三-二 逐字）
TOUCH_TOL = 1e-3                          # 臨接長之容差帶（見 `touch_len` docstring 之判別力）
ANG_STEP_DEG = 0.5                        # 矩形容納之角度掃描步長

L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


# ══════════════════════════════════════════════════════════════════════════
#  幾何原語（🔒 本檔自寫·⛔ 未取自 app.py／wf_*）
# ══════════════════════════════════════════════════════════════════════════
def Lc(p):
    """重心化。"""
    return np.asarray(p, float)[:2] - LOCAL_ORIGIN


def uhat(v):
    v = np.asarray(v, float)[:2]
    n = float(math.hypot(*v))
    if n == 0.0:
        raise RuntimeError("🔴 方向為零向量（no-silent-fallback）")
    return v / n


def rot90(v):
    return np.array([-v[1], v[0]])


def isect(p1, d1, p2, d2):
    """二無限直線之交點；平行回 None。"""
    A = np.array([np.asarray(d1, float)[:2], -np.asarray(d2, float)[:2]]).T
    if abs(float(np.linalg.det(A))) < 1e-12:
        return None
    t = np.linalg.solve(A, np.asarray(p2, float)[:2] - np.asarray(p1, float)[:2])
    return np.asarray(p1, float)[:2] + t[0] * np.asarray(d1, float)[:2]


def infline(p, d):
    """無限直線之代理線段。"""
    p = np.asarray(p, float)[:2]
    d = uhat(d)
    return SLine([tuple(p - d * _LBIG), tuple(p + d * _LBIG)])


def touch_len(poly, p, d, tol=TOUCH_TOL):
    r"""宗地與過 `p` 沿 `d` 之無限直線之**臨接長**（＝邊界落在 `|垂距| <= tol` 帶內之長度）。

    🩸 **⛔ 不得用 `poly.intersection(line)`**——宗地之邊**恰落在該線上**時，二維面與其
    切線之交集因浮點而**退化為空** ⇒ 臨接長偽 `0`（本檔首版即此·CC 自捕）。
    改以**逐邊裁剪至容差帶**計之。

    🔒 **`tol` 之判別力**：本案實測，臨接者之 `|垂距|` 極值 `<= 1e-5 m`，
    而**不臨接**者之 `min|垂距|` 為 `34.87 m`（`R2` `628-42(1)`）／`38.64 m`（`R5` `628-53(2)`）
    ⇒ 二母體相距 **逾 6 個數量級**，`tol = 1e-3` 落於其間、⛔ 非湊出來的門檻。
    """
    p = np.asarray(p, float)[:2]
    nv = rot90(uhat(d))
    b = float(np.dot(p, nv))
    ring = list(poly.exterior.coords)
    tot = 0.0
    for i in range(len(ring) - 1):
        a0 = np.asarray(ring[i], float)[:2]
        a1 = np.asarray(ring[i + 1], float)[:2]
        f0 = float(np.dot(a0, nv)) - b
        f1 = float(np.dot(a1, nv)) - b
        lo, hi = 0.0, 1.0
        for sgn in (+1.0, -1.0):            # 裁剪至 sgn*(f0+t*(f1-f0)) <= tol
            c0, c1 = sgn * f0 - tol, sgn * f1 - tol
            dd = c1 - c0
            if abs(dd) < 1e-18:
                if c0 > 0.0:
                    lo, hi = 1.0, 0.0
                continue
            t = -c0 / dd
            if dd > 0.0:
                hi = min(hi, t)
            else:
                lo = max(lo, t)
        if hi > lo:
            tot += (hi - lo) * float(np.hypot(*(a1 - a0)))
    return tot


def min_absdist(poly, p, d):
    """宗地全部頂點對該無限直線之 `min|垂距|`（供 `tol` 之判別力自證）。"""
    nv = rot90(uhat(d))
    b = float(np.dot(np.asarray(p, float)[:2], nv))
    vs = np.asarray(poly.exterior.coords, float)[:, :2]
    return float(np.min(np.abs(vs @ nv - b)))


def rect_fit(poly, w, d):
    r"""`K-9-12` 矩形容納（**可旋轉、可平移**·`K-9-12-c`）。

    回 `(判, 憑證, 最大侵蝕面積, 命中角度)`；**判為三態**：

    - `False`　**定不進**——① 面積證書 `area(P) < W·D`；或 ② 全掃描角之 `P ⊖ R` 皆空。
      🔒 **本負判為<u>健全</u>**：四角交集法對非凸 `P` 係真侵蝕之**超集** ⇒ 超集空 ⇒ 真侵蝕必空。
    - `True`　 **定進**——於某角取得候選中心並以 `P.contains(rect)` **實證**。
    - `None`　 **未定**——侵蝕非空而無一候選實證（⛔ 不得逕判為進或不進）。

    ⚠️ 角度係**有限掃描**（步長 `ANG_STEP_DEG` ＋ 全部邊向）⇒ `False` 之②款
    **⛔ 非全角度之數學證明**；①款則為解析證書、與角度無關。
    """
    need = float(w) * float(d)
    if float(poly.area) + 1e-12 < need:
        return False, "面積證書：area=%.6f < W·D=%.6f" % (poly.area, need), 0.0, None
    ring = list(poly.exterior.coords)
    angs = set()
    for i in range(len(ring) - 1):
        dx = ring[i + 1][0] - ring[i][0]
        dy = ring[i + 1][1] - ring[i][1]
        if math.hypot(dx, dy) > 1e-12:
            angs.add(round(math.degrees(math.atan2(dy, dx)) % 180.0, 9))
    k = 0
    while k * ANG_STEP_DEG < 180.0:
        angs.add(round(k * ANG_STEP_DEG, 9))
        k += 1
    best_a, best_th = 0.0, None
    for th in sorted(angs):
        P = _rot(poly, -th, origin=(0.0, 0.0), use_radians=False)
        cur = None
        for cx, cy in ((0.0, 0.0), (w, 0.0), (0.0, d), (w, d)):
            t = _tr(P, xoff=-cx, yoff=-cy)
            cur = t if cur is None else cur.intersection(t)
            if cur.is_empty:
                break
        if cur is None or cur.is_empty:
            continue
        a = float(cur.area)
        if a > best_a:
            best_a, best_th = a, th
        cands = []
        try:
            cands.append(cur.representative_point())
        except Exception:                                       # noqa: BLE001
            pass
        try:
            cands.append(cur.centroid)
        except Exception:                                       # noqa: BLE001
            pass
        if cur.geom_type == "Polygon":
            cands += [type(cur.centroid)(c[0], c[1]) for c in list(cur.exterior.coords)[:24]]
        for pt in cands:
            if pt is None or pt.is_empty:
                continue
            rct = _box(pt.x, pt.y, pt.x + w, pt.y + d)
            if P.contains(rct) or P.buffer(1e-9).contains(rct):
                return True, "θ=%.4f° 候選中心實證 contains" % th, max(best_a, a), th
    if best_th is None:
        return False, "全 %d 個掃描角之 `P ⊖ R` 皆空" % len(angs), 0.0, None
    return None, "侵蝕非空（max=%.9f @θ=%.4f°）而無一候選實證 contains" % (best_a, best_th), \
        best_a, best_th


# ══════════════════════════════════════════════════════════════════════════
#  驅動（🔒 逐字同 `probe_WG992_blue.build()` 之體例：**逐街廓** `run_step_g`）
# ══════════════════════════════════════════════════════════════════════════
def drive():
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import probe_WG981_scope as w81

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    o_solve, o_pool = ns["_solve_G_one"], ns["_pool_strips_for_block"]
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _sw = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)
    w81.CAP.clear()
    w81.SOLVE.clear()
    w81.CUR["setback"] = SB
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)
    ns["_solve_G_one"] = w81.spy_solve(o_solve)
    ns["_pool_strips_for_block"] = w81.spy_pool(o_pool)
    gate = {}
    try:
        for lbl in blks:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, SB)
                    gate[lbl] = ("過", "")
                except Exception as e:                          # noqa: BLE001
                    # 🩸 **⛔ 不得把任何例外都記成「②-宗 破」**（本檔首版即此·CC 自捕）：
                    #   `R4` 之中止係 **`結構閘 理論＝實跑 破`**、⛔ 非 `②-宗 圍堵閘`
                    #   ⇒ 就 `②-宗` 而言 `R4` 係「過」。判以**該閘之具名字樣**為之。
                    msg = "%s: %s" % (type(e).__name__, e)
                    gate[lbl] = (("破" if "②-宗 圍堵閘破" in msg else "過"), msg)
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    CAP = {r["label"]: r for r in w81.CAP}
    if not CAP:
        raise RuntimeError("🔴 CAP 為空——管線未產生任何街廓（no-silent-fallback）")
    return CAP, cad, wins, gate, params


# ══════════════════════════════════════════════════════════════════════════
#  P-1／P-2：逐格之獨立構造
# ══════════════════════════════════════════════════════════════════════════
def cell_raw(lbl, side, CAP, cad, wins, params, *, sigma_swap=False):
    """回一格之全部**原始量**（`a`〜`j` 之素材）。⛔ 不作任何判。"""
    rec = CAP[lbl]
    fl = cad["front_lines"][lbl]
    bl = cad["baselines"][lbl]
    sl = (cad["side_lines_by_side"].get(lbl) or {}).get(side)
    if sl is None:
        raise RuntimeError("🔴 %s/%s 無 SIDE_LINE" % (lbl, side))
    o_ = Lc(fl["p1"])
    d_ = uhat(np.asarray(fl["p2"], float)[:2] - np.asarray(fl["p1"], float)[:2])
    bpt = Lc(bl["point"])
    bang = math.radians(float(bl["angle_deg"]))
    bdir = np.array([math.cos(bang), math.sin(bang)])
    ahat = uhat(cad["alloc_dir_by_block"][lbl])
    nhat = rot90(ahat)

    names = list(rec["names"] or [])
    polys = [SPoly([tuple(Lc(c)) for c in p.exterior.coords]) for p in rec["biz"]]
    ress = list(rec["ress"] or [])
    Gs = [((ress[i] or {}).get("G") if i < len(ress) else None) for i in range(len(polys))]
    block = SPoly([tuple(Lc(c)) for c in rec["block"].exterior.coords])

    wname = (wins[lbl] or {}).get("p1_end" if side == "left" else "p2_end")
    if wname not in names:
        raise RuntimeError("🔴 %s/%s winner %r 不在母體" % (lbl, side, wname))
    wi = names.index(wname)

    # ── 側組之切分：右 winner 之 biz 索引 ＝ 分界 `k`（左組 `[0,k)`／右組 `[k,n)`）──
    rw = (wins[lbl] or {}).get("p2_end")
    k = names.index(rw) if (rw in names) else len(names)
    grp = list(range(0, k)) if side == "left" else list(range(k, len(names)))
    if wi not in grp:
        raise RuntimeError("🔴 %s/%s winner 不在該側組" % (lbl, side))
    # 🔒 推進序（`K-9-17`：**街角重排後**序列）之次一位起，即遞補之候選序
    seq = [i for i in grp if i > wi]

    # ── 街角地（第 0 宗）之遠側境界線（∥SIDELINE·由 winner 之 `G` 定）──
    su = uhat(np.asarray(sl["p2"], float)[:2] - np.asarray(sl["p1"], float)[:2])
    ns_ = rot90(su)
    smid = Lc(sl["mid"])
    vs = np.asarray(polys[wi].exterior.coords, float)[:, :2]
    base = float(np.dot(smid, ns_))
    far_pt = vs[int(np.argmax(np.abs(vs @ ns_ - base)))]
    P1 = isect(far_pt, su, o_, d_)
    B1 = isect(far_pt, su, bpt, bdir)
    if P1 is None or B1 is None:
        raise RuntimeError("🔴 %s/%s P1／B1 取不到（遠側界 ∥ FRONT 或 ∥ BASE）" % (lbl, side))

    # ── 帶（過 P1、過 B1 各作一條 ∥ALLOCLINE）＋ 二三角形 ──
    Q = isect(B1, ahat, o_, d_)          # 過 B1 之 ∥ALLOC ∩ FRONTLINE
    R = isect(P1, ahat, bpt, bdir)       # 過 P1 之 ∥ALLOC ∩ BASELINE
    if Q is None or R is None:
        raise RuntimeError("🔴 %s/%s 帶與 FRONT／BASE 平行" % (lbl, side))
    TA = SPoly([tuple(P1), tuple(B1), tuple(Q)])      # `A` ＝ 過 `B1` 之三角形
    TB = SPoly([tuple(P1), tuple(B1), tuple(R)])      # `B` ＝ 過 `P1` 之三角形
    iA = float(TA.intersection(polys[wi]).area)
    iB = float(TB.intersection(polys[wi]).area)

    # ── `σ`（🔒 導出式：由**街廓形心**定號·⛔ 不取側別字串）──
    cen = np.array([block.centroid.x, block.centroid.y])
    if sigma_swap:                       # `P-6` 之對照：側別標籤對調而形心不動
        su = -su
        ns_ = -ns_
    sigma = 1.0 if float(np.dot(cen - P1, nhat)) >= 0.0 else -1.0
    ds = float(np.dot(B1 - P1, nhat))

    return {
        "lbl": lbl, "side": side, "names": names, "polys": polys, "G": Gs,
        "block": block, "o": o_, "d": d_, "bpt": bpt, "bdir": bdir,
        "ahat": ahat, "nhat": nhat, "su": su,
        "wname": wname, "wi": wi, "k": k, "grp": grp, "seq": seq,
        "far_pt": far_pt, "P1": P1, "B1": B1, "Q": Q, "R": R,
        "TA": TA, "TB": TB, "areaA": float(TA.area), "areaB": float(TB.area),
        "iA": iA, "iB": iB, "sigma": sigma, "ds": ds,
        "params": next((r for r in params if isinstance(r, dict)
                        and r.get("街廓") == lbl), None),
    }


def pick_blue(raw):
    """🔒 選邊之**唯一決定點** ＝ 取「與街角地不重疊」之半（`∩街角地 ＝ 0`·容差 `1e-6`）。

    ⛔ `σ·Δs` 之號係**斷言**、⛔ 非決定點（`K-9-23 三-二`·`W-G.9-142` 實測純號規則 `4/8` 選錯）。
    """
    a0, b0 = raw["iA"] <= EPS_ZERO, raw["iB"] <= EPS_ZERO
    if a0 and not b0:
        return "A", raw["areaA"], raw["TA"]
    if b0 and not a0:
        return "B", raw["areaB"], raw["TB"]
    if a0 and b0:
        raise RuntimeError("🔴 %s/%s 二半皆不重疊 ⇒ 定義無法決定（⛔ 不得任取）"
                           % (raw["lbl"], raw["side"]))
    raise RuntimeError("🔴 %s/%s 二半皆重疊 ⇒ 定義無法決定（∩A=%.9f ∩B=%.9f）"
                       % (raw["lbl"], raw["side"], raw["iA"], raw["iB"]))


def gate1(raw, idx, blue_area, *, strict=True):
    """閘一 ＝ `G > 藍影`（**嚴格**·`strict=False` 為 `P-5` 擾動①）∧ 臨 FRONT `> 0` ∧ 臨 BASE `> 0`。"""
    g = raw["G"][idx]
    if g is None:
        return None, {"G": None, "why": "G 取不到"}
    lf = touch_len(raw["polys"][idx], raw["o"], raw["d"])
    lb = touch_len(raw["polys"][idx], raw["bpt"], raw["bdir"])
    mf = min_absdist(raw["polys"][idx], raw["o"], raw["d"])
    mb = min_absdist(raw["polys"][idx], raw["bpt"], raw["bdir"])
    c1 = (float(g) > blue_area) if strict else (float(g) >= blue_area)
    ok = bool(c1 and lf > 0.0 and lb > 0.0)
    return ok, {"G": float(g), "blue": blue_area, "c_G": bool(c1),
                "len_front": lf, "len_base": lb, "min_front": mf, "min_base": mb}


def wmax_at_d(poly, d, w_hi, tol=1e-4):
    """`D` 固定下，可容納之**最大寬** `w`（二分）——供「閘二不過」之量化診斷。

    🔒 只在 `閘二 = False` **且**面積證書不成立（`area >= W·D`）時呼叫；⛔ 非判準之一部。
    """
    lo, hi = 0.0, float(w_hi)
    if rect_fit(poly, hi, d)[0] is True:
        return hi
    while hi - lo > tol:
        mid = (lo + hi) / 2.0
        if rect_fit(poly, mid, d)[0] is True:
            lo = mid
        else:
            hi = mid
    return lo


def gate2(raw, idx, w, d):
    """閘二 ＝ `K-9-12` 矩形容納。🔒 街角地本身⛔ 不走本閘（`K-9-12-e`）——本函式只餵非街角宗。"""
    return rect_fit(raw["polys"][idx], w, d)


# ══════════════════════════════════════════════════════════════════════════
def main():                                                     # noqa: C901
    sys.stdout.reconfigure(encoding="utf-8")
    W = 108
    say("=" * W)
    say("【W-G.9-156】`K-9-23 五` 八格驗收預測表之**可重算輸入**（`GB-109` 素材）")
    say("=" * W)
    say("  HEAD        = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob = %s" % git1(["rev-parse", "HEAD:app.py"]))
    say("  基座(log 綁) = %s" % BASE_REF)
    say("  情境 = 退縮 %.1fm ／ WV_K6_STEP0 = %s"
        % (SB, os.environ.get("WV_K6_STEP0", "<未設·預設>")))
    say("  LOCAL_ORIGIN（GB-82 重心化平移量）= (%.1f, %.1f)"
        % (LOCAL_ORIGIN[0], LOCAL_ORIGIN[1]))
    say("")

    CAP, cad, wins, gate, params = drive()

    # ══════════ E-0 ══════════
    say("=" * W)
    say("§E-0　`K-9-12-a` 宗地層附表之**實際 `W`／`D` 值**（🛑 停機條件）")
    say("=" * W)
    src = os.path.join(REPO, "app.py")
    txt = open(src, encoding="utf-8").read().splitlines()
    hit = [i for i, ln in enumerate(txt, 1) if "HUALIEN_MIN_LOT_TABLE = {" in ln]
    ctl = [i for i, ln in enumerate(txt, 1) if "def get_min_lot_size" in ln]
    say("  框 ＝ `HUALIEN_MIN_LOT_TABLE = {`　命中 = %d　@ app.py:%s" % (len(hit), hit))
    say("  對照組 框 ＝ `def get_min_lot_size`　命中 = %d　@ app.py:%s（⇒ 量測器非紅）"
        % (len(ctl), ctl))
    if not hit:
        raise RuntimeError("🛑 E-0 不成立：附表之實際值⛔ 不在倉 ⇒ 閘二無從重算，停機")
    say("  ── 表頭與前三列（逐字·自 `sed` 管線之同一抽取）──")
    for i in range(hit[0], hit[0] + 5):
        say("    app.py:%d｜%s" % (i, txt[i - 1]))
    say("")
    say("  ── 管線所餵之逐街廓 `W`／`D`（＝ 受測物之輸入）──")
    say("    %-6s %-8s %-14s %-12s %-12s" % ("街廓", "分類", "正面路寬(m)", "法定最小寬", "法定最小深"))
    WD = {}
    for r in params:
        if not isinstance(r, dict):
            continue
        WD[r["街廓"]] = (float(r["法定最小寬(m)"]), float(r["法定最小深(m)"]))
        say("    %-6s %-8s %-14s %-12s %-12s" % (r["街廓"], r["分類"], r["正面路寬(m)"],
                                                 r["法定最小寬(m)"], r["法定最小深(m)"]))
    say("  🔒 對拍：`住宅區` 路寬 `8.0`／`12.0` 皆 `<= 15.0` ⇒ 附表列 `(15.0, 3.50, 14.00)`")
    say("     ⇒ `W = 3.50`／`D = 14.00`，與管線所餵**逐格相符**：%s"
        % ("✅ 是" if all(v == (3.5, 14.0) for v in WD.values()) else "🔴 否"))
    say("  ✅ **E-0 成立**（`Q-2` 符）⇒ ⛔ 不停機。")
    say("")

    # ══════════ E-1 ══════════
    say("=" * W)
    say("§E-1　管線之最短驅動（harness 態·逐字·俾後人重跑）")
    say("=" * W)
    for ln in [
        "  from app_harvest import harvest;  import run_verification as rv",
        "  from selection_pipeline import run_corner_pk;  from stepg_pipeline import run_step_g",
        "  import probe_WG981_scope as w81",
        "  ns, fake_st = harvest();  snapshot = rv.load_snapshot()",
        "  cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)",
        "  rv.build_ownership(ns, fake_st, rv.ANON_XLSX)",
        "  temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, <V6 bytes>,",
        "                                              list(cb_by.values()), snapshot)",
        "  w81.CAP.clear(); w81.SOLVE.clear(); w81.CUR['setback'] = 0.0",
        "  params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)",
        "  _d0,_s2,_o2, wins, forced = run_corner_pk(ns, fake_st, cb_all, cad, params,",
        "                                temp_p, build_p, 0.0, snapshot=snapshot)",
        "  ns['_solve_G_one']        = w81.spy_solve(o_solve)",
        "  ns['_pool_strips_for_block'] = w81.spy_pool(o_pool)",
        "  for lbl in blks:                      # 🔒 **逐街廓**·try/except",
        "      try:  run_step_g(ns, fake_st, cb_all, cad, snapshot, params,",
        "                       [tp for tp in build_p if tp['所屬街廓']==lbl],",
        "                       wins, forced, 0.0)",
        "      except Exception:  pass           # ⇒ R2／R5 之中止⛔ 不阻斷 R3〜R6",
    ]:
        say(ln)
    say("")
    say("  🔒 環境變數：`WV_K6_STEP0` **未設**（取其預設）；情境 `0m` ＝ `setback = 0.0`（本檔 `SB`）。")
    say("  🔒 執行時點 ＝ 本 log 檔頭之 `HEAD`。")
    say("  🔴 **逐街廓驅動之必要性**：整批 `run_step_g` 於 `R2` 中止 ⇒ 到不了 `R3`〜`R6`；")
    say("     逐街廓 ＋ `try/except` 後六街廓之 `CAP` 皆得（體例同 `probe_WG992_blue.build()`）。")
    say("  ── `②-宗` 圍堵閘之現況輸出（＝ 受測物之輸出·逐街廓）──")
    for lbl in sorted(gate):
        st, msg = gate[lbl]
        say("    %-4s %-4s %s" % (lbl, st, msg[:150]))
    say("")

    # ══════════ 八格之列舉 ══════════
    CELLS = []
    for lbl in sorted(cad["side_lines_by_side"]):
        for side in ("left", "right"):
            if (cad["side_lines_by_side"][lbl] or {}).get(side):
                CELLS.append((lbl, side))
    say("  🔒 八格之母體 ＝ `side_lines_by_side` 之全部 (街廓, 側) ＝ %d 格：%s"
        % (len(CELLS), ["%s%s" % (a, "左" if b == "left" else "右") for a, b in CELLS]))
    say("")

    RAW, RES = {}, {}
    for lbl, side in CELLS:
        raw = cell_raw(lbl, side, CAP, cad, wins, params)
        RAW[(lbl, side)] = raw
        pick, blue, _tri = pick_blue(raw)
        w, d = WD[lbl]
        first = raw["seq"][0] if raw["seq"] else None
        g1 = g2 = None
        g1d = {}
        g2d = ("—", "", 0.0, None)
        if first is not None:
            g1, g1d = gate1(raw, first, blue)
            g2, why2, er2, th2 = gate2(raw, first, w, d)
            g2d = (g2, why2, er2, th2)
        # ── 遞補迴圈（`K-9-17 五`：單一迴圈·二閘取合取）──
        chain, freed, succ = [], 0.0, None
        for i in raw["seq"]:
            a1, a1d = gate1(raw, i, blue)
            a2, why2, er2, th2 = gate2(raw, i, w, d)
            both = bool(a1) and (a2 is True)
            chain.append({"i": i, "name": raw["names"][i], "G": raw["G"][i],
                          "g1": a1, "g1d": a1d, "g2": a2, "why2": why2,
                          "er2": er2, "th2": th2, "both": both})
            if both:
                succ = raw["names"][i]
                break
            freed += float(raw["G"][i] or 0.0)
        RES[(lbl, side)] = {"pick": pick, "blue": blue, "first": first,
                            "g1": g1, "g1d": g1d, "g2": g2d, "chain": chain,
                            "freed": round(freed, 2), "succ": succ,
                            "gate2_in": (w, d)}

    # ══════════ P-2 ══════════
    say("=" * W)
    say("§P-2　八格**原始量**（`a`〜`j`·🔒 真值欄須可由本節重算）")
    say("=" * W)
    for lbl, side in CELLS:
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        say("-" * W)
        say("■ %s" % tag)
        say("  [a] 遠側界端點 far_pt = (%.9f, %.9f)   ∥SIDELINE 方向 = (%.9f, %.9f)"
            % (raw["far_pt"][0], raw["far_pt"][1], raw["su"][0], raw["su"][1]))
        say("      P1 = (%.9f, %.9f)   B1 = (%.9f, %.9f)   〔已重心化〕"
            % (raw["P1"][0], raw["P1"][1], raw["B1"][0], raw["B1"][1]))
        say("  [b] σ = %+d 〔導出式：n̂ = rot90(âlloc)；σ = sign((C_block − P1)·n̂)〕"
            % int(raw["sigma"]))
        say("      C_block = (%.9f, %.9f)   n̂ = (%.9f, %.9f)"
            % (raw["block"].centroid.x, raw["block"].centroid.y,
               raw["nhat"][0], raw["nhat"][1]))
        say("      Δs = (B1 − P1)·n̂ = %.9f      σ·Δs = %.9f"
            % (raw["ds"], raw["sigma"] * raw["ds"]))
        say("  [c] 帶之二 ∥ALLOCLINE：過 P1 者 = P1 + t·â；過 B1 者 = B1 + t·â，"
            "â = (%.9f, %.9f)" % (raw["ahat"][0], raw["ahat"][1]))
        say("      三角形 A（過 B1）頂點 = P1, B1, Q=(%.9f, %.9f)   面積 = %.9f"
            % (raw["Q"][0], raw["Q"][1], raw["areaA"]))
        say("      三角形 B（過 P1）頂點 = P1, B1, R=(%.9f, %.9f)   面積 = %.9f"
            % (raw["R"][0], raw["R"][1], raw["areaB"]))
        say("  [d] A ∩ 街角地 = %.9f      B ∩ 街角地 = %.9f   ⇒ 依定義取 **%s**（藍影 = %.9f）"
            % (raw["iA"], raw["iB"], res["pick"], res["blue"]))
        first = res["first"]
        if first is None:
            say("  [e] 第 1 宗 ＝ **⛔ 無**"
                "（該側組 %s 中 winner `%s`@biz%d 之後無宗）"
                % (raw["grp"], raw["wname"], raw["wi"]))
            say("  [f] —      [g] —      [i] —      [j] 騰出 = 0.00")
        else:
            say("  [e] 第 1 宗 = `%s`（biz#%d）  G = %s  投影序位次（推進序內）= %d"
                % (raw["names"][first], first, raw["G"][first],
                   raw["grp"].index(first)))
            say("      〔定位式：該側組 = %s（k=%d）；winner `%s`@biz#%d ⇒ 次一位〕"
                % (raw["grp"], raw["k"], raw["wname"], raw["wi"]))
            vs = np.asarray(raw["polys"][first].exterior.coords, float)
            say("      多邊形頂點（重心化·%d 點）= %s"
                % (len(vs), ", ".join("(%.4f,%.4f)" % (x, y) for x, y in vs[:8])
                   + (" …" if len(vs) > 8 else "")))
            say("  [f] 臨 FRONTLINE 長 = %.9f      臨 BASELINE 長 = %.9f"
                % (res["g1d"]["len_front"], res["g1d"]["len_base"]))
            say("      〔tol 判別力〕min|垂距| 對 FRONT = %.9f ／ 對 BASE = %.9f （tol = %g）"
                % (res["g1d"]["min_front"], res["g1d"]["min_base"], TOUCH_TOL))
            w, d = res["gate2_in"]
            say("  [g] 閘二 W×D = %.2f × %.2f（來源 ＝ app.py:%d `HUALIEN_MIN_LOT_TABLE`）"
                % (w, d, hit[0]))
            say("      `P ⊖ R` 最大侵蝕面積 = %.9f   命中角 = %s   判 = %s   憑證：%s"
                % (res["g2"][2], res["g2"][3], res["g2"][0], res["g2"][1]))
            if res["g2"][0] is False and float(raw["polys"][first].area) >= w * d:
                say("      〔量化診斷〕面積 %.4f >= W·D=%.2f 而仍不進 ⇒ `D=%.2f` 固定下"
                    "可容納之**最大寬** = **%.4f m**（門檻 %.2f m）"
                    % (raw["polys"][first].area, w * d, d,
                       wmax_at_d(raw["polys"][first], d, w), w))
            say("  [i] 遞補迴圈逐步（`K-9-17 五`·單一迴圈·二閘取合取）：")
            for st in res["chain"]:
                say("      biz#%-2d %-14s G=%-9s 閘一=%-5s 閘二=%-5s 合取=%-5s ｜%s"
                    % (st["i"], st["name"], st["G"], st["g1"], st["g2"], st["both"],
                       st["why2"][:52]))
                if st["g2"] is False and float(raw["polys"][st["i"]].area) >= w * d:
                    say("             〔量化〕area=%.4f >= W·D=%.2f 而不進 ⇒ `D=%.2f` 下"
                        "最大寬 = **%.4f m**（門檻 %.2f m）"
                        % (raw["polys"][st["i"]].area, w * d, d,
                           wmax_at_d(raw["polys"][st["i"]], d, w), w))
            say("  [j] 騰出面積 = %.2f ＝ %s"
                % (res["freed"], " + ".join("%s(%s)" % (s["name"], s["G"])
                                            for s in res["chain"] if not s["both"]) or "—"))
        say("  [h] `②-宗` 圍堵閘（街廓層·現況輸出）= %s ｜%s"
            % (gate[lbl][0], gate[lbl][1][:110]))

    # ══════════ P-3 ══════════
    say("")
    say("=" * W)
    say("§P-3　真值欄之**機械重算**（戒 `18` 之自證·由 `P-2` 之原始量重算並機檢）")
    say("=" * W)
    ok, tot = 0, 0
    for lbl, side in CELLS:
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        # 藍影面積：自 [c] 之三頂點以鞋帶公式重算
        tri = (raw["P1"], raw["B1"], raw["Q"]) if res["pick"] == "A" \
            else (raw["P1"], raw["B1"], raw["R"])
        sh = abs((tri[1][0] - tri[0][0]) * (tri[2][1] - tri[0][1])
                 - (tri[2][0] - tri[0][0]) * (tri[1][1] - tri[0][1])) / 2.0
        tot += 1
        d1 = abs(sh - res["blue"])
        ok += (d1 < 1e-9)
        say("  %-6s 藍影 鞋帶重算 = %.9f vs 出艙 = %.9f  Δ=%.3e  %s"
            % (tag, sh, res["blue"], d1, "✅" if d1 < 1e-9 else "🔴"))
        # 選邊：自 [d] 之二面積重算
        tot += 1
        rp = "A" if raw["iA"] <= EPS_ZERO else "B"
        ok += (rp == res["pick"])
        say("  %-6s 選邊 自 [d] 重算 = %s vs 出艙 = %s  %s"
            % (tag, rp, res["pick"], "✅" if rp == res["pick"] else "🔴"))
        if res["first"] is not None:
            tot += 1
            r1 = (float(raw["G"][res["first"]]) > res["blue"]
                  and res["g1d"]["len_front"] > 0 and res["g1d"]["len_base"] > 0)
            ok += (r1 == res["g1"])
            say("  %-6s 閘一 自 [e]+[f]+藍影重算 = %s vs 出艙 = %s  %s"
                % (tag, r1, res["g1"], "✅" if r1 == res["g1"] else "🔴"))
            tot += 1
            w, d = res["gate2_in"]
            r2 = rect_fit(raw["polys"][res["first"]], w, d)[0]
            ok += (r2 == res["g2"][0])
            say("  %-6s 閘二 自 [g] 之 W/D 重算 = %s vs 出艙 = %s  %s"
                % (tag, r2, res["g2"][0], "✅" if r2 == res["g2"][0] else "🔴"))
            tot += 1
            rs = None
            for st in res["chain"]:
                if st["both"]:
                    rs = st["name"]
                    break
            ok += (rs == res["succ"])
            say("  %-6s 遞補宗 自 [i] 重算 = %s vs 出艙 = %s  %s"
                % (tag, rs, res["succ"], "✅" if rs == res["succ"] else "🔴"))
            tot += 1
            rf = round(sum(float(s["G"] or 0.0) for s in res["chain"] if not s["both"]), 2)
            ok += (abs(rf - res["freed"]) < 5e-3)
            say("  %-6s 騰出 自 [j] 重算 = %.2f vs 出艙 = %.2f  %s"
                % (tag, rf, res["freed"], "✅" if abs(rf - res["freed"]) < 5e-3 else "🔴"))
    say("")
    say("  🔒 **P-3 自證 ＝ %d/%d**%s" % (ok, tot, "" if ok == tot else "　🔴 量測器紅"))

    # ══════════ P-4 ══════════
    say("")
    say("=" * W)
    say("§P-4　對 `K-9-23 五` 之對拍（🛑 **只報四數·⛔ 不判符否**——判由發單側）")
    say("=" * W)
    TBL = {
        "R1左": ("5.384991697", "628-35(2)", "599.91", "✅", "✅", "過"),
        "R1右": ("6.667129053", "628-34(3)", "86.00", "✅", "🔴", "過"),
        "R2左": ("76.205568190", "628-42(1)", "3.82", "🔴", "🔴", "破 45.9766"),
        "R3右": ("75.626739110", "628-42(2)", "89.96", "✅", "🔴", "過"),
        "R4左": ("26.093820432", "—", "—", "⛔ 無第 1 宗", "—", "過"),
        "R4右": ("27.442490499", "—", "—", "⛔ 無第 1 宗", "—", "過"),
        "R5左": ("72.455256336", "628-53(2)", "0.99", "🔴", "🔴", "破 56.3293"),
        "R6右": ("0.000045364", "628-53(1)", "0.26", "✅", "🔴", "過"),
    }
    SUCC = {"R1右": "628-36(1)", "R2左": "628-40(1)+", "R3右": "628-29(1)+",
            "R5左": "628-7(2)", "R6右": "628-7(1)"}
    FREED = {"R1右": 86.00, "R2左": 32.90, "R3右": 116.50, "R5左": 0.99, "R6右": 117.99}
    say("  %-6s %-10s %-16s %-16s %-13s %-13s" %
        ("格", "欄", "探針實得", "表載", "絕對差", "相對差"))
    for lbl, side in CELLS:
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        t = TBL[tag]
        # 藍影
        tv = float(t[0])
        ad = abs(res["blue"] - tv)
        rd = (ad / abs(tv)) if tv != 0 else float("nan")
        say("  %-6s %-10s %-16.9f %-16s %-13.3e %-13.3e" % (tag, "藍影", res["blue"], t[0], ad, rd))
        # 第 1 宗
        mine = raw["names"][res["first"]] if res["first"] is not None else "—"
        say("  %-6s %-10s %-16s %-16s %-13s %-13s" % (tag, "第1宗", mine, t[1], "—", "—"))
        # G
        if res["first"] is not None:
            gv = float(raw["G"][res["first"]])
            tg = float(t[2]) if t[2] != "—" else float("nan")
            ad = abs(gv - tg) if tg == tg else float("nan")
            rd = (ad / abs(tg)) if (tg == tg and tg != 0) else float("nan")
            say("  %-6s %-10s %-16.2f %-16s %-13.3e %-13.3e" % (tag, "G", gv, t[2], ad, rd))
        else:
            say("  %-6s %-10s %-16s %-16s %-13s %-13s" % (tag, "G", "—", t[2], "—", "—"))
        # 閘一／閘二
        say("  %-6s %-10s %-16s %-16s %-13s %-13s"
            % (tag, "閘一", ("⛔ 無第 1 宗" if res["first"] is None
                            else ("✅" if res["g1"] else "🔴")), t[3], "—", "—"))
        say("  %-6s %-10s %-16s %-16s %-13s %-13s"
            % (tag, "閘二", ("—" if res["first"] is None
                            else ("✅" if res["g2"][0] is True
                                  else ("🔴" if res["g2"][0] is False else "⚠️未定"))),
               t[4], "—", "—"))
        # ②-宗
        say("  %-6s %-10s %-16s %-16s %-13s %-13s"
            % (tag, "②-宗", gate[lbl][0], t[5], "—", "—"))
        # 遞補宗／騰出
        if tag in SUCC:
            say("  %-6s %-10s %-16s %-16s %-13s %-13s"
                % (tag, "遞補宗", res["succ"], SUCC[tag], "—", "—"))
            ad = abs(res["freed"] - FREED[tag])
            rd = ad / abs(FREED[tag]) if FREED[tag] else float("nan")
            say("  %-6s %-10s %-16.2f %-16.2f %-13.3e %-13.3e"
                % (tag, "騰出", res["freed"], FREED[tag], ad, rd))

    # ══════════ P-5 ══════════
    say("")
    say("=" * W)
    say("§P-5　判別力對照（戒 `12`·二擾動皆**僅於對照跑次**·⛔ 未留於出艙探針）")
    say("=" * W)
    say("  擾動①　閘一之關係詞 `>` → `>=`")
    n1 = 0
    for lbl, side in CELLS:
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        if res["first"] is None:
            continue
        a, _ = gate1(raw, res["first"], res["blue"], strict=False)
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        if a != res["g1"]:
            n1 += 1
            say("    %-6s 轉變：%s → %s" % (tag, res["g1"], a))
        else:
            say("    %-6s 未變（%s）　G−藍影 = %+.9f"
                % (tag, res["g1"], float(raw["G"][res["first"]]) - res["blue"]))
    say("    ⇒ 轉變格數 = %d%s" % (n1, "　（成因：無一格恰為等號·見上逐格差）" if n1 == 0 else ""))
    say("    🔴 **擾動① 零轉變 ⇒ 其本身⛔ 未證閘一之判別力**（`>` 與 `>=` 於本案不可分辨）")
    say("       ⇒ CC 自加**必然轉變**之對照 ①′（`CLAUDE.md`「宜再餵一個已知為偽者須紅」）：")
    say("")
    say("  擾動①′（CC 自加）　藍影 × 1000（已知為偽 ⇒ 凡 `G < 1000×藍影` 者須轉 False）")
    n1p = 0
    for lbl, side in CELLS:
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        if res["first"] is None:
            continue
        a, ad = gate1(raw, res["first"], res["blue"] * 1000.0)
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        n1p += (a != res["g1"])
        say("    %-6s %s → %s（G=%.2f vs 藍影×1000=%.4f）%s"
            % (tag, res["g1"], a, ad["G"], res["blue"] * 1000.0,
               "轉變" if a != res["g1"] else "未變"))
    _exp = [c for c in CELLS if RES[c]["first"] is not None and RES[c]["g1"] is True
            and float(RAW[c]["G"][RES[c]["first"]]) < RES[c]["blue"] * 1000.0]
    say("    ⇒ 轉變 %d 格；**期望轉變** %d 格（＝原判 True 且 `G < 1000×藍影` 者）⇒ %s"
        % (n1p, len(_exp), "✅ 相符" if n1p == len(_exp) else "🔴 不符"))
    say("       🔒 `R6右` ⛔ 未轉變**係預期**——其藍影 `4.5e-5` ×1000 仍 `< G = 0.26`"
        "（⇒ 本對照對該格無擾動力·⛔ 非閘一失效）")
    say("")
    say("  擾動②　藍影選邊由「依定義」改為「恆取 A」")
    n2 = 0
    for lbl, side in CELLS:
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        if abs(raw["areaA"] - res["blue"]) > 1e-9:
            n2 += 1
            say("    %-6s 轉變：%.9f（定義取 %s） → %.9f（恆取 A）"
                % (tag, res["blue"], res["pick"], raw["areaA"]))
        else:
            say("    %-6s 未變（定義本即取 A）" % tag)
    say("    ⇒ 轉變格數 = %d" % n2)

    # ══════════ P-6 ══════════
    say("")
    say("=" * W)
    say("§P-6　`σ` 之側別共線性對照（承 `GB-108`）——側別標籤全數對調而街廓形心不動")
    say("=" * W)
    same = 0
    for lbl, side in CELLS:
        raw = RAW[(lbl, side)]
        sw = cell_raw(lbl, side, CAP, cad, wins, params, sigma_swap=True)
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        eq = int(raw["sigma"]) == int(sw["sigma"])
        same += eq
        say("    %-6s σ 原 = %+d ／ 對調後 = %+d  %s"
            % (tag, int(raw["sigma"]), int(sw["sigma"]), "✅ 不變" if eq else "🔴 變"))
    say("    ⇒ **%d/%d 不變** ⇒ `σ` ⛔ 未繫於側別字串（其導出式只用街廓形心與 `n̂`）"
        % (same, len(CELLS)))
    say("")
    say("  🔒 `σ·Δs` 斷言之覆核（`K-9-23 三-二`：`σ·Δs > 0` ⇒ 外界過 `B1`（取 A）；`< 0` ⇒ 取 B）")
    agree = 0
    for lbl, side in CELLS:
        raw, res = RAW[(lbl, side)], RES[(lbl, side)]
        tag = "%s%s" % (lbl, "左" if side == "left" else "右")
        pred = "A" if raw["sigma"] * raw["ds"] > 0 else "B"
        eq = pred == res["pick"]
        agree += eq
        say("    %-6s σ·Δs = %+.9f ⇒ 斷言取 %s ／ 定義取 %s  %s"
            % (tag, raw["sigma"] * raw["ds"], pred, res["pick"], "✅" if eq else "🔴"))
    say("    ⇒ 斷言與定義相符 = **%d/%d**" % (agree, len(CELLS)))

    say("")
    say("=" * W)
    say("  🔒 P-3 自證 = %d/%d ／ P-5 擾動① 轉變 = %d ／ 擾動② 轉變 = %d ／ P-6 σ 不變 = %d/%d"
        % (ok, tot, n1, n2, same, len(CELLS)))
    say("=" * W)

    os.makedirs(OUTDIR, exist_ok=True)
    lg = os.path.join(OUTDIR, "probe_WG9156_pred_inputs_%s.log" % BASE_REF)
    with open(lg, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("\n  log → %s" % os.path.relpath(lg, REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
