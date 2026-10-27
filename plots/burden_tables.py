# -*- coding: utf-8 -*-
"""
W-P.004　附表 20 公共設施用地負擔面積統計表、附表 22 計算負擔總計表（附表 23 為其範例 2·同式·一張）。
照手冊表樣（KL 2026-10-24 02:14／14:55）；填法依 KL 2026-10-27 23:15、23:20。

命令列：python plots/burden_tables.py --out <目錄>
輸出（皆寫至 --out，⛔ 入倉）：見 OUT_NAMES。
所據：出圖線/orders/W-P.004_附表20-22.md（§一、§二）。
  附表 20：使用者圖（data/V6.dxf）之 BLOCK 圖層，每一公共設施區塊一列（編號、名稱取其註記「編號-名稱」；
    道路在前、餘次之，各依編號）；合計面積 ＝ 區塊之圖面面積；臨街地特別負擔 ＝ 臨接該區塊之街廓邊之負擔面積
    （verify/case_params_UC9898.json 之 blocks.*.{正面,左側,右側}.期望負擔面積_m2）之和 ×（1−C），各列乘後再取位
    （KL 23:15 問二）；一般負擔 ＝ 合計 − 特別。
  附表 22：一 實測面積（財務接線_v3.重劃區總面積_m2_精確）、私有與公有之登記面積（U_LAND「公私別」）、
    未登記與實測誤差填 0（KL 23:15 問三 B·差額記於備註）；二 抵充 0；三 所有權人數（同一統一編號計一人·問四）；
    四 留空；五 Σ（登記面積 × 區段單價〔個位〕）÷ 登記面積和（問五 乙）；六 抄附表 20 之小計；七 費用總額；
    八 Σ（街廓面積 × 單價）、平均地價；九 實測面積 − 公設合計；十 第八項 ÷ 第五項（表上之數·KL 23:20）；
    十一 一般負擔係數（核心線之式·重劃前平均地價以圖面面積計）；十二 費用負擔係數（加總形）；十三 平均負擔比率。
    位數（問六 乙）：面積二位、總地價至元、平均地價二位、上漲率與係數六位、比率 0.01％。
缺值或與單之所據不符一律報錯停止（⛔ 靜默補值）；匯入資料所無之欄留空（⛔ 杜撰）。
"""
import argparse
import io
import json
import math
import os
import re
import sys
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （讀取與表樣之共用函式·W-P.001／002）
import appx_tables as AT  # noqa: E402  （表樣之共用函式·W-P.003）

DXF_BLOCK = os.path.join(REPO, "data", "V6.dxf")
DXF_ENCODING = "cp950"
LAYER_BLOCK, LAYER_FRONT, LAYER_SIDE = "BLOCK", "FRONT_LINE", "SIDE_LINE"
FACE_LAYER = {"正面": LAYER_FRONT, "左側": LAYER_SIDE, "右側": LAYER_SIDE}
LOT_RE = re.compile(r"^R\d+$")      # 可分配之街廓（app parse_block_dxf 之慣例「R<數字>」）
ROAD_WORD = "道路"                  # 手冊第 3085 列：道路、溝渠在前
OFFSET_M = 0.5                      # 街廓邊向外取樣之距
SAMPLES = 400
MIN_SHARE = Decimal("0.9")          # 一邊之取樣落於同一公設區塊之最低比例
UNION_TOL = 0.01                    # 聯集區塊之面積 ＝ 其成員之和之容差（㎡）
C_PUBPRIV = 38                      # U_LAND「公私別」（所有權部）
TITLE_A20 = "○○縣(市)第○○期○○○○市地重劃區公共設施用地負擔面積統計表"
TITLE_A22 = "○○縣(市)第○期○○○○市地重劃區計算負擔總計表"
A20_HEAD = ("編號", "名稱", "合計面積（平方公尺）", "臨街地特別負擔面積（平方公尺）", "一般負擔面積（平方公尺）", "備註")
SIGN_A20 = ("製表日期:　年　月　日", "承辦:", "股長:", "科長:")
SIGN_A22 = ("承辦", "股長", "科長", "局(處)長", "製表日期:　年　月　日")
NOTE_PRE_PRICE = "一般負擔係數所用之重劃前地價，係以各宗地之圖面面積計"   # KL 23:15 問五（逐字）

OUT_NAMES = {
    "a20": "附表20_公共設施用地負擔面積統計表.xlsx",
    "a22": "附表22_計算負擔總計表.xlsx",
}


