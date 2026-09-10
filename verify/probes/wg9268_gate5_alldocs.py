#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 §1 乙部：四簿取號量之**全 `docs/` 母體**（⛔ 取號用·只為證母體之別）。

🛑 正字之取號母體 ＝ **各該單檔**（`W-G.9-192-PRE-b 🔧 一`）。
   本表之全 `docs/` 值**僅供對照**，證「母體之別確實改變其數」——⛔ 得據以取號。
"""
import re
import subprocess

REV = "e57d2ef86894472761e1403974ff1f2ce1e6a2df"

F_ZIWU_DEF = re.compile(r'^#+[^0-9０-９（(\n]*?自誤[\s　`]*`?([0-9]{1,4})`?', re.M)
F_GB_TBL = re.compile(r'^\| *\*\*`?GB-([0-9]{1,4})`?\*\*', re.M)
F_GB_A = re.compile(r'^## `GB-([0-9]{1,4})`', re.M)
F_GB_B = re.compile(r'^### `GB-([0-9]{1,4})`', re.M)
F_VR = re.compile(r'^#+ `?VR-([0-9]{1,4})`?', re.M)
F_K9 = re.compile(r'^#{2,4}[^\n]*?K-9-([0-9]{1,3})', re.M)

SINGLE = {
    "自誤": "docs/reports/W-G.9波_claude.ai側自誤登記.md",
    "GB": "docs/reports/W-G.4_泛用阻塞項登記表.md",
    "VR": "docs/驗證裁定登記表.md",
    "K-9": "docs/rulings/K-6_街角地分配程序與可分配判準.md",
}
SENT = {"GB": {997}, "VR": {999}, "自誤": set(), "K-9": set()}

names = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", REV, "docs/"],
                       capture_output=True, check=True).stdout.decode("utf-8").split("\0")
files = [p for p in names if p.strip().endswith(".md")]
texts, bad = {}, 0
for p in files:
    r = subprocess.run(["git", "show", "%s:%s" % (REV, p)], capture_output=True)
    if r.returncode != 0:
        bad += 1
        continue
    try:
        texts[p] = r.stdout.decode("utf-8")
    except UnicodeDecodeError:
        bad += 1

print("母體（乙部）＝ 全 `docs/` 之 `.md` %d 檔（讀不到 %d）·態 %s" % (len(files), bad, REV[:7]))
print("粒度框 ＝ 列框；⛔ 此欄僅供對照·⛔ 得據以取號")
print("")
print("%-6s %10s %10s %10s %10s" % ("簿", "單檔相異", "單檔MAX", "全docs相異", "全docsMAX"))

for book, path in SINGLE.items():
    def nums_of(text):
        s = set()
        if book == "自誤":
            for m in F_ZIWU_DEF.finditer(text):
                s.add(int(m.group(1)))
        elif book == "GB":
            for rx in (F_GB_TBL, F_GB_A, F_GB_B):
                for m in rx.finditer(text):
                    s.add(int(m.group(1)))
        elif book == "VR":
            for m in F_VR.finditer(text):
                s.add(int(m.group(1)))
        else:
            for m in F_K9.finditer(text):
                s.add(int(m.group(1)))
        return s - SENT[book]

    one = nums_of(texts.get(path, ""))
    allx = set()
    for t in texts.values():
        allx |= nums_of(t)
    print("%-6s %10d %10d %10d %10d   Δ相異 %+d ／ ΔMAX %+d"
          % (book, len(one), max(one), len(allx), max(allx),
             len(allx) - len(one), max(allx) - max(one)))
