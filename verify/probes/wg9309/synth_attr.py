# 發單側原型檢核（scratch）：右側分支之合成例（甲-3）——強制帶 vs 解析之規定範圍（SIDELINE 內移 D）
import os, sys, io, contextlib, math
import numpy as np
from shapely.geometry import Polygon, LineString
from shapely import affinity
REPO=sys.argv[1]
sys.path.insert(0, os.path.join(REPO,"verify"))
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns,_ = harvest(os.path.join(REPO,"app.py"))
def unit(v): v=np.asarray(v,float); return v/np.linalg.norm(v)
def case(side, side_tilt_deg, alloc_tilt_deg, D, fd_sign):
    # FRONT 沿 x 軸 (0,0)→(60,0)；深 30；SIDELINE 在 side 端，傾 side_tilt
    t=math.radians(side_tilt_deg)
    if side=='right':
        s0=np.array([60.0,0.0]); s1=s0+30*np.array([math.tan(t),1.0])
        blk=Polygon([(0,0),tuple(s0),tuple(s1),(0,30)])
    else:
        s0=np.array([0.0,0.0]); s1=s0+30*np.array([math.tan(t),1.0])
        blk=Polygon([tuple(s0),(60,0),(60,30),tuple(s1)])
    sv=unit(s1-s0)                                   # SIDE 線向
    nrm=np.array([sv[1],-sv[0]]) if side=='left' else np.array([-sv[1],sv[0]])  # 指向街廓內
    nrm = nrm if np.dot(nrm, np.array(blk.centroid.coords[0])-s0)>0 else -nrm
    # 解析之規定範圍：街廓 ∩ {距 SIDELINE ≤ D}
    big=1e4
    p=s0+D*nrm
    hp=Polygon([tuple(s0-big*sv),tuple(s0+big*sv),tuple(p+big*sv),tuple(p-big*sv)])
    rng=blk.intersection(hp)
    a=math.radians(alloc_tilt_deg); allocation_dir=np.array([math.cos(a),math.sin(a)])   # ⊥ ALLOC 線
    d_hat=np.array([1.0,0.0]); front_p1=np.array([0.0,0.0])
    fd=fd_sign*np.array([sv[1],-sv[0]])              # ⊥ SIDE（±）
    with contextlib.redirect_stdout(io.StringIO()):
        buf=ns["_corner_buffer_S"](blk,d_hat,front_p1,allocation_dir,float(rng.area),side,_label='synth',far_line_dir=fd)
        g,ar=ns["_corner_band_geom"](blk,d_hat,front_p1,allocation_dir,buf,side,far_line_dir=fd)
    sd=g.symmetric_difference(rng).area
    dom=ns['_strip_s_range'](blk,d_hat,front_p1,allocation_dir)
    return dict(s_min=float(dom[0]),s_max=float(dom[1]),side=side,side_tilt=side_tilt_deg,alloc_tilt=alloc_tilt_deg,D=D,fd_sign=fd_sign,range=round(rng.area,6),band=round(ar,6),buf=round(buf,6),symdiff=sd)

from collections import Counter
cnt=Counter()
for side in ('left','right'):
    for st in (-6.0,-2.7,2.7,6.0):
        for at in (0.0,3.0,-4.0):
            for sg in (1,-1):
                r=case(side,st,at,7.0,sg)
                bad=r['symdiff']>1e-3
                neg=(r['s_min']<-1e-9) if side=='left' else (r['s_max']>60+1e-9)
                cnt[(side,'bad' if bad else 'ok','s_min<0' if (side=='left' and r['s_min']<-1e-9) else 's_min>=0')]+=1
                mx=max(cnt.get('mx',0), r['symdiff'] if not bad else 0)
print(dict(cnt))
