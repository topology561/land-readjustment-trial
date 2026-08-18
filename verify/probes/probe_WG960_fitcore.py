#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-60】`fits_at` 之**單調性閘** ＋ `D_max` 之**飽和閘** ⛔ 零生產碼

**受詞**：本檔**不量幾何**，只量**儀器自身**——
- **單調性閘**（`GB-82`）：`fits_at(pst, w, d, θ, r)` 對 `d` 應**非遞增**
  （薄矩形為厚矩形之子集 ⇒ 厚者可容納則薄者必可容納）。
  ⇒ 於 `d` 之遞增格上取真值集，**出現 `0` 之後再現 `1` 即為紅**。
- **飽和閘**（`GB-81`）：`D_max` 常式之上界框取自**原框** bbox，而判定發生於**轉框**
  ⇒ 若回值 **等於其內部 `hi`**，該常式**從未進入二分** ⇒ **紅**。

🔒 **本檔<u>先證紅、後修</u>**（施工單 `W-G.9-60` §A-1 明令：⛔ 不得先修）。
🔒 **⛔ 不新增第二份判定原語**——本檔只**呼叫** `probe_WG949_free_pose.fits_at`。
  🔒 **`GB-8` 之受詞裁定（`W-G.9-60`）**：其所禁者為「⛔ 不得**並存**兩份互相獨立之判定原語」，
  ⛔ **非**「不得修復既有之唯一原語」⇒ 修復須**就地**為之。

🔒 **`D_max` 於單調性閘轉綠前一律以<u>掃描式</u>取得**（施工單 §A-4·⛔ 不得二分）：
  `d` 由 `1e−9` 起 ×1.5 遞增至 `0.1`、其後 `+0.25` 遞增至 `50`，取**最大之 True**，
  再於其後 `0.25` 內以 `1e−6` 細化。

