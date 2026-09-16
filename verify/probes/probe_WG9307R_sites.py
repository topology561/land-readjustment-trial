"""`W-G.9-307` `§五`：`_corner_buffer_S` **七處之在域現查**（**AST 為框**·靜態·⛔ 跑 harness）。

🔒 授權（單 `§五` 首段逐字）：新增本量測器 ＋ 其落檔 `verify/out/WG9307R_sites.log`；
   **AST 為框**·讀 blob 取 bytes·**`rev` 釘死**。
🛑 本器**⛔ 判改法、⛔ 判可施與否、⛔ 擬任何 diff**——其結果供發單側釘 `W-G.9-308` 之逐處改法。
🛑 **泛用化**：⛔ 硬寫街廓名、側標籤、個案常數；受詞名（`_corner_buffer_S` 等）係**受詞本身**，非個案常數。

用法：`python verify/probes/probe_WG9307R_sites.py <rev>`（`rev` 須釘死·⛔ 用工作區）。
"""
import ast
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")

TARGET = "_corner_buffer_S"
SOLVE = "_solve_G_one"
KW_MID = "side_mid"
KW_CORNER = "is_corner"
TRACE_CAP = 12                 # 逆溯深度上限（超出 ⇒ loud）
BAR = "=" * 116
LOUD = []


def sh(args):
    return subprocess.run(args, capture_output=True)


def blob(rev, path):
    r = sh(["git", "cat-file", "blob", "%s:%s" % (rev, path)])
    assert r.returncode == 0, "🔴 讀 blob 失敗：%s（rc=%d）" % (path, r.returncode)
    return r.stdout


def prod34(rev):
    """母體 ＝ 生產碼 `34` 檔（**正面列舉**·外部錨 ＝ `§一` 閘 `7`）。"""
    out = sh(["git", "ls-tree", rev, "--name-only", "-z", "verify/"]).stdout
    py = sorted(n.decode("utf-8") for n in out.split(b"\x00")
                if n and n.decode("utf-8").endswith(".py"))
    return ["app.py"] + py


# ─────────────────────────────────────────────────────────────────────
#  AST 基建：parent 連結／語句路徑（⛔ 以行號判先後）
# ─────────────────────────────────────────────────────────────────────
def annotate(tree):
    for p in ast.walk(tree):
        for c in ast.iter_child_nodes(p):
            c._parent = p


