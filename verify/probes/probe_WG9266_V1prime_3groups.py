# -*- coding: utf-8 -*-
"""W-G.9-266 工項三：`V-1′` 之**三組**對照（陽性／真陰性／第三類）。唯讀探針。

用法：probe_WG9266_V1prime_3groups.py <態A 根> <態B 根> <front_lines.json>

🔒 唯讀：只讀二態之 harness 落檔 `verify/out/got_G值_退縮3.5m_partial.csv`
   ＋ 一份自**生產解析器**（`run_verification.build_pipeline` → `cad['front_lines']`）匯出之 `FRONT_LINE` 端點。
   ⛔ 動 `app.py` 與 `verify/` 生產路徑一字。

【與 `-265` 之器之別（⛔ 改判準一字）】
  · `V-1′` 五款判準**一字不動**（`1e-6` ⛔ 放寬）。
  · 🆕 **三組**（`-265` 為二組）；陰性由 `R2·right` 改為 **`R1·right`**（`自誤 328`）。
  · 🆕 **每組同格出艙其判定集基數 `n`（＝ 非鏈頭宗數）；`n = 0` ⇒ loud 拒測**，
    ⛔ 計為通過、⛔ 靜默略（`自誤 329`）。
  · 🆕 併出艙二態之 `cut_coords` **逐位相同數**（`k/n`），使「該側是否已動」成為**已量**而非斷言。

【框之來源（逐項具名·`VR-091` 一）】
  · `d̂` ＝ `FRONT_LINE` 之 `p1 → p2` 單位向量 ＝ **生產解析器之輸出**（⛔ 質心導出·⛔ 自寫第二份解析）。
  · 界之 `s` 位置 `b_i` ＝ 第 `i` 宗與第 `i+1` 宗之**共用邊**所在直線 × `FRONT_LINE` 之交點於 `d̂` 上之座標 ＝ **自擬**。
  · 第 `i` 宗之 `s` 區間 ＝ `[b_{i−1}, b_i]` ＝ **自擬**。

【自我驗證閘（⛔ 省）】閘 `γ` 共用邊恰 `2` 頂點／閘 `α` `b_i − b_{i−1}` vs 落檔 `S(m)` `±0.01`／
閘 `β` `area` vs 落檔 `G(㎡)` `±0.02`。任一不過 ⇒ ⛔ 據本表下任何結論（`rc ≠ 0`）。
"""
import ast
import csv
import io
import json
import math
import os
import sys

from shapely.geometry import Polygon

CSV3 = os.path.join("verify", "out", "got_G值_退縮3.5m_partial.csv")
QK = 1e-6
TOL_K1 = 1e-6      # ⛔ 放寬（單 §四 (b)）
TOL_K3 = 1e-6


def poly(c):
    p = Polygon(c)
    return p if p.is_valid else p.buffer(0)


