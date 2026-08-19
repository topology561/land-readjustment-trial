#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""`W-G.9-74` **容差 vs 欄位粒度之全倉對照**（`K-8` 遷移項乙）　🔒 **只量不改**

**受詞**：對每一處「以容差比對之數值」，問——**該容差是否 ≥ 被比欄之粒度**？
若是，該檢**對一個粒度為盲**（`GB-27` 之形狀：`abs(G − exp) > 0.01` 而 `G` 於來源即
`round(..., 2)` ⇒ 有效解析度 `0.02㎡`，而 `0.01㎡` 正是法定面積粒度）。

────────────────────────────────────────────────────────────
🔒 **A-0　錯誤方向之事前選定（⛔ 本段寫於任何一行碼之前·考古節 98）**
────────────────────────────────────────────────────────────
本工具係**「找漏」之工具**。節 98 之通則：

> **偵測器往「多報」錯會吵、會被追；往「少報」錯會<u>安靜</u>，而安靜正是它要對抗的東西。**

⇒ 🔒 **本工具一律偏向「多報」**，具體為三條**寫死之取捨**：

1. **粒度不明 ⇒ 類丙（須人判）**，⛔ **不得**歸入「安全（類甲）」。
2. **樣式不確定 ⇒ 收進母體**（寧可多一筆待判，⛔ 不可少一筆）。
3. **範圍取捨一律具名**——本器唯一之排除為**本檔自身**（其 docstring 逐字引用了
   全部四式之樣式 ⇒ 自我匹配純為套套邏輯之偽命中）；⛔ **其餘一律不排除**，
   `probes/`／`fixtures/`／`tools/`／`archive/` **全收**，並逐目錄出艙其筆數。

🔴 **本器⛔ 不改任何容差、⛔ 不改任何錨**（施工單 §七-2）。

────────────────────────────────────────────────────────────
**四式（`--forms` 可退化以自證其必要）**
────────────────────────────────────────────────────────────
    甲 `abs(...) <|>|<=|>= <數值>`        直式容差比較
    乙 具名常數 `TOL`／`_tol`／`tol=`      具名容差
    丙 `isclose(`／`approx(`／`round(A,n) == round(B,n)`
    丁 比對器內建之容差（`diff_rows`／`_norm`／`wv_reconcile` 一族）

**粒度之來源（⛔ 逐項具名·⛔ 不得由「看起來像面積所以是 0.01」推定）**：
本器只承認**可指出出處**之粒度——自全倉建 `欄名 → round 位數` 之映射
（樣式 `"COL": round(..., n)`），再由命中行**上方 8 行內**之 `["COL"]`／`.get("COL"`
反查該行所比之欄。查不到 ⇒ **類丙**。

用法：
    python verify/tools/wg974_tol_vs_granularity.py
    python verify/tools/wg974_tol_vs_granularity.py --forms 甲     # 退化版（自證多式必要）
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
SELF = os.path.abspath(__file__)

# ── 四式 ─────────────────────────────────────────────────────────────
_NUM = r"[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"
RX = {
    "甲": re.compile(r"abs\s*\(.*?\)\s*(<=|>=|<|>)\s*(" + _NUM + r")"),
    "乙": re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*TOL[A-Za-z0-9_]*\b|\b[A-Za-z_][A-Za-z0-9_]*_tol\b|\btol\s*="),
    "丙": re.compile(r"\bisclose\s*\(|\bapprox\s*\(|round\s*\([^)]*\)\s*==\s*round\s*\("),
    "丁": re.compile(r"\bdiff_rows\b|\b_norm\b|\bnormalize\s*\(|\breconcile_text\b"),
}
_COL = re.compile(r"""\[\s*["']([^"']+)["']\s*\]|\.get\(\s*["']([^"']+)["']""")
_ROUND_COL = re.compile(r"""["']([^"']+)["']\s*:\s*round\s*\([^,]*,\s*([0-9]+)\s*\)""")
WINDOW = 8


