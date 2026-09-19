# -*- coding: utf-8 -*-
"""`W-G.9-316` `§三`：**`W₀` 之消費者全定位**（🛑 **全唯讀**·AST ＋ 字樣錨·⛔ 驅動管線）。

🛑 **⛔ 判孰為正確、⛔ 提修法主張、⛔ 擬任何 diff、⛔ 稱任何處為「缺陷」**——**照實具名**。
🛑 **⛔ 匯入即驅動**：本器**不 import** `app_harvest`／`run_verification`／`stepg_pipeline`，
   亦**不執行**任何生產碼；其母體為**原始碼之文字與 AST**。
🛑 **⛔ 以推定代上溯**（單 `§三` 逐字）：上溯不可達者一律載為
   「**⛔ 可達·其止於 <逐字>**」，⛔ 以「應為」「推測」填之。

**出艙之受詞**（單 `§三` 之 `a`〜`f`）
   `a` `_tele_exp` 之賦值式逐字與其所在（**列框**·母體 ＝ `verify/stepg_pipeline.py` 單檔）
   `b` `_sd_W0` 之**產生鏈**（**AST `Assign`／`For`**·⛔ 文字層）
   `c` `rw_increment` 之**全部呼叫節點**及其實參（`ast.unparse`）＋ 包層函式
   `d` `_rw_start` 之決定式逐字 ＋ `W_cur = W_prev + S` 之 `W_prev` 執行緒初值
   `e` `rw_from_width` 之**全部呼叫節點** ＋ 包層 ＋ 實參
   `f` `_fo_left`／`_fo_right` 之賦值節點 ＋ 包層 ＋ 與 `b` 之 `W₀` 賦值節點**是否同框**

🔒 **判別力二造**（單 `§三` 逐字）
   `甲[必有命中]` `rw_increment` 之呼叫節點數須 `> 0`（`GB-168` 二次精化載
     `solve_G_binary` `1`／`iterate_G_S` `2`·本器自行重得並與之對拍）；
   `乙[必為零]` 一人造之函式名（**執行期組出**·字面⛔ 出艙·坑 `bd`）之呼叫節點數 ＝ `0`。
   **二造同色 ⇒ 器紅 `rc = 5` ⇒ ⛔ 出艙任何定位之數。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9316_w0_consumers.py [倉根]`
`rc`：`0`／`5` **器紅**（判別力二造未成立）。
"""
import ast
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))

W = 132
SP = "verify/stepg_pipeline.py"
APP = "app.py"
# 🔒 `GB-168` 二次精化所載之呼叫點分布（**外部錨**·⛔ 人造）
GB168_CALLS = {"solve_G_binary": 1, "iterate_G_S": 2}


def say(s=""):
    print(s)


def rd(rel):
    with open(os.path.join(REPO, rel), 'rb') as f:
        return f.read().decode('utf-8')


def py_files():
    """母體 ＝ `app.py` ＋ `verify/` 之全部 `*.py`（**正面列舉**·⛔ 全倉排除式）。"""
    out = [APP]
    base = os.path.join(REPO, "verify")
    for dp, _dn, fn in os.walk(base):
        for f in sorted(fn):
            if f.endswith(".py"):
                out.append(os.path.relpath(os.path.join(dp, f), REPO).replace("\\", "/"))
    return out


def parse(rel):
    try:
        return ast.parse(rd(rel), filename=rel)
    except Exception as e:                                       # noqa: BLE001
        return e


def enclosing(tree, node):
    """回傳含 `node` 之最內層 `FunctionDef` 之名（⛔ 有則回 `<module>`）。"""
    best = None
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if getattr(fn, "lineno", None) is None or getattr(fn, "end_lineno", None) is None:
            continue
        if fn.lineno <= node.lineno and node.end_lineno <= fn.end_lineno:
            if best is None or fn.lineno > best.lineno:
                best = fn
    return best.name if best else "<module>"


def call_name(c):
    f = c.func
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return None


