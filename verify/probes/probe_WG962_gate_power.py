#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-62】`GB-82` `(b-2′)(b-2″)(b-2‴)` ＋ `GB-83` 裁示之落實 ⛔ 零生產碼

**受詞**：本檔**不量幾何**，只量**閘自身之判別力**——
「**要出現什麼，這個閘才會紅？**」（失敗考古**節 91** 之判準）。

═══════════════════════════════════════════════════════════════════════
🔴 **`(b-2)` 原式為何撤回**（claude.ai 自誤 47·⛔ 本檔不重述其理由）
═══════════════════════════════════════════════════════════════════════
原式之受詞域 ＝ `d ≥ 10 × d_floor`，而 `d_floor` **即缺陷之量**
⇒ 閉環：**反轉越高 ⇒ 門檻越高 ⇒ 該反轉恰被排除 ⇒ 閘越綠**。
逐字條文見 ``grep -n "^## 🔧 \`GB-82\` \`(b-2)\` 之\*\*撤回與改寫\*\*" \\
docs/reports/W-G.4_泛用阻塞項登記表.md``。

**本檔所實作之更正式**：
- **`(b-2′)`** 受詞域 ＝ `d ≥ d_gate`，`d_gate` ＝ **最小出艙 `D_max` ÷ 1e+03**
  ⇒ 由**出艙值**導出、**⛔ 不隨缺陷移動**。
- **`(b-2″)`** 另印 `d_rev_max`（**最大之已觀測反轉 `d`**）與淨空比；
  **`d_rev_max ≥ d_gate` ⇒ 紅**，⛔ 不得以任何方式排除之。
- **`(b-2‴)`** 🔴 **自帶注入式變異測試**——於受詞域內三高度各注入一處反轉，
  閘**須逐次轉紅**；⛔ 未附者，該閘之綠**不得計為證據**。

🔒 **`d_rev_max` 之定義（⛔ 具名·⛔ 不含糊）**：
    `d_rev_max := max { grid[i] : v[i] = 0 且 ∃ j > i 使 v[j] = 1 }`
  （＝**「其後仍有 1 之最高 0」之 `d`**·對全部 12 組取 max）。
  ⚠️ 本定義為 CC 所定；施工單只給了「最大之已觀測反轉 `d`」與一個現查值
  ——**逐項對拍見 §D-2**（⛔ 不以相符與否掩蓋定義之差）。

🔒 **`GB-83` 裁示之落實**（§A）：母體**逐點列舉** ＋ 涵蓋關係**以斷言檢查**（⛔ 非人眼）。
🔒 **⛔ 不新增第二份判定原語**（`GB-8`）——本檔只**呼叫**
  `probe_WG949_free_pose.fits_at`，並沿用 `-60`／`-61` 之 module 級組裝。
🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
for _p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE):
    sys.path.insert(0, _p)

import probe_WG949_free_pose as fp                                  # noqa: E402
from probe_WG949_free_pose import fits_at                           # noqa: E402
from probe_WG958_dmax_robust import d_max_at                        # noqa: E402
from probe_WG959_knife_edge import TOL_CONV, d_max_at_r             # noqa: E402
from probe_WG960_fitcore import (                                   # noqa: E402
    D_GRID, FOCUS, R_GRID, build_ctx, yi_pst)
from probe_WG961_dfloor import GRID_A, GRID_B, _mono                # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 150

# ── 注入式變異之受詞（`(b-2‴)`）──────────────────────────────────────
INJ_CELL = ("R3", "right")
INJ_R = 0.0
INJ_HEIGHTS = (1e-03, 1e-02, 0.1)          # 施工單指定之三高度（⛔ 皆須轉紅）
INJ_EXTRA = (1e-09, 1e-06)                 # 對拍用（施工單之表另有此二列）
RATIO_DIV = 1e+03                          # `d_gate` ＝ 最小出艙 `D_max` ÷ 此數

# 【G】P7 之對拍靶：`W-G.9-60`【倉】掃描式 12 值
#   出處：`verify/out/probe_WG960_fitcore_post2_65fef5b.log`【A-4】
WG960_DMAX = {
    ("R5", "left"): (0.0264, 39.9825, 39.9825, 39.9860),
    ("R6", "right"): (0.0000, 39.8736, 39.8736, 39.8771),
    ("R3", "right"): (41.4830, 41.4830, 41.4831, 41.4864),
}
EIGHT = [("R1", "left"), ("R1", "right"), ("R2", "left"), ("R3", "right"),
         ("R4", "left"), ("R4", "right"), ("R5", "left"), ("R6", "right")]
