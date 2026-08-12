# -*- coding: utf-8 -*-
r"""`W-G.9-17` `B1`：`K-8 §三`／`§四` 是否落在「KL 逐字」引文區塊內。

## 為何要問

KL 之裁定四〜六**自陳為「變更自己 2026-07-31 之裁示」**。
⇒ 入倉之**性質**（「變更自己的裁示」vs「移除從未經裁示之敘述」）**取決於本題**。
⛔ 判錯即在第 1 級正典（權威序**第 1 級**）寫下錯誤之性質敘述。

## 判法（⛔ 重用 `W-G.9-15` 之機械規則·⛔ 不另寫一份）

規則於 `verify/tools/wg915_ruling_provenance.py`（事前登記於量測前寫定）：
引文行＝`^>`／區塊＝極大連續段／引言＝區塊起點往上最近之非空白非引文行／
在區塊內且引言含 `KL 逐字`／`KL 裁` ⇒ **KL 逐字**。

🔒 **母體釘在明確 commit**（驗收 #9）⇒ `git show <sha>:<path>`，⛔ 不用工作樹現況。
🔒 **判別力自檢**：同一規則須於全檔判出**非 0** 條「KL 逐字」，否則它是恆 0 之空規則。

## 重跑
    python verify/probes/probe_WG917_B1.py [<commit-sha>]
"""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"

SHA = sys.argv[1] if len(sys.argv) > 1 else "053705f"      # ＝ W-G.9-17 commit A
RULE = os.path.join(VERIFY, "tools", "wg915_ruling_provenance.py")
assert os.path.exists(RULE), f"🔴 規則檔不存在：{RULE}"
PATH = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
OUT = os.path.join(VERIFY, "out", "probe_WG917_B1.log")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def main():
    # 🔒 重用同一份規則（⛔ 不另寫）
    src = open(RULE, encoding="utf-8").read().split("def main(")[0]
    ns = {"__file__": RULE, "__name__": "wg915rule"}
    exec(compile(src, RULE, "exec"), ns)

    raw = subprocess.run(["git", "-C", REPO, "show", f"{SHA}:{PATH}"],
                         capture_output=True).stdout.decode("utf-8")
    assert raw.strip(), f"🔴 母體為空（sha={SHA}）⇒ ⛔ 不得視為「無 KL 逐字」"
    lines = raw.split("\n")
    inq, bid, lead = ns["build_blocks"](lines)

    say("=" * 104)
    say("【`W-G.9-17` `B1`】`§三`／`§四` 是否落在「KL 逐字」引文區塊內")
    say("=" * 104)
    say(f"  🔒 母體釘於 commit **{SHA}**｜`{PATH}`｜{len(lines)} 行"
        f"（⛔ 非工作樹現況·驗收 #9）")
    say(f"  🔒 規則來源 ＝ `verify/tools/wg915_ruling_provenance.py`（⛔ 未另寫一份）")

    hits = [(i, lines[i]) for i in range(len(lines))
            if lines[i].startswith("### §三") or lines[i].startswith("### §四")]
    say(f"  🔒 母體自證：`^### §三`／`^### §四` 命中 **{len(hits)}** 節")
    ok = True
    for i, head in hits:
        j = i + 1
        while j < len(lines) and not lines[j].startswith("### "):
            j += 1
        seg = list(range(i, j))
        nq = sum(1 for x in seg if inq[x])
        nkl = sum(1 for x in seg if inq[x]
                  and any(m in lead[bid[x]] for m in ns["KL_MARKS"]))
        say()
        say(f"  ══ {head.strip()} ══（行 {i+1}〜{j}·{len(seg)} 行）")
        say(f"      引文行 ＝ **{nq}**｜落在 **KL 逐字** 區塊內之行 ＝ **{nkl}**")
        for x in seg:
            say(f"        {x+1} [{'>' if inq[x] else ' '}] {lines[x][:80]}")
        lay, why = ns["classify"](lines, inq, bid, lead, i)
        say(f"      ⇒ **{lay}**｜{why}")
        if nkl > 0:
            say("      ⇒ ✅ 本節有 KL 逐字之行")
        else:
            say("      ⇒ 🔴 **本節<u>無任何</u>行落在 KL 逐字區塊內**")
            ok = False

    # 🔒 判別力自檢（⛔ 兩端至少一端來自受詞之外·考古 76）
    say()
    kl_all = [i for i in range(len(lines)) if inq[i]
              and any(m in lead[bid[i]] for m in ns["KL_MARKS"])]
    say(f"  🔒 **判別力自檢**：同一規則於**全檔**判為「KL 逐字」之行 ＝ **{len(kl_all)}**"
        f" ⇒ {'✅ 非恆 0（規則具鑑別力）' if kl_all else '🔴 恆 0 ⇒ 規則無效、結果不得出艙'}")
    for i in kl_all[:4]:
        say(f"      {i+1} | {lines[i][:76]}")
    if not kl_all:
        RC[0] = 1

    say()
    say("=" * 104)
    say(f"【判定】`B1`（`§三`／`§四` 皆在 KL 逐字區塊內）＝ "
        f"{'✅ 成立' if ok else '🔴 **破** ⇒ `G-4` 停機上呈'}")
    say("=" * 104)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
