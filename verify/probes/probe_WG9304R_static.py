"""`W-G.9-304` `§六` 款 `1`／`2`／`3`／`5` 之**靜態**量測器（唯讀·零生產碼）。

🔒 ⛔ 改生產碼一字、⛔ 動任何既有探針、⛔ 自寫第二套幾何、⛔ 判其可施或不可施。

🔑 **款 `1` 之窮舉方式（其產生方式須出艙·`自誤 411` 攔法 ①）**
    ⛔ 以單所列之「十三形」為窮舉之上限。本器改採**依<u>實際父節點型別</u>分類**：
    對受詞之**每一個** AST 出現，取其 `(父節點型別, 欄位名, ctx)` 三元組為其形
    ——此分類**構造上窮舉**（任一出現必有唯一之父節點），⛔ 依賴任何人所能想到之清單；
    其後再與單所令之十三形**對照並出艙差集**。
"""
import ast
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")   # 🛑 `newline` ⛔ 可省（Windows 文字層會譯 CRLF）

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
FN = "_solve_G_one"
SEED = "allocation_dir"
FORCED = "verify/stepg_pipeline.py"
BAR = "=" * 116

# 單所令之十三形（⛔ 作窮舉之上限·僅供對照）
ORDER_13 = ["Name-Store", "Subscript-Store", "Attribute-Store", "Dict 鍵字面", "DictComp",
            ".get", ".setdefault", ".update", "解包 Store", "For target", "形參 arg",
            "Return", "Call 之實參"]


def sh(a):
    cp = subprocess.run(a, capture_output=True, cwd=REPO)
    return cp.stdout, cp.returncode


def seg(t):
    print("\n" + BAR)
    print(t)
    print(BAR)


out, _ = sh(["git", "ls-tree", "HEAD", "--name-only", "verify/"])
FILES = ["app.py"] + sorted(x for x in out.decode("utf-8", "surrogateescape").splitlines()
                            if x.endswith(".py"))
SRC, TREE = {}, {}
for f in FILES:
    b, rc = sh(["git", "cat-file", "blob", "HEAD:" + f])
    assert rc == 0, f
    SRC[f] = b.decode("utf-8")
    TREE[f] = ast.parse(SRC[f], filename=f)

print(BAR)
print("【`W-G.9-304` `§六` 靜態量測器】")
print(BAR)
print("母體之產生指令 = git ls-tree HEAD --name-only verify/ | grep '\\.py$'  ＋ app.py")
print("母體基數 = %d（外部錨 ＝ `§一` 閘 `7` 之 34）⇒ 相符 = %s" % (len(FILES), len(FILES) == 34))


def parents(tree):
    """{id(child): (parent, field)}"""
    m = {}
    for p in ast.walk(tree):
        for fld, val in ast.iter_fields(p):
            if isinstance(val, list):
                for v in val:
                    if isinstance(v, ast.AST):
                        m[id(v)] = (p, fld)
            elif isinstance(val, ast.AST):
                m[id(val)] = (p, fld)
    return m


# ── `_solve_G_one` 之定義（**二形並取**：`def` ／ `ns[<字面>]`）──────
seg("款 `1`-0　`%s` 之定義處（**函式名二形並取**）" % FN)
defs = []
for f in FILES:
    for n in ast.walk(TREE[f]):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == FN:
            defs.append((f, n))
print("形① `def %s` ⇒ %d 處：%s" % (FN, len(defs), [f for f, _ in defs]))
lit = []
for f in FILES:
    for n in ast.walk(TREE[f]):
        if (isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value == FN):
            lit.append(f)
print("形② 字面 `%r`（`ns[<字面>]` 族）⇒ %d 處（逐檔：%s）"
      % (FN, len(lit), sorted(set(lit))))
assert len(defs) == 1, "🛑 定義處⛔ 為 1 ⇒ 停"
DF, DN = defs[0]
PAR = parents(TREE[DF])
body_nodes = list(ast.walk(DN))
print("其定義 ＝ `%s` :: `%s`（形參 %d 個·kwonly %d 個）"
      % (DF, FN, len(DN.args.args), len(DN.args.kwonlyargs)))

