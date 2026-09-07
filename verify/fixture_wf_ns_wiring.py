# -*- coding: utf-8 -*-
"""`W-G.9-4b`：**app 接線清單 `_WF_NS_NAMES` ↔ 引擎 `ns[...]` 消費**之守護夾具。

## 存在理由（⛔ 非「再加一道保險」——現行守備確有洞）

`W-G.9-4` 於 `verify/stepg_pipeline.py` 加入 `ns["k956_W_from_mp"]`，
但**未**把該名列入 `app.py` 之 `_WF_NS_NAMES` ⇒ app 生產路徑
（「執行七級調配」→ `_build_wf_ctx` → `_wf_ns()` → `wf_f0.compute` → `run_step_g`）
之 ns 取不到該名 ⇒ **`KeyError` 於 `stepg_pipeline.py` 之 ns 解包段**
（實測見 `verify/out/probe_WG94b_wiring.log`）。

**該缺陷本應由既有之 W-8 反向閘攔下**（`verify/run_verification.py` 之
「W-G G.1 接線層 ctx-builder 同源」內），惟該閘於到達差集檢查**之前**
即因 `_ctx["0m"]` 缺鍵而崩（`verify/out/WG94_runall.log` 之
`🔴 FAIL  W-G G.1 …` ／ `[G.1] '0m'`）⇒ **閘在、但為死閘**。

⚠️ 本夾具**繞過**該死閘、**不修**它——上游 `'0m'` 屬另案
（其根因＝`run_step_g` 之結構閘 raise，見下「另案」節），`W-G.9-4b` §3 明文不修。

## 另案（⛔ 本夾具**不得**因它而變紅，亦**不得**因它而放水）

`verify/out/WG94_runall.log` 之 `v3·StepG0m`／`v3·StepG3.5m`（結構閘/看守觸發）
為**既有 FAIL**：`run_step_g` 於**兩情境皆** raise `RuntimeError`（街廓 R1 left
「理論@k* ≠ 實跑」）。該 raise 落於 **ns 解包段之後**。
⇒ 動態層之判準寫成「**ns 解包段是否通過**」（＝有無 `ns[...]` 之 `KeyError`），
   ⛔ 而非「`run_step_g` 是否成功」——後者在本倉態下**恆假**，會使本夾具永紅而失去意義。

## 三層（⛔ 缺一不可）

| 層 | 內容 |
|---|---|
| **靜態** | AST 取引擎檔之 `ns[<字面字串>]` 取用點，與 `_WF_NS_NAMES` 取差集；非空即紅 |
| **動態** | 以 **`_wf_ns()`**（⛔ 非 `harvest()` 全 globals）建 ns，**實跑** `run_step_g` |
| **竄改自檢** | 自清單抽掉一名 ⇒ 二層皆須轉紅；還原 ⇒ 轉綠。**兩態皆印入本輸出** |

⛔ **空集合不算通過**：`ns[...]` 母體為 0 ⇒ 自判紅（「空真假綠」病灶）。

## 重跑
    python verify/fixture_wf_ns_wiring.py        # rc=0 ⇒ 綠
"""
import ast
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

# 【目錄射程】硬判之檔集 ＝ **app 路徑實際執行**之引擎檔。
#   採 `run_verification.py` W-8 反向閘之既有檔集（其排除 `selection_pipeline.py` 之
#   理由已記於該處：該檔僅走 harness 全 harvest、非 `_wf_ns()` 路徑）。
#   ⚠️ 更寬之 import 遞移閉包另行**列示**（見下 `_closure`），⛔ 不靜默截斷。
HARD_FILES = ("wf_f0.py", "wf_f1.py", "wf_f2.py", "wf_f3.py", "wf_f4.py",
              "stepg_pipeline.py")
APP_PY = os.path.join(REPO, "app.py")
RC = [0]


