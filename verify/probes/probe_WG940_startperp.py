#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-40】`K-9-9` 起算垂線約束之現況違反範圍實測（⛔ 零生產碼·新檔）

受詞：對**全部街廓之兩側**，逐宗（第 2 宗起）判其遠側境界線是否滿足 `K-9-9 二`
（FRONTLINE 交點與 BASELINE 交點**皆須在起算垂線之對應端點之後**）。

🔴 **⛔ 禁以街廓名／側別／宗序號硬編**——甲乙之判別、左右分界，一律**由量得之幾何決定**。
🔴 生產碼之 `②-宗 圍堵閘`於部分街廓**必 raise** ⇒ 一律 `try/except` 包住，⛔ 不因其中止量測。
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
W = 178
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


def line_isect(p, u, q, v):
    """過 p 方向 u 之直線 × 過 q 方向 v 之直線。平行 ⇒ None。"""
    den = u[0] * v[1] - u[1] * v[0]
    if abs(den) < 1e-12:
        return None
    t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / den
    return (p[0] + t * u[0], p[1] + t * u[1])


def s_of(pt, origin, d):
    """沿 FRONTLINE 方向之定序座標（相對 origin）。"""
    return (pt[0] - origin[0]) * d[0] + (pt[1] - origin[1]) * d[1]


def far_side_dir_and_pt(poly, d_hat):
    """自宗地多邊形取其**遠側界**（沿推進方向 s 較大之側界）之 (方向, 一點)。

    側界 ＝ 與 FRONTLINE 方向夾角最大之二邊；遠側 ＝ 其中邊中點 s 較大者。
    """
    ext = list(poly.exterior.coords)
    cand = []
    for t in range(len(ext) - 1):
        u = unit(ext[t + 1][0] - ext[t][0], ext[t + 1][1] - ext[t][1])
        if u is None:
            continue
        c = abs(u[0] * d_hat[0] + u[1] * d_hat[1])
        cr = abs(u[0] * d_hat[1] - u[1] * d_hat[0])
        ang = math.degrees(math.atan2(cr, c))
        mid = ((ext[t][0] + ext[t + 1][0]) / 2, (ext[t][1] + ext[t + 1][1]) / 2)
        cand.append((ang, u, mid))
    if len(cand) < 2:
        return None, None
    cand.sort(key=lambda e: -e[0])
    two = cand[:2]
    two.sort(key=lambda e: e[2][0] * d_hat[0] + e[2][1] * d_hat[1])
    return two[1][1], two[1][2]      # 遠側


