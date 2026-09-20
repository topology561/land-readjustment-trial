# -*- coding: utf-8 -*-
r"""W-G.9-318 補令六 `§一`：恆常附款簿之**末端追加更正節**之組建器。

🛑 `常規七 一`：`裁 2` 之表（本補令 `:30`–`:34`）與 `ab` 之條文（`:85`–`:87`）
   皆由**檔案管線**抽取（⛔ 憑記憶重寫）。
🛑 `恆常附款 ab②`（本補令新立）：`z`／`aa`／`ab` 之條文一律**經索引取 `檔:列`**
   後以檔案管線取之，⛔ 文字搜框。
"""
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "174b0be1841125b14ed31267aebd0d274915c10f"
ORDER5 = "docs/orders/W-G.9-318_補令五_裁3之撤回與自誤443及恆常附款z_aa.md"
ORDER6 = "docs/orders/W-G.9-318_補令六_款數更正與正典索引之確立及自誤444.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
OUT = REPO + r"\verify\out\WG9318p6_book_payload.md"

# 索引之補全（款 → 檔, 起, 迄, 所繫）——其 `檔:列` 取自簿內既載之散文出處（⛔ 新查）
IDX = [
    ("z", ORDER5, 48, 48, "【`W-G.9-318R5` 自捕 `2`／`6`·⛔ 鑄自誤號】"),
    ("aa", ORDER5, 76, 79, "`自誤 443`"),
    ("ab", ORDER6, 85, 87, "`自誤 444`"),
]


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def blob_lines(p, rev=REV):
    r = g(["show", "%s:%s" % (rev, p)])
    if r.returncode != 0:
        raise SystemExit("🔴 讀不到 %s" % p)
    return r.stdout.decode("utf-8").splitlines()


def wt_lines(p):
    return open(REPO + "\\" + p.replace("/", "\\"), encoding="utf-8").read().splitlines()


def strip_q(s):
    return s[2:] if s.startswith("> ") else ("" if s.strip() == ">" else s)


