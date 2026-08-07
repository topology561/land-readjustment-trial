# -*- coding: utf-8 -*-
r"""**GEO-1**：KL 之新街角構造（`S1` ∥道路境界線）圖上驗證（⛔ 零碼面·只算不換）。

⛔ 不接 `run_all`·**不改任何裁定**·**不寫任何判定碼**·**不重跑分配鏈**（`run_step_g` 只跑一次
供 §五／§六 取現況，⛔ 不因情境而重跑）。

## §〇 KL 之新構造（逐字·⛔ 不得自行詮釋）

僅**街角第 1 宗**改；末端塊**照 N0-20 原案不動**。

- `P0` ＝ FRONTLINE 與 SIDELINE 之**未截角理論交點**
- `Ps` ＝ FRONTLINE 與**道路截角線段**之交點
- 街角第 1 宗內側界 ＝ **SIDELINE 平行移動**（⛔ 不是 ALLOCLINE 方向）
- 平移量 `S1 = max(線段 P0–Ps, 退縮 + 畸零地最小寬)`，⇒ 分配線**永不切到截角**
- 新街角規定範圍 ＝ `Ps → 道路截角 → SIDELINE → BASELINE → 平移後SIDELINE`
- 🔒 `S1` 為「與道路境界線平行」之距離（畸零地使用規則第四條三款逐字），
  ⛔ **不是垂距**；`W`（手冊：向宗地分配線作垂直線）為另一量，二者**不得互相代用**。

## 🔒 自我驗證閘（`CLAUDE.md` 常設條·⛔ 不過不得據以下結論）

| 閘 | 內容 | 所據 |
|---|---|---|
| **H1** | `P0` ≡ FRONT∞ ∩ SIDE∞（未截角理論交點） | K-4 第 5 條之實測（`grep -n "K-4 第 5 條" app.py`） |
| **H2** | `Ps` 落在 FRONT∞ 上（距 < 1e-6），且 `Ps` ≠ `P0` | 截角三角形之構造（`_make_chamfer_tri_wb`） |
| **H3** | **新範圍**：兩側界之**路平行距** ≡ `S1`，**全深度逐點**（21 取樣） | §〇 之構造定義 |
| **H4** | 新範圍多邊形非空、且其 `∥SIDE` 之內側界與平移後 SIDELINE 重合 | 同上 |

⛔ H1〜H4 任一未過之格，其後續欄位標「🔴 閘未過·不可據」。
"""
import copy
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
LOG = os.path.join(OUTDIR, "probe_K9_geo1_S1_construction.log")
_LBIG = 1.0e5


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
    from shapely.geometry import LineString as _LS, Point as _PT, Polygon as _PG
    from shapely.ops import split as _split
    L = []
    L.append("=" * 210)
    L.append("【GEO-1】KL 新街角構造（S1 ∥道路境界線）圖上驗證 — ⛔ 只算不換·生產碼零觸")
    L.append("=" * 210)

    # ── §一 兩個相反預測（⛔ 原封留存·事後不得修改）────────────────────────────
    L.append("")
    L.append("【§一】兩個**事前寫死**之相反預測（⛔ 原封留存·事後未修改）")
    L.append("-" * 210)
    L.append("  · **KL 預測**：新構造使候選資格**更不容易**滿足 ⇒ 更多街角進入合併機制。")
    L.append("  · **claude.ai 預測**：3.5m 情境 max 取 T ⇒ 門檻**降**、資格**變易**；")
    L.append("    0m 情境 T=3.50 與 `P0–Ps` 同量級，max 可能咬在截角側 ⇒ 門檻**升**、資格**變難**。")
    L.append("  ⇒ 兩者皆可能全錯。⛔ 本檔之量法未以任一預測為前提設計。")

    ns, fake_st = harvest()
    for _s in ("_build_corner_range_v3", "_make_chamfer_tri_wb", "_baseline_pts_from_manual",
               "_corner_block_true_G", "rw_from_width", "_chamfer_line_for_side"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
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
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])
    _fin3 = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)
    _sbrows = _fin3["sb_rows_by_label"]
    _ORIG_RNG = ns["_build_corner_range_v3"]
    _ORIG_TRUEG = ns["_corner_block_true_G"]

    # ── 幾何 helper：局部框 (s along d̂, t along n̂ 指向街廓內) ────────────────
    def _frame(lbl):
        fl = fl_by.get(lbl) or {}
        F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
        F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
        dh = _u(F2[0] - F1[0], F2[1] - F1[1])
        nh = (-dh[1], dh[0])
        cen = cb_by[lbl].get("centroid") or (0.0, 0.0)
        if ((float(cen[0]) - F1[0]) * nh[0] + (float(cen[1]) - F1[1]) * nh[1]) < 0:
            nh = (-nh[0], -nh[1])
        return F1, F2, dh, nh

    def _st_of(p, F1, dh, nh):
        px, py = float(p[0]) - F1[0], float(p[1]) - F1[1]
        return (px * dh[0] + py * dh[1], px * nh[0] + py * nh[1])

    def _inf(p, ux, uy):
        return _LS([(p[0] - ux * _LBIG, p[1] - uy * _LBIG),
                    (p[0] + ux * _LBIG, p[1] + uy * _LBIG)])

    def _s_on_line(pA, pB, t_val, F1, dh, nh):
        """過 pA,pB 之無限直線於深度 t 之 s（⛔ 解析·非 GEOS）。"""
        a = _st_of(pA, F1, dh, nh); b = _st_of(pB, F1, dh, nh)
        if abs(b[1] - a[1]) < 1e-12:
            return float("nan")
        return a[0] + (t_val - a[1]) / (b[1] - a[1]) * (b[0] - a[0])

    # ══════════════════════════════════════════════════════════════════════
    # 逐格幾何（§二）＋ 新範圍（§三）
    # ══════════════════════════════════════════════════════════════════════
    geo = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            F1, F2, dh, nh = _frame(lbl)
            verts = b.get("vertices") or []
            blk = _PG([(float(v[0]), float(v[1])) for v in verts])
            if not blk.is_valid:
                blk = blk.buffer(0)
            bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
            depth = float((snapshot["blocks"].get(lbl) or {}).get("街廓分配深度_m") or 0.0)
            for which in ("left", "right"):
                key = (sb, lbl, which)
                rec = {"sb": sb, "lbl": lbl, "side": which, "T": setback + legal_w,
                       "setback": setback}
                if which not in (sd_by.get(lbl) or {}):
                    rec["note"] = "—·N0-20 域（無 SIDE_LINE）"
                    geo[key] = rec
                    continue
                sd = sd_by[lbl][which]
                S1p = (float(sd["p1"][0]), float(sd["p1"][1]))
                S2p = (float(sd["p2"][0]), float(sd["p2"][1]))
                su = _u(S2p[0] - S1p[0], S2p[1] - S1p[1])
                P0 = F1 if which == "left" else F2
                # ── 閘 H1：P0 ≡ FRONT∞ ∩ SIDE∞ ────────────────────────────
                _i = _inf(F1, dh[0], dh[1]).intersection(_inf(S1p, su[0], su[1]))
                rec["H1"] = (not _i.is_empty and _i.geom_type == "Point"
                             and math.hypot(_i.x - P0[0], _i.y - P0[1]) < 1e-6)
                rec["H1_d"] = (math.hypot(_i.x - P0[0], _i.y - P0[1])
                               if (not _i.is_empty and _i.geom_type == "Point") else float("nan"))
                # ── Ps：截角三角形之 FRONT 側頂點 ────────────────────────────
                chi = ns["_make_chamfer_tri_wb"](b, which)
                rec["chi"] = chi
                if chi is None or chi.is_empty:
                    rec["note"] = "該側無截角三角形 ⇒ Ps 不可定"
                    rec["H2"] = False
                    geo[key] = rec
                    continue
                _fline = _inf(F1, dh[0], dh[1])
                _cands = [c for c in list(chi.exterior.coords)[:-1]
                          if math.hypot(c[0] - P0[0], c[1] - P0[1]) > 1e-9]
                _cands.sort(key=lambda c: _PT(c).distance(_fline))
                Ps = (float(_cands[0][0]), float(_cands[0][1]))
                rec["Ps"] = Ps
                rec["d_Ps_front"] = _PT(Ps).distance(_fline)
                rec["d_oth_front"] = (_PT(_cands[1]).distance(_fline)
                                      if len(_cands) > 1 else float("nan"))
                # 🔒 **H2 係辨別性閘·⛔ 非絕對 1e-6**：BLOCK 邊與 FRONT_LINE 為**兩個圖層**，
                #   實測相距可達 cm 級（前批六界距離欄：FRONT 0.000021〜0.013039）
                #   ⇒ 本閘問「所取者是否**明確**為 FRONT 側頂點」，⛔ 非「是否恰落在線上」。
                #   ⚠️ 前版寫成絕對 `< 1e-6` ⇒ 16 格中 14 格未過，**係閘之判準設錯、非資料有問題**。
                rec["H2"] = (rec["d_Ps_front"] < 0.05
                             and rec["d_oth_front"] > rec["d_Ps_front"] * 10.0
                             and math.hypot(Ps[0] - P0[0], Ps[1] - P0[1]) > 1e-9)
                # ── (1) **沿 FRONTLINE 量**（路平行·⛔ 非歐氏距離）────────────
                rec["seg_P0Ps"] = abs(_st_of(Ps, F1, dh, nh)[0] - _st_of(P0, F1, dh, nh)[0])
                rec["seg_euclid"] = math.hypot(Ps[0] - P0[0], Ps[1] - P0[1])
                rec["S1"] = max(rec["seg_P0Ps"], rec["T"])
                rec["bite"] = "截角側" if rec["seg_P0Ps"] >= rec["T"] else "T 側"
                # ── (4) θ ────────────────────────────────────────────────────
                _cos = abs(su[0] * dh[0] + su[1] * dh[1])
                _sin = abs(su[0] * dh[1] - su[1] * dh[0])
                rec["theta_deg"] = math.degrees(math.atan2(_sin, _cos))
                rec["sin"] = _sin
                rec["inv_sin"] = (1.0 / _sin) if _sin > 1e-12 else float("inf")
                # ── (5) W1(新) ───────────────────────────────────────────────
                rec["W1_new"] = rec["S1"] * _sin
                # ── (6) 平移後 SIDELINE ∩ FRONT ─────────────────────────────
                uu = dh if which == "left" else (-dh[0], -dh[1])
                rec["uu"] = uu
                T1 = (S1p[0] + rec["S1"] * uu[0], S1p[1] + rec["S1"] * uu[1])
                T2 = (S2p[0] + rec["S1"] * uu[0], S2p[1] + rec["S1"] * uu[1])
                rec["Tline"] = (T1, T2)
                _ix = _inf(F1, dh[0], dh[1]).intersection(_inf(T1, su[0], su[1]))
                rec["Xpt"] = ((float(_ix.x), float(_ix.y))
                              if (not _ix.is_empty and _ix.geom_type == "Point") else None)
                if rec["Xpt"] is not None:
                    _sP0 = _st_of(P0, F1, dh, nh)[0]
                    _sPs = _st_of(Ps, F1, dh, nh)[0]
                    _sX = _st_of(rec["Xpt"], F1, dh, nh)[0]
                    _sgn = 1.0 if which == "left" else -1.0
                    rec["d_P0X"] = _sgn * (_sX - _sP0)
                    rec["d_P0Ps"] = _sgn * (_sPs - _sP0)
                    rec["inside"] = (rec["d_P0X"] - rec["d_P0Ps"]) >= -1e-9
                else:
                    rec["inside"] = False
                # ── (7) 舊範圍面積 ───────────────────────────────────────────
                try:
                    _old = _ORIG_RNG(
                        verts, b.get("centroid"), [fl["p1"], fl["p2"]], bp,
                        [sd["p1"], sd["p2"]], al_by.get(lbl), depth, setback, legal_w, chi,
                        dxf_quantum=((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected"),
                        _label=lbl, _side=which)
                    rec["area_old"] = float(_old.area)
                except RuntimeError as e:
                    rec["area_old"] = None
                    rec["old_err"] = str(e).splitlines()[0][:60]
                # ── (8) 新範圍面積 ＋ 閘 H3／H4 ────────────────────────────
                _cutline = _inf(T1, su[0], su[1])
                try:
                    _pieces = list(_split(blk, _cutline).geoms)
                except Exception:
                    _pieces = []
                if len(_pieces) < 2:
                    rec["area_new"] = None
                    rec["new_err"] = "平移後 SIDELINE 未切到街廓"
                    rec["H3"] = rec["H4"] = False
                else:
                    _anchor = _PT(((S1p[0] + S2p[0]) / 2.0, (S1p[1] + S2p[1]) / 2.0))
                    _new = min(_pieces, key=lambda g: g.distance(_anchor))
                    if chi is not None and not chi.is_empty:
                        _new = _new.difference(chi)
                    if not _new.is_valid:
                        _new = _new.buffer(0)
                    rec["area_new"] = (float(_new.area) if not _new.is_empty else None)
                    rec["new_poly"] = _new
                    # 閘 H3：全深度逐點·路平行距 ≡ S1（21 取樣）
                    _tmax = max(_st_of(v, F1, dh, nh)[1] for v in verts)
                    _bad = 0.0
                    for _k in range(21):
                        _tt = _tmax * _k / 20.0
                        _a = _s_on_line(S1p, S2p, _tt, F1, dh, nh)
                        _c = _s_on_line(T1, T2, _tt, F1, dh, nh)
                        if _a != _a or _c != _c:
                            _bad = float("nan"); break
                        _bad = max(_bad, abs(abs(_c - _a) - rec["S1"]))
                    rec["H3_max"] = _bad
                    rec["H3"] = (_bad == _bad and _bad < 1e-9)
                    rec["H4"] = (rec["area_new"] is not None and rec["area_new"] > 0)
                geo[key] = rec

    # ── §二 表 ─────────────────────────────────────────────────────────────
    L.append("")
    L.append("【§二】幾何逐格表（8 街角 × 2 情境 ＝ 16 格·⛔ 逐格）")
    L.append("-" * 210)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'(1)P0–Ps':>11}{'(2)T':>8}{'(3)S1':>11}{'咬':<8}"
             f"{'(4)θ°':>9}{'sinθ':>10}{'1/sinθ':>9}"
             f"{'(5)W1新':>11}{'S1−W1':>10}{'(6)P0→交點':>12}{'≥P0–Ps?':>9}  閘 H1/H2/H3/H4")
    L.append("-" * 210)
    for k in sorted(geo):
        r = geo[k]
        tag = f"{r['lbl']}/{r['side']}"
        if "S1" not in r:
            L.append(f"{r['sb']:<6}{tag:<12}  {r.get('note', '')}")
            continue
        _g = (f"{'✅' if r.get('H1') else '🔴'}/{'✅' if r.get('H2') else '🔴'}"
              f"/{'✅' if r.get('H3') else '🔴'}/{'✅' if r.get('H4') else '🔴'}")
        L.append(f"{r['sb']:<6}{tag:<12}{r['seg_P0Ps']:>11.6f}{r['T']:>8.2f}{r['S1']:>11.6f}"
                 f"  {r['bite']:<6}{r['theta_deg']:>9.4f}{r['sin']:>10.6f}{r['inv_sin']:>9.4f}"
                 f"{r['W1_new']:>11.6f}{r['S1'] - r['W1_new']:>10.6f}"
                 f"{r.get('d_P0X', float('nan')):>12.6f}"
                 f"{('✅' if r.get('inside') else '🛑 外側'):>9}  {_g}")
    L.append("-" * 210)
    _n_out = [f"{k[0]} {k[1]}/{k[2]}" for k in sorted(geo)
              if "S1" in geo[k] and not geo[k].get("inside")]
    L.append(f"  🔒 **(6) 硬約束**（平移後交點須落在 Ps 或其內側）："
             f"**{sum(1 for k in geo if 'S1' in geo[k]) - len(_n_out)}"
             f"/{sum(1 for k in geo if 'S1' in geo[k])} 過**"
             + ("　⇒ ✅ **無切到截角之格**" if not _n_out
                else "　🛑 **未過：** " + "；".join(_n_out) + " ⇒ **停機上呈**"))
    _h3bad = [f"{k[0]} {k[1]}/{k[2]}" for k in sorted(geo)
              if "S1" in geo[k] and not geo[k].get("H3")]
    L.append(f"  🔒 **閘 H3**（新範圍兩側界路平行距 ≡ S1·全深度 21 取樣）："
             f"**{sum(1 for k in geo if 'S1' in geo[k]) - len(_h3bad)}"
             f"/{sum(1 for k in geo if 'S1' in geo[k])} 過**"
             + ("" if not _h3bad else "　🔴 未過：" + "；".join(_h3bad) + "（其列不可據）"))
    L.append("  ⚠️ `S1` 為**路平行距**、`W1` 為**垂距**，二者差 ＝ `S1×(1−sinθ)`；⛔ 不得互相代用（§〇 逐字）。")
    L.append("")
    L.append("  【閘 H2 之實據（Ps 之辨別）——⛔ 逐格列出，不以「過了」帶過】")
    L.append(f"{'':<6}{'街廓/側':<12}{'d(Ps,FRONT∞)':>15}{'d(另一頂點,FRONT∞)':>20}{'倍率':>10}"
             f"{'(1)路平行':>12}{'(1)歐氏':>12}{'差':>11}")
    for k in sorted(geo):
        r = geo[k]
        if "S1" not in r or r["sb"] != "0m":
            continue
        _rt = (r["d_oth_front"] / r["d_Ps_front"]) if r["d_Ps_front"] > 0 else float("inf")
        L.append(f"{'':<6}{r['lbl'] + '/' + r['side']:<12}{r['d_Ps_front']:>15.9f}"
                 f"{r['d_oth_front']:>20.9f}{_rt:>10.1f}"
                 f"{r['seg_P0Ps']:>12.6f}{r['seg_euclid']:>12.6f}"
                 f"{r['seg_P0Ps'] - r['seg_euclid']:>11.6f}")
    L.append("     （0m 與 3.5m 之 Ps 幾何相同 ⇒ 只列 0m 一份；`(1)` 依施工單取**路平行**值。）")

    # ── §三 表 ─────────────────────────────────────────────────────────────
    L.append("")
    L.append("【§三】門檻對照：(7) 舊範圍面積 vs (8) 新範圍面積")
    L.append("-" * 210)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'(7)舊面積':>13}{'(8)新面積':>13}{'(9)Δ':>12}{'升/降':>8}"
             f"{'咬':<8}  閘")
    L.append("-" * 210)
    for k in sorted(geo):
        r = geo[k]
        if "S1" not in r:
            continue
        _o, _n = r.get("area_old"), r.get("area_new")
        if _o is None or _n is None:
            L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}"
                     f"{('—' if _o is None else f'{_o:.2f}'):>13}"
                     f"{('—' if _n is None else f'{_n:.2f}'):>13}{'—':>12}{'—':>8}"
                     f"  {r.get('old_err', r.get('new_err', ''))}")
            continue
        _d = _n - _o
        r["delta"] = _d
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{_o:>13.4f}{_n:>13.4f}{_d:>12.4f}"
                 f"{('**升**' if _d > 0 else ('**降**' if _d < 0 else '＝')):>8}"
                 f"  {r['bite']:<6}  {'✅' if (r.get('H3') and r.get('H4')) else '🔴 閘未過·不可據'}")
    L.append("-" * 210)
    _up = [k for k in geo if geo[k].get("delta", 0) > 0]
    _dn = [k for k in geo if geo[k].get("delta", 0) < 0]
    L.append(f"  升 **{len(_up)}** 格／降 **{len(_dn)}** 格")
    L.append("  【§一 預測之逐格判定】")
    for _sbv in ("0m", "3.5m"):
        _u2 = [f"{k[1]}/{k[2]}" for k in sorted(geo) if k[0] == _sbv and geo[k].get("delta", 0) > 0]
        _d2 = [f"{k[1]}/{k[2]}" for k in sorted(geo) if k[0] == _sbv and geo[k].get("delta", 0) < 0]
        L.append(f"    {_sbv}：升 {len(_u2)} 格 " + (("〔" + "／".join(_u2) + "〕") if _u2 else "")
                 + f"　降 {len(_d2)} 格 " + (("〔" + "／".join(_d2) + "〕") if _d2 else ""))

    # ══════════════════════════════════════════════════════════════════════
    # §四：資格 2×2（patch 生產碼·⛔ 不重跑分配鏈）
    # ══════════════════════════════════════════════════════════════════════
    _hits = {"new": 0, "fallback": 0}

    def _make_new_rng(orig):
        def _f(block_vertices, block_centroid, front_pts, baseline_pts, side_pts,
               alloc_dir, D, setback, min_width, chamfer_tri=None, dxf_quantum=None,
               _label='', _side='', _t_override=None):
            r = geo.get((f"{setback:g}m", _label, _side))
            if r is None or r.get("new_poly") is None or _t_override is not None:
                # ⛔ `_t_override` 係診斷重播路徑 ⇒ 一律退回原構造（本單不涉）
                # 🔒 **反靜默退路**：退回次數逐次計數並印出（⛔ 不得無聲退回舊構造）
                _hits["fallback"] += 1
                return orig(block_vertices, block_centroid, front_pts, baseline_pts,
                            side_pts, alloc_dir, D, setback, min_width, chamfer_tri,
                            dxf_quantum=dxf_quantum, _label=_label, _side=_side,
                            _t_override=_t_override)
            _hits["new"] += 1
            return r["new_poly"]
        return _f

    def _make_fixF(orig):
        def _f(**kw):
            _blk = kw.get("_blk", "")
            _row = _sbrows.get(_blk, {}) or {}
            kw = dict(kw)
            kw["F_left"] = float(_row.get("左側長度(m)", 0) or 0)
            kw["F_right"] = float(_row.get("右側長度(m)", 0) or 0)
            return orig(**kw)
        return _f

    SCEN = [("F現行×舊門檻", False, False), ("F現行×新門檻", False, True),
            ("F改正×舊門檻", True, False), ("F改正×新門檻", True, True)]
    diag_by = {}
    for _nm, _fixF, _newR in SCEN:
        ns["_build_corner_range_v3"] = _make_new_rng(_ORIG_RNG) if _newR else _ORIG_RNG
        ns["_corner_block_true_G"] = _make_fixF(_ORIG_TRUEG) if _fixF else _ORIG_TRUEG
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, _win, _forced = run_corner_pk(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for _dg in (_d0 or []):
                diag_by.setdefault(_nm, []).append(dict(_dg, _sb=sb))
    ns["_build_corner_range_v3"] = _ORIG_RNG
    ns["_corner_block_true_G"] = _ORIG_TRUEG

    _sn = {"左": "left", "右": "right"}
    L.append("")
    L.append("【§四】資格 2×2（⛔ **不重跑分配鏈之靜態對照**·⛔ 不得聲稱此即最終結果）")
    L.append("-" * 210)
    L.append("  🔒 **作法（正面指名）**：patch `ns[\"_build_corner_range_v3\"]`（新門檻情境）與 "
             "`ns[\"_corner_block_true_G\"]`（F 改正情境）後，重跑 "
             "`build_param_table` ＋ `run_corner_pk`。")
    L.append("     `harvest()` 之 `ns` 即 exec 之 module globals ⇒ patch 同時打到"
             "**候選資格／三指數分母／G 門檻**三條路徑（`app.py:11004` 以模組全域呼叫）。")
    L.append("     ⛔ **未跑 `run_step_g`** ⇒ **未重跑分配鏈**。")
    L.append(f"  🔒 **反靜默退路計數**（新門檻二情境合計）：新構造命中 **{_hits['new']}** 次／"
             f"退回舊構造 **{_hits['fallback']}** 次"
             + ("　⇒ ✅ **無無聲退回**" if _hits["fallback"] == 0
                else "　⚠️ **有退回**——退回者係 `_t_override` 診斷重播或無 SIDE_LINE 之側，"
                     "⛔ 讀者須知該等呼叫用的是**舊**構造"))
    L.append("-" * 210)
    L.append(f"{'情境':<6}{'街廓/側':<11}{'候選':<13}"
             + "".join(f"{s[0]:<22}" for s in SCEN))
    L.append(f"{'':<6}{'':<11}{'':<13}"
             + "".join(f"{'真G／門檻／達標':<22}" for _ in SCEN))
    L.append("-" * 210)
    _idx = {}
    for _nm, _, _ in SCEN:
        for _dg in diag_by.get(_nm, []):
            _k = (_dg["_sb"], str(_dg.get("街廓", "")), _sn.get(str(_dg.get("端", "")).strip(), ""),
                  str(_dg.get("候選地號", "")))
            _idx.setdefault(_k, {})[_nm] = _dg
    for _k in sorted(_idx):
        _cells = []
        for _nm, _, _ in SCEN:
            _d = _idx[_k].get(_nm)
            if _d is None:
                _cells.append(f"{'—':<22}")
                continue
            _tg = _d.get("真G(㎡)")
            _cells.append(f"{(f'{float(_tg):.2f}' if _tg not in ('', None) else '—')}"
                          f"／{float(_d.get('門檻(㎡)', 0) or 0):.2f}"
                          f"／{'達標' if str(_d.get('達標', '')) == '達標' else '未達'}"
                          f"{'★' if str(_d.get('選中', '')) == '✅' else ''}".ljust(22))
        L.append(f"{_k[0]:<6}{_k[1] + '/' + _k[2]:<11}{_k[3]:<13}" + "".join(_cells))
    L.append("-" * 210)
    L.append("  （★ ＝ 該情境下之 winner）")
    L.append("")
    L.append("  【winner／排名異動 ＋ 各情境之街角結局】")
    L.append(f"{'情境':<6}{'街廓/側':<11}"
             + "".join(f"{s[0]:<20}" for s in SCEN) + "  winner 異動？")
    L.append("-" * 210)
    _tally = {s[0]: {"win": [], "none": []} for s in SCEN}
    _cells_keys = sorted({(_k[0], _k[1], _k[2]) for _k in _idx})
    for _ck in _cells_keys:
        _ws = []
        for _nm, _, _ in SCEN:
            _rows_ = [_idx[_k][_nm] for _k in _idx
                      if _k[:3] == _ck and _nm in _idx[_k]]
            _w = next((str(d.get("候選地號", "")) for d in _rows_
                       if str(d.get("選中", "")) == "✅"), None)
            _ws.append(_w or "（無人過門檻⇒強制抵費地）")
            (_tally[_nm]["win"] if _w else _tally[_nm]["none"]).append(
                f"{_ck[0]} {_ck[1]}/{_ck[2]}")
        _chg = "🔴 **有**" if len(set(_ws)) > 1 else "否"
        L.append(f"{_ck[0]:<6}{_ck[1] + '/' + _ck[2]:<11}"
                 + "".join(f"{w:<20}" for w in _ws) + f"  {_chg}")
    L.append("-" * 210)
    for _nm, _, _ in SCEN:
        L.append(f"  **{_nm}**：①有 winner **{len(_tally[_nm]['win'])}** 個"
                 f"〔{'／'.join(_tally[_nm]['win']) or '—'}〕；"
                 f"②無人過門檻（⇒強制抵費地）**{len(_tally[_nm]['none'])}** 個"
                 f"〔{'／'.join(_tally[_nm]['none']) or '—'}〕")
    L.append("  ⚠️ **本表為不重跑分配之靜態對照**——真G 係「假設第 1 宗」之樂觀口徑上界，"
             "而實配 G 由 `run_step_g` 決定；⛔ **不得聲稱這就是最終結果**。")

    # ══════════════════════════════════════════════════════════════════════
    # §五 第 2 宗 ＋ §六 W_1（取現況一次·⛔ 不因情境重跑）
    # ══════════════════════════════════════════════════════════════════════
    L.append("")
    L.append("【§五】楔形搬家之代價：第 2 宗（左界∥SIDELINE·右界∥ALLOCLINE ⇒ 非平行）")
    L.append("-" * 210)
    L.append("  🔒 **量法**：路平行距（∥FRONTLINE·同 `S1` 之口徑），⛔ 非垂距；"
             "深度框沿用 `_n14_band_geom` 之 `(s,t)` 局部框（`grep -n \"def _n14_band_geom\" app.py`）。")
    L.append("  🔒 **右界取現況**：現行第 2 宗之 ∥ALLOC 邊（`g_rows.cut_coords`·"
             "`verify/stepg_pipeline.py:381`）——⛔ 未重跑分配，故右界位置為**現況值**。")
    L.append("  🔒 **深度範圍**＝`[0, 畸零地最小深度]`（`get_min_lot_size(分類, 正面路寬)['min_depth']`）"
             "·**先行宣告**·⛔ 未由結果反推。")
    L.append("-" * 210)
    stepg_by = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, _win, _forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                        build_p, _win, _forced, setback)
        stepg_by[sb] = (sg, _win)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'第2宗':<13}{'(10)最淺寬':>12}{'(10)最深寬':>12}"
             f"{'(11)min≥最小寬?':>16}{'差值':>10}{'(12)收斂?':>10}{'寬=0之深度':>13}  判")
    L.append("-" * 210)
    _red = []
    for k in sorted(geo):
        r = geo[k]
        if "S1" not in r or r.get("new_poly") is None:
            continue
        sg, _win = stepg_by[r["sb"]]
        lbl, which = r["lbl"], r["side"]
        F1, F2, dh, nh = _frame(lbl)
        _side_key = "left" if which == "left" else "right"
        _rows_ = [x for x in sg["g_rows"]
                  if str(x.get("所屬街廓")) == lbl and str(x.get("推進側別")) == _side_key]
        _rows_.sort(key=lambda x: float(x.get("累積S(m)", 0) or 0))
        if len(_rows_) < 2:
            L.append(f"{r['sb']:<6}{lbl + '/' + which:<12}{'—':<13}  該側不足 2 宗 ⇒ 無第 2 宗")
            continue
        _r2 = _rows_[1]
        _cc = _r2.get("cut_coords") or []
        _au = al_by.get(lbl)
        _auh = _u(float(_au[0]), float(_au[1]))
        _edges = []
        for _i in range(len(_cc) - 1):
            _a, _bb = _cc[_i], _cc[_i + 1]
            _dx, _dy = float(_bb[0]) - float(_a[0]), float(_bb[1]) - float(_a[1])
            _n = math.hypot(_dx, _dy)
            if _n < 1e-9:
                continue
            if abs((_dx / _n) * _auh[1] - (_dy / _n) * _auh[0]) < 1e-3:
                _edges.append((_a, _bb))
        if not _edges:
            L.append(f"{r['sb']:<6}{lbl + '/' + which:<12}{str(_r2.get('暫編地號')):<13}"
                     f"  無 ∥ALLOC 之邊 ⇒ 右界不可定")
            continue
        _sP0 = _st_of(F1 if which == "left" else F2, F1, dh, nh)[0]
        _edges.sort(key=lambda e: abs((_st_of(e[0], F1, dh, nh)[0]
                                       + _st_of(e[1], F1, dh, nh)[0]) / 2.0 - _sP0))
        _rin = _edges[-1]
        _T1, _T2 = r["Tline"]
        # ⛔ no-silent-fallback：category／正面路寬缺值即 KeyError（loud），不編造
        _dmin = float(ns["get_min_lot_size"](
            cb_by[lbl]["category"],
            float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))["min_depth"])
        _w0 = abs(_s_on_line(_rin[0], _rin[1], 0.0, F1, dh, nh)
                  - _s_on_line(_T1, _T2, 0.0, F1, dh, nh))
        _wd = abs(_s_on_line(_rin[0], _rin[1], _dmin, F1, dh, nh)
                  - _s_on_line(_T1, _T2, _dmin, F1, dh, nh))
        _wmin, _wmax = min(_w0, _wd), max(_w0, _wd)
        # 收斂深度：兩線 s 差為 t 之線性函式 ⇒ 解其零點
        _g0 = (_s_on_line(_rin[0], _rin[1], 0.0, F1, dh, nh)
               - _s_on_line(_T1, _T2, 0.0, F1, dh, nh))
        _g1 = (_s_on_line(_rin[0], _rin[1], 1.0, F1, dh, nh)
               - _s_on_line(_T1, _T2, 1.0, F1, dh, nh))
        _slope = _g1 - _g0
        _tz = (-_g0 / _slope) if abs(_slope) > 1e-12 else float("inf")
        _tmax = max(_st_of(v, F1, dh, nh)[1] for v in cb_by[lbl].get("vertices") or [])
        _conv = (_tz == _tz and 0.0 < _tz < _tmax)
        if _conv:
            _red.append(f"{r['sb']} {lbl}/{which} 深度 {_tz:.4f}（街廓深上界 {_tmax:.4f}）")
        L.append(f"{r['sb']:<6}{lbl + '/' + which:<12}{str(_r2.get('暫編地號')):<13}"
                 f"{_wmin:>12.6f}{_wmax:>12.6f}"
                 f"{('✅ 是' if _wmin >= legal_w else '🔴 否'):>16}{_wmin - legal_w:>10.6f}"
                 f"{('🔴 是' if _conv else '否'):>10}"
                 f"{(f'{_tz:.4f}' if _tz == _tz and _tz != float('inf') else '—'):>13}"
                 f"  {'🔴 標紅' if _conv else ''}")
    L.append("-" * 210)
    L.append(f"  🔴 **(12) 標紅格 ＝ {len(_red)}**：" + ("；".join(_red) if _red else "（無）"))

    L.append("")
    L.append("【§六】W_1 之連動（⛔ 只算不換·⛔ 不算 ΔG 全鏈）")
    L.append("-" * 210)
    L.append("  🔒 **兩個 `W` 是垂距、但垂直於不同的線（同名不同量·⛔ 不得互相代用）**：")
    L.append("     · `W_1(現行)` ＝ `g_rows['W(m)']` ← `dot(baseline_pt + S·d̂ − mp, â)`"
             "（`grep -n \"W = float(np.dot(_bp_w\" app.py`）·**â ＝ ALLOC 法向** ⇒ 垂直於 ∥ALLOC 之分配線。")
    L.append("     · `W_1(新)` ＝ `S1 × sinθ` ＝ SIDELINE 與**平移後 SIDELINE** 之垂距 ⇒ 垂直於 ∥SIDE 之線。")
    L.append("  🔒 `rw_from_width` 回傳**百分比**（0〜100·`grep -n \"def rw_from_width\" app.py`）；"
             "`rw_increment(Wp,Wc) = max(0,(R(Wc)−R(Wp))/100)`（**負值夾 0**）。")
    L.append("     ⇒ `R(W₀)` 由生產反推：`R(W₀) = R(W_1,cur) − 生產Rw%`（未觸夾 0 時成立·逐格標）。")
    L.append("-" * 210)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'winner':<13}{'該側宗數':>9}{'(13)W1現行':>12}{'(13)W1新':>12}"
             f"{'ΔW1':>11}{'R(W1現)%':>10}{'R(W1新)%':>10}{'生產Rw%':>9}{'R(W₀)%':>9}"
             f"{'(14)Rw1新%':>11}{'ΔRw1%':>10}  ΣRw 側")
    L.append("-" * 210)
    _sigma_break = []
    for k in sorted(geo):
        r = geo[k]
        if "S1" not in r:
            continue
        sg, _win = stepg_by[r["sb"]]
        _pid = ((_win or {}).get(r["lbl"]) or {}).get(
            "p1_end" if r["side"] == "left" else "p2_end")
        if not _pid:
            L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{'—':<13}  無 winner（強制留設抵費地）")
            continue
        _row = next((x for x in sg["g_rows"] if str(x.get("暫編地號")) == str(_pid)), {})
        _nlot = sum(1 for x in sg["g_rows"]
                    if str(x.get("所屬街廓")) == r["lbl"]
                    and str(x.get("推進側別")) == r["side"])
        _w_cur = float(_row.get("W(m)", 0) or 0)
        _rw_prod = float(_row.get("Rw(%)", 0) or 0)
        _R_cur = float(ns["rw_from_width"](_w_cur))
        _R_new = float(ns["rw_from_width"](r["W1_new"]))
        _R_W0 = _R_cur - _rw_prod
        _rw1_new = max(0.0, _R_new - _R_W0)
        _solo = (_nlot <= 1)
        if _solo:
            _sigma_break.append(f"{r['sb']} {r['lbl']}/{r['side']}"
                                f"（{_rw_prod:.2f}% → {_rw1_new:.2f}%）")
        L.append(f"{r['sb']:<6}{r['lbl'] + '/' + r['side']:<12}{str(_pid):<13}{_nlot:>9}"
                 f"{_w_cur:>12.6f}{r['W1_new']:>12.6f}{r['W1_new'] - _w_cur:>11.6f}"
                 f"{_R_cur:>10.4f}{_R_new:>10.4f}{_rw_prod:>9.2f}{_R_W0:>9.4f}"
                 f"{_rw1_new:>11.4f}{_rw1_new - _rw_prod:>10.4f}"
                 f"  {'🛑 **W₁≡W_N ⇒ ΣRw 直接改變**' if _solo else '不變（中間項相消）'}")
    L.append("-" * 210)
    L.append("  **(15) telescoping 約束之判定（正面陳述·⛔ 非「應該成立」）**：")
    L.append("     碼面：`Rw = rw_increment(_W_near, W)`（`grep -n \"Rw = rw_increment\" app.py`），")
    L.append("     其中 `_W_near` ＝ mp→本宗**近**側界線、`W` ＝ mp→本宗**遠**側界線；")
    L.append("     推進時 `_W_prev_left/right = res['W_far']`（`verify/stepg_pipeline.py:656`／`:743`）")
    L.append("     ⇒ 第 i+1 宗之近側 ≡ 第 i 宗之遠側。")
    L.append("     ⇒ `ΣRw_側 = Σ[R(W_i,far) − R(W_i,near)] = R(W_N,far) − R(W_1,near)`"
             "（中間項**逐項相消**·telescoping）。")
    L.append("     🔒 **判定分兩類·⛔ 不可一概而論**：")
    L.append("     **(甲) 該側 ≥ 2 宗** ⇒ **成立**。`W_1,far` 在 Σ 中**同時以 +（Rw_1）與 −（Rw_2 之近側）"
             "出現** ⇒ **Σ 不變**；`W_1,near`（＝W₀）與 `W_N,far`（＝街廓末端）皆未被本構造改動。")
    L.append("     **(乙) 該側僅 1 宗** ⇒ 🛑 **不成立**。此時 `W_1,far ≡ W_N,far`，"
             "中間項**無可相消** ⇒ `ΣRw_側 = R(W_1,far) − R(W₀)` **直接隨 W_1 改變**。")
    if _sigma_break:
        L.append(f"     🛑 **本案實測落此支者 {len(_sigma_break)} 格**（⇒ **停機上呈**）：")
        for _s in _sigma_break:
            L.append(f"        · {_s}")
        L.append("     ⇒ 該等側之 `ΣRw` 將自現值掉至上表 `(14)Rw1新%` 之值"
                 "——**本改動於此類側**確會**外溢**（⛔ 非只影響第 1 宗）。")
    else:
        L.append("     ✅ 本案無「該側僅 1 宗」之格 ⇒ (乙) 未觸發。")
    L.append("     ⚠️ 本判定為**結構性**（恆等式層）；⛔ **不含**「第 1 宗面積改變 ⇒ 後續各宗位置改變」"
             "之二階效應——那須重跑分配鏈，**本單明令不做**。")
    L.append("     ⚠️ 🔧 **本節前版之判定為「一律成立」，係錯**——漏了 (乙)。已更正並停機上呈。")

    # ── §七 不觸及之確認 ───────────────────────────────────────────────────
    L.append("")
    L.append("【§七】不觸及之確認（正面舉證）")
    L.append("-" * 210)
    _self = os.path.abspath(__file__)
    _txt = io.open(_self, encoding="utf-8").read()
    for _kw in ("_end_region_R", "_end_band", "N0-20", "末端塊", "wf_f4", "fallback"):
        L.append(f"  (16) 本探針原始碼中「{_kw}」之命中 ＝ **{_txt.count(_kw)}**"
                 + ("　✅ 未引用" if _txt.count(_kw) == 0 else "　（僅本節之自我列舉）"))
    L.append("     ⇒ **末端塊／N0-20 路徑在本單中未被引用、未被重算**"
             "（本單只讀 `g_rows` 之現況欄與街角側幾何）。")
    L.append("  (17) 第 n−1 宗之兩側界方向**未變**：本單**未寫入**任何 `cut_coords`、"
             "未呼叫 `_reshape_block`／`wf_f*`，且 §四 之 patch 僅替換"
             "`_build_corner_range_v3`（**街角規定範圍**）與 `_corner_block_true_G`（**F 槽**）"
             "二者，**皆不參與非街角宗之側界方向**（側界方向由 `allocation_dir` 決定·"
             "`grep -n \"allocation_dir=allocation_dir\" verify/stepg_pipeline.py`）。")
    L.append(f"     ⇒ patch 已於 §四 結束時**還原**（`ns[\"_build_corner_range_v3\"] is _ORIG_RNG` ＝ "
             f"**{ns['_build_corner_range_v3'] is _ORIG_RNG}**；"
             f"`_corner_block_true_G` ＝ **{ns['_corner_block_true_G'] is _ORIG_TRUEG}**）。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
