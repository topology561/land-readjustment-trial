# -*- coding: utf-8 -*-
"""
W-P.001 之預覽 PNG（單 §三 6）：自輸出之 DXF 讀回而繪（非自程式之內部資料），附表 2、3 之前 20 列截取。

命令列：python verify/plots/preview_W-P001.py <成果目錄> <PNG 之輸出目錄>
輸出：W-P.001_重劃前三圖層.png、W-P.001_附表2-3前20列.png
預覽之標題唯供 KL 一眼辨圖層，⛔ 屬 DXF 之內容（DXF 無標題·KL 17:48）。
"""
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

LAYERS = ("重劃前地籍線", "重劃前歸戶圖", "重劃前地價圖")


def maps_png(dxf_path, out_png):
    import ezdxf
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    fig, axes = plt.subplots(1, 3, figsize=(30, 11.5))
    outlines = [[(p[0], p[1]) for p in e.get_points("xy")]
                for e in msp if e.dxftype() == "LWPOLYLINE"]
    for ax, layer in zip(axes, LAYERS):
        for e in msp:
            if e.dxf.layer != layer:
                continue
            if e.dxftype() == "HATCH":
                for p in e.paths:
                    xs = [v[0] for v in p.vertices]
                    ys = [v[1] for v in p.vertices]
                    ax.fill(xs, ys, color=tuple(c / 255 for c in e.rgb), linewidth=0)
            elif e.dxftype() == "TEXT":
                x, y = e.dxf.align_point[0], e.dxf.align_point[1]
                ax.text(x, y, e.dxf.text, ha="center", va="center", fontsize=6)
        for pts in outlines:
            xs = [p[0] for p in pts] + [pts[0][0]]
            ys = [p[1] for p in pts] + [pts[0][1]]
            ax.plot(xs, ys, color="black", linewidth=0.5)
        ax.set_title(layer, fontsize=18)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(out_png, dpi=110)
    plt.close(fig)


def tables_png(a2, a3, out_png, n=20):
    import openpyxl
    fig, axes = plt.subplots(2, 1, figsize=(30, 15), gridspec_kw={"height_ratios": [1, 1]})
    for ax, path, title in ((axes[0], a2, "附表 2　重劃前土地地號摘錄簿（前 20 列）"),
                            (axes[1], a3, "附表 3　重劃前土地清冊（前 20 列）")):
        rows = list(openpyxl.load_workbook(path, read_only=True).active.iter_rows(values_only=True))
        head, body = rows[0], rows[1:1 + n]
        cells = [["" if v is None else str(v) for v in r] for r in body]
        ax.axis("off")
        ax.set_title(title, fontsize=14, loc="left")
        t = ax.table(cellText=cells, colLabels=list(head), loc="upper left", cellLoc="center")
        t.auto_set_font_size(False)
        t.set_fontsize(7)
        t.scale(1, 1.05)
    fig.tight_layout()
    fig.savefig(out_png, dpi=110)
    plt.close(fig)


def main(argv):
    src, out = argv
    os.makedirs(out, exist_ok=True)
    p1 = os.path.join(out, "W-P.001_重劃前三圖層.png")
    p2 = os.path.join(out, "W-P.001_附表2-3前20列.png")
    maps_png(os.path.join(src, "重劃前圖.dxf"), p1)
    tables_png(os.path.join(src, "附表02_重劃前土地地號摘錄簿.xlsx"),
               os.path.join(src, "附表03_重劃前土地清冊.xlsx"), p2)
    for p in (p1, p2):
        sz = os.path.getsize(p)
        print(f"{p}\t{sz} bytes")
        if sz == 0:
            return 1
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
