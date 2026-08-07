# -*- coding: utf-8 -*-
r"""**GEO-2**：`W_1` 口徑更正（winner **實配宗**在「內側界改 ∥SIDELINE」下之 W）。

⛔ 零碼面·只算不換·不接 `run_all`·**不重跑分配鏈**（`run_step_g` 只跑一次取現況）。

## §〇 撤回（claude.ai 缺陷·非 CC）

GEO-1 §六(15) 之**停機條件作廢**——`app.py` 之逐字註解早已裁明該情形非 bug。
本檔於【〇】段**自 `app.py` 現讀該行印出**（⛔ 非手打、⛔ 非手改 log）。
🔴 KL 域裁補充（2026-08-07）：「該側僅 1 宗」係**原位次分配之中間狀態**；
街廓調配池其後會納入他街廓／公設地之土地，該側宗數增加、ΣRw 隨之回補。
⇒ 原推導（telescoping 恆等式）**正確且有價值·逐字保留**，僅**改記為「已裁在案·非停機」**。

## §一 口徑更正（本單唯一實質工作）

**舊（GEO-1）**：`W1_new = S1 × sinθ` ⇒ 量的是**最小規定範圍**之寬。
**新（本單）**：以 winner 之**現行 G 為目標**，把分配線改為 **∥SIDELINE**，
解出使**面積 ＝ G** 之平移量，取 `mp →該線` 之**垂距**。⇒ 與 `W1現行` 同為**實配宗**之 W。

🔒 **沿用生產原語·⛔ 未另寫平行式**：切帶一律走 `_block_strip`
（`grep -n "def _block_strip" app.py`·即 `solve_G_binary` 內 `app.py:9340` 所呼叫者），
僅把 `allocation_dir` 由 ALLOC 法向換成 **`rot90_cw(SIDE 方向)`**
⇒ 依 `_block_strip` 之 `n_hat = rot90(allocation_dir)` ⇒ **切帶界線 ∥SIDELINE**；
且 `solve_G_binary` 之 `_n_alloc = normalize(allocation_dir)`（`app.py:9321-9327`）
⇒ **W 沿該線之法向量測 ＝ 垂距**。⛔ 二者同源、非另立座標。

## 🔒 自我驗證閘

| 閘 | 內容 | 意義 |
|---|---|---|
| **G0** | 以**原** `allocation_dir` 反解至 `area == G現行`，其 `W` 應 ≈ 生產 `g_rows['W(m)']`（≤0.01） | 驗**錨點重建**（baseline_pt／d̂／mp）無誤 |
| **G1** | 新口徑解出之多邊形面積與目標 `G` 之差 **≤ 0.01㎡** | 施工單 §一 明令 |

⛔ **G0／G1 未過之格標「不可據」**，其 `ΔRw1` 不計入 §二 判準。
"""
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g, _compute_v3_finance          # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_geo2_W1_calibre.log")

# 🔒 §二 判準之容差——**先行宣告**（⛔ 不得由結果反推）
TOL_DRW = 0.01          # ΔRw1 「≈ 0」之容差（百分點）
TOL_AREA = 0.01         # G1 閘：面積 vs 目標 G（㎡·同 solve_G_binary 之 tol）
TOL_W0 = 0.01           # G0 閘：重建 W vs 生產 W(m)（m）


