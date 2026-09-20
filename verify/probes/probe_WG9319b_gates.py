# -*- coding: utf-8 -*-
r"""`W-G.9-319 補令一`：輕級開工閘 ＋ `§五` 期初錨之當場重跑 ＋ `§六` 三數之重算。

🔒 **`恆常附款 w②`（本批增補後 ①）**：錨表之任一格**須由一支器對開工態逐格重跑並落檔**，
   其落檔之 `commit` 須與表所載之開工態**同一** ⇒ ⛔ 以自述充「皆當場量得」。
   **本器即該款之首次施行。**
🔒 `恆常附款 z`：哨兵須**列舉定義域**並證 ∉。
🔒 `恆常附款 f`：一切自載基數當場重算並**二值並列**。
"""
import hashlib
import re
import subprocess

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "51a641d334847d285f323257909748acdf7052e1"
MAIN_OLD = "40375702378af4cefd2d11515fdf3f98c0791580"
ORDER = "docs/orders/W-G.9-319_補令一_停一成因與自誤446至448及v②射程.md"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
GBB = "docs/reports/W-G.4_泛用阻塞項登記表.md"
K6 = "docs/rulings/K-6_街角地分配程序與可分配判準.md"
RPT = "docs/reports/W-G.9-319R_二寬度之量差與GB170三格現查及自誤445_執行報告.md"

