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
import platform
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
    say("  🔒 直譯器 ＝ CPython %s ｜ 🛑 下列 `ast.dump` 之 **bytes ⛔ 非跨環境錨**"
        "（`3.12.3` 與 `3.13.11` 得數不同，而**判定與實質差處數逐項相同**）"
        "⇒ **只對拍判定與差數**（`W-G.9-190R §八-2 4.`·⛔ 不鑄號）" % platform.python_version())
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


# ═══════════════════════════════════════════════════════════════════════════
# 🆕 **`S-6` 四分分類器**（`W-G.9-188 裁 一`／`W-G.9-190R §十`·**末端追加**）
#
# 🛑 **本區塊置於 `if __name__ == "__main__":` <u>之後</u>** ⇒ 以腳本執行本檔時，
#    `sys.exit(main())` 已先終止 ⇒ **既有判定路徑逐位未動、且⛔ 不受本區塊影響**
#    （`§十一-3` 禁改「既有判定路徑」·末端追加除外）。其入口係 `import` 本模組後呼叫
#    `classify4_main()`（驅動檔 ＝ `verify/probes/probe_WG9190R_class4.py`）。
#
# **四分之判準（🛑 機檢可判·⛔ 不得逐案裁量）**
#   乙 宿主介面差：**封閉白名單** ＝ `st.<...>` 之呼叫／`with st.<...>`／`ss[...]` 之寫入／
#                  `raise RuntimeError(...)` ↔ `st.error(...)` ＋ `st.stop()`。
#                  🛑 **名單外之任一<u>識別符</u> ⇒ 歸甲**（單 `§十` 逐字）——
#                  受檢之識別符集取**二側之對稱差**（CC 之實作解·見 `_c4_classify` 內之逐字）。
#   丙 單側獨有守備：僅 `insert`／`delete`（一側全無）者；再以 **AST def-use** 機檢——
#                  獨有碼所**寫回**之名，若為**共用流程**（該區之相同敘述）所**讀**，⇒ 歸甲。
#   丁 呼叫序差：僅**無裝飾器**之 `FunctionDef`／`ClassDef` 之重排得豁免；其餘 ⇒ 歸甲。
#   甲 其餘：🛑 **停機款**。
#
# 🔑 **判別力造（⛔ 不可省）**：於白名單區內注入一已知實質差（把某 `st.error(...)` 之引數
#    改為一**真實運算**），須**仍判甲**。恆判乙丙 ⇒ 分類器紅、⛔ 不得入倉。
# ═══════════════════════════════════════════════════════════════════════════

_C4_WL_ROOT = ("st", "ss")          # 封閉白名單之根識別符
_C4_WL_RAISE = ("RuntimeError",)    # `raise RuntimeError(...)` ↔ `st.error`+`st.stop`
# 🔒 白名單之**屬性名**（`st.<attr>`／`ss.<attr>`）——單 `§十` 之 `st.*`／`ss[...]` 所涵蓋
_C4_WL_ATTR = ("error", "stop", "info", "warning", "success", "caption", "write",
               "dataframe", "markdown", "setdefault", "get", "session_state")


def _c4_is_whitelist_stmt(n):
    """該敘述是否落在**封閉白名單**內（⛔ 名單外之任一形即否）。"""
    # `st.<...>(...)` 之單獨呼叫
    if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
        f = n.value.func
        while isinstance(f, ast.Attribute):
            f = f.value
        if isinstance(f, ast.Name) and f.id in _C4_WL_ROOT:
            return True
    # `with st.<...>:`
    if isinstance(n, ast.With):
        for it in n.items:
            f = it.context_expr
            if isinstance(f, ast.Call):
                f = f.func
            while isinstance(f, ast.Attribute):
                f = f.value
            if isinstance(f, ast.Name) and f.id in _C4_WL_ROOT:
                return True
        return False
    # `ss[...] = …` ／ `ss.setdefault(...)[...] = …`
    if isinstance(n, ast.Assign):
        for tg in n.targets:
            r = tg
            while isinstance(r, (ast.Subscript, ast.Attribute)):
                r = r.value
            if isinstance(r, ast.Call):
                f = r.func
                while isinstance(f, ast.Attribute):
                    f = f.value
                r = f
            if isinstance(r, ast.Name) and r.id in _C4_WL_ROOT:
                return True
        return False
    # `raise RuntimeError(...)`
    if isinstance(n, ast.Raise) and n.exc is not None:
        e = n.exc
        if isinstance(e, ast.Call):
            e = e.func
        if isinstance(e, ast.Name) and e.id in _C4_WL_RAISE:
            return True
    return False


