# -*- coding: utf-8 -*-
r"""K-9-6-b **宗地層量測帶** — 舊帶 vs 新帶 對照·**只算不換**（K-6-A2 段五(a)+(b)）。

## 兩個帶

| | 帶之上緣 `t_hi` | 來源 |
|---|---|---|
| **舊（生產中）** | `min_depth` ＝ 畸零地**附表**值（本案 `14.00`） | `get_min_lot_size(...)['min_depth']` ⇒ **GB-13** 所登記之誤 |
| **新（opt-in）** | **該宗二個後緣角點中較淺者之 `t`** | `grep -n "def _n14_band_geom" app.py` |

🔴 **帶底定義已於 (c)-1 更正**（KL 圖示裁定 2026-08-05）：段五(a) 之
`t_hi = t_lo + D·(b̂n·n̂)` **已作廢**——`K-9-6-a` 表列第 1 列之受詞與法規原文相反
（原文受詞＝**後側境界線**）。⛔ 新式**無平移、無投影係數**。
教訓：**失敗考古 節 42**；(c)-1 前之實料凍存於
`verify/out/probe_K9_6_parcel_band_段五a凍存.log`（⛔ 勿與本檔輸出混用）。

⛔ **量測方向不變**（K-9-6-b-2 逐字）：仍為「帶內**平行前緣線**之弦長取 min」。
⛔ **量測對象亦不變**（KL 2026-08-05 裁）：仍為**宗地多邊形之弦**。

## ⛔ 單一真相源

新帶之算式**只有一份**——`app._n14_band_hi`；本檔**逐字呼叫之**，
⛔ **未在本檔另寫第二份**（**GB-8** 之形狀：多份實作、無一致性看守）。

## 🔴 母體之界定（前一手在此出錯）

母體 ＝ `run_step_g` 之 `g_rows` 中 **`推進側別 ∈ {'left','right'}`** 者。
⛔ **不得以「有無 `cut_coords`」為篩**——抵費地**有真幾何**，卻於
`grep -n "if _side in ('抵費地'" app.py` **直接跳出、根本不量寬度**
⇒ 以幾何為篩會把它算進母體、稀釋分母。
🔒 本檔**逐字印出被剔除各列之 `推進側別` 分布**（⛔ 禁過濾診斷）。

## 街角宗

**本批不進量測**——街角宗於 `evaluate_parcel_width_n14` 因 **K-4 面積門檻豁免**
提前 return（`grep -n "WIDTH_VERDICT_CORNER_K4" app.py`）⇒ log 記 **`N/A·豁免中`**，
⛔ **不臆造數字**。（其量測路徑屬 **GB-39**／K-9-5·**段六**。）

## ⛔ 本檔不設任何門檻

放行門檻由 KL 於 (c) 前裁定。帶深自 `14.00` 改為 `33〜46`，
**任何以舊帶深估出之門檻皆不適用**（失敗考古 節 41 之形狀）。
⇒ 本檔 **rc 恆 0**、**不接 `run_all`**。

## 重跑

    python verify/probes/probe_K9_6_parcel_band.py

輸出 `verify/out/probe_K9_6_parcel_band.log`。
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_6_parcel_band.log")
# 🔒 (c)-1 前之實料（**凍存**）——§六-4 之對照靶。⛔ 本檔只讀不寫。
LOG_SEG5A = os.path.join(OUTDIR, "probe_K9_6_parcel_band_段五a凍存.log")

SIDES_IN = ("left", "right")


def _ring_ts_oracle(cut_coords, d_hat, front_pt):
    """**獨立復現**之環上 `t` 值（§六-2／§六-3 之 oracle）。

    ⚠️ **本函式係「獨立復現」、非單一真相源之複製**——其存在之目的，
    正是要**與 `app._n14_band_geom` 之產物比對**；二者一致與否即受檢項本身。
    ⛔ 故 **不得**改為呼叫 `_n14_band_geom` 取值（那會使 §六-2／3 成為恆真）。
    """
    import numpy as _np
    from shapely.geometry import Polygon as _Poly
    _d = _np.asarray(d_hat, dtype=float)[:2]
    _d = _d / float(_np.linalg.norm(_d))
    _n = _np.array([-_d[1], _d[0]], dtype=float)
    _fp = _np.asarray(front_pt, dtype=float)[:2]
    _P = _np.asarray([[float(p[0]), float(p[1])] for p in cut_coords],
                     dtype=float) - _fp
    _poly = _Poly(list(zip((_P @ _d).tolist(), (_P @ _n).tolist())))
    if not _poly.is_valid:
        _poly = _poly.buffer(0)
    _ring = [(float(p[0]), float(p[1])) for p in list(_poly.exterior.coords)]
    if float(_poly.centroid.coords[0][1]) < 0:
        _ring = [(_s, -_t) for _s, _t in _ring]
    return [_t for _s, _t in _ring]


def _parse_seg5a_raises(path):
    """自**凍存**之 (c)-1 前 log 取各 raise 列之 `深度 t=…`（§六-4 之對照靶）。

    回 `{(情境, 街廓/gid): t_舊}`。⛔ 只認可解析為浮點者
    （【D】段之說明行含「深度 t=…處」之全形刪節號 ⇒ 自然被排除）。
    """
    _out = {}
    if not os.path.exists(path):
        return _out
    _pat = re.compile(r"^\s+(\S+)\s+(\S+)（t_hi_新[^）]*）：.*?深度 t=([0-9]+\.[0-9]+)m")
    with open(path, encoding="utf-8") as _f:
        for _ln in _f:
            _m = _pat.match(_ln)
            if _m:
                _out[(_m.group(1), _m.group(2))] = float(_m.group(3))
    return _out


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 170)
    L.append("【K-9-6-b 宗地層量測帶】舊帶（附表 min_depth）vs 新帶（BASELINE 法向之該宗最小深度）"
             " — **只算不換·生產零呼叫點**（K-6-A2 段五(a)+(b)）")
    L.append("新帶 t_hi ＝ t_lo + D·(b̂n·n̂)｜⛔ 量測方向不變（仍取平行前緣線之弦）"
             "｜⛔ 本檔不設任何門檻")
    L.append("=" * 170)

    ns, fake_st = harvest()
    for _s in ("parcel_min_width_n14", "_n14_band_hi", "_n14_band_geom",
               "get_min_lot_size", "_baseline_pts_from_manual"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    _EPS = float(ns["_EPS_TOUCH_FRONT"])
    _seg5a = _parse_seg5a_raises(LOG_SEG5A)
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    bl_by = cad.get("baselines", {}) or {}

    rows = []
    excluded = {}
    for setback in (0.0, 3.5):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, winners, forced, setback)
        for r in sg["g_rows"]:
            _side = str(r.get("推進側別") or "（空）")
            if _side not in SIDES_IN:
                excluded.setdefault((f"{setback:g}m", _side), 0)
                excluded[(f"{setback:g}m", _side)] += 1
                continue
            rows.append((setback, r))

    # ── 【A】母體界定之診斷（⛔ 禁過濾）────────────────────────────────────────
    L.append("")
    L.append("【A】母體界定：`推進側別 ∈ {'left','right'}`（⛔ **非**以有無 `cut_coords` 為篩）")
    L.append("-" * 170)
    L.append(f"  納入母體：**{len(rows)}** 列（兩情境合計）")
    L.append("  被剔除各列之 `推進側別` 分布（逐字·⛔ 未過濾）：")
    if excluded:
        for (tag, sd), n in sorted(excluded.items()):
            L.append(f"    {tag:<6} 推進側別＝`{sd}`：{n} 列")
    else:
        L.append("    （無剔除列）")
    L.append("  ⚠️ **抵費地有真幾何但不量寬度**（`grep -n \"if _side in ('抵費地'\" app.py`）"
             "⇒ 以幾何為篩會稀釋分母。")

    # ── 【B】逐宗全精度 ────────────────────────────────────────────────────────
    L.append("")
    L.append("【B】逐宗：舊帶 vs 新帶（**全精度**·另附 2dp 生產值）")
    L.append("-" * 170)
    L.append(f"{'情境':<6}{'街廓':<5}{'gid':<13}{'側':<6}"
             f"{'t_lo':>12}{'t_hi_舊':>10}{'D':>12}{'g':>13}{'(b̂n·n̂)':>17}"
             f"{'後緣t1':>12}{'後緣t2':>12}{'n後緣':>6}"
             f"{'t_hi_新':>12}{'寬度_舊':>13}{'寬度_新':>13}{'Δ寬度':>13}"
             f"{'舊判定':>8}{'新判定':>8}  翻轉")
    L.append("-" * 190)
    _flip, _err, _corner, _idmax = [], [], 0, 0.0
    _acc = []          # §六 之逐宗驗收料：(tag, lbl, gid, t_hi, rear, tv_oracle)
    _agg = []          # 【H】聚合之逐宗料（⛔ 攤表之 min/max 一律出自此）
    for setback, r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
        tag = f"{setback:g}m"
        fl = fl_by.get(lbl) or {}
        cc = r.get("cut_coords") or []
        if str(r.get("街角地", "")).strip() == "是":
            _corner += 1
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                     f"{'— N/A·豁免中（K-4 面積門檻·街角宗不進量測·GB-39／段六）':<}")
            continue
        if not (fl.get("p1") and fl.get("p2")) or len(cc) < 3:
            _err.append((tag, lbl, gid, None, "缺 FRONT_LINE 或 cut_coords < 3"))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 缺件（見【D】）")
            continue
        _mw = ns["get_min_lot_size"](
            cb_by[lbl]["category"],
            float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        _md = float(_mw.get("min_depth", 0.0) or 0.0)
        _lw = float(_mw.get("min_width", 0.0) or 0.0)
        p1, p2 = fl["p1"], fl["p2"]
        _dx, _dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        _Lf = math.hypot(_dx, _dy)
        _dh = (_dx / _Lf, _dy / _Lf)
        _bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), cb_by[lbl].get("vertices"))
        # 🔒 **helper 先算**——即使 `parcel_min_width_n14` 其後 raise，
        #   `t_hi_新` 仍須留下，否則【D】無從自證「帶之上緣是否已越過該宗」。
        try:
            _t_lo, _t_hi_new, _D, _g, _bdn = ns["_n14_band_hi"](
                cc, _dh, p1, _bp, _label=f"{lbl}/{gid}")
            # 🔒 後緣角點之全體（供【B】欄與§六-2 稽核）——**同一真相源**
            _rear = ns["_n14_band_geom"](
                cc, _dh, p1, _bp, _label=f"{lbl}/{gid}")[1]
        except RuntimeError as e:
            _err.append((tag, lbl, gid, None, str(e).splitlines()[0][:150]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 helper raise（見【D】）")
            continue
        _idmax = max(_idmax, abs(_bdn - math.sqrt(max(0.0, 1.0 - _g * _g))))
        _acc.append((tag, lbl, gid, _t_hi_new, _rear,
                     _ring_ts_oracle(cc, _dh, p1)))
        _r1 = _rear[0][0]
        _r2 = _rear[1][0] if len(_rear) > 1 else float('nan')
        try:
            _w_old = float(ns["parcel_min_width_n14"](
                cc, _dh, p1, _md, _label=f"{lbl}/{gid}"))
            _w_new = float(ns["parcel_min_width_n14"](
                cc, _dh, p1, _md, _label=f"{lbl}/{gid}", baseline_pts=_bp))
        except RuntimeError as e:
            _err.append((tag, lbl, gid, _t_hi_new, str(e).splitlines()[0][:150]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                     f"{_t_lo:>12.6f}{_md:>10.2f}{_D:>12.6f}{_g:>13.6f}"
                     f"{_bdn:>17.12f}{_r1:>12.6f}{_r2:>12.6f}{len(_rear):>6}"
                     f"{_t_hi_new:>12.6f}"
                     f"   🔴 寬度 raise（見【D】）")
            continue
        _agg.append(dict(tag=tag, blk=lbl, gid=gid, thi=_t_hi_new, D=_D, g=_g,
                         bdn=_bdn, r1=_r1, r2=_r2, nre=len(_rear),
                         wo=_w_old, wn=_w_new, dw=_w_new - _w_old))
        _vo = "合格" if _w_old >= _lw else "不合格"
        _vn = "合格" if _w_new >= _lw else "不合格"
        _fl = (_vo != _vn)
        if _fl:
            _flip.append((tag, lbl, gid, side, _w_old, _w_new, _lw, _vo, _vn))
        L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                 f"{_t_lo:>12.6f}{_md:>10.2f}{_D:>12.6f}{_g:>13.6f}{_bdn:>17.12f}"
                 f"{_r1:>12.6f}{_r2:>12.6f}{len(_rear):>6}"
                 f"{_t_hi_new:>12.6f}{_w_old:>13.6f}{_w_new:>13.6f}"
                 f"{_w_new - _w_old:>13.6f}{_vo:>8}{_vn:>8}  {'🔴 翻轉' if _fl else '—'}")
    L.append("-" * 190)
    L.append(f"  2dp 生產值（`round(w, 2)`）另見上表之全精度欄；"
             f"街角宗 **{_corner}** 列記 `N/A·豁免中`（⛔ 未臆造數字）")

    # ── 【C】翻轉之宗（⛔ 不得只給計數）──────────────────────────────────────
    L.append("")
    L.append("【C】判定翻轉之宗（**逐宗列出**·⛔ 不只給計數）")
    L.append("-" * 170)
    if _flip:
        for tag, lbl, gid, side, wo, wn, lw, vo, vn in _flip:
            L.append(f"  {tag:<6}{lbl}/{gid}（{side}）："
                     f"寬度 {wo:.6f} → {wn:.6f}（門檻 {lw:.2f}）｜{vo} → {vn}")
    else:
        L.append("  （無）")
    L.append(f"  ⇒ 翻轉之宗：{len(_flip)} ／ 量得之宗 "
             f"{len(rows) - _corner - len(_err)}")

    # ── 【D】raise／缺件之列 ───────────────────────────────────────────────────
    L.append("")
    L.append(f"【D】raise／缺件之列：{len(_err)}")
    L.append("  🔴 **每列另附 `t_hi_新`**——與 raise 訊息內之「深度 t=…處之弦長為 0」對讀，")
    L.append("     即可自證『**新帶之下緣已抵／越過該宗之最深頂點**』（見攤表 §三之機制說明）。")
    for tag, lbl, gid, thi, why in _err:
        L.append(f"  {tag:<6}{lbl}/{gid}"
                 f"（t_hi_新 ＝ {'—' if thi is None else f'{thi:.6f}'}）：{why}")
    if not _err:
        L.append("  （無）")

    # ── 【E】恆等式自檢 ───────────────────────────────────────────────────────
    L.append("")
    L.append("【E】恆等式自檢 `(b̂n·n̂) ＝ sqrt(1 − g²)`（**逐宗值已印於【B】之 `(b̂n·n̂)` 欄**）")
    L.append(f"  逐宗 |(b̂n·n̂) − sqrt(1−g²)| 之**最大值** ＝ {_idmax:.3e}"
             f"（閘 `1e-12`·由 `_n14_band_hi` 內部逐宗 raise 把關）")
    L.append("  🔒 該閘為**獨立恆等式**（`{d̂,n̂}` 單範正交 ＋ `|b̂n|=1` ⇒ `g²+h²=1`），"
             "⛔ 非把同一算式抄兩遍。")

    # ── 【G】(c)-1 §六 驗收（**逐宗印出**·⛔ 不得只印「全過」）────────────────────
    L.append("")
    L.append("【G】(c)-1 §六 驗收（**可否證預言**·逐宗列示）")
    L.append("-" * 190)
    L.append("  🔒 §六-2／§六-3 之 `t_v` 係**獨立復現**（`_ring_ts_oracle`），"
             "⛔ 非自 `_n14_band_geom` 取值 ⇒ 二者一致與否即受檢項本身。")
    L.append(f"{'情境':<6}{'街廓':<5}{'gid':<13}"
             f"{'t_hi_新':>12}{'最近頂點t':>12}{'|差|':>11}{'該點|dep|':>11}"
             f"{'max(t_v)':>12}{'§六-2':>8}{'§六-3':>8}"
             f"{'舊raise之t':>13}{'§六-4':>8}")
    L.append("-" * 190)
    _g2 = _g3 = _g4 = 0
    _g2b, _g3b, _g4b = [], [], []
    _g4n = 0
    for tag, lbl, gid, _th, _rear, _tv_o in _acc:
        _near = min(_tv_o, key=lambda _t: abs(_t - _th))
        _dv = abs(_near - _th)
        _dep0 = abs(_rear[0][1])
        _tmax = max(_tv_o)
        _ok2 = (_dv < 1e-12) and (_dep0 <= _EPS)
        _ok3 = (_th <= _tmax)
        _told = _seg5a.get((tag, f"{lbl}/{gid}"))
        if _told is None:
            _ok4, _s4, _s_told = None, "—", f"{'—':>13}"
        else:
            _g4n += 1
            _ok4 = (_th <= _told)
            _s4 = "✅" if _ok4 else "🔴"
            _s_told = f"{_told:>13.6f}"
        _g2 += int(_ok2); _g3 += int(_ok3); _g4 += int(bool(_ok4))
        if not _ok2:
            _g2b.append((tag, lbl, gid, _dv, _dep0))
        if not _ok3:
            _g3b.append((tag, lbl, gid, _th, _tmax))
        if _ok4 is False:
            _g4b.append((tag, lbl, gid, _th, _told))
        L.append(f"{tag:<6}{lbl:<5}{gid:<13}"
                 f"{_th:>12.6f}{_near:>12.6f}{_dv:>11.3e}{_dep0:>11.3e}"
                 f"{_tmax:>12.6f}{'✅' if _ok2 else '🔴':>8}{'✅' if _ok3 else '🔴':>8}"
                 f"{_s_told}{_s4:>8}")
    L.append("-" * 190)
    L.append(f"  §六-2 帶底落在宗地頂點上（|差| < 1e-12 ∧ |dep| ≤ {_EPS}）："
             f"{_g2}／{len(_acc)}" + ("　🔴 破：" + str(_g2b) if _g2b else "　✅ 全成立"))
    L.append(f"  §六-3 帶底不越過最深頂點（t_hi ≤ max(t_v)）："
             f"{_g3}／{len(_acc)}" + ("　🔴 破：" + str(_g3b) if _g3b else "　✅ 全成立"))
    L.append(f"  §六-4 對凍存 log 之 raise 列（新 t_hi ≤ 舊 raise 之 t）："
             f"{_g4}／{_g4n}"
             + ("　🔴 破：" + str(_g4b) if _g4b else "　✅ 全成立")
             + f"（靶檔 `{os.path.basename(LOG_SEG5A)}`·"
             f"其 raise 列共 {len(_seg5a)} 筆）")

    # ── 【H】聚合（⛔ 皆為觀測·非門檻）────────────────────────────────────────
    #   🔒 攤表所引之 min/max 一律出自本段，⛔ 不得由讀者自行離線聚合後宣稱。
    L.append("")
    L.append("【H】聚合（⛔ 皆為觀測·非門檻·逐宗值見【B】）")
    L.append("-" * 190)
    if _agg:
        _thi = [_r['thi'] for _r in _agg]
        _Dv = [_r['D'] for _r in _agg]
        _dw = [_r['dw'] for _r in _agg]
        _nz = [_r for _r in _agg if _r['dw'] != 0.0]
        _rel = max((_r['D'] - _r['thi']) / _r['thi'] for _r in _agg)
        _gap = max(abs(_r['r1'] - _r['r2']) for _r in _agg if _r['nre'] >= 2)
        _mx = max(_agg, key=lambda _r: abs(_r['dw']))
        L.append(f"  帶底 `t_hi` 範圍　　　＝ {min(_thi):.6f} 〜 {max(_thi):.6f} m"
                 f"（附表 14.00 之 {min(_thi) / 14.0:.3f}× 〜 {max(_thi) / 14.0:.3f}×）")
        L.append(f"  報表量 `D` 範圍　　　＝ {min(_Dv):.6f} 〜 {max(_Dv):.6f} m")
        L.append(f"  `|g|` 最大　　　　　　＝ {max(abs(_r['g']) for _r in _agg):.6f}"
                 f"｜`(b̂n·n̂)` 最小 ＝ {min(_r['bdn'] for _r in _agg):.9f}")
        L.append(f"  `D` vs `t_hi` 相對差最大 ＝ {_rel * 100:.6f}%"
                 f"　（法規原文『垂直距離』之兩讀法·⛔ 不作裁定請求·見攤表註腳）")
        L.append(f"  後緣角點數 `n後緣` 之分布 ＝ "
                 f"{sorted(set(_r['nre'] for _r in _agg))}"
                 f"｜二後緣角點 `|t1−t2|` 最大 ＝ {_gap:.6f} m")
        L.append(f"  `max|Δ寬度|` ＝ {abs(_mx['dw']):.6f} m"
                 f"（{_mx['tag']} {_mx['blk']}/{_mx['gid']}）"
                 f"｜`Δ寬度 ≠ 0` 之列 ＝ {len(_nz)}／{len(_agg)}"
                 f"｜`|Δ寬度| > 法定粒度 0.01m` 之列 ＝ "
                 f"{sum(1 for _r in _agg if abs(_r['dw']) > 0.01)}")
        for _r in _nz:
            L.append(f"      Δ≠0：{_r['tag']:<6}{_r['blk']}/{_r['gid']}"
                     f"　舊 {_r['wo']:.6f} → 新 {_r['wn']:.6f}（Δ {_r['dw']:+.3e}）")
    else:
        L.append("  （無量得之宗）")

    L.append("")
    L.append("【F】註記")
    L.append("  · **只算不換**：`parcel_min_width_n14` 之生產呼叫點**未傳** `baseline_pts`")
    L.append("    （`grep -n -A2 \"^    _w = parcel_min_width_n14\" app.py` 之三行內無之）。")
    L.append("  · 新帶之算式**只有一份**（`app._n14_band_hi`）；本檔逐字呼叫，⛔ 未另寫第二份。")
    L.append("  · ⛔ **本檔不設任何門檻、不接 `run_all`**——放行門檻由 KL 於 (c) 前裁定。")
    L.append("  · 街角宗之量測路徑屬 **GB-39**／K-9-5（**段六**），本批 `N/A·豁免中`。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
