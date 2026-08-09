# -*- coding: utf-8 -*-
r"""**D-2b-17 §f-1c**：相鄰宗對「甲≈0 vs 乙 0.3–0.7」之**矛盾裁決**。

## 為何需要
§f-1 之對打出現**兩種**不一致，方向相反：
  · **大值**（R2 `宗0×宗k`／R5 `宗0×宗k`）：甲 76.26／72.20 vs 乙 77.75／74.15 ⇒ **一致**；
  · **小值**（`宗k×宗k+1` 等**相鄰**對）：甲 `< 5e-5` vs 乙 `0.30–0.71` ⇒ **矛盾**。
⛔ 施工單 §f-1 明令「不得以『差在容差內』代替判讀」⇒ 小值矛盾**須裁決**，不得略過。

## 裁決法（⛔ 不倚賴任一量法之面積值）
對乙所判「同屬 A 且屬 B」之格點，計算其**到 A 邊界**與**到 B 邊界**之
**點–線段最短距離**（純 numpy 自實作）。取 `d = min(d_A, d_B)` 之**最大值**：
  · `max d` **顯著 > 0**（≥ 1e-3 m）⇒ 該處存在**有實寬之公共內部** ⇒ **重疊為真**、
    甲之 `≈0` 係**假陰性**；
  · `max d` ≈ 0（同格距量級）⇒ 乙所數者全係**貼邊格**⇒ **乙之偏壓**、甲為真。
🔒 本判準**與面積無關**、亦**與 `.intersection()` 無關** ⇒ 可獨立裁決兩法。

⛔ 本批零生產碼變更。
"""
import io
import os
import sys
import contextlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
from probe_D2b17_dual import (_rings_of, poly_area_np, poly_bbox_np,  # noqa: E402
                              in_geom_np, replicate_pieces, overlap_B)

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b17_adjacent.log")
W = 200


def dist_to_boundary(px, py, rings):
    """點到多邊形**邊界**之最短距離（點–線段·純 numpy 自實作）。⛔ 未用 shapely。"""
    best = np.full(px.shape, np.inf)
    for ext, hol in rings:
        for ring in [ext] + list(hol):
            if len(ring) < 2:
                continue
            a = ring
            b = np.roll(ring, -1, axis=0)
            for i in range(len(ring)):
                ax, ay = a[i, 0], a[i, 1]
                bx, by = b[i, 0], b[i, 1]
                vx, vy = bx - ax, by - ay
                L2 = vx * vx + vy * vy
                if L2 <= 0:
                    d = np.hypot(px - ax, py - ay)
                else:
                    t = ((px - ax) * vx + (py - ay) * vy) / L2
                    t = np.clip(t, 0.0, 1.0)
                    d = np.hypot(px - (ax + t * vx), py - (ay + t * vy))
                np.minimum(best, d, out=best)
    return best


def adjudicate(gA, gB, n=2600, tag=""):
    """回傳乙-正區之最大內部深度。`max_d` ＝ min(d_A, d_B) 之最大值。"""
    bA, bB = poly_bbox_np(gA), poly_bbox_np(gB)
    if bA is None or bB is None:
        return None
    x0, y0 = max(bA[0], bB[0]), max(bA[1], bB[1])
    x1, y1 = min(bA[2], bB[2]), min(bA[3], bB[3])
    if not (x1 > x0 and y1 > y0):
        return {"tag": tag, "n_both": 0, "max_d": 0.0, "cell_h": 0.0, "verdict": "bbox 不交"}
    rA, rB = _rings_of(gA), _rings_of(gB)
    gx = x0 + (np.arange(n) + 0.5) * (x1 - x0) / n
    gy = y0 + (np.arange(n) + 0.5) * (y1 - y0) / n
    XX, YY = np.meshgrid(gx, gy)
    px, py = XX.ravel(), YY.ravel()
    m = in_geom_np(px, py, rA) & in_geom_np(px, py, rB)
    cell_h = min((x1 - x0) / n, (y1 - y0) / n)
    if not m.any():
        return {"tag": tag, "n_both": 0, "max_d": 0.0, "cell_h": cell_h,
                "verdict": "乙 亦判 0"}
    qx, qy = px[m], py[m]
    dA = dist_to_boundary(qx, qy, rA)
    dB = dist_to_boundary(qx, qy, rB)
    d = np.minimum(dA, dB)
    return {"tag": tag, "n_both": int(m.sum()), "max_d": float(d.max()),
            "med_d": float(np.median(d)), "cell_h": cell_h,
            "verdict": ("重疊為真（有實寬公共內部）" if float(d.max()) >= 1e-3
                        else "乙 之貼邊偏壓")}


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-17 §f-1c】相鄰宗對之矛盾裁決（判準＝公共內部之**實寬**·⛔ 與面積無關）")
    P("=" * W)
    import shapely
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P("  判準：對乙判「同屬 A∧B」之格點，取 min(到 A 邊界, 到 B 邊界) 之**最大值** `max_d`。")
    P("        `max_d ≥ 1e-3 m` ⇒ 公共內部有實寬 ⇒ **重疊為真**（甲之 ≈0 係假陰性）；")
    P("        `max_d ≈ 格距`  ⇒ 全係貼邊格 ⇒ **乙之偏壓**（甲為真）。")

    ns, fake_st = harvest()
    CAP = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        key = (_spy.tag, _label)
        if key not in CAP:
            try:
                pieces, biz = replicate_pieces(ns, block_poly, d_hat, corner_pt,
                                               allocation_dir, biz_polys)
                CAP[key] = {"block": block_poly, "pieces": pieces, "biz": biz}
            except Exception as e:                                  # noqa: BLE001
                CAP[key] = {"err": f"{type(e).__name__}: {e}"}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)
    _spy.tag = ""

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    _blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in _blks:
            _blks.append(_l)
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in _blks:
            _spy.tag = sb
            ns["_pool_strips_for_block"] = _spy
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass
            finally:
                ns["_pool_strips_for_block"] = _orig
            print(f"    [{sb}] {lbl} 擷取完畢", file=sys.stderr)

    # ── 逐格裁決：甲、乙皆算，再以實寬判準裁 ──
    P("")
    P(f"  {'情境':<5}{'街廓':<5}{'對':<12}{'甲':>12}{'乙':>12}{'乙-正格數':>10}"
      f"{'max_d(m)':>11}{'中位 d':>11}{'格距(m)':>10}  裁決")
    P("-" * W)
    for (sb, lbl) in sorted(CAP.keys()):
        c = CAP[(sb, lbl)]
        if "err" in c or c.get("biz") is None:
            continue
        biz = c["biz"]
        rows = []
        for i in range(len(biz)):
            for j in range(i + 1, len(biz)):
                a = float(biz[i].intersection(biz[j]).area)
                b = overlap_B(biz[i], biz[j], 400, 1500)["est"]
                if a > 1e-9 or b > 1e-9:
                    rows.append((i, j, a, b))
        for (i, j, a, b) in sorted(rows, key=lambda t: -max(t[2], t[3])):
            r = adjudicate(biz[i], biz[j], 2600, f"{lbl}:{i}×{j}")
            if r is None:
                continue
            P(f"  {sb:<5}{lbl:<5}{f'宗{i}×宗{j}':<12}{a:>12.4f}{b:>12.4f}"
              f"{r['n_both']:>10}{r['max_d']:>11.6f}{r.get('med_d', 0):>11.6f}"
              f"{r['cell_h']:>10.6f}  {r['verdict']}")
    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n→ {LOG}", file=sys.stderr)


if __name__ == "__main__":
    main()
