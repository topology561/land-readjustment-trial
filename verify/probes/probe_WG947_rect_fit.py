#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-47】`K-9-12` 矩形容納測試（⛔ 零生產碼·⛔ 不實作於生產）

**受詞**：`K-9-12`（KL 裁 2026-08-17）——宗地之**四至範圍**內能否**完整容納**
邊長 `W × D` 之矩形 ⇒ 能 ⇒ **非畸零地·可建築**。

🔴 **⛔ 不得硬編 `3.5`／`14`**（KL 逐字提醒：「若不同路寬級距或不同使用分區則就不是 3.5*14」）
⇒ `W`／`D` **一律由 `get_min_lot_size(分區, 正面路寬)` 取得並逐宗印出**（含 `table_key`）。

🔴 **⛔ 矩形不旋轉**（KL 逐字）：`W` 沿 **FRONTLINE 方向**、`D` 沿 **FRONTLINE 法向**
⇒ 即倉內現有 `st_frame` 之 `(s, t)` 框（`K-9-10 四` 之量測軸）⇒ **⛔ 不另立座標框**。

**解法（⛔ 其正確性繫於凸性·逐宗現查）**：
  矩形之四角相對其左下角之位移 ＝ `{(0,0), (W,0), (0,D), (W,D)}`。
  「角 `c` 落在宗內」⟺「左下角落在 `P − c`」⇒
  **可容納 ⟺ `∩_{c} (P − c) ≠ ∅`**（＝ `P` 對該矩形之 Minkowski 侵蝕非空）。
  🔒 **「四角皆在宗內 ⇒ 整個矩形在宗內」僅於 `P` <u>凸</u>時成立**
  （矩形 ＝ 其四角之凸包；凸集含其中任意點之凸包）。
  🔴 **非凸 ⇒ ⛔ 不得用本解法**（同 `K-9-10 五` 之禁令理由：兩點法倚賴凸性）
  ⇒ 本檔逐宗現查凸性並具名；遇非凸者**⛔ 不出該宗之數**。

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
# 🔒 **單一真相源**：(s,t) 框取自 `W-G.9-42` 已過 `C-1` 驗收閘之實作，⛔ 不另寫第二份（`GB-8`）。
from probe_WG941_bandbase import st_frame                           # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 176
SB = 0.0
# 🔒 **本檔明訂之容差（⛔ 非正典數字）**：侵蝕結果之面積 > `EPS_AREA` 方判「可容納」。
#   單位 ＝ ㎡（(s,t) 框為等距正交框 ⇒ 面積與世界座標同單位）。
#   🔴 **若有任一宗之分類繫於此值 ⇒ 停·具名上呈**（見【C-1b】之敏感度欄）。
EPS_AREA = 1e-9
EPS_CVX = 1e-9      # 凸性判定：|P| 與其凸包面積之差


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _poly_st(ring):
    from shapely.geometry import Polygon as _Pg
    p = _Pg(ring)
    if not p.is_valid:
        p = p.buffer(0)
    return p


def rect_fits(poly_st, w, d, t0=None):
    """回 `(可容納?, 侵蝕面積, 侵蝕之 t 範圍)`。

    `t0 is None` ⇒ **自由平移**（`s₀`、`t₀` 皆不受限·KL 未限制 ⇒ 本檔之預設）。
    `t0` 給值 ⇒ **限定矩形底邊落在該深度**（＝「須貼齊 FRONTLINE」之另一讀法）。
    """
    from shapely.affinity import translate as _tr
    from shapely.geometry import LineString as _LS
    cur = None
    for cx, cy in ((0.0, 0.0), (w, 0.0), (0.0, d), (w, d)):
        t = _tr(poly_st, xoff=-cx, yoff=-cy)
        cur = t if cur is None else cur.intersection(t)
        if cur.is_empty:
            return False, 0.0, None
    # 🩸 **開閉之更正（`W-G.9-47` 自檢紅所迫·⛔ 具名·⛔ 非放寬）**：
    #   首版以 `面積 > EPS_AREA` 判「可容納」，而本檔之**敘述**同時寫著「採**閉區域**」
    #   ⇒ **碼與敘述互相牴觸**（自檢 ③「恰為 `W×D`」期望「進」而實得「不進」坐實之）。
    #   🔒 **正解為閉區域**：宗地恰為 `W × D` 時，該矩形**確實被完整容納**
    #     （閉集含其自身）⇒ 侵蝕退化為**單點**（面積 0）**仍屬容納**。
    #   ⇒ 判準改為 **`not cur.is_empty`**，⛔ 非面積門檻。
    #   ⚠️ 面積仍逐宗印出，並於【C-1b】檢查**有無任一宗之分類繫於此退化情形**。
    if t0 is not None:
        cur = cur.intersection(_LS([(-1e6, t0), (1e6, t0)]))
        return (not cur.is_empty), float(getattr(cur, "length", 0.0)), (t0, t0)
    a = float(cur.area)
    ys = [c[1] for c in (cur.exterior.coords if cur.geom_type == "Polygon"
                         else list(cur.coords) if cur.geom_type == "LineString"
                         else [(cur.x, cur.y)] if cur.geom_type == "Point" else [])]
    return (not cur.is_empty), a, ((min(ys), max(ys)) if ys else None)