def py_files():
    """母體之**可執行集合定義**：`verify/` 下全部 `*.py`，扣除 `__pycache__` 與**本檔自身**。"""
    out = []
    for a, d, fs in os.walk(VERIFY):
        d[:] = [x for x in d if x != "__pycache__"]
        for f in fs:
            if f.endswith(".py"):
                p = os.path.join(a, f)
                if os.path.abspath(p) != SELF:
                    out.append(p)
    return sorted(out)


def build_granularity_map(files):
    """全倉建「欄名 → (位數, 出處, 全部出處)」——樣式 `"COL": round(..., n)`。

    🔒 **本映射係<u>全倉按欄名</u>之映射** ⇒ **跨檔同名會誤配**（如 `expect`）。
      依 A-0 之選定，該誤配之方向為**多報**（把不相干之粒度套上去 ⇒ 類乙變多、待判變多），
      ⛔ **非少報** ⇒ **可接受**，惟**須於報告具名**。
    🔒 **另檢同名多源之位數是否一致**——不一致本身即為一項發現（回傳於 `conflict`）。
    """
    acc = {}
    for p in files:
        try:
            txt = io.open(p, encoding="utf-8", errors="replace").read()
        except Exception:                                           # noqa: BLE001
            continue
        for i, l in enumerate(txt.split("\n"), 1):
            for col, n in _ROUND_COL.findall(l):
                acc.setdefault(col, []).append((int(n), f"{os.path.relpath(p, REPO)}:{i}"))
    g, conflict = {}, {}
    for col, lst in acc.items():
        digits = {n for n, _ in lst}
        # ⛔ 多源位數不一致時取**最小位數**（＝**最粗**之粒度）——粒度愈粗，愈易判為類乙
        #   ⇒ 方向為**多報**（A-0）。
        n = min(digits)
        g[col] = (n, next(s for d, s in lst if d == n), len(lst))
        if len(digits) > 1:
            conflict[col] = sorted(lst)
    return g, conflict


def scan(files, forms=("甲", "乙", "丙", "丁")):
    hits = []                       # (path, lineno, form, line, tol)
    for p in files:
        try:
            lines = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
        except Exception:                                           # noqa: BLE001
            continue
        for i, l in enumerate(lines, 1):
            s = l.split("#", 1)[0]           # ⛔ 註解不算碼（惟字串內之 # 亦被切·屬「少報」風險
            if not s.strip():                #    ⇒ 故**另以全行**再掃一次·取聯集·偏多報）
                continue
            for f in forms:
                m = RX[f].search(s) or RX[f].search(l)
                if m:
                    tol, op = None, None
                    m2 = RX["甲"].search(s) or RX["甲"].search(l)
                    if m2:
                        op = m2.group(1)
                        try:
                            tol = float(m2.group(2))
                        except Exception:                           # noqa: BLE001
                            tol = None
                    hits.append((p, i, f, l.strip(), tol, op))
    return hits


def classify(hits, gmap, all_lines):
    """回 [(path,line,form,tol,col,gran,src,類)]。⛔ 粒度不明一律類丙。"""
    out = []
    for p, i, f, l, tol, op in hits:
        lines = all_lines[p]
        col = gran = src = None
        for j in range(max(0, i - 1 - WINDOW), i):
            for a, b in _COL.findall(lines[j]):
                c = a or b
                if c in gmap:
                    n, src, _cnt = gmap[c]
                    col = c
                    gran = 10.0 ** (-n)
                    break
            if col:
                break
        if tol is None or gran is None:
            k = "丙"
        elif tol < gran:
            k = "甲"
        else:
            k = "乙"
        out.append((p, i, f, tol, col, gran, src, k, op))
    return out


