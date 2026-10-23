# -*- coding: utf-8 -*-
"""
W-P.001 之故意錯誤之測（單 §三 4）：成果須綠、8 種變異體須各紅。

命令列：python verify/plots/mutate_W-P001.py <成果目錄> <拋棄式之工作目錄>
  成果目錄 ＝ plots/prelim_maps.py --out 之目錄（⛔ 改之；變異體皆寫於工作目錄之複本）。
結束碼：成果綠且 8 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("check_W_P001", os.path.join(HERE, "check_W-P001.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)

DXF = "重劃前圖.dxf"
A2 = "附表02_重劃前土地地號摘錄簿.xlsx"
A3 = "附表03_重劃前土地清冊.xlsx"


def _copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for f in (DXF, A2, A3):
        shutil.copy2(os.path.join(src, f), os.path.join(dst, f))


def _lot_polys(doc):
    from shapely.geometry import Point, Polygon
    msp = doc.modelspace()
    polys = [Polygon([(p[0], p[1]) for p in e.get_points("xy")])
             for e in msp if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == chk.L_CAD]
    out = {}
    for e in msp:
        if e.dxftype() == "TEXT" and e.dxf.layer == chk.L_CAD:
            pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
            for pg in polys:
                if pg.contains(pt):
                    out[e.dxf.text] = pg
    return out


def _edit_dxf(d, fn):
    import ezdxf
    p = os.path.join(d, DXF)
    doc = ezdxf.readfile(p)
    fn(doc)
    doc.saveas(p)


def m1_drop_parcel(d):
    def f(doc):
        from shapely.geometry import Point
        pg = _lot_polys(doc)["628-20"]
        msp = doc.modelspace()
        dead = []
        for e in msp:
            if e.dxftype() == "TEXT":
                pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
            elif e.dxftype() == "LWPOLYLINE":
                from shapely.geometry import Polygon
                pt = Polygon([(p[0], p[1]) for p in e.get_points("xy")]).representative_point()
            elif e.dxftype() == "HATCH":
                pt = chk.hatch_poly(e).representative_point()
            else:
                continue
            if pg.contains(pt):
                dead.append(e)
        for e in dead:
            msp.delete_entity(e)
    _edit_dxf(d, f)


def m2_swap_labels(d):
    def f(doc):
        t = {e.dxf.text: e for e in doc.modelspace()
             if e.dxftype() == "TEXT" and e.dxf.layer == chk.L_CAD}
        t["628-1"].dxf.text, t["628-3"].dxf.text = "628-3", "628-1"
    _edit_dxf(d, f)


def m3_layer_name(d):
    bad = "重劃前歸户圖"

    def f(doc):
        doc.layers.add(bad)
        for e in doc.modelspace():
            if e.dxf.layer == chk.L_OWN:
                e.dxf.layer = bad
        doc.layers.remove(chk.L_OWN)
    _edit_dxf(d, f)


def m4_shift(d):
    from ezdxf.math import Matrix44

    def f(doc):
        m = Matrix44.translate(0.5, 0, 0)
        for e in doc.modelspace():
            e.transform(m)
    _edit_dxf(d, f)


def m5_recolor(d):
    def f(doc):
        lots, owners, hh, zone, price = chk.source_truth()
        polys = _lot_polys(doc)
        cnt = {}
        for ln in lots:
            cnt[hh[ln]] = cnt.get(hh[ln], 0) + 1
        target = sorted(ln for ln in lots if cnt[hh[ln]] >= 2)[0]
        pg = polys[target]
        for e in doc.modelspace():
            if e.dxftype() == "HATCH" and e.dxf.layer == chk.L_OWN \
                    and pg.contains(chk.hatch_poly(e).representative_point()):
                e.rgb = (1, 2, 3)
    _edit_dxf(d, f)


def m6_price_off_by_one(d):
    def f(doc):
        for e in doc.modelspace():
            if e.dxftype() == "TEXT" and e.dxf.layer == chk.L_PRICE:
                e.dxf.text = str(int(e.dxf.text) + 1)
                break
    _edit_dxf(d, f)


def m7_empty(d):
    open(os.path.join(d, DXF), "wb").close()


def m8_drop_coowner_row(d):
    import openpyxl
    p = os.path.join(d, A3)
    wb = openpyxl.load_workbook(p)
    ws = wb.active
    i_ln = [c.value for c in ws[1]].index("地號")
    lots = [ws.cell(r, i_ln + 1).value for r in range(2, ws.max_row + 1)]
    for r, ln in enumerate(lots, start=2):
        if lots.count(ln) >= 2:
            ws.delete_rows(r, 1)
            break
    wb.save(p)


MUTANTS = [
    ("① 漏一宗（628-20）", m1_drop_parcel),
    ("② 地號錯置（628-1↔628-3）", m2_swap_labels),
    ("③ 圖層名錯（歸戶→歸户）", m3_layer_name),
    ("④ 全圖平移 0.5 m", m4_shift),
    ("⑤ 同戶之一宗改色", m5_recolor),
    ("⑥ 一宗之地價差 1 元", m6_price_off_by_one),
    ("⑦ 空檔", m7_empty),
    ("⑧ 附表 3 漏一共有人之列", m8_drop_coowner_row),
]


def verdict(d):
    res = chk.run(os.path.join(d, DXF), os.path.join(d, A3))
    ok = bool(res) and len(res) == 12 and all(x[1] for x in res)
    return ok, [x[0] for x in res if not x[1]]


def main(argv):
    src, work = argv
    rows = []
    base = os.path.join(work, "base")
    _copy(src, base)
    print("== 成果 ==")
    ok, fails = verdict(base)
    rows.append(("成果", "綠" if ok else "紅", fails, ok))
    for name, fn in MUTANTS:
        d = os.path.join(work, f"mut{len(rows)}")
        _copy(src, d)
        fn(d)
        print(f"== {name} ==")
        ok, fails = verdict(d)
        rows.append((name, "綠" if ok else "紅", fails, not ok))
    print("\n| 對象 | 判 | 不過之量測 | 合期望 |")
    print("|---|---|---|---|")
    for n, v, f, good in rows:
        print(f"| {n} | {v} | {'、'.join(f) or '—'} | {'是' if good else '否'} |")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
