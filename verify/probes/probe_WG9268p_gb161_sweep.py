# -*- coding: utf-8 -*-
"""`GB-161` 全族掃描：倉內探針／工具之**硬編絕對路徑**與**樹相依**之判（補令十二 `§三-2`）。

🔒 **母體 ＝ `verify/**/*.py` 全體**（基數同格出艙）。
🛑 **含命中 `0` 之樣式**——`0` 亦須具名（⛔ 靜默）。
🛑 **本器只<u>登記</u>，⛔ 修任何檔**（補令十二 `§三-2` 明令）。

🔑 **樹相依之判準（機械·⛔ 推定·補令十二 `§二-1` 逐字）**
   同一倉之各 worktree **共用物件庫** ⇒ `git -C <任一樹> cat-file blob <完整 SHA>` **與樹無關**；
   惟 `<rev>:<path>` 之 `rev` 若為**分支名或 `HEAD`**，其解析為**該樹之 `HEAD`** ⇒ **樹相依**。
   ⇒ 本器逐支現查其 `spec`／`REV` 之**實際形**，⛔ 以「有 `git -C`」逕判。

用法：`python verify/probes/probe_WG9268p_gb161_sweep.py [倉根]`
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.join(REPO, "verify")

# ── 樣式（正面列舉·⛔ 全倉排除式）──────────────────────────────
PATS = [
    # 🩸 **⛔ 要求其後緊接分隔符**（本器首版之自捕）：`c1_synth` 之路徑**跨二源碼列**
    #    （`…worktrees"` ／ `r"/w-g-…"`）⇒ 舊式 `worktrees[/\\]` 於該列**不命中**
    #    ⇒ **漏抓了 `GB-161` 之起因那一支**。今放寬為裸字樣。
    ("worktrees", re.compile(r"worktrees")),
    ("os.chdir(", re.compile(r"os\.chdir\(")),
    ("git -C", re.compile(r'["\']-C["\']|git\s+-C')),
    ("絕對路徑 C:/ 或 C:\\\\", re.compile(r"[Cc]:[/\\]{1,2}Users")),
]
# 🔑 對照組（證掃描器非紅）
CTL_HI = ("import os", re.compile(r"^import os", re.M))          # 須 > 0
CTL_LO = ("⟨執行期組出之必不存在字樣⟩",
          re.compile(re.escape("ZZ" + "NO" + "SUCH" + "PAT" + "TERN")))   # 須 = 0
# 🔴 **必命中之對照（本類之已知成員）**——⛔ 只放「必不命中」之乙組：
#    乙組只證器能歸零，**⛔ 證其撈得到本類**。本器首版即因缺本組而漏抓。
CTL_MUST = "verify/probes/probe_WG9268p_c1_synth.py"


def pyfiles():
    out = []
    for dp, _dn, fn in os.walk(ROOT):
        if "__pycache__" in dp:
            continue
        for f in fn:
            if f.endswith(".py"):
                out.append(os.path.join(dp, f))
    return sorted(out)


files = pyfiles()
texts = {}
for p in files:
    try:
        texts[p] = io.open(p, encoding="utf-8").read()
    except Exception:                                               # noqa: BLE001
        texts[p] = ""

rel = lambda p: os.path.relpath(p, REPO).replace("\\", "/")         # noqa: E731

print("=" * 118)
print("【`GB-161`】全族掃描：硬編絕對路徑 ／ 他窗 worktree ／ 樹相依")
print("=" * 118)
print("三軸 (1) 來源 ＝ 工作區（`%s`）" % rel(ROOT))
print("三軸 (2) 母體 ＝ `verify/**/*.py` **%d** 支（⛔ `__pycache__`）" % len(files))
print("三軸 (3) 粒度框 ＝ 檔框 ＋ 列框")
print()

print("── 逐樣式之命中（**含命中 `0`**）──")
hits_by_pat = {}
for name, rx in PATS:
    h = []
    for p, t in texts.items():
        for i, ln in enumerate(t.split("\n"), 1):
            if rx.search(ln):
                h.append((rel(p), i, ln.strip()))
    hits_by_pat[name] = h
    print("   樣式 `%-22s` ⇒ 檔 **%d**／列 **%d**%s"
          % (name, len({x[0] for x in h}), len(h),
             "　🟡 **命中 `0`·具名**" if not h else ""))
print()

for role, (name, rx) in (("須 > 0", CTL_HI), ("須 = 0", CTL_LO)):
    n = sum(1 for t in texts.values() if rx.search(t))
    print("🔑 對照組（%s）`%s` ⇒ 檔 **%d** %s"
          % (role, name, n, "✅" if ((n > 0) == (role == "須 > 0")) else "🔴 **掃描器紅**"))
must = [x for x in hits_by_pat["worktrees"] if x[0] == CTL_MUST]
print("\U0001f534 對照組（**必命中**·本類之已知成員）`%s` ⇒ 列 **%d** %s"
      % (CTL_MUST, len(must),
         "✅ **撈得到本類**" if must else "🛑 **掃描器紅**（框漏抓本類之已知成員）"))
print()

# ── 逐支：指向他窗 worktree 者 ─────────────────────────────────
THIS = os.path.abspath(REPO).replace("\\", "/").rstrip("/")
print("=" * 118)
print("【逐支】硬編 `worktrees/` 之支（**逐支載：所指之樹／用法／樹相依之判**）")
print("=" * 118)
wt = {}
for p, i, ln in hits_by_pat["worktrees"]:
    wt.setdefault(p, []).append((i, ln))
if not wt:
    print("   🟡 **命中 `0`** ⇒ 具名（⛔ 靜默）")
for p in sorted(wt):
    t = texts[os.path.join(REPO, p.replace("/", os.sep))]
    tgt = set(re.findall(r"worktrees[/\\]([A-Za-z0-9_.\-]+)", t))
    chdir = "os.chdir(" in t
    gitc = bool(re.search(r'["\']-C["\']', t))
    # `rev:path` 之形（樹相依之關鍵）
    specs = re.findall(r'["\']([^"\']*\{[A-Za-z_]+\}[^"\']*:[^"\']*)["\']', t)
    revs = re.findall(r'^\s*(REV|SPEC|FROZEN|BASE)\s*=\s*(.+)$', t, re.M)
    others = sorted(x for x in tgt
                    if x and x not in os.path.basename(THIS))
    dep = "**是**" if (chdir or ("verify/out" in t and others)) else "**待判**"
    if gitc and not chdir:
        dep = "**待判（`git -C`）**"
    print()
    print("── `%s`" % p)
    print("   所指之樹 ＝ %s" % (sorted(tgt) or "—"))
    print("   本倉之樹 ＝ %s" % os.path.basename(THIS))
    print("   用法：`os.chdir` ＝ %s ／ `git -C` ＝ %s ／ 讀寫 `verify/out` ＝ %s"
          % (chdir, gitc, "verify/out" in t))
    print("   樹相依之判 ＝ %s" % dep)
    for i, ln in wt[p][:4]:
        print("     :%d ｜ %s" % (i, ln[:120]))
    if revs:
        print("   🔑 `REV`／`SPEC` 之**實際形**（樹相依之關鍵·⛔ 以「有 `git -C`」逕判）：")
        for k, v in revs[:6]:
            kind = ("**完整 SHA**（⇒ **樹無關**）" if re.search(r"[0-9a-f]{40}", v)
                    else "**分支名／`HEAD`**（⇒ **樹相依**）" if re.search(r"HEAD|wip/|main", v)
                    else "**待人工判**")
            print("      %s = %s　⇒ %s" % (k, v.strip()[:80], kind))
    if specs:
        print("   🔑 `<rev>:<path>` 之形：%s" % specs[:3])

print()
print("=" * 118)
print("🛑 **本器只登記·⛔ 修任何檔**（補令十二 `§三-2`）")
print("=" * 118)
