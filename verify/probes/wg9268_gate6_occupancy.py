#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""W-G.9-268 閘 6：號占用閘（宣告框·母體 ＝ 全 `docs/`·blob 層）。

🔒 框之出處（逐字自倉·CLAUDE.md 之補款節）
  ①  宣告框 ＝ D1 檔名 ∪ D2 文內標題形（列首 `#+` 之列含該號）
                ∪ D3 自稱形（列首**即**該號，或同列含「本單」＋ 該號）
                三者皆帶數字邊界 `(?!\\d)`
  ②  ⛔ 計入：計算式／引用／對照表／待辦清單之提及
  ③  母體 ＝ 全 `docs/`（倉側 blob）；`*.py` 之檔名含單號者係衍生物·⛔ 構成占用
  ④  二框並列、各載框；判準取宣告框，鬆框僅作**漏框偵察**
  ⑤  D3 之「本單」款：僅於該號 ＝ **該檔檔名所載之單號**時成立
  ⑥  三數分列：D1 檔數／D2 列數／D3 列數（D1 ⛔ 產生任何列命中）
  ⑦  列框 ＝ |D2 ∪ D3|（**聯集**·⛔ 和）；檔框 ＝ |D1 ∪ D2之檔 ∪ D3之檔|
  ⑧  D3「列首即該號」＝ **嚴格式**（⛔ 前導 ` * _ > - 空白）

  補款一（W-G.9-160）：意指占用之框一律用**錨定框** `(?<![0-9\\-])<完整號>(?!\\d)`
"""
import re
import subprocess
import sys

REV = sys.argv[1]
TARGET = sys.argv[2]                       # 受詢之號，如 W-G.9-268
CONTROLS = sys.argv[3:]                    # 對照組

# 錨定框（補款一）：前不得為數字或連字號，後不得為數字
ANCHORED = r"(?<![0-9\-])" + re.escape(TARGET) + r"(?![0-9])"


def blob_list():
    """🩸 **必用 `-z`**：CJK 檔名於預設 `core.quotePath` 下被**八進位跳脫**
       ⇒ `git show REV:<跳脫後之名>` 必敗 ⇒ 該檔靜默退出母體（本器首版即此瑕·622/628）。
       `-z` 為 NUL 分隔且**⛔ 跳脫** ⇒ 路徑為真值。"""
    out = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", REV, "docs/"],
                         capture_output=True, check=True).stdout
    return out.decode("utf-8").split("\0")


def blob(path):
    """⛔ `check=True` 之靜默吞——git 失敗與解碼失敗須**分列**（W-G.9-14 修法 ②：
       「無從判定」與「判定為偽」⛔ 共用同一出艙碼）。"""
    r = subprocess.run(["git", "show", "%s:%s" % (REV, path)], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git-fail rc=%d" % r.returncode)
    return r.stdout


files = [p for p in blob_list() if p.strip()]
texts, git_fail, dec_fail = {}, [], []
for p in files:
    try:
        raw = blob(p)
    except RuntimeError:
        git_fail.append(p)
        continue
    try:
        texts[p] = raw.decode("utf-8")
    except UnicodeDecodeError:
        dec_fail.append(p)
unreadable = git_fail + dec_fail

print("三軸 (1) 來源 ＝ %s" % REV)
print("三軸 (2) 母體 ＝ 全 docs/ %d 檔（讀不到 %d ＝ git失敗 %d ＋ 解碼失敗 %d）" % (len(files), len(unreadable), len(git_fail), len(dec_fail)))
print("三軸 (3) 粒度框 ＝ 檔框 ＋ 列框（宣告框·D1/D2/D3 三數分列）")
print("")


def measure(num, strict=True):
    """回 dict：D1 檔集／D2 列集／D3 列集／雙屬／列框(聯集)／檔框／鬆框。"""
    anch = r"(?<![0-9\-])" + re.escape(num) + r"(?![0-9])"
    rx_any = re.compile(anch)
    rx_d2 = re.compile(r"^#+.*?" + anch, re.S)
    # ⑧ 嚴格式：列首**即**該號；寬式：允前導 ` * _ > - 空白
    rx_d3a = re.compile(r"^" + anch) if strict else re.compile(r"^[\s`*>_-]*" + anch)
    d1_files, d2_lines, d3_lines, loose_lines, loose_files = set(), set(), set(), set(), set()
    for p, t in texts.items():
        base = p.rsplit("/", 1)[-1]
        if rx_any.search(base):
            d1_files.add(p)
        fname_num = rx_any.search(base) is not None      # ⑤：該號 ＝ 檔名之號
        for i, ln in enumerate(t.split("\n"), 1):
            if not rx_any.search(ln):
                continue
            loose_lines.add((p, i))
            loose_files.add(p)
            if rx_d2.match(ln):
                d2_lines.add((p, i))
            if rx_d3a.match(ln) or ("本單" in ln and fname_num):
                d3_lines.add((p, i))
    both = d2_lines & d3_lines
    lineframe = d2_lines | d3_lines                        # ⑦ 聯集
    filframe = d1_files | {p for p, _ in lineframe}
    return dict(d1=d1_files, d2=d2_lines, d3=d3_lines, both=both,
                lf=lineframe, ff=filframe, ll=loose_lines, lfl=loose_files)


