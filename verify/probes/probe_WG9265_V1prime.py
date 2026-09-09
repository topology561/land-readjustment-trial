# -*- coding: utf-8 -*-
"""W-G.9-265 工項八：`V-1′` 五款之實走（陽性／陰性二對照）。唯讀探針。

用法：probe_WG9265_V1prime.py <態A 根> <態B 根> <front_lines.json>

🔒 唯讀：只讀二態之 harness 落檔 `verify/out/got_G值_退縮3.5m_partial.csv`
   ＋ 一份自**生產解析器**（`run_verification.build_pipeline` → `cad['front_lines']`）
   匯出之 `FRONT_LINE` 端點。⛔ 動 app.py 與 verify/ 生產路徑一字。

【`V-1′` 五款（單 §九 (b) 逐字·⛔ 增刪）】對該側**非鏈頭**各宗須同時成立——
  (1) 宗地寬度（`s` 區間長度）逐宗不變；
  (2) 鏈序（宗之排列）不變；
  (3) `s` 區間下界之位移 `δ` **逐宗為同一常數**；
  (4) `ΣG ＋ Σ池 ＝ 街廓面積`，覆蓋殘差 ＝ `0`；
  (5) 凡任一非鏈頭宗之 `ΔG ≠ 0`，須逐宗出艙其 `ΔG` 與 `δ`。

【框之來源（逐項具名）】
  · `d̂` ＝ `FRONT_LINE` 之 `p1 → p2` 單位向量 ＝ **生產解析器之輸出**（⛔ 自寫第二份解析）。
  · **界之 `s` 位置** `b_i` ＝ 第 `i` 宗與第 `i+1` 宗之**共用邊**所在直線 × `FRONT_LINE` 之交點
    在 `d̂` 上之座標 ＝ **自擬**。
  · 第 `i` 宗之 `s` 區間 ＝ `[b_{i−1}, b_i]`（`b_{−1}` ＝ 鏈之起界）＝ **自擬**。

【自我驗證閘（⛔ 省）】
  · 閘 `α`：`b_i − b_{i−1}` 須與落檔 `S(m)` 欄（2dp）相符至 `±0.01`。
    ——`S(m)` 係碼面自身對「該宗沿 FRONTLINE 之推進量」之保證（`CLAUDE.md` 三量：`S`＝沿 FRONTLINE）。
  · 閘 `β`：`area(cut_coords)` 須與落檔 `G(㎡)` 相符至 `±0.02`（工項五之已驗性質）。
  · 閘 `γ`：共用邊之認定，逐相鄰對須**恰得 2 個共用頂點**（否則⛔ 得下結論）。
  🛑 任一閘不過 ⇒ ⛔ 據本表下任何結論（rc ≠ 0），⛔ 調框以就結果。
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
QK = 1e-6      # 頂點視為同一點之量子


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
    """回二多邊形之共用頂點（去重·量子 QK）。"""
    sh = []
    for a in cA:
        for b in cB:
            if abs(a[0] - b[0]) < QK and abs(a[1] - b[1]) < QK:
                if not any(abs(a[0] - s[0]) < QK and abs(a[1] - s[1]) < QK for s in sh):
                    sh.append(a)
    return sh


def s_of_line(q1, q2, fp, dh):
    """直線 q1q2 × FRONT_LINE（過 fp 方向 dh）之交點於 dh 上之座標。"""
    ux, uy = dh
    nx, ny = -uy, ux                       # FRONT_LINE 之法向
    # FRONT_LINE: (P − fp)·n = 0
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
        gam.append((items[i][0]["暫編地號"].strip(), items[i + 1][0]["暫編地號"].strip(), len(sh)))
        bounds.append(s_of_line(sh[0], sh[1], fp, dh) if len(sh) == 2 else None)

    lots = []
    for i, (r, cc, p) in enumerate(items):
        lots.append({
            "id": (r.get("暫編地號") or "").strip(),
            "hi": bounds[i] if i < len(bounds) else None,
            "lo": bounds[i - 1] if i >= 1 else None,
            "area": p.area,
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
    print("   ── 閘 γ（共用邊須恰 2 頂點）── [%s]" % tag)
    for a, b, n in m["gam"]:
        good = (n == 2)
        ok &= good
        print("      %-14s × %-14s 共用頂點 %d  %s" % (a, b, n, "✅" if good else "🔴"))
    print("   ── 閘 α（`b_i − b_{i−1}` vs 落檔 `S(m)`·容差 ±0.01）── [%s]" % tag)
    lots = m["lots"]
    for i in range(1, len(lots)):
        lo, hi = lots[i]["lo"], lots[i]["hi"]
        if lo is None or hi is None:
            print("      %-14s（末宗·無上界）跳過" % lots[i]["id"])
            continue
        w = hi - lo
        good = abs(abs(w) - lots[i]["S"]) <= 0.01
        ok &= good
        print("      %-14s 量得 %10.6f｜落檔 S %7.2f｜Δ %+.6f  %s"
              % (lots[i]["id"], abs(w), lots[i]["S"], abs(w) - lots[i]["S"], "✅" if good else "🔴"))
    print("   ── 閘 β（`area` vs 落檔 `G(㎡)`·容差 ±0.02）── [%s]" % tag)
    for d in lots:
        good = abs(d["area"] - d["G"]) <= 0.02
        ok &= good
        print("      %-14s area %10.4f｜G %10.4f｜Δ %+.6f  %s"
              % (d["id"], d["area"], d["G"], d["area"] - d["G"], "✅" if good else "🔴"))
    return ok


def run(rootA, rootB, blk, side, fl, label):
    print("=" * 118)
    print("【%s】%s·%s（情境 3.5m）" % (label, blk, side))
    print("=" * 118)
    mA, mB = measure(rootA, blk, side, fl), measure(rootB, blk, side, fl)
    if mA is None or mB is None:
        print("🔴 一態無該側之列 ⇒ ⛔ 得下結論")
        return None
    print("   `d̂`（生產解析器之 `FRONT_LINE` p1→p2 單位向量）＝ %s"
          % (tuple(round(v, 10) for v in mA["dh"]),))
    if not (gates(mA, "態A") and gates(mB, "態B")):
        print("🔴 自我驗證閘不過 ⇒ ⛔ 據本表下任何結論（⛔ 調框以就結果）")
        return False

    A = {d["id"]: d for d in mA["lots"]}
    B = {d["id"]: d for d in mB["lots"]}
    ida = [d["id"] for d in mA["lots"]]
    idb = [d["id"] for d in mB["lots"]]
    non_head = idb[1:]
    print()
    print("   鏈序 態A ＝ %s" % ida)
    print("   鏈序 態B ＝ %s" % idb)
    print("   鏈頭（第 `0` 宗）＝ 態A %s／態B %s" % (ida[0], idb[0]))
    print("   **非鏈頭**（受詞）＝ %d 宗：%s" % (len(non_head), non_head))

    k2 = (ida == idb)
    print()
    print("   `(2)` 鏈序不變 ⇒ %s" % ("✅" if k2 else "🔴 相異"))

    # `(1)` 之二讀法（單內同款二義·⛔ 靜默擇一）
    print("   `(1a)` 讀法甲 ＝ 落檔 `宗地寬度(m)` 欄（正典 `N-14` 之量·`CLAUDE.md` 三量之「宗地寬度」）")
    k1a = True
    for i in non_head:
        a, b = A.get(i), B.get(i)
        if not a:
            continue
        good = (a["N14"] == b["N14"])
        k1a &= good
        print("      %-14s A %-12s｜B %-12s  %s" % (i, a["N14"], b["N14"], "✅ 逐字相同" if good else "🔴 相異"))
    print("   `(1b)` 讀法乙 ＝ `s` 區間長度（全精度重建·⛔ 用 2dp 欄）")
    k1 = True
    for i in non_head:
        a, b = A.get(i), B.get(i)
        if not a or a["lo"] is None or a["hi"] is None or b["lo"] is None or b["hi"] is None:
            print("      %-14s 末宗（無上界）⇒ **不可得**·具名" % i)
            continue
        wa, wb = abs(a["hi"] - a["lo"]), abs(b["hi"] - b["lo"])
        d = wb - wa
        good = abs(d) <= 1e-6
        k1 &= good
        print("      %-14s A %12.9f｜B %12.9f｜Δ %+.9f  %s" % (i, wa, wb, d, "✅" if good else "🔴"))

    print("   `(3)` `s` 區間下界之位移 `δ` 逐宗為同一常數（非鏈頭·全精度）")
    deltas = []
    for i in non_head:
        a, b = A.get(i), B.get(i)
        if a and a["lo"] is not None and b["lo"] is not None:
            deltas.append((i, b["lo"] - a["lo"]))
    for i, d in deltas:
        print("      %-14s δ ＝ %+.9f" % (i, d))
    if deltas:
        dv = [d for _i, d in deltas]
        spread = max(dv) - min(dv)
        k3 = spread <= 1e-6
        print("      δ 之極差 ＝ %.9f ⇒ %s（判準 ≤ 1e-6）"
              % (spread, "✅ 同一常數" if k3 else "🔴 ⛔ 同一常數"))
    else:
        k3 = None
        print("      🔴 無可比之宗")

    print("   `(4)` `ΣG ＋ Σ池 ＝ 街廓面積`（街廓層·二態各自）")
    k4 = True
    for tag, m in (("態A", mA), ("態B", mB)):
        res = m["blkarea"] - m["sumG"] - m["sumpool"]
        good = abs(res) <= 0.05
        k4 &= good
        print("      %s ΣG %10.4f ＋ Σ池 %10.4f ＝ %11.4f｜街廓面積 %10.4f｜殘差 %+.4f（池 %d 筆）  %s"
              % (tag, m["sumG"], m["sumpool"], m["sumG"] + m["sumpool"], m["blkarea"], res, m["npool"],
                 "✅" if good else "🔴"))

    print("   `(5)` 出艙款：凡任一非鏈頭宗之 `ΔG ≠ 0` ⇒ 逐宗出艙 `ΔG` 與 `δ`")
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
        print("      🔑 %-14s ΔG ＝ %+.4f ㎡｜δ ＝ %+.9f" % (i, dg, dd))
    if not nz:
        print("      （`ΔG ≠ 0` 之非鏈頭宗 ＝ **0** 宗）")
    print("   ⇒ `(5)` 出艙 %d 宗" % len(nz))
    return {"k1": k1, "k2": k2, "k3": k3, "k4": k4, "n5": len(nz), "nz": nz}


def main():
    if len(sys.argv) < 4:
        print("用法：probe_WG9265_V1prime.py <態A 根> <態B 根> <front_lines.json>")
        return 64
    rootA, rootB, flp = sys.argv[1], sys.argv[2], sys.argv[3]
    fl = json.load(io.open(flp, encoding="utf-8"))
    print("態A ＝ %s／態B ＝ %s／FRONT_LINE ＝ %s（生產解析器之輸出）" % (rootA, rootB, flp))
    print()
    pos = run(rootA, rootB, "R2", "left", fl, "陽性對照（單 §九 (c)）")
    print()
    neg = run(rootA, rootB, "R2", "right", fl, "陰性對照（單 §九 (c)）")
    print()
    print("=" * 118)
    print("【`V-1′` 之判】")
    print("=" * 118)
    if not pos or not neg:
        print("🔴 閘不可得 ⇒ 停機")
        return 6
    print("   陽性（`R2·left`）　：(1) %s／(2) %s／(3) %s／(4) %s／(5) 出艙 %d 宗"
          % (pos["k1"], pos["k2"], pos["k3"], pos["k4"], pos["n5"]))
    print("   陰性（`R2·right`）：(1) %s／(2) %s／(3) %s／(4) %s／(5) 出艙 %d 宗"
          % (neg["k1"], neg["k2"], neg["k3"], neg["k4"], neg["n5"]))
    disc = (pos["n5"] > 0) and (neg["n5"] == 0)
    print("   🔑 **判別力**：陽性 `(5)` 出艙 %d 宗、陰性 %d 宗 ⇒ %s"
          % (pos["n5"], neg["n5"],
             "✅ ⛔ 皆零亦⛔ 皆非零 ⇒ 閘**有判別力**" if disc
             else "🔴 二者皆零或皆非零 ⇒ **閘失能、停機**（單 §九 (c) 逐字）"))
    return 0 if disc else 7


if __name__ == "__main__":
    sys.exit(main())
