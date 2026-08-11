# -*- coding: utf-8 -*-
r"""`W-G.9-8`：三支**真 app 路徑端到端複本**之**終止點**守護夾具。

## 受詞（🔒 ⛔ 逐字採考古 65 第四層——⛔ **不是**「三支跑不跑得通」）

> 守護閘之判準 **⛔ 不可寫成「該功能是否成功」**（在有既有另案時恆假、閘永紅而失義），
> 須寫成**受詞本身之命題**。

⇒ 本夾具之受詞 ＝ **「三支之終止點 ＋ 終止原因，與凍存者相符」**。

**為何**：`verify/wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py` 皆為
「app `_build_wf_ctx` → `wf_f0`→`f4` 全鏈」之端到端複本（其中 `wg_g3.py` 係
`CLAUDE.md` 所訂 **W-G 收官判準 ①** 之終驗工具），惟**三支皆不在任何自動流程內**
（`W-G.9-6` §6）。若以 `rc=0` 為判準掛入，將新增**三個永紅項** ＝ 把
`W-G.9-6`／`W-G.9-7` 剛修好的病**再造一次**。

## 🔒 設計意圖（**特性，不是缺陷**）

現況三支皆終止於**結構閘另案**（`理論＝實跑 破`）。
**該另案修好後，三支會跑得更遠 ⇒ 終止點改變 ⇒ 本夾具轉紅 ⇒ 逼人來看並更新凍存。**
⛔ 屆時**不得**逕自重凍了事——須確認「跑得更遠」確為預期，再更新。

## 沿用（⛔ 不另寫第二套正規化·`#20` 族）

正規化 `R1`／`R2`、三分類（類 I／II／III）、凍存格式與解析
**一律沿用** `verify/wv_reconcile.py`（`normalize`／`classify`／`report`／
`render_list`／`parse_list`）。⛔ 本檔**未新增任何**正規化規則或解析碼。

⚠️ 凍存檔沿用該格式，故每筆以 `🔴 FAIL  <腳本名>` 起頭——
**此處該標記之義為「終止記錄」**，⛔ 非「該腳本是一道失敗之閘」。

## 擷取範圍（⛔ 正面聲明）

每支之記錄 ＝ `rc=<n>` ＋ 其 **stderr 之全部非空行**（即 traceback ＋ 終止例外訊息），
經 `R1`／`R2` 正規化。⛔ **stdout 不入記錄**（其為進度輸出、含逐塊計數，噪音大）。
🔒 traceback **行號未正規化** ⇒ 若 raise 換了位置，落**類 II**，由人具名確認。

## 重跑
    python verify/fixture_e2e_termination.py            # rc=0 ⇒ 綠
    python verify/fixture_e2e_termination.py --freeze   # 產生／更新凍存
"""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import wv_reconcile as WR                                    # noqa: E402

SCRIPTS = ("wg_g1_smoke.py", "wg_g2_smoke.py", "wg_g3.py")
FROZEN = os.path.join(HERE, "out", "WG98_端到端複本_終止點凍存.txt")
RC = [0]


def red(msg):
    print(f"  🔴 {msg}")
    RC[0] = 1


def observe():
    """實跑三支，回 [(腳本名, [正規化後之終止記錄行])]。⛔ 不吞例外：rc 與 stderr 全入記錄。"""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    items = []
    for s in SCRIPTS:
        p = os.path.join(HERE, s)
        if not os.path.exists(p):
            red(f"腳本不存在：{s} ⇒ ⛔ 不得視為通過")
            items.append((s, ["(腳本不存在)"]))
            continue
        r = subprocess.run([sys.executable, p], capture_output=True, text=True,
                           encoding="utf-8", env=env, timeout=1800)
        rec = [f"rc={r.returncode}"] + [x.rstrip() for x in (r.stderr or "").splitlines()
                                        if x.strip()]
        items.append((s, [WR.normalize(x) for x in rec]))
    return items


