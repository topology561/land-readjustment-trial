# -*- coding: utf-8 -*-
"""W-G.5 裁定 N — **E 系列實測快照**（E-1′／E-2′／E-8／E-9／K-4·逐宗·兩情境）。

## 為何存在（BLOCKED-3·claude.ai 二度指認）

E 系列之全部依據（「45/59 距 FRONT 僅 4µm–247µm」「R3 街角宗 0.7655m」「R4 負側 −1.48e-2」）
先前**只存在於聊天與註解**，`verify/probes/` 無對應檔 ⇒ **倉內不可重現**。
倉內報告＝唯一本體（`CLAUDE.md`）⇒ 本檔把該批量測**機器化並入倉**。

## 量什麼

令 `t` ＝ 該宗頂點沿 **FRONT_LINE 法向**（指向宗地內）之深度（`front_pt = FRONT_LINE.p1`）。
逐宗輸出 `min t`（E-1′ 之判準量）、`max t`（E-2′ 之判準量）、
`凸性Δ` ＝ `convex_hull.area − poly.area`（E-8a 之判準量）、
`寬度` ＝ `parcel_min_width_n14` 之實際回傳（**真函式**·非複寫）。

## 兩層輸出

1. **實測快照**（回歸）：`verify/out/E系列實測快照_退縮{tag}.csv`
   → 對 `verify/baselines/E系列實測快照_退縮{tag}.csv` 逐格 diff。
   ⚠️ 該快照之身分 ＝ **回歸快照**（regression snapshot），**不是真值錨**
   （`fixture-provenance`：期望值不得由新碼現跑回填當真值）。
2. **獨立真值斷言**（T1–T7·**才是**正確性之舉證）：見 `_truth_assertions`，
   每條各自附出處；快照 diff 綠而 T 條紅 ⇒ **仍紅**。

## 重跑
    python verify/probes/probe_ruling_N_e1_touch.py            # 量測＋比對（rc=0 綠／1 紅）
    python verify/probes/probe_ruling_N_e1_touch.py --bake     # 重烤快照（**改碼致值變時才用**）

⚠️ **零注入·唯讀**：不改任何引擎狀態；`run_all` 以 subprocess 起（走 `[1/3]` golden 段
⇒ **不動 `run_verification.results` 之 PASS/FAIL 計數**）。
"""
import csv
import json
import math
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
BASEDIR = os.path.join(VERIFY, "baselines")
LOG = os.path.join(OUTDIR, "probe_ruling_N_e1_touch.log")
SNAP_NAME = "E系列實測快照_退縮{tag}.csv"

COLS = ["情境", "街廓", "暫編地號", "街角地", "第1筆街角", "街角側別",
        "min_t", "max_t", "凸性Δ(㎡)", "寬度(m)", "臨街邊長(m)", "E-6差(m)", "判定"]

# 非配地列（步驟 J 之濾集·`grep -n "Patch B-2" app.py` 同口徑）
_SKIP_SIDES = ("抵費地", "🟠 孤立公設地", "💰 現金補償")

EPS_TOUCH = 0.01        # 法定粒度（實施辦法 §3 長度 2dp）——KL 域裁·已鎖
# 🆕 快照 `min_t` 之**零判定**：|t| < 1e-12 一律記為 `0.000e+00`。
#   理由：快照係**跨機回歸**比對；(s,t) 局部框座標量級 O(1e2) ⇒ 雙精度絕對噪訊 ~1e-14，
#   而 `%.3e` 會把 −4.6e-14 與 +1.2e-14 印成**不同字串** ⇒ 產生與幾何無關之假紅。
#   1e-12 ＝ 噪訊上界之 100 倍、且**低於本案最小真實 |min t|（1.04e-08）四個數量級**
#   ⇒ 不損鑑別力。**非**法律門檻、**非**實測殘差定閘（僅為列印之零規範化）。
EPS_SNAP_ZERO = 1e-12
EPS_CONVEX = 0.01       # 法定粒度（面積 2dp）——E-8a 判準寬

_SNAP_CACHE = {}        # 案例快照（T4 之 SIDE_LINE 側數由此導出·非寫死）
_Q_CACHE = {}           # DXF 實測坐標量化步長 q（T6 之閘寬·逐檔實測·禁硬編）
_MERGE_CACHE = {}       # T7：步驟 J 判定 → merge_subparcels_by_parent 之真跑結果


