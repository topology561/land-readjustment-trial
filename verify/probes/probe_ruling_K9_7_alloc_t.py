# -*- coding: utf-8 -*-
"""K-9-7 解析定位 — **舊 vs 新 `t*` 對照·只算不換**（K-6-A2 段三(a)）。

## 定位

段三分三步，**(b) 為強制停機點**：

- **(a)（本檔）** 並行實作、**不接生產路徑** ⇒ 只算不換。
- **(b)** 位移表攤給 KL ⇒ **等 KL 點頭**。
- **(c)** 切換（待放行）。

## 兩個求解器

| | 符號 | 帶深 | 斜率 |
|---|---|---|---|
| **舊（生產中）** | `app._build_corner_range_v3` 內之閉式 | **街廓平均深度** `round(D_avg,2)`（常數） | `c` |
| **新（本批）** | `app.k97_solve_alloc_t` | **範圍自身之最小深度** `D(t)`（隨 `t` 變動） | 分支 ①`c`／②`c`／③`(c − k·m)` |

⇒ 差異即 **GB-14** 所登記者（`grep -n "GB-14" docs/reports/W-G.4_泛用阻塞項登記表.md`）。

## 記號警語

⚠️ `app._build_corner_range_v3` 之區域變數 `k = sigma / den_a` **係正典之 `c`**，
非正典之 `k`（`∂w/∂d`）——正典 K-9-7-a 衝突一。
⚠️ `P_front`（`ALLOC_LINE ∩ 前緣線`·K-9-7）與 `P_block`（`L_in ∩ BLOCK 邊界`·K-9-8）
**同名異物**——K-9-7-a 衝突二。本檔一律用全名。

## 重跑

    python verify/probes/probe_ruling_K9_7_alloc_t.py

**rc 恆 0**（只算不換·不作為閘）。輸出 `verify/out/probe_ruling_K9_7_alloc_t.log`。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_ruling_K9_7_alloc_t.log")

# 正典 K-9-7-c 表（`grep -n "^#### K-9-7-c " docs/rulings/K-6_…md`）——**獨立真相源**
CANON = {
    ("R1", "left"):  {"c": -1.003270, "k": 0.000000, "m": None, "br": "①"},
    ("R1", "right"): {"c": +1.003270, "k": 0.000000, "m": -0.000000, "br": "①"},
    ("R2", "left"):  {"c": +1.002499, "k": -0.075547, "m": +0.009750, "br": "③"},
    ("R3", "right"): {"c": +1.004284, "k": 0.000000, "m": None, "br": "①"},
    ("R4", "left"):  {"c": +1.001034, "k": -0.047599, "m": +0.000266, "br": "③"},
    ("R4", "right"): {"c": -1.001034, "k": -0.050087, "m": 0.000000, "br": "②"},
    ("R5", "left"):  {"c": +1.004284, "k": -0.075610, "m": -0.000000, "br": "②"},
    ("R6", "right"): {"c": -1.003245, "k": 0.000000, "m": 0.000000, "br": "①"},
}


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 126)
    L.append("【K-9-7 解析定位】舊 vs 新 t* 對照 — **只算不換·未接生產路徑**（K-6-A2 段三(a)）")
    L.append("舊＝_build_corner_range_v3（帶深＝街廓平均深度·斜率 c）")
    L.append("新＝k97_solve_alloc_t（帶深＝範圍自身最小深度 D(t)·斜率 ①c／②c／③(c−k·m)）")
    L.append("=" * 126)

    ns, fake_st = harvest()
    for _s in ("k97_solve_alloc_t", "_build_corner_range_v3", "_make_chamfer_tri_wb"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    rows = []
    for setback in (0.0, 3.5):
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            for side in ("left", "right"):
                if side not in (sd_by.get(lbl) or {}):
                    continue
                fl = fl_by.get(lbl) or {}
                if not (fl.get("p1") and fl.get("p2")):
                    continue
                _fp = [fl["p1"], fl["p2"]]
                _bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
                _sp = [sd_by[lbl][side]["p1"], sd_by[lbl][side]["p2"]]
                _chi = ns["_make_chamfer_tri_wb"](b, side)
                _depth = float(snapshot["blocks"][lbl]["街廓分配深度_m"])
                _q = ((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected")
                # 新求解器（帶 block_depth ⇒ 同框回算舊式 t*）
                try:
                    new = ns["k97_solve_alloc_t"](
                        b.get("centroid"), _fp, _bp, _sp, al_by.get(lbl),
                        setback, legal_w, chamfer_tri=_chi,
                        block_depth=_depth, _label=lbl, _side=side)
                    nerr = None
                except RuntimeError as e:
                    new, nerr = None, str(e)
                # 面積對照：**同一條多邊形構造路徑**（`_build_corner_range_v3`），
                #   只換 t —— 生產 t*（不傳 override）vs 新 t*（傳 override）
                a_old = a_new = None
                try:
                    _r_old = ns["_build_corner_range_v3"](
                        b.get("vertices"), b.get("centroid"), _fp, _bp, _sp,
                        al_by.get(lbl), _depth, setback, legal_w, _chi,
                        dxf_quantum=_q, _label=lbl, _side=side)
                    a_old = float(_r_old.area) if _r_old is not None else None
                except RuntimeError as e:
                    nerr = (nerr or "") + f"｜舊式 raise：{e}"
                if new is not None:
                    try:
                        _r_new = ns["_build_corner_range_v3"](
                            b.get("vertices"), b.get("centroid"), _fp, _bp, _sp,
                            al_by.get(lbl), _depth, setback, legal_w, _chi,
                            dxf_quantum=_q, _label=lbl, _side=side,
                            _t_override=new["t_star"])
                        a_new = float(_r_new.area) if _r_new is not None else None
                    except RuntimeError as e:
                        nerr = (nerr or "") + f"｜新 t* 構造 raise：{e}"
                rows.append({"sb": setback, "lbl": lbl, "side": side,
                             "new": new, "nerr": nerr,
                             "a_old": a_old, "a_new": a_new})

    # ── 【A】係數對拍：新求解器 vs 正典 K-9-7-c 表 ──────────────────────────
    L.append("")
    L.append("【A】係數對拍：新求解器算出之 c／k／m／分支 vs **正典 K-9-7-c 表**（獨立真相源）")
    L.append("-" * 126)
    L.append(f"{'街廓/側':<12}{'c(新)':>12}{'c(正典)':>12}{'k(新)':>12}{'k(正典)':>12}"
             f"{'m(新)':>12}{'m(正典)':>12}{'支(新)':>7}{'支(典)':>7}  對拍")
    L.append("-" * 126)
    _mis = []
    for r in [x for x in rows if x["sb"] == 0.0]:
        key = (r["lbl"], r["side"])
        cn = CANON.get(key)
        if cn is None or r["new"] is None:
            L.append(f"{r['lbl']+'/'+r['side']:<12}"
                     + (f"  🔴 新求解器 raise：{(r['nerr'] or '')[:70]}" if r["new"] is None
                        else "  （正典表無此格）"))
            continue
        n = r["new"]
        _dc = abs(n["c"] - cn["c"])
        _dk = abs(n["k"] - cn["k"])
        _dm = (abs(n["m"] - cn["m"]) if cn["m"] is not None else None)
        _okb = (n["branch"] == cn["br"])
        _ok = (_dc < 5e-5) and (_dk < 5e-5) and (_dm is None or _dm < 5e-5) and _okb
        if not _ok:
            _mis.append((key, n, cn))
        L.append(f"{r['lbl']+'/'+r['side']:<12}{n['c']:>12.6f}{cn['c']:>12.6f}"
                 f"{n['k']:>12.6f}{cn['k']:>12.6f}{n['m']:>12.6f}"
                 f"{(f'{cn[chr(109)]:.6f}' if cn['m'] is not None else '（非線性）'):>12}"
                 f"{n['branch']:>7}{cn['br']:>7}  {'✅' if _ok else '🔴'}")
    L.append("-" * 126)
    L.append(f"  ⇒ 不符者 {len(_mis)} 格" + ("（**須停機上呈**）" if _mis else "（逐格相符 ✅）"))

    # ── 【B】舊 vs 新 t* 位移 ────────────────────────────────────────────────
    L.append("")
    L.append("【B】舊 vs 新 `t*` 位移（**§三(b) 攤給 KL 之主表**）")
    L.append("-" * 126)
    L.append(f"{'情境':<6}{'街廓/側':<10}{'支':>3}{'t*(舊)':>12}{'t*(新)':>12}"
             f"{'Δt*(cm)':>10}{'面積舊(㎡)':>12}{'面積新(㎡)':>12}{'Δ面積(㎡)':>11}"
             f"{'切換點':>8} 斷言")
    L.append("-" * 126)
    _moved = []
    for r in rows:
        tag = f"{r['sb']:g}m"
        if r["new"] is None:
            L.append(f"{tag:<6}{r['lbl']+'/'+r['side']:<10}  🔴 新求解器 raise（見【C】）")
            continue
        n = r["new"]
        _dt_cm = (n["dt"] * 100.0) if n["dt"] is not None else None
        _da = ((r["a_new"] - r["a_old"])
               if (r["a_new"] is not None and r["a_old"] is not None) else None)
        if _dt_cm is not None and abs(_dt_cm) > 1e-6:
            _moved.append((tag, r["lbl"], r["side"], _dt_cm, _da))
        L.append(f"{tag:<6}{r['lbl']+'/'+r['side']:<10}{n['branch']:>3}"
                 f"{(n['t_star_legacy'] if n['t_star_legacy'] is not None else float('nan')):>12.5f}"
                 f"{n['t_star']:>12.5f}"
                 f"{(_dt_cm if _dt_cm is not None else float('nan')):>10.3f}"
                 f"{(r['a_old'] if r['a_old'] is not None else float('nan')):>12.3f}"
                 f"{(r['a_new'] if r['a_new'] is not None else float('nan')):>12.3f}"
                 f"{(_da if _da is not None else float('nan')):>11.3f}"
                 f"{(','.join(f'{s:g}' for s in n['switch_points']) or '—'):>8}"
                 f" {'✅' if n['W_at_t_star'] >= n['T'] - 1e-6 else '🔴'}")
    L.append("-" * 126)
    L.append(f"  ⇒ `t*` 有位移之格：**{len(_moved)}** / {len([r for r in rows if r['new']])}")
    if _moved:
        L.append("     " + "；".join(
            f"{t} {l}/{s} {d:+.3f}cm"
            + (f"／面積 {a:+.3f}㎡" if a is not None else "")
            for t, l, s, d, a in _moved))

    # ── 【C】新求解器 raise 之格 ────────────────────────────────────────────
    _err = [r for r in rows if r["new"] is None]
    L.append("")
    L.append(f"【C】新求解器 raise 之格：{len(_err)}")
    for r in _err:
        L.append(f"  {r['sb']:g}m {r['lbl']}/{r['side']}：{(r['nerr'] or '')[:200]}")

    # ── 【D】P_front 落截角旗標 ─────────────────────────────────────────────
    L.append("")
    L.append("【D】`P_front(t*)` 落截角三角形內之格（K-9-7-d 第二層分支·需 K-9-8）")
    _ch = [r for r in rows if r["new"] and r["new"]["P_front_on_chamfer"]]
    if _ch:
        for r in _ch:
            L.append(f"  {r['sb']:g}m {r['lbl']}/{r['side']}：t*={r['new']['t_star']:.6f}")
    else:
        L.append("  （無）")
    L.append("")
    L.append("【E】註記")
    L.append("  · 本檔**只算不換**：`k97_solve_alloc_t` 未接生產路徑（零呼叫點）。")
    L.append("  · K-9-7-d 之第二層分支（`P_block` 落截角邊 vs FRONT 重疊段）需 K-9-8 之 "
             "`PQ` 延伸線段（**段四**）⇒ 本批不臆造。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
