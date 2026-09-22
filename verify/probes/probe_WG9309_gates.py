# -*- coding: utf-8 -*-
r"""`W-G.9-309` 之閘器（發單側擬·隨單入倉·⛔ 零生產碼）

用法：python verify/probes/probe_WG9309_gates.py <基座樹> <受驗樹> <出艙目錄>
  基座樹 ＝ `2f46579` 之拋棄式 worktree；受驗樹 ＝ 施作後之 worktree（或凍存分支之 checkout）。
  逐（態·情境）以 `verify/probes/wg9309/chk_wg9309.py` 驅動二樹（list 形 `subprocess`·`n④`），
  另以 `verify/probes/wg9309/synth_attr.py` 驅動受驗樹。
出艙 ＝ `<出艙目錄>/WG9309_gates.md` ＋ 逐格 JSON；`rc` ＝ 🔴 閘數（🛑 未執行者亦計入）。

🔒 閘一律三值（🟢 已執行且通過／🛑 未執行／🔴 已執行且破·`恆常附款 n`）。
🔒 閘一、閘二之判別力 ＝ 基座樹之同量須為 🔴（**[必命中]**）；基座樹竟為 🟢 ⇒ 該閘不可證偽 ⇒ 🔴。
"""
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "wg9309")
BASE, NEW, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")   # 🔒 Windows 之管線編碼（受單側主 checkout）
CELLS = [("A_0", "甲", "0.0"), ("A_35", "甲", "3.5"), ("B_0", "乙", "0.0"), ("B_35", "乙", "3.5")]
# 🔒 期值（發單側於沙盒實測·窗二十一·`2026-09-22`·基座 `2f46579`）
EXPECT_CHANGED = {"A_0": ["R4"], "A_35": ["R2", "R4"], "B_0": [], "B_35": ["R2"]}
EXPECT_NEWDROP = {"A_0": {}, "A_35": {"R2/left": ["628-42(1)"]}, "B_0": {}, "B_35": {"R2/left": ["628-42(1)"]}}
EXPECT_SYNTH = "{('left', 'bad', 's_min<0'): 12, ('left', 'ok', 's_min>=0'): 12, ('right', 'ok', 's_min>=0'): 24}"
TOL_G1, TOL_G2, TOL_G4, TOL_SHIFT = 0.005, 1e-6, 1e-3, 1e-3

log = []
def say(s=""):
    print(s); log.append(s)

def run(tree, tag, mode, sb):
    out = os.path.join(OUT, "WG9309_%s_%s.json" % (tag, mode + "_" + sb))
    cp = subprocess.run([sys.executable, os.path.join(TOOLS, "chk_wg9309.py"), tree, mode, sb, out],
                        capture_output=True, env=ENV)
    if cp.returncode != 0 or not os.path.exists(out):
        return None, cp.returncode
    return json.load(open(out, encoding="utf-8")), 0

def key(r):
    return (r["所屬街廓"], r["推進側別"], r["暫編地號"])

def drops(d):
    return {k: sorted(set(x["暫編地號"] for x in v)) for k, v in (d["gates"]["dropped"] or {}).items()}

def maxshift(a, b):
    from shapely.geometry import Polygon
    pa, pb = Polygon(a), Polygon(b)
    return max(min(((x - u) ** 2 + (y - v) ** 2) ** 0.5 for u, v in pb.exterior.coords) for x, y in pa.exterior.coords)

G = {}
def gate(name, ok, detail):
    v = "🛑 未執行" if ok is None else ("🟢 已執行且通過" if ok else "🔴 已執行且破")
    G[name] = v; say("| %s | %s | %s |" % (name, v, detail))

say("# `W-G.9-309` 閘器出艙")
say("基座樹 ＝ `%s`；受驗樹 ＝ `%s`" % (BASE, NEW))
R = {}
for c, m, sb in CELLS:
    b, rb = run(BASE, "base", m, sb)
    n, rn = run(NEW, "new", m, sb)
    R[c] = (b, n)
    say("- 格 `%s`：基座 %s／受驗 %s" % (c, "rc 0" if b else "🔴 rc %s" % rb, "rc 0" if n else "🔴 rc %s" % rn))
say()
say("| 閘 | 三值 | 細 |")
say("|---|---|---|")
ok_run = all(b is not None and n is not None for b, n in R.values())
if not ok_run:
    for nm in ("閘1", "閘2", "閘3", "閘4", "閘5", "閘6", "閘7", "閘8", "閘10"):
        gate(nm, None, "驅動失敗 ⇒ 未執行")
