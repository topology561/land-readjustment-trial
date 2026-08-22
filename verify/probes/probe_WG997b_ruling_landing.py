#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-97 補正②**：`K-9-17` ＋ `K-9-15` 逐字補記之**入倉後機檢**（⛔ 零生產碼）。

## 受詞（施工單 `W-G.9-97 補正②` §六-2）

- **§三／§四 之逐字逐條對 blob**：本批 append 之每一句 KL 逐字，須於 `K-6` **現查得到**；
  且每句附**判別力陽性對照**（改一字 ⇒ 命中須為 `0`）。
- **母體／納入／略過**之出艙（`§Z-8` ＋ 其**補款②**：量測器須自母體扣除自身、扣除數計入略過）。
- **期初／期末錨**：`app.py` blob 不變；`K-6`／`SKILL.md`／`CLAUDE.md` 之附加為**純附加**。

## 🛑 紅線

⛔ 零生產碼變更；⛔ 不跑 `run_step_g`／`run_all`／`run_corner_pk`（以 raise 版覆蓋機械證明）；
⛔ 不改任何既有文字（本批全為 append）。

## 🔒 `§Z-8` 補款②（本檔自套）

母體一律**扣除 `SELF`**，扣除數**計入 `略過`**；`SELF` 之命中**檔名照列、行數⛔ 不印**
（本檔之 log 亦屬 `SELF` ⇒ 印行數即自我指涉 ⇒ log 無不動點）。

## 重跑

    python verify/probes/probe_WG997b_ruling_landing.py

rc **恆為 0**；唯缺件／逐字不符時 loud raise（`no-silent-fallback`）。
`A-1` 判準 ＝「基座 `7a6ae06` 為 `HEAD` 之祖先或等於 `HEAD`」（節 122 之併記）。
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
BASE_SHORT = "7a6ae06"

SELF = [
    "verify/probes/probe_WG997b_ruling_landing.py",
    "verify/out/probe_WG997b_ruling_landing_7a6ae06.log",
    "docs/reports/W-G.9-97補正②_逐字補記與K-9-17入倉.md",
]

K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
SK = ".claude/skills/failure-archaeology/SKILL.md"
ZW = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
CM = "CLAUDE.md"

