# -*- coding: utf-8 -*-
"""W-G Y 波 dump 對拍工具 — sub-cent 分岔點定位器。

用途：對拍 KL localhost 之 `st.session_state['f3_G_values']` dump（步驟 G 完成後即刻·
Patch B-2 尚未加工）與 harness native pipeline（`run_step_g`）產出之 g_rows，
逐列（by 暫編地號）逐欄 diff，顯性化 sub-cent 分岔點。

輸入（KL 提供·copy 至 verify/out/y_dump/）：
  - f3_G_values_退縮0m_livedump.json
  - f3_G_values_退縮3.5m_livedump.json

harness 側：走 selection_pipeline + stepg_pipeline（與 run_verification/wg_g3
同源），依 case_params_UC9898.json + V6.dxf + 匿名 xlsx 產出 g_rows。

輸出（verify/out/y_dump/）：
  - y_dump_diff_退縮{0m|3.5m}.csv    逐格差異（key=暫編地號·col=欄名）
  - y_dump_diff_摘要.md              分類統計＋top-N 顯著差異

分類（KL 交辦順序·失敗考古 #17 對稱）：
  ① 迭代次數/收斂路徑異        ← 最可疑（sub-cent 於 solve_G_binary tol）
  ② area_geom 差異             ← shapely/幾何精度
  ③ Patch B-2 改寫 G           ← 步驟 J 加工（本 dump 位置尚未觸發·純基準）
  ④ ghost 列                   ← app 不排 harness 排（Y.0 改點·預期差異）
  ⑤ 其他欄差異                 ← A 地價比／Rw／G／S 等

用法（cwd=repo root）：python verify/tools/y_dump_diff.py
退出 0＝跑完（無論 diff 多少·僅診斷用）。
"""
import os
import sys
import json
import csv
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                  # noqa: E402
import run_verification as rv                                    # noqa: E402
from selection_pipeline import (                                 # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g, compute_total_burden_rate  # noqa: E402

Y_OUT = os.path.join(VERIFY, "out", "y_dump")


def _load_live(tag):
    """讀 KL 提供之 live dump JSON。"""
    p = os.path.join(Y_OUT, f"f3_G_values_退縮{tag}_livedump.json")
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _run_harness(tag, setback, snap, ns, fake_st, cb_by, cad, temp, build):
    """跑 harness native step G · 產 g_rows（依 run_verification 之流程）。"""
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snap, setback)
    _dv, _sv, _od, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback)
    # 補鋪 f3_total_burden_rate_from_finance（stepg L169-176 loud gate）
    _rate, _ = compute_total_burden_rate(ns, list(cb_by.values()), snap)
    fake_st.session_state["f3_total_burden_rate_from_finance"] = float(_rate)
    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snap,
                    params, build, winners, forced, setback)
    return sg["g_rows"]


# 可容忍 float 抖動；欄之絕對容差（低於此不視為差異，僅列於「輕微抖動」統計）
FLOAT_TOL = {
    "A 地價比": 5e-4,
    "G(㎡)": 0.011,       # 2dp 顯示層抖動
    "幾何面積(㎡)": 0.011,
    "S(m)": 0.011,
    "W(m)": 0.011,
    "Rw(%)": 0.011,
    "宗地寬度(m)": 0.011,
    "累積S(m)": 0.011,
    "負擔比率": 5e-4,
    "F(m)": 0.011,
    "l₁ 側面尺度": 0.011,
    "l₂ 正面尺度": 0.011,
    "平均深度(m)": 0.011,
    "正面長度(m)": 0.011,
    "街廓面積(㎡)": 0.011,
    "a 面積(㎡)": 0.011,
    "迭代次數": 0,        # 整數·嚴格比對
}
NUMERIC_COLS = set(FLOAT_TOL.keys())
# Patch B-2 加欄（本 dump 不出現·若出現需另處理）
PATCH_B2_COLS = {"_below_min_width", "_width_violation_note",
                 "實際寬度(m)", "_G_before_width_violation"}
# 對拍主鍵
KEY = "暫編地號"
# 幾何欄（純視覺·CSV 中列數/座標抖動不視為 sub-cent 分岔·單獨統計）
GEOMETRY_COLS = {"cut_coords"}
# 分類鍵
CAT_ITER = "①迭代/收斂"
CAT_AREA = "②area_geom"
CAT_B2 = "③Patch B-2"
CAT_GHOST = "④ghost"
CAT_OTHER = "⑤其他"


def _classify(col, live_val, harn_val, is_ghost):
    """欄名 → 分類。"""
    if is_ghost:
        return CAT_GHOST
    if col in PATCH_B2_COLS:
        return CAT_B2
    if col in ("迭代次數", "是否收斂"):
        return CAT_ITER
    if col in ("幾何面積(㎡)", "area_geom"):
        return CAT_AREA
    return CAT_OTHER


