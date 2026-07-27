# -*- coding: utf-8 -*-
"""W-G.5 裁定 N — **E 系列實測快照**（E-1′／E-2′／E-7／E-8·逐宗·兩情境）。

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
EPS_CONVEX = 0.01       # 法定粒度（面積 2dp）——E-8a 判準寬

_SNAP_CACHE = {}        # 案例快照（T4 之 SIDE_LINE 側數由此導出·非寫死）
_Q_CACHE = {}           # DXF 實測坐標量化步長 q（T6 之閘寬·逐檔實測·禁硬編）
_MERGE_CACHE = {}       # T7：步驟 J 判定 → merge_subparcels_by_parent 之真跑結果


def _e7_merge_gate(ns, g_rows, front_lines, min_depth_by_blk, min_width_by_blk, mina_by_blk):
    """T7 之實料：以 **module 級真判定** 逐宗評 ＋ 真跑 `merge_subparcels_by_parent`。

    ⚠️ **不改引擎狀態**：`g_rows` 先 deepcopy（探針零注入）。
    """
    import copy as _cp
    _rows = _cp.deepcopy(g_rows)
    _ev = ns["evaluate_parcel_width_n14"]
    _pending = set()
    for r in _rows:
        _blk = str(r.get("所屬街廓", ""))
        r.update(_ev(r, (front_lines or {}).get(_blk) or {},
                     float(min_depth_by_blk.get(_blk, 0.0) or 0.0),
                     float(min_width_by_blk.get(_blk, 0.0) or 0.0),
                     _label=f"{_blk}·{r.get('暫編地號')}"))
        if r.get("寬度判定") == ns["WIDTH_VERDICT_PENDING"]:
            _pending.add(str(r.get("暫編地號")))
    _merged = ns["merge_subparcels_by_parent"](_rows, mina_by_blk)["merged_rows"]
    # 洩漏 ＝ pending 筆卻輸出乾淨 `✅`（無「待判」字樣）＝「寬度合格」之結論
    _leak = [str(m.get("暫編地號")) for m in _merged
             if str(m.get("暫編地號")) in _pending
             and str(m.get("是否達最小", "")).startswith("✅")
             and ns["WIDTH_VERDICT_PENDING"] not in str(m.get("是否達最小", ""))]
    # 🔒 **鑑別力**：pending 筆須**真的走到 `✅` 分支**（帶待判標記），否則本閘空真
    #    （＝夾具之(乙)死碼形：閘綠只因該路徑從未被踩到）。
    _marked = [str(m.get("暫編地號")) for m in _merged
               if str(m.get("暫編地號")) in _pending
               and ns["WIDTH_VERDICT_PENDING"] in str(m.get("是否達最小", ""))]
    return {"n_pending": len(_pending),
            "n_corner": sum(1 for r in g_rows if str(r.get("街角地", "")).strip() == "是"),
            "n_merged": len(_merged), "clean_ok_pending": _leak,
            "n_marked": len(_marked)}


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
            # E-7：街角宗之 `cut_coords` 為**截角後**幾何 ⇒ 量出之值非 N-14 所指
            #      ⇒ **不量、不輸出寬度結論**（俟 K-2(Ⅲ) 分家後接上）。
            w_s, verdict, e6 = "—", "街角·E-7待判（截角）", "—"
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
            "min_t": f"{t_min:.3e}", "max_t": f"{t_max:.4f}",
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

    # T7 **E-7 顯性未決態機器閘**（claude.ai BLOCKED-1 (b)）
    #    ① `待判（截角）` 筆數 == 街角 winner 筆數
    #    ② **無 pending 筆以「寬度合格」身分自 `merge_subparcels_by_parent` 產出**
    #       （即：其 `是否達最小` 欄不得為乾淨之 `✅`）
    #    ⚠️ 本閘之所以能跑，係因判定邏輯已抽為 module 級 `evaluate_parcel_width_n14`
    #       ——留在 Tab body 內則 headless 不可測、只能寫成 AST／prose gate（N0-17-b 之忌）。
    for tag in ("0m", "3.5m"):
        _mrg = _MERGE_CACHE.get(tag) or {}
        _n_pend, _n_corner = _mrg.get("n_pending", -1), _mrg.get("n_corner", -2)
        _ok = (_n_pend == _n_corner)
        L.append(f"  T7①[{tag}] 待判筆數 {_n_pend} == 街角 winner 筆數 {_n_corner}"
                 f"  {'✅' if _ok else '🔴'}")
        if not _ok:
            bad.append(f"T7①[{tag}] 待判 {_n_pend} ≠ 街角 {_n_corner}")
        _leak = _mrg.get("clean_ok_pending") or []
        _ok2 = not _leak
        L.append(f"  T7②[{tag}] 無 pending 筆以「寬度合格」身分產出"
                 f"（合併後 {_mrg.get('n_merged', 0)} 列）"
                 f"  {'✅' if _ok2 else '🔴 洩漏 ' + str(_leak[:5])}")
        if not _ok2:
            bad.append(f"T7②[{tag}] pending 以 ✅ 產出：{_leak[:5]}")
        _nm = _mrg.get("n_marked", 0)
        _ok3 = _nm > 0
        L.append(f"  T7③[{tag}] **鑑別力**：{_nm} 筆 pending 真的走到 `✅` 分支"
                 f"並帶待判標記（0 ⇒ T7② 空真）  {'✅' if _ok3 else '🔴'}")
        if not _ok3:
            bad.append(f"T7③[{tag}] 無 pending 筆走到 ✅ 分支 ⇒ T7② 空真、零鑑別力")

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
            rv.wf_f0_mina(ns, snapshot, cb_by))
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
