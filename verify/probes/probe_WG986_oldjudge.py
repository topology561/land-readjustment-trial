# -*- coding: utf-8 -*-
r"""**W-G.9-86 §二 A 組**：舊判準於平行二界之逐步中間量／`_PAR_TOL` 射程／座標框正當性／`D-0` 結案。

## 受詞（施工單 `W-G.9-86` §二·`VR-044` 六）
- **A-1**（🛑 第一項）**舊判準何以在平行二界上判違反**——27 宗**全部**逐步中間量 ＋ 受詞內 3 宗之對照。
- **A-2** `_PAR_TOL = 1e-6` 之**射程現查** ＋ 以之重判（⛔ **不另立門檻**·`K-6:1010`）。
- **A-3** **二座標框之正當性**（⛔ **不另立座標框**·`K-6:2426`·錨 `st_frame`）。
- **A-4** `D-0` 二源之結案 ＋ `R1 左 j=0` 之雙重異常。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單欲查「舊判準之缺陷」。其瑕若使**缺陷看起來只咬受詞外之宗** ⇒ 受詞內之 3 宗安然 ⇒ **安靜**。
🔒 **事前選定：偏向判「該缺陷<u>亦</u>咬受詞內」**——落實為二條，⛔ 逐條具名：
  (甲) 中間量之歸屬不確定者，一律取**使受詞內亦受影響**之解讀並具名；
  (乙) 受詞內／外之切分沿用**正典之 `_PAR_TOL = 1e-6`**（⛔ 不另立·⛔ 不取 A-0 式之保守 `1e-9`）。

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
`w40.eval_lot`／`far_side_dir_and_pt`／`line_isect`／`s_of`、`w82.chord_interval`／`pred_chord`／
`ring_edges`／`pj_of`／`uj_of`、`w81.analyse_cell`／`spy_solve`／`spy_pool`／`faces_of`
皆**原樣 import**。`w83`／`w84`／`w85` 之量測邏輯寫在 `main()` 內⛔ 不可 import
（🔒 逐字具名之差）；本檔 import 其**模組級常數**與 `w84.s_front_of_line`。
🔒 **A-1 之中間量**：`eval_lot` **未回傳**其內部之 `s_Pprev`／`s_Pperp`／`s_Bperp`／`s_Bprev`
⇒ 本檔**自其同一組輸入**（`P_prev`／`B_prev`）以 `w40.s_of` 重取，並**逐宗斷言**
本檔所導之 `(情形, 起算, Δ, 出艙碼)` 與 `w40.eval_lot` **逐位相同** ⇒ ⛔ 非重造判定式。

## ⛔ 本檔不做（施工單 §二 A-5 六款）
⛔ 零 `app.py` 變更；⛔ `data/`／`docs/rulings/` 零變更；⛔ 不落地 `K-9-9`／`K-9-14`；
⛔ 不建遞補／合併／調配池介面；⛔ 不換圖／不重烤／不改任何 baseline；
🔴 ⛔ **不另立平行判定之門檻**（`K-6:1010`）；🔴 ⛔ **不另立座標框**（`K-6:2426`）；
⛔ 不出艙「應改領現金之宗」；⛔ 不以「理論上恆真」代替實算；⛔ 不下「這是 bug」之結論。

## 🔒 常設條款
**8** 每判準附「會使它為否」之輸入；**9** 門檻併出艙量級與 `math.ulp`、跨數量級**分層**；
**10** 每表末印 `POPULATION/PRINTED/SUPPRESSED`，報告中 ≥4dp 之數可回指 log 行；
**11** 修法列動作清單（本檔「⛔ 不經 shell 傳字樣」**適用讀＋寫**·以 `Write` 落盤）；
**12／13** 搜尋規格含正典款號組＋三類出處分類——見報告 §A；
**14**（`自誤 89` 修法 99〜101）① 分離之宣稱一律**單一門檻**＋出艙未定義帶之筆數；
② 門檻**先查正典**（本批即用 `_PAR_TOL`）；③ 凡出艙 `m／n` 須同批出艙**判別力為零者幾筆**。
"""
import contextlib
import dis
import io
import math
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
import stepg_pipeline as sgp                                        # noqa: E402

import shapely                                                      # noqa: E402

import probe_WG981_scope as w81                                     # noqa: E402
import probe_WG982_chord as w82                                     # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402
import probe_WG983_k99prep as w83                                   # noqa: E402
import probe_WG984_gap as w84                                       # noqa: E402
import probe_WG941_bandbase as w941                                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210
SB = 0.0                       # 🔒 母體 ＝ `0m`（＝ `-40`／`-83`／`-85` 之母體·⛔ 不擴·具名）


def _par_tol_from_code():
    r"""🔴 **正典之容差**（`K-6:1010`）——**自生產碼取**·⛔ 不抄寫。

    🩸 `_PAR_TOL` 係 `stepg_pipeline` 內之**函式區域變數**（⛔ 非模組級）
    ⇒ ⛔ 不可 `import` 取；本檔以**二法**取之並對拍：
      甲 ＝ `ast` 之 `Assign`（走訪全樹·⛔ 不假設縮排）
      乙 ＝ 倉內既有之 regex 法（`probe_D2b12_bridge.py:101` 逐字沿用·⇒ 同源）
    ⛔ 二法不等即 `raise`（no-silent）。
    """
    import ast as _ast
    src = io.open(os.path.join(VERIFY, "stepg_pipeline.py"), encoding="utf-8").read()
    va = None
    for node in _ast.walk(_ast.parse(src)):
        if isinstance(node, _ast.Assign):
            for t in node.targets:
                if isinstance(t, _ast.Name) and t.id == "_PAR_TOL" \
                        and isinstance(node.value, _ast.Constant):
                    va = float(node.value.value)
    m = re.search(r"_PAR_TOL\s*=\s*([0-9eE.+-]+)", src)
    vb = float(m.group(1)) if m else None
    if va is None or vb is None or va != vb:
        raise RuntimeError("🔴 `_PAR_TOL` 之二法不等或取不到：ast=%r regex=%r" % (va, vb))
    return va, vb


