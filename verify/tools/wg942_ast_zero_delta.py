#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`W-G.9-42` §D-3／`S-1` 之閘：證明對 `.py` 之異動 **⛔ 未觸任何可執行敘述**。

🔴 **為何不能用 grep／awk 判**（本器之立案理由·CC 自誌）：
  首版以「行首字元是否為 `#`」判之，把**三行 docstring 續行**誤報為「疑似可執行」。
  ⇒ 該量測器**判別力不足**：它分不出「續行」與「敘述」。
  依 `CLAUDE.md`「探針還原內部幾何時須以碼面自身之保證當自我驗證閘」之**第二觸發點**
  （⛔ 停機上呈之前必先自證量測器非紅），改以 **AST** 判——
  **型別系統替我判，⛔ 不由我的正規表示式判。**

🔒 **受詞**：`ast.dump(tree)`，其中**每個 docstring 常數一律置換為固定哨兵**。
  ⇒ 通過即證：**除 docstring 文字外，語法樹逐節點相同**
  （＝變數、呼叫、常數、控制流、縮排結構**全部未動**）。
  ⚠️ **本器⛔ 不證「執行結果相同」**——它證的是**語法樹相同**；
  二者之差＝docstring 若被程式讀取（`__doc__`／`inspect`）仍可能有下游後果。
  本批之射程聲明：受動之四處 docstring／註解**無任何 `__doc__` 讀取者**（見報告 §B）。

🔒 **判別力自檢（⛔ 不得省·每次執行皆跑）**：對**新檔**注入一個真正的可執行差異
  （於模組末尾附加 `_wg942_probe = 1`），該注入本**必須**被判為 🔴 異。
  若注入本亦判「同」⇒ 本器恆綠、其 PASS ⛔ 不得採信。

用法：
    python verify/tools/wg942_ast_zero_delta.py            # 對 HEAD 比
    python verify/tools/wg942_ast_zero_delta.py <base-ref>
"""
import ast
import io
import subprocess
import sys

TARGETS = [
    "app.py",
    "verify/probes/probe_ruling_K9_block_depth.py",
]
SENTINEL = "<<WG942_DOCSTRING_ELIDED>>"


def strip_docstrings(tree):
    """把每個 module／class／function 之 docstring 常數置換為哨兵。⛔ 不刪節點
    （刪節點會改變 body 長度 ⇒ 與「新增一行敘述」不可分辨）。"""
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.ClassDef,
                                 ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not node.body:
            continue
        first = node.body[0]
        if (isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant)
                and isinstance(first.value.value, str)):
            first.value.value = SENTINEL
    return tree


def canon(src, name):
    return ast.dump(strip_docstrings(ast.parse(src, filename=name)),
                    include_attributes=False)


def blob(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"{ref}:{path} 取不到")
    return r.stdout.decode("utf-8")


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    bad = 0
    print(f"【`W-G.9-42` AST 零差異閘（§D-3／`S-1`）】base ＝ {base}")
    print("=" * 78)
    for path in TARGETS:
        old_src = blob(base, path)
        new_src = io.open(path, encoding="utf-8", newline="").read().replace("\r\n", "\n")
        o, n = canon(old_src, path), canon(new_src, path)
        same = (o == n)
        # 判別力自檢：對新檔注入一行真正之敘述 ⇒ 必須判「異」
        inj = canon(new_src + "\n_wg942_probe = 1\n", path)
        disc_same = (inj == o)
        ok = same and not disc_same
        if not ok:
            bad += 1
        nl_o, nl_n = old_src.count("\n"), new_src.count("\n")
        print(f"  {'✅' if same else '🔴'} {path}")
        print(f"       AST（docstring 已置換哨兵）逐節點相同 ＝ {same}"
              f"　｜ 行數 {nl_o} → {nl_n}（Δ{nl_n - nl_o:+d}·全為註解／docstring）")
        print(f"       判別力自檢（注入 `_wg942_probe = 1`）⇒ 相同 ＝ {disc_same}（須 False）")
    print("=" * 78)
    print(f"  結論：{'✅ 零可執行異動 ⇒ S-1 未觸發' if bad == 0 else f'🔴 {bad} 檔異 ⇒ S-1 觸發·停'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
