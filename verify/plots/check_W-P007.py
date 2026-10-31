# -*- coding: utf-8 -*-
"""
W-P.007 之量測（單 §三 3）：附表 13 重劃前後土地分配清冊之版面照手冊範本（KL 2026-10-31 08:32）。
獨立於 plots/：⛔ import 之；版面之期望（合併、字、直書、格線、欄寬之比）由發單端依
參考/手冊附表頁/附表13_重劃前後土地分配清冊_手冊PDF第88頁.png 量得、逐格寫於本檔（SPEC_*）；
內容之期望 ＝ 舊版（W-P.006_補令一·KL 2026-10-31 17:14 定版）之輸出——表之內容逐值⛔ 變。

命令列：python verify/plots/check_W-P007.py <成果目錄> <舊版成果目錄> <退縮…>
  <成果目錄>     ＝ 新版 plots/post_tables.py 之輸出（附表13_…、附表24_…_退縮<t>m.xlsx）。
  <舊版成果目錄> ＝ 舊版（wip/plots 15935e2）之 plots/post_tables.py 以同一配地結果之輸出。
各退縮印 L0〜L6 之 PASS／FAIL；全 PASS 者結束碼 0。
"""
import os
import sys

FMT = {"a13": "附表13_重劃前後土地分配清冊_退縮{}m.xlsx", "a24": "附表24_土地分配計算表_退縮{}m.xlsx"}
NCOL = 24
FIRST = 11
MIN_ROWS = 5
OLD_FIRST = 8                 # 舊版之資料首列
OLD_OWNER = ((3, 4), (3, 9), (3, 13), (4, 4), (4, 9))   # 舊版之首列登記人 姓名、統編、住址、管理人姓名、統編
OLD_NOTE_GAP, OLD_SIGN_GAP = 2, 4
OLD_SIGN_COL = (1, 5, 9, 13, 17)

# ---- 手冊第 88 頁之範本（發單端量得）
SPEC_CAPTION = ((1, 1), "附表 13 重劃前後土地分配清冊")
SPEC_BOOK = ((2, 19, 2, 24), "共　　冊　第　　冊　第　　頁")
SPEC_TITLE = ((3, 1, 3, 24), "○○縣(市)第○○期○○○○市地重劃區重劃前後土地分配清冊")
SPEC_LABEL = (
    ((4, 1, 5, 7), "土地所有權人（首列登記人）姓名\n國民身分證統一編號"),
    ((6, 1, 7, 7), "管理人姓名\n國民身分證統一編號"),
    ((4, 11, 7, 11), "住址"),
    ((8, 1, 8, 10), "重劃前土地情形"), ((8, 11, 10, 11), "扣除各項負擔後應分配面積(㎡)"),
    ((8, 12, 8, 23), "重劃後土地情形"), ((8, 24, 10, 24), "備註"),
    ((9, 1, 10, 1), "鄉鎮市區"), ((9, 2, 10, 2), "段"), ((9, 3, 10, 3), "小段"), ((9, 4, 10, 4), "地號"),
    ((9, 5, 10, 5), "登記面積(㎡)"), ((9, 6, 10, 6), "取配面積(㎡)"), ((9, 7, 9, 8), "所有權人"),
    ((10, 7, 10, 7), "姓名"), ((10, 8, 10, 8), "國民身分證統一編號"), ((9, 9, 10, 9), "持分比率"),
    ((9, 10, 10, 10), "評定單價(元／㎡)"),
    ((9, 12, 10, 12), "使用分區"), ((9, 13, 10, 13), "段"), ((9, 14, 10, 14), "小段"), ((9, 15, 10, 15), "地號"),
    ((9, 16, 10, 16), "面積(㎡)"), ((9, 17, 10, 17), "評定單價(元／㎡)"), ((9, 18, 9, 19), "預計繳領差額地價"),
    ((10, 18, 10, 18), "繳（元）"), ((10, 19, 10, 19), "領（元）"), ((9, 20, 9, 21), "所有權人"),
    ((10, 20, 10, 20), "姓名"), ((10, 21, 10, 21), "國民身分證統一編號"), ((9, 22, 10, 22), "持分比率"),
    ((9, 23, 10, 23), "建號"),
)
SPEC_VALUE = ((4, 8, 4, 10), (5, 8, 5, 10), (4, 12, 5, 24), (6, 8, 6, 10), (7, 8, 7, 10), (6, 12, 7, 24))
SPEC_VERT = {(4, 11), (8, 24), (9, 1), (9, 3), (9, 4), (9, 5), (9, 6), (9, 9), (9, 12), (9, 14), (9, 15),
             (9, 16), (9, 22), (9, 23), (10, 7), (10, 20)}
