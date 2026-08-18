#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-59】刀鋒之受詞更正：`D_max(r)` ＋ 臨界膨脹 `r*` ＋ 遠側頂點垂距散佈 ⛔ 零生產碼

**受詞**：`W-G.9-58` §B-1 由 `D_max` 推出之**性質判斷**（「差 ~14 公尺 ⇒ ⛔ 非邊緣」）
是否成立。本檔**換一個受詞再量一次**（＝考古節 87 之修法）：

- **`P2`／`P3`**：`D_max(r)`（`r < 0` ＝ **膨脹**）——若微量膨脹即使 `D_max` 由 ~0 躍升至 ~40，
  則「差 14 公尺」係**症狀**、⛔ 非幾何鴻溝。
- **`P4`**：**臨界膨脹** `r*`（二分·`tol=1e−12`）⇒ **寬度短少 ＝ `2|r*|`**
  （膨脹 `r` 使帶寬增 `2r`：兩側各 `r`）。
- **`P5`**：**遠側頂點垂距之散佈**——用以判該邊是否為乾淨之直邊。

🔒 **⛔ 未另寫第二份判定原語**（`GB-8`）：容納測試一律呼叫
`probe_WG949_free_pose.fits_at`（其內之 `MITRE` 逐字為 `join_style=2, mitre_limit=1e7`
——⛔ 本檔未改其值、亦未自建膨脹）。
`_perp_width`／`_u` 逐字沿用 `probe_WG958_dmax_robust`（⛔ 不重寫）；
`d_max_at_r` 係其 `d_max_at` **加一個 `r` 參數**之變體——**判定仍全部呼叫 `fits_at`**，
⛔ 未自建任何膨脹／侵蝕。

🔒 **乙式幾何**以注入 `min_width` 取得（⛔ 未改生產碼一行）；
引數組裝**逐字沿用** `verify/fixture_corner_range_k8.py` 之 `_build`。