else:
    # 閘1／閘2（受驗樹 ＋ 基座判別力）
    g1n, g1b, g2n, g2b, nb = [], [], [], [], 0
    for c, (b, n) in R.items():
        for tag, d, g1, g2 in (("new", n, g1n, g2n), ("base", b, g1b, g2b)):
            for blk, bg in d["gates"]["blocks"].items():
                for x in bg["bands"]:
                    if tag == "new": nb += 1
                    g1.append((c, blk, x["side"], x["g1_symdiff_mat_range"]))
                    g2.append((c, blk, x["side"], sum(v for _, v in x["g2_range_owner"])))
    g1_new_ok = nb > 0 and all(v is not None and v <= TOL_G1 for *_, v in g1n)
    g1_base_red = len(g1b) > 0 and all(v is None or v > TOL_G1 for *_, v in g1b)
    gate("閘1", g1_new_ok and g1_base_red, "強制抵費地物化形 vs 規定範圍（界 `%s`）：受驗 %s｜基座[必命中]須全破 %s（強制側數 `%d`）" % (TOL_G1, g1n, g1b, nb))
    g2_new_ok = nb > 0 and all(v <= TOL_G2 for *_, v in g2n)
    g2_base_red = any(v > TOL_G2 for *_, v in g2b)
    gate("閘2", g2_new_ok and g2_base_red, "規定範圍 ∩ 業主宗：受驗 %s｜基座[必命中]須至少一破 %s" % (g2n, g2b))
    # 閘3／閘4（自列重算·⛔ 採信量測器之欄）＋ 判別力造（擾動副本須被攔）
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    def g34(rows, blocks):
        b3, b4 = [], []
        for blk, bg in blocks.items():
            R_ = [r for r in rows if r["所屬街廓"] == blk and isinstance(r.get("cut_coords"), list) and len(r["cut_coords"]) >= 3]
            own = [(r["暫編地號"], Polygon(r["cut_coords"])) for r in R_ if r["推進側別"] in ("left", "right")]
            allp = [Polygon(r["cut_coords"]) for r in R_]
            inv = [k for k, q in own if not q.is_valid]
            ov = [(own[i][0], own[j][0]) for i in range(len(own)) for j in range(i + 1, len(own)) if own[i][1].intersection(own[j][1]).area > 1e-6]
            if inv or ov: b3.append((blk, inv, ov))
            ua = unary_union(allp).area if allp else 0.0
            if abs(sum(q.area for q in allp) - bg["block_area"]) > TOL_G4 or abs(ua - bg["block_area"]) > TOL_G4: b4.append((blk, round(sum(q.area for q in allp) - bg["block_area"], 6)))
        return b3, b4
    bad3, bad4, nblk = [], [], 0
    for c, (b, n) in R.items():
        x3, x4 = g34(n["rows"], n["gates"]["blocks"]); nblk += len(n["gates"]["blocks"])
        bad3 += [(c,) + t for t in x3]; bad4 += [(c,) + t for t in x4]
    _c0 = R["A_35"][1]; _rows = [dict(r) for r in _c0["rows"]]
    _own = [r for r in _rows if r["所屬街廓"] == "R2" and r["推進側別"] == "left"]
    _own[1]["cut_coords"] = [list(t) for t in _own[0]["cut_coords"]]            # 擾動：二宗疊合
    p3, p4 = g34(_rows, {"R2": _c0["gates"]["blocks"]["R2"]})
    say("  - 閘3／閘4 判別力造（`A_35`·`R2` 左二宗疊合之擾動副本）：閘3 攔 `%s`·閘4 攔 `%s`" % (bool(p3), bool(p4)))
    gate("閘3", nblk > 0 and not bad3 and bool(p3), "業主宗有效且兩兩不重疊（受驗·街廓格數 `%d`）：破 %s" % (nblk, bad3))
    gate("閘4", nblk > 0 and not bad4 and bool(p4), "街廓面積守恆（Σ ≡ 聯集 ≡ 街廓面積·界 `%s`）：破 %s" % (TOL_G4, bad4))
    # 閘5／閘6／閘7／閘8／閘10
    bad5, bad6, bad7, bad8, bad10, n10 = [], [], [], [], [], 0
    for c, (b, n) in R.items():
        ra = {key(r): r for r in b["rows"]}; rn = {key(r): r for r in n["rows"]}
        ch = sorted(set(k[0] for k in set(ra) | set(rn) if ra.get(k) != rn.get(k)))
        oth = [k for k in set(ra) | set(rn) if k[0] not in ch]
        same = sum(1 for k in oth if ra.get(k) == rn.get(k))
        if ch != EXPECT_CHANGED[c] or same != len(oth) or not oth: bad5.append((c, ch, same, len(oth)))
        say("  - `%s` 變動街廓 %s（期 %s）·其餘逐位 `%d／%d`" % (c, ch, EXPECT_CHANGED[c], same, len(oth)))
        da, dn = drops(b), drops(n)
        newd = {k: sorted(set(dn.get(k, [])) - set(da.get(k, []))) for k in dn if set(dn.get(k, [])) - set(da.get(k, []))}
        gone = {k: sorted(set(da.get(k, [])) - set(dn.get(k, []))) for k in da if set(da.get(k, [])) - set(dn.get(k, []))}
        if newd != EXPECT_NEWDROP[c] or gone: bad6.append((c, newd, gone))
        if b["err"] != n["err"] or (c.startswith("B_") and not b["err"]): bad7.append((c, (b["err"] or "")[:60], (n["err"] or "")[:60]))
        if EXPECT_NEWDROP[c]:
            chain = [r for r in n["rows"] if r["所屬街廓"] == "R2" and r["推進側別"] == "left"]
            h = chain[0] if chain else {}
            if h.get("暫編地號") != "628-41(1)" or h.get("驗_宗序") != "第2宗" or h.get("驗_B藍影") != "合格":
                bad8.append((c, h.get("暫編地號"), h.get("驗_宗序"), h.get("驗_B藍影")))
        for k in set(ra) & set(rn):
            if k[0] in ch and k[1] in ("left", "right"):
                side_forced = bool((n.get("forced") or {}).get(k[0], {}).get(k[1] + "_forced_offset", False))
                if not side_forced:
                    n10 += 1
                    s = maxshift(ra[k]["cut_coords"], rn[k]["cut_coords"])
                    if ra[k]["G(㎡)"] != rn[k]["G(㎡)"] or s > TOL_SHIFT: bad10.append((c, k, ra[k]["G(㎡)"], rn[k]["G(㎡)"], round(s, 6)))
    gate("閘5", not bad5, "變動街廓之集 ＝ 期值且其餘街廓逐宗逐位相同：破 %s" % bad5)
    gate("閘6", not bad6, "遞補剔除之差（受驗 − 基座）＝ 期值且無消失：破 %s" % bad6)
    gate("閘7", not bad7, "停機訊息二樹同一·態乙之基座須非空（既存之 `R4` 右結構閘）：破 %s" % bad7)
    gate("閘8", sum(1 for c in EXPECT_NEWDROP if EXPECT_NEWDROP[c]) > 0 and not bad8, "強制側鏈首（緊鄰強制抵費地）＝ `628-41(1)`·`第2宗`·藍影合格：破 %s" % bad8)
    gate("閘10", n10 > 0 and not bad10, "變動街廓之非強制鏈：`G` 同一且頂點位移 ≤ `%s` m（受詞宗數 `%d`）：破 %s" % (TOL_SHIFT, n10, bad10))
