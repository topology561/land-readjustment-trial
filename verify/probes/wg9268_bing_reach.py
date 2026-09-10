#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 丙：二態對拍之可行性——逐街廓可達性（自 run_verification 期初 log）。

🔒 三軸 (1) 來源 ＝ 本窗閘 8 之活體實跑（blob@e57d2ef 之工作樹）
             (2) 母體 ＝ wg9268_runverif_pre.out **單檔**
             (3) 粒度框 ＝ **字元框**（re.findall）＋ **列框**（逐列判）
"""
import io
import os
import re
import sys

SP = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(SP, "wg9268_runverif_pre.out")
t = io.open(p, encoding="utf-8").read()
lines = t.split("\n")

print("三軸 (2) 母體 ＝ %s（%d B／%d 列）" % (os.path.basename(p), len(t.encode("utf-8")),
                                        t.count("\n")))
print("三軸 (3) 粒度框 ＝ 字元框（re.findall）")
print("")

# ── 字元框計數 ＋ 兩造對照 ────────────────────────────────────────────
_NEG = "telescop" + "ZZZ"          # 執行期組出·⛔ 使其字面落入任何檔（GB-147）
for name, pat, expect in [
        ("telescoping", "telescoping", "受詞"),
        ("圍堵閘", "圍堵閘", "對照組 甲（須非零）"),
        ("⟨NEG⟩", _NEG, "對照組 乙（須為零）")]:
    print("  %-14s 字元框 = %-4d  ｜ %s" % (name, len(re.findall(pat, t)), expect))

print("")
print("── 中止閘（逐情境·逐字）──")
for m in re.finditer(r"\[StepG(0m|3\.5m)\] 街廓 (R\d) 抵費地計算失敗：(.*)", t):
    print("  %-6s 中止於 %s" % (m.group(1), m.group(2)))
    print("         %s" % m.group(3)[:150])

print("")
print("── 可達街廓（自診斷列之『街廓 Rn』出現序·列框）──")
for scen in ("0m", "3.5m"):
    seen, order = set(), []
    inblk = False
    for ln in lines:
        if ("診斷" + scen) in ln or ("StepG" + scen) in ln or ("[T2-DIAG]" in ln and scen in ln):
            inblk = True
        for mm in re.finditer(r"街廓 (R\d)", ln):
            b = mm.group(1)
            if b not in seen:
                seen.add(b)
                order.append(b)
    print("  %-6s 全 log 之街廓出現序（⚠️ 含跨情境·僅供漏框偵察）= %s" % (scen, order))

print("")
print("── 🔒 可達性之**可靠**判據 ＝ 中止街廓 ＋ 既有登記（⛔ 由 log 之街廓出現序推定）──")
print("   ⚠️ 上表之『出現序』母體含二情境之列，⛔ 具情境鑑別力 ⇒ ⛔ 作為可達性之證據。")
print("   逐情境之可達性須以**專屬探針**取得（本窗⛔ 跑修法探針·列為 W-G.9-268 之工項）。")
