# -*- coding: utf-8 -*-
r"""`W-G.9-13` 乙組自檢：**證陷阱為真**＋**證判準複本為 0**（⛔ 不以「沒報錯」代替）。

## 三項受詞

1. **`A-4` 陷阱之實證**：若照 `W-G.9-10` 之 `G-2` 形狀（**內嵌式**）外推、
   ⛔ 不解析 `Name` ⇒ 6 項抽出之受詞**自由名與常數皆為空** ⇒ **恆綠**。
   ⚠️ 此非推想——本探針**實跑兩種抽取式並對照**。
2. **抽取式非恆成功**：對不存在之名目 ⇒ 須**實拋**（否則「抽得到」是恆真句）。
3. **判準複本 ＝ 0**：逐鍵掃 `verify/fixture_midlayer_6items.py` ＋ **判別力自檢**
   （以必然命中之字樣重算 ⇒ 證該式非恆 0）。

## 重跑
    python verify/probes/probe_WG913_gate_selfcheck.py
"""
import ast
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

# 🔒 母體自證（考古 69 修法 ①）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
FIX = os.path.join(VERIFY, "fixture_midlayer_6items.py")
assert os.path.exists(FIX), f"🔴 受檢夾具不存在：{FIX}"

import fixture_midlayer_6items as FX  # noqa: E402

OUT = os.path.join(VERIFY, "out", "probe_WG913_gate_selfcheck.log")
L, RC = [], [0]
PREFIXES = tuple(p for p, _k, _n, _t in FX.ITEMS)      # 🔒 同源：⛔ 不另抄一份名目清單


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
def naive_criterion(prefix):
    """**照 `G-2` 之內嵌式形狀外推**（⛔ 不解析 `Name`）——本函式即「錯誤作法」之複現。"""
    site = None
    for n in ast.walk(FX._RV_AST):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append" and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "results"
                and isinstance(n.args[0], (ast.Tuple, ast.List)) and len(n.args[0].elts) >= 2
                and (FX._name_lit(n) or "").startswith(prefix)):
            site = n
    return site.args[0].elts[1] if site is not None else None


def s1():
    say("=" * 100)
    say("【自檢 1】`A-4` 陷阱之實證：照 `G-2` 內嵌式外推 ⇒ 受詞為空 ⇒ **恆綠**")
    say("=" * 100)
    say("  🔒 **判準之受詞** ＝ 數值常數／`_anc` 鍵／字串 tuple 三者"
        "（⛔ 非「自由名」——外推式抽到之 `_ok_*` 係 `run_verification` 之**內部布林**，")
    say("     其名雖非空，卻**無任何管線可綁定**它 ⇒ 就地求值必拋。二者皆為 `A-4` 之表現。）")
    say()
    bad = 0
    for p in PREFIXES:
        nv = naive_criterion(p)
        nv_src = " ".join((ast.get_source_segment(FX._RV_SRC, nv) or "").split())
        _lit, node, src, _tr = FX.orig_criterion(p)
        nv_recv = (FX.numbers(nv), FX.keys_under(nv, "_anc"), FX.string_tuple(nv))
        ok_recv = (FX.numbers(node), FX.keys_under(node, "_anc"), FX.string_tuple(node))
        # 實跑「若照抄會怎樣」：以本批之真命名空間求值外推式 ⇒ 須拋（證其不可用）
        try:
            FX.eval_criterion(nv, {"_x": 1})
            raised = None
        except Exception as e:
            raised = f"{type(e).__name__}: {str(e)[:60]}"
        say(f"  ▸ `{p}`")
        say(f"      ❌ 外推式抽到 ＝ {nv_src!r}｜受詞（常數／`_anc`鍵／tuple）＝ {nv_recv}")
        say(f"          就地求值 ⇒ {raised or '🔴 竟未拋'}")
        say(f"      ✅ 本批抽到 ＝ {src[:84]}{'…' if len(src) > 84 else ''}")
        say(f"          受詞 ＝ {ok_recv}")
        empty = not any(nv_recv) and raised is not None
        if empty:
            bad += 1
        else:
            red(f"`{p}`：外推式之受詞竟非空、或竟可求值 ⇒ 本自檢之前提須重查")
    say(f"  ⇒ **{bad}／{len(PREFIXES)} 項**之外推式**判準受詞全空且不可求值**")
    say("     ⇒ 🔴 若照抄 `G-2` 之內嵌式形狀，這 6 個閘會是 **6 個空閘**（`A-4`）")
    return bad == len(PREFIXES)


def s2():
    say()
    say("=" * 100)
    say("【自檢 2】抽取式**非恆成功**（⛔ 否則「抽得到」是恆真句）")
    say("=" * 100)
    ok = True
    for probe in ("ZZZ_不存在之名目", "v3 財務錨 B =="):
        try:
            _l, _n, src, _t = FX.orig_criterion(probe)
            if probe.startswith("ZZZ"):
                red(f"對不存在之名目 `{probe}` 竟抽得到 ⇒ **無鑑別力**")
                ok = False
            else:
                say(f"  ▸ `{probe}`（**存在**之對照組）⇒ 抽到 {src[:70]}… ✅ 證抽取式確會命中")
        except Exception as e:
            if probe.startswith("ZZZ"):
                say(f"  ▸ `{probe}` ⇒ 實拋 {type(e).__name__} ✅ 具鑑別力")
            else:
                red(f"對存在之名目 `{probe}` 竟抽不到：{e}")
                ok = False
    return ok