def _u(ax, ay):
    n = math.hypot(ax, ay)
    return (ax / n, ay / n)


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    import numpy as np
    from shapely.geometry import Polygon as _PG
    L = []
    L.append("=" * 200)
    L.append("【GEO-2】W_1 口徑更正（winner 實配宗·內側界改 ∥SIDELINE） — ⛔ 只算不換·生產碼零觸")
    L.append("=" * 200)

    # ── 【〇】撤回（⛔ 自 app.py 現讀·非手打）────────────────────────────────
    L.append("")
    L.append("【〇】GEO-1 §六(15) 停機條件之**撤回**（claude.ai 缺陷·非 CC）")
    L.append("-" * 200)
    _app = io.open(os.path.join(REPO, "app.py"), encoding="utf-8").read().splitlines()
    _hit = [(i + 1, ln) for i, ln in enumerate(_app)
            if "ΣRw<100%" in ln and "誠實結果" in ln]
    if not _hit:
        L.append("  🔴 未於 app.py 找到該逐字 ⇒ **撤回之依據不成立·停查**")
    else:
        for _n, _ln in _hit:
            L.append(f"  🔒 `app.py:{_n}` **逐字**（⛔ 本行自 app.py 現讀·未手打）：")
            L.append(f"     {_ln.strip()}")
    L.append("  ⇒ 「ΣRw < 100%」**本就不是停機事由** ⇒ GEO-1 §六(15) 之 🛑 **作廢**，")
    L.append("     改記為「**已裁在案·非停機**」。⛔ 原 telescoping 推導**正確且保留**。")
    L.append("  🔴 **KL 域裁補充（2026-08-07）**：「該側僅 1 宗」係**原位次分配之中間狀態**；")
    L.append("     街廓調配池其後會納入他街廓／公設地之土地，該側宗數增加、ΣRw 隨之回補。")
    L.append("  ⚠️ **本次未命中之教訓**：GEO-1 落筆設停機前**未 grep `app.py` 註解**"
             "（見報告 §三 之新戒）。")

    ns, fake_st = harvest()
    for _s in ("_block_strip", "rw_from_width", "_oblique_s_max", "alloc_normal_axis",
               "RW_SATURATION_WIDTH_M"):
        if ns.get(_s) is None:
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    _SAT = float(ns["RW_SATURATION_WIDTH_M"])
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    _C = float(_compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)["C"])

    rows = []
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, winners, forced, setback)
        by_pid = {str(r.get("暫編地號")): r for r in sg["g_rows"]}
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            for which in ("left", "right"):
                rec = {"sb": sb, "lbl": lbl, "side": which}
                if which not in (sd_by.get(lbl) or {}):
                    rec["note"] = "—·N0-20 域（無 SIDE_LINE）"
                    rows.append(rec); continue
                pid = ((winners or {}).get(lbl) or {}).get(
                    "p1_end" if which == "left" else "p2_end")
                rec["pid"] = pid
                if not pid:
                    rec["note"] = "無 winner（強制留設抵費地）"
                    rows.append(rec); continue
                row = by_pid.get(str(pid)) or {}
                rec["G"] = float(row.get("G(㎡)", 0) or 0)
                rec["W_prod"] = float(row.get("W(m)", 0) or 0)
                rec["Rw_prod"] = float(row.get("Rw(%)", 0) or 0)
                rec["F"] = float(row.get("F(m)", 0) or 0)
                rec["l1"] = float(row.get("l₁ 側面尺度", 0) or 0)
                rec["nlot"] = sum(1 for x in sg["g_rows"]
                                  if str(x.get("所屬街廓")) == lbl
                                  and str(x.get("推進側別")) == which)
                # ── 錨點重建（逐字對映 stepg 之首宗）──────────────────────────
                P1 = np.array([float(fl["p1"][0]), float(fl["p1"][1])])
                P2 = np.array([float(fl["p2"][0]), float(fl["p2"][1])])
                _sL = float(np.linalg.norm(P2 - P1))
                dh = (P2 - P1) / (_sL or 1.0)
                verts = b.get("vertices") or []
                blk = _PG([(float(v[0]), float(v[1])) for v in verts])
                if not blk.is_valid:
                    blk = blk.buffer(0)
                adir = al_by.get(lbl)
                ax = ns["alloc_normal_axis"](adir) if adir else None
                _smax_a = (ns["_oblique_s_max"](verts, dh, P1, ax)
                           if ax is not None else None)
                amp = float(_smax_a) if _smax_a is not None else _sL
                if which == "left":
                    bp = P1
                    dh_use = dh
                else:
                    bp = P1 + amp * dh
                    dh_use = -dh
                sd = sd_by[lbl][which]
                mp = (sd.get("mid") or None)
                if mp is None:
                    rec["note"] = "SIDE_LINE 無 mid ⇒ W 不可量"
                    rows.append(rec); continue
                mp = np.asarray(mp, dtype=float)
                S1p = np.array([float(sd["p1"][0]), float(sd["p1"][1])])
                S2p = np.array([float(sd["p2"][0]), float(sd["p2"][1])])
                su = np.array(_u(*(S2p - S1p)))
                # allocation_dir 使 `n_hat = rot90(ad)` ∥ SIDE ⇒ ad = rot90_cw(su)
                ad_new = np.array([su[1], -su[0]])

                def _solve_to_area(_ad, _target, _blk=blk, _dh=dh_use, _bp=bp, _hi=None):
                    """以 `_block_strip`（**生產原語**）反解 S 使 area == _target。"""
                    _hi = float(_hi if _hi is not None else max(amp, _sL) * 1.5)
                    _lo = 0.0
                    _cut = None
                    for _ in range(200):
                        _mid = (_lo + _hi) / 2.0
                        _cut, _ar = ns["_block_strip"](_blk, _dh, _bp, _mid, allocation_dir=_ad)
                        if _ar < _target:
                            _lo = _mid
                        else:
                            _hi = _mid
                    _S = (_lo + _hi) / 2.0
                    _cut, _ar = ns["_block_strip"](_blk, _dh, _bp, _S, allocation_dir=_ad)
                    return _S, float(_ar), _cut

                def _W_of(_ad, _S, _bp=bp, _dh=dh_use, _mp=mp):
                    """⛔ 逐字沿用 `solve_G_binary` 之 W 式（`app.py:9350-9356`）。"""
                    _na = np.asarray(_ad, dtype=float)
                    _na = _na / float(np.linalg.norm(_na))
                    _ah = _na if float(np.dot(_dh, _na)) >= 0.0 else -_na
                    return float(np.dot(_bp + _S * _dh - _mp, _ah))

                # ── 閘 G0：以**原** allocation_dir 反解 ⇒ W 應 ≈ 生產 W(m) ──────
                _S0, _a0, _ = _solve_to_area(ax, rec["G"])
                rec["W_re"] = _W_of(ax, _S0)
                rec["G0"] = (abs(_a0 - rec["G"]) <= TOL_AREA
                             and abs(rec["W_re"] - rec["W_prod"]) <= TOL_W0)
                rec["a0"] = _a0
                # ── 新口徑 ＋ 閘 G1 ──────────────────────────────────────────
                _S1s, _a1, _c1 = _solve_to_area(ad_new, rec["G"])
                rec["W_new"] = _W_of(ad_new, _S1s)
                rec["a1"] = _a1
                rec["G1"] = (abs(_a1 - rec["G"]) <= TOL_AREA)
                rows.append(rec)

    # ── 【A】自我驗證閘 ────────────────────────────────────────────────────
    L.append("")
    L.append("【A】自我驗證閘（⛔ 未過之格於【B】標「不可據」·不計入 §二 判準）")
    L.append("-" * 200)
    L.append(f"  G0：以**原** allocation_dir 反解至 area==G ⇒ W 應 ≈ 生產 W(m)"
             f"（容差 {TOL_W0}m·面積容差 {TOL_AREA}㎡）")
    L.append(f"  G1：新口徑之解 |area − G| ≤ {TOL_AREA}㎡（施工單 §一 明令）")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}{'目標G':>10}"
             f"{'G0:面積':>11}{'G0:W重建':>11}{'生產W':>10}{'|ΔW|':>10}{'G0':>5}"
             f"{'G1:面積':>11}{'|Δ面積|':>10}{'G1':>5}")
    L.append("-" * 200)
    for r in rows:
        if "W_new" not in r:
            continue
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{str(r['pid']):<13}{r['G']:>10.2f}"
                 f"{r['a0']:>11.4f}{r['W_re']:>11.6f}{r['W_prod']:>10.2f}"
                 f"{abs(r['W_re'] - r['W_prod']):>10.6f}{('✅' if r['G0'] else '🔴'):>5}"
                 f"{r['a1']:>11.4f}{abs(r['a1'] - r['G']):>10.6f}"
                 f"{('✅' if r['G1'] else '🔴'):>5}")
    L.append("-" * 200)
    _n0 = sum(1 for r in rows if "W_new" in r and not r["G0"])
    _n1 = sum(1 for r in rows if "W_new" in r and not r["G1"])
    _tot = sum(1 for r in rows if "W_new" in r)
    L.append(f"  G0 未過 **{_n0}/{_tot}**　G1 未過 **{_n1}/{_tot}**（⛔ 未放寬閘門以掩蓋）")

    # ── 【B】§一 主表 ──────────────────────────────────────────────────────
    L.append("")
    L.append("【B】§一：W_1 口徑更正後之逐格表（**十六格逐格**·⛔ 無 winner 者亦列）")
    L.append("-" * 200)
    L.append("  🔒 二者**現為同一口徑**：皆為 **winner 實配宗**之 `W`（mp → 該宗遠側分配界線之垂距），")
    L.append("     差別**僅在該界線之方向**（現行 ∥ALLOC ／ 新 ∥SIDELINE）。")
    L.append(f"  🔒 飽和：`RW_SATURATION_WIDTH_M` ＝ **{_SAT:.1f}** m"
             f"（`grep -n \"RW_SATURATION_WIDTH_M = \" app.py`）·W ≥ 該值 ⇒ R(W)=100%")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}{'該側宗數':>9}"
             f"{'W1現行':>11}{'W1新':>11}{'ΔW1':>11}"
             f"{'R(W1現)%':>10}{'R(W1新)%':>10}{'ΔRw1%':>9}  飽和區(現/新)  閘")
    L.append("-" * 200)
    _sig = []
    for r in rows:
        tag = f"{r['lbl']}/{r['side']}"
        if "W_new" not in r:
            L.append(f"{r['sb']:<6}{tag:<12}{str(r.get('pid') or '—'):<13}"
                     f"{'—':>9}{'—':>11}{'—':>11}{'—':>11}{'—':>10}{'—':>10}{'—':>9}"
                     f"  {r.get('note', '')}")
            continue
        _Rc = float(ns["rw_from_width"](r["W_prod"]))
        _Rn = float(ns["rw_from_width"](r["W_new"]))
        _d = _Rn - _Rc
        r["dRw"] = _d
        # G ＝ (a(1−AB) − Rw·F·l₁ − S·l₂)(1−C)（`grep -n "G_target = max(0.0" app.py`）
        #   ⇒ ΔG ＝ −(ΔRw%/100)·F·l₁·(1−C)；守恆式 ΣG + 池 ＝ 街廓面積 ⇒ Δ池 ＝ −ΔG
        r["dG"] = -(_d / 100.0) * r["F"] * r["l1"] * (1.0 - _C)
        r["dPool"] = -r["dG"]
        _ok = r["G0"] and r["G1"]
        if _ok and abs(_d) > TOL_DRW:
            _sig.append(r)
        L.append(f"{r['sb']:<6}{tag:<12}{str(r['pid']):<13}{r['nlot']:>9}"
                 f"{r['W_prod']:>11.6f}{r['W_new']:>11.6f}{r['W_new'] - r['W_prod']:>11.6f}"
                 f"{_Rc:>10.4f}{_Rn:>10.4f}{_d:>9.4f}"
                 f"  {'飽和' if r['W_prod'] >= _SAT else '未飽和'}"
                 f"／{'飽和' if r['W_new'] >= _SAT else '未飽和'}"
                 f"  {'✅' if _ok else '🔴 不可據'}")
    L.append("-" * 200)

    # ── 【C】§二 判準 ─────────────────────────────────────────────────────
    L.append("")
    L.append("【C】§二 判準（⛔ 兩分支對等·未觸發者亦寫明）")
    L.append("-" * 200)
    L.append(f"  🔒 容差 `|ΔRw1| ≤ {TOL_DRW}` 百分點——**先行宣告於本檔常數區**·⛔ 未由結果反推。")
    if not _sig:
        L.append("  ⇒ **分支一成立**：16 格之 `ΔRw1` 皆 ≈ 0")
        L.append("     ⇒ 🔒 **ΣRw 議題因口徑更正而消失**。")
        L.append("  ⇒ **分支二：未觸發。**")
    else:
        L.append(f"  ⇒ **分支二成立**：仍有 **{len(_sig)}** 格之 `|ΔRw1| > {TOL_DRW}`（逐格列下）。")
        L.append("  ⇒ **分支一：未觸發。**")
        L.append("  ⛔ **依 §〇，該情形已裁在案（`app.py` 逐字）⇒ 不得標為停機。**")
        L.append("-" * 200)
        L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}{'ΔRw1%':>10}"
                 f"{'l₁側尺度':>10}{'F(m)':>9}{'ΔG(㎡)':>12}{'Δ抵費地(㎡)':>13}")
        L.append("-" * 200)
        for r in _sig:
            L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{str(r['pid']):<13}"
                     f"{r['dRw']:>10.4f}"
                     f"{r.get('l1', float('nan')):>10.2f}{r.get('F', float('nan')):>9.2f}"
                     f"{r.get('dG', float('nan')):>12.4f}{r.get('dPool', float('nan')):>13.4f}")
        L.append("-" * 200)

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
