# -*- coding: utf-8 -*-
"""§4 末端塊 fallback 合成夾具（獨立單測·不碰 pipeline/xlsx/錨）。**左＋右雙向**（claude.ai W3）。

KL 旗（2026-07-21）：守恆須完整恆等式·且**真檢**（reviewer 揭舊「4 項恆等式」＝end_abate 相消·套套邏輯·零力）。
真檢＝驗0（`_end_region_R` 直測 band/frag/R_end 對獨立手算）＋②（帳池==幾何池·block−實際 union−街角·**可 fail**）＋③非疊＋④G守恆。
右向（W3·claude.ai）：右 has_side=False＋右未臨正街（block∩{s>s(p2)}）＋全候選 G<area(R_end)。
若右側非乾淨鏡像 → RESULT FAIL（停機上呈·退 loud-raise 保底）。

harvest() 只 exec app.py 之 def（AST 過濾·無 read_excel）→ ns 純函式·無 xlsx。
"""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
REPO = r"C:/Users/admin/Desktop/land-readjustment-trial"
sys.path.insert(0, os.path.join(REPO, "verify")); os.chdir(os.path.join(REPO, "verify"))
import numpy as np
from shapely.geometry import Polygon
from shapely.ops import unary_union as _uu
from app_harvest import harvest
import wf_f4, wf_f1

ns, _st = harvest()
assert "_end_region_R" in ns, "harvest 未取得 _end_region_R"

F, W, H, MW = 4.0, 40.0, 10.0, 3.5       # frag 深 F·街廓寬 W·高 H·畸零寬 MW
BLK = "TEST"
area_rend_expect = (F + MW) * H          # 75.0
band_expect, frag_expect = MW * H, F * H # 35.0 / 40.0
blk_area = (W + F) * H                   # 440.0
cand_G = [60.0, 60.0, 60.0]              # 全 < area(R_end)=75 → 逼 fallback
sumG = sum(cand_G)                       # 180
corner_abate = 0.0
poolE_clean = blk_area - sumG - corner_abate   # 260

snap = {"blocks": {BLK: {"街廓分配深度_m": H, "正面": {"路寬_m": 12.0}}}}
cad = {"front_lines": {BLK: {"p1": [0.0, 0.0], "p2": [float(W), 0.0]}},
       "alloc_dir_by_block": {BLK: [0.0, 1.0]}}     # cad_alloc = +y
mina = {BLK: 30.0}


def build_case(side):
    """回傳 (block_poly, frag_poly, end_pt, forced, rowsE)。左右鏡像·cad_alloc=+y·s＝x。"""
    if side == "left":
        block = Polygon([(-F, 0), (W, 0), (W, H), (-F, H)])
        frag = Polygon([(-F, 0), (0, 0), (0, H), (-F, H)])          # s<0（p1 外）
        end_pt = [0.0, 0.0]                                         # p1
        frag_s = 0.2
        forced = {"left_has_side": False, "right_has_side": True}
        xs = [MW + 6 * i for i in range(3)]                         # 候選右於 R_end：[3.5,9.5,15.5..]
        cum0 = [x for x in xs]                                       # 左 s＝x（累積S）
    else:  # right
        block = Polygon([(0, 0), (W + F, 0), (W + F, H), (0, H)])
        frag = Polygon([(W, 0), (W + F, 0), (W + F, H), (W, H)])    # s>s(p2)=W（p2 外）
        end_pt = [float(W), 0.0]                                    # p2
        frag_s = 0.99
        forced = {"left_has_side": True, "right_has_side": False}
        # R_end 右＝[W−MW, W+F]=[36.5,44]；候選左於 R_end：[18.5,24.5],[24.5,30.5],[30.5,36.5]
        xs = [(W - MW) - 6 * (i + 1) for i in range(3)]             # [30.5,24.5,18.5]（右→左）
        cum0 = [(W + F) - (x + 6) for x in xs]                       # 距右角 corner(W+F)：[7.5,13.5,19.5]
    forced.update({"left_forced_offset": False, "right_forced_offset": False,
                   "left_corner_min_area": 0.0, "right_corner_min_area": 0.0})
    rowsE = []
    for i, (g, x, c) in enumerate(zip(cand_G, xs, cum0)):
        wdt = g / H                                                # 乾淨：G=寬×H → 寬=6.0(≥MW)
        poly_i = Polygon([(x, 0), (x + wdt, 0), (x + wdt, H), (x, H)])
        rowsE.append({"所屬街廓": BLK, "推進側別": side, "暫編地號": f"{BLK}-{i+1}",
                      "S(m)": wdt, "G(㎡)": g, "宗地寬度(m)": wdt, "累積S(m)": c,
                      "幾何面積(㎡)": g, "畸零地旗標": "",
                      "cut_coords": list(poly_i.exterior.coords)})
    frag_row = {"街廓": BLK, "暫編": f"{BLK}-抵費地-2", "poly": frag, "面積": round(frag.area, 2),
                "s": frag_s, "三分類": "碎片", "cut_coords": list(frag.exterior.coords)}
    return block, frag, end_pt, forced, rowsE, frag_row


