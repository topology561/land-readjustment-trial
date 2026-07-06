# -*- coding: utf-8 -*-
"""
W-D.3 §4 碎片幾何 — 潔淨複驗（KL 2026-07-06 evidence-line 要求，git 錨定）。

背景：本 session CC 環境曾兩度出現注入/幻覺 stdout（假 commit、未落地的 Q5 depth-t）。
KL 裁定：凡進 §4 規格之幾何必須 **git 錨定**（committed 腳本 → committed CSV → 讀回 →
潔淨新狀態複現一致），不接受只存在於某次 stdout 的數字。本檔即該潔淨複驗器。

產出（committed CSV，供 KL pull 判）：
  verify/out/wd3_fragment_geom.csv   ← 每抵費地片：面積/沿街s/長寬比/緊湊度（複驗附錄A）
  verify/out/wd3_fragment_edges.csv  ← Q5 逐邊：每片邊界對 FRONT/SIDE(路) vs BASELINE/BLOCK(非路)
                                        分類 → 臨路/不臨路 裁決

確定性：管線無隨機（harvest→固定 DXF/xlsx→shapely 幾何）；representative_point /
minimum_rotated_rectangle 對定多邊形確定 → 兩次潔淨執行應 byte-identical（run_twice 驗）。

用法：
  python verify/wd3_fragment_geom.py            # 算＋寫 CSV＋對附錄A自檢，exit 0=一致
  python verify/wd3_fragment_geom.py --readback # 純從 committed CSV 讀回印出（不重算）
"""
import os
import sys
import csv

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import json
from shapely.geometry import Polygon, LineString, Point
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
from stepg_pipeline import run_step_g

OUT_GEOM = os.path.join(HERE, "out", "wd3_fragment_geom.csv")
OUT_EDGES = os.path.join(HERE, "out", "wd3_fragment_edges.csv")

# c1584a8 附錄A 宣稱值（三 <100㎡ 碎片；潔淨複驗須逐項吻合才平反）
CLAIMED = {
    ("0m", "R1-抵費地-2"): {"面積": 5.30, "沿街s": 0.02, "長寬比": 91.8, "緊湊度": 0.02},
    ("0m", "R3-抵費地-2"): {"面積": 78.19, "沿街s": 0.99, "長寬比": 12.2, "緊湊度": 0.13},
    ("0m", "R6-抵費地-2"): {"面積": 85.66, "沿街s": 0.01, "長寬比": 13.3, "緊湊度": 0.11},
    ("3.5m", "R6-抵費地-2"): {"面積": 85.66, "沿街s": 0.01, "長寬比": 13.3, "緊湊度": 0.11},
}
PERP_TOL = 0.10   # 邊落於某 CAD 線之垂距容差（m；cad-layer skill：≥1cm，0.05-0.1 實用）


def _seg_line(d):
    p1, p2 = d.get("p1"), d.get("p2")
    if p1 and p2:
        try:
            return LineString([tuple(p1), tuple(p2)])
        except Exception:
            return None
    return None


def _edge_on_segment(a, b, seg):
    """邊(a,b) 是否落於線段 seg（兩端垂距 < PERP_TOL 且投影落 seg span 內）。"""
    if seg is None:
        return False
    L = seg.length
    if L <= 0:
        return False
    pa, pb = Point(a), Point(b)
    if pa.distance(seg) > PERP_TOL or pb.distance(seg) > PERP_TOL:
        return False
    ta, tb = seg.project(pa), seg.project(pb)
    return (min(ta, tb) > -PERP_TOL) and (max(ta, tb) < L + PERP_TOL)


