# -*- coding: utf-8 -*-
"""W-G.9-308 補令一 工項四：強制呼叫與側界名之綁定次序之靜態全證（零生產碼·零 harness）。

受詞：生產碼 34 檔（HEAD 之 verify/ 頂層 *.py 與 app.py·正面列舉）內，
      對 _corner_buffer_S 之每一呼叫（語法形二：Name 形 與 ns 下標形）。
對每一呼叫，取其最內層之迴圈（For／While·同一函式內），於該迴圈體內：
  (一) 名集 N7 之七名，各出艙其迴圈體內首次 Store 之列、及首次 Store 之前之 Load（含巢狀定義內）；
  (二) 通則：迴圈體內「首次 Store 在呼叫列之後、而於呼叫列（含）之前有 Load」之名 ⇒ 期 0；
  (三) 該呼叫之引數所含之 Name，其迴圈體內首次 Store 在呼叫列之後者 ⇒ 期 0。
判別力二造（執行期組出之來源字串·不落檔）：[必命中] 讀前於綁 ⇒ (二) >= 1；[必為零] 綁前於讀 ⇒ (二) = 0。
用法：python verify/probes/probe_WG9308S1_bindorder.py <rev>
落檔：verify/out/WG9308S1_bindorder.log（open(p,'wb')·utf-8·LF）。
"""
import ast
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out", "WG9308S1_bindorder.log")
TARGET = "_corner_buffer_S"
N7 = ("_side_lines_blk", "_sl_left", "_sl_right", "_side_mid_left",
      "_side_mid_right", "_has_left_corner", "_has_right_corner")
LINES = []


def emit(s=""):
    LINES.append(s)