def report(num, strict, role):
    r = measure(num, strict)
    print("  %-14s %-5s D1 檔=%-4d D2 列=%-4d D3 列=%-4d 雙屬=%-3d "
          "列框(∪)=%-4d 檔框=%-4d ｜ 鬆框 檔=%-4d 列=%-4d ｜ %s"
          % (num, "嚴格" if strict else "寬式",
             len(r["d1"]), len(r["d2"]), len(r["d3"]), len(r["both"]),
             len(r["lf"]), len(r["ff"]), len(r["lfl"]), len(r["ll"]), role))
    return r


print("── 受詢之號 ──")
t_strict = report(TARGET, True, "受詢 ⇒ 須全 0")
t_loose = report(TARGET, False, "受詢 ⇒ 須全 0")
print("")
print("── 對照組 甲（已知占用·須 ≥1）──")
for c in CONTROLS:
    report(c, True, "甲（須 ≥1）")
    report(c, False, "甲（須 ≥1）")

# 對照組 乙（須 =0）：人造受詞，其字樣**於執行期組出**，⛔ 使其字面落入任何檔（GB-147）
_NEG = "W-G" + ".9-" + str(7 * 137 + 4)          # ⇒ 一必不存在之號
print("")
print("── 對照組 乙（人造·執行期組出·代稱 ⟨NEG⟩·須 =0）──")
_r = report(_NEG, True, "乙（須 =0）")
_r2 = report(_NEG, False, "乙（須 =0）")
print("   ⟨NEG⟩ 之六數 =",
      [len(_r["d1"]), len(_r["d2"]), len(_r["d3"]),
       len(_r2["d1"]), len(_r2["d2"]), len(_r2["d3"])],
      "／鬆框列 =", len(_r["ll"]))

print("")
print("🔒 判：受詢之六數（嚴格 D1/D2/D3 ＋ 寬式 D1/D2/D3）=",
      [len(t_strict["d1"]), len(t_strict["d2"]), len(t_strict["d3"]),
       len(t_loose["d1"]), len(t_loose["d2"]), len(t_loose["d3"])])
if t_strict["ll"]:
    print("🔴 鬆框之命中（漏框偵察·逐筆具名）：")
    for p, i in sorted(t_strict["ll"]):
        print("     %s:%d ｜ %s" % (p, i, texts[p].split("\n")[i - 1].strip()[:110]))
else:
    print("   鬆框亦 0 ⇒ ⛔ 漏框之虞")
