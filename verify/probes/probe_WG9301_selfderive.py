#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-301` 工項四：**自導可行性之現查**（主線·零生產碼·🛑 含停機款 `停四`）。

── 本器之地位 ────────────────────────────────────────────────────────────────
單 `§六` 令現查「`_corner_buffer_S` 之**現有形參**是否足以導出『街角第 `1` 宗之臨街向』
（＝ `_first_corner_alloc_dir(side_mid)` 之等價）」。
🛑 **本器⛔ 改生產碼一字、⛔ 驅動 `run_verification`、⛔ 擬任何改法或 diff**——**只現查**。
🛑 **⛔ 自寫第二套幾何**（`GB-48` 族）——只現查**既有原語**之可得性；
   凡須新原語者一律具名為「**不可自現有形參導出**」。

── 恆常附款之遵行 ────────────────────────────────────────────────────────────
· 母體 ＝ 生產碼 **`34`** 檔（**正面列舉**）；🆕 **其基數綁<u>外部錨</u>**（坑 `bj`）。
· 一切 `git` 呼叫**一律取 bytes**（坑 `bk`）——⛔ `text=True`。
· 頂層之取用一律 `t.body`；定義框 **二形並取**（`FunctionDef`／`AsyncFunctionDef`）。
· [必為零]之造一律**執行期組出**，其字面⛔ 落入輸出（`GB-147`）。
· 判定組為空一律 **loud 拒測**。

