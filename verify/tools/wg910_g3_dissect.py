# -*- coding: utf-8 -*-
r"""`W-G.9-10` §0／`R-1`：`G3` 三項之 `try`／`except` 結構與**主判定站點**拆解。

**受詞**：`verify/run_verification.py` 中，期望 FAIL 名單上之三項
（`W-D.3 碎片`／`W-F F.3`／`W-G G.2 世代幾何曝出契約`）——
現查其名目**是否出自 `except` 分支**，及其 `try` body 內之 `results.append` 站點
（＝**主判定**）於覆蓋資料中**是否曾執行**。

⛔ 由 AST 逐節點讀出（考古 67 修法 ③：不得以 grep 上下文窗抽清單）。
🔒 **母體自證**（考古 69 修法 ①②）：斷言母體檔存在、並印出母體規模。

## 重跑
    python verify/tools/wg910_g3_dissect.py
"""
import ast
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
RV = os.path.join(VERIFY, "run_verification.py")
COV = os.path.join(VERIFY, "out", "WG96_coverage.txt")

# 🔒 母體自證：⛔ 少一層 dirname／指錯檔即產生假綠（`W-G.9-9` 自誌·考古 69）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
assert os.path.exists(RV), f"🔴 母體檔不存在：{RV}"
assert os.path.exists(COV), f"🔴 覆蓋資料不存在：{COV}"

TARGETS = ("W-D.3 碎片", "W-F F.3", "W-G G.2 世代幾何曝出契約")


def name_literal(node):
    a0 = node.args[0]
    t = a0.elts[0] if isinstance(a0, (ast.Tuple, ast.List)) and a0.elts else a0
    if isinstance(t, ast.Constant) and isinstance(t.value, str):
        return t.value
    if isinstance(t, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str)
                       else "{…}" for v in t.values)
    return None


def main():
    src = open(RV, encoding="utf-8").read()
    tree = ast.parse(src)
    lines = src.splitlines()
    executed = set()
    for ln in open(COV, encoding="utf-8"):
        if ln.startswith("#") or not ln.strip():
            continue
        executed.add(int(ln.split("\t")[0]))

    appends = []
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "results"):
            appends.append((n.lineno, name_literal(n)))
    print(f"【母體】{os.path.relpath(RV, REPO)}：{len(lines)} 行"
          f"｜`results.append` 站點 {len(appends)} 處")
    print(f"【覆蓋】{os.path.relpath(COV, REPO)}：已執行行 {len(executed)}")
    assert appends and executed, "🔴 母體或覆蓋為空 ⇒ ⛔ 不得續（考古 67 修法 ①）"
    print()

    tries = [n for n in ast.walk(tree) if isinstance(n, ast.Try)]
    total_main, total_dead = 0, 0
    for tgt in TARGETS:
        hit = None
        for t in tries:
            for h in t.handlers:
                for n in ast.walk(h):
                    if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                            and n.func.attr == "append"
                            and isinstance(n.func.value, ast.Name)
                            and n.func.value.id == "results"
                            and name_literal(n) == tgt):
                        hit = (t, h, n.lineno)
        if hit is None:
            print(f"🔴 【{tgt}】**未**於任何 `except` 分支找到同名站點 ⇒ `R-1` 後半破")
            continue
        t, h, ln_exc = hit
        b0 = min(x.lineno for st in t.body for x in ast.walk(st) if hasattr(x, "lineno"))
        b1 = max(getattr(x, "end_lineno", x.lineno) for st in t.body
                 for x in ast.walk(st) if hasattr(x, "lineno"))
        main_sites = [(l, s) for l, s in appends if b0 <= l <= b1]
        dead = [(l, s) for l, s in main_sites if l not in executed]
        total_main += len(main_sites)
        total_dead += len(dead)
        print(f"【{tgt}】try {b0}–{b1}｜except 之名目站點 @{ln_exc}"
              f"（曾執行 ⇒ {ln_exc in executed}）")
        print(f"   主判定站點 {len(main_sites)} 個｜曾執行 "
              f"{[l for l, _ in main_sites if l in executed]}｜**從未執行 {len(dead)} 個**")
        for l, s in main_sites:
            print(f"     {'🔴' if l not in executed else '✅'} :{l:<6} {s}")
        print()
    print(f"⇒ 三項合計：主判定站點 **{total_main}** 個｜**從未執行 {total_dead}** 個")
    print("🔒 判別力自檢（考古 69 修法 ④）：以一個**必然執行**之名目重算 ——")
    probe = [(l, s) for l, s in appends if s and s.startswith("參數")]
    print(f"   `參數{{…}}` 站點 {probe}｜曾執行 ⇒ "
          f"{[l in executed for l, _ in probe]}　⇒ 上式**非恆判未執行**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