def dec(x):
    if isinstance(x, Decimal):
        return x
    if isinstance(x, float):
        return Decimal(repr(x))
    return Decimal(str(x))


def q(x, nd):
    return dec(x).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- 讀取
def load_dxf(path=DXF_BLOCK):
    import ezdxf
    with open(path, "rb") as f:
        doc = ezdxf.read(io.TextIOWrapper(f, encoding=DXF_ENCODING, newline=None))
    return doc.modelspace()


def _ring(e):
    if e.dxftype() == "LWPOLYLINE":
        return [(p[0], p[1]) for p in e.get_points("xy")], e.closed
    return [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices], e.is_closed


def load_blocks(msp):
    """⇒ {編號: (名稱, Polygon)}（唯單一註記之區塊）。聯集之區塊（含二以上之註記）須 ＝ 其成員之和。"""
    from shapely.geometry import Point, Polygon
    polys = []
    for e in msp.query(f'LWPOLYLINE POLYLINE[layer=="{LAYER_BLOCK}"]'):
        pts, closed = _ring(e)
        if not closed:
            raise PM.SourceError(f"{LAYER_BLOCK} 有未閉合之線（{len(pts)} 點）")
        polys.append(Polygon(pts))
    texts = []
    for e in msp.query(f'TEXT MTEXT[layer=="{LAYER_BLOCK}"]'):
        t = e.plain_text() if e.dxftype() == "MTEXT" else e.dxf.text
        texts.append((t.strip(), Point(e.dxf.insert.x, e.dxf.insert.y)))
    single, unions = {}, []
    for p in polys:
        labs = [t for t, pt in texts if p.contains(pt)]
        if not labs:
            raise PM.SourceError(f"{LAYER_BLOCK} 有無註記之區塊（面積 {p.area:.4f}）")
        if len(labs) > 1:
            unions.append((labs, p))
            continue
        if "-" not in labs[0]:
            raise PM.SourceError(f"區塊之註記非「編號-名稱」：{labs[0]!r}")
        no, name = labs[0].split("-", 1)
        if no in single:
            raise PM.SourceError(f"區塊之編號重複：{no}")
        single[no] = (name, p)
    for labs, p in unions:
        nos = [t.split("-", 1)[0] for t in labs]
        if any(n not in single for n in nos):
            raise PM.SourceError(f"聯集區塊之成員無單獨之區塊：{labs}")
        s = sum(single[n][1].area for n in nos)
        if abs(s - p.area) > UNION_TOL:
            raise PM.SourceError(f"聯集區塊 {nos} 之面積 {p.area:.4f} ≠ 成員之和 {s:.4f}")
    return single


def public_blocks(blocks):
    pub = {k: v for k, v in blocks.items() if not LOT_RE.match(k)}
    if not pub:
        raise PM.SourceError("圖上無公共設施之區塊")
    return pub


def block_order(no, name):
    m = re.match(r"^(\D*)(\d*)$", no)
    pre, num = (m.group(1), int(m.group(2)) if m.group(2) else 0) if m else (no, 0)
    return (0 if ROAD_WORD in name else 1, pre, num, no)


def load_case(path=AT.CASE_PARAMS):
    d = json.load(open(path, encoding="utf-8"))
    v = d["財務接線_v3"]
    for k in ("重劃區總面積_m2_精確", "抵充地_m2", "已徵收公設_m2", "重劃前平均地價_元每m2", "重劃後平均地價_元每m2",
              "貸款利息_元", "中繼錨", "後街廓_面積單價", "重劃前區段_面積單價"):
        if k not in v:
            raise PM.SourceError(f"case_params 之 財務接線_v3 缺 {k}")
    return d["blocks"], v


def cost_total(v):
    m = v["中繼錨"]
    s = int(m["工程費_元"]) + int(m["重劃費_元"]) + int(v["貸款利息_元"])
    if s != int(m["費用總額_元"]):
        raise PM.SourceError(f"費用總額 {m['費用總額_元']} ≠ 工程費＋重劃費＋利息 {s}")
    return s


def post_total(v):
    """Σ（街廓面積 × 單價·各二位四捨五入）＝ 附表 21 之總價之和（W-P.003）。"""
    t = Decimal(0)
    for b, x in v["後街廓_面積單價"].items():
        if PM._blank(x.get("面積_m2")) or PM._blank(x.get("單價_元每m2")):
            raise PM.SourceError(f"後街廓 {b} 之面積或單價為空")
        t += q(dec(x["面積_m2"]) * dec(x["單價_元每m2"]), 2)
    return t


