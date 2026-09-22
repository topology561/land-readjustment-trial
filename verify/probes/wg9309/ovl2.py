# 發單側原型檢核（scratch）：強制帶（雙線）與業主宗之重疊（逐宗）
import contextlib, io, os, sys, json
REPO=sys.argv[1]; MODE=sys.argv[2]; SB=float(sys.argv[3])
sys.path.insert(0, os.path.join(REPO,"verify"))
if MODE=="甲": os.environ.pop("WV_K6_STEP0",None)
else: os.environ["WV_K6_STEP0"]="off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO,"app.py"))
cap=[]
_o=ns["_pool_strips_for_block"]
def _p(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    if forced_bands:
        cap.append((_label, [p for p in biz_polys], list(forced_bands), block_poly))
    return _o(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, forced_bands=forced_bands)
ns["_pool_strips_for_block"]=_p
snapshot=rv.load_snapshot()
cb_by,cad=rv.build_pipeline(ns,fake_st,snapshot)
rv.build_ownership(ns,fake_st,rv.ANON_XLSX)
v6=open(rv.V6DXF,"rb").read()
temp_p,build_p,_=rv.build_build_parcels(ns,fake_st,v6,list(cb_by.values()),snapshot)
params=rv.build_param_table(ns,fake_st,cb_by,cad,snapshot,SB)
_d,_s,_off,wins,forced=run_corner_pk(ns,fake_st,list(cb_by.values()),cad,params,temp_p,build_p,SB,snapshot=snapshot)
try:
    with contextlib.redirect_stdout(io.StringIO()):
        run_step_g(ns,fake_st,list(cb_by.values()),cad,snapshot,params,build_p,wins,forced,SB,eff_min_build_by_blk={})
except RuntimeError as e:
    print("RuntimeError:", str(e)[:160])
seen=set()
for lbl,biz,fb,bp in cap:
    key=(lbl, round(sum(p.area for p in biz),6))
    if key in seen: continue
    seen.add(key)
    import pickle; pickle.dump((lbl,biz,fb,bp),open(f"cap_{MODE}_{SB}_{lbl}.pkl","wb"))
    for k,b in enumerate(fb):
        ov=[(i, round(p.area,4), round(b.intersection(p).area,4)) for i,p in enumerate(biz) if b.intersection(p).area>1e-6]
        print(json.dumps(dict(mode=MODE,sb=SB,blk=lbl,band_area=round(b.area,4),n_biz=len(biz),overlaps=ov,sum_ov=round(sum(x[2] for x in ov),6)),ensure_ascii=False))