def selfcheck(P):
    """【C-4】判別力自檢——**兩方向各一** ＋ 邊界情形（⛔ 必附）。"""
    from shapely.geometry import Polygon as _Pg
    P("【C-4】判別力自檢（⛔ 兩方向各一·附實際輸出）")
    P("-" * W)
    w, d = 3.0, 10.0            # ⛔ 本自檢之合成參數（⛔ 非本案之 W/D·⛔ 非附表值）
    rows, ok = [], []

    def _minw_band(poly, t_lo, t_hi):
        """現行寬度判準之簡化重現（帶內 `w(t)` 之 min）——**僅供自檢對照**。"""
        ring = list(poly.exterior.coords)
        ts = {t_lo, t_hi} | {t for _s, t in ring if t_lo <= t <= t_hi}
        best = None
        for t in sorted(ts):
            xs = []
            for i in range(len(ring) - 1):
                s0, y0 = ring[i]
                s1, y1 = ring[i + 1]
                if y0 == y1:
                    if y0 == t:
                        xs += [s0, s1]
                    continue
                if (y0 - t) * (y1 - t) <= 0.0:
                    u = (t - y0) / (y1 - y0)
                    xs.append(s0 + u * (s1 - s0))
            if xs:
                wv = max(xs) - min(xs)
                best = wv if best is None else min(best, wv)
        return best

    def case(tag, ring, want_rect, want_width, note):
        p = _Pg(ring)
        fit, a, _ = rect_fits(p, w, d)
        mw = _minw_band(p, 0.0, max(t for _s, t in ring))
        wpass = (mw is not None and mw >= w - 1e-12)
        good = (fit == want_rect) and (wpass == want_width)
        ok.append(good)
        rows.append((tag, fit, wpass, a, mw, want_rect, want_width, good, note))

    # ① 寬足而深不足 ⇒ 矩形**不過** ∧ 現行寬度判準**過**
    case("①寬足深不足", [(0, 0), (20, 0), (20, 6), (0, 6)], False, True,
         "20×6：寬 20 ≥ 3 ⇒ 寬過；深 6 < 10 ⇒ 矩形不進")
    # ② 前窄後寬（凸·梯形）⇒ 矩形**過** ∧ 現行寬度判準**不過**
    #    🔒 **⛔ 未用非凸形狀**：本案宗地皆凸（E-8a），以凹形自檢不具本案輸入形狀
    #    （考古 85 修法 1）；改以**凸梯形**達成同一二分。
    case("②前窄後寬", [(0, 0), (1.5, 0), (12, 14), (0, 14)], True, False,
         "前緣寬 1.5 < 3 ⇒ 寬不過；深處足寬足深 ⇒ 矩形進")
    # ③ 邊界情形：恰為 W × D 之矩形本身
    case("③恰為 W×D", [(0, 0), (w, 0), (w, d), (0, d)], True, True,
         "恰好等大 ⇒ 侵蝕退化為單點（面積 0）⇒ **本檔採閉區域** ⇒ 判可容納")
    # ④ 邊界之反面：略小於 W×D（寬少 1e-6）⇒ 須**不**可容納（證 ③ 非恆真）
    # 🩸 **本項之期望首版寫錯（⛔ 具名·期望之錯·非碼之錯）**：原寫 `want_width=True`，
    #   而該宗之寬 ＝ `w − 1e-6` **確實小於** `w` ⇒ 現行寬度判準**本就不過**。
    #   ⇒ 期望改為 `False`。🔒 本項之受詞仍成立：它證 **③ 之「進」非恆真**。
    case("④略小於 W×D", [(0, 0), (w - 1e-6, 0), (w - 1e-6, d), (0, d)], False, False,
         "寬少 1e-6 ⇒ 矩形不進、現行寬亦不過（⇒ ③ 之「進」非恆真）")

    P(f"  {'項':<14}{'矩形':>6}{'現行寬':>7}{'侵蝕面積':>13}{'帶內min寬':>11}"
      f"{'期矩形':>7}{'期寬':>6}  判　說明")
    for tag, fit, wp, a, mw, wr, ww, good, note in rows:
        P(f"  {tag:<14}{('進' if fit else '不進'):>6}{('過' if wp else '不過'):>7}"
          f"{a:>13.6f}{(mw if mw is not None else float('nan')):>11.4f}"
          f"{('進' if wr else '不進'):>7}{('過' if ww else '不過'):>6}"
          f"  {'✅' if good else '🔴'}　{note}")
    P("  🔒 **雙向不等價已坐實**：① 現行寬度判準**過**而矩形**不進**；"
      "② 現行寬度判準**不過**而矩形**進** ⇒ 二判準**互不蘊含**。")
    P("  🔒 **邊界之開閉（⛔ 本檔明訂·非正典·⛔ 已與碼同步）**：判準 ＝ **侵蝕結果非空**"
      "（`not is_empty`），⛔ **非面積門檻**。")
    P("     ③ 恰為 `W×D` ⇒ 侵蝕退化為**單點**（面積 0）而**非空** ⇒ 判**可容納**（閉區域）；")
    P("     ④ 寬少 `1e-6` ⇒ 侵蝕**空** ⇒ 判**不可容納** ⇒ ③ 之「進」**非恆真**。")
    P("     🩸 **首版碼用 `面積 > 1e-9` 而敘述寫「閉區域」⇒ 碼與敘述互相牴觸**，"
      "由自檢 ③ 抓出並已改碼（⛔ 非改敘述遷就碼）。")
    P("  ⚠️ **⛔ 未以非凸形狀自檢**——本案宗地皆凸（見【C-0】逐宗現查），"
      "以合成凹形自檢不具本案之輸入形狀（考古 85 修法 1）⇒ 改以**凸梯形**達成同一二分。")
    return all(ok)


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * W)
    P("【W-G.9-47】`K-9-12` 矩形容納測試（⛔ 零生產碼）")
    P("=" * W)
    P(f"  產生於 commit：{sha}")
    P("  🔴 ⛔ 不旋轉（KL 裁）：W 沿 FRONTLINE 方向、D 沿其法向 ＝ `st_frame` 之 (s,t) 框")
    P("  🔴 ⛔ W／D 一律由 `get_min_lot_size` 取得（⛔ 無字面量 3.5／14）")
    P("")
    if not selfcheck(P):
        P("")
        P("🛑 判別力自檢紅 ⇒ 停機·本次量測⛔ 不出艙。")
        return L, sha
    P("  ⇒ 自檢：PASS")
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

    # ── §Q2／C-5：W/D 之來源與騎樓分支 ──────────────────────────────────────
    P("=" * W)
    P("【C-0】`W`／`D` 之來源（⛔ 逐街廓印出·⛔ 無字面量）")
    P("=" * W)
    WD = {}
    for lbl in sorted({str(r.get("所屬街廓")) for r in rows}):
        cat = cb_by[lbl]["category"]
        rw = float(snapshot["blocks"][lbl]["正面"]["路寬_m"])
        mw = ns["get_min_lot_size"](cat, rw)
        WD[lbl] = (float(mw["min_width"]), float(mw["min_depth"]), mw)
        P(f"  {lbl}：分區 `{cat}`　正面路寬 {rw:.2f} m"
          f"　⇒ W ＝ {mw['min_width']}　D ＝ {mw['min_depth']}"
          f"　min_area ＝ {mw['min_area']}　table_key ＝ `{mw['table_key']}`")
    P("")
    P("【C-5】「應留設騎樓」之資料源現查（`K-9-12` 之 W／D 繫於此）")
    P("-" * W)
    _keys = set()
    for _b in snapshot.get("blocks", {}).values():
        _keys |= set(_b.keys())
        for _v in _b.values():
            if isinstance(_v, dict):
                _keys |= set(_v.keys())
    _hit = sorted(k for k in _keys if ("騎樓" in str(k)) or ("arcade" in str(k).lower()))
    P(f"  快照 `blocks` 之欄位全集（{len(_keys)} 個）中含「騎樓／arcade」者 ＝ **{len(_hit)}**"
      f"{('：' + '／'.join(_hit)) if _hit else ''}")
    P(f"  `HUALIEN_MIN_LOT_TABLE` 之鍵：{sorted(ns['HUALIEN_MIN_LOT_TABLE'].keys())}")
    P("  🛑 ⇒ **資料源不存在** ⇒ 本案各街廓**是否應留設騎樓 ＝ 「無從判定」**")
    P("     ⛔ **不假設為無**（`W-G.9-47` §C-5 明令）。⇒ 上開 `W`／`D` 係**第一款（一般建築基地）**之值；")
    P("     若任一街廓實應留設騎樓，其 `W` 應為 **7.10**（短少 3.60 m）⇒ 見 `GB-73`。")
    P("")

    # ── 逐宗 ────────────────────────────────────────────────────────────────
    P("=" * W)
    P("【C-1】矩形容納測試 ＋【C-2】面積先分流 ＋【C-3】新舊判準對照")
    P("=" * W)
    P(f"  {'街廓':<5}{'側':<6}{'暫編地號':<14}{'面積㎡':>10}{'W':>6}{'D':>7}{'W×D':>8}"
      f"{'凸?':>5}{'矩形':>6}{'侵蝕面積':>12}{'t₀=t_lo':>8}{'t₀=0':>6}"
      f"{'現行寬':>10}{'現行判':>8}{'分歧':>6}")
    A_SMALL, DAT, NONCVX, TOL_SENS, READ_SENS = [], [], [], [], []
    for r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
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
        bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl),
                                             (cb_by.get(lbl) or {}).get("vertices"))
        # ── C-2：面積 < W×D ⇒ 算術上必不容納 ⇒ 先分流、⛔ 不併入形狀測試之計數 ──
        if area < w * d:
            A_SMALL.append((lbl, gid, area, w * d))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{area:>10.2f}{w:>6.2f}{d:>7.2f}{w*d:>8.2f}"
              f"   — **面積 < W×D ⇒ 算術上必不容納**（⛔ 未量形狀·⛔ 不併入計數）")
            continue
        try:
            ring, t_lo, sg, dd, nn, fe = st_frame(cc, dh, p1, eps_touch)
        except Exception as e:                                       # noqa: BLE001
            P(f"  {lbl:<5}{side:<6}{gid:<14}{area:>10.2f}   🔴 框 raise：{str(e)[:60]}")
            continue
        pst = _poly_st(ring)
        cvx = abs(pst.area - pst.convex_hull.area) <= EPS_CVX
        if not cvx:
            NONCVX.append((lbl, gid, area, abs(pst.area - pst.convex_hull.area)))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{area:>10.2f}{w:>6.2f}{d:>7.2f}{w*d:>8.2f}"
              f"{'🔴否':>5}   — **非凸 ⇒ ⛔ 不用簡化解法·⛔ 不出本宗之數**")
            continue
        fit, ar_er, trng = rect_fits(pst, w, d)
        # 🩸 **變體之定義首版寫錯（⛔ 具名·⛔ 非量測器之錯）**：首版只試 `t₀ = 0.0`
        #   （＝ FRONTLINE 本身），實得 **26/26 全判「不進」**。
        #   🔴 **成因**：宗地之前緣邊落在 `t ≈ t_lo`（`_n14_band_geom` 容許其偏離
        #   `_EPS_TOUCH_FRONT` ＝ 0.01 m）⇒ `t = 0` 之線**根本不在宗內**
        #   ⇒ 該變體量的是「宗地有沒有恰好碰到 `t=0`」，**⛔ 不是**「矩形須不須貼齊前緣」。
        #   ⇒ **補 `t₀ = t_lo`**（＝ 該宗**自己的前緣**）作為「貼齊前緣」之正解；
        #     `t₀ = 0` 仍保留並列，供讀者看見二者之別。
        fit0, _len0, _ = rect_fits(pst, w, d, t0=0.0)
        fitL, _lenL, _ = rect_fits(pst, w, d, t0=t_lo)
        # 現行寬度判準
        try:
            wprod = float(ns["parcel_min_width_n14"](cc, dh, p1, float(_mw["min_depth"]),
                                                     _label=f"{lbl}/{gid}", baseline_pts=bp))
            wpass = (wprod >= w - 1e-9)
            wtxt, jtxt = f"{wprod:.4f}", ("合格" if wpass else "不合格")
        except Exception as e:                                       # noqa: BLE001
            wprod, wpass = None, None
            wtxt, jtxt = "raise", str(e).splitlines()[0][:18]
        div = "" if wpass is None else ("🔴 是" if (fit != wpass) else "否")
        if fit != fitL:
            READ_SENS.append((lbl, gid, area, fit, fitL, fit0, t_lo))
        if fit and ar_er <= 1e-6:
            TOL_SENS.append((lbl, gid, area, ar_er))
        DAT.append((lbl, gid, side, area, w, d, fit, fitL, ar_er, wprod, wpass, fit0, t_lo))
        P(f"  {lbl:<5}{side:<6}{gid:<14}{area:>10.2f}{w:>6.2f}{d:>7.2f}{w*d:>8.2f}"
          f"{'凸':>5}{('進' if fit else '不進'):>6}{ar_er:>12.6f}"
          f"{('進' if fitL else '不進'):>8}{('進' if fit0 else '不進'):>6}"
          f"{wtxt:>10}{jtxt:>8}{div:>6}")

    # ── 統計與敏感度 ────────────────────────────────────────────────────────
    P("-" * W)
    P(f"  【C-2】面積 < W×D 而先分流者 ＝ **{len(A_SMALL)}** 宗"
      f"（⛔ 不併入形狀測試之計數）")
    for lbl, gid, a_, wd_ in A_SMALL:
        P(f"      {lbl}/{gid}　面積 {a_:.2f} < W×D {wd_:.2f}")
    P(f"  非凸而⛔ 未出數者 ＝ **{len(NONCVX)}** 宗")
    if not NONCVX:
        P("      🔒 **凸性之現查結論**：進入形狀測試之宗**全部為凸**"
          f"（判準 `|area − convex_hull.area| ≤ {EPS_CVX:.0e}`）")
        P("      ⇒ 「四角皆在宗內 ⇒ 整個矩形在宗內」成立（矩形 ＝ 其四角之凸包）")
        P("      ⇒ 侵蝕法之正確性**有據**（⛔ 非假設）。")
    P(f"  形狀測試之母體 ＝ **{len(DAT)}** 宗；其中矩形**可容納** ＝ "
      f"**{sum(1 for x in DAT if x[6])}** 宗")
    P("")
    P("  🔴 **【C-1b】敏感度（⛔ 兩項皆須為空，否則停·具名上呈）**")
    P(f"     · 分類繫於**容差** `EPS_AREA={EPS_AREA:.0e}` 者（侵蝕面積 ≤ 1e-6 而判可容納）"
      f" ＝ **{len(TOL_SENS)}** 宗")
    for x in TOL_SENS:
        P(f"         🛑 {x[0]}/{x[1]}　侵蝕面積 {x[3]:.3e}")
    if not TOL_SENS:
        P("         ✅ 無 ⇒ 本檔明訂之容差**未決定任何宗之分類**")
        P("         🔒 零計數之構造證：自檢 ③（恰為 `W×D`）之侵蝕面積 ＝ 0.000000"
          "（即該情形**可出現**）⇒ 本計數非結構恆 0。")
    P(f"     · 分類繫於**讀法**（自由平移 vs **貼齊該宗前緣** `t₀=t_lo`）者 ＝ "
      f"**{len(READ_SENS)}** 宗")
    for x in READ_SENS:
        P(f"         🛑 {x[0]}/{x[1]}　面積 {x[2]:.2f}　自由平移 ＝ {'進' if x[3] else '不進'}"
          f"／`t₀=t_lo` ＝ {'進' if x[4] else '不進'} ⇒ **讀法未定·無從判定**（⛔ 不自行選邊）")
    if not READ_SENS:
        P("         ✅ 無 ⇒ 二讀法於本母體**給出相同分類** ⇒ 該讀法之擇一於本案**無土地後果**")
    _n0 = sum(1 for x in DAT if not x[11])
    P(f"     · 🔴 **另記（⛔ 非上項）**：`t₀ = 0`（＝ FRONTLINE 本身）者 **{_n0}／{len(DAT)}** 宗判「不進」")
    P("       ——**⛔ 非「都不合格」**，係**該變體之受詞錯**：宗地前緣落在 `t ≈ t_lo > 0`")
    P("       （`_n14_band_geom` 容許其偏離 `_EPS_TOUCH_FRONT` ＝ 0.01 m）⇒ `t = 0` 之線不在宗內。")
    P(f"       本母體之 `t_lo` 範圍 ＝ [{min(x[12] for x in DAT):.6f}, {max(x[12] for x in DAT):.6f}]")
    P("       ⇒ 「貼齊前緣」之正解為 **`t₀ = t_lo`**（上項所用者）。")

    # ── C-3：新舊判準之分歧 ────────────────────────────────────────────────
    P("")
    P("【C-3】新舊判準之分歧")
    P("-" * W)
    dv = [x for x in DAT if x[10] is not None and x[6] != x[10]]
    P(f"  分歧宗數 ＝ **{len(dv)}**／{len([x for x in DAT if x[10] is not None])}")
    for lbl, gid, side, a_, w_, d_, fit, _fL, ar_, wp_, wpass, _f0, _tl in dv:
        P(f"      {lbl}/{gid}　面積 {a_:.2f}　矩形 {'進' if fit else '不進'}"
          f"　現行寬度 {wp_:.4f} ⇒ {'合格' if wpass else '不合格'}（門檻 {w_:.2f}）")
    r1 = [x for x in DAT if x[1] == "628-34(3)"]
    P("")
    P("  🔴 **R1 `628-34(3)` 之特別列示（`GB-65` 之土地後果）**")
    if r1:
        x = r1[0]
        P(f"      面積 {x[3]:.2f}　W×D ＝ {x[4]*x[5]:.2f}　矩形容納 ＝ **{'是' if x[6] else '否'}**")
        P("      🔒 **平行／不平行兩支之結果比較**：`K-9-12` 之判準**⛔ 不含**「垂線容納條件」，")
        P("         其輸入僅為【宗地四至範圍】＋【`W`／`D`】——**二者皆與 `K-9-6-h ④` 之平行判無關**")
        P("         ⇒ **兩支結果必然相同**（⛔ 非實測巧合，係**構造上**不依賴）。")
        P("      ⇒ 若 `K-9-12` 取代寬度判準成為可建築之唯一判定，")
        P("         **`GB-65` 於本案（就可建築判定而言）失去土地後果**。")
        P("      🔒 ⛔ **不逕撤 `GB-65`**——其射程尚及 `K-9-6-h ④` 之**深度**定式（見 `GB-65` 追加）。")
    else:
        P("      🛑 `628-34(3)` 不在形狀測試母體內（見上分流）⇒ 具名，⛔ 不臆測")
    P("")
    P("【C-6】遞補連鎖 ⇒ 🛑 **⛔ 未實跑**（須先有 `K-9-12` 之實作）")
    P(f"  **靜態預測（⛔ 標明為預測）**：以 `K-9-12` 為唯一判準時，"
      f"本母體之不可建築宗 ＝ **{len(A_SMALL) + sum(1 for x in DAT if not x[6])}** 宗"
      f"（面積分流 {len(A_SMALL)} ＋ 形狀不進 {sum(1 for x in DAT if not x[6])}）")
    P("  ⛔ **不預測輪數／最終不配地數**——遞補改變後續各宗之 G 值與四至範圍，須實跑重排。")
    for lbl in BLKS:
        if lbl in ERR:
            P(f"  ⛔ 街廓 {lbl}：`run_step_g` raise ⇒ **未量**（{ERR[lbl]}）")
    P("=" * W)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG947_rect_fit_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
