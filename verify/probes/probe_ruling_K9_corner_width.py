# -*- coding: utf-8 -*-
"""K-9-6／K-9-7 街角幾何實測 — **只量不判·不設門檻·不出合格/不合格**。

## 🔴 前版數字已全部作廢（帶深定義錯誤·K-9-6）

**本檔前版**（commit `b061b00`）以**畸零地附表之最小深度 `14.00`** 為量測帶深，
量出八街角之「截角前寬度」並逕與門檻比較。

**該帶深定義錯誤** ⇒ **前版所有寬度數字、以及據之而生之「翻盤／貼線」結論，全部作廢**。
（前版之 `verify/out/probe_ruling_K9_corner_width.{log,csv}` 已由本版覆寫；
凡他處引用前版數字者，皆已同批標作廢。）

**法規原文**（花蓮縣畸零地使用規則 §4·逐字）：

> 最小深度係指臨接之道路境界線至該基地後側境界線垂直距離之最小值。
> 最小寬度係指最小深度範圍內基地二側境界線間與道路境界線平行距離之最小值。
> 但道路境界線為曲線者，以該曲線與基地兩側境界線交點之連線視為道路境界線。

⇒ **「最小深度」是逐宗（逐範圍）量出來的量**（本案 33〜46m）；
附表之 `14.00` 是**可建築門檻**。**兩者嚴禁互代**（正典 K-9-6·失敗考古 #36 之形狀）。

## 本檔量什麼（A〜G·**皆只量不判**）

| 項 | 內容 |
|---|---|
| (A) | 逐街角**範圍**與逐街角**宗**之**自身最小深度**（K-9-6 定義·線性 ⇒ 只取兩端·**禁取樣**） |
| (B) | 寬度沿深度之斜率 `k`／深度沿 `t` 之斜率 `m`／寬度沿 `t` 之斜率 `c` |
| (C) | 八街角各落在 **K-9-7** 之哪一分支（①②③） |
| (D) | 以 (A) 之帶深重量最小寬度（**截角前／截角後**各一·兩情境全列） |
| (E) | **包含關係**：`街角規定範圍 ⊆ 街角第 1 宗` 是否成立·不成立差在哪 |
| (F) | 截角接合實距（頂點↔頂點 min ＋ 交集型態）＋**局部框重測**（E-10 同族） |
| (G) | `628-1(1)` 之 `−1.4826e-2m` 溯源：CAD 圖面既有？抑或程式產生？ |

⚠️ **符號注意**：本檔沿用**正典 K-9-7 之記號**——
`k` ＝ ∂w/∂d（寬度對深度）、`c` ＝ ∂w/∂t（寬度對 ALLOC 位移）。
而 `app._build_corner_range_v3` 內之區域變數 `k = sigma / den_a` 係**本檔之 `c`**
（`grep -n "k = sigma / den_a" app.py`）。**二者同名異義·勿混**（見 GB-14）。

## 量測方法（**不自寫幾何算法**）

- **斜率 (B) 一律以「擾動 app 自身函式之輸入、觀測其輸出」取得**
  ——`_build_corner_range_v3` 為**純函式**，且 W 對 `t`、`d` 皆仿射
  ⇒ 有限差分為**精確**（非數值近似）、且**以 app 為 oracle**，非另寫一份算式。
  線性性另以**兩組不同擾動量**互證（自由自檢·見 log【B】列之 `線性`）。
- **深度 (A)** 直接照 K-9-6 之定義式：臨街段兩端點至 **BASELINE 無限直線**之垂距取 min。
  線性 ⇒ **只取兩端·禁取樣**（K-8 §二 同一線性性質）。
- **寬度 (D)** 一律走 `app.parcel_min_width_n14`（唯一寬度原語），只換其 `min_depth` 引數。
- `EPS_TOUCH = 0.01` ＝ **法定粒度**（實施辦法 §3 長度 2dp·KL 域裁已鎖），
  與姊妹探針 `probe_ruling_N_e1_touch.py` 同源同值（`grep -n "EPS_TOUCH = " verify/probes/probe_ruling_N_e1_touch.py`）
  ——**非本檔自訂之容差**。

## 紀律

- ⛔ **未改 `app.py` 任何一行**。
- ⛔ **不掛 `run_all` 判定鏈**（`grep -n "probe" verify/run_all.py` ⇒ 本檔不在其中）。
- ⛔ **不代裁 U-K9-1／U-K9-2**——前提已換（帶深定義更正），兩題暫緩；本檔只出數字不出結論。
- rc **恆為 0**；唯缺件／取不到資料時 loud raise（no-silent-fallback）。

## 重跑

    python verify/probes/probe_ruling_K9_corner_width.py                    # 預設 data/V6.dxf
    python verify/probes/probe_ruling_K9_corner_width.py --dxf data/V6_1.dxf  # 平行對照

⛔ **預設值不得改**——`--dxf`／`WV_K9_DXF` 僅供**平行對照**，且只在本探針行程內
就地覆寫 `rv.V6DXF`；`run_verification.V6DXF` 之定義與其餘 ~20 個消費者**一律未動**。
非預設路徑之輸出**另存檔名**（`..._V6_1.log/.csv`），**不覆寫預設輪之輸出**。
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import LineString, Polygon                    # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")

# ── DXF 路徑之參數化（**預設一律不變**·段六）────────────────────────────────
#   ⛔ **生產路徑不動**：`run_verification.V6DXF` 之定義、`app.py`、以及其餘
#      ~20 個消費者**一律未改**，預設仍讀 `data/V6.dxf`。
#   本旗標**僅供本探針之平行對照**（V6 vs V6_1），且**只在本探針行程內**生效：
#   取得路徑後就地覆寫 `rv.V6DXF`，使下游 harness 呼叫（`build_pipeline`／
#   `build_build_parcels`）讀到同一檔——**不寫回任何檔案、不影響他行程**。
#   用法：`--dxf <path>` 或 `WV_K9_DXF=<path>`；**未給即為預設 V6.dxf**。
def _resolve_dxf():
    _p = None
    if "--dxf" in sys.argv:
        _i = sys.argv.index("--dxf")
        if _i + 1 >= len(sys.argv):
            raise RuntimeError("🔴 --dxf 未帶路徑（no-silent-fallback）")
        _p = sys.argv[_i + 1]
    _p = _p or os.environ.get("WV_K9_DXF") or None
    if _p is None:
        return rv.V6DXF, ""                      # ← 預設：**不變**
    _p = os.path.abspath(_p)
    if not os.path.exists(_p):
        raise RuntimeError(f"🔴 --dxf 指定之檔不存在：{_p}（no-silent-fallback）")
    _tag = "_" + os.path.splitext(os.path.basename(_p))[0]
    return _p, ("" if os.path.abspath(_p) == os.path.abspath(rv.V6DXF) else _tag)


DXF_PATH, _SFX = _resolve_dxf()
rv.V6DXF = DXF_PATH          # 行程內覆寫（見上·預設時此行為 no-op）

LOG = os.path.join(OUTDIR, f"probe_ruling_K9_corner_width{_SFX}.log")
CSV = os.path.join(OUTDIR, f"probe_ruling_K9_corner_width{_SFX}.csv")

# 法定粒度（實施辦法 §3 長度 2dp·KL 域裁已鎖）——同 probe_ruling_N_e1_touch.EPS_TOUCH
EPS_TOUCH = 0.01
# 面積之法定粒度（實施辦法 §3 第三位四捨五入）——同 app 之 E-8a 凸性閘寬
#   （`grep -n "面積之法定粒度" app.py`）。**非本檔自訂**；用於區辨
#   「真溢出」與「shapely 差集之浮點噪訊」（後者實測 ~1e-15㎡）。
EPS_AREA = 0.01
_LBIG = 1.0e5           # 無限直線之代理長度（同 app._build_corner_range_v3 之 _LBIG 口徑）

COLS = ["情境", "街廓", "側別", "街角第1宗",
        "範圍最小深度(m)", "宗最小深度(m)", "附表最小深(m)",
        "k=∂w/∂d", "m=-∂D/∂t", "c=∂w/∂t", "K-9-7分支",
        "寬度_截角前_新帶深(m)", "寬度_截角後_新帶深(m)",
        "寬度_截角前_舊帶深14(m)", "寬度_截角後_舊帶深14(m)",
        "範圍⊆宗", "範圍−宗 溢出(㎡)", "截角接合", "頂點最小距(m)", "局部框最小距(m)",
        # 🆕 K-9-8 第三代量測
        "K98_P", "K98_P落點", "K98_內縮量(m)", "K98_PQ長(m)", "K98_平行殘差",
        "K98_最小深度(m)", "K98_最小寬度(m)", "K98_虛擬塊面積(㎡)", "K98_虛擬−宗(㎡)",
        "K98_其中在街廓外(㎡)", "K98_其中在截角三角形內(㎡)", "K98_截角三角形面積(㎡)",
        "UK93_溢出(㎡)", "UK93_其中在截角三角形內(㎡)", "UK93_佔截角比", "UK93_落截角內比例",
        "UK93_在街廓內(㎡)", "UK93_在街廓外(㎡)", "UK93_位置s範圍", "UK93_位置t範圍",
        "UK93_形心st", "UK93_截角△s範圍"]

_END_OF = {"left": "p1_end", "right": "p2_end"}
_FORCED_OF = {"left": "left_forced_offset", "right": "right_forced_offset"}


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_K9_corner_width：{msg}（no-silent-fallback）")


def _md5(path):
    import hashlib
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _unit(v):
    n = float(np.linalg.norm(v))
    if n < 1e-12:
        _fail("方向向量退化為零")
    return v / n


def _inf_line(pt, u):
    return LineString([tuple(pt - u * _LBIG), tuple(pt + u * _LBIG)])


def _perp_dist_to_baseline(P, B0, bu):
    """點至 BASELINE **無限直線**之垂距（K-8 §一：BASELINE 恆為無限直線）。"""
    bn = np.array([-bu[1], bu[0]], float)
    return abs(float(np.dot(np.asarray(P, float)[:2] - B0, bn)))


def _front_seg_ends(poly, p1, d, n):
    """多邊形之**臨街段**（road-side chain）兩端點。

    🔴 **不可**以「|t| ≤ EPS_TOUCH」定義之——實測**部分多邊形之前緣側邊界並不落在
    FRONT_LINE 上**（退縮 0m 之 R1 左 **−0.1662m**、R3 右 **−0.0599m** 且**不平行**）。
    ⚠️ **段六更正**：該二值**非圖面落差**，而係「該範圍整個落在**截角區內**」所致
    （與「不扣截角」逐格同值、且退縮 3.5m 時回到 ~1e-5）。**圖面本身**之落差
    （V6 之 R4 右 `+0.014826m`）已由 `data/V6_1.dxf` 修正、全區 ≤ `7.6e-6m`。
    無論成因為何，以絕對 `t≈0` 篩選都會整段漏掉 ⇒ 仍須以多邊形自身極值為錨。

    改以**多邊形自身之前緣側極值**為錨：取 `t ≥ t_max − EPS_TOUCH` 之頂點鏈，
    再取其沿 `d` 之兩極值。不足 2 點（前緣邊不平行 FRONT）⇒ 退為 `t` 最大之兩點，
    並回報 `note` 明示之（**不靜默**）。

    回 (P_lo, P_hi, 段長, note)。
    """
    pts = [np.asarray(v[:2], float) for v in poly.exterior.coords]
    if len(pts) < 3:
        return None, None, 0.0, "頂點不足"
    tv = [float(np.dot(P - p1, n)) for P in pts]
    t_max = max(tv)
    on = [P for P, t in zip(pts, tv) if t >= t_max - EPS_TOUCH]
    note = f"前緣偏移 {t_max:+.6f}m"
    if len(on) < 2:
        order = sorted(range(len(pts)), key=lambda i: -tv[i])[:2]
        on = [pts[i] for i in order]
        note += "·⚠️ 前緣邊不平行 FRONT（退為 t 最大之兩點）"
    s = [float(np.dot(P - p1, d)) for P in on]
    return (on[int(np.argmin(s))], on[int(np.argmax(s))],
            max(s) - min(s), note)


def _own_min_depth(poly, p1, d, n, B0, bu, who):
    """K-9-6 之**自身最小深度**：臨街段各點至 BASELINE 垂距之 min。

    垂距沿臨街段**線性** ⇒ 最小值必落於兩端之一 ⇒ **只取兩端·禁取樣**。
    """
    A, B, L, note = _front_seg_ends(poly, p1, d, n)
    if A is None:
        return None, f"{who}：取不到臨街段（{note}）"
    dA = _perp_dist_to_baseline(A, B0, bu)
    dB = _perp_dist_to_baseline(B, B0, bu)
    return min(dA, dB), f"兩端 {dA:.4f}／{dB:.4f}·臨街段長 {L:.4f}m·{note}"


def _alloc_tau(poly, au, ref):
    """多邊形之 ALLOC 邊沿 ALLOC 法向之**有號位移**（相對固定參考點 ref）。

    只用於**差分**（Δτ ＝ Δt）⇒ 參考點之選擇不影響結果，故不需重建 Q0。
    """
    an = np.array([-au[1], au[0]], float)
    best, blen = None, -1.0
    cs = list(poly.exterior.coords)
    for P, Q in zip(cs[:-1], cs[1:]):
        v = np.asarray(Q, float)[:2] - np.asarray(P, float)[:2]
        n = float(np.linalg.norm(v))
        if n < 1e-9:
            continue
        if abs(abs(float(np.dot(v / n, au))) - 1.0) < 1e-6 and n > blen:
            best, blen = np.asarray(P, float)[:2], n
    if best is None:
        return None
    return float(np.dot(best - ref, an))



# ══════════════════════════════════════════════════════════════════════════
# K-9-8 虛擬量測塊（KL 裁 2026-08-02·canonical 見正典 `grep -n "^### K-9-8"`）
# ══════════════════════════════════════════════════════════════════════════
#  (1) L_in ＝ 該宗**往街廓內部那一側**之 ALLOC_LINE
#  (2) P   ＝ L_in ∩ **BLOCK 邊界**（可能落在截角邊，也可能落在與 FRONT 重疊之段）
#  (3) 自 P 作**平行 FRONT_LINE** 之線段，往街角方向延伸，**止於該宗靠街角側之境界線**
#      （街角第 1 宗 → SIDE_LINE）
#  (4) 虛擬塊 ＝ 該延伸線段、該宗二側境界線、BASELINE 所圍之多邊形
#  (5) **深度自該延伸線段起算**（⇒ `parcel_min_width_n14` 之 `front_pt` 取 P）
#  (6) P 落在與 FRONT 重疊段時，PQ 與 FRONT 重疊 ⇒ **退化**為自 FRONT 起算之原式
#  ⛔ **禁與街廓多邊形取交集**（取交集即把還原部分裁掉、等於沒還原）
#  ⛔ 虛擬塊**僅供量測**；其面積**禁進入任何面積帳**


def _line_x(P0, u0, P1, u1, who):
    """兩條**無限直線**之交點（P0+t·u0 與 P1+r·u1）。平行 ⇒ loud raise。"""
    den = u0[0] * (-u1[1]) - u0[1] * (-u1[0])
    if abs(den) < 1e-12:
        _fail(f"{who}：兩線平行、交點不存在")
    rhs = np.asarray(P1, float)[:2] - np.asarray(P0, float)[:2]
    t = (rhs[0] * (-u1[1]) - rhs[1] * (-u1[0])) / den
    return np.asarray(P0, float)[:2] + t * np.asarray(u0, float)[:2]


def _interior_alloc_edge(cc, au, d, p1, corner_s, who):
    """該宗**往街廓內部那一側**之 ALLOC 邊（＝平行 ALLOC 之邊中，s 離街角最遠者）。

    ⚠️ 須濾掉**零長邊**（實測 R6 右有一條 L=0.00 之退化邊）。
    """
    best = None
    ring = [np.asarray(c, float)[:2] for c in cc]
    for a, b in zip(ring, ring[1:] + ring[:1]):
        v = b - a
        L = float(np.linalg.norm(v))
        if L < 1e-6:                      # 零長邊 ⇒ 濾除（非靜默：見 docstring）
            continue
        if abs(abs(float(np.dot(v / L, au))) - 1.0) >= 1e-6:
            continue
        mid = (a + b) / 2.0
        s_mid = float(np.dot(mid - p1, d))
        if best is None or abs(s_mid - corner_s) > abs(best[0] - corner_s):
            best = (s_mid, a, b, L)
    if best is None:
        _fail(f"{who}：取不到平行 ALLOC 之側界邊")
    return best


def _k98_virtual_block(cc, blk_poly, p1, d, n, au, side_pts, base_pts,
                       corner_s, who):
    """建 K-9-8 虛擬量測塊。回 dict（**不與街廓取交集**）。"""
    A = _interior_alloc_edge(cc, au, d, p1, corner_s, who)
    s_in, ea, eb = A[0], A[1], A[2]
    # L_in ＝ 過該邊之無限直線（方向 au）
    # P ＝ L_in ∩ BLOCK 邊界：取**最靠前緣**（t 最大）之交點
    big = 1.0e5
    L_in = LineString([tuple(ea - au * big), tuple(ea + au * big)])
    inter = L_in.intersection(blk_poly.exterior)
    cand = []
    if inter.is_empty:
        _fail(f"{who}：L_in 與 BLOCK 邊界無交點")
    for g in (inter.geoms if hasattr(inter, "geoms") else [inter]):
        for c in (list(g.coords) if g.geom_type != "Point" else [g.coords[0]]):
            cand.append(np.asarray(c, float)[:2])
    P = max(cand, key=lambda q: float(np.dot(q - p1, n)))
    t_P = float(np.dot(P - p1, n))
    # P 落在截角邊，抑或落在與 FRONT 重疊之段？（K-9-7 新增之一層分支）
    on_front = abs(t_P) <= EPS_TOUCH
    # Q ＝ 過 P 之平行 FRONT 直線 ∩ SIDE_LINE（無限直線）
    su = _unit(np.asarray(side_pts[1], float)[:2] - np.asarray(side_pts[0], float)[:2])
    Q = _line_x(P, d, np.asarray(side_pts[0], float)[:2], su, who + "·PQ∩SIDE")
    # R ＝ L_in ∩ BASELINE； S ＝ SIDE_LINE ∩ BASELINE（皆無限直線）
    bu = _unit(np.asarray(base_pts[-1], float)[:2] - np.asarray(base_pts[0], float)[:2])
    B0 = np.asarray(base_pts[0], float)[:2]
    R = _line_x(P, au, B0, bu, who + "·L_in∩BASELINE")
    S = _line_x(np.asarray(side_pts[0], float)[:2], su, B0, bu, who + "·SIDE∩BASELINE")
    vb = Polygon([tuple(Q), tuple(P), tuple(R), tuple(S)])
    if not vb.is_valid:
        vb = vb.buffer(0)
    if vb.is_empty or vb.geom_type != "Polygon":
        _fail(f"{who}：虛擬塊非單一 Polygon（{vb.geom_type}）")
    return {"P": P, "Q": Q, "R": R, "S": S, "poly": vb, "t_P": t_P,
            "on_front": on_front, "s_in": s_in,
            "para_res": abs(abs(float(np.dot(_unit(Q - P), d))) - 1.0),
            "PQ_len": float(np.linalg.norm(Q - P))}


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L, rows = [], []
    by_pid_all = {}      # (情境, 街廓, 暫編地號) → g_row（供 F-2／G 之溯源）
    L.append("=" * 120)
    L.append("【K-9-6／K-9-7 街角幾何實測】**只量不判·不設門檻·不出合格/不合格**")
    L.append("🔴 **前版數字已全部作廢**（帶深誤用畸零地附表之 14.00·正典 K-9-6）"
             "——本檔為改寫版，勿引前版任何寬度數字。")
    L.append(f"DXF ＝ {os.path.relpath(DXF_PATH, REPO)}"
             f"{'（預設·生產路徑）' if not _SFX else '（**平行對照**·非生產路徑）'}"
             f"   md5 ＝ {_md5(DXF_PATH)}")
    L.append("=" * 120)

    ns, fake_st = harvest()
    width_fn = ns.get("parcel_min_width_n14")
    if not callable(width_fn):
        _fail("harvest 未取得 parcel_min_width_n14")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    front_lines = cad.get("front_lines") or {}
    sides_by = cad.get("side_lines_by_side", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    alloc_by = cad.get("alloc_dir_by_block", {}) or {}
    corners = [(lbl, w) for lbl in rv.CORNER_BLOCKS for w in ("left", "right")
               if w in (sides_by.get(lbl) or {})]
    if not corners:
        _fail("取不到任何街角側（side_lines_by_side 全空）")
    L.append(f"街角側共 {len(corners)} 個："
             f"{'、'.join(f'{b}/{s}' for b, s in corners)}")

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6_raw = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6_raw, list(cb_by.values()), snapshot)

    def _axes(blk):
        fl = (front_lines or {}).get(blk) or {}
        if not (fl.get("p1") and fl.get("p2")):
            _fail(f"{blk} 缺 FRONT_LINE")
        p1 = np.asarray(fl["p1"], float)[:2]
        d = _unit(np.asarray(fl["p2"], float)[:2] - p1)
        n = np.array([-d[1], d[0]], float)
        mb = bl_by.get(blk) or {}
        bp = ns["_baseline_pts_from_manual"](mb, cb_by[blk]["vertices"])
        if not (bp and len(bp) >= 2):
            _fail(f"{blk} 缺 BASELINE")
        B0 = np.asarray(bp[0], float)[:2]
        bu = _unit(np.asarray(bp[-1], float)[:2] - B0)
        au = _unit(np.asarray(alloc_by[blk], float)[:2])
        return p1, d, n, B0, bu, au, bp

    def _build_range(blk, side, setback, **over):
        """呼叫 app 之受測函式（**唯一街角範圍原語**）。擾動用 `over`。"""
        b = cb_by[blk]
        mb = bl_by[blk]
        fl = front_lines[blk]
        sd = sides_by[blk][side]
        mw = float(ns["get_min_lot_size"](
            b["category"], float(snapshot["blocks"][blk]["正面"]["路寬_m"]))["min_width"])
        kw = dict(block_vertices=b["vertices"], block_centroid=b["centroid"],
                  front_pts=[fl["p1"], fl["p2"]],
                  baseline_pts=ns["_baseline_pts_from_manual"](mb, b["vertices"]),
                  side_line_pts=[sd["p1"], sd["p2"]],
                  alloc_dir=alloc_by[blk],
                  block_depth=float(snapshot["blocks"][blk]["街廓分配深度_m"]),
                  setback=setback, min_width=mw,
                  chamfer_tri=ns["_make_chamfer_tri_wb"](b, side),
                  dxf_quantum=(mb.get("_match") or {}).get("q_detected"),
                  _label=blk, _side=side)
        kw.update(over)
        return ns["_build_corner_range_v3"](**kw), mw, kw["block_depth"]

    # ══ (B)(C) 斜率與分支：以擾動 app 自身函式取得（純函式＋仿射 ⇒ 差分為精確）══
    L.append("")
    L.append("【B】【C】斜率與 K-9-7 分支（**以擾動 app 函式輸入取得·非另寫算式**）")
    L.append("-" * 120)
    L.append(f"  {'街廓側':11}{'c=∂w/∂t':>11}{'c線性':>7}{'k=∂w/∂d':>11}"
             f"{'m=-∂D/∂t':>11}{'m線性':>7}{'分支':>7}  說明")
    slope = {}
    for blk, side in corners:
        p1, d, n, B0, bu, au, bp = _axes(blk)
        ref = p1
        # c：擾動 min_width（δ 與 2δ 互證線性·仿射 ⇒ 應逐位相等）
        r0, mw0, D0 = _build_range(blk, side, 0.0)
        t0 = _alloc_tau(r0, au, ref)
        cs = []
        for dlt in (0.5, 1.0):
            rr, _, _ = _build_range(blk, side, 0.0, min_width=mw0 + dlt)
            tt = _alloc_tau(rr, au, ref)
            if t0 is None or tt is None:
                _fail(f"{blk}/{side} 取不到範圍多邊形之 ALLOC 邊")
            cs.append(dlt / (tt - t0))
        c_lin = abs(cs[0] - cs[1]) <= 1e-9 * max(1.0, abs(cs[0]))
        c = cs[0]
        # k：擾動 block_depth。Δτ==0 ⇒ min 在 d=0 ⇒ k ≥ 0；否則 k = −c·Δτ/ΔD
        dD = 1.0
        rD, _, _ = _build_range(blk, side, 0.0, block_depth=D0 + dD)
        tD = _alloc_tau(rD, au, ref)
        dtau = tD - t0
        if abs(dtau) <= 1e-12:
            k, kmsg = 0.0, "k ≥ 0（帶深不影響 t* ⇒ 寬度 min 恆在 d=0）"
        else:
            k = -c * dtau / dD
            kmsg = f"k < 0（帶深影響 t*·Δτ/ΔD={dtau / dD:+.6f}）"
        # m ＝ −∂D/∂t：**直接量範圍自身之最小深度 D(t)**（K-9-6 定義），三點差分。
        #   ⛔ **不走「dD/ds × ds/dt」之連鎖律**——實測其於 R1 左／R3 右 得出
        #      |ds/dt| ≈ 6.8／7.0，而由構造 |ds/dt| ＝ |1/den_a| ＝ |c| ≈ 1.00
        #      ⇒ 該路徑於「臨街段鏈跳段」時失效（街廓前緣邊界為折線）。
        #   改以三點量 D(t) 並**互證線性**：非線性即代表臨街段鏈跳段，據實報 `🔴 非線性`。
        Dts = []
        for dlt in (0.0, 0.5, 1.0):
            rr = r0 if dlt == 0.0 else _build_range(
                blk, side, 0.0, min_width=mw0 + dlt)[0]
            _dv, _ = _own_min_depth(rr, p1, d, n, B0, bu, "範圍")
            if _dv is None:
                _fail(f"{blk}/{side} 範圍取不到自身最小深度（δ={dlt}）")
            Dts.append(_dv)
        dt_1 = 0.5 / c
        m1 = -(Dts[1] - Dts[0]) / dt_1
        m2 = -(Dts[2] - Dts[1]) / dt_1
        m_lin = abs(m1 - m2) <= 1e-6 * max(1.0, abs(m1))
        m = m1
        branch = ("①（k ≥ 0·深度不影響）" if k >= 0
                  else ("②（k<0·D 常數）" if abs(m) <= 1e-9
                        else "③（k<0·D 隨 t 變）"))
        if not m_lin:
            branch += "⚠️非線性"
        # 前緣偏移：範圍多邊形之前緣側極值 t（＝街廓多邊形前緣邊界 vs FRONT_LINE 之落差）
        _tv_r = [float(np.dot(np.asarray(v[:2], float) - p1, n))
                 for v in r0.exterior.coords]
        _t_front = max(_tv_r, key=abs) if False else _tv_r[int(np.argmax(_tv_r))]
        _has_par = any(
            abs(abs(float(np.dot(_unit(np.asarray(Q, float)[:2]
                                       - np.asarray(P, float)[:2]), d))) - 1.0) < 1e-6
            for P, Q in zip(list(r0.exterior.coords)[:-1], list(r0.exterior.coords)[1:])
            if float(np.linalg.norm(np.asarray(Q, float)[:2]
                                    - np.asarray(P, float)[:2])) > 1e-9)
        slope[(blk, side)] = dict(c=c, k=k, m=m, branch=branch,
                                  c_lin=c_lin, m_lin=m_lin, kmsg=kmsg,
                                  Dts=Dts, m2=m2,
                                  t_front=_t_front, has_par=_has_par)
        L.append(f"  {blk + '/' + side:11}{c:>11.6f}{'✅' if c_lin else '🔴':>7}"
                 f"{k:>11.6f}{m:>11.6f}{'✅' if m_lin else '🔴':>7}"
                 f"{branch.split('（')[0]:>7}  {kmsg}"
                 f"·D(t) 三點 {Dts[0]:.4f}/{Dts[1]:.4f}/{Dts[2]:.4f}"
                 f"·m2={m2:+.6f}")

    # ══ 前緣偏移（**新發現·GB-15 之實料**）═════════════════════════════════
    L.append("")
    L.append("【前緣偏移】**街角規定範圍多邊形自身**之前緣側極值 t（退縮 0m）")
    L.append("-" * 120)
    L.append("  🔴 **勿誤讀為『圖面落差』**（段六更正·原 GB-15 之誤歸因）：")
    L.append("     本欄係該**範圍多邊形自身**之前緣側極值。退縮 0m 時該範圍可能**整個落在")
    L.append("     截角區內**，其極值遂落在**截角邊**上——此與圖面畫得準不準**無關**。")
    L.append("     實證：本欄與『不扣截角』之值**逐格相同**（故非扣截角所致），")
    L.append("     且同一街角於退縮 3.5m 時回到 ~1e-5（範圍夠大、已越過截角）。")
    L.append("     **真正之圖面落差**＝各街廓多邊形本身 vs FRONT_LINE，")
    L.append("     見 `verify/tools/verify_dxf_v6_1.py` 之【5b】（V6_1 全區 ≤ 7.6e-6m）。")
    L.append(f"  {'街廓側':11}{'前緣偏移(m)':>14}{'有平行FRONT之邊':>18}")
    for blk, side in corners:
        sl = slope[(blk, side)]
        L.append(f"  {blk + '/' + side:11}{sl['t_front']:>+14.6f}"
                 f"{('✅ 有' if sl['has_par'] else '🔴 無（不平行）'):>18}")

    # ══ 逐情境 × 逐街角 ═══════════════════════════════════════════════════
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _md_tbl = {str(p["街廓"]): float(p.get("法定最小深(m)", 0) or 0) for p in params}
        _d2, _sel, _off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build_parcels, winners_state, forced_map, setback)
        for _r0 in sg["g_rows"]:
            by_pid_all[(tag, str(_r0.get("所屬街廓", "")),
                        str(_r0.get("暫編地號", "")))] = _r0
        by_pid = {(str(r.get("所屬街廓", "")), str(r.get("暫編地號", ""))): r
                  for r in sg["g_rows"]}

        for blk, side in corners:
            p1, d, n, B0, bu, au, bp = _axes(blk)
            sl = slope[(blk, side)]
            rng, mw, _D0 = _build_range(blk, side, setback)
            rng_depth, rng_note = _own_min_depth(rng, p1, d, n, B0, bu, "範圍")
            rec = {"情境": tag, "街廓": blk, "側別": side,
                   "附表最小深(m)": f"{_md_tbl[blk]:.2f}",
                   "範圍最小深度(m)": ("—" if rng_depth is None else f"{rng_depth:.4f}"),
                   "k=∂w/∂d": f"{sl['k']:.6f}", "m=-∂D/∂t": f"{sl['m']:.6f}",
                   "c=∂w/∂t": f"{sl['c']:.6f}", "K-9-7分支": sl["branch"]}
            pid = (winners_state.get(blk) or {}).get(_END_OF[side])
            if not pid:
                _why = ("強制留設抵費地"
                        if (forced_map.get(blk) or {}).get(_FORCED_OF[side])
                        else "無街角 winner")
                rec.update({"街角第1宗": f"—（{_why}）", "宗最小深度(m)": "—",
                            "寬度_截角前_新帶深(m)": "—", "寬度_截角後_新帶深(m)": "—",
                            "寬度_截角前_舊帶深14(m)": "—", "寬度_截角後_舊帶深14(m)": "—",
                            "範圍⊆宗": "—", "範圍−宗 溢出(㎡)": "—",
                            "截角接合": "—", "頂點最小距(m)": "—", "局部框最小距(m)": "—"})
                rows.append(rec)
                continue
            r = by_pid.get((blk, str(pid)))
            if r is None:
                _fail(f"[{tag}] {blk}/{side} winner {pid} 不在 g_rows")
            cc = r.get("cut_coords") or []
            if len(cc) < 3:
                _fail(f"[{tag}] {blk}/{side} {pid} cut_coords 不足（{len(cc)} 點）")
            par = Polygon([(float(x[0]), float(x[1])) for x in cc])
            par_depth, par_note = _own_min_depth(par, p1, d, n, B0, bu, "宗")
            tri = ns["_make_chamfer_tri_wb"](cb_by[blk], side)

            # (D) 以新帶深重量寬度；舊帶深 14.00 併列以顯落差
            def _w2(coords, dh, fp, md, lab):
                """走 `parcel_min_width_n14`（唯一寬度原語）·front_pt 可指定（K-9-8 (5)）。"""
                if md is None or md <= 0:
                    return "—"
                try:
                    return f"{float(width_fn(coords, dh, fp, md, _label=lab)):.4f}"
                except RuntimeError as e:
                    return "raise:" + str(e).split("：", 1)[-1].splitlines()[0][:40]

            def _w(coords, md, lab):
                if md is None or md <= 0:
                    return "—"
                try:
                    return f"{float(width_fn(coords, tuple(d), tuple(p1), md, _label=lab)):.4f}"
                except RuntimeError as e:
                    return "raise:" + str(e).split("：", 1)[-1].splitlines()[0][:34]

            pre = None
            if tri is not None and par.union(tri).geom_type == "Polygon":
                pre = list(par.union(tri).exterior.coords)
            _newmd = par_depth
            rec["宗最小深度(m)"] = ("—" if par_depth is None else f"{par_depth:.4f}")
            rec["寬度_截角後_新帶深(m)"] = _w(cc, _newmd, f"{blk}·{pid}·後·新")
            rec["寬度_截角後_舊帶深14(m)"] = _w(cc, _md_tbl[blk], f"{blk}·{pid}·後·舊")
            rec["寬度_截角前_新帶深(m)"] = (_w(pre, _newmd, f"{blk}·{pid}·前·新")
                                     if pre else "—（非邊接合）")
            rec["寬度_截角前_舊帶深14(m)"] = (_w(pre, _md_tbl[blk], f"{blk}·{pid}·前·舊")
                                       if pre else "—（非邊接合）")

            # (E) 包含關係
            over = rng.difference(par)
            _oa = float(over.area)
            if _oa <= EPS_AREA:
                rec["範圍⊆宗"] = ("✅ 成立" if _oa == 0.0
                                else f"✅ 成立（噪訊 {_oa:.2e}㎡ ≤ 法定粒度）")
            else:
                rec["範圍⊆宗"] = "🔴 不成立"
            rec["範圍−宗 溢出(㎡)"] = f"{_oa:.6f}"

            # (F) 截角接合：交集型態 ＋ 頂點↔頂點最小距 ＋ 局部框重測
            if tri is None:
                rec.update({"截角接合": "無截角", "頂點最小距(m)": "—",
                            "局部框最小距(m)": "—"})
            else:
                inter = par.intersection(tri)
                kind = ("邊接合" if inter.geom_type in ("LineString", "MultiLineString")
                        else ("點接合" if inter.geom_type == "Point" else inter.geom_type))
                pv = [np.asarray(v[:2], float) for v in par.exterior.coords]
                tv = [np.asarray(v[:2], float) for v in tri.exterior.coords]
                vmin = min(float(np.linalg.norm(a - b)) for a in pv for b in tv)
                # 局部框（E-10 同族）：以 FRONT p1 為原點、(d,n) 為軸之剛體變換後重測
                def _loc(P):
                    q = P - p1
                    return np.array([float(np.dot(q, d)), float(np.dot(q, n))])
                pl = [_loc(a) for a in pv]
                tl = [_loc(b) for b in tv]
                vmin_l = min(float(np.linalg.norm(a - b)) for a in pl for b in tl)
                rec.update({"截角接合": f"{kind}（{inter.geom_type}）",
                            "頂點最小距(m)": f"{vmin:.3e}",
                            "局部框最小距(m)": f"{vmin_l:.3e}"})
            # ── 🆕 K-9-8 虛擬量測塊（第三代量測·**只量不判**）────────────────
            _who = f"{tag}·{blk}/{side}·{pid}"
            _blkpoly = Polygon([(float(v[0]), float(v[1]))
                                for v in cb_by[blk]["vertices"]])
            if not _blkpoly.is_valid:
                _blkpoly = _blkpoly.buffer(0)
            _sl = sides_by[blk][side]
            _su = _unit(np.asarray(_sl["p2"], float)[:2]
                        - np.asarray(_sl["p1"], float)[:2])
            _sn = np.array([-_su[1], _su[0]], float)
            _corner_s = float(np.dot(np.asarray(_sl["p1"], float)[:2] - p1, _sn)
                              / np.dot(d, _sn))
            _vb = _k98_virtual_block(cc, _blkpoly, p1, d, n, au,
                                     [_sl["p1"], _sl["p2"]], bp, _corner_s, _who)
            # (A)(B) P／PQ 之讀數
            rec["K98_P"] = f"({_vb['P'][0]:.4f}, {_vb['P'][1]:.4f})"
            rec["K98_P落點"] = ("FRONT 重疊段（**退化**）" if _vb["on_front"]
                              else f"截角邊（t_P={_vb['t_P']:+.6f}m）")
            rec["K98_內縮量(m)"] = f"{-_vb['t_P']:+.6f}"
            rec["K98_PQ長(m)"] = f"{_vb['PQ_len']:.4f}"
            rec["K98_平行殘差"] = f"{_vb['para_res']:.3e}"
            # (D) 依 K-9-8 重量：深度自 PQ 起算 ⇒ front_pt 取 P
            _vbc = list(_vb["poly"].exterior.coords)
            _dep_k98, _dep_note = _own_min_depth(_vb["poly"], _vb["P"], d, n,
                                                 B0, bu, "虛擬塊")
            rec["K98_最小深度(m)"] = ("—" if _dep_k98 is None else f"{_dep_k98:.4f}")
            rec["K98_最小寬度(m)"] = _w2(_vbc, tuple(d), tuple(_vb["P"]),
                                      _dep_k98, f"{_who}·K98")
            # (C) 虛擬塊 − 實際宗地：差集面積與其是否落在截角區內
            _diff = _vb["poly"].difference(par)
            rec["K98_虛擬塊面積(㎡)"] = f"{_vb['poly'].area:.4f}"
            rec["K98_虛擬−宗(㎡)"] = f"{_diff.area:.6f}"
            _outside = _diff.difference(_blkpoly)          # 落在街廓之外者
            rec["K98_其中在街廓外(㎡)"] = f"{_outside.area:.6f}"
            if tri is not None:
                _in_tri = _diff.intersection(tri)
                rec["K98_其中在截角三角形內(㎡)"] = f"{_in_tri.area:.6f}"
                rec["K98_截角三角形面積(㎡)"] = f"{tri.area:.6f}"
            else:
                rec["K98_其中在截角三角形內(㎡)"] = "—"
                rec["K98_截角三角形面積(㎡)"] = "—"
            # U-K9-3 專項：前版之「範圍−宗」溢出多邊形是否落在截角區內
            if tri is not None and over.area > EPS_AREA:
                _ov_in = over.intersection(tri).area
                rec["UK93_溢出(㎡)"] = f"{over.area:.6f}"
                rec["UK93_其中在截角三角形內(㎡)"] = f"{_ov_in:.6f}"
                rec["UK93_佔截角比"] = f"{100.0 * over.area / tri.area:.1f}%"
                rec["UK93_落截角內比例"] = (f"{100.0 * _ov_in / over.area:.2f}%"
                                      if over.area > 0 else "—")
                # 🔎 溢出多邊形之**所在位置**（純量測·不解釋）：
                #    在街廓內／外、其 (s,t) 局部框範圍與形心
                _ov_in_blk = over.intersection(_blkpoly).area
                _ov_out_blk = over.difference(_blkpoly).area
                _ovc = [(float(np.dot(np.asarray(v[:2], float) - p1, d)),
                         float(np.dot(np.asarray(v[:2], float) - p1, n)))
                        for v in over.exterior.coords] if over.geom_type == "Polygon"                     else [(float(np.dot(np.asarray(v[:2], float) - p1, d)),
                           float(np.dot(np.asarray(v[:2], float) - p1, n)))
                          for g in over.geoms for v in g.exterior.coords]
                _cen = over.centroid
                rec["UK93_在街廓內(㎡)"] = f"{_ov_in_blk:.6f}"
                rec["UK93_在街廓外(㎡)"] = f"{_ov_out_blk:.6f}"
                rec["UK93_位置s範圍"] = (f"[{min(x for x, _ in _ovc):.3f},"
                                     f"{max(x for x, _ in _ovc):.3f}]")
                rec["UK93_位置t範圍"] = (f"[{min(t for _, t in _ovc):.3f},"
                                     f"{max(t for _, t in _ovc):.3f}]")
                rec["UK93_形心st"] = (
                    f"({float(np.dot(np.asarray(_cen.coords[0], float)[:2] - p1, d)):.3f},"
                    f"{float(np.dot(np.asarray(_cen.coords[0], float)[:2] - p1, n)):.3f})")
                rec["UK93_截角△s範圍"] = (
                    f"[{min(float(np.dot(np.asarray(v[:2], float) - p1, d)) for v in tri.exterior.coords):.3f},"
                    f"{max(float(np.dot(np.asarray(v[:2], float) - p1, d)) for v in tri.exterior.coords):.3f}]")
            else:
                for _k in ("UK93_溢出(㎡)", "UK93_其中在截角三角形內(㎡)",
                           "UK93_佔截角比", "UK93_落截角內比例",
                           "UK93_在街廓內(㎡)", "UK93_在街廓外(㎡)", "UK93_位置s範圍",
                           "UK93_位置t範圍", "UK93_形心st", "UK93_截角△s範圍"):
                    rec[_k] = "—"
            rec["街角第1宗"] = str(pid)
            rec["_rng_note"] = rng_note
            rec["_par_note"] = par_note or ""
            rec["_k98_note"] = _dep_note
            rows.append(rec)

    # ══ 列印 ════════════════════════════════════════════════════════════
    for tag in ("0m", "3.5m"):
        L.append("")
        L.append(f"【A】【D】[{tag}] 自身最小深度 與 據之重量之最小寬度"
                 f"（**舊帶深 14.00 併列以顯落差**）")
        L.append("-" * 120)
        L.append(f"  {'街廓':5}{'側':>6}{'街角第1宗':>15}{'範圍深':>9}{'宗深':>9}"
                 f"{'附表深':>8}{'前·新':>10}{'後·新':>10}{'前·舊14':>10}{'後·舊14':>10}")
        for r in [x for x in rows if x["情境"] == tag]:
            L.append(f"  {r['街廓']:5}{r['側別']:>6}{r['街角第1宗']:>15}"
                     f"{r['範圍最小深度(m)']:>9}{r['宗最小深度(m)']:>9}"
                     f"{r['附表最小深(m)']:>8}{r['寬度_截角前_新帶深(m)']:>10}"
                     f"{r['寬度_截角後_新帶深(m)']:>10}{r['寬度_截角前_舊帶深14(m)']:>10}"
                     f"{r['寬度_截角後_舊帶深14(m)']:>10}")

    # ══ 🆕 K-9-8 第三代量測 ═══════════════════════════════════════════════
    L.append("")
    L.append("【K-9-8-A/B】P 之落點（K-9-7 新增分支）與延伸線段 PQ")
    L.append("-" * 120)
    L.append("  P ＝ L_in（該宗往街廓內側之 ALLOC_LINE）∩ BLOCK 邊界；")
    L.append("  PQ ＝ 自 P 平行 FRONT、往街角延伸至 SIDE_LINE。深度自 PQ 起算（K-9-8 (5)）。")
    L.append(f"  {'情境':6}{'街廓側':11}{'街角第1宗':>15}{'內縮量(m)':>12}"
             f"{'PQ長(m)':>10}{'平行殘差':>11}  P 落點")
    for r in rows:
        if r.get("K98_P落點", "—") == "—":
            continue
        L.append(f"  {r['情境']:6}{r['街廓'] + '/' + r['側別']:11}{r['街角第1宗']:>15}"
                 f"{r['K98_內縮量(m)']:>12}{r['K98_PQ長(m)']:>10}"
                 f"{r['K98_平行殘差']:>11}  {r['K98_P落點']}")

    L.append("")
    L.append("【K-9-8-C】虛擬塊 − 實際宗地：差集落在哪裡（**禁與街廓取交集**·故差集本應外溢）")
    L.append("-" * 120)
    L.append(f"  {'情境':6}{'街廓側':11}{'虛擬塊(㎡)':>12}{'虛擬−宗(㎡)':>13}"
             f"{'其中在街廓外':>13}{'其中在截角△內':>14}{'截角△(㎡)':>11}")
    for r in rows:
        if r.get("K98_P落點", "—") == "—":
            continue
        L.append(f"  {r['情境']:6}{r['街廓'] + '/' + r['側別']:11}"
                 f"{r['K98_虛擬塊面積(㎡)']:>12}{r['K98_虛擬−宗(㎡)']:>13}"
                 f"{r['K98_其中在街廓外(㎡)']:>13}"
                 f"{r['K98_其中在截角三角形內(㎡)']:>14}"
                 f"{r['K98_截角三角形面積(㎡)']:>11}")

    L.append("")
    L.append("【K-9-8-C·U-K9-3 專項】前版「範圍−宗」溢出多邊形**是否確實落在截角區內**")
    L.append("-" * 120)
    L.append("  若是 ⇒ 『包含關係不成立』非缺陷（虛擬塊本應含還原角）⇒ **U-K9-3 可撤回**。")
    L.append("  若否 ⇒ **停機上呈**（本探針不自行解釋）。")
    L.append(f"  {'情境':6}{'街廓側':11}{'溢出(㎡)':>11}{'其中在截角△內':>14}"
             f"{'落截角內比例':>13}{'溢出佔截角△':>13}")
    _uk93_bad = []
    for r in rows:
        if r.get("UK93_溢出(㎡)", "—") == "—":
            continue
        L.append(f"  {r['情境']:6}{r['街廓'] + '/' + r['側別']:11}"
                 f"{r['UK93_溢出(㎡)']:>11}{r['UK93_其中在截角三角形內(㎡)']:>14}"
                 f"{r['UK93_落截角內比例']:>13}{r['UK93_佔截角比']:>13}")
        try:
            if float(str(r["UK93_落截角內比例"]).rstrip("%")) < 99.99:
                _uk93_bad.append(f"{r['情境']} {r['街廓']}/{r['側別']}")
        except ValueError:
            _uk93_bad.append(f"{r['情境']} {r['街廓']}/{r['側別']}（比例無法解析）")
    L.append("")
    L.append("  🔎 溢出多邊形之**所在位置**（純量測·本探針不解釋）：")
    L.append(f"     {'情境':6}{'街廓側':11}{'在街廓內':>11}{'在街廓外':>11}"
             f"{'溢出 s 範圍':>18}{'截角△ s 範圍':>18}{'形心(s,t)':>20}")
    for r in rows:
        if r.get("UK93_溢出(㎡)", "—") == "—":
            continue
        L.append(f"     {r['情境']:6}{r['街廓'] + '/' + r['側別']:11}"
                 f"{r['UK93_在街廓內(㎡)']:>11}{r['UK93_在街廓外(㎡)']:>11}"
                 f"{r['UK93_位置s範圍']:>18}{r['UK93_截角△s範圍']:>18}"
                 f"{r['UK93_形心st']:>20}")
    if _uk93_bad:
        L.append(f"  🔴 **有溢出未完全落在截角三角形內**：{_uk93_bad}"
                 f" ⇒ **停機上呈**（本探針不代解釋·裁量在 KL）")
    else:
        L.append("  ✅ **全部溢出皆完全落在截角三角形內**（≥99.99%）"
                 " ⇒ 支持『U-K9-3 係方法產物、非缺陷』之判讀（**裁量仍在 KL**）")

    L.append("")
    L.append("【K-9-8-D】三代量測併列（最小深度／最小寬度）")
    L.append("-" * 120)
    L.append("  一代＝帶深誤用附表 14.00（已作廢）；二代＝自身最小深度＋`cut_coords`（已作廢）；")
    L.append("  **三代＝K-9-8 虛擬還原塊＋深度自 PQ 起算**。")
    L.append(f"  {'情境':6}{'街廓側':11}{'街角第1宗':>15}"
             f"{'深:二代':>10}{'深:三代':>10}{'寬:一代14':>11}{'寬:二代':>10}{'寬:三代':>10}")
    for r in rows:
        if r.get("K98_P落點", "—") == "—":
            continue
        L.append(f"  {r['情境']:6}{r['街廓'] + '/' + r['側別']:11}{r['街角第1宗']:>15}"
                 f"{r['宗最小深度(m)']:>10}{r['K98_最小深度(m)']:>10}"
                 f"{r['寬度_截角後_舊帶深14(m)']:>11}{r['寬度_截角後_新帶深(m)']:>10}"
                 f"{r['K98_最小寬度(m)']:>10}")

    L.append("")
    L.append("【E】包含關係查核：`街角規定範圍 ⊆ 街角第 1 宗`？")
    L.append("-" * 120)
    L.append("  （KL 推論：兩者皆為「街廓 ∩ 平行 ALLOC 半平面」⇒ G ≥ 範圍面積 應蘊含包含關係）")
    for r in rows:
        if r["範圍⊆宗"] == "—":
            continue
        L.append(f"  {r['情境']:5}{r['街廓']:4}{r['側別']:>6} {r['街角第1宗']:>14}  "
                 f"{r['範圍⊆宗']}·範圍−宗 溢出 {r['範圍−宗 溢出(㎡)']}㎡")

    L.append("")
    L.append("【F】截角接合實距（頂點↔頂點 min）＋ **局部框重測**（E-10 同族）")
    L.append("-" * 120)
    L.append("  ⚠️ KL 圖示：R1 左 連得起來、R4 右 連不起來。前版兩者皆判「點接合」。")
    for r in rows:
        if r["截角接合"] == "—":
            continue
        L.append(f"  {r['情境']:5}{r['街廓']:4}{r['側別']:>6} {r['街角第1宗']:>14}  "
                 f"{r['截角接合']:28} 絕對框 {r['頂點最小距(m)']:>11}"
                 f"  局部框 {r['局部框最小距(m)']:>11}")

    # ── (F)-2 點接合者之接觸組態（KL 圖示對拍用）────────────────────────────
    L.append("")
    L.append("【F-2】**點接合**者之接觸組態（局部框 (s,t)·s 沿 FRONT／t 為 FRONT 法向）")
    L.append("-" * 120)
    L.append("  假說「R1 左係次微米級座標不合之假點接合」⇒ 由上表 **絕對框／局部框皆 0.000e+00**")
    L.append("  （＝**頂點完全重合**、非近似）**否證**。以下列出接觸點與兩多邊形之局部座標。")
    _seen = set()
    for r in rows:
        if not str(r.get("截角接合", "")).startswith("點接合"):
            continue
        key = (r["街廓"], r["側別"], r["街角第1宗"])
        if key in _seen:
            continue
        _seen.add(key)
        blk, side, pid = key
        p1, d, n, B0, bu, au, bp = _axes(blk)
        rr = by_pid_all[(r["情境"], blk, pid)]
        par = Polygon([(float(x[0]), float(x[1])) for x in rr.get("cut_coords")])
        tri = ns["_make_chamfer_tri_wb"](cb_by[blk], side)
        inter = par.intersection(tri)
        cp = np.asarray(inter.coords[0], float)[:2] if inter.geom_type == "Point" else None

        def _loc2(P):
            q = np.asarray(P, float)[:2] - p1
            return (float(np.dot(q, d)), float(np.dot(q, n)))
        L.append(f"  {blk}/{side} {pid}（情境 {r['情境']}）"
                 f"  接觸點 (s,t)＝{'—' if cp is None else _loc2(cp)}")
        L.append(f"      截角三角形頂點 (s,t)："
                 f"{[tuple(round(v, 4) for v in _loc2(v2)) for v2 in list(tri.exterior.coords)[:-1]]}")
        _pv = [(_loc2(v)) for v in list(par.exterior.coords)[:-1]]
        _pv.sort(key=lambda st: -st[1])
        L.append(f"      宗之最靠前緣三頂點 (s,t)："
                 f"{[tuple(round(x, 4) for x in v) for v in _pv[:3]]}")

    # ── (G) −1.4826e-2 溯源 ────────────────────────────────────────────────
    L.append("")
    L.append("【G】`628-1(1)` 之 `−1.4826e-2m` 溯源：CAD 圖面既有？抑或程式產生？")
    L.append("-" * 120)
    _gb = "R4"
    p1, d, n, B0, bu, au, bp = _axes(_gb)
    _bv = [np.asarray(v[:2], float) for v in cb_by[_gb]["vertices"]]
    _bt = [float(np.dot(P - p1, n)) for P in _bv]
    _i = int(np.argmax(_bt))
    L.append(f"  ① **街廓 {_gb} 多邊形**（`cb_by['{_gb}']['vertices']`·W-A.3 方案B **直讀**"
             f" DXF BLOCK 閉合多邊形）")
    L.append(f"     其 t 最大之頂點 ＝ ({_bv[_i][0]:.6f}, {_bv[_i][1]:.6f})，"
             f"t ＝ **{_bt[_i]:+.6f}m**")
    _rr = by_pid_all.get(("0m", _gb, "628-1(1)"))
    if _rr is not None:
        _pv2 = [np.asarray(v[:2], float) for v in _rr.get("cut_coords")]
        _pt2 = [float(np.dot(P - p1, n)) for P in _pv2]
        _j = int(np.argmax(_pt2))
        _dist = float(np.linalg.norm(_pv2[_j] - _bv[_i]))
        L.append(f"  ② **宗 `628-1(1)` 之 cut_coords** t 最大之頂點 ＝ "
                 f"({_pv2[_j][0]:.6f}, {_pv2[_j][1]:.6f})，t ＝ **{_pt2[_j]:+.6f}m**")
        L.append(f"  ③ **①②兩頂點之距離 ＝ {_dist:.3e} m**"
                 f"{'（＝同一點）' if _dist < 1e-9 else '（不同點·須續追）'}")
    # ④ 回到原始 DXF：BLOCK 圖層是否本來就有該點
    try:
        import ezdxf as _ez
        _doc = _ez.readfile(rv.V6DXF, encoding="cp950")
        _hit, _best, _skipped = None, None, []
        for _e in _doc.modelspace():
            if _e.dxf.layer != "BLOCK":
                continue
            # BLOCK 圖層實為舊式 `POLYLINE`（`.vertices`），非 `LWPOLYLINE`（`.get_points()`）
            #   ⇒ 兩式皆試；**皆不通即記錄**，不靜默跳過。
            _pts = []
            if _e.dxftype() == "POLYLINE":
                _pts = [(float(_v.dxf.location[0]), float(_v.dxf.location[1]))
                        for _v in _e.vertices]
            elif hasattr(_e, "get_points"):
                _pts = [(float(x[0]), float(x[1])) for x in _e.get_points()]
            if not _pts:
                _skipped.append(f"{_e.dxftype()}#{_e.dxf.handle}")
                continue
            for _q in _pts:
                _dd = float(np.linalg.norm(np.asarray(_q) - _bv[_i]))
                if _best is None or _dd < _best[0]:
                    _best, _hit = (_dd, _q), _e.dxf.handle
        if _best is None:
            L.append(f"  ④ 🔴 **原始 DXF BLOCK 圖層取不到任何頂點**"
                     f"（略過之實體：{_skipped[:5]}）——溯源未完成，不臆測")
        else:
            L.append(f"  ④ **原始 `{os.path.relpath(DXF_PATH, REPO)}` BLOCK 圖層**"
                     f"距該頂點最近之點 ＝ "
                     f"({_best[1][0]:.6f}, {_best[1][1]:.6f})，"
                     f"距離 **{_best[0]:.3e} m**（entity handle {_hit}）")
            L.append(f"  ⇒ **結論：{'CAD 圖面既有' if _best[0] < 1e-6 else '非 CAD 直出·須續追'}**"
                     f"——該偏移**非程式產生**，係 BLOCK 圖層之頂點本身即位於 FRONT_LINE "
                     f"外側 {_bt[_i]:+.6f}m。")
    except Exception as _e_g:
        L.append(f"  ④ 原始 DXF 覆核未完成：{type(_e_g).__name__}: {_e_g}")

    L.append("")
    L.append("【診斷】各多邊形之臨街段兩端垂距（(A) 之原始讀數·線性 ⇒ 只取兩端）")
    L.append("-" * 120)
    for r in rows:
        if "_rng_note" not in r:
            continue
        L.append(f"  {r['情境']:5}{r['街廓']:4}{r['側別']:>6}  範圍：{r['_rng_note']}")
        if r["_par_note"]:
            L.append(f"  {'':5}{'':4}{'':>6}  宗　：{r['_par_note']}")

    L.append("")
    L.append("-" * 120)
    L.append("RESULT: 只量不判（**無 PASS/FAIL 貢獻·rc 恆 0**）。"
             "本檔不代裁 U-K9-1／U-K9-2（前提已換·兩題暫緩）。")
    L.append("=" * 120)

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    with open(CSV, "w", encoding="utf-8-sig", newline="") as f:
        # `_rng_note`／`_par_note` 係列印用私有欄 ⇒ CSV 只出 COLS（非吞錯）
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore", restval="—")
        w.writeheader()
        w.writerows(rows)
    print(f"\n→ {os.path.relpath(LOG, REPO)}\n→ {os.path.relpath(CSV, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
