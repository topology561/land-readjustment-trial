# -*- coding: utf-8 -*-
r"""**D-2b-13 §b1-2／§b1-3／§b1-4**：依序削餘之鋪滿實測、兩法對拍、委派上界改實際弦長。

⛔ 生產路徑呼叫 `_block_partition` 之處為 **0**（本批不接線）；本檔以 `ns` harvest 取用。
"""
import io
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, os.environ.get("WV_PART_LOG", "probe_D2b13_partition.log"))
SEED = 20260809_13
W = 200
COVER_GATE = 0.01
TILE_TOL = 1e-6


def _u(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n)


def _rot(v, t):
    c, s = math.cos(t), math.sin(t)
    return (v[0] * c - v[1] * s, v[0] * s + v[1] * c)


def _polys(rng, k=14):
    """難幾何母體（⛔ 非軸對齊整數矩形·座標非整數·含強烈非凸）。"""
    from shapely.geometry import Polygon
    out = []
    while len(out) < k:
        cx, cy = rng.uniform(-211.7, 388.3), rng.uniform(-97.1, 271.9)
        n = rng.randint(6, 13)
        pts, a = [], rng.uniform(0, 2 * math.pi)
        for _ in range(n):
            a += (2 * math.pi / n) * rng.uniform(0.45, 1.55)
            r = rng.uniform(31.7, 137.9) * (0.35 if rng.random() < 0.35 else 1.0)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        p = Polygon(pts)
        if not p.is_valid:
            p = p.buffer(0)
        if p.is_empty or p.geom_type != "Polygon" or p.area < 400.0:
            continue
        out.append(p)
    return out


