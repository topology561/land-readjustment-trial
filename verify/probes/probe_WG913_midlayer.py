# -*- coding: utf-8 -*-
r"""`W-G.9-13` 甲組：**中間層其餘 5 項之逐項補跑**（⛔ 不以主樣本外推·⛔ 不以「同在財務段」推定）。

## 為何須逐項（施工單 §2-1）

`W-G.9-12` 只實跑了**一項**主樣本（`v3 reverse-test③`）。
【裁定 B】之生效條件僅由該一項證成 ⇒ 其餘 5 項之「跑得完」**仍為未證**。
⚠️ `W-G.9-12` 之教訓：**形狀相似不代表結構相同**（`F.2` 之碼面多繞一個中介變數）。
⇒ **5 項要跑 5 次**，⛔ 不得外推。

## 🔒 每項各自一個 `try`（**考古 70**）

考古 70 之症狀 ＝「一個 `try` 把『要管線的』與『不要管線的』判定綁在一起——上游一崩，
連不需要它的也陪葬」。⇒ 本探針**逐項獨立 `try`**；任一項失敗 ⛔ 不得使其餘項失去結果。

## 🔒 判別力自檢（**考古 69 修法 ④**）

每項附「餵壞輸入 ⇒ 須實拋（或須轉偽）」——⛔ 只證「現在跑得完」不算，
須證**跑不完時會被抓到**，否則「跑得完」是恆真句。

## 重跑
    python verify/probes/probe_WG913_midlayer.py
"""
import copy
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

# 🔒 母體自證（考古 69 修法 ①）：⛔ 指錯倉根即全綠假象
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
assert os.path.exists(os.path.join(VERIFY, "run_verification.py")), "🔴 母體檔不存在"

OUT = os.path.join(VERIFY, "out", "probe_WG913_midlayer.log")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
# 管線層（**逐層**建·每項具名聲明其所需之層·⛔ 不預設誰需要誰）
# ══════════════════════════════════════════════════════════════════════════
_S = {}


def stage_A():
    """層 A ＝ `harvest` ＋ `load_snapshot`（引擎符號＋快照）。"""
    if "A" not in _S:
        from app_harvest import harvest
        import run_verification as rv
        snap = rv.load_snapshot()
        ns, fake_st = harvest()
        _S["A"] = {"rv": rv, "snap": snap, "ns": ns, "fake_st": fake_st}
    return _S["A"]


def stage_B():
    """層 B ＝ `build_pipeline`（⇒ `cb_by`／`cad`，且**於其函式體內**寫入
    `f3_total_burden_rate_from_finance` 與 `_v3_burden_rate_breakdown`）。"""
    if "B" not in _S:
        a = stage_A()
        cb_by, cad = a["rv"].build_pipeline(a["ns"], a["fake_st"], a["snap"])
        _S["B"] = {"cb_by": cb_by, "cad": cad}
    return _S["B"]


def stage_C():
    """層 C ＝ `build_build_parcels`（⇒ `build_parcels`）。

    🔴 **「是否需 `build_ownership` 先行」為前置登記所列之未知** ⇒ 本層**實跑判定**：
    先**不跑** `build_ownership` 直接試；拋則改為先跑 `build_ownership` 再試。
    ⛔ 不預設答案、⛔ 不以「看起來要」推定。
    """
    if "C" not in _S:
        a, _ = stage_A(), stage_B()
        from selection_pipeline import build_ownership, build_build_parcels
        with open(a["rv"].V6DXF, "rb") as f:
            v6 = f.read()
        cbl = list(_S["B"]["cb_by"].values())
        need_own, err = None, None
        try:
            tp, bp, sw = build_build_parcels(a["ns"], a["fake_st"], v6, cbl, a["snap"])
            need_own = False
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
            build_ownership(a["ns"], a["fake_st"], a["rv"].ANON_XLSX)
            tp, bp, sw = build_build_parcels(a["ns"], a["fake_st"], v6, cbl, a["snap"])
            need_own = True
        _S["C"] = {"temp": tp, "build_parcels": bp, "swaps": sw,
                   "need_ownership": need_own, "first_err": err}
    return _S["C"]


# ══════════════════════════════════════════════════════════════════════════
# 5 項（⛔ 逐項獨立·每項 ＝ (名目字面, 所需層, 評估式, 判別力自檢)）
# ══════════════════════════════════════════════════════════════════════════
def item1():
    """`v3 重劃總負擔率錨 == `（型② `_anc` 字典查值）。"""
    a, _ = stage_A(), stage_B()
    anc = a["snap"]["財務接線_v3"]["斷言錨"]
    live = float(a["fake_st"].session_state["f3_total_burden_rate_from_finance"])
    ok = round(live, 8) == float(anc["重劃總負擔率"])
    return ok, f"錨 {anc['重劃總負擔率']}｜現算 {live:.8f}｜Δ {live - float(anc['重劃總負擔率']):+.10f}"


