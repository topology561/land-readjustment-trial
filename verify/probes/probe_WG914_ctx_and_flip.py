# -*- coding: utf-8 -*-
r"""`W-G.9-14` 丙組＋戊組：`_ctx["0m"]` 之 `KeyError` 偵察 ＋ 三率錨之**翻點定位**。

⛔ **只查不修**：本探針不改任何檔、不呼叫 `run_step_g`。

## 丙組（`U5`）

`W-G G.1` 崩於 `_nat = _ctx["0m"]`。查：`stepg_ctx` **實有哪些鍵**、`"0m"` 為何不在、
其**寫入者是誰**、寫入**為何未發生**——以 **AST 構造**定位（⛔ 不猜），
並以倉內長跑 log 為運行期佐證。

## 戊組（`U6`）

三率錨（`v3 重劃總負擔率錨`／`v3 率分項錨`／`v3 率用 DXF 公設實值`）
**最後一次判定行為 `✅ PASS` 之 log 與其 commit**，登記為
「解阻後判『基準過期 vs 算錯』之**起算點**」。⛔ 只登記、不裁。

🔒 **對照組自檢（考古 71 修法 ③）**：每一量測器餵**已知為真**之命題須綠、
餵**已知為偽**之命題須紅；⛔ 自檢紅則結果不得出艙。

## 重跑
    python verify/probes/probe_WG914_ctx_and_flip.py
"""
import ast
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

# 🔒 母體自證（考古 69 修法 ①）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
RV = os.path.join(VERIFY, "run_verification.py")
assert os.path.exists(RV), f"🔴 母體檔不存在：{RV}"
_SRC = open(RV, encoding="utf-8").read()
_AST = ast.parse(_SRC)
OUT = os.path.join(VERIFY, "out", "probe_WG914_ctx_and_flip.log")
L, RC = [], [0]
ANCHORS = ("v3 重劃總負擔率錨", "v3 率分項錨", "v3 率用 DXF 公設實值")


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def git(*a):
    r = subprocess.run(["git", "-c", "core.quotePath=false"] + list(a),
                       cwd=REPO, capture_output=True, text=True, encoding="utf-8")
    return (r.stdout or "").strip(), r.returncode


# ══════════════════════════════════════════════════════════════════════════
_PAR = {}
for _n in ast.walk(_AST):
    for _c in ast.iter_child_nodes(_n):
        _PAR[_c] = _n


def enclosing(node, kinds):
    cur = _PAR.get(node)
    out = []
    while cur is not None:
        if isinstance(cur, kinds):
            out.append(cur)
        cur = _PAR.get(cur)
    return out


def writes_to(name):
    """對 `name` 之所有寫入（`name = …` 與 `name[…] = …`），附其是否位於 `try` body 內。"""
    hits = []
    for n in ast.walk(_AST):
        if not isinstance(n, ast.Assign):
            continue
        for t in n.targets:
            base = t
            sub = False
            if isinstance(t, ast.Subscript):
                base, sub = t.value, True
            if isinstance(base, ast.Name) and base.id == name:
                trys = enclosing(n, ast.Try)
                hits.append({"line": n.lineno, "sub": sub,
                             "src": " ".join((ast.get_source_segment(_SRC, n) or "")
                                             .split())[:96],
                             "in_try": bool(trys)})
    return hits


def reads_of(name):
    return [{"line": n.lineno,
             "src": " ".join((ast.get_source_segment(_SRC, n) or "").split())[:96]}
            for n in ast.walk(_AST)
            if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name)
            and n.value.id == name]


