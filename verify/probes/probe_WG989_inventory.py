# -*- coding: utf-8 -*-
r"""**W-G.9-89 §二 A 組**：以**權威源**重判歷批名單 ＋ `far_side_dir_and_pt` 使用點全查
＋ **落地介面清單**（⛔ 只列不建）＋ 落地之影響母體。

## 受詞（施工單 `W-G.9-89` §二·`VR-047` 六）
- **A-1**（🛑 第一項）以**權威源 ＝ 解算面**（`faces_of(...)[1]`·`VR-047` 二）重判
  `-40`／`-83`（35 宗）／`-85`（8／3 宗）／`-87`（25 宗）／`-88`（2 宗·自洽）之名單。
- **A-2** `far_side_dir_and_pt` 之**使用點全查**（🔴 含 `app.py`·停機條款②）。
- **A-3** **落地介面清單**（`K-9-12`＋`K-9-13`／`②-宗` 錨點更正·⛔ 只列不建）。
- **A-4** **落地之影響母體**（12 格·⛔ 只數不算後果）＋ 現況基線。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單係**盤點**。其瑕若使**清單偏短**（漏列使用點／漏列缺口）⇒ 落地時才發現
⇒ 🔴 **代價落在生產碼那一批**。
🔒 **事前選定：偏向<u>多列</u>**——凡「是否算一個使用點／是否算一個缺口」不確定者，
**一律列入並具名其不確定**（⇒ 清單偏長之代價 ＝ 多讀幾行）。

## 🩸 自身污染之防（`-88` §I-3·施工單 §一-⑨ 明令「逐字出艙該排除」）
凡掃 `verify/probes/` 之母體，**須排除本檔自身**（本檔 docstring 內即寫有
`far_side_dir_and_pt` 等受詞字樣）⇒ 見輸出之 `SELF` 行；⛔ 不得默默排除、⛔ 不得不排除。

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
`w82.chord_interval`／`pred_chord`／`ring_edges`／`pj_of`／`uj_of`、
`w88.s_star_of`／`margin_of`（**權威源之判定**）、`w87.eval_exact`（正典逐字·組⑦）、
`w40.eval_lot`／`far_side_dir_and_pt`／`line_isect`／`s_of`、`w81.analyse_cell`／`faces_of`／`_u`、
`w86.PAR_TOL`／`_sin`，以及**生產碼**之 `evaluate_parcel_width_n14`／`parcel_min_width_n14`
（自 `harvest()` 之 `ns` 取）皆**原樣**使用。🔒 **⛔ 不重造任何判定式。**

## ⛔ 本檔不做（施工單 §二 A-5 八款）
⛔ 零 `app.py` 變更；⛔ `data/`／`docs/rulings/` 零變更；🔴 ⛔ **不建任何介面**；
⛔ 不落地 `K-9-12`／`K-9-13`／`K-9-15`／錨點更正；⛔ 不換圖／不重烤／不改 baseline；
⛔ 不改舊命名、⛔ 不修史；⛔ 不另立門檻／座標框／交叉判準；
⛔ 不出艙「應改領現金之宗」；⛔ 不以「理論上恆真」代替實算；
🔴 ⛔ **不得以 `A-1` 之產物作為土地結論**（其判準已由 `K-9-15` 廢止·只換源）；
🔴 ⛔ **不得提出落地之排程建議**（排程屬 KL·§一-⑨②：正典未規定順序）。

## 🔒 常設條款
**8** 每判準附「會使它為否」之輸入；**9** 門檻併出艙量級與 `math.ulp`、跨數量級**分層**；
**10** 每表末印 `POPULATION/PRINTED/SUPPRESSED`；**11** ⛔ 不經 shell 傳字樣（`Write` 落盤）；
**12／13** 搜尋規格含正典款號組＋三類出處分類；**14** 單一門檻＋`m／n` 併出艙判別力為零者；
**15**（節 110 ＋ `自誤 92`）① 解釋既有款須逐字引原文；
② **凡預測含一份名單，須逐字寫出「產生批次 ＋ 產生指令 ＋ 所用之源」三者**；
③ **凡倉內存在未結之二源爭議，其下游產物一律標記「繫於 `X` 之未結」**（標記之責在引用者）。
"""
import contextlib
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

import shapely                                                      # noqa: E402

import probe_WG981_scope as w81                                     # noqa: E402
import probe_WG982_chord as w82                                     # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402
import probe_WG983_k99prep as w83                                   # noqa: E402
import probe_WG984_gap as w84                                       # noqa: E402
import probe_WG985_grouphead as w85                                 # noqa: E402
import probe_WG986_oldjudge as w86                                  # noqa: E402
import probe_WG987_exact as w87                                     # noqa: E402
import probe_WG988_nocross as w88                                   # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 210
SB = 0.0                       # 🔒 情境母體 ＝ 僅 0m（⛔ 不擴·具名）

PAR_TOL = w86.PAR_TOL          # 🔴 正典容差（`K-6:1010`）·⛔ 不另立
TOL_85 = 1e-9                  # 🔒 `-85` 之受詞門檻（**該批所用**·⛔ 非本批另立·供對帳）

_u = w81._u
s_star_of = w88.s_star_of      # 🔒 原樣（⛔ 不重造）
margin_of = w88.margin_of

# 🩸 自身污染之防：掃 `verify/probes/` 時**排除本檔**（⛔ 不默默排除）
SELF = os.path.relpath(os.path.abspath(__file__), REPO).replace(os.sep, "/")


def _short_head():
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                              capture_output=True, text=True).stdout.strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG989_inventory_%s.log" % COMMIT)


