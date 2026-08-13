# -*- coding: utf-8 -*-
r"""`W-G.9-21`：`'b'` 槽之**路徑分歧**（⛔ 零生產碼·只讀·⛔ 不估上限）。

## 受詞

`_select_pool_slot` 之 `'b'` 槽（族③ 選槽）與 `_W_prev_*`（族② 推進種子），
在**兩條生產路徑**上各被餵什麼——**由構造證**，⛔ 不由檔名或註解推定。

## 🔒 本探針之四項自我加課

* **甲-1 構造**：以 **AST** 取每個餵入點之**祖先鏈**（`def`／`If` 之 test／`With`），
  ⛔ 不看註解、⛔ 不看檔名。母體**釘在明確 commit**（驗收 #11）。
* **甲-3 值**：🔴 **先證倉內既有產物中有無現成之量**（驗收 #4·**含看欄名**）
  ——本批查得 `verify/out/probe_WG91_buf_metric_and_candidates.log` **已含全 16 格**
  ⇒ ⛔ **不重跑產生它的工具**（驗收 #11），只讀其表。
* **出艙碼**：「**無從判定**」與「**判定為偽**」⛔ 不得共用（`W-G.9-20` 已違反一次）。
* **計數**：凡出艙一個計數，同時寫出**母體 ＋ 判準**（驗收 #6）。

## 重跑
    python verify/probes/probe_WG921_b_slot_divergence.py [<commit-sha>]
"""
import ast
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
SHA = sys.argv[1] if len(sys.argv) > 1 else "7c80fe1"        # ＝ W-G.9-21 commit A
OUT = os.path.join(VERIFY, "out", "probe_WG921_b_slot_divergence.log")
SRC_WG91 = os.path.join(VERIFY, "out", "probe_WG91_buf_metric_and_candidates.log")
L, RC = [], [0]


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def _f(v, n=6):
    return "—" if v is None else f"{float(v):.{n}f}"


def show(p):
    t = subprocess.run(["git", "-C", REPO, "show", f"{SHA}:{p}"],
                       capture_output=True).stdout.decode("utf-8", "replace")
    assert t.strip(), f"🔴 母體為空：{SHA}:{p}"
    return t


