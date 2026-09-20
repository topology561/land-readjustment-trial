# -*- coding: utf-8 -*-
"""W-G.9-318 補令四：`GB` 框與 `恆常附款 u` 定義數之對位（唯讀）。

受詞：本器只回答二問——
  ① 何種框可復現補令 `裁 1` 所載之 `GB` 相異 `169`／MAX `171`／缺號 `[12, 87]`？
  ② `裁 3` 所載「`j`〜`w` 各 `2`（`u` ＝ `4`）」之 `u ＝ 4` 出自何框？
🛑 本器唯讀；`GB` 之定義列式⛔ 經正典釘定（`GB-138` 處置③ 攢批中）
   ⇒ 本器只作**框之對位**，⛔ 據以出艙 `GB` 之缺號集為結論。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
LEDGER_GB = "docs/reports/W-G.4_泛用阻塞項登記表.md"


def run(a):
    return subprocess.run(a, cwd=REPO, capture_output=True)


def text(rev, path):
    return run(["git", "show", "%s:%s" % (rev, path)]).stdout.decode("utf-8")


def rep(name, s, target=169):
    if not s:
        print("  %-46s 相異 `0`" % name)
        return
    lo, hi = min(s), max(s)
    miss = sorted(set(range(lo, hi + 1)) - s)
    hit = "  ◀ ✅ 復現" if (len(s) == target and hi == 171 and miss == [12, 87]) else ""
    print("  %-46s 相異 `%d`／MIN `%d`／MAX `%d`／缺 %s%s"
          % (name, len(s), lo, hi, miss if len(miss) <= 8 else "(%d)" % len(miss), hit))


def main():
    rev = sys.argv[1]
    print("態 ＝ `%s`" % run(["git", "rev-parse", rev]).stdout.decode().strip())
    t = text(rev, LEDGER_GB)
    print("\n── ① `GB` 框之對位（母體 ＝ `%s` 單檔）──" % LEDGER_GB)
    cands = [
        (r"裸 4 碼 `GB-N{1,4}`", r"(?<![0-9\-])GB-([0-9]{1,4})(?![0-9])", set()),
        (r"裸 3 碼 `GB-N{1,3}`", r"(?<![0-9\-])GB-([0-9]{1,3})(?![0-9])", set()),
        (r"裸 3 碼 扣哨兵 `997`／`998`", r"(?<![0-9\-])GB-([0-9]{1,3})(?![0-9])", {997, 998}),
        (r"帶反引號 `` `GB-N` ``", r"`GB-([0-9]{1,3})`", set()),
        (r"帶反引號 扣哨兵", r"`GB-([0-9]{1,3})`", {997, 998}),
        (r"標題錨定 `^#{2,4}…GB-N`", r"^#{2,4}[^\n]*?GB-([0-9]{1,4})", set()),
    ]
    for name, pat, drop in cands:
        f = re.findall(pat, t, re.M)
        rep(name, set(int(x) for x in f) - drop)

    print("\n── ② `恆常附款 u` 之定義數（母體 ＝ 全倉追蹤 `.md`）──")
    files = [x for x in run(["git", "-c", "core.quotepath=false", "ls-tree",
                             "-r", "--name-only", rev]).stdout.decode().splitlines()
             if x.endswith(".md")]
    forms = [("形 ①`立為恆常附款…`x``", r"立為恆常附款[^\n]{0,20}?`([a-z])`"),
             ("形 ②`恆常附款 `x` ：／＝`", r"恆常附款 `([a-z])` [：＝]"),
             ("形 ③`恆常附款 `x`` 全稱", r"恆常附款 `([a-z])`"),
             ("形 ④`恆常附款 x` 無反引號", r"恆常附款 ([a-z])(?![a-z`])")]
    for nm, pat in forms:
        cnt = {}
        fr = re.compile(pat)
        for p in files:
            for i, ln in enumerate(text(rev, p).splitlines(), 1):
                for m in fr.finditer(ln):
                    cnt.setdefault(m.group(1), set()).add((p, i))
        js = [len(cnt.get(c, ())) for c in "jklmnopqrstvw"]
        print("  %-28s `u` ＝ `%d`／`j`〜`w`（扣 u）之值集 ＝ %s"
              % (nm, len(cnt.get("u", ())), sorted(set(js))))


if __name__ == "__main__":
    main()