# ══════════════════════════════════════════════════════════════════════════
#  🔒 第十五法：**`ast.unparse` 之往返（round-trip）法**
#     受詞 ＝ **由 AST <u>重新生成</u>之文本**（⛔ 非原始碼文本、⛔ 非位置切片（⑭）、
#     ⛔ 非行號區間（⑬）、⛔ 非常數池（④⑥）、⛔ 非運算元（⑫））。
#     🔒 其獨有之判別力：`unparse` 會**正規化掉註解／續行** ⇒ 對「元組內含註解」之案，
#        ⑭（原始碼切片）會把註解內之 `.py` 一併數進去，而 ⑮ 不會。
# ══════════════════════════════════════════════════════════════════════════
def run_all_count_method15(src=None, path=None):
    """回 (筆數, 名單, unparse 之長度)。⛔ 僅 `ast.parse`／`ast.unparse`·⛔ 未 `compile`／`exec`。"""
    import ast
    if src is None:
        path = os.path.join(VERIFY, "run_all.py")
        src = io.open(path, encoding="utf-8").read()
    best = None
    for node in ast.walk(ast.parse(src, path or "<src>")):
        if not isinstance(node, (ast.For, ast.AsyncFor)):
            continue
        gen = ast.unparse(node.iter)
        names = re.findall(r'["\']([A-Za-z0-9_./]+\.py)["\']', gen)
        if names and (best is None or len(names) > len(best[0])):
            best = (names, len(gen))
    if best is None:
        return 0, [], 0
    return len(best[0]), best[0], best[1]


