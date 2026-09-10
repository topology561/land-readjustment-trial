#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 工項零：原封入倉之逐位驗（`作業常規之追加四` 款一）。

用法：wg9268_ingest_verify.py <staged|COMMIT>
  staged  ⇒ 比對 index 之 blob（落檔後、入倉前）
  COMMIT  ⇒ 比對該 commit 之 blob（入倉後·**durable 之側**）

🔒 受詞 ＝ **blob 之內容 `sha256`**（⛔ git 物件 hash·後者含 header）。
🩸 二側之別：工作樹（`wc -c`）與倉內 blob 於本倉**不相等**（`core.autocrlf=true`）
   ——本批全部來源為**純 LF** ⇒ 二側應相等；本器即證之。
"""
import hashlib
import io
import os
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-268-review-window-42a7ad"
SP = os.path.dirname(os.path.abspath(__file__))
DL = r"C:\Users\admin\Downloads"
WHERE = sys.argv[1] if len(sys.argv) > 1 else "staged"

# 受詞 ＝ (倉內路徑, 落檔前來源之絕對路徑)
PAIRS = [
    ("docs/orders/W-G.9-268_施工單_GB67開修_K923二閘轉主動_K917遞補迴圈.md",
     os.path.join(DL, "W-G.9-268_施工單_GB67開修_K923二閘轉主動_K917遞補迴圈.md")),
    ("docs/orders/W-G.9-268_附件甲_審查窗報告與草稿.md",
     os.path.join(SP, "W-G.9-268_附件甲_審查窗報告與草稿.md")),
]
for fn in sorted(os.listdir(SP)):
    if fn.startswith("wg9268_") and fn.endswith(".py"):
        PAIRS.append(("verify/probes/" + fn, os.path.join(SP, fn)))


def blob_bytes(path):
    spec = (":" + path) if WHERE == "staged" else (WHERE + ":" + path)
    r = subprocess.run(["git", "-C", REPO, "cat-file", "blob", spec],
                       capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git cat-file 失敗 rc=%d ｜ %s"
                           % (r.returncode, r.stderr.decode("utf-8", "replace")[:120]))
    return r.stdout


print("比較端 ＝ %s" % ("index（staged）" if WHERE == "staged" else "commit " + WHERE))
print("受詞檔數 ＝ %d" % len(PAIRS))
print("")
print("%-3s %-44s %-10s %-10s %s" % ("#", "倉內路徑（basename）", "來源sha", "blob sha", "判"))
print("-" * 104)

ok = bad = 0
for i, (repo_path, src) in enumerate(PAIRS, 1):
    s = hashlib.sha256(io.open(src, "rb").read()).hexdigest()
    try:
        b = hashlib.sha256(blob_bytes(repo_path)).hexdigest()
    except RuntimeError as e:
        print("%-3d %-44s %-10s %-10s 🔴 %s" % (i, os.path.basename(repo_path)[:44],
                                               s[:8], "—", e))
        bad += 1
        continue
    same = (s == b)
    ok += same
    bad += (not same)
    print("%-3d %-44s %-10s %-10s %s" % (i, os.path.basename(repo_path)[:44],
                                         s[:8], b[:8],
                                         "✅ 逐位相同" if same else "🔴 相異"))

print("")
print("🔒 相同 %d ／ 相異 %d ／ 受詞 %d" % (ok, bad, len(PAIRS)))

# ── 判別力（⛔ 恆綠之自證）──────────────────────────────────────────
# 對照組 甲（須相異）：拿 A 檔之來源比 B 檔之 blob
a_src = hashlib.sha256(io.open(PAIRS[0][1], "rb").read()).hexdigest()
b_blob = hashlib.sha256(blob_bytes(PAIRS[1][0])).hexdigest()
print("🔒 對照組 甲（錯配·須相異）：%s vs %s ⇒ %s"
      % (a_src[:8], b_blob[:8], "✅ 相異" if a_src != b_blob else "🔴 相同 ⇒ 器紅"))
# 對照組 乙（須相同）：同一 blob 自比
c = hashlib.sha256(blob_bytes(PAIRS[0][0])).hexdigest()
print("🔒 對照組 乙（自比·須相同）：%s vs %s ⇒ %s"
      % (c[:8], c[:8], "✅ 相同"))
print("")
print("🔒 判 ＝ %s" % ("✅ 原封入倉成立" if bad == 0 else "🔴 停機（款二：該工項不過即停）"))
sys.exit(0 if bad == 0 else 1)
