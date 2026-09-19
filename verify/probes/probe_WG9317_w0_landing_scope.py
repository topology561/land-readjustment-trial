# -*- coding: utf-8 -*-
"""`W-G.9-317` `§四` 工項二：落地前之最後定位（**全唯讀**·AST ＋ 字樣錨）。

🛑 **⛔ 驅動管線**（⛔ `run_step_g`／`run_corner_pk`／`solve_G_binary` 之任何執行）、
   **⛔ 匯入即驅動**（一切動作皆在 `if __name__ == "__main__"` 之下）、
   **⛔ 修任何檔一字**、**⛔ 施任何替身**、**⛔ 判孰為正確**、**⛔ 提修法主張**。

受詞（單 `§四` 逐字）：
  `a` `_solve_G_one` 之完整簽章（AST 實查其真實 `lineno`）
  `b` `_solve_G_one` 之全部呼叫節點：檔／`lineno`／包層函式名／實參 `ast.unparse`
  `c` 對 `b` 之每一呼叫節點，其包層函式之區域名空間是否含七名（逐名逐節點之布林表）
  `d` `_mp_base_W0` 之全部定義節點之完整函式體 `ast.unparse`，二者是否逐字相同
  `e` 「強制抵費地⛔ 計 `G`」之碼面現況
  `f` `_W_near`／`_W_near_out` 之全部出現節點（賦值與使用）
  `g` `left_forced_offset`／`right_forced_offset` 之產生處 ＋ 倉內既有落檔中本案之值

判別力二造：`(甲·必有命中)` `_solve_G_one` 之呼叫節點數 `> 0`；
             `(乙·必為零)` 一人造之函式名（**執行期組出**·字面⛔ 出艙·坑 `bd`）＝ `0`。
**二造同色 ⇒ 器紅 ⇒ ⛔ 出艙任何定位之數**（`rc = 5`）。
"""
import ast
import os
import subprocess
import sys

W = 128
TARGET = "_solve_G_one"
SEVEN = ["_fo_left", "_fo_right", "_b_L0", "_b_R0",
         "_mp_base_W0", "_left_buffer_S", "_right_buffer_S"]
SELF = os.path.basename(__file__)

_OUT = []


def say(s=""):
    _OUT.append(s)
    print(s)


def rule(ch="─"):
    say(ch * W)


def git(args):
    return subprocess.run(["git"] + args, capture_output=True)


def tracked_py():
    """母體（**正面列舉**）＝ `app.py` ＋ `verify/` 之全部 `*.py`（含未追蹤之本器）。"""
    r = git(["ls-tree", "-r", "-z", "--name-only", "HEAD"])
    tr = [p for p in r.stdout.decode("utf-8", "replace").split("\0") if p]
    files = [p for p in tr if p == "app.py"
             or (p.startswith("verify/") and p.endswith(".py"))]
    here = "verify/probes/" + SELF
    if os.path.exists(here) and here not in files:
        files.append(here)
    return sorted(files)


def load(path):
    try:
        src = open(path, "rb").read().decode("utf-8")
    except Exception:
        return None, None
    try:
        return src, ast.parse(src)
    except SyntaxError:
        return src, None


def with_parents(tree):
    for node in ast.walk(tree):
        for ch in ast.iter_child_nodes(node):
            ch._parent = node
    return tree


def enclosing_func(node):
    cur = getattr(node, "_parent", None)
    while cur is not None:
        if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return cur
        cur = getattr(cur, "_parent", None)
    return None


def enclosing_stmt(node):
    cur = node
    while cur is not None and not isinstance(cur, ast.stmt):
        cur = getattr(cur, "_parent", None)
    return cur


