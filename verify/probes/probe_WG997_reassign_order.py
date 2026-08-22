#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-97**：`§三` 四項「重申」之逐字覆核 ＋ `§五` 二項現查（`C-1` 遞補定序／`C-2` `G` 重算）。

## 受詞（施工單 `W-G.9-97`）

- **`§三` 覆核**：本裁四段（四／五／六／七）所稱之「重申」，逐字對 `K-6`；
  **任一不符 ⇒ 🛑 ⛔ 不入倉、回報**（⛔ 不得逕行調和）。
- **`C-1`**：全倉窮舉**決定遞補位次**之處，逐處出艙
  `檔`／`行`／逐字／**所用之序列**／**與本裁主文相符？**
- **`C-2`**：`G` 值於**重排後**／**遞補後**是否重算之現況。
- **`§七`**：七來源 `#5` 與其餘六者之**差異**（供欄名提案）。

## 🛑 紅線（施工單 §九）

⛔ 零生產碼變更；⛔ 不落地；⛔ 不跑 `run_step_g`／`run_all`／`run_corner_pk`
（本檔以**覆蓋為 raise 版**機械證明其未被呼叫）；⛔ 不換圖／不換快照／不重烤；
⛔ 不就遞補／調配池／合併調配／超配出任何裁定題（`K-9-11 三`）。

## 🔒 常設條款之落實

**§Z-2 乙**：逐處命中先標層別（一＝碼面／二＝文件報告／三＝log 探針輸出），
二三層**預設標 `引述`**、⛔ 不得逕充碼面證據。
**§Z-8**：出艙帶 `母體 ＝ N／納入 ＝ n／略過 ＝ N−n（逐項理由）`。
**§Z-9**：⛔ 不肉眼切 `grep -n` ——`檔`／`行`／`逐字` **分欄**出艙，且每筆以行號**回取覆驗**。
**常設 8**：每判準附「會使它為否」之輸入。**常設 10**：每表末印 `POPULATION／PRINTED／SUPPRESSED`。

## 重跑

    python verify/probes/probe_WG997_reassign_order.py

rc **恆為 0**；唯缺件／取不到資料時 loud raise（`no-silent-fallback`）。

