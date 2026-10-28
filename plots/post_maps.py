# -*- coding: utf-8 -*-
"""
W-P.005　重劃後三圖層（公告分配地籍線·分配後歸戶圖·重劃後地價圖）＋ 暫編→正式地號對照表
＋ 顏色對照表（重劃後）。

命令列：python plots/post_maps.py --state <配地結果_退縮*.json> --pre-dxf <重劃前圖.dxf>
          --moedict <dict-revised.json> --out <目錄> [--map <地號對照表.xlsx>]
  --state   ＝ plots/alloc_state.py 之輸出。
  --pre-dxf ＝ plots/prelim_maps.py 之「重劃前圖.dxf」（三圖層·W-P.001／002 定版）；本程式讀之、加三圖層、另存（⛔ 改原檔）。
  --map     ＝ 承辦人改過之地號對照表（本程式前次之輸出）；無 ⇒ 依 S 型自動編定之預設。
輸出（皆寫至 --out，⛔ 入倉）：公告圖_退縮<t>m.dxf（六圖層）、地號對照表_退縮<t>m.xlsx、顏色對照表_重劃後_退縮<t>m.xlsx。

所據：出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md（§一、§二）。
  KL 2026-10-28 23:31：問一 甲（程式依 S 型自動編定；全範圍同一地段；先排區〔東北先〕、再區內 S 型）；
  問四 乙（每宗註記地號、面積、分配寬度、深度）；問五 乙（抵費地自成一色並註「抵費地」；道路、公園不填色、
  只畫界線；原地主分得之地照一般歸戶上色）。KL 23:37：保留「暫編 → 正式地號對照表」（重號或缺號即停）。
缺值一律報錯停止（⛔ 靜默補值）。
"""
import argparse
import json
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （重劃前之歸戶、顏色、歸戶號·W-P.001／002）
import owner_index  # noqa: E402

LAYER_POST_CAD = "公告分配地籍線"
LAYER_POST_OWN = "分配後歸戶圖"
LAYER_POST_PRICE = "重劃後地價圖"
POST_LAYERS = (LAYER_POST_CAD, LAYER_POST_OWN, LAYER_POST_PRICE)
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_TEXT = "抵費地"
OFFSET_COLOR = (160, 160, 160)
LINE_GAP = 1.4                       # 多列註記之行距（× 字高）
REGION_TOL = 0.01                    # 區之相接之容差（公尺）
NO_RE = re.compile(r"^[1-9]\d{0,4}(-[1-9]\d*)?$")   # 母號（不超過五位數）或「母號-子號」（手冊第 3849〜3854 列）
MAP_SHEET = "地號對照表"
MAP_HEAD = ("暫編", "街廓", "類別", "配地之暫編地號", "預設地號（S 型）", "正式地號", "面積（㎡）")
MAP_NOTE = "「正式地號」得由承辦人改之（例：段界另有調整）；重號或空白者，本程式即停止產出（KL 2026-10-28 23:37）。"


def q2(x):
    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def f2(x):
    return f"{q2(x):.2f}"


# ---------------------------------------------------------------- 讀取
def load_state(path):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    for k in ("退縮_m", "街廓", "宗", "略"):
        if k not in doc:
            raise PM.SourceError(f"配地結果缺 {k}")
    if not doc["宗"]:
        raise PM.SourceError("配地結果無宗")
    return doc


def tag_of(doc):
    return f"{float(doc['退縮_m']):g}"


def post_prices():
    v = json.load(open(PM.CASE_PARAMS, encoding="utf-8"))["財務接線_v3"]
    if "後街廓_面積單價" not in v:
        raise PM.SourceError("case_params 之 財務接線_v3 缺 後街廓_面積單價")
    return {b: float(d["單價_元每m2"]) for b, d in v["後街廓_面積單價"].items()}


# ---------------------------------------------------------------- 宗之整理
def entries_of(doc):
    """⇒ 重劃後之各宗（分配地、抵費地、公設之區塊），各附暫編（街廓-序號；公設 ＝ 其編號）。"""
    from shapely.geometry import Polygon
    blocks = doc["街廓"]
    ents = []
    by_blk = {}
    for x in doc["宗"]:
        by_blk.setdefault(x["街廓"], []).append(x)
    for lbl in sorted(blocks):
        b = blocks[lbl]
        if "宗地分配線方向" not in b:
            continue
        lots = by_blk.get(lbl, [])
        if not lots:
            raise PM.SourceError(f"可分配之街廓 {lbl} 無宗")
        (x1, y1), (x2, y2) = b["正面臨路線"]
        L = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        ux, uy = (x2 - x1) / L, (y2 - y1) / L

        def t_of(x):
            p = Polygon(x["多邊形"]).representative_point()
            return (p.x - x1) * ux + (p.y - y1) * uy
        for i, x in enumerate(sorted(lots, key=t_of), start=1):
            e = dict(x)
            e["暫編"] = f"{lbl}-{i:02d}"
            ents.append(e)
    for lbl in sorted(blocks):
        b = blocks[lbl]
        if "宗地分配線方向" in b:
            continue
        if lbl in by_blk:
            raise PM.SourceError(f"非可分配之街廓 {lbl} 有配地之宗")
        ents.append({"暫編": lbl, "配地暫編": None, "街廓": lbl, "類別": b["分類"],
                     "面積": float(q2(Polygon(b["多邊形"]).area)), "多邊形": b["多邊形"]})
    return ents


