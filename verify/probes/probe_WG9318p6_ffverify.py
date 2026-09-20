# -*- coding: utf-8 -*-
r"""W-G.9-318 補令六 工項零′：**主線快轉後之五項出艙**（唯讀·⛔ 延後）。

受詞 ＝ `W-G.9-318R7` `§七-1` 所令之 ①〜⑤。
用法：`probe_WG9318p6_ffverify.py <期望之新主線全 40 碼>`
🔒 每項皆附判別力二造（必非零／必為零），⛔ 恆綠。
"""
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
OLD = "40375702378af4cefd2d11515fdf3f98c0791580"

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

SIX = ["7f43924", "7c346b1", "7c07a36", "6cc51e6", "b1141a3", "8e056b4"]


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def o(a):
    return g(a).stdout.decode("utf-8")


def blob(rev, p):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout if r.returncode == 0 else None


def main():
    exp = sys.argv[1]
    g(["fetch", "origin", "--prune"])          # 俾 `branch -r --contains` 讀得新態
    print("# `W-G.9-318` 工項零′　主線快轉後之五項出艙")
    print("期望之新主線 ＝ `%s`\n" % exp)

    # ① ls-remote 全 40 碼
    row = o(["ls-remote", "origin", "refs/heads/wip/s1-endpart"]).split()
    got = row[0] if row else "?"
    print("══ ① `ls-remote` 全 `40` 碼 ══")
    print("  `refs/heads/wip/s1-endpart` ＝ `%s`" % got)
    print("  ⇒ ＝ 期望值？ **%s** %s" % (got == exp, "🟢" if got == exp else "🔴"))
    print("  判別力［必非零之對照］：舊值 `%s` ≠ 期望值 ⇒ %s\n" % (OLD[:7], OLD != exp))

    # ② is-ancestor
    rc = g(["merge-base", "--is-ancestor", OLD, got]).returncode
    rc_neg = g(["merge-base", "--is-ancestor", got, OLD]).returncode
    print("══ ② `merge-base --is-ancestor` ══")
    print("  `4037570` → 新主線：`rc` ＝ **`%d`**（須 `0`）%s" % (rc, "🟢" if rc == 0 else "🔴"))
    print("  判別力［必為非零］反向（新主線 → `4037570`）：`rc` ＝ **`%d`**（須 `≠ 0`）%s\n"
          % (rc_neg, "🟢" if rc_neg != 0 else "🔴"))

    # ③ 分支數
    tot = len(o(["ls-remote", "--heads", "origin"]).splitlines())
    ver = len(o(["ls-remote", "--heads", "origin", "refs/heads/verify/*"]).splitlines())
    pres = o(["ls-remote", "origin", "refs/heads/wip/W-G.9-318-preserve"]).split()
    print("══ ③ 遠端分支 ══")
    print("  總數 ＝ **`%d`**（須 `25`·⛔ 減）%s" % (tot, "🟢" if tot == 25 else "🔴"))
    print("  `refs/heads/verify/*` ＝ **`%d`**（須 `20`）%s" % (ver, "🟢" if ver == 20 else "🔴"))
    print("  `preserve` **保留** ＝ `%s` %s\n"
          % (pres[0] if pres else "🔴 已不存在", "🟢" if pres else "🔴"))

    # ④ 生產碼 34 檔
    diff = [p for p in PROD34 if blob(got, p) != blob(exp, p)]
    print("══ ④ 生產碼 `34` 檔（正面列舉·⛔ 空 pathspec） ══")
    print("  新主線 vs `%s` 之相異 ＝ **`%d`**（須 `0`）%s %s"
          % (exp[:7], len(diff), "🟢" if not diff else "🔴", diff))
    dk = blob(OLD, "app.py") != blob(exp, "app.py")
    print("  判別力［必非零］：`app.py` 於 `4037570` vs `%s` ⇒ 相異 ＝ **%s**（須 `True`）%s\n"
          % (exp[:7], dk, "🟢" if dk else "🔴"))

    # ⑤ 六筆之可達性
    print("══ ⑤ 六筆生產碼 `commit` 之可達性 ══")
    ok = 0
    for h in SIX:
        br = o(["branch", "-r", "--contains", h]).splitlines()
        hit = any(b.strip().startswith("origin/wip/s1-endpart") for b in br)
        ok += hit
        print("  `%s`  含 `origin/wip/s1-endpart`？ **%s** %s"
              % (h, hit, "🟢" if hit else "🔴"))
    print("  ⇒ `%d`／`6` 🟢" % ok if ok == 6 else "  ⇒ `%d`／`6` 🔴" % ok)
    # 判別力［必不命中］：4037570 之父⛔ 落於 4037570..新主線 內
    par = o(["rev-parse", "%s^" % OLD]).strip()
    inrange = par in o(["rev-list", "%s..%s" % (OLD, got)]).split()
    print("  判別力［必不命中］：`4037570^`（`%s…`）∈ `4037570..新主線`？ **%s**（須 `False`）%s"
          % (par[:8], inrange, "🟢" if not inrange else "🔴"))
    print("  （其確為既有物件：`git cat-file -t` ⇒ `%s`）"
          % o(["cat-file", "-t", par]).strip())


if __name__ == "__main__":
    main()
