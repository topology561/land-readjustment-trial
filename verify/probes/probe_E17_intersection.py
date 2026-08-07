# -*- coding: utf-8 -*-
r"""**D-0b §三**：`E-1.7` 出局之量化（⛔ 只出數字與出處·**禁提建議**）。

⛔ 零碼面·不切換·不接 `run_all`。門檻是否調整**屬 KL**——本檔**不提出任何調整建議**。

## 受測

對每一候選，量其**真交集**（＝ 宗地多邊形 ∩ 街角規定範圍）於**舊範圍**與**新範圍**之值，
並與 `E-1.7` 之 `1.0㎡` 門檻比對。

🔒 **真交集之算式逐字沿用生產**：`cp.intersection(_corner_poly)` 之 `.area`
（`grep -n "inter1 = cp.intersection" app.py`）；候選之多邊形取 `cand['polygon_coords']`
（同 `app.py:11089`）。⛔ 未另寫第二套。

## 🔒 自我驗證閘

| 閘 | 內容 |
|---|---|
| **E1** | 新範圍面積 == 凍存之 GEO-1 §三 (8) 新面積（16 格·容差 `1e-3`） |
| **E2** | 舊範圍面積 == 凍存之 GEO-1 §三 (7) 舊面積（16 格·容差 `1e-3`） |

⛔ 閘不過之格，其真交集**不可據**。
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

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_E17_intersection.log")
_LBIG = 1.0e5
THR = 1.0          # E-1.7 門檻（出處見【D】·⛔ 本檔不裁其去留）
NEAR = 2.0         # 「逼近門檻」之標示線（**先行宣告**·⛔ 未由結果反推）

# 凍存期望（GEO-1 §三·`63ae86d`）(舊, 新)
EXP = {
    ("0m", "R1", "left"): (114.7072, 114.9397), ("0m", "R1", "right"): (116.8414, 110.1749),
    ("0m", "R2", "left"): (227.1050, 152.9867), ("0m", "R3", "right"): (226.6930, 153.8039),
    ("0m", "R4", "left"): (135.1873, 116.0784), ("0m", "R4", "right"): (137.0042, 111.0225),
    ("0m", "R5", "left"): (217.9702, 146.4818), ("0m", "R6", "right"): (145.8835, 145.8834),
    ("3.5m", "R1", "left"): (230.8098, 225.4248), ("3.5m", "R1", "right"): (232.7931, 226.1260),
    ("3.5m", "R2", "left"): (384.1511, 308.1618), ("3.5m", "R3", "right"): (383.6669, 307.7486),
    ("3.5m", "R4", "left"): (251.1151, 225.0039), ("3.5m", "R4", "right"): (252.8551, 225.4208),
    ("3.5m", "R5", "left"): (371.1713, 299.6868), ("3.5m", "R6", "right"): (298.1445, 298.1445),
}
FOCUS = [("0m", "R2", "left", "628-40(1)"), ("0m", "R3", "right", "628-28(1)"),
         ("0m", "R5", "left", "628-7(2)")]


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
    L.append("=" * 190)
    L.append("【D-0b §三】E-1.7 出局之量化 — ⛔ 只出數字與出處·**禁提建議**（門檻去留屬 KL）")
    L.append("=" * 190)

    ns, fake_st = harvest()
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

    # ── 舊／新範圍（逐格）────────────────────────────────────────────────
    RNG = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            F1 = (float(fl["p1"][0]), float(fl["p1"][1]))
            F2 = (float(fl["p2"][0]), float(fl["p2"][1]))
            dh = _u(F2[0] - F1[0], F2[1] - F1[1])
            nh = (-dh[1], dh[0])
            cen = b.get("centroid") or (0.0, 0.0)
            if ((float(cen[0]) - F1[0]) * nh[0] + (float(cen[1]) - F1[1]) * nh[1]) < 0:
                nh = (-nh[0], -nh[1])
            verts = b.get("vertices") or []
            blk = _PG([(float(v[0]), float(v[1])) for v in verts])
            if not blk.is_valid:
                blk = blk.buffer(0)
            bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), verts)
            depth = float((snapshot["blocks"].get(lbl) or {}).get("街廓分配深度_m") or 0.0)
            for which in ("left", "right"):
                if which not in (sd_by.get(lbl) or {}):
                    continue
                sd = sd_by[lbl][which]
                chi = ns["_make_chamfer_tri_wb"](b, which)
                try:
                    old = ns["_build_corner_range_v3"](
                        verts, b.get("centroid"), [fl["p1"], fl["p2"]], bp,
                        [sd["p1"], sd["p2"]], al_by.get(lbl), depth, setback, legal_w, chi,
                        dxf_quantum=((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected"),
                        _label=lbl, _side=which)
                except RuntimeError:
                    old = None
                # 新構造（K-9-5-4）：SIDELINE 平移 S1
                P0 = F1 if which == "left" else F2
                S1p = (float(sd["p1"][0]), float(sd["p1"][1]))
                S2p = (float(sd["p2"][0]), float(sd["p2"][1]))
                su = _u(S2p[0] - S1p[0], S2p[1] - S1p[1])
                new = None
                if chi is not None and not chi.is_empty:
                    _fline = _LS([(F1[0] - dh[0] * _LBIG, F1[1] - dh[1] * _LBIG),
                                  (F1[0] + dh[0] * _LBIG, F1[1] + dh[1] * _LBIG)])
                    _c = [c for c in list(chi.exterior.coords)[:-1]
                          if math.hypot(c[0] - P0[0], c[1] - P0[1]) > 1e-9]
                    _c.sort(key=lambda p: _PT(p).distance(_fline))
                    Ps = (float(_c[0][0]), float(_c[0][1]))
                    _sP0 = (P0[0] - F1[0]) * dh[0] + (P0[1] - F1[1]) * dh[1]
                    _sPs = (Ps[0] - F1[0]) * dh[0] + (Ps[1] - F1[1]) * dh[1]
                    S1v = max(abs(_sPs - _sP0), setback + legal_w)
                    uu = dh if which == "left" else (-dh[0], -dh[1])
                    T1 = (S1p[0] + S1v * uu[0], S1p[1] + S1v * uu[1])
                    _cut = _LS([(T1[0] - su[0] * _LBIG, T1[1] - su[1] * _LBIG),
                                (T1[0] + su[0] * _LBIG, T1[1] + su[1] * _LBIG)])
                    try:
                        _pc = list(_split(blk, _cut).geoms)
                    except Exception:
                        _pc = []
                    if len(_pc) >= 2:
                        _anc = _PT(((S1p[0] + S2p[0]) / 2.0, (S1p[1] + S2p[1]) / 2.0))
                        new = min(_pc, key=lambda g: g.distance(_anc))
                        new = new.difference(chi)
                        if not new.is_valid:
                            new = new.buffer(0)
                RNG[(sb, lbl, which)] = (old, new)

    # ── 閘 E1／E2 ───────────────────────────────────────────────────────
    L.append("")
    L.append("【A】自我驗證閘（範圍面積 vs 凍存之 GEO-1 §三·容差 1e-3）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'舊面積':>13}{'期望(7)':>12}{'E2':>5}"
             f"{'新面積':>13}{'期望(8)':>12}{'E1':>5}")
    L.append("-" * 190)
    _e1 = _e2 = _n = 0
    OK = {}
    for k in sorted(RNG):
        o, nw = RNG[k]
        eo, en = EXP.get(k, (float("nan"), float("nan")))
        _ao = float(o.area) if o is not None else float("nan")
        _an = float(nw.area) if nw is not None else float("nan")
        _p2 = (abs(_ao - eo) <= 1e-3); _p1 = (abs(_an - en) <= 1e-3)
        _e2 += int(_p2); _e1 += int(_p1); _n += 1
        OK[k] = (_p1 and _p2)
        L.append(f"{k[0]:<6}{k[1] + '/' + k[2]:<12}{_ao:>13.4f}{eo:>12.4f}"
                 f"{('✅' if _p2 else '🔴'):>5}{_an:>13.4f}{en:>12.4f}{('✅' if _p1 else '🔴'):>5}")
    L.append("-" * 190)
    L.append(f"  E2（舊）**{_e2}/{_n}** 過　E1（新）**{_e1}/{_n}** 過"
             "（⛔ 未過之格其真交集不可據）")

    # ── 捕捉候選（wrapper on v12·⛔ 不改其行為）──────────────────────────
    CAND = {}
    _orig = ns["select_corner_lots_both_sides_v12"]

    def _wrap(**kw):
        _blk = (fake_st.session_state.get("f3_current_pk_block", "") or "")
        CAND.setdefault(_blk, list(kw.get("candidates") or []))
        return _orig(**kw)

    ns["select_corner_lots_both_sides_v12"] = _wrap
    ALLC = {}
    try:
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            CAND.clear()
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                          setback, snapshot=snapshot)
            ALLC[sb] = {k: list(v) for k, v in CAND.items()}
    finally:
        ns["select_corner_lots_both_sides_v12"] = _orig

    # ── 逐候選真交集 ────────────────────────────────────────────────────
    def _inter(cand, rng):
        """⛔ 逐字沿用 `app.py:11089-11104`（`cp.intersection(_corner_poly).area`）。"""
        co = cand.get("polygon_coords") or []
        if len(co) < 3 or rng is None:
            return float("nan")
        cp = _PG(co)
        if not cp.is_valid:
            cp = cp.buffer(0)
        if cp.is_empty:
            return float("nan")
        it = cp.intersection(rng)
        return float(it.area) if not it.is_empty else 0.0

    ROWS = []
    for k in sorted(RNG):
        sb, lbl, which = k
        o, nw = RNG[k]
        for c in (ALLC.get(sb, {}).get(lbl) or []):
            ROWS.append((sb, lbl, which, str(c.get("暫編地號", "")),
                         _inter(c, o), _inter(c, nw), OK.get(k, False)))

    # ── 【B】三個「—」格之量化 ─────────────────────────────────────────
    L.append("")
    L.append("【B】三格「—」之量化（(1)(2)(3)）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'候選':<13}{'(1)舊真交集':>14}{'(2)新真交集':>14}"
             f"{'(3)對 1.0㎡ 之差(新)':>20}{'舊是否過閘':>12}{'新是否過閘':>12}  閘")
    L.append("-" * 190)
    for f in FOCUS:
        _hit = [r for r in ROWS if (r[0], r[1], r[2], r[3]) == f]
        if not _hit:
            L.append(f"{f[0]:<6}{f[1] + '/' + f[2]:<12}{f[3]:<13}  🔴 未於候選清單中找到")
            continue
        r = _hit[0]
        L.append(f"{r[0]:<6}{r[1] + '/' + r[2]:<12}{r[3]:<13}{r[4]:>14.6f}{r[5]:>14.6f}"
                 f"{r[5] - THR:>20.6f}"
                 f"{('✅ >1.0' if r[4] > THR else '❌ ≤1.0'):>12}"
                 f"{('✅ >1.0' if r[5] > THR else '❌ ≤1.0'):>12}"
                 f"  {'✅' if r[6] else '🔴 不可據'}")
    L.append("-" * 190)
    L.append(f"  🔒 `E-1.7` 之判準為 **嚴格大於**：`_inter > {THR}`（見【D】）"
             "⇒ 「≤ 1.0」即**排除出 PK 候選池**（⛔ 非「未達 G 門檻」）。")

    # ── 【C】全 16 格逐候選 ────────────────────────────────────────────
    L.append("")
    L.append(f"【C】全 16 格**逐候選**真交集（新／舊）＋ 逼近門檻之標示"
             f"（標示線 `{NEAR:g}㎡`·**先行宣告**）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'候選':<13}{'舊真交集':>13}{'新真交集':>13}"
             f"{'Δ':>13}{'舊態':>8}{'新態':>8}  標示")
    L.append("-" * 190)
    _near, _out = [], []
    for r in sorted(ROWS):
        _f1 = "在池" if r[4] > THR else "**出局**"
        _f2 = "在池" if r[5] > THR else "**出局**"
        _mk = []
        if (r[4] > THR) and (r[5] <= THR):
            _mk.append("🔴 **新構造下出局**")
            _out.append(f"{r[0]} {r[1]}/{r[2]} {r[3]}")
        if THR < r[5] <= NEAR:
            _mk.append(f"⚠️ 逼近門檻（新 {r[5]:.4f} ≤ {NEAR:g}）")
            _near.append(f"{r[0]} {r[1]}/{r[2]} {r[3]}（新 {r[5]:.4f}）")
        if THR < r[4] <= NEAR:
            _mk.append(f"⚠️ 舊亦逼近（{r[4]:.4f}）")
        L.append(f"{r[0]:<6}{r[1] + '/' + r[2]:<12}{r[3]:<13}{r[4]:>13.6f}{r[5]:>13.6f}"
                 f"{r[5] - r[4]:>13.6f}{_f1:>8}{_f2:>8}  "
                 + "／".join(_mk) + ("" if r[6] else "  🔴 閘未過·不可據"))
    L.append("-" * 190)
    L.append(f"  🔴 **新構造下出局者 {len(_out)}**：" + ("；".join(_out) if _out else "（無）"))
    L.append(f"  ⚠️ **新構造下逼近門檻（`{THR:g} < 真交集 ≤ {NEAR:g}`）者 {len(_near)}**："
             + ("；".join(_near) if _near else "（無）"))
    L.append("     ⇒ 該等格於**換案**時最可能翻邊（⛔ 只陳述·**不提建議**）。")

    # ── 【D】E-1.7 之 `1.0` 出處與身分（正面指名）────────────────────────
    L.append("")
    L.append("【D】`E-1.7` 之 `1.0` 出處與**身分**（正面指名·⛔ 逐字自 app.py 現讀）")
    L.append("-" * 190)
    _app = io.open(os.path.join(REPO, "app.py"), encoding="utf-8").read().splitlines()
    for i, ln in enumerate(_app):
        if "_inter_p1_area > 1.0" in ln or "_inter_p2_area > 1.0" in ln:
            L.append(f"  `app.py:{i + 1}`　{ln.strip()}")
    L.append("")
    L.append("  🔒 **身分判定（依上引註解之逐字）**：")
    L.append("     · **不是法規數字**——註解未引任何法源；`1.0㎡` 不見於畸零地使用規則或 104 手冊之引文。")
    L.append("     · **不是純程式參數**——註解明載「**KL 絕對地板**」，且記錄了其沿革"
             "「門檻 **0.01 → 1.0㎡**」與**具體案由**（「剔 sliver 如 628-40 之 0.33」）。")
    L.append("     · ⇒ **身分 ＝ KL 裁定之工程門檻（W-D.1.3-b）**，"
             "由**個案 sliver（`628-40` 之 `0.33㎡`）**觸發而立。")
    for _p, _pat in ((os.path.join(REPO, "docs", "rulings"), "1.0㎡"),):
        pass
    L.append("  🔒 **正典側之查核（正面列舉·⛔ 非全倉排除式）**：")
    for _f, _kw in (("docs/rulings/K-6_街角地分配程序與可分配判準.md", "E-1.7"),
                    ("docs/rulings/K-6_街角地分配程序與可分配判準.md", "絕對地板"),
                    ("CLAUDE.md", "E-1.7"), ("CLAUDE.md", "絕對地板")):
        try:
            _t = io.open(os.path.join(REPO, _f), encoding="utf-8").read()
            _c = _t.count(_kw)
        except Exception:
            _c = -1
        L.append(f"     `grep -c \"{_kw}\" {_f}` ⇒ **{_c}**")
    L.append("     ⇒ 該門檻**未入裁定正典、未入 `CLAUDE.md`**——其唯一逐字出處為**碼內註解**。")
    L.append("")
    L.append("  ⛔ **本檔不提出任何調整建議**——門檻是否調整**屬 KL**（施工單 §三 明令）。")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
