# -*- coding: utf-8 -*-
r"""`W-G.9-9` §2-4：`CLAUDE.md:<行號>` 引用之**失準稽核**（加註前／後各跑一次）。

用法：python <本檔> <插入點行號 P> <插入行數 N>
  ⇒ 凡引用之行號 `>= P` 者，於插入後將失準（其真正內容已下移 N 行）。
  加註**前**跑：以「若在 P 插入 N 行，誰會失準」預示；
  加註**後**跑：以同一組 (P, N) 覆核**實際**失準者。

⛔ 逐行 `finditer` 讀原文（考古 67 修法 ③：不得以 grep 上下文窗抽清單）。
🔒 decode 失敗之檔**具名並改以 latin-1 納入**（⛔ 不靜默跳過·考古 67 修法 ①）。
"""
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
PAT = re.compile(r"CLAUDE\.md:(\d+)")
P = int(sys.argv[1]) if len(sys.argv) > 1 else 76
N = int(sys.argv[2]) if len(sys.argv) > 2 else 0


def kind(f):
    if f == "CLAUDE.md":
        return "活文件"
    if f.startswith(".claude/skills/"):
        return "活文件"
    if "新session交接文" in f:
        return "活文件"
    return "歷史記錄"


rows, special, scanned = [], [], 0
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 🔒 母體自證（考古 67 修法①）：倉根必含 CLAUDE.md；⛔ 少取一層 dirname 會使母體縮成
#    `verify/` 而產生「活文件 0」之**假綠**——本檔首版即如此（`W-G.9-9` 自誌）。
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
os.chdir(REPO)
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules")]
    if "/worktrees" in root.replace("\\", "/"):
        continue
    for fn in files:
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, ".").replace("\\", "/")
        try:
            txt = open(p, encoding="utf-8").read()
        except UnicodeDecodeError:
            txt = open(p, encoding="latin-1").read()
            special.append(rel)
        except Exception as e:
            special.append(f"{rel}（⛔ 無法讀：{type(e).__name__}）")
            continue
        scanned += 1
        for i, ln in enumerate(txt.splitlines(), 1):
            for m in PAT.finditer(ln):
                rows.append((rel, i, int(m.group(1))))

assert rows, "🔴 母體為 0 ⇒ ⛔ 不得視為「無失準」（考古 67 修法 ①）"
aff = [r for r in rows if r[2] >= P]
live = [r for r in aff if kind(r[0]) == "活文件"]
hist = [r for r in aff if kind(r[0]) == "歷史記錄"]
print(f"掃描檔數 {scanned}｜非 UTF-8 而改以 latin-1 納入者 {len(special)} 檔（皆具名）")
print(f"引用總數 {len(rows)}｜以 P={P}、N={N} 判：**失準 {len(aff)}** "
      f"＝ 活文件 **{len(live)}** ＋ 歷史記錄 {len(hist)}")
print()
print("── 活文件之失準（⛔ 期望 0；非 0 即 `K5` 破）──")
for f, ln, n in sorted(live):
    t = ""
    try:
        t = open(f, encoding="utf-8").read().splitlines()[ln - 1].strip()[:80]
    except Exception:
        pass
    print(f"  🔴 {f}:{ln} → CLAUDE.md:{n}")
    print(f"       {t}")
if not live:
    print("  （空）")
print()
print("── 歷史記錄之失準（⛔ 不追改）──")
for k, v in sorted(Counter(f for f, _, _ in hist).items()):
    print(f"  {v:>2} 處  {k}")
print()
print("🔒 判別力自檢：把門檻降為 P=1（則**所有**引用皆應計入失準）⇒ "
      f"活文件 {len([r for r in rows if kind(r[0])=='活文件'])} 處"
      "　⇒ 上式**非恆為 0**")
