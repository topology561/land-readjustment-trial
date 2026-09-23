# 段三物化試作（拋棄式·發單側量測器）：依情境改 parcels 之 a 並移除被併宗，重跑街角評定與配地（原型 v2 樹）
import contextlib, io, os, sys, json, copy
sys.stdout.reconfigure(encoding="utf-8")
REPO=sys.argv[1]; SCN=sys.argv[2]; SB=3.5; OUT=sys.argv[3]
os.environ["WV_K6_STEP0"]="off"
sys.path.insert(0, os.path.join(REPO,"verify")); sys.path.insert(0, os.path.join(REPO,"verify","probes"))
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
from shapely.geometry import Polygon
with contextlib.redirect_stdout(io.StringIO()):
    ns,fake_st=harvest(os.path.join(REPO,"app.py"))
    snapshot=rv.load_snapshot(); cb_by,cad=rv.build_pipeline(ns,fake_st,snapshot)
    rv.build_ownership(ns,fake_st,rv.ANON_XLSX)
    v6=open(rv.V6DXF,"rb").read()
    temp_p,build_p,_=rv.build_build_parcels(ns,fake_st,v6,list(cb_by.values()),snapshot)
    params=rv.build_param_table(ns,fake_st,cb_by,cad,snapshot,SB)
tp=copy.deepcopy(temp_p); byid={t['暫編地號']:t for t in tp}
bp=[byid[b['暫編地號']] for b in build_p]
a=lambda k: float(byid[k]['分攤登記面積_m2'])
half_rd2=(a('628-45(5)')+a('628-30(4)'))/2; half_pub=(a('628-45(4)')+a('628-45(3)'))/2
plan={'S0':{'628-45(2)':['628-30(3)'],'628-45(1)':['628-20(2)','628-30(1)'],'628-41(1)':['628-41(2)','628-41(3)']},
      'S1':{'628-45(2)':['628-30(3)','628-30(2)'],'628-45(1)':['628-20(2)','628-30(1)'],'628-41(1)':['628-41(2)','628-41(3)']}}[SCN]
extra={'S0':{},'S1':{'628-45(2)':half_rd2+half_pub,'628-45(1)':half_rd2+half_pub}}[SCN]
removed=set()
for t,ms in plan.items():
    add=sum(a(m) for m in ms)+extra.get(t,0.0)   # 本案同區段 ⇒ a′＝a
    byid[t]['分攤登記面積_m2']=round(a(t)+add,2); removed|=set(ms)
bp=[b for b in bp if b['暫編地號'] not in removed]
with contextlib.redirect_stdout(io.StringIO()):
    diag,sel,off,wins,forced=run_corner_pk(ns,fake_st,list(cb_by.values()),cad,params,tp,bp,SB,snapshot=snapshot)
ns["K917_DROPPED"].clear(); err=None
with contextlib.redirect_stdout(io.StringIO()):
    try:
        sg=run_step_g(ns,fake_st,list(cb_by.values()),cad,snapshot,params,bp,wins,forced,SB,eff_min_build_by_blk={}); rows=sg["g_rows"]
    except RuntimeError as e:
        err=str(e).split("\n")[0][:300]; rows=(getattr(e,"partial",None) or {}).get("g_rows") or []
dropped={f"{k[0]}/{k[1]}":sorted({d['暫編地號'] for d in v}) for k,v in ns["K917_DROPPED"].items()}
pools=[]
for r in rows:
    if '抵費地' in str(r.get('暫編地號')) and r.get('cut_coords'):
        P=Polygon(r['cut_coords']).buffer(0); blk=r['所屬街廓']; prow=[p for p in params if p['街廓']==blk][0]
        ms=ns['get_min_lot_size'](cb_by[blk].get('category',''),float(prow.get('正面路寬(m)',0) or 0))
        det={}; ok=ns['_rect_fits_free_pose'](P,float(ms['min_width']),float(ms['min_depth']),_detail=det)
        pools.append({'池':r['暫編地號'],'面積':round(P.area,2),'W':ms['min_width'],'D':ms['min_depth'],'容納內接矩形':bool(ok)})
out={'scn':SCN,'err':err,'wins':wins,'forced':{k:{kk:v[kk] for kk in ('left_forced_offset','right_forced_offset')} for k,v in forced.items()},
     'rows':[{**{k:r.get(k) for k in ('暫編地號','所屬街廓','推進側別','a 面積(㎡)','G(㎡)','驗_總判','第1筆街角','驗_宗序')},'cc':(list(Polygon(r['cut_coords']).buffer(0).centroid.coords)[0] if r.get('cut_coords') and not isinstance(r.get('cut_coords'),str) else None)} for r in rows],
     'dropped':dropped,'pools':pools,'half_rd2':half_rd2,'half_pub':half_pub}
json.dump(out,open(OUT,'w',encoding='utf-8'),ensure_ascii=False,default=str)
print(json.dumps({'scn':SCN,'err':err,'n':len(rows),'pools':pools,'dropped':dropped},ensure_ascii=False))
