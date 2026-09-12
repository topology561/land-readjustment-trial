# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令三 序 `1`：`自誤 368`〜`371` 之**取號現查**（定義框求 MAX ＋ 意指占用二形並取）。

🔒 **取最大號一律用<u>定義列式</u>**（`常規四（八）`）——⛔ 裸框；
   母體 ＝ `docs/reports/W-G.9波_claude.ai側自誤登記.md` **單檔**（`W-G.9-192-PRE-b 🔧 一`）；
   框 ＝ `VR-091 四` 之**定義框 ＋ 範圍框**（`W-G.9-214`／`W-G.9-215`：`:779` 寬形⛔ 再用）。

🔒 **意指占用之搜尋**（`常規四（七）二`）——母體 ＝ **全倉**；
   **二形並取**（`常規四（七）補款二` ＋ `GB-158`）：`自誤 N` ⋀ `` `自誤 N` ``；
   **錨定框**（補款一）：`(?<![0-9\\-])…(?![0-9])`。
   🛑 **逐筆歸類**（`裁 H`）：命中數本身⛔ 判準，係待歸類之材料。

🔒 **對照組二造**（`常規五`）：甲 ＝ 一**已知已鑄**之號（須 `≥1`）／
   乙 ＝ 一**人造哨兵**（**執行期組出**·字面⛔ 出艙·`GB-147`·以 `⟨NEG⟩` 代稱）須 `=0`。

