#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-38】相鄰性之三獨立判準 ＋ 楔形之幾何量測（⛔ 零生產碼·新檔）

受詞（施工單 W-G.9-38）：
  A-2 三個**互相獨立**之相鄰性判準（甲：多邊形距離／乙：共用邊界／丙：視線遮擋）
  B-1 逐宗兩側界之方向與夾角
  B-2 界線對之夾角（判不平行）
  B-3 楔形交集之尖端定位

🔴 **判準與門檻於本檔頂端先寫下**（⛔ 未看結果才訂·施工單明令）：
  · 判準甲（多邊形距離）：`g_i.distance(g_j) <= THRESH_DIST` ⇒ 判**相鄰**
      `THRESH_DIST = 0.001`（公尺·量測框＝地籍座標單位）
  · 判準乙（共用邊界）：`g_i.boundary.intersection(g_j.boundary).length > THRESH_LEN` ⇒ 判**相鄰**
      `THRESH_LEN = 0.0`（嚴格大於 0·⛔ 只共一點者其 length ＝ 0 ⇒ 判不相鄰）
  · 判準丙（視線遮擋）：連接兩宗 `representative_point()` 之線段，
      若**穿過任何第三宗之 interior**（相交長度 > `THRESH_LOS`）⇒ 判**不相鄰**；否則判相鄰
      `THRESH_LOS = 0.001`
      🔒 用 `representative_point`（⛔ 非 `centroid`）——凹多邊形之 centroid 可落在形外。
  · 判「平行」之門檻（B-2）：兩單位方向向量之**夾角** `<= THRESH_PARA_DEG = 0.001` 度
      ⛔ **不以原始 Δ 分量比 1e-3**（已否證：同一直線之不同分段其 Δ 互異）。