def enclosing_func(node):
    p = getattr(node, "_parent", None)
    while p is not None:
        if isinstance(p, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return p
        p = getattr(p, "_parent", None)
    return None


def qualname(node):
    out, p = [], node
    while p is not None:
        if isinstance(p, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            out.append(p.name)
        p = getattr(p, "_parent", None)
    return "::".join(reversed(out)) if out else "<module>"


def stmt_paths(func):
    """回 {id(stmt): path}；`path` ＝ 逐層 body 索引之 tuple（**語句路徑**·⛔ 行號）。"""
    out = {}

    def rec(body, base):
        for i, st in enumerate(body):
            p = base + (i,)
            out[id(st)] = p
            for fld in ("body", "orelse", "finalbody"):
                sub = getattr(st, fld, None)
                if isinstance(sub, list) and sub and isinstance(sub[0], ast.stmt):
                    rec(sub, p + (fld,))
            for h in getattr(st, "handlers", []) or []:
                out[id(h)] = p + ("handler",)
                rec(h.body, p + ("handler",))
    rec(func.body, ())
    return out


def owning_stmt(node, paths):
    p = node
    while p is not None:
        if id(p) in paths:
            return p
        p = getattr(p, "_parent", None)
    return None


def cmp_path(a, b):
    """語句路徑之全序比較（字串與整數混列 ⇒ 以型別序穩定化）。"""
    ka = tuple((0, x, "") if isinstance(x, int) else (1, 0, x) for x in a)
    kb = tuple((0, x, "") if isinstance(x, int) else (1, 0, x) for x in b)
    return (ka > kb) - (ka < kb)


_LINE_CACHE = {}


def _lines_of(src):
    """🔒 `ast.get_source_segment` 每呼叫一次即 `splitlines` 全檔（`app.py` ＝ `1.4` MB）
       ⇒ 於數千次呼叫下不可終止。本快取使其**每源一次**；**取得之字串逐位不變**。

    🩸 **首版以 `id(src)` 為鍵** ⇒ CPython 於原字串被回收後**重用同一 `id`**
       ⇒ 取到**他檔之列**（`seg` 自我驗證閘由 `837`／`0` 轉紅而當場捕獲）。
       ⇒ 本版**併存其字串本身**並以 `is` 覆核（兼使該字串不被回收）——
       即本倉之 `id(·)` ⛔ 作錨。
    """
    k = id(src)
    v = _LINE_CACHE.get(k)
    if v is not None and v[0] is src:
        return v[1]
    lines = src.splitlines(True)
    _LINE_CACHE[k] = (src, lines)
    return lines


def seg(src, node):
    """回該節點之原始碼逐字（等價於 `ast.get_source_segment`·⛔ 改其取得之字串）。"""
    try:
        lo = getattr(node, "lineno", None)
        hi = getattr(node, "end_lineno", None)
        co = getattr(node, "col_offset", None)
        eo = getattr(node, "end_col_offset", None)
        if lo is None or hi is None or co is None or eo is None:
            return ast.dump(node)[:120]
        L = _lines_of(src)
        if hi - 1 >= len(L):
            return ast.dump(node)[:120]
        # 🔴 `col_offset`／`end_col_offset` 係 **UTF-8 位元組**偏移（⛔ 字元）
        #    ⇒ 須**先 encode 再切**（同 `ast.get_source_segment` 之作法）。
        if lo == hi:
            return L[lo - 1].encode("utf-8")[co:eo].decode("utf-8")
        first = L[lo - 1].encode("utf-8")[co:].decode("utf-8")
        last = L[hi - 1].encode("utf-8")[:eo].decode("utf-8")
        return "".join([first] + L[lo:hi - 1] + [last])
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("seg 例外：%r" % (e,))
        return ast.dump(node)[:120]


# ─────────────────────────────────────────────────────────────────────
#  款 `1`：呼叫端集 `S`（框之語法形**窮舉**）
# ─────────────────────────────────────────────────────────────────────
def func_form(fn, name):
    """回 ('①'/'②'/'③', True) 若該 `func` 節點直取 `name`。"""
    if isinstance(fn, ast.Name) and fn.id == name:
        return "①Name"
    if isinstance(fn, ast.Subscript):
        sl = fn.slice
        if isinstance(sl, ast.Constant) and isinstance(sl.value, str) and sl.value == name:
            return "②Subscript"
    if isinstance(fn, ast.Attribute) and fn.attr == name:
        return "③Attribute"
    return None


def alias_names(tree, name):
    """④ 別名一層：`X = <①②③ 之 func 形>` ⇒ 收 `X`；鏈更深者 loud。"""
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name):
            if func_form(n.value, name):
                out[n.targets[0].id] = n
    return out


def collect_sites(rev, files):
    sites, residue = [], []
    trees = {}
    for f in files:
        src_b = blob(rev, f)
        src = src_b.decode("utf-8")
        if TARGET not in src:
            continue
        tree = ast.parse(src)
        annotate(tree)
        trees[f] = (src, tree)
        alias = alias_names(tree, TARGET)
        call_funcs = set()
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            form = func_form(n.func, TARGET)
            if form is None and isinstance(n.func, ast.Name) and n.func.id in alias:
                form = "④Alias(%s)" % n.func.id
            if form:
                call_funcs.add(id(n.func))
                sites.append({"file": f, "call": n, "form": form,
                              "src": src, "tree": tree})
        # 殘餘之全量：凡含該字樣之節點而⛔ 屬上列 func 者
        for n in ast.walk(tree):
            hit = False
            for fld, val in ast.iter_fields(n):
                if isinstance(val, str) and val == TARGET:
                    hit = True
                elif isinstance(val, list):
                    for x in val:
                        if isinstance(x, str) and x == TARGET:
                            hit = True
            if hit and id(n) not in call_funcs:
                residue.append({"file": f, "type": type(n).__name__,
                                "line": getattr(n, "lineno", None),
                                "qual": qualname(n)})
    return sites, residue, trees


# ─────────────────────────────────────────────────────────────────────
#  逆溯：名之綁定鏈 ⇒ 至「以字面鍵取自登記表之式」為止
# ─────────────────────────────────────────────────────────────────────
def literal_keys(node):
    """收該式中一切**字面字串鍵**（`Subscript` 之 `Constant` 與 `.get('lit')` 之首實參）。"""
    keys = []
    for n in ast.walk(node):
        if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) \
                and isinstance(n.slice.value, str):
            keys.append(n.slice.value)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr == "get" and n.args:
            a0 = n.args[0]
            if isinstance(a0, ast.Constant) and isinstance(a0.value, str):
                keys.append(a0.value)
    return keys


