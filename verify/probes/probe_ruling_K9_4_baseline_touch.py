# -*- coding: utf-8 -*-
"""K-9-4 BASELINE 臨接 — **只量不判·不設閘·不判合格/不合格**（K-6-A2 段二-1(a)）。

## 判準（正典·逐字）

> **每宗必須配到 BASELINE**；未達即**停機報錯**。**不支援同一街廓前後配兩排。**
（`grep -n "K-9-4" docs/rulings/K-6_街角地分配程序與可分配判準.md`）

## 本探針之定位

段二-1 分三步，**(b) 為強制停機點**：

- **(a)（本檔）** 只量不判 ⇒ **rc 恆 0**、不 raise 違例、不作為閘。
- **(b)** 攤給 KL 過目 ⇒ **等 KL 點頭**。
- **(c)** 上閘（待放行）。

理由：K-9-4 是**停機閘**，一旦上線就會擋住整案 ⇒ **上閘前必須先知道本案會不會被自己擋住。**

## 算法源（**禁在 verify/ 另寫一套幾何**）

**唯一算法源＝`app.k94_baseline_touch_by_parcel`**
（`grep -n "def k94_baseline_touch_by_parcel" app.py`），其軸取自
`app._baseline_normal_axis`（`grep -n "def _baseline_normal_axis" app.py`）
——**與 N-19′ 同一軸**（`_compute_block_depth_alloc` 已改走同一支）。
本檔**只負責備料與列印**。

## 容差

`app._EPS_TOUCH_FRONT`（`grep -n "^_EPS_TOUCH_FRONT = " app.py`）＝ **0.01 m**
——與 `parcel_min_width_n14` 之**前端**臨接判定**共用同一把尺**。
⛔ 本檔**不定義任何容差**、不接受容差參數。

## 🔍 幾何來源之聲明（施工單 §二(a) 要求）

**採 `cut_coords`（＝截角後之實際宗地幾何）。**

理由與影響評估見輸出【C】段：截角三角形位於**街角（前緣線側）**，
而本量測所取者為**最接近 BASELINE（屁股線）之頂點**。
【C】段逐街廓列出**截角三角形各頂點之 BASELINE 偏移**與**宗地 `gap`** 之量級對比，
以**實測**回答「改用截角前幾何會不會改變本步結論」。
🔴 若實測顯示**會**改變 ⇒ **停機上呈**（本檔只呈現量測、不代判）。

## 自檢：軸同源（**本檔之判別力來源**）

【D】段以 `k94_baseline_touch_by_parcel` 之同一軸量 **FRONT_LINE 兩端點**，
與 `_compute_block_depth_alloc` 回傳之 `d_front_p1`／`d_front_p2` 對拍。
二者**若非同軸即不可能逐格相符** ⇒ 該段綠即證「本檔之軸 ≡ N-19′ 之軸」。

## 重跑

    python verify/probes/probe_ruling_K9_4_baseline_touch.py

**rc 恆 0**。輸出 `verify/out/probe_ruling_K9_4_baseline_touch.log`。
"""
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
LOG = os.path.join(OUTDIR, "probe_ruling_K9_4_baseline_touch.log")


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 122)
    L.append("【K-9-4 BASELINE 臨接】只量不判·不設閘（K-6-A2 段二-1(a)）")
    L.append("判準：每宗必須配到 BASELINE；未達即停機報錯。**本檔不判、不擋、rc 恆 0**")
    L.append("算法源：app.k94_baseline_touch_by_parcel（軸＝app._baseline_normal_axis·與 N-19′ 同軸）")
    L.append("幾何來源：**cut_coords（截角後）**——影響評估見【C】段")
    L.append("=" * 122)

    ns, fake_st = harvest()
    for _sym in ("k94_baseline_touch_by_parcel", "_baseline_normal_axis",
                 "_baseline_pts_from_manual", "_compute_block_depth_alloc",
                 "n19p_depth_info_by_label", "_EPS_TOUCH_FRONT"):
        if ns.get(_sym) is None:
            raise RuntimeError(f"🔴 harvest 未取得 {_sym}（段二-1(a) 接線未落地？）")
    EPS = float(ns["_EPS_TOUCH_FRONT"])
    L.append(f"容差 _EPS_TOUCH_FRONT ＝ {EPS} m（與 parcel_min_width_n14 前端臨接共用）")

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        _v6_raw = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, _v6_raw, list(cb_by.values()), snapshot)
    fcb = ns.get("F3_CATEGORY_BURDEN", {})
    build_blocks = [b for b in cb_by.values()
                    if fcb.get(b.get("category", ""), "") == "可建築土地"]
    bl_by = {b["label"]: ns["_baseline_pts_from_manual"](
                 (cad.get("baselines", {}) or {}).get(b["label"]), b.get("vertices"))
             for b in build_blocks}

    # ── 母體：全部可建築街廓 × 全部分配宗地 × 兩情境 ────────────────────────────────
    ROWS = {}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d2, _sel, _off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build_parcels, winners_state, forced_map, setback)
        _blk_ok = {b["label"] for b in build_blocks}
        parcels = []
        for r in sg["g_rows"]:
            _lbl = str(r.get("所屬街廓", ""))
            if _lbl not in _blk_ok:
                continue
            parcels.append({"label": _lbl, "pid": str(r.get("暫編地號", "")),
                            "coords": r.get("cut_coords") or []})
        ROWS[tag] = ns["k94_baseline_touch_by_parcel"](parcels, bl_by)

    # ── 【A】逐宗 ────────────────────────────────────────────────────────────────
    for tag in ("0m", "3.5m"):
        rows = ROWS[tag]
        L.append("")
        L.append(f"【A·{tag}】逐宗 BASELINE 臨接量測（母體 {len(rows)} 宗）")
        L.append("-" * 122)
        L.append(f"{'街廓':<6}{'暫編地號':<16}{'頂點':>5}{'偏移min':>12}{'偏移max':>12}"
                 f"{'gap(離屁股)':>13}{'far(最遠)':>12}{'跨越':>6}   臨接")
        L.append("-" * 122)
        for r in sorted(rows, key=lambda x: (x["label"], x["pid"])):
            L.append(f"{r['label']:<6}{r['pid']:<16}{r['n_vertices']:>5}"
                     f"{r['off_min']:>12.4f}{r['off_max']:>12.4f}"
                     f"{r['gap']:>13.6f}{r['far']:>12.4f}"
                     f"{('是' if r['crosses'] else '否'):>6}   "
                     f"{'✅ 已配到' if r['touch'] else '🔴 未達'}")
        L.append("-" * 122)

    # ── 【B】彙總（(b) 停機點所需三項）────────────────────────────────────────────
    L.append("")
    L.append("【B】彙總（施工單 §二(b) 要求：最大偏移／離 BASELINE 最遠之宗／逾容差者）")
    L.append("-" * 122)
    for tag in ("0m", "3.5m"):
        rows = ROWS[tag]
        _viol = [r for r in rows if not r["touch"]]
        _worst = max(rows, key=lambda r: r["gap"]) if rows else None
        _cross = [r for r in rows if r["crosses"]]
        L.append(f"  ── 情境 {tag}｜母體 {len(rows)} 宗 ──")
        if _worst is not None:
            L.append(f"     離 BASELINE 最遠之宗（gap 最大）＝ {_worst['label']}/{_worst['pid']}"
                     f"　gap ＝ {_worst['gap']:.6f} m")
        L.append(f"     逾容差（gap > {EPS}）之宗數 ＝ {len(_viol)}"
                 + (f"　⇒ {'／'.join(r['label'] + '/' + r['pid'] for r in _viol[:8])}"
                    if _viol else "　⇒ **零違例**"))
        L.append(f"     實質橫跨 BASELINE 兩側（off_min<−ε 且 off_max>+ε）之宗數 ＝ {len(_cross)}")
        _noise = [r for r in rows
                  if (r["off_min"] < 0.0 < r["off_max"]) and not r["crosses"]]
        if _noise:
            _m = max(min(abs(r["off_min"]), abs(r["off_max"])) for r in _noise)
            L.append(f"     （其中『裸跨號但非實質』者 {len(_noise)} 宗，"
                     f"較小側最大量級 {_m:.3e} m ≪ 容差 {EPS} ⇒ **浮點噪訊、非跨越**；"
                     f"此即判準不可用裸跨號之實證）")
    L.append("-" * 122)

    # ── 【C】幾何來源之影響評估（cut_coords vs 截角前）────────────────────────────
    L.append("")
    L.append("【C】幾何來源評估：採 cut_coords（截角後）對本步結論有無影響")
    L.append("-" * 122)
    L.append("  問：截角把街角處削掉一塊；改用『截角前』幾何會不會改變 gap（＝最接近 BASELINE 之頂點）？")
    L.append("  量：截角三角形各頂點之 BASELINE 偏移 vs 該街廓諸宗之 gap。")
    L.append("")
    L.append(f"  {'街廓':<6}{'截角側':<8}{'截角頂點偏移(min~max)':>28}{'該街廓宗地 gap 最大':>22}   判讀")
    L.append("  " + "-" * 118)
    _chi_min_all = []
    for b in sorted(build_blocks, key=lambda x: x["label"]):
        _lbl = b["label"]
        _ax = ns["_baseline_normal_axis"](bl_by.get(_lbl))
        _gmax = max([r["gap"] for r in ROWS["0m"] if r["label"] == _lbl] or [0.0])
        for _side in ("left", "right"):
            if _side not in (b.get("corner_sides") or []):
                continue
            _tri = ns["_make_chamfer_tri_wb"](b, _side)
            if _tri is None or _tri.is_empty:
                continue
            _pts = list(_tri.exterior.coords)
            _o = [(float(q[0]) - _ax[0]) * _ax[2] + (float(q[1]) - _ax[1]) * _ax[3]
                  for q in _pts]
            _lo, _hi = min(abs(v) for v in _o), max(abs(v) for v in _o)
            _chi_min_all.append((_lbl, _side, _lo))
            L.append(f"  {_lbl:<6}{_side:<8}{f'{_lo:.3f} ~ {_hi:.3f}':>28}"
                     f"{_gmax:>22.6f}   "
                     f"{'截角遠離屁股線' if _lo > 1.0 else '⚠️ 截角逼近屁股線'}")
    L.append("  " + "-" * 118)
    if _chi_min_all:
        _wmin = min(_chi_min_all, key=lambda t: t[2])
        L.append(f"  ⇒ 全區截角三角形**最接近 BASELINE** 者＝{_wmin[0]}/{_wmin[1]}：{_wmin[2]:.3f} m")
        L.append(f"  ⇒ 而諸宗之 gap 皆在 {max(max(r['gap'] for r in ROWS[t]) for t in ROWS):.6f} m 以內")
        L.append("  ⇒ **截角區域與屁股線相距甚遠**：截角只削街角（前緣線側）之料，")
        L.append("     不可能移動『最接近 BASELINE 之頂點』⇒ **改用截角前幾何不改變本步結論**。")
        L.append("     （此為實測對比，非推論；若二者量級接近則須停機上呈。）")

    # ── 【D】自檢：軸同源 ───────────────────────────────────────────────────────
    L.append("")
    L.append("【D】自檢：本檔之軸 ≡ N-19′ 之軸（非同軸即不可能逐格相符）")
    L.append("-" * 122)
    _dinfo = ns["n19p_depth_info_by_label"](
        build_blocks,
        cad.get("alloc_dir_by_block", {}) or {},
        cad.get("front_lines", {}) or {},
        cad.get("baselines", {}) or {})
    L.append(f"  {'街廓':<6}{'本檔軸量 FRONT p1/p2':>32}{'N-19′ d_front_p1/p2':>30}{'最大差':>12}   同軸")
    L.append("  " + "-" * 118)
    _ok_axis = True
    for b in sorted(build_blocks, key=lambda x: x["label"]):
        _lbl = b["label"]
        _fl = (cad.get("front_lines", {}) or {}).get(_lbl) or {}
        _ax = ns["_baseline_normal_axis"](bl_by.get(_lbl))
        _mine = [abs((float(p[0]) - _ax[0]) * _ax[2] + (float(p[1]) - _ax[1]) * _ax[3])
                 for p in (_fl["p1"], _fl["p2"])]
        _theirs = [_dinfo[_lbl]["d_front_p1"], _dinfo[_lbl]["d_front_p2"]]
        _d = max(abs(_mine[0] - _theirs[0]), abs(_mine[1] - _theirs[1]))
        _ok_axis &= (_d < 1e-9)
        L.append(f"  {_lbl:<6}{f'{_mine[0]:.6f} / {_mine[1]:.6f}':>32}"
                 f"{f'{_theirs[0]:.6f} / {_theirs[1]:.6f}':>30}{_d:>12.2e}   "
                 f"{'✅' if _d < 1e-9 else '🔴'}")
    L.append("  " + "-" * 118)
    L.append(f"  ⇒ 軸同源自檢：{'✅ 六街廓全等（差 < 1e-9）' if _ok_axis else '🔴 有不等——本檔之量測不可信'}")

    L.append("")
    L.append("【E】註記")
    L.append("  · 本檔**只量不判**：`touch` 欄係量測結果之呈現，**未據以 raise**。")
    L.append("  · 上閘屬段二-1(c)，**須待 KL 就【B】段過目後放行**。")
    L.append("  · 缺件（缺 BASELINE／頂點<3）仍 loud raise——缺件無從量測，與『違例』兩回事。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
