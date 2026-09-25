# -*- coding: utf-8 -*-
"""W-G.9-345 量測器（發單側窗四十一擬·檔 F4·⛔ 由受單側改一字）：畫面二段之抽出與段三畫面接線。

受詞：`app.py` `def main()` 內二 If 之本體——
  (甲) 街角選位（If 之 test 含字樣 KEY_PK）→ 模組層 `f3_screen_corner_pk_run(st, *, …)`；
  (乙) 配地（If 之 test 含字樣 KEY_G）→ 模組層 `f3_screen_stepg_run(st, *, …)`；
及段三畫面入口 `f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs)`（`W-G.9-345 §三-2`）。

子命令（一律 python verify/probes/probe_WG9345_screen.py <子命令> …）：
  census   <repo> <基準 commit>
           於基準之 app.py 普查二本體：main 區域自由變數（symtable 實查）、所寫之 session 鍵（字面）、
           可達之模組層函式中經任一別名讀寫 session 者、所改之模組層全域容器。只出艙·rc 0。
  ast      <repo> <基準 commit>
           抽出之零變更：A1 新函式在模組層、簽名 (st, *, 無預設)；A2 本體（去 docstring）與基準 If 本體
           ast 全等；A3 參數集 ＝ 基準之自由變數集；A4 目標 main() ＝ 基準 main() 將二 If 本體各換為
           單一呼叫 fn(st, p=p, …)（關鍵字集 ＝ 參數集）；A5 模組層其餘節點依序全等；A6 新函式之全域參照
           ⛔ 含基準 main() 之區域名、⛔ 含未定義名。
  parity   <repo> <退縮> <off|on|s3off> [<out.json>] [--perturb]
           以 harness 同源之量組裝畫面二函式之輸入（映射見 `_screen_inputs`），逐鍵對拍：
           off：畫面（f3_screen_corner_pk_run → f3_screen_stepg_run）對 harness（run_corner_pk → run_step_g）；
           on ：畫面（f3_screen_k6b_stage3 → f3_screen_stepg_run〔段三後之 build〕）對 harness
                （run_corner_pk_k6b → run_step_g〔段三後之 build〕）；另驗 session 之回復與 K917_DROPPED。
           s3off：同 on 之二路徑，惟旗標 WV_K6B_STAGE3=off（二側皆須回到段三前·紀錄為空）。
           配地列以暫編地號對齊；一側獨有之列須「幾何面積 0 且 G 0」（零面積池列·逐一出艙為 Z），餘須全等；
           cut_coords 以環（去閉合點·容旋轉與反向）比對。--perturb：將畫面側之 B 值乘 1.0001（必紅造）。
  wiring   <repo>
           工項五之接線（AST·工作樹）：W0 模組層新函式；W1 街角選位 If 之本體 ＝ 單一呼叫 f3_screen_k6b_stage3；
           W2 配地 If 之本體 ＝ 單一呼叫 f3_screen_stepg_run（build_parcels＝k6b_screen_build_for_g(st, build_parcels)）；
           W3 _f3L_invalidate_g_cache 失效段三之鍵；W4 wf_f4.compute 之五呼叫點皆以 k6b_f4_ctx 為首參；
           W5 _build_wf_ctx 依段三取 build／temp（ctx 仍 14 鍵）；W6 步驟 M 之讀；W7 過時之說明已去；W8 候選診斷表入 session。
           本部全綠時另施四種 AST 突變，須逐一轉紅（器紅 ⇒ rc 1）。
  f4ctx    <repo>        verify/selection_pipeline.py 之 k6b_f4_ctx 之單元檢。
  wfctx    <repo> <退縮>  _build_wf_ctx 之四情形：無段三之鍵／段三仍適用／指紋不符（二造）／前次停機。
  selftest 合成對照（⛔ 讀倉）：ast 之四種突變皆紅、原封者綠；列比對之擾動紅、環旋轉綠、零面積列入 Z。
rc：0 相符／1 不符／2 用法錯／3 無從判定（受詞缺或執行中止·⛔ 等同相符）。
"""
import ast, builtins, collections, contextlib, copy, hashlib, importlib.util, io, json, math, os, re, subprocess, sys, symtable

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

KEY_PK = "執行第 1 宗街角地優先權選位（左右側獨立）"
KEY_G = "_btn_clicked or _auto_recalc"
FN_PK, FN_G, FN_S3 = "f3_screen_corner_pk_run", "f3_screen_stepg_run", "f3_screen_k6b_stage3"
FNS = {FN_PK: KEY_PK, FN_G: KEY_G}
ENV = "WV_K6B_STAGE3"
BI = set(dir(builtins))
PK_KEYS = ("f3L_corner_winners", "f3L_forced_offset", "f3_corner_winners", "f3_current_pk_block",
           "f3_k6b_dual_side_assign", "f3_k6b_stage1_locked_by_block", "f3_k6b_stage1_locks",
           "f3_k6b_stage2_order", "f3_pk_alloc_depth", "f3_pk_legal_min_width")
PK_WRITES = set(PK_KEYS) | {"f3L_corner_side_warnings",           # 街角選位本體所寫之 session 鍵（census 實查·基準 3914b6e）
                              "f3_corner_range_areas", "f3_corner_range_polys"}  # 及其可達函式（select_corner_lots_both_sides_v12）所寫者
TOL = 1e-6


def D(x):
    return ast.dump(x, include_attributes=False)


# ───────────────────────── 靜態：定位、普查、零變更 ─────────────────────────
def _main_of(tree):
    hits = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "main"]
    if len(hits) != 1:
        raise LookupError(f"模組層 def main 之數 ＝ {len(hits)}")
    return hits[0]


def _target_if(main, lines, key):
    hits = [n for n in ast.walk(main) if isinstance(n, ast.If)
            and key in "\n".join(lines[n.test.lineno - 1:n.test.end_lineno])]
    if len(hits) != 1:
        raise LookupError(f"main() 內 test 含 {key!r} 之 If 之數 ＝ {len(hits)}")
    return hits[0]


def _body_stores(ifn):
    s = set()
    for n in ast.walk(ifn):
        if isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)):
            s.add(n.id)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            a = n.args
            for x in a.posonlyargs + a.args + a.kwonlyargs + [v for v in (a.vararg, a.kwarg) if v]:
                s.add(x.arg)
            if not isinstance(n, ast.Lambda):
                s.add(n.name)
        elif isinstance(n, ast.ExceptHandler) and n.name:
            s.add(n.name)
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                s.add((a.asname or a.name).split(".")[0])
    return s