def eval_lot(P_prev, B_prev, P_cur, B_cur, o, d, n):
    """K-9-9 二：回 (情形, 起算垂線兩端, 兩端差額, 出艙碼)。

    o/d ＝ FRONTLINE 之原點與方向；n ＝ FRONTLINE 法向。
    """
    # B⊥ ＝ 自 P_prev 沿 n 至 BASELINE 之垂足 ；P⊥ ＝ 自 B_prev 沿 n 至 FRONTLINE 之垂足
    # 兩者之 s 座標（沿 d 定序）
    s_Pprev = s_of(P_prev, o, d)
    s_Pperp = s_of(B_prev, o, d)      # B_prev 沿 n 投影到 FRONTLINE ⇒ 其 s 不變
    s_Bperp = s_Pprev                 # P_prev 沿 n 投影到 BASELINE ⇒ 其 s 不變
    s_Bprev = s_of(B_prev, o, d)
    if s_Pperp < s_Pprev - 1e-9:
        case = "甲"
        start_front_s, start_base_s = s_Pprev, s_Bperp
    elif s_Pperp > s_Pprev + 1e-9:
        case = "乙"
        start_front_s, start_base_s = s_Pperp, s_Bprev
    else:
        case = "退化(P⊥＝P_prev)"
        start_front_s, start_base_s = s_Pprev, s_Bprev
    s_Pcur = s_of(P_cur, o, d)
    s_Bcur = s_of(B_cur, o, d)
    d_front = s_Pcur - start_front_s
    d_base = s_Bcur - start_base_s
    if d_front >= -1e-6 and d_base >= -1e-6:
        code = "合格"
    else:
        code = "不合格"
    return case, (start_front_s, start_base_s), (d_front, d_base), code


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    import shapely
    P("=" * W)
    P("【W-G.9-40】`K-9-9` 起算垂線約束之現況違反範圍實測")
    P("=" * W)
    P(f"  產生於 commit：{sha}")
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P("  🔴 ⛔ 禁硬編：甲乙判別與左右分界一律由量得之幾何決定")
    P("")

    # ── §0 量測器自檢（⛔ 先自檢後量測·測資刻意傾斜）────────────────────
    P("【0】量測器自檢（⛔ 傾斜測資·⛔ 非軸向矩形·附對照組實際輸出）")
    P("-" * W)
    TH = math.radians(17.0)                       # FRONTLINE 之傾角（⛔ 非軸向）
    d = (math.cos(TH), math.sin(TH))
    n = (-d[1], d[0])
    o = (0.0, 0.0)
    DEPTH = 40.0
    ob = (o[0] + DEPTH * n[0], o[1] + DEPTH * n[1])   # BASELINE 過此點、方向亦 d（平行）
    def front_pt(s):  return (o[0] + s * d[0], o[1] + s * d[1])
    def base_pt(s):   return (ob[0] + s * d[0], ob[1] + s * d[1])
    ok = {}
    # 甲：前一宗遠側界往「s 減少」方向傾（B_prev 之 s < P_prev 之 s）
    Pp, Bp = front_pt(10.0), base_pt(4.0)
    c1, st1, df1, cd1 = eval_lot(Pp, Bp, front_pt(20.0), base_pt(20.0), o, d, n)
    ok["甲"] = (c1 == "甲")
    P(f"  ① 已知【甲】(P_prev s=10, B_prev s=4)  ⇒ 判 {c1}"
      f"　起算(front s={st1[0]:.3f}, base s={st1[1]:.3f}) ⇒ {'✅' if ok['甲'] else '🔴'}")
    # 乙：前一宗遠側界往「s 增加」方向傾
    Pp2, Bp2 = front_pt(10.0), base_pt(16.0)
    c2, st2, df2, cd2 = eval_lot(Pp2, Bp2, front_pt(20.0), base_pt(20.0), o, d, n)
    ok["乙"] = (c2 == "乙")
    P(f"  ② 已知【乙】(P_prev s=10, B_prev s=16) ⇒ 判 {c2}"
      f"　起算(front s={st2[0]:.3f}, base s={st2[1]:.3f}) ⇒ {'✅' if ok['乙'] else '🔴'}")
    # 合格 / 不合格
    _, _, dfa, cda = eval_lot(Pp2, Bp2, front_pt(30.0), base_pt(30.0), o, d, n)
    _, _, dfb, cdb = eval_lot(Pp2, Bp2, front_pt(12.0), base_pt(12.0), o, d, n)
    ok["合格"] = (cda == "合格")
    ok["不合格"] = (cdb == "不合格")
    P(f"  ③ 已知【合格】(本宗 s=30·皆在起算之後) ⇒ {cda}"
      f"（差額 front {dfa[0]:+.3f} / base {dfa[1]:+.3f}）⇒ {'✅' if ok['合格'] else '🔴'}")
    P(f"  ④ 已知【不合格】(本宗 s=12·front 在 P⊥=16 之前) ⇒ {cdb}"
      f"（差額 front {dfb[0]:+.3f} / base {dfb[1]:+.3f}）⇒ {'✅' if ok['不合格'] else '🔴'}")
    P(f"  🔒 自檢測資之 FRONTLINE 傾角 = 17°（⛔ 非軸向）")
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
        CAP[key] = {"block": block_poly, "d_hat": np.asarray(d_hat, float),
                    "corner": np.asarray(corner_pt, float), "biz": list(_biz)}
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
                    ERR[lbl] = f"{type(e).__name__}: {str(e)[:110]}"
        finally:
            ns["_pool_strips_for_block"] = _orig

    FL = cad.get("front_lines") or {}
    BL = cad.get("baselines") or {}

    # ── §2 逐街廓逐側逐宗 ───────────────────────────────────────────
    P("")
    P("【C-2】逐街廓逐側逐宗（⛔ 母體 ＝ 全部街廓之兩側）")
    P("-" * W)
    STAT = {"甲": 0, "乙": 0, "退化(P⊥＝P_prev)": 0}
    BAD = []
    for lbl in BLKS:
        key = next((k for k in CAP if k[0] == lbl), None)
        if key is None:
            P(f"  {lbl}：⛔ 未攔到呼叫 ⇒ **無從量測**"
              f"{'（生產碼 raise：' + ERR[lbl] + '）' if lbl in ERR else ''}")
            continue
        biz = CAP[key]["biz"]
        d_hat = tuple(CAP[key]["d_hat"])
        nrm = (-d_hat[1], d_hat[0])
        fl = FL.get(lbl) or {}
        bl = BL.get(lbl) or {}
        if not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            P(f"  {lbl}：⛔ 缺 FRONTLINE 或 BASELINE ⇒ **無從量測**")
            continue
        o = tuple(float(x) for x in fl["p1"])
        bpt = tuple(float(x) for x in bl["point"])
        bang = math.radians(float(bl.get("angle_deg", 0.0)))
        bdir = (math.cos(bang), math.sin(bang))
        # 左右分界：合併投影區間（⛔ 由幾何決定·禁硬編）
        IV = []
        for g in biz:
            ss_ = [(x * d_hat[0] + y * d_hat[1]) for x, y in list(g.exterior.coords)]
            IV.append((min(ss_), max(ss_)))
        k_break = None
        for k in range(1, len(IV)):
            if min(v[0] for v in IV[k:]) > max(v[1] for v in IV[:k]) + 1e-6:
                k_break = k if k_break is None else -1
        groups = ([("左", list(range(0, k_break))), ("右", list(range(k_break, len(IV))))]
                  if isinstance(k_break, int) and k_break > 0
                  else [("單組(未測得唯一分界)", list(range(len(IV))))])
        P("")
        P(f"  ── {lbl}（{len(biz)} 宗·分界索引 ＝ {k_break}）"
          f"{'　⚠️ 生產碼 raise：' + ERR[lbl] if lbl in ERR else ''} ──")
        P(f"    {'側':<4}{'i':<4}{'情形':<6}{'P_prev s':>12}{'B_prev s':>12}"
          f"{'起算front':>12}{'起算base':>12}{'本宗P s':>12}{'本宗B s':>12}"
          f"{'Δfront':>11}{'Δbase':>11}  出艙碼")
        for side, idxs in groups:
            prev = None
            for i in idxs:
                u_far, p_far = far_side_dir_and_pt(biz[i], d_hat)
                if u_far is None:
                    P(f"    {side:<4}{i:<4}⛔ 取不出遠側界 ⇒ 無從判定")
                    continue
                Pc = line_isect(p_far, u_far, o, d_hat)
                Bc = line_isect(p_far, u_far, bpt, bdir)
                if Pc is None or Bc is None:
                    P(f"    {side:<4}{i:<4}⛔ 遠側界 ∥ FRONT 或 ∥ BASE ⇒ 無從判定")
                    prev = None
                    continue
                if prev is None:
                    P(f"    {side:<4}{i:<4}{'（起點·本則不適用）':<6}"
                      f"{'':>12}{'':>12}{'':>12}{'':>12}"
                      f"{s_of(Pc,o,d_hat):>12.3f}{s_of(Bc,o,d_hat):>12.3f}"
                      f"{'':>11}{'':>11}  —")
                    prev = (Pc, Bc)
                    continue
                case, st, df, code = eval_lot(prev[0], prev[1], Pc, Bc, o, d_hat, nrm)
                STAT[case] = STAT.get(case, 0) + 1
                if code == "不合格":
                    BAD.append((lbl, side, i, df, float(biz[i].area)))
                P(f"    {side:<4}{i:<4}{case:<6}"
                  f"{s_of(prev[0],o,d_hat):>12.3f}{s_of(prev[1],o,d_hat):>12.3f}"
                  f"{st[0]:>12.3f}{st[1]:>12.3f}"
                  f"{s_of(Pc,o,d_hat):>12.3f}{s_of(Bc,o,d_hat):>12.3f}"
                  f"{df[0]:>+11.3f}{df[1]:>+11.3f}  "
                  f"{'✅ 合格' if code=='合格' else '🔴 不合格'}")
                prev = (Pc, Bc)

    # ── §3 統計 ────────────────────────────────────────────────────
    P("")
    P("【C-3】統計（⛔ 逐宗可回溯·⛔ 計數非唯一證據）")
    P("-" * W)
    P(f"  情形分布：{STAT}")
    P(f"  不合格宗數 ＝ {len(BAD)}")
    if BAD:
        ar = [b[4] for b in BAD]
        P(f"  不合格宗之面積：帶號合計 {sum(ar):+.4f}　絕對值合計 {sum(abs(x) for x in ar):.4f}")
        P(f"  {'街廓':<6}{'側':<4}{'i':<4}{'Δfront':>12}{'Δbase':>12}{'面積':>12}")
        for (lbl, side, i, df, a) in BAD:
            P(f"  {lbl:<6}{side:<4}{i:<4}{df[0]:>+12.3f}{df[1]:>+12.3f}{a:>12.4f}")
    else:
        P("  🔒 **零計數之構造**（空集鐵律）：見自檢 ④——已知不合格之人造測資，"
          "本探針判為「不合格」（Δfront −4.000）⇒ 該計數**非恆 0**。")
    if ERR:
        P("")
        P("  ⚠️ 生產碼 raise 之街廓（⛔ 不影響 CAP·spy 於呼叫前已存）：")
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
    _log = os.path.join(OUTDIR, f"probe_WG940_startperp_{_sha}.log")
    with open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
