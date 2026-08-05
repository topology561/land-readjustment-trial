# -*- coding: utf-8 -*-
r"""K-9-6-b **宗地層量測帶** — 舊帶 vs 新帶 對照·**只算不換**（K-6-A2 段五(a)+(b)）。

## 兩個帶

| | 帶之上緣 `t_hi` | 來源 |
|---|---|---|
| **舊（生產中）** | `min_depth` ＝ 畸零地**附表**值（本案 `14.00`） | `get_min_lot_size(...)['min_depth']` ⇒ **GB-13** 所登記之誤 |
| **新（本批 opt-in）** | `t_lo + D·(b̂n·n̂)`，`D` ＝ 該宗自 **BASELINE 法向**量得之最小深度 | `grep -n "def _n14_band_hi" app.py` |

⛔ **量測方向不變**（K-9-6-b-2 逐字）：仍為「帶內**平行前緣線**之弦長取 min」。

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

SIDES_IN = ("left", "right")


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
    for _s in ("parcel_min_width_n14", "_n14_band_hi", "get_min_lot_size",
               "_baseline_pts_from_manual"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
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
             f"{'t_hi_新':>12}{'寬度_舊':>13}{'寬度_新':>13}{'Δ寬度':>13}"
             f"{'舊判定':>8}{'新判定':>8}  翻轉")
    L.append("-" * 170)
    _flip, _err, _corner, _idmax = [], [], 0, 0.0
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
        except RuntimeError as e:
            _err.append((tag, lbl, gid, None, str(e).splitlines()[0][:150]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}  🔴 helper raise（見【D】）")
            continue
        _idmax = max(_idmax, abs(_bdn - math.sqrt(max(0.0, 1.0 - _g * _g))))
        try:
            _w_old = float(ns["parcel_min_width_n14"](
                cc, _dh, p1, _md, _label=f"{lbl}/{gid}"))
            _w_new = float(ns["parcel_min_width_n14"](
                cc, _dh, p1, _md, _label=f"{lbl}/{gid}", baseline_pts=_bp))
        except RuntimeError as e:
            _err.append((tag, lbl, gid, _t_hi_new, str(e).splitlines()[0][:150]))
            L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                     f"{_t_lo:>12.6f}{_md:>10.2f}{_D:>12.6f}{_g:>13.6f}"
                     f"{_bdn:>17.12f}{_t_hi_new:>12.6f}"
                     f"   🔴 寬度 raise（見【D】）")
            continue
        _vo = "合格" if _w_old >= _lw else "不合格"
        _vn = "合格" if _w_new >= _lw else "不合格"
        _fl = (_vo != _vn)
        if _fl:
            _flip.append((tag, lbl, gid, side, _w_old, _w_new, _lw, _vo, _vn))
        L.append(f"{tag:<6}{lbl:<5}{gid:<13}{side:<6}"
                 f"{_t_lo:>12.6f}{_md:>10.2f}{_D:>12.6f}{_g:>13.6f}{_bdn:>17.12f}"
                 f"{_t_hi_new:>12.6f}{_w_old:>13.6f}{_w_new:>13.6f}"
                 f"{_w_new - _w_old:>13.6f}{_vo:>8}{_vn:>8}  {'🔴 翻轉' if _fl else '—'}")
    L.append("-" * 170)
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
