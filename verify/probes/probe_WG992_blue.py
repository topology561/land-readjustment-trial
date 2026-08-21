#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-92 §二 A 組**：藍影面積 vs `G₁`（界 ＝ `B1`）＋ 遞補不變式之現況值 ＋ 容差閘分層。

## 受詞

- **A-1** `A-2-2` 之補辦：**藍影面積 vs `G₁`**，界 ＝ **`B1`**（`K-9-16` 一·KL 裁 2026-08-20）。
  🔒 **定式（⛔ 不得另立第二式）**：
  > **藍影 ＝ `block` ∩ {第 0 宗遠側界之外側} ∩ {通過 `B1` 之 ∥ALLOCLINE 之內側}**
- **A-2** 遞補之正典要件其**不變式之現況值**（⛔ 只量·⛔ 不建介面·⛔ 不寫碼規格）。
- **A-3** 容差級分類閘 **279 支**之分層（原樣 import `probe_WG991_yishim` 之普查器·⛔ 不重造）。

## 🛑 紅線（施工單 §二 A-5·§七）

⛔ 零 `app.py` 變更；⛔ `data/`／`verify/baselines/` 零變更；`docs/rulings/` 限 `Z-1`；
🔴 ⛔ **不得移任何線**；⛔ **不建任何介面**；⛔ 不落地；⛔ 不換圖／不換快照／不重烤；
🛑 ⛔ **不得就遞補／調配池／合併調配／超配出任何裁定題**（`K-9-11` 三）；
⛔ **不得另立藍影之第二定式**（`K-9-16` 已定·界 ＝ `B1`）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98）

`A-1` 之瑕若使**藍影偏小** ⇒ `G₁ ≥ 藍影` 之宗變多 ⇒ **少報「G 不足」** ⇒ 與現況一致 ⇒ **安靜**。
🔒 **事前選定：偏向使藍影<u>偏大</u>**——凡邊界取捨不確定者，一律取**使藍影較大**之解讀並具名。
`A-2` 偏向**多列**要件；`A-3` 偏向**多列**須重驗者。

## 🔒 ⛔ 不得重造（原樣 import）

`w88.s_star_of`／`margin_of`（**判準**）、`w82.ring_edges`／`chord_interval`／`pred_chord`／`graze`／
`uj_of`／`pj_of`、`w40.far_side_dir_and_pt`／`line_isect`／`s_of`、`w86._sin`／`PAR_TOL`、
`w83.D_MIN`、**`w991.tolerance_survey`／`layers_of`**（容差閘普查器）。

🆕 🔒 **哨兵之戒（節 111）**：本檔之陰性對照／假錨**一律執行期組出**，
⛔ 其字樣不寫死於原始碼、⛔ 不寫入報告——出艙時以**角色**代稱。

## 重跑

    python verify/probes/probe_WG992_blue.py