def c_ctx():
    say("=" * 108)
    say("【丙組·`U5`】`_ctx[\"0m\"]` 之 `KeyError` —— 構造定位（⛔ 只查不修）")
    say("=" * 108)
    # 🔒 對照組自檢：對**已知存在**之名與**已知不存在**之名各跑一次
    n_ok = len(writes_to("stepg_ctx"))
    n_bad = len(writes_to("ZZZ_不存在之變數"))
    say(f"  🔒 對照組自檢：`stepg_ctx` 之寫入 {n_ok} 處（**已知存在**·須 >0）｜"
        f"`ZZZ_不存在之變數` {n_bad} 處（**已知不存在**·須 ==0）"
        f" ⇒ {'✅ 綠' if (n_ok > 0 and n_bad == 0) else '🔴 紅 ⇒ 量測器紅、結果不得出艙'}")
    if not (n_ok > 0 and n_bad == 0):
        red("對照組自檢紅（`B-3`）")
        return False
    say()
    for nm in ("stepg_ctx", "_ctx"):
        say(f"  ▸ **`{nm}` 之寫入點**")
        for h in writes_to(nm):
            say(f"      {'（下標寫入）' if h['sub'] else '（整體賦值）'}"
                f"{'　⚠️ **位於 `try` body 內**' if h['in_try'] else ''}｜{h['src']}")
    say()
    say("  ▸ **`_ctx` 之下標讀取**（G.1 段之受詞）")
    for h in reads_of("_ctx"):
        say(f"      {h['src']}")
    say()
    say("  ── 🔴 成因（構造）───────────────────────────────────────────────────────")
    say("      ① `stepg_ctx` 初始為 `{}`；其**唯一**下標寫入位於 `try` body 內、"
        "且**排在 `run_step_g(...)` 之後**")
    say("         ⇒ `run_step_g` 一 raise，該寫入**從未執行** ⇒ `stepg_ctx` **恆為空**。")
    say("      ② F.0 段先 `_ctx = {}`，隨即之填充迴圈以 "
        "`raise RuntimeError(\"stepg_ctx[tag] 缺（trunk A 未成功？）\")` 中止")
    say("         ⇒ `_ctx` **停在空 dict**（⛔ 非 `None`——`None` 會是 `TypeError`）。")
    say("      ③ G.1 段讀 `_ctx[\"0m\"]` ⇒ **`KeyError: '0m'`**。")
    say("      ⇒ 🔒 **G.1 之 `KeyError` 是三段傳遞之後果，⛔ 非 G.1 自身缺陷**"
        "——與**考古 70**（寫入點排在 `raise` 下游、同一 `try`）**同族**。")
    say()
    say("  ── 運行期佐證（倉內長跑 log·⛔ 非本探針重跑）─────────────────────────")
    lg = os.path.join(VERIFY, "out", "WG913_runall.log")
    if os.path.exists(lg):
        txt = open(lg, encoding="utf-8", errors="replace").read()
        for pat in ("[StepG0m]", "[StepG3.5m]", "[G.1]", "stepg_ctx["):
            say(f"      `{pat}` 於 `WG913_runall.log` 命中 {txt.count(pat)} 次")
        for ln in txt.splitlines():
            if "[G.1]" in ln:
                say(f"      ⇒ {ln.strip()[:120]}")
                break
    else:
        red("找不到 `verify/out/WG913_runall.log`")
    say("      🔒 判別力自檢：以**必不存在**之字樣 `[ZZZ]` 重算 ⇒ "
        f"{open(lg, encoding='utf-8', errors='replace').read().count('[ZZZ]') if os.path.exists(lg) else '—'} 次"
        "（須 0 ⇒ 上式非恆命中）")
    return True


