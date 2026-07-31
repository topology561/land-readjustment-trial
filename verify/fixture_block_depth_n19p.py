# -*- coding: utf-8 -*-
r"""K-8 §二 夾具 — **N-19′ 街廓平均深度**（KL 裁 2026-07-31·施工單更正 2026-07-31）。

## 本夾具看守什麼

`app._compute_block_depth_alloc` **是否真的實作了 N-19′、且走法定 2dp 鏈**。
在此之前，倉內唯一的 N-19′ 舉證是 `probes/probe_ruling_K8_baseline_pairing.py` §3，
但那支是**探針自己內嵌的 numpy 算式**——它證明「靶算得出來」，
**不證明 app 的取值法是它**。本夾具以 `harvest()` 取 **app 真符號**逐格對拍。

> 🔗 與 `verify/fixture_baseline_candidates.py`（C-5 三分支＋R1 共線 golden）及
> `probes/probe_ruling_K8_baseline_pairing.py`（配對輸出＋全精度 N-19′ 靶）**三者職能不重疊**：
> · `fixture_baseline_candidates` 看守**候選分支邏輯**（哪些線進候選、三分支怎麼走）
> · `probe_ruling_K8_baseline_pairing` 看守**配對輸出**與 **N-19′ 之全精度解析靶**
> · **本檔**看守 **app 取值函式**本身（2dp 鏈、診斷欄、缺件 raise、`region_min`）
> 三者**互為補集、無一取代另一**。

## N-19′ 定義（裁定 K-8 §二）

自前緣線上任一點作**垂直 BASELINE** 之直線交 BASELINE 於一點，該兩點距離為該點深度；
沿前緣線取平均。BASELINE 取**無限直線**（K-8 §一 不變式）。
前緣線與 BASELINE 皆直線 ⇒ 垂距沿弦**線性** ⇒ 平均 ＝ 中點垂距 ＝ **兩端垂距之平均**
⇒ **解析式·禁取樣**。

## 🔒 2dp 鏈（施工單 §零 更正·**本檔之核心斷言**）

`_compute_block_depth_alloc` 回傳時即 `round(D_avg, 2)`，法源＝市地重劃實施辦法 §3
（長度記至二位小數）。故：

    逐街廓乘積 ＝ round(D_avg, 2) × min_width      # R4：33.10 × 3.5 = 115.85
    region_min ＝ 各可建築街廓乘積之最小值 ＝ 115.85 @ R4
    ½ 門檻     ＝ 115.85 ÷ 2 = 57.925 → Decimal HALF_UP → 57.93

⚠️ **反例錨（T9c）**：若移除該 round 改用全精度深度，R4 得
`33.1046288875 × 3.5 = 115.8662…` → **115.87**、½ → 57.94。**二者不得混**。

## 期望值出處（`fixture-provenance`：禁由新碼現跑回填）

| 格 | 期望值來源 |
|---|---|
| T1–T5 | **手算**（合成幾何·逐格於碼旁列閉式；非由受測函式回填） |
| T4b | **解析捷徑之前提看守**：前緣線跨越 BASELINE ⇒ `\|d(t)\|` 沿弦為 V 形、
        兩端均值 ≠ 沿弦均值 ⇒ 本式不適用 ⇒ loud raise。實測六塊皆同號（見 T8） |
| T6 | 缺件語意＝施工單 §一「取不到 BASELINE ⇒ **loud raise**，禁 fallback 回方法 B」 |
| T7 | 手算（方法B 蓄意造 2 倍差 ⇒ 證其**不參與值**）＋ 方法A 診斷仍在（禁刪） |
| T8 | **K-8 段二 施工單 §六** 之 2dp 深度靶與逐街廓乘積靶 |
| T9 | 施工單 §六：`region_min = 115.85 @ R4`；½ 顯示 `57.93`（**呼叫倉內
        `wd4_tier_list._half_display` 實跑**，非算術推導） |
| T10 | 兩路深度之制度看守（見下） |

## T10：**檔案層**制度看守（🆕 K-8 §三 commit A 後語意已變·勿照舊讀）

深度原有**兩條互不相通的路徑**：app-live 走本函式；harness／baseline 直讀快照
`case_params_UC9898.json` 之 `街廓分配深度_m`。K-8 段二只換了前者 ⇒ 二路分岔。

**🆕 K-8 §三 commit A（KL 裁 2026-07-31）已使兩路同源**——`run_verification.load_snapshot()`
於**記憶體內**把該欄覆寫為現算 N-19′，故**執行期**已無分岔；但**檔案本體仍為凍結舊值**
（U-K8-1＝乙：快照留到 K-8 全案完成後一次換）。

⇒ 本格看守之對象自此**明確為「檔案」**（故讀 `rv.load_snapshot_raw()`、**不可**用
`load_snapshot()`——注入後兩邊同值，看守會靜默失效、永遠報綠）。三態：

- **制度甲＝檔案仍為凍結舊值**（commit A 後之**正常態**：執行期同源、檔案未換）
- **制度乙＝檔案已換 N-19′ 之 2dp 值**——**必須**與 v3 baseline 重烤、
  `wd4_tier_list.MINA_QU_EXPECT`／`HALF_EXPECT`、`run_verification` 名目字串**同批**完成。
- **其餘任何值 ⇒ 紅**。

⚠️ 併看守**執行期同源**（commit A 之真正標的）者為
`stepg_pipeline.assert_depth_same_source`（loud raise·非本夾具）。

## 重跑
    python verify/fixture_block_depth_n19p.py        # rc=0 綠／rc=1 紅
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from wd4_tier_list import _half_display                             # noqa: E402

# ── K-8 段二 施工單 §六 之兩張靶（**唯一真相源**·禁由本檔現跑回填）────────────────
DEPTH_2DP_TARGET = {"R1": 33.15, "R2": 44.47, "R3": 44.34,
                    "R4": 33.10, "R5": 45.71, "R6": 45.51}
PROD_TARGET = {"R1": 116.025, "R2": 155.645, "R3": 155.19,
               "R4": 115.85, "R5": 159.985, "R6": 159.285}
REGION_MIN_TARGET = 115.85
REGION_MIN_BLOCK = "R4"
HALF_DISPLAY_TARGET = 57.93
# 反例錨（T9c）：移除 round(D_avg,2) 改全精度之結果——**必須不等於**實得
REGION_MIN_IF_UNROUNDED = 115.87
HALF_IF_UNROUNDED = 57.94

# ── T10：快照深度之兩個合法制度 ──────────────────────────────────────────────
SNAP_REGIME_A = {"R1": 32.97, "R2": 43.90, "R3": 43.64,
                 "R4": 32.59, "R5": 45.04, "R6": 44.59}
SNAP_REGIME_B = dict(DEPTH_2DP_TARGET)


def _bl_pts(px, py, angle_deg, half=1.0):
    """由 (點, 角度) 造 BASELINE 之二點；`half` 為半長——N-19′ 取無限直線 ⇒ 其值不應影響結果。"""
    a = math.radians(angle_deg)
    return [(px - half * math.cos(a), py - half * math.sin(a)),
            (px + half * math.cos(a), py + half * math.sin(a))]


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ns, _fs = harvest()
    f = ns.get("_compute_block_depth_alloc")
    if not callable(f):
        print("🔴 harvest 未取得 _compute_block_depth_alloc")
        return 1

    out, ok = [], True

    def _chk(desc, got, exp, tol=1e-9, fmt="{:.6f}"):
        nonlocal ok
        hit = (got is not None) and abs(got - exp) <= tol
        ok &= hit
        out.append(f"  {desc:<50} → {fmt.format(got) if got is not None else 'None'}"
                   f"（期 {exp}）　{'✅' if hit else '🔴'}")

    def _chk_raise(desc, fn):
        """施工單 §一：缺件／幾何不合 ⇒ **loud raise**（禁回 None、禁 fallback 回方法 B）。"""
        nonlocal ok
        try:
            got = fn()
            ok = False
            out.append(f"  {desc:<50} → 🔴 未 raise，回 {repr(got)[:40]}")
        except RuntimeError as e:
            _m = str(e)
            _good = ("N-19" in _m) and ("方法 B" in _m or "方法B" in _m)
            ok &= _good
            out.append(f"  {desc:<50} → RuntimeError　{'✅' if _good else '🔴 訊息未具名'}")
        except Exception as e:                      # 非 RuntimeError ⇒ 不合契約
            ok = False
            out.append(f"  {desc:<50} → 🔴 {type(e).__name__}: {str(e)[:40]}")

    out.append("【T1–T5】合成幾何·手算對拍（回傳已 round 2dp）")
    out.append("-" * 104)

    # T1 軸對齊：BASELINE = x 軸；FRONT p1=(0,10) p2=(100,20) ⇒ d=10,20 ⇒ 平均 15
    r1 = f(None, None, None, front_pts=[(0.0, 10.0), (100.0, 20.0)],
           baseline_pts=_bl_pts(0.0, 0.0, 0.0, half=5.0))
    _chk("T1 BASELINE=x軸·前緣兩端 d=10/20 ⇒ 平均", r1["D_avg"], 15.0)
    _chk("T1b D_min（無 ALLOC ⇒ 源＝N-19′兩端·min）", r1["D_min"], 10.0)
    _chk("T1c D_max（同上·max）", r1["D_max"], 20.0)

    # T2 無限直線不變式：同一直線，半長 5→0.001 且遠移 x=−1e4（完全不在前緣投影域內）
    r2 = f(None, None, None, front_pts=[(0.0, 10.0), (100.0, 20.0)],
           baseline_pts=_bl_pts(-1.0e4, 0.0, 0.0, half=0.001))
    _chk("T2 同直線·半長 5→0.001 且遠移 x=−1e4（無限直線不變式）", r2["D_avg"], 15.0)

    # T3 量測軸＝**BASELINE 法向**（非 FRONT 法向）
    #    BASELINE 過原點·傾 30°：bn=(−sin30, cos30)=(−0.5, cos30)
    #    前緣 p1=(0,10) p2=(10,20)（整條同側）
    #      s1 = 10·cos30            = 8.6602540378
    #      s2 = −5 + 20·cos30       = 12.3205080757   ⇒ 平均 10.4903810568 → 2dp 10.49
    #    （若誤用 FRONT 法向：斜距 ＝ 垂距 / cos∠(n,bn) ⇒ 平均 10.86 ≠ 10.49 ⇒ 本格即抓）
    _c30 = math.cos(math.radians(30.0))
    _exp3 = round((10.0 * _c30 + (-5.0 + 20.0 * _c30)) / 2.0, 2)
    _FRONT3 = [(0.0, 10.0), (10.0, 20.0)]
    r3 = f(None, None, None, front_pts=_FRONT3, baseline_pts=_bl_pts(0.0, 0.0, 30.0))
    _chk("T3 BASELINE 傾 30°·量測軸須為 BASELINE 法向", r3["D_avg"], _exp3)

    # T4 線性 ⇒ 兩端平均 ≡ **中點**垂距（「禁取樣」之等價式）
    _mp = ((_FRONT3[0][0] + _FRONT3[1][0]) / 2.0, (_FRONT3[0][1] + _FRONT3[1][1]) / 2.0)
    _mid = f(None, None, None, front_pts=[_mp, _mp], baseline_pts=_bl_pts(0.0, 0.0, 30.0))
    _chk("T4 中點垂距 ≡ 兩端平均（弦上線性·解析式）", _mid["D_avg"], _exp3)

    # 🔒 T4b 解析捷徑之**前提看守**：前緣線跨越 BASELINE ⇒ loud raise
    #    p1=(0,10) s=+8.6602540378／p2=(10,0) s=−5.0（異號）
    #      · 兩端 |d| 均值 = 6.8301270189　· 中點 (5,5) 之 |d| = 1.8301270189 ⇒ 不等 ⇒ 式不適用
    _chk_raise("T4b 前緣線跨越 BASELINE（有號垂距異號）⇒ raise",
               lambda: f(None, None, None, front_pts=[(0.0, 10.0), (10.0, 0.0)],
                         baseline_pts=_bl_pts(0.0, 0.0, 30.0)))

    # T5 前緣線 ∥ BASELINE ⇒ 兩端垂距相等
    r5 = f(None, None, None, front_pts=[(0.0, 7.5), (60.0, 7.5)],
           baseline_pts=_bl_pts(0.0, 0.0, 0.0))
    _chk("T5 前緣∥BASELINE ⇒ D_min==D_max==D_avg", r5["D_avg"], 7.5)
    _chk("T5b   D_max−D_min", r5["D_max"] - r5["D_min"], 0.0)

    # ── T6 缺件 ⇒ loud raise（施工單 §一）──────────────────────────────────────
    out.append("")
    out.append("【T6】缺件 ⇒ loud raise（禁回 None、禁 fallback 回方法 B／area÷front_len）")
    out.append("-" * 104)
    _sq = [(0, 0), (100, 0), (100, 15), (0, 15), (0, 0)]
    _chk_raise("T6a 缺 BASELINE（baseline_pts=None）",
               lambda: f(_sq, 1500.0, (0, 1), front_pts=[(0.0, 10.0), (100.0, 20.0)],
                         baseline_pts=None))
    _chk_raise("T6b 缺 FRONT_LINE（front_pts=None）",
               lambda: f(_sq, 1500.0, (0, 1), front_pts=None, baseline_pts=_bl_pts(0, 0, 0)))
    _chk_raise("T6c FRONT 只有一點",
               lambda: f(_sq, 1500.0, (0, 1), front_pts=[(0.0, 10.0)],
                         baseline_pts=_bl_pts(0, 0, 0)))
    _chk_raise("T6d BASELINE 退化為點（二點重合）",
               lambda: f(_sq, 1500.0, (0, 1), front_pts=[(0.0, 10.0), (100.0, 20.0)],
                         baseline_pts=[(3.0, 4.0), (3.0, 4.0)]))
    # 反向：**有** FRONT+BASELINE 但缺 ALLOC/面積 ⇒ 值仍可算（診斷欄缺料·不編造）
    _r6e = f(None, None, None, front_pts=[(0.0, 10.0), (100.0, 20.0)],
             baseline_pts=_bl_pts(0, 0, 0))
    _chk("T6e 缺 ALLOC/面積/頂點 ⇒ N-19′ 值仍成立", _r6e["D_avg"], 15.0)
    _ok6f = (_r6e["D_avg_B"] is None) and ("N-19′兩端" in (_r6e.get("note") or ""))
    ok &= _ok6f
    out.append(f"  {'T6f   D_avg_B=None 且 note 具名 D_min/D_max 之源':<50} → "
               f"{(_r6e.get('note') or '')[:46]}　{'✅' if _ok6f else '🔴'}")

    # ── T7 方法 A／B **僅診斷·禁刪**（施工單 §一）─────────────────────────────────
    out.append("")
    out.append("【T7】方法B 不參與值；方法A 仍在（降為 D_min/D_max 診斷·禁刪）")
    out.append("-" * 104)
    #   頂點 x 跨幅 100、alloc_dir=(0,1) ⇒ n_alloc=(−1,0) ⇒ W_block=100
    #   面積蓄意給 3000 ⇒ D_avg_B = 30（＝N-19′ 15 之兩倍）
    r7 = f(_sq, 3000.0, (0, 1), front_pts=[(0.0, 10.0), (100.0, 20.0)],
           baseline_pts=_bl_pts(0, 0, 0, half=200.0))
    _chk("T7a 值 ＝ N-19′（15）而非方法B（30）", r7["D_avg"], 15.0)
    _chk("T7b 診斷欄 D_avg_B ＝ 3000/100", r7["D_avg_B"], 30.0)
    _ok7c = ("⚠️" in (r7.get("note") or "")) and ("N-19′" in (r7.get("method") or ""))
    ok &= _ok7c
    out.append(f"  {'T7c 差異大 ⇒ note 掛 ⚠️ 且 method 標 N-19′':<50} → "
               f"{(r7.get('note') or '')[:46]}　{'✅' if _ok7c else '🔴'}")
    _ok7d = ("方法A" in (r7.get("note") or ""))
    ok &= _ok7d
    out.append(f"  {'T7d 有 ALLOC ⇒ D_min/D_max 源＝方法A（診斷未被刪）':<50} → "
               f"D_min={r7['D_min']} D_max={r7['D_max']}　{'✅' if _ok7d else '🔴'}")

    # ── T8/T9 真案六塊：對施工單 §六 兩張靶 ────────────────────────────────────
    out.append("")
    out.append("【T8】V6.dxf 六街廓 vs 施工單 §六 靶（app 真符號·2dp 鏈）")
    out.append("-" * 104)
    snap = rv.load_snapshot_raw()   # 🔒 T10 制度看守須讀**檔案原值**：注入後兩邊同值＝看守靜默失效
    cb_by, cad = rv.build_pipeline(ns, _fs, snap)
    fls = cad.get("front_lines") or {}
    bls = cad.get("baselines") or {}
    prod_got = {}
    out.append(f"  {'街廓':6}{'D_avg(2dp)':>12}{'靶':>9}{'min_w':>8}"
               f"{'乘積(未round)':>16}{'靶':>12}  判")
    for blk in sorted(DEPTH_2DP_TARGET):
        fl = fls.get(blk) or {}
        bv = bls.get(blk)
        if not (fl.get("p1") and fl.get("p2") and bv):
            ok = False
            out.append(f"  {blk:6}  🔴 缺 FRONT_LINE／BASELINE")
            continue
        b = cb_by[blk]
        #   半長蓄意取 1.0m（遠短於街廓）——再證 K-8 §一 無限直線不變式於真案亦成立
        res = f(b.get("vertices") or [], float(b.get("area_m2") or 0.0),
                (cad.get("alloc_dir_by_block") or {}).get(blk),
                front_pts=[fl["p1"], fl["p2"]],
                baseline_pts=_bl_pts(bv["point"][0], bv["point"][1],
                                     float(bv["angle_deg"]), half=1.0))
        mw = float(ns["get_min_lot_size"](
            b["category"], float(snap["blocks"][blk]["正面"]["路寬_m"]))["min_width"])
        prod_got[blk] = res["D_avg"] * mw          # WARNING-B：比較用**未 round 原始乘積**
        _hit = (abs(res["D_avg"] - DEPTH_2DP_TARGET[blk]) < 1e-9
                and abs(prod_got[blk] - PROD_TARGET[blk]) < 0.01)
        ok &= _hit
        out.append(f"  {blk:6}{res['D_avg']:12.2f}{DEPTH_2DP_TARGET[blk]:9.2f}{mw:8.2f}"
                   f"{prod_got[blk]:16.5f}{PROD_TARGET[blk]:12.3f}  {'✅' if _hit else '🔴'}")

    out.append("")
    out.append("【T9】region_min ＋ ½ 門檻（實跑·非算術推導）")
    out.append("-" * 104)
    if prod_got:
        _rmin_raw = min(prod_got.values())
        _rblk = min(prod_got, key=prod_got.get)
        _rmin = round(_rmin_raw, 2)
        _ok9 = (abs(_rmin_raw - REGION_MIN_TARGET) < 0.01 and _rblk == REGION_MIN_BLOCK)
        ok &= _ok9
        out.append(f"  region_min = {_rmin_raw:.5f}（顯示 {_rmin:.2f}）@ {_rblk}"
                   f"（靶 {REGION_MIN_TARGET} @ {REGION_MIN_BLOCK}）　{'✅' if _ok9 else '🔴'}")
        _half = _half_display(_rmin)               # 倉內 wd4_tier_list 之真函式
        _ok9b = (_half == HALF_DISPLAY_TARGET)
        ok &= _ok9b
        out.append(f"  ½ 顯示 = _half_display({_rmin:.2f}) = {_half}"
                   f"（靶 {HALF_DISPLAY_TARGET}·Decimal HALF_UP）　{'✅' if _ok9b else '🔴'}")
        _ok9c = (_rmin != REGION_MIN_IF_UNROUNDED) and (_half != HALF_IF_UNROUNDED)
        ok &= _ok9c
        out.append(f"  🔒 2dp 鏈證：≠ {REGION_MIN_IF_UNROUNDED}／{HALF_IF_UNROUNDED}"
                   f"（＝移除 round(D_avg,2) 走全精度之反例值）　{'✅' if _ok9c else '🔴'}")
    else:
        ok = False
        out.append("  🔴 無乘積可算")

    # ── T10 兩路深度之制度看守 ──────────────────────────────────────────────────
    out.append("")
    out.append("【T10】現算 N-19′ vs **快照檔案原值**：檔案層制度看守"
               "（🆕 commit A 後執行期已同源·本格只看檔案）")
    out.append("-" * 104)
    _snap_d = {k: float(snap["blocks"][k]["街廓分配深度_m"]) for k in SNAP_REGIME_A}
    _is_a = all(abs(_snap_d[k] - v) < 5e-9 for k, v in SNAP_REGIME_A.items())
    _is_b = all(abs(_snap_d[k] - v) < 5e-9 for k, v in SNAP_REGIME_B.items())
    out.append(f"  {'街廓':6}{'app N-19′(2dp)':>16}{'快照檔案':>10}{'Δ':>10}")
    for k in sorted(_snap_d):
        out.append(f"  {k:6}{DEPTH_2DP_TARGET[k]:16.2f}{_snap_d[k]:10.2f}"
                   f"{DEPTH_2DP_TARGET[k] - _snap_d[k]:+10.2f}")
    if _is_a:
        out.append("  ⇒ **制度甲：檔案仍為凍結舊值**（＝K-8 §三 commit A 後之正常態）　✅")
        out.append("     **執行期已同源**：`run_verification.load_snapshot()` 於記憶體內"
                   "以現算 N-19′ 覆寫該欄（檔案零修改·U-K8-1＝乙），"
                   "逐塊同源由 `stepg_pipeline.assert_depth_same_source` loud 看守。")
        out.append("     ⇒ 引擎側 MinA_區 自 commit A 起為 **115.85**（非 114.07）。")
        out.append("     🚩 尚未做者＝**換檔＋重烤 v3 baseline**（U-K8-1＝乙·K-8 全案完成後一次換）。")
    elif _is_b:
        out.append("  ⇒ **制度乙：檔案已換 N-19′ 2dp**　✅")
        out.append("     此制度**必須**同批完成：v3 baseline 重烤 ＋ "
                   "`wd4_tier_list.MINA_QU_EXPECT` 114.07→115.85 ＋ `HALF_EXPECT` 57.04→57.93 ＋ "
                   "`run_verification` 之 `_ok_der` 與其測項名目字串。")
    else:
        ok = False
        out.append("  ⇒ 🔴 **兩制度皆不符**——快照**檔案**深度被改成第三組值。")
        out.append(f"     實得   {_snap_d}")
        out.append(f"     制度甲 {SNAP_REGIME_A}")
        out.append(f"     制度乙 {SNAP_REGIME_B}")
        out.append("     深度是 MinA／G／街角面積／PK 勝負之共同上游，**不得無聲漂移**："
                   "請確認係有意之裁定，並同批更新本夾具之制度表與下游硬錨。")

    print("=" * 104)
    print("【K-8 §二 夾具】N-19′ 街廓平均深度（垂直 BASELINE·無限直線·兩端垂距平均·解析·2dp 鏈）")
    print("=" * 104)
    for ln in out:
        print(ln)
    print("-" * 104)
    print(f"RESULT: {'PASS' if ok else 'FAIL'}")
    print("=" * 104)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