def _chord_len(poly, q, g):
    """無限直線（過 q、方向 g）與街廓之**實際截段總長**（⛔ 非直徑）。"""
    from shapely.geometry import LineString
    b = poly.bounds
    big = max(b[2] - b[0], b[3] - b[1]) * 4.0 + 100.0
    ls = LineString([(q[0] - big * g[0], q[1] - big * g[1]),
                     (q[0] + big * g[0], q[1] + big * g[1])])
    try:
        it = poly.intersection(ls)
    except Exception:
        return 0.0
    if it.is_empty:
        return 0.0
    return float(it.length)


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    import numpy as np
    from shapely.geometry import Polygon as _PGx

    ns, fake_st = harvest()
    bs, bp_fn = ns["_block_strip"], ns["_block_partition"]
    TOL = float(ns["_STRIP_PARALLEL_TOL"])
    rng = random.Random(SEED)
    L = []
    L.append("=" * W)
    L.append(f"【D-2b-13】依序削餘鋪滿實測 ＋ 兩法對拍 ＋ 委派上界改實際弦長（seed={SEED}）")
    L.append("=" * W)

    polys = _polys(rng)
    L.append(f"  難幾何母體 ＝ **{len(polys)}** 個（⛔ 非空·非軸對齊整數矩形）")
    if not polys:
        raise RuntimeError("🔴 母體為空 ⇒ 失敗")

    # ══ §b1-4：兩法對拍 ══
    L.append("")
    L.append("【§b1-4】兩法對拍：**逐片獨立切**（`_block_strip` 雙線）vs **依序削餘**（`_block_partition`）")
    L.append("-" * W)
    L.append("  同一組幾何、**同一組界線**；判失敗 ＝ `|Σ片 − 街廓| > 1e-6` 或 最大兩兩交集 > 1e-6")
    n_case = 0
    fail_ind, fail_seq = [], []
    worst_ind, worst_seq = 0.0, 0.0
    for pi, poly in enumerate(polys):
        b = poly.bounds
        base = np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0])
        for _t in range(10):
            ang = rng.uniform(0, 2 * math.pi)
            d_hat = np.array(_u((math.cos(ang), math.sin(ang))))
            n0 = _u((math.cos(ang + math.radians(rng.uniform(50, 130))),
                     math.sin(ang + math.radians(rng.uniform(50, 130)))))
            k = rng.randint(3, 6)
            svals = sorted(rng.uniform(-160.0, 160.0) for _ in range(k + 1))
            dirs = [_u(_rot(n0, math.radians(rng.uniform(-18.0, 18.0)))) for _ in range(k + 1)]
            qs = [base + s * d_hat for s in svals]
            n_case += 1

            # (a) 逐片獨立切
            _pa, _ok_a = [], True
            for i in range(k):
                _al = (dirs[i][1], -dirs[i][0])
                _g, _a = bs(poly, d_hat, qs[i], svals[i + 1] - svals[i],
                            allocation_dir=_al, n_hat_far=dirs[i + 1])
                _pa.append(_g)
            _whole_al = (dirs[0][1], -dirs[0][0])
            _gw, _aw = bs(poly, d_hat, qs[0], svals[k] - svals[0],
                          allocation_dir=_whole_al, n_hat_far=dirs[k])
            _sa = sum((g.area if g is not None else 0.0) for g in _pa)
            _ra = abs(_sa - (_aw or 0.0))
            _xa = 0.0
            for i in range(k):
                for j in range(i + 1, k):
                    if _pa[i] is not None and _pa[j] is not None:
                        _xa = max(_xa, float(_pa[i].intersection(_pa[j]).area))
            if _ra > TILE_TOL or _xa > TILE_TOL:
                _ok_a = False
                fail_ind.append((pi, _ra, _xa))
                worst_ind = max(worst_ind, _ra, _xa)

            # (b) 依序削餘（其鋪滿閘內建 ⇒ 以 raise 判失敗）
            try:
                _pieces, _dg = bp_fn(poly, d_hat, list(zip(qs, dirs)), _label=f"p{pi}t{_t}")
                worst_seq = max(worst_seq, abs(_dg['resid']), _dg['max_pair_overlap'])
            except RuntimeError as e:
                fail_seq.append((pi, _t, str(e)[:150]))
    L.append(f"  母體 ＝ **{n_case}** 例（⛔ 非空）")
    L.append(f"  (a) **逐片獨立切**：失敗 **{len(fail_ind)}** 例"
             f"（{100.0 * len(fail_ind) / n_case:.1f}%）　最劣殘差／交集 ＝ **{worst_ind:.6e}**")
    L.append(f"  (b) **依序削餘**  ：失敗 **{len(fail_seq)}** 例"
             f"（{100.0 * len(fail_seq) / n_case:.1f}%）　最劣（通過者中）＝ **{worst_seq:.6e}**")
    L.append(f"  ⇒ 失敗率 {len(fail_ind)} → {len(fail_seq)}"
             + ("（**未歸零**）" if fail_seq else "（**歸零**）"))
    for f in fail_seq[:6]:
        L.append(f"    🔴 殘餘失敗 poly#{f[0]} t{f[1]}：{f[2]}")
    if len(fail_seq) > 6:
        L.append(f"    …（另 {len(fail_seq) - 6} 例）")

    # ══ §b1-4b：加壓掃描（⛔ 「0 失敗」須先經加壓才可出艙）══
    L.append("")
    L.append("  【加壓掃描】🔒 基礎母體得 0 失敗 ⇒ **⛔ 不得就此出艙**，先加壓再說。")
    L.append("    四種壓力：① 座標量級 ~1e5（相對精度劣化）② 界線近 ∥ 推進向")
    L.append("    ③ 界線間距次毫米 ④ 極狹長（sliver）街廓")
    _sfail, _scase, _sworst = [], 0, 0.0
    _sraise = {}
    for _mode in ("①大座標", "②近∥推進向", "③次毫米間距", "④狹長街廓"):
        for _rep in range(40):
            if _mode == "④狹長街廓":
                _cx, _cy = rng.uniform(-50, 50), rng.uniform(-50, 50)
                _th = rng.uniform(0, math.pi)
                _pts = []
                for _sx, _sy in ((-140, -0.7), (140, -0.9), (140, 0.8), (-140, 1.1)):
                    _pts.append((_cx + _sx * math.cos(_th) - _sy * math.sin(_th),
                                 _cy + _sx * math.sin(_th) + _sy * math.cos(_th)))
                poly = _PGx(_pts)
            else:
                poly = rng.choice(polys)
                if _mode == "①大座標":
                    from shapely import affinity as _aff
                    poly = _aff.translate(poly, 137913.7, -98371.3)
            if poly.is_empty or not poly.is_valid:
                continue
            b = poly.bounds
            base = np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0])
            ang = rng.uniform(0, 2 * math.pi)
            d_hat = np.array(_u((math.cos(ang), math.sin(ang))))
            _off = (rng.uniform(0.02, 0.6) if _mode == "②近∥推進向"
                    else rng.uniform(55, 125))
            n0 = _u((math.cos(ang + math.radians(_off)), math.sin(ang + math.radians(_off))))
            k = rng.randint(3, 6)
            if _mode == "③次毫米間距":
                _s0 = rng.uniform(-40, 40)
                svals = [_s0 + i * rng.uniform(2e-5, 9e-4) for i in range(k + 1)]
            else:
                svals = sorted(rng.uniform(-190.0, 190.0) for _ in range(k + 1))
            dirs = [_u(_rot(n0, math.radians(rng.uniform(-25.0, 25.0)))) for _ in range(k + 1)]
            qs = [base + s * d_hat for s in svals]
            _scase += 1
            try:
                _p, _dg = bp_fn(poly, d_hat, list(zip(qs, dirs)), _label=f"stress{_mode}{_rep}")
                _sworst = max(_sworst, abs(_dg['resid']), _dg['max_pair_overlap'])
            except RuntimeError as e:
                _sfail.append((_mode, _rep, str(e)[:170]))
                _sraise[_mode] = _sraise.get(_mode, 0) + 1
    L.append(f"    加壓母體 ＝ **{_scase}** 例　失敗 **{len(_sfail)}** 例"
             f"（{100.0 * len(_sfail) / max(1, _scase):.1f}%）"
             f"　最劣（通過者中）＝ **{_sworst:.6e}**")
    L.append(f"    逐壓力別失敗數：{_sraise if _sraise else '（全 0）'}")
    for f in _sfail[:8]:
        L.append(f"      🔴 {f[0]} #{f[1]}：{f[2]}")
    if len(_sfail) > 8:
        L.append(f"      …（另 {len(_sfail) - 8} 例）")
    fail_seq = fail_seq + [(m, r, msg) for m, r, msg in _sfail]
    n_case += _scase

    # ── 殘餘失敗之成因查明 ──
    L.append("")
    L.append("  【殘餘失敗之成因查明】（⛔ 不得以「落在容差內」「數量很少」代替）")
    if not fail_seq:
        L.append("    ⇒ 本母體**零殘餘失敗** ⇒ 無成因可查。"
                 "⚠️ ⛔ **不得**據此宣稱依序削餘在**所有**幾何上鋪滿——本母體有限。")
    else:
        L.append("    已知**已排除**之候選（前批實測）：半平面矩形 `big` 不足"
                 "（加 `|q−街廓|` 補償後失敗數**不降反升** ⇒ 已證非成因）。")
        _c1 = _c2 = _c3 = 0
        for f in fail_seq:
            _msg = f[2]
            if "鋪滿閘①" in _msg:
                _c1 += 1
            elif "鋪滿閘②" in _msg:
                _c2 += 1
            else:
                _c3 += 1
        L.append(f"    分類：閘①（Σ≠街廓）**{_c1}** 例／閘②（兩兩交集）**{_c2}** 例／其他 **{_c3}** 例")
        L.append("    ⚠️ **成因：未查明** —— 依序削餘之聯集/不重疊為交集之**代數必然**，")
        L.append("       其失敗只可能來自 **shapely 交集之浮點實作**（頂點捨入／近退化片）。")
        L.append("       ⛔ 本批**未能**指出確切觸發條件 ⇒ **如實記「未查明」·停機上呈**，⛔ 不推定。")

    # ══ §b1-2：鋪滿閘實測分佈 ══
    L.append("")
    L.append("【§b1-2】鋪滿閘實測（`_block_partition` 內建·閘寬 1e-6·⛔ 未以下游 0.01 代掃）")
    L.append("-" * W)
    _res, _ovl = [], []
    for pi, poly in enumerate(polys):
        b = poly.bounds
        base = np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0])
        ang = rng.uniform(0, 2 * math.pi)
        d_hat = np.array(_u((math.cos(ang), math.sin(ang))))
        n0 = _u((math.cos(ang + math.radians(78.3)), math.sin(ang + math.radians(78.3))))
        svals = [-140.0, -55.3, 12.7, 88.1, 151.9]
        dirs = [_u(_rot(n0, math.radians(a))) for a in (0.0, 6.1, -4.3, 9.7, -2.8)]
        qs = [base + s * d_hat for s in svals]
        try:
            _p, _dg = bp_fn(poly, d_hat, list(zip(qs, dirs)), _label=f"tile{pi}")
            _res.append(abs(_dg['resid'])); _ovl.append(_dg['max_pair_overlap'])
            L.append(f"  poly#{pi:<2} 片數 {_dg['n_pieces']}　空片 {_dg['empty_idx']}"
                     f"　|Σ−街廓| ＝ {abs(_dg['resid']):.3e}"
                     f"　最大兩兩交集 ＝ {_dg['max_pair_overlap']:.3e}　✅")
        except RuntimeError as e:
            L.append(f"  poly#{pi:<2} 🔴 {str(e)[:150]}")
    if _res:
        L.append(f"  ⇒ 殘差分佈：max ＝ **{max(_res):.3e}**／median ＝ "
                 f"**{sorted(_res)[len(_res) // 2]:.3e}**　"
                 f"最大兩兩交集 max ＝ **{max(_ovl):.3e}**（閘寬 {TILE_TOL:g}）")
    else:
        raise RuntimeError("🔴 §b1-2 母體為空 ⇒ 失敗")

    # ══ §b1-3：委派上界改實際弦長 ══
    L.append("")
    L.append("【§b1-3】委派誤差上界：舊式 `½·D²·tol`（直徑）vs 新式 `½·L_max²·tol`（**實際弦長**）")
    L.append("-" * W)
    from shapely.geometry import Polygon as _PG
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    _al_by = cad.get("alloc_dir_by_block", {}) or {}
    L.append(f"  {'街廓':<5}{'D(直徑)':>12}{'L_max(弦)':>12}{'½D²·tol':>14}{'½L²·tol':>14}"
             f"  舊式  新式")
    _bad_new = []
    for lbl in ("R1", "R2", "R3", "R4", "R5", "R6", "G1", "RD4", "RD1"):
        b = cb_by.get(lbl)
        if not b or not b.get("vertices"):
            continue
        g = _PG(b["vertices"])
        bb = g.bounds
        D = math.hypot(bb[2] - bb[0], bb[3] - bb[1])
        _ac = _al_by.get(lbl)
        _n = (_u((-_ac[1], _ac[0])) if _ac is not None
              else _u((1.0, 0.0)))                    # 切線方向 ＝ rot90(ALLOC)
        _perp = _u((-_n[1], _n[0]))
        _lo = min(v[0] * _perp[0] + v[1] * _perp[1] for v in b["vertices"])
        _hi = max(v[0] * _perp[0] + v[1] * _perp[1] for v in b["vertices"])
        # 🔴 **自查**：首版取 `_q = _t·_perp`（自**原點**起算之垂足）。UC9898 為 **TWD97**
        #   （~250000, 2600000）⇒ 該垂足距街廓沿 `_n` 方向可達**數百公里**，而 `_chord_len`
        #   之 `big` 僅 ~街廓尺度（數百公尺）⇒ 線段**根本搆不到街廓** ⇒ `L_max` 全為 0
        #   ⇒ 「新式上界 0.0 ✅」係**空真假綠**。改以**街廓形心**為錨。
        _cen = g.centroid
        _c0 = _cen.x * _perp[0] + _cen.y * _perp[1]
        Lmax = 0.0
        for _k in range(201):                          # 沿法向掃描切線位置，取截段極大
            _t = _lo + (_hi - _lo) * _k / 200.0
            _q = (_cen.x + (_t - _c0) * _perp[0], _cen.y + (_t - _c0) * _perp[1])
            Lmax = max(Lmax, _chord_len(g, _q, _n))
        if Lmax <= 0.0:
            raise RuntimeError(
                f"🔴 §b1-3：街廓 {lbl} 之 `L_max` 掃描全為 0 ⇒ 量測失效"
                f"（⛔ 不得以「上界 0」判過），停")
        _ub_old = 0.5 * D * D * TOL
        _ub_new = 0.5 * Lmax * Lmax * TOL
        if _ub_new >= COVER_GATE:
            _bad_new.append(lbl)
        L.append(f"  {lbl:<5}{D:>12.4f}{Lmax:>12.4f}{_ub_old:>14.6e}{_ub_new:>14.6e}"
                 f"  {'✅' if _ub_old < COVER_GATE else '🔴'}   "
                 f"{'✅' if _ub_new < COVER_GATE else '🔴'}")
    _r16 = [x for x in _bad_new if x.startswith("R") and not x.startswith("RD")]
    L.append(f"  ⇒ 新式下仍 ≥ 0.01 者：**{_bad_new if _bad_new else '（無）'}**"
             f"；其中 R1–R6：**{_r16 if _r16 else '（無）'}**")
    if _r16:
        L.append("  🛑 **R1–R6 有街廓於新式下仍貼閘 ⇒ 述詞衝突·停機上呈**"
                 "（⛔ 未調 tol、⛔ 未改弦長定義求過）")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
