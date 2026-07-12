# -*- coding: utf-8 -*-
"""W-G G.2 smoke（截圖證據）：headless 跑 app `_build_wf_ctx`→wf_f0→f4，
以 harvested app 視覺 builder（純呈現、只讀引擎曝出幾何）產每代＋4 專題 PNG
入 docs/reports/g2_png/（回報新制：截圖即證據）。kaleido 失敗→列印警告走備援（不卡波）。
用法：python verify/wg_g2_smoke.py    退出 0＝全部 PNG 產出。"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from app_harvest import harvest                                   # noqa: E402
import run_verification as rv                                     # noqa: E402
from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk  # noqa: E402
from stepg_pipeline import run_step_g                             # noqa: E402
import wf_f0, wf_f1, wf_f2, wf_f3, wf_f4                          # noqa: E402
from wg_g1_smoke import _reconstruct_sb_rows                      # noqa: E402（同 G.1 smoke 重建法）

OUTPNG = os.path.join(REPO, "docs", "reports", "g2_png")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    os.makedirs(OUTPNG, exist_ok=True)
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    setback, tag = 0.0, "0m"
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    _d, _s, _o, winners_state, forced_map = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback)
    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                    params, build, winners_state, forced_map, setback)

    seed = dict(fake_st.session_state)
    seed.update({
        "f3_G_values": sg["g_rows"], "f3_classified_blocks": list(cb_by.values()),
        "f3_temp_parcels": temp, "f3_build_parcels": build,
        "f3_wd2_pool_diag": sg["pool_diag"], "f3L_setback_default": setback,
        "f3_sb_rows": _reconstruct_sb_rows(ns, cad, snapshot),
        "f3_cad_front_lengths": cad["front_lengths"],
        "f3_cad_side_lengths_by_side": cad["side_lengths_by_side"],
        "f3_cad_front_lines": cad["front_lines"],
        "f3_cad_side_lines_by_side": cad.get("side_lines_by_side", {}),
        "f3_cad_alloc_dir": cad.get("alloc_dir_by_block", {}),
        "f3_manual_road_centerlines": cad.get("centerlines", {}),
    })
    ctx = ns["_build_wf_ctx"](seed, tag, ns["__file__"])
    cbt = {tag: ctx}
    f0 = wf_f0.compute(cbt)
    f1 = wf_f1.compute(cbt, f0)
    f2 = wf_f2.compute(cbt, f0)
    f3 = wf_f3.compute(cbt, f2)
    f4 = wf_f4.compute(cbt, f0, f2, f3)
    print("… 引擎全鏈跑通，開始出圖（純呈現：只讀曝出幾何）")

    e_resh = {}
    for blk_p in (f4[tag].get("reshape_polys") or {}).values():
        e_resh.update(blk_p)
    gens = {
        "v3": dict(rows=ctx["gA"], title="v3 配地基準"),
        "f0": dict(rows=f0[tag]["sgB_rows"], title="f0 同街廓合併＋梯3釋池"),
        "f1": dict(rows=f0[tag]["sgB_rows"], reshape_polys=f1[tag]["reshape_polys"],
                   wedge_coords=f1[tag]["wedge_coords"], compare_mode=True,
                   title="f1 R1楔形整形"),
        "f2": dict(rows=f2[tag]["sgC_rows"], title="f2 跨街廓a′"),
        "f3": dict(rows=f3[tag]["sgD_rows"], title="f3 公設調配"),
        "E":  dict(rows=f4[tag]["sgE_rows"], reshape_polys=e_resh,
                   title="E 終態（7-5最佳化＋終態整形）"),
    }
    figs = {}
    for k, v in gens.items():
        figs[k] = ns["_wg_gen_figure"](
            v["rows"], ctx["cb_by"],
            reshape_polys=v.get("reshape_polys"), wedge_coords=v.get("wedge_coords"),
            title=v["title"], compare_mode=v.get("compare_mode", False))
    omap = ctx["omap"]
    figs["theme_pool_flow"] = ns["_wg_theme_pool_flow"](
        f4[tag]["pool_rows"], f4[tag]["conv_rows"], ctx["cb_by"], "池流向")
    figs["theme_exit"] = ns["_wg_theme_exit"](
        f4[tag]["sgE_rows"], f4[tag]["exit_rows"], ctx["cb_by"], omap, "7-5 雙出口（旗標）")
    figs["theme_reshape"] = ns["_wg_gen_figure"](
        f0[tag]["sgB_rows"], ctx["cb_by"], reshape_polys=f1[tag]["reshape_polys"],
        wedge_coords=f1[tag]["wedge_coords"], title="碎片與整形（前後對照）", compare_mode=True)
    figs["theme_ledger"] = ns["_wg_theme_ledger"](
        f4[tag]["sgE_rows"], f4[tag]["ledger_rows"], ctx["cb_by"], omap, "33 群總決算")

    n_ok = 0
    for name, fig in figs.items():
        path = os.path.join(OUTPNG, f"{name}.png")
        try:
            fig.write_image(path, width=760, height=560, scale=1)
            n_ok += 1
            print(f"  ✅ {name}.png")
        except Exception as e:
            print(f"  ⚠️ {name}.png 匯出失敗（kaleido 備援待補）：{e}")
    print(f"{'✅ SMOKE PASS' if n_ok == len(figs) else '⚠️ 部分匯出'}：{n_ok}/{len(figs)} PNG → {OUTPNG}")
    return 0 if n_ok == len(figs) else 2


if __name__ == "__main__":
    sys.exit(main())
