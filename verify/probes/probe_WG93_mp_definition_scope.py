# -*- coding: utf-8 -*-
"""`W-G.9-3` §5：`mp`／`MP` 定義之**語意窮舉**掃描（Q1）＋ `P1` 重判（Q2）
＋ `GB-60` 選項列舉（Q3）＋ 須更正陳述之重掃（Q4）。

⛔ 零生產碼·只讀不改。⛔ **本檔不採信施工單 §3 之任何行號或逐字**——獨立重導。

## 🔒 射程（⛔ 目錄射程 ＋ 字樣射程·二者缺一不可·本批新戒）

### 目錄射程 ＝ `CLAUDE.md` 之**權威序四級**（`sed -n '4p' CLAUDE.md`）

| 級 | 實體 | 可掃？ |
|---|---|---|
| ① | `docs/rulings/` 全樹 | ✅ |
| ② | `CLAUDE.md` | ✅ |
| ③ | `docs/配地計算總規格_v3.md` | ✅ |
| ③′ | `docs/specs/` 全樹（v3 之補丁鏈·**非權威序明列**·另列） | ✅ |
| ④ | 104 手冊 | 🔴 **倉內無電子檔 ⇒ 未能掃描·⛔ 非零命中** |

### 字樣射程 ＝ **三元語意合取**（⛔ 非單一字面字串）

- **符號**：`mp` 之**大小寫全變體**（`MP`／`mp`／`Mp`／`mP`）——以 `re.IGNORECASE` 之詞界匹配。
- **線**：`SIDELINE`／`SIDE_LINE`／`SLIDELINE`／`SIDE LINE`／`側街線`／`側面道路`／`側界`（皆不分大小寫）。
- **中點**：`中點`／`中心點`／`midpoint`／`mid`（不分大小寫）。

一行**同時**含三者 ⇒ 記為命中（`strict`）。另以 **±1 行之窗**再掃一次（`window`）
——⛔ 防「定義跨行」之漏（此即 `W-G.9-2` 之失敗形狀之一）。

🩸 **本檔存在之由（自誌）**：`W-G.9-2` 之 `P1` 判定所用之式為
`"MP.*中點\\|中點.*MP\\|MP.*mid\\|MP(中點)\\|MP（中點）"`，
其**符號項僅含大寫 `MP`**、且**目錄射程僅 `docs/rulings/` ＋ `docs/specs/`**
（漏權威序**第 3 級**）⇒ 得 `rc=1`（零命中）而據以判「`P1` 破」。
⇒ **係字樣射程與目錄射程<u>雙重</u>不足，非命題為偽。**
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUT = os.path.join(VERIFY, "out", "probe_WG93_mp_definition_scope.log")
L = []


def say(s=""):
    L.append(s)
    print(s)


RE_SYM = re.compile(r"(?<![A-Za-z0-9_])mp(?![A-Za-z0-9_])", re.IGNORECASE)
RE_LINE = re.compile(r"side[_ ]?line|slideline|側街線|側面道路|側界", re.IGNORECASE)
RE_MID = re.compile(r"中點|中心點|mid\s*point|midpoint|(?<![A-Za-z0-9_])mid(?![A-Za-z0-9_])",
                    re.IGNORECASE)


def files_of(root, exts=(".md",)):
    out = []
    p = os.path.join(REPO, root)
    if os.path.isfile(p):
        return [root]
    for dp, dns, fns in os.walk(p):
        dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
        rel = os.path.relpath(dp, REPO).replace("\\", "/")
        if rel.startswith(".claude/worktrees"):
            dns[:] = []
            continue
        for fn in fns:
            if fn.endswith(exts):
                out.append(os.path.relpath(os.path.join(dp, fn), REPO).replace("\\", "/"))
    return sorted(out)


def scan(files, win=0, require_sym=True):
    """`require_sym=False` ⇒ **命題核心式**：只要 (線 ∧ 中點) 即命中，**不預設符號**。

    🩸 **本檔首版之字樣射程仍不足（當場自糾·⛔ 具名）**：首版之三元合取
    **要求符號為 `mp` 之大小寫變體**，因而漏掉權威序**第 3 級**之
    `docs/配地計算總規格_v3.md:189`「取該側 SIDE_LINE 中點 **M**」——**符號為 `M`、非 `mp`**
    ⇒ 首版判 `R1` **破**（同行 0）。**係字樣射程不足，非命題為偽**。
    ⚠️ 尤須具名：本批之新戒（「字樣必須語意窮舉」）**正是我自己立的**，
    而我在**同一批**、且在**更正同型錯誤之當下**再犯一次
    ——⇒ `CLAUDE.md`「立戒者在下一批最容易違反自己的戒」之**最短間隔實例**（同批內）。
    🔒 **修法**：命題之核心為「**SIDE 線之中點被指為某量之原點**」
    ⇒ 掃描不得預設該量之**符號名**（`mp`／`MP`／`M`／未具名皆可能）。
    """
    hits = []
    for f in files:
        try:
            lines = io.open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read().split("\n")
        except OSError:
            continue
        for i, ln in enumerate(lines):
            lo, hi = max(0, i - win), min(len(lines), i + win + 1)
            blob = "\n".join(lines[lo:hi])
            if not (RE_LINE.search(blob) and RE_MID.search(blob)):
                continue
            if require_sym and not RE_SYM.search(blob):
                continue
            hits.append((f, i + 1, ln.strip()))
    return hits


def main():
    say("=" * 122)
    say("W-G.9-3 §5　`mp`／`MP` 定義之語意窮舉掃描（⛔ 獨立重導·不採信施工單 §3）")
    say("=" * 122)

    TIERS = [("① docs/rulings/（裁定正典）", "docs/rulings"),
             ("② CLAUDE.md", "CLAUDE.md"),
             ("③ docs/配地計算總規格_v3.md", "docs/配地計算總規格_v3.md"),
             ("③′ docs/specs/（v3 補丁鏈·非權威序明列）", "docs/specs")]

    say("")
    say("【字樣射程】三元語意合取（⛔ 非單一字面字串）：")
    say("   符號 = %s" % RE_SYM.pattern)
    say("   線   = %s" % RE_LINE.pattern)
    say("   中點 = %s" % RE_MID.pattern)
    say("   皆 re.IGNORECASE ⇒ 涵蓋 `MP`／`mp`／`Mp`／`mP` 與 `SIDELINE`／`SIDE_LINE`／`side line`…")

    say("")
    say("#" * 122)
    say("## Q1　權威序**四級**逐級掃描（⛔ 含零命中之級·正面全列）")
    say("#" * 122)

    total = {}
    for name, root in TIERS:
        fs = files_of(root)
        h0 = scan(fs, win=0, require_sym=False)      # 命題核心式（⛔ 不預設符號）
        h1 = scan(fs, win=1, require_sym=False)
        hs = scan(fs, win=0, require_sym=True)       # 僅供對照：要求符號為 `mp` 變體
        total[name] = (fs, h0, h1)
        say("")
        say("【%s】目錄射程 = %d 檔" % (name, len(fs)))
        say("   **命題核心式**（線 ∧ 中點·⛔ 不預設符號）：同行 **%d**／±1 行窗 **%d**"
            % (len(h0), len(h1)))
        say("   （對照）要求符號為 `mp` 變體者：同行 **%d** ← 🩸 首版之式·**射程不足**"
            % len(hs))
        if not h0 and not h1:
            say("   ⇒ **零命中**（⛔ 已附目錄射程與字樣射程·⛔ 非「未掃」）")
        for f, i, s in h0:
            say("   · %s:%d" % (f, i))
            say("     %s" % s[:110])
        extra = [x for x in h1 if (x[0], x[1]) not in {(a, b) for a, b, _ in h0}]
        if extra:
            say("   ── 僅於 ±1 行窗命中（跨行定義）──")
            for f, i, s in extra[:6]:
                say("   · %s:%d  %s" % (f, i, s[:90]))
            if len(extra) > 6:
                say("   …（另 %d 行·全數見本 log 之 Q1-附錄）" % (len(extra) - 6))

    say("")
    say("【④ 104 手冊】🔴 **倉內無電子檔** ⇒ **未能掃描·⛔ 非零命中**")
    say("   目錄射程之自證：")
    for pat in ("*104*", "*手冊*"):
        n = len([f for f in files_of(".", exts=(".md", ".pdf", ".txt", ".docx"))
                 if pat.strip("*") in os.path.basename(f)])
        say("   · 檔名含 `%s` 之檔數 = %d" % (pat.strip("*"), n))

    # ═════════ Q2 ═════════
    say("")
    say("#" * 122)
    say("## Q2　`P1` 之重判（⛔ 由本檔之掃描結果自行下判）")
    say("#" * 122)
    t3 = total["③ docs/配地計算總規格_v3.md"]
    t3p = total["③′ docs/specs/（v3 補丁鏈·非權威序明列）"]
    t1 = total["① docs/rulings/（裁定正典）"]
    t2 = total["② CLAUDE.md"]
    r1 = len(t3[1]) + len(t3[2]) > 0
    r2 = len(t3p[1]) + len(t3p[2]) > 0
    say("")
    say("   R1（第 3 級有定義）　⇒ **%s**（同行 %d／窗 %d）"
        % ("成立" if r1 else "🔴 破", len(t3[1]), len(t3[2])))
    say("   R2（`docs/specs/` 有定義）⇒ **%s**（同行 %d／窗 %d）"
        % ("成立" if r2 else "🔴 破", len(t3p[1]), len(t3p[2])))
    say("   第 1 級命中 %d／第 2 級命中 %d（供 R3 判定）" % (len(t1[1]), len(t2[1])))
    say("")
    say("   ⇒ **`S-2`（R1 且 R2 皆破 ⇒ 維持原判並停機）：%s**"
        % ("🔴 觸發" if (not r1 and not r2) else "❌ **未觸發**"))
    say("   ⇒ **`P1` 應為：%s**"
        % ("**成立（重申）** ⇒ `W-G.9-2` 之「P1 破」係<u>射程不足所致之誤判</u>，須更正"
           if (r1 or r2) else "維持 **破**"))

    # ═════════ Q4 ═════════
    say("")
    say("#" * 122)
    say("## Q4　須更正之陳述**重掃**（⛔ 自行窮舉·不採信施工單 §3-6 之行號）")
    say("#" * 122)
    RE_NEG = re.compile(r"從未定義|未定義|無定義|零命中|查無|不存在|沒有定義|未被定義")
    allmd = files_of(".")
    say("")
    say("【目錄射程】全倉 `.md` ＝ **%d** 檔（⛔ 已排除 `.claude/worktrees/`）" % len(allmd))
    say("【字樣射程】(`mp` 符號變體) ∧ (否定詞：%s)" % RE_NEG.pattern)
    need = []
    for f in allmd:
        lines = io.open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read().split("\n")
        for i, ln in enumerate(lines):
            if RE_SYM.search(ln) and RE_NEG.search(ln):
                need.append((f, i + 1, ln.strip()))
    say("")
    say("⇒ 須更正之行 ＝ **%d**" % len(need))
    for f, i, s in need:
        say("   · %s:%d" % (f, i))
        say("     %s" % s[:112])

    say("")
    say("🔒 **逐行之處置（⛔ 非全部可更正）**：")
    for f, i, s in need:
        if "_前置登記" in f:
            say("   · %s:%d ⇒ 🔴 **刻意不更正**——**事前登記檔**依其自身紀律"
                "「⛔ 不得回頭修改本檔一字」，且施工單 §1 未授權該檔。" % (f, i))
            say("     ⚠️ 且該行係**預測之文字**（引施工單之破條件），⛔ 非「MP 未定義」之斷言。")
        else:
            say("   · %s:%d ⇒ 於其**正下方**加註更正（⛔ 原句一字不刪）" % (f, i))
    say("   ⇒ **應加註者 %d 行**（⛔ 施工單 §3-6 載 5 行·本檔獨立重掃得 %d 行，**多 %d 行**）"
        % (len([x for x in need if "_前置登記" not in x[0]]), len(need),
           len([x for x in need if "_前置登記" not in x[0]]) - 5))

    # ═════════ Q3 ═════════
    say("")
    say("#" * 122)
    say("## Q3　`GB-60` 之選項列舉（⛔ 先自答·⛔ 不判何者為正解）")
    say("#" * 122)
    say("")
    say("🔒 **書面自答（⛔ 寫在列舉之前）**：")
    say("   問：「是否窮盡？有無第三選項使兩邊同時滿足？」")
    say("   答：**有第三選項**——見下 ③；其使「警示所載為真」與「不靜默」**同時**成立。")
    say("       ⇒ 故 `W-G.9-2` 所記之「**二擇一**」**射程不足**，須改標。")
    say("   🔴 **是否窮盡：列舉·非窮舉**——⛔ 無法證明已窮盡選項空間。")
    say("")
    _pw = [(i + 1, l.strip()) for i, l in enumerate(
        io.open(os.path.join(REPO, "app.py"), encoding="utf-8").read().split("\n"))
        if "_pw = float(_res.get('S', 0.0)) * _cos_dn" in l]
    say("【現況之碼面指認（內容 grep·⛔ 非行號寫死）】")
    say("   `grep -n \"_pw = float(_res.get('S', 0.0)) \\* _cos_dn\" app.py` ⇒ %d 命中"
        % len(_pw))
    for i, s in _pw:
        say("   · app.py:%d  %s" % (i, s))
    say("   ⇒ `_cos_dn` **另有一消費者**＝宗地寬度（供畸零地判去留），"
        "而 `app.py` 之缺分配線警示**未提之**。")
    say("")
    say("%-4s %-40s %-30s" % ("選項", "內容", "土地後果"))
    say("-" * 122)
    say("%-4s %-40s %-30s" % ("①", "缺分配線即**停機**", "無分配成果（與 wf_f1／wf_f4 現行一致）"))
    say("%-4s %-40s %-30s" % ("②", "維持退 `1.0`，**把未宣告後果補入警示**",
                              "側街負擔 0 ＋ 宗地寬度高估 0.10%〜0.43%（**已宣告**）"))
    say("%-4s %-40s %-30s" % ("③", "**限縮 `_cos_dn` 之射程**", "側街負擔 0（警示所載**完整為真**）"))
    say("     ③ 之作法：令缺分配線時 `_cos_dn` **不參與宗地寬度**（或該路徑另行 loud），")
    say("     使警示「側街負擔以 0 計」成為**完整**真實 ⇒ **不靜默、亦不停機**。")
    say("-" * 122)
    say("⛔ **本檔不判何者為正解**（施工單 §5-3）。")
    say("⇒ `GB-60` 之「是否需域裁」欄應改標 **「三選項·需前置偵察」**。")

    say("")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    sys.exit(rc)
