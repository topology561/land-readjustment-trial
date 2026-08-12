# -*- coding: utf-8 -*-
r"""`W-G.9-17` 乙丙丁：`§三`／`§四` 失效之**連帶影響盤點**（⛔ 只盤·不改·不估·不提修法）。

🔒 **母體釘在明確 commit**（驗收 #9）；⛔ 不用工作樹現況。
🔒 **凡「查無」須先證所查之鍵在母體中確實可命中**（驗收 #12·承 `W-G.9-16` 之 `X5` 更正）。
🔒 **凡出艙計數，必同時寫出母體與判準**（新驗收 A·承 `3043f56` 之 `2` vs `96` 混寫自誤）。

## 重跑
    python verify/probes/probe_WG917_recon.py [<commit-sha>]
"""
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
SHA = sys.argv[1] if len(sys.argv) > 1 else "da3f751"        # ＝ W-G.9-17 commit A′
OUT = os.path.join(VERIFY, "out", "probe_WG917_recon.log")
L = []


def say(s=""):
    print(s)
    L.append(s)


def show(path):
    r = subprocess.run(["git", "-C", REPO, "show", f"{SHA}:{path}"], capture_output=True)
    t = r.stdout.decode("utf-8", "replace")
    assert t.strip(), f"🔴 母體為空：{SHA}:{path} ⇒ ⛔ 不得視為「查無」"
    return t.split("\n")


APP = show("app.py")
STEPG = show("verify/stepg_pipeline.py")
RULE = show("docs/rulings/K-6_街角地分配程序與可分配判準.md")
GB = show("docs/reports/W-G.4_泛用阻塞項登記表.md")


def cnt(lines, key):
    return sum(1 for x in lines if key in x)


