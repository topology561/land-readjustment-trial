# -*- coding: utf-8 -*-
"""W-G G.1 smoke（headless 日誌證據）：app `_build_wf_ctx` → wf_f0→f4 全鏈端到端跑通。
複用 harness 建置（禁改 stepg/引擎），組真 app session → 呼叫 harvested `_build_wf_ctx`
→ 依序跑 f0→f4，印終態摘要。**證 app 接線路徑於 UC9898 執行無崩**（catch 如 cad centerlines 之 runtime bug）。
sb rows 由 snapshot blocks＋cad 重建（負擔尺度 C-無關，忠實複現 app live sb 之 尺度；不動 stepg）。
用法：python verify/wg_g1_smoke.py    退出 0＝跑通。"""
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from app_harvest import harvest                                   # noqa: E402
import run_verification as rv                                     # noqa: E402
from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk  # noqa: E402
from stepg_pipeline import run_step_g                             # noqa: E402
import wf_f0, wf_f1, wf_f2, wf_f3, wf_f4                          # noqa: E402


def _reconstruct_sb_rows(ns, cad, snapshot):
    """複刻 stepg road_data（106-129）→ calc_special_burden_total。負擔尺度 C-無關，
    面積用 斷言錨 C（引擎不從 snap.blocks 讀面積）。忠實得 app live sb 之 尺度。"""
    SB = snapshot["blocks"]                      # UC9898：R1-R6 全可建築
    flen = cad.get("front_lengths", {}) or {}
    slbs = cad.get("side_lengths_by_side", {}) or {}
    C = float(snapshot["財務接線_v3"]["斷言錨"]["C"])
    road = []
    for lbl, blk in SB.items():
        sides = slbs.get(lbl, {}) or {}
        road.append({
            "label": lbl,
            "front_width": float(blk["正面"]["路寬_m"]),
            "front_length": float(flen.get(lbl, 0.0) or 0.0),
            "front_new": float(blk["正面"]["負擔尺度_輸入"]) > 0,
            "left_side_width": float(blk["左側"]["路寬_m"]),
            "left_side_length": float(sides.get("left", 0.0) or 0.0),
            "left_side_new": float(blk["左側"]["負擔尺度_輸入"]) > 0,
            "right_side_width": float(blk["右側"]["路寬_m"]),
            "right_side_length": float(sides.get("right", 0.0) or 0.0),
            "right_side_new": float(blk["右側"]["負擔尺度_輸入"]) > 0,
        })
    return ns["calc_special_burden_total"](road, C)["rows"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    setback, tag = 0.0, "0m"
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    _diag, _sel, _off, winners_state, forced_map = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback)
    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                    params, build, winners_state, forced_map, setback)

    ss = fake_st.session_state       # 含 run_step_g 寫入之 f3_corner_winners/f3L_corner_min_table/… ＋ build_ownership 之 t8_*
    seed = dict(ss)
    seed.update({
        "f3_G_values": sg["g_rows"],
        "f3_classified_blocks": list(cb_by.values()),
        "f3_temp_parcels": temp,
        "f3_build_parcels": build,
        "f3_wd2_pool_diag": sg["pool_diag"],
        "f3L_setback_default": setback,
        "f3_sb_rows": _reconstruct_sb_rows(ns, cad, snapshot),
        "f3_cad_front_lengths": cad["front_lengths"],
        "f3_cad_side_lengths_by_side": cad["side_lengths_by_side"],
        "f3_cad_front_lines": cad["front_lines"],
        "f3_cad_side_lines_by_side": cad.get("side_lines_by_side", {}),
        "f3_cad_alloc_dir": cad.get("alloc_dir_by_block", {}),
        "f3_manual_road_centerlines": cad.get("centerlines", {}),
    })

    print(f"… _is_uc9898(seed) = {ns['_is_uc9898'](seed)}")
    ctx = ns["_build_wf_ctx"](seed, tag, ns["__file__"])
    print(f"… _build_wf_ctx OK：cb_by {len(ctx['cb_by'])} 塊、snap.blocks {len(ctx['snap']['blocks'])} 塊、"
          f"cad.centerlines {len(ctx['cad']['centerlines'])}、gA {len(ctx['gA'])} 列、"
          f"β財務源＝快照:{ctx['snap']['財務接線_v3'] is snapshot['財務接線_v3'] or ctx['snap']['財務接線_v3']==snapshot['財務接線_v3']}")

    cbt = {tag: ctx}
    f0 = wf_f0.compute(cbt)
    wf_f1.compute(cbt, f0)
    f2 = wf_f2.compute(cbt, f0)
    f3 = wf_f3.compute(cbt, f2)
    f4 = wf_f4.compute(cbt, f0, f2, f3)
    o = f4[tag]
    print(f"✅ SMOKE PASS：app `_build_wf_ctx` → wf_f0→f4 全鏈跑通（{tag}，無崩）")
    print(f"   7-4三級調配 conv={len(o['conv_rows'])}｜7-5雙出口 exit={len(o['exit_rows'])}｜"
          f"池終態 pool={len(o['pool_rows'])}｜終態整形 reshape={len(o['reshape_rows'])}｜"
          f"33群總決算 ledger={len(o['ledger_rows'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
