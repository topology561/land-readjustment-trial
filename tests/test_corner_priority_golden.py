# -*- coding: utf-8 -*-
"""
W-D.1.3-d ① 手冊圖 8 golden 回歸單測（鎖街角地優先權三指數評分基準）。

**測的是 app.py 的實際評分函式，不是平行複本。** 以 AST 從 app.py 抽出 top-level
函式 `_pk_one_side_v12`（W-D.1.3-c 三指數逐筆化之單側 PK 核心），compile 該單一節點、
exec 進獨立命名空間後直接呼叫——**不 import app.py**（模組級有 `st.set_page_config`，
headless 會炸；且 `_pk_one_side_v12` 純 stdlib、無 numpy/shapely/streamlit 依賴，可獨立 exec）。

手冊圖 8（規格 §7.3）：雙側、單一 range、兩候選；分母＝range 自身量
（截角斜邊長 5、側街線總長 37＝25+12、範圍面積 300＝100+200）：
  1地號 項一 5/5、項二 25/37、項三 100/300 → 0.4·1 + 0.2·(25/37) + 0.4·(100/300) ≈ 0.6685
  2地號 項一 0/5、項二 12/37、項三 200/300 → 0 + 0.2·(12/37) + 0.4·(200/300) ≈ 0.3315
  winner = 1地號。

若此測失敗＝評分公式被動到（回歸），停機交 KL。每波必跑：
  python tests/test_corner_priority_golden.py      （exit 0＝pass）
  或  pytest tests/test_corner_priority_golden.py
"""
import ast
import os
import sys

# Windows 終端預設 cp950；確保中文/emoji 輸出（含失敗時的中文 assert 訊息）不炸編碼。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

FUNC_NAME = "_pk_one_side_v12"
_APP_PY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")


def _extract_func(name=FUNC_NAME, app_path=_APP_PY):
    """AST-抽 app.py 的 top-level 函式 name，exec 進獨立命名空間並回傳該 callable。"""
    with open(app_path, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src)
    node = next(
        (n for n in tree.body
         if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name),
        None,
    )
    if node is None:
        raise AssertionError(
            f"在 app.py 找不到 top-level 函式 `{name}`——評分核心被改名或刪除？"
            f"（W-D.1.3-d 應保留此 LIVE V13 評分路徑）"
        )
    mod = ast.Module(body=[node], type_ignores=[])
    ns = {}
    exec(compile(mod, filename=f"<{name}@app.py>", mode="exec"), ns)
    fn = ns.get(name)
    if not callable(fn):
        raise AssertionError(f"exec `{name}` 後未取得 callable")
    return fn


def _fig8_group():
    """手冊圖 8 兩候選；G-gate 設 min_area_to_apply=0、G_value 極大 → 雙雙達標。"""
    return [
        {  # 1地號
            "暫編地號": "1", "min_area_to_apply": 0.0, "G_value": 1e9,
            "_corner_cut_len": 5.0, "_corner_cut_den": 5.0,     # 項一 5/5
            "_side_line_len": 25.0, "_side_line_den": 37.0,     # 項二 25/37
            "_corner_intersection_area": 100.0, "_corner_range_area": 300.0,  # 項三 100/300
        },
        {  # 2地號
            "暫編地號": "2", "min_area_to_apply": 0.0, "G_value": 1e9,
            "_corner_cut_len": 0.0, "_corner_cut_den": 5.0,     # 項一 0/5
            "_side_line_len": 12.0, "_side_line_den": 37.0,     # 項二 12/37
            "_corner_intersection_area": 200.0, "_corner_range_area": 300.0,  # 項三 200/300
        },
    ]


def test_fig8_golden():
    pk = _extract_func()
    res = pk(_fig8_group(), g_values_map={}, base_front_len_m=100.0)

    by_id = {c["暫編地號"]: c for c in res["qualified"]}
    assert set(by_id) == {"1", "2"}, f"兩候選皆應達標，實得 {sorted(by_id)}"

    s1 = round(float(by_id["1"]["priority_index"]), 4)
    s2 = round(float(by_id["2"]["priority_index"]), 4)
    assert s1 == 0.6685, f"1地號 總分應＝0.6685，實得 {s1}"
    assert s2 == 0.3315, f"2地號 總分應＝0.3315，實得 {s2}"

    winner = res["winner"]
    assert winner is not None and winner["暫編地號"] == "1", (
        f"winner 應＝1地號，實得 {winner and winner.get('暫編地號')}"
    )

    # 三分項亦鎖（權重 0.4/0.2/0.4；項一全臨角＝0.4）
    assert round(float(by_id["1"]["_score_corner_cut"]), 4) == 0.4
    assert round(float(by_id["2"]["_score_corner_cut"]), 4) == 0.0


if __name__ == "__main__":
    test_fig8_golden()
    print("✅ W-D.1.3-d golden（手冊圖 8）通過：1地號=0.6685、2地號=0.3315、winner=1地號")
