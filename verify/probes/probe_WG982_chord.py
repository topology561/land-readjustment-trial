# -*- coding: utf-8 -*-
r"""**W-G.9-82 §二 A 組**：**弦區間閉式**——把必要條件推成充要，且仍⛔ 不先算交點。

## 受詞（施工單 `W-G.9-82` §二·`VR-040` 四）
> **在內 ⟺ `s* ∈ [λ_a, λ_b]`**，其中（`û_j` 為單位向量·`n_e` 為街廓邊 `e` 之**外向單位法向**）
> `λ_b = min{ ⟨q_e−p_j, n_e⟩ / ⟨û_j, n_e⟩ : ⟨û_j, n_e⟩ > 0 }`
> `λ_a = max{ ⟨q_e−p_j, n_e⟩ / ⟨û_j, n_e⟩ : ⟨û_j, n_e⟩ < 0 }`

- **A-1** `[λ_a, λ_b]` 之構造（⛔ 純算術·⛔ 不得用 `intersection()`／`contains()`）＋**方形街廓判別力**。
- **A-2** 弦區間謂詞於 **86 真實對** ＋ **144 掃描列**之驗證＋**邊界擦邊類**＋**負對照**（外接盒式須仍 34）。
- **A-3** 「**不先算交點**」之**碼面自證**（shim 計數·⛔ 非讀碼推定）。
- **A-4** `0m R3` 之**真實餘裕**（`s* − λ_b`）與 `3.4192` 對帳。
- **A-5** 補完 `-81` 二項：例外類 **6** 對逐對列出／乙類 **36** 對之幾何定位。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本探針欲證「弦區間式為**充要**」。其瑕若使 `[λ_a, λ_b]` **偏窄** ⇒ 多判「在外」
⇒ 與真實 86 對中之在內者衝突 ⇒ **會吵**。偏寬 ⇒ 多判「在內」⇒ 與現行外接盒式同病 ⇒ **較安靜**。
🔒 **事前選定：偏向使 `[λ_a, λ_b]` 偏窄**——落實為三條，⛔ 逐條具名：
  (甲) 邊之**外向性**若與代表點檢查不合 ⇒ 該邊之界**照取**（⛔ 不丟棄該約束）並具名；
  (乙) `|⟨û_j,n_e⟩| ≤ TOL_DEN` 之**平行邊**：`⟨q_e−p_j,n_e⟩ < TOL_NUM` ⇒ 判**空區間**（最緊）；
  (丙) 零長邊／重複頂點 ⇒ **跳過並計數**（⛔ 不臆造法向）。

## 🔒 恆等式（承 `W-G.9-80`／`-81`·`VR-039` 二判為坐實·⛔ 中途不換）
```
s*   = d_signed / sinα          d_signed = cross(p_k − p_j, û_k)   sinα = cross(û_j, û_k)
t_X  = t(p_j) + s* · ⟨û_j, n̂⟩                    n̂ = rot90(m̂)
```
🔒 `s*` 為**沿 `û_j`（單位）自 `p_j` 起算之世界座標公尺數** ⇒ 與 `λ_a`／`λ_b` **同一參數軸**。

## 🔒 施工單 §四 之 `P1`〜`P8`（⛔ **逐字保留**·事後不得調整）
```
P1  §Z 三塊之 bytes／LF／sha256 逐塊相符 ⇒ 3／3
P2  A-1 之 p_j 內含性：12 格之每一街角宗皆 λ_a < 0 < λ_b。⛔ 否者逐項具名
P3  A-2 之弦區間謂詞與 block.contains 於 86 真實對：對稱差 ＝ 空集（邊界擦邊類另計）
P4  A-2 之掃描 144 列不一致 ＝ 0；負對照（外接盒式）須仍為 34。
    ⛔ 若弦區間式亦為 34 ⇒ VR-040 四之推導證偽·具名
P5  A-3：弦區間計算次數 ＝ 街角宗總數（⛔ ≠ 86）；謂詞路徑之 _line_cross／.intersection(／
    .contains( 呼叫 ＝ 0；驗證端之 contains 呼叫 > 0
P6  A-5-2：36 對乙類之約束邊皆⛔ 非軸向邊 ⇒「被 4 條軸向邊放進來」之說成立。
    ⛔ 若有任一對之約束邊為軸向 ⇒ 該說不全·具名
P7  A-4：0m R3 (7,9) 之 s* − λ_b ≥ 3.4192 / ⟨û_j,n̂⟩
P8  app.py blob 仍 a9e5671d…；docs/rulings/ 0；verify/baselines/ 0；verify/**.py 變更 2；
    run_all ＝ 15（第八法）；run_all.py blob 逐位相同
```

## 🔒 常設條款之落實
- **第 8 條**（會使它為否之具體輸入）：`selfcheck` ⑤／⑥ 各給一個**實得為否**之輸入與其實得值。
- **第 9 條**（門檻須併出艙量級與 `ulp`）：本檔三個門檻 `TOL_DEN`／`TOL_NUM`／`TOL_GRAZE`
  皆於 `【0】` 印出其**被測量之量級範圍**與該範圍上端之 `math.ulp`；殘差一律併印 `殘差/ulp`。
- **第 10 條**（表尾機器可讀母體）：每表末印 `POPULATION= / PRINTED= / SUPPRESSED=`。
- **第 11 條**（修法須列適用之**動作清單**）：本檔之「⛔ 不經 shell 傳含反斜線之內容」
  **適用動作 ＝ 讀 ＋ 寫**——本檔係以 `Write` 工具落盤，⛔ 未經 heredoc。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修任何生產碼；⛔ 不修 `②-宗` 閘／不調上界／不改 `near_dir`；
⛔ 不重烤／不換圖；⛔ 不以擬合代替恆等式；⛔ 不 shim `S`；⛔ 不接入 `run_all`；
⛔ 不下「這是 bug」之結論。
"""
import contextlib
import io
import math
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

import shapely                                                      # noqa: E402
from shapely.geometry.base import BaseGeometry                      # noqa: E402
from shapely.geometry import Polygon as SPoly                       # noqa: E402

# 🔒 §五 備料：直接沿用 `W-G.9-81` 之**同一支**量測器（⛔ 不另造第二份 ⇒ 負對照可比）
import probe_WG981_scope as w81                                     # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210

# ── 門檻（🔒 常設第 9 條：量級與 ulp 於【0】出艙）──────────────────────────────
TOL_DEN = 1e-12      # |⟨û_j, n_e⟩|：二單位向量之內積 ⇒ 量級 [0, 1]
TOL_NUM = 0.0        # ⟨q_e−p_j, n_e⟩：公尺 ⇒ 量級 [0, 1e3]；A-0(乙) 取 `< TOL_NUM` 為空
TOL_LEN = 1e-12      # 零長邊
TOL_GRAZE = 1e-9     # 相對擦邊門檻（施工單 A-2 所令）
TOL_AXIS = 1e-9      # 軸向邊：|⟨ê, m̂⟩| 或 |⟨ê, n̂⟩| ≤ 之


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG982_chord_%s.log" % COMMIT)

_u = w81._u
_rot90 = w81._rot90
_ulp_ratio = w81._ulp_ratio


# ═══ A-3 之計數 shim（🔒 以 shim 計數·⛔ 非讀碼推定）═════════════════════════
CNT = {"line_cross": 0, "intersection": 0, "contains": 0}
_ORIG = {}


def _reset_cnt():
    for k in CNT:
        CNT[k] = 0


def _snapshot_cnt():
    return dict(CNT)


def patch_on():
    """🔒 只於**分析階段**掛（⛔ 不掛在管線驅動期）——否則計數混入生產碼之呼叫。"""
    if _ORIG:
        return
    _ORIG["line_cross"] = w81._line_cross
    _ORIG["intersection"] = BaseGeometry.intersection
    _ORIG["contains"] = BaseGeometry.contains

    def _lc(*a, **kw):
        CNT["line_cross"] += 1
        return _ORIG["line_cross"](*a, **kw)

    def _inter(self, other, **kw):
        CNT["intersection"] += 1
        return _ORIG["intersection"](self, other, **kw)

    def _cont(self, other):
        CNT["contains"] += 1
        return _ORIG["contains"](self, other)

    w81._line_cross = _lc
    BaseGeometry.intersection = _inter
    BaseGeometry.contains = _cont


