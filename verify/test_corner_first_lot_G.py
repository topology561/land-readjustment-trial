# -*- coding: utf-8 -*-
"""P-A（裁定M·M-2/Q1）單測：`_corner_first_lot_G`（假設第 1 宗真 G·樂觀口徑）。

**本檔＝deterministic 守衛**（無需 converging 幾何）：
  A-3 缺值 loud：a_m2=None／avg_depth=0／side_mid=None 各觸 RuntimeError（Q-M4·no-silent-fallback）。
  A-4 fallback 覆蓋：blk_poly=None → `_solve_G_one` 走 iterate_G_S·label='代數迭代(fallback)'·不 raise。

**A-1 同一路徑＋A-2 左右 S_max 不同源** 之驗證改由 `probes/probe_corner_trueG.py` 承載
（該探針於**真 converging 幾何**上呼 `_corner_first_lot_G`·13 候選逐位·輸出與 T1 committed log 對拍）——
合成方塊會撞 S0d「切帶與街廓不交」邊界故非 converging、不適合這兩測（reviewer NOTE-5 之對偶：勿以假幾何冒充真幾何）。

harvest() 只 exec app.py def（AST·無 xlsx）→ ns 純函式。獨立單測·不碰 pipeline/baseline。
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from shapely.geometry import Polygon          # noqa: E402
from app_harvest import harvest                # noqa: E402

ns, _st = harvest()
for _n in ("_corner_first_lot_G", "_solve_G_one"):
    assert callable(ns.get(_n)), f"harvest 未取得 {_n}"
cflg = ns["_corner_first_lot_G"]
solve1 = ns["_solve_G_one"]

BLK = Polygon([(0, 0), (100, 0), (100, 40), (0, 40)])
BASE = dict(a_m2=200.0, A_ratio=1.0, B=0.171043, C=0.091319, l_front=100.0,
            l_side=40.0, F=8.0, block_poly=BLK, d_hat=(1.0, 0.0),
            corner_pt=(0.0, 0.0), s_max_left=100.0, s_max_right=60.0,
            side='左', allocation_dir=(0.0, 1.0), side_mid=(0.0, 20.0),
            avg_depth=32.59, tab6_burden=0.40712387)


def _fail(m):
    print(f"  🔴 {m}")
    return False


def a3_loud():
    """A-3：缺值 loud raise。"""
    cases = [("a_m2=None", {**BASE, 'a_m2': None}),
             ("avg_depth=0", {**BASE, 'avg_depth': 0.0}),
             ("side_mid=None", {**BASE, 'side_mid': None})]
    allok = True
    for nm, kw in cases:
        try:
            cflg(_label=f"A3·{nm}", **{k: v for k, v in kw.items() if k != '_label'})
            allok = False
            print(f"  A-3 {nm}：🔴 未 raise")
        except RuntimeError:
            print(f"  A-3 {nm}：✅ RuntimeError")
    return allok or _fail("A-3：缺值未 loud")


def a4_fallback():
    """A-4：blk_poly=None → _solve_G_one 走 fallback·label 正確·不 raise。"""
    res, lbl = solve1(a_m2=200.0, A=1.0, l_front=100.0, l_side=40.0, F=8.0,
                      blk_poly=None, d_hat=None, baseline_pt=None, S_max=100.0,
                      is_corner=True, side='左側', avg_depth=32.59,
                      B=0.171043, C=0.091319, tab6_burden=0.40712387)
    ok = (lbl == '代數迭代(fallback)') and float(res.get('G', 0.0) or 0.0) > 0
    print(f"  A-4 fallback：label={lbl!r} G={res.get('G')} {'✅' if ok else '🔴'}")
    return ok or _fail("A-4：fallback label/G 異常")


def main():
    print("=== P-A 單測：_corner_first_lot_G（A-3 缺值 loud＋A-4 fallback） ===")
    results = [a3_loud(), a4_fallback()]
    ok = all(results)
    print(f"\nRESULT: {'PASS ✅' if ok else 'FAIL 🔴'}（{sum(results)}/2）"
          "｜A-1/A-2 見 probe_corner_trueG.py（真幾何）")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