def find_calls(name, files):
    """全部呼叫節點（**AST**·⛔ 文字層）。回 list of (rel, lineno, 包層, unparse)。"""
    out = []
    for rel in files:
        t = parse(rel)
        if isinstance(t, Exception):
            continue
        for n in ast.walk(t):
            if isinstance(n, ast.Call) and call_name(n) == name:
                out.append((rel, n.lineno, enclosing(t, n), ast.unparse(n)))
    return out


def find_assigns(name, rel):
    """對 `name` 之**綁定節點**（`Assign`／`AnnAssign`／`For` 之 target）。"""
    t = parse(rel)
    if isinstance(t, Exception):
        return []
    out = []
    for n in ast.walk(t):
        tgts = []
        if isinstance(n, ast.Assign):
            tgts = n.targets
        elif isinstance(n, ast.AnnAssign):
            tgts = [n.target]
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            tgts = [n.target]
        else:
            continue
        names = set()
        for tg in tgts:
            for sub in ast.walk(tg):
                if isinstance(sub, ast.Name):
                    names.add(sub.id)
        if name in names:
            if isinstance(n, (ast.For, ast.AsyncFor)):
                txt = "for %s in %s:" % (ast.unparse(n.target), ast.unparse(n.iter))
                kind = "For"
            else:
                txt = ast.unparse(n)
                kind = type(n).__name__
            out.append((rel, n.lineno, enclosing(t, n), kind, txt))
    return out


def lines_with(rel, needle):
    """**列框**：含 `needle` 之列（1-based）及其逐字。"""
    return [(i, l.rstrip()) for i, l in enumerate(rd(rel).split("\n"), 1) if needle in l]


