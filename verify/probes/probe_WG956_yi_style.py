#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-56】乙式（SIDELINE 沿**法向**平移·**垂距**）之影響實測 ⛔ 零生產碼

**受詞（⛔ 不互代）**
- **§B**：`app.py` 之 `S1_par = max(_seg_P0Ps, T)` 是否**在比兩種不同之距離**
  （`_seg_P0Ps` ＝ 路平行長度／`T` 自本裁起 ＝ 垂距）。⇒ 數值坐實或推翻。
- **§C-1**：8 個街角位置之甲式／乙式 面積・垂寬・矩形容納（**下限二式並列**·⛔ 不擇一）。
- **§C-2**：依 `A-2 三` 扣除**退縮帶**後再測矩形容納。
- **§C-3**：`K-9-5-2 ④` 之土地後果——資格代表之真 G vs 甲式門檻 vs 乙式門檻。
- **§C-4**：`GB-76` 之追加——乙式下 `K-9-5-2 ③` 之保證是否**恢復**。
- **§D-1/-2/-3**：母體改 8 個／判「不進」者之證書逐級／`_seg_P0Ps` vs `T` 對照。

🔴 **乙式幾何之取得方式（⛔ 不改 `_build_corner_range_v3`·⛔ 不另寫第二份構造）**

`_build_corner_range_v3` 內 `min_width` **僅**餵 `T`（字樣錨
`T = float(setback or 0.0) + float(min_width or 0.0)`），而 `T` **僅**餵
`S1_par = max(_seg_P0Ps, T)`（另一處僅為錯誤訊息字串）⇒ **注入 `min_width` 即等值於指定平移量**。

而「沿 `d̂`（前緣線方向）平移 `s`」與「沿側界法向平移 `n`」**產生同一條直線**，
換算為 `n = s · sinθ`（`θ` ＝ 側界與前緣線之夾角）⇒ 乙式所需之注入值為
`S1_par(乙) = 目標垂距 / sinθ`
⇒ **乙式範圍多邊形 ＝ 生產函式在該注入值下之輸出**，⛔ 非探針自建之近似物。

🔒 **自我驗證閘**（`CLAUDE.md`「探針還原內部幾何時須以碼面自身之保證當自我驗證閘」）：
探針自行重建之 `S1_par(甲)` 回代生產函式（`setback=0, min_width=S1_par(甲)`），
其輸出須與生產原呼叫**逐面積相同**；並附**判別力反例**（乘 1.05 之錯值須使面積分家）。
**閘不過 ⇒ ⛔ 本次量測不出艙。**

🔴 **掃描策略之二處變更（⛔ 具名揭露·⛔ 非靜默）**

1. **新增具名候選姿態角**（側界／前緣／BASELINE 之方向及其法向·精確 `fits_at`）。
   **必要性已實測**：乙式之垂寬**恰** ＝ `W` 時，矩形僅於**唯一**角度可容納
   （寬 3.5 之帶：`θ=0` ⇒ True、`θ=1e-6` ⇒ **False**）⇒ 均勻網格**永遠掃不到**
   ⇒ 不加候選角必**系統性誤判「不進」**。
   🔒 候選角**只能使「不進」翻為「進」**、⛔ 不可能反向 ⇒ 對判「不進」**保守**。
2. **`margin_ub` 之階梯**（⛔ 非靜默截斷·逐級印出）：實測 `margin_ub` 每次 3.18 ms、
   `fits_at` 每次 0.105 ms ⇒ 二者成本差 **30 倍**。
   🆕 **`W-G.9-57` §F-3**：主階梯已自 `1e-3` **延伸為** `(2e-2, 5e-3, 1e-3, 2e-4, 5e-5)`
   （⛔ **非放寬**——加細只使門檻 `R·Δθ/2` 變小、證書**變嚴格**）；
   `C-2` 之階梯**另行封頂於 `1e-3`**（其受詞非證書·見 `STEPS_C2`）。
   **另以「精確 `fits_at` 細掃 `Δθ=1e-4`」**補其**找解**之一半；
   ⇒ 🔒 **細掃⛔ 不產生證書**、⛔ 不謊稱已至該級之證書。
3. 🆕 **`W-G.9-57`：出艙碼改為<u>三態</u>**（`進`／`未證`／`不進`）——見 `_hit` 之 docstring。

🔒 沿用倉內既有機具、⛔ 不另寫第二份（`GB-8`）：
  `probe_WG949_free_pose` 之 `scan`／`witness`／`fits_at`／`margin_ub`／`selfcheck`、
  `probe_WG947_rect_fit` 之 `_poly_st`／`rect_fits`、
  `fixture_corner_range_k8` 之 `_build` 引數組裝（逐字沿用·⛔ 不自創）。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
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
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from probe_WG947_rect_fit import _poly_st                           # noqa: E402
from probe_WG949_free_pose import (scan, witness, selfcheck,        # noqa: E402
                                   fits_at, margin_ub)

OUTDIR = os.path.join(VERIFY, "out")
WID = 178
SB = 0.0
# 🔒 退縮之**第二情境**：⛔ 非本探針自創——係倉內 harness 既有之雙情境，出處見【C-2】。
SB2 = 3.5
# `margin_ub` 階梯。
# 🆕 **`W-G.9-57` §F-3 延伸至 `5e-5`**（原封頂 `1e-3`）——⛔ **非放寬**：
#   加細只使門檻 `R·Δθ/2` **變小**、證書**變嚴格**。所需之級由 `Δθ < 2ε/R` 實算：
#   乙ii `R5/left`／`R6/right`（ε≈0.00195）⇒ 需 `<5.4e-4` ⇒ `2e-4` 足；
#   甲式 `R5/left`（真 |max m|≈0.000253）⇒ 需 `<7.0e-5` ⇒ `5e-5`。
STEPS_EPS = (2e-2, 5e-3, 1e-3, 2e-4, 5e-5)
# 🆕 **`W-G.9-57` §E-2**：`C-2` 之階梯**另行封頂於 `1e-3`**（⛔ 具名揭露·⛔ 非靜默）
#   ——`C-2` 之受詞係「該欄之差異是否落在雜訊級」，⛔ 非證書之取得；
#   其判別力門檻為 `ε > 1e-5`，而 `1e-3` 級之 ε 已足以判之。
STEPS_C2 = (2e-2, 5e-3, 1e-3)
DTH_C2_EPS = 1e-3          # `C-2` 判「不進」者一律於此步長印 ε／門檻（⛔ 固定·非階梯）
# 精確 `fits_at` 之細掃步長（⛔ 只做「找解」·⛔ 不產生證書）
DTH_FINE = 1e-4


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _u(vx, vy):
    n = math.hypot(vx, vy)
    return (vx / n, vy / n)