def probe1():
    """判別力：餵壞輸入（`cb=None`）於**本項之生產路徑** ⇒ 須實拋。"""
    from stepg_pipeline import compute_total_burden_rate
    a = stage_A()
    try:
        compute_total_burden_rate(a["ns"], None, a["snap"])
        return False, "餵壞輸入（cb=None）仍未拋"
    except Exception as e:
        return True, f"餵壞輸入（cb=None）⇒ 實拋 {type(e).__name__}"


def item2():
    """`v3 率分項錨 公設負擔比 `（型① 內嵌數值字面 34.754211／5.958176）。"""
    a, _ = stage_A(), stage_B()
    bd = a["fake_st"].session_state["_v3_burden_rate_breakdown"]
    g = round(bd["公設負擔比"] * 100, 6)
    f = round(bd["費用負擔比"] * 100, 6)
    ok = (g == 34.754211 and f == 5.958176)
    return ok, f"公設負擔比 {g}%（錨 34.754211）｜費用負擔比 {f}%（錨 5.958176）"


def probe2():
    """判別力：以變異快照重算 ⇒ 分項須**改變**（證其為現算、非常數）。"""
    from stepg_pipeline import compute_total_burden_rate
    a, b = stage_A(), stage_B()
    s2 = copy.deepcopy(a["snap"])
    s2["財務接線_v3"]["單位工程費_元每m2"] = 3550
    _, bd2 = compute_total_burden_rate(a["ns"], list(b["cb_by"].values()), s2)
    bd0 = a["fake_st"].session_state["_v3_burden_rate_breakdown"]
    moved = round(bd2["費用負擔比"] * 100, 6) != round(bd0["費用負擔比"] * 100, 6)
    return moved, (f"單位工程費 3500→3550 ⇒ 費用負擔比 "
                   f"{bd0['費用負擔比']*100:.6f}% → {bd2['費用負擔比']*100:.6f}%"
                   + ("（**會變** ⇒ 具鑑別力）" if moved else "（**未變** ⇒ 疑似常數）"))


def item3():
    """`v3 率用 DXF 公設實值 `（型① 內嵌數值字面 12146.5579·容差 5e-4）。"""
    a, _ = stage_A(), stage_B()
    bd = a["fake_st"].session_state["_v3_burden_rate_breakdown"]
    v = float(bd["公設共同負擔_DXF"])
    ok = abs(v - 12146.5579) < 5e-4
    return ok, f"DXF 公設實值 {v:.4f}（錨 12146.5579·容差 5e-4）｜Δ {v - 12146.5579:+.6f}"


def probe3():
    """判別力：以**截圖 rounded 12146.56** 代入同一容差式 ⇒ 須轉偽（證容差非鬆到無鑑別力）。"""
    v = 12146.56
    still = abs(v - 12146.5579) < 5e-4
    return (not still), (f"以截圖 rounded {v} 代入 ⇒ |Δ|={abs(v-12146.5579):.6f}"
                         f" ⇒ {'仍為真（**無鑑別力**）' if still else '轉偽 ⇒ 具鑑別力'}")


def item5():
    """`F.2 跨區段 fixture（a→b 模式一 a′=`（型③ 自參照·期望值由被測函式自己回傳）。"""
    a, c = stage_A(), stage_C()
    import wf_f2
    fx = wf_f2.fixture_cross_zone(a["snap"], c["build_parcels"])
    ok = (fx["ratio_ne_1"] and abs(fx["mode1_a_to_b"] - fx["expect_m1"]) < 0.01
          and fx["mode1_a_to_b"] > fx["a"])
    return ok, (f"a={fx['a']}｜mode1_a_to_b={fx['mode1_a_to_b']}｜expect_m1={fx['expect_m1']}"
                f"｜ratio_ne_1={fx['ratio_ne_1']}｜mode2_tgtR2={fx['mode2_tgtR2']}"
                f"｜mode2_tgtR1_mixed={fx['mode2_tgtR1_mixed']}")


def probe5():
    """判別力：餵壞 `snap`（空 dict）⇒ 須實拋。"""
    import wf_f2
    c = stage_C()
    try:
        wf_f2.fixture_cross_zone({}, c["build_parcels"])
        return False, "餵壞輸入（snap={}）仍未拋"
    except Exception as e:
        return True, f"餵壞輸入（snap={{}}）⇒ 實拋 {type(e).__name__}"


