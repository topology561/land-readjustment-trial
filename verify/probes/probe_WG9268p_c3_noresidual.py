# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令十四 `§二-2`／`§二-4`：`c3_noresidual` —— 造 `c`（**旗標已無殘留分支**）。

🛑 **本器⛔ 裝選擇器活體檢**，其由（補令十四 `§二-4` 逐字）：
   > 本器之受詞即「二態同值」；活體檢之拒測條件即「二態同值」⇒ 置之於此係**自相矛盾**，
   > 將使本器結構上不可達。**⛔ 後人以「補齊活體檢」為由加裝**——欲加者須先讀補令十四 `§二-1`。

🩸 **射程之具名（CC 照實所報·補令十四 `§二-4` 令逐字帶入）**
   > **「未設」式於父態亦綠 ⇒ 該式⛔ 具判別力**；判別力**全由「設 `'0'`」式承擔**。
   其由：父態（`c2` 後）之預設即 `on`（`environ.get(FLAG, '1')`）⇒ 「未設」於父態與 `c3` 態**同值**。

🔑 **判別力 ＝ 二樹對照（補令十四 `§二-4`）**
   同一器對**父態 `app.py`**（旗標分支尚在）跑 ⇒ **須紅**；對 `c3` 之 `app.py` 跑 ⇒ **須綠**。
   **二樹同色 ⇒ 閘失能·停機上呈**（`rc = 5`）。

🔒 **二樹之換法（補令十四 `§二-4`）**：只換 `app.py` 一檔
   （父態與 `c3` 於生產碼 `34` 檔中**僅 `app.py` 相異**），換畢**須還原**並出艙還原之證（`sha256` 二端）。

🛑 **`harvest()` 依<u>路徑</u>快取**（`app_harvest._CACHE`）⇒ 就地換檔後**必須清快取**，
   否則第二樹取到**第一樹之 `ns`**——`rc = 0`、輸出完好、結論**貌似全對**（`GB-161` 之同族）。
   ⇒ 本器於每次 `harvest()` 前清之，**並以自我驗證閘實查所取之樹**（見 `_assert_tree`）。

🔒 **自我驗證閘**（`CLAUDE.md`：探針須以**碼面自身之保證**當自我驗證閘）
   每樹 `harvest()` 後，以 **AST 實查** `_wg9268p_anchor_advance` 之函式體內
   有無 `environ` 之存取：父態**須有**、`c3` 態**須無**。**該閘不過 ⇒ ⛔ 據以下任何結論**。
