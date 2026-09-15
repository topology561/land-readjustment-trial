"""`W-G.9-303`　`§三` 工項一 ＋ `§四` 款 `1`／`2`／`5` 之**靜態**量測器（唯讀·零生產碼）。

🔒 **本器⛔ 改生產碼一字**、⛔ 動任何既有探針、⛔ 自寫第二套幾何——只讀 AST 與文字層。
🔒 母體一律以**產生指令**界定（`自誤 406`）：
    生產碼 `34` 檔 ＝ `git ls-tree HEAD --name-only verify/` ⋂ `*.py`（**非遞迴**）＋ `app.py`。
🔒 **框之四形分列**（款 `1`）：`Subscript`／`Assign`／`.get`／`Dict`-`DictComp`
    ——⛔ 沿用 `W-G.9-302R` 已具名其對 `ast.Dict` 鍵字面有盲區之三形框。
🔒 判別力之[必為零]造，其字樣一律**執行期組出**，字面⛔ 落入任何 log（`GB-147`）。

用法：python verify/probes/probe_WG9303R6_static.py
"""
import ast
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

KEY = "side_lines_by_side"
SS_KEY = "f3_cad_side_lines_by_side"
TARGET_FN = "_corner_buffer_S"
K2_WORDS = ["blk", "label", "lbl", "block_id"]          # 🔒 四字樣·分列並報·⛔ 合併
GEOM_WORDS = ["block_poly", "poly", "geom"]
K4_WORDS = ["corner", "first", "_fc"]                   # `§四` 款 `2` 之三字樣


def sh(args):
    cp = subprocess.run(args, capture_output=True, cwd=REPO)
    return cp.stdout, cp.returncode


def sentinel(tag):
    """執行期組出之人造字樣（字面⛔ 出艙）。"""
    return "Z" + chr(0x5A) + tag + str(os.getpid()) + chr(0x5F) + "NOSUCH"


# ── 母體（產生指令界定）──────────────────────────────────────────
out, _ = sh(["git", "ls-tree", "HEAD", "--name-only", "verify/"])
top = [x for x in out.decode("utf-8", "surrogateescape").splitlines()
       if x.endswith(".py")]
FILES = ["app.py"] + sorted(top)
SRC = {}
TREE = {}
for f in FILES:
    b, rc = sh(["git", "cat-file", "blob", "HEAD:" + f])
    assert rc == 0, f
    SRC[f] = b.decode("utf-8")
    TREE[f] = ast.parse(SRC[f], filename=f)

BAR = "=" * 116


def seg(t):
    print("\n" + BAR)
    print(t)
    print(BAR)


print(BAR)
print("【`W-G.9-303` `§三`／`§四` 靜態量測器】")
print(BAR)
print("母體之產生指令 = git ls-tree HEAD --name-only verify/ | grep '\\.py$'   ＋ app.py")
print("母體基數 = %d 檔（外部錨 ＝ `§零` 閘 `7` 之 `34`）⇒ 相符 = %s"
      % (len(FILES), len(FILES) == 34))


# ── 共用：函式歸屬（`檔 :: 函式`）─────────────────────────────────
def owner_map(tree):
    """回 {node: 函式限定名}；頂層者為 '<module>'。"""
    m = {}

    def walk(n, q):
        for ch in ast.iter_child_nodes(n):
            if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)):
                nq = q + [ch.name]
                m[id(ch)] = "::".join(q) if q else "<module>"
                walk(ch, nq)
            elif isinstance(ch, ast.ClassDef):
                walk(ch, q + [ch.name])
            else:
                m[id(ch)] = "::".join(q) if q else "<module>"
                walk(ch, q)
    walk(tree, [])
    return m


OWN = {}
for f in FILES:
    o = {}

    def walk(n, q, o=o):
        for ch in ast.iter_child_nodes(n):
            nq = q
            if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                nq = q + [ch.name]
            o[id(ch)] = "::".join(q) if q else "<module>"
            walk(ch, nq)
    walk(TREE[f], [])
    OWN[f] = o


def own(f, node):
    return OWN[f].get(id(node), "?")


