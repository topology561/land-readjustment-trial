#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-49】自由姿態之矩形容納（`K-9-12` ＋ KL 2026-08-17 之自陳更正）⛔ 零生產碼

**受詞**：`∃ θ ∈ [0, π)` 與平移 `(u, v)`，使 `W × D` 矩形**整個落在宗地四至範圍內**
⇒ **可建築**。**⛔ 姿態無約束**（可旋轉、可平移、⛔ 不須貼齊 FRONTLINE）。

🔴 **證明義務之不對稱（本檔之核心）**：
  · **判「進」** ⇒ 須具名**見證矩形**（`θ` ＋ 四角座標），並**逐角獨立驗證**其在宗內
    （⛔ 不以侵蝕之非空當證明——那是同一次計算）。
  · **判「不進」** ⇒ 掃描找不到 **⛔ 不等於不存在**。須附 **Lipschitz 證書**。

**餘裕函數 `m(θ)` 之定義（⛔ 具名·⛔ 非啟發式）**：
    `m(θ) := sup { r ∈ ℝ : W×D 之軸對齊盒可置入 erode(rot(P, −θ), r) }`
  其中 `erode(Q, r) = Q.buffer(−r, join_style=mitre)`（`r < 0` 即膨脹）。
  · **`m(θ) ≥ 0 ⟺ 該 θ 可容納`**（`r = 0` 即原宗地）。
  · **幾何意義**：矩形四角**距宗地邊界之最小內距**之最大可達值。
  · **計算式**：對 `r` 之**二分搜尋**——`fits(r)` 對 `r` **單調遞減**
    （`r` 愈大 ⇒ `erode` 愈小 ⇒ 愈難置入）⇒ 二分精確至 `TOL_M`。

**Lipschitz 常數**：矩形繞其中心轉 `dθ`，各角位移 `≤ R·dθ`，
  `R = √(W² + D²)/2`（＝半對角線·本案 **7.215469 m/rad**）；
  而「距邊界之距離」對位置為 **1-Lipschitz** ⇒ `|m(θ₁) − m(θ₂)| ≤ R·|θ₁ − θ₂|`。
**證書**：以步長 `Δθ` 掃描 `[0, π)`，令 `ε := −max_k m(θ_k)`。
  若 `ε > R·Δθ/2` ⇒ **任意 θ 之 `m(θ) ≤ −ε + R·Δθ/2 < 0`** ⇒ **證明無解**。
  🔒 週期為 **π**（`W ≠ D` ⇒ ⛔ **不可**再減為 `[0, π/2)`）。

🔒 `W`／`D` 一律 `get_min_lot_size` 取得（⛔ 無字面量 `3.5`／`14`）。
🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
from probe_WG941_bandbase import st_frame                           # noqa: E402
# 🔒 **沿用 `-47` 已驗收之侵蝕實作**（⛔ 不另寫第二份·`GB-8`）
from probe_WG947_rect_fit import rect_fits, _poly_st                # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 176
SB = 0.0
# 掃描步長之**階梯**（rad·由粗到細）——⛔ 非逕採單之建議值 `1e-4`，見【B-3a】
STEPS = (2e-2, 5e-3, 1e-3, 2e-4, 1e-4)
DTHETA = STEPS[-1]     # 最細步長（＝單之建議值·作為階梯之終點）
TOL_M = 1e-4           # `m(θ)` 二分之收斂容差（m）——回**上界** ⇒ 偏保守
MITRE = dict(join_style=2, mitre_limit=1e7)
# 🔒 `GB-82` 之修（`W-G.9-60`）之開關——⛔ **生產路徑恆 `True`**；
#   置 `False` 僅供 `GB-82` (b-3) 之**判別力反例**（證限縮後之閘仍抓得到原缺陷）。
LOCAL_ORIGIN = True


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _rot(p, th):
    from shapely.affinity import rotate as _r
    return _r(p, th, origin=(0.0, 0.0), use_radians=True)


