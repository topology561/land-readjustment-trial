# -*- coding: utf-8 -*-
"""§4 **P2-f 末端保留**合成夾具（獨立單測·不碰 pipeline/xlsx/錨）。**左＋右雙向**。

## 存在理由（**區辨兩種 no-op**）

P2-f 於 UC9898 實測為**零數值影響**（E2 診斷字串逐字相同）。但「no-op」有兩種成因、
結論相同而意義相反：

  (甲) **正確計算後本就不影響**——gate 有觸發、末端帶算出，惟該區本就落在階段2 池窗之外；
  (乙) **因 bug 而根本沒觸發**——如旗標鍵名錯、cond2 判反 ⇒ 形同死碼。

倉內證據（`W-G.4_plan_reviewer退回_三域裁題上呈.md:103-118`）指向 (甲)，但那是**間接**推論。
本夾具以**合成幾何直測** `_place_pool_parcels` 之末端保留：同一組輸入僅切換
`has_side_{side}` 旗標，驗窗起點是否恰好位移**一個手算值**——(乙) 下位移必為 0。

## 期望值出處（`fixture-provenance`·**皆獨立手算**·禁跑一次回填）

`cad_alloc = +y` ⇒ s 軸＝x 軸（`_strip_axis` 於 d̂=+x／alloc=+y 退化為正交·m̂=+x·denom=1）。
`_end_band` ＝過 `end_pt`、∥`cad_alloc`、向形心側 ⊥垂距 `MW` 之帶 ∩ block：

| 側 | block | s_max | end_pt | 形心 | 定號後 nrm | **末端帶 s 區間（手算）** | 保留式 |
|---|---|---|---|---|---|---|---|
| 左 | x∈[−F, W] | W=40 | p1=(0,0) | (18,5) | (+1,0) | **[0, MW]＝[0, 3.5]** | `lo = 3.5` |
| 右 | x∈[0, W+F] | W+F=44 | p2=(40,0) | (22,5) | (−1,0) | **[W−MW, W]＝[36.5, 40]** | `hi = 36.5` |

**手算之兩個可觀測量**（皆自上表導出）：

| 側 | 窗起點 s（gate 關 → 開） | 窗寬 `S_max`（gate 關 → 開） | 縮減量 |
|---|---|---|---|
| 左 | 0 → **3.5** | 40 − 0 ＝ 40 → 40 − 3.5 ＝ **36.5** | **MW ＝ 3.5** |
| 右 | 0 → 0（不動·見下） | 44 − 0 ＝ 44 → 36.5 − 0 ＝ **36.5** | **F ＋ MW ＝ 7.5** |

右側縮減 ＝ `F+MW` 而非 `MW`：末端區 ＝ 未臨正街（s>40·＝F 段）∪ 末端帶（[36.5,40]）＝ **[36.5, 44]**，
保留須同時排除二者 ⇒ 窗迄點 44 → 36.5。

⚠️ **右案為何量窗寬而非起點**：兩側跨占皆 0 ⇒ B5 tie-break **落左**（決定性·`_place_pool_parcels`
既有語意），故右案之落位仍在左端、起點不動；但**窗寬為左右共用**（`_pool_S = _pool_hi − _pool_lo`），
右側保留必反映於 `S_max`。故右案以 `S_max` 為觀測量——**非**繞過測試，而是取該側唯一未被
tie-break 遮蔽之可觀測量。

cond2（未臨正街半平面）：左 `block∩{s<0}` ＝ F×H ＝ 40.0㎡ > ε；右 `block∩{s>s(p2)}` 同 40.0㎡。
（與 `fixture_end_fallback.py` 同一組合成幾何·數值可互相對拍。）

## 重跑
    python verify/fixture_end_reserve.py
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "verify"))
os.chdir(os.path.join(REPO, "verify"))

import numpy as np                                        # noqa: E402
from shapely.geometry import Polygon                      # noqa: E402
from app_harvest import harvest                           # noqa: E402

ns, _st = harvest()
for _n in ("_place_pool_parcels", "_end_band", "_strip_s_range"):
    assert _n in ns, f"harvest 未取得 {_n}"

F, W, H, MW = 4.0, 40.0, 10.0, 3.5        # 同 fixture_end_fallback 之合成幾何
D_HAT = np.array([1.0, 0.0])              # FRONT ＝ +x
ALLOC_CAD = [0.0, 1.0]                    # 宗地分配線方向 ＝ +y
ALLOC_AXIS = ns["alloc_normal_axis"](ALLOC_CAD)   # rot90 ⇒ 切帶法向（引擎口徑）

# ── 手算期望（**獨立於本碼**·見 docstring 二表）────────────────────────────────
EXPECT = {
    # band_s：末端帶 s 區間｜s0_off/s0_on：窗起點（gate 關/開）｜Smax_off/Smax_on：窗寬
    "left":  {"band_s": (0.0, MW), "s0_off": 0.0, "s0_on": MW,
              "Smax_off": W, "Smax_on": W - MW},                      # 縮 MW
    "right": {"band_s": (W - MW, W), "s0_off": 0.0, "s0_on": 0.0,
              "Smax_off": W + F, "Smax_on": W - MW},                  # 縮 F+MW
}


def _case(side):
    if side == "left":
        block = Polygon([(-F, 0), (W, 0), (W, H), (-F, H)])
        corner_pt = np.array([0.0, 0.0])          # p1
    else:
        block = Polygon([(0, 0), (W + F, 0), (W + F, H), (0, H)])
        corner_pt = np.array([0.0, 0.0])          # p1（右案 block 自 0 起）
    return block, corner_pt


def _stub_solver(rec):
    """記錄實際餵入之 baseline_pt／S_max，並回傳「恰好落位」之 res（G==幾何 ⇒ 不觸 P2-g 拒絕）。"""
    def solve_one(_a, _A, _lf, _ls, _F, _bp_poly, _dh, _baseline_pt, _S_max,
                  _is_corner, _side, _depth, _allocation_dir=None, _side_mid=None, _W_prev=0.0):
        rec.append({"baseline_pt": np.asarray(_baseline_pt, dtype=float), "S_max": float(_S_max)})
        return ({"G": 10.0, "area_geom": 10.0, "S": 1.0, "S_raw": 1.0,
                 "W": 0.0, "W_far": 0.0, "Rw_pct": 0.0, "cut_coords": [],
                 "converged": True, "iterations": 1, "trace": []}, "stub")
    return solve_one


def _run(side, has_side):
    """回傳 (窗起點 s, 末端帶 s 區間 or None)。`has_side` 即 gate 條件1 之反。"""
    block, corner_pt = _case(side)
    rec = []
    tp = {"暫編地號": "SYN-1", "配地階段": "池內", "面積_m2": 20.0,
          "重劃前地價區段": "z", "所屬街廓": "TEST"}
    adv = {"rows": [], "left_results": [], "right_results": [],
           "left_cum_S": 0.0, "right_cum_S": 0.0, "Wf_left": 0.0, "Wf_right": 0.0}
    s_max_blk = (W if side == "left" else W + F)
    ns["_place_pool_parcels"](
        stage2_parcels=[tp], adv_final=adv, blk_poly=block, blk_area=float(block.area),
        blk_label="TEST", blk_vertices=list(block.exterior.coords),
        blk_centroid=(block.centroid.x, block.centroid.y),
        d_hat=D_HAT, corner_pt=corner_pt, s_max_blk=s_max_blk,
        allocation_dir=ALLOC_AXIS, alloc_dir_cad=ALLOC_CAD,
        front_len=W, l_front=1.0, avg_depth=H,
        side_mid_left=None, side_mid_right=None,          # 無 SIDE_LINE ⇒ 跨占 0（不干擾）
        l_side_left=0.0, F_left=0.0, l_side_right=0.0, F_right=0.0,
        post_price=100.0, pre_price_by_zone={"z": 100.0},
        solve_one=_stub_solver(rec), build_g_row=lambda *a, **k: {},
        mark_zaling=lambda r: r,
        has_side_left=(has_side if side == "left" else True),
        has_side_right=(has_side if side == "right" else True),
        min_width=MW, s_front_p2=W, _verbose=False)
    assert rec, f"{side}/has_side={has_side}：solver 未被呼叫（窗為空？）"
    bp = rec[0]["baseline_pt"]
    # 左：窗起點 s ＝ (bp − corner)·d̂；右：自 end_pt 反向推進 ⇒ 窗迄點 s ＝ s_max − cum_right
    s_start = float(np.dot(bp - corner_pt, D_HAT))
    return s_start, rec[0]["S_max"]


def main():
    ok = True
    print("=" * 78)
    print("§4 P2-f 末端保留 合成夾具（左＋右雙向·期望值獨立手算）")
    print("=" * 78)
    for side in ("left", "right"):
        block, corner_pt = _case(side)
        exp = EXPECT[side]

        # 驗0：`_end_band` 直測 vs 手算 s 區間
        end_pt = (corner_pt if side == "left"
                  else corner_pt + W * D_HAT)
        band = ns["_end_band"](block, ALLOC_CAD, end_pt, MW, _label=f"fx·{side}")
        bs = ns["_strip_s_range"](band, D_HAT, corner_pt, ALLOC_AXIS)
        d0 = max(abs(bs[0] - exp["band_s"][0]), abs(bs[1] - exp["band_s"][1]))
        print(f"\n[{side}] 驗0 末端帶 s 區間：實測 ({bs[0]:.4f}, {bs[1]:.4f})  "
              f"手算 ({exp['band_s'][0]:.4f}, {exp['band_s'][1]:.4f})  Δ={d0:.2e}"
              f"  {'✅' if d0 < 1e-6 else '🔴'}")
        ok &= d0 < 1e-6

        # 驗1：gate 關（該側有 SIDELINE）→ 不保留；gate 開 → 窗起點／窗寬各如手算
        s_off, smax_off = _run(side, has_side=True)
        s_on, smax_on = _run(side, has_side=False)
        for _nm, _got, _exp in (("窗起點 gate關", s_off, exp["s0_off"]),
                                ("窗起點 gate開", s_on, exp["s0_on"]),
                                ("窗寬   gate關", smax_off, exp["Smax_off"]),
                                ("窗寬   gate開", smax_on, exp["Smax_on"])):
            _d = abs(_got - _exp)
            print(f"[{side}] 驗1 {_nm}：實測 {_got:9.4f}  手算 {_exp:9.4f}  "
                  f"Δ={_d:.2e}  {'✅' if _d < 1e-6 else '🔴'}")
            ok &= _d < 1e-6
        _shrink = smax_off - smax_on
        print(f"[{side}] 驗1 窗寬縮減 ＝ {_shrink:.4f}"
              f"（＝{'MW' if side == 'left' else 'F+MW'} ＝ "
              f"{MW if side == 'left' else F + MW:.4f}）"
              f"  {'✅' if abs(_shrink - (MW if side == 'left' else F + MW)) < 1e-6 else '🔴'}")
        ok &= abs(_shrink - (MW if side == "left" else F + MW)) < 1e-6

    print("\n" + "=" * 78)
    print(f"RESULT: {'PASS' if ok else 'FAIL'}"
          + ("　⇒ 末端保留路徑**活著**（非死碼）：gate 觸發且位移恰為手算 MW。"
             if ok else "　⇒ 停機上呈"))
    print("=" * 78)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