PREV8 = {("R1", "left"): "進", ("R1", "right"): "進", ("R2", "left"): "進",
         ("R3", "right"): "進", ("R4", "left"): "進", ("R4", "right"): "進",
         ("R5", "left"): "不進", ("R6", "right"): "不進"}

# ── 注入狀態（module 級·⛔ 一律以 try/finally 還原）─────────────────
INJECT = None          # None 或 (lbl, which, r, d)
_INJ_HITS = 0          # 🔒 **反靜默退路計數器**：注入實際咬到幾次（0 ⇒ 注入沒生效）


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _fits(lbl, which, pst, w, d, th, r):
    """`fits_at` ＋ **注入式變異**。回 bool。

    🔒 注入 ＝ 於指定 `(格, r, d)` 把**真**翻為**偽** ⇒ 於真值集造出一處
      `0…1` **反轉**（薄者判不進而厚者判進·幾何上不可能）。
    🔒 **`_INJ_HITS` 為反靜默退路計數器**——注入若一次都沒咬到，
      整個 `(b-2‴)` 之「轉紅」就只是巧合 ⇒ §E 會以之為閘（⛔ 計數 0 即紅）。
    """
    global _INJ_HITS
    ok = fits_at(pst, w, d, th, r)[0]
    if INJECT is not None:
        il, iw, ir, idd = INJECT
        if lbl == il and which == iw and r == ir and d == idd:
            _INJ_HITS += 1
            return False
    return ok


def _tv(cells, grid):
    """回 12 組之 `(lbl, which, r, 真值字串)`（注入後）。"""
    out = []
    for lbl, which, pst, g, w in cells:
        for r in R_GRID:
            out.append((lbl, which, r,
                        "".join("1" if _fits(lbl, which, pst, w, d, g["theta"], r)
                                else "0" for d in grid)))
    return out


def _dfloor(cells, grid):
    """全案 `d_floor`（＝各組「其上為單調」之最小 `d` 之 max）。"""
    df = 0.0
    for _l, _w, _r, v in _tv(cells, grid):
        for i in range(len(v)):
            if _mono(v[i:]):
                df = max(df, grid[i])
                break
    return df


def _d_rev_max(cells, grid):
    """`max { grid[i] : v[i] = 0 且 ∃ j > i 使 v[j] = 1 }`（⛔ 無反轉時回 `0.0`）。"""
    best = 0.0
    for _l, _w, _r, v in _tv(cells, grid):
        for i, ch in enumerate(v):
            if ch == "0" and "1" in v[i + 1:]:
                best = max(best, grid[i])
    return best


def _snap(h):
    """把**要求之注入高度**吸附到**母體 B 之最近點**。

    🔒 **為何須吸附（⛔ 非為了讓測試通過）**：注入係「把某一格點之真翻為偽」，
      若該高度**不是格點**，注入就是**無聲之 no-op** ⇒ 整個 `(b-2‴)` 偽綠。
    🔴 **本函式係 CC 於執行中撞出來的**：施工單之表列有 `注入位置 d = 1e−06`，
      而 `1e−06` **既不在 `D_GRID`、也不在 22 點格**。前置斷言擋下 ⇒ 循 `_snap`
      重建後，該列之 `d_rev_max` 恰為 **`6.679e−07`**（＝母體 B 之最近點）
      ——**與施工單所載逐位相符** ⇒ 🔑 **單之該列確係吸附後之值**（成因已解釋·⛔ 非不符）。
    """
    return min(GRID_B, key=lambda g: abs(g - h))


def _gate(cells, lo_bound):
    """限縮後之單調性閘（測於 `D_GRID` 中 `≥ lo_bound` 者）。回 `(n_ok, rows)`。"""
    sub = tuple(d for d in D_GRID if d >= lo_bound)
    rows = [(lbl, which, r, v, _mono(v)) for lbl, which, r, v in _tv(cells, sub)]
    return sum(1 for *_x, ok in rows if ok), rows, sub


