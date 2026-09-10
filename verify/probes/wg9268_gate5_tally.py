#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 審查窗 閘 5：四簿取號量（母體 ＝ 各該單檔·blob 層·列框）。

🔒 三軸
  (1) 來源 commit ＝ 由 argv[1] 給定（實查所得·⛔ 硬編）
  (2) 母體 ＝ 各該**單檔**（⛔ 全 docs/）——逐簿分列
  (3) 粒度框 ＝ **列框**（一列至多計一次；相異 ＝ 集合基數）

🔒 框之出處（逐字自倉讀·⛔ 憑開場文）
  自誤 ＝ VR-091 補款二 ①（候選 A）＋ 範圍框
  GB   ＝ VR-093（GB-116 三框聯集·扣哨兵 997）
  VR   ＝ VR-092 就地加註所引（扣哨兵 999）
  K-9  ＝ W-G.9-266 工項四 四-1（CLAUDE.md:2496）

🔒 靜態清單（已鑄而定義框結構上撈不到·⛔ 得列為缺號·⛔ 得重用）
  自誤 1-6 ／ VR 1-13 ／ K-9-1 ／ GB（無低端盲區）
  ⇒ 缺號集依 VR-092 取 [MIN..MAX]，MIN ＝ 各簿之框內最小值。
"""
import re
import subprocess
import sys

REV = sys.argv[1]

# ── 框（逐字·自倉讀得）────────────────────────────────────────────────
F_ZIWU_DEF = re.compile(r'^#+[^0-9０-９（(\n]*?自誤[\s　`]*`?([0-9]{1,4})`?', re.M)
F_ZIWU_RNG = re.compile(
    r'^#+[^\n]*?自誤[\s　`]*`?([0-9]{1,4})`?[\s　`]*[〜～\-–~]+[\s　`]*`?([0-9]{1,4})`?',
    re.M)
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
SENTINEL = {"GB": {997}, "VR": {999}, "自誤": set(), "K-9": set()}
# 靜態清單：已鑄而框外 ⇒ ⛔ 得列為缺號（其號恆 < MIN ⇒ 結構上已在 [MIN..MAX] 外）
STATIC = {"自誤": set(range(1, 7)), "VR": set(range(1, 14)), "K-9": {1}, "GB": set()}


def blob(path):
    """取倉側 blob 之 bytes（⛔ 工作樹·免 CRLF 之框差）。"""
    return subprocess.run(["git", "show", "%s:%s" % (REV, path)],
                          capture_output=True, check=True).stdout


def lineframe(rx, text, ngroups=1):
    """列框：回 (命中列號集, 號集)。一列至多計一次列命中。"""
    lines, nums = set(), set()
    for m in rx.finditer(text):
        ln = text.count("\n", 0, m.start()) + 1
        lines.add(ln)
        for g in range(1, ngroups + 1):
            nums.add(int(m.group(g)))
    return lines, nums


print("=" * 78)
print("W-G.9-268 閘 5：四簿取號量")
print("三軸 (1) 來源 commit ＝ %s" % REV)
print("三軸 (2) 母體 ＝ 各該**單檔**（⛔ 全 docs/）·逐簿分列於下")
print("三軸 (3) 粒度框 ＝ **列框**（相異 ＝ 集合基數）")
print("=" * 78)

for book, path in BOOKS.items():
    raw = blob(path)
    text = raw.decode("utf-8")
    nbytes = len(raw)
    n_nl = text.count("\n")
    n_split = len(text.split("\n"))

    if book == "自誤":
        dl, dn = lineframe(F_ZIWU_DEF, text, 1)
        rl, rn = lineframe(F_ZIWU_RNG, text, 2)
        # 範圍框：展開既有攢批標題之區間
        rng_nums = set()
        for m in F_ZIWU_RNG.finditer(text):
            a, b = int(m.group(1)), int(m.group(2))
            if a <= b and b - a < 60:
                rng_nums |= set(range(a, b + 1))
        nums = dn | rng_nums
        lines = dl | rl
        extra = "定義框列 %d／範圍框列 %d／重咬列 %d" % (
            len(dl), len(rl), len(dl & rl))
    elif book == "GB":
        tl, tn = lineframe(F_GB_TBL, text, 1)
        al, an = lineframe(F_GB_A, text, 1)
        bl, bn = lineframe(F_GB_B, text, 1)
        nums = tn | an | bn
        lines = tl | al | bl
        extra = "式表列 %d(相異%d)／式A列 %d(相異%d)／式B列 %d(相異%d)" % (
            len(tl), len(tn), len(al), len(an), len(bl), len(bn))
    elif book == "VR":
        lines, nums = lineframe(F_VR, text, 1)
        extra = "單框"
    else:
        lines, nums = lineframe(F_K9, text, 1)
        extra = "單框"

    nums -= SENTINEL[book]
    mx, mn = max(nums), min(nums)
    missing = sorted(set(range(mn, mx + 1)) - nums)

    print("")
    print("── %s ── 母體 ＝ %s" % (book, path))
    print("   bytes = %d ／ \\n 數 = %d ／ split('\\n') 長 = %d" % (nbytes, n_nl, n_split))
    print("   框內細目：%s" % extra)
    print("   命中列（聯集）= %d" % len(lines))
    print("   相異〔集合基數〕= %d ／ MAX = %d ／ MIN = %d" % (len(nums), mx, mn))
    print("   缺號集 [MIN..MAX] = %s" % missing)
    print("   扣除之哨兵 = %s ／ 靜態清單(已鑄而框外·⛔ 計缺號) = %s" % (
        sorted(SENTINEL[book]) or "無",
        ("%d-%d" % (min(STATIC[book]), max(STATIC[book]))) if STATIC[book] else "無"))
