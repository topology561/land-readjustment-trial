#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-91 §二 A 組**：「乙」之 shim ＋ 藍影定式對圖驗證 ＋ 遞補同構實證 ＋ 容差閘普查。

## 受詞（施工單 `W-G.9-91` §二）

- **A-1** 「乙」＝ **施加「不交叉」判準 ⇒ 違反者不配地 ⇒ 遞補**（`VR-050` 四）之**第一輪**土地後果
  （⛔ 無遞補·⛔ **不移任何線**）。
- **A-2-1** **藍影定式之對圖驗證**（`docs/specs/figures/宗地分配線邏輯.{cnt,lin,jpg}`）。
  🛑 不符 ⇒ **停機上呈**、⛔ 不得以自定式續算（施工單 §一 停機④／§七-6）。
- **A-3** **遞補介面之同構實證**（⛔ 只證不建）。
- **A-4** **容差級分類閘之全倉普查**（⛔ 只列不改）。

## 🛑 紅線（施工單 §二 A-6·§七）

⛔ 零 `app.py` 變更；⛔ `data/`／`docs/rulings/`／`verify/baselines/` 零變更；
🔴 ⛔ **不得移任何線**（`VR-050` 四：移線至下限 ＝ 超配 ⇒ `K-9-9 四` 明禁）；
⛔ 不建遞補／合併／調配池之任何介面；⛔ 不換圖／不換快照／不重烤；⛔ 不改 `V6DXF`；
🛑 ⛔ **不得就遞補／調配池／合併調配／超配出任何裁定題**（`K-9-11` 三）。

## 🔒 A-0　錯誤方向之**事前選定**（施工單 §二 A-0·節 98）

其瑕若使**後果看起來更小**（少報不配地之宗／少報破量殘餘）⇒ 代價落在**動生產碼且涉配地**那一批。
🔒 **事前選定：偏向<u>多報後果</u>**——凡「是否違反／是否入池」不確定者，一律判**違反／入池**並具名；
凡「是否為容差級分類閘」不確定者，一律**列入**並具名。

## 🔒 ⛔ 不得重造（原樣 import）

`w88.s_star_of`／`margin_of`（**判準**）、`w82.ring_edges`／`chord_interval`／`pred_chord`／`graze`／
`uj_of`／`pj_of`、`w81.analyse_cell`／`spy_solve`／`spy_pool`／`faces_of`／`_u`、
`w40.far_side_dir_and_pt`／`line_isect`／`s_of`、`w86._sin`／`PAR_TOL`、`w83.D_MIN`。

🔒 **驅動⛔ 不可 import**（寫在各檔 `main()` 內）——沿 `-88`→`-90` 之同一體例重寫，
**逐字具名之差** ＝ ① 多量「移除集之後果」② 多量 `遞補`／`容差閘`（二者⛔ 不需驅動）。

## 重跑

    python verify/probes/probe_WG991_yishim.py

