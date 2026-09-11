#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 戊-3：名目差集（凍存期望 FAIL 名單 vs 本窗實測）。

🔒 三軸 (1) 來源 ＝ 凍存名單 blob@e57d2ef ／ 本窗閘 8 之活體實跑
             (2) 母體 ＝ 二者**逐檔分列**（見下）
             (3) 粒度框 ＝ **列框**（凍存 ＝ `^🔴 FAIL`；實測 ＝ `\\s*🔴 FAIL`）

🛑 **射程之界（照實·⛔ 頂替）**：凍存名單之對帳器 `verify/wv_reconcile.py`
   於 **`run_all`** 內自動執行；本窗所跑者為 **`run_verification`** 單支。
   ⇒ 本表係「**名目集**」之比較，**⛔ 等同 `wv_reconcile` 之對帳結果**。
"""
import io
import os
import re
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 🔒 W-G.9-269 p2：自 `__file__` 上溯·⛔ 硬編他樹（GB-161）
SP = os.path.dirname(os.path.abspath(__file__))
REV = "e57d2ef86894472761e1403974ff1f2ce1e6a2df"
FROZEN = "verify/out/K6A2_期望FAIL名單_WG97_名目加原因.txt"

raw = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (REV, FROZEN)],
                     capture_output=True, check=True).stdout.decode("utf-8")
frozen = []
for ln in raw.split("\n"):
    m = re.match(r"^🔴 FAIL\s+(.*)", ln)
    if m:
        frozen.append(m.group(1).strip())

live = []
t = io.open(os.path.join(SP, "wg9268_runverif_pre.out"), encoding="utf-8").read()
for ln in t.split("\n"):
    m = re.match(r"\s*🔴 FAIL\s+(.*)", ln)
    if m:
        live.append(m.group(1).strip())

F, L = set(frozen), set(live)
print("母體 A ＝ %s（blob@%s·框 `^🔴 FAIL`）⇒ %d 列／相異 %d"
      % (FROZEN, REV[:7], len(frozen), len(F)))
print("母體 B ＝ wg9268_runverif_pre.out（本窗活體·框 `\\s*🔴 FAIL`）⇒ %d 列／相異 %d"
      % (len(live), len(L)))
print("")
print("🔒 名目集基數：凍存 %d ／ 實測 %d ／ 交集 %d" % (len(F), len(L), len(F & L)))
print("")
print("── B ∖ A（實測有、凍存無 ＝ 新紅）%d 項 ──" % len(L - F))
for n in sorted(L - F):
    print("   🔴 %s" % n)
print("")
print("── A ∖ B（凍存有、實測無 ＝ 已轉綠或改名）%d 項 ──" % len(F - L))
for n in sorted(F - L):
    print("   🟢 %s" % n)
print("")
print("🔒 對照組（證框非紅）：凍存之 `^# ` 註解列 = %d（須 > 0）"
      % len([1 for ln in raw.split("\n") if ln.startswith("#")]))
_NEG = "^🔴 FA" + "ILZZZ"
print("               人造陰性（執行期組出）= %d（須 = 0）"
      % len([1 for ln in raw.split("\n") if re.match(_NEG, ln)]))
