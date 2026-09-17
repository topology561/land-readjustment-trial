"""`W-G.9-308` `§五`：**七處在域現查之補量**（**AST 為框**·靜態·⛔ 跑 harness）。

🔒 授權（單 `§五` 首段逐字）：新增本量測器 ＋ 其落檔 `verify/out/WG9308R_sites2.log`
   （**AST 為框**·讀 blob 取 bytes·**`rev` 釘死`）。
🛑 本器**⛔ 判改法、⛔ 判可施與否、⛔ 擬任何 diff**。
🛑 **⛔ 動 `verify/probes/probe_WG9307R_sites.py` 一字。**

🩸 **`import` 之照實具名（單 `§五` 首段「得 `import` 其函式，惟須出艙所用之名」）**
   `verify/probes/probe_WG9307R_sites.py` 之**模組級末列為 `main()`**（⛔ `if __name__` 之守衛）
   ⇒ `import` 之即驅動其全量、並覆寫其落檔 ⇒ **本器⛔ `import` 之**（所用之名 ＝ **無**）。
   其框（`func_form` ①Name ②Subscript ③Attribute ＋ `alias_names` ④Alias 一層）於本器**逐字重寫**，
   並以**外部錨**（`S` ＝ `7`、且 `S1`〜`S7` 之 (檔, qualname, 形) 與 `verify/out/WG9307R_sites.log`
   所印者逐一相符）自證其框未漂移。

🛑 **泛用化**：⛔ 硬寫街廓名、側標籤、個案常數；受詞名（`_corner_buffer_S` 等）係**受詞本身**。

用法：`python verify/probes/probe_WG9308R_sites2.py <rev>`（`rev` 須釘死·⛔ 用工作區）。
"""
import ast
import hashlib
import io
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")

# 🔒 落檔 ＝ `open(p, 'wb')`（⛔ shell 重導向 Python `stdout`·坑 `bn`）
_BUF = io.StringIO()
_REAL = sys.stdout


class _Tee(object):
    def write(self, s):
        _REAL.write(s)
        _BUF.write(s)

    def flush(self):
        _REAL.flush()


sys.stdout = _Tee()

TARGET = "_corner_buffer_S"
REG_LIT = "f3L_forced_offset"
REG_WORD = "forced"
CAD_NAME = "cad"
SLBS = "side_lines_by_side"
SS_KEY = "f3_cad_side_lines_by_side"
TRACE_CAP = 12
FIELD_CAP = 8
BAR = "=" * 116
LOUD = []

# 🔒 款 `6` 之名集 `ℕ`（發單側自 blob 定·逐字·**20** 名）
N6 = ["is_first_corner_marker", "is_first_corner_l", "is_first_corner_r",
      "is_second_after_corner", "is_corner_first", "_is_first_corner",
      "is_chain_head", "_is_chain_head", "is_corner_winner",
      "_lg_idx_left", "_lg_idx_right", "first_corner_used_left",
      "first_corner_used_right", "_first_corner_alloc_dir",
      "_near_dir_left", "_near_dir_right", "驗_宗序", "第1筆街角",
      "is_corner", "_is_corner"]

# 🔒 款 `7` 之名集 `ℕ′`（發單側自 blob 定·逐字·**11** 名）
N7 = ["_build_corner_range_v3", "eff_min_build", "_end_region_R", "_end_band",
      "_end_gate", "_area_rend", "_place_pool_parcels", "get_min_lot_size",
      "_k923_gate2", "_lot_gate", "S_raw"]

IDX_NAMES = ("_lg_idx_left", "_lg_idx_right")


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
#  AST 基建
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


def lines_of(src_b):
    return src_b.decode("utf-8").split("\n")


def line_at(lines, node):
    ln = getattr(node, "lineno", None)
    if ln is None or ln < 1 or ln > len(lines):
        return "—"
    return lines[ln - 1].rstrip("\r")


def uq(node):
    try:
        return ast.unparse(node)
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("unparse 例外：%r" % (e,))
        return "<unparse 失敗>"


# ─────────────────────────────────────────────────────────────────────
#  款 `1`：呼叫端集 `S`（框逐字承 `W-G.9-307 §五-1`）
# ─────────────────────────────────────────────────────────────────────
def func_form(fn, name):
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
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name):
            if func_form(n.value, name):
                out[n.targets[0].id] = n
    return out


def collect_sites(rev, files):
    sites, trees = [], {}
    for f in files:
        src_b = blob(rev, f)
        src = src_b.decode("utf-8")
        if TARGET not in src:
            continue
        tree = ast.parse(src)
        annotate(tree)
        trees[f] = (src_b, tree, lines_of(src_b))
        alias = alias_names(tree, TARGET)
        for n in ast.walk(tree):
            if not isinstance(n, ast.Call):
                continue
            form = func_form(n.func, TARGET)
            if form is None and isinstance(n.func, ast.Name) and n.func.id in alias:
                form = "④Alias(%s)" % n.func.id
            if form:
                sites.append({"file": f, "call": n, "form": form})
    return sites, trees


# ─────────────────────────────────────────────────────────────────────
#  款 `1`（`a′`）：外圍守衛之**全鏈與極性**
# ─────────────────────────────────────────────────────────────────────
GUARD_TYPES = (ast.If, ast.IfExp, ast.Try, ast.For, ast.AsyncFor, ast.While,
               ast.With, ast.AsyncWith)


def field_of(parent, child):
    """回 (欄位名, 索引)：`child` 於 `parent` 之何欄。⛔ 命中 ⇒ (None, None)。"""
    for fld, val in ast.iter_fields(parent):
        if val is child:
            return (fld, None)
        if isinstance(val, list):
            for i, x in enumerate(val):
                if x is child:
                    return (fld, i)
    return (None, None)


