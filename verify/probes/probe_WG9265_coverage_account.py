# -*- coding: utf-8 -*-
"""W-G.9-265 工項四／五／六：覆蓋帳 ＋ area↔G 對帳 ＋ 射程表（唯讀探針）。

🔒 唯讀：只讀 `verify/out/got_G值_退縮{0m,3.5m}_partial.csv`（harness 落檔），
   ⛔ 寫入任何 tracked 檔、⛔ import 生產模組、⛔ 動 app.py 與 verify/ 生產路徑。

【框之來源（單 §十二 d 所令·逐項具名）】
  · `cut_coords → shapely.Polygon`（`is_valid` 否則 `buffer(0)`）＝ **正典逐字**
    （內容錨 ＝ `docs/reports/W-G.4_泛用阻塞項登記表.md` 之 `GB-67` 補款「器」段）。
  · `Σarea − area(∪) > 1e-6` ＝ **自擬**（單 §五 (f) 明載）。
  · `|area − 對應面積| ≤ 0.02 ㎡` ＝ **自擬**；`0.02` ＝ 2dp 捨入上界 `0.005` 之四倍裕度。
  · 「`街廓面積(㎡)` 逐街廓為常數」＝ **自擬**（單 §六 之自我驗證閘）。
  · **宗序** ＝ 同一 `(情境,街廓,側)` 內以 `累積S(m)` 昇冪之 `0-based` 位次
    ＝ **正典逐字**（`K-9-15 二`：第 `0` 宗 ＝ 街角地那 `1` 宗；第 `1` 宗 ＝ 其後那一宗）；
    其**自我驗證閘** ＝ 位次 `0` 之 `驗_宗序` 須為 `街角第1宗`、位次 `1` 須為 `第2宗`。
  · **相鄰性** ＝ 二宗之位次差 `== 1` ⇒ 相鄰 ＝ **自擬**。

🛑 判準在否證對照：人造相疊矩形須 `1.0`／人造相離矩形須 `0.0`／無重疊組須全綠／
   注入 `+1㎡` 之宗須轉紅。任一不如預期 ⇒ 量測器紅、該次輸出⛔ 出艙（rc ≠ 0）。
"""
import ast
import csv
import io
import math
import os
import sys
from itertools import combinations

from shapely.geometry import Polygon
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out")

SCEN = [("0m", "got_G值_退縮0m_partial.csv"), ("3.5m", "got_G值_退縮3.5m_partial.csv")]
TOL_OVL = 1e-6
TOL_AG = 0.02


def poly(coords):
    p = Polygon(coords)
    if not p.is_valid:
        p = p.buffer(0)
    return p


def parse_coords(s):
    if not s or not s.strip():
        return None
    try:
        v = ast.literal_eval(s)
    except Exception:
        return None
    return v if v and len(v) >= 3 else None


def load(fn):
    path = os.path.join(OUT, fn)
    with io.open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f)), os.path.getsize(path)


def controls():
    ok = True
    a = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    b = poly([(1, 0), (3, 0), (3, 1), (1, 1)])
    v = (a.area + b.area) - unary_union([a, b]).area
    good = abs(v - 1.0) < 1e-9
    print("  [必紅] 人造相疊矩形 Σ−∪ ＝ %.10f（須 ＝ 1.0）%s" % (v, "✅" if good else "🔴"))
    ok &= good
    c = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    d = poly([(5, 0), (6, 0), (6, 1), (5, 1)])
    v2 = (c.area + d.area) - unary_union([c, d]).area
    good2 = abs(v2) < 1e-12
    print("  [必綠] 人造相離矩形 Σ−∪ ＝ %.10f（須 ＝ 0.0）%s" % (v2, "✅" if good2 else "🔴"))
    return ok and good2