def patch_off():
    if not _ORIG:
        return
    w81._line_cross = _ORIG["line_cross"]
    BaseGeometry.intersection = _ORIG["intersection"]
    BaseGeometry.contains = _ORIG["contains"]
    _ORIG.clear()


# ═══ A-1 之構造（⛔ 純算術·⛔ 零 shapely）═══════════════════════════════════
def ring_edges(xy):
    """由**環之頂點序列**造 `[(i, q, n_hat, e_hat, seg_len)]`；外向法向由**帶號面積**定。

    🔒 ⛔ 不用 `shapely`；🔒 ⛔ 不用代表點來**決定**方向（代表點只用來**驗**）。
    回 `(edges, diag)`；`diag` 含零長邊數、帶號面積、質心。
    """
    pts = [(float(c[0]), float(c[1])) for c in xy]
    if len(pts) >= 2 and abs(pts[0][0] - pts[-1][0]) < 1e-15 and abs(pts[0][1] - pts[-1][1]) < 1e-15:
        pts = pts[:-1]
    n = len(pts)
    a2 = 0.0
    cx = cy = 0.0
    for i in range(n):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % n]
        cr = x0 * y1 - x1 * y0
        a2 += cr
        cx += (x0 + x1) * cr
        cy += (y0 + y1) * cr
    sgn = 1.0 if a2 > 0 else -1.0
    cen = (cx / (3.0 * a2), cy / (3.0 * a2)) if abs(a2) > 1e-15 else (float("nan"),) * 2
    edges = []
    ndeg = 0
    for i in range(n):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % n]
        ex, ey = x1 - x0, y1 - y0
        L = math.hypot(ex, ey)
        if L <= TOL_LEN:
            ndeg += 1
            continue
        nx, ny = sgn * ey / L, -sgn * ex / L          # CCW ⇒ (e_y, −e_x)；CW ⇒ 反號
        edges.append((i, np.array([x0, y0]), np.array([nx, ny]),
                      np.array([ex / L, ey / L]), L))
    return edges, {"n_vert": n, "signed_area2": a2, "orient": "CCW" if sgn > 0 else "CW",
                   "centroid": np.array(cen), "n_degenerate": ndeg}


def outward_check(edges, rep):
    """🔒 A-1 所令：以街廓**代表點**驗 `⟨rep − q_e, n_e⟩ ≤ 0` 對全部邊成立。"""
    vals = [float(np.dot(np.asarray(rep, float)[:2] - q, nh)) for _i, q, nh, _e, _L in edges]
    return (max(vals) if vals else float("nan")), vals


PLAIN_VIOL = {"n": 0, "why": [], "calls": 0}


def _assert_plain(edges, p, u):
    """🔒 A-3-④ 之**機械證**：`chord_interval` 之三個實參⛔ 不得含幾何物件。

    判準逐字：凡具 `geom_type`／`exterior`／`coords` 屬性者即計為違反（shapely 之三個標記）。
    🔒 **判別力**：`selfcheck` ⑧ 以一個**真的** shapely 物件餵入 ⇒ 本計數須 +1。
    """
    PLAIN_VIOL["calls"] += 1
    bad = []
    for obj, nm in ((p, "p"), (u, "u")):
        if any(hasattr(obj, a) for a in ("geom_type", "exterior", "coords")):
            bad.append(nm)
    for it in (edges or []):
        for x in it[1:4]:
            if any(hasattr(x, a) for a in ("geom_type", "exterior", "coords")):
                bad.append("edges")
                break
    if bad:
        PLAIN_VIOL["n"] += 1
        PLAIN_VIOL["why"].append(tuple(sorted(set(bad))))
    return not bad


def chord_interval(edges, p, u):
    """🔴 **本檔之受詞**：一條直線 `p + s·u` 於凸多邊形內之**參數區間** `[λ_a, λ_b]`。

    ⛔ **純算術**：只用 `edges`（構造量）、`p`、`u`。⛔ 無 `intersection()`／`contains()`／交點。
    回 dict：`lam_a`／`lam_b`／`ia`／`ib`／`empty`／`rows`（逐邊）／平行邊統計。
    """
    _assert_plain(edges, p, u)
    p = np.asarray(p, float)[:2]
    u = np.asarray(u, float)[:2]
    lam_a, lam_b = -math.inf, math.inf
    ia = ib = None
    empty = False
    par_free = par_block = 0
    rows = []
    for i, q, nh, eh, L in edges:
        den = float(np.dot(u, nh))
        num = float(np.dot(q - p, nh))
        kind = ""
        lam = float("nan")
        if den > TOL_DEN:
            lam = num / den
            kind = "上界"
            if lam < lam_b:
                lam_b, ib = lam, i
        elif den < -TOL_DEN:
            lam = num / den
            kind = "下界"
            if lam > lam_a:
                lam_a, ia = lam, i
        else:
            if num < TOL_NUM:                       # 🔒 A-0(乙)：最緊
                par_block += 1
                empty = True
                kind = "平行·空"
            else:
                par_free += 1
                kind = "平行·無約束"
        rows.append({"i": i, "den": den, "num": num, "lam": lam, "kind": kind,
                     "e_hat": eh, "n_hat": nh, "q": q, "len": L})
    if lam_a > lam_b:
        empty = True
    return {"lam_a": lam_a, "lam_b": lam_b, "ia": ia, "ib": ib, "empty": empty,
            "par_free": par_free, "par_block": par_block, "rows": rows}


def pred_chord(ci, s_star):
    """🔴 **弦區間謂詞**：`在內 ⟺ s* ∈ [λ_a, λ_b]`（⛔ 純純量比較）。"""
    if ci["empty"]:
        return False
    return ci["lam_a"] <= s_star <= ci["lam_b"]


def graze(ci, s_star):
    """🔒 邊界擦邊（施工單 A-2）：相對門檻 `TOL_GRAZE`。回 (是否擦邊, 相對距離, 端點名)。"""
    best = (False, float("inf"), "")
    for lam, nm in ((ci["lam_a"], "λ_a"), (ci["lam_b"], "λ_b")):
        if not math.isfinite(lam):
            continue
        rel = abs(s_star - lam) / max(1.0, abs(lam))
        if rel < best[1]:
            best = (rel <= TOL_GRAZE, rel, nm)
    return best


def pt_seg_dist(x, a, b):
    """點到線段之距離（⛔ 純算術）。"""
    x = np.asarray(x, float)[:2]
    a = np.asarray(a, float)[:2]
    b = np.asarray(b, float)[:2]
    ab = b - a
    L2 = float(np.dot(ab, ab))
    if L2 <= 0:
        return float(np.linalg.norm(x - a))
    t = max(0.0, min(1.0, float(np.dot(x - a, ab)) / L2))
    return float(np.linalg.norm(x - (a + t * ab)))


def is_axis_edge(e_hat, m_hat, n_hat):
    """軸向邊 ⟺ `ê ∥ m̂` 或 `ê ∥ n̂`（＝外接盒之四條邊之方向）。"""
    dm = abs(float(np.dot(e_hat, m_hat)))
    dn = abs(float(np.dot(e_hat, n_hat)))
    return (dm <= TOL_AXIS or dn <= TOL_AXIS), dm, dn


def pj_of(rec, j):
    """🔒 `p_j` ＝ **遠側界之基點**（`faces_of` 之 far face 第二元素）——構造量。"""
    r = (rec["ress"] or [None] * (j + 1))[j]
    ff = w81.faces_of(w81.SOLVE.get(id(r)))[1]
    return None if ff is None else np.asarray(ff[1], float)[:2]


def uj_of(rec, j):
    """🔒 `û_j` ＝ **遠側界之方向**（單位）——構造量。"""
    r = (rec["ress"] or [None] * (j + 1))[j]
    ff = w81.faces_of(w81.SOLVE.get(id(r)))[1]
    return None if ff is None else _u(ff[0])