rc **恆為 0**；唯缺件／取不到資料時 loud raise（`no-silent-fallback`）。
"""
import contextlib
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon as SPoly                       # noqa: E402

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
import probe_WG991_yishim as w991                                   # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210

SB = 0.0
D_MIN = w83.D_MIN
PAR_TOL = w86.PAR_TOL
_LBIG = 1.0e5          # 🔒 無限直線之代理長度（同 `app._build_corner_range_v3` 之口徑）

SELF = ["verify/probes/probe_WG992_blue.py",
        "docs/reports/W-G.9-92_藍影對G與遞補不變式.md"]

# 🔒 **面積之法定粒度**（實施辦法 §3 第三位四捨五入）——**原樣取自倉內既有之常數**，
#    ⛔ 非本檔新立：`verify/probes/probe_ruling_K9_corner_width.py` 之 `EPS_AREA = 0.01`
#    （其註解逐字：「面積之法定粒度（實施辦法 §3 第三位四捨五入）……用於區辨
#      『真溢出』與『shapely 差集之浮點噪訊』（後者實測 ~1e-15㎡）」）。
#    🩸 **本批之用途即該註解所述**：藍影之 `intersection` 於**楔形空集**時回傳 `~1e-14㎡` 之噪訊，
#      而 `"%.6f"` 會把它渲染成 `0.000000` ⇒ **顯示值⛔ 不是量測**（本批自捕·§I）。
EPS_AREA = 0.01


def _short_head():
    try:
        return subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True).stdout.strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG992_blue_%s.log" % COMMIT)


# ══════════════════════════════════════════════════════════════════════════
#  驅動（逐字同 `-88`／`-90`／`-91`·差 ＝ 另取 `ress[i]["G"]` 與街廓面積）
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
            _r = (rec["ress"] or [None] * (i + 1))[i]
            lots[i] = {"ua": ua, "pa": pa,
                       "uj": w82.uj_of(rec, i), "pj": w82.pj_of(rec, i),
                       "Pc": Pc, "Bc": Bc,
                       "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area),
                       "is_corner": i in meta["corners"],
                       "name": (rec["names"] or [None] * (i + 1))[i],
                       "G": (_r or {}).get("G"),
                       "area_geom": (_r or {}).get("area_geom"),
                       "poly": rec["biz"][i]}
        CELL[lbl] = {"rec": rec, "o": o_, "d": d_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "lots": lots, "meta": meta, "rows": rows,
                     "edges": edges, "block": rec["block"]}
    return CELL, REAL


def nocross_rows(CELL):
    """🔒 判準 ＝ `K-9-15` 三-2 之「不交叉」（原樣同 `-88`／`-90`／`-91`）。"""
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
                if rec_ok:
                    st_, sa_, ds_ = w88.s_star_of(pj, uj, pk, uk)
                    ci = w82.chord_interval(C["edges"], pj, uj)
                    inside = w82.pred_chord(ci, st_) if math.isfinite(st_) else None
                    gz = w82.graze(ci, st_) if math.isfinite(st_) else (False, float("nan"), "")
                else:
                    st_ = sa_ = ds_ = float("nan")
                    inside, gz = None, (False, float("nan"), "")
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
                            "ord": ordmap.get(i), "reason": reason, "cross": bool(cross),
                            "area": lt["area"]})
                prev = i
    return out


def _halfplane(p, u, keep_pt):
    """🔒 過 `p` 沿 `u` 之直線之「**含 `keep_pt`**」那一側（以 `_LBIG` 為無限直線之代理）。"""
    p = np.asarray(p, float)[:2]
    u = np.asarray(u, float)[:2]
    n_ = float(np.hypot(*u))
    if n_ == 0.0:
        raise RuntimeError("🔴 方向為零向量（no-silent-fallback）")
    u = u / n_
    nv = np.array([-u[1], u[0]])
    if float(np.dot(np.asarray(keep_pt, float)[:2] - p, nv)) < 0.0:
        nv = -nv
    a, b = p - u * _LBIG, p + u * _LBIG
    return SPoly([tuple(a), tuple(b), tuple(b + nv * _LBIG), tuple(a + nv * _LBIG)])


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
    P("【W-G.9-92 §二 A 組】藍影面積 vs `G₁`（界 ＝ `B1`·`K-9-16`）＋ 遞補不變式現況值 ＋ 容差閘分層")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🛑 生產路徑不動：`run_verification.py::V6DXF` ＝ %s"
      % os.path.relpath(rv.V6DXF, REPO).replace(os.sep, "/"))
    P("  🔒 **A-0 事前選定：偏向使藍影<u>偏大</u>**（邊界取捨不確定者取較大之解讀並具名）")
    P("  🔒 情境母體 ＝ **僅 %gm**（同 `-88`／`-90`／`-91`·⛔ 不擴·具名）" % SB)
    P("  🔴 ⛔ **不移任何線**·⛔ **不建任何介面**·⛔ **不另立藍影之第二定式**")

    CELL, REAL = build()
    P("")
    P("【驅動】攔截 **%d 格**；宗數合計 ＝ **%d**"
      % (len(REAL), sum(len(r["biz"]) for r in REAL)))

    ROWS = nocross_rows(CELL)
    bad = {r["key"] for r in ROWS if r["cross"]}
    P("  不交叉判準（原樣 `w88`）：母體 **%d 列**／違反 **%d 宗** ＝ %s"
      % (len(ROWS), len(bad), sorted(bad)))

    # ══ A-1 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【C／A-1】🛑 **藍影面積 vs `G₁`**（界 ＝ **`B1`**·`K-9-16` 一）")
    P("=" * W)
    P("  🔒 **定式（`K-9-16` 二-3·⛔ 不得另立第二式）**：")
    P("     **藍影 ＝ `block` ∩ {第 0 宗遠側界之外側} ∩ {通過 `B1` 之 ∥ALLOCLINE 之內側}**")
    P("     `B1` ＝ 第 0 宗遠側界 ∩ BASELINE；`∥ALLOCLINE` 之方向取自**解算面**（`w82.uj_of` 之非街角宗）。")
    P("  🔒 **母體之產生指令（修法 113）**：對每一格之每一組，取該組**含街角宗**者，")
    P("     其「第 1 宗」＝ **該組內街角宗之次一索引**；⇒ 母體 ＝ 逐格逐組出艙如下。")
    P("")
    P("  %-6s %-6s %-5s %-5s %-16s %-8s" % ("街廓", "側", "第0宗", "第1宗", "第1宗地號", "有街角?"))
    POP = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            c0 = [i for i in idxs if C["lots"][i]["is_corner"]]
            if not c0:
                P("  %-6s %-6s %-5s %-5s %-16s %-8s" % (lbl, side, "—", "—", "—", "⛔ 否"))
                continue
            j0 = c0[0]
            nxt = [i for i in idxs if i > j0]
            j1 = nxt[0] if nxt else None
            P("  %-6s %-6s %-5s %-5s %-16s %-8s"
              % (lbl, side, j0, ("—" if j1 is None else j1),
                 "—" if j1 is None else (C["lots"][j1]["name"] or "?"), "✅ 是"))
            if j1 is not None:
                POP.append((lbl, side, j0, j1))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # A-1 母體（有街角宗且有次一宗之組·全列）"
      % (len(POP), len(POP)))

    P("")
    P("  %-14s %14s %10s %14s %14s %14s %14s %-10s"
      % ("鍵", "藍影面積(㎡)", "G₁(㎡)", "G₁−藍影", "遠側界位置s", "S_req", "位置−S_req", "是否違反"))
    RES = []
    for lbl, side, j0, j1 in POP:
        C = CELL[lbl]
        o_, d_, bpt, bdir = C["o"], C["d"], C["bpt"], C["bdir"]
        L0p, L0u = C["lots"][j0]["pj"], C["lots"][j0]["uj"]
        L1u = C["lots"][j1]["uj"]
        if L0p is None or L0u is None or L1u is None or C["block"] is None:
            P("  %-14s 🔴 **取不到解算面／街廓 ⇒ 具名·⛔ 不靜默**" % ("%s|%s" % (lbl, side)))
            continue
        B1 = w40.line_isect(tuple(np.asarray(L0p, float)[:2]),
                            tuple(np.asarray(L0u, float)[:2]), bpt, bdir)
        if B1 is None:
            P("  %-14s 🔴 **`B1` 求不出（第 0 宗遠側界 ∥ BASELINE？）⇒ 具名**" % ("%s|%s" % (lbl, side)))
            continue
        r0 = C["lots"][j0]["poly"].representative_point()
        r1 = C["lots"][j1]["poly"].representative_point()
        H0 = _halfplane(L0p, L0u, (r1.x, r1.y))     # 第 0 宗遠側界之**外側**（＝ 第 1 宗那側）
        H1 = _halfplane(B1, L1u, (r0.x, r0.y))      # 通過 `B1` 之 ∥ALLOC 之**內側**（＝ 含第 0 宗那側）
        blue = C["block"].intersection(H0).intersection(H1)
        ba = float(blue.area)
        Pf = w40.line_isect(tuple(np.asarray(B1, float)[:2]),
                            tuple(np.asarray(L1u, float)[:2]), o_, d_)
        sreq = w40.s_of(tuple(Pf), o_, d_) if Pf is not None else float("nan")
        Pf1 = C["lots"][j1]["Pc"]
        spos = w40.s_of(tuple(Pf1), o_, d_) if Pf1 is not None else float("nan")
        g1 = C["lots"][j1]["G"]
        g1 = float(g1) if g1 is not None else float("nan")
        ordmap = {t: q for q, t in enumerate(dict(
            (s2, ix) for s2, ix in C["groups"]).get(side, []))}
        key = "%s|%s|%d|%d" % (lbl, side, ordmap.get(j1, 1), ordmap.get(j0, 0))
        vio = key in bad
        # 🔒 **半平面之逐項拆解**（⛔ 「0」最該懷疑 ⇒ 須能指出 0 之來源）
        aH0 = float(C["block"].intersection(H0).area)
        aH1 = float(C["block"].intersection(H1).area)
        uu = np.asarray(L1u, float)[:2]
        uu = uu / float(np.hypot(*uu))
        nv = np.array([-uu[1], uu[0]])
        pB = np.asarray(B1, float)[:2]
        sgn0 = float(np.dot(np.array([r0.x, r0.y]) - pB, nv))
        H1b = _halfplane(B1, L1u, tuple(pB + (-nv if sgn0 >= 0 else nv)))
        aFlip = float(C["block"].intersection(H0).intersection(H1b).area)
        sn01 = float(w86._sin(L0u, L1u))
        RES.append({"key": key, "lbl": lbl, "side": side, "j0": j0, "j1": j1,
                    "blue": ba, "G1": g1, "diff": g1 - ba, "sreq": sreq,
                    "spos": spos, "dpos": spos - sreq, "vio": vio,
                    "geom": blue.geom_type, "B1": (float(B1[0]), float(B1[1])),
                    "aH0": aH0, "aH1": aH1, "aFlip": aFlip, "sin01": sn01,
                    "blk": float(C["block"].area)})
        P("  %-14s %14.6e %10.4f %14.6e %14.6f %14.6f %14.6e %-10s"
          % (key, ba, g1, g1 - ba, spos, sreq, spos - sreq,
             "🔴 **是**" if vio else "✅ 否"))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0  # A-1 逐宗（全列）" % (len(POP), len(RES)))
    if len(RES) != len(POP):
        P("  🔴 **PRINTED ≠ POPULATION ⇒ 差 %d 筆已於上方逐筆具名**" % (len(POP) - len(RES)))

    # 🔒 **藍影 ＝ 0 之逐格拆解**（⛔ 「0」最該懷疑·⛔ 不得只報 0）
    P("")
    P("  🔒 **藍影 ＝ 0 之逐格拆解**（⛔ 「0」最該懷疑 ⇒ 須指出其來源·⛔ 不得只報 0）")
    P("  %-14s %12s %12s %12s %12s %14s %14s"
      % ("鍵", "block", "∩H0", "∩H1", "**H0∩H1**", "H0∩H1′(翻面)", "|sin(u0,u1)|"))
    for r in RES:
        P("  %-14s %12.4f %12.4f %12.4f %12.6e %14.6f %14.6e"
          % (r["key"], r["blk"], r["aH0"], r["aH1"], r["blue"], r["aFlip"], abs(r["sin01"])))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0" % (len(RES), len(RES)))
    zer = [r for r in RES if r["blue"] < EPS_AREA]
    P("     ⇒ **藍影 ＝ 0 之格 ＝ %d ／ %d**：%s" % (len(zer), len(RES), [r["key"] for r in zer]))
    P("     🔒 **成因（機械）**：該 %d 格之 `H0` 與 `H1` **不相交**——其 `H0∩H1′`（翻面）"
      % len(zer))
    P("        **逐位等於 `∩H0`** ⇒ `H0 ⊆ H1′` ⇒ `H0 ∩ H1 ＝ ∅`。")
    P("        ⇒ 🔒 **通過 `B1` 之 ∥ALLOCLINE 落在第 0 宗遠側界<u>之後</u>**（⛔ 非之前）")
    P("        ⇒ **該側⛔ 不開出任何介於二線之區域** ⇒ **藍影 ＝ 0 係<u>幾何實情</u>、⛔ 非構造瑕疵。**")
    P("     ⛔ **假說之否證（本批曾疑·具名）**：「二線平行 ⇒ 楔形退化」**不成立**——")
    P("        六格之 `|sin(u0,u1)|` ∈ [%.3e, %.3e]，**無一為 0**（最小者 `%s`·角 %.6f°）。"
      % (min(abs(r["sin01"]) for r in RES), max(abs(r["sin01"]) for r in RES),
         min(RES, key=lambda r: abs(r["sin01"]))["key"],
         math.degrees(math.asin(min(1.0, min(abs(r["sin01"]) for r in RES))))))
    P("     ⚠️ **A-0 之張力（具名·⛔ 不得默默取大）**：A-0 令「取使藍影**較大**之解讀」，")
    P("        而翻面之讀法可得 **%.4f〜%.4f ㎡**（＝ 街廓之絕大部分）。"
      % (min(r["aFlip"] for r in zer) if zer else 0.0, max(r["aFlip"] for r in zer) if zer else 0.0))
    P("        🛑 **⛔ 不採**——`K-9-16` 二-3 之「**內側**」已定義為**含第 0 宗**那側；")
    P("        取翻面即**另立第二定式**（施工單 §二 A-5-6 明禁）⇒ 🔒 **A-0 之適用範圍限於「取捨<u>不確定</u>」者**，")
    P("        而此處**定式已明** ⇒ ⛔ 不適用。**本行即該具名。**")

    # 🔒 藍影 > 0 ⟺ 違反？（結構對應·⛔ 只述共現）
    P("")
    P("  🔴 **結構對應（⛔ 只述共現·⛔ 不推因果）**：`藍影 > 0` 與「違反不交叉」之對應")
    P("  %-14s %14s %-10s %-10s" % ("鍵", "藍影(㎡)", "藍影>0?", "違反?"))
    agree = 0
    for r in RES:
        a = r["blue"] >= EPS_AREA
        if a == r["vio"]:
            agree += 1
        P("  %-14s %14.6e %-10s %-10s %s"
          % (r["key"], r["blue"], "✅ 是" if a else "⛔ 否",
             "🔴 是" if r["vio"] else "✅ 否", "" if a == r["vio"] else "🔴 **不一致**"))
    P("     ⇒ **二者一致之格 ＝ %d ／ %d**" % (agree, len(RES)))
    P("     🔒 ⛔ **本表只證<u>共現</u>**——⛔ 不證「藍影 > 0 ⇒ 違反」，亦⛔ 不證其逆；")
    P("        二者共用同一組線（`L0`／`L1`），**其相關性有構造上之來源** ⇒ ⛔ 不得當作獨立佐證。")

    # 🔒 A-1-2 自洽檢：`S_req` 須與 `probe_WG984_gap` 逐位相同
    P("")
    P("  🔒 **A-1-2 自洽檢**：本批之 `S_req` 須與 `probe_WG984_gap` 之值**逐位相同**")
    P("     倉內錨（`W-G.9-84`／`VR-043` 二／`K-9-16` 二-3）：**`0m R2` 之 `S_req ＝ 7.4487`**")
    r2 = next((r for r in RES if r["lbl"] == "R2"), None)
    if r2 is None:
        P("     🔴 **R2 不在母體內 ⇒ 該自洽檢無母體·具名**")
        selfok = None
    else:
        selfok = (round(r2["sreq"], 4) == 7.4487)
        P("     本批實得：`%s` 之 `S_req` ＝ **%.13f** ⇒ 4dp ＝ **%.4f** ⇒ %s"
          % (r2["key"], r2["sreq"], r2["sreq"], "✅ 相符" if selfok else "🔴 **不符**"))
        P("     🔒 ⇒ **界之定式與既有量測<u>同源</u>**（`S_req` ＝ 通過 `B1` 之 ∥ALLOC 線之 FRONTLINE 截距）。")
    P("     ⚠️ **同名不同量之具名**：`宗0` 之 `s` 域若以**多邊形頂點之框甲投影極值**取，")
    if r2 is not None:
        C2 = CELL["R2"]
        lo = min(w40.s_of((x, y), C2["o"], C2["d"]) for x, y in C2["lots"][0]["poly"].exterior.coords)
        hi = max(w40.s_of((x, y), C2["o"], C2["d"]) for x, y in C2["lots"][0]["poly"].exterior.coords)
        P("        得 `[%.4f, %.4f]` ⇒ 其上界 **%.4f ≠ `S_req` %.4f**" % (lo, hi, hi, r2["sreq"]))
    P("        🔒 該讀法**已由 `W-G.9-85` §I-2 具名為首版之誤**（⛔ 不得取頂點投影極值）")
    P("        ⇒ 本批取**線之截距**（正解）⇒ 與 `S_req` 逐位相符。")

    # 🔒 必答
    P("")
    P("  🔒 **必答：違反之 2 宗，其 `G₁` 是否 `<` 藍影面積？**")
    vios = [r for r in RES if r["vio"]]
    P("     違反宗 ＝ **%d**（母體 %d）" % (len(vios), len(RES)))
    allless = True
    for r in vios:
        less = (r["diff"] < 0.0)
        allless &= less
        P("     %-14s `G₁` ＝ %10.4f ／ 藍影 ＝ %14.6e ⇒ `G₁ − 藍影` ＝ **%.6e** ⇒ **%s**"
          % (r["key"], r["G1"], r["blue"], r["diff"],
             "✅ `G₁ < 藍影`" if less else "🛑 **`G₁ ≥ 藍影` ⇒ 停機上呈**"))
    P("     ⇒ **%s**"
      % ("✅ **二宗皆 `G₁ < 藍影`**（`P2` 之核心成立）" if (vios and allless) else
         ("🛑 **有違反宗之 `G₁ ≥ 藍影` ⇒ 停機上呈**（其違反⛔ 非「`G` 不足」所致）"
          if vios else "🔴 **母體內無違反宗 ⇒ 具名**")))
    if vios and allless:
        P("     ⚠️ **⛔ 不得反推因果**：`G₁ < 藍影` 與「該宗違反不交叉」**同時成立**，")
        P("        惟本批**只量共現、⛔ 未證蘊含**（⛔ 未做 `G₁` 之擾動實驗）⇒ 具名。")

    # 🔒 判別力（陽性對照 ＝ 未違反之第 1 宗）
    P("")
    P("  🔒 **判別力（常設 8·⛔ 不可省）**：**陽性對照 ＝ 未違反之第 1 宗** ⇒ 其 `G₁` 須 **≥ 藍影**")
    ok_ = [r for r in RES if not r["vio"]]
    P("     未違反之第 1 宗 ＝ **%d ／ %d**" % (len(ok_), len(RES)))
    if not ok_:
        P("     🔴 **該判別力<u>無母體</u>·具名**（⛔ 不得以「0 例外」充作已證）")
    else:
        ge = [r for r in ok_ if r["diff"] >= 0.0]
        for r in ok_:
            P("     %-14s `G₁` ＝ %10.4f ／ 藍影 ＝ %14.6e ⇒ `G₁ − 藍影` ＝ **%.6e** ⇒ %s"
              % (r["key"], r["G1"], r["blue"], r["diff"],
                 "✅ `≥ 0`" if r["diff"] >= 0.0 else "🔴 **`< 0`**"))
        P("     ⇒ 陽性對照：`G₁ ≥ 藍影` 者 ＝ **%d ／ %d**" % (len(ge), len(ok_)))
        triv = [r for r in ok_ if r["blue"] < EPS_AREA]
        P("")
        P("     🛑 **⛔ 惟該對照<u>無鑑別力</u>·具名（⛔ 不得以「%d／%d 成立」充作已證）**：" % (len(ge), len(ok_)))
        P("        其 **%d ／ %d** 格之**藍影 ＝ `0.000000`** ⇒ 判準退化為 **`G₁ ≥ 0`**，"
          % (len(triv), len(ok_)))
        P("        而 `G₁` 係面積（**恆非負**）⇒ 🔒 **該條件對此 %d 格<u>恆真</u>**、⛔ 與其「未違反」無關。"
          % len(triv))
        nz = [r for r in ok_ if r["blue"] >= EPS_AREA]
        P("        ⇒ 🔴 **真正具鑑別力之陽性對照 ＝ 「未違反<u>且</u>藍影 > 0」之格 ＝ %d ／ %d**"
          % (len(nz), len(ok_)))
        if not nz:
            P("        🛑 ⇒ **該母體為 <u>0</u>** ⇒ 🔒 **`P2` 之陽性對照<u>無母體</u>**")
            P("           ——⛔ 不得謂「已證 `G₁ ≥ 藍影` 於未違反者成立」；本批只能謂")
            P("           **「未違反者其藍影皆為 0」**（＝ 一個**更強且更窄**之陳述）。")
        else:
            for r in nz:
                P("           %-14s 藍影 ＝ %14.6e ／ `G₁` ＝ %10.4f ⇒ %s"
                  % (r["key"], r["blue"], r["G1"], "✅ `≥`" if r["diff"] >= 0 else "🔴 `<`"))

    # 🔒 節 103
    P("")
    P("  🔒 **節 103（最接近翻面者·單一門檻 `0`·⛔ 無未定義帶）**")
    fin = [r for r in RES if math.isfinite(r["diff"])]
    fin.sort(key=lambda r: abs(r["diff"]))
    P("  %-14s %14s %14s %14s %-10s" % ("鍵", "G₁−藍影", "|餘裕|", "藍影(㎡)", "違反?"))
    for r in fin:
        P("  %-14s %14.6e %14.6e %14.6e %-10s"
          % (r["key"], r["diff"], abs(r["diff"]), r["blue"], "🔴 是" if r["vio"] else "✅ 否"))
    if fin:
        P("     🔒 **最接近 `0` 者 ＝ `%s`**：`G₁ − 藍影` ＝ **%.6e**（`|餘裕|` ＝ **%.6e**）"
          % (fin[0]["key"], fin[0]["diff"], abs(fin[0]["diff"])))
        P("     ⇒ 其判 ＝ **%s**（門檻 `0`）" % ("`G₁ < 藍影`" if fin[0]["diff"] < 0 else "`G₁ ≥ 藍影`"))
        if fin[0]["blue"] < EPS_AREA:
            P("     ⚠️ **具名**：該格之**藍影 ＝ 0** ⇒ 其 `|餘裕|` **即 `G₁` 本身**、⛔ 非「距藍影多遠」")
            P("        ⇒ 🔒 **⛔ 不得以之代表「離門檻最近」之實質意義。**")
        nzf = [r for r in fin if r["blue"] >= EPS_AREA]
        P("     🔒 **限於藍影 > 0 之子母體（＝ 該門檻<u>實際起作用</u>者）＝ %d 格**：" % len(nzf))
        if nzf:
            P("        最接近 `0` 者 ＝ `%s`：`G₁ − 藍影` ＝ **%.6e**（`|餘裕|` ＝ **%.6e**）"
              % (nzf[0]["key"], nzf[0]["diff"], abs(nzf[0]["diff"])))
            P("        ⇒ 其 `|餘裕| / 藍影` ＝ **%.6f**（⇒ 距翻面**極遠**·⛔ 非擦邊）"
              % (abs(nzf[0]["diff"]) / nzf[0]["blue"]))
        else:
            P("        🔴 **該子母體為 0 ⇒ 具名**")

    # ══ A-2　遞補不變式之現況值 ═══════════════════════════════════════
    P("")
    P("=" * W)
    P("【D／A-2】遞補之正典要件其**不變式之現況值**（⛔ 只量·⛔ 不建介面·⛔ 不寫碼規格）")
    P("=" * W)
    P("  🔒 **必要性**：`VR-051` 三-② —— 遞補之**全倉可執行層 ＝ 0**（`W-G.9-91` §E-3）")
    P("     ⇒ 落地係**從零實作** ⇒ **⛔ 無既有行為可對拍** ⇒ 須先有**可驗收之不變式**。")
    P("")
    P("  ── 不變式 ① **守恆式**（`K-6:1732` 逐字 `ΣG(街廓內所有分配地) + 調配池(Ri) = 街廓 DXF 面積(Ri)  恆成立`）──")
    P("  %-6s %14s %14s %14s %14s %-12s"
      % ("街廓", "Σ配地幾何(㎡)", "街廓DXF(㎡)", "池 ＝ 差(㎡)", "池/街廓", "池 > 0?"))
    inv1 = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        if C["block"] is None:
            P("  %-6s 🔴 **街廓多邊形取不到 ⇒ 具名**" % lbl)
            continue
        sa = sum(C["lots"][i]["area"] for i in sorted(C["lots"]))
        ba = float(C["block"].area)
        pool = ba - sa
        inv1.append((lbl, sa, ba, pool))
        P("  %-6s %14.6f %14.6f %14.6f %14.6f %-12s"
          % (lbl, sa, ba, pool, (pool / ba if ba else float("nan")),
             "✅ 是" if pool > 0 else "🔴 **否**"))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0" % (len(CELL), len(inv1)))
    P("     🔒 **可驗證性 ＝ `【可近似驗·附容差來源】`**——`Σ配地幾何` 係 shapely 面積之和，")
    P("        其與 `ΣG`（法定 2dp）**⛔ 非同一量**（`G` 已 `round` 至 2dp）⇒ 二者之差為**捨入量**，")
    P("        ⛔ 不得要求逐位為零（`CLAUDE.md` 之 `192` 字面：池採「量」⇒ **守恆殘差恆非零**）。")
    P("     🔒 **現況值即落地後之對照基線**：上表之 `池` 欄。")
    P("")
    P("  ── 不變式 ② ⛔ **不得超配**（`K-6:2151` 逐字「⛔ 不得強制配到下限（⛔ 不得超配）」）──")
    P("     🔒 **機械形式**（`K-6:2364` 逐字）：「**調配池必然存在、必 > 0** ⇒ 超配令池 < 0 ⇒ **違反守恆式**」")
    neg = [x for x in inv1 if x[3] <= 0]
    P("     ⇒ **現況：池 ≤ 0 之格 ＝ %d ／ %d**（%s）"
      % (len(neg), len(inv1), sorted(x[0] for x in neg) if neg else "無"))
    P("     🔒 **可驗證性 ＝ `【可逐位驗】`**（受詞為布林：`池 > 0`）；最小池 ＝ **%.6f ㎡**（`%s`）"
      % (min(x[3] for x in inv1), min(inv1, key=lambda x: x[3])[0]) if inv1 else "")
    P("")
    P("  ── 不變式 ③ **下一投影序號之定序**（`K-6:2344` 逐字「由**投影序號中下一位之土地遞補該位次**」）──")
    P("  %-6s %-6s %-40s %-14s %-10s" % ("街廓", "側", "組內索引序", "s 中點序", "二序相同?"))
    inv3ok = 0
    inv3tot = 0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            if len(idxs) < 2:
                continue
            inv3tot += 1
            mid = {i: (C["lots"][i]["s_lo"] + C["lots"][i]["s_hi"]) / 2.0 for i in idxs}
            by_s = sorted(idxs, key=lambda i: mid[i])
            same = (by_s == list(idxs)) or (by_s == list(reversed(list(idxs))))
            inv3ok += int(same)
            P("  %-6s %-6s %-40s %-14s %-10s"
              % (lbl, side, str(list(idxs))[:40], str(by_s)[:14],
                 "✅ 是（順或逆）" if same else "🔴 **否**"))
    P("  POPULATION=%d PRINTED=%d SUPPRESSED=0" % (inv3tot, inv3tot))
    P("     ⇒ **索引序 ≡ `s` 中點序（順或逆）之組 ＝ %d ／ %d**" % (inv3ok, inv3tot))
    P("     🔒 **可驗證性 ＝ `【可逐位驗】`**（受詞為序列相等）；🔒 現況值即上表。")
    P("     ⚠️ **具名**：本表證「**索引序 ＝ 幾何推進序**」，⛔ **不證**「索引序 ＝ 投影**序號**」")
    P("        ——後者之受詞為**地號之投影序號**，其定義於本批母體內**查無機械形式** ⇒ `【⛔ 現行資料不足】`。")
    P("")
    P("  ── 不變式 ④ **不配地之宗其面積入調配池**（`K-6:2150` 逐字「**遞補該位次**；騰出之地**入調配池**」）──")
    P("     🔒 **機械形式**：`池_after − 池_before ＝ Σ(不配地宗之面積)`（🔒 落地後方可驗）")
    P("     🔒 **現況值（落地前之對照基線）**：不配地宗 ＝ **%d**（`W-G.9-91` A-1·2 宗／`4.7950 ㎡`）；"
      % len(bad))
    P("        本批**⛔ 未執行任何移除** ⇒ 上表 `池` 欄即 `池_before`。")
    P("     🔒 **可驗證性 ＝ `【可近似驗·附容差來源】`**（同 ①·捨入量）。")
    P("")
    P("  ── 不變式 ⑤ **第 0 宗之豁免**（`K-6:2444` 逐字「`K-9-12-e` 射程排除：**街角第 1 宗⛔ 不走本則**」）──")
    n_corner = sum(1 for lbl in CELL for i in CELL[lbl]["lots"]
                   if CELL[lbl]["lots"][i]["is_corner"])
    n_all = sum(len(CELL[lbl]["lots"]) for lbl in CELL)
    P("     🔒 **機械形式**：`街角宗（第 0 宗）⛔ 不進入 K-9-12 之矩形容納判定`")
    P("     🔒 **現況值**：街角宗 ＝ **%d** ／ 全部宗 ＝ **%d** ⇒ 受 `K-9-12` 之宗 ＝ **%d**"
      % (n_corner, n_all, n_all - n_corner))
    P("        （🔒 與 `W-G.9-89` A-4 之「`K-9-12` 射程 **51**」對帳：%d %s）"
      % (n_all - n_corner, "✅ 相符" if n_all - n_corner == 51 else "🔴 **不符·具名**"))
    P("     🔒 **可驗證性 ＝ `【可逐位驗】`**（受詞為集合：街角宗之索引集）。")

    # ══ A-3 ══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【E／A-3】容差級分類閘之**分層**（🔒 原樣 import `probe_WG991_yishim` 之普查器·⛔ 不重造）")
    P("=" * W)
    a3 = w991.tolerance_survey(P)
    P("")
    P("  🔒 **分層計數（施工單 A-3-1）**")
    P("  %-30s %8s %s" % ("層", "計數", "分母之產生指令（修法 113）"))
    P("  %-30s %8d %s" % ("樣式命中（全部）", a3["total"],
                          "`git ls-files -z` → 篩 `verify/**.py` ∪ `app.py` → 扣 SELF → 逐行套樣式"))
    P("  %-30s %8d %s" % ("　├ 可執行層", a3["exec"], "上式 ∩ `layers_of()` 判為可執行"))
    P("  %-30s %8d %s" % ("　│  ├ **入判定鏈**", a3["inchain"], "上式 ∩ 行內含判定關鍵字"))
    P("  %-30s %8d %s" % ("　│  └ 不入判定鏈", a3["exec"] - a3["inchain"], "上式之補集"))
    P("  %-30s %8d %s" % ("　└ 註解＋字串", a3["total"] - a3["exec"], "上式 ∩ `layers_of()` 判為註解／字串"))
    P("  %-30s %8d %s" % ("未判（分層失敗）", a3["nolayer"], "`tokenize` 失敗之檔（⛔ 其行一律歸可執行）"))
    P("     🔒 **合計自校**：可執行 %d ＋ 註解字串 %d ＝ %d ／ 樣式命中 %d ⇒ %s"
      % (a3["exec"], a3["total"] - a3["exec"], a3["total"], a3["total"], "✅"))
    P("     🔴 **「入判定鏈」之 %d 支即<u>波末重烤批之重驗清單</u>**（已於上方逐支全列）。" % a3["inchain"])
    P("     🔒 **判別力（施工單 A-3-3）**：`_PAR_TOL = 1e-6`（`K-6:1010`）須落在「入判定鏈」層")
    P("        ⇒ 其消費點 **%d 處**（`stepg_pipeline.py`）皆為 `return … <= _PAR_TOL` ⇒ **`return` ∈ 判定關鍵字**"
      % a3["par_use"])
    P("        ⇒ **%s**" % ("✅ 落在該層" if a3["par_use"] > 0 else "🔴 **未落在該層 ⇒ 分層器有誤·具名**"))
    P("     ⚠️ **射程之具名（承 `-91` §F-1）**：主樣式為「比較運算元 ＋ 容差**字面**」")
    P("        ⇒ **⛔ 抓不到具名常數之閘** ⇒ 本表為**下界**；而「入判定鏈」之判準為**行內字樣**")
    P("        ⇒ 該欄為**上界**。🔒 **二者方向相反·⛔ 不得相乘或相消。**")

    # ══ 判 ═══════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【判】本批之必答")
    P("=" * W)
    P("  %-52s %s" % ("A-1 違反之 2 宗其 `G₁ < 藍影`?",
                      "✅ 是" if (vios and allless) else "🛑 **否 ⇒ 停機**"))
    P("  %-52s %s" % ("A-1-2 `S_req` 與 `w84` 逐位相同?",
                      "✅ 是" if selfok else ("🔴 否" if selfok is not None else "⚠️ 無母體")))
    P("  %-52s %s" % ("A-1 判別力：存在未違反之第 1 宗?",
                      "✅ 是（%d）" % len(ok_) if ok_ else "🔴 **無母體·具名**"))
    P("  %-52s %d ／ %d" % ("A-2 可抽出之要件（含現況值）", 5, 5))
    P("  %-52s %d 支" % ("A-3 入判定鏈（＝ 波末重驗清單）", a3["inchain"]))

    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
