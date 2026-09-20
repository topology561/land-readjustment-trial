# -*- coding: utf-8 -*-
r"""W-G.9-318 補令五：**輕級**開工閘 `②`／`③`／`④` 之量測（唯讀）。

🔒 **恆常附款 `z`（本補令 `裁 4` 新立·本器即其首次施行）**：
   凡以人造哨兵充判別力[必為零]之造者，須**當場自證該哨兵確不在受詞之定義域中**
   ——**列舉該定義域並證哨兵 ⛔ 屬之**；⛔ 以「執行期組出」或「看起來不會出現」充之。

🔒 **恆常附款 `aa`（`§二` 新立）① 之遵守**：[必命中]之造須與受詢受詞**屬同一形族**
   ——本器之 `自誤 442`（同為自誤簿之定義列形）／`恆常附款 y`（同為簿內款列形）即是。
"""
import re
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"
REV = "549121b27beb6a34b3a6c823af43c78e37b0c7ee"
LEDGER = "docs/reports/W-G.9波_claude.ai側自誤登記.md"
BOOK = "docs/reports/W-G.9波_恆常附款登記表.md"
ORDER5 = "docs/orders/W-G.9-318_補令五_裁3之撤回與自誤443及恆常附款z_aa.md"

Z_DEF = re.compile(r"^#+[^0-9０-９\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?", re.M)
Z_RNG = re.compile(r"^#+[^\n]*?自誤[\s\u3000`]*`?([0-9]{1,4})`?[\s\u3000`]*[〜～\-–~]+[\s\u3000`]*`?([0-9]{1,4})`?", re.M)


def g(a):
    return subprocess.run(["git", "-c", "core.quotepath=false"] + a,
                          cwd=REPO, capture_output=True)


def text(path, rev=REV):
    p = g(["show", "%s:%s" % (rev, path)])
    return p.stdout.decode("utf-8") if p.returncode == 0 else None


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


def clause_domain(rev=REV):
    """本簿之款名定義域（`§一` 表之款列·⛔ `§二` 之定義處表）。"""
    t = text(BOOK, rev)
    sec = t[t.index("## `§一`"):t.index("## `§二`")]
    return sorted(set(re.findall(r"^\| `([a-z]{1,2})` \|", sec, re.M)))


def two_forms(plain, ticked, files, cache):
    res = {}
    for nm, tok in (("B 形", plain), ("C 形", ticked)):
        pat = re.compile(r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])")
        res[nm] = {(p, i) for p in files
                   for i, ln in enumerate(cache[p].splitlines(), 1) if pat.search(ln)}
    return res


