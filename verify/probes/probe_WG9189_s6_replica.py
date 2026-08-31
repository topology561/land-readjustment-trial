# -*- coding: utf-8 -*-
r"""**`W-G.9-189` `S-6`**：複刻區同步閘——AST 正規化對拍 ＋ 遞迴下鑽（⛔ 零生產碼變更）

## 受詞（施工單 `W-G.9-189 §零 S-6` 逐字）

> 倉內三處逐字自陳迴圈層係**人工複本**：`verify/stepg_pipeline.py:35`／`:345`／`:401`。
> 發單側已現查：`verify/` 內**⛔ 無任何比對此二區之自動閘**。
> ⇒ 動任何一字之前：① 逐段對拍 `app.py` Step G 迴圈區與 `stepg_pipeline.py:401` 起之複刻區，
> **出艙現存分歧清單**（逐項具名：僅縮排／僅註解／僅 `ns` 取用形 ⇒ 記為**形式差**；
> 控制流、判斷式、賦值、呼叫序之任一差異 ⇒ 記為**實質差**）。② 同法對拍 `:345` 起之
> `_build_g_row` / `_solve_one` 二份。③ 🛑 **若出現任一「實質差」⇒ 停機上呈，⛔ 不得先寫遞補。**

🔒 **本檔即該自動閘之首次落地**（`verify/` 內原⛔ 無之）。

## 框（逐字宣告·`S-6` 末段所令）

**母體** ＝ 本倉之 `app.py` 與 `verify/stepg_pipeline.py` 之**四組對應區**：
`_build_g_row`／`_solve_one`／`_advance_block_with_split`／逐街廓迴圈
（`for blk_label, parcels_in_blk in parcels_by_block.items():`）。
🔒 **界定以 AST 之 `FunctionDef`／`For` 節點**，⛔ **非**自陳之舊行號「約 `14650-15450`」
——後者係 `app.py` 為 `~15450` 列時之錨，現為 `23412` 列（`行號衛生`）。

**正規化**（＝單所定義之「形式差」之機械實現）：
1. **僅縮排** ⇒ AST 天然不變。
2. **僅註解** ⇒ AST 天然不含；**docstring 逐層剝除**。
3. **僅取用形** ⇒ `ns["X"]`／`ns['X']` → `X`；`st.session_state` → `ss`
   （二者為同一 session 容器之 app 側／harness 側形）。
🔒 其餘一切**⛔ 不正規化**。

**分類**：`st.*` 略去（app 有／stepg 無且為 `st.<...>` 之單獨敘述·自陳「headless fake no-op 故略」）
／**實質差**（其餘一切）。

## 🩸 首版之量測器缺口（CC 自捕·`W-G.9-14` 修法 ②）

首版於**敘述層**⛔ 未剝 docstring、⛔ 未正規化 `st.session_state`、且對複合敘述⛔ 未下鑽
⇒ 偽陽（docstring／取用形／「僅內部有差之整個 `for`」全被記為實質差）。本版補之，
並附**判別力對照**（注入 `round(`→`int(`，須被抓到）證其**非恆綠**。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不改 `verify/stepg_pipeline.py`。⛔ 不寫死本機絕對路徑。
"""
import ast
import difflib
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 推得·⛔ 不寫死絕對路徑
APP = os.path.join(REPO, "app.py")
STG = os.path.join(VERIFY, "stepg_pipeline.py")
OUTDIR = os.path.join(VERIFY, "out")
MAXDEPTH = 6

L = []


def say(s=""):
    L.append(s)
    print(s)


class Norm(ast.NodeTransformer):
    def visit_Subscript(self, node):
        self.generic_visit(node)
        v, s = node.value, node.slice
        if isinstance(v, ast.Name) and v.id == "ns" and isinstance(s, ast.Constant) \
                and isinstance(s.value, str):
            return ast.copy_location(ast.Name(id=s.value, ctx=node.ctx), node)
        return node

    def visit_Attribute(self, node):
        self.generic_visit(node)
        if isinstance(node.value, ast.Name) and node.value.id == "st" \
                and node.attr == "session_state":
            return ast.copy_location(ast.Name(id="ss", ctx=node.ctx), node)
        return node

    def _strip(self, node):
        b = getattr(node, "body", None)
        if isinstance(b, list) and b and isinstance(b[0], ast.Expr) \
                and isinstance(b[0].value, ast.Constant) \
                and isinstance(b[0].value.value, str):
            node.body = b[1:] or [ast.Pass()]
        return node

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        return self._strip(node)