def guard_chain(call, lines):
    """自呼叫節點上溯至其所在函式之 `def`，逐層回報外圍守衛。"""
    fn = enclosing_func(call)
    out = []
    child = call
    p = getattr(child, "_parent", None)
    depth = 0
    while p is not None and p is not fn and depth < 64:
        depth += 1
        if isinstance(p, GUARD_TYPES):
            fld, idx = field_of(p, child)
            if isinstance(p, (ast.For, ast.AsyncFor)):
                head = "target ＝ `%s`／iter ＝ `%s`" % (uq(p.target), uq(p.iter))
            elif isinstance(p, (ast.If, ast.IfExp, ast.While)):
                head = "test ＝ `%s`" % uq(p.test)
            elif isinstance(p, ast.Try):
                head = "（`Try` ⛔ `test`）"
            else:
                head = "items ＝ `%s`" % "; ".join(uq(it.context_expr)
                                                  for it in getattr(p, "items", []))
            out.append({
                "型別": type(p).__name__,
                "欄位名": fld if fld else "🛑 ⛔ 命中",
                "索引": idx,
                "head": head,
                "列": getattr(p, "lineno", None),
                "該列逐字": line_at(lines, p),
            })
        child = p
        p = getattr(p, "_parent", None)
    return fn, out


# ─────────────────────────────────────────────────────────────────────
#  款 `2`（`c′`）：街廓鍵之逆溯
# ─────────────────────────────────────────────────────────────────────
def bind_index(func):
    """回 {名: [(形, 語句, 右式)]}。形 ∈ {`Assign`, `For 目標`, `形參`, `with`}。"""
    idx = {}

    def add(nm, kind, st, rhs):
        idx.setdefault(nm, []).append((kind, st, rhs))

    for a in list(func.args.posonlyargs) + list(func.args.args) + list(func.args.kwonlyargs):
        add(a.arg, "形參", func, None)
    if func.args.vararg:
        add(func.args.vararg.arg, "形參(*)", func, None)
    if func.args.kwarg:
        add(func.args.kwarg.arg, "形參(**)", func, None)
    for n in ast.walk(func):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                for nm in ast.walk(t):
                    if isinstance(nm, ast.Name):
                        add(nm.id, "Assign", n, n.value)
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign)):
            if isinstance(n.target, ast.Name):
                add(n.target.id, type(n).__name__, n, n.value)
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            for nm in ast.walk(n.target):
                if isinstance(nm, ast.Name):
                    add(nm.id, "For 目標", n, n.iter)
        elif isinstance(n, (ast.With, ast.AsyncWith)):
            for it in n.items:
                if it.optional_vars is not None:
                    for nm in ast.walk(it.optional_vars):
                        if isinstance(nm, ast.Name):
                            add(nm.id, "with", n, it.context_expr)
    return idx


def key_of_registry_read(node):
    """若 `node` 係自強制登記表取值之式，回 (鍵之 AST, 式逐字)；否則 `None`。"""
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Subscript):
            recv = uq(n.value)
            if REG_LIT in recv or REG_WORD in recv:
                out.append((n.slice, uq(n)))
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr == "get" and n.args:
            recv = uq(n.func.value)
            if REG_LIT in recv or REG_WORD in recv:
                out.append((n.args[0], uq(n)))
    return out


def trace_block_key(func, names, lines):
    """自守衛所用之名逆溯至強制登記表之取值式，回其街廓鍵之實參。"""
    idx = bind_index(func)
    seen, queue, found = set(), list(names), []
    steps = []
    depth = 0
    while queue and depth < TRACE_CAP:
        depth += 1
        nxt = []
        for nm in queue:
            if nm in seen:
                continue
            seen.add(nm)
            for kind, st, rhs in idx.get(nm, []):
                steps.append({"名": nm, "形": kind,
                              "語句逐字": uq(st) if kind != "形參" else "（形參·⛔ 語句）",
                              "列": getattr(st, "lineno", None),
                              "該列逐字": line_at(lines, st)})
                if rhs is None:
                    continue
                hits = key_of_registry_read(rhs)
                for kn, expr in hits:
                    found.append({"鍵逐字": uq(kn), "取值式逐字": expr,
                                  "經由之名": nm})
                for sub in ast.walk(rhs):
                    if isinstance(sub, ast.Name) and sub.id not in seen:
                        nxt.append(sub.id)
        queue = nxt
    if depth >= TRACE_CAP:
        LOUD.append("款 `2` 逆溯深度逾 `%d` ⇒ loud 截斷" % TRACE_CAP)
    return found, steps, idx


def binding_form_of(idx, key_src, func, lines):
    """回該鍵之綁定語句逐字與其形。"""
    out = []
    for kind, st, _rhs in idx.get(key_src, []):
        out.append({"形": kind,
                    "語句逐字": (uq(st) if kind not in ("形參", "形參(*)", "形參(**)")
                                 else "（形參 of `%s`）" % func.name),
                    "列": getattr(st, "lineno", None),
                    "該列逐字": line_at(lines, st)})
    return out


