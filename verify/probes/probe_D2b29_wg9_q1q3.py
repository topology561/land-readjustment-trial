#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""D-2b-29 §4：W-G.9 前置偵察 Q1〜Q3（⛔ 只查不改·零生產碼·不接線·不實作）。

🔒 **射程宣告**（依本批新立之失敗考古 **節 60**·立戒者次批須自檢）：
  · 母體 ＝ 倉內全部 `*.py`，⛔ 排除 `.claude/worktrees/`（巢狀 worktree ＝ 完整倉副本）。
  · Q1／Q2 之「活碼」判準 ＝ **AST 之 Name／Call 節點**（⛔ 非文字命中、⛔ 非全檔 walk 存在性）；
    每一命中**逐函式定位**至最內層 FunctionDef。
  · Q3 之呼叫形式 ＝ `func.id`（裸名）／`func.attr`（屬性）／`ns["…"](…)`（間接）**三種全覆蓋**。
  · 凡窮舉均附**差集自證**：文字命中 ∖ 已歸類 ＝ ∅（⛔ 總數相符不算·空集合不算通過）。

⛔ 本探針不改任何檔、不呼叫任何生產函式，僅做靜態剖析。
"""
import ast
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "verify", "out", "probe_D2b29_wg9_q1q3.log")

# 生產碼之定義（與 D-2b-28 §五 同）：⛔ probes／fixtures／tools 為量測件，不計生產
PROD = ("app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
        "verify/run_verification.py", "verify/wf_f0.py", "verify/wf_f1.py",
        "verify/wf_f2.py", "verify/wf_f3.py", "verify/wf_f4.py")

buf = []


def say(s=""):
    buf.append(s)
    print(s)


def py_files():
    """⚠️ 排除巢狀 worktree 之判斷**必須相對 ROOT**。

    🩸 血訓（本探針首版·D-2b-29 當場自糾）：首版以絕對路徑判
    `if os.sep + ".claude" + os.sep + "worktrees" in dp: continue`
    ——而本 session 之 ROOT **自身**即位於 `…/.claude/worktrees/<name>/`
    ⇒ **每一個目錄都命中該式** ⇒ 母體 `0` 檔、三問全部印出漂亮的「0」。
    ⇒ 與失敗考古**節 60**（工具射程小於命題）同族，
      且係 `D-2b-2` 已登記之「**空真假綠（母體 = 0）**」之再現。
    🔒 故本函式附**母體非空閘**（見 main() 開頭），⛔ 母體為 0 一律 fail-fast。
    """
    out = []
    for dp, dns, fns in os.walk(ROOT):
        dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
        rel_dir = os.path.relpath(dp, ROOT).replace("\\", "/")
        if rel_dir == ".claude/worktrees" or rel_dir.startswith(".claude/worktrees/"):
            dns[:] = []
            continue
        for fn in fns:
            if fn.endswith(".py"):
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT).replace("\\", "/"))
    return sorted(out)


def innermost_map(tree):
    """回傳 {id(node): 最內層封閉 FunctionDef 名}。"""
    owner = {}

    def walk(node, cur):
        for ch in ast.iter_child_nodes(node):
            nxt = ch.name if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)) else cur
            owner[id(ch)] = cur
            walk(ch, nxt)
    walk(tree, "<module>")
    return owner


def live_lines(tree, ident):
    """該識別字作為**活 AST 節點**出現之 (lineno, 最內層函式) 清單。"""
    owner = innermost_map(tree)
    hits = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Name) and n.id == ident:
            hits.append((n.lineno, owner.get(id(n), "<module>")))
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == ident:
            hits.append((n.lineno, "<def>"))
    return hits


def text_lines(path, needle):
    res = []
    for i, ln in enumerate(io.open(os.path.join(ROOT, path), encoding="utf-8",
                                   errors="replace").read().split("\n"), 1):
        if needle in ln:
            res.append((i, ln.strip()))
    return res


def parse(path):
    try:
        return ast.parse(io.open(os.path.join(ROOT, path), encoding="utf-8").read())
    except SyntaxError:
        return None


def str_const_lines(tree, needle):
    """該檔中「字串常數（含 docstring）內含 needle」所覆蓋之行號集合。"""
    out = set()
    if tree is None:
        return out
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and needle in n.value:
            lo = getattr(n, "lineno", None)
            hi = getattr(n, "end_lineno", lo)
            if lo:
                out.update(range(lo, (hi or lo) + 1))
    return out


def partition(text_hits, ast_keys, needle, trees):
    """三分：AST 活節點／`#` 註解／字串常數。回傳 (comment, string, residual)。

    🔒 **差集自證之正確框**（§4-3）：殘差須為 ∅。
    ⚠️ 首版把「註解／字串」也算進殘差 ⇒ 印出「須為 0」卻得 30，係**框錯非資料錯**；
       ⛔ 註解與字串本來就是合法歸類，不該落在殘差。
    """
    comment, string, residual = [], [], []
    for f, ln, src in text_hits:
        if (f, ln) in ast_keys:
            continue
        head = src.split(needle)[0] if needle in src else src
        if src.lstrip().startswith("#") or "#" in head:
            comment.append((f, ln, src))
        elif ln in str_const_lines(trees.get(f), needle):
            string.append((f, ln, src))
        else:
            residual.append((f, ln, src))
    return comment, string, residual


def main():
    files = py_files()
    say("=" * 80)
    say("D-2b-29 §4　W-G.9 前置偵察 Q1〜Q3（⛔ 只查不改）")
    say("=" * 80)
    say("【射程】倉內 *.py 共 %d 檔（⛔ 已排除 .claude/worktrees/）" % len(files))
    say("        生產碼定義 = %s" % " / ".join(PROD))

    # ── 🔒 母體非空閘（§4-3「空集合不得算通過」·fail-fast）──────────
    missing = [p for p in PROD if p not in files]
    say("")
    say("【自我驗證閘⓪】母體非空 ＋ 生產碼全在母體內：")
    say("   · 母體檔數 = %d（須 > 0）" % len(files))
    say("   · 生產碼 %d 支中不在母體者 = %d %s"
        % (len(PROD), len(missing), ("⇒ " + ", ".join(missing)) if missing else ""))
    if not files or missing:
        say("🛑 母體為空或生產碼缺漏 ⇒ **本輪結果一律不得採信**（rc=2）")
        return 2

    # ══════════════════════════ Q1 ══════════════════════════
    say("")
    say("#" * 80)
    say("## Q1　`w_lo = min(_W(0,0), _W(D,0))` 於倉內是否存在為**活碼**")
    say("#" * 80)

    q1_text, q1_live = [], []
    for f in files:
        for ln, src in text_lines(f, "w_lo"):
            q1_text.append((f, ln, src))
        t = parse(f)
        if t is not None:
            for ln, fn in live_lines(t, "w_lo"):
                q1_live.append((f, ln, fn))

    say("")
    say("【文字命中】`w_lo` 共 %d 處：" % len(q1_text))
    for f, ln, src in q1_text:
        say("   · %-46s :%-6d %s" % (f, ln, src[:88]))

    say("")
    say("【活碼命中】`w_lo` 作為 AST Name 節點 共 %d 處：" % len(q1_live))
    if not q1_live:
        say("   （無）")
    for f, ln, fn in q1_live:
        say("   · %-46s :%-6d  函式 = %s" % (f, ln, fn))

    # 差集自證：文字命中 ∖ 活碼命中 = 註解／字串
    live_key = {(f, ln) for f, ln, _ in q1_live}
    _trees1 = {f: parse(f) for f in files}
    q1_cmt, q1_str, q1_res = partition(q1_text, live_key, "w_lo", _trees1)
    say("")
    say("【差集自證】三分：AST 活節點 %d ＋ `#` 註解 %d ＋ 字串常數 %d ＝ %d／文字命中 %d"
        % (len(live_key), len(q1_cmt), len(q1_str),
           len(live_key) + len(q1_cmt) + len(q1_str), len(q1_text)))
    say("            ⇒ **殘差 = %d**（須為 0）" % len(q1_res))
    for f, ln, s in q1_cmt:
        say("   · [註解]   %-42s :%-6d %s" % (f, ln, s[:70]))
    for f, ln, s in q1_str:
        say("   · [字串]   %-42s :%-6d %s" % (f, ln, s[:70]))
    for f, ln, s in q1_res:
        say("   🔴 殘差 · %-42s :%-6d %s" % (f, ln, s[:70]))

    say("")
    say("【Q1 判定】`w_lo` 於 `_build_corner_range_v3` 內是否為活碼：")
    in_v3 = [x for x in q1_live if x[2] == "_build_corner_range_v3"]
    say("   ⇒ %s（該函式內活碼命中 %d 處）"
        % ("❌ **否**（無活碼）" if not in_v3 else "✅ 是", len(in_v3)))

    # ══════════════════════════ Q2 ══════════════════════════
    say("")
    say("#" * 80)
    say("## Q2　活之「min 取二端」結構位於哪些函式；其二端幾何各是什麼線")
    say("#" * 80)

    say("")
    say("【活碼】`min(...)` 之實參中含 `_W(...)` 呼叫者：")
    found2 = []
    for f in files:
        t = parse(f)
        if t is None:
            continue
        owner = innermost_map(t)
        for n in ast.walk(t):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id == "min"):
                continue
            wargs = [a for a in n.args
                     if isinstance(a, ast.Call) and isinstance(a.func, ast.Name)
                     and a.func.id.startswith("_W")]
            if not wargs:
                continue
            try:
                expr = ast.unparse(n)
            except Exception:
                expr = "<unparse 不可用>"
            found2.append((f, n.lineno, owner.get(id(n), "<module>"), expr))
    if not found2:
        say("   （無）")
    for f, ln, fn, expr in found2:
        say("   · %-30s :%-6d 函式 = %-26s %s" % (f, ln, fn, expr[:100]))

    say("")
    say("【`_W` 之定義處（活碼·逐函式）】：")
    for f in files:
        t = parse(f)
        if t is None:
            continue
        owner = innermost_map(t)
        for n in ast.walk(t):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == "_W":
                say("   · %-30s :%-6d 定義於 = %s" % (f, n.lineno, owner.get(id(n), "<module>")))

    # ══════════════════════════ Q3 ══════════════════════════
    say("")
    say("#" * 80)
    say("## Q3　`k97_solve_alloc_t` 之**生產呼叫數**（三形式全覆蓋 ＋ 差集自證）")
    say("#" * 80)

    NAME = "k97_solve_alloc_t"
    q3_text = []
    for f in files:
        for ln, src in text_lines(f, NAME):
            q3_text.append((f, ln, src))

    cls = {}   # (f, ln) -> [分類…]
    for f in files:
        t = parse(f)
        if t is None:
            continue
        owner = innermost_map(t)
        for n in ast.walk(t):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == NAME:
                cls.setdefault((f, n.lineno), []).append(("def", owner.get(id(n), "<module>")))
            if isinstance(n, ast.Call):
                fn_ = n.func
                hit = None
                if isinstance(fn_, ast.Name) and fn_.id == NAME:
                    hit = "call:func.id"
                elif isinstance(fn_, ast.Attribute) and fn_.attr == NAME:
                    hit = "call:func.attr"
                elif isinstance(fn_, ast.Subscript) and isinstance(fn_.value, ast.Name) \
                        and fn_.value.id == "ns":
                    sl = fn_.slice
                    if isinstance(sl, ast.Constant) and sl.value == NAME:
                        hit = 'call:ns["…"]'
                if hit:
                    cls.setdefault((f, n.lineno), []).append((hit, owner.get(id(n), "<module>")))
            if isinstance(n, ast.Name) and n.id == NAME:
                cls.setdefault((f, n.lineno), []).append(("ref:Name", owner.get(id(n), "<module>")))

    say("")
    say("【文字命中】共 %d 處：" % len(q3_text))
    for f, ln, src in q3_text:
        tags = cls.get((f, ln), [])
        lab = "／".join(sorted({t for t, _ in tags})) if tags else "**未歸類**"
        home = tags[0][1] if tags else "—"
        say("   · %-30s :%-6d [%-22s] 函式=%-24s %s" % (f, ln, lab, home, src[:52]))

    trees = {f: parse(f) for f in files}
    q3_ast = {(f, ln) for (f, ln) in cls}
    q3_cmt, q3_str, q3_res = partition(q3_text, q3_ast, NAME, trees)
    say("")
    say("【差集自證】三分：AST 活節點 %d ＋ `#` 註解 %d ＋ 字串常數 %d ＝ %d／文字命中 %d"
        % (len(q3_ast), len(q3_cmt), len(q3_str), len(q3_ast) + len(q3_cmt) + len(q3_str),
           len(q3_text)))
    say("            ⇒ **殘差 = %d**（須為 0·⛔ 空集合不算通過·母體 %d > 0 已由閘⓪保證）"
        % (len(q3_res), len(q3_text)))
    for f, ln, s in q3_res:
        say("   🔴 殘差 · %-30s :%-6d %s" % (f, ln, s[:60]))

    calls = [(f, ln, t, home) for (f, ln), tags in sorted(cls.items())
             for t, home in tags if t.startswith("call:")]
    prod_calls = [c for c in calls if c[0] in PROD]
    say("")
    say("【呼叫彙總】全倉呼叫 %d 處；其中**生產碼**內 %d 處" % (len(calls), len(prod_calls)))
    for f, ln, t, home in calls:
        say("   · %-30s :%-6d %-16s 函式=%-26s %s"
            % (f, ln, t, home, "🔴 生產" if f in PROD else "（量測件）"))

    say("")
    say("【Q3 判定】`%s` 之**生產呼叫數 ＝ %d**" % (NAME, len(prod_calls)))

    say("")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write("\n".join(buf) + "\n")
    sys.exit(rc)
