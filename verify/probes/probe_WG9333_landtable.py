# -*- coding: utf-8 -*-
r"""`W-G.9-333` 工項三：全區逐宗之**四欄表**（改前／改後·⛔ 零生產碼）。

輸入 ＝ 二份 `verify/probes/wg9309/chk_wg9309.py` 之出艙 json（同一「態·退縮」·改前樹與改後樹各一）。
四欄 ＝ 暫編地號｜改前 `G`（㎡）｜改後 `G`（㎡）｜差（㎡）；另附街廓、幾何對稱差（㎡）。
改前中止（`err` 非空）者，其未算之宗改前欄記「未算（中斷）」。
判：「同」＝ `G` 逐位相等 ∧ 幾何對稱差 `≤ 0.005`；餘為「異」。
用法：python probe_WG9333_landtable.py <改前.json> <改後.json> <出艙.md>
rc ＝ 二者皆有之宗中「異」之數（⛔ 含改前未算者）。
"""
import json, sys
from shapely.geometry import Polygon
sys.stdout.reconfigure(encoding="utf-8")
A = json.load(open(sys.argv[1], encoding="utf-8")); B = json.load(open(sys.argv[2], encoding="utf-8")); OUT = sys.argv[3]
def idx(d): return {(r["所屬街廓"], r["暫編地號"]): r for r in d["rows"]}
ia, ib = idx(A), idx(B)
def poly(r):
    c = r.get("cut_coords")
    return Polygon(c).buffer(0) if isinstance(c, list) and len(c) >= 3 else None
keys = sorted(set(ia) | set(ib))
L = [f"# 四欄表：{A.get('mode')} 態·退縮 {A.get('sb')} m", "",
     f"改前：{len(ia)} 列·中止 ＝ {repr((A.get('err') or '')[:120]) if A.get('err') else '無'}",
     f"改後：{len(ib)} 列·中止 ＝ {repr((B.get('err') or '')[:120]) if B.get('err') else '無'}", "",
     "| 街廓 | 暫編地號 | 改前 G（㎡） | 改後 G（㎡） | 差（㎡） | 幾何對稱差（㎡） | 判 |", "|---|---|---|---|---|---|---|"]
ndiff = nsame = nnew = ngone = 0
for k in keys:
    x, y = ia.get(k), ib.get(k)
    if x is None:
        nnew += 1; L.append(f"| {k[0]} | {k[1]} | 未算（中斷） | {y.get('G(㎡)')} | — | — | 改前未算 |" if A.get("err") else f"| {k[0]} | {k[1]} | 無此列 | {y.get('G(㎡)')} | — | — | 新列 |"); continue
    if y is None:
        ngone += 1; L.append(f"| {k[0]} | {k[1]} | {x.get('G(㎡)')} | 無此列 | — | — | 消失 |"); continue
    px, py = poly(x), poly(y)
    sd = None if (px is None or py is None) else px.symmetric_difference(py).area
    gx, gy = x.get("G(㎡)"), y.get("G(㎡)")
    same = (gx == gy) and (sd is None or sd <= 0.005)
    d = None if (gx is None or gy is None) else round(float(gy) - float(gx), 2)
    if same: nsame += 1
    else: ndiff += 1
    L.append(f"| {k[0]} | {k[1]} | {gx} | {gy} | {d} | {'—' if sd is None else round(sd, 4)} | {'同' if same else '**異**'} |")
L += ["", f"計：同 {nsame}／異 {ndiff}／改前未算或新列 {nnew}／消失 {ngone}（合 {len(keys)}）"]
open(OUT, "w", encoding="utf-8", newline="").write("\n".join(L) + "\n")
print(f"{A.get('mode')} {A.get('sb')}：同 {nsame}／異 {ndiff}／改前未算或新列 {nnew}／消失 {ngone}（合 {len(keys)}）⇒ {OUT}")
sys.exit(ndiff + ngone)