# ─────────────────────────────────────────────────────────────────────
#  款 `6`／`7`：AST 六形之普查
# ─────────────────────────────────────────────────────────────────────
def six_form_hits(tree, lines, nameset):
    """框 ＝ 六形：`Name.id`／`Attribute.attr`／`keyword.arg`／`arg.arg`／
    `FunctionDef.name`／`str` 型 `Constant.value`（**整值相等**·⛔ 子字串）。"""
    hits = []
    S = set(nameset)
    for n in ast.walk(tree):
        got = None
        if isinstance(n, ast.Name) and n.id in S:
            got = ("Name.id", n.id)
        elif isinstance(n, ast.Attribute) and n.attr in S:
            got = ("Attribute.attr", n.attr)
        elif isinstance(n, ast.keyword) and n.arg in S:
            got = ("keyword.arg", n.arg)
        elif isinstance(n, ast.arg) and n.arg in S:
            got = ("arg.arg", n.arg)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in S:
            got = ("FunctionDef.name", n.name)
        elif isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value in S:
            got = ("Constant.value", n.value)
        if got:
            hits.append({"形": got[0], "名": got[1],
                         "qual": qualname(n),
                         "列": getattr(n, "lineno", None),
                         "該列逐字": line_at(lines, n)})
    return hits


def idx_compares(tree, lines):
    """以整數字面 `0`／`1` 與 `_lg_idx_left`／`_lg_idx_right` 比較之式（`Compare`·兩側任一）。"""
    out = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Compare):
            continue
        parts = [n.left] + list(n.comparators)
        has_idx = any(isinstance(x, ast.Name) and x.id in IDX_NAMES for x in parts)
        has_lit = any(isinstance(x, ast.Constant) and isinstance(x.value, int)
                      and not isinstance(x.value, bool) and x.value in (0, 1)
                      for x in parts)
        if has_idx and has_lit:
            out.append({"式逐字": uq(n), "qual": qualname(n),
                        "列": getattr(n, "lineno", None),
                        "該列逐字": line_at(lines, n)})
    return out


