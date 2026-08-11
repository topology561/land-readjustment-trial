# -*- coding: utf-8 -*-
r"""`W-G.9-10`：`G3` 三項中**不依賴管線**之主判定——獨立立閘。

## 為何（`W-G.9-6` §4-2／`W-G.9-10` §0）

期望 FAIL 名單上之三項（`W-D.3 碎片`／`W-F F.3`／`W-G G.2 世代幾何曝出契約`）
**其名目皆出自 `except` 分支**；其 `try` body 內合計 **15 個主判定站點，一個都沒登記過**
（`python verify/tools/wg910_g3_dissect.py`）。
⇒ `W-G.9-7` 之對帳只凍**失敗原因**，**原命題從未被正面驗證**。

本夾具把其中**經現查證實不依賴 `run_step_g` 跑完**之 **3 個**主判定獨立出來守。

## 🔒 四項聲明（`W-G.9-10` §2-4·⛔ 逐條·不得留空）

### 1. 本閘守的是原命題之哪個子集？

| # | 原主判定（名目字面） | 本閘所守之子集 |
|---|---|---|
| **G-1** | `F.3 靜態閘（wf_f3 不呼叫 calc_a_prime／三廢）` | **全部**——該判定本身即純靜態 |
| **G-2** | `F.3 跨區段 fixture（a→b a′={…}≠a·ratio≠1）` | **全部**——其輸入只有 `snapshot` |
| **G-3** | `W-G G.2 世代幾何曝出契約＋只寫不讀（…靜態越界=0）` | **只寫不讀之靜態圍欄**（`(b)` 部） |

### 2. 🔴 放棄了哪個子集？其後果是什麼？

| # | 放棄 | 後果（**本閘不看**） |
|---|---|---|
| **G-3** | **曝出契約（`(a)` 部）**——`v3/f0/f2/f3/E` 各代原始列**逐宗 `cut_coords` 是否存在**、`f1/f4` 之 `reshape_polys`／`wedge_coords` 是否非空 | 若某代**產得出資料但漏曝座標**，本閘**看不見**；該子集需上游世代成功，⛔ 現況無法計算 |
| — | **其餘 12 個主判定**（`W-D.3` 之 2 ＋ `F.3` 之 10） | **完全未守**——見報告之**守備移交清單** |

⇒ **15 個主判定中，本閘守 3 個之命題（其中 1 個只守一半）；12 個仍無人守。**

### 3. 本閘之受詞與既有 `except` 分支是否重疊？

**⛔ 不重疊。** 既有 `except` 分支之受詞 ＝ **compute 失敗之訊息**
（已由 `W-G.9-7` 之對帳凍存）；本閘之受詞 ＝ **命題本身之真偽**。
⇒ 二者為**不同述詞**，⛔ 非同一述詞兩處定義。

### 4. 另案修好之後，本閘會怎樣？

**不變、仍綠。** 三項受詞**皆與管線無關**（純檔案讀取／純快照算術）
⇒ ⛔ **不會假紅**（`X-4` 未觸發）。
⚠️ 另案修好後，`run_verification` 內之**原主判定亦將開始執行** ⇒ 屆時同一命題有兩處判定
——**惟二者同源**（見下），且原判定復活時本夾具應**併同檢討是否退場**。

## 🔒 同源（⛔ 不抄寫第二份述詞·`#20` 族）

本檔**不複製**任何判準常數：`G-1` 之函式名清單、`G-3` 之檔／鍵清單，
**一律以 AST 自 `verify/run_verification.py` 原碼抽取**（`_orig_*`）。
⇒ 原碼一改，本夾具**跟著改**；⛔ 無漂移空間。
`G-2` 之斷言式無法以常數表達，改以**原始碼文字之同源自證**（`_assert_expr_unchanged`）
——原式一變即 **loud 紅**，⛔ 不靜默沿用舊式。

## 重跑
    python verify/fixture_g3_static_guards.py       # rc=0 ⇒ 綠
"""
import ast
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

RV = os.path.join(HERE, "run_verification.py")
# 🔒 母體自證（考古 69 修法 ①）：⛔ 指錯檔即全綠假象
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
assert os.path.exists(RV), f"🔴 母體檔不存在：{RV}"
_RV_SRC = open(RV, encoding="utf-8").read()
_RV_AST = ast.parse(_RV_SRC)
RC = [0]


