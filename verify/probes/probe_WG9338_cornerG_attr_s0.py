# -*- coding: utf-8 -*-
# `W-G.9-338`：街角第 1 宗之「評定 G」（run_corner_pk → _corner_first_lot_G）與「配地實跑 G」（run_step_g）之差，逐輸入歸因。
# 情境 ＝ 純生產路徑（⛔ 物化），態由參數給（on ⇒ 甲／off ⇒ 乙），退縮 SB 由參數給。
# 法：包裹 ns["_solve_G_one"] 攔二路徑之 is_corner=True 呼叫；以（a_m2、side）配對；**實跑側取「G 與該宗列值相符」之末次呼叫**
#     （同一宗可有多次求解·`自誤 515`：取首次者其「全換重現」只證重現被攔之值、⛔ 證重現列值）；
#     逐鍵單換、全換（須重現實跑 G ⇒ 器非紅之證）。
# 🔒 閘（器紅 ⇒ rc 6）：① 每一配對之攔得 G 四捨五入至 2 位 ＝ 列值；② 全換重現；③ `_corner_first_lot_G.__globals__ is ns`。
# 🔒 rc（器非紅時）＝ 非強制側之街角第 1 宗中，|差| > 0.005 且「單換非零之鍵」⛔ 恰為 {S_max} 者之數。
#     S_max 類（求解區間上界之別·二分精度）另計、⛔ 入 rc；強制側（該端為強制抵費地）另列、⛔ 入 rc（`GB-170` 族·設計上本不同）。
# 本檔 ＝ 上器之 S0 物化版（plan ＝ verify/probes/probe_WG9333_k6s3_mat.py 之 S0 逐字·態乙）。
# 用法：python probe_WG9338_cornerG_attr_s0.py <repo> <SB> <out.json>
import contextlib, io, os, sys, json, copy
import numpy as np
sys.stdout.reconfigure(encoding="utf-8")
REPO = sys.argv[1]; SB = float(sys.argv[2]); OUT = sys.argv[3]
os.environ["WV_K6_STEP0"] = "off"
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
with contextlib.redirect_stdout(io.StringIO()):
    ns, fake_st = harvest(os.path.join(REPO, "app.py"))
    snapshot = rv.load_snapshot(); cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    v6 = open(rv.V6DXF, "rb").read()
    temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
tp = copy.deepcopy(temp_p); byid = {t['暫編地號']: t for t in tp}
bp = [byid[b['暫編地號']] for b in build_p]
a = lambda k: float(byid[k]['分攤登記面積_m2'])
plan = {'628-45(2)': ['628-30(3)'], '628-45(1)': ['628-20(2)', '628-30(1)'], '628-41(1)': ['628-41(2)', '628-41(3)']}  # ＝ mat S0 逐字
removed = set()
for t, ms in plan.items():
    byid[t]['分攤登記面積_m2'] = round(a(t) + sum(a(m) for m in ms), 2); removed |= set(ms)
bp = [b for b in bp if b['暫編地號'] not in removed]
orig = ns["_solve_G_one"]; CALLS = []; PHASE = {'p': None}
def wrap(**kw):
    r = orig(**kw)
    if kw.get('is_corner'):
        CALLS.append({'phase': PHASE['p'], 'kw': copy.deepcopy(kw), 'G': float(r[0].get('G', 0) or 0), 'solver': r[1], 'res': {k: r[0].get(k) for k in ('S_raw','W','W_near','W_rw_start_raw','area_geom','G')}})
    return r
ns["_solve_G_one"] = wrap
# 🔴 器非紅之前提：_corner_first_lot_G 之全域須即 ns（否則評定路徑攔不到）
assert ns["_corner_first_lot_G"].__globals__ is ns, "評定路徑之全域非 ns ⇒ 攔截失效"
PHASE['p'] = 'pk'
with contextlib.redirect_stdout(io.StringIO()):
    diag, sel, off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, tp, bp, SB, snapshot=snapshot)
PHASE['p'] = 'sg'; ns["K917_DROPPED"].clear()
with contextlib.redirect_stdout(io.StringIO()):
    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp, wins, forced, SB, eff_min_build_by_blk={})
rows = sg["g_rows"]
ns["_solve_G_one"] = orig

def same(x, y):
    if x is None or y is None: return x is y
    try:
        ax, ay = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
        return ax.shape == ay.shape and bool(np.allclose(ax, ay, rtol=0, atol=1e-9))
    except Exception:
        return x == y
def show(v):
    try:
        arr = np.asarray(v, dtype=float)
        return [round(float(t), 6) for t in arr.ravel()] if arr.ndim else round(float(arr), 6)
    except Exception:
        return str(v)[:60]
def G_of(kw):
    return float(orig(**kw)[0].get('G', 0) or 0)

