"""`W-G.9-303`　`§三` 款 `1`／`4` ＋ `§四` 款 `1` 之**框補正器**（v2·唯讀·零生產碼）。

🩸 **本器之由**（v1 之三處自捕·⛔ 頂替·⛔ 覆寫 v1 之落檔）：
  甲　`§三` 款 `1` 所令之**四形**（`Subscript`／`Assign`／`.get`／`Dict`-`DictComp`）
      **⛔ 涵蓋 `.setdefault`**，而層① 鍵之**真寫入形正是 `.setdefault`**
      ⇒ v1 之「源頭」節**零命中**。本器加**第五形 `.setdefault`** 並逐層溯至源頭之名。
  乙　`§四` 款 `1` 之 `Store` 框於 v1 **漏抓 `Subscript`-Store（`X['is_corner'] = …`）
      與 `Dict` 鍵字面** ——🔴 **即同單 `§三` 款 `1` 附款所警告之 `ast.Dict` 盲區**，
      於次一款即重踩（`CLAUDE.md`「立戒者在下一批最容易違反自己的戒」之實例）。
  丙　`§三` 款 `4` 之母體（`ns` 全部鍵 ＝ `t.body` 頂層名）**結構上⛔ 含內層閉包**
      ⇒ 本器**分列**頂層與內層二母體，並逐項具名其結構性成因。

🔒 ⛔ 改生產碼一字、⛔ 動任何既有探針、⛔ 自寫第二套幾何、⛔ 判「可信／不可信」。
"""
import ast
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
KEY, SS_KEY = "side_lines_by_side", "f3_cad_side_lines_by_side"
K2_WORDS = ["blk", "label", "lbl", "block_id"]
GEOM_WORDS = ["block_poly", "poly", "geom"]
BAR = "=" * 116


def sh(a):
    cp = subprocess.run(a, capture_output=True, cwd=REPO)
    return cp.stdout, cp.returncode


def sentinel(t):
    return "Z" + chr(0x5A) + t + str(os.getpid()) + chr(0x5F) + "NOSUCH"


out, _ = sh(["git", "ls-tree", "HEAD", "--name-only", "verify/"])
FILES = ["app.py"] + sorted(x for x in out.decode("utf-8", "surrogateescape").splitlines()
                            if x.endswith(".py"))
SRC, TREE = {}, {}
for f in FILES:
    b, rc = sh(["git", "cat-file", "blob", "HEAD:" + f])
    SRC[f], TREE[f] = b.decode("utf-8"), ast.parse(b.decode("utf-8"), filename=f)

OWN = {}
for f in FILES:
    o = {}

    def walk(n, q, o=o):
        for ch in ast.iter_child_nodes(n):
            nq = q + [ch.name] if isinstance(
                ch, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else q
            o[id(ch)] = "::".join(q) if q else "<module>"
            walk(ch, nq)
    walk(TREE[f], [])
    OWN[f] = o


def own(f, n):
    return OWN[f].get(id(n), "?")


def line(f, n):
    return SRC[f].splitlines()[n.lineno - 1].strip()


def seg(t):
    print("\n" + BAR); print(t); print(BAR)


print(BAR); print("【`W-G.9-303` 靜態量測器 v2 —— 框補正】"); print(BAR)
print("母體之產生指令 = git ls-tree HEAD --name-only verify/ | grep '\\.py$'  ＋ app.py")
print("母體基數 = %d（外部錨 `§零` 閘 `7` ＝ 34）⇒ 相符 = %s" % (len(FILES), len(FILES) == 34))

# ══ 甲　第五形 `.setdefault` ＋ 層① 鍵之源頭鏈 ════════════════════
seg("`§三` 款 `1` 補正　**第五形 `.setdefault`**（單所令四形⛔ 涵蓋之）")
sd = []
for f in FILES:
    for n in ast.walk(TREE[f]):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "setdefault"):
            base = n.func.value
            txt = ast.get_source_segment(SRC[f], base) or ""
            if KEY in txt or SS_KEY in txt:
                sd.append((f, n, txt))
print("形 `.setdefault` 且其 receiver 逐字含 `%s`／`%s` ⇒ %d 處" % (KEY, SS_KEY, len(sd)))
if not sd:
    print("   🛑 **loud**：無命中（母體 = %d 檔）" % len(FILES))