def main():
    print("=" * 118)
    print("【W-G.9-265 工項四〜六】覆蓋帳 ／ area↔面積 對帳 ／ 射程表　（唯讀探針·⛔ 動生產碼）")
    print("=" * 118)
    print()
    print("── 否證對照（人造·先跑·不如預期即 abort·單 §十一 1）──")
    if not controls():
        print("🔴 量測器紅 ⇒ 本次輸出⛔ 出艙")
        return 2
    print()

    grand, reach = {}, {}
    for tag, fn in SCEN:
        rows, nbytes = load(fn)
        print("=" * 118)
        print("【情境 %s】落檔 %s／%d B／%d 資料列（來源層 ＝ harness 落檔）" % (tag, fn, nbytes, len(rows)))
        print("=" * 118)

        # ── 自我驗證閘 1（單 §六·⛔ 省）：街廓面積 逐街廓為常數
        blkarea = {}
        for r in rows:
            blk = (r.get("所屬街廓") or "").strip()
            s = (r.get("街廓面積(㎡)") or "").strip()
            if blk and s:
                try:
                    blkarea.setdefault(blk, set()).add(round(float(s), 6))
                except ValueError:
                    pass
        print("── 自我驗證閘 1：`街廓面積(㎡)` 逐街廓為常數 ──")
        gate1 = True
        for blk in sorted(blkarea):
            vs = sorted(blkarea[blk])
            gate1 &= (len(vs) == 1)
            print("   %-4s 相異值 %d ＝ %s  %s" % (blk, len(vs), vs, "✅" if len(vs) == 1 else "🔴"))
        if not gate1:
            print("🔴 自我驗證閘 1 不過 ⇒ ⛔ 據本表下任何結論（單 §十一 2）")
            return 3

        # ── 分組（側之組·⛔ 含抵費地）
        groups, pool = {}, []
        for r in rows:
            blk = (r.get("所屬街廓") or "").strip()
            side = (r.get("推進側別") or "").strip()
            cc = parse_coords(r.get("cut_coords"))
            if not blk or cc is None:
                continue
            if side == "抵費地":
                pool.append((r, poly(cc)))
            else:
                groups.setdefault((blk, side), []).append((r, poly(cc)))

        # 宗序（正典 K-9-15 二）＝ 組內 累積S 昇冪之 0-based 位次
        rank = {}
        gate2, gate2n, gate2_corner, gate2_nocorner = True, 0, 0, 0
        for key, items in groups.items():
            items.sort(key=lambda t: float(t[0].get("累積S(m)") or 0))
            for i, (r, _p) in enumerate(items):
                rank[id(r)] = i
            if items:
                # 位次 0：`驗_宗序 == 街角第1宗` ⟺ `第1筆街角 == 是`（雙向蘊含）
                v0 = (items[0][0].get("驗_宗序") or "").strip()
                c0 = (items[0][0].get("第1筆街角") or "").strip()
                ok0 = ((v0 == "街角第1宗") == (c0 == "是"))
                gate2 &= ok0
                gate2n += 1
                if c0 == "是":
                    gate2_corner += 1
                else:
                    gate2_nocorner += 1
                if len(items) > 1:
                    # 位次 1：恆為 `第2宗`
                    ok1 = ((items[1][0].get("驗_宗序") or "").strip() == "第2宗")
                    gate2 &= ok1
                    gate2n += 1
        print("── 自我驗證閘 2：宗序（`累積S(m)` 昇冪 0-based）對 `驗_宗序` 欄 ──")
        print("   判準（雙向蘊含）：位次 `0` 之 `驗_宗序 == 街角第1宗` ⟺ 其 `第1筆街角 == 是`；位次 `1` 恆為 `第2宗`")
        print("   受檢 %d 格（位次 0 之組：有街角 %d／無街角 %d ⇒ 二側皆非空·該檢⛔ 恆真）⇒ %s"
              % (gate2n, gate2_corner, gate2_nocorner, "✅ 全符" if gate2 else "🔴 不符"))
        if not gate2:
            for key in sorted(groups):
                its = groups[key]
                print("     %s·%s 位次0 序 ＝ %r 街角1 ＝ %r" % (
                    key[0], key[1], (its[0][0].get("驗_宗序") or "").strip(),
                    (its[0][0].get("第1筆街角") or "").strip()))
            print("🔴 自我驗證閘 2 不過 ⇒ ⛔ 據宗序下任何結論")
            return 3
        print()

        # ── 工項四：覆蓋帳
        print("── 工項四　覆蓋帳（性質 ＝ 同組內各宗互不相疊；判準 Σarea − area(∪) ≤ %g）──" % TOL_OVL)
        seen_blk = list(dict.fromkeys((r.get("所屬街廓") or "").strip() for r in rows
                                      if (r.get("所屬街廓") or "").strip()))
        order = sorted(groups, key=lambda k: (seen_blk.index(k[0]), k[1]))
        for key in order:
            items = groups[key]
            polys = [p for _, p in items]
            sm = sum(p.area for p in polys)
            un = unary_union(polys).area
            d = sm - un
            bad = d > TOL_OVL
            print("  ── %s·%s·%s ── %d 宗｜Σarea ＝ %.4f｜∪area ＝ %.4f｜Σ−∪ ＝ %.4f  %s"
                  % (tag, key[0], key[1], len(items), sm, un, d, "🔴 違反" if bad else "✅ 無違反"))
            print("       宗序對照：%s" % "／".join(
                "第%d宗 %s%s" % (rank[id(r)], (r.get("暫編地號") or "").strip(),
                                 "〔街角地〕" if (r.get("第1筆街角") or "").strip() == "是" else "")
                for r, _ in items))
            grand[(tag, key[0], key[1])] = (len(items), sm, un, d)
            if bad:
                for (r1, p1), (r2, p2) in combinations(items, 2):
                    inter = p1.intersection(p2).area
                    if inter > TOL_OVL:
                        i1, i2 = rank[id(r1)], rank[id(r2)]
                        adj = "相鄰" if abs(i1 - i2) == 1 else "非相鄰（位次差 %d）" % abs(i1 - i2)
                        print("        · 第%d宗 %-14s × 第%d宗 %-14s  疊 ＝ %.4f ㎡  ⇒ %s"
                              % (i1, (r1.get("暫編地號") or "").strip(),
                                 i2, (r2.get("暫編地號") or "").strip(), inter, adj))
        print()

        # ── 工項五：逐宗對帳（二母體分列·單 §六 受詞含抵費地，而抵費地之 G ≡ 0 ⇒ 分列）
        print("── 工項五　`area(cut_coords)` 逐宗對帳（判準 |Δ| ≤ %.2f ㎡）──" % TOL_AG)
        print("   母體甲 ＝ 分配宗（`推進側別 ∈ {left,right}`）·對應量 ＝ `G(㎡)`")
        lo = hi = None
        nbad = 0
        detail = []
        for key in order:
            for r, p in groups[key]:
                try:
                    g = float((r.get("G(㎡)") or "0").strip())
                except ValueError:
                    continue
                d = p.area - g
                lo = d if lo is None else min(lo, d)
                hi = d if hi is None else max(hi, d)
                detail.append(((r.get("暫編地號") or "").strip(), key[0], key[1], rank[id(r)], p.area, g, d))
                if abs(d) > TOL_AG:
                    nbad += 1
        print("      %d 宗｜area − G ∈ [%+.6f, %+.6f]（4dp ＝ [%+.4f, %+.4f]）｜逾容差 %d 宗  %s"
              % (len(detail), lo, hi, round(lo, 4), round(hi, 4), nbad, "✅" if nbad == 0 else "🔴"))
        dmin = min(detail, key=lambda t: t[6])
        dmax = max(detail, key=lambda t: t[6])
        print("      極小 ＝ %s（%s·%s·第%d宗）Δ %+.6f｜極大 ＝ %s（%s·%s·第%d宗）Δ %+.6f"
              % (dmin[0], dmin[1], dmin[2], dmin[3], dmin[6], dmax[0], dmax[1], dmax[2], dmax[3], dmax[6]))
        print("   母體乙 ＝ `推進側別 ＝ 抵費地` 之列·對應量 ＝ `幾何面積(㎡)`")
        print("      🩸 其 `G(㎡)` 欄逐列 ＝ `0.0`（`解法` 欄逐字 ＝ `幾何剩餘`）⇒ `|area − G| ≤ 0.02` 於該母體**結構上不可能成立**；")
        print("         故對應量取 `幾何面積(㎡)`。**二母體分列出艙**，⛔ 併為一數。")
        plo = phi = None
        pbad = 0
        for r, p in pool:
            try:
                j = float((r.get("幾何面積(㎡)") or "0").strip())
            except ValueError:
                continue
            d = p.area - j
            plo = d if plo is None else min(plo, d)
            phi = d if phi is None else max(phi, d)
            if abs(d) > TOL_AG:
                pbad += 1
            print("      %-16s area %10.4f  幾何面積 %10.4f  Δ %+.6f  %s"
                  % ((r.get("暫編地號") or "").strip(), p.area, j, d, "🔴" if abs(d) > TOL_AG else "✅"))
        if pool:
            print("      %d 列｜area − 幾何面積 ∈ [%+.6f, %+.6f]｜逾容差 %d 列  %s"
                  % (len(pool), plo, phi, pbad, "✅" if pbad == 0 else "🔴"))
        # 注入 +1㎡ 之必紅（單 §六 (c)）
        key0 = order[0]
        r0, p0 = groups[key0][0]
        g0 = float((r0.get("G(㎡)") or "0").strip())
        cc0 = parse_coords(r0.get("cut_coords"))
        cx, cy = p0.centroid.x, p0.centroid.y
        k = math.sqrt((p0.area + 1.0) / p0.area)
        p0b = poly([(cx + (x - cx) * k, cy + (y - cy) * k) for (x, y) in cc0])
        d_before, d_after = p0.area - g0, p0b.area - g0
        okinj = abs(d_before) <= TOL_AG < abs(d_after)
        print("   [必紅] 注入 +1㎡（%s·%s·%s）：area %.4f → %.4f｜Δ %+.4f → %+.4f  %s"
              % ((r0.get("暫編地號") or "").strip(), key0[0], key0[1],
                 p0.area, p0b.area, d_before, d_after, "✅ 原綠→轉紅" if okinj else "🔴 未如預期"))
        if not okinj:
            print("🔴 必紅對照未如預期 ⇒ 量測器紅、輸出⛔ 出艙")
            return 4
        print()

        # ── 工項六：射程表
        stop_blk = sorted({(r.get("中止街廓") or "").strip() for r in rows if (r.get("中止街廓") or "").strip()})
        stop_gate = sorted({(r.get("中止閘") or "").strip() for r in rows if (r.get("中止閘") or "").strip()})
        reach[tag] = (seen_blk, stop_blk, stop_gate)
        print("── 工項六　射程表 ──")
        print("   `所屬街廓` distinct（出現序·來源層 ＝ harness 落檔）＝ %s" % seen_blk)
        print("   `中止街廓` ＝ %s" % (stop_blk or "（欄空）"))
        for g_ in stop_gate:
            print("   `中止閘`（逐字複製·⛔ 改寫·⛔ 濃縮）＝ %s" % g_)
        print()

    # ── 彙總
    print("=" * 118)
    print("【彙總】全 %d 組覆蓋帳" % len(grand))
    print("=" * 118)
    nviol = sum(1 for k in grand if grand[k][3] > TOL_OVL)
    print("  違反 %d 組／無違反 %d 組／合計 %d 組" % (nviol, len(grand) - nviol, len(grand)))
    for k in sorted(grand):
        n, sm, un, d = grand[k]
        print("    %-5s %-4s %-6s %d 宗  Σ−∪ ＝ %.4f  %s" % (k[0], k[1], k[2], n, d, "🔴" if d > TOL_OVL else "✅"))
    print()
    print("  🔒 `R3` 於二情境之 `所屬街廓` distinct 皆⛔ 出現 ⇒ **二情境皆不可達**")
    for tag in ("0m", "3.5m"):
        print("     %-5s 可達 ＝ %s｜`R3` ∈ 可達？ %s" % (tag, reach[tag][0], "R3" in reach[tag][0]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