def red(msg):
    print(f"  🔴 {msg}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
# 同源抽取（⛔ 不抄寫·一律自原碼取）
# ══════════════════════════════════════════════════════════════════════════
def _orig_f3_static_names():
    """`F.3 靜態閘` 之函式名清單——自 `_f3hit = [...]` 之 comprehension 取。"""
    for n in ast.walk(_RV_AST):
        if (isinstance(n, ast.Assign) and n.targets
                and isinstance(n.targets[0], ast.Name) and n.targets[0].id == "_f3hit"
                and isinstance(n.value, ast.ListComp)):
            it = n.value.generators[0].iter
            if isinstance(it, (ast.Tuple, ast.List)):
                return tuple(e.value for e in it.elts if isinstance(e, ast.Constant))
    raise RuntimeError("🔴 同源抽取失敗：`run_verification.py` 內找不到 `_f3hit` 之清單")


def _orig_g2_static_lists():
    """`G.2 只寫不讀` 之 (每檔恰 1 次清單, 越界檔清單, 越界鍵清單)——自原碼之 for 迭代式取。"""
    once, cross_files, cross_keys = None, None, None
    for n in ast.walk(_RV_AST):
        if not isinstance(n, ast.For):
            continue
        tgt, it = n.target, n.iter
        if (isinstance(tgt, ast.Tuple) and len(tgt.elts) == 2
                and getattr(tgt.elts[0], "id", "") == "_fn2"
                and isinstance(it, (ast.Tuple, ast.List))):
            once = tuple((e.elts[0].value, tuple(k.value for k in e.elts[1].elts))
                         for e in it.elts)
        elif (getattr(tgt, "id", "") == "_fn2" and isinstance(it, (ast.Tuple, ast.List))):
            cross_files = tuple(e.value for e in it.elts if isinstance(e, ast.Constant))
            for sub in ast.walk(n):
                if (isinstance(sub, ast.For) and getattr(sub.target, "id", "") == "_k2"
                        and isinstance(sub.iter, (ast.Tuple, ast.List))):
                    cross_keys = tuple(e.value for e in sub.iter.elts
                                       if isinstance(e, ast.Constant))
    if not (once and cross_files and cross_keys):
        raise RuntimeError("🔴 同源抽取失敗：`run_verification.py` 內找不到 G.2 之靜態圍欄清單")
    return once, cross_files, cross_keys


# 🔒 `G-2` 之斷言式無法以常數表達 ⇒ 以**原始碼文字**同源自證（原式一變即 loud 紅）
_G2_EXPR_FROZEN = ('_fx3["ratio_ne_1"] and abs(_fx3["a_prime_a_to_b"] - _fx3["expect"]) < 0.01')


def _assert_expr_unchanged():
    for n in ast.walk(_RV_AST):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and n.args
                and isinstance(n.args[0], (ast.Tuple, ast.List))
                and len(n.args[0].elts) >= 2):
            t0 = n.args[0].elts[0]
            lit = ""
            if isinstance(t0, ast.JoinedStr):
                lit = "".join(v.value for v in t0.values
                              if isinstance(v, ast.Constant) and isinstance(v.value, str))
            if lit.startswith("F.3 跨區段 fixture"):
                cur = ast.get_source_segment(_RV_SRC, n.args[0].elts[1])
                cur = " ".join((cur or "").split())
                if cur != _G2_EXPR_FROZEN:
                    raise RuntimeError(
                        f"🔴 同源自證破：`run_verification` 之 `F.3 跨區段 fixture` 斷言式已改\n"
                        f"       凍存：{_G2_EXPR_FROZEN}\n       現況：{cur}")
                return cur
    raise RuntimeError("🔴 同源抽取失敗：找不到 `F.3 跨區段 fixture` 之站點")


# ══════════════════════════════════════════════════════════════════════════
# 三個受詞（⛔ 皆為原命題之再執行·非另寫判準）
# ══════════════════════════════════════════════════════════════════════════
def g1(src=None):
    """`F.3 靜態閘`：`wf_f3.py` 不得呼叫 `calc_a_prime`／三廢函式。回違規清單。"""
    s = open(os.path.join(HERE, "wf_f3.py"), encoding="utf-8").read() if src is None else src
    return [f"{n}(" for n in _orig_f3_static_names() if f"{n}(" in s]


def g3(srcs=None):
    """`G.2 只寫不讀`：新曝鍵於各引擎檔恰 1 次、他檔零越界。回違規清單。"""
    once, cross_files, cross_keys = _orig_g2_static_lists()
    get = (lambda fn: open(os.path.join(HERE, fn), encoding="utf-8").read()) \
        if srcs is None else (lambda fn: srcs.get(fn, ""))
    v = []
    for fn, keys in once:
        s = get(fn)
        for k in keys:
            n = s.count(f'"{k}"')
            if n != 1:
                v.append(f"{fn}:{k} 出現 {n} 次≠1（只寫不讀破）")
    for fn in cross_files:
        s = get(fn)
        for k in cross_keys:
            if f'"{k}"' in s:
                v.append(f"{fn} 出現 {k}（越界）")
    return v