def free_main_locals(src, key):
    """本體所讀、於本體內⛔ 賦值、而於 main() 為區域名者（symtable 實查）。"""
    tree = ast.parse(src)
    lines = src.split("\n")
    main = _main_of(tree)
    ifn = _target_if(main, lines, key)
    top = symtable.symtable(src, "app.py", "exec")
    mst = [c for c in top.get_children() if c.get_name() == "main"][0]
    mloc = {s.get_name() for s in mst.get_symbols() if s.is_local()}
    loads = {n.id for s in ifn.body for n in ast.walk(s) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    return sorted((loads & mloc) - _body_stores(ifn)), ifn, main, tree, mloc


def _ss_literal_writes(node):
    """<X>.session_state[<字面>] = …／del／.pop／.setdefault／.update 之字面鍵（任一別名 X）。"""
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Subscript) and isinstance(n.ctx, (ast.Store, ast.Del)):
            v = n.value
            if isinstance(v, ast.Attribute) and v.attr == "session_state":
                out.add(n.slice.value if isinstance(n.slice, ast.Constant) else "<expr>")
            elif isinstance(v, ast.Name) and re.match(r"_?ss\w*$", v.id):
                out.add((n.slice.value if isinstance(n.slice, ast.Constant) else "<expr>") + f"（經 {v.id}）")
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in ("pop", "setdefault", "update", "clear"):
            v = n.func.value
            if isinstance(v, ast.Attribute) and v.attr == "session_state":
                a0 = n.args[0].value if (n.args and isinstance(n.args[0], ast.Constant)) else f"<{n.func.attr}>"
                out.add(a0 if isinstance(a0, str) else f"<{n.func.attr}>")
    return out


def cmd_census(repo, base):
    src = _git_show(repo, base, "app.py")
    lines = src.split("\n")
    tree = ast.parse(src)
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    glob = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}

    def calls(node):
        return {m.id for m in ast.walk(node) if isinstance(m, ast.Name) and isinstance(m.ctx, ast.Load) and m.id in funcs}
    MUT = {"append", "extend", "update", "clear", "pop", "add", "setdefault", "insert", "remove", "discard"}
    print(f"【F4 census】基準 {base}·app.py {len(src.encode('utf-8'))} B")
    for key in (KEY_PK, KEY_G):
        free, ifn, main, _t, _m = free_main_locals(src, key)
        seen, stack = set(), list(calls(ifn))
        while stack:
            f = stack.pop()
            if f in seen or f == "main":
                continue
            seen.add(f)
            stack.extend(calls(funcs[f]))
        sess = {}
        for f in sorted(seen):
            seg = "\n".join(lines[funcs[f].lineno - 1:funcs[f].end_lineno])
            al = sorted({m.group(1) for m in re.finditer(r"(\w+)\.session_state", seg)})
            if al:
                sess[f] = al
        muts = {}
        for f in sorted(seen):
            ms = sorted({f"{m.func.value.id}.{m.func.attr}" for m in ast.walk(funcs[f])
                         if isinstance(m, ast.Call) and isinstance(m.func, ast.Attribute) and isinstance(m.func.value, ast.Name)
                         and m.func.value.id in glob and m.func.attr in MUT})
            if ms:
                muts[f] = ms
        w_body = sorted(_ss_literal_writes(ifn), key=str)
        w_reach = {f: sorted(_ss_literal_writes(funcs[f]), key=str) for f in sorted(seen) if _ss_literal_writes(funcs[f])}
        print(f"\n## If@{ifn.lineno}–{ifn.end_lineno}（test 含 {key!r}）")
        print(f"  main 區域自由變數（{len(free)}）：{free}")
        print(f"  本體所寫之 session 鍵（{len(w_body)}）：{w_body}")
        print(f"  可達之模組層函式（{len(seen)}）中讀寫 session 者：{sess}")
        print(f"  可達之模組層函式所寫之 session 鍵：{w_reach}")
        print(f"  可達之模組層函式所改之模組層全域容器：{muts}")
    return 0


def _git_show(repo, rev, path):
    r = subprocess.run(["git", "-C", repo, "show", f"{rev}:{path}"], capture_output=True)
    if r.returncode != 0:
        raise LookupError(f"git show {rev}:{path} 失敗：{r.stderr.decode('utf-8', 'replace')[:200]}")
    return r.stdout.decode("utf-8")


def ast_check(base_src, tgt_src, say):
    """回傳不符項數。"""
    bad = 0

    def chk(ok, msg):
        nonlocal bad
        bad += (not ok)
        say(("✅ " if ok else "🔴 ") + msg)
    tb = ast.parse(base_src)
    tt = ast.parse(tgt_src)
    mb = _main_of(tb)
    mt = _main_of(tt)
    fnt = {n.name: n for n in tt.body if isinstance(n, ast.FunctionDef)}
    need = {}
    for fn, key in FNS.items():
        free, ifn, _m, _t, mloc = free_main_locals(base_src, key)
        need[fn] = (set(free), ifn)
    subst = {}
    for fn, key in FNS.items():
        free, ifn = need[fn]
        f = fnt.get(fn)
        chk(f is not None, f"A1 模組層有 def {fn}")
        if f is None:
            continue
        a = f.args
        sig_ok = (len(a.args) == 1 and a.args[0].arg == "st" and not a.posonlyargs and not a.vararg
                  and not a.kwarg and not a.defaults and all(d is None for d in a.kw_defaults) and not f.decorator_list)
        chk(sig_ok, f"A1 {fn} 之簽名 ＝ (st, *, …)·無預設·無裝飾")
        body = f.body
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
            body = body[1:]
        chk(D(ast.Module(body=body, type_ignores=[])) == D(ast.Module(body=ifn.body, type_ignores=[])),
            f"A2 {fn} 之本體（去 docstring）與基準 If@{ifn.lineno} 之本體 ast 全等（{len(ifn.body)} 敘述）")
        got = {x.arg for x in a.kwonlyargs}
        chk(got == free, f"A3 {fn} 之參數集 ＝ 基準之自由變數集（{len(free)}）"
            + ("" if got == free else f"：多 {sorted(got - free)}／缺 {sorted(free - got)}"))
        subst[key] = (fn, sorted(got))
    # A4：以單一呼叫換基準之二 If 本體（關鍵字依名排序）後，與目標 main 比（目標之關鍵字亦依名排序）
    lb = base_src.split("\n")
    mb2 = copy.deepcopy(mb)
    for key, (fn, params) in subst.items():
        ifn = _target_if(mb2, lb, key)
        ifn.body = [ast.Expr(ast.Call(func=ast.Name(fn, ast.Load()), args=[ast.Name("st", ast.Load())],
                                      keywords=[ast.keyword(arg=p, value=ast.Name(p, ast.Load())) for p in params]))]
    mt2 = copy.deepcopy(mt)
    for n in ast.walk(mt2):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in FNS:
            n.keywords = sorted(n.keywords, key=lambda k: k.arg or "")
    ok4 = len(subst) == 2 and D(mb2) == D(mt2)
    chk(ok4, "A4 目標 main() ＝ 基準 main() 之二 If 本體各換為單一呼叫 fn(st, p=p, …)")
    rb = [n for n in tb.body if not (isinstance(n, ast.FunctionDef) and n.name == "main")]
    rt = [n for n in tt.body if not (isinstance(n, ast.FunctionDef) and (n.name == "main" or n.name in FNS))]
    ok5 = len(rb) == len(rt) and all(D(x) == D(y) for x, y in zip(rb, rt))
    chk(ok5, f"A5 模組層其餘節點依序全等（基準 {len(rb)}／目標 {len(rt)}）")
    try:
        top = symtable.symtable(tgt_src, "app.py", "exec")
        topb = symtable.symtable(base_src, "app.py", "exec")
        mloc = {s.get_name() for s in [c for c in topb.get_children() if c.get_name() == "main"][0].get_symbols() if s.is_local()}
        mod_def = {s.get_name() for s in top.get_symbols() if s.is_assigned() or s.is_imported() or s.is_namespace()}

        def walk(t):
            yield t
            for c in t.get_children():
                yield from walk(c)
        for fn in FNS:
            tabs = [c for c in top.get_children() if c.get_name() == fn]
            if not tabs:
                continue
            g = {s.get_name() for t in walk(tabs[0]) for s in t.get_symbols() if s.is_global() and s.is_referenced()}
            und = sorted(x for x in g if x not in mod_def and x not in BI)
            sh = sorted(x for x in g if x in mloc)
            chk(not und and not sh, f"A6 {fn} 之全域參照（{len(g)}）無未定義名、無基準 main() 之區域名"
                + ("" if (not und and not sh) else f"：未定義 {und}／原為 main 區域 {sh}"))
    except Exception as e:  # noqa: BLE001
        chk(False, f"A6 symtable 無從判定：{type(e).__name__}: {e}")
    return bad