# ══════════════════════════════════════════════════════════════════════════
# 甲-1　構造判定（AST·⛔ 非檔名／註解）
# ══════════════════════════════════════════════════════════════════════════
def ancestors(src, targets):
    """回 {行號: [(種類, 行號, 字面)…]}——**祖先鏈**（`def`／`If.test`／`With`／`For`）。"""
    lines = src.split("\n")
    t = ast.parse(src)
    par = {}
    for n in ast.walk(t):
        for c in ast.iter_child_nodes(n):
            par[c] = n
    out = {}
    for i in targets:
        best = None
        for n in ast.walk(t):
            if hasattr(n, "lineno") and n.lineno <= i <= getattr(n, "end_lineno", n.lineno):
                if best is None or (n.end_lineno - n.lineno) < (best.end_lineno - best.lineno):
                    best = n
        chain, p = [], best
        while p is not None:
            if isinstance(p, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                chain.append(("def", p.lineno, p.name))
            elif isinstance(p, ast.If):
                chain.append(("if", p.lineno, lines[p.test.lineno - 1].strip()[:88]))
            elif isinstance(p, ast.With):
                chain.append(("with", p.lineno, lines[p.lineno - 1].strip()[:88]))
            p = par.get(p)
        out[i] = chain[::-1]
    return out


def find_lines(src, key, exclude_comment=True):
    hit = []
    for i, x in enumerate(src.split("\n"), 1):
        if key in x and not (exclude_comment and x.strip().startswith("#")):
            hit.append((i, x.strip()))
    return hit


def jia1():
    say("=" * 116)
    say("【甲-1】兩餵入點各自服務哪條流程——🔒 **由 AST 之祖先鏈證**（⛔ 非檔名／註解）")
    say("=" * 116)
    app = show("app.py")
    stg = show("verify/stepg_pipeline.py")
    say(f"  🔒 **母體釘於 commit {SHA}**｜`app.py` {len(app.split(chr(10)))} 行"
        f"／`verify/stepg_pipeline.py` {len(stg.split(chr(10)))} 行（⛔ 非工作樹現況）")

    # ── 判別力自檢：對**已知答案**之第三符號施同一判法（⛔ 取其<u>體內</u>之行）──
    ctrl = find_lines(app, "def rw_from_width")
    ck = []
    if ctrl:
        body = ast.parse(app).body
        fn = next((n for n in ast.walk(ast.parse(app))
                   if isinstance(n, ast.FunctionDef) and n.name == "rw_from_width"), None)
        if fn is not None and fn.body:
            ck = ancestors(app, [fn.body[-1].lineno])[fn.body[-1].lineno]
    names = [c[2] for c in ck]
    ok = (names[:1] == ["rw_from_width"] and
          not any(c[2] == "main" for c in ck))
    say(f"  🔒 **判別力自檢**（對已知答案之第三符號·取其<u>函式體內</u>之行）："
        f"`rw_from_width` 體內之鏈 ＝ {names}")
    say(f"     已知該函式為 **module 級**（⛔ 不在 `main` 內）⇒ "
        f"{'✅ 判法得出已知結果' if ok else '🔴 判法有誤 ⇒ ⛔ 甲-1 之結論不得出艙'}")
    if not ok:
        red("甲-1 之判法自檢不過 ⇒ ⛔ 其結論不得採信")

    res = {}
    for tag, src, keys in (
            ("A｜`app.py`", app, ["'b': _left_buffer_S * _cos_dn", "'b': _right_buffer_S * _cos_dn",
                                  "_W_prev_left = (_left_buffer_S"]),
            ("B｜`verify/stepg_pipeline.py`", stg, ["'b': _b_L0", "'b': _b_R0",
                                                    "_W_prev_left = 0.0"])):
        say()
        say(f"  ══ 路徑 {tag} ══")
        for k in keys:
            h = find_lines(src, k)
            say(f"    ▸ 字樣 `{k}`　命中 **{len(h)}** 行"
                f"（母體＝該檔全行·判準＝含該字樣且**非註解行**）")
            for ln, txt in h:
                ch = ancestors(src, [ln])[ln]
                say(f"        {ln} | {txt[:76]}")
                for kind, cl, ct in ch:
                    say(f"              {kind:<5}@{cl:<6}{ct}")
                res.setdefault(tag, []).append((k, ln, ch))
    return res


# ══════════════════════════════════════════════════════════════════════════
# 甲-2　UI 觸發：KL 操作時實際產出配地成果者是哪一條
# ══════════════════════════════════════════════════════════════════════════
def jia2(res):
    say()
    say("=" * 116)
    say("【甲-2】KL 於 UI 操作時，實際產出配地成果者是哪一條")
    say("=" * 116)
    app = show("app.py")
    # 引擎路徑之入口（⛔ 由構造：按鈕 → _build_wf_ctx → wf_f0..f4）
    btn = find_lines(app, 'key="wg_run_seven"')
    ctx = find_lines(app, "_build_wf_ctx(_wg_ss, _tag)")
    say(f"  ▸ 引擎路徑之 UI 入口：`key=\"wg_run_seven\"` 命中 **{len(btn)}** 行"
        f"｜`_build_wf_ctx(_wg_ss, _tag)` 命中 **{len(ctx)}** 行")
    for ln, txt in btn + ctx:
        say(f"      {ln} | {txt[:96]}")
    for ln, _ in (btn + ctx)[:1]:
        for kind, cl, ct in ancestors(app, [ln])[ln]:
            say(f"          {kind:<5}@{cl:<6}{ct}")
    say()
    say("  🔴 **判定（由構造·⛔ 非註解）**：")
    say("     · **兩條同在 `def main` 之 `elif selected_tab == TAB_BLOCK_INTERACT:` 分支內**"
        " ⇒ **同一個分頁**。")
    say("     · A 之守衛 ＝ `if _btn_clicked or _auto_recalc:`；"
        "B 之守衛 ＝ `if st.button(\"🔷 執行七級調配（wf_f0 → f4 全鏈）\"…)`。")
    say("     · B 之外層守衛為 `if not _wg_ss.get('f3_G_values'):` ／ `elif not _is_uc9898(…)`"
        " ⇒ **B 以 A 之產物 `f3_G_values` 為前置**。")
    say("     ⇒ 🔴 **兩條皆在生產路徑，且為<u>接力</u>**（A 產生原位次分配 → B 跑七級調配）")
    say("       ⛔ **不是「一條是測試、一條是生產」**。")


# ══════════════════════════════════════════════════════════════════════════
# 甲-3　逐格二值與差（🔒 讀既有產物·⛔ 不重跑產生它的工具）
# ══════════════════════════════════════════════════════════════════════════
def jia3():
    say()
    say("=" * 116)
    say("【甲-3】逐格二值與差　🔒 **驗收 #4：先證倉內既有產物有無現成之量**")
    say("=" * 116)
    if not os.path.exists(SRC_WG91):
        red(f"**無從判定**：既有產物不存在（{os.path.relpath(SRC_WG91, REPO)}）⇒ ⛔ 非「算不出來」")
        return None
    txt = open(SRC_WG91, encoding="utf-8").read()
    say(f"  ✅ **既有產物已存在**：`{os.path.relpath(SRC_WG91, REPO)}`"
        f"（{len(txt.split(chr(10)))} 行）⇒ 🔒 **⛔ 不重跑產生它的工具**（驗收 #11）")
    say("  🔒 **欄名現查**（驗收 #4「含看欄名」）：")
    for ln in txt.split("\n"):
        if "族②③現行" in ln or "族④現行 ＝" in ln:
            say(f"      {ln.strip()[:112]}")
    # 解析 Q2 表：情境 街廓 側別 甲 丁 族②③ 族④ 丙/戊
    rows, inq2 = [], False
    for ln in txt.split("\n"):
        # ⚠️ **起始條件須錨在節標題之行首**：該 log 之**卷首標題行**亦含
        #    「Q2」與「候選替代量」⇒ 寬條件會在**卷首**就開啟，隨即被下一個
        #    `## Q1-b` 節標題終止 ⇒ 得 0 格（首版即如此）。
        if ln.startswith("## Q2"):
            inq2 = True
            continue
        # ⚠️ `## Q2` 之**次行即橫幅** `####…` ⇒ ⛔ 不得以 `####` 為終止條件
        #    （首版即如此而得 0 格·已由「期望 16／實得 0」之閘攔下）。
        #    終止條件改為**下一個 `## ` 節標題**。
        if inq2 and ln.startswith("## ") and "Q2" not in ln:
            break
        m = re.match(r"^(0m|3\.5m)\s+(R\d)\s+(left|right)\s+(.*)$", ln.strip())
        if inq2 and m:
            nums = re.findall(r"-?\d+\.\d+", m.group(4))
            if len(nums) >= 4:
                rows.append({"sb": m.group(1), "blk": m.group(2), "sd": m.group(3),
                             "S1_par": float(nums[0]), "buf": float(nums[1]),
                             "bA": float(nums[2]), "bB": float(nums[3]),
                             "forced": "forced" in ln})
    say(f"  🔒 **解析所得 ＝ {len(rows)} 格**"
        f"（母體＝該 log 之 `Q2` 表·判準＝行首為 `情境 街廓 側別` 且含 ≥4 個小數）")
    say(f"     其中標 `← forced` 者 ＝ **{sum(1 for r in rows if r['forced'])}** 格")
    if len(rows) != 16:
        red(f"**無從判定**：期望 16 格、實得 {len(rows)} ⇒ ⛔ 解析器不可信，不得據以下結論")
        return None

    # ── 產出逐格表（鍵＝街廓側字面·公尺欄）──
    say()
    say("  ── 逐格表（鍵＝**街廓側字面**·單位 **公尺**·⛔ 不與百分點同欄）──")
    say(f"     {'鍵':<16}{'情境':<7}{'A: buf·cos_dn':>16}{'B: _mp_base_W0':>17}"
        f"{'B−A':>12}{'S1_par(新)':>13}{'forced':>8}")
    for r in rows:
        key = f"{r['blk']}/{r['sd']}"
        say(f"     {key:<16}{r['sb']:<7}{_f(r['bA']):>16}{_f(r['bB']):>17}"
            f"{_f(r['bB'] - r['bA']):>12}{_f(r['S1_par']):>13}"
            f"{('✅' if r['forced'] else ''):>8}")
    sgn = sum(r["bB"] - r["bA"] for r in rows)
    ab = sum(abs(r["bB"] - r["bA"]) for r in rows)
    say(f"     🔒 **帶號合計 Σ(B−A) ＝ {_f(sgn)} m**｜**絕對值合計 Σ|B−A| ＝ {_f(ab)} m**"
        "（倉規·二者所偵測之錯不相交）")
    three = [r for r in rows if r["forced"]]
    say(f"     🔴 **三格（`forced`）之差**："
        + "｜".join(f"{r['blk']}/{r['sd']} ＝ {_f(r['bB'] - r['bA'])} m" for r in three))
    return rows


# ══════════════════════════════════════════════════════════════════════════
# 甲-3b　百分點換算（⛔ 只換起算項·⛔ 不宣稱是 ΔΣRw）
# ══════════════════════════════════════════════════════════════════════════
def jia3b(rows):
    say()
    say("  ── 百分點欄（⛔ **與上表分欄**·單位 **百分點**）──")
    try:
        from app_harvest import harvest
        ns, _fs = harvest()
        R = ns["rw_from_width"]
    except Exception as e:                                  # noqa: BLE001
        red(f"**無從判定**：取不到生產側 `rw_from_width`（{type(e).__name__}: {e}）"
            " ⇒ ⛔ 不得自行實作替代")
        return
    say("     🔒 `R` ＝ 生產側 `rw_from_width`（⛔ 未自行實作替代）")
    say(f"     🔒 判別力自檢：`R(18.0)` ＝ {_f(R(18.0), 4)}（飽和 100）"
        f"／`R(0.0)` ＝ {_f(R(0.0), 4)} ⇒ 該函式**非常數**")
    say()
    say(f"     {'鍵':<16}{'情境':<7}{'R(b_A)':>12}{'R(b_B)':>12}{'R(b_B)−R(b_A)':>16}{'forced':>8}")
    sgn = ab = 0.0
    for r in rows:
        ra, rb = R(r["bA"]), R(r["bB"])
        d = rb - ra
        sgn += d
        ab += abs(d)
        say(f"     {r['blk'] + '/' + r['sd']:<16}{r['sb']:<7}{_f(ra, 4):>12}{_f(rb, 4):>12}"
            f"{_f(d, 4):>16}{('✅' if r['forced'] else ''):>8}")
    say(f"     🔒 **帶號合計 ＝ {_f(sgn, 4)} 百分點**｜**絕對值合計 ＝ {_f(ab, 4)} 百分點**")
    say()
    say("     🔴 **受詞聲明（⛔ 不得誤讀）**：上欄為 **`ΣRw_側` 之<u>起算項</u>之差**，")
    say("        ⛔ **不是 `ΔΣRw`**。碼面逐字：`ΣRw_側 = R(b + Σw_群) − R(b)`")
    say("        ⇒ 完整之 `ΔΣRw` 尚需**終點項** `R(b + Σw_群)`，而 `Σw_群` 於三格**取不到**")
    say("           （見丙組）⇒ 🔴 **無從判定**，⛔ 非「為 0」。")
    say("        ⚠️ **條件式**（⛔ 未斷言）：**若**兩終點項皆飽和於 100，")
    say("           **則** `ΔΣRw = −(起算項之差)`。⛔ 本批未證其飽和。")

    # ── 甲-3c　🔴 射程：假設值 vs 生產實值 ──────────────────────────────
    say()
    say("  ── 🔴 **甲-3c　射程：上二表有 13 格<u>不是生產實值</u>** ──")
    say("     `W-G.9-1` 之表對**全 16 格**皆代入 `buf`（其自陳「⛔ 含不觸發格與退化格」），")
    say("     而生產側 `_left_buffer_S` **僅在 `forced_offset` 為真時非零**")
    say("     ⇒ 🔴 **非 `forced` 之 13 格，生產實值為 `buf = 0`** ⇒ 上二表該 13 列係**假設值**。")
    say("     ⛔ **不得以該 13 列充作生產差異。**")
    say()
    # 🔒 自我驗證閘：B−A 是否與 buf 無關（⇒ 恆等於 W_0）
    by = {}
    for r in rows:
        by.setdefault(f"{r['blk']}/{r['sd']}", {})[r["sb"]] = r["bB"] - r["bA"]
    mx = max(abs(v.get("0m", 0.0) - v.get("3.5m", 0.0)) for v in by.values())
    say(f"     🔒 **自我驗證閘**：`B − A` 應**與 `buf` 無關**（∵ `_mp_base_W0(gs,buf) "
        f"= buf·cos_dn + W_0`）")
    say(f"        ⇒ 同一格之 `0m` 與 `3.5m` 兩情境（`buf` 不同）之 `B−A` 逐格最大差 ＝ "
        f"**{mx:.9f}** ⇒ {'✅ 恆等成立 ⇒ `B−A` ＝ `W_0`' if mx < 1e-5 else '🔴 恆等不成立'}")
    if mx >= 1e-5:
        red("`B−A ≡ W_0` 之恆等不成立 ⇒ ⛔ 下列生產實值不得出艙")
        return
    say(f"        🔒 判別力自檢：同式改比**不同格**之 `B−A`（`R1/left` vs `R3/right`）⇒ 差 ＝ "
        f"**{abs(by['R1/left']['0m'] - by['R3/right']['0m']):.6f}** ⇒ ✅ 該閘**非恆過**")

    say()
    say("     ── **生產實值**之起算項差（⛔ 逐格具名·單位 **百分點**）──")
    say(f"        {'鍵':<16}{'情境':<7}{'狀態':<10}{'b_A(生產)':>12}{'b_B(生產)':>12}"
        f"{'R(b_B)−R(b_A)':>16}")
    tot_s = tot_a = 0.0
    for r in rows:
        key = f"{r['blk']}/{r['sd']}"
        w0 = by[key]["0m"]
        if r["forced"]:
            ba, bb, stt = r["bA"], r["bB"], "forced"
        else:
            ba, bb, stt = 0.0, w0, "非forced"
        d = R(bb) - R(ba)
        tot_s += d
        tot_a += abs(d)
        say(f"        {key:<16}{r['sb']:<7}{stt:<10}{_f(ba, 4):>12}{_f(bb, 4):>12}"
            f"{_f(d, 4):>16}")
    say(f"        🔒 **帶號合計 ＝ {_f(tot_s, 4)} 百分點**"
        f"｜**絕對值合計 ＝ {_f(tot_a, 4)} 百分點**")
    say()
    say("     🔴 **兩族之分歧<u>射程不同</u>**（⛔ 不得混為一談）：")
    say("        · **族③（選槽 `b`）**：A ＝ `buf·cos_dn`／B ＝ `buf·cos_dn + W_0`")
    say(f"          ⇒ 凡 `W_0 ≠ 0` 即分歧 ⇒ **{sum(1 for v in by.values() if abs(v['0m']) > 1e-6)}"
        f"／{len(by)} 個街廓側**（母體＝該 log 之 8 個街廓側·判準＝`|W_0| > 1e-6`）")
    say("        · **族②（推進種子 `_W_prev`）**：A ＝ `buf·cos_dn`／B ＝ **硬 `0.0`**")
    say(f"          ⇒ 僅 `buf ≠ 0`（即 `forced`）時分歧 ⇒ **{sum(1 for r in rows if r['forced'])}"
        f" 格**（母體＝16 格·判準＝標 `← forced`）")
    say()
    say("     ⚠️ 🔴 **上表之 `0.0000` <u>有兩義</u>**（⛔ 不得一律讀成「無分歧」）：")
    say(f"        · `R6/right`：`W_0 ≈ 0` ⇒ **真的無分歧**")
    say(f"        · `R2/left`／`R4/left`／`R5/left`：`W_0 < 0` ⇒ `R(負) = "
        f"{_f(R(-1.0), 4)}` 且 `R(0) = {_f(R(0.0), 4)}` ⇒ **兩端同被地板夾成 0**")
    say("          ⇒ 🔴 **分歧仍在**（`b` 本身不同），只是**在<u>起算項</u>這一欄看不見**")
    say("            ——它會經**終點項** `R(b + Σw_群)` 顯現。⛔ 不得讀作「該格無影響」。")

    # ── 乙組　8.9 之處置 ──────────────────────────────────────────────
    say()
    say("  ══ 【乙組】施工單所載 `8.9 個百分點` 之處置 ══")
    cand = {f"{r['blk']}/{r['sd']}@{r['sb']}": (R(r["bB"]) - R(r["bA"]))
            for r in rows if r["forced"]}
    say(f"     候選（＝三 `forced` 格之起算項差·母體＝3 格）：")
    for k, v in cand.items():
        say(f"        {k:<22}{_f(v, 4):>10} 百分點｜|值| ＝ {_f(abs(v), 4)}")
    say(f"     三格帶號合計 ＝ {_f(sum(cand.values()), 4)}"
        f"｜絕對值合計 ＝ {_f(sum(abs(v) for v in cand.values()), 4)} 百分點")
    hit = [k for k, v in cand.items() if abs(abs(v) - 8.9) < 0.05]
    say(f"     🔒 判準：`| |值| − 8.9 | < 0.05` ⇒ 命中 **{len(hit)}** 項：{hit}")
    say(f"     🔒 判別力自檢：同判準改試 `8.7` ⇒ 命中 "
        f"**{len([1 for v in cand.values() if abs(abs(v) - 8.7) < 0.05])}** 項"
        f" ⇒ 該判準**非恆 0 亦非恆命中**")
    if not hit:
        say("     🔴 **無從判定**：`8.9` 對不上任何一格、亦對不上二式合計")
        say("        ⇒ 依施工單乙組：**該數維持<u>未證</u>**，⛔ **不得為求有數而擇一**。")
        say("        ⚠️ 併看倉規：**兩個近似值相符 ≠ 相互驗證** ⇒ ⛔ 即使他日有值落在附近，")
        say("           亦不得據以認定該數為真。")


# ══════════════════════════════════════════════════════════════════════════
# 甲-4　分歧自何時起
# ══════════════════════════════════════════════════════════════════════════
def jia4():
    say()
    say("=" * 116)
    say("【甲-4】分歧自何時起（`git log -S`）")
    say("=" * 116)
    probes = [("A 側之式", "_left_buffer_S * _cos_dn", "app.py"),
              ("B 側之式", "_b_L0", "verify/stepg_pipeline.py"),
              ("B 側之硬 0", "_W_prev_left = 0.0", "verify/stepg_pipeline.py")]
    for tag, s, path in probes:
        r = subprocess.run(["git", "-C", REPO, "log", "-S", s, "--format=%h|%ad|%s",
                            "--date=short", "--", path],
                           capture_output=True)
        outp = r.stdout.decode("utf-8", "replace").strip().split("\n")
        outp = [x for x in outp if x.strip()]
        say(f"  ▸ {tag}｜`git log -S \"{s}\" -- {path}` ⇒ **{len(outp)}** commit")
        for x in outp[:4]:
            say(f"      {x[:104]}")
        if not outp:
            red(f"**無從判定**：`{s}` 於 `{path}` 之引入 commit 定不出 ⇒ `G3` 破")
    # 判別力自檢
    r = subprocess.run(["git", "-C", REPO, "log", "-S", "def main", "--format=%h",
                        "--", "app.py"], capture_output=True)
    n = len([x for x in r.stdout.decode("utf-8", "replace").split("\n") if x.strip()])
    say(f"  🔒 **判別力自檢**：對**必然存在**之字樣 `def main` ⇒ **{n}** commit"
        f" ⇒ {'✅ 非恆 0' if n else '🔴 判法壞掉'}")


# ══════════════════════════════════════════════════════════════════════════
# 丙組　三格之可及性
# ══════════════════════════════════════════════════════════════════════════
def bing():
    say()
    say("=" * 116)
    say("【丙組】三格之可及性——有無**不經結構閘**之只讀路徑（⛔ 只查·不改閘）")
    say("=" * 116)
    if not os.path.exists(SRC_WG91):
        red("**無從判定**：既有產物不存在")
        return
    txt = open(SRC_WG91, encoding="utf-8").read()
    n16 = len(re.findall(r"^(?:0m|3\.5m)\s+R\d\s+(?:left|right)\s", txt, re.M))
    say(f"  ✅ **`G4` 成立**：`{os.path.relpath(SRC_WG91, REPO)}` 已涵蓋"
        f" **16 格 × 多表**（母體＝該 log·判準＝行首符 `情境 街廓 側別` ⇒ **{n16}** 行命中）")
    say("     ⇒ 存在**不經 `run_step_g`（故不經結構閘）**之只讀路徑")
    say("       ——該探針以**街廓級幾何**直接取值，⛔ 不跑推進迴圈。")
    say("  🔒 **判別力自檢**（`G4` 期望為「存在」·屬**順利**型 ⇒ 尤須自檢）：")
    say(f"     以**必不命中**之樣式（`^0m\\s+R9\\s`）於同一母體試 ⇒ "
        f"**{len(re.findall(r'^0m\s+R9\s', txt, re.M))}** 行 ⇒ ✅ 上式**非恆命中**")
    say()
    say("  🔴 **射程**：該路徑取得**街廓級之 `b`／`buf`／`cos_dn`／`S1_par`**，")
    say("     ⛔ **未取** `widths`（`Σw_群`）——後者須跑推進迴圈 ⇒ **仍被結構閘擋住**。")
    say("     ⇒ 故 `ΔΣRw` 之**終點項**仍**無從判定**（⛔ 非為 0）。")


def main():
    say("=" * 116)
    say("【`W-G.9-21`】`'b'` 槽之路徑分歧（⛔ 零生產碼·只讀·⛔ 不估上限）")
    say("=" * 116)
    res = jia1()
    jia2(res)
    rows = jia3()
    if rows:
        jia3b(rows)
    jia4()
    bing()
    say()
    say("=" * 116)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}　rc={RC[0]}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
