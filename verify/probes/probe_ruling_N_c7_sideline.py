# -*- coding: utf-8 -*-
"""W-G.5 C-7 — **SIDE_LINE／FRONT_LINE 歸屬現況實測**（只量不改·先測再決定是否上呈）。

## 為何（KL 裁 2026-07-26）

現行綁定：
- `FRONT_LINE`：中點距 <5m ＋ **first-hit break**，且候選池含道路。
- `SIDE_LINE`：端點與 `FRONTLINE` 端點重合 ≤0.5m ＋ **first-hit break**
  （`grep -n "端點重合容差" app.py`）——街角處端點聚集 ⇒ 一條側街線可能同時吻合兩塊
  ⇒ **由 dict 順序決勝**、有歸錯塊之實風險。

**域裁（KL·canonical）**：`FRONTLINE`／`SIDELINE` 之**對側必為道路(RD)**；
一條 FRONT/SIDE 線**只屬於一個可建築街廓**，**不存在 R-R 共用**
（`BASELINE` 則相反·屁股對屁股共用為合法·見 `cad-layer-semantics`）。

## 判準（**復用倉內既有經證實原語·禁自創第三種**）

`app.py:_anchor_chamfers_topology`（`grep -n "def _anchor_chamfers_topology" app.py`）
之 docstring 明載：「CAD 的 FRONT/SIDE 線畫到**未截角尖角**、比 BLOCK 邊長約一截角腿
⇒ **端點重合法一端合一端差、六塊全滅**。改共線：方位角 mod180 差 < ang_tol、
BLOCK 邊兩端到線垂距 < perp_tol、邊中點投影落線 span 內」。

本探針即以**同一判準**（`ang_tol=2.0°`／`perp_tol=1.0m`·與該函式預設同）
＋**真實 1-D 投影重疊長度**（非邊長）計算歸屬。

## 判定（KL 明令）

- 現行綁定與「共線重疊最大」**全部一致** ⇒ 現行結果**碰巧正確**，C-6 為**預防性**修正、
  仍屬丙案 scope（不動分配幾何）。
- **有不一致** ⇒ 街角地判定**現正出錯** ⇒ **立即停機上呈 KL**。

## 重跑
    WV_RULING_N_C7=1 python verify/probes/probe_ruling_N_c7_sideline.py

⚠️ **零注入·零引擎改動**。輸出 `verify/out/probe_ruling_N_c7_sideline.log`。
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import ezdxf                                                        # noqa: E402
from shapely.geometry import Polygon                                # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUT_LOG = os.path.join(VERIFY, "out", "probe_ruling_N_c7_sideline.log")
ANG_TOL = 2.0        # 與 `_anchor_chamfers_topology` 預設同
PERP_TOL = 1.0       # 同上


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_N_c7：{msg}（no-silent-fallback）")


def _az(a, b):
    return math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])) % 180.0


def _perp(pt, a, b):
    dx = b[0] - a[0]; dy = b[1] - a[1]
    L = math.hypot(dx, dy)
    if L < 1e-9:
        return math.hypot(pt[0] - a[0], pt[1] - a[1])
    return abs(dx * (pt[1] - a[1]) - dy * (pt[0] - a[0])) / L


def _tproj(pt, a, b):
    """`pt` 於線段 a→b 之**弧長**投影（公尺·非正規化）。"""
    dx = b[0] - a[0]; dy = b[1] - a[1]
    L = math.hypot(dx, dy)
    if L < 1e-9:
        return 0.0
    return ((pt[0] - a[0]) * dx + (pt[1] - a[1]) * dy) / L


def _overlap_len(edge, line_a, line_b):
    """BLOCK 邊 `edge` 與線 `line_a→line_b` 之**共線 1-D 投影重疊長**（不共線 → 0）。"""
    e1, e2 = edge
    if abs((_az(e1, e2) - _az(line_a, line_b) + 90.0) % 180.0 - 90.0) > ANG_TOL:
        return 0.0
    if _perp(e1, line_a, line_b) > PERP_TOL or _perp(e2, line_a, line_b) > PERP_TOL:
        return 0.0
    t1 = _tproj(e1, line_a, line_b); t2 = _tproj(e2, line_a, line_b)
    lo, hi = (t1, t2) if t1 <= t2 else (t2, t1)
    L = math.hypot(line_b[0] - line_a[0], line_b[1] - line_a[1])
    return max(0.0, min(hi, L) - max(lo, 0.0))


def _block_overlap(poly, line_a, line_b):
    """該街廓**所有邊**與線之重疊長總和（同一直邊可能由多段組成·故加總）。"""
    co = list(poly.exterior.coords)
    return sum(_overlap_len((co[i][:2], co[i + 1][:2]), line_a, line_b)
               for i in range(len(co) - 1))


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.environ.get("WV_RULING_N_C7") != "1":
        print("🔴 本探針須 WV_RULING_N_C7=1 明示啟用。")
        return 2
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    snapshot = rv.load_snapshot()   # 🆕 K-8 §三 A-2：現算 N-19′ 深度注入（檔案零修改）
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)

    # 可建築街廓（依域裁：候選池只含可建築者·排除 RD/公設）
    F3 = ns["F3_CATEGORY_BURDEN"]
    build_polys = {}
    for lbl, b in cb_by.items():
        if F3.get(b.get("category", ""), "") != "可建築土地":
            continue
        p = Polygon(b["vertices"])
        build_polys[lbl] = p if p.is_valid else p.buffer(0)
    road_polys = {}
    for lbl, b in cb_by.items():
        if lbl in build_polys:
            continue
        p = Polygon(b["vertices"])
        road_polys[lbl] = p if p.is_valid else p.buffer(0)

    # DXF 原始線層
    doc = ezdxf.readfile(rv.V6DXF)
    raw = {"SIDE_LINE": [], "FRONT_LINE": []}
    for e in doc.modelspace():
        ly = str(e.dxf.layer).upper()
        if ly not in raw:
            continue
        if e.dxftype() == "LINE":
            pts = [(float(e.dxf.start.x), float(e.dxf.start.y)),
                   (float(e.dxf.end.x), float(e.dxf.end.y))]
        elif e.dxftype() == "LWPOLYLINE":
            pts = [(float(p[0]), float(p[1])) for p in e.get_points()]
        else:
            continue
        if len(pts) < 2:
            continue
        raw[ly].append({"pts": pts, "handle": str(e.dxf.handle),
                        "len": math.hypot(pts[-1][0] - pts[0][0], pts[-1][1] - pts[0][1])})

    L = []
    L.append("=" * 122)
    L.append("【C-7】SIDE_LINE／FRONT_LINE 歸屬現況實測（現行綁定 vs 共線＋投影重疊最大）")
    L.append("  判準來源＝倉內既有經證實原語 `_anchor_chamfers_topology`"
             f"（ang_tol={ANG_TOL}°／perp_tol={PERP_TOL}m）·**未自創第三種**")
    L.append(f"  可建築街廓 {sorted(build_polys)}｜道路/公設 {sorted(road_polys)}"
             f"｜DXF：FRONT {len(raw['FRONT_LINE'])} 條、SIDE {len(raw['SIDE_LINE'])} 條")
    L.append("=" * 122)

    inconsistent = []

    # ── FRONT_LINE ──
    L.append("")
    L.append("【F】FRONT_LINE")
    L.append("-" * 122)
    L.append(f"  {'handle':>8}{'長度':>9}  {'現行綁定':<10}{'重疊最大':<10}{'重疊(m)':>10}"
             f"{'次者':<10}{'次重疊':>9}{'勝差':>9}  一致")
    cur_front = {}
    for lbl, fl in (cad.get("front_lines") or {}).items():
        cur_front[(round(fl["p1"][0], 2), round(fl["p1"][1], 2),
                   round(fl["p2"][0], 2), round(fl["p2"][1], 2))] = lbl
    for r in raw["FRONT_LINE"]:
        a, b = r["pts"][0], r["pts"][-1]
        key = (round(a[0], 2), round(a[1], 2), round(b[0], 2), round(b[1], 2))
        cur = cur_front.get(key, "—")
        ov = sorted(((lbl, _block_overlap(p, a, b)) for lbl, p in build_polys.items()),
                    key=lambda x: -x[1])
        w, w_ov = ov[0]
        s, s_ov = (ov[1] if len(ov) > 1 else ("—", 0.0))
        ok = (cur == w)
        if not ok:
            inconsistent.append(("FRONT", r["handle"], cur, w))
        L.append(f"  {r['handle']:>8}{r['len']:9.2f}  {cur:<10}{w:<10}{w_ov:10.2f}"
                 f"{s:<10}{s_ov:9.2f}{w_ov - s_ov:9.2f}  {'✅' if ok else '🔴'}")

    # ── SIDE_LINE ──
    L.append("")
    L.append("【S】SIDE_LINE（**本項為 C-7 之標的**）")
    L.append("-" * 122)
    L.append(f"  {'handle':>8}{'長度':>9}  {'現行綁定':<14}{'重疊最大':<10}{'重疊(m)':>10}"
             f"{'次者':<10}{'次重疊':>9}{'勝差':>9}  一致")
    cur_side = {}
    for lbl, d in (cad.get("side_lines_by_side") or {}).items():
        for side, v in (d or {}).items():
            cur_side[(round(v["p1"][0], 2), round(v["p1"][1], 2),
                      round(v["p2"][0], 2), round(v["p2"][1], 2))] = (lbl, side)
    for r in raw["SIDE_LINE"]:
        a, b = r["pts"][0], r["pts"][-1]
        key = (round(a[0], 2), round(a[1], 2), round(b[0], 2), round(b[1], 2))
        cur_lbl, cur_side_nm = cur_side.get(key, ("—", "—"))
        ov = sorted(((lbl, _block_overlap(p, a, b)) for lbl, p in build_polys.items()),
                    key=lambda x: -x[1])
        w, w_ov = ov[0]
        s, s_ov = (ov[1] if len(ov) > 1 else ("—", 0.0))
        ok = (cur_lbl == w)
        if not ok:
            inconsistent.append(("SIDE", r["handle"], f"{cur_lbl}·{cur_side_nm}", w))
        L.append(f"  {r['handle']:>8}{r['len']:9.2f}  {cur_lbl + '·' + cur_side_nm:<14}"
                 f"{w:<10}{w_ov:10.2f}{s:<10}{s_ov:9.2f}{w_ov - s_ov:9.2f}"
                 f"  {'✅' if ok else '🔴'}")

    # ── 域裁複驗：FRONT/SIDE 對側是否為道路 ──
    L.append("")
    L.append("【D】域裁複驗：一條 FRONT/SIDE 線是否**只屬於一個可建築街廓**（禁 R-R 共用）")
    L.append("-" * 122)
    _multi = []
    for ly in ("FRONT_LINE", "SIDE_LINE"):
        for r in raw[ly]:
            a, b = r["pts"][0], r["pts"][-1]
            owners = [lbl for lbl, p in build_polys.items()
                      if _block_overlap(p, a, b) > 1.0]
            if len(owners) > 1:
                _multi.append((ly, r["handle"], owners))
    if _multi:
        for ly, h, ow in _multi:
            L.append(f"  🔴 {ly} handle={h}：重疊 >1m 之可建築街廓有 {ow} ⇒ 與域裁相違")
    else:
        L.append("  ✅ 全部線層皆**恰一個**可建築街廓重疊 >1m ⇒ 與域裁一致（無 R-R 共用）")

    L.append("")
    L.append("=" * 122)
    if inconsistent:
        L.append(f"🔴🔴 **不一致 {len(inconsistent)} 條** ⇒ 街角地判定**現正出錯** ⇒ **停機上呈 KL**")
        for t, h, cur, w in inconsistent:
            L.append(f"    {t} handle={h}：現行 {cur} ／ 共線重疊最大 {w}")
    else:
        L.append("✅ **現行綁定與共線重疊最大 逐條一致** ⇒ 現行結果**碰巧正確**")
        L.append("   ⇒ C-6 為**預防性**修正、仍屬丙案 scope（不動分配幾何）·**不需驚動 KL**")
    L.append("=" * 122)
    out = "\n".join(L)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write(out + "\n")
    print(out)
    print(f"\n📄 {OUT_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