def main():
    print("# `W-G.9-318` 補令五　輕級開工閘（唯讀）")
    print("開工態 ＝ `%s`" % REV)
    files = md_files()
    cache = {p: (text(p) or "") for p in files}
    own = {ORDER5}
    print("母體 ＝ 全倉追蹤 `.md` **`%d`** 檔（讀不到 `%d`）\n"
          % (len(files), sum(1 for p in files if not cache[p])))

    # ══ 閘 ②　號占用 ══
    print("══ 閘 `②`　號占用 ══")

    # ── 受詞一：自誤 443 ──
    dom = ziwu_domain()
    print("\n【受詞一】`自誤 443`")
    print("  🔒 `恆常附款 z` 之定義域列舉：自誤簿之**已鑄集**（正典框）")
    print("     基數 ＝ `%d`／`MIN` ＝ `%d`／`MAX` ＝ `%d`／缺號 ＝ %s"
          % (len(dom), min(dom), max(dom),
             sorted(set(range(min(dom), max(dom) + 1)) - dom)))
    print("     ⇒ `443` ∈ 定義域？ **%s**（須 `False` ⇒ 可鑄）" % (443 in dom))
    for lbl, n, need in (("受詢", 443, "＝ 0"), ("對照甲［必命中·同形族］", 442, "> 0")):
        r = two_forms("自誤 %d" % n, "`自誤 %d`" % n, files, cache)
        u = r["B 形"] | r["C 形"]
        ext = [(p, i) for p, i in sorted(u) if p not in own]
        print("  %-22s `自誤 %d`：B 形 `%d` 列／C 形 `%d` 列／聯集 `%d` 列"
              % (lbl, n, len(r["B 形"]), len(r["C 形"]), len(u)))
        print("      ⇒ 除本補令自身之產物外 ＝ **`%d`** 列（須 %s）%s"
              % (len(ext), need, [("%s:%d" % (p, i)) for p, i in ext[:3]]))
    # 哨兵：⛔ 執行期組出即算數——須證其⛔ 屬定義域（恆常附款 z）
    sent = None
    for cand in range(500, 900):
        if cand not in dom:
            sent = cand
            break
    r = two_forms("自誤 %d" % sent, "`自誤 %d`" % sent, files, cache)
    print("  對照乙［必為零］：哨兵（字面⛔ 出艙）")
    print("      🔒 `z` 之自證：該值 ∈ 已鑄集？ **%s**（枚舉 `%d` 個成員後判·⛔ 以「執行期組出」充證）"
          % (sent in dom, len(dom)))
    print("      ⇒ 全倉命中 B 形 `%d`／C 形 `%d` 列（須 `0`／`0`）"
          % (len(r["B 形"]), len(r["C 形"])))

    # ── 受詞二／三：恆常附款 z ／ aa ──
    cdom = clause_domain()
    print("\n【受詞二·三】`恆常附款 z` ／ `恆常附款 aa`")
    print("  🔒 `z` 之定義域列舉：本簿 `§一` 表之款名 ＝ `%d` 個 ⇒ %s" % (len(cdom), cdom))
    for nm in ("z", "aa"):
        print("     ⇒ `%s` ∈ 定義域？ **%s**（須 `False` ⇒ 可立）" % (nm, nm in cdom))
    f_def = [re.compile(r"立為恆常附款[^\n]{0,20}?`([a-z]{1,2})`"),
             re.compile(r"恆常附款 `([a-z]{1,2})` [：＝]"),
             re.compile(r"^[>\s]*[（(]\s*`?([a-z]{1,2})`?\s*[）)]", re.M)]
    hits = {}
    for p in files:
        for fr in f_def:
            for m in fr.finditer(cache[p]):
                hits.setdefault(m.group(1), set()).add(p)
    for nm, need in (("z", "＝ 0"), ("aa", "＝ 0"), ("y", "> 0")):
        ext = sorted(hits.get(nm, set()) - own)
        tag = "對照甲［必命中·同形族］" if nm == "y" else "受詢"
        print("  %-22s `恆常附款 %s`：定義形之檔命中 ＝ **`%d`**（須 %s）%s"
              % (tag, nm, len(ext), need, ext[:2]))
    # 哨兵：須證⛔ 屬款名定義域
    csent = next(c for c in ("ab", "ac", "ad") if c not in cdom and c not in ("z", "aa"))
    print("  對照乙［必為零］：哨兵（字面⛔ 出艙）")
    print("      🔒 `z` 之自證：該名 ∈ 定義域（含本批將立之 `z`／`aa`）？ **%s**"
          % (csent in set(cdom) | {"z", "aa"}))
    print("      ⇒ 定義形之檔命中 ＝ `%d`（須 `0`）" % len(hits.get(csent, set())))

    # ══ 閘 ③　只數被追加之該一簿 ══
    print("\n══ 閘 `③`　被追加之簿（⛔ 數他簿） ══")
    print("  自誤簿　相異 ＝ `%d`／MAX ＝ `%d`" % (len(dom), max(dom)))
    print("  恆常附款簿　`§一` 表之款數 ＝ `%d`（%s）" % (len(cdom), "".join(cdom)))
    print("  🩸 **與單 `§一` 閘所載之相異**：單載「款數 `23` → `25`（增 `z`／`aa`）」，")
    print("     而本簿現有 **`%d`** 款（`a`〜`y`·含補令四 `§四` 所立之 `x`／`y`）" % len(cdom))
    print("     ⇒ 依 **恆常附款 `f`**（不符者以**列舉**為準並具名）：期末 ＝ `%d` ＋ `2` ＝ **`%d`**"
          % (len(cdom), len(cdom) + 2))

    # ══ 閘 ④　append-only 前綴（期初三值）══
    print("\n══ 閘 `④`　append-only 之期初（**三值化**·恆常附款 `x`） ══")
    for path in (BOOK, LEDGER, "docs/reports/W-G.9-318_CC側換手_一.md"):
        b0 = g(["show", "%s:%s" % (REV, path)]).stdout
        wt = open(REPO + "\\" + path.replace("/", "\\"), "rb").read()
        print("  %-44s 倉側 `%d` B／工作區 `%d` B／相同 %s"
              % (path.rsplit("/", 1)[-1][:42], len(b0), len(wt), b0 == wt))


if __name__ == "__main__":
    main()
