#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-96**：乙落地驗收靶（三不變式）之**現況量測** ＋ **落地後閘之預寫**。

## 受詞（施工單 `W-G.9-96` §二）

乙 ＝ `K-9-11`／`K-9-9 四` 之「不配地 ＋ 投影序號下一位遞補該位次 ＋ 騰出之地入調配池」。

- **不變式 II**（遞補下一位）＝ 生產函式 `_projection_order` 回傳序列之**次一元素**。
- **不變式 I**（不配地之三獨立判準）：`I-A` 地界線交叉／`I-B` 零合格垂線／`I-C` 矩形容納（負向）。
- **不變式 III**（入池母體分帳）：乙甲產物 vs `K-6:109` 第二來源**分帳**。

🔒 本檔**⛔ 不實作**上列任何一條——只**量現況**並把它們寫成「落地後哪裡會紅」。

## 🛑 紅線（施工單 §零）

⛔ 零 `app.py`／`verify/stepg_pipeline.py`／`verify/wf_f*.py`／`verify/wd4_tier_list.py`／
`verify/run_verification.py`／`verify/selection_pipeline.py` 變更；⛔ `data/`／`verify/baselines/**` 零變更；
🛑 ⛔ **不跑 `run_all`／`run_step_g`／`run_corner_pk`**（本檔以**覆蓋為 raise 版**機械證明其未被呼叫·見 `§0-3`）；
⛔ 不移線、不建介面、不落地、不換圖／不換快照／不重烤；
⛔ **不得就遞補／調配池／合併調配／超配出任何裁定題**（`K-9-11 三`）。

## 🔒 本檔**可跑**者之逐項具名（⛔ 非管線）

`app_harvest.harvest`（＝ `exec(app.py)` 取真符號·**非**管線）／`run_verification.load_snapshot`／
`run_verification.build_pipeline`（CAD 解析·唯讀）／`run_verification.build_ownership`（xlsx 唯讀）／
`selection_pipeline.build_build_parcels`（宗地建置·唯讀）。
🩸 **`build_ownership` 為<u>硬前置</u>**：不呼叫則 `所屬街廓` **靜默給錯**（本批自捕·詳報告 §I-1）。

## 🔒 常設條款之落實

**8** 每判準附「會使它為否」之輸入（`§B-3` 對調判別力／`§D-3` 合成證偽之設計）；
**10** 每表末印 `POPULATION／PRINTED／SUPPRESSED`；
**11**（節 111）哨兵／陰性對照字樣**執行期組出**、⛔ 不寫死於原始碼；
**14** 分離之宣稱一律單一門檻＋`m／n` 併出艙；
**15**（節 110）解釋既有款之效力須逐字引原文。

## 重跑

    python verify/probes/probe_WG996_yi_invariants.py