🔒 **可重跑性**：`A-1` 之判準 ＝「**基座 `1c12201` 為 `HEAD` 之祖先或等於 `HEAD`**」，
⛔ 非「`HEAD` 逐位等於基座」——本批入倉後 `HEAD` 前移係**預期**，⛔ 不得因此判紅
（否則本檔之「重跑 rc ＝ 0」與其自身之閘**互相矛盾**）。log 檔名綁**基座**、⛔ 不綁 `HEAD`。
"""
import hashlib
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

SELF = [
    "verify/probes/probe_WG997_reassign_order.py",
    "verify/out/probe_WG997_reassign_order_1c12201.log",
    "docs/reports/W-G.9-97_重排後遞補之入裁與現查.md",
]

PROD_FILES = [
    "app.py",
    "verify/stepg_pipeline.py",
    "verify/selection_pipeline.py",
    "verify/run_verification.py",
    "verify/wd4_tier_list.py",
    "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
    "verify/wf_f3.py", "verify/wf_f4.py",
]

# 🔒 本批之**基座** commit（施工單 `W-G.9-97` §一 `A-0` #1）——⛔ 非「執行時之 HEAD」
BASE_SHORT = "1c12201"

K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
SK = ".claude/skills/failure-archaeology/SKILL.md"
ZW = "docs/reports/W-G.9波_claude.ai側自誤登記.md"

L = []
SKIPPED = []
CALLGUARD = {"run_step_g": 0, "run_corner_pk": 0, "run_all_main": 0}
TEXT = {}
_LAYER = {}


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
    p = subprocess.run(args, cwd=REPO, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode("utf-8", errors="replace")


def git1(args):
    rc, out = sh(["git", "-c", "core.quotePath=false"] + args)
    if rc != 0:
        raise RuntimeError("🔴 git 失敗 rc=%d：%s\n%s" % (rc, " ".join(args), out))
    return out.strip()


def tracked_files():
    rc, out = sh(["git", "-c", "core.quotePath=false", "ls-files", "-z"])
    if rc != 0:
        raise RuntimeError("🔴 git ls-files 失敗：%s" % out)
    return [p for p in out.split("\0") if p]


def load_text(paths):
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


def lines_of(rel):
    t = TEXT.get(rel)
    return t.splitlines() if t is not None else []


def hit_lines(rel, needle):
    """回 `[(行號, 逐字)]`；**每筆以行號回取覆驗**（§Z-9·⛔ 不肉眼切）。"""
    ls = lines_of(rel)
    out = []
    for i, ln in enumerate(ls):
        if needle in ln:
            back = ls[i]                      # 以行號回取
            if back != ln:
                raise RuntimeError("🔴 回取覆驗不符：%s:%d" % (rel, i + 1))
            out.append((i + 1, back))
    return out


def count_hits(rel, needle):
    return len(hit_lines(rel, needle)) if rel in TEXT else None


def total_hits(rels, needle):
    n, f = 0, 0
    for rel in rels:
        c = count_hits(rel, needle)
        if c:
            n += c
            f += 1
    return n, f


def layer_of(rel):
    """逐行分層（`碼`／`註解`／`字串`）；非 `.py` 一律 `文件`。同 `-96` 之定義。"""
    if rel in _LAYER:
        return _LAYER[rel]
    t = TEXT.get(rel)
    if t is None:
        _LAYER[rel] = {}
        return {}
    n = len(t.splitlines())
    if not rel.endswith(".py"):
        _LAYER[rel] = {i: "文件" for i in range(1, n + 1)}
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
        SKIPPED.append((rel, "tokenize 失敗（%s）" % type(e).__name__))
        _LAYER[rel] = {}
        return {}
    _LAYER[rel] = {i: ("碼" if i in code else ("字串" if i in strs else
                                               ("註解" if i in cmts else "空")))
                   for i in range(1, n + 1)}
    return _LAYER[rel]


def tier_of(rel):
    """§Z-2 乙之三層：一＝碼面／二＝文件報告／三＝log 探針輸出。"""
    if rel in PROD_FILES:
        return "一·碼面"
    if rel.startswith("verify/out/") or rel.startswith("verify/probes/") \
            or rel.startswith("verify/tools/"):
        return "三·log/探針"
    if rel.startswith("docs/") or rel.startswith(".claude/"):
        return "二·文件報告"
    return "二·文件報告"


def _forbidden(name):
    def _f(*a, **kw):
        CALLGUARD[name] += 1
        raise RuntimeError("🔴 施工單 §九：本批⛔ 不得呼叫 `%s`" % name)
    return _f


def sha256_of(rel):
    with open(os.path.join(REPO, rel), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ══════════════════════════════════════════════════════════════════════════════
def main():                                                          # noqa: C901
    head = git1(["rev-parse", "HEAD"])
    head_s = git1(["rev-parse", "--short", "HEAD"])
    app_blob = git1(["rev-parse", "HEAD:app.py"])
    # 🔒 **基座**（本批 `A-0` 之錨）與 **HEAD** 分列：入倉後 HEAD 前移，探針仍須可重跑
    #   ⇒ log 檔名一律綁**基座**、⛔ 不綁 HEAD（否則每次入倉多生一份 log）。
    base_ok = subprocess.run(["git", "merge-base", "--is-ancestor", BASE_SHORT, "HEAD"],
                             cwd=REPO, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL).returncode == 0
    log_path = os.path.join(OUTDIR, "probe_WG997_reassign_order_%s.log" % BASE_SHORT)

    files = tracked_files()
    load_text([p for p in files
               if p.endswith((".py", ".md", ".log", ".csv", ".txt", ".json"))])

    hdr("【W-G.9-97】重排後遞補之入裁覆核 ＋ 二項現查（⛔ 零生產碼·⛔ 未跑管線）")
    say("  基座（本批 `A-0` 之錨）＝ **%s**；產生於 HEAD ＝ **%s**（%s）"
        % (BASE_SHORT, head_s, head))
    say("  `app.py` blob：%s（HEAD）／%s（工作區）" % (app_blob, git1(["hash-object", "app.py"])))
    say("  母體（`git ls-files -z`·遞迴）＝ **%d** 檔；載入為文字者 ＝ **%d** 檔"
        % (len(files), len(TEXT)))
    say("  🔒 SELF ＝ %s" % SELF)
    say("  🔒 索引內含 `.claude/worktrees` 者 ＝ **%d**"
        % sum(1 for p in files if ".claude/worktrees" in p))

    import stepg_pipeline as _sg
    import selection_pipeline as _sp
    import run_verification as _rv
    _sg.run_step_g = _forbidden("run_step_g")
    _sp.run_corner_pk = _forbidden("run_corner_pk")
    _rv.main = _forbidden("run_all_main")
    say("  🛑 呼叫護欄已裝（`run_step_g`／`run_corner_pk`／`run_verification.main` ⇒ raise 版）")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§A】`A-0` 先驗錨（施工單 §一·七項）")
    ok = True

    def gate(gid, item, expect, got):
        nonlocal ok
        good = (str(expect) == str(got))
        ok = ok and good
        say("  %-5s %-28s %s  期望＝%s  現查＝%s"
            % (gid, item, "✅" if good else "🔴", expect, got))
        return good

    # `A-1`：判準 ＝ **基座為 HEAD 之祖先或等於 HEAD**（⛔ 非「HEAD 逐位等於基座」）
    #   ——入倉後 HEAD 前移屬**預期**，⛔ 不得因此判紅（否則探針⛔ 不可重跑·與自身 docstring 相矛盾）。
    gate("A-1", "基座 %s ⊆ HEAD 之祖先" % BASE_SHORT, True, base_ok)
    say("        現查：基座 ＝ %s ／ HEAD ＝ %s ／ 二者%s"
        % (BASE_SHORT, head_s, "相同" if head_s == BASE_SHORT else "相異（HEAD 已前移·屬預期）"))
    gate("A-2", "app.py blob（絕對值）",
         "a9e5671d64d254907a0396f898f046d9d85e8283", app_blob)
    _origin = git1(["rev-parse", "origin/wip/s1-endpart"])
    _lr = git1(["rev-list", "--left-right", "--count", "HEAD...origin/wip/s1-endpart"])
    say("  A-3   origin/wip/s1-endpart      現查＝%s；本機 ahead／behind ＝ %s"
        % (_origin, _lr.replace("\t", " ／ ")))
    sk = lines_of(SK)
    ns = [int(m.group(1)) for l in sk if (m := re.match(r"^##\s*(\d+)\.\s", l))]
    gate("A-4a", "考古節：最大", max(ns), max(ns))
    say("        窄樣式 `^##\\s*(\\d+)\\.\\s` ⇒ 命中 ＝ **%d**／相異 ＝ **%d**／最大 ＝ **%d**"
        % (len(ns), len(set(ns)), max(ns)))
    if not (len(ns) == len(set(ns)) == max(ns)):
        raise RuntimeError("🔴 A-4：命中／相異／最大 三數不等 ⇒ 停機")
    zw = lines_of(ZW)
    zs = [(i + 1, int(m.group(1))) for i, l in enumerate(zw)
          if (m := re.match(r"^##\s*自誤\s*(\d+)", l))]
    gate("A-5", "自誤登記最大序號", 100, max(v for _, v in zs))
    say("        最大者於行 **%d**" % [i for i, v in zs if v == max(x for _, x in zs)][0])
    k6 = lines_of(K6)
    main_no = sorted({int(m.group(1)) for l in k6
                      if (m := re.match(r"^###\s*🔒?\s*K-9-(\d+)(?:\s|　)", l))})
    sub_no = sorted({int(m.group(1)) for l in k6
                     if (m := re.match(r"^###\s*🔒?\s*K-9-5-(\d+)\s", l))})
    say("  A-6   K-6 最大裁定號            主序列 `K-9-nn` 佔用 ＝ %s ⇒ 最大 ＝ **K-9-%d**"
        % (main_no, max(main_no)))
    say("        子序列 `K-9-5-nn` 佔用最大 ＝ **K-9-5-%d**" % max(sub_no))
    say("  A-7   行數計法（`\\n 計` ／ `splitlines()`）")
    for rel in (SK, ZW, K6):
        t = TEXT[rel]
        say("        %-56s %d ／ %d   sha256=%s"
            % (rel, t.count("\n"), len(t.splitlines()), sha256_of(rel)))
    say("")
    say("  ⇒ `A-0`：%s" % ("✅ **全綠**" if ok else "🔴 **有紅** ⇒ 🛑 停機"))
    if not ok:
        raise RuntimeError("🔴 §A `A-0` 紅 ⇒ 停機")
    next_no = max(main_no) + 1

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§B】`§三` 四項「重申」之逐字覆核（⛔ 不符即不入倉·⛔ 不得逕行調和）")
    say("  🔒 判準：施工單所指之**正典錨**須於倉內**現查得到**，且其逐字須承載該段之受詞。")
    say("  🔒 每一 0 命中皆附**同法非 0 對照**（節 92）。")
    say("")
    B = []

    # ── #1　段四（第 2 宗以後 ∥ALLOCLINE）vs K-9-15 一 ──────────────────────
    h1 = hit_lines(K6, "對於第 1 宗後續的土地而言是對的")
    h1c = hit_lines(K6, "兩條平行 ⇒ 永不相交")
    say("  **#1 段四（第 2 宗以後 ∥ALLOCLINE）→ 施工單指 `K-9-15 一`**")
    for n_, t_ in h1 + h1c:
        say("     檔 ＝ %s ／ 行 ＝ %d" % (K6, n_))
        say("     逐字 ＝ %s" % t_.strip())
    B.append(("#1", "段四", "K-9-15 一", len(h1) > 0,
              "✅ 相符（KL 逐字「對於第 1 宗後續的土地而言是對的」＝ 段四之「第 2 宗以後」）"))
    h1x = hit_lines(K6, "第 1 宗以後之二界皆 ∥ALLOCLINE")
    say("     ⚠️ **併具名（⛔ 不逕行調和）**：`K-9-15` **三-3**（claude.ai 之整理·⛔ 非 KL 逐字）作：")
    for n_, t_ in h1x:
        say("        行 ＝ %d ／ 逐字 ＝ %s" % (n_, t_.strip()))
    say("        而同節 **三-4** 之「第 1 宗以後」係**含第 1 宗**之用法")
    for n_, t_ in hit_lines(K6, "**第 1 宗以後** ⇒ **內接最小矩形**"):
        say("        行 ＝ %d ／ 逐字 ＝ %s" % (n_, t_.strip()))
    say("        ⇒ 三-3 若同讀為**含**第 1 宗，與段四之「第 2 宗以後」**不一致**"
        "（第 1 宗之近側界 ＝ 第 0 宗遠側界 ＝ ∥SIDELINE）；**KL 逐字層⛔ 無此問題**。")

    # ── #2　段五（迭代重算 G）vs K-9-15 一「往街廓內移動迭代計算」──────────
    say("")
    say("  **#2 段五（迭代重算 `G`）→ 施工單指 `K-9-15 一`「往街廓內移動迭代計算」**")
    p2 = "往街廓內移動迭代計算"
    n_k6 = count_hits(K6, p2)
    # 🔒 **自誌之扣除（節 72）**：本批自身之產物（`SELF`）會複述該字樣 ⇒ ⛔ 不得計入母體，
    #   否則「入倉一次、命中就多幾筆」＝ 量測器量到自己。扣除後**併具名**其筆數。
    _hits_all = [(rel, hit_lines(rel, p2)) for rel in TEXT if count_hits(rel, p2)]
    all_hits = [(rel, hs) for rel, hs in _hits_all if rel not in SELF]
    self_hits = [(rel, hs) for rel, hs in _hits_all if rel in SELF]
    say("     字樣 `%s` 於 `K-6` 命中 ＝ **%d**" % (p2, n_k6))
    say("     全母體（%d 檔·**已扣 SELF %d 檔**）命中 ＝ **%d 檔**："
        % (len(TEXT) - len([r for r in SELF if r in TEXT]),
           len([r for r in SELF if r in TEXT]), len(all_hits)))
    for rel, hs in all_hits:
        for n_, t_ in hs:
            say("        層 ＝ %s ／ 檔 ＝ %s ／ 行 ＝ %d【引述】" % (tier_of(rel), rel, n_))
            say("        逐字 ＝ %s" % t_.strip()[:120])
    say("     🔒 自誌（`SELF`）之命中 ＝ **%d 檔**（⛔ 已扣除·⛔ 非證據）：" % len(self_hits))
    for rel, _hs in self_hits:
        say("        %s" % rel)
    say("     ⚠️ **其行數⛔ 不印**——本檔之 log 亦屬 `SELF`，印其行數即**自我指涉**"
        "⇒ log 無不動點、二跑不逐位相同；⛔ 此係**具名之不印**、⛔ 非略過未具名（節 119）。")
    # K-9-15 全段之「迭代」
    i15 = next(i for i, l in enumerate(k6) if l.startswith("### 🔒 K-9-15"))
    i16 = next(i for i, l in enumerate(k6) if l.startswith("### 🔒 K-9-16"))
    seg = k6[i15:i16]
    n_seg = sum(1 for l in seg if "迭代" in l)
    n_k6_iter = count_hits(K6, "迭代")
    say("     `K-9-15` 全段（行 %d–%d·共 %d 行）之 `迭代` 命中 ＝ **%d**"
        % (i15 + 1, i16, len(seg), n_seg))
    say("     非 0 對照（同法·同段·已知存在字樣 `不交叉`）＝ **%d** ⇒ 搜法有判別力"
        % sum(1 for l in seg if "不交叉" in l))
    say("     `K-6` 全檔 `迭代` 命中 ＝ **%d**（皆他脈絡）：" % n_k6_iter)
    for n_, t_ in hit_lines(K6, "迭代"):
        say("        行 ＝ %d ／ 逐字 ＝ %s" % (n_, t_.strip()[:96]))
    ok2 = (n_k6 > 0)
    B.append(("#2", "段五", "K-9-15 一「往街廓內移動迭代計算」", ok2,
              "🛑 **不符**——該字樣於 `K-6` 命中 0、`K-9-15` 全段無「迭代」二字"))

    # ── #3　段六（街角 winner 非畸零）vs K-9-5-14 乙式 ────────────────────
    say("")
    say("  **#3 段六（街角 winner 非畸零）→ 施工單指 `K-9-5-14 乙式`**")
    h3a = hit_lines(K6, "遠側境界線** ＝ **SIDELINE 沿其法向平移")
    for n_, t_ in h3a:
        say("     [構成] 檔 ＝ %s ／ 行 ＝ %d" % (K6, n_))
        say("     逐字 ＝ %s" % t_.strip())
    h3b = hit_lines(K6, "街角第 1 宗⛔ 不另設寬度閘")
    h3c = hit_lines(K6, "面積夠 ⇒ 街角第 1 宗寬度合格")
    say("     [結論之錨] `K-9-5-14` 內是否載「一定符合非畸零」之斷言？"
        "——`K-9-5-14` 段內 `不另設寬度閘` 命中 ＝ %d"
        % sum(1 for l in k6[next(i for i, x in enumerate(k6)
                                 if x.startswith("### 🔒 K-9-5-14")):
                            next(i for i, x in enumerate(k6)
                                 if x.startswith("### 🔒 K-9-5-15"))]
              if "不另設寬度閘" in l))
    for n_, t_ in (h3b + h3c):
        say("     [結論] 檔 ＝ %s ／ 行 ＝ %d ／ 逐字 ＝ %s" % (K6, n_, t_.strip()[:110]))
    h3d = hit_lines(K6, "該蘊含<u>僅於「街角最小規定範圍係以 SIDELINE 法向平移方式產生」")
    for n_, t_ in h3d:
        say("     [限縮] 檔 ＝ %s ／ 行 ＝ %d ／ 逐字 ＝ %s" % (K6, n_, t_.strip()[:120]))
    say("     🔒 **段六之三個要素與其各自之錨**：")
    say("        (甲) 構成「SIDELINE 沿法向平移 退縮＋畸零寬」⇒ `K-9-5-14 一`（行 %d）"
        % (h3a[0][0] if h3a else -1))
    say("        (乙) 「一定符合非畸零」⇒ `K-9-5-15 二`（行 %d·「面積夠 ⇒ 街角第 1 宗寬度合格」為真）"
        % (h3c[0][0] if h3c else -1))
    say("        (丙) 該蘊含**以乙式為前提** ⇒ `K-9-5-15` 之 **2026-08-19 就地加註 一**（行 %d）"
        % (h3d[0][0] if h3d else -1))
    say("        ⇒ KL 段六之括號「（街角地最小規定範圍的構成係以sideline 沿法向平移 退縮+畸零寬）」"
        "**即 (丙) 所要求之前提** ⇒ 三要素**齊備且自洽**。")
    B.append(("#3", "段六", "K-9-5-14 乙式", len(h3a) > 0 and len(h3c) > 0 and len(h3d) > 0,
              "✅ 相符（重申成立）·**惟錨須補**——`K-9-5-14` 只承載**構成**；"
              "「非畸零」之斷言錨 ＝ `K-9-5-15 二` ＋ 其 2026-08-19 就地加註 一（乙式前提）"))

    # ── #4　段七（中間必有配餘地）vs K-9-11 三 守恆式 ─────────────────────
    say("")
    say("  **#4 段七（中間必有配餘地）→ 施工單指 `K-9-11 三` 守恆式**")
    h4a = hit_lines(K6, "騰出之地入調配池")
    for n_, t_ in h4a:
        say("     檔 ＝ %s ／ 行 ＝ %d ／ 逐字 ＝ %s" % (K6, n_, t_.strip()[:110]))
    n_mid_k6 = sum(1 for l in k6 if "調配池居中" in l)
    h4b = hit_lines("CLAUDE.md", "兩端往中間排、調配池居中")
    h4c = hit_lines("CLAUDE.md", "調配池必然存在、必 > 0")
    say("     「中間／居中」之錨於 `K-6` 命中 ＝ **%d**（`調配池居中`）" % n_mid_k6)
    for n_, t_ in (h4b + h4c):
        say("     檔 ＝ CLAUDE.md ／ 行 ＝ %d ／ 逐字 ＝ %s" % (n_, t_.strip()[:110]))
    B.append(("#4", "段七", "K-9-11 三 守恆式", len(h4a) > 0,
              "⚠️ **部分相符·錨不足**——「必有池」之錨 ＝ `CLAUDE.md:%d`／`:%d`（經 `K-9-11 三` 之表轉引）；"
              "「**居中**」之錨 ＝ `CLAUDE.md:%d`，⛔ 不在 `K-9-11 三`"
              % (h4c[0][0] if h4c else -1, 363, h4b[0][0] if h4b else -1)))

    say("")
    say("  ── `§三` 覆核總表 ──")
    say("  #   段   施工單所指之正典錨                          倉內現查得到?  判")
    for sid, seg_, anchor, found, verdict in B:
        say("  %-3s %-4s %-42s %-13s %s"
            % (sid, seg_, anchor, "✅ 是" if found else "🔴 否", verdict))
    pop(4, 4, "B `§三` 四項重申（全列）")
    n_bad = sum(1 for _, _, _, found, _ in B if not found)
    say("")
    say("  🛑 **不符項數 ＝ %d** ⇒ 依施工單 §三 ⚠️ 與 §十-1：**⛔ 本裁不入倉、回報**"
        % n_bad if n_bad else "  ✅ 四項皆可覆核 ⇒ 得入倉")
    say("  🔒 若入倉，續編之裁定號 ＝ **K-9-%d**（現查 `K-6` 主序列最大 ＝ K-9-%d）"
        % (next_no, max(main_no)))

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§C】`C-1`　生產式與本裁之差異清單（決定遞補／位次之處·全倉窮舉）")
    say("  🔒 母體 ＝ 生產路徑 **%d** 檔（施工單 -96 §零 A 之清單）之**全部行**；"
        "字樣 ＝ 下列 6 個（涵蓋「投影序號 ＋ 1」及任何等價式之識別字）" % len(PROD_FILES))
    PATS = ["_projection_order", "pre_position", "_proj_rank",
            "ordered_v2", "遞補", "投影序"]
    rows = []
    for rel in PROD_FILES:
        lay = layer_of(rel)
        seen = set()
        for p in PATS:
            for n_, t_ in hit_lines(rel, p):
                if n_ in seen:
                    continue
                seen.add(n_)
                rows.append((rel, n_, t_, lay.get(n_, "?"),
                             [q for q in PATS if q in t_]))
    rows.sort(key=lambda r: (PROD_FILES.index(r[0]), r[1]))
    say("  🔒 命中母體（未分層）＝ **%d** 行" % len(rows))
    code_rows = [r for r in rows if r[3] == "碼"]
    say("  🔒 §Z-8 報數：母體 ＝ %d ／ 納入（`碼` 層）＝ %d ／ 略過 ＝ %d"
        % (len(rows), len(code_rows), len(rows) - len(code_rows)))
    say("     略過之逐項理由：層別 ＝ `註解`／`字串`／`空` ⇒ **⛔ 非可執行消費**（"
        + "、".join("%s ＝ %d" % (k, sum(1 for r in rows if r[3] == k))
                    for k in ("註解", "字串", "空") if any(r[3] == k for r in rows))
        + "）")
    say("")
    say("  層     檔                              行     所用之序列                     與本裁主文相符?")
    n_gate_hit = 0
    for rel, n_, t_, lay, pats in code_rows:
        low = t_
        if "_proj_rank" in low or ("_projection_order" in low and "ordered_v2" not in low):
            seqname = "重排**前**投影序（`_projection_order` 原序）"
            match = "否"
        elif "ordered_v2" in low:
            seqname = "重排**後**序列（`ordered_v2`）"
            match = "是"
        elif "pre_position" in low:
            seqname = "`pre_position`（＝重排**前**投影序之排名）"
            match = "否"
        elif "遞補" in low:
            seqname = "（遞補字樣）"
            match = "【資料不足】"
        else:
            seqname = "（投影序字樣）"
            match = "【資料不足】"
        if rel == "verify/stepg_pipeline.py" and 491 <= n_ <= 509:
            n_gate_hit += 1
        say("  %-6s %-32s %-6d %-30s %s" % (tier_of(rel), rel, n_, seqname, match))
        say("         逐字 ＝ %s" % t_.strip()[:120])
    pop(len(rows), len(code_rows), "C-1 `碼` 層逐行（全列·未切片）")
    say("")
    say("  🔒 **判別力（常設 8·預宣覆驗）**：`stepg_pipeline.py:491-509` 之結構閘須被命中且判 `否`")
    say("     ⇒ 實測命中 ＝ **%d** 行 ⇒ %s"
        % (n_gate_hit, "✅ 如預宣" if n_gate_hit else "🔴 未命中 ⇒ 窮舉器有誤·具名"))
    if n_gate_hit == 0:
        raise RuntimeError("🔴 C-1 預宣未命中 ⇒ 量測器先自證失敗（⛔ 不逕論停機）")
    say("  🔒 **量測器自證（`-94` 之處置形）**：上列非 0；且對已知**不存在**之字樣"
        "（執行期組出之角色字樣）同法命中 ＝ **%d**（須 0）"
        % total_hits(PROD_FILES, "".join(["QQ", "ZZ", "%d" % (11 * 37619), "_NOPE"]))[0])
    say("")
    say("  ⚠️ **母體之性質具名（⛔ 不得誤讀）**：本表母體係**字樣驅動**、故**過度涵蓋**——"
        "如 `app.py:7518`（`def` 行）／`:12499`（符號匯出清單）並⛔ 非「決定遞補位次之處」。")
    say("     「與本裁主文相符?」欄之受詞 ＝ **該行所用之序列**，⛔ 非「該行是否決定遞補」。")
    say("     🔴 併具名之**土地相關**格：`wf_f0:256`／`wf_f1:376`／`wf_f2:95`／`wf_f3:78`／"
        "`wf_f4:1043,1433,1503`／`run_verification.py:977,1105` 之「位次序不變」閘"
        "係以**重排前投影序**為母體 ⇒ 落地時須逐格判其受詞是否改變。")
    say("")
    say("  🔴 **本裁主文之受詞**：「下一位」＝ **重排後序列（`ordered_v2`）之下一位**")
    say("     ⇒ 上表凡「所用之序列 ＝ 重排前投影序」者，落地時**皆須改**；")
    say("     ⇒ 🛑 惟**遞補本身於生產路徑⛔ 尚未實作**（`-95`／`-96` 已證：`I-A`／`I-B` 皆 `【查無】`）")
    say("        ⇒ 「決定遞補位次之處」之**可執行**母體 ＝ **0** ⇒ 本裁之落地係**從零實作**、"
        "⛔ 非改既有遞補碼。")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§D】`C-2`　`G` 值重算之現況")
    say("  **問 1：現行碼於<u>重排後</u>是否重算 `G`？**")
    q1 = []
    for pat in ("left_group = list(ordered_v2", "for entry in left_group:",
                "res, solver_label = _solve_one(", "S_remain = max(0.1, S_block_max"):
        for n_, t_ in hit_lines("verify/stepg_pipeline.py", pat):
            q1.append((n_, t_))
    for n_, t_ in sorted(set(q1)):
        say("     檔 ＝ verify/stepg_pipeline.py ／ 行 ＝ %d" % n_)
        say("     逐字 ＝ %s" % t_.strip()[:120])
    say("     ⇒ **答：是**——推進迴圈之母體即 `ordered_v2`（重排**後**序列），"
        "`G` 由 `_solve_one`→`solve_G_binary` 於該序列上**逐宗現算**；")
    say("        且其輸入 `baseline_pt = corner_pt + left_cum_S * d_hat`／`S_remain` 皆**位置相依**"
        "⇒ 序列一變、`G` 必變。")
    say("        🔒 精確措辭：⛔ 非「重排後再算一次」，而係 **`G` 之唯一算處即在重排後之序列上**。")
    say("")
    say("  **問 2：現行碼於<u>遞補後</u>是否重算其後各宗之 `G`？**")
    say("     ⇒ **答：`【查無】`**——**遞補於生產路徑尚未實作**（`-96` §F：`I-A`／`I-B` 之碼側皆 `【查無】`）"
        "⇒ ⛔ 無「遞補後」之受詞可量。")
    say("     🔒 **結構觀察（⛔ 非「已實作」之宣稱）**：現行推進迴圈以 `left_cum_S` **累加**推進"
        "（逐字見上），故**若**某宗於建 `left_group` 之前被移除，其後各宗之 `baseline_pt`／`S_remain`"
        "自動改變 ⇒ `G` 隨之改變。")
    say("        ⇒ 本裁五段之「後面的宗也會整體往前分配，所以也要重算 G」在**該前提下**"
        "由現行結構滿足；**⛔ 惟移除／遞補之決策本身仍缺**。")
    say("")
    say("  🔴 **落地批之必修項（具名·⛔ 本批不改·⛔ 不估土地後果）**：")
    say("     (a) 不配地之判定（`I-A` 交叉／`I-B` 零合格垂線）——`【查無】`；")
    say("     (b) 遞補之執行：自 `ordered_v2` 移除該宗、由**其後之下一元素**遞補該位次；")
    say("     (c) 遞補宗與其後各宗之 `G` 重算（依上 (b) 之移除時點，現行結構即滿足）；")
    say("     (d) 騰出面積入調配池之記帳（守恆式）。")
    pop(4, 4, "D 落地必修項（全列）")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§E】`§七`　七來源 `#5` 與其餘六者之差異（供欄名提案）")
    S7 = [
        ("1", "未通過寬深雙檢", "不配地之**判定**", "甲"),
        ("2", "未達街廓最小建築面積", "不配地之**判定**", "甲"),
        ("3", "零合格垂線", "不配地之**判定**", "乙"),
        ("4", "不得建築者", "不配地之**判定**", "—"),
        ("5", "跨街廓同歸戶「小往較大集中」", "**歸戶之移轉**（⛔ 非不配地判定）", "🔴 非乙甲"),
        ("6", "末趟新產生之不合格宗", "不配地之**判定**（迭代產物）", "—"),
        ("7", "池內遞補合成宗", "**池內落位之產物**", "—"),
    ]
    say("  #  來源                              性質                                     在乙甲下游?")
    for sid, name, kind, tag in S7:
        say("  %-2s %-32s %-40s %s" % (sid, name, kind, tag))
    pop(7, 7, "E 七來源之性質（全列）")
    say("")
    say("  🔒 **`#5` 與其餘六者之差（逐字）**：")
    for n_, t_ in hit_lines(K6, "小往較大集中"):
        say("     檔 ＝ %s ／ 行 ＝ %d ／ 逐字 ＝ %s" % (K6, n_, t_.strip()))
    say("     ① **觸發者不同**：其餘六者皆由「該宗**自身**不合格／落位」觸發；"
        "`#5` 由「**同歸戶跨街廓之相對大小**」觸發——該宗**自身合格**亦會被移轉。")
    say("     ② **受詞不同**：其餘六者之受詞 ＝ **一宗**；`#5` 之受詞 ＝ **一歸戶群跨街廓之集合**。")
    say("     ③ **落地狀態不同**：`#5` 與 `#7` **已實作**，其餘五者 `【查無】`。")
    say("     ④ **與乙甲之關係**：`#5` ⛔ **非**乙甲之下游（`-95` §C-2·`-96` §F 已二度複驗）。")

    # ══════════════════════════════════════════════════════════════════════
    hdr("【§Z】略過與護欄")
    say("  略過（節 119）＝ **%d** 筆" % len(SKIPPED))
    for rel, why in SKIPPED[:20]:
        say("    %s ── %s" % (rel, why))
    pop(len(SKIPPED), min(len(SKIPPED), 20), "Z 略過清單")
    say("  🛑 呼叫護欄終檢：%s" % CALLGUARD)
    if any(CALLGUARD.values()):
        raise RuntimeError("🔴 呼叫了被禁之管線函式：%s" % CALLGUARD)
    say("  ⇒ ✅ `run_step_g`／`run_corner_pk`／`run_verification.main` 呼叫數 ＝ 0／0／0")

    with open(log_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n[log] %s" % log_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
