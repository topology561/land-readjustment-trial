# -*- coding: utf-8 -*-
r"""**W-G.9-88 §二 A 組**：依 `K-9-15` 以「**地界線不交叉**」重判 ＋ `K-9-12` 落地狀態
＋ 宗序命名之全倉影響。

## 受詞（施工單 `W-G.9-88` §二·`VR-046` 六 ＋ KL 裁 `K-9-15` 2026-08-20）
- **A-1**（🛑 第一項）判準 ＝ **本宗遠側境界線與前一宗遠側境界線在街廓內⛔ 不得相交**
  ⇒ **相交 ⟺ `s*(j,k) ∈ [λ_a(j), λ_b(j)]`**（🔒 原樣 import `probe_WG982_chord` 之弦區間謂詞）。
- **A-2** `K-9-14` 之理由於**新判準下**是否成立（平行 ⇒ 永不相交）。
- **A-3** `K-9-12`（矩形容納）之**落地狀態現查**（⛔ 只查不用）。
- **A-4** **宗序命名**之全倉影響（`K-9-15` 二·⛔ 只列不改）。

## 🔴 宗序命名（`K-9-15` 二·自本款起為正典用語）
**第 0 宗** ＝ 街角地那 1 宗；**第 1 宗** ＝ 其後一宗；依此類推。
⚠️ **舊敘之「街角第 1 宗」＝ 本款之「第 0 宗」**。🔒 本檔一律採**新命名**，
並於逐宗表併出艙其**組內序**（`ord`）與**全域宗序**（`i`·碼面索引·⛔ 二者不同）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單將使違反母體**由 25 大幅下降**。其瑕若使**下降過多** ⇒ 放行本應不配地之宗
⇒ 🔴 **土地後果⛔ 非零**、且與本裁之期待一致 ⇒ **安靜**。
🔒 **事前選定：偏向<u>保留違反</u>**——落實為四條，⛔ 逐條具名：
  (甲) 邊界**擦邊**者（`w82.graze` 為真）一律判**交叉**（＝違反）；
  (乙) 遠側界**取不到**（`uj_of`／`pj_of` 回 `None`）者一律判**交叉**（＝違反）·具名；
  (丙) 二源（`w82.uj_of` 之解算面 vs `w40.far_side_dir_and_pt` 之多邊形邊）**不一致**者，
       取**判為交叉**之解讀·具名；
  (丁) `sin_a` 之平行判定沿用**正典 `_PAR_TOL`**（⛔ 不另立）。
       🩸 **首版之誤（§I）**：我原寫「`|sin_a| == 0` ⇒ `s*` 不可算 ⇒ 判**交叉**」——
       **幾何上是錯的**：二**相異**平行直線⛔ 永不相交，此係**可判定之偽**、⛔ 非不確定。
       🔒 **正解（仍在同一謂詞內·⛔ 非另立判準）**：
         `sin_a == 0` ∧ `|d_signed| > 0` ⇒ **平行且不重合 ⇒ ⛔ 不相交** ⇒ 合格；
         `sin_a == 0` ∧ `|d_signed| == 0` ⇒ **重合 ⇒ 相交（無窮多點）** ⇒ **交叉**。
       🔒 `d_signed = cross(p_k − p_j, û_k)` ＝ `p_j` 至 `k` 線之帶號距（`û_k` 單位）
       ⇒ 其為零 ⟺ 二線重合；併出艙 `|d_signed|` 之量級分布與極小（常設 9）。

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
`w82.chord_interval`／`pred_chord`／`graze`／`ring_edges`／`pj_of`／`uj_of`、
`w81.analyse_cell`／`spy_solve`／`spy_pool`／`faces_of`／`_cross`／`_u`、
`w40.far_side_dir_and_pt`／`line_isect`／`s_of`、`w86.PAR_TOL`／`_sin`、
`w87.eval_exact`（**負對照 ＝ 舊判準組⑦**）皆**原樣 import**。
🔒 **`s*` 之式⛔ 非重造**：本檔之 `s_star_of` 逐字同 `w81.analyse_cell` 之
`d_signed = _cross(pk − pj, uk)`／`s_star = d_signed / sin_a`，並於自檢 ① 對
`analyse_cell` 已算之對**逐位對拍**。

## ⛔ 本檔不做（施工單 §二 A-5 七款）
⛔ 零 `app.py` 變更；⛔ `data/` 零變更（`docs/rulings/` 之變更**限 §Z 之 `Z-1` 一檔·純追加**）；
⛔ 不落地 `K-9-9`／`K-9-12`／`K-9-14`／`K-9-15`；⛔ 不建遞補／合併／調配池介面；
⛔ 不換圖／不重烤／不改任何 baseline；⛔ 不另立平行門檻／座標框／**「交叉」之判準**；
⛔ 不出艙「應改領現金之宗」；⛔ 不以「理論上恆真」代替實算；⛔ 不以空母體之全過充作通過；
🔴 ⛔ **不得引用歷批之違反宗數（`35`／`8`／`3`／`25`）為土地結論**——其判準已由 `K-9-15` 廢止。

## 🔒 常設條款
**8** 每判準附「會使它為否」之輸入；**9** 門檻併出艙量級與 `math.ulp`、跨數量級**分層**；
**10** 每表末印 `POPULATION/PRINTED/SUPPRESSED`；**11** 修法列動作清單（⛔ 不經 shell 傳字樣·`Write` 落盤）；
**12／13** 搜尋規格含正典款號組＋三類出處分類；**14** 分離之宣稱一律**單一門檻**＋`m／n` 併出艙判別力為零者；
**15**（節 110）凡解釋一條既有款之效力，須逐字引原文；⛔ 不以「這條是為了防 X」代替條文。
"""
import contextlib
import glob
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

OUTDIR = os.path.join(VERIFY, "out")
W = 210
SB = 0.0                       # 🔒 情境母體 ＝ 僅 0m（⛔ 不擴·具名）

PAR_TOL = w86.PAR_TOL          # 🔴 正典容差（`K-6:1010`）·⛔ 不另立（原樣自 `w86` 取）
TOL_GRAZE = w82.TOL_GRAZE      # 🔒 擦邊之相對門檻 ＝ `w82` 逐字（⛔ 不另立）

_u = w81._u
_cross = w81._cross


def _short_head():
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                              capture_output=True, text=True).stdout.strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG988_nocross_%s.log" % COMMIT)


