# -*- coding: utf-8 -*-
r"""`W-G.9-99 補正④`：列數之**量測框**與**扣法受詞**——`229` ⇒ `228`。

## 受詞（⛔ 非土地結論）

`補正③ v2` `§零 A0-8` 寫「扣掉含 `HEAD ＝` 之列後：`229` 列／`sha256 = ee214ab6…c43112`」——
其 `sha256` 量自**已扣**之字串、`229` 量自**未扣**之字串 ⇒ **同句前後半受詞不同**。
扣後之**正典框**（`splitlines()`·`SKILL.md:4696` `W2`）值 ＝ **`228`**。

## 🔒 本檔⛔ 不跑管線

⛔ 不 `harvest()`、⛔ 不 `run_step_g`、⛔ 不 `import` 任何既有探針；
一切量皆自 **git blob** 讀取（基座 `BASE_REF`）或自**工作區**讀取，並逐格具名其來源。

## 「`229`」之二來源（本檔之核心）

`229` 可由二條路徑得出：**原態之 `splitlines()`** 與 **扣後之 `split("\n")` 段數**。
前者少扣一列、後者多算一個尾隨空段，二者恰**互抵** ⇒ 該數⛔ 不具分辨力。

## 預測值之出處（`fixture-provenance`）

`Q-1`〜`Q-7` 之期望值**逐項引自施工單** `W-G.9-99 補正④` `§一`
（⛔ 非由本檔現跑一次回填）。停機③〜⑥ 亦逐字引自該單。

## 重跑

    python verify/probes/probe_WG9101_frame.py

`rc` **恆 `0`**；停機以**逐字具名**表示。
log 落 `verify/out/probe_WG9101_frame_<基座短碼>.log`（檔名綁**基座**·考古節 `122`）。
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "d488970"
WIDTH = 112

LOG_PATH_REL = "verify/out/probe_WG999c_true_chain_3103ab5.log"
DROP_MARK = "HEAD ＝"
CANON_ANCHOR = ".claude/skills/failure-archaeology/SKILL.md"

TARGETS = ["docs/reports/W-G.9-99_乙之遞補鏈shim.md",
           "docs/驗證裁定登記表.md",
           "docs/reports/W-G.9波_claude.ai側自誤登記.md"]

PROD_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/run_verification.py", "verify/wd4_tier_list.py",
              "verify/wf_f0.py", "verify/wf_f1.py", "verify/wf_f2.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]

SELF = ["verify/probes/probe_WG9101_frame.py",
        "verify/out/probe_WG9101_frame_%s.log" % BASE_REF,
        "docs/reports/W-G.9-99_乙之遞補鏈shim.md（【四度更正】段）",
        "docs/驗證裁定登記表.md（`VR-057`）",
        "docs/reports/W-G.9波_claude.ai側自誤登記.md（自誤 `115`）"]

# ── 施工單 `§一` 之預測值（⛔ 非本檔現跑回填）──────────────────────────────
EXP_RAW = {"splitlines": 229, "count_nl": 229, "split_seg": 230, "bytes": 18109,
           "sha256": "5de85394a87c78ce080024299cc958ebbb8567a2dcc57b1f465a3d9b667c2d28"}
EXP_CUT = {"splitlines": 228, "count_nl": 228, "split_seg": 229, "bytes": 17996,
           "sha256": "ee214ab64fca45ca6ca834a27cf4f3826f39468e3f5f4a50f91ed6c122c43112"}
EXP_APP = {"last": ")", "splitlines": 22160, "count_nl": 22159, "bytes": 1307679,
           "blob": "a9e5671d64d254907a0396f898f046d9d85e8283"}
EXP_SPOT_BEFORE = {"docs/reports/W-G.9-99_乙之遞補鏈shim.md": 1,
                   "docs/驗證裁定登記表.md": 1,
                   "docs/reports/W-G.9波_claude.ai側自誤登記.md": 1}
EXP_SPOT_AFTER = {"docs/reports/W-G.9-99_乙之遞補鏈shim.md": 5,
                  "docs/驗證裁定登記表.md": 3,
                  "docs/reports/W-G.9波_claude.ai側自誤登記.md": 4}
EXP_BARE_FILES = 2
EXP_BARE_FAKE = "docs/reports/W-G.9-69_重烤與乙式耦合斷言.md"
EXP_BARE_TRUE = "docs/reports/W-G.9-100_CC交接文.md"
SPOT_PAT = "`229` 列"
BARE_PAT = "22159"

# 🔒 土地三數 ＝ **未重算之轉述**（`驗收 12`）；本檔⛔ 零管線故⛔ 不重算。
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


def blob(ref, path):
    return git(["show", "%s:%s" % (ref, path)])


def wtree(path):
    with open(os.path.join(REPO, path.replace("/", os.sep)), "rb") as fh:
        return fh.read()


def four(b):
    """🔒 四數並陳（⛔ 不擇一）：`splitlines()`／`count(NL)`／`split(NL)` 段數／`bytes`。"""
    t = b.decode("utf-8")
    return {"splitlines": len(t.splitlines()), "count_nl": t.count("\n"),
            "split_seg": len(t.split("\n")), "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest()}


def show(tag, got, exp):
    ok = all(got[k] == exp[k] for k in exp)
    P("  %s %-8s splitlines=%-6d %s ｜ count(NL)=%-6d %s ｜ split 段數=%-6d %s ｜ bytes=%-8d %s"
      % (M(ok), tag, got["splitlines"], M(got["splitlines"] == exp["splitlines"]),
         got["count_nl"], M(got["count_nl"] == exp["count_nl"]),
         got["split_seg"], M(got["split_seg"] == exp["split_seg"]),
         got["bytes"], M(got["bytes"] == exp["bytes"])))
    P("           sha256 ＝ %s %s" % (got["sha256"], M(got["sha256"] == exp["sha256"])))
    return ok


def prod_hashes():
    return {f: git1(["hash-object", f]) for f in PROD_FILES}


def main():                                                          # noqa: C901
    log_path = os.path.join(OUTDIR, "probe_WG9101_frame_%s.log" % BASE_REF)
    H_BEFORE = prod_hashes()

    hdr("【W-G.9-99 補正④】列數之量測框與扣法受詞（⛔ 零生產碼·⛔ **零管線**·純檔級量測）")
    P("  基座（log 檔名所綁）＝ **%s**" % BASE_REF)
    P("  HEAD ＝ %s；`app.py` blob ＝ %s"
      % (git1(["rev-parse", "HEAD"]), git1(["rev-parse", "HEAD:app.py"])))
    P("  🔒 **資料源 ＝ git blob（基座 `%s`）＋ 工作區**，逐格具名其來源；"
      "⛔ 未跑管線、⛔ 未 import 任何既有探針。" % BASE_REF)
    P("  🔒 **預測值出處 ＝ 施工單 `W-G.9-99 補正④` `§一`**（⛔ 非本檔現跑回填）。")
    P("  🔒 **扣法（逐字·施工單 `A0-8`）**："
      "`\"\\n\".join(l for l in t.split(\"\\n\") if \"%s\" not in l)`" % DROP_MARK)

    # ── §一　log 之原態與扣後（`Q-1`／`Q-2`）──────────────────────────────
    hdr("【§一】`%s` 之原態與扣後（`Q-1`／`Q-2`·來源 ＝ blob@%s）"
        % (LOG_PATH_REL.split("/")[-1], BASE_REF))
    lb = blob(BASE_REF, LOG_PATH_REL)
    t = lb.decode("utf-8")
    raw = four(lb)
    ok1 = show("`Q-1` 原態", raw, EXP_RAW)
    cut_txt = "\n".join(l for l in t.split("\n") if DROP_MARK not in l)
    cut = four(cut_txt.encode("utf-8"))
    ok2 = show("`Q-2` 扣後", cut, EXP_CUT)
    ndrop = raw["split_seg"] - cut["split_seg"]
    P("  被扣列數 ＝ %d（含 `%s` 之列）" % (ndrop, DROP_MARK))
    if not (ok1 and ok2):
        stop("③", "`Q-1`／`Q-2` 有與預測不符之數 ⇒ ⛔ 不得自行改扣法去湊（家法 `6`）")

    # ── §二　互抵之直檢（`Q-3`）───────────────────────────────────────────
    hdr("【§二】🔒 「`229`」之**二來源**與其互抵——直檢（`Q-3`）")
    same = (cut["split_seg"] == raw["splitlines"])
    P("  路徑甲：**原態**之 `splitlines()`      ＝ **%d**" % raw["splitlines"])
    P("  路徑乙：**扣後**之 `split(NL)` 段數    ＝ **%d**" % cut["split_seg"])
    P("  %s 布林「扣後 `split(NL)` 段數 == 原態 `splitlines()`」＝ **%s**（預測 `True`）"
      % (M(same), same))
    P("  🔒 **機制**：路徑甲**少扣一列**（+1）、路徑乙**多算一個尾隨空段**（+1），二者恰互抵。")
    P("  ⇒ 「`229`」⛔ **不具分辨力**：無法區別「扣了沒扣」與「用哪個框」。")
    P("  ⛔ **會使本判為否之輸入**：該 log 之末字元非換行（則路徑乙不會多算空段）。")
    P("     實測末字元 ＝ %r ⇒ 該否證條件**不成立**" % t[-1])
    if not same:
        stop("④", "`Q-3` 之布林為 `False` ⇒ 互抵之歸因不成立 ⇒ 上呈發單側")

    # ── §三　`app.py` 二框（`Q-4`）────────────────────────────────────────
    hdr("【§三】`app.py` 之二框（`Q-4`·來源 ＝ blob@%s）" % BASE_REF)
    ab = blob(BASE_REF, "app.py")
    at = ab.decode("utf-8")
    g4 = {"last": at[-1], "splitlines": len(at.splitlines()),
          "count_nl": at.count("\n"), "bytes": len(ab),
          "blob": git1(["rev-parse", "%s:app.py" % BASE_REF])}
    ok4 = all(g4[k] == EXP_APP[k] for k in EXP_APP)
    P("  %s 末字元 ＝ %r %s ｜ `splitlines()` ＝ **%d** %s ｜ `count(NL)` ＝ **%d** %s ｜ bytes ＝ %d %s"
      % (M(ok4), g4["last"], M(g4["last"] == EXP_APP["last"]),
         g4["splitlines"], M(g4["splitlines"] == EXP_APP["splitlines"]),
         g4["count_nl"], M(g4["count_nl"] == EXP_APP["count_nl"]),
         g4["bytes"], M(g4["bytes"] == EXP_APP["bytes"])))
    P("     blob ＝ %s %s" % (g4["blob"], M(g4["blob"] == EXP_APP["blob"])))
    P("  🔒 正典框（`%s:4696` `W2`：正典行數 ＝ `splitlines()`）⇒ **正值 ＝ %d**；"
      "`22159` 係 `count(NL)`／`wc -l` 框。" % (CANON_ANCHOR, g4["splitlines"]))
    P("  ⇒ `bytes` 與 blob 逐位相符 ⇒ ⛔ **非內容不符**、⛔ 非錯，僅**框未具名**。")
    if not ok4:
        stop("③", "`Q-4` 有與預測不符之數")

    # ── §四　判別力對照：尾隨換行之有無（`Q-5`）───────────────────────────
    hdr("【§四】🔒 判別力對照：**尾隨換行之有無**（`Q-5`·來源 ＝ blob@%s）" % BASE_REF)
    P("  %-46s %-8s %-14s %-14s %s" % ("檔", "末字元", "splitlines()", "count(NL)", "二框差"))
    diffs = []
    for p in TARGETS + ["app.py"]:
        b = blob(BASE_REF, p)
        s = b.decode("utf-8")
        d = len(s.splitlines()) - s.count("\n")
        diffs.append(d)
        P("  %-46s %-8r %-14d %-14d %d"
          % (p.split("/")[-1], s[-1], len(s.splitlines()), s.count("\n"), d))
    pert = max(diffs)
    P("  🔒 **擾動量 ＝ %d 列**（三受詞文件各 %s；`app.py` %d）"
      % (pert, "／".join(str(x) for x in diffs[:3]), diffs[3]))
    ok5 = (diffs[:3] == [0, 0, 0] and diffs[3] == 1)
    P("  %s 預測：三受詞文件各 `0`、`app.py` `1` ⇒ 擾動量 `1` > `0`（對照⛔ 未退化）" % M(ok5))
    if pert == 0:
        skipped("⑤", "`Q-5` 之擾動量 ＝ 0（對照退化）")

    # ── §五　落點掃描（`Q-6`）─────────────────────────────────────────────
    hdr("【§五】就地更正之落點掃描（`Q-6`·樣式 「%s」）" % SPOT_PAT)
    P("  %-46s %-14s %-14s %s" % ("檔", "更正前(blob)", "更正後(工作區)", "列號(工作區)"))
    before, after = {}, {}
    for p in TARGETS:
        bb = blob(BASE_REF, p).decode("utf-8")
        wt = wtree(p).decode("utf-8")
        before[p] = bb.count(SPOT_PAT)
        after[p] = wt.count(SPOT_PAT)
        ln = [i for i, l in enumerate(wt.splitlines(), 1) if SPOT_PAT in l]
        P("  %-46s %-14d %-14d %s" % (p.split("/")[-1], before[p], after[p], ln))
    sb, sa = sum(before.values()), sum(after.values())
    ok6b = (before == EXP_SPOT_BEFORE)
    hit_after = "更正後" if after == EXP_SPOT_AFTER else (
        "更正前（工作區尚未附加）" if after == EXP_SPOT_BEFORE else "🛑 二預測皆不符")
    P("  %s 更正前合計 ＝ %d（預測 %d）" % (M(ok6b), sb, sum(EXP_SPOT_BEFORE.values())))
    P("  %s 更正後合計 ＝ %d（預測 %d）；工作區之態 ＝ **%s**"
      % (M(after == EXP_SPOT_AFTER), sa, sum(EXP_SPOT_AFTER.values()), hit_after))
    if not ok6b:
        stop("③", "`Q-6` 更正前之落點數與預測不符")

    # ── §六　裸數字掃描之分層（`Q-7`）─────────────────────────────────────
    hdr("【§六】🔒 裸數字掃描**須分層**（`Q-7`·`%s` 於 `docs/`·來源 ＝ blob@%s）"
        % (BARE_PAT, BASE_REF))
    names = git(["-c", "core.quotePath=false", "ls-tree", "-r", "--name-only",
                 BASE_REF, "docs/"]).decode("utf-8").split("\n")
    names = [n for n in names if n.strip()]
    hits = []
    for f in names:
        try:
            s = blob(BASE_REF, f).decode("utf-8")
        except UnicodeDecodeError:
            continue
        for i, l in enumerate(s.splitlines(), 1):
            if BARE_PAT in l:
                hits.append((f, i, l.strip()))
    nf = len({h[0] for h in hits})
    P("  `docs/` 母體 ＝ **%d** 檔；裸命中 ＝ **%d** 列／**%d** 檔（預測 %d 檔）%s"
      % (len(names), len(hits), nf, EXP_BARE_FILES, M(nf == EXP_BARE_FILES)))
    P("  🔒 **逐字上下文（停機⑥ 之硬要求·⛔ 不得僅以命中數下判）**：")
    fake = real = 0
    for f, i, l in hits:
        kind = "🩸 偽命中（hex 值之子字串·⛔ 非列數）" if f == EXP_BARE_FAKE else "✅ 真命中（列數）"
        if f == EXP_BARE_FAKE:
            fake += 1
        else:
            real += 1
        P("     %s:%d　%s" % (f, i, kind))
        P("        逐字：%s" % l[:180])
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # 裸命中（全列）" % (len(hits), len(hits)))
    ok7 = (nf == EXP_BARE_FILES and fake == 1 and real == 1
           and any(h[0] == EXP_BARE_TRUE for h in hits))
    P("  %s 分層後：真命中 ＝ **%d**（`%s`）／偽命中 ＝ **%d**（`%s`）"
      % (M(ok7), real, EXP_BARE_TRUE.split("/")[-1], fake, EXP_BARE_FAKE.split("/")[-1]))
    P("  ⇒ 純數字之裸掃描與中文複合詞同理**須分層**（考古節·`恆` 咬中 `守恆式` 之同族）。")
    if not ok7:
        stop("⑥", "`Q-7` 之分層與預測不符（逐字上下文見上）")

    # ── §七　土地三數（`驗收 12`·**未重算之轉述**）─────────────────────────
    hdr("【§七】🔒 土地三數 ＝ **未重算之轉述**（`驗收 12`）")
    P("  %s" % LAND_QUOTED)
    P("  🔒 本檔**零管線** ⇒ 上三數⛔ **未重算**，係自 `W-G.9-99 補正②`／`補正③` 之**轉述**；")
    P("     其來源檔於本批 `numstat` **零觸**（見 `驗收 1`／`驗收 2`）。")
    P("  🔒 出艙稱謂（`VR-054 三`）：池增量 `84.0800 ㎡` 係**依守恆式導出·⛔ 非幾何實量**。")

    return finish(log_path, H_BEFORE)


def finish(log_path, H_BEFORE):
    hdr("【§八】收工：生產檔 hash 前後對拍・`SELF` 自扣・停機逐字")
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
    P("     ⇒ 其中三受詞文件之**更正後**落點數已列於 `Q-6`（⛔ 非自母體隱去·係具名並陳）。")
    P("  🔒 **⛔ 零管線**：本檔未 `harvest()`／未 `run_step_g`／未 import 任何既有探針。")
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