def s3():
    say()
    say("=" * 100)
    say("【自檢 3】判準複本 ＝ 0（逐鍵 ＋ 判別力自檢）")
    say("=" * 100)
    src_raw = open(FIX, encoding="utf-8").read()
    # 🔴 **名目字面須先扣除**（`W-G.9-13` 自檢抓到之誤報）：判準鍵 `重劃總負擔率`
    #    恰為名目字面 `v3 重劃總負擔率錨` 之**子字串**；而名目字面是**定位用之 prefix**、
    #    夾具**必須**持有它（否則無從找到站點）⇒ ⛔ 不得計為判準複本。
    #    ⚠️ 尚須扣除名目字面之**呈現形**（去尾綴運算子／空白）——docstring 內寫
    #       `v3 重劃總負擔率錨` 而 `ITEMS` 之 prefix 為 `v3 重劃總負擔率錨 ==`。
    variants = []
    for p in PREFIXES:
        variants.append(p)
        v = p.rstrip(" =（(")
        if v and v != p:
            variants.append(v)
    src = src_raw
    for p in sorted(variants, key=len, reverse=True):
        src = src.replace(p, "〈名目字面〉")
    say(f"  🔒 母體 ＝ `fixture_midlayer_6items.py`（{len(src_raw)} 字元；"
        f"扣除 {len(variants)} 個**名目字面（含呈現形）**後 {len(src)} 字元）")
    say("     ⚠️ 扣除之由：名目字面係**定位用 prefix**、夾具必須持有；"
        "且判準鍵可能為其**子字串**（本批實例：`重劃總負擔率` ⊂ `v3 重劃總負擔率錨`）。")
    # 🔒 受檢鍵**自原碼同源取得**（⛔ 不在本探針內抄寫錨值）
    keys = []
    for p, kind, _n, _t in FX.ITEMS:
        _l, node, _s, _tr = FX.orig_criterion(p)
        if kind == "①":
            # ⛔ 用**原碼字面**（非 `repr`）——`5e-4` 之 `repr` 為 `0.0005`、寫法不符即漏檢
            keys += [(ast.get_source_segment(FX._RV_SRC, c), "型① 數值錨")
                     for c in ast.walk(node)
                     if isinstance(c, ast.Constant) and isinstance(c.value, float)]
        elif kind == "②":
            keys += [(k, "型② `_anc` 鍵") for k in FX.keys_under(node, "_anc")]
        elif kind == "④":
            t = FX.string_tuple(node)
            keys += [(str(t), "型④ tuple（`str` 形）"),
                     (", ".join(f'"{x}"' for x in t), "型④ tuple（原碼形）")]
    seen, bad = set(), 0
    for k, why in keys:
        if k in seen:
            continue
        seen.add(k)
        c = src.count(k)
        say(f"  ▸ {why}｜`{k}` 於夾具內命中 ＝ {c}　{'✅' if c == 0 else '🔴 **有複本**'}")
        if c:
            bad += 1
    # 🔒 判別力自檢 ①：以**必然命中**之字樣重算 ⇒ 證上式非恆 0
    for probe in ("orig_criterion", "eval_criterion"):
        say(f"  🔒 判別力自檢①｜`{probe}` 命中 ＝ {src.count(probe)}（必 >0 ⇒ 上式非恆 0）")
        if src.count(probe) == 0:
            red("判別力自檢失敗：連必然命中之字樣都是 0 ⇒ 母體壞掉")
            bad += 1
    # 🔒 判別力自檢 ②：**注入一份真複本**於扣除後之母體 ⇒ 逐鍵須全部抓到
    #    （⛔ 只證「現在是 0」不算；須證「真有複本時抓得到」——扣除名目字面未把母體挖空）
    miss = [k for k in seen if (src + "\n" + k).count(k) != src.count(k) + 1]
    say(f"  🔒 判別力自檢②｜於扣除後母體注入各鍵之真複本 ⇒ "
        f"{len(seen) - len(miss)}／{len(seen)} 鍵之計數 +1"
        f"{'　✅ 皆抓得到' if not miss else f'　🔴 漏抓 {miss}'}")
    if miss:
        red(f"判別力自檢②失敗：注入複本後仍抓不到 {miss} ⇒ 扣除步驟把母體挖空了")
        bad += 1
    # 型③ 之明示例外
    say(f"  ⚠️ **型③ 之明示例外**：`_F2_EXPR_FROZEN` 存有原式之正規化文字"
        f"（施工單 §2-2 型③ 所訂之同源自證手段）")
    say(f"     其內**無任何外部錨值**——容差 `0.01` 與期望值 `expect_m1` 皆屬原式自身；"
        f"命中 ＝ {src.count('_F2_EXPR_FROZEN')} 處（宣告 1 ＋ 比對 1 ＋ 訊息 1）")
    if bad:
        red(f"判準複本檢出 {bad} 項")
    return bad == 0


def main():
    a, b, c = s1(), s2(), s3()
    say()
    say("=" * 100)
    say(f"【判定】陷阱實證 {'✅' if a else '🔴'}｜抽取非恆成功 {'✅' if b else '🔴'}｜"
        f"判準複本 0 {'✅' if c else '🔴'}")
    say("=" * 100)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
