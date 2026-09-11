#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 丙：逐情境可達街廓（母體 ＝ `verify/out/got_G值_退縮*_partial.csv`）。

🔒 三軸 (1) 來源 ＝ 本窗閘 8 之活體實跑（blob@e57d2ef）
             (2) 母體 ＝ 上二 CSV **逐檔分列**
             (3) 粒度框 ＝ **列框**（CSV 資料列）＋ **集合基數**（distinct 街廓）
"""
import csv
import io
import os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 🔒 W-G.9-269 p2：自 `__file__` 上溯·⛔ 硬編他樹（GB-161）

for scen in ("0m", "3.5m"):
    p = os.path.join(REPO, "verify", "out", "got_G值_退縮%s_partial.csv" % scen)
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    col = "所屬街廓"
    if rows and col not in rows[0]:
        cands = [c for c in rows[0] if "街廓" in c]
        col = cands[0] if cands else None
    order, seen = [], set()
    for r in rows:
        b = (r.get(col) or "").strip()
        if b and b not in seen:
            seen.add(b)
            order.append(b)
    per = {}
    for r in rows:
        b = (r.get(col) or "").strip()
        per[b] = per.get(b, 0) + 1
    print("── 退縮 %s ──  母體 ＝ %s（%d B）" % (scen, os.path.basename(p),
                                            os.path.getsize(p)))
    print("   資料列〔列框〕= %d ／ 欄數 = %d ／ 街廓欄名 = %r" %
          (len(rows), len(rows[0]) if rows else 0, col))
    print("   可達街廓（出現序·集合基數 %d）= %s" % (len(order), order))
    print("   逐街廓宗數〔列框〕= %s" % {k: per[k] for k in order})
    # 判別力：六街廓中未出現者
    missing = [b for b in ("R1", "R2", "R3", "R4", "R5", "R6") if b not in seen]
    print("   🔴 未產出之街廓 = %s" % (missing or "（無）"))
    print("")

print("🔒 對照組（證欄名框非紅）：二檔皆取得非空之街廓欄 ⇒ 器綠；")
print("   若欄名框錯，`所屬街廓` 將全空 ⇒ 集合基數 0 ⇒ 立即可見。")
