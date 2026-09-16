#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_WG9305_issuer_static.py — 發單側（claude.ai）出 `W-G.9-305` 前之自擬靜態現查器·原封入倉（自誤 331 之體例）

🔒 地位：發單側自擬框·**⛔ 正典**。入倉之唯一目的 ＝ 使受單側可逐字重跑發單側於單內所引之數（自誤 409）。
🔒 唯讀：只以 `git cat-file blob <rev>:<path>` 取 bytes（坑 bk）；⛔ 寫任何 tracked 檔；⛔ import 生產路徑。
用法：python verify/probes/probe_WG9305_issuer_static.py [<rev>]      （預設 HEAD）

節 A：`app.py :: _solve_G_one` 之受詞出現普查——二種「出現」之定義並報
  A1 ＝ `W-G.9-304R §六-1` 之定義（僅 `ast.Name` 節點 ＋ `ast.arg` 節點）之 (父節點型別, 欄位, ctx)
  A2 ＝ **構造上之定義**：AST 內**每一節點之每一欄位值**，凡為 `str` 且逐字等於受詞者皆為一「出現」
        （含 `Constant.value`／`keyword.arg`／`Attribute.attr`／`alias.name`／`Global.names` 等·⛔ 以型別清單界定）
節 B：`verify/stepg_pipeline.py :: _run_step_g_impl` 之巢狀作用域與七名之所屬作用域

🔒 本器之自限（loud）：
  ① 「出現」＝ 逐字相等（⛔ 子字串）；執行期組出之字串、變數鍵之 `getattr`、`exec` 靜態不可見 ⇒ 由動態款承擔。
  ② 節 B 之「所屬作用域」以具名函式／lambda 計；comprehension 作用域併入其外層具名函式——其受影響之數逐名出艙。
  ③ 位序（行號）只供比較先後，⛔ 為錨。
