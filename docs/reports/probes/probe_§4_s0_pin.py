# -*- coding: utf-8 -*-
"""§4 顯式釘準 s=0 原點＋末端帶參照（KL 要 <0.01 CAD-可重現）。R6：
   未臨正街三法對拍：(a) _block_strip strip s∈[smin,0]；(b) 直接半平面 clip {(p−p1)·û<0}；
   (c) 半平面用 CAD 原始 vertices（非 pipeline 處理後）。定位 Δ0.018 之源（構造 vs 資料）。"""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
REPO = r"C:/Users/admin/Desktop/land-readjustment-trial"
sys.path.insert(0, os.path.join(REPO, "verify")); os.chdir(os.path.join(REPO, "verify"))
import numpy as np
from shapely.geometry import Polygon
import run_verification as RV
from app_harvest import harvest
snap = json.load(open(RV.SNAPSHOT, encoding="utf-8")); ns, st = harvest()
cb_by, cad = RV.build_pipeline(ns, st, snap)
_ssr = ns["_strip_s_range"]; _bs = ns["_block_strip"]; aax = ns["alloc_normal_axis"]
def rot90(v): return np.array([-v[1], v[0]])
lbl = "R6"; blk = cb_by[lbl]; fl = cad["front_lines"][lbl]
polyP = Polygon(blk["vertices"]); polyP = polyP if polyP.is_valid else polyP.buffer(0)
p1 = np.array(fl["p1"], float); p2 = np.array(fl["p2"], float); d = (p2-p1)/np.linalg.norm(p2-p1)
ca = np.array(cad["alloc_dir_by_block"][lbl], float); ca /= np.linalg.norm(ca)
ad = np.array(aax(cad["alloc_dir_by_block"][lbl]), float)
smin, smax = _ssr(polyP, d, p1, ad)
# û = 半平面外向法向（s<0 側）：s(p)=(p−p1)·m̂/(d̂·m̂)·m̂=rot90(rot90(ad))... 用 rot90(ca) 定號
uhat = rot90(ca); cen = np.array(polyP.centroid.coords[0]); uhat = -uhat if np.dot(cen-p1, uhat) > 0 else uhat  # 指向 s<0（離centroid）
# (a) _block_strip
a_bs = float(_bs(polyP, d, p1+smin*d, -smin, allocation_dir=ad)[1])
# (b) 直接半平面 clip（大矩形 ∩ block）
B=1000.0; hp = Polygon([p1-B*ca, p1+B*ca, p1+B*ca+B*uhat, p1-B*ca+B*uhat])
a_hp = float(hp.intersection(polyP).area)
print(f"{lbl} 未臨正街：(a)_block_strip={a_bs:.4f}  (b)半平面clip={a_hp:.4f}  Δ(a−b)={a_bs-a_hp:+.4f}")
print(f"   claude.ai=85.6883·我(前)=85.7064；s=0 線＝過 p1={p1.tolist()} ∥cad_alloc={ca.round(4).tolist()}")
print(f"   末端帶參照線＝同 s=0 線（過 p1 ∥cad_alloc）·⊥法向 rot90(cad_alloc)往 centroid 平移 W=畸零寬")
