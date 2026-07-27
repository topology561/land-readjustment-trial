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

    # ── 🆕 甲-1(c)（KL 裁 2026-07-25）：**禁寫死本機絕對路徑**之全倉機檢 ──────────────────
    #   案由：`verify/fixture_end_fallback.py` 曾寫死 `REPO = r"<本機絕對路徑>"`
    #   ⇒ 自 `e45bbb2` 起 `run_all` 在**任何非本機機器**上必 FAIL（claude.ai 他機實跑 rc=1·
    #   FileNotFoundError；另二夾具 rc=0）。此為泛用化直接違例，故立永久機檢。
    #   ⚠️ 樣式以**片段串接**構成——否則本閘會咬到自己（自我匹配·假紅）。
    _ok_abs, _abs_hits = True, []
    _ABS_PAT = ["C:" + "/", "C:" + "\\", "/" + "Users" + "/",
                "Desktop" + "/land", "Desktop" + "\\land"]
    for _root, _dirs, _files in os.walk(REPO):
        _dirs[:] = [d for d in _dirs if not d.startswith(".")
                    and d not in ("__pycache__", "node_modules")]
        for _fn in _files:
            if not _fn.endswith(".py"):
                continue
            _fp = os.path.join(_root, _fn)
            try:
                _txt = open(_fp, encoding="utf-8").read().splitlines()
            except Exception:
                continue
            for _i, _ln in enumerate(_txt, 1):
                if any(_pt in _ln for _pt in _ABS_PAT):
                    _abs_hits.append(f"{os.path.relpath(_fp, REPO)}:{_i}: {_ln.strip()[:90]}")
    if _abs_hits:
        _ok_abs = False
        rc = 1
    print(f"  {'✅' if _ok_abs else '🔴'} 禁寫死絕對路徑閘（全倉 *.py）："
          + ("0 命中" if _ok_abs else f"{len(_abs_hits)} 命中"))
    for _h in _abs_hits[:12]:
        print("     " + _h)

    # ── 🆕 F-2（KL 裁 2026-07-25）：**末端機制三夾具納入 run_all** ──────────────────────
    #   覆蓋率洞：三檔存在於 `verify/` 卻**不在任何自動流程內**——「沒人檢查 ≠ 相符」
    #   （交接文 §5.2）。以 **subprocess** 起（`fixture_end_fallback` 於 import 期即
    #   `sys.exit()`，直接 import 會把 harness 一併帶走）。
    #   ⚠️ 本段屬 run_all `[1/3]` golden 段、**不進** `run_verification.results`
    #      ⇒ 不動 PASS/FAIL 計數，亦不動 P-H 之「161 名目」母體。
    import subprocess
    for _fx, _what in (("fixture_cad_binding_order.py", "🆕 C-6 CAD 線層綁定·順序不變性(3 置換)"),
                       ("fixture_baseline_candidates.py", "🆕 C-5 BASELINE 候選三分支＋R1 共線 golden"),
                       ("fixture_n14_min_width.py", "🆕 N-14/N-15 宗地最小寬度·深度帶內取 min"),
                       ("fixture_end_reserve.py", "P2-f 末端保留·窗位移(左右)"),
                       ("fixture_end_fallback.py", "§4 無勝者 fallback·守恆真檢(左右)"),
                       ("fixture_end_winner.py", "末端 gate 判別力·_unfront_area＋咬合反例")):
        try:
            _r = subprocess.run([sys.executable, os.path.join(HERE, _fx)],
                                capture_output=True, text=True, encoding="utf-8", timeout=600)
            _ok_fx = (_r.returncode == 0)
        except Exception as _e_fx:
            _r, _ok_fx = None, False
            print(f"  🔴 末端夾具 {_fx} 執行失敗：{_e_fx}")
        if _r is not None:
            print(f"  {'✅' if _ok_fx else '🔴'} 末端夾具 {_fx}（{_what}）rc={_r.returncode}")
            if not _ok_fx:
                for _ln in ((_r.stdout or "") + (_r.stderr or "")).strip().splitlines()[-10:]:
                    print("     " + _ln)
        if not _ok_fx:
            rc = 1
    print()

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