def main():
    print("=" * 96)
    print("# `W-G.9-10` 夾具：`G3` 三項中**不依賴管線**之主判定（⛔ 受詞＝命題本身）")
    print("=" * 96)
    print(f"  母體：{os.path.relpath(RV, REPO)}（{len(_RV_SRC.splitlines())} 行）"
          f"｜判準常數**一律自其 AST 抽取**（⛔ 不抄寫·`#20` 族）")

    names = _orig_f3_static_names()
    once, cf, ck = _orig_g2_static_lists()
    print(f"  同源抽取：`F.3 靜態閘` 函式名 {len(names)} 個 {names}")
    print(f"            `G.2` 恰 1 次清單 {len(once)} 檔｜越界檔 {len(cf)}｜越界鍵 {len(ck)}")
    assert names and once and cf and ck, "🔴 抽取為空 ⇒ ⛔ 不得算通過（考古 67 修法 ①）"

    # ── G-1 ──────────────────────────────────────────────────────────────
    print()
    print("─" * 96)
    print("【G-1】`F.3 靜態閘`：`wf_f3.py` 不呼叫 `calc_a_prime`／三廢")
    print("─" * 96)
    v1 = g1()
    print(f"  違規 ＝ {v1 if v1 else '（空）'}")
    if v1:
        red("G-1 破 ⇒ 🔴 **停機上呈**（`X-2`：它抓到了真東西·⛔ 不得調門檻）")
    else:
        print("  ✅ G-1 綠")
    #   🔒 判別力自檢（考古 69 修法 ④）：期望值為「空」⇒ 須證它會非空
    t1 = g1(src=f"x = {names[0]}(1)\n")
    print(f"  竄改態（合成一支含 `{names[0]}(` 之原始碼）⇒ {t1 if t1 else '（空）'}"
          f"　{'✅ 具鑑別力' if t1 else '🔴 **無鑑別力**'}")
    if not t1:
        red("G-1 之竄改自檢無鑑別力 ⇒ 本閘不得計入交付（`X-3`）")

    # ── G-2 ──────────────────────────────────────────────────────────────
    print()
    print("─" * 96)
    print("【G-2】`F.3 跨區段 fixture`：`a→b` 之 `a′≠a` 且 `ratio≠1`")
    print("─" * 96)
    expr = _assert_expr_unchanged()
    print(f"  同源自證：原斷言式逐字未變 ⇒ `{expr}`")
    import run_verification as rv
    import wf_f3
    snap = rv.load_snapshot()
    fx = wf_f3.fixture_cross_zone_f3(snap)
    ok2 = fx["ratio_ne_1"] and abs(fx["a_prime_a_to_b"] - fx["expect"]) < 0.01
    print(f"  實測 ＝ {fx}")
    print(f"  判 ＝ {'✅ 綠' if ok2 else '🔴 紅'}")
    if not ok2:
        red("G-2 破 ⇒ 🔴 **停機上呈**（`X-2`）")
    #   🔒 判別力自檢：期望為「綠」⇒ 須證它會紅
    bad = dict(fx, a_prime_a_to_b=fx["expect"] + 1.0)
    ok2t = bad["ratio_ne_1"] and abs(bad["a_prime_a_to_b"] - bad["expect"]) < 0.01
    print(f"  竄改態（`a_prime` 偏移 +1.0）⇒ {'🔴 仍綠' if ok2t else '✅ 轉紅'}"
          f"　{'🔴 **無鑑別力**' if ok2t else '✅ 具鑑別力'}")
    if ok2t:
        red("G-2 之竄改自檢無鑑別力 ⇒ 本閘不得計入交付（`X-3`）")

    # ── G-3 ──────────────────────────────────────────────────────────────
    print()
    print("─" * 96)
    print("【G-3】`G.2 只寫不讀`（靜態圍欄·⛔ **不含**曝出契約——見 docstring 聲明 2）")
    print("─" * 96)
    v3 = g3()
    print(f"  違規 ＝ {v3 if v3 else '（空）'}")
    if v3:
        red("G-3 破 ⇒ 🔴 **停機上呈**（`X-2`）")
    else:
        print("  ✅ G-3 綠")
    #   🔒 判別力自檢：兩種違規各造一次
    fn0, k0 = once[0][0], once[0][1][0]
    t3a = g3(srcs={fn0: f'"{k0}" "{k0}"'})
    t3b = g3(srcs={fn0: f'"{k0}"', cf[0]: f'"{ck[0]}"'})
    print(f"  竄改態 A（`{fn0}` 之 `{k0}` 出現 2 次）⇒ {t3a[:1] if t3a else '（空）'}"
          f"　{'✅' if t3a else '🔴'}")
    print(f"  竄改態 B（`{cf[0]}` 出現越界鍵 `{ck[0]}`）⇒ "
          f"{[x for x in t3b if '越界' in x][:1] or '（無越界項）'}"
          f"　{'✅' if any('越界' in x for x in t3b) else '🔴'}")
    if not t3a or not any("越界" in x for x in t3b):
        red("G-3 之竄改自檢無鑑別力 ⇒ 本閘不得計入交付（`X-3`）")

    print()
    print("=" * 96)
    print(f"{'✅ 夾具 PASS' if RC[0] == 0 else '🔴 夾具 FAIL'}（rc={RC[0]}）")
    print("=" * 96)
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
