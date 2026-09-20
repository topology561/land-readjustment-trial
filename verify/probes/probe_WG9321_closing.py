# -*- coding: utf-8 -*-
r"""`W-G.9-321` `§五`：收工閘之其餘項（唯讀·`probe_WG9270_closegate.py` 所未涵蓋者）。

🛑 凡閘三值出艙（`恆常附款 n①`）並同格載其基線態（`r`）；不符即**具名相異·⛔ 追改**。
"""
import hashlib
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
BASE = "d9df12bad5441ec3e1df7819c17e6de9b8e8f10c"
MAIN_OLD = "40375702378af4cefd2d11515fdf3f98c0791580"
APP_EXP = "8466f7493082bf84aa4f02d6c1c6e55ff746fc4a"

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

TOUCH = [("docs/reports/W-G.9波_claude.ai側自誤登記.md", "本批受改"),
         ("docs/reports/W-G.9波_恆常附款登記表.md", "本批受改"),
         ("docs/reports/W-G.4_泛用阻塞項登記表.md", "本批⛔ 受改"),
         ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "本批⛔ 受改"),
         ("CLAUDE.md", "本批⛔ 受改")]


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def blob(rev, p):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout if r.returncode == 0 else None


def main():
    head = g(["rev-parse", "HEAD"]).stdout.decode().strip()
    revs = g(["rev-list", "--reverse", "%s..HEAD" % BASE]).stdout.decode().split()
    print("# `W-G.9-321` `§五` 收工閘之其餘項")
    print("開工態 ＝ `%s`／期末 ＝ `%s`／本批 **`%d`** 筆\n" % (BASE, head, len(revs)))

    print("══ 閘 `1`　逐 `commit` `numstat`（刪除欄須全 `0`） ══")
    bad = 0
    for r in revs:
        rows = [l for l in g(["show", "--numstat", "--format=", r]).stdout
                .decode().splitlines() if l.strip()]
        d = sum(int(x.split("\t")[1]) for x in rows
                if len(x.split("\t")) >= 3 and x.split("\t")[1].isdigit())
        bad += d != 0
        print("  %s %s  檔 `%d`／刪除 `%d`" % ("🟢" if d == 0 else "🔴", r[:7], len(rows), d))
    print("  ⇒ 非零之 `commit` ＝ `%d`（須 `0`）%s\n" % (bad, "🟢" if bad == 0 else "🔴"))

    print("══ 閘　生產碼（單 `§五`：`34` ⛔ 動·`app.py` blob ⛔ 動） ══")
    diff = [p for p in PROD34 if blob(BASE, p) != blob(head, p)]
    app = g(["rev-parse", "%s:app.py" % head]).stdout.decode().strip()
    print("  母體 ＝ 正面列舉 **`%d`** 檔；相異 ＝ **`%d`**（須 `0`）%s %s"
          % (len(PROD34), len(diff), "🟢" if not diff else "🔴", diff))
    print("  `app.py` blob ＝ **`%s`**／單載 `%s` ⇒ %s"
          % (app, APP_EXP, "🟢 **⛔ 動**" if app == APP_EXP else "🔴"))
    print("  判別力［必非零］：`app.py` 於 `%s` vs 期末 ⇒ 相異 ＝ **%s**（須 `True`）\n"
          % (MAIN_OLD[:7], blob(MAIN_OLD, "app.py") != blob(head, "app.py")))

    print("══ 閘　子層 `*.py`（單 `§五` 載 `367`） ══")
    import re
    sub = [x for x in g(["ls-tree", "-r", "--name-only", head]).stdout.decode().splitlines()
           if re.match(r"^verify/.+/.+\.py$", x)]
    new = [x for x in sub if "WG9321" in x]
    print("  實測 ＝ **`%d`**／單載 `367` ⇒ %s"
          % (len(sub), "🟢" if len(sub) == 367 else "🩸 **具名相異·⛔ 追改**"))
    print("  **列舉**本批所增（`%d` 支）：" % len(new))
    for x in new:
        print("     · %s" % x)
    print("  ⇒ 算式 ＝ 期初 `366` ＋ **`%d`** ＝ **`%d`**\n" % (len(new), 366 + len(new)))

    print("══ 閘　`append-only` **三值化**（`恆常附款 x`） ══")
    for path, note in TOUCH:
        b0, b1 = blob(BASE, path), blob(head, path)
        v = ("🔵 **前綴且未改**（%s）" % note) if b1 == b0 else (
            "🟢 **前綴且增長** `+%d` B" % (len(b1) - len(b0)) if b1.startswith(b0)
            else "🔴 **前綴被破**")
        print("  %-42s %s" % (path.rsplit("/", 1)[-1][:40], v))
        print("       期初 `%d` B／`%s…`　期末 `%d` B／`%s…`"
              % (len(b0), hashlib.sha256(b0).hexdigest()[:16],
                 len(b1), hashlib.sha256(b1).hexdigest()[:16]))
    print("\n══ 閘　自限 ══")
    bl = subprocess.run(["git", "ls-tree", "-r", "HEAD", "verify/baselines"],
                        cwd=REPO, capture_output=True).stdout
    print("  `baselines` ＝ `%s`·**`%d`** 列" % (hashlib.sha256(bl).hexdigest(),
                                                len(bl.decode().splitlines())))
    print("  遠端總數 ＝ `%d`／`verify/*` ＝ `%d`"
          % (len(g(["ls-remote", "--heads", "origin"]).stdout.decode().splitlines()),
             len(g(["ls-remote", "--heads", "origin", "refs/heads/verify/*"]).stdout
                 .decode().splitlines())))
    m = g(["ls-remote", "origin", "refs/heads/wip/s1-endpart"]).stdout.decode().split()
    print("  主線 ＝ `%s`（於 `push` 前量）" % (m[0] if m else "?"))


if __name__ == "__main__":
    main()
