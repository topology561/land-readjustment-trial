# 發單側原型檢核（scratch·不入倉）：P3 之四閘（綁土地性質·⛔ 綁中間量）
#  ① 強制抵費地之物化形 ≡ 規定範圍多邊形（對稱差 ≤ 0.005 ㎡）
#  ② 強制帶 ∩ 全部業主宗 ≤ 1e-6 ㎡
#  ③ 業主宗兩兩不重疊（≤ 1e-6）且皆為有效多邊形；強制側緊鄰宗之藍影判與臨接長
#  ④ 街廓面積守恆（全部列之聯集 ≡ 街廓·Σ 面積 ≡ 街廓面積）
# 用法：python3 chk_p3.py <repo> <甲|乙> <0.0|3.5> <out.json>
import contextlib, io, os, sys, json
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3]); OUT = sys.argv[4]
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from shapely.geometry import Polygon
from shapely.ops import unary_union
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
cap = {}; crp = {}
_o_ps = ns["_pool_strips_for_block"]
def _ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    cap[_label] = dict(block=block_poly, bands=list(forced_bands or []))
    _kw = {} if forced_bands is None else {"forced_bands": forced_bands}
    return _o_ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, **_kw)
ns["_pool_strips_for_block"] = _ps
_olg = ns["_lot_gate"]
def _lg(res, tp, ctx, *a, **k):
    cp = (ctx.get("corner_range_polys") or {}).get(k.get("chain_side"))
    if cp is not None: crp[(k.get("_label"), k.get("chain_side"))] = cp
    return _olg(res, tp, ctx, *a, **k)
ns["_lot_gate"] = _lg
ns["K917_DROPPED"].clear()
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
err = None
with contextlib.redirect_stdout(io.StringIO()):
    try:
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
        g_rows = sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:300]; g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
dropped = {f"{k[0]}/{k[1]}": v for k, v in ns["K917_DROPPED"].items()}
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
def poly(r):
    c = r.get("cut_coords")
    return Polygon(c) if isinstance(c, list) and len(c) >= 3 else None
G = {"err": err, "dropped": dropped, "blocks": {}}
for blk, c in cap.items():
    R = [r for r in rows if r["所屬街廓"] == blk]
    own = [(r["暫編地號"], poly(r)) for r in R if r["推進側別"] in ("left", "right")]
    pools = [(r["暫編地號"], poly(r)) for r in R if r["推進側別"] == "抵費地"]
    allp = [p for _, p in own + pools if p is not None]
    bg = {}
    bg["n_own"] = len(own); bg["n_pool"] = len(pools)
    bg["own_invalid"] = [k for k, p in own if p is None or not p.is_valid]
    ov = []
    for i in range(len(own)):
        for j in range(i + 1, len(own)):
            a, b = own[i][1], own[j][1]
            if a is not None and b is not None:
                x = a.intersection(b).area
                if x > 1e-6: ov.append((own[i][0], own[j][0], round(x, 6)))
    bg["own_own_overlap"] = ov
    bl = c["block"]
    bg["block_area"] = round(bl.area, 6); bg["sum_rows"] = round(sum(p.area for p in allp), 6)
    bg["union_symdiff_block"] = round(unary_union(allp).symmetric_difference(bl).area, 6) if allp else None
    bands = []
    for bnd in c["bands"]:
        side = None; best = None
        for (lb, sd), cp in crp.items():
            if lb == blk:
                x = bnd.symmetric_difference(cp).area
                if best is None or x < best: best, side = x, sd
        mat = [(k, p) for k, p in pools if p is not None and p.intersection(bnd).area > 0.5 * bnd.area]
        mp = mat[0][1] if len(mat) == 1 else None
        rng = crp.get((blk, side))
        bands.append(dict(side=side, band_area=round(bnd.area, 6),
                          mat_piece=[k for k, _ in mat], mat_area=(None if mp is None else round(mp.area, 6)),
                          range_area=(None if rng is None else round(rng.area, 6)),
                          g1_symdiff_mat_range=(None if (mp is None or rng is None) else round(mp.symmetric_difference(rng).area, 6)),
                          g2_band_owner=[(k, round(p.intersection(bnd).area, 6)) for k, p in own if p is not None and p.intersection(bnd).area > 1e-6]))
    bg["bands"] = bands
    adj = [dict(k=r["暫編地號"], side=r["推進側別"], G=r["G(㎡)"], 序=r.get("驗_宗序"), B=r.get("驗_B藍影"),
                藍影=r.get("驗_B_藍影面積"), 正街=r.get("驗_B_臨正街"), 屁股=r.get("驗_B_臨屁股"),
                nv=(None if poly(r) is None else len(poly(r).exterior.coords) - 1))
           for r in R if r.get("驗_宗序") in ("第2宗", "街角第1宗")]
    bg["checked_lots"] = adj
    G["blocks"][blk] = bg
json.dump({"mode": MODE, "sb": SB, "err": err, "rows": rows, "gates": G}, open(OUT, "w"), ensure_ascii=False, default=str)
print(json.dumps({"mode": MODE, "sb": SB, "err": (err or "")[:120], "n_rows": len(rows), "dropped": dropped}, ensure_ascii=False, default=str))
for blk, bg in G["blocks"].items():
    flag = []
    if bg["own_invalid"]: flag.append("invalid")
    if bg["own_own_overlap"]: flag.append("own-ov")
    if bg["union_symdiff_block"] is not None and bg["union_symdiff_block"] > 1e-3: flag.append("union≠block")
    for b in bg["bands"]:
        if b["g1_symdiff_mat_range"] is None or b["g1_symdiff_mat_range"] > 0.005: flag.append("g1")
        if b["g2_band_owner"]: flag.append("g2")
    print(blk, "OK" if not flag else flag, "blk", bg["block_area"], "Σ", bg["sum_rows"], "∪Δ", bg["union_symdiff_block"],
          "bands", [(b["side"], b["band_area"], b["mat_piece"], b["mat_area"], b["range_area"], b["g1_symdiff_mat_range"], b["g2_band_owner"]) for b in bg["bands"]])
    for a in bg["checked_lots"]:
        print("   ", a)
