#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-41】帶底新定式（`K-9-10`）對寬度判定之影響實測（⛔ 零生產碼·新檔）

🔴 **⛔ 不改 `parcel_min_width_n14`／`_n14_band_hi`**——本探針**另行計算**，
   與舊定式**並列對照**，⛔ 不覆寫、⛔ 不切換生產。

**新舊定式**：
  舊 `t_hi` ＝ min(近側後角之 t , 遠側後角之 t)
  新 `t_band` ＝ min( 最淺**有效垂線**之深度 , 近側境界線終止之深度 )

**「最淺有效垂線」之解析求法（⛔ 非等距取樣）**：
  有效垂線 ＝ 自 FRONTLINE 沿法向至 BASELINE 之完整線段、**整條落在宗內**。
  宗地為切帶 ∩ 街廓 ⇒ **凸** ⇒ 該垂線與宗之交集為單一線段
  ⇒ 「整條落在宗內」⟺ 其**兩端點**（FRONTLINE 上者、BASELINE 上者）皆在宗內。
  令 `I_F` ＝ 宗 ∩ FRONTLINE 沿 d̂ 之投影區間；`I_B` ＝ 宗 ∩ BASELINE 之同投影區間，
  則有效 s 範圍 ＝ `I_F ∩ I_B`。深度 `D(s)`（FRONT→BASE 沿法向）對 s **線性**
  （二直線之夾角固定）⇒ **極小值必落於該區間之端點** ⇒ 只需比兩端，⛔ 無須取樣。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import math
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 186
EPS = 1e-9


def _short_sha():
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           cwd=VERIFY, capture_output=True, text=True, timeout=20)
        return (r.stdout or "").strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


def unit(dx, dy):
    L = math.hypot(dx, dy)
    return (dx / L, dy / L) if L > EPS else None


def st_of(pt, o, d, n):
    """回 (s, t)：s 沿 FRONTLINE、t 沿其法向（皆相對 o）。"""
    vx, vy = pt[0] - o[0], pt[1] - o[1]
    return (vx * d[0] + vy * d[1], vx * n[0] + vy * n[1])


def clip_interval(poly, o, d, n, t_target, tol=1e-6):
    """宗 ∩ {t ＝ t_target} 之 s 區間（凸 ⇒ 單一區間）。回 (s_lo, s_hi) 或 None。"""
    ext = list(poly.exterior.coords)
    hits = []
    for i in range(len(ext) - 1):
        s1, t1 = st_of(ext[i], o, d, n)
        s2, t2 = st_of(ext[i + 1], o, d, n)
        if abs(t1 - t_target) <= tol:
            hits.append(s1)
        if (t1 - t_target) * (t2 - t_target) < 0:
            r = (t_target - t1) / (t2 - t1)
            hits.append(s1 + r * (s2 - s1))
    if len(hits) < 2:
        return None
    return (min(hits), max(hits))


def width_at(poly, o, d, n, t, tol=1e-6):
    """第四款之寬度：於深度 t 處，沿 FRONTLINE 方向自近側界至遠側界之距離。"""
    iv = clip_interval(poly, o, d, n, t, tol)
    return (iv[1] - iv[0]) if iv else 0.0


def min_width_breakpoints(poly, o, d, n, t_band):
    """斷點法求 [0, t_band] 內之最小寬度（w(t) 分段線性 ⇒ 極小落於斷點）。"""
    if t_band <= 1e-9:
        return 0.0, 0.0
    ts = {0.0, t_band}
    for (x, y) in list(poly.exterior.coords):
        _s, t = st_of((x, y), o, d, n)
        if -1e-9 <= t <= t_band + 1e-9:
            ts.add(min(max(t, 0.0), t_band))
    best, at = None, None
    for t in sorted(ts):
        w = width_at(poly, o, d, n, t)
        if best is None or w < best:
            best, at = w, t
    return best, at