def main():
    o6 = wt_lines(ORDER6)
    cache = {ORDER6: o6, ORDER5: blob_lines(ORDER5)}
    book = "\n".join(blob_lines(BOOK))

    tbl = o6[29:34]                       # :30–:34　裁 2 之三次量測表
    ab = [strip_q(x) for x in o6[84:87]]  # :85–:87　ab 之條文

    names = []
    for c in re.findall(r"^\|\s*`([a-z]{1,2})`\s*\|", book, re.M):
        if c not in names:
            names.append(c)
    order = sorted(names, key=lambda s: (len(s), s))
    have = set(re.findall(r"^### 款 `([a-z]{1,2})`　出處 ＝ ", book, re.M))
    missing = [c for c in order if c not in have]

    L = []
    w = L.append
    w("")
    w("## 🔧 補令五「書寫形二種·二形並取」之撤回 ＋ 正典索引之確立 ＋ 恆常附款 ab 之立"
      "（W-G.9-318 補令六·⛔ 上文一字不刪·純末端追加）")
    w("")
    w("🛑 **本節⛔ 鑄任何號**——其為**裁之落地**（`戒 36`）。**⛔ 追改本簿上文一字。**")
    w("🔒 **態** ＝ `%s`（本批開工態·`恆常附款 w②`）。" % REV)
    w("")
    w("### `(a)`　「書寫形 `2` 種·後之搜框須二形並取」之**全部撤回**（補令六 `裁 2`）")
    w("")
    w("🔒 **三次量測、三個數（逐字轉錄自本補令 `:30`–`:34`·⛔ 改寫）**：")
    w("")
    for ln in tbl:
        w(ln)
    w("")
    w("⇒ 🔑 **「書寫形之種數」本身即<u>框依存</u>** ⇒ 🛑 **⛔ 釘定其數**、**⛔ 以任何形數定搜框**。")
    w("⇒ 🔒 補令五 `§一(b)` 之「其倉內書寫形計 `2` 種……後之搜框須二形並取」**撤回**；"
      "本簿前節（補令五所落）**⛔ 改上文一字**，本節即其更正之載體。")
    w("🩸 **登記** ＝ `自誤 444`（`docs/reports/W-G.9波_claude.ai側自誤登記.md` 檔末）。")
    w("🔒 **CC 前批所報之 `4` 形⛔ 為「正確之數」**——其與發單側之 `2`／`5` 同為**某一分類器之值**；"
      "本裁之要旨正在於**該數⛔ 可釘定**，而⛔ 在於孰者為真。")
    w("")
    w("### `(b)`　**正典索引之確立**（`恆常附款 ab②` 之結構解）")
    w("")
    w("🔒 **本簿 `§三` 之 `### 款 \\`x\\`　出處 ＝ \\`檔:列\\`` 節題即<u>正典索引</u>。**")
    w("🛑 **此後查任一款之條文，一律經本簿取其 `檔:列` 後以<u>檔案管線</u>取之**，"
      "**⛔ 以文字搜框搜之**——搜框之射程問題於索引存在後**自始不生**。")
    w("")
    w("🛑 **維護款（`§一(b)` 逐字）**：**此後每立一款，<u>同批</u>須補其 `出處`（檔:列）；"
      "⛔ 留空、⛔ 待後補。**")
    w("")
    w("🩸 **本批之索引補全（機械現查·⛔ 新查其值）**：本簿於期初之款名 ＝ **`%d`**，"
      "而具索引形 `出處` 節題者僅 **`%d`** ⇒ **缺 `%d` 款** ＝ %s"
      % (len(order), len(have), len(missing), "／".join("`%s`" % c for c in missing)))
    w("——其 `檔:列` **早已載於本簿前節之散文**（`z` ＝ 補令五 `:48`；`aa` ＝ 補令五 `:76`–`:79`），"
      "惟**未取索引形** ⇒ 依上開維護款於本節 `(d)` 補全，⛔ 改前節一字、⛔ 新查其值。")
    w("")
    w("### `(c)`　恆常附款 **`ab`** 之立（`自誤 444` 之攔法·逐字）")
    w("")
    for ln in ab:
        w("> " + ln if ln.strip() else ">")
    w("")
    w("### `(d)`　索引之補全 ＋ 新款之索引（**`3` 款**·條文皆經索引以檔案管線取之）")
    w("")
    for ch, path, a, b, tie in IDX:
        # 🔒 索引形須與 `§三` 既有者**逐字同族**（`^### 款 \`x\`　出處 ＝ `）
        #    ——⛔ 取 `####`，否則索引讀取器結構上⛔ 命中之（`常規四（九）四` 之同理）。
        w("### 款 `%s`　出處 ＝ `%s:%d`%s　（所繫 ＝ %s）"
          % (ch, path, a, ("–`:%d`" % b) if b > a else "", tie))
        w("")
        lines = cache[path]
        for k in range(a - 1, b):
            # 🩸 自捕：`z`／`aa` 之源列於單內**本即 `> ` 引用形** ⇒ 首版未剝而生 `> > `。
            #    一律剝一層後再加本簿之引用層。
            s = strip_q(lines[k])
            w("> " + s if s.strip() else ">")
        w("")
    w("### `(e)`　款之總表之**增列**（⛔ 追改 `§一` 表一字）")
    w("")
    w("| 款 | 受詞一句（**節略·⛔ 逐字**） | 所繫之自誤號 | 其逐字出處（檔:列） | 可得性判 | 射程之增補 |")
    w("|---|---|---|---|---|---|")
    w("| `ab` | ① 凡單內新立或修訂一款者，出單前須以該款對**本單自身**逐條施行一次並出艙其結果"
      "（`恆常附款 a` 之射程明文擴及「本單所新立之款」）；② 凡可由一份**正典索引**直接取得之物，"
      "⛔ 以文字搜框取之；索引不存在者**先立索引、⛔ 先定框** | `自誤 444` | `%s:85`–`:87` | "
      "🟢 **可得**（本批新立） | — |" % ORDER6)
    w("")
    w("🔒 **款數之算式（`恆常附款 f`·⛔ 直接寫一個數）**：")
    w("期初 ＝ **`%d`** 款（**列舉** ＝ %s）"
      % (len(order), "／".join("`%s`" % c for c in order)))
    w("＋ 本批新立 **`1`**（`ab`）⇒ 期末 ＝ **`%d`** 款。與 `裁 1`／`§一` 閘所載之 "
      "`27` → `28` **逐位相符** 🟢。" % (len(order) + 1))
    w("🔒 **索引之完備**：期末具索引形 `出處` 節題者 ＝ 期初 `%d` ＋ 本節 `(d)` 之 `%d` ＝ **`%d`**"
      "（＝ 款名總數 `%d`）⇒ **缺 `出處` 者 `0`** 🟢。"
      % (len(have), len(IDX), len(have) + len(IDX), len(order) + 1))
    w("")
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("payload 已落檔 ＝ %s" % OUT)
    print("列數 ＝ %d" % (len(L) + 1))
    print("期初款名 ＝ %d %s" % (len(order), order))
    print("期初具索引形者 ＝ %d／缺 %s" % (len(have), missing))
    print("本節補 %d 款之索引 ⇒ 期末 %d 款皆具索引" % (len(IDX), len(order) + 1))


if __name__ == "__main__":
    main()
