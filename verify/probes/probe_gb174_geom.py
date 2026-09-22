# -*- coding: utf-8 -*-
"""發單側（窗二十四·唯讀·⛔ 零生產碼）：GB-174 附圖之幾何取出。
用法：python probe_gb174_geom.py <repo 絕對> <出艙 json 絕對>"""
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
    blk[k] = {"keys": sorted(b.keys()), "label": b.get("label", k), "category": b.get("category"), "geo": geo}
tgt = [tp for tp in temp if str(tp.get("原地號")) in ("628-42", "628-27", "628-53")]
json.dump({"blocks": blk, "parcels": [{k: tp.get(k) for k in ("暫編地號", "原地號", "所屬街廓", "街廓分類", "polygon_coords", "面積_m2", "分攤登記面積_m2", "幾何面積_m2", "登記面積_m2")} for tp in tgt],
           "n_temp": len(temp), "n_build": len(build)}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, default=str)
print("ok", len(tgt))
