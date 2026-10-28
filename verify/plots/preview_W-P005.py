# -*- coding: utf-8 -*-
"""
W-P.005 之預覽 PNG（單 §三 6）：自輸出之 DXF 讀回而繪（非自程式之內部資料）。

命令列：python verify/plots/preview_W-P005.py <成果目錄> <PNG 之輸出目錄> <退縮…>
輸出：每一退縮一檔 W-P.005_重劃後三圖層_退縮<t>m.png（左上：公告分配地籍線；右上：重劃後地號之 S 型之序〔示意〕；
      左下：分配後歸戶圖；右下：重劃後地價圖）。
預覽之標題與箭線唯供 KL 一眼辨圖層與編號之序，⛔ 屬 DXF 之內容（DXF 無標題·KL 17:48）。
"""
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

for _f in ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",):
    if os.path.exists(_f):
        font_manager.fontManager.addfont(_f)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=_f).get_name()

L_CAD, L_OWN, L_PRICE = "公告分配地籍線", "分配後歸戶圖", "重劃後地價圖"
NO_RE = re.compile(r"^\d+(-\d+)?$")


def _key(s):
    a = s.split("-")
    return (int(a[0]), int(a[1]) if len(a) > 1 else 0)


def _draw(ax, msp, layer, outlines, fs):
    for e in msp:
        if e.dxf.layer != layer:
            continue
        if e.dxftype() == "HATCH":
            for p in e.paths:
                xs = [v[0] for v in p.vertices]
                ys = [v[1] for v in p.vertices]
                ax.fill(xs, ys, color=tuple(c / 255 for c in e.rgb), linewidth=0)
        elif e.dxftype() == "TEXT":
            ax.text(e.dxf.align_point[0], e.dxf.align_point[1], e.dxf.text, ha="center", va="center", fontsize=fs)
    for pts in outlines:
        xs = [p[0] for p in pts] + [pts[0][0]]
        ys = [p[1] for p in pts] + [pts[0][1]]
        ax.plot(xs, ys, color="black", linewidth=0.6)


def maps_png(dxf_path, out_png, title):
    import ezdxf
    from shapely.geometry import Point, Polygon
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    outlines = [[(p[0], p[1]) for p in e.get_points("xy")]
                for e in msp if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == L_CAD]
    fig, axes = plt.subplots(2, 2, figsize=(24, 24))
    _draw(axes[0][0], msp, L_CAD, outlines, 5)
    axes[0][0].set_title(L_CAD + "（每宗：地號／面積／寬／深）", fontsize=16)
    # S 型之序之示意：每宗之地號之註記之位置，依地號之序連以箭線
    pts = []
    for pl in outlines:
        poly = Polygon(pl)
        nos = [t for t in msp.query(f'TEXT[layer=="{L_CAD}"]')
               if NO_RE.match(t.dxf.text) and poly.contains(Point(t.dxf.align_point[0], t.dxf.align_point[1]))]
        if len(nos) != 1:
            raise SystemExit(f"一宗之地號之註記非一（{len(nos)}）")
        c = poly.representative_point()
        pts.append((_key(nos[0].dxf.text), nos[0].dxf.text, c.x, c.y))
    pts.sort()
    ax = axes[0][1]
    for pl in outlines:
        xs = [p[0] for p in pl] + [pl[0][0]]
        ys = [p[1] for p in pl] + [pl[0][1]]
        ax.plot(xs, ys, color="0.6", linewidth=0.6)
    for (_, _, x0, y0), (_, _, x1, y1) in zip(pts, pts[1:]):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", color="tab:red", linewidth=1.2))
    for _, s, x, y in pts:
        ax.text(x, y, s, ha="center", va="center", fontsize=11, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="tab:red", lw=0.8))
    ax.set_title("重劃後地號之序（S 型·示意）", fontsize=16)
    _draw(axes[1][0], msp, L_OWN, outlines, 9)
    axes[1][0].set_title(L_OWN + "（歸戶號／抵費地）", fontsize=16)
    _draw(axes[1][1], msp, L_PRICE, outlines, 7)
    axes[1][1].set_title(L_PRICE + "（元／㎡）", fontsize=16)
    for a in axes.flat:
        a.set_aspect("equal")
        a.axis("off")
    fig.suptitle(title, fontsize=20)
    fig.tight_layout()
    fig.savefig(out_png, dpi=90)
    plt.close(fig)


def main(argv):
    src, out, *tags = argv
    os.makedirs(out, exist_ok=True)
    rc = 0
    for t in tags:
        p = os.path.join(out, f"W-P.005_重劃後三圖層_退縮{t}m.png")
        maps_png(os.path.join(src, f"公告圖_退縮{t}m.dxf"), p, f"W-P.005　重劃後三圖層（退縮 {t} m·示範資料）")
        sz = os.path.getsize(p)
        print(f"{p}\t{sz} bytes")
        rc |= int(sz == 0)
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