def registry_reads(func, expr):
    """回該式中**以字面鍵取自登記表**之讀取（鍵·其基名）。

    🔒 **「登記表」之構造上界定** ＝ 其**基名於本函式內⛔ 有綁定**者（形參／外層／全域，
       如 `ss`）——即該鏈**出本函式之界**之處。此即單所令之止點
       「**至以字面鍵取自登記表之式為止**」，⛔ 任一字面鍵（首版止於 `_sl_left.get('mid')`
       之 `'mid'` 而⛔ 抵 `ss.get('f3_cad_side_lines_by_side', …)` ⇒ 誤紅）。
    """
    out = []

    def base_name(n):
        while isinstance(n, (ast.Subscript, ast.Attribute, ast.Call)):
            n = n.value if isinstance(n, (ast.Subscript, ast.Attribute)) else n.func
        return n.id if isinstance(n, ast.Name) else None

    for n in ast.walk(expr):
        key = None
        if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) \
                and isinstance(n.slice.value, str):
            key = n.slice.value
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr == "get" and n.args \
                and isinstance(n.args[0], ast.Constant) \
                and isinstance(n.args[0].value, str):
            key = n.args[0].value
        if key is None:
            continue
        b = base_name(n)
        if b is not None and _is_external(func, b):
            out.append((key, b))
    return out


def _is_external(func, name):
    """該名是否**自本函式之外**取得其值 ＝ 無綁定，**或其綁定全為形參**。

    🩸 首版只認「無綁定」⇒ `ss`（`_run_step_g_impl` 之**形參**）⛔ 被認作登記表基名
       ⇒ 止點**永不觸發**、鏈續溯至深度上限（`7676` 次截斷）。
       形參之值係**呼叫端**所供 ⇒ 其於本函式內即「界外」，正是單所稱之「登記表」。
    """
    bs = bindings_of(func, name)
    if not bs:
        return True
    return all(k == "形參" for k, _, _ in bs)


_BIND_CACHE = {}


def bindings_of(func, name):
    """該函式（含巢狀）內 `name` 之**每一**綁定；回 [(kind, stmt, rhs_node)]。

    🔒 **索引一次建成**（`_BIND_CACHE`）——首版逐名重走整個函式，於 `app.py :: main`
       （數萬節點）× 數百名下**不可終止**；本版之結果**與首版逐位相同**，只改其取得方式。
    """
    key = id(func)
    idx = _BIND_CACHE.get(key)
    if idx is None:
        idx = _build_bind_index(func)
        _BIND_CACHE[key] = idx
    return idx.get(name, [])


def _build_bind_index(func):
    idx = {}

    def add(nm, kind, st, rhs):
        idx.setdefault(nm, []).append((kind, st, rhs))

    for n in ast.walk(func):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                for nn in ast.walk(t):
                    if isinstance(nn, ast.Name):
                        add(nn.id, "Assign", n, n.value)
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            add(n.target.id, "AnnAssign", n, n.value)
        elif isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name):
            add(n.target.id, "AugAssign", n, n.value)
        elif isinstance(n, ast.NamedExpr) and isinstance(n.target, ast.Name):
            add(n.target.id, "NamedExpr", n, n.value)
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            for nn in ast.walk(n.target):
                if isinstance(nn, ast.Name):
                    add(nn.id, "for目標", n, n.iter)
        elif isinstance(n, ast.With):
            for it in n.items:
                if it.optional_vars is not None:
                    for nn in ast.walk(it.optional_vars):
                        if isinstance(nn, ast.Name):
                            add(nn.id, "with目標", n, it.context_expr)
    for a in list(func.args.args) + list(func.args.kwonlyargs):
        add(a.arg, "形參", func, None)
    return idx