def fits_at(poly, w, d, th, r=0.0):
    """`erode(rot(P, −θ), r)` 內能否置入軸對齊 `w × d` 盒。回 `(bool, 侵蝕集)`。

    🩸 **`GB-82` 之就地修復（`W-G.9-60` §A-2）**：判定**先平移至局部原點**再進行。
      **案由**：本案座標為 TWD97 絕對值（`~2.17e6`〜`2.65e6`），而 `buffer(+1e−06)` 後
      前二角之交集為一條**寬 `2e−06`** 之細條 ⇒ 細條寬／座標量級 `≈ 1e−12`
      **已抵 `double` 之懸崖** ⇒ GEOS 於 `d = 1e−5` 回空、於 `d = 1e−4` 回非空
      ⇒ **`fits_at` 對 `d` 不單調**（薄者判不進而厚者判進·幾何上不可能）。
      ⇒ 一切建於其上之**二分**，其前提為偽。
    🔒 **⛔ 未新增第二份判定原語**（`GB-8` 之受詞裁定：其所禁者為「並存兩份」，
      ⛔ 非「修復既有之唯一原語」）——本函式**就地**修復、`MITRE` 一字未改。

    🔴 **偏離施工單之一處（⛔ 具名·`W-G.9-60` CC）**：單令「判定完成後 ⛔ 不還原」。
      **判定之布林**確實對平移嚴格不變，惟**本函式之回傳幾何有下游消費者**
      ——`witness()` 取 `er.representative_point()` 並映射回**原框**以做逐角 `poly.covers`。
      若不還原，**每一個見證之四角都會偏移一個形心向量** ⇒ **見證全毀**
      （而見證正是本倉判「進」之唯一證明義務）。
      ⇒ 🔒 **折衷**：**判定於局部原點**（＝數值修復之所在），
      **回傳之幾何還原至原框**（＝保既有呼叫端契約·`witness` 免改）。
    """
    from shapely.affinity import translate as _tr
    # ── 平移至局部原點（⇒ 判定於小座標下進行）──────────────────────────
    # 🔒 **`LOCAL_ORIGIN` 係<u>判別力反例</u>之開關**（`W-G.9-61` `GB-82` (b-3)）：
    #   置 `False` 即**暫時還原**本修，用以證「限縮後之閘仍抓得到原缺陷」。
    #   ⚠️ **⛔ 生產路徑一律 `True`**；切換者須以 `try/finally` 還原（⛔ 不得留在 False）。
    _c = poly.centroid
    _cx, _cy = (float(_c.x), float(_c.y)) if LOCAL_ORIGIN else (0.0, 0.0)
    q = _rot(_tr(poly, xoff=-_cx, yoff=-_cy), -th)
    if r != 0.0:
        q = q.buffer(-r, **MITRE)
        if q.is_empty:
            return False, None
    cur = None
    for cx, cy in ((0.0, 0.0), (w, 0.0), (0.0, d), (w, d)):
        t = _tr(q, xoff=-cx, yoff=-cy)
        cur = t if cur is None else cur.intersection(t)
        if cur.is_empty:
            return False, None
    # ── 回傳幾何還原至**原框**（rot(P−c) ＝ rot(P) − rot(c) ⇒ 加回 rot(c)）──
    _co, _si = math.cos(-th), math.sin(-th)
    _rcx = _cx * _co - _cy * _si
    _rcy = _cx * _si + _cy * _co
    return True, _tr(cur, xoff=_rcx, yoff=_rcy)


def margin_ub(poly, w, d, th, tol=TOL_M):
    """回 `m(θ)` 之**嚴格上界**（⛔ 非近似值——證書須用上界方為證明）。

    二分維持不變式 `fits(lo) 為真、fits(hi) 為假` ⇒ `m ∈ [lo, hi)` ⇒ **回 `hi`**。
    🔒 用**上界**之由：證書之推論為「`max m ≤ −ε`」，
      以上界代入只會使 `ε` **偏小**（＝**偏保守**）⇒ 證書若成立則**確實成立**。
    """
    lo = -(w + d)                       # 必 fits（大幅膨脹）
    hi = 0.5 * max(poly.bounds[2] - poly.bounds[0], poly.bounds[3] - poly.bounds[1]) + 1.0
    if not fits_at(poly, w, d, th, lo)[0]:
        return lo                       # 連大幅膨脹都塞不進 ⇒ 回下界（⛔ 不謊報）
    if fits_at(poly, w, d, th, hi)[0]:
        return hi
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if fits_at(poly, w, d, th, mid)[0]:
            lo = mid
        else:
            hi = mid
    return hi


