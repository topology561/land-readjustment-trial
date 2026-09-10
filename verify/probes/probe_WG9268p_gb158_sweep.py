# -*- coding: utf-8 -*-
"""`GB-158` 波及面掃描：全倉凡依 `常規四（七）補款二` 所作之**既往鑄號查**，逐處具名。

🔒 **受詞**：`常規四（七）補款二` 令意指占用之查須「`<前綴> N` 與 `` <前綴> `N` `` **二形並取**」。
   其 **B 形**（`` <前綴> `N` ``·反引號只包號）於本倉對**已知占用之對照組**多得 `0`
   ⇒ 單獨採 B 形者，其「未占用」之結論**⛔ 帶資訊**（量測器紅）。
🛑 **本掃描逐處出艙（含命中 `0`）**——`0` 亦須具名，⛔ 靜默。

**框（正面列舉·⛔ 全倉排除式）**：以下列字樣掃**全倉追蹤 `.md`**——
   `意指占用`／`二形並取`／`常規四（七）補款二`／`補款二`
用法：`python verify/probes/probe_WG9268p_gb158_sweep.py <REV>`
"""
import re
import subprocess
import sys

REV = sys.argv[1]

PATS = [
    ("意指占用", re.compile(r"意指占用")),
    ("二形並取", re.compile(r"二形並取")),
    ("常規四（七）補款二", re.compile(r"常規四（七）\s*補款二")),
    ("補款二", re.compile(r"補款二")),
]
# 🔑 對照組（證本掃描器非紅）
CTL_HI = ("常規四", re.compile(r"常規四"))          # 須 > 0
CTL_LO = ("⟨必不存在之字樣·執行期組出⟩",
          re.compile(re.escape("NOSUCH" + "-" + "SWEEP" + "-" + "TOKEN")))   # 須 = 0


def files():
    out = subprocess.run(["git", "ls-tree", "-r", "-z", "--name-only", REV],
                         capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8").split("\0")
            if p and p.endswith(".md")]


def blob(p):
    r = subprocess.run(["git", "show", "%s:%s" % (REV, p)], capture_output=True)
    if r.returncode != 0:
        return None
    try:
        return r.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None


fl = files()
texts = {}
unread = 0
for p in fl:
    t = blob(p)
    if t is None:
        unread += 1
    else:
        texts[p] = t

print("三軸 (1) 來源 ＝ %s" % REV)
print("三軸 (2) 母體 ＝ 全倉追蹤 `.md` %d 檔（讀不到 %d）" % (len(fl), unread))
print("三軸 (3) 粒度框 ＝ 檔框 ＋ 列框")
print()

for name, rx in PATS:
    hits = []
    for p, t in texts.items():
        for i, line in enumerate(t.split("\n"), 1):
            if rx.search(line):
                hits.append((p, i, line.strip()))
    print("── 字樣 `%s` ⇒ 檔 **%d**／列 **%d**%s"
          % (name, len({h[0] for h in hits}), len(hits),
             "　🟡 **命中 `0`·具名**" if not hits else ""))
    for p, i, line in hits:
        print("     %s:%d ｜ %s" % (p, i, line[:150]))
    print()

for role, (name, rx) in (("須 > 0", CTL_HI), ("須 = 0", CTL_LO)):
    n = sum(1 for t in texts.values() for line in t.split("\n") if rx.search(line))
    print("🔑 對照組（%s）字樣 `%s` ⇒ 列 **%d** %s"
          % (role, name, n,
             "✅" if ((n > 0) == (role == "須 > 0")) else "🔴 **量測器紅**"))
