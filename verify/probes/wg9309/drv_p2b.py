# 發單側原型驅動器（scratch·不入倉）：一（態·情境）→ 逐宗列 + forced 資訊
import contextlib, io, os, sys, json
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3]); OUT = sys.argv[4]
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
spy = {"cbs": [], "slot": []}
_o_cbs = ns["_corner_buffer_S"]
def _cbs(*a, **k):
    r = _o_cbs(*a, **k); spy["cbs"].append({"label": k.get("_label"), "side": a[5] if len(a) > 5 else k.get("side"), "range": a[4] if len(a) > 4 else k.get("range_area"), "buf": r}); return r
ns["_corner_buffer_S"] = _cbs
_o_slot = ns["_select_pool_slot"]
def _slot(w, l, r, *a, **k):
    out = _o_slot(w, l, r, *a, **k)
    f = sys._getframe(1).f_locals
    spy["slot"].append({"blk": f.get("blk_label"), "widths": list(w), "bL": l.get("b"), "bR": r.get("b"), "k": out.get("k") if isinstance(out, dict) else None}); return out
ns["_select_pool_slot"] = _slot
_o_ps = ns["_pool_strips_for_block"]
spy["xover"] = []
def _ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    fb = list(forced_bands or [])
    bad = [round(sum(b.intersection(p).area for p in biz_polys if p is not None), 6) for b in fb]
    if any(x > 1e-6 for x in bad):
        spy["xover"].append({"blk": _label, "band_owner_overlap": bad})
        fb = [b for b, x in zip(fb, bad) if x <= 1e-6]      # 量測用：交叉之帶退回 P1 行為（loud 記錄）
    return _o_ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, forced_bands=fb)
ns["_pool_strips_for_block"] = _ps
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
err = None
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
    g_rows = sg["g_rows"]
except RuntimeError as e:
    err = str(e).split("\n")[0][:300]; g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
KEEP = None
rows = []
for r in g_rows:
    d = {}
    for k, v in r.items():
        if k == "cut_coords":
            try: d[k] = [[float(a), float(b)] for a, b in v] if v and not isinstance(v, str) else v
            except Exception: d[k] = str(v)
        else:
            try: json.dumps(v); d[k] = v
            except Exception: d[k] = str(v)
    rows.append(d)
json.dump({"mode": MODE, "sb": SB, "err": err, "forced": str(forced)[:2000], "off": str(_off)[:2000], "rows": rows, "cbs": spy["cbs"], "slot": spy["slot"], "xover": spy["xover"], "log_tail": buf.getvalue()[-3000:]}, open(OUT, "w"), ensure_ascii=False, default=str)
print("OK", MODE, SB, "rows", len(rows), "err", (err or "")[:60], "cbs", len(spy["cbs"]), "xover", spy["xover"][:2])
