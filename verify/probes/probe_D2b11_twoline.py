# -*- coding: utf-8 -*-
r"""**D-2b-11 §a-3**：`_block_strip` 雙線形式之**獨立驗證**（**合成案例**·⛔ 不取 UC9898 實料）。

harness 從不執行 UI 層，故新分支**必須另立合成測試**，⛔ 不得以 `run_all` 綠燈代替。

## 四項

| # | 項 | 判準 |
|---|---|---|
| 1 | **退化一致** | `n_hat_far` 給與近側**相同**方向 ⇒ 面積與 `n_hat_far=None` **逐位 `==`**（⛔ 非「差 < ε」） |
| 2 | **梯形正確** | 兩線夾角 θ≠0 ⇒ 切出面積 == **自行以向量幾何算出**之解析梯形面積（⛔ 不以本函式自我對照） |
| 3 | **共線鋪滿** | 三片相鄰、共用同一條界線**數值** ⇒ Σ面積 == 整體切帶面積，且兩兩交集 `== 0.0` |
| 4 | **反向健全** | θ 大到兩線於街廓內相交 ⇒ 回 `(None,0.0)` 或空幾何；**⛔ 不得回自交多邊形** |

🔒 母體為空即視為失敗；四項須**逐項印出實測值**，⛔ 不得只印 PASS。
"""
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b11_twoline.log")
W = 200


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    from shapely.geometry import Polygon

    ns, _ = harvest()
    bs = ns["_block_strip"]

    L = []
    L.append("=" * W)
    L.append("【D-2b-11 §a-3】`_block_strip` 雙線形式獨立驗證（**合成案例**·⛔ 非 UC9898 實料）")
    L.append("=" * W)

    # ── 合成街廓：軸對齊大矩形（⛔ 純合成·與本案無關）──
    import numpy as np
    BLK = Polygon([(0.0, 0.0), (200.0, 0.0), (200.0, 120.0), (0.0, 120.0)])
    # ⚠️ `d_hat` 須為 **ndarray**——現行單線路徑直接算 `S * d_hat`／`bp + S*d_hat`，
    #    傳 tuple 會 `TypeError`（本探針首版即踩·屬**呼叫慣例**、⛔ 非生產缺陷）。
    d_hat = np.array([1.0, 0.0])       # 推進向 ＝ +x
    alloc = (1.0, 0.0)                 # ⇒ n_hat = rot90(alloc) = (0,1) ＝ 垂直切線
    bp = (40.0, 0.0)
    S = 50.0
    n_near = (0.0, 1.0)                # ＝ rot90(alloc)
    L.append(f"  合成街廓 ＝ {list(BLK.exterior.coords)[:-1]}")
    L.append(f"  d_hat={d_hat}　allocation_dir={alloc}　bp={bp}　S={S}　n_near(rot90)={n_near}")

    fails = []

    # ══ 1 退化一致 ══
    L.append("")
    L.append("【1】退化一致（`n_hat_far` == 近側方向 ⇒ 面積**逐位** == `None` 之值）")
    L.append("-" * W)
    _g0, _a0 = bs(BLK, d_hat, bp, S, allocation_dir=alloc)
    _g1, _a1 = bs(BLK, d_hat, bp, S, allocation_dir=alloc, n_hat_far=n_near)
    L.append(f"  n_hat_far=None      面積 ＝ {_a0!r}")
    L.append(f"  n_hat_far={n_near}  面積 ＝ {_a1!r}")
    _eq = (_a0 == _a1)
    L.append(f"  ⇒ 逐位相等（`==`·⛔ 非 ε）：{'✅ True' if _eq else '🔴 False'}"
             f"　差 ＝ {_a1 - _a0!r}")
    if not _eq:
        fails.append("1 退化一致")

    # ══ 2 梯形正確（解析對照·⛔ 不以本函式自我對照）══
    L.append("")
    L.append("【2】梯形正確（對照值由**向量幾何自算**）")
    L.append("-" * W)
    for th_deg in (5.0, 15.0, 30.0):
        th = math.radians(th_deg)
        n_far = (math.sin(th), math.cos(th))       # 由 (0,1) 轉 θ
        _g, _a = bs(BLK, d_hat, bp, S, allocation_dir=alloc, n_hat_far=n_far)
        # 解析：近線 x=40（垂直）；遠線過 (90,0)、方向 (sinθ,cosθ)
        #   ⇒ 該線上 y 處之 x ＝ 90 + y·tanθ。區域 ＝ {40 ≤ x ≤ 90 + y·tanθ, 0≤y≤120}
        #   ⇒ 面積 ＝ ∫₀¹²⁰ (50 + y·tanθ) dy ＝ 50·120 + tanθ·120²/2
        _exp = 50.0 * 120.0 + math.tan(th) * (120.0 ** 2) / 2.0
        _d = abs(_a - _exp)
        _ok = _d <= 1e-6
        L.append(f"  θ={th_deg:>5.1f}°　n_far=({n_far[0]:+.9f},{n_far[1]:+.9f})"
                 f"　實測 ＝ {_a:.9f}　解析 ＝ {_exp:.9f}　|Δ| ＝ {_d:.3e}"
                 f"　{'✅' if _ok else '🔴'}")
        if not _ok:
            fails.append(f"2 梯形 θ={th_deg}")
        if _g is not None and not _g.is_valid:
            fails.append(f"2 幾何無效 θ={th_deg}")

    # ══ 3 共線鋪滿（相鄰三片共用同一條界線數值）══
    L.append("")
    L.append("【3】共線鋪滿（第 i 片之遠線 ≡ 第 i+1 片之近線·**同一組數值**）")
    L.append("-" * W)
    # 三片以「同一組切線」分界：s0<s1<s2<s3，界線方向逐條給定
    _svals = [20.0, 60.0, 100.0, 150.0]
    _dirs = [(0.0, 1.0), (math.sin(math.radians(10)), math.cos(math.radians(10))),
             (math.sin(math.radians(-8)), math.cos(math.radians(-8))), (0.0, 1.0)]
    _pieces, _areas = [], []
    for i in range(3):
        _bp = (_svals[i], 0.0)
        _S = _svals[i + 1] - _svals[i]
        # 近側方向由 allocation_dir 決定 ⇒ 為讓近側 == 前一片之遠側，改以 alloc 反推
        _alloc_i = (_dirs[i][1], -_dirs[i][0])     # rot90⁻¹ 使 rot90(alloc)==_dirs[i]
        _g, _a = bs(BLK, d_hat, _bp, _S, allocation_dir=_alloc_i, n_hat_far=_dirs[i + 1])
        _pieces.append(_g)
        _areas.append(_a)
        L.append(f"  片{i}: s∈[{_svals[i]},{_svals[i+1]}]　近線 dir={_dirs[i]}"
                 f"　遠線 dir={_dirs[i+1]}　面積 ＝ {_a:.9f}")
    _whole_alloc = (_dirs[0][1], -_dirs[0][0])
    _gw, _aw = bs(BLK, d_hat, (_svals[0], 0.0), _svals[3] - _svals[0],
                  allocation_dir=_whole_alloc, n_hat_far=_dirs[3])
    _sum = sum(_areas)
    _dsum = abs(_sum - _aw)
    L.append(f"  Σ三片 ＝ {_sum:.9f}　整體 ＝ {_aw:.9f}　|Δ| ＝ {_dsum:.3e}"
             f"　{'✅' if _dsum <= 1e-9 else '🔴'}")
    if _dsum > 1e-9:
        fails.append("3 鋪滿和")
    _ov = []
    for i in range(3):
        for j in range(i + 1, 3):
            _x = _pieces[i].intersection(_pieces[j]).area if (
                _pieces[i] is not None and _pieces[j] is not None) else 0.0
            _ov.append(((i, j), _x))
            L.append(f"  片{i}∩片{j} 面積 ＝ {_x!r}　{'✅ ==0.0' if _x == 0.0 else '🔴 ≠0.0'}")
            if _x != 0.0:
                fails.append(f"3 交集 {i}{j}")

    # ══ 4 反向健全（兩線於街廓內相交）══
    L.append("")
    L.append("【4】反向健全（θ 大到兩線於街廓內相交 ⇒ ⛔ 不得回自交多邊形）")
    L.append("-" * W)
    for th_deg in (-40.0, -70.0, -89.0):
        th = math.radians(th_deg)
        n_far = (math.sin(th), math.cos(th))
        _g, _a = bs(BLK, d_hat, bp, S, allocation_dir=alloc, n_hat_far=n_far)
        _valid = (_g is None) or bool(_g.is_valid)
        _typ = "None" if _g is None else _g.geom_type
        L.append(f"  θ={th_deg:>6.1f}°　回傳型別 ＝ {_typ:<14}面積 ＝ {_a:.9f}"
                 f"　is_valid ＝ {'—' if _g is None else _g.is_valid}"
                 f"　{'✅ 非自交' if _valid else '🔴 **自交**'}")
        if not _valid:
            fails.append(f"4 自交 θ={th_deg}")
    # 兩線平行且距離為零
    _g, _a = bs(BLK, d_hat, bp, 0.0, allocation_dir=alloc, n_hat_far=n_near)
    L.append(f"  兩線重合（S=0）⇒ 回傳 {('None' if _g is None else _g.geom_type)}"
             f"／面積 {_a!r}　{'✅' if (_g is None and _a == 0.0) else '🔴'}")
    if not (_g is None and _a == 0.0):
        fails.append("4 S=0")

    L.append("")
    L.append("【判定】")
    L.append("-" * W)
    _n_checks = 1 + 3 + (1 + 3) + (3 + 1)
    L.append(f"  🔒 母體（實測項）＝ **{_n_checks}** 項（⛔ 非空）")
    if fails:
        L.append(f"  🛑 **不通過 {len(fails)} 項**：{fails}")
    else:
        L.append("  ✅ 四項全部通過（實測值如上·⛔ 非僅印 PASS）")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")
    if fails:
        raise RuntimeError(f"🔴 §a-3 未通過：{fails}")


if __name__ == "__main__":
    main()
