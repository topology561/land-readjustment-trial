# -*- coding: utf-8 -*-
r"""`W-G.9-341`：`GB-182` 之四格量測器（改前／改後二份 `chk_wg9309.py` 之出艙對拍·⛔ 零生產碼）。

輸入 ＝ 同一格（態 × 退縮）之改前、改後 json（`verify/probes/wg9309/chk_wg9309.py` 之出艙）。
受詞與閘（逐項三值出艙·rc ＝ 破者之和）：
  ① 地主宗（推進側別 ≠ 抵費地）：二份之宗集合同、逐宗逐欄同（含 cut_coords）⇒ 相異宗數 ＝ 0。
  ② 抵費地之面積和：|改後 − 改前| ≤ 0.01 ㎡（＝ app `_pool_strips_for_block` 之 ①' 覆蓋閘之既有容差·⛔ 新訂）。
  ③ 相接之抵費地對（同街廓二片·小片之頂點以 `2e-4`〔＝ app 之 `_S_EPS`〕吸附至大片後，其聯集為單一 Polygon）：改後 ＝ 0。
  ④ 改後之抵費地片中，與改前任一片⛔ 逐位相同者（受併之片），其「零寬折返頂點」數 ＝ 0。
     折返頂點：頂點 b 與前一頂點相距 ≤ 2e-4；或 ab·bc < 0 且 b 至直線 ac 之距 ≤ 2e-4（a、c 相距 ≤ 2e-4 者距取 0）。
  ⑤ 改前無相接對之街廓，其抵費地列於改後逐列逐欄同（名、面積、cut_coords）⇒ 相異列數 ＝ 0。
另出艙（⛔ 入 rc）：改前之相接對逐對（街廓·二片名·二片面積）與其小片之折返頂點數；改後⛔ 與任一片相接之抵費地片中面積 < 1 ㎡ 者（`GB-186` 之受詞）。
器紅（rc 90）：任一份無地主宗、或無抵費地列、或二份之態／退縮不同。
用法：python probe_WG9341_poolpieces.py <before.json> <after.json>
判別力［必破］：以改前 json 同充二參（改前 ⇒ 改後）⇒ ③ 之數 ＝ 改前之相接對數（> 0 者）。
"""
import json, math, sys
from shapely.geometry import Polygon
from shapely.ops import unary_union, snap
sys.stdout.reconfigure(encoding="utf-8")
EPS = 2e-4
A = json.load(open(sys.argv[1], encoding="utf-8")); B = json.load(open(sys.argv[2], encoding="utf-8"))

def P(r):
    c = r.get("cut_coords")
    return Polygon(c) if isinstance(c, list) and len(c) >= 3 else None

def rev_count(g):
    if g is None or g.is_empty: return 0
    cs = [tuple(c) for c in list(g.exterior.coords)[:-1]]; n = len(cs); k = 0
    for i in range(n):
        a, b, c = cs[i - 1], cs[i], cs[(i + 1) % n]
        ab = (b[0] - a[0], b[1] - a[1]); bc = (c[0] - b[0], c[1] - b[1]); ac = (c[0] - a[0], c[1] - a[1])
        if math.hypot(*ab) <= EPS: k += 1; continue
        Lac = math.hypot(*ac)
        d = abs(ac[0] * ab[1] - ac[1] * ab[0]) / Lac if Lac > EPS else 0.0
        if ab[0] * bc[0] + ab[1] * bc[1] < 0 and d <= EPS: k += 1
    return k

def pools(D):
    out = {}
    for r in D["rows"]:
        if r.get("推進側別") == "抵費地":
            out.setdefault(r["所屬街廓"], []).append(r)
    return out

def pairs(pl):
    res = []
    for b, rs in sorted(pl.items()):
        gs = [(r["暫編地號"], P(r)) for r in rs]
        for i in range(len(gs)):
            for j in range(i + 1, len(gs)):
                (ki, gi), (kj, gj) = gs[i], gs[j]
                if gi is None or gj is None or gi.area <= 0 or gj.area <= 0: continue
                big, sm, kb, ks = (gi, gj, ki, kj) if gi.area >= gj.area else (gj, gi, kj, ki)
                if big.distance(sm) > EPS: continue
                if unary_union([big, snap(sm, big, EPS)]).geom_type == "Polygon":
                    res.append((b, kb, ks, round(big.area, 4), round(sm.area, 4), rev_count(sm)))
    return res