# ---------------------------------------------------------------- 臨街地特別負擔之歸屬
def _locate(blocks, x, y):
    from shapely.geometry import Point
    pt = Point(x, y)
    for no, (_, p) in blocks.items():
        if p.contains(pt):
            return no
    return None


def face_road(blocks, pub, lot, line):
    """街廓 lot 之一邊（LINE）沿兩側法向各外移 OFFSET_M 取樣；一側須落於 lot，他側之多數 ⇒ 所臨之公設區塊。"""
    (x1, y1), (x2, y2) = line
    L = math.hypot(x2 - x1, y2 - y1)
    nx, ny = -(y2 - y1) / L, (x2 - x1) / L
    side = {1: Counter(), -1: Counter()}
    for i in range(SAMPLES):
        t = (i + 0.5) / SAMPLES
        px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        for s in (1, -1):
            side[s][_locate(blocks, px + s * OFFSET_M * nx, py + s * OFFSET_M * ny)] += 1
    inner = [s for s in (1, -1) if side[s].most_common(1)[0][0] == lot]
    if len(inner) != 1:
        raise PM.SourceError(f"街廓 {lot} 之邊 {line} 兩側皆非／皆是該街廓")
    out = side[-inner[0]]
    road, n = max(((k, c) for k, c in out.items() if k is not None), key=lambda kc: kc[1], default=(None, 0))
    if road not in pub or Decimal(n) / SAMPLES < MIN_SHARE:
        raise PM.SourceError(f"街廓 {lot} 之邊外側之取樣未集中於一公設區塊：{dict(out)}")
    return road


def face_lines(msp):
    out = {LAYER_FRONT: [], LAYER_SIDE: []}
    for lay in out:
        for e in msp.query(f'LINE[layer=="{lay}"]'):
            out[lay].append(((e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)))
    return out


def special_by_road(msp, blocks, pub, case_blocks):
    """⇒ {公設編號: Σ 期望負擔面積（未乘 1−C）}、[(街廓, 面, 負擔, 公設)]。"""
    lines = face_lines(msp)
    raw = {k: Decimal(0) for k in pub}
    faces = []
    for lot in sorted(case_blocks, key=AT.block_key):
        if lot not in blocks:
            raise PM.SourceError(f"case_params 之街廓 {lot} 不在圖上")
        for face, lay in FACE_LAYER.items():
            f = case_blocks[lot].get(face)
            if f is None:
                raise PM.SourceError(f"case_params 之 {lot}.{face} 缺")
            burden = dec(f["期望負擔面積_m2"])
            if burden == 0:
                continue
            want = q(f["期望長度_m"], 3)
            hit = [ln for ln in lines[lay] if q(math.hypot(ln[1][0] - ln[0][0], ln[1][1] - ln[0][1]), 3) == want]
            if len(hit) != 1:
                raise PM.SourceError(f"{lot}.{face}：{lay} 中長 {want} 之線 {len(hit)} 條（須恰一條）")
            road = face_road(blocks, pub, lot, hit[0])
            raw[road] += burden
            faces.append((lot, face, burden, road))
    return raw, faces


# ---------------------------------------------------------------- 附表 20
def a20_rows(pub, raw, one_minus_c):
    rows = []
    for no in sorted(pub, key=lambda k: block_order(k, pub[k][0])):
        name, p = pub[no]
        total = q(p.area, 2)
        sp = q(raw[no] * one_minus_c, 2)          # 各列乘（1−C）後再取位（KL 23:15 問二）
        rows.append((no, name, total, sp, total - sp))
    sub = tuple(sum(r[i] for r in rows) for i in (2, 3, 4))
    return rows, sub


def write_a20(path, rows, sub):
    wb, ws = AT._book()
    ws.title = "公設負擔面積統計表"
    n = len(A20_HEAD)
    AT._title(ws, 1, TITLE_A20, n)
    for c, lab in enumerate(A20_HEAD, start=1):
        ws.cell(2, c, lab).alignment = AT._center()
    r = 2
    for no, name, total, sp, gen in rows:
        r += 1
        for c, v in enumerate((no, name, float(total), float(sp), float(gen)), start=1):
            ws.cell(r, c, v)
        for c in (3, 4, 5):
            ws.cell(r, c).number_format = "#,##0.00"
    r += 1
    ws.cell(r, 2, "小　計").alignment = AT._center()
    for c, v in zip((3, 4, 5), sub):
        ws.cell(r, c, float(v)).number_format = "#,##0.00"
    PM._grid(ws, 2, r, n)
    AT._sign(ws, r + 1, SIGN_A20, n)
    PM._page(ws, "1:2", landscape=False)
    wb.save(path)