# ─────────────────────────────────────────────────────────────────────
#  main
# ─────────────────────────────────────────────────────────────────────
def main():
    rev = sys.argv[1]
    files = prod34(rev)
    print(BAR)
    print("【`W-G.9-308` `§五`　七處在域現查之補量】（**AST 為框**·靜態·`rev` 釘死）")
    print("`rev` ＝ `%s`" % rev)
    print("母體（生產碼·**正面列舉**）＝ **%d** 檔（`app.py` ＋ `verify/` 頂層 `*.py`）" % len(files))
    print("🩸 `import probe_WG9307R_sites` ＝ **未為**（其模組級末列為 `main()`）⇒ 所用之名 ＝ **無**")
    print(BAR)

    sites, trees = collect_sites(rev, files)
    print("\n── 呼叫端集 `S`（框逐字承 `W-G.9-307 §五-1`：①Name ②Subscript ③Attribute ④Alias 一層）──")
    print("`S` 之基數 ＝ **%d**（期 `7`）" % len(sites))
    print("| 處 | 檔 | qualname | 形 | 列 |")
    print("|---|---|---|---|---|")
    site_sig = []
    for k, s in enumerate(sites, 1):
        fn = enclosing_func(s["call"])
        q = fn.name if fn is not None else "<module>"
        site_sig.append((s["file"], q, s["form"]))
        print("| `%d` | `%s` | `%s` | %s | `%s` |"
              % (k, s["file"], q, s["form"], getattr(s["call"], "lineno", None)))

    # 外部錨（自 `verify/out/WG9307R_sites.log` 所印者·逐字）
    ANCHOR = [("app.py", "main", "①Name"),
              ("app.py", "main", "①Name"),
              ("verify/stepg_pipeline.py", "_run_step_g_impl", "①Name"),
              ("verify/stepg_pipeline.py", "_run_step_g_impl", "①Name"),
              ("verify/wf_f1.py", "compute", "②Subscript"),
              ("verify/wf_f4.py", "_reshape_block", "②Subscript"),
              ("verify/wf_f4.py", "_reshape_block", "②Subscript")]
    same7 = (site_sig == ANCHOR)
    print("\n🔒 **外部錨**（`verify/out/WG9307R_sites.log` 之處 `1`〜`7` 之 (檔, qualname, 形)）")
    print("   逐一相符 ＝ **%s**" % same7)
    if not same7:
        print("   🔴 本器所得 ＝ %r" % (site_sig,))
        print("   🔴 錨       ＝ %r" % (ANCHOR,))

    # ── 款 `1` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-1`　款 `1`　`(a′)` 外圍守衛之**全鏈與極性**（全量 `%d` 處）──" % len(sites))
    for k, s in enumerate(sites, 1):
        src_b, tree, lines = trees[s["file"]]
        fn, chain = guard_chain(s["call"], lines)
        print("\n### 處 `%d`　`%s` :: `%s`　（形 %s·呼叫列 `%s`）"
              % (k, s["file"], fn.name if fn else "<module>", s["form"],
                 getattr(s["call"], "lineno", None)))
        print("  `def` 之列 ＝ `%s`；外圍守衛層數 ＝ **%d**"
              % (getattr(fn, "lineno", None) if fn else None, len(chain)))
        if not chain:
            print("  🛑 **判定組為空**：自呼叫節點至 `def` 之間⛔ 任何 "
                  "`If`／`IfExp`／`Try`／`For`／`While`／`With` ⇒ loud 具名")
        print("  | 層 | 父節點型別 | **本節點所在之欄位名** | 索引 | `test`／`target`·`iter` 逐字 | 列 |")
        print("  |---|---|---|---|---|---|")
        for i, c in enumerate(chain, 1):
            print("  | %d | `%s` | **`%s`** | %s | %s | `%s` |"
                  % (i, c["型別"], c["欄位名"], c["索引"], c["head"], c["列"]))

    # ── 款 `2` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-2`　款 `2`　`(c′)` 街廓鍵（全量 `%d` 處）──" % len(sites))
    print("🔒 逆溯之止點 ＝ `.get(<X>)` 或 `[<X>]` 之**接收者鏈**含字面 `%s`（或含字面或名 `%s`）者"
          % (REG_LIT, REG_WORD))
    blkkeys = []
    for k, s in enumerate(sites, 1):
        src_b, tree, lines = trees[s["file"]]
        fn, chain = guard_chain(s["call"], lines)
        gnames = []
        # 守衛所用之名 ＝ 全鏈之 test／iter 內之 Name
        child, p = s["call"], getattr(s["call"], "_parent", None)
        while p is not None and p is not fn:
            if isinstance(p, (ast.If, ast.IfExp, ast.While)):
                gnames += [x.id for x in ast.walk(p.test) if isinstance(x, ast.Name)]
            elif isinstance(p, (ast.For, ast.AsyncFor)):
                gnames += [x.id for x in ast.walk(p.iter) if isinstance(x, ast.Name)]
            child, p = p, getattr(p, "_parent", None)
        gnames = list(dict.fromkeys(gnames))
        found, steps, idx = trace_block_key(fn, gnames, lines) if fn else ([], [], {})
        print("\n### 處 `%d`　`%s` :: `%s`" % (k, s["file"], fn.name if fn else "<module>"))
        print("  守衛所用之名（全鏈 `test`／`iter` 內之 `Name`·去重）＝ %s" % (gnames,))
        if not found:
            print("  🛑 **判定組為空**：逆溯⛔ 達含 `%s`／`%s` 之取值式 ⇒ loud 具名"
                  % (REG_LIT, REG_WORD))
            blkkeys.append(None)
        for f in found:
            print("  - **`<X>` 逐字 ＝ `%s`**（經由名 `%s`）｜取值式逐字 ＝ `%s`"
                  % (f["鍵逐字"], f["經由之名"], f["取值式逐字"]))
        ks = sorted({f["鍵逐字"] for f in found})
        if len(ks) == 1:
            blkkeys.append(ks[0])
        elif len(ks) > 1:
            blkkeys.append(ks)
            LOUD.append("處 `%d` 之 `<X>` 非單一：%r" % (k, ks))
        if ks:
            for kk in ks:
                bf = binding_form_of(idx, kk, fn, lines)
                if not bf:
                    print("    🛑 `<X>` ＝ `%s` 於該函式內⛔ 綁定語句（或係外部名）" % kk)
                for b in bf:
                    print("    · `<X>` ＝ `%s` 之綁定：**形 ＝ `%s`**｜列 `%s`｜語句逐字 ＝ `%s`"
                          % (kk, b["形"], b["列"], b["語句逐字"]))
        print("  （逆溯步數 ＝ %d）" % len(steps))
    print("\n🔒 **款 `2` 之總表**（處 ⇒ `<X>`）：%r" % (blkkeys,))

    # ── 款 `3` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-3`　款 `3`　`(d3)` 側界線登記表之在域可達性（處 `5`〜`7`）──")
    for k in (5, 6, 7):
        if k > len(sites):
            print("🛑 處 `%d` ⛔ 存在（`S` ＝ %d）⇒ loud" % (k, len(sites)))
            continue
        s = sites[k - 1]
        src_b, tree, lines = trees[s["file"]]
        fn = enclosing_func(s["call"])
        print("\n### 處 `%d`　`%s` :: `%s`" % (k, s["file"], fn.name if fn else "<module>"))
        idx = bind_index(fn) if fn else {}
        # ① 名 `cad` 之綁定語句（或形參）
        bl = idx.get(CAD_NAME, [])
        if not bl:
            print("  ① 名 `%s` 於該函式內：🛑 **⛔ 綁定亦⛔ 形參** ⇒ loud 具名" % CAD_NAME)
        for kind, st, _r in bl:
            print("  ① 名 `%s` ｜形 ＝ **`%s`**｜列 `%s`｜逐字 ＝ `%s`"
                  % (CAD_NAME, kind, getattr(st, "lineno", None),
                     uq(st) if kind not in ("形參", "形參(*)", "形參(**)")
                     else "（形參 of `%s`）" % fn.name))
        # ② 自該名上溯至 `ctx` 之 `"cad"` 之傳遞鏈
        calls = []
        for f2 in files:
            if f2 not in trees:
                sb = blob(rev, f2)
                try:
                    t2 = ast.parse(sb.decode("utf-8"))
                except SyntaxError as e:                      # noqa: BLE001
                    LOUD.append("parse 失敗：%s %r" % (f2, e))
                    continue
                annotate(t2)
                trees[f2] = (sb, t2, lines_of(sb))
            sb, t2, l2 = trees[f2]
            for n in ast.walk(t2):
                if isinstance(n, ast.Call):
                    nm = (n.func.id if isinstance(n.func, ast.Name)
                          else (n.func.attr if isinstance(n.func, ast.Attribute) else None))
                    if fn is not None and nm == fn.name:
                        calls.append((f2, n, l2))
        print("  ② 呼叫端（以被呼叫名 `%s` 為框）＝ **%d** 處"
              % (fn.name if fn else "?", len(calls)))
        for f2, n, l2 in calls:
            args = [uq(a) for a in n.args]
            kws = {(kw.arg or "**"): uq(kw.value) for kw in n.keywords}
            print("     · `%s`:`%s`｜實參 ＝ %r｜關鍵字 ＝ %r｜該列逐字 ＝ `%s`"
                  % (f2, getattr(n, "lineno", None), args, kws, line_at(l2, n)))
        if fn is not None:
            ps = [a.arg for a in (list(fn.args.posonlyargs) + list(fn.args.args)
                                  + list(fn.args.kwonlyargs))]
            print("     形參對位逐字 ＝ %r" % (ps,))
        # ⑥ 所在函式內字面 `side_lines_by_side` 或 `mid` 之讀取處
        rd = []
        if fn is not None:
            for n in ast.walk(fn):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) \
                        and n.value in (SLBS, "mid"):
                    rd.append((n.value, getattr(n, "lineno", None), line_at(lines, n)))
        print("  ⑥ 所在函式內字面 `%s`／`mid` 之讀取處 ＝ **%d**" % (SLBS, len(rd)))
        if not rd:
            print("     🛑 **loud**：現碼於該函式內**⛔ 讀**該字面")
        for v, ln, txt in rd:
            print("     · 字面 `%s`｜列 `%s`｜逐字 ＝ `%s`" % (v, ln, txt))

    # ③ harness 側
    print("\n#### ③ harness 側（`verify/run_verification.py`）")
    rvb = blob(rev, "verify/run_verification.py")
    rvt = ast.parse(rvb.decode("utf-8"))
    annotate(rvt)
    rvl = lines_of(rvb)
    for n in ast.walk(rvt):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value == "cad":
            par = getattr(n, "_parent", None)
            print("   · 字面 `\"cad\"`｜列 `%s`｜qual `%s`｜父 `%s`｜該列逐字 ＝ `%s`"
                  % (getattr(n, "lineno", None), qualname(n),
                     type(par).__name__ if par else None, line_at(rvl, n)))
    for n in ast.walk(rvt):
        hit = False
        for fld, val in ast.iter_fields(n):
            if isinstance(val, str) and val in (SLBS, SS_KEY):
                hit = True
        if hit and isinstance(n, ast.Constant):
            st = n
            while st is not None and not isinstance(st, ast.stmt):
                st = getattr(st, "_parent", None)
            print("   · 字面 `%s`｜列 `%s`｜qual `%s`｜語句逐字 ＝ `%s`"
                  % (n.value, getattr(n, "lineno", None), qualname(n),
                     uq(st) if st is not None else "—"))
    for n in ast.walk(rvt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "build_pipeline":
            rets = [x for x in ast.walk(n) if isinstance(x, ast.Return)]
            print("   · `build_pipeline` 之回傳語句 ＝ %d 處" % len(rets))
            for r in rets:
                print("       列 `%s`｜逐字 ＝ `%s`" % (getattr(r, "lineno", None), uq(r)))

    # ④ app 側
    print("\n#### ④ app 側（`app.py` 之 `_build_wf_ctx` 內鍵 `\"%s\"` 之值式）" % SLBS)
    apb = blob(rev, "app.py")
    apt = ast.parse(apb.decode("utf-8"))
    annotate(apt)
    apl = lines_of(apb)
    found_ctx = 0
    for n in ast.walk(apt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "_build_wf_ctx":
            for d in ast.walk(n):
                if isinstance(d, ast.Dict):
                    for kk, vv in zip(d.keys, d.values):
                        if isinstance(kk, ast.Constant) and kk.value == SLBS:
                            found_ctx += 1
                            print("   · 鍵 `%s` 之**值式逐字** ＝ `%s`｜列 `%s`｜該列逐字 ＝ `%s`"
                                  % (SLBS, uq(vv), getattr(vv, "lineno", None),
                                     line_at(apl, vv)))
                            # ⑤ `or {}` 之分支 loud
                            if isinstance(vv, ast.BoolOp) and isinstance(vv.op, ast.Or):
                                print("     ⑤ 🛑 **loud**：右式為 `%s` ⇒ 登記表為**假值**時"
                                      "產生**新物件**、與登記表**⛔ 為同一物**"
                                      % uq(vv.values[-1]))
    if found_ctx == 0:
        print("   🛑 **判定組為空** ⇒ loud 具名")

    print("\n#### ⑤ `or {}` 之分支（harness 側·全量）")
    for n in ast.walk(rvt):
        if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or):
            txt = uq(n)
            if SLBS in txt or SS_KEY in txt:
                print("   · 逐字 ＝ `%s`｜列 `%s`｜qual `%s`" % (txt, getattr(n, "lineno", None),
                                                                 qualname(n)))
                print("     🛑 **loud**：右式產生**新物件**、與登記表**⛔ 為同一物**")

    # ── 款 `4` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-4`　款 `4`　`(e3′)` 街角第 `1` 宗之述詞之在域可達性（處 `5`〜`7`）──")
    spb = blob(rev, "verify/stepg_pipeline.py")
    spt = ast.parse(spb.decode("utf-8"))
    annotate(spt)
    spl = lines_of(spb)
    F = []
    for n in ast.walk(spt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "_build_g_row":
            for d in ast.walk(n):
                if isinstance(d, ast.Dict):
                    for kk, vv in zip(d.keys, d.values):
                        names = {x.id for x in ast.walk(vv) if isinstance(x, ast.Name)}
                        if "_is_first_corner" in names or "_alloc_side" in names:
                            if isinstance(kk, ast.Constant):
                                F.append((kk.value, uq(vv),
                                          "_is_first_corner" if "_is_first_corner" in names
                                          else "_alloc_side"))
    print("① `𝔽` 之取得（`verify/stepg_pipeline.py` :: `_build_g_row` 之回傳 `Dict`）")
    for kk, vv, via in F:
        print("   · 鍵 `'%s'`｜值式逐字 ＝ `%s`｜經由名 `%s`" % (kk, vv, via))
    FSET = sorted({x[0] for x in F})
    print("   ⇒ `𝔽` ＝ %r" % (FSET,))

    for k in (5, 6, 7):
        if k > len(sites):
            continue
        s = sites[k - 1]
        src_b, tree, lines = trees[s["file"]]
        fn = enclosing_func(s["call"])
        print("\n### 處 `%d`　`%s` :: `%s`" % (k, s["file"], fn.name if fn else "<module>"))
        reads = []
        if fn is not None:
            for n in ast.walk(fn):
                if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) \
                        and n.slice.value in FSET:
                    reads.append((n.slice.value, uq(n), uq(n.value),
                                  getattr(n, "lineno", None)))
                elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                        and n.func.attr == "get" and n.args \
                        and isinstance(n.args[0], ast.Constant) \
                        and n.args[0].value in FSET:
                    reads.append((n.args[0].value, uq(n), uq(n.func.value),
                                  getattr(n, "lineno", None)))
        cnt = {f: 0 for f in FSET}
        for v, _e, _o, _l in reads:
            cnt[v] = cnt.get(v, 0) + 1
        print("  ② 以字面 ∈ `𝔽` 為鍵之讀取 ＝ **%d**｜逐鍵 %r" % (len(reads), cnt))
        for v, e, o, ln in reads:
            print("     · 鍵 `'%s'`｜式逐字 ＝ `%s`｜**所讀之名** ＝ `%s`｜列 `%s`" % (v, e, o, ln))
        if not reads:
            print("     🛑 **loud**：該函式內⛔ 以 `𝔽` 之任一字面為鍵之讀取")
        # 持列之名之綁定與上溯
        holders = sorted({o for _v, _e, o, _l in reads})
        idx = bind_index(fn) if fn else {}
        for h in holders:
            base = h.split("[")[0].split(".")[0].strip()
            print("     · 持列之名 `%s`（基名 `%s`）之綁定：" % (h, base))
            bs = idx.get(base, [])
            if not bs:
                print("        🛑 ⛔ 綁定（或係外部名／形參以外）")
            for kind, st, rhs in bs:
                print("        形 `%s`｜列 `%s`｜逐字 ＝ `%s`"
                      % (kind, getattr(st, "lineno", None),
                         uq(st) if kind not in ("形參", "形參(*)", "形參(**)")
                         else "（形參 of `%s`）" % fn.name))
                # 上溯鏈（深度上限 `FIELD_CAP`）
                seen, cur, d = set(), [base], 0
                while cur and d < FIELD_CAP:
                    d += 1
                    nx = []
                    for nm in cur:
                        if nm in seen:
                            continue
                        seen.add(nm)
                        for _k2, _st2, r2 in idx.get(nm, []):
                            if r2 is None:
                                continue
                            t2 = uq(r2)
                            if "run_step_g" in t2 or "g_rows" in t2:
                                print("        ⇒ 上溯命中：`%s` ＝ `%s`" % (nm, t2))
                            for sub in ast.walk(r2):
                                if isinstance(sub, ast.Name) and sub.id not in seen:
                                    nx.append(sub.id)
                    cur = nx
                if d >= FIELD_CAP:
                    print("        🛑 **loud**：上溯深度逾 `%d` ⇒ 截斷具名" % FIELD_CAP)

    # ── 款 `5` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-5`　款 `5`　處 `5` 之字面街廓（`verify/wf_f1.py` :: `compute`）──")
    f1b = blob(rev, "verify/wf_f1.py")
    f1t = ast.parse(f1b.decode("utf-8"))
    annotate(f1t)
    f1l = lines_of(f1b)
    for n in ast.walk(f1t):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "compute":
            lo, hi = n.lineno, getattr(n, "end_lineno", len(f1l))
            print("  `compute` 之區間 ＝ 列 `%d`〜`%d`" % (lo, hi))
            hit = 0
            for x in ast.walk(n):
                if isinstance(x, ast.Assign) and len(x.targets) == 1 \
                        and isinstance(x.targets[0], ast.Name) and x.targets[0].id == "lbl" \
                        and isinstance(x.value, ast.Constant):
                    hit += 1
                    print("  · 對 `lbl` 之**字面賦值**｜列 `%s`｜逐字 ＝ `%s`"
                          % (x.lineno, uq(x)))
            if hit == 0:
                print("  🛑 **判定組為空**：⛔ 對 `lbl` 之字面賦值 ⇒ loud")
            todo = [(i, f1l[i - 1].rstrip("\r")) for i in range(lo, min(hi, len(f1l)) + 1)
                    if "TODO(泛化波)" in f1l[i - 1]]
            print("  · 含 `TODO(泛化波)` 之註解列（**讀 blob 之列**）＝ **%d**" % len(todo))
            for i, t in todo:
                print("     列 `%d`｜逐字 ＝ `%s`" % (i, t))
            if not todo:
                print("     🛑 **loud**：該區間內⛔ 含該字樣之列")
    print("  🛑 **⛔ 判其當否**（單明文）")

    # ── 款 `6` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-6`　款 `6`　「第 `1` 宗／第 `2` 宗」之碼面普查──")
    print("🔒 名集 `ℕ` ＝ **%d** 名（逐字）：%r" % (len(N6), N6))
    print("🔒 框 ＝ AST 六形（`Name.id`／`Attribute.attr`／`keyword.arg`／`arg.arg`／"
          "`FunctionDef.name`／`str` 型 `Constant.value`·**整值相等**·⛔ 子字串）")
    tab6, all6, cmp6 = {}, [], {}
    for f in files:
        if f not in trees:
            sb = blob(rev, f)
            try:
                t = ast.parse(sb.decode("utf-8"))
            except SyntaxError as e:                          # noqa: BLE001
                LOUD.append("parse 失敗：%s %r" % (f, e))
                continue
            annotate(t)
            trees[f] = (sb, t, lines_of(sb))
        sb, t, ls = trees[f]
        hs = six_form_hits(t, ls, N6)
        if hs:
            tab6[f] = hs
            for h in hs:
                all6.append(dict(h, 檔=f))
        cs = idx_compares(t, ls)
        if cs:
            cmp6[f] = cs
    print("\n**逐檔逐名之計數表**")
    print("| 檔 | 命中 | 逐名 |")
    print("|---|---|---|")
    tot6 = 0
    for f in sorted(tab6):
        per = {}
        for h in tab6[f]:
            per[h["名"]] = per.get(h["名"], 0) + 1
        tot6 += len(tab6[f])
        print("| `%s` | **%d** | %s |" % (f, len(tab6[f]),
                                          ", ".join("`%s`×%d" % (k, v)
                                                    for k, v in sorted(per.items()))))
    print("\n命中之檔 ＝ **%d**｜合計 ＝ **%d**" % (len(tab6), tot6))
    print("\n**逐命中之全量**（檔, qualname, 形, 名, 該列逐字）")
    for h in all6:
        print("   | `%s` | `%s` | %s | `%s` | `%s` |"
              % (h["檔"], h["qual"], h["形"], h["名"], h["該列逐字"].strip()))
    print("\n**以整數字面 `0`／`1` 與 `_lg_idx_left`／`_lg_idx_right` 比較之式**（`Compare`·兩側任一）")
    nc = 0
    for f in sorted(cmp6):
        for c in cmp6[f]:
            nc += 1
            print("   · `%s`｜列 `%s`｜qual `%s`｜式逐字 ＝ `%s`"
                  % (f, c["列"], c["qual"], c["式逐字"]))
    if nc == 0:
        print("   🛑 **判定組為空** ⇒ loud 具名")
    print("🛑 **⛔ 判何處與 `K-9-31` 相違、⛔ 判改法**——僅出艙。")

    # ── 款 `7` ───────────────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-7`　款 `7`　`K-9-33`〜`K-9-35` 所涉之碼面所在──")
    print("🔒 名集 `ℕ′` ＝ **%d** 名（逐字）：%r" % (len(N7), N7))
    tab7, fdefs = {}, []
    for f in files:
        if f not in trees:
            continue
        sb, t, ls = trees[f]
        hs = six_form_hits(t, ls, N7)
        if hs:
            tab7[f] = hs
        for n in ast.walk(t):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in set(N7):
                fdefs.append((f, n.name, n.lineno, getattr(n, "end_lineno", None)))
    print("\n**① 逐檔逐名之命中數表**")
    print("| 檔 | 命中 | 逐名 |")
    print("|---|---|---|")
    tot7 = 0
    for f in sorted(tab7):
        per = {}
        for h in tab7[f]:
            per[h["名"]] = per.get(h["名"], 0) + 1
        tot7 += len(tab7[f])
        print("| `%s` | **%d** | %s |" % (f, len(tab7[f]),
                                          ", ".join("`%s`×%d" % (k, v)
                                                    for k, v in sorted(per.items()))))
    print("\n命中之檔 ＝ **%d**｜合計 ＝ **%d**" % (len(tab7), tot7))
    print("\n**② `ℕ′` 中為 `FunctionDef` 者之 (檔, 起迄列)** ＝ **%d**" % len(fdefs))
    for f, nm, lo, hi in fdefs:
        print("   · `%s`｜`%s`｜列 `%s`〜`%s`" % (f, nm, lo, hi))

    print("\n**③ `app.py` :: `_build_corner_range_v3` 之函式區間內**")
    for n in ast.walk(apt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and n.name == "_build_corner_range_v3":
            lo, hi = n.lineno, getattr(n, "end_lineno", len(apl))
            emb = sum(1 for x in ast.walk(n)
                      if isinstance(x, ast.Name) and x.id == "eff_min_build")
            seg_lines = apl[lo - 1:hi]
            lit = sum(s.count("最小建築面積") for s in seg_lines)
            tstr = "T = float(setback or 0.0) + float(min_width or 0.0)"
            tcnt = sum(s.count(tstr) for s in seg_lines)
            print("   區間 ＝ 列 `%d`〜`%d`" % (lo, hi))
            print("   · 名 `eff_min_build` 之 AST 命中 ＝ **%d**" % emb)
            print("   · 字面 `最小建築面積` 之命中（**讀 blob 之列**·含註解）＝ **%d**" % lit)
            print("   · 字樣 `%s` 之命中 ＝ **%d**" % (tstr, tcnt))

    print("\n**④ `app.py` :: `_lot_gate` 之回傳 `Dict` 之鍵逐字（全量）及各鍵之值式逐字**")
    for n in ast.walk(apt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "_lot_gate":
            rets = [x for x in ast.walk(n) if isinstance(x, ast.Return)]
            print("   `Return` ＝ %d 處" % len(rets))
            nk = 0
            for r in rets:
                if isinstance(r.value, ast.Dict):
                    for kk, vv in zip(r.value.keys, r.value.values):
                        nk += 1
                        print("   · 鍵 `%s`｜值式逐字 ＝ `%s`"
                              % (uq(kk) if kk is not None else "**", uq(vv)))
            print("   ⇒ 鍵數 ＝ **%d**（🛑 **⛔ 判**）" % nk)

    print("\n**⑤ `verify/wf_f4.py` :: `_reshape_block` 內 `_end_gate` 與 `_area_rend` 之"
          "賦值語句與比較語句逐字**")
    f4b = blob(rev, "verify/wf_f4.py")
    f4t = ast.parse(f4b.decode("utf-8"))
    annotate(f4t)
    f4l = lines_of(f4b)
    for n in ast.walk(f4t):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "_reshape_block":
            for x in ast.walk(n):
                if isinstance(x, ast.Assign):
                    tn = {y.id for y in ast.walk(x.targets[0]) if isinstance(y, ast.Name)}
                    if tn & {"_end_gate", "_area_rend"}:
                        print("   · **賦值**｜列 `%s`｜逐字 ＝ `%s`" % (x.lineno, uq(x)))
                if isinstance(x, ast.Compare):
                    t2 = uq(x)
                    if "_end_gate" in t2 or "_area_rend" in t2:
                        print("   · **比較**｜列 `%s`｜逐字 ＝ `%s`" % (x.lineno, t2))

    print("\n**⑥ `verify/run_verification.py` 內含字樣 `因 F.0 raise 而` 之列逐字**"
          "（**讀 blob 之列**）")
    n6c = 0
    for i, s in enumerate(rvl, 1):
        if "因 F.0 raise 而" in s:
            n6c += 1
            print("   列 `%d`｜逐字 ＝ `%s`" % (i, s.rstrip("\r")))
    if n6c == 0:
        print("   🛑 **判定組為空** ⇒ loud 具名")
    print("🛑 **⛔ 判改法**（單明文）")

    # ── 款 `8`　判別力造 ───────────────────────────────────────────
    print("\n" + BAR)
    print("── `§五-8`　款 `8`　判別力造──")
    res = []
    res.append(("[必為 `7`] 款 `1`〜`2` 之母體", len(sites), 7, len(sites) == 7))
    ok_F = (FSET == ["推進側別", "第1筆街角"] or sorted(FSET) == sorted(["第1筆街角", "推進側別"]))
    res.append(("[必命中甲] 款 `4` ① 之 `𝔽`", FSET, ["第1筆街角", "推進側別"], ok_F))
    bp_hit = 0
    for n in ast.walk(rvt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "build_pipeline":
            bp_hit = sum(1 for x in ast.walk(n)
                         if isinstance(x, ast.Constant) and x.value == SLBS)
    res.append(("[必命中乙] 款 `3` ③ 字面 `%s` 於 `build_pipeline` 內" % SLBS,
                bp_hit, ">= 1", bp_hit >= 1))
    # [必為零]：以執行期組出之人造欄名替 `𝔽` 重跑款 `4` ②
    fake_col = "第" + str(9 * 100 + 9 * 10 + 7) + "筆" + chr(0x8857) + chr(0x89D2)
    zero = 0
    for k in (5, 6, 7):
        if k > len(sites):
            continue
        fn = enclosing_func(sites[k - 1]["call"])
        if fn is None:
            continue
        for n in ast.walk(fn):
            if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant) \
                    and n.slice.value == fake_col:
                zero += 1
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.func.attr == "get" and n.args \
                    and isinstance(n.args[0], ast.Constant) and n.args[0].value == fake_col:
                zero += 1
    res.append(("[必為零] 人造欄名（**執行期組出**）替 `𝔽` 重跑款 `4` ②", zero, 0, zero == 0))
    sp_hit = len(six_form_hits(spt, spl, N6))
    res.append(("[必命中丙] 款 `6` 之框於 `verify/stepg_pipeline.py`", sp_hit, "> 0", sp_hit > 0))
    fake_n = "_" + chr(0x69) + "s_first_corner_" + str(9 * 100 + 9 * 10 + 7)
    zero2 = 0
    for f in files:
        if f not in trees:
            continue
        _sb, t, ls = trees[f]
        zero2 += len(six_form_hits(t, ls, [fake_n]))
    res.append(("[必為零乙] 人造名（**執行期組出**）替 `ℕ` 重跑款 `6`", zero2, 0, zero2 == 0))
    d_hit = sum(1 for n in ast.walk(apt)
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                and n.name == "_build_corner_range_v3")
    res.append(("[必命中丁] 款 `7` 之框於 `app.py` 之 `FunctionDef` 名 `_build_corner_range_v3`",
                d_hit, 1, d_hit == 1))
    fake_n2 = "_build_corner_range_v" + str(9 * 100 + 9 * 10 + 7)
    zero3 = 0
    for f in files:
        if f not in trees:
            continue
        _sb, t, ls = trees[f]
        zero3 += len(six_form_hits(t, ls, [fake_n2]))
    res.append(("[必為零丙] 人造名（**執行期組出**）替 `ℕ′` 重跑款 `7` ①", zero3, 0, zero3 == 0))

    print("| 造 | 實得 | 期 | 判 |")
    print("|---|---|---|---|")
    for nm, got, exp, ok in res:
        print("| %s | `%r` | `%r` | %s |" % (nm, got, exp, "✅" if ok else "🔴"))

    stop13 = (len(sites) != 7) or (not ok_F) or (bp_hit < 1) or (sp_hit <= 0) or (d_hit != 1)
    print("\n**停十三**（`S` ≠ `7`，或 [必命中甲]／[必命中乙]／[必命中丙]／[必命中丁] 不中）⇒ %s"
          % ("🔴 **成就 ⇒ 停、上呈**" if stop13 else "✅ **不成就**"))

    print("\n── 🛑 loud 之全量 ──")
    if not LOUD:
        print("   （無記錄）**⛔ 讀為「無異常」**")
    for m in sorted(set(LOUD)):
        print("   - %s   ×%d" % (m, LOUD.count(m)))

    print("\n" + BAR)
    print("【本器⛔ 判改法·⛔ 判可施與否·⛔ 擬任何 diff·⛔ 開分支·⛔ 動用 KL 之放行】")
    print(BAR)


main()

_here = os.path.dirname(os.path.abspath(__file__))
_dst = os.path.join(os.path.dirname(_here), "out", "WG9308R_sites2.log")
_data = _BUF.getvalue().encode("utf-8")
with open(_dst, "wb") as _fh:
    _fh.write(_data)
sys.stdout = _REAL
print("\n落檔 ＝ `verify/out/WG9308R_sites2.log`｜%d B｜`sha256` %s｜`CR` %d"
      % (len(_data), hashlib.sha256(_data).hexdigest(), _data.count(b"\r")))