own = lambda D: {r["暫編地號"]: r for r in D["rows"] if r.get("推進側別") != "抵費地"}
oA, oB = own(A), own(B); pA, pB = pools(A), pools(B)
if (not oA or not oB or not pA or not pB or A.get("mode") != B.get("mode") or A.get("sb") != B.get("sb")):
    print("🔴 器紅：地主宗或抵費地為空、或二份之態／退縮不同"); sys.exit(90)
print(f"格 {A.get('mode')} {A.get('sb')}｜改前 err {A.get('err')}｜改後 err {B.get('err')}｜地主宗 {len(oA)}／{len(oB)}｜抵費地列 {sum(map(len,pA.values()))}／{sum(map(len,pB.values()))}")
rc = 0
d1 = sorted(k for k in set(oA) | set(oB) if json.dumps(oA.get(k), sort_keys=True, ensure_ascii=False) != json.dumps(oB.get(k), sort_keys=True, ensure_ascii=False))
print(f"① 地主宗逐宗逐欄相異 ＝ {len(d1)} {d1[:8]} ⇒ {'🟢' if not d1 else '🔴'}"); rc += len(d1)
sA = sum(P(r).area for rs in pA.values() for r in rs); sB = sum(P(r).area for rs in pB.values() for r in rs)
ok2 = abs(sB - sA) <= 0.01
print(f"② 抵費地面積和 改前 {sA:.4f}／改後 {sB:.4f}／差 {sB - sA:+.6f} ⇒ {'🟢' if ok2 else '🔴'}"); rc += (0 if ok2 else 1)
prA, prB = pairs(pA), pairs(pB)
print(f"   改前之相接對 {len(prA)}：")
for x in prA: print(f"     {x[0]} {x[1]}（{x[3]}）＋ {x[2]}（{x[4]}）·小片之折返頂點 {x[5]}")
print(f"③ 改後之相接對 ＝ {len(prB)} {prB} ⇒ {'🟢' if not prB else '🔴'}"); rc += len(prB)
sigA = {json.dumps(r.get("cut_coords")) for rs in pA.values() for r in rs}
chg = [(b, r["暫編地號"], round(P(r).area, 4), rev_count(P(r))) for b, rs in sorted(pB.items()) for r in rs if json.dumps(r.get("cut_coords")) not in sigA]
bad4 = [x for x in chg if x[3] > 0]
print(f"④ 受併之片 {len(chg)}：{chg}；其折返頂點 > 0 者 ＝ {len(bad4)} ⇒ {'🟢' if not bad4 else '🔴'}"); rc += len(bad4)
blkA = {x[0] for x in prA}
d5 = []
for b in sorted(set(pA) | set(pB)):
    if b in blkA: continue
    ra = [json.dumps({k: r.get(k) for k in sorted(r)}, sort_keys=True, ensure_ascii=False) for r in pA.get(b, [])]
    rb = [json.dumps({k: r.get(k) for k in sorted(r)}, sort_keys=True, ensure_ascii=False) for r in pB.get(b, [])]
    if ra != rb: d5.append(b)
print(f"⑤ 改前無相接對之街廓 {sorted(set(pA) - blkA)}；其抵費地列改後相異之街廓 ＝ {len(d5)} {d5} ⇒ {'🟢' if not d5 else '🔴'}"); rc += len(d5)
iso = []
for b, rs in sorted(pB.items()):
    for r in rs:
        g = P(r)
        if g is not None and g.area < 1 and not any(x[0] == b and r["暫編地號"] in (x[1], x[2]) for x in prB):
            iso.append((b, r["暫編地號"], round(g.area, 4), rev_count(g)))
print(f"   另列（⛔ 入 rc）：改後未與他片相接之 < 1 ㎡ 抵費地片 {iso}")
print(f"rc {rc}")
sys.exit(rc)