def _e7_merge_gate(ns, g_rows, front_lines, min_depth_by_blk, min_width_by_blk,
                   mina_by_blk, corner_area_by_blk):
    """T7（**K-4 版**）之實料：以 module 級真判定逐宗評 ＋ 真跑 `merge_subparcels_by_parent`。

    K-4（KL 裁 2026-07-27）：街角第 1 宗**不走 N-14**，其判定 ＝
    `G ≥ 街角最小分配面積`（＝ (Ⅰ) 街角規定範圍面積）之**蘊含**。
    ⇒ 舊「待判（截角）」框架作廢；`PENDING` 態自此**不應再產生**。

    ⚠️ **不改引擎狀態**：`g_rows` 先 deepcopy（探針零注入）。
    """
    import copy as _cp
    _ev = ns["evaluate_parcel_width_n14"]

    def _eval_rows(_src, _g_override=None):
        _rows = _cp.deepcopy(_src)
        _k4, _pend = [], []
        for r in _rows:
            _blk = str(r.get("所屬街廓", ""))
            _sd = {"左側": "left", "右側": "right"}.get(str(r.get("街角側別", "")).strip())
            _thr = (corner_area_by_blk.get(_blk) or {}).get(_sd) if _sd else None
            if _g_override and str(r.get("暫編地號")) in _g_override:
                r["G(㎡)"] = _g_override[str(r.get("暫編地號"))]
            r.update(_ev(r, (front_lines or {}).get(_blk) or {},
                         float(min_depth_by_blk.get(_blk, 0.0) or 0.0),
                         float(min_width_by_blk.get(_blk, 0.0) or 0.0),
                         corner_min_area=_thr,
                         _label=f"{_blk}·{r.get('暫編地號')}"))
            _v = r.get("寬度判定")
            if _v == ns["WIDTH_VERDICT_CORNER_K4"]:
                _k4.append(r)
            elif _v == ns["WIDTH_VERDICT_PENDING"]:
                _pend.append(str(r.get("暫編地號")))
        return _rows, _k4, _pend

    _rows, _k4, _pend = _eval_rows(g_rows)
    # ① 街角 winner 皆 G ≥ 門檻（K-4 之實質檢驗·門檻缺者另計）
    _viol, _nothr = [], []
    for r in _k4:
        _g = r.get("_width_k4_G")
        _t = r.get("_width_k4_threshold")
        if _t is None or _g is None:
            _nothr.append(str(r.get("暫編地號")))
        elif float(_g) < float(_t):
            _viol.append(f"{r.get('所屬街廓')}·{r.get('暫編地號')}：G {_g} < 門檻 {_t}")
    _merged = ns["merge_subparcels_by_parent"](_rows, mina_by_blk)["merged_rows"]
    # ② 無街角 winner 以 PENDING 態產出（K-4 後該態邏輯上不可能）
    _leak = [str(m.get("暫編地號")) for m in _merged
             if str(m.get("寬度判定", "")) == ns["WIDTH_VERDICT_PENDING"]]
    # ③ **鑑別力**：刻意把某街角 winner 之 G 壓到門檻下 ⇒ ① 必須抓到
    _disc = None
    if _k4:
        _t0 = next((r for r in _k4 if r.get("_width_k4_threshold") is not None), None)
        if _t0 is not None:
            _pid0 = str(_t0.get("暫編地號"))
            _low = round(float(_t0["_width_k4_threshold"]) - 1.0, 2)
            _, _k4b, _ = _eval_rows(g_rows, {_pid0: _low})
            _hit = any(float(r.get("_width_k4_G", 0) or 0)
                       < float(r.get("_width_k4_threshold", 0) or 0)
                       for r in _k4b if str(r.get("暫編地號")) == _pid0)
            _disc = (_pid0, _low, _hit)
    return {"n_k4": len(_k4), "n_pending": len(_pend),
            "n_corner": sum(1 for r in g_rows if str(r.get("街角地", "")).strip() == "是"),
            "n_merged": len(_merged), "viol": _viol, "no_thr": _nothr,
            "leak": _leak, "disc": _disc}


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_N_e1_touch：{msg}（no-silent-fallback）")


