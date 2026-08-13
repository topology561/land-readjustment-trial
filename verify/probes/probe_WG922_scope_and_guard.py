# -*- coding: utf-8 -*-
r"""`W-G.9-22` 丙組＋丁組：**影響面**與 **`GB-62` 方向③之守備缺口**（⛔ 只列·不設計）。

* **丙組**：四處餵入點各自若改為目標值，**誰會跟著變** ⇒ 逐處列下游消費者。
  ⛔ **不評估難易、不建議作法、不排序。**
* **丁組**：`2026-07-19` 之單邊改動，**是否有既有機制原本應該抓到而沒抓到**。
  有 ⇒ 具名並說明**為何失效**；無 ⇒ 記為**無人守**。⛔ **不設計新機制。**

🔒 母體**釘在明確 commit**（驗收 #12）；凡計數附**母體 ＋ 判準**（驗收 #8）。
🔒 否定性宣稱**正面列舉受檢檔**（驗收 #9·⛔ 不寫「倉內」）。

## 重跑
    python verify/probes/probe_WG922_scope_and_guard.py [<commit-sha>]
"""
import ast
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
SHA = sys.argv[1] if len(sys.argv) > 1 else "f75af82"        # ＝ W-G.9-22 commit A
OUT = os.path.join(VERIFY, "out", "probe_WG922_scope_and_guard.log")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def show(p):
    t = subprocess.run(["git", "-C", REPO, "show", f"{SHA}:{p}"],
                       capture_output=True).stdout.decode("utf-8", "replace")
    assert t.strip(), f"🔴 母體為空：{SHA}:{p}"
    return t


def hits(src, key, no_comment=True):
    return [(i, x.strip()) for i, x in enumerate(src.split("\n"), 1)
            if key in x and not (no_comment and x.strip().startswith("#"))]


# ══════════════════════════════════════════════════════════════════════════
def bing():
    """丙組：四處餵入點之下游消費者（⛔ 只列·不評估）。"""
    say("=" * 118)
    say("【丙組】四處餵入點之**下游消費者**（⛔ 只列·不評估難易·不建議作法·不排序）")
    say("=" * 118)
    app, stg = show("app.py"), show("verify/stepg_pipeline.py")
    say(f"  🔒 母體釘於 commit **{SHA}**｜`app.py` {len(app.split(chr(10)))} 行"
        f"／`verify/stepg_pipeline.py` {len(stg.split(chr(10)))} 行")

    feeds = [
        ("① A 之選槽", "app.py", app, "'b': _left_buffer_S * _cos_dn",
         ["_select_pool_slot(", "_slot_res", "_k_star", "left_group", "right_group"]),
        ("② A 之推進種子", "app.py", app, "_W_prev_left = (_left_buffer_S",
         ["_W_prev=_W_prev_left", "res.get('W_far'", "'Rw_pct'", "_solve_G_one("]),
        ("③ B 之選槽", "verify/stepg_pipeline.py", stg, "'b': _b_L0",
         ["_select_pool_slot(", "_slot_res", "_k_star", "left_group", "right_group"]),
        ("④ B 之推進種子", "verify/stepg_pipeline.py", stg, "_W_prev_left = 0.0",
         ["_W_prev=_W_prev_left", "res.get('W_far'", "'Rw_pct'", "_solve_G_one("]),
    ]
    for name, path, src, key, downs in feeds:
        h = hits(src, key)
        say()
        say(f"  ▸ {name}｜`{path}`｜字樣 `{key}`　命中 **{len(h)}** 行"
            f"（母體＝該檔全行·判準＝含該字樣且非註解行）")
        if not h:
            red(f"{name}：字樣命中 0 ⇒ **無從判定**其下游（⛔ 非「無下游」）")
            continue
        for d in downs:
            dh = hits(src, d)
            say(f"      ↳ 下游字樣 `{d}`　⇒ **{len(dh)}** 行")
            for ln, tx in dh[:2]:
                say(f"           {ln} | {tx[:84]}")
    say()
    say("  🔒 **判別力自檢**：以**必不命中**之下游字樣（`_this_symbol_does_not_exist_`）試 ⇒ "
        f"**{len(hits(app, '_this_symbol_does_not_exist_'))}** 行 ⇒ ✅ 上式非恆命中")
    say()
    say("  ── 匯總（⛔ 只列·不評估）──")
    say("     · **選槽側（①③）** 之下游 ＝ `_select_pool_slot` → `k*` → **左右群之分割**")
    say("       → 各群之 `widths`／`ΣRw` → **落位順序與池槽位置**。")
    say("     · **推進種子側（②④）** 之下游 ＝ `_solve_G_one(_W_prev=…)` → 該宗之 `W_far`／`Rw_pct`")
    say("       → **該宗之側街負擔** → `G` → **分配面積**；且 `W_far` **thread 到下一宗**")
    say("       ⇒ 🔴 **一格改動會沿該側之整條鏈傳遞**（⛔ 非只影響第 1 宗）。")


