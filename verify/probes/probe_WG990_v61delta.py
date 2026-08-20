#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""**W-G.9-90 §二 A 組**：以 `V6_1.dxf` 跑**現行之新判定**，逐項與 `V6.dxf` 對照。

## 受詞（施工單 `W-G.9-90` §二 A-1）

`W-G.9-77` **之後**才出現之判定，於 `V6_1` 下之值，逐項與 `V6` 並列 ＋ `Δ`：

| # | 量 | `V6` 之倉內錨 |
|---|---|---|
| 1 | `∠(用, ALLOC)` | `4.3220°`（`R2`／`R5`）等 |
| 2 | 弦區間 `[λ_a, λ_b]` | `0m R2` ＝ `[0.0000, 44.9154]` |
| 3 | `s*`（權威源） | — |
| 4 | 🔴 `K-9-9 二`（**不交叉**）之違反宗數與名單 | **2 宗**：`R2左第1宗` `3.8082`／`R5左第1宗` `0.9867` |
| 5 | `S_req` | `0m R2` ＝ `7.4487` |
| 6 | `0m R3` 之餘裕 | `3.502697 m` |
| 7 | 🔴 `②-宗` 破量 | `R2` `45.9766 ㎡`／`R5` `56.3293 ㎡` |

## 🛑 紅線（施工單 §零／§二 A-5／§七）

- ⛔ **不換圖**（`K-6:1651`）／⛔ **不換快照**（`K-6:1753`·`U-K8-1` ＝ 乙）／⛔ **不重烤**（`K-6:237`／`:1057`）。
- ⛔ **不得改 `verify/run_verification.py::V6DXF`**——`V6_1` **只在本探針行程內**作為輸入。
  手法 ＝ **就地覆寫 `rv.V6DXF`**，係 `W-G.5_K8-段六` §四**已行之於 `probe_ruling_K9_corner_width.py`
  之同一手法**（⛔ 非本檔新創）：不寫回任何檔案、不影響他行程、生產路徑預設仍讀 `data/V6.dxf`。
- ⛔ 零 `app.py` 變更；⛔ `data/`／`docs/rulings/`／`verify/baselines/` 零變更。

## 🔒 A-0　錯誤方向之**事前選定**（施工單 §二 A-0·節 98）

本檔欲答「換圖會不會翻動判定」。其瑕**若使變動看起來更小** ⇒ 結論為「不翻動」⇒ **安靜**，
且落地驗證將在**未經確認**之前提下進行 ⇒ 代價落在波末重烤那一批。
🔒 **事前選定：偏向<u>放大變動</u>**——

- (甲) 母體**取超集**：`∠`／弦區間／`s*` 一律出艙**全部**宗／對，⛔ 非只出艙施工單所舉之格；
- (乙) 凡任一判定翻動，一律判為**「翻動」**，⛔ 不得以「量級很小」淡化；
- (丙) 數值取捨不確定者，取**使 `|Δ|` 較大**之解讀並具名；
- (丁) 集合比對取**對稱差**（⛔ 非只比計數）——**數目相同⛔ 不蘊含母體相同**
  （`VR-048` 記功一：`-87` 之 25 宗「同數而換 7 宗」）。

## 🔒 ⛔ 不重造（一律原樣 import）

`w81.analyse_cell`／`spy_solve`／`spy_pool`／`faces_of`／`_u`／`_cross`、
`w82.ring_edges`／`chord_interval`／`pred_chord`／`graze`／`uj_of`／`pj_of`、
`w40.far_side_dir_and_pt`／`line_isect`／`s_of`、`w86._sin`／`PAR_TOL`、
`w88.s_star_of`／`margin_of`。

🔒 **驅動（`main()` 內之 harvest→pipeline→CELL 構造）⛔ 不可 import**——其寫在各檔 `main()` 內；
本檔沿 `-88` 對 `-87` 之同一體例**重寫驅動、逐字具名其差**（差 ＝ 僅 `rv.V6DXF` 之值 ＋ 多量 `∠`／`②-宗`）。

🩸 **`S_req`（第 5 項）之具名例外**：其**全稱式**與所需之 `groups_of`／`A2` 母體
**皆為 `w84.main()` 內之巢狀定義**（`probe_WG984_gap.py` 之 `def groups_of` 係縮排於 `main()` 內）
⇒ **⛔ 不可 import**，而重寫之即為施工單所禁之**重造**。
⇒ 🔒 本檔改以**原樣執行 `w84.main()`**（各 DXF 各一次）取其出艙值，
   **Δ 之精度 ＝ 該 log 之列印精度 `4dp`（`1e-4 m`）**——⛔ **不偽稱 `ulp` 級**。
   🔒 判別力聲明：`GB-16` 所載之變動為 `45m` 處 `7.11mm` ＝ `7.11e-3 m` ⇒ **較 `1e-4 m` 粗 71 倍**
   ⇒ 該精度**足以偵測翻動**；其不足僅在「Δ 之尾數」，⛔ 不在「有無 Δ」。

## 重跑

    python verify/probes/probe_WG990_v61delta.py

內部模式（由上式自行以 subprocess 呼叫·⛔ 非供人工直呼）：

    python verify/probes/probe_WG990_v61delta.py --measure <dxf> <json_out>
    python verify/probes/probe_WG990_v61delta.py --asprobe <mod> <dxf> <log_out>

🔒 **三輪 subprocess 隔離**：`V6` ／ `V6_1` ／ **`V6` 再一次**（判別力·常設 8）。
   隔離之由：`harvest()` 係 `exec(app.py)`，同行程重入之等冪性**未經證**
   ⇒ ⛔ 不得以同行程三呼替代（否則 `Δ ＝ 0` 可能係狀態殘留所致之**假綠**）。