def item6():
    """`F.4 模式二 p_avg 母體＝原始 build_parcels（R1/R4 可算）`（型④ 名單型）。"""
    a, c = stage_A(), stage_C()
    import wf_f4
    pre, pavg = wf_f4.fixture_mode2_hand(a["snap"], c["build_parcels"])
    ok = all(b in pavg for b in ("R1", "R4"))
    return ok, (f"p_avg 鍵 {sorted(pavg)}｜R1={pavg.get('R1')}｜R4={pavg.get('R4')}"
                f"｜pre 區段 {len(pre)} 個")


def probe6():
    """判別力：以**必不存在**之塊名代入同一 `all(...)` 式 ⇒ 須轉偽（證 `all` 非空集恆真）。"""
    a, c = stage_A(), stage_C()
    import wf_f4
    _, pavg = wf_f4.fixture_mode2_hand(a["snap"], c["build_parcels"])
    still = all(b in pavg for b in ("R1", "ZZZ_不存在之塊"))
    return (not still), (f"以 ('R1','ZZZ_不存在之塊') 代入 ⇒ "
                         f"{'仍為真（**無鑑別力**·疑母體為空）' if still else '轉偽 ⇒ 具鑑別力'}"
                         f"｜母體規模 |p_avg|={len(pavg)}")


ITEMS = (
    ("v3 重劃總負擔率錨 == ", "型② `_anc` 字典查值", "層 B", item1, probe1),
    ("v3 率分項錨 公設負擔比 ", "型① 內嵌數值字面", "層 B", item2, probe2),
    ("v3 率用 DXF 公設實值 ", "型① 內嵌數值字面", "層 B", item3, probe3),
    ("F.2 跨區段 fixture（a→b 模式一 a′=", "型③ 自參照·無外部錨", "層 C", item5, probe5),
    ("F.4 模式二 p_avg 母體＝原始 build_parcels（R1/R4 可算）", "型④ 名單型", "層 C", item6, probe6),
)


def main():
    say("=" * 100)
    say("【`W-G.9-13` 甲組】中間層**其餘 5 項**逐項補跑（⛔ 不以 `v3 reverse-test③` 外推）")
    say("=" * 100)
    say("  ⚠️ 名目 4（`v3 reverse-test③`）已於 `W-G.9-12` 實跑 ⇒ **本探針不重跑**、亦不計入 5 項。")
    say("  🔒 每項**各自一個 `try`**（考古 70）：任一項失敗 ⛔ 不得使其餘項失去結果。")
    say()

    ran, ok_all = 0, True
    for nm, kind, layer, fn, pb in ITEMS:
        say("─" * 100)
        say(f"▸ 名目：`{nm}`")
        say(f"    判準型 ＝ {kind}｜所需管線層 ＝ {layer}")
        try:
            ok, detail = fn()
            ran += 1
            say(f"    ✅ **跑得完**（`T1` 之受詞）")
            say(f"    實跑值：{detail}")
            say(f"    斷言現況 ⇒ {'✅ 綠' if ok else '🔴 **紅**'}")
            if not ok:
                say(f"    🛑 現況為紅 ⇒ `T4` 破 ⇒ `A-2`：⛔ 不得調錨／縮受詞／放寬容差，停機上呈 KL")
                ok_all = False
        except Exception as e:
            red(f"**跑不完** ⇒ `T1` 破 ⇒ `A-1`（該項不立閘·具名照實報）：{type(e).__name__}: {e}")
            say(traceback.format_exc()[-500:])
            ok_all = False
            continue
        try:
            disc, dmsg = pb()
            say(f"    🔒 判別力自檢：{dmsg}")
            if not disc:
                red("判別力自檢**失敗** ⇒ 該項之「跑得完／為真」係恆真句")
                ok_all = False
        except Exception as e:
            say(f"    🔒 判別力自檢：實拋 {type(e).__name__}: {str(e)[:90]} ⇒ 具鑑別力")
    say("─" * 100)

    # 層 C 之附帶實跑事實（前置登記 §1 所列之未知）
    if "C" in _S:
        c = _S["C"]
        say()
        say(f"🔑 **前置登記 §1 之未知已由實跑判定**："
            f"`build_build_parcels` {'**需**' if c['need_ownership'] else '**不需**'} "
            f"`build_ownership` 先行。")
        if c["first_err"]:
            say(f"    （不跑 `build_ownership` 之首試實拋：{c['first_err'][:160]}）")
        say(f"    build_parcels {len(c['build_parcels'])} 筆｜temp {len(c['temp'])} 筆")

    say()
    say("=" * 100)
    say(f"【判定】5 項中**跑得完** ＝ {ran}／5｜`T1` ＝ "
        f"{'✅ 成立' if ran == 5 else '🔴 破（見上具名項）'}")
    say(f"        斷言全綠 ＝ {'✅ 是' if ok_all and ran == 5 else '🔴 否（見上）'}")
    say("=" * 100)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