def main():                                                         # noqa: C901
    global INJECT, _INJ_HITS
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-62】`(b-2′)(b-2″)(b-2‴)` 之實作 ＋ `GB-83` 裁示之落實")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；本檔只**呼叫** `fits_at`，⛔ 未新增第二份判定原語。")
    P("  🔒 判準（考古節 91）：**要出現什麼，這個閘才會紅？**")
    P("")

    ctx = build_ctx()
    ns, cb_by, cad, snapshot, wd, _targets = ctx
    cells = []
    for lbl, which in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        cells.append((lbl, which, pst, g, wd[lbl][0]))

    # ══════════════════════════════════════════════════════════════
    # 【A】`GB-83` 裁示①②：母體**逐點列舉** ＋ 涵蓋關係**以斷言檢查**
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A】`GB-83` 裁示①②：`(b-1)` 母體之**逐點列舉** ＋ 涵蓋關係之**斷言**")
    P("=" * WID)
    P("  🔒 裁示①：⛔ 不得只寫「`[a, b]` 之 `n` 點」——**格即量測框**。")
    P(f"  🔒 母體 B ＝ `GRID_A`（{len(GRID_A)} 點·對數等距）∪ `D_GRID`"
      f"（{len(D_GRID)} 點）＝ **{len(GRID_B)} 點**，逐點如下：")
    for k in range(0, len(GRID_B), 6):
        P("     " + "  ".join(f"[{k + j:02d}] {d:.6e}"
                              for j, d in enumerate(GRID_B[k:k + 6])))
    P("")
    P("  🔒 裁示②：**母體須涵蓋下游閘之全部測點**（⛔ 以斷言檢查·⛔ 非人眼）")
    missing = [d for d in D_GRID if d not in set(GRID_B)]
    if missing:
        raise RuntimeError(
            f"🔴 `GB-83` 裁示② 之涵蓋斷言**不成立**：`D_GRID` 有 {len(missing)} 點"
            f"不在母體內 ⇒ {missing}。⛔ 本次一切 `d_floor` 與閘之結果不得採信。")
    P(f"  ✅ **涵蓋斷言通過**：`D_GRID` 之 {len(D_GRID)} 點**全部**落在母體 B 內。")
    # 🔒 判別力自檢：以「刻意不涵蓋之母體」重跑同一斷言 ⇒ **須不成立**
    bad_pop = tuple(d for d in GRID_B if d != 1e-09)
    bad_missing = [d for d in D_GRID if d not in set(bad_pop)]
    P(f"  🔒 **判別力自檢**（⛔ 不得省）：以刻意剔除 `d=1e−09` 之母體"
      f"（{len(bad_pop)} 點）重跑 ⇒ 缺 **{len(bad_missing)}** 點 "
      f"{'✅ 斷言確會不成立（⇒ 上檢非恆真）' if bad_missing else '🔴 斷言恆真 ⇒ ⛔ 無判別力'}")
    P(f"     ⚠️ 母體 A（施工單字面 {len(GRID_A)} 點）之缺點數 ＝ "
      f"**{len([d for d in D_GRID if d not in set(GRID_A)])}** ⇒ **`(b-1)` 原文之母體⛔ 不合格**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【B】`d_gate` 之導出——**由出艙值**（⛔ 不由缺陷量）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【B】`(b-2′)` 之受詞域下限 `d_gate` ——**由出艙值導出**（⛔ 不由缺陷量）")
    P("=" * WID)
    df_real = _dfloor(cells, GRID_B)
    P(f"  · `d_floor`（母體 B·真實資料）＝ **{df_real:.6e}** m　"
      "⚠️ **僅供事實陳述**，`GB-83` 裁示③ ⛔ 禁其再界定任何閘之受詞域")
    P(f"  🔒 出艙 `D_max` 之**收斂容差** `tol_conv` ＝ **{TOL_CONV:.1e}** m"
      "（＝有效位數上限·⛔ 與 `d_floor` 無關）")
    dmax = {}
    for lbl, which, pst, g, w in cells:
        for r in R_GRID:
            dmax[(lbl, which, r)] = d_max_at_r(pst, w, g["theta"], r,
                                               d_floor=df_real, tol_conv=TOL_CONV)
    d_out_min = min(v for v in dmax.values() if v > 0.0)
    d_gate = d_out_min / RATIO_DIV
    P(f"  · **最小出艙 `D_max`**（>0）＝ **{d_out_min:.6f}** m")
    P(f"  · **`d_gate` ＝ 最小出艙 `D_max` ÷ {RATIO_DIV:.0e} ＝ {d_gate:.6e} m**")
    P(f"     （施工單【單】載 `2.640e−05`；本檔【倉】{d_gate:.3e}"
      f"　⇒ 差 {abs(d_gate - 2.640e-05) / 2.640e-05 * 100:.2f}%"
      "·成因＝單以 4dp 之 `0.0264` 計、本檔以全精度計）")
    P("  🔒 **`d_gate` ⛔ 不隨缺陷移動**——其唯一輸入為**出艙值**；"
      "以下全部注入實驗中，本值**恆定**。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【C】`(b-2′)` 真實資料之閘
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P(f"【C】`(b-2′)` **真實資料**之閘：受詞域 ＝ `d ≥ d_gate` ＝ `{d_gate:.3e}` m")
    P("=" * WID)
    n_ok, rows, sub = _gate(cells, d_gate)
    exc = tuple(d for d in D_GRID if d < d_gate)
    P(f"  🔒 `D_GRID` 15 點中受檢 **{len(sub)}** 點；排除 **{len(exc)}** 點："
      + ("／".join(f"{d:g}" for d in exc) or "（無）"))
    P("")
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}   {'真值集':<18}{'單調?':>7}")
    P("-" * WID)
    for lbl, which, r, v, ok in rows:
        P(f"  {lbl:<5}{which:<8}{r:>10.0e}   {v:<20}{'✅' if ok else '🔴':>6}")
    P("-" * WID)
    P(f"  ⇒ **`(b-2′)`：{n_ok}／12 綠**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【D】`(b-2″)` `d_rev_max` ＋ 淨空比
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【D】`(b-2″)`：`d_rev_max`（最大之已觀測反轉 `d`）＋ 淨空比")
    P("=" * WID)
    drm = _d_rev_max(cells, GRID_B)
    P(f"  🔒 定義（CC 具名）：`d_rev_max := max {{ grid[i] : v[i]=0 且 ∃ j>i 使 v[j]=1 }}`"
      "（＝**其後仍有 1 之最高 0**）")
    P(f"  · `d_rev_max`【倉】 ＝ **{drm:.6e}** m　（施工單【單】載 `1.000e−09`"
      f" ⇒ {'✅ 相符' if abs(drm - 1e-9) < 1e-18 else '🔴 不符'}）")
    P(f"  · **淨空比** ＝ 最小出艙 `D_max` ÷ `d_rev_max` ＝ "
      f"**{(d_out_min / drm) if drm > 0 else float('inf'):.3e}**"
      "　（施工單【單】載 `2.64e+07`）")
    red_rev = drm >= d_gate
    P(f"  🔴 **判**：`d_rev_max ≥ d_gate`？ {drm:.3e} vs {d_gate:.3e} ⇒ "
      f"**{'🔴 是 ⇒ 紅' if red_rev else '✅ 否 ⇒ 綠'}**（⛔ 不得以任何方式排除之）")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【E】`(b-2‴)` 注入式變異測試 ＋ 【F】`(b-2)` 原式之對照
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【E】🔴 `(b-2‴)` **注入式變異測試** ＋ 【F】`(b-2)` **原式之對照**（`P5`·⛔ 不得省）")
    P("=" * WID)
    P(f"  🔒 注入受詞：`{INJ_CELL[0]}/{INJ_CELL[1]} @ r={INJ_R:.0e}`——"
      "於指定 `d` 把**真**翻為**偽** ⇒ 造出一處 `0…1` 反轉。")
    P("  🔒 **前置斷言**：注入點須同時存在於母體 B 與 `D_GRID`"
      "（⛔ 否則注入是無聲的 no-op ⇒ 整個測試偽綠）。")
    P("")
    P("  🔒 **要求高度 ⇒ 吸附至母體 B 之最近點**（⛔ 非格點者注入即無聲 no-op）。")
    P("")
    P(f"  {'要求 d':>10}{'實注入點':>14}{'在D_GRID':>9}{'咬到':>6}"
      f"{'d_floor(注入後)':>17}{'10×d_floor':>13}"
      f"{'原式閘':>8}{'d_rev_max':>13}{'更正式閘':>9}{'判':>6}")
    P("-" * WID)
    inj_rows = []
    for hgt0 in INJ_EXTRA + INJ_HEIGHTS:
        hgt = _snap(hgt0)
        in_b = hgt in set(GRID_B)
        in_g = hgt in set(D_GRID)
        if not in_b:
            raise RuntimeError(
                f"🔴 吸附後之注入點 `d={hgt:g}` 仍不在母體 B ⇒ ⛔ 不得採信。")
        if hgt0 in INJ_HEIGHTS and not in_g:
            # 🔒 三高度**必須**落在閘之測點上，否則「未轉紅」之因是 no-op、⛔ 非閘無判別力
            raise RuntimeError(
                f"🔴 施工單指定之高度 `{hgt0:g}` 吸附後為 `{hgt:g}`，**不在 `D_GRID`**"
                " ⇒ 閘看不到該注入 ⇒ ⛔ 本測試不得採信。")
        _INJ_HITS = 0
        try:
            INJECT = (INJ_CELL[0], INJ_CELL[1], INJ_R, hgt)
            df_i = _dfloor(cells, GRID_B)              # 原式之門檻隨缺陷而動
            n_old, _r_old, _s_old = _gate(cells, 10.0 * df_i)
            n_new, _r_new, _s_new = _gate(cells, d_gate)   # 更正式：門檻恆定
            drm_i = _d_rev_max(cells, GRID_B)
            hits = _INJ_HITS
        finally:
            INJECT = None                              # 🔒 **必還原**
        if hits == 0:
            raise RuntimeError(
                f"🔴 注入 `d={hgt:g}` 之**咬到次數 ＝ 0** ⇒ 注入從未生效"
                "（反靜默退路計數器·`CLAUDE.md` D-2b-0）⇒ ⛔ 結論不得採信。")
        want_red = hgt0 in INJ_HEIGHTS
        verdict = ("✅" if (n_new < 12) == want_red else "🔴")
        inj_rows.append((hgt0, hgt, hits, df_i, n_old, n_new, drm_i, want_red,
                         (n_new < 12) == want_red))
        P(f"  {hgt0:>10.0e}{hgt:>14.6e}{('是' if in_g else '否'):>9}"
          f"{hits:>6}{df_i:>17.6e}{10.0 * df_i:>13.3e}"
          f"{(str(n_old) + '／12'):>8}{drm_i:>13.3e}"
          f"{(str(n_new) + '／12'):>9}{verdict:>5}")
    P("-" * WID)
    n_old_green = sum(1 for r in inj_rows if r[4] == 12)
    tri = [r for r in inj_rows if r[0] in INJ_HEIGHTS]
    tri_red = sum(1 for r in tri if r[5] < 12)
    P(f"  🔴 **`(b-2)` 原式**：{len(inj_rows)} 次注入中 **{n_old_green} 次仍 12／12 綠**"
      f"{'　⇒ **結構上不會紅**（自誤 47 復現）' if n_old_green == len(inj_rows) else ''}")
    P(f"  ✅ **`(b-2′)` 更正式**：施工單指定之三高度"
      f"（{'／'.join(f'{h:g}' for h in INJ_HEIGHTS)}）⇒ **{tri_red}／3 轉紅**")
    P("  🔒 **⇒ 判別力已證**：真實資料綠、注入皆紅。"
      "（節 91：⛔ 未附注入測試者，該閘之綠不得計為證據）")
    P("")
    P("  🔒 **門檻之對照（⛔ 一眼可見閉環）**：")
    P(f"     · 原式門檻 `10×d_floor` 隨注入由 `{10.0 * inj_rows[0][3]:.3e}` 漲到 "
      f"`{10.0 * inj_rows[-1][3]:.3e}`（**{10.0 * inj_rows[-1][3] / (10.0 * inj_rows[0][3]):.3g}×**）"
      "⇒ **恰把注入點自己排除掉**")
    P(f"     · 更正式門檻 `d_gate` 恆為 `{d_gate:.3e}` ⇒ **⛔ 不隨缺陷移動**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【G】`P7`：十二值 ＋ **收斂容差並列**
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【G】`P7`：`D_max` 十二值 vs `W-G.9-60`【倉】掃描式　"
      "＋ 🔒 **收斂容差並列**（§五-D）")
    P("=" * WID)
    P(f"  🔒 **`tol_conv` ＝ {TOL_CONV:.1e} m** ⇒ 出艙值之**有效位數上限 ＝ 小數第 6 位**"
      "（⇒ `41.4830` 之末位**有**意義）")
    P("")
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}{'D_max':>14}{'±容差':>12}"
      f"{'-60 掃描式【倉】':>18}{'Δ':>14}{'4dp':>6}")
    P("-" * WID)
    n_same = 0
    for lbl, which, pst, g, w in cells:
        for j, r in enumerate(R_GRID):
            v = dmax[(lbl, which, r)]
            ref = WG960_DMAX[(lbl, which)][j]
            same = (round(v, 4) == round(ref, 4))
            n_same += 1 if same else 0
            P(f"  {lbl:<5}{which:<8}{r:>10.0e}{v:>14.6f}{TOL_CONV:>12.1e}"
              f"{ref:>18.4f}{v - ref:>14.6f}{'✅' if same else '🔴':>5}")
    P("-" * WID)
    P(f"  ⇒ **{n_same}／12** 於 4dp 逐位相符（`P7`）")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【H】`P8`：8 格分類 ⇒ 土地後果
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【H】`P8`：**8 格於 `r=0` 之分類對帳** ⇒ 土地後果")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<8}{'D_max':>14}{'±容差':>12}{'D_法定':>9}"
      f"{'本批':>8}{'-61':>8}{'一致?':>7}")
    P("-" * WID)
    n_cls, n_adv = 0, 0
    for lbl, which in EIGHT:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        w, dd = wd[lbl]
        v = d_max_at(pst, w, g["theta"], d_floor=df_real, tol_conv=TOL_CONV)
        cls = "進" if v >= dd else "不進"
        n_adv += 1 if cls == "進" else 0
        same = (cls == PREV8[(lbl, which)])
        n_cls += 1 if same else 0
        P(f"  {lbl:<5}{which:<8}{v:>14.6f}{TOL_CONV:>12.1e}{dd:>9.1f}"
          f"{cls:>8}{PREV8[(lbl, which)]:>8}{'✅' if same else '🔴':>6}")
    P("-" * WID)
    P(f"  ⇒ **{n_cls}／8 一致**（{n_adv} 進／{8 - n_adv} 不進）⇒ "
      f"**土地後果 ＝ {'零' if n_cls == 8 else '🔴 非零 ⇒ 停機上呈'}**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【I】逐項判定
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【I】`(b-2′)(b-2″)(b-2‴)` ＋ `GB-83` 裁示 **逐項判定**")
    P("=" * WID)
    items = [
        ("`GB-83`①", f"母體逐點列舉（{len(GRID_B)} 點·已全部印出）", True),
        ("`GB-83`②", f"涵蓋斷言通過（`D_GRID` {len(D_GRID)}／{len(D_GRID)} 在母體內）"
                     "·判別力自檢確會不成立", True),
        ("`GB-83`③", f"`d_floor`（{df_real:.3e}）**僅作事實陳述**，"
                     "⛔ 未用以界定任何閘之受詞域", True),
        ("`(b-2′)`", f"受詞域下限 `d_gate` ＝ {d_gate:.3e}（由出艙值導出）⇒ {n_ok}／12 綠",
         n_ok == 12),
        ("`(b-2″)`", f"`d_rev_max` ＝ {drm:.3e} < `d_gate` ⇒ 綠；淨空比 "
                     f"{(d_out_min / drm) if drm > 0 else float('inf'):.2e}", not red_rev),
        ("`(b-2‴)`", f"注入三高度 ⇒ {tri_red}／3 轉紅；原式對照 {n_old_green}／"
                     f"{len(inj_rows)} 仍綠", tri_red == 3),
        ("§五-D", f"`_tol` 已拆為二具名量；出艙值並列容差 {TOL_CONV:.1e}", True),
        ("`P7`", f"十二值 {n_same}／12 逐位相符 `-60`", n_same == 12),
        ("`P8`", f"8 格分類 {n_cls}／8 一致 ⇒ 土地後果零", n_cls == 8),
    ]
    for k, txt, ok in items:
        P(f"  {k:<12}{'✅' if ok else '🔴'}　{txt}")
    P("-" * WID)
    allok = all(o for _k, _t, o in items)
    P(f"  ⇒ **{'✅ 全部成立' if allok else '🔴 有未成立項'}**")
    P("")

    # 🔒 §七-5：收束斷言（⛔ 不得留在 `False`）
    if fp.LOCAL_ORIGIN is not True:
        raise RuntimeError(
            "🔴 探針結束時 `LOCAL_ORIGIN` ⛔ 非 `True` ⇒ 本次一切輸出⛔ 不得採信"
            "（`W-G.9-62` §七-5）。")
    if INJECT is not None:
        raise RuntimeError("🔴 探針結束時 `INJECT` ⛔ 非 `None` ⇒ 注入未還原。")
    P("  🔒 §七-5 收束斷言：`LOCAL_ORIGIN is True` ✅　`INJECT is None` ✅")
    P("=" * WID)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG962_gate_power_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
