#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-56】候選角機制之**判別力自檢**（獨立小檢·⛔ 零生產碼）

🩸 **本檔之由來（CC 自誌·第三次同戒）**：`probe_WG956_yi_style.py` 之【S-2】兩版皆未成立——
  v1 合成例取**軸對齊**（`θ=0` 恰在網格上 ⇒ 網格必中）；
  v2 改轉一個非格點角，惟合成帶寬**恰** ＝ `W` ⇒ 旋轉之 ~1e-15 誤差即使其**任何角度皆不進**。
🔒 **修法**：合成帶給一個**穩健但仍窄**之餘裕（寬 ＝ `W + MARGIN`），
  使可容納之**角度窗**非退化、且**窄於均勻階梯之最細步長** ⇒ 網格漏、候選角抓到。

🔒 沿用 `probe_WG949_free_pose` 之 `fits_at`／`scan`（⛔ 不另寫第二份）。
"""
import io, math, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); VERIFY = os.path.dirname(HERE)
for p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE): sys.path.insert(0, p)
from probe_WG947_rect_fit import _poly_st
from probe_WG949_free_pose import fits_at, scan
from shapely.geometry import Polygon

W, D = 3.5, 14.0
R = math.sqrt(W * W + D * D) / 2.0
STEPS_EPS = (2e-2, 5e-3, 1e-3)
TH0 = 0.012345678901234                 # ⛔ 非任何步長之整數倍
MARGIN = 1.0e-3                         # 穩健餘裕（⇒ 角度窗非退化）
L = []
def P(s=""): L.append(s)
sha = (subprocess.run(["git","rev-parse","--short","HEAD"],cwd=VERIFY,
       capture_output=True,text=True,timeout=20).stdout or "").strip() or "nogit"
P("=" * 110); P("【W-G.9-56】候選角機制之判別力自檢（獨立小檢）"); P("=" * 110)
P(f"  產生於 commit：{sha}")
P(f"  合成帶：寬 ＝ W+{MARGIN} ＝ {W+MARGIN}　長 ＝ {3.0*D}　轉 {TH0:.12f} rad")
P(f"  🔒 該角⛔ 非 {STEPS_EPS} 之整數倍（逐項餘數見下）")
for s in STEPS_EPS: P(f"      TH0 % {s:.0e} ＝ {TH0 % s:.3e}（≠0 ⇒ 非格點）")
c, s_ = math.cos(TH0), math.sin(TH0)
ring = [(x*c - y*s_, x*s_ + y*c) for x, y in
        ((0,0), (W+MARGIN,0), (W+MARGIN,3.0*D), (0,3.0*D))]
pst = _poly_st(list(Polygon(ring).exterior.coords))
grid = scan(pst, W, D, steps=STEPS_EPS, R=R)[0]
cand = fits_at(pst, W, D, TH0, 0.0)[0]
# 角度窗之寬度（自 TH0 往兩側掃至失敗）
win = 0.0
for k in range(1, 200000):
    if not fits_at(pst, W, D, TH0 + k*1e-6, 0.0)[0]:
        win = k*1e-6; break
P("")
P(f"  ① 均勻階梯 {STEPS_EPS}（＝本波實際所用者）⇒ "
  + ("🔴 進（本檢無判別力）" if grid is not None else "**不進** ✅"))
P(f"  ② 具名候選角（精確 `fits_at` @ TH0）⇒ " + ("**進** ✅" if cand else "🔴 不進"))
P(f"  ③ 可容納之**角度窗**（單側）≈ {win:.3e} rad"
  f"　vs 最細步長 {STEPS_EPS[-1]:.0e} ⇒ 窗{'窄於' if win < STEPS_EPS[-1] else '寬於'}步長")
P("")
P(f"  ⇒ **判別力：{'✅ 成立（網格漏、候選角抓到）' if (cand and grid is None) else '🔴 未成立'}**")
P("  🔒 **本檢所證者**：均勻網格**確會漏掉**角度窗窄於步長之解，而具名候選角**抓得到**")
P("     ⇒ 候選角機制**非贅餘**。")
P("  ⚠️ **本檢⛔ 未證「本案 8 格上候選角為必要」**——`fit_search` 先試候選角，")
P("     故本波之 log ⛔ 無從得知均勻網格是否亦能找到該 6 格之解。**具名為未辦。**")
P("  🔒 **⛔ 且不影響結果之正確性**：候選角**只能使「不進」翻為「進」**，")
P("     而每個「進」皆附**見證矩形＋逐角獨立驗證**（`covers` 逐角 True）⇒ ⛔ 不可能製造假「進」。")
P("=" * 110)
out = os.path.join(VERIFY, "out", f"probe_WG956_cand_angle_disc_{sha}.log")
with io.open(out, "w", encoding="utf-8") as f: f.write("\n".join(L) + "\n")
print("\n".join(L)); print(f"\n→ {out}", file=sys.stderr)
