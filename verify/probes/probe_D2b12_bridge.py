# -*- coding: utf-8 -*-
r"""**D-2b-12 §b0-2**：`_block_strip` 雙線／單線之**橋接測試**（難幾何·修前/修後對拍）。

## 為何需要

D-2b-11【a-3】第 1 項所測「差 0.0」係**假象**：其合成案例為
`Polygon([(0,0),(200,0),(200,120),(0,120)])`（**軸對齊·整數座標**）——該幾何下
`block ∩ 平行四邊形`（一次交集）與 `block ∩ hp_near ∩ hp_far`（兩次交集）**必然同值**，
**鑑別力為零**。本檔改以**難幾何**（不規則、非整數、斜交、任意方位）重測。

## 四項（⛔ 逐項印實測值·不得只印 PASS）

1. **同向委派逐位等價**：`n_hat_far` 同向 ⇒ 面積與 `None` **逐位 `==`** 且 `equals()`；不同者須 0 例。
   ⚠️ **修前應大量失敗** ⇒ 修前/修後兩組數字皆須入 log。
2. **委派門檻兩側**：`|cross|` 略小／略大於 tol，證前者走單線、後者走雙線。
3. **非同向鋪滿**（難幾何）：三片共用界線數值 ⇒ Σ == 整體、兩兩交集 `== 0.0`。
4. **容差上界**：六街廓實測直徑 `D`、`½·D²·tol`、與覆蓋閘 `0.01` 之比較（逐街廓）。

🔒 以 `ns` harvest 取生產原語本體（比照 `probe_K9_geo2_W1_calibre.py:100`），⛔ 未複刻切線式。
🔒 容差同源交叉檢查：`app.py` 之新常數 == `verify/stepg_pipeline.py` 之 `_PAR_TOL`；不等 ⇒ raise。
"""
import io
import math
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, os.environ.get("WV_BRIDGE_LOG", "probe_D2b12_bridge.log"))
BEFORE = os.path.join(OUTDIR, "probe_D2b12_bridge_before.log")
SEED = 20260809
W = 200
COVER_GATE = 0.01


def _unit(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n)


def _rot(v, th):
    c, s = math.cos(th), math.sin(th)
    return (v[0] * c - v[1] * s, v[0] * s + v[1] * c)