def trace(func, src, expr, depth=0, seen=None):
    """逆溯一式所依之名，**至其名於本函式內⛔ 再有綁定為止**；回逐層之記述。

    🩸 **本函式之首版於「遇第一個字面鍵即止」**——該止法使鏈止於 `_sl_left.get('mid')` 之
       `'mid'`，而**⛔ 抵登記表之鍵**（`ss.get('f3_cad_side_lines_by_side', …)`）
       ⇒ `§五-3` 之 [必命中甲] 誤紅。單所令者為「**鍵鏈**」（chain），
       其止點係「**以字面鍵取自登記表之式**」，⛔ 任一字面鍵。
       ⇒ 改為**逐層累積字面鍵、續溯至名無綁定**（自然終止）或逾深度上限。
    """
    seen = seen or set()
    rec = []
    if depth > TRACE_CAP:
        LOUD.append("逆溯深度逾 %d ⇒ 截斷（loud）" % TRACE_CAP)
        rec.append({"層": depth, "註": "⛔ 逾深度上限·截斷"})
        return rec
    if expr is None:
        return rec
    reg = registry_reads(func, expr)
    rec.append({"層": depth, "式": seg(src, expr), "字面鍵": literal_keys(expr),
                "登記表讀取": [{"鍵": k, "基名": b} for k, b in reg]})
    if reg:
        return rec                       # 🔒 已達「以字面鍵取自登記表之式」⇒ **止**
    for n in ast.walk(expr):
        if isinstance(n, ast.Name) and n.id not in seen:
            seen.add(n.id)
            bs = bindings_of(func, n.id)
            if not bs:
                continue                 # 本函式內無綁定（形參／外層／內建）⇒ 該支止
            for kind, st, rhs in bs:
                if rhs is None:
                    rec.append({"層": depth + 1, "名": n.id, "綁定": kind,
                                "式": "（形參·無 RHS）"})
                    continue
                r2 = registry_reads(func, rhs)
                rec.append({"層": depth + 1, "名": n.id, "綁定": kind,
                            "式": seg(src, rhs), "字面鍵": literal_keys(rhs),
                            "登記表讀取": [{"鍵": k, "基名": b} for k, b in r2]})
                if not r2:
                    rec.extend(trace(func, src, rhs, depth + 2, seen))
    return rec


# ─────────────────────────────────────────────────────────────────────
#  薄殼（以 AST 證其轉傳）
# ─────────────────────────────────────────────────────────────────────
def thin_shells(tree, kw_out, kw_in_prefix="_"):
    """同檔內以**形參原樣**轉傳 `kw_out=` 至 `_solve_G_one` 之函式 ⇒ {fname: 形參名}。"""
    out = {}
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        params = {a.arg for a in list(fn.args.args) + list(fn.args.kwonlyargs)}
        for c in ast.walk(fn):
            if not isinstance(c, ast.Call):
                continue
            if func_form(c.func, SOLVE) is None:
                continue
            for kw in c.keywords:
                if kw.arg == kw_out and isinstance(kw.value, ast.Name) \
                        and kw.value.id in params:
                    out[fn.name] = kw.value.id
    return out


def calls_to(func, tree, names):
    """該函式內對 `_solve_G_one` 或其薄殼之呼叫。"""
    out = []
    for c in ast.walk(func):
        if not isinstance(c, ast.Call):
            continue
        if func_form(c.func, SOLVE):
            out.append((SOLVE, c))
        elif isinstance(c.func, ast.Name) and c.func.id in names:
            out.append((c.func.id, c))
        elif isinstance(c.func, ast.Subscript) and isinstance(c.func.slice, ast.Constant) \
                and c.func.slice.value in names:
            out.append((c.func.slice.value, c))
    return out


def kwarg_of(call, wanted):
    for kw in call.keywords:
        if kw.arg in wanted:
            return kw.arg, kw.value
    return None, None