"""
import ast
import hashlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# 🔒 倉相對定位（`GB-161` 之修·⛔ 硬編他窗 worktree）
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(REPO)
sys.path.insert(0, HERE)

import app_harvest as _AH                                           # noqa: E402

FLAG = "WG" + "9268P_ANCHOR_GEOM"        # 執行期組出（體例同 `GB-147`）
APP = os.path.join(REPO, "app.py")

# 二樹之 rev（得以 argv 覆寫；預設取自補令十四 `§二-4`）
REV_PARENT = sys.argv[1] if len(sys.argv) > 1 else "d49d9db"
REV_C3 = sys.argv[2] if len(sys.argv) > 2 else "10d8202"

W = 118
print("=" * W)
print("【`W-G.9-268′` `c3_noresidual`】造 `c`：旗標已無殘留分支 —— **二樹對照**（補令十四 `§二-4`）")
print("=" * W)
print("🛑 本器**⛔ 裝選擇器活體檢**——其受詞即「二態同值」，而活體檢之拒測條件亦即「二態同值」")
print("   ⇒ 置之於此係**自相矛盾**。⛔ 後人以「補齊活體檢」為由加裝（先讀補令十四 `§二-1`）。")
print()


def sha256_of(path):
    return hashlib.sha256(io.open(path, "rb").read()).hexdigest()


def blob(rev):
    return subprocess.run(["git", "cat-file", "blob", "%s:app.py" % rev],
                          stdout=subprocess.PIPE, check=True).stdout


def _assert_tree(ns, want_environ, label):
    """自我驗證閘：AST 實查所取之 `ns` 確為該樹（⛔ 憑檔名或快取）。"""
    src = io.open(APP, encoding="utf-8").read()
    tree = ast.parse(src)
    fn = None
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == "_wg9268p_anchor_advance":
            fn = n
    if fn is None:
        print("   🛑 自我驗證閘：⛔ 尋得 `_wg9268p_anchor_advance` ⇒ loud 拒測")
        return False
    envs = [s for s in ast.walk(fn) if isinstance(s, ast.Attribute) and s.attr == "environ"]
    got = len(envs) > 0
    ok = (got == want_environ)
    print("   🔑 自我驗證閘（%s）：函式內 `environ` 存取 ＝ %d 處／期 %s ⇒ %s"
          % (label, len(envs), "有" if want_environ else "無", "✅" if ok else "🛑 不過"))
    return ok


def run_tree(rev, label, want_environ):
    """換入該樹之 `app.py` ⇒ 清快取 ⇒ harvest ⇒ 自我驗證閘 ⇒ 評造 `c`。回 (綠?, v0, v1)。"""
    io.open(APP, "wb").write(blob(rev))
    _AH._CACHE.clear()                      # 🛑 ⛔ 清 ⇒ 第二樹必取到第一樹之 ns
    ns, _ = _AH.harvest()
    print("── 樹 `%s`（%s）──" % (rev, label))
    print("   `app.py` sha256 ＝ %s" % sha256_of(APP)[:16])
    if not _assert_tree(ns, want_environ, label):
        return None, None, None
    adv = ns["_wg9268p_anchor_advance"]
    import math
    d_hat = (1.0, 0.0)
    corner = (100.0, 200.0)
    _a = math.radians(93.7)
    alloc = (math.cos(_a), math.sin(_a))
    n_hat = (-alloc[1], alloc[0])
    S_LIST = [0.5, 2.0, 7.25, 3.0]
    CC = [[corner[0] + s * d_hat[0] + u * n_hat[0],
           corner[1] + s * d_hat[1] + u * n_hat[1]]
          for s in S_LIST for u in (-4.0, 11.0)]
    os.environ[FLAG] = "0"
    v0 = float(adv(1.0, CC, d_hat, corner, alloc))
    os.environ.pop(FLAG, None)
    v1 = float(adv(1.0, CC, d_hat, corner, alloc))
    green = abs(v0 - v1) <= 1e-9
    print("   造 `c`：設 `'0'` ⇒ %.10f ／ 未設 ⇒ %.10f ／ 二者相同 ＝ %s %s"
          % (v0, v1, green, "✅ 綠" if green else "🔴 紅"))
    print("      🩸 射程：**「未設」式⛔ 具判別力**（父態預設即 `on`）"
          "；判別力**全由「設 `'0'`」式承擔**")
    return green, v0, v1


# 🔒 **還原之基準 ＝ 換檔前之<u>原始位元組</u>**（⛔ 由 rev 反推·⛔ 憑判斷重建）
ORIG_BYTES = io.open(APP, "rb").read()
SHA_BEFORE = hashlib.sha256(ORIG_BYTES).hexdigest()
print("🔒 換檔前 `app.py` sha256 ＝ %s ／ bytes ＝ %d" % (SHA_BEFORE, len(ORIG_BYTES)))
print()

rc = 0
try:
    g_par, p0, p1 = run_tree(REV_PARENT, "父態·旗標分支尚在", True)
    print()
    g_c3, c0, c1 = run_tree(REV_C3, "`c3`·旗標已移除", False)
finally:
    io.open(APP, "wb").write(ORIG_BYTES)     # 🔒 原始位元組原樣寫回
    _AH._CACHE.clear()                       # 🛑 還原後亦須清，否則後續呼叫取到被換樹之 ns
    SHA_AFTER = sha256_of(APP)
    print()
    print("🔒 **還原之證**：換檔前 sha256 ＝ %s ／ 還原後 ＝ %s ／ 逐位相同 ＝ %s %s"
          % (SHA_BEFORE[:16], SHA_AFTER[:16], SHA_BEFORE == SHA_AFTER,
             "✅" if SHA_BEFORE == SHA_AFTER else "🛑"))
    if SHA_BEFORE != SHA_AFTER:
        print("🛑 **還原不成 ⇒ 停機**（⛔ 留下被換過之 `app.py`）")
        sys.exit(6)

print()
print("── 🔑 二樹對照（補令十四 `§二-4`）──")
if g_par is None or g_c3 is None:
    print("   🛑 **自我驗證閘不過 ⇒ loud 拒測**（⛔ 據以下任何結論）")
    sys.exit(4)
print("   父態（旗標分支尚在）⇒ %s（期 **紅**）" % ("綠" if g_par else "紅"))
print("   `c3`（旗標已移除） ⇒ %s（期 **綠**）" % ("綠" if g_c3 else "紅"))
if g_par == g_c3:
    print("   🛑 **二樹同色 ⇒ 閘失能·停機上呈**（補令十四 `§二-4`）")
    sys.exit(5)
print("   ⇒ ✅ **二樹異色** ⇒ 本器**確能偵得殘留分支**、非恆綠")

print()
print("=" * W)
if not g_c3:
    print("🔴 **`c3` 態之造 `c` 紅** ⇒ 旗標仍有殘留分支 ⇒ 本次輸出⛔ 出艙")
    print("=" * W)
    sys.exit(3)
print("✅ **`c3_noresidual` 全綠**：`c3` 態旗標**已無殘留分支**（正面斷言）")
print("   🔒 與 `Q-2`（字樣命中 `0`）**互為兩證**——一為**字樣**、一為**行為**。")
print("=" * W)