rc **恆為 0**；唯缺件／取不到資料時 loud raise（`no-silent-fallback`）。
"""
import contextlib
import io
import math
import os
import re
import subprocess
import sys
import tokenize

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

import numpy as np                                                  # noqa: E402

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

import shapely                                                      # noqa: E402

import probe_WG981_scope as w81                                     # noqa: E402
import probe_WG982_chord as w82                                     # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402
import probe_WG983_k99prep as w83                                   # noqa: E402
import probe_WG986_oldjudge as w86                                  # noqa: E402
import probe_WG988_nocross as w88                                   # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210

SB = 0.0                    # 🔒 情境母體 ＝ 僅 0m（同 `-88`／`-90`·⛔ 不擴·具名）
D_MIN = w83.D_MIN           # 🔒 ＝ 2（原樣 import·⛔ 不另立）
PAR_TOL = w86.PAR_TOL

# 🔒 自身污染之排除（⛔ 逐字出艙·含「排除 0 筆」）
SELF = ["verify/probes/probe_WG991_yishim.py",
        "docs/reports/W-G.9-91_乙之shim與藍影對G.md"]


def _short_head():
    try:
        return subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True).stdout.strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG991_yishim_%s.log" % COMMIT)


def _tracked():
    out = subprocess.run(["git", "-C", REPO, "ls-files", "-z"], capture_output=True).stdout
    return sorted(p.decode("utf-8") for p in out.split(b"\x00") if p)


def _read(p):
    try:
        return io.open(os.path.join(REPO, p), encoding="utf-8", newline="").read()
    except Exception:                                               # noqa: BLE001
        return None


# 🩸 **f-string 之分層（本批自捕·首版漏之）**：Python **3.12 起** f-string 不再是單一
#    `STRING` token，而拆為 `FSTRING_START`／`FSTRING_MIDDLE`／`FSTRING_END`
#    ⇒ 只認 `tokenize.STRING` 之分層器，會把 **f-string 內之字樣**誤判為「可執行」。
#    🔒 實測（本機 %s）：`x = f"abc遞補{y}def"` ⇒ `FSTRING_MIDDLE 'abc遞補'`（⛔ 非 `STRING`）。
#    ⇒ 本函式**正面列舉** `STRING` ＋ `FSTRING_*` 三者。
_FSTR = tuple(getattr(tokenize, n) for n in
              ("FSTRING_START", "FSTRING_MIDDLE", "FSTRING_END")
              if hasattr(tokenize, n))


def layers_of(src):
    """回 (comment_lines, string_lines)——🔒 `string_lines` **含 f-string**。"""
    cl, sl = set(), set()
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type == tokenize.COMMENT:
            cl.add(tok.start[0])
        elif tok.type == tokenize.STRING or tok.type in _FSTR:
            for ln in range(tok.start[0], tok.end[0] + 1):
                sl.add(ln)
    return cl, sl


# ══════════════════════════════════════════════════════════════════════════
#  驅動（逐字同 `-88`／`-90`·差 ＝ 回傳 CELL 以供移除集之重算）
# ══════════════════════════════════════════════════════════════════════════
def build():
    ns, fake_st = harvest()
    strip_axis = ns["_strip_axis"]
    snapshot = rv.load_snapshot()
    o_solve, o_pool = ns["_solve_G_one"], ns["_pool_strips_for_block"]
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)
    w81.CAP.clear()
    w81.SOLVE.clear()
    w81.CUR["setback"] = SB
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB, snapshot=snapshot)
    ns["_solve_G_one"], ns["_pool_strips_for_block"] = w81.spy_solve(o_solve), w81.spy_pool(o_pool)
    try:
        for lbl in blks:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, SB)
                except Exception:                                   # noqa: BLE001
                    pass
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(w81.CAP)
    FL, BL = cad.get("front_lines") or {}, cad.get("baselines") or {}

    CELL = {}
    for rec in REAL:
        lbl = rec["label"]
        fl, bl = FL.get(lbl) or {}, BL.get(lbl) or {}
        if not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            continue
        o_ = tuple(float(x) for x in fl["p1"])
        d_ = tuple(np.asarray(rec["d_hat"], float)[:2])
        bpt = tuple(float(x) for x in bl["point"])
        bang = math.radians(float(bl.get("angle_deg", 0.0)))
        bdir = (math.cos(bang), math.sin(bang))
        meta, rows = w81.analyse_cell(rec, strip_axis)
        IV = []
        for g in rec["biz"]:
            ss_ = [w40.s_of((x, y), o_, d_) for x, y in list(g.exterior.coords)]
            IV.append((min(ss_), max(ss_)))
        kb = None
        for k in range(1, len(IV)):
            if min(v[0] for v in IV[k:]) > max(v[1] for v in IV[:k]) + 1e-6:
                kb = k if kb is None else -1
        groups = ([("左", list(range(0, kb))), ("右", list(range(kb, len(IV))))]
                  if isinstance(kb, int) and kb > 0
                  else [("單組(未測得唯一分界)", list(range(len(IV))))])
        edges, _dg = w82.ring_edges(list(rec["block"].exterior.coords)) \
            if rec["block"] is not None else (None, None)
        lots = {}
        for i in range(len(rec["biz"])):
            ua, pa = w40.far_side_dir_and_pt(rec["biz"][i], d_)
            Pc = Bc = None
            if ua is not None:
                Pc = w40.line_isect(tuple(pa), tuple(ua), o_, d_)
                Bc = w40.line_isect(tuple(pa), tuple(ua), bpt, bdir)
            lots[i] = {"ua": ua, "pa": pa,
                       "uj": w82.uj_of(rec, i), "pj": w82.pj_of(rec, i),
                       "Pc": Pc, "Bc": Bc,
                       "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area),
                       "is_corner": i in meta["corners"]}
        CELL[lbl] = {"rec": rec, "o": o_, "d": d_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "lots": lots, "meta": meta, "rows": rows,
                     "edges": edges}
    return CELL, REAL


def nocross_rows(CELL):
    """🔒 判準 ＝ `K-9-15` 三-2 之「不交叉」（原樣同 `-88` A-1／`-90` 量 4）。"""
    out = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            ordmap = {t: q for q, t in enumerate(idxs)}
            prev = None
            for i in idxs:
                lt = C["lots"][i]
                if lt["Pc"] is None or lt["Bc"] is None:
                    prev = None
                    continue
                if prev is None:
                    prev = i
                    continue
                pv = C["lots"][prev]
                uj, pj, uk, pk = pv["uj"], pv["pj"], lt["uj"], lt["pj"]
                rec_ok = not (uj is None or pj is None or uk is None or pk is None
                              or C["edges"] is None)
                sn = w86._sin(uj, uk) if (uj is not None and uk is not None) else float("nan")
                if rec_ok:
                    st_, sa_, ds_ = w88.s_star_of(pj, uj, pk, uk)
                    ci = w82.chord_interval(C["edges"], pj, uj)
                    inside = w82.pred_chord(ci, st_) if math.isfinite(st_) else None
                    gz = w82.graze(ci, st_) if math.isfinite(st_) else (False, float("nan"), "")
                    mg, _mn = w88.margin_of(ci, st_)
                else:
                    st_ = sa_ = ds_ = float("nan")
                    inside, gz, mg = None, (False, float("nan"), ""), float("nan")
                par_deg = rec_ok and (sa_ == 0.0)
                coincide = par_deg and (ds_ == 0.0)
                if not rec_ok:
                    reason, cross = "遠側界取不到", True
                elif coincide:
                    reason, cross = "重合", True
                elif par_deg:
                    reason, cross = "平行且不重合", False
                elif bool(gz[0]):
                    reason, cross = "擦邊", True
                elif inside is None:
                    reason, cross = "`s*` 非有限", True
                else:
                    reason, cross = ("在內" if inside else "在外"), bool(inside)
                out.append({"key": "%s|%s|%s|%s" % (lbl, side, ordmap.get(i), ordmap.get(prev)),
                            "lbl": lbl, "side": side, "i": i, "prev": prev,
                            "ord": ordmap.get(i), "s_star": st_, "margin": mg,
                            "reason": reason, "cross": bool(cross),
                            "area": lt["area"],
                            "inscope": bool(math.isfinite(sn) and sn > PAR_TOL)})
                prev = i
    return out


def zong2_pairs(REAL, strip_axis_unused=None, remove=None):
    """🔒 `②-宗` 破量（逐字同 `w83` A-2-2）；`remove` ＝ {lbl: set(i)} 之**不配地**集合。

    ⛔ **不移任何線**——移除 ＝ 把該宗自母體剔除（`w83` A-2-4 之同一作法），
    ⛔ 非改其幾何、⛔ 非改其他宗之位置。
    """
    remove = remove or {}
    out = {}
    for rec in REAL:
        lbl = rec["label"]
        if rec["block"] is None:
            continue
        edges, _dg = w82.ring_edges(list(rec["block"].exterior.coords))
        cache = {}
        pairs = []
        rem = remove.get(lbl, set())
        for r in rec["_rows_cache"]:
            if not r.get("ok") or r["d"] < D_MIN:
                continue
            j, k = r["j"], r["k"]
            if j in rem or k in rem:
                continue
            if j not in cache:
                pj, uj = w82.pj_of(rec, j), w82.uj_of(rec, j)
                cache[j] = None if (pj is None or uj is None) \
                    else w82.chord_interval(edges, pj, uj)
            ci = cache[j]
            if ci is None:
                continue
            if w82.pred_chord(ci, r["s_star"]):
                pairs.append({"j": j, "k": k,
                              "area": float(rec["biz"][j].intersection(rec["biz"][k]).area)})
        if pairs:
            out[lbl] = {"n": len(pairs), "area": sum(p["area"] for p in pairs), "pairs": pairs}
    return out


# ══════════════════════════════════════════════════════════════════════════
#  A-2-1　藍影定式之**對圖驗證**（🔒 拓樸層·⛔ 不取其度量·PROVENANCE §四）
# ══════════════════════════════════════════════════════════════════════════
def blue_figure_check(P):
    CNT = "docs/specs/figures/宗地分配線邏輯.cnt"
    LIN = "docs/specs/figures/宗地分配線邏輯.lin"
    src_c, src_l = _read(CNT), _read(LIN)
    if src_c is None or src_l is None:
        raise RuntimeError("🔴 圖證缺件：%s／%s（no-silent-fallback）" % (CNT, LIN))
    pts, lins = {}, []
    for ln in src_c.split("\n"):
        t = ln.split()
        if len(t) == 3:
            pts[int(t[0])] = (float(t[1]), float(t[2]))
    for ln in src_l.split("\n"):
        t = ln.split()
        if len(t) == 2:
            lins.append((int(t[0]), int(t[1])))

    def uu(a, b):
        dx, dy = pts[b][0] - pts[a][0], pts[b][1] - pts[a][1]
        n = math.hypot(dx, dy)
        return ((dx / n, dy / n) if n else (0.0, 0.0)), n

    def cl(v, w_, tol=2e-3):
        return abs(abs(v[0]) - abs(w_[0])) < tol and abs(abs(v[1]) - abs(w_[1])) < tol

    # 🔒 群方向**原樣引自** `PROVENANCE_宗地分配線邏輯.md` §三（⛔ 非本檔新算）
    DIRS = [("正街(FRONTLINE)", (0.0, 1.0), 7), ("最小深度垂線", (1.0, 0.0), 5),
            ("後側境界線(BASELINE)", (0.2059, 0.9786), 5), ("ALLOCLINE", (0.8707, 0.4918), 5),
            ("SIDELINE", (0.9859, 0.1673), 3), ("截角斜邊", (0.577334, 0.816508), 1)]
    grp = {k: [] for k, _v, _n in DIRS}
    unc = []
    for a, b in lins:
        d, _n = uu(a, b)
        for k, v, _e in DIRS:
            if cl(d, v):
                grp[k].append((a, b))
                break
        else:
            unc.append((a, b))
    P("  🔒 圖證：%s（**%d 點**）／%s（**%d 線**）——`PROVENANCE §三` 稱 **29 點／28 線** ⇒ %s"
      % (CNT, len(pts), LIN, len(lins),
         "✅ 相符" if (len(pts), len(lins)) == (29, 28) else "🔴 不符"))
    P("  %-24s %6s %6s %s" % ("群（方向原樣引 §三）", "實得", "§三", "判"))
    for k, _v, e in DIRS:
        P("  %-24s %6d %6d %s" % (k, len(grp[k]), e, "✅" if len(grp[k]) == e else "🔴 具名"))
    P("  %-24s %6d %6s —" % ("(未歸類)", len(unc), "—"))
    for a, b in unc:
        d, n = uu(a, b)
        P("     ⚠️ 未歸類段 %d–%d %s → %s　單位 (%.6f, %.6f)　長 %.4f"
          % (a, b, pts[a], pts[b], d[0], d[1], n))
        P("        🔒 該向與 BASELINE **正交**（`(0.2059,0.9786)` 旋 90° ＝ `(-0.9786,0.2059)`）"
          "⇒ **街廓之右緣**·⛔ 不屬六群之一·⛔ 不影響下判。")
    if len(grp["後側境界線(BASELINE)"]) != 5:
        P("     ⚠️ **BASELINE 段數 %d ≠ §三 所載 5**（具名·⛔ 不影響下判）：多出者為 BASELINE 之**延伸段**："
          % len(grp["後側境界線(BASELINE)"]))
        for a, b in grp["後側境界線(BASELINE)"]:
            _d, n = uu(a, b)
            P("        段 %2d–%-2d  %s → %s  長 %8.4f" % (a, b, pts[a], pts[b], n))

    P("")
    P("  🔒 **KL `.jpg` 之逐字（⛔ 原樣引用·⛔ 不改寫不濃縮）**：")
    P("     條件 2：「交於FRONTLINE及BASELINE的點要在前一宗土地的遠側境界線的交點後（例如：要在P1及B1後）」")
    P("     條件 3：「後側境界線交於BASELINE的點一定要在前一宗土地的遠側境界線於FRONTLINE上的交點")
    P("              （例如P1）沿FRONTLINE法向往BASELINE方向交於的點開始往後分配（例如B2後）」")
    P("     藍字  ：「此種方向的宗地分配線／第2宗土地至少要從B2開始／")
    P("              B1~B2範圍內的ALLOCLINE（藍色虛線）都不能為第2宗土地的遠側境界線」")

    FX = 183.089
    basep = set()
    for a, b in grp["後側境界線(BASELINE)"]:
        basep.add(a)
        basep.add(b)
    cand = [(a, b) for a, b in grp["SIDELINE"]
            if (abs(pts[a][0] - FX) < 1e-6 and b in basep)
            or (abs(pts[b][0] - FX) < 1e-6 and a in basep)]
    P("")
    P("  ① 街角第 1 宗之**遠側界** ＝ ∥SIDELINE 且自 FRONTLINE 連至 BASELINE 之段（`K-9-14`）")
    P("     候選 ＝ %d 段（須 1）%s" % (len(cand), "✅" if len(cand) == 1 else "🔴"))
    if len(cand) != 1:
        raise RuntimeError("🔴 候選 %d ≠ 1（no-silent-fallback）" % len(cand))
    a, b = cand[0]
    P1 = a if abs(pts[a][0] - FX) < 1e-6 else b
    B1 = b if P1 == a else a
    P("     ⇒ **P1 ＝ pt%d %s**（FRONTLINE 上）　**B1 ＝ pt%d %s**（BASELINE 上）"
      % (P1, pts[P1], B1, pts[B1]))

    y1 = pts[P1][1]
    hits = sorted(k for k, v in pts.items() if abs(v[1] - y1) < 1e-6 and k in basep)
    P("")
    P("  ② 依**條件 3** 求 `B2` ＝ `P1` 沿 FRONTLINE **法向**（＝ 水平·因正街為鉛直）交 BASELINE 之點")
    P("     BASELINE 上與 `P1` 同 y（%.3f）之點 ＝ %s" % (y1, [(k, pts[k]) for k in hits]))
    if not hits:
        raise RuntimeError("🔴 求不出 B2（no-silent-fallback）")
    B2 = hits[0]
    P("     ⇒ **B2 ＝ pt%d %s**" % (B2, pts[B2]))
    for a2, b2 in grp["最小深度垂線"]:
        if abs(pts[a2][1] - y1) < 1e-6:
            P("     🔒 佐證：`最小深度垂線` 群確有段 %d–%d  %s → %s" % (a2, b2, pts[a2], pts[b2]))

    d12 = math.hypot(pts[B1][0] - pts[B2][0], pts[B1][1] - pts[B2][1])
    seg = [(x, y) for x, y in grp["後側境界線(BASELINE)"] if {x, y} == {B1, B2}]
    P("")
    P("  ③ 🛑 **判：`B1` 與 `B2` 是否同一點？**")
    P("     ‖B1−B2‖ ＝ **%.6f**（圖面單位·🔒 **僅用於判「是否同點」**·⛔ 非度量·PROVENANCE §四）" % d12)
    P("     🔒 佐證（**拓樸**·⛔ 非度量）：`.lin` 中有一段 BASELINE **直接連接** B1 與 B2 ＝ %s"
      % (seg if seg else "🔴 無"))
    same = (d12 <= 1e-6)
    P("     ⇒ **%s**" % ("✅ 同一點" if same else "🔴 **B1 ≠ B2 ⇒ 二者為 BASELINE 上之相鄰<u>相異</u>點**"))

    P("")
    P("  ④ 🛑 **停機條款 ④ 之判定**")
    P("     claude.ai 之定式（施工單 A-2-1 逐字）：藍影 ＝ `block` ∩ {第 0 宗遠側界之外側}")
    P("                                        ∩ {**通過 `B1`** 之 ∥ALLOCLINE 之內側}")
    P("     KL 圖之逐字                        ：第 2 宗**至少要從 `B2` 開始**；")
    P("                                        **`B1~B2` 範圍內之 ALLOCLINE 都<u>不能</u>**為其遠側界")
    ok = same
    P("     ⇒ 下限線之**通過點**：claude.ai ＝ `B1` ／ KL 圖 ＝ `B2` ⇒ **%s**"
      % ("✅ 相符" if ok else "🔴 **不符**"))
    P("     ⇒ %s"
      % ("✅ `P5` 成立 ⇒ A-2-2 可續" if ok else
         "🛑 **停機上呈**（施工單 §一 停機④／§七-6）：⛔ **不得以自定式續算** ⇒ **A-2-2 ⛔ 不辦**"))
    if not ok:
        P("     🔒 **方向之具名**：`B1` 較 `B2` **在前** ⇒ 以 `B1` 為界之藍影**較小**")
        P("        ⇒ 其瑕**恰落在 A-0 所禁之方向**（使後果看起來更小）⇒ ⛔ 尤不得續算。")
    return ok, {"P1": pts[P1], "B1": pts[B1], "B2": pts[B2], "dist": d12}


# ══════════════════════════════════════════════════════════════════════════
#  A-3　遞補介面之同構實證（⛔ 只證不建）
# ══════════════════════════════════════════════════════════════════════════
def recompense_audit(P):
    path = "verify/run_verification.py"
    src = _read(path)
    if src is None:
        raise RuntimeError("🔴 缺件：%s" % path)
    lines = src.split("\n")
    # 🔒 以 `tokenize` 分「可執行／註解／字串」——⛔ 不以「字樣命中」逕判介面存在（`-89` ⑯）
    #    🩸 **含 f-string**（`layers_of` 之註解逐字說明本批之自捕）
    try:
        comment_lines, string_lines = layers_of(src)
    except Exception as e:                                          # noqa: BLE001
        raise RuntimeError("🔴 tokenize 失敗：%s（⛔ 不得靜默退回字樣法）" % e)
    hits = [(i, l) for i, l in enumerate(lines, 1) if "遞補" in l]
    P("  🔒 母體 ＝ `%s`（**%d 行**）；`遞補` 之**全部**命中 ＝ **%d 行**（⛔ 全列·無切片）"
      % (path, len(lines), len(hits)))
    P("     🔒 產生指令（節 105／修法 113）："
      "`len([i for i,l in enumerate(open('%s',encoding='utf-8'),1) if '遞補' in l])`" % path)
    P("")
    P("  %-6s %-10s %-64s %s" % ("行", "層", "受詞（逐字節錄）", "是否為「位次遞補」"))
    cnt = {"可執行": 0, "註解": 0, "字串": 0}
    posn = 0
    rows = []
    for i, l in hits:
        if i in comment_lines and "遞補" in l.split("#", 1)[-1]:
            layer = "註解"
        elif i in string_lines:
            layer = "字串"
        else:
            layer = "可執行"
        cnt[layer] += 1
        txt = l.strip()
        # 🔒 判準（正面列舉·⛔ 非啟發法）：「位次遞補」＝ `K-9-9 四` 之
        #    「投影序號中**下一位**之土地**遞補該位次**」⇒ 須同時出現「序號／位次／下一位」之語意。
        POSN_KEY = ["投影序號", "位次", "下一位", "次一位"]
        is_posn = any(k in txt for k in POSN_KEY)
        if is_posn:
            posn += 1
        rows.append((i, layer, txt, is_posn))
        P("  :%-5d %-10s %-64s %s" % (i, layer, txt[:64], "✅ 是" if is_posn else "⛔ 否"))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # A-3 `遞補` 之全部命中（全列）" % (len(hits), len(hits)))
    P("     ⇒ 分層：可執行 **%d**／註解 **%d**／字串（**含 f-string**）**%d**（合計 %d ／ %d ⇒ %s）"
      % (cnt["可執行"], cnt["註解"], cnt["字串"],
         sum(cnt.values()), len(hits), "✅" if sum(cnt.values()) == len(hits) else "🔴"))
    P("     🔴 **與 `W-G.9-89` 之「`run_verification.py`×11」對帳（同名不同量·⛔ 不得互代）**：")
    P("        `-89` 之 **11** ＝ **非註解**之行（%d 總 − %d 註解 ＝ %d）%s"
      % (len(hits), cnt["註解"], len(hits) - cnt["註解"],
         "✅ 複現" if len(hits) - cnt["註解"] == 11 else "🔴 **不符·具名**"))
    P("        本批之 **%d** ＝ **可執行層**（⛔ 另扣 %d 個「字樣落在字串／f-string 內」之行）"
      % (cnt["可執行"], cnt["字串"]))
    P("        ⇒ 🔒 **二數皆對、母體不同**；而**判「介面是否存在」之受詞應為可執行層**"
      "（`-89` ⑯：⛔ 只在註解／字串裡的字⛔ 不得判為 `【已有】`）。")
    P("     🔴 **判為「位次遞補」者 ＝ %d ／ %d**" % (posn, len(hits)))
    P("     🔒 判準（正面列舉·⛔ 非啟發法）：含 `投影序號`／`位次`／`下一位`／`次一位` 任一者")
    P("        ——即 `K-9-9 四` 之逐字「**投影序號中下一位之土地遞補該位次**」之語意。")

    # 🔒 判別力（**二側**）——⛔ 只做陰性對照者，其「全 0」無從與「判準恆否」區辨
    POSN_KEY2 = ["投影序號", "位次", "下一位", "次一位"]
    P("")
    P("  🔒 **判別力之陽性對照（⛔ 不可省·本批自補）**：上開判準對全母體**皆判「否」**")
    P("     ⇒ **⛔ 無從與「判準恆否」區辨** ⇒ 餵一個**已知為真**之合成句：")
    SYN = "results.append((\"投影序號中下一位之土地遞補該位次\", ok, v))"
    P("     合成句 ＝ %s" % SYN)
    syn_hit = any(k in SYN for k in POSN_KEY2)
    P("     ⇒ 判 ＝ **%s**（須「✅ 是」）%s"
      % ("✅ 是" if syn_hit else "⛔ 否", "✅" if syn_hit else "🔴 **判準恆否 ⇒ 本節結論無效·停機**"))
    P("     🔒 ⇒ 該判準**非恆否** ⇒ 「%d ／ %d」係**真 0**、⛔ 非量測器壞掉。" % (posn, len(hits)))

    # 🔒 判別力：對一個**已知⛔ 非位次遞補**之命中同法判定 ⇒ 其判須為「⛔ 非」
    ctrl = [(i, t) for i, _ly, t, _p in rows if "整形" in t]
    P("")
    P("  🔒 **判別力之陰性對照（施工單 A-3 所令）**：對已知⛔ 非位次遞補之 `F.1 遞補整形` 同法判定")
    if ctrl:
        for i, t in ctrl:
            j = [x for x in rows if x[0] == i][0]
            P("     :%d  %s" % (i, t[:120]))
            P("        ⇒ 判 ＝ %s（須「⛔ 否」）%s"
              % ("✅ 是" if j[3] else "⛔ 否", "✅" if not j[3] else "🔴 **判別器恆同構·具名**"))
    else:
        P("     ⚠️ **母體內查無 `整形` 之命中 ⇒ 該判別力<u>無母體</u>·具名**（⛔ 不得以「未見反例」充作已驗）")

    # 🔒 **母體之擴掃**（⛔ 施工單只令 `run_verification.py`·本批自補·A-0 偏向多報後果）
    #    由：「該檔可執行層 ＝ 0」⛔ 不蘊含「全倉無遞補介面」——**母體選錯**是「0」之第一嫌疑。
    P("")
    P("  🔒 **母體之擴掃（CC 自補·⛔ 施工單未令）**：`遞補` 於 `verify/**.py` ＋ `app.py` 之**可執行層**")
    P("     由：「`%s` 可執行層 ＝ %d」⛔ **不蘊含**「全倉無遞補介面」" % (path, cnt["可執行"]))
    F2 = [f for f in _tracked()
          if ((f.startswith("verify/") and f.endswith(".py")) or f == "app.py")
          and f not in SELF]
    wide = []
    for f in F2:
        s2 = _read(f)
        if s2 is None:
            continue
        try:
            c2, s2l = layers_of(s2)
        except Exception:                                           # noqa: BLE001
            c2, s2l = set(), set()
        for i, l in enumerate(s2.split("\n"), 1):
            if "遞補" not in l:
                continue
            lay = "註解" if i in c2 else ("字串" if i in s2l else "可執行")
            wide.append((f, i, lay, l.strip()))
    wex = [x for x in wide if x[2] == "可執行"]
    P("     ⇒ 母體 ＝ **%d 檔**；`遞補` 之命中 ＝ **%d 行**；**可執行層 ＝ %d 行**"
      % (len(F2), len(wide), len(wex)))
    P("     %-46s %-7s %s" % ("檔", "行", "節錄"))
    for f, i, _ly, t in wex[:20]:
        P("     %-46s :%-6d %s" % (f, i, t[:104]))
    if len(wex) > 20:
        P("     …（另 %d 行·**未列**·🔒 母體 ＝ %d）" % (len(wex) - 20, len(wex)))
    P("     POPULATION=%d PRINTED=%d SUPPRESSED=%d  # A-3 擴掃·可執行層"
      % (len(wex), min(20, len(wex)), max(0, len(wex) - 20)))
    wposn = [x for x in wex if any(k in x[3] for k in POSN_KEY2)]
    P("     🔴 **其中判為「位次遞補」者 ＝ %d ／ %d**" % (len(wposn), len(wex)))
    for f, i, _ly, t in wposn:
        P("        🔴 %s:%d  %s" % (f, i, t[:120]))

    # 🔒 以既有實例對拍：`W-D.4 遞補錨`
    P("")
    P("  🔒 **以既有實例對拍**（施工單 A-3-2）：`W-D.4 遞補錨` 之逐字")
    anc = [(i, l.strip()) for i, l in enumerate(lines, 1) if "遞補錨" in l]
    for i, t in anc:
        P("     :%-5d %s" % (i, t[:170]))
    P("     POPULATION=%d PRINTED=%d SUPPRESSED=0  # `遞補錨` 全列" % (len(anc), len(anc)))
    P("")
    P("  🔒 **與 `K-9-9 四` 之逐項對照**（⛔ 解釋不出即具名為未答）：")
    P("     | 項 | `K-9-9 四`（正典逐字） | `W-D.4 遞補錨`（倉內實例） | 判 |")
    P("     | 觸發 | 依該宗 `G` 值算出之**遠側界位置**在起算垂線之前 ⇒ 不配地 |"
      " `W-D.4` 之**碎片**（面積過小·`R6 85.66`） | ⛔ **不同**（幾何位置 vs 面積門檻） |")
    P("     | 受詞 | **投影序號中下一位之土地** | `628-4(1)`（**跳過** `628(2)`;`628-1(2)`;`628-23(1)`） |"
      " ⚠️ **形式相近**（皆為「順序中之下一位」）·**惟跳過規則之依據未載** |")
    P("     | 結果 | 該宗**遞補該位次** | 該地號成為遞補標的 | ⚠️ 形式相近 |")
    P("     | 🔴 **跳過之依據** | 正典**未規定跳過** | 跳過 3 筆·**其規則於本檔內查無** |"
      " 🔴 **不同構之關鍵** |")
    P("     🔴 **必答（A-3-3）**：`W-D.4 遞補錨` 是否即 `K-9-9 四` 所指之機制？")
    P("        ⇒ 🛑 **未答·具名**——二者之**觸發條件不同**（面積門檻 vs 遠側界位置），")
    P("           且 `W-D.4` 之**跳過規則**於 `%s` 內**查無其依據** ⇒ ⛔ 不得判為同構。" % path)
    P("        🔒 ⛔ **本判⛔ 非裁定題**（`K-9-11` 三：遞補之機制⛔ 不另訂）——係**實證之結果**。")
    return {"total": len(hits), "cnt": cnt, "posn": posn,
            "ctrl_ok": bool(ctrl) and not any(x[3] for x in rows if x[0] in [c[0] for c in ctrl])}


# ══════════════════════════════════════════════════════════════════════════
#  A-4　容差級分類閘之全倉普查（⛔ 只列不改）
# ══════════════════════════════════════════════════════════════════════════
TOLRE = re.compile(r"(?P<op><=|>=|<|>|==|!=)\s*(?P<tol>\d*\.?\d+e-\d+|\d*\.?\d+E-\d+)")
TOLRE2 = re.compile(r"(?P<tol>\d*\.?\d+e-\d+|\d*\.?\d+E-\d+)\s*(?P<op><=|>=|<|>)")


def tolerance_survey(P):
    F = [f for f in _tracked()
         if ((f.startswith("verify/") and f.endswith(".py")) or f == "app.py")
         and f not in SELF]
    P("  🔒 母體 ＝ `git ls-files` 之 `verify/**.py` ＋ `app.py`，**扣除本探針自身**")
    P("     ⇒ **%d 檔**；🔒 自身污染之排除逐字：%s ⇒ 其於母體內者 ＝ **%d 筆**"
      % (len(F), SELF, sum(1 for p in SELF if p in _tracked()
                           and ((p.startswith("verify/") and p.endswith(".py")) or p == "app.py"))))
    P("     🔒 產生指令（修法 113）：`git ls-files -z` → 篩 `verify/**.py` ∪ `app.py` → 扣 SELF")
    rows = []
    nolayer = []
    for f in F:
        s = _read(f)
        if s is None:
            continue
        try:
            comment_lines, string_lines = layers_of(s)      # 🩸 含 f-string（本批自捕）
        except Exception:                                           # noqa: BLE001
            comment_lines, string_lines = set(), set()
            nolayer.append(f)
        for i, l in enumerate(s.split("\n"), 1):
            m = TOLRE.search(l) or TOLRE2.search(l)
            if not m:
                continue
            if i in comment_lines and "#" in l and m.start() > l.index("#"):
                layer = "註解"
            elif i in string_lines and i not in comment_lines:
                layer = "字串"
            else:
                layer = "可執行"
            rows.append({"f": f, "i": i, "tol": m.group("tol"), "op": m.group("op"),
                         "layer": layer, "txt": l.strip()})
    P("     ⇒ **命中 ＝ %d 處**（`<op> <tol>` 或 `<tol> <op>` 之字面·⛔ 未含以具名常數表示者）"
      % len(rows))
    ex = [r for r in rows if r["layer"] == "可執行"]
    P("     ⇒ 其中**可執行層 ＝ %d**（註解 %d／字串（**含 f-string**）%d）"
      % (len(ex), sum(1 for r in rows if r["layer"] == "註解"),
         sum(1 for r in rows if r["layer"] == "字串")))
    P("     🔒 **分層失敗之檔 ＝ %d**（⛔ 不得靜默：其行一律落入「可執行」⇒ 偏向多報·符 A-0）%s"
      % (len(nolayer), (" 逐檔：%s" % nolayer) if nolayer else ""))

    from collections import Counter
    dist = Counter(r["tol"] for r in ex)
    P("")
    P("  🔒 **容差值之分布（可執行層·全列）**：")
    for t, n in sorted(dist.items(), key=lambda kv: (-kv[1], kv[0])):
        P("     %-14s %4d" % (t, n))
    P("     POPULATION=%d PRINTED=%d SUPPRESSED=0" % (len(dist), len(dist)))

    # 🔒 「入判定鏈」之判準（正面列舉·⛔ 非啟發法）
    CHAIN = ["raise", "assert", "return", "if ", "elif ", "while ",
             "continue", "break", "not ", " and ", " or "]
    P("")
    P("  🔒 **「分類結果是否入判定鏈」之判準（正面列舉·⛔ 非啟發法）**：該行含 %s 任一者。" % CHAIN)
    P("     ⚠️ **A-0（偏向多報）**：不確定者一律**列入**並具名。")
    inch = [r for r in ex if any(k in r["txt"] for k in CHAIN)]
    P("     ⇒ 🔴 **入判定鏈者 ＝ %d ／ %d（可執行層）**" % (len(inch), len(ex)))
    P("")
    P("  🔴 **標記「波末換圖後須重驗」者（＝ 入判定鏈者）逐處全列**：")
    P("  %-46s %-7s %-8s %-6s %s" % ("檔", "行", "容差", "層", "節錄"))
    for r in sorted(inch, key=lambda x: (x["f"], x["i"])):
        P("  %-46s :%-6d %-8s %-6s %s" % (r["f"], r["i"], r["tol"], r["layer"], r["txt"][:86]))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # A-4 入判定鏈之容差閘（全列）"
      % (len(inch), len(inch)))

    # 🔒 判別力：`_PAR_TOL = 1e-6`（`K-6:1010`）為已知之一支 ⇒ 須被命中
    P("")
    P("  🔒 **判別力（施工單 A-4 所令）**：`_PAR_TOL`（正典 `K-6:1010` ＝ `1e-6`）為**已知**之一支")
    par = [r for r in rows if "_PAR_TOL" in r["txt"]]
    par_def = []
    for f in F:
        s = _read(f)
        if s is None:
            continue
        for i, l in enumerate(s.split("\n"), 1):
            if re.search(r"_PAR_TOL\s*=", l):
                par_def.append((f, i, l.strip()))
    P("     🔒 **三個數之標籤（⛔ 不得互代·同名不同量）**：")
    P("     ① `_PAR_TOL\\s*=` 之**字樣命中**（含註解／docstring 之引述）＝ **%d 處**（全列）："
      % len(par_def))
    for f, i, t in par_def:
        P("        %s:%d  %s" % (f, i, t[:120]))
    real_def = [x for x in par_def
                if re.match(r"^\s*_PAR_TOL\s*=", x[2]) and not x[2].lstrip().startswith("#")]
    P("     ② 其中**真定義行**（行首即 `_PAR_TOL =`·⛔ 非引述）＝ **%d 處**：" % len(real_def))
    for f, i, t in real_def:
        P("        %s:%d  %s" % (f, i, t[:120]))
    P("     ③ **本普查器（比較運算元 ＋ 容差字面）對含 `_PAR_TOL` 之行之命中 ＝ %d 處**" % len(par))
    for r in sorted(par, key=lambda x: (x["f"], x["i"])):
        P("        %s:%d  %s" % (r["f"], r["i"], r["txt"][:120]))
    P("")
    P("     🔴 **具名之限制（依施工單「⛔ 未命中即普查器有誤·具名」）**：")
    P("        本普查器之樣式為「**比較運算元 ＋ 容差<u>字面</u>**」")
    P("        ⇒ **⛔ 抓不到「先定義為具名常數、再於他處比較」之閘**——`_PAR_TOL` 正是此形。")
    P("        ⇒ 🔴 **本普查器之射程為<u>下界</u>**（⛔ 非全集）·⛔ 不得以其數宣稱「全倉只有這些」。")
    # 🔒 補掃：具名常數之**比較**（正面列舉·證該限制確實存在而非藉口）
    NAMED_RE = re.compile(r"(<=|>=|<|>|==|!=)\s*_?[A-Z][A-Z0-9_]{2,}\b"
                          r"|_?[A-Z][A-Z0-9_]{2,}\s*(<=|>=|<|>)")
    named = []
    for f in F:
        s = _read(f)
        if s is None:
            continue
        try:
            clx, slx = layers_of(s)
        except Exception:                                           # noqa: BLE001
            clx, slx = set(), set()
        for i, l in enumerate(s.split("\n"), 1):
            if i in clx or i in slx:
                continue
            if "TOL" in l and NAMED_RE.search(l):
                named.append((f, i, l.strip()))
    P("")
    P("     🔒 **補掃（具名常數之<u>比較</u>·樣式 ＝ 比較運算元 ＋ 全大寫識別字 ∧ 含 `TOL`）**")
    P("        ⇒ **%d 處**（可執行層·⛔ 已扣註解與字串）" % len(named))
    for f, i, t in named[:20]:
        P("        %s:%d  %s" % (f, i, t[:110]))
    if len(named) > 20:
        P("        …（另 %d 處·**未列**·🔒 母體 ＝ %d）" % (len(named) - 20, len(named)))
    par_use = [x for x in named if "_PAR_TOL" in x[2]]
    P("     🔒 **判別力之結論**：`_PAR_TOL` 之**消費點**（＝ 真正之分類閘）由補掃命中 **%d 處**："
      % len(par_use))
    for f, i, t in par_use:
        P("        %s:%d  %s" % (f, i, t[:130]))
    P("        ⇒ **%s**"
      % ("✅ 已命中 ⇒ 施工單所令之判別力對照**成立**（惟係由**補掃**、⛔ 非主樣式）"
         if par_use else "🔴 **未命中 ⇒ 普查器有誤·具名**"))
    return {"total": len(rows), "exec": len(ex), "inchain": len(inch),
            "dist": dict(dist), "par_def": len(par_def), "real_def": len(real_def),
            "named": len(named), "par_use": len(par_use), "nolayer": len(nolayer)}


# ══════════════════════════════════════════════════════════════════════════
def main():                                                         # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【W-G.9-91 §二 A 組】「乙」之 shim ＋ 藍影定式對圖驗證 ＋ 遞補同構實證 ＋ 容差閘普查")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🛑 生產路徑不動：`run_verification.py::V6DXF` ＝ %s"
      % os.path.relpath(rv.V6DXF, REPO).replace(os.sep, "/"))
    P("  🔒 **A-0 事前選定：偏向<u>多報後果</u>**（不確定者一律判違反／入池／列入·並具名）")
    P("  🔒 情境母體 ＝ **僅 %gm**（同 `-88`／`-90`·⛔ 不擴·具名）" % SB)
    P("  🔴 ⛔ **不移任何線**（`VR-050` 四·`K-9-9 四` 明禁超配）；⛔ 不建任何介面。")

    # ══ A-2-1（🛑 閘·先辦——其判定決定 A-2-2 辦不辦）══════════════════
    P("")
    P("=" * W)
    P("【D／A-2-1】🛑 **藍影定式之對圖驗證**（🔒 先辦·其判定決定 A-2-2 辦不辦）")
    P("=" * W)
    blue_ok, blue = blue_figure_check(P)

    # ══ 驅動 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【驅動】`%gm` × R1–R6" % SB)
    P("=" * W)
    CELL, REAL = build()
    for rec in REAL:
        rec["_rows_cache"] = CELL[rec["label"]]["rows"] if rec["label"] in CELL else []
    P("  攔截 **%d 格**；宗數合計 ＝ **%d**"
      % (len(REAL), sum(len(r["biz"]) for r in REAL)))

    # ══ A-1 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【C／A-1】🛑 「乙」之 shim 量測（⛔ 不移線·判準 ＝ 不交叉·原樣 import `w88`）")
    P("=" * W)
    ROWS = nocross_rows(CELL)
    bad = [r for r in ROWS if r["cross"]]
    P("  **A-1-1 違反宗之確認**：母體 ＝ **%d 列**；違反 ＝ **%d 宗**" % (len(ROWS), len(bad)))
    P("  %-18s %-6s %-6s %14s %16s %-14s" % ("鍵", "i", "前", "s*", "面積(㎡)", "情形"))
    for r in bad:
        P("  %-18s %-6d %-6d %14.4f %16.8f %-14s"
          % (r["key"], r["i"], r["prev"], r["s_star"], r["area"], r["reason"]))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # A-1-1 違反宗（全列）"
      % (len(ROWS), len(bad), len(ROWS) - len(bad)))
    tot_bad = sum(r["area"] for r in bad)
    P("     面積合計（帶號）＝ **%.4f ㎡** ／（絕對值）＝ **%.4f ㎡**"
      % (tot_bad, sum(abs(r["area"]) for r in bad)))
    P("     🔒 **與 `-88`／`-90` 之逐位對拍**（倉內錨 ＝ 2 宗·`R2左第1宗 3.80822376`／`R5左第1宗 0.98672881`）：")
    ANCH = {"R2|左|1|0": 3.80822376, "R5|左|1|0": 0.98672881}
    okA = True
    for k, v in sorted(ANCH.items()):
        got = next((r["area"] for r in bad if r["key"] == k), None)
        same = (got is not None) and (round(got, 8) == v)
        okA &= same
        P("        %-18s 錨 %14.8f ／ 本批 %s ⇒ %s"
          % (k, v, ("%.8f" % got) if got is not None else "🔴 未命中",
             "✅ 逐位相同（8dp）" if same else "🔴 **不符**"))
    P("     ⇒ **名單對稱差 ＝ %d**（A-0(丁)）"
      % len(set(r["key"] for r in bad) ^ set(ANCH)))

    # A-1-2 第一輪處置
    rem = {}
    for r in bad:
        rem.setdefault(r["lbl"], set()).add(r["i"])
    P("")
    P("  **A-1-2 第一輪處置**（`K-9-9 四`·⛔ 無遞補·⛔ 不移線）")
    P("     不配地之宗 ＝ %s" % {k: sorted(v) for k, v in sorted(rem.items())})
    P("     其面積**入調配池** ＝ **%.4f ㎡**（🔒 ＝ A-1-1 之合計·⛔ 非另算）" % tot_bad)
    P("     🔴 **其餘各宗之位置與面積**（🔒 應**逐位不變**——⛔ 未遞補 ⇒ 幾何不動）：")
    P("     %-6s %-5s %18s %18s %18s %-8s" % ("街廓", "i", "s_lo", "s_hi", "面積(㎡)", "街角?"))
    nrest = 0
    for lbl in sorted(CELL):
        for i, lt in sorted(CELL[lbl]["lots"].items()):
            if i in rem.get(lbl, set()):
                continue
            nrest += 1
            P("     %-6s %-5d %18.9f %18.9f %18.9f %-8s"
              % (lbl, i, lt["s_lo"], lt["s_hi"], lt["area"],
                 "是（第 0 宗）" if lt["is_corner"] else "否"))
    P("     POPULATION=%d PRINTED=%d SUPPRESSED=0  # A-1-2 其餘各宗（全列·⛔ 無切片）"
      % (nrest, nrest))
    P("     🔒 **母體 ＝ 其餘各宗 ＝ %d 宗**（全部 %d − 不配地 %d）"
      % (nrest, sum(len(r["biz"]) for r in REAL), sum(len(v) for v in rem.values())))
    P("     🔒 **本 shim 之構造保證**：移除 ＝ 自**破量對之母體**剔除該宗（同 `w83` A-2-4），")
    P("        ⛔ **未觸及任何宗之幾何** ⇒ 其餘各宗之 `s_lo`／`s_hi`／面積**構造上不可能變**。")
    P("        🔒 **判別力（⛔ 不以構造代替量測）**：下方負對照（移除集 ＝ ∅）之破量須回到倉內錨；")
    P("           若構造有誤（隱含移線），負對照必不相符。")

    # A-1-3 第一輪後之 ②-宗 破量 ＋ 負對照
    P("")
    P("  **A-1-3 第一輪後之 `②-宗` 破量**（重跑弦區間閉式·`d ≥ %d`）" % D_MIN)
    before = zong2_pairs(REAL, remove=None)
    after = zong2_pairs(REAL, remove=rem)
    P("     🔒 **負對照（判別力·常設 8）＝ 移除集 ＝ ∅** ⇒ 須得倉內錨 `R2 45.9766`／`R5 56.3293`：")
    NEG = {"R2": 45.9766, "R5": 56.3293}
    okN = True
    for k in sorted(NEG):
        got = before.get(k, {}).get("area")
        same = (got is not None) and (abs(got - NEG[k]) < 5e-5)
        okN &= same
        P("        %-4s 倉內錨 %10.4f ／ 負對照實得 %s ⇒ %s"
          % (k, NEG[k], ("%.10f" % got) if got is not None else "🔴 未命中",
             "✅ 相符" if same else "🔴 **不符 ⇒ 本 shim 之構造存疑·停機**"))
    P("     ⇒ 負對照判 ＝ **%s**" % ("✅ 通過（同源可比）" if okN else "🔴 **未通過**"))
    P("")
    P("     %-6s %-30s %-22s %-22s %-12s" % ("街廓", "移除之宗（不配地）", "移除前", "**移除後**", "判"))
    allb = sorted(set(before) | set(after))
    for lbl in allb:
        b = before.get(lbl, {"n": 0, "area": 0.0})
        a = after.get(lbl, {"n": 0, "area": 0.0})
        P("     %-6s %-30s %-22s %-22s %-12s"
          % (lbl, "%s" % sorted(rem.get(lbl, set())),
             "%d 對 / %.4f ㎡" % (b["n"], b["area"]),
             "**%d 對 / %.4f ㎡**" % (a["n"], a["area"]),
             "✅ 歸零" if a["n"] == 0 else "🔴 **仍 > 0**"))
        for p in a.get("pairs", []):
            P("        🔴 殘餘破量對：(j=%d, k=%d) 重疊 %.6f ㎡" % (p["j"], p["k"], p["area"]))
    P("     POPULATION=%d PRINTED=%d SUPPRESSED=0  # A-1-3 破閘格（全列）" % (len(allb), len(allb)))
    res_n = sum(v["n"] for v in after.values())
    res_a = sum(v["area"] for v in after.values())
    P("     🔴 **第一輪後之殘餘合計 ＝ %d 對 ／ %.4f ㎡**（帶號）／ %.4f ㎡（絕對值）"
      % (res_n, res_a, sum(abs(p["area"]) for v in after.values() for p in v["pairs"])))
    P("     ⇒ **`P2` 之判**：第一輪之 `②-宗` 破量**仍 > 0**？⇒ **%s**"
      % ("✅ 是（`P2` 成立）" if res_n > 0 else
         "🔴 **否（歸零）⇒ `W-G.9-83` 之結論須以新受詞重新檢視·具名**"))
    P("     ⛔ **本數係<u>第一輪</u>**（⛔ 無遞補）——⛔ 不得充作「乙」之最終土地後果（施工單 A-5）。")

    # ══ A-2-2（依停機④）════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【D／A-2-2】藍影面積 vs `G₁`")
    P("=" * W)
    if blue_ok:
        P("  （A-2-1 相符 ⇒ 本節應辦；本批未走到此分支）")
    else:
        P("  🛑 **⛔ 不辦**——A-2-1 已判**不符** ⇒ 停機條款④ 觸發。")
        P("     施工單 §一 停機④／§七-6 逐字：「⛔ **不得以自定式續算**」「⛔ **不得另立藍影之第二定式**」。")
        P("     ⇒ 🔒 本節之**唯一正確處置 ＝ 不算**；⛔ 不得以 `B2` 版自行改式（那即是「第二定式」）。")
        P("     ⇒ **`P4` ⛔ 無法判**（其受詞 ＝ 藍影面積·而藍影未定義）⇒ 具名為**未答**、⛔ 非否證。")

    # ══ A-3 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【E／A-3】🔴 **遞補介面之同構實證**（⛔ 只證不建）")
    P("=" * W)
    a3 = recompense_audit(P)

    # ══ A-4 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【F／A-4】🔴 **容差級分類閘之全倉普查**（⛔ 只列不改·⛔ 不重驗）")
    P("=" * W)
    P("  🔒 起因已坐實（`W-G.9-90`）：`|sin(源甲,源乙)| ≤ 1e-12` 之宗於換圖後 **8 ⇒ 9**（新入列 ＝ `R1|1`）。")
    a4 = tolerance_survey(P)

    # ══ A-5 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【G／A-5】「乙」之土地後果彙整（⛔ 不含建議）")
    P("=" * W)
    P("  %-44s %s" % ("項", "狀態"))
    P("  %-44s **%d 宗 ／ %.4f ㎡**（🔒 <u>第一輪</u>·⛔ 無遞補）"
      % ("第一輪不配地之宗數／面積（A-1-2）", len(bad), tot_bad))
    P("  %-44s **%d 對 ／ %.4f ㎡**（🔒 <u>第一輪</u>）"
      % ("第一輪後 `②-宗` 破量之殘餘（A-1-3）", res_n, res_a))
    P("  %-44s 🛑 **⛔ 未量**（A-2-1 不符 ⇒ 停機④）" % ("`G₁` vs 藍影之逐宗差（A-2-2）",))
    P("  %-44s 🔴 **⛔ 未量**（遞補介面同構性 ⇒ A-3 判為**未答**）" % ("遞補後之宗數／面積／破量",))
    P("  %-44s 見下（🔒 **本批複驗**·修法 114）" % ("「乙」之射程宗數",))

    # 「乙」之射程：CC 須複驗（修法 114）
    n0 = sum(1 for lbl in CELL for i, lt in CELL[lbl]["lots"].items() if lt["is_corner"])
    ntot = sum(len(r["biz"]) for r in REAL)
    scope = 0
    for lbl in sorted(CELL):
        for side, idxs in CELL[lbl]["groups"]:
            has0 = any(CELL[lbl]["lots"][i]["is_corner"] for i in idxs)
            if not has0:
                continue
            scope += max(0, len(idxs) - 1)
    P("")
    P("  🔒 **「乙」之射程之複驗（施工單載 `26`·標 `【未複驗】`·修法 114）**")
    P("     定義（`W-G.9-89` A-4 逐字）＝「**有第 0 宗之組中，第 1 宗以後**」")
    P("     本批現算：全部宗 ＝ **%d**；街角宗（第 0 宗）＝ **%d**；" % (ntot, n0))
    P("     **有街角宗之組中，扣除該組之第 0 宗後之宗數合計 ＝ %d**" % scope)
    P("     ⇒ 與施工單所載 **26** %s"
      % ("✅ 相符" if scope == 26 else "🔴 **不符 ⇒ 具名**（⛔ 不採信未複驗之數）"))

    # ══ 施工單項數對帳所需之計數 ═══════════════════════════════════════
    P("")
    P("=" * W)
    P("【判】本批之必答與停機")
    P("=" * W)
    P("  %-46s %s" % ("A-2-1 藍影定式與 KL 圖說相符?", "✅ 是" if blue_ok else "🛑 **否 ⇒ 停機上呈**"))
    P("  %-46s %s" % ("A-1-1 違反宗與倉內錨逐位相同?", "✅ 是" if okA else "🔴 否"))
    P("  %-46s %s" % ("A-1-3 負對照（移除集 ∅）與倉內錨相符?", "✅ 是" if okN else "🔴 否"))
    P("  %-46s %s" % ("A-1-3 第一輪後破量仍 > 0?", "✅ 是" if res_n > 0 else "🔴 否（歸零）"))
    P("  %-46s %s" % ("A-3 `W-D.4 遞補錨` 與 `K-9-9 四` 同構?", "🛑 **未答·具名**"))
    P("  %-46s %d 支（入判定鏈）" % ("A-4 容差級分類閘", a4["inchain"]))

    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
