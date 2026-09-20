# -*- coding: utf-8 -*-
"""W-G.9-318 補令四 工項一：各單 `§一-1` 之逐字傾印（唯讀·⛔ 改寫）。

🔑 **第六形（本器之受詞）**：單之 `§一-1` 內之「🆕 **本單所增**…」區塊
   ——此形涵蓋 `a`〜`w` 之**全部**，而裁 `3` 之二形與第四形皆只覆其一部。
🛑 `常規七 一`：逐字交付塊之文字須由**檔案管線**直接產生，⛔ 憑記憶重寫。
"""
import subprocess
import sys

REPO = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-docs-196235"

SRC = [
    ("a b c", "docs/orders/W-G.9-308_補令一_K-9-38與K-9-39之鑄及自誤420至421與款4之靜態結案.md"),
    ("d", "docs/orders/W-G.9-310_施工單_K-9-40之鑄與三則末端註記及自誤422.md"),
    ("e f", "docs/orders/W-G.9-311_施工單_修批前置之現態診斷與自誤423_424.md"),
    ("g", "docs/orders/W-G.9-312_施工單_步驟0二態對拍與自誤425.md"),
    ("h i", "docs/orders/W-G.9-313_施工單_自誤426與312二態對拍之登記.md"),
    ("j k", "docs/orders/W-G.9-314_施工單_自誤427與428之鑄及恆常附款jk之立.md"),
    ("l", "docs/orders/W-G.9-315_施工單_K-9-5-12反事實之態乙驅動與自誤429.md"),
    ("m n", "docs/orders/W-G.9-316_施工單_W0消費者定位與項5補測及自誤430_431.md"),
    ("o", "docs/orders/W-G.9-317_施工單_K-9-41之鑄與落地前最後定位及自誤432.md"),
    ("p", "docs/orders/W-G.9-318_施工單_K-9-41①之落地與W0起算點之修及自誤433.md"),
    ("q r s t u", "docs/orders/W-G.9-318_補令一_forced側之避讓與自誤434至438.md"),
    ("v", "docs/orders/W-G.9-318_補令二_換窗前之保全與GB-171及自誤439_440.md"),
    ("w", "docs/orders/W-G.9-318_補令三_保全push之授權與四簿期值更正及自誤441.md"),
]


def run(a):
    return subprocess.run(a, cwd=REPO, capture_output=True)


def main():
    rev = sys.argv[1]
    print("態 ＝ `%s`" % run(["git", "rev-parse", rev]).stdout.decode().strip())
    for letters, path in SRC:
        p = run(["git", "show", "%s:%s" % (rev, path)])
        if p.returncode != 0:
            print("\n🔴 讀不到 %s" % path)
            continue
        lines = p.stdout.decode("utf-8").splitlines()
        print("\n" + "=" * 90)
        print("### 款 %s　來源 ＝ `%s`" % (letters, path))
        print("=" * 90)
        start = None
        for i, ln in enumerate(lines):
            if ln.startswith("#") and "§一-1" in ln:
                start = i
                break
        if start is None:
            print("  🔴 ⛔ `§一-1` 標題 ⇒ 改搜「本單所增」")
            for i, ln in enumerate(lines):
                if "本單所增" in ln:
                    start = i
                    break
        if start is None:
            print("  🔴 二法皆⛔ 命中")
            continue
        for j in range(start, min(start + 34, len(lines))):
            if j > start and lines[j].startswith("#") and "§一-1" not in lines[j]:
                break
            if j > start and lines[j].startswith("---"):
                break
            print("%5d| %s" % (j + 1, lines[j]))


if __name__ == "__main__":
    main()
