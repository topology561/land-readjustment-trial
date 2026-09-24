# 發單側量測器（倉外）：乙態、退縮 SB，指定街廓內同歸戶諸宗之兩兩直接相鄰（k6_shares_segment）、
# 投影序、個別原位次之實跑列與剔除紀錄。受詞宗由參數給（⛔ 寫死於生產碼；本器為量測用）。
import contextlib, io, os, sys, json, copy
sys.stdout.reconfigure(encoding="utf-8")
REPO = sys.argv[1]; SB = float(sys.argv[2]); BLK = sys.argv[3]; KEYS = sys.argv[4].split(",")
os.environ["WV_K6_STEP0"] = "off"
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
from shapely.geometry import Polygon
with contextlib.redirect_stdout(io.StringIO()):
    ns, fake_st = harvest(os.path.join(REPO, "app.py"))
    snapshot = rv.load_snapshot(); cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    v6 = open(rv.V6DXF, "rb").read()
    temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
om = fake_st.session_state['t8_ownership_map']
P = {t['暫編地號']: t for t in temp_p}
poly = {k: (lambda q: q if q.is_valid else q.buffer(0))(Polygon(P[k]['polygon_coords'])) for k in KEYS}
print('歸戶', {k: om.get(P[k]['原地號']) for k in KEYS}, '街廓', {k: P[k]['所屬街廓'] for k in KEYS})
for i, a in enumerate(KEYS):
    for b in KEYS[i + 1:]:
        print('相鄰', a, b, ns['k6_shares_segment'](poly[a], poly[b])[0])
with contextlib.redirect_stdout(io.StringIO()):
    diag, sel, off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
ns["K917_DROPPED"].clear()
with contextlib.redirect_stdout(io.StringIO()):
    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
rows = [r for r in sg["g_rows"] if r.get('所屬街廓') == BLK]
print('wins', wins.get(BLK), 'forced', {k: forced.get(BLK, {}).get(k) for k in ('left_forced_offset', 'right_forced_offset')})
for r in rows:
    print('列', {k: r.get(k) for k in ('暫編地號', '推進側別', 'a 面積(㎡)', 'G(㎡)', '宗地寬度(m)', '驗_總判', '驗_宗序', '第1筆街角')})
for k, v in ns["K917_DROPPED"].items():
    if k[0] == BLK:
        for d in v:
            dd = {kk: (vv if isinstance(vv, (int, float, str, bool)) or vv is None else str(vv)[:80]) for kk, vv in d.items()}
            print('剔除', k, json.dumps(dd, ensure_ascii=False)[:600])