🔒 輸出檔名含產生它之 commit 短碼 ＋ 階段標記；⛔ 不覆寫任何既有 log。
"""
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
for _p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE):
    sys.path.insert(0, _p)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from probe_WG947_rect_fit import _poly_st                           # noqa: E402
from probe_WG949_free_pose import fits_at                           # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 150
SB = 0.0
FOCUS = [("R5", "left"), ("R6", "right"), ("R3", "right")]
R_GRID = (0.0, -1e-06, -1e-05, -1e-03)
D_GRID = (1e-9, 1e-7, 1e-5, 1e-4, 1e-3, 1e-2, 0.1, 1, 5, 14, 25, 35, 39, 41, 43)


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _u(vx, vy):
    n = math.hypot(vx, vy)
    return (vx / n, vy / n)


# ══════════════════════════════════════════════════════════════════════
# 幾何組裝（module 級 ⇒ 後批可 import·⛔ 不必再抄一次）
# 🔒 引數組裝**逐字沿用** `verify/fixture_corner_range_k8.py` 之 `_build`。
# ══════════════════════════════════════════════════════════════════════
def build_ctx():
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    sides = cad.get("side_lines_by_side", {}) or {}
    targets = [(lbl, wch) for lbl in sorted(sides)
               for wch in ("left", "right") if wch in (sides.get(lbl) or {})]
    wd = {}
    for lbl, _w in targets:
        if lbl in wd:
            continue
        mw = ns["get_min_lot_size"](cb_by[lbl]["category"],
                                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        wd[lbl] = (float(mw["min_width"]), float(mw["min_depth"]))
    return ns, cb_by, cad, snapshot, wd, targets


def build_range(ns, cb_by, cad, snapshot, wd, lbl, which, setback, min_width=None):
    b = cb_by[lbl]
    mb = cad["baselines"][lbl]
    fl = cad["front_lines"][lbl]
    sd = cad["side_lines_by_side"][lbl][which]
    mw = (wd[lbl][0] if min_width is None else float(min_width))
    return ns["_build_corner_range_v3"](
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


def geom(ns, cb_by, cad, lbl, which):
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
    t_q = ((S1[0] - F1[0]) * sn[0] + (S1[1] - F1[1]) * sn[1]) / den_s
    P0 = (F1[0] + t_q * dxy[0], F1[1] + t_q * dxy[1])
    chi = ns["_make_chamfer_tri_wb"](cb_by[lbl], which)

    def _d_front(p):
        return abs((p[0] - F1[0]) * (-dxy[1]) + (p[1] - F1[1]) * dxy[0])

    cv = [(float(c[0]), float(c[1])) for c in chi.exterior.coords[:-1]]
    cv = [c for c in cv if math.hypot(c[0] - P0[0], c[1] - P0[1]) > 1e-9]
    cv.sort(key=_d_front)
    Ps = cv[0]
    s_Ps = (Ps[0] - F1[0]) * dxy[0] + (Ps[1] - F1[1]) * dxy[1]
    return dict(F1=F1, d=dxy, S1=S1, su=su, sn=sn,
                seg=abs(s_Ps - t_q), sin=abs(su[0] * dxy[1] - su[1] * dxy[0]),
                theta=(math.atan2(su[1], su[0]) + math.pi / 2.0) % math.pi)


def yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which, setback=SB):
    """乙式(ii) 之範圍多邊形（`_poly_st` 後）＋ 其幾何 dict。"""
    g = geom(ns, cb_by, cad, lbl, which)
    w, _d = wd[lbl]
    T = setback + w
    s1 = max(g["seg"], T / g["sin"])
    poly = build_range(ns, cb_by, cad, snapshot, wd, lbl, which, 0.0, min_width=s1)
    return _poly_st([(float(x), float(y)) for x, y in list(poly.exterior.coords)]), g, poly


def perp_width(poly, S1, sn):
    return max(abs((float(x) - S1[0]) * sn[0] + (float(y) - S1[1]) * sn[1])
               for x, y in list(poly.exterior.coords))


def hi_of(pst):
    """`W-G.9-58`／`-59` 之 `D_max` 常式所用之上界框（**原框** bbox·⛔ 本檔只是複算它）。"""
    b = pst.bounds
    return max(b[2] - b[0], b[3] - b[1]) + 1.0


def d_max_scan(pst, w, th, r, cap=50.0, fine=1e-6):
    """§A-4 之**掃描式** `D_max`（⛔ 非二分·⛔ 不依賴單調性）。

    `d` 由 `1e−9` ×1.5 遞增至 `0.1`、其後 `+0.25` 至 `cap`，取**最大之 True**；
    再於其後 `0.25` 內以 `fine` 細化。回 `(D_max, 是否觸及 cap)`。
    """
    ds, x = [], 1e-9
    while x < 0.1:
        ds.append(x)
        x *= 1.5
    x = 0.1
    while x <= cap:
        ds.append(x)
        x += 0.25
    best = 0.0
    for d in ds:
        if fits_at(pst, w, d, th, r)[0]:
            best = d
    if best >= cap:
        return best, True
    lo, hi = best, best + 0.25
    while hi - lo > fine:
        mid = 0.5 * (lo + hi)
        if fits_at(pst, w, mid, th, r)[0]:
            lo = mid
        else:
            hi = mid
    return lo, False


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    stage = os.environ.get("WG960_STAGE", "pre")
    P("=" * WID)
    P(f"【W-G.9-60】`fits_at` 單調性閘 ＋ `D_max` 飽和閘　（階段：{stage}）")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；本檔只**呼叫** `fits_at`，⛔ 未新增第二份判定原語。")
    P("")

    ns, cb_by, cad, snapshot, wd, targets = build_ctx()

    # ══════════════════════════════════════════════════════════════
    # 【A-1-a】單調性閘
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-1-a】**單調性閘**：`fits_at` 對 `d` 應非遞增 ⇒ 真值集出現 `0…1` 反轉即為**紅**")
    P("=" * WID)
    P("  🔒 `d` 之 15 點格（逐位）：" + "／".join(f"{d:g}" for d in D_GRID))
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'r':>10}  {'真值集（依 d 遞增）':<20}  判")
    mono_bad = []
    for lbl, wch in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        w, _d = wd[lbl]
        for r in R_GRID:
            bits = "".join("1" if fits_at(pst, w, d, g["theta"], r)[0] else "0"
                           for d in D_GRID)
            # 反轉 ＝ 出現 `0` 之後再現 `1`
            bad = ("01" in bits.lstrip("0").replace("1", "1"))
            first0 = bits.find("0")
            bad = (first0 != -1 and "1" in bits[first0:])
            if bad:
                mono_bad.append((lbl, wch, r, bits))
            P(f"  {lbl:<5}{wch:<7}{r:>10.0e}  {bits:<20}  {'🔴 反轉' if bad else '✅'}")
    P("-" * WID)
    P(f"  ⇒ **單調性閘：{'🔴 紅（' + str(len(mono_bad)) + ' 組反轉）' if mono_bad else '✅ 綠'}**")
    for lbl, wch, r, bits in mono_bad:
        P(f"      🔴 反例 ＝ ({lbl}/{wch}, r={r:g})　真值集 ＝ `{bits}`")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-1-b】飽和閘
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-1-b】**飽和閘**：`D_max` 常式之回值 ＝ 其內部 `hi` ⇒ **紅**（從未進入二分）")
    P("=" * WID)
    P("  🔒 `hi` ＝ `max(原框 bbox_w, 原框 bbox_h) + 1.0`（＝ `-58`／`-59` 之寫法·本檔複算之）")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'原框 bbox_w':>13}{'原框 bbox_h':>13}{'hi':>12}"
      f"{'-59 所報 D_max':>16}{'相符?':>7}{'轉框後長邊':>13}")
    sat_bad = []
    D59 = {("R5", "left"): 33.3787, ("R6", "right"): 35.6825, ("R3", "right"): 36.5961}
    for lbl, wch in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        b = pst.bounds
        bw, bh = b[2] - b[0], b[3] - b[1]
        hi = hi_of(pst)
        from shapely.affinity import rotate as _rt
        q = _rt(pst, -g["theta"], origin=(0.0, 0.0), use_radians=True)
        qb = q.bounds
        rot_long = max(qb[2] - qb[0], qb[3] - qb[1])
        d59 = D59[(lbl, wch)]
        same = abs(hi - d59) < 5e-4
        if same:
            sat_bad.append((lbl, wch, hi, d59))
        P(f"  {lbl:<5}{wch:<7}{bw:>13.4f}{bh:>13.4f}{hi:>12.4f}{d59:>16.4f}"
          f"{('🔴 逐位' if same else '否'):>7}{rot_long:>13.4f}")
    P("-" * WID)
    P(f"  ⇒ **舊式框之診斷：{'🔴 ' + str(len(sat_bad)) + '／' + str(len(FOCUS)) + ' 格飽和' if sat_bad else '✅ 未飽和'}**")
    P("  🔒 **相符即證**：`-59` 所報之 `D_max` **就是該常式之上界本身**"
      "（⇒ 從未進入二分·⛔ 非量測值）。")
    P("")
    P("  【飽和閘·修後】直接呼叫 `d_max_at_r`（其內建飽和閘應 loud raise）")
    P(f"  {'街廓':<5}{'側':<7}{'新 hi(直徑+1)':>15}{'回值':>13}{'閘':>18}")
    sat_post_ok = True
    from probe_WG959_knife_edge import d_max_at_r
    from probe_WG958_dmax_robust import _diameter
    for lbl, wch in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        w, _d = wd[lbl]
        nh = _diameter(pst) + 1.0
        try:
            v = d_max_at_r(pst, w, g["theta"], 0.0)
            msg = "✅ 未飽和"
            if abs(v - nh) < 1e-9:
                msg = "🔴 回值＝hi"
                sat_post_ok = False
            P(f"  {lbl:<5}{wch:<7}{nh:>15.4f}{v:>13.4f}{msg:>18}")
        except RuntimeError as e:
            sat_post_ok = False
            P(f"  {lbl:<5}{wch:<7}{nh:>15.4f}{'—':>13}{'🔴 raise 飽和':>18}")
            P(f"        {str(e).splitlines()[0][:110]}")
    P(f"  ⇒ **飽和閘（修後）：{'✅ 綠' if sat_post_ok else '🔴 紅'}**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-4】掃描式 `D_max`（⛔ 非二分·不依賴單調性）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-4】**掃描式** `D_max`（⛔ 非二分·⛔ 不依賴單調性）")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}" + "".join(f"{('r=' + ('%g' % r)):>16}" for r in R_GRID))
    for lbl, wch in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        w, _d = wd[lbl]
        row = f"  {lbl:<5}{wch:<7}"
        for r in R_GRID:
            v, capped = d_max_scan(pst, w, g["theta"], r)
            row += f"{(('%.4f' % v) + ('🔴cap' if capped else '')):>16}"
        P(row)
    P("-" * WID)
    P("  🔒 `🔴cap` ＝ 觸及掃描上限 `50.0` ⇒ **該值為下界、⛔ 不得當量測值**。")
    P("")

    P("=" * WID)
    P("【C-1】三焦點格之 `D_max`：**本批（掃描式）** vs `W-G.9-59`【倉】 vs 施工單【單】")
    P("=" * WID)
    D59 = {("R5", "left"): (0.0447, 33.3787, 33.3787, 33.3787),
           ("R6", "right"): (0.0000, 35.6825, 35.6825, 35.6825),
           ("R3", "right"): (36.5961, 36.5961, 36.5961, 36.5961)}
    DAN = {("R5", "left"): (0.0447, 39.9825, 39.9825, 39.9860),
           ("R6", "right"): (0.0000, 0.0000, 39.8736, 39.8771),
           ("R3", "right"): (41.4830, 41.4830, 41.4831, 41.4864)}
    P(f"  {'街廓':<5}{'側':<7}{'r':>10}{'本批':>12}{'-59【倉】':>13}{'單【單】':>12}"
      f"{'與 -59':>10}{'與單':>10}")
    for lbl, wch in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        w, _d = wd[lbl]
        for k, r in enumerate(R_GRID):
            v, _cap = d_max_scan(pst, w, g["theta"], r)
            o, a_ = D59[(lbl, wch)][k], DAN[(lbl, wch)][k]
            P(f"  {lbl:<5}{wch:<7}{r:>10.0e}{v:>12.4f}{o:>13.4f}{a_:>12.4f}"
              f"{('✅' if abs(v - o) < 5e-4 else '🔴'):>10}"
              f"{('✅' if abs(v - a_) < 5e-4 else '🔴'):>10}")
    P("")

    P("=" * WID)
    P("【C-2】`W-G.9-58` §B-1 之 **8 格**於 `r=0` 之 `D_max` 重測 ＋ **進／不進分類對帳**")
    P("=" * WID)
    OLD8 = {("R1", "left"): 25.986091, ("R1", "right"): 24.932952,
            ("R2", "left"): 34.260514, ("R3", "right"): 36.596060,
            ("R4", "left"): 26.007323, ("R4", "right"): 26.214424,
            ("R5", "left"): 0.044673, ("R6", "right"): 0.000000}
    P(f"  {'街廓':<5}{'側':<7}{'舊 D_max(下界)':>16}{'新 D_max':>12}{'新 ≥ 舊?':>10}"
      f"{'D=14':>8}{'新分類':>9}{'-59 分類':>10}{'一致?':>7}")
    cls_same = True
    for lbl, wch in targets:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        w, dd = wd[lbl]
        v, _cap = d_max_scan(pst, w, g["theta"], 0.0)
        o = OLD8[(lbl, wch)]
        newc = "進" if v >= dd else "不進"
        oldc = "進" if o >= dd else "不進"
        same = (newc == oldc)
        cls_same &= same
        P(f"  {lbl:<5}{wch:<7}{o:>16.6f}{v:>12.4f}{('✅' if v >= o - 5e-4 else '🔴'):>10}"
          f"{dd:>8.1f}{newc:>9}{oldc:>10}{('✅' if same else '🔴'):>7}")
    P("-" * WID)
    P(f"  ⇒ **分類逐格一致 ＝ {'✅ 8／8' if cls_same else '🔴 有格不一致'}**"
      f" ⇒ **土地後果 ＝ {'零' if cls_same else '🔴 非零'}**")
    P("")

    P("=" * WID)
    P("【C-3】`|r*|`（臨界膨脹）× **三個座標框**：絕對 TWD97／移至形心／移 `+1e6`")
    P("=" * WID)
    from probe_WG959_knife_edge import r_star
    from shapely.affinity import translate as _tr2
    P(f"  {'街廓':<5}{'側':<7}{'絕對 TWD97':>16}{'移至形心':>16}{'移 +1e6':>16}{'相對差':>10}")
    for lbl, wch in FOCUS:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, wch)
        w, dd = wd[lbl]
        c = pst.centroid
        frames = [pst,
                  _tr2(pst, xoff=-float(c.x), yoff=-float(c.y)),
                  _tr2(pst, xoff=1e6, yoff=1e6)]
        vals = [r_star(f, w, dd, g["theta"]) for f in frames]
        vv = [v for v in vals if v is not None and v > 0]
        rel = (max(vv) - min(vv)) / max(vv) * 100.0 if vv else 0.0
        P(f"  {lbl:<5}{wch:<7}" + "".join(
            f"{('%.6e' % v if v is not None else '—'):>16}" for v in vals)
          + f"{rel:>9.2f}%")
    P("  🔒 **平移不變性**：`|r*|` 若跨框穩定 ⇒ 係**真幾何**、⛔ 非座標殘差。")
    P("")

    P("=" * WID)
    P("【C-4】見證檢：`R3/right`、`W=3.5`、`D=41.0`、`r=0` ⇒ 四角 `covers` ＋ 四角至邊界距")
    P("=" * WID)
    from probe_WG949_free_pose import witness as _wit
    from shapely.geometry import Point as _Pt2
    pst3, g3, _p3 = yi_pst(ns, cb_by, cad, snapshot, wd, "R3", "right")
    w3, _ = wd["R3"]
    for DD in (41.0, 41.4830, 41.4835):
        ok = fits_at(pst3, w3, DD, g3["theta"], 0.0)[0]
        wt = _wit(pst3, w3, DD, g3["theta"]) if ok else None
        if wt is None:
            P(f"  D = {DD:<9.4f} ⇒ 不進")
            continue
        dists = [pst3.exterior.distance(_Pt2(c)) for c in wt["corners"]]
        P(f"  D = {DD:<9.4f} ⇒ 進　四角皆在內 ＝ {wt['all_in']}"
          f"　四角至邊界距 ＝ " + "／".join(f"{v:.3e}" for v in dists))
    P("")

    P("=" * WID)
    P("【C-5】🔒 **儀器自身之解析度** vs **被測量之量級**（⛔ 二者須並列·自誤 43 修法 7）")
    P("=" * WID)
    from probe_WG949_free_pose import MITRE, TOL_M
    from probe_WG959_knife_edge import TOL_R
    P(f"  · `fits_at` 之 `MITRE`       ＝ {MITRE}（⛔ 本批一字未改）")
    P(f"  · `margin_ub` 之二分 `TOL_M` ＝ {TOL_M:.0e} m")
    P(f"  · `r_star` 之二分 `TOL_R`    ＝ {TOL_R:.0e}")
    P(f"  · `d_max_scan` 之細化步長    ＝ {1e-6:.0e} m；粗掃 ×1.5（<0.1）／+0.25（≥0.1）")
    P("  · `double` 相對精度 ＝ 2.2e−16 ⇒ 於座標量級 ~2.65e6 之絕對誤差 ≈ **5.9e−10 m**")
    P("    🔒 **修後判定於局部原點** ⇒ 座標量級降至 ~4e1 ⇒ 絕對誤差 ≈ **8.9e−15 m**")
    P("")
    P("  **被測量之量級**：")
    P("    · 寬度短少（`2|r*|`）   ≈ **1e−07 m**")
    P("    · DXF 量子 `q_detected` ＝ **1e−05 m**")
    P("    · `D_max` 之大值        ≈ **4e+01 m**")
    P("  🔑 **判**：修前絕對誤差 `5.9e−10` 與寬度短少 `1e−07` **僅差 2 個數量級**；")
    P("     修後降至 `8.9e−15` ⇒ **差 7 個數量級** ⇒ **該量已可信**。")
    P("     ⚠️ 惟 `D_max(r=0)` 於刀鋒格（`R5/left`）**仍不穩**——其真餘裕即 ~1e−07")
    P("     ⇒ 🔒 **該格之 `D_max` 小值⛔ 不得引用有效位數**。")
    P("=" * WID)
    return L, sha, stage


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha, _stage = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG960_fitcore_{_stage}_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