def cmd_ast(repo, base):
    try:
        bsrc = _git_show(repo, base, "app.py")
        tsrc = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    except Exception as e:  # noqa: BLE001
        print(f"🔴 受詞缺：{e} ⇒ 無從判定")
        return 3
    head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    print(f"【F4 ast】基準 {base} ／ 目標 {head}（工作樹之 app.py）")
    try:
        bad = ast_check(bsrc, tsrc, print)
    except LookupError as e:
        print(f"🔴 受詞缺：{e} ⇒ 無從判定")
        return 3
    print(f"⇒ rc {1 if bad else 0}（不符 {bad} 項）")
    return 1 if bad else 0


# ───────────────────────── 動態：啞 st、輸入映射、對拍 ─────────────────────────
class _Stop(Exception):
    pass


class _Rerun(Exception):
    pass


class _CM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __call__(self, *a, **k):
        return _CM()

    def __getattr__(self, n):
        return _CM()

    def __iter__(self):
        return iter(())


class QuietSt:
    """啞 st：session_state ＝ 模組層函式經 streamlit 模組所讀之**同一物件**；UI no-op；stop ⇒ _Stop；rerun ⇒ _Rerun。"""
    def __init__(self, ss):
        object.__setattr__(self, "session_state", ss)
        object.__setattr__(self, "msgs", [])

    def stop(self):
        raise _Stop("st.stop")

    def rerun(self, *a, **k):
        raise _Rerun("st.rerun")

    def columns(self, spec, *a, **k):
        return [_CM() for _ in range(spec if isinstance(spec, int) else len(spec))]

    def tabs(self, names, *a, **k):
        return [_CM() for _ in names]

    def __getattr__(self, name):
        def _f(*a, **k):
            if name in ("error", "warning", "info", "success", "caption", "markdown", "write"):
                self.msgs.append((name, str(a[0])[:300] if a else ""))
            return _CM()
        return _f


def _same(a, b, tol=TOL):
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if isinstance(a, float) and isinstance(b, float) and math.isnan(a) and math.isnan(b):
            return True
        return abs(float(a) - float(b)) <= tol
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_same(a[k], b[k], tol) for k in a)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_same(x, y, tol) for x, y in zip(a, b))
    if isinstance(a, (set, frozenset)) and isinstance(b, (set, frozenset)):
        return a == b
    try:
        import numpy as np
        if isinstance(a, np.ndarray) or isinstance(b, np.ndarray):
            return _same(np.asarray(a).tolist(), np.asarray(b).tolist(), tol)
    except Exception:  # noqa: BLE001
        pass
    if hasattr(a, "equals_exact") and hasattr(b, "equals_exact"):
        return a.equals_exact(b, 0.0)
    return a == b


def _ring_norm(cc):
    pts = [(float(p[0]), float(p[1])) for p in (cc or [])]
    if len(pts) >= 2 and pts[0] == pts[-1]:
        pts = pts[:-1]
    if not pts:
        return []
    cands = []
    for seq in (pts, pts[::-1]):
        i = min(range(len(seq)), key=lambda k: seq[k])
        cands.append(seq[i:] + seq[:i])
    return min(cands)


def compare_rows(rh, rs, say, cap=12):
    """配地列對拍。回傳 (不符格數, Z 列表)。Z ＝ 一側獨有且幾何面積 0、G 0 之列。"""
    bh = collections.OrderedDict((r.get("暫編地號"), r) for r in rh)
    bs = collections.OrderedDict((r.get("暫編地號"), r) for r in rs)
    bad, Z, shown = 0, [], 0
    for side, only, src in (("harness", [k for k in bh if k not in bs], bh), ("畫面", [k for k in bs if k not in bh], bs)):
        for k in only:
            r = src[k]
            zero = abs(float(r.get("幾何面積(㎡)", 1) or 0)) == 0.0 and abs(float(r.get("G(㎡)", 1) or 0)) == 0.0
            if zero:
                Z.append((side, k))
            else:
                bad += 1
                say(f"    🔴 僅見於{side}且非零面積：{k}（幾何面積 {r.get('幾何面積(㎡)')}·G {r.get('G(㎡)')}）")
    common = [k for k in bh if k in bs]
    order_ok = [k for k in bh if k in bs] == [k for k in bs if k in bh]
    if not order_ok:
        bad += 1
        say("    🔴 共有列之次序不同")
    for k in common:
        a, b = bh[k], bs[k]
        for f in sorted(set(a) | set(b), key=str):
            va, vb = a.get(f, "<缺>"), b.get(f, "<缺>")
            ok = (_ring_norm(va) == _ring_norm(vb)) if f == "cut_coords" and isinstance(va, (list, tuple)) and isinstance(vb, (list, tuple)) else _same(va, vb)
            if not ok:
                bad += 1
                if shown < cap:
                    shown += 1
                    say(f"    🔴 {k}·{f}：harness {str(va)[:100]} ／ 畫面 {str(vb)[:100]}")
    return bad, Z


