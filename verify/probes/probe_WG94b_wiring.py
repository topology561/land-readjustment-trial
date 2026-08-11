# -*- coding: utf-8 -*-
"""`W-G.9-4b` §1 探針：命題 **P** 之**由構造**雙證（AST ＋ 實際呼叫）。

## 命題 P（`docs/reports/W-G.9-4b_前置登記.md` §1）

> 於 app 生產路徑（UI 鈕「執行七級調配」`app.py:21931` → `_build_wf_ctx`
> → `_wf_ns()` → `wf_f0.compute` → `run_step_g`），`ns["k956_W_from_mp"]`
> 拋 `KeyError` ⇒ 七級調配全鏈無法產出。

## 為何須雙證（⛔ 非僅 grep）

`grep` 只證「該字面存在於某行」，**不證其會被執行**——若該行落於 `Try`／`If`
之內，P 即為偽。故：

* **A 層（AST）**：證 `stepg` 之 `ns["k956_W_from_mp"]` 落於 `run_step_g` 函式體、
  且其**祖先鏈上無** `Try`／`If`／`ExceptHandler`／`While`／`For` ⇒ **無條件執行**。
* **B 層（實際呼叫）**：以 `_wf_ns()`（⛔ 非 `harvest()` 全 globals）建出之受限 ns
  實跑 `run_step_g` ⇒ 觀測其**是否實拋** `KeyError`，並記其**鍵名**與**發生行號**。

⛔ 本探針**零碼改動**（獨立 script·不注入 app／verify 引擎）。

## 重跑
    python verify/probes/probe_WG94b_wiring.py
"""
import ast
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

OUT_LOG = os.path.join(VERIFY, "out", "probe_WG94b_wiring.log")
TARGET = "k956_W_from_mp"
L = []


def say(s=""):
    print(s)
    L.append(s)


# ══════════════════════════════════════════════════════════════════════════
# A 層：AST — `ns[<字面字串>]` 之取用點 ＋ 祖先鏈條件性判定
# ══════════════════════════════════════════════════════════════════════════
BLOCKING = (ast.Try, ast.ExceptHandler, ast.If, ast.While, ast.For,
            ast.AsyncFor, ast.With, ast.AsyncWith, ast.IfExp)


def ns_subscripts(path):
    """回傳 [(name, lineno, [祖先節點…])]；字樣＝**任何** `ns[<字面字串>]`（⛔ 不預設符號名）。"""
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    parent = {}
    for node in ast.walk(tree):
        for ch in ast.iter_child_nodes(node):
            parent[ch] = node
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Subscript):
            continue
        if not (isinstance(node.value, ast.Name) and node.value.id == "ns"):
            continue
        sl = node.slice
        if not (isinstance(sl, ast.Constant) and isinstance(sl.value, str)):
            continue
        chain, cur = [], parent.get(node)
        while cur is not None:
            chain.append(cur)
            cur = parent.get(cur)
        hits.append((sl.value, node.lineno, chain))
    return hits


def layer_A():
    say("=" * 96)
    say("【A 層】AST：`ns[<字面字串>]` 取用點之條件性判定（⛔ 不預設符號名）")
    say("=" * 96)
    p = os.path.join(VERIFY, "stepg_pipeline.py")
    hits = [h for h in ns_subscripts(p) if h[0] == TARGET]
    say(f"  檔：verify/stepg_pipeline.py")
    say(f"  `ns[\"{TARGET}\"]` 取用點數 ＝ {len(hits)}")
    if not hits:
        say(f"  🔴 母體為 0 ⇒ **不得算通過**（空真假綠）")
        return False, "AST 取用點 0"
    ok_all = True
    for name, lineno, chain in hits:
        fdefs = [c for c in chain if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef))]
        enclosing = fdefs[0].name if fdefs else "(module level)"
        # 祖先鏈中、位於「最內層 FunctionDef 之內」的條件性節點
        inner = []
        for c in chain:
            if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef)):
                break
            if isinstance(c, BLOCKING):
                inner.append(type(c).__name__)
        say(f"    :{lineno}  所屬函式 ＝ `{enclosing}`")
        say(f"           祖先鏈上之條件性節點（函式體內）＝ {inner if inner else '(無)'}")
        if inner:
            ok_all = False
    say(f"  ⇒ A 層判定：{'✅ 無條件執行' if ok_all else '🔴 為條件式（P 可能為偽）'}")
    return ok_all, ("無條件執行" if ok_all else f"落於 {inner}")