def src_line(f, node):
    return SRC[f].splitlines()[node.lineno - 1].strip()


# ══════════════════════════════════════════════════════════════════
# `§三` 款 `1`：層① 之鍵之**寫入端**——四形分列
# ══════════════════════════════════════════════════════════════════
seg("`§三` 款 `1`　`%s` 之**寫入端**與層① 鍵之源頭（**四形分列**·⛔ 三形盲框）" % SS_KEY)

forms = {"Subscript": [], "Assign": [], ".get": [], "Dict/DictComp": []}
for f in FILES:
    for node in ast.walk(TREE[f]):
        # 形① Subscript（Store）：X['<key>'] = ...
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if (isinstance(tgt, ast.Subscript)
                        and isinstance(tgt.slice, ast.Constant)
                        and tgt.slice.value in (KEY, SS_KEY)):
                    forms["Subscript"].append((f, node, tgt.slice.value))
            # 形② Assign 至裸名
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in (KEY, SS_KEY):
                    forms["Assign"].append((f, node, tgt.id))
        # 形③ .get('<key>' ...)
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args
                and isinstance(node.args[0], ast.Constant)
                and node.args[0].value in (KEY, SS_KEY)):
            forms[".get"].append((f, node, node.args[0].value))
        # 形④ Dict 鍵字面 ／ DictComp
        if isinstance(node, ast.Dict):
            for k in node.keys:
                if isinstance(k, ast.Constant) and k.value in (KEY, SS_KEY):
                    forms["Dict/DictComp"].append((f, node, k.value))
        if isinstance(node, ast.DictComp):
            forms["Dict/DictComp"].append((f, node, "<DictComp>"))

for nm in ("Subscript", "Assign", ".get", "Dict/DictComp"):
    rows = forms[nm]
    if nm == "Dict/DictComp":
        rows = [r for r in rows if r[2] != "<DictComp>"]
    print("\n── 形 `%s` ⇒ %d 處 ──" % (nm, len(rows)))
    if not rows:
        print("   🛑 **loud**：該形於母體內**無命中**（母體基數 = %d 檔）" % len(FILES))
    for f, node, k in rows:
        print("   %s :: %s   鍵 = %r" % (f, own(f, node), k))
        print("       逐字 = %s" % src_line(f, node))

# 層① 鍵之源頭：追 `side_lines_by_side` 之建構處（其 value 之 Subscript-Store 鍵）
seg("`§三` 款 `1`（續）　層① 鍵之**源頭之名**（逐層溯至產生式）")
for f in FILES:
    for node in ast.walk(TREE[f]):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if (isinstance(tgt, ast.Subscript)
                        and isinstance(tgt.value, ast.Name)
                        and tgt.value.id in ("side_lines_by_side", "slbs", "sl_by_side")):
                    print("   %s :: %s" % (f, own(f, node)))
                    print("       逐字 = %s" % src_line(f, node))
                    print("       層① 鍵之 AST = %s" % ast.dump(tgt.slice)[:160])


# ══════════════════════════════════════════════════════════════════
# `§三` 款 `2`：`_corner_buffer_S` 體內可解之名中語義為「街廓識別」者
# ══════════════════════════════════════════════════════════════════
seg("`§三` 款 `2`　母體 ＝ `ns` 全部鍵（`app.py` 之 `t.body` 頂層名）＋ `%s` 之八形參" % TARGET_FN)

ns_keys = []
for st in TREE["app.py"].body:                       # 🔒 頂層全域取 `t.body`
    if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        ns_keys.append(st.name)
    elif isinstance(st, ast.Assign):
        for tg in st.targets:
            for nd in ast.walk(tg):
                if isinstance(nd, ast.Name):
                    ns_keys.append(nd.id)
    elif isinstance(st, ast.AnnAssign) and isinstance(st.target, ast.Name):
        ns_keys.append(st.target.id)
    elif isinstance(st, (ast.Import, ast.ImportFrom)):
        for al in st.names:
            ns_keys.append(al.asname or al.name.split(".")[0])
