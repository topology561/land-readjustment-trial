# -*- coding: utf-8 -*-
r"""W-G.9-319：輕級開工閘 `②`／`④`／`⑤` ＋ `§零-3` 態錨之復現 ＋ `§八` 三數之當場重算。

🔒 `恆常附款 z`：哨兵須**列舉定義域**（全倉 `.md` 內出現過之 `W-G.9-N` 之 `N`）並證 ∉。
🔒 `恆常附款 aa①`：[必命中]之造須與受詢**同形族**（`W-G.9-318`／`W-G.9-309`）。
🔒 `恆常附款 f`：一切自載基數當場重算並**二值並列**。
🔒 `恆常附款 ab②`：款之條文一律經簿之 `出處` 欄取 `檔:列`，⛔ 文字搜框。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "c286a79cc6a699c57c7763306c4beae9ef7b60a3"
ORDER = "docs/orders/W-G.9-319_施工單_二寬度之量差與GB170三格現查及自誤445.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
GBB = "docs/reports/W-G.4_泛用阻塞項登記表.md"
K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
HANDOVER = "docs/reports/W-G.9-318_CC側換手_一.md"

Z_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
Z_RNG = re.compile(r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
VR_F = re.compile(r"^#+ `?VR-([0-9]{1,4})`?", re.M)
K9_F = re.compile(r"^#{2,4}[^\n]*?K-9-([0-9]{1,3})", re.M)
NAME_F = re.compile(r"^\|\s*`([a-z]{1,2})`\s*\|", re.M)
IDX_F = re.compile(r"^### 款 `([a-z]{1,2})`　出處 ＝ `([^`]+):(\d+)`", re.M)

DONE = "a b e f g h i k l m n o p q r v w x z aa ab".split()
NA = "c d j s t u y".split()


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def txt(p, rev=REV):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def md_files(rev=REV):
    return [x for x in g(["ls-tree", "-r", "--name-only", rev]).stdout
            .decode("utf-8").splitlines() if x.endswith(".md")]


def main():
    print("# `W-G.9-319`　輕級開工閘 ＋ 態錨復現（唯讀）")
    print("開工態 ＝ `%s`\n" % REV)
    files = md_files()
    cache = {p: (txt(p) or "") for p in files}
    own = {ORDER}

    # ══ 閘 ②　號占用（恆常附款 z／aa①）══
    print("══ 閘 `②`　號占用（`W-G.9-319`） ══")
    print("母體 ＝ 追蹤 `.md` **`%d`** 檔（讀不到 `%d`）"
          % (len(files), sum(1 for p in files if not cache[p])))
    # 定義域之列舉：全倉 .md 內出現過之 W-G.9-N 之 N
    dom = set()
    for p in files:
        for m in re.finditer(r"(?<![0-9\-])W-G\.9-([0-9]{1,3})(?![0-9])", cache[p]):
            dom.add(int(m.group(1)))
    print("🔒 `z` 之定義域列舉：全倉 `.md` 內出現過之 `W-G.9-N` 之 `N` ＝ **`%d`** 個相異號"
          "（`MIN` `%d`／`MAX` `%d`）" % (len(dom), min(dom), max(dom)))

    def occ(tok):
        pat_b = re.compile(r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])")
        pat_c = re.compile(r"(?<![0-9\-])`" + re.escape(tok) + r"`(?![0-9])")
        b = {(p, i) for p in files for i, l in enumerate(cache[p].splitlines(), 1) if pat_b.search(l)}
        c = {(p, i) for p in files for i, l in enumerate(cache[p].splitlines(), 1) if pat_c.search(l)}
        u = b | c
        return len(b), len(c), len(u), len([1 for p, _ in u if p not in own])

    for lbl, tok, need in (("受詢", "W-G.9-319", "＝ 0"),
                           ("對照甲［必命中·同形族］", "W-G.9-318", "> 0"),
                           ("對照甲2［必命中·同形族］", "W-G.9-309", "> 0")):
        b, c, u, ext = occ(tok)
        print("  %-24s `%s`：B `%d`／C `%d`／並取 `%d` ⇒ **除本單自身之產物外 `%d`**（須 %s）"
              % (lbl, tok, b, c, u, ext, need))
    sent = next(n for n in range(1000, 9999) if n not in dom)
    b, c, u, ext = occ("W-G.9-%d" % sent)
    print("  對照乙［必為零］哨兵（字面⛔ 出艙）：∈ 定義域？ **%s**（枚舉 `%d` 成員後判）"
          % (sent in dom, len(dom)))
    print("      ⇒ B `%d`／C `%d`／並取 `%d`（須 `0`）" % (b, c, u))
    print("  🔒 `aa②` 二框之**相異維度** ＝ **鄰接形**（裸 vs 反引號括全 token），"
          "⛔ 僅差標點或動詞\n")

    # ══ 閘 ④　四簿二框並報 ══
    print("══ 閘 `④`　四簿（**二框並報**·期初） ══")
    t = txt(LEDGER)
    s = set(int(x) for x in Z_DEF.findall(t))
    for a, b2 in Z_RNG.findall(t):
        a, b2 = int(a), int(b2)
        if b2 > a and b2 - a < 40:
            s.update(range(a, b2 + 1))
    miss = sorted(set(range(min(s), max(s) + 1)) - s)
    print("  自誤〔正典框〕 相異 **`%d`**／MAX **`%d`**／缺 %s" % (len(s), max(s), miss))
    for nm, path, fr, drop in (("VR", "docs/驗證裁定登記表.md", VR_F, {999}),
                               ("K-9", K6, K9_F, set())):
        v = set(int(x) for x in fr.findall(txt(path))) - drop
        print("  %-4s〔標題錨定框〕 相異 **`%d`**／MAX **`%d`**／缺 %s"
              % (nm, len(v), max(v), sorted(set(range(min(v), max(v) + 1)) - v)))
    reg = subprocess.run(["python", "verify/probes/probe_WG9267_issuer_measurers.py", "registry"],
                         cwd=REPO, capture_output=True,
                         env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    print("  ── 自擬框（`probe_WG9267_issuer_measurers.py registry`）──")
    for l in reg.stdout.decode("utf-8", "replace").splitlines():
        if l.strip().startswith(("自誤", "GB", "VR", "K-9")):
            print("     %s" % l.strip())
    print()

    # ══ 閘 ⑤　append-only 期初（三值化）══
    print("══ 閘 `⑤`　`append-only` 之期初（**三值化**·`恆常附款 x`） ══")
    for path in (LEDGER, BOOK, HANDOVER, GBB, K6):
        b0 = g(["show", "%s:%s" % (REV, path)]).stdout
        wt = open(REPO + "\\" + path.replace("/", "\\"), "rb").read()
        print("  %-40s 倉側 `%d` B／`%s…`／工作區 ＝ 倉側 **%s**"
              % (path.rsplit("/", 1)[-1][:38], len(b0),
                 hashlib.sha256(b0).hexdigest()[:16], b0 == wt))
    print()

    # ══ §零-3 態錨之復現 ══
    print("══ `§零-3` 態錨之復現（`恆常附款 f`·二值並列） ══")
    tracked = g(["ls-tree", "-r", "--name-only", REV]).stdout.decode().splitlines()
    docs = [x for x in tracked if x.startswith("docs/")]
    vout = [x for x in tracked if x.startswith("verify/out/")]
    sub = [x for x in tracked if re.match(r"^verify/.+/.+\.py$", x)]
    rows = [
        ("項 `3` 生產碼 `verify/` 頂層 `*.py`", 33,
         len([x for x in tracked if re.match(r"^verify/[^/]+\.py$", x)])),
        ("項 `3` 判別力 子層 `*.py`", 356, len(sub)),
        ("項 `7` 自誤簿列數", 10758, len(txt(LEDGER).splitlines())),
        ("項 `7` 恆常附款簿列數", 342, len(txt(BOOK).splitlines())),
        ("項 `8` 全倉追蹤", 2548, len(tracked)),
        ("項 `8` `.md`", 868, len(files)),
        ("項 `8` `docs/`", 842, len(docs)),
        ("項 `8` `verify/out/`", 989, len(vout)),
        ("`§五` 受詞檔列數", 423, len(txt(HANDOVER).splitlines())),
    ]
    for nm, exp, got in rows:
        print("  %-34s 單載 `%s`／實測 **`%s`**  %s"
              % (nm, exp, got, "🟢" if exp == got else "🩸 **相異·具名**"))
    for nm, path, exp in (("`GB` 簿 blob", GBB, "64e91c72779fe84e36a6b124711cdce7c6eba893"),
                          ("`K-6` 典 blob", K6, "3bc628dffb7688eaf9bba0618095d4f92680b099")):
        got = g(["rev-parse", "%s:%s" % (REV, path)]).stdout.decode().strip()
        print("  %-34s 單載 `%s…`／實測 **`%s…`**  %s"
              % (nm, exp[:16], got[:16], "🟢" if exp == got else "🔴"))
    print()

    # ══ §八 三數之當場重算 ══
    print("══ `§八` 三數之當場重算（`恆常附款 f` 後段） ══")
    book = txt(BOOK)
    names = []
    for c in NAME_F.findall(book):
        if c not in names:
            names.append(c)
    order = sorted(names, key=lambda s2: (len(s2), s2))
    idx = {c for c, _, _ in IDX_F.findall(book)}
    print("  受掃之款（框 ＝ 簿內款列之去重）＝ 單載 `28`／實測 **`%d`**  %s"
          % (len(order), "🟢" if len(order) == 28 else "🩸"))
    print("     列舉 ＝ %s" % " ".join(order))
    print("  🟢 施行 ＝ 單載 `21`／實測 **`%d`**  %s"
          % (len(DONE), "🟢" if len(DONE) == 21 else "🩸"))
    print("  ⚪ 不生 ＝ 單載 `7`／實測 **`%d`**  %s"
          % (len(NA), "🟢" if len(NA) == 7 else "🩸"))
    uni = sorted(set(DONE) | set(NA), key=lambda s2: (len(s2), s2))
    print("  `21 + 7` ＝ **`%d`**；二列舉之聯集 ＝ **`%d`** 個" % (len(DONE) + len(NA), len(uni)))
    print("  ⇒ 聯集 ＝ 簿內款名？ **%s** %s" % (uni == order, "🟢" if uni == order else "🔴"))
    print("     差集（簿∖表）＝ %s／（表∖簿）＝ %s"
          % (sorted(set(order) - set(uni)), sorted(set(uni) - set(order))))
    print("  🔒 重疊之檢（須空）：`DONE ∩ NA` ＝ %s" % sorted(set(DONE) & set(NA)))
    print("  🔒 索引（`ab②` 之受詞）：具索引形 `出處` 者 ＝ **`%d`**／缺 **`%d`** %s"
          % (len(idx), len([c for c in order if c not in idx]),
             "🟢" if len(idx) == len(order) else "🔴"))


if __name__ == "__main__":
    main()
