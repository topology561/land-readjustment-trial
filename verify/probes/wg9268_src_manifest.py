#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 工項零：來源檔之 `sha256` ＋ 行尾清單（**落檔前**之錨）。

🔒 `作業常規之追加四` 款一：驗**入倉 blob 之內容 `sha256` ＝ 落檔前來源 `sha256`**（逐位相同）。
🩸 **CRLF 陷阱**：本倉 `core.autocrlf=true`，`.gitattributes` 之 `-text` **僅涵蓋 `*.dxf`／`*.dwg`**
   ⇒ 凡來源含 `CRLF` 者，入倉時被正規化為 `LF` ⇒ **blob `sha256` ≠ 來源 `sha256`**。
   ⇒ 本表**先驗行尾**，含 `CRLF` 者須於落檔前具名。
"""
import hashlib
import io
import os

SP = os.path.dirname(os.path.abspath(__file__))
DL = r"C:\Users\admin\Downloads"

SRC = [
    ("單", os.path.join(DL, "W-G.9-268_施工單_GB67開修_K923二閘轉主動_K917遞補迴圈.md")),
    ("附件甲", os.path.join(SP, "W-G.9-268_附件甲_審查窗報告與草稿.md")),
]
for fn in sorted(os.listdir(SP)):
    if fn.startswith("wg9268_") and fn.endswith(".py"):
        SRC.append(("探針", os.path.join(SP, fn)))

print("%-6s %-46s %10s %8s %6s %6s  %s" %
      ("類", "檔名", "bytes", "sha256", "CRLF", "裸CR", "行尾判"))
print("-" * 130)
rows = []
for kind, p in SRC:
    b = io.open(p, "rb").read()
    h = hashlib.sha256(b).hexdigest()
    crlf = b.count(b"\r\n")
    bare_cr = b.count(b"\r") - crlf
    verdict = "純 LF ✅" if (crlf == 0 and bare_cr == 0) else "🔴 含 CR ⇒ 入倉必被正規化"
    print("%-6s %-46s %10d %8s %6d %6d  %s" %
          (kind, os.path.basename(p)[:46], len(b), h[:8], crlf, bare_cr, verdict))
    rows.append((kind, os.path.basename(p), len(b), h, crlf, bare_cr))

print("")
print("🔒 逐檔全 `sha256`（落檔前之錨·入倉後須逐位復驗）")
for kind, name, n, h, _, _ in rows:
    print("   %s  %s  %d B" % (h, name, n))
print("")
bad = [r for r in rows if r[4] or r[5]]
print("🔒 含 CR 之檔數 ＝ %d（須 0，否則 blob ≠ 來源）" % len(bad))
print("🔒 受詞檔數 ＝ %d（單 1 ＋ 附件甲 1 ＋ 探針 %d）" % (len(rows), len(rows) - 2))