# 閘9 合成例（受驗樹）
cp = subprocess.run([sys.executable, os.path.join(TOOLS, "synth_attr.py"), NEW], capture_output=True, env=ENV)
got = cp.stdout.decode("utf-8", "replace").strip().split("\n")[-1] if cp.returncode == 0 else ""
gate("閘9", (got == EXPECT_SYNTH) if cp.returncode == 0 else None, "合成例計數 ＝ `%s`（期 `%s`）" % (got, EXPECT_SYNTH))
# 土地影響表（變動街廓·基座 → 受驗）
say()
say("## 土地影響（變動街廓·基座 → 受驗）")
for c, (b, n) in R.items():
    if not (b and n): continue
    ra = {key(r): r for r in b["rows"]}; rn = {key(r): r for r in n["rows"]}
    for k in sorted(set(ra) | set(rn)):
        if k[0] in EXPECT_CHANGED[c] and ra.get(k) != rn.get(k):
            f = lambda r, x: "—" if r is None else r.get(x)
            say("- `%s` %s｜G %s → %s｜幾何 %s → %s｜負擔比率 %s → %s" % (c, "/".join(k), f(ra.get(k), "G(㎡)"), f(rn.get(k), "G(㎡)"),
                f(ra.get(k), "幾何面積(㎡)"), f(rn.get(k), "幾何面積(㎡)"), f(ra.get(k), "負擔比率"), f(rn.get(k), "負擔比率")))
red = sum(1 for v in G.values() if not v.startswith("🟢"))
say()
say("rc ＝ 非 🟢 閘數 ＝ `%d`（閘數 `%d`）" % (red, len(G)))
open(os.path.join(OUT, "WG9309_gates.md"), "w", encoding="utf-8", newline="\n").write("\n".join(log) + "\n")
sys.exit(red)