🔒 輸出檔名含產生它的 commit 短碼；掃描母體⛔ 不含自身輸出；⛔ 不覆寫任何既有 log。
"""
import math
import os
import subprocess
import sys

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
W = 170

THRESH_DIST = 0.001
THRESH_LEN = 0.0
THRESH_LOS = 0.001
THRESH_PARA_DEG = 0.001


def _short_sha():
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           cwd=VERIFY, capture_output=True, text=True, timeout=20)
        return (r.stdout or "").strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


# ── 三判準（⛔ 互相獨立·各不呼叫對方）─────────────────────────────────────
def crit_A(gi, gj):
    """甲：多邊形最短距離。"""
    d = float(gi.distance(gj))
    return (d <= THRESH_DIST), d


def crit_B(gi, gj):
    """乙：邊界交集之長度。"""
    try:
        L = float(gi.boundary.intersection(gj.boundary).length)
    except Exception:                                               # noqa: BLE001
        return None, None
    return (L > THRESH_LEN), L


def crit_C(gi, gj, others):
    """丙：視線遮擋。回 (是否相鄰, 被穿過之第三宗清單, 最長穿越長)。"""
    from shapely.geometry import LineString
    pi, pj = gi.representative_point(), gj.representative_point()
    seg = LineString([(pi.x, pi.y), (pj.x, pj.y)])
    blocked, mx = [], 0.0
    for k, gk in others:
        try:
            L = float(seg.intersection(gk).length)
        except Exception:                                           # noqa: BLE001
            continue
        if L > THRESH_LOS:
            blocked.append(k)
            mx = max(mx, L)
    return (not blocked), blocked, mx


def ang_deg(u, v):
    """兩方向之夾角（度·取 [0,90]·⛔ 號無關）。

    🩸 **首版用 `acos(|dot|)`，其自檢對傾斜平行四邊形之對邊得 `8.54e-7°` 而非 0**
    ——成因：`acos` 於 `c → 1` 時導數發散（`d(acos)/dc → ∞`），
    浮點之 `c` 誤差 `~1e-16` 被放大為角度 `~1e-8` 弧度。**⛔ 非該二邊真的不平行。**
    ⇒ 依「先疑量測器」改用 `atan2(|cross|, |dot|)`：其於夾角 → 0 時
    `atan2(ε, 1) ≈ ε` **線性且穩定**，⛔ 無放大。
    """
    d = abs(u[0] * v[0] + u[1] * v[1])
    cr = abs(u[0] * v[1] - u[1] * v[0])
    return math.degrees(math.atan2(cr, d))


def unit(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    if L == 0:
        return None, 0.0
    ux, uy = dx / L, dy / L
    if (ux < 0) or (ux == 0 and uy < 0):
        ux, uy = -ux, -uy
    return (ux, uy), L


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    import shapely
    from shapely.geometry import Polygon as _Pg
    P("=" * W)
    P("【W-G.9-38】相鄰性之三獨立判準 ＋ 楔形之幾何量測")
    P("=" * W)
    P(f"  產生於 commit：{sha}")
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P(f"  🔴 門檻（**先寫下再量**）：甲 dist<={THRESH_DIST}／乙 len>{THRESH_LEN}"
      f"／丙 los>{THRESH_LOS} 即遮擋／平行 <= {THRESH_PARA_DEG}°")
    P("")

    # ── §0 三判準之判別力自檢（⛔ 各自一組·⛔ 不共用）────────────────────
    P("【0】三判準之判別力自檢（⛔ 各判準各一組·⛔ 不共用·附對照組實際輸出）")
    P("-" * W)
    # 🔒 自檢用之測資【刻意傾斜】——⛔ 不用軸向矩形（考古：對照物須具備使量測困難之性質）
    SK = 0.35   # 斜率（使各邊皆非軸向）
    def skew(pts):
        return _Pg([(x + SK * y, y) for x, y in pts])
    adj1 = skew([(0, 0), (5, 0), (5, 10), (0, 10)])
    adj2 = skew([(5, 0), (10, 0), (10, 10), (5, 10)])          # 與 adj1 共一整條邊
    far2 = skew([(12, 0), (17, 0), (17, 10), (12, 10)])        # 與 adj1 相距 7
    pt2 = skew([(5, 10), (10, 10), (10, 20), (5, 20)])         # 與 adj1 僅共一點 (5,10)
    ok = {}
    # 甲
    a1, d1 = crit_A(adj1, adj2)
    a2, d2 = crit_A(adj1, far2)
    ok["甲"] = (a1 is True) and (a2 is False)
    P(f"  甲（距離）已知相鄰：dist={d1:.6f} ⇒ 判{'相鄰' if a1 else '不相鄰'}"
      f"　已知不相鄰：dist={d2:.6f} ⇒ 判{'相鄰' if a2 else '不相鄰'}"
      f"　⇒ {'✅' if ok['甲'] else '🔴'}")
    # 乙
    b1, l1 = crit_B(adj1, adj2)
    b2, l2 = crit_B(adj1, pt2)
    ok["乙"] = (b1 is True) and (b2 is False)
    P(f"  乙（共邊長）已知共整條邊：len={l1:.6f} ⇒ 判{'相鄰' if b1 else '不相鄰'}"
      f"　已知僅共一點：len={l2:.6f} ⇒ 判{'相鄰' if b2 else '不相鄰'}"
      f"　⇒ {'✅' if ok['乙'] else '🔴'}")
    # 丙
    mid = skew([(5, 0), (7, 0), (7, 10), (5, 10)])             # 夾在 adj1 與 far2 之間
    c1, bl1, m1 = crit_C(adj1, far2, [(9, mid)])               # 中間有 ⇒ 須判不相鄰
    c2, bl2, m2 = crit_C(adj1, far2, [(9, pt2)])               # 中間無（pt2 在上方）⇒ 須判相鄰
    ok["丙"] = (c1 is False) and (c2 is True)
    P(f"  丙（視線）中間有第三宗：blocked={bl1} 穿越長={m1:.6f} ⇒ 判{'相鄰' if c1 else '不相鄰'}"
      f"　中間無：blocked={bl2} ⇒ 判{'相鄰' if c2 else '不相鄰'}"
      f"　⇒ {'✅' if ok['丙'] else '🔴'}")
    P(f"  🔒 自檢用測資【刻意傾斜】（skew={SK}·各邊皆非軸向）"
      f"——⛔ 未以軸向矩形自檢一個須處理傾斜多邊形之量測器")
    P(f"  ⇒ 自檢結果：甲 {'PASS' if ok['甲'] else 'FAIL'}／"
      f"乙 {'PASS' if ok['乙'] else 'FAIL'}／丙 {'PASS' if ok['丙'] else 'FAIL'}")
    for k, v in ok.items():
        if not v:
            P(f"  🛑 判準{k} 紅 ⇒ 其結果⛔ 不得出艙（S-2·其餘判準照辦）")

    # ── §1 驅動 ────────────────────────────────────────────────────────
    ns, fake_st = harvest()
    CAP = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        key = (_spy.tag, _label, _spy.seq.get((_spy.tag, _label), 0))
        _spy.seq[(_spy.tag, _label)] = _spy.seq.get((_spy.tag, _label), 0) + 1
        _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
        CAP[key] = {"block": block_poly, "d_hat": np.asarray(d_hat, float),
                    "alloc": np.asarray(allocation_dir, float) if allocation_dir is not None else None,
                    "biz": list(_biz)}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)
    _spy.seq = {}
    _spy.tag = ""

    import contextlib
    import io as _io
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    TARGET = "R2"
    sb = 0.0
    _spy.tag = f"{sb:g}m"
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, sb, snapshot=snapshot)
    ns["_pool_strips_for_block"] = _spy
    try:
        with contextlib.redirect_stdout(_io.StringIO()):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                           [tp for tp in build_p if tp.get("所屬街廓") == TARGET],
                           wins, forced, sb)
            except Exception:                                       # noqa: BLE001
                pass        # 🔴 ②-宗 圍堵閘於 R2 必破（本批受詞）·CAP 已於其前存好
    finally:
        ns["_pool_strips_for_block"] = _orig

    key = next((k for k in CAP if k[0] == "0m" and k[1] == TARGET), None)
    if key is None:
        P("")
        P(f"🛑 未攔到 {TARGET} 之 0m 呼叫 ⇒ ⛔ 無從量測")
        return L, sha
    biz = CAP[key]["biz"]
    d_hat = CAP[key]["d_hat"]
    alloc = CAP[key]["alloc"]

    # ── §2 A-2／A-3：三判準逐對 ──────────────────────────────────────
    P("")
    P("【A-2／A-3】三獨立判準逐對（⛔ 不投票·不一致即具名為發現）")
    P("-" * W)
    P(f"  {'對':<12}{'甲:dist':>12}{'甲判':>7}{'乙:共邊長':>12}{'乙判':>7}"
      f"{'丙:遮擋者':>16}{'丙:穿越長':>12}{'丙判':>7}{'  出艙碼':<26}")
    QUAD = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    for (i, j) in QUAD:
        if max(i, j) >= len(biz):
            continue
        others = [(k, biz[k]) for k in range(len(biz)) if k not in (i, j)]
        aok, ad = crit_A(biz[i], biz[j])
        bok, bl = crit_B(biz[i], biz[j])
        cok, cbl, cm = crit_C(biz[i], biz[j], others)
        votes = [aok, bok, cok]
        if all(v is True for v in votes):
            code = "三判準一致判相鄰"
        elif all(v is False for v in votes):
            code = "三判準一致判不相鄰"
        else:
            code = "🔴 三判準不一致"
        P(f"  宗{i}×宗{j:<7}{ad:>12.6f}{('相鄰' if aok else '不相鄰'):>7}"
          f"{bl:>12.6f}{('相鄰' if bok else '不相鄰'):>7}"
          f"{(str(cbl) if cbl else '（無）'):>16}{cm:>12.6f}"
          f"{('相鄰' if cok else '不相鄰'):>7}  {code:<26}")

    # ── §3 B-1：逐宗兩側界之方向 ────────────────────────────────────
    P("")
    P("【B-1】逐宗兩側界之方向與夾角（左組 i=0..7·⛔ 側界＝與正街夾角最大之二邊）")
    P("-" * W)
    P("  🔒 量測器自檢：")
    _ax = _Pg([(0, 0), (10, 0), (10, 5), (0, 5)])
    _e = list(_ax.exterior.coords)
    _angs = sorted({round(ang_deg(unit(_e[t], _e[t + 1])[0], (1.0, 0.0)), 6)
                    for t in range(len(_e) - 1)})
    P(f"    軸向矩形之各邊與 x 軸夾角集合 = {_angs}  期望 [0.0, 90.0] ⇒ "
      f"{'✅' if _angs == [0.0, 90.0] else '🔴'}")
    _th = math.radians(23.0)
    _pg = _Pg([(0, 0), (10, 0), (10 + 5 * math.sin(_th), 5 * math.cos(_th)),
               (5 * math.sin(_th), 5 * math.cos(_th))])
    _pe = list(_pg.exterior.coords)
    _u = [unit(_pe[t], _pe[t + 1])[0] for t in range(len(_pe) - 1)]
    _opp1 = ang_deg(_u[0], _u[2])
    _opp2 = ang_deg(_u[1], _u[3])
    _adj = ang_deg(_u[0], _u[1])
    _s4 = (_opp1 < 1e-9 and _opp2 < 1e-9)
    P(f"    傾斜平行四邊形（斜角 23°）：對邊夾角 = {_opp1:.9f}° / {_opp2:.9f}°"
      f"（期望 0°）⇒ {'✅' if _s4 else '🛑 S-4'}")
    P(f"    　　　　　　　　　　　　　　鄰邊夾角 = {_adj:.6f}°（期望 = 90−23 = 67°）⇒ "
      f"{'✅' if abs(_adj - 67.0) < 1e-6 else '⚠️ ' + f'{_adj:.6f}'}")
    if not _s4:
        P("  🛑 S-4 觸發 ⇒ 停機，⛔ B 組不得出艙")
        return L, sha

    SIDES = {}
    P("")
    P(f"  {'i':<4}{'近側界 u':>26}{'遠側界 u':>26}{'兩側界夾角':>12}"
      f"{'近側vs正街':>12}{'遠側vs正街':>12}")
    for i in range(min(8, len(biz))):
        g = biz[i]
        ext = list(g.exterior.coords)
        edges = []
        for t in range(len(ext) - 1):
            u, ln = unit(ext[t], ext[t + 1])
            if u is None or ln < 1e-9:
                continue
            mid_s = ((ext[t][0] + ext[t + 1][0]) / 2 * d_hat[0]
                     + (ext[t][1] + ext[t + 1][1]) / 2 * d_hat[1])
            edges.append((ang_deg(u, tuple(d_hat)), u, ln, mid_s))
        edges.sort(key=lambda e: -e[0])            # 與正街夾角最大者 ＝ 側界
        two = sorted(edges[:2], key=lambda e: e[3])
        if len(two) < 2:
            continue
        near, far = two[0], two[1]
        SIDES[i] = {"near": near[1], "far": far[1]}
        P(f"  {i:<4}({near[1][0]:>9.6f},{near[1][1]:>9.6f}) "
          f"({far[1][0]:>9.6f},{far[1][1]:>9.6f})"
          f"{ang_deg(near[1], far[1]):>12.6f}"
          f"{near[0]:>12.6f}{far[0]:>12.6f}")
    if alloc is not None:
        au, _ = unit((0.0, 0.0), tuple(alloc))
        P(f"  參考：ALLOC 方向 u = ({au[0]:.6f}, {au[1]:.6f})；"
          f"正街 d_hat = ({d_hat[0]:.6f}, {d_hat[1]:.6f})；二者夾角 = "
          f"{ang_deg(au, tuple(d_hat)):.6f}°")

    # ── §4 B-2：界線對之夾角 ──────────────────────────────────────
    P("")
    P(f"【B-2】宗 i 之遠側界 × 宗 j 之近側界（平行門檻 <= {THRESH_PARA_DEG}°·**先寫下**）")
    P("-" * W)
    P(f"  {'對':<14}{'夾角(度)':>14}{'判':>10}")
    nonpara = 0
    for (i, j) in QUAD:
        if i not in SIDES or j not in SIDES:
            continue
        a = ang_deg(SIDES[i]["far"], SIDES[j]["near"])
        par = a <= THRESH_PARA_DEG
        if not par:
            nonpara += 1
        P(f"  宗{i}遠×宗{j}近 {a:>14.6f}{('平行' if par else '🔴 不平行'):>10}")
    P(f"  ⇒ 超出門檻（不平行）之對數 = {nonpara}")

    # ── §5 B-3：楔形尖端 ──────────────────────────────────────────
    P("")
    P("【B-3】楔形交集之尖端定位")
    P("-" * W)
    nrm = np.array([-d_hat[1], d_hat[0]])
    for (i, j) in [(0, 3), (0, 2)]:
        if max(i, j) >= len(biz):
            continue
        inter = biz[i].intersection(biz[j])
        if inter.is_empty or getattr(inter, "geom_type", "") != "Polygon":
            P(f"  宗{i}×宗{j}：⛔ 非單一 Polygon ⇒ 無從判定")
            continue
        pts = list(inter.exterior.coords)[:-1]
        P(f"  宗{i}×宗{j}　頂點數 {len(pts)}　座標：")
        for p in pts:
            P(f"      ({p[0]:.4f}, {p[1]:.4f})　t(垂直正街) = {p[0]*nrm[0]+p[1]*nrm[1]:.4f}")
        # 內角
        angs = []
        n = len(pts)
        for t in range(n):
            a0, a1, a2 = pts[(t - 1) % n], pts[t], pts[(t + 1) % n]
            v1 = (a0[0] - a1[0], a0[1] - a1[1])
            v2 = (a2[0] - a1[0], a2[1] - a1[1])
            L1 = math.hypot(*v1) or 1.0
            L2 = math.hypot(*v2) or 1.0
            c = (v1[0] * v2[0] + v1[1] * v2[1]) / (L1 * L2)
            angs.append(math.degrees(math.acos(max(-1.0, min(1.0, c)))))
        k = min(range(n), key=lambda t: angs[t])
        tip = pts[k]
        P(f"    內角 = {[round(x,4) for x in angs]}　⇒ 尖端 ＝ 頂點 {k} {tuple(round(x,4) for x in tip)}"
          f"（內角 {angs[k]:.4f}°）")
        tt = [p[0] * nrm[0] + p[1] * nrm[1] for p in pts]
        tip_t = tt[k]
        lo_t, hi_t = min(tt), max(tt)
        span = hi_t - lo_t
        rel = (tip_t - lo_t) / span if span > 1e-12 else 0.5
        if span < 1e-9:
            code = "無從判定（交集之 t 跨距退化）"
        elif rel <= 0.25:
            code = "尖端在前緣側" if tip_t == lo_t or rel <= 0.25 else "尖端在中段"
        elif rel >= 0.75:
            code = "尖端在後緣側"
        else:
            code = "尖端在中段"
        P(f"    t 跨距 [{lo_t:.4f}, {hi_t:.4f}]（span {span:.4f}）　尖端 t = {tip_t:.4f}"
          f"　相對位置 {rel:.4f}")
        P(f"    🔒 出艙碼 ＝ **{code}**"
          f"（判準先寫下：rel<=0.25 ⇒ 前緣側／>=0.75 ⇒ 後緣側／其餘 ⇒ 中段）")
        P(f"    尖端至 t 較小端之距 = {tip_t-lo_t:.4f}　至 t 較大端之距 = {hi_t-tip_t:.4f}")
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG938_adjacency3_{_sha}.log")
    with open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
