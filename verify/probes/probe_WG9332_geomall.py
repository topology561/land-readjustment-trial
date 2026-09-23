import json, os, sys
REPO, OUT = sys.argv[1], sys.argv[2]
os.chdir(REPO); sys.path.insert(0, os.path.join(REPO, "verify"))
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import build_build_parcels
snapshot = rv.load_snapshot()
ns, fake_st = harvest()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
v6 = open(rv.V6DXF, "rb").read()
temp, build, _ = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
blk = {}
for k, b in cb_by.items():
    geo = {kk: vv for kk, vv in b.items() if isinstance(vv, (list, tuple)) and vv and isinstance(vv[0], (list, tuple))}
    sc = {kk: vv for kk, vv in b.items() if isinstance(vv,(int,float,str))}
    blk[k] = {"scalars": sc, "geo": geo}
keys=set()
for tp in temp: keys|=set(tp.keys())
json.dump({"blocks": blk, "parcel_keys": sorted(keys), "parcels":[{k:v for k,v in tp.items() if isinstance(v,(int,float,str,list,type(None)))} for tp in temp], "snap_keys": sorted(snapshot.keys())},
          open(OUT,"w",encoding="utf-8"), ensure_ascii=False, default=str)
print("ok", len(temp), len(build), len(cb_by))
