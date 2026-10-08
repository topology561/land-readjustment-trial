# -*- coding: utf-8 -*-
"""W-G.9-358 量測器（發單側窗五十五擬·檔 F17·⛔ 由受單側改一字）：段三後處理之 `K-9-48` 七項 3〜6 與 `K-9-51`
（`W-G.9-357` ＋ 補令一）之接線——以程式字樣為錨。

緣由：`W-G.9-357 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之
未處置不變、`R-5` 之「所施者恆已通過」、`R-6` 之候選與序、`R-7` 之 `raise` 已去、`R-10` 之二處同形、`R-11`／`R-12`
之落點）及其突變之判別力」，並含補令一之 `R-7′`／`X-3′`／`R-15`／`R-6′` 之落點。受詞之行為已由 F16
（`probe_WG9357_k948.py`）之 `selftest`／`run` 量之；本器量**程式字樣**（防日後之漂移）。

受詞（工作樹）：app.py 之 k6b_stage3_run（含其巢狀 _has357／_res357／_max357／_dist357／_k951／_split357／_t14_357
與步驟 10）、adj_intake、k6b_screen_callbacks 之巢狀 alloc_state；verify/selection_pipeline.py 之 k6b_stage3_pool_temp、
_k6b_callbacks 之巢狀 alloc_state。

子命令（一律 python verify/probes/probe_WG9358_k948_wiring.py <子命令> <repo>）：
  wiring <repo>
    W0  受詞在：五模組層函式在；七巢狀 def 各恰 1 且皆在 k6b_stage3_run 內（app.py 他處⛔ 同名）。
    W1  `R-2` 未處置不變：k6b_stage3_run 內 `結果='未處置'` 恰 1，在 `if not _qs:` 之本體，同本體有
        log_print「…未處置：二半片皆不鄰 B 內街廓」且以 continue 終；「未處置：「不影響原位次」不過」之字樣 0。
    W2  `R-5`／`R-5′` 所施者恆已通過：_max357 內 `state =` 恰 2，各在 `if <其值> is not None:` 之本體，其值 ∈ {_t, _best}；
        `_t = _try(s)`；`_best` 除初值 None 外唯於 `if _tm is not None:` 內得 `_tm`，`_tm = _try(_mid / 100)`（格值 n / 100）；
        巢狀 _try 唯一 return ＝ `_t if _noaff(…) else None`；末句 `return _lo / 100`。
    W3  `R-6`／`R-6′` ②③ 候選與序：_k951 內 alloc_state(state['temp'], state['build']) 恰 1、其 err ⇒ raise；
        篩 ＝ `_p == x or _p in merged_out or _b in F or _p not in state['by']` ⇒ continue；歸戶 `!= _gx` ⇒ continue；
        `_G = _cur.get('G')` 恰 1 且在 `if _pre:` 內（含「未回 G」之 raise ≥ 2 皆在其內）；序之鍵 ＝
        `(_dist357(x, _b), -float(_G[_p]), _p, …)`；`_cands.sort()` 無 key。
    W4  `R-6′` ③ 距離：_dist357 之末句 ＝ `float(<Decimal>(repr(<d>)).quantize(<Decimal>('0.01'), rounding=<ROUND_HALF_UP>))`
        （別名依其 `from decimal import …` 解之）；_dist357 內⛔ round；街廓之聯集取 `_blk_of[p] == blk` 之全部切片。
    W5  `R-7`／`R-7′`：app.py 內「七項 3〜5 未落地」之字樣 0；`_r4 = None` 恰 1、在 `if _noaff(state, _t2, …):` 之 else；
        `_t14_357(…)` 恰 1、在 `if _r4 is not None:` 之 else；`_t14_done` 唯 `= set()` 一賦值、唯 `.add(c)` 一呼叫，
        其為 _t14_357 本體之頂層句且先於其首個 if（① 之結果不論）；_t14_357 內 c 之整筆不過 ⇒
        `_k951(c, _a357(c), {W['blk']}, True)`，其半之片 ⇒ `_max357(x, w, _s)` 與 `if _has357(_rem):` 之 `_k951(…, False)`。
    W6  `X-3′`：k6b_stage3_run 本體（⛔ 巢狀）之 `R =` 恰 2：`R = _mem - merged_out - set(_recv_by_blk.values()) - L -
        _t14_done`、`R = R - _stay`。
    W7  `R-15`：_has357 ＝ `return round(float(r), 4) > 0`；`_EPS357` 之名 0；_res357／_split357／_k951／_t14_357 與
        末之鍵之環內⛔ 以浮點小量（0 < |v| < 1e-3）比較；諸判之字樣各在其處（見 _R15）；_split357 之
        `if _has357(_s - _g):` 本體含 `_F.add(…)` 與 `_rem += _s - _g`。
    W8  `R-10` 二處同形：二 alloc_state 之 `elif _r.get('驗_總判') == '保留':` 本體逐 AST 同，含
        `_kept.setdefault(_blk, set()).add(_pid)` 與 `_G[_pid] = float(_r.get('G(㎡)', 0) or 0)`；末句皆回
        {'kept': _kept, 'bad_pools': _bad, 'err': _err, 'G': _G}；`_G` 之初值 {}。
    W9  `R-11` 落點：k6b_stage3_pool_temp 之諸句（見 _R11）皆在；`_tp = dict(tp)`（淺拷貝）；二面積欄各乘 _rho。
    W10 `R-12` 落點：adj_intake 內 X-4 四字樣各恰 1（全檔亦恰 1）；`_s3_ids.add(_k)` 恰 2；① 之 `_row.update(類=
        ADJ_DISP_COMMON_UNIT, 原有面積=_a(t) * _rho, 段三併出面積=_a(t) * (1.0 - _rho))` 在 `if '段三併出' in t:` 內；
        `_s3` 之分在 `if _pool or (_cm and not _al):` 之 else，另成之單位之 '軌' ＝ ADJ_TRACK_PUBLIC、'共同負擔用地' ＝ _s3；
        `_tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']`。
    W11 `R-8` 鍵：k6b_stage3_run 本體恰一 `for _pid in sorted(set(marks) | set(_left)):`，在 `for _pid, _rs in marks.items():`
        之後；三支：有剩下且在 marks ⇒ 寫二鍵；有剩下 ⇒ 去 段三部分併出、段三餘量 ＝ round(_a357(_pid), 4)；否則去二鍵。
    W12 `R-3`／`R-4` 步驟 10：`for p in _plan:` 之本體中 `if not _qs:` → `if not _batch_ok and not _whole:`（本體 ＝
        _split357(x, _qs, _lvl_name[_cl2], _extra)；continue）→ `if _batch_ok:` 依序；`if _ok:` 之 else ＝
        `_row(**_base, 結果='未成', 檢核='不過')`；`_k951(x, _a357(x), {…}, True)`。
    本部全綠時另施 29 種原始碼突變，每一突變須使其所指之項轉紅（器紅 ⇒ rc 1）。
  🔧 `W-G.9-373`（`K-9-66`／`K-9-68`·⛔ 上列一字不刪）：`K-9-48` 七項 3／4／7 之逐片（`_max357`·`_k951`·`_split357`）由
    `K-9-66`（逐受併之街廓之順序及比例）與 `K-9-68`（`K-9-51` 之逐輪）代之，其三巢狀 def 去之 ⇒ W0 之巢狀唯
    `_has357`／`_res357`／`_dist357`／`_t14_357`；**W2、W3、W12 退**（其受詞已去·新碼之接線與突變之判別力由次單以 CC 之碼
    之字樣為錨補寫）；W5 唯量 `R-7`／`R-7′` 之既有落點（舊 raise 去、`_r4 = None`、`_t14_357` 之一呼、`_t14_done`）；W7 唯
    量 `_has357`／`_res357`／鍵之環；W8 之回傳之鍵增 `'members'`（`K-9-67`·第五鍵）；W11 之三支取鍵之環中測試為
    `_has357(_rm) and _pid in marks` 之 if（建地之支另立於其前·⛔ 計）。突變去 M2〜M9、M14、M16、M19、M22、M28、M29
    （其錨已去·M2 之錨之縮排隨步驟 10 之重排而異），餘 15 種。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import ast, contextlib, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FA, FS = "app.py", "verify/selection_pipeline.py"
FN_S3, FN_AI, FN_CB = "k6b_stage3_run", "adj_intake", "k6b_screen_callbacks"
FN_PT, FN_HCB = "k6b_stage3_pool_temp", "_k6b_callbacks"
NEST = ("_has357", "_res357", "_max357", "_dist357", "_k951", "_split357", "_t14_357")
# 🔧 `W-G.9-373`（`K-9-66`）：`_max357`／`_k951`／`_split357` 去之
NEST = tuple(x for x in NEST if x not in ("_max357", "_k951", "_split357"))
X4 = ("float(_r['應分配面積'])", "if _pool or (_cm and not _al):", "if '段三併出' in t:", "if len(_cands) != 1:")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


# ── AST 之小工具 ──
def _u(n):
    try:
        return ast.unparse(n)
    except Exception:  # noqa: BLE001
        return "<?>"


def _n(src):
    """期之字樣之正規形（以 ast.unparse 之形比較·例 `a and not b` ⇒ `a and (not b)`）。"""
    return ast.unparse(ast.parse(src, mode="eval").body)


def _top(tree):
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


def _walk_own(fn):
    """fn 之節點，⛔ 入巢狀之 def／lambda。"""
    todo = [s for s in fn.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))]
    while todo:
        n = todo.pop()
        yield n
        for c in ast.iter_child_nodes(n):
            if not isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                todo.append(c)


def _defs(node, name):
    return [n for n in ast.walk(node) if isinstance(n, ast.FunctionDef) and n.name == name]


def _is_call(n, name):
    return isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name


def _parents(root):
    return {c: p for p in ast.walk(root) for c in ast.iter_child_nodes(p)}


def _in_branch(node, par, test_src, branch):
    """node 之某祖為 If（其 test 之 unparse ＝ test_src），且 node 在其 branch（'body'／'orelse'）之下。"""
    cur = node
    while cur in par:
        p = par[cur]
        if isinstance(p, ast.If) and _u(p.test) == _n(test_src):
            if any(cur is s for s in getattr(p, branch)):
                return True
        cur = p
    return False


def _stmts(fn, own=True):
    it = _walk_own(fn) if own else ast.walk(fn)
    return [n for n in it if isinstance(n, ast.stmt)]


def _ifs(fn, own=True):
    return [n for n in (_walk_own(fn) if own else ast.walk(fn)) if isinstance(n, ast.If)]


def _strs(node):
    return [n.value for n in ast.walk(node) if isinstance(n, ast.Constant) and isinstance(n.value, str)]


class _Ctx:
    def __init__(self, sa, ss):
        self.ta, self.ts = ast.parse(sa), ast.parse(ss)
        self.top_a, self.top_s = _top(self.ta), _top(self.ts)
        self.s3 = self.top_a.get(FN_S3)
        self.n = {}
        if self.s3 is not None:
            for nm in NEST:
                d = _defs(self.s3, nm)
                if len(d) == 1:
                    self.n[nm] = d[0]


# ── 接線 ──
def _w0(c):
    miss = [f for f in (FN_S3, FN_AI, FN_CB) if f not in c.top_a] + [f for f in (FN_PT, FN_HCB) if f not in c.top_s]
    bad = []
    for nm in NEST:
        tot = len(_defs(c.ta, nm))
        ins = len(_defs(c.s3, nm)) if c.s3 is not None else 0
        if not (tot == 1 and ins == 1):
            bad.append((nm, tot, ins))
    return (not miss and not bad), f"缺 {miss}；巢狀（名, 全檔, 段三內）之不符 {bad}"


def _w1(c):
    s3 = c.s3
    kws = [n for n in ast.walk(s3) if isinstance(n, ast.keyword) and n.arg == "結果"
           and isinstance(n.value, ast.Constant) and n.value.value == "未處置"]
    ifs = [n for n in ast.walk(s3) if isinstance(n, ast.If) and _u(n.test) == "not _qs"]
    old = [s for s in _strs(s3) if "未處置：「不影響原位次」不過" in s]
    if len(kws) != 1 or len(ifs) != 1:
        return False, f"結果='未處置' {len(kws)}（期 1）；`if not _qs:` {len(ifs)}（期 1）"
    body = ifs[0].body
    in_body = any(kws[0] in list(ast.walk(s)) for s in body)
    lp = any(_is_call(n, "log_print") and any("未處置：二半片皆不鄰 B 內街廓" in v for v in _strs(n))
             for s in body for n in ast.walk(s))
    cont = isinstance(body[-1], ast.Continue)
    ok = in_body and lp and cont and not old
    return ok, f"在 `if not _qs:` {in_body}；log_print {lp}；continue {cont}；舊字樣 {len(old)}（期 0）"


def _w2(c):
    # 🔧 `W-G.9-373`：退（`_max357` 去之·`K-9-66`）
    return True, "退（W-G.9-373·K-9-66）"


def _w3(c):
    # 🔧 `W-G.9-373`：退（`_k951` 去之·`K-9-68`）
    return True, "退（W-G.9-373·K-9-68）"


def _w4(c):
    d = c.n["_dist357"]
    al = {}
    for n in list(ast.walk(d)) + list(c.ta.body):
        if isinstance(n, ast.ImportFrom) and n.module == "decimal":
            for a in n.names:
                al[a.asname or a.name] = a.name
    dec = {k for k, v in al.items() if v == "Decimal"}
    hu = {k for k, v in al.items() if v == "ROUND_HALF_UP"}
    last = d.body[-1]
    ok_ret = False
    if isinstance(last, ast.Return) and _is_call(last.value, "float") and len(last.value.args) == 1:
        q = last.value.args[0]
        if isinstance(q, ast.Call) and isinstance(q.func, ast.Attribute) and q.func.attr == "quantize":
            inner = q.func.value
            ok_ret = (isinstance(inner, ast.Call) and isinstance(inner.func, ast.Name) and inner.func.id in dec
                      and len(inner.args) == 1 and _is_call(inner.args[0], "repr")
                      and len(q.args) == 1 and isinstance(q.args[0], ast.Call) and isinstance(q.args[0].func, ast.Name)
                      and q.args[0].func.id in dec and _u(q.args[0].args[0]) == "'0.01'"
                      and [(kw.arg, _u(kw.value)) for kw in q.keywords] in ([("rounding", h)] for h in hu))
    rnd = [n for n in ast.walk(d) if _is_call(n, "round")]
    un = any(isinstance(n, ast.Assign) and _u(n.targets[0]) == "_gs" and "_blk_of[p] == blk" in _u(n.value)
             and "_geo" in _u(n.value) for n in ast.walk(d))
    ok = ok_ret and not rnd and un
    return ok, f"ROUND_HALF_UP 之式 {ok_ret}；round 之呼 {len(rnd)}（期 0）；街廓之全部切片 {un}"


def _w5(c):
    s3, t = c.s3, c.n["_t14_357"]
    old = [s for s in _strs(c.ta) if "七項 3〜5 未落地" in s]
    par = _parents(s3)
    r4 = [n for n in ast.walk(s3) if isinstance(n, ast.Assign) and _u(n) == "_r4 = None"]
    r4_ok = len(r4) == 1 and _in_branch(r4[0], par, "_noaff(state, _t2, {W['blk'], _lb}, {Lo['c']})", "orelse")
    cl = [n for n in ast.walk(s3) if _is_call(n, "_t14_357")]
    cl_ok = len(cl) == 1 and _in_branch(cl[0], par, "_r4 is not None", "orelse")
    asg = [n for n in ast.walk(s3) if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign))
           and "_t14_done" in [_u(x) for x in (n.targets if isinstance(n, ast.Assign) else [n.target])]]
    asg_ok = len(asg) == 1 and _u(asg[0]) == "_t14_done = set()" and any(asg[0] is s for s in s3.body)
    mut = [n for n in ast.walk(s3) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
           and _u(n.func.value) == "_t14_done"]
    add = [s for s in t.body if isinstance(s, ast.Expr) and _u(s) == "_t14_done.add(c)"]
    first_if = next((i for i, s in enumerate(t.body) if isinstance(s, ast.If)), len(t.body))
    add_ok = len(mut) == 1 and len(add) == 1 and t.body.index(add[0]) < first_if
    # 🔧 `W-G.9-373`：c 與其半之去處改依 `K-9-66`／`K-9-68`（`_k951`／`_max357` 去之）⇒ 該三判退
    ok = not old and r4_ok and cl_ok and asg_ok and add_ok
    return ok, (f"舊 raise 之字樣 {len(old)}（期 0）；_r4＝None 於合併不過 {r4_ok}；_t14_357 一呼於其 else {cl_ok}；"
                f"_t14_done 唯 set() {asg_ok}；唯 .add(c) 於頂層先於 if {add_ok}（方法呼 {len(mut)}）")


def _w6(c):
    rs = [_u(n) for n in _walk_own(c.s3) if isinstance(n, ast.Assign) and _u(n.targets[0]) == "R"]
    want = ["R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done", "R = R - _stay"]
    return sorted(rs) == sorted(want), f"R 之賦值 {rs}"


_R15 = {"_res357": {"not _has357(s - g)"}}     # 🔧 `W-G.9-373`：`_split357`／`_k951` 去之；`_t14_357` 之判移入 K-9-66


def _keyloop(s3):
    return [n for n in _walk_own(s3) if isinstance(n, ast.For) and _u(n.iter) == "sorted(set(marks) | set(_left))"]


def _tiny(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Compare):
            for x in [n.left] + list(n.comparators):
                v = x.operand.value if (isinstance(x, ast.UnaryOp) and isinstance(x.operand, ast.Constant)) else \
                    (x.value if isinstance(x, ast.Constant) else None)
                if isinstance(v, float) and 0 < abs(v) < 1e-3:
                    out.append(_u(n))
    return out


def _w7(c):
    h = c.n["_has357"]
    h_ok = [a.arg for a in h.args.args] == ["r"] and len(h.body) >= 1 and _u(h.body[-1]) == "return round(float(r), 4) > 0" \
        and all(isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) for s in h.body[:-1])
    eps = [n for n in ast.walk(c.ta) if isinstance(n, ast.Name) and n.id == "_EPS357"]
    kl = _keyloop(c.s3)
    places = [(nm, c.n[nm]) for nm in _R15] + [("鍵之環", kl[0])] if len(kl) == 1 else [(nm, c.n[nm]) for nm in _R15]
    tiny = {nm: _tiny(fn) for nm, fn in places if _tiny(fn)}
    need = dict(_R15)
    need["鍵之環"] = {"_has357(_rm) and _pid in marks", "_has357(_rm)"}
    miss = {}
    for nm, fn in places:
        tests = {_u(n.test) for n in ast.walk(fn) if isinstance(n, ast.If)}
        lack = {_n(x) for x in need[nm]} - tests
        if lack:
            miss[nm] = sorted(lack)
    ok = h_ok and not eps and len(kl) == 1 and not tiny and not miss      # 🔧 `W-G.9-373`：`_split357` 之判退
    return ok, f"_has357 之式 {h_ok}；_EPS357 {len(eps)}（期 0）；浮點小量之比較 {tiny}；缺判 {miss}"


def _alloc_parts(fn):
    a = _defs(fn, "alloc_state")
    if len(a) != 1:
        return None
    a = a[0]
    el = [n for n in ast.walk(a) if isinstance(n, ast.If) and _u(n.test) == "_r.get('驗_總判') == '保留'"]
    init = [n for n in ast.walk(a) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple)
            and "_G" in [_u(x) for x in n.targets[0].elts]]
    g0 = None
    if len(init) == 1 and isinstance(init[0].value, ast.Tuple):
        m = dict(zip([_u(x) for x in init[0].targets[0].elts], [_u(x) for x in init[0].value.elts]))
        g0 = m.get("_G")
    last = a.body[-1]
    ret = None
    if isinstance(last, ast.Return) and isinstance(last.value, ast.Dict):
        ret = [(_u(k), _u(v)) for k, v in zip(last.value.keys, last.value.values)]
    return ([ast.dump(s) for s in el[0].body] if len(el) == 1 else None), \
        ([_u(s) for s in el[0].body] if len(el) == 1 else None), g0, ret


def _w8(c):
    pa, ps = _alloc_parts(c.top_a[FN_CB]), _alloc_parts(c.top_s[FN_HCB])
    if pa is None or ps is None:
        return False, f"alloc_state 之巢狀 def 不恰 1（app {pa is not None}／harness {ps is not None}）"
    want_ret = [("'kept'", "_kept"), ("'bad_pools'", "_bad"), ("'err'", "_err"), ("'G'", "_G")]
    need = {"_kept.setdefault(_blk, set()).add(_pid)", "_G[_pid] = float(_r.get('G(㎡)', 0) or 0)"}
    same = pa[0] is not None and pa[0] == ps[0]
    has = pa[1] is not None and need <= set(pa[1])
    # 🔧 `W-G.9-373`（`K-9-67`）：回傳之鍵 ＝ 前四鍵 ＋ 'members'（其值之式二處各異·⛔ 比）
    ra = pa[3] is not None and pa[3][:4] == want_ret and [k for k, _ in pa[3][4:]] == ["'members'"]
    rs = ps[3] is not None and ps[3][:4] == want_ret and [k for k, _ in ps[3][4:]] == ["'members'"]
    ok = same and has and pa[2] == "{}" and ps[2] == "{}" and ra and rs
    return ok, (f"保留之支逐 AST 同 {same}；含 kept 與 G {has}；_G 之初值 {pa[2]}／{ps[2]}；"
                f"回傳之鍵 app {ra}／harness {rs}")


_R11 = ["_out = []", "_out.append(tp)", "_rem = float(tp.get('段三餘量', 0) or 0)",
        "_a = float(tp.get('分攤登記面積_m2', 0) or 0) + float(tp.get('面積_m2', 0) or 0)", "_rho = _rem / _a",
        "_tp = dict(tp)", "_tp['分攤登記面積_m2'] = float(tp.get('分攤登記面積_m2', 0) or 0) * _rho",
        "_tp['面積_m2'] = float(tp.get('面積_m2', 0) or 0) * _rho", "_out.append(_tp)", "return _out"]


def _w9(c):
    f = c.top_s[FN_PT]
    st = [_u(s) for s in ast.walk(f) if isinstance(s, ast.stmt) and not isinstance(s, (ast.For, ast.If))]
    miss = [s for s in _R11 if s not in st]
    tests = [(_u(n.test), [_u(s) for s in n.body]) for n in ast.walk(f) if isinstance(n, ast.If)]
    t1 = ("'段三併出' not in tp", ["_out.append(tp)", "continue"]) in tests
    t2 = ("not _rem > 0", ["continue"]) in tests
    return (not miss and t1 and t2), f"缺句 {miss}；無段三併出 ⇒ 原物件 {t1}；無剩下 ⇒ 去 {t2}"


def _w10(c, sa):
    ai = c.top_a[FN_AI]
    seg = ast.get_source_segment(sa, ai) or ""
    x4 = [(s, sa.count(s), seg.count(s)) for s in X4]
    x4_ok = all(a == 1 and b == 1 for _, a, b in x4)
    par = _parents(ai)
    adds = [n for n in ast.walk(ai) if isinstance(n, ast.Call) and _u(n) == "_s3_ids.add(_k)"]
    ini = [n for n in ast.walk(ai) if isinstance(n, ast.Assign) and _u(n) == "_s3_ids = set()"]
    up = [n for n in ast.walk(ai) if isinstance(n, ast.Expr) and _u(n) ==
          "_row.update(類=ADJ_DISP_COMMON_UNIT, 原有面積=_a(t) * _rho, 段三併出面積=_a(t) * (1.0 - _rho))"]
    up_ok = len(up) == 1 and _in_branch(up[0], par, "'段三併出' in t", "body")
    rho = any(isinstance(n, ast.Assign) and _u(n) == "_rho = _rem3 / _den" for n in ast.walk(ai))
    s3 = [n for n in ast.walk(ai) if isinstance(n, ast.Assign) and _u(n) ==
          "_s3 = [_r for _r in _cm if _r['暫編地號'] in _s3_ids]"]
    s3_ok = len(s3) == 1 and _in_branch(s3[0], par, "_pool or (_cm and not _al)", "orelse")
    un = []
    for n in ast.walk(ai):
        if isinstance(n, ast.Call) and _u(n.func) == "_units.append" and n.args and isinstance(n.args[0], ast.Dict):
            d = {_u(k): _u(v) for k, v in zip(n.args[0].keys, n.args[0].values)}
            if d.get("'共同負擔用地'") == "_s3":
                un.append(d)
    un_ok = len(un) == 1 and un[0].get("'軌'") == "ADJ_TRACK_PUBLIC" and un[0].get("'原街廓'") == "None"
    tot = any(isinstance(n, ast.AugAssign) and _u(n) == "_tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']"
              for n in ast.walk(ai))
    ok = x4_ok and len(adds) == 2 and len(ini) == 1 and up_ok and rho and s3_ok and un_ok and tot
    return ok, (f"X-4（字樣, 全檔, adj_intake）{x4 if not x4_ok else '皆 1'}；_s3_ids 之加 {len(adds)}（期 2）；"
                f"① 之落點 {up_ok}；ρ {rho}；不成單位者之分 {s3_ok}；另成單位（公設軌） {un_ok}；總計之面積 {tot}")


def _w11(c):
    s3 = c.s3
    kl = _keyloop(s3)
    if len(kl) != 1:
        return False, f"鍵之環 {len(kl)}（期 1）"
    kl = kl[0]
    mk = [n for n in s3.body if isinstance(n, ast.For) and _u(n.iter) == "marks.items()"]
    order_ok = len(mk) == 1 and kl in s3.body and s3.body.index(mk[0]) < s3.body.index(kl)
    # 🔧 `W-G.9-373`：取測試為 `_has357(_rm) and _pid in marks` 之 if（建地之支另立於其前·⛔ 計）
    ifs = [s for s in kl.body if isinstance(s, ast.If) and _u(s.test) == "_has357(_rm) and _pid in marks"]
    ok3 = False
    if len(ifs) == 1:
        a = [_u(s) for s in ifs[0].body]
        e = ifs[0].orelse
        if len(e) == 1 and isinstance(e[0], ast.If) and _u(e[0].test) == "_has357(_rm)":
            b = [_u(s) for s in e[0].body]
            z = [_u(s) for s in e[0].orelse]
            ok3 = (any(s.startswith("_tp['段三部分併出'] = ") for s in a) and "_tp['段三餘量'] = round(_rm, 4)" in a
                   and b == ["_tp.pop('段三部分併出', None)", "_tp['段三餘量'] = round(_a357(_pid), 4)"]
                   and z == ["_tp.pop('段三部分併出', None)", "_tp.pop('段三餘量', None)"])
    return order_ok and ok3, f"序於 段三併出 之後 {order_ok}；三支 {ok3}"


def _w12(c):
    # 🔧 `W-G.9-373`：退（步驟 10 之逐片之 `_split357`／`_k951` 去之·`K-9-66`）
    return True, "退（W-G.9-373·K-9-66）"


def _checks(sa, ss):
    try:
        c = _Ctx(sa, ss)
    except SyntaxError as e:
        return [("W0 可剖析", False, f"{e}")]
    res = []
    items = (("W0 受詞在", lambda: _w0(c)), ("W1 R-2 未處置不變", lambda: _w1(c)),
             ("W2 R-5 所施者恆已通過（退）", lambda: _w2(c)), ("W3 R-6 候選與序（退）", lambda: _w3(c)),
             ("W4 R-6′ 距離之取捨", lambda: _w4(c)), ("W5 R-7／R-7′ 題一 4", lambda: _w5(c)),
             ("W6 X-3′ 步驟 10 之 R", lambda: _w6(c)), ("W7 R-15 剩下之判準", lambda: _w7(c)),
             ("W8 R-10 二處同形", lambda: _w8(c)), ("W9 R-11 公設地調配之 temp", lambda: _w9(c)),
             ("W10 R-12 調配之輸入", lambda: _w10(c, sa)), ("W11 R-8 片之鍵", lambda: _w11(c)),
             ("W12 R-3／R-4 步驟 10 之逐片（退）", lambda: _w12(c)))
    for name, fn in items:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ok, note = fn()
        except Exception as e:  # noqa: BLE001
            ok, note = False, f"器拋 {type(e).__name__}: {e}"
        res.append((name, ok, note))
    return res


# ── 突變（每一須使其所指之項轉紅）── 各為 (名, 所指之項, [(檔, 錨, 代)])
def _mut_list():
    # 🔧 `W-G.9-373`：去 M2〜M9、M14、M16、M19、M22、M28、M29（其錨已去·`K-9-66`／`K-9-68`）
    return [
        ("M1 無受併宗之片改記未成", "W1",
         [(FA, "_row(**{**_base, '受併宗': '—'}, 結果='未處置', 檢核='—')", "_row(**{**_base, '受併宗': '—'}, 結果='未成', 檢核='—')")]),
        ("M10 距離以 round", "W4",
         [(FA, "return float(_Dec357(repr(_d)).quantize(_Dec357('0.01'), rounding=_HU357))", "return round(_d, 2)")]),
        ("M11 距離以 Decimal(float)", "W4", [(FA, "_Dec357(repr(_d))", "_Dec357(_d)")]),
        ("M12 距離以 ROUND_HALF_EVEN", "W4",
         [(FA, "from decimal import Decimal as _Dec357, ROUND_HALF_UP as _HU357",
           "from decimal import Decimal as _Dec357, ROUND_HALF_EVEN as _HU357")]),
        ("M13 R-7 之候選⛔ 入已處置之集", "W5", [(FA, "        _t14_done.add(c)    #", "        pass    #")]),
        ("M15 題一 4 之合併不過復停機", "W5",
         [(FA, "                    _r4 = None\n",
           "                    raise RuntimeError(\"🔴 [K-6-B 段三 K-9-50 題一] `K-9-48` 七項 3〜5 未落地（停機款 9）\")\n")]),
        ("M17 步驟 10 之 R ⛔ 扣已處置之候選", "W6",
         [(FA, "R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done", "R = _mem - merged_out - set(_recv_by_blk.values()) - L")]),
        ("M18 有剩下以 1e-6 判", "W7", [(FA, "return round(float(r), 4) > 0", "return float(r) > 1e-6")]),
        ("M20 鍵之環以 1e-6 判", "W7",
         [(FA, "        if _has357(_rm) and _pid in marks:\n", "        if _rm > 1e-6 and _pid in marks:\n")]),
        ("M21 畫面之 G 取他欄", "W8", [(FA, "_G[_pid] = float(_r.get('G(㎡)', 0) or 0)", "_G[_pid] = float(_r.get('G', 0) or 0)")]),
        ("M23 公設地調配之 temp 改原物件", "W9", [(FS, "_tp = dict(tp)", "_tp = tp")]),
        ("M24 面積_m2 ⛔ 乘 ρ", "W9",
         [(FS, "_tp[\"面積_m2\"] = float(tp.get(\"面積_m2\", 0) or 0) * _rho", "_tp[\"面積_m2\"] = float(tp.get(\"面積_m2\", 0) or 0)")]),
        ("M25 一分未併者⛔ 入合併單位", "W10",
         [(FA, "            _row['類'] = ADJ_DISP_COMMON_UNIT\n            _s3_ids.add(_k)\n", "            _row['類'] = ADJ_DISP_COMMON_UNIT\n")]),
        ("M26 已併出之量⛔ 計入原位次配地", "W10",
         [(FA, "            _tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']\n", "            pass\n")]),
        ("M27 剩下全收者⛔ 去 段三餘量", "W11",
         [(FA, "            _tp.pop('段三部分併出', None)\n            _tp.pop('段三餘量', None)\n",
           "            _tp.pop('段三部分併出', None)\n")]),
    ]


def wiring(repo):
    src = {FA: _read(repo, FA), FS: _read(repo, FS)}
    red = []
    print("── 接線（AST·工作樹之 app.py ＋ verify/selection_pipeline.py）──")
    for name, ok, note in _checks(src[FA], src[FS]):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    if red:
        print("── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（每一突變須使其所指之項轉紅）──")
    for mname, target, reps in _mut_list():
        m = dict(src)
        miss = []
        for f, a, b in reps:
            if m[f].count(a) != 1:
                miss.append(m[f].count(a))
                continue
            m[f] = m[f].replace(a, b, 1)
        if miss:
            print(f"  🔴 {mname}：突變錨之命中 {miss}（期 各 1）")
            red.append(mname.split()[0])
            continue
        turned = [n.split()[0] for n, ok, _ in _checks(m[FA], m[FS]) if not ok]
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