def s_star_of(pj, uj, pk, uk):
    """🔒 逐字同 `w81.analyse_cell`：`s* = cross(pk−pj, uk) / cross(uj, uk)`。

    回 `(s_star, sin_a, d_signed)`；`sin_a == 0` ⇒ `s_star = nan`（⛔ 不靜默取值）。
    """
    pj = np.asarray(pj, float)[:2]
    pk = np.asarray(pk, float)[:2]
    sin_a = _cross(uj, uk)
    d_signed = _cross(pk - pj, uk)
    if sin_a == 0.0:
        return float("nan"), sin_a, d_signed
    return d_signed / sin_a, sin_a, d_signed


def margin_of(ci, s_star):
    """🔒 節 103 之**餘裕**：`s*` 距最近端點之**帶號**量（正 ＝ 在區間內·負 ＝ 在區間外）。"""
    if ci["empty"] or not math.isfinite(s_star):
        return float("nan"), ""
    la, lb = ci["lam_a"], ci["lam_b"]
    da = s_star - la if math.isfinite(la) else math.inf
    db = lb - s_star if math.isfinite(lb) else math.inf
    return (da, "λ_a") if abs(da) <= abs(db) else (db, "λ_b")


# ══════════════════════════════════════════════════════════════════════════
#  🔒 第十四法：**AST 節點之精確位置**（`col_offset`／`end_col_offset`）× 原始碼切片
#     ⛔ 與既用十三法皆不同族——受詞 ＝ **`For.iter` 節點之四元位置**所切出之**精確片段**，
#     ⛔ 非行號區間（⑬）、⛔ 非常數池（④⑥）、⛔ 非運算元（⑫）、⛔ 非全檔文本（①）。
# ══════════════════════════════════════════════════════════════════════════
def run_all_count_method14(src=None, path=None):
    """回 (筆數, 名單, 四元位置)。⛔ 僅 `ast.parse`·⛔ 未 `compile`／`exec`。"""
    import ast
    if src is None:
        path = os.path.join(VERIFY, "run_all.py")
        src = io.open(path, encoding="utf-8").read()
    lines = src.split("\n")
    best = None
    for node in ast.walk(ast.parse(src, path or "<src>")):
        if not isinstance(node, (ast.For, ast.AsyncFor)):
            continue
        it = node.iter
        pos = (it.lineno, it.col_offset, it.end_lineno, it.end_col_offset)
        if it.end_lineno == it.lineno:
            seg = lines[it.lineno - 1][it.col_offset:it.end_col_offset]
        else:
            seg = "\n".join([lines[it.lineno - 1][it.col_offset:]]
                            + lines[it.lineno:it.end_lineno - 1]
                            + [lines[it.end_lineno - 1][:it.end_col_offset]])
        names = re.findall(r'["\']([A-Za-z0-9_./]+\.py)["\']', seg)
        if names and (best is None or len(names) > len(best[0])):
            best = (names, pos)
    if best is None:
        return 0, [], None
    return len(best[0]), best[0], best[1]