def callee_name(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    if isinstance(func, ast.Subscript):
        sl = func.slice
        if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
            return sl.value
    return None


def call_nodes(tree, name):
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and callee_name(n.func) == name:
            out.append(n)
    return out


# ────────────────────────────────────────────────────────────────────────────
def main():
    say("=" * W)
    say("【`W-G.9-317` `§四` 工項二】落地前之最後定位（**全唯讀**）")
    say("=" * W)

    head = git(["rev-parse", "HEAD"]).stdout.decode().strip()
    dirty = git(["status", "--porcelain"]).stdout.decode("utf-8", "replace")
    dirty_n = len([x for x in dirty.split("\n") if x.strip()])
    files = tracked_py()
    say("三軸 (1) 來源 ＝ 工作區（`HEAD` ＝ %s／`git status` 條目 ＝ %d）" % (head, dirty_n))
    say("三軸 (2) 母體 ＝ `app.py` ＋ `verify/` 之全部 `*.py` ＝ **%d** 檔（本器自身含在內）" % len(files))
    say("三軸 (3) 粒度框 ＝ AST 節點（`a`、`b`、`c`、`d`、`f`）／列框（`e`、`g`）")

    trees, bad = {}, []
    for p in files:
        src, tr = load(p)
        if tr is None:
            bad.append(p)
            continue
        trees[p] = (src, with_parents(tr))
    say("  AST 解析失敗 ＝ **%d** 檔%s" % (len(bad), ("：" + ", ".join(bad)) if bad else ""))
    say("")

    # ── 判別力二造（先決）────────────────────────────────────────────────
    rule()
    say("【判別力二造・先決】")
    a_cnt = sum(len(call_nodes(t, TARGET)) for _, t in trees.values())
    neg = "_solve_G_" + "".join(chr(ord("a") + (7 * i + 3) % 26) for i in range(5))
    b_cnt = sum(len(call_nodes(t, neg)) for _, t in trees.values())
    say("  造甲[必有命中] `%s` 之呼叫節點 ＝ **%d**（須 `> 0`）⇒ %s"
        % (TARGET, a_cnt, "✅" if a_cnt > 0 else "\U0001f534"))
    say("  造乙[必為零] 一人造之函式名（**執行期組出**·字面⛔ 出艘）＝ **%d**（須 ＝ `0`）⇒ %s"
        % (b_cnt, "✅" if b_cnt == 0 else "\U0001f534"))
    if not (a_cnt > 0 and b_cnt == 0):
        say("  \U0001f6d1 **二造同色 ⇒ 器紅 ⇒ ⛔ 出艘任何定位之數**")
        return 5
    say("  ⇒ **器非紅** ✅")
    rule()
    say("")

    # ── a ───────────────────────────────────────────────────────────────
    say("【`a`】`%s` 之完整簽章（AST·母體 ＝ `app.py`）" % TARGET)
    rule()
    src_app, t_app = trees["app.py"]
    defs = [n for n in ast.walk(t_app)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == TARGET]
    say("  定義節點數 ＝ **%d**" % len(defs))
    for d in defs:
        enc = enclosing_func(d)
        say("  - `app.py:%d`｜包層 ＝ %s｜逐字 ＝"
            % (d.lineno, ("`%s`" % enc.name) if enc else "（頂層）"))
        say("      def %s(%s):" % (d.name, ast.unparse(d.args)))
        say("      體列數 ＝ %d（`lineno` %d – %d）"
            % (len(d.body), d.lineno, getattr(d, "end_lineno", d.lineno)))
    rule()
    say("")

    # ── b ───────────────────────────────────────────────────────────────
    say("【`b`】`%s` 之全部呼叫節點" % TARGET)
    rule()
    say("   | # | 檔:列 | 包層函式 | 呼叫之逐字（`ast.unparse`） |")
    say("   |---|---|---|---|")
    calls = []
    for p in sorted(trees):
        _, t = trees[p]
        for n in call_nodes(t, TARGET):
            calls.append((p, n))
    self_path = "verify/probes/" + SELF
    for i, (p, n) in enumerate(calls, 1):
        enc = enclosing_func(n)
        say("   | %d | `%s:%d` | %s | `%s` |"
            % (i, p, n.lineno, ("`%s`" % enc.name) if enc else "（頂層）",
               ast.unparse(n)))
    n_self = sum(1 for p, _ in calls if p == self_path)
    say("   ⇒ 合計 **%d** 個（**未扣除本器**）／**%d** 個（**已扣除本器自身**）"
        % (len(calls), len(calls) - n_self))
    rule()
    say("")

    # ── c ───────────────────────────────────────────────────────────────
    say("【`c`】每一呼叫節點之包層函式內，七名是否出現（AST `Name`／`arg`）")
    rule()
    say("\U0001f512 **二框並報（本器自捕·入倉前）**：")
    say("   框 `c-1`（**單之逐字框**）＝ 只掃**最內層**包層函式之 AST 子樹；")
    say("   框 `c-2`（**包層鏈框**）＝ 掃**自最內層逐層向外至模組頂層**之全部包層函式。")
    say("   \U0001f534 **二框相異之因**：巢狀函式之外層名⛔ 落於其自身之子樹")
    say("   ⇒ `c-1` 之 `⛔` 只證「**不在本函式之字面內**」，**⛔ 證「不可見」**。")
    say("   \U0001f6d1 本器只出二框之數，**⛔ 判孰為單所欲之受詞**。")
    say("")
    for frame, chain in (("c-1", False), ("c-2", True)):
        say("  ── 框 `%s`%s" % (frame, "（包層鏈）" if chain else "（最內層）"))
        say("   | # | 檔:列 | 包層%s | " % ("鏈" if chain else "")
            + " | ".join("`%s`" % s for s in SEVEN) + " |")
        say("   |---|---|---|" + "---|" * len(SEVEN))
        for i, (p, n) in enumerate(calls, 1):
            encs, cur = [], enclosing_func(n)
            while cur is not None:
                encs.append(cur)
                if not chain:
                    break
                cur = enclosing_func(cur)
            names = set()
            for e in encs:
                for x in ast.walk(e):
                    if isinstance(x, ast.Name):
                        names.add(x.id)
                    elif isinstance(x, ast.arg):
                        names.add(x.arg)
                    elif isinstance(x, ast.Attribute):
                        names.add(x.attr)
            cells = ["✅" if s in names else "⛔" for s in SEVEN]
            label = " ← ".join("`%s`" % e.name for e in encs) if encs else "（頂層）"
            say("   | %d | `%s:%d` | %s | %s |" % (i, p, n.lineno, label, " | ".join(cells)))
        say("")
    rule()
    say("")

    # ── d ───────────────────────────────────────────────────────────────
    say("【`d`】`_mp_base_W0` 之全部定義節點與其逐字比對")
    rule()
    mp = []
    for p in sorted(trees):
        _, t = trees[p]
        for n in ast.walk(t):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "_mp_base_W0":
                mp.append((p, n))
    say("  定義節點數 ＝ **%d**（母體 ＝ 上開 %d 檔）" % (len(mp), len(trees)))
    say("  \U0001f534 **單之受詞逐字 ＝ 「`app.py` ＋ `verify/stepg_pipeline.py`」之二者**；")
    say("     而全母體實得 **%d** 個定義節點 ⇒ 第三個係**射程外**，照實具名、**⛔ 入比對**。" % len(mp))
    bodies = {}
    for p, n in mp:
        enc = enclosing_func(n)
        body = ast.unparse(n)
        bodies.setdefault(p, []).append(body)
        say("")
        say("  ── `%s:%d`｜包層 ＝ %s｜體 bytes（`ast.unparse`）＝ %d｜%s"
            % (p, n.lineno, ("`%s`" % enc.name) if enc else "（頂層）",
               len(body.encode("utf-8")),
               "**單之受詞**" if p in ("app.py", "verify/stepg_pipeline.py")
               else "\U0001f7e1 **射程外·⛔ 入比對**"))
        for ln in body.split("\n"):
            say("      %s" % ln)
    say("")
    pair = ("app.py", "verify/stepg_pipeline.py")
    if all(k in bodies for k in pair):
        b1, b2 = bodies[pair[0]][0], bodies[pair[1]][0]
        same = (b1 == b2)
        say("  ⇒ **單所名之二者（`app.py` vs `verify/stepg_pipeline.py`）逐字相同 ＝ %s**"
            % ("✅ 是" if same else "\U0001f534 否"))
        say("     bytes ＝ %d ／ %d" % (len(b1.encode("utf-8")), len(b2.encode("utf-8"))))
        if not same:
            import difflib
            say("     逐字差（`unified_diff`·前 ＝ `app.py`／後 ＝ `stepg`）：")
            for i, ln in enumerate(difflib.unified_diff(
                    b1.split("\n"), b2.split("\n"), lineterm="", n=1)):
                if i < 40:
                    say("      %s" % ln)
    else:
        say("  \U0001f6d1 單所名之二檔中有一⛔ 見定義節點 ⇒ 【⛔ 可得】")
    rule()
    say("")

    # ── e ───────────────────────────────────────────────────────────────
    say("【`e`】「強制抵費地⛔ 計 `G`」之碼面現況")
    rule()
    FORCED = ["_fo_left", "_fo_right", "forced", "left_forced_offset",
              "right_forced_offset", "強制抵費地"]
    say("  查法一（AST）：掃全母體之 `If`／`IfExp` 節點，其 `test` 之 `ast.unparse` 含上列任一 forced 字樣者，")
    say("           再於其 `body` 內尋「跳過」（`Continue`／`Pass`／`Break`）或「歸零」（目標名含 `G` 且值為常數 `0`）。")
    say("  查法二（列框）：逐檔計 forced 字樣與 `G` 同列之命中。")
    hits_e = []
    for p in sorted(trees):
        _, t = trees[p]
        if p == self_path:
            continue
        for n in ast.walk(t):
            test = None
            if isinstance(n, ast.If):
                test = n.test
                body = n.body
            elif isinstance(n, ast.IfExp):
                test = n.test
                body = [ast.Expr(value=n.body)]
            if test is None:
                continue
            ts = ast.unparse(test)
            if not any(f in ts for f in FORCED):
                continue
            kinds = []
            for x in body:
                for y in ast.walk(x):
                    if isinstance(y, (ast.Continue, ast.Pass, ast.Break)):
                        kinds.append(type(y).__name__)
                    if isinstance(y, ast.Assign):
                        tgt = ", ".join(ast.unparse(z) for z in y.targets)
                        if "G" in tgt and isinstance(y.value, ast.Constant) \
                                and y.value.value in (0, 0.0):
                            kinds.append("G歸零: %s = %s" % (tgt, ast.unparse(y.value)))
            if kinds:
                enc = enclosing_func(n)
                hits_e.append((p, n.lineno,
                               ("`%s`" % enc.name) if enc else "（頂層）",
                               ts, kinds))
    say("")
    say("  查法一之命中 ＝ **%d** 筆" % len(hits_e))
    for p, ln, enc, ts, kinds in hits_e:
        say("   - `%s:%d`｜包層 %s｜`test` ＝ `%s`｜%s"
            % (p, ln, enc, ts, "／".join(kinds)))
    if not hits_e:
        say("   （**無命中·照實載為 `0`**）")
    say("")
    say("  查法二之逐檔列框（forced 字樣 ⋀ 同列含 `G`）：")
    for p in ["app.py", "verify/stepg_pipeline.py", "verify/wf_f1.py", "verify/wf_f4.py"]:
        if p not in trees:
            continue
        src, _ = trees[p]
        c = 0
        for ln in src.split("\n"):
            if any(f in ln for f in FORCED) and "G" in ln:
                c += 1
        say("   - `%s` ＝ **%d** 列" % (p, c))
    rule()
    say("")

    # ── f ───────────────────────────────────────────────────────────────
    say("【`f`】`_W_near`／`_W_near_out` 之全部出現節點")
    rule()
    say("   | # | 檔:列 | 包層 | `ctx` | 所在敍述之逐字（`ast.unparse`） |")
    say("   |---|---|---|---|---|")
    seen, k = set(), 0
    n_self_f = 0
    for p in sorted(trees):
        _, t = trees[p]
        for n in ast.walk(t):
            if isinstance(n, ast.Name) and n.id in ("_W_near", "_W_near_out"):
                st = enclosing_stmt(n)
                enc = enclosing_func(n)
                key = (p, getattr(st, "lineno", n.lineno), n.id, type(n.ctx).__name__)
                if key in seen:
                    continue
                seen.add(key)
                k += 1
                if p == self_path:
                    n_self_f += 1
                src_line = ast.unparse(st) if st is not None else "（無）"
                if len(src_line) > 150:
                    src_line = src_line[:150] + "…"
                say("   | %d | `%s:%d` | %s | `%s` | `%s` |"
                    % (k, p, getattr(st, "lineno", n.lineno),
                       ("`%s`" % enc.name) if enc else "（頂層）",
                       type(n.ctx).__name__, src_line))
    say("   ⇒ 合計 **%d**（未扣除本器）／**%d**（已扣除本器）" % (k, k - n_self_f))
    rule()
    say("")

    # ── f′（本器之附帶量·⛔ 單之受詞·照實具名）────────────────────────
    say("【`f′`】**本器之附帶量·⛔ 單之受詞·照實具名**：鍵 `'W_near'` 之全部出現節點")
    rule()
    say("   （其用：`f` 已定位 `_W_near_out` 止於 `solve_G_binary` 之回傳字典；本項只出該鍵之讀寫處，**⛔ 判其為同一鎖**。）")
    say("   | # | 檔:列 | 包層 | 所在敍述之逐字 |")
    say("   |---|---|---|---|")
    seen2, k2, k2_self = set(), 0, 0
    for p in sorted(trees):
        _, t = trees[p]
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and n.value == "W_near":
                st = enclosing_stmt(n)
                enc = enclosing_func(n)
                key = (p, getattr(st, "lineno", n.lineno))
                if key in seen2:
                    continue
                seen2.add(key)
                k2 += 1
                if p == self_path:
                    k2_self += 1
                s = ast.unparse(st) if st is not None else "（無）"
                if len(s) > 150:
                    s = s[:150] + "…"
                say("   | %d | `%s:%d` | %s | `%s` |"
                    % (k2, p, getattr(st, "lineno", n.lineno),
                       ("`%s`" % enc.name) if enc else "（頂層）", s))
    say("   ⇒ 合計 **%d**（未扣除本器）／**%d**（已扣除本器）" % (k2, k2 - k2_self))
    rule()
    say("")

    # ── g ───────────────────────────────────────────────────────────────
    say("【`g`】`left_forced_offset`／`right_forced_offset` 之產生處 ＋ 倉內既有落檔之值")
    rule()
    say("  一、產生處（AST：含該字串常數之敍述）")
    g_hits = 0
    for p in sorted(trees):
        if p == self_path:
            continue
        _, t = trees[p]
        rows = set()
        for n in ast.walk(t):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) \
                    and n.value in ("left_forced_offset", "right_forced_offset",
                                    "f3L_forced_offset"):
                st = enclosing_stmt(n)
                enc = enclosing_func(n)
                s = ast.unparse(st) if st is not None else ""
                if len(s) > 160:
                    s = s[:160] + "…"
                rows.add((getattr(st, "lineno", n.lineno),
                          ("`%s`" % enc.name) if enc else "（頂層）", s))
        for ln, enc, s in sorted(rows):
            g_hits += 1
            say("   - `%s:%d`｜包層 %s｜`%s`" % (p, ln, enc, s))
    say("   ⇒ 合計 **%d** 筆" % g_hits)

    say("")
    say("  二、倉內既有落檔（`verify/out/`·**⛔ 新驅動**）中之字樣")
    outs = git(["ls-tree", "-r", "-z", "--name-only", "HEAD", "--", "verify/out/"])
    out_files = [x for x in outs.stdout.decode("utf-8", "replace").split("\0") if x]
    say("   母體 ＝ `verify/out/` 之追蹤檔 **%d**" % len(out_files))
    for tok in ("right_forced_offset", "W0_right", "Wf_right"):
        r = git(["grep", "-a", "-c", tok, "HEAD", "--", "verify/out/"])
        lines = [x for x in r.stdout.decode("utf-8", "replace").split("\n") if x.strip()]
        say("   - 字樣 `%s` ⇒ **%d** 檔" % (tok, len(lines)))
        for x in lines[:8]:
            say("       %s" % x)
        if len(lines) > 8:
            say("       （餘 %d 檔略）" % (len(lines) - 8))
    say("")
    say("  三、**實掃**：含 `right_forced_offset` 之每一檔，逐檔判其是否同檔載")
    say("     `(i)` 態乙之標記（字樣 `WV_K6_STEP0` 或 `態乙`）｜`(ii)` 態甲之標記（字樣 `態甲`）｜")
    say("     `(iii)` 一列同時含 `R4` 與 `right_forced_offset`（其值逐字）")
    say("   | # | 檔 | 態乙標記 | 態甲標記 | `R4` 同列之值（逐字·至多二筆） |")
    say("   |---|---|---|---|---|")
    fo_files = []
    r = git(["grep", "-a", "-l", "right_forced_offset", "HEAD", "--", "verify/out/"])
    for x in r.stdout.decode("utf-8", "replace").split("\n"):
        x = x.strip()
        if x.startswith("HEAD:"):
            fo_files.append(x[5:].strip('"'))
    n_b = n_a = 0
    for i, f in enumerate(sorted(fo_files), 1):
        raw = git(["show", "HEAD:%s" % f]).stdout.decode("utf-8", "replace")
        has_b = ("WV_K6_STEP0" in raw) or ("態乙" in raw)
        has_a = ("態甲" in raw)
        rows = [ln.strip() for ln in raw.split("\n")
                if "R4" in ln and "right_forced_offset" in ln]
        if has_b and rows:
            n_b += 1
        if has_a and rows:
            n_a += 1
        shown = " ／ ".join(x[:70] for x in rows[:2]) if rows else "（無）"
        say("   | %d | `%s` | %s | %s | `%s` |"
            % (i, f, "✅" if has_b else "⛔", "✅" if has_a else "⛔", shown))
    say("")
    say("   \U0001f512 **實掃之得數**：同檔具「態乙標記 ⋀ `R4` 列」者 ＝ **%d** 檔；"
        % n_b)
    say("     判別力[必非零]：同檔具「態甲標記 ⋀ `R4` 列」者 ＝ **%d** 檔 ⇒ %s"
        % (n_a, "✅ 本檢⛔ 恒為零" if n_a > 0 else "\U0001f534 器紅"))
    say("")
    if n_b == 0:
        say("   \U0001f512 本案 `R4` **右**側於**態乙**之 `right_forced_offset`：")
        say("     【**⛔ 可得·其止於**】上表實掃 ＝ **0** 檔同檔具「態乙標記 ⋀ `R4` 列」；")
        say("     取得之法須**新驅動**（單 `§七` 之禁）⇒ **候發單側另單**。")
    else:
        say("   \U0001f512 實掃得 **%d** 檔同檔具二者 ⇒ **其值可得**，逐檔具名於上表。" % n_b)
    rule()
    say("")
    say("\U0001f512 **本器只出定位·⛔ 判孰為正確·⛔ 提修法主張·⛔ 擬任何 diff·⛔ 稱任何處為「缺陷」**")
    return 0


if __name__ == "__main__":
    rc = main()
    dst = os.path.join("verify", "out", "WG9317_landing_scope.log")
    try:
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(_OUT) + "\n")
    except Exception as exc:                                  # noqa: BLE001
        print("\U0001f6d1 落檔失敗：%s" % exc)
        rc = rc or 4
    sys.exit(rc)
