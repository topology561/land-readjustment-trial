# -*- coding: utf-8 -*-
r"""`W-G.9-101`：純追加稽核器之**受詞母體缺口**（量測·⛔ 零管線）。

## 受詞

`wg942_append_audit` 之受詞由**人工維護之硬編清單** `TARGETS` 界定 ⇒ 其「綠」
⛔ 不蘊含「本批之受詞皆已受檢」。二者之差即**受詞母體缺口**（`GB-88`／`VR-059`）。

## 🔒 母體之態（`VR-058 三` 之自我適用）

- `TARGETS` **自 `blob@BASE_FULL` 取**（`git show`），⛔ **不自工作區 import**
  —— 否則本批之補登會使 `S-1`／`S-8` 漂移。
- commit 範圍**寫死為具名區間** `LOW..BASE_FULL`（⛔ 不用 `HEAD` 等隨態漂移之寫法）。
- 🔒 本檔**不印任何隨 `HEAD` 而變之值** ⇒ 補登前後重跑之輸出**逐位相同**（`驗收 11`）。

## 🔒 `core.quotepath`

一切 `git` 呼叫**明綁 `-c core.quotepath=false`**；唯 `S-4` 之受詞刻意取**二框對照**。

## 受詞之定義

狀態 `M`（⛔ 不含 `A`·新檔本器與稽核器皆略過）且尾綴 `.md` 者。

## 預測值之出處（`fixture-provenance`）

`S-1`〜`S-8` 之期望值**逐項引自施工單** `W-G.9-101` `§二 2-1`（⛔ 非由本檔現跑一次回填）。

## 重跑

    python verify/probes/probe_WG9103_targetcov.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
"""
import ast
import collections
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "65f575b"
BASE_FULL = "65f575bd5c95c301eeec83ddffe764beebe25dda"
LOW = "a331c3cb1cfedc672bcf8b8adff91a11983e5647"
SERIES_LOW = "23a63d3"
WIDTH = 112

AUDIT = "verify/tools/wg942_append_audit.py"
SHIM = "docs/reports/W-G.9-99_乙之遞補鏈shim.md"

# ── 施工單 `§二 2-1` 之預測值（⛔ 非本檔現跑回填）──────────────────────────
EXP_S1 = (75, 52, 52, 23, 8, 60, 0)
EXP_S2 = (262, 20, 17, 99)
EXP_S3 = 12
EXP_S3_TOP = [(SHIM, 5),
              ("docs/reports/W-G.9波_新session交接文_WG913-WG931.md", 4),
              ("docs/design/W-G.9-30_∥SIDELINE界線之接線設計.md", 2)]
EXP_S4 = (0, 3)
EXP_S6 = [("02964ba", 1, 1, 0), ("3103ab5", 2, 1, 1), ("dea0ba3", 3, 2, 1),
          ("84bb7a6", 0, 0, 0), ("d488970", 3, 2, 1), ("b0d0db8", 3, 2, 1),
          ("65f575b", 3, 2, 1)]
EXP_S6_GAP = 5
EXP_S8 = (False, 5)
EXP_BAD_INC = 2

LAND_QUOTED = "ΣΔ ＝ +1.0300／池增量 84.0800 ㎡／R1 ΣΔ ＝ +0.000000"

L, STOPS, SKIPPED = [], [], []


def P(s=""):
    print(s)
    L.append(s)


def hdr(s):
    P("")
    P("=" * WIDTH)
    P(s)
    P("=" * WIDTH)


def stop(tag, text):
    STOPS.append((tag, text))
    P("  🛑 **停機 %s**：%s" % (tag, text))


def skipped(tag, text):
    SKIPPED.append((tag, text))
    P("  ⚠️ **略過 %s**：%s（⛔ 不計為證據·亦⛔ 不計為反證）" % (tag, text))


def M(ok):
    return "✅" if ok else "🛑"


def git(args, quotepath=False):
    """🔒 一切 `git` 呼叫明綁 `core.quotepath`（`S-4` 之受詞刻意取二框）。"""
    pre = ["git", "-C", REPO, "-c", "core.quotepath=%s" % ("true" if quotepath else "false")]
    return subprocess.run(pre + args, stdout=subprocess.PIPE,
                          check=True).stdout.decode("utf-8")


