# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令一 `§四`：**`p4` 梯次門檻之跨機不可判帶**（零生產碼·唯讀·量測與提案）。

🛑 本器**全唯讀**：⛔ 寫任何生產碼、⛔ 寫 `verify/baselines`、⛔ 設 `WV_BAKE`、
  ⛔ 落地該帶（其須動 `verify/wd4_tier_list.py` ＝ 生產碼 `34` 檔之一 ⇒ 他批 ＋ KL 放行）。
🔒 **真相源** ＝ `verify.wd4_tier_list.compute(fixture=False)`（**記憶體側**·該函式⛔ 寫任何檔·
  正面列舉：其 `183`–`399` 區間內之寫檔命中僅 `open(rv.V6DXF, "rb")` 一處 ⇒ 合 `GB-162` 三禁令）。

🔒 **四款（補令一 `§四`）**
  `1` `ε` 之出處具名——⛔ 以口語之 `0.05` 代之。
  `2` 全戶落位表（二情境 × 建地軌全戶）；母體須完整並具名基數；公設軌之排除須具名其由。
  `3` 最壞情形——建地軌中**宗數最多**之戶及其帶寬（帶寬之上界）。
  `4` 提案（⛔ 動生產碼一字）。

🔒 **式（補令一 `§三-1` 逐字）**：`跨機帶寬 ＝ 2 × 宗數 × ε`；
  判定式（`verify/wd4_tier_list.py:436` 之形）＝ `2×ΣG_戶 ≥ MinA_區`（整數倍·無除法無二次 round）。

🔒 **`MinA_區` ⛔ 擇一（`CLAUDE.md` 之四值並列 ＋ 補令三 `§四` 明令二值並報）**
  本器對每一候選各算一欄，並逐欄具名其**角色**（`VR-091 一 (3)`／作業紀律 `7`）。