def _measure(g_rows, front_lines, min_depth_by_blk, width_fn, tag):
    """逐宗量 min t／max t／凸性Δ／寬度。**不吞例外**：`parcel_min_width_n14` 之
    loud raise 係其設計語意 ⇒ 記為 `判定` 欄之內容、不轉靜默。"""
    rows = []
    for r in g_rows:
        if r.get("推進側別") in _SKIP_SIDES:
            continue
        blk = str(r.get("所屬街廓", ""))
        pid = str(r.get("暫編地號", ""))
        cc = r.get("cut_coords") or []
        fl = (front_lines or {}).get(blk) or {}
        if not (fl.get("p1") and fl.get("p2")):
            _fail(f"{blk}·{pid} 缺 FRONT_LINE——E 系列之量測軸不可定義")
        if len(cc) < 3:
            _fail(f"{blk}·{pid} cut_coords 不足（{len(cc)} 點）")
        p1 = np.asarray(fl["p1"], float)[:2]
        p2 = np.asarray(fl["p2"], float)[:2]
        _L = float(np.linalg.norm(p2 - p1))
        if _L <= 0:
            _fail(f"{blk} FRONT_LINE 長度 0")
        d = (p2 - p1) / _L
        n = np.array([-d[1], d[0]], dtype=float)
        poly = Polygon([(float(c[0]), float(c[1])) for c in cc])
        if not poly.is_valid:
            poly = poly.buffer(0)
        if poly.is_empty or poly.geom_type != "Polygon":
            _fail(f"{blk}·{pid} 幾何非單一 Polygon（{poly.geom_type}）")
        cen = np.asarray(poly.centroid.coords[0], float)
        if float(np.dot(cen - p1, n)) < 0:
            n = -n
        ring = list(poly.exterior.coords)
        tv = [float(np.dot(np.asarray(v[:2], float) - p1, n)) for v in ring]
        t_min, t_max = min(tv), max(tv)
        conv = float(poly.convex_hull.area - poly.area)
        # ── E-6 之比對對象：**由 cut_coords 直接量得之臨街邊長**（歐氏長·不經任何弦機制）
        #    ＝ 兩端點皆在法定粒度內之邊之長度和。與 `parcel_min_width_n14` **無共用碼路徑**
        #    ⇒ 構成真正的「跨層」自檢（非同一算式自我對照）。
        fl_len = 0.0
        for _i in range(len(ring) - 1):
            if abs(tv[_i]) <= EPS_TOUCH and abs(tv[_i + 1]) <= EPS_TOUCH:
                fl_len += float(np.linalg.norm(np.asarray(ring[_i + 1][:2], float)
                                               - np.asarray(ring[_i][:2], float)))
        is_corner = str(r.get("街角地", "")).strip() == "是"
        md = float(min_depth_by_blk.get(blk, 0.0) or 0.0)
        if is_corner:
            # 🆕 **K-4**（KL 裁 2026-07-27）：街角第 1 宗**不走 N-14**——(Ⅰ) 街角規定範圍
            #    之寬度即法規最小寬 ⇒ `G ≥ 街角最小分配面積` 蘊含寬深合格（已於 winner
            #    選拔時檢過）。舊「待判（截角）」框架**作廢**。
            w_s, verdict, e6 = "—", "街角·K-4 面積門檻蘊含（N-14 不適用）", "—"
        else:
            try:
                _w = float(width_fn(cc, tuple(d), tuple(p1), md, _label=f'{blk}·{pid}'))
                w_s = f"{_w:.4f}"
                e6 = f"{abs(_w - fl_len):.3e}"
                verdict = "臨街(法定粒度內)"
            except RuntimeError as e:
                w_s, e6 = "—", "—"
                verdict = "🔴raise:" + str(e).split("：", 1)[-1][:48]
        rows.append({
            "情境": tag, "街廓": blk, "暫編地號": pid,
            "街角地": str(r.get("街角地", "")), "第1筆街角": str(r.get("第1筆街角", "")),
            "街角側別": str(r.get("街角側別", "")),
            "min_t": ("0.000e+00" if abs(t_min) < EPS_SNAP_ZERO else f"{t_min:.3e}"),
            "max_t": f"{t_max:.4f}",
            "凸性Δ(㎡)": f"{conv:.6f}", "寬度(m)": w_s,
            "臨街邊長(m)": f"{fl_len:.4f}", "E-6差(m)": e6, "判定": verdict,
        })
    return rows


