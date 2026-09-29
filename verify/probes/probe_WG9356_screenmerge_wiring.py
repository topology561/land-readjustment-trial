# -*- coding: utf-8 -*-
"""W-G.9-356 量測器（發單側窗五十二擬·檔 F15·⛔ 由受單側改一字）：末端塊之合併再試之畫面路徑之接線與 `main()` 之合成案。

緣由：`W-G.9-355`（規格單流程之首張）之 `§四-2`——以程式字樣為錨之接線檢查須待碼成方能寫 ⇒ 發單側讀 CC 之碼
（`f173a4e`）後補寫。受詞之行為（三出口之編排、四注入物、顯示函式）已由 F14（`probe_WG9355_screenmerge.py`）之
`selftest`／`run` 量之；本器量**程式字樣**（防日後之漂移）與 `main()` 內之二處（`run_all`／F14 皆⛔ 執行之·`自誤 517`）。

受詞（`app.py`·工作樹）：
  f3_screen_k6b_stage3／f3_screen_end_block_merge／k6b_screen_callbacks／end_block_merge_rows（模組層）、
  K6B_SCREEN_TRIAL_KEYS／SS_END_BLOCK_MODE／SS_END_BLOCK_MERGE（模組層常數）、main() 內之 _f3L_invalidate_g_cache 與
  成果區「末端塊之合併再試」之區塊。

子命令（一律 python verify/probes/probe_WG9356_screenmerge_wiring.py <子命令> <repo>）：
  wiring <repo>
    W1 `R-1` 三出口：段三之畫面入口（巢狀 def 之外）之 return 恰 3，各 ＝ 呼叫同一巢狀函式，該函式呼
       f3_screen_end_block_merge(st, …) 恰 1；各 return 之前、同一敘述列中有真 st 之 f3_screen_corner_pk_run(st, …)，
       且 return 所傳之宗地 ＝ 該次街角選位所用之宗地（`**pk_kwargs` ⇒ temp0／build0；`**dict(…, temp_parcels=X, build_parcels=Y)` ⇒ X／Y）。
    W2 `R-1` 單一真相源：end_block_merge_run 於 app.py 中唯以名呼叫（⛔ 別名、⛔ 作引數傳遞、⛔ 預綁）、呼叫恰 1、
       且在 f3_screen_end_block_merge 內；f3_screen_end_block_merge 之呼叫恰 1、在段三之畫面入口內。
    W3 `R-5` 單一真相源：k6b_screen_callbacks 內有巢狀 a_prime／trial_winner／alloc_state／alloc_eval 且回此四鍵；app.py 他處
       ⛔ 有同名之巢狀 def；段三之畫面入口與合併再試之入口各呼 k6b_screen_callbacks 恰 1；k6b_stage3_run 之第 8〜10 引數
       ＝ 其回傳之 a_prime／trial_winner／alloc_state，end_block_merge_run 之第 8〜10 引數 ＝ a_prime／alloc_eval／alloc_state。
    W4 `R-3`／`R-4` 試算：alloc_state 與 alloc_eval 內，`<session>[SS_END_BLOCK_MODE] = 'trial'` 先於同一敘述列中之
       f3_screen_stepg_run(<代理 st>, …)（代理 st ＝ 同函式內 `_K6BTrialSt(st)` 之所賦）。
    W5 `R-6` 隔離：SS_END_BLOCK_MODE 之值 ∈ K6B_SCREEN_TRIAL_KEYS（literal_eval）；合併再試之入口於呼叫 end_block_merge_run
       之 try 之前以 K6B_SCREEN_TRIAL_KEYS 存、其 finally 以 K6B_SCREEN_TRIAL_KEYS 復並復 K917_DROPPED。
    W6 `R-7` 紀錄：合併再試之入口於該 try 之後寫 `[SS_END_BLOCK_MERGE] ＝ rec`、`['f3_end_block_merge_log'] ＝ log`（rec／log ＝
       end_block_merge_run 之第 4／3 回傳）；段三之畫面入口於其首個 if 之前去此二鍵。
    W7 `R-12` 失效：main() 內 _f3L_invalidate_g_cache 去 SS_END_BLOCK_MERGE 與 'f3_end_block_merge_log'。
    W8 `R-12` 顯示之接線：main() 內同一敘述列中，`X = st.session_state.get(SS_END_BLOCK_MERGE)` 緊接 `if X is not None:`，其本體呼
       end_block_merge_rows(X, st.session_state.get('f3_end_block_merge_log'))；位置 ＝ 末端塊之評選（_eb352）之 if 之後、_adj351_bf
       之賦值之前。
    S1 `自誤 517`：W8 之二句（賦值 ＋ if）自 main() 抽出，以假 st 實際執行三情形（有標的而有逐列／無標的而無逐列／無紀錄），
       期值為本器另寫之字面（⛔ 呼叫受測函式求期）。
    S2 `自誤 517`：main() 內之 _f3L_invalidate_g_cache 抽出以假 st 實際執行：所列之鍵皆去、他鍵留、f3_g_needs_rerun ＝ True
       （該函式以 `except Exception: pass` 包裹 ⇒ 以結果判、⛔ 以「未拋」判）。
    本部全綠時另施 14 種原始碼突變，每一突變須使其所指之項轉紅（器紅 ⇒ rc 1）。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import ast, contextlib, copy, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FN_S3, FN_EBM, FN_CB, FN_ROWS = ("f3_screen_k6b_stage3", "f3_screen_end_block_merge", "k6b_screen_callbacks",
                                 "end_block_merge_rows")
CB4 = ("a_prime", "trial_winner", "alloc_state", "alloc_eval")
LOGK = "f3_end_block_merge_log"


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


# ── AST 之小工具 ──
def _top(tree):
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


def _consts(tree):
    return {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
            and isinstance(n.targets[0], ast.Name)}


def _walk_own(fn):
    """fn 之節點，⛔ 入巢狀之 def／lambda。"""
    todo = [s for s in fn.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))]
    while todo:
        n = todo.pop()
        yield n
        for c in ast.iter_child_nodes(n):
            if not isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                todo.append(c)


def _nested(fn):
    return {n.name: n for n in ast.walk(fn) if isinstance(n, ast.FunctionDef) and n is not fn}


def _is_call(n, name):
    return isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name


def _calls(node, name, own=False):
    it = _walk_own(node) if own else ast.walk(node)
    return [n for n in it if _is_call(n, name)]


def _stmt_lists(node):
    for n in ast.walk(node):
        for fld in ("body", "orelse", "finalbody"):
            b = getattr(n, fld, None)
            if isinstance(b, list) and b and isinstance(b[0], ast.stmt):
                yield b
        for h in getattr(n, "handlers", []) or []:
            yield h.body


def _uparse(n):
    try:
        return ast.unparse(n)
    except Exception:  # noqa: BLE001
        return "<?>"


def _is_sub(n, key_name=None, key_str=None):
    """n ＝ `<x>[Name key_name]` 或 `<x>['key_str']`。"""
    if not isinstance(n, ast.Subscript):
        return False
    s = n.slice
    if key_name is not None:
        return isinstance(s, ast.Name) and s.id == key_name
    return isinstance(s, ast.Constant) and s.value == key_str


def _is_pop(n, key_name=None, key_str=None):
    if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "pop" and n.args):
        return False
    a = n.args[0]
    if key_name is not None:
        return isinstance(a, ast.Name) and a.id == key_name
    return isinstance(a, ast.Constant) and a.value == key_str


def _main_of(tree):
    return _top(tree).get("main")


# ── 接線 ──
def _w1(top):
    s3 = top.get(FN_S3)
    if s3 is None:
        return False, "段三之畫面入口缺"
    rets = [n for n in _walk_own(s3) if isinstance(n, ast.Return)]
    nest = _nested(s3)
    tgt = {n.value.func.id for n in rets if isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)}
    if len(rets) != 3 or len(tgt) != 1 or next(iter(tgt)) not in nest:
        return False, f"return {len(rets)}（期 3）；所呼 {sorted(tgt)}（期 恰 1 且為巢狀函式）"
    em = nest[next(iter(tgt))]
    ebm = _calls(em, FN_EBM)
    if len(ebm) != 1 or not ebm[0].args or not (isinstance(ebm[0].args[0], ast.Name) and ebm[0].args[0].id == "st"):
        return False, f"{em.name} 內 {FN_EBM}(st, …) 之呼叫 {len(ebm)}（期 1·首參 st）"
    # temp0／build0 之源
    src0 = [n for n in s3.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple)
            and [_uparse(e) for e in n.targets[0].elts] == ["temp0", "build0"]
            and _uparse(n.value) == "(pk_kwargs['temp_parcels'], pk_kwargs['build_parcels'])"]
    if len(src0) != 1:
        return False, "temp0／build0 ＝ pk_kwargs 之 temp_parcels／build_parcels 之賦值缺"
    bad = []
    for lst in _stmt_lists(s3):
        for i, st_ in enumerate(lst):
            if not (isinstance(st_, ast.Return) and st_ in rets):
                continue
            pk = None
            for prev in reversed(lst[:i]):
                if isinstance(prev, ast.Return):
                    break
                if isinstance(prev, ast.Expr) and _is_call(prev.value, "f3_screen_corner_pk_run"):
                    pk = prev.value
                    break
            if pk is None or not (pk.args and isinstance(pk.args[0], ast.Name) and pk.args[0].id == "st"):
                bad.append(f"L{st_.lineno}：前無真 st 之街角選位")
                continue
            kw = pk.keywords
            if len(kw) == 1 and kw[0].arg is None and _uparse(kw[0].value) == "pk_kwargs":
                exp = ["temp0", "build0"]
            elif len(kw) == 1 and kw[0].arg is None and _is_call(kw[0].value, "dict"):
                d = {k.arg: _uparse(k.value) for k in kw[0].value.keywords}
                exp = [d.get("temp_parcels"), d.get("build_parcels")]
            else:
                bad.append(f"L{st_.lineno}：街角選位之引數形未識")
                continue
            got = [_uparse(a) for a in st_.value.args[:2]]
            if got != exp:
                bad.append(f"L{st_.lineno}：合併再試之宗地 {got} ≠ 街角選位所用 {exp}")
    return (not bad), f"{bad}" if bad else f"三出口皆經 {em.name} → {FN_EBM}(st, …)"


def _w2(tree, top):
    loads = [n for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "end_block_merge_run"]
    calls = [n for n in ast.walk(tree) if _is_call(n, "end_block_merge_run")]
    as_func = {id(c.func) for c in calls}
    stray = [n.lineno for n in loads if id(n) not in as_func]
    ebm = top.get(FN_EBM)
    in_ebm = len(_calls(ebm, "end_block_merge_run")) if ebm else 0
    c_ebm = [n for n in ast.walk(tree) if _is_call(n, FN_EBM)]
    s3 = top.get(FN_S3)
    in_s3 = len(_calls(s3, FN_EBM)) if s3 else 0
    ok = not stray and len(calls) == 1 and in_ebm == 1 and len(c_ebm) == 1 and in_s3 == 1
    return ok, (f"end_block_merge_run：呼叫 {len(calls)}（期 1）·在合併再試之入口 {in_ebm}·非呼叫之引用列 {stray}；"
                f"{FN_EBM} 之呼叫 {len(c_ebm)}（期 1）·在段三之畫面入口 {in_s3}")


def _cb_var(fn):
    for n in ast.walk(fn):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
                and _is_call(n.value, FN_CB):
            return n.targets[0].id
    return None


def _slot_keys(call, var, idx):
    out = []
    for i in idx:
        a = call.args[i] if len(call.args) > i else None
        if isinstance(a, ast.Subscript) and isinstance(a.value, ast.Name) and a.value.id == var \
                and isinstance(a.slice, ast.Constant):
            out.append(a.slice.value)
        else:
            out.append(_uparse(a) if a is not None else None)
    return out


def _w3(tree, top):
    cb = top.get(FN_CB)
    if cb is None:
        return False, f"{FN_CB} 缺"
    nest = _nested(cb)
    rets = [n for n in _walk_own(cb) if isinstance(n, ast.Return)]
    ret_ok = (len(rets) == 1 and isinstance(rets[0].value, ast.Dict)
              and {k.value: _uparse(v) for k, v in zip(rets[0].value.keys, rets[0].value.values)
                   if isinstance(k, ast.Constant)} == {k: k for k in CB4})
    dup = sorted({f"{f.name}.{n.name}" for f in top.values() if f is not cb
                  for n in ast.walk(f) if isinstance(n, ast.FunctionDef) and n is not f and n.name in CB4})
    notes = []
    s3, ebm = top.get(FN_S3), top.get(FN_EBM)
    ok_s3 = ok_ebm = False
    if s3 is not None:
        v = _cb_var(s3)
        k3 = _calls(s3, "k6b_stage3_run")
        ok_s3 = (len(_calls(s3, FN_CB)) == 1 and v is not None and len(k3) == 1
                 and _slot_keys(k3[0], v, (7, 8, 9)) == ["a_prime", "trial_winner", "alloc_state"])
        notes.append(f"段三：{_slot_keys(k3[0], v, (7, 8, 9)) if k3 and v else '—'}")
    if ebm is not None:
        v = _cb_var(ebm)
        km = _calls(ebm, "end_block_merge_run")
        ok_ebm = (len(_calls(ebm, FN_CB)) == 1 and v is not None and len(km) == 1
                  and _slot_keys(km[0], v, (7, 8, 9)) == ["a_prime", "alloc_eval", "alloc_state"])
        notes.append(f"合併再試：{_slot_keys(km[0], v, (7, 8, 9)) if km and v else '—'}")
    ok = set(CB4) <= set(nest) and ret_ok and not dup and ok_s3 and ok_ebm
    return ok, f"巢狀 {sorted(set(CB4) & set(nest))}；回四鍵 {ret_ok}；他處同名 {dup}；" + "；".join(notes)


def _w4(top):
    cb = top.get(FN_CB)
    if cb is None:
        return False, f"{FN_CB} 缺"
    nest = _nested(cb)
    res = {}
    for nm in ("alloc_state", "alloc_eval"):
        f = nest.get(nm)
        if f is None:
            res[nm] = "缺"
            continue
        px = {n.targets[0].id for n in ast.walk(f) if isinstance(n, ast.Assign) and len(n.targets) == 1
              and isinstance(n.targets[0], ast.Name) and _is_call(n.value, "_K6BTrialSt")
              and [_uparse(a) for a in n.value.args] == ["st"]}
        hit = False
        for lst in _stmt_lists(f):
            for i, s in enumerate(lst):
                if isinstance(s, ast.Expr) and _is_call(s.value, "f3_screen_stepg_run") and s.value.args \
                        and isinstance(s.value.args[0], ast.Name) and s.value.args[0].id in px:
                    hit = hit or any(isinstance(p, ast.Assign) and len(p.targets) == 1
                                     and _is_sub(p.targets[0], key_name="SS_END_BLOCK_MODE")
                                     and isinstance(p.value, ast.Constant) and p.value.value == "trial"
                                     for p in lst[:i])
        res[nm] = hit
    return all(v is True for v in res.values()), f"{res}"


def _w5(tree, top):
    c = _consts(tree)
    try:
        mode = ast.literal_eval(c["SS_END_BLOCK_MODE"].value)
        keys = ast.literal_eval(c["K6B_SCREEN_TRIAL_KEYS"].value)
    except Exception as e:  # noqa: BLE001
        return False, f"常數無從取：{type(e).__name__}"
    ebm = top.get(FN_EBM)
    if ebm is None:
        return False, f"{FN_EBM} 缺"
    tries = [(i, s) for i, s in enumerate(ebm.body) if isinstance(s, ast.Try) and _calls(s, "end_block_merge_run")]
    if len(tries) != 1:
        return False, f"含 end_block_merge_run 之 try {len(tries)}（期 1）"
    i, t = tries[0]
    saved = any(isinstance(n, ast.DictComp) and any(isinstance(g.iter, ast.Name) and g.iter.id == "K6B_SCREEN_TRIAL_KEYS"
                                                    for g in n.generators)
                for s in ebm.body[:i] for n in ast.walk(s))
    fin = t.finalbody
    rest = any(isinstance(s, ast.For) and isinstance(s.iter, ast.Name) and s.iter.id == "K6B_SCREEN_TRIAL_KEYS"
               for s in fin)
    k917 = {_uparse(s.value.func) for s in fin if isinstance(s, ast.Expr) and isinstance(s.value, ast.Call)}
    ok = mode in keys and saved and rest and {"K917_DROPPED.clear", "K917_DROPPED.update"} <= k917
    return ok, f"SS_END_BLOCK_MODE＝{mode!r} ∈ 鍵 {mode in keys}；try 前存 {saved}；finally 復 {rest}；K917 {sorted(k917)}"


def _w6(top):
    ebm, s3 = top.get(FN_EBM), top.get(FN_S3)
    if ebm is None or s3 is None:
        return False, "受詞缺"
    ti = [i for i, s in enumerate(ebm.body) if isinstance(s, ast.Try) and _calls(s, "end_block_merge_run")]
    if len(ti) != 1:
        return False, "try 無從定"
    t = ebm.body[ti[0]]
    asg = [n for n in ast.walk(t) if isinstance(n, ast.Assign) and _calls(n, "end_block_merge_run")]
    tgt = [_uparse(e) for e in asg[0].targets[0].elts] if asg and isinstance(asg[0].targets[0], ast.Tuple) else []
    if len(tgt) != 4:
        return False, f"end_block_merge_run 之回傳之受值 {tgt}"
    after = ebm.body[ti[0] + 1:]
    w_rec = any(isinstance(s, ast.Assign) and _is_sub(s.targets[0], key_name="SS_END_BLOCK_MERGE")
                and _uparse(s.value) == tgt[3] for s in after)
    w_log = any(isinstance(s, ast.Assign) and _is_sub(s.targets[0], key_str=LOGK)
                and _uparse(s.value) == tgt[2] for s in after)
    before = ebm.body[:ti[0]]
    in_try = any(isinstance(n, ast.Assign) and (_is_sub(n.targets[0], key_name="SS_END_BLOCK_MERGE")
                                                or _is_sub(n.targets[0], key_str=LOGK))
                 for s in before + [t] for n in ast.walk(s))
    fi = next((i for i, s in enumerate(s3.body) if isinstance(s, ast.If)), len(s3.body))
    head = s3.body[:fi]
    pop_rec = any(_is_pop(n, key_name="SS_END_BLOCK_MERGE") for s in head for n in ast.walk(s))
    pop_log = any(_is_pop(n, key_str=LOGK) for s in head for n in ast.walk(s))
    ok = w_rec and w_log and not in_try and pop_rec and pop_log
    return ok, (f"try 後寫 rec {w_rec}／log {w_log}；try 內或其前寫 {in_try}；"
                f"段三之畫面入口之首去 rec {pop_rec}／log {pop_log}")


def _inv_of(main):
    inv = [n for n in ast.walk(main) if isinstance(n, ast.FunctionDef) and n.name == "_f3L_invalidate_g_cache"]
    return inv[0] if len(inv) == 1 else None


def _w7(main):
    if main is None:
        return False, "main 缺"
    inv = _inv_of(main)
    if inv is None:
        return False, "_f3L_invalidate_g_cache 缺或非唯一"
    a = any(_is_pop(n, key_name="SS_END_BLOCK_MERGE") for n in ast.walk(inv))
    b = any(_is_pop(n, key_str=LOGK) for n in ast.walk(inv))
    return a and b, f"去 SS_END_BLOCK_MERGE {a}；去 {LOGK} {b}"


def _get_call(n, key_name=None, key_str=None):
    """n ＝ st.session_state.get(<key>)。"""
    if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "get"
            and _uparse(n.func.value) == "st.session_state" and len(n.args) == 1 and not n.keywords):
        return False
    a = n.args[0]
    if key_name is not None:
        return isinstance(a, ast.Name) and a.id == key_name
    return isinstance(a, ast.Constant) and a.value == key_str


def _find_disp(main):
    """回 (敘述列, 賦值之 idx) 或 None。"""
    for lst in _stmt_lists(main):
        for i, s in enumerate(lst):
            if isinstance(s, ast.Assign) and len(s.targets) == 1 and isinstance(s.targets[0], ast.Name) \
                    and _get_call(s.value, key_name="SS_END_BLOCK_MERGE") and i + 1 < len(lst) \
                    and isinstance(lst[i + 1], ast.If):
                return lst, i
    return None


def _w8(main):
    if main is None:
        return False, "main 缺"
    f = _find_disp(main)
    if f is None:
        return False, "`X = st.session_state.get(SS_END_BLOCK_MERGE)` ＋ if 之二句缺"
    lst, i = f
    x = lst[i].targets[0].id
    t = lst[i + 1].test
    t_ok = (isinstance(t, ast.Compare) and isinstance(t.left, ast.Name) and t.left.id == x
            and len(t.ops) == 1 and isinstance(t.ops[0], ast.IsNot)
            and isinstance(t.comparators[0], ast.Constant) and t.comparators[0].value is None)
    rc = [n for n in ast.walk(lst[i + 1]) if _is_call(n, FN_ROWS)]
    r_ok = (len(rc) == 1 and len(rc[0].args) == 2 and isinstance(rc[0].args[0], ast.Name) and rc[0].args[0].id == x
            and _get_call(rc[0].args[1], key_str=LOGK))
    eb = [j for j, s in enumerate(lst) if isinstance(s, ast.Assign) and _uparse(s.targets[0]) == "_eb352"]
    ad = [j for j, s in enumerate(lst) if isinstance(s, ast.Assign) and _uparse(s.targets[0]) == "_adj351_bf"]
    p_ok = (len(eb) == 1 and len(ad) == 1 and eb[0] + 1 < i and isinstance(lst[eb[0] + 1], ast.If)
            and i + 1 < ad[0])
    return t_ok and r_ok and p_ok, f"if 之式 {t_ok}；{FN_ROWS}(X, …get('{LOGK}')) {r_ok}；位置 {p_ok}"


# ── 合成案（自誤 517）──
class _NullCM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def _f(*a, **k):
            self.calls.append((name, a, k))
            return _NullCM()
        return _f


REC = {"退縮": 3.5, "標的": [["QA", "left"], ["QB", "right"]], "皆未達": {"QA": ["left"]},
       "競合": [{"形": "一", "列": [["QA", "左", "K(4)", 66.49], ["QB", "右", "K(3)", 237.57]]}]}
LOG = [{"序": 1, "街廓": "QB", "端": "右", "候選": "K(3)", "結果": "成", "檢核": None},
       {"序": "後處理", "街廓": "QB", "端": "右", "候選": "K(4)", "結果": "成", "檢核": "通過"}]
ROWS_EXP = [{"序": "1", "街廓": "QB", "端": "右", "候選": "K(3)", "結果": "成", "檢核": "—"},
            {"序": "後處理", "街廓": "QB", "端": "右", "候選": "K(4)", "結果": "成", "檢核": "通過"}]
NEED = ["QA", "QB", "K(4)", "K(3)", "66.49", "237.57", "強制抵費地", "3.5"]


def _ns_for(src, tree):
    c = _consts(tree)
    top = _top(tree)
    parts = [ast.get_source_segment(src, c[k]) for k in ("SS_END_BLOCK_MERGE", "K6B_SCREEN_STAGE3_KEYS") if k in c]
    if FN_ROWS in top:
        parts.append(ast.get_source_segment(src, top[FN_ROWS]))
    ns = {}
    exec(compile("\n\n".join(parts), "<f15_extract>", "exec"), ns)
    return ns


def _s1(src, tree):
    main = _main_of(tree)
    f = _find_disp(main) if main is not None else None
    if f is None:
        return False, "抽不到顯示區塊"
    lst, i = f
    try:
        import pandas as pd
        base = _ns_for(src, tree)
        code = compile(ast.Module(body=lst[i:i + 2], type_ignores=[]), "<main_ebm_block>", "exec")
        out = {}
        for tag, ss in (("有", {base["SS_END_BLOCK_MERGE"]: copy.deepcopy(REC), LOGK: copy.deepcopy(LOG)}),
                        ("空", {base["SS_END_BLOCK_MERGE"]: {"退縮": 0.0, "標的": [], "皆未達": {}}, LOGK: []}),
                        ("無", {"其他": 1})):
            fst = _FakeSt(ss)
            g = dict(base, st=fst, _pd=pd)
            exec(code, g)
            out[tag] = fst.calls
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    have = out["有"]
    exps = [c for c in have if c[0] == "expander"]
    caps = "\n".join(str(c[1][0]) for c in have if c[0] == "caption")
    dfs = [c[1][0] for c in have if c[0] == "dataframe"]
    empty = out["空"]
    checks = {
        "有·expander 1（展開）": len(exps) == 1 and "末端塊之合併再試" in str(exps[0][1][0]) and exps[0][2].get("expanded") is True,
        "有·行載標的／競合／皆未達／退縮": not [s for s in NEED if s not in caps],
        "有·逐列表 1 ＝ 紀錄之列（字串·None ⇒ —）": len(dfs) == 1 and dfs[0].to_dict("records") == ROWS_EXP,
        "有·無 st.error": not [c for c in have if c[0] == "error"],
        "空·expander 1（收合）·含無標的·無逐列表": ([c[2].get("expanded") for c in empty if c[0] == "expander"] == [False]
                                   and any("無標的" in str(c[1][0]) for c in empty if c[0] == "caption")
                                   and not [c for c in empty if c[0] == "dataframe"]),
        "無·⛔ 顯示": out["無"] == [],
    }
    bad = [k for k, v in checks.items() if not v]
    return (not bad), f"不符 {bad}" if bad else "三情形皆符"


def _s2(src, tree):
    main = _main_of(tree)
    inv = _inv_of(main) if main is not None else None
    if inv is None:
        return False, "抽不到 _f3L_invalidate_g_cache"
    try:
        base = _ns_for(src, tree)
        mk, s3k = base["SS_END_BLOCK_MERGE"], tuple(base["K6B_SCREEN_STAGE3_KEYS"])
        gone = ["f3_G_values", "f3_G_trace", "f3_corner_winners", "f3L_corner_winners", *s3k,
                "f3_k6b_stage3_error", mk, LOGK]
        ss = {k: "舊" for k in gone}
        ss["留"] = "留"
        fst = _FakeSt(ss)
        g = dict(base, st=fst)
        exec(compile(ast.Module(body=[inv], type_ignores=[]), "<main_inv>", "exec"), g)
        g["_f3L_invalidate_g_cache"]()
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    left = [k for k in gone if k in ss]
    ok = not left and ss.get("留") == "留" and ss.get("f3_g_needs_rerun") is True
    return ok, f"未去 {left}；他鍵留 {ss.get('留') == '留'}；f3_g_needs_rerun {ss.get('f3_g_needs_rerun')!r}"


def _checks(src):
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [("W0 可剖析", False, f"{e}")]
    top = _top(tree)
    main = _main_of(tree)
    miss = [n for n in (FN_S3, FN_EBM, FN_CB, FN_ROWS) if n not in top]
    res = [("W0 受詞在模組層", not miss, f"缺 {miss}")]
    for name, fn in (("W1 R-1 三出口", lambda: _w1(top)), ("W2 R-1 單一真相源", lambda: _w2(tree, top)),
                     ("W3 R-5 四注入物之單一真相源", lambda: _w3(tree, top)), ("W4 R-3／R-4 試算 'trial'", lambda: _w4(top)),
                     ("W5 R-6 隔離", lambda: _w5(tree, top)), ("W6 R-7 紀錄", lambda: _w6(top)),
                     ("W7 R-12 失效之二鍵", lambda: _w7(main)), ("W8 R-12 顯示之接線", lambda: _w8(main)),
                     ("S1 自誤517 顯示區塊之合成案", lambda: _s1(src, tree)),
                     ("S2 自誤517 失效函式之合成案", lambda: _s2(src, tree))):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ok, note = fn()
        except Exception as e:  # noqa: BLE001
            ok, note = False, f"器拋 {type(e).__name__}: {e}"
        res.append((name, ok, note))
    return res


# ── 突變（每一須使其所指之項轉紅）──
def _mut_list():
    T = "K6B_SCREEN_TRIAL_KEYS"
    return [
        ("M1 出口①⛔ 辦合併再試", "W1",
         [("        return _end_merge(temp0, build0, [], _order, False)",
           "        return {'temp': temp0, 'build': build0, 'log': [], 'order': _order, 'ran': False}")]),
        ("M2 出口③以段三前之宗地辦合併再試", "W1",
         [("    return _end_merge(temp2, build2, log, order, True)",
           "    return _end_merge(temp0, build0, log, order, True)")]),
        ("M3 以別名呼叫單一真相源", "W2",
         [("temp3, build3, log, rec = end_block_merge_run(", "temp3, build3, log, rec = globals()['end_block_merge_run']("),
          ]),
        ("M4 合併再試另寫 alloc_eval", "W3",
         [("    _cb = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)\n    _saved = {k: _cp_ebm",
           "    _cb = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)\n\n"
           "    def alloc_eval(temp, build):\n        return {}\n    _saved = {k: _cp_ebm"),
          ("_cb['a_prime'], _cb['alloc_eval'], _cb['alloc_state'],", "_cb['a_prime'], alloc_eval, _cb['alloc_state'],")]),
        ("M5 合併再試之注入物錯位", "W3",
         [("_cb['a_prime'], _cb['alloc_eval'], _cb['alloc_state'],", "_cb['a_prime'], _cb['alloc_state'], _cb['alloc_state'],")]),
        ("M6 段三之試算配地⛔ 設 'trial'", "W4",
         [("_ss[SS_END_BLOCK_MODE] = 'trial'   # 🆕", "pass   # 🆕")]),
        ("M7 合併再試之試算配地⛔ 設 'trial'", "W4",
         [("                _ss[SS_END_BLOCK_MODE] = 'trial'\n                f3_screen_stepg_run(_px, **dict(",
           "                f3_screen_stepg_run(_px, **dict(")]),
        ("M8 試算旗標⛔ 入隔離之鍵", "W5", [("    'f3_end_block_mode',\n", "")]),
        ("M9 合併再試之 finally ⛔ 復原", "W5",
         [("        for _k in " + T + ":\n            if _k in _saved:\n                _ss[_k] = _saved[_k]\n"
           "            else:\n                _ss.pop(_k, None)\n        K917_DROPPED.clear()\n"
           "        K917_DROPPED.update(_k917_saved)\n    _ss[SS_END_BLOCK_MERGE] = rec",
           "        pass\n    _ss[SS_END_BLOCK_MERGE] = rec")]),
        ("M10 逐列紀錄⛔ 寫", "W6", [("    _ss['f3_end_block_merge_log'] = log\n", "")]),
        ("M11 段三之畫面入口之首⛔ 去前次之紀錄", "W6",
         [("    _ss.pop(SS_END_BLOCK_MERGE, None)\n    _ss.pop('f3_end_block_merge_log', None)\n\n    def _end_merge",
           "\n    def _end_merge")]),
        ("M12 失效函式⛔ 去紀錄", "S2",
         [("                            _st_inv.session_state.pop(SS_END_BLOCK_MERGE, None)\n", "")]),
        ("M13 顯示⛔ 傳逐列", "S1",
         [("end_block_merge_rows(_ebm355, st.session_state.get('f3_end_block_merge_log'))",
           "end_block_merge_rows(_ebm355, [])")]),
        ("M14 顯示⛔ 出逐列表", "S1",
         [("                                st.dataframe(_pd.DataFrame(_ebm355_v['rows']),",
           "                                st.write(_pd.DataFrame(_ebm355_v['rows']),")]),
    ]


def wiring(repo):
    src = _read(repo, "app.py")
    red = []
    print("── 接線與合成案（AST·工作樹之 app.py）──")
    base = _checks(src)
    for name, ok, note in base:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    if red:
        print("── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（每一突變須使其所指之項轉紅）──")
    for mname, target, reps in _mut_list():
        m = src
        miss = []
        for a, b in reps:
            if m.count(a) != 1:
                miss.append(m.count(a))
                continue
            m = m.replace(a, b, 1)
        if miss:
            print(f"  🔴 {mname}：突變錨之命中 {miss}（期 各 1）")
            red.append(mname.split()[0])
            continue
        turned = [n.split()[0] for n, ok, _ in _checks(m) if not ok]
        ok = target in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}（須含 {target}）")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) != 3 or argv[1] != "wiring":
        print(__doc__)
        return 2
    return wiring(argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
