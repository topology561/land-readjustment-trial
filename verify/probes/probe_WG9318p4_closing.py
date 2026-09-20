# -*- coding: utf-8 -*-
r"""W-G.9-318 補令四 `§五`：收工閘 `1`〜`8` 之實測（報告入倉後量·唯讀）。

🔒 `恆常附款 x`：`append-only` 之判**三值化**（🟢 前綴且增長／🔵 前綴且未改／🔴 前綴被破）。
🔒 `恆常附款 w②`：一切 blob 錨繫於**本批開工態** `bc97c9d…`（⛔ 沿用他批）。
🩸 CJK 路徑：一律 `-c core.quotepath=false`（⛔ 八進位跳脫）。
"""
import hashlib
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
BASE = "bc97c9d72d1680e820872aba787ecc453fa3a509"
MAIN = "40375702378af4cefd2d11515fdf3f98c0791580"

PROD34 = ["app.py"] + ["verify/" + n for n in [
    "app_harvest.py", "b6_isomorphism.py", "fixture_baseline_candidates.py",
    "fixture_block_depth_n19p.py", "fixture_cad_binding_order.py",
    "fixture_corner_range_k8.py", "fixture_e2e_termination.py",
    "fixture_end_fallback.py", "fixture_end_reserve.py", "fixture_end_winner.py",
    "fixture_g3_static_guards.py", "fixture_klui_t2diag.py",
    "fixture_midlayer_6items.py", "fixture_n14_feed_chain.py",
    "fixture_n14_min_width.py", "fixture_wf_ns_wiring.py",
    "fixture_yi_construction.py", "run_all.py", "run_verification.py",
    "selection_pipeline.py", "stepg_pipeline.py", "test_corner_first_lot_G.py",
    "wd3_fragment_geom.py", "wd4_tier_list.py", "wf_f0.py", "wf_f1.py",
    "wf_f2.py", "wf_f3.py", "wf_f4.py", "wg_g1_smoke.py", "wg_g2_smoke.py",
    "wg_g3.py", "wv_reconcile.py"]]

APPEND_TARGETS = [
    ("docs/reports/W-G.9波_claude.ai側自誤登記.md", "本批受改"),
    ("docs/reports/W-G.9-318_CC側換手_一.md", "本批受改"),
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "本批⛔ 受改"),
    ("CLAUDE.md", "本批⛔ 受改"),
    ("docs/reports/W-G.4_泛用阻塞項登記表.md", "本批⛔ 受改"),
    ("docs/驗證裁定登記表.md", "本批⛔ 受改"),
]


def g(args):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + args,
                          cwd=REPO, capture_output=True)


def out(args):
    return g(args).stdout.decode("utf-8")


def blob(rev, path):
    p = g(["show", "%s:%s" % (rev, path)])
    return p.stdout if p.returncode == 0 else None