def _truth_assertions(rows_by_tag, L):
    """**獨立真值斷言**（非快照回歸）。每條附出處；任一紅 ⇒ 整支紅。"""
    bad = []
    L.append("")
    L.append("【T】獨立真值斷言（出處各自列明·快照綠而此處紅仍算紅）")
    L.append("-" * 112)

    # T1 R3·628-45(2)（**0m 專屬**）之 min t ≈ 0.7655
    #    出處：claude.ai 由 data/V6.dxf 獨立重建 R3 右側道路截角斜邊頂點
    #          (89.8392, 0) → (93.3461, 3.4782)（FRONT_LINE 全長 93.4051
    #          ＝ SIDE/FRONT 延伸理論交點）——**非**由本碼現跑回填。
    #    ⚠️ **只在 0m 成立**：3.5m 情境下 R3 右為「強制抵費地」（見 T4 之 baseline 出處）
    #       ⇒ R3 無街角 winner ⇒ 該宗以**非街角**身分入列、min t 回落至 µm 級。
    #       此差異本身即 T1 之鑑別力（把它寫成兩情境同錨，就是拿錯的母體當錨）。
    _r0 = [r for r in rows_by_tag["0m"] if r["街廓"] == "R3" and r["暫編地號"] == "628-45(2)"]
    if not _r0:
        L.append("  T1[0m] 🔴 找不到 R3·628-45(2)")
        bad.append("T1[0m] 缺列")
    else:
        _v = float(_r0[0]["min_t"])
        _ok = abs(_v - 0.7655) <= 5e-4 and _r0[0]["街角地"] == "是"
        L.append(f"  T1[0m] R3·628-45(2)（街角={_r0[0]['街角地']}）min t = {_v:.6f}"
                 f"（錨 0.7655±5e-4·截角所致）  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T1[0m] 街角={_r0[0]['街角地']}·min t {_v:.6f} ≠ 0.7655±5e-4")
    _r35 = [r for r in rows_by_tag["3.5m"] if r["街廓"] == "R3" and r["暫編地號"] == "628-45(2)"]
    if not _r35:
        L.append("  T1′[3.5m] 🔴 找不到 R3·628-45(2)")
        bad.append("T1′[3.5m] 缺列")
    else:
        _ok = _r35[0]["街角地"] != "是" and abs(float(_r35[0]["min_t"])) <= EPS_TOUCH
        L.append(f"  T1′[3.5m] 同宗轉**非街角**（街角={_r35[0]['街角地']}）"
                 f"·min t = {float(_r35[0]['min_t']):.3e} ≤ {EPS_TOUCH}"
                 f"  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T1′[3.5m] 街角={_r35[0]['街角地']}·min t {_r35[0]['min_t']}")

    # T2 非街角宗之 |min t| 上界 ≤ 法定粒度 0.01
    #    出處：E-1′ 判準本身（KL 域裁之容差）。此條斷言「資料滿足該判準」。
    for tag in ("0m", "3.5m"):
        _nc = [r for r in rows_by_tag[tag] if r["街角地"] != "是"]
        _mx = max((abs(float(r["min_t"])) for r in _nc), default=0.0)
        _ok = _mx <= EPS_TOUCH
        L.append(f"  T2[{tag}] 非街角宗 max|min t| = {_mx:.3e} ≤ {EPS_TOUCH}"
                 f"（{len(_nc)} 宗）  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T2[{tag}] {_mx:.3e} > {EPS_TOUCH}")

    # T3 街角宗負側偏差：R4·628-1(1) ≈ −1.48e-2（**超容差**·正是 E-7 跳過之族）
    #    出處：claude.ai 複驗實測（本波 CC 側失敗考古之肇因值）。
    for tag in ("0m", "3.5m"):
        _r = [r for r in rows_by_tag[tag] if r["街廓"] == "R4" and r["暫編地號"] == "628-1(1)"]
        if not _r:
            L.append(f"  T3[{tag}] 🔴 找不到 R4·628-1(1)")
            bad.append(f"T3[{tag}] 缺列")
            continue
        _v = float(_r[0]["min_t"])
        _ok = abs(_v - (-1.4826e-2)) <= 5e-4
        L.append(f"  T3[{tag}] R4·628-1(1) min t = {_v:.6f}（錨 −1.4826e-2±5e-4·"
                 f"**負側超容差** ⇒ 雙向守衛之鑑別對象）  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T3[{tag}] {_v:.6f} ≠ −1.4826e-2±5e-4")

    # T4 `街角地=='是'` ⟺ `第1筆街角=='是'`（同一集合·無過度跳過）
    #    ＋ **筆數**對兩個獨立倉內來源：
    #      · 0m  ＝ `case_params_UC9898.json` 之 `有SIDE_LINE == true` 側數（本案 8）
    #      · 3.5m＝ 上數 − `baselines/W-D.1.3-d 驗收_退縮3.5m.csv` 之強制抵費地側數（3）
    #    ⇒ **不是**把實跑數字寫死（那是回填），而是由既有快照／baseline 導出。
    _n_side = sum(1 for b in _SNAP_CACHE["blocks"].values()
                  for k in ("左側", "右側")
                  if bool((b.get(k) or {}).get("有SIDE_LINE", False)))
    _n_forced = len(_read_csv(os.path.join(BASEDIR, "W-D.1.3-d 驗收_退縮3.5m.csv")))
    _exp_n = {"0m": _n_side, "3.5m": _n_side - _n_forced}
    for tag in ("0m", "3.5m"):
        _a = {r["暫編地號"] for r in rows_by_tag[tag] if r["街角地"] == "是"}
        _b = {r["暫編地號"] for r in rows_by_tag[tag] if r["第1筆街角"] == "是"}
        _ok = (_a == _b) and (len(_a) == _exp_n[tag])
        L.append(f"  T4[{tag}] 街角地 ⟺ 第1筆街角：{len(_a)} vs {len(_b)} 宗"
                 f"（期 {_exp_n[tag]} ＝ SIDE_LINE {_n_side} 側"
                 f"{'' if tag == '0m' else f' − 強制抵費地 {_n_forced} 側'}）"
                 f"  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T4[{tag}] 集合對稱差 {sorted(_a ^ _b)}／筆數 {len(_a)}≠{_exp_n[tag]}")

    # T6 **E-6 跨層自檢**：`parcel_min_width_n14` vs **由 cut_coords 直接量得之臨街邊長**
    #    （二者無共用碼路徑 ⇒ 真跨層）。
    #    ── 閘寬 ＝ **DXF 實測坐標量化步長 `q`**（`_detect_dxf_quantum`·本檔 1e-5）───────
    #    **依據（機制導出·非實測殘差·非留餘量）**：兩條 ALLOC 線之端點各被檔案寫入位數
    #    捨入 ⇒ 其夾角殘差 ~ `q/L`（`L`＝分配線長）⇒ 於量測帶深 `min_depth` 內所致之
    #    寬度差 ~ `(min_depth/L)·q` < `q`（因 `min_depth < L`）。
    #    本案 `14/33×1e-5 = 4.2e-6`，實測上界 **4.574e-06**（R1 `628-35(2)`）——**相符**。
    #    ⇒ 低於圖檔寫入量化步長之幾何偏差，在該圖檔上**不可分辨**（與 C-5 之
    #      「eps ＝ 法定粒度＋DXF 實測 q」同族）。**q 逐檔實測、禁硬編**（泛用化）。
    #    📌 交接文 §4.1 之 `≤1e-6` **低於本檔量化步長 1e-5**，在原理上不可達成
    #       ——非「閘太嚴」而是「圖檔承載不了那麼細的主張」。已記入報告上呈。
    if _Q_CACHE.get("q") is None:
        bad.append("T6 缺 DXF 量化步長 q（_detect_dxf_quantum 回 None）")
        L.append("  T6 🔴 缺 q ⇒ E-6 閘不可定義（禁以硬編值兜底）")
    else:
        _q = float(_Q_CACHE["q"])
        for tag in ("0m", "3.5m"):
            _v = [(float(r["E-6差(m)"]), r["街廓"], r["暫編地號"])
                  for r in rows_by_tag[tag] if r["E-6差(m)"] != "—"]
            _mx = max(_v) if _v else (0.0, "—", "—")
            _ok = _mx[0] <= _q
            L.append(f"  T6[{tag}] E-6 跨層自檢 max|寬度−臨街邊長| = {_mx[0]:.3e}"
                     f"（{_mx[1]}·{_mx[2]}）≤ DXF 量化步長 q={_q:.0e}"
                     f"（{len(_v)} 宗）  {'✅' if _ok else '🔴'}")
            if not _ok:
                bad.append(f"T6[{tag}] {_mx[0]:.3e} > q={_q:.0e} @ {_mx[1]}·{_mx[2]}")

    # T7 **K-4 機器閘**（KL 裁 2026-07-27·取代舊 E-7 待判框架）
    #    ① 街角 winner 皆 `G ≥ 街角最小分配面積`（K-4 之實質檢驗）
    #    ② 無任何筆以已作廢之 `待判（截角）` 態自 `merge_subparcels_by_parent` 產出
    #    ③ **鑑別力**：刻意把一筆街角 winner 之 G 壓到門檻下 ⇒ ① 必須抓到（否則 ① 空真）
    for tag in ("0m", "3.5m"):
        _m = _MERGE_CACHE.get(tag) or {}
        _nk4, _nc = _m.get("n_k4", -1), _m.get("n_corner", -2)
        _viol = _m.get("viol") or []
        _ok1 = (_nk4 == _nc) and not _viol
        L.append(f"  T7①[{tag}] 街角 winner {_nc} 筆全數以 K-4 面積門檻判定"
                 f"（K-4 態 {_nk4} 筆）且 G ≥ 門檻  {'✅' if _ok1 else '🔴'}")
        for _v in _viol[:5]:
            L.append(f"        🔴 {_v}")
        if _m.get("no_thr"):
            L.append(f"        ⚠️ 門檻取不到 {len(_m['no_thr'])} 筆：{_m['no_thr'][:5]}")
        if not _ok1:
            bad.append(f"T7①[{tag}] K-4 態 {_nk4} vs 街角 {_nc}／違例 {_viol[:3]}")
        _leak = _m.get("leak") or []
        _ok2 = not _leak
        L.append(f"  T7②[{tag}] 無已作廢之 `待判（截角）` 態產出"
                 f"（合併後 {_m.get('n_merged', 0)} 列）  {'✅' if _ok2 else '🔴 ' + str(_leak[:5])}")
        if not _ok2:
            bad.append(f"T7②[{tag}] PENDING 殘留：{_leak[:5]}")
        _d = _m.get("disc")
        _ok3 = bool(_d and _d[2])
        L.append(f"  T7③[{tag}] **鑑別力**：壓 {(_d[0] if _d else '—')} 之 G 至 "
                 f"{(_d[1] if _d else '—')}（門檻下）⇒ ① 有抓到"
                 f"  {'✅' if _ok3 else '🔴（① 為空真）'}")
        if not _ok3:
            bad.append(f"T7③[{tag}] 壓 G 後 ① 未咬 ⇒ 零鑑別力")

    # T5 凸性：可達形狀集合①②③全為凸多邊形（KL 裁）⇒ 凸性Δ ≤ 法定粒度 0.01㎡
    #    出處：KL 之可達形狀集合封閉性。此條斷言「資料滿足該前提」＝ E-8a 之立閘依據。
    for tag in ("0m", "3.5m"):
        _mx = max((float(r["凸性Δ(㎡)"]) for r in rows_by_tag[tag]), default=0.0)
        _ok = _mx <= EPS_CONVEX
        L.append(f"  T5[{tag}] max 凸性Δ = {_mx:.6f}㎡ ≤ {EPS_CONVEX}㎡"
                 f"（可達形狀集合全凸）  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T5[{tag}] 凸性Δ {_mx:.6f} > {EPS_CONVEX}")
    return bad


