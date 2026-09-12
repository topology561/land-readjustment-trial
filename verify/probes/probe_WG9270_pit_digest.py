# -*- coding: utf-8 -*-
"""`W-G.9-270` `S-8` 之續：全 `67` 坑之**徵候／攔法逐字摘出**（供開場文所令之「逐坑覆述」）。

🩸 **本器之存在理由**：`probe_WG9269_pit_index.py` 只證「三字樣**齊備**」（`✅✅✅`），
   **⛔ 出艙其內容** ⇒ 新窗若僅貼其索引，即等於把「可覆述」當成「已覆述」。

🔒 **定位之來源** ＝ `probe_WG9269_pit_index.py` 之索引輸出（`檔:列`·D-H／D-T）；
   本器**⛔ 另寫第二份定義框**，只依該索引逐處取文。
🔒 **檔名之取法**：以 `os.listdir` ＋ **ASCII 片段比對**取得（Python 側 UTF-8）
   ——**⛔ 令 CJK 檔名穿過 shell 引號層**（`§六`·坑 `g`）。

用法：`python verify/probes/probe_WG9270_pit_digest.py <pit_index.log>`
`rc`：`0` 全數取得／`6` 有坑取不到文（loud 拒測·⛔ 猜、⛔ 略過）。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(REPO, "docs")

BT = chr(96)

# 🔒 母體 ＝ `docs/` **全樹**（⛔ 僅 `docs/reports/`）——坑之定義處實跨 `orders/`／`reports/`。
_INDEX = None


def _build_index():
    global _INDEX
    _INDEX = {}
    for dp, _dn, fns in os.walk(DOCS):
        for fn in fns:
            _INDEX.setdefault(fn, os.path.join(dp, fn))


def find_file(basename):
    """以完整 basename 於 `docs/` 全樹內定位（Python 側·⛔ 經 shell 引號層）。"""
    if _INDEX is None:
        _build_index()
    return _INDEX.get(basename)


def main():
    logp = sys.argv[1]
    with open(logp, encoding="utf-8") as fh:
        log = fh.read()

    # 索引之資料列：| `lab` | `檔:列`（D-X）… |
    rx = re.compile(
        r"^\s*\|\s*" + BT + r"([0-9a-z]{1,2})" + BT +
        r"\s*\|\s*" + BT + r"([^" + BT + r"]+?):([0-9]+)" + BT +
        r"[^|]*（(D-[HT])）", re.M)
    rows = rx.findall(log)
    print("【索引解析】自 %s 取得 %d 坑" % (os.path.basename(logp), len(rows)))
    if len(rows) != 67:
        print("🔴 期 67 ／ 實得 %d ⇒ loud 拒測" % len(rows))
        sys.exit(6)

    miss = []
    cache = {}
    for lab, base, ln, kind in rows:
        path = find_file(base)
        if path is None:
            miss.append((lab, base, "檔不存在"))
            continue
        if path not in cache:
            with open(path, encoding="utf-8") as fh:
                cache[path] = fh.read().split("\n")
        lines = cache[path]
        i = int(ln) - 1
        if i >= len(lines):
            miss.append((lab, base, "列越界"))
            continue
        if kind == "D-T":
            body = [lines[i]]
        else:
            # D-H：自該標題至次一同級或更高級標題（上限 12 列）
            m = re.match(r"^(#+)", lines[i])
            lvl = len(m.group(1)) if m else 6
            body = [lines[i]]
            for j in range(i + 1, min(i + 13, len(lines))):
                m2 = re.match(r"^(#+)\s", lines[j])
                if m2 and len(m2.group(1)) <= lvl:
                    break
                body.append(lines[j])
        txt = "\n".join(body).rstrip()
        if not txt.strip():
            miss.append((lab, base, "取得為空"))
            continue
        print()
        print("=" * 104)
        print("【坑 %s】%s:%s（%s）" % (lab, base, ln, kind))
        print("-" * 104)
        for b in body:
            if b.strip():
                print("  " + b.rstrip())

    print()
    print("=" * 104)
    if miss:
        print("🔴 取不到文之坑 = %d ⇒ loud 拒測（⛔ 猜、⛔ 略過）" % len(miss))
        for lab, base, why in miss:
            print("   坑 %s @ %s ⇒ %s" % (lab, base, why))
        sys.exit(6)
    print("✅ 全 %d 坑之徵候／攔法皆取得逐字（⛔ 猜、⛔ 略過）" % len(rows))
    sys.exit(0)


if __name__ == "__main__":
    main()