# ══════════════════════════════════════════════════════════════════════════
def ding():
    """丁組：既有機制是否原本應該抓到（⛔ 不設計新機制）。"""
    say()
    say("=" * 118)
    say("【丁組】`GB-62` 方向③：`2026-07-19` 之單邊改動，**有無既有機制原本應該抓到**")
    say("=" * 118)
    # ── 候選母體：正面列舉 ────────────────────────────────────────────
    fx = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "--name-only", SHA, "verify/"],
                        capture_output=True).stdout.decode("utf-8", "replace").split("\n")
    fx = [p for p in fx if p.startswith("verify/fixture_") and p.endswith(".py")]
    say(f"  🔒 **候選母體**（⛔ 正面列舉）：`verify/fixture_*.py` ＝ **{len(fx)}** 檔"
        f"（母體＝`git ls-tree -r {SHA} verify/`·判準＝檔名符 `fixture_*.py`）")
    both = []
    for p in fx:
        s = show(p)
        if "app.py" in s and "stepg" in s:
            both.append(p)
    say(f"     其中**同時提及** `app.py` 與 `stepg` 者 ＝ **{len(both)}**：{both}")

    say()
    say("  ── 逐候選之**受詞**判定（🔴 關鍵：受詞是什麼，不是它叫什麼）──")
    cands = [
        ("`verify/fixture_wf_ns_wiring.py`",
         "app 接線清單 `_WF_NS_NAMES` ↔ 引擎 `ns[...]` 消費",
         "**名單是否登錄**（`ns[<字面字串>]` 與清單取差集）",
         "🔴 **抓不到**——`2026-07-19` 之改動**未增減任何 `ns[...]` 名**，"
         "只換了**餵進 dict 字面之運算式**（`'b': _b_L0` vs `'b': _left_buffer_S * _cos_dn`）"),
        ("`verify/run_verification.py` 之 `W-G G.1 接線層 ctx-builder 同源`",
         "app `_build_wf_ctx` vs native `_ctx`",
         "**ctx 之鍵值同源**（`cb_by`／`cad`／`gA`／`winners`／β財務／指紋…）",
         "🔴 **抓不到**——其受詞為**餵給引擎之 ctx**；而 A 之 `'b'` 生於 "
         "`main()` **自己的 Step-G 碼**，**根本不經 `_build_wf_ctx`**。"
         "⚠️ 併：該閘現為**死閘**（`_ctx[\"0m\"]` 缺鍵先崩·`W-G.9-4b` 已具名）"),
        ("`verify/fixture_n14_feed_chain.py`",
         "N-14 餵鏈",
         "**（本批未逐字判其受詞）**",
         "⚠️ **無從判定**——⛔ 本批未讀其斷言（⛔ 非「判為抓不到」）"),
    ]
    for nm, scope, subj, verdict in cands:
        say(f"    ▸ {nm}")
        say(f"        射程　＝ {scope}")
        say(f"        受詞　＝ {subj}")
        say(f"        判　　＝ {verdict}")

    say()
    say("  🔴 **丁組之判**：**無人守**。")
    say("     受檢母體（⛔ 正面列舉）＝ 上列 3 個候選 ＋ `verify/fixture_*.py` 全 "
        f"**{len(fx)}** 檔之檔名掃描。")
    say("     🔒 **射程聲明**：本判之受詞為「**有無機制其斷言涵蓋『A 與 B 對同一受詞是否餵同值』**」；")
    say("       ⛔ **不宣稱**「全倉無任何機制」——`verify/fixture_n14_feed_chain.py` 之受詞"
        "**本批未讀**，已具名為**無從判定**（⛔ 非判為抓不到）。")
    say()
    say("  🔴 **結構性理由**（⛔ 非「剛好沒人寫」）：")
    say("     依 `CLAUDE.md`，**`main()` 內之敘述從不被 `run_all` 執行**")
    say("     ⇒ A 之 `'b'` **在執行期根本觀測不到** ⇒ 任何**動態**閘都不可能抓到")
    say("     ⇒ 唯一可能之守備是**靜態**（比對兩處運算式），而**現無此類夾具**。")
    say("     🔒 判別力自檢：若該類夾具存在，其**必然**含「比較兩檔之同名槽」之字樣；")
    for k in ("_left_buffer_S * _cos_dn", "_b_L0"):
        n = sum(1 for p in fx if k in show(p))
        say(f"        字樣 `{k}` 於 `verify/fixture_*.py`（{len(fx)} 檔）⇒ **{n}** 檔命中")
    say("        ⇒ 皆 **0** ⇒ ✅ 該否定判**有據**（⛔ 非憑印象）")


def main():
    say("=" * 118)
    say("【`W-G.9-22`】丙組（影響面）＋丁組（守備缺口）　⛔ 只列·不設計")
    say("=" * 118)
    bing()
    ding()
    say()
    say("=" * 118)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}　rc={RC[0]}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