def _read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _write_csv(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)


def _diff(got, exp, tag):
    """逐格 diff（鍵＝街廓＋暫編地號）。回違例字串列。"""
    v = []
    gk = {(r["街廓"], r["暫編地號"]): r for r in got}
    ek = {(r["街廓"], r["暫編地號"]): r for r in exp}
    for k in sorted(set(ek) - set(gk)):
        v.append(f"[{tag}] 快照有而實跑無：{k}")
    for k in sorted(set(gk) - set(ek)):
        v.append(f"[{tag}] 實跑有而快照無：{k}")
    for k in sorted(set(gk) & set(ek)):
        for c in COLS:
            if str(gk[k].get(c, "")) != str(ek[k].get(c, "")):
                v.append(f"[{tag}] {k[0]}·{k[1]} 欄「{c}」：快照 {ek[k].get(c)!r} → 實跑 {gk[k].get(c)!r}")
    return v


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    bake = "--bake" in sys.argv
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 112)
    L.append("【E 系列實測快照】E-1′ min t／E-2′ max t／E-8a 凸性Δ／E-7 街角待判（兩情境·逐宗）")
    L.append("=" * 112)

    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    _SNAP_CACHE.update(snapshot)
    ns, fake_st = harvest()
    width_fn = ns.get("parcel_min_width_n14")
    if not callable(width_fn):
        _fail("harvest 未取得 parcel_min_width_n14")
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    front_lines = cad.get("front_lines") or {}
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6_raw = f.read()
    _Q_CACHE["q"] = ns["_detect_dxf_quantum"](v6_raw)      # T6 閘寬（逐檔實測）
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6_raw, list(cb_by.values()), snapshot)

    rows_by_tag, viol = {}, []
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        # 法定最小深＝N-14 量測帶之上界（per-block·來自參數表·禁硬編 14）
        _md_by = {}
        for p in params:
            _md_by[str(p["街廓"])] = float(p.get("法定最小深(m)", 0) or 0)
        if not all(v > 0 for v in _md_by.values()):
            _fail(f"[{tag}] 法定最小深缺／≤0：{_md_by}")
        diag, sel, off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build_parcels, winners_state, forced_map, setback)
        rows = _measure(sg["g_rows"], front_lines, _md_by, width_fn, tag)
        rows_by_tag[tag] = rows
        _mw_by = {}
        for p in params:
            _mw_by[str(p["街廓"])] = float(p.get("法定最小寬(m)", 0) or 0)
        _MERGE_CACHE[tag] = _e7_merge_gate(
            ns, sg["g_rows"], front_lines, _md_by, _mw_by,
            rv.wf_f0_mina(ns, snapshot, cb_by),
            fake_st.session_state.get("f3_corner_range_areas", {}) or {})
        _got = os.path.join(OUTDIR, SNAP_NAME.format(tag=tag))
        _write_csv(_got, rows)
        _n_corner = sum(1 for r in rows if r["街角地"] == "是")
        L.append("")
        L.append(f"【{tag}】{len(rows)} 宗（街角 {_n_corner}／非街角 {len(rows) - _n_corner}）"
                 f"→ {os.path.relpath(_got, REPO)}")
        L.append("-" * 112)
        L.append(f"  {'街廓':5}{'暫編地號':>14}{'角':>3}{'min_t':>13}{'max_t':>10}"
                 f"{'凸性Δ':>10}{'寬度':>10}{'臨街邊長':>10}{'E-6差':>11}  判定")
        for r in rows:
            L.append(f"  {r['街廓']:5}{r['暫編地號']:>14}{r['街角地']:>3}"
                     f"{r['min_t']:>13}{r['max_t']:>10}{r['凸性Δ(㎡)']:>10}"
                     f"{r['寬度(m)']:>10}{r['臨街邊長(m)']:>10}{r['E-6差(m)']:>11}"
                     f"  {r['判定']}")
        _exp_p = os.path.join(BASEDIR, SNAP_NAME.format(tag=tag))
        if bake:
            _write_csv(_exp_p, rows)
            L.append(f"  🍞 已重烤快照 → {os.path.relpath(_exp_p, REPO)}")
        elif not os.path.exists(_exp_p):
            viol.append(f"[{tag}] 快照不存在：{os.path.relpath(_exp_p, REPO)}"
                        f"（首次請跑 --bake）")
        else:
            viol.extend(_diff(rows, _read_csv(_exp_p), tag))

    viol.extend(_truth_assertions(rows_by_tag, L))

    L.append("")
    L.append("-" * 112)
    if viol:
        L.append(f"RESULT: FAIL（{len(viol)} 違例）")
        for x in viol[:30]:
            L.append("  " + x)
    else:
        L.append("RESULT: PASS（快照逐格全等 ＋ T1–T7 獨立真值斷言全綠）")
    L.append("=" * 112)
    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    return 1 if viol else 0


if __name__ == "__main__":
    sys.exit(main())
