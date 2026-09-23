import contextlib, io, os, sys, json, copy, time
sys.stdout.reconfigure(encoding="utf-8")
REPO=sys.argv[1]; SB=float(sys.argv[2]); os.environ["WV_K6_STEP0"]="off"
sys.path.insert(0, os.path.join(REPO,"verify")); sys.path.insert(0, os.path.join(REPO,"verify","probes"))
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from shapely.geometry import Polygon
with contextlib.redirect_stdout(io.StringIO()):
    ns,fake_st=harvest(os.path.join(REPO,"app.py"))
    snapshot=rv.load_snapshot(); cb_by,cad=rv.build_pipeline(ns,fake_st,snapshot)
    rv.build_ownership(ns,fake_st,rv.ANON_XLSX)
    v6=open(rv.V6DXF,"rb").read()
    temp_p,build_p,_=rv.build_build_parcels(ns,fake_st,v6,list(cb_by.values()),snapshot)
    params=rv.build_param_table(ns,fake_st,cb_by,cad,snapshot,SB)
ss=fake_st.session_state; om=ss['t8_ownership_map']
def pk(tp,bp):
    with contextlib.redirect_stdout(io.StringIO()):
        return run_corner_pk(ns,fake_st,list(cb_by.values()),cad,params,tp,bp,SB,snapshot=snapshot)
t0=time.time(); diag,sel,off,wins,forced=pk(temp_p,build_p); print('pk sec',round(time.time()-t0,1))
order=list(ss['f3_k6b_stage2_order']); locks={p for v in ss['f3_k6b_stage1_locked_by_block'].values() for p in v}
thr={}
for d in diag: thr[(d['街廓'],d['端'])]=d['門檻(㎡)']
P=[]
for p in temp_p:
    q=dict(p); poly=Polygon(p['polygon_coords']); q['polygon']=poly if poly.is_valid else poly.buffer(0); P.append(q)
idx={p['暫編地號']:i for i,p in enumerate(P)}
groups=ns['k6_merge_groups'](P,om); gof={}
for gi,g in enumerate(groups):
    for i in g: gof[i]=gi
def a(i): return round(float(P[i].get('分攤登記面積_m2') or 0)+float(P[i].get('面積_m2') or 0),2)
zof=snapshot["財務接線_v3"]["原地號_區段"]; pz=snapshot["財務接線_v3"]["重劃前區段_面積單價"]
def price(i): return float(pz[zof[P[i]['原地號']]]['單價_元每m2'])
def sameblock_comp(ci, members):
    blk=P[ci]['所屬街廓']; S={ci}; stk=[ci]
    cand=[m for m in members if P[m]['所屬街廓']==blk]
    while stk:
        u=stk.pop()
        for v in cand:
            if v not in S and ns['k6_shares_segment'](P[u]['polygon'],P[v]['polygon'])[0]:
                S.add(v); stk.append(v)
    return S-{ci}
def trial(ci, extra):
    tp=copy.deepcopy(temp_p); byid={t['暫編地號']:t for t in tp}
    bp=[byid[b['暫編地號']] for b in build_p]
    pt=price(ci); add=sum(a(j)*price(j)/pt for j in extra)
    byid[P[ci]['暫編地號']]['分攤登記面積_m2']=round(float(byid[P[ci]['暫編地號']]['分攤登記面積_m2'])+add,2)
    d2,s2,o2,w2,f2=pk(tp,bp)
    k=P[ci]['暫編地號']; blk=P[ci]['所屬街廓']
    g=[d for d in d2 if d['候選地號']==k]
    win=w2[blk]
    return round(a(ci)+add,2), {d['端']:d['真G(㎡)'] for d in g}, win
res=[]
for o in order:
    ci=idx[o['暫編地號']]; gi=gof.get(ci); members=[m for m in (groups[gi] if gi is not None else []) if m!=ci and P[m]['暫編地號'] not in locks]
    S=sameblock_comp(ci,members)
    PUB=[m for m in members if P[m]['所屬街廓'].startswith(('RD','G'))]
    OTH=[m for m in members if m not in S and m not in PUB]
    row={'序':o['最終序位'],'街廓':o['街廓'],'端':o['端'],'候選':o['暫編地號'],'門檻':thr[(o['街廓'],o['端'])],'單獨G':o['街角試算G(㎡)'],
         '歸戶':om.get(P[ci]['原地號']),'同街廓':[P[m]['暫編地號'] for m in S],'公設道路':[(P[m]['暫編地號'],a(m)) for m in PUB],'他街廓':[(P[m]['暫編地號'],P[m]['所屬街廓']) for m in OTH]}
    for tag,ext in (('A',S),('B',set(S)|set(PUB)),('C',set(members))):
        if not ext: row[tag]=None; continue
        ae,g,win=trial(ci,ext); row[tag]={'a':ae,'G':g.get(o['端']),'win':win}
    res.append(row); print(json.dumps(row,ensure_ascii=False))
json.dump(res,open(f'/home/claude/r/st3_{SB}.json','w',encoding='utf-8'),ensure_ascii=False)
