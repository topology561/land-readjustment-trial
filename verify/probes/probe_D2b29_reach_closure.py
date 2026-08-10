#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D-2b-29 §1-2 #3：產出鏈之**遞移閉包**是否可達結構閘「實跑」側算子。

⛔ 只量不判、零生產碼。⛔ **不得只做一層**（施工單明令）。

命題（§1-2 #3）：
    現用頂層之 7 份已過期基準（街角地指配 ×2／W-D.1.2 診斷 ×2／
    W-D.1.3-a 診斷 ×2／W-D.1.3-d 抵費地驗收 ×1）之產出鏈，
    **遞移可達** `solve_G_binary` ／ `iterate_G_S`。

射程宣告（本探針之工具射程·⛔ 命題射程 ⊆ 本射程 方為有效）：
    · 種子 ＝ `verify/selection_pipeline.py` 內**全部** `ns["…"]` 取名（AST 取·非 grep）。
    · 圖   ＝ `app.py` 之**全部** FunctionDef（含巢狀），邊 ＝ 函式體內之 ast.Call，
             涵蓋 `func.id`（裸名）／`func.attr`（屬性）／`ns["…"](…)`（間接）三形式。
    · 歸屬 ＝ 每個 Call 僅歸**最內層**之封閉 FunctionDef（⛔ 不自動加 parent→nested 邊，
             避免對「可達」作出過度近似之正向宣稱）。
    · 閉包 ＝ BFS 至不動點，並保留 parent 指標以**印出實際路徑**（供逐跳複核）。

自我驗證閘（CLAUDE.md：探針還原內部量須以碼面自身之保證為閘）：
    ① 種子名須**全部**在 app.py 找得到定義，否則印出缺名並 rc=2
       —— 因 ns 係由 app.py 之 globals() 供給，缺名即表示本探針之圖不完整。
    ② 目標名須存在於 app.py，否則命題無從測試 ⇒ rc=2。
    ③ 差集自證：閉包內之名 ∖ (有定義者 ∪ 外部名) ＝ ∅ 之對照數印出。
"""
import ast
import os
import sys
from collections import deque

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APP = os.path.join(ROOT, "app.py")
SEL = os.path.join(ROOT, "verify", "selection_pipeline.py")
OUT = os.path.join(ROOT, "verify", "out", "probe_D2b29_reach_closure.log")

TARGETS = ("solve_G_binary", "iterate_G_S")

buf = []


def say(s=""):
    buf.append(s)
    print(s)


def collect_ns_names(path):
    """AST 取 selection_pipeline 內 ns["…"] 之全部字串鍵。"""
    tree = ast.parse(open(path, encoding="utf-8").read())
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id == "ns":
            sl = n.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                names.add(sl.value)
    return names


def build_graph(path):
    """回傳 (defs, edges)。edges[f] = 該函式體內直接呼叫到的名字集合。"""
    tree = ast.parse(open(path, encoding="utf-8").read())
    defs, edges = {}, {}

    funcs = [n for n in ast.walk(tree)
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    for f in funcs:
        defs.setdefault(f.name, []).append(f.lineno)
        edges.setdefault(f.name, set())

    # 每個 Call 歸最內層封閉 FunctionDef：由外而內指派，內層覆寫外層
    owner = {}

    def assign(node, cur):
        for ch in ast.iter_child_nodes(node):
            nxt = ch.name if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)) else cur
            if isinstance(ch, ast.Call):
                owner[id(ch)] = cur
            assign(ch, nxt)

    assign(tree, None)

    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        home = owner.get(id(n))
        if home is None:
            continue
        fn = n.func
        callee = None
        if isinstance(fn, ast.Name):
            callee = fn.id
        elif isinstance(fn, ast.Attribute):
            callee = fn.attr
        elif isinstance(fn, ast.Subscript) and isinstance(fn.value, ast.Name) and fn.value.id == "ns":
            sl = fn.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str):
                callee = sl.value
        if callee:
            edges.setdefault(home, set()).add(callee)
    return defs, edges


def main():
    say("=" * 78)
    say("D-2b-29 §1-2 #3　產出鏈遞移閉包 → 結構閘「實跑」側算子")
    say("=" * 78)

    seeds = collect_ns_names(SEL)
    defs, edges = build_graph(APP)

    say("")
    say("【射程】種子（selection_pipeline 之 ns[\"…\"]·AST 取） = %d 個" % len(seeds))
    for s in sorted(seeds):
        say("   · %-42s app.py 有定義？ %s" % (s, "✅" if s in defs else "❌（外部／常數）"))

    # ── 自我驗證閘 ② ─────────────────────────────────────────
    say("")
    say("【自我驗證閘②】目標名於 app.py 之定義：")
    miss = [t for t in TARGETS if t not in defs]
    for t in TARGETS:
        say("   · %-20s %s  (lineno=%s)" % (t, "✅ 有定義" if t in defs else "❌ 無定義",
                                            defs.get(t, "—")))
    if miss:
        say("🛑 目標名缺定義 ⇒ 命題無從測試")
        return 2

    # ── BFS 遞移閉包（保留 parent 以印路徑）─────────────────
    seed_defined = sorted(s for s in seeds if s in defs)
    parent, seen = {}, set(seed_defined)
    dq = deque(seed_defined)
    depth = {s: 0 for s in seed_defined}
    while dq:
        cur = dq.popleft()
        for nxt in sorted(edges.get(cur, ())):
            if nxt not in seen:
                seen.add(nxt)
                parent[nxt] = cur
                depth[nxt] = depth[cur] + 1
                dq.append(nxt)

    say("")
    say("【閉包】自 %d 個有定義之種子起，BFS 至不動點 ⇒ 觸及名 %d 個"
        % (len(seed_defined), len(seen)))
    say("        其中 app.py 有定義者 %d／外部名（stdlib 等）%d"
        % (sum(1 for n in seen if n in defs), sum(1 for n in seen if n not in defs)))

    say("")
    say("【判定】目標可達性（⛔ 遞移·非一層）：")
    rc = 0
    for t in TARGETS:
        if t in seen:
            path, cur = [], t
            while cur is not None:
                path.append(cur)
                cur = parent.get(cur)
            path.reverse()
            say("   ✅ %-18s 可達（跳數 %d）" % (t, depth[t]))
            say("      路徑：%s" % " → ".join(path))
        else:
            say("   ❌ %-18s **不可達**" % t)
            rc = 1

    # ── 一層對照（坐實「⛔ 一層不算」之必要性）────────────
    one = set()
    for s in seed_defined:
        one |= edges.get(s, set())
    say("")
    say("【對照】只做一層之結果（施工單所禁之作法）：")
    for t in TARGETS:
        say("   · %-18s 一層命中？ %s" % (t, "是" if t in one else "**否**"))
    say("   ⇒ 若只做一層即下「零交集」之結論，將與遞移閉包之結果相反。")

    # ── 自我驗證閘 ③ 差集自證 ────────────────────────────
    undef = sorted(n for n in seen if n not in defs)
    say("")
    say("【自我驗證閘③】差集自證：閉包 %d ＝ app.py 有定義 %d ＋ 外部名 %d，差 %d（須為 0）"
        % (len(seen), len(seen) - len(undef), len(undef), len(seen) - (len(seen) - len(undef)) - len(undef)))

    say("")
    say("rc = %d" % rc)
    return rc


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(buf) + "\n")
    sys.exit(rc)
