# -*- coding: utf-8 -*-
r"""**D-2b-15 §d-4-2**：回歸測試——本案例於**新判準**下不 raise，且各片面積 == 面積鏈差值。

⛔ **不得**斷言「（舊）鋪滿閘②通過」——該區帶內 `.intersection()` 量法**本身不可信**，
   斷言它等於把**不可信量測**寫成期望值（`fixture-provenance`）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import case_D2b15_tilegate_intersection as C                        # noqa: E402

TOL = 1e-6


def main():
    # ⚠️ Windows 主控台預設 cp950 ⇒ 直接 print emoji/中文會 UnicodeEncodeError
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding='utf-8')
        except Exception:
            pass
    from shapely.geometry import Polygon
    ns, _ = harvest()
    poly = Polygon(C.BLOCK)
    pieces, diag = ns["_block_partition"](poly, C.D_HAT, C.LINES, _label="D2b15-test")
    assert diag["n_pieces"] == len(C.LINES), \
        f"片數 {diag['n_pieces']} != 界線數 {len(C.LINES)}"
    # 各片面積 == 面積鏈差值（逐步）
    for c in diag["chain"]:
        assert c["resid"] <= TOL, \
            f"步{c['i']} |片−(rem₋₁−rem)| = {c['resid']:.3e} > {TOL:g}"
    assert abs(diag["resid"]) <= TOL, f"總量恆等 {diag['resid']:.3e} > {TOL:g}"
    assert diag["max_compl_both"] <= TOL and diag["max_compl_gap"] <= TOL, \
        f"互補性 both={diag['max_compl_both']:.3e} gap={diag['max_compl_gap']:.3e}"
    print(f"✅ D-2b-15 回歸案例通過新判準："
          f"片數 {diag['n_pieces']}／總量 {abs(diag['resid']):.3e}"
          f"／逐步 max {diag['max_chain_resid']:.3e}"
          f"／互補 both {diag['max_compl_both']:.3e} gap {diag['max_compl_gap']:.3e}")
    print(f"   各片面積 = {[round(a, 6) for a in diag['areas']]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
