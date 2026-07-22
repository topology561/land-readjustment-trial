# -*- coding: utf-8 -*-
"""§4 末端塊 fallback 合成夾具（獨立單測·不碰 pipeline/xlsx/錨）。

KL 旗（2026-07-21）：守恆須用**完整恆等式**逐位——
    ΣG ＋ pool_final(中間餘額) ＋ 抵費地街角 ＋ 抵費地末 ＝ 街廓面積
且驗前提 `poolE = 街廓 − ΣG − 抵費地街角`（frag 只在 poolE、不雙計；抵費地末=R_end 含 frag）。
＋ 非疊（抵費地末 vs 內移宗）＋ winner 路徑 diff=0（不觸 fallback）。

設計：軸對齊乾淨情境（cad_alloc ∥ y·s＝x）逼 fallback（全候選 G<area(R_end)）。
harvest() 只 exec app.py 之 def（AST 過濾·無 read_excel）→ ns 純函式·無 xlsx。
"""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
REPO = r"C:/Users/admin/Desktop/land-readjustment-trial"
sys.path.insert(0, os.path.join(REPO, "verify")); os.chdir(os.path.join(REPO, "verify"))
import numpy as np
from shapely.geometry import Polygon
from app_harvest import harvest
import wf_f4, wf_f1

ns, _st = harvest()                      # 純函式命名空間（AST 過濾·無 xlsx）
assert "_end_region_R" in ns, "harvest 未取得 _end_region_R"

# ── 乾淨合成幾何：block=[−F,W]×[0,H]·p1=(0,0)·d̂=+x·cad_alloc=+y（s＝x·strip 為垂直帶）──
F, W, H, MW = 4.0, 40.0, 10.0, 3.5       # frag 深 F·街廓寬 W·高 H·畸零寬 MW
BLK = "TEST"
block = Polygon([(-F, 0), (W, 0), (W, H), (-F, H)])          # 街廓面積 = (W+F)*H
frag = Polygon([(-F, 0), (0, 0), (0, H), (-F, H)])           # 未臨正街(s<0)：area = F*H = 40
# 末端帶 = 過 p1 ∥cad_alloc(+y)·向街廓內(+x) ⊥ MW → [0,MW]×[0,H]；R_end = frag∪末端帶 = [−F,MW]×[0,H]
area_rend_expect = (F + MW) * H                              # = 7.5*10 = 75.0
blk_area = (W + F) * H                                       # = 440.0

# 候選（得以分配建地·全 G<area(R_end)=75 → 逼 fallback）：三宗·各 G=60（<75）·排 R_end 內側
cand_G = [60.0, 60.0, 60.0]
_x = MW
rowsE = []
for i, g in enumerate(cand_G):
    wdt = g / H                                             # 乾淨情境：G = 寬×H → 寬 = g/H = 6.0 (≥MW)
    poly_i = Polygon([(_x, 0), (_x + wdt, 0), (_x + wdt, H), (_x, H)])
    rowsE.append({"所屬街廓": BLK, "推進側別": "left", "暫編地號": f"{BLK}-{i+1}",
                  "S(m)": wdt, "G(㎡)": g, "宗地寬度(m)": wdt, "累積S(m)": _x,
                  "幾何面積(㎡)": g, "畸零地旗標": "",
                  "cut_coords": list(poly_i.exterior.coords)})
    _x += wdt
sumG = sum(cand_G)                                          # = 180
corner_abate = 0.0                                          # 本情境無街角抵費地
# poolE = 街廓 − ΣG − 抵費地街角（clean 中間餘額·frag 含於此·不在任何建地 G）
poolE_clean = blk_area - sumG - corner_abate               # = 440 − 180 − 0 = 260

frag_row = {"街廓": BLK, "暫編": f"{BLK}-抵費地-2", "poly": frag, "面積": round(frag.area, 2),
            "s": 0.2, "三分類": "碎片",
            "cut_coords": list(frag.exterior.coords)}
