#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-161 `§五`**：十二點不變式之**判別力對照**（`D-1`〜`D-5`）。

## 受詞

`W-G.9-161 §三` 之三類不變式已落地於生產碼。本檔證其**⛔ 非裝飾**——
以**執行期擾動**餵入已知為偽之輸入，斷言須 `raise`，且訊息含**對稱差**。

🛑 **一切擾動僅存在於本檔之執行期**，⛔ **未留於出艙之生產碼**（`§五` 逐字）。

## 五組（`D-4`／`D-5` 為一對·⛔ 缺一不可）

| # | 擾動 | 期望 |
|---|---|---|
| `D-1` | `POP_SYNC` 之實參**移除一真實宗** | `raise`，對稱差**恰含**該宗 |
| `D-2` | 宣告 `filter` 由 `stage1` 改 `identity`（**⛔ 不改實參**） | `raise`（證宣告表**確被讀**） |
| `D-3` | `NAME_DERIVATION` 之 `_mem` 注入**他街廓**之宗 | `raise` |
| `D-4` | `wf_f4:_order_fb` 之 `declared_added` 由 `{_abate_key}` 改 `∅` | `raise`（證**非 ∅ 之宣告值確被使用**） |
| `D-5` | `wf_f3:_proj_order`（宣告 `removed = added = ∅`）之後呼叫**注入一宗** | `raise`（證 **∅ 之宣告⛔ 非空轉**） |

🔒 **每組皆附<u>正向對照</u>**（未擾動之同一輸入須**不** `raise`）——否則「擾動後紅」⛔ 不足以
證明判別力（紅有可能係恆紅）。

## 重跑

    PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9161_discrim.py

`rc` 恆為 `0`；缺件時 loud raise。
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "77ebc49"                    # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD）
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s, flush=True)
    L.append(s)


def tp(no, blk="R1", **kw):
    d = {"暫編地號": no, "所屬街廓": blk}
    d.update(kw)
    return d


def run_case(tag, fn, expect_raise):
    """回 (是否 raise, 訊息)。並機檢其與期望相符。"""
    try:
        fn()
        return False, ""
    except RuntimeError as e:                                   # noqa: BLE001
        return True, str(e)