def pred_t_plain(pair, cell):
    """🔒 外接盒式（負對照）之**純值複本**——須與 `w81.pred_t` 逐對相同（本檔斷言之）。"""
    return (cell["t_lo"] - pair["t_pj"]) <= pair["s_star"] * pair["dot_jn"] <= (cell["t_hi"] - pair["t_pj"])


# ═══ 【0】量測器自檢 ═════════════════════════════════════════════════════
SQ_CCW = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
SQ_CW = [(0.0, 0.0), (0.0, 10.0), (10.0, 10.0), (10.0, 0.0)]


def selfcheck(P):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·每項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    # ① 🔒 A-1 判別力：人工方形街廓 ＋ 已知斜率之線 ⇒ 手算值
    e_ccw, d_ccw = ring_edges(SQ_CCW)
    p = np.array([1.0, 2.0])
    u = _u((3.0, 4.0))                                   # ＝ (0.6, 0.8)
    ci = chord_interval(e_ccw, p, u)
    hand_a = -1.0 / float(u[0])                          # x=0 邊：(0−1)/0.6
    hand_b = (10.0 - 2.0) / float(u[1])                  # y=10 邊：(10−2)/0.8
    ra = abs(ci["lam_a"] - hand_a)
    rb = abs(ci["lam_b"] - hand_b)
    r1 = ra <= 8 * math.ulp(abs(hand_a)) and rb <= 8 * math.ulp(abs(hand_b))
    ok &= r1
    P("  ① **方形街廓對照**（A-1 判別力·施工單所令）：p=(1,2)·û=(%.17g,%.17g)" % (u[0], u[1]))
    P("     λ_a 實得 %.17g／手算 %.17g　殘差 %.3e　**殘差/ulp = %.2f**（ulp=%.3e）"
      % (ci["lam_a"], hand_a, ra, _ulp_ratio(ra, hand_a), math.ulp(abs(hand_a))))
    P("     λ_b 實得 %.17g／手算 %.17g　殘差 %.3e　**殘差/ulp = %.2f**（ulp=%.3e）"
      % (ci["lam_b"], hand_b, rb, _ulp_ratio(rb, hand_b), math.ulp(abs(hand_b))))
    P("     約束邊索引：λ_a←邊 %s（期望 3＝x=0）／λ_b←邊 %s（期望 2＝y=10）⇒ %s"
      % (ci["ia"], ci["ib"], "PASS" if r1 and ci["ia"] == 3 and ci["ib"] == 2 else "🔴 FAIL"))

    # ② 外向性⛔ 不依賴環之走向（CCW／CW 同值）
    e_cw, d_cw = ring_edges(SQ_CW)
    ci2 = chord_interval(e_cw, p, u)
    r2 = (abs(ci2["lam_a"] - ci["lam_a"]) == 0.0 and abs(ci2["lam_b"] - ci["lam_b"]) == 0.0)
    ok &= r2
    P("  ② 走向無關：CCW(%s) vs CW(%s) ⇒ λ 逐位相同 = %s ⇒ %s"
      % (d_ccw["orient"], d_cw["orient"], r2, "PASS" if r2 else "🔴 FAIL"))
    mx1, _ = outward_check(e_ccw, d_ccw["centroid"])
    mx2, _ = outward_check(e_cw, d_cw["centroid"])
    P("     代表點檢 `max ⟨rep−q_e,n_e⟩`：CCW %.3e ／ CW %.3e（期望 ≤ 0）" % (mx1, mx2))

    # ③ 🔒 常設第 8 條：**會使閉式為否**之具體輸入及其實得值（其一：整條線在外）
    p_out = np.array([-5.0, -5.0])
    u_out = _u((1.0, 0.0))
    ci3 = chord_interval(e_ccw, p_out, u_out)
    r3 = ci3["empty"] and not pred_chord(ci3, 0.0)
    ok &= r3
    P("  ③ **常設 8（其一）**：p=(−5,−5)·û=(1,0)（整條線在方形外）⇒ empty=%s"
      "·平行·空邊數=%d ⇒ 謂詞(s*=0)=%s（期望 False）⇒ %s"
      % (ci3["empty"], ci3["par_block"], pred_chord(ci3, 0.0), "PASS" if r3 else "🔴 FAIL"))

    # ④ 🔒 常設第 8 條（其二）：在內／在外之**同一條線**上二個 s* ⇒ 一真一偽
    s_in, s_out = 0.0, 1e6
    r4 = pred_chord(ci, s_in) and not pred_chord(ci, s_out)
    ok &= r4
    P("  ④ **常設 8（其二）**：同一條線上 s*=0 ⇒ %s（期望 True）／s*=1e6 ⇒ %s（期望 False）"
      "·λ=[%.6f, %.6f] ⇒ %s"
      % (pred_chord(ci, s_in), pred_chord(ci, s_out), ci["lam_a"], ci["lam_b"],
         "PASS" if r4 else "🔴 FAIL"))

    # ⑤ 🔒 A-3 之計數器**非恆 0**（判別力）
    _reset_cnt()
    patch_on()
    try:
        sq = SPoly(SQ_CCW)
        _ = sq.contains(sq.centroid)
        _ = sq.intersection(sq)
        _ = w81._line_cross((0, 0), (1, 0), (0, 1), (0, 1))
    finally:
        patch_off()
    c5 = _snapshot_cnt()
    r5 = c5["contains"] >= 1 and c5["intersection"] >= 1 and c5["line_cross"] >= 1
    ok &= r5
    P("  ⑤ **計數器判別力**（⛔ 證其非恆 0）：contains=%d／intersection=%d／_line_cross=%d"
      "（各期望 ≥1）⇒ %s" % (c5["contains"], c5["intersection"], c5["line_cross"],
                          "PASS" if r5 else "🔴 FAIL"))
    _reset_cnt()

    # ⑥ 🔒 常設第 8 條（其三）：**外接盒式**於一個已知輸入為**偽** ⇒ 二式確實不同
    #    斜置正方形（旋轉 45°）＋ 一條穿過外接盒角落但不在多邊形內之線
    dia = [(5.0, 0.0), (10.0, 5.0), (5.0, 10.0), (0.0, 5.0)]
    e_d, d_d = ring_edges(dia)
    p_d = np.array([0.0, 0.0])                            # 外接盒之左下角（⛔ 不在菱形內）
    u_d = _u((1.0, 0.0))
    ci6 = chord_interval(e_d, p_d, u_d)
    bbox_in = (0.0 <= 10.0) and (0.0 <= 0.0 <= 10.0)      # 外接盒式：y=0 落在 [0,10] ⇒ 判在內
    chord_in = pred_chord(ci6, 0.0)
    r6 = bbox_in and not chord_in
    ok &= r6
    P("  ⑥ **常設 8（其三）·二式判別力**：斜置正方形(菱形)·p=(0,0)（外接盒角落）"
      "⇒ 外接盒式=%s／弦區間式=%s（λ=[%.6f, %.6f]）⇒ %s"
      % (bbox_in, chord_in, ci6["lam_a"], ci6["lam_b"], "PASS" if r6 else "🔴 FAIL"))

    # ⑦ 🔒 常設第 9 條：三門檻之量級與 ulp
    P("  ⑦ **常設 9**：門檻 vs 被測量之量級")
    P("     TOL_DEN =%.1e；被測量 |⟨û_j,n_e⟩| ∈ [0,1]，ulp(1.0)=%.3e ⇒ 門檻/ulp = %.3e"
      % (TOL_DEN, math.ulp(1.0), TOL_DEN / math.ulp(1.0)))
    P("     TOL_GRAZE=%.1e（**相對**）；被測量 |λ| 之量級於【C】表出艙，"
      "相對門檻⛔ 不受量級漂移影響" % TOL_GRAZE)
    P("     TOL_AXIS =%.1e；被測量 |⟨ê,m̂⟩| ∈ [0,1]，同 ulp(1.0) ⇒ 門檻/ulp = %.3e"
      % (TOL_AXIS, TOL_AXIS / math.ulp(1.0)))

    # ⑧ 🔒 `_assert_plain` 之判別力（⛔ 證其非恆 0）——以**真的** shapely 物件餵入
    n0 = PLAIN_VIOL["n"]
    _assert_plain(e_ccw, SPoly(SQ_CCW), u)
    r8 = (PLAIN_VIOL["n"] == n0 + 1)
    ok &= r8
    P("  ⑧ **`_assert_plain` 判別力**：餵入真 shapely `Polygon` 作 `p` ⇒ 違反計數 %d→%d"
      "（期望 +1）·why=%s ⇒ %s"
      % (n0, PLAIN_VIOL["n"], PLAIN_VIOL["why"][-1] if PLAIN_VIOL["why"] else None,
         "PASS" if r8 else "🔴 FAIL"))
    PLAIN_VIOL["n"] = 0
    PLAIN_VIOL["why"].clear()
    PLAIN_VIOL["calls"] = 0
    P("     🔒 已歸零（本項為自檢·⛔ 不得計入正式量測）")

    P("  ⇒ 量測器自檢：%s" % ("PASS" if ok else "🔴 FAIL（⛔ 以下量測結果不得採信）"))
    return ok


