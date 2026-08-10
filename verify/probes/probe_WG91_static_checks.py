# -*- coding: utf-8 -*-
"""`W-G.9-1` 靜態檢查：**P3**（`_cos_dn` 兩側同構）／**P4**（族②③ ≡ `GB-47` 四處殘存）
＋ `_left/_right_buffer_S` **消費者窮舉**（附差集自證）＋ **AST 呼叫數**。

⛔ 零生產碼、只讀不改。

## 🔒 射程聲明

- **消費者窮舉之母體** ＝ `grep -rn "_left_buffer_S\\|_right_buffer_S" --include=*.py .`
  **排除 `.claude/worktrees/`** ⇒ 基準 SHA 實跑 **31** 行
  （⚠️ 施工單 §3-1 載 `33`，**不可複現**·已於 commit A §0-1 具名）。
  ⇒ 本檔以 **31** 為母體，逐行分類並附**差集自證**（殘差須為 0）。
- **呼叫數** 一律以 **AST `ast.Call`** 為據（`func.id`／`func.attr`／`ns["…"]` 三形式全覆蓋）；
  ⛔ 禁裸 `grep -c`（考古節 60·我於 `D-2b-31` commit A 犯過一次）。
- **P3 之比對** ＝ 兩檔中「含 `_cos_dn` 指派之 `ast.If` 節點」之 `ast.dump`
  （`include_attributes=False` ⇒ 忽略行號／欄位）；⛔ 非逐字文字比對。
"""
import ast
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUT = os.path.join(VERIFY, "out", "probe_WG91_static_checks.log")
L = []


def say(s=""):
    L.append(s)
    print(s)


def _rd(rel):
    return io.open(os.path.join(REPO, rel), encoding="utf-8").read()


def py_files():
    out = []
    for dp, dns, fns in os.walk(REPO):
        dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
        rel = os.path.relpath(dp, REPO).replace("\\", "/")
        if rel == ".claude/worktrees" or rel.startswith(".claude/worktrees/"):
            dns[:] = []
            continue
        for fn in fns:
            if fn.endswith(".py"):
                out.append(os.path.relpath(os.path.join(dp, fn), REPO).replace("\\", "/"))
    return sorted(out)


