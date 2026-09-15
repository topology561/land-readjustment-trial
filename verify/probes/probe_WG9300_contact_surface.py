#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-300` 工項一：**路丙之接觸面之現查**（主線·零生產碼·🛑 含三停機款）。

── 本器之地位 ──────────────────────────────────────────────────────────────────
單 `§三` **明文授權**二項手段：① 執行 `run_verification` 全量一次（供款 `2` **乙形**之動態量測）
② 於 `verify/probes/` **新增**量測器（**⛔ 動既有探針一字**）。本器即 ②。
🛑 **本器⛔ 改生產碼一字**——其對生產態之唯一介入係**包裹 `ns["_corner_buffer_S"]`**
（`W-G.9-299 §五` 款 `2` 所明定之取法），且該包裹**只讀不改**其回傳值（`return f(*a, **k)`）。

── 款之對應 ────────────────────────────────────────────────────────────────────
`款 1` `S` ＝ `_corner_buffer_S` 之全部呼叫端（**AST**·二形並取·母體 ＝ 生產碼 `34` 檔·正面列舉）
`款 2` `F` ＝ 生產期實走者（**(甲) 靜態** `import` 遞移閉包／**(乙) 動態** 包裹計次·**二形分列**）
`款 3` `_first_corner_alloc_dir` 之可達性（三態）＋ `side_mid` 之在域性（`f_locals`／`t.body`·**二鍵並報**）
`款 4` **判準載體**之現查（頂層 `*_EXPECT` 之 AST 賦值數 ＋ `baselines` 之列框數）
`款 5` 判別力四造

── 恆常附款之遵行 ──────────────────────────────────────────────────────────────
· `id(·)` **⛔ 作錨**——呼叫端之辨識一律以**呼叫鏈之 `co_name`／`co_filename` 序**；
  同一性之比對用 `is`（`code` 物件之 `in` 判定係 `is` 語意）。
· **字樣錨**（⛔ 行號為錨）＋ 其**唯一性之判別力自檢**（寬字樣須 `> 1`）。
· **判定組為空一律 loud 拒測**（⛔ `all()` 空集恆真）。
· **量測器之母體⛔ 含其自身輸出**——本器⛔ 呼叫 `_corner_buffer_S`；包裹之計數分
  「生產錄」與「器自身」二欄（後者恆 `0`·出艙以證之）。
· **[必為零]之造一律<u>執行期組出</u>**，其字面⛔ 落入任何輸出（`GB-147`）。
· 頂層之取用一律 `t.body`（⛔ `ast.walk` 誤收巢狀）。
· **帶號與絕對值並列**（本器之數皆為計數·無號問題·仍逐欄具名其框）。

用法：
  `python verify/probes/probe_WG9300_contact_surface.py static`    # 款 1／3 之靜態半／4／5
  `python verify/probes/probe_WG9300_contact_surface.py dynamic`   # 款 2 乙 ＋ 款 3 之動態半（**長跑**）