def witness(poly, w, d, th):
    """回見證矩形之四角（**原框**座標）＋ 逐角獨立驗證之結果。"""
    ok, er = fits_at(poly, w, d, th, 0.0)
    if not ok:
        return None
    pt = er.representative_point()
    u, v = float(pt.x), float(pt.y)
    c, s = math.cos(th), math.sin(th)
    corners = []
    for cx, cy in ((0.0, 0.0), (w, 0.0), (w, d), (0.0, d)):
        x, y = u + cx, v + cy
        corners.append((x * c - y * s, x * s + y * c))      # 轉回原框
    from shapely.geometry import Point as _Pt
    # 🔒 **逐角獨立驗證**（⛔ 非以侵蝕之非空當證明——那是同一次計算）
    inside = [bool(poly.covers(_Pt(p))) for p in corners]
    return dict(theta=th, corners=corners, inside=inside, all_in=all(inside))


def scan(poly, w, d, steps=STEPS, R=None):
    """掃描 `[0, π)`（週期 π·`W ≠ D` ⇒ ⛔ 不可減半）。

    🔒 **兩個判定各用各的量（⛔ 不混）**：
      · **判「進」** ＝ `fits_at(…, r=0)` 之**精確**侵蝕非空（⛔ 非 `m ≥ 0`
        ——`m` 係二分之數值結果，於**邊界情形**〔宗地恰為 `W×D`〕會落在 `−1e−8`
        而使「閉區域」之裁判失準；`W-G.9-49` 首版自檢 ③ 即由此紅）。
      · **判「不進」** ＝ Lipschitz 證書（用 `m` 之**上界**）。

    🔒 **由粗到細（⛔ 非為省時而放寬）**：證書之門檻為 `R·Δθ/2`，而實測 `ε` 多達
      `O(0.1〜1) m` ⇒ **粗網格即足以證明**。逐宗取**第一個使證書成立之 Δθ**並印出。
      ⇒ 只有「`ε` 很小」之宗才需細網格 ⇒ **⛔ 不因步長而漏解**：
      任一 Δθ 之掃描皆先做「判進」之精確測試。

    回 `(命中 θ 或 None, 採用之 Δθ, max_m_ub, 掃描點數, 證書成立?)`。
    """
    for dth in steps:
        n = int(math.ceil(math.pi / dth))
        best_m = -1e18
        for k in range(n):
            th = k * dth
            if fits_at(poly, w, d, th, 0.0)[0]:      # ← 判「進」：精確
                return th, dth, None, k + 1, None
            m = margin_ub(poly, w, d, th)
            if m > best_m:
                best_m = m
        eps = -best_m
        if R is not None and eps > R * dth / 2.0:
            return None, dth, best_m, n, True
    return None, steps[-1], best_m, n, False


