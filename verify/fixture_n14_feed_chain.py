# -*- coding: utf-8 -*-
"""K-6-A2 段五(c)-2 **合成案** — `baseline_pts` 餵值鏈（🔒 `CLAUDE.md:56` 強制）。

## 為什麼非有本檔不可

生產之餵值鏈（`grep -n "_bl_by_jw = bl_pts_by_label" app.py`
→ `grep -n "baseline_pts=_bl_by_jw.get(_blk_jw)" app.py`）**在 `main()` 內**，
而 `harvest()` 以 AST 跳過 UI、harness 走 `verify/stepg_pipeline.run_step_g`
⇒ **`main()` 內之敘述從不被 `run_all` 執行**。
⇒ 依 `CLAUDE.md:56`：**`run_all` 之名目集合結果不得單獨作為驗收依據，必須另附合成案。**
家法比照 **GB-24**（K-9-4 閘）／**GB-25**（F-2 狀態機）。

## 本檔證什麼（⛔ 各案皆為可否證之預言）

| # | 案 | 預言 |
|---|---|---|
| ① | `bl_pts_by_label` 逐街廓映射 | 有 BASELINE 之街廓得端點對；**缺者得 `None`**（⛔ 不代判、不兜底） |
| ② | **路由正確**（本批最大風險） | 送進 `parcel_min_width_n14` 之 `baseline_pts` ＝ **該宗所屬街廓**者，⛔ 非他街廓者 |
| ③ | **查無 BASELINE ⇒ loud raise** | `_require_baseline=True` ＋ `None` ⇒ `RuntimeError`；⛔ **禁靜默回退舊帶** |
| ④ | 守衛**不誤咬早退類** | 抵費地／街角第 1 宗即使 `None` ＋ `_require_baseline=True` 亦**不得** raise |
| ⑤ | **端到端真換帶** | 同一宗地，舊帶（附表 14.0）與新帶（抵 BASELINE）之寬度**不同**，且傳入 `baseline_pts` 時得後者 |

②之作法：於 harvest 命名空間 **patch `parcel_min_width_n14`** 為記錄器
（`evaluate_parcel_width_n14` 與之共用同一 globals dict ⇒ patch 可見）。
⛔ 記錄器**比對值而非只看有無**——只看有無會讓「接錯街廓」全數漏網，
而施工單 §三-3 明指：`diff` 非空之**第一嫌疑就是餵值鏈接錯街廓**。

## 期望值之出處（`fixture-provenance`：⛔ 禁由新碼現跑回填）

⑤ 之二值係**解析手算**：宗地左界 `x=0`、右界自 `(6,0)` 向內傾 `4°`
⇒ `w(t) = 6 − t·tan(4°)`（於 `t` 遞減）⇒ min 落**帶之深端**
⇒ 舊帶 `w(14) = 6 − 14·tan(4°)`；新帶 `w(40) = 6 − 40·tan(4°)`。
（體例同 `verify/fixture_n14_min_width.py` 之案⑥。）

## 重跑

    python verify/fixture_n14_feed_chain.py        # rc=0 綠／rc=1 紅
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402

MD = 14.0            # 法定最小深度（附表值·舊帶之上界）
DEEP = 40.0          # 合成宗地深度（BASELINE 所在）
SLOPE = math.tan(math.radians(4.0))      # 右界向內之傾角（本案 SIDE/ALLOC 夾角量級）

FRONT = {'p1': (0.0, 0.0), 'p2': (10.0, 0.0)}


def _tapered_parcel():
    """左界 `x=0` 垂直、右界自 `(6,0)` 向內傾 4°、後緣在 `y=DEEP`（＝ BASELINE 上）。

    ⇒ `w(t) = 6 − t·tan(4°)` 於 `t` **嚴格遞減** ⇒ 舊帶／新帶之 min 必**不同值**
      （若二者相同，本案即失去判別力 ⇒ ⑤ 之預言不可否證）。
    """
    return [(0.0, 0.0), (6.0, 0.0),
            (6.0 - DEEP * SLOPE, DEEP), (0.0, DEEP), (0.0, 0.0)]


def _blocks():
    """二街廓：`R_A` 有 BASELINE（y=DEEP 水平）／`R_B` 有**不同**之 BASELINE／`R_C` **無**。"""
    _v = [(0.0, 0.0), (10.0, 0.0), (10.0, DEEP), (0.0, DEEP)]
    return ([{'label': 'R_A', 'vertices': _v},
             {'label': 'R_B', 'vertices': _v},
             {'label': 'R_C', 'vertices': _v}],
            {'R_A': {'point': (0.0, DEEP), 'angle_deg': 0.0},
             # 🔒 R_B 之 BASELINE **刻意不同**（平移 5m）——②之判別力全靠這個差
             'R_B': {'point': (0.0, DEEP - 5.0), 'angle_deg': 0.0}})


def _row(side='left', corner='否'):
    return {'推進側別': side, '街角地': corner, 'cut_coords': _tapered_parcel(),
            '暫編地號': 'fx-1', 'G(㎡)': 100.0}


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ns, _ = harvest()
    for _s in ('bl_pts_by_label', 'evaluate_parcel_width_n14',
               'parcel_min_width_n14', '_baseline_pts_from_manual'):
        if not callable(ns.get(_s)):
            print(f"🔴 harvest 未取得 {_s}")
            return 1
    blp = ns['bl_pts_by_label']
    ev = ns['evaluate_parcel_width_n14']
    real_pmw = ns['parcel_min_width_n14']

    out, ok = [], True

    def _say(desc, hit, detail=''):
        nonlocal ok
        ok &= bool(hit)
        out.append(f"  {desc:<56} {'✅' if hit else '🔴'}  {detail}")

    blocks, mbl = _blocks()

    # ── ① `bl_pts_by_label` 逐街廓映射（缺者得 None·⛔ 不代判）─────────────────
    bl = blp(blocks, mbl)
    _say("① 映射鍵集 ＝ 三街廓", set(bl) == {'R_A', 'R_B', 'R_C'}, f"keys={sorted(bl)}")
    _say("① R_A／R_B 得端點對", bl['R_A'] is not None and bl['R_B'] is not None)
    _say("① R_B 之端點對 ≠ R_A 之（判別力前提）", bl['R_A'] != bl['R_B'],
         f"R_A={bl['R_A'][0][1]:.1f}／R_B={bl['R_B'][0][1]:.1f}")
    _say("① **缺 BASELINE 之街廓得 `None`**（⛔ 不兜底）", bl['R_C'] is None)

    # ── ② 路由正確：送進去的是**該宗所屬街廓**之 baseline_pts ────────────────
    seen = []

    def _spy(cut_coords, d_hat, front_pt, min_depth, _label='', baseline_pts=None):
        seen.append(baseline_pts)
        return 4.0                       # 任意值·本案只驗「送了什麼」
    try:
        ns['parcel_min_width_n14'] = _spy
        for _lbl in ('R_A', 'R_B'):
            seen.clear()
            ev(_row(), FRONT, MD, 3.5, _label=f"fx/{_lbl}",
               baseline_pts=bl[_lbl], _require_baseline=True)
            _say(f"② `{_lbl}` 之呼叫確實送出 baseline_pts", len(seen) == 1 and seen[0] is not None)
            _say(f"② `{_lbl}` 送出者 ＝ **該街廓**之端點對", seen and seen[0] == bl[_lbl])
            _other = 'R_B' if _lbl == 'R_A' else 'R_A'
            _say(f"② `{_lbl}` 送出者 ≠ `{_other}` 之（⛔ 接錯街廓之反例）",
                 seen and seen[0] != bl[_other])
    finally:
        ns['parcel_min_width_n14'] = real_pmw
    _say("② patch 已還原", ns['parcel_min_width_n14'] is real_pmw)

    # ── ③ 查無 BASELINE ⇒ loud raise（⛔ 禁靜默回退舊帶）──────────────────────
    try:
        ev(_row(), FRONT, MD, 3.5, _label="fx/R_C",
           baseline_pts=bl['R_C'], _require_baseline=True)
        _say("③ 查無 BASELINE ⇒ **loud raise**", False, "未 raise ⇒ 靜默回退舊帶！")
    except RuntimeError as e:
        _say("③ 查無 BASELINE ⇒ **loud raise**", True, str(e).splitlines()[0][:56])

    # ── ③′ 對照：未 opt-in（`_require_baseline=False`）⇒ 不得 raise（沿用舊帶）──
    try:
        _r = ev(_row(), FRONT, MD, 3.5, _label="fx/legacy", baseline_pts=None)
        _say("③′ 未 opt-in ⇒ 不 raise·走舊帶（commit 2 行為保持）",
             _r.get('實際寬度(m)') is not None, f"寬度={_r.get('實際寬度(m)')}")
    except RuntimeError as e:
        _say("③′ 未 opt-in ⇒ 不 raise", False, str(e)[:56])

    # ── ④ 守衛不誤咬早退類 ────────────────────────────────────────────────────
    for _desc, _rw in (("抵費地", _row(side='抵費地')),
                       ("孤立公設地", _row(side='🟠 孤立公設地')),
                       ("街角第 1 宗", _row(corner='是'))):
        try:
            ev(_rw, FRONT, MD, 3.5, _label=f"fx/{_desc}",
               baseline_pts=None, _require_baseline=True)
            _say(f"④ `{_desc}` 即使 None＋require 亦**不得** raise", True)
        except RuntimeError as e:
            _say(f"④ `{_desc}` 即使 None＋require 亦**不得** raise", False,
                 str(e).splitlines()[0][:56])

    # ── ⑤ 端到端真換帶（**手算期望值**·⛔ 非由新碼回填）─────────────────────
    _exp_old = 6.0 - MD * SLOPE          # 舊帶：min 落 t=14
    _exp_new = 6.0 - DEEP * SLOPE        # 新帶：min 落 t=DEEP（抵 BASELINE）
    _got_old = ev(_row(), FRONT, MD, 3.5, _label="fx/old",
                  baseline_pts=None)['實際寬度(m)']
    _got_new = ev(_row(), FRONT, MD, 3.5, _label="fx/new",
                  baseline_pts=bl['R_A'], _require_baseline=True)['實際寬度(m)']
    _say("⑤ 判別力前提：二帶之手算值不同", abs(_exp_old - _exp_new) > 0.01,
         f"舊 {_exp_old:.6f} vs 新 {_exp_new:.6f}")
    _say("⑤ 舊帶 ＝ 手算 `6 − 14·tan4°`", abs(_got_old - round(_exp_old, 2)) < 1e-9,
         f"got={_got_old}／手算 {round(_exp_old, 2)}")
    _say("⑤ **新帶 ＝ 手算 `6 − 40·tan4°`**（⇒ `baseline_pts` 真的到達量測）",
         abs(_got_new - round(_exp_new, 2)) < 1e-9,
         f"got={_got_new}／手算 {round(_exp_new, 2)}")

    print("=" * 96)
    print("【K-6-A2 段五(c)-2 合成案】`baseline_pts` 餵值鏈（`main()` 內 ⇒ run_all 不執行）")
    print("=" * 96)
    print("\n".join(out))
    print("-" * 96)
    print(("✅ 合成案全綠" if ok else "🔴 合成案有紅"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