ns_keys = sorted(set(ns_keys))
print("`ns` 鍵基數 = %d（產生指令 ＝ ast.parse(app.py).body 之頂層定義名）" % len(ns_keys))

fn = None
for node in ast.walk(TREE["app.py"]):
    if isinstance(node, ast.FunctionDef) and node.name == TARGET_FN:
        fn = node
params = [a.arg for a in fn.args.args] + [a.arg for a in fn.args.kwonlyargs]
print("`%s` 之形參（%d 個·逐名）= %s" % (TARGET_FN, len(params), params))

POP = sorted(set(ns_keys) | set(params))
print("款 `2` 之母體基數 = %d（`ns` 鍵 %d ∪ 形參 %d）" % (len(POP), len(ns_keys), len(params)))
for w in K2_WORDS:
    hit = [x for x in POP if w in x]
    print("\n── 字樣 `%s` ⇒ 命中 %d（**全量逐名**·⛔ 只報基數）──" % (w, len(hit)))
    if not hit:
        print("   🛑 **loud**：無命中；母體基數 = %d" % len(POP))
    for x in hit:
        kind = "形參" if x in params else "頂層名"
        extra = ""
        if x in params:
            extra = "（`%s` 之第 %d 形參）" % (TARGET_FN, params.index(x) + 1)
        else:
            for st in TREE["app.py"].body:
                if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef)) and st.name == x:
                    extra = "（頂層 `def`·逐字 = %s）" % src_line("app.py", st)[:90]
                    break
                if isinstance(st, ast.Assign) and any(
                        isinstance(n, ast.Name) and n.id == x for tg in st.targets
                        for n in ast.walk(tg)):
                    extra = "（頂層 `Assign`·逐字 = %s）" % src_line("app.py", st)[:90]
                    break
                if isinstance(st, (ast.Import, ast.ImportFrom)) and extra == "":
                    for al in st.names:
                        if (al.asname or al.name.split(".")[0]) == x:
                            extra = "（`import`·逐字 = %s）" % src_line("app.py", st)[:90]
                            break
        print("   - `%s`  [%s] %s" % (x, kind, extra))

s2 = sentinel("k2")
print("\n判別力[必為零]（字樣**執行期組出**·字面⛔ 出艙）⇒ 命中 %d（須 0）⇒ %s"
      % (len([x for x in POP if s2 in x]), "✅" if not [x for x in POP if s2 in x] else "🔴"))
print("判別力[必非零] `ns` 鍵基數 = %d（須 ≥ 1）⇒ %s"
      % (len(ns_keys), "✅" if len(ns_keys) >= 1 else "🔴"))


# ══════════════════════════════════════════════════════════════════
# `§三` 款 `3`：`_label` 實參之溯源
# ══════════════════════════════════════════════════════════════════
seg("`§三` 款 `3`　`%s` 各呼叫點之 `_label` 實參**逐處溯源**（⛔ 以名同判物同）" % TARGET_FN)


def enclosing_fn(tree, lineno):
    best = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            end = getattr(node, "end_lineno", node.lineno)
            if node.lineno <= lineno <= end:
                if best is None or node.lineno > best.lineno:
                    best = node
    return best


calls = []
for f in FILES:
    for node in ast.walk(TREE[f]):
        if isinstance(node, ast.Call):
            nm = (node.func.id if isinstance(node.func, ast.Name)
                  else node.func.attr if isinstance(node.func, ast.Attribute) else None)
            sub = None
            if (isinstance(node.func, ast.Subscript)
                    and isinstance(node.func.slice, ast.Constant)):
                sub = node.func.slice.value                 # ns["_corner_buffer_S"](…)
            if nm == TARGET_FN or sub == TARGET_FN:
                calls.append((f, node))
