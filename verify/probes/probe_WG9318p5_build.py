# -*- coding: utf-8 -*-
r"""W-G.9-318 補令五 `§一`：恆常附款簿之**末端追加更正節**之組建器。

🛑 `常規七 一`：`z`／`aa` 之逐字條文由**檔案管線**自本補令抽取（⛔ 憑記憶重寫）：
   `z`  ＝ 本補令 `:48`（剝 `> `）
   `aa` ＝ 本補令 `:76`–`:79`（剝 `> `）
🛑 `裁 1` 之逐字亦自本補令 `:36`–`:38` 抽取。
🔒 形之分佈取自 `probe_WG9318p5_forms.py` 之實測（⛔ 採單載之「`2` 種」·`恆常附款 f`）。
"""
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "549121b27beb6a34b3a6c823af43c78e37b0c7ee"
ORDER5 = "docs/orders/W-G.9-318_補令五_裁3之撤回與自誤443及恆常附款z_aa.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
OUTPAY = REPO + r"\verify\out\WG9318p5_book_payload.md"

FORMS = [
    ("① 指向形", re.compile(r"立為恆常附款（`§一-1` 款 `[a-z]{1,2}`）")),
    ("② 區塊「（x）條文」形", re.compile(r"^[>\s]*[（(]\s*`?[a-z]{1,2}`?\s*[·`）)]")),
    ("③ 攔法形", re.compile(r"^\s*>?\s*\*\*攔法[^\n]*立為恆常附款 `[a-z]{1,2}`")),
    ("④ 行內「本單所增（x…）」形", re.compile(r"^🆕 \*\*本單所增")),
]


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def text(p, rev=REV):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def strip_q(s):
    return s[2:] if s.startswith("> ") else ("" if s.strip() == ">" else s)


