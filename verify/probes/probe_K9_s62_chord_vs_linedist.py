# -*- coding: utf-8 -*-
r"""**S6-2 補丁一 §一-補**：街角規定範圍多邊形之**弦** vs **線距**（⛔ 只查不改）。

⛔ 零生產變更·不接 `run_all`·不設任何門檻。

## 本檔要判別什麼

`K-9-5-2` ③ 之「構造保證」＝ **線距**（二側**無限直線**間、沿前緣線方向之距離）
——`_build_corner_range_v3` 之自檢①（`grep -n "構造自檢不合" app.py`）逐格斷言
`min(w0, wD) == T`，不成立即 `_stop`。

而 `K-9-5` 之實量（`parcel_min_width_n14`）量的是**某個多邊形之弦**。

🔑 **判別（KL 補丁一 §一-補）**：對**街角規定範圍多邊形本身**（`rng`·⛔ **不是** winner 之虛擬塊）
量其**自身構造帶二端**之

  (a) **線距**  (b) **該多邊形之弦**  (c) 差、及**弦兩端點之邊界歸屬**

- 若 **(b) < T 而 (a) == T** ⇒ **與 winner 完全無關**：「構造保證」與「實量」是**兩個量**，
  `K-9-5-2` ⑤ 之推論**當場證偽** ⇒ ⛔ 不必再看 winner。
- 若 **(b) == (a) == T** ⇒ 假說**在規定範圍上不成立**，成因必在
  「規定範圍 → winner 虛擬塊」之間 ⇒ 回原單 §一 逐格追。

## 🔒 為何 `rng` 之弦可能 < 線距（依碼·非臆測）

`grep -n "rng = min(pieces" app.py` 起：`rng` ＝ **街廓多邊形**被 `L(t*)` 切後之街角側片，
**再 `difference(chamfer_tri)`**（`grep -n "rng = rng.difference(chamfer_tri)" app.py`）。
⇒ 其邊界為「FRONT／**截角後**側界／BASELINE／`L(t*)`」。
而**線距**量到的是 **SIDE_LINE 實體（截角前）之無限直線**
（`CLAUDE.md`：**兩套側界·禁混用**——量測用＝截角前；範圍邊界＝截角後）。
⇒ 二者**本就不是同一個量**。碼內已有一筆現成實測：
`grep -n "實測 R4 左 弦@d=0" app.py`（「弦@d=0 ＝1.36 vs 真寬 5.08」）。

## 量法（⛔ 單一真相源·未另寫第二份幾何）

- `rng` ← `app._build_corner_range_v3`（引數逐字沿用 `verify/run_verification.py` 之 `rng(which)`）
- 帶二端 ← `app.k97_solve_alloc_t` 之 `band_d_top`／`band_d_bot`（**生產所消費者**）
- 深度軸號規**逐字重現**碼面：`bn = (-buy, bux)`，再「定號：指向 BASELINE」
  （`grep -n "定號：指向 BASELINE" app.py`）
- **線距**：量測線 ∩ `SIDE_LINE` 無限直線、與 ∩ `L(t*)` 無限直線之 `d̂` 座標差。
  `L(t*)` 由 `rng` 上**平行 `alloc_dir` 且離側界最遠**之邊還原。
  🔒 **自我驗證**：若該還原正確，`min(線距@二端)` 應 **== `T`**（碼面自檢①之保證）
  ⇒ 本檔逐格印出該核對；不符即代表**本檔之還原有誤**，⛔ 不得據以下結論。

## 重跑

    python verify/probes/probe_K9_s62_chord_vs_linedist.py

輸出 `verify/out/probe_K9_s62_chord_vs_linedist.log`。rc 恆 0。
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_s62_chord_vs_linedist.log")
_LBIG = 1.0e5


def _u(ax, ay):
    n = math.hypot(ax, ay)
    return (ax / n, ay / n)


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    from shapely.geometry import LineString as _LS, Point as _PT
    L = []
    L.append("=" * 190)
    L.append("【S6-2 補丁一 §一-補】街角規定範圍多邊形 `rng` 之**弦** vs **線距**"
             "（⛔ 只查不改·不是 winner 之虛擬塊）")
    L.append("=" * 190)

    ns, fake_st = harvest()
    for _s in ("_build_corner_range_v3", "k97_solve_alloc_t", "_make_chamfer_tri_wb",
               "_baseline_pts_from_manual", "_compute_per_end_cutoff_areas"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    legal_w = float(snapshot["global"]["法定最小寬_m"])
    SB = snapshot["blocks"]
    slm = cad.get("side_lines_by_side", {}) or {}
    flm = cad.get("front_lines", {}) or {}
    alloc = cad.get("alloc_dir_by_block", {}) or {}
    bls = cad.get("baselines", {}) or {}

    rows = []
    for setback in (0.0, 3.5):
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            blk = SB.get(lbl) or {}
            fl = flm.get(lbl) or {}
            side_map = slm.get(lbl) or {}
            verts = b.get("vertices") or []
            if not (fl.get("p1") and fl.get("p2")) or not verts:
                continue
            _mb = bls.get(lbl) or {}
            _bpts = ns["_baseline_pts_from_manual"](_mb, verts)
            _q = (_mb.get("_match") or {}).get("q_detected")
            _fpts = [fl["p1"], fl["p2"]]
            au_raw = alloc.get(lbl)
            depth = float(blk.get("街廓分配深度_m") or 0.0)
            if not au_raw or depth <= 0:
                continue
            for which in ("left", "right"):
                if which not in side_map:
                    continue
                rec = {"sb": f"{setback:g}m", "lbl": lbl, "side": which,
                       "T": setback + legal_w}
                chi = ns["_make_chamfer_tri_wb"](b, which)
                _sp = [side_map[which]["p1"], side_map[which]["p2"]]
                _args = dict(block_vertices=verts, block_centroid=b.get("centroid"),
                             front_pts=_fpts, baseline_pts=_bpts, side_line_pts=_sp,
                             alloc_dir=au_raw, block_depth=depth, setback=setback,
                             min_width=legal_w, chamfer_tri=chi,
                             dxf_quantum=_q, _label=lbl, _side=which)
                try:
                    rng = ns["_build_corner_range_v3"](**_args)
                except RuntimeError as e:
                    rec["err"] = "rng：" + str(e).splitlines()[0][:90]
                    rows.append(rec); continue
                try:
                    _k = ns["k97_solve_alloc_t"](
                        b.get("centroid"), _fpts, _bpts, _sp, au_raw, setback,
                        legal_w, chamfer_tri=chi, block_depth=depth,
                        _label=lbl, _side=which, block_vertices=verts)
                except (RuntimeError, TypeError) as e:
                    rec["err"] = "k97：" + str(e).splitlines()[0][:90]
                    rows.append(rec); continue
                rec["t_star"] = _k.get("t_star")
                _dtop = float(_k.get("band_d_top", 0.0) or 0.0)
                _dbot = float(_k.get("band_d_bot", 0.0) or 0.0)
                rec["band"] = (_dtop, _dbot)

                # ── 座標軸：逐字重現碼面 ──────────────────────────────────────
                F1 = (float(_fpts[0][0]), float(_fpts[0][1]))
                F2 = (float(_fpts[1][0]), float(_fpts[1][1]))
                dxh, dyh = _u(F2[0] - F1[0], F2[1] - F1[1])
                B0 = (float(_bpts[0][0]), float(_bpts[0][1]))
                B1 = (float(_bpts[-1][0]), float(_bpts[-1][1]))
                bux, buy = _u(B1[0] - B0[0], B1[1] - B0[1])
                bnx, bny = -buy, bux
                if (B0[0] - F1[0]) * bnx + (B0[1] - F1[1]) * bny < 0:   # 定號：指向 BASELINE
                    bnx, bny = -bnx, -bny
                aux, auy = _u(float(au_raw[0]), float(au_raw[1]))

                # SIDE_LINE **實體（截角前）** 之無限直線
                S1 = (float(_sp[0][0]), float(_sp[0][1]))
                S2 = (float(_sp[1][0]), float(_sp[1][1]))
                sux, suy = _u(S2[0] - S1[0], S2[1] - S1[1])
                _Sinf = _LS([(S1[0] - sux * _LBIG, S1[1] - suy * _LBIG),
                             (S1[0] + sux * _LBIG, S1[1] + suy * _LBIG)])

                # `L(t*)` ← 自 `rng` 還原：平行 alloc_dir 且離側界最遠之邊
                _best, _bestd = None, -1.0
                _ring = list(rng.exterior.coords)
                for _i in range(len(_ring) - 1):
                    _a, _b2 = _ring[_i], _ring[_i + 1]
                    _ex, _ey = _b2[0] - _a[0], _b2[1] - _a[1]
                    _n = math.hypot(_ex, _ey)
                    if _n < 1e-9:
                        continue
                    if abs((_ex / _n) * auy - (_ey / _n) * aux) > 1e-7:
                        continue
                    _mid = _PT((_a[0] + _b2[0]) / 2.0, (_a[1] + _b2[1]) / 2.0)
                    _dd = _mid.distance(_Sinf)
                    if _dd > _bestd:
                        _best, _bestd = (_a, _b2), _dd
                if _best is None:
                    rec["err"] = "rng 上無平行 alloc_dir 之邊 ⇒ L(t*) 不可還原"
                    rows.append(rec); continue
                _Lt = _LS([(_best[0][0] - aux * _LBIG, _best[0][1] - auy * _LBIG),
                           (_best[0][0] + aux * _LBIG, _best[0][1] + auy * _LBIG)])

                def _s_of(pt):
                    return (pt[0] - F1[0]) * dxh + (pt[1] - F1[1]) * dyh

                _res = []
                for _d in (_dtop, _dbot):
                    _P = (F1[0] + _d * bnx, F1[1] + _d * bny)
                    _line = _LS([(_P[0] - dxh * _LBIG, _P[1] - dyh * _LBIG),
                                 (_P[0] + dxh * _LBIG, _P[1] + dyh * _LBIG)])
                    # (a) 線距
                    _i1, _i2 = _line.intersection(_Sinf), _line.intersection(_Lt)
                    _ld = (abs(_s_of((_i2.x, _i2.y)) - _s_of((_i1.x, _i1.y)))
                           if (not _i1.is_empty and not _i2.is_empty
                               and _i1.geom_type == 'Point' and _i2.geom_type == 'Point')
                           else float('nan'))
                    # (b) 弦（該多邊形之實體交集）
                    _cl = _line.intersection(rng)
                    if _cl.is_empty:
                        _ch, _nseg, _ends = 0.0, 0, []
                    elif _cl.geom_type == 'LineString':
                        _ch, _nseg = _cl.length, 1
                        _ends = [_cl.coords[0], _cl.coords[-1]]
                    else:
                        _gs = [g for g in getattr(_cl, 'geoms', []) if g.length > 0]
                        _ch = sum(g.length for g in _gs)
                        _nseg = len(_gs)
                        _ends = ([_gs[0].coords[0], _gs[-1].coords[-1]] if _gs else [])
                    # (c) 弦兩端點之邊界歸屬
                    _own = []
                    for _e in _ends:
                        _p = _PT(_e)
                        _cand = [("SIDE(截角前)", _p.distance(_Sinf)),
                                 ("L(t*)", _p.distance(_Lt))]
                        if chi is not None and not chi.is_empty:
                            _cand.append(("截角邊", _p.distance(chi.boundary)))
                        _cand.append(("街廓邊界", _p.distance(
                            rng.exterior)))     # 恆為 0（端點在 rng 邊界上）·僅作對照
                        _pick = sorted([c for c in _cand if c[0] != "街廓邊界"],
                                       key=lambda x: x[1])
                        # 🔒 三線皆不在容差內 ⇒ 標「其他」，⛔ 不得逕取最近者充數
                        _own.append(f"{_pick[0][0]}({_pick[0][1]:.4f})"
                                    if _pick[0][1] <= 1e-6
                                    else f"其他/街廓·BASELINE(近 {_pick[0][0]} {_pick[0][1]:.4f})")
                    _res.append((_d, _ld, _ch, _nseg, _own))
                rec["res"] = _res
                # ── §三-補：**d = 0 專測**（＝ FRONT_LINE 上）──────────────────
                _P0 = (F1[0], F1[1])
                _l0 = _LS([(_P0[0] - dxh * _LBIG, _P0[1] - dyh * _LBIG),
                           (_P0[0] + dxh * _LBIG, _P0[1] + dyh * _LBIG)])
                _j1, _j2 = _l0.intersection(_Sinf), _l0.intersection(_Lt)
                _ld0 = (abs(_s_of((_j2.x, _j2.y)) - _s_of((_j1.x, _j1.y)))
                        if (_j1.geom_type == 'Point' and _j2.geom_type == 'Point')
                        else float('nan'))
                _c0 = _l0.intersection(rng)
                _ch0 = (0.0 if _c0.is_empty else
                        (_c0.length if _c0.geom_type == 'LineString'
                         else sum(g.length for g in getattr(_c0, 'geoms', []))))
                rec["d0"] = (_ld0, _ch0)
                rows.append(rec)

    # ── 【A】逐格：帶二端之 (a)線距／(b)弦／(c)歸屬 ────────────────────────────
    L.append("")
    L.append("【A】`rng` 於**其自身構造帶二端**之 (a)線距／(b)弦（⛔ 全精度·逐格）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'T':>7}{'帶端 d':>12}"
             f"{'(a)線距':>13}{'(b)弦':>13}{'(a)−(b)':>13}{'弦段數':>7}  (c) 弦兩端點之邊界歸屬")
    L.append("-" * 190)
    _viol, _okcell, _errc = [], 0, 0
    for r in rows:
        _tag = f"{r['lbl']}/{r['side']}"
        if "err" in r:
            _errc += 1
            L.append(f"{r['sb']:<6}{_tag:<12}{r['T']:>7.2f}  🔴 {r['err']}")
            continue
        _okcell += 1
        for _d, _ld, _ch, _ns, _own in r["res"]:
            _gap = _ld - _ch
            L.append(f"{r['sb']:<6}{_tag:<12}{r['T']:>7.2f}{_d:>12.6f}"
                     f"{_ld:>13.6f}{_ch:>13.6f}{_gap:>13.6f}{_ns:>7}  "
                     + "｜".join(_own))
            if _ch < r['T'] - 1e-9:
                _viol.append((r['sb'], _tag, _d, _ld, _ch, r['T']))
    L.append("-" * 190)

    # ── 【B】自我驗證：min(線距@二端) 是否 == T ────────────────────────────────
    L.append("")
    L.append("【B】🔒 **本檔之自我驗證**：`min(線距@帶二端)` 應 **== `T`**"
             "（碼面自檢①之保證·`grep -n \"構造自檢不合\" app.py`）")
    L.append("-" * 190)
    _bad = []
    for r in rows:
        if "res" not in r:
            continue
        _m = min(x[1] for x in r["res"])
        _ok = abs(_m - r["T"]) < 1e-6
        if not _ok:
            _bad.append((r["sb"], f"{r['lbl']}/{r['side']}", _m, r["T"]))
        L.append(f"  {r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}"
                 f"min(線距) ＝ {_m:.9f}　T ＝ {r['T']:.2f}　{'✅' if _ok else '🔴'}")
    L.append("-" * 190)
    if _bad:
        L.append(f"  🔴 **{len(_bad)} 格不符 ⇒ 本檔對 `L(t*)` 之還原有誤**，"
                 f"⛔ **不得據【A】下任何結論**：{_bad}")
    else:
        L.append("  ✅ **全格相符** ⇒ 本檔之 `L(t*)` 還原正確、(a) 欄可信。")

    # ── 【C】判別結論（⛔ 只述觀測）──────────────────────────────────────────
    L.append("")
    L.append("【C】§一-補 之判別（⛔ 只述觀測·不作裁定）")
    L.append("-" * 190)
    L.append(f"  受檢格：{_okcell}（另 {_errc} 格取不到 `rng`／`k97`）")
    L.append(f"  **(b) 弦 < T 之帶端**：**{len(_viol)}** 處")
    for v in _viol:
        L.append(f"      {v[0]:<6}{v[1]:<12}d＝{v[2]:.6f}　線距 {v[3]:.6f}"
                 f"　**弦 {v[4]:.6f}** < T {v[5]:.2f}")
    if _viol and not _bad:
        L.append("  ⇒ 🔴 **(b) < T 而 (a) == T** ⇒ 「構造保證」與「實量」**是兩個量**；")
        L.append("     `K-9-5-2` ⑤「面積夠 ⇒ 寬度自動合格」之推論**於規定範圍上即已證偽**，")
        L.append("     **與 winner 無關** ⇒ ⛔ 不必再看 winner 之虛擬塊。")
    elif not _viol:
        L.append("  ⇒ **(b) == (a) == T** ⇒ 假說**於規定範圍上不成立**；")
        L.append("     成因必在「規定範圍 → winner 虛擬塊」之間 ⇒ 回原單 §一 逐格追。")

    # ── 【C-2】§三-補：`d = 0`（FRONT_LINE 上）之弦 vs 線距 ────────────────────
    L.append("")
    L.append("【C-2】§三-補：**`d = 0`**（＝ FRONT_LINE 上）之 (a)線距／(b)弦"
             "——碼內既有註記之複現靶（`grep -n \"實測 R4 左 弦@d=0\" app.py`）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'(a)線距@d=0':>15}{'(b)弦@d=0':>15}{'(a)−(b)':>13}")
    L.append("-" * 190)
    for r in rows:
        if "d0" not in r:
            continue
        _a0, _b0 = r["d0"]
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}"
                 f"{_a0:>15.6f}{_b0:>15.6f}{_a0 - _b0:>13.6f}")
    L.append("-" * 190)
    L.append("  🎯 **靶**：碼內註記載「實測 R4 左 弦@d=0 ＝1.36 vs 真寬 5.08」"
             "（`app.py` 之自檢①′ 上方）⇒ 對讀本表 `0m R4/left` 一列。")

    L.append("")
    L.append("【D】註記")
    L.append("  · ⛔ 零生產變更：未動 `app.py`、未動 `verify/` 既有檔、不接 `run_all`。")
    L.append("  · `rng` 與帶二端**皆取自生產真符號**（`_build_corner_range_v3`／`k97_solve_alloc_t`）；")
    L.append("    本檔自算者僅「量測線之求交」與「`L(t*)` 之還原」，後者由【B】把關。")
    L.append("  · **兩套側界**（`CLAUDE.md`）：線距量到 **SIDE_LINE 實體（截角前）**；"
             "`rng` 之邊界為**截角後**（其構造末段 `rng.difference(chamfer_tri)`）。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