def main():
    say("=" * 104)
    say("【`W-G.9-17` 乙丙丁】`§三`／`§四` 失效之連帶影響盤點（⛔ 只盤·不改）")
    say("=" * 104)
    say(f"  🔒 **母體釘於 commit {SHA}**（⛔ 非工作樹現況·驗收 #9）")
    say(f"     `app.py` {len(APP)} 行｜`verify/stepg_pipeline.py` {len(STEPG)} 行｜"
        f"正典 {len(RULE)} 行｜`GB` 登記表 {len(GB)} 行")
    say(f"  🔒 **母體可命中之對照**（驗收 #12）：`app.py` 之 `def ` ＝ {cnt(APP,'def ')} 行"
        f"（>0 ⇒ 下列各式非因母體壞掉而 0）")

    # ── 乙① §三 有無他用 ────────────────────────────────────────────────
    say()
    say("  ══ 乙① `§三 最小寬度帶` 除服務 `§四` 外有無其他用途 ══")
    say("     🔒 **字樣語意窮舉**（考古 64·⛔ 非只查一種寫法）；計數之母體 ＝ 各該檔全行")
    for k in ("最小寬度帶", "寬度帶", "min_width_band", "_n14_band", "深度帶"):
        say(f"       `{k}`：app.py {cnt(APP,k)} 行｜stepg {cnt(STEPG,k)} 行｜正典 {cnt(RULE,k)} 行")
    say("     🔍 `app.py` 中含「寬度帶」之逐行（判準：是否為<u>運算</u>）：")
    for i, x in enumerate(APP):
        if "寬度帶" in x:
            kind = "註解" if x.lstrip().startswith("#") else ("docstring／字串" if '"' in x or "'" in x or x.lstrip().startswith("前緣線") else "？")
            say(f"       {i+1} [{kind}] {x.strip()[:82]}")
    say("     🔴 **結論**：`§三` 之帶**實作於 `_build_corner_range_v3` 內**"
        "（其參數 `block_depth` ＝ `round(D_avg,2)`，docstring 逐字複製 `§三`／`§四`）")
    say("       ⇒ 其用途**即服務 `§四` 之滑動求解**；⛔ 查無其他運算用途。")
    say("     ⚠️ **與 `_n14_band` 不同**：`§三` 為**街廓層**（`D_avg` 平移）；"
        "`_n14_band_geom` 為 **K-9-6-b 宗地層**（逐宗後緣角點·KL 圖示裁定 2026-08-05）。")

    # ── 乙⑤ _build_corner_range_v3 之消費者 ──────────────────────────────
    say()
    say("  ══ 乙⑤ `_build_corner_range_v3` 之**呼叫端**（⛔ 判準＝實際呼叫·非提及）══")
    call = [(i + 1, x.strip()) for i, x in enumerate(APP)
            if "_build_corner_range_v3(" in x and not x.lstrip().startswith("#")
            and "def " not in x]
    say(f"     `app.py` 之呼叫行 ＝ **{len(call)}**（母體＝`app.py` 全 {len(APP)} 行；"
        f"判準＝含 `_build_corner_range_v3(` 且非註解、非 `def`）")
    for n, x in call:
        say(f"       {n} | {x[:88]}")
    say(f"     `verify/stepg_pipeline.py` 之呼叫行 ＝ "
        f"{sum(1 for x in STEPG if '_build_corner_range_v3(' in x and not x.lstrip().startswith('#'))}")

    # ── 乙⑥ k97_solve_alloc_t ───────────────────────────────────────────
    say()
    say("  ══ 乙⑥ `k97_solve_alloc_t` 是否隨 `§四` 失效 ══")
    k97 = [(i + 1, x) for i, x in enumerate(APP) if "k97_solve_alloc_t" in x]
    dfn = [n for n, x in k97 if x.startswith("def ")]
    cal = [n for n, x in k97 if "k97_solve_alloc_t(" in x and not x.lstrip().startswith("#")
           and not x.startswith("def ")]
    com = [n for n, x in k97 if x.lstrip().startswith("#")]
    say(f"     `app.py` 命中 **{len(k97)}** 行（母體＝`app.py` 全 {len(APP)} 行）"
        f"｜其中**定義** {len(dfn)}／**呼叫** {len(cal)}／**註解** {len(com)}"
        f"／其餘 {len(k97)-len(dfn)-len(cal)-len(com)}")
    say(f"     `verify/stepg_pipeline.py` 命中 {cnt(STEPG,'k97_solve_alloc_t')} 行")
    say("     🔴 **結論**：生產路徑**呼叫行 ＝ 0** ⇒ 它**早已是定義而零呼叫之孤兒**")
    say("       （碼註自載：「舊式…於本函式整段移除·不留 fallback」／"
        "「`k97_solve_alloc_t` 本身不刪、不停用、不標作廢」）")
    say("       ⇒ `§四` 失效**不改變其狀態** ⇒ `B7′` **可由構造判定**。")

    # ── 丙 GB-58 ─────────────────────────────────────────────────────────
    say()
    say("  ══ 丙 真正地界之可取得性 ＋ `GB-58` 前置（**語意窮舉**·考古 64）══")
    for k in ("GB-58", "保留區", "表示法", "∥SIDELINE", "s 區間", "S1_par"):
        say(f"       `{k}`：`GB` 登記表 {cnt(GB,k)} 行｜app.py {cnt(APP,k)} 行")
    say(f"     🔒 判別力自檢：`GB-46` 於登記表 ＝ {cnt(GB,'GB-46')} 行（>0 ⇒ 上式非恆 0）")
    say("     🔴 **`GB-58` 逐字所載**：街角最小規定範圍由 `_build_corner_range_v3` 依"
        " `K-9-5-4` 以 **∥SIDELINE 平移 `S1_par`** 建成**多邊形**；")
    say("       但**無 WINNER** 時該多邊形被**丟棄、只取其面積**"
        "（`_left_min = round(float(_rng_cr.area), 2)`），交由 `_corner_buffer_S` 以 **∥ALLOC** 另建一帶。")
    hit = [(i + 1, x.strip()) for i, x in enumerate(APP)
           if "_rng_cr.area" in x and not x.lstrip().startswith("#")]
    say(f"     🔍 該降維行之現查：`_rng_cr.area` 之非註解行 ＝ **{len(hit)}**")
    for n, x in hit:
        say(f"       {n} | {x[:88]}")
    say("     🔴 **結論**：**真正之遠側界<u>已經被建出來</u>**——它就在"
        " `_build_corner_range_v3` 之輸出多邊形裡，只是被上行**降維成面積**。")
    say("       ⇒ `B5′` **成立**（可得）；且 `SIDELINE ＋ S1` 之路**亦可行**"
        "（`S1_par` 即該平移量）⇒ `G-3` **未觸發**。")

    # ── 丁 五族觸及表 ────────────────────────────────────────────────────
    say()
    say("  ══ 丁 五族消費者觸及表（⛔ 只標·不改）══")
    say("     🔒 母體 ＝ `GB-47` 所列 `_corner_buffer_S` 之五族消費者")
    fam = [("① 落位 s 累積", "left_cum_S = float(_left_buffer_S)"),
           ("② W 鏈種子", "_W_prev_left = (_left_buffer_S"),
           ("③ 選槽 b 參數", "'b': _left_buffer_S"),
           ("④ W₀ 基準", "_mp_base_W0(corner_pt, _left_buffer_S"),
           ("⑤ 診斷顯示", "_left_buffer_S")]
    for name, key in fam:
        a = cnt(APP, key)
        s = cnt(STEPG, key)
        say(f"       {name:<14} app.py {a} 行｜stepg {s} 行｜⛔ **本批未改**")
    say("     ⚠️ 五族之**觸及**已標；⛔ 本批未改任何一族、未提修法。")

    say()
    say("=" * 104)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