🔒 **判別力二造（⛔ 恆綠亦⛔ 恆紅）**
  造甲[必落帶] 人造一戶，其 `2ΣG` 恰等於 `MinA_區` ⇒ 距 `0` ⇒ 須判**落帶**。
  造乙[必不落帶] 人造一戶，其距為帶寬之 `100` 倍 ⇒ 須判**正常**。
  二者皆須如期，否則 `rc = 5`（**量測器紅**·⛔ 出艙任何落位判）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5_p4_tier_band.py [倉根]`
`rc`：`0` 量測成立／`5` 量測器紅／`6` 母體不自洽。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)

# 🔒 `ε` 之出處（`p4` 款 `1`·⛔ 口語）
#   實測值 ＝ 0.04 ㎡ —— `GB-101` 原文逐字：「差達 `0.04 ㎡`」；其逐值坐實 ＝
#     `R4` 左 `628(1)` 之 `幾何面積(㎡)` KL `1521.09` vs CC `1521.05`（差 0.04）。
#   所取之保守值 ＝ 0.05 ㎡ —— `GB-101` 原文之**過渡紀律**逐字：
#     「凡以 `G` 或 `幾何面積` 作跨環境對拍者，**容差一律 `±0.05 ㎡`**，⛔ 不得用 `±0.01`」。
#   其由 ＝ 該值係倉內**明文之紀律**（⛔ 本器自訂）；KL 已於 `2026-09-10` 裁「`GB-101` 可」。
EPS_MEASURED = 0.04     # 角色 ＝ 實測值（GB-101 原文）
EPS_CONSERV = 0.05      # 角色 ＝ 所取之保守值（GB-101 過渡紀律逐字）

# 🔒 `MinA_區` 之候選（⛔ 擇一·逐欄具名角色）
#   `mina_live` 於執行期自 `compute()` 取得，⛔ 硬編。
MINA_CANDIDATES = [
    ("115.85", 115.85, "CLAUDE.md 之現值記載（½ 顯示 57.93）"),
    ("114.07", 114.07, "期望值·斷言錨（wd4_tier_list.MINA_QU_EXPECT／W-D.4 規格）⛔ 現值"),
]

W = 78


def hr(t=""):
    print("\n── %s %s" % (t, "─" * max(0, W - len(t) - 4)))


def band(n_lots, eps):
    """跨機帶寬 ＝ 2 × 宗數 × ε（補令一 §三-1 逐字）"""
    return 2.0 * n_lots * eps


def classify(dist, bw):
    """|2ΣG − MinA| ≤ 帶寬 ⇒ 落帶（梯次跨機可翻）"""
    return "🔴 落帶" if abs(dist) <= bw else "正常"


def selftest():
    """判別力二造——⛔ 恆綠亦⛔ 恆紅"""
    hr("判別力二造（`p4` 之落帶判準）")
    ok = True
    # 造甲[必落帶]：2ΣG 恰等於 MinA ⇒ 距 0
    bw_a = band(2, EPS_CONSERV)
    ja = classify(0.0, bw_a)
    oa = ja.endswith("落帶")
    print("   造甲[必落帶] 宗數 2·距 0.0000·帶寬 ±%.4f ⇒ %s  期 落帶 %s"
          % (bw_a, ja, "✅" if oa else "🔴"))
    # 造乙[必不落帶]：距 ＝ 帶寬之 100 倍
    bw_b = band(2, EPS_CONSERV)
    jb = classify(bw_b * 100.0, bw_b)
    ob = (jb == "正常")
    print("   造乙[必不落帶] 宗數 2·距 %.4f（＝帶寬 ×100）·帶寬 ±%.4f ⇒ %s  期 正常 %s"
          % (bw_b * 100.0, bw_b, jb, "✅" if ob else "🔴"))
    ok = oa and ob
    print("   ⇒ **器%s**" % ("非紅 ✅" if ok else "紅 🔴"))
    return ok


def main():
    print("=" * W)
    print("【`W-G.9-270` 補令一 `§四`】`p4` 梯次門檻之跨機不可判帶（零生產碼·唯讀）")
    print("=" * W)

    if not selftest():
        print("\n🛑 **量測器紅** ⇒ ⛔ 出艙任何落位判。")
        return 5

    hr("款 `1`　`ε` 之出處（⛔ 口語）")
    print("   實測值      ε ＝ %.2f ㎡   出處 ＝ `GB-101` 原文逐字「差達 `0.04 ㎡`」" % EPS_MEASURED)
    print("                            逐值 ＝ `R4` 左 `628(1)` 幾何面積 KL `1521.09` vs CC `1521.05`")
    print("   所取保守值  ε ＝ %.2f ㎡   出處 ＝ `GB-101` 原文之**過渡紀律**逐字：" % EPS_CONSERV)
    print("                            「凡以 `G` 或 `幾何面積` 作跨環境對拍者，容差一律 `±0.05 ㎡`」")
    print("   其由        ＝ 該值係倉內**明文之紀律**（⛔ 本器自訂）；KL `2026-09-10` 裁「`GB-101` 可」")
    print("   🔒 本器二值並算（下表之帶寬欄二者並列）。")

    from wd4_tier_list import compute, MINA_QU_EXPECT, HALF_EXPECT
    print("\n   碼面之期望值錨（逐字·角色 ＝ 期望值·斷言錨·⛔ 現值）：")
    print("     MINA_QU_EXPECT = %s ／ HALF_EXPECT = %s" % (MINA_QU_EXPECT, HALF_EXPECT))

    res = compute(fixture=False)

    worst_all = []
    for tag in ("0m", "3.5m"):
        d = res[tag]
        mina_live = d["mina_qu"]
        groups = d["groups"]
        cands = list(MINA_CANDIDATES) + [
            ("%.2f" % mina_live, float(mina_live), "**活體實算**（compute() 之 `mina_qu`）＝ 現值")]

        hr("情境 `退縮 %s`　母體與基數" % tag)
        print("   群組總數 ＝ %d" % len(groups))
        tr = {}
        ti = {}
        for g in groups:
            tr[g["軌別"]] = tr.get(g["軌別"], 0) + 1
            ti[g["梯次"]] = ti.get(g["梯次"], 0) + 1
        print("   軌別分布 ＝ %s   （Σ ＝ %d）" % (tr, sum(tr.values())))
        print("   梯次分布 ＝ %s   （Σ ＝ %d）" % (ti, sum(ti.values())))
        if sum(tr.values()) != len(groups) or sum(ti.values()) != len(groups):
            print("   🔴 母體不自洽 ⇒ 停")
            return 6
        print("   ✅ 自洽驗算：Σ軌別 ＝ Σ梯次 ＝ 群組總數")
        print("   `MinA_區` 活體實算 ＝ %s ／ ½ 顯示 ＝ %s" % (mina_live, d["half_disp"]))

        bd = [g for g in groups if g["軌別"] == "建地軌"]
        other = [g for g in groups if g["軌別"] != "建地軌"]
        print("   建地軌 ＝ %d 戶（本表之母體）／非建地軌 ＝ %d 戶" % (len(bd), len(other)))
        print("   🔒 非建地軌之排除之由（逐字·⛔ 靜默排除）：")
        for g in other:
            print("     · %s  軌別=%s  梯次=%s  路徑標註=%s"
                  % (g["歸戶鍵Gxxx"], g["軌別"], g["梯次"], str(g["路徑標註"])[:76]))

        hr("情境 `退縮 %s`　款 `2`：建地軌全戶落位表（⛔ 擇一 MinA·三欄並列）" % tag)
        print("   帶寬 ＝ 2 × 宗數 × ε　｜　距 ＝ 2ΣG_戶 − MinA_區　｜　落帶 ⟺ |距| ≤ 帶寬")
        hdr = "   | 歸戶 | 宗數 | ΣG_戶(㎡) | 梯次 |"
        for nm, _v, _r in cands:
            hdr += " 距@%s | 距/帶(ε=.05) | 判@%s |" % (nm, nm)
        print(hdr)
        rows = []
        for g in sorted(bd, key=lambda x: x["歸戶鍵Gxxx"]):
            n = int(g["宗數"])
            sg = float(g["ΣG_戶(㎡)"])
            bw5 = band(n, EPS_CONSERV)
            bw4 = band(n, EPS_MEASURED)
            line = "   | %s | %d | %.2f | %s |" % (g["歸戶鍵Gxxx"], n, sg, g["梯次"])
            rec = {"gid": g["歸戶鍵Gxxx"], "n": n, "sg": sg, "tier": g["梯次"],
                   "bw5": bw5, "bw4": bw4, "d": {}}
            for nm, v, _r in cands:
                dist = 2.0 * sg - v
                ratio = abs(dist) / bw5 if bw5 else float("inf")
                rec["d"][nm] = (dist, ratio, classify(dist, bw5))
                line += " %+.4f | %.1f× | %s |" % (dist, ratio, classify(dist, bw5))
            print(line)
            rows.append(rec)

        hr("情境 `退縮 %s`　最緊之戶（逐候選具名）" % tag)
        for nm, _v, role in cands:
            tight = min(rows, key=lambda r: r["d"][nm][1])
            dist, ratio, jd = tight["d"][nm]
            print("   MinA_區 ＝ %s（%s）" % (nm, role))
            print("     最緊 ＝ %s  宗數 %d  ΣG %.2f  距 %+.4f  帶寬 ±%.4f(ε=.05) / ±%.4f(ε=.04)"
                  % (tight["gid"], tight["n"], tight["sg"], dist, tight["bw5"], tight["bw4"]))
            print("     距／帶寬 ＝ %.1f×(ε=.05) / %.1f×(ε=.04)   判 ＝ %s"
                  % (ratio, abs(dist) / tight["bw4"] if tight["bw4"] else float("inf"), jd))
            inband = [r for r in rows if r["d"][nm][2].endswith("落帶")]
            print("     落帶之戶 ＝ %d 戶 %s"
                  % (len(inband), [r["gid"] for r in inband] if inband else "（無）"))
            worst_all.append((tag, nm, tight["gid"], ratio, len(inband)))

        hr("情境 `退縮 %s`　款 `3`：最壞情形（宗數最多之戶 ＝ 帶寬之上界）" % tag)
        mx = max(rows, key=lambda r: r["n"])
        print("   宗數最多 ＝ %s（宗數 %d）⇒ 帶寬上界 ±%.4f ㎡(ε=.05) ／ ±%.4f ㎡(ε=.04)"
              % (mx["gid"], mx["n"], mx["bw5"], mx["bw4"]))
        print("   其 ΣG_戶 ＝ %.2f，梯次 ＝ %s" % (mx["sg"], mx["tier"]))
        for nm, _v, _r in cands:
            dist, ratio, jd = mx["d"][nm]
            print("     @%s：距 %+.4f ⇒ %.1f×(ε=.05) ⇒ %s" % (nm, dist, ratio, jd))

    # ── 併辦：補令一 `§一-1`／`§一-2` 之當場復現（⛔ 轉引發單側之表）──────────────
    hr("併辦　補令一 `§一-1`／`§一-2` 之復現（三戶 ＋ 全梯 2/3 戶）")
    print("   🛑 `GB-159`：受影響之宗之配地圖與負擔表 **⛔ 對外**（含本節之補償數）。")
    print("   🔒 三項齊載（補令一 `§一-2` 明令）：`(1)` 估算性質　`(2)` 時態錨　`(3)` `GB-159` 之⛔ 對外。")
    for tag in ("0m", "3.5m"):
        d = res[tag]
        print("   ── 情境 `退縮 %s`（`MinA_區` 活體 ＝ %s）" % (tag, d["mina_qu"]))
        for g in sorted(d["groups"], key=lambda x: x["歸戶鍵Gxxx"]):
            if g["梯次"] not in ("2", "3"):
                continue
            print("     · %s 梯%s 宗數%d ΣG=%.2f ｜ 2ΣG≥MinA? %s ｜ 增配a′=%s ｜ §52-1=%s"
                  % (g["歸戶鍵Gxxx"], g["梯次"], int(g["宗數"]), float(g["ΣG_戶(㎡)"]),
                     ("達" if 2.0 * float(g["ΣG_戶(㎡)"]) >= float(d["mina_qu"]) else "未達"),
                     g["增配a′(㎡)"], g["差額地價(元)§52-1"]))
            print("       §53-2 放棄改領=%s ｜ **§53-1 本文式=%s** ｜ 但書式=%s ｜ 估算性質=%s"
                  % (g["放棄改領(元)§53-2"], g["補償_本文式(元)§53-1"],
                     g["補償_但書式(元)"], g["估算性質"]))

    hr("跨情境彙總（逐候選·⛔ 擇一）")
    for tag, nm, gid, ratio, nin in worst_all:
        print("   %-5s @%-7s 最緊 ＝ %s（%.1f×）  落帶戶數 ＝ %d" % (tag, nm, gid, ratio, nin))
    print("\n🔒 **現態之判**：見上各欄「落帶之戶」——其為**現態之事實**，")
    print("   🛑 **⛔ 以之為由不設該帶**（`GB-164` 受詞逐字：「其為現態之事實，⛔ 結構之保證」）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