def main():
    order = open(REPO + "\\" + ORDER5.replace("/", "\\"), encoding="utf-8").read().splitlines()
    book = text(BOOK)

    z_txt = strip_q(order[47])                       # :48
    aa_txt = [strip_q(x) for x in order[75:79]]      # :76–:79
    rule1 = [order[35], order[36], order[37]]        # :36–:38

    # ── 形之實測分佈（逐款）──
    heads = re.findall(r"^### 款 `([a-z]{1,2})`　出處 ＝ `([^`]+):(\d+)`", book, re.M)
    cache, tally, unc = {}, {}, []
    for ch, path, ln in heads:
        if path not in cache:
            cache[path] = (text(path) or "").splitlines()
        line = cache[path][int(ln) - 1]
        hit = [nm for nm, pat in FORMS if pat.search(line)]
        if hit:
            tally.setdefault(hit[0], []).append(ch)
        else:
            unc.append(ch)
    aw = set("abcdefghijklmnopqrstuvw")

    L = []
    w = L.append
    w("")
    w("## 🔧 補令四 裁 3 之撤回 ＋ 第四形之具名 ＋ 恆常附款 z・aa 之立"
      "（W-G.9-318 補令五·⛔ 上文一字不刪·純末端追加）")
    w("")
    w("🛑 **本節⛔ 鑄任何號**——其為**裁之落地**（`戒 36`）。**⛔ 追改本簿上文一字。**")
    w("🔒 **態** ＝ `%s`（本批開工態·`恆常附款 w②`）。" % REV)
    w("")
    w("### `(a)`　補令四 `裁 3` 之**全部撤回**（補令五 `裁 1` 逐字）")
    w("")
    w("🔒 **發單側自倉逐字覆核之結論（逐字轉錄·⛔ 改寫）**：")
    w("")
    for ln in rule1:
        w("> " + ln if ln.strip() else ">")
    w("")
    w("⇒ 🔒 **補令四 `裁 3` 之「失傳 `3`／重鑄 `4`」<u>全部撤回</u>**；"
      "其 `§二` **三禁 ①②撤回**（**三禁 ③ 維持**）。")
    w("⇒ 🔒 **本簿 `§一`／`§二`／`§三` 之判（`a`〜`w` 全 `23` 款 🟢 可得·逐款附 `檔:列`）"
      "經發單側受領為<u>正</u>**——⛔ 改其上文一字。")
    w("🩸 **登記** ＝ `自誤 443`（`docs/reports/W-G.9波_claude.ai側自誤登記.md` 檔末）。")
    w("")
    w("### `(b)`　諸款**書寫形**之具名（🔴 **實測 `%d` 形·⛔ 單載之 `2` 形**）" % (len(tally) + (1 if unc else 0)))
    w("")
    w("🩸 **具名之相異（`恆常附款 f`：自載基數不符者**以列舉為準並具名**）**："
      "補令五 `§一 (b)` 逐字載「其倉內書寫形計 **`2` 種**」並令「**後之搜框須二形並取**」；")
    w("CC 以簿 `§三` 之逐款 `(檔, 起列)` 為受詞當場分類，得 **`%d` 形**（`a`〜`y`）。"
      % (len(tally) + (1 if unc else 0)))
    w("🛑 **⇒ 後之搜框須 `%d` 形並取，⛔ 二形**——二形並取將漏 `%d` 款。"
      % (len(tally) + (1 if unc else 0),
         len([c for c in tally.get("④ 行內「本單所增（x…）」形", []) if c in aw])
         + len([c for c in tally.get("③ 攔法形", []) if c in aw])))
    w("")
    w("| 形 | 樣式（逐字·`grep` 可用） | 款數（`a`〜`y`） | 逐款 |")
    w("|---|---|---|---|")
    pats = {
        "① 指向形": "`立為恆常附款（\\`§一-1\\` 款 \\`x\\`）`",
        "② 區塊「（x）條文」形": "`^[>\\s]*[（(]\\s*\\`?[a-z]{1,2}\\`?\\s*[·\\`）)]`",
        "③ 攔法形": "`^\\s*>?\\s*\\*\\*攔法[^\\n]*立為恆常附款 \\`[a-z]{1,2}\\``",
        "④ 行內「本單所增（x…）」形": "`^🆕 \\*\\*本單所增`",
    }
    for nm, _ in FORMS:
        v = tally.get(nm, [])
        w("| %s | %s | **`%d`** | %s |"
          % (nm, pats[nm], len(v), "／".join("`%s`" % c for c in v) or "—"))
    if unc:
        w("| 🆕 ⑤ 補令四 `§四` 之「**`x`**：條文」形 | `^\\*\\*\\`[a-z]{1,2}\\`\\*\\*：` | **`%d`** | %s |"
          % (len(unc), "／".join("`%s`" % c for c in unc)))
    w("")
    w("🔑 **形 ① 之要**：`c`／`d` 之「指向形」**⛔ 條文之所在**——其僅**指向**，"
      "條文本身在形 ②／④。⇒ 補令四 `裁 3` 表所載「`c`／`d` 🟢 可得——其條文 ＝ 該單 "
      "`§一-1` 之款 `c` 列」**其結論為真而其所指之列為誤**；本簿 `§三` 所錄者為**條文本身**。")
    w("🔒 **判別力二造（`恆常附款 aa①`：[必命中]之造須與受詢**同一形族**）**：")
    w("[必命中] ＝ 形 ①〜④ 中有款者 ＝ **`%d`** 種（`> 0`）；" % len([1 for nm, _ in FORMS if tally.get(nm)]))
    w("[必為零] ＝ 一不存在之形樣式 ⇒ **`0`** 款。合計 `%d` ＝ 受詞數 `%d` 🟢"
      % (sum(len(v) for v in tally.values()) + len(unc), len(heads)))
    w("🔒 **器** ＝ `verify/probes/probe_WG9318p5_forms.py`·落檔 `verify/out/WG9318p5_forms.log`。")
    w("")
    w("### `(c)`　恆常附款 **`z`** 之立（補令五 `裁 4` 逐字）")
    w("")
    w("> " + z_txt)
    w("")
    w("🔒 **出處** ＝ `%s:48`。**所繫** ＝【`W-G.9-318R5` 自捕 `2`／`6`·⛔ 鑄自誤號】。" % ORDER5)
    w("🔒 **本節即其首次施行**：見 `verify/out/WG9318p5_gates.log` "
      "——哨兵之判別力[必為零]二造，皆先**列舉定義域**（自誤已鑄集 `432` 個成員／本簿款名 `25` 個）"
      "再證哨兵 ⛔ 屬之。")
    w("")
    w("### `(d)`　恆常附款 **`aa`** 之立（`自誤 443` 之攔法·逐字）")
    w("")
    for ln in aa_txt:
        w("> " + ln if ln.strip() else ">")
    w("")
    w("🔒 **出處** ＝ `%s:76`–`:79`。**所繫** ＝ `自誤 443`。" % ORDER5)
    w("")
    w("### `(e)`　款之總表之**增列**（⛔ 追改 `§一` 表一字）")
    w("")
    w("| 款 | 受詞一句（**節略·⛔ 逐字**） | 所繫之自誤號 | 其逐字出處（檔:列） | 可得性判 | 射程之增補 |")
    w("|---|---|---|---|---|---|")
    w("| `z` | 凡以**人造哨兵**充判別力[必為零]之造者，須**當場自證**該哨兵確不在受詞之"
      "**定義域**中（**列舉該定義域並證哨兵⛔ 屬之**）；⛔ 以「執行期組出」充之 | "
      "【`W-G.9-318R5` 自捕 `2`／`6`·⛔ 鑄自誤號】 | `%s:48` | 🟢 **可得**（本批新立·`裁 4`） | — |" % ORDER5)
    w("| `aa` | 全稱否定之判別力須以**同一形族**之已知成員為[必命中]之造；二框並取須先"
      "**具名其相異維度**（僅差標點或動詞者⛔ 充二造）；受詞為某簿之全部成員者須先自"
      "**至少 `3` 個不同批次**取樣其書寫形 | `自誤 443` | `%s:76`–`:79` | 🟢 **可得**（本批新立） | — |" % ORDER5)
    w("")
    w("🔒 **款數之算式（`恆常附款 f`·⛔ 直接寫一個數）**：")
    w("期初 ＝ **`%d`** 款（`a`〜`y`·**列舉** ＝ %s）"
      % (len(heads), "／".join("`%s`" % c for c, _, _ in heads)))
    w("＋ 本批新立 **`2`**（`z`／`aa`）⇒ 期末 ＝ **`%d`** 款。" % (len(heads) + 2))
    w("🩸 **與單 `§一` 閘所載之相異（具名·⛔ 追改）**：單載「款數 `23` → **`25`**（增 `z`／`aa`）」，"
      "其期初 `23` 係 `a`〜`w` 之數，**未計補令四 `§四` 所立且已錄於本簿之 `x`／`y`** "
      "⇒ 依 `恆常附款 f` **以列舉為準**：`%d` → **`%d`**。" % (len(heads), len(heads) + 2))
    w("🔒 **可得性判之款數**：🔴 失傳 ＝ **`0`**／🟡 重鑄 ＝ **`0`**（全 🟢）——與單 `§一` 閘所載**相符**。")
    w("")
    with open(OUTPAY, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("payload 已落檔 ＝ %s" % OUTPAY)
    print("列數 ＝ %d" % (len(L) + 1))
    print("形之分佈 ＝ %s" % {k: len(v) for k, v in tally.items()})
    print("⛔ 歸類 ＝ %s" % unc)


if __name__ == "__main__":
    main()
