# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令五 `§二-B` 款 `2`：**翻梯之戶之具名**（值空間定位法）。

🔒 **值空間·⛔ commit 空間**——二端點皆可求值（`7fa957e` 與現態），受詞在**值**上定位。
🛑 **判準（款 `2` 明令）**：翻梯之戶數須 ＝ **`2`** ⋀ 其方向須為 **`0 → 1`**；
  任一不符 ⇒ **停機回報**（`rc = 7`）⇒ 前此之分布差解讀有誤。
🛑 **⛔ 歸因、⛔ 提處置**（補令五 `§七` 款 `7`）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5c_p9p_flip.py <舊態 json> <現態 json>`
`rc`：`0` 如期／`5` 量測器紅（母體不對齊）／`7` 停機（戶數或方向不符）。
"""
import json
import sys

W = 100


def hr(t=""):
    print("\n── %s %s" % (t, "─" * max(0, W - len(t) - 4)))


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def by_gid(d):
    return {g["歸戶鍵Gxxx"]: g for g in d["groups"]}


def main():
    old = load(sys.argv[1])          # 7fa957e 態
    cur = load(sys.argv[2])          # 現態
    print("=" * W)
    print("【`W-G.9-270` 補令五 `§二-B` 款 `2`】**翻梯之戶之具名**（值空間定位·⛔ commit 空間）")
    print("=" * W)
    print("🛑 ⛔ 歸因、⛔ 提處置——照實出艙即止（補令五 `§七` 款 `7`）。")

    rc = 0
    flips_all = {}
    for tag in ("0m", "3.5m"):
        o, c = by_gid(old[tag]), by_gid(cur[tag])
        hr("情境 `退縮 %s`" % tag)
        # ── 母體對齊之自我驗證閘（⛔ 可省）──────────────────────────
        ko, kc = set(o), set(c)
        print("   母體：舊態 %d 戶 ／ 現態 %d 戶 ／ 交集 %d ／ 僅舊 %s ／ 僅現 %s"
              % (len(ko), len(kc), len(ko & kc),
                 sorted(ko - kc) or "（無）", sorted(kc - ko) or "（無）"))
        if ko != kc:
            print("   🔴 **母體不對齊 ⇒ 量測器紅**（歸戶鍵之集合相異）⇒ ⛔ 出艙任何翻梯判")
            rc = 5
            continue
        print("   `tiers`：舊 %s ／ 現 %s"
              % (json.dumps(old[tag]["tiers"], ensure_ascii=False),
                 json.dumps(cur[tag]["tiers"], ensure_ascii=False)))
        print("   `flagged_ct`：舊 %s ／ 現 %s" % (old[tag]["flagged_ct"], cur[tag]["flagged_ct"]))
        print("   `mina_qu`：舊 %s ／ 現 %s" % (old[tag]["mina_qu"], cur[tag]["mina_qu"]))

        flips = [(g, o[g]["梯次"], c[g]["梯次"]) for g in sorted(ko)
                 if o[g]["梯次"] != c[g]["梯次"]]
        flips_all[tag] = flips
        print("\n   **翻梯之戶 ＝ %d 戶**" % len(flips))
        if flips:
            print("   | 歸戶 | 舊梯 | 現梯 | 舊宗數→現宗數 | 舊 ΣG_戶→現 ΣG_戶 | 舊旗標→現旗標 | 舊宗清單 → 現宗清單 |")
            print("   |---|---|---|---|---|---|---|")
            for g, a, b in flips:
                print("   | `%s` | `%s` | `%s` | %s→%s | %s→%s | %s→%s | `%s` → `%s` |"
                      % (g, a, b, o[g]["宗數"], c[g]["宗數"],
                         o[g]["ΣG_戶(㎡)"], c[g]["ΣG_戶(㎡)"],
                         o[g]["含旗標宗數"], c[g]["含旗標宗數"],
                         o[g]["宗清單"], c[g]["宗清單"]))

        # ── 款 `2` 之停機判準 ─────────────────────────────────────
        dirs = set((a, b) for _, a, b in flips)
        ok_n = (len(flips) == 2)
        ok_d = (dirs == {("0", "1")})
        print("\n   款 `2` 之判準：戶數 ＝ `2`？ **%s**（實 %d）／方向 ＝ `0 → 1`？ **%s**（實 %s）"
              % (ok_n, len(flips), ok_d,
                 sorted("%s→%s" % d for d in dirs) or "（無）"))
        if not (ok_n and ok_d):
            print("   🛑 **停機回報**（款 `2` 明令）⇒ 前此之分布差解讀有誤")
            rc = 7

    # ── 全戶之梯次對拍（供發單側覆核·⛔ 只列翻者）──────────────────
    hr("全戶梯次對拍（二情境·⛔ 只列翻者）")
    for tag in ("0m", "3.5m"):
        o, c = by_gid(old[tag]), by_gid(cur[tag])
        same = sum(1 for g in o if g in c and o[g]["梯次"] == c[g]["梯次"])
        print("   [%s] 逐戶相同 %d ／ 相異 %d ／ 合計 %d"
              % (tag, same, len(flips_all.get(tag, [])), len(o)))

    # ── 旗標之逐戶差（款 `3` 路 `(c)` 之材料·⛔ 歸因）────────────────
    hr("旗標（`含旗標宗數`）之逐戶差（款 `3` 路 `(c)` 之材料·🛑 ⛔ 歸因）")
    for tag in ("0m", "3.5m"):
        o, c = by_gid(old[tag]), by_gid(cur[tag])
        diffs = [(g, o[g]["含旗標宗數"], c[g]["含旗標宗數"]) for g in sorted(o)
                 if g in c and o[g]["含旗標宗數"] != c[g]["含旗標宗數"]]
        print("   [%s] 旗標數相異之戶 ＝ %d ／ Σ舊 %d → Σ現 %d"
              % (tag, len(diffs),
                 sum(int(x["含旗標宗數"]) for x in o.values()),
                 sum(int(x["含旗標宗數"]) for x in c.values())))
        for g, a, b in diffs:
            print("     · `%s`  %s → %s" % (g, a, b))
    return rc


if __name__ == "__main__":
    sys.exit(main())
