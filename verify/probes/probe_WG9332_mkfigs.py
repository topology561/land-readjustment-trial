# -*- coding: utf-8 -*-
"""發單側窗二十七（唯讀·倉外·⛔ 零生產碼）：T2／T4／T7 呈 KL 附圖。輸入 = geomall.py 之出艙。"""
import json, sys
from decimal import Decimal, ROUND_HALF_UP
H2 = lambda v: str((Decimal(str(v)) / 2).quantize(Decimal("0.01"), ROUND_HALF_UP))
from shapely.geometry import Polygon, box
d = json.load(open(sys.argv[1], encoding="utf-8")); OUTD = sys.argv[2]
P = {p["暫編地號"]: Polygon(p["polygon_coords"]) for p in d["parcels"] if p.get("polygon_coords")}
B = {k: Polygon(v["geo"]["vertices"]) for k, v in d["blocks"].items()}
CAT = {k: v["scalars"].get("category") or "" for k, v in d["blocks"].items()}
FONT = "Noto Sans CJK TC, Microsoft JhengHei, sans-serif"
RED, BLUE, ORG, GRN = "#c62828", "#1565c0", "#e65100", "#2e7d32"
def path(g, tf):
    gs = [g] if g.geom_type == "Polygon" else [x for x in getattr(g, "geoms", []) if x.geom_type == "Polygon"]
    return "".join("M" + " L".join("%.1f,%.1f" % tf(x, y) for x, y in q.exterior.coords) + " Z " for q in gs)
def frame(win, ox, oy, pw, ph):
    minx, miny, maxx, maxy = win.bounds
    sc = min(pw / (maxx - minx), ph / (maxy - miny))
    return sc, (lambda x, y: (ox + (x - minx) * sc, oy + (maxy - y) * sc))
def blocks(out, win, tf, label=True, lab=None):
    for k, g in B.items():
        c = g.intersection(win)
        if c.is_empty: continue
        cat = CAT[k]; isb = cat == "住宅區"
        fill = "#f7f7f7" if isb else ("#e9f1e3" if "公園" in cat else "#e4e4e4")
        out.append('<path d="%s" fill="%s" stroke="#555" stroke-width="1.1"/>' % (path(c, tf), fill))
    if label:
        for k, g in B.items():
            c = g.intersection(win)
            if c.is_empty: continue
            p = c.representative_point(); x, y = tf(p.x, p.y)
            t = (lab or {}).get(k, k if CAT[k] == "住宅區" else "%s（%s）" % (k, CAT[k]))
            out.append('<text x="%.1f" y="%.1f" font-size="12" fill="#555" text-anchor="middle">%s</text>' % (x, y, t))
def svg(name, W, H, title, sub, body, foot):
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="%s">' % (W, H, W, H, FONT),
         '<rect width="100%" height="100%" fill="#fff"/>',
         '<text x="20" y="28" font-size="16" font-weight="bold">%s</text>' % title]
    for i, t in enumerate(sub): s.append('<text x="20" y="%d" font-size="12" fill="#444">%s</text>' % (50 + 17 * i, t))
    s += body
    for i, t in enumerate(foot): s.append('<text x="20" y="%d" font-size="11.5" fill="#444">%s</text>' % (H - 16 - 17 * (len(foot) - 1 - i), t))
    s.append("</svg>")
    open("%s/%s" % (OUTD, name), "w", encoding="utf-8", newline="\n").write("\n".join(s) + "\n")

# ---------- 附圖一（T7）----------
W1 = 800; body = []
panels = [("甲　原地號 628-27（R2 與 R3 背對背相接處）", box(310380, 2651857, 310426, 2651899), 10,
           [("628-27(1)", "R2", "51.32", "20.52", RED), ("628-27(2)", "R3", "46.68", "26.54", BLUE)],
           "依原有面積 → 併向 R2（51.32 ＞ 46.68）", "依應分配面積 → 併向 R3（26.54 ＞ 20.52）"),
          ("乙　原地號 628-53（R5 與 R6 相接處）", box(310459.5, 2651814.5, 310470.5, 2651823.0), 2,
           [("628-53(2)", "R5", "2.78", "0.00", RED), ("628-53(1)", "R6", "0.44", "0.26", BLUE)],
           "依原有面積 → 併向 R5（2.78 ＞ 0.44）", "依應分配面積 → 併向 R6（0.26 ＞ 0.00）")]