🔒 **自我驗證閘（⛔ 閘不過即不出艙）**：乙ii 垂寬須 ＝ `max(_seg_P0Ps·sinθ, T)`
（自輸出頂點量得）＋ 判別力反例（注入值 ×1.05 須使垂寬分家）。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
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
from probe_WG958_dmax_robust import _u, _perp_width                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 152
SB = 0.0
TOL_R = 1e-12         # 臨界膨脹二分之收斂容差
FAR_WIN = 0.5         # 「遠側頂點」之定義窗（m）：垂距 ≥ max − FAR_WIN
# 🔒 受測位置：二個「不進」之格 ＋ **一個判別力對照格**（⛔ 不得只量刀鋒格）
FOCUS = [("R5", "left"), ("R6", "right"), ("R3", "right")]
R_GRID = (0.0, -1e-06, -1e-05, -3.4e-05, -1e-03)


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def r_star(pst, w, d, th, lo=-1.0, tol=TOL_R):
    """臨界膨脹之**上界** `|r*|`：使 `w × d` 恰可容納之最小膨脹量。

    二分維持不變式：`fits(lo)` 為真、`fits(hi)` 為偽 ⇒ `|r*| ∈ (|lo|, |hi|]` ⇒ 回 `|lo|`。
    🔒 回**上界**（`|lo|`）⇒ 「短少 ≤ 2|r*|」之宣稱**偏保守**（回值只會偏大）。
    ⚠️ 若 `r=0` 已可容納 ⇒ 回 `0.0`（⛔ 不謊報）。
    """
    if fits_at(pst, w, d, th, 0.0)[0]:
        return 0.0
    if not fits_at(pst, w, d, th, lo)[0]:
        return None                       # 連 1 m 膨脹都塞不下 ⇒ ⛔ 不外推
    hi = 0.0
    while abs(lo - hi) > tol:
        mid = 0.5 * (lo + hi)
        if fits_at(pst, w, d, th, mid)[0]:
            lo = mid
        else:
            hi = mid
    return abs(lo)


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-59】刀鋒之受詞更正：`D_max(r)` ＋ 臨界膨脹 `r*` ＋ 遠側頂點垂距散佈")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；容納測試一律用 `fits_at`（其 `MITRE` ＝ "
      "`join_style=2, mitre_limit=1e7`·⛔ 本檔未改）。")
    P("")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    sides = cad.get("side_lines_by_side", {}) or {}
    TARGETS = [(lbl, wch) for lbl in sorted(sides)
               for wch in ("left", "right") if wch in (sides.get(lbl) or {})]

    WD = {}
    for lbl, _w in TARGETS:
        if lbl in WD:
            continue
        mw = ns["get_min_lot_size"](cb_by[lbl]["category"],
                                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        WD[lbl] = (float(mw["min_width"]), float(mw["min_depth"]))

    def _build_range(lbl, which, setback, min_width=None):
        b = cb_by[lbl]
        mb = cad["baselines"][lbl]
        fl = cad["front_lines"][lbl]
        sd = cad["side_lines_by_side"][lbl][which]
        mw = (WD[lbl][0] if min_width is None else float(min_width))
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

    def _geom(lbl, which):
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
                    seg=abs(s_Ps - t_q), sin=abs(su[0] * dxy[1] - su[1] * dxy[0]))

    # ══════════════════════════════════════════════════════════════════
    # 【S】自我驗證閘
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【S】自我驗證閘：乙ii 垂寬 ＝ `max(_seg_P0Ps·sinθ, T)`（自輸出頂點量得）＋ 判別力反例")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'乙ii垂寬(量)':>15}{'期望':>12}{'Δ':>12}"
      f"{'錯值×1.05':>13}{'分家?':>7}  判")
    G, RNG, TH, ok_g, ok_d = {}, {}, {}, True, True
    for lbl, wch in TARGETS:
        g = _geom(lbl, wch)
        w, d = WD[lbl]
        T = SB + w
        s1 = max(g["seg"], T / g["sin"])
        poly = _build_range(lbl, wch, 0.0, min_width=s1)
        bad = _build_range(lbl, wch, 0.0, min_width=s1 * 1.05)
        pw, pwb = _perp_width(poly, g["S1"], g["sn"]), _perp_width(bad, g["S1"], g["sn"])
        exp = max(g["seg"] * g["sin"], T)
        good, disc = abs(pw - exp) <= 1e-9, abs(pwb - pw) > 1e-6
        ok_g &= good
        ok_d &= disc
        G[(lbl, wch)], RNG[(lbl, wch)] = g, poly
        TH[(lbl, wch)] = (math.atan2(g["su"][1], g["su"][0]) + math.pi / 2.0) % math.pi
        P(f"  {lbl:<5}{wch:<7}{pw:>15.9f}{exp:>12.6f}{pw - exp:>12.2e}"
          f"{pwb:>13.6f}{('✅' if disc else '🔴'):>7}  {'✅' if (good and disc) else '🔴'}")
    P("-" * WID)
    P(f"  ⇒ 閉合檢 {'✅ 全過' if ok_g else '🔴'}；判別力 {'✅ 全過' if ok_d else '🔴'}")
    if not (ok_g and ok_d):
        P("  🛑 **閘不過 ⇒ 本次量測⛔ 不出艙**")
        P("=" * WID)
        return L, sha
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【P2／P3】`D_max(r)`
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【P2／P3】`D_max(r)`：固定寬 `W`、姿態 `θ*`，逐級**膨脹** `r`（`r < 0`）")
    P("=" * WID)
    P("  🔒 受測 ＝ 二個「不進」之格 ＋ **一個判別力對照格**（`R3/right`·⛔ 不得只量刀鋒格）")
    P(f"  🔒 `θ*` ＝ 側界方向 + 90°（mod π）·**現算**；`D` ＝ {WD[FOCUS[0][0]][1]}")
    P("")
    hdr = f"  {'街廓':<5}{'側':<7}"
    for r in R_GRID:
        hdr += f"{('r=' + ('%g' % r)):>14}"
    P(hdr)
    DM = {}
    for lbl, wch in FOCUS:
        if (lbl, wch) not in RNG:
            P(f"  {lbl:<5}{wch:<7}  🔴 該位置不在母體")
            continue
        w, d = WD[lbl]
        pst = _poly_st([(float(x), float(y))
                        for x, y in list(RNG[(lbl, wch)].exterior.coords)])
        row = f"  {lbl:<5}{wch:<7}"
        vals = []
        for r in R_GRID:
            # 🔒 膨脹一律經 `fits_at` 之 `r` 參數（⛔ 不自建 buffer）
            v = d_max_at_r(pst, w, TH[(lbl, wch)], r)
            vals.append(v)
            row += f"{v:>14.4f}"
        DM[(lbl, wch)] = vals
        P(row)
    P("-" * WID)
    P("  🔑 **判別力**：對照格須**全程平緩**、而刀鋒格須**由 ~0 躍升**；下方逐項具名。")
    for lbl, wch in FOCUS:
        if (lbl, wch) not in DM:
            continue
        v = DM[(lbl, wch)]
        P(f"     {lbl}/{wch}：r=0 ⇒ {v[0]:.4f}　→　r={R_GRID[-1]:g} ⇒ {v[-1]:.4f}"
          f"　（躍升倍率 {'∞' if v[0] == 0 else '%.1f' % (v[-1] / v[0])}）")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【P4】臨界膨脹 `r*` ⇒ 寬度短少 ＝ `2|r*|`
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【P4】臨界膨脹 `r*`（二分·`tol=1e−12`）⇒ **寬度短少 ＝ `2|r*|`**")
    P("=" * WID)
    P("  🔒 膨脹 `r` 使帶寬增 `2r`（兩側各 `r`）⇒ 短少 ＝ `2|r*|`。")
    P("  🔒 二分回**上界** ⇒ 「短少 ≤ …」之宣稱**偏保守**。")
    P("")
    q_det = None
    for lbl, wch in FOCUS:
        _mb = cad["baselines"].get(lbl) or {}
        _q = (_mb.get("_match") or {}).get("q_detected")
        if _q:
            q_det = float(_q)
    P(f"  🔒 **DXF 量子 `q_detected` ＝ {q_det}**（⛔ 現查·非硬編）")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'|r*| 上界':>16}{'寬度短少 ≤':>16}{'／量子':>12}{'判':>8}")
    for lbl, wch in FOCUS:
        if (lbl, wch) not in RNG:
            continue
        w, d = WD[lbl]
        pst = _poly_st([(float(x), float(y))
                        for x, y in list(RNG[(lbl, wch)].exterior.coords)])
        rs = r_star(pst, w, d, TH[(lbl, wch)])
        if rs is None:
            P(f"  {lbl:<5}{wch:<7}   🔴 連 1 m 膨脹都塞不下 ⇒ ⛔ 不外推")
            continue
        short = 2.0 * rs
        ratio = (short / q_det) if q_det else float("nan")
        P(f"  {lbl:<5}{wch:<7}{rs:>16.6e}{short:>16.6e}{ratio:>12.4f}"
          f"{('刀鋒' if 0 < short < (q_det or 1e-5) else ('恰容納' if short == 0 else '非刀鋒')):>8}")
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【P5】遠側頂點垂距之散佈
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【P5】遠側頂點垂距之散佈（⇒ 該邊是否為乾淨之直邊）")
    P("=" * WID)
    P(f"  🔒 **「遠側頂點」之定義（⛔ 單未給·本檔自訂並具名）**：垂距 ≥ `max − {FAR_WIN}` m 之頂點。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'頂點數':>8}{'遠側頂點數':>11}{'min':>15}{'max':>15}{'散佈':>13}")
    for lbl, wch in FOCUS:
        if (lbl, wch) not in RNG:
            continue
        g = G[(lbl, wch)]
        cs = list(RNG[(lbl, wch)].exterior.coords)[:-1]
        ds = sorted((abs((float(x) - g["S1"][0]) * g["sn"][0]
                         + (float(y) - g["S1"][1]) * g["sn"][1]) for x, y in cs),
                    reverse=True)
        far = [v for v in ds if v >= ds[0] - FAR_WIN]
        P(f"  {lbl:<5}{wch:<7}{len(ds):>8}{len(far):>11}{min(far):>15.9f}"
          f"{max(far):>15.9f}{max(far) - min(far):>13.3e}")
    P("-" * WID)
    P("  🔒 **逐頂點之全部垂距（⛔ 不概括·失敗考古節 88）**：")
    for lbl, wch in FOCUS:
        if (lbl, wch) not in RNG:
            continue
        g = G[(lbl, wch)]
        cs = list(RNG[(lbl, wch)].exterior.coords)[:-1]
        ds = sorted((abs((float(x) - g["S1"][0]) * g["sn"][0]
                         + (float(y) - g["S1"][1]) * g["sn"][1]) for x, y in cs),
                    reverse=True)
        P(f"     {lbl}/{wch}：" + "／".join(f"{v:.9f}" for v in ds))
    P("=" * WID)
    return L, sha


def d_max_at_r(pst, w, th, r):
    """`D_max` 於膨脹 `r` 下之值（⛔ 膨脹一律經 `fits_at` 之 `r` 參數·不自建 buffer）。"""
    # 🩸 **`GB-81` 之修（`W-G.9-60` §B-1）**：見 `probe_WG958_dmax_robust.d_max_at` 之同註。
    from probe_WG958_dmax_robust import _diameter
    hi = _diameter(pst) + 1.0
    if fits_at(pst, w, hi, th, r)[0]:
        # 🔒 **飽和閘（§B-2）**：回值 ＝ `hi` ⇒ **loud raise**、⛔ 不得靜默出艙。
        raise RuntimeError(
            f"🔴 d_max_at_r 飽和：`hi`={hi:.6f} 仍可容納 ⇒ 回值將等於上界、⛔ 非量測值（`GB-81`）。")
    lo = 1e-6
    if not fits_at(pst, w, lo, th, r)[0]:
        return 0.0
    while hi - lo > 1e-6:
        mid = 0.5 * (lo + hi)
        if fits_at(pst, w, mid, th, r)[0]:
            lo = mid
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG959_knife_edge_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
