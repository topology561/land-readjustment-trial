#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-70 B-3】`q` 之取值序：檔案級優先／街廓級回退／二者皆無仍停機　⛔ 零生產碼

**受測者** ＝ `app.py` 之 `_cad_dxf_quantum`（由 `harvest` 取**真符號**·⛔ 非複本）。

🔒 **入倉之由**：本檔驗的是**生產碼變更後之行為** ⇒ 須**倉內可重現**。
  ⚠️ B-1（**修前**之紅）之腳本係施工單 §三 B-1 明令之**倉外** scratchpad 腳本，
  其逐字 raise 訊息存於 `verify/out/wg970_B1_prove_red_21159c9.log`。

**三格（⛔ 缺一不可）**：
  (1) **檔案級有值 ＋ 手動鎖邊（無 `_match`）** ⇒ `q` 取得 ⇒ **正常回多邊形**
      （＝ `GB-85` 出路③所修之情境；修前此格 loud raise）
  (2) **檔案級無 ＋ `_match` 有**（舊 session／既有探針與夾具之路）⇒ **回退成立**
  (3) **二者皆無** ⇒ `q=None` ⇒ **仍 loud raise**（⛔ 證未兜底——該停機是對的）

🔒 **儀器沿用既有者**（`probe_WG960_fitcore.build_ctx`）——⛔ 未新增第二份判定原語。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
for _p in (VERIFY, HERE):
    sys.path.insert(0, _p)

from probe_WG960_fitcore import build_ctx                           # noqa: E402

LBL, WHICH = "R1", "left"


def call_range(ns, cb_by, cad, snapshot, wd, q):
    b = cb_by[LBL]
    mb = cad["baselines"][LBL]
    fl = cad["front_lines"][LBL]
    sd = cad["side_lines_by_side"][LBL][WHICH]
    return ns["_build_corner_range_v3"](
        block_vertices=b["vertices"], block_centroid=b["centroid"],
        front_pts=[fl["p1"], fl["p2"]],
        baseline_pts=ns["_baseline_pts_from_manual"](mb, b["vertices"]),
        side_line_pts=[sd["p1"], sd["p2"]],
        alloc_dir=cad["alloc_dir_by_block"][LBL],
        block_depth=float(snapshot["blocks"][LBL]["街廓分配深度_m"]),
        setback=0.0, min_width=wd[LBL][0],
        chamfer_tri=ns["_make_chamfer_tri_wb"](b, WHICH),
        dxf_quantum=q, _label=LBL, _side=WHICH)


def main():
    ns, cb_by, cad, snapshot, wd, _t = build_ctx()
    getq = ns["_cad_dxf_quantum"]
    real_mb = cad["baselines"][LBL]
    # 模擬 UI 之「手動鎖邊」所寫入之 `f3_manual_baseline[街廓]`（⛔ 無 `_match`）
    manual_mb = {'point': real_mb.get('point'),
                 'angle_deg': real_mb.get('angle_deg'), 'enabled': True}

    print("=" * 110)
    print("【W-G.9-70 B-3】`q` 取值序（受測者 ＝ `app.py` 之 `_cad_dxf_quantum`·harvest 真符號）")
    print("=" * 110)
    print(f"  受測街廓／側 ＝ {LBL}／{WHICH}"
          f"　CAD 解析所得之 `_match.q_detected` ＝ {(real_mb.get('_match') or {}).get('q_detected')!r}")
    rc = 0
    cases = [
        ("(1) 檔案級有 ＋ 手動鎖邊(無 _match)", {'f3_cad_dxf_quantum': 1e-05}, manual_mb, True),
        ("(2) 檔案級無 ＋ _match 有（回退）", {}, real_mb, True),
        ("(3) 二者皆無（⛔ 不得兜底）", {}, manual_mb, False),
    ]
    for name, ss, mb, expect_ok in cases:
        q = getq(ss, mb)
        print(f"  ── {name}")
        print(f"     `_cad_dxf_quantum(...)` ⇒ {q!r}")
        try:
            poly = call_range(ns, cb_by, cad, snapshot, wd, q)
            got_ok, detail = True, f"回多邊形　area ＝ {float(poly.area):.6f} ㎡"
        except RuntimeError as e:
            got_ok, detail = False, "loud raise：" + str(e).splitlines()[0][:100]
        ok = (got_ok == expect_ok)
        rc = rc or (0 if ok else 1)
        print(f"     {'✅' if ok else '🔴'} 期望{'成功' if expect_ok else 'raise'}／實得"
              f"{'成功' if got_ok else 'raise'}　{detail}")
    print("-" * 110)
    print(f"  ⇒ **{'✅ 三格全符' if rc == 0 else '🔴 有格不符'}**")
    print("=" * 110)
    return rc


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    sys.exit(main())