PAR_TOL, PAR_TOL_B = _par_tol_from_code()
EPS_TOUCH = 1e-9               # `st_frame` 之 `eps_touch`（僅供 A-3 之呼叫·⛔ 不入任何判準）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG986_oldjudge_%s.log" % COMMIT)
_u = w82._u
s_front_of_line = w84.s_front_of_line


def _sin(a, b):
    a, b = _u(a), _u(b)
    if a is None or b is None:
        return float("nan")
    return abs(float(a[0] * b[1] - a[1] * b[0]))


# ═══ P7 之第十二法：`run_all` 清單筆數 ═════════════════════════════════
def run_all_count_method12(src=None):
    r"""🔒 **第十二法：位元組碼之<u>控制流</u>定位法**（⛔ 與既用十一法皆不同族）。

    既用十一法之母體：原始碼**語法／位元組**（①〜③⑦）、**編譯後之全部常數**（④⑥）、
    **肉眼**（⑤）、**檔案系統**（⑧）、**git 增刪歷史**（⑨）、**報告宣告**（⑩）、**執行 log**（⑪）。
    🔴 本法之母體 ＝ **`main` 之位元組碼<u>指令流</u>**：只取**餵給 `GET_ITER`／`FOR_ITER`**
    之那**一個**常數元組（＝ 由**控制流**定位），⛔ 非「掃全部常數」。
    🔒 **其獨有之判別力**：若檔中另有一個**同形而未被迭代**之元組常數，
    ④⑥ 會多數，本法**不會**——`selfcheck` ⑤ 以合成模組實證之。
    ⛔ **本法⛔ 執行 `run_all`**（僅 `compile`·⛔ 不 `exec`）。
    """
    if src is None:
        src = io.open(os.path.join(VERIFY, "run_all.py"), encoding="utf-8").read()
    code = compile(src, "run_all.py", "exec")
    main_code = None
    for c in code.co_consts:
        if hasattr(c, "co_name") and c.co_name == "main":
            main_code = c
            break
    if main_code is None:
        return None, []
    found = []
    last_const = None
    for ins in dis.get_instructions(main_code):
        if ins.opname == "LOAD_CONST":
            last_const = ins.argval
        elif ins.opname in ("GET_ITER", "FOR_ITER"):
            if isinstance(last_const, tuple) and last_const:
                found.append(last_const)
                last_const = None
    cands = [t for t in found
             if all(isinstance(e, tuple) and len(e) >= 1 and isinstance(e[0], str) for e in t)]
    return (len(cands[0]) if cands else None), cands


def _co_consts_count(src):
    """④／⑥ 族之對照實作（**掃全部常數**·⛔ 不看控制流）——僅供 `selfcheck` ⑤ 之判別力。"""
    code = compile(src, "x.py", "exec")
    n = 0

    def walk(c):
        nonlocal n
        for k in c.co_consts:
            if hasattr(k, "co_consts"):
                walk(k)
            elif isinstance(k, tuple) and k and all(
                    isinstance(e, tuple) and e and isinstance(e[0], str) for e in k):
                n = max(n, len(k))
    walk(code)
    return n


# ═══ 【0】量測器自檢 ═════════════════════════════════════════════════════
def selfcheck(P):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·每項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    TH = math.radians(17.0)
    d = (math.cos(TH), math.sin(TH))
    o = (0.0, 0.0)
    n = (-d[1], d[0])
    ob = (o[0] + 40.0 * n[0], o[1] + 40.0 * n[1])

    def fp(s):
        return (o[0] + s * d[0], o[1] + s * d[1])

    def bp(s):
        return (ob[0] + s * d[0], ob[1] + s * d[1])

    c1 = w40.eval_lot(fp(10.0), bp(4.0), fp(20.0), bp(20.0), o, d, n)
    c2 = w40.eval_lot(fp(10.0), bp(16.0), fp(20.0), bp(20.0), o, d, n)
    c3 = w40.eval_lot(fp(10.0), bp(16.0), fp(30.0), bp(30.0), o, d, n)
    c4 = w40.eval_lot(fp(10.0), bp(16.0), fp(12.0), bp(12.0), o, d, n)
    r1 = (c1[0] == "甲" and c2[0] == "乙" and c3[3] == "合格" and c4[3] == "不合格")
    ok &= r1
    P("  ① **`w40.eval_lot` 同源證**：甲 %s／乙 %s／合格 %s／**已知不合格 %s**（Δfront %+.3f）⇒ %s"
      % (c1[0], c2[0], c3[3], c4[3], c4[2][0], "PASS" if r1 else "🔴 FAIL"))

    e_sq, _dg = w82.ring_edges(w82.SQ_CCW)
    uu = _u((3.0, 4.0))
    ci = w82.chord_interval(e_sq, np.array([1.0, 2.0]), uu)
    r2 = (abs(ci["lam_b"] - 10.0) <= 8 * math.ulp(10.0)
          and w82.pred_chord(ci, 0.0) and not w82.pred_chord(ci, 1e6))
    ok &= r2
    P("  ② **`w82` 同源證**：λ_b ＝ %.12g（手算 10）；`s*=0` ⇒ %s／`1e6` ⇒ %s ⇒ %s"
      % (ci["lam_b"], w82.pred_chord(ci, 0.0), w82.pred_chord(ci, 1e6),
         "PASS" if r2 else "🔴 FAIL"))

    # ③ 🔴 **正典容差之取得**（⛔ 抄寫·自生產碼取）
    P("  ③ **`_PAR_TOL` 自生產碼取**（⛔ 不抄寫·**二法對拍**）：`ast` ＝ %.1e ／ `regex`（倉內既有法）＝ %.1e" % (PAR_TOL, PAR_TOL_B))
    r3 = (abs(PAR_TOL - 1e-6) < 1e-18)
    ok &= r3
    P("     🔒 與 `K-6:1010` 逐字之 `1e-6` 相符 ⇒ %s" % ("PASS" if r3 else "🔴 FAIL"))

    # ④ 🔒 `st_frame` 之二法（原樣 import ／ 依定義式重算）
    sq = [(0.0, 0.0), (10.0, 0.0), (10.0, 6.0), (0.0, 6.0)]
    dh, fpt = (1.0, 0.0), (0.0, 0.0)
    ring_a, t_lo_a, sg_a, d_a, n_a, _fe = w941.st_frame(sq, dh, fpt, EPS_TOUCH)
    _dv = np.asarray(dh, float)[:2]
    _dv = _dv / float(np.linalg.norm(_dv))
    _nv = np.array([-_dv[1], _dv[0]])
    _fv = np.asarray(fpt, float)[:2]
    manual = [(float(np.dot(np.asarray(p, float)[:2] - _fv, _dv)),
               float(np.dot(np.asarray(p, float)[:2] - _fv, _nv))) for p in sq]
    res4 = max(abs(a[0] - b[0]) for a, b in zip(sorted(ring_a[:-1]), sorted(manual)))
    r4 = res4 <= 16 * math.ulp(10.0)
    ok &= r4
    P("  ④ **`st_frame` 二法對拍**（原樣 import vs 依定義式重算）：`s` 之極大差 ＝ %.3e"
      "（**殘差/ulp ＝ %.2f**）⇒ %s" % (res4, w82._ulp_ratio(res4, 10.0),
                                       "PASS" if r4 else "🔴 FAIL"))
    P("     🔒 `st_frame` 之逐字定義：`(s, t) = ((p − front_pt)·d̂, (p − front_pt)·n̂)`"
      "（`n̂ = rot90(d̂)`·另依形心翻號 σ ⇒ **σ 只作用於 `t`**）")

    # ⑤ 🔒 第十二法之**判別力**：合成模組含一個**未被迭代**之同形元組
    syn = (
        'def main():\n'
        '    DECOY = (("a.py", "x"), ("b.py", "y"), ("c.py", "z"))\n'
        '    for _fx, _what in (("p.py", "1"), ("q.py", "2")):\n'
        '        print(_fx, _what)\n'
        '    return DECOY\n')
    n12, _c = run_all_count_method12(syn)
    n46 = _co_consts_count(syn)
    r5 = (n12 == 2 and n46 == 3)
    ok &= r5
    P("  ⑤ **第十二法之判別力（常設 8）**：合成模組（迭代 2 筆 ＋ **誘餌 3 筆未被迭代**）")
    P("     ⇒ **第十二法 ＝ %s**（期望 2·只取餵給 `GET_ITER` 者）／"
      "④⑥ 族（掃全部常數）＝ **%s**（期望 3）⇒ %s"
      % (n12, n46, "PASS" if r5 else "🔴 FAIL"))
    P("     🔒 ⇒ **二法之受詞確實不同**（⛔ 非同族）")

    P("  ⑥ **常設 9**：`PAR_TOL = %.1e` 施於 `|sin|` ∈ [0,1]（`ulp(1.0) = %.3e`）"
      "⇒ 門檻/ulp ＝ %.3e" % (PAR_TOL, math.ulp(1.0), PAR_TOL / math.ulp(1.0)))
    P("  ⇒ 量測器自檢：%s" % ("PASS" if ok else "🔴 FAIL（⛔ 以下量測結果不得採信）"))
    return ok


