# -*- coding: utf-8 -*-
"""W-G G.3 雙路同源終驗（收官王牌）：app 接線路徑（`_build_wf_ctx` → wf_f0→f4）之終態
逐代表，對拍**重烤後 baseline**（v3 勘誤重烤 b288446，正解區段價）——**逐格零 diff ＋ byte-perfect**。

真同源：app-path 之 β 財務 ctx 取自快照 `財務接線_v3`（正解區段價），baseline 亦重烤自同快照
→ 二路皆正解價（非前輪雙路共錯綠）。app-path 唯一異於 native 者＝ctx 由 session_state 經
`_build_wf_ctx` 忠實重組（G.1 +1 gate 已證 ctx 欄同源）；G.3 端到端證**輸出**亦 byte-perfect。

種子＝harness native 管線（禁改 stepg/引擎），組真 app session → harvested `_build_wf_ctx`。
用法：python verify/wg_g3.py    退出 0＝全綠。"""
import os
import sys
import io
import csv
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from app_harvest import harvest                                   # noqa: E402
import run_verification as rv                                     # noqa: E402
from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk  # noqa: E402
from stepg_pipeline import run_step_g                             # noqa: E402
import wf_f0, wf_f1, wf_f2, wf_f3, wf_f4                          # noqa: E402
from wg_g1_smoke import _reconstruct_sb_rows                      # noqa: E402（負擔尺度 C-無關·忠實複現 app live sb）

# 世代 → (baseline 子目錄, 檔名前綴, [(compute 回傳鍵, 表名, key欄)])
GEN_TABLES = [
    ("f0", rv.F0DIR, "F.0", [
        ("g_tab", "G值", ["所屬街廓", "暫編地號"]),
        ("diag_tab", "滑池槽診斷", ["街廓"]),
        ("slot_tab", "逐槽J表", ["街廓", "k"]),
        ("dec_rows", "合併決策", ["情境", "歸戶", "街廓"]),
        ("flag_rows", "旗標消長", ["情境", "暫編地號"]),
        ("pool_rows", "池差", ["情境", "街廓"]),
    ]),
    ("f1", rv.F1DIR, "F.1", [
        ("reshape_rows", "遞補整形", ["情境", "暫編地號"]),
        ("frag_rows", "碎片處置", ["情境", "碎片"]),
        ("pool_rows", "池驗證", ["情境", "街廓", "池片"]),
    ]),
    ("f2", rv.F2DIR, "F.2", [
        ("conv_rows", "跨街廓調配", ["情境", "歸戶", "源宗"]),
        ("g_tab", "G值", ["所屬街廓", "暫編地號"]),
        ("pool_rows", "池流向", ["情境", "街廓"]),
    ]),
    ("f3", rv.F3DIR, "F.3", [
        ("conv_rows", "公設調配", ["情境", "公設筆"]),
        ("to74_rows", "轉7-4", ["情境", "公設筆"]),
        ("g_tab", "G值", ["所屬街廓", "暫編地號"]),
        ("pool_rows", "池流向", ["情境", "街廓"]),
    ]),
    ("f4", rv.F4DIR, "F.4", [
        ("conv_rows", "公設調配", ["情境", "段", "目標宗"]),
        ("exit_rows", "七五雙出口", ["情境", "歸戶"]),
        ("g_tab", "G值", ["所屬街廓", "暫編地號"]),
        ("pool_rows", "池流向", ["情境", "街廓"]),
        ("reshape_rows", "整形", ["情境", "街廓", "暫編地號"]),
        ("ledger_rows", "總決算", ["情境", "歸戶"]),
    ]),
]


def _serialize(rows, base_col_order):
    """以 baseline 欄序序列化 rows 為 CSV bytes（utf-8-sig BOM＋LF，同 _bake_csv）。
    空表 → 0 byte（比照 _bake_csv 空表寫空檔慣例·免與 baseline 空檔 byte 不符；UC9898 無空表）。"""
    if not rows:
        return b""
    got_cols = list(rows[0].keys())
    cols = ([c for c in base_col_order if c in got_cols] +
            [c for c in got_cols if c not in base_col_order]) if base_col_order else got_cols
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue().encode("utf-8-sig")


