# -*- coding: utf-8 -*-
r"""W-G.9-318 補令六 `§四`：收工閘 `1`〜`8` 之實測（報告入倉後量·唯讀）。

🔒 開工態 ＝ `549121b…`（`恆常附款 w②`·⛔ 沿用他批）。
🔒 閘 `4` 之 `GB` 依補令六 `裁 2`：以 `probe_WG9267_issuer_measurers.py registry` 之
   **自擬框**出艙，並同格具名其定義列式⛔ 經正典釘定。
🔒 閘 `5` `append-only` **三值化**（`恆常附款 x`）。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
BASE = "174b0be1841125b14ed31267aebd0d274915c10f"
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

TOUCH = [
    ("docs/reports/W-G.9波_恆常附款登記表.md", "本批受改"),
    ("docs/reports/W-G.9波_claude.ai側自誤登記.md", "本批受改"),
    ("docs/reports/W-G.9-318_CC側換手_一.md", "本批受改"),
    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "本批⛔ 受改"),
    ("CLAUDE.md", "本批⛔ 受改"),
    ("docs/reports/W-G.4_泛用阻塞項登記表.md", "本批⛔ 受改"),
    ("docs/驗證裁定登記表.md", "本批⛔ 受改"),
]

Z_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
Z_RNG = re.compile(r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
VR_F = re.compile(r"^#+ `?VR-([0-9]{1,4})`?", re.M)
K9_F = re.compile(r"^#{2,4}[^\n]*?K-9-([0-9]{1,3})", re.M)


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def o(a):
    return g(a).stdout.decode("utf-8")


def blob(rev, p):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout if r.returncode == 0 else None


def main():
    head = o(["rev-parse", "HEAD"]).strip()
    revs = o(["rev-list", "--reverse", "%s..HEAD" % BASE]).split()
    print("# `W-G.9-318` 補令六　收工閘（報告入倉後量）")
    print("開工態 ＝ `%s`／期末 ＝ `%s`／本批 **`%d`** 筆\n" % (BASE, head, len(revs)))

    print("══ 閘 `1`　逐 `commit` `numstat`（刪除欄須全 `0`） ══")
    bad = 0
    for r in revs:
        rows = [l for l in o(["show", "--numstat", "--format=", r]).splitlines() if l.strip()]
        d = sum(int(x.split("\t")[1]) for x in rows
                if len(x.split("\t")) >= 3 and x.split("\t")[1].isdigit())
        bad += d != 0
        print("  %s %s  檔 `%d`／刪除 `%d`  %s"
              % ("🟢" if d == 0 else "🔴", r[:7], len(rows), d,
                 o(["log", "-1", "--format=%s", r]).strip()[:46]))
    print("  ⇒ 非零之 `commit` ＝ `%d`（須 `0`）%s\n" % (bad, "🟢" if bad == 0 else "🔴"))

    print("══ 閘 `2`　生產碼 `34` 檔之相異 ══")
    diff = [p for p in PROD34 if blob(BASE, p) != blob(head, p)]
    print("  母體 ＝ 正面列舉 `%d` 檔；相異 ＝ **`%d`**（須 `0`）%s %s"
          % (len(PROD34), len(diff), "🟢" if not diff else "🔴", diff))
    print("  判別力［必非零］：`app.py` `BASE` vs 主線 `%s` ⇒ 相異 ＝ %s\n"
          % (MAIN[:7], blob(BASE, "app.py") != blob(MAIN, "app.py")))

    print("══ 閘 `3`　本批 `.md` 之 `CR` ══")
    files = [x for x in o(["diff", "--name-only", BASE, "HEAD"]).splitlines() if x.endswith(".md")]
    print("  受檢集 ＝ **`%d`** 檔（`0` ⇒ 器紅）%s" % (len(files), "🟢" if files else "🔴"))
    tot = 0
    for f in files:
        c = (blob(head, f) or b"").count(b"\r")
        tot += c
        print("    · %s  `CR` ＝ `%d`" % (f, c))
    print("  ⇒ 合計 ＝ **`%d`**（須 `0`）%s\n" % (tot, "🟢" if tot == 0 else "🔴"))

    print("══ 閘 `4`　四簿（**二框並報**） ══")
    for tag, rev in (("開工", BASE), ("期末", head)):
        t = (blob(rev, "docs/reports/W-G.9波_claude.ai側自誤登記.md") or b"").decode("utf-8")
        s = set(int(x) for x in Z_DEF.findall(t))
        for a, b in Z_RNG.findall(t):
            a, b = int(a), int(b)
            if b > a and b - a < 40:
                s.update(range(a, b + 1))
        print("  自誤〔CC 正典框〕 %s  相異 `%d`／MAX `%d`／缺 %s"
              % (tag, len(s), max(s), sorted(set(range(min(s), max(s) + 1)) - s)))
    for nm, path, fr, drop in (("VR", "docs/驗證裁定登記表.md", VR_F, {999}),
                               ("K-9", "docs/rulings/K-6_街角地分配程序與可分配判準.md", K9_F, set())):
        for tag, rev in (("開工", BASE), ("期末", head)):
            t = (blob(rev, path) or b"").decode("utf-8")
            s = set(int(x) for x in fr.findall(t)) - drop
            print("  %-4s〔標題錨定框〕 %s  相異 `%d`／MAX `%d`" % (nm, tag, len(s), max(s)))
    print("  🔒 自誤之算式（`w①`）：開工 `433` ＋ 本批新鑄 `1`（`自誤 444`）＝ **`434`**；MAX ＝ **`444`**")
    print("  🛑 `GB` 依補令六 `裁 2` 以 `probe_WG9267_issuer_measurers.py registry` 之**自擬框**出艙")
    print("     （其定義列式**⛔ 經正典釘定**·候 `GB-138` 處置 ③·本數僅為該一框之值）：")
    reg = subprocess.run(["python", "verify/probes/probe_WG9267_issuer_measurers.py", "registry"],
                         cwd=REPO, capture_output=True,
                         env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    for l in reg.stdout.decode("utf-8", "replace").splitlines():
        if "GB" in l or "自誤" in l:
            print("     %s" % l.strip())
    print()

    print("══ 閘 `5`　`append-only`（**三值化**·`恆常附款 x`） ══")
    for path, note in TOUCH:
        b0, b1 = blob(BASE, path), blob(head, path)
        v = ("🔵 **前綴且未改**（%s）" % note) if b1 == b0 else (
            "🟢 **前綴且增長** `+%d` B" % (len(b1) - len(b0)) if b1.startswith(b0)
            else "🔴 **前綴被破**")
        print("  %-42s %s" % (path.rsplit("/", 1)[-1][:40], v))
        print("       期初 `%d` B／`%s…`　期末 `%d` B／`%s…`"
              % (len(b0), hashlib.sha256(b0).hexdigest()[:16],
                 len(b1), hashlib.sha256(b1).hexdigest()[:16]))
    print()

    print("══ 閘 `6`　自限 ══")
    bl = subprocess.run(["git", "ls-tree", "-r", "HEAD", "verify/baselines"],
                        cwd=REPO, capture_output=True).stdout
    print("  `baselines` ＝ `%s`·**`%d`** 列" % (hashlib.sha256(bl).hexdigest(),
                                                len(bl.decode().splitlines())))
    print("  遠端總數 ＝ `%d`／`verify/*` ＝ `%d`"
          % (len(o(["ls-remote", "--heads", "origin"]).splitlines()),
             len(o(["ls-remote", "--heads", "origin", "refs/heads/verify/*"]).splitlines())))
    m = o(["ls-remote", "origin", "refs/heads/wip/s1-endpart"]).split()
    print("  主線 ＝ `%s` %s\n" % (m[0], "🟢 未動" if m[0] == MAIN else "🔴"))

    print("══ 閘 `7`　母體三數（`VR-091 一`） ══")
    md = [x for x in o(["ls-tree", "-r", "--name-only", "HEAD"]).splitlines() if x.endswith(".md")]
    docs = o(["ls-tree", "-r", "--name-only", "HEAD", "docs/"]).splitlines()
    vo = o(["ls-tree", "-r", "--name-only", "HEAD", "verify/out/"]).splitlines()
    v0 = o(["ls-tree", "-r", "--name-only", BASE, "verify/out/"]).splitlines()
    print("  `(1)` 來源 `commit` ＝ `%s`" % head)
    print("  `(2)` 全倉 `.md` `%d`／全 `docs/` `%d`／`verify/out/` `%d`" % (len(md), len(docs), len(vo)))
    print("  `(3)` 粒度框 ＝ **列框**（計數）／**bytes**（blob）")
    print("  `verify/out/` 既有 `%d` 檔 blob 相異 ＝ **`%d`**（須 `0`）·新增 **`%d`**\n"
          % (len(v0), sum(1 for p in v0 if blob(BASE, p) != blob("HEAD", p)), len(vo) - len(v0)))

    print("══ 閘 `8`　`ls-remote`（全 `40` 碼） ══")
    pr = o(["ls-remote", "origin", "refs/heads/wip/W-G.9-318-preserve"]).split()
    print("  `preserve` ＝ `%s`" % (pr[0] if pr else "?"))
    print("  本地 HEAD ＝ `%s`" % head)
    print("  ⇒ %s" % ("🟢 已 push·逐位相符" if pr and pr[0] == head else "🛑 尚未 push（於 push 前量）"))


if __name__ == "__main__":
    main()