rc **恆為 0**；唯缺件／取不到資料時 loud raise（`no-silent-fallback`）。
"""
import ast
import contextlib
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

OUTDIR = os.path.join(VERIFY, "out")
WIDTH = 150

# 🔒 本檔自身之產物（母體自證時扣除·節 72 自誌）
SELF = [
    "verify/probes/probe_WG996_yi_invariants.py",
    "verify/out/probe_WG996_yi_invariants_ba0af85.log",
    "docs/reports/W-G.9-96_乙落地驗收靶.md",
]

# 🔒 **生產路徑之定義**＝施工單 §零 A 所列六檔（⛔ 非本檔自訂）
PROD_FILES = [
    "app.py",
    "verify/stepg_pipeline.py",
    "verify/selection_pipeline.py",
    "verify/run_verification.py",
    "verify/wd4_tier_list.py",
    "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
    "verify/wf_f3.py", "verify/wf_f4.py",
]

L = []
SKIPPED = []          # 🔒 略過須具名（節 119）
CALLGUARD = {"run_step_g": 0, "run_corner_pk": 0, "run_all_main": 0}


def say(s=""):
    print(s)
    L.append(s)


def hdr(s):
    say("")
    say("=" * WIDTH)
    say(s)
    say("=" * WIDTH)


def pop(n_total, n_printed, note=""):
    say("  POPULATION=%d PRINTED=%d SUPPRESSED=%d%s"
        % (n_total, n_printed, n_total - n_printed, ("  # " + note) if note else ""))


def sh(args):
    """跑 git 指令；回 (rc, stdout)。⛔ 不吞例外。"""
    p = subprocess.run(args, cwd=REPO, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode("utf-8", errors="replace")


def git1(args):
    rc, out = sh(["git", "-c", "core.quotePath=false"] + args)
    if rc != 0:
        raise RuntimeError("🔴 git 失敗 rc=%d：%s\n%s" % (rc, " ".join(args), out))
    return out.strip()


# ══════════════════════════════════════════════════════════════════════════════
#  §0　母體自證 ＋ 呼叫護欄
# ══════════════════════════════════════════════════════════════════════════════
def tracked_files():
    """母體 ＝ `git ls-files -z`（**遞迴**·⛔ 非 `ls`）。巢狀 worktree 不在索引內（已現查）。"""
    rc, out = sh(["git", "-c", "core.quotePath=false", "ls-files", "-z"])
    if rc != 0:
        raise RuntimeError("🔴 git ls-files 失敗：%s" % out)
    return [p for p in out.split("\0") if p]


TEXT = {}


def load_text(paths):
    """讀入文字檔（**位元組→utf-8**）。⛔ 不可解者一律**具名略過**、⛔ 不靜默丟。"""
    for rel in paths:
        if rel in TEXT:
            continue
        ap = os.path.join(REPO, rel)
        if not os.path.isfile(ap):
            SKIPPED.append((rel, "檔不存在於工作區"))
            continue
        with open(ap, "rb") as f:
            b = f.read()
        try:
            TEXT[rel] = b.decode("utf-8")
        except UnicodeDecodeError as e:                              # noqa: BLE001
            SKIPPED.append((rel, "非 utf-8（%s）" % type(e).__name__))


def count_hits(rel, needle):
    """**命中行數**（同 `grep -c`）。⛔ 不套任何後續過濾管線（節 44 戒 b）。"""
    t = TEXT.get(rel)
    if t is None:
        return None
    return sum(1 for ln in t.splitlines() if needle in ln)


def hit_lines(rel, needle):
    t = TEXT.get(rel)
    if t is None:
        return []
    return [(i + 1, ln) for i, ln in enumerate(t.splitlines()) if needle in ln]


def total_hits(rels, needle):
    n, files = 0, 0
    for rel in rels:
        c = count_hits(rel, needle)
        if c:
            n += c
            files += 1
    return n, files


_LAYER = {}


def layer_of(rel):
    """逐行分層（`碼`／`註解`／`字串`）——`.py` 以 `tokenize` 判，非 `.py` 一律 `文件`。

    🔒 定義（⛔ 不以「行首是不是 `#`」代替）：該行含**至少一個**非
    `COMMENT`／`STRING`／`NL`／`NEWLINE`／`INDENT`／`DEDENT`／`ENDMARKER` 之 token ⇒ `碼`；
    否則該行若被 `STRING` token 覆蓋 ⇒ `字串`（含 docstring）；若只有 `COMMENT` ⇒ `註解`。
    🩸 立本層之由：`寬深雙檢` 於生產路徑之 2 命中**皆在 docstring**（逐字為「已裁定、
    K-6-A2 尚未實作」）——不分層即把「文件說它沒實作」讀成「已實作」（本批自捕）。
    """
    if rel in _LAYER:
        return _LAYER[rel]
    t = TEXT.get(rel)
    if t is None:
        _LAYER[rel] = {}
        return {}
    n_lines = len(t.splitlines())
    if not rel.endswith(".py"):
        _LAYER[rel] = {i: "文件" for i in range(1, n_lines + 1)}
        return _LAYER[rel]
    import tokenize
    code, strs, cmts = set(), set(), set()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(t).readline):
            a, b = tok.start[0], tok.end[0]
            if tok.type == tokenize.COMMENT:
                cmts.update(range(a, b + 1))
            elif tok.type == tokenize.STRING:
                strs.update(range(a, b + 1))
            elif tok.type in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT,
                              tokenize.DEDENT, tokenize.ENDMARKER):
                continue
            else:
                code.update(range(a, b + 1))
    except (tokenize.TokenError, IndentationError, SyntaxError) as e:  # noqa: BLE001
        SKIPPED.append((rel, "tokenize 失敗（%s）⇒ 該檔之分層未成立" % type(e).__name__))
        _LAYER[rel] = {}
        return {}
    m = {}
    for i in range(1, n_lines + 1):
        m[i] = "碼" if i in code else ("字串" if i in strs else
                                       ("註解" if i in cmts else "空"))
    _LAYER[rel] = m
    return m


def layered_hits(rels, needle):
    """回 `{'碼':n, '註解':n, '字串':n, '文件':n, '空':n, '檔':k}`（⛔ 不合併層）。"""
    out = {"碼": 0, "註解": 0, "字串": 0, "文件": 0, "空": 0, "檔": 0}
    for rel in rels:
        hs = hit_lines(rel, needle)
        if not hs:
            continue
        out["檔"] += 1
        lay = layer_of(rel)
        for ln, _txt in hs:
            out[lay.get(ln, "文件")] = out.get(lay.get(ln, "文件"), 0) + 1
    return out


def _forbidden(name):
    def _f(*a, **kw):
        CALLGUARD[name] += 1
        raise RuntimeError(
            "🔴 施工單 §零 F：本批⛔ 不得呼叫 `%s`（run_all／run_step_g 類）——"
            "若某量非跑管線不可得，出艙【須執行該碼·本批不跑】" % name)
    return _f


# ══════════════════════════════════════════════════════════════════════════════
def main():                                                          # noqa: C901
    head = git1(["rev-parse", "HEAD"])
    head_s = git1(["rev-parse", "--short", "HEAD"])
    app_blob = git1(["rev-parse", "HEAD:app.py"])
    origin = git1(["rev-parse", "origin/wip/s1-endpart"])

    log_path = os.path.join(OUTDIR, "probe_WG996_yi_invariants_%s.log" % head_s)

    files = tracked_files()
    load_text([p for p in files
               if p.endswith((".py", ".md", ".log", ".csv", ".txt", ".json"))])

    hdr("【W-G.9-96】乙落地驗收靶（三不變式）——現況量測 ＋ 落地後閘之預寫")
    say("  產生於 commit：%s（%s）" % (head_s, head))
    say("  `app.py` blob：%s" % app_blob)
    say("  母體（`git ls-files -z`·遞迴）＝ **%d** 檔；本檔載入為文字者 ＝ **%d** 檔"
        % (len(files), len(TEXT)))
    say("  🔒 SELF（母體自證·節 72）＝ %s" % SELF)
    say("  🔒 巢狀 worktree 於索引內之命中 ＝ **%d**（⇒ 母體無巢狀污染）"
        % sum(1 for p in files if ".claude/worktrees" in p))
    import shapely                                                   # noqa: E402
    import numpy                                                     # noqa: E402
    say("  環境：shapely %s | GEOS %s | numpy %s"
        % (shapely.__version__, shapely.geos_version, numpy.__version__))

    # ── §0-3　呼叫護欄（機械證明「未跑管線」）────────────────────────────────
    import stepg_pipeline as _sg
    import selection_pipeline as _sp
    import run_verification as rv
    _sg.run_step_g = _forbidden("run_step_g")
    _sp.run_corner_pk = _forbidden("run_corner_pk")
    rv.main = _forbidden("run_all_main")
    say("  🛑 **呼叫護欄已裝**：`stepg_pipeline.run_step_g`／`selection_pipeline.run_corner_pk`／"
        "`run_verification.main` 皆已覆蓋為 **raise 版**")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§A】開工閘（`A0-1`〜`A0-8`）——⛔ 其後受詞在此之前一律未開辦")
    ok_a = True

    def gate(gid, expect, got, cmd):
        nonlocal ok_a
        good = (str(expect) == str(got))
        ok_a = ok_a and good
        say("  %-6s %s  期望＝%s  現查＝%s" % (gid, "✅" if good else "🔴", expect, got))
        say("         產生指令：%s" % cmd)
        return good

    gate("A0-1", "ba0af85fc8e727fd67d3822e2e62712b1904d1b6", head, "git rev-parse HEAD")
    gate("A0-2", "ba0af85fc8e727fd67d3822e2e62712b1904d1b6", origin,
         "git rev-parse origin/wip/s1-endpart")
    gate("A0-3", "a9e5671d64d254907a0396f898f046d9d85e8283", app_blob,
         "git rev-parse HEAD:app.py")
    gate("A0-4", app_blob, git1(["hash-object", "app.py"]), "git hash-object app.py")

    _porc = [ln for ln in git1(["status", "--porcelain"]).splitlines() if ln.strip()]
    _porc_out = [ln for ln in _porc
                 if not any(s in ln for s in SELF) and "verify/out/" not in ln]
    say("  A0-5   %s  受詞檔外之 porcelain 列 ＝ %d（本批授權檔與未追蹤 verify/out 已扣）"
        % ("✅" if not _porc_out else "🔴", len(_porc_out)))
    for ln in _porc_out[:10]:
        say("         %s" % ln)
    ok_a = ok_a and not _porc_out

    sk_rel = ".claude/skills/failure-archaeology/SKILL.md"
    zw_rel = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
    sk_lines = TEXT[sk_rel].splitlines()
    zw_lines = TEXT[zw_rel].splitlines()
    sk_h = [(i + 1, ln) for i, ln in enumerate(sk_lines) if re.match(r"^## (\d+)\. ", ln)]
    zw_h = [(i + 1, ln) for i, ln in enumerate(zw_lines) if ln.startswith("## 自誤")]
    gate("A0-6a", 4715, len(sk_lines), "SKILL.md splitlines()")
    gate("A0-6b", 121, int(re.match(r"^## (\d+)\. ", sk_h[-1][1]).group(1)),
         "窄樣式 `^## (\\d+)\\. ` 之最大節號")
    gate("A0-7a", 2657, len(zw_lines), "自誤登記表 splitlines()")
    gate("A0-7b", 100,
         int(re.match(r"^## 自誤\s*(\d+)", zw_h[-1][1]).group(1)),
         "窄樣式 `^## 自誤(\\d+)` 之最大序號")
    _1633 = zw_lines[1632]
    _needle_1633 = "**（清 claude.ai）｜"
    gate("A0-8", True, _needle_1633 in _1633, "登記表 :1633 逐字含「（清 claude.ai）｜」")
    say("         :1633 原樣 ＝ %r" % _1633[:40])
    say("")
    say("  ⇒ 開工閘：%s" % ("✅ **全綠**" if ok_a else "🔴 **有紅** ⇒ 🛑 停機①"))
    if not ok_a:
        raise RuntimeError("🔴 §A 開工閘紅 ⇒ 停機①（⛔ 不開受詞）")

    # ── 編號現查（§零 M）────────────────────────────────────────────────────
    _num_hits = []
    for rel in TEXT:
        if rel in SELF:
            continue
        c = count_hits(rel, "W-G.9-96")
        if c:
            _num_hits.append((rel, c))
    _ctrl_hits = sum(1 for rel in TEXT if count_hits(rel, "W-G.9-95Z"))
    say("  編號現查：`W-G.9-96` 於母體（扣 SELF）之命中檔數 ＝ **%d**" % len(_num_hits))
    say("            非 0 對照（同法·已知存在字樣 `W-G.9-95Z`）＝ **%d 檔** ⇒ 搜法有判別力"
        % _ctrl_hits)
    for rel, c in _num_hits:
        say("            🔴 %s ×%d" % (rel, c))

    # ══════════════════════════════════════════════════════════════════════
    #  §B　不變式 II（遞補下一位 ＝ `_projection_order` 之次一元素）
    # ══════════════════════════════════════════════════════════════════════
    hdr("【§B】不變式 II：遞補之「下一位」＝ 生產函式 `_projection_order` 之次一元素")

    # ── B-1　符號定位（AST ＋ 裸 grep·停機⑧）──────────────────────────────
    app_src = TEXT["app.py"]
    n_def = sum(1 for ln in app_src.splitlines() if ln.startswith("def _projection_order("))
    tree = ast.parse(app_src)
    fdefs = [nd for nd in ast.walk(tree)
             if isinstance(nd, ast.FunctionDef) and nd.name == "_projection_order"]
    say("  **B-1 符號定位**")
    say("    裸 grep `^def _projection_order(` 於 `app.py` 之命中 ＝ **%d**（停機⑧ 之受詞：須 ＝ 1）"
        % n_def)
    say("    AST `FunctionDef(_projection_order)` ＝ **%d** 個；lineno ＝ **%s**"
        % (len(fdefs), [f.lineno for f in fdefs]))
    if n_def != 1 or len(fdefs) != 1:
        raise RuntimeError("🔴 `_projection_order` 定義命中 ≠ 1 ⇒ 🛑 停機⑧")
    po_lineno = fdefs[0].lineno

    # 🔒 `ast.col_offset` ＝ **utf-8 位元組**偏移（節 114）——CJK 樣本**先驗**
    _cjk = [nd for nd in ast.walk(tree)
            if isinstance(nd, ast.FunctionDef)
            and any(ord(c) > 127 for c in (ast.get_docstring(nd) or ""))]
    _probe_ln = app_src.splitlines()[po_lineno + 1] if len(app_src.splitlines()) > po_lineno else ""
    _bytes_line = _probe_ln.encode("utf-8")
    say("    🔒 `col_offset` 口徑先驗（節 114）：定義次二行之 `len(str)`＝%d、`len(utf-8 bytes)`＝%d"
        % (len(_probe_ln), len(_bytes_line)))
    say("       ⇒ 二者%s ⇒ 本檔**⛔ 不以 `col_offset` 切字元**（只用 `lineno`）"
        % ("**相異**（該行含 CJK）" if len(_probe_ln) != len(_bytes_line) else "相同（該行純 ASCII）"))
    say("    含 CJK docstring 之 FunctionDef ＝ %d 個（⇒ CJK 樣本非空·節 67）" % len(_cjk))

    # ── B-2　取生產函式（⛔ 不手寫 sort）────────────────────────────────────
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        from app_harvest import harvest
        from selection_pipeline import build_build_parcels
        ns, fake_st = harvest()
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
        rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp_p, build_p, _sw = build_build_parcels(
            ns, fake_st, v6, list(cb_by.values()), snap)
    PO = ns["_projection_order"]
    say("")
    say("  **B-2 生產函式同一性**（⛔ 不自行重建排序）")
    say("    `PO is ns['_projection_order']` ＝ %s；`__name__` ＝ `%s`"
        % (PO is ns["_projection_order"], PO.__name__))
    say("    `PO.__code__.co_firstlineno` ＝ **%d**；AST 定義行 ＝ **%d** ⇒ %s"
        % (PO.__code__.co_firstlineno, po_lineno,
           "✅ 同一物" if PO.__code__.co_firstlineno == po_lineno else "🔴 不同"))
    if PO.__code__.co_firstlineno != po_lineno:
        raise RuntimeError("🔴 取到之 `_projection_order` 非 `app.py:%d` 之定義" % po_lineno)

    # ── B-3　判別力（對調兩宗 ⇒ successor 必變·常設 8）──────────────────────
    def mk(name, x):
        return {"暫編地號": name,
                "polygon_coords": [(x, 0.0), (x + 1.0, 0.0), (x + 1.0, 1.0), (x, 1.0)]}

    KEY = "暫編地號"
    caseA = [mk("A", 0.0), mk("B", 10.0), mk("C", 20.0)]
    caseB = [mk("A", 0.0), mk("B", 20.0), mk("C", 10.0)]
    oA = [t[KEY] for t in PO(caseA, (0.0, 0.0), (100.0, 0.0))]
    oB = [t[KEY] for t in PO(caseB, (0.0, 0.0), (100.0, 0.0))]
    sA, sB = oA[oA.index("A") + 1], oB[oB.index("A") + 1]
    say("")
    say("  **B-3 判別力**（人造 3 宗·只把 `B`／`C` 之幾何對調·⛔ 不動輸入順序）")
    say("    序 ①＝%s ⇒ `A` 之 successor ＝ **%s**" % (oA, sA))
    say("    序 ②＝%s ⇒ `A` 之 successor ＝ **%s**" % (oB, sB))
    say("    ⇒ successor %s ⇒ %s"
        % ("**變**" if sA != sB else "**未變**",
           "✅ 探針確實接到該函式（節 78）" if sA != sB else "🔴 探針未接到函式"))
    if sA == sB:
        raise RuntimeError("🔴 B-3 判別力為零 ⇒ 探針未接到 `_projection_order`（節 78）")

    # ── B-4　現況（生產輸入·pipeline-free）──────────────────────────────────
    ss = fake_st.session_state
    FL_prod = ss.get("f3_cad_front_lines") or {}
    FL_cad = cad.get("front_lines") or {}
    same_fl = all(FL_prod.get(k) == FL_cad.get(k) for k in set(FL_prod) | set(FL_cad))
    say("")
    say("  **B-4 現況**（**生產輸入**·⛔ 未跑管線）")
    say("    FRONT_LINE 來源＝`ss['f3_cad_front_lines']`（生產存取式·`stepg_pipeline.py:427`）；"
        "與 `cad['front_lines']` 逐鍵相同 ＝ %s" % same_fl)
    say("    母體＝`build_parcels` 扣 `_is_ghost_sliver`（`stepg_pipeline.py:315-319` 逐字）"
        "再扣 `'配地階段' in tp`（`:416-417`）")

    by_blk = {}
    n_ghost = 0
    for tp in build_p:
        if tp.get("_is_ghost_sliver", False):
            n_ghost += 1
            continue
        by_blk.setdefault(tp.get("所屬街廓"), []).append(tp)
    say("    `build_parcels` ＝ **%d** 宗；`_is_ghost_sliver` 扣除 ＝ **%d** 宗 ⇒ 餘 **%d** 宗"
        % (len(build_p), n_ghost, len(build_p) - n_ghost))

    RB = ["R1", "R2", "R3", "R4", "R5", "R6"]
    RANK = {}
    say("")
    say("    街廓  n   投影序號 → 暫編地號（1-based·＝ `pre_position`）")
    for lbl in RB:
        fl = FL_prod.get(lbl) or {}
        st1 = [tp for tp in by_blk.get(lbl, []) if "配地階段" not in tp]
        if not st1:
            raise RuntimeError("🔴 街廓 %s 之階段1宗母體為空（⛔ 不得以空母體充作通過）" % lbl)
        if not (fl.get("p1") and fl.get("p2")):
            raise RuntimeError("🔴 街廓 %s 缺 FRONT_LINE ⇒ 投影序不可定義（禁兜底）" % lbl)
        order = PO(st1, fl["p1"], fl["p2"])
        RANK[lbl] = [t[KEY] for t in order]
        say("    %-4s %2d  %s" % (lbl, len(order),
                                  "  ".join("%d:%s" % (i + 1, t[KEY])
                                            for i, t in enumerate(order))))
    pop(len(RB), len(RB), "B-4 逐街廓投影序（全列）")

    # 違反宗（其**暫編地號**取自入倉 log·見 §C-1）
    VIOL = {"R2": "628-42(1)", "R5": "628-53(2)"}
    say("")
    say("    ── 兩違反宗之 successor（受詞 ＝ **投影序號中下一位**·`K-6:2344` 逐字）──")
    say("    街廓  違反宗              投影序號   下一位（投影序號＋1）      該宗身分")
    ZERO0 = {"R2": "628-41(1)", "R5": "628-18(2)"}   # 🔒 `宗0`：轉引 `-77`（見 §C-5）
    succ_rows = []
    for lbl, nm in sorted(VIOL.items()):
        seq = RANK[lbl]
        if nm not in seq:
            raise RuntimeError("🔴 違反宗 %s 不在 %s 之投影序母體內" % (nm, lbl))
        i = seq.index(nm)
        if i + 1 >= len(seq):
            raise RuntimeError("🔴 %s 之違反宗為末項 ⇒ 無次一元素（⛔ 不 wrap）" % lbl)
        succ = seq[i + 1]
        role = ("🔴 **＝ 該側 `宗0`（街角 PK winner）**"
                if succ == ZERO0.get(lbl) else "非 `宗0`")
        succ_rows.append((lbl, nm, i + 1, succ, i + 2, role))
        say("    %-4s %-18s %4d      %-18s(%d)   %s" % (lbl, nm, i + 1, succ, i + 2, role))
    pop(len(VIOL), len(succ_rows), "B-4 違反宗 successor（全列）")

    # ── B-5　轉引之重讀（自**入倉 log**·⛔ 不抄報告小數）────────────────────
    LOG92 = "verify/out/probe_WG992_blue_451f0f8.log"
    LOG91 = "verify/out/probe_WG991_yishim_2cb0fe9.log"
    for rel in (LOG92, LOG91):
        if rel not in TEXT:
            raise RuntimeError("🔴 入倉 log 缺件：%s" % rel)
    l92 = TEXT[LOG92].splitlines()
    blob_451 = git1(["rev-parse", "451f0f8:app.py"])
    say("")
    say("  **B-5 轉引之重讀**（源 ＝ **入倉 log**·⛔ 非報告內文）")
    say("    `451f0f8:app.py` ＝ %s" % blob_451)
    say("    `ba0af85:app.py` ＝ %s ⇒ %s"
        % (app_blob, "✅ **逐位相同** ⇒ 該批量測於本基座仍有效"
           if blob_451 == app_blob else "🔴 相異 ⇒ 轉引失錨"))
    if blob_451 != app_blob:
        raise RuntimeError("🔴 451f0f8 與 ba0af85 之 app.py 不同 blob ⇒ 轉引失錨")

    grp = [ln for ln in TEXT[LOG92].splitlines()
           if re.match(r"^\s+R\d\s+[左右]\s+\[", ln)]
    say("")
    say("    `-92` 不變式 ③ 之十組表（**原樣重讀**·⛔ 未重跑）：")
    for ln in grp:
        say("      %s" % ln.rstrip())
    pop(10, len(grp), "B-5 十組表（`-92` log 原樣）")
    if len(grp) != 10:
        raise RuntimeError("🔴 `-92` log 之十組表重讀得 %d 列（≠10）⇒ 解析器壞" % len(grp))

    def _first_seq(ln):
        m = re.search(r"\[([0-9,\s]+)", ln)
        return [int(x) for x in m.group(1).replace(" ", "").strip(",").split(",")] if m else []

    # ── B-5b　`biz` 索引 ↔ 投影序號之對應（**可證偽之重建**·⛔ 未跑管線）────────
    say("")
    say("  **B-5b `biz` 索引 ↔ 投影序號之對應**（以生產碼逐字重建·⛔ 未跑管線）")
    say("    重建式（`app.py:7614-7700` 之 `_spatial_order_parcels_v2` 逐字）：")
    say("      `ordered_v2` ＝ 投影序列，其中 `p1_end` winner **移至 index 0**、"
        "`p2_end` winner **移至末位**；")
    say("      `left_group = ordered_v2[:k]`／`right_group = reversed(ordered_v2[k:])`"
        "（`stepg_pipeline.py:594-595` 逐字）；`biz = left_group + right_group`"
        "（`:924` 之 `left_results + right_results`）。")
    csv_rel = "verify/baselines/第 1 宗街角地指配結果_退縮0m.csv"
    if csv_rel not in TEXT:
        raise RuntimeError("🔴 缺件：%s" % csv_rel)
    WIN = {}
    for row in TEXT[csv_rel].splitlines()[1:]:
        c = row.split(",")
        if len(c) < 12 or not c[0].strip():
            continue
        def _tmp(x):
            m = re.search(r"\[([^\]]+)\]", x)
            return m.group(1) if m else None
        WIN[c[0].strip().lstrip("﻿")] = (_tmp(c[7]), _tmp(c[10]))
    say("    winner 之源 ＝ `%s`（🔴 **凍結期 baseline**·其自身之時效見 §C-5）" % csv_rel)
    # -92 log：每組之索引序（第一欄 list）→ k；A-1 表 → 第0宗／第1宗／第1宗地號
    KSPLIT, A1 = {}, {}
    for ln in grp:
        w = ln.split()
        seq = _first_seq(ln)
        if w[1] == "左":
            KSPLIT[w[0]] = len(seq)
    for ln in l92:
        if "[" in ln:
            continue
        m = re.match(r"^\s+(R\d)\s+([左右])\s+([—\d]+)\s+([—\d]+)\s+(\S+)\s+", ln)
        if m and ("是" in ln or "否" in ln):
            A1[(m.group(1), m.group(2))] = (m.group(3), m.group(4), m.group(5))
    say("")
    say("    街廓 側  k  重建 biz[第0宗]      log 第0宗身分        重建 biz[第1宗]      log 第1宗地號        判")
    ok_rec, n_rec = 0, 0
    BIZ = {}
    for lbl in RB:
        P = list(RANK[lbl])
        wl, wr = WIN.get(lbl, (None, None))
        ov = [x for x in P if x not in (wl, wr)]
        if wl in P:
            ov = [wl] + ov
        if wr in P:
            ov = ov + [wr]
        k = KSPLIT.get(lbl, len(ov))
        biz = ov[:k] + list(reversed(ov[k:]))
        BIZ[lbl] = biz
        for side in ("左", "右"):
            row = A1.get((lbl, side))
            if not row or row[0] == "—":
                continue
            if row[1] == "—":
                say("    %-3s %-2s  —  有街角但**無次一宗** ⇒ 具名略過（同 `-92` A-1 母體之 6 格）"
                    % (lbl, side))
                continue
            i0, i1, nm1 = int(row[0]), int(row[1]), row[2]
            got1 = biz[i1] if i1 < len(biz) else "?"
            good = (got1 == nm1)
            ok_rec += 1 if good else 0
            n_rec += 1
            say("    %-3s %-2s %2d  %-18s %-20s %-18s %-18s %s"
                % (lbl, side, k, biz[i0] if i0 < len(biz) else "?",
                   "biz[%d]" % i0, got1, nm1, "✅" if good else "🔴"))
    pop(n_rec, n_rec, "B-5b 重建對拍（有街角之格·全列）")
    say("    ⇒ 重建之 `biz[第1宗]` 與 `-92` log 之「第1宗地號」逐格相同 ＝ **%d／%d**"
        % (ok_rec, n_rec))
    if ok_rec != n_rec or n_rec == 0:
        raise RuntimeError("🔴 B-5b 重建對拍 %d/%d ⇒ 重建式或 winner 源已失效（⛔ 不得續用）"
                           % (ok_rec, n_rec))
    # 判別力（常設 8）：擾動 winner ⇒ 對拍必翻
    _lbl = "R2"
    _P = list(RANK[_lbl])
    _wl_bad = next(x for x in _P if x not in WIN.get(_lbl, (None, None)))
    _ov = [_wl_bad] + [x for x in _P if x != _wl_bad]
    _k = KSPLIT[_lbl]
    _biz_bad = _ov[:_k] + list(reversed(_ov[_k:]))
    _i1 = int(A1[(_lbl, "左")][1])
    say("    🔒 判別力（常設 8）：把 `%s` 之 `p1_end` winner 換成 `%s` ⇒ 重建 `biz[%d]` ＝ `%s`"
        % (_lbl, _wl_bad, _i1, _biz_bad[_i1]))
    say("       ⇒ 與 log 之 `%s` %s ⇒ %s"
        % (A1[(_lbl, "左")][2],
           "相同" if _biz_bad[_i1] == A1[(_lbl, "左")][2] else "**不同**",
           "🔴 對拍無判別力" if _biz_bad[_i1] == A1[(_lbl, "左")][2] else "✅ 對拍有判別力"))
    if _biz_bad[_i1] == A1[(_lbl, "左")][2]:
        raise RuntimeError("🔴 B-5b 對拍無判別力（擾動 winner 而結果不變）")

    say("")
    say("    ── 三候選定序於 `R2左`／`R5左` 之「下一位」（`biz` 陣列索引空間）──")
    say("    組     ① 組內索引序        ② s 中點序（log 截斷·僅取可見前綴）   ①之下一位  ②之下一位")
    idx_rows = 0
    for ln in grp:
        if not re.match(r"^\s+R[25]\s+左", ln):
            continue
        parts = re.findall(r"\[([0-9,\s]+)\]?", ln)
        a = [int(x) for x in parts[0].replace(" ", "").strip(",").split(",")]
        b = [int(x) for x in parts[1].replace(" ", "").strip(",").split(",")]
        na = a[a.index(1) + 1] if 1 in a and a.index(1) + 1 < len(a) else None
        nb = b[b.index(1) + 1] if 1 in b and b.index(1) + 1 < len(b) else None
        say("    %-6s %-18s %-36s %-10s %s"
            % (ln.split()[0] + "左", a, b, na, nb))
        idx_rows += 1
    pop(2, idx_rows, "B-5 二格之①②下一位（自 log 重讀）")
    say("    🔒 ③ `_projection_order`（`-93` §C-3 稱 ＝ ② 逐格相同·10/10）＝ "
        "**【轉引 `-93` §C-3·⛔ 本批未重跑】**")
    say("       理由：`-93` **未入倉任何探針／log**（`git show --name-only f6169a7` ＝ 報告 1 檔）"
        "⇒ 其 ③ 之**輸入無從現查**；重跑其 `biz` 空間須 `run_step_g` ⇒ **【須執行該碼·本批不跑】**")

    # ── B-5c　🛑 決定性表：三候選之「下一位」換算至**投影序號**空間 ────────────
    say("")
    say("  **B-5c 🛑 三候選之「下一位」換算至<u>投影序號</u>空間**"
        "（用 `B-5b` 之對應·6／6 已對拍）")
    say("    🔒 `-93` §C-3 之 `2`／`3` 係 **`biz` 陣列索引**"
        "（其 ① 欄逐字為「`rec[\"biz\"]` 之**陣列索引**」）——⛔ **非**投影序號。")
    say("")
    say("    候選（下一位之定序）                       R2左：biz→暫編地號(投影序號)     R5左：biz→暫編地號(投影序號)")
    CAND = [("① 組內索引序（＝`ordered_v2` 序）", 2),
            ("②／③ `-93` 所載（s 中點序）", 3)]
    cand_rows = 0
    for cname, bidx in CAND:
        cells = []
        for lbl in ("R2", "R5"):
            nm = BIZ[lbl][bidx]
            cells.append("biz%d → %s (%d)" % (bidx, nm, RANK[lbl].index(nm) + 1))
        say("    %-38s %-32s %s" % (cname, cells[0], cells[1]))
        cand_rows += 1
    cells = []
    for lbl, _nm, _r0, succ, r1, _role in succ_rows:
        cells.append("biz%d → %s (%d)" % (BIZ[lbl].index(succ), succ, r1))
    say("    %-38s %-32s %s"
        % ("③′ **生產式**：投影序號 ＋1（本批現算）", cells[0], cells[1]))
    cand_rows += 1
    pop(3, cand_rows, "B-5c 三候選（全列）")
    say("")
    say("    🛑 **停機② 之代回**（施工單 §五 ②：「重跑後 `R2左` 或 `R5左` 之 "
        "`_projection_order` successor ≠ 3 ⇒ 停」）")
    say("       · 受詞若為 **`biz` 陣列索引**：本批**⛔ 無法重跑**（須 `run_step_g`）"
        "⇒ 該受詞**未開辦**；⛔ 不以 `-93` 之值充作重跑。")
    say("       · 受詞若為 **生產函式對生產輸入之回傳序列**（＝施工單 §三 II 之定義逐字）：")
    say("         successor ＝ **投影序號 2**，其 `biz` 索引 ＝ **%d**（R2）／**%d**（R5）"
        % (BIZ["R2"].index(succ_rows[0][3]), BIZ["R5"].index(succ_rows[1][3])))
    say("         ⇒ **≠ 3** ⇒ 🛑 **停機② 字面觸發·上呈**。")
    say("       · 🔴 **併出艙之現查事實**（⛔ 非主張、⛔ 非提名、⛔ 不改不變式去湊）：")
    say("         該 successor 於**二格皆 ＝ 該側 `宗0`（街角 PK winner）**，"
        "而 `宗0` 依 `_spatial_order_parcels_v2` 已被移至 `ordered_v2[0]`（＝街角）")
    say("         ⇒ 「遞補該位次」之受詞於此二格**退化**（下一位者已在該位）。")
    say("       · ⛔ 本批**不判**何者為正——`K-9-11 三` 明訂遞補機制⛔ 不另訂，"
        "且 `-93` `B-3` 明禁提名。")

    # ── B-5d　十組之 order 指紋（暫編地號序列·⛔ 非 hash）───────────────────
    say("")
    say("  **B-5d 十組之 `order` 指紋**（`biz` 序之**暫編地號序列**·⛔ 不以 hash 代替）")
    say("    🔒 母體 ＝ `-92` log 之十組（`R4` 之二格**無組列** ⇒ 具名不在母體）")
    fp_rows = 0
    for lbl in RB:
        if lbl not in KSPLIT:
            say("    %-3s ── `-92` log 無組列 ⇒ **具名略過**（非母體）" % lbl)
            continue
        k, biz = KSPLIT[lbl], BIZ[lbl]
        for side, seq in (("左", biz[:k]), ("右", biz[k:])):
            say("    %-3s %-2s n=%-2d  %s"
                % (lbl, side, len(seq),
                   " → ".join("%s(%d)" % (x, RANK[lbl].index(x) + 1) for x in seq)))
            fp_rows += 1
    pop(10, fp_rows, "B-5d 十組 order 指紋（全列·括號內 ＝ 投影序號）")
    if fp_rows != 10:
        raise RuntimeError("🔴 B-5d 得 %d 組（≠10）⇒ 母體與 `-92` 不符" % fp_rows)

    # ── B-6　負向（W-D.4 碎片遞補 ≠ 乙遞補）────────────────────────────────
    wd4 = "verify/wd4_tier_list.py"
    nd_frag = hit_lines(wd4, "自碎片端往內走第一筆有效")
    nd_s = total_hits([wd4], "累積S")
    say("")
    say("  **B-6 負向**（`W-D.4` 碎片遞補 ⛔ 非乙介面·節 116／`-95` A-2）")
    for ln, txt in nd_frag:
        say("    %s:%d  %s" % (wd4, ln, txt.strip()))
    say("    `累積S` 於 `%s` 之命中 ＝ **%d**（＝ 其定序受詞）" % (wd4, nd_s[0]))
    say("    ⇒ 定序受詞 ＝ `累積S(m)`／走向 ＝ 自碎片端往內／產物 ＝ CSV 欄 "
        "⇒ 與 II 之 `_projection_order` **受詞不同** ⇒ ⛔ 不得互代")

    # ══════════════════════════════════════════════════════════════════════
    #  §C　不變式 I-A（地界線交叉 ⇒ 不配地）
    # ══════════════════════════════════════════════════════════════════════
    hdr("【§C】不變式 I-A：地界線交叉 ⇒ 不配地（`K-9-15`／`K-9-16` 條件 2）")

    l92 = TEXT[LOG92].splitlines()
    ln_pop = [ln for ln in l92 if "不交叉判準" in ln and "母體" in ln]
    say("  **C-1 違反名單**（原樣重讀·源 `%s`）" % LOG92)
    for ln in ln_pop:
        say("    %s" % ln.strip())
    if not ln_pop:
        raise RuntimeError("🔴 `-92` log 內找不到違反名單列 ⇒ 解析器壞（⛔ 不以 0 充作結論）")
    say("    ⇒ 本批解出之違反宗地號 ＝ %s（其地號取自 `-92` log 之「第1宗地號」欄·見下）"
        % sorted(VIOL.values()))

    say("")
    say("  **C-2 藍影 vs `G₁`（界 ＝ `B1`·`K-9-16` 一）**（原樣重讀·⛔ 不手抄小數）")
    for ln in l92:
        if re.match(r"^\s+R\d\|", ln) and "e+" in ln and "是" in ln:
            say("    %s" % ln.rstrip())
    say("")
    say("  **C-3 第0宗／第1宗地號表**（原樣重讀）")
    z_rows = 0
    for ln in l92:
        if re.match(r"^\s+R\d\s+[左右]\s+[—\d]", ln):
            say("    %s" % ln.rstrip())
            z_rows += 1
    pop(12, z_rows, "C-3 逐格（`-92` log 原樣）")

    say("")
    say("  **C-4 面積**（源 `%s`）" % LOG91)
    for ln in TEXT[LOG91].splitlines():
        if "4.7950" in ln or ("違反" in ln and "47" in ln):
            say("    %s" % ln.strip())

    say("")
    say("  **C-5 合成翻面（`G₁ := 藍影 + ε`）**")
    say("    🛑 **【須執行該碼·本批⛔ 不跑】**——其載體幾何（`rec['biz']`／`w88.s_star_of` 之解算面）"
        "須 `run_step_g` 方得，而施工單 §零 F ⛔ 之。轉引 `-93` §B-3：`A-3` 之 1／2／3／4 於載體 2 宗全部成立。")
    say("    ⚠️ `-93` 已具名：此合成**未補**「未違反者」之陽性對照缺口；本批**同樣⛔ 不宣稱**"
        "「已證 `G₁ ≥ 藍影` 於未違反者成立」（自然母體無「藍影>EPS 且未違反」之格·`-92`）。")
    say("    🔒 `宗0` 之身分（`R2`＝`%s`／`R5`＝`%s`）＝ **【轉引 `-77` §C 表·⛔ 本批未重跑】**"
        % (ZERO0["R2"], ZERO0["R5"]))
    say("       （交叉驗證：二者於 §B-4 之投影序號皆 ＝ **2**，且 `-92` log 之「第1宗地號」"
        "＝ 投影序號 **1** 之宗 ⇒ `ordered_v2 = [宗0, 投影序1, 投影序3, …]` 自洽）")
    _stale = "verify/baselines/第 1 宗街角地指配結果_退縮0m.csv"
    _stale_commit = git1(["log", "-1", "--format=%h %ad", "--date=short", "--", _stale])
    say("    🔴 **⛔ 不可用之錨**：`%s` 之最後異動 ＝ `%s`（初始遷移）"
        % (_stale, _stale_commit))
    say("       ——其 `R2【左】第1宗指配` 欄載 `628-41(1)`，與 `-77` 相同；惟該 CSV 早於"
        "本波全部幾何變更 ⇒ 本批**⛔ 不以之為 winner 之權威錨**，只作為與 `-77` 一致之旁證。")

    # ══════════════════════════════════════════════════════════════════════
    #  §D　不變式 I-B（零合格垂線 ⇒ 不配地）
    # ══════════════════════════════════════════════════════════════════════
    hdr("【§D】不變式 I-B：零合格垂線 ⇒ 不配地（`K-9-11 二`）——現況 ＝ **【閘不存在】**")

    ZERO_PATS = ["合格垂線", "整條落在",
                 "垂線", "perp_ok", "valid_perp", "perpendicular"]
    CTRL_PATS = ["def parcel_min_width_n14", "def _n14_band_hi",
                 "def _n14_band_geom", "min_depth"]
    say("  🔒 **射程**：目錄 ＝ 生產路徑 %d 檔（施工單 §零 A 之清單）；字樣 ＝ 下表（含 ASCII 大小寫變體）"
        % len(PROD_FILES))
    say("  🔒 **分層**：`碼`／`註解`／`字串`（`tokenize` 判·⛔ 不以行首 `#` 代替）——"
        "判準取 **`碼`** 層（＝可執行消費）")
    say("")
    say("    字樣                     app.py全   生產路徑:碼  註解  字串   全母體合計(檔數)")
    n_zero = 0
    for p in ZERO_PATS:
        a = count_hits("app.py", p)
        s = layered_hits(PROD_FILES, p)
        g = total_hits(list(TEXT), p)
        n_zero += (1 if s["碼"] == 0 else 0)
        say("    %-24s %8s   %10d  %4d  %4d   %d(%d)"
            % ("`" + p + "`", a, s["碼"], s["註解"], s["字串"], g[0], g[1]))
    pop(len(ZERO_PATS), len(ZERO_PATS), "D-1 應為 0 之字樣（全列）")
    say("")
    say("    ── 非 0 對照（同法·同母體·節 92）──")
    for p in CTRL_PATS:
        a = count_hits("app.py", p)
        s = layered_hits(PROD_FILES, p)
        say("    %-24s %8s   %10d  %4d  %4d"
            % ("`" + p + "`", a, s["碼"], s["註解"], s["字串"]))
    pop(len(CTRL_PATS), len(CTRL_PATS), "D-1 非 0 對照（全列）")
    # 🔒 陰性對照字樣：**執行期組出**（節 111·⛔ 不寫死）
    _neg = "".join(["ZZ", "QQ", "_", "%d" % (7 * 60611), "_", "NOPE"])
    _neg_hits = total_hits(list(TEXT), _neg)
    say("    陰性對照（執行期組出之角色字樣·⛔ 不出艙其字面）＝ **%d** 命中（須 0）" % _neg_hits[0])

    # ── D-1b　非 0 之**逐筆裁斷**（⛔ 不以「命中即存在」結案）────────────────
    say("")
    say("    ── 非 0 命中之**逐筆裁斷**（⛔ 命中 ≠ 該閘存在·須逐筆看受詞）──")
    adj_rows, adj_ib = 0, 0
    for p in ZERO_PATS:
        s = layered_hits(PROD_FILES, p)
        if s["碼"] == 0:
            continue
        for rel in PROD_FILES:
            for ln, txt in hit_lines(rel, p):
                if layer_of(rel).get(ln) != "碼":
                    continue
                adj_rows += 1
                say("    %s:%d  %s" % (rel, ln, txt.strip()[:96]))
    say("    🔒 裁斷：上列 **%d** 筆之受詞皆為 **`ALLOC_LINE ⊥ FRONT_LINE` 之軸向診斷**"
        "（`_perp_deg`／`ALLOC⊥FRONT_ok`·`app.py:19502-19526`）" % adj_rows)
    say("       ⇒ 與 `K-9-11 二` 之「**合格垂線**（整條落在該宗地內、且與後側境界線實體線段相交）」"
        "**受詞不同** ⇒ **⛔ 不是** I-B 之閘 ⇒ 計入 I-B 者 ＝ **%d**" % adj_ib)
    pop(adj_rows, adj_rows, "D-1b 非 0 命中逐筆（全列）")

    say("")
    say("  **D-2 出艙碼（鎖定）**：I-B 之現況 ＝ **【閘不存在】**")
    say("    ⇒ 語意直指 I-B 之字樣（`合格垂線`／`整條落在`／`垂線`／`valid_perp`）於**生產路徑**"
        "命中 **0**；弱樣式之 %d 筆命中經 `D-1b` 逐筆裁斷**皆非** I-B 之閘（計入 ＝ %d）"
        % (adj_rows, adj_ib))
    say("    ⇒ 非 0 對照同法命中 > 0 ⇒ **搜法有判別力**（⛔ 非「搜不到」）")
    say("    🔒 `K-9-11-a` 逐字（`docs/rulings/K-6…:2386-2387`）：")
    for ln, txt in hit_lines("docs/rulings/K-6_街角地分配程序與可分配判準.md",
                             "不檢查垂線是否整條落在宗內"):
        say("      :%d  %s" % (ln, txt.strip()))
    say("    🛑 ⛔ **不得**出艙「現況零垂線宗數 ＝ N」——閘不存在 ≠ 命題為偽（節 71／98）；"
        "若探針硬從現行帶底路徑數出一個 `0`，該 `0` **視同未量**。")
    say("")
    say("  **D-3 落地閘（本批只寫·⛔ 不實作）**")
    say("    閘：`合格垂線數 == 0 ∧ 非④平行 ∧ 非第 0 宗` ⇒ 該宗 ∈ 不配地")
    say("    合成證偽（常設 8·設計已具名·⛔ 本批不造）：")
    say("      (甲) 造一宗「四至內 0 條合格垂線」——構造 ＝ 取其 `cut_coords`，令其於帶內之"
        "**弦寬** < `min_width`，並使**每條**自 FRONT 法向之線段皆有一段落在宗外；"
        "數法 ＝ 沿 `s` 掃斷點（同 `parcel_min_width_n14` 之分段線性斷點集）逐點檢"
        "「該垂線段 ⊆ 宗地多邊形」⇒ 期望「不配地 ＝ 是」")
    say("      (乙) 造一宗 ≥1 條合格垂線 ⇒ 期望「不配地 ⛔ 不因 I-B 觸發」")
    say("    ⇒ 舉不出「會使它為否」之輸入者，該閘**未成立**。")
    say("    🔒 `K-9-6-h ④` 判平行之街廓：本則⛔ 不適用；第 0 宗⛔ 不走本則（`K-9-12-e`）。")
    say("    🛑 I-A 與 I-B ⛔ **不得加總**（`K-9-11 五`）——本檔全程**分欄**、⛔ 無任何聯集數。")

    # ══════════════════════════════════════════════════════════════════════
    #  §E　不變式 I-C（矩形容納·負向）
    # ══════════════════════════════════════════════════════════════════════
    hdr("【§E】不變式 I-C（負向）：`K-9-12` 矩形容納**尚未生效**")

    IC_PATS = ["fits_at", "rect_fits", "矩形容納", "K-9-12"]
    probe_files = [p for p in TEXT
                   if (p.startswith("verify/probes/") or p.startswith("verify/tools/"))
                   and p.endswith(".py")]
    doc_files = [p for p in TEXT if p.startswith("docs/")]
    log_files = [p for p in TEXT if p.startswith("verify/out/")]
    say("  🔒 **分層**（碼面-生產／碼面-探針／文件／log·⛔ 不混計）；生產欄再分 `碼`／`非碼`")
    say("")
    say("    字樣            生產:碼  生產:非碼   探針+工具   docs/    verify/out/")
    ic_prod = 0
    for p in IC_PATS:
        s = layered_hits(PROD_FILES, p)
        b = total_hits(probe_files, p)[0]
        c = total_hits(doc_files, p)[0]
        d = total_hits(log_files, p)[0]
        ic_prod += s["碼"]
        say("    %-15s %7d  %9d   %9d   %6d   %6d"
            % ("`" + p + "`", s["碼"], s["註解"] + s["字串"], b, c, d))
    pop(len(IC_PATS), len(IC_PATS), "E-1 四字樣 × 四層（全列）")
    say("")
    say("    ⇒ **生產路徑可執行消費 ＝ %d**（停機③ 之受詞：須 ＝ 0 或僅探針）" % ic_prod)
    say("    ⇒ 停機③ %s" % ("⛔ **不觸發**" if ic_prod == 0 else "🛑 **觸發·上呈**"))
    say("    🔒 `K-9-12-b` 逐字（`K-6` 內）：")
    for ln, txt in hit_lines("docs/rulings/K-6_街角地分配程序與可分配判準.md",
                             "已裁定、⛔ 生產碼未實作")[:3]:
        say("      :%d  %s" % (ln, txt.strip()))
    say("    ⇒ 守護之預測（負向）：乙落地若未同時實作 `K-9-12`，"
        "⛔ 不得把「沒跑矩形容納」讀成「已通過可建築」。")

    # ══════════════════════════════════════════════════════════════════════
    #  §F　不變式 III（入池母體分帳）
    # ══════════════════════════════════════════════════════════════════════
    hdr("【§F】不變式 III：入池母體之**分帳**（乙甲產物 vs `K-6:109` 第二來源）")

    K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
    SRC7 = [
        ("1", "未通過寬深雙檢", K6, "未通過寬深雙檢",
         PROD_FILES, "寬深雙檢", "甲"),
        ("2", "未達街廓最小建築面積", K6,
         "未達街廓最小", PROD_FILES,
         "街廓最小建築面積", "甲"),
        ("3", "零合格垂線", K6, "一條合格垂線都沒有",
         PROD_FILES, "合格垂線", "乙"),
        ("4", "不得建築者", K6, "不得建築者",
         PROD_FILES, "不得建築者", "—"),
        ("5", "跨街廓同歸戶小往較大集中", K6,
         "小往較大集中", ["verify/wf_f0.py", "verify/wf_f2.py"],
         "級1相鄰", "🔴 非乙甲"),
        ("6", "末趟新產生之不合格宗", K6,
         "末趟新產生之不合格宗", PROD_FILES,
         "末趟新產生", "—"),
        ("7", "池內遞補合成宗", K6, "騰出之地",
         ["verify/wf_f4.py"], "配地階段", "—"),
    ]
    say("  🔒 判準（正面列舉）：正典內逐字謂「⇒ 進入七級調配／列入合併調配／入調配池」者。")
    say("  🔒 **判 ＝ 只看 `碼` 層**（可執行消費）；`註解`／`字串` 併列但⛔ 不計入判。")
    say("  🩸 **量測器之戒（本批自捕）**：`K-6:106-107` 之「未達街廓最小／建築面積」**跨行**"
        "⇒ 行內樣式必 0 命中；本表 `#2` 之正典錨改用行內可見之 `未達街廓最小`。")
    say("")
    say("    #  來源                          正典錨命中   碼側字樣                碼  註解  字串   判")
    n_src = 0
    for sid, name, anchor_f, anchor_pat, code_files, code_pat, tag in SRC7:
        na = total_hits([anchor_f], anchor_pat)[0]
        s = layered_hits(code_files, code_pat)
        verdict = "**已實作**" if s["碼"] > 0 else "`【查無】`"
        say("    %-2s %-28s %8d   %-22s %3d  %4d  %4d   %s / %s"
            % (sid, name, na, "`" + code_pat + "`", s["碼"], s["註解"], s["字串"],
               verdict, tag))
        if na == 0:
            raise RuntimeError("🔴 來源 #%s 之正典錨 `%s` 命中 0 ⇒ 錨壞（⛔ 不以 0 充作結論）"
                               % (sid, anchor_pat))
        n_src += 1
    pop(7, n_src, "F-1 七來源（全列）")
    say("    ⇒ **`#5` ⛔ 非乙甲之產物** ⇒ 落地後其增量須**另欄**、⛔ 不得算進「乙造成的池增量」。")

    say("")
    say("  **F-2 機械枚舉式**（`-95` C-3 之枚舉點·本批重查）")
    for rel in ("app.py", "verify/stepg_pipeline.py"):
        for ln, txt in hit_lines(rel, "_stage2_parcels = [tp for tp in parcels_in_blk"):
            say("    %s:%d  %s" % (rel, ln, txt.strip()))
    for ln, txt in hit_lines("verify/wf_f4.py", "配地階段"):
        say("    verify/wf_f4.py:%d  %s" % (ln, txt.strip()))
    for ln, txt in hit_lines("verify/wf_f4.py", "def add_syn"):
        say("    verify/wf_f4.py:%d  %s" % (ln, txt.strip()))
    say("    🛑 **live 入池清單 ＝【須執行該碼·本批⛔ 不跑】**（須 `run_step_g`；施工單 §零 F ⛔）")
    say("    ⚠️ baseline 之 `74·` 前綴係**代理**（`-95` 已具名射程）——`verify/baselines/wf/**.csv` "
        "含 `配地階段` **欄**者 ＝ **0** ⇒ 旗標不入 baseline 欄。")

    say("")
    say("  **F-3 守恆／不得超配**（凍結·本批只**重讀**現況·⛔ 不改）")
    pool_rows = [ln for ln in l92
                 if re.match(r"^\s+R\d\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+", ln)]
    for ln in pool_rows:
        say("    %s" % ln.rstrip())
    pop(6, len(pool_rows), "F-3 六街廓池（`-92` log 原樣重讀）")
    if len(pool_rows) != 6:
        raise RuntimeError("🔴 池表重讀得 %d 列（≠6）⇒ 解析器壞" % len(pool_rows))
    _pools = [float(ln.split()[3]) for ln in pool_rows]
    say("    `F-1` 池 > 0 之格 ＝ **%d／6**；最小池 ＝ **%.6f ㎡**（%s）"
        % (sum(1 for v in _pools if v > 0), min(_pools),
           pool_rows[_pools.index(min(_pools))].split()[0]))
    say("    `F-2` 守恆 ＝ **【可近似驗·附容差來源】**——`Σ配地幾何`（shapely 面積）與 `ΣG`"
        "（法定 2dp `round`）⛔ 非同一量 ⇒ 差為**捨入量**；")
    say("         🔒 容差來源逐字（`CLAUDE.md`）：")
    for ln, txt in hit_lines("CLAUDE.md", "ΣG(街廓內所有分配地)"):
        say("           CLAUDE.md:%d  %s" % (ln, txt.strip()))
    say("         ⛔ **不得以精確 `0` 當閘**（池採「量」⇒ 守恆殘差恆非零）。")
    say("    🔒 `T3′`（入池母體連續二批逐位不變）之**判法**："
        "取二批之 `[tp['暫編地號'] for tp in parcels_in_blk if '配地階段' in tp]`，逐位比對 ⇒ 可機械判；"
        "**本批⛔ 不跑二批 live**。")

    # ══════════════════════════════════════════════════════════════════════
    #  §G　落地後驗收表（欄名逐字鎖定·下一生產批將 grep 本表）
    # ══════════════════════════════════════════════════════════════════════
    hdr("【§G】落地後驗收表（欄名鎖定·⛔ 不得改欄名）")
    say("  | ID | 性質 | 現況出艙碼 | 乙落地後期望 | 閘會紅的條件 | 讀取位置（字樣 grep） |")
    say("  | II | 下一位＝_projection_order 次元 | %s | %s | 實作改用索引序或累積S | def _projection_order( |"
        % ("R2:%s→%s(投影序 %d→%d)／R5:%s→%s(投影序 %d→%d)"
           % (succ_rows[0][1], succ_rows[0][3], succ_rows[0][2], succ_rows[0][4],
              succ_rows[1][1], succ_rows[1][3], succ_rows[1][2], succ_rows[1][4]),
           "遞補者 ＝ 違反宗投影序號＋1 之宗（現算：R2 `%s`／R5 `%s`）"
           "🛑 與施工單所載期望「biz 索引 3」**不同空間**·見 §B-5c"
           % (succ_rows[0][3], succ_rows[1][3])))
    say("  | I-A | 交叉⇒不配地 | 2 宗（`-92` log 重讀：%s） | 該 2 宗 ∈ 不配地 | 該 2 宗仍配地 | "
        "w88.s_star_of／margin_of（probe_WG988_nocross） |" % sorted(VIOL.values()))
    say("  | I-B | 零垂線⇒不配地 | 【閘不存在】 | 閘存在且會紅 | 仍不檢查整條落在宗內 | "
        "parcel_min_width_n14／_n14_band_hi |")
    say("  | I-C | 矩形容納 | 未實作（生產消費 ＝ %d） | 乙批若未做 I-C，不得把未跑當通過 | 未跑卻標可建築 | K-9-12 |"
        % ic_prod)
    say("  | III | 入池分帳 | 七來源現查（#5 已實作·非乙甲下游） | 乙增量與 #5 分欄 | 乙帳含 #5 | _stage2_parcels |")
    say("  | F-1 | 池>0 | 6／6 皆 >0（最小 %.6f） | 六格仍 >0 | 任一格 ≤0 | 池 ＝ 幾何剩餘（`-92` log） |"
        % min(_pools))
    say("  | F-2 | 守恆近似 | 【可近似驗·附容差來源＝ CLAUDE.md 守恆句＋2dp round】 | 仍成立 | 以精確 0 當閘 | "
        "CLAUDE.md 守恆句 |")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§Y】停機款之判定（施工單 §五·逐款·⛔ 不略）")
    say("  款  觸發條件                                                    本批                                        判")
    say("  ①   `A0` 任一錨不符／`app.py` blob 變／開工閘紅                     八錨全符·開工閘全綠·blob 逐位未動            ⛔ 不觸發")
    say("  ②   `R2左`／`R5左` 之 `_projection_order` successor ≠ 3          生產輸入口徑：successor ＝ 投影序號 **2**"
        "（`biz` 索引 0）  🛑 **觸發·上呈**")
    say("      （biz 索引口徑：本批⛔ 無法重跑·須 `run_step_g` ⇒ 該受詞未開辦）")
    say("  ③   `I-C` 生產路徑已有矩形容納消費                                 生產 `碼` 層命中 ＝ **%d**（僅探針／文件）      ⛔ 不觸發" % ic_prod)
    say("  ④   探針把 `I-A`／`I-B`／`I-C` 加總成一個「不配地 N 宗」且未分欄        本檔全程分欄·⛔ 無任何聯集數                   ⛔ 不觸發")
    say("  ⑤   報告主張 `W-D.4` 碎片遞補可充乙介面                            `B-6` 已具名其受詞不同·⛔ 未主張可充             ⛔ 不觸發")
    say("  ⑥   `I-B` 出艙「現況零垂線 ＝ 0／N」而未標【閘不存在】                 `D-2` 逐字標【閘不存在】·⛔ 未出艙任何宗數        ⛔ 不觸發")
    say("  ⑦   預宣證偽輸入與實測相反，且對照組證明量測器非紅                     `B-3`／`B-5b` 之判別力皆成立（對照組會翻）        ⛔ 不觸發")
    say("  ⑧   `_projection_order` 定義命中 ≠ 1                            裸 grep ＝ **%d**·AST ＝ **%d**                ⛔ 不觸發"
        % (n_def, len(fdefs)))
    pop(8, 8, "Y 停機款（全列）")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§Z】略過與護欄之出艙")
    say("  略過（節 119·須具名，否則該量測⛔ 不成立）＝ **%d** 筆" % len(SKIPPED))
    for rel, why in SKIPPED[:20]:
        say("    %s ── %s" % (rel, why))
    pop(len(SKIPPED), min(len(SKIPPED), 20), "Z 略過清單")
    say("")
    say("  🛑 呼叫護欄之終檢（機械證明「未跑管線」）：%s" % CALLGUARD)
    if any(v for v in CALLGUARD.values()):
        raise RuntimeError("🔴 本批呼叫了被禁之管線函式：%s" % CALLGUARD)
    say("  ⇒ ✅ `run_step_g`／`run_corner_pk`／`run_verification.main` 之呼叫數 ＝ **0／0／0**")
    say("  ⇒ ✅ 本批⛔ 未跑 `run_all`（log 內無本次 `run_all` 產物）")

    with open(log_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n[log] %s" % log_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