print("呼叫點總數（`Name` ∪ `Attribute` ∪ `ns[<字面>]` 三形並取）= %d" % len(calls))
for f, node in calls:
    lab = None
    for kw in node.keywords:
        if kw.arg == "_label":
            lab = kw.value
    pos = node.args[7] if len(node.args) > 7 else None
    expr = lab if lab is not None else pos
    print("\n   ● %s :: %s   （呼叫列逐字）" % (f, own(f, node)))
    print("       %s" % src_line(f, node))
    if expr is None:
        print("       `_label` ⇒ **未傳**（取預設 `''`）")
        continue
    txt = ast.get_source_segment(SRC[f], expr) or ast.dump(expr)
    print("       `_label` 實參逐字 = %s" % txt)
    names = sorted({n.id for n in ast.walk(expr) if isinstance(n, ast.Name)})
    print("       其所含之名 = %s" % names)
    host = enclosing_fn(TREE[f], node.lineno)
    hname = host.name if host else "<module>"
    for nm2 in names:
        stores = []
        scope = host if host else TREE[f]
        for nd in ast.walk(scope):
            if isinstance(nd, ast.Assign):
                for tg in nd.targets:
                    for x in ast.walk(tg):
                        if isinstance(x, ast.Name) and x.id == nm2 and isinstance(x.ctx, ast.Store):
                            stores.append(("Assign", nd))
            elif isinstance(nd, (ast.For, ast.AsyncFor)):
                for x in ast.walk(nd.target):
                    if isinstance(x, ast.Name) and x.id == nm2:
                        stores.append(("For.target", nd))
            elif isinstance(nd, (ast.FunctionDef, ast.AsyncFunctionDef)) and nd is scope:
                for a in nd.args.args + nd.args.kwonlyargs:
                    if a.arg == nm2:
                        stores.append(("形參", nd))
        print("       └ `%s` 於 `%s` 內之賦值來源 ⇒ %d 處" % (nm2, hname, len(stores)))
        if not stores:
            print("           🛑 **loud：⛔ 可判**（該名於本函式內無 `Store`·可能為外層閉包或全域）")
        for kind, nd in stores[:6]:
            print("           [%s] %s" % (kind, src_line(f, nd)[:110]))


# ══════════════════════════════════════════════════════════════════
# `§三` 款 `4`：既有之「幾何 → 街廓識別」映射之全量
# ══════════════════════════════════════════════════════════════════
seg("`§三` 款 `4`　既有之「幾何 → 街廓識別」映射（**全量**·⛔ 自寫第二套幾何）")

found = []
for st in TREE["app.py"].body:
    if not isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef)):
        continue
    ps = [a.arg for a in st.args.args] + [a.arg for a in st.args.kwonlyargs]
    if not any(any(g in p for g in GEOM_WORDS) for p in ps):
        continue
    rets = []
    for nd in ast.walk(st):
        if isinstance(nd, ast.Return) and nd.value is not None:
            t = ast.get_source_segment(SRC["app.py"], nd.value) or ""
            if any(w in t for w in K2_WORDS):
                rets.append((nd, t))
    if rets:
        found.append((st, ps, rets))
print("母體 ＝ `ns` 全部鍵（基數 %d）；框 ＝ 形參含 %s ⋀ `Return` 值含 %s"
      % (len(ns_keys), GEOM_WORDS, K2_WORDS))
print("命中 = %d" % len(found))
if not found:
    print("🛑 **loud：母體內無此映射**（母體基數 = %d）" % len(ns_keys))
for st, ps, rets in found:
    print("\n   ● `%s`   形參 = %s" % (st.name, ps))
    for nd, t in rets[:6]:
        print("       Return 逐字 = %s" % t[:130])


# ══════════════════════════════════════════════════════════════════
# `§四` 款 `1`：`is_corner` 之定義與求值來源
# ══════════════════════════════════════════════════════════════════
seg("`§四` 款 `1`　`is_corner` 之 `Store`／`Load` **二形分列** ＋ 文字層列框對照")

stores, loads = [], []
for f in FILES:
    for nd in ast.walk(TREE[f]):
        if isinstance(nd, ast.Name) and nd.id == "is_corner":
            (stores if isinstance(nd.ctx, ast.Store) else loads).append((f, nd))
        if isinstance(nd, ast.arg) and nd.arg == "is_corner":
            stores.append((f, nd))
        if isinstance(nd, ast.Attribute) and nd.attr == "is_corner":
            loads.append((f, nd))
        if (isinstance(nd, ast.Constant) and isinstance(nd.value, str)
                and nd.value == "is_corner"):
            loads.append((f, nd))