def inject_one_granularity(tol, op, gran):
    """🔴 **A-4 注入式一粒度變異**：把 `got` 側加上**恰一個粒度** ⇒ 該檢是否**轉紅**？

    🔒 **受詞（⛔ 精確界定）**：本函式**逐字重演該行之比較式**——以 `Δ = gran` 代入
      `abs(Δ) <op> tol`，回傳其真值。**⛔ 非重跑整條管線**；其所測者為
      **該比較式之「運算子 ＋ 容差」對「恰一個粒度」之反應**——而 `GB-27` 之要害正在此
      （`>` 嚴格不等式使 `Δ` 恰為 `0.01` 時**不觸發**）。
    ⚠️ **⛔ 不以「讀常數再推理」代替**：本式**實際求值**，故 `>` 與 `>=` 之差被真正走過。

    🩸 **極性（⛔ 首版寫反·`W-G.9-74` 自誤 2）**：「條件為真」**⛔ 不等於**「轉紅」——
      · `>`／`>=` 式 ＝ **違規述詞**（`abs(Δ) > tol` 為真 ⇒ **報出違規** ⇒ **轉紅**）；
      · `<`／`<=` 式 ＝ **近似斷言**（`abs(Δ) < tol` 為真 ⇒ **通過** ⇒ **⛔ 非轉紅**；
        其轉紅條件為該式**為偽**）。
      首版一律回傳條件之真值 ⇒ `<` 族之極性顛倒 ⇒ 類乙 8 筆中 7 筆被報成「竟轉紅」
      ——**與判類自相矛盾**，故當場現形。🔒 **表列「預期 vs 實得」是它現形的唯一原因。**
    """
    d = float(gran)
    cond = {"<": d < tol, "<=": d <= tol, ">": d > tol, ">=": d >= tol}[op]
    return cond if op in (">", ">=") else (not cond)


