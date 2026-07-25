# -*- coding: utf-8 -*-
"""W-V 單一命令：手冊圖8 golden ＋ headless 雙情境對拍 baselines。exit 0＝全綠。
用法：python verify/run_all.py"""
import ast
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "tests"))


def _candidates_append_keys(pyfile):
    """🆕 P-C（裁定M·B-3）：AST 取該檔內 `_candidates.append({...})` dict literal 之鍵集
    （app.py main() PK 與 selection_pipeline.run_corner_pk 各一）。app 段在 main() 內·靜態解析
    不執行碼。回 frozenset|None。"""
    tree = ast.parse(open(pyfile, encoding="utf-8").read())
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "append"
                and isinstance(n.func.value, ast.Name)
                and n.func.value.id == "_candidates"
                and n.args and isinstance(n.args[0], ast.Dict)):
            keys = []
            for k in n.args[0].keys:
                if isinstance(k, ast.Constant):
                    keys.append(k.value)
            return frozenset(keys)
    return None


def _check_candidates_keyset():
    """app _candidates 欄集 == selection_pipeline _candidates 欄集（B-3 鏡射結構閘）。"""
    _app = _candidates_append_keys(os.path.join(REPO, "app.py"))
    _sel = _candidates_append_keys(os.path.join(HERE, "selection_pipeline.py"))
    if _app is None or _sel is None:
        return False, f"取不到 _candidates.append 字面（app={_app is not None}·sel={_sel is not None}）"
    if _app != _sel:
        return False, (f"欄集不等：app∖sel={sorted(_app - _sel)}·sel∖app={sorted(_sel - _app)}")
    return True, f"{len(_app)} 鍵一致"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    rc = 0

    print("### [1/3] golden 單測（手冊圖8 ＋ W-D.2 滑池槽 8 案 ＋ B-3 欄集結構閘）")
    _ok_ks, _msg_ks = _check_candidates_keyset()
    print(f"  {'✅' if _ok_ks else '🔴'} B-3 欄集結構閘（app==sel _candidates 鍵集）：{_msg_ks}")
    if not _ok_ks:
        rc = 1
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
        print(f"  ✅ 滑池槽 golden PASS（{_n_ps}/8：KL例 J=1.80/1.50㎡＋E1-E7）\n")
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