# ---------------------------------------------------------------- 附表 22
def registry(lots, owners, area, zone_of, price):
    """⇒ 私／公之登記面積、所有權人數（統一編號不重複）、Σ（登記面積 × 區段單價〔個位〕）。"""
    a = {"私": Decimal(0), "公": Decimal(0)}
    uid = {"私": set(), "公": set()}
    pre_total = Decimal(0)
    for x in lots:
        ln = x["地號"]
        kinds = {r[C_PUBPRIV] for seq in owners[ln].values() for r in seq}
        if len(kinds) != 1 or not kinds <= set(a):
            raise PM.SourceError(f"{ln} 之公私別 {kinds}（須唯「私」或「公」）")
        k = kinds.pop()
        a[k] += dec(area[ln])
        for r in PM.owner_rows(owners, ln):
            if PM._blank(r[PM.C_UID]):
                raise PM.SourceError(f"{ln} 有統一編號為空之所有權人")
            uid[k].add(str(r[PM.C_UID]).strip())
        pre_total += dec(area[ln]) * dec(price[zone_of[ln]])
    if uid["私"] & uid["公"]:
        raise PM.SourceError(f"同一統一編號兼為私有與公有：{sorted(uid['私'] & uid['公'])}")
    return a, {k: len(s) for k, s in uid.items()}, pre_total


def a22_values(v, reg_area, n_owner, pre_total, sub20):
    exact = dec(v["重劃區總面積_m2_精確"])
    offset, kept = dec(v["抵充地_m2"]), dec(v["已徵收公設_m2"])
    if offset != 0 or kept != 0:
        raise PM.SourceError(f"抵充地 {offset}／原位置原面積分配 {kept} 非 0：本單未定其填法")
    reg = reg_area["私"] + reg_area["公"]
    diff = exact - reg
    if diff < 0:
        raise PM.SourceError(f"實測面積小於登記面積（{diff}）：本單未定其填法（KL 23:15 問三唯定「多」者）")
    denom = exact - offset - kept
    pre_avg = q(pre_total / reg, 2)
    post_t = post_total(v)
    post_avg_full = dec(v["重劃後平均地價_元每m2"])
    post_avg = q(post_avg_full, 2)
    cost = cost_total(v)
    total20, sp20, gen20 = sub20
    pub_raw = dec(v["_pub_raw"])
    r1 = pub_raw / denom
    r2 = Decimal(cost) / (post_avg_full * denom)
    pre_avg_map = dec(v["重劃前平均地價_元每m2"])
    return {
        "實測": q(exact, 2), "私有": q(reg_area["私"], 2), "公有": q(reg_area["公"], 2),
        "未登記": Decimal(0), "實測誤差": Decimal(0), "差額": q(diff, 2),
        "抵充": q(offset, 2), "抵充已登記": Decimal(0), "抵充未登記": Decimal(0),
        "人數": n_owner["私"] + n_owner["公"], "人數私": n_owner["私"], "人數公": n_owner["公"],
        "前總": q(pre_total, 0), "前均": pre_avg,
        "共同負擔": total20 - offset - kept, "特別": sp20, "一般": gen20,
        "費用": cost,
        "後總": q(post_t, 0), "後均": post_avg,
        "可分配": q(exact - total20, 2),
        "上漲率": q(post_avg / pre_avg, 6),                       # 表上第八項 ÷ 第五項（KL 23:20）
        "B": q(gen20 * pre_avg_map / (post_avg_full * denom), 6),
        "C": q(Decimal(cost) / post_t, 6),
        "比率": q(r1 + r2, 4), "公設比": q(r1, 4), "費用比": q(r2, 4),
        "_前均圖面": q(pre_avg_map, 2), "_前總圖面": q(v["_pre_total_map"], 0), "_denom": q(denom, 2), "_kept": q(kept, 2),
    }


def _fmt(x, nd):
    return f"{dec(x):,.{nd}f}"