# ─────────────────────────────────────────────────────────────────────
#  主
# ─────────────────────────────────────────────────────────────────────
def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else None
    assert rev, "🛑 須以 rev 呼叫（rev 釘死·⛔ 用工作區）"
    full = sh(["git", "rev-parse", rev]).stdout.decode().strip()

    print(BAR)
    print("【`W-G.9-307` `§五` 七處之在域現查】**AST 為框**·靜態·⛔ 跑 harness")
    print("rev（釘死·全 40 碼）＝ %s" % full)
    print(BAR)

    files = prod34(full)
    print("\n母體（**正面列舉**·外部錨 ＝ `§一` 閘 `7`）＝ **%d** 檔" % len(files))

    # 🔒 **`seg` 之自我驗證閘**（重建須自證＝現況·⛔ 器綠即認其重建為真）
    _n = _same = _diff = 0
    for _f in files:
        _s = blob(full, _f).decode("utf-8")
        if TARGET not in _s:
            continue
        _t = ast.parse(_s)
        for _x in ast.walk(_t):
            if not isinstance(_x, (ast.Call, ast.Assign, ast.Name, ast.Constant)):
                continue
            _n += 1
            if _n % 97:                      # 抽樣（全量過鉅）·樣本數出艙
                continue
            _a = ast.get_source_segment(_s, _x)
            if _a is None:
                continue
            _same += (seg(_s, _x) == _a)
            _diff += (seg(_s, _x) != _a)
    print("🔒 `seg` 自我驗證閘（vs `ast.get_source_segment`·抽樣 1/97）⇒ 相同 **%d**／相異 **%d** ⇒ %s"
          % (_same, _diff, "✅" if _diff == 0 and _same > 0 else "🔴 **器紅·停**"))
    assert _diff == 0 and _same > 0, "🛑 `seg` 之重建⛔ 等於 `ast.get_source_segment` ⇒ 器紅"

    sites, residue, trees = collect_sites(full, files)

    # ── 款 `1` ───────────────────────────────────────────────────────
    print("\n" + BAR)
    print("── 款 `1`　呼叫端集 `S`（框之語法形**窮舉**：①Name ②Subscript ③Attribute ④Alias 一層）──")
    print(BAR)
    print("`S` 之基數 ＝ **%d**（期 `7`）" % len(sites))
    rows = []
    for k, s in enumerate(sites, 1):
        fn = enclosing_func(s["call"])
        qn = qualname(fn) if fn else "<module>"
        args = s["call"].args
        ad = seg(s["src"], args[3]) if len(args) > 3 else None
        for kw in s["call"].keywords:
            if kw.arg == "allocation_dir":
                ad = seg(s["src"], kw.value)
        side = seg(s["src"], args[5]) if len(args) > 5 else None
        for kw in s["call"].keywords:
            if kw.arg == "side":
                side = seg(s["src"], kw.value)
        lab = None
        for kw in s["call"].keywords:
            if kw.arg == "_label":
                lab = seg(s["src"], kw.value)
        rows.append({"#": k, "file": s["file"], "qual": qn, "form": s["form"],
                     "alloc": ad, "side": side, "label": lab,
                     "def_line": getattr(fn, "lineno", None), "site": s})
    print("\n| # | 檔 | 所在函式 qualname | 形 | `allocation_dir` 位逐字 | `side` 逐字 | `_label` 逐字 |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        print("| `%d` | `%s` | `%s` | %s | `%s` | `%s` | `%s` |"
              % (r["#"], r["file"], r["qual"], r["form"], r["alloc"], r["side"], r["label"]))

    print("\n🔒 **殘餘之全量**（含字樣而⛔ 屬上列 `func` 者·⛔ 靜默略過）＝ **%d** 節點" % len(residue))
    for x in residue:
        print("   - `%s` ｜ 節點型別 `%s` ｜ 列 `%s`（⛔ 作錨·僅出艙）｜ qualname `%s`"
              % (x["file"], x["type"], x["line"], x["qual"]))

    # ── 款 `2` ───────────────────────────────────────────────────────
    print("\n" + BAR)
    print("── 款 `2`　逐處之在域事實（**全量**·每處一節）──")
    print(BAR)
    d1_results = {}
    for r in rows:
        s = r["site"]
        src, tree = s["src"], s["tree"]
        fn = enclosing_func(s["call"])
        paths = stmt_paths(fn) if fn else {}
        cst = owning_stmt(s["call"], paths)
        cpath = paths.get(id(cst)) if cst else None
        print("\n### 處 `%d`　`%s` :: `%s`　（形 %s）" % (r["#"], r["file"], r["qual"], r["form"]))

        # (a)
        print("**`(a)` 所在函式與外圍守衛**")
        print("   - qualname ＝ `%s`｜其 `def` 列 ＝ `%s`（⛔ 作錨·僅出艙）" % (r["qual"], r["def_line"]))
        guards, p = [], getattr(s["call"], "_parent", None)
        while p is not None and p is not fn:
            if isinstance(p, ast.If):
                guards.append(("If", seg(src, p.test)))
            elif isinstance(p, ast.IfExp):
                guards.append(("IfExp", seg(src, p.test)))
            elif isinstance(p, ast.Try):
                guards.append(("Try", "（try 區·handlers ＝ %s）"
                               % [seg(src, h.type) if h.type else "bare" for h in p.handlers]))
            p = getattr(p, "_parent", None)
        if guards:
            for kind, t in guards:
                print("   - 外圍 `%s` 之 `test` 逐字（由內而外）＝ `%s`" % (kind, t))
        else:
            print("   - 🛑 **loud：無外圍 `If`／`IfExp`／`Try`**（判定組為空·照實具名）")

        # (b)
        print("**`(b)` 實參**：`allocation_dir` ＝ `%s`｜`side` ＝ `%s`｜`_label` ＝ `%s`"
              % (r["alloc"], r["side"], r["label"]))

        # (c)
        print("**`(c)` 街廓鍵**")
        ckeys = []
        for kind, t in guards:
            for nm in [t]:
                pass
        for g in guards:
            try:
                gt = ast.parse(g[1], mode="eval").body if g[0] != "Try" else None
            except Exception:                                 # noqa: BLE001
                gt = None
            if gt is not None:
                for nn in ast.walk(gt):
                    if isinstance(nn, ast.Name):
                        for kind, st, rhs in bindings_of(fn, nn.id):
                            ks = literal_keys(rhs) if rhs is not None else []
                            if ks:
                                ckeys.append((nn.id, kind, seg(src, rhs), ks))
        if ckeys:
            for nm, kind, rhs, ks in ckeys:
                print("   - 守衛名 `%s`（`%s`）⇒ RHS 逐字 `%s`｜**字面鍵** %s" % (nm, kind, rhs, ks))
        else:
            print("   - 🛑 **loud：守衛內無可逆溯至字面鍵之名**（照實具名）")

        # (d1)
        print("**`(d1)` 側界線之 `mid` 之在域來源**")
        shells = thin_shells(tree, KW_MID)
        cl = calls_to(fn, tree, set(shells)) if fn else []
        d1 = []
        for cname, c in cl:
            k, v = kwarg_of(c, {KW_MID, "_" + KW_MID})
            if v is not None:
                d1.append((cname, k, v))
        if not d1:
            print("   - 🛑 **loud：`(d1)` 為空**（該函式內無以 `%s`／`_%s` 傳入 `%s` 或其薄殼之實參）"
                  % (KW_MID, KW_MID, SOLVE))
            print("   - `(d3)` 之處置見下")
        for cname, k, v in d1:
            print("   - 經 `%s`（kw `%s`）⇒ 實參逐字 ＝ `%s`" % (cname, k, seg(src, v)))
            for line in trace(fn, src, v):
                print("        %s" % json.dumps(line, ensure_ascii=False))
        d1_results[r["#"]] = d1

        # (d2)
        print("**`(d2)` 綁定與強制呼叫之先後**（🔒 **以語句路徑判·⛔ 以行號判**）")
        if not d1:
            print("   - （`(d1)` 為空 ⇒ 無受詞·判定組為空·loud 具名）")
        for cname, k, v in d1:
            nms = sorted({n.id for n in ast.walk(v) if isinstance(n, ast.Name)})
            for nm in nms:
                for kind, st, rhs in bindings_of(fn, nm):
                    bp = paths.get(id(st))
                    if bp is None or cpath is None:
                        print("   - 名 `%s`（`%s`）⇒ ⛔ 可定位其語句路徑（loud）" % (nm, kind))
                        continue
                    rel = "前" if cmp_path(bp, cpath) < 0 else "後"
                    print("   - 名 `%s`（`%s`）之綁定語句路徑 ＝ `%s`；強制呼叫之語句路徑 ＝ `%s` ⇒ **%s**"
                          % (nm, kind, bp, cpath, rel))
                    rebinds = [x for x in bindings_of(fn, nm)
                               if paths.get(id(x[1])) is not None
                               and cmp_path(min(bp, cpath, key=lambda z: str(z)),
                                            paths[id(x[1])]) < 0
                               and cmp_path(paths[id(x[1])],
                                            max(bp, cpath, key=lambda z: str(z))) < 0]
                    print("        二者之間重綁該名之語句 ＝ %s"
                          % ([kk for kk, _, _ in rebinds] or "空集（**loud 具名其為空**）"))

        # (e1)
        print("**`(e1)` `K-9-30` 之述詞之在域來源**（`%s` 之實參）" % KW_CORNER)
        shells_c = thin_shells(tree, KW_CORNER)
        cl2 = calls_to(fn, tree, set(shells_c)) if fn else []
        e1 = []
        for cname, c in cl2:
            k, v = kwarg_of(c, {KW_CORNER, "_" + KW_CORNER})
            if v is not None:
                e1.append((cname, k, v))
        if not e1:
            print("   - 🛑 **loud：`(e1)` 為空**（該函式內無 `%s` 或其薄殼之 `%s` 實參）"
                  % (SOLVE, KW_CORNER))
        for cname, k, v in e1:
            print("   - 經 `%s`（kw `%s`）⇒ 實參逐字 ＝ `%s`" % (cname, k, seg(src, v)))
            for line in trace(fn, src, v):
                print("        %s" % json.dumps(line, ensure_ascii=False))

        # (e2)
        print("**`(e2)` 該鏈上每一名於強制呼叫之時是否已綁定**")
        if not e1:
            print("   - （`(e1)` 為空 ⇒ 判定組為空·loud 具名）")
        for cname, k, v in e1:
            for nm in sorted({n.id for n in ast.walk(v) if isinstance(n, ast.Name)}):
                bs = bindings_of(fn, nm)
                if not bs:
                    print("   - 名 `%s` ⇒ **未綁定**（該函式內無其綁定）" % nm)
                    continue
                for kind, st, rhs in bs:
                    bp = paths.get(id(st))
                    if bp is None or cpath is None:
                        print("   - 名 `%s`（`%s`）⇒ ⛔ 可定位（loud）" % (nm, kind))
                        continue
                    ok = cmp_path(bp, cpath) < 0
                    print("   - 名 `%s`（`%s`）⇒ **%s**（綁定路徑 `%s` vs 呼叫路徑 `%s`）"
                          % (nm, kind, "已綁定" if ok else "🛑 **未綁定**（其值依強制呼叫<u>之後</u>始決定）",
                             bp, cpath))

        # (e3)
        if not cl2:
            print("**`(e3)`** 該函式內無 `%s` 之呼叫 ⇒ 讀取同一欄位名之處：" % SOLVE)
            found = []
            for n in ast.walk(fn):
                if isinstance(n, ast.Name) and n.id == KW_CORNER:
                    found.append(getattr(n, "lineno", None))
                if isinstance(n, ast.Constant) and n.value == KW_CORNER:
                    found.append(getattr(n, "lineno", None))
            print("   - 命中列（⛔ 作錨·僅出艙）＝ %s%s"
                  % (found, "" if found else "　🛑 **loud：⛔ 在域**"))

        # (f)
        print("**`(f)` 是否由 `run_verification` 驅動**：⛔ 重量 ⇒ **逕引 `W-G.9-300R`**"
              "（其 `F` 之逐處具名見該報告 `三-2`；本器⛔ 複算）")

    # ── 款 `3` ───────────────────────────────────────────────────────
    print("\n" + BAR)
    print("── 款 `3`　判別力造 ──")
    print(BAR)
    ok7 = (len(sites) == 7)
    print("[必為 `7`] 外部錨 ＝ `W-G.9-300R` 之「AST 之處」⇒ `S` 基數 %d ⇒ %s"
          % (len(sites), "✅" if ok7 else "🔴"))

    # [必命中甲]／[必命中乙]：stepg_pipeline 之左支
    tgt = [r for r in rows
           if r["file"].endswith("stepg_pipeline.py") and r["side"] and "left" in r["side"]]
    hit_a = hit_b = False
    if tgt:
        r = tgt[0]
        d1 = d1_results.get(r["#"], [])
        names, keys = set(), set()
        for cname, k, v in d1:
            for n in ast.walk(v):
                if isinstance(n, ast.Name):
                    names.add(n.id)
            fnx = enclosing_func(r["site"]["call"])
            for line in trace(fnx, r["site"]["src"], v):
                for kk in line.get("字面鍵", []) or []:
                    keys.add(kk)
                if "名" in line:
                    names.add(line["名"])
        hit_a = any(n.endswith("_side_mid_left") or n == "_side_mid_left" for n in names) \
            and ("f3_cad_side_lines_by_side" in keys)
        print("[必命中甲] `stepg_pipeline.py` 左支之 `(d1)` ⇒ 得名集含 `_side_mid_left` ＝ %s"
              "；鍵鏈含字面 `f3_cad_side_lines_by_side` ＝ %s ⇒ %s"
              % ("_side_mid_left" in names, "f3_cad_side_lines_by_side" in keys,
                 "✅" if hit_a else "🔴"))
        print("     （實得名集 ＝ %s｜實得字面鍵 ＝ %s）"
              % (sorted(names), sorted(keys)))
        # 乙：以語句路徑重判
        fnx = enclosing_func(r["site"]["call"])
        px = stmt_paths(fnx)
        cs = owning_stmt(r["site"]["call"], px)
        cp = px.get(id(cs))
        rel = None
        for kind, st, rhs in bindings_of(fnx, "_side_mid_left"):
            bp = px.get(id(st))
            if bp is not None and cp is not None:
                rel = "前" if cmp_path(bp, cp) < 0 else "後"
        hit_b = (rel == "後")
        print("[必命中乙] 同上之 `(d2)` ＝ `%s`（期 `後`）⇒ %s" % (rel, "✅" if hit_b else "🔴"))
        # 🔑 鍵鏈之**判別力對照**（⛔ 令 [必命中甲] 恆真）：逐處之 `(d1)` 鍵鏈是否含該字面
        print("     🔑 **鍵鏈之判別力對照**（該字面須⛔ 逐處皆中，否則該檢恆真）：")
        per = []
        for rr in rows:
            ks2 = set()
            fny = enclosing_func(rr["site"]["call"])
            for cname, k, v in d1_results.get(rr["#"], []):
                for line in trace(fny, rr["site"]["src"], v):
                    for kk in line.get("字面鍵", []) or []:
                        ks2.add(kk)
            per.append((rr["#"], rr["file"], "f3_cad_side_lines_by_side" in ks2))
        for num, f, ok in per:
            print("        處 `%d`（`%s`）⇒ 含該字面 ＝ %s" % (num, f, ok))
        nhit = sum(1 for _, _, ok in per if ok)
        print("        ⇒ 命中 %d ／ %d 處 ⇒ %s"
              % (nhit, len(per),
                 "✅ **非恆真**（該檢具鑑別力）" if 0 < nhit < len(per) else
                 "🔴 **恆真或恆假 ⇒ 該檢⛔ 具鑑別力**"))
    else:
        print("🛑 **loud：⛔ 覓得 `stepg_pipeline.py` 之左支 ⇒ 判定組為空 ⇒ 拒測**")

    # [必為零]：執行期組出之人造函式名
    fake = "_corner_" + "buffer_" + "S" + chr(90) + chr(90)   # 執行期組出·字面⛔ 出艙
    cnt = 0
    for f in files:
        try:
            src = blob(full, f).decode("utf-8")
        except AssertionError:
            continue
        if fake not in src:
            pass
        t = ast.parse(src)
        for n in ast.walk(t):
            if isinstance(n, ast.Call) and func_form(n.func, fake):
                cnt += 1
    print("[必為零] 以**執行期組出**之人造函式名重跑款 `1` 之框 ⇒ `S` 基數 %d（須 `0`）⇒ %s"
          % (cnt, "✅" if cnt == 0 else "🔴"))

    # ── 停十一 ───────────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-4`　停機款 ──")
    print(BAR)
    stop11 = not ok7
    print("**停十一**（`S` 基數 ≠ `7`，或⛔ 與 `S1`〜`S7` 逐一對照）⇒ %s"
          % ("🔴 **成就 ⇒ 停、上呈**" if stop11 else "✅ **不成就**"))
    print("🔒 款 `2` 之任一「⛔ 在域」**⛔ 停**——其為量測之結果，逐處照實具名，**裁屬發單側**。")

    print("\n── 🛑 loud 之全量 ──")
    if not LOUD:
        print("   （無記錄）**⛔ 讀為「無異常」**")
    for m in sorted(set(LOUD)):
        print("   - %s   ×%d" % (m, LOUD.count(m)))

    print("\n" + BAR)
    print("【本器⛔ 判改法·⛔ 判可施與否·⛔ 擬任何 diff】")
    print(BAR)


main()