def freeze():
    items = observe()
    os.makedirs(os.path.dirname(FROZEN), exist_ok=True)
    with open(FROZEN, "w", encoding="utf-8") as f:
        f.write(WR.render_list(items, "（實跑 verify/wg_g1_smoke.py 等三支之 stderr）",
                               "（現場實跑·無單一來源檔）", batch="W-G.9-8 端到端複本終止點"))
    # 🔒 考古 67 修法 ④：建檔後**立刻驗其存在並反讀**
    assert os.path.exists(FROZEN), "🔴 凍存檔未建立"
    back = WR.parse_list(open(FROZEN, encoding="utf-8").read())
    assert len(back) == len(items), f"🔴 反讀 {len(back)} 筆 ≠ 寫入 {len(items)} 筆"
    print(f"✅ 已凍存：{os.path.relpath(FROZEN, REPO)}（{len(items)} 支）")
    for nm, det in items:
        print(f"   {nm}：{det[0]}｜終止 ＝ {det[-1][:110] if len(det) > 1 else '(無 stderr)'}")
    return 0


def main():
    print("=" * 92)
    print("# `W-G.9-8` 夾具：三支端到端複本之**終止點**（⛔ 受詞非「跑不跑得通」）")
    print("=" * 92)
    # 🔒 考古 67 修法 ①：比較前先斷言兩端存在且非空
    if not os.path.exists(FROZEN):
        red(f"凍存不存在（{os.path.relpath(FROZEN, REPO)}）⇒ ⛔ 不得視為通過")
        return RC[0]
    frozen = WR.parse_list(open(FROZEN, encoding="utf-8").read())
    if not frozen:
        red("凍存解析出 0 筆 ⇒ ⛔ 空集合不得算通過")
        return RC[0]
    print(f"  凍存 ＝ {os.path.relpath(FROZEN, REPO)}（{len(frozen)} 支）")
    print("  ⚠️ 記錄 ＝ `rc` ＋ stderr 全部非空行（正規化後）；⛔ stdout 不入記錄")
    print("  ⚠️ traceback 行號**未**正規化 ⇒ raise 換位置 ⇒ 落**類 II**、須人具名確認")

    cur = observe()
    rc0, L = WR.report(WR.classify(frozen, cur), "端到端複本終止點")
    for x in L:
        print(x)
    if rc0:
        red("終止點／終止原因與凍存不符 ⇒ ⛔ 不得逕自重凍（見本檔 docstring「設計意圖」）")

    # ── 竄改自檢（⛔ 兩態皆印）────────────────────────────────────────────
    #   🔒 受詞 ＝ **終止記錄本身**——三支皆終止於此、該記錄即本夾具所擷取之物
    #      ⇒ **現查證明必被執行**（⛔ 非「不保證執行到之點」·考古 65 第五層）。
    print()
    print("─" * 92)
    print("【竄改自檢】人造「終止點提前」⇒ 必轉紅；還原 ⇒ 轉綠（⛔ 兩態皆印）")
    print("─" * 92)
    victim = cur[0][0]
    early = [(victim, ["rc=1", "RuntimeError: （合成）於更早階段即終止——W-G.9-8 竄改自檢"])] \
        + cur[1:]
    r_t, _ = WR.report(WR.classify(frozen, early), "竄改態")
    r_r, _ = WR.report(WR.classify(frozen, cur), "還原態")
    print(f"  竄改態（`{victim}` 之終止記錄換成更早階段）⇒ {'🔴 紅' if r_t else '✅ 綠'}")
    print(f"  還原態                                   ⇒ {'🔴 紅' if r_r else '✅ 綠'}")
    if r_t and not r_r:
        print("  ✅ 竄改自檢具鑑別力（竄改態紅 ∧ 還原態綠）")
    elif r_t and r_r:
        print("  ⚠️ 二態皆紅——本夾具此刻本即為紅；改判**相對**鑑別力：")
        only_t = {n for n, _ in WR.classify(frozen, early)["III"]}
        only_r = {n for n, _ in WR.classify(frozen, cur)["III"]}
        if victim in only_t - only_r:
            print(f"  ✅ 具鑑別力（`{victim}` 因竄改而**新出現**於類 III）")
        else:
            red("竄改自檢**無鑑別力** ⇒ 本夾具不得計入交付")
    else:
        red("竄改態未轉紅 ⇒ 竄改自檢**無鑑別力** ⇒ 本夾具不得計入交付")

    print()
    print("=" * 92)
    print(f"{'✅ 夾具 PASS' if RC[0] == 0 else '🔴 夾具 FAIL'}（rc={RC[0]}）")
    print("=" * 92)
    return RC[0]


if __name__ == "__main__":
    sys.exit(freeze() if "--freeze" in sys.argv else main())
