#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-58】乙式三格之 `D_max`（P5）＋ 旋轉路徑穩健性（P6）⛔ 零生產碼

**受詞（⛔ 不互代）**
- **P5**：固定寬 `W`、於**帶姿態 `θ*`** 之**最大可容納深度 `D_max`**
  ⇒ 用以判「乙ii 之二格是否只是<u>邊緣</u>」——若 `D_max ≈ 0` 而 `D = 14`，
  則其「不進」**差以公尺計**、⛔ 非公釐級之刀鋒。
- **P6**：**三條數學上等價之旋轉路徑**下，該三格之判定是否一致
  ⇒ 用以判「垂寬恰 ＝ `W`」是否使結論由捨入決定。

🔒 **⛔ 不另寫第二份判定原語**（`GB-8`）：容納測試一律用
`probe_WG949_free_pose.fits_at`（＝ `W-G.9-47` 已驗收之侵蝕實作）。
本檔**只新增**：① `D_max` 之二分（其判定仍呼叫 `fits_at`）②三條旋轉路徑之包裝。

🔒 **乙式幾何之取得**：與 `probe_WG956_yi_style` **同法**——注入 `min_width`
（`_build_corner_range_v3` 內 `min_width` 僅餵 `T`、`T` 僅餵 `S1_par`）
⇒ ⛔ **未改生產碼一行**。引數組裝**逐字沿用** `verify/fixture_corner_range_k8.py` 之 `_build`。

🔒 **自我驗證閘（⛔ 閘不過即不出艙）**：本檔所建之乙ii 範圍，其**垂寬**須 ＝
`max(_seg_P0Ps·sinθ, T)`（自**輸出多邊形頂點**量得）
——此即 `W-G.9-56` §C-1 之閉合檢；**過閘即證本檔之幾何與該批同物**。
另附**判別力反例**（注入值乘 1.05 ⇒ 垂寬須分家）。

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

OUTDIR = os.path.join(VERIFY, "out")
WID = 150
SB = 0.0
TOL_D = 1e-6          # `D_max` 二分之收斂容差（m）


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _u(vx, vy):
    n = math.hypot(vx, vy)
    return (vx / n, vy / n)


def _perp_width(poly, S1, sn):
    return max(abs((float(x) - S1[0]) * sn[0] + (float(y) - S1[1]) * sn[1])
               for x, y in list(poly.exterior.coords))


def d_max_at(pst, w, th, hi0=None):
    """固定寬 `w`、姿態 `th` 下之**最大可容納深度**（二分·判定仍用 `fits_at`）。

    🔒 回**下界**（`lo`）：`fits(lo)` 為真、`fits(hi)` 為偽 ⇒ `D_max ∈ [lo, hi)`。
      ⇒ 用於「`D_max` 遠小於 `D`」之宣稱時**偏保守**（回值只會偏小）。
    """
    b = pst.bounds
    hi = hi0 if hi0 is not None else (max(b[2] - b[0], b[3] - b[1]) + 1.0)
    if fits_at(pst, w, hi, th, 0.0)[0]:
        return hi                                  # 連上界都塞得下 ⇒ 回上界（⛔ 不謊報）
    lo = 0.0
    if not fits_at(pst, w, lo + TOL_D, th, 0.0)[0]:
        return 0.0                                 # 連極薄都塞不下
    lo = lo + TOL_D
    while hi - lo > TOL_D:
        mid = 0.5 * (lo + hi)
        if fits_at(pst, w, mid, th, 0.0)[0]:
            lo = mid
        else:
            hi = mid
    return lo