def _load_f2(repo):
    spec = importlib.util.spec_from_file_location("f2", os.path.join(repo, "verify", "probes", "probe_WG9344_k6s3.py"))
    f2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f2)
    return f2


def _screen_inputs(ns, fst, snap, cb, cad, params, tp, bp, sb):
    """畫面二函式之輸入 ← harness 同源之量（對映 main() 於二 If 之前所備者）。
    session ＝ fst.session_state（**同一物件**：v12／_first_corner_alloc_dir／bl_pts_by_label／
    _estimate_G_for_qualification 經 streamlit 模組讀之）。"""
    from stepg_pipeline import _compute_v3_finance
    import pandas as pd
    from shapely.geometry import Polygon as _P
    fin = _compute_v3_finance(ns, snap, cb, cad)
    SB = snap["blocks"]
    bb = fin["_build_blocks"]
    rows = {r["街廓"]: r for r in params}
    ss = fst.session_state
    ss["f3L_setback_default"] = sb
    ss["f3_cad_front_lengths"] = cad.get("front_lengths", {}) or {}
    ss["f3_cad_side_lengths"] = cad.get("side_lengths", {}) or {}
    ss.setdefault("f3_g_iter_params", {})
    ss["f3_alloc_depth_by_label"] = {b["label"]: float(SB[b["label"]]["街廓分配深度_m"]) for b in bb}
    ss["f3_min_width_by_label"] = {
        b["label"]: float(ns["get_min_lot_size"](b["category"], float(SB[b["label"]]["正面"]["路寬_m"])).get("min_width", 0.0) or 0.0)
        for b in bb}
    ss["f3L_corner_min_table"] = params
    ss["f3_manual_baseline"] = cad.get("baselines")
    ss["f3_manual_road_centerlines"] = dict(cad.get("centerlines", {}) or {})   # main() 讀 CAD 後所存（同 _build_wf_ctx 之源）
    bmeta = {}
    for b in cb:
        m = dict(b)
        try:
            p = _P(b["vertices"])
            m["shapely"] = p if p.is_valid else p.buffer(0)
        except Exception:  # noqa: BLE001
            m["shapely"] = None
        bmeta[b["label"]] = m
    pk = dict(build_parcels=bp, _build_blocks=bb, _corner_rows_init=[rows[b["label"]] for b in bb if b["label"] in rows],
              temp_parcels=tp, sb_rows_by_label=fin["sb_rows_by_label"], B_value=fin["B"], C_for_calc=fin["C"],
              post_price_by_block=fin["post_price_by_block"], pre_price_by_zone=fin["pre_price_by_zone"], _pd=pd)
    g = dict(_param_key="f3_g_iter_params", B_value=fin["B"], C_for_calc=fin["C"],
             _tab6_burden=float(ss.get("f3_total_burden_rate_from_finance")), block_meta_by_label=bmeta,
             sb_rows_by_label=fin["sb_rows_by_label"], post_price_by_block=fin["post_price_by_block"],
             pre_price_by_zone=fin["pre_price_by_zone"], classified_blocks=cb)
    return pk, g


def _copy_pair(tp, bp):
    t = copy.deepcopy(tp)
    by = {x["暫編地號"]: x for x in t}
    return t, [by[b["暫編地號"]] for b in bp]


def _run_screen_g(ns, qs, g, build, say):
    kw = dict(g, _auto_recalc=False, _btn_clicked=True, build_parcels=build,
              _new_params=dict(qs.session_state.get("f3_g_iter_params", {}) or {}))
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ns[FN_G](qs, **kw)
    except _Rerun:
        pass
    except _Stop:
        say(f"  🔴 畫面配地中止（st.stop）：{qs.msgs[-3:]}")
        return None
    return qs.session_state.get("f3_G_values")