def main(argv):                                                     # noqa: C901
    forms = ("甲", "乙", "丙", "丁")
    if "--forms" in argv:
        forms = tuple(argv[argv.index("--forms") + 1].split(","))
    files = py_files()
    all_lines = {}
    for p in files:
        try:
            all_lines[p] = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
        except Exception:                                           # noqa: BLE001
            all_lines[p] = []
    gmap, gconf = build_granularity_map(files)

    W = 120
    print("=" * W)
    print("【`W-G.9-74`】容差 vs 欄位粒度之全倉對照（`K-8` 遷移項乙）　🔒 只量不改")
    print("=" * W)
    print("  🔒 **A-0 錯誤方向 ＝ 偏向「多報」**（節 98）：粒度不明／樣式不確定 ⇒ **類丙**，⛔ 不入「安全」。")
    print(f"  🔒 **母體（可執行之集合定義）** ＝ `verify/` 下全部 `*.py`，扣 `__pycache__` 與**本檔自身**"
          f"　⇒ **{len(files)} 檔**")
    _by_dir = {}
    for p in files:
        _by_dir[os.path.relpath(os.path.dirname(p), REPO).replace("\\", "/")] = \
            _by_dir.get(os.path.relpath(os.path.dirname(p), REPO).replace("\\", "/"), 0) + 1
    print("     逐目錄：" + "／".join(f"{k} {v}" for k, v in sorted(_by_dir.items())))
    print(f"  🔒 **粒度映射**（`\"COL\": round(...,n)`）⇒ **{len(gmap)}** 個欄名可指出出處")
    print(f"     ⚠️ **本映射係<u>全倉按欄名</u>** ⇒ 跨檔同名會誤配；其方向為**多報**（A-0）⇒ 可接受·**已具名**")
    print(f"     🔒 **同名多源而位數不一致者 ＝ {len(gconf)}**"
          + ("　⇒ " + "／".join(f"`{c}`{sorted({n for n, _ in v})}" for c, v in sorted(gconf.items())[:6])
             + ("…" if len(gconf) > 6 else "") if gconf else "（無）"))
    print("        （不一致時取**最小位數 ＝ 最粗粒度** ⇒ 愈易判類乙 ⇒ **偏多報**）")
    print(f"  🔒 本次採用之式 ＝ {'／'.join(forms)}"
          + ("　⚠️ **退化版**" if tuple(forms) != ("甲", "乙", "丙", "丁") else ""))
    print("")

    # ── 逐式涵蓋（單位 ＝ 命中行·母體 ＝ 上開檔集）─────────────────
    per = {f: scan(files, (f,)) for f in ("甲", "乙", "丙", "丁")}
    keyset = {f: {(p, i) for p, i, *_ in per[f]} for f in per}
    union = set().union(*keyset.values())
    print("  逐式涵蓋（單位 ＝ **命中行**）")
    for f in ("甲", "乙", "丙", "丁"):
        only = keyset[f] - set().union(*[keyset[g] for g in keyset if g != f])
        print(f"    式 {f} ⇒ **{len(keyset[f])}** 行　（**僅由本式涵蓋** ＝ {len(only)}）")
    print(f"    ⇒ **四式聯集（去重）＝ {len(union)} 行**")
    print("")

    hits = scan(files, forms)
    rows = classify(hits, gmap, all_lines)
    # 去重（同一行可能被多式命中）
    seen, uniq = set(), []
    for r in rows:
        k = (r[0], r[1])
        if k not in seen:
            seen.add(k)
            uniq.append(r)
    cnt = {"甲": 0, "乙": 0, "丙": 0}
    for r in uniq:
        cnt[r[7]] += 1
    print(f"  **判類（去重後 {len(uniq)} 行）**：甲 **{cnt['甲']}**／乙 **{cnt['乙']}**／丙 **{cnt['丙']}**")
    print("")
    print("  🔴 **類乙（容差 ≥ 粒度 ⇒ 對一個粒度為盲）逐項列名**")
    print(f"  {'檔:行':<52}{'式':<4}{'容差':>10}{'被比欄':<16}{'粒度':>8}  粒度出處")
    print("-" * W)
    for p, i, f, tol, col, gran, src, k, op in uniq:
        if k == "乙":
            print(f"  {os.path.relpath(p, REPO).replace(chr(92), '/') + ':' + str(i):<52}"
                  f"{f:<4}{tol:>10}{str(col):<16}{gran:>8}  {src}")
    print("-" * W)
    print(f"  ⇒ **類乙 ＝ {cnt['乙']} 筆**")
    print("")
    print(f"  ⚠️ **類丙 ＝ {cnt['丙']} 筆（須人判·⛔ 未推定為安全）**——逐項見下（前 40）")
    print(f"  {'檔:行':<52}{'式':<4}{'容差':>10}{'被比欄':<16}")
    print("-" * W)
    _c = [r for r in uniq if r[7] == "丙"]
    for p, i, f, tol, col, gran, src, k, op in _c[:40]:
        print(f"  {os.path.relpath(p, REPO).replace(chr(92), '/') + ':' + str(i):<52}"
              f"{f:<4}{str(tol):>10}{str(col):<16}")
    if len(_c) > 40:
        print(f"  …（另 {len(_c) - 40} 筆未顯示·🔒 **⛔ 非靜默截斷**·總數已於上行給出）")
    print("")

    # ══════════════════════════════════════════════════════════════
    print("=" * W)
    print("【A-4】注入式**一粒度**變異（⛔ 實測·⛔ 非讀常數）")
    print("=" * W)
    print("  🔒 **受詞**：以 `Δ = 一個粒度` 代入該行之 `abs(Δ) <op> tol` **實際求值**")
    print("     ⇒ 測其**運算子 ＋ 容差**對「恰一個粒度」之反應（`GB-27` 之要害）。⛔ 非重跑管線。")
    print("")
    _B = [r for r in uniq if r[7] == "乙" and r[8]]
    _A = [r for r in uniq if r[7] == "甲" and r[8]]
    print(f"  ── **類乙**（預期：**不轉紅** ＝ 盲）　母體 {len(_B)} 筆"
          + (f"·🔒 取樣規則 ＝ **依 `檔:行` 字典序取前 8 筆**" if len(_B) > 8 else "·**全取**"))
    print(f"  {'檔:行':<48}{'op':>4}{'容差':>9}{'粒度':>9}{'注入後轉紅?':>13}{'判':>6}")
    print("-" * W)
    _bad_b = 0
    for p, i, f, tol, col, gran, src, k, op in (sorted(_B, key=lambda r: (r[0], r[1]))[:8]
                                                if len(_B) > 8 else _B):
        red = inject_one_granularity(tol, op, gran)
        if red:
            _bad_b += 1
        print(f"  {os.path.relpath(p, REPO).replace(chr(92), '/') + ':' + str(i):<48}"
              f"{op:>4}{tol:>9}{gran:>9}{str(red):>13}"
              f"{('🔴 竟轉紅' if red else '✅ 盲'):>6}")
    print("-" * W)
    print(f"  ⇒ **類乙之注入：轉紅 {_bad_b} 筆／未轉紅（盲）{min(len(_B), 8) - _bad_b} 筆**")
    print("")
    print(f"  ── 🔒 **判別力（類甲·⛔ 不得省）**（預期：**須全數轉紅**）　母體 {len(_A)} 筆")
    print(f"  {'檔:行':<48}{'op':>4}{'容差':>9}{'粒度':>9}{'注入後轉紅?':>13}{'判':>6}")
    print("-" * W)
    _ok_a = 0
    for p, i, f, tol, col, gran, src, k, op in sorted(_A, key=lambda r: (r[0], r[1])):
        red = inject_one_granularity(tol, op, gran)
        if red:
            _ok_a += 1
        print(f"  {os.path.relpath(p, REPO).replace(chr(92), '/') + ':' + str(i):<48}"
              f"{op:>4}{tol:>9}{gran:>9}{str(red):>13}"
              f"{('✅ 紅' if red else '🔴 未紅'):>6}")
    print("-" * W)
    print(f"  ⇒ **類甲之注入：轉紅 {_ok_a}／{len(_A)}**"
          f"　{'✅ 注入器有效' if _ok_a >= 2 else '🔴 **注入器無效 ⇒ A-4 全部結果作廢**'}")
    print("")

    # ── 🔴 靜態判準 vs 實測之**不符**（⛔ 逐項具名·節 97）────────────
    print("  🔴 **靜態判準（A-2）vs 注入實測之不符——逐項具名**")
    print("     🔒 靜態判準（施工單 A-2 逐字）＝ `容差 ≥ 粒度 ⇒ 類乙`，**對運算子之嚴格性為盲**：")
    print("        · `>` ／ `<=` 之盲域 ＝ `粒度 ≤ 容差`　· `>=` ／ `<` 之盲域 ＝ `粒度 < 容差`（**嚴格**）")
    print("        ⇒ **`粒度 == 容差` 時二者分家**。")
    # ⛔ 母體限**可注入者**（`op`／`容差`／`粒度` 三者皆具）——類丙之 `粒度 is None`
    #   ⇒ 無從注入 ⇒ **不入本比較**（其待判狀態已於上方類丙清單具名·⛔ 非漏掉）
    _inj = [r for r in uniq if r[8] and r[3] is not None and r[5] is not None]
    _dis = [r for r in _inj
            if (r[7] == "乙") != (not inject_one_granularity(r[3], r[8], r[5]))]
    for p, i, f, tol, col, gran, src, k, op in sorted(_dis, key=lambda r: (r[0], r[1])):
        print(f"     🔴 {os.path.relpath(p, REPO).replace(chr(92), '/')}:{i}"
              f"　靜態判＝{k}／實測＝{'盲' if not inject_one_granularity(tol, op, gran) else '轉紅'}"
              f"　（op `{op}`·容差 {tol}·粒度 {gran}）")
    print(f"     ⇒ **不符 ＝ {len(_dis)} 筆**"
          + ("（🔒 其方向為**把非盲多報為盲** ⇒ **偏多報**·符合 A-0 ⇒ ⛔ 本批不改判準·只具名）"
             if _dis else ""))
    print("=" * W)
    return 0


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    sys.exit(main(sys.argv))
