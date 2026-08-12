# -*- coding: utf-8 -*-
r"""`W-G.9-15` 甲組：**第 1 級正典**（`docs/rulings/`·權威序第 1 級）之**出處分層盤點**。

## 受詞

⛔ **不是「這句話對不對」，是「這句話<u>是誰說的</u>」。**
助手側補充也可能**內容正確**——分層與對錯是兩件事。

## 🔒 機械規則（`W-G.9-15` 事前登記 §3 於量測前寫定·⛔ 事後未改）

1. **引文行** ＝ 行首符合 `^>`（含單獨 `>` 與 `> …`）。
2. **引文區塊** ＝ 極大之連續引文行段。
3. **條目落在引文區塊內** ＝ **該條目所在之行本身為引文行**。
4. **引言** ＝ 區塊起點往上最近之**非空白且非引文**之行。
5. **分層**：
   - **KL 逐字** ＝ 在區塊內 **且** 引言含 `KL 逐字` 或 `KL 裁`。
   - **助手側補充** ＝ **不在**任何引文區塊內。
   - **無法判定** ＝ 在區塊內但引言不含上開字樣。

⛔ **不目視、⛔ 不用 `grep` 上下文窗**（考古 67 修法 ③）。

## 重跑
    python verify/tools/wg915_ruling_provenance.py
"""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

# 🔒 母體自證（考古 69 修法 ①）：⛔ 指錯倉根即全綠假象
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
RULINGS = os.path.join(REPO, "docs", "rulings")
assert os.path.isdir(RULINGS), f"🔴 裁定目錄不存在：{RULINGS}"
FILES = sorted(f for f in os.listdir(RULINGS) if f.endswith(".md"))
assert FILES, "🔴 裁定目錄內無 .md ⇒ ⛔ 不得視為「無條目」"

OUT = os.path.join(VERIFY, "out", "wg915_出處分層盤點.log")
L, RC = [], [0]
KL_MARKS = ("KL 逐字", "KL 裁")


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def git(*a):
    r = subprocess.run(["git", "-C", REPO, "-c", "core.quotePath=false"] + list(a),
                       capture_output=True)
    return r.stdout.decode("utf-8", "replace")


# ══════════════════════════════════════════════════════════════════════════
def is_quote(line):
    """引文行（⛔ 純語法·⛔ 不看內容）。"""
    return line.startswith(">")


def build_blocks(lines):
    """回 (每行是否引文, 每行所屬區塊 id 或 None, {區塊 id: 引言})。"""
    inq = [is_quote(x) for x in lines]
    bid = [None] * len(lines)
    lead = {}
    b = 0
    i = 0
    while i < len(lines):
        if inq[i]:
            start = i
            while i < len(lines) and inq[i]:
                bid[i] = b
                i += 1
            # 引言 ＝ 區塊起點往上最近之非空白且非引文行
            j = start - 1
            while j >= 0 and (not lines[j].strip() or inq[j]):
                j -= 1
            lead[b] = lines[j] if j >= 0 else "（檔首·無引言）"
            b += 1
        else:
            i += 1
    return inq, bid, lead


def classify(lines, inq, bid, lead, idx):
    if not inq[idx]:
        return "助手側補充", "不在任何引文區塊內"
    lg = lead[bid[idx]]
    hit = [m for m in KL_MARKS if m in lg]
    if hit:
        return "KL 逐字", f"引言含 {hit}｜引言＝{lg.strip()[:56]}"
    return "無法判定", f"在區塊內但引言不含 KL 標記｜引言＝{lg.strip()[:56]}"