def cmd_parity(repo, sb, mode, out=None, perturb=False):
    if mode not in ("off", "on", "s3off"):
        return 2
    k6b = mode in ("on", "s3off")                     # s3off：旗標 off 而走段三入口（二側皆應逐位回到段三前）
    os.environ[ENV] = "off" if mode == "s3off" else mode
    f2 = _load_f2(repo)
    head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    print(f"【F4 parity】態 {head}·退縮 {sb}·{ENV}={mode}·擾動 {perturb}")
    ns, fst, snap, cb_by, cad, tp, bp, params = f2._boot(repo, sb)
    miss = [n for n in ((FN_PK, FN_G, FN_S3) if k6b else (FN_PK, FN_G)) if n not in ns]
    if miss:
        print(f"🔴 受詞缺：app.py 模組層無 {miss} ⇒ 無從判定")
        return 3
    from selection_pipeline import run_corner_pk, run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    cb = list(cb_by.values())
    ss = fst.session_state
    ss0 = copy.deepcopy(dict(ss))
    k0 = copy.deepcopy(ns["K917_DROPPED"])
    bad = 0
    rep = {"head": head, "sb": sb, "mode": mode, "perturb": perturb}

    def say(s):
        print(s)
    # ── harness ──
    tH, bH = _copy_pair(tp, bp)
    ns["K917_DROPPED"].clear()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            if not k6b:
                dH, sH, oH, wH, fH = run_corner_pk(ns, fst, cb, cad, params, tH, bH, sb, snapshot=snap)
            else:
                dH, sH, oH, wH, fH, tH, bH = run_corner_pk_k6b(ns, fst, cb, cad, params, tH, bH, sb, snapshot=snap)
        ssH = copy.deepcopy(dict(ss))
        k917H_pk = copy.deepcopy(ns["K917_DROPPED"])
        with contextlib.redirect_stdout(io.StringIO()):
            sgH = run_step_g(ns, fst, cb, cad, snap, params, bH, wH, fH, sb, eff_min_build_by_blk={})
    except Exception as e:  # noqa: BLE001
        print(f"🔴 harness 執行中止：{type(e).__name__}: {str(e)[:300]} ⇒ 無從判定")
        return 3
    gH = sgH["g_rows"]
    REF = dict(ssH)
    REF.update({"f3_corner_winners": wH, "f3L_forced_offset": fH, "f3L_corner_winners": sH})
    # ── 畫面 ──
    ss.clear()
    ss.update(copy.deepcopy(ss0))
    ns["K917_DROPPED"].clear()
    ns["K917_DROPPED"].update(copy.deepcopy(k0))
    tS, bS = _copy_pair(tp, bp)
    pk, g = _screen_inputs(ns, fst, snap, cb, cad, params, tS, bS, sb)
    if perturb:
        pk["B_value"] = pk["B_value"] * 1.0001
        g["B_value"] = g["B_value"] * 1.0001
    qs = QuietSt(ss)
    pre = copy.deepcopy(dict(ss))
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            if not k6b:
                ns[FN_PK](qs, **pk)
                tS2, bS2 = tS, bS
            else:
                ret = ns[FN_S3](qs, pk_kwargs=pk, g_kwargs=g)
                tS2, bS2 = ret["temp"], ret["build"]
                rep["s3_ret_keys"] = sorted(ret)
    except _Stop:
        print(f"🔴 畫面街角選位中止（st.stop）：{qs.msgs[-3:]} ⇒ 無從判定")
        return 3
    except Exception as e:  # noqa: BLE001
        print(f"🔴 畫面街角選位執行中止：{type(e).__name__}: {str(e)[:300]} ⇒ 無從判定")
        return 3
    ssS_pk = copy.deepcopy(dict(ss))
    k917S_pk = copy.deepcopy(ns["K917_DROPPED"])
    for k in PK_KEYS:
        ok = _same(REF.get(k, "<缺>"), ssS_pk.get(k, "<缺>"))
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} 街角選位 session 鍵 {k}")
    if k6b:
        for k in ("f3_k6b_stage3_log", "f3_k6b_stage3_order_used"):
            ok = _same(REF.get(k, "<缺>"), ssS_pk.get(k, "<缺>"))
            bad += (not ok)
            say(f"  {'✅' if ok else '🔴'} 段三 session 鍵 {k}（{len(REF.get(k) or [])} 列）")
        idsH = [(t["暫編地號"], t.get("段三併出")) for t in tH]
        idsS = [(t["暫編地號"], t.get("段三併出")) for t in tS2]
        ok = idsH == idsS
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} 段三後 temp 之暫編地號與「段三併出」逐元素依序（{len(idsH)}／{len(idsS)}）")
        F4 = ("面積_m2", "分攤登記面積_m2", "登記面積_m2", "幾何面積_m2", "所屬街廓")
        ok = all(_same([t.get(f) for f in F4], [u.get(f) for f in F4]) for t, u in zip(tH, tS2))
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} 段三後 temp 之面積四欄與所屬街廓逐元素")
        ok = [b["暫編地號"] for b in bH] == [b["暫編地號"] for b in bS2]
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} 段三後 build 之暫編地號依序（{len(bH)}／{len(bS2)}）")
        ids_t = {id(x) for x in tS2}
        ok = all(id(b) in ids_t for b in bS2)
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} 段三後 build ⊂ temp（同物件）")
        ok = _same(k917H_pk, k917S_pk)
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} K917_DROPPED（段三畢·與 harness 同）")
        leak = [k for k in pre if k not in PK_WRITES and not k.startswith("f3_k6b_stage3")
                and k != "f3_corner_cand_diag" and not _same(pre.get(k), ssS_pk.get(k))]
        newk = sorted(k for k in ssS_pk if k not in pre and k not in PK_WRITES and not k.startswith("f3_k6b_stage3")
                      and k != "f3_corner_cand_diag")
        ok = not leak and not newk
        bad += (not ok)
        say(f"  {'✅' if ok else '🔴'} session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵"
            + ("" if ok else f"（值變 {sorted(leak)[:12]}；新生 {newk[:12]}）"))
    # ── 配地 ──
    ns["K917_DROPPED"].clear()
    gS = _run_screen_g(ns, qs, g, bS2, say)
    if gS is None:
        print(f"⇒ rc 3（畫面配地無出艙）")
        return 3
    nd, Z = compare_rows(gH, gS, say)
    ok = nd == 0
    bad += (not ok)
    say(f"  {'✅' if ok else '🔴'} 配地列（harness {len(gH)}／畫面 {len(gS)}；不符格 {nd}）")
    say(f"  ℹ️ Z（一側獨有之零面積池列）＝ {Z}")
    rep.update({"n_rows": [len(gH), len(gS)], "Z": Z, "bad": bad,
                "stage3_log": ssS_pk.get("f3_k6b_stage3_log") if k6b else None})
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(rep, fh, ensure_ascii=False, indent=1, default=str)
    print(f"⇒ rc {1 if bad else 0}（不符 {bad} 項）")
    return 1 if bad else 0


# ───────────────────────── 接線（工項五）：靜態 ─────────────────────────
G9 = ("_param_key", "B_value", "C_for_calc", "_tab6_burden", "block_meta_by_label", "sb_rows_by_label",
      "post_price_by_block", "pre_price_by_zone", "classified_blocks")
WF4_SITES = ("app.py", "verify/run_verification.py", "verify/wg_g1_smoke.py", "verify/wg_g2_smoke.py", "verify/wg_g3.py")
STALE = ("（逐一嘗試／集中規則／跨街廓合併）尚未落地", "而段三尚未落地（`VR-086`）。⛔ 作用於")


def _kw_names_eq(call, names):
    return (isinstance(call, ast.Call) and not call.args and
            sorted(k.arg or "" for k in call.keywords) == sorted(names) and
            all(isinstance(k.value, ast.Name) and k.value.id == k.arg for k in call.keywords))


def _wf4_calls(tree):
    return [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
            and n.func.attr == "compute" and isinstance(n.func.value, ast.Name) and n.func.value.id in ("wf_f4", "_wf4")]


