# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令十四 `§二-2`：`c3_unit` —— 造 `a′`／`b`（**單態**）。

🔒 **本器⛔ 裝選擇器活體檢**，其由（補令十四 `§二-2` 之表逐字）：
   > **無**——**單態·⛔ 態之切換** ⇒ 該閘依構造不適用。
   本器之二造**皆於同一態**（旗標未設）求值，⛔ 構造任何「二態」；
   而活體檢之受詞為「**本探針所構造之二態，須於一具名可觀測量上確有相異**」
   ⇒ 其於**無二態**之器上**無受詞**。**⛔ 後人以「補齊活體檢」為由加裝。**

🩸 **其所以自 `c1_synth` 拆出（`自誤 349`）**：`c1_synth` 內活體檢之**拒測條件**
   與造 `c` 之**通過條件**同為「二態同值」⇒ 造 `c` 結構上不可達；
   且活體檢置於**全部判定之前** ⇒ 連**與態之切換無涉**之造 `a′`／`b` 亦一併未執行。
   ⇒ 依補令十四 `§二-2` **拆器**：本器承造 `a′`／`b`（⛔ 涉態之切換）。

🔒 **期望值之來源（⛔ 由本碼現跑回填·`fixture-provenance`）**
   `_strip_s_range` 之 docstring 逐字載**恆等式** `s(corner_pt + s0·d_hat) ≡ s0`
   ⇒ 以 `corner_pt + s_i·d̂ + u_j·n̂` 造點者，其 `max strip` **閉式恆為 `max(s_i)`**。
   🔒 **⛔ 另寫第二份幾何定義**：`s_geo` 一律自 `_oblique_s_max` 取（`GB-48` 族）。

🛑 **容差沿用** `chk` 之既有 `1e-9`·⛔ 放寬。
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# 🔒 倉相對定位（`GB-161` 之修·⛔ 硬編他窗 worktree）
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(REPO)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402

FAIL = []
NEG_FAIL = []


def chk(name, got, want, tol=1e-9, bucket=None):
    ok = (want is None and got is None) or (
        got is not None and want is not None and abs(got - want) <= tol)
    print("  %-56s 得 %-18s 期 %-18s %s"
          % (name, ("%.10f" % got) if got is not None else "None",
             ("%.10f" % want) if want is not None else "None", "✅" if ok else "🔴"))
    (FAIL if bucket is None else bucket).append(None if ok else name)
    return ok


W = 118
print("=" * W)
print("【`W-G.9-268′` `c3_unit`】造 `a′`／`b` —— **單態**·⛔ 裝選擇器活體檢（補令十四 `§二-2`）")
print("=" * W)

ns, _fake = harvest()
adv = ns["_wg9268p_anchor_advance"]
osm = ns["_oblique_s_max"]
print("🔒 受測符號自 `harvest()` 取得：`_wg9268p_anchor_advance` %s ／ `_oblique_s_max` %s"
      % (callable(adv), callable(osm)))

# ── 合成幾何（**斜交**·⛔ 正交特例·`_strip_axis` docstring 之戒 ＝ 失敗考古 #7）──
d_hat = (1.0, 0.0)
corner = (100.0, 200.0)
_a = math.radians(93.7)                       # ALLOC 與 FRONT 斜交 3.7°
alloc = (math.cos(_a), math.sin(_a))
n_hat = (-alloc[1], alloc[0])
S_LIST = [0.5, 2.0, 7.25, 3.0]                # ⇒ 閉式期望 max strip ＝ 7.25
U_LIST = [-4.0, 11.0]
CC = [[corner[0] + s * d_hat[0] + u * n_hat[0],
       corner[1] + s * d_hat[1] + u * n_hat[1]]
      for s in S_LIST for u in U_LIST]
S_GEO = max(S_LIST)

print()
print("── 閉式自證（`_oblique_s_max` ＝ `max(s_i)`）──")
print("   斜交角 ＝ %.1f°（⛔ 正交）／頂點 %d 個／`s_i` ＝ %s" % (math.degrees(_a) - 90.0, len(CC), S_LIST))
chk("`_oblique_s_max`（閉式期望 max(s_i)）", float(osm(CC, d_hat, corner, alloc)), S_GEO)

# 🔒 本器⛔ 設旗標：二造皆於**同一態**（環境變數未設）求值
os.environ.pop("WG9268P_ANCHOR_GEOM", None)

print()
print("── 造 `a′`：**錨⛔ 後退**（`s_geo < cum_S` ⇒ 須為 `cum_S`·`max()` 之語意）──")
chk("`cum_S ＝ 10.0` 而 `s_geo ＝ 7.25`（須仍 10.0）",
    float(adv(10.0, CC, d_hat, corner, alloc)), 10.0)

print()
print("── 造 `b`：**生效**（`s_geo > cum_S` ⇒ 須為 `s_geo`）──")
chk("`cum_S ＝ 1.0` 而 `s_geo ＝ 7.25`（須 7.25）",
    float(adv(1.0, CC, d_hat, corner, alloc)), S_GEO)

# ── 判別力（補令十四 `§二-3`）──────────────────────────────────────────
print()
print("── 🔑 判別力（補令十四 `§二-3`）──")
print("   陽性二造**同一函式、同一輪、期望相異**（`10.0` vs `7.25`）⇒ 二者⛔ 同時為恆綠：")
print("     凡以常數回傳之偽實作，必令其一轉紅。")
print("   **陰性二造**（期望互換·**須皆紅**）：")
neg = []
chk("[陰性] `cum_S ＝ 10.0` 而斷言須為 `s_geo`（須紅）",
    float(adv(10.0, CC, d_hat, corner, alloc)), S_GEO, bucket=neg)
chk("[陰性] `cum_S ＝ 1.0` 而斷言須為 `cum_S`（須紅）",
    float(adv(1.0, CC, d_hat, corner, alloc)), 1.0, bucket=neg)

pos_ok = not [x for x in FAIL if x]
neg_red = len([x for x in neg if x])
print()
print("   陽性二造 ＝ %s ／ 陰性二造之紅 ＝ %d／2"
      % ("全綠" if pos_ok else "有紅", neg_red))
if neg_red != 2:
    print("   🛑 **陰性未皆紅 ⇒ 閘失能·停機上呈**（補令十四 `§二-3`）")
    sys.exit(5)
print("   ⇒ ✅ **二造⛔ 同色**（陽性全綠 ∧ 陰性全紅）⇒ 本器**非恆綠、亦非恆紅**")

print()
print("=" * W)
_bad = [x for x in FAIL if x]
if _bad:
    print("🔴 **`c3_unit` 紅 ＝ %d 項** ⇒ 本次輸出⛔ 出艙：" % len(_bad))
    for x in _bad:
        print("   · %s" % x)
    print("=" * W)
    sys.exit(3)
print("✅ **`c3_unit` 全綠**：閉式自證 ⋀ 造 `a′`（錨⛔ 後退）⋀ 造 `b`（生效）⋀ 陰性二造皆紅")
print("=" * W)
