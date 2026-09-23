# -*- coding: utf-8 -*-
r"""`W-G.9-333` 工項二／三：選槽估算之**全槽驗證**（判別力二造之器·⛔ 零生產碼·⛔ 改倉內任何檔）。

受詞（土地性質）：調配池置於街廓內**每一合法槽位** k 時，選槽所估之各側側街負擔（`ΣRw` 理論）
與實際推進所得（實跑·階段 1）之差，逐（街廓·側·k）皆 `≤ 0.1`（＝ 生產碼「理論＝實跑」閘之容差）。
⛔ 只驗所選之 k*——k* 恰等於估算所依之試推進時，該比較退為同一推進之自比（`自誤 506`）。

作法：讀 `<repo>/verify/stepg_pipeline.py` 之原文，於**記憶體內**施二處探針鉤（字樣錨各須恰命中 `1`），
寫入倉外暫存目錄並置於 `sys.path` 之首 ⇒ 倉內檔一字不動。
  鉤一：`ns['_PROBE_FORCE_K']` 有值 ⇒ 記各街廓之合法槽 `K` 與 k*，並依之強制槽位；略過「J 下降」之看守。
  鉤二：「理論＝實跑」閘改為**記錄**（⛔ raise）。
次序：① 基準一趟（取 `K`）② 各街廓之第 j 槽同趟強制（j ＝ 0…）③ 前趟因他街廓中止而缺之格，逐（街廓·k）單獨強制補跑。
單獨強制仍中止者 ＝ 該槽**不可配地**（例：`K-9-9 六` 候選耗盡），列名出艙、⛔ 入比較。

用法：python probe_WG9333_allslots.py <repo> <甲|乙> <0.0|3.5> <out.json>
rc ＝ 差 `> 0.1` 之格數（`0` ＝ 綠）；探針鉤之錨命中 ≠ `1` ⇒ rc `90`。
"""
import contextlib, copy, io, json, os, sys, tempfile
sys.stdout.reconfigure(encoding="utf-8")
REPO, MODE, SB, OUT = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
src = open(os.path.join(REPO, "verify", "stepg_pipeline.py"), encoding="utf-8").read()
A1 = ("            _k_star = int(_slot_res['k'])\n"
      "            _J_by_k = {t['k']: t['J'] for t in _slot_res['table']}\n"
      "            if (_k_naive in _J_by_k")
B1 = ("            _k_star = int(_slot_res['k'])\n"
      "            _PFK = ns.get('_PROBE_FORCE_K')\n"
      "            if _PFK is not None:\n"
      "                _Ks = [t['k'] for t in _slot_res['table']]\n"
      "                ns.setdefault('_PROBE_KS', {})[blk_label] = (_Ks, _k_star)\n"
      "                _fk = _PFK.get(blk_label)\n"
      "                if _fk is not None and _fk in _Ks:\n"
      "                    _k_star = int(_fk)\n"
      "            _J_by_k = {t['k']: t['J'] for t in _slot_res['table']}\n"
      "            if (_PFK is None and _k_naive in _J_by_k")
A2 = "                if abs(_th - _re) > _IFACE_TOL:\n"
B2 = ("                ns.setdefault('_PROBE_TH', {})[(blk_label, _sd_tag2)] = (_th, _re, _k_star)\n"
      "                if abs(_th - _re) > _IFACE_TOL and ns.get('_PROBE_FORCE_K') is None:\n")
n1, n2 = src.count(A1), src.count(A2)
if (n1, n2) != (1, 1):
    print(f"🔴 探針鉤之錨命中 ≠ 1：鉤一 {n1}／鉤二 {n2} ⇒ 停"); sys.exit(90)
TMP = tempfile.mkdtemp(prefix="wg9333_allslots_")
open(os.path.join(TMP, "stepg_pipeline.py"), "w", encoding="utf-8", newline="").write(src.replace(A1, B1).replace(A2, B2))
sys.path.insert(0, os.path.join(REPO, "verify", "probes")); sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, TMP)
import stepg_pipeline as SP          # 🔒 先於他模組載入 ⇒ sys.modules 快取之即掛鉤副本（他模組自插路徑亦不改其取）
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
assert os.path.dirname(os.path.abspath(SP.__file__)) == TMP, "🔴 未載入掛鉤之副本"
with contextlib.redirect_stdout(io.StringIO()):
    ns, fake_st = harvest(os.path.join(REPO, "app.py"))
    snapshot = rv.load_snapshot(); cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    v6 = open(rv.V6DXF, "rb").read()
    temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d, _s, _o, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
def run(force):
    ns["_PROBE_FORCE_K"] = force; ns["_PROBE_TH"] = {}; err = None
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            SP.run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, copy.deepcopy(params), copy.deepcopy(build_p),
                          copy.deepcopy(wins), copy.deepcopy(forced), SB, eff_min_build_by_blk={})
        except Exception as e:
            err = str(e).split("\n")[0][:200]
    return dict(ns["_PROBE_TH"]), err
ns["_PROBE_KS"] = {}
_, err0 = run({})
KS = dict(ns["_PROBE_KS"])
cells = {}
def take(th):
    for (b, sd), (t, r, k) in th.items():
        cells[(b, sd, int(k))] = (round(t, 4), round(r, 4))
for j in range(max((len(v[0]) for v in KS.values()), default=0)):
    th, _ = run({b: v[0][j] for b, v in KS.items() if j < len(v[0])}); take(th)
infeasible = []
for b, (Ks, _k) in KS.items():
    for k in Ks:
        if any((b, sd, k) in cells for sd in ("left", "right")): continue
        th, err = run({b: k})
        got = {kk: vv for kk, vv in th.items() if kk[0] == b}
        if got: take(got)
        else: infeasible.append((b, k, err))
rows = [dict(blk=b, side=sd, k=k, k_star=KS[b][1], th=t, re=r, d=round(abs(t - r), 4)) for (b, sd, k), (t, r) in sorted(cells.items())]
bad = [x for x in rows if x["d"] > 0.1]
json.dump(dict(mode=MODE, sb=SB, base_err=err0, KS=KS, rows=rows, infeasible=infeasible), open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print(f"{MODE} {SB}：格 {len(rows)}｜最大差 {max((x['d'] for x in rows), default=None)}｜差 >0.1 者 {len(bad)}｜不可配地之槽 {[(b, k) for b, k, _ in infeasible]}")
for x in sorted(bad, key=lambda x: -x["d"])[:10]: print("   ", x)
sys.exit(len(bad))