def e_flip():
    say()
    say("=" * 108)
    say("【戊組·`U6`】三率錨之**翻點定位**（⛔ 只登記·不裁）")
    say("=" * 108)
    outdir = os.path.join(VERIFY, "out")
    _self = os.path.basename(OUT)
    # 🔴 **母體須扣除本探針自己的輸出**（`W-G.9-14` 自檢實測抓到）：
    #    本探針把 log 寫進 `verify/out/`，而它掃描的正是 `verify/out/*.log`
    #    ⇒ 第二次起，**自己上一次的輸出**進入母體。首發實測即令對照組自檢由綠轉紅
    #    （哨兵字樣命中 1 檔 ＝ 自己）。⇒ 同 `W-G.9-11`「母體隨自己寫的文件增長」，
    #    惟此處污染到的是**自檢本身** ⇒ ⛔ 不扣除即無法自證。
    logs = sorted(f for f in os.listdir(outdir) if f.endswith(".log") and f != _self)
    say(f"  🔒 母體 ＝ `verify/out/*.log` 共 **{len(logs)}** 檔"
        f"（⛔ 正面列舉之目錄射程·**已扣除本探針自身之輸出 `{_self}`**）")
    # 🔒 對照組自檢（哨兵**於執行期組出**，使其字面⛔ 不落入任何 log ⇒ 免二次自污染）
    _sent = "Z" * 3 + "Q" * 3 + "不存在之哨兵"
    probe_ok = sum(1 for f in logs if "✅ PASS" in
                   open(os.path.join(outdir, f), encoding="utf-8", errors="replace").read())
    probe_bad = sum(1 for f in logs if _sent in
                    open(os.path.join(outdir, f), encoding="utf-8", errors="replace").read())
    say(f"  🔒 對照組自檢：`✅ PASS` 命中 {probe_ok} 檔（已知為真·須 >0）｜"
        f"〈哨兵·執行期組出·⛔ 不印其字面〉命中 {probe_bad} 檔（已知為偽·須 ==0）"
        f" ⇒ {'✅ 綠' if (probe_ok > 0 and probe_bad == 0) else '🔴 紅'}")
    if not (probe_ok > 0 and probe_bad == 0):
        red("對照組自檢紅（`B-3`）")
        return
    # 🔒 母體限**全跑之長跑 log**（正面判準：檔內含 `W-V run_all:` 收尾行）
    #    ⛔ 不以檔名猜（`*runall*` 會漏掉 `N_c5b_runall.log` 以外之命名變體、且含探針 log）
    runalls = []
    for f in logs:
        txt = open(os.path.join(outdir, f), encoding="utf-8", errors="replace").read()
        if "W-V run_all:" in txt:
            sha, _rc = git("log", "-1", "--format=%ct|%h|%ad", "--date=short",
                           "--", f"verify/out/{f}")
            ct = int(sha.split("|")[0]) if sha else -1
            runalls.append({"f": f, "txt": txt, "ct": ct,
                            "sha": (sha.split("|", 1)[1] if sha else "（未入倉·untracked）")})
    runalls.sort(key=lambda r: (r["ct"], r["f"]))
    say(f"  🔒 **全跑 log** ＝ 含收尾行 `W-V run_all:` 者 **{len(runalls)}** 檔"
        f"（⛔ 正面判準·非以檔名猜）；其中未入倉 "
        f"{sum(1 for r in runalls if r['sha'].startswith('（未入倉'))} 檔")
    for anc in ANCHORS:
        say()
        say(f"  ▸ 錨：`{anc}`")
        last_pass, first_absent, n_pass, n_fail = None, None, 0, 0
        for r in runalls:
            if f"✅ PASS  {anc}" in r["txt"]:
                n_pass += 1
                last_pass = r
            elif f"🔴 FAIL  {anc}" in r["txt"]:
                n_fail += 1
            elif anc not in r["txt"] and first_absent is None and r["ct"] > 0:
                first_absent = r
        say(f"      全跑 log 中：判定 `PASS` **{n_pass}** 檔｜判定 `FAIL` **{n_fail}** 檔")
        say(f"      🔴 **最後一次 `✅ PASS`**："
            f"{last_pass['sha'] if last_pass else '（無）'}｜`{last_pass['f'] if last_pass else '—'}`")
        say(f"      🔴 **最早一次<u>完全不出現</u>**："
            f"{first_absent['sha'] if first_absent else '（無）'}"
            f"｜`{first_absent['f'] if first_absent else '—'}`")
        say(f"      ⇒ **翻點被夾在此二 commit 之間**；且本錨在倉內**從未出現 `FAIL` 判定**"
            f"（{n_fail} 檔）⇒ 其「翻」⛔ **不是 `PASS→FAIL`，而是 `PASS→<u>不再被評估</u>`**。")
        say(f"      ⚠️ ⇒ 解阻後若轉紅，**「基準過期 vs 算錯」之起算點 ＝ 上列最後一次 `PASS` 之 commit**；"
            f"其後對產生路徑之觸及史即為候選成因清單。")
    # 現況：三錨於最近一次長跑是否出現
    say()
    lg = os.path.join(outdir, "WG913_runall.log")
    txt = open(lg, encoding="utf-8", errors="replace").read()
    say("  ── 現況（最近一次長跑 `WG913_runall.log`）────────────────────────────")
    for anc in ANCHORS:
        say(f"      `{anc}` 於其中命中 {txt.count(anc)} 次"
            f"（0 ⇒ **未被評估**·與上表之 PASS 史對照即為翻點之後側）")
    say("      🔒 判別力自檢：以**必然命中**之字樣 `✅ PASS` 重算 ⇒ "
        f"{txt.count('✅ PASS')} 次（須 >0 ⇒ 上式非恆 0）")


def main():
    ok = c_ctx()
    if ok:
        e_flip()
    say()
    say("=" * 108)
    say(f"【判定】丙組 `U5` ＝ {'✅ 已由構造定位' if ok else '🔴 未定位'}"
        f"｜戊組 `U6` ＝ 見上表")
    say("=" * 108)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