def _perp_width(poly, S1, sn):
    """範圍多邊形二側界之**垂距**——自**輸出幾何**量得（⛔ 非以平移量自證）。"""
    return max(abs((float(x) - S1[0]) * sn[0] + (float(y) - S1[1]) * sn[1])
               for x, y in list(poly.exterior.coords))


def _cut_off_setback(poly, S1, sn, setback):
    """扣除**退縮帶**：留「至側界∞ 垂距 ≥ `setback`」之部分（`A-2 三`）。

    回 `(幾何, 是否重合)`。

    🩸 **首版之缺陷（`W-G.9-56` 自誌·⛔ 具名）**：`sn = (-su[1], su[0])` 之號**由側界
      端點順序決定**、⛔ 未定向至範圍所在之半平面 ⇒ 半平面指向範圍**之外**時
      交集為空。實測 8 格中 **4 格**（全部 `right` 側）印出「扣後為空」
      ——**係符號錯、⛔ 非幾何發現**。
    🔒 **修法**：以**範圍自身之代表點**定號（`(pt − S1)·sn < 0 ⇒ 翻號`），
      並由呼叫端以「扣後非空 ∧ 扣後垂寬 ＝ `T − setback`」為閘。
    """
    if setback <= 0.0:
        return poly, True                       # 與全範圍**重合**（具名·⛔ 非近似）
    from shapely.geometry import Polygon as _Pg
    _pt = poly.representative_point()
    if (float(_pt.x) - S1[0]) * sn[0] + (float(_pt.y) - S1[1]) * sn[1] < 0.0:
        sn = (-sn[0], -sn[1])                   # 定號：指向範圍所在之半平面
    b = poly.bounds
    ext = 2.0 * (b[2] - b[0] + b[3] - b[1]) + 100.0
    su = (-sn[1], sn[0])
    base = (S1[0] + sn[0] * setback, S1[1] + sn[1] * setback)
    half = _Pg([(base[0] - su[0] * ext, base[1] - su[1] * ext),
                (base[0] + su[0] * ext, base[1] + su[1] * ext),
                (base[0] + su[0] * ext + sn[0] * ext, base[1] + su[1] * ext + sn[1] * ext),
                (base[0] - su[0] * ext + sn[0] * ext, base[1] - su[1] * ext + sn[1] * ext)])
    return poly.intersection(half), False


def _cands_of(g, bl_ang_rad):
    """具名候選姿態角（mod π）：側界／前緣／BASELINE 之方向及其法向。"""
    out = []
    for nm, ang in (("側界", math.atan2(g["su"][1], g["su"][0])),
                    ("前緣", math.atan2(g["d"][1], g["d"][0])),
                    ("BASELINE", bl_ang_rad)):
        for suf, off in (("", 0.0), ("+90°", math.pi / 2.0)):
            out.append((nm + suf, (ang + off) % math.pi))
    return out


def eps_at(pst, w, d, R, dth):
    """於**指定單一步長**求 `ε = −max m(θ)` 與門檻 `R·Δθ/2`（⛔ 非階梯·⛔ 不早停）。

    🔒 `W-G.9-57` §E-2 用：其受詞係「該格之餘裕是否落在雜訊級」，⛔ 非證書之取得。
    """
    n = int(math.ceil(math.pi / dth))
    best = -1e18
    for k in range(n):
        m = margin_ub(pst, w, d, k * dth)
        if m > best:
            best = m
    return -best, R * dth / 2.0, n


def ladder(pst, w, d, R, steps):
    """逐級掃描並**記錄每一級**之 `(Δθ, ε, 門檻, 證書?, 點數, 命中θ)`；首個證書成立即停。

    🔒 **⛔ 非另寫第二份判定**——原語仍為 `probe_WG949_free_pose` 之 `fits_at`／`margin_ub`
      （`GB-8`）；本函式只是**把階梯之逐級結果留下來**，
      使 `D-2` 之逐級表**直接取用**、⛔ 不必重跑一次同樣的掃描
      （`W-G.9-56` 之 `D-2` 即重跑了一次·本批已消除該重複）。
    """
    recs = []
    for dth in steps:
        n = int(math.ceil(math.pi / dth))
        best, hit = -1e18, None
        for k in range(n):
            th = k * dth
            if fits_at(pst, w, d, th, 0.0)[0]:
                hit = th
                break
            m = margin_ub(pst, w, d, th)
            if m > best:
                best = m
        if hit is not None:
            recs.append((dth, None, None, None, n, hit))
            return hit, recs
        eps, thr = -best, R * dth / 2.0
        cert = eps > thr
        recs.append((dth, eps, thr, cert, n, None))
        if cert:
            return None, recs
    return None, recs