def main():
    head = out(["rev-parse", "HEAD"]).strip()
    print("# `W-G.9-318` 補令四　收工閘之實測（報告入倉後量）")
    print("開工態 ＝ `%s`／期末 HEAD ＝ `%s`" % (BASE, head))
    revs = out(["rev-list", "--reverse", "%s..HEAD" % BASE]).split()
    print("本批 `commit` ＝ **`%d`** 筆\n" % len(revs))

    # ── 閘 1　逐 commit numstat（刪除欄全 0）──
    print("══ 閘 `1`　逐 `commit` `numstat`（刪除欄須全 `0`） ══")
    bad = 0
    for r in revs:
        rows = [l for l in out(["show", "--numstat", "--format=", r]).splitlines() if l.strip()]
        dels = 0
        for l in rows:
            f = l.split("\t")
            if len(f) >= 3 and f[1].isdigit():
                dels += int(f[1])
        flag = "🟢" if dels == 0 else "🔴"
        bad += dels != 0
        print("  %s %s  檔 `%d`／刪除欄合計 `%d`  %s"
              % (flag, r[:7], len(rows), dels, out(["log", "-1", "--format=%s", r]).strip()[:48]))
    print("  ⇒ 刪除欄非零之 `commit` ＝ `%d`（須 `0`）%s\n" % (bad, "🟢" if bad == 0 else "🔴"))

    # ── 閘 2　生產碼 34 檔之相異 ──
    print("══ 閘 `2`　生產碼 `34` 檔相對**開工態 `%s`** 之相異 ══" % BASE[:7])
    diff = [p for p in PROD34 if blob(BASE, p) != blob(head, p)]
    print("  母體 ＝ 正面列舉 `%d` 檔（⛔ 空 pathspec）" % len(PROD34))
    print("  相異 ＝ **`%d`**（須 `0`）%s  %s" % (len(diff), "🟢" if not diff else "🔴", diff))
    print("  判別力［必非零］：`app.py` 之 `BASE` vs `MAIN` 之 blob 相異 ＝ %s"
          % (blob(BASE, "app.py") != blob(MAIN, "app.py")))
    print()

    # ── 閘 3　本批 .md 之 CR ──
    print("══ 閘 `3`　本批 `.md` 之 `CR` ══")
    files = [x for x in out(["diff", "--name-only", BASE, "HEAD"]).splitlines()
             if x.endswith(".md")]
    print("  受檢集 ＝ **`%d`** 檔（`0` ⇒ 器紅）%s" % (len(files), "🟢" if files else "🔴"))
    tot = 0
    for f in files:
        b = blob(head, f) or b""
        tot += b.count(b"\r")
        print("    · %s  `CR` ＝ `%d`" % (f, b.count(b"\r")))
    print("  ⇒ `CR` 合計 ＝ **`%d`**（須 `0`）%s\n" % (tot, "🟢" if tot == 0 else "🔴"))

    # ── 閘 4　四簿二框並報 ──
    print("══ 閘 `4`　四簿（**二框並報**·期末態） ══")
    import re
    Z_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
    Z_RNG = re.compile(r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
    specs = [("自誤", "docs/reports/W-G.9波_claude.ai側自誤登記.md", None, set()),
             ("GB", "docs/reports/W-G.4_泛用阻塞項登記表.md",
              re.compile(r"^#{2,4}[^\n]*?GB-([0-9]{1,4})", re.M), set()),
             ("VR", "docs/驗證裁定登記表.md",
              re.compile(r"^#+ `?VR-([0-9]{1,4})`?", re.M), {999}),
             ("K-9", "docs/rulings/K-6_街角地分配程序與可分配判準.md",
              re.compile(r"^#{2,4}[^\n]*?K-9-([0-9]{1,3})", re.M), set())]
    for name, path, frame, drop in specs:
        for tag, rev in (("開工", BASE), ("期末", head)):
            t = (blob(rev, path) or b"").decode("utf-8")
            if frame is None:
                s = set(int(x) for x in Z_DEF.findall(t))
                for a, b in Z_RNG.findall(t):
                    a, b = int(a), int(b)
                    if b > a and b - a < 40:
                        s.update(range(a, b + 1))
            else:
                s = set(int(x) for x in frame.findall(t)) - drop
            miss = sorted(set(range(min(s), max(s) + 1)) - s)
            print("  %-4s %s  相異 `%d`／MAX `%d`／缺 %s"
                  % (name, tag, len(s), max(s),
                     miss if len(miss) <= 10 else "(%d)" % len(miss)))
    print("  🔒 算式（`恆常附款 w①`）：自誤 相異 ＝ 開工 `431` ＋ 本批新鑄 `1`（`自誤 442`）＝ **`432`**；MAX ＝ **`442`**\n")

    # ── 閘 5　append-only（三值化）──
    print("══ 閘 `5`　`append-only`（**三值化**·`恆常附款 x`） ══")
    for path, note in APPEND_TARGETS:
        b0, b1 = blob(BASE, path), blob(head, path)
        if b0 is None or b1 is None:
            print("  🔴 %s：blob 缺" % path)
            continue
        if b1 == b0:
            v = "🔵 **前綴且未改**（%s）" % note
        elif b1.startswith(b0):
            v = "🟢 **前綴且增長** `+%d` B" % (len(b1) - len(b0))
        else:
            v = "🔴 **前綴被破**"
        print("  %-46s %s" % (path.rsplit("/", 1)[-1][:44], v))
        print("       期初 `%d` B／`%s…`　期末 `%d` B／`%s…`"
              % (len(b0), hashlib.sha256(b0).hexdigest()[:16],
                 len(b1), hashlib.sha256(b1).hexdigest()[:16]))
    print()

    # ── 閘 6　自限 ──
    print("══ 閘 `6`　自限 ══")
    bl = subprocess.run(["git", "ls-tree", "-r", "HEAD", "verify/baselines"],
                        cwd=REPO, capture_output=True).stdout
    print("  `baselines` `sha256` ＝ `%s`·**`%d`** 列（須 `a898f4e1…`／`298`）"
          % (hashlib.sha256(bl).hexdigest(), len(bl.decode().splitlines())))
    print("  遠端總數 ＝ `%d`（須 `25`）；`refs/heads/verify/*` ＝ `%d`（須 `20`）"
          % (len(out(["ls-remote", "--heads", "origin"]).splitlines()),
             len(out(["ls-remote", "--heads", "origin", "refs/heads/verify/*"]).splitlines())))
    m = out(["ls-remote", "origin", "refs/heads/wip/s1-endpart"]).split()
    print("  主線 ＝ `%s`（須 `%s`·**未動**）%s"
          % (m[0] if m else "?", MAIN, "🟢" if m and m[0] == MAIN else "🔴"))
    print()

    # ── 閘 7　母體三數 ──
    print("══ 閘 `7`　母體三數（`VR-091 一`） ══")
    print("  `(1)` 來源 `commit` ＝ `%s`" % head)
    md = [x for x in out(["ls-tree", "-r", "--name-only", "HEAD"]).splitlines() if x.endswith(".md")]
    docs = [x for x in out(["ls-tree", "-r", "--name-only", "HEAD", "docs/"]).splitlines()]
    vout = [x for x in out(["ls-tree", "-r", "--name-only", "HEAD", "verify/out/"]).splitlines()]
    print("  `(2)` 母體：全倉追蹤 `.md` ＝ **`%d`** 檔／全 `docs/` ＝ **`%d`** 檔／`verify/out/` ＝ **`%d`** 檔"
          % (len(md), len(docs), len(vout)))
    print("  `(3)` 粒度框 ＝ **列框**（計數）／**bytes**（blob）")
    b0v = [x for x in out(["ls-tree", "-r", "--name-only", BASE, "verify/out/"]).splitlines()]
    same = sum(1 for p in b0v if blob(BASE, p) != blob("HEAD", p))
    print("  `verify/out/` 既有 `%d` 檔之 blob 相異 ＝ **`%d`**（須 `0`）·新增 **`%d`** 檔"
          % (len(b0v), same, len(vout) - len(b0v)))
    print()

    # ── 閘 8　ls-remote ──
    print("══ 閘 `8`　`ls-remote`（全 `40` 碼）＋ 本批筆數 ══")
    pr = out(["ls-remote", "origin", "refs/heads/wip/W-G.9-318-preserve"]).split()
    print("  `wip/W-G.9-318-preserve` ＝ `%s`" % (pr[0] if pr else "?"))
    print("  本地 HEAD ＝ `%s`" % head)
    print("  本批筆數 ＝ **`%d`**" % len(revs))
    print("  ⇒ %s" % ("🟢 **已 push·逐位相符**" if pr and pr[0] == head
                      else "🛑 **尚未 push**（本節於 push 前量·其判見報告 `§七-5`）"))


if __name__ == "__main__":
    main()