# ═══ P8 之第八法：`run_all` 清單筆數 ══════════════════════════════════════
def run_all_count_method8():
    """🔒 **第八法：檔案系統母體 × 引用交叉**（⛔ 與既用七法皆不同族）。

    既用七法之母體**皆為 `run_all.py` 之語法／位元組**（字面 `re`／`ast`／`tokenize`／
    `co_consts`×2／肉眼／括號深度）。本法之母體 ＝ **檔案系統上真實存在之 `verify/**.py`**，
    逐檔問「其**引用名**是否以雙引號出現於 `run_all.py`」⇒ ⛔ 不解析清單之語法結構。
    🔒 其對 `verify/run_all.py:80` 之 `endswith(".py")` **結構上免疫**（`.py` ⛔ 非任何檔之引用名）。
    """
    lines = io.open(os.path.join(VERIFY, "run_all.py"), encoding="utf-8").read().split(chr(10))
    src = chr(10).join(lines)
    hits, miss = [], []
    for dp, dns, fns in os.walk(VERIFY):
        dns[:] = [d for d in dns if d not in ("__pycache__", "out", "baselines", "probes")]
        for fn in fns:
            if not fn.endswith(".py"):
                continue
            rel = os.path.relpath(os.path.join(dp, fn), VERIFY).replace(os.sep, "/")
            for cand in (rel, fn):
                tok = '"' + cand + '"'
                if tok in src:
                    where = [(i + 1, lines[i].strip()[:78])
                             for i in range(len(lines)) if tok in lines[i]]
                    hits.append((cand, where))
                    break
            else:
                miss.append(rel)
    return sorted(hits), sorted(miss)


