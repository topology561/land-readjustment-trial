# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令五 `§二-B` 款 `3`：**翻梯之受詞之三路逐一判**（⛔ 擇一書之）。

🔒 **`_qual(r)` 逐字**（`verify/wd4_tier_list.py`·⛔ 另寫第二份判準）：
  `return (float(r.get("G(㎡)", 0) or 0) >= mina.get(r["所屬街廓"], 1e9)`
  `        and not str(r.get("畸零地旗標", "")).strip())`
  `all_qual = bool(lots) and all(_qual(r) for r in lots)`
⇒ 梯 `0 → 1` ⟺ `all_qual` 由 `False` 轉 `True`。恰有**三條**路：
  `(a)` 該戶某宗之 `G(㎡)` **升**（價格相依）
  `(b)` 該宗所屬街廓之 `mina[街廓]` **降**
  `(c)` 該宗之 `畸零地旗標` **消失**

🛑 **⛔ 逕取其一**——三路**逐一判其是否為因**（補令五 `§二-B` 款 `3` 明令）。
🛑 **⛔ 歸因逾此**（`§七` 款 `7`）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5c_p9p_three.py <舊 rows json> <現 rows json> <歸戶...>`
`rc`：`0` 量測成立／`5` 量測器紅。
"""
import json
import sys

W = 104


def hr(t=""):
    print("\n── %s %s" % (t, "─" * max(0, W - len(t) - 4)))


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def qual(r, mina):
    g = float(r.get("G(㎡)", 0) or 0)
    m = mina.get(r["所屬街廓"], 1e9)
    flag = str(r.get("畸零地旗標", "") or "").strip()
    return (g >= m) and (not flag), g, m, flag


def main():
    old, cur = load(sys.argv[1]), load(sys.argv[2])
    gids = sys.argv[3:]
    print("=" * W)
    print("【`W-G.9-270` 補令五 `§二-B` 款 `3`】**三路逐一判**（⛔ 擇一書之）")
    print("=" * W)
    print("🛑 ⛔ 歸因逾此（`§七` 款 `7`）。")

    hr("路 `(b)`　`mina[街廓]` 之二態並列（全街廓）")
    print("   | 街廓 | 舊態 | 現態 | 判 |")
    print("   |---|---|---|---|")
    降 = []
    for k in sorted(set(old["mina"]) | set(cur["mina"])):
        a, b = old["mina"].get(k), cur["mina"].get(k)
        d = "同" if a == b else ("🔴 **降**" if (b is not None and a is not None and b < a) else "🔴 升")
        if a is not None and b is not None and b < a:
            降.append(k)
        print("   | `%s` | `%s` | `%s` | %s |" % (k, a, b, d))
    print("   ⇒ **`mina` 下降之街廓 ＝ %s**" % (降 or "（無）"))
    print("   ⇒ 🔒 路 `(b)` %s" % ("**成立**（有街廓之 mina 降）" if 降 else "**⛔ 成立**——無一街廓之 `mina` 降"))

    rc = 0
    for tag in ("0m", "3.5m"):
        for gid in gids:
            o = old["by_tag"][tag]["per_gid"].get(gid, [])
            c = cur["by_tag"][tag]["per_gid"].get(gid, [])
            hr("情境 `退縮 %s`　歸戶 `%s`　逐宗四欄（⛔ 強行配對·二態宗集相異）" % (tag, gid))
            for lab, rows, mina in (("舊態", o, old["mina"]), ("現態", c, cur["mina"])):
                print("   **%s**（%d 宗）" % (lab, len(rows)))
                print("   | 暫編地號 | 所屬街廓 | `G(㎡)` | `mina[街廓]` | `G ≥ mina`? | 畸零地旗標 | `_qual` |")
                print("   |---|---|---|---|---|---|---|")
                for r in rows:
                    q, g, m, flag = qual(r, mina)
                    print("   | `%s` | `%s` | `%s` | `%s` | %s | `%s` | %s |"
                          % (r["暫編地號"], r["所屬街廓"], g, m,
                             "✅" if g >= m else "🔴 **否**",
                             flag or "（無）", "✅" if q else "🔴 **否**"))
                allq = bool(rows) and all(qual(r, mina)[0] for r in rows)
                print("   ⇒ `all_qual` ＝ **%s**" % allq)
            # ── 三路之逐一判（就本戶本情境）────────────────────────
            bad_old = [r for r in o if not qual(r, old["mina"])[0]]
            print("\n   🔑 **舊態⛔ `_qual` 之宗 ＝ %d**" % len(bad_old))
            for r in bad_old:
                q, g, m, flag = qual(r, old["mina"])
                why = []
                if g < m:
                    why.append("`G %s < mina %s`" % (g, m))
                if flag:
                    why.append("**畸零地旗標 ＝ `%s`**" % flag)
                print("     · `%s`（`%s`）⛔ qual 之由 ＝ %s" % (r["暫編地號"], r["所屬街廓"], " ⋀ ".join(why)))
            if not o:
                print("   🔴 舊態之宗集為空 ⇒ **量測器紅**（母體 `0`·坑 `al`）")
                rc = 5
    return rc


if __name__ == "__main__":
    sys.exit(main())
