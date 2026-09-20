# -*- coding: utf-8 -*-
"""W-G.9-318 補令四 工項一：恆常附款之**第四形**（單 `§一-1` 之「（`x`）」列舉形）之採收。

🩸 **本器之緣起**：裁 `3` 以二形（`立為恆常附款…`x``／`恆常附款 `x` ：＝`）判 `a`／`b`／`f`
   為【⛔ 可得·失傳】。本器現查得**第四形**——單之 `§一-1` 內之
   `（`a`）**…**（`自誤 NNN`）` 列舉形——其結構上**⛔ 可能**被該二形命中。

🛑 本器**只抽取、⛔ 改寫**（`常規七 一`）。其輸出即簿所轉錄之來源。
🔒 判別力二造：必非零 ＝ 已知之 `a`（`補令一:81`）；必為零 ＝ 執行期組出之字母（字面⛔ 出艙）。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"

# 第四形：列首（容許 `>`／空白）＋ 全形或半形括號包一小寫字母（得帶反引號）
FORM4 = re.compile(r"^[>\s]*[（(]\s*`?([a-z])`?\s*[）)]")
# 第五形：`含補令一所增之款 `a`（…）` 之行內列舉（僅作**佐證**·⛔ 為條文）
FORM5 = re.compile(r"款 `([a-z])`（([^）]{2,60})）")


def run(a):
    return subprocess.run(a, cwd=REPO, capture_output=True)


def text(rev, p):
    return run(["git", "show", "%s:%s" % (rev, p)]).stdout.decode("utf-8")


def main():
    rev = sys.argv[1]
    files = [x for x in run(["git", "-c", "core.quotepath=false", "ls-tree", "-r",
                             "--name-only", rev]).stdout.decode().splitlines()
             if x.endswith(".md")]
    print("態 ＝ `%s`／母體 ＝ 全倉追蹤 `.md` `%d` 檔／粒度框 ＝ **列框**"
          % (run(["git", "rev-parse", rev]).stdout.decode().strip(), len(files)))

    form4, form5 = {}, {}
    for p in files:
        lines = text(rev, p).splitlines()
        in_sec = False
        for i, ln in enumerate(lines, 1):
            if ln.startswith("#"):
                in_sec = "§一-1" in ln and "恆常附款" in ln
            if in_sec:
                m = FORM4.match(ln)
                if m and ("凡" in ln or "須" in ln or "一律" in ln or "⛔" in ln):
                    form4.setdefault(m.group(1), []).append((p, i, ln.rstrip()))
            for m in FORM5.finditer(ln):
                form5.setdefault(m.group(1), []).append((p, i, m.group(2)))

    print("\n══ 第四形（單 `§一-1` 之「（`x`）」列舉形）══")
    for ch in sorted(form4):
        print("\n## 款 `%s`　命中 `%d`" % (ch, len(form4[ch])))
        for p, i, ln in form4[ch]:
            print("  %s:%d" % (p, i))
            print("    %s" % ln)

    print("\n══ 第五形（行內之受詞括註·**⛔ 為條文·僅作佐證**）══")
    for ch in sorted(form5):
        seen = set()
        for p, i, g in form5[ch]:
            if g in seen:
                continue
            seen.add(g)
            print("  款 `%s`　〔%s〕　%s:%d" % (ch, g, p, i))

    print("\n══ 判別力二造 ══")
    print("  必非零：款 `a` 第四形命中 ＝ `%d`（須 `> 0`）" % len(form4.get("a", ())))
    absent = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in form4]
    print("  必為零：第四形⛔ 命中之字母 ＝ `%d` 個 ⇒ 本器⛔ 恆命中" % len(absent))
    print("  第四形所得之款集 ＝ %s" % sorted(form4))


if __name__ == "__main__":
    main()
