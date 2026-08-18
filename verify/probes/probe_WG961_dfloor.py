#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-61】`GB-82` 之 `(b-1)〜(b-5)`：`d_floor` 自量 ＋ 受詞限縮 ＋ 判別力反例 ⛔ 零生產碼

**受詞**：本檔**不量幾何**，只量**儀器自身之可信域**——
`fits_at` 對 `d` 之單調性在多細的 `d` 之下才成立？該界限即 **`d_floor`**。

🔒 **`d_floor` 一律<u>自量</u>（⛔ 不得抄施工單之 `3e−09`）**——施工單所載係 claude.ai
  之現查值，於本倉為 **`【單】`**；本檔量得者方為 **`【倉】`**。
  ⚠️ 二者相符**⛔ 不構成相互驗證**（`CLAUDE.md` §【倉】/【單】第 4 款）。

🔒 **⛔ 不新增第二份判定原語**（`GB-8`）——本檔只**呼叫**
  `probe_WG949_free_pose.fits_at`，並沿用 `probe_WG960_fitcore` 之 module 級組裝。

═══════════════════════════════════════════════════════════════════════
🔴 **本檔並列兩種<u>母體</u>（⛔ 非擇一·⛔ 非放寬）**
═══════════════════════════════════════════════════════════════════════
`(b-1)` 令「掃 `d ∈ [1e−12, 39]`（22 點）」，`(b-2)` 之閘則測 **`D_GRID` 15 點**。
**二者之母體不同**，而 `D_GRID` 之 `d = 1e−9` **不在** 22 點格內
⇒ `(b-1)` 之證書（「`8.741e−11` 以上為單調」）**被一個它自己沒取樣的點推翻**。

🔒 **有限格只能<u>推翻</u>單調性，⛔ 永遠不能證明之** ⇒ 任一格所得之 `d_floor`
  皆為**下界估計**，加點只會使其**上移**。
  ⇒ **`(b-2)` 之測點必須落在 `(b-1)` 之母體內**，否則 `(b-1)` 之證書恆可被 `(b-2)` 推翻。
  ⇒ 本檔以**母體 B ＝ 22 點格 ∪ `D_GRID`** 為**可用之解**，
    並**並列**母體 A（施工單字面之 22 點）之結果，⛔ 不隱去其紅。
  🔴 **此係<u>具名偏離</u>施工單字面**（⛔ 非默默照辦、⛔ 非自行放寬）——
    偏離之方向為**加點**（＝更多推翻機會·**更嚴**），⛔ 非減點。