def regions(blocks):
    """⇒ [[街廓…]]：重劃範圍之相連之各區（各街廓之多邊形外擴 REGION_TOL 後之相連者）。"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    polys = {k: Polygon(v["多邊形"]) for k, v in blocks.items()}
    u = unary_union([p.buffer(REGION_TOL) for p in polys.values()])
    parts = list(getattr(u, "geoms", [u]))
    out = []
    for part in parts:
        mem = sorted(k for k, p in polys.items() if part.contains(p.representative_point()))
        out.append((part, mem))
    if sorted(k for _, m in out for k in m) != sorted(polys):
        raise PM.SourceError("街廓之分區不全或重複")
    return out


def _ne_key(geom):
    c = geom.centroid
    return (-round(c.y, 3), -round(c.x, 3))


def s_order(doc, ents):
    """重劃後地號之預設編定（KL 23:31 問一 甲）⇒ [暫編]（依地號 1、2、3…之序）。
    區：依其形心先北後南（同者先東）；區內之可分配之街廓：依形心先北後南（同者先東），
    第 1、3、5…個街廓之宗自東而西、第 2、4、6…個自西而東（S 型）；正東西向之正面臨路線則以先北後南代東西。
    各區之宗編畢，公設之區塊（道路、公園）續編於後（依區之序，區內依形心先北後南、同者先東）。"""
    from shapely.geometry import Polygon
    blocks = doc["街廓"]
    by_blk = {}
    for e in ents:
        by_blk.setdefault(e["街廓"], []).append(e)
    regs = sorted(regions(blocks), key=lambda pm: _ne_key(pm[0]))
    order, publics = [], []
    for _part, mem in regs:
        alloc = [k for k in mem if "宗地分配線方向" in blocks[k]]
        pub = [k for k in mem if "宗地分配線方向" not in blocks[k]]
        alloc.sort(key=lambda k: _ne_key(Polygon(blocks[k]["多邊形"])))
        for i, k in enumerate(alloc):
            (x1, y1), (x2, y2) = blocks[k]["正面臨路線"]
            dx, dy = x2 - x1, y2 - y1
            L = (dx * dx + dy * dy) ** 0.5
            ux, uy = dx / L, dy / L
            west = (-ux > 1e-9) or (abs(ux) <= 1e-9 and uy < 0)
            if not west:
                ux, uy = -ux, -uy          # u 指向西（正東西向者指向南）
            if i % 2 == 1:
                ux, uy = -ux, -uy          # 第 2、4、6…個街廓：自西而東

            def t_of(e):
                p = Polygon(e["多邊形"]).representative_point()
                return p.x * ux + p.y * uy
            order.extend(e["暫編"] for e in sorted(by_blk[k], key=t_of))
        pub.sort(key=lambda k: _ne_key(Polygon(blocks[k]["多邊形"])))
        publics.extend(pub)
    order.extend(publics)
    if sorted(order) != sorted(e["暫編"] for e in ents):
        raise PM.SourceError("S 型之編定漏宗或重複")
    return order


# ---------------------------------------------------------------- 地號對照表
def default_numbers(order):
    return {t: str(i) for i, t in enumerate(order, start=1)}


def write_map(path, ents, order, numbers, default):
    import openpyxl
    from openpyxl.styles import Alignment
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = MAP_SHEET
    ws.append(list(MAP_HEAD))
    pos = {t: i for i, t in enumerate(order)}
    for e in sorted(ents, key=lambda e: pos[e["暫編"]]):
        ws.append([e["暫編"], e["街廓"], e["類別"], e.get("配地暫編"), default[e["暫編"]],
                   numbers[e["暫編"]], float(q2(e["面積"]))])
    ws.append([])
    ws.append([MAP_NOTE])
    for c in ws[1]:
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    wb.save(path)


def read_map(path, ents):
    """承辦人之對照表 ⇒ {暫編: 正式地號}。暫編之集合不符、正式地號空白、格式不合、重號 ⇒ SourceError（停止）。"""
    import openpyxl
    ws = openpyxl.load_workbook(path, data_only=True)[MAP_SHEET]
    rows = list(ws.iter_rows(values_only=True))
    if tuple(rows[0][:len(MAP_HEAD)]) != MAP_HEAD:
        raise PM.SourceError(f"對照表之表頭不符：{rows[0]}")
    want = {e["暫編"] for e in ents}
    got = {}
    for r in rows[1:]:
        t = r[0]
        if t is None or str(t).strip() == "" or str(t) == MAP_NOTE:
            continue
        t = str(t).strip()
        if t not in want:
            raise PM.SourceError(f"對照表之暫編 {t} 非本次配地之宗")
        if t in got:
            raise PM.SourceError(f"對照表之暫編 {t} 重複")
        v = r[5]
        if v is None or str(v).strip() == "":
            raise PM.SourceError(f"對照表之暫編 {t} 之正式地號空白（缺號）")
        s = str(int(v)) if isinstance(v, (int, float)) and float(v).is_integer() else str(v).strip()
        if not NO_RE.match(s):
            raise PM.SourceError(f"對照表之暫編 {t} 之正式地號 {v!r} 非整數之母號（或母號-子號）")
        got[t] = s
    miss = sorted(want - set(got))
    if miss:
        raise PM.SourceError(f"對照表缺暫編：{miss}")
    seen = {}
    for t, s in sorted(got.items()):
        if s in seen:
            raise PM.SourceError(f"正式地號 {s} 重號：{seen[s]}、{t}")
        seen[s] = t
    return got


# ---------------------------------------------------------------- 歸戶（照重劃前之歸戶號與顏色）
def owner_scheme(moedict, ents):
    strokes = owner_index.load_strokes(moedict)
    lots, owners, area = PM.load_cadastre()
    key_of, hh_order = PM.households(lots, owners)
    hh_color = dict(zip(hh_order, PM.distinct_palette(len(hh_order))))
    hh_lots, members = PM.household_members(owners, key_of)
    hh_no = owner_index.number_households(hh_lots, members, strokes, PM.landno_key)
    if OFFSET_COLOR in hh_color.values():
        raise PM.SourceError("抵費地之色與某戶之色同")
    g_of = {}
    for e in ents:
        if e["類別"] != KIND_LOT:
            continue
        ln = e["原地號"]
        if ln not in key_of:
            raise PM.SourceError(f"{e['暫編']} 之原地號 {ln} 不在重劃前之地籍")
        k = key_of[ln]
        if g_of.setdefault(e["歸戶"], k) != k:
            raise PM.SourceError(f"配地之歸戶 {e['歸戶']} 與重劃前之歸戶不一（{ln}）")
    if len(set(g_of.values())) != len(g_of):
        raise PM.SourceError("重劃前之一戶對應配地之數歸戶")
    return key_of, hh_color, hh_no


# ---------------------------------------------------------------- DXF
def _texts(msp, layer, lines, p):
    from ezdxf.enums import TextEntityAlignment
    n = len(lines)
    for i, s in enumerate(lines):
        y = p.y + ((n - 1) / 2 - i) * PM.TEXT_HEIGHT * LINE_GAP
        t = msp.add_text(s, height=PM.TEXT_HEIGHT, dxfattribs={"layer": layer, "style": PM.TEXT_STYLE})
        t.set_placement((p.x, y), align=TextEntityAlignment.MIDDLE_CENTER)


def cad_lines(e, no):
    if e["類別"] == KIND_LOT:
        w = q2(e["宗地寬度"])
        d = (Decimal(repr(float(e["面積"]))) / w).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return [no, f2(e["面積"]), f"寬{w:.2f}", f"深{d:.2f}"]
    return [no, f2(e["面積"])]


def write_dxf(pre_path, path, ents, numbers, key_of, hh_color, hh_no, price, price_color):
    import ezdxf
    from shapely.geometry import Polygon
    doc = ezdxf.readfile(pre_path)
    for name in PM.LAYERS:
        if name not in doc.layers:
            raise PM.SourceError(f"重劃前圖缺圖層 {name}")
    for name in POST_LAYERS:
        if name in doc.layers:
            raise PM.SourceError(f"重劃前圖已有圖層 {name}")
        doc.layers.add(name)
    msp = doc.modelspace()
    for e in sorted(ents, key=lambda e: e["暫編"]):
        coords = [(float(x), float(y)) for x, y in e["多邊形"]]
        if coords[0] == coords[-1]:
            coords = coords[:-1]
        rp = Polygon(coords).representative_point()
        no = numbers[e["暫編"]]
        msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": LAYER_POST_CAD})
        _texts(msp, LAYER_POST_CAD, cad_lines(e, no), rp)
        if e["類別"] in (KIND_LOT, KIND_OFFSET):
            h = msp.add_hatch(dxfattribs={"layer": LAYER_POST_OWN})
            if e["類別"] == KIND_LOT:
                k = key_of[e["原地號"]]
                h.set_solid_fill(rgb=hh_color[k])
                lab = str(hh_no[k])
            else:
                h.set_solid_fill(rgb=OFFSET_COLOR)
                lab = OFFSET_TEXT
            h.paths.add_polyline_path(coords, is_closed=True)
            _texts(msp, LAYER_POST_OWN, [lab], rp)
            v = price[e["街廓"]]
            h2 = msp.add_hatch(dxfattribs={"layer": LAYER_POST_PRICE})
            h2.set_solid_fill(rgb=price_color[v])
            h2.paths.add_polyline_path(coords, is_closed=True)
            _texts(msp, LAYER_POST_PRICE, [f2(v)], rp)
        else:
            msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": LAYER_POST_OWN})
    doc.saveas(path)


def write_color_table(path, ents, numbers, key_of, hh_color, hh_no, price, price_color):
    import openpyxl
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    ws = wb.create_sheet(LAYER_POST_OWN)
    ws.append(["圖層", "歸戶號", "顏色 R,G,B", "正式地號"])
    by_hh = {}
    for e in ents:
        if e["類別"] == KIND_LOT:
            by_hh.setdefault(key_of[e["原地號"]], []).append(numbers[e["暫編"]])
    for k in sorted(by_hh, key=lambda kk: hh_no[kk]):
        ws.append([LAYER_POST_OWN, hh_no[k], "{},{},{}".format(*hh_color[k]),
                   "、".join(sorted(by_hh[k], key=PM.landno_key))])
    offs = sorted((numbers[e["暫編"]] for e in ents if e["類別"] == KIND_OFFSET), key=PM.landno_key)
    if offs:
        ws.append([LAYER_POST_OWN, OFFSET_TEXT, "{},{},{}".format(*OFFSET_COLOR), "、".join(offs)])
    ws2 = wb.create_sheet(LAYER_POST_PRICE)
    ws2.append(["圖層", "顏色 R,G,B", "重劃後地價（元/㎡）", "街廓", "正式地號"])
    for v in sorted(price_color):
        blks = sorted(b for b, p in price.items() if p == v)
        nos = sorted((numbers[e["暫編"]] for e in ents
                      if e["類別"] in (KIND_LOT, KIND_OFFSET) and price[e["街廓"]] == v), key=PM.landno_key)
        ws2.append([LAYER_POST_PRICE, "{},{},{}".format(*price_color[v]), f2(v), "、".join(blks), "、".join(nos)])
    wb.save(path)


OUT_FMT = {"dxf": "公告圖_退縮{}m.dxf", "map": "地號對照表_退縮{}m.xlsx", "color": "顏色對照表_重劃後_退縮{}m.xlsx"}


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 重劃後三圖層＋地號對照表＋顏色對照表")
    ap.add_argument("--state", required=True)
    ap.add_argument("--pre-dxf", required=True)
    ap.add_argument("--moedict", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map")
    a = ap.parse_args(argv)
    doc = load_state(a.state)
    tag = tag_of(doc)
    ents = entries_of(doc)
    order = s_order(doc, ents)
    default = default_numbers(order)
    numbers = read_map(a.map, ents) if a.map else dict(default)
    key_of, hh_color, hh_no = owner_scheme(a.moedict, ents)
    price_all = post_prices()
    blks = sorted({e["街廓"] for e in ents if e["類別"] in (KIND_LOT, KIND_OFFSET)})
    miss = [b for b in blks if b not in price_all]
    if miss:
        raise PM.SourceError(f"case_params 之 後街廓_面積單價 缺：{miss}")
    price = {b: price_all[b] for b in blks}
    vals = sorted(set(price.values()))
    price_color = dict(zip(vals, PM.distinct_palette(len(vals))))
    os.makedirs(a.out, exist_ok=True)
    p = {k: os.path.join(a.out, v.format(tag)) for k, v in OUT_FMT.items()}
    write_map(p["map"], ents, order, numbers, default)
    write_dxf(a.pre_dxf, p["dxf"], ents, numbers, key_of, hh_color, hh_no, price, price_color)
    write_color_table(p["color"], ents, numbers, key_of, hh_color, hh_no, price, price_color)
    n = {k: sum(1 for e in ents if e["類別"] == k) for k in (KIND_LOT, KIND_OFFSET)}
    print(f"退縮 {tag} m：分配地 {n[KIND_LOT]}、抵費地 {n[KIND_OFFSET]}、公設 {len(ents) - sum(n.values())}；"
          f"略 {[x['配地暫編'] for x in doc['略']]}")
    print("地號：" + "、".join(f"{t}→{numbers[t]}" for t in order))
    print(f"重劃後地價 {[f2(v) for v in vals]}（街廓 {price}）")
    for k, v in p.items():
        print(f"輸出 {v}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