roots = []
for f, n, txt in sd:
    karg = n.args[0] if n.args else None
    ktxt = ast.get_source_segment(SRC[f], karg) if karg is not None else "(無)"
    print("   %s :: %s" % (f, own(f, n)))
    print("       逐字        = %s" % line(f, n))
    print("       receiver    = %s" % txt)
    print("       🔑 層① 鍵   = %s   （AST = %s）" % (ktxt, type(karg).__name__))
    if isinstance(karg, ast.Name):
        roots.append((f, own(f, n), karg.id, n.lineno))

seg("`§三` 款 `1` 補正（續）　層① 鍵之名**逐層溯至源頭之產生式**")
for f, scope, nm, ln in roots:
    print("\n   ● 層① 鍵之名 = `%s`   （於 %s :: %s）" % (nm, f, scope))
    host = None
    for n in ast.walk(TREE[f]):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if n.lineno <= ln <= getattr(n, "end_lineno", n.lineno):
                if host is None or n.lineno > host.lineno:
                    host = n
    hits = 0
    for n in ast.walk(host if host else TREE[f]):
        tg = []
        if isinstance(n, ast.Assign):
            tg = n.targets
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            tg = [n.target]
        for t in tg:
            for x in ast.walk(t):
                if isinstance(x, ast.Name) and x.id == nm and isinstance(x.ctx, ast.Store):
                    hits += 1
                    val = getattr(n, "value", None) or getattr(n, "iter", None)
                    vtxt = ast.get_source_segment(SRC[f], val) if val is not None else "?"
                    print("       [Store] 逐字 = %s" % line(f, n))
                    print("               產生式 = %s" % (vtxt or "")[:150])
                    if isinstance(val, ast.Call):
                        fn = val.func
                        fnm = (fn.id if isinstance(fn, ast.Name)
                               else fn.attr if isinstance(fn, ast.Attribute) else "?")
                        print("               🔑 **源頭之名 = `%s`**（`Call`·其位序回傳）" % fnm)
                        for dn in ast.walk(TREE[f]):
                            if isinstance(dn, (ast.FunctionDef, ast.AsyncFunctionDef)) and dn.name == fnm:
                                ps = [a.arg for a in dn.args.args]
                                print("               `%s` 之定義 :: %s   形參 = %s"
                                      % (fnm, own(f, dn), ps))
                                print("               層級 = %s"
                                      % ("**頂層**（在 `ns` 內）" if own(f, dn) == "<module>"
                                         else "🔴 **內層閉包**（於 `%s` 之內·⛔ 在 `ns` 內）" % own(f, dn)))
                                for rn in ast.walk(dn):
                                    if isinstance(rn, ast.Return) and rn.value is not None:
                                        print("               Return 逐字 = %s"
                                              % (ast.get_source_segment(SRC[f], rn.value) or "")[:120])
    if hits == 0:
        print("       🛑 **loud：⛔ 可判**（該名於其函式內無 `Store`）")

# ══ 乙　`is_corner` 之**五形分列** ═════════════════════════════════
seg("`§四` 款 `1` 補正　`is_corner` 之**五形分列**（v1 之二形⛔ 涵蓋字面鍵）")
F = {"Name-Store": [], "arg(形參)": [], "Subscript-Store(字面鍵)": [],
     "Dict 鍵字面": [], "Load(讀)": []}
for f in FILES:
    for n in ast.walk(TREE[f]):
        if isinstance(n, ast.Name) and n.id == "is_corner":
            F["Name-Store" if isinstance(n.ctx, ast.Store) else "Load(讀)"].append((f, n))
        if isinstance(n, ast.arg) and n.arg == "is_corner":
            F["arg(形參)"].append((f, n))
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if (isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Constant)
                        and t.slice.value == "is_corner"):
                    F["Subscript-Store(字面鍵)"].append((f, n))
        if isinstance(n, ast.Dict):
            for k in n.keys:
                if isinstance(k, ast.Constant) and k.value == "is_corner":
                    F["Dict 鍵字面"].append((f, n))