L = []
SKIPPED = []
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
    p = subprocess.run(args, cwd=REPO, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    return p.returncode, p.stdout.decode("utf-8", errors="replace")


def git1(args):
    rc, out = sh(["git", "-c", "core.quotePath=false"] + args)
    if rc != 0:
        raise RuntimeError("🔴 git 失敗 rc=%d：%s\n%s" % (rc, " ".join(args), out))
    return out.strip()


def read_text(rel):
    with open(os.path.join(REPO, rel), "rb") as f:
        return f.read().decode("utf-8")


def blob_sha256(rel, rev="HEAD"):
    rc, _ = sh(["git", "cat-file", "-e", "%s:%s" % (rev, rel)])
    if rc != 0:
        return None
    p = subprocess.run(["git", "-c", "core.quotePath=false", "cat-file",
                        "blob", "%s:%s" % (rev, rel)],
                       cwd=REPO, stdout=subprocess.PIPE)
    return hashlib.sha256(p.stdout).hexdigest()


def find_lines(text, needle):
    """回 `[(行號, 逐字)]`；以行號**回取覆驗**（§Z-9·⛔ 不肉眼切）。"""
    ls = text.splitlines()
    out = []
    for i, ln in enumerate(ls):
        if needle in ln:
            if ls[i] != ln:
                raise RuntimeError("🔴 回取覆驗不符：行 %d" % (i + 1))
            out.append((i + 1, ls[i]))
    return out


def mutate_one(s):
    """改一字（末字元換成執行期組出之替身）——供判別力陽性對照（常設 8）。"""
    alt = chr(0x24B6)                                   # ⛔ 不寫死可讀哨兵字樣
    return s[:-1] + alt if s else alt


def _forbidden(name):
    def _f(*a, **kw):
        CALLGUARD[name] += 1
        raise RuntimeError("🔴 本批⛔ 不得呼叫 `%s`" % name)
    return _f


# ══════════════════════════════════════════════════════════════════════════════
#  受詞：本批 append 之 KL 逐字（⛔ 照 `W-G.9-97 補正②` 之單內文字）
# ══════════════════════════════════════════════════════════════════════════════
V_K915 = ("若其計算的 G 值大於藍影線面積，則多出來的 G 值就從圖面上的 B1 "
          "往街廓內移動迭代計算到該宗土地 G 值，後續的宗地就是平行 ALLOCLINE，"
          "並依其應分配 G 值確定其遠側境界線")

V_MAIN = ("「投影序號中下一位」之受詞 ＝ <u>街角重排後</u>序列之下一位；"
          "⛔ 非重排前之投影序號 ＋ 1。")

V_SEG = [
    ("一", "街廓順序都要先從左右側街角宗開始各自往街廓中間分配，所以首先要確立由街角宗開始的順序"),
    ("一", "則該街廓投影順序此時就要變成2,1,3,4,5"),
    ("二", "那麼該空位就由3遞補(空位位置係由第0宗遠側境界線開始依據遞補宗的G再決定第1宗遠側境界線"),
    ("二", "而1地號空出之面積當然依據街廓面積守恆式，就是列為配餘地(調配池)"),
    ("三", "就是代表KL 上面裁示的街角地確立後序位重排的機制，那就是對的，以性質為準。"),
    ("四", "之後的第2宗以後因為境界線間都是平行allocline ，所以之前有裁示不交叉恆真直至街廓中間"),
    ("五", "所以任何的重排或遞補當然要重算G值（後面的宗也會整體往前分配，所以也要重算G）"),
    ("六", "街角winner 一定符合非畸零地，之前已說明過（街角地最小規定範圍的構成係以sideline 沿法向平移 退縮+畸零寬）。"),
    ("七", "則街廓中間一定會有配餘地（調配池）。"),
]

V_AFTER = [
    "🔴 **落地前提之更正**：`W-G.9-97` `C-1` 現查 —— 「決定遞補位次之處」可執行母體 ＝ **0**",
    "⇒ 現行碼**並無**遞補之實作，落地係**從零實作**。",
    "⇒ `stepg_pipeline.py:491-509` 係**結構閘**（驗「位次＝投影序」）、⛔ 非遞補式；",
    "其口徑為**重排前**，於本裁落地後**必然轉紅** ⇒ 落地批須**同批處置**，否則第一跑即停。",
]

V_ZDASH = "量測器須自母體扣除自身，並將扣除數計入 `略過`。"
V_RULE2 = ("「純新增檔」以 `git diff --stat` 之 **`deletions ＝ 0` ＋ 既有檔零命中**為準，"
           "⛔ 非以檔數判。")


def main():                                                          # noqa: C901
    head = git1(["rev-parse", "HEAD"])
    head_s = git1(["rev-parse", "--short", "HEAD"])
    app_blob = git1(["rev-parse", "HEAD:app.py"])
    base_ok = subprocess.run(["git", "merge-base", "--is-ancestor", BASE_SHORT, "HEAD"],
                             cwd=REPO, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL).returncode == 0
    log_path = os.path.join(OUTDIR, "probe_WG997b_ruling_landing_%s.log" % BASE_SHORT)

    import stepg_pipeline as _sg
    import selection_pipeline as _sp
    import run_verification as _rv
    _sg.run_step_g = _forbidden("run_step_g")
    _sp.run_corner_pk = _forbidden("run_corner_pk")
    _rv.main = _forbidden("run_all_main")

    hdr("【W-G.9-97 補正②】`K-9-17` ＋ `K-9-15` 逐字補記之入倉後機檢（⛔ 零生產碼·⛔ 未跑管線）")
    say("  基座 ＝ **%s**；產生於 HEAD ＝ **%s**（%s）" % (BASE_SHORT, head_s, head))
    say("  `app.py` blob：%s（HEAD）／%s（工作區）"
        % (app_blob, git1(["hash-object", "app.py"])))
    say("  🔒 SELF ＝ %s" % SELF)
    say("  🛑 呼叫護欄已裝（`run_step_g`／`run_corner_pk`／`run_verification.main` ⇒ raise 版）")

    # ── §A　A-0 ────────────────────────────────────────────────────────────
    hdr("【§A】`A-0` 先驗錨（`-97` §一 七列 ＋ 加驗 `K-6` blob）")
    ok = True

    def gate(gid, item, expect, got):
        nonlocal ok
        good = (str(expect) == str(got))
        ok = ok and good
        say("  %-6s %-30s %s  期望＝%s  現查＝%s"
            % (gid, item, "✅" if good else "🔴", expect, got))

    gate("A-1", "基座 %s ⊆ HEAD 之祖先" % BASE_SHORT, True, base_ok)
    gate("A-2", "app.py blob", "a9e5671d64d254907a0396f898f046d9d85e8283", app_blob)
    say("  A-3   origin/wip/s1-endpart        現查＝%s；ahead／behind ＝ %s"
        % (git1(["rev-parse", "origin/wip/s1-endpart"]),
           git1(["rev-list", "--left-right", "--count",
                 "HEAD...origin/wip/s1-endpart"]).replace("\t", " ／ ")))
    sk_t = read_text(SK)
    ns = [int(m.group(1)) for l in sk_t.splitlines() if (m := re.match(r"^##\s*(\d+)\.\s", l))]
    say("  A-4   考古節（期末）                命中 ＝ %d／相異 ＝ %d／最大 ＝ **%d**（缺號 %s）"
        % (len(ns), len(set(ns)), max(ns),
           [i for i in range(1, max(ns) + 1) if i not in set(ns)]))
    zw_t = read_text(ZW)
    zs = [(i + 1, int(m.group(1))) for i, l in enumerate(zw_t.splitlines())
          if (m := re.match(r"^##\s*自誤\s*(\d+)", l))]
    gate("A-5", "自誤登記最大序號（期末）", 100, max(v for _, v in zs))
    say("        ⇒ 🛑 **自誤 101–103 ⛔ 未辦**（其逐字本文未到·見報告 §E-1）"
        "——最大序號仍 **100**＠`:%d`" % [i for i, v in zs if v == 100][0])
    k6_t = read_text(K6)
    mn = sorted({int(m.group(1)) for l in k6_t.splitlines()
                 if (m := re.match(r"^###\s*🔒?\s*K-9-(\d+)(?:\s|　)", l))})
    gate("A-6", "K-6 主序列最大（期末）", 17, max(mn))
    say("        佔用 ＝ %s" % mn)
    say("  A-7   行數計法（`\\n 計` ／ `splitlines()`）／期初→期末 blob SHA-256")
    for rel, exp0 in ((K6, "9d61f35b6f8793ea5e1a891c28c39714c743bb49987aacee8c5e284b7f6e6c1a"),
                      (SK, None), (ZW, None), (CM, None)):
        t = read_text(rel)
        s0 = blob_sha256(rel, BASE_SHORT)
        s1 = blob_sha256(rel, "HEAD")
        note = ""
        if exp0 is not None:
            note = "  期初期望＝%s ⇒ %s" % (exp0[:16] + "…",
                                       "✅" if s0 == exp0 else "🔴")
            ok = ok and (s0 == exp0)
        say("        %-52s %d ／ %d" % (rel, t.count("\n"), len(t.splitlines())))
        say("          期初(%s)＝%s%s" % (BASE_SHORT, s0, note))
        say("          期末(HEAD)＝%s   %s" % (s1, "（**未變**）" if s0 == s1 else "（**已變**·本批 append）"))
    say("")
    say("  ⇒ `A-0`：%s" % ("✅ **全綠**" if ok else "🔴 **有紅** ⇒ 🛑 停機"))
    if not ok:
        raise RuntimeError("🔴 §A `A-0` 紅 ⇒ 停機")

    # ── §B　逐字對 blob ＋ 判別力 ────────────────────────────────────────────
    hdr("【§B】本批 append 之逐字逐條對 blob（每句附**判別力陽性對照**·常設 8）")
    say("  🔒 判準：每句於 `K-6` 命中 **≥1**；其**改一字**之變體命中須 **＝ 0**（否則該檢無判別力）。")
    say("  🔒 每筆以行號**回取覆驗**（§Z-9）；`檔`／`行`／`逐字` 分欄。")
    say("")
    rows = []
    CASES = ([("K-9-15 逐字補記", V_K915), ("K-9-17 主文", V_MAIN)]
             + [("K-9-17 段%s" % k, v) for k, v in V_SEG]
             + [("K-9-17 後果註 %d" % (i + 1), v) for i, v in enumerate(V_AFTER)])
    for name, s in CASES:
        hits = find_lines(k6_t, s)
        bad = find_lines(k6_t, mutate_one(s))
        good = (len(hits) >= 1 and len(bad) == 0)
        rows.append((name, len(hits), len(bad), good))
        say("  %-22s 命中 ＝ %d  改一字命中 ＝ %d  %s"
            % (name, len(hits), len(bad), "✅" if good else "🔴"))
        for n_, _t in hits[:1]:
            say("        檔 ＝ %s ／ 行 ＝ %d" % (K6, n_))
    pop(len(CASES), len(rows), "B 逐字對拍（全列）")
    n_bad = sum(1 for _, _, _, g in rows if not g)
    say("  ⇒ 不符 ＝ **%d** ／ %d" % (n_bad, len(rows)))
    if n_bad:
        raise RuntimeError("🔴 §B 逐字對拍不符 %d 項 ⇒ 停機（⛔ 不入倉）" % n_bad)

    say("")
    say("  ── 其餘二處 append 之逐字 ──")
    sk_hits = find_lines(sk_t, V_ZDASH)
    sk_bad = find_lines(sk_t, mutate_one(V_ZDASH))
    say("  `§Z-8` 補款②（`SKILL.md` 節 122）  命中 ＝ %d  改一字 ＝ %d  %s"
        % (len(sk_hits), len(sk_bad), "✅" if sk_hits and not sk_bad else "🔴"))
    for n_, _t in sk_hits:
        say("        檔 ＝ %s ／ 行 ＝ %d" % (SK, n_))
    cm_t = read_text(CM)
    cm_hits = find_lines(cm_t, V_RULE2)
    cm_bad = find_lines(cm_t, mutate_one(V_RULE2))
    say("  常規一 `②` 補款（`CLAUDE.md`）      命中 ＝ %d  改一字 ＝ %d  %s"
        % (len(cm_hits), len(cm_bad), "✅" if cm_hits and not cm_bad else "🔴"))
    for n_, _t in cm_hits:
        say("        檔 ＝ %s ／ 行 ＝ %d" % (CM, n_))
    pop(2, 2, "B 其餘二處（全列）")
    if not (sk_hits and not sk_bad and cm_hits and not cm_bad):
        raise RuntimeError("🔴 §B 其餘二處逐字對拍不符 ⇒ 停機")

    # ── §C　純附加之機械證明 ────────────────────────────────────────────────
    hdr("【§C】純附加之機械證明（`deletions ＝ 0`·嚴格前綴）")
    say("  🔒 判準（常規一 `②` 之補款逐字）：`deletions ＝ 0` ＋ 既有檔零命中；⛔ 非以檔數判。")
    say("")
    say("  🔒 期末 ＝ **index（已 stage）之 blob**——⛔ 非 `HEAD`（未 commit 時 `HEAD` ＝ 基座 ⇒ 空檢）。")
    say("")
    say("  檔                                                    期初 bytes → 期末 bytes   嚴格前綴且增長  刪除列")
    n_app = 0
    for rel in (K6, SK, CM):
        p0 = subprocess.run(["git", "-c", "core.quotePath=false", "cat-file",
                             "blob", "%s:%s" % (BASE_SHORT, rel)],
                            cwd=REPO, stdout=subprocess.PIPE).stdout
        # 🔒 **期末 ＝ index（已 stage 之 blob）**——⛔ 非 `HEAD`：本批尚未 commit 時
        #   `HEAD` 仍等於基座 ⇒ 以 `HEAD` 比即**恆真之空檢**（本檔自捕·⛔ 不留空檢）。
        p1 = subprocess.run(["git", "-c", "core.quotePath=false", "cat-file",
                             "blob", ":%s" % rel],
                            cwd=REPO, stdout=subprocess.PIPE).stdout
        pre = bool(p1) and p1.startswith(p0) and len(p1) > len(p0)
        # 🔒 刪除列取 **基座 → 工作區**（`git diff --numstat <基座> -- <檔>`）——
        #   ⛔ 非 `--cached`：入倉後 index 已清空 ⇒ `--cached` 為空 ⇒ 該檢**隨倉態失效**
        #   （本檔第二次自捕·同「探針須可重跑」之族）。本式於入倉前後**同值**。
        _rc, ns_out = sh(["git", "-c", "core.quotePath=false", "diff", "--numstat",
                          BASE_SHORT, "--", rel])
        dele = ns_out.strip().split("\t")[1] if ns_out.strip() else "0"
        say("  %-52s %7d → %7d      %-10s  %s"
            % (rel, len(p0), len(p1), pre, dele))
        n_app += 1
        if not pre or dele != "0":
            raise RuntimeError("🔴 %s 非純附加（startswith=%s·刪除列=%s）" % (rel, pre, dele))
    pop(3, n_app, "C 三檔純附加（全列）")
    say("  ⇒ ✅ 三檔皆 `startswith(期初) ＝ True` 且**刪除列 ＝ 0**")

    # ── §D　母體／納入／略過（§Z-8 ＋ 補款②）────────────────────────────────
    hdr("【§D】母體／納入／略過（`§Z-8` ＋ **補款②**：自母體扣除自身）")
    rc, out = sh(["git", "-c", "core.quotePath=false", "ls-files", "-z"])
    files = [x for x in out.split("\0") if x]
    txt = [f for f in files if f.endswith((".py", ".md", ".log", ".csv", ".txt", ".json"))]
    self_in = [f for f in SELF if f in txt]
    say("  母體 ＝ **%d**（`git ls-files -z` 之全部追蹤檔）" % len(files))
    say("  納入 ＝ **%d**" % (len(txt) - len(self_in)))
    say("  略過 ＝ **%d** ＝ 非文字副檔名 **%d** ＋ `SELF` **%d**"
        % ((len(files) - len(txt)) + len(self_in), len(files) - len(txt), len(self_in)))
    say("  🔒 `SELF` 於母體內之命中**檔名照列**（節 122 補款②：量測器須自母體扣除自身）：")
    for f in self_in:
        say("        %s" % f)
    if not self_in:
        say("        （**0 檔**——本批之三產物**尚未入倉**故不在 `git ls-files` 內；"
            "入倉後重跑即為 **3 檔**·此即補款② 所防之「入倉一次、命中就多幾筆」）")
    say("  ⚠️ 其**行數⛔ 不印**——本檔之 log 亦屬 `SELF`，印其行數即自我指涉 ⇒ log 無不動點；"
        "🔒 此係**具名之不印**、⛔ 非略過未具名（節 119／節 122）。")
    pop(len(files), len(txt) - len(self_in), "D 母體報數")

    # ── §Z ────────────────────────────────────────────────────────────────
    hdr("【§Z】護欄")
    say("  🛑 呼叫護欄終檢：%s" % CALLGUARD)
    if any(CALLGUARD.values()):
        raise RuntimeError("🔴 呼叫了被禁之管線函式：%s" % CALLGUARD)
    say("  ⇒ ✅ `run_step_g`／`run_corner_pk`／`run_verification.main` 呼叫數 ＝ 0／0／0")
    say("  ⇒ ✅ 本批⛔ 未跑 `run_all`")

    with open(log_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n[log] %s" % log_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