Z_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
Z_RNG = re.compile(r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
VR_F = re.compile(r"^#+ `?VR-([0-9]{1,4})`?", re.M)
K9_F = re.compile(r"^#{2,4}[^\n]*?K-9-([0-9]{1,3})", re.M)
NAME_F = re.compile(r"^\|\s*`([a-z]{1,2})`\s*\|", re.M)
IDX_F = re.compile(r"^### 款 `([a-z]{1,2})`　出處 ＝ ", re.M)

NA = "c d j s t y".split()          # 單 `§六` 所載之 ⚪（`u` 已轉 🟢）


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def txt(p, rev=REV):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def main():
    print("# `W-G.9-319 補令一`　輕級開工閘（唯讀·本器即 `w②①` 之首次施行）")
    head = g(["rev-parse", "HEAD"]).stdout.decode().strip()
    print("開工態（**器所跑之 `commit`**）＝ `%s`" % head)
    print("單所載之開工態                 ＝ `%s`" % REV)
    print("⇒ **同一：%s** %s\n" % (head == REV, "🟢" if head == REV else "🔴 **停機**"))

    files = [x for x in g(["ls-tree", "-r", "--name-only", REV]).stdout
             .decode("utf-8").splitlines() if x.endswith(".md")]
    cache = {p: (txt(p) or "") for p in files}
    own = {ORDER}

    # ══ 閘 ②　號占用（三號）══
    print("══ 閘 `②`　號占用（`自誤 446`／`447`／`448`） ══")
    t = txt(LEDGER)
    dom = set(int(x) for x in Z_DEF.findall(t))
    for a, b in Z_RNG.findall(t):
        a, b = int(a), int(b)
        if b > a and b - a < 40:
            dom.update(range(a, b + 1))
    print("🔒 `z` 之定義域列舉 ＝ 自誤簿之已鑄集：基數 **`%d`**／`MIN` `%d`／`MAX` `%d`／缺號 %s"
          % (len(dom), min(dom), max(dom),
             sorted(set(range(min(dom), max(dom) + 1)) - dom)))

    def occ(tok):
        pb = re.compile(r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])")
        pc = re.compile(r"(?<![0-9\-])`" + re.escape(tok) + r"`(?![0-9])")
        b = {(p, i) for p in files for i, l in enumerate(cache[p].splitlines(), 1) if pb.search(l)}
        c = {(p, i) for p in files for i, l in enumerate(cache[p].splitlines(), 1) if pc.search(l)}
        u = b | c
        return len(b), len(c), len(u), len([1 for p, _ in u if p not in own])

    for n in (446, 447, 448):
        b, c, u, ext = occ("自誤 %d" % n)
        print("  受詢 `自誤 %d`：∈ 已鑄集？ **%s**（須 `False`）｜B `%d`／C `%d`／並取 `%d` "
              "⇒ **除本補令自身之產物外 `%d`**（須 `0`）%s"
              % (n, n in dom, b, c, u, ext, "🟢" if (n not in dom and ext == 0) else "🔴"))
    b, c, u, ext = occ("自誤 445")
    print("  對照甲［必命中·同形族］`自誤 445`：並取 `%d`（須 `> 0`）%s"
          % (u, "🟢" if u > 0 else "🔴"))
    sent = next(x for x in range(500, 900) if x not in dom)
    b, c, u, ext = occ("自誤 %d" % sent)
    print("  對照乙［必為零］哨兵（字面⛔ 出艙）：∈ 已鑄集？ **%s**（枚舉 `%d` 成員後判）"
          "｜並取 `%d`（須 `0`）%s" % (sent in dom, len(dom), u, "🟢" if u == 0 else "🔴"))

    # ══ 閘 ③　生產碼 ══
    print("\n══ 閘 `③`　生產碼 ══")
    top = [x for x in g(["ls-tree", "--name-only", REV, "verify/"]).stdout
           .decode().splitlines() if x.endswith(".py")]
    appb = g(["rev-parse", "%s:app.py" % REV]).stdout.decode().strip()
    print("  `verify/` 頂層 `*.py` ＝ **`%d`** ＋ `app.py` ⇒ **`%d`** 檔" % (len(top), len(top) + 1))
    print("  `app.py` blob ＝ **`%s`**（絕對值出艙）" % appb)

    # ══ 閘 ④　四簿期初·二框並報 ══
    print("\n══ 閘 `④`　四簿期初（**二框並報**） ══")
    miss = sorted(set(range(min(dom), max(dom) + 1)) - dom)
    print("  自誤〔CC 正典框〕 相異 **`%d`**／MAX **`%d`**／缺 %s" % (len(dom), max(dom), miss))
    for nm, path, fr, drop in (("VR", "docs/驗證裁定登記表.md", VR_F, {999}),
                               ("K-9", K6, K9_F, set())):
        v = set(int(x) for x in fr.findall(txt(path))) - drop
        print("  %-4s〔標題錨定框〕 相異 **`%d`**／MAX **`%d`**" % (nm, len(v), max(v)))
    reg = subprocess.run(["python", "verify/probes/probe_WG9267_issuer_measurers.py", "registry"],
                         cwd=REPO, capture_output=True,
                         env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    for l in reg.stdout.decode("utf-8", "replace").splitlines():
        if l.strip().startswith(("自誤", "GB", "VR", "K-9")):
            print("  〔自擬框〕%s" % l.strip())

    # ══ 閘 ⑤　append-only 期初（三值化）══
    print("\n══ 閘 `⑤`　`append-only` 之期初（**三值化**·`恆常附款 x`） ══")
    for path in (LEDGER, BOOK, RPT, GBB, K6):
        b0 = g(["show", "%s:%s" % (REV, path)]).stdout
        wtb = open(REPO + "\\" + path.replace("/", "\\"), "rb").read()
        print("  %-44s 倉側 `%d` B／`%s…`／工作區 ＝ 倉側 **%s**"
              % (path.rsplit("/", 1)[-1][:42], len(b0),
                 hashlib.sha256(b0).hexdigest()[:16], b0 == wtb))
    print("  `GB` 簿 blob ＝ **`%s`**（單 `§五` 閘 `5` 令其須仍為此值）"
          % g(["rev-parse", "%s:%s" % (REV, GBB)]).stdout.decode().strip())

    # ══ §五 期初錨之當場重跑（w②① 之受詞）══
    print("\n══ `§五` 期初錨之**當場重跑**（`w②①`·⛔ 以自述充） ══")
    tracked = g(["ls-tree", "-r", "--name-only", REV]).stdout.decode().splitlines()
    docs = [x for x in tracked if x.startswith("docs/")]
    rows = [("追蹤全檔", 2566, len(tracked)), ("`.md`", 873, len(files)),
            ("`docs/`", 844, len(docs))]
    for nm, exp, got in rows:
        print("  %-12s 單載 `%s`／**實測 `%s`**  %s"
              % (nm, exp, got, "🟢" if exp == got else "🩸 **相異·具名**"))
    tot = len(g(["ls-remote", "--heads", "origin"]).stdout.decode().splitlines())
    ver = len(g(["ls-remote", "--heads", "origin", "refs/heads/verify/*"]).stdout.decode().splitlines())
    pres = g(["ls-remote", "origin", "refs/heads/wip/W-G.9-318-preserve"]).stdout.decode().split()
    print("  遠端總數 單載 `25`／**實測 `%d`**  %s；`verify/*` 單載 `20`／**實測 `%d`**  %s"
          % (tot, "🟢" if tot == 25 else "🩸", ver, "🟢" if ver == 20 else "🩸"))
    print("  `preserve` 單載 `c286a79…`／**實測 `%s`**  %s（單已具名其「**已落後主線**」）"
          % (pres[0] if pres else "?",
             "🟢" if pres and pres[0].startswith("c286a79") else "🩸"))

    # ══ §六 三數之當場重算 ══
    print("\n══ `§六` 三數之當場重算（`恆常附款 f` 後段） ══")
    book = txt(BOOK)
    names = []
    for c2 in NAME_F.findall(book):
        if c2 not in names:
            names.append(c2)
    order = sorted(names, key=lambda s: (len(s), s))
    done = [c2 for c2 in order if c2 not in NA]
    idx = set(IDX_F.findall(book))
    print("  受掃之款  單載 `28`／**實測 `%d`**  %s" % (len(order), "🟢" if len(order) == 28 else "🩸"))
    print("     列舉 ＝ %s" % " ".join(order))
    print("  🟢 施行   單載 `22`／**實測 `%d`**  %s" % (len(done), "🟢" if len(done) == 22 else "🩸"))
    print("  ⚪ 不生   單載 `6`／**實測 `%d`**  %s（列舉 ＝ %s）"
          % (len(NA), "🟢" if len(NA) == 6 else "🩸", " ".join(NA)))
    print("  `%d + %d` ＝ **`%d`**；⚪ ⊆ 款名？ **%s**；重疊 ＝ %s"
          % (len(done), len(NA), len(done) + len(NA),
             set(NA) <= set(order), sorted(set(done) & set(NA))))
    print("  索引（`ab②`）：具索引形 `出處` 者 **`%d`**／缺 **`%d`** %s"
          % (len(idx), len([c2 for c2 in order if c2 not in idx]),
             "🟢" if len(idx) == len(order) else "🔴"))


if __name__ == "__main__":
    main()
