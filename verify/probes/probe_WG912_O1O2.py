# -*- coding: utf-8 -*-
r"""`W-G.9-12` `O-1`／`O-2`：**實跑**驗證（⛔ 不引分類器、⛔ 不以間接證據交差）。

## 為何須實跑（施工單 §1-1）

`verify/tools/wg911_all_dissect.py` **已自行宣告**「校準失敗（偽陰性）⇒ ⛔ 本分類器之判定
不得採信」。⇒ 其把 `F.2 靜態閘`／`F.4 靜態閘` 判為「只被順序擋住」**僅作候選、非依據**。

## `O-1`：三個 `F.N 靜態閘` 各自可獨立實跑

⚠️ **三者形狀不同**（本批現查）：`F.3`／`F.4` 之禁用名為**內嵌 tuple**；
`F.2` 多繞一個中介變數 `_forbid`。⇒ 抽取式須同時吃兩種形狀，
⛔ **不得以 `F.3` 之形狀外推**（施工單 §8-1 所警告之「看起來同型同構」）。

## `O-2`：CAD 管線於現況實跑跑得完（不需 `run_step_g`）

**主樣本 ＝ `v3 reverse-test③`**（事前登記 §2-2 已寫死取樣與理由）：
其相依恰為 `ns`／`cb_by`／`snapshot`，**不含** `_ctx`／`stepg_ctx`。
⚠️ **具名區分**：「**管線跑不完**」才構成 `O-2` 為偽；
「管線跑完但**其斷言不符**」⛔ **不**構成 `O-2` 為偽。

## 重跑
    python verify/probes/probe_WG912_O1O2.py
"""
import ast
import copy
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

RV = os.path.join(VERIFY, "run_verification.py")
# 🔒 母體自證（考古 69 修法 ①）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
assert os.path.exists(RV), f"🔴 母體檔不存在：{RV}"
_SRC = open(RV, encoding="utf-8").read()
_AST = ast.parse(_SRC)
OUT = os.path.join(VERIFY, "out", "probe_WG912_O1O2.log")
GATES = ("F.2 靜態閘", "F.3 靜態閘", "F.4 靜態閘")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
# 同源抽取（⛔ 一份邏輯吃兩種形狀·⛔ 夾具內不持有任何複本）
# ══════════════════════════════════════════════════════════════════════════
def _parent_map():
    p = {}
    for n in ast.walk(_AST):
        for c in ast.iter_child_nodes(n):
            p[c] = n
    return p


_PAR = _parent_map()


def _name_lit(node):
    a0 = node.args[0]
    t = a0.elts[0] if isinstance(a0, (ast.Tuple, ast.List)) and a0.elts else a0
    if isinstance(t, ast.Constant) and isinstance(t.value, str):
        return t.value
    if isinstance(t, ast.JoinedStr):
        return "".join(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str)
                       else "{…}" for v in t.values)
    return None


def orig_static_gate(prefix):
    """回 (受測檔名, 禁用名 tuple)——**自 `run_verification.py` 原碼 AST 抽取**。

    吃兩種形狀：① `[f"{n}(" for n in (<tuple>) if …]`（`F.3`／`F.4`）
    ② 先 `_forbid = [f"{n}(" for n in (<tuple>)]` 再過濾（`F.2`）。
    ⇒ **一份邏輯**，⛔ 不為每個閘各寫一份（`#20` 族）。
    """
    site = None
    for n in ast.walk(_AST):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "results"
                and (_name_lit(n) or "").startswith(prefix)):
            site = n
    if site is None:
        raise RuntimeError(f"🔴 抽取失敗：找不到 `{prefix}` 之站點")
    cur = _PAR.get(site)
    while cur is not None and not isinstance(cur, ast.Try):
        cur = _PAR.get(cur)
    if cur is None:
        raise RuntimeError(f"🔴 抽取失敗：`{prefix}` 不在任何 `try` 內")
    target, names = None, None
    for st in cur.body:
        for x in ast.walk(st):
            if (isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                    and x.func.id == "open"):
                for a in ast.walk(x):
                    if (isinstance(a, ast.Constant) and isinstance(a.value, str)
                            and a.value.endswith(".py")):
                        target = a.value
            if (isinstance(x, ast.ListComp) and x.generators
                    and isinstance(x.generators[0].iter, (ast.Tuple, ast.List))
                    and all(isinstance(e, ast.Constant) and isinstance(e.value, str)
                            for e in x.generators[0].iter.elts)
                    and x.generators[0].iter.elts):
                names = tuple(e.value for e in x.generators[0].iter.elts)
    if not target or not names:
        raise RuntimeError(f"🔴 抽取失敗：`{prefix}` 之受測檔或禁用名清單取不到"
                           f"（target={target}·names={names}）")
    return target, names