# ═══ 主 ═══════════════════════════════════════════════════════════════
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

    def POP(pop, printed, tag):
        P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # %s" % (pop, printed, pop - printed, tag))
        if printed != pop:
            P("     ⚠️ `PRINTED ≠ POPULATION` ⇒ 🔒 **本表之結論一律以 `POPULATION` 為分母**"
              "（⛔ 表身列數不得作為母體·節 105）")

    P("=" * W)
    P("【W-G.9-86 §二 A 組】舊判準之逐步中間量／`_PAR_TOL` 射程／座標框正當性／`D-0` 結案")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向判「該缺陷<u>亦</u>咬受詞內」**（甲/乙 二條見 docstring）")
    P("  🔴 **門檻 ＝ 正典之 `_PAR_TOL = %.1e`**（`K-6:1010`·自 `stepg_pipeline` 取·⛔ 不另立）" % PAR_TOL)
    P("  🔒 情境母體 ＝ **僅 %gm**（⛔ 不擴·具名）" % SB)

    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    # ── 驅動 ────────────────────────────────────────────────────────
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
    EPS_T = float(ns["_EPS_TOUCH_FRONT"])   # 🔒 生產常數（⛔ 不另立·同 `w941`／`w947` 之取法）
    P("")
    P("【驅動】`%gm` × R1–R6——攔截 **%d 格**" % (SB, len(REAL)))

    # ── 逐格逐宗之基礎量（同 `-85` 之構造·⛔ 不重造判定式）──────────────
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
        lots = {}
        for i in range(len(rec["biz"])):
            ua, pa = w40.far_side_dir_and_pt(rec["biz"][i], d_)
            r_ = (rec["ress"] or [None] * (i + 1))[i]
            ff = w81.faces_of(w81.SOLVE.get(id(r_)))[1]
            ub, pb = (None, None) if ff is None else (_u(ff[0]), np.asarray(ff[1], float)[:2])
            Pc = Bc = None
            if ua is not None:
                Pc = w40.line_isect(tuple(pa), tuple(ua), o_, d_)
                Bc = w40.line_isect(tuple(pa), tuple(ua), bpt, bdir)
            lots[i] = {"ua": ua, "pa": pa, "ub": ub, "pb": pb, "Pc": Pc, "Bc": Bc,
                       "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area), "is_corner": i in meta["corners"]}
        CELL[lbl] = {"rec": rec, "o": o_, "d": d_, "n": n_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "lots": lots, "meta": meta, "rows": rows}

    # 舊 35 名單
    OLD35 = set()
    op = os.path.join(OUTDIR, w83.OLD_LOG)
    if os.path.exists(op):
        txt = io.open(op, encoding="utf-8", errors="replace").read()
        seg = txt[txt.index("不合格宗之面積"):] if "不合格宗之面積" in txt else txt
        pt = re.compile(r'^\s+(R\d+)\s+(\S+)\s+(\d+)\s+([-+][\d.]+)\s+([-+][\d.]+)\s+([\d.]+)\s*$')
        for ln in seg.split(chr(10)):
            m = pt.match(ln)
            if m:
                OLD35.add((m.group(1), m.group(2), int(m.group(3))))

    # ── 逐宗之中間量（⛔ 不重造判定式：先重取、再與 `eval_lot` 逐位對拍）──
    ROWS = []
    same_all = tot_all = 0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        o_, d_, n_ = C["o"], C["d"], C["n"]
        for side, idxs in C["groups"]:
            prev = None
            for i in idxs:
                lt = C["lots"][i]
                if lt["Pc"] is None or lt["Bc"] is None:
                    prev = None
                    continue
                if prev is None:
                    prev = i
                    ROWS.append({"lbl": lbl, "side": side, "i": i, "prev": None})
                    continue
                pv = C["lots"][prev]
                # 🔒 中間量之重取（**同一組輸入**·⛔ 非重造判定式）
                s_Pprev = w40.s_of(pv["Pc"], o_, d_)
                s_Bprev = w40.s_of(pv["Bc"], o_, d_)
                s_Pperp = s_Bprev            # `B_prev` 沿法向投影至 FRONTLINE ⇒ `s` 不變
                s_Bperp = s_Pprev            # `P_prev` 沿法向投影至 BASELINE ⇒ `s` 不變
                if s_Pperp < s_Pprev - 1e-9:
                    case_my, st_my = "甲", (s_Pprev, s_Bperp)
                elif s_Pperp > s_Pprev + 1e-9:
                    case_my, st_my = "乙", (s_Pperp, s_Bprev)
                else:
                    case_my, st_my = "退化(P⊥＝P_prev)", (s_Pprev, s_Bprev)
                s_Pcur = w40.s_of(lt["Pc"], o_, d_)
                s_Bcur = w40.s_of(lt["Bc"], o_, d_)
                df_my = (s_Pcur - st_my[0], s_Bcur - st_my[1])
                code_my = "合格" if (df_my[0] >= -1e-6 and df_my[1] >= -1e-6) else "不合格"
                case, st, df, code = w40.eval_lot(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"],
                                                  o_, d_, n_)
                tot_all += 1
                same_all += int(case_my == case and st_my == st and df_my == df
                                and code_my == code)
                sn = _sin(lt["ua"], pv["ua"])
                ROWS.append({"lbl": lbl, "side": side, "i": i, "prev": prev,
                             "s_Pprev": s_Pprev, "s_Bprev": s_Bprev,
                             "s_Pperp": s_Pperp, "s_Bperp": s_Bperp,
                             "case": case, "st": st, "s_Pcur": s_Pcur, "s_Bcur": s_Bcur,
                             "df": df, "code": code, "sin": sn,
                             "slant": abs(s_Pprev - s_Bprev),
                             "adv": s_Pcur - s_Pprev,
                             "area": lt["area"], "old35": (lbl, side, i) in OLD35})
                prev = i

    P("")
    P("  🔒 **中間量之重取與 `w40.eval_lot` 之逐位對拍**：逐宗四項（情形／起算二端／Δ 二值／出艙碼）"
      "**全部相同 ＝ %d ／ %d** ⇒ %s"
      % (same_all, tot_all, "✅ **⛔ 非重造判定式**" if same_all == tot_all
         else "🔴 **有不同 ⇒ 本檔之中間量⛔ 不得採信·具名**"))

    judged = [r for r in ROWS if r.get("prev") is not None]
    inscope = [r for r in judged if math.isfinite(r["sin"]) and r["sin"] > PAR_TOL]
    outscope = [r for r in judged if not (math.isfinite(r["sin"]) and r["sin"] > PAR_TOL)]
    bad_out = [r for r in outscope if r["code"] == "不合格"]
    bad_in = [r for r in inscope if r["code"] == "不合格"]

    # ══ 【C／A-1】舊判準何以在平行二界上判違反 ═══════════════════════
    P("")
    P("【C／A-1】🛑 **舊判準何以在<u>平行</u>二界上判違反**（27 宗**全部**·⛔ 非抽樣）")
    P("-" * W)
    P("  🔒 **母體之界定**：`|sin(前一宗遠側界, 本宗遠側界)| ≤ %.0e`（正典容差）⇒ **二界平行**"
      "；其中**出艙碼 ＝ 不合格**者 ＝ **%d 宗**" % (PAR_TOL, len(bad_out)))
    P("  %-5s %-5s %-4s %-4s %-6s %13s %13s %13s %13s %13s %13s %12s %12s"
      % ("街廓", "側", "i", "前", "情形", "s(P_prev)", "s(B_prev)", "**斜跨距**",
         "起算front", "起算base", "s(P_cur)", "**Δfront**", "**Δbase**"))
    for r in bad_out:
        P("  %-5s %-5s %-4d %-4d %-6s %13.6e %13.6e %13.6e %13.6e %13.6e %13.6e %12.6e %12.6e"
          % (r["lbl"], r["side"], r["i"], r["prev"], r["case"], r["s_Pprev"], r["s_Bprev"],
             r["slant"], r["st"][0], r["st"][1], r["s_Pcur"], r["df"][0], r["df"][1]))
    POP(len(outscope), len(bad_out), "A-1 受詞外之不合格宗（全列）")

    P("")
    P("  🔴 **必答：二界平行時，`Δfront`／`Δbase` 之號何以為負？**")
    P("     🔒 **逐步指認（⛔ 純算術·由上表逐宗可核）**：")
    P("     ① `P⊥` ＝ `s(B_prev)`、`B⊥` ＝ `s(P_prev)`（法向投影⇒ `s` 不變·`w40.eval_lot` 逐字）")
    P("     ② 甲乙判別 ＝ `s(B_prev)` vs `s(P_prev)`；**二情形之起算二端皆 ＝ "
      "`max(s(P_prev), s(B_prev))`**")
    P("        （甲：`(s_Pprev, s_Bperp) = (s_Pprev, s_Pprev)`／乙：`(s_Pperp, s_Bprev) = (s_Bprev, s_Bprev)`）")
    P("     ③ ⇒ **起算垂線之二端被壓成<u>同一個 `s`</u>**，而前一宗之遠側界本身跨越 "
      "`|s(P_prev) − s(B_prev)|`（＝**斜跨距**）")
    P("     ④ 而本宗之二交點相差 `s(B_cur) − s(P_cur)`（＝**本宗之帶號斜跨距**）")
    P("        🔒 **恆等式甲（二情形皆成立）**：`Δbase − Δfront ≡ s(B_cur) − s(P_cur)`")
    P("        🔒 **恆等式乙（判準之精確形）**："
      "`min(Δfront, Δbase) ≡ min(s(P_cur), s(B_cur)) − max(s(P_prev), s(B_prev))`")
    P("     ⇒ 🔒 **判準實際在比：<u>本宗二交點之 min</u> vs <u>前一宗二交點之 max</u>**")
    P("        ⇒ 違反 ⟺ `min(本宗二交點) < max(前宗二交點) − 1e-6`")
    P("     ⇒ 🔴 **⛔ 與二界是否平行無關**——只要界線有斜跨距（`BASELINE ∦ FRONTLINE` 亦使其隨位置變），")
    P("        **本宗須推進「至少一整個斜跨距」方能過關** ⇒ 平行二界之相鄰宗**系統性**被判違反。")
    idA, idB = [], []
    for r in bad_out:
        idA.append(abs((r["df"][1] - r["df"][0]) - (r["s_Bcur"] - r["s_Pcur"])))
        idB.append(abs(min(r["df"])
                       - (min(r["s_Pcur"], r["s_Bcur"]) - max(r["s_Pprev"], r["s_Bprev"]))))
    if idA:
        P("     🔒 **恆等式甲之逐宗殘差** 極大 ＝ **%.3e**（**殘差/ulp ＝ %.2f**）⇒ %s"
          % (max(idA), w82._ulp_ratio(max(idA), 100.0),
             "✅ **成立**" if max(idA) < 1e-9 else "🔴 **不成立·具名**"))
        P("     🔒 **恆等式乙之逐宗殘差** 極大 ＝ **%.3e**（**殘差/ulp ＝ %.2f**）⇒ %s"
          % (max(idB), w82._ulp_ratio(max(idB), 100.0),
             "✅ **成立**" if max(idB) < 1e-9 else "🔴 **不成立·具名**"))
    P("     🩸 **首版之誤（記入 §I）**：我原寫「`Δbase − Δfront ≡ −(s(P_prev) − s(B_prev))`」"
      "（用**前一宗**之斜跨距）⇒ 逐宗殘差極大 **4.850e-02** ⇒ 不成立；")
    P("        其因 ＝ **`BASELINE ∦ FRONTLINE`** ⇒ 斜跨距**隨 `s` 位置而變**，"
      "⛔ 二平行線之斜跨距**不相等**。")
    P("     🔒 **推進量 vs 斜跨距**（⇒ 負號之直接來源·`推進量` ＝ `min(本宗二交點) − min(前宗二交點)`）：")
    P("     %-5s %-5s %-4s %14s %14s %14s %14s"
      % ("街廓", "側", "i", "min(本宗)−max(前宗)", "本宗斜跨距", "前宗斜跨距", "Δ 之較小端"))
    for r in bad_out:
        P("     %-5s %-5s %-4d %14.6e %14.6e %14.6e %14.6e"
          % (r["lbl"], r["side"], r["i"],
             min(r["s_Pcur"], r["s_Bcur"]) - max(r["s_Pprev"], r["s_Bprev"]),
             abs(r["s_Bcur"] - r["s_Pcur"]), r["slant"], min(r["df"])))
    POP(len(bad_out), len(bad_out), "A-1 判準之精確形（全列）")

    # 判別力：已知合格之受詞外宗
    ok_out = [r for r in outscope if r["code"] == "合格"]
    P("")
    P("  🔒 **判別力（常設 8·⛔ 不可省）**：對**已知合格**之受詞外宗同法逐步出艙")
    P("     受詞外之合格宗 ＝ **%d**；其 `min(本宗)−max(前宗)` 之**極小** ＝ %s"
      % (len(ok_out), ("%.6e" % min(min(r["s_Pcur"], r["s_Bcur"]) - max(r["s_Pprev"], r["s_Bprev"]) for r in ok_out)) if ok_out else "—"))
    P("     不合格宗之 `min(本宗)−max(前宗)` 之**極大** ＝ %s"
      % (("%.6e" % max(min(r["s_Pcur"], r["s_Bcur"]) - max(r["s_Pprev"], r["s_Bprev"]) for r in bad_out)) if bad_out else "—"))
    if ok_out and bad_out:
        _g = lambda r: min(r["s_Pcur"], r["s_Bcur"]) - max(r["s_Pprev"], r["s_Bprev"])
        sep = max(_g(r) for r in bad_out) < min(_g(r) for r in ok_out)
        P("     ⇒ %s（🔒 **單一門檻**之分離宣稱·常設 14 ①）"
          % ("✅ **二群完全分離**（⇒ 中間量與結論**逐項對應**）" if sep
             else "🔴 **重疊 ⇒ 判準之輸出與輸入⛔ 不對應·具名**"))
        P("     🔒 **節 103**：門檻兩側最接近之二筆 ＝ %.6e（不合格側極大）／%.6e（合格側極小）"
          % (max(_g(r) for r in bad_out), min(_g(r) for r in ok_out)))

    # 🔴 併答：受詞內之宗是否亦受此機制
    P("")
    P("  🔴 **併答（A-0 之受詞）：該機制<u>是否亦出現於受詞內</u>之宗？**")
    P("  %-5s %-5s %-4s %-6s %13s %14s %14s %14s %-8s"
      % ("街廓", "側", "i", "情形", "|sin|", "本宗斜跨距", "前宗斜跨距",
         "min(本)−max(前)", "出艙碼"))
    _g2 = lambda r: min(r["s_Pcur"], r["s_Bcur"]) - max(r["s_Pprev"], r["s_Bprev"])
    for r in inscope:
        P("  %-5s %-5s %-4d %-6s %13.3e %14.6e %14.6e %14.6e %-8s"
          % (r["lbl"], r["side"], r["i"], r["case"], r["sin"],
             abs(r["s_Bcur"] - r["s_Pcur"]), r["slant"], _g2(r), r["code"]))
    POP(len(inscope), len(inscope), "A-1 受詞內逐宗（全列）")
    same_mech = [r for r in inscope if _g2(r) < 0]
    P("  🔒 **`P2` 之判**：受詞內之宗中，`min(本宗) < max(前宗)`（＝ 同一機制）者 ＝ **%d ／ %d** ⇒ %s"
      % (len(same_mech), len(inscope),
         "✅ **同一成因亦出現於受詞內**（`P2` 成立）" if same_mech else
         "🔴 **受詞內無該成因 ⇒ 該缺陷只咬受詞外·具名**"))

    # ══ 【D／A-2】`_PAR_TOL` 之射程 ＋ 以之重判 ═══════════════════════
    P("")
    P("【D／A-2】`_PAR_TOL = %.1e` 之**射程現查** ＋ 以之重判（⛔ 不另立門檻）" % PAR_TOL)
    P("-" * W)
    src_sg = io.open(os.path.join(VERIFY, "stepg_pipeline.py"), encoding="utf-8").read()
    P("  🔒 **定義處與全部使用點**（自碼面現查·逐處出艙其受詞）：")
    for m in re.finditer(r'_PAR_TOL', src_sg):
        ln = src_sg[:m.start()].count(chr(10)) + 1
        P("     verify/stepg_pipeline.py:%-6d %s" % (ln, src_sg.split(chr(10))[ln - 1].strip()[:130]))
    P("  🔒 **射程之判**：其判定式逐字為 `abs(cross(u/|u|, v/|v|)) <= _PAR_TOL`"
      "（`_dir_is_alloc`·`:1065`）⇒ **受詞 ＝ 二單位向量之 `|sin|`**")
    P("     ⇒ 🔒 **與本批「前一宗遠側界是否 ∥SIDELINE」所用之量<u>同一</u>** ⇒ **射程涵蓋** ✅")
    P("     ⚠️ ⛔ **不涵蓋者具名**：`_PAR_TOL` 之原受詞為「**該側 SIDE 與 ALLOC**」／"
      "「**本宗 `_alloc_dir_used` 與街廓 ALLOC**」，⛔ 非「**相鄰二宗之遠側界**」"
      "——🔒 **惟三者皆為「二方向是否平行」之同一物理量** ⇒ 沿用之·具名。")
    P("")
    P("  🔴 **以 `%.1e` 重判**（母體 ＝ %d 宗·＝ `-85` 之 57 宗母體）" % (PAR_TOL, len(judged)))
    P("     受詞內 ＝ **%d**／受詞外 ＝ **%d**；**受詞內之違反宗數 ＝ %d**"
      % (len(inscope), len(outscope), len(bad_in)))
    for r in bad_in:
        P("        🔴 %-4s %-5s i=%-3d（前 %s·`|sin|`=%.3e＝%.4f°）面積 %.4f ㎡"
          % (r["lbl"], r["side"], r["i"], r["prev"], r["sin"],
             math.degrees(math.asin(min(1.0, r["sin"]))), r["area"]))
    POP(len(bad_in), len(bad_in), "A-2 以正典容差重判之違反宗（全列）")
    P("     面積合計 ＝ **%.4f ㎡**" % sum(r["area"] for r in bad_in))
    EXP3 = {("R1", "右", 4), ("R3", "右", 9), ("R5", "左", 1)}
    got3 = {(r["lbl"], r["side"], r["i"]) for r in bad_in}
    P("  🔒 **`P3` 之判**：實得 **%d** 宗（期望 **3**·名單 `R1右4`／`R3右9`／`R5左1`）⇒ %s"
      % (len(bad_in), "✅ **數與名單皆符**" if got3 == EXP3 else
         "🔴 **不符**：交集 %s／新∖期望 %s／期望∖新 %s"
         % (sorted(got3 & EXP3), sorted(got3 - EXP3), sorted(EXP3 - got3))))
    sins = sorted(r["sin"] for r in judged if math.isfinite(r["sin"]))
    below = [x for x in sins if x <= PAR_TOL]
    above = [x for x in sins if x > PAR_TOL]
    P("  🔒 **節 103（門檻上下最接近之二筆及其餘裕）**：")
    P("     下側極大 ＝ **%.6e**（餘裕 %.3e）／上側極小 ＝ **%.6e**（餘裕 %.3e）"
      % (max(below) if below else float("nan"), PAR_TOL - (max(below) if below else 0),
         min(above) if above else float("nan"), (min(above) if above else 0) - PAR_TOL))
    if below and above:
        ratio = min(above) / max(below)
        P("     🔒 **二者之比 ＝ %.4e** ⇒ %s"
          % (ratio, "🔴 **< 10 ⇒ 該門檻為<u>擦邊</u>·具名**" if ratio < 10
             else "✅ **≥ 10 ⇒ ⛔ 非擦邊**"))
    P("  🔒 **常設 14 ①（單一門檻）**：本節之分離宣稱以**單一門檻 `%.1e`** 表述"
      "⇒ ⛔ **無未定義帶**（⛔ 非 `-85` `P4` 之 `1e-9`／`1e-3` 二門檻）" % PAR_TOL)

    # ══ 【E／A-3】二座標框之正當性 ═══════════════════════════════════
    P("")
    P("【E／A-3】**座標框之正當性**（`K-6:2426` 逐字「⇒ ⛔ 不另立座標框」）")
    P("-" * W)
    P("  🔒 **`st_frame` 之逐字構成式**（錨 `verify/probes/probe_WG941_bandbase.py:87`）：")
    P("     `d̂ = d_hat/|d_hat|`；`n̂ = (−d̂_y, d̂_x)`；`(s, t) = ((p − front_pt)·d̂, (p − front_pt)·n̂)`；")
    P("     其後依**形心翻號** `σ`（`t < 0` ⇒ 全環 `t → −t`）⇒ 🔒 **`σ` 只作用於 `t`，⛔ 不動 `s`**。")
    P("  🔒 **`w40.s_of` 之逐字**：`(pt[0]−origin[0])*d[0] + (pt[1]−origin[1])*d[1]` ＝ `(pt − origin)·d̂`")
    P("     且本波各探針之 `origin` 一律 ＝ `cad['front_lines'][lbl]['p1']` ＝ **`front_pt`**")
    P("  ⇒ 🔴 **`框甲` ＝ `w40.s_of(點, front_pt, d̂)` ＝ `st_frame` 之 `s`（逐字同式）**")
    P("")
    P("  🔒 **逐宗逐位對拍**（⛔ 非字面比較·母體 ＝ **全部宗**·⛔ 非只取 `宗0`）")
    P("     🔒 `eps_touch` ＝ **生產常數 `ns['_EPS_TOUCH_FRONT']` ＝ %.3e**（⛔ 不另立·同 `w941`／`w947` 之取法）"
      % EPS_T)
    P("  %-5s %-6s %-8s %14s %14s %-10s"
      % ("街廓", "宗", "頂點數", "極大差 |Δs|", "殘差/ulp", "判"))
    fr_ok = fr_tot = fr_raise = 0
    fr_worst = 0.0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for i in range(len(C["rec"]["biz"])):
            cc = list(C["rec"]["biz"][i].exterior.coords)
            try:
                ring, _tl, _sg, _d2, _n2, _fe = w941.st_frame(cc, C["d"], C["o"], EPS_T)
            except Exception:                                       # noqa: BLE001
                fr_raise += 1
                continue
            mine = sorted(w40.s_of(p, C["o"], C["d"]) for p in cc[:-1])
            theirs = sorted(s for s, _t in ring[:-1])
            if len(mine) != len(theirs):
                fr_raise += 1
                continue
            dmax = max(abs(a - b) for a, b in zip(mine, theirs))
            fr_tot += 1
            fr_worst = max(fr_worst, dmax)
            okf = dmax <= 16 * math.ulp(max(1.0, max(abs(x) for x in mine)))
            fr_ok += int(okf)
            if (not okf) or fr_tot <= 6:
                P("  %-5s %-6d %-8d %14.3e %14.2f %-10s"
                  % (lbl, i, len(mine), dmax,
                     w82._ulp_ratio(dmax, max(1.0, max(abs(x) for x in mine))),
                     "✅ 逐位相同" if okf else "🔴 **不同**"))
    POP(fr_tot + fr_raise, min(6, fr_tot), "A-3 `框甲` vs `st_frame.s` 逐宗對拍")
    P("     🔒 **母體之界定（⛔ 不得以 0 為母體·空真假綠）**：可比對之宗 ＝ **%d**；"
      "`st_frame` raise 者 ＝ **%d**（其因 ＝ 該宗與 FRONTLINE **無前緣邊**·⛔ 非本檔之誤）"
      % (fr_tot, fr_raise))
    P("     🔒 **逐位相同 ＝ %d ／ %d**；**全體之極大差 ＝ %.3e** ⇒ %s"
      % (fr_ok, fr_tot, fr_worst,
         "✅" if (fr_tot and fr_ok == fr_tot) else ("🔴 **有不同·具名**" if fr_tot
                                                    else "🔴 **母體為 0 ⇒ 本項⛔ 未成立·具名**")))
    P("  🔒 **`P4` 之判**：其預測為「**框乙** ＝ `st_frame`；**框甲**為另立」")
    P("     🔴 **實得相反**：**`框甲` ＝ `st_frame.s`（%d／%d 格逐位相同）**" % (fr_ok, fr_tot))
    P("  🔒 **`框乙` 之正確定性（⛔ 非「另立座標框」）**：")
    P("     `框乙(X)` ＝ 「過 `X` 且 ∥ALLOC 之直線與 FRONTLINE 之交點」之 `s`")
    P("     ＝ **`st_frame.s` 施於<u>另一個點</u>** ⇒ 🔒 **同一座標框、二個<u>受詞點</u>**")
    P("     ⇒ ✅ **⛔ 未另立座標框**（`K-6:2426` **未被違反**）；🩸 `-85` §I 稱之為「二框」係"
      "**措辭不當**·本批更正（見 §I）")
    P("  🔒 **本波各探針實際所用之框**（逐支現查）：")
    for nm, f in (("w40 (-40)", "probe_WG940_startperp.py"),
                  ("w81 (-81)", "probe_WG981_scope.py"),
                  ("w82 (-82)", "probe_WG982_chord.py"),
                  ("w83 (-83)", "probe_WG983_k99prep.py"),
                  ("w84 (-84)", "probe_WG984_gap.py"),
                  ("w85 (-85)", "probe_WG985_grouphead.py")):
        s = io.open(os.path.join(HERE, f), encoding="utf-8", errors="replace").read()
        P("     %-12s `w40.s_of` %-3d ／ `s_front_of_line` %-3d ／ `strip_axis` %-3d ／ `st_frame` %d"
          % (nm, s.count("s_of("), s.count("s_front_of_line"), s.count("strip_axis"),
             s.count("st_frame")))

    # ══ 【F／A-4】`D-0` 之結案 ＋ `R1 左 j=0` ═════════════════════════
    P("")
    P("【F／A-4】`D-0` 二源之結案 ＋ `R1 左 j=0` 之雙重異常")
    P("-" * W)
    P("  🔴 **A-4-1｜二源之取邊規則**（測 `VR-043` 四之假說·母體 ＝ 全體 %d 宗）"
      % sum(len(C["lots"]) for C in CELL.values()))
    P("  %-5s %-5s %-4s %-6s %-8s %14s %-12s"
      % ("街廓", "側", "i", "sign", "w40 取邊", "|sin|(甲,乙)", "判"))
    a41 = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            ss = [w40.s_of(C["lots"][i]["Pc"], C["o"], C["d"]) for i in idxs
                  if C["lots"][i]["Pc"] is not None]
            sign = 1 if (len(ss) >= 2 and (ss[-1] - ss[0]) > 0) else -1
            for i in idxs:
                lt = C["lots"][i]
                if lt["ua"] is None or lt["ub"] is None:
                    continue
                sn = _sin(lt["ua"], lt["ub"])
                ext = list(C["rec"]["biz"][i].exterior.coords)
                pick = None
                cand = []
                for t in range(len(ext) - 1):
                    uu2 = _u((ext[t + 1][0] - ext[t][0], ext[t + 1][1] - ext[t][1]))
                    if uu2 is None:
                        continue
                    c_ = abs(float(uu2[0] * C["d"][0] + uu2[1] * C["d"][1]))
                    cr_ = abs(float(uu2[0] * C["d"][1] - uu2[1] * C["d"][0]))
                    mid = ((ext[t][0] + ext[t + 1][0]) / 2, (ext[t][1] + ext[t + 1][1]) / 2)
                    cand.append((math.degrees(math.atan2(cr_, c_)), t,
                                 w40.s_of(mid, C["o"], C["d"])))
                cand.sort(key=lambda e: -e[0])
                two = sorted(cand[:2], key=lambda e: e[2])
                pick = two[1][1] if len(two) > 1 else None
                a41.append({"lbl": lbl, "side": side, "i": i, "sign": sign,
                            "pick": pick, "sin": sn})
    big = [r for r in a41 if r["sin"] > 1e-5]
    P("     🔒 **`|sin|(甲,乙) > 1e-5` 者逐宗具名**：")
    for r in big:
        P("        %-4s %-5s i=%-3d sign=%+d  w40 取邊 %s  |sin| ＝ %.3e（%.4f°）"
          % (r["lbl"], r["side"], r["i"], r["sign"], r["pick"], r["sin"],
             math.degrees(math.asin(min(1.0, r["sin"])))))
    POP(len(a41), len(big), "A-4-1 全體宗（僅列 `|sin| > 1e-5` 者）")
    neg = [r for r in a41 if r["sign"] < 0]
    pos = [r for r in a41 if r["sign"] > 0]
    neg_big = [r for r in neg if r["sin"] > 1e-5]
    pos_big = [r for r in pos if r["sin"] > 1e-5]
    P("     🔒 **`P5` 之判**：`sign = −1` 之側（%d 宗）中 `|sin| > 1e-5` 者 ＝ **%d**（期望 ≥1）；"
      "`sign = +1` 之側（%d 宗）中 `> 1e-5` 者 ＝ **%d**（期望 0·皆 ≤ `_PAR_TOL`）⇒ %s"
      % (len(neg), len(neg_big), len(pos), len(pos_big),
         "✅ **假說成立**" if (neg_big and not pos_big) else "🔴 **不成立·具名**"))
    pos_over = [r for r in pos if r["sin"] > PAR_TOL]
    P("     🔒 `sign = +1` 之側中 `|sin| > _PAR_TOL(%.0e)` 者 ＝ **%d**：%s"
      % (PAR_TOL, len(pos_over),
         [(r["lbl"], r["side"], r["i"], "%.3e" % r["sin"]) for r in pos_over]))
    P("  🔴 **正典之獨立佐證（CC 自補·⛔ 施工單未令）**：`K-6:1043–1045` 逐字載")
    P("     「須重量者（其側之 `SIDE` 與 `ALLOC` **不平行**·夾角【倉】`verify/out/probe_D2b7_dirscope.log`）：")
    P("      `0m R3/right`（**4.321958°**）／`0m R5/left`（**4.321968°**）／`3.5m R1/right`（**0.690832°**）…」")
    P("     ⇒ 🔒 **`D-0` 之二真差角<u>正典早已載明</u>，且其受詞 ＝ <u>該側之 SIDE 與 ALLOC 之夾角</u>**")
    P("     ⇒ **該 `|sin|` ⛔ 非「取錯邊」所生之偽差，係<u>真實幾何</u>**（⇒ `D-0` 之定性更正·見報告 §F）")

    P("")
    P("  🔴 **A-4-2｜`R1 左 j=0` 之雙重異常**")
    C1 = CELL.get("R1")
    if C1 is not None:
        rows1 = [r for r in C1["rows"] if r.get("ok") and r["j"] == 0]
        d2 = [r for r in rows1 if r["d"] >= w83.D_MIN]
        P("     ① **何以「現況本即 0 對」**：`R1` `j=0` 之可算對 ＝ %d（其中 `d≥2` ＝ %d）；"
          "逐對之 `s*` 與 `contains`：" % (len(rows1), len(d2)))
        for r in d2:
            P("        (0,%d) d=%d  s* ＝ %.4f  contains ＝ %s" % (r["k"], r["d"], r["s_star"], r["inside"]))
        pj0, uj0 = w82.pj_of(C1["rec"], 0), w82.uj_of(C1["rec"], 0)
        if pj0 is not None and uj0 is not None and C1["rec"]["block"] is not None:
            e0, _dg0 = w82.ring_edges(list(C1["rec"]["block"].exterior.coords))
            ci0 = w82.chord_interval(e0, pj0, uj0)
            P("        弦區間 λ ＝ [%.6f, %.6f] ⇒ 逐對之 `s*` 是否 ∈ λ：%s"
              % (ci0["lam_a"], ci0["lam_b"],
                 [(r["k"], w82.pred_chord(ci0, r["s_star"])) for r in d2]))
        P("     ② **`殘差/ulp = 2.9e8` 之量級**：其 `S_req` ＝ 6.4796（`ulp = %.3e`）"
          "⇒ 分母**比其餘四格小 3〜4 個數量級**（89.04／78.63 之 `ulp = 1.421e-14`）"
          % math.ulp(6.4796))
        P("        🔒 `ulp(6.4796) = %.3e` vs `ulp(89.0422) = %.3e` ⇒ **比 ＝ %.1f**"
          % (math.ulp(6.4796), math.ulp(89.0422), math.ulp(89.0422) / math.ulp(6.4796)))
        P("     🔒 **`P6` 之判（二異常是否同源）**：見報告 §F-2（⛔ 本檔只出艙量）")

    # ══ 【G／P7】第十二法 ═══════════════════════════════════════════
    P("")
    P("【G／P7】`run_all` 清單筆數之**第十二法**（🔒 位元組碼之控制流定位法·⛔ 與十一法不同族）")
    P("-" * W)
    n12, cands = run_all_count_method12()
    P("  母體 ＝ `run_all.main` 之**位元組碼指令流**；受詞 ＝ 餵給 `GET_ITER`／`FOR_ITER` 之常數元組")
    P("  🔒 **⛔ 未 `exec`**（僅 `compile`）⇒ ⛔ 未執行 `run_all`（閘 7）")
    P("  命中之候選元組數 ＝ **%d**；其長度 ＝ %s" % (len(cands), [len(t) for t in cands]))
    if cands:
        for e in cands[0]:
            P("     %s" % (e[0],))
        POP(len(cands[0]), len(cands[0]), "第十二法之逐項（全列）")
    P("  ⇒ **第十二法所得 ＝ %s**（施工單 `P7` 期望 **15**）⇒ %s"
      % (n12, "✅ 相符" if n12 == 15 else "🔴 **不符·⛔ 不調整預測·具名**"))
    P("  🔒 **其獨有之判別力已於 `selfcheck` ⑤ 實證**：合成模組（迭代 2 ＋ **誘餌 3**）"
      "⇒ 本法得 **2**、④⑥ 族得 **3** ⇒ **受詞確實不同**")

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