def _hit(pst, w, d, th, via, recs, fine=0):
    """組出「找到解」之回傳，並**以見證之逐角獨立驗證決定出艙碼**。

    🩸 **`W-G.9-57` 修（CC 自誌·⛔ 具名）**：前版把 `fits_at`（侵蝕非空）之真**逕作「進」**，
      而**見證雖已算出、其 `all_in` 卻沒有接到出艙碼上** ⇒ 出現「判進而四角驗證 False」之格
      （`W-G.9-56`／本批 v3 之【E-2b】退縮 3.5 共 **4 格**）。
      這與本倉紀律「**判『可以』須具名見證物並逐角獨立驗證·⛔ 不以侵蝕之非空當證明**」**直接相違**。
    🔒 **修法 ＝ 三態**：
      · `code="進"` ＝ 侵蝕非空 **∧** 見證四角 `poly.covers` 皆真（**已證**）
      · `code="未證"` ＝ 侵蝕非空 **∧** 見證逐角驗證**失敗**（⇒ 刀鋒·⛔ 不得當「進」用）
      · `code="不進"` ＝ 掃不到解（另依證書分「已證明不存在」／「未找到」）
    ⚠️ **⛔ 「未證」不得讀作「不進」**——後者是另一個命題，本函式並未證得。
    """
    wit = witness(pst, w, d, th)
    ok = bool(wit and wit["all_in"])
    return dict(pst=pst, th=th, via=via, eps=None, thr=None, cert=None,
                dth=(recs[-1][0] if recs else None), wit=wit, fine=fine, recs=recs,
                proven=ok, code=("進" if ok else "未證"))