def load(root):
    with io.open(os.path.join(root, CSV3), "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def side_rows(rows, blk, side):
    out = []
    for r in rows:
        if (r.get("所屬街廓") or "").strip() != blk:
            continue
        if (r.get("推進側別") or "").strip() != side:
            continue
        cc = (r.get("cut_coords") or "").strip()
        if not cc:
            continue
        v = [(float(a), float(b)) for a, b in ast.literal_eval(cc)]
        out.append((r, v, poly(v)))
    out.sort(key=lambda t: float(t[0].get("累積S(m)") or 0))
    return out


def shared_edge(cA, cB):
    sh = []
    for a in cA:
        for b in cB:
            if abs(a[0] - b[0]) < QK and abs(a[1] - b[1]) < QK:
                if not any(abs(a[0] - s[0]) < QK and abs(a[1] - s[1]) < QK for s in sh):
                    sh.append(a)
    return sh


def s_of_line(q1, q2, fp, dh):
    ux, uy = dh
    nx, ny = -uy, ux
    d1 = (q1[0] - fp[0]) * nx + (q1[1] - fp[1]) * ny
    d2 = (q2[0] - fp[0]) * nx + (q2[1] - fp[1]) * ny
    if abs(d1 - d2) < 1e-12:
        return None
    t = d1 / (d1 - d2)
    px = q1[0] + t * (q2[0] - q1[0])
    py = q1[1] + t * (q2[1] - q1[1])
    return (px - fp[0]) * ux + (py - fp[1]) * uy


def measure(root, blk, side, fl):
    rows = load(root)
    items = side_rows(rows, blk, side)
    if not items:
        return None
    p1, p2 = fl[blk]["p1"], fl[blk]["p2"]
    L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    dh = ((p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L)
    fp = (p1[0], p1[1])

    bounds, gam = [], []
    for i in range(len(items) - 1):
        sh = shared_edge(items[i][1], items[i + 1][1])
        gam.append(((items[i][0].get("暫編地號") or "").strip(),
                    (items[i + 1][0].get("暫編地號") or "").strip(), len(sh)))
        bounds.append(s_of_line(sh[0], sh[1], fp, dh) if len(sh) == 2 else None)

    lots = []
    for i, (r, cc, p) in enumerate(items):
        lots.append({
            "id": (r.get("暫編地號") or "").strip(),
            "hi": bounds[i] if i < len(bounds) else None,
            "lo": bounds[i - 1] if i >= 1 else None,
            "area": p.area, "cc": cc,
            "G": float(r.get("G(㎡)") or 0),
            "S": float(r.get("S(m)") or 0),
            "N14": (r.get("宗地寬度(m)") or "").strip(),
            "序": (r.get("驗_宗序") or "").strip(),
        })
    pool = [r for r in rows if (r.get("所屬街廓") or "").strip() == blk
            and (r.get("推進側別") or "").strip() == "抵費地"]
    blkarea = next((float(r["街廓面積(㎡)"]) for r in rows
                    if (r.get("所屬街廓") or "").strip() == blk and (r.get("街廓面積(㎡)") or "").strip()), None)
    sumG = sum(float(r.get("G(㎡)") or 0) for r in rows if (r.get("所屬街廓") or "").strip() == blk)
    sumpool = sum(float(r.get("幾何面積(㎡)") or 0) for r in pool)
    return {"lots": lots, "gam": gam, "dh": dh, "blkarea": blkarea,
            "sumG": sumG, "sumpool": sumpool, "npool": len(pool)}


def gates(m, tag):
    ok = True
    lots = m["lots"]
    ng = sum(1 for _a, _b, n in m["gam"] if n == 2)
    ok &= (ng == len(m["gam"]))
    print("     閘 γ（共用邊恰 2 頂點）%d/%d  %s" % (ng, len(m["gam"]), "✅" if ng == len(m["gam"]) else "🔴"))
    na = nat = 0
    worst = 0.0
    for i in range(1, len(lots)):
        lo, hi = lots[i]["lo"], lots[i]["hi"]
        if lo is None or hi is None:
            continue
        nat += 1
        d = abs(abs(hi - lo) - lots[i]["S"])
        worst = max(worst, d)
        if d <= 0.01:
            na += 1
    ok &= (na == nat)
    print("     閘 α（`b_i − b_{i−1}` vs 落檔 `S(m)`·±0.01）%d/%d｜最大 |Δ| ＝ %.6f  %s"
          % (na, nat, worst, "✅" if na == nat else "🔴"))
    nb = sum(1 for d in lots if abs(d["area"] - d["G"]) <= 0.02)
    ok &= (nb == len(lots))
    print("     閘 β（`area` vs 落檔 `G(㎡)`·±0.02）%d/%d  %s" % (nb, len(lots), "✅" if nb == len(lots) else "🔴"))
    return ok


def run(rootA, rootB, blk, side, fl, role):
    print("=" * 116)
    print("【%s】受詞逐字 ＝ `3.5m`·`%s`·`%s`（⛔ 以容器名代之）" % (role, blk, side))
    print("=" * 116)
    mA, mB = measure(rootA, blk, side, fl), measure(rootB, blk, side, fl)
    if mA is None or mB is None:
        print("🔴 一態無該側之列 ⇒ **loud 拒測**")
        return {"refuse": True, "n": 0}

    A = {d["id"]: d for d in mA["lots"]}
    B = {d["id"]: d for d in mB["lots"]}
    ida = [d["id"] for d in mA["lots"]]
    idb = [d["id"] for d in mB["lots"]]
    non_head = idb[1:]
    n = len(non_head)

    print("   鏈序 態A ＝ %s" % ida)
    print("   鏈序 態B ＝ %s" % idb)
    print("   鏈頭（第 `0` 宗）＝ %s（`驗_宗序` ＝ %s）" % (idb[0], B[idb[0]]["序"]))
    print("   🔑 **判定集基數 `n`（非鏈頭宗數）＝ %d**" % n)
    if n == 0:
        print("   🛑 **`n = 0` ⇒ loud 拒測**（`自誤 329`）——⛔ 計為通過、⛔ 靜默略")
        return {"refuse": True, "n": 0}

    # 二態 cut_coords 逐位相同數（使「該側是否已動」成為已量·自誤 328）
    same = sum(1 for i in idb if i in A and A[i]["cc"] == B[i]["cc"])
    print("   🔑 **二態 `cut_coords` 逐位相同 ＝ %d/%d 宗**（全側·含鏈頭）⇒ 該側 %s"
          % (same, len(idb), "**已證未動**" if same == len(idb) else "🔴 **已動**"))
    dgmax = max(abs(B[i]["G"] - A[i]["G"]) for i in idb if i in A)
    print("        全側 `|ΔG|` 最大 ＝ %.4f ㎡" % dgmax)

    print("   ── 自我驗證閘 ──")
    if not (gates(mA, "態A") and gates(mB, "態B")):
        print("🔴 自我驗證閘不過 ⇒ ⛔ 據本表下任何結論（⛔ 調框以就結果）")
        return {"refuse": True, "n": n, "gate": False}

    print("   ── `V-1′` 五款（判準一字不動·`1e-6`）──")
    k1a = all(A[i]["N14"] == B[i]["N14"] for i in non_head if i in A)
    print("   `(1a)` 落檔 `宗地寬度(m)` 欄逐宗不變 ⇒ %s" % ("✅" if k1a else "🔴"))
    for i in non_head:
        if i in A:
            print("        %-14s A %-10s｜B %-10s  %s"
                  % (i, A[i]["N14"], B[i]["N14"], "✅" if A[i]["N14"] == B[i]["N14"] else "🔴"))

    k1b, w1 = True, []
    for i in non_head:
        a, b = A.get(i), B.get(i)
        if not a or a["lo"] is None or a["hi"] is None or b["lo"] is None or b["hi"] is None:
            print("        %-14s 末宗（無上界）⇒ **不可得**·具名" % i)
            continue
        d = abs(b["hi"] - b["lo"]) - abs(a["hi"] - a["lo"])
        w1.append(d)
        if abs(d) > TOL_K1:
            k1b = False
        print("        %-14s A %12.9f｜B %12.9f｜Δ %+.9f  %s"
              % (i, abs(a["hi"] - a["lo"]), abs(b["hi"] - b["lo"]), d, "✅" if abs(d) <= TOL_K1 else "🔴"))
    print("   `(1b)` `s` 區間長度逐宗不變 ⇒ %s｜Δ ∈ [%+.9f, %+.9f]"
          % ("✅" if k1b else "🔴", min(w1) if w1 else 0, max(w1) if w1 else 0))

    k2 = (ida == idb)
    print("   `(2)` 鏈序不變 ⇒ %s" % ("✅" if k2 else "🔴"))

    deltas = [(i, B[i]["lo"] - A[i]["lo"]) for i in non_head
              if i in A and A[i]["lo"] is not None and B[i]["lo"] is not None]
    for i, d in deltas:
        print("        %-14s δ ＝ %+.9f" % (i, d))
    if deltas:
        dv = [d for _i, d in deltas]
        spread = max(dv) - min(dv)
        k3 = spread <= TOL_K3
    else:
        spread, k3 = float("nan"), None
    print("   `(3)` `δ` 逐宗同一常數 ⇒ %s｜極差 ＝ %.9f（判準 ≤ %g）"
          % ("✅" if k3 else "🔴", spread, TOL_K3))

    k4 = True
    for tag, m in (("態A", mA), ("態B", mB)):
        res = m["blkarea"] - m["sumG"] - m["sumpool"]
        if abs(res) > 0.05:
            k4 = False
        print("   `(4)` %s ΣG %10.4f ＋ Σ池 %10.4f ＝ %11.4f｜街廓面積 %10.4f｜殘差 %+.4f  %s"
              % (tag, m["sumG"], m["sumpool"], m["sumG"] + m["sumpool"], m["blkarea"], res,
                 "✅" if abs(res) <= 0.05 else "🔴"))

    nz = []
    for i in non_head:
        a, b = A.get(i), B.get(i)
        if not a:
            continue
        dg = b["G"] - a["G"]
        if abs(dg) > 1e-9:
            dd = (b["lo"] - a["lo"]) if (a["lo"] is not None and b["lo"] is not None) else float("nan")
            nz.append((i, dg, dd))
    for i, dg, dd in nz:
        print("   `(5)` 🔑 %-14s ΔG ＝ %+.4f ㎡｜δ ＝ %+.9f" % (i, dg, dd))
    if not nz:
        print("   `(5)` （`ΔG ≠ 0` 之非鏈頭宗 ＝ **0** 宗）")
    print("   ⇒ `(5)` 出艙 %d 宗｜判定集基數 `n` ＝ %d" % (len(nz), n))
    return {"refuse": False, "n": n, "k1a": k1a, "k1b": k1b, "k2": k2, "k3": k3, "k4": k4,
            "n5": len(nz), "same": same, "tot": len(idb)}


def main():
    if len(sys.argv) < 4:
        print("用法：probe_WG9266_V1prime_3groups.py <態A 根> <態B 根> <front_lines.json>")
        return 64
    rootA, rootB, flp = sys.argv[1], sys.argv[2], sys.argv[3]
    fl = json.load(io.open(flp, encoding="utf-8"))
    print("態A ＝ %s／態B ＝ %s／FRONT_LINE ＝ %s（生產解析器之輸出）" % (rootA, rootB, flp))
    print()
    GROUPS = [("陽性", "R2", "left"), ("真陰性", "R1", "right"), ("第三類（`G` 於 2dp 不變而 `cut_coords` 逐位相異之組）", "R2", "right")]
    res = {}
    for role, blk, side in GROUPS:
        res[role] = run(rootA, rootB, blk, side, fl, role)
        print()
    print("=" * 116)
    print("【三組並列之判】")
    print("=" * 116)
    print("  %-46s %-4s %-5s %-5s %-4s %-5s %-4s %-6s" % ("組（受詞逐字）", "n", "(1a)", "(1b)", "(2)", "(3)", "(4)", "(5)"))
    for role, blk, side in GROUPS:
        r = res[role]
        if r.get("refuse"):
            print("  %-46s %-4d 🛑 loud 拒測" % ("3.5m·%s·%s〔%s〕" % (blk, side, role), r["n"]))
            continue
        print("  %-46s %-4d %-5s %-5s %-4s %-5s %-4s %d 宗"
              % ("3.5m·%s·%s〔%s〕" % (blk, side, role[:3]), r["n"],
                 "✅" if r["k1a"] else "🔴", "✅" if r["k1b"] else "🔴",
                 "✅" if r["k2"] else "🔴", "✅" if r["k3"] else "🔴",
                 "✅" if r["k4"] else "🔴", r["n5"]))
    pos, neg, thr = res[GROUPS[0][0]], res[GROUPS[1][0]], res[GROUPS[2][0]]
    if any(x.get("refuse") for x in (pos, neg, thr)):
        print("🛑 有組 loud 拒測 ⇒ 停機")
        return 8
    ok_pos = (pos["n5"] > 0) and (not pos["k1b"]) and (not pos["k3"])
    ok_neg = (neg["n5"] == 0) and neg["k1b"] and neg["k3"]
    ok_thr = (thr["n5"] == 0) and (not thr["k1b"]) and (not thr["k3"])
    print()
    print("  判別力（單 §四 (c) 逐字）：")
    print("    陽性　　須 `(5) > 0` 且 `(1b)`／`(3)` 紅 ⇒ %s" % ("✅" if ok_pos else "🔴"))
    print("    真陰性　須 `(5) = 0` 且 `(1b)`／`(3)` **綠** ⇒ %s" % ("✅" if ok_neg else "🔴"))
    print("    第三類　須 `(5) = 0` 而 `(1b)`／`(3)` 紅 ⇒ %s" % ("✅" if ok_thr else "🔴"))
    same_color = (pos["k1b"] == neg["k1b"] == thr["k1b"]) and (pos["k3"] == neg["k3"] == thr["k3"])
    print("    三者同色？ %s ⇒ %s" % (same_color, "🔴 **閘失能·停機**" if same_color else "✅ **閘⛔ 失能**"))
    return 0 if (ok_pos and ok_neg and ok_thr and not same_color) else 9


if __name__ == "__main__":
    sys.exit(main())