def _norm_val(v):
    """欄值歸一：strip、None→''、bool→str。"""
    if v is None:
        return ""
    if isinstance(v, bool):
        return str(v)
    if isinstance(v, str):
        return v.strip()
    return v


def _diff_val(col, live_v, harn_v):
    """回傳 (differ, absdiff or None)。"""
    lv, hv = _norm_val(live_v), _norm_val(harn_v)
    if col in NUMERIC_COLS:
        try:
            f_lv = float(lv) if lv != "" else None
            f_hv = float(hv) if hv != "" else None
        except (TypeError, ValueError):
            return (lv != hv, None)
        if f_lv is None and f_hv is None:
            return (False, 0.0)
        if f_lv is None or f_hv is None:
            return (True, None)
        d = abs(f_lv - f_hv)
        tol = FLOAT_TOL.get(col, 1e-9)
        return (d > tol, d)
    # 非數值欄
    return (lv != hv, None)


def _diff_scenario(tag, live_rows, harn_rows):
    """單情境 diff。回傳 (row_diffs, only_live_keys, only_harn_keys, summary)。"""
    live_by = {r[KEY]: r for r in live_rows}
    harn_by = {r[KEY]: r for r in harn_rows}
    common = sorted(set(live_by) & set(harn_by))
    only_live = sorted(set(live_by) - set(harn_by))
    only_harn = sorted(set(harn_by) - set(live_by))

    row_diffs = []            # [{key, col, live, harn, absdiff, cat, is_ghost}]
    per_col_stats = defaultdict(lambda: {"n_differ": 0, "max_absdiff": 0.0,
                                          "cat": CAT_OTHER})
    per_cat_count = defaultdict(int)

    for k in common:
        lr, hr = live_by[k], harn_by[k]
        is_ghost = bool(lr.get("_is_ghost_sliver") or "_GHOST" in str(k)
                        or hr.get("_is_ghost_sliver"))
        cols = set(lr.keys()) | set(hr.keys())
        for c in cols:
            if c in GEOMETRY_COLS:
                continue
            differ, absdiff = _diff_val(c, lr.get(c), hr.get(c))
            if differ:
                cat = _classify(c, lr.get(c), hr.get(c), is_ghost)
                row_diffs.append({
                    "情境": tag, "暫編地號": k, "欄": c,
                    "live": _norm_val(lr.get(c)),
                    "harness": _norm_val(hr.get(c)),
                    "absdiff": (f"{absdiff:.6g}" if absdiff is not None else ""),
                    "分類": cat,
                    "ghost": ("是" if is_ghost else "否"),
                    "所屬街廓": lr.get("所屬街廓", ""),
                    "推進側別": lr.get("推進側別", ""),
                })
                per_col_stats[c]["n_differ"] += 1
                if absdiff is not None:
                    per_col_stats[c]["max_absdiff"] = max(
                        per_col_stats[c]["max_absdiff"], absdiff)
                per_col_stats[c]["cat"] = cat
                per_cat_count[cat] += 1

    summary = {
        "tag": tag,
        "n_live": len(live_by),
        "n_harn": len(harn_by),
        "n_common": len(common),
        "n_only_live": len(only_live),
        "n_only_harn": len(only_harn),
        "only_live_keys": only_live,
        "only_harn_keys": only_harn,
        "n_row_diffs": len(row_diffs),
        "per_col": dict(per_col_stats),
        "per_cat": dict(per_cat_count),
    }
    return row_diffs, summary


def _write_diff_csv(tag, row_diffs):
    p = os.path.join(Y_OUT, f"y_dump_diff_退縮{tag}.csv")
    cols = ["情境", "所屬街廓", "推進側別", "暫編地號", "ghost",
            "分類", "欄", "live", "harness", "absdiff"]
    with open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        for r in row_diffs:
            w.writerow({c: r.get(c, "") for c in cols})
    return p


