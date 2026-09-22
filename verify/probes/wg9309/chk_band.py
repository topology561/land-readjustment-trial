# 發單側原型檢核（scratch）：強制帶（改後雙線形）vs 規定範圍多邊形之對稱差；SIDELINE 至帶遠側線之垂距
import contextlib, io, os, sys, json
import numpy as np
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3])
sys.path.insert(0, os.path.join(REPO, "verify"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
rec = {"cbs": [], "crp": {}}
_o = ns["_corner_buffer_S"]
def _cbs(block_poly, d_hat, front_p1, allocation_dir, range_area, side, tol=0.01, _label='', far_line_dir=None):
    buf = (_o(block_poly, d_hat, front_p1, allocation_dir, range_area, side, tol=tol, _label=_label) if far_line_dir is None else _o(block_poly, d_hat, front_p1, allocation_dir, range_area, side, tol=tol, _label=_label, far_line_dir=far_line_dir))
    rec["cbs"].append(dict(bp=block_poly, d=np.asarray(d_hat,float), p1=np.asarray(front_p1,float), ad=np.asarray(allocation_dir,float), ra=float(range_area), side=side, lbl=_label, fd=None if far_line_dir is None else np.asarray(far_line_dir,float), buf=buf))
    return buf
ns["_corner_buffer_S"] = _cbs
_olg = ns["_lot_gate"]
def _lg(res, tp, ctx, *a, **k):
    try:
        cs = k.get("chain_side"); lb = k.get("_label")
        cp = (ctx.get("corner_range_polys") or {}).get(cs)
        if cp is not None: rec["crp"][(lb, cs)] = cp
    except Exception: pass
    return _olg(res, tp, ctx, *a, **k)
ns["_lot_gate"] = _lg
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
try:
    with contextlib.redirect_stdout(io.StringIO()):
        run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
except RuntimeError as e:
    pass
slbs = fake_st.session_state.get('f3_cad_side_lines_by_side', {})
for c in rec["cbs"]:
    dom = ns["_strip_s_range"](c["bp"], c["d"], c["p1"], c["ad"]); s_min, s_max = float(dom[0]), float(dom[1])
    lo = max(s_min, 0.0); buf = c["buf"]
    a, b = (lo, buf) if c["side"] == 'left' else (s_max - buf, s_max)
    bpt = c["p1"] + a * c["d"]
    if c["fd"] is None:
        g, ar = ns["_block_strip"](c["bp"], c["d"], bpt, b - a, allocation_dir=c["ad"])
    else:
        fl = c["fd"] / np.linalg.norm(c["fd"]); al = c["ad"] / np.linalg.norm(c["ad"])
        if c["side"] == 'left':
            g, ar = ns["_block_strip"](c["bp"], c["d"], bpt, b - a, allocation_dir=c["ad"], n_hat_far=np.array([-fl[1], fl[0]]))
        else:
            g, ar = ns["_block_strip"](c["bp"], c["d"], bpt, b - a, allocation_dir=fl, n_hat_far=np.array([-al[1], al[0]]))
    crp = rec["crp"].get((c["lbl"], c["side"]))
    sd = float(g.symmetric_difference(crp).area) if (g is not None and crp is not None) else None
    sl = (slbs.get(c["lbl"]) or {}).get(c["side"]) or {}
    p1s = np.asarray(sl["p1"], float)[:2]; p2s = np.asarray(sl["p2"], float)[:2]; v = (p2s - p1s) / np.linalg.norm(p2s - p1s); nrm = np.array([-v[1], v[0]])
    inner = c["p1"] + buf * c["d"] if c["side"] == 'left' else c["p1"] + (s_max - buf) * c["d"]
    perp = abs(float(np.dot(inner - p1s, nrm)))
    print(json.dumps(dict(mode=MODE, sb=SB, lbl=c["lbl"], side=c["side"], range_area=c["ra"], buf=buf, band_area=float(ar), range_poly_area=(None if crp is None else float(crp.area)), symdiff=sd, perp_SIDELINE_to_inner=perp, two_line=c["fd"] is not None), ensure_ascii=False))