def red(msg):
    print(f"  🔴 {msg}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
# 【字樣射程】＋【連接方式】：AST 之 `ns[<字面字串>]`
# ══════════════════════════════════════════════════════════════════════════
def ns_uses(path):
    """回 {name: [(lineno, 所屬函式)]}。

    【字樣射程】＝**任何** `ns[<字面字串>]`——⛔ 不預設任何符號名、
      ⛔ 不列舉已知名單（否則新加的名正好是抓不到的那個）。
    【連接方式】＝**AST 之 `Subscript(value=Name('ns'), slice=Constant(str))`**
      ——結構匹配，⛔ 非正則、⛔ 無固定距離窗 `.{0,N}`。
    """
    tree = ast.parse(open(path, encoding="utf-8").read())
    fn_of = {}
    for fn in ast.walk(tree):
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for sub in ast.walk(fn):
                fn_of.setdefault(id(sub), fn.name)
    out = {}
    for node in ast.walk(tree):
        if (isinstance(node, ast.Subscript)
                and isinstance(node.value, ast.Name) and node.value.id == "ns"
                and isinstance(node.slice, ast.Constant)
                and isinstance(node.slice.value, str)):
            out.setdefault(node.slice.value, []).append(
                (node.lineno, fn_of.get(id(node), "(module)")))
    return out


def app_ns_names():
    """讀 `app.py` 之 `_WF_NS_NAMES` 字面（AST·⛔ 不 import app、⛔ 不 exec）。"""
    tree = ast.parse(open(APP_PY, encoding="utf-8").read())
    for node in ast.walk(tree):
        if (isinstance(node, ast.Assign) and node.targets
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "_WF_NS_NAMES"
                and isinstance(node.value, ast.List)):
            return [e.value for e in node.value.elts
                    if isinstance(e, ast.Constant) and isinstance(e.value, str)]
    raise RuntimeError("🔴 app.py 找不到 `_WF_NS_NAMES` 之 list 字面")


def _closure():
    """`HARD_FILES` 於 `verify/` 內之 import 遞移閉包（⛔ 只為**列示**、不判紅）。"""
    seen, stack = set(), list(HARD_FILES)
    while stack:
        f = stack.pop()
        if f in seen or not os.path.exists(os.path.join(HERE, f)):
            continue
        seen.add(f)
        tree = ast.parse(open(os.path.join(HERE, f), encoding="utf-8").read())
        for n in ast.walk(tree):
            mods = []
            if isinstance(n, ast.Import):
                mods = [a.name for a in n.names]
            elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
                mods = [n.module]
            for m in mods:
                cand = m.split(".")[0] + ".py"
                if os.path.exists(os.path.join(HERE, cand)):
                    stack.append(cand)
    return sorted(seen)


# ══════════════════════════════════════════════════════════════════════════
# 靜態層
# ══════════════════════════════════════════════════════════════════════════
def collect_used(files):
    used = {}
    for f in files:
        p = os.path.join(HERE, f)
        if not os.path.exists(p):
            continue
        for name, locs in ns_uses(p).items():
            used.setdefault(name, []).extend((f, ln, fn) for ln, fn in locs)
    return used


def layer_static(listed):
    print("─" * 92)
    print("【靜態層】AST：引擎 `ns[<字面字串>]` 消費 ⊆ app `_WF_NS_NAMES`")
    print("─" * 92)
    print(f"  【目錄射程】硬判 {len(HARD_FILES)} 檔：{', '.join(HARD_FILES)}")
    print(f"              （相對 `verify/`·⛔ 不含 `.claude/worktrees/`）")
    print("  【字樣射程】**任何** `ns[<字面字串>]`——⛔ 不預設符號名、⛔ 不列舉已知名單")
    print("  【連接方式】AST `Subscript(Name('ns'), Constant(str))` 結構匹配"
          "——⛔ 非正則、⛔ 無固定距離窗")
    used = collect_used(HARD_FILES)
    print(f"  引擎消費之相異名 ＝ {len(used)}；app 清單名目 ＝ {len(listed)}")
    if not used:
        red("`ns[...]` 母體 ＝ 0 ⇒ **不得算通過**（空真假綠）")
        return set()
    missing = sorted(set(used) - set(listed))
    if missing:
        red(f"引擎消費但 `_WF_NS_NAMES` 漏列（app 路徑必 KeyError）：{missing}")
        for m in missing:
            for f, ln, fn in used[m]:
                print(f"       {m} ← {f}:{ln}  函式 `{fn}`")
    else:
        print("  ✅ 差集為空（引擎消費 ⊆ 清單）")

    # ── 更寬射程之**列示**（⛔ 不判紅·⛔ 不靜默截斷）──
    clos = _closure()
    extra_files = [f for f in clos if f not in HARD_FILES]
    extra = collect_used(extra_files)
    beyond = sorted(set(extra) - set(listed))
    print(f"  ── 射程外之列示：import 遞移閉包 {len(clos)} 檔，"
          f"硬判範圍外 {len(extra_files)} 檔 ＝ {', '.join(extra_files) or '（無）'}")
    print(f"     其中「消費但未列」之名 ＝ {beyond if beyond else '（無）'}"
          f"　⚠️ **僅列示不判紅**（harness 全 harvest 路徑·非 `_wf_ns()` 路徑）")
    return set(used)


# ══════════════════════════════════════════════════════════════════════════
# 動態層
# ══════════════════════════════════════════════════════════════════════════
_COND = (ast.Try, ast.ExceptHandler, ast.If, ast.IfExp, ast.While, ast.For,
         ast.AsyncFor, ast.With, ast.AsyncWith)


def _stepg_unpack_lines():
    """`run_step_g`／`_run_step_g_impl` 內 `ns[...]` 之 [(行號, 名, 是否無條件)]。

    **「無條件」＝** 該節點至其最內層 `FunctionDef`（須為 `run_step_g` **或** `_run_step_g_impl`）之
    祖先鏈上，⛔ 無 `Try`／`If`／迴圈／`With`，且 ⛔ 無中介之巢狀 `FunctionDef`／`Lambda`。
    🔒 竄改自檢**只能抽無條件者**——抽到條件式者（如階段2 分支之名）在該情境
       根本不執行 ⇒ 竄改態不會轉紅，會誤判本層「無鑑別力」（本夾具首版即如此翻紅）。
    """
    src = open(os.path.join(HERE, "stepg_pipeline.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    parent = {}
    for node in ast.walk(tree):
        for ch in ast.iter_child_nodes(node):
            parent[ch] = node
    out = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Subscript)
                and isinstance(node.value, ast.Name) and node.value.id == "ns"
                and isinstance(node.slice, ast.Constant)
                and isinstance(node.slice.value, str)):
            continue
        uncond, cur = True, parent.get(node)
        fname = "(module)"
        while cur is not None:
            if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                fname = getattr(cur, "name", "<lambda>")
                break
            if isinstance(cur, _COND):
                uncond = False
            cur = parent.get(cur)
        # 🆕 `W-G.9-247`（KL 令 `2026-09-07`·採候裁 `(甲)`）：受詞擴為**薄殼與其 `_impl`**。
        #   🩸 案由：`W-G.9-247` 段乙將 `run_step_g` 拆為「薄殼 ＋ `_run_step_g_impl`」
        #      （其由見該批報告 `§四 a`：單所令之「本體縮排包住」會改寫 `33` 個跨列
        #      字串常數之內容，與同單 `V-1` 互斥）⇒ 全部 `ns[...]` 解包點移入 `_impl`
        #      ⇒ 本函式之母體**歸零**，`layer_dynamic` 遂於解引用處 `IndexError`。
        #   🔒 二名**皆須收**：薄殼日後若自行解包，漏收即回到同一盲區。
        if fname in ("run_step_g", "_run_step_g_impl"):
            out.append((node.lineno, node.slice.value, uncond))
    return sorted(out)


def _run(ns, args):
    """跑 `run_step_g`，回 (是否有 ns 解包之 KeyError, 敘述)。

    ⛔ **非吞例外**：例外之型別、鍵名、落點、訊息一律印出；
    判準只問一事——**ns 解包段是否通過**（見 docstring 之「另案」節）。
    """
    from stepg_pipeline import run_step_g
    unpack = {ln for ln, _n, _u in _stepg_unpack_lines()}
    try:
        run_step_g(ns, *args)
        print("       跑完·未拋例外 ⇒ ns 解包必已通過")
        return False, "未拋"
    except BaseException as e:
        tb = traceback.extract_tb(sys.exc_info()[2])[-1]
        where = f"{os.path.basename(tb.filename)}:{tb.lineno}"
        print(f"       實拋 {type(e).__name__} @ {where}｜{str(e).splitlines()[0][:150]}")
        hit = (isinstance(e, KeyError)
               and os.path.basename(tb.filename) == "stepg_pipeline.py"
               and tb.lineno in unpack)
        return hit, f"{type(e).__name__} @ {where}"


def layer_dynamic():
    print()
    print("─" * 92)
    print("【動態層】ns 由 **`_wf_ns()`** 建出（⛔ 非 `harvest()` 全 globals）·實跑 `run_step_g`")
    print("─" * 92)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk

    unpack = _stepg_unpack_lines()
    uncond = [(ln, n) for ln, n, u in unpack if u]
    # 🆕 `W-G.9-247`（採候裁 `(甲)`）：**空集守衛前移至解引用之前**。
    #   🩸 案由：舊序為「先 `print(unpack[0][0])` 後守衛」⇒ 母體為空時**恆 `IndexError`**，
    #      其所欲之 `red("… 空真假綠")` **結構上不可達** ⇒ 空集之紅被換成一個 traceback。
    #   🔒 通則：**守衛須先於其所守之解引用**；否則該守衛之訊息永不出現。
    if not unpack or not uncond:
        red("`run_step_g`／`_run_step_g_impl` 內 `ns[...]`（或其無條件子集）"
            "母體 ＝ 0 ⇒ 動態層無受詞（空真假綠）")
        return
    print(f"  `run_step_g`／`_run_step_g_impl` 內之 `ns[...]` 解包點 ＝ {len(unpack)} 處"
          f"（行 {unpack[0][0]}–{unpack[-1][0]}）；其中**無條件執行** {len(uncond)} 處")

    snapshot = rv.load_snapshot()
    ns_full, fake_st = harvest()
    setback = 0.0
    print("  ⚠️ **情境射程 ＝ 僅 `0m`**（施工單 §2-3 之「至少一次」）"
          "——⛔ 正面標示，非靜默截斷")
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
    args = (fake_st, list(cb_by.values()), cad, snapshot, params, build,
            winners, forced, setback)
    print("  ⚠️ 建置階段用 harvest 全 ns（harness 函式所需）；"
          "**受詞為 `run_step_g` 所收之受限 ns**")

    ns_app = ns_full["_wf_ns"]()
    print(f"  `_wf_ns()` 受限 ns 名目數 ＝ {len(ns_app)}")
    print("  → [正常態] run_step_g(ns=_wf_ns(), …)")
    bad, why = _run(ns_app, args)
    if bad:
        red(f"ns 解包段拋 KeyError ⇒ app 生產路徑必崩（{why}）")
    else:
        print(f"  ✅ ns 解包段通過（終止於 {why}）"
              "　⚠️ 其終止係**既有另案**（結構閘）·⛔ 非本閘所守")

    # ── 竄改自檢（動態）：抽**最早之無條件解包點**（保證於本情境必執行）──
    victim = uncond[0][1]
    ns_bad = {k: v for k, v in ns_app.items() if k != victim}
    print(f"  → [竄改態] 自受限 ns 抽掉 `{victim}`（`stepg:{uncond[0][0]}`·無條件）後重跑")
    bad2, why2 = _run(ns_bad, args)
    if bad2:
        print(f"  ✅ 竄改態如期轉紅（{why2}）⇒ **動態層具鑑別力**")
    else:
        red(f"竄改態仍未觸 ns 解包 KeyError（{why2}）⇒ 動態層**無鑑別力**")


# ══════════════════════════════════════════════════════════════════════════
def main():
    print("=" * 92)
    print("# `W-G.9-4b` 夾具：app `_WF_NS_NAMES` ↔ 引擎 `ns[...]` 接線守護")
    print("=" * 92)
    listed = app_ns_names()
    used = layer_static(listed)

    # ── 竄改自檢（靜態）：抽一個**確被引擎消費**之名 ⇒ 必轉紅；還原 ⇒ 轉綠 ──
    print()
    print("─" * 92)
    print("【竄改自檢·靜態】⛔ 二態皆印；抽名後仍綠 ⇒ 本夾具不得計入交付")
    print("─" * 92)
    if not used:
        red("無可竄改之受詞（母體 0）")
    else:
        victim = sorted(used)[0]
        tampered = [n for n in listed if n != victim]
        miss_t = sorted(used - set(tampered))
        miss_r = sorted(used - set(listed))
        print(f"  抽掉 `{victim}`（引擎確有消費）")
        print(f"   ├ 竄改態 差集 ＝ {miss_t}  ⇒ {'🔴 紅' if miss_t else '✅ 綠'}")
        print(f"   └ 還原態 差集 ＝ {miss_r if miss_r else '（空）'}"
              f"  ⇒ {'🔴 紅' if miss_r else '✅ 綠'}")
        # 🔒 判準為**相對**鑑別力：`victim` 須因抽名而**新出現**於差集。
        #   ⛔ 不可寫成「竄改態紅 ∧ 還原態綠」——本閘若正因真缺陷而紅（還原態即紅），
        #      該寫法會誤報「無鑑別力」（實測：`1041874` 缺陷態下首版即誤報）。
        if victim in miss_t and victim not in miss_r:
            print(f"  ✅ 竄改自檢具鑑別力（`{victim}` 因抽名而新出現於差集）")
        else:
            red(f"竄改自檢**無鑑別力**（`{victim}` 未因抽名而新出現於差集）")

    layer_dynamic()
    print()
    print("=" * 92)
    print(f"{'✅ 夾具 PASS' if RC[0] == 0 else '🔴 夾具 FAIL'}（rc={RC[0]}）")
    print("=" * 92)
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
