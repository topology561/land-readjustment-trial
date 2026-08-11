# -*- coding: utf-8 -*-
r"""`W-G.9-7` `H1`／`H2`：對帳器之**鑑別力**與**規則非冗餘**（⛔ 以真實歷史資料為靶）。

## 為何不能用合成竄改交差（施工單 §2-3·§8-2）

本批最大之恆真陷阱＝**用現況 log 凍結、再用現況 log 對帳 ⇒ 必相符**。
故鑑別力之靶取**倉內現成之真實歷史資料**：

| 端 | 資料 | 期望 |
|---|---|---|
| **H1-a** | `verify/out/D2b1_runall.log` × 由其自身凍存之名單 | 類 II、類 III **皆空** |
| **H1-b** | `verify/out/WG94b_runall.log` × **同一份**歷史名單 | 類 III **恰 4 項**，且逐項 ＝ `W-G.9-6` 所具名者 |

🔒 **雙向閘**：**多 ⇒ 正規化不足**（假差異未除）；**少 ⇒ 正規化過度**（真差異被抹）。
⛔ 不得調參數湊到 4。

## `H2`：每條正規化規則皆非冗餘

逐條**移除**該規則後重跑 `H1-b`，其三分類結果**必須改變**；不變者即冗餘。

## 重跑
    python verify/probes/probe_WG97_rules.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import wv_reconcile as WR                                        # noqa: E402

OUT = os.path.join(VERIFY, "out", "probe_WG97_rules.log")
LOG_THEN = os.path.join(VERIFY, "out", "D2b1_runall.log")
LOG_NOW = os.path.join(VERIFY, "out", "WG94b_runall.log")
LIST_HIST = os.path.join(VERIFY, "out", "WG97_歷史凍存_D2b1_名目加原因.txt")

# 🔒 期望值之出處（`fixture-provenance`·⛔ 非本檔現跑回填）：
#   `docs/reports/W-G.9-6_期望FAIL名單守備盤點.md` §3-1 之四項表
#   （其實測 log ＝ `verify/out/probe_WG96_reconcile.log`）。
EXPECT_III = ["v3·StepG0m（結構閘/看守觸發）", "v3·StepG3.5m（結構閘/看守觸發）",
              "W-D.3 碎片", "W-D.4"]
L = []
RC = [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def run(log_path, rules):
    frozen = WR.parse_list(open(LIST_HIST, encoding="utf-8").read())
    cur = WR.parse_log(open(log_path, encoding="utf-8").read())
    return WR.classify(frozen, cur, rules)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    say("=" * 96)
    say("# `W-G.9-7` `H1`／`H2`：對帳器鑑別力（⛔ 真實歷史資料·非合成竄改）")
    say("=" * 96)
    if not os.path.exists(LIST_HIST):
        red(f"歷史凍存名單不存在（{os.path.relpath(LIST_HIST, REPO)}）⇒ ⛔ 不得視為通過")
        return _dump()
    say(f"  歷史凍存名單 ＝ {os.path.relpath(LIST_HIST, REPO)}"
        f"（{len(WR.parse_list(open(LIST_HIST, encoding='utf-8').read()))} 名目）")
    say(f"  🔒 其來源 ＝ `…_D2b1切換後.txt` **檔頭自陳**之來源 log"
        f"（`# 來源 log ：verify/out/D2b1_runall.log`）⇒ 還原入單時之事實，⛔ 非另立標準")

    # ── H1-a ──
    say()
    say("─" * 96)
    say("【H1-a】`D2b1_runall.log` × 歷史凍存 ⇒ 期：類 II、類 III **皆空**")
    say("─" * 96)
    a = run(LOG_THEN, WR.RULES)
    say(f"  類 I {len(a['I'])}（raw 即相同 {len(a['I_raw同'])}）"
        f"｜類 II {len(a['II'])}｜類 III {len(a['III'])}")
    if a["II"] or a["III"]:
        red(f"H1-a 破：類 II={[x[0] for x in a['II']]}／類 III={[x[0] for x in a['III']]}")
    else:
        say("  ✅ H1-a 成立")

    # ── H1-b ──
    say()
    say("─" * 96)
    say("【H1-b】`WG94b_runall.log` × 歷史凍存 ⇒ 期：類 III **恰 4 項**（雙向閘）")
    say("─" * 96)
    b = run(LOG_NOW, WR.RULES)
    got = [x[0] for x in b["III"]]
    say(f"  類 I {len(b['I'])}（raw 即相同 {len(b['I_raw同'])}）"
        f"｜類 II {len(b['II'])}｜類 III {len(b['III'])}")
    say(f"  類 III 實得 ＝ {got}")
    say(f"  類 III 期望 ＝ {EXPECT_III}　（出處：`W-G.9-6` 報告 §3-1·⛔ 非本檔回填）")
    extra = [x for x in got if x not in EXPECT_III]
    miss = [x for x in EXPECT_III if x not in got]
    if extra:
        red(f"**多** {extra} ⇒ **正規化不足**（假差異未除）⛔ 不得調參數湊到 4")
    if miss:
        red(f"**少** {miss} ⇒ **正規化過度**（真差異被抹）⛔ 不得調參數湊到 4")
    if not extra and not miss:
        say("  ✅ H1-b 成立（不多不少·雙向閘皆過）")

    # ── H2 ──
    say()
    say("─" * 96)
    say("【H2】逐條移除正規化規則 ⇒ `H1-b` 之三分類**必須改變**（不變者即冗餘）")
    say("─" * 96)
    base = (len(b["I"]), len(b["II"]), len(b["III"]))
    say(f"  基準（全規則 R1+R2）＝ 類 I/II/III = {base}")
    for rid, desc, _fn in WR.RULES:
        sub = tuple(r for r in WR.RULES if r[0] != rid)
        c = run(LOG_NOW, sub)
        cur = (len(c["I"]), len(c["II"]), len(c["III"]))
        changed = cur != base
        say(f"  移除 {rid}（{desc}）⇒ 類 I/II/III = {cur}"
            f"　{'✅ 已改變（非冗餘）' if changed else '🔴 **未變（冗餘）**'}")
        if not changed:
            red(f"{rid} 冗餘 ⇒ H2 破（該條須刪或說明其為何仍需要）")
    say()
    say("  🔴 **每條規則之盲點**（⛔ 不得留空·見 `verify/wv_reconcile.py` docstring 表）：")
    say("     R1：看不見「路徑分隔符本身改變」⇒ 無法分辨 log 產於 Windows 或 POSIX。")
    say("     R2：看不見「這份 log 產於哪個工作樹／哪個倉」⇒ **誤用他倉基準無法由對帳發現**")
    say("         （前例：`W-G.9-4b` `E4` 之基準產於 `k6a2-d2b21-wiring-6ef500`）。")
    say("         補償＝名單檔頭載來源 log 之倉相對路徑與 `git hash-object`。")

    say()
    say("=" * 96)
    say(f"{'✅ 探針 PASS' if RC[0] == 0 else '🔴 探針 FAIL'}（rc={RC[0]}）")
    say("=" * 96)
    return _dump()


def _dump():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
