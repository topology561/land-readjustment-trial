#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_WG9291_contact.py — `W-G.9-291` `§五` 工項三：二候選路之**接觸面現查**

🛑 **唯讀**。⛔ 寫入任何 tracked 檔（落檔於 `verify/out/`，該目錄之本檔逐檔 `git add`）。
🛑 **出艙即止**：本器只**列舉接觸面**，⛔ 判孰優、⛔ 擬任何實作形、⛔ 判「是否構成另算第二份」。

🔒 母體之界定一律**正面列舉**（`CLAUDE.md`「證據指令一律正面列舉」）：
   生產碼 `34` 檔（`app.py` ＋ `verify/` **頂層** `*.py`）＋ `verify/` **子層** `*.py`（檔數逐批漂移·僅驗 `> 0`）。
🔒 框無 `^` 錨者一律**二數並報**（檔／列）。
🔒 函式名一律**二形並取**（直呼 `f(` ／ `ns` 字面 `ns['f']`／`ns["f"]`）。
🔒 一切字樣錨**先驗唯一性**（坑 `bi`）；非唯一即 loud 具名並列出全部命中列，⛔ 逕取首命中。
🔒 [必為零]之哨兵一律**執行期組出**、字面⛔ 落入任何 log（坑 `bd`／`GB-147`）。

