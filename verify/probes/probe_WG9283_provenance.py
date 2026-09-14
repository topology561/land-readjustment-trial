#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-283` `§三`：「該點即『面積換算出來的替身線』」之**出處判定**（🛑 出艙即止）。

🔒 **準據 ＝ `W-G.9-15` 甲組之<u>同一</u>機械規則**——本器**直接 import**
`verify/tools/wg915_ruling_provenance.py` 之 `build_blocks`／`classify`／`is_quote`／`KL_MARKS`，
**⛔ 另寫第二份判準**（單 `§三-2`）。

🛑 **該器之受詞與本項<u>不合</u>之處，於下 loud 明載**；⛔ 逕自改寫該器。

🛑 **⛔ 判該等同成立與否、⛔ 判碼面是否違反任何裁、⛔ 鑄 `GB`、⛔ 解除或收窄
   `GB-168`／`GB-169`、⛔ 提修法主張、⛔ 呈 KL。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9283_provenance.py <rev>`
`rc`：`0`／`5` **器紅**（字樣錨非唯一／判別力二造同判）。
"""
import io
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "tools"))

BT = chr(96)                                    # 反引號·⛔ 令其經 bash 一層（坑 `3`）
REV = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"

# ── 受詞與二造之字樣錨（`grep -F` 固定字串·⛔ regex·⛔ 行號為錨·**皆須唯一**）──
SUBJ = "（該點即「面積換算出來的替身線」）"
CTL_KL = "**裁定二**：「是 ⇒ 起算一律用真正的地界"
CTL_ASSIST = "；forced 時為其 buffer 起算點。"


def say(s=""):
    print(s)


def git(*a):
    r = subprocess.run(["git", "-C", REPO, "-c", "core.quotePath=false"] + list(a),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.returncode, r.stdout, r.stderr


def hdr(s):
    say("")
    say("#" * 112)
    say("# " + s)
    say("#" * 112)


import wg915_ruling_provenance as W15            # noqa: E402

hdr("器之載入與其**框逐字**（`W-G.9-15` 甲組·⛔ 另寫第二份判準）")
say("  器 ＝ verify/tools/wg915_ruling_provenance.py")
say("  🔒 所 import 之符號：build_blocks／classify／is_quote／KL_MARKS")
say("  框（逐字·自該器之 docstring 抽取·⛔ 重寫）：")
for ln in (W15.__doc__ or "").split("\n"):
    if ln.strip().startswith(("1.", "2.", "3.", "4.", "5.", "-")):
        say("     | " + ln.rstrip())
say("  KL_MARKS 逐字 ＝ " + repr(W15.KL_MARKS))
say("  is_quote 之逐字 ＝ " + repr(
    "return line.startswith(" + BT.join(["", ""]) + repr(">") + ")"))

hdr("🛑 **該器之受詞與本項之不合**（loud·⛔ 逕自改寫）")
say("  該器之**條目母體** ＝ 「含 🔒 之行」（其 main() 內逐字 ＝")
say("     pop = [i for i, x in enumerate(lines) if \"\\U0001f512\" in x]）；")
say("  本項之受詞 ＝ 一**不含 🔒** 之行 ⇒ **⛔ 落於該器之條目母體內**。")
say("  🔒 **處置**：本器**只沿用其機械規則之四符號**，**⛔ 沿用其條目母體**；")
say("     受詞由本單 §三-3 款 1 之字樣錨界定 ⇒ **⛔ 改該器一字**（其 blob 期初＝期末·見收工閘）。")

# ══ 母體 ═══════════════════════════════════════════════════════════════
rc, raw, err = git("show", REV + ":" + K6)
if rc != 0:
    raise SystemExit("讀不到 " + K6)
LINES = raw.decode("utf-8").split("\n")
hdr("母體之三軸")
say("  (1) 來源 commit ＝ " + REV)
say("  (2) 母體 ＝ " + K6 + " **單檔**｜" + str(len(raw)) + " B / "
    + str(len(LINES)) + " 列｜core.quotePath=false（該器之 git 包裝所釘）")
say("  (3) 粒度框 ＝ **列框**")

INQ, BID, LEAD = W15.build_blocks(LINES)
NB = ((max([b for b in BID if b is not None]) + 1)
      if any(b is not None for b in BID) else 0)
say("  引文行 ＝ " + str(sum(INQ)) + "｜引文區塊 ＝ " + str(NB) + " 段")


def locate(needle):
    return [i for i, x in enumerate(LINES) if needle in x]


def uniq(needle, tag):
    hs = locate(needle)
    say("  " + tag + "：字樣錨（grep -F 固定字串）⇒ **命中列數 = " + str(len(hs)) + "**（須 1）")
    if len(hs) != 1:
        say("     🛑 **非唯一 ⇒ 量測器紅**（⛔ 取 hs[0] 充之）；逐筆列出：")
        for h in hs:
            say("       [" + str(h + 1) + "] " + LINES[h][:130])
        return None
    return hs[0]


def block_span(idx):
    b = BID[idx]
    if b is None:
        return None, None
    s = idx
    while s > 0 and BID[s - 1] == b:
        s -= 1
    e = idx
    while e + 1 < len(LINES) and BID[e + 1] == b:
        e += 1
    return s, e


def two_counts(needle):
    n = sum(1 for x in LINES if needle in x)
    return (1 if n else 0), n


# ══ 款 1 ═══════════════════════════════════════════════════════════════
hdr("款 1　受詞行逐字 ＋ 其引文區塊之起迄 ＋ 該區塊之**引言逐字**")
nf, nl = two_counts("失效加註")
say("  錨（無 ^ 錨·**二數並報**）＝ 失效加註 ⇒ 命中檔數 " + str(nf) + " / 命中列數 " + str(nl))
I = uniq(SUBJ, "受詞")
if I is None:
    sys.exit(5)
say("")
say("  受詞行（逐字·列號作佐證·⛔ 作錨）：")
say("     [" + str(I + 1) + "] " + LINES[I])
say("  是否為引文行（is_quote·規則第 1 款「行首符合 ^>」）＝ " + str(W15.is_quote(LINES[I])))
S, E = block_span(I)
if S is None:
    say("")
    say("  🛑 **受詞行⛔ 落於任何引文區塊內**（其 BID ＝ None）")
    say("     由 ＝ 機械規則第 1 款以 **行首** 為準，而本行**以空白起首**：")
    say("     前 8 個字元之 repr ＝ " + repr(LINES[I][:8]))
    say("     LINES[I].startswith('>')          ＝ " + str(LINES[I].startswith(">")))
    say("     LINES[I].lstrip().startswith('>') ＝ " + str(LINES[I].lstrip().startswith(">")))
    say("  🔒 **⛔ 逕自改寫該規則**（單 §三-2 明令）——照實出艙即止。")
    _pre = [j for j in range(I - 1, -1, -1) if LINES[j].strip()]
    say("  其**往上最近之六個非空白行**（逐字·供發單側判讀）：")
    for j in _pre[:6][::-1]:
        say("     [" + str(j + 1) + "] " + LINES[j])
else:
    say("  其引文區塊 ＝ 列 " + str(S + 1) + "–" + str(E + 1) + "（" + str(E - S + 1) + " 列）")
    say("  區塊全文（逐字）：")
    for j in range(S, E + 1):
        say("     [" + str(j + 1) + "] " + LINES[j])
    say("  **引言**（區塊起點往上最近之非空白非引文行·逐字）：")
    say("     " + repr(LEAD[BID[I]]))

# ══ 款 2 ═══════════════════════════════════════════════════════════════
hdr("款 2　受詞行與其**前一行**之分界 ＋ 受詞是否落於「」引號對內")
say("  二行並列（逐字）：")
say("     前一行 [" + str(I) + "] " + LINES[I - 1])
say("     受詞行 [" + str(I + 1) + "] " + LINES[I])
RX_Q = re.compile("「[^」]*」")
say("")
say("  框 ＝ 該列內 「[^」]* 」 之比對（**逐列**）")
say("     前一行之引號對 = " + repr(RX_Q.findall(LINES[I - 1])))
say("     受詞行之引號對 = " + repr(RX_Q.findall(LINES[I])))
inside = any(SUBJ.strip("（）") in p for p in RX_Q.findall(LINES[I]))
say("  受詞（括號子句之全文）是否落於**任一**引號對之內？ " + str(inside))
say("  🔒 併報：受詞行之括號子句**本身**含一引號對（「面積換算出來的替身線」）")
say("     ——其為**子句之內部**，⛔ 使該子句落於某引號對之內。")

# ══ 款 3 ═══════════════════════════════════════════════════════════════
hdr("款 3　引入 commit 與日期（git log -S 之**字面**·⛔ regex）")


def log_S(s, tag):
    rc, out, _ = git("log", "--format=%H|%ad", "--date=iso", "-S", s, "--", K6)
    rows = [x for x in out.decode("utf-8", "replace").split("\n") if x.strip()]
    say("  ── " + tag)
    say("     git log -S <字面> -- <K-6> ⇒ 命中 commit 數 = " + str(len(rows)))
    for r in rows:
        say("       " + r)
    return rows[-1] if rows else None


r_subj = log_S(SUBJ, "受詞（括號子句）")
r_513 = log_S("### \U0001f512 K-9-5-13 ", "K-9-5-13 節之節題")
say("")
if r_subj and r_513:
    c_subj = r_subj.split("|")[0]
    c_513 = r_513.split("|")[0]
    rc1, _, _ = git("merge-base", "--is-ancestor", c_513, c_subj)
    rc2, _, _ = git("merge-base", "--is-ancestor", c_subj, c_513)
    say("  merge-base --is-ancestor <K-9-5-13 引入> <受詞引入> ⇒ rc = " + str(rc1))
    say("  **反向同式**（判別力自檢）⇒ rc = " + str(rc2))
    same = (c_subj == c_513)
    say("  二 commit 是否**同一**？ " + str(same))
    if same:
        say("  🔒 **二者係<u>同一</u> commit** ⇒ 反向同式必同得 rc = 0")
        say("     ——此係**受詞之事實**（同批引入），**⛔ 該檢之缺陷**；")
        say("     其判別力另由下式證：對一**必非祖先**之 rev 施同式須得 rc ≠ 0。")
        rc3, _, _ = git("merge-base", "--is-ancestor",
                        "05a11bd665f6c2790ff821c9e3a1606651e345d4", c_subj)
        say("     [判別力必非祖先] p3a ⇒ rc = " + str(rc3) + "（期 ≠ 0） ⇒ "
            + ("✅" if rc3 != 0 else "🔴"))
    else:
        say("  ⇒ 二 rc " + ("**相異** ⇒ 該檢非恆同 ✅" if rc1 != rc2
                            else "**相同** ⇒ 🛑 該檢無判別力"))
    say("  🔒 二者之日期見上（%ad·iso）。")

# ══ 款 4 ═══════════════════════════════════════════════════════════════
hdr("款 4　器之判（三類之一·依 §三-2 之**引言**判之·⛔ 以「在 > 內」充「KL 逐字」）")
kind, why = W15.classify(LINES, INQ, BID, LEAD, I)
say("  受詞行之判 ＝ **" + kind + "**")
say("  其由（器之逐字輸出）＝ " + why)

# ══ 款 5 ═══════════════════════════════════════════════════════════════
hdr("款 5　判別力二造（經**同一器**須得**相異**之判）")
CASES = [("[必為 KL 逐字] K-9-5-13（二）所答 之裁定二該行", CTL_KL, "KL 逐字"),
         ("[必為助手側] K-9-5-12（六）已判之「首宗起點」行", CTL_ASSIST, "助手側補充")]
res = []
allok = True
for tag, needle, exp in CASES:
    say("  ── " + tag)
    h = uniq(needle, "    錨")
    if h is None:
        allok = False
        res.append(None)
        continue
    k, w = W15.classify(LINES, INQ, BID, LEAD, h)
    say("     [" + str(h + 1) + "] 逐字 = " + LINES[h][:130])
    say("     判 = **" + k + "**｜" + w)
    say("     期 = " + exp + "｜實 = " + k + " ⇒ " + ("✅" if k == exp else "🔴"))
    if k != exp:
        allok = False
    res.append(k)
say("")
say("  二造之判 ＝ " + repr(res))
if len(res) == 2 and res[0] is not None and res[0] == res[1]:
    say("  🛑 **二造同判 ⇒ 判器紅、停、上呈**")
    sys.exit(5)
if None in res:
    say("  🛑 **有造之錨非唯一 ⇒ 判器紅、停**")
    sys.exit(5)
say("  ⇒ 二造**相異** ⇒ **器非紅** " + ("✅" if allok else "🟡（惟有期／實不符·見上）"))

# ══ 併查：受詞所在之「失效加註」區塊之全體判 ═══════════════════════════
hdr("併查（照實·出艙即止）：`失效加註` 三處之逐行判")
for i in locate("失效加註"):
    say("  ── 加註列 [" + str(i + 1) + "]｜is_quote = " + str(W15.is_quote(LINES[i]))
        + "｜判 = " + W15.classify(LINES, INQ, BID, LEAD, i)[0])
    say("     逐字 = " + LINES[i][:130])

say("")
say("#" * 112)
say("🛑 **出艙即止**：⛔ 判該等同成立與否、⛔ 判碼面是否違反 K-9-5-13／K-9-5-12（四）、")
say("⛔ 鑄 GB、⛔ 解除或收窄 GB-168／GB-169、⛔ 提修法主張、⛔ 呈 KL。")
say("#" * 112)
sys.exit(0)