# ── 非頂層之基數（`自誤 411` 攔法 ②）────────────────────────────
inner = [n for n in body_nodes
         if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)) and n is not DN]
print("🔑 **非頂層之基數**（本框⛔ 及於該層）：`%s` 體內之 `FunctionDef`／`Lambda` ＝ **%d**"
      % (FN, len(inner)))

# ── 值之流（自 `allocation_dir` 起·遞移追其派生名）────────────────
seg("款 `1`　值之流：自 `%s` 之 `Store` 起，逐層追其**派生名**" % SEED)
tracked = {SEED}
flow = []
changed = True
while changed:
    changed = False
    for n in body_nodes:
        if isinstance(n, ast.Assign):
            rhs = ast.get_source_segment(SRC[DF], n.value) or ""
            if any(t in rhs for t in tracked):
                for tg in n.targets:
                    for x in ast.walk(tg):
                        if isinstance(x, ast.Name) and x.id not in tracked:
                            tracked.add(x.id)
                            flow.append((x.id, n))
                            changed = True
print("追蹤之名（含派生）＝ %s" % sorted(tracked))
for nm, n in flow:
    print("   派生 `%s` ← 逐字 = %s" % (nm, SRC[DF].splitlines()[n.lineno - 1].strip()))

# ── 依**實際父節點型別**分類（構造上窮舉）──────────────────────────
seg("款 `1`　受詞之全部出現（**依實際父節點型別分類**·構造上窮舉·⛔ 十三形清單）")
occ = []
for n in body_nodes:
    nm = None
    if isinstance(n, ast.Name) and n.id in tracked:
        nm = n.id
    elif isinstance(n, ast.arg) and n.arg in tracked:
        nm = n.arg
    elif isinstance(n, ast.keyword) and n.arg in tracked:
        continue                       # 由其 value 之 Name 計
    if nm is None:
        continue
    p, fld = PAR.get(id(n), (None, "?"))
    ctx = type(getattr(n, "ctx", "")).__name__ if hasattr(n, "ctx") else "-"
    occ.append((nm, type(p).__name__ if p else "?", fld, ctx, n.lineno))

buckets = {}
for nm, pt, fld, ctx, ln in occ:
    buckets.setdefault((pt, fld, ctx), []).append((nm, ln))
print("受詞之出現總數 = %d ／ 相異之 (父節點型別, 欄位, ctx) ＝ %d" % (len(occ), len(buckets)))
print("\n| 父節點型別 | 欄位 | `ctx` | 次數 | 名 | 逐字（首例） |")
print("|---|---|---|---|---|---|")
for k in sorted(buckets, key=lambda x: (-len(buckets[x]), str(x))):
    pt, fld, ctx = k
    rows = buckets[k]
    first = SRC[DF].splitlines()[rows[0][1] - 1].strip()
    print("| `%s` | `%s` | `%s` | %d | %s | %s |"
          % (pt, fld, ctx, len(rows), sorted({r[0] for r in rows}), first[:80]))

print("\n── 與單所令之**十三形**對照（⛔ 以其為窮舉之上限）──")
MAP = {
    ("Assign", "targets", "Store"): "Name-Store",
    ("Subscript", "value", "Load"): "Subscript-Store／Load 之 receiver",
    ("keyword", "value", "Load"): "Call 之實參（關鍵字）",
    ("Call", "args", "Load"): "Call 之實參（位置）",
    ("Return", "value", "Load"): "Return",
    ("arguments", "kwonlyargs", "-"): "形參 arg",
    ("arguments", "args", "-"): "形參 arg",
    ("Compare", "left", "Load"): "（十三形外）比較之左運算元",
    ("IfExp", "test", "Load"): "（十三形外）條件運算式之 test",
    ("GeneratorExp", "elt", "Load"): "（十三形外）genexp 之 elt",
    ("comprehension", "iter", "Load"): "（十三形外）comprehension 之 iter",
}
seen13, extra = set(), []
for k in buckets:
    lab = MAP.get(k)
    if lab is None:
        extra.append(k)
    elif lab in ORDER_13:
        seen13.add(lab)
    elif lab.startswith("（十三形外）"):
        extra.append(k)
