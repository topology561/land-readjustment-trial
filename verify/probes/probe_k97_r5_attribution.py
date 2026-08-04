# -*- coding: utf-8 -*-
r"""K-6-A2 段三(c)-2 §二：**R5 未動之歸因量測**（只量不判·⛔ 禁以推論代替量測）。

## 問題

`R5/left` 之街角規定面積 `378.47 → 371.17`（**−7.30㎡·八格最大**），
為何 **`G007@R5` 之 `G(Σa)` 未破錨**？（破錨者僅 `G010@R2`，該側僅 `+1.30㎡`。）

## 量測（施工單 §二 四項）

1. **六 gid 之 `G(Σa)`**（新舊各一組）
   🔴 **粒度上限＝`0.01`**：`G(㎡)` 於來源即 `round(..., 2)`
   （`grep -n "'G(㎡)': round" verify/stepg_pipeline.py`）⇒ **本欄無法解析到 0.01 以下**，
   施工單所稱之「全精度·不捨入」**在此欄不可得**；`|Δ| < 0.005` 之判別**只能表述為
   「2dp 下為 0」**、不能斷言「真值未變」。
   ⚠️ **錨檢為嚴格不等式** `abs(G - exp) > 0.01`
   （`grep -n "abs(G - exp) > 0.01" verify/wf_f0.py`）⇒ **`Δ` 恰為 `0.01` 者「不」破錨**。
2. **三 forced 側之池帶 `s 寬`**（新舊）——前次重錨之機制驅動量係 **`s 寬`**、非面積。
3. `G007` 標的宗 **`628-20(2)`** 在 R5 之 **`s` 序位**（在抵費地帶之前或之後）。
4. 三側之 `W`／`Rw`／負擔比率 新舊對照。

## 手法

- **舊**輪＝以 `_t_override` 注入 `t_star_legacy`（同 `probe_ruling_K9_7_pk_impact`）。
- **錨檢中性化**：行程內把 `wf_f0.GSA_EXPECT` 換成空表 ⇒ 值檢與覆蓋率檢皆不觸發
  （`exp=None` 不比；`set({}) - set(gsa) = ∅` 不 raise）⇒ `compute` 得以跑完、交出真值。
  ⛔ **僅存在於本行程**；`verify/wf_f0.py` **一字未改**。

**rc 恆 0**（只量不判）。輸出 `verify/out/probe_k97_r5_attribution.log`。
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
import wf_f0                                                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_k97_r5_attribution.log")
GIDS = ("G006", "G007", "G009", "G010", "G014", "G017")


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 118)
    L.append("【K-6-A2 段三(c)-2 §二】R5 未動之歸因量測 — 只量不判")
    L.append("問：R5左 範圍面積 −7.30㎡（最大）為何未推動 G007@R5 之 G(Σa)？")
    L.append("錨檢已於行程內中性化（wf_f0.GSA_EXPECT→空表）；verify/wf_f0.py 一字未改")
    L.append("=" * 118)

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    # 舊式 t*（供「舊」輪注入）
    T_OLD = {}
    for setback in (0.0, 3.5):
        for lbl in sorted(cb_by):
            for side in ("left", "right"):
                if side not in (sd_by.get(lbl) or {}):
                    continue
                fl = fl_by.get(lbl) or {}
                if not (fl.get("p1") and fl.get("p2")):
                    continue
                r = ns["k97_solve_alloc_t"](
                    cb_by[lbl].get("centroid"), [fl["p1"], fl["p2"]],
                    ns["_baseline_pts_from_manual"](bl_by.get(lbl),
                                                    cb_by[lbl].get("vertices")),
                    [sd_by[lbl][side]["p1"], sd_by[lbl][side]["p2"]],
                    al_by.get(lbl), setback, legal_w,
                    chamfer_tri=ns["_make_chamfer_tri_wb"](cb_by[lbl], side),
                    block_depth=float(snapshot["blocks"][lbl]["街廓分配深度_m"]),
                    _label=lbl, _side=side)
                T_OLD[(lbl, side, setback)] = r["t_star_legacy"]

    _orig_range = ns["_build_corner_range_v3"]
    STATE = {"setback": None, "use_new": True, "hits": 0}

    def _patched_range(*a, **kw):
        if not STATE["use_new"]:
            key = (kw.get("_label"), kw.get("_side"), STATE["setback"])
            if key in T_OLD and T_OLD[key] is not None:
                kw = dict(kw)
                kw["_t_override"] = T_OLD[key]
                STATE["hits"] += 1
        return _orig_range(*a, **kw)

    ns["_build_corner_range_v3"] = _patched_range
    _orig_gsa = wf_f0.GSA_EXPECT
    wf_f0.GSA_EXPECT = {"0m": {}, "3.5m": {}}     # ← 錨檢中性化（僅本行程）

    def _run(setback, use_new):
        STATE["setback"] = setback
        STATE["use_new"] = use_new
        tag = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _o, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build_parcels, winners, forced, setback)
        # 🔒 ctx 之鍵集**逐字比照** `run_verification` 之組法
        #   （`grep -n '"setback": _c\["sb"\], "gA"' verify/run_verification.py`）
        #   ——⛔ 禁自行揣測鍵集（初版漏 `poolA`／`temp` 即 KeyError）。
        ctx = {tag: {"ns": ns, "fake_st": fake_st, "cb_by": cb_by, "cad": cad,
                     "snap": snapshot,
                     "omap": fake_st.session_state["t8_ownership_map"],
                     "build": build_parcels, "params": params,
                     "winners": winners, "forced": forced, "setback": setback,
                     "gA": sg["g_rows"], "poolA": sg["pool_diag"],
                     "temp": temp_parcels}}
        f0 = wf_f0.compute(ctx)[tag]
        return {"f0": f0, "params": {r["街廓"]: r for r in params},
                "gA": sg["g_rows"], "forced": forced}

    RES = {}
    for setback in (3.5, 0.0):
        RES[(setback, True)] = _run(setback, True)
        RES[(setback, False)] = _run(setback, False)

    ns["_build_corner_range_v3"] = _orig_range
    wf_f0.GSA_EXPECT = _orig_gsa
    L.append(f"舊輪 patch 命中 ＝ {STATE['hits']}（新輪＝生產原樣·零 patch）")

    # ── (1) 六 gid 之 G(Σa) 全精度 ────────────────────────────────────────────
    for setback in (3.5, 0.0):
        tag = f"{setback:g}m"
        new, old = RES[(setback, True)], RES[(setback, False)]
        gn, go = new["f0"].get("gsa", {}), old["f0"].get("gsa", {})
        L.append("")
        L.append(f"【1·{tag}】六 gid 之 G(Σa)（**粒度 0.01**·來源即 round(...,2)）")
        L.append("-" * 118)
        L.append(f"  {'gid':<7}{'舊 G(Σa)':>14}{'新 G(Σa)':>14}{'Δ':>10}"
                 f"{'錨':>10}  判讀（粒度 0.01·錨檢嚴格 >0.01）")
        L.append("-" * 118)
        for g in GIDS:
            a, b = go.get(g), gn.get(g)
            anc = _orig_gsa[tag].get(g)
            if a is None and b is None:
                L.append(f"  {g:<7}{'—（未進 gsa）':>20}{'—（未進 gsa）':>20}"
                         f"{'—':>18}{anc if anc is not None else '—':>10}"
                         f"  ⚠️ **無合併決策 ⇒ 錨從未被評估**")
                continue
            if a is None or b is None:
                L.append(f"  {g:<7}{a if a is not None else '—':>20}"
                         f"{b if b is not None else '—':>20}{'—':>18}"
                         f"{anc if anc is not None else '—':>10}  ⚠️ 單邊缺")
                continue
            d = b - a
            # 🔒 §二 之「Δ=0 ⇒ 停機」判準**只對 G007** 而言（該問即「R5 為何未動」）；
            #   其餘 gid 之 Δ=0 屬預期（其街廓範圍未變）⇒ 不套該判準。
            if abs(d) > 0.01:
                jd = "🔴 逾錨檢容差（嚴格 >0.01）⇒ **破錨**"
            elif abs(d) == 0.0:
                # §二 之問專指 **3.5m**（破錨處）；且 0m 之 R5左 `forced=False`
                #   ⇒ 無抵費地帳、本就不預期受影響 ⇒ 該判準不套 0m。
                jd = ("🔴 **G007@3.5m 於 2dp 下未變 ⇒ 停機上呈**"
                      if (g == "G007" and tag == "3.5m")
                      else "—（2dp 下未變·預期）")
            else:
                jd = (f"⚠️ **Δ={d:+.2f} 恰落容差邊界**（`>0.01` 為 False ⇒ 不破錨）"
                      if abs(abs(d) - 0.01) < 1e-12 else
                      f"有變動 {d:+.2f}（2dp 粒度）")
            L.append(f"  {g:<7}{a:>14.2f}{b:>14.2f}{d:>+10.2f}"
                     f"{anc if anc is not None else '—':>10}  {jd}")
        L.append("-" * 118)
        _cov = sorted(set(_orig_gsa[tag]) - set(gn))
        L.append(f"  ⇒ **新輪未進 `gsa` 之 gid**：{_cov if _cov else '（無）'}")
        _covo = sorted(set(_orig_gsa[tag]) - set(go))
        L.append(f"  ⇒ **舊輪未進 `gsa` 之 gid**：{_covo if _covo else '（無）'}")

    # ── (2)(3)(4) 三 forced 側之池帶／序位／負擔 ──────────────────────────────
    L.append("")
    L.append("【2】三 forced 側之街角規定面積與 forced 狀態（新舊）")
    L.append("-" * 118)
    for setback in (3.5, 0.0):
        new, old = RES[(setback, True)], RES[(setback, False)]
        for lbl, side, zh in (("R2", "left", "左"), ("R5", "left", "左"),
                              ("R3", "right", "右")):
            fo = ((old["forced"] or {}).get(lbl) or {}).get(
                f"{'left' if side == 'left' else 'right'}_forced_offset")
            fn = ((new["forced"] or {}).get(lbl) or {}).get(
                f"{'left' if side == 'left' else 'right'}_forced_offset")
            ao = old["params"][lbl].get(f"【{zh}】街角最小面積(㎡)")
            an = new["params"][lbl].get(f"【{zh}】街角最小面積(㎡)")
            L.append(f"  {setback:g}m {lbl}/{side:<5} 範圍面積 {ao}→{an}"
                     f"（Δ {float(an) - float(ao):+.2f}）｜forced {fo}→{fn}")
    L.append("-" * 118)

    L.append("")
    L.append("【3】G007 標的宗 628-20(2) 於 R5 之 s 序位（相對抵費地宗）")
    L.append("-" * 118)
    for setback in (3.5, 0.0):
        new = RES[(setback, True)]
        rows = [r for r in new["gA"] if str(r.get("所屬街廓")) == "R5"]
        rows.sort(key=lambda r: float(r.get("累積S(m)", 0) or 0))
        L.append(f"  ── {setback:g}m｜R5 依累積S 排序 ──")
        for r in rows:
            pid = str(r.get("暫編地號", ""))
            mark = "  ← G007 標的宗" if pid == "628-20(2)" else (
                "  ← 抵費地" if "抵費地" in pid or r.get("推進側別") == "抵費地" else "")
            L.append(f"     {pid:<16} 累積S={float(r.get('累積S(m)', 0) or 0):>9.4f}"
                     f"  推進側別={r.get('推進側別')}{mark}")
    L.append("-" * 118)

    L.append("")
    L.append("【4】註記")
    L.append("  · 本檔只量不判；判讀欄僅標示落在哪一區間，**不代裁**。")
    L.append("  · 錨檢中性化僅存在於本行程，verify/wf_f0.py 一字未改。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
