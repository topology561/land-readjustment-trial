# -*- coding: utf-8 -*-
"""發單側窗二十八（倉外·唯讀）：W-G.9-332 收單復驗器。用法：python verify332.py <repo> <單檔> <塊目錄> <F1> <F2> <F3>"""
import hashlib, subprocess, sys, os
R, O, BD, F1, F2, F3 = sys.argv[1:7]
BASE = "338bd08b4e480aba4eec6d315284ce8a9fea6d1f"
def g(*a, raw=False):
    r = subprocess.run(["git", "-C", R, "-c", "core.quotepath=false", *a], capture_output=True)
    return r.stdout if raw else r.stdout.decode("utf-8", "replace").strip()
def sha(b): return hashlib.sha256(b).hexdigest()
res = []
def chk(name, ok, info=""): res.append((name, ok)); print(("🟢" if ok else "🔴"), name, info)
head = g("rev-parse", "origin/wip/s1-endpart")
cs = g("rev-list", "--reverse", BASE + ".." + head).split()
chk("主線已前進", len(cs) > 0, "%s（%d commit）" % (head[:7], len(cs)))
chk("單親線性", all(len(g("rev-list", "--parents", "-n1", c).split()) == 2 for c in cs))
msgs = [g("log", "-1", "--format=%s", c) for c in cs]
for m in msgs: print("    ", m[:90])
chk("工項零〜八 各一 commit", [any(("工項%s" % k) in m for m in msgs) for k in "零一二三四五六七八"] == [True] * 9)
order = open(O, "rb").read()
chk("單之 blob ＝ 發單側之單", g("cat-file", "blob", head + ":docs/orders/W-G.9-332_輕量單.md", raw=True) == order)
T = {1: "docs/rulings/K-6_街角地分配程序與可分配判準.md", 2: "docs/配地計算總規格_v3.md", 3: "docs/W-D.4_合併分配規格.md",
     4: "docs/specs/W-G.4_KL域裁L_達半佇列_算術不可行剔除.md", 5: "docs/reports/W-G.4_泛用阻塞項登記表.md",
     6: "docs/reports/W-G.9波_claude.ai側自誤登記.md", 7: "CLAUDE.md"}
for k, f in T.items():
    a = g("cat-file", "blob", BASE + ":" + f, raw=True); b = g("cat-file", "blob", head + ":" + f, raw=True)
    blk = open(os.path.join(BD, "P%d.md" % k), "rb").read()
    chk("塊 P%d 恰為 %s 之末端追加" % (k, f.split("/")[-1][:18]), b == a + blk, "%d + %d" % (len(a), len(b) - len(a)))
for f, src in (("docs/specs/調配階段_泛用規格_v1.md", F1), ("verify/probes/probe_WG9332_geomall.py", F2), ("verify/probes/probe_WG9332_mkfigs.py", F3)):
    chk("檔 %s 逐位同" % f.split("/")[-1], g("cat-file", "blob", head + ":" + f, raw=True) == open(src, "rb").read())
chk("報告兼 CC 交接文存在", g("cat-file", "-t", head + ":docs/reports/W-G.9-332R_CC交接文.md") == "blob")
prod = ["app.py"] + [x for x in g("ls-tree", "--name-only", BASE, "verify/").split("\n") if x.endswith(".py")]
chk("生產碼相異 0", g("diff", "--name-only", BASE, head, "--", *prod) == "", "app.py %s" % g("rev-parse", head + ":app.py")[:8])
ns = g("diff", "--numstat", BASE, head).split("\n")
chk("刪除欄皆 0", all(l.split("\t")[1] == "0" for l in ns if l), "%d 檔" % len([l for l in ns if l]))
ch = [x for x in g("diff", "--name-only", BASE, head).split("\n") if x]
chk("變動檔 CR 0", sum(g("cat-file", "blob", head + ":" + x, raw=True).count(b"\r") for x in ch) == 0, "%d 檔" % len(ch))
new = [x for x in g("diff", "--name-only", "--diff-filter=A", BASE, head).split("\n") if x]
print("    新檔", len(new), new)
allf = g("ls-tree", "-r", "--name-only", head).split("\n")
print("    母體 全倉 %d｜.md %d｜docs/ %d｜verify/out/ %d" % (len(allf), sum(x.endswith(".md") for x in allf),
      sum(x.startswith("docs/") for x in allf), sum(x.startswith("verify/out/") for x in allf)))
bl = subprocess.run(["git", "-C", R, "-c", "core.quotepath=true", "ls-tree", "-r", head, "verify/baselines"], capture_output=True).stdout
chk("baselines 不變", sha(bl).startswith("a898f4e1"))
chk("遠端 heads 26", len(g("ls-remote", "--heads", "origin").split("\n")) == 26)
chk("凍存 tip 不變", g("rev-parse", "origin/verify/W-G.9-299-gb170").startswith("488c4858"))
print("合計 🟢 %d／🔴 %d" % (sum(1 for _, o in res if o), sum(1 for _, o in res if not o)))