def main():
    say("=" * 118)
    say("W-G.9-1 靜態檢查　P3 ／ P4 ／ 消費者窮舉（差集自證） ／ AST 呼叫數")
    say("=" * 118)

    files = py_files()
    say("")
    say("【射程】倉內 *.py ＝ %d 檔（⛔ 已排除 .claude/worktrees/）" % len(files))
    if not files:
        raise RuntimeError("🔴 母體為空 ⇒ ⛔ 不算通過")

    # ══════════════ P3 ══════════════
    say("")
    say("#" * 118)
    say("## P3　`app.py` 與 `verify/stepg_pipeline.py` 之 `_cos_dn` 構造是否**逐節點同構**")
    say("#" * 118)

    def _cos_if(rel):
        """定位「**test 本身**引用 `_n_alloc_blk`」之 `ast.If`。

        🩸 **首版設太鬆（當場自糾）**：首版以「**子樹** dump 含 `'_cos_dn'` 與
        `'_n_alloc_blk'`」為條件 ⇒ 把**一切祖先 `If`** 也算進去
        （`app.py` 得 13 個、`stepg` 得 2 個）⇒ 誤判為「P3 未取得證據」。
        **係我的匹配條件錯，非兩側真的不同構。**
        ⇒ 改以 **`n.test` 之 dump** 為條件——該層才是 `_cos_dn` 之計算閘。
        """
        t = ast.parse(_rd(rel))
        hits = []
        for n in ast.walk(t):
            if not isinstance(n, ast.If):
                continue
            if "'_n_alloc_blk'" in ast.dump(n.test, include_attributes=False):
                hits.append((n.lineno, ast.dump(n, include_attributes=False)))
        return hits

    a_hits, s_hits = _cos_if("app.py"), _cos_if("verify/stepg_pipeline.py")
    say("   `app.py` 命中 If 節點 %d 個（lineno=%s）" % (len(a_hits), [h[0] for h in a_hits]))
    say("   `stepg`  命中 If 節點 %d 個（lineno=%s）" % (len(s_hits), [h[0] for h in s_hits]))
    if len(a_hits) == 1 and len(s_hits) == 1:
        same = a_hits[0][1] == s_hits[0][1]
        say("   ⇒ `ast.dump` 逐節點比對：**%s**" % ("完全相同 ✅" if same else "🔴 相異"))
        if not same:
            say("   🔴 首處相異之字元位置 = %d"
                % next((i for i, (x, y) in enumerate(zip(a_hits[0][1], s_hits[0][1])) if x != y),
                       min(len(a_hits[0][1]), len(s_hits[0][1]))))
        say("   ⇒ **P3 %s**" % ("✅ 成立" if same else "🔴 破 ⇒ 兩側須分別出值·並進 GB-60"))
    else:
        say("   🔴 命中數非 1:1 ⇒ **P3 未取得證據**（⛔ 空集合／多重命中不算通過）")

    # ══════════════ P4 ══════════════
    say("")
    say("#" * 118)
    say("## P4　族②③ ＝ `GB-47` 所載之四處殘存（⛔ 非新增項）")
    say("#" * 118)
    reg = _rd("docs/reports/W-G.4_泛用阻塞項登記表.md")
    row = [ln for ln in reg.split("\n") if ln.startswith("| **GB-47**")]
    say("   `GB-47` 列命中 %d（須 1）" % len(row))
    if row:
        for kw in ("殘存實為 4 處", "_W_prev", "_select_pool_slot"):
            say("   · 該列含「%s」：%s" % (kw, "✅" if kw in row[0] else "🔴 否"))
    app_src = _rd("app.py").split("\n")
    fam = [("②-左", "_W_prev_left = (_left_buffer_S * _cos_dn)"),
           ("②-右", "_W_prev_right = (_right_buffer_S * _cos_dn)"),
           ("③-左", "'b': _left_buffer_S * _cos_dn"),
           ("③-右", "'b': _right_buffer_S * _cos_dn")]
    say("")
    say("   **族②③ 之四處（內容 grep 指認·⛔ 未沿用 `GB-47` 所載之舊行號）**：")
    n_ok = 0
    for tag, pat in fam:
        hit = [i + 1 for i, ln in enumerate(app_src) if pat in ln]
        say("   · %-5s `%s` ⇒ app.py:%s" % (tag, pat, hit if hit else "🔴 0 命中"))
        n_ok += 1 if len(hit) == 1 else 0
    say("   ⇒ 四處各恰 1 命中：**%d/4** ⇒ **P4 %s**"
        % (n_ok, "✅ 成立" if n_ok == 4 else "🔴 破"))

    # ══════════════ 消費者窮舉 ══════════════
    say("")
    say("#" * 118)
    say("## `_left_buffer_S`／`_right_buffer_S` 之**消費者窮舉**（母體 31·附差集自證）")
    say("#" * 118)
    # 🩸 **自我汙染之排除（當場自糾·⛔ 具名）**：本檔**自身原始碼**即含
    #   `_left_buffer_S`／`_right_buffer_S` 二字串（分類器之 pattern 與說明用），
    #   不排除則母體由 31 膨脹為 41（**差 10 ＝ 本檔自身之出現數**）
    #   ⇒ **量測器把自己量進去了**。
    #   ⛔ 排除範圍**僅限本批新增之探針**；`probe_K9_s62c_attribution.py` 之 2 行**仍在母體內**。
    _SELF = "verify/probes/probe_WG91_"
    pat = re.compile(r"_left_buffer_S|_right_buffer_S")
    pop, self_hits = [], 0
    for f in files:
        for i, ln in enumerate(_rd(f).split("\n"), 1):
            if pat.search(ln):
                if f.startswith(_SELF):
                    self_hits += 1
                else:
                    pop.append((f, i, ln.strip()))
    say("   母體 = **%d** 行（⛔ 已排除本批探針自身之 %d 行·見碼註之自我汙染說明）"
        % (len(pop), self_hits))
    say("   ⇒ 與 commit A §0-1 所載之基準值 **31** %s"
        % ("**相符** ✅" if len(pop) == 31 else "🔴 **不符**（須查）"))
    from collections import Counter as _C0
    for _f, _c in sorted(_C0(f for f, _, _ in pop).items()):
        say("      · %-46s %d 行" % (_f, _c))

    CLS = [("族①落位 s 累積", lambda s: "cum_S = float(" in s),
           ("族②W 鏈種子", lambda s: "_W_prev_" in s),
           ("族③選槽 b 參數", lambda s: "'b': _" in s),
           ("族④W₀ 基準", lambda s: "_mp_base_W0(" in s),
           ("族⑤診斷顯示", lambda s: "buffer_S': round(" in s or "_msg_buf" in s),
           ("初值 = 0.0", lambda s: re.search(r"_buffer_S = 0\.0", s) is not None),
           ("`_corner_buffer_S(` 呼叫／指派", lambda s: "_corner_buffer_S(" in s),
           ("顯示串／條件判斷", lambda s: ("> 0" in s or "f\"" in s or ':.2f' in s)),
           ("註解", lambda s: s.lstrip().startswith("#")),
           ("探針內之引用", lambda s: False)]
    cls_of = {}
    for f, i, s_ in pop:
        lab = None
        if f.startswith("verify/probes/"):
            lab = "探針內之引用"
        else:
            for name, fn in CLS:
                if fn(s_):
                    lab = name
                    break
        cls_of[(f, i)] = lab
    from collections import Counter
    cnt = Counter(v for v in cls_of.values() if v)
    say("")
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        say("   %-26s %d" % (k, v))
    resid = [(f, i, s_) for f, i, s_ in pop if cls_of[(f, i)] is None]
    say("")
    say("   【差集自證】母體 %d ∖ 已分類 %d ＝ **殘差 %d**（須 0）"
        % (len(pop), len(pop) - len(resid), len(resid)))
    for f, i, s_ in resid:
        say("   🔴 殘差 %s:%d  %s" % (f, i, s_[:70]))

    # ══════════════ AST 呼叫數 ══════════════
    say("")
    say("#" * 118)
    say("## AST 呼叫數（⛔ 禁裸 `grep -c`·考古節 60）")
    say("#" * 118)
    TARGETS = ("_corner_buffer_S", "_mp_base_W0", "_first_corner_alloc_dir",
               "_block_strip", "_strip_axis")
    for name in TARGETS:
        rowsn = []
        for f in files:
            try:
                t = ast.parse(_rd(f))
            except SyntaxError:
                continue
            for n in ast.walk(t):
                if not isinstance(n, ast.Call):
                    continue
                fn_ = n.func
                if (isinstance(fn_, ast.Name) and fn_.id == name) or \
                   (isinstance(fn_, ast.Attribute) and fn_.attr == name) or \
                   (isinstance(fn_, ast.Subscript) and isinstance(fn_.value, ast.Name)
                        and fn_.value.id == "ns" and isinstance(fn_.slice, ast.Constant)
                        and fn_.slice.value == name):
                    rowsn.append((f, n.lineno))
        prod = [x for x in rowsn if not x[0].startswith(("verify/probes/", "verify/fixture"))]
        say("   %-26s 全倉 %2d 處／**生產碼 %2d 處**" % (name, len(rowsn), len(prod)))
        for f, ln in prod:
            say("        · %s:%d" % (f, ln))

    say("")
    say("rc = 0")
    return 0


if __name__ == "__main__":
    rc = main()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    sys.exit(rc)