def _c4_all_names(nodes):
    """該組敘述內之**全部識別符**（`Name.id` ＋ `Attribute.attr`·⛔ 不分 ctx）。"""
    out = set()
    for n in nodes:
        for m in ast.walk(n):
            if isinstance(m, ast.Name):
                out.add(m.id)
            elif isinstance(m, ast.Attribute):
                out.add(m.attr)
    return out


def _c4_names(nodes, ctx):
    out = set()
    for n in nodes:
        for m in ast.walk(n):
            if isinstance(m, ast.Name) and isinstance(m.ctx, ctx):
                out.add(m.id)
    return out


def _c4_is_plain_def(n):
    return (isinstance(n, (ast.FunctionDef, ast.ClassDef))
            and not getattr(n, "decorator_list", []))


def _c4_walk(name, a_body, s_body, depth, path, acc):
    """與 `walk()` 同構之遞迴，惟**保留 AST 節點**以供分類（⛔ 不改 `walk()` 一字）。"""
    sm = difflib.SequenceMatcher(None, [sig(x) for x in a_body], [sig(x) for x in s_body])
    common = [a_body[i] for tag, i1, i2, _j1, _j2 in sm.get_opcodes()
              if tag == "equal" for i in range(i1, i2)]
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        av, sv = a_body[i1:i2], s_body[j1:j2]
        if av and not sv and all(is_st(x) for x in av):
            continue                      # `st.*` 略去（既有路徑已另計）
        if len(av) == 1 and len(sv) == 1 and depth < MAXDEPTH \
                and type(av[0]) is type(sv[0]) and head(av[0]) == head(sv[0]) \
                and body_of(av[0]) and body_of(sv[0]):
            _c4_walk(name, body_of(av[0]), body_of(sv[0]), depth + 1,
                     path + [head(av[0]).strip()[:60]], acc)
            oa = list(getattr(av[0], "orelse", []) or [])
            os_ = list(getattr(sv[0], "orelse", []) or [])
            if oa or os_:
                _c4_walk(name, oa, os_, depth + 1, path + ["<orelse>"], acc)
            continue
        acc.append({"name": name, "path": list(path), "tag": tag,
                    "av": av, "sv": sv, "common": common})


