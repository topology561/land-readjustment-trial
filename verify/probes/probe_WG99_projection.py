# -*- coding: utf-8 -*-
r"""`W-G.9-9` `K1`／`K4`：呈現層敏感度之**倉內合成**驗證（⛔ 不依賴任何外部觀測）。

## 命題

- **`K1`**：**現行**凍存物（`W-G.9-8` 之未投影版）含 traceback **呈現層** token，
  且 `wv_reconcile` 對其變動**敏感** ⇒ 合成變動後該項落入**類 III**。
- **`K4`**：**投影後**（`W-G.9-9`）對**同一份**合成變動**不再敏感** ⇒ **仍綠**。

🔒 二者用**同一份合成輸入**，差別只在「有無投影」——⇒ 此為投影效果之**單變因**證明。

## 合成之三種機械變動（⛔ 皆只動呈現層·不動 `raise` 幀與例外訊息）

| # | 變動 | 屬性 |
|---|---|---|
| **M1** | 錯誤位置標記行 `~~~~^^` → `^^^^^^` | 直譯器標記樣式 |
| **M2** | 摺疊 `...<4 lines>...` → 展開為兩行原始碼列 | 摺疊呈現 |
| **M3** | 上游幀之原始碼列重排（換行位置改變） | 呼叫處寫法 |

⛔ **不改動**：`raise` 所在之 `File` 幀、例外型別、例外訊息 ⇒ **真受詞逐字未變**。

## 重跑
    python verify/probes/probe_WG99_projection.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import wv_reconcile as WR                                          # noqa: E402
from fixture_e2e_termination import _record                        # noqa: E402

OLD = os.path.join(VERIFY, "out", "WG98_端到端複本_終止點凍存.txt")
OUT = os.path.join(VERIFY, "out", "probe_WG99_projection.log")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def mutate(det):
    """三種呈現層變動（⛔ 不動 raise 幀與例外訊息）。回 (新記錄, 命中數 dict)。"""
    out, hits = [], {"M1": 0, "M2": 0, "M3": 0}
    for x in det:
        if "~~~" in x and "^^" in x:
            out.append(x.replace("~", "^"))
            hits["M1"] += 1
        elif re.search(r"\.\.\.<\d+ lines>\.\.\.", x):
            ind = " " * (len(x) - len(x.lstrip()))
            out.append(ind + 'f"（合成展開之第 1 行）"')
            out.append(ind + 'f"（合成展開之第 2 行）"')
            hits["M2"] += 1
        elif x.strip().startswith("sg = run_step_g("):
            out.append(x.replace("run_step_g(ns, fake_st,", "run_step_g(\n        ns, fake_st,")
                       .replace("\n", " "))
            hits["M3"] += 1
        else:
            out.append(x)
    return out, hits


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    say("=" * 100)
    say("# `W-G.9-9` `K1`／`K4`：呈現層敏感度（⛔ 倉內合成·不依賴外部觀測）")
    say("=" * 100)
    # 🔒 考古 67 修法 ①：比較前先斷言兩端存在且非空
    if not os.path.exists(OLD):
        red(f"現行凍存不存在（{os.path.relpath(OLD, REPO)}）")
        return _dump()
    base = WR.parse_list(open(OLD, encoding="utf-8").read())
    if not base:
        red("現行凍存解析出 0 筆 ⇒ ⛔ 空集合不得算通過")
        return _dump()
    say(f"  現行凍存（**未投影**）＝ {os.path.relpath(OLD, REPO)}（{len(base)} 支）")

    mut, tot = [], {"M1": 0, "M2": 0, "M3": 0}
    for nm, det in base:
        nd, h = mutate(det)
        mut.append((nm, nd))
        for k in tot:
            tot[k] += h[k]
    say(f"  合成變動命中：M1 標記行 {tot['M1']}｜M2 摺疊 {tot['M2']}｜M3 原始碼列 {tot['M3']}")
    if sum(tot.values()) == 0:
        red("三種合成變動**皆 0 命中** ⇒ 本探針無受詞（⛔ 空不算通過）")
        return _dump()

    say()
    say("─" * 100)
    say("【輸入樣本】`wg_g1_smoke.py` 之變動行（原 → 合成）")
    say("─" * 100)
    for a, b in zip(base[0][1], mut[0][1]):
        if a != b:
            say(f"  原  : {a[:96]}")
            say(f"  合成: {b[:96]}")

    # ── K1：未投影 ⇒ 應敏感（類 III）──────────────────────────────────
    say()
    say("─" * 100)
    say("【K1】**未投影**：現行凍存 × 合成變動 ⇒ 期 **類 III 非空**（敏感）")
    say("─" * 100)
    r1 = WR.classify(base, mut)
    say(f"  類 I {len(r1['I'])}｜類 II {len(r1['II'])}｜**類 III {len(r1['III'])}**"
        f"　⇒ {[n for n, _ in r1['III']]}")
    if r1["III"]:
        say("  ✅ **`K1` 成立**：對帳器對呈現層變動**敏感** ⇒ 現行凍存受詞過寬")
    else:
        red("`K1` 破 ⇒ 對帳器對呈現層不敏感 ⇒ 本批前提錯誤（`W-1` 停機）")

    # ── K4：投影後 ⇒ 應不敏感（仍綠）─────────────────────────────────
    say()
    say("─" * 100)
    say("【K4】**投影後**：同一份合成輸入 ⇒ 期 **類 II／III 皆空**（不再敏感）")
    say("─" * 100)
    pb = [(nm, _record(det)) for nm, det in base]
    pm = [(nm, _record(det)) for nm, det in mut]
    r4 = WR.classify(pb, pm)
    say(f"  類 I {len(r4['I'])}｜類 II {len(r4['II'])}｜類 III {len(r4['III'])}")
    say("  投影後之記錄（`wg_g1_smoke.py`）：")
    for x in pb[0][1]:
        say(f"     | {x[:110]}")
    if not r4["II"] and not r4["III"]:
        say("  ✅ **`K4` 成立**：投影後呈現層變動**不再致紅**")
    else:
        red(f"`K4` 破：類 II={[n for n, _ in r4['II']]}／類 III={[n for n, _ in r4['III']]}")

    # ── 判別力自檢：投影**不是**把所有差異都吃掉 ──────────────────────
    say()
    say("─" * 100)
    say("【判別力自檢】投影後仍須對**真受詞**之變動敏感（⛔ 否則投影過窄）")
    say("─" * 100)
    real = [(pb[0][0], [pb[0][1][0], "RuntimeError: （合成）真受詞已改變"])] + pb[1:]
    r5 = WR.classify(pb, real)
    say(f"  只改**例外訊息** ⇒ 類 III {len(r5['III'])}　⇒ {[n for n, _ in r5['III']]}")
    frame = [(pb[0][0], ['File "verify/wg_g1_smoke.py", line 58, in main'] + pb[0][1][1:])] + pb[1:]
    r6 = WR.classify(pb, frame)
    say(f"  只改**raise 幀** ⇒ 類 III {len(r6['III'])}　⇒ {[n for n, _ in r6['III']]}")
    if r5["III"] and r6["III"]:
        say("  ✅ 投影**未過窄**：真受詞之二要素（訊息／raise 幀）改變皆致紅")
    else:
        red("投影**過窄** ⇒ 真受詞之變動未致紅")

    say()
    say("=" * 100)
    say(f"{'✅ 探針 PASS' if RC[0] == 0 else '🔴 探針 FAIL'}（rc={RC[0]}）")
    say("=" * 100)
    return _dump()


def _dump():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