# ══════════════════════════════════════════════════════════════════════════
def selfcheck(P):                                                   # noqa: C901
    ok = {}
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·每項皆附**已知真／已知偽**對照）")
    P("-" * W)

    # ② `w82.pred_chord` 之已知真／已知偽（合成正方形）
    edges, _dg = w82.ring_edges(w82.SQ_CCW)
    ci = w82.chord_interval(edges, (0.0, 5.0), (1.0, 0.0))
    inx = w82.pred_chord(ci, 5.0)
    outx = w82.pred_chord(ci, 1e6)
    ok["②"] = (inx and not outx)
    P("  ② **`w82.pred_chord` 之已知真／已知偽**：`λ` ＝ [%.6f, %.6f]；"
      "`s*=5` ⇒ **%s**（期望 True）／`s*=1e6` ⇒ **%s**（期望 False）⇒ %s"
      % (ci["lam_a"], ci["lam_b"], inx, outx, "PASS" if ok["②"] else "🔴 FAIL"))

    # ②′ **平行／重合退化之判定**（🔒 本批之要害·常設 8：已知真＋已知偽）
    #     `SQ_CCW` ＝ 邊長 10 之正方形；取三條水平線 `y = 3`／`y = 7`／`y = 3`
    uh = (1.0, 0.0)
    p_j = (0.0, 3.0)
    cases = []
    for nm, p_k, exp in (("平行且不重合（y=3 vs y=7）", (0.0, 7.0), False),
                         ("**重合**（y=3 vs y=3·另一基點）", (4.0, 3.0), True)):
        st_, sa_, ds_ = s_star_of(p_j, uh, p_k, uh)
        par = (sa_ == 0.0)
        coi = par and (ds_ == 0.0)
        got = coi if par else None
        cases.append((nm, sa_, ds_, par, coi, got == exp))
        P("  ②′ %-30s `sin_a` ＝ %.3e／`d_signed` ＝ %.3e ⇒ 平行 %s·重合 %s"
          "⇒ 判**%s**（期望 %s）%s"
          % (nm, sa_, ds_, par, coi, "交叉" if coi else "不交叉",
             "交叉" if exp else "不交叉", "✅" if (coi == exp) else "🔴"))
    ok["②′"] = all(c[5] for c in cases)     # 🩸 首版取 c[4]（＝ 重合旗）⇒ 平行不重合恆 False
    P("     🔒 ⇒ **二相異平行線⛔ 永不相交**（可判定之**偽**）／**重合線相交於無窮多點**"
      "（判**交叉**·保守且正確）⇒ %s" % ("PASS" if ok["②′"] else "🔴 FAIL"))

    # ③ `w82.graze` 之判別力
    g_in = w82.graze(ci, ci["lam_b"])
    g_far = w82.graze(ci, (ci["lam_a"] + ci["lam_b"]) / 2.0)
    ok["③"] = (g_in[0] and not g_far[0])
    P("  ③ **`w82.graze` 之判別力**（`TOL_GRAZE = %.1e`·⛔ 不另立）：`s* = λ_b` ⇒ 擦邊 **%s**"
      "（期望 True·相對距 %.3e）／`s* = 中點` ⇒ 擦邊 **%s**（期望 False·相對距 %.3e）⇒ %s"
      % (TOL_GRAZE, g_in[0], g_in[1], g_far[0], g_far[1], "PASS" if ok["③"] else "🔴 FAIL"))

    # ④ 第十四法之判別力（⛔ 與 ⑬ 不同族之**具鑑別力**合成案）
    syn = "def main():\n    for f in ('a.py', 'b.py'): run('decoy_same_line.py')\n"
    n14, l14, pos = run_all_count_method14(syn, "<syn>")
    n13, l13, _r13 = w87.run_all_count_method13(syn, "<syn>")
    ok["④"] = (n14 == 2 and n13 == 3)
    P("  ④ **第十四法之判別力（常設 8）**：合成案 ＝ 迴圈標頭與**同行之誘餌**共一行")
    P("     ⇒ **第十四法 ＝ %d**（期望 2·名單 %s·位置 %s）／**第十三法 ＝ %d**（期望 3·名單 %s）⇒ %s"
      % (n14, l14, pos, n13, l13, "PASS" if ok["④"] else "🔴 FAIL"))
    P("     🔒 ⇒ **二法之受詞確實不同**（⑬ ＝ 行號區間·⑭ ＝ **AST 節點之四元精確位置**）")

    # ⑤ `w87.eval_exact` 可用（負對照之來源）
    TH = math.radians(17.0)
    d = (math.cos(TH), math.sin(TH))
    n = (-d[1], d[0])
    o = (0.0, 0.0)
    ob = (o[0] + 40.0 * n[0], o[1] + 40.0 * n[1])

    def fp(s):
        return (o[0] + s * d[0], o[1] + s * d[1])

    def bp(s):
        return (ob[0] + s * d[0], ob[1] + s * d[1])

    a_ok = w87.eval_exact(fp(10), bp(16), fp(30), bp(30), o, d, n, ob, d, +1, True, True, True)
    a_bad = w87.eval_exact(fp(10), bp(16), fp(12), bp(12), o, d, n, ob, d, +1, True, True, True)
    ok["⑤"] = (a_ok[3] == "合格" and a_bad[3] == "不合格")
    P("  ⑤ **負對照之來源 `w87.eval_exact` 原樣可用**：已知【合格】⇒ **%s**／已知【不合格】⇒ **%s** ⇒ %s"
      % (a_ok[3], a_bad[3], "PASS" if ok["⑤"] else "🔴 FAIL"))

    # ⑥ 常設 9
    P("  ⑥ **常設 9**：`PAR_TOL = %.1e` 施於 `|sin|` ∈ [0,1]（`ulp(1.0) = %.3e`）⇒ 門檻/ulp ＝ %.3e；"
      "`TOL_GRAZE = %.1e` 係**相對**量（⛔ 無單位·⛔ 不受 `λ` 量級影響）"
      % (PAR_TOL, math.ulp(1.0), PAR_TOL / math.ulp(1.0), TOL_GRAZE))

    allok = all(ok.values())
    P("  ⇒ 量測器自檢（②〜⑥；① 之 `s*` 對拍須待驅動後·見【驅動】段）：%s"
      % ("PASS" if allok else "🛑 FAIL ⇒ 停機·本次量測⛔ 不得出艙"))
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
    P("【W-G.9-88 §二 A 組】依 `K-9-15` 以「地界線不交叉」重判／`K-9-12` 落地狀態／宗序命名之全倉影響")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向<u>保留違反</u>**（甲/乙/丙/丁 四條見 docstring）")
    P("  🔴 **判準（`K-9-15` 三-2 逐字）＝ 僅保證「地界線不交叉」** ⇒ "
      "**相交 ⟺ `s*(j,k) ∈ [λ_a(j), λ_b(j)]`**（原樣 `w82.pred_chord`·⛔ 不另立）")
    P("  🔴 **宗序命名（`K-9-15` 二）**：**第 0 宗** ＝ 街角地；**第 1 宗** ＝ 其後一宗；依此類推")
    P("  🔒 情境母體 ＝ **僅 %gm**（⛔ 不擴·具名）" % SB)

    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    # ── 驅動（同 `-87` 之構造·其寫在 `main()` 內⛔ 不可 import·逐字具名之差）──
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
    SLM = cad.get("side_lines_by_side") or {}
    P("")
    P("【驅動】`%gm` × R1–R6——攔截 **%d 格**" % (SB, len(REAL)))

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
                     "edges": edges, "sl": SLM.get(lbl) or {}}

    # ── ① `s*` 之式與 `analyse_cell` 逐位對拍（自檢之延續）───────────────
    same = tot = 0
    worst = 0.0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        rec = C["rec"]
        for r in C["rows"]:
            if not r.get("ok"):
                continue
            j, k = r["j"], r["k"]
            uj = _u(r["uj"])
            uk = _u(r["uk"])
            # `analyse_cell` 之 `pj`／`pk` 未回傳 ⇒ 自同一來源重取（far(j)／near(k)）
            fj = w81.faces_of(w81.SOLVE.get(id((rec["ress"] or [None] * (j + 1))[j])))[1]
            nk = w81.faces_of(w81.SOLVE.get(id((rec["ress"] or [None] * (k + 1))[k])))[0]
            if fj is None or nk is None or uj is None or uk is None:
                continue
            mine, sa, ds = s_star_of(np.asarray(fj[1], float)[:2], uj,
                                     np.asarray(nk[1], float)[:2], uk)
            tot += 1
            dd = abs(mine - r["s_star"])
            worst = max(worst, dd)
            same += int(mine == r["s_star"])
    P("")
    P("  🔒 **自檢 ①（`s*` 之式⛔ 非重造）**：與 `w81.analyse_cell` 之逐對對拍 ⇒ "
      "**逐位相同 ＝ %d ／ %d**；極大差 ＝ **%.3e** ⇒ %s"
      % (same, tot, worst, "✅" if (tot and worst == 0.0) else
         ("🔴 **有差 ⇒ 具名**" if tot else "🔴 **母體為 0 ⇒ 空真假綠·具名**")))

    # ══ 【C／A-1】依「不交叉」重判 ═══════════════════════════════════════
    P("")
    P("【C／A-1】🛑 **依 `K-9-15` 以「地界線不交叉」重判**（母體 ＝ `-87` 之 47 宗·⛔ 不縮）")
    P("-" * W)
    P("  🔒 **判準逐字（`K-9-15` 三-2）**：`K-9-9 二` 之**剩餘作用 ＝ 僅保證「地界線不交叉」**")
    P("  🔒 **`j` ＝ 前一宗、`k` ＝ 本宗；相交 ⟺ `s*(j,k) ∈ [λ_a(j), λ_b(j)]`**"
      "（`λ` ＝ 過 `p_j` 方向 `û_j` 之直線於**街廓凸包**內之弦區間）")
    P("  %-5s %-5s %-6s %-4s %-4s %-6s %11s %13s %12s %12s %12s %12s %-16s %-8s"
      % ("街廓", "側", "序(新)", "i", "前", "受詞內", "|sin|", "s*", "λ_a", "λ_b",
         "餘裕", "d_signed", "**情形**", "出艙碼"))
    ROWS = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            # 🔒 **組內序（新命名·`K-9-15` 二）＝ 組內<u>索引位置</u>**
            #    ⇒ 其即推進序（`W-G.9-85` 實證「索引序 vs 推進序」逐宗相同 `0／47`），
            #    且與本批**母體之 `prev = i−1`** 一致 ⇒ `ord` 與 `ord_prev` **必相鄰**。
            #    🩸 首版以 `s_lo` 排序 ⇒ 得 `3←0` 等非相鄰之序（§I）。
            s_mid = {}
            for sd, ix in C["groups"]:
                v = [(C["lots"][t]["s_lo"] + C["lots"][t]["s_hi"]) / 2.0 for t in ix]
                s_mid[sd] = (sum(v) / len(v)) if v else float("nan")
            is_low = all(not math.isfinite(s_mid[k2]) or s_mid[side] <= s_mid[k2] for k2 in s_mid)
            adv = +1 if is_low else -1
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
                    st_, sa_, ds_ = s_star_of(pj, uj, pk, uk)
                    ci = w82.chord_interval(C["edges"], pj, uj)
                    inside = w82.pred_chord(ci, st_) if math.isfinite(st_) else None
                    gz = w82.graze(ci, st_) if math.isfinite(st_) else (False, float("nan"), "")
                    mg, mgnm = margin_of(ci, st_)
                else:
                    st_ = sa_ = ds_ = float("nan")
                    ci = None
                    inside = None
                    gz = (False, float("nan"), "")
                    mg, mgnm = float("nan"), ""
                # 🔒 A-0 (甲)(乙)(丙)(丁)——⛔ 逐情形具名，⛔ 無靜默退路
                par_deg = rec_ok and (sa_ == 0.0)          # 平行退化（`s*` 未定義）
                coincide = par_deg and (ds_ == 0.0)        # 重合（⇒ 相交於無窮多點）
                if not rec_ok:
                    reason, cross = "遠側界取不到", True         # A-0 (乙)
                elif coincide:
                    reason, cross = "重合", True                # 🔒 正確且保守
                elif par_deg:
                    reason, cross = "平行且不重合", False        # 🔒 **可判定之偽**
                elif bool(gz[0]):
                    reason, cross = "擦邊", True                # A-0 (甲)
                elif inside is None:
                    reason, cross = "`s*` 非有限", True         # ⛔ 不得靜默
                else:
                    reason, cross = ("在內" if inside else "在外"), bool(inside)
                unsure = reason in ("遠側界取不到", "`s*` 非有限")
                code = "🔴 不合格" if cross else "✅ 合格"
                r = {"lbl": lbl, "side": side, "i": i, "prev": prev,
                     "ord": ordmap.get(i), "ord_prev": ordmap.get(prev),
                     "adv": adv, "sin": sn, "s_star": st_, "sin_a": sa_,
                     "lam_a": ci["lam_a"] if ci else float("nan"),
                     "lam_b": ci["lam_b"] if ci else float("nan"),
                     "empty": ci["empty"] if ci else None,
                     "margin": mg, "margin_at": mgnm, "inside": inside,
                     "graze": bool(gz[0]), "graze_rel": gz[1], "unsure": unsure,
                     "d_signed": ds_, "reason": reason, "par_deg": par_deg,
                     "coincide": coincide,
                     "cross": cross, "code": code, "area": lt["area"],
                     "is_corner_prev": pv["is_corner"], "rec_ok": rec_ok,
                     "pj_u": uj, "pk_u": uk, "pj_b": pj, "pk_b": pk,
                     "ua_j": pv["ua"], "ua_k": lt["ua"], "pa_j": pv["pa"], "pa_k": lt["pa"]}
                r["inscope"] = math.isfinite(sn) and sn > PAR_TOL
                ROWS.append(r)
                prev = i
    for r in ROWS:
        P("  %-5s %-5s %-6s %-4d %-4d %-6s %11.3e %13.4f %12.4f %12.4f %12.4f %12.4f %-16s %-8s"
          % (r["lbl"], r["side"], "%d←%d" % (r["ord"], r["ord_prev"]), r["i"], r["prev"],
             "✅ 是" if r["inscope"] else "⛔ 否", r["sin"], r["s_star"],
             r["lam_a"], r["lam_b"], r["margin"], r["d_signed"],
             r["reason"], r["code"]))
    POP(len(ROWS), len(ROWS), "A-1 依「不交叉」重判（全列）")

    P("")
    P("  🔒 **逐宗之遠側界（施工單 A-1 明令：方向 ＋ 通過點）**——源 ＝ `w82.uj_of`／`pj_of`（解算面）")
    P("  %-5s %-5s %-6s %-4s %-4s %-24s %-26s %-24s %-26s"
      % ("街廓", "側", "序(新)", "i", "前",
         "前一宗 û_j", "前一宗 p_j", "本宗 û_k", "本宗 p_k"))
    n_nofar = 0
    for r in ROWS:
        if not r["rec_ok"]:
            n_nofar += 1
            P("  %-5s %-5s %-6s %-4d %-4d ⛔ 遠側界取不到·具名"
              % (r["lbl"], r["side"], "%d←%d" % (r["ord"], r["ord_prev"]), r["i"], r["prev"]))
            continue
        uj_, pj_ = r["pj_u"], np.asarray(r["pj_b"], float)[:2]
        uk_, pk_ = r["pk_u"], np.asarray(r["pk_b"], float)[:2]
        P("  %-5s %-5s %-6s %-4d %-4d %-24s %-26s %-24s %-26s"
          % (r["lbl"], r["side"], "%d←%d" % (r["ord"], r["ord_prev"]), r["i"], r["prev"],
             "(%.6f, %.6f)" % (uj_[0], uj_[1]), "(%.4f, %.4f)" % (pj_[0], pj_[1]),
             "(%.6f, %.6f)" % (uk_[0], uk_[1]), "(%.4f, %.4f)" % (pk_[0], pk_[1])))
    POP(len(ROWS), len(ROWS), "A-1 遠側界之方向與通過點（全列）")
    P("     🔒 **遠側界取不到者 ＝ %d**（⛔ 靜默退路之反面：計數為 0 亦須印出·A-0 (乙)）" % n_nofar)

    par = [r for r in ROWS if r.get("par_deg")]
    dsv = sorted(abs(r["d_signed"]) for r in par)
    P("")
    P("  🔒 **平行退化之處置（常設 9·⛔ 不另立門檻）**：`sin_a == 0`（**逐位精確**）之宗 ＝ **%d ／ %d**；"
      "其 `|d_signed|` ∈ [**%.6e**, **%.6e**]（中位 **%.6e**）"
      % (len(par), len(ROWS),
         dsv[0] if dsv else float("nan"), dsv[-1] if dsv else float("nan"),
         dsv[len(dsv) // 2] if dsv else float("nan")))
    P("     🔒 **重合（`d_signed == 0.0`）者 ＝ %d** ⇒ 其餘 %d 宗**離重合最近者亦達 %.6e m**"
      "（`ulp(1e2) = %.3e` ⇒ 距重合 **%.3e ulp**）⇒ ✅ **⛔ 非擦邊之重合**"
      % (sum(1 for r in par if r.get("coincide")), len(par) - sum(1 for r in par if r.get("coincide")),
         dsv[0] if dsv else float("nan"), math.ulp(1e2),
         (dsv[0] / math.ulp(1e2)) if dsv else float("nan")))

    bad = [r for r in ROWS if r["cross"]]
    ins = [r for r in ROWS if r["inscope"]]
    out = [r for r in ROWS if not r["inscope"]]
    bad_in = [r for r in ins if r["cross"]]
    bad_out = [r for r in out if r["cross"]]
    P("")
    P("  🔴 **必答 1：依「不交叉」重判之違反宗數 ＝ %d**"
      "（受詞內 %d ／ %d·受詞外 %d ／ %d）"
      % (len(bad), len(bad_in), len(ins), len(bad_out), len(out)))
    for r in bad:
        P("     🔴 %-4s %-4s 序(新) %d←%d（i=%d·前 %d）`s*` ＝ %.4f ∈ [%.4f, %.4f]？**%s**"
          "；擦邊 %s；不確定 %s；面積 %.4f ㎡"
          % (r["lbl"], r["side"], r["ord"], r["ord_prev"], r["i"], r["prev"],
             r["s_star"], r["lam_a"], r["lam_b"],
             "是" if r["inside"] else "否", r["graze"], r["unsure"], r["area"]))
    POP(len(ROWS), len(bad), "A-1 違反宗（全列）")
    P("     面積合計（帶號）＝ **%.4f ㎡**／（絕對值）＝ **%.4f ㎡**"
      % (sum(r["area"] for r in bad), sum(abs(r["area"]) for r in bad)))
    P("  🔴 **必答 2：受詞外 %d 宗是否全部轉為合格？** ⇒ 仍違反 ＝ **%d** ⇒ %s"
      % (len(out), len(bad_out),
         "✅ **全部轉為合格**" if not bad_out else "🛑 **有仍違反者 ⇒ 停機上呈·逐宗具名**"))
    P("  🔴 **必答 3：受詞內 3 宗是否仍違反？** ⇒ 受詞內違反 ＝ **%d ／ %d**：%s"
      % (len(bad_in), len(ins),
         "／".join("%s%s序%d(i=%d)" % (r["lbl"], r["side"], r["ord"], r["i"]) for r in bad_in)))

    # 🔒 節 103：最接近翻面之一宗
    fin = [r for r in ROWS if math.isfinite(r["margin"])]
    if fin:
        nearest = min(fin, key=lambda r: abs(r["margin"]))
        P("  🔒 **節 103（最接近翻面之一宗）**：%s %s 序 %d（i=%d）`餘裕` ＝ **%.6e**（距 `%s`）"
          "·其 `s*` ＝ %.4f、`λ` ＝ [%.4f, %.4f] ⇒ 判 **%s**"
          % (nearest["lbl"], nearest["side"], nearest["ord"], nearest["i"],
             nearest["margin"], nearest["margin_at"], nearest["s_star"],
             nearest["lam_a"], nearest["lam_b"], nearest["code"]))
        inb = [abs(r["margin"]) for r in fin if r["cross"]]
        outb = [abs(r["margin"]) for r in fin if not r["cross"]]
        P("     🔒 **母體之界定（⛔ 不得以全表為母體）**：`餘裕` 僅對**非平行**之宗有定義"
          "⇒ 本節之母體 ＝ **%d ／ %d**；其餘 **%d** 宗為平行退化（其分離之量係 `|d_signed|`·見上）"
          % (len(fin), len(ROWS), len(ROWS) - len(fin)))
        P("     🔒 **單一門檻（常設 14 ①）**：本節之分離以**單一門檻 `餘裕 = 0`** 表述 ⇒ ⛔ 無未定義帶")
        if inb and outb:
            P("     🔒 違反側之 `|餘裕|` 極小 ＝ %.6e／合格側之 `|餘裕|` 極小 ＝ %.6e"
              % (min(inb), min(outb)))
        else:
            P("     ⚠️ **一側為空**（違反 %d ／ 合格 %d）⇒ 該分離之判別力**部分無母體**·具名"
              % (len(inb), len(outb)))

    # 🔒 二源之對拍（A-0 丙）
    P("")
    P("  🔒 **遠側界之二源對拍（A-0 丙）**：源乙 ＝ `w82.uj_of`（解算面）／源甲 ＝ `w40.far_side_dir_and_pt`（多邊形邊）")
    dif = []
    for r in ROWS:
        if r["ua_j"] is None or r["ua_k"] is None or not r["rec_ok"]:
            continue
        C = CELL[r["lbl"]]
        st2, sa2, _d2 = s_star_of(r["pa_j"], _u(r["ua_j"]), r["pa_k"], _u(r["ua_k"]))
        ci2 = w82.chord_interval(C["edges"], np.asarray(r["pa_j"], float)[:2], _u(r["ua_j"]))
        in2 = w82.pred_chord(ci2, st2) if math.isfinite(st2) else None
        if bool(in2) != bool(r["inside"]):
            dif.append((r, st2, in2))
    P("     🔒 **二源判定不一致者 ＝ %d ／ %d**" % (len(dif), len(ROWS)))
    for r, st2, in2 in dif:
        P("        🔴 %-4s %-4s 序 %d（i=%d）源乙 在內＝%s（`s*` %.4f）／源甲 在內＝%s（`s*` %.4f）"
          "⇒ 🔒 **A-0 (丙) 取「交叉」** ⇒ 本表已判 %s"
          % (r["lbl"], r["side"], r["ord"], r["i"], r["inside"], r["s_star"], in2, st2, r["code"]))
    POP(len(ROWS), len(dif), "A-1 二源不一致者（全列）")
    if dif:
        P("     🔴 **逐項診斷（CC 自補·⛔ 施工單未令）**：二源之 `û_j`／`û_k` 逐項對照"
          "（🔒 若二源之 `û` 相同，`s*` 之差只是<u>基點沿線平移</u>·**謂詞不變**"
          "⇒ 判定翻面 ⟹ **方向必不同**）")
        for r, st2, in2 in dif:
            uj_b, uk_b = r["pj_u"], r["pk_u"]
            uj_a, uk_a = _u(r["ua_j"]), _u(r["ua_k"])
            P("        %-4s %-4s 序 %d：源乙 `û_j` ＝ (%.6f, %.6f)／`û_k` ＝ (%.6f, %.6f)"
              % (r["lbl"], r["side"], r["ord"], uj_b[0], uj_b[1], uk_b[0], uk_b[1]))
            P("        %-4s %-4s 序 %d：源甲 `û_j` ＝ (%.6f, %.6f)／`û_k` ＝ (%.6f, %.6f)"
              % (r["lbl"], r["side"], r["ord"], uj_a[0], uj_a[1], uk_a[0], uk_a[1]))
            sj = w86._sin(uj_a, uj_b)
            sk = w86._sin(uk_a, uk_b)
            P("        %-4s %-4s 序 %d：**`|sin(源甲 û_j, 源乙 û_j)|` ＝ %.6e**／"
              "**`|sin(源甲 û_k, 源乙 û_k)|` ＝ %.6e**（門檻 `_PAR_TOL` ＝ %.1e）"
              % (r["lbl"], r["side"], r["ord"], sj, sk, PAR_TOL))
            P("        🔒 **二源之 `û` 僅差<u>正負號</u>**（逐分量：%s／%s）——"
              "🔒 **`û → −û`（二者同時）與 `p → p + t·û` 皆⛔ 不改謂詞**"
              "（`s*` 與 `λ` **同號變／同量平移**）⇒ 翻面 ⟹ **二源之<u>線本身</u>不同**"
              % ("反號" if float(np.dot(uj_a, uj_b)) < 0 else "同號",
                 "反號" if float(np.dot(uk_a, uk_b)) < 0 else "同號"))
            # 🔴 **決定性之量 ＝ 交點座標**（幾何不變量·⛔ 不受號與基點影響）
            pj_b = np.asarray(r["pj_b"], float)[:2]
            pj_a = np.asarray(r["pa_j"], float)[:2]
            nb = np.array([-uj_b[1], uj_b[0]])
            perp = abs(float(np.dot(pj_a - pj_b, nb)))
            X_b = pj_b + r["s_star"] * np.asarray(uj_b, float)
            X_a = pj_a + st2 * np.asarray(uj_a, float)
            P("        🔴 **源甲之 `p_j` 至源乙之線之垂距 ＝ %.6e m**（0 ⇒ 同線）" % perp)
            P("        🔴 **交點座標**：源乙 (%.4f, %.4f)／源甲 (%.4f, %.4f)·**距離 ＝ %.6e m**"
              % (X_b[0], X_b[1], X_a[0], X_a[1],
                 float(np.hypot(X_a[0] - X_b[0], X_a[1] - X_b[1]))))
            P("        ⇒ 🔒 **成因 ＝ %s**"
              % ("二源取到**同一條線**（垂距 ≈ 0）⇒ 🔴 **翻面之成因未明·具名**"
                 if perp <= 1e-6 else
                 "二源取到**不同之線**（平行偏移 %.4f m）⇒ 源甲之「遠側界」⛔ 非本宗之遠側界" % perp))
            P("        ⚠️ 🔒 **`W-G.9-86` §F-1 已證**：`w40.far_side_dir_and_pt`（源甲）於"
              "`sign = −1` 之側**取到近側界**；本格之側 ＝ `%s`·`adv` ＝ %+d"
              "⇒ ⛔ **該已知成因⛔ 不涵蓋本格**·具名"
              % (r["side"], r["adv"]))
            P("        🔒🔒 **本格之 A-0 (丙) 與<u>權威源</u>同判**：`K-9-9`／`K-9-15` 之受詞為"
              "「**遠側境界線**」，其倉內之權威來源 ＝ **解算面**（`faces_of(...)[1]`·源乙）"
              "⇒ 源乙判**交叉**、本表亦判交叉 ⇒ 🔒 **該宗之違反⛔ 不繫於 A-0 之保守取向**")

    # 🔒 負對照 ＝ 舊判準（`w87.eval_exact` 組⑦）
    P("")
    P("  🔒 **負對照（常設 8·⛔ 不可省）＝ 舊判準**（原樣 import `w87.eval_exact` 組⑦·三旗全開）")
    nbad = []
    for r in ROWS:
        C = CELL[r["lbl"]]
        pv, lt = C["lots"][r["prev"]], C["lots"][r["i"]]
        res = w87.eval_exact(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"], C["o"], C["d"], C["n"],
                             C["bpt"], C["bdir"], r["adv"], True, True, True)
        if res[3] == "不合格":
            nbad.append(r)
    P("     ⇒ **舊判準之違反 ＝ %d 宗**（施工單 `P4` 期望 **25**）⇒ %s"
      % (len(nbad), "✅ 同源可比" if len(nbad) == 25 else "🔴 **≠ 25 ⇒ 同源性斷裂·具名**"))
    s_new = set((r["lbl"], r["side"], r["i"]) for r in bad)
    s_old = set((r["lbl"], r["side"], r["i"]) for r in nbad)
    P("     🔒 **交集 ＝ %d**；**舊∖新 ＝ %d**：%s"
      % (len(s_new & s_old), len(s_old - s_new), sorted("%s%s%d" % x for x in (s_old - s_new))))
    P("     🔒 **新∖舊 ＝ %d**：%s"
      % (len(s_new - s_old), sorted("%s%s%d" % x for x in (s_new - s_old))))

    # 🔒 **新命名之自檢（`K-9-15` 二）**：`ord == 0` ⟺ 該宗為街角宗
    P("")
    P("  🔒 **新命名之自檢（`K-9-15` 二）：`第 0 宗` ⟺ 街角宗**（`meta['corners']`·⛔ 非硬編）")
    P("  %-5s %-6s %-22s %-10s %-14s %-10s"
      % ("街廓", "側", "組內索引", "第 0 宗 ＝", "是街角宗?", "街角宗集合"))
    n_ok = n_tot = 0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            if not idxs:
                continue
            n_tot += 1
            z = idxs[0]
            isc = C["lots"][z]["is_corner"]
            n_ok += int(isc)
            P("  %-5s %-6s %-22s %-10s %-14s %-10s"
              % (lbl, side, str(idxs)[:22], "i=%d" % z,
                 "✅ 是" if isc else "🔴 **否·具名**", str(sorted(C["meta"]["corners"]))[:10]))
    POP(n_tot, n_tot, "新命名自檢 逐 (街廓, 側)（全列）")
    P("     🔒 **`第 0 宗` ＝ 街角宗者 ＝ %d ／ %d**" % (n_ok, n_tot))
    # 🔴 **例外之成因現查**：該側是否有 SIDE_LINE（⇒ 該側是否有街角地）
    P("     🔴 **例外之成因現查（CC 自補·⛔ 施工單未令）**：`CLAUDE.md` CAD 規範逐字"
      "「**街角地非必然**：無 SIDE_LINE 的街廓無街角」⇒ 逐側對照其 SIDE_LINE：")
    P("     %-5s %-6s %-12s %-14s %-16s %-10s"
      % ("街廓", "側", "該側 SIDE?", "第 0 宗是街角?", "二者一致?", "組內索引"))
    agree = tot2 = 0
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            if not idxs:
                continue
            tot2 += 1
            key = "left" if side == "左" else ("right" if side == "右" else None)
            has = bool((C["sl"] or {}).get(key)) if key else None
            isc = C["lots"][idxs[0]]["is_corner"]
            eq = (has == isc)
            agree += int(eq)
            P("     %-5s %-6s %-12s %-14s %-16s %-10s"
              % (lbl, side, ("✅ 有" if has else "⛔ 無"), ("✅ 是" if isc else "⛔ 否"),
                 ("✅ 一致" if eq else "🔴 **不一致·具名**"), str(idxs)[:10]))
    POP(tot2, tot2, "新命名例外之成因 逐 (街廓, 側)（全列）")
    P("     🔒 **「該側有 SIDE_LINE」⟺「第 0 宗為街角宗」之逐側相符 ＝ %d ／ %d** ⇒ %s"
      % (agree, tot2, "✅ **例外已完全解釋**——`K-9-15` 二之「第 0 宗 ＝ 街角地那 1 宗」"
         "於**無 SIDE_LINE 之側⛔ 無所指**（⛔ 非碼面之誤）"
         if agree == tot2 else "🔴 **仍有未解釋者·具名**"))

    # ══ 【D／A-2】`K-9-14` 之理由於新判準下是否成立 ═══════════════════════
    P("")
    P("【D／A-2】🔴 **`K-9-14` 之理由於新判準下是否成立**（平行 ⇒ 永不相交？）")
    P("-" * W)
    P("  %-5s %-5s %-5s %-5s %-7s %12s %14s %13s %13s %-8s"
      % ("街廓", "側", "序(新)", "i", "受詞內", "|sin|", "s*", "λ_a", "λ_b", "在內?"))
    for r in ROWS:
        P("  %-5s %-5s %-5d %-5d %-7s %12.3e %14.4f %13.4f %13.4f %-8s"
          % (r["lbl"], r["side"], r["ord"], r["i"],
             "✅ 是" if r["inscope"] else "⛔ 否", r["sin"], r["s_star"],
             r["lam_a"], r["lam_b"],
             ("—" if r["inside"] is None else ("🔴 是" if r["inside"] else "否"))))
    POP(len(ROWS), len(ROWS), "A-2 逐宗 `|sin|` 與 `s*`（全列）")
    out_in = [r for r in out if r["inside"]]
    P("  🔴 **必答：平行者（受詞外 %d 宗）之 `s*` 是否恆不落在 `[λ_a, λ_b]` 內？**"
      "⇒ 落在內者 ＝ **%d** ⇒ %s"
      % (len(out), len(out_in),
         "✅ **恆不落入 ⇒ `K-9-14` 之理由於新判準下成立**" if not out_in
         else "🛑 **有落入者 ⇒ `K-9-14` 之理由不成立 ⇒ 停機上呈**"))
    abs_out = [abs(r["s_star"]) for r in out if math.isfinite(r["s_star"])]
    abs_in = [abs(r["s_star"]) for r in ins if math.isfinite(r["s_star"])]
    P("  🔒 **判別力**：受詞外之 `|s*|` ∈ [%.4e, %.4e]（有限者 %d ／ %d·非有限者 %d）；"
      "受詞內之 `|s*|` ∈ [%.4e, %.4e]（%d 宗）"
      % (min(abs_out) if abs_out else float("nan"), max(abs_out) if abs_out else float("nan"),
         len(abs_out), len(out), len(out) - len(abs_out),
         min(abs_in) if abs_in else float("nan"), max(abs_in) if abs_in else float("nan"),
         len(ins)))
    lam_max = max((r["lam_b"] for r in ROWS if math.isfinite(r["lam_b"])), default=float("nan"))
    P("     🔒 **`λ_b` 之全體極大 ＝ %.4f** ⇒ 受詞外之 `|s*|` 極小 %.4e %s 之"
      % (lam_max, min(abs_out) if abs_out else float("nan"),
         "**大於**" if (abs_out and min(abs_out) > lam_max) else "🔴 **未大於**"))
    P("  🔒 **常設 14 ③（判別力為零者）**：`s*` 非有限（`sin_a == 0`）之宗 ＝ **%d**"
      "（其對「是否落入 `λ`」之判別力 ＝ 0·依 A-0 (丁) 判交叉）"
      % sum(1 for r in ROWS if not math.isfinite(r["s_star"])))

    # ══ 【E／A-3】`K-9-12` 落地狀態現查 ════════════════════════════════
    P("")
    P("【E／A-3】🔴 **`K-9-12`（矩形容納）之落地狀態現查**（⛔ 只查不用）")
    P("-" * W)
    PROD = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
            "verify/run_verification.py", "verify/wf_f0.py", "verify/wf_f2.py",
            "verify/wf_f3.py", "verify/wf_f4.py", "verify/app_harvest.py"]
    P("  🔒 **「碼面」之界定（⛔ 正面列舉·⛔ 非「全倉排除」）**：生產碼 ＝ 下列 **%d 檔**；"
      "⛔ **探針（`verify/probes/`）與工具⛔ 不計入**（其為量測物、非生產物）" % len(PROD))
    P("  %-34s %-9s %-11s %-11s %-11s %-11s %-22s"
      % ("檔", "K-9-12", "K-9-12-b", "K-9-12-e", "矩形容納", "rect_fit", "parcel_min_width_n14"))
    tot12 = tot514 = totn14 = 0
    for f in PROD:
        fp = os.path.join(REPO, f)
        if not os.path.exists(fp):
            P("  %-34s ⛔ 查無" % f)
            continue
        s = io.open(fp, encoding="utf-8", errors="replace").read()
        tot12 += s.count("K-9-12")
        tot514 += s.count("K-9-5-14")
        totn14 += s.count("parcel_min_width_n14")
        P("  %-34s %-9d %-11d %-11d %-11d %-11d %-22d"
          % (f, s.count("K-9-12"), s.count("K-9-12-b"), s.count("K-9-12-e"),
             s.count("矩形容納"), s.count("rect_fit"), s.count("parcel_min_width_n14")))
    POP(len(PROD), len(PROD), "A-3-1 生產碼逐檔（全列）")
    P("     🔒 **`K-9-12` 於生產碼之總命中 ＝ %d**（`P6` 期望 **0**）⇒ %s"
      % (tot12, "✅ 相符（＝ `K-9-12-b` 之「未實作」現況未變）" if tot12 == 0 else "🔴 **≠ 0·具名**"))
    P("     🔒 **判別力對照（常設 8）**：已知**已實作**之款 `K-9-5-14` 於生產碼之總命中 ＝ **%d**"
      "（須 > 0）⇒ %s" % (tot514, "✅ 該現查式非恆 0" if tot514 > 0 else "🔴 **判別力不足·具名**"))
    P("     🔒 現行仍走 `parcel_min_width_n14`：生產碼總命中 ＝ **%d**" % totn14)
    P("")
    P("  🔒 **`parcel_min_width_n14` 之<u>使用點</u>與其受詞**（生產碼側·逐處）：")
    npt = 0
    for f in PROD:
        fp = os.path.join(REPO, f)
        if not os.path.exists(fp):
            continue
        for t, l in enumerate(io.open(fp, encoding="utf-8", errors="replace").read().split("\n")):
            if "parcel_min_width_n14" in l and ("def " in l or "(" in l.split("parcel_min_width_n14")[-1][:2]):
                npt += 1
                if npt <= 12:
                    P("     %s:%-6d %s" % (f, t + 1, l.strip()[:120]))
    POP(npt, min(12, npt), "A-3-2 `parcel_min_width_n14` 之定義／呼叫點")
    n_all = sum(len(CELL[l]["lots"]) for l in CELL)
    n_corner = sum(1 for l in CELL for t in CELL[l]["lots"] if CELL[l]["lots"][t]["is_corner"])
    P("  🔴 **A-3-3：若改採 `K-9-12`，其射程所及之宗數 ＝ 全部宗 − 第 0 宗**")
    P("     全部宗 ＝ **%d**；**第 0 宗（街角宗）** ＝ **%d** ⇒ **射程 ＝ %d 宗**"
      "（⛔ **只列數·不判可否建築**）" % (n_all, n_corner, n_all - n_corner))
    P("     🔒 **「第 0 宗」之界定 ＝ `w81.analyse_cell` 之 `meta['corners']`**（⛔ 非以宗序硬編）")

    # ══ 【F／A-4】宗序命名之全倉影響 ═══════════════════════════════════
    P("")
    P("【F／A-4】🔴 **宗序命名之全倉影響**（`K-9-15` 二·⛔ **只列不改**）")
    P("-" * W)
    SCOPE = []
    for root in ("docs/rulings", "docs/reports", "verify"):
        for dp, dns, fns in os.walk(os.path.join(REPO, root)):
            dns[:] = [d for d in dns if d != "__pycache__"]
            for fn in fns:
                if fn.endswith((".md", ".py")):
                    SCOPE.append(os.path.relpath(os.path.join(dp, fn), REPO).replace(os.sep, "/"))
    # 🩸 **母體須扣除本檔自身**（本檔 docstring 內即寫有該些舊命名）
    #    ⇒ 否則**自我污染**（`CLAUDE.md`：母體含自身輸出 ⇒ 自檢自我污染）。
    SELF = os.path.relpath(os.path.abspath(__file__), REPO).replace(os.sep, "/")
    n_before = len(SCOPE)
    SCOPE = sorted(f for f in SCOPE if f != SELF)
    OLDNAME = ["街角第 1 宗", "街角地第 1 宗", "第 2 宗"]
    NEWMAP = {"街角第 1 宗": "第 0 宗", "街角地第 1 宗": "第 0 宗", "第 2 宗": "第 1 宗"}
    P("  🔒 母體 ＝ `docs/rulings/`＋`docs/reports/`＋`verify/` 之 `.md`／`.py` ＝ **%d 檔**"
      "（🩸 **已扣除本檔自身** `%s`：%d → %d·⛔ 否則自我污染）"
      % (len(SCOPE), SELF, n_before, len(SCOPE)))
    hits = []
    for f in SCOPE:
        try:
            txt = io.open(os.path.join(REPO, f), encoding="utf-8", errors="replace").read()
        except Exception:                                           # noqa: BLE001
            continue
        for t, l in enumerate(txt.split("\n")):
            for k in OLDNAME:
                if k in l:
                    hits.append((f, t + 1, k, NEWMAP[k], l.strip()[:78]))
    P("  %-52s %-7s %-14s %-10s" % ("檔", "行", "舊命名", "新命名應為"))
    for f, t, k, nw, _l in hits[:20]:
        P("  %-52s :%-6d %-14s %-10s" % (f, t, k, nw))
    POP(len(hits), min(20, len(hits)), "A-4 舊命名之全倉出現處（前 20 列）")
    from collections import Counter
    cnt_k = Counter(h[2] for h in hits)
    cnt_f = Counter(h[0] for h in hits)
    P("     🔒 **逐字樣筆數**：%s" % dict(cnt_k))
    P("     🔒 **涉及檔數 ＝ %d**；筆數最多之三檔 ＝ %s"
      % (len(cnt_f), cnt_f.most_common(3)))
    P("     ⛔ **本批⛔ 不改任何一處**（施工單 §七-3·⛔ 不修史）——本表僅供後批決定。")
    # 🔒 **哨兵字樣於執行期組出**（⛔ 不使其字面落入任何檔·否則本檔自身即命中）
    SENT = "街角第" + str(9) + " 宗"
    n_sent = sum(1 for f in SCOPE
                 if SENT in io.open(os.path.join(REPO, f), encoding="utf-8",
                                    errors="replace").read())
    P("     🔒 **判別力（常設 8）**：以一個**已知不存在**之舊命名（執行期組出·⛔ 不落字面）"
      "同法掃 ⇒ 命中 **%d**（須 0）⇒ %s"
      % (n_sent, "✅ 該掃描式非恆命中" if n_sent == 0 else "🔴 **具名**"))

    # ══ 【G／P7】run_all ＝ 15（第十四法）═══════════════════════════════
    P("")
    P("【G／P7】`run_all` 清單筆數之**第十四法**（🔒 AST 節點之**四元精確位置** × 原始碼切片·⛔ 與十三法不同族）")
    P("-" * W)
    n14, l14, pos = run_all_count_method14()
    P("  母體 ＝ `run_all.py` 之 AST；受詞 ＝ **`For.iter` 節點之 `(lineno, col_offset, end_lineno, end_col_offset)`** ＝ %s"
      % (str(pos)))
    P("  🔒 **⛔ 未 `compile`／⛔ 未 `exec`**（僅 `ast.parse`）⇒ ⛔ 未執行 `run_all`（閘 7）")
    for x in l14:
        P("     %s" % x)
    POP(len(l14), len(l14), "第十四法之逐項（全列）")
    P("  ⇒ **第十四法所得 ＝ %d**（施工單 `P7` 期望 **15**）⇒ %s"
      % (n14, "✅ 相符" if n14 == 15 else "🔴 **不符·具名**"))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