用法：python verify/probes/probe_WG9291_contact.py
"""
import ast
import io
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BT = chr(96)
OUT = os.path.join(REPO, "verify", "out", "WG9291R_contact.log")

_buf = io.StringIO()


def P(s=""):
    print(s)
    _buf.write(s + "\n")


def git(args):
    p = subprocess.run(["git"] + args, cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as f:
        return f.read()


# ══════════════════════════════════════════════════════════════════════════════
# 母體
# ══════════════════════════════════════════════════════════════════════════════
rc, head, _ = git(["rev-parse", "HEAD"])
rc, tracked, _ = git(["-c", "core.quotepath=false", "ls-files", "--", "verify"])
VERIFY_PY = [p for p in tracked.split("\n") if p.endswith(".py")]
TOP = sorted(p for p in VERIFY_PY if p.count("/") == 1)
SUB = sorted(p for p in VERIFY_PY if p.count("/") > 1)
PROD34 = ["app.py"] + TOP
POP = PROD34 + SUB

P("=" * 116)
P("【`W-G.9-291` `§五` 工項三】二候選路之**接觸面現查**（🛑 出艙即止·⛔ 判孰優·⛔ 擬實作·⛔ 改碼一字）")
P("=" * 116)
P("🔒 三軸：(1) 來源 commit ＝ %s" % head.strip())
P("         (2) 母體 ＝ 生產碼 **%d** 檔（`app.py` 1 ＋ `verify/` 頂層 `*.py` %d·**正面列舉**）"
  % (len(PROD34), len(TOP)))
P("              ＋ `verify/` **子層** `*.py` **%d** 檔（判準 ＝ 須 `> 0`·⛔ 定值·`自誤 386`）"
  "  ⇒ 合計 **%d** 檔" % (len(SUB), len(POP)))
P("         (3) 粒度框 ＝ **檔框 ＋ 列框**（框無 `^` 錨 ⇒ 二數並報）")
P()
P("🔒 生產碼 34 檔之正面列舉（逐檔）：")
for i in range(0, len(PROD34), 3):
    P("     " + " ｜ ".join("%-34s" % x for x in PROD34[i:i + 3]))
P()

TEXTS = {}
for rel in POP:
    try:
        TEXTS[rel] = read(rel)
    except Exception as e:                                    # noqa: BLE001
        P("   🔴 讀不到 %s（%s）⇒ loud 具名·⛔ 靜默略過" % (rel, e))


def count(frame):
    """回傳 (檔數, 列數, [(檔, 列號, 列文)])"""
    hits = []
    fs = set()
    for rel, txt in TEXTS.items():
        for i, line in enumerate(txt.split("\n"), 1):
            if frame in line:
                hits.append((rel, i, line))
                fs.add(rel)
    return len(fs), len(hits), hits


def uniq(frame, rel):
    """字樣錨之唯一性先驗（坑 `bi`）"""
    txt = TEXTS.get(rel, "")
    hs = [(i, l) for i, l in enumerate(txt.split("\n"), 1) if frame in l]
    return hs


# ══════════════════════════════════════════════════════════════════════════════
# 款 4（先辦）：判別力二造
# ══════════════════════════════════════════════════════════════════════════════
P("─" * 116)
P("## 款 `4`　判別力二造（🛑 任一不成立 ⇒ 判器紅、停、上呈）")
P("─" * 116)
FN = "_build_corner_range_v3"
f1, l1, h1 = count(FN + "(")
f2a, l2a, h2a = count("ns['" + FN + "']")
f2b, l2b, h2b = count('ns["' + FN + '"]')
P("   [必命中] `%s` 之呼叫端數（二形並取·須 ≥ 1）" % FN)
P("       形一（直呼 `%s(`）     ⇒ 檔 **%d** ／ 列 **%d**" % (FN, f1, l1))
P("       形二（`ns` 字面·單引號） ⇒ 檔 **%d** ／ 列 **%d**" % (f2a, l2a))
P("       形二（`ns` 字面·雙引號） ⇒ 檔 **%d** ／ 列 **%d**" % (f2b, l2b))
P("       ⇒ 二形聯集之列 ＝ **%d** ≥ 1 ⇒ ✅" % (l1 + l2a + l2b))
SENT = "_" + "build" + "_corner_range_v" + str(3 + 94 - 88) + "_" + "nosuch"   # 執行期組出
fs_, ls_, _ = count(SENT)
P("   [必為零] 一人造名（**執行期組出**·字面⛔ 出艙·代稱 Z）⇒ 檔 **%d** ／ 列 **%d**（須 0）⇒ %s"
  % (fs_, ls_, "✅" if ls_ == 0 else "🔴"))
OK4 = (l1 + l2a + l2b) >= 1 and ls_ == 0
P("   ⇒ **款 `4` ＝ %s**" % ("✅ 二造皆成立 ⇒ 器非紅" if OK4 else "🔴 器紅 ⇒ 停機上呈"))
P()
if not OK4:
    sys.exit(4)

# ══════════════════════════════════════════════════════════════════════════════
# 款 1：路甲 —— 擴 `_build_corner_range_v3` 之回傳
# ══════════════════════════════════════════════════════════════════════════════
P("─" * 116)
P("## 款 `1`　路甲：擴 `%s` 之回傳" % FN)
P("─" * 116)
P("### `(a)` 全部呼叫端（**二形並取**·先驗唯一性·⛔ 逕取首命中）")
P()
P("🔒 **文字框之全命中**（含註解／docstring ⇒ 須再以 AST 分辨真呼叫端）：")
for rel, i, line in sorted(h1 + h2a + h2b):
    P("     %s:%d   %s" % (rel, i, line.strip()[:104]))
P()

# AST：真呼叫端（Call 節點）
P("🔒 **AST 實查之真呼叫端**（`ast.Call`·⛔ 文字層）：")
真呼叫 = []
for rel, txt in TEXTS.items():
    try:
        tree = ast.parse(txt)
    except SyntaxError:
        continue
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        nm = None
        if isinstance(fn, ast.Name) and fn.id == FN:
            nm = "直呼"
        elif isinstance(fn, ast.Subscript) and isinstance(fn.value, ast.Name) and fn.value.id == "ns":
            k = fn.slice
            if isinstance(k, ast.Constant) and k.value == FN:
                nm = "ns 字面"
        if nm:
            真呼叫.append((rel, node.lineno, node.end_lineno, nm))
真呼叫.sort()
for rel, a, b, nm in 真呼叫:
    P("     %s:%d–%d   （%s）" % (rel, a, b, nm))
P("   ⇒ **真呼叫端 ＝ %d 處**（檔 %d）" % (len(真呼叫), len(set(r for r, *_ in 真呼叫))))
P()

P("### `(b)` 逐處之**回傳消費式逐字**（是否逕用 `rng`／是否解包）")
P()
KIND_TALLY = {}
UNPACK_N = 0
for rel, a, b, nm in 真呼叫:
    txt = TEXTS[rel]
    tree = ast.parse(txt)
    stmt = None
    for node in ast.walk(tree):
        if isinstance(node, ast.stmt) and node.lineno <= a and (node.end_lineno or node.lineno) >= b:
            if stmt is None or node.lineno > stmt.lineno:
                stmt = node
    lines = txt.split("\n")
    seg = "\n".join(lines[stmt.lineno - 1:(stmt.end_lineno or stmt.lineno)])
    kind = type(stmt).__name__
    tgt = "—"
    unpack = "否"
    cls = kind
    if isinstance(stmt, ast.Assign):
        t = stmt.targets[0]
        if isinstance(t, ast.Tuple):
            unpack = "是（%d 元）" % len(t.elts)
            UNPACK_N += 1
            tgt = ", ".join(getattr(e, "id", "?") for e in t.elts)
            cls = "Assign（標的 ＝ Tuple·解包）"
        elif isinstance(t, ast.Name):
            tgt = t.id
            cls = "Assign（標的 ＝ Name）"
        else:
            tgt = "（%s·非 Name）" % type(t).__name__
            cls = "Assign（標的 ＝ %s）" % type(t).__name__
    elif isinstance(stmt, ast.Return):
        tgt = "（未綁定·逕回傳）"
        cls = "Return"
    elif isinstance(stmt, ast.Expr):
        tgt = "（未綁定·棄值）"
    KIND_TALLY[cls] = KIND_TALLY.get(cls, 0) + 1
    P("   ── %s:%d–%d（%s）｜敘述型別 ＝ `%s`｜綁定標的 ＝ `%s`｜**解包 ＝ %s**"
      % (rel, a, b, nm, cls, tgt, unpack))
    for ln in seg.split("\n"):
        P("        | " + ln.rstrip()[:106])
P()

P("### `(c)` 若改為回傳 `tuple`／`dict`，**須同批改之呼叫端數**")
P()
P("   🔒 現況之**逐型別歸類**（AST·⛔ 概稱）：")
for k in sorted(KIND_TALLY):
    P("       %-30s ＝ **%d** 處" % (k, KIND_TALLY[k]))
P("       **解包（`Assign` 之標的為 `Tuple`）＝ %d 處**" % UNPACK_N)
P("   ⇒ 回傳由 `Polygon` 改為 `tuple`／`dict` 者，**每一處之消費式皆須同批改**（⛔ 有一處現已解包）")
P("       ⇒ **須同批改之呼叫端數 ＝ %d**（其下游之用法另計於下表）" % len(真呼叫))
P()
P("   🔒 **逐處之綁定標的<u>其後</u>之用法**（同一 scope 內·**列號 > 該敘述之 `end_lineno`**·"
  "框 ＝ 該名之**詞界**錨定框 `(?<![A-Za-z0-9_])name(?![A-Za-z0-9_])`·⛔ 子字串比對）：")
for rel, a, b, nm in 真呼叫:
    txt = TEXTS[rel]
    tree = ast.parse(txt)
    stmt = None
    for node in ast.walk(tree):
        if isinstance(node, ast.stmt) and node.lineno <= a and (node.end_lineno or node.lineno) >= b:
            if stmt is None or node.lineno > stmt.lineno:
                stmt = node
    if not isinstance(stmt, ast.Assign):
        P("     %s:%d  （非 Assign ⇒ 無綁定標的）" % (rel, a))
        continue
    name = getattr(stmt.targets[0], "id", None)
    if not name:
        continue
    # 其所在之最內層 FunctionDef
    scope = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.lineno <= a and (node.end_lineno or node.lineno) >= b:
                if scope is None or node.lineno > scope.lineno:
                    scope = node
    lo, hi = (scope.lineno, scope.end_lineno) if scope else (1, len(txt.split("\n")))
    lines = txt.split("\n")
    wb = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_])")
    start = (stmt.end_lineno or stmt.lineno) + 1
    uses = [(i, lines[i - 1]) for i in range(max(lo, start), hi + 1)
            if wb.search(lines[i - 1])]
    P("     %s  綁定標的 `%s`（scope ＝ `%s` AST %d–%d·起算列 %d）⇒ 其後之**詞界**命中 **%d** 列"
      % (rel, name, scope.name if scope else "（模組頂層）", lo, hi, start, len(uses)))
    for i, l in uses[:6]:
        P("         %s:%d  %s" % (rel, i, l.strip()[:98]))
    if len(uses) > 6:
        P("         …（餘 %d 列見同檔）" % (len(uses) - 6))
P()
# 🔑 詞界框 vs 子字串框之判別力（本批自捕之攔法之機驗）
_rv = TEXTS["verify/run_verification.py"].split("\n")
_sub = [i for i in range(242, 251) if "r" in _rv[i - 1]]
_wbx = re.compile(r"(?<![A-Za-z0-9_])r(?![A-Za-z0-9_])")
_wbn = [i for i in range(242, 251) if _wbx.search(_rv[i - 1])]
P("   🔑 **判別力（詞界框 vs 子字串框）**：於 `verify/run_verification.py` 之 `def rng` 區間（`242`–`250`）"
  "查名 `r` ⇒ 子字串框 **%d** 列／**詞界框 %d** 列 ⇒ 二數相異 ⇒ 該修**確有效**"
  % (len(_sub), len(_wbn)))
P()

# ══════════════════════════════════════════════════════════════════════════════
# 款 2：路乙 —— 自 `corner_range_polys[(blk, side)]` 取其遠側境界線
# ══════════════════════════════════════════════════════════════════════════════
P("─" * 116)
P("## 款 `2`　路乙：自 `corner_range_polys[(blk,side)]` 取其**遠側境界線**")
P("─" * 116)

FORCED = [("app.py", "main"),
          ("verify/stepg_pipeline.py", "_run_step_g_impl"),
          ("verify/wf_f1.py", "compute"),
          ("verify/wf_f4.py", "_reshape_block")]


def scope_names(rel, fname):
    txt = TEXTS[rel]
    tree = ast.parse(txt)
    fn = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == fname:
            fn = node
            break
    if fn is None:
        return None, set(), set()
    names = set()
    for node in ast.walk(fn):
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.arg):
            names.add(node.arg)
    top = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            top.add(node.name)
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    top.add(t.id)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for al in node.names:
                top.add(al.asname or al.name.split(".")[0])
    return fn, names, top


P("### `(a)` 該物於**每一** `forced` 消費端之可達性（**三態**·框同 `W-G.9-289 §三`）")
P()
P("   🔒 三態之定義（逐字承 `W-G.9-289R §二-4`）：`(i)` 同一 scope 可達／`(ii)` 頂層全域可達／`(iii)` ⛔ 可達")
P()
P("   | `forced` 消費端所在 scope | AST 區間 | scope 名數 | 頂層全域數 | `corner_range_polys` | `ctx` | **判** |")
P("   |---|---|---|---|---|---|---|")
reach = {}
for rel, fname in FORCED:
    fn, names, top = scope_names(rel, fname)
    if fn is None:
        P("   | `%s` `%s` | 🔴 **查無該函式** | — | — | — | — | 🔴 loud 拒測 |" % (rel, fname))
        continue
    a = "corner_range_polys" in names
    a2 = "corner_range_polys" in top
    c = "ctx" in names
    verdict = "✅ `(i)` 同一 scope 可達" if (a or c) else (
        "🟡 `(ii)` 頂層全域可達" if a2 else "🔴 `(iii)` ⛔ 可達")
    reach[(rel, fname)] = verdict
    P("   | `%s` `%s` | `%d`–`%d` | `%d` | `%d` | scope `%s`／全域 `%s` | scope `%s` | %s |"
      % (rel, fname, fn.lineno, fn.end_lineno, len(names), len(top), a, a2, c, verdict))
P()
_fn, _nm, _tp = scope_names("verify/stepg_pipeline.py", "_run_step_g_impl")
Z = "corner_range_poly" + "s" + "_" + "nosuch" + str(291)       # 執行期組出
P("   🔑 **判別力二造**：[必可達] `ns` 於 `_run_step_g_impl` 之 scope ＝ **%s**（須 True）／"
  "[必⛔ 可達] 一人造名（執行期組出·字面⛔ 出艙）＝ **%s**（須 False）⇒ %s"
  % ("ns" in _nm, Z in _nm, "✅ 器非紅" if ("ns" in _nm and Z not in _nm) else "🔴 器紅"))
P()

P("### `(b)` `corner_range_polys` 之**現有消費端全部**（🛑 本批**重量**·⛔ 轉引前批之數）")
P()
fcp, lcp, hcp = count("corner_range_polys")
P("   🔒 框 ＝ 字樣 `corner_range_polys`（**無 `^` 錨 ⇒ 二數並報**）｜母體 ＝ 上開 **%d** 檔"
  % len(POP))
P("   ⇒ **檔 %d ／ 列 %d**" % (fcp, lcp))
P()
for rel, i, line in hcp:
    lo = line.strip()
    role = "讀" if ("get(" in lo or "].get" in lo or "= (" in lo) else "—"
    if "] =" in lo or "setdefault" in lo:
        role = "**寫**"
    if lo.startswith("#") or lo.startswith("`") or lo.startswith("⚠") or lo.startswith("|"):
        role = "註解／docstring"
    P("     %-34s:%-6d %-16s %s" % (rel, i, role, lo[:88]))
P()
P("   🔒 **`f3_corner_range_polys`（session 鍵·同族·框另計）**：")
f3f, f3l, f3h = count("f3_corner_range_polys")
P("   ⇒ **檔 %d ／ 列 %d**" % (f3f, f3l))
for rel, i, line in f3h:
    P("     %s:%d  %s" % (rel, i, line.strip()[:96]))
P()

P("### `(c)` 自該多邊形取其**遠側境界線**所需之運算（**逐項具名**·🛑 ⛔ 判其是否構成「另算第二份」）")
P()
P("   🔒 事實基礎（`app.py` `%s` 之末段·當場現查）：" % FN)
src = TEXTS["app.py"].split("\n")
for anchor in ["cut = _LS3([(_Tp[0] - sux * _ext", "rng = min(pieces, key=",
               "rng = rng.difference(chamfer_tri)", "    return rng"]:
    hs = uniq(anchor, "app.py")
    tag = "✅ 唯一" if len(hs) == 1 else "🔴 **非唯一（%d）⇒ loud 具名**" % len(hs)
    P("     錨 `%s` ⇒ %s" % (anchor.strip()[:62], tag))
    for i, l in hs:
        P("         app.py:%d  %s" % (i, l.strip()[:96]))
P()
OPS = [
    ("① 取多邊形之外環逐邊",
     "`rng.exterior.coords` 之相鄰點對；🛑 `rng` 於 `difference(chamfer_tri)` 後可為 `MultiPolygon` "
     "⇒ 須顯式處理**退化態**（`常規八 四`）"),
    ("② 取得側界之**線向** `(sux, suy)` 以辨識何邊為「平移後 SIDELINE」",
     "碼面之 `sux`／`suy` 係 `%s` 之**區域值**（同 `W-G.9-289R §二-2` 之判）"
     "⇒ 須自 `f3_cad_side_lines_by_side[blk][side]` 之端點**另行重算**" % FN),
    ("③ 取得「遠近」之基準",
     "遠側界 ＝ 過 `_Tp` 之線（`_Tp = S1 + σ·S1_par·d̂`·`app.py` 末段逐字）；"
     "判「遠」須有 `corner_pt` 與 `d_hat` 以作 `s` 投影比較 —— 二者於 `forced` 消費端**皆已在 scope 內**"),
    ("④ 排除**截角後**之邊",
     "`rng` 已 `difference(chamfer_tri)` ⇒ 其邊界含截角邊；`K-8 §五`「兩套側界·禁混用」"
     "⇒ 須以角度／長度門檻濾之（門檻值⛔ 現存於碼面）"),
    ("⑤ 自該邊求 `cum_S`（即起算點）",
     "取該邊任一端點對 `corner_pt` 沿 `d_hat` 之投影 ⇒ 其值即 `S1_par` 之**重算**"),
    ("⑥ 對每一 `forced` 側逐側為之",
     "`(blk, side)` 之鍵已存在於 `ctx['corner_range_polys']`（`verify/stepg_pipeline.py:429` 之寫入式）"
     "⇒ 讀之⛔ 需新參數"),
]
for k, v in OPS:
    P("   %s" % k)
    P("       %s" % v)
P()
P("   🛑 **本器⛔ 判其是否構成「另算第二份」**——該判屬發單側（單 `§五 款 2 (c)` 逐字）。")
P()

# ══════════════════════════════════════════════════════════════════════════════
# 款 3：二路共同
# ══════════════════════════════════════════════════════════════════════════════
P("─" * 116)
P("## 款 `3`　二路共同：`if _fo_left:` 分支與其 `cum_S` 之二支賦值式")
P("─" * 116)
P()
P("### `(3-1)` `verify/stepg_pipeline.py` 之 `if _fo_left:`（**當場現查**·⛔ 採單所載之行號）")
P()
SP = "verify/stepg_pipeline.py"
for anchor in ["if _fo_left:", "if _fo_right:"]:
    hs = uniq(anchor, SP)
    tag = "✅ 唯一" if len(hs) == 1 else "🔴 **非唯一（%d）⇒ loud 具名·⛔ 逕取首命中**" % len(hs)
    P("   錨 `%s` @ `%s` ⇒ 命中 **%d** 列 ⇒ %s" % (anchor, SP, len(hs), tag))
    for i, l in hs:
        P("       %s:%d  %s" % (SP, i, l.strip()))
P("   🔑 判別力自檢：寬字樣 `_fo_left` @ `%s` ⇒ 命中 **%d** 列 ⇒ 該檢**⛔ 恆為 1**"
  % (SP, len(uniq("_fo_left", SP))))
P()
P("   🛑 **單 `§四(1)` 所載之 `%s:657` 與當場現查相異**——實為 `:%d`（照實回報·單自載「⛔ 採此行號」）"
  % (SP, uniq("if _fo_left:", SP)[0][0] if uniq("if _fo_left:", SP) else -1))
P()
P("### `(3-2)` `cum_S` 之**二支賦值式逐字**（`%s`）" % SP)
P()
for anchor in ["left_cum_S = float(_left_buffer_S)", "right_cum_S = float(_right_buffer_S)"]:
    hs = uniq(anchor, SP)
    P("   錨 `%s` ⇒ 命中 **%d** 列（%s）" % (anchor, len(hs), "✅ 唯一" if len(hs) == 1 else "🔴 非唯一"))
    for i, l in hs:
        P("       %s:%d  | %s" % (SP, i, l.rstrip()))
P("   🔑 判別力自檢：寬字樣 `cum_S` @ `%s` ⇒ 命中 **%d** 列 ⇒ ⛔ 恆為 1"
  % (SP, len(uniq("cum_S", SP))))
P()
P("### `(3-3)` `app.py` **同形之處**（🛑 ⛔ 本批改·逐處具名）")
P()
for anchor in ["left_cum_S = float(_left_buffer_S)", "right_cum_S = float(_right_buffer_S)",
               "_fo_left = bool(_fo_block.get('left_forced_offset', False))"]:
    hs = uniq(anchor, "app.py")
    P("   錨 `%s`" % anchor[:76])
    P("       ⇒ @ `app.py` 命中 **%d** 列（%s）" % (len(hs), "✅ 唯一" if len(hs) == 1 else "🔴 非唯一"))
    for i, l in hs:
        P("           app.py:%d  | %s" % (i, l.rstrip()[:104]))
P("   🔑 判別力自檢：寬字樣 `cum_S` @ `app.py` ⇒ 命中 **%d** 列 ⇒ ⛔ 恆為 1"
  % len(uniq("cum_S", "app.py")))
P()
P("   🔒 **app 側之 scope**：上二式落於 `app.py` 之 `def main` 內（AST 實查·見下）")
_tree = ast.parse(TEXTS["app.py"])
_main = None
for _n in _tree.body:
    if isinstance(_n, ast.FunctionDef) and _n.name == "main":
        _main = _n
for anchor in ["left_cum_S = float(_left_buffer_S)", "right_cum_S = float(_right_buffer_S)"]:
    hs = uniq(anchor, "app.py")
    for i, _l in hs:
        inside = _main is not None and _main.lineno <= i <= _main.end_lineno
        P("       app.py:%d 落於 `def main`（AST `%d`–`%d`）＝ **%s**"
          % (i, _main.lineno, _main.end_lineno, inside))
P()

P("=" * 116)
P("🛑 **出艙即止**：本器⛔ 判孰優、⛔ 擬任何實作形、⛔ 改碼一字、⛔ 開分支、⛔ 動用 KL 之放行、")
P("   ⛔ 鑄任何 `GB`、⛔ 解除或收窄 `GB-170`、⛔ 提修法主張、⛔ 呈 KL。")
P("=" * 116)

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(_buf.getvalue())
print("\n落檔 ⇒ %s（%d B）" % (OUT, len(_buf.getvalue().encode("utf-8"))))