def selfcheck(P, w, d, R):
    """【B-4】判別力自檢——兩方向各一 ＋ 邊界二例（⛔ 必附）。"""
    from shapely.geometry import Polygon as _Pg
    P("【B-4】判別力自檢（⛔ 兩方向各一 ＋ 邊界·附實際輸出）")
    P("-" * WID)
    rows, ok = [], []

    def case(tag, ring, want_axis, want_free, note):
        p = _Pg(ring)
        ax = rect_fits(p, w, d)[0]
        th, dth, mmax, npt, cert = scan(p, w, d, R=R)
        fr = (th is not None)
        good = (ax == want_axis) and (fr == want_free)
        ok.append(good)
        rows.append((tag, ax, fr, th, mmax, want_axis, want_free, good, note, dth, cert))

    # ① 軸對齊**不進** ∧ 旋轉後**進**（＝ 本裁之所以必要）
    #    構造：把 W×D 盒整個旋轉 0.30 rad 當宗地 ⇒ 軸對齊之外接必大於盒
    ang = 0.30
    c, s = math.cos(ang), math.sin(ang)
    tilted = [(x * c - y * s, x * s + y * c)
              for x, y in ((0, 0), (w, 0), (w, d), (0, d))]
    case("①斜置之 W×D", tilted, False, True,
         f"宗地 ＝ W×D 盒繞原點轉 {ang} rad ⇒ 軸對齊不進、θ={ang} 進")
    # ② 任何角度皆**不進**（凸·⛔ 非凹形·考古 85 修法 1）
    #    構造：等腰三角形，面積 > W×D 而**最大內接矩形**小於 W×D
    case("②凸三角·恆不進", [(0, 0), (3.0 * w, 0), (0, 0.9 * d)], False, False,
         "面積 > W×D 而任何姿態皆塞不下 ⇒ 須證書成立")
    # ③ 邊界：宗地恰為 W×D
    case("③恰為 W×D", [(0, 0), (w, 0), (w, d), (0, d)], True, True,
         "閉區域 ⇒ 進（θ=0 即見證）")
    # ④ 邊界之反面：寬少 1e-6
    case("④略小於 W×D", [(0, 0), (w - 1e-6, 0), (w - 1e-6, d), (0, d)], False, False,
         "寬少 1e-6 ⇒ 任何姿態皆不進（⇒ ③ 之「進」非恆真）")

    P(f"  {'項':<16}{'軸對齊':>7}{'自由姿態':>9}{'見證θ':>11}{'max m上界':>12}"
      f"{'期軸':>6}{'期自由':>7}  判　說明")
    for tag, ax, fr, th, mm, wa, wf, good, note, dth, cert in rows:
        P(f"  {tag:<16}{('進' if ax else '不進'):>7}{('進' if fr else '不進'):>9}"
          f"{(f'{th:.4f}' if th is not None else '—'):>11}"
          f"{(f'{mm:.6f}' if mm is not None else '—'):>12}"
          f"{('進' if wa else '不進'):>6}{('進' if wf else '不進'):>7}"
          f"  {'✅' if good else '🔴'}　{note}")
    P("  🔒 **雙向已坐實**：① 軸對齊**不進**而自由姿態**進**（⇒ 本裁確有效力）；")
    P("     ② 面積足而**任何姿態皆不進**（⇒ 自由姿態**非恆真**）。")
    P("  🔒 ③④ 為邊界對：③ 恰等大 ⇒ 進（閉區域）；④ 少 `1e-6` ⇒ 不進 ⇒ ③ 非恆真。")
    P("  ⚠️ ⛔ **未以凹形自檢**——本案宗地皆凸（`-47` 已逐宗現查）"
      "⇒ 以凹形自檢不具本案之輸入形狀（考古 85 修法 1）。")
    return all(ok), rows


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-49】自由姿態之矩形容納（`K-9-12` ＋ KL 2026-08-17 自陳更正）")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔴 姿態**無約束**：可旋轉、可平移、⛔ 不須貼齊 FRONTLINE")
    P("")

    ns, fake_st = harvest()
    eps_touch = float(ns["_EPS_TOUCH_FRONT"])
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d, _s, _o, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        SB, snapshot=snapshot)
    BLKS = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in BLKS:
            BLKS.append(_l)
    g_rows, ERR = [], {}
    for lbl in BLKS:
        try:
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                             [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                             winners, forced, SB)
            g_rows.extend(_sg["g_rows"])
        except Exception as e:                                       # noqa: BLE001
            ERR[lbl] = f"{type(e).__name__}: {str(e).splitlines()[0][:130]}"
    rows = [r for r in g_rows if str(r.get("推進側別")) in ("left", "right")]

    # ── `W`／`D`（⛔ 無字面量）────────────────────────────────────────────
    WD = {}
    P("【B-5】`W`／`D` 之來源（⛔ 逐街廓·⛔ 無字面量）")
    P("-" * WID)
    for lbl in sorted({str(r.get("所屬街廓")) for r in rows}):
        cat = cb_by[lbl]["category"]
        rw = float(snapshot["blocks"][lbl]["正面"]["路寬_m"])
        mw = ns["get_min_lot_size"](cat, rw)
        WD[lbl] = (float(mw["min_width"]), float(mw["min_depth"]), mw)
        P(f"  {lbl}：分區 `{cat}`　路寬 {rw:.2f}　⇒ W ＝ {mw['min_width']}"
          f"　D ＝ {mw['min_depth']}　table_key ＝ `{mw['table_key']}`")
    w0, d0, _ = WD[sorted(WD)[0]]
    R = math.sqrt(w0 * w0 + d0 * d0) / 2.0
    P(f"  ⇒ **Lipschitz 常數 `R = √(W²+D²)/2` ＝ {R:.6f} m/rad**")
    P("")

    # ── 【B-3a】步長之自行驗證（⛔ 不逕採單之建議）──────────────────────
    P("【B-3a】掃描步長與證書門檻之**自行驗證**（⛔ 未逕採單之建議值）")
    P("-" * WID)
    # 🩸 **`W-G.9-53` §E-4 修**：本段首版印「採 Δθ = 1.0e-04」與同段標題
    #   「⛔ 未逕採單之建議值」**互相牴觸**，且與【B-6】門檻欄（`Δθ=2e-2` 之 7.215e-02）不符
    #   ⇒ **段陳舊**（判準已改為階梯而印出未同步·同族 `GB-71`）。改印**實際階梯**。
    P("  🔒 **實際採用者 ＝ 由粗到細之階梯**（⛔ 非單一步長）：")
    for _dd in STEPS:
        P(f"      Δθ ＝ {_dd:.1e} rad ⇒ 門檻 `R·Δθ/2` ＝ {R * _dd / 2:.6e} m"
          f"（{R * _dd / 2 * 1000:.4f} mm）·掃描點數 {int(math.ceil(math.pi / _dd))}")
    P("  ⇒ 逐宗取**第一個使證書成立之 Δθ**，並於【B-6】之「門檻」欄印該宗實際所用者。")
    P(f"  🔒 階梯之終點 ＝ {DTHETA:.1e}（＝ 單之建議值）⇒ **⛔ 未較單寬鬆**。")
    P(f"  🔒 **⛔ 不可減為 `[0, π/2)`**：`W ≠ D`（{w0} ≠ {d0}）⇒ 轉 π/2 後盒之長短邊互換、非同一問題。")
    P(f"  🔒 **`m(θ)` 之二分容差** `TOL_M` ＝ {TOL_M:.0e} m ≪ 門檻 ⇒ 不影響證書。")
    P("")

    okc, _sc = selfcheck(P, w0, d0, R)
    P(f"  ⇒ 自檢：{'PASS' if okc else '🛑 FAIL ⇒ 停機·本次量測⛔ 不出艙'}")
    if not okc:
        return L, sha
    P("")

    # ── 逐宗 ───────────────────────────────────────────────────────────
    P("=" * WID)
    P("【B-6】逐宗：自由姿態容納 ＋ 見證／證書 ＋ 對 `-47` 軸對齊之翻轉")
    P("=" * WID)
    P(f"  {'街廓':<5}{'暫編地號':<14}{'面積㎡':>9}{'|I_F|':>8}{'軸對齊':>7}{'自由':>7}"
      f"{'見證θ':>10}{'四角皆在內':>11}{'max m上界':>11}{'ε':>10}{'門檻':>11}{'證書':>6}{'翻轉':>6}")
    DAT, SMALL, C1 = [], [], []
    for r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        cc = r.get("cut_coords") or []
        if len(cc) < 3 or lbl not in WD:
            continue
        try:
            area = float(r.get("幾何面積(㎡)") or 0.0)
        except Exception:                                            # noqa: BLE001
            area = float("nan")
        w, d, _mw = WD[lbl]
        fl = fl_by.get(lbl) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        if not (p1 and p2):
            continue
        dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        Lf = math.hypot(dx, dy)
        dh = (dx / Lf, dy / Lf)
        if area < w * d:
            SMALL.append((lbl, gid, area, w * d))
            P(f"  {lbl:<5}{gid:<14}{area:>9.2f}   — **面積 < W×D ⇒ 算術上必不容納**（⛔ 未量形狀）")
            continue
        try:
            ring, t_lo, sg, dd, nn, fe = st_frame(cc, dh, p1, eps_touch)
        except Exception as e:                                       # noqa: BLE001
            P(f"  {lbl:<5}{gid:<14}{area:>9.2f}   🔴 框 raise：{str(e)[:60]}")
            continue
        pst = _poly_st(ring)
        fs = sorted({ring[i][0] for i in fe} | {ring[i + 1][0] for i in fe})
        iF = fs[-1] - fs[0]
        ax = rect_fits(pst, w, d)[0]
        th, dth, mmax, npt, cert_ = scan(pst, w, d, R=R)
        free = (th is not None)
        wit = witness(pst, w, d, th) if free else None
        eps = (-mmax) if (mmax is not None) else float("nan")
        thr = R * dth / 2.0
        cert = bool((not free) and cert_)
        code = ("進" if free else ("不進(證書成立)" if cert else "🛑 未找到"))
        DAT.append((lbl, gid, area, iF, ax, free, th, wit, mmax, eps, cert, w, d, dth, thr))
        if free and iF < w:
            C1.append((lbl, gid, area, iF, w))
        P(f"  {lbl:<5}{gid:<14}{area:>9.2f}{iF:>8.4f}{('進' if ax else '不進'):>7}"
          f"{code:>7}{(f'{th:.4f}' if th is not None else '—'):>10}"
          f"{('✅ 4/4' if (wit and wit['all_in']) else ('🔴' if wit else '—')):>11}"
          f"{(f'{mmax:.6f}' if mmax is not None else '—'):>11}"
          f"{(f'{eps:.6f}' if not free else '—'):>10}{thr:>11.3e}"
          f"{('✅' if cert else ('—' if free else '🔴')):>6}"
          f"{('🔴 是' if (ax != free) else '否'):>6}")

    # ── 統計 ───────────────────────────────────────────────────────────
    P("-" * WID)
    P(f"  面積 < W×D 先分流 ＝ **{len(SMALL)}** 宗；形狀測試母體 ＝ **{len(DAT)}** 宗")
    nfree = sum(1 for x in DAT if x[5])
    nax = sum(1 for x in DAT if x[4])
    nflip = [x for x in DAT if x[4] != x[5]]
    P(f"  軸對齊可容納 ＝ **{nax}** 宗；**自由姿態可容納 ＝ {nfree}** 宗")
    P(f"  🔴 **翻轉（軸對齊不進 → 自由姿態進）＝ {len(nflip)} 宗**")
    for x in nflip:
        P(f"      {x[0]}/{x[1]}　面積 {x[2]:.2f}　見證 θ ＝ {x[6]:.6f} rad"
          f"（{math.degrees(x[6]):.4f}°）")
    nbad = [x for x in DAT if (not x[5]) and (not x[10])]
    P(f"  判「不進」者 ＝ **{len(DAT) - nfree}** 宗；其中**證書成立** ＝ "
      f"**{len(DAT) - nfree - len(nbad)}** 宗")
    if nbad:
        P(f"  🛑 **證書不成立 ＝ {len(nbad)} 宗 ⇒ 出艙碼「未找到·⛔ 非證明不存在」**")
        for x in nbad:
            P(f"      {x[0]}/{x[1]}　max m 上界 ＝ {x[8]:.6f}　ε ＝ {x[9]:.6f}"
              f" ≤ 門檻 {x[14]:.3e}（Δθ ＝ {x[13]:.1e}）")
    else:
        P("      ✅ 全部成立 ⇒ 「不進」係**已證明**、⛔ 非「沒找到」")
    nw = [x for x in DAT if x[5] and x[7] and not x[7]["all_in"]]
    P(f"  見證矩形之**逐角獨立驗證**：{nfree - len(nw)}／{nfree} 宗四角全在宗內"
      f"{'　🔴 ' + str(len(nw)) + ' 宗未過' if nw else '　✅'}")

    # ── 見證矩形之四角座標（⛔ 具名·可覆核）────────────────────────────
    P("")
    P("【B-3b】見證矩形之四角座標（**原 (s,t) 框**·⛔ 逐角獨立驗證·前 6 宗示例＋全部翻轉宗）")
    P("-" * WID)
    _show = [x for x in DAT if x[4] != x[5]] + [x for x in DAT if x[5] and x[4] == x[5]][:6]
    for x in _show:
        wt = x[7]
        P(f"  {x[0]}/{x[1]}　θ ＝ {wt['theta']:.9f} rad")
        for i, (cpt, ins) in enumerate(zip(wt["corners"], wt["inside"])):
            P(f"      角{i + 1} ＝ ({cpt[0]:.9f}, {cpt[1]:.9f})　在宗內 ＝ {ins}")

    # ── §C-1 ──────────────────────────────────────────────────────────
    P("")
    P("【C-1】自由姿態判「進」 ∧ `|I_F| < W` 之宗（＝「不臨足夠路寬而仍判可建築」）")
    P("-" * WID)
    P(f"  查得 ＝ **{len(C1)}** 宗")
    for lbl, gid, a_, i_, w_ in C1:
        P(f"      🔴 {lbl}/{gid}　面積 {a_:.2f}　|I_F| ＝ {i_:.4f} < W ＝ {w_:.2f}")
    if not C1:
        n_i = sum(1 for x in DAT if x[3] < x[11])
        P(f"  🔒 **零計數之構造證（⛔ 不寫成「不可能」）**：二子句於本母體各自出現過否——")
        P(f"     (i) 自由姿態判「進」 ＝ **{nfree}** 宗；(ii) `|I_F| < W` ＝ **{n_i}** 宗")
        P(f"     ⇒ {'二者皆非空 ⇒ 其合取非結構恆假，本案無宗同時滿足' if (nfree and n_i) else '其一為空 ⇒ 合取於本母體結構上不可能'}")

    # ── §D-3 新對拍 ────────────────────────────────────────────────────
    P("")
    P("【D-3】兩側界**平行**之宗：閉式 vs 侵蝕掃描（⛔ 未假定全部平行·逐宗現查）")
    P("-" * WID)
    P(f"  {'街廓':<5}{'暫編地號':<14}{'兩側界平行?':>12}{'垂距':>10}{'帶長':>10}"
      f"{'閉式':>7}{'掃描':>7}{'一致?':>7}")
    npar, nagree = 0, 0
    for x in DAT:
        lbl, gid = x[0], x[1]
        r = next((rr for rr in rows if str(rr.get("所屬街廓")) == lbl
                  and str(rr.get("暫編地號")) == gid), None)
        if r is None:
            continue
        cc = r.get("cut_coords") or []
        fl = fl_by.get(lbl) or {}
        p1, p2 = fl["p1"], fl["p2"]
        dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        Lf = math.hypot(dx, dy)
        dh = (dx / Lf, dy / Lf)
        ring, t_lo, sg, dd, nn, fe = st_frame(cc, dh, p1, eps_touch)
        # 兩側界 ＝ 非前緣邊、非後緣邊之邊 ⇒ 以「與 t 軸夾角最小之二邊」取之
        edges = []
        for i in range(len(ring) - 1):
            a, b = ring[i], ring[i + 1]
            vx, vy = b[0] - a[0], b[1] - a[1]
            ln = math.hypot(vx, vy)
            if ln < 1e-9:
                continue
            edges.append((abs(vy) / ln, (vx / ln, vy / ln), a, b, ln))
        edges.sort(key=lambda e: -e[0])
        e1, e2 = edges[0], edges[1]
        cross = abs(e1[1][0] * e2[1][1] - e1[1][1] * e2[1][0])
        par = cross < 1e-6
        w, d = x[11], x[12]
        if par:
            npar += 1
            n_hat = (-e1[1][1], e1[1][0])
            dist = abs((e2[2][0] - e1[2][0]) * n_hat[0] + (e2[2][1] - e1[2][1]) * n_hat[1])
            band = max(e1[4], e2[4])
            closed = (dist >= w - 1e-12) and (band >= d - 1e-12)
            agree = (closed == x[5])
            nagree += agree
            P(f"  {lbl:<5}{gid:<14}{'✅ 平行':>12}{dist:>10.6f}{band:>10.4f}"
              f"{('進' if closed else '不進'):>7}{('進' if x[5] else '不進'):>7}"
              f"{('✅' if agree else '🔴'):>7}")
        else:
            P(f"  {lbl:<5}{gid:<14}{'不平行':>12}{'—':>10}{'—':>10}{'—':>7}"
              f"{('進' if x[5] else '不進'):>7}{'—':>7}")
    P(f"  ⇒ 兩側界平行之宗 ＝ **{npar}**／{len(DAT)}；閉式與掃描**一致 ＝ {nagree}**")
    for lbl in BLKS:
        if lbl in ERR:
            P(f"  ⛔ 街廓 {lbl}：`run_step_g` raise ⇒ **未量**")
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
    _log = os.path.join(OUTDIR, f"probe_WG949_free_pose_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