用法：`python verify/probes/probe_WG9270R4_ziwu_occ.py <rev> [倉根]`
`rc`：`0`／`5` **量測器紅**（二造不如預期）。
"""
import os
import re
import subprocess
import sys

REV = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.dirname(HERE))

BT = chr(96)
W = 112
BOOK = "docs/reports/W-G.9波_claude.ai側自誤登記.md"

# 🔒 `VR-091 四` 之定義框 ＋ 範圍框（逐字·⛔ `:779` 寬形）
F_DEF = re.compile(r'^#+[^0-9０-９\n]*?自誤[\s　`]*`?([0-9]{1,4})`?', re.M)
F_RNG = re.compile(
    r'^#+[^\n]*?自誤[\s　`]*`?([0-9]{1,4})`?[\s　`]*[〜～\-–~]+[\s　`]*`?([0-9]{1,4})`?', re.M)
# 🔒 靜態清單（已鑄而定義框結構上撈不到·⛔ 得列為缺號·`CLAUDE.md` 之「自誤簿首六則」節）
STATIC = set(range(1, 7))


def say(s=""):
    print(s)


def git_show(path):
    r = subprocess.run(["git", "show", "%s:%s" % (REV, path)], capture_output=True)
    if r.returncode != 0:
        return None
    try:
        return r.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None


def tracked(pat):
    r = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", REV],
                       capture_output=True, check=True)
    return [f for f in r.stdout.decode("utf-8").split("\0") if f and f.endswith(pat)]


def main():
    say("=" * W)
    say("【`W-G.9-270` 補令三 序 `1`】`自誤` 之取號現查（態 ＝ `%s`）" % REV[:12])
    say("=" * W)

    # ── 一　定義框求 MAX（母體 ＝ 登記表單檔）─────────────────────────
    t = git_show(BOOK)
    if t is None:
        say("🛑 `%s` ⛔ 可讀 ⇒ loud 拒測" % BOOK)
        sys.exit(3)
    s = set()
    for m in F_DEF.finditer(t):
        s.add(int(m.group(1)))
    nr = 0
    for m in F_RNG.finditer(t):
        a, b = int(m.group(1)), int(m.group(2))
        nr += 1
        for i in range(min(a, b), max(a, b) + 1):
            s.add(i)
    mx, mn = max(s), min(s)
    miss = sorted(set(range(mn, mx + 1)) - s - STATIC)
    say("── 一　**定義框**求 MAX（`常規四（八）`：⛔ 裸框）──")
    say("   母體 ＝ `%s` **單檔**（`%d` B／`%d` 列）" % (BOOK, len(t.encode("utf-8")), t.count("\n")))
    say("   框 ＝ `VR-091 四` 之**定義框 ＋ 範圍框**（逐字見本器 docstring·⛔ `:779` 寬形）")
    say("   相異 ＝ **%d**（範圍框之標題 %d 條）／**MAX ＝ %d**／MIN ＝ %d" % (len(s), nr, mx, mn))
    say("   缺號集 `[MIN..MAX]`（已扣靜態清單 `1`–`6`）＝ %s" % miss)
    say("   ⇒ **次號 ＝ %d**" % (mx + 1))

    # ── 二　意指占用（全倉·二形並取·錨定框）──────────────────────────
    say("")
    say("── 二　**意指占用**（母體 ＝ 全倉追蹤 `.md`·**二形並取**·錨定框）──")
    md = tracked(".md")
    texts = []
    unread = 0
    for p in md:
        x = git_show(p)
        if x is None:
            unread += 1
        else:
            texts.append((p, x))
    say("   母體 ＝ 追蹤 `.md` **%d** 檔（讀不到 %d）" % (len(md), unread))

    CTL_A = mx                                     # 對照甲：已知已鑄（須 ≥1）
    CTL_B = 9000 + 431                             # 對照乙：人造哨兵（執行期組出·字面⛔ 出艙）
    targets = [(n, "受詢") for n in (368, 369, 370, 371)]
    targets += [(CTL_A, "對照甲·已鑄·須 ≥1"), (CTL_B, "對照乙·人造·須 =0")]

    res = {}
    say("   %-8s %-22s %-12s %-12s %s" % ("號", "角色", "裸形 列", "C形 列", "檔數(聯集)"))
    for n, role in targets:
        bare = re.compile(r"(?<![0-9\-])自誤\s*%d(?![0-9])" % n)
        cfrm = re.compile(r"(?<![0-9\-])" + re.escape(BT) + r"自誤\s*%d" % n + re.escape(BT))
        hb, hc, files = [], [], set()
        for p, x in texts:
            for i, line in enumerate(x.split("\n"), 1):
                if bare.search(line):
                    hb.append((p, i, line))
                    files.add(p)
                if cfrm.search(line):
                    hc.append((p, i, line))
                    files.add(p)
        res[n] = (hb, hc, files)
        shown = "⟨NEG⟩" if n == CTL_B else str(n)
        say("   %-8s %-22s %-12d %-12d %d" % (shown, role, len(hb), len(hc), len(files)))

    ok_a = len(res[CTL_A][0]) >= 1 or len(res[CTL_A][1]) >= 1
    ok_b = len(res[CTL_B][0]) == 0 and len(res[CTL_B][1]) == 0
    say("   【量測器自證】對照甲(須≥1) ⇒ %s ／ 對照乙(須=0) ⇒ %s"
        % ("✅" if ok_a else "🔴", "✅" if ok_b else "🔴"))
    if not (ok_a and ok_b):
        say("   🛑 **量測器紅** ⇒ ⛔ 出艙任何判")
        sys.exit(5)

    # ── 三　受詢之逐筆歸類（`裁 H`）────────────────────────────────
    say("")
    say("── 三　受詢之**逐筆歸類**（`裁 H` 二：命中數本身⛔ 判準）──")
    for n in (368, 369, 370, 371):
        hb, hc, files = res[n]
        allh = {}
        for p, i, line in hb + hc:
            allh[(p, i)] = line
        say("   **`自誤 %d`** ⇒ 命中 **%d** 筆（%d 檔）" % (n, len(allh), len(files)))
        for (p, i), line in sorted(allh.items()):
            say("      %s:%d" % (p, i))
            say("         %s" % line.strip()[:140])
        if not allh:
            say("      （無）")
    sys.exit(0)


if __name__ == "__main__":
    main()
