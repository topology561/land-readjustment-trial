# -*- coding: utf-8 -*-
"""
W-P.005_補令一 之預覽 PNG：街角第 1 宗之放大圖（公告分配地籍線之註記自輸出之 DXF 讀回；
道路截角〔斜線〕以 check_W-P005.py 之異法自配地結果重導，唯供 KL 一眼辨「深」所納之面積）。

命令列：python verify/plots/preview_W-P005a.py <成果目錄> <PNG 之輸出目錄> <退縮…>
輸出：每一退縮一檔 W-P.005_補令一_街角宗之寬深_退縮<t>m.png。
預覽之標題、斜線與說明唯供 KL 辨圖，⛔ 屬 DXF 之內容（DXF 無標題·KL 17:48）。
"""
import importlib.util
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

for _f in ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",):
    if os.path.exists(_f):
        font_manager.fontManager.addfont(_f)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=_f).get_name()

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("check_W_P005", os.path.join(HERE, "check_W-P005.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
L_CAD = chk.L_CAD


def corner_png(src, tag, out_png):
    import ezdxf
    from shapely.geometry import Point, Polygon
    state = json.load(open(os.path.join(src, chk.FMT["state"].format(tag)), encoding="utf-8"))
    msp = ezdxf.readfile(os.path.join(src, chk.FMT["dxf"].format(tag))).modelspace()
    outlines = [[(p[0], p[1]) for p in e.get_points("xy")] for e in msp.query(f'LWPOLYLINE[layer=="{L_CAD}"]')]
    texts = [(e.dxf.align_point[0], e.dxf.align_point[1], e.dxf.text) for e in msp.query(f'TEXT[layer=="{L_CAD}"]')]
    c = chk.Ctx()
    c.state = state
    corners = [x for x in state["宗"] if "街角第1宗側別" in x]
    if not corners:
        raise SystemExit("無街角第 1 宗")
    n = len(corners)
    cols = 4
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(6 * cols, 6.6 * rows))
    axes = [a for r in (axes if rows > 1 else [axes]) for a in r]
    for ax, x in zip(axes, corners):
        lot = Polygon(x["多邊形"])
        cut = chk._cut_alt(c, x)
        cx, cy = chk._theory_corner(c, x)
        minx, miny, maxx, maxy = lot.union(cut).bounds
        pad = 4.0
        for pl in outlines:
            xs = [p[0] for p in pl] + [pl[0][0]]
            ys = [p[1] for p in pl] + [pl[0][1]]
            ax.plot(xs, ys, color="black", linewidth=0.8)
        xs, ys = cut.exterior.xy
        ax.fill(xs, ys, facecolor="none", edgecolor="tab:red", hatch="////", linewidth=1.0)
        ax.plot([cx], [cy], marker="o", color="tab:red", markersize=4)
        for tx, ty, s in texts:
            if lot.contains(Point(tx, ty)):
                ax.text(tx, ty, s, ha="center", va="center", fontsize=11)
        a = float(x["面積"])
        w = float(x["宗地寬度"])
        ax.set_title(f"{x['街廓']}・{'左' if x['街角第1宗側別'] == '左' else '右'}側街角第 1 宗（{x['配地暫編']}）\n"
                     f"S {x['S']:.2f}／W {w:.2f}／截角 {cut.area:.2f} ㎡\n"
                     f"深 ＝（{a:.2f} ＋ {cut.area:.2f}）÷ {w:.2f}", fontsize=11)
        ax.set_xlim(minx - pad, maxx + pad)
        ax.set_ylim(miny - pad, maxy + pad)
        ax.set_aspect("equal")
        ax.axis("off")
    for ax in axes[n:]:
        ax.axis("off")
    fig.suptitle(f"W-P.005_補令一　街角第 1 宗之寬（S）與深（含道路截角·紅斜線）（退縮 {tag} m·示範資料）",
                 fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(out_png, dpi=90)
    plt.close(fig)


def main(argv):
    src, out, *tags = argv
    os.makedirs(out, exist_ok=True)
    rc = 0
    for t in tags:
        p = os.path.join(out, f"W-P.005_補令一_街角宗之寬深_退縮{t}m.png")
        corner_png(src, t, p)
        sz = os.path.getsize(p)
        print(f"{p}\t{sz} bytes")
        rc |= int(sz == 0)
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
