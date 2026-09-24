# -*- coding: utf-8 -*-
r"""`W-G.9-341`：`GB-182` 之合成案（幾何餘併入以邊相接之池帶·閉式期值·⛔ 零生產碼）。

受詞 ＝ `<repo>/app.py` 之 `_pool_strips_for_block`（經 `verify/app_harvest.py` 之 ns·二路徑同源之唯一產生者）。
合成幾何（⛔ 取自本案）：街廓 ＝ 矩形 x∈[0,100]、y∈[−30,0]；正面臨路線 y＝0；d̂＝(1,0)；
分配線 ∥ y 軸（函式之 allocation_dir ＝ 分配線之法向 (1,0)）⇒ s ＝ x。深度 30。
  甲 街角宗之遠側界斜置（正面端 x＝38、後端 x＝40·仿實案之「正面寬、後端尖」）：宗 ＝ (0,0)-(38,0)-(40,−30)-(0,−30)
     ⇒ 幾何餘 ＝ 三角 (38,0)-(40,0)-(40,−30)·30 ㎡，與池帶 s∈[40,100]（1800 ㎡）以邊 x＝40 相接
     ⇒ 期：池 1 片 ＝ 街廓 − 宗（1830 ㎡·對稱差 ≤ 1e-6）·無折返頂點。
  乙 同甲，另一宗占 x∈[40,60] ⇒ 幾何餘夾於二宗之間、⛔ 與池帶相接 ⇒ 期：池 2 片 {1200, 30}（沿舊法另成一片）。
  丙 同甲，另以強制帶 x∈[40,60] 傳入 forced_bands ⇒ 幾何餘只與強制帶相接 ⇒ 期：池 3 片 {1200, 600, 30}；強制帶之形逐位不變。
  丁 街角宗為矩形 x∈[0,40] ⇒ 無幾何餘 ⇒ 期：池 1 片 ＝ 矩形 x∈[40,100]（對稱差 ≤ 1e-9）。
  戊 同甲，惟宗之正面為 (0,0)-(38,−1e-6)（正面臨路線上留零寬之縫，與幾何餘連成一片 ⇒ 幾何餘之外緣沿正面臨路線
     折返 `38 m`·仿實案 R4 甲 3.5 m 之 `36.13 m`）⇒ 期：池 1 片、|面積 − 1830| ≤ 1e-3、無折返頂點。
折返頂點之判（本器自寫·⛔ 引受詞之碼）：頂點 b 與前一頂點相距 ≤ ε；或 ab·bc < 0 且 b 至直線 ac 之距 ≤ ε
（a、c 相距 ≤ ε 者距取 0）；ε ＝ ns 之 `_S_EPS`。
rc ＝ 不符之項數；器紅（ns 缺受詞或 `_S_EPS`）⇒ rc 90。
判別力：開工態（`09170db`）之樹 ⇒ 甲1、甲2、戊1、戊2、戊3 不符（必紅·rc 5）；乙、丙、丁於二樹皆符（未併之界不因本修而變）。
用法：python probe_WG9341_synth.py <repo 絕對路徑>
"""
import contextlib, io, math, os, sys
sys.stdout.reconfigure(encoding="utf-8")
REPO = sys.argv[1]
sys.path.insert(0, os.path.join(REPO, "verify"))
from app_harvest import harvest
from shapely.geometry import Polygon, box
with contextlib.redirect_stdout(io.StringIO()):
    ns, _fake_st = harvest(os.path.join(REPO, "app.py"))
if "_pool_strips_for_block" not in ns or "_S_EPS" not in ns:
    print("🔴 器紅：ns 缺 _pool_strips_for_block 或 _S_EPS"); sys.exit(90)
F = ns["_pool_strips_for_block"]; EPS = float(ns["_S_EPS"])
import numpy as np
D = np.array([1.0, 0.0]); C0 = np.array([0.0, 0.0]); AD = np.array([1.0, 0.0])
BLK = box(0, -30, 100, 0)

def rev_count(g):
    cs = [tuple(c) for c in list(g.exterior.coords)[:-1]]; n = len(cs); k = 0
    for i in range(n):
        a, b, c = cs[i - 1], cs[i], cs[(i + 1) % n]
        ab = (b[0] - a[0], b[1] - a[1]); bc = (c[0] - b[0], c[1] - b[1]); ac = (c[0] - a[0], c[1] - a[1])
        if math.hypot(*ab) <= EPS: k += 1; continue
        Lac = math.hypot(*ac)
        d = abs(ac[0] * ab[1] - ac[1] * ab[0]) / Lac if Lac > EPS else 0.0
        if ab[0] * bc[0] + ab[1] * bc[1] < 0 and d <= EPS: k += 1
    return k

def run(biz, fb=None):
    with contextlib.redirect_stdout(io.StringIO()):
        return F(BLK, D, C0, AD, biz, _label="SYN", _depth=30.0, _verbose=False, forced_bands=fb)

bad = 0
def chk(name, ok, got):
    global bad
    print(f"{'✅' if ok else '🔴'} {name}：得 {got}")
    bad += (0 if ok else 1)

lotA = Polygon([(0, 0), (38, 0), (40, -30), (0, -30)])
# 甲
out = run([lotA]); exp = BLK.difference(lotA)
chk("甲1 池片數 ＝ 1", len(out) == 1, [round(g.area, 6) for g in out])
chk("甲2 池片 ≡ 街廓 − 宗（對稱差 ≤ 1e-6）", len(out) == 1 and out[0].symmetric_difference(exp).area <= 1e-6,
    round(out[0].symmetric_difference(exp).area, 9) if out else None)
chk("甲3 併後之片無折返頂點", len(out) >= 1 and rev_count(out[0]) == 0, [rev_count(g) for g in out])
# 乙
lot2 = box(40, -30, 60, 0)
out = run([lotA, lot2])
chk("乙1 池片 ＝ {1200, 30}（夾於二宗之間者⛔ 併）", sorted(round(g.area, 6) for g in out) == [30.0, 1200.0],
    sorted(round(g.area, 6) for g in out))
# 丙
fb = box(40, -30, 60, 0)
out = run([lotA], fb=[fb])
chk("丙1 池片 ＝ {1200, 600, 30}（只與強制帶相接者⛔ 併）", sorted(round(g.area, 6) for g in out) == [30.0, 600.0, 1200.0],
    sorted(round(g.area, 6) for g in out))
chk("丙2 強制帶之形逐位不變", any(g.equals_exact(fb, 0.0) for g in out), [g.wkt[:60] for g in out if abs(g.area - 600) < 1e-6])
# 丁
out = run([box(0, -30, 40, 0)]); expD = box(40, -30, 100, 0)
chk("丁1 無幾何餘：池 1 片 ≡ 矩形 x∈[40,100]（對稱差 ≤ 1e-9）",
    len(out) == 1 and out[0].symmetric_difference(expD).area <= 1e-9, [round(g.area, 6) for g in out])
# 戊
lotE = Polygon([(0, 0), (38, -1e-6), (40, -30), (0, -30)])
out = run([lotE])
chk("戊1 池片數 ＝ 1", len(out) == 1, [round(g.area, 6) for g in out])
chk("戊2 |面積 − 1830| ≤ 1e-3", len(out) == 1 and abs(out[0].area - 1830.0) <= 1e-3, [round(g.area, 6) for g in out])
chk("戊3 無折返頂點", all(rev_count(g) == 0 for g in out), [rev_count(g) for g in out])
print(f"ε ＝ {EPS}｜rc {bad}")
sys.exit(bad)
