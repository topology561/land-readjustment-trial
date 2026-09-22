# -*- coding: utf-8 -*-
"""發單側（窗二十四）：GB-174 呈文附圖（原宗切片之平面圖）。輸入 = probe_gb174_geom.py 之出艙。"""
import json, sys
from shapely.geometry import Polygon, box
d = json.load(open(sys.argv[1], encoding="utf-8"))
OUT = sys.argv[2]
P = {p["暫編地號"]: Polygon(p["polygon_coords"]) for p in d["parcels"]}
B = {k: Polygon(v["geo"]["vertices"]) for k, v in d["blocks"].items()}
RED, BLUE, GRAY = "#c62828", "#1565c0", "#9e9e9e"
DROP = {"628-42(1)": "8.34", "628-27(1)": "51.32", "628-53(2)": "2.78"}
KEEP = {"628-42(2)": "153.46", "628-27(2)": "46.68", "628-53(1)": "0.44"}
NUM = {"628-42(1)": ("1", (0, 0)), "628-42(2)": ("2", (0, 0)), "628-27(1)": ("3", (0, 0)), "628-27(2)": ("4", (0, 0)),
       "628-53(2)": ("5", (0, 0)), "628-53(1)": ("6", (14, 12))}
NOTE = {"628-27(1)": "不配地（僅 0 m；3.5 m 照常分配）", "628-42(1)": "不配地（0 m、3.5 m 皆然）",
        "628-53(2)": "不配地（0 m、3.5 m 皆然）"}
BLK = {p["暫編地號"]: p["所屬街廓"] for p in d["parcels"]}
W = 760
panels = [
    ("甲　原地號 628-42、628-27（街廓 R2 與 R3 相接處）", box(310380, 2651857, 310426, 2651899), 10),
    ("乙　原地號 628-53（街廓 R5 與 R6 相接處）", box(310459.5, 2651814.5, 310470.5, 2651823.0), 2),
]
out = []
Y0 = 70
PW, PH = 340, 330
def path(poly, tf):
    if poly.is_empty:
        return ""
    geoms = [poly] if poly.geom_type == "Polygon" else [g for g in getattr(poly, "geoms", []) if g.geom_type == "Polygon"]
    s = ""
    for g in geoms:
        pts = [tf(x, y) for x, y in g.exterior.coords]
        s += "M" + " L".join("%.1f,%.1f" % p for p in pts) + " Z "
    return s
for i, (title, win, bar) in enumerate(panels):
    LBL = []
    ox = 20 + i * (PW + 40)
    minx, miny, maxx, maxy = win.bounds
    sc = min(PW / (maxx - minx), PH / (maxy - miny))
    tf = lambda x, y, ox=ox, minx=minx, maxy=maxy, sc=sc: (ox + (x - minx) * sc, Y0 + 30 + (maxy - y) * sc)
    out.append('<text x="%d" y="%d" font-size="13" font-weight="bold">%s</text>' % (ox, Y0 + 18, title))
    out.append('<rect x="%d" y="%d" width="%.1f" height="%.1f" fill="none" stroke="#bbb"/>' % (ox, Y0 + 30, (maxx - minx) * sc, (maxy - miny) * sc))
    for k, g in B.items():
        c = g.intersection(win)
        if c.is_empty:
            continue
        cat = d["blocks"][k]["category"] or ""
        isb = (cat == "住宅區")
        fill = "#f5f5f5" if isb else ("#e9f1e3" if "公園" in cat else "#e4e4e4")
        out.append('<path d="%s" fill="%s" stroke="#555" stroke-width="1.2"/>' % (path(c, tf), fill))
        LBL.append((k, cat, c, isb))
    # 分配線（相鄰二住宅街廓之共同邊）
    for a_, b_ in (("R2", "R3"), ("R5", "R6")):
        sh = B[a_].boundary.intersection(B[b_].boundary).intersection(win)
        if not sh.is_empty and sh.length > 0:
            for ln in (sh.geoms if hasattr(sh, "geoms") else [sh]):
                if ln.geom_type != "LineString":
                    continue
                pts = [tf(x, y) for x, y in ln.coords]
                out.append('<polyline points="%s" fill="none" stroke="#222" stroke-width="2.4" stroke-dasharray="7,4"/>' % " ".join("%.1f,%.1f" % q for q in pts))
    for pid, g in P.items():
        c = g.intersection(win)
        if c.is_empty or (pid not in DROP and pid not in KEEP):
            continue
        col = RED if pid in DROP else BLUE
        out.append('<path d="%s" fill="%s" fill-opacity="0.55" stroke="%s" stroke-width="1.5"/>' % (path(c, tf), col, col))
    # 街廓名（畫在切片之後，避免被蓋）
    for k, cat, c, isb in LBL:
        lp = c.representative_point(); x, y = tf(lp.x, lp.y)
        name = k if isb else "%s（%s）" % (k, cat)
        out.append('<text x="%.1f" y="%.1f" font-size="12" fill="#666" text-anchor="middle">%s</text>' % (x, y, name))
    # 編號圈 ＋ 圖下清單
    ly = Y0 + 30 + (maxy - miny) * sc + 52
    for pid in NUM:
        g = P[pid]
        if g.intersection(win).is_empty:
            continue
        n, off = NUM[pid]
        col = RED if pid in DROP else BLUE
        cx, cy = tf(g.centroid.x, g.centroid.y); cx += off[0]; cy += off[1]
        out.append('<circle cx="%.1f" cy="%.1f" r="9" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (cx, cy, col))
        out.append('<text x="%.1f" y="%.1f" font-size="11" font-weight="bold" fill="%s" text-anchor="middle">%s</text>' % (cx, cy + 4, col, n))
        txt = "%s　%s　街廓 %s　原有 %s ㎡　%s" % (n, pid, BLK[pid], DROP.get(pid) or KEEP.get(pid), NOTE.get(pid, "不配地" if pid in DROP else "照常分配"))
        out.append('<text x="%d" y="%.1f" font-size="11.5" fill="%s" font-weight="bold">%s</text>' % (ox, ly, col, txt))
        ly += 18
    # 比例尺
    bx, by = ox + 10, Y0 + 30 + (maxy - miny) * sc + 22
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="2"/>' % (bx, by, bx + bar * sc, by))
    out.append('<text x="%.1f" y="%.1f" font-size="11">%d 公尺</text>' % (bx + bar * sc + 6, by + 4, bar))
H = Y0 + 30 + PH + 175
head = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Noto Sans CJK TC, Microsoft JhengHei, sans-serif">' % (W, H, W, H),
        '<rect width="100%" height="100%" fill="#fff"/>',
        '<text x="20" y="28" font-size="16" font-weight="bold">附圖　三筆不配地之地，皆為同一筆原地號被新街廓界線切開之一半</text>',
        '<text x="20" y="50" font-size="12" fill="#444">重劃前原宗之切片；灰線＝重劃後街廓界線，黑虛線＝兩住宅街廓背對背之分配線。紅＝因位置太窄而不配地；藍＝同一地主照常分配。</text>']
foot = ['<text x="20" y="%d" font-size="11.5" fill="#444">原有面積：程式計算所用之值（628-42(2) 取畫面輸出「歸戶負擔計算表」之 153.46 ㎡）。兩圖比例尺不同。</text>' % (H - 40),
        '<text x="20" y="%d" font-size="11.5" fill="#444">628-42、628-53 另有落入道路、公園之部分（屬共同負擔），與本問無關，未著色。街廓 R5 與 R6 僅於一點相接。</text>' % (H - 20),
        '</svg>']
open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(head + out + foot) + "\n")
print("ok")