rc **恆為 0**；唯缺件／取不到資料時 loud raise（`no-silent-fallback`）。
"""
import contextlib
import io
import json
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

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

import shapely                                                      # noqa: E402

import probe_WG981_scope as w81                                     # noqa: E402
import probe_WG982_chord as w82                                     # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402
import probe_WG986_oldjudge as w86                                  # noqa: E402
import probe_WG988_nocross as w88                                   # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210

SB = 0.0            # 🔒 情境母體 ＝ 僅 0m（同 `-88` 之 `SB`·⛔ 不擴·具名）
D_MIN = 2           # 🔒 `②-宗` 之非相鄰門檻（原樣同 `w83.D_MIN`）
PAR_TOL = w86.PAR_TOL

V6 = os.path.join(REPO, "data", "V6.dxf")
V61 = os.path.join(REPO, "data", "V6_1.dxf")


def _short_head():
    try:
        return subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True).stdout.strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG990_v61delta_%s.log" % COMMIT)


def _md5(path):
    import hashlib
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


# ══════════════════════════════════════════════════════════════════════════
#  量測（單一 DXF·單一行程）
# ══════════════════════════════════════════════════════════════════════════
def measure(dxf_path):
    """🔒 驅動同 `-88` `main()`（逐字具名之差：`rv.V6DXF` 之值 ＋ 多量 `∠`／`②-宗`）。

    回 dict：全部量之**原生 float**（⛔ 不四捨五入·JSON 以 `repr` 往返）。
    """
    if not os.path.exists(dxf_path):
        raise RuntimeError("🔴 DXF 不存在：%s（no-silent-fallback）" % dxf_path)

    # 🛑 **只在本行程內**覆寫（⛔ 不寫回 `run_verification.py`·段六 §四之同一手法）
    rv.V6DXF = os.path.abspath(dxf_path)

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

    out = {"dxf": os.path.relpath(rv.V6DXF, REPO).replace(os.sep, "/"),
           "md5": _md5(rv.V6DXF),
           "n_cells": len(REAL),
           "angle": {}, "chord": {}, "sstar": {},
           "rows": [], "bad": [], "margin": {}, "zong2": {},
           "env": {"shapely": shapely.__version__,
                   "geos": str(shapely.geos_version),
                   "numpy": np.__version__}}

    # ── 建 CELL（逐字同 `-88`）────────────────────────────────────────────
    CELL = {}
    for rec in REAL:
        lbl = rec["label"]
        fl, bl = FL.get(lbl) or {}, BL.get(lbl) or {}
        if not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            continue
        o_ = tuple(float(x) for x in fl["p1"])
        d_ = tuple(np.asarray(rec["d_hat"], float)[:2])
        n_ = (-d_[1], d_[0])
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
        edges, degen = w82.ring_edges(list(rec["block"].exterior.coords)) \
            if rec["block"] is not None else (None, None)
        lots = {}
        for i in range(len(rec["biz"])):
            ua, pa = w40.far_side_dir_and_pt(rec["biz"][i], d_)
            uj = w82.uj_of(rec, i)
            pj = w82.pj_of(rec, i)
            Pc = Bc = None
            if ua is not None:
                Pc = w40.line_isect(tuple(pa), tuple(ua), o_, d_)
                Bc = w40.line_isect(tuple(pa), tuple(ua), bpt, bdir)
            lots[i] = {"ua": ua, "pa": pa, "uj": uj, "pj": pj, "Pc": Pc, "Bc": Bc,
                       "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area), "is_corner": i in meta["corners"]}
        CELL[lbl] = {"rec": rec, "o": o_, "d": d_, "n": n_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "lots": lots, "meta": meta, "rows": rows,
                     "edges": edges}

    # ── 量 1：`∠(用, ALLOC)`（🔒 A-0(甲) 超集：**逐宗**·⛔ 非只六格）──────────
    #    式 ＝ `w977` 之 `_ang(alloc_used, rec["alloc"])`；`alloc_used` 取自
    #    `w81.SOLVE[id(res)]["alloc_used"]`（＝ 生產碼之 `_alloc_dir_used` 回值）。
    def _ang(u, v):
        if u is None or v is None:
            return float("nan")
        a = np.asarray(u, float)[:2]
        b = np.asarray(v, float)[:2]
        na, nb = float(np.hypot(*a)), float(np.hypot(*b))
        if na == 0.0 or nb == 0.0:
            return float("nan")
        c = float(np.dot(a, b)) / (na * nb)
        return math.degrees(math.acos(max(-1.0, min(1.0, abs(c)))))

    for rec in REAL:
        lbl = rec["label"]
        for i in range(len(rec.get("names") or [])):
            r = (rec["ress"] or [None] * (i + 1))[i]
            info = w81.SOLVE.get(id(r)) if r is not None else None
            au = (info or {}).get("alloc_used")
            out["angle"]["%s|%d" % (lbl, i)] = _ang(au, rec["alloc"])

    # ── 量 2：弦區間（🔒 A-0(甲) 超集：**逐宗 j**·⛔ 非只第 0 宗）────────────
    for lbl in sorted(CELL):
        C = CELL[lbl]
        if C["edges"] is None:
            continue
        for j in range(len(C["rec"]["biz"])):
            pj, uj = w82.pj_of(C["rec"], j), w82.uj_of(C["rec"], j)
            if pj is None or uj is None:
                continue
            ci = w82.chord_interval(C["edges"], pj, uj)
            out["chord"]["%s|%d" % (lbl, j)] = [ci["lam_a"], ci["lam_b"], bool(ci["empty"])]

    # ── 量 3：`s*`（🔒 權威源 ＝ 解算面·母體 ＝ `analyse_cell` 之全部 ok 對）──
    for lbl in sorted(CELL):
        for r in CELL[lbl]["rows"]:
            if not r.get("ok"):
                continue
            out["sstar"]["%s|%d|%d" % (lbl, r["j"], r["k"])] = r["s_star"]

    # ── 量 4／6：`K-9-9 二`（不交叉）之重判 ＋ 餘裕（逐字同 `-88` A-1）────────
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
                    mg, mgnm = w88.margin_of(ci, st_)
                else:
                    st_ = sa_ = ds_ = float("nan")
                    ci = None
                    inside = None
                    gz = (False, float("nan"), "")
                    mg, mgnm = float("nan"), ""
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
                key = "%s|%s|%s|%s" % (lbl, side, ordmap.get(i), ordmap.get(prev))
                row = {"key": key, "lbl": lbl, "side": side, "i": i, "prev": prev,
                       "ord": ordmap.get(i), "ord_prev": ordmap.get(prev),
                       "s_star": st_, "lam_a": ci["lam_a"] if ci else float("nan"),
                       "lam_b": ci["lam_b"] if ci else float("nan"),
                       "margin": mg, "margin_at": mgnm, "sin": sn,
                       "reason": reason, "cross": bool(cross), "area": lt["area"],
                       "inscope": bool(math.isfinite(sn) and sn > PAR_TOL)}
                out["rows"].append(row)
                out["margin"][key] = mg
                if cross:
                    out["bad"].append({"key": key, "area": lt["area"],
                                       "s_star": st_, "reason": reason})
                prev = i

    # ── 量 8：`|sin(源甲, 源乙)|` 逐宗（🔴 **CC 自補**·⛔ 施工單未令）────────────
    #    由 ＝ `w84` A-1 之**判別力對照組**母體（`|sin| ≤ 1e-12` 之宗）於 `V6 ⇒ V6_1`
    #      由 **8 ⇒ 9**（本批實測），而 `w84` **只印計數、不印名單**
    #      ⇒ ⛔ 無從指認**是哪一宗跨過門檻** ⇒ 本量補之。
    #    源甲 ＝ `w40.far_side_dir_and_pt`（`lots[i]["ua"]`）；
    #    源乙 ＝ `w82.uj_of`（解算面·`lots[i]["uj"]`）；式 ＝ `w86._sin`（⛔ 不另立）。
    out["sin2"] = {}
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for i, lt in sorted(C["lots"].items()):
            if lt["ua"] is None or lt["uj"] is None:
                continue
            out["sin2"]["%s|%d" % (lbl, i)] = float(w86._sin(lt["ua"], lt["uj"]))

    # ── 量 7：`②-宗` 破量（逐字同 `w83` A-2-2·`d ≥ D_MIN`）──────────────────
    for rec in REAL:
        lbl = rec["label"]
        if rec["block"] is None:
            continue
        meta, rows = w81.analyse_cell(rec, strip_axis)
        edges, _diag = w82.ring_edges(list(rec["block"].exterior.coords))
        cache = {}
        pairs = []
        for r in rows:
            if not r.get("ok") or r["d"] < D_MIN:
                continue
            j = r["j"]
            if j not in cache:
                pj, uj = w82.pj_of(rec, j), w82.uj_of(rec, j)
                cache[j] = None if (pj is None or uj is None) \
                    else w82.chord_interval(edges, pj, uj)
            ci = cache[j]
            if ci is None:
                continue
            if w82.pred_chord(ci, r["s_star"]):
                a = float(rec["biz"][j].intersection(rec["biz"][r["k"]]).area)
                pairs.append({"j": j, "k": r["k"], "area": a})
        if pairs:
            out["zong2"][lbl] = {"n": len(pairs),
                                 "area": sum(p["area"] for p in pairs),
                                 "pairs": [[p["j"], p["k"], p["area"]] for p in pairs]}
    return out


# ══════════════════════════════════════════════════════════════════════════
#  比較器
# ══════════════════════════════════════════════════════════════════════════
def _ulp_of(a, b):
    m = max(abs(a), abs(b))
    if not math.isfinite(m) or m == 0.0:
        return float("nan")
    return math.ulp(m)


def _d(a, b):
    """回 (Δ, Δ/ulp)。`nan` 對 `nan` ⇒ Δ ＝ 0（🔒 具名：二者皆未定義 ＝ 未變動）。"""
    if a is None or b is None:
        return float("nan"), float("nan")
    an, bn = (not math.isfinite(a)), (not math.isfinite(b))
    if an and bn:
        return 0.0, 0.0
    if an != bn:
        return float("inf"), float("inf")
    dd = b - a
    u = _ulp_of(a, b)
    return dd, (dd / u if (u == u and u != 0.0) else float("nan"))


def compare(P, A, B):
    """逐量並列 ＋ Δ。回 dict：每項之 (max|Δ|, 翻動?)。"""
    res = {}

    # ── 量 1 `∠(用, ALLOC)` ────────────────────────────────────────────
    P("")
    P("  ── 量 1　`∠(用, ALLOC)`（度）──　🔒 A-0(甲) 母體 ＝ **逐宗超集**")
    ka, kb = set(A["angle"]), set(B["angle"])
    P("     母體：%s ＝ %d ／ %s ＝ %d；**對稱差 ＝ %d**（A-0(丁)）"
      % (A["dxf"], len(ka), B["dxf"], len(kb), len(ka ^ kb)))
    if ka ^ kb:
        P("     🔴 **母體本身變動** ⇒ 逐鍵具名：%s" % sorted(ka ^ kb))
    mx, mxk, nz = 0.0, "", 0
    P("     %-12s %18s %18s %14s %14s" % ("鍵", "V6", "V6_1", "Δ", "Δ/ulp"))
    for k in sorted(ka & kb):
        dd, du = _d(A["angle"][k], B["angle"][k])
        if dd != 0.0:
            nz += 1
            P("     %-12s %18.12f %18.12f %14.6e %14.3e"
              % (k, A["angle"][k], B["angle"][k], dd, du))
        if abs(dd) > mx:
            mx, mxk = abs(dd), k
    P("     ⇒ **有 Δ 之鍵 ＝ %d ／ %d**；極大 `|Δ|` ＝ **%.6e°**（%s）" % (nz, len(ka & kb), mx, mxk))
    res["1_angle"] = {"max": mx, "nz": nz, "pop": len(ka & kb), "symdiff": len(ka ^ kb)}

    # ── 量 2 弦區間 ────────────────────────────────────────────────────
    P("")
    P("  ── 量 2　弦區間 `[λ_a, λ_b]`（m）──　🔒 A-0(甲) 母體 ＝ **逐宗超集**")
    ka, kb = set(A["chord"]), set(B["chord"])
    P("     母體：%d ／ %d；**對稱差 ＝ %d**" % (len(ka), len(kb), len(ka ^ kb)))
    mx, mxk, nz, emp = 0.0, "", 0, 0
    P("     %-12s %18s %18s %14s %14s %-6s" % ("鍵", "V6", "V6_1", "Δ", "Δ/ulp", "端"))
    for k in sorted(ka & kb):
        for t, nm in ((0, "λ_a"), (1, "λ_b")):
            dd, du = _d(A["chord"][k][t], B["chord"][k][t])
            if dd != 0.0:
                nz += 1
                if nz <= 40:
                    P("     %-12s %18.12f %18.12f %14.6e %14.3e %-6s"
                      % (k, A["chord"][k][t], B["chord"][k][t], dd, du, nm))
            if abs(dd) > mx:
                mx, mxk = abs(dd), "%s.%s" % (k, nm)
        if bool(A["chord"][k][2]) != bool(B["chord"][k][2]):
            emp += 1
            P("     🔴 %-12s `empty` 翻動：%s ⇒ %s" % (k, A["chord"][k][2], B["chord"][k][2]))
    if nz > 40:
        P("     …（另 %d 端有 Δ·**未列**·🔒 母體以下開計數為準）" % (nz - 40))
    P("     ⇒ **有 Δ 之端 ＝ %d ／ %d**；極大 `|Δ|` ＝ **%.6e m**（%s）；`empty` 翻動 ＝ **%d**"
      % (nz, 2 * len(ka & kb), mx, mxk, emp))
    res["2_chord"] = {"max": mx, "nz": nz, "pop": 2 * len(ka & kb),
                      "symdiff": len(ka ^ kb), "flip": emp}

    # ── 量 3 `s*` ──────────────────────────────────────────────────────
    P("")
    P("  ── 量 3　`s*`（m·權威源 ＝ 解算面）──")
    ka, kb = set(A["sstar"]), set(B["sstar"])
    P("     母體：%d 對 ／ %d 對；**對稱差 ＝ %d**" % (len(ka), len(kb), len(ka ^ kb)))
    mx, mxk, nz = 0.0, "", 0
    P("     %-14s %18s %18s %14s %14s" % ("鍵", "V6", "V6_1", "Δ", "Δ/ulp"))
    for k in sorted(ka & kb):
        dd, du = _d(A["sstar"][k], B["sstar"][k])
        if dd != 0.0:
            nz += 1
            if nz <= 40:
                P("     %-14s %18.12f %18.12f %14.6e %14.3e"
                  % (k, A["sstar"][k], B["sstar"][k], dd, du))
        if abs(dd) > mx:
            mx, mxk = abs(dd), k
    if nz > 40:
        P("     …（另 %d 對有 Δ·**未列**·🔒 母體以下開計數為準）" % (nz - 40))
    P("     ⇒ **有 Δ 之對 ＝ %d ／ %d**；極大 `|Δ|` ＝ **%.6e m**（%s）" % (nz, len(ka & kb), mx, mxk))
    res["3_sstar"] = {"max": mx, "nz": nz, "pop": len(ka & kb), "symdiff": len(ka ^ kb)}

    # ── 量 4 `K-9-9 二`（不交叉）──────────────────────────────────────
    P("")
    P("  ── 量 4　🔴 `K-9-9 二`（**不交叉**）之違反宗數與名單 ──　🔒 **現行有效之土地結論**")
    sa = set(x["key"] for x in A["bad"])
    sb = set(x["key"] for x in B["bad"])
    aa = sum(x["area"] for x in A["bad"])
    ab = sum(x["area"] for x in B["bad"])
    P("     `V6`  ：違反 **%d 宗**／面積合計 **%.4f ㎡**　名單 ＝ %s" % (len(sa), aa, sorted(sa)))
    P("     `V6_1`：違反 **%d 宗**／面積合計 **%.4f ㎡**　名單 ＝ %s" % (len(sb), ab, sorted(sb)))
    P("     🔒 **A-0(丁) 對稱差 ＝ %d**（⛔ 數目相同⛔ 不蘊含母體相同·`VR-048` 記功一）" % len(sa ^ sb))
    if sa ^ sb:
        P("     🔴 **名單變動逐宗具名**：只在 `V6` ＝ %s ／ 只在 `V6_1` ＝ %s"
          % (sorted(sa - sb), sorted(sb - sa)))
    dd, du = _d(aa, ab)
    P("     面積合計 `Δ` ＝ **%.6e ㎡**（`Δ/ulp` ＝ %.3e）" % (dd, du))
    for k in sorted(sa & sb):
        x = next(y for y in A["bad"] if y["key"] == k)
        y2 = next(y for y in B["bad"] if y["key"] == k)
        d2, u2 = _d(x["area"], y2["area"])
        P("       %-18s 面積 %14.8f ⇒ %14.8f　Δ ＝ %13.6e（%.3e ulp）"
          % (k, x["area"], y2["area"], d2, u2))
    flip4 = (len(sa) != len(sb)) or bool(sa ^ sb)
    res["4_nocross"] = {"nA": len(sa), "nB": len(sb), "symdiff": len(sa ^ sb),
                        "areaA": aa, "areaB": ab, "flip": flip4, "max": abs(dd)}

    # ── 逐列 `cross` 之翻動（超集·A-0(甲)）───────────────────────────────
    ra = {r["key"]: r for r in A["rows"]}
    rb = {r["key"]: r for r in B["rows"]}
    kk = set(ra) & set(rb)
    fl = [k for k in sorted(kk) if ra[k]["cross"] != rb[k]["cross"]]
    rz = [k for k in sorted(kk) if ra[k]["reason"] != rb[k]["reason"]]
    P("     🔒 **逐列判定之翻動**（母體 ＝ %d 列·對稱差 %d）：`cross` 翻動 ＝ **%d**／`reason` 變動 ＝ **%d**"
      % (len(kk), len(set(ra) ^ set(rb)), len(fl), len(rz)))
    for k in fl:
        P("       🔴 %s：`cross` %s ⇒ %s（reason %s ⇒ %s）"
          % (k, ra[k]["cross"], rb[k]["cross"], ra[k]["reason"], rb[k]["reason"]))
    for k in rz:
        P("       🔴 %s：`reason` %s ⇒ %s" % (k, ra[k]["reason"], rb[k]["reason"]))
    res["4b_rowflip"] = {"pop": len(kk), "flip": len(fl), "reason": len(rz),
                         "symdiff": len(set(ra) ^ set(rb))}

    # ── 量 6 餘裕 ──────────────────────────────────────────────────────
    P("")
    P("  ── 量 6　餘裕（m·節 103）──　🔒 施工單所舉 ＝ `0m R3` `3.502697`")
    ka, kb = set(A["margin"]), set(B["margin"])
    mx, mxk, nz = 0.0, "", 0
    P("     %-18s %18s %18s %14s %14s" % ("鍵", "V6", "V6_1", "Δ", "Δ/ulp"))
    for k in sorted(ka & kb):
        dd, du = _d(A["margin"][k], B["margin"][k])
        if dd != 0.0:
            nz += 1
            if nz <= 30:
                P("     %-18s %18.12f %18.12f %14.6e %14.3e"
                  % (k, A["margin"][k], B["margin"][k], dd, du))
        if abs(dd) > mx:
            mx, mxk = abs(dd), k
    if nz > 30:
        P("     …（另 %d 鍵有 Δ·**未列**）" % (nz - 30))
    finA = [(k, v) for k, v in A["margin"].items() if math.isfinite(v)]
    finB = [(k, v) for k, v in B["margin"].items() if math.isfinite(v)]
    nA = min(finA, key=lambda kv: abs(kv[1])) if finA else (None, float("nan"))
    nB = min(finB, key=lambda kv: abs(kv[1])) if finB else (None, float("nan"))
    P("     🔒 **節 103 最接近翻面者**：`V6` ＝ %s（餘裕 %.9e）／`V6_1` ＝ %s（餘裕 %.9e）"
      % (nA[0], nA[1], nB[0], nB[1]))
    P("     ⇒ **有 Δ 之鍵 ＝ %d ／ %d**；極大 `|Δ|` ＝ **%.6e m**（%s）" % (nz, len(ka & kb), mx, mxk))
    res["6_margin"] = {"max": mx, "nz": nz, "pop": len(ka & kb),
                       "nearestA": list(nA), "nearestB": list(nB)}

    # ── 量 7 `②-宗` 破量 ───────────────────────────────────────────────
    P("")
    P("  ── 量 7　🔴 `②-宗` 破量（㎡）──")
    ka, kb = set(A["zong2"]), set(B["zong2"])
    P("     破閘之格：`V6` ＝ %s ／ `V6_1` ＝ %s；**對稱差 ＝ %d**"
      % (sorted(ka), sorted(kb), len(ka ^ kb)))
    mx, mxk = 0.0, ""
    for k in sorted(ka & kb):
        dd, du = _d(A["zong2"][k]["area"], B["zong2"][k]["area"])
        P("     %-6s 對數 %d ⇒ %d　面積 %16.10f ⇒ %16.10f　Δ ＝ %13.6e（%.3e ulp）"
          % (k, A["zong2"][k]["n"], B["zong2"][k]["n"],
             A["zong2"][k]["area"], B["zong2"][k]["area"], dd, du))
        if abs(dd) > mx:
            mx, mxk = abs(dd), k
    flip7 = bool(ka ^ kb) or any(A["zong2"][k]["n"] != B["zong2"][k]["n"] for k in (ka & kb))
    P("     ⇒ 極大 `|Δ|` ＝ **%.6e ㎡**（%s）；**破閘格集合／對數翻動 ＝ %s**" % (mx, mxk, flip7))
    res["7_zong2"] = {"max": mx, "symdiff": len(ka ^ kb), "flip": flip7}

    # ── 量 8 `|sin(源甲, 源乙)|`（🔴 CC 自補·⛔ 施工單未令）────────────────────
    TSAME = 1e-12       # 🔒 `w84.TOL_SAME` 之值（⛔ 不另立·同 `w84:81`）
    P("")
    P("  ── 量 8　`|sin(源甲, 源乙)|` 逐宗 ──　🔴 **CC 自補**（⛔ 施工單未令）")
    P("     由：`w84` A-1 之**判別力對照組母體**（`|sin| ≤ %.0e` 之宗）本批實測由 **8 ⇒ 9**，" % TSAME)
    P("        而 `w84` **只印計數、⛔ 不印名單** ⇒ 無從指認**是哪一宗跨過門檻** ⇒ 本量補之。")
    ka, kb = set(A.get("sin2") or {}), set(B.get("sin2") or {})
    setA = set(k for k in ka if A["sin2"][k] <= TSAME)
    setB = set(k for k in kb if B["sin2"][k] <= TSAME)
    P("     母體：%d ／ %d；**對稱差 ＝ %d**" % (len(ka), len(kb), len(ka ^ kb)))
    P("     `|sin| ≤ %.0e` 之宗：`V6` ＝ **%d** %s ／ `V6_1` ＝ **%d** %s"
      % (TSAME, len(setA), sorted(setA), len(setB), sorted(setB)))
    P("     🔒 **對稱差 ＝ %d**；只在 `V6` ＝ %s ／ 🔴 **只在 `V6_1` ＝ %s**"
      % (len(setA ^ setB), sorted(setA - setB), sorted(setB - setA)))
    for k in sorted(setA ^ setB):
        P("       🔴 **跨門檻之宗 `%s`**：`|sin|` %.6e ⇒ %.6e（門檻 %.0e）"
          % (k, A["sin2"].get(k, float("nan")), B["sin2"].get(k, float("nan")), TSAME))
    mx, mxk, nz = 0.0, "", 0
    for k in sorted(ka & kb):
        dd, du = _d(A["sin2"][k], B["sin2"][k])
        if dd != 0.0:
            nz += 1
        if abs(dd) > mx:
            mx, mxk = abs(dd), k
    P("     ⇒ **有 Δ 之宗 ＝ %d ／ %d**；極大 `|Δ|` ＝ **%.6e**（%s）" % (nz, len(ka & kb), mx, mxk))
    res["8_sin2"] = {"max": mx, "nz": nz, "pop": len(ka & kb),
                     "symdiff": len(setA ^ setB), "nA": len(setA), "nB": len(setB),
                     "flip": bool(setA ^ setB),
                     "moved": sorted(setB - setA) + sorted(setA - setB)}

    return res


# ══════════════════════════════════════════════════════════════════════════
def _run_measure(dxf, jout):
    r = measure(dxf)
    with io.open(jout, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False)
    return 0


def _run_asprobe(mod, dxf, lout):
    """🔒 **原樣執行**來源探針之 `main()`（⛔ 不改其碼）·只把 `rv.V6DXF` 與 `LOG` 就地換掉。"""
    import importlib
    rv.V6DXF = os.path.abspath(dxf)
    m = importlib.import_module(mod)
    m.LOG = lout
    if hasattr(m, "CSV"):
        m.CSV = lout + ".csv"
    try:
        m.main()
    except SystemExit:
        pass
    return 0


def main():                                                         # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)

    if len(sys.argv) >= 4 and sys.argv[1] == "--measure":
        return _run_measure(sys.argv[2], sys.argv[3])
    if len(sys.argv) >= 5 and sys.argv[1] == "--asprobe":
        return _run_asprobe(sys.argv[2], sys.argv[3], sys.argv[4])

    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【W-G.9-90 §二 A 組】以 `V6_1` 跑**現行之新判定**，逐項與 `V6` 對照（🔒 只量不修·⛔ 不換圖）")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  🛑 **生產路徑不動**：`run_verification.py::V6DXF` ＝ %s（⛔ 逐字未改）"
      % os.path.relpath(rv.V6DXF, REPO).replace(os.sep, "/"))
    P("  🔒 **A-0 事前選定：偏向<u>放大變動</u>**（甲 超集母體／乙 一律判翻動／丙 取大 `|Δ|`／丁 對稱差）")
    P("  🔒 情境母體 ＝ **僅 %gm**（同 `-88`·⛔ 不擴·具名）" % SB)
    P("  🔒 三輪**subprocess 隔離**：`V6` ／ `V6_1` ／ **`V6` 再一次**（判別力·常設 8）")
    for nm, p in (("V6", V6), ("V6_1", V61)):
        P("     %-5s %s  md5 ＝ %s  bytes ＝ %d"
          % (nm, os.path.relpath(p, REPO).replace(os.sep, "/"), _md5(p), os.path.getsize(p)))

    tmp = os.path.join(OUTDIR, "_wg990")
    os.makedirs(tmp, exist_ok=True)
    runs = [("V6", V6, os.path.join(tmp, "v6.json")),
            ("V6_1", V61, os.path.join(tmp, "v61.json")),
            ("V6#2", V6, os.path.join(tmp, "v6b.json"))]
    P("")
    P("【驅動】三輪量測（各一 subprocess·⛔ 同行程重入之等冪性未經證 ⇒ 不以同行程三呼替代）")
    got = {}
    for nm, dxf, jout in runs:
        if os.path.exists(jout):
            os.remove(jout)
        cp = subprocess.run([sys.executable, os.path.abspath(__file__), "--measure", dxf, jout],
                            capture_output=True, text=True,
                            env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        if cp.returncode != 0 or not os.path.exists(jout):
            P("  🔴 **輪 %s 失敗**（rc=%d）⇒ 停機（no-silent-fallback）" % (nm, cp.returncode))
            P((cp.stderr or "")[-3000:])
            with io.open(LOG, "w", encoding="utf-8") as f:
                f.write("\n".join(L) + "\n")
            raise RuntimeError("🔴 量測輪 %s 失敗 rc=%d" % (nm, cp.returncode))
        with io.open(jout, encoding="utf-8") as f:
            got[nm] = json.load(f)
        P("  ✅ 輪 %-5s rc=0　DXF ＝ %-16s md5 ＝ %s　攔截 %d 格　列 %d　違反 %d"
          % (nm, got[nm]["dxf"], got[nm]["md5"], got[nm]["n_cells"],
             len(got[nm]["rows"]), len(got[nm]["bad"])))
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (got["V6"]["env"]["shapely"], got["V6"]["env"]["geos"], got["V6"]["env"]["numpy"]))

    # ── 🔒 判別力（常設 8）：`V6` 對 `V6` 自身 ⇒ 全部 Δ ＝ 0（逐位）──────────
    P("")
    P("=" * W)
    P("【判別力自檢（常設 8·⛔ 不可省）】`V6` 對 **`V6` 自身**跑同一路徑 ⇒ 期望全部 `Δ ＝ 0`（逐位）")
    P("=" * W)
    self_res = compare(P, got["V6"], got["V6#2"])
    self_ok = all((v.get("max", 0.0) == 0.0 and not v.get("flip")
                   and v.get("symdiff", 0) == 0 and v.get("nz", 0) == 0
                   and v.get("reason", 0) == 0)
                  for v in self_res.values())
    P("")
    P("  🔒 **判別力判**：全部量之 `Δ` 皆為 **0**（逐位）？⇒ **%s**"
      % ("✅ 是 ⇒ 該對照器**非恆報變動**" if self_ok else
         "🔴 **否 ⇒ 對照器不穩定·本批全部 Δ 之效力存疑·停機上呈**"))

    # ── 本體：`V6` vs `V6_1` ────────────────────────────────────────────
    P("")
    P("=" * W)
    P("【C／A-1】🛑 **`V6` vs `V6_1`**——七項逐項並列 ＋ `Δ`")
    P("=" * W)
    main_res = compare(P, got["V6"], got["V6_1"])

    # ── 量 5 `S_req`：原樣執行 `w84.main()` ────────────────────────────
    P("")
    P("  ── 量 5　`S_req`（m）──　🩸 **具名例外**：其全稱式與 `groups_of`／`A2` 母體")
    P("     **皆為 `w84.main()` 內之巢狀定義 ⇒ ⛔ 不可 import**，重寫之即施工單所禁之**重造**。")
    P("     ⇒ 🔒 改以**原樣執行 `probe_WG984_gap.main()`**（各 DXF 各一次），比其出艙之表。")
    P("     🔒 **Δ 之精度 ＝ 該 log 之列印精度 `4dp`（`1e-4 m`）**——⛔ **不偽稱 `ulp` 級**；")
    P("        判別力：`GB-16` 之變動為 `45m` 處 `7.11mm` ＝ `7.11e-3 m` ⇒ **較 `1e-4 m` 粗 71 倍**")
    P("        ⇒ 該精度**足以偵測翻動**，其不足僅在「Δ 之尾數」、⛔ 不在「有無 Δ」。")
    s5 = {}
    for nm, dxf in (("V6", V6), ("V6_1", V61)):
        lo = os.path.join(tmp, "w84_%s.log" % nm.replace("_", ""))
        if os.path.exists(lo):
            os.remove(lo)
        cp = subprocess.run([sys.executable, os.path.abspath(__file__),
                             "--asprobe", "probe_WG984_gap", dxf, lo],
                            capture_output=True, text=True,
                            env=dict(os.environ, PYTHONIOENCODING="utf-8"))
        if not os.path.exists(lo):
            P("     🔴 **`w84` 輪 %s 未產出 log**（rc=%d）⇒ 具名（⛔ 不靜默）" % (nm, cp.returncode))
            P((cp.stderr or "")[-2000:])
            s5[nm] = None
            continue
        s5[nm] = io.open(lo, encoding="utf-8").read()
        P("     ✅ `w84` 輪 %-5s rc=%d　log ＝ %s（%d 行）"
          % (nm, cp.returncode, os.path.relpath(lo, REPO).replace(os.sep, "/"),
             s5[nm].count("\n")))
    if s5.get("V6") and s5.get("V6_1"):
        # 🔒 逐行比：⛔ 排除含 commit／路徑之行（其變動與圖無關·**逐條具名**）
        def _keep(x):
            return not any(t in x for t in ("產生於 commit", "→ ", "\\", "log ＝", "DXF"))
        za = [x for x in s5["V6"].split("\n") if _keep(x)]
        zb = [x for x in s5["V6_1"].split("\n") if _keep(x)]
        dif = [(i, x, y) for i, (x, y) in enumerate(zip(za, zb), 1) if x != y]
        P("     🔒 **`w84` 全 log 逐行對照**（🔒 已排除 `產生於 commit`／`→ `／含 `\\` 之路徑行／`log ＝`／`DXF`）")
        P("        可比行 %d ／ %d；**相異行 ＝ %d**" % (len(za), len(zb), len(dif)))
        if len(za) != len(zb):
            P("     🔴 **行數不同**（%d vs %d）⇒ 具名" % (len(za), len(zb)))
        shown = 0
        for i, x, y in dif:
            if "S_req" in x or "S_req" in y:
                P("       🔴 S_req :%d  V6   %s" % (i, x.strip()[:180]))
                P("       🔴 S_req :%d  V6_1 %s" % (i, y.strip()[:180]))
                shown += 1
        P("     ⇒ 🔒 **其中含 `S_req` 字樣之相異行 ＝ %d**（＝ 本量之受詞本身）" % shown)

        # ── 🔒 三判準之分類（⛔ 不以「有無相異行」定翻動·必答明訂 ⛔ 非「數值有無變動」）──
        import re as _re
        _NUM = _re.compile(r"[-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?")
        #    整數 ＝ 前後皆非 [.0-9eE+-] 之數字串（⛔ 排除小數／指數之片段）
        _INT = _re.compile(r"(?<![\d.eE+-])\d+(?![\d.]|[eE][-+]?\d)")
        _TOK = ["合格", "不合格", "單調", "非單調", "較鬆", "較嚴",
                "✅", "\U0001f534", "是", "否", "情形 甲", "情形 乙", "破閘", "未破閘"]

        def _cls(x, y):
            a1 = _NUM.sub("#", x) != _NUM.sub("#", y)                    # 非數值之差
            a2 = tuple(x.count(t) for t in _TOK) != tuple(y.count(t) for t in _TOK)
            a3 = _INT.findall(x) != _INT.findall(y)                      # 整數／母體基數
            return a1, a2, a3

        c1 = [(i, x, y) for i, x, y in dif if _cls(x, y)[0]]
        c2 = [(i, x, y) for i, x, y in dif if _cls(x, y)[1]]
        c3 = [(i, x, y) for i, x, y in dif if _cls(x, y)[2]]
        pure = [(i, x, y) for i, x, y in dif if not any(_cls(x, y))]
        P("     🔒 **三判準之分類**（⛔ 「有無相異行」⛔ 不等於「判定翻動」）：")
        P("        (甲) 去掉全部數字後仍相異 ＝ **%d**" % len(c1))
        P("        (乙) 判定 token 計數相異 ＝ **%d**（token 集 ＝ %s）" % (len(c2), _TOK))
        P("        (丙) 🔴 **整數（計數／母體基數）相異 ＝ %d**"
          "——🔒 (甲) 會把基數當數值吃掉 ⇒ 非本判準不可得" % len(c3))
        P("        (丁) 純小數 Δ（三判準皆不咬）＝ **%d**" % len(pure))
        P("        🔒 **合計自校**：%d ＋ %d ＝ %d ／ 相異行 %d ⇒ %s"
          % (len(set(i for i, _x, _y in c1 + c2 + c3)), len(pure),
             len(set(i for i, _x, _y in c1 + c2 + c3)) + len(pure), len(dif),
             "✅" if len(set(i for i, _x, _y in c1 + c2 + c3)) + len(pure) == len(dif) else "🔴 不合"))
        for lab, cc in (("甲", c1), ("乙", c2), ("丙", c3)):
            for i, x, y in cc:
                P("        🔴 (%s) :%d  V6   %s" % (lab, i, x.strip()[:175]))
                P("        🔴 (%s) :%d  V6_1 %s" % (lab, i, y.strip()[:175]))
        # 🔒 判別力（陽性＋陰性對照·⛔ 不得只報 0）
        _p1 = "母體（之宗）＝ **8**；完全相同 ＝ 8"
        _p2 = "母體（之宗）＝ **9**；完全相同 ＝ 9"
        _n1 = "Δfront -10.1319　⇒ 不合格"
        _n2 = "Δfront -10.1320　⇒ 不合格"
        P("        🔒 **判別力**：陽性對照（`8 ⇒ 9`）(丙) 咬到 ＝ **%s**（須 True）；"
          "陰性對照（純小數 `-10.1319 ⇒ -10.1320`）(丙) 咬到 ＝ **%s**（須 False）"
          % (_INT.findall(_p1) != _INT.findall(_p2), _INT.findall(_n1) != _INT.findall(_n2)))
        for i, x, y in pure[:12]:
            P("       Δ(純小數) :%d  V6   %s" % (i, x.strip()[:165]))
            P("       Δ(純小數) :%d  V6_1 %s" % (i, y.strip()[:165]))
        if len(pure) > 12:
            P("       …（另 %d 行純小數 Δ·**未列**·🔒 母體 ＝ %d）" % (len(pure) - 12, len(pure)))
        # 🔒 本量之受詞 ＝ `S_req` 本身 ⇒ 翻動之判準 ＝ 含 `S_req` 之相異行 ＋ (甲)(乙)(丙)
        sreq_flip = (shown > 0) or bool(c1) or bool(c2)
        main_res["5_sreq"] = {"difflines": len(dif), "pop": len(za),
                              "c1": len(c1), "c2": len(c2), "c3": len(c3),
                              "pure": len(pure), "sreq_lines": shown,
                              "flip": sreq_flip, "max": float("nan")}
        P("     🔒 **量 5（`S_req` 本身）之判**：含 `S_req` 之相異行 %d ＋ (甲) %d ＋ (乙) %d ⇒ **%s**"
          % (shown, len(c1), len(c2), "🔴 翻動" if sreq_flip else "✅ 未翻動"))
        if c3:
            P("     🛑 **⛔ 非本量受詞、惟本批之實得**：(丙) %d 行——見【必答】表下之具名。" % len(c3))
    else:
        main_res["5_sreq"] = {"difflines": -1, "pop": 0, "flip": None, "max": float("nan")}
        P("     🔴 **量 5 未取得** ⇒ 具名為**未答**（⛔ 不以「無差異」充數）")

    # ── 🔒 必答 ────────────────────────────────────────────────────────
    P("")
    P("=" * W)
    P("【必答】上開七項中，**有無任何一項之<u>判定</u>翻動**？（⛔ 非「數值有無變動」）")
    P("=" * W)
    P("  %-20s %-46s %-14s %-14s" % ("項", "判定之受詞", "**翻動?**", "極大|Δ|"))
    verdicts = [
        ("1 `∠(用,ALLOC)`", "母體對稱差 ＝ 0",
         main_res["1_angle"]["symdiff"] != 0, main_res["1_angle"]["max"]),
        ("2 弦區間", "`empty` 之真偽 ＋ 母體對稱差",
         bool(main_res["2_chord"]["flip"]) or main_res["2_chord"]["symdiff"] != 0,
         main_res["2_chord"]["max"]),
        ("3 `s*`", "母體（對）之對稱差",
         main_res["3_sstar"]["symdiff"] != 0, main_res["3_sstar"]["max"]),
        ("4 `K-9-9 二` 不交叉", "🔴 **違反宗數與名單**",
         bool(main_res["4_nocross"]["flip"]), main_res["4_nocross"]["max"]),
        ("4b 逐列 `cross`", "逐列合格／不合格 ＋ `reason`",
         (main_res["4b_rowflip"]["flip"] != 0 or main_res["4b_rowflip"]["reason"] != 0
          or main_res["4b_rowflip"]["symdiff"] != 0), float("nan")),
        ("5 `S_req`", "🩸 含 `S_req` 之相異行 ＋ (甲)(乙)（4dp）",
         main_res["5_sreq"]["flip"], main_res["5_sreq"]["max"]),
        ("6 餘裕", "節 103 之最接近翻面者（鍵）",
         main_res["6_margin"]["nearestA"][0] != main_res["6_margin"]["nearestB"][0],
         main_res["6_margin"]["max"]),
        ("7 `②-宗` 破量", "🔴 **破閘格集合與對數**",
         bool(main_res["7_zong2"]["flip"]), main_res["7_zong2"]["max"]),
    ]
    nflip = 0
    for nm, subj, fl, mx in verdicts:
        if fl:
            nflip += 1
        P("  %-20s %-46s %-14s %.6e"
          % (nm, subj, ("🔴 **是**" if fl else ("✅ 否" if fl is not None else "⚠️ 未答")), mx))
    P("")
    P("  🔒 **必答之答（施工單七項＋逐列 `cross`）：翻動之項數 ＝ %d ／ %d**" % (nflip, len(verdicts)))
    P("  %s" % ("✅ **施工單七項無一判定翻動**（⛔ 惟數值仍有 Δ·見上表）"
                if nflip == 0 else
                "🛑 **有判定翻動 ⇒ 依施工單 §四 `P2` 之令：立即上呈·⛔ 不得逕自續判**"))

    # ── 🔴 具名：⛔ 非施工單七項之受詞、惟本批實得之變動 ────────────────────
    P("")
    P("  🔴 **⛔ 非施工單七項之受詞、惟本批實得之變動（⛔ 不得因「不在受詞內」而不報·A-0(乙)）**：")
    s8 = main_res.get("8_sin2") or {}
    P("     ① **量 8（CC 自補）`|sin(源甲, 源乙)| ≤ 1e-12` 之宗**：**%s ⇒ %s**；"
      "對稱差 ＝ **%s**；移動之宗 ＝ **%s**"
      % (s8.get("nA"), s8.get("nB"), s8.get("symdiff"), s8.get("moved")))
    P("        🔒 該母體 ＝ `w84` A-1 之**判別力對照組**（「已知二源相同」之宗）"
      "⇒ 其基數變動**⛔ 不改 `S_req`**，惟證 **換圖確會使宗跨越容差門檻**。")
    P("     ② **`w84` log 之 (丙) 整數／母體基數相異行 ＝ %s**（`w84` 只印計數、⛔ 不印名單 ⇒ 由 ① 指認）"
      % (main_res.get("5_sreq") or {}).get("c3"))
    P("     🔒 二者**係同一件事之二面**（`w84` 之計數 ／ 本檔之名單），⛔ 不得相加。")

    # ── A-2 節 103：最接近翻面者 ────────────────────────────────────────
    P("")
    P("=" * W)
    P("【D／A-2】節 103：**最接近翻面者**及其**餘裕**（⛔ 以被判別之量本身度量·非布林）")
    P("=" * W)
    P("  🔒 **單一門檻**（常設 14 ①）⇒ ⛔ 無未定義帶：判準 ＝ `s* ∈ [λ_a, λ_b]`（`w82.pred_chord`）")
    P("     ⇒ **被判別之量 ＝ `餘裕`**（`s*` 距最近端點之帶號距·`w88.margin_of`）")
    cand = []
    for k in sorted(set(got["V6"]["margin"]) & set(got["V6_1"]["margin"])):
        a, b = got["V6"]["margin"][k], got["V6_1"]["margin"][k]
        if not (math.isfinite(a) and math.isfinite(b)):
            continue
        cand.append((abs(a), abs(b - a), k, a, b))
    cand.sort()
    P("  %-20s %18s %18s %14s %14s %-12s" % ("鍵", "餘裕(V6)", "餘裕(V6_1)", "|餘裕|", "|Δ|", "擦邊?"))
    n_graze = 0
    for _ab, dd, k, a, b in cand:
        gz = (dd > 0) and (abs(a) < 10.0 * dd)
        if gz:
            n_graze += 1
    for _ab, dd, k, a, b in cand[:12]:
        gz = (dd > 0) and (abs(a) < 10.0 * dd)
        P("  %-20s %18.11f %18.11f %14.6e %14.6e %-12s"
          % (k, a, b, abs(a), dd, "🔴 **擦邊**" if gz else "否"))
    if len(cand) > 12:
        P("  …（另 %d 鍵·**未列**·🔒 母體 ＝ %d）" % (len(cand) - 12, len(cand)))
    if cand:
        _ab, dd, k, a, b = cand[0]
        P("")
        P("  🔒 **最接近翻面者 ＝ `%s`**：`餘裕` ＝ **%.11f m**（`V6`）⇒ **%.11f m**（`V6_1`）" % (k, a, b))
        P("     其 `|Δ|` ＝ **%.6e m**；`|餘裕| / |Δ|` ＝ **%s**"
          % (dd, ("%.3e" % (abs(a) / dd)) if dd > 0 else "∞（`Δ ＝ 0`）"))
        P("     ⚠️ 判準（施工單 A-2）：`餘裕 < 10 × |Δ|` ⇒ **具名為擦邊** ⇒ **%s**"
          % ("🔴 **擦邊**" if ((dd > 0) and (abs(a) < 10.0 * dd)) else "✅ 非擦邊"))
    P("  🔒 **全母體之擦邊計數 ＝ %d ／ %d**（⛔ 不得只報「未翻動」）" % (n_graze, len(cand)))

    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
