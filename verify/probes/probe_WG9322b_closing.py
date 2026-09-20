# -*- coding: utf-8 -*-
r"""`W-G.9-322 補令一` `§三`：收工閘之增補 ＋ `§四`／`§五` 三數之當場重算（唯讀）。

🛑 凡閘三值（`恆常附款 n①`）並同格載其基線態（`r`）；不符即**具名相異·⛔ 追改**。
🔒 `§三` 明文：本補令**⛔ 取代**原單 `§三`，**只增受檢集**；原單閘 `2`／`4`／`6`／`8` ⛔ 變。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
BASE = "4c5a143a2d55d7d9a251a255f46e216086babd43"
C5 = "91a0d10"          # 工項五之 commit（`R0` 之期初）
MAIN_OLD = "40375702378af4cefd2d11515fdf3f98c0791580"
R0 = "docs/reports/W-G.9-322R0_CC側新窗交接文.md"
ORD = "docs/orders/W-G.9-322_補令一_CC側新窗交接文.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"

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

DONE = "a d e f g h k l n p r t u v w x aa ab".split()
NA = "b c i j m o q s y z".split()


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def blob(rev, p):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout if r.returncode == 0 else None


def main():
    head = g(["rev-parse", "HEAD"]).stdout.decode().strip()
    revs = g(["rev-list", "--reverse", "%s..HEAD" % BASE]).stdout.decode().split()
    print("# `W-G.9-322 補令一`　收工閘之增補（`§三`）")
    print("開工態 ＝ `%s`／期末 ＝ `%s`／本批 **`%d`** 筆（單 `§三` 期 `2`）%s\n"
          % (BASE, head, len(revs), "🟢" if len(revs) == 2 else "🩸"))

    print("══ 閘 `1`　刪除欄（受檢集**增本補令之 `2` 筆**·須逐檔 `0`） ══")
    bad = 0
    for r in revs:
        rows = [l for l in g(["show", "--numstat", "--format=", r]).stdout
                .decode().splitlines() if l.strip()]
        per = [(x.split("\t")[2], x.split("\t")[1]) for x in rows if len(x.split("\t")) >= 3]
        d = sum(int(v) for _, v in per if v.isdigit())
        bad += d != 0
        print("  %s %s  檔 `%d`／**刪除欄逐檔** %s"
              % ("🟢" if d == 0 else "🔴", r[:7], len(rows),
                 " ".join("%s=%s" % (p.rsplit('/', 1)[-1][:22], v) for p, v in per)))
    print("  ⇒ 非零之 `commit` ＝ `%d`（須 `0`）%s\n" % (bad, "🟢" if bad == 0 else "🔴"))

    print("══ 閘 `3`　`.md` 之 `CR`（受檢集**增 `2`**：本補令檔 ＋ `W-G.9-322R0`） ══")
    files = [x for x in g(["diff", "--name-only", BASE, "HEAD"]).stdout
             .decode().splitlines() if x.endswith(".md")]
    tot = 0
    for f in files:
        c = (blob(head, f) or b"").count(b"\r")
        tot += c
        mark = " ◀ **本補令所增之受檢集**" if f in (ORD, R0) else ""
        print("    · %s  `CR` ＝ `%d`%s" % (f, c, mark))
    print("  受檢集 ＝ **`%d`** 檔（`0` ⇒ 器紅）；`CR` 合計 ＝ **`%d`**（須 `0`）%s\n"
          % (len(files), tot, "🟢" if tot == 0 and files else "🔴"))

    print("══ 閘 `5`　`append-only` **三值化**（**增一受詞** ＝ `W-G.9-322R0`） ══")
    b0, b1 = blob(C5, R0), blob(head, R0)
    v = "🔵 **前綴且未改**" if b1 == b0 else (
        "🟢 **前綴且增長** `+%d` B" % (len(b1) - len(b0)) if b1.startswith(b0)
        else "🔴 **前綴被破**")
    print("  `W-G.9-322R0`（期初 ＝ **工項五落檔後之態 `%s`**·`恆常附款 r`）" % C5)
    print("     %s｜期初 `%d` B／`%s…`　期末 `%d` B／`%s…`"
          % (v, len(b0), hashlib.sha256(b0).hexdigest()[:16],
             len(b1), hashlib.sha256(b1).hexdigest()[:16]))
    for path in ("docs/reports/W-G.9波_claude.ai側自誤登記.md", BOOK,
                 "docs/reports/W-G.4_泛用阻塞項登記表.md",
                 "docs/rulings/K-6_街角地分配程序與可分配判準.md", "CLAUDE.md"):
        a0, a1 = blob(BASE, path), blob(head, path)
        vv = "🔵 **前綴且未改**（本批⛔ 涉）" if a1 == a0 else (
            "🟢 **前綴且增長** `+%d` B" % (len(a1) - len(a0)) if a1.startswith(a0)
            else "🔴 **前綴被破**")
        print("  %-40s %s" % (path.rsplit("/", 1)[-1][:38], vv))
    print()

    print("══ 原單 `§三` 閘 `2`／`4`／`6`／`8`（單 `§三` 令其**⛔ 變**） ══")
    diff = [p for p in PROD34 if blob(BASE, p) != blob(head, p)]
    print("  閘 `2` 生產碼 `34` 檔相異 ＝ **`%d`**（須 `0`）%s；`app.py` blob ＝ `%s`"
          % (len(diff), "🟢" if not diff else "🔴",
             g(["rev-parse", "%s:app.py" % head]).stdout.decode().strip()))
    print("     判別力[必非零]：`app.py` 對 `%s` ⇒ 相異 ＝ **%s**"
          % (MAIN_OLD[:7], blob(MAIN_OLD, "app.py") != blob(head, "app.py")))
    cg = subprocess.run(["python", "verify/probes/probe_WG9270_closegate.py", "449", "448", "."],
                        cwd=REPO, capture_output=True,
                        env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    for l in cg.stdout.decode("utf-8", "replace").splitlines():
        if l.strip().startswith(("自誤", "GB", "VR", "K-9")):
            print("  閘 `4` 〔正典器〕%s" % l.strip())
    print("     🔒 本補令**⛔ 鑄任何號** ⇒ 四簿期末 ⛔ 變（與原單期初同）")
    bl = subprocess.run(["git", "ls-tree", "-r", "HEAD", "verify/baselines"],
                        cwd=REPO, capture_output=True).stdout
    print("  閘 `6` `baselines` ＝ `%s`·**`%d`** 列；遠端 `%d`／`verify/*` `%d`"
          % (hashlib.sha256(bl).hexdigest(), len(bl.decode().splitlines()),
             len(g(["ls-remote", "--heads", "origin"]).stdout.decode().splitlines()),
             len(g(["ls-remote", "--heads", "origin", "refs/heads/verify/*"]).stdout
                 .decode().splitlines())))
    m = g(["ls-remote", "origin", "refs/heads/wip/s1-endpart"]).stdout.decode().split()
    print("  閘 `8` 主線（於 `push` 前量）＝ `%s`\n" % (m[0] if m else "?"))

    print("══ 閘 `7`　母體三數（**自指增長逐項具名**·須含本補令與 `W-G.9-322R0` 二檔） ══")
    for tag, rev in (("期初", BASE), ("期末", head)):
        tr = g(["ls-tree", "-r", "--name-only", rev]).stdout.decode().splitlines()
        print("  %s：全倉追蹤 **`%d`**／`.md` **`%d`**／`docs/` **`%d`**／`verify/out/` **`%d`**"
              % (tag, len(tr), len([x for x in tr if x.endswith(".md")]),
                 len([x for x in tr if x.startswith("docs/")]),
                 len([x for x in tr if x.startswith("verify/out/")])))
    add = [x for x in g(["diff", "--name-only", "--diff-filter=A", BASE, "HEAD"]).stdout
           .decode().splitlines()]
    print("  **本批新增逐檔（`%d`）**：" % len(add))
    for x in add:
        print("     · %s%s" % (x, " ◀ **單 `§三` 閘 `7` 所令須含者**" if x in (ORD, R0) else ""))
    sub = [x for x in g(["ls-tree", "-r", "--name-only", head]).stdout.decode().splitlines()
           if re.match(r"^verify/.+/.+\.py$", x)]
    print("  子層 `*.py` ＝ **`%d`**（交接文 `§二` 項 `2` 載 `370`）%s"
          % (len(sub), "🟢" if len(sub) == 370 else "🩸 **具名相異**"))
    print()

    print("══ `§四`／`§五` 三數之當場重算（`恆常附款 f` 後段） ══")
    book = blob(head, BOOK).decode("utf-8")
    names = []
    for c in re.findall(r"^\|\s*`([a-z]{1,2})`\s*\|", book, re.M):
        if c not in names:
            names.append(c)
    order = sorted(names, key=lambda s: (len(s), s))
    print("  受掃之款  單 `§四`／`§五` 皆載 `28`／**實測 `%d`**  %s"
          % (len(order), "🟢" if len(order) == 28 else "🩸"))
    print("  🟢 施行   `§四` 末載 **`18`**（`§五` 表載 `16`）／**列舉得 `%d`**  %s"
          % (len(DONE), "🟢" if len(DONE) == 18 else "🩸"))
    print("  ⚪ 不生   `§四` 末載 **`10`**（`§五` 表載 `12`）／**列舉得 `%d`**  %s"
          % (len(NA), "🟢" if len(NA) == 10 else "🩸"))
    uni = sorted(set(DONE) | set(NA), key=lambda s: (len(s), s))
    print("  `%d + %d` ＝ **`%d`**；聯集 ＝ **`%d`** 個；聯集 ＝ 簿內款名？ **%s**"
          % (len(DONE), len(NA), len(DONE) + len(NA), len(uni), uni == order))
    print("  重疊（須空）＝ %s；差集（簿∖表）＝ %s／（表∖簿）＝ %s"
          % (sorted(set(DONE) & set(NA)), sorted(set(order) - set(uni)),
             sorted(set(uni) - set(order))))
    print("  🩸 **單內相異之具名**：`§四` 末已自載其更正（`16`／`12` → `18`／`10`），"
          "而 `§五` 之驗收表**未同步** ⇒ 依 `恆常附款 f` **以列舉為準** ＝ `18`／`10`·⛔ 追改單一字。")

    print("\n══ `§五` 表之其餘二數 ══")
    print("  本補令工項數 單載 `2`（五・六）／**實測 `%d`**  %s"
          % (len(revs), "🟢" if len(revs) == 2 else "🩸"))
    s6 = blob(head, R0).decode("utf-8")
    items = len(re.findall(r"^#### 項 `[1-6]`", s6, re.M))
    print("  工項六應載受詞數 單載 `6`／**實測（`§六-1` 之 `#### 項 N` 節題）`%d`**  %s"
          % (items, "🟢" if items == 6 else "🩸"))


if __name__ == "__main__":
    main()