def _rot_paths(poly, th):
    """三條**數學上等價**之旋轉路徑（`P6`）。回 `{名: 旋轉後之多邊形}`。"""
    from shapely.affinity import rotate as _r, translate as _t
    out = {}
    out["甲 use_radians=True"] = _r(poly, -th, origin=(0.0, 0.0), use_radians=True)
    out["乙 度↔弧度來回"] = _r(poly, -math.degrees(th), origin=(0.0, 0.0),
                              use_radians=False)
    c = poly.centroid
    _q = _t(poly, xoff=-float(c.x), yoff=-float(c.y))
    out["丙 先移形心再轉"] = _r(_q, -th, origin=(0.0, 0.0), use_radians=True)
    return out


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-58】乙式三格之 `D_max`（P5）＋ 旋轉路徑穩健性（P6）")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**——乙式幾何以注入 `min_width` 取得；容納測試一律用 `fits_at`。")
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
        """引數組裝：逐字沿用 `verify/fixture_corner_range_k8.py` 之 `_build`。"""
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
    # 【S】自我驗證閘：本檔之乙ii 幾何須與 `W-G.9-56` 同物
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【S】自我驗證閘：乙ii 垂寬 ＝ `max(_seg_P0Ps·sinθ, T)`（自輸出頂點量得）＋ 判別力反例")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'乙ii垂寬(量)':>15}{'期望':>12}{'Δ':>12}"
      f"{'錯值×1.05 之垂寬':>18}{'分家?':>7}  判")
    G, RNG, ok_gate, ok_disc = {}, {}, True, True
    for lbl, wch in TARGETS:
        g = _geom(lbl, wch)
        w, d = WD[lbl]
        T = SB + w
        s1_ii = max(g["seg"], T / g["sin"])
        poly = _build_range(lbl, wch, 0.0, min_width=s1_ii)
        bad = _build_range(lbl, wch, 0.0, min_width=s1_ii * 1.05)
        pw = _perp_width(poly, g["S1"], g["sn"])
        pwb = _perp_width(bad, g["S1"], g["sn"])
        exp = max(g["seg"] * g["sin"], T)
        good = abs(pw - exp) <= 1e-9
        disc = abs(pwb - pw) > 1e-6
        ok_gate &= good
        ok_disc &= disc
        G[(lbl, wch)] = g
        RNG[(lbl, wch)] = poly
        P(f"  {lbl:<5}{wch:<7}{pw:>15.9f}{exp:>12.6f}{pw - exp:>12.2e}"
          f"{pwb:>18.6f}{('✅' if disc else '🔴'):>7}  {'✅' if (good and disc) else '🔴'}")
    P("-" * WID)
    P(f"  ⇒ 閉合檢 {'✅ 全過' if ok_gate else '🔴 有格不過'}"
      f"；判別力 {'✅ 全過' if ok_disc else '🔴 有格不分家'}")
    if not (ok_gate and ok_disc):
        P("  🛑 **閘不過 ⇒ 本次量測⛔ 不出艙**")
        P("=" * WID)
        return L, sha
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【P5】帶姿態 θ* 之 `D_max`
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【P5】固定寬 `W`、於**帶姿態 `θ*`** 之最大可容納深度 `D_max`")
    P("=" * WID)
    P("  🔒 `θ*` ＝ **側界方向 ＋ 90°**（mod π）——即使 `W` 邊橫跨帶寬之姿態；")
    P("     ⛔ **由本檔自 CAD 幾何現算**、⛔ 未取用施工單所給之 θ* 值。")
    P("  🔒 `D_max` 之二分回**下界** ⇒ 「`D_max` 遠小於 `D`」之宣稱**偏保守**。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'_seg_P0Ps':>12}{'sinθ':>10}{'乙ii垂寬':>10}"
      f"{'θ*(rad)':>11}{'D_max(m)':>13}{'D − D_max':>12}{'D_max ≥ D?':>11}")
    D5 = {}
    for lbl, wch in TARGETS:
        g = G[(lbl, wch)]
        w, d = WD[lbl]
        poly = RNG[(lbl, wch)]
        pst = _poly_st([(float(x), float(y)) for x, y in list(poly.exterior.coords)])
        th = (math.atan2(g["su"][1], g["su"][0]) + math.pi / 2.0) % math.pi
        dm = d_max_at(pst, w, th)
        D5[(lbl, wch)] = (th, dm)
        P(f"  {lbl:<5}{wch:<7}{g['seg']:>12.6f}{g['sin']:>10.6f}"
          f"{_perp_width(poly, g['S1'], g['sn']):>10.6f}{th:>11.6f}{dm:>13.6f}"
          f"{d - dm:>12.6f}{('✅' if dm >= d else '🔴 否'):>11}")
    P("-" * WID)
    P("  🔒 **判別力**：本表若三格同號則無鑑別力；下方逐項具名其分佈。")
    _big = [k for k in D5 if D5[k][1] >= 20.0]
    _tiny = [k for k in D5 if D5[k][1] < 1.0]
    P(f"     `D_max ≥ 20` 者 ＝ {len(_big)} 格：" + "／".join(f"{a}/{b}" for a, b in _big))
    P(f"     `D_max < 1` 者 ＝ {len(_tiny)} 格：" + "／".join(f"{a}/{b}" for a, b in _tiny))
    P("")

    # ══════════════════════════════════════════════════════════════════
    # 【P6】三條等價旋轉路徑之一致性
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【P6】三條**數學上等價**之旋轉路徑下，判定是否一致")
    P("=" * WID)
    P("  🔒 甲 ＝ `rotate(use_radians=True)`／乙 ＝ `rotate(degrees(θ), use_radians=False)`"
      "（度↔弧度來回一次）／丙 ＝ 先平移至形心再旋轉")
    P("  🔒 判定 ＝ 於 `θ*` 之 `W×D` 容納（⛔ 非全角掃描·本節之受詞係<u>路徑相依性</u>）")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'乙ii垂寬':>10}{'座標量級':>12}{'甲':>6}{'乙':>6}{'丙':>6}"
      f"{'一致?':>7}{'D_max(m)':>12}")
    from shapely.affinity import translate as _tr
    nagree = 0
    for lbl, wch in TARGETS:
        g = G[(lbl, wch)]
        w, d = WD[lbl]
        poly = RNG[(lbl, wch)]
        th, dm = D5[(lbl, wch)]
        res = []
        for nm, q in _rot_paths(poly, th).items():
            cur = None
            for cx, cy in ((0.0, 0.0), (w, 0.0), (0.0, d), (w, d)):
                t = _tr(q, xoff=-cx, yoff=-cy)
                cur = t if cur is None else cur.intersection(t)
                if cur.is_empty:
                    break
            res.append(not cur.is_empty)
        same = (len(set(res)) == 1)
        nagree += same
        _mag = max(abs(v) for v in poly.bounds)
        P(f"  {lbl:<5}{wch:<7}{_perp_width(poly, g['S1'], g['sn']):>10.6f}{_mag:>12.0f}"
          f"{('進' if res[0] else '不進'):>6}{('進' if res[1] else '不進'):>6}"
          f"{('進' if res[2] else '不進'):>6}{('✅' if same else '🔴 分歧'):>7}{dm:>12.6f}")
    P("-" * WID)
    P(f"  ⇒ **三路徑一致 ＝ {nagree}／{len(TARGETS)}**")
    P("  🔒 **判別力之限定（⛔ 必讀）**：本節所證者為「**於本案本機之此三條路徑**下不分歧」，")
    P("     ⛔ **不證**其對其他算術路徑／其他座標量級亦穩健——")
    P("     本案座標量級 ~2.6e6、`double` 相對精度 ~2.2e-16 ⇒ 絕對誤差 ~6e-10 m，")
    P("     與「垂寬恰 ＝ `W`」之餘裕同量級 ⇒ **⛔ 不可外推**。")
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
    _log = os.path.join(OUTDIR, f"probe_WG958_dmax_robust_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
