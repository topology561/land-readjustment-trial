# -*- coding: utf-8 -*-
r"""`W-G.9-338`：街角第 1 宗與其後 1 宗之間之片（`GB-178` 失效條件 `(2)` 之器·⛔ 零生產碼）。

輸入 ＝ `verify/probes/wg9309/chk_wg9309.py` 之出艙 json（一格）。
受詞 ＝ 每一（街廓·側）之「街角第 1 宗」（`驗_宗序 ＝ 街角第1宗`）與同側之「第 2 宗」（`驗_宗序 ＝ 第2宗`·`驗_總判 ＝ 保留`）。
片 ＝ 配餘地列（`推進側別 ＝ 抵費地`）中，與二宗之邊界各共線長 `> 0.05 m` 者（夾於二宗之間）。
另列（⛔ 入 rc）：與街角第 1 宗共界 `> 0.05 m`、面積 `< 400 ㎡` 之其餘配餘地片（街角宗旁之小片·`GB-180` 之受詞）。
rc ＝ 夾於二宗之間而面積 `> 0.005 ㎡` 之片數；全格無任一「街角第 1 宗 ＋ 第 2 宗」之對 ⇒ rc 5（無受詞·該格⛔ 判綠）。
用法：python probe_WG9338_gapcheck.py <chk.json>
"""
import json, sys
from shapely.geometry import Polygon
sys.stdout.reconfigure(encoding="utf-8")
D = json.load(open(sys.argv[1], encoding="utf-8"))
def P(r):
    c = r.get("cut_coords")
    return Polygon(c).buffer(0) if isinstance(c, list) and len(c) >= 3 else None
def shared(p, q): return p.boundary.intersection(q.boundary).length
rows = D["rows"]; pairs = 0; hits = []; small = []
for b in sorted({r["所屬街廓"] for r in rows}):
    R = [r for r in rows if r["所屬街廓"] == b]
    pools = [(r, P(r)) for r in R if r.get("推進側別") == "抵費地" and P(r) is not None and P(r).area > 0]
    for sd in ("left", "right"):
        c1 = [r for r in R if r.get("推進側別") == sd and r.get("驗_宗序") == "街角第1宗"]
        c2 = [r for r in R if r.get("推進側別") == sd and r.get("驗_宗序") == "第2宗" and r.get("驗_總判") == "保留"]
        if not c1: continue
        p1 = P(c1[0])
        if c2:
            pairs += 1; p2 = P(c2[0])
            for r, q in pools:
                if shared(q, p1) > 0.05 and shared(q, p2) > 0.05:
                    hits.append((b, sd, c1[0]["暫編地號"], c2[0]["暫編地號"], r["暫編地號"], round(q.area, 4)))
        for r, q in pools:
            if q.area < 400 and shared(q, p1) > 0.05 and not any(h[4] == r["暫編地號"] for h in hits):
                small.append((b, sd, c1[0]["暫編地號"], r["暫編地號"], round(q.area, 4)))
print("格", D.get("mode"), D.get("sb"), "err", D.get("err"), "對數", pairs)
for h in hits: print("  夾片", h)
for s in small: print("  旁片（另列）", s)
if pairs == 0:
    print("⚪ 無受詞：本格無「街角第 1 宗 ＋ 第 2 宗」之對·⛔ 判綠"); sys.exit(5)
n = sum(1 for h in hits if h[5] > 0.005)
print("rc", n); sys.exit(n)
