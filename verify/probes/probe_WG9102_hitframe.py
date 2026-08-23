# -*- coding: utf-8 -*-
r"""`W-G.9-99 補正⑤`：「命中」之**框**與**母體之態**須具名。

## 受詞（⛔ 非土地結論）

`補正④` `Q-6` 出艙「更正後：報告 `5`／登記表 `3`／自誤表 `4`」而⛔ 未標框名。
其 `4` 係 `str.count()`（**出現次數**）框；同表並列之「列號」欄係 `grep -c`（**命中列數**）框、僅 `3` 個
（`…claude.ai側自誤登記.md:2834` **一列含二次**）。

## 二框之定義（本檔逐格並列·⛔ 不擇一）

- **出現次數**（`str.count()`／逐次 `finditer`）：單列含 `N` 次即計 `N`。
- **命中列數**（`grep -c`）：每檔**每列至多計 `1`**。

## 🔒 母體之態 ＝ `blob@BASE_REF`（⛔ 非工作區）

如此本檔之預測值⛔ 不因附加而漂移（`VR-058 三` 之**自我適用**）。
`R-7` 另取**工作區**之態作對照，以坐實「態須具名」之必要性。

## 🔒 ⛔ 零管線

⛔ 不 `harvest()`、⛔ 不 `run_step_g`、⛔ 不 import 任何既有探針；
既有探針與 log **一律原樣**、⛔ 不改一字（`log` 係證據）。

## 預測值之出處（`fixture-provenance`）

`R-1`〜`R-7` 之期望值**逐項引自施工單** `W-G.9-99 補正⑤` `§一`（⛔ 非由本檔現跑一次回填）。

## 重跑

    python verify/probes/probe_WG9102_hitframe.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
log 落 `verify/out/probe_WG9102_hitframe_<基座短碼>.log`（檔名綁**基座**·考古節 `122`）。
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "b0d0db8"
WIDTH = 112

PAT = "`229` 列"
EVIDENCE_LOG = "verify/out/probe_WG9101_frame_d488970.log"
EVIDENCE_ROWS = (53, 56)
CANON_11 = ".claude/skills/failure-archaeology/SKILL.md:4368"

TARGETS = ["docs/reports/W-G.9-99_乙之遞補鏈shim.md",
           "docs/驗證裁定登記表.md",
           "docs/reports/W-G.9波_claude.ai側自誤登記.md"]

PROD_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/run_verification.py", "verify/wd4_tier_list.py",
              "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]

SELF = ["verify/probes/probe_WG9102_hitframe.py",
        "verify/out/probe_WG9102_hitframe_%s.log" % BASE_REF,
        "docs/reports/W-G.9-99_乙之遞補鏈shim.md（【五度更正】段）",
        "docs/驗證裁定登記表.md（`VR-058`）",
        "docs/reports/W-G.9波_claude.ai側自誤登記.md（自誤 `116`）"]

# ── 施工單 `§一` 之預測值（⛔ 非本檔現跑回填）──────────────────────────────
EXP_R1 = {"docs/reports/W-G.9-99_乙之遞補鏈shim.md": (5, 5),
          "docs/驗證裁定登記表.md": (3, 3),
          "docs/reports/W-G.9波_claude.ai側自誤登記.md": (4, 3)}
EXP_R2 = (12, 11, 1)
EXP_R3_LINES = [2819, 2828, 2834]
EXP_R3_TIMES = [1, 1, 2]
EXP_R7 = {"docs/reports/W-G.9-99_乙之遞補鏈shim.md": (7, 7),
          "docs/驗證裁定登記表.md": (3, 3),
          "docs/reports/W-G.9波_claude.ai側自誤登記.md": (5, 4)}

# 🔒 土地三數 ＝ **轉述**（`驗收 12`）；本檔零管線 ⇒ ⛔ 未重算。
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


def git(a):
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True, check=True).stdout


def git1(a):
    return git(a).decode("utf-8").strip()


def blob_text(path, ref=BASE_REF):
    return git(["show", "%s:%s" % (ref, path)]).decode("utf-8")


def wtree_text(path):
    with open(os.path.join(REPO, path.replace("/", os.sep)), "rb") as fh:
        return fh.read().decode("utf-8")


def two_frames(t):
    """🔒 二框並陳（⛔ 不擇一）：出現次數 ＝ `str.count()`；命中列數 ＝ `grep -c`。"""
    occ = t.count(PAT)
    rows = [(i, l.count(PAT)) for i, l in enumerate(t.splitlines(), 1) if PAT in l]
    return occ, len(rows), rows


def prod_hashes():
    return {f: git1(["hash-object", f]) for f in PROD_FILES}


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG9102_hitframe_%s.log" % BASE_REF)
    H_BEFORE = prod_hashes()

    hdr("【W-G.9-99 補正⑤】「命中」之框與母體之態（⛔ 零生產碼·⛔ **零管線**·母體 ＝ blob@%s）"
        % BASE_REF)
    P("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    P("  HEAD ＝ %s；`app.py` blob ＝ %s"
      % (git1(["rev-parse", "HEAD"]), git1(["rev-parse", "HEAD:app.py"])))
    P("  🔒 **樣式** ＝ 「%s」（逐字）" % PAT)
    P("  🔒 **二框之定義**：出現次數 ＝ `str.count()`（單列含 `N` 次即計 `N`）；"
      "命中列數 ＝ `grep -c`（每列至多計 `1`）。")
    P("  🔒 **母體之態 ＝ blob@%s**（⛔ 非工作區）⇒ `R-1`〜`R-6` 之值⛔ 不因附加而漂移。" % BASE_REF)
    P("  🔒 **預測值出處 ＝ 施工單 `W-G.9-99 補正⑤` `§一`**（⛔ 非本檔現跑回填）。")

    # ── §一　二框逐檔（`R-1`／`R-2`／`R-3`）────────────────────────────────
    hdr("【§一】二框逐檔（`R-1`）・合計（`R-2`）・框差之落點（`R-3`）")
    P("  %-46s %-18s %-18s %-6s %s"
      % ("檔（母體 ＝ blob@%s）" % BASE_REF, "出現次數(count)", "命中列數(grep -c)", "差", "命中列號"))
    tot_o = tot_l = 0
    ok1 = True
    detail = {}
    for p in TARGETS:
        t = blob_text(p)
        occ, nline, rows = two_frames(t)
        detail[p] = (occ, nline, rows)
        eo, el = EXP_R1[p]
        good = (occ == eo and nline == el)
        ok1 = ok1 and good
        tot_o += occ
        tot_l += nline
        P("  %s %-44s %-18s %-18s %-6d %s"
          % (M(good), p.split("/")[-1], "%d（單 %d）" % (occ, eo),
             "%d（單 %d）" % (nline, el), occ - nline, [r[0] for r in rows]))
    ok2 = ((tot_o, tot_l, tot_o - tot_l) == EXP_R2)
    P("  %s `R-2` 合計：出現次數 ＝ **%d**（單 %d）／命中列數 ＝ **%d**（單 %d）／差 ＝ **%d**（單 %d）"
      % (M(ok2), tot_o, EXP_R2[0], tot_l, EXP_R2[1], tot_o - tot_l, EXP_R2[2]))

    zp = TARGETS[2]
    rows = detail[zp][2]
    got_lines = [r[0] for r in rows]
    got_times = [r[1] for r in rows]
    ok3 = (got_lines == EXP_R3_LINES and got_times == EXP_R3_TIMES)
    P("  %s `R-3` 框差之落點（`%s`）：" % (M(ok3), zp.split("/")[-1]))
    P("        命中列號 ＝ %s（單 %s）" % (got_lines, EXP_R3_LINES))
    P("        逐列出現次數 ＝ %s（單 %s）" % (got_times, EXP_R3_TIMES))
    for i, n in rows:
        if n >= 2:
            P("        🔒 差 `%d` 之來源 ＝ `:%d`（**單列含 %d 次**·逐字如下）" % (n - 1, i, n))
            P("           %s" % blob_text(zp).splitlines()[i - 1].strip()[:170])
    if not (ok1 and ok2 and ok3):
        stop("③", "`R-1`／`R-2`／`R-3` 有與預測不符者 ⇒ ⛔ 不得改樣式去湊（家法 `6`）")

    # ── §二　判別力對照 ＋ 否證通道（`R-4`／`R-5`）─────────────────────────
    hdr("【§二】🔒 判別力對照（`R-4`）與**否證通道**（`R-5`）")
    diffs = [detail[p][0] - detail[p][1] for p in TARGETS]
    pert = max(diffs)
    P("  %-46s %s" % ("檔", "二框差"))
    for p, d in zip(TARGETS, diffs):
        P("  %-46s %d" % (p.split("/")[-1], d))
    P("  🔒 **擾動量 ＝ %d**（單 `1`）%s ⇒ 該對照%s"
      % (pert, M(pert == 1), "⛔ 未退化（家法 `9`）" if pert > 0 else "**已退化**"))
    if pert == 0:
        skipped("⑤", "`R-4` 之擾動量 ＝ 0（對照退化）")
    all_zero = all(d == 0 for d in diffs)
    P("  %s `R-5` 否證通道：布林「三檔二框差**皆** `0`」＝ **%s**（單 `False`）"
      % (M(not all_zero), all_zero))
    P("     ⇒ 若為 `True`，則二框無別、本單受詞不成立。")
    if all_zero:
        stop("④", "`R-5` 之布林為 `True` ⇒ 本單受詞不成立 ⇒ 上呈發單側")
    P("  ⇒ 併得一則**否證**：以「某二檔之二框相同」推論「框無所謂」係⛔ 無效——須逐檔具名。")

    # ── §三　log 之異框表（`R-6`·⛔ 不改一字）──────────────────────────────
    hdr("【§三】`R-6`：既有 log 之**異框並列**表（⛔ 不改一字·log 係證據）")
    lg = blob_text(EVIDENCE_LOG).splitlines()
    a, b = EVIDENCE_ROWS
    P("  `【倉】` `%s:%d`–`:%d` 逐字：" % (EVIDENCE_LOG, a, b))
    for i in range(a, b + 1):
        P("     %d| %s" % (i, lg[i - 1]))
    P("  🔒 **就地具名（⛔ 不改 log 一字）**：")
    P("     「更正後(工作區)」欄 ＝ **出現次數**框（`str.count()`）；"
      "「列號(工作區)」欄 ＝ **命中列數**框（`grep -c`）。")
    P("     ⇒ 自誤表該列遂呈 `4` 與 `3` 個列號並列；該 log 之 `Q-1`〜`Q-5`／`Q-7` ⛔ 不受影響。")
    P("  🔒 形之歸屬：`常設第 11 條`（`【倉】` `%s`：修法之射程只及於寫下它時手上那個動作）"
      % CANON_11)
    P("     ——`VR-057 一`（採他框須標框名）係**同一張施工單**所立而未帶到同單下一格。")

    # ── §四　態之對照（`R-7`）─────────────────────────────────────────────
    hdr("【§四】`R-7`：**態**之對照（blob@%s vs 工作區）⇒ 坐實「態須具名」" % BASE_REF)
    P("  %-46s %-22s %-22s %s"
      % ("檔", "blob@%s（R-1）" % BASE_REF, "工作區（R-7）", "相異"))
    ok7 = True
    ident = True
    for p in TARGETS:
        bo, bl = detail[p][0], detail[p][1]
        wo, wl, _r = two_frames(wtree_text(p))
        eo, el = EXP_R7[p]
        good = (wo == eo and wl == el)
        ok7 = ok7 and good
        if (wo, wl) != (bo, bl):
            ident = False
        P("  %s %-44s %-22s %-22s %s"
          % (M(good), p.split("/")[-1], "%d／%d" % (bo, bl),
             "%d／%d（單 %d／%d）" % (wo, wl, eo, el), (wo, wl) != (bo, bl)))
    P("  %s `R-7` 與 `R-1` **全等** ＝ **%s**（單 `False`）" % (M(not ident), ident))
    if ident:
        stop("⑥", "`R-7` 與 `R-1` 全等 ⇒ 態之區辨無判別力 ⇒ 上呈發單側")
    if not ok7:
        P("  ⚠️ 工作區之值與 `R-7` 預測不符——若本檔**於附加前**執行則屬預期；"
          "本批之定案態係**附加後**（見 `驗收 4`）。")
    P("  ⇒ 出艙命中數時須同時具名母體之態：`blob@<commit>`（可複現）抑或**工作區**（隨附加而變）。")

    # ── §五　土地三數（`驗收 12`·**未重算之轉述**）─────────────────────────
    hdr("【§五】🔒 土地三數 ＝ **未重算之轉述**（`驗收 12`）")
    P("  %s" % LAND_QUOTED)
    P("  🔒 本檔**零管線** ⇒ 上三數⛔ **未重算**，係自 `補正②`／`補正③` 之**轉述**；"
      "其來源檔於本批 `numstat` **零觸**。")
    P("  🔒 出艙稱謂（`VR-054 三`）：池增量 `84.0800 ㎡` 係**依守恆式導出·⛔ 非幾何實量**。")

    return finish(log_path, H_BEFORE)


def finish(log_path, H_BEFORE):
    hdr("【§六】收工：生產檔 hash 前後對拍・`SELF` 自扣・停機逐字")
    H_AFTER = prod_hashes()
    same = [f for f in PROD_FILES if H_BEFORE.get(f) == H_AFTER.get(f)]
    P("  10 支生產檔 `git hash-object` 出艙前後**逐位相同** ＝ **%d／%d** ⇒ %s"
      % (len(same), len(PROD_FILES),
         "✅ 零生產碼變更" if len(same) == len(PROD_FILES) else "🔴"))
    for f in PROD_FILES:
        P("     %-34s %s %s" % (f, H_BEFORE.get(f),
                                "✅" if H_BEFORE.get(f) == H_AFTER.get(f)
                                else "🔴 → %s" % H_AFTER.get(f)))
    if len(same) != len(PROD_FILES):
        stop("①", "生產檔 hash 前後不同 ⇒ 「零生產碼」宣稱**不成立**")
    P("")
    P("  🔒 **`SELF` 自扣**：本批產物 ＝ **%d** 檔／段：" % len(SELF))
    for s in SELF:
        P("     `%s`" % s)
    P("     ⇒ 本檔之母體 ＝ blob@%s 之**三受詞文件**（⛔ 非檔案母體·⛔ 非工作區）；"
      "工作區之態另列於 `R-7`。" % BASE_REF)
    P("  🔒 **⛔ 零管線**：本檔未 `harvest()`／未 `run_step_g`／未 import 任何既有探針。")
    P("  🔒 **⛔ 未改既有探針或 log 一字**：`%s` 僅被**讀取**（`git show`）。" % EVIDENCE_LOG)
    P("")
    if SKIPPED:
        P("  ⚠️ **本批之略過（對照退化·⛔ 不計為證據亦不計為反證）**：")
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
