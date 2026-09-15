#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-302` 工項二：**側界資料之來源現查**（主線·零生產碼·🛑 含二停機款 `停五`／`停六`）。

── 本器之地位 ────────────────────────────────────────────────────────────────
單 `§四-1` 逐字：本項**⛔ 重問** `停四` 之事，只問一新受詞——
**生產態中 `side_mid`（側界中點）究竟自何處取得、其表以何為鍵、於 `_corner_buffer_S` 之體內
是否可達且可正確取本街廓者。**
🛑 **⛔ 判「可施」或「不可施」**——只出艙；⛔ 擬任何改法或 diff。
🛑 **⛔ 改生產碼一字、⛔ 驅動 `run_verification`。**

── 恆常附款之遵行 ────────────────────────────────────────────────────────────
· 🆕 **母體一律以<u>產生指令</u>界定**（`自誤 406` 攔法 ②）——⛔ 取單內之列舉。
· 母體基數綁**外部錨**（坑 `bj`）；一切 `git` 呼叫**取 bytes**（坑 `bk`）。
· 四字樣**分列並報**（⛔ 合併）；框無 `^` 錨者**二數並報**；頂層取 `t.body`。
· [必為零]之造一律**執行期組出**，其字面⛔ 落入輸出（`GB-147`）。
· 判定組為空一律 **loud 拒測**。

