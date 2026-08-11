# -*- coding: utf-8 -*-
r"""`W-G.9-13` 丙組：`_w4` 之來源與 `W-D.4 MinA_區 reverse-test` 之歸類（⛔ 只歸類·不立閘）。

## 待答（`W-G.9-11` 之**唯一未定項**）

`W-D.4 MinA_區 reverse-test(改深度→隨動·非寫死)` 應歸入
「只被順序擋住」／「中間層（需 CAD 管線·不需 `run_step_g`）」／「真需管線」之何者。

## 判法（⛔ 二者並用·⛔ 不以其一交差）

1. **構造現查**：`wd4_tier_list.compute` 之函式體內是否呼叫 `run_step_g`（AST）。
2. **實跑**：`wd4_tier_list.compute(fixture=False)` 跑或不跑得完；若拋，其 traceback
   是否落在 `run_step_g` 之內。

🔒 **判別力自檢**：同一判法施於**已證不需 `run_step_g`** 之對照組
（`wf_f2.fixture_cross_zone`·`W-G.9-13` 甲組已實跑）⇒ 須得出「**不需**」，
否則本判法對任何受詞都會答「需」，即無鑑別力。

## 重跑
    python verify/probes/probe_WG913_w4_class.py
"""
import ast
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

# 🔒 母體自證（考古 69 修法 ①）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"

OUT = os.path.join(VERIFY, "out", "probe_WG913_w4_class.log")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def calls_in(path, fname):
    """`path` 內名為 `fname` 之函式體所呼叫之具名函式（AST·⛔ 非文字 grep）。"""
    src = open(os.path.join(VERIFY, path), encoding="utf-8").read()
    fn = [n for n in ast.walk(ast.parse(src))
          if isinstance(n, ast.FunctionDef) and n.name == fname]
    if not fn:
        raise RuntimeError(f"🔴 母體壞掉：`{path}` 內無 `def {fname}`")
    return sorted({c.func.id for c in ast.walk(fn[0])
                   if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)})


def judge(label, path, fname, runner):
    """回 (需否 run_step_g, 構造證據, 實跑證據)。"""
    cs = calls_in(path, fname)
    struct = "run_step_g" in cs
    say(f"  ▸ {label}")
    say(f"      ① 構造：`{fname}()` 內具名呼叫 {len(cs)} 個｜含 `run_step_g` ⇒ {struct}")
    try:
        r = runner()
        say(f"      ② 實跑：✅ **跑得完**（回傳 {type(r).__name__}）")
        inside = False
    except Exception as e:
        tb = traceback.format_exc()
        inside = ("stepg_pipeline.py" in tb and "in run_step_g" in tb)
        say(f"      ② 實跑：🔴 實拋 {type(e).__name__}｜traceback **落在 `run_step_g` 內** ⇒ {inside}")
        say(f"         訊息首 150 字：{str(e)[:150]}")
    return struct, inside


def main():
    say("=" * 100)
    say("【`W-G.9-13` 丙組】`_w4` 來源與 `W-D.4 MinA_區 reverse-test` 之歸類")
    say("=" * 100)
    say("  `_w4` 之來源（`run_verification.py` 現查）＝ `import wd4_tier_list as _w4`"
        "（**模組匯入**，⛔ 非管線產物）；其消費式 ＝ `_w4.compute(fixture=False)`。")
    say()

    import wd4_tier_list as w4
    s1, i1 = judge("受詞：`wd4_tier_list.compute(fixture=False)`",
                   "wd4_tier_list.py", "compute", lambda: w4.compute(fixture=False))

    say()
    say("  🔒 **判別力自檢**（對照組·已證**不需** `run_step_g`）")
    import run_verification as rv
    import wf_f2
    from app_harvest import harvest
    from selection_pipeline import build_build_parcels

    def ctrl():
        snap = rv.load_snapshot()
        ns, fs = harvest()
        cb_by, _cad = rv.build_pipeline(ns, fs, snap)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        _t, bp, _s = build_build_parcels(ns, fs, v6, list(cb_by.values()), snap)
        return wf_f2.fixture_cross_zone(snap, bp)

    s2, i2 = judge("對照：`wf_f2.fixture_cross_zone`", "wf_f2.py", "fixture_cross_zone", ctrl)

    say()
    say("=" * 100)
    if s2 or i2:
        red("判別力自檢**失敗**：對照組亦被判為「需 `run_step_g`」⇒ 本判法無鑑別力，"
            "⇒ `T6` 破，歸類維持**未定**")
        say("=" * 100)
    else:
        say("  ✅ 判別力自檢通過：對照組之構造與實跑皆判「**不需**」⇒ 本判法會區分。")
        verdict = ("**真需管線（更精確：真需 `run_step_g`）**" if (s1 and i1) else
                   "**未定**（構造與實跑不一致 ⇒ ⛔ 不猜）")
        say(f"【歸類】`W-D.4 MinA_區 reverse-test` ⇒ {verdict}")
        say("  依據：① 構造 ＝ `compute()` 體內呼叫 `run_step_g`；"
            "② 實跑 ＝ 拋於 `run_step_g` 之內。")
        say("  ⇒ ⛔ **非**「只被順序擋住」、⛔ **非**「中間層」")
        say("  ⇒ 【裁定 B】之擴充**不適用**於本項；⛔ 本批不為其立閘（施工單 §3 明文未授權）。")
        if not (s1 and i1):
            red("構造與實跑不一致 ⇒ `T6` 破 ⇒ 維持未定")
        say("=" * 100)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