def compute():
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    raw = open(rv.V6DXF, "rb").read()
    temp, build, _sw = build_build_parcels(ns, fake_st, raw, list(cb_by.values()))
    flm = cad.get("front_lines", {}) or {}
    slm = cad.get("side_lines_by_side", {}) or {}

    geom_rows, edge_rows = [], []
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _pk = run_corner_pk(ns, fake_st, list(cb_by.values()), cad,
                            params, temp, build, setback)
        winners, forced = _pk[3], _pk[4]
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build, winners, forced, setback)
        for r in sg["g_rows"]:
            if r.get("推進側別") != "抵費地":
                continue
            lbl = r["所屬街廓"]
            cs = r.get("cut_coords") or []
            if len(cs) < 3:
                continue
            frag = Polygon(cs)
            if not frag.is_valid:
                frag = frag.buffer(0)
            if frag.is_empty:
                continue
            area = frag.area
            cen = frag.representative_point()
            # 沿街 s（投影 FRONT_LINE）
            fl = flm.get(lbl) or {}
            fseg = _seg_line(fl)
            s_rel = (fseg.project(Point(cen.x, cen.y)) / fseg.length
                     if (fseg is not None and fseg.length > 0) else None)
            # 長寬比（最小外接矩形）＋緊湊度
            mrr = frag.minimum_rotated_rectangle
            mc = list(mrr.exterior.coords)
            e1 = Point(mc[0]).distance(Point(mc[1]))
            e2 = Point(mc[1]).distance(Point(mc[2]))
            longs, shorts = max(e1, e2), (min(e1, e2) or 1e-9)
            aspect = longs / shorts
            compact = (4 * 3.14159265 * area / (frag.length ** 2)) if frag.length > 0 else 0.0
            geom_rows.append({
                "情境": tag, "暫編地號": r["暫編地號"], "街廓": lbl,
                "面積": round(area, 2),
                "沿街s": (round(s_rel, 2) if s_rel is not None else ""),
                "長寬比": round(aspect, 1), "緊湊度": round(compact, 2),
            })
            # Q5 逐邊分類（對 FRONT/SIDE 道路 vs BASELINE/BLOCK 非路）
            sl = slm.get(lbl) or {}
            fseg_c = fseg
            sseg_l = _seg_line(sl.get("left") or {})
            sseg_r = _seg_line(sl.get("right") or {})
            blk = cb_by[lbl]
            bpoly = Polygon(blk["vertices"])
            if not bpoly.is_valid:
                bpoly = bpoly.buffer(0)
            coords = list(frag.exterior.coords)
            L_front = L_sideL = L_sideR = L_nonroad = L_internal = 0.0
            for i in range(len(coords) - 1):
                a, b = coords[i], coords[i + 1]
                elen = Point(a).distance(Point(b))
                if elen < 1e-6:
                    continue
                mid = Point((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
                on_block = mid.distance(bpoly.exterior) < PERP_TOL
                if not on_block:
                    L_internal += elen
                    continue
                if _edge_on_segment(a, b, fseg_c):
                    L_front += elen
                elif _edge_on_segment(a, b, sseg_l):
                    L_sideL += elen
                elif _edge_on_segment(a, b, sseg_r):
                    L_sideR += elen
                else:
                    L_nonroad += elen   # 街廓邊界但非 FRONT/SIDE → BASELINE屁股線/BLOCK分區界/截角
            road_len = L_front + L_sideL + L_sideR
            verdict = "臨路" if road_len > 0.5 else "不臨路"
            edge_rows.append({
                "情境": tag, "暫編地號": r["暫編地號"], "街廓": lbl,
                "面積": round(area, 2),
                "臨正街長": round(L_front, 2), "臨左側街長": round(L_sideL, 2),
                "臨右側街長": round(L_sideR, 2),
                "非路邊界長(屁股/分區/截角)": round(L_nonroad, 2),
                "內部切長": round(L_internal, 2),
                "裁決": verdict,
            })
    return geom_rows, edge_rows


def _write(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def _readback():
    print("== 讀回 committed CSV ==")
    for path in (OUT_GEOM, OUT_EDGES):
        print(f"-- {os.path.relpath(path, HERE)}")
        with open(path, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                print("  " + " | ".join(f"{k}={v}" for k, v in row.items()))


def main():
    if "--readback" in sys.argv:
        _readback()
        return 0
    geom_rows, edge_rows = compute()
    _write(OUT_GEOM, geom_rows)
    _write(OUT_EDGES, edge_rows)
    # 自檢：從 committed CSV 讀回，對 c1584a8 附錄A 宣稱值逐項比對
    back = {(r["情境"], r["暫編地號"]): r
            for r in csv.DictReader(open(OUT_GEOM, encoding="utf-8-sig"))}
    print("== 附錄A 潔淨複驗（讀回 committed CSV vs c1584a8 宣稱）==")
    allok = True
    for key, claim in CLAIMED.items():
        got = back.get(key)
        if got is None:
            print(f"  🔴 {key} 缺列"); allok = False; continue
        diffs = []
        for col, cv in claim.items():
            gv = float(got[col])
            tol = 0.05 if col in ("沿街s", "緊湊度") else (0.15 if col == "長寬比" else 0.01)
            if abs(gv - cv) > tol:
                diffs.append(f"{col}: 宣稱{cv} vs 複驗{gv}")
        print(f"  {'✅' if not diffs else '🔴'} {key[0]} {key[1]}: "
              + ("逐項吻合" if not diffs else "；".join(diffs)))
        allok = allok and not diffs
    print("== Q5 逐邊裁決 ==")
    for r in edge_rows:
        if r["面積"] < 100:
            print(f"  {r['情境']} {r['暫編地號']}({r['面積']}㎡): 臨正街{r['臨正街長']}/"
                  f"左側{r['臨左側街長']}/右側{r['臨右側街長']} 非路{r['非路邊界長(屁股/分區/截角)']}"
                  f" 內部{r['內部切長']} → {r['裁決']}")
    print("RESULT:", "APPENDIX-A 平反（一致）" if allok else "APPENDIX-A 不一致→重生")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