def _c4_classify(item):
    """回 (類, 理由)。🛑 機檢可判·⛔ 不得逐案裁量。"""
    av, sv, common = item["av"], item["sv"], item["common"]
    allst = av + sv
    # ── 乙：封閉白名單 ────────────────────────────────────────────
    #   🛑 **判準係「識別符」、⛔ 非「敘述形」**（單 `§十` 逐字：「名單外之任一**識別符**
    #      ⇒ 歸甲」）。🩸 **本器首版誤實作為敘述形之判**，致判別力造之注入
    #      （`st.error(f'x')` ↔ `st.error(_dev * 2 + _tol_lot)`）**逃過而判乙** ⇒ 分類器紅。
    #   🔒 **CC 之實作解（工程裁·`§零-2`「純技術自行做完」·逐字呈裁）**：受檢之識別符集
    #      取**二側之<u>對稱差</u>**（⛔ 非聯集）——理由：「宿主介面差」之受詞係**差異本身**；
    #      二側**相同**之訊息負載（如 `blk_label`）⛔ 非介面差之一部。
    #      ⇒ 注入案之對稱差 ＝ {`_dev`, `_tol_lot`} ⊄ 白名單 ⇒ **判甲** ✅；
    #        而真實之 `st.error(f"…")`+`st.stop()` ↔ `raise RuntimeError(f"…")`（負載相同）
    #        其對稱差 ＝ {`st`, `RuntimeError`} ⊆ 白名單 ⇒ **判乙** ✅。
    #      🛑 若發單側認本解過寬，改採**聯集**即可（一行之改），惟屆時類乙將近乎不可達。
    _WL = set(_C4_WL_ROOT) | set(_C4_WL_RAISE) | set(_C4_WL_ATTR)
    _na = _c4_all_names(av)
    _ns = _c4_all_names(sv)
    _sym = (_na | _ns) - (_na & _ns)
    if allst and all(_c4_is_whitelist_stmt(n) for n in allst) and (_sym <= _WL):
        return "乙", ("全部敘述皆落於封閉白名單，且二側識別符之**對稱差** %s ⊆ 白名單"
                      % (sorted(_sym) or "（空）"))
    if allst and all(_c4_is_whitelist_stmt(n) for n in allst):
        return "甲", ("敘述形雖落白名單，惟二側識別符之**對稱差** %s **⊄ 白名單** ⇒ 歸甲"
                      % sorted(_sym - _WL))
    # ── 丁：僅無裝飾器之 def/class 重排 ──
    if av and sv and all(_c4_is_plain_def(n) for n in allst):
        na = sorted(getattr(n, "name", "") for n in av)
        ns_ = sorted(getattr(n, "name", "") for n in sv)
        if na == ns_:
            return "丁", "僅**無裝飾器**之 `FunctionDef`／`ClassDef` 之重排（名集相同）"
        return "甲", "def/class 之名集不同（%s vs %s）⇒ ⛔ 非單純重排" % (na, ns_)
    # ── 丙：單側獨有 ＋ def-use 機檢 ──
    if (av and not sv) or (sv and not av):
        own = av if av else sv
        stores = _c4_names(own, ast.Store)
        loads_common = _c4_names(common, ast.Load)
        bad = sorted(stores & loads_common)
        if bad:
            return "甲", ("單側獨有碼**寫回**了共用流程所讀之名 ⇒ def-use 判甲：%s" % bad)
        return "丙", ("單側獨有守備；其所寫回之名 %s **⛔ 未**為共用流程所讀"
                      % (sorted(stores) or "（無）"))
    return "甲", "⛔ 不落於乙／丙／丁之任一機械判準"


def classify4(src_a=None, src_s=None):
    """對四組對應區之**實質差**逐項四分。回 (items, 統計)。"""
    src_a = src_a if src_a is not None else open(APP, encoding="utf-8").read()
    src_s = src_s if src_s is not None else open(STG, encoding="utf-8").read()
    TA, TS = ast.parse(src_a), ast.parse(src_s)
    PAIRS = [("_build_g_row", find(TA, "def", "_build_g_row"), find(TS, "def", "_build_g_row")),
             ("_solve_one", find(TA, "def", "_solve_one"), find(TS, "def", "_solve_one")),
             ("_advance_block_with_split", find(TA, "def", "_advance_block_with_split"),
              find(TS, "def", "_advance_block_with_split")),
             ("逐街廓迴圈", find(TA, "for"), find(TS, "for"))]
    acc = []
    for nm, na, ns_ in PAIRS:
        if na is None or ns_ is None:
            continue
        A, S = normalize(na), normalize(ns_)
        if sig(A) == sig(S):
            continue
        _c4_walk(nm, body_of(A), body_of(S), 0, [], acc)
    out = []
    for it in acc:
        cls, why = _c4_classify(it)
        out.append((cls, it["name"], " › ".join(it["path"]) or "<頂層>", it["tag"], why,
                    [head(x) for x in it["av"]][:2], [head(x) for x in it["sv"]][:2]))
    stat = {}
    for c, *_ in out:
        stat[c] = stat.get(c, 0) + 1
    return out, stat