def _seed_ctx(ns, fake_st, cb_by, cad, snapshot, temp, build, tag, setback):
    """組真 app session_state → harvested `_build_wf_ctx`（複現 live 缺率鍵→證主動鋪底）。"""
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    _d, _s, _o, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback)
    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                    params, build, winners, forced, setback)
    seed = dict(fake_st.session_state)
    seed.pop("f3_total_burden_rate_from_finance", None)      # 複現 live 缺鍵（G.1 補丁：ctx-builder 主動鋪底）
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
    if not ns["_is_uc9898"](seed):
        raise RuntimeError(f"🔴 [{tag}] _is_uc9898(seed) False——指紋誤判本案")
    return ns["_build_wf_ctx"](seed, tag, ns["__file__"])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    results = []       # (name, ok, detail)
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        print(f"… app-path _build_wf_ctx → wf_f0→f4（{tag}）")
        ctx = _seed_ctx(ns, fake_st, cb_by, cad, snapshot, temp, build, tag, setback)
        cbt = {tag: ctx}
        f0 = wf_f0.compute(cbt)
        f1 = wf_f1.compute(cbt, f0)
        f2 = wf_f2.compute(cbt, f0)
        f3 = wf_f3.compute(cbt, f2)
        f4 = wf_f4.compute(cbt, f0, f2, f3)
        gens = {"f0": f0, "f1": f1, "f2": f2, "f3": f3, "f4": f4}
        for gkey, bdir, prefix, tabs in GEN_TABLES:
            d = gens[gkey][tag]
            for rkey, nm, kcols in tabs:
                rows = d[rkey]
                bpath = os.path.join(bdir, f"{prefix}_{nm}_退縮{tag}.csv")
                # 逐格（diff_rows·2dp 容差·key 對齊）
                ok_cell, viol = rv.diff_rows(rows, bpath, kcols, f"G.3·{prefix}{nm}{tag}")
                # byte-perfect（LF 正規化內容·免 autocrlf 假象）
                base_bytes = open(bpath, "rb").read().replace(b"\r\n", b"\n")
                base_cols = list(rv._read_csv(bpath)[0].keys()) if rv._read_csv(bpath) else []
                got_bytes = _serialize(rows, base_cols)
                ok_byte = (got_bytes == base_bytes)
                ok = ok_cell and ok_byte
                det = []
                if not ok_cell:
                    det += viol[:6]
                if not ok_byte and ok_cell:
                    det.append(f"逐格全等但 byte 異（欄序/格式）：got {len(got_bytes)}B vs base {len(base_bytes)}B")
                results.append((f"{prefix}_{nm}_{tag}", ok, det))

    # 圍欄 headless proxy：快照段價＝正解（勘誤後）·A 逐宗吃之（live 圍欄視覺留 localhost）
    z = snapshot["財務接線_v3"]["重劃前區段_面積單價"]
    ok_a = abs(float(z["a"]["單價_元每m2"]) - 43909.2308486259) < 1e-9
    ok_b = abs(float(z["b"]["單價_元每m2"]) - 37322.846221332016) < 1e-9
    results.append(("圍欄段價快照＝正解（a=43909.23·b=37322.85·勘誤後）", ok_a and ok_b,
                    [] if ok_a and ok_b else [f"a={z['a']['單價_元每m2']} b={z['b']['單價_元每m2']}"]))

    print("=" * 64)
    allok = True
    n_byte = n_cell = 0
    for name, ok, det in results:
        allok = allok and ok
        if ok:
            n_cell += 1
        else:
            print(f"  🔴 FAIL  {name}")
            for x in det:
                print("       ", x)
    print(f"  ✅ {sum(1 for _,o,_ in results if o)}/{len(results)} 閘綠"
          f"（app-path f0→f4 逐代 byte-perfect＋逐格 vs 重烤 baseline·雙情境＋圍欄段價）")
    print("=" * 64)
    print("W-G G.3 雙路同源終驗:", "ALL GREEN（app live §7 == 重烤後 baseline·真同源）" if allok else "FAIL")
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