def run_case(side):
    block, frag, end_pt, forced, rowsE, frag_row = build_case(side)
    cb_by = {BLK: {"vertices": list(block.exterior.coords)[:-1], "category": "住宅區"}}
    forced_map = {BLK: forced}
    # 驗0（強·獨立幾何）：_end_region_R 直測·對獨立手算
    band_poly, _rd, rend_area_direct = ns["_end_region_R"](
        block, [0.0, 1.0], end_pt, MW, frag, _label=f"fixture-{side}")
    ok_band = abs(band_poly.area - band_expect) < 1e-6
    ok_fragA = abs(frag.area - frag_expect) < 1e-6
    ok_rend0 = abs(rend_area_direct - area_rend_expect) < 1e-6
    # 跑 _reshape_block（逼 fallback）
    try:
        rrows, npolys, tgt = wf_f4._reshape_block(ns, snap, cb_by, cad, forced_map, rowsE, BLK,
                                                  frag_row, f"fx-{side}", mina)
    except Exception as e:
        return False, f"[{side}] ❌ _reshape_block raise：{type(e).__name__}: {e}"
    E_keys = {r["暫編地號"] for r in rowsE}
    new_abate = {k: p for k, p in npolys.items() if k not in E_keys}
    in_E = {k: p for k, p in npolys.items() if k in E_keys}
    end_abate_area = sum(p.area for p in new_abate.values())
    pool_final = poolE_clean - end_abate_area
    abate_key = f"{BLK}-抵費地末"
    rend_poly = new_abate.get(abate_key)
    if rend_poly is None:
        return False, f"[{side}] ❌ 無 {abate_key}（fallback 未觸發·tgt={tgt}·npolys={list(npolys)}）"
    ok_abate = (abs(end_abate_area - area_rend_expect) < 1e-6) and (abate_key in new_abate)
    placed_union = _uu([rend_poly] + list(in_E.values()))
    geom_pool = blk_area - placed_union.area - corner_abate           # 真幾何交叉
    ok_geom = abs(geom_pool - pool_final) < 1e-6
    max_ov = max((rend_poly.intersection(p).area for k, p in in_E.items()), default=0.0)
    ok_nonoverlap = max_ov < 1e-6
    ok_G = all(abs(p.area - float(next(r["G(㎡)"] for r in rowsE if r["暫編地號"] == k))) < 1e-6
               for k, p in in_E.items())
    ok = ok_band and ok_fragA and ok_rend0 and ok_abate and ok_geom and ok_nonoverlap and ok_G
    out = (f"[{side}] _end_region_R 直測 frag={frag.area:.4f}(期{frag_expect}) band={band_poly.area:.4f}(期{band_expect})"
           f" R_end={rend_area_direct:.4f}(期{area_rend_expect})\n"
           f"[{side}] 抵費地末={end_abate_area:.4f} pool_final={pool_final:.4f} 幾何池={geom_pool:.4f}"
           f" Δ={geom_pool-pool_final:.2e} 非疊={max_ov:.2e} 內移宗={len(in_E)}\n"
           f"[{side}] 0直測band∧frag∧R_end:{'✅' if (ok_band and ok_fragA and ok_rend0) else '❌'}"
           f"  ①抵費地末=R_end:{'✅' if ok_abate else '❌'}  ②帳池==幾何池:{'✅' if ok_geom else '❌'}"
           f"  ③非疊:{'✅' if ok_nonoverlap else '❌'}  ④G守恆:{'✅' if ok_G else '❌'}")
    return ok, out


print("=" * 72)
_all = True
for _side in ("left", "right"):
    _ok, _out = run_case(_side)
    print(_out)
    print("-" * 72)
    _all = _all and _ok
print("RESULT:", "ALL GREEN ✅（左右雙向）" if _all else "FAIL ❌（右側非乾淨鏡像→停機上呈·退 loud-raise 保底）")
sys.exit(0 if _all else 1)