def fit_search(poly, w, d, R, cands, steps=STEPS_EPS, fine=True):
    """矩形容納之三段式搜尋。回 dict（含 `pst`／`th`／`via`／`code`／`proven`／`eps`／`thr`／`cert`／`wit`／`recs`）。"""
    pst = _poly_st([(float(x), float(y)) for x, y in list(poly.exterior.coords)])
    for nm, th in cands:                       # ① 具名候選角（精確·⛔ 非近似）
        if fits_at(pst, w, d, th, 0.0)[0]:
            return _hit(pst, w, d, th, f"候選角:{nm}", [])
    th, recs = ladder(pst, w, d, R, steps)     # ② 均勻階梯（逐級留檔）
    if th is not None:
        return _hit(pst, w, d, th, "均勻網格", recs)
    n = 0
    if fine:                                   # ③ 細掃（僅 fits_at·⛔ 無證書）
        n = int(math.ceil(math.pi / DTH_FINE))
        for k in range(n):
            t = k * DTH_FINE
            if fits_at(pst, w, d, t, 0.0)[0]:
                return _hit(pst, w, d, t, f"細掃 Δθ={DTH_FINE:.0e}", recs, fine=n)
    _last = recs[-1]
    return dict(pst=pst, th=None, via="未找到", eps=_last[1], thr=_last[2],
                cert=bool(_last[3]), dth=_last[0], wit=None, fine=n, recs=recs,
                proven=False, code="不進")


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-56】乙式（SIDELINE 沿法向平移·垂距）之影響實測")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**——乙式幾何以**注入 `min_width`** 取得（見檔頭）。")
    P(f"  🔒 掃描策略：候選角（精確）→ 均勻階梯 {STEPS_EPS}（證書）→ 細掃 "
      f"Δθ={DTH_FINE:.0e}（僅找解）。**⛔ 已具名揭露封頂**。")
    P("")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    sides = cad.get("side_lines_by_side", {}) or {}

    TARGETS = [(lbl, wch) for lbl in sorted(sides)
               for wch in ("left", "right") if wch in (sides.get(lbl) or {})]
    P("=" * WID)
    P("【D-1】母體補正：受測位置 ＝ `cad['side_lines_by_side']` **全部**")
    P("=" * WID)
    P(f"  ⇒ **{len(TARGETS)}** 個位置：" + "／".join(f"{a}/{b}" for a, b in TARGETS))
    P("  🔒 `-53` §C-1 之母體 ＝ 4 個（沿用「`run_step_g` 成功之街廓」之過濾）；")
    P("     🔴 規定範圍之構造**不需** `run_step_g` ⇒ 該過濾對本受詞**非必要** ⇒ 已移除。")
    P("")

    WD = {}
    for lbl, _w in TARGETS:
        if lbl in WD:
            continue
        mw = ns["get_min_lot_size"](cb_by[lbl]["category"],
                                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        WD[lbl] = (float(mw["min_width"]), float(mw["min_depth"]))

    def _build_range(lbl, which, setback, min_width=None):
        """引數組裝：逐字沿用 `verify/fixture_corner_range_k8.py` 之 `_build`。"""
        b = cb_by[lbl]
        mb = cad["baselines"][lbl]
        fl = cad["front_lines"][lbl]
        sd = cad["side_lines_by_side"][lbl][which]
        mw = (WD[lbl][0] if min_width is None else float(min_width))
        kw = dict(
            block_vertices=b["vertices"], block_centroid=b["centroid"],
            front_pts=[fl["p1"], fl["p2"]],
            baseline_pts=ns["_baseline_pts_from_manual"](mb, b["vertices"]),
            side_line_pts=[sd["p1"], sd["p2"]],
            alloc_dir=cad["alloc_dir_by_block"][lbl],
            block_depth=float(snapshot["blocks"][lbl]["街廓分配深度_m"]),
            setback=setback, min_width=mw,
            chamfer_tri=ns["_make_chamfer_tri_wb"](b, which),
            dxf_quantum=(mb.get("_match") or {}).get("q_detected"),
            _label=lbl, _side=which)
        return ns["_build_corner_range_v3"](**kw)

    def _geom(lbl, which):
        """探針側**獨立**重建 `P0`／`Ps`／`_seg_P0Ps`／`sinθ`（⛔ 不取生產區域變數）。"""
        fl = cad["front_lines"][lbl]
        F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
        F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
        dxy = _u(F2[0] - F1[0], F2[1] - F1[1])
        sd = cad["side_lines_by_side"][lbl][which]
        S1 = (float(sd["p1"][0]), float(sd["p1"][1]))
        S2 = (float(sd["p2"][0]), float(sd["p2"][1]))
        su = _u(S2[0] - S1[0], S2[1] - S1[1])
        sn = (-su[1], su[0])
        den_s = dxy[0] * sn[0] + dxy[1] * sn[1]
        if abs(den_s) < 1e-12:
            return None
        t_q = ((S1[0] - F1[0]) * sn[0] + (S1[1] - F1[1]) * sn[1]) / den_s
        P0 = (F1[0] + t_q * dxy[0], F1[1] + t_q * dxy[1])
        chi = ns["_make_chamfer_tri_wb"](cb_by[lbl], which)
        if chi is None or getattr(chi, "is_empty", True):
            return None

        def _d_front(p):
            return abs((p[0] - F1[0]) * (-dxy[1]) + (p[1] - F1[1]) * dxy[0])

        cv = [(float(c[0]), float(c[1])) for c in chi.exterior.coords[:-1]]
        cv = [c for c in cv if math.hypot(c[0] - P0[0], c[1] - P0[1]) > 1e-9]
        if len(cv) < 2:
            return None
        cv.sort(key=_d_front)
        Ps = cv[0]
        s_Ps = (Ps[0] - F1[0]) * dxy[0] + (Ps[1] - F1[1]) * dxy[1]
        sin_t = abs(su[0] * dxy[1] - su[1] * dxy[0])
        return dict(F1=F1, d=dxy, S1=S1, su=su, sn=sn, P0=P0, Ps=Ps,
                    seg=abs(s_Ps - t_q), sin=sin_t, dfront_Ps=_d_front(Ps),
                    ang=math.degrees(math.asin(min(1.0, sin_t))))

    G = {(lbl, wch): _geom(lbl, wch) for lbl, wch in TARGETS}
    BLANG = {lbl: math.radians(float(cad["baselines"][lbl]["angle_deg"]))
             for lbl, _ in TARGETS}

    # ══════════════════════════════════════════════════════════════════
    # 【S】自我驗證閘（⛔ 閘不過即停機·本次量測不出艙）
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【S】自我驗證閘：探針重建之 `S1_par(甲)` 回代生產函式須逐面積相同（＋判別力反例）")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'生產原呼叫面積':>17}{'回代面積':>15}{'Δ':>12}"
      f"{'錯值×1.05':>15}{'Δ(錯)':>12}  判")
    gate_ok, gate_disc = True, True
    for lbl, wch in TARGETS:
        g = G[(lbl, wch)]
        w, d = WD[lbl]
        if g is None:
            P(f"  {lbl:<5}{wch:<7}  🔴 幾何重建失敗（截角三角形或側界退化）")
            gate_ok = False
            continue
        s1a = max(g["seg"], SB + w)
        a_prod = float(_build_range(lbl, wch, SB).area)
        a_back = float(_build_range(lbl, wch, 0.0, min_width=s1a).area)
        a_bad = float(_build_range(lbl, wch, 0.0, min_width=s1a * 1.05).area)
        ok = abs(a_prod - a_back) <= 1e-9
        disc = abs(a_prod - a_bad) > 1e-6
        gate_ok &= ok
        gate_disc &= disc
        P(f"  {lbl:<5}{wch:<7}{a_prod:>17.9f}{a_back:>15.9f}{a_prod - a_back:>12.2e}"
          f"{a_bad:>15.9f}{a_prod - a_bad:>12.2e}  {'✅' if (ok and disc) else '🔴'}")
    P("-" * WID)
    P(f"  ⇒ 回代相同 ＝ {'✅ 全過' if gate_ok else '🔴 有格不過'}"
      f"；判別力（錯值須分家）＝ {'✅ 全過' if gate_disc else '🔴 有格不分家'}")
    if not (gate_ok and gate_disc):
        P("  🛑 **閘不過 ⇒ 本次量測⛔ 不出艙**（`CLAUDE.md`：量測器須先自證非紅）")
        P("=" * WID)
        return L, sha
    P("")

    w0, d0 = WD[sorted(WD)[0]]
    R0 = math.sqrt(w0 * w0 + d0 * d0) / 2.0
    okc, _sc = selfcheck(P, w0, d0, R0)
    P(f"  ⇒ 矩形容納求值器自檢：{'PASS' if okc else '🛑 FAIL ⇒ 停機·⛔ 不出艙'}")
    if not okc:
        P("=" * WID)
        return L, sha
    P("")
    # 🔒 候選角機制之**判別力自檢**：寬恰 ＝ W 之帶，均勻網格須「不進」而候選角須「進」
    # 🩸 **首版之缺陷（`W-G.9-56` 自誌·⛔ 具名）**：合成帶取**軸對齊**（θ=0）
    #   ⇒ `θ=0` **恰在均勻網格上**（`k=0`）⇒ 網格當然找得到 ⇒ 該自檢**無判別力**
    #     （首版印「🔴 進（則候選角非必要）」）。
    # 🔒 **修法**：把合成帶轉一個**刻意不落在任何步長格點上**之角度。
    from shapely.geometry import Polygon as _Pg0
    _TH0 = 0.012345678901234          # ⛔ 非 2e-2／5e-3／1e-3／1e-4 之整數倍
    _c0, _s0 = math.cos(_TH0), math.sin(_TH0)
    _strip = _Pg0([(x * _c0 - y * _s0, x * _s0 + y * _c0)
                   for x, y in ((0, 0), (w0, 0), (w0, 3.0 * d0), (0, 3.0 * d0))])
    _pst0 = _poly_st(list(_strip.exterior.coords))
    _grid_hit = scan(_pst0, w0, d0, steps=STEPS_EPS, R=R0)[0] is not None
    _cand_hit = fits_at(_pst0, w0, d0, _TH0, 0.0)[0]
    P("【S-2】候選角機制之判別力自檢（⛔ 證其非恆真、且確有必要）")
    P("-" * WID)
    P(f"  合成帶 ＝ 寬恰 {w0}（＝W）× 長 {3.0 * d0} 之帶，**轉 {_TH0:.12f} rad**")
    P(f"     （⛔ 刻意非任何步長 {STEPS_EPS + (DTH_FINE,)} 之整數倍 ⇒ 均勻網格掃不到該角）")
    P(f"  均勻階梯 {STEPS_EPS} ⇒ "
      f"{'🔴 進（⇒ 本自檢無判別力·須換角）' if _grid_hit else '**不進** ✅'}")
    P(f"  精確測試於該角 ⇒ {'**進** ✅' if _cand_hit else '🔴 不進'}")
    P(f"  該角偏 `1e-6` ⇒ {'進' if fits_at(_pst0, w0, d0, _TH0 + 1e-6, 0.0)[0] else '**不進**'}"
      "　⇒ 可容納之角度窗**窄於任何實用網格**")
    P(f"  ⇒ 候選角機制之判別力：{'✅ 成立（網格漏、候選角抓到）' if (_cand_hit and not _grid_hit) else '🔴 未成立'}")
    P("  🔒 **方向性**：候選角**只能使「不進」翻為「進」**，且每個「進」皆附")
    P("     **見證矩形＋逐角獨立驗證**（見【C-1b】）⇒ ⛔ 不可能製造假「進」。")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【B／D-3】受詞混用之數值坐實
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【B／D-3】`S1_par = max(_seg_P0Ps, T)` 之二量：`_seg_P0Ps`（路平行）vs `T`（本裁後＝垂距）")
    P("=" * WID)
    P("  🔒 `_seg_P0Ps` 為**路平行長度**之獨立佐證：`P0`／`Ps` 皆在 FRONT∞ 上"
      "（`d(Ps,F∞)` 欄 ⇒ 其沿 `d̂` 之座標差即沿前緣線之距離）")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'夾角θ°':>10}{'sinθ':>10}{'_seg_P0Ps':>12}{'T':>8}"
      f"{'S1_par(甲)':>12}{'seg>T?':>7}{'d(Ps,F∞)':>11}{'甲式垂距':>11}{'甲垂距<T?':>11}")
    for lbl, wch in TARGETS:
        g = G[(lbl, wch)]
        w, d = WD[lbl]
        T = SB + w
        s1a = max(g["seg"], T)
        pw = s1a * g["sin"]
        P(f"  {lbl:<5}{wch:<7}{g['ang']:>10.4f}{g['sin']:>10.6f}{g['seg']:>12.6f}{T:>8.2f}"
          f"{s1a:>12.6f}{('是' if g['seg'] > T else '否'):>7}{g['dfront_Ps']:>11.2e}"
          f"{pw:>11.6f}{('🔴 是' if pw < T - 1e-9 else '否'):>11}")
    P("-" * WID)
    P("  🔴 **甲式垂距 ＝ `S1_par(甲)·sinθ`** ＝ 甲式所實際保證之**垂寬**。")
    P("     其若 < `T` ⇒ `K-9-5-2 ③`（最小寬度 ≥ 畸零地寬）於**垂距口徑**下**不成立**。")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【C-1】甲式 vs 乙式（下限二式並列·⛔ 不擇一）
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C-1】甲式 vs 乙式：面積／垂寬／矩形容納（**擋截角下限二式並列**·⛔ 不擇一）")
    P("=" * WID)
    P("  🔒 **式(i)**  `垂距 = max(_seg_P0Ps, T)`      ＝ 逐字沿用現行 `max()`（⇒ 仍混二量）")
    P("  🔒 **式(ii)** `垂距 = max(_seg_P0Ps·sinθ, T)` ＝ 將下限**換算為垂距**後再取 max")
    P(f"  🔒 `W`／`D` ＝ {w0}／{d0}（`get_min_lot_size`·⛔ 無字面量）")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'甲面積':>11}{'乙i面積':>11}{'乙ii面積':>11}"
      f"{'Δ(乙ii−甲)':>12}{'甲垂寬':>10}{'乙ii垂寬':>10}"
      f"{'甲容納':>8}{'乙i':>6}{'乙ii':>7}{'乙ii經由':>18}")
    CR = {}
    for lbl, wch in TARGETS:
        g = G[(lbl, wch)]
        w, d = WD[lbl]
        Rp = math.sqrt(w * w + d * d) / 2.0
        T = SB + w
        cands = _cands_of(g, BLANG[lbl])
        s1a = max(g["seg"], T)
        s1_i = max(g["seg"], T) / g["sin"]
        s1_ii = max(g["seg"], T / g["sin"])
        pA = _build_range(lbl, wch, 0.0, min_width=s1a)
        pI = _build_range(lbl, wch, 0.0, min_width=s1_i)
        pII = _build_range(lbl, wch, 0.0, min_width=s1_ii)
        res = {tag: fit_search(pp, w, d, Rp, cands)
               for tag, pp in (("A", pA), ("I", pI), ("II", pII))}
        CR[(lbl, wch)] = dict(g=g, T=T, s1a=s1a, s1_i=s1_i, s1_ii=s1_ii,
                              pA=pA, pI=pI, pII=pII, res=res, w=w, d=d, R=Rp,
                              wA=_perp_width(pA, g["S1"], g["sn"]),
                              wII=_perp_width(pII, g["S1"], g["sn"]), cands=cands)
        c = CR[(lbl, wch)]
        P(f"  {lbl:<5}{wch:<7}{pA.area:>11.4f}{pI.area:>11.4f}{pII.area:>11.4f}"
          f"{pII.area - pA.area:>12.4f}{c['wA']:>10.6f}{c['wII']:>10.6f}"
          f"{res['A']['code']:>8}"
          f"{res['I']['code']:>6}"
          f"{res['II']['code']:>7}"
          f"{res['II']['via']:>18}")
    P("-" * WID)
    P("  🔒 **三態**（`W-G.9-57` 修）：`進` ＝ 侵蝕非空 **∧** 見證四角獨立驗證皆真（**已證**）；")
    P("     `未證` ＝ 侵蝕非空而見證逐角驗證**失敗**（⇒ 刀鋒·⛔ 不得當「進」用、⛔ 亦非「不進」）；")
    P("     `不進` ＝ 掃不到解（另依證書分「已證明不存在」／「未找到」）。")
    for tag, nm in (("A", "甲式"), ("I", "乙式(i)"), ("II", "乙式(ii)")):
        n = sum(1 for k in CR if CR[k]["res"][tag]["code"] == "進")
        nu = sum(1 for k in CR if CR[k]["res"][tag]["code"] == "未證")
        P(f"  ⇒ 矩形容納：{nm} **{n}／{len(CR)}** 已證"
          + (f"；🔴 **未證 {nu}**" if nu else "；未證 0"))
    P("")
    P("  【垂寬之閉合檢】乙式(ii) 之垂寬須 ＝ `max(_seg_P0Ps·sinθ, T)`（自**輸出幾何頂點**量得）")
    P(f"  {'街廓':<5}{'側':<7}{'乙ii垂寬(量)':>15}{'期望':>12}{'Δ':>12}  判")
    _wok = True
    for lbl, wch in TARGETS:
        c = CR[(lbl, wch)]
        exp = max(c["g"]["seg"] * c["g"]["sin"], c["T"])
        dd = c["wII"] - exp
        good = abs(dd) <= 1e-9
        _wok &= good
        P(f"  {lbl:<5}{wch:<7}{c['wII']:>15.9f}{exp:>12.6f}{dd:>12.2e}  {'✅' if good else '🔴'}")
    P(f"  ⇒ {'✅ 全過' if _wok else '🔴 有格不過'}　🔒 量測自**輸出多邊形頂點**（⛔ 非以平移量自證）")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【D-2】判「不進」者之證書：逐級 Δθ
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【D-2】判「不進」者之證書：逐級 Δθ 之 ε 與門檻（⛔ 逐位置具名）")
    P("=" * WID)
    _nofit = [(lbl, wch, tag) for lbl, wch in TARGETS for tag in ("A", "I", "II")
              if CR[(lbl, wch)]["res"][tag]["th"] is None]
    if not _nofit:
        P("  ⇒ **三式之 8 個位置全部判「進」** ⇒ 本節無受詞（⛔ 非略過·係空集）")
    else:
        P(f"  {'街廓':<5}{'側':<7}{'式':<4}{'Δθ':>9}{'ε':>12}{'門檻 R·Δθ/2':>14}"
          f"{'ε/門檻':>9}{'掃描點數':>9}{'證書':>6}")
        P(f"  🔒 階梯 ＝ {STEPS_EPS}（`W-G.9-57` §F-3 已自 `1e-3` **延伸**至 `5e-5`）")
        P("  🔒 本表**直接取用** `fit_search` 之逐級留檔（⛔ 未重跑一次掃描·"
          "`W-G.9-56` 之同表曾重跑·本批已消除）")
        for lbl, wch, tag in _nofit:
            c = CR[(lbl, wch)]
            for dth, eps, thr, cert, n, hit in c["res"][tag]["recs"]:
                if hit is not None:
                    P(f"  {lbl:<5}{wch:<7}{tag:<4}{dth:>9.1e}   🔴 該步長下**找到解** θ={hit:.6f}")
                    continue
                P(f"  {lbl:<5}{wch:<7}{tag:<4}{dth:>9.1e}{eps:>12.6f}{thr:>14.6e}"
                  f"{eps / thr:>9.2f}{n:>9}{('✅' if cert else '—'):>6}")
            P(f"  {lbl:<5}{wch:<7}{tag:<4}{'細掃':>9}  Δθ={DTH_FINE:.0e}"
              f"（{int(math.ceil(math.pi / DTH_FINE))} 點·僅 `fits_at`）⇒ "
              f"{'🔴 找到解' if c['res'][tag]['th'] is not None else '仍未找到'}")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【C-2】扣除退縮帶後之矩形容納
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C-2】依 `A-2 三` **扣除退縮帶**後之矩形容納")
    P("=" * WID)
    P(f"  🔒 情境一 `setback = {SB}`（＝本 harness 之生產情境）⇒ 退縮帶寬 ＝ 0")
    P("     ⇒ **扣除後與全範圍重合**（具名·⛔ 非近似·下表 `Δ面積` 欄 ＝ 0 為證）")
    P(f"  🔒 情境二 `setback = {SB2}`——**倉內既有之第二情境**、⛔ 非本探針假造：")
    P("     出處 `verify/run_verification.py` 檔頭「雙情境（退縮 0m/3.5m）」"
      "＋入庫 `verify/baselines/退縮3.5m參數.csv`")
    _sbsrc = []
    for lbl, wch in TARGETS:
        _b = snapshot["blocks"].get(lbl) or {}
        for _k in ("退縮", "退縮寬_m", "側街退縮_m", "退縮_m", "退縮寬"):
            if _k in _b:
                _sbsrc.append(f"{lbl}.{_k}")
    P(f"  🔴 **快照內逐街廓側街退縮欄之現查命中 ＝ {len(_sbsrc)}**"
      + ("：" + "／".join(_sbsrc) if _sbsrc else "（空）⇒ **無逐街廓資料源**"))
    P("     ⚠️ ⛔ **不得讀作「本案側街退縮 ＝ 3.5m」**——`CLAUDE.md`：退縮係案件／街廓級參數；")
    P("     本情境僅為**參數掃描**，⛔ 非本案之值。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'退縮':>6}{'全範圍':>11}{'扣後面積':>11}{'Δ面積':>10}"
      f"{'扣後垂寬':>10}{'閘':>4}{'扣後容納':>9}{'經由':>18}{'ε(1e-3)':>11}{'ε/門檻':>8}")
    _c2_gate = True
    C2ROWS = []
    for sbv in (SB, SB2):
        for lbl, wch in TARGETS:
            g = G[(lbl, wch)]
            w, d = WD[lbl]
            Rp = math.sqrt(w * w + d * d) / 2.0
            s1_ii = max(g["seg"], (sbv + w) / g["sin"])
            poly = _build_range(lbl, wch, 0.0, min_width=s1_ii)
            cut, same = _cut_off_setback(poly, g["S1"], g["sn"], sbv)
            if cut.is_empty:
                _c2_gate = False
                P(f"  {lbl:<5}{wch:<7}{sbv:>6.1f}{poly.area:>11.4f}   🔴 **扣後為空 ⇒ 閘破**"
                  "（法向定號或半平面方向有誤·⛔ 該格不出艙）")
                continue
            if cut.geom_type == "MultiPolygon":
                cut = max(cut.geoms, key=lambda q: q.area)
            _cw = _perp_width(cut, g["S1"], g["sn"]) - sbv
            # 🔒 **閘**：扣後之垂寬須恰為 `T − setback` ＝ `min_width`
            #   （乙式之遠側界在垂距 `T` 處、扣除帶在垂距 `setback` 處）
            _exp_cw = max(g["seg"] * g["sin"], sbv + w) - sbv
            _gk = abs(_cw - _exp_cw) <= 1e-6
            _c2_gate &= _gk
            r = fit_search(cut, w, d, Rp, _cands_of(g, BLANG[lbl]),
                           steps=STEPS_C2, fine=False)
            # 🆕 **`W-G.9-57` §E-2**：判「不進」者一律於**固定** `Δθ=1e-3` 印 ε／門檻
            #   （⛔ 不接受「係雜訊」之未量測斷言）
            if r["th"] is None:
                _e, _thr, _n = eps_at(r["pst"], w, d, Rp, DTH_C2_EPS)
            else:
                _e, _thr, _n = None, None, 0
            _es = "—" if _e is None else ("%.6f" % _e)
            _rt = "—" if _e is None else ("%.2f" % (_e / _thr))
            C2ROWS.append((lbl, wch, sbv, r, _e, _thr, _cw))
            P(f"  {lbl:<5}{wch:<7}{sbv:>6.1f}{poly.area:>11.4f}{cut.area:>11.4f}"
              f"{cut.area - poly.area:>10.4f}{_cw:>10.6f}{('✅' if _gk else '🔴'):>4}"
              f"{r['code']:>9}{r['via']:>18}{_es:>11}{_rt:>8}"
              + ("　（重合）" if same else ""))
    P("-" * WID)
    P(f"  ⇒ 【C-2】閘（扣後非空 ∧ 扣後垂寬 ＝ `T − setback`）："
      f"{'✅ 全過' if _c2_gate else '🔴 有格不過 ⇒ 該等格⛔ 不出艙'}")
    P(f"  🔒 **階梯封頂於 {STEPS_C2}**（⛔ 具名揭露）；判「不進」者之 ε 一律"
      f"另於**固定** `Δθ={DTH_C2_EPS:.0e}` 求得（⛔ 非階梯之早停值）。")
    P("")
    # ── 🆕 `W-G.9-57` §E-2：「係雜訊」之判別（⛔ 不接受未量測之斷言）──────────
    P("  【E-2】`W-G.9-56` §C-2 之「其進／不進由 ~1e-9 之浮點雜訊決定」⇒ **實測驗之**")
    P(f"  🔒 判別力門檻 ＝ **1e-5**（取在雜訊 ~1e-9 與公釐級 ~1e-3 **之間**·⛔ 不貼任一側）")
    _nofit_c2 = [x for x in C2ROWS if x[3]["code"] == "不進"]
    _fit_c2 = [x for x in C2ROWS if x[3]["code"] == "進"]
    _unpr_c2 = [x for x in C2ROWS if x[3]["code"] == "未證"]
    P(f"  判「不進」＝ **{len(_nofit_c2)}** 格；判「進」（已證）＝ **{len(_fit_c2)}** 格；"
      f"🔴 **「未證」＝ {len(_unpr_c2)}** 格")
    if _unpr_c2:
        P("  🔴 **「未證」之逐格具名（侵蝕非空而見證逐角驗證失敗 ⇒ 刀鋒）**：")
        for lbl, wch, sbv, r, e, thr, cw in _unpr_c2:
            _ins = r["wit"]["inside"] if r["wit"] else []
            P(f"      {lbl}/{wch}（退縮 {sbv}）θ ＝ {r['wit']['theta']:.9f}"
              f"　四角在內 ＝ {_ins}　⇒ ⛔ 不得當「進」用、⛔ 亦非「不進」")
    if _nofit_c2:
        P(f"    {'街廓':<5}{'側':<7}{'退縮':>6}{'ε(Δθ=1e-3)':>13}{'門檻':>13}{'ε/門檻':>9}"
          f"{'ε > 1e-5?':>11}")
        for lbl, wch, sbv, r, e, thr, cw in _nofit_c2:
            P(f"    {lbl:<5}{wch:<7}{sbv:>6.1f}{e:>13.6f}{thr:>13.3e}{e / thr:>9.2f}"
              f"{('✅ 是' if e > 1e-5 else '🔴 否'):>11}")
        _all_gt = all(x[4] > 1e-5 for x in _nofit_c2)
        P(f"  ⇒ **{'全部 ε > 1e-5' if _all_gt else '🔴 有格 ε ≤ 1e-5'}**"
          f" ⇒ 「係雜訊」之敘述{'**過寬**·須改述為具名之量測結論' if _all_gt else '於該等格**成立**·逐格具名'}")
    P("  【E-2b】判「進」者之見證（⛔ 逐角獨立驗證·⛔ 非以侵蝕非空當證明）")
    for lbl, wch, sbv, r, e, thr, cw in _fit_c2:
        wt = r["wit"]
        if wt is None:
            P(f"    {lbl}/{wch}（退縮 {sbv}）🔴 無見證")
            continue
        P(f"    {lbl}/{wch}（退縮 {sbv}）θ ＝ {wt['theta']:.9f} rad"
          f"　四角皆在內 ＝ {wt['all_in']}　經由 {r['via']}")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【C-3】門檻上升之土地後果
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C-3】門檻上升之土地後果：資格代表之真 G vs 甲式門檻 vs 乙式門檻")
    P("=" * WID)
    P("  🔒 門檻之讀取點 ＝ `min_area_to_apply`（`app.py` 字樣錨"
      " `cand_G < cand.get('min_area_to_apply', 0)`）")
    P("     其值 ＝ `round(規定範圍面積, 2)`（`verify/run_verification.py` 字樣錨"
      " `return round(float(r.area), 2)`）")
    P("  🔒 **⛔ 未實跑重排**（須先有實作）——本表僅作**單變因**對照。")
    diag, sel, off, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        SB, snapshot=snapshot)
    P(f"  🔒 `run_corner_pk` 之候選診斷列 ＝ {len(diag)}；指配列 ＝ {len(sel or [])}")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'資格代表':<14}{'真G(㎡)':>10}{'甲式門檻':>10}{'乙ii門檻':>10}"
      f"{'甲餘裕':>10}{'乙ii餘裕':>10}{'乙下失格?':>11}{'候選數':>7}")
    _lose = []
    for lbl, wch in TARGETS:
        c = CR[(lbl, wch)]
        thr_a = round(float(c["pA"].area), 2)
        thr_ii = round(float(c["pII"].area), 2)
        _zh = {"left": "左", "right": "右"}[wch]
        _cands = [r for r in diag if str(r.get("街廓")) == lbl
                  and str(r.get("端")) in (wch, _zh)]
        _best = None
        for r in _cands:
            try:
                gv = float(r.get("真G(㎡)") or 0)
            except Exception:                                       # noqa: BLE001
                gv = 0.0
            if _best is None or gv > _best[0]:
                _best = (gv, r)
        if _best is None:
            P(f"  {lbl:<5}{wch:<7}{'（無候選列）':<14}{'—':>10}{thr_a:>10.2f}{thr_ii:>10.2f}")
            continue
        gv, r = _best
        gid = str(r.get("候選地號") or "")
        ok_a, ok_ii = gv >= thr_a, gv >= thr_ii
        if ok_a and not ok_ii:
            _lose.append((lbl, wch, gid))
        P(f"  {lbl:<5}{wch:<7}{gid:<14}{gv:>10.2f}{thr_a:>10.2f}{thr_ii:>10.2f}"
          f"{gv - thr_a:>10.2f}{gv - thr_ii:>10.2f}"
          f"{('🔴 是' if (ok_a and not ok_ii) else '否'):>11}{len(_cands):>7}")
    P("-" * WID)
    P(f"  ⇒ **乙式門檻下失去資格之位置 ＝ {len(_lose)}**"
      + ("" if not _lose else "：" + "／".join(f"{a}/{b}·{c}" for a, b, c in _lose)))
    P("  ⚠️ **取「真 G 最大之候選」為代表**（⛔ 非 PK 之 winner——winner 由三指數決定，")
    P("     而資格閘先於指數）：若連**最寬鬆**之代表都失格，該側即**無**候選可過。")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【C-4】`GB-76` 之追加
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C-4】`GB-76` 追加：乙式下 `K-9-5-2 ③` 之保證是否**恢復**")
    P("=" * WID)
    P("  🔒 **③ 之字面 ＝ 兩個一維量**（最小深度 ≥ 畸零地深 ∧ 最小寬度 ≥ 畸零地寬）；")
    P("     本表之「垂寬 ≥ W」僅為 ③ 之**寬度半**，⛔ 非 ③ 之全部、⛔ 非矩形容納。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'甲垂寬':>10}{'甲≥W?':>8}{'乙ii垂寬':>10}{'乙≥W?':>8}"
      f"{'乙ii矩形':>10}{'經由':>18}{'ε':>11}{'證書':>6}")
    _yi_no = []
    for lbl, wch in TARGETS:
        c = CR[(lbl, wch)]
        w = c["w"]
        r = c["res"]["II"]
        if r["th"] is None:
            _yi_no.append((lbl, wch, r))
        _es = "—" if r["eps"] is None else ("%.6f" % r["eps"])
        P(f"  {lbl:<5}{wch:<7}{c['wA']:>10.6f}{('✅' if c['wA'] >= w - 1e-9 else '🔴'):>8}"
          f"{c['wII']:>10.6f}{('✅' if c['wII'] >= w - 1e-9 else '🔴'):>8}"
          f"{r['code']:>10}{r['via']:>18}{_es:>11}"
          f"{('—' if r['th'] is not None else ('✅' if r['cert'] else '🔴')):>6}")
    P("-" * WID)
    if _yi_no:
        P(f"  🔴 **乙式下仍判「不進」＝ {len(_yi_no)} 個位置**（⛔ 不得視為構造失敗·`C-4` 限縮）：")
        for lbl, wch, r in _yi_no:
            P(f"      {lbl}/{wch}　ε ＝ {r['eps']:.6f}　門檻 ＝ {r['thr']:.3e}　"
              f"證書 ＝ {'✅ 成立' if r['cert'] else '🔴 不成立（出艙碼＝未找到·⛔ 非證明不存在）'}")
        P("  🔒 **`C-4` 之限縮由本測坐實**：垂寬 ＝ `W` 係**必要非充分**。")
    else:
        P("  ✅ **乙式下 8 個位置全部判「進」**")
        P("  ⚠️ ⛔ **不得推論為「構造保證矩形容納」**——本項僅為**本案 8 個位置**之實測；")
        P("     `C-4` 之限縮（垂寬 ＝ W 係必要非充分）**未被本測推翻**，只是本案未觸發。")
    P("")

    P("【C-1b】乙式(ii) 判「進」者之見證矩形四角（**逐角獨立驗證**·⛔ 非以侵蝕非空當證明）")
    P("-" * WID)
    for lbl, wch in TARGETS:
        wit = CR[(lbl, wch)]["res"]["II"]["wit"]
        if wit is None:
            continue
        P(f"  {lbl}/{wch}　θ ＝ {wit['theta']:.9f} rad（{math.degrees(wit['theta']):.4f}°）"
          f"　四角皆在內 ＝ {wit['all_in']}")
        for i, (cpt, ins) in enumerate(zip(wit["corners"], wit["inside"])):
            P(f"      角{i + 1} ＝ ({cpt[0]:.9f}, {cpt[1]:.9f})　在範圍內 ＝ {ins}")
    P("=" * WID)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG956_yi_style_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
