# -*- coding: utf-8 -*-
"""`W-G.9-270` **收工閘**（`常規四（九）二`：① 形之自證 ⋀ ② MAX 之推進）＋ 四簿期末復查。

🔒 **框之出處（逐簿分列·⛔ 冠單一框名·`補令十八 §二-2`）**
   自誤 ＝ `VR-091` 補款二 `①`（候選 `A`）＋ **範圍框**
   `GB` ＝ `VR-093`（`GB-116` 三框聯集·扣哨兵 `997`）
   `VR` ＝ `VR-092` 就地加註所引（扣哨兵 `999`）
   `K-9` ＝ `W-G.9-266` 工項四 `四-1`

🔒 **靜態清單**（已鑄而定義框結構上撈不到·⛔ 得列為缺號）：自誤 `1`–`6`／`VR` `1`–`13`／`K-9-1`。

用法：`python verify/probes/probe_WG9270_closegate.py <新鑄之號> <前一 MAX> [倉根]`
`rc`：`0` 二閘皆過／`7` **不過 ⇒ 停機回報**（`常規四（九）三`）。
"""
import io
import os
import re
import sys

NEW = int(sys.argv[1])
PREV = int(sys.argv[2])
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.dirname(HERE))

BT = chr(96)
W = 104

# 框（逐字·同 `verify/probes/wg9268_gate5_tally.py`·⛔ 另寫第二份定義）
F_ZIWU_DEF = re.compile(r'^#+[^0-9０-９（(\n]*?自誤[\s　`]*`?([0-9]{1,4})`?', re.M)
F_ZIWU_RNG = re.compile(
    r'^#+[^\n]*?自誤[\s　`]*`?([0-9]{1,4})`?[\s　`]*[〜～\-–~]+[\s　`]*`?([0-9]{1,4})`?', re.M)
F_GB_TBL = re.compile(r'^\| *\*\*`?GB-([0-9]{1,4})`?\*\*', re.M)
F_GB_A = re.compile(r'^## `GB-([0-9]{1,4})`', re.M)
F_GB_B = re.compile(r'^### `GB-([0-9]{1,4})`', re.M)
F_VR = re.compile(r'^#+ `?VR-([0-9]{1,4})`?', re.M)
F_K9 = re.compile(r'^#{2,4}[^\n]*?K-9-([0-9]{1,3})', re.M)

BOOKS = {
    "自誤": "docs/reports/W-G.9波_claude.ai側自誤登記.md",
    "GB": "docs/reports/W-G.4_泛用阻塞項登記表.md",
    "VR": "docs/驗證裁定登記表.md",
    "K-9": "docs/rulings/K-6_街角地分配程序與可分配判準.md",
}
SENT = {"GB": {997}, "VR": {999}, "自誤": set(), "K-9": set()}
STATIC = {"自誤": set(range(1, 7)), "VR": set(range(1, 14)), "K-9": {1}, "GB": set()}


def say(s=""):
    print(s)


def read(p):
    with io.open(os.path.join(REPO, p), "r", encoding="utf-8") as f:
        return f.read()


def nums(book):
    t = read(BOOKS[book])
    s = set()
    if book == "自誤":
        for m in F_ZIWU_DEF.finditer(t):
            s.add(int(m.group(1)))
        for m in F_ZIWU_RNG.finditer(t):
            a, b = int(m.group(1)), int(m.group(2))
            for i in range(min(a, b), max(a, b) + 1):
                s.add(i)
    elif book == "GB":
        for rx in (F_GB_TBL, F_GB_A, F_GB_B):
            for m in rx.finditer(t):
                s.add(int(m.group(1)))
    elif book == "VR":
        for m in F_VR.finditer(t):
            s.add(int(m.group(1)))
    else:
        for m in F_K9.finditer(t):
            s.add(int(m.group(1)))
    return s - SENT[book]


def main():
    bad = False
    say("=" * W)
    say("【`W-G.9-270` 收工閘】`常規四（九）二`：① 形之自證 ⋀ ② MAX 之推進")
    say("=" * W)

    s = nums("自誤")
    mx = max(s)
    lo = min(s)
    miss = sorted(set(range(lo, mx + 1)) - s - STATIC["自誤"])

    say("── 閘 ①　**形之自證**（以自誤之定義列式掃該簿，須命中新號 `%d`）──" % NEW)
    ok1 = NEW in s
    say("   新號 `%d` ∈ 定義框之命中集 ⇒ %s" % (NEW, "✅" if ok1 else "🔴"))
    say("   🔒 其標題形（自倉逐字取·⛔ 自創）：")
    t = read(BOOKS["自誤"])
    for m in F_ZIWU_DEF.finditer(t):
        if int(m.group(1)) == NEW:
            ln = t.count("\n", 0, m.start()) + 1
            say("      %s:%d  %s" % (BOOKS["自誤"], ln,
                                     t.split("\n")[ln - 1][:96]))
    if not ok1:
        bad = True

    say("")
    say("── 閘 ②　**MAX 之推進**（須由 `%d` 轉為 `%d`，且 `%d` ⛔ 在缺號集）──"
        % (PREV, NEW, NEW))
    ok2a = (mx == NEW)
    ok2b = (NEW not in miss)
    say("   MAX 實測 ＝ **%d**（期 `%d`）⇒ %s" % (mx, NEW, "✅" if ok2a else "🔴"))
    say("   缺號集 `[MIN..MAX]` ＝ %s（MIN ＝ %d·已扣靜態清單 `1`–`6`）" % (miss, lo))
    say("   新號在缺號集？ %s ⇒ %s" % ("是" if NEW in miss else "否", "✅" if ok2b else "🔴"))
    if not (ok2a and ok2b):
        bad = True

    say("")
    say("── 四簿期末復查（**逐簿具名其各自之框及其出處**·⛔ 冠單一框名）──")
    say("   %-6s %-52s %-8s %-8s %s" % ("簿", "框之出處", "相異", "MAX", "缺號集"))
    src = {"自誤": "VR-091 補款二 ① ＋ 範圍框",
           "GB": "VR-093（GB-116 三框聯集·扣哨兵 997）",
           "VR": "VR-092 就地加註所引（扣哨兵 999）",
           "K-9": "W-G.9-266 工項四 四-1"}
    for b in ("自誤", "GB", "VR", "K-9"):
        ss = nums(b)
        m2 = max(ss)
        l2 = min(ss)
        mi = sorted(set(range(l2, m2 + 1)) - ss - STATIC[b])
        say("   %-6s %-52s %-8d %-8d %s" % (b, src[b], len(ss), m2, mi))

    say("")
    say("=" * W)
    if bad:
        say("🛑 **收工閘不過 ⇒ 停機回報**（`常規四（九）三`·⛔ 逕行入倉）")
        sys.exit(7)
    say("✅ 二閘皆過")
    sys.exit(0)


if __name__ == "__main__":
    main()