print("AST `Store`（含形參）= %d 處" % len(stores))
print("AST `Load`（含 `Attribute`／字面鍵）= %d 處" % len(loads))
txt_hits = {}
tot = 0
for f in FILES:
    c = len([1 for ln in SRC[f].splitlines() if "is_corner" in ln])
    if c:
        txt_hits[f] = c
        tot += c
print("文字層**列框** = %d 列（逐檔：%s）" % (tot, txt_hits))
print("🛑 二數相異之成因：AST 數以**出現節點**計（一列可含多個），文字層以**列**計 ⇒ 口徑不同，⛔ 應相等")

print("\n── `Store` 之全量（`檔 :: 函式` ＋ 賦值產生式逐字）──")
for f, nd in stores:
    line = SRC[f].splitlines()[nd.lineno - 1].strip()
    print("   %s :: %s" % (f, own(f, nd) if not isinstance(nd, ast.arg) else "(形參)"))
    print("       逐字 = %s" % line[:150])

s4 = sentinel("k41")
print("\n判別力[必為零]（人造名·執行期組出）⇒ AST 命中 %d（須 0）"
      % len([1 for f in FILES for nd in ast.walk(TREE[f])
             if isinstance(nd, ast.Name) and nd.id == s4]))
print("判別力[必非零] `Store` 處數 = %d（須 ≥ 1）" % len(stores))


# ══════════════════════════════════════════════════════════════════
# `§四` 款 `2`：「街角第 1 宗」判準之載體
# ══════════════════════════════════════════════════════════════════
seg("`§四` 款 `2`　`corner`／`first`／`_fc` **三字樣分列** 之 `FunctionDef`／頂層 `Assign`")

for w in K4_WORDS:
    fns, asg = [], []
    for f in FILES:
        for st in TREE[f].body:
            if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef)) and w in st.name:
                fns.append((f, st.name))
            if isinstance(st, ast.Assign):
                for tg in st.targets:
                    for nd in ast.walk(tg):
                        if isinstance(nd, ast.Name) and w in nd.id:
                            asg.append((f, nd.id, src_line(f, st)[:100]))
    print("\n── 字樣 `%s` ⇒ `FunctionDef` %d ／ 頂層 `Assign` %d（**全量**）──"
          % (w, len(fns), len(asg)))
    if not fns and not asg:
        print("   🛑 **loud**：無命中（母體 = %d 檔）" % len(FILES))
    for f, n in fns:
        print("   [def] %s :: %s" % (f, n))
    for f, n, t in asg:
        print("   [assign] %s :: %s   逐字 = %s" % (f, n, t))


# ══════════════════════════════════════════════════════════════════
# 判別力四造（`§三` 款 `5` ／ `§四` 款 `5`）
# ══════════════════════════════════════════════════════════════════
seg("判別力四造（`§三` 款 `5` ／ `§四` 款 `5`）")
print("[必為 `34`] 生產碼母體基數 = %d ⇒ %s" % (len(FILES), "✅" if len(FILES) == 34 else "🔴"))
print("[必非零] `ns` 鍵基數 = %d ⇒ %s" % (len(ns_keys), "✅" if ns_keys else "🔴"))
s5 = sentinel("k5")
print("[必為零] 人造字樣於款 `2` 之框下命中 = %d ⇒ %s"
      % (len([x for x in POP if s5 in x]), "✅" if not [x for x in POP if s5 in x] else "🔴"))
print("[必真] `st` 在 `ns` 之鍵 = %s ⇒ %s"
      % ("st" in ns_keys, "✅" if "st" in ns_keys else "🔴"))
print("[必相異] `§四` 款 `1` 之 AST 數（Store %d ＋ Load %d ＝ %d）與文字層列框 %d ⇒ 相異 = %s"
      % (len(stores), len(loads), len(stores) + len(loads), tot,
         (len(stores) + len(loads)) != tot))
print("\n" + BAR)
print("【本器⛔ 判「可信／不可信」·⛔ 擬任何改法或 diff】")
print(BAR)
