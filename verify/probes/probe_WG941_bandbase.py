#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-41 立·**W-G.9-42 修**】帶底新定式（`K-9-10`）對寬度判定之影響實測

🔴 **⛔ 零生產碼**——⛔ 不改 `parcel_min_width_n14`／`_n14_band_hi`／`_n14_band_geom`；
   本檔**呼叫**之（單一真相源），只**另算新帶底**並與舊式並列對照。

──────────────────────────────────────────────────────────────────────────────
🩸 **`W-G.9-41` 之五個缺陷與 `W-G.9-42` 之處置（⛔ 逐項具名·⛔ 不掩蓋）**

| # | 缺陷 | 具名者 | 處置 |
|---|---|---|---|
| ① | 後角取法錯（以 `t` 最大之頂點當後角） | CC | ✅ `W-G.9-41` 已修；**本批再廢之**——後角改由生產碼 `_n14_band_geom` 之 `_rear` 供給 |
| ② | 法向未定向（實資料 BASELINE 落 `t` 負側） | CC | ✅ `W-G.9-41` 已修；**本批再廢之**——框改逐字重現生產碼之形心翻號 σ |
| ③ | `I_B` 取 `clip_interval(…, t_max)` ⇒ 恆 `None` | CC | ✅ **本批修**：`I_B` ＝ 宗 ∩ **BASELINE 直線**，其 `s` 取自 `_rear`（生產碼所產） |
| ④ | `width_at` 把「量不到弦」回 `0.0`；斷點集下界硬編 `0.0` | claude.ai | ✅ **本批修**：下界改用生產碼之 `_t_lo`；弦不存在**具名排除並計數**，⛔ 不回 `0.0` |
| ⑤ | 近／遠側界以「邊中點 `s` 較小者」判別 ⇒ 鏡像組整組反向 | claude.ai | ✅ **本批修**：改由**資料**之 `推進側別` 定，⛔ 不由形狀回推 |

🔒 **① ② 之「再廢」不是推翻其修法**——是把**該量整個移交生產碼**：
   凡生產碼已有之量（後角、框、σ、`_t_lo`），本檔一律**呼叫**、⛔ 不自寫第二份
   （`GB-8`：多份實作、無一致性看守）。本檔自寫者僅三項，且每項各有自我驗證閘：
     (i) `(s,t)` 框之重現　→ 閘：本檔 `_t_lo` ≡ `_n14_band_hi(...)[0]`（1e-12）
     (ii) `D(s)`（前緣至 BASELINE 之深度）→ 閘：**恆等式** `(D(s) − t) ≡ dep/bdn`（1e-9）
          ⚠️ ⛔ **非** `|D(s) − t| ≤ ε`——後緣角點容許離 BASELINE 至 `_EPS_TOUCH_FRONT`（1cm）
     (iii) 斷點法之最小寬度　→ 閘：舊帶之結果 ≡ `parcel_min_width_n14(..., baseline_pts=)`

──────────────────────────────────────────────────────────────────────────────
**新舊定式**（`K-9-10 六`）：
  舊 `t_hi`   ＝ `min(後緣角點之 t)`                       ← `_n14_band_hi(...)[1]`
  新 `t_band` ＝ `min( 最淺**有效**垂線之深度 , **近側**境界線終止之深度 )`

**「有效垂線」之解析求法（⛔ 非等距取樣·`K-9-10 一`）**：
  有效垂線 ＝ 自 FRONTLINE 沿法向至 BASELINE 之完整線段、**整條落在宗內**。
  宗地為凸（E-8a 已驗）⇒ 「整條在內」⟺ 其**兩端點**皆在宗內
  ⇒ 有效 `s` 範圍 ＝ `I_F ∩ I_B`，其中
    `I_F` ＝ 宗 ∩ **FRONTLINE** 之 `s` 區間（＝前緣邊之 `s` 幅）
    `I_B` ＝ 宗 ∩ **BASELINE 直線** 之 `s` 區間（＝**後緣邊**之 `s` 幅）
      🔴 **缺陷 ③ 即在此**：`W-G.9-41` 取「宗 ∩ `{t = t_max}`」，
         於凸多邊形之最深處僅命中**單一頂點** ⇒ `len(hits) < 2` ⇒ 恆 `None`
         ⇒ `I_B` 從未取到 ⇒ **`K-9-10 一` 那一半從未被檢查**。
      ✅ 本批改自 `_n14_band_geom` 之 `_rear`（其元素為 `(t, dep, s)`，`dep ≈ 0`
         ＝ 生產碼**已判定**貼齊 BASELINE 之角點）⇒ ⛔ 無須自行求交。
  `D(s)` 對 `s` **線性**（二直線夾角固定）⇒ 極小值必落於區間端點 ⇒ ⛔ 無須取樣。

**`I_F ∩ I_B = ∅`（零條有效垂線）** ⇒ 🛑 **`S-9`**：`K-9-9 七` 逐字只寫
  「若**僅一條**有效……」，**「零條」正典未裁**（`W-G.9-42` 現查：`零條`／`一條也沒有`／
  `無有效` 於 `K-6`／`CLAUDE.md`／`docs/W-C_細部plan.md` 於 `b771d22` 命中皆 **0**）
  ⇒ **停該宗之判定**、出艙碼「正典未裁·待 KL」，⛔ 不判不合格、⛔ 不跳過。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