A22_NCOL = 10
NF = {"area": "#,##0.00", "yuan": "#,##0", "avg": "#,##0.00", "k6": "0.000000", "pct": "0.00%", "int": "0"}


def write_a22(path, x):
    wb, ws = AT._book()
    ws.title = "計算負擔總計表"
    AT._title(ws, 1, TITLE_A22, A22_NCOL)
    left = [  # (列, 大類, 項次, 項目, 值, 格式, 單位)
        (2, "重劃前情形", "一", "重劃區實測面積", x["實測"], "area", "平方公尺"),
        (3, None, None, "1.私有土地面積", x["私有"], "area", "平方公尺"),
        (4, None, None, "2.公有土地面積", x["公有"], "area", "平方公尺"),
        (5, None, None, "3.未登記土地面積", x["未登記"], "area", "平方公尺"),
        (6, None, None, "4.實測誤差面積", x["實測誤差"], "area", "平方公尺"),
        (7, None, "二", "原公有道路溝渠河川及未登記等土地抵充面積", x["抵充"], "area", "平方公尺"),
        (8, None, None, "1.已登記土地面積", x["抵充已登記"], "area", "平方公尺"),
        (9, None, None, "2.未登記土地面積", x["抵充未登記"], "area", "平方公尺"),
        (10, None, "三", "重劃區土地所有權人數", x["人數"], "int", "人"),
        (11, None, None, "1.私有：", x["人數私"], "int", "人"),
        (12, None, None, "2.公有：", x["人數公"], "int", "人"),
        (13, None, "四", "私有土地所有權人申請（同意）辦理重劃情形　人數：", None, None, "人，占　　％"),
        (14, None, None, "面積：", None, None, "平方公尺，占　　％"),
        (15, None, "五", "評定之重劃前平均地價及總地價　總地價：", x["前總"], "yuan", "元"),
        (16, None, None, "每平方公尺地價：", x["前均"], "avg", "元"),
        (17, "各項負擔情形", "六", "公共設施用地扣除原公有道路溝渠河川及未登記土地等抵充土地後共同負擔總面積",
         x["共同負擔"], "area", "平方公尺"),
        (18, None, None, "1.臨街地特別負擔×(1-C)", x["特別"], "area", "平方公尺"),
        (19, None, None, "2.一般負擔", x["一般"], "area", "平方公尺"),
        (20, None, "七", "費用負擔總額：1.費用總額", x["費用"], "yuan", "元"),
        (21, None, None, "2.補助金額", None, None, "元"),
    ]
    right = [
        (2, "重劃後情形", "八", "評定之重劃後平均地價及總地價　總地價：", x["後總"], "yuan", "元"),
        (3, None, None, "每平方公尺地價：", x["後均"], "avg", "元"),
        (4, None, "九", "重劃後可分配土地面積", x["可分配"], "area", "平方公尺"),
        (5, "計算負擔", "十", "重劃前後每平方公尺平均地價上漲率：", x["上漲率"], "k6", None),
        (6, None, None, f"{_fmt(x['後均'], 2)} ÷ {_fmt(x['前均'], 2)}", None, None, None),
        (7, None, "十一", "公共設施用地一般負擔係數：", x["B"], "k6", None),
        (8, None, None, f"{_fmt(x['一般'], 2)} × {_fmt(x['_前均圖面'], 2)} ÷ [{_fmt(x['後均'], 2)} × "
                        f"({_fmt(x['實測'], 2)} － {_fmt(x['抵充'], 2)} － {_fmt(x['_kept'], 2)})]", None, None, None),
        (9, None, "十二", "費用負擔係數：", x["C"], "k6", None),
        (10, None, None, f"{_fmt(x['費用'], 0)} ÷ {_fmt(x['後總'], 0)}", None, None, None),
        (11, None, "十三", "平均負擔比率：", x["比率"], "pct", None),
        (12, None, None, "1.公共設施用地負擔比率：", x["公設比"], "pct", None),
        (13, None, None, "2.費用負擔比率：", x["費用比"], "pct", None),
        (14, "備註", None, "1.公共設施用地負擔比率", None, None, None),
        (15, None, None, f"{_fmt(x['共同負擔'], 2)} ÷ ({_fmt(x['實測'], 2)} － {_fmt(x['抵充'], 2)} － {_fmt(x['_kept'], 2)}) ＝ "
                         f"{x['公設比'] * 100:.2f}％", None, None, None),
        (16, None, None, "2.費用負擔比率", None, None, None),
        (17, None, None, f"{_fmt(x['費用'], 0)} ÷ [{_fmt(x['後均'], 2)} × ({_fmt(x['實測'], 2)} － "
                         f"{_fmt(x['抵充'], 2)} － {_fmt(x['_kept'], 2)})] ＝ {x['費用比'] * 100:.2f}％", None, None, None),
    ]
    if x["差額"] > 0:
        right.append((18, None, None, f"3.實測面積較登記面積多 {_fmt(x['差額'], 2)} 平方公尺，係登記與實測之差，非未登記地。",
                      None, None, None))
    for base, rows in ((0, left), (5, right)):
        for r, grp, no, lab, val, nf, unit in rows:
            if grp:
                ws.cell(r, base + 1, grp).alignment = AT._center()
            if no:
                ws.cell(r, base + 2, no).alignment = AT._center()
            ws.cell(r, base + 3, lab)
            if val is not None:
                c = ws.cell(r, base + 4, float(val) if nf != "int" else int(val))
                c.number_format = NF[nf]
            if unit:
                ws.cell(r, base + 5, unit)
    last = 21
    for c1, (r1, r2) in ((1, (2, 16)), (1, (17, 21)), (6, (2, 4)), (6, (5, 13)), (6, (14, last))):
        ws.merge_cells(start_row=r1, start_column=c1, end_row=r2, end_column=c1)
    PM._grid(ws, 2, last, A22_NCOL)
    AT._sign(ws, last + 1, SIGN_A22, A22_NCOL)
    ws.cell(last + 2, 1, f"註：{NOTE_PRE_PRICE}（總地價 {_fmt(x['_前總圖面'], 0)} 元，每平方公尺 "
                         f"{_fmt(x['_前均圖面'], 2)} 元），第五項係依重劃前土地清冊以登記面積計，故二數不同。")
    PM._page(ws, "1:1", landscape=True)
    wb.save(path)


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.004 附表 20、22（23 同式）")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)

    case_blocks, v = load_case()
    msp = load_dxf()
    blocks = load_blocks(msp)
    pub = public_blocks(blocks)
    raw, faces = special_by_road(msp, blocks, pub, case_blocks)
    cost = cost_total(v)
    one_minus_c = 1 - Decimal(cost) / post_total(v)
    rows, sub = a20_rows(pub, raw, one_minus_c)

    lots, owners, area = PM.load_cadastre()
    zone_of, unit, price = PM.load_price_zones()
    miss = {x["地號"] for x in lots} - set(zone_of)
    if miss:
        raise PM.SourceError(f"case_params 之原地號_區段 缺：{sorted(miss)}")
    reg_area, n_owner, pre_total = registry(lots, owners, area, zone_of, price)
    zones = v["重劃前區段_面積單價"]
    za = sum(dec(z["面積_m2"]) for z in zones.values())
    zt = sum(dec(z["面積_m2"]) * dec(z["單價_元每m2"]) for z in zones.values())
    if abs(zt / za - dec(v["重劃前平均地價_元每m2"])) > Decimal("0.01"):
        raise PM.SourceError(f"區段之 Σ面積×單價÷Σ面積 {zt / za} ≠ 重劃前平均地價 {v['重劃前平均地價_元每m2']}")
    v = dict(v, _pub_raw=sum(dec(p.area) for _, p in pub.values()), _pre_total_map=zt)
    x = a22_values(v, reg_area, n_owner, pre_total, sub)

    p = {k: os.path.join(a.out, n) for k, n in OUT_NAMES.items()}
    write_a20(p["a20"], rows, sub)
    write_a22(p["a22"], x)
    for lot, face, b, road in faces:
        print(f"特別負擔 {lot}.{face} {b} → {road}")
    print("附表20 " + "；".join(f"{r[0]} {r[2]}／{r[3]}／{r[4]}" for r in rows))
    print(f"附表20 小計 {sub[0]}／{sub[1]}／{sub[2]}")
    print(f"附表22 前 {x['前總']}·{x['前均']}；後 {x['後總']}·{x['後均']}；上漲率 {x['上漲率']}；"
          f"B {x['B']}；C {x['C']}；比率 {x['比率']}（{x['公設比']}＋{x['費用比']}）；人數 {x['人數']}")
    for k, f in p.items():
        print(f"輸出 {f}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
