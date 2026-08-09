# -*- coding: utf-8 -*-
r"""**D-2b-16 §e-2**：`_block_partition` 鋪滿閘之**突變測試**（常設）。

## 為何需要

現行 `test_D2b15_tilegate.py` 只證「閘在**正確**分割上**不叫**」。
🔒 **一道從未被證明叫得出來的閘，不得視為已驗。** 本檔注入**已知錯誤**之分割，斷言閘**確實 raise**。

## 注入手法（⛔ 未改 `_block_partition` 本體）

以 `ns` 內之 `_strip_halfplane` 為注入點——將**指定步**之半平面沿 `d̂` **平移 δ**。
⇒ 錯誤發生於**片產生之時**、由**輸入幾何**造成，⛔ 生產碼一字未動。

## 已涵蓋之錯誤類型

| # | 類型 | 注入 | 期望 |
|---|---|---|---|
| 1 | **真重疊** | 某步 `hp⁻` 外推 δ ⇒ 片脹大、與後續片重疊 | 閘① raise·殘差 **正** |
| 2 | **真缺口** | 某步 `hp⁻` 內縮 δ ⇒ 片縮小、與後續片間留縫 | 閘① raise·殘差 **負** |
| 3 | **鏈斷（總量相消）** | 兩步之 `hp⁺` 反向平移、令 Σ 相消 | 閘① **不**足以抓·閘② raise |

🔒 **殘差正負號亦斷言**（正＝重疊、負＝缺口）——方向可辨正是本判準優於舊判準之處。

## ⛔ 未涵蓋者（⛔ 不得寫成「閘正確」）

本檔**只**證明閘對上述三類注入**有反應**。**未**涵蓋：
- 非平移型之幾何畸變（旋轉／扭曲／自交輸入）
- 多步同時錯且彼此部分相消至**小於** `1e-6` 者（該量級本即閘寬之下，設計上不抓）
- `.intersection()` 自身失效所致之錯誤（本判準**刻意不做片與片互切** ⇒ 不在其射程）
- 非 fixture 幾何上之行為（本檔母體 n = 1）
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


def _patched(ns, step_deltas):
    """回傳一個 `_strip_halfplane` 替身：對指定步之指定側，沿 d̂ 平移 δ。

    `step_deltas` ＝ {(呼叫序, keep_sign): δ}。呼叫序自 0 起（每步先 lo 後 hi）。
    """
    import numpy as np
    _orig = ns["_strip_halfplane"]
    _n = {"i": 0}
    _dh = np.asarray(C.D_HAT, dtype=float)
    _dh = _dh / float(np.linalg.norm(_dh))

    def _p(_q, _g, _keep_sign, _dh_unit, _big):
        _k = (_n["i"], float(_keep_sign))
        _n["i"] += 1
        _d = step_deltas.get(_k)
        if _d:
            _q = np.asarray(_q, dtype=float) + float(_d) * _dh
        return _orig(_q, _g, _keep_sign, _dh_unit, _big)
    return _p, _n


def _carve_measure(ns, poly, deltas):
    """以**同一**（已注入之）`_strip_halfplane` 手動削餘，取 Σ 與逐步鏈殘差（⛔ 不經閘）。"""
    import numpy as np
    hp, _ = _patched(ns, deltas)
    b = poly.bounds
    big = max(b[2] - b[0], b[3] - b[1]) * 4.0 + 100.0
    dh = np.asarray(C.D_HAT, dtype=float)
    dh = dh / float(np.linalg.norm(dh))
    rem, areas, chain = poly, [], []
    for q, g in C.LINES[1:]:
        _q = np.asarray(q, dtype=float)
        _g = np.asarray(g, dtype=float)
        _g = _g / float(np.linalg.norm(_g))
        lo = hp(_q, _g, -1.0, dh, big)
        hi = hp(_q, _g, +1.0, dh, big)
        prev = float(rem.area)
        pc = rem.intersection(lo)
        rem = rem.intersection(hi)
        areas.append(float(pc.area))
        chain.append(abs(float(pc.area) - (prev - float(rem.area))))
    areas.append(float(rem.area))
    return sum(areas) - float(poly.area), max(chain)


def _run(ns, poly, deltas, label):
    """以注入之替身跑生產 `_block_partition`；回傳 (raised, message)。"""
    _orig = ns["_strip_halfplane"]
    _p, _ = _patched(ns, deltas)
    ns["_strip_halfplane"] = _p
    try:
        ns["_block_partition"](poly, C.D_HAT, C.LINES, _label=label)
        return False, ""
    except RuntimeError as e:
        return True, str(e)
    finally:
        ns["_strip_halfplane"] = _orig


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    from shapely.geometry import Polygon
    ns, _ = harvest()
    poly = Polygon(C.BLOCK)
    fails = []

    # 呼叫序：步 i（1-based）之 lo ＝ 2(i−1)、hi ＝ 2(i−1)+1
    def _lo(i):
        return (2 * (i - 1), -1.0)

    def _hi(i):
        return (2 * (i - 1), 1.0) if False else (2 * (i - 1) + 1, 1.0)

    # ── 1 真重疊：步3 之 hp⁻ 外推 +0.05 ⇒ 片脹大 ──
    d1 = {_lo(3): +0.05}
    s1, c1 = _carve_measure(ns, poly, d1)
    r1, m1 = _run(ns, poly, d1, "mut-overlap")
    print(f"【1 真重疊】注入 步3 hp⁻ +0.05m　Σ殘差 ＝ {s1:+.9e}（期望**正**）")
    print(f"          raise ＝ {r1}　訊息：{m1[:150]}")
    if not r1:
        fails.append("1 未 raise")
    if not (s1 > TOL):
        fails.append(f"1 殘差非正（{s1:+.3e}）")
    if r1 and "鋪滿閘①" not in m1:
        fails.append(f"1 非閘①：{m1[:60]}")

    # ── 2 真缺口：步3 之 hp⁻ 內縮 −0.05 ⇒ 片縮小 ──
    d2 = {_lo(3): -0.05}
    s2, c2 = _carve_measure(ns, poly, d2)
    r2, m2 = _run(ns, poly, d2, "mut-gap")
    print(f"【2 真缺口】注入 步3 hp⁻ −0.05m　Σ殘差 ＝ {s2:+.9e}（期望**負**）")
    print(f"          raise ＝ {r2}　訊息：{m2[:150]}")
    if not r2:
        fails.append("2 未 raise")
    if not (s2 < -TOL):
        fails.append(f"2 殘差非負（{s2:+.3e}）")
    if r2 and "鋪滿閘①" not in m2:
        fails.append(f"2 非閘①：{m2[:60]}")

    # ── 3 鏈斷（總量相消）：兩步 hp⁺ 反向平移，令 Σ 相消 ⇒ 閘① 不足、閘② 須抓 ──
    #   🔑 **注意**：單一步之鏈斷**必同時**破總量（Σ 與鏈之誤差同源）
    #      ⇒ 閘② 之**獨立**鑑別力只在「**多步相消**」時才顯現。本例即造該情形。
    #   方向：步2 之 hp⁺ 外推 +a ⇒ rem₂ 變小 ⇒ Σ **減**；步4 之 hp⁺ 內縮 −b ⇒ rem₄ 變大 ⇒ Σ **增**。
    #   ⇒ Σ(b) 隨 b **遞增** ⇒ bisect 應「Σ<0 則加大 b」。（首版方向寫反、b 收斂至 0·已修）
    _a = 0.05
    _lo_d, _hi_d = 0.0, 2.0
    for _ in range(80):
        _b = (_lo_d + _hi_d) / 2.0
        _s, _ = _carve_measure(ns, poly, {_hi(2): +_a, _hi(4): -_b})
        if _s < 0:
            _lo_d = _b                        # Σ 仍負 ⇒ 需更大之 b
        else:
            _hi_d = _b
    d3 = {_hi(2): +_a, _hi(4): -_b}
    s3, c3 = _carve_measure(ns, poly, d3)
    r3, m3 = _run(ns, poly, d3, "mut-chain")
    print(f"【3 鏈斷·總量相消】注入 步2 hp⁺ +{_a}m／步4 hp⁺ −{_b:.9f}m")
    print(f"          Σ殘差 ＝ {s3:+.9e}（|Σ| ≤ 1e-6 ⇒ 閘① **抓不到**）"
          f"　逐步鏈 max ＝ {c3:.9e}")
    print(f"          raise ＝ {r3}　訊息：{m3[:150]}")
    if not r3:
        fails.append("3 未 raise")
    if r3 and "鋪滿閘②" not in m3:
        fails.append(f"3 非閘②（Σ相消後仍由①攔下？）：{m3[:80]}")
    if abs(s3) > TOL:
        print(f"          ⚠️ Σ 未能相消至閘寬內（{s3:+.3e}）⇒ 本例仍由閘① 攔下，"
              f"閘② 之獨立鑑別力**未證**")

    print()
    if fails:
        print(f"🛑 **突變測試不通過 {len(fails)} 項**：{fails}")
        return 1
    print("✅ 三類注入**皆使閘 raise**，且殘差正負號與預期一致。")
    print("   ⛔ 本結論僅及於上列三類注入（見 docstring「未涵蓋者」），"
          "⛔ 不得寫成「閘正確」。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
