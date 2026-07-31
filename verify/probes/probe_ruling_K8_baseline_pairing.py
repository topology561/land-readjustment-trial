# -*- coding: utf-8 -*-
r"""W-G.5 K-8 段一 — **BASELINE ↔ 街廓 配對之驗證**（＋N-19′ 平均深度對照靶）。

## ⚠️ 本檔驗證的是**既有機制**，不是新機制

配對規則 ＝ **KL 2026-07-26 第二批裁定 C-1／C-2／C-3／C-5**
（`grep -n "C-4：\`baselines_matched_count\`" app.py` 一帶；失敗考古 #38）。
其判準為**三個結構條件**——(a) 近平行、(b) 位於屁股側、(c) 深度域內——
**垂距僅為其後之收斂鍵，非距離判準**。

> 🔴 **本檔曾差點被用來取代該機制**（claude.ai 2026-07-31 撤銷）：
> CC 一度以「共線重疊長 ≈ 實體全長」之結構判準改寫配對碼。該判準在本案**碰巧**
> 給出相同答案，但**會在「一條 BASELINE 橫跨兩並排街廓」時雙雙給出 0.50 ⇒ 假紅**。
> ⇒ 重疊比**保留為診斷欄、不得升為選取閘**；`app.py` 之配對碼**不動**。

## 斷言（既有規則之輸出·**禁寫死單一實體編號**）

| 街廓 | 期望 |
|---|---|
| R1 | **`#0` 或 `#2` 任一** |
| R2 | `#3` |
| R3 | `#3` |
| R4 | **`#0` 或 `#2` 任一** |
| R5 | `#1` |
| R6 | `#1` |

R1／R4 允許二選一之理由：`#0` 與 `#2` 實測為**同一條無限直線之兩段**
（夾角 0.00000°、端點離線 0.00000m、端對端間隔 8.03m），**C-5 已走無條件等價路徑**
（垂距差 5.169e-07／5.795e-06）。寫死單一編號即製造假紅。

## 🔒 K-8 不變式（本檔一併看守）

**BASELINE 一律以「無限直線」參與量測與範圍構造，不得以線段端點截斷。**
理由：`#0`／`#2` 為同一直線之兩段 ⇒ 若以線段為準，R1／R4 之實體選擇會產生**假差異**；
以無限直線為準則其平均深度**嚴格相同**。本檔之 N-19′ 對照即以無限直線算。

## N-19′ 街廓平均深度（KL 裁 2026-07-31）

自前緣線上任一點作**垂直 BASELINE** 之直線交 BASELINE 於一點，兩點距離為該點深度；
沿前緣線取平均。前緣線與 BASELINE 皆直線 ⇒ 垂距沿弦**線性**
⇒ 平均 ＝ **中點垂距** ＝ **兩端垂距之平均**（**解析式·禁取樣**）。

### 對照靶＝**全精度**（K-8 段二 施工單 §六·取代舊 3dp 靶）·基準容差 `1e-6`

🔒 **R1／R4 走等價類判準**：K-8 §一 判 `#0`／`#2` **等價**且**禁寫死單一實體編號**；
二段角度有 µ 度級差 ⇒ N-19′ 亦有等價類散布（**實測 R1 5.16e-07／R4 5.80e-06**，
與 §一 所載垂距差 5.169e-07／5.795e-06 同量級）。**R4 之散布 > 1e-6**
⇒ 若硬比單值，C-5 之 tie-break 一換段即假紅——等於把「禁寫死單一實體」之禁令
從**配對層**漏到**數值層**。故該二塊判「落在等價類任一成員之 1e-6 內」。
附記：施工單 §六 之 R1 靶（33.1460885310）算在 `#2` 線，碼之 C-5 選中 `#0`
（33.1460880149）——二者**同屬等價類**，非歧異。

## 重跑
    python verify/probes/probe_ruling_K8_baseline_pairing.py     # rc=0 綠／1 紅

⚠️ **零注入·唯讀**。輸出 `verify/out/probe_ruling_K8_baseline_pairing.log`。

## 🔗 三檔職能分工（K-8 段二 §八·免下一手誤以為新的取代舊的）

| 檔 | 看守什麼 |
|---|---|
| `verify/fixture_baseline_candidates.py` | **候選分支邏輯**（哪些線進候選、C-5 三分支怎麼走、R1 共線 golden） |
| `verify/probes/probe_ruling_K8_baseline_pairing.py` | **配對輸出**（集合斷言）＋ **N-19′ 全精度解析靶** |
| `verify/fixture_block_depth_n19p.py` | **app 取值函式**（2dp 鏈／診斷欄 A・B／缺件 raise／`region_min`） |

**三者互為補集、無一取代另一。**
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

LOG = os.path.join(VERIFY, "out", "probe_ruling_K8_baseline_pairing.log")

# 既有 C-2/C-5 配對之期望輸出（**集合**·R1/R4 二選一·見 docstring）
PAIR_EXPECT = {"R1": {0, 2}, "R2": {3}, "R3": {3}, "R4": {0, 2}, "R5": {1}, "R6": {1}}
# N-19′ 對照靶（claude.ai 自 DXF 獨立算出·**全精度**·K-8 段二 施工單 §六 取代舊 3dp 靶）
N19P_EXPECT = {"R1": 33.1460885310, "R2": 44.4678768610, "R3": 44.3350248667,
               "R4": 33.1046288875, "R5": 45.7071870059, "R6": 45.5093305253}
# 基準容差（施工單 §六）：解析式、無取樣 ⇒ 不應有 1e-4 量級殘差。
N19P_TOL = 1e-6
# 🔒 **等價類加寬**（機制依據·非實測殘差）：K-8 §一 判 `#0`／`#2` 為**同一無限直線之兩段**、
#   **等價**且**禁寫死單一實體編號**。二段之角度有 µ 度級差 ⇒ 由其導出之 N-19′ 亦有一個
#   **等價類散布**。實測散布 R1 5.16e-07／R4 5.80e-06（與 K-8 §一 所載垂距差
#   5.169e-07／5.795e-06 同量級）⇒ **R4 之散布 > 基準容差**。
#   若仍用 1e-6 硬比，等於把「禁寫死單一實體」之禁令從**配對層**漏到**數值層**：
#   C-5 之決定性 tie-break（垂距→handle）一旦換段即假紅。
#   故 R1/R4 之判準改為「**落在等價類任一成員之 N19P_TOL 內**」（現算·不硬編散布值）。
N19P_EQUIV_BLOCKS = ("R1", "R4")


def _bl_entities():
    """DXF 內 BASELINE 圖層之線段（依讀取序編號 `#i`·與 `app` 之候選集同源）。"""
    import ezdxf
    doc = ezdxf.readfile(rv.V6DXF)
    out = []
    for e in doc.modelspace():
        if "BASELINE" not in str(e.dxf.layer).upper().replace("_", ""):
            continue
        if e.dxftype() == "LINE":
            out.append((np.array([e.dxf.start.x, e.dxf.start.y]),
                        np.array([e.dxf.end.x, e.dxf.end.y]), str(e.dxf.handle)))
        elif e.dxftype() == "LWPOLYLINE":
            pts = [np.array(p[:2], float) for p in e.get_points()]
            for i in range(len(pts) - 1):
                out.append((pts[i], pts[i + 1], str(e.dxf.handle)))
    return out


def _overlap_ratio(a, b, verts, tol):
    """**診斷欄**：實體 `a-b` 與街廓邊界之共線重疊長 ÷ 實體全長。
    ⛔ **不得升為選取閘**——一條 BASELINE 橫跨兩並排街廓時雙雙 0.50 ⇒ 假紅。"""
    u = b - a
    L = float(np.linalg.norm(u))
    if L < 1e-9:
        return 0.0
    u = u / L
    n = np.array([-u[1], u[0]])
    iv = []
    m = len(verts)
    for i in range(m):
        p = np.asarray(verts[i][:2], float)
        q = np.asarray(verts[(i + 1) % m][:2], float)
        if abs(float(np.dot(p - a, n))) > tol or abs(float(np.dot(q - a, n))) > tol:
            continue
        s1 = float(np.dot(p - a, u)); s2 = float(np.dot(q - a, u))
        lo, hi = max(min(s1, s2), 0.0), min(max(s1, s2), L)
        if hi > lo:
            iv.append((lo, hi))
    iv.sort()
    tot, ce = 0.0, -1e18
    for lo, hi in iv:
        if lo > ce:
            tot += hi - lo; ce = hi
        elif hi > ce:
            tot += hi - ce; ce = hi
    return tot / L


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    L, bad = [], []
    snap = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fs = harvest()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    fls = cad.get("front_lines") or {}
    bls = cad.get("baselines") or {}
    with open(rv.V6DXF, "rb") as f:
        q = ns["_detect_dxf_quantum"](f.read())
    ents = _bl_entities()

    L.append("=" * 112)
    L.append("【K-8 段一】BASELINE↔街廓 配對之**驗證**（既有 C-1/C-2/C-3/C-5·非新機制）")
    L.append("=" * 112)
    L.append(f"  DXF 量化步長 q = {q}｜BASELINE 線段數 = {len(ents)}")
    for i, (a, b, h) in enumerate(ents):
        L.append(f"    #{i} handle={h} len={float(np.linalg.norm(b - a)):.4f}")

    # ── 【1】配對輸出對拍（**集合**斷言）─────────────────────────────────────────
    L.append("")
    L.append("【1】既有配對之輸出（`cad['baselines']`）vs 期望集合")
    L.append("-" * 112)
    _h2i = {}
    for i, (_a, _b, h) in enumerate(ents):
        _h2i.setdefault(h, i)
    L.append(f"  {'街廓':6}{'配到之 point':>26}{'angle°':>11}  期望  判")
    for blk in sorted(PAIR_EXPECT):
        bv = bls.get(blk)
        if not bv:
            L.append(f"  {blk:6}  🔴 缺 BASELINE")
            bad.append(f"{blk} 缺 BASELINE")
            continue
        # 由 point 落在哪一段之無限直線上反查實體（**允許同線多段**）
        _pt = np.asarray(bv["point"], float)[:2]
        _th = math.radians(float(bv["angle_deg"]))
        _u = np.array([math.cos(_th), math.sin(_th)])
        _n = np.array([-_u[1], _u[0]])
        _hit = {i for i, (a, b, _h) in enumerate(ents)
                if abs(float(np.dot(a - _pt, _n))) <= 10 * q
                and abs(float(np.dot(b - _pt, _n))) <= 10 * q}
        _ok = bool(_hit & PAIR_EXPECT[blk])
        L.append(f"  {blk:6}({_pt[0]:11.3f},{_pt[1]:11.3f}){float(bv['angle_deg']):11.4f}"
                 f"  {sorted(PAIR_EXPECT[blk])}  {'✅' if _ok else '🔴 實得 ' + str(sorted(_hit))}")
        if not _ok:
            bad.append(f"{blk} 配對 {sorted(_hit)} ∉ 期望 {sorted(PAIR_EXPECT[blk])}")
    _mc = cad.get("baselines_matched_count")
    _miss = sorted(set(fls) - set(bls))
    L.append(f"  ⇒ matched_count = {_mc}（期 6）｜缺件集合 = {_miss or '∅'}（期 ∅）"
             f"  {'✅' if (_mc == 6 and not _miss) else '🔴'}")
    if _mc != 6 or _miss:
        bad.append(f"matched_count={_mc}／缺件={_miss}")

    # ── 【2】重疊比（**診斷欄·非閘**）───────────────────────────────────────────
    L.append("")
    L.append("【2】共線重疊長 ÷ 實體全長（**診斷欄·不得升為選取閘**·見 docstring）")
    L.append("-" * 112)
    L.append(f"  {'街廓':6}" + "".join(f"{'#' + str(i):>10}" for i in range(len(ents))))
    for blk in sorted(PAIR_EXPECT):
        v = cb_by[blk]["vertices"]
        L.append(f"  {blk:6}" + "".join(
            f"{_overlap_ratio(a, b, v, 10 * q):10.4f}" for a, b, _h in ents))
    L.append("  ⚠️ 0.50 者＝該實體橫跨兩並排街廓之一半——**正是此欄不可作閘之理由**。")

    # ── 【3】N-19′ 平均深度（K-8 不變式：BASELINE 取無限直線）───────────────────
    L.append("")
    L.append("【3】N-19′ 街廓平均深度（垂直 BASELINE·**無限直線**·解析式·禁取樣）")
    L.append("-" * 112)
    L.append(f"  {'街廓':6}{'p1垂距':>11}{'p2垂距':>11}{'N-19′':>14}{'對照靶(全精度)':>16}{'Δ':>11}  判")
    for blk in sorted(N19P_EXPECT):
        fl = fls.get(blk) or {}
        bv = bls.get(blk)
        if not (fl.get("p1") and fl.get("p2") and bv):
            bad.append(f"{blk} 缺 FRONT_LINE／BASELINE ⇒ N-19′ 不可量")
            L.append(f"  {blk:6}  🔴 缺件")
            continue
        p1 = np.asarray(fl["p1"], float)[:2]
        p2 = np.asarray(fl["p2"], float)[:2]
        bp = np.asarray(bv["point"], float)[:2]
        th = math.radians(float(bv["angle_deg"]))
        bu = np.array([math.cos(th), math.sin(th)])
        bn = np.array([-bu[1], bu[0]])            # 「垂直 BASELINE」之量測軸
        d1 = abs(float(np.dot(p1 - bp, bn)))
        d2 = abs(float(np.dot(p2 - bp, bn)))
        avg = (d1 + d2) / 2.0
        dv = avg - N19P_EXPECT[blk]
        _ok = abs(dv) <= N19P_TOL
        _how = ""
        if not _ok and blk in N19P_EQUIV_BLOCKS:
            # 等價類：以 `{#0,#2}` 各自之無限直線重算 N-19′，取最接近靶者
            _alt = []
            for _i in sorted(PAIR_EXPECT[blk]):
                _a, _b, _h = ents[_i]
                _uu = (_b - _a) / float(np.linalg.norm(_b - _a))
                _nn = np.array([-_uu[1], _uu[0]])
                _alt.append((abs(float(np.dot(p1 - _a, _nn)))
                             + abs(float(np.dot(p2 - _a, _nn)))) / 2.0)
            _spread = (max(_alt) - min(_alt)) if len(_alt) > 1 else 0.0
            if any(abs(avg - _v) <= N19P_TOL for _v in _alt) and                any(abs(N19P_EXPECT[blk] - _v) <= N19P_TOL for _v in _alt):
                _ok = True
                _how = f"（等價類內·散布 {_spread:.2e}）"
        L.append(f"  {blk:6}{d1:11.4f}{d2:11.4f}{avg:14.7f}{N19P_EXPECT[blk]:16.7f}"
                 f"{dv:+11.2e}  {'✅' if _ok else '🔴'}{_how}")
        if not _ok:
            bad.append(f"{blk} N-19′={avg:.10f} ≠ 靶 {N19P_EXPECT[blk]}（Δ={dv:+.3e}·容差 {N19P_TOL}）")

    L.append("")
    L.append("-" * 112)
    if bad:
        L.append(f"RESULT: FAIL（{len(bad)} 違例）")
        for x in bad[:20]:
            L.append("  " + x)
    else:
        L.append("RESULT: PASS（既有配對正確＋N-19′ 對照靶逐格相符）")
    L.append("=" * 112)
    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