def _write_summary_md(summaries):
    p = os.path.join(Y_OUT, "y_dump_diff_摘要.md")
    lines = ["# W-G Y 波 dump 對拍摘要（sub-cent 定位器）",
             "",
             f"- 產出：{os.path.relpath(p, REPO)}",
             f"- 工具：`verify/tools/y_dump_diff.py`",
             f"- Live 種子：`verify/out/y_dump/f3_G_values_退縮{{0m|3.5m}}_livedump.json`（KL localhost dump·步驟 G 完成後·Patch B-2 尚未觸發）",
             f"- Harness 種子：`case_params_UC9898.json` + `V6.dxf` + `地籍資料來源_匿名版.xlsx` → `run_step_g`",
             ""]
    for s in summaries:
        tag = s["tag"]
        lines += [f"## 退縮 {tag}",
                  "",
                  f"- 列數：live={s['n_live']} / harness={s['n_harn']} / 交集={s['n_common']}",
                  f"- 僅 live 有（app 端獨有·多為 ghost）：{s['n_only_live']}",
                  f"- 僅 harness 有（若非 0 屬異常）：{s['n_only_harn']}",
                  f"- 總欄差異數（列 × 欄）：**{s['n_row_diffs']}**",
                  ""]
        if s["only_live_keys"]:
            lines += ["**僅 live 有之列**："]
            lines += [f"  - {k}" for k in s["only_live_keys"][:20]]
            if len(s["only_live_keys"]) > 20:
                lines += [f"  - ...（另 {len(s['only_live_keys']) - 20} 筆）"]
            lines += [""]
        if s["only_harn_keys"]:
            lines += ["**⚠️ 僅 harness 有之列（不預期·調查）**："]
            lines += [f"  - {k}" for k in s["only_harn_keys"][:20]]
            lines += [""]
        lines += ["**分類統計**：", ""]
        for cat in (CAT_ITER, CAT_AREA, CAT_B2, CAT_GHOST, CAT_OTHER):
            n = s["per_cat"].get(cat, 0)
            lines += [f"- {cat}：{n} 欄差異"]
        lines += [""]
        # per-col top
        cols_sorted = sorted(s["per_col"].items(),
                              key=lambda kv: (-kv[1]["n_differ"], kv[0]))
        lines += ["**欄別 top 差異**：", "",
                  "| 欄 | 分類 | 差異列數 | max abs diff |",
                  "|---|---|---|---|"]
        for c, st in cols_sorted[:15]:
            mad = st["max_absdiff"]
            mad_s = (f"{mad:.4g}" if mad > 0 else "-")
            lines += [f"| {c} | {st['cat']} | {st['n_differ']} | {mad_s} |"]
        lines += [""]
    lines += ["## 判讀重點（Y 波 sub-cent 靶）",
              "",
              "① **迭代/收斂 差異 > 0**：solve_G_binary tol=0.01 之收斂路徑於 live vs harness 分岔；重點查 fake_st vs 真 st 差、B/C 精度差、W_prev thread 差；",
              "② **area_geom 差異 > 0**：shapely `buffer(0)` 版本／`_res['area_geom'] = round(S × avg_depth, 2)` 之來源差；",
              "③ **A 地價比整體性偏移**（若集中在特定歸戶）：post_price/pre_price 快照 vs live 分岔（非 sub-cent·屬財務同源性問題）；",
              "④ **ghost 列 only-live**：預期（Y.0 拿掉 stepg L228-232 後對齊）；",
              "⑤ **其他 sub-cent**：逐欄查 tol/round 鏈條。",
              ""]
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return p


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if not os.path.isdir(Y_OUT):
        raise SystemExit(f"🔴 {Y_OUT} 不存在（KL live dump 未 copy 到位）")
    # harness 一次 bootstrap
    with open(rv.SNAPSHOT, encoding="utf-8") as f:
        snap = json.load(f)
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snap)

    summaries = []
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        print(f"… 跑 harness step G（退縮 {tag}）")
        harn_rows = _run_harness(tag, setback, snap, ns, fake_st,
                                  cb_by, cad, temp, build)
        print(f"   harness rows: {len(harn_rows)}")
        live_rows = _load_live(tag)
        print(f"   live rows:    {len(live_rows)}")
        diffs, summary = _diff_scenario(tag, live_rows, harn_rows)
        print(f"   差異數（列×欄）: {summary['n_row_diffs']}")
        p_csv = _write_diff_csv(tag, diffs)
        print(f"   → {os.path.relpath(p_csv, REPO)}")
        summaries.append(summary)

    p_md = _write_summary_md(summaries)
    print(f"→ 摘要：{os.path.relpath(p_md, REPO)}")
    # 打印分類簡表
    print("=" * 64)
    for s in summaries:
        cats = s["per_cat"]
        print(f"退縮 {s['tag']}：{s['n_row_diffs']} 欄差異  "
              f"[①{cats.get(CAT_ITER, 0)}] "
              f"[②{cats.get(CAT_AREA, 0)}] "
              f"[③{cats.get(CAT_B2, 0)}] "
              f"[④{cats.get(CAT_GHOST, 0)}] "
              f"[⑤{cats.get(CAT_OTHER, 0)}]  "
              f"only-live={s['n_only_live']} only-harn={s['n_only_harn']}")
    print("=" * 64)
    print("Y 波 dump diff：完成（純診斷·退出 0）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
