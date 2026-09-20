# -*- coding: utf-8 -*-
"""W-G.9-318 補令四 工項一：款 `p`／`v`／`w` 之逐字傾印（自誤簿·唯讀·⛔ 改寫）。"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"


def main():
    rev = sys.argv[1]
    out = subprocess.run(["git", "show", "%s:%s" % (rev, LEDGER)],
                         cwd=REPO, capture_output=True).stdout.decode("utf-8")
    lines = out.splitlines()
    pat = re.compile(r"立為恆常附款 `([pvw])`")
    for i, ln in enumerate(lines):
        m = pat.search(ln)
        if not m:
            continue
        print("\n" + "=" * 88)
        print("### 款 `%s`　定義處 ＝ `%s:%d`" % (m.group(1), LEDGER, i + 1))
        print("=" * 88)
        blank = 0
        for j in range(i, min(i + 14, len(lines))):
            if lines[j].startswith("###") and j > i:
                break
            if not lines[j].strip():
                blank += 1
                if blank >= 1 and j > i:
                    break
            print("%6d| %s" % (j + 1, lines[j]))


if __name__ == "__main__":
    main()
