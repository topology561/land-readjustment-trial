# -*- coding: utf-8 -*-
"""K-9-5 街角第 1 宗**寬度實量**（**截角前**）— **只量不改·只量不判**。

## 本探針之定位（**先讀**）

**K-9-5**（KL 裁 2026-08-01·正典
`grep -n "^## K-9 " docs/rulings/K-6_街角地分配程序與可分配判準.md`）：
街角第 1 宗**寬度要實量**，門檻 ＝ **退縮寬 ＋ 畸零地最小寬**；其餘各宗 ＝ 畸零地最小寬。
此係 K-7（寬深豁免）**撤銷**後之新判準。

K-9-5 是段四唯一有**實質土地風險**者——退縮 3.5m 情境下街角門檻由 `3.50` 升為 **`7.00`**，
而八個街角地**從未被量過寬度**。

⇒ **本探針先只量不判，把數字給 KL 看；KL 確認後才由 K-6-A2 上閘。**

- ⛔ **不掛 `run_all` 之判定鏈**（只量不判 ⇒ **無 PASS/FAIL 貢獻**）。
  `grep -n "probe" verify/run_all.py` ⇒ 本檔**不在其中**（掛回前須先上呈）。
- ⛔ **不改 `app.py` 任何一行**；量測一律走**倉內既有原語與其自帶容差**。
- 本探針之 rc **恆為 0**（量測結果不設 rc）；**唯缺件／取不到資料時 loud raise**
  （no-silent-fallback）。

## 量測所用之既有原語（**禁自寫幾何算法·禁自訂容差**）

| 用途 | 原語 | 查法 |
|---|---|---|
| 宗地最小寬度（N-14） | `app.parcel_min_width_n14` | `grep -n "def parcel_min_width_n14" app.py` |
| 截角三角形（per side） | `app._make_chamfer_tri_wb` | `grep -n "def _make_chamfer_tri_wb" app.py` |
| 畸零地最小寬（法定附表） | `app.get_min_lot_size(分區, 正面路寬)['min_width']` | `grep -n "def get_min_lot_size" app.py` |
| 街角 winner（per side） | `winners_state[blk]['p1_end'/'p2_end']` | `verify/selection_pipeline.py::run_corner_pk` |
| 強制留設抵費地 | `forced_map[blk]['left_forced_offset'/'right_forced_offset']` | 同上 |

`parcel_min_width_n14` 自帶之三道 loud raise（臨接 FRONT／E-2′ 深度／E-8a 凸性）
**照其設計語意生效**——本探針**不吞**，逐格記入「量測結果」欄。

## 🔴 截角前幾何（§4 末段·**本探針之核心風險點**）

正典 §4 末段：「角地應截角時，其**寬度及深度係指截角前**之寬度及深度」
（`grep -n "截角前" docs/rulings/K-6_街角地分配程序與可分配判準.md`）。

現行 `cut_coords` 係**截角後** ⇒ **直接餵會量到偏小的寬度、造成假不合格**。
故本探針之截角前幾何 ＝ `Polygon(cut_coords) ∪ _make_chamfer_tri_wb(blk, side)`。

**倉內既有事實**（K-8 §五 實作附記）：`SIDE_LINE ＝ 截角前側界；街廓邊界 ＝ 截角後側界`；
街廓多邊形本身即截角後（街廓 ∩ 截角三角形 ＝ 0.0000㎡）⇒ 上開聯集**恆不重疊**。

⚠️ **本探針實測發現：該聯集之接合型態有兩類**（見「接合」欄，逐格列明）：

- **邊接合**（`宗 ∩ 截角三角形` ＝ `LineString`·本案實測 ~5.0m）
  ⇒ 聯集為**單一 Polygon** ⇒ 截角前幾何**良定義**、可量。
- **點接合**（該交集 ＝ `Point`）⇒ 聯集為 **MultiPolygon** ⇒ 該宗**並未以邊臨接截角**
  ⇒ **截角前幾何在現行構造下不良定義** ⇒ 本探針**不代裁、不兜底**，
  該格之截角前寬度記 `—`，另記其**截角後**寬度供 KL 參照。

⛔ **禁以 `buffer(±ε)` 合攏點接合**：實測其**非單調**
（R4 右：`±1e-6/±1e-5` 合成 Polygon，而 `±1e-4/±1e-3` 又散回 MultiPolygon）
⇒ 該手法係**換了一把尺**、非更嚴謹。**已上呈 KL 待裁**（見報告 §「上呈」）。

## 輸出

- log：`verify/out/probe_ruling_K9_corner_width.log`
- CSV：`verify/out/probe_ruling_K9_corner_width.csv`（**只寫 `out/`·不進 `baselines/`**）

兩情境（0m／3.5m）× **八街角全列**（無 winner 之側亦列，並記其成因）。

## 重跑
    python verify/probes/probe_ruling_K9_corner_width.py
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon                                # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_ruling_K9_corner_width.log")
CSV = os.path.join(OUTDIR, "probe_ruling_K9_corner_width.csv")

COLS = ["情境", "街廓", "側別", "退縮(m)", "畸零地最小寬(m)", "門檻(m)",
        "街角第1宗", "接合", "寬度_截角前(m)", "寬度_截角後(m)",
        "差(截角前−門檻)", "若上閘會如何"]

_END_OF = {"left": "p1_end", "right": "p2_end"}
_FORCED_OF = {"left": "left_forced_offset", "right": "right_forced_offset"}


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_K9_corner_width：{msg}（no-silent-fallback）")


def _front_axis(front_lines, blk):
    """FRONT 之單位方向 d̂ 與起點 p1（`parcel_min_width_n14` 之量測軸·同 E 系列口徑）。"""
    fl = (front_lines or {}).get(blk) or {}
    if not (fl.get("p1") and fl.get("p2")):
        _fail(f"{blk} 缺 FRONT_LINE —— N-14 之量測軸不可定義")
    p1 = np.asarray(fl["p1"], float)[:2]
    p2 = np.asarray(fl["p2"], float)[:2]
    L = float(np.linalg.norm(p2 - p1))
    if L <= 0:
        _fail(f"{blk} FRONT_LINE 長度 0")
    return (p2 - p1) / L, p1


def _measure_width(width_fn, coords, d, p1, md, label):
    """走 `parcel_min_width_n14`（**唯一寬度原語**）。其 loud raise 不吞、轉為文字記錄。"""
    try:
        return f"{float(width_fn(coords, tuple(d), tuple(p1), md, _label=label)):.4f}", ""
    except RuntimeError as e:
        return "—", "🔴raise:" + str(e).split("：", 1)[-1].splitlines()[0][:60]


def _join_kind(parcel_poly, tri):
    """宗與截角三角形之接合型態 ⇒ 決定截角前幾何是否良定義。**不做任何合攏**。"""
    if tri is None:
        return "無截角", None, "該側無截角三角形（`_make_chamfer_tri_wb` 回 None）"
    inter = parcel_poly.intersection(tri)
    u = parcel_poly.union(tri)
    if u.geom_type == "Polygon":
        return ("邊接合", u,
                f"宗∩截角＝{inter.geom_type}·長 {getattr(inter, 'length', 0.0):.4f}m")
    return ("點接合", None,
            f"宗∩截角＝{inter.geom_type}（非邊）⇒ 聯集為 {u.geom_type}"
            f"·截角前幾何**不良定義**")


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L, rows = [], []
    L.append("=" * 118)
    L.append("【K-9-5 街角第 1 宗寬度實量（截角前）】**只量不判**——KL 過目材料，"
             "上閘屬 K-6-A2")
    L.append("=" * 118)

    ns, fake_st = harvest()
    width_fn = ns.get("parcel_min_width_n14")
    if not callable(width_fn):
        _fail("harvest 未取得 parcel_min_width_n14")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    front_lines = cad.get("front_lines") or {}
    sides_by = cad.get("side_lines_by_side", {}) or {}
    corners = [(lbl, w) for lbl in rv.CORNER_BLOCKS for w in ("left", "right")
               if w in (sides_by.get(lbl) or {})]
    if not corners:
        _fail("取不到任何街角側（side_lines_by_side 全空）")
    L.append(f"街角側共 {len(corners)} 個："
             f"{'、'.join(f'{b}/{s}' for b, s in corners)}")

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6_raw = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6_raw, list(cb_by.values()), snapshot)

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _md_by, _mw_par = {}, {}
        for p in params:
            _md_by[str(p["街廓"])] = float(p.get("法定最小深(m)", 0) or 0)
            _mw_par[str(p["街廓"])] = float(p.get("法定最小寬(m)", 0) or 0)
        if not all(v > 0 for v in _md_by.values()):
            _fail(f"[{tag}] 法定最小深缺／≤0：{_md_by}")
        _d, _sel, _off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build_parcels, winners_state, forced_map, setback)
        by_pid = {}
        for r in sg["g_rows"]:
            by_pid[(str(r.get("所屬街廓", "")), str(r.get("暫編地號", "")))] = r

        for blk, side in corners:
            b = cb_by[blk]
            # 畸零地最小寬＝法定附表（S1 §6 查表化之正典路徑）
            mw = float(ns["get_min_lot_size"](
                b["category"],
                float(snapshot["blocks"][blk]["正面"]["路寬_m"]))["min_width"])
            # 免費一致性看守：與參數表之「法定最小寬(m)」須同值（二者本應同源）
            if abs(mw - _mw_par.get(blk, -1.0)) > 0:
                _fail(f"[{tag}] {blk} 畸零地最小寬兩來源分歧："
                      f"get_min_lot_size={mw} vs 參數表={_mw_par.get(blk)}"
                      f"——量測基準不唯一，停")
            thr = setback + mw
            rec = {"情境": tag, "街廓": blk, "側別": side,
                   "退縮(m)": f"{setback:.2f}", "畸零地最小寬(m)": f"{mw:.2f}",
                   "門檻(m)": f"{thr:.2f}"}
            pid = (winners_state.get(blk) or {}).get(_END_OF[side])
            if not pid:
                _why = ("強制留設抵費地"
                        if (forced_map.get(blk) or {}).get(_FORCED_OF[side])
                        else "無街角 winner")
                rec.update({"街角第1宗": f"—（{_why}）", "接合": "—",
                            "寬度_截角前(m)": "—", "寬度_截角後(m)": "—",
                            "差(截角前−門檻)": "—",
                            "若上閘會如何": f"—（該情境無街角第 1 宗·{_why}）",
                            "_w_pre": "—", "_w_post": "—", "_exc": ""})
                rows.append(rec)
                continue
            r = by_pid.get((blk, str(pid)))
            if r is None:
                _fail(f"[{tag}] {blk}/{side} winner {pid} 不在 g_rows —— 上游不一致")
            cc = r.get("cut_coords") or []
            if len(cc) < 3:
                _fail(f"[{tag}] {blk}/{side} {pid} cut_coords 不足（{len(cc)} 點）")
            poly = Polygon([(float(c[0]), float(c[1])) for c in cc])
            tri = ns["_make_chamfer_tri_wb"](b, side)
            kind, pre_poly, note = _join_kind(poly, tri)
            d, p1 = _front_axis(front_lines, blk)
            md = _md_by[blk]
            w_post, e_post = _measure_width(
                width_fn, cc, d, p1, md, f"{blk}·{pid}·截角後")
            if pre_poly is not None:
                w_pre, e_pre = _measure_width(
                    width_fn, list(pre_poly.exterior.coords), d, p1, md,
                    f"{blk}·{pid}·截角前")
            else:
                w_pre, e_pre = "—", ""
            if w_pre != "—":
                _diff = float(w_pre) - thr
                _dtxt = f"{_diff:+.4f}"
                _verd = ("合格（K-9-5 上閘後仍過）" if _diff >= 0
                         else "🔴 **不合格**（K-9-5 上閘後翻盤）")
            elif kind == "點接合":
                _dtxt = "—"
                _verd = "⏸ 截角前幾何不良定義 ⇒ **待 KL 裁**（本探針不代裁）"
            else:
                _dtxt = "—"
                _verd = f"⏸ 無法量測：{e_pre or e_post or note}"
            rec.update({"街角第1宗": str(pid), "接合": f"{kind}（{note}）",
                        "寬度_截角前(m)": w_pre + (f" {e_pre}" if e_pre else ""),
                        "寬度_截角後(m)": w_post + (f" {e_post}" if e_post else ""),
                        "差(截角前−門檻)": _dtxt, "若上閘會如何": _verd,
                        # 列印用：數字欄不摻例外文字（例外另立診斷區）
                        "_w_pre": w_pre, "_w_post": w_post,
                        "_exc": "／".join(x for x in (e_pre, e_post) if x)})
            rows.append(rec)

    # ── 列印 ────────────────────────────────────────────────────────────────
    for tag in ("0m", "3.5m"):
        L.append("")
        L.append(f"【{tag}】門檻 ＝ 退縮 ＋ 畸零地最小寬")
        L.append("-" * 118)
        L.append(f"  {'街廓':5}{'側':>6}{'退縮':>7}{'最小寬':>8}{'門檻':>8}"
                 f"{'街角第1宗':>16}{'接合':>8}{'截角前寬':>11}{'截角後寬':>11}"
                 f"{'差':>11}  若上閘會如何")
        for r in [x for x in rows if x["情境"] == tag]:
            L.append(f"  {r['街廓']:5}{r['側別']:>6}{r['退縮(m)']:>7}"
                     f"{r['畸零地最小寬(m)']:>8}{r['門檻(m)']:>8}"
                     f"{r['街角第1宗']:>16}{r['接合'].split('（')[0]:>8}"
                     f"{r['_w_pre']:>11}{r['_w_post']:>11}"
                     f"{r['差(截角前−門檻)']:>11}  {r['若上閘會如何']}")

    # ── 接合診斷（點接合＝上呈項之實料）───────────────────────────────────────
    L.append("")
    L.append("【接合診斷】截角前幾何是否良定義（**點接合者不代裁·上呈 KL**）")
    L.append("-" * 118)
    for r in rows:
        if r["接合"] == "—":
            continue
        L.append(f"  {r['情境']:5}{r['街廓']:4}{r['側別']:>6}  {r['接合']}")

    # ── 量測例外（`parcel_min_width_n14` 之 loud raise·**不吞·逐格列明**）──────
    _exc = [r for r in rows if r.get("_exc")]
    L.append("")
    L.append("【量測例外】`parcel_min_width_n14` 之 loud raise（其設計語意·本探針不吞）")
    L.append("-" * 118)
    if not _exc:
        L.append("  （無）")
    for r in _exc:
        L.append(f"  {r['情境']:5}{r['街廓']:4}{r['側別']:>6} {r['街角第1宗']}：{r['_exc']}")

    _pt = [r for r in rows if r["接合"].startswith("點接合")]
    _bad = [r for r in rows if r["若上閘會如何"].startswith("🔴")]
    L.append("")
    L.append("-" * 118)
    L.append(f"【彙總】列數 {len(rows)}（{len(rv.CORNER_BLOCKS)} 街廓／"
             f"{len(corners)} 街角側 × 2 情境）")
    L.append(f"  · 可量測（邊接合）        ：{sum(1 for r in rows if r['接合'].startswith('邊接合'))} 格")
    L.append(f"  · **點接合·截角前不良定義**：{len(_pt)} 格 ⇒ **上呈 KL**")
    L.append(f"  · 無街角第 1 宗（含強制抵費地）：{sum(1 for r in rows if r['接合'] == '—')} 格")
    L.append(f"  · **K-9-5 上閘後會翻盤（不合格）**：{len(_bad)} 格")
    for r in _bad:
        L.append(f"      🔴 {r['情境']} {r['街廓']}/{r['側別']} {r['街角第1宗']}："
                 f"截角前寬 {r['寬度_截角前(m)']} < 門檻 {r['門檻(m)']}"
                 f"（差 {r['差(截角前−門檻)']}）")
    L.append("")
    L.append("RESULT: 只量不判（**無 PASS/FAIL 貢獻·rc 恆 0**）——判準上閘屬 K-6-A2，"
             "前置＝本表經 KL 過目")
    L.append("=" * 118)

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    with open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        # `_w_pre`／`_w_post`／`_exc` 係**列印用**私有欄（數字欄不摻例外文字）
        # ⇒ CSV 只出 `COLS`。`extrasaction="ignore"` 為此而設、非吞錯。
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"\n→ {os.path.relpath(LOG, REPO)}\n→ {os.path.relpath(CSV, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