# 手冊第 88 頁（2000 像素寬之圖）之 25 條縱線之 x
SPEC_X = (135, 198, 262, 325, 388, 451, 515, 588, 662, 730, 830, 943, 997, 1051, 1105, 1159, 1213, 1335, 1408,
          1482, 1566, 1650, 1708, 1767, 1865)
TOL_W = 0.004                 # 各欄寬占全寬之比之容差
NOTE = "附註：重劃後分配面積與實地指界交接土地面積如有不符，應以地政機關實際登記面積為準。"
SIGN = ("日期：", "承辦：", "股長：", "科長：", "局(處)長：")
SIGN_COL = (1, 6, 10, 14, 19)


def load(out, old, tag):
    import openpyxl
    p = {k: os.path.join(out, v.format(tag)) for k, v in FMT.items()}
    q = {k: os.path.join(old, v.format(tag)) for k, v in FMT.items()}
    new = {k: openpyxl.load_workbook(v) for k, v in p.items()}
    new["raw13"] = raw_borders(p["a13"])
    return new, {k: openpyxl.load_workbook(v) for k, v in q.items()}


def data_rows(ws, first, stop=None):
    """first 列起之資料列（值與格式）：舊版至首一全空之列止；新版至框末列（stop）止、去其末之全空列。"""
    out, r = [], first
    while (r <= stop) if stop else any(ws.cell(r, c).value is not None for c in range(1, NCOL + 1)):
        out.append(tuple((ws.cell(r, c).value, ws.cell(r, c).number_format) for c in range(1, NCOL + 1)))
        r += 1
    while out and all(v is None for v, _ in out[-1]):
        out.pop()
    return out


def last_row(ws):
    """框之末列 ＝ 附註之上一列。"""
    hit = [r for r in range(FIRST, ws.max_row + 1) if ws.cell(r, 1).value == NOTE]
    if len(hit) != 1:
        raise ValueError(f"{ws.title} 之附註 {len(hit)} 處")
    return hit[0] - 1


def raw_borders(path):
    """⇒ {表名: {(列, 欄): (左, 右, 上, 下)}}：逕讀 xlsx 之 XML（openpyxl 讀回時以合併之首格重設其餘格之框線，
    故⛔ 用之量合併範圍內之線）。"""
    import re
    import zipfile
    from xml.etree import ElementTree as ET
    from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
          "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    z = zipfile.ZipFile(path)
    st = ET.fromstring(z.read("xl/styles.xml"))
    borders = []
    for b in st.find("m:borders", ns):
        borders.append(tuple((b.find(f"m:{k}", ns).get("style") if b.find(f"m:{k}", ns) is not None else None)
                             for k in ("left", "right", "top", "bottom")))
    xf = [int(x.get("borderId", 0)) for x in st.find("m:cellXfs", ns)]
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    out = {}
    for sh in ET.fromstring(z.read("xl/workbook.xml")).find("m:sheets", ns):
        tgt = rels[sh.get(f"{{{ns['r']}}}id")]
        tgt = re.sub(r"^/?(xl/)?", "xl/", tgt)
        cells = {}
        for c in ET.fromstring(z.read(tgt)).iter(f"{{{ns['m']}}}c"):
            col, row = coordinate_from_string(c.get("r"))
            cells[(row, column_index_from_string(col))] = borders[xf[int(c.get("s", 0))]]
        out[sh.get("name")] = cells
    return out