def wiring_check(srcs, say):
    """srcs：{相對路徑: 原文}（須含 WF4_SITES）。回傳不符項數。"""
    bad = 0

    def chk(ok, msg):
        nonlocal bad
        bad += (not ok)
        say(("✅ " if ok else "🔴 ") + msg)
    src = srcs["app.py"]
    tree = ast.parse(src)
    lines = src.split("\n")
    main = _main_of(tree)
    fns = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    for fn in (FN_PK, FN_G, FN_S3, "k6b_stage3_fingerprint", "k6b_stage3_selected", "k6b_screen_build_for_g"):
        chk(fn in fns, f"W0 模組層有 def {fn}")
    if not all(fn in fns for fn in (FN_PK, FN_G, FN_S3)):
        return bad
    pk10 = [a.arg for a in fns[FN_PK].args.kwonlyargs]
    g13 = [a.arg for a in fns[FN_G].args.kwonlyargs]
    # W1
    ifn = _target_if(main, lines, KEY_PK)
    ok = False
    if len(ifn.body) == 1 and isinstance(ifn.body[0], ast.Expr) and isinstance(ifn.body[0].value, ast.Call):
        c = ifn.body[0].value
        kw = {k.arg: k.value for k in c.keywords}
        ok = (isinstance(c.func, ast.Name) and c.func.id == FN_S3 and len(c.args) == 1
              and isinstance(c.args[0], ast.Name) and c.args[0].id == "st" and set(kw) == {"pk_kwargs", "g_kwargs"}
              and isinstance(kw["pk_kwargs"], ast.Call) and isinstance(kw["pk_kwargs"].func, ast.Name) and kw["pk_kwargs"].func.id == "dict"
              and _kw_names_eq(kw["pk_kwargs"], pk10)
              and isinstance(kw["g_kwargs"], ast.Call) and isinstance(kw["g_kwargs"].func, ast.Name) and kw["g_kwargs"].func.id == "dict"
              and _kw_names_eq(kw["g_kwargs"], G9))
    chk(ok, f"W1 街角選位 If 之本體 ＝ 單一呼叫 {FN_S3}(st, pk_kwargs=dict(<{len(pk10)} 名>), g_kwargs=dict(<{len(G9)} 名>))")
    # W2
    ifn = _target_if(main, lines, KEY_G)
    ok = False
    if len(ifn.body) == 1 and isinstance(ifn.body[0], ast.Expr) and isinstance(ifn.body[0].value, ast.Call):
        c = ifn.body[0].value
        kw = {k.arg: k.value for k in c.keywords}
        bp = kw.get("build_parcels")
        ok = (isinstance(c.func, ast.Name) and c.func.id == FN_G and len(c.args) == 1 and set(kw) == set(g13)
              and all(isinstance(v, ast.Name) and v.id == k for k, v in kw.items() if k != "build_parcels")
              and isinstance(bp, ast.Call) and isinstance(bp.func, ast.Name) and bp.func.id == "k6b_screen_build_for_g"
              and [ast.unparse(a) for a in bp.args] == ["st", "build_parcels"] and not bp.keywords)
    chk(ok, f"W2 配地 If 之本體 ＝ 單一呼叫 {FN_G}(st, …·build_parcels=k6b_screen_build_for_g(st, build_parcels))")
    # W3
    inv = [n for n in ast.walk(main) if isinstance(n, ast.FunctionDef) and n.name == "_f3L_invalidate_g_cache"]
    ok = (len(inv) == 1 and any(isinstance(x, ast.Name) and x.id == "K6B_SCREEN_STAGE3_KEYS" for x in ast.walk(inv[0]))
          and any(isinstance(x, ast.Constant) and x.value == "f3_k6b_stage3_error" for x in ast.walk(inv[0])))
    chk(ok, "W3 _f3L_invalidate_g_cache 一併失效段三之結果（K6B_SCREEN_STAGE3_KEYS）與停機訊息（f3_k6b_stage3_error）")
    # W4
    sites, wrapped = [], []
    for rel in WF4_SITES:
        t = ast.parse(srcs[rel])
        for c in _wf4_calls(t):
            sites.append(f"{rel}:{c.lineno}")
            a0 = c.args[0] if c.args else None
            if isinstance(a0, ast.Call) and isinstance(a0.func, ast.Name) and a0.func.id in ("k6b_f4_ctx", "_k6b_f4_ctx"):
                wrapped.append(f"{rel}:{c.lineno}")
    chk(len(sites) == 5 and sites == wrapped, f"W4 wf_f4.compute 之呼叫點 {len(sites)}（期 5）皆以 k6b_f4_ctx(…) 為首參（{len(wrapped)}）")
    # W5
    bw = fns.get("_build_wf_ctx")
    rets = [n for n in ast.walk(bw) if isinstance(n, ast.Return) and isinstance(n.value, ast.Dict)] if bw else []
    keys = [k.value for k in rets[0].value.keys] if rets else []
    ok = (bw is not None and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name) and x.func.id == "k6b_stage3_selected"
                                 for x in ast.walk(bw)) and len(keys) == 14
          and all(any(isinstance(y, ast.Name) and y.id == "_s3" for y in ast.walk(rets[0].value.values[keys.index(k)]))
                  for k in ("build", "temp")))
    chk(ok, "W5 _build_wf_ctx 呼叫 k6b_stage3_selected；回傳之 ctx 仍 14 鍵、其 build／temp 依 _s3 取")
    # W6
    i0 = next((i + 1 for i, l in enumerate(lines) if "步驟 M：公共設施用地分配" in l), None)
    i1 = next((i + 1 for i, l in enumerate(lines) if i0 and i + 1 > i0 and "步驟 I：推送資料至下游分頁" in l), None)
    tp = sorted(n.lineno for n in ast.walk(main) if isinstance(n, ast.Name) and n.id == "temp_parcels"
                and isinstance(n.ctx, ast.Load) and i0 and i0 <= n.lineno <= i1)
    tm = sorted(n.lineno for n in ast.walk(main) if isinstance(n, ast.Name) and n.id == "_tp_m"
                and isinstance(n.ctx, ast.Load) and i0 and i0 <= n.lineno <= i1)
    chk(len(tp) == 2 and len(tm) == 4, f"W6 步驟 M 區內：temp_parcels 之讀 {len(tp)}（期 2：_tp_m 之定義與歸戶自有土地之圖示）·_tp_m 之讀 {len(tm)}（期 4）")
    # W7／W8
    chk(not any(x in src for x in STALE), "W7 二則過時之說明（段三尚未落地）已不在 app.py")
    n8 = sum(1 for x in ast.walk(fns[FN_PK]) if isinstance(x, ast.Assign) and len(x.targets) == 1
             and ast.unparse(x.targets[0]) == "st.session_state['f3_corner_cand_diag']" and ast.unparse(x.value) == "_corner_cand_diag")
    chk(n8 == 1, f"W8 {FN_PK} 內 st.session_state['f3_corner_cand_diag'] = _corner_cand_diag 恰一（{n8}）")
    return bad


def _mutants(srcs):
    """AST 突變四造（格式無關）：各回 (名, 突變後之 srcs)。"""
    out = []
    t = ast.parse(srcs["app.py"])
    main = _main_of(t)
    lines = srcs["app.py"].split("\n")
    # m1：g_kwargs 少一名
    t1 = copy.deepcopy(t); m1 = _main_of(t1)
    c = _target_if(m1, lines, KEY_PK).body[0].value
    gk = [k for k in c.keywords if k.arg == "g_kwargs"][0].value
    gk.keywords = gk.keywords[:-1]
    out.append(("m1 g_kwargs 少一名", dict(srcs, **{"app.py": ast.unparse(t1)})))
    # m2：配地改回段三前之 build
    t2 = copy.deepcopy(t); m2 = _main_of(t2)
    c = _target_if(m2, lines, KEY_G).body[0].value
    for k in c.keywords:
        if k.arg == "build_parcels":
            k.value = ast.Name("build_parcels", ast.Load())
    out.append(("m2 配地改回段三前之 build", dict(srcs, **{"app.py": ast.unparse(t2)})))
    # m3：app 之 wf_f4.compute 去 k6b_f4_ctx
    t3 = copy.deepcopy(t)
    for c in _wf4_calls(t3):
        if c.args and isinstance(c.args[0], ast.Call):
            c.args[0] = c.args[0].args[0]
    out.append(("m3 app 之 wf_f4.compute 去 k6b_f4_ctx", dict(srcs, **{"app.py": ast.unparse(t3)})))
    # m4：失效函式去段三鍵
    t4 = copy.deepcopy(t); m4 = _main_of(t4)
    inv = [n for n in ast.walk(m4) if isinstance(n, ast.FunctionDef) and n.name == "_f3L_invalidate_g_cache"][0]
    for n in ast.walk(inv):
        if isinstance(n, ast.Name) and n.id == "K6B_SCREEN_STAGE3_KEYS":
            n.id = "_K6B_REMOVED"
    out.append(("m4 失效函式去段三鍵", dict(srcs, **{"app.py": ast.unparse(t4)})))
    return out