# ══════════════════════════════════════════════════════════════════════════
# B 層：實際呼叫 — 以 `_wf_ns()` 建出之受限 ns 跑 `run_step_g`
# ══════════════════════════════════════════════════════════════════════════
def layer_B():
    say()
    say("=" * 96)
    say("【B 層】實際呼叫：ns 由 `_wf_ns()` 建出（⛔ 非 harvest 全 globals）")
    say("=" * 96)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    snapshot = rv.load_snapshot()
    ns_full, fake_st = harvest()
    say(f"  harvest 全 globals 名目數 ＝ {len(ns_full)}")
    ns_app = ns_full["_wf_ns"]()          # ⇦ 受詞：app 生產路徑之 ns
    say(f"  `_wf_ns()` 受限 ns 名目數 ＝ {len(ns_app)}")
    say(f"  `\"{TARGET}\" in _wf_ns()` ⇒ {TARGET in ns_app}")
    say(f"  `\"{TARGET}\" in harvest()` ⇒ {TARGET in ns_full}   ← 二路徑分岔即缺陷所在")

    # ── 建置（**逐行同 `verify/wg_g1_smoke.py::main`**·⛔ 非另寫平行式）──
    setback, tag = 0.0, "0m"
    cb_by, cad = rv.build_pipeline(ns_full, fake_st, snapshot)
    params = rv.build_param_table(ns_full, fake_st, cb_by, cad, snapshot, setback)
    build_ownership(ns_full, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns_full, fake_st, v6, list(cb_by.values()), snapshot)
    _d, _s, _o, winners, forced = run_corner_pk(
        ns_full, fake_st, list(cb_by.values()), cad, params, temp, build,
        setback, snapshot=snapshot)
    say(f"  建置完成（tag={tag}）：cb {len(cb_by)} 塊、build {len(build)} 宗")
    say("  ⚠️ 建置階段用 harvest 全 ns（harness 函式所需）；受詞為其後之**受限 ns**")

    args = (fake_st, list(cb_by.values()), cad, snapshot,
            params, build, winners, forced, setback)

    # ── B-0：**對照組**（全 ns）——確立「既有另案」之落點與錨值 ──────────────
    #   ⛔ 非本批所引入：`verify/out/WG94_runall.log` 之 `v3·StepG0m/3.5m（結構閘/看守觸發）`
    #   已為既有 FAIL。本組之作用 ＝ 證明 ns 解包**通過**後才撞另案 ⇒ 二失敗互不相干。
    say()
    say("  → [B-0·對照組] run_step_g(ns=harvest 全 ns, …)   ＝ 既有另案之落點")
    b0 = _witness(lambda: run_step_g(ns_full, *args), expect_key=None)

    # ── B-2：受詞（`_wf_ns()` 受限 ns 直呼·定位發生行）─────────────────────
    #   🔒 **判準自適應**（⛔ 非事後放寬·二態於事前登記 `F1`／`F2`＋`F3` 各自寫死）：
    #     · 清單**未含**該名（修復前）⇒ 須實拋 `KeyError: TARGET` ＝ `F1`（命題 P）。
    #     · 清單**已含**該名（修復後）⇒ 須與 **B-0 落於同一點** ＝ `F2`／`F3`
    #       （受限 ns 已足供引擎；其後之落點係既有另案、與 ns 無關）。
    _post = TARGET in ns_app
    say()
    say(f"  → [B-2·受詞] run_step_g(ns=`_wf_ns()` 受限 ns, …)   ｜清單已含該名 ⇒ {_post}")
    b2 = _witness(lambda: run_step_g(ns_app, *args),
                  expect_key=(None if _post else TARGET))

    say()
    say(f"     B-0（全 ns）  落點 ＝ {b0[1]}")
    say(f"     B-2（受限 ns）落點 ＝ {b2[1]}")
    if _post:
        _same = (b0[1] == b2[1])
        say(f"  {'✅' if _same else '🔴'} **修復後判準**：二落點{'相同' if _same else '不同'}"
            f" ⇒ 受限 ns {'已足供引擎（`F2`／`F3` 之碼面證據）' if _same else '仍不足'}")
        b2 = (_same, b2[1])
    else:
        say("  🔒 **二失敗之先後**：受限 ns 之 KeyError 落於 ns 解包段（`stepg` 之 `ns[...]` 區），"
            "而另案之 RuntimeError 落於結構閘——後者行號**大於**前者 ⇒ **KeyError 先發**。")

    # ── B-1：真 app 路徑（`_build_wf_ctx`→`wf_f0.compute`）**無法執行**之具名理由 ──
    say()
    say("  ⛔ **[B-1] 真 app 路徑（`_build_wf_ctx` → `wf_f0.compute`）本批無法執行**——")
    say("     `_build_wf_ctx` 之 seed 需 `f3_G_values`（＝ `run_step_g` 之 `g_rows`），")
    say("     而 `run_step_g` 於**兩情境皆** raise（B-0）⇒ 取不到。")
    say("     ⛔ **不以偽造 seed 代替**（fixture-provenance：期望值/輸入須有獨立真相源）。")
    say("     ⇒ B-1 之缺席**已正面列出**，⛔ 不作靜默略過。")

    return b2[0], f"B-2 {b2[1]}｜B-0(另案) {b0[1]}"