def git_bytes(*args):
    r = subprocess.run(["git", "-C", REPO] + list(args), capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git %r rc=%d %r" % (args, r.returncode, r.stderr[:200]))
    return r.stdout


def population(rev):
    raw = git_bytes("ls-tree", "--name-only", "-z", rev, "verify/")
    names = [x.decode("utf-8") for x in raw.split(b"\0") if x]
    top = sorted(n for n in names if n.endswith(".py") and n.count("/") == 1)
    raw2 = git_bytes("ls-tree", "-r", "--name-only", "-z", rev, "verify/")
    sub = [x for x in raw2.split(b"\0") if x and x.endswith(b".py") and x.count(b"/") >= 2]
    return top + ["app.py"], len(sub)


def is_target_call(node):
    if not isinstance(node, ast.Call):
        return None
    f = node.func
    if isinstance(f, ast.Name) and f.id == TARGET:
        return "Name"
    if isinstance(f, ast.Subscript):
        sl = f.slice
        if isinstance(sl, ast.Constant) and sl.value == TARGET:
            return "Subscript"
    return None


def parents_map(tree):
    par = {}
    for p in ast.walk(tree):
        for c in ast.iter_child_nodes(p):
            par[c] = p
    return par


def innermost_loop(node, par):
    cur = par.get(node)
    while cur is not None:
        if isinstance(cur, (ast.For, ast.AsyncFor, ast.While)):
            return cur
        if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            return None
        cur = par.get(cur)
    return None


def _target_names(t):
    return [m.id for m in ast.walk(t) if isinstance(m, ast.Name)]


def body_events(loop):
    """迴圈體之 Name 事件。🔒 語義：迴圈目標之名視為於迴圈列 Store；
    推導式（List/Set/Dict/GeneratorExp）之目標名屬其自身作用域 ⇒ 其 Store 與對之 Load 皆⛔ 計；
    巢狀 def／lambda／class 內之 Store 屬其自身作用域 ⇒ ⛔ 計，其 Load 保守計入。"""
    ev = []
    if isinstance(loop, (ast.For, ast.AsyncFor)):
        for nm in _target_names(loop.target):
            ev.append((loop.lineno, -1, "Store", nm))

    def visit(node, comp_bound, nested):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            bound = set(comp_bound)
            for g in node.generators:
                visit(g.iter, bound, nested)
                bound |= set(_target_names(g.target))
                for cond in g.ifs:
                    visit(cond, bound, nested)
            elts = [node.key, node.value] if isinstance(node, ast.DictComp) else [node.elt]
            for e in elts:
                visit(e, bound, nested)
            return
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            for c in ast.iter_child_nodes(node):
                visit(c, comp_bound, True)
            return
        if isinstance(node, ast.Name):
            if node.id in comp_bound:
                return
            k = type(node.ctx).__name__
            if k == "Store" and nested:
                return
            ev.append((node.lineno, node.col_offset, k, node.id))
            return
        for c in ast.iter_child_nodes(node):
            visit(c, comp_bound, nested)

    for stmt in loop.body + loop.orelse:
        visit(stmt, frozenset(), False)
    ev.sort()
    return ev


def analyse(src, fname):
    tree = ast.parse(src)
    par = parents_map(tree)
    rows = []
    for n in ast.walk(tree):
        form = is_target_call(n)
        if not form:
            continue
        loop = innermost_loop(n, par)
        row = {"file": fname, "line": n.lineno, "form": form,
               "loop": None, "n7": {}, "general": [], "args_stale": []}
        if loop is None:
            rows.append(row)
            continue
        row["loop"] = (type(loop).__name__, loop.lineno, loop.end_lineno)
        ev = body_events(loop)
        first_store = {}
        for ln, col, k, nm in ev:
            if k == "Store" and nm not in first_store:
                first_store[nm] = ln
        for nm in N7:
            fs = first_store.get(nm)
            early = [ln for ln, col, k, x in ev if x == nm and k == "Load" and (fs is None or ln < fs)]
            row["n7"][nm] = (fs, early)
        cl = n.lineno
        gen = set()
        for ln, col, k, nm in ev:
            fs = first_store.get(nm)
            if k == "Load" and fs is not None and fs > cl and ln <= cl:
                gen.add(nm)
        row["general"] = sorted(gen)
        argnames = set()
        for a in list(n.args) + [kw.value for kw in n.keywords]:
            for m in ast.walk(a):
                if isinstance(m, ast.Name):
                    argnames.add(m.id)
        row["args_stale"] = sorted(x for x in argnames
                                   if first_store.get(x) is not None and first_store[x] > cl)
        rows.append(row)
    return rows


def selftest():
    q = chr(39)
    hit = "\n".join([
        "def f(ns, blocks):",
        "    for b in blocks:",
        "        x = _side_mid_left",
        "        _corner_buffer_S(b, x)",
        "        _side_mid_left = ns.get(" + q + "m" + q + ")",
    ])
    zero = "\n".join([
        "def f(ns, blocks):",
        "    for b in blocks:",
        "        _side_mid_left = ns.get(" + q + "m" + q + ")",
        "        _corner_buffer_S(b, _side_mid_left)",
    ])
    zero2 = "\n".join([
        "def f(ns, blocks):",
        "    for b, c in blocks:",
        "        y = c + 1",
        "        _corner_buffer_S(b, y)",
        "        z = [c for c in range(3)]",
    ])
    rz2 = analyse(zero2, "<selftest-zero2>")
    rh = analyse(hit, "<selftest-hit>")
    rz = analyse(zero, "<selftest-zero>")
    gh = sum(len(r["general"]) for r in rh)
    gz = sum(len(r["general"]) for r in rz)
    gz += sum(len(r["general"]) for r in rz2)
    return gh, gz, len(rh), len(rz) + len(rz2)


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    full = git_bytes("rev-parse", rev).decode().strip()
    emit("=" * 100)
    emit("【W-G.9-308 補令一 工項四】強制呼叫與側界名之綁定次序（靜態·rev=%s）" % full)
    emit("=" * 100)
    gh, gz, nh, nz = selftest()
    emit("判別力二造：[必命中] 通則命中 %d（呼叫數 %d）｜[必為零] 通則命中 %d（呼叫數 %d）" % (gh, nh, gz, nz))
    ok_self = (gh >= 1 and gz == 0 and nh == 1 and nz == 2)
    emit("⇒ 器 %s" % ("非紅 ✅" if ok_self else "紅 🔴（停）"))
    files, subcount = population(full)
    emit("母體：生產碼 %d 檔（verify/ 頂層 *.py %d ＋ app.py）｜判別力[必不命中] 子層 *.py = %d"
         % (len(files), len(files) - 1, subcount))
    allrows = []
    for fn in files:
        src = git_bytes("show", "%s:%s" % (full, fn)).decode("utf-8")
        allrows.extend(analyse(src, fn))
    emit("呼叫總數 = %d（Name 形 %d／Subscript 形 %d）" % (
        len(allrows), sum(r["form"] == "Name" for r in allrows),
        sum(r["form"] == "Subscript" for r in allrows)))
    emit("")
    emit("| # | 檔:列 | 形 | 最內層迴圈 | 通則命中 | 引數含後綁之名 |")
    emit("|---|---|---|---|---|---|")
    for i, r in enumerate(allrows, 1):
        emit("| %d | %s:%d | %s | %s | %s | %s |" % (
            i, r["file"], r["line"], r["form"],
            ("%s %d-%d" % r["loop"]) if r["loop"] else "無",
            r["general"] or "[]", r["args_stale"] or "[]"))
    emit("")
    emit("名集 N7 之逐呼叫明細（首次 Store 列／首次 Store 前之 Load 列）")
    for i, r in enumerate(allrows, 1):
        if not r["loop"]:
            continue
        emit("  #%d %s:%d" % (i, r["file"], r["line"]))
        for nm in N7:
            fs, early = r["n7"][nm]
            emit("     %-20s Store@%s  前置Load=%s" % (nm, fs, early))
    gen_total = sum(len(r["general"]) for r in allrows)
    stale_total = sum(len(r["args_stale"]) for r in allrows)
    early_total = sum(len(r["n7"][nm][1]) for r in allrows if r["loop"] for nm in N7)
    emit("")
    emit("彙總：通則命中合計 = %d｜引數含後綁之名合計 = %d｜N7 首次 Store 前之 Load 合計 = %d"
         % (gen_total, stale_total, early_total))
    red = (not ok_self) or subcount <= 0 or len(allrows) == 0
    emit("器紅 = %s" % red)
    data = ("\n".join(LINES) + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as fh:
        fh.write(data)
    sys.stdout.buffer.write(data)
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
