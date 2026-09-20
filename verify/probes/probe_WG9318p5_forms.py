# -*- coding: utf-8 -*-
r"""W-G.9-318 補令五 工項一 `(b)`：本簿諸款之**書寫形**之逐款機械分類（唯讀）。

🔒 受詞 ＝ 簿 `§三` 所載之每一款之 `(檔, 起列)`；判其首列屬何形。
🔒 判別力二造：[必命中] 至少一款歸入每一已宣告之形；[必為零] 一不存在之形樣式須得 `0`。
"""
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "549121b27beb6a34b3a6c823af43c78e37b0c7ee"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"

# 形之樣式（逐字·⛔ 憑記憶）
FORMS = [
    ("① 指向形", re.compile(r"立為恆常附款（`§一-1` 款 `[a-z]{1,2}`）")),
    ("② 區塊「（x）條文」形", re.compile(r"^[>\s]*[（(]\s*`?[a-z]{1,2}`?\s*[·`）)]")),
    ("③ 攔法形", re.compile(r"^\s*>?\s*\*\*攔法[^\n]*立為恆常附款 `[a-z]{1,2}`")),
    ("④ 行內「本單所增（x…）」形", re.compile(r"^🆕 \*\*本單所增")),
    ("⑨ 哨兵形［必為零］", re.compile(r"^\*\*\*\*⛔此形不存在⛔\*\*\*\*")),
]


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def text(p, rev=REV):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def main():
    book = text(BOOK)
    heads = re.findall(r"^### 款 `([a-z]{1,2})`　出處 ＝ `([^`]+):(\d+)`", book, re.M)
    print("態 ＝ `%s`／受詞 ＝ 簿 `§三` 之 `%d` 款" % (REV, len(heads)))
    cache = {}
    tally = {}
    rows = []
    for ch, path, ln in heads:
        if path not in cache:
            cache[path] = (text(path) or "").splitlines()
        line = cache[path][int(ln) - 1]
        hit = [nm for nm, pat in FORMS if pat.search(line)]
        nm = hit[0] if hit else "🔴 ⛔ 歸類"
        tally.setdefault(nm, []).append(ch)
        rows.append((ch, nm, path.rsplit("/", 1)[-1][:40], ln, line.strip()[:64]))
    print("\n逐款之判：")
    for ch, nm, f, ln, s in rows:
        print("  `%-2s`  %-22s  %s:%s" % (ch, nm, f, ln))
    print("\n形之分佈：")
    for nm, _ in FORMS:
        v = tally.get(nm, [])
        print("  %-22s `%d` 款  %s" % (nm, len(v), "".join(x + "," for x in v).rstrip(",")))
    un = tally.get("🔴 ⛔ 歸類", [])
    print("  %-22s `%d` 款  %s" % ("🔴 ⛔ 歸類", len(un), un))
    print("\n判別力二造：")
    nz = [nm for nm, _ in FORMS[:4] if tally.get(nm)]
    print("  ［必命中］形 ①〜④ 中有款者 ＝ `%d` 種（須 `> 0`）⇒ %s" % (len(nz), nz))
    print("  ［必為零］哨兵形之命中 ＝ `%d` 款（須 `0`）" % len(tally.get("⑨ 哨兵形［必為零］", [])))
    print("  合計 ＝ `%d`（須 ＝ 受詞數 `%d`）%s"
          % (sum(len(v) for v in tally.values()), len(heads),
             "🟢" if sum(len(v) for v in tally.values()) == len(heads) else "🔴"))


if __name__ == "__main__":
    main()