"""
import ast, sys, subprocess, collections

sys.stdout.reconfigure(encoding="utf-8", newline="\n")   # 坑 bn：`newline` ⛔ 可省

REV = sys.argv[1] if len(sys.argv) > 1 else "HEAD"


def blob(path):
    r = subprocess.run(["git", "cat-file", "blob", f"{REV}:{path}"], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"STOP: cat-file rc={r.returncode} for {path}")
    return r.stdout.decode("utf-8")


def fdef(tree, name):
    hits = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name]
    return hits


def parents(root):
    P = {}
    for p in ast.walk(root):
        for f, v in ast.iter_fields(p):
            for c in (v if isinstance(v, list) else [v]):
                if isinstance(c, ast.AST):
                    P[id(c)] = (p, f)
    return P


def ctxname(n):
    return type(n.ctx).__name__ if hasattr(n, "ctx") else "-"


def census_A1(fn, names):
    P = parents(fn)
    C = collections.Counter()
    for n in ast.walk(fn):
        if isinstance(n, ast.Name) and n.id in names:
            p, f = P[id(n)]; C[(type(p).__name__, f, ctxname(n))] += 1
        elif isinstance(n, ast.arg) and n.arg in names:
            p, f = P[id(n)]; C[(type(p).__name__, f, "-")] += 1
    return C


def census_A2(fn, names):
    """每一節點之每一欄位值逐一比對（構造上窮舉·⛔ 型別清單）。
    節點形出現（其欄位屬於 Name/Constant 等葉節點）⇒ 以其**父節點**之 (型別, 欄位) 為形；
    其餘（識別字為某節點之 str 欄位，如 keyword.arg／arg.arg）⇒ 以 (擁有者型別.欄位, 其父型別, 父欄位) 為形。"""
    P = parents(fn)
    C = collections.Counter()
    for owner in ast.walk(fn):
        for field, val in ast.iter_fields(owner):
            for v in (val if isinstance(val, list) else [val]):
                if not (isinstance(v, str) and v in names):
                    continue
                par, pf = P.get(id(owner), (None, "-"))
                pt = type(par).__name__ if par is not None else "(root)"
                C[(f"{type(owner).__name__}.{field}", pt, pf, ctxname(owner))] += 1
    return C


def main():
    print("=" * 100)
    print(f"【probe_WG9305_issuer_static】rev = {REV}")
    ls = subprocess.run(["git", "rev-parse", REV], capture_output=True).stdout.decode().strip()
    print(f"rev-parse = {ls}")
    print("=" * 100)

    # ── 外部錨（坑 bj）──
    tops = subprocess.run(["git", "ls-tree", REV, "--name-only", "verify/"], capture_output=True).stdout.decode("utf-8").split("\n")
    prod = sorted([t for t in tops if t.endswith(".py")] + ["app.py"])
    print(f"[錨] git ls-tree {REV} --name-only verify/ ⋂ *.py ＋ app.py ⇒ {len(prod)} 檔")

    # ── 節 A ──
    app = ast.parse(blob("app.py"))
    d = fdef(app, "_solve_G_one")
    print(f"\n── 節 A　app.py :: _solve_G_one（定義處 {len(d)}）──")
    if len(d) != 1:
        raise SystemExit("STOP: _solve_G_one 定義處 ≠ 1")
    fn = d[0]
    names = {"allocation_dir", "_alloc_dir_used", "_r"}
    print(f"受詞名集（逐字·承 W-G.9-304R §六-1）＝ {sorted(names)}")
    a1 = census_A1(fn, names); a2 = census_A2(fn, names)
    print(f"A1（Name∪arg 節點）：出現 {sum(a1.values())}／相異形 {len(a1)}")
    for k, v in sorted(a1.items(), key=lambda x: (-x[1], x[0])):
        print(f"   {v:>3}  {k}")
    print(f"A2（每一欄位值·構造上）：出現 {sum(a2.values())}／相異形 {len(a2)}")
    for k, v in sorted(a2.items(), key=lambda x: (-x[1], x[0])):
        print(f"   {v:>3}  {k}")
    a2_nodeform = collections.Counter()
    for (own, pt, pf, cx), v in a2.items():
        if own in ("Name.id",):
            a2_nodeform[(pt, pf, cx)] += v
        elif own == "arg.arg":
            a2_nodeform[(pt, pf, "-")] += v
    extra = {k: v for k, v in a2.items() if k[0] not in ("Name.id", "arg.arg")}
    print(f"A2 ∖ A1（A1 之定義結構上⛔ 及者）：出現 {sum(extra.values())}／形 {len(extra)} ⇒ {sorted(extra.items())}")
    print(f"自洽：A2 之 Name/arg 部分 ＝ A1 ？ {dict(a2_nodeform) == dict(a1)}")
    art = "".join(chr(c) for c in (95, 122, 122, 113, 57, 51, 48, 53))   # 執行期組出之人造名
    print(f"判別力[必為零] 人造名於 A2 ⇒ {sum(census_A2(fn, {art}).values())}")
    print(f"判別力[必非零] A2 出現 ⇒ {sum(a2.values())}")
    inner = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)) for n in ast.walk(fn) if n is not fn)
    print(f"非頂層基數（自誤 411 攔法 ②）：_solve_G_one 內 FunctionDef/AsyncFunctionDef/Lambda ＝ {inner}")

    # ── 節 B ──
    sp = ast.parse(blob("verify/stepg_pipeline.py"))
    d = fdef(sp, "_run_step_g_impl")
    print(f"\n── 節 B　verify/stepg_pipeline.py :: _run_step_g_impl（定義處 {len(d)}）──")
    if len(d) != 1:
        raise SystemExit("STOP: _run_step_g_impl 定義處 ≠ 1")
    g = d[0]
    scopes = [n for n in ast.walk(g) if n is not g and isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp, ast.ClassDef))]
    cnt = collections.Counter(type(n).__name__ for n in scopes)
    print(f"巢狀作用域（Function/Async/Lambda/ClassDef ＋ 四種 comprehension）＝ {len(scopes)} ⇒ {dict(sorted(cnt.items()))}")
    named = [n for n in scopes if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    print(f"其中具名者 ＝ {len(named)} ⇒ {[n.name for n in named]}")

    # 每一節點之最內層「具名或 lambda」作用域
    owner_scope = {}
    def walk(node, cur):
        for c in ast.iter_child_nodes(node):
            nxt = c.name if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else ("<lambda>" if isinstance(c, ast.Lambda) else cur)
            owner_scope[id(c)] = nxt if nxt is not cur else cur
            walk(c, nxt)
    walk(g, "_run_step_g_impl")

    comp_t = (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    in_comp = set()
    for c in ast.walk(g):
        if isinstance(c, comp_t):
            for x in ast.walk(c):
                if x is not c:
                    in_comp.add(id(x))
    six = ["res", "_n", "_nodes", "_prev_dir", "_near_dir_left", "_near_dir_right", "_alloc_dir_used"]
    print(f"\n名集（逐字）＝ {six}")
    for nm in six:
        store = collections.Counter(); load = collections.Counter(); strf = collections.Counter()
        for owner in ast.walk(g):
            for field, val in ast.iter_fields(owner):
                for v in (val if isinstance(val, list) else [val]):
                    if not (isinstance(v, str) and v == nm):
                        continue
                    sc = owner_scope.get(id(owner), "_run_step_g_impl")
                    if isinstance(owner, ast.Name):
                        (store if isinstance(owner.ctx, ast.Store) else load)[sc] += 1
                    elif isinstance(owner, ast.arg):
                        store[sc + "(形參)"] += 1
                    else:
                        strf[(sc, f"{type(owner).__name__}.{field}")] += 1
        print(f"  {nm:<16} Store/形參 所屬作用域 ⇒ {dict(store)}")
        print(f"  {'':<16} Load 所屬作用域      ⇒ {dict(load)}")
        print(f"  {'':<16} 其餘 str 欄位（含字串常數）⇒ {dict(strf)}")
        nc = sum(1 for o in ast.walk(g) if isinstance(o, ast.Name) and o.id == nm and isinstance(o.ctx, ast.Store) and id(o) in in_comp)
        print(f"  {'':<16} 其 Name-Store 位於 comprehension 作用域內者（本器將其併入外層具名函式·自限）⇒ {nc}")

    # 強制呼叫點與巢狀函式之呼叫點，於最外層逐街廓 For 內之先後
    fors = [n for n in ast.walk(g) if isinstance(n, ast.For) and "parcels_by_block" in ast.unparse(n.iter)]
    print(f"\n逐街廓 For（iter 含字樣 parcels_by_block）＝ {len(fors)} 處")
    for F in fors:
        calls = []
        for n in ast.walk(F):
            if isinstance(n, ast.Call):
                fnm = n.func.id if isinstance(n.func, ast.Name) else None
                if fnm:
                    calls.append((n.lineno, fnm, owner_scope.get(id(n), "?")))
        cb = [c for c in calls if c[1] == "_corner_buffer_S"]
        inner_names = {x.name for x in named}
        ic = [c for c in calls if c[1] in inner_names]
        defs_in = [(x.lineno, x.name) for x in named if F.lineno <= x.lineno <= F.end_lineno]
        print(f"  For 所屬作用域 = {owner_scope.get(id(F), '_run_step_g_impl')}")
        print(f"  _corner_buffer_S 之 Name 形呼叫 ⇒ {len(cb)} 處；所屬作用域 ⇒ {sorted({c[2] for c in cb})}")
        print(f"  於本 For 內定義之巢狀具名函式 ⇒ {len(defs_in)} 個 ⇒ {[x[1] for x in sorted(defs_in)]}")
        print(f"  全部 {len(inner_names)} 個巢狀具名函式（含本 For 外定義者）於本 For 內之 Name 形呼叫 ⇒ {len(ic)} 處 ⇒ {dict(sorted(collections.Counter(c[1] for c in ic).items()))}")
        if cb:
            last_cb = max(c[0] for c in cb)
            before = [c for c in ic if c[0] < last_cb]
            print(f"  （位序·⛔ 為錨）上開 {len(ic)} 處呼叫之位序先於最末一處強制呼叫者 ⇒ {len(before)} 處 ⇒ {before}")
            dbefore = [x for x in defs_in if x[0] < min(c[0] for c in cb)]
            print(f"  （位序·⛔ 為錨）於本 For 內定義之 {len(defs_in)} 個中，其定義位序先於首處強制呼叫者 ⇒ {len(dbefore)} 個 ⇒ {[x[1] for x in dbefore]}")
    print("\n【本器⛔ 判可施與否·⛔ 擬任何改法】")


if __name__ == "__main__":
    main()
