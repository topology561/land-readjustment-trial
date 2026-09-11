# -*- coding: utf-8 -*-
"""`W-G.9-268′` 序 `4`：六號之**意指占用查**（補令九 `§一-2`：**二形並取** ＋ 對照組逐形出艙）。

🔒 **框（`常規四（七）` 補款一 錨定框 ＋ 補款二 二形並取）**
   `B` 形 ＝ `` <前綴> `N` ``（反引號只包號）
   `C` 形 ＝ `` `<前綴> N` ``（反引號包全 token·**本倉現行標題形**）
   併報**鬆框** `<前綴> N`（僅作漏框偵察·⛔ 為判準）。
   皆帶數字邊界 `(?<![0-9\\-])…(?![0-9])`。

🛑 **`GB-158` 之受詞**：`B` 形於本倉對**已知占用之對照組**皆得 `0` ⇒ **⛔ 單獨採信**。
   本器**逐形出艙對照組之命中**，使該事實於每次取號時可見。

母體 ＝ **全倉追蹤檔**（意指占用之母體係全倉·⛔ 單檔）。
用法：`python verify/probes/probe_WG9268p_occ6.py <REV>`
"""
import re
import subprocess
import sys

REV = sys.argv[1]

TARGETS = [("自誤", 343), ("自誤", 344), ("自誤", 345),
           ("GB", 158), ("GB", 159), ("GB", 160)]
# 🔒 得由 `argv[2:]` 覆寫受詢集（形 ＝ `<前綴>:<號>`）；⛔ 改對照組與框。
if len(sys.argv) > 2:
    TARGETS = [(s.split(":")[0], int(s.split(":")[1])) for s in sys.argv[2:]]
CONTROL_HI = [("自誤", 341), ("自誤", 340), ("GB", 157), ("GB", 156)]   # 須 ≥1
# 🩸 **哨兵之號⛔ 得為字面**（`GB-147`／`CLAUDE.md`：哨兵字樣宜**於執行期組出**，
#    ⛔ 使其字面落入任何檔或 log）——本器初版寫死一個號並隨本檔入倉，
#    致該號於次批之查中由**真零**變為**非零**（自捕·`W-G.9-268′ 補令十一 序 `1``）。
#    ⇒ 改為**執行期自倉內掃出**一個三形皆 `0` 之號；其字面**⛔ 出艙**，一律以代稱 `⟨NEG⟩` 指之。
CONTROL_LO_RANGE = (9000, 9999)


def files():
    out = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", REV],
                         capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8").split("\0") if p]


def blob(p):
    r = subprocess.run(["git", "show", "%s:%s" % (REV, p)], capture_output=True)
    if r.returncode != 0:
        return None, "git"
    try:
        return r.stdout.decode("utf-8"), None
    except UnicodeDecodeError:
        return None, "dec"


def frames(pre, n):
    sep = " " if pre == "自誤" else "-"
    tok = "%s%s%d" % (pre, sep, n)
    return [
        ("B 形 <前綴>`N`", re.compile(r"(?<![0-9\-])%s%s`%d`(?![0-9])"
                                     % (re.escape(pre), re.escape(sep), n))),
        ("C 形 `<前綴> N`", re.compile(r"`%s`" % re.escape(tok))),
        ("鬆框（偵察）", re.compile(r"(?<![0-9\-])%s(?![0-9])" % re.escape(tok))),
    ]


fl = files()
texts = {}
gf = df = 0
for p in fl:
    t, why = blob(p)
    if t is None:
        gf += 1 if why == "git" else 0
        df += 1 if why == "dec" else 0
    else:
        texts[p] = t

print("三軸 (1) 來源 ＝ %s" % REV)
print("三軸 (2) 母體 ＝ 全倉追蹤檔 %d 檔（讀不到 %d ＝ git失敗 %d ＋ 解碼失敗 %d）"
      % (len(fl), gf + df, gf, df))
print("三軸 (3) 粒度框 ＝ 檔框 ＋ 列框（錨定框·三形分列）")
print()


def scan(pre, n, verbose=False):
    out = {}
    for fname, rx in frames(pre, n):
        hits = []
        for p, t in texts.items():
            for i, line in enumerate(t.split("\n"), 1):
                if rx.search(line):
                    hits.append((p, i, line.strip()))
        out[fname] = hits
    return out


def show(pre, n, role, verbose=False):
    r = scan(pre, n)
    cells = []
    for fname in ("B 形 <前綴>`N`", "C 形 `<前綴> N`", "鬆框（偵察）"):
        h = r[fname]
        cells.append("%s 檔=%d 列=%d" % (fname, len({x[0] for x in h}), len(h)))
    print("   %-12s %s ｜ %s" % ("%s %d" % (pre, n), " ｜ ".join(cells), role))
    if verbose:
        seen = set()
        for fname in ("B 形 <前綴>`N`", "C 形 `<前綴> N`", "鬆框（偵察）"):
            for p, i, line in r[fname]:
                if (p, i) in seen:
                    continue
                seen.add((p, i))
                print("        %s:%d ｜ %s" % (p, i, line[:150]))
    return r


print("── 受詢之六號（逐筆歸類·`裁 H`：命中係待歸類之材料·⛔ 判準）──")
res = {}
for pre, n in TARGETS:
    res[(pre, n)] = show(pre, n, "受詢", verbose=True)
print()
print("── 對照組 甲（已知占用·須 `≥1`）──")
hi = {}
for pre, n in CONTROL_HI:
    hi[(pre, n)] = show(pre, n, "甲（須 ≥1）")
print()
print("── 對照組 乙（人造·**執行期自倉掃出**·須 `=0`·其號⛔ 出艙·代稱 `⟨NEG⟩`）──")
lo_ok = {}
for pre in ("自誤", "GB"):
    picked = None
    for cand in range(CONTROL_LO_RANGE[0], CONTROL_LO_RANGE[1] + 1):
        r = scan(pre, cand)
        if all(len(v) == 0 for v in r.values()):
            picked = cand
            break
    if picked is None:
        print("   %-4s ⟨NEG⟩ 🛑 於 `%d`–`%d` 內**無**三形皆 `0` 之號 ⇒ **loud 拒測**"
              % (pre, CONTROL_LO_RANGE[0], CONTROL_LO_RANGE[1]))
        lo_ok[pre] = False
        continue
    lo_ok[pre] = True
    print("   %-4s ⟨NEG⟩（執行期選出·字面⛔ 出艙）　B 形 檔=0 列=0 ｜ C 形 檔=0 列=0 ｜ 鬆框 檔=0 列=0 ｜ ✅ 乙（須 =0）"
          % pre)
print("   🔒 **⟨NEG⟩ 之三形皆 `0` ⇒ 量測器能歸零**（⛔ 恆非零）")
print()

print("🔑 **`GB-158` 之受詞（B 形之量測器紅）逐形出艙**")
for (pre, n), r in hi.items():
    b = len(r["B 形 <前綴>`N`"])
    c = len(r["C 形 `<前綴> N`"])
    print("   已知占用 %s %d ⇒ B 形 **%d** 列／C 形 **%d** 列 %s"
          % (pre, n, b, c, "🔴 **B 形為 0 ⇒ ⛔ 單獨採信**" if b == 0 else ""))
print()
bad = [k for k, r in hi.items() if len(r["C 形 `<前綴> N`"]) == 0]
print("   ⇒ 對照組甲於 **C 形** 皆非零？ %s" % ("✅ 是" if not bad else "🔴 否 %r" % bad))