Y0 = 92; PW, PH = 355, 320
for i, (t, win, bar, sl, l1, l2) in enumerate(panels):
    ox = 20 + i * (PW + 50)
    sc, tf = frame(win, ox, Y0 + 26, PW, PH)
    body.append('<text x="%d" y="%d" font-size="13" font-weight="bold">%s</text>' % (ox, Y0 + 14, t))
    blocks(body, win, tf)
    for pid, blk, a, g, col in sl:
        c = P[pid].intersection(win)
        body.append('<path d="%s" fill="%s" fill-opacity="0.5" stroke="%s" stroke-width="1.5"/>' % (path(c, tf), col, col))
    minx, miny, maxx, maxy = win.bounds
    by = Y0 + 26 + (maxy - miny) * sc + 22
    body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="2"/>' % (ox + 8, by, ox + 8 + bar * sc, by))
    body.append('<text x="%.1f" y="%.1f" font-size="11">%d 公尺</text>' % (ox + 14 + bar * sc, by + 4, bar))
    ly = by + 28
    for pid, blk, a, g, col in sl:
        body.append('<text x="%d" y="%d" font-size="12" font-weight="bold" fill="%s">%s　位於 %s　原有 %s ㎡　應分配 %s ㎡</text>' % (ox, ly, col, pid, blk, a, g)); ly += 19
    body.append('<text x="%d" y="%d" font-size="12.5" font-weight="bold" fill="#222">○ %s</text>' % (ox, ly + 6, l1))
    body.append('<text x="%d" y="%d" font-size="12.5" font-weight="bold" fill="#222">● %s</text>' % (ox, ly + 26, l2))
svg("附圖一_T7_跨分配線之較大側.svg", W1, 640,
    "附圖一　同一筆原地號被分配線切開、一側未達時，「較大的一側」要比什麼？",
    ["紅＝未達（或不配地）之一側；藍＝另一側。灰線＝重劃後街廓界線。兩筆皆為二種比法結論相反之實例（退縮 0 m）。"],
    body, ["原有、應分配面積：倉內 GB-175 所載之實測（主線態 77e3ede·退縮 0 m）。兩圖比例尺不同。",
           "此一側即為後續合併試配之第一個目標街廓，並決定折算時以哪一街廓之地價為準。"])

# ---------- 附圖二（T2）----------
allw = box(*B["G1"].union(B["R1"]).union(B["R4"]).union(B["R5"]).union(B["R6"]).union(B["R2"]).union(B["R3"]).buffer(6).bounds)
body = []; sc, tf = frame(allw, 20, 128, 760, 470)
anc = P["628-24(1)"].centroid
blocks(body, allw, tf, lab={"RD4": ""})
_rp = B["RD4"].intersection(box(anc.x + 95, -1e9, 1e9, 1e9)).representative_point(); _x, _y = tf(_rp.x, _rp.y)
body.append('<text x="%.1f" y="%.1f" font-size="12" fill="#555" text-anchor="middle">RD4（道路）</text>' % (_x, _y))
G025 = [("628-53(1)", "R6　建築街廓", "0.44", RED), ("628-53(2)", "R5　建築街廓", "2.78", RED),
        ("628-24(1)", "G1　公園", "621.00", GRN), ("628-53(3)", "G1　公園", "300.44", GRN), ("628-53(4)", "RD4　道路", "229.34", ORG)]
for pid, w, a, col in G025:
    body.append('<path d="%s" fill="%s" fill-opacity="0.55" stroke="%s" stroke-width="1.6"/>' % (path(P[pid], tf), col, col))
anc = P["628-24(1)"].centroid; ax, ay = tf(anc.x, anc.y)
body.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#000"/>' % (ax, ay))
body.append('<text x="%.1f" y="%.1f" font-size="11.5" font-weight="bold">最大一筆 628-24(1)</text>' % (ax - 20, ay + 30))
for k in ("R3", "R5"):
    c = B[k].centroid; x, y = tf(c.x, c.y)
    body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="1.3" stroke-dasharray="5,4"/>' % (ax, ay, x, y))
    body.append('<text x="%.1f" y="%.1f" font-size="11" fill="#000">%.0f m</text>' % ((ax + x) / 2 + 4, (ay + y) / 2 - 4, c.distance(anc)))
for k in ("R5", "R6"):
    c = P["628-53(2)" if k == "R5" else "628-53(1)"].centroid; x, y = tf(c.x, c.y)
    body.append('<circle cx="%.1f" cy="%.1f" r="7" fill="none" stroke="%s" stroke-width="2"/>' % (x, y, RED))
ly = 128 + (allw.bounds[3] - allw.bounds[1]) * sc + 26
body.append('<text x="20" y="%.1f" font-size="12.5" font-weight="bold">同一地主（歸戶 G025）之五筆，合計 1,154.00 ㎡：</text>' % ly); ly += 20
for pid, w, a, col in G025:
    body.append('<text x="36" y="%.1f" font-size="12" fill="%s" font-weight="bold">%s　%s　%s ㎡</text>' % (ly, col, pid, w, a)); ly += 18
