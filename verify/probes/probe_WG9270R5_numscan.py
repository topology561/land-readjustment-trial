# -*- coding: utf-8 -*-
"""`W-G.9-270R5`　取號現查：**意指占用**（全倉 `.md`·錨定框·**B 形 ⋀ C 形並取**）。

🔒 依據：`常規四（七）`（意指占用）＋其`補款一`（錨定框 `(?<![0-9\\-])<號>(?![0-9])`）
  ＋`補款二`（號之二形並取）＋`GB-158`（B 形於本倉對已知占用之對照組多得 `0`
  ⇒ **二形並取·各形之對照組須同格出艙**）。
🔒 **母體以 `git ls-tree -r HEAD` 取**——⛔ `grep -r … .`（該形恆含**未入倉之草稿**·`W-G.9-199` 常規補款 `二`）。
🔒 **取最大號 → 登記表單檔**（`W-G.9-192-PRE-b 🔧 一`）；**查占用 → 全倉**。本器專司後者。
🔒 **哨兵之字面⛔ 出艙**（`GB-147`）：其於**執行期組出**（字串串接）⇒ 本檔之完整字面命中為 `0`
  （判別力：同檔 `GB-` 命中 `4` ⇒ 該檢⛔ 恆為 `0`）；其框亦以代稱印出。
🛑 本器**全唯讀**：⛔ 寫任何生產碼、⛔ 寫 `verify/baselines`、⛔ 設 `WV_BAKE`。
"""
import re
import subprocess
import sys

REV = "HEAD"


def tracked_md():
    out = subprocess.run(
        ["git", "-c", "core.quotepath=false", "ls-tree", "-r", "--name-only", REV],
        capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return [p for p in out.splitlines() if p.endswith(".md")]


def blob(path):
    try:
        return subprocess.run(
            ["git", "cat-file", "blob", "%s:%s" % (REV, path)],
            capture_output=True, check=True).stdout.decode("utf-8", "replace")
    except subprocess.CalledProcessError:
        return None


def scan(files, pat):
    """回傳 [(檔, 列號, 列逐字)]"""
    rx = re.compile(pat)
    hits = []
    for f in files:
        t = blob(f)
        if t is None:
            print("  🔴 讀不到：%s" % f)
            continue
        for i, line in enumerate(t.splitlines(), 1):
            if rx.search(line):
                hits.append((f, i, line))
    return hits


def anchored(tok):
    """錨定框（補款一）：前後皆不得為數字或連字號"""
    return r"(?<![0-9\-])" + re.escape(tok) + r"(?![0-9])"


def report(name, pats, files, sample=0, hide_pat=False):
    print("\n── %s ──────────────────────────────" % name)
    allhits = {}
    for label, pat in pats:
        h = scan(files, pat)
        allhits[label] = h
        nf = len(set(x[0] for x in h))
        shown = "〔代稱·字面⛔ 出艙·GB-147〕" if hide_pat else pat
        print("   %-28s 檔 %4d ／ 列 %4d   框(逐字)= %s" % (label, nf, len(h), shown))
        if sample and h:
            for f, i, line in h[:sample]:
                print("       · %s:%d  %s" % (f, i, line.strip()[:140]))
    return allhits


def main():
    files = tracked_md()
    print("母體 ＝ %s 之追蹤 .md ＝ %d 檔" % (REV, len(files)))

    # 受詢二號
    for tok_b, tok_c, title in [
        ("GB-164", "`GB-164`", "受詢 GB-164"),
        ("自誤 368", "`自誤 368`", "受詢 自誤 368"),
    ]:
        report(title, [("B 形(裸·錨定)", anchored(tok_b)),
                       ("C 形(反引號包全 token)", anchored(tok_c))], files, sample=100)

    # 對照組甲（已知占用·須各形 >= 1）
    for tok_b, tok_c, title in [
        ("GB-165", "`GB-165`", "對照甲 GB-165(已鑄)"),
        ("自誤 371", "`自誤 371`", "對照甲 自誤 371(已鑄)"),
    ]:
        report(title, [("B 形(裸·錨定)", anchored(tok_b)),
                       ("C 形(反引號包全 token)", anchored(tok_c))], files)

    # 對照組乙（人造哨兵·執行期組出·字面⛔ 出艙·須 = 0）
    sen_b = "GB-" + str(9000 + 91)
    sen_c = "`" + sen_b + "`"
    report("對照乙 人造哨兵(字面⛔ 出艙)",
           [("B 形(裸·錨定)", anchored(sen_b)),
            ("C 形(反引號包全 token)", anchored(sen_c))], files, hide_pat=True)


if __name__ == "__main__":
    sys.exit(main())