def load_targets():
    """🔒 自 `blob@BASE_FULL` 以 `ast` 解析（⛔ 不 import 工作區之模組）。"""
    src = git(["show", "%s:%s" % (BASE_FULL, AUDIT)])
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(
                getattr(t, "id", None) == "TARGETS" for t in node.targets):
            return ast.literal_eval(node.value)
    raise RuntimeError("🔴 `TARGETS` 於 blob@%s 未找到 ⇒ ⛔ 禁靜默兜底" % BASE_REF)


def md_modified(commit, quotepath=False):
    """該 commit 中狀態 `M` 且尾綴 `.md` 之路徑（⛔ 不含 `A`）。"""
    out = git(["show", "--no-renames", "--diff-filter=M", "--name-status",
               "--format=", commit], quotepath=quotepath)
    paths = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        if parts[1].endswith(".md"):
            paths.append(parts[1])
    return paths


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG9103_targetcov_%s.log" % BASE_REF)

    hdr("【W-G.9-101】純追加稽核器之受詞母體缺口（⛔ 零生產碼·⛔ 零管線·態 ＝ blob@%s）" % BASE_REF)
    P("  基座（一切量之態）＝ **%s**（⛔ 本檔不印任何隨 `HEAD` 而變之值 ⇒ 補登前後輸出逐位相同）" % BASE_FULL)
    P("  `app.py` blob@基座 ＝ %s" % git(["rev-parse", "%s:app.py" % BASE_FULL]).strip())
    P("  🔒 `TARGETS` 自 **blob@%s** 以 `ast` 解析（⛔ 不自工作區 import·`VR-058 三` 自我適用）。" % BASE_REF)
    P("  🔒 一切 `git` 呼叫明綁 `-c core.quotepath=false`（`S-4` 之受詞刻意取二框對照）。")
    P("  🔒 預測值出處 ＝ 施工單 `W-G.9-101` `§二 2-1`（⛔ 非本檔現跑回填）。")

    T = load_targets()
    files = [x for x in T if x[1] == "檔"]
    segs = [x for x in T if x[1] != "檔"]
    fp = [x[0] for x in files]
    sp = [x[0] for x in segs]
    COVER = set(fp) | set(sp)

    # ── §一　`S-1` ─────────────────────────────────────────────────────────
    hdr("【§一】`S-1`：`TARGETS` 結構（態 ＝ blob@%s）" % BASE_REF)
    got1 = (len(T), len(files), len(set(fp)), len(segs), len(set(sp)), len(COVER),
            len(fp) - len(set(fp)))
    ok1 = (got1 == EXP_S1)
    P("  %s 項數 ＝ **%d**（單 %d）｜檔級 ＝ **%d**（相異 %d·單 %d/%d）｜"
      "段級 ＝ **%d**（相異檔 %d·單 %d/%d）"
      % (M(ok1), got1[0], EXP_S1[0], got1[1], got1[2], EXP_S1[1], EXP_S1[2],
         got1[3], got1[4], EXP_S1[3], EXP_S1[4]))
    P("        **涵蓋相異檔 ＝ %d**（單 %d）｜檔級重複登錄 ＝ %d（單 %d）｜`kind` 值集 ＝ %s"
      % (got1[5], EXP_S1[5], got1[6], EXP_S1[6], sorted({x[1] for x in T})))

    # ── §二　`S-2`／`S-3`／`S-5` ───────────────────────────────────────────
    hdr("【§二】`S-2`：受詞缺口（母體 ＝ commit 區間 `%s..%s`）" % (LOW[:7], BASE_REF))
    commits = git(["rev-list", "--reverse", "%s..%s" % (LOW, BASE_FULL)]).splitlines()
    inst = gap = 0
    gap_commits = set()
    gap_files = collections.Counter()
    for c in commits:
        for p in md_modified(c):
            inst += 1
            if p not in COVER:
                gap += 1
                gap_commits.add(c)
                gap_files[p] += 1
    got2 = (inst, gap, len(gap_commits), len(commits))
    ok2 = (got2 == EXP_S2)
    P("  %s commit 數 ＝ **%d**（單 %d）｜被修改之 `.md` 實例 ＝ **%d**（單 %d）｜"
      "⛔ 不在涵蓋內 ＝ **%d**（單 %d·**%.1f%%**）｜含缺口之 commit ＝ **%d / %d**（單 %d）"
      % (M(ok2), got2[3], EXP_S2[3], got2[0], EXP_S2[0], got2[1], EXP_S2[1],
         100.0 * gap / inst, got2[2], got2[3], EXP_S2[2]))
    ok3 = (len(gap_files) == EXP_S3)
    P("  %s `S-3` 相異缺口檔 ＝ **%d**（單 %d）｜框 ＝ **該檔出現於幾個 commit**（⛔ 非出現次數）"
      % (M(ok3), len(gap_files), EXP_S3))
    P("        %-70s %s" % ("檔", "commit 數"))
    for p, n in sorted(gap_files.items(), key=lambda kv: (-kv[1], kv[0])):
        P("        %-70s %d" % (p, n))
    P("        POPULATION=%d PRINTED=%d SUPPRESSED=0  # 缺口檔（全列）"
      % (len(gap_files), len(gap_files)))
    for p, n in EXP_S3_TOP:
        ok3 = ok3 and (gap_files.get(p) == n)
    P("  %s 前三名逐檔對拍（單 %s）" % (M(ok3), [(x[0].split("/")[-1], x[1]) for x in EXP_S3_TOP]))
    ones = sum(1 for n in gap_files.values() if n == 1)
    P("        其餘 **%d** 檔各 `1`（單 `9`）%s" % (ones, M(ones == 9)))

    empty = (gap == 0)
    P("  %s `S-5` 否證通道：布林「缺口集為空」＝ **%s**（單 `False`）" % (M(not empty), empty))
    if empty:
        stop("⑤", "`S-5` 之布林為 `True` ⇒ 本單受詞不成立 ⇒ 上呈發單側")
    if not (ok1 and ok2 and ok3):
        stop("④", "`S-1`／`S-2`／`S-3` 有與預測不符者 ⇒ ⛔ 不得改樣式去湊（家法 `6`）")

    # ── §三　`S-4`（`core.quotepath` 二框）────────────────────────────────
    hdr("【§三】🔒 `S-4` 判別力對照：`core.quotepath` 二框（受詞 ＝ blob@%s 之 `M(.md)` 計數）"
        % BASE_REF)
    got4 = []
    for qp in (True, False):
        raw = git(["show", "--no-renames", "--diff-filter=M", "--name-status",
                   "--format=", BASE_FULL], quotepath=qp).splitlines()
        n = len(md_modified(BASE_FULL, quotepath=qp))
        got4.append(n)
        P("  `quotepath=%-5s` ⇒ `M(.md)` ＝ **%d**" % (str(qp).lower(), n))
        P("        逐字樣本（首列）＝ %r" % (raw[0] if raw else None))
    ok4 = (tuple(got4) == EXP_S4)
    pert = abs(got4[1] - got4[0])
    P("  %s 二框 ＝ %s（單 %s）｜**擾動量 ＝ %d**（單 `3`）⇒ %s"
      % (M(ok4), tuple(got4), EXP_S4, pert,
         "該對照⛔ 未退化（家法 `9`）" if pert > 0 else "**已退化**"))
    P("  🔒 **後果之形**：母體歸零 ⇒ 迴圈零次 ⇒ `bad` 停留初值 ⇒ **閘恆綠**（`VR-059 三`）。")
    if pert == 0:
        skipped("⑥", "`S-4` 之擾動量 ＝ 0（對照退化）")

    # ── §四　`S-6`（本系列逐 commit）──────────────────────────────────────
    hdr("【§四】`S-6`：本系列逐 commit（`%s..%s`·格式 `M(.md)/in/gap`）" % (SERIES_LOW, BASE_REF))
    ser = git(["rev-list", "--reverse", "%s..%s" % (SERIES_LOW, BASE_FULL)]).splitlines()
    got6 = []
    tot_gap = 0
    all_shim = True
    P("  %-10s %-8s %-8s %-8s %s" % ("commit", "M(.md)", "in", "gap", "gap 之檔"))
    for c in ser:
        md = md_modified(c)
        ins = [p for p in md if p in COVER]
        gp = [p for p in md if p not in COVER]
        tot_gap += len(gp)
        if gp and any(p != SHIM for p in gp):
            all_shim = False
        got6.append((c[:7], len(md), len(ins), len(gp)))
        P("  %-10s %-8d %-8d %-8d %s" % (c[:7], len(md), len(ins), len(gp),
                                          [p.split("/")[-1] for p in gp]))
    ok6 = (got6 == EXP_S6 and tot_gap == EXP_S6_GAP and all_shim)
    P("  %s 逐 commit 與預測相同 ＝ %s｜缺口實例合計 ＝ **%d**（單 %d）｜"
      "`gap` 逐 commit 皆恰為 `shim.md` ＝ **%s**"
      % (M(ok6), got6 == EXP_S6, tot_gap, EXP_S6_GAP, all_shim))
    if not ok6:
        stop("④", "`S-6` 與預測不符（逐格見上）")

    # ── §五　`S-7`（機制歸因·引被檢物逐字）────────────────────────────────
    hdr("【§五】🔒 `S-7`：機制歸因（**引被檢物實作逐字**·⛔ 非數值吻合·家法 `12`）")
    aud = git(["show", "%s:%s" % (BASE_FULL, AUDIT)]).splitlines()
    loop_ind = len(aud[484]) - len(aud[484].lstrip())
    P("  `%s:485@%s` 逐字 ＝" % (AUDIT, BASE_REF))
    P("     %r  （縮排 %d）" % (aud[484], loop_ind))
    P("  `%s:524@%s` 逐字（結論列）＝" % (AUDIT, BASE_REF))
    P("     %r" % aud[523])
    P("  ⇒ **迴圈之母體即 `TARGETS`** ⇒ 未列者**永不到訪** ⇒ `bad` ⛔ 不可能因之遞增。")
    P("")
    P("  🔒 **反例搜尋**（`bad` 之全站點·母體 ＝ blob@%s）：" % BASE_REF)
    inc = 0
    outside = 0
    P("     %-8s %-8s %s" % ("列", "縮排", "逐字"))
    for i, l in enumerate(aud, 1):
        if "bad" not in l:
            continue
        ind = len(l) - len(l.lstrip())
        kind = ""
        if "bad += 1" in l:
            inc += 1
            inside = (i > 485 and ind > loop_ind)
            if not inside:
                outside += 1
            kind = "遞增·%s" % ("迴圈**內**" if inside else "🔴 迴圈**外**")
        elif "bad = 0" in l:
            kind = "初始化·迴圈**外**"
        else:
            kind = "讀取"
        P("     :%-7d %-8d %s   ⇒ %s" % (i, ind, l.strip()[:70], kind))
    ok7 = (inc == EXP_BAD_INC and outside == 0)
    P("  %s ⇒ **遞增站點恰 %d**（單 %d）、**無一在迴圈外**（迴圈外遞增 ＝ %d）⇒ **反例 ＝ 0**"
      % (M(ok7), inc, EXP_BAD_INC, outside))
    if not ok7:
        stop("④", "`S-7` 之反例搜尋與預測不符")

    # ── §六　`S-8`（具名之單一受詞）───────────────────────────────────────
    hdr("【§六】`S-8`：具名之單一受詞 `%s`" % SHIM.split("/")[-1])
    in_cover = SHIM in COVER
    n_ser = sum(1 for c in ser if SHIM in md_modified(c))
    ok8 = ((in_cover, n_ser) == EXP_S8)
    P("  %s `shim.md` ∈ 涵蓋 ＝ **%s**（單 %s）｜其於本系列被修改之 commit 數 ＝ **%d**（單 %d）"
      % (M(ok8), in_cover, EXP_S8[0], n_ser, EXP_S8[1]))
    P("  判別力對照：已在 `TARGETS` 之任一檔級項 ∈ 涵蓋 ＝ %s（應 `True`）" % (fp[0] in COVER))
    if not ok8:
        stop("④", "`S-8` 與預測不符")

    # ── §七　土地三數（**未重算之轉述**）──────────────────────────────────
    hdr("【§七】🔒 土地三數 ＝ **未重算之轉述**")
    P("  %s" % LAND_QUOTED)
    P("  🔒 本檔**零管線** ⇒ 上三數⛔ **未重算**；池增量係**依守恆式導出·⛔ 非幾何實量**（`VR-054 三`）。")

    return finish(log_path)


def finish(log_path):
    hdr("【§八】收工：停機逐字")
    if SKIPPED:
        P("  ⚠️ **本批之略過（對照退化）**：")
        for t_, x in SKIPPED:
            P("     略過 %s：%s" % (t_, x))
    if STOPS:
        P("  🛑 **本批之停機（逐字具名·`rc` 恆 `0`）**：")
        for t_, x in STOPS:
            P("     停機 %s：%s" % (t_, x))
    else:
        P("  ✅ 本檔未觸任一停機條件。")
    os.makedirs(OUTDIR, exist_ok=True)
    with open(log_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("")
    print("log -> %s" % os.path.relpath(log_path, REPO).replace(os.sep, "/"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