def cmd_wiring(repo):
    try:
        srcs = {rel: open(os.path.join(repo, *rel.split("/")), encoding="utf-8").read() for rel in WF4_SITES}
    except Exception as e:  # noqa: BLE001
        print(f"🔴 受詞缺：{e} ⇒ 無從判定")
        return 3
    head = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    print(f"【F4 wiring】態 {head}（工作樹）")
    tree = ast.parse(srcs["app.py"])
    if FN_S3 not in {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}:
        print(f"🔴 受詞缺：app.py 模組層無 {FN_S3} ⇒ 無從判定")
        return 3
    bad = wiring_check(srcs, print)
    ir = 0
    if bad == 0:
        for name, ms in _mutants(srcs):
            sink = []
            b = wiring_check(ms, sink.append)
            ok = b > 0
            ir += (not ok)
            print(f"  {'✅' if ok else '🔴 器紅'} 丙 {name} ⇒ 紅項 {[x for x in sink if x.startswith('🔴')][:2]}")
    else:
        print("⚪ 丙部略（本部已紅）")
    print(f"⇒ rc {1 if (bad or ir) else 0}（不符 {bad}·器紅 {ir}）")
    return 1 if (bad or ir) else 0


# ───────────────────────── 接線（工項五）：動態 ─────────────────────────
def cmd_f4ctx(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    try:
        import selection_pipeline as sp
        fn = sp.k6b_f4_ctx
    except Exception as e:  # noqa: BLE001
        print(f"🔴 受詞缺：verify/selection_pipeline.py 無 k6b_f4_ctx（{type(e).__name__}）⇒ 無從判定")
        return 3
    A0, A1, B0, B1, X = [1], [2], [3], [4], object()
    ctx = {"0m": {"build": A0, "x": X}, "3.5m": {"build": A1, "x": X}}
    out = fn(ctx, {"0m": B0, "3.5m": B1})
    checks = [
        ("回傳新 dict（情境層與各 ctx 皆非輸入之物件）", out is not ctx and all(out[t] is not ctx[t] for t in ctx)),
        ("build 換為所給之段三前（同一物件）", out["0m"]["build"] is B0 and out["3.5m"]["build"] is B1),
        ("他鍵為輸入之同一物件", all(out[t]["x"] is X for t in ctx)),
        ("輸入未改", ctx["0m"]["build"] is A0 and ctx["3.5m"]["build"] is A1 and set(ctx["0m"]) == {"build", "x"}),
        ("情境集同輸入", set(out) == set(ctx)),
    ]
    bad = 0
    for n, ok in checks:
        bad += (not ok)
        print(f"  {'✅' if ok else '🔴'} k6b_f4_ctx：{n}")
    print(f"⇒ rc {1 if bad else 0}")
    return 1 if bad else 0


def cmd_wfctx(repo, sb):
    os.environ[ENV] = "on"
    f2 = _load_f2(repo)
    ns, fst, snap, cb_by, cad, tp, bp, params = f2._boot(repo, sb)
    if "k6b_stage3_fingerprint" not in ns or "k6b_stage3_selected" not in ns:
        print("🔴 受詞缺：app.py 模組層無 k6b_stage3_fingerprint／k6b_stage3_selected ⇒ 無從判定")
        return 3
    from selection_pipeline import run_corner_pk_k6b, k6b_stage3_pool_temp
    from stepg_pipeline import run_step_g
    from wg_g1_smoke import _reconstruct_sb_rows
    cb = list(cb_by.values())
    tag = "0m" if abs(sb) < 1e-9 else "3.5m"
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _o, w, fo, t2, b2 = run_corner_pk_k6b(ns, fst, cb, cad, params, tp, bp, sb, snapshot=snap)
        sg = run_step_g(ns, fst, cb, cad, snap, params, b2, w, fo, sb)
    base = dict(fst.session_state)
    base.pop("f3_total_burden_rate_from_finance", None)
    base.update({"f3_G_values": sg["g_rows"], "f3_classified_blocks": cb, "f3_temp_parcels": tp, "f3_build_parcels": bp,
                 "f3_wd2_pool_diag": sg["pool_diag"], "f3L_setback_default": sb,
                 "f3_sb_rows": _reconstruct_sb_rows(ns, cad, snap), "f3_cad_front_lengths": cad["front_lengths"],
                 "f3_cad_side_lengths_by_side": cad["side_lengths_by_side"], "f3_cad_front_lines": cad["front_lines"],
                 "f3_cad_side_lines_by_side": cad.get("side_lines_by_side", {}),
                 "f3_cad_alloc_dir": cad.get("alloc_dir_by_block", {}), "f3_manual_road_centerlines": cad.get("centerlines", {})})
    s3 = {"f3_k6b_stage3_temp": t2, "f3_k6b_stage3_build": b2, "f3_k6b_stage3_fp": ns["k6b_stage3_fingerprint"](bp, sb)}
    bad = 0

    def run(seed):
        with contextlib.redirect_stdout(io.StringIO()):
            return ns["_build_wf_ctx"](seed, tag, ns["__file__"])

    def chk(ok, msg):
        nonlocal bad
        bad += (not ok)
        print(f"  {'✅' if ok else '🔴'} {msg}")
    print(f"【F4 wfctx】退縮 {sb}·段三改動之 temp 片數 {sum(1 for x in t2 if '段三併出' in x)}")
    c4 = run(dict(base))
    chk(c4["build"] is bp and c4["temp"] is tp, "T4 無段三之鍵 ⇒ build／temp ＝ f3_build_parcels／f3_temp_parcels（同一物件）")
    c1 = run(dict(base, **s3))
    pool = k6b_stage3_pool_temp(t2)
    chk(c1["build"] is b2 and len(c1["temp"]) == len(pool) and all(a is b for a, b in zip(c1["temp"], pool)),
        f"T1 段三之鍵仍適用 ⇒ build ＝ 段三後（同一物件）、temp ＝ 去段三併出者（{len(pool)} 片·逐元素同一物件）")
    for name, seed in (("T2 指紋不符（退縮 +1）", dict(base, **s3, f3L_setback_default=sb + 1.0)),
                       ("T2′ 指紋不符（段三前之 build 少一宗）", dict(base, **s3, f3_build_parcels=bp[:-1])),
                       ("T3 前次段三停機之訊息在", dict(base, **s3, f3_k6b_stage3_error="x"))):
        try:
            run(seed)
            chk(False, f"{name} ⇒ 期 raise ／ 實 無")
        except RuntimeError as e:
            chk("重跑" in str(e), f"{name} ⇒ raise（{str(e)[:60]}…）")
    print(f"⇒ rc {1 if bad else 0}")
    return 1 if bad else 0


# ───────────────────────── 自檢 ─────────────────────────
_MINI = '''import os
X = 1
st = None


def helper(v):
    return v + X


def main():
    a = 1
    b = [1, 2]
    if st.button("執行第 1 宗街角地優先權選位（左右側獨立）", key="k"):
        c = a + helper(2)
        for i in b:
            c += i
        st.session_state["w"] = c
    _btn_clicked = True
    _auto_recalc = False
    if _btn_clicked or _auto_recalc:
        d = [a * i for i in b]
        st.session_state["g"] = d
    return a
'''


def _mini_extract(src, mut=None):
    """合成之「正確抽出」（mut ⇒ 四種突變之一）。"""
    fpk = ("def f3_screen_corner_pk_run(st, *, a, b):\n    \"\"\"doc\"\"\"\n    c = a + helper(2)\n    for i in b:\n        c += i\n"
           "    st.session_state[\"w\"] = c\n\n\n")
    fg = ("def f3_screen_stepg_run(st, *, a, b):\n    d = [a * i for i in b]\n    st.session_state[\"g\"] = d\n\n\n")
    call_pk = "        f3_screen_corner_pk_run(st, b=b, a=a)\n"
    call_g = "        f3_screen_stepg_run(st, a=a, b=b)\n"
    if mut == "body":
        fpk = fpk.replace("helper(2)", "helper(3)")
    if mut == "param":
        fg = fg.replace("(st, *, a, b)", "(st, *, a, b, extra)")
        call_g = "        f3_screen_stepg_run(st, a=a, b=b, extra=a)\n"
    if mut == "scope":
        fg = fg.replace("d = [a * i for i in b]", "d = [a * i for i in b] + [X] + [zz]")
    out = src
    out = out.replace('        c = a + helper(2)\n        for i in b:\n            c += i\n        st.session_state["w"] = c\n', call_pk)
    out = out.replace('        d = [a * i for i in b]\n        st.session_state["g"] = d\n', call_g)
    if mut == "main":
        out = out.replace("    return a\n", "    a = a + 0\n    return a\n")
    out = out.replace("def main():", fpk + fg + "def main():")
    return out


def cmd_selftest():
    n, ok_n = 0, 0

    def expect(name, got_bad, want_red):
        nonlocal n, ok_n
        n += 1
        ok = (got_bad > 0) == want_red
        ok_n += ok
        print(f"  {'✅' if ok else '🔴'} {name}：期 {'紅' if want_red else '綠'} ／ 實 {'紅' if got_bad else '綠'}（{got_bad}）")
    sink = []
    expect("ast·原封之合成抽出", ast_check(_MINI, _mini_extract(_MINI), sink.append), False)
    for m in ("body", "param", "main", "scope"):
        expect(f"ast·突變 {m}", ast_check(_MINI, _mini_extract(_MINI, m), sink.append), True)
    base = [{"暫編地號": "R1-1", "G(㎡)": 10.0, "幾何面積(㎡)": 10.0, "cut_coords": [[0, 0], [1, 0], [1, 1], [0, 0]]},
            {"暫編地號": "R1-抵費地-1", "G(㎡)": 0.0, "幾何面積(㎡)": 5.0, "cut_coords": [[0, 0], [2, 0], [2, 2], [0, 2], [0, 0]]},
            {"暫編地號": "R1-抵費地-2", "G(㎡)": 0.0, "幾何面積(㎡)": 0.0, "cut_coords": []}]
    rot = copy.deepcopy(base[:2])
    rot[1]["cut_coords"] = [[2, 2], [0, 2], [0, 0], [2, 0], [2, 2]]
    b1, z1 = compare_rows(base, rot, sink.append)
    expect("列比對·環旋轉 ＋ 一側獨有之零面積列（⇒ Z）", b1, False)
    n += 1
    okz = z1 == [("harness", "R1-抵費地-2")]
    ok_n += okz
    print(f"  {'✅' if okz else '🔴'} 列比對·Z 之內容：期 [('harness','R1-抵費地-2')] ／ 實 {z1}")
    per = copy.deepcopy(base)
    per[0]["G(㎡)"] = 10.01
    expect("列比對·G 差 0.01", compare_rows(base, per, sink.append)[0], True)
    nz = copy.deepcopy(base[:2])
    expect("列比對·一側獨有之非零面積列", compare_rows(nz + [{"暫編地號": "X", "G(㎡)": 1.0, "幾何面積(㎡)": 1.0}], nz, sink.append)[0], True)
    rev = copy.deepcopy(base)
    rev[0], rev[1] = rev[1], rev[0]
    expect("列比對·共有列之次序不同", compare_rows(base, rev, sink.append)[0], True)
    print(f"selftest {ok_n}/{n} ⇒ {'✅' if ok_n == n else '🔴'}")
    return 0 if ok_n == n else 1


def main(argv):
    try:
        if len(argv) == 2 and argv[1] == "selftest":
            return cmd_selftest()
        if len(argv) == 4 and argv[1] in ("census", "ast"):
            return (cmd_census if argv[1] == "census" else cmd_ast)(argv[2], argv[3])
        if len(argv) == 3 and argv[1] in ("wiring", "f4ctx"):
            return (cmd_wiring if argv[1] == "wiring" else cmd_f4ctx)(argv[2])
        if len(argv) == 4 and argv[1] == "wfctx":
            return cmd_wfctx(argv[2], float(argv[3]))
        if len(argv) >= 5 and argv[1] == "parity":
            rest = argv[5:]
            perturb = "--perturb" in rest
            rest = [x for x in rest if x != "--perturb"]
            if len(rest) > 1:
                return 2
            return cmd_parity(argv[2], float(argv[3]), argv[4], rest[0] if rest else None, perturb)
    except ValueError:
        return 2
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
