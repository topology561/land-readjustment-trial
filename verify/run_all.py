# -*- coding: utf-8 -*-
"""W-V 單一命令：手冊圖8 golden ＋ headless 雙情境對拍 baselines。exit 0＝全綠。
用法：python verify/run_all.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "tests"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rc = 0

    print("### [1/3] golden 單測（手冊圖8 ＋ W-D.2 滑池槽 8 案）")
    try:
        import test_corner_priority_golden as g
        g.test_fig8_golden()
        print("  ✅ 圖8 golden PASS（1地號=0.6685、2地號=0.3315、winner=1地號）")
    except Exception as e:
        print(f"  🔴 圖8 golden FAIL: {e}")
        rc = 1
    try:
        import test_pool_slot as ps
        _n_ps = ps.run_all_cases()
        print(f"  ✅ 滑池槽 golden PASS（{_n_ps}/8：KL例 J=180/150＋E1-E7）\n")
    except Exception as e:
        print(f"  🔴 滑池槽 golden FAIL: {e}\n")
        rc = 1

    print("### [2/3] diff 引擎自檢（竄改必咬＋Gxxx 分流；證綠非虛）")
    import run_verification as v
    if not v.self_check_diff_engine():
        print("  🔴 diff 引擎自檢 FAIL → 對拍結果不可信，停")
        rc = 1
    print()

    print("### [3/3] W-V headless 對拍（verify/run_verification.py）")
    rc2 = v.main()
    rc = rc or rc2

    print("\n" + "#" * 60)
    print("W-V run_all:", "ALL GREEN" if rc == 0 else "FAIL")
    return rc


if __name__ == "__main__":
    sys.exit(main())
