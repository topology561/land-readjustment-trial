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


def _range_min_depth(cad, lbl, which, t_line_pts):
    """夾具側**獨立**量得該街角規定範圍**自身**之最小深度 `D(t*)`（K-9-6-b 之帶深）。

    🔴 **K-6-A2 段三(c)-2 §二 新增**：T1 原以 `snap["blocks"][lbl]["街廓分配深度_m"]`
      （＝**街廓平均深度**）為帶深，量的是 **K-9-7 接生產前之舊定義**之帶。
      **K-9-6-b 明訂**帶深為「該範圍**自身**之最小深度」
      （`grep -n "^#### K-9-6-b " docs/rulings/K-6_街角地分配程序與可分配判準.md`）。

    **定義**：`D(t*)` ＝ 範圍臨街段（街角 `Q0` → `ALLOC 邊 ∩ 前緣線` 之 `P_front`）
    各點至 **BASELINE** 垂距之 **min**；垂距沿前緣線**線性** ⇒ min 必落兩端之一。

    🔒 **獨立性護欄（claude.ai 明令）**：本函式**只吃 `cad` 幾何與範圍多邊形之 ALLOC 邊**
      （`t_line_pts`·＝受測函式之**輸出幾何**），
      ⛔ **不自 `k97_solve_alloc_t` 或 `_build_corner_range_v3` 之回傳取任何值**
      ——否則本檔 §「T1 之量測係第三份獨立實作」當場消滅、T1 退化為恆真閘。

    ⚠️ **段四須複查**：K-9-6-b-1 明訂量測用之「道路境界線」＝ **K-9-8 之 `PQ` 延伸線段**，
      深度自該線段起算。本案 `P` 多落 FRONT 重疊段而**退化為 FRONT_LINE**，
      故現行自 FRONT_LINE 起算可行；**K-9-8 落地後本函式之起算線須一併改**（登記見 GB-28）。
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

    def _x_on_front(P, U):
        """前緣線（過 F1、方向 d）與直線（過 P、方向 U）之交點。"""
        n = np.array([-U[1], U[0]])
        den = d @ n
        if abs(den) < 1e-12:
            return None
        return F1 + d * (((P - F1) @ n) / den)

    Q0 = _x_on_front(S1, su)              # 街角：前緣線 ∩ 側界（皆無限直線）
    Pf = _x_on_front(L1, lu)              # P_front：前緣線 ∩ ALLOC 邊
    if Q0 is None or Pf is None:
        return None
    # 至 BASELINE 之垂距（bn 已定號指向 BASELINE）
    return float(min(abs((bp - Q0) @ bn), abs((bp - Pf) @ bn)))


def _band_min_width(cad, cb_by, lbl, which, depth, t_line_pts):
    """夾具側**獨立**量測：帶內二側界間、平行前緣線之距離，取兩端之 min。

    第三份實作（numpy 閉式解聯立），與受測函式之 ① ①′ 皆不同路徑。
    `t_line_pts` ＝ 受測函式所回傳範圍多邊形之「ALLOC 邊」兩點——由**輸出幾何**反推，
    故本格量的是**成品**，不是重跑受測者的算式。
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
    for dd in (0.0, float(depth)):
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
            _Dt = _range_min_depth(cad, lbl, which, edge)
            if _Dt is None:
                ok = False
                out.append(f"  {lbl+' '+which:10}{setback:6.1f}  🔴 D(t*) 不可量（前緣線與側界／ALLOC 無交點）")
                continue
            w = _band_min_width(cad, cb_by, lbl, which, _Dt, edge)
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