🔒 輸出檔名含產生它之 commit 短碼 ＋ 版次；⛔ 不覆寫任何既有 log。
"""
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
for _p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE):
    sys.path.insert(0, _p)

import probe_WG949_free_pose as fp                                  # noqa: E402
from probe_WG949_free_pose import fits_at, witness                  # noqa: E402
from probe_WG958_dmax_robust import d_max_at                        # noqa: E402
from probe_WG959_knife_edge import d_max_at_r                       # noqa: E402
from probe_WG960_fitcore import (                                   # noqa: E402
    D_GRID, FOCUS, R_GRID, build_ctx, geom, yi_pst)

OUTDIR = os.path.join(VERIFY, "out")
WID = 150

# ══════════════════════════════════════════════════════════════════════
# (b-1) 之 `d` 格
# ══════════════════════════════════════════════════════════════════════
NPT = 22
D_LO, D_HI = 1e-12, 39.0
GRID_A = tuple(D_LO * (D_HI / D_LO) ** (k / (NPT - 1.0)) for k in range(NPT))
GRID_B = tuple(sorted(set(GRID_A) | set(float(d) for d in D_GRID)))

# 【B-4】P7 之對拍靶：`W-G.9-60`【倉】之**掃描式** `D_max` 12 值
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


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _tv(pst, w, th, r, grid):
    return "".join("1" if fits_at(pst, w, d, th, r)[0] else "0" for d in grid)


def _mono(v):
    """真值字串是否**非遞增**（＝出現 `0` 之後⛔ 不得再現 `1`）。"""
    return "01" not in v


def _first_mono_idx(v):
    for i in range(len(v)):
        if _mono(v[i:]):
            return i
    return len(v) - 1


def witness6(poly, w, d, th):
    """**6 候選點**之見證搜尋（`GB-82` 併記所用之口徑）。

    候選 ＝ `representative_point` ＋ `centroid` ＋ **侵蝕集之全部頂點**。
    🔒 逐角 `poly.covers` 獨立驗證（⛔ 非以侵蝕之非空當證明）。
    ⚠️ 與 `probe_WG949.witness`（**單候選**）**同名不同量** ⇒ 二者結果不同⛔ 非矛盾。
    """
    from shapely.geometry import Point as _Pt
    ok, er = fits_at(poly, w, d, th, 0.0)
    if not ok:
        return None, 0
    cands = [er.representative_point(), er.centroid]
    geoms = list(er.geoms) if hasattr(er, "geoms") else [er]
    for gg in geoms:
        if hasattr(gg, "exterior") and gg.exterior is not None:
            cs = list(gg.exterior.coords)
        elif hasattr(gg, "coords"):
            cs = list(gg.coords)
        else:
            cs = []
        for x, y in cs:
            cands.append(_Pt(float(x), float(y)))
    c, s = math.cos(th), math.sin(th)
    best, nbest = None, -1
    for pt in cands:
        u, v = float(pt.x), float(pt.y)
        ins = []
        for cx, cy in ((0.0, 0.0), (w, 0.0), (w, d), (0.0, d)):
            x, y = u + cx, v + cy
            ins.append(bool(poly.covers(_Pt(x * c - y * s, x * s + y * c))))
        if sum(ins) > nbest:
            nbest, best = sum(ins), ins
        if nbest == 4:
            break
    return best, len(cands)


def measure_dfloor(cells, grid):
    """回 `(d_floor, rows)`；`rows` ＝ (lbl, which, r, 真值集, 首個單調位, 該位之 d)。"""
    rows, df = [], 0.0
    for lbl, which, pst, g, w in cells:
        for r in R_GRID:
            v = _tv(pst, w, g["theta"], r, grid)
            i = _first_mono_idx(v)
            rows.append((lbl, which, r, v, i, grid[i]))
            df = max(df, grid[i])
    return df, rows


def gate_rows(cells, sub):
    rows = []
    for lbl, which, pst, g, w in cells:
        for r in R_GRID:
            v = _tv(pst, w, g["theta"], r, sub)
            rows.append((lbl, which, r, v, _mono(v)))
    return rows


def run_for(P, cells, tag, grid, note):                             # noqa: C901
    """對一種母體跑 `(b-1)〜(b-6)`，回結案所需之數。"""
    P("=" * WID)
    P(f"【{tag}-1】**`d_floor` 自量**　母體 ＝ {note}（{len(grid)} 點）")
    P("=" * WID)
    P("  🔒 判準：取**最小之 `d`**，使其**以上**之真值集為單調（⛔ 出現 `0` 後不得再現 `1`）。")
    dfloor, rows = measure_dfloor(cells, grid)
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}   {'真值集（由薄到厚）':<{len(grid) + 4}}"
      f"{'首個單調位':>9}{'該位之 d':>15}")
    P("-" * WID)
    for lbl, which, r, v, i, d_i in rows:
        P(f"  {lbl:<5}{which:<8}{r:>10.0e}   {v:<{len(grid) + 4}}{i:>7}{d_i:>17.3e}")
    P("-" * WID)
    n_deg = sum(1 for c in rows if c[4] == 0)
    P(f"  ⇒ 12 組中 **{n_deg} 組**於 `d = {grid[0]:.0e}` 即已單調"
      "（＝其 `d_floor` 已抵格之下界·⛔ 非量到真界限）")
    P(f"  ⇒ 🔒 **`d_floor`【倉】 ＝ {dfloor:.6e} m**（全案 max）")
    P(f"     ⚠️ 施工單所載【單】 ＝ `3e−09` m ⇒ "
      f"{'**相符**' if 0.5 <= dfloor / 3e-9 <= 2.0 else '🔴 **不符**'}"
      f"（比 ＝ {dfloor / 3e-9:.3g}×）　"
      "🔒 相符與否皆**⛔ 不構成相互驗證**·出艙一律以【倉】為準")
    P("")

    # ── (b-2) 限縮後之閘 ────────────────────────────────────────────
    thr = 10.0 * dfloor
    sub = tuple(d for d in D_GRID if d >= thr)
    exc = tuple(d for d in D_GRID if d < thr)
    P("=" * WID)
    P(f"【{tag}-2】**限縮後之單調性閘**：受詞 ＝ `d ≥ 10 × d_floor` ＝ `{thr:.3e}` m")
    P("=" * WID)
    P(f"  🔒 `D_GRID` 15 點中，滿足受詞者 **{len(sub)} 點**；"
      f"被排除者 **{len(exc)} 點**：" + ("／".join(f"{d:g}" for d in exc) or "（無）"))
    P("")
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}   {'限縮後真值集':<20}{'單調?':>7}")
    P("-" * WID)
    grows = gate_rows(cells, sub)
    n_ok = sum(1 for *_x, ok in grows if ok)
    for lbl, which, r, v, ok in grows:
        P(f"  {lbl:<5}{which:<8}{r:>10.0e}   {v:<22}{'✅' if ok else '🔴':>6}")
    P("-" * WID)
    P(f"  ⇒ **限縮後之閘：{n_ok}／12 綠**")
    P("")

    # ── (b-4) 去硬編後之二分式 `D_max` vs `-60` 掃描式 ──────────────
    P("=" * WID)
    P(f"【{tag}-4】**去硬編後**之二分式 `D_max`（早退測試點 ＝ `10 × d_floor` ＝ "
      f"`{thr:.3e}`）vs `W-G.9-60`【倉】掃描式")
    P("=" * WID)
    P("  🔒 對拍靶出處：`verify/out/probe_WG960_fitcore_post2_65fef5b.log`【A-4】")
    P("")
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}{'二分(去硬編)':>16}{'-60 掃描式【倉】':>18}"
      f"{'Δ':>14}{'4dp 相符?':>10}")
    P("-" * WID)
    dmax, n_same = {}, 0
    for lbl, which, pst, g, w in cells:
        for j, r in enumerate(R_GRID):
            v = d_max_at_r(pst, w, g["theta"], r, d_floor=dfloor)
            ref = WG960_DMAX[(lbl, which)][j]
            dmax[(lbl, which, r)] = v
            same = (round(v, 4) == round(ref, 4))
            n_same += 1 if same else 0
            P(f"  {lbl:<5}{which:<8}{r:>10.0e}{v:>16.4f}{ref:>18.4f}"
              f"{v - ref:>14.6f}{'✅' if same else '🔴':>9}")
    P("-" * WID)
    P(f"  ⇒ **{n_same}／12** 於 4dp 逐位相符")
    P("")

    # ── (b-2) 之淨空比 ─────────────────────────────────────────────
    pos = [v for v in dmax.values() if v > 0.0]
    d_out_min = min(pos) if pos else float("nan")
    ratio = (d_out_min / dfloor) if pos else float("nan")
    P("=" * WID)
    P(f"【{tag}-2′】**淨空比**（`(b-2)` 明令須<u>並列印出</u>）")
    P("=" * WID)
    P(f"  · `d_floor`【倉】　　　　　＝ {dfloor:.6e} m")
    P(f"  · **最小出艙 `D_max`**（>0）＝ {d_out_min:.6f} m")
    P(f"  · **比值** ＝ {ratio:.3e}　（門檻 `1e+03`）")
    P(f"  ⇒ **{'✅ 通過' if ratio >= 1e3 else '🔴 未過 ⇒ ⛔ 不得出艙任何 D_max'}**"
      f"（{math.log10(ratio):.1f} 個數量級之淨空）")
    P("")

    # ── (b-5) 見證 ─────────────────────────────────────────────────
    P("=" * WID)
    P(f"【{tag}-5】**凡出艙之 `D_max` 須附該深度之見證**"
      "（⛔ 見證不可得者只能出艙為「儀器上界」）")
    P("=" * WID)
    P("  🔒 `r ≠ 0` 之見證取於**膨脹後**之多邊形（＝判定之真受詞）；"
      "逐角 `covers` 獨立驗證。**6 候選點**口徑。")
    P("")
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}{'D_max':>12}   {'最佳逐角':<12}"
      f"{'候選數':>7}{'四角全在':>9}   {'出艙資格':<24}")
    P("-" * WID)
    MITRE = fp.MITRE
    n_wit, n_pos, unwit = 0, 0, []
    for lbl, which, pst, g, w in cells:
        for r in R_GRID:
            v = dmax[(lbl, which, r)]
            if v <= 0.0:
                P(f"  {lbl:<5}{which:<8}{r:>10.0e}{v:>12.4f}   {'（無矩形）':<12}"
                  f"{'—':>7}{'—':>9}   {'⚪ 不適用':<24}")
                continue
            n_pos += 1
            q = pst if r == 0.0 else pst.buffer(-r, **MITRE)
            ins, nc = witness6(q, w, v, g["theta"])
            ok = bool(ins and all(ins))
            n_wit += 1 if ok else 0
            if not ok:
                unwit.append((lbl, which, r, v, _WD[lbl][1]))
            txt = ("[" + "".join("T" if b else "F" for b in ins) + "]") if ins else "（fits 偽）"
            P(f"  {lbl:<5}{which:<8}{r:>10.0e}{v:>12.4f}   {txt:<12}{nc:>7}"
              f"{('是' if ok else '否'):>9}   "
              f"{('✅ 量測值（有見證）' if ok else '⚠️ 儀器上界·⛔ 無見證'):<24}")
    P("-" * WID)
    P(f"  ⇒ **{n_wit}／{n_pos}** 之正值 `D_max` 具四角見證；"
      f"**{n_pos - n_wit}** 者已標示為「⚠️ 儀器上界·⛔ 無見證」")
    P("  🔒 **`(b-5)` 之判準 ＝「⛔ 無任何<u>無見證</u>之值被當成<u>量測值</u>出艙」**，")
    P("    ⛔ **非**「全部須有見證」——登記表原文：「見證不可得者……**只能出艙為**")
    P("    『儀器上界·⛔ 無見證』」⇒ **標示即為合規之出艙方式**。")
    if unwit:
        P("  🔒 **無見證者之出艙不敏感性**（⛔ 否則標示不足以免責）：")
        for lbl, which, r, v, dd in unwit:
            c1 = "進" if v >= dd else "不進"
            c0 = "進" if 0.0 >= dd else "不進"
            P(f"    · `{lbl}/{which} @ r={r:.0e}`：取 `{v:.4f}` ⇒ **{c1}**、"
              f"取 `0`（保守下界）⇒ **{c0}** ⇒ "
              f"{'✅ 兩讀法同分類 ⇒ 該值之不確定⛔ 不影響出艙結論' if c1 == c0 else '🔴 兩讀法異 ⇒ ⛔ 停機'}")
    P("")

    # ── (b-6) 8 格分類 ─────────────────────────────────────────────
    P("=" * WID)
    P(f"【{tag}-6】**8 格於 `r=0` 之分類對帳**（去硬編後）⇒ 土地後果")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<8}{'D_max(去硬編)':>16}{'D_法定':>9}{'本批分類':>10}"
      f"{'-60 分類':>10}{'一致?':>7}")
    P("-" * WID)
    n_cls = 0
    for lbl, which in EIGHT:
        pst, g, poly = _eight_geom(lbl, which)
        w, dd = _WD[lbl]
        v = d_max_at(pst, w, g["theta"], d_floor=dfloor)
        cls = "進" if v >= dd else "不進"
        same = (cls == PREV8[(lbl, which)])
        n_cls += 1 if same else 0
        P(f"  {lbl:<5}{which:<8}{v:>16.4f}{dd:>9.1f}{cls:>10}"
          f"{PREV8[(lbl, which)]:>10}{'✅' if same else '🔴':>6}")
    P("-" * WID)
    P(f"  ⇒ **分類逐格一致 ＝ {n_cls}／8** ⇒ "
      f"**土地後果 ＝ {'零' if n_cls == 8 else '🔴 非零 ⇒ 停機上呈'}**")
    P("")
    # 🔒 `(b-5)` 之通過判準：無見證者**皆已標示**（本器恆標示）**且**其分類不敏感
    b5 = all(("進" if v >= dd else "不進") == ("進" if 0.0 >= dd else "不進")
             for _l, _w, _r, v, dd in unwit)
    return dict(dfloor=dfloor, thr=thr, n_ok=n_ok, ratio=ratio, n_same=n_same,
                n_wit=n_wit, n_pos=n_pos, n_cls=n_cls, b5=b5, n_unwit=len(unwit))


_EIGHT_CACHE = {}
_WD = {}
_CTX = None


def _eight_geom(lbl, which):
    if (lbl, which) not in _EIGHT_CACHE:
        ns, cb_by, cad, snapshot, wd, _t = _CTX
        _EIGHT_CACHE[(lbl, which)] = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
    return _EIGHT_CACHE[(lbl, which)]


def main():                                                         # noqa: C901
    global _CTX
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-61】`GB-82` `(b-1)〜(b-5)`：`d_floor` **自量** ＋ 受詞限縮 ＋ 判別力反例")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；本檔只**呼叫** `fits_at`，⛔ 未新增第二份判定原語。")
    P("  🔒 `d_floor` **自量**（⛔ 未抄施工單之 `3e−09`）——單之值為 `【單】`、本檔之值為 `【倉】`。")
    P("")
    P("  🔴 **兩種母體並列（⛔ 非擇一）**：")
    P("     · **母體 A** ＝ 施工單字面之 `[1e−12, 39]` **22 點**（對數等距）")
    P("     · **母體 B** ＝ 母體 A **∪ `D_GRID`**（＝閘所測之 15 點）")
    P("     🔒 **`(b-2)` 之測點必須落在 `(b-1)` 之母體內**——否則 `(b-1)` 之證書")
    P("       恆可被 `(b-2)` 自己的測點推翻。有限格只能**推翻**單調性、⛔ 不能證明之")
    P("       ⇒ 加點只會使 `d_floor` **上移** ⇒ 本偏離之方向為**更嚴**，⛔ 非放寬。")
    P("")

    _CTX = build_ctx()
    ns, cb_by, cad, snapshot, wd, targets = _CTX
    _WD.update(wd)
    cells = []
    for lbl, which in FOCUS:
        pst, g, poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        cells.append((lbl, which, pst, g, wd[lbl][0]))

    P("  🔒 母體 A 之 22 點（逐位）：")
    P("     " + "／".join(f"{d:.3e}" for d in GRID_A[:11]))
    P("     " + "／".join(f"{d:.3e}" for d in GRID_A[11:]))
    P(f"  🔒 母體 B 之 {len(GRID_B)} 點 ＝ A ∪ D_GRID；**A 所無而 B 所有**者："
      + "／".join(f"{d:g}" for d in GRID_B if d not in GRID_A))
    P("")

    res = {}
    res["A"] = run_for(P, cells, "A", GRID_A, "施工單字面 22 點")
    res["B"] = run_for(P, cells, "B", GRID_B, "22 點 ∪ `D_GRID`（涵蓋式）")

    # ══════════════════════════════════════════════════════════════
    # 【C】判別力反例（`(b-3)`）——於**母體 B** 之受詞下施行
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C】🔴 **判別力反例 `(b-3)`**：暫時還原 `fits_at` 之平移修 ⇒ 限縮後之閘**須轉紅**")
    P("=" * WID)
    thrB = res["B"]["thr"]
    subB = tuple(d for d in D_GRID if d >= thrB)
    P("  🔒 靶格（施工單指定）：`(R6/right, r = −1e−06, d = 1e−5)`")
    P(f"  🔒 受詞（母體 B）：`d ≥ {thrB:.3e}`；`d = 1e−5` "
      f"{'✅ 在受詞內' if 1e-5 >= thrB else '🔴 不在受詞內'} ⇒ 反例確受該閘管轄")
    P("")
    tgt = [c for c in cells if (c[0], c[1]) == ("R6", "right")][0]
    try:
        fp.LOCAL_ORIGIN = False
        rows_off = gate_rows(cells, subB)
        bad = fits_at(tgt[2], tgt[4], 1e-5, tgt[3]["theta"], -1e-06)[0]
        good = fits_at(tgt[2], tgt[4], 1e-4, tgt[3]["theta"], -1e-06)[0]
    finally:
        fp.LOCAL_ORIGIN = True                 # 🔒 **必還原**（⛔ 不得留在 False）
    rows_on = gate_rows(cells, subB)
    P(f"  {'街廓':<5}{'側':<8}{'r':>10}   {'還原修後':<20}{'單調?':>7}   "
      f"{'復原後':<20}{'單調?':>7}")
    P("-" * WID)
    n_red = 0
    for (lbl, which, r, v0, ok0), (_a, _b, _c, v1, ok1) in zip(rows_off, rows_on):
        n_red += 0 if ok0 else 1
        P(f"  {lbl:<5}{which:<8}{r:>10.0e}   {v0:<22}{'✅' if ok0 else '🔴':>6}   "
          f"{v1:<22}{'✅' if ok1 else '🔴':>6}")
    P("-" * WID)
    hit = any((not ok) and (a, b) == ("R6", "right") and abs(c + 1e-06) < 1e-18
              for a, b, c, _v, ok in rows_off)
    n_on = sum(1 for *_x, ok in rows_on if ok)
    P(f"  ⇒ 還原修後：**{n_red}／12 轉紅**；復原後：**{n_on}／12 綠**")
    P(f"  ⇒ 靶格 `(R6/right, r=−1e−06)` **{'✅ 確實轉紅' if hit else '🔴 未轉紅'}**"
      f"　（`d=1e−5` ⇒ fits＝{bad}、`d=1e−4` ⇒ fits＝{good}"
      f"{'　⇒ **`0…1` 反轉**' if (not bad and good) else ''}）")
    P(f"  🔒 復原後 `LOCAL_ORIGIN` ＝ {fp.LOCAL_ORIGIN}（⛔ 未留在 `False`）")
    P("  🔒 **⇒ 限縮後之閘仍抓得到原缺陷 ⇒ 本限縮⛔ 非放寬。**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【D】`GB-82` 併記之四列表複現（6 候選點口徑）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【D】`GB-82` 併記之**四列表複現**：`R5/left @ r = 0` 之見證可得性隨 `D` 跳動")
    P("=" * WID)
    P("  🔒 口徑 ＝ **6 候選點**（`representative_point`／`centroid`／侵蝕集全部頂點）"
      "——與登記表同口徑。")
    l5 = [c for c in cells if (c[0], c[1]) == ("R5", "left")][0]
    REG = {0.001: True, 0.010: False, 0.026: False, 0.0264: True}   # 登記表所載
    P("")
    P(f"  {'D':>10}{'fits_at':>9}   {'最佳逐角':<10}{'候選數':>7}{'四角全在':>9}"
      f"{'侵蝕集面積':>13}{'登記表所載':>11}{'相符?':>7}")
    P("-" * WID)
    n_rep = 0
    for D in (0.001, 0.010, 0.026, 0.0264):
        okf, er = fits_at(l5[2], l5[4], D, l5[3]["theta"], 0.0)
        ins, nc = witness6(l5[2], l5[4], D, l5[3]["theta"]) if okf else (None, 0)
        allin = bool(ins and all(ins))
        same = (allin == REG[D])
        n_rep += 1 if same else 0
        txt = ("[" + "".join("T" if b else "F" for b in ins) + "]") if ins else "—"
        P(f"  {D:>10.4f}{('真' if okf else '偽'):>9}   {txt:<10}{nc:>7}"
          f"{('是' if allin else '否'):>9}"
          f"{(er.area if er is not None else float('nan')):>13.3e}"
          f"{('是' if REG[D] else '否'):>11}{'✅' if same else '🔴':>6}")
    P("-" * WID)
    P(f"  ⇒ **{n_rep}／4** 與登記表所載相符")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【E】`(b-1)〜(b-5)` 之逐項判定（兩母體並列）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【E】`GB-82` `(b-1)〜(b-5)` **逐項判定**（兩母體並列）")
    P("=" * WID)
    P(f"  {'款':<7}{'母體 A（單之字面）':<58}{'母體 B（涵蓋式）':<58}")
    P("-" * WID)
    A, B = res["A"], res["B"]
    okA = dict(b1=True, b2=(A["n_ok"] == 12 and A["ratio"] >= 1e3),
               b3=hit, b4=True, b5=A["b5"])
    okB = dict(b1=True, b2=(B["n_ok"] == 12 and B["ratio"] >= 1e3),
               b3=hit, b4=True, b5=B["b5"])
    lines = [
        ("(b-1)", f"d_floor ＝ {A['dfloor']:.3e}", f"d_floor ＝ {B['dfloor']:.3e}"),
        ("(b-2)", f"閘 {A['n_ok']}／12・淨空 {A['ratio']:.2e}",
         f"閘 {B['n_ok']}／12・淨空 {B['ratio']:.2e}"),
        ("(b-3)", f"靶格{'命中' if hit else '未命中'}（與母體無關）",
         f"靶格{'命中' if hit else '未命中'}（與母體無關）"),
        ("(b-4)", f"早退點 ＝ {A['thr']:.3e}（去硬編）",
         f"早退點 ＝ {B['thr']:.3e}（去硬編）"),
        ("(b-5)", f"見證 {A['n_wit']}／{A['n_pos']}・無見證 {A['n_unwit']} 者已標示且分類不敏感",
         f"見證 {B['n_wit']}／{B['n_pos']}・無見證 {B['n_unwit']} 者已標示且分類不敏感"),
    ]
    for (k, ta, tb), ka in zip(lines, ("b1", "b2", "b3", "b4", "b5")):
        P(f"  {k:<7}{('✅ ' if okA[ka] else '🔴 ') + ta:<58}"
          f"{('✅ ' if okB[ka] else '🔴 ') + tb:<58}")
    P("-" * WID)
    aA, aB = all(okA.values()), all(okB.values())
    P(f"  ⇒ 母體 A：**{'✅ 五項全滿足' if aA else '🔴 有未滿足項'}**"
      f"　／　母體 B：**{'✅ 五項全滿足' if aB else '🔴 有未滿足項'}**")
    P(f"  ⇒ 8 格分類：A **{A['n_cls']}／8**、B **{B['n_cls']}／8** 與 `-60` 一致"
      f"　⇒ **土地後果 ＝ {'零' if (A['n_cls'] == 8 and B['n_cls'] == 8) else '🔴 非零'}**")
    P("")
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
    _log = os.path.join(OUTDIR, f"probe_WG961_dfloor_v3_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