# ══════════════════════════════════════════════════════════════════════════
def selfcheck(P, ns):                                               # noqa: C901
    ok = {}
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·每項皆附**已知真／已知偽**對照）")
    P("-" * W)

    # ① `w88.s_star_of` 原樣可用（已知真／已知偽）
    st1, sa1, ds1 = s_star_of((0.0, 0.0), (1.0, 0.0), (5.0, 3.0), (0.0, 1.0))
    st2, sa2, ds2 = s_star_of((0.0, 0.0), (1.0, 0.0), (0.0, 4.0), (1.0, 0.0))
    ok["①"] = (abs(st1 - 5.0) < 1e-12 and math.isnan(st2) and sa2 == 0.0)
    P("  ① **`w88.s_star_of` 原樣**：已知【相交於 s*=5】⇒ **%.6f**（期望 5）／"
      "已知【平行】⇒ `sin_a` ＝ %.3e·`s*` ＝ **%s**（期望 nan）⇒ %s"
      % (st1, sa2, st2, "PASS" if ok["①"] else "🔴 FAIL"))

    # ② `w82.pred_chord` 已知真／已知偽
    edges, _dg = w82.ring_edges(w82.SQ_CCW)
    ci = w82.chord_interval(edges, (0.0, 5.0), (1.0, 0.0))
    ok["②"] = (w82.pred_chord(ci, 5.0) and not w82.pred_chord(ci, 1e6))
    P("  ② **`w82.pred_chord` 原樣**：`λ` ＝ [%.6f, %.6f]；`s*=5` ⇒ **%s**／`s*=1e6` ⇒ **%s** ⇒ %s"
      % (ci["lam_a"], ci["lam_b"], w82.pred_chord(ci, 5.0), w82.pred_chord(ci, 1e6),
         "PASS" if ok["②"] else "🔴 FAIL"))

    # ③ **生產判定器** `evaluate_parcel_width_n14` 之判別力（常設 8·`P6` 之前置）
    ev = ns["evaluate_parcel_width_n14"]
    fl = {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}
    wide = {"cut_coords": [(10, 0), (30, 0), (30, 20), (10, 20), (10, 0)], "推進側別": "左"}
    narrow = {"cut_coords": [(10, 0), (11, 0), (11, 20), (10, 20), (10, 0)], "推進側別": "左"}
    r_w = ev(dict(wide), fl, 14.0, 3.5, _label="selfcheck·寬")
    r_n = ev(dict(narrow), fl, 14.0, 3.5, _label="selfcheck·窄")
    ok["③"] = (r_w.get("寬度判定") == ns["WIDTH_VERDICT_OK"]
               and r_n.get("寬度判定") == ns["WIDTH_VERDICT_BAD"])
    P("  ③ **生產判定器 `evaluate_parcel_width_n14` 之判別力（常設 8）**：")
    P("     已知【寬 20m ≥ 3.5】⇒ 判 **%s**（實測寬 %s）／已知【窄 1m < 3.5】⇒ 判 **%s**（實測寬 %s）⇒ %s"
      % (r_w.get("寬度判定"), r_w.get("實際寬度(m)"), r_n.get("寬度判定"), r_n.get("實際寬度(m)"),
         "PASS" if ok["③"] else "🔴 FAIL"))
    P("     🔒 ⇒ **該判定器⛔ 非恆真**（⛔ 亦非恆偽）——`P6` 之前置成立")

    # ④ 第十五法之判別力（⛔ 與 ⑭ 不同族之**具鑑別力**合成案）
    # 🩸 **首版之誤（§I）**：誘餌**未加引號** ⇒ ⑭ 之 regex（要求**引號包夾**）不咬
    #    ⇒ ⑭ 亦得 2 ⇒ **該合成案⛔ 無判別力**（自檢如實擋下出艙）。修法：誘餌**加引號**。
    syn = ("def main():\n"
           "    for f in ('a.py',  # 'decoy_in_comment.py'\n"
           "              'b.py'):\n"
           "        pass\n")
    n15, l15, _ln = run_all_count_method15(syn, "<syn>")
    n14, l14, _pos = w88.run_all_count_method14(syn, "<syn>")
    ok["④"] = (n15 == 2 and n14 == 3)
    P("  ④ **第十五法之判別力（常設 8）**：合成案 ＝ 元組內含**註解**（其中有一個 `.py` 誘餌）")
    P("     ⇒ **第十五法 ＝ %d**（期望 2·名單 %s）／**第十四法 ＝ %d**（期望 3·名單 %s）⇒ %s"
      % (n15, l15, n14, l14, "PASS" if ok["④"] else "🔴 FAIL"))
    P("     🔒 ⇒ **二法之受詞確實不同**（⑭ ＝ **原始碼切片**·含註解／⑮ ＝ **`unparse` 重生之文本**·註解已正規化）")

    # ⑤ 常設 9
    P("  ⑤ **常設 9**：`PAR_TOL = %.1e` 施於 `|sin|` ∈ [0,1]（`ulp(1.0) = %.3e`）⇒ 門檻/ulp ＝ %.3e；"
      "`TOL_85 = %.1e` 係 **`-85` 該批所用之門檻**（⛔ 本批未另立·僅供對帳）"
      % (PAR_TOL, math.ulp(1.0), PAR_TOL / math.ulp(1.0), TOL_85))

    allok = all(ok.values())
    P("  ⇒ 量測器自檢：%s" % ("PASS" if allok else "🛑 FAIL ⇒ 停機·本次量測⛔ 不得出艙"))
    return allok


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

    def POP(pop, printed, tag):
        P("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # %s" % (pop, printed, pop - printed, tag))
        if printed != pop:
            P("     ⚠️ `PRINTED ≠ POPULATION` ⇒ 🔒 **本表之結論一律以 `POPULATION` 為分母**"
              "（⛔ 表身列數不得作為母體·節 105）")

    P("=" * W)
    P("【W-G.9-89 §二 A 組】權威源之回溯重判／`far_side_dir_and_pt` 使用點全查／落地介面清單／影響母體")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向<u>多列</u>**（⛔ 清單寧長勿短·不確定者列入並具名）")
    P("  🔴 **權威源 ＝ 解算面**（`faces_of(...)[1]`·`VR-047` 二·⛔ 非 `w40.far_side_dir_and_pt`）")
    P("  🩸 **自身污染之排除（逐字）**：掃 `verify/probes/` 之母體**排除** `%s`" % SELF)
    P("  🔒 情境母體 ＝ **僅 %gm**（⛔ 不擴·具名）" % SB)

    ns, fake_st = harvest()
    if not selfcheck(P, ns):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    # ── 驅動（同 `-88` 之構造·⛔ 不可 import·逐字具名之差；🆕 併**捕獲 `g_rows`**）──
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
    GROWS, GERR = {}, {}
    try:
        for lbl in blks:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    _res = run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                      [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                      wins, forced, SB)
                    GROWS[lbl] = list(_res.get("g_rows") or [])
                except Exception as e:                              # noqa: BLE001
                    GERR[lbl] = "%s: %s" % (type(e).__name__, str(e)[:110])
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(w81.CAP)
    FL, BL = cad.get("front_lines") or {}, cad.get("baselines") or {}
    P("")
    P("【驅動】`%gm` × R1–R6——攔截 **%d 格**；`g_rows` 取得之街廓 ＝ **%d**（raise 者 **%d**·⛔ 逐項具名）"
      % (SB, len(REAL), len(GROWS), len(GERR)))
    for k, v in GERR.items():
        P("     ⚠️ %s raise：%s" % (k, v))

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
        edges, _dg = (w82.ring_edges(list(rec["block"].exterior.coords))
                      if rec["block"] is not None else (None, None))
        lots = {}
        for i in range(len(rec["biz"])):
            ua, pa = w40.far_side_dir_and_pt(rec["biz"][i], d_)     # 源甲（🛑 已失權威）
            uj, pj = w82.uj_of(rec, i), w82.pj_of(rec, i)           # 源乙 ＝ **權威源**
            PcA = BcA = PcB = BcB = None
            if ua is not None:
                PcA = w40.line_isect(tuple(pa), tuple(ua), o_, d_)
                BcA = w40.line_isect(tuple(pa), tuple(ua), bpt, bdir)
            if uj is not None and pj is not None:
                PcB = w40.line_isect(tuple(pj), tuple(uj), o_, d_)
                BcB = w40.line_isect(tuple(pj), tuple(uj), bpt, bdir)
            lots[i] = {"ua": ua, "pa": pa, "uj": uj, "pj": pj,
                       "PcA": PcA, "BcA": BcA, "PcB": PcB, "BcB": BcB,
                       "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area), "is_corner": i in meta["corners"]}
        CELL[lbl] = {"rec": rec, "o": o_, "d": d_, "n": n_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "lots": lots, "meta": meta, "rows": rows,
                     "edges": edges, "sl": (cad.get("side_lines_by_side") or {}).get(lbl) or {}}

    # ══ 【C／A-1】以權威源重判歷批名單 ═════════════════════════════════
    P("")
    P("【C／A-1】🛑 **以權威源重判歷批一切名單**（⛔ 只換<u>源</u>·⛔ 不換判準）")
    P("-" * W)
    P("  🔒 **節 110 ②（`自誤 92` 修法）：每一份名單須逐字寫出「產生批次 ＋ 產生指令 ＋ 所用之源」**")
    P("  🔴 ⛔ **本節之產物⛔ 不得作為土地結論**——`-40`／`-83`／`-85`／`-87` 之**判準**"
      "（起算垂線端點）已由 `K-9-15` 廢止；本節只量「**源之影響**」。")
    ROWS = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            s_mid = {}
            for sd, ix in C["groups"]:
                v = [(C["lots"][t]["s_lo"] + C["lots"][t]["s_hi"]) / 2.0 for t in ix]
                s_mid[sd] = (sum(v) / len(v)) if v else float("nan")
            is_low = all(not math.isfinite(s_mid[k2]) or s_mid[side] <= s_mid[k2] for k2 in s_mid)
            adv = +1 if is_low else -1
            ordmap = {t: q for q, t in enumerate(idxs)}
            prevA = prevB = None
            for i in idxs:
                lt = C["lots"][i]
                r = {"lbl": lbl, "side": side, "i": i, "adv": adv,
                     "ord": ordmap.get(i), "area": lt["area"],
                     "is_corner": lt["is_corner"]}
                # 源甲之序列（其 prev 之推進同 `-87`／`-88`）
                if lt["PcA"] is None or lt["BcA"] is None:
                    prevA = None
                elif prevA is None:
                    prevA = i
                else:
                    pv = C["lots"][prevA]
                    r["prevA"] = prevA
                    r["oldA"] = w40.eval_lot(pv["PcA"], pv["BcA"], lt["PcA"], lt["BcA"],
                                             C["o"], C["d"], C["n"])[3]
                    r["exA"] = w87.eval_exact(pv["PcA"], pv["BcA"], lt["PcA"], lt["BcA"],
                                              C["o"], C["d"], C["n"], C["bpt"], C["bdir"],
                                              adv, True, True, True)[3]
                    r["sinA"] = w86._sin(lt["ua"], pv["ua"])
                    prevA = i
                # 源乙（**權威源**）之序列
                if lt["PcB"] is None or lt["BcB"] is None:
                    prevB = None
                elif prevB is None:
                    prevB = i
                else:
                    pv = C["lots"][prevB]
                    r["prevB"] = prevB
                    r["oldB"] = w40.eval_lot(pv["PcB"], pv["BcB"], lt["PcB"], lt["BcB"],
                                             C["o"], C["d"], C["n"])[3]
                    r["exB"] = w87.eval_exact(pv["PcB"], pv["BcB"], lt["PcB"], lt["BcB"],
                                              C["o"], C["d"], C["n"], C["bpt"], C["bdir"],
                                              adv, True, True, True)[3]
                    r["sinB"] = w86._sin(lt["uj"], pv["uj"])
                    # `-88` 之判準（不交叉·**權威源**·⛔ 原樣）
                    st_, sa_, ds_ = s_star_of(pv["pj"], pv["uj"], lt["pj"], lt["uj"])
                    ci = w82.chord_interval(C["edges"], pv["pj"], pv["uj"])
                    if sa_ == 0.0:
                        r["cross"] = (ds_ == 0.0)
                        r["why"] = "重合" if ds_ == 0.0 else "平行且不重合"
                    else:
                        gz = w82.graze(ci, st_)
                        r["cross"] = bool(w82.pred_chord(ci, st_)) or bool(gz[0])
                        r["why"] = "在內" if w82.pred_chord(ci, st_) else ("擦邊" if gz[0] else "在外")
                    r["s_star"] = st_
                    prevB = i
                ROWS.append(r)

    def _key(r):
        return "%s%s%d" % (r["lbl"], r["side"], r["i"])

    def _set(pred):
        return set(_key(r) for r in ROWS if pred(r))

    BATCH = [
        ("`-40`／`-83`", "35 宗·`5758.9877 ㎡`",
         "`probe_WG940_startperp.py` 之 `eval_lot`（舊形）·全體",
         lambda r: r.get("oldA") == "不合格", lambda r: r.get("oldB") == "不合格"),
        ("`-85`（門檻 `1e-9`）", "8 宗",
         "舊形 ∩ `K-9-14` 受詞內（`|sin| > 1e-9`）",
         lambda r: r.get("oldA") == "不合格" and (r.get("sinA") or 0) > TOL_85,
         lambda r: r.get("oldB") == "不合格" and (r.get("sinB") or 0) > TOL_85),
        ("`-85`／`-86`（正典容差 `1e-6`）", "3 宗",
         "舊形 ∩ `K-9-14` 受詞內（`|sin| > _PAR_TOL`）",
         lambda r: r.get("oldA") == "不合格" and (r.get("sinA") or 0) > PAR_TOL,
         lambda r: r.get("oldB") == "不合格" and (r.get("sinB") or 0) > PAR_TOL),
        ("`-87`", "25 宗",
         "`w87.eval_exact(..., True, True, True)`（正典逐字·組⑦）·全體",
         lambda r: r.get("exA") == "不合格", lambda r: r.get("exB") == "不合格"),
        ("`-88`", "2 宗·`4.7950 ㎡`",
         "`K-9-15` 不交叉（`w82.pred_chord`）·**已為權威源**",
         lambda r: r.get("cross") is True, lambda r: r.get("cross") is True),
    ]
    P("")
    P("  %-28s %-22s %-10s %-10s %-8s %-8s %-8s"
      % ("批", "原載", "源甲(w40)", "源乙(權威)", "交集", "甲∖乙", "乙∖甲"))
    A1 = []
    for nm, orig, cmdtxt, fa, fb in BATCH:
        sa_, sb_ = _set(fa), _set(fb)
        A1.append((nm, orig, cmdtxt, sa_, sb_))
        P("  %-28s %-22s %-10d %-10d %-8d %-8d %-8d"
          % (nm, orig, len(sa_), len(sb_), len(sa_ & sb_), len(sa_ - sb_), len(sb_ - sa_)))
    POP(len(BATCH), len(BATCH), "A-1 逐批（全列）")
    P("")
    P("  🔒 **逐批之「產生批次 ＋ 產生指令 ＋ 所用之源」（節 110 ②）**：")
    for nm, orig, cmdtxt, sa_, sb_ in A1:
        P("     %-28s 產生指令 ＝ %s" % (nm, cmdtxt))
    P("")
    P("  🔴 **偏移之宗逐宗具名**：")
    for nm, orig, cmdtxt, sa_, sb_ in A1:
        P("     %-28s 甲∖乙 ＝ %s" % (nm, sorted(sa_ - sb_) or "[]"))
        P("     %-28s 乙∖甲 ＝ %s" % ("", sorted(sb_ - sa_) or "[]"))
    P("")
    # 面積
    ar = {}
    for r in ROWS:
        ar[_key(r)] = r["area"]
    for nm, orig, cmdtxt, sa_, sb_ in A1:
        P("     %-28s 面積：源甲 **%.4f ㎡**／源乙（權威）**%.4f ㎡**"
          % (nm, sum(ar[k] for k in sa_), sum(ar[k] for k in sb_)))
    P("")
    P("  🔴 **必答 2（自洽之判別力）**：`-88` 之 **2 宗**於本檔重跑 ⇒ 源甲 **%d** ／ 源乙 **%d**"
      % (len(A1[4][3]), len(A1[4][4])))
    P("     名單 ＝ %s" % sorted(A1[4][4]))
    # 與 `-88` log 之對拍（【倉】錨）
    p88 = os.path.join(OUTDIR, "probe_WG988_nocross_7505c80.log")
    if os.path.exists(p88):
        t88 = io.open(p88, encoding="utf-8", errors="replace").read()
        m88 = re.findall(r'🔴 (R\d+)\s+(\S+)\s+序\(新\) \d+←\d+（i=(\d+)', t88)
        old88 = set("%s%s%s" % (a, b, c) for a, b, c in m88)
        P("     🔒 **與 `-88` log 之對拍**（【倉】`verify/out/probe_WG988_nocross_7505c80.log`）："
          "舊 log 解析所得 ＝ **%d** ⇒ 名單 %s" % (len(old88), sorted(old88)))
        P("     🔒 **逐宗相同 ＝ %s**（期望 True·⇒ 自洽）"
          % (old88 == A1[4][4] if old88 else "🔴 **解析得 0 ⇒ ⛔ 不得視為相同·具名**"))
    else:
        P("     ⛔ **`-88` log 不在倉內 ⇒ 無從對拍·具名**")
    P("")
    P("  🔴 **必答 3：`5758.9877 ㎡` 之權威源版本**")
    P("     源甲（`w40`·原載之源）＝ **%d 宗／%.4f ㎡**；"
      "🔴 **源乙（權威）＝ %d 宗／%.4f ㎡**"
      % (len(A1[0][3]), sum(ar[k] for k in A1[0][3]),
         len(A1[0][4]), sum(ar[k] for k in A1[0][4])))
    P("     ⚠️ 🔒 **該數之判準（起算垂線端點）已由 `K-9-15` 廢止** ⇒ 二者**皆⛔ 非現行有效之土地結論**；"
      "現行有效者 ＝ `-88` 之 **%d 宗／%.4f ㎡**"
      % (len(A1[4][4]), sum(ar[k] for k in A1[4][4])))

    # ══ 【D／A-2】`far_side_dir_and_pt` 使用點全查 ══════════════════════
    P("")
    P("【D／A-2】🔴 **`far_side_dir_and_pt` 之使用點全查**（⛔ 只列不改）")
    P("-" * W)
    APP = io.open(os.path.join(REPO, "app.py"), encoding="utf-8", errors="replace").read()
    P("  🛑 **A-2-1：`app.py` 之命中 ＝ %d**（停機條款②·期望 0）⇒ %s"
      % (APP.count("far_side_dir_and_pt"),
         "✅ **該缺陷⛔ 從未進入生產碼**" if APP.count("far_side_dir_and_pt") == 0 else "🛑 停機上呈"))
    P("     🔒 **判別力（常設 8·會使它為否之輸入）**：同法掃**已知在 `app.py` 內**之 "
      "`parcel_min_width_n14` ⇒ 命中 **%d**（須 > 0）⇒ ✅ 該掃描式非恆 0"
      % APP.count("parcel_min_width_n14"))

    def walk(root, ext):
        out = []
        for dp, dns, fns in os.walk(os.path.join(REPO, root)):
            dns[:] = [d for d in dns if d != "__pycache__"]
            for fn in fns:
                if fn.endswith(ext):
                    out.append(os.path.relpath(os.path.join(dp, fn), REPO).replace(os.sep, "/"))
        return sorted(out)

    VPY = [f for f in walk("verify", ".py") if f != SELF]
    P("")
    P("  🔴 **A-2-2：`verify/**.py` 之逐檔逐處**（🩸 母體**已排除本檔** `%s`）" % SELF)
    P("  %-46s %-7s %-58s %-10s" % ("檔", "行", "逐字（節錄）", "**受正典限**?"))
    n_use = 0
    files_hit = set()
    for f in VPY:
        txt = io.open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read()
        for t, line in enumerate(txt.split("\n")):
            if "far_side_dir_and_pt" not in line:
                continue
            n_use += 1
            files_hit.add(f)
            st = line.strip()
            # 🔒 A-0（偏向多列）：凡**呼叫**（含 `(`）者一律列為「受詞判定」之候選·具名
            is_call = "far_side_dir_and_pt(" in st and not st.startswith("#")
            P("  %-46s :%-6d %-58s %-10s"
              % (f.split("/")[-1], t + 1, st[:58],
                 "🔴 **是（呼叫）**" if is_call else "否（註解/import/字串）"))
    POP(n_use, n_use, "A-2-2 `verify/**.py` 之逐處（全列）")
    P("     🔒 **命中檔 ＝ %d**（claude.ai 現查稱 **7**·⛔ CC 獨立重查）⇒ %s"
      % (len(files_hit), "✅ 相符" if len(files_hit) == 7 else "🔴 **不符·逐項具名**"))
    P("     🔒 逐檔：%s" % sorted(x.split("/")[-1] for x in files_hit))

    RPT = walk("docs/reports", ".md")
    P("")
    P("  **A-2-3：`docs/reports/` 之引用**（⛔ 只列筆數與檔名·⛔ 不修史）")
    n_rpt = 0
    for f in RPT:
        c = io.open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read().count(
            "far_side_dir_and_pt")
        if c:
            n_rpt += 1
            P("     %-56s x%d" % (f.split("/")[-1], c))
    POP(n_rpt, n_rpt, "A-2-3 `docs/reports/` 之引用檔（全列）")

    # ══ 【E／A-3】落地介面清單 ═════════════════════════════════════════
    P("")
    P("【E／A-3】🔴 **落地介面清單**（⛔ **只列不建**·三態：`【已有】`／`【缺】`／`【部分】`）")
    P("-" * W)
    PROD = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
            "verify/run_verification.py", "verify/wf_f0.py", "verify/wf_f2.py",
            "verify/wf_f3.py", "verify/wf_f4.py", "verify/app_harvest.py"]
    PRODTXT = {}
    for f in PROD:
        PRODTXT[f] = io.open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read()

    # 🔒 **token 級分類**（🩸 修 2：字樣出現在**註解**裡⛔ 不算介面存在）
    #    `COMMENT`／`DOCSTRING`（敘述層之字串）⇒ **文件**；其餘 ⇒ **可執行**。
    import tokenize as _tk
    import token as _tkn

    def _classify(fname, pat):
        """回 (可執行命中數, 註解命中數, docstring 命中數, 可執行之逐處樣本)。

        🩸 **修 5**：`tokenize` 把 `foo(` 拆為 `NAME` ＋ `OP` ⇒ 以**帶 `(`** 之字樣比對
        **恆不命中**（甲-1 曾因此被誤判 `【缺】`）⇒ 一律**去尾 `(`** 後比對。
        """
        pt = pat[:-1] if pat.endswith("(") else pat
        n_exec = n_cmt = n_doc = 0
        samples = []
        prev_significant = _tkn.NEWLINE
        try:
            with io.open(os.path.join(REPO, fname), "rb") as fh:
                for tok in _tk.tokenize(fh.readline):
                    if pt in tok.string:
                        if tok.type == _tkn.COMMENT:
                            n_cmt += 1
                        elif tok.type == _tkn.STRING and prev_significant in (
                                _tkn.NEWLINE, _tkn.NL, _tkn.INDENT, _tkn.DEDENT,
                                _tkn.ENCODING):
                            n_doc += 1
                        else:
                            n_exec += 1
                            if len(samples) < 3:
                                samples.append((tok.start[0], tok.line.strip()[:66]))
                    if tok.type not in (_tkn.COMMENT, _tkn.NL):
                        prev_significant = tok.type
        except Exception as _e:                                  # noqa: BLE001
            return (-1, -1, -1, [])
        return (n_exec, n_cmt, n_doc, samples)

    def prod_hits(pats):
        """回 [(檔, 字樣, 可執行數, 註解數, docstring 數)]（⛔ 只列有命中者）。"""
        out = []
        for f in PROD:
            for p in pats:
                if PRODTXT[f].count(p) == 0:
                    continue
                ne, nc, nd, sm = _classify(f, p)
                out.append((f, p, ne, nc, nd, sm))
        return out

    ITEMS = [
        ("甲-1", "`K-9-12`", "現行判定入口 `parcel_min_width_n14` 之呼叫點",
         ["parcel_min_width_n14("]),
        ("甲-2", "`K-9-12`", "**矩形容納之判定式**（`W × D` 能否完整容納）",
         ["矩形容納", "rect_fit", "can_contain_rect", "_fits_rect"]),
        ("甲-3", "`K-9-12`", "`W × D` 之**取值來源**（法定最小寬／深）",
         ["法定最小寬_m", "法定最小深_m", "get_min_lot_size"]),
        ("甲-4", "`K-9-12-c`", "**可旋轉可平移**之搜尋（自由位姿）",
         ["free_pose", "rotate", "旋轉"]),
        ("甲-5", "`K-9-5-14 三`", "**受測區域**（規定範圍扣除退縮帶）",
         ["扣除退縮", "退縮帶", "_range_minus_setback"]),
        ("甲-6", "`K-9-12-e`", "**第 0 宗之例外分支**（街角 ⇒ 街角最小規定範圍）",
         ["WIDTH_VERDICT_CORNER_K4", "corner_min_area"]),
        ("甲-7", "`K-9-13`", "不得建築者之後果：**合併**",
         ["合併", "_merge_group"]),
        ("甲-8", "`K-9-13`", "不得建築者之後果：**調配**",
         ["調配", "_tier"]),
        ("甲-9", "`K-9-13`", "不得建築者之後果：🔴 **遞補**（下一投影序號）",
         ["遞補"]),
        ("甲-10", "`K-9-13`", "不得建築者之後果：**入調配池**",
         ["調配池", "pool"]),
        ("乙-1", "`②-宗` 錨點", "現行**起算垂線之錨**於碼面之位置",
         ["起算垂線", "_startperp", "eval_lot"]),
        ("乙-2", "`②-宗` 錨點", "🔴 **`S_req` 之計算入口**",
         ["S_req", "s_req"]),
        ("乙-3", "`②-宗` 錨點", "🔴 **`S_req` 與 `K-9-9 二` 判定之接點**",
         ["K-9-9", "K-9-15"]),
    ]
    P("  🔒 **「碼面」＝ 生產碼 %d 檔（正面列舉·⛔ 探針不計入）**" % len(PROD))
    P("  🔒 **三態之判準（🩸 修 2）**：`【已有】` ⟺ **全部**受詞字樣皆有"
      "**可執行**（⛔ 非註解／⛔ 非 docstring）之命中；`【部分】` ⟺ 部分；`【缺】` ⟺ **零可執行命中**")
    P("  %-6s %-13s %-34s %-11s %-7s %-46s"
      % ("#", "款", "所需之物", "**三態**", "可執行", "證據（檔×可執行／註解／doc）"))
    cnt3 = {"【已有】": 0, "【缺】": 0, "【部分】": 0}
    A3 = []
    for tag, kk, what, pats in ITEMS:
        hs = prod_hits(pats)
        ex = [(f, p, ne, nc, nd, sm) for f, p, ne, nc, nd, sm in hs if ne > 0]
        pats_ex = set(p for _f, p, _ne, _nc, _nd, _sm in ex)
        if not ex:
            state = "【缺】"
        elif pats_ex == set(pats):
            state = "【已有】"
        else:
            state = "【部分】"
        cnt3[state] += 1
        n_ex = sum(ne for _f, _p, ne, _nc, _nd, _sm in ex)
        ev = "／".join("%s×%d(%s)" % (f.split("/")[-1], ne, p[:14])
                      for f, p, ne, _nc, _nd, _sm in ex[:3]) or "—（僅註解/doc：%d）" % sum(
            nc + nd for _f, _p, _ne, nc, nd, _sm in hs)
        A3.append((tag, kk, what, state, n_ex, hs))
        P("  %-6s %-13s %-34s %-11s %-7d %-46s"
          % (tag, kk, what[:34], state, n_ex, ev[:46]))
    POP(len(ITEMS), len(ITEMS), "A-3 落地介面清單（全列）")
    P("     🔒 **三態計數**：`【已有】` **%d**／`【部分】` **%d**／`【缺】` **%d**（合計 %d ＝ %d）⇒ %s"
      % (cnt3["【已有】"], cnt3["【部分】"], cnt3["【缺】"],
         cnt3["【已有】"] + cnt3["【部分】"] + cnt3["【缺】"], len(ITEMS),
         "✅ 三態之外⛔ 無第四類" if sum(cnt3.values()) == len(ITEMS) else "🔴 **有漏·具名**"))
    P("     ⚠️ 🔒 **A-0（偏向多列）之落實**：判為 `【部分】` 者係「**部分字樣有可執行命中**」，"
      "⛔ **不代表該介面可用**——其「缺之部分」＝ 無可執行命中之字樣。")
    P("     🔴 **「字在倉內、但只在<u>註解／docstring</u>」之逐項具名（🩸 修 2 之受詞）**：")
    n_only_doc = 0
    for tag, kk, what, state, n_ex, hs in A3:
        onlydoc = [(f, p, nc, nd) for f, p, ne, nc, nd, _sm in hs if ne == 0 and (nc + nd) > 0]
        if not onlydoc:
            continue
        n_only_doc += 1
        P("        %-6s %-34s ⇒ %s"
          % (tag, what[:34],
             "／".join("%s:%s 註解%d·doc%d" % (f.split("/")[-1], p[:12], nc, nd)
                       for f, p, nc, nd in onlydoc[:3])))
    P("        🔒 **僅見於註解／doc 之項 ＝ %d**（⛔ 該類**不得**判為 `【已有】`）" % n_only_doc)
    P("     🔒 **`【已有】`／`【部分】` 之<u>可執行命中逐處樣本</u>（🩸 修 6·至多 3 處／項）**"
      "——⛔ 只給計數者，讀者無從分辨「字是**資料欄名**」與「字是**介面**」：")
    n_smp = 0
    for tag, kk, what, state, n_ex, hs in A3:
        if state == "【缺】":
            continue
        for f, p, ne, _nc, _nd, sm in hs:
            if ne <= 0 or not sm:
                continue
            for ln, txt in sm:
                n_smp += 1
                P("        %-6s %-22s %-28s :%-6d %s"
                  % (tag, p[:22], f.split("/")[-1][:28], ln, txt))
    POP(n_smp, n_smp, "A-3 可執行命中之逐處樣本（全列·至多 3 處／(項,檔,字樣)）")

    # ══ 【F／A-4】落地之影響母體 ═══════════════════════════════════════
    P("")
    P("【F／A-4】🔴 **落地之影響母體**（12 格·⛔ **只數不算後果**）")
    P("-" * W)
    P("  %-5s %-6s %-8s %-10s %-14s %-14s %-10s"
      % ("街廓", "側", "宗數", "第 0 宗?", "`K-9-12` 射程", "錨點更正射程", "交集"))
    t12 = tanc = tint = tall = 0
    n_cell = 0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            if not idxs:
                continue
            n_cell += 1
            has0 = C["lots"][idxs[0]]["is_corner"]
            n_all = len(idxs)
            n_corner = sum(1 for t in idxs if C["lots"][t]["is_corner"])
            r12 = n_all - n_corner                      # K-9-12：全部宗 − 第 0 宗
            ranc = (n_all - 1) if has0 else 0           # 錨點更正：有第 0 宗之組·第 1 宗以後
            inter = min(r12, ranc) if has0 else 0
            t12 += r12
            tanc += ranc
            tint += inter
            tall += n_all
            P("  %-5s %-6s %-8d %-10s %-14d %-14d %-10d"
              % (lbl, side, n_all, "✅ 有" if has0 else "⛔ 無", r12, ranc, inter))
    POP(n_cell, n_cell, "A-4 逐 (街廓, 側)（全列）")
    P("     🔒 **合計**：全部宗 **%d**／`K-9-12` 射程 **%d**／錨點更正射程 **%d**／交集 **%d**"
      % (tall, t12, tanc, tint))
    P("     🔒 **`P5` 之判**：`K-9-12` 射程（**%d**） %s 錨點更正射程（**%d**）⇒ %s"
      % (t12, ">" if t12 > tanc else ("＝" if t12 == tanc else "<"), tanc,
         "✅ 成立" if t12 > tanc else "🔴 **不成立·具名**"))

    # A-4-4 現況基線
    P("")
    P("  🔴 **A-4-4：現況基線**——現行 `evaluate_parcel_width_n14`（**生產判定器·原樣**）之判定")
    lw = float(snapshot["global"]["法定最小寬_m"])
    md = float(snapshot["global"]["法定最小深_m"])
    P("     🔒 入參：`legal_min_width` ＝ **%.2f m**／`min_depth` ＝ **%.2f m**"
      "（皆自 `snapshot['global']`·⛔ 不硬編）；`baseline_pts` ＝ `None`（＝ **現行生產路徑**）" % (lw, md))
    ev = ns["evaluate_parcel_width_n14"]
    VER = {}
    n_rows = 0
    for lbl, rows_ in sorted(GROWS.items()):
        for r in rows_:
            n_rows += 1
            try:
                out = ev(dict(r), FL.get(lbl) or {}, md, lw, _label="%s·%s" % (lbl, r.get("暫編地號")))
            except Exception as e:                                  # noqa: BLE001
                VER.setdefault("⛔ raise", []).append("%s·%s：%s" % (lbl, r.get("暫編地號"),
                                                                  str(e)[:60]))
                continue
            VER.setdefault(str(out.get("寬度判定")), []).append("%s·%s" % (lbl, r.get("暫編地號")))
    P("     `g_rows` 總列數 ＝ **%d**（來自 %d 街廓）" % (n_rows, len(GROWS)))
    for k in sorted(VER):
        P("       %-16s ＝ **%d**" % (k, len(VER[k])))
    POP(n_rows, n_rows, "A-4-4 現況基線（全列·依判定分組）")
    bad_n = len(VER.get(ns["WIDTH_VERDICT_BAD"], []))
    P("     🔴🔴 **母體之限制（🩸 修 4·⛔ 就地具名）**：`g_rows` 僅得 **%d ／ %d 街廓**"
      "（**%d 街廓 raise**·見【驅動】段之逐項）⇒ 本節之 **%d 列 ⛔ 非全部 %d 宗**"
      "；⛔ **不得以部分母體充作全體**"
      % (len(GROWS), len(blks), len(GERR), n_rows, tall))
    P("     🔴 **判為<u>不合格</u>（`%s`）之宗數 ＝ %d**" % (ns["WIDTH_VERDICT_BAD"], bad_n))
    if bad_n:
        for _x in VER[ns["WIDTH_VERDICT_BAD"]]:
            P("       %s" % _x)
        POP(bad_n, bad_n, "A-4-4 判為不合格之宗（全列·🩸 修 3：首版 `[:12]` 靜默截斷）")
    P("     🔒 **`P6` 之判**：判定器**非恆真** ⇒ 自檢 ③ 已證（已知寬 ⇒ 合格·已知窄 ⇒ 不合格）；"
      "**於本案之實資料**判為不合格者 ＝ **%d** ⇒ %s"
      % (bad_n, "✅ **本案母體內亦有反例**" if bad_n > 0
         else "⚠️ **本案母體內⛔ 無反例 ⇒ 該判定器於本案<u>無判別力</u>·具名**"))
    P("     ⚠️ 🔒 **⛔ 只出艙現況·⛔ 不算「改後會怎樣」**（施工單 A-4-4 明令）")

    # ══ 【G／P7】run_all ＝ 15（第十五法）═══════════════════════════════
    P("")
    P("【G／P7】`run_all` 清單筆數之**第十五法**（🔒 `ast.unparse` 之**往返法**·⛔ 與十四法不同族）")
    P("-" * W)
    n15, l15, glen = run_all_count_method15()
    P("  母體 ＝ `run_all.py` 之 AST；受詞 ＝ **`ast.unparse(For.iter)` 所<u>重新生成</u>之文本**"
      "（長度 %d 字元）" % glen)
    P("  🔒 **⛔ 未 `compile`／⛔ 未 `exec`**（僅 `ast.parse`／`ast.unparse`）⇒ ⛔ 未執行 `run_all`（閘 7）")
    for x in l15:
        P("     %s" % x)
    POP(len(l15), len(l15), "第十五法之逐項（全列）")
    P("  ⇒ **第十五法所得 ＝ %d**（施工單 `P7` 期望 **15**）⇒ %s"
      % (n15, "✅ 相符" if n15 == 15 else "🔴 **不符·具名**"))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
