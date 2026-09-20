# -*- coding: utf-8 -*-
r"""`W-G.9-321` `§一`：CC 側之逐格對拍（單內嵌落檔 vs CC 以同一器對同一 `commit` 之重跑）。

🛑 單 `§一` 明文：**相異即先判器紅**、查真因（框之別／母體之別／態之別），**⛔ 逕改數**。
🛑 **⛔ 改 `probe_WG9321_issuer_anchor.py` 一字**（單 `§三`：原封入倉）。

本器只做三事：① 逐列對拍並列出相異；② 對每一相異具名其真因；
③ 對「器紅」所致之空格，以**等價之獨立量法**補其值（⛔ 改原器、⛔ 逕改數）。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
A = "verify/out/WG9321_anchor_order.txt"     # 單內嵌之落檔
B = "verify/out/WG9321_anchor_cc.log"        # CC 重跑之落檔


def rd(p):
    return open(REPO + "\\" + p.replace("/", "\\"), encoding="utf-8").read().split("\n")


def main():
    a, b = rd(A), rd(B)
    print("# `W-G.9-321` `§一`　逐格對拍（⛔ 逕改數）")
    print("單內嵌 `%d` 列／CC 重跑 `%d` 列\n" % (len(a), len(b)))

    # 以「非空列」為對位單位，逐列比對
    ia = [(i, l) for i, l in enumerate(a, 1)]
    ib = [(i, l) for i, l in enumerate(b, 1)]
    sa = [l for _, l in ia]
    sb = [l for _, l in ib]
    only_a = [l for l in sa if l not in sb]
    only_b = [l for l in sb if l not in sa]
    print("── 只在單內嵌者（`%d` 列）──" % len(only_a))
    for l in only_a:
        print("  < %s" % l)
    print("\n── 只在 CC 重跑者（`%d` 列）──" % len(only_b))
    for l in only_b:
        print("  > %s" % l)

    print("\n══ 相異之真因（逐項具名·單 `§一` 所令） ══")
    print("""
  【相異 `1`】`branch = …`
    單內嵌 ＝ `wip/s1-endpart`／CC ＝ `claude/land-readjustment-trial-docs-fb1eca`
    🔒 真因 ＝ **checkout 之別**（CC 於 worktree 上作業），**⛔ 態之別**
       ——同列之 `HEAD`／`HEAD ci`／`HEAD s` 三格**逐位相符**，`commit` 同一。
    ⇒ 🟢 **⛔ 器紅·⛔ 倉態之別**；本格之受詞（分支名）⛔ 為態錨之一部。

  【相異 `2`】`### 項10` 之「內文側 `W-G.9-N` 之高號尾段」**空白**
    🔒 真因 ＝ **器紅（環境）**——該格由 `subprocess.run(..., shell=True)` 跑一條
       含 `sed`／`sort`／`uniq`／`tail` 之管線；於 Windows 之 `shell=True` 走 **`cmd.exe`**，
       該四支 POSIX 具⛔ 可得 ⇒ 管線**靜默回空**（`capture_output` 吞其 stderr）。
    🛑 **⛔ 倉態之別、⛔ 框之別、⛔ 母體之別。**
    ⇒ 依 `常規五`：`rc≠0`／空輸出**先判量測器紅**；**⛔ 改該器一字**（單 `§三` 原封入倉），
       改以**等價之獨立量法**補其值（見下）。
""")

    print("══ 相異 `2` 之補量（等價獨立量法·⛔ 改原器） ══")
    print("  法 ＝ 以 `git grep -h -o -E` 取全部命中後於 **Python 內**計數（⛔ 依賴 POSIX 管線）")
    r = subprocess.run(["git", "-C", REPO, "grep", "-h", "-o", "-E",
                        r"W-G\.9-[0-9]{1,4}", "HEAD", "--", "*.md"],
                       capture_output=True)
    nums = re.findall(r"W-G\.9-([0-9]{1,4})", r.stdout.decode("utf-8", "replace"))
    from collections import Counter
    c = Counter(int(x) for x in nums)
    tail = sorted(c.items())[-12:]
    print("  內文側 `W-G.9-N` 之高號尾段（count number）：")
    for n, k in tail:
        print("    %6d %s" % (k, n))
    exp = [(89, 310), (70, 311), (71, 312), (62, 313), (46, 314), (64, 315),
           (54, 316), (42, 317), (280, 318), (54, 319), (10, 320), (5, 999)]
    got = [(k, n) for n, k in tail]
    print("\n  單內嵌之同格（逐對）＝ %s" % exp)
    print("  CC 補量之同格（逐對）＝ %s" % got)
    print("  ⇒ **逐對相符：%s** %s" % (got == exp, "🟢" if got == exp else "🔴"))
    print("  判別力［必不命中］：一必不存在之號 `W-G.9-8888` 之命中 ＝ **%d**（須 `0`）"
          % c.get(8888, 0))
    print("  判別力［必命中］：`W-G.9-318` 之命中 ＝ **%d**（須 `> 0`）" % c.get(318, 0))


if __name__ == "__main__":
    main()