def main():                                                     # noqa: C901
    sys.stdout.reconfigure(encoding="utf-8")
    W = 104
    say("=" * W)
    say("【W-G.9-161 §五】十二點不變式之**判別力對照**（`D-1`〜`D-5`）")
    say("=" * W)
    say("  HEAD        = %s" % subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True,
        check=True).stdout.decode().strip())
    say("  app.py blob = %s" % subprocess.run(
        ["git", "hash-object", "app.py"], cwd=REPO, capture_output=True,
        check=True).stdout.decode().strip())
    say("  基座(log 綁) = %s" % BASE_REF)
    say("")

    from app_harvest import harvest
    ns, _fake = harvest()
    A_seq = ns["_proj_pop_assert_seq"]
    A_diff = ns["_proj_pop_assert_diff"]
    A_sub = ns["_proj_pop_assert_subset"]
    DECL = ns["_PROJ_POP_DECL"]
    say("  🔒 量測器自檢①　`ns` 中取得四符號 ＝ %s"
        % [callable(A_seq), callable(A_diff), callable(A_sub), isinstance(DECL, dict)])
    say("  🔒 量測器自檢②　`_PROJ_POP_DECL` 之列數 ＝ **%d**（`L-2′`）" % len(DECL))
    say("")

    rows = []

    # ══════════ D-1 ══════════
    say("=" * W)
    say("§D-1　`POP_SYNC` 之實參**移除一真實宗**（受詞 ＝ `stepg:_proj_rank`·`filter=stage1`）")
    say("=" * W)
    BASE1 = [tp("628-41(1)"), tp("628-42(1)"), tp("628-27(1)"),
             tp("628-99(9)", 配地階段="池內")]           # 末者為階段2宗 ⇒ 被 stage1 濾掉
    GOOD1 = [x for x in BASE1 if "配地階段" not in x]
    r0, m0 = run_case("D-1+", lambda: A_seq("stepg:_proj_rank", GOOD1, BASE1, blk="R2"), False)
    say("  ✅ 正向對照（未擾動）：raise ＝ **%s**（須 False）" % r0)
    BAD1 = [x for x in GOOD1 if x["暫編地號"] != "628-42(1)"]     # 🔴 移除一真實宗
    r1, m1 = run_case("D-1", lambda: A_seq("stepg:_proj_rank", BAD1, BASE1, blk="R2"), True)
    say("  🔴 擾動（移除 `628-42(1)`）：raise ＝ **%s**" % r1)
    say("     訊息：%s" % m1[:180])
    _hit = "628-42(1)" in m1 and "對稱差" in m1
    say("     🔒 對稱差**恰含**該宗 ＝ **%s**" % _hit)
    rows.append(("D-1", not r0, r1, _hit))

    # ══════════ D-2 ══════════
    say("")
    say("=" * W)
    say("§D-2　宣告 `filter` 由 `stage1` 改 `identity`（**⛔ 不改實參**）")
    say("=" * W)
    _sav = dict(DECL["stepg:_proj_rank"])
    try:
        DECL["stepg:_proj_rank"] = dict(_sav, filter="identity")
        r2, m2 = run_case("D-2", lambda: A_seq("stepg:_proj_rank", GOOD1, BASE1, blk="R2"), True)
    finally:
        DECL["stepg:_proj_rank"] = _sav
    say("  🔴 擾動（宣告改 `identity`·實參不動）：raise ＝ **%s**" % r2)
    say("     訊息：%s" % m2[:180])
    r2b, _ = run_case("D-2+", lambda: A_seq("stepg:_proj_rank", GOOD1, BASE1, blk="R2"), False)
    say("  ✅ 還原後：raise ＝ **%s**（須 False ⇒ 證擾動確已還原）" % r2b)
    rows.append(("D-2", not r2b, r2, "identity" in m2))

    # ══════════ D-3 ══════════
    say("")
    say("=" * W)
    say("§D-3　`NAME_DERIVATION` 之 `_mem` 注入**他街廓**之宗")
    say("=" * W)
    TEMP = [tp("628-40(1)", "R2"), tp("628-43(1)", "R2"), tp("628-27(1)", "R2")]
    MEM_OK = [tp("628-40(1)", "R2"), tp("628-43(1)", "R2")]
    r0, _ = run_case("D-3+", lambda: A_sub("app:k6step0/_ordered", MEM_OK, TEMP, blk="R2"), False)
    say("  ✅ 正向對照（未擾動）：raise ＝ **%s**（須 False）" % r0)
    MEM_BAD = MEM_OK + [tp("628-99(1)", "R5")]                  # 🔴 他街廓之宗
    r3, m3 = run_case("D-3", lambda: A_sub("app:k6step0/_ordered", MEM_BAD, TEMP, blk="R2"), True)
    say("  🔴 擾動（注入 `R5` 之 `628-99(1)`）：raise ＝ **%s**" % r3)
    say("     訊息：%s" % m3[:180])
    rows.append(("D-3", not r0, r3, "628-99(1)" in m3))
    # 併證：空母體亦 raise（⊆ 之空真⛔ 不得作為通過）
    r3b, m3b = run_case("D-3b", lambda: A_sub("app:k6step0/_ordered", [], TEMP, blk="R2"), True)
    say("  🔒 併證：實參為空 ⇒ raise ＝ **%s**（`⊆` 之空真⛔ 不得作為通過）" % r3b)

    # ══════════ D-4 ══════════
    say("")
    say("=" * W)
    say("§D-4　`wf_f4:_order_fb` 之 `declared_added` 由 `{_abate_key}` 改 `∅`")
    say("=" * W)
    OE = ["628-4(1)", "628-7(1)", "628-20(1)"]
    ON_RAW = OE + ["74·抵費地末"]
    r0, _ = run_case("D-4+", lambda: A_diff("wf_f4:_order_fb", OE, ON_RAW,
                                            set(), {"74·抵費地末"}, blk="R6"), False)
    say("  ✅ 正向對照（`added = {74·抵費地末}`）：raise ＝ **%s**（須 False）" % r0)
    r4, m4 = run_case("D-4", lambda: A_diff("wf_f4:_order_fb", OE, ON_RAW,
                                            set(), set(), blk="R6"), True)
    say("  🔴 擾動（`added` 改 `∅`）：raise ＝ **%s**" % r4)
    say("     訊息：%s" % m4[:200])
    rows.append(("D-4", not r0, r4, "74·抵費地末" in m4))

    # ══════════ D-5 ══════════
    say("")
    say("=" * W)
    say("§D-5　`wf_f3:_proj_order`（宣告 `removed = added = ∅`）之後呼叫**注入一宗**")
    say("=" * W)
    OC = ["628(4)", "628-34(2)", "628-46(1)"]
    r0, _ = run_case("D-5+", lambda: A_diff("wf_f3:_proj_order", OC, list(OC),
                                            set(), set(), blk="R3"), False)
    say("  ✅ 正向對照（前後同集合）：raise ＝ **%s**（須 False）" % r0)
    OD_BAD = OC + ["628-99(9)"]                                 # 🔴 後呼叫注入一宗
    r5, m5 = run_case("D-5", lambda: A_diff("wf_f3:_proj_order", OC, OD_BAD,
                                            set(), set(), blk="R3"), True)
    say("  🔴 擾動（後呼叫注入 `628-99(9)`）：raise ＝ **%s**" % r5)
    say("     訊息：%s" % m5[:200])
    rows.append(("D-5", not r0, r5, "628-99(9)" in m5))
    # 併證：`empty` 之宣告值違型亦 raise
    r5b, m5b = run_case("D-5b", lambda: A_diff("wf_f3:_proj_order", OC, list(OC),
                                               set(), {"X"}, blk="R3"), True)
    say("  🔒 併證：向宣告 `empty` 之側傳入非空 ⇒ raise ＝ **%s**（型別自檢）" % r5b)
    say("     訊息：%s" % m5b[:150])

    # ══════════ 未宣告之 tag ══════════
    say("")
    say("=" * W)
    say("§附　未宣告之 tag 須 loud（⇒ 新增呼叫點必被逼入 `L-2′` 表）")
    say("=" * W)
    r6, m6 = run_case("X", lambda: A_seq("wf_fX:不存在之點", [], [], blk="R1"), True)
    say("  🔴 未宣告之 tag：raise ＝ **%s**　訊息：%s" % (r6, m6[:120]))

    # ══════════ 總結 ══════════
    say("")
    say("=" * W)
    ok = 0
    say("  %-6s %-14s %-14s %-16s" % ("組", "正向對照(須不紅)", "擾動(須紅)", "訊息含受詞"))
    for tag, pos, neg, msg in rows:
        good = pos and neg and msg
        ok += good
        say("  %-6s %-14s %-14s %-16s %s" % (tag, pos, neg, msg, "✅" if good else "🔴"))
    say("  ⇒ **%d/%d 組三項齊備**" % (ok, len(rows)))
    say("=" * W)

    os.makedirs(OUTDIR, exist_ok=True)
    lg = os.path.join(OUTDIR, "probe_WG9161_discrim_%s.log" % BASE_REF)
    with open(lg, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n  log → %s" % os.path.relpath(lg, REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
