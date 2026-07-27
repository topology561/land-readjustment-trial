# -*- coding: utf-8 -*-
"""W-G.5 N-14／N-15 夾具 — **宗地最小寬度**之定義與缺件行為（KL 裁 2026-07-26）。

## 存在理由

N-15 廢止了兩個**冒充寬度**之來源：
- `S(m)`＝**剩餘正面道路可分配長**（非 §4③ 之寬度）——失敗考古 **#35 之碼版、#36 之肇因**；
- `_compute_strip_width`＝ d_hat 投影長／**MBR 短邊** fallback（未限深度帶、未沿 FRONTLINE 量）
  ⇒ **已整段刪除**（`grep -n "_compute_strip_width" app.py` 僅存「已刪」註記）。

替代＝`parcel_min_width_n14`。本夾具即其**定義正確性**與**缺件 loud** 之回歸保護。

## N-14 定義（畸零地使用規則 §4③）

最小寬度＝**自 FRONTLINE 起算、深度至法定最小深度為止**之帶內，
**二側境界線間平行 FRONTLINE 之距離**之**最小值**。

## 期望值一律**手算**（`fixture-provenance`：禁由新碼現跑回填）

| # | 幾何 | min_depth | 手算 | 理由 |
|---|---|---|---|---|
| ① | 矩形 寬5 × 深50 | 14 | **5.0** | 帶內弦長恆 5 |
| ② | 梯形 底5(t=0) → 頂1(t=20) 線性 | 14 | **2.2** | `w(t)=5−4·(t/20)`；`w(14)=5−2.8` |
| ③ | 同②，帶**超出**宗地深 | 25 | **1.0** | 帶夾至宗地深 20 ⇒ min 落 t=20 之頂寬 |
| ④ | `min_depth≤0`／座標<3 | — | **loud raise** | 缺件禁靜默兜底 |

### ③ 之要點（**一閘一事**）
帶若不夾至宗地自身深度，`t∈(20,25]` 弦長為 0 ⇒ 寬度算成 **0**
⇒ **寬度閘因「深度不足」而觸發**、與 N-11(3) **深度閘重複計**。
故量測帶 `t ∈ [0, min(min_depth, 宗地最大深)]`；深度不足由 N-11(3) 專責。

### 演算法為**精確**（非取樣）
`w(t)` 對多邊形為**分段線性** ⇒ 極小值必落於斷點
（`{0, t_hi} ∪ 各頂點於法向之投影`）⇒ 只在斷點取值。
**不做等距取樣**——取樣會產生解析度產物（見 N-12′ 深度量測之教訓）。

## 重跑
    python verify/fixture_n14_min_width.py        # rc=0 綠／rc=1 紅
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402

TOL = 1e-9


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ns, _ = harvest()
    f = ns.get("parcel_min_width_n14")
    if not callable(f):
        print("🔴 harvest 未取得 parcel_min_width_n14")
        return 1
    out, ok = [], True

    RECT = [(0, 0), (5, 0), (5, 50), (0, 50), (0, 0)]
    # 梯形：底 x∈[0,5] @t=0；頂 x∈[2,3] @t=20 ⇒ 每側各內縮 2 ⇒ w(t)=5−4(t/20)
    TRAP = [(0, 0), (5, 0), (3, 20), (2, 20), (0, 0)]

    for desc, geom, md, exp in (
        ("① 矩形 5×50", RECT, 14.0, 5.0),
        ("② 梯形 底5→頂1@t=20", TRAP, 14.0, 2.2),
        ("③ 帶超出宗地深(夾至20)", TRAP, 25.0, 1.0),
    ):
        got = f(geom, (1, 0), (0, 0), md, _label="fx")
        hit = abs(got - exp) < 1e-6
        ok &= hit
        out.append(f"  {desc:<26} min_depth={md:<5} → {got:.6f}（手算 {exp}）"
                   f"　{'✅' if hit else '🔴'}")

    for desc, args in (
        ("④a min_depth=0", (RECT, (1, 0), (0, 0), 0.0)),
        ("④b 座標<3", ([(0, 0), (1, 1)], (1, 0), (0, 0), 14.0)),
        ("④c d_hat 退化", (RECT, (0, 0), (0, 0), 14.0)),
    ):
        try:
            f(*args, _label="fx")
            ok = False
            out.append(f"  {desc:<26} → 🔴 未 raise（缺件被靜默兜底）")
        except RuntimeError:
            out.append(f"  {desc:<26} → ✅ loud raise")

    # 反例自證：舊「MBR 短邊」語意對 ② 會得 **底邊 5**（而非帶內 min 2.2）
    #   ⇒ 證本夾具測得到「是否限深度帶」，非恆真。手算：梯形 MBR 短邊 = 5（底寬）。
    _mbr_like = 5.0
    _disc = abs(f(TRAP, (1, 0), (0, 0), 14.0) - _mbr_like) > 1.0
    ok &= _disc
    out.append(f"  反例自證：N-14 值 2.2 vs 舊 MBR 短邊語意 {_mbr_like} 顯著不同 ⇒ "
               f"{'✅ 有鑑別力' if _disc else '🔴 兩者同值·無鑑別力'}")

    print("=" * 96)
    print("【N-14／N-15 夾具】宗地最小寬度（深度帶內·平行 FRONTLINE·取 min）")
    print("=" * 96)
    for ln in out:
        print(ln)
    print("-" * 96)
    print(f"RESULT: {'PASS' if ok else 'FAIL'}")
    print("=" * 96)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
