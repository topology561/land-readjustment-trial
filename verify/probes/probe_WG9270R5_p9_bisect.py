# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令四 `§四-2`：**`p9` `TIER_EXPECT` 之翻紅點**（零生產碼·唯讀·二分）。

🛑 本器**⛔ 動主 worktree 之任何檔**——其於一個**拋棄式 worktree** 內 `checkout --detach` 逐候選態，
  並於該態內呼 `wd4_tier_list.compute(fixture=False)`（**記憶體側**·該函式⛔ 寫任何檔）。
🛑 **⛔ 改 `TIER_EXPECT` 一字、⛔ 判其為缺陷、⛔ 提遷移主張**（補令四 `§四-2` 款 `4`）。

🔒 **已知之二端（本批當場實跑·⛔ 假定）**
  `7fa957e`（`K-8 段三 commit A`）⇒ `tiers = {'0':13,'1':7,'—':8,'2':3,'3':2}` ＝ **`TIER_EXPECT` 相符**
  `HEAD`                          ⇒ `tiers = {'0':11,'1':9,'—':8,'2':3,'3':2}` ⇒ **相異**
🔒 **判別力（款 `2` 明令·已於本批先行辦畢）**：於 `TIER_EXPECT` **最後一次更新之 commit**
  （`7ce98e6`·`git log -L` 現查）實跑得 `{'0':13,'1':7,…}` ⇒ **該錨曾為真** ⇒ 得續二分。

🔒 **⛔ 靜默**：任一態之 `compute()` 拋出者，**⛔ 視為「紅」**——其為 **loud 拒測**（`rc = 5`），
  ⛔ 與「判定為偽」共用出艙碼（`CLAUDE.md` 之「無從判定 ⛔ 與判定為偽共用同一出艙碼」）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9270R5_p9_bisect.py <worktree 路徑>`
`rc`：`0` 定位成功／`5` 某態求值失敗（loud 拒測）／`6` 二端之前提不成立。
"""
import json
import os
import subprocess
import sys

WT = sys.argv[1] if len(sys.argv) > 1 else None
if not WT or not os.path.isdir(WT):
    print("🛑 須給一個既存之拋棄式 worktree 路徑（⛔ 主 worktree）")
    sys.exit(6)

GOOD = "7fa957e"          # 已實測：相符
EXPECT = {"—": 8, "0": 13, "1": 7, "2": 3, "3": 2}

SNIP = (
    "import sys, json\n"
    "sys.path.insert(0,'verify')\n"
    "from wd4_tier_list import compute\n"
    "r = compute(fixture=False)\n"
    "out = {t: r[t]['tiers'] for t in ('0m','3.5m')}\n"
    "out['mina_qu'] = r['0m']['mina_qu']\n"
    "print('###JSON###' + json.dumps(out, ensure_ascii=False))\n"
)


def tiers_at(rev):
    """回 (ok, payload)；ok=False 表求值失敗 ⇒ loud 拒測（⛔ 視為紅）"""
    r = subprocess.run(["git", "-C", WT, "checkout", "--detach", rev],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        return False, "checkout 失敗：" + (r.stderr or "")[-300:]
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    p = subprocess.run([sys.executable, "-c", SNIP], cwd=WT, env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        return False, "compute 失敗（rc=%d）：%s" % (p.returncode, (p.stderr or "")[-400:])
    for line in (p.stdout or "").split("\n"):
        if line.startswith("###JSON###"):
            return True, json.loads(line[len("###JSON###"):])
    return False, "⛔ 取得 JSON 標記（stdout 尾）：" + (p.stdout or "")[-300:]


def is_red(payload):
    """紅 ⟺ 任一情境之 tiers ≠ EXPECT"""
    return any(payload[t] != EXPECT for t in ("0m", "3.5m"))


def main():
    revs = subprocess.run(["git", "rev-list", "--reverse", "%s..HEAD" % GOOD],
                          capture_output=True, text=True, check=True).stdout.split()
    print("=" * 96)
    print("【`W-G.9-270` 補令四 `§四-2`】`p9` `TIER_EXPECT` 之翻紅點（二分）")
    print("=" * 96)
    print("區間 ＝ %s..HEAD ／ 候選 commit 數 ＝ %d" % (GOOD, len(revs)))
    print("EXPECT ＝ %s" % json.dumps(EXPECT, ensure_ascii=False))
    print("判準 ＝ 任一情境之 tiers ≠ EXPECT ⇒ 紅")
    print()

    # 二端之前提（⛔ 假定·當場復現）
    for rev, want_red in ((GOOD, False), (revs[-1], True)):
        ok, pay = tiers_at(rev)
        if not ok:
            print("🛑 二端之 %s 求值失敗 ⇒ **loud 拒測**：%s" % (rev[:7], pay))
            return 5
        red = is_red(pay)
        print("  端 %s  mina_qu=%s  0m=%s  ⇒ %s（期 %s）%s"
              % (rev[:7], pay["mina_qu"], json.dumps(pay["0m"], ensure_ascii=False),
                 "紅" if red else "相符", "紅" if want_red else "相符",
                 "✅" if red == want_red else "🔴"))
        if red != want_red:
            print("🛑 二端之前提不成立 ⇒ ⛔ 續二分")
            return 6
    print()

    lo, hi = -1, len(revs) - 1          # revs[lo] 相符（lo=-1 代表 GOOD）／revs[hi] 紅
    step = 0
    while hi - lo > 1:
        mid = (lo + hi) // 2
        step += 1
        ok, pay = tiers_at(revs[mid])
        if not ok:
            print("🛑 步 %d：%s 求值失敗 ⇒ **loud 拒測**（⛔ 視為紅）：%s"
                  % (step, revs[mid][:7], pay))
            return 5
        red = is_red(pay)
        print("  步 %-2d idx=%-4d %s  mina_qu=%-8s 0m=%s ⇒ %s"
              % (step, mid, revs[mid][:7], pay["mina_qu"],
                 json.dumps(pay["0m"], ensure_ascii=False), "🔴 紅" if red else "✅ 相符"))
        if red:
            hi = mid
        else:
            lo = mid

    ans = revs[hi]
    print()
    print("🔑 **首次為紅之 commit** ＝ %s" % ans)
    msg = subprocess.run(["git", "log", "-1", "--format=%H%n%s", ans],
                         capture_output=True, text=True, encoding="utf-8",
                         errors="replace").stdout.strip().split("\n")
    print("   全 40 碼 ＝ %s" % msg[0])
    print("   訊息首列 ＝ %s" % (msg[1] if len(msg) > 1 else ""))
    par = subprocess.run(["git", "rev-parse", ans + "^"],
                         capture_output=True, text=True).stdout.strip()
    print("   其父 ＝ %s" % par)
    print("   其異動（numstat）：")
    ns = subprocess.run(["git", "-c", "core.quotepath=false", "diff", "--numstat",
                         ans + "^", ans], capture_output=True, text=True,
                        encoding="utf-8", errors="replace").stdout
    for L in ns.strip().split("\n"):
        print("     " + L)
    print()
    print("🛑 **本器⛔ 判其為缺陷、⛔ 提任何遷移主張**（補令四 `§四-2` 款 `4`）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