svg("附圖二_T2_兼有建地與公設地之地主.svg", 800, int(ly + 70),
    "附圖二　同一地主兼有建築街廓內土地與公設地、道路時，試配街廓之先後依何者？",
    ["紅（圈示）＝建築街廓內之切片（極小，合 3.22 ㎡）；綠＝公園；橘＝道路。黑點＝該戶面積最大之一筆。",
     "虛線＝至最近二街廓之距離（質心間·示意）。依距離：自最大一筆起最近者先（R3、R5、R2…）。",
     "依五級：比照建地，以使用分區、最小建築面積、正面道路、路寬、深度、距離之順序排。"],
    body, ["面積：倉內 K-9-45 所載。距離為街廓質心至 628-24(1) 質心之直線距離（發單側現算·僅示意）。",
           "舊程式之凍結結果（依距離·已由 K-9-45 廢止·新程式不再如此）：配於 R2 163.04 ㎡、R3 511.33 ㎡，建築街廓內 3.22 ㎡ 先領現金。",
           "依 K-9-45：五筆合併計算、一併調配，建築街廓內 3.22 ㎡ 不先領現金。"])

# ---------- 附圖三（T4）----------
MINA = {"R4": 115.88, "R1": 116.02, "R3": 155.19, "R2": 155.64, "R6": 159.28, "R5": 159.99}
PR = {"R1": 100, "R4": 100, "R3": 95, "R5": 95, "R2": 90, "R6": 90}
DEP = {k: d["blocks"][k]["scalars"]["mbr_short_m"] for k in MINA}
body = []; allw2 = box(*B["R1"].union(B["R4"]).union(B["R5"]).union(B["R6"]).union(B["R2"]).union(B["R3"]).buffer(6).bounds)
sc, tf = frame(allw2, 20, 100, 500, 440)
lab = {k: "" for k in B}
blocks(body, allw2, tf, lab=lab)
body.append('<path d="%s" fill="#fff3c4" stroke="#b58900" stroke-width="2"/>' % path(B["R4"], tf))
for k in MINA:
    p = B[k].representative_point(); x, y = tf(p.x, p.y)
    body.append('<text x="%.1f" y="%.1f" font-size="13" font-weight="bold" text-anchor="middle">%s</text>' % (x, y - 16, k))
    body.append('<text x="%.1f" y="%.1f" font-size="11" text-anchor="middle">深約 %.1f m·後地價 %d%%</text>' % (x, y, DEP[k], PR[k]))
    body.append('<text x="%.1f" y="%.1f" font-size="11" text-anchor="middle">最小分配 %.2f·半 %s</text>' % (x, y + 15, MINA[k], H2(MINA[k])))
# 右側：寬 3.5 m 之最小分配土地示意（依比例）
ox, oy, s2 = 590, 110, 6.0
for i, (k, col) in enumerate((("R4", "#b58900"), ("R2", "#555"))):
    x = ox + i * 90; h = DEP[k] * s2; w = 3.5 * s2
    body.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#fff" stroke="%s" stroke-width="1.6"/>' % (x, oy, w, h, col))
    body.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity="0.35" stroke="none"/>' % (x, oy + h / 2, w, h / 2, col))
    body.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="bold">%s</text>' % (x + w + 6, oy + 14, k))
    body.append('<text x="%.1f" y="%.1f" font-size="11">%.2f ㎡</text>' % (x + w + 6, oy + 30, MINA[k]))
    body.append('<text x="%.1f" y="%.1f" font-size="11">半 %s</text>' % (x + w + 6, oy + h / 2 + 14, H2(MINA[k])))
body.append('<text x="%d" y="%.1f" font-size="11" fill="#444">寬 3.5 m × 街廓深度（同比例）</text>' % (ox - 10, oy + DEP["R5"] * s2 + 24))
svg("附圖三_T4_二分之一之門檻.svg", 820, 640,
    "附圖三　「達二分之一」之門檻：全區一個數，抑或隨試配之街廓而變？",
    ["黃＝全區最淺、最小分配面積最小之街廓（R4）。各街廓標示深度、重劃後地價比率、最小分配面積及其半（㎡）。",
     "全區單一值 ⇒ 門檻恆為 57.94 ㎡；隨街廓而變 ⇒ 試配 R2 時門檻為 77.82 ㎡、試配 R5 時為 80.00 ㎡。"],
    body, ["最小分配面積：主線 338bd08 現算（寬 3.5 m × 該街廓平均深度）；R4 之值第三位小數之取法另案，不影響本問。",
           "深度為街廓最小外接矩形之短邊（示意）；後地價比率：倉內快照「後街廓_面積單價」。"])
print("ok")
