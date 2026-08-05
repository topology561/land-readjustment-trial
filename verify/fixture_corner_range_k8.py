# -*- coding: utf-8 -*-
"""K-8 §三〜§五 夾具 — 街角規定範圍新構造之**兩項零成本自檢** ＋ **判別力反例**。

受測符號：`app._build_corner_range_v3`
（`grep -n "def _build_corner_range_v3" app.py`）。

## 裁定（KL 2026-07-31·canonical·全文見 `docs/rulings/K-6_街角地分配程序與可分配判準.md`）

- **§三 最小寬度帶**：前緣線沿 BASELINE 法向往 BASELINE 方向平移 `round(D_avg,2)`，
  二線所夾之帶。**純量測工具**：不截斷實體、不參與面積、不定義任何宗地邊界。
- **§四 ALLOC_LINE 定位**：平行 ALLOC_LINE 之直線，起始通過「前緣線 ∩ **截角前**側街境界線」
  交點，往街廓內側平行滑動，直到**帶內**二側界間、**平行前緣線**之距離**最小值**
  ＝ 退縮寬 ＋ 畸零地最小寬。
- **§五 範圍**：前緣線、**截角後**側界、上開 ALLOC_LINE、**BASELINE** 所圍多邊形；面積扣截角。

## 期望值出處（`fixture-provenance`：禁由新碼現跑回填）

| 格 | 期望值來源 |
|---|---|
| T1 | **法定附表**：`setback + get_min_lot_size(分區, 正面路寬)['min_width']`
      （花蓮縣畸零地使用規則 §3① 附表）——**非**由受測函式回填 |
| T2 | **結構性不等式**（0m 門檻嚴格小於 3.5m 門檻）·無魔術數字 |
| T3 | **停機語意**（施工單 §6-1）：滑動至街廓另一側仍達不到最小寬度 ⇒ raise·禁兜底 |
| T4 | **缺件語意**（no-silent-fallback）：缺 SIDE_LINE／BASELINE／FRONT_LINE、
      ALLOC∥FRONT ⇒ 一律 loud raise |

⚠️ **本夾具刻意不放「新面積」硬錨**——那將是「由新碼現跑一次把輸出回填當期望值」
（套套邏輯禁令）。八街角新舊面積之逐一對照屬**報告**之事，見
`docs/reports/W-G.5_K8-段三_commitB_街角規定範圍新構造.md`。

## T1 之量測係**第三份獨立實作**

`_build_corner_range_v3` 內已有 ①（閉式回代）與 ①′（shapely 求交）兩道自檢。
本格於**夾具側**以 numpy 再算一次（第三份），以免「受測者自己說自己對」。

## 重跑
    python verify/fixture_corner_range_k8.py        # rc=0 綠／rc=1 紅
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import numpy as np                                    # noqa: E402
from app_harvest import harvest                       # noqa: E402
import run_verification as rv                         # noqa: E402

SETBACKS = (0.0, 3.5)


def _range_min_depth(cad, cb_by, lbl, which, t_line_pts):
    """夾具側**獨立**量得該街角規定範圍**自身**之最小深度 `D(t*)`（K-9-6-b 之帶深）。

    🔴 **K-6-A2 段三(c)-2 §二 新增**：T1 原以 `snap["blocks"][lbl]["街廓分配深度_m"]`
      （＝**街廓平均深度**）為帶深，量的是 **K-9-7 接生產前之舊定義**之帶。
      **K-9-6-b 明訂**帶深為「該範圍**自身**之最小深度」
      （`grep -n "^#### K-9-6-b " docs/rulings/K-6_街角地分配程序與可分配判準.md`）。

    **定義（段四(c)-1 後）**：`D(t*)` ＝ 範圍臨街段（`PQ` ∩ 側界 → `P_block`）
    各點至 **BASELINE** 垂距之 **min**；垂距沿 `PQ` **線性** ⇒ min 必落兩端之一（⛔ 不取樣）。
    ⚠️ 改前為「前緣線 ∩ 側界 → 前緣線 ∩ ALLOC 邊」，即自 **FRONT_LINE** 起算（已作廢·見下）。

    🔒 **獨立性護欄（claude.ai 明令）**：本函式**只吃 `cad` 幾何與範圍多邊形之 ALLOC 邊**
      （`t_line_pts`·＝受測函式之**輸出幾何**），
      ⛔ **不自 `k97_solve_alloc_t` 或 `_build_corner_range_v3` 之回傳取任何值**
      ——否則本檔 §「T1 之量測係第三份獨立實作」當場消滅、T1 退化為恆真閘。

    🔴 **K-6-A2 段四(c)-1 已改（GB-28 解除）**：起算線由 **FRONT_LINE** 改為 **K-9-8 之 `PQ`**
      （K-9-6-b-1 明訂量測用之「道路境界線」＝ K-9-8 (3) 之延伸線段，深度自該線段起算）。
      `PQ` ＝ 過 **`P_block`**、平行前緣線之直線；`P_block` ＝ **`L_in` ∩ BLOCK 邊界**之**臨街側**者
      （K-9-8 (2)）。臨街段之二端遂為 **`P_block`**（本就在 `L_in` 上）與 **`PQ` ∩ SIDE_LINE**。
      ⚠️ 本案多數格 `P_block` 落 FRONT 重疊段 ⇒ **`PQ` 與 FRONT_LINE 共線**、與改前同值
      （K-9-8 (6) 之退化）；**`R4/right` 兩情境**落截角邊（內縮 `0.013039`）⇒ 該二格會變。
      ⛔ 但**不得**以此當回歸靶——見段四(b) 報告之 3mm 餘裕警語（換 `V6_1` 後該實例消失）。

    🔒 **獨立性護欄仍守**：新增之 `cb_by` 只用來取**街廓多邊形頂點**（`vertices`），
      `P_block` 由**本檔自行以 numpy 求線段∩無限直線**，
      ⛔ **仍不自 `k97_solve_alloc_t`／`_build_corner_range_v3`／`k98_virtual_measure_block`
      取任何回傳值**——否則 T1 退化為恆真閘。
      ⚠️ 刻意**不 import shapely**：本檔之獨立性正來自「numpy 閉式解、不共用 GEOS」。
    """
    fl = cad["front_lines"][lbl]
    F1 = np.array(fl["p1"], float)[:2]
    F2 = np.array(fl["p2"], float)[:2]
    d = (F2 - F1) / np.linalg.norm(F2 - F1)
    mb = cad["baselines"][lbl]
    bp = np.array(mb["point"], float)[:2]
    th = math.radians(float(mb["angle_deg"]))
    bu = np.array([math.cos(th), math.sin(th)])
    bn = np.array([-bu[1], bu[0]])
    if (bp - F1) @ bn < 0:
        bn = -bn
    sd = cad["side_lines_by_side"][lbl][which]
    S1 = np.array(sd["p1"], float)[:2]
    S2 = np.array(sd["p2"], float)[:2]
    su = (S2 - S1) / np.linalg.norm(S2 - S1)
    L1 = np.array(t_line_pts[0], float)
    L2 = np.array(t_line_pts[1], float)
    lu = (L2 - L1) / np.linalg.norm(L2 - L1)

    # ── K-9-8 (2)：`P_block` ＝ `L_in`（過 L1、方向 lu 之**無限直線**）∩ **BLOCK 邊界** ──────
    #   取**臨街側**者＝至 BASELINE 垂距最大者。⛔ 不與街廓取「面」交集（K-9-8 紅線一）。
    _verts = (cb_by.get(lbl) or {}).get("vertices")
    if not _verts or len(_verts) < 3:
        return None
    _ln = np.array([-lu[1], lu[0]])                   # L_in 之法向
    _cands = []
    _ring = [np.array(v, float)[:2] for v in _verts]
    for _a, _b in zip(_ring, _ring[1:] + _ring[:1]):
        _v = _b - _a
        _nv = np.linalg.norm(_v)
        if _nv < 1e-12:
            continue                                   # 零長邊 ⇒ 濾（非靜默：見 docstring）
        _den = _v @ _ln
        if abs(_den) < 1e-12:
            continue                                   # 與 L_in 平行 ⇒ 無單點交
        _t = ((L1 - _a) @ _ln) / _den
        if -1e-9 <= _t <= 1.0 + 1e-9:                  # 交點須落在該**邊**上
            _cands.append(_a + _v * _t)
    if not _cands:
        return None
    P_block = max(_cands, key=lambda q: abs((bp - q) @ bn))

    # ── K-9-8 (3)(5)：`PQ` ＝ 過 `P_block` 平行前緣線；深度自 `PQ` 起算 ──────────────────
    #   臨街段二端 ＝ `P_block`（本就在 `L_in` 上）與 `PQ` ∩ SIDE_LINE。
    def _x_on_pq(P, U):
        """`PQ`（過 P_block、方向 d）與直線（過 P、方向 U）之交點。"""
        n = np.array([-U[1], U[0]])
        den = d @ n
        if abs(den) < 1e-12:
            return None
        return P_block + d * (((P - P_block) @ n) / den)

    Q0 = _x_on_pq(S1, su)                 # 街角：PQ ∩ 側界（皆無限直線）
    if Q0 is None:
        return None
    # ── 🆕 K-9-6-b-2（KL 裁 2026-08-05·乙式）：另回傳 `δ_P` ────────────────────────
    #   `δ_P` ＝ 使「`PQ` ＝ FRONT 沿 `bn` 平移 `δ_P`」成立之平移量
    #   ＝ `P_block − F1` 在**非正交**基底 `{d, bn}` 下之 `bn` 分量。
    #   以 FRONT 之單位法向 `n̂` 取分量：`(P_block−F1)·n̂ = δ_P·(bn·n̂)`。
    #   ⛔ **不是 `(P_block − F1) @ bn`**——後者 ＝ `δ_P + α·g`（`α` ＝ 沿 `d` 之座標、
    #     `g = d·bn`），本案實測最劣差 **4.12 m**（`R6/right 0m`）。
    #     逐格對照與三條旁證見 `docs/reports/W-G.5_K6-A2-段四c2a2_乙式八支推導.md` §二-3。
    #   🔒 **本值由本檔自 CAD 幾何算得**（`P_block` 亦然），
    #     ⛔ **不自 `k97_solve_alloc_t`／`_build_corner_range_v3` 取任何回傳值**
    #     ——否則夾具即由「第三份獨立實作」退化為引擎之複讀機。
    _nf = np.array([-d[1], d[0]])
    _h = bn @ _nf
    if abs(_h) < 1e-9:
        return None                        # bn ∥ d ⇒ δ_P 不可定義（缺件語意·由呼叫端判紅）
    _dlt = float(((P_block - F1) @ _nf) / _h)
    # 至 BASELINE 之垂距（bn 已定號指向 BASELINE）；垂距沿 PQ 線性 ⇒ 取兩端·⛔ 不取樣
    _D = float(min(abs((bp - Q0) @ bn), abs((bp - P_block) @ bn)))
    return _D, _dlt


def _band_min_width(cad, cb_by, lbl, which, depth, t_line_pts, delta_p=0.0):
    """夾具側**獨立**量測：帶內二側界間、平行前緣線之距離，取兩端之 min。

    第三份實作（numpy 閉式解聯立），與受測函式之 ① ①′ 皆不同路徑。
    `t_line_pts` ＝ 受測函式所回傳範圍多邊形之「ALLOC 邊」兩點——由**輸出幾何**反推，
    故本格量的是**成品**，不是重跑受測者的算式。

    🆕 **K-9-6-b-2（KL 裁 2026-08-05·乙式）**：帶之**兩條**邊界線皆自 `PQ` 起算
    ⇒ 帶 ＝ **`[delta_p, delta_p + depth]`**（`d` ＝ FRONT 沿 `bn` 之平移量）。
    `delta_p` 由 `_range_min_depth` **於本檔內**算得後傳入
    （⛔ 不自引擎取值·見該函式之獨立性護欄）。
    🗄️ **甲式（帶 ＝ `[0, depth]`）已作廢**；`delta_p=0.0` 之預設**僅供
    `verify/probes/probe_K9_7d_stageA.py` 重現甲式對照**，⛔ **生產判定一律顯式傳入**。
    """
    fl = cad["front_lines"][lbl]
    F1 = np.array(fl["p1"], float)[:2]
    F2 = np.array(fl["p2"], float)[:2]
    d = (F2 - F1) / np.linalg.norm(F2 - F1)
    mb = cad["baselines"][lbl]
    bp = np.array(mb["point"], float)[:2]
    th = math.radians(float(mb["angle_deg"]))
    bu = np.array([math.cos(th), math.sin(th)])
    bn = np.array([-bu[1], bu[0]])
    if (bp - F1) @ bn < 0:
        bn = -bn
    sd = cad["side_lines_by_side"][lbl][which]
    S1 = np.array(sd["p1"], float)[:2]
    S2 = np.array(sd["p2"], float)[:2]
    su = (S2 - S1) / np.linalg.norm(S2 - S1)
    L1, L2 = np.array(t_line_pts[0], float), np.array(t_line_pts[1], float)
    lu = (L2 - L1) / np.linalg.norm(L2 - L1)
    cen = np.array(cb_by[lbl]["centroid"], float)[:2]

    def _hit(P, U, Q):
        """深度線（過 Q、方向 d）與直線（過 P、方向 U）之交點沿 d 之座標。"""
        n = np.array([-U[1], U[0]])
        den = d @ n
        if abs(den) < 1e-12:
            return None
        return ((P - Q) @ n) / den + (Q - F1) @ d

    ws = []
    for dd in (float(delta_p), float(delta_p) + float(depth)):
        Q = F1 + dd * bn
        a = _hit(S1, su, Q)
        b = _hit(L1, lu, Q)
        if a is None or b is None:
            return None
        sg = 1.0 if ((cen - F1) @ d) > a else -1.0
        ws.append(sg * (b - a))
    return min(ws)


def _alloc_edge_of(poly, cad, lbl):
    """自範圍多邊形取「與 ALLOC 平行」之邊（＝ L(t*) 落在多邊形上的那一段）。"""
    au = np.array(cad["alloc_dir_by_block"][lbl], float)
    au = au / np.linalg.norm(au)
    cs = list(poly.exterior.coords)
    best, blen = None, -1.0
    for p, q in zip(cs[:-1], cs[1:]):
        v = np.array(q, float)[:2] - np.array(p, float)[:2]
        n = float(np.linalg.norm(v))
        if n < 1e-9:
            continue
        if abs(abs((v / n) @ au) - 1.0) < 1e-6 and n > blen:
            best, blen = (p[:2], q[:2]), n
    return best


def main():
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ok = True
    out = []
    ns, fs = harvest()
    snap = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    sides = cad.get("side_lines_by_side", {}) or {}
    corners = [(lbl, w) for lbl in rv.CORNER_BLOCKS for w in ("left", "right")
               if w in (sides.get(lbl) or {})]

    def _build(lbl, which, setback, **over):
        b = cb_by[lbl]
        mb = cad["baselines"][lbl]
        fl = cad["front_lines"][lbl]
        sd = cad["side_lines_by_side"][lbl][which]
        mw = float(ns["get_min_lot_size"](
            b["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
        kw = dict(
            block_vertices=b["vertices"], block_centroid=b["centroid"],
            front_pts=[fl["p1"], fl["p2"]],
            baseline_pts=ns["_baseline_pts_from_manual"](mb, b["vertices"]),
            side_line_pts=[sd["p1"], sd["p2"]],
            alloc_dir=cad["alloc_dir_by_block"][lbl],
            block_depth=float(snap["blocks"][lbl]["街廓分配深度_m"]),
            setback=setback, min_width=mw,
            chamfer_tri=ns["_make_chamfer_tri_wb"](b, which),
            dxf_quantum=(mb.get("_match") or {}).get("q_detected"),
            _label=lbl, _side=which)
        kw.update(over)
        return ns["_build_corner_range_v3"](**kw), kw["min_width"]

    # ── T1 構造自檢（夾具側第三份實作）──────────────────────────────────────────
    out.append("【T1】構造自檢：帶內最小寬 ＝ 退縮寬 ＋ 畸零地最小寬（靶＝法定附表值）")
    out.append("-" * 100)
    out.append(f"  {'街廓側':10}{'退縮':>6}{'靶T':>8}{'夾具獨立量測':>14}{'Δ':>12}  判")
    areas = {}
    for setback in SETBACKS:
        for lbl, which in corners:
            poly, mw = _build(lbl, which, setback)
            areas[(lbl, which, setback)] = float(poly.area)
            T = setback + mw
            edge = _alloc_edge_of(poly, cad, lbl)
            if edge is None:
                ok = False
                out.append(f"  {lbl+' '+which:10}{setback:6.1f}  🔴 範圍多邊形取不到 ALLOC 邊")
                continue
            # 🔴 K-6-A2 段三(c)-2 §二：帶深改用**該範圍自身之最小深度 `D(t*)`**
            #   （K-9-6-b），不再用街廓平均深度 `街廓分配深度_m`（＝已被取代之舊定義）。
            #   `D(t*)` 由 `_range_min_depth` **獨立**量得（只吃 cad 幾何＋範圍之 ALLOC 邊）。
            # 🆕 K-9-6-b-2（乙式）：同時取得 `δ_P`，帶 ＝ `[δ_P, δ_P + D(t*)]`。
            _rmd = _range_min_depth(cad, cb_by, lbl, which, edge)
            if _rmd is None:
                ok = False
                out.append(f"  {lbl+' '+which:10}{setback:6.1f}  🔴 D(t*) 不可量（前緣線與側界／ALLOC 無交點）")
                continue
            _Dt, _dP = _rmd
            w = _band_min_width(cad, cb_by, lbl, which, _Dt, edge, delta_p=_dP)
            eps = ns["_corner_range_eps"]((cad["baselines"][lbl].get("_match") or {}).get("q_detected"))
            good = (w is not None) and abs(w - T) <= eps
            ok &= good
            out.append(f"  {lbl+' '+which:10}{setback:6.1f}{T:8.2f}{w:14.6f}{w-T:+12.2e}"
                       f"  {'✅' if good else '🔴'}")

    # ── T2 單調性自檢 ───────────────────────────────────────────────────────────
    out.append("")
    out.append("【T2】單調性：同一街角 退縮 0m 之門檻 **嚴格小於** 3.5m 之門檻")
    out.append("-" * 100)
    out.append(f"  {'街廓側':10}{'0m 面積':>12}{'3.5m 面積':>12}  判")
    for lbl, which in corners:
        a0, a35 = areas[(lbl, which, 0.0)], areas[(lbl, which, 3.5)]
        good = a0 < a35
        ok &= good
        out.append(f"  {lbl+' '+which:10}{a0:12.4f}{a35:12.4f}  {'✅' if good else '🔴 非嚴格遞增'}")

    # ── T3 判別力：寬度需求大於街廓 ⇒ 停機（§6-1·禁兜底）────────────────────────
    out.append("")
    out.append("【T3】判別力反例：min_width 大於街廓可容納者 ⇒ **必須 loud raise**（§6-1）")
    out.append("-" * 100)
    for lbl, which in corners[:3]:
        try:
            _build(lbl, which, 0.0, min_width=1.0e4)
            ok = False
            out.append(f"  {lbl+' '+which:10}🔴 未 raise —— 閘無判別力（可能靜默兜底）")
        except RuntimeError as e:
            out.append(f"  {lbl+' '+which:10}✅ raise：{str(e).splitlines()[0][:78]}")

    # ── T4 缺件語意（no-silent-fallback）────────────────────────────────────────
    out.append("")
    out.append("【T4】缺件／退化 ⇒ **必須 loud raise**（no-silent-fallback）")
    out.append("-" * 100)
    _lbl, _wh = corners[0]
    for _what, _over in (
            ("缺 SIDE_LINE", {"side_line_pts": None}),
            ("缺 BASELINE", {"baseline_pts": None}),
            ("缺 FRONT_LINE", {"front_pts": None}),
            ("深度 ≤ 0", {"block_depth": 0.0}),
            ("退縮＋最小寬 ＝ 0", {"min_width": 0.0}),
            ("ALLOC ∥ FRONT（平行前緣線之距離不可定義）",
             {"alloc_dir": None})):
        try:
            _build(_lbl, _wh, 0.0, **_over)
            ok = False
            out.append(f"  🔴 {_what}：未 raise")
        except RuntimeError:
            out.append(f"  ✅ {_what}：loud raise")

    print("=" * 100)
    print("【K-8 §三〜§五 夾具】街角規定範圍新構造（最小寬度帶＋ALLOC_LINE 解析定位＋範圍多邊形）")
    print("=" * 100)
    for ln in out:
        print(ln)
    print("-" * 100)
    print(f"RESULT: {'PASS' if ok else 'FAIL'}")
    print("=" * 100)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