def normalize(node):
    m = Norm().visit(ast.parse(ast.unparse(node)))
    if m.body and isinstance(m.body[0], ast.Expr) \
            and isinstance(m.body[0].value, ast.Constant) \
            and isinstance(m.body[0].value.value, str):
        m.body = m.body[1:]
    ast.fix_missing_locations(m)
    return m.body[0] if len(m.body) == 1 else m


def body_of(n):
    return list(getattr(n, "body", []) or [])


def sig(st):
    return ast.dump(st, annotate_fields=False)


def head(st):
    try:
        return ast.unparse(st).splitlines()[0][:130]
    except Exception:                                            # noqa: BLE001
        return "<unparse 失敗>"


def is_st(st):
    h = head(st).strip()
    return h.startswith("st.") or h.startswith("with st.")


FOUND = {"st": [], "real": []}


def walk(name, a_body, s_body, depth, path):
    sm = difflib.SequenceMatcher(None, [sig(x) for x in a_body], [sig(x) for x in s_body])
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        av, sv = a_body[i1:i2], s_body[j1:j2]
        if av and not sv and all(is_st(x) for x in av):
            FOUND["st"].append((name, path, [head(x) for x in av]))
            continue
        if len(av) == 1 and len(sv) == 1 and depth < MAXDEPTH \
                and type(av[0]) is type(sv[0]) and head(av[0]) == head(sv[0]) \
                and body_of(av[0]) and body_of(sv[0]):
            walk(name, body_of(av[0]), body_of(sv[0]), depth + 1,
                 path + [head(av[0]).strip()[:60]])
            oa = list(getattr(av[0], "orelse", []) or [])
            os_ = list(getattr(sv[0], "orelse", []) or [])
            if oa or os_:
                walk(name, oa, os_, depth + 1, path + ["<orelse>"])
            continue
        FOUND["real"].append((name, path, tag, [head(x) for x in av], [head(x) for x in sv]))


def find(tree, kind, nm=None):
    for n in ast.walk(tree):
        if kind == "def" and isinstance(n, ast.FunctionDef) and n.name == nm:
            return n
        if kind == "for" and isinstance(n, ast.For) and isinstance(n.target, ast.Tuple):
            if [e.id for e in n.target.elts if isinstance(e, ast.Name)] == \
                    ["blk_label", "parcels_in_blk"]:
                return n
        if kind == "entryfor" and isinstance(n, ast.For) \
                and isinstance(n.target, ast.Name) and n.target.id == "entry" \
                and isinstance(n.iter, ast.Name) and n.iter.id == nm:
            return n
    return None