def run_gate(prefix, src=None):
    target, names = orig_static_gate(prefix)
    s = open(os.path.join(VERIFY, target), encoding="utf-8").read() if src is None else src
    return target, names, [f"{n}(" for n in names if f"{n}(" in s]


# ══════════════════════════════════════════════════════════════════════════
def o1():
    say("=" * 96)
    say("【O-1】三個 `F.N 靜態閘` **各自**實跑（⛔ 不引分類器·⛔ 不以其一外推其二）")
    say("=" * 96)
    ok = True
    for g in GATES:
        try:
            target, names, hit = run_gate(g)
        except Exception as e:
            red(f"{g}：抽取／實跑失敗 ⇒ {e}")
            ok = False
            continue
        say(f"  ▸ {g}")
        say(f"      受測檔 ＝ {target}｜禁用名 {len(names)} 個 ＝ {names}")
        say(f"      實跑違規 ＝ {hit if hit else '（空）'}　⇒ {'✅ 綠' if not hit else '🔴 紅'}")
        if hit:
            red(f"{g} 現況即為紅 ⇒ `Z-3` 停機上呈（⛔ 不得調門檻或縮受詞）")
            ok = False
        # 🔒 判別力自檢（考古 69 修法 ④）：期望為「空」⇒ 須證它會非空
        t = run_gate(g, src=f"x = {names[0]}(1)\n")[2]
        say(f"      竄改態（合成含 `{names[0]}(` 之原始碼）⇒ {t if t else '（空）'}"
            f"　{'✅ 具鑑別力' if t else '🔴 **無鑑別力**'}")
        if not t:
            red(f"{g} 之判別力自檢失敗")
            ok = False
    say(f"  ⇒ **`O-1` {'成立' if ok else '破'}**")
    return ok


def o2():
    say()
    say("=" * 96)
    say("【O-2】CAD 管線於現況**實跑**跑得完（不需 `run_step_g`）")
    say("=" * 96)
    say("  主樣本 ＝ `v3 reverse-test③ 單位工程費 3500→3550 ⟹ 重劃總負擔率隨動`")
    say("  取樣理由（事前登記 §2-2）：其相依恰為 `ns`／`cb_by`／`snapshot`，"
        "**不含** `_ctx`／`stepg_ctx` ⇒ 對 `O-2` 最具鑑別力")
    say("  ⚠️ **其餘 5 項未實跑**（⛔ 不以一項外推全部）")
    try:
        from app_harvest import harvest
        import run_verification as rv
        from stepg_pipeline import compute_total_burden_rate
        snapshot = rv.load_snapshot()
        ns, fake_st = harvest()
        say(f"  ① harvest ⇒ ns {len(ns)} 名")
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        say(f"  ② build_pipeline ⇒ cb {len(cb_by)} 塊、cad 鍵 {len(cad)}")
        rate0, bd0 = compute_total_burden_rate(ns, list(cb_by.values()), snapshot)
        say(f"  ③ compute_total_burden_rate（原快照）⇒ 率 ＝ {rate0:.8f}")
        s3 = copy.deepcopy(snapshot)
        s3["財務接線_v3"]["單位工程費_元每m2"] = 3550
        rate3, _ = compute_total_burden_rate(ns, list(cb_by.values()), s3)
        say(f"  ④ compute_total_burden_rate（單位工程費 3550）⇒ 率 ＝ {rate3:.8f}")
    except Exception as e:
        red(f"**管線跑不完** ⇒ `O-2` 破（`Z-2`·裁定 B 不生效）：{type(e).__name__}: {e}")
        say(traceback.format_exc()[-600:])
        return False
    say("  ⇒ ✅ **管線跑完**（⛔ 未經 `run_step_g`）⇒ **`O-2` 成立**")
    moved = round(rate3, 8) != round(rate0, 8)
    say(f"  附帶：該主判定之斷言（率隨動）⇒ {'✅ 成立' if moved else '🔴 不成立'}"
        f"　⚠️ **此項⛔ 不構成 `O-2` 之判準**（事前登記 §2-2 已具名區分）")
    # 🔒 判別力自檢：期望為「跑得完」⇒ 須證「跑不完」會被抓到
    try:
        compute_total_burden_rate(ns, None, snapshot)
        say("  🔴 判別力自檢：餵壞輸入仍未拋 ⇒ 上式**無鑑別力**")
        RC[0] = 1
    except Exception as e:
        say(f"  🔒 判別力自檢：餵壞輸入（`cb=None`）⇒ 實拋 {type(e).__name__}"
            f"　⇒ 「跑得完」之判定**非恆真**")
    return True


def main():
    ok1 = o1()
    ok2 = o2()
    say()
    say("=" * 96)
    say(f"【判定】`O-1` ＝ {'✅ 成立' if ok1 else '🔴 破'}｜`O-2` ＝ {'✅ 成立' if ok2 else '🔴 破'}")
    say("=" * 96)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
