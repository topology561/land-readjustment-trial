# -*- coding: utf-8 -*-
"""§4 R_end 定案構造驗（未臨正街 s<0 ∪ ⊥ALLOCLINE 平移帶 W=畸零寬）·三塊·union 非疊加。"""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
REPO = r"C:/Users/admin/Desktop/land-readjustment-trial"
sys.path.insert(0, os.path.join(REPO, "verify")); os.chdir(os.path.join(REPO, "verify"))
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union
import run_verification as RV
from app_harvest import harvest
snap = json.load(open(RV.SNAPSHOT, encoding="utf-8")); ns, st = harvest()
cb_by, cad = RV.build_pipeline(ns, st, snap)
_ssr = ns["_strip_s_range"]; _bs = ns["_block_strip"]; aax = ns["alloc_normal_axis"]; gm = ns["get_min_lot_size"]
def rot90(v): return np.array([-v[1], v[0]])
for lbl in ("R1", "R3", "R6"):
    blk = cb_by[lbl]; fl = cad["front_lines"][lbl]
    poly = Polygon(blk["vertices"]); poly = poly if poly.is_valid else poly.buffer(0)
    p1 = np.array(fl["p1"], float); p2 = np.array(fl["p2"], float); d = (p2-p1)/np.linalg.norm(p2-p1)
    ca = np.array(cad["alloc_dir_by_block"][lbl], float); ca /= np.linalg.norm(ca)
    ad = np.array(aax(cad["alloc_dir_by_block"][lbl]), float)
    smin, smax = _ssr(poly, d, p1, ad)
    mw = float(gm(blk["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
    # 未臨正街 = block ∩ {s<0}
    wai = _bs(poly, d, p1+smin*d, -smin, allocation_dir=ad)[0] if smin < -1e-9 else None
    # 末端帶 = ⊥ALLOCLINE 平移帶（過 p1·法向 rot90(ca) 往街廓內·W=mw）
    n = rot90(ca); n = n if np.dot(np.array(poly.centroid.coords[0])-p1, n) > 0 else -n
    B = 500.0
    band = Polygon([p1-B*ca, p1+B*ca, p1+B*ca+mw*n, p1-B*ca+mw*n]).intersection(poly)
    parts = [g for g in (wai, band) if g is not None and not g.is_empty]
    rend = unary_union(parts)
    wa = float(wai.area) if wai else 0.0
    print(f"{lbl}: 未臨正街(s<0)={wa:8.4f} ＋ 末端帶(⊥W={mw})={float(band.area):8.4f} → R_end∪={float(rend.area):8.4f}"
          + (f"  [R6錨252.28 Δ={float(rend.area)-252.28:+.3f}]" if lbl=="R6" else ""))