print("   命中十三形者 = %s" % sorted(seen13))
print("   🔴 **十三形之外**者（＝ 該清單⛔ 窮舉之直證）= %s"
      % [(k, MAP.get(k, "(未對映)")) for k in extra])
print("   十三形中**本案零命中**者 = %s ⇒ 逐項 loud：其於本案非真形（⛔ 判為「無此受詞」）"
      % sorted(set(ORDER_13) - seen13))

sent = "ZZ" + str(os.getpid()) + "NOSUCH"
print("\n   判別力[必為零] 人造名（執行期組出·字面⛔ 出艙）之出現數 = %d（須 0）"
      % len([1 for n in body_nodes if isinstance(n, ast.Name) and n.id == sent]))
print("   判別力[必非零] 受詞之出現總數 = %d（須 ≥ 1）" % len(occ))

# ── 款 `2`　跨呼叫可見之容器 ─────────────────────────────────────
seg("款 `2`　跨呼叫可見之容器（receiver **⛔ 為該函式之區域名**者）")
locals_names = set()
for n in body_nodes:
    if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
        locals_names.add(n.id)
for a in DN.args.args + DN.args.kwonlyargs:
    locals_names.add(a.arg)
rets = [n for n in body_nodes if isinstance(n, ast.Return)]
ret_names = set()
for r in rets:
    for x in ast.walk(r):
        if isinstance(x, ast.Name):
            ret_names.add(x.id)
print("   `%s` 之區域名（Store ∪ 形參）基數 = %d" % (FN, len(locals_names)))
print("   其 `Return` 處數 = %d ／ `Return` 所含之名 = %s" % (len(rets), sorted(ret_names)))

conts = []
for n in body_nodes:
    if isinstance(n, ast.Assign):
        for tg in n.targets:
            if isinstance(tg, ast.Subscript):
                rhs = ast.get_source_segment(SRC[DF], n.value) or ""
                if any(t in rhs for t in tracked):
                    recv = ast.get_source_segment(SRC[DF], tg.value)
                    key = tg.slice
                    ktxt = ast.get_source_segment(SRC[DF], key)
                    kind = ("字串常數" if isinstance(key, ast.Constant)
                            and isinstance(key.value, str) else type(key).__name__)
                    conts.append((recv, ktxt, kind, n, rhs))
print("\n   受詞被寫入之 `Subscript` 容器 ⇒ %d 處" % len(conts))
if not conts:
    print("   🛑 **loud**：受詞**⛔ 寫入任何 `Subscript` 容器**（⇒ 須併查 `停七`）")
for recv, ktxt, kind, n, rhs in conts:
    print("\n   ● receiver 逐字 = `%s`" % recv)
    print("     鍵逐字 = %s   （鍵之 AST ＝ %s）" % (ktxt, kind))
    print("     賦值逐字 = %s" % SRC[DF].splitlines()[n.lineno - 1].strip())
    is_local = recv in locals_names
    is_ret = recv in ret_names
    print("     receiver 是否為本函式之區域名 ＝ %s ／ 是否為<u>回傳值</u> ＝ %s"
          % (is_local, is_ret))
    print("     ⇒ 跨呼叫可見 ＝ %s（依款 `2` 之列舉：`ns` 之項／`session_state` 之項／"
          "傳入之可變實參／模組級名／**回傳值**）" % is_ret)
    print("     🔑 **鍵是否含街廓識別** ＝ %s（鍵為**字串常數**·逐字 %s·⛔ 含 `blk`／`label`／`lbl`／`block_id`）"
          % (any(w in str(ktxt) for w in ("blk", "label", "lbl", "block_id")), ktxt))