def merges(ws):
    return {(m.min_row, m.min_col, m.max_row, m.max_col) for m in ws.merged_cells.ranges}


# ---------------------------------------------------------------- 量測
def l0(new, old):
    """附表 24：與舊版逐格同（表名、值、格式、合併）。"""
    bad = []
    a, b = new["a24"], old["a24"]
    if a.sheetnames != b.sheetnames:
        return [f"附表 24 之表名 {len(a.sheetnames)}／{len(b.sheetnames)}"]
    for x, y in zip(a, b):
        if merges(x) != merges(y) or (x.max_row, x.max_column) != (y.max_row, y.max_column):
            bad.append(f"附表 24 {x.title} 之合併或範圍")
            continue
        for r in range(1, x.max_row + 1):
            for c in range(1, x.max_column + 1):
                u, v = x.cell(r, c), y.cell(r, c)
                if (u.value, u.number_format) != (v.value, v.number_format):
                    bad.append(f"附表 24 {x.title} {u.coordinate}")
    return bad


def l1(new, old):
    """附表 13：表名、首列登記人五值、資料列（24 欄之值與格式）、資料列外之格皆與舊版同（唯位置依範本）。"""
    bad = []
    a, b = new["a13"], old["a13"]
    if a.sheetnames != b.sheetnames:
        return [f"附表 13 之表名 {a.sheetnames[:3]}…／{b.sheetnames[:3]}…"]
    for x, y in zip(a, b):
        got = tuple(x.cell(r, c).value for r, c, _, _ in SPEC_VALUE[:5])
        want = tuple(y.cell(r, c).value for r, c in OLD_OWNER)
        if got != want or x.cell(SPEC_VALUE[5][0], SPEC_VALUE[5][1]).value is not None:
            bad.append(f"{x.title} 之首列登記人 {got}／{want}")
        dn, do = data_rows(x, FIRST, last_row(x)), data_rows(y, OLD_FIRST)
        if dn != do:
            bad.append(f"{x.title} 之資料列（{len(dn)}／{len(do)}）")
        if y.cell(OLD_FIRST + len(do) + OLD_NOTE_GAP - 1, 1).value != NOTE or \
                tuple(y.cell(OLD_FIRST + len(do) + OLD_SIGN_GAP - 1, c).value for c in OLD_SIGN_COL) != SIGN:
            bad.append(f"{y.title} 之舊版之附註或簽欄不在其位（舊版之讀法不合）")
    return bad


def l2(new, old):
    """合併範圍 ＝ 範本（冊頁、題、標籤、所有權人之值格；資料列無合併）。"""
    bad = []
    want = {m for m in {SPEC_BOOK[0], SPEC_TITLE[0]} | {m for m, _ in SPEC_LABEL} | set(SPEC_VALUE)
            if m[:2] != m[2:]}
    for ws in new["a13"]:
        got = merges(ws)
        if got != want:
            bad.append(f"{ws.title} 之合併 多 {sorted(got - want)[:3]} 少 {sorted(want - got)[:3]}")
    return bad


def l3(new, old):
    """字：表名、冊頁、題、各標籤、附註（緊接框下）、簽欄（附註之下一列·五處）；資料列數 ＝ max(列數, 5)。"""
    bad = []
    for ws in new["a13"]:
        (r, c), t = SPEC_CAPTION
        if ws.cell(r, c).value != t:
            bad.append(f"{ws.title} 之表名")
        for (r1, c1, _, _), t in (SPEC_BOOK, SPEC_TITLE) + SPEC_LABEL:
            if ws.cell(r1, c1).value != t:
                bad.append(f"{ws.title} {ws.cell(r1, c1).coordinate} {ws.cell(r1, c1).value!r}≠{t!r}")
        try:
            last = last_row(ws)
        except ValueError as ex:
            bad.append(str(ex))
            continue
        n = len(data_rows(ws, FIRST, last))
        if last != FIRST + max(n, MIN_ROWS) - 1:
            bad.append(f"{ws.title} 之框末列 {last}（資料 {n} 列）")
        if tuple(ws.cell(last + 2, c).value for c in SIGN_COL) != SIGN:
            bad.append(f"{ws.title} 之簽欄")
        for r in range(FIRST + n, last + 1):
            if any(ws.cell(r, c).value is not None for c in range(1, NCOL + 1)):
                bad.append(f"{ws.title} 列 {r} 非空")
    return bad


