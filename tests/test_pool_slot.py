# -*- coding: utf-8 -*-
"""
W-D.2 §3 滑池槽 golden 單測（8 案：KL 例＋W-D_細部plan §3.1 邊界 E1-E7）。

**測 app.py 實體 `_select_pool_slot`＋`rw_from_width`，非平行複本**——以 AST 抽兩個
top-level 函式、exec 進獨立命名空間（不 import app.py，模組級 st.set_page_config 會炸）。

Rw 表關鍵值（app.py rw_from_width，104 手冊 P.103）：
  R(4)=37.8  R(5)=44.0  R(6)=50.0  R(8)=61.1  R(10)=71.1  R(12)=80.0  R(18+)=100.0

每波必跑：python tests/test_pool_slot.py（exit 0＝pass）；run_all.py stage[1] 併跑。
"""
import ast
import os
import sys

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

_APP_PY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")
_FUNCS = ("rw_from_width", "_select_pool_slot")


def _extract():
    with open(_APP_PY, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    nodes = [n for n in tree.body
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in _FUNCS]
    got = {n.name for n in nodes}
    missing = set(_FUNCS) - got
    if missing:
        raise AssertionError(f"app.py 缺 top-level 函式 {sorted(missing)}——被改名或刪除？")
    mod = ast.Module(body=nodes, type_ignores=[])
    ns = {}
    exec(compile(mod, filename="<pool_slot@app.py>", mode="exec"), ns)
    return ns["_select_pool_slot"], ns["rw_from_width"]


def _side(has, F=1.0, l1=1.0, b=0.0):
    return {"has": has, "F": F, "l1": l1, "b": b}


def run_all_cases():
    slot, R = _extract()

    # 案1（KL 例，D-1 8/8 之錨）：w=[12,24,6] 雙側等權 →
    #   J(1)=(R(12)+R(30))/100=1.80、J(2)=(R(36)+R(6))/100=1.50 → k*=1（J 精確值鎖死）
    #   （J 單位＝負擔面積㎡，KL 量級裁示 2026-07-05；等權例 ×100 ↔ 手冊 %表述 180/150）
    r = slot([12, 24, 6], _side(True), _side(True))
    jb = {t["k"]: round(t["J"], 4) for t in r["table"]}
    assert jb == {1: 1.8, 2: 1.5}, f"案1 J 表應 {{1:1.8, 2:1.5}}，實得 {jb}"
    assert r["k"] == 1, f"案1 k* 應=1，實得 {r['k']}"

    # 案2（E1 無側街）：J≡0 → cand=K 全體 → dev tie（10 vs 10）→ 取小 k=1
    r = slot([10, 10, 10], _side(False), _side(False))
    assert all(t["J"] == 0.0 for t in r["table"]), "案2 J 應全 0"
    assert r["k"] == 1, f"案2 k* 應=1（dev 平手取小 k），實得 {r['k']}"

    # 案3（E2 單側左·首筆即飽和）：w=[20,5,5] → ΣRw_L 全 100 平坦 → dev 最小 k=1（池回居中）
    r = slot([20, 5, 5], _side(True), _side(False))
    assert r["k"] == 1, f"案3 k* 應=1（飽和平坦段取最靠中央），實得 {r['k']}"

    # 案4（E3 單側左·永不飽和）：w=[4,4,4] → J 嚴格遞增 → k*=k_max=3（池貼遠端）
    r = slot([4, 4, 4], _side(True), _side(False))
    assert r["k"] == 3, f"案4 k* 應=3（私有全擺負擔側），實得 {r['k']}"

    # 案5（E4 forced buffer）：單側左 b=10、w=[8] → ΣRw=R(18)−R(10)=28.9（自 b 起算）
    r = slot([8], _side(True, b=10.0), _side(False))
    got = round(r["table"][-1]["ΣRw_L"], 4)
    exp = round(R(18) - R(10), 4)
    assert got == exp == 28.9, f"案5 ΣRw 應={exp}（R(18)−R(10)），實得 {got}"
    assert r["k"] == 1, f"案5 k* 應=1，實得 {r['k']}"

    # 案6（E5 單筆過寬越 18m）：w=[40,5,5] 雙側 → 飽和側邊際 0 →
    #   J(1)=(100+R(10))/100=1.711 > J(2)=(100+R(5))/100=1.44 → k*=1
    r = slot([40, 5, 5], _side(True), _side(True))
    jb = {t["k"]: round(t["J"], 4) for t in r["table"]}
    assert jb == {1: 1.711, 2: 1.44}, f"案6 J 表應 {{1:1.711, 2:1.44}}，實得 {jb}"
    assert r["k"] == 1, f"案6 k* 應=1，實得 {r['k']}"

    # 案7（E6 pinned）：n=2 雙側 → K={1} 唯一（釘選街角不可被池頂掉）
    r = slot([9, 9], _side(True), _side(True))
    assert [t["k"] for t in r["table"]] == [1], f"案7 K 應=[1]，實得 {[t['k'] for t in r['table']]}"
    assert r["k"] == 1

    # 案8（E7 F×l₁ 加權·兩側皆<100%）：w=[4,4,4]、左權 2/右權 1、雙側 pin → K=[1,2]
    #   J(1)=(2·R(4)+R(8))/100=1.367、J(2)=(2·R(8)+R(4))/100=1.60 → k*=2（餵大權側；
    #   reviewer NOTE：直接鎖 k 值不依賴 J 大小關係）
    r = slot([4, 4, 4], _side(True, F=2.0, l1=1.0), _side(True, F=1.0, l1=1.0))
    jb = {t["k"]: round(t["J"], 4) for t in r["table"]}
    assert jb == {1: 1.367, 2: 1.6}, f"案8 J 表應 {{1:1.367, 2:1.6}}，實得 {jb}"
    assert r["k"] == 2, f"案8 k* 應=2（加權最大側優先），實得 {r['k']}"

    return 8


if __name__ == "__main__":
    n = run_all_cases()
    print(f"✅ W-D.2 滑池槽 golden {n}/{n} 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）")