def main():                                                      # noqa: C901
    os.makedirs(OUTDIR, exist_ok=True)
    name = os.environ.get("WV_OUT_NAME") or "probe_WG9189_S6_replica.log"
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)

    src_a = open(APP, encoding="utf-8").read()
    src_s = open(STG, encoding="utf-8").read()
    TA, TS = ast.parse(src_a), ast.parse(src_s)

    say("=" * 124)
    say("【W-G.9-189 S-6】複刻區同步閘——AST 正規化對拍 ＋ 遞迴下鑽（⛔ 零生產碼）")
    say("=" * 124)
    say("  母體 ＝ app.py（%d 列）／verify/stepg_pipeline.py（%d 列）之四組對應區"
        % (len(src_a.splitlines()), len(src_s.splitlines())))
    say("  界定 ＝ AST FunctionDef／For 節點（⛔ 非自陳之舊行號「約 14650-15450」）")
    say("  正規化 ＝ ①縮排(AST天然) ②註解/docstring(逐層剝) ③ns[\"X\"]→X ＋ st.session_state→ss")
    say("")

    PAIRS = [("_build_g_row", find(TA, "def", "_build_g_row"), find(TS, "def", "_build_g_row")),
             ("_solve_one", find(TA, "def", "_solve_one"), find(TS, "def", "_solve_one")),
             ("_advance_block_with_split", find(TA, "def", "_advance_block_with_split"),
              find(TS, "def", "_advance_block_with_split")),
             ("逐街廓迴圈", find(TA, "for"), find(TS, "for"))]

    for nm, na, ns_ in PAIRS:
        say("─" * 124)
        if na is None or ns_ is None:
            say("🛑 %s：一側取不到 ⇒ 逐字具名，⛔ 不以推定代之" % nm)
            continue
        A, S = normalize(na), normalize(ns_)
        eq = sig(A) == sig(S)
        say("■ %-26s app @%-6d／stepg @%-5d　正規化後全等 = %-5s（dump %d B vs %d B）"
            % (nm, na.lineno, ns_.lineno, eq, len(sig(A)), len(sig(S))))
        if eq:
            say("   ⇒ ✅ **零分歧**")
            continue
        n0 = (len(FOUND["real"]), len(FOUND["st"]))
        walk(nm, body_of(A), body_of(S), 0, [])
        say("   ⇒ 本區新增：實質差 %d ／ st.* 略去 %d"
            % (len(FOUND["real"]) - n0[0], len(FOUND["st"]) - n0[1]))

    say("")
    say("═" * 124)
    say("■ `st.*` 略去：共 %d 處" % len(FOUND["st"]))
    for nm, p, hs in FOUND["st"]:
        say("   [%s] %s" % (nm, " › ".join(p) or "<頂層>"))
        for h in hs[:2]:
            say("        ▸ %s" % h)
    say("")
    say("■ 🔴 **實質差**：共 %d 處" % len(FOUND["real"]))
    for i, (nm, p, tag, av, sv) in enumerate(FOUND["real"], 1):
        say("   %2d. [%s] %s　（%s）" % (i, nm, " › ".join(p) or "<頂層>", tag))
        for h in av[:3]:
            say("        app ▸ %s" % h)
        if len(av) > 3:
            say("        app ▸ …（另 %d 句）" % (len(av) - 3))
        for h in sv[:3]:
            say("        stg ▸ %s" % h)
        if len(sv) > 3:
            say("        stg ▸ …（另 %d 句）" % (len(sv) - 3))

    # ── 🔑 遞補所在之二迴圈：單獨下鑽並釘出唯一分歧之逐字 ────────────────
    say("")
    say("═" * 124)
    say("🔑 **遞補所在之二迴圈**（`for entry in left_group:`／`right_group:`）之單獨下鑽")
    say("   （🛑 本區即 `K-9-17` 遞補之落點 ⇒ 其分歧最具決定性）")
    for grp in ("left_group", "right_group"):
        la, ls = find(TA, "entryfor", grp), find(TS, "entryfor", grp)
        if la is None or ls is None:
            say("   🛑 %s：一側取不到" % grp)
            continue
        A, S = normalize(la).body, normalize(ls).body
        sa = [sig(x) for x in A]
        ss_ = [sig(x) for x in S]
        say("")
        say("── for entry in %s　app @%d／stepg @%d　正規化後 body：app %d 句／stepg %d 句／全等 = %s"
            % (grp, la.lineno, ls.lineno, len(A), len(S), sa == ss_))
        sm = difflib.SequenceMatcher(None, sa, ss_)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            say("   [%s] app[%d:%d]／stepg[%d:%d]" % (tag, i1, i2, j1, j2))
            for k in range(i1, i2):
                say("     ── app 側敘述 #%d（正規化後 unparse）──" % k)
                for ln in ast.unparse(A[k]).splitlines():
                    say("        " + ln[:150])
            for k in range(j1, j2):
                say("     ── stepg 側敘述 #%d（正規化後 unparse）──" % k)
                for ln in ast.unparse(S[k]).splitlines():
                    say("        " + ln[:150])

    # ── 判別力（🛑 ⛔ 不得省·`常規八 二 ②`）────────────────────────────
    say("")
    say("── 判別力對照（證比對器**非恆綠**）──")
    base = ast.unparse(normalize(find(TA, "def", "_build_g_row")))
    mut = base.replace("round(", "int(", 1)
    say("   注入：`_build_g_row` 之首個 `round(` → `int(`（必然改語意）")
    say("   源碼相同 = %s（須 False）／AST 仍判全等 = %s（須 False）%s"
        % (mut == base, sig(ast.parse(base)) == sig(ast.parse(mut)),
           "✅" if (mut != base and sig(ast.parse(base)) != sig(ast.parse(mut))) else "🔴"))
    say("")
    say("═" * 124)
    say("🛑 `X-1` 之判：**實質差 %d 處** ⇒ %s"
        % (len(FOUND["real"]), "🛑 **觸發·停機上呈**" if FOUND["real"] else "✅ 未觸發"))
    say("═" * 124)

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n  ✅ 已落檔：%s" % path)
    return 1 if FOUND["real"] else 0


if __name__ == "__main__":
    sys.exit(main())