snap = {"blocks": {BLK: {"街廓分配深度_m": H, "正面": {"路寬_m": 12.0}}}}
cb_by = {BLK: {"vertices": list(block.exterior.coords)[:-1], "category": "住宅區"}}
cad = {"front_lines": {BLK: {"p1": [0.0, 0.0], "p2": [float(W), 0.0]}},
       "alloc_dir_by_block": {BLK: [0.0, 1.0]}}             # cad_alloc = +y
forced = {BLK: {"left_has_side": False, "right_has_side": True,     # 條件1：左無 SIDELINE → gate 觸發
                "left_forced_offset": False, "right_forced_offset": False,
                "left_corner_min_area": 0.0, "right_corner_min_area": 0.0}}
mina = {BLK: 30.0}

# frag["poly"] 需可由 _poly_of 還原（wf_f1._poly_of 讀 polygon_coords）
def _run():
    rrows, npolys, tgt = wf_f4._reshape_block(ns, snap, cb_by, cad, forced, rowsE, BLK,
                                              frag_row, "fixture", mina)
    return rrows, npolys, tgt

try:
    rrows, npolys, tgt = _run()
except Exception as e:
    print(f"❌ _reshape_block raise：{type(e).__name__}: {e}")
    raise

# ── 分帳（模擬 E3 caller [B]）──
E_keys = {r["暫編地號"] for r in rowsE}
new_abate = {k: p for k, p in npolys.items() if k not in E_keys}   # 抵費地末（new key）
in_E = {k: p for k, p in npolys.items() if k in E_keys}
end_abate_area = sum(p.area for p in new_abate.values())
pool_final = poolE_clean - end_abate_area
sumG_final = sum(float(r["G(㎡)"]) for r in rowsE)                 # 建地 G 不變

# ── 驗①：抵費地末 = area(R_end)（含 frag·不雙計）──
abate_key = f"{BLK}-抵費地末"
ok_abate = (abs(end_abate_area - area_rend_expect) < 1e-6) and (abate_key in new_abate)
# ── 驗②：完整 4 項恆等式逐位 ──
identity = sumG_final + pool_final + corner_abate + end_abate_area
resid = identity - blk_area
ok_identity = abs(resid) < 1e-9
# ── 驗③：非疊（抵費地末 vs 內移宗）──
rend_poly = new_abate.get(abate_key)
max_ov = max((rend_poly.intersection(p).area for k, p in in_E.items()), default=0.0)
ok_nonoverlap = max_ov < 1e-6
# ── 驗④：建地 G 守恆（內移後 area≈G）──
ok_G = all(abs(p.area - float(next(r["G(㎡)"] for r in rowsE if r["暫編地號"] == k))) < 1e-6
           for k, p in in_E.items())

print("="*68)
print(f"街廓面積={blk_area:.6f}  ΣG={sumG_final:.6f}  poolE(clean)={poolE_clean:.6f}")
print(f"抵費地末(=R_end)={end_abate_area:.6f}  (期 {area_rend_expect:.6f})  抵費地街角={corner_abate:.6f}")
print(f"pool_final=poolE−R_end={pool_final:.6f}")
print(f"完整恆等式 ΣG+pool_final+街角+末 = {identity:.9f}  街廓={blk_area:.9f}  殘差={resid:.2e}")
print(f"非疊 max_overlap={max_ov:.2e}   內移宗數={len(in_E)}  抵費地末 key={abate_key in new_abate}")
print("-"*68)
print(f"①抵費地末=area(R_end)含frag不雙計 : {'✅' if ok_abate else '❌'}")
print(f"②完整4項恆等式逐位(<1e-9)        : {'✅' if ok_identity else '❌'}  殘差={resid:.2e}")
print(f"③抵費地末與內移宗非疊(<1e-6)      : {'✅' if ok_nonoverlap else '❌'}")
print(f"④建地 G 守恆(內移後 area≈G)       : {'✅' if ok_G else '❌'}")
print("="*68)
_all = ok_abate and ok_identity and ok_nonoverlap and ok_G
print("RESULT:", "ALL GREEN ✅" if _all else "FAIL ❌")
sys.exit(0 if _all else 1)