def main():
    FILES = py_files()
    say("=" * W)
    say("【`W-G.9-316` `§三`】`W₀` 之**消費者全定位**（🛑 全唯讀·⛔ 驅動·⛔ 修任何檔一字）")
    say("=" * W)
    say("\U0001f6d1 **⛔ 判孰為正確、⛔ 提修法主張、⛔ 擬任何 diff、⛔ 稱任何處為「缺陷」**——照實具名。")
    say("\U0001f512 母體（**正面列舉**）＝ `app.py` ＋ `verify/` 之全部 `*.py` ＝ **%d** 檔" % len(FILES))
    bad = [r for r in FILES if isinstance(parse(r), Exception)]
    say("\U0001f512 其中 **AST 解析失敗** ＝ **%d** 檔%s"
        % (len(bad), ("：%r" % bad) if bad else "（⇒ 母體零缺口）"))

    # ── 判別力二造（先決） ──────────────────────────────────────
    say("")
    say("─" * W)
    say("【判別力二造·先決】甲[必有命中] `rw_increment` 之呼叫節點 `> 0`／乙[必為零] 一人造函式名")
    say("─" * W)
    calls_rwi = find_calls("rw_increment", FILES)
    fake = "rw" + "_increment_" + "NOSUCH"          # 🔒 坑 `bd`：**執行期組出**·字面⛔ 出艙
    calls_fake = find_calls(fake, FILES)
    say("   · 造甲：`rw_increment` 之呼叫節點 ＝ **%d**（須 `> 0`）⇒ %s"
        % (len(calls_rwi), "✅" if calls_rwi else "\U0001f6d1 器紅"))
    say("   · 造乙：一人造函式名（**執行期組出**）之呼叫節點 ＝ **%d**（須 ＝ `0`）⇒ %s"
        % (len(calls_fake), "✅" if not calls_fake else "\U0001f6d1 器紅"))
    if not calls_rwi or calls_fake:
        say("   \U0001f6d1 **二造同色 ⇒ 器紅** ⇒ **⛔ 出艙任何定位之數**（`rc = 5`）。")
        return 5
    say("   ⇒ **器非紅** ✅")
    say("")
    say("   · **與 `GB-168` 二次精化之外部錨對拍**（⛔ 人造之數）：")
    byfn = {}
    for rel, ln, fn, txt in calls_rwi:
        byfn[fn] = byfn.get(fn, 0) + 1
    say("     | 包層函式 | 本器實得 | `GB-168` 二次精化所載 | 判 |")
    say("     |---|---|---|---|")
    for fn, exp in sorted(GB168_CALLS.items()):
        got = byfn.get(fn, 0)
        say("     | `%s` | **%d** | `%d` | %s |"
            % (fn, got, exp, "✅ 逐位相符" if got == exp else "\U0001f534 相異"))
    for fn in sorted(set(byfn) - set(GB168_CALLS)):
        say("     | `%s` | **%d** | （該錨未載） | 🟡 **錨外之包層**（照實具名） |" % (fn, byfn[fn]))

    # ── a ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`a`】`_tele_exp` 之賦值式逐字與其所在（**列框**·母體 ＝ `%s` 單檔）" % SP)
    say("─" * W)
    hits = lines_with(SP, "_tele_exp")
    say("   · 含 `_tele_exp` 之列 ＝ **%d**" % len(hits))
    for ln, txt in hits:
        say("     - `%s:%d`　`%s`" % (SP, ln, txt.strip()))
    say("   · 其**綁定節點**（AST）：")
    for rel, ln, fn, kind, txt in find_assigns("_tele_exp", SP):
        say("     - `%s:%d`｜包層 `%s`｜`%s`｜逐字 ＝ `%s`" % (rel, ln, fn, kind, txt))

    # ── b ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`b`】`_sd_W0` 之**產生鏈**（AST·⛔ 文字層·⛔ 以推定代之）")
    say("─" * W)
    chain = [("_sd_W0", SP), ("_adv_final", SP)]
    for nm, rel in chain:
        ass = find_assigns(nm, rel)
        say("   · **環**：`%s` @ `%s` ⇒ 綁定節點 **%d** 個" % (nm, rel, len(ass)))
        if not ass:
            say("     \U0001f6d1 **⛔ 可達·其止於** `%s`（該檔內無其綁定節點）" % nm)
        for r, ln, fn, kind, txt in ass:
            say("     - `%s:%d`｜包層 `%s`｜`%s`｜逐字 ＝ `%s`" % (r, ln, fn, kind, txt))
    say("   · **環**：`W0_left`／`W0_right` 之**鍵**之寫入處（母體 ＝ 全部 `*.py`·**列框**）")
    found_key = 0
    for rel in FILES:
        for key in ("W0_left", "W0_right"):
            for ln, txt in lines_with(rel, key):
                found_key += 1
                say("     - `%s:%d`　`%s`" % (rel, ln, txt.strip()))
    if not found_key:
        say("     \U0001f6d1 **⛔ 可達·其止於** `W0_left`／`W0_right`（全母體無其字樣）")

    # ── c ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`c`】`rw_increment` 之**全部呼叫節點**及其實參（`ast.unparse`）＋ 包層函式")
    say("─" * W)
    say("   | # | 檔:列 | 包層函式 | 呼叫之逐字（`ast.unparse`） |")
    say("   |---|---|---|---|")
    for i, (rel, ln, fn, txt) in enumerate(calls_rwi, 1):
        say("   | %d | `%s:%d` | `%s` | `%s` |" % (i, rel, ln, fn, txt))
    say("   ⇒ 合計 **%d** 個呼叫節點（母體 ＝ 上開 **%d** 檔）" % (len(calls_rwi), len(FILES)))

    # ── d ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`d`】`_rw_start` 之決定式逐字 ＋ `W_cur = W_prev + S` 之 `W_prev` 執行緒初值")
    say("─" * W)
    say("   · `_rw_start` 之**綁定節點**（AST·母體 ＝ 全部 `*.py`）：")
    n_rs = 0
    for rel in FILES:
        for r, ln, fn, kind, txt in find_assigns("_rw_start", rel):
            n_rs += 1
            say("     - `%s:%d`｜包層 `%s`｜`%s`｜逐字 ＝ `%s`" % (r, ln, fn, kind, txt))
    if not n_rs:
        say("     \U0001f6d1 **⛔ 可達·其止於** `_rw_start`（全母體無其綁定節點）")
    say("   · `W_cur` 之**綁定節點**（AST·⛔ 文字層）：")
    wcur = []
    for rel in FILES:
        wcur += find_assigns("W_cur", rel)
    if not wcur:
        say("     \U0001f6d1 **⛔ 可達·其止於** `W_cur`（全母體無其綁定節點）")
    encl_wcur = set()
    for r, ln, fn, kind, txt in wcur:
        encl_wcur.add((r, fn))
        say("     - `%s:%d`｜包層 `%s`｜`%s`｜逐字 ＝ `%s`" % (r, ln, fn, kind, txt))
    say("   · `W_prev` 之**綁定節點**（AST·**限上開 `W_cur` 之包層**·即其執行緒之初值候選）：")
    n_wp = 0
    for rel, fname in sorted(encl_wcur):
        t = parse(rel)
        for r, ln, fn, kind, txt in find_assigns("W_prev", rel):
            if fn != fname:
                continue
            n_wp += 1
            say("     - `%s:%d`｜包層 `%s`｜`%s`｜逐字 ＝ `%s`" % (r, ln, fn, kind, txt))
    if not n_wp:
        say("     \U0001f6d1 **⛔ 可達·其止於** `W_prev`（上開包層內無其綁定節點"
            "⇒ 其為**參數**或**外層之名**·照實具名）")
        say("     · 併查：`W_prev` 為**函式參數**之處（AST `arg`）：")
        got_arg = 0
        for rel in FILES:
            t = parse(rel)
            if isinstance(t, Exception):
                continue
            for fn in ast.walk(t):
                if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                args = [a.arg for a in list(fn.args.posonlyargs) + list(fn.args.args)
                        + list(fn.args.kwonlyargs)]
                if "W_prev" in args:
                    got_arg += 1
                    say("       - `%s:%d`｜`def %s(%s)`"
                        % (rel, fn.lineno, fn.name, ", ".join(args)))
        if not got_arg:
            say("       \U0001f6d1 **⛔ 可達**（無其為參數之處）")

    # ── e ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`e`】`rw_from_width` 之**全部呼叫節點** ＋ 包層 ＋ 實參")
    say("─" * W)
    for nm in ("rw_from_width", "_rw_from_width"):
        cs = find_calls(nm, FILES)
        say("   · 名 `%s` ⇒ 呼叫節點 **%d** 個" % (nm, len(cs)))
        for i, (rel, ln, fn, txt) in enumerate(cs, 1):
            say("     %2d. `%s:%d`｜包層 `%s`｜`%s`" % (i, rel, ln, fn, txt))

    # ── f ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`f`】`_fo_left`／`_fo_right` 之賦值節點 ＋ 包層 ＋ 與 `b` 之 `W₀` 賦值節點**是否同框**")
    say("─" * W)
    fo_encl = set()
    for nm in ("_fo_left", "_fo_right"):
        n_fo = 0
        for rel in FILES:
            for r, ln, fn, kind, txt in find_assigns(nm, rel):
                n_fo += 1
                fo_encl.add((r, fn))
                say("   · `%s` ⇒ `%s:%d`｜包層 `%s`｜`%s`｜逐字 ＝ `%s`" % (nm, r, ln, fn, kind, txt))
        if not n_fo:
            say("   \U0001f6d1 `%s` ⇒ **⛔ 可達·其止於**（全母體無其綁定節點）" % nm)
    w0_encl = set()
    for rel in FILES:
        for key in ("W0_left", "W0_right"):
            t = parse(rel)
            if isinstance(t, Exception):
                continue
            for n in ast.walk(t):
                if isinstance(n, ast.Constant) and n.value == key:
                    w0_encl.add((rel, enclosing(t, n)))
    say("   · `b` 之 `W₀` 鍵所在之包層（AST `Constant`）＝ %r" % (sorted(w0_encl),))
    say("   · `f` 之 `forced` 旗標所在之包層 ＝ %r" % (sorted(fo_encl),))
    inter = sorted(w0_encl & fo_encl)
    say("   ⇒ **是否同框**：交集 ＝ **%d** 個 %s ⇒ %s"
        % (len(inter), inter, "🟢 **有同框者**" if inter else "🛑 **無同框者**（照實具名·⛔ 判）"))

    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
