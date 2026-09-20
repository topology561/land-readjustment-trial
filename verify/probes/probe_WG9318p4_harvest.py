# -*- coding: utf-8 -*-
"""W-G.9-318 補令四 工項一：恆常附款 `a`〜`w` 之逐字採收（唯讀）。

🛑 本器**只抽取、⛔ 改寫**（`常規七 一`：逐字交付塊須由檔案管線直接產生）。
   其輸出即 `§二` 之簿所轉錄之來源；⛔ 憑記憶重寫。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
DEF_FORM = re.compile(r"立為恆常附款[^\n]{0,20}?`([a-z])`")
REF_FORM = re.compile(r"恆常附款 `?([a-z])`?(?![a-z])")


def run(a):
    return subprocess.run(a, cwd=REPO, capture_output=True)


def text(rev, path):
    return run(["git", "show", "%s:%s" % (rev, path)]).stdout.decode("utf-8")


def main():
    rev = sys.argv[1]
    files = [x for x in run(["git", "-c", "core.quotepath=false", "ls-tree",
                             "-r", "--name-only", rev]).stdout.decode().splitlines()
             if x.endswith(".md")]
    cache = {p: text(rev, p).splitlines() for p in files}
    print("態 ＝ `%s`／母體 ＝ 全倉追蹤 `.md` `%d` 檔" % (
        run(["git", "rev-parse", rev]).stdout.decode().strip(), len(files)))

    hits = {}
    for p in files:
        for i, ln in enumerate(cache[p], 1):
            for m in DEF_FORM.finditer(ln):
                hits.setdefault(m.group(1), []).append((p, i, ln))

    for ch in "abcdefghijklmnopqrstuvw":
        print("\n" + "=" * 78)
        print("## 款 `%s`　定義形命中 ＝ %d" % (ch, len(hits.get(ch, []))))
        for p, i, ln in hits.get(ch, []):
            print("--- 定義處 %s:%d" % (p, i))
            print("    %s" % ln.strip())
            # 其所指之單 §一-1 款列（`c`／`d` 型）
            mm = re.search(r"§一-1[^\n]{0,12}?款 `%s`" % ch, ln)
            if mm:
                print("    ↳ 指向該單 `§一-1` 之款 `%s` 列，逐字抽取如下：" % ch)
                for j, l2 in enumerate(cache[p], 1):
                    if re.match(r"^\s*\|?\s*`?%s`?\s*[｜|]" % ch, l2) and "恆常附款" not in l2:
                        print("      %s:%d| %s" % (p, j, l2.strip()[:300]))
        if not hits.get(ch):
            refs = []
            for p in files:
                for i, ln in enumerate(cache[p], 1):
                    for m in REF_FORM.finditer(ln):
                        if m.group(1) == ch:
                            refs.append((p, i, ln))
            print("  🔴 ⛔ 定義形；引用 ＝ %d，逐列如下（供判可重建與否）：" % len(refs))
            for p, i, ln in refs[:10]:
                print("    · %s:%d" % (p, i))
                print("      %s" % ln.strip()[:400])


if __name__ == "__main__":
    main()
