# -*- coding: utf-8 -*-
"""補令五 `§五` 前置 `4.`：`殘-1` 之**土地量問答**。

問：`3.5m·R4·left 街角第1宗 628(1)+` 之 `累積S` `+1.58`，
    **是否改變該宗面積／該街廓（`R4`）之抵費地面積？**

🔒 母體 ＝ `D_off`（旗標 `off`·中止 ⇒ `_partial`）與 `D_on`（旗標 `on`·跑完 ⇒ 完整檔）之落檔。
🔒 抵費地（調配池）由**守恆式**得：`街廓面積 − ΣG`（`CLAUDE.md` 最高鐵律
   `ΣG(街廓內所有分配地) + 調配池(Ri) = 街廓 DXF 面積(Ri)` 恆成立）。
"""
import csv
import io
import os
import sys

SCR = (sys.argv[1] if len(sys.argv) > 1
       else os.path.dirname(os.path.abspath(__file__)))
W = 116


def load(d, scen):
    for suf in ("_partial", ""):
        p = os.path.join(d, "got_G值_退縮%s%s.csv" % (scen, suf))
        if os.path.exists(p):
            with io.open(p, encoding="utf-8-sig", newline="") as f:
                return list(csv.DictReader(f)), os.path.basename(p)
    return [], "⛔ 無"


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


print("=" * W)
print("【補令五 `§五` 前置 `4.`】`殘-1` 之土地量問答（`3.5m·R4·left` `628(1)+`·`+1.58`）")
print("=" * W)
print()

A, fa = load(os.path.join(SCR, "D_off"), "3.5m")
B, fb = load(os.path.join(SCR, "D_on"), "3.5m")
print("  off 落檔 %-34s %3d 列 ／ on 落檔 %-26s %3d 列" % (fa, len(A), fb, len(B)))
print()

LOT = "628(1)+"
COLS = ["累積S(m)", "S(m)", "幾何面積(㎡)", "G(㎡)", "a 面積(㎡)",
        "宗地寬度(m)", "負擔比率", "街廓面積(㎡)"]
ra = next((r for r in A if r["暫編地號"] == LOT), None)
rb = next((r for r in B if r["暫編地號"] == LOT), None)
print("── 一、該宗（`%s`）之逐欄 off vs on ──" % LOT)
print("  %-16s %14s %14s %14s %s" % ("欄", "off", "on", "Δ", "判"))
land_changed = []
for c in COLS:
    va, vb = f((ra or {}).get(c)), f((rb or {}).get(c))
    if va is None or vb is None:
        print("  %-16s %14s %14s %14s" % (c, (ra or {}).get(c), (rb or {}).get(c), "—"))
        continue
    d = vb - va
    mark = ""
    if c in ("幾何面積(㎡)", "G(㎡)", "a 面積(㎡)") and abs(d) > 1e-9:
        mark = "🔴 **土地量有變**"
        land_changed.append((c, va, vb, d))
    elif abs(d) > 1e-9:
        mark = "🟡 非土地量"
    else:
        mark = "🟢 不變"
    print("  %-16s %14.4f %14.4f %+14.4f %s" % (c, va, vb, d, mark))
print()

print("── 二、該街廓（`R4`）之守恆帳（抵費地 ＝ 街廓面積 − ΣG）──")
print("  %-6s %10s %14s %14s %14s %s" % ("態", "宗數", "ΣG(㎡)", "街廓面積(㎡)", "抵費地(㎡)", "備註"))
res = {}
for tag, rows in (("off", A), ("on", B)):
    rs = [r for r in rows if (r.get("所屬街廓") or "").strip() == "R4"]
    sg = sum(f(r.get("G(㎡)")) or 0.0 for r in rs)
    blk = f(rs[0].get("街廓面積(㎡)")) if rs else None
    pool = (blk - sg) if blk is not None else None
    res[tag] = (len(rs), sg, blk, pool)
    print("  %-6s %10d %14.4f %14s %14s"
          % (tag, len(rs), sg,
             ("%.4f" % blk) if blk is not None else "—",
             ("%.4f" % pool) if pool is not None else "—"))
if res["off"][2] is not None and res["on"][2] is not None:
    dsg = res["on"][1] - res["off"][1]
    dpool = res["on"][3] - res["off"][3]
    dblk = res["on"][2] - res["off"][2]
    print("  Δ：宗數 %+d ／ **ΣG %+.4f** ／ 街廓面積 %+.4f ／ **抵費地 %+.4f**"
          % (res["on"][0] - res["off"][0], dsg, dblk, dpool))
    print("  🔒 守恆自證：`ΔΣG + Δ抵費地 ＝ %+.4f`（須 ＝ `Δ街廓面積 ＝ %+.4f`）%s"
          % (dsg + dpool, dblk, "✅" if abs((dsg + dpool) - dblk) < 1e-6 else "🔴"))
print()

print("── 三、逐宗（`R4`）之 `G` 與幾何面積 off vs on ──")
ao = {r["暫編地號"]: r for r in A if (r.get("所屬街廓") or "").strip() == "R4"}
bo = {r["暫編地號"]: r for r in B if (r.get("所屬街廓") or "").strip() == "R4"}
keys = sorted(set(ao) | set(bo))
print("  %-16s %-8s %12s %12s %12s %12s" % ("暫編地號", "側", "G off", "G on", "幾何 off", "幾何 on"))
for k in keys:
    a, b = ao.get(k), bo.get(k)
    print("  %-16s %-8s %12s %12s %12s %12s"
          % (k, (b or a or {}).get("推進側別", "—"),
             (a or {}).get("G(㎡)", "⛔ 無"), (b or {}).get("G(㎡)", "⛔ 無"),
             (a or {}).get("幾何面積(㎡)", "⛔ 無"), (b or {}).get("幾何面積(㎡)", "⛔ 無")))
print()
print("=" * W)
print("🔒 **答**：見上三表。`土地量有變` 之欄 ＝ %s"
      % ([c for c, _a, _b, _d in land_changed] or "（無）"))
print("=" * W)