def classify4_main():                                            # noqa: C901
    """入口（供驅動檔呼叫）。回 `rc`：判別力造未判甲 ⇒ `1`（`§十一-1` 停機款 `10`）。"""
    say("=" * 124)
    say("【W-G.9-190R commit 5】`S-6` 四分分類器（`W-G.9-188 裁 一`）— ⛔ 零生產碼")
    say("=" * 124)
    say("  🛑 判準（機檢可判·⛔ 不得逐案裁量）：")
    say("     乙 ＝ **封閉白名單**（`st.<...>` 呼叫／`with st.<...>`／`ss[...]` 寫入／"
        "`raise RuntimeError`）·**名單外之任一敘述形 ⇒ 歸甲**")
    say("     丙 ＝ 單側獨有 ＋ **AST def-use**：所寫回之名若為共用流程所讀 ⇒ **歸甲**")
    say("     丁 ＝ 僅**無裝飾器**之 `FunctionDef`／`ClassDef` 重排（名集須相同）")
    say("     甲 ＝ 其餘（🛑 停機款）")
    say("")
    items, stat = classify4()
    say("── 逐項四分（共 %d 項）──" % len(items))
    for i, (cls, nm, path, tag, why, av, sv) in enumerate(items, 1):
        say("  %2d. [%s] %s › %s（%s）" % (i, cls, nm, path, tag))
        say("        理由：%s" % why)
        for h in av:
            say("        app ▸ %s" % h)
        for h in sv:
            say("        stg ▸ %s" % h)
    say("")
    say("── 統計 ──")
    for c in ("甲", "乙", "丙", "丁"):
        say("  類 %s：%d 項" % (c, stat.get(c, 0)))
    say("  🛑 **類甲數 ＝ %d**（`§十` 之**預期為 `0`**·🛑 **預測·⛔ 非停機款**）"
        % stat.get("甲", 0))
    if stat.get("甲", 0):
        say("  ⇒ 依 `§十` 逐字：仍有類甲 ⇒ **逐項具名呈裁**，"
            "⛔ 不自行豁免、⛔ 不改白名單以求綠。")
    say("")

    # ── 🔑 判別力造（⛔ 不可省·`§十一-1` 停機款 10）──────────────────
    say("── 🔑 判別力造：於白名單區內注入一已知實質差，須**仍判甲** ──")
    inj_a = ast.parse("st.error(f'x')").body
    inj_s = ast.parse("st.error(_dev * 2 + _tol_lot)").body   # 引數改為**真實運算**
    fake = {"name": "<judge>", "path": [], "tag": "replace",
            "av": inj_a, "sv": inj_s, "common": []}
    cls, why = _c4_classify(fake)
    say("     注入：`st.error(f'x')` ↔ `st.error(_dev * 2 + _tol_lot)`（引數係真實運算）")
    say("     ⇒ 判為 **類 %s**（%s）" % (cls, why))
    ok = (cls == "甲")
    say("     🛑 判別力之判：%s"
        % ("✅ **仍判甲** ⇒ 分類器⛔ 非恆判乙丙" if ok
           else "🔴 **未判甲 ⇒ 分類器紅·⛔ 不得入倉**（`§十一-1` 停機款 `10`）"))
    say("")
    say("=" * 124)
    say("🛑 總判：判別力造 %s ／ 類甲 %d 項（⛔ 非停機款·逐項具名呈裁）"
        % ("✅ 過" if ok else "🛑 **紅**", stat.get("甲", 0)))
    say("=" * 124)
    return 0 if ok else 1