def analyse(poly, o, d, n, D_of_s):
    """回 dict：舊 t_hi／最淺有效垂線深度／近側界終止深度／新 t_band。"""
    ext = list(poly.exterior.coords)[:-1]
    ST = [st_of(p, o, d, n) for p in ext]
    t_max = max(t for _s, t in ST)
    # 🩸 **首版以「t 最大之頂點」當後角 ⇒ 自檢 ② 失敗**（該式對「遠側後角較淺」之形狀
    #    只命中一個頂點，近／遠後角遂同值）。**改依側界取端點**（⛔ 非依 t 極值）：
    #    側界 ＝ 與 FRONTLINE 方向夾角最大之二邊；近側 ＝ 邊中點 s 較小者。
    ring = list(poly.exterior.coords)
    edges = []
    for i in range(len(ring) - 1):
        u = unit(ring[i + 1][0] - ring[i][0], ring[i + 1][1] - ring[i][1])
        if u is None:
            continue
        c = abs(u[0] * d[0] + u[1] * d[1])
        cr = abs(u[0] * d[1] - u[1] * d[0])
        ang = math.degrees(math.atan2(cr, c))
        a_st, b_st = st_of(ring[i], o, d, n), st_of(ring[i + 1], o, d, n)
        edges.append((ang, (a_st[0] + b_st[0]) / 2.0, a_st, b_st))
    edges.sort(key=lambda e: -e[0])
    two = sorted(edges[:2], key=lambda e: e[1])
    near_e, far_e = two[0], two[1]
    t_near_end = max(near_e[2][1], near_e[3][1])
    t_far_end = max(far_e[2][1], far_e[3][1])
    t_hi_old = min(t_near_end, t_far_end)
    # 有效 s 範圍 ＝ (宗 ∩ FRONT) ∩ (宗 ∩ BASE)
    IF = clip_interval(poly, o, d, n, 0.0, tol=1e-3)
    shallow, s_at = None, None
    IB = None
    if IF is not None:
        # BASELINE 在 t ＝ D(s)；先取宗之最深處作為 BASE 之近似 t（凸 ⇒ 端點）
        IB = clip_interval(poly, o, d, n, t_max, tol=1e-3)
        if IB is not None:
            lo, hi = max(IF[0], IB[0]), min(IF[1], IB[1])
            if hi >= lo - 1e-9:
                cand = [(D_of_s(lo), lo), (D_of_s(hi), hi)]
                cand.sort()
                shallow, s_at = cand[0]
    t_band_new = min(x for x in [shallow, t_near_end] if x is not None) \
        if shallow is not None else t_near_end
    return {"t_hi_old": t_hi_old, "shallow": shallow, "s_at": s_at,
            "t_near_end": t_near_end, "t_band_new": t_band_new,
            "IF": IF, "IB": IB, "t_max": t_max}


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    import shapely
    from shapely.geometry import Polygon as _Pg
    P("=" * W)
    P("【W-G.9-41】帶底新定式（`K-9-10`）對寬度判定之影響實測")
    P("=" * W)
    P(f"  產生於 commit：{sha}")
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P("  🔴 ⛔ 未改 parcel_min_width_n14／_n14_band_hi——本探針另行計算、與舊式並列對照")
    P("  🔒 最淺有效垂線：**解析求解**（凸 ⇒ D(s) 線性 ⇒ 極值在端點）·⛔ 非等距取樣")
    P("")

    # ── §0 量測器自檢（⛔ 傾斜測資·⛔ 非軸向矩形）────────────────────────
    P("【0】量測器自檢（⛔ 傾斜測資·附對照組實際輸出）")
    P("-" * W)
    TH = math.radians(19.0)
    d = (math.cos(TH), math.sin(TH))
    n = (-d[1], d[0])
    o = (0.0, 0.0)
    def W2(s, t):  return (o[0] + s * d[0] + t * n[0], o[1] + s * d[1] + t * n[1])
    ok = {}
    # ① 已知 舊 ＝ 新（矩形帶·兩後角等深、近側界貫穿全深）
    p1 = _Pg([W2(0, 0), W2(10, 0), W2(10, 30), W2(0, 30)])
    r1 = analyse(p1, o, d, n, lambda s: 30.0)
    ok["①舊=新"] = abs(r1["t_hi_old"] - r1["t_band_new"]) < 1e-6
    P(f"  ① 已知【舊 ＝ 新】(矩形·後角等深 30)：舊 {r1['t_hi_old']:.4f}／新 {r1['t_band_new']:.4f}"
      f"（最淺有效垂線 {r1['shallow']}, 近側界終止 {r1['t_near_end']:.4f}）⇒ {'✅' if ok['①舊=新'] else '🔴'}")
    # ② 已知 舊 < 新（遠側後角較淺 ⇒ 舊帶較淺）
    p2 = _Pg([W2(0, 0), W2(10, 0), W2(10, 18), W2(0, 30)])
    r2 = analyse(p2, o, d, n, lambda s: 30.0)
    ok["②舊<新"] = (r2["t_hi_old"] < r2["t_band_new"] - 1e-6)
    P(f"  ② 已知【舊 < 新】(遠側後角 18 < 近側 30)：舊 {r2['t_hi_old']:.4f}／新 {r2['t_band_new']:.4f}"
      f"　Δt ＝ {r2['t_band_new']-r2['t_hi_old']:+.4f} ⇒ {'✅' if ok['②舊<新'] else '🔴'}")
    # ③ 已知最小寬度（帶內含頂點·梯形上窄下寬 ⇒ min 在 t=0）
    p3 = _Pg([W2(0, 0), W2(6, 0), W2(10, 20), W2(0, 20)])
    w3, at3 = min_width_breakpoints(p3, o, d, n, 20.0)
    ok["③已知寬"] = abs(w3 - 6.0) < 1e-6 and abs(at3) < 1e-6
    P(f"  ③ 已知【最小寬 ＝ 6.0 @ t=0】(梯形 6→10)：斷點法得 {w3:.6f} @ t={at3:.4f}"
      f" ⇒ {'✅' if ok['③已知寬'] else '🔴'}")
    # ④ 對照：反向梯形（min 應在 t=20）
    p4 = _Pg([W2(0, 0), W2(10, 0), W2(6, 20), W2(0, 20)])
    w4, at4 = min_width_breakpoints(p4, o, d, n, 20.0)
    ok["④對照"] = abs(w4 - 6.0) < 1e-6 and abs(at4 - 20.0) < 1e-6
    P(f"  ④ 對照【最小寬 ＝ 6.0 @ t=20】(反向梯形 10→6)：斷點法得 {w4:.6f} @ t={at4:.4f}"
      f" ⇒ {'✅' if ok['④對照'] else '🔴'}"
      f"　⇒ ③④ 之 min 落在**不同端**，證該法非恆取同一端")
    P(f"  🔒 自檢測資之 FRONTLINE 傾角 ＝ 19°（⛔ 非軸向）")
    allok = all(ok.values())
    P(f"  ⇒ 自檢：{'PASS' if allok else '🛑 FAIL ⇒ S-2 ⇒ 停機·本次量測⛔ 不得出艙'}")
    if not allok:
        P("")
        P("🛑 量測器紅 ⇒ 停機。")
        return L, sha

    # ── §1 驅動 ────────────────────────────────────────────────────
    ns, fake_st = harvest()
    CAP = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        key = (_label, _spy.seq.get(_label, 0))
        _spy.seq[_label] = _spy.seq.get(_label, 0) + 1
        _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
        CAP[key] = {"d_hat": np.asarray(d_hat, float), "biz": list(_biz)}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)
    _spy.seq = {}

    import contextlib
    import io as _io
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    BLKS = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in BLKS:
            BLKS.append(_l)
    sb = 0.0
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, sb, snapshot=snapshot)
    ERR = {}
    for lbl in BLKS:
        ns["_pool_strips_for_block"] = _spy
        try:
            with contextlib.redirect_stdout(_io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, sb)
                except Exception as e:                              # noqa: BLE001
                    ERR[lbl] = f"{type(e).__name__}: {str(e)[:90]}"
        finally:
            ns["_pool_strips_for_block"] = _orig

    FL = cad.get("front_lines") or {}
    BL = cad.get("baselines") or {}
    MW = {}
    for r in params:
        try:
            MW[r.get("街廓")] = float(r.get("法定最小寬") or r.get("最小建築寬度") or 0.0)
        except Exception:                                           # noqa: BLE001
            pass

    P("")
    P("【C-2】逐街廓逐側逐宗（⛔ 母體 ＝ 全部街廓）")
    P("-" * W)
    FLIP_F, FLIP_B, DT = [], [], []
    for lbl in BLKS:
        key = next((k for k in CAP if k[0] == lbl), None)
        fl = FL.get(lbl) or {}
        bl = BL.get(lbl) or {}
        if key is None or not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            P(f"  {lbl}：⛔ 缺件 ⇒ **無從量測**"
              f"{'（生產碼 raise：' + ERR[lbl] + '）' if lbl in ERR else ''}")
            continue
        biz = CAP[key]["biz"]
        d_hat = tuple(CAP[key]["d_hat"])
        nrm = (-d_hat[1], d_hat[0])
        o = tuple(float(x) for x in fl["p1"])
        bpt = tuple(float(x) for x in bl["point"])
        # 🩸 **法向須指向 BASELINE 那一側**——首版直接取 rot90(d̂)，實資料之 BASELINE
        #    落在 t **負**側 ⇒ 全部 t 為負、`t_hi(舊)` 退化為 0、`t_band` 為負（帶為空）。
        #    自檢測資由我自訂 t 正向朝 BASELINE ⇒ **不具備該性質** ⇒ 自檢過而實測錯
        #    （＝考古 85 修法 2「對照物須具備使量測困難的那個性質」之再犯）。
        if (bpt[0] - o[0]) * nrm[0] + (bpt[1] - o[1]) * nrm[1] < 0:
            nrm = (-nrm[0], -nrm[1])
        bang = math.radians(float(bl.get("angle_deg", 0.0)))
        bdir = (math.cos(bang), math.sin(bang))
        # D(s)：FRONTLINE 上 s 處沿 nrm 至 BASELINE 之距離（解析）
        bs, bt = st_of(bpt, o, d_hat, nrm)
        bds = bdir[0] * d_hat[0] + bdir[1] * d_hat[1]
        bdt = bdir[0] * nrm[0] + bdir[1] * nrm[1]
        def D_of_s(s, _bs=bs, _bt=bt, _bds=bds, _bdt=bdt):
            if abs(_bds) < 1e-12:
                return _bt
            return _bt + (s - _bs) * (_bdt / _bds)
        mw = MW.get(lbl, 3.5) or 3.5
        P("")
        P(f"  ── {lbl}（{len(biz)} 宗·法定最小寬 {mw:.2f}）"
          f"{'　⚠️ raise：' + ERR[lbl] if lbl in ERR else ''} ──")
        P(f"    {'i':<4}{'t_hi(舊)':>11}{'最淺有效':>11}{'@s':>11}{'近側終止':>11}"
          f"{'t_band(新)':>12}{'Δt':>10}{'舊min寬':>10}{'新min寬':>10}{'Δ寬':>9}"
          f"{'舊判':>7}{'新判':>7}  翻轉")
        for i, g in enumerate(biz):
            try:
                r = analyse(g, o, d_hat, nrm, D_of_s)
            except Exception as e:                                  # noqa: BLE001
                P(f"    {i:<4}⛔ 分析失敗：{type(e).__name__} ⇒ 無從判定")
                continue
            dt = r["t_band_new"] - r["t_hi_old"]
            w_old, _ = min_width_breakpoints(g, o, d_hat, nrm, r["t_hi_old"])
            w_new, _ = min_width_breakpoints(g, o, d_hat, nrm, r["t_band_new"])
            j_old = "合格" if w_old >= mw - 1e-9 else "不合格"
            j_new = "合格" if w_new >= mw - 1e-9 else "不合格"
            flip = ""
            if j_old == "合格" and j_new == "不合格":
                flip = "🔴 合→不"
                FLIP_F.append((lbl, i, float(g.area), w_old, w_new))
            elif j_old == "不合格" and j_new == "合格":
                flip = "🔵 不→合"
                FLIP_B.append((lbl, i, float(g.area), w_old, w_new))
            if abs(dt) > 1e-6:
                DT.append((lbl, i, dt))
            P(f"    {i:<4}{r['t_hi_old']:>11.4f}"
              f"{(f'{r[chr(115)+chr(104)+chr(97)+chr(108)+chr(108)+chr(111)+chr(119)]:.4f}' if r['shallow'] is not None else '—'):>11}"
              f"{(f'{r[chr(115)+chr(95)+chr(97)+chr(116)]:.4f}' if r['s_at'] is not None else '—'):>11}"
              f"{r['t_near_end']:>11.4f}{r['t_band_new']:>12.4f}{dt:>+10.4f}"
              f"{w_old:>10.4f}{w_new:>10.4f}{w_new-w_old:>+9.4f}"
              f"{j_old:>7}{j_new:>7}  {flip}")

    P("")
    P("【C-3】統計（⛔ 逐宗可回溯）")
    P("-" * W)
    P(f"  |Δt| > 1e-6 之宗數 ＝ {len(DT)}")
    if DT:
        agg = {}
        for lbl, i, dt in DT:
            agg.setdefault(lbl, []).append(dt)
        for lbl, v in sorted(agg.items()):
            P(f"    {lbl}: {len(v)} 宗　Δt 範圍 [{min(v):+.4f}, {max(v):+.4f}]")
    else:
        P("  🔒 零計數之構造（空集鐵律）：見自檢 ②——已知 舊<新 之測資，"
          f"本探針得 Δt ＝ {r2['t_band_new']-r2['t_hi_old']:+.4f} ⇒ 該計數非恆 0。")
    P(f"  判定翻轉 合格→不合格 ＝ {len(FLIP_F)} 宗")
    if FLIP_F:
        ar = [x[2] for x in FLIP_F]
        P(f"    面積 帶號合計 {sum(ar):+.4f}　絕對值合計 {sum(abs(x) for x in ar):.4f}")
        for lbl, i, a, wo, wn in FLIP_F:
            P(f"      {lbl} i={i:<3} 面積 {a:>10.4f}　舊寬 {wo:.4f} → 新寬 {wn:.4f}")
    P(f"  反向翻轉 不合格→合格 ＝ {len(FLIP_B)} 宗")
    if FLIP_B:
        for lbl, i, a, wo, wn in FLIP_B:
            P(f"      {lbl} i={i:<3} 面積 {a:>10.4f}　舊寬 {wo:.4f} → 新寬 {wn:.4f}")
    else:
        P("    🔒 零計數之構造（空集鐵律）：本探針之翻轉判定式對兩方向**對稱**"
          "（`j_old==合格 and j_new==不合格` ／ 其反向），"
          "且自檢 ②③④ 已證 `t_band` 與 `min_width` 兩量皆隨形狀變動"
          " ⇒ 反向翻轉之計數**非結構上恆 0**；本案實得 0 係資料所致。")
    if len(FLIP_B) == 0 and len(FLIP_F) > 0:
        code = "新定式較嚴（僅單向翻轉）"
    elif len(FLIP_B) > 0 and len(FLIP_F) > 0:
        code = "雙向翻轉（附各自清單）"
    elif len(FLIP_B) == 0 and len(FLIP_F) == 0:
        code = "無翻轉（新舊定式於本案對判定等價）"
    else:
        code = "雙向翻轉（附各自清單）"
    P("")
    P(f"  🔒 出艙碼 ＝ **{code}**")
    if ERR:
        P("")
        P("  ⚠️ 生產碼 raise 之街廓（⛔ 不影響 CAP）：")
        for k, v in ERR.items():
            P(f"    {k}: {v}")
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
    with open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
