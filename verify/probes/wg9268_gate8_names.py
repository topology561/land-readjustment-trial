#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 閘 8：run_verification 期初態之名目集抽取。

🩸 ⛔ 用 `grep -oP`——本環境 `-P` 於非 UTF-8 locale 得 0／0（`-267R 自捕 2`）。
   一律走 python re。「0 最該懷疑」⇒ 本器附兩造對照。
"""
import re
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")

RX_FAIL = re.compile(r"\s*🔴 FAIL\s+(.*)")
RX_PASS = re.compile(r"\s*✅ PASS\s+(.*)")

fails, passes, other_marks = [], [], {}
for ln in lines:
    m = RX_FAIL.match(ln)
    if m:
        fails.append(m.group(1).strip())
        continue
    m = RX_PASS.match(ln)
    if m:
        passes.append(m.group(1).strip())
        continue
    # 漏框偵察：任何含 FAIL/PASS 而未被上二框咬中之列
    if ("FAIL" in ln or "PASS" in ln) and not ln.startswith("RESULT"):
        other_marks[ln.strip()[:90]] = other_marks.get(ln.strip()[:90], 0) + 1

print("🔴 FAIL 名目數 =", len(fails), "／相異 =", len(set(fails)))
print("✅ PASS 名目數 =", len(passes), "／相異 =", len(set(passes)))
print("   合計 =", len(fails) + len(passes))
print("")
print("── 🔴 FAIL 名目（逐項）──")
for i, n in enumerate(sorted(fails), 1):
    print("  %2d. %s" % (i, n))
print("")
print("── ✅ PASS 名目（逐項）──")
for i, n in enumerate(sorted(passes), 1):
    print("  %2d. %s" % (i, n))
print("")
print("── 漏框偵察：含 FAIL/PASS 而未被二框咬中之列 ──")
if other_marks:
    for k, v in sorted(other_marks.items()):
        print("   [%d] %s" % (v, k))
else:
    print("   （無）")
print("")
# 🔒 兩造人造對照（證量測器非紅·⛔ 恆綠）
POS = "   🔴 FAIL  WG9268-人造陽性對照"
NEG = "   這一列不含任何判定標記-WG9268人造陰性對照"
print("對照組 甲（人造陽性·期望 咬中）=", bool(RX_FAIL.match(POS)),
      "→", (RX_FAIL.match(POS).group(1).strip() if RX_FAIL.match(POS) else None))
print("對照組 乙（人造陰性·期望 不咬）=", bool(RX_FAIL.match(NEG)))
print("判定集基數〔母體列數〕=", len(lines))