firsts = [r for r in rows if r.get('第1筆街角') == '是']
out = []
for r in firsts:
    k = r['暫編地號']; am = round(float(r['a 面積(㎡)']), 2); sd = {'left': '左側', 'right': '右側'}[r['推進側別']]
    sgc = [c for c in CALLS if c['phase'] == 'sg' and round(float(c['kw']['a_m2']), 2) == am and c['kw']['side'] == sd]
    pkc = [c for c in CALLS if c['phase'] == 'pk' and round(float(c['kw']['a_m2']), 2) == am and c['kw']['side'] == sd]
    rec = {'宗': k, '街廓': r['所屬街廓'], '側': sd, 'a': am, '實跑G(列)': r['G(㎡)'], 'n_sg': len(sgc), 'n_pk': len(pkc)}
    if not sgc or not pkc:
        rec['註'] = '配對缺'; out.append(rec); print(json.dumps(rec, ensure_ascii=False)); continue
    _m = [c for c in sgc if round(c['G'], 2) == round(float(r['G(㎡)']), 2)]
    rec['sg_G諸次'] = [round(c['G'], 4) for c in sgc]
    if not _m:
        rec['註'] = '配對未及終值'; out.append(rec); print(json.dumps(rec, ensure_ascii=False)); continue
    s, p = _m[-1], pkc[0]
    rec['評定G'] = round(p['G'], 4); rec['實跑G(攔)'] = round(s['G'], 4); rec['差'] = round(s['G'] - p['G'], 4)
    keys = sorted(set(p['kw']) | set(s['kw']))
    dk = [kk for kk in keys if not same(p['kw'].get(kk), s['kw'].get(kk))]
    rec['相異鍵'] = {kk: {'評定': show(p['kw'].get(kk)), '實跑': show(s['kw'].get(kk))} for kk in dk}
    one = {}
    for kk in dk:
        kw = copy.deepcopy(p['kw']); kw[kk] = copy.deepcopy(s['kw'].get(kk)); one[kk] = round(G_of(kw) - p['G'], 4)
    rec['單換之ΔG'] = one
    rec['中間量'] = {'評定': {k: (round(float(v),6) if v is not None else None) for k,v in p['res'].items()}, '實跑': {k: (round(float(v),6) if v is not None else None) for k,v in s['res'].items()}}
    rec['l_front'] = p['kw']['l_front']; rec['l_side'] = p['kw']['l_side']; rec['F'] = p['kw']['F']; rec['C'] = p['kw']['C']; rec['A'] = p['kw']['A']
    try:
        _dh = np.asarray(p['kw']['d_hat'], float); _db = np.asarray(s['kw']['baseline_pt'], float) - np.asarray(p['kw']['baseline_pt'], float)
        rec['起點位移_沿dhat'] = round(float(np.dot(_db, _dh)), 6); rec['起點位移_長'] = round(float(np.linalg.norm(_db)), 6)
    except Exception as e:
        rec['起點位移_err'] = str(e)
    kw = copy.deepcopy(p['kw']); [kw.__setitem__(kk, copy.deepcopy(s['kw'].get(kk))) for kk in dk]
    rec['全換G'] = round(G_of(kw), 4); rec['全換重現實跑'] = abs(rec['全換G'] - s['G']) < 1e-6
    out.append(rec); print(json.dumps(rec, ensure_ascii=False))
_fo = {b: {'左側': bool((forced.get(b) or {}).get('left_forced_offset')), '右側': bool((forced.get(b) or {}).get('right_forced_offset'))} for b in forced}
red = []
for rec in out:
    rec['強制側'] = bool(_fo.get(rec['街廓'], {}).get(rec['側'], False))
    if rec.get('註'): red.append((rec['宗'], rec['註'])); continue
    if round(rec['實跑G(攔)'], 2) != round(float(rec['實跑G(列)']), 2): red.append((rec['宗'], '攔≠列'))
    if not rec['全換重現實跑']: red.append((rec['宗'], '全換未重現'))
    nz = {k for k, v in rec['單換之ΔG'].items() if abs(v) > 1e-9}
    rec['類'] = ('同' if abs(rec['差']) <= 0.005 else ('強制側' if rec['強制側'] else ('S_max' if nz == {'S_max'} else '異')))
cnt = {k: sum(1 for x in out if x.get('類') == k) for k in ('同', '異', 'S_max', '強制側')}
print('類計', cnt, '器紅', red)
for x in out:
    if x.get('類') not in (None, '同'): print('  ', x.get('類'), x['街廓'], x['側'], x['宗'], '評定', x.get('評定G'), '實跑', x['實跑G(列)'], '差', x.get('差'))
json.dump({'SB': SB, 'recs': out, '類計': cnt, '器紅': red, 'n_calls': {'pk': sum(c['phase'] == 'pk' for c in CALLS), 'sg': sum(c['phase'] == 'sg' for c in CALLS)}},
          open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.exit(6 if red else cnt['異'])