用法：`python verify/probes/probe_WG9302_sidesrc.py`
`rc`：`0` 正常出艙／`2` **量測器紅**（判別力造不如預期 ⇒ loud 拒測）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」；`停五`／`停六` 之成否由**報告**承載（本器只出艙其受詞）。
"""
import ast
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = 112
KEY = "f3_cad_side_lines_by_side"
TGT = "_corner_buffer_S"
INJ = "_first_corner_alloc_dir"
EXTERNAL_ANCHOR = 34
FOUR = (KEY, "side_line", "SIDE_LINE", "side_mid")
FORCED_TOKENS = ("_fo_left", "_fo_right", "forced_offset", "forced")


def hr(ch="─"):
    print(ch * W)


def title(s):
    print()
    print("=" * W)
    print(s)
    print("=" * W)


def sh(a):
    """🔒 **一律取 bytes**（坑 `bk`）。"""
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True)


def prod_files():
    """🔒 母體之**產生指令** ＝ `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`。"""
    out = sh(["ls-tree", "HEAD", "--name-only", "verify/"]).stdout.decode("utf-8")
    return ["app.py"] + sorted(x for x in out.split("\n") if x.endswith(".py"))


def blob(p):
    r = sh(["cat-file", "blob", "HEAD:" + p])
    return None if r.returncode != 0 else r.stdout.decode("utf-8")


def ns_keys_with_nodes():
    """🔒 `ns` 之鍵框之**產生指令** ＝ `app.py` 之 `t.body` 頂層名（`W-G.9-298R` 已證 `ns` 係純 `dict`）。"""
    s = blob("app.py")
    t = ast.parse(s)
    keys = {}
    for nd in t.body:
        if isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef)):
            keys[nd.name] = nd
        elif isinstance(nd, ast.ClassDef):
            keys[nd.name] = nd
        elif isinstance(nd, ast.Assign):
            for tg in nd.targets:
                if isinstance(tg, ast.Name):
                    keys.setdefault(tg.id, nd)
        elif isinstance(nd, ast.AnnAssign) and isinstance(nd.target, ast.Name):
            keys.setdefault(nd.target.id, nd)
        elif isinstance(nd, (ast.Import, ast.ImportFrom)):
            for al in nd.names:
                keys.setdefault(al.asname or al.name.split(".")[0], nd)
    return keys, s


def func_stack(tree, line):
    out = []

    def rec(n):
        for ch in ast.iter_child_nodes(n):
            if hasattr(ch, "lineno") and hasattr(ch, "end_lineno") \
                    and ch.lineno <= line <= ch.end_lineno:
                if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out.append(ch.name)
                rec(ch)
    rec(tree)
    return ".".join(out) or "<模組層>"


def enclosing_loops(tree, line):
    out = []

    def rec(n):
        for ch in ast.iter_child_nodes(n):
            if hasattr(ch, "lineno") and hasattr(ch, "end_lineno") \
                    and ch.lineno <= line <= ch.end_lineno:
                if isinstance(ch, ast.For):
                    out.append(("For", ast.unparse(ch.target), ast.unparse(ch.iter)))
                elif isinstance(ch, ast.While):
                    out.append(("While", "—", ast.unparse(ch.test)))
                rec(ch)
    rec(tree)
    return out


def enclosing_tests(src, line):
    t = ast.parse(src)
    out = []

    def rec(n):
        for ch in ast.iter_child_nodes(n):
            if hasattr(ch, "lineno") and hasattr(ch, "end_lineno") \
                    and ch.lineno <= line <= ch.end_lineno:
                if isinstance(ch, ast.If):
                    out.append(("If", ast.unparse(ch.test)))
                elif isinstance(ch, ast.IfExp):
                    out.append(("IfExp", ast.unparse(ch.test)))
                rec(ch)
    rec(t)
    return out


def main():
    red = []
    files = prod_files()
    print("【`W-G.9-302` 工項二｜側界資料之來源現查】")
    print("態 ＝ %s" % sh(["rev-parse", "HEAD"]).stdout.decode().strip())
    print("母體（**產生指令** ＝ `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`）"
          "　基數 ＝ **%d**　外部錨（`§零` 閘 `7`）＝ **%d** ⇒ %s"
          % (len(files), EXTERNAL_ANCHOR,
             "✅ 相符" if len(files) == EXTERNAL_ANCHOR else "🔴 **相異**"))
    if len(files) != EXTERNAL_ANCHOR:
        red.append("母體基數 ≠ 外部錨")

    NSK, APPSRC = ns_keys_with_nodes()

    # ══ 款 1 ════════════════════════════════════════════════════════════════
    title("款 `1`　**側界符號之全量現查**（母體 ＝ `ns` 之全部鍵·**四字樣分列並報**·⛔ 合併）")
    print("🔒 母體之**產生指令** ＝ `app.py` 之 `ast.parse(...).body` 頂層名之集　基數 ＝ **%d**"
          % len(NSK))
    print("   （🛑 **本批自行重得**·`W-G.9-301R` 實測 `286` ⇒ %s）"
          % ("相符" if len(NSK) == 286 else "**相異·照實出艙**"))
    print()
    for tok in FOUR:
        hits = []
        for k, nd in NSK.items():
            if not isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            body = ast.unparse(nd)
            if tok in body:
                hits.append(k)
        print("── 字樣 `%s` ── 命中之鍵 ＝ **%d** 個（**全量列舉**·⛔ 只報基數）：" % (tok, len(hits)))
        for h in sorted(hits):
            print("      `%s`" % h)
        if not hits:
            print("      **空**")
    fake_tok = "f3_cad_" + "".join(["nosuch", str(int(time.time()))]) + "_by_side"
    nf = sum(1 for k, nd in NSK.items()
             if isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef))
             and fake_tok in ast.unparse(nd))
    print()
    print("判別力[必為零] 一**執行期組出**之人造字樣（字面⛔ 出艙）於全母體命中 ＝ **%d** ⇒ %s"
          % (nf, "✅" if nf == 0 else "🔴"))

    # ══ 款 2 ════════════════════════════════════════════════════════════════
    title("款 `2`　🔑 `%s` 之全部**寫入處**與**讀取處**（**三形分列並報** ＋ 文字層對照）" % KEY)
    forms = {"形甲 Subscript.slice 為該常數": [],
             "形乙 Assign 之目標含之": [],
             "形丙 .get(<該常數>) 之 Call": []}
    txt_total = 0
    per_file_txt = {}
    allsites = []
    for p in files:
        s = blob(p)
        if s is None:
            continue
        c = sum(1 for l in s.split("\n") if KEY in l)
        if c:
            per_file_txt[p] = c
        txt_total += c
        t = ast.parse(s)
        for n in ast.walk(t):
            if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) \
                    and n.slice.value == KEY:
                kind = "寫入" if isinstance(n.ctx, ast.Store) else "讀取"
                forms["形甲 Subscript.slice 為該常數"].append((p, n.lineno, kind, n))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.func.attr == "get" and n.args \
                    and isinstance(n.args[0], ast.Constant) and n.args[0].value == KEY:
                forms["形丙 .get(<該常數>) 之 Call"].append((p, n.lineno, "讀取", n))
            if isinstance(n, ast.Assign):
                for tg in n.targets:
                    if isinstance(tg, ast.Subscript) and isinstance(tg.slice, ast.Constant) \
                            and tg.slice.value == KEY:
                        forms["形乙 Assign 之目標含之"].append((p, n.lineno, "寫入", n))
    for fn, lst in forms.items():
        print("   %-34s 處 ＝ **%d**／檔 ＝ **%d**" % (fn, len(lst), len({x[0] for x in lst})))
    uniq = sorted({(p, ln) for lst in forms.values() for (p, ln, _k, _n) in lst})
    print("   ⇒ 三形之**聯集** ＝ **%d** 處／**%d** 檔" % (len(uniq), len({p for p, _ in uniq})))
    print("   **文字層列框** ＝ **%d** 列／**%d** 檔（**二數並報**）" % (txt_total, len(per_file_txt)))
    for p, c in sorted(per_file_txt.items()):
        print("      %-36s %d 列" % (p, c))
    if txt_total != len(uniq):
        print("   🛑 **loud 具名：二數相異**（差 ＝ %d）——其成因逐項：" % (txt_total - len(uniq)))
        for p in files:
            s = blob(p)
            if s is None:
                continue
            for j, l in enumerate(s.split("\n"), 1):
                if KEY in l and (p, j) not in uniq:
                    print("      · `%s` ⛔ 三形之列：`%s`" % (p, l.strip()[:82]))
    print()
    hr()
    for lst in forms.values():
        for (p, ln, kind, n) in lst:
            key2 = (p, ln, kind)
            if key2 in [(a, b, c) for a, b, c, _ in allsites]:
                continue
            allsites.append((p, ln, kind, n))
    seen = set()
    for (p, ln, kind, n) in sorted(allsites, key=lambda x: (x[0], x[1])):
        if (p, ln) in seen:
            continue
        seen.add((p, ln))
        s = blob(p)
        anc = s.split("\n")[ln - 1].strip()
        print("`%s` :: `%s`　**%s**" % (p, func_stack(ast.parse(s), ln), kind))
        print("   字樣錨（⛔ 行號為錨）＝ `%s`" % anc[:92])
        print("   ⛔ 非錨·當態 blob 之位 ＝ :%d" % ln)
    hr()

    # ══ 款 3 ════════════════════════════════════════════════════════════════
    title("款 `3`　🔑 其表之**鍵結構**逐層（AST 之 `Subscript`／`Assign`／`.get` 鏈**逐字**·⛔ 讀來像是）")
    writes = [(p, ln, n) for (p, ln, k, n) in allsites if k == "寫入"]
    print("**寫入處** ＝ **%d** 處：" % len(writes))
    for (p, ln, n) in writes:
        s = blob(p)
        print("   `%s` :: `%s`" % (p, func_stack(ast.parse(s), ln)))
        print("      賦值逐字 ＝ `%s`" % ast.unparse(n).replace("\n", " ")[:100])
    print()
    print("**讀取處之鍵鏈逐層**（自讀取處之 AST 逐層取其鍵）：")
    reads = [(p, ln, n) for (p, ln, k, n) in allsites if k == "讀取"]
    for (p, ln, n) in reads:
        s = blob(p)
        t = ast.parse(s)
        # 取包含該讀取之最小完整 statement，逐字出艙
        stmt = None
        for nd in ast.walk(t):
            if isinstance(nd, ast.stmt) and hasattr(nd, "lineno") \
                    and nd.lineno <= ln <= (nd.end_lineno or nd.lineno):
                if stmt is None or nd.lineno > stmt.lineno:
                    stmt = nd
        u = ast.unparse(stmt).replace("\n", " ") if stmt else "—"
        print("   `%s` :: `%s`" % (p, func_stack(t, ln)))
        print("      敘述逐字 ＝ `%s`" % u[:126])
    print()
    print("🔑 **其鍵是否含街廓層**（`blk_label` 或等價）——**逐處之第二層鍵逐字**：")
    for (p, ln, n) in reads:
        s = blob(p)
        t = ast.parse(s)
        stmt = None
        for nd in ast.walk(t):
            if isinstance(nd, ast.stmt) and hasattr(nd, "lineno") \
                    and nd.lineno <= ln <= (nd.end_lineno or nd.lineno):
                if stmt is None or nd.lineno > stmt.lineno:
                    stmt = nd
        u = ast.unparse(stmt).replace("\n", " ") if stmt else ""
        # 取該敘述中緊隨該常數之後的 `.get(X)` 或 `[X]`
        import re as _re
        m = _re.search(r"%s['\"]\s*,?\s*[^)]*\)\s*(?:or\s*\{\})?\s*\)?\s*\.get\(([^,)]+)"
                       % _re.escape(KEY), u)
        m2 = _re.search(r"%s['\"]\][^\[]*\[([^\]]+)\]" % _re.escape(KEY), u)
        second = m.group(1).strip() if m else (m2.group(1).strip() if m2 else "**無第二層**")
        print("   `%-26s` :: `%-22s` ⇒ 第二層鍵逐字 ＝ `%s`"
              % (p, func_stack(t, ln)[:22], second))

    # ══ 款 3′ ═══════════════════════════════════════════════════════════════
    title("款 `3′`　🔑 **消費端之鍵鏈逐層**（`%s` 體內·AST `For`／`Subscript`／`.get` **逐字**）" % INJ)
    if isinstance(inj_pre := NSK.get(INJ), (ast.FunctionDef, ast.AsyncFunctionDef)):
        print("**`For` 之 `target`／`iter` 逐字**（＝ 其逐層之走法）：")
        for n in ast.walk(inj_pre):
            if isinstance(n, ast.For):
                print("   `for %s in %s:`" % (ast.unparse(n.target), ast.unparse(n.iter)))
        print()
        print("**`Subscript`／`.get` 之鍵逐字**（去重·序同 AST 之走訪）：")
        seen_k = []
        for n in ast.walk(inj_pre):
            if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant):
                u = repr(n.slice.value)
                if u not in seen_k:
                    seen_k.append(u)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.func.attr == "get" and n.args:
                u = ast.unparse(n.args[0])
                if u not in seen_k:
                    seen_k.append(u)
        for u in seen_k:
            print("   %s" % u)
        print()
        print("🔑 **其是否以<u>街廓標籤</u>索引** ＝ 見上 `for` 之 `target`；"
              "若其為**遍歷全表**而以幾何比對定位，則**⛔ 以標籤索引**（照實出艙·⛔ 判其可施）")

    # ══ 款 4 ════════════════════════════════════════════════════════════════
    title("款 `4`　🔑 **寫入之時機**（外圍 `For`／`While` 之 `target` 與 `iter` **逐字**）"
          "　🔑 **此即 `停五` 之受詞**")
    for (p, ln, n) in writes:
        s = blob(p)
        t = ast.parse(s)
        loops = enclosing_loops(t, ln)
        print("   `%s` :: `%s`" % (p, func_stack(t, ln)))
        if loops:
            for (kind, tg, it) in loops:
                print("      外圍 %-5s target ＝ `%s`　iter ＝ `%s`" % (kind, tg, it[:64]))
        else:
            print("      外圍 `For`／`While` ＝ **無**（⇒ **⛔ 在逐街廓迴圈內**）")
        print("      ⇒ 其賦值之受詞 ＝ **整表一次賦值**（逐字見款 `3`）"
              if not loops else "      ⇒ 其於每次迭代之行為須逐字判（見上）")

    # ══ 款 5 ════════════════════════════════════════════════════════════════
    title("款 `5`　🔑 `_st_fc` 之可達性（**三態分列**）　🔑 **此即 `停六` 之受詞**")
    inj = NSK.get(INJ)
    st_fc_assign = []
    if isinstance(inj, (ast.FunctionDef, ast.AsyncFunctionDef)):
        for n in ast.walk(inj):
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                for al in n.names:
                    if (al.asname or al.name) == "_st_fc" or al.asname == "_st_fc":
                        st_fc_assign.append(ast.unparse(n))
    print("`_st_fc` 之**賦值逐字**（其為何物）＝ %r" % st_fc_assign)
    print("`_st_fc` 在 `ns` 之鍵框內 ＝ **%s**" % ("_st_fc" in NSK))
    print()
    print("**三態分列**：")
    s1 = "_st_fc" in NSK
    print("   態① **在 `ns`** ＝ %s" % s1)
    alt = []
    for k, nd in NSK.items():
        if isinstance(nd, (ast.Import, ast.ImportFrom)):
            for al in nd.names:
                if al.name.split(".")[0] == "streamlit":
                    alt.append((k, ast.unparse(nd)))
    print("   態② **⛔ 在 `ns` 而可自他途** ＝ %s" % (bool(alt) and not s1))
    for k, u in alt:
        print("        `ns` 之鍵 `%s`　其頂層敘述逐字 ＝ `%s`" % (k, u))
    print("   態③ **⛔ 可達** ＝ %s" % (not s1 and not alt))
    print()
    print("🔒 **`_corner_buffer_S` 之體內是否可解**（框 ＝ `app.py` 頂層名之集·⛔ 模組 `__globals__`）：")
    tgt_nd = NSK.get(TGT)
    tgt_body_names = set()
    if isinstance(tgt_nd, (ast.FunctionDef, ast.AsyncFunctionDef)):
        for n in ast.walk(tgt_nd):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                tgt_body_names.add(n.id)
    for k, _u in alt:
        print("   名 `%s` 於 `ns` 之鍵框內 ＝ **%s**（⇒ `%s` 體內該名可經 `__globals__`(=`ns`) 解析）"
              % (k, k in NSK, TGT))
        print("   （併記·⛔ 判其可施）`%s` 體內現有之 `Name.Load` 是否已含 `%s` ＝ %s"
              % (TGT, k, k in tgt_body_names))

    # ══ 款 6 ════════════════════════════════════════════════════════════════
    title("款 `6`　`%s` 之**接觸面**（定義處 ＋ 全部呼叫端·AST **二形並取**·本批**只量**）" % INJ)
    defs, calls = [], []
    for p in files:
        s = blob(p)
        if s is None:
            continue
        t = ast.parse(s)
        for n in ast.walk(t):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == INJ:
                defs.append((p, n.lineno))
            if isinstance(n, ast.Call):
                f = n.func
                ok = (isinstance(f, ast.Name) and f.id == INJ) or (
                    isinstance(f, ast.Subscript) and isinstance(f.value, ast.Name)
                    and f.value.id == "ns" and isinstance(f.slice, ast.Constant)
                    and f.slice.value == INJ)
                if ok:
                    calls.append((p, n.lineno, s))
    print("**定義處**：檔 ＝ **%d**／處 ＝ **%d**" % (len({x[0] for x in defs}), len(defs)))
    for p, ln in defs:
        print("   `%s`　字樣錨 ＝ `%s`" % (p, blob(p).split("\n")[ln - 1].strip()[:78]))
    print("**呼叫端**：檔 ＝ **%d**／處 ＝ **%d**" % (len({x[0] for x in calls}), len(calls)))
    if not calls:
        print("   🛑 **判定組為空 ⇒ loud 拒測**（⛔ `all()` 空集恆真）——`%s` 之呼叫端 ＝ **0**" % INJ)
    for p, ln, s in calls:
        tests = enclosing_tests(s, ln)
        h = [t for t in tests if any(tok in t[1] for tok in FORCED_TOKENS)]
        print("   `%s` :: `%s`" % (p, func_stack(ast.parse(s), ln)))
        print("      字樣錨 ＝ `%s`" % s.split("\n")[ln - 1].strip()[:78])
        print("      外圍守衛 `test` 逐字 ＝ %s"
              % ([t[0] + " `" + t[1] + "`" for t in tests] or "**無**"))
        print("      其中命中 `forced` 旗字樣者 ＝ %s" % ([t[1] for t in h] or "**無**"))
    if defs:
        dl = defs[0][1]
        ctl = enclosing_tests(blob(defs[0][0]), dl)
        print()
        print("判別力[必為否] `def %s` 之定義列：外圍 `If`／`IfExp` ＝ **%d** 個 ⇒ 判 ＝ %s（須「否」）"
              % (INJ, len(ctl),
                 "🔴 是" if any(any(tok in t for tok in FORCED_TOKENS) for _k, t in ctl) else "否"))

    # ══ 款 7 ════════════════════════════════════════════════════════════════
    title("款 `7`　判別力四造")
    c1 = len(uniq) >= 1
    print("[必非零] 款 `2` 之處數 `≥ 1` ⇒ **%d** ⇒ %s" % (len(uniq), "✅" if c1 else "🔴"))
    c2 = len(files) == EXTERNAL_ANCHOR
    print("[必為 `%d`] 母體基數之**外部錨**（坑 `bj`）⇒ **%d** ⇒ %s"
          % (EXTERNAL_ANCHOR, len(files), "✅" if c2 else "🔴"))
    c3 = nf == 0
    print("[必為零] **執行期組出**之人造字樣於款 `1` 之框下命中 ⇒ **%d** ⇒ %s" % (nf, "✅" if c3 else "🔴"))
    c4 = INJ in NSK
    print("[必真] `%s` 在 `ns` 之鍵 ＝ **%s** ⇒ %s" % (INJ, c4, "✅" if c4 else "🔴"))
    if not (c1 and c2 and c3 and c4):
        red.append("判別力四造")

    # ══ 停機款之受詞 ═══════════════════════════════════════════════════════
    title("🛑 二停機款之**受詞**（本器只出艙·其成否之判由報告承載）")
    print("`停五`（鍵結構·**二合取項須分列**）：")
    print("   合取 `(i)` 鍵結構**⛔ 含街廓層** ⇒ 見款 `3` 之第二層鍵逐字")
    print("   合取 `(ii)` 寫入**不隨街廓更新** ⇒ 見款 `4` 之外圍迴圈逐字")
    print()
    print("`停六`（可達性）：款 `5` 判 `_st_fc` 於 `%s` 之體內**⛔ 可達** ⇒ 見款 `5` 之三態" % TGT)

    print()
    if red:
        print("🛑 **量測器紅**：%s ⇒ loud 拒測·⛔ 出艙任何判" % "／".join(red))
        return 2
    print("✅ 判別力四造全數成立 ⇒ 本器非恆綠亦非恆紅")
    print("🔒 **出艙即止**——⛔ 判「可施」或「不可施」·⛔ 擬任何改法或 diff。")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