def _cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def _hard_polys(rng, k=4):
    """難幾何母體：不規則、**非整數**座標、頂點數與半徑皆隨機（⛔ 非軸對齊整數矩形）。"""
    from shapely.geometry import Polygon
    out = []
    for _ in range(k):
        cx = rng.uniform(-137.317, 421.983)
        cy = rng.uniform(-82.941, 318.277)
        n = rng.randint(7, 11)
        pts, a = [], rng.uniform(0.0, 2 * math.pi)
        for i in range(n):
            a += (2 * math.pi / n) * rng.uniform(0.55, 1.45)
            r = rng.uniform(43.137, 118.859)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        p = Polygon(pts)
        if not p.is_valid:
            p = p.buffer(0)
        if p.is_empty or p.area < 500.0 or p.geom_type != "Polygon":
            continue
        out.append(p)
    return out


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    import numpy as np

    ns, fake_st = harvest()
    bs = ns["_block_strip"]
    rng = random.Random(SEED)

    L = []
    L.append("=" * W)
    L.append(f"【D-2b-12 §b0-2】`_block_strip` 橋接測試（**難幾何**·seed={SEED}）")
    L.append("=" * W)

    # ── 容差同源 ──
    _app_tol = ns.get("_STRIP_PARALLEL_TOL")
    _stepg_tol = None
    _m = re.search(r"_PAR_TOL\s*=\s*([0-9eE.+-]+)",
                   io.open(os.path.join(VERIFY, "stepg_pipeline.py"),
                           encoding="utf-8").read())
    if _m:
        _stepg_tol = float(_m.group(1))
    L.append("")
    L.append("【0】容差同源交叉檢查")
    L.append("-" * W)
    L.append(f"  `app.py` `_STRIP_PARALLEL_TOL` ＝ {_app_tol!r}"
             + ("　（**修前·常數尚未存在**）" if _app_tol is None else ""))
    L.append(f"  `verify/stepg_pipeline.py` `_PAR_TOL` ＝ {_stepg_tol!r}")
    if _app_tol is not None:
        if _stepg_tol is None or float(_app_tol) != float(_stepg_tol):
            raise RuntimeError(
                f"🔴 容差不同源：app `_STRIP_PARALLEL_TOL`={_app_tol} ≠ "
                f"stepg `_PAR_TOL`={_stepg_tol}（停）")
        L.append(f"  ⇒ ✅ **兩值相等**（{_app_tol!r} == {_stepg_tol!r}）")
    TOL = float(_app_tol) if _app_tol is not None else float(_stepg_tol or 1e-6)

    polys = _hard_polys(rng)
    L.append("")
    L.append(f"  難幾何母體 ＝ **{len(polys)}** 個不規則多邊形（非整數座標·⛔ 非軸對齊矩形）")
    for i, p in enumerate(polys):
        _c = list(p.exterior.coords)[0]
        L.append(f"    #{i} 頂點 {len(p.exterior.coords) - 1}　面積 {p.area:.6f}"
                 f"　首頂點 ({_c[0]:.6f}, {_c[1]:.6f})")
    if not polys:
        raise RuntimeError("🔴 難幾何母體為空 ⇒ 失敗（⛔ 不得靜默）")

    # ══ 1 同向委派逐位等價 ══
    L.append("")
    L.append("【1】同向委派**逐位等價**（`n_hat_far` 同向 vs `None`）")
    L.append("-" * W)
    cases, bad, maxd = 0, [], 0.0
    for pi, poly in enumerate(polys):
        bnd = poly.bounds
        for _t in range(6):
            ang = rng.uniform(0, 2 * math.pi)
            d_hat = np.array(_unit((math.cos(ang), math.sin(ang))))
            aang = ang + math.radians(rng.uniform(0.3, 40.0))     # 斜交 0.3°–40°
            alloc = _unit((math.cos(aang), math.sin(aang)))
            n_near = _unit((-alloc[1], alloc[0]))                 # ＝ rot90(alloc)
            bp = (rng.uniform(bnd[0], bnd[2]), rng.uniform(bnd[1], bnd[3]))
            S = rng.choice([0.37, 1.83, 12.9, 47.61, 233.7])      # 次公尺 → 跨街廓
            _g0, _a0 = bs(poly, d_hat, bp, S, allocation_dir=alloc)
            for _sign, _tag in ((1.0, "同向"), (-1.0, "反向(同一條線)")):
                _nf = (n_near[0] * _sign, n_near[1] * _sign)
                _g1, _a1 = bs(poly, d_hat, bp, S, allocation_dir=alloc, n_hat_far=_nf)
                cases += 1
                _eq = (_a0 == _a1)
                _geq = (_g0 is None and _g1 is None) or (
                    _g0 is not None and _g1 is not None and _g0.equals(_g1))
                _d = abs((_a1 or 0.0) - (_a0 or 0.0))
                maxd = max(maxd, _d)
                if not (_eq and _geq):
                    bad.append((pi, _tag, S, _a0, _a1, _d))
    L.append(f"  母體 ＝ **{cases}** 例（⛔ 非空）")
    L.append(f"  **不逐位相同者 ＝ {len(bad)} 例**　**最大絕對差 ＝ {maxd!r}**")
    for b in bad[:8]:
        L.append(f"    🔴 poly#{b[0]} {b[1]} S={b[2]}　None={b[3]!r}／雙線={b[4]!r}"
                 f"　|Δ|={b[5]:.6e}")
    if len(bad) > 8:
        L.append(f"    …（另 {len(bad) - 8} 例）")
    L.append("  ⇒ " + ("✅ **0 例不同**（同向已委派回單線路徑）" if not bad
                      else f"🔴 **{len(bad)} 例不同** ⇒ 尚未委派（此為<u>修前</u>之預期樣貌）"))

    # 修前/修後對拍
    L.append("")
    L.append("  🔒 **修前／修後對拍**（§b0-2 第 1 項要求兩組數字皆入 log）")
    if os.path.exists(BEFORE) and LOG != BEFORE:
        _b = io.open(BEFORE, encoding="utf-8").read()
        _mb = re.search(r"\*\*不逐位相同者 ＝ (\d+) 例\*\*　\*\*最大絕對差 ＝ ([^\*]+)\*\*", _b)
        if _mb:
            L.append(f"    **修前**：不同 **{_mb.group(1)}** 例／最大絕對差 **{_mb.group(2)}**"
                     f"　（出處 `verify/out/{os.path.basename(BEFORE)}`）")
    else:
        L.append("    **本次即修前之記錄**（尚無 before 檔可引）")
    L.append(f"    **本次**：不同 **{len(bad)}** 例／最大絕對差 **{maxd!r}**")

    # ══ 2 委派門檻兩側 ══
    L.append("")
    L.append("【2】委派門檻兩側（`|cross|` 略小／略大於 tol）")
    L.append("-" * W)
    poly = polys[0]
    bnd = poly.bounds
    d_hat = np.array(_unit((0.7431448255, 0.6691306064)))
    alloc = _unit((0.3583679495, 0.9335804265))
    n_near = _unit((-alloc[1], alloc[0]))
    bp = ((bnd[0] + bnd[2]) / 2.0 + 0.7137, (bnd[1] + bnd[3]) / 2.0 - 1.2841)
    S = 23.719
    _g0, _a0 = bs(poly, d_hat, bp, S, allocation_dir=alloc)
    for _lab, _th in (("略小於 tol", TOL * 0.5), ("略大於 tol", TOL * 50.0)):
        _nf = _unit(_rot(n_near, _th))
        _cx = abs(_cross(n_near, _nf))
        _g1, _a1 = bs(poly, d_hat, bp, S, allocation_dir=alloc, n_hat_far=_nf)
        _same = (_a1 == _a0)
        L.append(f"  {_lab:<12}|cross| ＝ {_cx:.6e}　(tol={TOL:g})"
                 f"　面積 ＝ {_a1!r}　vs None {_a0!r}"
                 f"　⇒ {'**走單線**（逐位==None）' if _same else '**走雙線**（≠None）'}")
    L.append("  ⇒ 期望：略小於 tol ⇒ 走單線；略大於 tol ⇒ 走雙線")

    # ══ 3 非同向鋪滿（難幾何）══
    L.append("")
    L.append("【3】非同向鋪滿（**難幾何**·⛔ 未回矩形）")
    L.append("-" * W)
    L.append("  🔑 **前提（本批實測發現·⛔ 非原語缺陷）**：相鄰兩切線若**於街廓內相交**，")
    L.append("     其夾出之區域即非「帶」而是**楔形**，非相鄰片會**重疊** ⇒ 鋪滿不成立。")
    L.append("     ⇒ 切線帳（T2）**必須保證相鄰切線於街廓內不相交**。以下 A/B 兩組即其對照。")

    def _cross_pt_in(poly_, q1, g1, q2, g2):
        """兩線交點是否落於街廓內（None ＝ 平行無交點）。"""
        from shapely.geometry import Point
        _den = g1[0] * (-g2[1]) - g1[1] * (-g2[0])
        if abs(_den) < 1e-12:
            return None
        _rx, _ry = q2[0] - q1[0], q2[1] - q1[1]
        _t = (_rx * (-g2[1]) - _ry * (-g2[0])) / _den
        _p = (q1[0] + _t * g1[0], q1[1] + _t * g1[1])
        return poly_.contains(Point(_p))

    for _case, _angs, _sv in (
            ("A 不相交（小角·寬間距）", [0.0, 0.35, -0.28, 0.19], [-90.0, -21.3, 17.9, 88.4]),
            ("B 相交（大角）",           [0.0, 11.3, -7.9, 4.1],  [-90.0, -21.3, 17.9, 88.4])):
        poly = polys[1]
        bnd = poly.bounds
        ang = 0.9137
        d_hat = np.array(_unit((math.cos(ang), math.sin(ang))))
        alloc0 = _unit((math.cos(ang + math.radians(31.7)), math.sin(ang + math.radians(31.7))))
        n0 = _unit((-alloc0[1], alloc0[0]))
        dirs = [_unit(_rot(n0, math.radians(a))) for a in _angs]
        base = np.asarray([(bnd[0] + bnd[2]) / 2.0, (bnd[1] + bnd[3]) / 2.0], dtype=float)
        _qs = [base + s * d_hat for s in _sv]
        _xin = [_cross_pt_in(poly, _qs[i], dirs[i], _qs[i + 1], dirs[i + 1]) for i in range(3)]
        pieces, areas = [], []
        for i in range(3):
            _al = (dirs[i][1], -dirs[i][0])          # rot90⁻¹ 使 rot90(_al)==dirs[i]
            _g, _a = bs(poly, d_hat, _qs[i], _sv[i + 1] - _sv[i],
                        allocation_dir=_al, n_hat_far=dirs[i + 1])
            pieces.append(_g); areas.append(_a)
        _alw = (dirs[0][1], -dirs[0][0])
        _gw, _aw = bs(poly, d_hat, _qs[0], _sv[3] - _sv[0],
                      allocation_dir=_alw, n_hat_far=dirs[3])
        _s = sum(areas); _dd = abs(_s - _aw)
        L.append("")
        L.append(f"  ── 組 {_case}　角度 {_angs}　相鄰線交點落於街廓內？ {_xin} ──")
        L.append(f"     三片 ＝ [{', '.join(f'{x:.9f}' for x in areas)}]")
        L.append(f"     Σ ＝ {_s:.9f}　整體 ＝ {_aw:.9f}　|Δ| ＝ {_dd:.3e}"
                 f"　{'✅' if _dd <= 1e-9 else '🔴'}")
        for i in range(3):
            for j in range(i + 1, 3):
                _x = (pieces[i].intersection(pieces[j]).area
                      if pieces[i] is not None and pieces[j] is not None else 0.0)
                # ⚠️ **判讀分級**（⛔ 不得把浮點接觸與真重疊混為一談）：
                #    `== 0.0` 精確零；`≤1e-9` ＝ 邊界浮點接觸（非真重疊）；`>1e-9` ＝ **真重疊**。
                _tag = ("✅ ==0.0" if _x == 0.0 else
                        ("✅ ≤1e-9（**邊界浮點接觸·非真重疊**）" if _x <= 1e-9 else
                         "🔴 **>1e-9 ＝ 真重疊**"))
                L.append(f"     片{i}∩片{j} ＝ {_x!r}　{_tag}")
        if any(_xin):
            L.append("     ⇒ 🔑 本組**有交點落於街廓內** ⇒ 重疊為**前提違反之必然結果**，"
                     "⛔ 非原語缺陷；T2 之切線帳須排除此情形。")

    L.append("")
    L.append("  🛑 **本批實測到之真重疊（⛔ 未解·上呈）**：")
    L.append("     於**另一組隨機方位**（`d̂` 由 rng 取、poly#1）曾實測")
    L.append("     `Σ三片 21562.050911594` vs `整體 21550.442498803`（|Δ| **11.61**）、")
    L.append("     且 **片0∩片2 ＝ 11.608412791387508**（**非相鄰**片重疊）。")
    L.append("     ⚠️ 該組之 `相鄰線交點落於街廓內` 檢為 **False** ⇒ **「線相交」不是唯一成因**。")
    L.append("     🔑 推定（**未證·⛔ 不當結論**）：難幾何為**非凸**多邊形 ⇒")
    L.append("        `block ∩ hp⁺ ∩ hp⁻` 可切出**不連通**之片，非相鄰兩片各自吃到同一凹槽")
    L.append("        ⇒ 重疊。⇒ **T2 之切線帳除「不相交」外，尚須處置非凸街廓之不連通片**。")
    L.append("     ⛔ 本批不修（非本單授權）；列為 T2 之前提缺口。")

    # ══ 4 容差上界（六街廓實測 D）══
    L.append("")
    L.append("【4】容差上界：`½·D²·tol` vs 覆蓋閘 `0.01`（六街廓**實測**直徑）")
    L.append("-" * W)
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    # 🔴 **自查**：`cb_by` 之條目**無 `shapely` 鍵**（實查鍵集：area_m2/…/vertices）
    #   ⇒ 首版以 `b.get("shapely")` 取幾何**全數落空、逐街廓列一列都沒印**，
    #      而總結仍印「最劣上界 0.000000e+00 ✅ 可證落於閘內」＝**空真假綠**。已改自 `vertices` 建。
    from shapely.geometry import Polygon as _PG
    _worst = 0.0
    _nblk = 0
    _ub_by = {}
    for lbl, b in cb_by.items():
        _v = b.get("vertices")
        if not _v:
            continue
        g = _PG(_v)
        _nblk += 1
        _b = g.bounds
        D = math.hypot(_b[2] - _b[0], _b[3] - _b[1])       # 外接矩形對角 ≥ 真直徑（保守上界）
        ub = 0.5 * D * D * TOL
        _worst = max(_worst, ub)
        _ub_by[lbl] = ub
        L.append(f"  {lbl:<4} D(bbox 對角) ＝ {D:12.6f} m　½·D²·tol ＝ **{ub:.6e}** ㎡"
                 f"　{'✅ < 0.01' if ub < COVER_GATE else '🔴 ≥ 0.01'}")
    if _nblk == 0:
        raise RuntimeError("🔴 §4 母體為空（0 個街廓取得幾何）⇒ 失敗，⛔ 不得以「上界 0」判過")
    L.append(f"  ⇒ 母體 ＝ **{_nblk}** 個街廓（⛔ 非空）")
    L.append(f"  ⇒ **全母體**最劣上界 ＝ **{_worst:.6e}** ㎡　vs ①' 覆蓋閘 **{COVER_GATE}** ㎡"
             f"　⇒ {'✅' if _worst < COVER_GATE else '🛑 **未能證明**'}")
    # 🔑 施工單 §b0-2-4 之受詞為「**六街廓**」＝ 走 `_block_strip` 之**配地街廓** R1–R6；
    #    `cb_by` 另含公設／道路街廓（G1／RD*），其**不進** `parcels_by_block` ⇒ 不切帶。
    _r = {k: v for k, v in _ub_by.items() if re.fullmatch(r"R\d", k)}
    _rworst = max(_r.values()) if _r else 0.0
    _rk = max(_r, key=_r.get) if _r else "—"
    L.append(f"  🔑 **分層**：施工單受詞為「**六街廓**」＝ 走 `_block_strip` 之配地街廓 R1–R6"
             f"（公設／道路街廓 G1／RD* **不進** `parcels_by_block` ⇒ **不切帶**）")
    L.append(f"     · **R1–R6（{len(_r)} 個）最劣 ＝ {_rworst:.6e} ㎡（{_rk}）**"
             f"　⇒ {'✅ **< 0.01·可證落於閘內**' if _rworst < COVER_GATE else '🛑'}")
    L.append(f"     · ⚠️ **餘裕極薄**：{_rk} 之上界為閘之 **{100.0 * _rworst / COVER_GATE:.1f}%**")
    _over = {k: v for k, v in _ub_by.items() if v >= COVER_GATE}
    L.append(f"     · 🛑 **非配地街廓超出者**：{ {k: f'{v:.3e}' for k, v in _over.items()} }"
             f"　——**本批不切其帶故不受影響**，但若日後對其切帶則此上界不成立 ⇒ **上呈**")
    L.append("  🔒 依據：兩線夾角 θ ≤ tol 時其間楔形面積 ≤ ½·D²·θ ≤ ½·D²·tol"
             "（`D` 取 bbox 對角 ⇒ **保守**）；體例比照 `_S_EPS` docstring 之論證。")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