def _witness(fn, *, expect_key):
    """跑 fn，把**實際發生什麼**逐項印出（⛔ 不吞例外·全文入 log）。

    `expect_key is None` ⇒ 只記錄落點（對照組）；否則須為該鍵之 `KeyError` 才算證成。
    回 (是否證成, 落點敘述)。
    """
    try:
        fn()
        say("     ⚠️ **未拋例外**（完整跑完）")
        return (expect_key is None), "未拋（完整跑完）"
    except BaseException as e:                       # ⛔ 不分型別先全收 → 印全文 → 再分類
        tb = traceback.extract_tb(sys.exc_info()[2])
        last = tb[-1]
        where = f"{os.path.basename(last.filename)}:{last.lineno}"
        say(f"     實拋 {type(e).__name__}｜落點 ＝ {where}")
        say(f"        該行原文 ＝ {(last.line or '').strip()[:110]}")
        _msg = str(e).replace("\n", " ")[:220]
        say(f"        訊息 ＝ {_msg}")
        if expect_key is None:
            return True, f"{type(e).__name__} @ {where}"
        ok = isinstance(e, KeyError) and e.args and e.args[0] == expect_key
        if not ok:
            say(f"     🔴 非期望之 `KeyError: {expect_key!r}` ⇒ 不足以證 P")
        else:
            say(f"     ✅ 即期望之 `KeyError: {expect_key!r}`")
        return bool(ok), f"{type(e).__name__} @ {where}"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    say(f"# `W-G.9-4b` §1 探針：命題 P 之由構造雙證（目標鍵 `{TARGET}`）")
    say()
    okA, whyA = layer_A()
    okB, whyB = layer_B()
    say()
    say("=" * 96)
    say(f"【判定】A 層 ＝ {'✅' if okA else '🔴'}（{whyA}）")
    say(f"       B 層 ＝ {'✅' if okB else '🔴'}（{whyB}）")
    verdict = okA and okB
    say(f"⇒ 命題 **P** ＝ {'**真**（F1 成立·續 §2 工項）' if verdict else '**偽 / 未證**（⇒ S′-1 停機上呈）'}")
    say("=" * 96)
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT_LOG, REPO)}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
