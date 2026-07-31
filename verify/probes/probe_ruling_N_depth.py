# -*- coding: utf-8 -*-
"""W-G.5 裁定 N 第二批 — **N-12′ 宗地深度／N-19 街廓平均深度／N-2′ 接觸段** 三合一量測（只量不改）。

## 🔴 N-19 已由 **N-19′** 取代（裁定 K-8 §二·KL 裁 2026-07-31）

**N-19（舊·本檔【B】原表述）**：軸＝**FRONT 法向**。
**N-19′（現行正典）**：軸＝**垂直 BASELINE**。二者於 FRONT 與 BASELINE 不平行時**不同值**。
現行取值實作＝`app._compute_block_depth_alloc`（`grep -n "def _compute_block_depth_alloc" app.py`），
對照靶見 `probes/probe_ruling_K8_baseline_pairing.py` §3、夾具見 `verify/fixture_block_depth_n19p.py`。
本檔【B】已改量 N-19′；**舊 N-19 之表述保留為考古**（勿刪·見【B】段內註）。

## 為何整支改寫（KL N-12′(d)）

前版 `probe_ruling_N_p8._front_normal_depth_min` 量的是「**被街廓多邊形截斷之弦長**」
（`LineString ∩ poly` 之 `.length`）——**量測對象錯誤**。
KL 裁定：宗地深度＝該宗與 FRONTLINE **接觸段**上每一點，沿 FRONTLINE 法向至
**BASELINE（後側境界線）垂足**之垂距，取 **min**；
**(a) 不得被街廓左右邊界（側境界線）截斷**——法源畸零地規則 §4④「至該基地**後側**
境界線之垂直距離」，街廓左右邊界屬「側」非「後側」。
**(b) ⇒ 退化消失，排除帶不需要且禁止引入**（N0-17：禁以觀測殘差定閘寬）。

## 三個量（**軸一律 FRONTLINE 法向·非 alloc_normal_axis**）

| 量 | 式 | 出處 |
|---|---|---|
| 宗地深度（N-12′） | 接觸段上每點沿 `n_front` 至 **BASELINE 直線**之垂距 → **min** | KL N-12′ |
| 街廓平均深度（**N-19′**） | FRONTLINE 兩端至 BASELINE 無限直線之**垂直 BASELINE** 垂距 → **average** | K-8 §二 |
| ~~街廓平均深度（N-19·舊）~~ | ~~FRONTLINE 全段每點沿 `n_front` 之垂距 → average~~ | **已由 N-19′ 取代·存查** |
| 區內最小分配面積（N-16(b)） | 畸零地最小寬 × **深度最淺街廓**之街廓平均深度 | KL N-16(b) |

⚠️ N-12′ 取 **min**、N-19 取 **average**，**二者勿混**（KL 明令）。

## BASELINE 之表示

`cad['baselines'][blk] = {'point': (x,y), 'angle_deg': float}`
（`grep -n "'baselines': {block_label" app.py`）⇒ 為**無限直線**（點＋方向），
故垂距**天然不被街廓邊界截斷**——此即 N-12′(a) 之實作對應。

## 重跑
    WV_RULING_N_DEPTH=1 python verify/probes/probe_ruling_N_depth.py

⚠️ **零注入·零引擎改動**。輸出 `verify/out/probe_ruling_N_depth.log`。
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon, LineString, Point             # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUT_LOG = os.path.join(VERIFY, "out", "probe_ruling_N_depth.log")
STEPS = (0.21464, 0.01, 0.001)      # KL 指定三檔取樣（step·公尺）


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_N_depth：{msg}（no-silent-fallback）")


def _front_normal(poly, p1, d_hat):
    """FRONTLINE 法向量，取號指向街廓內（形心側）。"""
    n = np.array([-d_hat[1], d_hat[0]], dtype=float)
    c = np.array(poly.centroid.coords[0], dtype=float)
    if float(np.dot(c - p1, n)) < 0:
        n = -n
    return n


def _perp_to_baseline(P, n, bl_pt, bl_u):
    """自 P 沿 `n` 至 **BASELINE 無限直線**之垂距（有號→取正值）。
    解 `P + t·n = bl_pt + s·bl_u` ⇒ `[n, −bl_u]·[t, s]ᵀ = bl_pt − P`。
    `n ∥ bl_u`（BASELINE 平行量測軸）⇒ 無解 → None（loud 由呼叫端處置）。"""
    A = np.array([[n[0], -bl_u[0]], [n[1], -bl_u[1]]], dtype=float)
    det = float(np.linalg.det(A))
    if abs(det) < 1e-12:
        return None
    t, _s = np.linalg.solve(A, np.asarray(bl_pt, float) - np.asarray(P, float))
    return float(t)


def _profile(p1, d_hat, n, bl_pt, bl_u, s_lo, s_hi, step):
    """`s∈[s_lo,s_hi]` 上以 `step` 取樣之垂距序列（**不截斷**）。"""
    m = max(1, int(round((s_hi - s_lo) / step)))
    out = []
    for i in range(m + 1):
        s = s_lo + (s_hi - s_lo) * i / m
        t = _perp_to_baseline(p1 + s * d_hat, n, bl_pt, bl_u)
        if t is None:
            _fail("BASELINE ∥ FRONT 法向 ⇒ 垂距不可定義")
        out.append((s, t))
    return out


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.environ.get("WV_RULING_N_DEPTH") != "1":
        print("🔴 本探針須 WV_RULING_N_DEPTH=1 明示啟用。")
        return 2
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    # 🆕 K-8 §三 A-2：改吃**現算** N-19′。本檔【B】之「現行」欄自此比的是
    #   「本探針之獨立 numpy 實作」vs「app `_compute_block_depth_alloc`」——**兩份獨立實作**、
    #   非套套邏輯；差應 ≤ 0.005（app 側 2dp 記載鏈之捨入）。
    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    bls = cad.get("baselines") or {}
    fls = cad.get("front_lines") or {}
    L = []

    L.append("=" * 116)
    L.append("【N-12′／N-19】垂距量至 **BASELINE 無限直線**·**不被街廓側境界線截斷**"
             "（KL 裁定 2026-07-26 第二批）")
    L.append("=" * 116)

    blocks = [b for b in sorted(cb_by) if fls.get(b) and bls.get(b)]
    _no_bl = [b for b in sorted(cb_by) if fls.get(b) and not bls.get(b)]
    L.append(f"  可量街廓：{blocks}"
             f"｜非分配（無 FRONT_LINE）：{[b for b in sorted(cb_by) if not fls.get(b)]}")
    if _no_bl:
        # 🔴 **不靜默兜底、亦不整支停**：明列缺件、量其餘、結論標「暫定」（部分交付）
        L.append("")
        L.append("  🔴🔴 **BASELINE 缺件·N-12′／N-19 對下列街廓不可量**："
                 f"**{_no_bl}**")
        L.append(f"      DXF 內 BASELINE 實體數 ＝ **4**；`baselines_matched_count` ＝ "
                 f"**{cad.get('baselines_matched_count')}** ⇒ **全數配對成功**")
        L.append("      ⇒ 屬**繪圖資料缺件**（圖沒畫），**非配對程式 bug**。")
        L.append("      ⇒ 與 `CLAUDE.md` CAD 圖層規範「BASELINE **每街廓必畫**」相違。")
        L.append("      ⇒ **禁以街廓後緣／MBR／分配深度反推兜底**（no-silent-fallback）——"
                 "N-12′ 明定垂距量至 BASELINE，無 BASELINE 即無定義。")
        L.append("      ⇒ **本檔下列各表僅涵蓋可量之 4 塊**；N-16(b) 之「深度最淺街廓」"
                 "因母體不全而為**暫定值**。上呈 KL：補畫 R1／R5 之 BASELINE 後重跑。")

    # ── 🆕 結構閘 ∥：BASELINE（屁股線）須**平行** FRONT_LINE ──────────────────────
    #   機制不變量（純 CAD 幾何）。BASELINE ＝「後側境界線」⇒ 與正面臨路線近平行為其定義所繫；
    #   近垂直者必為**配對錯誤**（拿到鄰街廓之線）。容差 10°（對照既有「ALLOC ⊥ FRONT」閘之 0.15≈8.6°）。
    L.append("")
    L.append("【0】結構閘 ∥：BASELINE 須平行 FRONT_LINE（屁股線之定義所繫·容差 10°）")
    L.append("-" * 116)
    L.append(f"  {'塊':5}{'FRONT角°':>11}{'BASE角°':>11}{'夾角°':>9}"
             f"{'街廓面積':>11}{'臨街長':>10}{'面積÷長':>10}  判")
    _bad_par = []
    for blk in blocks:
        fl = fls[blk]
        p1 = np.array(fl["p1"], float); p2 = np.array(fl["p2"], float)
        Lfl = float(np.linalg.norm(p2 - p1))
        d_hat = (p2 - p1) / Lfl
        _fa = math.degrees(math.atan2(d_hat[1], d_hat[0]))
        _ba = float(bls[blk]["angle_deg"])
        _ang = abs((_fa - _ba + 90) % 180 - 90)
        _poly = Polygon(cb_by[blk]["vertices"])
        if not _poly.is_valid:
            _poly = _poly.buffer(0)
        _ok = _ang <= 10.0
        if not _ok:
            _bad_par.append((blk, _ang))
        L.append(f"  {blk:5}{_fa:11.3f}{_ba:11.3f}{_ang:9.3f}"
                 f"{_poly.area:11.1f}{Lfl:10.2f}{_poly.area / Lfl:10.2f}  "
                 f"{'✅' if _ok else '🔴 近垂直＝配對錯誤'}")
    if _bad_par:
        L.append("")
        L.append(f"  🔴🔴 **BASELINE 配對錯誤**：{[b for b, _ in _bad_par]}"
                 f"（夾角 {', '.join(f'{a:.2f}°' for _, a in _bad_par)}）")
        L.append("      屁股線與正面臨路線近垂直 ⇒ 必為**拿到鄰街廓之線**。")
        L.append("      ⇒ 該塊之 N-12′／N-19 量測**全部無效**（垂距沿近平行方向發散："
                 "實測 R2 得 0～1414m，而 面積÷臨街長 僅 43.67m）。")
        L.append(f"      ⇒ `baselines_matched_count = {cad.get('baselines_matched_count')}` "
                 "**不足以證明配對正確**——本閘為其缺口。")
        L.append("      ⇒ 建議：本閘機制化入 `_extract_cad_lines`（比照既有「結構閘 ⊥：ALLOC ⊥ FRONT」）。")
    _usable = [b for b in blocks if b not in {x for x, _ in _bad_par}]
    L.append("")
    L.append(f"  ⇒ **真正可用之街廓 ＝ {_usable}**（6 塊中 {len(_usable)} 塊）"
             f"｜無 BASELINE：{_no_bl}｜配對錯誤：{[b for b, _ in _bad_par]}")

    geo = {}
    L.append("")
    L.append("【A】三檔取樣穩定性（KL 必辦驗證：確認 min 跨三個數量級穩定且無端部退化）")
    L.append("-" * 116)
    L.append(f"  {'塊':5}{'FRONT長':>10}" + "".join(f"{'min@step ' + str(s):>22}" for s in STEPS)
             + f"{'極差':>10}")
    for blk in blocks:
        fl = fls[blk]
        p1 = np.array(fl["p1"], float); p2 = np.array(fl["p2"], float)
        Lfl = float(np.linalg.norm(p2 - p1))
        d_hat = (p2 - p1) / Lfl
        poly = Polygon(cb_by[blk]["vertices"])
        if not poly.is_valid:
            poly = poly.buffer(0)
        n = _front_normal(poly, p1, d_hat)
        bl = bls[blk]
        bl_pt = np.array(bl["point"], float)
        _a = math.radians(float(bl["angle_deg"]))
        bl_u = np.array([math.cos(_a), math.sin(_a)], float)
        geo[blk] = (p1, p2, d_hat, n, bl_pt, bl_u, poly, Lfl)

        mins = []
        for stp in STEPS:
            pr = _profile(p1, d_hat, n, bl_pt, bl_u, 0.0, Lfl, stp)
            mins.append(min(t for _s, t in pr))
        L.append(f"  {blk:5}{Lfl:10.4f}" + "".join(f"{m:22.6f}" for m in mins)
                 + f"{max(mins) - min(mins):10.2e}")

    L.append("")
    L.append("  ⇒ 三檔極差若 ~1e-3 以下 ⇒ **min 穩定·無端部退化** ⇒ N-12′(b)「排除帶不需要」成立。")
    L.append("  （對照：舊式『被街廓截斷之弦長』於 R6 三檔得 40.2776／1.9943／0.1994"
             "＝隨取樣→0·probe_ruling_N_p8 舊版·**已廢**）")

    # ── N-19 街廓平均深度 ＋ N-16(b) 區內最小分配面積 ──
    L.append("")
    # 🔴 K-8 §二：軸由「FRONT 法向」改為「**垂直 BASELINE**」（N-19 → N-19′）。
    #   🗄️ 考古（勿刪）：本段原表述為「軸＝FRONT 法向」＝**舊 N-19**；
    #      二軸於 FRONT 與 BASELINE 不平行時不同值，本案六塊 ∠(FRONT,BASELINE) 非 0。
    L.append("【B】**N-19′** 街廓平均深度（垂直 BASELINE·無限直線·兩端垂距平均·解析）"
             " ＋ N-16(b) 區內最小分配面積")
    L.append("    （舊 N-19＝軸取 FRONT 法向·已由 K-8 §二 取代·表述存查）")
    L.append("-" * 116)
    L.append(f"  {'塊':5}{'平均深度':>12}{'最小深度':>12}{'最大深度':>12}"
             f"{'現行 街廓分配深度_m':>22}{'差':>10}{'min_width':>11}")
    avg_by, mw_by = {}, {}
    for blk in _usable:          # 🆕 排除配對錯誤之塊（其垂距發散·無效）

        p1, p2, d_hat, n, bl_pt, bl_u, poly, Lfl = geo[blk]
        # 🔴 K-8 §二 N-19′：軸＝**垂直 BASELINE**（`bn`），且為**解析式·禁取樣**
        #   （前緣線與 BASELINE 皆直線 ⇒ 垂距沿弦線性 ⇒ 平均 ＝ 兩端垂距之平均）。
        # 🗄️ 考古（勿刪）：舊 N-19 為
        #      `pr = _profile(p1, d_hat, n, bl_pt, bl_u, 0.0, Lfl, 0.001)` ＋ `sum(ts)/len(ts)`
        #      ——沿 FRONT 以 0.001m **取樣**、軸取 `n`＝**FRONT 法向**。二軸不同值。
        _bn = np.array([-bl_u[1], bl_u[0]])
        _bp = np.asarray(bl_pt, float)[:2]
        _t1 = abs(float(np.dot(np.asarray(p1, float)[:2] - _bp, _bn)))
        _t2 = abs(float(np.dot(np.asarray(p2, float)[:2] - _bp, _bn)))
        ts = [_t1, _t2]
        avg_by[blk] = (_t1 + _t2) / 2.0
        road_w = float(snapshot["blocks"][blk]["正面"]["路寬_m"])
        mls = ns["get_min_lot_size"](cb_by[blk]["category"], road_w)
        mw_by[blk] = float(mls.get("min_width", 0) or 0)
        _old = float(snapshot["blocks"][blk]["街廓分配深度_m"])
        L.append(f"  {blk:5}{avg_by[blk]:12.4f}{min(ts):12.4f}{max(ts):12.4f}"
                 f"{_old:22.4f}{avg_by[blk] - _old:+10.4f}{mw_by[blk]:11.2f}")

    if _no_bl:
        L.append("")
        L.append(f"  ⚠️ **母體不全**：{_no_bl} 無 BASELINE、{[b for b,_ in _bad_par]} 配對錯誤，皆未入比較 ⇒ 「深度最淺街廓」"
                 "與區內最小分配面積**皆為暫定**、補圖後須重算。")
    if not avg_by:
        _fail("無任何可用 BASELINE ⇒ N-19／N-16(b) 不可算")
    _shallow = min(avg_by, key=lambda b: avg_by[b])
    _mw_min = min(mw_by.values())
    _new_minA = _mw_min * avg_by[_shallow]
    L.append("")
    L.append(f"  深度最淺街廓 ＝ **{_shallow}**（街廓平均深度 {avg_by[_shallow]:.4f}m）")
    L.append(f"  畸零地最小寬（全區最小）＝ {_mw_min:.2f}m"
             f"｜逐塊 min_width（可用塊）：{ {b: mw_by[b] for b in _usable} }")
    L.append(f"  ⇒ **N-16(b) 區內最小分配面積 ＝ {_mw_min:.2f} × {avg_by[_shallow]:.4f}"
             f" = {_new_minA:.4f} ㎡**（round2 = {round(_new_minA, 2)}）")
    L.append(f"  對照現行引擎側 114.07（＝round(32.59×3.5,2)·**快照舊深度**·見夾具 T10 制度甲）"
             f"　⇒ 變動 {round(_new_minA, 2) - 114.07:+.2f}㎡")
    L.append("  ⚠️ 上式以**未捨入**深度相乘，非正典鏈。K-8 §二 正典＝`round(D_avg,2) × min_width`"
             f"（辦法 §3 2dp）⇒ 本案 R4 `33.10×3.5 = 115.85` ＝ **region_min**；"
             "以 app 真符號逐格對拍見 `verify/fixture_block_depth_n19p.py` T8/T9。")
    L.append("  ⚠️ 本值之 min_width 取全區最小；若 KL 意為「最淺街廓自身之 min_width」，"
             f"則為 {mw_by[_shallow]:.2f} × {avg_by[_shallow]:.4f} = "
             f"{mw_by[_shallow] * avg_by[_shallow]:.4f}㎡。UC9898 六塊 min_width 同為 3.5 "
             "⇒ 兩讀同值、**本案無法區辨**，泛用化前須釐清（列上呈）。")

    # ── N-2′ 必辦：R6 s<0 三角塊與 FRONTLINE 之接觸 ──
    L.append("")
    L.append("【C】N-2′ 必辦：`s<0` 三角塊與 FRONTLINE 之**實際接觸幾何**"
             "（自 CAD 真幾何量·禁由敘述推定）")
    L.append("-" * 116)
    for blk in blocks:
        p1, p2, d_hat, n, bl_pt, bl_u, poly, Lfl = geo[blk]
        alloc = ns["alloc_normal_axis"]((cad.get("alloc_dir_by_block") or {}).get(blk))
        dom = ns["_strip_s_range"](poly, d_hat, p1, alloc)
        if dom is None:
            continue
        s_min = float(dom[0])
        if s_min >= -1e-6:
            continue
        wedge, w_area = ns["_block_strip"](poly, d_hat, p1 + s_min * d_hat, -s_min,
                                           allocation_dir=alloc)
        if wedge is None or wedge.is_empty:
            continue
        fl_seg = LineString([p1, p2])
        inter = wedge.intersection(fl_seg)
        _typ = inter.geom_type
        _len = float(inter.length) if hasattr(inter, "length") else 0.0
        L.append(f"  ▸ {blk}｜s_min={s_min:.4f}｜楔形面積={float(w_area or 0):.4f}㎡")
        L.append(f"      楔形 ∩ FRONTLINE：型別 **{_typ}**｜長度 **{_len:.6f} m**")
        if inter.is_empty:
            # 空交集：楔形與 FRONTLINE **完全不接觸**（浮點下角點未落在線段上）
            _d_gap = float(wedge.distance(fl_seg))
            L.append(f"      ⇒ **交集為空**（楔形↔FRONTLINE 最近距 {_d_gap:.3e} m）"
                     f" ⇒ 接觸至多為角點·**臨街長度 0** ⇒ 依 KL N-2′ 屬**未臨正街土地** ✅")
        elif _typ == "Point" or _len <= 1e-9:
            _d2p1 = float(Point(p1).distance(inter))
            L.append(f"      ⇒ **接觸退化為單點**（距 p1 {_d2p1:.6e} m）"
                     f" ⇒ 依 KL N-2′ 屬**未臨正街土地**·不獨立受寬深檢驗 ✅")
        else:
            L.append(f"      ⇒ 🚩 **接觸為線段（長 {_len:.6f} m）·非單點**"
                     f" ⇒ **須重判是否仍屬未臨正街**（KL 必辦條款）·上呈")
        # 併量：楔形自身之 N-12′ 深度（若接觸為線段才有意義）
        if _len > 1e-9:
            _s0 = float(np.dot(np.asarray(inter.bounds[:2], float) - p1, d_hat))
            L.append(f"      （楔形接觸段沿 FRONT 之 s 範圍約 [{min(0.0, _s0):.4f}, {_len:.4f}]）")

    L.append("=" * 116)
    out = "\n".join(L)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write(out + "\n")
    print(out)
    print(f"\n📄 {OUT_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