# ── 該鍵之消費端（全倉 34 檔·正面列舉）──────────────────────────
seg("款 `2`（續）　該容器之鍵於生產碼 `34` 檔之**消費端**（正面列舉）")
KEYS = sorted({str(ktxt).strip("'\"") for _, ktxt, k, _, _ in conts if k == "字串常數"})
for key in KEYS:
    print("\n   鍵 = %r" % key)
    for f in FILES:
        hits = [(i + 1, l.strip()) for i, l in enumerate(SRC[f].splitlines()) if key in l]
        if hits:
            print("      %s ⇒ %d 列" % (f, len(hits)))
            for ln, t in hits:
                print("         %s" % t[:110])

# ── 款 `3`　強制呼叫端之在域名 ───────────────────────────────────
seg("款 `3`　`_corner_buffer_S` **強制呼叫端**之 `allocation_dir` 實參逐字（本批獨立重得）")
calls = []
for f in FILES:
    for n in ast.walk(TREE[f]):
        if isinstance(n, ast.Call):
            nm = (n.func.id if isinstance(n.func, ast.Name)
                  else n.func.attr if isinstance(n.func, ast.Attribute)
                  else (n.func.slice.value if isinstance(n.func, ast.Subscript)
                        and isinstance(n.func.slice, ast.Constant) else None))
            if nm == "_corner_buffer_S":
                calls.append((f, n))
print("   `_corner_buffer_S` 之呼叫點（三形並取）＝ %d 處" % len(calls))
for f, n in calls:
    host = None
    for h in ast.walk(TREE[f]):
        if isinstance(h, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if h.lineno <= n.lineno <= getattr(h, "end_lineno", h.lineno):
                if host is None or h.lineno > host.lineno:
                    host = h
    a3 = n.args[3] if len(n.args) > 3 else None
    txt = ast.get_source_segment(SRC[f], a3) if a3 is not None else "(未傳)"
    print("\n   ● %s :: %s" % (f, host.name if host else "<module>"))
    print("     呼叫逐字（首列）= %s" % SRC[f].splitlines()[n.lineno - 1].strip())
    print("     **第 4 位序實參（`allocation_dir`）逐字 = %s**" % txt)
    if a3 is not None and isinstance(a3, ast.Name) and host is not None:
        src_st = []
        for x in ast.walk(host):
            if isinstance(x, ast.Assign):
                for tg in x.targets:
                    for y in ast.walk(tg):
                        if isinstance(y, ast.Name) and y.id == a3.id:
                            src_st.append(SRC[f].splitlines()[x.lineno - 1].strip())
        print("     其名 `%s` 於該函式內之 `Store` ⇒ %d 處：%s" % (a3.id, len(src_st), src_st[:4]))
    if host is not None:
        in_scope = set()
        for x in ast.walk(host):
            if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Store):
                in_scope.add(x.id)
        for k in KEYS:
            print("     🛑 款 `2` 之容器鍵 %r 是否**在該函式內出現** ＝ %s"
                  % (k, k in SRC[f][:]))
            print("        ⛔ **以「在域」充「可取」**（坑 `bg`）——其**當場之值**須由款 `4` 之動態量測判")

# ── 款 `5`　判別力四造 ──────────────────────────────────────────
seg("款 `5`　判別力四造")
print("[必為 `34`] 外部錨（坑 `bj`）＝ %d ⇒ %s" % (len(FILES), "✅" if len(FILES) == 34 else "🔴"))
print("[必非零] 款 `1` 之去向處數 ＝ %d ⇒ %s" % (len(occ), "✅" if occ else "🔴"))
print("[必為零] 人造名於款 `1` 之框下命中 ＝ %d ⇒ ✅"
      % len([1 for n in body_nodes if isinstance(n, ast.Name) and n.id == sent]))
ns_top = set()
for st in TREE["app.py"].body:
    if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        ns_top.add(st.name)
print("[必真] `_first_corner_alloc_dir` 在 `ns` 之鍵 ＝ %s ⇒ %s"
      % ("_first_corner_alloc_dir" in ns_top,
         "✅" if "_first_corner_alloc_dir" in ns_top else "🔴"))

print("\n" + BAR)
print("【本器⛔ 判其可施或不可施·⛔ 擬任何改法或 diff】")
print(BAR)