# ═══ 主 ═══════════════════════════════════════════════════════════════
def main():                                                         # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    def POP(pop, printed, tag):
        P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # %s" % (pop, printed, pop - printed, tag))
        if printed != pop:
            P("     ⚠️ `PRINTED ≠ POPULATION` ⇒ 🔒 **本表之結論一律以 `POPULATION` 為分母**"
              "（⛔ 表身列數不得作為母體·節 105）")

    P("=" * W)
    P("【W-G.9-82 §二 A 組】弦區間閉式——把必要條件推成充要，且仍⛔ 不先算交點（⛔ 只量不修）")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向使 [λ_a, λ_b] 偏窄**（甲/乙/丙 三條見 docstring）⇒ 錯誤方向**會吵**。")
    P("  🔒 同源聲明：`analyse_cell`／`pred_t`／`spy_*` 皆自 `probe_WG981_scope` **原樣 import**"
      "（⛔ 不另造第二份 ⇒ 負對照可比·節 100）。")

    ns, fake_st = harvest()
    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    strip_axis = ns["_strip_axis"]
    snapshot = rv.load_snapshot()
    o_solve, o_pool = ns["_solve_G_one"], ns["_pool_strips_for_block"]
    o_fcad = ns["_first_corner_alloc_dir"]

    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)

    def one_pass():
        for setback in (0.0, 3.5):
            w81.CUR["setback"] = setback
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, wins, forced = run_corner_pk(
                ns, fake_st, cb_all, cad, params, temp_p, build_p, setback, snapshot=snapshot)
            for lbl in blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass

    P("")
    P("【驅動·第一趟（真實）】R1–R6 × 兩情境——街廓母體 = %s" % blks)
    P("-" * W)
    w81.CAP.clear()
    ns["_solve_G_one"], ns["_pool_strips_for_block"] = w81.spy_solve(o_solve), w81.spy_pool(o_pool)
    try:
        one_pass()
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(w81.CAP)

    # ── 【TRUTH 階段】（計數器 ON·⛔ 此階段之呼叫**不**計入謂詞路徑）───────────
    _reset_cnt()
    patch_on()
    try:
        CELL = [(rec,) + w81.analyse_cell(rec, strip_axis) for rec in REAL]
    finally:
        patch_off()
    CNT_TRUTH = _snapshot_cnt()
    ALL = [(rec, meta, r) for rec, meta, rows in CELL for r in rows if r.get("ok")]
    P("  攔截 %d 格；**可算交點之對（母體）＝ %d**（🔒 承 `-80`／`-81`·⛔ 非 67）"
      % (len(REAL), len(ALL)))
    P("  🔒 TRUTH 階段之呼叫計數：contains=%d／intersection=%d／_line_cross=%d"
      % (CNT_TRUTH["contains"], CNT_TRUTH["intersection"], CNT_TRUTH["line_cross"]))

    # ── 【C】A-1：弦區間之構造（逐 (情境, 街廓, 街角宗 j)）────────────────────
    P("")
    P("【C／A-1】`[λ_a, λ_b]` 之構造——逐 (情境, 街廓, **宗 j**)（⛔ 純算術·⛔ 零 shapely）")
    P("-" * W)
    EDGES = {}          # cell_idx -> (edges, diag)
    CI = {}             # (cell_idx, j) -> chord_interval
    PJ = {}             # (cell_idx, j) -> p_j
    UJ = {}
    lam_calls = 0
    c_rows = []
    _reset_cnt()
    patch_on()                       # 🔒 λ **構造**亦屬謂詞路徑 ⇒ 一併受計數
    try:
        for ci_idx, (rec, meta, rows) in enumerate(CELL):
            b = rec["block"]
            edges, diag = ring_edges(list(b.exterior.coords))
            mxv, _vals = outward_check(edges, diag["centroid"])
            EDGES[ci_idx] = (edges, diag, mxv)
            js = sorted({r["j"] for r in rows if r.get("ok")})
            for j in js:
                pj = pj_of(rec, j)
                uj = uj_of(rec, j)
                if pj is None or uj is None:
                    continue
                ci = chord_interval(edges, pj, uj)
                lam_calls += 1
                CI[(ci_idx, j)] = ci
                PJ[(ci_idx, j)] = pj
                UJ[(ci_idx, j)] = uj
                c_rows.append((ci_idx, rec, meta, j, ci, edges, diag, mxv))
    finally:
        patch_off()
    CNT_LAM = _snapshot_cnt()
    P("  %-6s %-5s %-4s %-7s %-6s %10s %12s %12s %12s %-6s %-6s %-9s"
      % ("情境", "街廓", "j", "是街角?", "頂點", "外向檢max", "**λ_a**", "**λ_b**",
         "λ_b−λ_a", "←邊a", "←邊b", "p_j 內含"))
    n_inner = 0
    for ci_idx, rec, meta, j, ci, edges, diag, mxv in c_rows:
        inner = (ci["lam_a"] < 0.0 < ci["lam_b"]) and not ci["empty"]
        n_inner += int(inner)
        P("  %-6s %-5s %-4d %-7s %-6d %10.3e %12.4f %12.4f %12.4f %-6s %-6s %-9s"
          % ("%gm" % rec["setback"], rec["label"], j,
             "是" if j in meta["corners"] else "否", diag["n_vert"], mxv,
             ci["lam_a"], ci["lam_b"], ci["lam_b"] - ci["lam_a"],
             ci["ia"], ci["ib"], "✅" if inner else "🔴 **否**"))
    POP(len(c_rows), len(c_rows), "A-1 逐 (格, j)（全列）")
    P("  🔒 **`P2`（`p_j` 內含性）**：`λ_a < 0 < λ_b` 者 **%d ／ %d**" % (n_inner, len(c_rows)))
    if n_inner != len(c_rows):
        P("     🔴 **⛔ 不成立者逐項具名**：")
        for ci_idx, rec, meta, j, ci, edges, diag, mxv in c_rows:
            if not ((ci["lam_a"] < 0.0 < ci["lam_b"]) and not ci["empty"]):
                P("       [%gm] %-4s j=%d  λ=[%.6f, %.6f]  empty=%s  平行空邊=%d"
                  % (rec["setback"], rec["label"], j, ci["lam_a"], ci["lam_b"],
                     ci["empty"], ci["par_block"]))
    P("  🔒 街廓之外向性：12 格之 `max ⟨cen−q_e,n_e⟩` 極大 = %.3e（期望 ≤ 0·凸 ⇒ 嚴格 < 0）"
      % max(EDGES[i][2] for i in EDGES))
    P("  🔒 零長邊（A-0 丙）合計 = %d；環走向 = %s"
      % (sum(EDGES[i][1]["n_degenerate"] for i in EDGES),
         sorted({EDGES[i][1]["orient"] for i in EDGES})))
    lam_mag = [abs(v) for ci_idx, rec, meta, j, ci, e, d, m in c_rows
               for v in (ci["lam_a"], ci["lam_b"]) if math.isfinite(v)]
    P("  🔒 **常設 9**：`|λ|` 之量級 ∈ [%.4f, %.4f]；上端 ulp = %.3e ⇒ 相對門檻 %.1e 遠高於之"
      % (min(lam_mag), max(lam_mag), math.ulp(max(lam_mag)), TOL_GRAZE))

    # ── 【D】A-2：謂詞驗證（86 真實對）───────────────────────────────────
    P("")
    P("【D／A-2】弦區間謂詞於 **%d 真實對** vs `block.contains(X)`" % len(ALL))
    P("-" * W)
    _reset_cnt()
    patch_on()
    PLAIN = []
    try:
        for ci_idx, (rec, meta, rows) in enumerate(CELL):
            for r in rows:
                if not r.get("ok"):
                    continue
                key = (ci_idx, r["j"])
                if key not in CI:
                    continue
                ci = CI[key]
                pc = pred_chord(ci, r["s_star"])
                gz, grel, gnm = graze(ci, r["s_star"])
                pt_plain = pred_t_plain({"t_pj": r["t_pj"], "s_star": r["s_star"],
                                         "dot_jn": r["dot_jn"]},
                                        {"t_lo": meta["t_lo"], "t_hi": meta["t_hi"]})
                PLAIN.append((ci_idx, rec, meta, r, ci, pc, gz, grel, gnm, pt_plain))
    finally:
        patch_off()
    CNT_PRED = _snapshot_cnt()

    agree = disagree = grazed = 0
    dis_rows = []
    for ci_idx, rec, meta, r, ci, pc, gz, grel, gnm, pt_plain in PLAIN:
        if gz:
            grazed += 1
            continue
        if pc == r["inside"]:
            agree += 1
        else:
            disagree += 1
            dis_rows.append((ci_idx, rec, meta, r, ci, pc, grel, gnm))
    P("  %-6s %-5s %-4s %-4s %13s %13s %13s %11s %-8s %-9s %-8s"
      % ("情境", "街廓", "j", "k", "s*", "λ_a", "λ_b", "擦邊相對", "弦區間", "contains", "判"))
    show = dis_rows if dis_rows else PLAIN[:12]
    for tup in show:
        if len(tup) == 8:
            ci_idx, rec, meta, r, ci, pc, grel, gnm = tup
        else:
            ci_idx, rec, meta, r, ci, pc, gz, grel, gnm, _pt = tup
        P("  %-6s %-5s %-4d %-4d %13.4f %13.4f %13.4f %11.2e %-8s %-9s %-8s"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], r["s_star"],
             ci["lam_a"], ci["lam_b"], grel, pc, r["inside"],
             "✅" if pc == r["inside"] else "🔴 **不一致**"))
    POP(len(PLAIN), len(show), "A-2 真實對（僅列不一致者；無則列前 12）")
    P("  ⇒ **一致 %d ／ 不一致 %d ／ 邊界擦邊（另計·⛔ 不計入二者）%d**；和 = %d ／ 母體 = %d ⇒ %s"
      % (agree, disagree, grazed, agree + disagree + grazed, len(PLAIN),
         "✅ 相等" if agree + disagree + grazed == len(PLAIN) else "🔴 **不等·量測器有誤**"))
    P("  🔒 **`P3`**：對稱差 %s"
      % ("＝ **空集** ✅" if disagree == 0 else "＝ **%d 對** 🔴·已逐對具名" % disagree))
    if grazed:
        P("  🔒 **邊界擦邊類逐對具名**（`contains` 於邊界回 False 而閉區間回 True）：")
        for ci_idx, rec, meta, r, ci, pc, gz, grel, gnm, _pt in PLAIN:
            if gz:
                P("     [%gm] %-4s (%d,%d) s*=%.6f 貼 %s=%.6f 相對距=%.3e contains=%s 弦=%s"
                  % (rec["setback"], rec["label"], r["j"], r["k"], r["s_star"],
                     gnm, ci["lam_a"] if gnm == "λ_a" else ci["lam_b"], grel, r["inside"], pc))
    # 🔒 負對照之**純值複本**須與 w81.pred_t 逐對相同
    same = sum(1 for ci_idx, rec, meta, r, ci, pc, gz, grel, gnm, pt
               in PLAIN if pt == w81.pred_t(r, meta))
    P("  🔒 `pred_t_plain` vs `w81.pred_t` 逐對相同：%d／%d ⇒ %s"
      % (same, len(PLAIN), "✅" if same == len(PLAIN) else "🔴 **不同·負對照不可比**"))
    a_t = sum(1 for ci_idx, rec, meta, r, ci, pc, gz, grel, gnm, pt
              in PLAIN if w81.pred_t(r, meta) == r["inside"])
    P("  🔒 **負對照（外接盒單軸式）於 86 真實對**：一致 %d ／ 不一致 %d" % (a_t, len(PLAIN) - a_t))

    # ── 【E】A-3：碼面自證 ──────────────────────────────────────────────
    P("")
    P("【E／A-3】⛔「**不先算交點**」之碼面自證（🔒 shim 計數·⛔ 非讀碼推定）")
    P("-" * W)
    corner_tot = sum(len(meta["corners"]) for _rec, meta, _rows in CELL)
    P("  ① **弦區間之計算次數 = %d**　vs　**對數 = %d**　⇒ %s"
      % (lam_calls, len(ALL), "✅ 前者 ≠ 後者" if lam_calls != len(ALL) else "🔴 **二者相等 ⇒ 未達成目標**"))
    P("     🔒 相對照之二母體：**街角宗總數（Σ|meta.corners|）= %d**；"
      "**相異 j 之 (格,j) 數 = %d**" % (corner_tot, lam_calls))
    P("     🔒 `P5` 之受詞逐字為「弦區間計算次數 ＝ **街角宗總數**」⇒ 實得 %d vs %d ⇒ %s"
      % (lam_calls, corner_tot, "✅ 相符" if lam_calls == corner_tot else "🔴 **不符·⛔ 不調整預測·具名**"))
    P("  ② **謂詞路徑之呼叫計數**（🔒 **二段皆計**：λ 構造段 ＋ 謂詞求值段）")
    P("     λ 構造段：_line_cross=%d／.intersection(=%d／.contains(=%d"
      % (CNT_LAM["line_cross"], CNT_LAM["intersection"], CNT_LAM["contains"]))
    P("     謂詞求值段：_line_cross=%d／.intersection(=%d／.contains(=%d"
      % (CNT_PRED["line_cross"], CNT_PRED["intersection"], CNT_PRED["contains"]))
    _mx = max(list(CNT_LAM.values()) + list(CNT_PRED.values()))
    P("     ⇒ 二段合計之極大 = %d（期望 **0**）⇒ %s"
      % (_mx, "✅" if _mx == 0 else "🔴 **非 0·具名**"))
    P("  ③ **判別力**：TRUTH 階段之 contains=%d（期望 > 0 ⇒ 證計數器⛔ 非恆 0）⇒ %s"
      % (CNT_TRUTH["contains"], "✅" if CNT_TRUTH["contains"] > 0 else "🔴 FAIL"))
    P("  ④ 🔒 **`chord_interval` 之實參⛔ 不含幾何物件**（機械證·⛔ 非讀碼推定）：")
    P("     `_assert_plain` 呼叫數 = %d（＝ 弦區間計算次數）／**違反數 = %d**（期望 0）⇒ %s"
      % (PLAIN_VIOL["calls"], PLAIN_VIOL["n"],
         "✅" if PLAIN_VIOL["n"] == 0 else "🔴 **有違反：%s**" % (PLAIN_VIOL["why"][:5],)))
    P("     🔒 其判別力已於 `selfcheck` ⑧ 以**真的** shapely `Polygon` 實證為 +1（⛔ 非恆 0）。")
    P("     🔒 實際餵入者僅 `(edges, p_j, û_j)`；`edges` 由 `ring_edges` 自**街廓頂點序列**造。")

    # ── 【F】A-4：0m R3 之真實餘裕 ──────────────────────────────────────
    P("")
    P("【F／A-4】`0m R3` 之**真實餘裕**（`s* − λ_b`）——與 `VR-037` 二-甲之 `3.4192` 對帳")
    P("-" * W)
    P("  🔒 倉內錨（引 `docs/reports/W-G.9-81b_CC交接文.md` §四-2）：`0m R3` `(7,9)` 之最小 `t` 越界量"
      " ＝ **3.4192 m**（`t_X 11.7089` vs `t_hi 8.2897`）")
    tgt = [(i, rec, meta, rows) for i, (rec, meta, rows) in enumerate(CELL)
           if rec["label"] == "R3" and abs(rec["setback"]) < 1e-9]
    if not tgt:
        P("  🔴 **查無 `0m R3` 之格** ⇒ ⛔ 本節不出艙數（具名）")
    for ci_idx, rec, meta, rows in tgt:
        ci = CI.get((ci_idx, 7))
        if ci is None:
            P("  🔴 **`0m R3` 之 j=7 無弦區間**（該 j 未出現於任何可算之對）⇒ 具名")
            continue
        edges, diag, mxv = EDGES[ci_idx]
        eb = [e for e in ci["rows"] if e["i"] == ci["ib"]]
        P("  `0m R3` j=7：λ_a=%.6f　**λ_b=%.6f**　**約束邊索引=%s**　邊長=%.4f　"
          "⟨û_j,n_e⟩=%.6f　⟨q_e−p_j,n_e⟩=%.6f"
          % (ci["lam_a"], ci["lam_b"], ci["ib"], eb[0]["len"] if eb else float("nan"),
             eb[0]["den"] if eb else float("nan"), eb[0]["num"] if eb else float("nan")))
        P("  %-4s %13s %13s %13s %13s %13s %13s %-10s"
          % ("k", "s*", "⟨û_j,n̂⟩", "t_X(實測)", "t_hi", "t 越界量", "**s*−λ_b**", "contains"))
        f_rows = [r for r in rows if r.get("ok") and r["j"] == 7]
        for r in sorted(f_rows, key=lambda x: x["k"]):
            over_t = r["t_meas"] - meta["t_hi"]
            P("  %-4d %13.4f %13.6f %13.4f %13.4f %13.4f %13.4f %-10s"
              % (r["k"], r["s_star"], r["dot_jn"], r["t_meas"], meta["t_hi"],
                 over_t, r["s_star"] - ci["lam_b"], r["inside"]))
        POP(len(f_rows), len(f_rows), "A-4 `0m R3` j=7 之逐 k（全列）")
        r79 = [r for r in f_rows if r["k"] == 9]
        if r79:
            r = r79[0]
            bound = 3.4192 / r["dot_jn"] if abs(r["dot_jn"]) > 0 else float("nan")
            got = r["s_star"] - ci["lam_b"]
            P("  🔒 **`P7`**：`s*−λ_b` 實得 **%.6f** vs `3.4192/⟨û_j,n̂⟩` = **%.6f** ⇒ %s"
              % (got, bound, "✅ ≥ 成立" if got >= bound else
                 "🔴 **小於 ⇒ `VR-040` 四之單調性推論錯·具名**"))
            P("     🔒 併出艙（節 103）：本格為**最接近翻面**者；`t` 越界量實測 = %.4f"
              "（倉內錨 3.4192·差 %.3e）" % (r["t_meas"] - meta["t_hi"],
                                          abs((r["t_meas"] - meta["t_hi"]) - 3.4192)))
        # 🔴 **`P7` 之受詞更正量**（⛔ **不改** `P7` 之逐字判·另列）
        P("")
        P("  🔴 **`P7` 之受詞更正量**（⛔ **不改**上列逐字判·⛔ 不調整預測；本段係**另一個量**）")
        P("     🔒 成因逐字：`⟨û_j,n̂⟩ = %.6f` **為負** ⇒ `t ≤ t_hi` 之約束於 `s` 軸上化為**下界**"
          "（`s ≥ (t_hi−t_pj)/⟨û_j,n̂⟩`）⇒ **被違反者是 `λ_a` 側、⛔ 非 `λ_b` 側**。"
          % (f_rows[0]["dot_jn"] if f_rows else float("nan")))
        P("     ⇒ `P7` 逐字所寫之 `s*−λ_b` **量到的是另一側**；其對應之正量為 `λ_a − s*`。")
        P("  %-4s %12s %12s %-7s %14s %14s %14s %-8s"
          % ("k", "s*", "被違反之界", "側", "**真實餘裕**", "外接盒餘裕", "t越界/|⟨û_j,n̂⟩|", "真≥盒?"))
        n_ok = n_tot = 0
        for r in sorted(f_rows, key=lambda x: x["k"]):
            dj = r["dot_jn"]
            lo_b, hi_b = ((meta["t_lo"] - r["t_pj"]) / dj, (meta["t_hi"] - r["t_pj"]) / dj) \
                if dj > 0 else ((meta["t_hi"] - r["t_pj"]) / dj, (meta["t_lo"] - r["t_pj"]) / dj)
            if r["s_star"] < ci["lam_a"]:
                side, viol, r_true, r_bbox = "λ_a(下界)", ci["lam_a"], ci["lam_a"] - r["s_star"], lo_b - r["s_star"]
            elif r["s_star"] > ci["lam_b"]:
                side, viol, r_true, r_bbox = "λ_b(上界)", ci["lam_b"], r["s_star"] - ci["lam_b"], r["s_star"] - hi_b
            else:
                side, viol, r_true, r_bbox = "無(在內)", float("nan"), float("nan"), float("nan")
            ratio = abs(r["t_meas"] - meta["t_hi"]) / abs(dj) if abs(dj) > 0 else float("nan")
            good = (r_true >= r_bbox) if math.isfinite(r_true) else None
            n_tot += 1
            n_ok += int(bool(good))
            P("  %-4d %12.4f %12.6f %-7s %14.6f %14.6f %14.6f %-8s"
              % (r["k"], r["s_star"], viol, side, r_true, r_bbox, ratio, good))
        POP(n_tot, n_tot, "A-4 更正量·逐 k（全列）")
        P("     ⇒ **真實餘裕 ≥ 外接盒餘裕**者 = **%d ／ %d** ⇒ %s"
          % (n_ok, n_tot,
             "✅ **`VR-040` 四之單調性推論（外接盒之界恆不緊於真實邊）成立**"
             if n_ok == n_tot else "🔴 **有反例·具名**"))
        if r79:
            r = r79[0]
            dj = r["dot_jn"]
            lo_b = (meta["t_hi"] - r["t_pj"]) / dj if dj < 0 else (meta["t_lo"] - r["t_pj"]) / dj
            P("     🔒 **`(7,9)` 之定錨**：真實餘裕 `λ_a − s*` = **%.6f** ≥ `3.4192/|⟨û_j,n̂⟩|` = **%.6f**"
              "（差 %.6f）⇒ %s"
              % (ci["lam_a"] - r["s_star"], 3.4192 / abs(dj),
                 (ci["lam_a"] - r["s_star"]) - 3.4192 / abs(dj),
                 "✅" if (ci["lam_a"] - r["s_star"]) >= 3.4192 / abs(dj) else "🔴"))

    # ── 【G-1】A-5-1：例外類 6 對逐對列出 ─────────────────────────────────
    P("")
    P("【G-1／A-5-1】`A-4` 更正後之**例外類**（`û_k` 不 ∥ `n̂`）逐對列出")
    P("-" * W)
    base = [(rec, meta, r) for rec, meta, r in ALL if abs(r["dot_jm"]) >= 1e-15]
    exc = [(rec, meta, r) for rec, meta, r in base if abs(r["cr_kn"]) > 1e-12]
    P("  %-6s %-5s %-4s %-4s %15s %15s %-10s %-10s %-26s"
      % ("情境", "街廓", "j", "k", "|cross(û_k,n̂)|", "**|比值|**", "宗k 是街角?",
         "宗j 是街角?", "宗k 之 near_dir 來源"))
    for rec, meta, r in exc:
        rk = (rec["ress"] or [None] * (r["k"] + 1))[r["k"]]
        info = w81.SOLVE.get(id(rk)) or {}
        nd = info.get("near_dir")
        src = ("near_dir=None(⇒用 alloc_used)" if nd is None else
               "near_dir=" + str(tuple(round(float(x), 6) for x in np.asarray(nd, float)[:2])))
        P("  %-6s %-5s %-4d %-4d %15.3e %15.9f %-10s %-10s %-26s"
          % ("%gm" % rec["setback"], rec["label"], r["j"], r["k"], abs(r["cr_kn"]),
             abs(r["ratio"]), "是" if r["k"] in meta["corners"] else "否",
             "是" if r["j"] in meta["corners"] else "否", src))
    POP(len(exc), len(exc), "A-5-1 例外類（全列·⛔ 非取樣）")
    P("  ⇒ 更正後母體 **%d**；例外類（`û_k` 不 ∥ `n̂`）＝ **%d**（`VR-040` 一載 `-81` 實得 6）"
      % (len(base), len(exc)))

    # ── 【B/掃描】A-2 之 144 列 ＋ A-3 歸因 ＋ A-5-2 ────────────────────────
    P("")
    P("【D-2／A-2 掃描】`θ` 掃描 %s ——弦區間式 vs 外接盒式（🔒 負對照須仍 34）"
      % ", ".join("%d°" % t for t in w81.SWEEP_DEG))
    P("-" * W)
    ss_ = fake_st.session_state
    slbs = (ss_.get('f3_cad_side_lines_by_side', {}) or {})
    adir = (ss_.get('f3_cad_alloc_dir', {}) or {})
    alloc_axis = ns["alloc_normal_axis"]

    def blk_of_mid(mid):
        m = np.asarray(mid, dtype=float)[:2]
        for lbl in slbs:
            for w_ in ('left', 'right'):
                sd = (slbs.get(lbl) or {}).get(w_)
                if sd and sd.get('mid') is not None:
                    if float(np.linalg.norm(np.asarray(sd['mid'], dtype=float)[:2] - m)) < 1e-6:
                        return lbl
        return None

    def make_fcad(theta_deg):
        def _f(side_mid):
            lbl = blk_of_mid(side_mid)
            if lbl is None or adir.get(lbl) is None:
                raise RuntimeError("🔴 掃描 shim：side_mid 查無街廓／該塊無 ALLOC（no-silent）")
            b = _u(alloc_axis(adir[lbl]))
            th = math.radians(theta_deg)
            ct, st_ = math.cos(th), math.sin(th)
            return (float(b[0] * ct - b[1] * st_), float(b[0] * st_ + b[1] * ct))
        return _f

    SW = {"t_ag": 0, "t_dis": 0, "c_ag": 0, "c_dis": 0}
    ATTR = {"甲": 0, "乙": 0, "丙": 0}
    yi_rows = []
    c_dis_rows = []
    pred_cnt_sweep = {"line_cross": 0, "intersection": 0, "contains": 0}
    for th in w81.SWEEP_DEG:
        w81.CAP.clear()
        w81.CUR["theta"] = th
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = w81.spy_solve(o_solve), w81.spy_pool(o_pool)
        ns["_first_corner_alloc_dir"] = make_fcad(th)
        try:
            one_pass()
        finally:
            ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
            ns["_first_corner_alloc_dir"] = o_fcad
        for rec in list(w81.CAP):
            # 🔒 **⛔ 不得跳過任何格**——母體須恆為 `12θ × 12 格 = 144`
            #    （首版曾以 `if not ok: continue` 跳過，母體縮為 75 而表頭仍寫 144；
            #     係 `POPULATION=` 行自己把它抓出來·記入 §I）。
            meta, rows = w81.analyse_cell(rec, strip_axis)
            ok = [r for r in rows if r.get("ok")]
            edges = m_hat = n_hat = None
            if rec["block"] is not None:
                edges, _diag = ring_edges(list(rec["block"].exterior.coords))
                m_hat, _denom = strip_axis(rec["d_hat"], rec["alloc"])
                m_hat = np.asarray(m_hat, float)[:2]
                n_hat = _rot90(m_hat)
            cache = {}
            _reset_cnt()
            patch_on()
            try:
                if edges is not None:
                    for r in ok:
                        if r["j"] not in cache:
                            pj, uj = pj_of(rec, r["j"]), uj_of(rec, r["j"])
                            cache[r["j"]] = None if (pj is None or uj is None) \
                                else (chord_interval(edges, pj, uj), pj, uj)
            finally:
                patch_off()
            for kk in pred_cnt_sweep:
                pred_cnt_sweep[kk] += CNT[kk]
            meas = sum(1 for r in ok if r["inside"] and r["d"] >= 2)
            p_t = sum(1 for r in ok if w81.pred_t(r, meta) and r["d"] >= 2)
            p_c = sum(1 for r in ok
                      if cache.get(r["j"]) and pred_chord(cache[r["j"]][0], r["s_star"])
                      and r["d"] >= 2)
            if (meas >= 1) == (p_t >= 1):
                SW["t_ag"] += 1
            else:
                SW["t_dis"] += 1
                for r in ok:
                    if not (w81.pred_t(r, meta) and r["d"] >= 2):
                        continue
                    ov = w81.over_s(r, meta)
                    bbox_in = (ov <= 0) and w81.pred_t(r, meta)
                    if ov > 0:
                        cls = "甲"
                    elif bbox_in and not r["inside"]:
                        cls = "乙"
                    else:
                        cls = "丙"
                    ATTR[cls] += 1
                    if cls == "乙" and edges is not None:
                        ent = cache.get(r["j"])
                        ci_ = ent[0] if ent else None
                        # 最近之街廓邊（⛔ 純算術）
                        near_i, near_d = None, float("inf")
                        for (ei, q, nh, eh, Le) in edges:
                            b_pt = q + eh * Le
                            dd = pt_seg_dist(r["X"], q, b_pt)
                            if dd < near_d:
                                near_i, near_d = ei, dd
                        con_i, con_side = None, ""
                        if ci_ is not None and not ci_["empty"]:
                            if r["s_star"] > ci_["lam_b"]:
                                con_i, con_side = ci_["ib"], "λ_b"
                            elif r["s_star"] < ci_["lam_a"]:
                                con_i, con_side = ci_["ia"], "λ_a"
                        ax_con = ax_near = None
                        dmc = dnc = float("nan")
                        for (ei, q, nh, eh, Le) in edges:
                            if ei == con_i:
                                ax_con, dmc, dnc = is_axis_edge(eh, m_hat, n_hat)
                            if ei == near_i:
                                ax_near = is_axis_edge(eh, m_hat, n_hat)[0]
                        yi_rows.append({
                            "th": th, "sb": rec["setback"], "lb": rec["label"],
                            "j": r["j"], "k": r["k"], "s_star": r["s_star"],
                            "lam_a": ci_["lam_a"] if ci_ else float("nan"),
                            "lam_b": ci_["lam_b"] if ci_ else float("nan"),
                            "chord": (pred_chord(ci_, r["s_star"]) if ci_ else None),
                            "near_i": near_i, "near_d": near_d, "near_axis": ax_near,
                            "con_i": con_i, "con_side": con_side, "con_axis": ax_con,
                            "dm": dmc, "dn": dnc})
            if (meas >= 1) == (p_c >= 1):
                SW["c_ag"] += 1
            else:
                SW["c_dis"] += 1
                c_dis_rows.append((th, rec["setback"], rec["label"], meas, p_t, p_c))
        print("    θ=%d° 完畢" % th, file=sys.stderr)

    P("  🔒 **負對照（外接盒·單軸 `t`）**：掃描不一致 = **%d**（施工單期望 **34**）⇒ %s"
      % (SW["t_dis"], "✅ 相符" if SW["t_dis"] == 34 else "🔴 **不符·具名**"))
    P("  🔴 **弦區間式**：掃描不一致 = **%d** ⇒ %s"
      % (SW["c_dis"],
         "✅ **`P4` 成立（＝ 0）**" if SW["c_dis"] == 0 else
         ("🔴 **與負對照同數 ⇒ `VR-040` 四之推導證偽·具名**" if SW["c_dis"] == SW["t_dis"]
          else "⚠️ **由 %d 降至 %d·未歸零·具名**" % (SW["t_dis"], SW["c_dis"]))))
    POP(SW["t_ag"] + SW["t_dis"], SW["t_ag"] + SW["t_dis"], "掃描列（12θ × 12 格）")
    if c_dis_rows:
        P("  🔴 **弦區間式之不一致列逐列具名**：")
        for th, sb, lb, meas, p_t, p_c in c_dis_rows:
            P("     θ=%d° [%gm] %-4s  實測在內對數=%d  外接盒判=%d  弦區間判=%d"
              % (th, sb, lb, meas, p_t, p_c))
    P("  🔒 掃描期間 **PRED 路徑**之呼叫計數：_line_cross=%d／.intersection(=%d／.contains(=%d（各期望 0）"
      % (pred_cnt_sweep["line_cross"], pred_cnt_sweep["intersection"], pred_cnt_sweep["contains"]))
    P("  🔒 歸因（承 `-81` 之三類·⛔ 同一判準）：甲=%d ／ 乙=%d ／ 丙=%d"
      % (ATTR["甲"], ATTR["乙"], ATTR["丙"]))

    # ── 【G-2】A-5-2：乙類之幾何定位 ────────────────────────────────────
    P("")
    P("【G-2／A-5-2】**乙類 %d 對**之幾何定位——最近街廓邊 ＋ **約束邊**是否軸向" % len(yi_rows))
    P("-" * W)
    P("  %-5s %-6s %-5s %-4s %-4s %12s %12s %12s %-7s %-7s %11s %-7s %-8s %-7s"
      % ("θ", "情境", "街廓", "j", "k", "s*", "λ_a", "λ_b", "弦判", "最近邊",
         "到邊距離", "近邊軸向", "**約束邊**", "軸向?"))
    n_axis = 0
    for y in yi_rows:
        n_axis += int(bool(y["con_axis"]))
        P("  %-5s %-6s %-5s %-4d %-4d %12.4f %12.4f %12.4f %-7s %-7s %11.4f %-7s %-8s %-7s"
          % ("%d°" % y["th"], "%gm" % y["sb"], y["lb"], y["j"], y["k"], y["s_star"],
             y["lam_a"], y["lam_b"], y["chord"], y["near_i"], y["near_d"],
             y["near_axis"], "%s(%s)" % (y["con_i"], y["con_side"]), y["con_axis"]))
    POP(len(yi_rows), len(yi_rows), "A-5-2 乙類（全列·⛔ 非取樣）")
    P("  🔒 **`P6`**：約束邊為**軸向**者 = **%d ／ %d** ⇒ %s"
      % (n_axis, len(yi_rows),
         "✅ **皆非軸向 ⇒「被 4 條軸向邊放進來」之說成立**" if n_axis == 0 else
         "🔴 **有軸向者 ⇒ 該說不全·已逐對具名**"))
    _dms = [y["dm"] for y in yi_rows if math.isfinite(y["dm"])]
    _dns = [y["dn"] for y in yi_rows if math.isfinite(y["dn"])]
    if _dms and _dns:
        _marg = min(min(a, b) for a, b in zip(_dms, _dns))
        P("  🔒 **常設 9**：軸向判定之量級——約束邊之 `|⟨ê,m̂⟩|` ∈ [%.4f, %.4f]／"
          "`|⟨ê,n̂⟩|` ∈ [%.4f, %.4f]；門檻 %.1e（ulp(1.0)=%.3e）"
          % (min(_dms), max(_dms), min(_dns), max(_dns), TOL_AXIS, math.ulp(1.0)))
        P("  🔒 **節 103（最接近翻面者及其餘裕）**：軸向 ⟺ `min(|⟨ê,m̂⟩|,|⟨ê,n̂⟩|) ≤ %.1e`；"
          "**全 36 對之最小者 = %.6f**（＝ 離軸 %.3f°）⇒ 距翻面尚有 %.3e 個門檻"
          % (TOL_AXIS, _marg, math.degrees(math.asin(min(1.0, _marg))), _marg / TOL_AXIS))
        P("     🔑 **其土地意義**：約束邊與 `m̂` 之夾角僅 **%.3f°〜%.3f°**——"
          "外接盒所漏者正是這幾度之傾斜（⛔ 非大角度之邊）。"
          % (math.degrees(math.acos(min(1.0, max(_dms)))),
             math.degrees(math.acos(min(1.0, min(_dms))))))
    if yi_rows:
        nch = sum(1 for y in yi_rows if y["chord"] is False)
        P("  🔒 交叉核：乙類中**弦區間式判在外**者 = **%d ／ %d** ⇒ %s"
          % (nch, len(yi_rows),
             "✅ 全數被弦區間式正確排除" if nch == len(yi_rows) else "🔴 **有殘留·具名**"))

    # ── 【H】P8 之第八法 ────────────────────────────────────────────────
    P("")
    P("【H／P8】`run_all` 清單筆數之**第八法**（🔒 檔案系統母體 × 引用交叉·⛔ 與七法不同族）")
    P("-" * W)
    hits, miss = run_all_count_method8()
    P("  母體 ＝ `verify/**.py`（⛔ 排除 `probes/`／`out/`／`baselines/`／`__pycache__`）")
    P("  🔒 **裸值（⛔ 未扣任何項）= %d**；逐筆附其於 `run_all.py` 之**行號與原文**（⇒ 扣除可稽核）"
      % len(hits))
    for cand, where in hits:
        P("     %-34s %s" % (cand, "; ".join("run_all.py:%d %s" % (ln, tx) for ln, tx in where)))
    POP(len(hits), len(hits), "第八法之命中（全列·含行號）")
    #  🔒 假陽性之**逐字判準**（⛔ 仍為字面測試·⛔ 未解析語法）：
    #     清單項之出現形恆為 `("<名>",`（名為 2-tuple 之首元素）；非清單項則否。
    ent = [(c, w) for c, w in hits if any(('("' + c + '",') in t for _l, t in w)]
    fp = [(c, w) for c, w in hits if (c, w) not in ent]
    P("  🔒 **假陽性之逐字判準**：清單項之出現形恆為 `(\"<名>\",`（tuple 首元素）；否則即非清單項。")
    for c, w in fp:
        P("     🔴 具名假陽性：%-30s @ %s"
          % (c, "; ".join("run_all.py:%d %s" % (ln, tx) for ln, tx in w)))
    P("     🔒 其性質與既用①③之假陽性（`run_all.py:80` 之 `endswith(\".py\")`）**同族**"
      "——量測器之已知邊界，⛔ 非清單有誤。")
    P("  ⇒ **第八法 ＝ 裸值 %d − 具名假陽性 %d ＝ %d**（施工單 `P8` 期望 **15**）⇒ %s"
      % (len(hits), len(fp), len(ent),
         "✅ 相符" if len(ent) == 15 else "🔴 **不符·⛔ 不調整預測·具名**"))
    P("  🔒 未被引用之 `verify/**.py` = %d（僅供對帳·⛔ 非清單）" % len(miss))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
