# -*- coding: utf-8 -*-
"""`W-G.9-6` `Q2`：**對帳準則之鑑別力**（洞 B）。

## 受測之準則有**獨立出處**（⛔ 非 CC 自撰之稻草人）

倉內**無任何可執行碼**讀取期望 FAIL 名單（`W-G.9-6_前置登記.md` §0-2 之五式窮舉）
⇒ 對帳為**人工程序**。其定義取**正典·權威序第 2 級**（`CLAUDE.md:71-72`·逐字）：

> ⇒ 期間之驗收改為 **「與凍存之期望 FAIL 名單逐項相同」**，⛔ **非「全綠」**。
> 凍存名單：`verify/out/K6A2_期望FAIL名單_902f5d1.txt`（**逐項名目**·⛔ 非計數）。

⇒ 本檔只把該條文**程式化**；其**語義出處獨立於本碼**（`fixture-provenance`）。

⚠️ **具名不一致（登記 §0-4）**：正典指名 `902f5d1`（46 名目），現行實務用
`D2b1切換後`（22 名目）。本檔**兩份都跑**，⛔ 不代 KL 選一份。

## 四項試驗

| # | 內容 | 資料性質 |
|---|---|---|
| **A** | `D2b1_runall.log`（入單時）vs `WG94b_runall.log`（現況）**皆對帳** | 🔴 **真實資料**·⛔ 非合成 |
| **B** | 取現況 log，**只改某期望 FAIL 項之訊息**、名目不動 | 合成（施工單 §2-2 指定） |
| **C** | 取現況 log，**只改名目** | 合成·**反向自檢**（無鑑別力 ⇒ `T-2` 停機） |
| **D** | 22 名目**逐項**：入單時 vs 現況之**訊息是否改變** | 🔴 真實資料（供 `Q3` ② 與 `T-3`） |

⛔ **不改動 `verify/out/` 之任何真實檔**（合成僅存於記憶體）。
⛔ 不改名單、⛔ 不改 `run_verification.py`。

## 重跑
    python verify/probes/probe_WG96_reconcile.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUT = os.path.join(VERIFY, "out", "probe_WG96_reconcile.log")

LIST_CANON = os.path.join(VERIFY, "out", "K6A2_期望FAIL名單_902f5d1.txt")
LIST_INUSE = os.path.join(VERIFY, "out", "K6A2_期望FAIL名單_D2b1切換後.txt")
LOG_AT_LISTING = os.path.join(VERIFY, "out", "D2b1_runall.log")
LOG_NOW = os.path.join(VERIFY, "out", "WG94b_runall.log")

FAIL_RE = re.compile(r"^\s*🔴 FAIL\s\s(.*?)\s*$")
JUDGE_RE = re.compile(r"^\s*(✅ PASS|🔴 FAIL)\s\s")
L = []
RC = [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


# ── 準則之程式化（⛔ 語義出處＝CLAUDE.md:71-72）────────────────────────────
def names_of_log(text):
    """log 之 FAIL **名目**序列（⛔ 不取訊息——這正是準則之界線所在）。"""
    return [m.group(1) for m in (FAIL_RE.match(x) for x in text.splitlines()) if m]


def names_of_list(text):
    return [m.group(1) for m in (FAIL_RE.match(x) for x in text.splitlines()) if m]


def reconcile(log_text, list_text):
    """正典準則：**逐項名目相同**（⛔ 非計數、⛔ 不看訊息）。回 (符合?, 差異敘述)。"""
    a, b = names_of_log(log_text), names_of_list(list_text)
    if a == b:
        return True, "逐項名目相同"
    only_log = [x for x in a if x not in b]
    only_lst = [x for x in b if x not in a]
    if not only_log and not only_lst:
        return False, "名目集合相同但**順序**不同"
    return False, f"log 獨有={only_log}；名單獨有={only_lst}"


def blocks_of_log(text):
    """{名目: [其後之明細行]}——⛔ 僅供 `D` 試驗，**不入對帳準則**。"""
    out, cur = {}, None
    for ln in text.splitlines():
        m = FAIL_RE.match(ln)
        if m:
            cur = m.group(1)
            out.setdefault(cur, [])
            continue
        if JUDGE_RE.match(ln):
            cur = None
            continue
        if cur is not None and ln.strip():
            out[cur].append(ln.strip())
    return out


def read(p):
    return open(p, encoding="utf-8").read()


def norm_detail(s):
    """去除**與版本無關**之環境噪音，⛔ 不觸任何數值。

    🔒 **為何必須**：兩 log 產於**不同 worktree**，明細行中之 traceback 含絕對路徑
    ⇒ 未正規化直接比對會把**純路徑差**誤報為「失敗原因改變」（本探針首版即報 12 項，
    正規化後實為 4 項——`W-G.9-4b` 之 `E4` 同型教訓）。
    ⚠️ traceback **行號**亦一併正規化，惟本案 8 項純路徑差者其行號**本即相同**
    （已實測）⇒ 該步未遮蔽任何真差異。
    """
    s = s.replace("\\", "/")
    s = re.sub(r'[A-Za-z]:/[^\s"\']*?/(?=verify/|app\.py)', '', s)
    s = re.sub(r'(\w+\.py)", line \d+', r'\1", line <行號>', s)
    return s


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    say("=" * 100)
    say("# `W-G.9-6` `Q2` 探針：對帳準則之鑑別力（洞 B）")
    say("  準則出處＝**正典·權威序第 2 級**（`CLAUDE.md:71-72`）：逐項**名目**相同·⛔ 非計數")
    say("=" * 100)

    t_now, t_then = read(LOG_NOW), read(LOG_AT_LISTING)
    l_inuse, l_canon = read(LIST_INUSE), read(LIST_CANON)
    say(f"  現況 log      ＝ {os.path.relpath(LOG_NOW, REPO)}（FAIL 名目 {len(names_of_log(t_now))}）")
    say(f"  入單時 log    ＝ {os.path.relpath(LOG_AT_LISTING, REPO)}（FAIL 名目 {len(names_of_log(t_then))}）")
    say(f"  實務用名單    ＝ {os.path.relpath(LIST_INUSE, REPO)}（{len(names_of_list(l_inuse))} 名目）")
    say(f"  正典指名名單  ＝ {os.path.relpath(LIST_CANON, REPO)}（{len(names_of_list(l_canon))} 名目）")

    # ── A：真實資料·二 log 皆對帳（⛔ 非合成）────────────────────────────
    say()
    say("─" * 100)
    say("【A】真實資料：入單時 log 與現況 log **皆**對帳（對實務用名單）")
    say("─" * 100)
    okA1, whyA1 = reconcile(t_then, l_inuse)
    okA2, whyA2 = reconcile(t_now, l_inuse)
    say(f"  入單時 log vs 名單 ⇒ {'✅ 符合' if okA1 else '🔴 不符'}（{whyA1}）")
    say(f"  現況   log vs 名單 ⇒ {'✅ 符合' if okA2 else '🔴 不符'}（{whyA2}）")
    say(f"  對正典指名之 `902f5d1` 名單：現況 log ⇒ "
        f"{'✅ 符合' if reconcile(t_now, l_canon)[0] else '🔴 不符'}"
        f"　⚠️ 二名單不同檔（登記 §0-4）·⛔ 本批不代裁")

    # ── D：逐項訊息是否改變（真實資料·供 T-3）────────────────────────────
    say()
    say("─" * 100)
    say("【D】22 名目**逐項**：入單時 vs 現況之**訊息**是否改變（🔴 真實資料）")
    say("─" * 100)
    b_then, b_now = blocks_of_log(t_then), blocks_of_log(t_now)
    say("  🔒 判準：**正規化後**（去絕對路徑／traceback 行號·見 `norm_detail`）仍相異者"
        "才記為「已變」")
    say("     ⛔ 未正規化之數**不得出艙**——兩 log 產於不同 worktree")
    changed, same, absent, raw_chg = [], [], [], 0
    say(f"  {'名目':<44}{'raw':>5}{'正規化':>7}  判")
    say("  " + "-" * 66)
    for nm in names_of_list(l_inuse):
        d1, d2 = b_then.get(nm), b_now.get(nm)
        if d1 is None or d2 is None:
            absent.append(nm)
            mark, r, n = "⚠️ 一方缺", "-", "-"
        else:
            r_diff = (d1 != d2)
            n_diff = ([norm_detail(x) for x in d1] != [norm_detail(x) for x in d2])
            raw_chg += int(r_diff)
            r, n = ("異" if r_diff else "同"), ("異" if n_diff else "同")
            if n_diff:
                changed.append(nm)
                mark = "🔴 **原因已變**"
            else:
                same.append(nm)
                mark = "＝ 未變" + ("（raw 異＝純路徑差）" if r_diff else "")
        say(f"  {nm[:42]:<44}{r:>5}{n:>7}  {mark}")
    say("  " + "-" * 66)
    say(f"  未正規化「異」＝ {raw_chg} 項　→　**正規化後真正原因已變 ＝ {len(changed)} 項**"
        f"（未變 {len(same)}／一方缺 {len(absent)}）")
    for nm in changed:
        say(f"     🔴 {nm}")
    say(f"  ⇒ 對帳結果（只比名目）：**{'符合' if okA2 else '不符'}** —— "
        f"⛔ 與上列「原因已變 {len(changed)} 項」**無關**")
    if changed:
        say(f"  ⇒ 🛑 **`T-3` 觸發**：{len(changed)} 項之當前失敗原因 ≠ 入單時之原因，"
            "而對帳仍為綠 ⇒ **洞 B 已實際發生**")

    # ── B：合成竄改訊息（施工單 §2-2 指定）───────────────────────────────
    say()
    say("─" * 100)
    say("【B】合成：只改**訊息**、名目不動 ⇒ 對帳是否改變")
    say("─" * 100)
    victim_line = None
    for ln in t_now.splitlines():
        if ln.strip().startswith("[StepG0m]"):
            victim_line = ln
            break
    if victim_line is None:
        red("找不到可竄改之明細行 ⇒ 本試驗無受詞（⛔ 空不算通過）")
    else:
        t_tamper = t_now.replace(
            victim_line, "        [StepG0m] 🔴 合成竄改：完全不同之失敗原因（W-G.9-6 試驗 B）")
        okB, whyB = reconcile(t_tamper, l_inuse)
        say(f"  受詞明細行 ＝ {victim_line.strip()[:88]}…")
        say(f"  竄改後對帳 ⇒ {'✅ 符合（＝**未察覺**）' if okB else '🔴 不符（＝已察覺）'}（{whyB}）")
        if okB:
            say("  ⇒ **`G2` 成立**：改失敗原因、不改名目 ⇒ 對帳準則**看不見**")
        else:
            say("  ⇒ **`G2` 破**——須查是何機制察覺的")

    # ── C：反向自檢（改名目 ⇒ 須轉紅）────────────────────────────────────
    say()
    say("─" * 100)
    say("【C】反向自檢：只改**名目** ⇒ 對帳須轉紅（否則本探針無鑑別力 ⇒ `T-2`）")
    say("─" * 100)
    nm0 = names_of_list(l_inuse)[0]
    t_rev = t_now.replace(f"🔴 FAIL  {nm0}", f"🔴 FAIL  {nm0}·合成改名", 1)
    okC, whyC = reconcile(t_rev, l_inuse)
    say(f"  受詞名目 ＝ `{nm0}` → `{nm0}·合成改名`")
    say(f"  改名後對帳 ⇒ {'🔴 仍符合' if okC else '✅ 不符（已察覺）'}（{whyC}）")
    if okC:
        red("反向自檢**無鑑別力** ⇒ `T-2` 停機，本探針不得計入交付")
    else:
        say("  ⇒ ✅ 反向自檢具鑑別力（改名目必被察覺 ∧ 改訊息不被察覺）")

    say()
    say("=" * 100)
    say(f"{'✅ 探針 PASS' if RC[0] == 0 else '🔴 探針 FAIL'}（rc={RC[0]}）")
    say("=" * 100)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