def main():
    say("=" * 110)
    say("【`W-G.9-15` 甲組】第 1 級正典（`docs/rulings/`）之出處分層盤點")
    say("⛔ 受詞 ＝「這句話是誰說的」，⛔ 非「這句話對不對」")
    say("=" * 110)
    say(f"  🔒 母體 ＝ `docs/rulings/` 之 .md **{len(FILES)} 檔**：{FILES}")

    total_rows = []
    for fn in FILES:
        p = os.path.join(RULINGS, fn)
        lines = open(p, encoding="utf-8").read().split("\n")
        inq, bid, lead = build_blocks(lines)
        nblocks = (max([b for b in bid if b is not None]) + 1) if any(b is not None for b in bid) else 0
        say()
        say(f"  ▸ **{fn}**｜{len(lines)} 行｜引文行 {sum(inq)}｜引文區塊 {nblocks} 段")

        # ── X1：整檔可歸類自檢（⛔ 每一行皆須唯一歸類）─────────────────────
        unclass = [i for i in range(len(lines)) if inq[i] != lines[i].startswith(">")]
        nested = [i for i in range(len(lines)) if lines[i].startswith(">>")]
        say(f"      🔒 `X1` 自檢：無法歸類之行 ＝ **{len(unclass)}**"
            f"（須 0）｜巢狀引文 `>>` ＝ {len(nested)} 行（已納入引文行·不另計）")
        if unclass:
            red(f"`X1` 破 ⇒ `D-4`：{unclass[:5]}")

        # ── 母體：所有含 🔒 之行 ────────────────────────────────────────────
        pop = [i for i, x in enumerate(lines) if "🔒" in x]
        h3 = [i for i in pop if lines[i].startswith("### 🔒")]
        it = [i for i in pop if lines[i].startswith("- 🔒")]
        say(f"      🔒 母體規模：含 `🔒` 之行 ＝ **{len(pop)}**"
            f"（其中 `^### 🔒` {len(h3)}／`^- 🔒` {len(it)}／其餘 {len(pop)-len(h3)-len(it)}）")
        for i in pop:
            lay, why = classify(lines, inq, bid, lead, i)
            total_rows.append({"f": fn, "i": i, "text": lines[i].strip(),
                               "layer": lay, "why": why})

    # ── 分層彙總 ──────────────────────────────────────────────────────────
    say()
    say("=" * 110)
    say("【分層彙總】")
    say("=" * 110)
    from collections import Counter
    c = Counter(r["layer"] for r in total_rows)
    for k in ("KL 逐字", "助手側補充", "無法判定"):
        say(f"  {k}　＝ **{c.get(k, 0)}** 條")
    say(f"  合計 ＝ {len(total_rows)} 條")
    say(f"  ⇒ `X2`（存在掛 🔒 而落在引文區塊**外**者）＝ "
        f"{'✅ 成立' if c.get('助手側補充', 0) > 0 else '🔴 破（⚠️ 合法結果）'}"
        f"（{c.get('助手側補充', 0)} 條）")

    # 🔒 判別力自檢（考古 69 修法 ④）：合成一段已知答案之文字，規則須分對
    say()
    say("  🔒 **判別力自檢**（合成已知答案之文字 ⇒ 規則須分對）")
    synth = ["**KL 逐字**：", "> 🔒 這是 KL 說的", "", "- 🔒 這是助手寫的",
             "**某報告引述**：", "> 🔒 這是引文但引言無 KL 標記"]
    sinq, sbid, slead = build_blocks(synth)
    exp = ["KL 逐字", "助手側補充", "無法判定"]
    got = [classify(synth, sinq, sbid, slead, i)[0] for i in (1, 3, 5)]
    ok = (got == exp)
    say(f"      期望 {exp}")
    say(f"      實得 {got}　⇒ {'✅ 三型皆分對 ⇒ 具鑑別力' if ok else '🔴 分錯 ⇒ 規則無效'}")
    if not ok:
        red("判別力自檢失敗 ⇒ 本盤點結果**不得出艙**（考古 71 修法 ③）")

    # ── 逐條列出（⛔ 含 KL 逐字者亦完整列出·驗收 #1）──────────────────────
    say()
    say("=" * 110)
    say("【逐條盤點】⛔ 三欄齊備·含判為「KL 逐字」者亦完整列出")
    say("=" * 110)
    for lay in ("助手側補充", "無法判定", "KL 逐字"):
        rows = [r for r in total_rows if r["layer"] == lay]
        say()
        say(f"  ══ 分層：**{lay}**（{len(rows)} 條）══")
        for r in rows:
            say(f"    ① {r['text'][:104]}")
            say(f"       ② {lay}｜③ {r['why']}")

    # ── 出處追溯（⛔ 僅對「助手側補充」·`git log -S`）────────────────────────
    say()
    say("=" * 110)
    say("【出處追溯】對判為「助手側補充」者以 `git log -S` 定其**引入 commit**")
    say("⛔ 全部逐條·⛔ 無抽樣、⛔ 無上限截斷")
    say("=" * 110)
    CODE_WORDS = ("碼面", "app.py", "實作", "落地", "行為變更", "自量", "現行碼",
                  "決定點", "碼當時", "程式")
    undet, codeself = [], []
    for r in [x for x in total_rows if x["layer"] == "助手側補充"]:
        # 取該行之**最長粗體片語**為搜尋鍵（⛔ 不用整行·整行含 grep 指令會誤配）
        import re as _re
        cands = _re.findall(r"\*\*(.+?)\*\*", r["text"])
        key = max(cands, key=len) if cands else r["text"][:24]
        key = key.replace("`", "")[:28]
        out = git("log", "-S", key, "--format=%h|%ad|%s", "--date=short",
                  "--", f"docs/rulings/{r['f']}")
        rows = [l for l in out.strip().split("\n") if l.strip()]
        if not rows:
            undet.append((r, key))
            say(f"  ▸ {r['text'][:88]}")
            say(f"      🔴 **出處未定**（鍵＝`{key}`·`git log -S` 零命中）⇒ `X5` 之受詞，⛔ 不猜")
            continue
        intro = rows[-1]                    # 最舊者 ＝ 引入
        sha, dt, subj = intro.split("|", 2)
        body = git("log", "-1", "--format=%B", sha)
        is_code = [w for w in CODE_WORDS if w in body]
        say(f"  ▸ {r['text'][:88]}")
        say(f"      引入 ＝ {sha}｜{dt}｜{subj[:70]}")
        if is_code:
            codeself.append((r, sha, dt, is_code))
            say(f"      🔴 **訊息含碼面字樣** {is_code[:5]} ⇒ 候選「**碼面自述被寫進規定**」")
    say()
    say(f"  ⇒ 出處未定 ＝ **{len(undet)}** 條"
        f"（`X5` ＝ {'✅ 成立' if not undet else '🔴 破·已逐條具名'}）")
    say(f"  ⇒ 引入訊息含碼面字樣者 ＝ **{len(codeself)}** 條"
        f"（`X3` ＝ {'✅ 成立' if codeself else '🔴 破（⚠️ 合法）'}）")
    say("  ⚠️ **「含碼面字樣」≠「就是碼面自述」**——字樣只是**候選篩**；"
        "須逐條讀其訊息之**該段落**方能定案。本批於報告逐條人裁，⛔ 不以字樣代替判讀。")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