`rc`：`0` 正常出艙／`2` **量測器紅**（判別力造不如預期 ⇒ loud 拒測·⛔ 出艙任何判）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」。
"""
import ast
import os
import subprocess
import sys
import time


# 🩸 **本器自捕（`W-G.9-300`·出艙前攔下·⛔ 頂替）**：本行原為**二層** `dirname`
#    ⇒ 本器居 `verify/probes/` ⇒ `REPO` 解為 `…/verify` ⇒ `git ls-tree HEAD -- verify/`
#    於該 cwd 解為 `verify/verify/` ⇒ **靜默得空** ⇒ 母體由 `34` 檔塌為 `1` 檔（僅 `app.py`，
#    其由 `HEAD:app.py` 與 cwd 無關而倖存）。🔴 **原四造全綠**——`[必非零] |S|≥1` 由 `app.py`
#    之二處滿足、`[必命中]` 係自反 ⇒ 二者對母體流失**全盲**。⇒ 增 `[必為 34]` 之**外部錨**
#    （`常規八`：`N/N` 之自證只證一致·⛔ 證正確）。
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = 112
TARGET = "_corner_buffer_S"
INJECT = "_first_corner_alloc_dir"


def hr(ch="─"):
    print(ch * W)


def title(s):
    print()
    print("=" * W)
    print(s)
    print("=" * W)


# ══════════════════════════════════════════════════════════════════════════════
# 母體：生產碼 34 檔（**正面列舉**·⛔ pathspec `verify/*.py`·坑 `be`）
# ══════════════════════════════════════════════════════════════════════════════
def prod_files():
    r = subprocess.run(["git", "ls-tree", "HEAD", "--name-only", "verify/"],
                       cwd=REPO, capture_output=True, text=True)
    tops = sorted(x for x in r.stdout.split("\n") if x.endswith(".py"))
    files = ["app.py"] + tops
    return files, r.returncode


def read_blob(path):
    r = subprocess.run(["git", "cat-file", "blob", "HEAD:" + path],
                       cwd=REPO, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8")


# ══════════════════════════════════════════════════════════════════════════════
# 款 1：`S` ＝ 全部呼叫端（AST·二形並取）
# ══════════════════════════════════════════════════════════════════════════════
def _is_target_call(node, name):
    """二形並取：`Name(<name>)` 或 `Subscript(Name('ns'), Constant(<name>))`。"""
    f = node.func
    if isinstance(f, ast.Name) and f.id == name:
        return "形甲 Name"
    if isinstance(f, ast.Subscript) and isinstance(f.value, ast.Name) and f.value.id == "ns":
        sl = f.slice
        if isinstance(sl, ast.Constant) and sl.value == name:
            return "形乙 ns[...]"
    return None


def _func_stack(tree, line):
    """該行所在之函式鏈（外→內）。"""
    out = []

    def rec(node):
        for ch in ast.iter_child_nodes(node):
            if hasattr(ch, "lineno") and hasattr(ch, "end_lineno") \
                    and ch.lineno <= line <= ch.end_lineno:
                if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out.append(ch.name)
                rec(ch)
    rec(tree)
    return out or ["<模組層>"]


def _alloc_dir_arg(node):
    """`allocation_dir` 位之實參逐字（`ast.unparse`）。
    契約：`def _corner_buffer_S(block_poly, d_hat, front_p1, allocation_dir, range_area, side, ...)`
    ⇒ 位置第 `4`（索引 `3`）或關鍵字 `allocation_dir`。"""
    for kw in node.keywords:
        if kw.arg == "allocation_dir":
            return ast.unparse(kw.value), "關鍵字"
    if len(node.args) >= 4:
        return ast.unparse(node.args[3]), "位置#4"
    return None, "⛔ 不可得"


def scan_calls(name, files):
    """回 [(檔, 形, 函式鏈, allocation_dir 逐字, 取位, 行)]（行⛔ 為錨·僅供對位）。"""
    hits = []
    for p in files:
        src = read_blob(p)
        if src is None:
            print("  🔴 blob 讀不到：%s" % p)
            continue
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                form = _is_target_call(node, name)
                if form:
                    a, how = _alloc_dir_arg(node)
                    hits.append((p, form, ".".join(_func_stack(tree, node.lineno)),
                                 a, how, node.lineno))
    return hits


def anchor_for(path, line):
    """字樣錨（⛔ 行號為錨）＝ 該呼叫之賦值列去空白後之逐字。"""
    src = read_blob(path)
    lines = src.split("\n")
    return lines[line - 1].strip()


def count_lines(path, needle):
    src = read_blob(path)
    return sum(1 for ln in src.split("\n") if needle in ln)


def in_def_main(path, line):
    """該行是否落於該檔之 `def main` 內（**AST 實查**·⛔ 硬編）。"""
    src = read_blob(path)
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "main":
            return (node.lineno <= line <= node.end_lineno), (node.lineno, node.end_lineno)
    return False, None


# ══════════════════════════════════════════════════════════════════════════════
# 款 2 (甲)：`import` 之遞移閉包（自 `verify/run_verification.py` 起·母體 ＝ 34 檔）
# ══════════════════════════════════════════════════════════════════════════════
def import_closure(root, files):
    stem = {}
    for p in files:
        stem[os.path.splitext(os.path.basename(p))[0]] = p
    seen, order, queue = set(), [], [root]
    while queue:
        cur = queue.pop(0)
        if cur in seen:
            continue
        seen.add(cur)
        order.append(cur)
        src = read_blob(cur)
        if src is None:
            continue
        tree = ast.parse(src)
        for node in ast.walk(tree):
            mods = []
            if isinstance(node, ast.Import):
                mods = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    mods = [node.module.split(".")[0]]
            for m in mods:
                if m in stem and stem[m] not in seen:
                    queue.append(stem[m])
    return order


# ══════════════════════════════════════════════════════════════════════════════
# 款 3（靜態半）：`_first_corner_alloc_dir` 之可達性 ＋ `side_mid` 在域性（`t.body` 頂層）
# ══════════════════════════════════════════════════════════════════════════════
def top_level_names(path):
    src = read_blob(path)
    tree = ast.parse(src)
    out = set()
    for node in tree.body:                       # 🔒 `t.body`·⛔ `ast.walk`
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            out.add(node.name)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    out.add(t.id)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for a in node.names:
                out.add(a.asname or a.name.split(".")[0])
    return out


def assigned_before(path, func_line, call_line, prefix):
    """該函式內、**呼叫列之前**是否已有合 `prefix` 之名被賦值（⛔ 及於呼叫列之後）。"""
    src = read_blob(path)
    tree = ast.parse(src)
    res = {"之前": [], "之後": []}
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store) \
                and prefix in node.id and func_line <= node.lineno:
            key = "之前" if node.lineno < call_line else "之後"
            if node.id not in res[key]:
                res[key].append(node.id)
    return res


# ══════════════════════════════════════════════════════════════════════════════
# 款 4：判準載體（頂層 `*_EXPECT` 之 AST 賦值數 ＋ `baselines` 列框）
# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# 款 4′：`forced` 路徑之判（`停二` 之受詞）
# ══════════════════════════════════════════════════════════════════════════════
# 🔒 **旗字樣集**（逐字·⛔ 裸「forced」一詞而已）——其涵蓋本倉 `forced` 之三種寫法：
#    `app`／`stepg` 之 `_fo_left`／`_fo_right`；`wf_f1`／`wf_f4` 之 `fo.get("…_forced_offset")`。
FORCED_TOKENS = ("_fo_left", "_fo_right", "forced_offset", "forced")


def enclosing_tests(path, line):
    """該行之**全部外圍** `If`／`IfExp` 之 `test`（`ast.unparse`）。"""
    src = read_blob(path)
    tree = ast.parse(src)
    out = []

    def rec(node):
        for ch in ast.iter_child_nodes(node):
            if hasattr(ch, "lineno") and hasattr(ch, "end_lineno") \
                    and ch.lineno <= line <= ch.end_lineno:
                if isinstance(ch, ast.If):
                    out.append(("If", ast.unparse(ch.test)))
                elif isinstance(ch, ast.IfExp):
                    out.append(("IfExp", ast.unparse(ch.test)))
                rec(ch)
    rec(tree)
    return out


def _def_line(path, name):
    src = read_blob(path)
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node.lineno
    return 1


def expect_top_level(path):
    src = read_blob(path)
    tree = ast.parse(src)
    names = []
    for node in tree.body:                       # 🔒 `t.body`·⛔ 字樣掃
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            tgts = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in tgts:
                if isinstance(t, ast.Name) and t.id.endswith("_EXPECT"):
                    names.append(t.id)
    return names


# ══════════════════════════════════════════════════════════════════════════════
# static
# ══════════════════════════════════════════════════════════════════════════════
def run_static():
    red = []
    files, rc = prod_files()
    title("款 1　`S` ＝ `%s` 之全部呼叫端（**AST**·二形並取）" % TARGET)
    print("母體（**正面列舉**）＝ `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`"
          "　rc ＝ %d　基數 ＝ **%d**（1 + %d）" % (rc, len(files), len(files) - 1))
    S = scan_calls(TARGET, files)
    fset = sorted({h[0] for h in S})
    print("**檔／處二數並報**：檔 ＝ **%d**／處 ＝ **%d**" % (len(fset), len(S)))
    print()
    hr()
    for i, (p, form, fn, a, how, ln) in enumerate(S, 1):
        anc = anchor_for(p, ln)
        uniq = count_lines(p, anc)
        wide = count_lines(p, TARGET + "(")
        inmain, rng = in_def_main(p, ln)
        print("S%d  檔 ＝ `%s`" % (i, p))
        print("     形            ＝ %s" % form)
        print("     所在函式名     ＝ `%s`" % fn)
        print("     字樣錨（⛔ 行號為錨）＝ `%s`" % anc)
        print("     　唯一性 ＝ %d（該檔·列框）／判別力自檢 寬字樣 `%s(` ＝ %d ⇒ 非恆為 1：%s"
              % (uniq, TARGET, wide, wide > uniq))
        print("     `allocation_dir` 位之實參逐字（`ast.unparse`）＝ `%s`（取位 %s）" % (a, how))
        print("     落於該檔 `def main` 內（**AST 實查**）＝ **%s**%s"
              % (inmain, ("（`def main` ＝ %d-%d）" % rng) if rng else ""))
        print("     ⛔ 非錨·當態 blob 之位 ＝ :%d" % ln)
        hr()

    print()
    print("── **文字層**之數（以資對照·`%s(` 之**列框**）──" % TARGET)
    tot_txt = 0
    for p in files:
        c = count_lines(p, TARGET + "(")
        if c:
            print("   %-34s 列框 ＝ %d" % (p, c))
            tot_txt += c
    print("   文字層合計 ＝ **%d** 列／AST 之處 ＝ **%d**" % (tot_txt, len(S)))
    if tot_txt != len(S):
        print("   🛑 **loud 具名：二數相異**（差 ＝ %d）——成因逐項：" % (tot_txt - len(S)))
        for p in files:
            src = read_blob(p)
            for j, ln in enumerate(src.split("\n"), 1):
                if TARGET + "(" in ln and not any(h[0] == p and h[5] == j for h in S):
                    print("     · `%s` ⛔ 非 `Call` 之列：`%s`" % (p, ln.strip()[:88]))
    else:
        print("   二數相同 ⇒ ⛔ 須 loud")

    # ── 款 4 ──────────────────────────────────────────────────────────────────
    title("款 4　**判準載體**之現查（頂層 `*_EXPECT` 之 AST 賦值 ＋ `baselines` 列框）")
    print("母體 ＝ 全 `%d` 檔（供 `S ∪ F` 之取用·逐檔二數並報）" % len(files))
    hr()
    tot_e = 0
    carriers = []
    for p in files:
        e = expect_top_level(p)
        b = count_lines(p, "baselines")
        tot_e += len(e)
        if e or b:
            print("   %-34s 頂層 `*_EXPECT` ＝ %-2d  `baselines` 列框 ＝ %-3d %s"
                  % (p, len(e), b, ("　" + ", ".join("`%s`" % x for x in e)) if e else ""))
        if e:
            carriers.append(p)
    print()
    print("   全母體頂層 `*_EXPECT` 合計 ＝ **%d** 個／分布於 **%d** 檔：%s"
          % (tot_e, len(carriers), ", ".join("`%s`" % c for c in carriers)))
    print("   🔒 發單側之預查（⛔ 充結論·本器自行重得）＝ `11` 個·分布 "
          "`run_verification.py`／`wd4_tier_list.py`／`wf_f0.py`／`wf_f4.py`")
    print("   ⇒ 本器實得 ＝ **%d** 個／**%d** 檔 ⇒ 與預查 %s"
          % (tot_e, len(carriers), "相符" if tot_e == 11 else "**相異·照實出艙**"))

    # ── 款 2 (甲) ─────────────────────────────────────────────────────────────
    title("款 2 (甲)　**靜態**：`verify/run_verification.py` 之遞移 `import` 閉包（母體 ＝ 34 檔）")
    clo = import_closure("verify/run_verification.py", files)
    print("閉包之**全量列舉**（基數 ＝ **%d**）：" % len(clo))
    for i, c in enumerate(clo, 1):
        print("   %02d %s" % (i, c))
    print()
    print("S 之各檔是否在閉包內：")
    for p in fset:
        print("   %-34s ⇒ %s" % (p, "✅ 在閉包內" if p in clo else "🔴 **⛔ 在閉包內**"))

    # ── 款 3（靜態半）────────────────────────────────────────────────────────
    title("款 3（靜態半）　`%s` 之可達性 ＋ `side_mid` 之在域性（`t.body` 頂層）" % INJECT)
    for i, (p, form, fn, a, how, ln) in enumerate(S, 1):
        tops = top_level_names(p)
        print("S%d `%s` :: `%s`" % (i, p, fn))
        print("   `%s` 於**該檔頂層**（`t.body`）＝ **%s**" % (INJECT, INJECT in tops))
        print("   `ns` 於該檔頂層 ＝ %s；該檔含 `ns[\"%s\"]` 之列框 ＝ %d"
              % ("ns" in tops, INJECT, count_lines(p, 'ns["%s"]' % INJECT)))
        fl = None
        src = read_blob(p)
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                    and node.lineno <= ln <= node.end_lineno:
                if fl is None or node.lineno > fl:
                    fl = node.lineno
        sm = assigned_before(p, fl, ln, "side_mid")
        print("   `side_mid` 族之名於該函式內（**二鍵並報**·⛔ 只報其一）：")
        print("      **呼叫列之前**已賦值 ＝ %s" % (sm["之前"] or "**空**"))
        print("      **呼叫列之後**方賦值 ＝ %s" % (sm["之後"] or "**空**"))
        print("   ⇒ 靜態在域性判 ＝ %s"
              % ("✅ 可取" if sm["之前"] else "🔴 **⛔ 可取（呼叫列之前無任何 `side_mid` 族之名被賦值）**"))
        hr()

    # ── 款 4′：`forced` 路徑之逐處判（停二之受詞）────────────────────────────
    title("款 4′　各處**是否為 `forced` 之路徑**（`停二` 之受詞·⛔ 憑閱讀·**AST 實查**）")
    print("**其判之產生指令**（逐字）：對每一 `Call` 節點，取其於該檔 AST 中之**全部外圍**")
    print("`ast.If`／`ast.IfExp` 節點（判準 ＝ `n.lineno <= call.lineno <= n.end_lineno`，")
    print("且 `IfExp` 以 `body`／`orelse` 之行域界之），將其 `test` 以 `ast.unparse` 出艙；")
    print("**旗字樣集**（逐字）＝ %s；任一外圍 `test` 命中即判其為 `forced` 路徑。" % (FORCED_TOKENS,))
    print()
    hr()
    forced_map = {}
    for i, (p, form, fn, a, how, ln) in enumerate(S, 1):
        tests = enclosing_tests(p, ln)
        hit = [t for t in tests if any(tok in t[1] for tok in FORCED_TOKENS)]
        forced_map["S%d" % i] = bool(hit)
        print("S%d `%s` :: `%s`" % (i, p, fn))
        for kind, t in tests:
            mk = "🔑 **命中**" if any(tok in t for tok in FORCED_TOKENS) else "　"
            print("    %s %-6s `%s`" % (mk, kind, t[:86]))
        print("    ⇒ **是否 `forced` 之路徑 ＝ %s**" % ("**是**" if hit else "否"))
        hr()
    print("判別力[必為否] 一**非** `forced` 之對照受詞：`%s` 之定義列（`def _corner_buffer_S`）"
          "其外圍 `If`／`IfExp` ＝ %d 個 ⇒ 判 ＝ %s（須「否」）"
          % (TARGET, len(enclosing_tests("app.py", _def_line("app.py", TARGET))),
             "否" if not any(any(tok in t for tok in FORCED_TOKENS)
                             for _k, t in enclosing_tests("app.py", _def_line("app.py", TARGET)))
             else "🔴 是"))

    # ── 款 5 判別力四造 ───────────────────────────────────────────────────────
    title("款 5　判別力五造")
    c1 = len(S) >= 1
    print("[必非零] `|S| ≥ 1` ⇒ |S| ＝ %d ⇒ %s" % (len(S), "✅" if c1 else "🔴"))
    c2 = True
    print("[必相異] 文字層之數（%d）與 AST 之數（%d）**各自出艙** ⇒ ✅（⛔ 只報其一）"
          % (tot_txt, len(S)))
    fake = "_" + "".join(["corner", "buffer", "S"]) + "_nosuch_" + str(int(time.time()))
    nf = scan_calls(fake, files)
    c3 = len(nf) == 0
    print("[必為零] 一**執行期組出**之人造函式名（字面⛔ 出艙）於款 1 之框下命中 ＝ %d ⇒ %s"
          % (len(nf), "✅" if c3 else "🔴"))
    c4 = "verify/run_verification.py" in clo
    print("[必命中] `verify/run_verification.py` 在款 2 甲形之閉包內（自反）＝ %s ⇒ %s"
          % (c4, "✅" if c4 else "🔴"))
    # 🆕 第五造（**本器自捕所增**·`常規八 二 ③` 界限檢查）：母體基數之**外部錨**。
    #    其外部錨 ＝ `§零` 閘 `7` 獨立所得之 `34`（⛔ 由本器自身重算而自證一致）。
    c5 = len(files) == 34
    print("[必為 34] 母體基數（外部錨 ＝ `§零` 閘 `7`）＝ %d ⇒ %s　"
          "🔒 本造係本器自捕母體塌陷（`34`→`1`）後所增·⛔ 原四造能偵之"
          % (len(files), "✅" if c5 else "🔴"))
    if not (c1 and c2 and c3 and c4 and c5):
        red.append("判別力五造")

    print()
    if red:
        print("🛑 **量測器紅**：%s ⇒ loud 拒測·⛔ 出艙任何判" % "／".join(red))
        return 2
    print("✅ 判別力四造全數成立 ⇒ 本器非恆綠亦非恆紅")
    return 0


# ══════════════════════════════════════════════════════════════════════════════
# dynamic：款 2 (乙) ＋ 款 3（動態半）
# ══════════════════════════════════════════════════════════════════════════════
REC = []          # 生產錄
SELF = []         # 器自身之呼叫（**母體須扣除**·恆應為 0）
_IN_DRIVE = [False]


def _chain(depth=15):
    """呼叫鏈之 `co_name`／`co_filename` 序（**⛔ `id(·)`**）。"""
    out = []
    f = sys._getframe(2)
    for _ in range(depth):
        if f is None:
            break
        out.append((f.f_code.co_name, os.path.basename(f.f_code.co_filename), f.f_lineno))
        f = f.f_back
    return out


def _probe_keys(depth=3):
    """呼叫端 `f_locals` 之 `side_mid`／`ns`／`_first_corner_alloc_dir` 之在否（**鍵先自證存在**）。"""
    f = sys._getframe(2)
    out = []
    for _ in range(depth):
        if f is None:
            break
        loc = f.f_locals
        glb = f.f_globals
        ent = {
            "函式": f.f_code.co_name,
            "檔": os.path.basename(f.f_code.co_filename),
            # 🔒 二鍵並報（`自誤`「`blk` 恆得 None」之攔法）
            "鍵 `side_mid` 在 f_locals": "side_mid" in loc,
            "鍵 `_side_mid_left` 在 f_locals": "_side_mid_left" in loc,
            "鍵 `_side_mid_right` 在 f_locals": "_side_mid_right" in loc,
            "鍵 `_side_lines_blk` 在 f_locals": "_side_lines_blk" in loc,
            "鍵 `ns` 在 f_locals": "ns" in loc,
            "鍵 `ns` 在 f_globals": "ns" in glb,
            "`%s` 在 f_globals" % INJECT: INJECT in glb,
            "閉包 co_freevars": tuple(f.f_code.co_freevars),
        }
        if "ns" in loc and isinstance(loc["ns"], dict):
            ent["`ns` 含 `%s`" % INJECT] = INJECT in loc["ns"]
        out.append(ent)
        f = f.f_back
    return out


def make_wrapper(fn):
    def _w(*a, **k):
        ch = _chain()
        if _IN_DRIVE[0]:
            REC.append({"chain": ch, "keys": _probe_keys(),
                        "alloc_dir_arg": (a[3] if len(a) >= 4 else k.get("allocation_dir")),
                        "side": (a[5] if len(a) >= 6 else k.get("side")),
                        "label": k.get("_label")})
        else:
            SELF.append(ch)
        return fn(*a, **k)                      # 🔒 只讀不改·⛔ 改其回傳值
    _w._wg9300 = True
    _w.__wrapped__ = fn
    return _w


# ── 外圍函式之執行計數 ───────────────────────────────────────────────────────────
# 🔑 其用：區辨「**外圍函式從未執行**」與「**外圍執行而 `forced` 分支為偽**」。
#    `W-G.9-299 §五` 款 `2` 逐字：未執行者⛔ 以「未執行」充「非接觸面」，
#    一律 **loud 具名為「本案未走·射程未定」**——而該二因**射程之未定程度相異**，故須分辨。
ENCL = {}


def make_counter(fn, tag):
    ENCL.setdefault(tag, 0)

    def _c(*a, **k):
        ENCL[tag] += 1
        return fn(*a, **k)
    _c._wg9300 = True
    _c.__wrapped__ = fn
    return _c


def run_dynamic():
    sys.path.insert(0, os.path.join(REPO, "verify"))
    os.chdir(REPO)
    import run_verification as RV

    title("款 2 (乙)　**動態**：包裹 `ns[\"%s\"]` ＋ 呼叫鏈之 `co_name` 序（**⛔ `id(·)`**）" % TARGET)
    _orig = RV.harvest
    state = {"wrapped": 0}

    def _patched(*a, **k):
        ns, fs = _orig(*a, **k)
        cur = ns.get(TARGET)
        if cur is not None and not getattr(cur, "_wg9300", False):
            ns[TARGET] = make_wrapper(cur)
            state["wrapped"] += 1
        return ns, fs

    RV.harvest = _patched                        # 🔒 ⛔ 改生產碼·只換 driver 之模組屬性
    print("包裹之取法 ＝ 換 `run_verification.harvest` 之**模組屬性**（⛔ 改 `app.py`／`verify/` 任一檔之 bytes）")

    # 外圍函式之計數（**模組屬性**·⛔ 改其 bytes）
    import wf_f1 as _F1
    import wf_f4 as _F4
    import stepg_pipeline as _SP
    _F1.compute = make_counter(_F1.compute, "wf_f1.compute")
    _F4.compute = make_counter(_F4.compute, "wf_f4.compute")
    _F4._reshape_block = make_counter(_F4._reshape_block, "wf_f4._reshape_block")
    # 🩸 `run_verification` 係 `from stepg_pipeline import (…)` ⇒ 其名**於 import 時already-bound**
    #    ⇒ 換 `_SP` 之模組屬性對該 driver **無效**。故**二處並換**並逐處出艙其在否
    #    （⛔ 只換其一而據以報 `0`——該 `0` 將係**綁定之別**、⛔ 受詞之真）。
    _SP.run_step_g = make_counter(_SP.run_step_g, "stepg_pipeline.run_step_g（模組屬性）")
    _has_rv_bind = hasattr(RV, "run_step_g")
    if _has_rv_bind:
        RV.run_step_g = make_counter(RV.run_step_g, "run_verification.run_step_g（已綁之名）")
    print("外圍函式計數器 ＝ %s（⛔ 改其 bytes·只換模組屬性）" % sorted(ENCL))
    print("`run_verification` 是否已綁 `run_step_g` 之名 ＝ %s（⇒ 二處並換之由）" % _has_rv_bind)
    print("開跑 `run_verification.main()` … （**等待綁行程結束**·⛔ `| tail -N`）")
    sys.stdout.flush()
    t0 = time.time()
    _IN_DRIVE[0] = True
    rc = None
    err = None
    try:
        rc = RV.main()
    except SystemExit as e:
        rc = e.code
    except BaseException as e:                   # noqa: BLE001  loud·⛔ 靜默
        err = "%s: %s" % (type(e).__name__, e)
    finally:
        _IN_DRIVE[0] = False
    dt = time.time() - t0

    title("款 2 (乙)　結果")
    print("`run_verification.main()` rc ＝ %r　耗時 ＝ %.1f s　例外 ＝ %s" % (rc, dt, err or "無"))
    print("包裹實際生效次數 ＝ %d（`harvest` 有快取 ⇒ 1 即足）" % state["wrapped"])
    print("**逐閘出艙執行次數**：生產錄 ＝ **%d**　器自身 ＝ **%d**（母體已扣除自身·後者須 `0`）"
          % (len(REC), len(SELF)))
    if len(SELF) != 0:
        print("🛑 **loud**：器自身之呼叫非零 ⇒ 母體遭自我污染")

    print()
    print("── 外圍函式之執行計數（**區辨「外圍未執行」與「外圍執行而 `forced` 為偽」**）──")
    for tag in sorted(ENCL):
        print("   %-46s ＝ **%d** 次" % (tag, ENCL[tag]))

    # ── `F` 之逐site歸屬（**鍵 ＝ 呼叫端自身之框**·⛔ 其上一層）─────────────────
    files, _ = prod_files()
    S = scan_calls(TARGET, files)
    base2path = {}
    for p in files:
        base2path.setdefault(os.path.basename(p), p)
    site_of = {}
    for i, (p, form, fn, a, how, ln) in enumerate(S, 1):
        site_of[(os.path.basename(p), ln)] = ("S%d" % i, p, fn)

    if not REC:
        print()
        print("🛑 **判定組為空 ⇒ loud 拒測**（⛔ `all()` 空集恆真）——`|F| = 0` 之候選")
        F_sites = set()
    else:
        print()
        hr()
        agg = {}
        for r in REC:
            # 🩸 **本器自捕**：原式取 `chain[1]`（＝呼叫端之**呼叫端**）⇒ 七處全塌為一桶、
            #    且所印之「位」係上一層之位。`_chain()` 自 `sys._getframe(2)` 起
            #    ⇒ `chain[0]` **即呼叫端自身之框**。已改取 `chain[0]`。
            caller = r["chain"][0]
            key = (caller[1], caller[0], caller[2])
            agg.setdefault(key, []).append(r)
        F_sites = set()
        for (cf, cn, cl), rs in sorted(agg.items()):
            sid = site_of.get((cf, cl))
            if sid:
                F_sites.add(sid[0])
            print("呼叫端（**呼叫端自身之框**·`co_filename`／`co_name`）＝ 檔 `%s` :: 函式 `%s`　"
                  "⛔ 非錨·位 :%d　⇒ 對位之 AST 處 ＝ **%s**"
                  % (cf, cn, cl, sid[0] if sid else "🔴 **⛔ 對位**（loud）"))
            print("   執行次數 ＝ **%d**　side 之分布 ＝ %s　_label 之分布 ＝ %s"
                  % (len(rs), sorted({str(x["side"]) for x in rs}),
                     sorted({str(x["label"]) for x in rs})))
            print("   呼叫鏈（`co_name`@`co_filename` 序·外→內之逆）：")
            for nm, fl, lno in rs[0]["chain"][:8]:
                print("      · `%s` @ `%s`" % (nm, fl))
            print("   款 3（動態半）逐層 `f_locals` 之鍵（**二鍵並報**·鍵先自證存在）：")
            for lay in rs[0]["keys"]:
                print("      層 `%s`@`%s`:" % (lay["函式"], lay["檔"]))
                for k2, v2 in lay.items():
                    if k2 in ("函式", "檔"):
                        continue
                    print("         %-42s ＝ %s" % (k2, v2))
            hr()

    # ── `S` 對 `F` 之逐處判（**⛔ 由 CC 判「改幾處算只改該處」**）──────────────
    title("`S` ／ `F` ／ `S∖F` 之逐處判（**出艙即止**·孰為 KL 射程 `(b)` 之「該處」**由發單側裁**）")
    print("|S| ＝ **%d**（檔 %d）　|F| ＝ **%d**　|S∖F| ＝ **%d**"
          % (len(S), len({h[0] for h in S}), len(F_sites), len(S) - len(F_sites)))
    print()
    hr()
    for i, (p, form, fn, a, how, ln) in enumerate(S, 1):
        sid = "S%d" % i
        inF = sid in F_sites
        anc = anchor_for(p, ln)
        inmain, _r = in_def_main(p, ln)
        n = sum(1 for r in REC if r["chain"][0][1] == os.path.basename(p)
                and r["chain"][0][2] == ln)
        print("%s  `%s` :: `%s`" % (sid, p, fn))
        print("    字樣錨 ＝ `%s`" % anc)
        print("    ∈ F ＝ **%s**　執行次數 ＝ **%d**" % (inF, n))
        print("    落於 `def main` 內（AST 實查）＝ %s" % inmain)
        print("    頂層 `*_EXPECT` 之數（該檔）＝ **%d**　%s"
              % (len(expect_top_level(p)),
                 ("　".join("`%s`" % x for x in expect_top_level(p))) or ""))
        if not inF:
            print("    🛑 **loud 具名：本案未走·射程未定**"
                  "（⛔ 以「未執行」充「非接觸面」）")
        hr()

    print()
    print("🔒 出艙即止——`S`／`F`／逐處之判由報告承載；孰為 KL 射程 `(b)` 之「該處」**由發單側裁**。")
    return 0 if err is None else 2


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    mode = sys.argv[1] if len(sys.argv) > 1 else "static"
    print("【`W-G.9-300` 工項一｜路丙之接觸面之現查】mode ＝ %s" % mode)
    print("態 ＝ %s" % subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                                      capture_output=True, text=True).stdout.strip())
    sys.exit(run_static() if mode == "static" else run_dynamic())