用法：`python verify/probes/probe_WG9301_selfderive.py`
`rc`：`0` 正常出艙／`2` **量測器紅**（判別力造不如預期 ⇒ loud 拒測）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」；**`停四` 之成否由報告承載**（本器只出艙其受詞）。
"""
import ast
import builtins
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W = 112
TGT = "_corner_buffer_S"
INJ = "_first_corner_alloc_dir"
EXTERNAL_ANCHOR = 34            # 🔒 外部錨 ＝ `§零` 閘 `7` 獨立所得（坑 `bj`）


def hr(ch="─"):
    print(ch * W)


def title(s):
    print()
    print("=" * W)
    print(s)
    print("=" * W)


def sh(args):
    """🔒 **一律取 bytes**（坑 `bk`）。"""
    return subprocess.run(args, cwd=REPO, capture_output=True)


def prod_files():
    out = sh(["git", "ls-tree", "HEAD", "--name-only", "verify/"]).stdout
    tops = sorted(x for x in out.decode("utf-8").split("\n") if x.endswith(".py"))
    return ["app.py"] + tops


def blob(path):
    r = sh(["git", "cat-file", "blob", "HEAD:" + path])
    return None if r.returncode != 0 else r.stdout.decode("utf-8")


# ══════════════════════════════════════════════════════════════════════════════
def find_defs(name, files):
    """二形並取：`FunctionDef`／`AsyncFunctionDef`。回 [(檔, node, src)]。"""
    out = []
    for p in files:
        s = blob(p)
        if s is None:
            continue
        t = ast.parse(s)
        for n in ast.walk(t):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name:
                out.append((p, n, s))
    return out


def sig_of(n):
    a = n.args
    parts = []
    pos = list(a.posonlyargs) + list(a.args)
    defs = [None] * (len(pos) - len(a.defaults)) + list(a.defaults)
    for arg, d in zip(pos, defs):
        parts.append(arg.arg + ("" if d is None else "=" + ast.unparse(d)))
    if a.vararg:
        parts.append("*" + a.vararg.arg)
    elif a.kwonlyargs:
        parts.append("*")
    for arg, d in zip(a.kwonlyargs, a.kw_defaults):
        parts.append(arg.arg + ("" if d is None else "=" + ast.unparse(d)))
    if a.kwarg:
        parts.append("**" + a.kwarg.arg)
    return parts


def param_names(n):
    a = n.args
    out = [x.arg for x in list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs)]
    if a.vararg:
        out.append(a.vararg.arg)
    if a.kwarg:
        out.append(a.kwarg.arg)
    return out


def free_names(n):
    """體內之**自由名** ＝ `Name.Load` 扣形參、扣體內 `Store`／`import`、扣 `builtins`。"""
    params = set(param_names(n))
    stores, loads = set(), []
    for x in ast.walk(n):
        if isinstance(x, ast.Name):
            if isinstance(x.ctx, ast.Store):
                stores.add(x.id)
            elif isinstance(x.ctx, ast.Load):
                loads.append(x.id)
        elif isinstance(x, (ast.Import, ast.ImportFrom)):
            for al in x.names:
                stores.add(al.asname or al.name.split(".")[0])
        elif isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef)) and x is not n:
            stores.add(x.name)
    bi = set(dir(builtins))
    seen, out = set(), []
    for nm in loads:
        if nm in params or nm in stores or nm in bi or nm in seen:
            continue
        seen.add(nm)
        out.append(nm)
    return out


def called_names(n):
    out = []
    for x in ast.walk(n):
        if isinstance(x, ast.Call):
            f = x.func
            if isinstance(f, ast.Name):
                nm = f.id
            elif isinstance(f, ast.Attribute):
                nm = ast.unparse(f)
            else:
                nm = ast.unparse(f)
            if nm not in out:
                out.append(nm)
    return out


def attr_chains(n, root):
    out = []
    for x in ast.walk(n):
        if isinstance(x, (ast.Attribute, ast.Subscript)):
            s = ast.unparse(x)
            if s.startswith(root) and s not in out:
                out.append(s)
    return out


def ns_keys(files):
    """`ns` 之鍵框：harvest 之 `ns` ＝ `app.py` 之**頂層**名（`t.body`）。"""
    s = blob("app.py")
    t = ast.parse(s)
    keys = set()
    for nd in t.body:
        if isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            keys.add(nd.name)
        elif isinstance(nd, ast.Assign):
            for tg in nd.targets:
                if isinstance(tg, ast.Name):
                    keys.add(tg.id)
        elif isinstance(nd, ast.AnnAssign) and isinstance(nd.target, ast.Name):
            keys.add(nd.target.id)
        elif isinstance(nd, (ast.Import, ast.ImportFrom)):
            for al in nd.names:
                keys.add(al.asname or al.name.split(".")[0])
    return keys


def enclosing_tests(src, line):
    t = ast.parse(src)
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
    rec(t)
    return out


FORCED_TOKENS = ("_fo_left", "_fo_right", "forced_offset", "forced")


def scan_calls(name, files):
    hits = []
    for p in files:
        s = blob(p)
        if s is None:
            continue
        t = ast.parse(s)
        for n in ast.walk(t):
            if isinstance(n, ast.Call):
                f = n.func
                ok = (isinstance(f, ast.Name) and f.id == name) or (
                    isinstance(f, ast.Subscript) and isinstance(f.value, ast.Name)
                    and f.value.id == "ns" and isinstance(f.slice, ast.Constant)
                    and f.slice.value == name)
                if ok:
                    hits.append((p, n.lineno, s))
    return hits


# ══════════════════════════════════════════════════════════════════════════════
def main():
    red = []
    files = prod_files()
    print("【`W-G.9-301` 工項四｜自導可行性之現查】")
    print("態 ＝ %s" % sh(["git", "rev-parse", "HEAD"]).stdout.decode().strip())
    print("母體（**正面列舉**）＝ `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`"
          "　基數 ＝ **%d**　外部錨（`§零` 閘 `7`）＝ **%d**　⇒ %s"
          % (len(files), EXTERNAL_ANCHOR,
             "✅ 相符" if len(files) == EXTERNAL_ANCHOR else "🔴 **相異**"))
    if len(files) != EXTERNAL_ANCHOR:
        red.append("母體基數 ≠ 外部錨")

    # ── 款 1 ──────────────────────────────────────────────────────────────────
    title("款 `1`　二函式之**定義處**與**簽章逐字**（框 ＝ AST `FunctionDef`／`AsyncFunctionDef`·二形並取）")
    D = {}
    for nm in (TGT, INJ):
        ds = find_defs(nm, files)
        D[nm] = ds
        fset = sorted({d[0] for d in ds})
        print()
        print("`%s`　**檔／處二數並報**：檔 ＝ **%d**／處 ＝ **%d**" % (nm, len(fset), len(ds)))
        for p, n, s in ds:
            print("   檔 ＝ `%s`　形 ＝ %s" % (p, type(n).__name__))
            print("   簽章逐字 ＝ `def %s(%s)`" % (nm, ", ".join(sig_of(n))))
            print("   形參名序 ＝ %r" % param_names(n))
            print("   體之列數 ＝ **%d**（`%d`-`%d`）" % (n.end_lineno - n.lineno + 1,
                                                    n.lineno, n.end_lineno))
            print("   字樣錨 ＝ `%s`" % s.split("\n")[n.lineno - 1].strip()[:88])
        if not ds:
            print("   🛑 **判定組為空 ⇒ loud 拒測**")
            red.append("`%s` 之定義處 ＝ 0" % nm)

    if red:
        print()
        print("🛑 **量測器紅**：%s ⇒ ⛔ 出艙任何判" % "／".join(red))
        return 2

    tgt_n = D[TGT][0][1]
    inj_n = D[INJ][0][1]
    TGT_PARAMS = param_names(tgt_n)
    NSK = ns_keys(files)

    # ── 款 2 ──────────────────────────────────────────────────────────────────
    title("款 `2`　二函式體內之**自由名**（框 ＝ `Name.Load` 扣形參／扣體內 `Store`／扣 `builtins`）")
    for nm, n in ((TGT, tgt_n), (INJ, inj_n)):
        fn = free_names(n)
        print()
        print("`%s` 之自由名 ＝ **%d** 個：" % (nm, len(fn)))
        for x in fn:
            print("   %-28s 於 `ns` 之鍵框內 ＝ %s" % ("`" + x + "`", x in NSK))
        print("   🔒 `ns` 之鍵框 ＝ `app.py` 之**頂層**名（`t.body`）·基數 ＝ **%d**"
              "（⛔ 模組 `__globals__`·`W-G.9-298R` 已證 `ns` 係純 `dict`）" % len(NSK))

    # ── 款 3 ──────────────────────────────────────────────────────────────────
    title("款 `3`　🔑 **所需輸入集 `R`**（`%s` 求值所<u>實需</u>之輸入）" % INJ)
    R_params = param_names(inj_n)
    R_free = free_names(inj_n)
    print("`R` ＝ 其**形參** %r ＋ 其體所消費之**自由名** %r" % (R_params, R_free))
    print()
    print("逐名之**來源**（⛔ 判「可導」·只出艙來源）：")
    hr()
    src_map = {}
    for x in R_params + R_free:
        in_tgt = x in TGT_PARAMS
        in_ns = x in NSK
        s = ("`%s` 之形參" % TGT) if in_tgt else ("`ns`" if in_ns else "**二者皆非**")
        src_map[x] = (in_tgt, in_ns)
        print("   %-24s ⇒ 於 `%s` 之形參 ＝ %-5s／於 `ns` ＝ %-5s ⇒ 來源 ＝ %s"
              % ("`" + x + "`", TGT, in_tgt, in_ns, s))
    hr()
    print("`%s` 之現有形參（受詞）＝ %r" % (TGT, TGT_PARAMS))

    # ── 款 4 ──────────────────────────────────────────────────────────────────
    title("款 `4`　🔑 `side_mid` 之等價量於 `%s` 內之可得性（**只現查既有原語**·⛔ 自寫第二套幾何）" % TGT)
    prims = called_names(tgt_n)
    print("`%s` 體內**已調用**之名 ＝ %r" % (TGT, prims))
    print()
    print("其中屬 `ns` 之鍵者（＝ 既有原語·可於函式體內取用）：")
    for p in prims:
        if p in NSK:
            ds = find_defs(p, files)
            if ds:
                pn = ds[0][1]
                rets = []
                for x in ast.walk(pn):
                    if isinstance(x, ast.Return) and x.value is not None:
                        r = ast.unparse(x.value)
                        if r not in rets:
                            rets.append(r)
                print("   `%s`　簽章 ＝ `def %s(%s)`" % (p, p, ", ".join(sig_of(pn))))
                print("      回傳結構（逐字·去重）＝ %r" % rets[:6])
    print()
    print("🔑 **`%s` 所消費之側界資料**（其 `Attribute`／`Subscript` 鏈·逐字）：" % INJ)
    for c in attr_chains(inj_n, "_st_fc") + attr_chains(inj_n, "_sd") + attr_chains(inj_n, "_slbs"):
        print("   `%s`" % c)
    print()
    key_lit = [ast.unparse(x) for x in ast.walk(inj_n)
               if isinstance(x, ast.Constant) and isinstance(x.value, str)]
    print("`%s` 體內之**字串常數**（＝ 其查表之鍵·逐字）＝ %r" % (INJ, key_lit))
    print()
    print("🔑 **本街廓該側之側界線及其中點，是否在既有原語之回傳結構中**：")
    hit = []
    for p in prims:
        if p not in NSK:
            continue
        ds = find_defs(p, files)
        if not ds:
            continue
        body = ast.unparse(ds[0][1])
        if ("side_line" in body) or ("SIDE_LINE" in body) or ("f3_cad_side_lines_by_side" in body):
            hit.append(p)
    print("   既有原語中，其體內含 `side_line`／`SIDE_LINE`／`f3_cad_side_lines_by_side` 者 ＝ %r"
          % hit)
    print("   ⇒ %s" % ("🔴 **無**——側界資料⛔ 在既有原語之回傳結構中" if not hit
                       else "有（逐項具名於上）"))

    # ── 款 4′：`_label` 之實參（**唯一之「標籤狀」形參**·⛔ 推定）────────────
    title("款 `4′`　`_label`（`%s` 唯一之「標籤狀」形參）之**實參逐字**（⛔ 推定·AST 實查）" % TGT)
    print("🔑 其由：`%s` 之 docstring **逐字**令「以 `side_mid` 幾何反查 SIDE_LINE"
          "——⛔ **不靠任何字串標籤**」" % INJ)
    print("   ⇒ 「以 `_label` 查表」之路，**其禁止已寫在受詞函式自身之 docstring 內**；")
    print("   本款只現查該實參**實際為何**，⛔ 判其可否用。")
    print()
    for i, (p, ln, s) in enumerate(scan_calls(TGT, files), 1):
        t = ast.parse(s)
        arg = None
        for nd in ast.walk(t):
            if isinstance(nd, ast.Call) and nd.lineno == ln:
                for kw in nd.keywords:
                    if kw.arg == "_label":
                        arg = ast.unparse(kw.value)
                if arg is None and len(nd.args) >= 8:
                    arg = ast.unparse(nd.args[7])
                break
        print("   S%d `%-26s` 之 `_label` 實參逐字 ＝ %s"
              % (i, p, ("`" + arg + "`") if arg is not None else "**⛔ 傳**（取預設 `''`）"))

    # ── 款 5 ──────────────────────────────────────────────────────────────────
    title("款 `5`　**非 `forced` 呼叫端之復驗**（🔒 本批**獨立重得**·⛔ 轉引 `W-G.9-300R`）")
    S = scan_calls(TGT, files)
    print("`S` ＝ **%d** 處／**%d** 檔（框 ＝ AST `Call`·二形並取）"
          % (len(S), len({x[0] for x in S})))
    nonforced = []
    for i, (p, ln, s) in enumerate(S, 1):
        tests = enclosing_tests(s, ln)
        h = [t for t in tests if any(tok in t[1] for tok in FORCED_TOKENS)]
        if not h:
            nonforced.append(i)
        print("   S%d `%-26s` 命中之外圍 `test` ＝ %s"
              % (i, p, (h[0][0] + " `" + h[0][1] + "`") if h else "🔴 **無**"))
    print()
    print("⇒ **非 `forced` 之呼叫端 ＝ %d／%d**（須 `0`／`%d`）"
          % (len(nonforced), len(S), len(S)))
    dl = [n for n in ast.walk(ast.parse(blob("app.py")))
          if isinstance(n, ast.FunctionDef) and n.name == TGT][0].lineno
    ctl = enclosing_tests(blob("app.py"), dl)
    ctl_forced = any(any(tok in t for tok in FORCED_TOKENS) for _k, t in ctl)
    print("判別力[必為否] `def %s` 之定義列：外圍 `If`／`IfExp` ＝ **%d** 個 ⇒ 判 ＝ %s（須「否」）"
          % (TGT, len(ctl), "🔴 是" if ctl_forced else "否"))

    # ── 款 6 ──────────────────────────────────────────────────────────────────
    title("款 `6`　判別力四造")
    c1 = len(D[TGT]) >= 1 and len(D[INJ]) >= 1
    print("[必非零] 二函式之定義處 `≥ 1` ⇒ `%s` ＝ %d／`%s` ＝ %d ⇒ %s"
          % (TGT, len(D[TGT]), INJ, len(D[INJ]), "✅" if c1 else "🔴"))
    c2 = len(files) == EXTERNAL_ANCHOR
    print("[必為 `%d`] 母體基數之**外部錨**（坑 `bj`）⇒ %d ⇒ %s"
          % (EXTERNAL_ANCHOR, len(files), "✅" if c2 else "🔴"))
    fake = "_" + "".join(["corner", "buffer"]) + "_nosuch_" + str(int(time.time()))
    c3 = len(find_defs(fake, files)) == 0
    print("[必為零] 一**執行期組出**之人造函式名（字面⛔ 出艙）之定義處 ＝ %d ⇒ %s"
          % (len(find_defs(fake, files)), "✅" if c3 else "🔴"))
    c4 = INJ in NSK
    print("[必真] `%s` 在 `ns` 之鍵 ＝ %s ⇒ %s" % (INJ, c4, "✅" if c4 else "🔴"))
    if not (c1 and c2 and c3 and c4):
        red.append("判別力四造")

    # ── 停四之受詞（**只出艙·判由報告承載**）────────────────────────────────
    title("🛑 `停四` 之**受詞**（本器只出艙·其成否之判由報告承載）")
    print("`停四` 逐字：款 `3` 之 `R` 中**有任一名**既⛔ 在 `%s` 之現有形參內、"
          "亦⛔ 可自其現有形參經**既有原語**導出（款 `4`）⇒ 停、上呈。" % TGT)
    print()
    for x in R_params:
        in_tgt, in_ns = src_map[x]
        print("   `R` 之形參 `%s`：於 `%s` 之現有形參 ＝ **%s**" % (x, TGT, in_tgt))
    print()
    print("   既有原語之回傳結構含側界資料者 ＝ %r（款 `4`）" % hit)
    print("   `%s` 查表之鍵（字串常數）＝ %r" % (INJ, key_lit))

    print()
    if red:
        print("🛑 **量測器紅**：%s ⇒ loud 拒測·⛔ 出艙任何判" % "／".join(red))
        return 2
    print("✅ 判別力四造全數成立 ⇒ 本器非恆綠亦非恆紅")
    print("🔒 **出艙即止**——⛔ 擬任何改法或 diff；`停四` 之成否與其處置**由報告承載**。")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
