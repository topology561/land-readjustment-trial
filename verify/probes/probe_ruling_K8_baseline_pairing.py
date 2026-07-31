# -*- coding: utf-8 -*-
"""W-G.5 K-8 段一 — **BASELINE ↔ 街廓 配對之驗證**（＋N-19′ 平均深度對照靶）。

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

## 重跑
    python verify/probes/probe_ruling_K8_baseline_pairing.py     # rc=0 綠／1 紅

⚠️ **零注入·唯讀**。輸出 `verify/out/probe_ruling_K8_baseline_pairing.log`。
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
# N-19′ 對照靶（claude.ai 自 DXF 獨立算出·CC 逐格重現·小數三位）
N19P_EXPECT = {"R1": 33.146, "R2": 44.468, "R3": 44.335,
               "R4": 33.105, "R5": 45.707, "R6": 45.509}


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
    L.append(f"  {'街廓':6}{'p1垂距':>11}{'p2垂距':>11}{'N-19′':>11}{'對照靶':>11}{'Δ':>11}  判")
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
        _ok = abs(dv) <= 5e-4
        L.append(f"  {blk:6}{d1:11.3f}{d2:11.3f}{avg:11.3f}{N19P_EXPECT[blk]:11.3f}"
                 f"{dv:+11.4f}  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"{blk} N-19′={avg:.4f} ≠ 靶 {N19P_EXPECT[blk]}（Δ={dv:+.4f}）")

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