def l4(new, old):
    """直書之格 ＝ 範本（text_rotation 255）；他格皆非直書。"""
    bad = []
    for ws in new["a13"]:
        got = {(cell.row, cell.column) for row in ws.iter_rows() for cell in row
               if cell.alignment is not None and cell.alignment.text_rotation == 255}
        if got != SPEC_VERT:
            bad.append(f"{ws.title} 之直書 多 {sorted(got - SPEC_VERT)[:3]} 少 {sorted(SPEC_VERT - got)[:3]}")
    return bad


def l5(new, old):
    """格線（逕讀 XML）：框內（第 3 列至框末列·1〜24 欄）每格四邊有線、外框粗線；框外（第 1、2 列、附註與簽欄）無線。"""
    bad = []
    for ws in new["a13"]:
        raw = new["raw13"][ws.title]
        last = last_row(ws)
        miss, outer = 0, 0
        for r in range(3, last + 1):
            for c in range(1, NCOL + 1):
                lt, rt, tp, bt = raw.get((r, c), (None,) * 4)
                if None in (lt, rt, tp, bt):
                    miss += 1
                if (c == 1 and lt != "medium") or (c == NCOL and rt != "medium") or \
                        (r == 3 and tp != "medium") or (r == last and bt != "medium"):
                    outer += 1
        for r in (1, 2, last + 1, last + 2):
            for c in range(1, NCOL + 1):
                if any(x is not None for x in raw.get((r, c), (None,) * 4)):
                    miss += 1
        if miss or outer:
            bad.append(f"{ws.title} 之格線 缺／多 {miss}、外框 {outer}")
    return bad


def l6(new, old):
    """欄寬之比 ＝ 範本（各欄占全寬之比差 ≤ 0.004）；A4 橫式、每頁重出 1〜10 列、寬一頁。"""
    from openpyxl.utils import get_column_letter
    bad = []
    px = [b - a for a, b in zip(SPEC_X, SPEC_X[1:])]
    for ws in new["a13"]:
        w = [ws.column_dimensions[get_column_letter(c)].width for c in range(1, NCOL + 1)]
        if any(x is None or x <= 0 for x in w):
            bad.append(f"{ws.title} 之欄寬未設")
            continue
        d = max(abs(x / sum(w) - y / sum(px)) for x, y in zip(w, px))
        if d > TOL_W:
            bad.append(f"{ws.title} 之欄寬之比差 {d:.4f}")
        ps = ws.page_setup
        if (ps.orientation, str(ps.paperSize), str(ws.print_title_rows).replace("$", ""), ps.fitToWidth) != \
                ("landscape", "9", "1:10", 1):
            bad.append(f"{ws.title} 之紙張 {ps.orientation} {ps.paperSize} {ws.print_title_rows} {ps.fitToWidth}")
    return bad


def run(fn, *a):
    try:
        return fn(*a)
    except Exception as ex:  # noqa: BLE001
        return [f"量測中止：{type(ex).__name__}: {ex}"]


def main(argv):
    out, old, tags = argv[0], argv[1], argv[2:]
    ok = True
    for tag in tags:
        tag = f"{float(tag):g}"
        new, ref = load(out, old, tag)
        for name, fn in (("L0", l0), ("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4), ("L5", l5), ("L6", l6)):
            bad = run(fn, new, ref)
            ok &= not bad
            print(f"退縮 {tag} m {name} {'PASS' if not bad else 'FAIL'}" + ("" if not bad else "：" + "；".join(bad[:4])))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
