#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-283` `§四`：`forced` band 之界係**定義**抑或**近似**（四-1）
＋ 否定性存在宣稱之**射程補足**（四-2）。🛑 **出艙即止·⛔ 判**。

🔒 四-1 款 `2` 之母體 ＝ `_corner_buffer_S` 之**函式體（AST 區間）**——⛔ 文字層估界。
🔒 四-2 之母體 ＝ `verify/` 之**全部** `.py`（**含子層**·正面列舉）＋ `docs/specs/` 之全部 `.md`
   ——⛔ 以 pathspec glob 界定（坑 `be`）；`git ls-tree -z` 之**原始位元組**（坑 `bc`）。

🛑 **⛔ 判該界為「真正的地界」抑或「替身線」、⛔ 判碼面是否違反任何裁、⛔ 鑄號、⛔ 呈 KL。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9283_band.py <rev>`
`rc`：`0`／`5` **器紅**（AST 區間取不到／判別力造不如預期）。
"""
import ast
import io
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
REV = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
APP = "app.py"
SP = "verify/stepg_pipeline.py"


def say(s=""):
    print(s)


def git(*a):
    r = subprocess.run(["git", "-C", REPO, "-c", "core.quotePath=false"] + list(a),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.returncode, r.stdout, r.stderr


def blob(p):
    rc, o, _ = git("show", REV + ":" + p)
    return o if rc == 0 else None


def hdr(s):
    say("")
    say("#" * 112)
    say("# " + s)
    say("#" * 112)


RA = blob(APP)
LA = RA.decode("utf-8").split("\n")
RS = blob(SP)
LS = RS.decode("utf-8").split("\n")

say("=" * 112)
say("【`W-G.9-283` `§四`】`forced` band 之界 ＋ 否定性宣稱之射程補足")
say("=" * 112)
say("  三軸 (1) 來源 commit ＝ " + REV)
say("       (2) 母體逐款具名（見各款）")
say("       (3) 粒度框 ＝ **列框**（另註者從其註）")
say("  " + APP + "　" + str(len(RA)) + " B / " + str(len(LA)) + " 列")
say("  " + SP + "　" + str(len(RS)) + " B / " + str(len(LS)) + " 列")

# ══ 四-1 款 1 ═══════════════════════════════════════════════════════════
hdr("四-1 款 1　`_corner_buffer_S` 之「帶之構造」段與「bisect 解 buf」段**逐字**（本批重量）")
NEEDLE = "_corner_buffer_S"
nf = sum(1 for L in (LA, LS) if any(NEEDLE in x for x in L))
nl = sum(sum(1 for x in L if NEEDLE in x) for L in (LA, LS))
say("  錨（無 ^ 錨·**二數並報**）＝ " + NEEDLE + "｜母體 ＝ " + APP + " ＋ " + SP
    + " 二檔 ⇒ **命中檔數 " + str(nf) + " / 命中列數 " + str(nl) + "**")

# AST 區間
tree = ast.parse(RA.decode("utf-8"))
fn = None
for n in ast.walk(tree):
    if isinstance(n, ast.FunctionDef) and n.name == "_corner_buffer_S":
        fn = n
        break
if fn is None:
    say("  🛑 AST 取不到 `_corner_buffer_S` ⇒ loud 拒測")
    sys.exit(5)
S, E = fn.lineno, fn.end_lineno
say("  🔒 **AST 區間**（⛔ 文字層估界）：`def` 於列 " + str(S) + "，`end_lineno` ＝ "
    + str(E) + "（共 " + str(E - S + 1) + " 列）")
BODY = LA[S - 1:E]

say("")
say("  ── 「bisect 解 buf」段（逐字·框 ＝ 含 `bisect` 或 `range_area ==` 之列）")
for i, x in enumerate(BODY, start=S):
    if "bisect" in x or "range_area ==" in x:
        say("     [" + str(i) + "] " + x)
say("")
say("  ── 「帶之構造」段（逐字·框 ＝ 自含 `帶之構造` 之列起至次一 `── ` 標尺前）")
k = None
for i, x in enumerate(BODY, start=S):
    if "帶之構造" in x:
        k = i
        break
if k is None:
    say("     🛑 查無「帶之構造」之列 ⇒ loud")
else:
    j = k
    while j <= E:
        say("     [" + str(j) + "] " + LA[j - 1])
        j += 1
        if j <= E and "──" in LA[j - 1] and "帶之構造" not in LA[j - 1]:
            break

# ══ 四-1 款 2 ═══════════════════════════════════════════════════════════
hdr("四-1 款 2　bisect 之**目標函式**：其面積由**實際多邊形**抑或**矩形／平均深度**近似算得")
say("  母體 ＝ `_corner_buffer_S` 之**函式體**（AST 區間 " + str(S) + "–" + str(E)
    + "·⛔ 文字層估界）·粒度框 ＝ **列框**")
CAND = ["_block_strip(", "_strip_s_range(", "avg_depth", "矩形", "近似",
        "rect", "range_area", "area", "bisect"]
say("  逐字樣之命中（**逐項具名**·⛔ 只書「查無」）：")
CNT = {}
for c in CAND:
    n = sum(1 for x in BODY if c in x)
    CNT[c] = n
    say("     · `%-18s` ⇒ 列數 %d" % (c, n))
say("")
say("  [必命中] `_block_strip(` 於該函式體內 ＝ **" + str(CNT["_block_strip("])
    + "**（須 ≥ 1） ⇒ " + ("✅" if CNT["_block_strip("] >= 1 else "🔴 loud"))
FAKE = "_block_strip_" + str(9000 + 997) + "("      # 執行期組出·字面⛔ 出艙
nfk = sum(1 for x in BODY if FAKE in x)
say("  [必為零] 人造字樣（**執行期組出**·字面⛔ 出艙）＝ **" + str(nfk)
    + "**（須 0） ⇒ " + ("✅" if nfk == 0 else "🔴"))
if CNT["_block_strip("] < 1 or nfk != 0:
    say("  🛑 判別力造不如預期 ⇒ loud 拒測")
    sys.exit(5)
say("")
say("  ── 含 `_block_strip(` 之列（逐字）")
for i, x in enumerate(BODY, start=S):
    if "_block_strip(" in x:
        say("     [" + str(i) + "] " + x)
say("  ── 含 `avg_depth`／`矩形`／`近似` 之列（逐字·供發單側判讀）")
for i, x in enumerate(BODY, start=S):
    if ("avg_depth" in x) or ("矩形" in x) or ("近似" in x):
        say("     [" + str(i) + "] " + x)

# ══ 四-1 款 3 ═══════════════════════════════════════════════════════════
hdr("四-1 款 3　`range_area` 之**來源**：其產生式逐字 ＋ 所依之裁")
say("  母體 ＝ 呼叫端二檔（**逐檔具名**）：" + APP + "／" + SP + "·粒度框 ＝ **列框**")
for path, L in ((APP, LA), (SP, LS)):
    idx = [i for i, x in enumerate(L) if "_corner_buffer_S(" in x]
    say("  ── " + path + "：`_corner_buffer_S(` 之呼叫列數 ＝ " + str(len(idx)))
    for i in idx:
        say("     [" + str(i + 1) + "] " + L[i].rstrip())
        for j in range(i + 1, min(i + 9, len(L))):
            say("              | " + L[j].rstrip())
            if L[j].rstrip().endswith(")"):
                break
RNG = "_build_corner_range_v3"
nf2 = sum(1 for L in (LA, LS) if any(RNG in x for x in L))
nl2 = sum(sum(1 for x in L if RNG in x) for L in (LA, LS))
say("")
say("  `range_area` 之上游（錨 ＝ " + RNG + "·無 ^ 錨 ⇒ **二數並報**）⇒ 檔數 "
    + str(nf2) + " / 列數 " + str(nl2))
say("  ── 含 `range_area` 且含 `=` 之賦值列（`app.py`·逐字）")
for i, x in enumerate(LA):
    if re.match(r"^\s*_?range_area\s*=", x) or re.search(r"range_area=", x):
        say("     [" + str(i + 1) + "] " + x.rstrip()[:150])

# ══ 四-1 款 4 ═══════════════════════════════════════════════════════════
hdr("四-1 款 4　帶之**上界**是否即 `buf` ＋ 消費端 `left_cum_S = buf` 之逐位對映（本批重量）")
say("  框（**有 ^ 錨**）＝ `^\\s*left_cum_S = float`｜母體 ＝ " + SP + " 單檔")
hits = [i for i, x in enumerate(LS) if re.match(r"^\s*left_cum_S = float", x)]
say("     ⇒ **命中檔數 1 / 命中列數 " + str(len(hits)) + "**")
for i in hits:
    say("     [" + str(i + 1) + "] " + LS[i])
say("  🔒 前批（`W-G.9-282R §四` 款 `2`／`3`）已得之逐位對拍：")
say("     `0m`   態甲 R4/left：left_cum_S = 4.49975224003872   ＝ buf（range_area = 116.08）")
say("     `3.5m` 態甲 R4/left：left_cum_S = 7.8185635189090075 ＝ buf（range_area = 226.01）")
say("  🛑 上二列係**轉引前批之實測**（其母體 ＝ `verify/out/WG9282R_branch.log`）——本款只重量其**框**，")
say("     ⛔ 於本批重跑該長跑（單 `§七`：⛔ 未經本單具名之長跑）。")

# ══ 四-2　射程補足 ═══════════════════════════════════════════════════════
hdr("四-2　否定性存在宣稱之**射程補足**（⛔ 只書「查無」·逐一列出所查之側）")
rc, o, _ = git("ls-tree", "-r", "--name-only", "-z", REV)
ALL = [x for x in o.decode("utf-8").split("\x00") if x.strip()]
VPY = sorted(p for p in ALL if p.startswith("verify/") and p.endswith(".py"))
SPECS = sorted(p for p in ALL if p.startswith("docs/specs/") and p.endswith(".md"))
say("  母體（**正面列舉**·`git ls-tree -z` 之原始位元組·坑 `bc`）：")
say("     · `verify/` 之全部 `.py`（**含子層**）＝ **" + str(len(VPY)) + "** 檔")
say("     · `docs/specs/` 之全部 `.md` ＝ **" + str(len(SPECS)) + "** 檔")
say("     · 合計 ＝ **" + str(len(VPY) + len(SPECS)) + "** 檔")
say("  🔒 **⛔ 以 pathspec glob 界定**（坑 `be`：git 之 `*` 跨 `/`）——以上係逐檔過濾之結果。")

CACHE = {}
unread = 0
for p in VPY + SPECS:
    b = blob(p)
    if b is None:
        unread += 1
        continue
    try:
        CACHE[p] = b.decode("utf-8").split("\n")
    except Exception:                                           # noqa: BLE001
        unread += 1
say("  可讀 ＝ " + str(len(CACHE)) + "（讀不到 " + str(unread) + "）")

WORDS = ["抵費地", "強制抵費地", "抵費地多邊形", "抵費地_poly", "offset_poly",
         "_off_poly", "forced_poly", "range_poly", "forced_offset",
         "left_buffer_S", "right_buffer_S", "_corner_buffer_S",
         "_block_strip(", "橘色抵費地", "指配", "Polygon", "shapely"]
say("")
say("  **所查之字樣（逐項具名·⛔ 只書「查無」）與其命中（檔數／列數）**：")
for w in WORDS:
    nfw = nlw = 0
    for p, L in CACHE.items():
        k = sum(1 for x in L if w in x)
        if k:
            nfw += 1
        nlw += k
    say("     · `%-18s` ⇒ 檔數 %-4d / 列數 %d" % (w, nfw, nlw))

say("")
say("  ── **`抵費地` ∩ 幾何字樣**（`Polygon`／`poly`／`shapely`／`buffer`／`intersection`）之列")
GEO = re.compile("Polygon|poly|shapely|buffer|intersection")
ngeo = 0
for p, L in sorted(CACHE.items()):
    for i, x in enumerate(L):
        if "抵費地" in x and GEO.search(x):
            ngeo += 1
            say("     [" + p + ":" + str(i + 1) + "] " + x.strip()[:140])
say("  ⇒ 交集之列數 ＝ **" + str(ngeo) + "**")

say("")
say("  ── `docs/specs/` 內之**規格**（若碼面未實作 ⇒ loud 具名·⛔ 判其效力）")
nspec = 0
for p in SPECS:
    L = CACHE.get(p, [])
    for i, x in enumerate(L):
        if "抵費地" in x and (GEO.search(x) or "多邊形" in x or "界線" in x):
            nspec += 1
            say("     [" + p + ":" + str(i + 1) + "] " + x.strip()[:140])
say("  ⇒ `docs/specs/` 內之相關列數 ＝ **" + str(nspec) + "**")

# 判別力二造
CTL_Y = "def "
nfy = nly = 0
for p, L in CACHE.items():
    k = sum(1 for x in L if CTL_Y in x)
    if k:
        nfy += 1
    nly += k
FAKE2 = "抵費地" + chr(0x5EE3) + str(9000 + 997) + "XYZ"   # 執行期組出·字面⛔ 出艙
nfn = nln = 0
for p, L in CACHE.items():
    k = sum(1 for x in L if FAKE2 in x)
    if k:
        nfn += 1
    nln += k
say("")
say("  [判別力必命中] 字樣 `def ` ⇒ 檔數 " + str(nfy) + " / 列數 " + str(nly))
say("  [判別力必為零] 人造字樣（**執行期組出**·字面⛔ 出艙）⇒ 檔數 " + str(nfn)
    + " / 列數 " + str(nln))
say("  ⇒ 器 " + ("**非紅** ✅" if (nly > 0 and nln == 0) else "🔴 紅"))
if not (nly > 0 and nln == 0):
    sys.exit(5)

say("")
say("#" * 112)
say("🛑 **出艙即止**：⛔ 判該界為「真正的地界」抑或「替身線」（繫 §三 之出處判定）、")
say("⛔ 判碼面是否違反任何裁、⛔ 鑄號、⛔ 提修法主張、⛔ 呈 KL。")
say("#" * 112)
sys.exit(0)
