# -*- coding: utf-8 -*-
r"""W-G.9-318 補令四 `§二` 閘 `二-1`〜`二-4` 之實測（唯讀）。

🔒 `二-2` 之覆核法 ＝ **重跑抽取並與簿內文字逐位 `diff`**（`常規七 三`：
   ⛔ 僅比對三數）。抽驗 `5` 款。
🔒 `二-3` 之人造款名**執行期組出**，字面⛔ 落入本檔、亦⛔ 落入 log。
"""
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "bc97c9d72d1680e820872aba787ecc453fa3a509"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
SAMPLE = ["a", "d", "j", "q", "w"]          # 抽驗 5 款


def blob(path, rev=REV):
    p = subprocess.run(["git", "show", "%s:%s" % (rev, path)],
                       cwd=REPO, capture_output=True)
    return p.stdout.decode("utf-8").splitlines() if p.returncode == 0 else None


def main():
    book = open(REPO + "\\" + BOOK.replace("/", "\\"), encoding="utf-8").read()
    blines = book.splitlines()

    # ── 二-1　款數 ──
    # 🩸 自捕：母體須**限於 `§一` 之表**——`§二` 之「定義處」表亦含 `| `a` |` 形，
    #    首版未限範圍而得 `34`／`32`（偽陽 `9` 列）。
    s1 = book.index("## `§一`")
    s2 = book.index("## `§二`")
    sec1 = book[s1:s2]
    rows = re.findall(r"^\| `([a-z])` \|", sec1, re.M)
    aw = [c for c in rows if c <= "w"]
    print("══ 閘 `二-1`　款數 ══")
    print("  `§一` 表之款列 ＝ `%d`（逐字集 ＝ %s）" % (len(rows), "".join(sorted(set(rows)))))
    print("  其中 `a`〜`w` ＝ **`%d`**（單所令 ＝ `23`）⇒ %s"
          % (len(aw), "🟢 符" if len(aw) == 23 else "🔴 不符"))
    miss = [chr(c) for c in range(ord("a"), ord("x")) if chr(c) not in rows]
    print("  `a`〜`w` 之缺號 ＝ %s（須 `[]`）" % (miss or "[]"))
    print("  本批新立 ＝ %s" % [c for c in sorted(set(rows)) if c > "w"])

    # ── 二-2　出處欄之可復現（重跑抽取 ＋ 逐位 diff）──
    print("\n══ 閘 `二-2`　出處欄之逐字復現（抽驗 `%d` 款·重跑抽取並逐位比對）══" % len(SAMPLE))
    ok = 0
    for ch in SAMPLE:
        m = re.search(r"^### 款 `%s`　出處 ＝ `([^`]+):(\d+)`(?:–`:(\d+)`)?" % ch,
                      book, re.M)
        if not m:
            print("  款 `%s`：🔴 ⛔ 於簿內定位其 `§三` 節題" % ch)
            continue
        path, a = m.group(1), int(m.group(2))
        b = int(m.group(3)) if m.group(3) else a
        src = blob(path)
        if src is None:
            print("  款 `%s`：🔴 讀不到 `%s`" % (ch, path))
            continue
        expect = [("> " + src[k]) if src[k].strip() else ">" for k in range(a - 1, b)]
        # 🩸 自捕：節題列含「（所繫 ＝ …）」後綴 ⇒ ⛔ 以 `m.group(0)` 全列比對定位
        head = "### 款 `%s`　出處 ＝ " % ch
        i = next(j for j, l in enumerate(blines) if l.startswith(head)) + 2
        got = blines[i:i + len(expect)]
        same = got == expect
        ok += same
        print("  款 `%s`　`%s:%d`%s　列 `%d`　逐位相符：%s"
              % (ch, path.rsplit("/", 1)[-1][:34], a,
                 ("–`:%d`" % b) if b > a else "", len(expect),
                 "🟢 True" if same else "🔴 False"))
        if not same:
            for e, g in zip(expect, got):
                if e != g:
                    print("      期 %r" % e[:90])
                    print("      得 %r" % g[:90])
                    break
    print("  ⇒ 相符 `%d`／`%d`" % (ok, len(SAMPLE)))

    # ── 二-3　判別力［必不命中］──
    # 🩸 自捕：首版之 `chr(0x71 + 2)` ＝ `s`，係**真存在之款** ⇒ ［必不命中］得 `1`
    #    ——對照組紅即量測器紅（`常規五`）。改取真不存在之字母。
    fake = "恆常附款 " + chr(96) + chr(0x7A) + chr(96)      # 執行期組出·字面⛔ 出艙
    fake2 = "### 款 " + chr(96) + chr(0x7A) + chr(96)
    print("\n══ 閘 `二-3`　判別力二造 ══")
    print("  ［必不命中］人造款名（字面⛔ 出艙）於本簿之命中 ＝ `%d`／`%d`（須 `0`）"
          % (book.count(fake), book.count(fake2)))
    print("  ［必命中］已知款 `a` 之節題於本簿之命中 ＝ `%d`（須 `> 0`）"
          % len(re.findall(r"^### 款 `a`　", book, re.M)))

    # ── 二-4　🔴／🟡 之款數 ──
    red = len(re.findall(r"\| 🔴 \*\*失傳\*\*", book))
    yel = len(re.findall(r"\| 🟡 \*\*重鑄", book))
    grn = len(re.findall(r"\| 🟢 \*\*可得\*\*", book))
    print("\n══ 閘 `二-4`　可得性判之款數 ══")
    print("  實得：🔴 失傳 ＝ `%d`／🟡 重鑄 ＝ `%d`／🟢 可得 ＝ `%d`" % (red, yel, grn))
    print("  單所令：🔴 ＝ `3`／🟡 ＝ `4`")
    print("  ⇒ %s ——依單之明文「不符 ⇒ **具名相異·⛔ 追改**」，其具名 ＝ 簿 `§二`。"
          % ("🟢 符" if (red, yel) == (3, 4) else "🩸 **不符·已具名**"))


if __name__ == "__main__":
    main()
