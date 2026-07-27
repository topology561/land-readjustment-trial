# -*- coding: utf-8 -*-
"""W-G.5 N-14／N-15／E 系列夾具 — **宗地最小寬度**（KL 裁 2026-07-26／E 系列定稿 2026-07-27）。

## N-14 定義（畸零地使用規則 §4③）
最小寬度＝**自 FRONTLINE 起算、深度至法定最小深度為止**之帶內，
**二側境界線間平行 FRONTLINE 之距離**之**最小值**。

## 🔒 可達宗地形狀集合（KL 裁·**封閉**·夾具母體以此為準·禁再自造形狀）
| # | 形狀 | 邊序 |
|---|---|---|
| ① | 街角地第 1 宗 | FRONT → **截角** → SIDE → BASELINE → ALLOC（五邊形·含截角） |
| ② | 中間宗地（第 2 宗起） | FRONT → ALLOC → BASELINE → ALLOC（**兩側 ALLOC 平行**） |
| ③ | 末端塊 | FRONT → **街廓界(R–R)** → BASELINE → ALLOC |

**本案實測角度**（KL 由 V6.dxf 坐實·寫入正典但**禁硬編為常數**）：
`∠(ALLOC, FRONT)` **84.706°～87.395°**（**非**手冊示意圖之 90°）；
`∠(SIDE, ALLOC)` **0.000°～4.322°**（側街線與宗地分配線**不平行**）。
⇒ 幾何推論：
· ② 兩側平行 ⇒ 平行 FRONT 之弦**恆等長** ⇒ ②之最小寬度 **≡ 該宗臨街寬度**。
· ①③ 非平行四邊形 ⇒ 寬度**隨深度變化**（4.322° 於 14m 深內差約 1.05m，
  足以翻越 3.5m 門檻）⇒ ①③ **必須**跑真掃描，**禁以臨街寬度代替**。

## 🔒 E-1′～E-4 不變量守衛（量測前先驗·一律 loud raise·**禁回任何數字**）
形狀集合封閉 ⇒ 下列依作業規範**不可能發生**，發生即上游有誤。
- **E-1′** `min(t) > 1e-6` ⇒ 本宗未臨接正面路街線（⛔ 禁改為夾近端後續算）。
- **E-2′** `max(t) < min_depth` ⇒ 分配線深度不合規（手冊 二(一)3）。
  ⛔ 舊之 `_t_hi = min(min_depth, max(t))` 夾制**已撤**——它會**靜默吸收不合規分配線**。
- **E-3′** 斷點處弦非單一 `LineString` ⇒ 宗地幾何違反分配模型。
  ⛔ 舊之 `_ln.length` 總長語意**已撤**——多段加總會**製造一個不存在的寬度**。
  附註：「U 字形宗地」之讀法選項經 KL 裁定**作廢**（該形狀不可能存在）⇒ **禁實作讀法選項**。
- **E-4** `buffer(0)` 後非單一 `Polygon` ⇒ loud raise。

## 期望值一律**手算**（`fixture-provenance`：禁由新碼現跑回填）

## 重跑
    python verify/fixture_n14_min_width.py        # rc=0 綠／rc=1 紅
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402

MD = 14.0          # 法定最小深度（住宅區×8m 路寬查表值·本夾具之量測帶上界）
DEEP = 40.0        # 合成宗地深度（> MD ⇒ 滿足 E-2′）


def _mid_parcel(front_w, alloc_deg, depth=DEEP, base_deg=0.0):
    """② 中間宗地：FRONT 在 y=0（x∈[0, front_w]），兩側 ALLOC **平行**（傾角 alloc_deg），
    BASELINE 與 FRONT 夾 base_deg。回頂點序（逆時針）。"""
    _sx = math.tan(math.radians(alloc_deg))          # 每單位深度之側向位移（兩側同 ⇒ 平行）
    _by = lambda x: depth + x * math.tan(math.radians(base_deg))   # noqa: E731
    _xl_top = 0.0 + _by(0.0) * _sx
    _xr_top = front_w + _by(front_w) * _sx
    return [(0.0, 0.0), (front_w, 0.0),
            (_xr_top, _by(front_w)), (_xl_top, _by(0.0)), (0.0, 0.0)]


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

    def _chk(desc, geom, exp, md=MD, d=(1, 0), fp=(0, 0)):
        nonlocal ok
        got = f(geom, d, fp, md, _label="fx")
        hit = abs(got - exp) < 1e-6
        ok &= hit
        out.append(f"  {desc:<42} → {got:.6f}（手算 {exp}）　{'✅' if hit else '🔴'}")

    # ── ②中間宗地：三格皆須 ≡ 臨街寬度 S（證「兩側平行 ⇒ 弦恆等長」）──────────────
    S = 5.0
    _chk("① ②中間宗地·ALLOC ⊥ FRONT（傾 0°）", _mid_parcel(S, 0.0), S)
    _chk("② ②中間宗地·ALLOC 傾 5°（近本案實況）", _mid_parcel(S, 5.0), S)
    _chk("③ ②中間宗地·BASELINE 微斜 0.6°", _mid_parcel(S, 5.0, base_deg=0.6), S)

    # ── ①街角地：截角後 vs 截角前（**併存＝判別力反例**）───────────────────────
    #   手算：前寬 8、截角腿 4。
    #   截角前＝矩形 x∈[0,8] ⇒ 帶內弦恆 8.0。
    #   截角後＝切掉右下角之 (8,0)-(4,0)-(8,4) 三角形 ⇒
    #     w(t) = 8 − (4 − t)  於 t∈[0,4]（截角斜邊 x = 8−(4−t)）；t≥4 起恆 8
    #     ⇒ min 落 t=0：w(0) = 8 − 4 = **4.0**
    CHAM_AFTER = [(0.0, 0.0), (4.0, 0.0), (8.0, 4.0), (8.0, DEEP), (0.0, DEEP), (0.0, 0.0)]
    CHAM_BEFORE = [(0.0, 0.0), (8.0, 0.0), (8.0, DEEP), (0.0, DEEP), (0.0, 0.0)]
    _chk("④ ①街角地·**截角後**（前寬8·截角腿4）", CHAM_AFTER, 4.0)
    _chk("⑤ ①街角地·**截角前**（同上）", CHAM_BEFORE, 8.0)
    out.append("      ↑ ④⑤ 併存＝**判別力反例**：同一宗地截角前後差 2 倍"
               "⇒ E-7「街角宗須以截角前幾何量」非空話")

    # ── ⑥①街角地·SIDE 與 ALLOC 夾 4.322°（本案實測上界）───────────────────────
    #   手算：左界為 ALLOC 垂直線 x=0；右界為 SIDE，自 (6,0) 起向**內**傾 4.322°
    #     ⇒ 右界 x(t) = 6 − t·tan(4.322°)；w(t) = 6 − t·tan(4.322°) 遞減
    #     ⇒ min 落**帶之深端** t=MD=14：w = 6 − 14×tan(4.322°)
    _TAN = math.tan(math.radians(4.322))
    W6 = 6.0 - MD * _TAN
    SIDE_TILT = [(0.0, 0.0), (6.0, 0.0),
                 (6.0 - DEEP * _TAN, DEEP), (0.0, DEEP), (0.0, 0.0)]
    _chk(f"⑥ ①街角地·SIDE×ALLOC 4.322°（min 落深端）", SIDE_TILT, W6)
    out.append(f"      ↑ 手算 6 − 14×tan(4.322°) = {W6:.6f}"
               f"；臨街寬 6.0 ⇒ **差 {6.0 - W6:.4f}m·足以翻越 3.5m 門檻** ⇒ ①③ 必須真掃描")

    # ── ⑦③末端塊·街廓界(R–R) 斜率 ≠ ALLOC ────────────────────────────────────
    #   手算：左界 ALLOC 垂直 x=0；右界為街廓界，自 (5,0) 起**外**傾 3° ⇒ w 遞增
    #     ⇒ min 落 t=0 ＝ 臨街寬 **5.0**（外傾者最小值在近端·與⑥反向·證掃描非單點）
    _T3 = math.tan(math.radians(3.0))
    END_BLK = [(0.0, 0.0), (5.0, 0.0),
               (5.0 + DEEP * _T3, DEEP), (0.0, DEEP), (0.0, 0.0)]
    _chk("⑦ ③末端塊·街廓界外傾 3°（min 落近端）", END_BLK, 5.0)

    # ── ⑧ 不變量三格：一律 loud raise ────────────────────────────────────────
    _NOT_TOUCH = [(0.0, 2.0), (5.0, 2.0), (5.0, DEEP), (0.0, DEEP), (0.0, 2.0)]
    _TOO_SHALLOW = _mid_parcel(5.0, 0.0, depth=MD - 1.0)
    for desc, args in (
        ("⑧a E-1′ 未臨接正面路街線", (_NOT_TOUCH, (1, 0), (0, 0), MD)),
        ("⑧b E-2′ 深度 < 法定最小深", (_TOO_SHALLOW, (1, 0), (0, 0), MD)),
        ("⑧c E-4 座標<3", ([(0, 0), (1, 1)], (1, 0), (0, 0), MD)),
        ("⑧d min_depth≤0", (_mid_parcel(5.0, 0.0), (1, 0), (0, 0), 0.0)),
        ("⑧e d_hat 退化", (_mid_parcel(5.0, 0.0), (0, 0), (0, 0), MD)),
    ):
        try:
            f(*args, _label="fx")
            ok = False
            out.append(f"  {desc:<42} → 🔴 未 raise（上游錯誤被靜默吸收）")
        except RuntimeError:
            out.append(f"  {desc:<42} → ✅ loud raise")

    # ── 舊格保留（末端塊型梯形）：底5→頂1@t=20·md=14 ⇒ w(14)=5−4(14/20)=2.2 ──────
    _chk("⑨ ③末端塊型梯形 底5→頂1@t=20（舊格保留）",
         [(0, 0), (5, 0), (3, 20), (2, 20), (0, 0)], 2.2)
    out.append("      ↑ 舊「梯形超深 md=25 → 1.0」格**已改為 E-2′ raise**（見 ⑧b 同族）")

    print("=" * 104)
    print("【N-14／E-5 夾具】宗地最小寬度·母體＝可達形狀集合（①街角／②中間／③末端）")
    print("=" * 104)
    for ln in out:
        print(ln)
    print("-" * 104)
    print(f"RESULT: {'PASS' if ok else 'FAIL'}")
    print("=" * 104)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
