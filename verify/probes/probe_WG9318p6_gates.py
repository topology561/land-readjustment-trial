# -*- coding: utf-8 -*-
r"""W-G.9-318 補令六：**輕級**開工閘 `②`／`③`／`④` ＋ `§一` 之索引閘（唯讀）。

🔒 `恆常附款 z`：哨兵須**列舉定義域並證 ∉**，⛔ 以「執行期組出」充證。
🔒 `恆常附款 ab②`（本補令新立·本器即其首次施行）：凡可由**正典索引**直接取得之物，
   ⛔ 以文字搜框取之 ⇒ 本器查款之條文一律經簿之 `出處` 欄取 `檔:列` 後以檔案管線取之。
🔒 `裁 1` 之款名框（逐字）＝ 簿內 `^\|\s*`([a-z]{1,2})`\s*\|` 之去重。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "174b0be1841125b14ed31267aebd0d274915c10f"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
ORDER6 = "docs/orders/W-G.9-318_補令六_款數更正與正典索引之確立及自誤444.md"

NAME_F = re.compile(r"^\|\s*`([a-z]{1,2})`\s*\|", re.M)          # 裁 1 之框（逐字）
Z_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
Z_RNG = re.compile(r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
SRC_F = re.compile(r"^### 款 `([a-z]{1,2})`　出處 ＝ `([^`]+):(\d+)`(?:–`:(\d+)`)?", re.M)


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def text(p, rev=REV):
    r = g(["show", "%s:%s" % (rev, p)])
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def md_files(rev=REV):
    return [x for x in g(["ls-tree", "-r", "--name-only", rev]).stdout
            .decode("utf-8").splitlines() if x.endswith(".md")]


def ziwu_domain(rev=REV):
    t = text(LEDGER, rev)
    s = set(int(x) for x in Z_DEF.findall(t))
    for a, b in Z_RNG.findall(t):
        a, b = int(a), int(b)
        if b > a and b - a < 40:
            s.update(range(a, b + 1))
    return s


def two_forms(plain, ticked, files, cache):
    out = {}
    for nm, tok in (("B 形", plain), ("C 形", ticked)):
        pat = re.compile(r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])")
        out[nm] = {(p, i) for p in files
                   for i, ln in enumerate(cache[p].splitlines(), 1) if pat.search(ln)}
    return out


def main():
    print("# `W-G.9-318` 補令六　輕級開工閘（唯讀）")
    print("開工態 ＝ `%s`" % REV)
    files = md_files()
    cache = {p: (text(p) or "") for p in files}
    own = {ORDER6}
    print("母體 ＝ 全倉追蹤 `.md` **`%d`** 檔（讀不到 `%d`）\n"
          % (len(files), sum(1 for p in files if not cache[p])))

    book = text(BOOK)
    names = []
    for c in NAME_F.findall(book):
        if c not in names:
            names.append(c)
    order = sorted(names, key=lambda s: (len(s), s))

    # ══ 閘 ②　號占用 ══
    print("══ 閘 `②`　號占用（`恆常附款 z`：先列舉定義域·⛔ 以「執行期組出」充證） ══")
    dom = ziwu_domain()
    print("\n【受詞一】`自誤 444`")
    print("  定義域 ＝ 自誤簿已鑄集：基數 `%d`／MIN `%d`／MAX `%d`／缺號 %s"
          % (len(dom), min(dom), max(dom),
             sorted(set(range(min(dom), max(dom) + 1)) - dom)))
    print("  ⇒ `444` ∈ 定義域？ **%s**（須 `False`）" % (444 in dom))
    for lbl, n, need in (("受詢", 444, "＝ 0"), ("對照甲［必命中·同形族］", 443, "> 0")):
        r = two_forms("自誤 %d" % n, "`自誤 %d`" % n, files, cache)
        u = r["B 形"] | r["C 形"]
        ext = [(p, i) for p, i in sorted(u) if p not in own]
        print("  %-22s `自誤 %d`：B `%d`／C `%d`／聯集 `%d` ⇒ 除本補令自身之產物外 **`%d`**（須 %s）"
              % (lbl, n, len(r["B 形"]), len(r["C 形"]), len(u), len(ext), need))
    sent = next(c for c in range(500, 900) if c not in dom)
    r = two_forms("自誤 %d" % sent, "`自誤 %d`" % sent, files, cache)
    print("  對照乙［必為零］哨兵（字面⛔ 出艙）：∈ 已鑄集？ **%s**（枚舉 `%d` 成員後判）"
          % (sent in dom, len(dom)))
    print("      ⇒ 全倉 B `%d`／C `%d`（須 `0`／`0`）" % (len(r["B 形"]), len(r["C 形"])))

    print("\n【受詞二】`恆常附款 ab`")
    print("  定義域 ＝ 簿內款名（`裁 1` 之框·去重）＝ **`%d`** 個 ⇒ %s" % (len(order), order))
    print("  ⇒ `ab` ∈ 定義域？ **%s**（須 `False`）" % ("ab" in order))
    f_def = [re.compile(r"立為恆常附款[^\n]{0,20}?`([a-z]{1,2})`"),
             re.compile(r"恆常附款 `([a-z]{1,2})` [：＝]"),
             re.compile(r"^[>\s]*[（(]\s*`?([a-z]{1,2})`?\s*[·`）)]", re.M)]
    hits = {}
    for p in files:
        for fr in f_def:
            for m in fr.finditer(cache[p]):
                hits.setdefault(m.group(1), set()).add(p)
    for nm, need in (("ab", "＝ 0"), ("aa", "> 0")):
        ext = sorted(hits.get(nm, set()) - own)
        print("  %-22s `恆常附款 %s`：定義形之檔命中 **`%d`**（須 %s）%s"
              % ("受詢" if nm == "ab" else "對照甲［必命中·同形族］", nm, len(ext), need, ext[:2]))
    csent = next(c for c in ("ac", "ad", "ae") if c not in order and c != "ab")
    print("  對照乙［必為零］哨兵：∈ 定義域 ∪ {`ab`}？ **%s** ⇒ 定義形之檔命中 `%d`（須 `0`）"
          % (csent in set(order) | {"ab"}, len(hits.get(csent, set()))))

    # ══ 閘 ③　被追加之簿 ══
    print("\n══ 閘 `③`　被追加之簿（⛔ 數他簿） ══")
    print("  自誤簿　相異 `%d`／MAX `%d`" % (len(dom), max(dom)))
    print("  恆常附款簿　款名（`裁 1` 之框·去重）＝ **`%d`**（與 `裁 1` 所載之 `27` %s）"
          % (len(order), "相符 🟢" if len(order) == 27 else "🔴 不符"))

    # ══ §一 之索引閘：出處欄非空 ══
    print("\n══ `§一` 索引閘　逐款 `出處` 欄**非空**（`恆常附款 ab②` 之受詞） ══")
    src = {c: (f, int(a), int(b) if b else int(a)) for c, f, a, b in SRC_F.findall(book)}
    miss = [c for c in order if c not in src]
    print("  簿 `§三` 具 `出處` 節題者 ＝ **`%d`** 款；款名總數 ＝ `%d`；**缺 `出處` 者 ＝ `%d`** %s"
          % (len(src), len(order), len(miss), miss or "🟢"))
    # 抽驗 5 款：經索引取條文（⛔ 文字搜框）
    print("\n  抽驗 `5` 款（**經索引取 `檔:列` 後以檔案管線取之**·⛔ 文字搜框·`ab②`）：")
    ok = 0
    for c in ["a", "e", "l", "u", "aa"]:
        if c not in src:
            print("    款 `%s`：🔴 ⛔ 索引" % c)
            continue
        f, a, b = src[c]
        lines = (text(f) or "").splitlines()
        got = lines[a - 1:b]
        good = bool(got) and any(ch.strip() for ch in got)
        ok += good
        print("    款 `%-2s`  `%s:%d`%s  取得 `%d` 列·非空 %s"
              % (c, f.rsplit("/", 1)[-1][:36], a, ("–`:%d`" % b) if b > a else "",
                 len(got), "🟢" if good else "🔴"))
    print("  ⇒ 相符 `%d`／`5`" % ok)

    # ══ 閘 ④　append-only 期初 ══
    print("\n══ 閘 `④`　`append-only` 之期初（**三值化**·`恆常附款 x`） ══")
    for path in (BOOK, LEDGER, "docs/reports/W-G.9-318_CC側換手_一.md"):
        b0 = g(["show", "%s:%s" % (REV, path)]).stdout
        wt = open(REPO + "\\" + path.replace("/", "\\"), "rb").read()
        print("  %-42s 倉側 `%d` B／工作區 `%d` B／相同 %s"
              % (path.rsplit("/", 1)[-1][:40], len(b0), len(wt), b0 == wt))


if __name__ == "__main__":
    main()