for k in F:
    print("\n── 形 `%s` ⇒ %d 處 ──" % (k, len(F[k])))
    if not F[k]:
        print("   🛑 **loud**：無命中")
    if k == "Load(讀)":
        seen = {}
        for f, n in F[k]:
            seen.setdefault((f, own(f, n)), 0)
            seen[(f, own(f, n))] += 1
        for (f, o), c in sorted(seen.items()):
            print("   %s :: %s   ×%d" % (f, o, c))
        continue
    for f, n in F[k]:
        print("   %s :: %s" % (f, own(f, n) if not isinstance(n, ast.arg) else "(形參)"))
        print("       逐字 = %s" % line(f, n)[:150])

print("\n🔑 **受詞係逐宗抑或逐街廓**（以其賦值式所消費之名判·逐字出艙）")
for f, n in F["Subscript-Store(字面鍵)"]:
    tgt = n.targets[0]
    recv = ast.get_source_segment(SRC[f], tgt.value)
    val = ast.get_source_segment(SRC[f], n.value)
    print("   %s :: %s" % (f, own(f, n)))
    print("       receiver（被寫之物）逐字 = %s" % recv)
    print("       值（賦值式）逐字         = %s" % (val or "")[:140])

# ══ 丙　款 `4` 之母體分列 ═════════════════════════════════════════
seg("`§三` 款 `4` 補正　母體**二層分列**（頂層 `ns` 鍵 ／ 內層閉包）")
top_fn, inner_fn = [], []
for f in FILES:
    for n in ast.walk(TREE[f]):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            (top_fn if own(f, n) == "<module>" else inner_fn).append((f, n))
print("頂層 `FunctionDef` = %d ／ 內層 `FunctionDef` = %d（母體 %d 檔）"
      % (len(top_fn), len(inner_fn), len(FILES)))
for tag, pool in (("頂層（＝ 款 `4` 所令之母體）", top_fn), ("🔴 內層閉包（⛔ 在該母體內）", inner_fn)):
    hit = []
    for f, n in pool:
        ps = [a.arg for a in n.args.args] + [a.arg for a in n.args.kwonlyargs]
        if not any(any(g in p for g in GEOM_WORDS) for p in ps):
            continue
        for rn in ast.walk(n):
            if isinstance(rn, ast.Return) and rn.value is not None:
                t = ast.get_source_segment(SRC[f], rn.value) or ""
                if any(w in t for w in K2_WORDS):
                    hit.append((f, n, ps, t))
                    break
    print("\n── %s ⇒ 命中 %d ──" % (tag, len(hit)))
    if not hit:
        print("   🛑 **loud**：該層內無此映射（該層基數 = %d）" % len(pool))
    for f, n, ps, t in hit:
        print("   %s :: %s   形參 = %s" % (f, n.name, ps))
        print("       Return 逐字 = %s" % t[:130])

print("\n🔑 **`_best_block` 之二獨立結構性成因**（其為本案唯一之「幾何 → 街廓識別」實質映射）")
for f, n in inner_fn:
    if n.name == "_best_block":
        ps = [a.arg for a in n.args.args]
        print("   定義 = %s :: %s（內層閉包·宿主 = `%s`）" % (f, n.name, own(f, n)))
        print("   形參 = %s" % ps)
        print("   成因① 其為**內層閉包** ⇒ ⛔ 在 `t.body` 頂層名（`ns` 鍵）之母體內")
        print("   成因② 其形參⛔ 含 %s 任一字樣 ⇒ 縱置於頂層，款 `4` 之框亦⛔ 命中" % GEOM_WORDS)
        for rn in ast.walk(n):
            if isinstance(rn, ast.Return) and rn.value is not None:
                print("   Return 逐字 = %s" % (ast.get_source_segment(SRC[f], rn.value) or "")[:120])

s = sentinel("v2")
print("\n判別力[必為零] 人造名（執行期組出·字面⛔ 出艙）於 AST 命中 = %d（須 0）"
      % len([1 for f in FILES for n in ast.walk(TREE[f])
             if isinstance(n, ast.Name) and n.id == s]))
print("判別力[必非零] `is_corner` 五形合計 = %d（須 ≥ 1）" % sum(len(v) for v in F.values()))
print("\n" + BAR); print("【本器⛔ 判「可信／不可信」·⛔ 擬任何改法或 diff】"); print(BAR)