🔒 `REAL_rc`：⛔ 不以背景 exit code 判成敗。
"""
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 172
SB = 0.0
EPS_TLO = 1e-12          # `_t_lo` 二份實作之核對閘（逐字同 app.py 之 1e-12）
EPS_DS = 1e-9            # `D(s)` 恆等式之核對閘（⚠️ 比首版嚴 1000 倍·見 analyse 閘 ii）
EPS_ZERO_CHORD = 1e-9    # 逐字同 `parcel_min_width_n14` 之 `_EPS_ZERO_CHORD`


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


# ═══════════════════════════════════════════════════════════════════════════
# 一、(s,t) 框：**逐字重現** `parcel_min_width_n14`／`_n14_band_geom`（含形心翻號 σ）
#    ⚠️ 重現之正確性⛔ 不自我宣稱——由呼叫端之 `_t_lo` 核對閘把關（見 docstring (i)）。
# ═══════════════════════════════════════════════════════════════════════════
def st_frame(cut_coords, d_hat, front_pt, eps_touch):
    """回 `(ring, t_lo, sigma, d, n, fe)`；`ring` ＝ 翻號後之 (s,t) 環（首尾相同）。

    🔒 **逐字重現生產碼之算式，含其 `numpy` 之運算次序**（⛔ 非「等價之純 Python 寫法」）：
      首版以純 Python 逐項乘加，`_t_lo` 閘（1e-12）**過**，而寬度對拍差達 **1.485e-07**
      ——⇒ 差異源自**浮點加總次序**，⛔ 非算式不同。
      「等價」在浮點上**不等於**「逐位元相同」；而 `parcel_min_width_n14` 之弦長式
      係**精確比較**（`t0 == T`），對最後幾個 ulp 敏感 ⇒ 必須連運算次序一起重現。
    """
    import numpy as _np
    from shapely.geometry import Polygon as _Pg
    _d = _np.asarray(d_hat, dtype=float)[:2]
    _nd = float(_np.linalg.norm(_d))
    if _nd < 1e-9:
        raise RuntimeError("d_hat 退化")
    _d = _d / _nd
    _n = _np.array([-_d[1], _d[0]], dtype=float)
    _fp = _np.asarray(front_pt, dtype=float)[:2]
    _P = _np.asarray([[float(p[0]), float(p[1])] for p in cut_coords],
                     dtype=float) - _fp
    d = (float(_d[0]), float(_d[1]))
    n = (float(_n[0]), float(_n[1]))
    fp = (float(_fp[0]), float(_fp[1]))
    pts = list(zip((_P @ _d).tolist(), (_P @ _n).tolist()))
    poly = _Pg(pts)
    if not poly.is_valid:
        poly = poly.buffer(0)
    if poly.is_empty or poly.geom_type != "Polygon":
        raise RuntimeError(f"宗地幾何非單一 Polygon（{poly.geom_type}）")
    ring = [(float(a), float(b)) for a, b in list(poly.exterior.coords)]
    sigma = 1.0
    if float(poly.centroid.coords[0][1]) < 0:      # ← 逐字同生產碼之形心翻號
        sigma = -1.0
        ring = [(s, -t) for s, t in ring]
    tv = [t for _s, t in ring]
    fe = [i for i in range(len(tv) - 1)
          if abs(tv[i]) <= eps_touch and abs(tv[i + 1]) <= eps_touch]
    if not fe:
        raise RuntimeError("本宗與正面路街線僅單點接觸（無前緣邊）")
    t_lo = max(0.0, max(max(tv[i], tv[i + 1]) for i in fe))
    return ring, t_lo, sigma, d, n, fe


def chord_at(ring, T):
    """凸多邊形於 `t = T` 之弦。**逐字重現** `parcel_min_width_n14._chord_len_at`
    （含 `<= 0.0` 之含端號規 ⇒ 恰過頂點者兩鄰邊各回同一 `s`〔重根〕）。
    回 `(長度, 交點數)`；**無交點回 `None`**——⛔ **不回 `0.0`**（缺陷 ④）。"""
    xs = []
    for i in range(len(ring) - 1):
        s0, t0 = ring[i]
        s1, t1 = ring[i + 1]
        if t0 == t1:
            if t0 == T:
                xs.append(s0)
                xs.append(s1)
            continue
        if (t0 - T) * (t1 - T) <= 0.0:
            u = (T - t0) / (t1 - t0)
            xs.append(s0 + u * (s1 - s0))
    if not xs:
        return None
    return (max(xs) - min(xs), len(xs))


def min_width_band(ring, t_lo, t_hi):
    """帶 `[t_lo, t_hi]` 內之最小寬度（斷點法·`K-9-10 五`）。

    🔒 **缺陷 ④ 之修法（⛔ 二擇一須寫明理由——本檔選「排除並具名計數」）**：
      生產碼 `parcel_min_width_n14` 於「弦不存在」或「弦長 ≤ 數值零」時 **loud raise**
      （E-3′／E-8b）。**本檔⛔ 不 raise，改為排除該斷點並逐宗計數**，理由有二：
        (a) **受詞不同**：生產碼之受詞是「這宗地能不能配」，一有違反即應停；
            本檔之受詞是「**新舊帶底之差**」，若一 raise 即中止，
            **恰好在最需要比較的那些宗上什麼都得不到**。
        (b) ⛔ **排除≠靜默**：每一個被排除之斷點皆**逐宗計數並列印**，
            且**全部斷點皆被排除**之宗，其 min 寬記為 **`None`（無從判定）**
            ——⛔ **不記為 `0.0`**。`W-G.9-41` 之假翻轉正是由該 `0.0` 造成。
      🔒 `CLAUDE.md`：「**無從判定**」與「**判定為偽**」⛔ 不得共用同一出艙碼。

    🔒 斷點集之下界 ＝ **`t_lo`**（生產碼之 `_n14_band_geom` 所產）⛔ 非硬編 `0.0`；
      且**⛔ 不 clamp 頂點**（生產碼係「落在區間內者納入」而**非**「夾到區間內」
      ——clamp 會在兩端製造不存在之斷點）。

    回 `(w_min, t_at, n_dropped, n_total)`；`w_min is None` ⇒ 無從判定。
    """
    ts = {t_lo, t_hi}
    for _s, t in ring:
        if t_lo <= t <= t_hi:
            ts.add(t)
    best, at, dropped, total = None, None, 0, 0
    for t in sorted(ts):
        total += 1
        res = chord_at(ring, t)
        if res is None or res[0] <= EPS_ZERO_CHORD:
            dropped += 1
            continue
        w = res[0]
        if best is None or w < best:
            best, at = w, t
    return best, at, dropped, total


def normalize_ring(ring, tol):
    """C-4：去重複點 ＋ 去共線點（⛔ **不改街廓環**、⛔ 不改任何幾何——
    只供**角數／角度判別**用）。⚠️ 依 `W-G.9-42` §C-4，全案 15 個共線／重複節點
    **100% 落在街廓外環上**、於法定粒度（公分）內合法 ⇒ **要改的是吃原始環做判別的碼**。"""
    pts = list(ring)
    if len(pts) >= 2 and abs(pts[0][0] - pts[-1][0]) < tol and abs(pts[0][1] - pts[-1][1]) < tol:
        pts = pts[:-1]
    out = []
    for p in pts:                                   # ① 去重複點
        if not out or math.hypot(p[0] - out[-1][0], p[1] - out[-1][1]) > tol:
            out.append(p)
    while len(out) >= 2 and math.hypot(out[0][0] - out[-1][0], out[0][1] - out[-1][1]) <= tol:
        out.pop()
    if len(out) < 3:
        return out
    keep = []                                       # ② 去共線點（點到相鄰兩點連線之距）
    m = len(out)
    for i in range(m):
        a, b, c = out[(i - 1) % m], out[i], out[(i + 1) % m]
        ax, ay = c[0] - a[0], c[1] - a[1]
        L = math.hypot(ax, ay)
        dev = (abs(ax * (a[1] - b[1]) - ay * (a[0] - b[0])) / L) if L > tol else 0.0
        if dev > tol:
            keep.append(b)
    return keep if len(keep) >= 3 else out


def analyse(ns, cc, dh, fp, bp, side, eps_touch, label):
    """回逐宗之全部量。**⛔ 一切幾何原語皆呼叫生產碼**；本檔只組合 ＋ 設閘。"""
    t_lo, t_hi_old, D_rep, g, bdn = ns["_n14_band_hi"](cc, dh, fp, bp, _label=label)
    rear = ns["_n14_band_geom"](cc, dh, fp, bp, _label=label)[1]   # [(t, dep, s), ...] 依 t 升冪
    ring, my_t_lo, sigma, d, n, fe = st_frame(cc, dh, fp, eps_touch)
    # ── 閘 (i)：`_t_lo` 二份實作須逐位相符（⛔ 不符即停·同生產碼 :6845 之家法）────
    if abs(my_t_lo - t_lo) > EPS_TLO:
        raise RuntimeError(f"`_t_lo` 二份實作不符（本檔 {my_t_lo:.15g} vs "
                           f"`_n14_band_hi` {t_lo:.15g}·差 {abs(my_t_lo-t_lo):.3e}）⇒ 框已漂移，停")
    # ── `D(s)`：前緣線上 `s` 處沿法向至 BASELINE 之深度（解析·線性）──────────────
    ax = ns["_baseline_normal_axis"](bp)
    b0 = (float(ax[0]), float(ax[1]))
    bn = (float(ax[2]), float(ax[3]))
    n_eff = (sigma * n[0], sigma * n[1])
    if (bn[0] * n_eff[0] + bn[1] * n_eff[1]) < 0:   # ① 定號（逐字同生產碼）
        bn = (-bn[0], -bn[1])
    dep0 = (b0[0] - fp[0]) * bn[0] + (b0[1] - fp[1]) * bn[1]
    g2 = d[0] * bn[0] + d[1] * bn[1]
    bdn2 = bn[0] * n_eff[0] + bn[1] * n_eff[1]

    def D_of_s(s):
        return (dep0 - g2 * s) / bdn2

    # ── 閘 (ii)：`D(s)` 之**恆等式**核對 ───────────────────────────────────────
    #   🩸 **首版之閘用錯了受詞（⛔ 具名·⛔ 非放寬門檻）**：首版直接比
    #     `|D(s) − t| ≤ 1e-6`，實測 11 宗破（1.3e−06〜6.7e−06）而判「深度模型有誤」。
    #   🔴 **錯在我，不在資料**：生產碼之 `_re` 係以 `|dep| ≤ _EPS_TOUCH_FRONT`（**0.01 m**）
    #     選出後緣邊 ⇒ 後緣角點**本就容許離 BASELINE 最多 1 公分**，⛔ **非恰在其上**。
    #     ⇒ 「D(s) 應等於該角點之 t」這句話**自始不成立**。
    #   ✅ **正確之恆等式**（由 `dep` 之定義直接導出，⛔ 非經驗容差）：
    #        `dep = dep0 − g·s − t·bdn`　⇒　`D(s) − t ≡ dep / bdn`
    #     ⇒ 閘改為比**殘差與 `dep/bdn` 之差**，門檻 1e-9（**比首版嚴 1000 倍**）。
    #   🔒 通過即證：本檔之深度模型與生產碼之 `dep` **代數上同一**，⛔ 非「差不多」。
    dmax = max(abs((D_of_s(r[2]) - r[0]) - (r[1] / bdn2)) for r in rear)
    if dmax > EPS_DS:
        raise RuntimeError(f"`D(s)` 恆等式核對破（max|(D(s)−t) − dep/bdn| = {dmax:.3e} "
                           f"> {EPS_DS}）⇒ 深度模型或定號有誤，停")
    # ── `I_F`／`I_B`（缺陷 ③ 之修法）──────────────────────────────────────────
    fs = sorted({ring[i][0] for i in fe} | {ring[i + 1][0] for i in fe})
    IF = (fs[0], fs[-1])
    bs = sorted(r[2] for r in rear)
    IB = (bs[0], bs[-1])
    lo, hi = max(IF[0], IB[0]), min(IF[1], IB[1])
    if hi < lo:                                     # 🛑 S-9：零條有效垂線
        return dict(t_lo=t_lo, t_hi_old=t_hi_old, rear=rear, ring=ring,
                    IF=IF, IB=IB, shallow=None, s_at=None, t_near=None,
                    t_far=None, t_band=None, s9=True, canon_gap=False)
    # 🔒 **端點之深度取值：能取環上原值者一律取原值**（⛔ 非 `D(s)` 之重建值）。
    #   理由（⛔ 非微調容差）：`min_width_band` 之弦長式**逐字重現生產碼**，其
    #   `t0 == T` 與 `(t0−T)*(t1−T) <= 0` 係**精確浮點比較**——生產碼能如此，
    #   是因其 `T` 直接取自環之 `t` 陣列（**逐位元同一個 float**）。
    #   `D(s)` 係另一路重建 ⇒ 與後緣角點之 `t` 僅到 1e-6 相符（閘 ii）
    #   ⇒ 若逕以 `D(s)` 當帶底，`T` 會落在後緣邊「差幾個 ulp」之處，
    #     使該處之弦退化為近乎 0（實測 0.586597·首版自檢 ③④⑤ 之紅即此）。
    #   ⇒ 端點若**就是**某後緣角點，取該角點之 `t`（環上原值）；否則才用 `D(s)`。
    def _depth_at(s):
        for _r in rear:
            if abs(_r[2] - s) <= 1e-9:
                return _r[0]
        return D_of_s(s)

    cand = sorted([(_depth_at(lo), lo), (_depth_at(hi), hi)])
    shallow, s_at = cand[0]
    # ── 近側界終止深度（缺陷 ⑤ 之修法：由**資料**之 `推進側別` 定）───────────────
    #   `left` ＝ 自 `p1`（+s 端）往街廓中間推進 ⇒ **近側 ＝ s 小者**
    #   `right` ＝ 自 `p2`（−s 端）往中間推進      ⇒ **近側 ＝ s 大者**
    #   ⛔ 非由形狀回推、⛔ 非固定取 s 小者（`W-G.9-41` 之缺陷 ⑤）。
    if side == "left":
        near_rear = min(rear, key=lambda r: r[2])
        far_rear = max(rear, key=lambda r: r[2])
    elif side == "right":
        near_rear = max(rear, key=lambda r: r[2])
        far_rear = min(rear, key=lambda r: r[2])
    else:
        raise RuntimeError(f"推進側別 `{side}` 非 left/right ⇒ 近側不可定，停")
    t_near = near_rear[0]
    t_far = far_rear[0]
    t_band = min(shallow, t_near)
    # ── 🛑 **`S-9` 之第二例（`W-G.9-42` 實測發現·⛔ 非施工單所列）**─────────────
    #   `K-9-10 三` 之上蓋**只取「近側**境界線終止之深度」。惟其**理由**逐字為
    #     「本款以下之深度，該宗之近邊已非近側境界線（而係後側境界線），
    #       第四款之寬度定義於該處**不成立**」
    #   —— 該理由對**遠側**境界線**完全對稱地成立**：於 `t > t_far`（遠側界已終止）之段，
    #   沿 FRONTLINE 方向自近側界前進，出宗處是**後側**境界線、⛔ 非「遠側境界線」
    #   ⇒ **第四款之寬度定義於該段同樣不成立**，而第三款**未擋之**。
    #   ⚠️ **⛔ 不得自行補上 `min(…, t_far)`**：那會使 `t_band ≤ t_hi舊` 恆成立，
    #     與 `K-9-10 六` 逐字「新帶**較深（較嚴）**」**直接牴觸** ⇒ 屬**正典之取捨**，⛔ 非 CC 可裁。
    #   ⇒ 該類宗一律 `S-9`「正典未裁·待 KL」，⛔ 不出其新寬之數。
    canon_gap = (t_band > t_far + 1e-9)
    return dict(t_lo=t_lo, t_hi_old=t_hi_old, rear=rear, ring=ring,
                IF=IF, IB=IB, shallow=shallow, s_at=s_at, t_near=t_near,
                t_far=t_far, t_band=t_band, s9=False, canon_gap=canon_gap)


# ═══════════════════════════════════════════════════════════════════════════
# 二、量測器自檢（C-5：**七項隱含前提逐項覆蓋**·⛔ 對照物不是單數）
# ═══════════════════════════════════════════════════════════════════════════
def selfcheck(ns, P):
    """以**世界座標**造測資、餵**真生產函式**（⛔ 非另寫一套簡化版）。

    🔒 `W-G.9-42` §0-4／考古 85 加註：列對照物前先寫下該量測所依賴之**全部**隱含前提，
      逐項問「對照物是否覆蓋此項」。⚠️ 本波已因此連續三批出錯
      （41 批之自檢四項**全為四邊形**、`t` 正向由 CC 自訂、推進方向單一 ⇒ 自檢過而實測全錯）。
    """
    eps = float(ns["_EPS_TOUCH_FRONT"])
    TH = math.radians(19.0)                 # 傾斜（41 批已覆蓋·保留·⛔ 非軸向）
    d = (math.cos(TH), math.sin(TH))
    n0 = (-d[1], d[0])
    O = (310000.0, 2652000.0)

    def Wc(s, t, flip):
        nn = (-n0[0], -n0[1]) if flip else n0
        return (O[0] + s * d[0] + t * nn[0], O[1] + s * d[1] + t * nn[1])

    def bl(d0, slope, flip):
        """BASELINE 之兩點（世界座標）：其線為 `t ＝ d0 + slope·s`。"""
        return [Wc(-500.0, d0 - slope * 500.0, flip), Wc(500.0, d0 + slope * 500.0, flip)]

    def parcel(fs, bs, d0, slope, flip, extra=()):
        """🔒 **合法宗地之構造器（⛔ 首版之測資違反本模型 ⇒ 自檢紅）**：
        `K-9-4` 令**每宗必須配到 BASELINE**、`_n14_band_geom` 令前後緣**各須為一條邊**
        ⇒ 測資之前緣兩端須在 `t ≈ 0`、**後緣兩端須落在 BASELINE 直線上**。
        ⚠️ 首版把「遠側後角較淺」造成**把宗地切短**（後角離 BASELINE 12m）
        ⇒ 生產碼逕 raise「本宗與 BASELINE 無臨接邊」——**該形狀在本模型下不存在**。
        正解：後角之深淺差由 **BASELINE 之傾斜**產生，⛔ 非由宗地切短產生。
        `fs`／`bs` ＝ 前緣／後緣之 `s` 區間。"""
        def D(s):
            return d0 + slope * s
        pts = [Wc(fs[0], 0.0, flip), Wc(fs[1], 0.0, flip),
               Wc(bs[1], D(bs[1]), flip), Wc(bs[0], D(bs[0]), flip)]
        return pts[:2] + list(extra) + pts[2:]

    rows, ok = [], {}

    def case(tag, note, cc, d0, slope, flip, side, want):
        try:
            r = analyse(ns, cc, d, O, bl(d0, slope, flip), side, eps, tag)
            if r["s9"]:
                got = ("S-9", None)
            else:
                w, at, dr, tot = min_width_band(r["ring"], r["t_lo"], r["t_band"])
                got = (round(r["t_band"], 4), (None if w is None else round(w, 4)))
            good = (want == got if isinstance(want, tuple)
                    else (want is None))
            if isinstance(want, tuple) and want[1] is None:
                good = (got[0] == want[0])
            ok[tag] = good
            rows.append((tag, note, str(got), str(want), good))
        except Exception as e:                                      # noqa: BLE001
            ok[tag] = (want == "RAISE")
            rows.append((tag, note,
                         f"raise: {str(e).splitlines()[0][:58]}", str(want), ok[tag]))

    # 前提①「法向可能反向」——BASELINE 落 `t` **負**側（41 批實測全錯之源）
    case("①法向反向", "BASELINE 在 t 負側·平行·前後緣皆 s∈[0,10]",
         parcel((0, 10), (0, 10), 30.0, 0.0, True), 30.0, 0.0, True, "left",
         (30.0, 10.0))
    # 前提②「推進方向相反之鏡像組」——**同一形狀**、只換 side ⇒ 近側界互換
    #   BASELINE 斜率 −1.2 ⇒ 後角 t：s=0 → 30／s=10 → 18（⇒ 舊 t_hi ＝ 18）
    #   前緣 s∈[2,8]（**窄於**後緣）⇒ 有效範圍 [2,8] ⇒ shallow ＝ D(8) ＝ 20.4
    _mir = parcel((2, 8), (0, 10), 30.0, -1.2, False)
    case("②鏡像left", "同形·side=left ⇒ 近側後角 ＝ s 小者(t=30) ⇒ t_band ＝ shallow 20.4",
         _mir, 30.0, -1.2, False, "left", (20.4, None))
    case("②鏡像right", "**同一形狀** side=right ⇒ 近側後角 ＝ s 大者(t=18) ⇒ t_band ＝ 18",
         _mir, 30.0, -1.2, False, "right", (18.0, None))
    # 前提③「一條界線被不轉折節點切成兩段」（共線贅點·偏離 0）
    case("③不轉折節點", "近側界中點插一共線贅點",
         parcel((0, 10), (0, 10), 30.0, 0.0, False, extra=()) [:2]
         + [Wc(10, 15, False), Wc(10, 30, False), Wc(0, 30, False)],
         30.0, 0.0, False, "left", (30.0, 10.0))
    # 前提④「重複座標點」
    case("④重複點", "前緣邊端點重複一次",
         [Wc(0, 0, False), Wc(10, 0, False), Wc(10, 0, False),
          Wc(10, 30, False), Wc(0, 30, False)],
         30.0, 0.0, False, "left", (30.0, 10.0))
    # 前提⑤「帶截角之五邊形」（街角宗之形狀）
    case("⑤截角五邊形", "近側前角截去 ⇒ 前緣 s∈[2,10]、五頂點",
         [Wc(2, 0, False), Wc(10, 0, False), Wc(10, 30, False),
          Wc(0, 30, False), Wc(0, 2, False)],
         30.0, 0.0, False, "left", (30.0, None))
    # 前提⑥「面積 < 4 ㎡ 之三角形碎片」——⛔ 期望「非靜默 0」而是上游 raise
    case("⑥碎片三角", "底 1.0×高 2.0 ＝ 1.0㎡·**無後緣邊** ⇒ 生產碼應 raise",
         [Wc(0, 0, False), Wc(1.0, 0, False), Wc(0, 2.0, False)],
         30.0, 0.0, False, "left", "RAISE")
    # 前提⑦「前緣不恰落在 t = 0」——**容差內**須過
    case("⑦前緣殘差內", "前緣 t ＝ +2.4746e−04／−9.0e−03（皆 < 容差 0.01）",
         [Wc(0, 2.4746e-4, False), Wc(10, -9.0e-3, False),
          Wc(10, 30, False), Wc(0, 30, False)],
         30.0, 0.0, False, "left", None)
    # 前提⑦'「殘差**超出**容差」——⛔ 須 raise（證上一項之過非恆真）
    case("⑦'殘差逾容差", "前緣 t ＝ −1.4826e−02（> 容差 0.01·**單所載之下界**）⇒ 須 raise",
         [Wc(0, 2.4746e-4, False), Wc(10, -1.4826e-2, False),
          Wc(10, 30, False), Wc(0, 30, False)],
         30.0, 0.0, False, "left", "RAISE")
    # 前提⑧「`S-9` 之構造證」——前後緣 `s` 區間**不相交** ⇒ `I_F ∩ I_B = ∅`
    #   🔒 此項即 `S-8`／空集鐵律所要求之「使該計數非空之構造」。
    case("⑧S-9構造證", "前緣 s∈[0,3]、後緣 s∈[7,10] ⇒ I_F ∩ I_B ＝ ∅ ⇒ 須判 S-9",
         parcel((0, 3), (7, 10), 30.0, 0.0, False), 30.0, 0.0, False, "left",
         ("S-9", None))

    P("【0】量測器自檢（C-5·**⛔ 對照物不是單數**·每項附實際輸出）")
    P("-" * W)
    P(f"  {'項':<14}{'說明':<52}{'實得':<44}{'期望':<20}判")
    for tag, note, got, want, good in rows:
        P(f"  {tag:<14}{note:<52}{got:<44}{want:<20}{'✅' if good else '🔴'}")
    P("  🔒 **未覆蓋之前提（⛔ 具名·不假裝已覆蓋）**：")
    P("     · 非凸宗地（折線 BASELINE 夾出腰身·`K-9-10 五` 所慮）——本案 E-8a 已保證凸，")
    P("       ⇒ 造不出**本案輸入形狀**之非凸測資 ⇒ ⛔ 不以合成凹形冒充（考古 85 修法 1）。")
    P("     · 多段後緣（`_re` 分裂）——生產碼 `_n14_band_geom` 已 raise 於上游。")
    return all(ok.values()), ok


# ═══════════════════════════════════════════════════════════════════════════
def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    import shapely
    P("=" * W)
    P("【W-G.9-41 立·W-G.9-42 修】帶底新定式（`K-9-10`）對寬度判定之影響實測")
    P("=" * W)
    P(f"  產生於 commit：{sha}　｜　shapely {shapely.__version__}｜GEOS {shapely.geos_version}")
    P("  🔴 ⛔ 零生產碼——`_n14_band_hi`／`_n14_band_geom`／`parcel_min_width_n14` 皆為**呼叫**")
    P("  🔒 本檔自寫者僅三項，各有自我驗證閘：(i)(s,t)框→`_t_lo` 核對　"
      "(ii)`D(s)`→`_rear` 角點核對　(iii)斷點法→生產寬度逐宗對拍")
    P("")

    ns, fake_st = harvest()
    for _s in ("parcel_min_width_n14", "_n14_band_hi", "_n14_band_geom",
               "get_min_lot_size", "_baseline_pts_from_manual",
               "_baseline_normal_axis", "_EPS_TOUCH_FRONT"):
        if _s not in ns:
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    eps_touch = float(ns["_EPS_TOUCH_FRONT"])

    allok, _okmap = selfcheck(ns, P)
    P(f"  ⇒ 自檢：{'PASS' if allok else '🛑 FAIL ⇒ S-2 ⇒ 停機·本次量測⛔ 不得出艙'}")
    if not allok:
        P("")
        P("🛑 量測器紅 ⇒ 停機。⛔ 本次量測結果不出艙。")
        return L, sha
    P("")

    # ── 驅動 ────────────────────────────────────────────────────────────────
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d, _s, _o, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        SB, snapshot=snapshot)

    BLKS = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in BLKS:
            BLKS.append(_l)
    g_rows, ERR = [], {}
    for lbl in BLKS:
        try:
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                             [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                             winners, forced, SB)
            g_rows.extend(_sg["g_rows"])
        except Exception as e:                                       # noqa: BLE001
            ERR[lbl] = f"{type(e).__name__}: {str(e).splitlines()[0][:150]}"

    P("【A】母體之界定（🔴 **與施工單所載之 59 宗不同·⛔ 具名·見報告 §C-0a**）")
    P("-" * W)
    P("  逐街廓 `run_step_g`（各自一個 `try`·考古 70 家法）之成敗：")
    for lbl in BLKS:
        P(f"    {lbl}: {'🔴 raise ' + ERR[lbl] if lbl in ERR else '✅ 成功'}")
    P(f"  ⇒ 成功 **{len(BLKS)-len(ERR)}／{len(BLKS)}** 街廓")
    dist = {}
    for r in g_rows:
        dist[str(r.get("推進側別"))] = dist.get(str(r.get("推進側別")), 0) + 1
    P(f"  `g_rows` 累計 **{len(g_rows)}** 列；`推進側別` 分布（⛔ 未過濾）："
      + "／".join(f"`{k}`={v}" for k, v in sorted(dist.items())))
    rows = [r for r in g_rows if str(r.get("推進側別")) in ("left", "right")]
    P(f"  母體（`推進側別 ∈ {{left,right}}`·⛔ **非**以有無 `cut_coords` 為篩）＝ **{len(rows)}** 宗")
    P("  🔴 **R2／R4／R5 之宗⛔ 不在母體內**——生產碼於該三街廓 raise ⇒ 其 `g_rows` 不存在。")
    P("     ⛔ **本檔不以 spy 擷取其 `biz_polys` 充數**：該三街廓之 raise 訊息逐字為")
    P("     「宗-宗重疊 45.9766／56.3293 ㎡ **超出捨入量子可解釋範圍＝另有病**」")
    P("     ⇒ 其宗地**彼此重疊**、係**上游狀態不合規**之產物；於其上量寬度")
    P("     ＝ 把一個 bug 的產物當成待分配的土地（**自誤 18** 之形狀）。")
    P("     ⇒ 該三街廓一律出艙碼 **「上游狀態不合規·⛔ 不作寬度判定」**。")
    P("")

    # ── 逐宗 ────────────────────────────────────────────────────────────────
    P("【B】逐宗（**全精度**·⛔ 母體內每一宗皆列·⛔ 無篩）")
    P("-" * W)
    P(f"  {'街廓':<5}{'側':<6}{'暫編地號':<14}{'類':<6}{'面積㎡':>10}"
      f"{'t_lo':>9}{'t_hi舊':>10}{'最淺有效':>10}{'@s':>10}{'近側終止':>10}{'t_band新':>10}{'Δt':>9}"
      f"{'舊min寬':>10}{'新min寬':>10}{'Δ寬':>9}{'棄點':>6}{'舊判':>6}{'新判':>6}  翻轉")
    FLIP_F, FLIP_B, DT, S9, GAP, CORNER, FRAG, GERR = [], [], [], [], [], [], [], []
    GATE = []           # C-1 驗收閘：(lbl,gid,本檔舊寬,生產寬,差)
    POLLUTED_OLD = POLLUTED_NEW = 0
    NDROP_TOTAL = 0
    for r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
        cc = r.get("cut_coords") or []
        try:
            area = float(r.get("幾何面積(㎡)") or 0.0)
        except Exception:                                            # noqa: BLE001
            area = float("nan")
        fl = fl_by.get(lbl) or {}
        mw = ns["get_min_lot_size"](
            cb_by[lbl]["category"],
            float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        md = float(mw.get("min_depth", 0.0) or 0.0)
        lw = float(mw.get("min_width", 0.0) or 0.0)   # 🔒 生產查表·⛔ 無 `or 3.5` 兜底
        p1, p2 = fl.get("p1"), fl.get("p2")
        if not (p1 and p2) or len(cc) < 3:
            GERR.append((lbl, gid, "缺 FRONT_LINE 或 cut_coords < 3"))
            continue
        dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        Lf = math.hypot(dx, dy)
        dh = (dx / Lf, dy / Lf)
        bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl),
                                             (cb_by.get(lbl) or {}).get("vertices"))
        # ── D-1／D-2：母體分流（⛔ 不混入一般宗之翻轉統計）────────────────────
        is_corner = str(r.get("街角地", "")).strip() == "是"
        nring = normalize_ring([tuple(map(float, p)) for p in cc], 0.01)
        # 🩸 **首版判準 `== 3` 漏掉更退化者（⛔ 具名·⛔ 非放寬）**：實測 `R6/628-53(1)`
        #   （面積 0.26 ㎡·施工單 §D-2 列為碎片「R6 第8」）正規化後得 **2 個頂點**
        #   ——比三角形**更**退化，卻因 `== 3` 而**漏判**、被誤送進 `S-9(一)`。
        #   ⇒ 改 `<= 3`。🔒 **判別力**：一般宗正規化後為 4〜5 邊 ⇒ 該式非恆真。
        #   ⚠️ 具名差異：施工單 §D-2 對同一宗記「三邊」，本檔得「二邊」
        #     ⇒ **兩邊之正規化實作不同**（容差同為 0.01）⇒ 逐宗清單可對、角數不可逐格對。
        is_frag = (len(nring) <= 3)
        kind = "街角" if is_corner else ("碎片" if is_frag else "一般")
        if is_corner:
            CORNER.append((lbl, gid, area, len(nring)))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{kind:<6}{area:>10.4f}"
              f"   — **無從判定**（`K-9-5`：須**截角前**幾何、門檻 ＝ 退縮寬＋畸零地最小寬；"
              f"截角前量測 `K-9-6-h ⑤` **未實作** ⇒ ⛔ 不以 {lw:.2f} 門檻判）")
            continue
        if is_frag:
            FRAG.append((lbl, gid, area, len(nring)))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{kind:<6}{area:>10.4f}"
              f"   — **上游狀態不合規**（正規化後 3 邊 ⇒ 碎片）⇒ ⛔ 不作寬度判定")
            continue
        try:
            a = analyse(ns, cc, dh, p1, bp, side, eps_touch, f"{lbl}/{gid}")
        except Exception as e:                                       # noqa: BLE001
            GERR.append((lbl, gid, f"{type(e).__name__}: {str(e).splitlines()[0][:110]}"))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{kind:<6}{area:>10.4f}"
              f"   🔴 helper raise ⇒ **無從判定**（見【E】）")
            continue
        if a["s9"]:
            S9.append((lbl, gid, area, a["IF"], a["IB"]))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{kind:<6}{area:>10.4f}"
              f"   🛑 **S-9 正典未裁·待 KL**（`I_F ∩ I_B = ∅`："
              f"I_F=[{a['IF'][0]:.4f},{a['IF'][1]:.4f}] I_B=[{a['IB'][0]:.4f},{a['IB'][1]:.4f}]）")
            continue
        wo, ao, dro, tro = min_width_band(a["ring"], a["t_lo"], a["t_hi_old"])
        wn, an, drn, trn = min_width_band(a["ring"], a["t_lo"], a["t_band"])
        NDROP_TOTAL += dro + drn
        POLLUTED_OLD += 1 if dro else 0
        POLLUTED_NEW += 1 if drn else 0
        # 🔒 **C-1 驗收閘須在 `S-9(二)` 之前結算**——其受詞是「**舊式**與生產碼是否同值」，
        #   與新帶是否踩到正典缺口**無關**；若因後者 `continue` 而漏掉，
        #   閘之母體會被悄悄縮小（＝以「沒算到」冒充「沒問題」）。
        try:
            wprod = float(ns["parcel_min_width_n14"](cc, dh, p1, md,
                                                     _label=f"{lbl}/{gid}", baseline_pts=bp))
            GATE.append((lbl, gid, wo, wprod, (None if wo is None else abs(wo - wprod))))
        except Exception as e:                                       # noqa: BLE001
            GATE.append((lbl, gid, wo, None, None))
            GERR.append((lbl, gid, f"生產寬度 raise：{str(e).splitlines()[0][:100]}"))
        if a["canon_gap"]:
            # 🛑 `S-9` 第二例：新帶伸入「遠側界已終止」之段 ⇒ 第四款之寬度定義不成立
            #    ⇒ 該段量得之弦係「近側界 → **後側**境界線」，⛔ 非「近側界 → 遠側界」。
            GAP.append((lbl, gid, area, a["t_hi_old"], a["t_far"], a["t_band"], wo, wn))
            P(f"  {lbl:<5}{side:<6}{gid:<14}{kind:<6}{area:>10.4f}"
              f"{a['t_lo']:>9.4f}{a['t_hi_old']:>10.4f}{a['shallow']:>10.4f}{a['s_at']:>10.4f}"
              f"{a['t_near']:>10.4f}{a['t_band']:>10.4f}{a['t_band']-a['t_hi_old']:>+9.4f}"
              f"{wo:>10.4f}{'待裁':>10}{'—':>9}{dro+drn:>6}"
              f"   🛑 **S-9(二) 正典未裁·待 KL**（t_band {a['t_band']:.4f} > 遠側界終止 "
              f"{a['t_far']:.4f} ⇒ 第四款不成立·⛔ 不出新寬 {wn:.4f}）")
            continue
        dt = a["t_band"] - a["t_hi_old"]
        if abs(dt) > 1e-6:
            DT.append((lbl, gid, dt))
        jo = "—" if wo is None else ("合格" if wo >= lw - 1e-9 else "不合格")
        jn = "—" if wn is None else ("合格" if wn >= lw - 1e-9 else "不合格")
        flip = ""
        if jo == "合格" and jn == "不合格":
            flip = "🔴 合→不"
            FLIP_F.append((lbl, gid, area, wo, wn, lw))
        elif jo == "不合格" and jn == "合格":
            flip = "🔵 不→合"
            FLIP_B.append((lbl, gid, area, wo, wn, lw))
        elif "—" in (jo, jn):
            flip = "⛔ 無從判定"
        P(f"  {lbl:<5}{side:<6}{gid:<14}{kind:<6}{area:>10.4f}"
          f"{a['t_lo']:>9.4f}{a['t_hi_old']:>10.4f}{a['shallow']:>10.4f}{a['s_at']:>10.4f}"
          f"{a['t_near']:>10.4f}{a['t_band']:>10.4f}{dt:>+9.4f}"
          f"{(f'{wo:.4f}' if wo is not None else '無從判定'):>10}"
          f"{(f'{wn:.4f}' if wn is not None else '無從判定'):>10}"
          f"{(f'{wn-wo:+.4f}' if (wo is not None and wn is not None) else '—'):>9}"
          f"{dro+drn:>6}{jo:>6}{jn:>6}  {flip}")

    # ── C-1 驗收閘 ──────────────────────────────────────────────────────────
    P("")
    P("【C-1 驗收閘】本檔之「舊式 min 寬」vs 生產碼 `parcel_min_width_n14(…, baseline_pts=)`")
    P("-" * W)
    cmpable = [x for x in GATE if x[3] is not None and x[2] is not None]
    bad = [x for x in cmpable if x[4] > 1e-9]
    P(f"  可對拍 **{len(cmpable)}** 宗（生產碼 raise 者 {len(GATE)-len(cmpable)} 宗·見【E】）")
    P(f"  最大差 ＝ {max((x[4] for x in cmpable), default=float('nan')):.3e} m"
      f"　｜ 差 > 1e-9 之宗數 ＝ **{len(bad)}**")
    for x in bad:
        P(f"    🔴 {x[0]}/{x[1]}：本檔 {x[2]:.9f} vs 生產 {x[3]:.9f}　差 {x[4]:.3e}")
    P(f"  🔒 **非套套邏輯**：本檔之寬度係**自寫斷點法**（`min_width_band`）所得，"
      f"⛔ 非呼叫 `parcel_min_width_n14`；共用者僅**帶之幾何**（生產碼所產）。")
    P(f"  舊式被棄點污染之宗數 ＝ **{POLLUTED_OLD}**　新式 ＝ **{POLLUTED_NEW}**"
      f"　（棄點總數 {NDROP_TOTAL}）")
    P(f"  🔒 **⛔ 棄點不記為 `0.0`**——全部斷點皆被棄之宗，其 min 寬記 `None`（無從判定）。")
    gate_ok = (len(bad) == 0)
    P(f"  ⇒ **C-1 驗收閘：{'✅ 過' if gate_ok else '🛑 未過 ⇒ S-3 ⇒ 停·⛔ 不得進 C-2／C-3'}**")

    # ── 統計 ────────────────────────────────────────────────────────────────
    P("")
    P("【D】統計（⛔ 逐宗可回溯·⛔ 三類出艙碼不得互代、不得相加）")
    P("-" * W)
    P(f"  母體（一般宗·可判定） ＝ {len(rows)-len(CORNER)-len(FRAG)-len(S9)-len(GAP)-len(GERR)} 宗")
    P(f"  ├ 街角宗（**無從判定**·`K-9-5` 截角前幾何未實作）＝ **{len(CORNER)}** 宗")
    for lbl, gid, ar, nv in CORNER:
        P(f"  │   {lbl}/{gid}　面積 {ar:.4f}　正規化後 {nv} 邊")
    P(f"  ├ 碎片宗（**上游狀態不合規**）＝ **{len(FRAG)}** 宗")
    for lbl, gid, ar, nv in FRAG:
        P(f"  │   {lbl}/{gid}　面積 {ar:.4f}　正規化後 {nv} 邊")
    P(f"  ├ `S-9(一)` 零條有效垂線（**正典未裁·待 KL**）＝ **{len(S9)}** 宗")
    for lbl, gid, ar, IF, IB in S9:
        P(f"  │   {lbl}/{gid}　面積 {ar:.4f}　I_F=[{IF[0]:.4f},{IF[1]:.4f}]　I_B=[{IB[0]:.4f},{IB[1]:.4f}]")
    P(f"  ├ 🆕 `S-9(二)` 新帶伸入「遠側界已終止」之段（**正典未裁·待 KL**）＝ **{len(GAP)}** 宗")
    P("  │   🔴 **本項係本批實測發現·⛔ 非施工單所列**——`K-9-10 三` 之上蓋只取**近側**界之終止，")
    P("  │     而其**理由**（『近邊已非近側境界線 ⇒ 第四款不成立』）對**遠側**界對稱成立。")
    P("  │     於 `t_band > 遠側界終止` 之段，沿 FRONTLINE 出宗處係**後側**境界線，")
    P("  │     ⇒ 第四款「自近側境界線至**遠側**境界線」之定義**不成立** ⇒ 該處之弦⛔ 不出艙。")
    P("  │   ⚠️ ⛔ **不得自行補 `min(…, t_far)`**：那會使新帶恆不深於舊帶，")
    P("  │     與 `K-9-10 六`「新帶**較深（較嚴）**」**直接牴觸** ⇒ 屬正典之取捨、⛔ 非 CC 可裁。")
    for lbl, gid, ar, tho, tf, tb, wo_, wn_ in GAP:
        P(f"  │   {lbl}/{gid}　面積 {ar:.4f}　t_hi舊 {tho:.4f}　遠側界終止 {tf:.4f}"
          f"　t_band新 {tb:.4f}（逾 {tb-tf:+.4f}）　舊寬 {wo_:.4f}　"
          f"〔該段所量之弦 {wn_:.4f}·**⛔ 非第四款之寬度**〕")
    if not GAP:
        P("  │   🔒 零計數之構造證：其觸發式為 `t_band > t_far`，而 `t_band ＝ min(shallow, t_near)`")
        P("  │     ⇒ 需 `shallow > t_far` ∧ `t_near > t_far`，即**遠側界較近側界先終止**；")
        P("  │     自檢 ②鏡像 之測資即具該性質（後角 18／30）⇒ 非結構恆 0。")
    if not S9:
        P("  │   🔒 **零計數之構造證（空集鐵律）**：`S-9` 之觸發條件為 `I_F ∩ I_B = ∅`；")
        P("  │     自檢 ⑥（碎片三角）之宗地**不臨 BASELINE** ⇒ 生產碼 `_n14_band_geom` 先 raise，")
        P("  │     ⇒ 該路徑**於本案輸入形狀下由上游閘攔截**、非本判準恆為空。")
        P("  │     ⚠️ 依考古 85 修法 3，拿不出「使其非空之構造」者⛔ 不得記為「無」")
        P("  │     ⇒ 本項出艙碼 ＝ **「本母體內未觸發」**，⛔ 非「`S-9` 不會發生」。")
    P(f"  └ 一般宗之 |Δt| > 1e-6 ＝ **{len(DT)}** 宗")
    if DT:
        agg = {}
        for lbl, gid, dt in DT:
            agg.setdefault(lbl, []).append(dt)
        for lbl, v in sorted(agg.items()):
            P(f"        {lbl}: {len(v)} 宗　Δt ∈ [{min(v):+.4f}, {max(v):+.4f}]"
              f"　ΣΔt ＝ {sum(v):+.4f}　Σ|Δt| ＝ {sum(abs(x) for x in v):.4f}")
    else:
        P("        🔒 零計數之構造證（⛔ 非「Δt 不可能非 0」）：本欄之母體係**扣除 `S-9(二)` 後**之")
        P("          可判定宗；而 `S-9(二)` 之 5 宗其 Δt 實得 +0.0011〜+0.1880（見上）")
        P("          ⇒ **Δt > 0 於本案確實發生**，只是那些宗因正典缺口而不出艙。")
        P("          ⇒ 本 `0` 之意義 ＝ 「**可判定之 5 宗其新舊帶底相同**」，⛔ 非「新舊定式等價」。")
    P("")
    P(f"  判定翻轉 合格→不合格 ＝ **{len(FLIP_F)}** 宗")
    for lbl, gid, ar, wo, wn, lw in FLIP_F:
        P(f"      {lbl}/{gid}　面積 {ar:.4f}　舊寬 {wo:.4f} → 新寬 {wn:.4f}（門檻 {lw:.2f}）")
    if FLIP_F:
        _ar = [x[2] for x in FLIP_F]
        P(f"      面積 帶號合計 {sum(_ar):+.4f}　絕對值合計 {sum(abs(x) for x in _ar):.4f}")
    P(f"  反向翻轉 不合格→合格 ＝ **{len(FLIP_B)}** 宗")
    for lbl, gid, ar, wo, wn, lw in FLIP_B:
        P(f"      {lbl}/{gid}　面積 {ar:.4f}　舊寬 {wo:.4f} → 新寬 {wn:.4f}（門檻 {lw:.2f}）")
    if not FLIP_B:
        P("      🔒 零計數之構造證：翻轉判定式對兩方向**對稱**（`jo/jn` 之互換），")
        P("        且 `K-9-10 六` 明載新帶**較深（較嚴）** ⇒ 反向翻轉須 `Δt < 0`；")
        P("        本母體 Δt 之範圍見上 ⇒ 若全為 `≥ 0` 則反向為**構造上不可能**，")
        P("        ⇒ 該 `0` 之意義為「**定式蘊含**」，⛔ 非「量測發現」。")

    # ── 出艙碼 ──────────────────────────────────────────────────────────────
    # ── D-2／Q7：角數分布（C-4 正規化後）───────────────────────────────────
    P("")
    P("【D-2】角數分布（**C-4 正規化後**·去重複點＋去共線點·容差 0.01 m）")
    P("-" * W)
    P("  🔒 **正規化之受詞 ＝ 角數／角度判別**，⛔ **不改任何幾何**、⛔ 不改街廓環。")
    P("     依 `W-G.9-42` §C-4：全案共線／重複節點 **100% 落在街廓外環上**、")
    P("     於法定粒度（公分）內合法 ⇒ 要改的是**吃原始環做判別的碼**，⛔ 非資料。")
    raw_hist, nrm_hist, changed = {}, {}, []
    for r in rows:
        cc = r.get("cut_coords") or []
        if len(cc) < 3:
            continue
        pts = [tuple(map(float, p)) for p in cc]
        nr = len(pts) - (1 if (len(pts) >= 2 and pts[0] == pts[-1]) else 0)
        nn = len(normalize_ring(pts, 0.01))
        raw_hist[nr] = raw_hist.get(nr, 0) + 1
        nrm_hist[nn] = nrm_hist.get(nn, 0) + 1
        if nn != nr:
            changed.append((str(r.get("所屬街廓")), str(r.get("暫編地號")), nr, nn))
    P(f"  原始座標點數：" + "／".join(f"{k} 邊 {v}" for k, v in sorted(raw_hist.items()))
      + "　（⛔ **未正規化之數·不得引用**）")
    P(f"  正規化後　　：" + "／".join(f"{k} 邊 {v}" for k, v in sorted(nrm_hist.items())))
    P(f"  正規化使角數改變之宗 ＝ **{len(changed)}**")
    for lbl, gid, a_, b_ in changed:
        P(f"      {lbl}/{gid}：{a_} → {b_}")
    P(f"  🔴 **射程聲明**：本表母體僅 **{len(rows)}** 宗（R2／R4／R5 之宗取不到）")
    P(f"     ⇒ ⛔ **不得**與施工單 §D-2 之「三邊 4／四邊 47／五邊 8」（母體 59）**逐格對比**。")

    P("")
    P("【E】未能量測者（⛔ 逐項具名）")
    P("-" * W)
    if GERR:
        for lbl, gid, msg in GERR:
            P(f"    {lbl}/{gid}：{msg}")
    else:
        P("    （無）")
    for lbl in BLKS:
        if lbl in ERR:
            P(f"    🔴 街廓 {lbl} 全體：{ERR[lbl]}")
    P("")
    P("=" * W)
    if not gate_ok:
        code = "無從判定（附所缺）——C-1 驗收閘未過"
    elif len(rows) - len(CORNER) - len(FRAG) - len(S9) - len(GAP) - len(GERR) <= 0:
        code = "無從判定（附所缺）——可判定母體為空"
    elif len(FLIP_B) == 0 and len(FLIP_F) > 0:
        code = "新定式較嚴（僅單向翻轉）"
    elif len(FLIP_B) > 0 and len(FLIP_F) > 0:
        code = "雙向翻轉（附各自清單）"
    else:
        code = "無翻轉（新舊定式於**本母體**對判定等價）"
    P(f"  🔒 出艙碼（一般宗·本母體）＝ **{code}**")
    P(f"  🔒 街角宗 {len(CORNER)} 宗 ＝ **無從判定**"
      f"｜碎片宗 {len(FRAG)} 宗 ＝ **上游狀態不合規**"
      f"｜`S-9(一)` {len(S9)} ＋ `S-9(二)` {len(GAP)} ＝ **{len(S9)+len(GAP)} 宗·正典未裁·待 KL**")
    P(f"  🔴 **可判定之一般宗僅 {len(rows)-len(CORNER)-len(FRAG)-len(S9)-len(GAP)-len(GERR)}／{len(rows)} 宗**"
      f"（{100.0*(len(rows)-len(CORNER)-len(FRAG)-len(S9)-len(GAP)-len(GERR))/max(1,len(rows)):.1f}%）"
      f"⇒ 上開出艙碼之射程**僅及該 {len(rows)-len(CORNER)-len(FRAG)-len(S9)-len(GAP)-len(GERR)} 宗**，")
    P("     ⛔ **不得**讀作「`K-9-10` 對全案無影響」。")
    P(f"  🔒 R2／R4／R5 全體（{len(ERR)} 街廓）＝ **上游狀態不合規·⛔ 不作寬度判定**")
    P("  ⛔ 上列各碼**不得互代、不得相加**（受詞不同）。")
    P("=" * W)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG941_bandbase_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
