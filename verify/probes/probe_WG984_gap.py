# -*- coding: utf-8 -*-
r"""**W-G.9-84 §二 A 組**：`D-0` 之 2 宗 ＋ 使 `(j,k)` 不重疊之**充要**約束 ＋ 其與 `K-9-9 二` 下限之差。

## 受詞（施工單 `W-G.9-84` §二·`VR-042` 六）
- **A-1**（🔴 **第一項**）`D-0` 之 2 宗（`R3 右 8` `4.3220°`／`R1 右 3` `0.6908°`）——
  **以二源各跑一次** `K-9-9 二` 判定 ⇒ **是否翻轉**；若翻轉出艙「35 ⇒ 新值」及**逐宗差集**；並**溯源**。
- **A-2** 由 `W-G.9-82` 之弦區間閉式導出 **`S_req`**（使**全部** `(j,k)`｜`d≥2` 皆 `s* ∉ [λ_a, λ_b]`
  之 **`宗(j+1)` 遠側界最小位置**）＋ **shim 驗證**（正對照 `S_req` ／ 負對照 `K-9-9 二` 下限）。
- **A-3** `S_req` 與 `K-9-9 二` 下限之**差**（逐格·含**號之聲明**·節 107）。
- **A-4** 常設第 12 條 ③ 之落實（出題資格現查·`docs/rulings/` 全庫）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單欲量「正典下限」與「充要約束」之**差**。
其瑕若使**差偏小** ⇒ 看起來「正典已經夠了」⇒ **安靜**；偏大 ⇒ 與既有結論衝突 ⇒ **會吵**。
🔒 **事前選定：偏向使差<u>偏大</u>**——落實為三條，⛔ 逐條具名：
  (甲) `S_req` 取**弦之出口端**（⛔ 非入口端）——即沿推進方向**較遠**之端點；
  (乙) 重疊之判定沿用 `W-G.9-82` 之**閉區間**（邊界擦邊計為**重疊**）⇒ `S_req` 更遠；
  (丙) `d ≥ 2` 之門檻沿用（⛔ 不放寬）。

## 🔒 A-2-4 之 shim 與 §七-6 之區別（🔒 施工單所令之逐字聲明）
本檔之 shim **僅沿 `d̂` 平移<u>一條界線</u>之位置**（`p_k → p_k + δ·d̂`），
⛔ **不改面積目標**、⛔ **不解 `S`**（`solve_G_binary` 未被呼叫）
⇒ ⛔ **不涉面積守恆**，⛔ **非** §七-6 所禁之「shim `S`」。

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
- `K-9-9 二` 判定式：**原樣 import** `probe_WG940_startperp` 之 `eval_lot`／`far_side_dir_and_pt`／
  `line_isect`／`s_of`（⛔ 未重寫一行）。
- 弦區間謂詞：**原樣 import** `probe_WG982_chord` 之 `ring_edges`／`chord_interval`／`pred_chord`／
  `pj_of`／`uj_of`。
- 逐格逐對之構造：**原樣 import** `probe_WG981_scope` 之 `analyse_cell`／`spy_solve`／`spy_pool`。
- `probe_WG983_k99prep`：其判定邏輯**寫在 `main()` 內⛔ 不可 import**（🔒 逐字具名之差）；
  本檔**原樣 import 其模組級常數**（`TOL_PAR`／`D_MIN`／`SB`／`OLD_LOG`）並於【0】出艙其值，
  且其所用之判定式**與本檔同為 `w40.eval_lot`** ⇒ 同源可比。

## ⛔ 本檔不做（施工單 §二 A-5 五款）
⛔ 零 `app.py` 變更；⛔ 不落地 `K-9-9` 任何一款；⛔ 不建遞補／合併／調配池介面；
⛔ 不換圖、⛔ 不重烤、⛔ 不改任何 baseline／快照、⛔ `data/` 零變更；
⛔ **不提出任何「正典應如何修改」之主張**（本檔只量**差**）；
⛔ 不出艙「應改領現金之宗」。

## 🔒 常設條款
**8** 每個判準附「會使它為否」之輸入；**9** 門檻併出艙量級與 `math.ulp`、跨數量級者**分層**；
**10** 每表末印 `POPULATION/PRINTED/SUPPRESSED`，且**報告中每一 ≥4dp 之數須可回指 log 行**；
**11** 修法列動作清單（本檔「⛔ 不經 shell 傳字樣」**適用讀＋寫**·以 `Write` 落盤）；
**12** 搜尋規格含正典款號組（`docs/rulings/` 全庫）——見 §A／A-4。
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

OUTDIR = os.path.join(VERIFY, "out")
W = 205
SETBACKS = (0.0, 3.5)          # 🔒 A-3 令「至少破閘二格 ＋ 其餘 10 格」⇒ 12 格 ⇒ 二情境
SB_A1 = 0.0                    # 🔒 A-1 之母體 ＝ `W-G.9-40`／`-83` 之 `0m`（⛔ 不擴·具名）
D_MIN = w83.D_MIN              # ＝ 2（原樣 import）
TOL_PAR = w83.TOL_PAR          # ＝ 1e-9（原樣 import）
TOL_SAME = 1e-12               # A-1 判別力：「已知二源相同」之門檻（⛔ 較 TOL_PAR 更嚴）
TOL_MONO = 1e-9                # A-2-2 單調性之容差（`s*` 之量級於表中出艙）
EPS_SHIM = 1e-6                # A-2-4 shim 之**嚴格越界量**（m·`s` 之量級 ~1e2）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG984_gap_%s.log" % COMMIT)
_u = w82._u


def _sin_between(a, b):
    a, b = _u(a), _u(b)
    if a is None or b is None:
        return float("nan")
    return abs(float(a[0] * b[1] - a[1] * b[0]))


# ═══ P7 之第十法：`run_all` 清單筆數 ═════════════════════════════════════
def run_all_count_method10():
    r"""🔒 **第十法：文件側對帳法**（⛔ 與既用九法皆不同族）。

    既用九法之母體：`run_all.py` 之**語法／位元組**（①〜⑦）、**檔案系統**（⑧）、**git 增刪歷史**（⑨）。
    本法之母體 ＝ **`docs/reports/**.md` 中<u>人所寫下</u>之宣告**——
    受詞 ＝ 「`run_all` 夾具／清單筆數」之逐次宣告值。
    🔒 **其獨有之產出**：**碼與紀錄是否一致**（八九法皆只看碼、看不見紀錄）。
    ⚠️ **其失效模式（⛔ 須併出艙）**：本法量的是**紀錄**、⛔ 非碼——
    紀錄若集體寫錯，本法會**一致地錯**。⇒ 🔒 **只能作為第 10 支、⛔ 不得單獨採信。**

    🔒 **樣式之受詞（承 `W-G.9-83` §I-1 之更正）**：一律「**行中出現**」，⛔ 非「行首為之」。
    """
    rep_dir = os.path.join(REPO, "docs", "reports")
    rows = []
    num = re.compile(r'(\d{1,3})')
    for fn in sorted(os.listdir(rep_dir)):
        if not fn.endswith(".md"):
            continue
        try:
            txt = io.open(os.path.join(rep_dir, fn), encoding="utf-8", errors="replace").read()
        except Exception:                                           # noqa: BLE001
            continue
        for ln in txt.split(chr(10)):
            if "run_all" not in ln:
                continue
            if ("夾具" not in ln) and ("清單" not in ln):
                continue
            vals = [int(v) for v in num.findall(ln) if 10 <= int(v) <= 30]
            if vals:
                rows.append((fn, ln.strip()[:96], vals))
    return rows


# ═══ 幾何小工具（⛔ 純算術）════════════════════════════════════════════
def s_front_of_line(p, u, o, d):
    """一條直線（過 `p`·方向 `u`）與 FRONTLINE 之交點沿 `d̂` 之 `s` 座標。⛔ 平行回 None。"""
    X = w40.line_isect(tuple(p), tuple(u), tuple(o), tuple(d))
    return None if X is None else w40.s_of(X, o, d)


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
    P("  ① **`w40.eval_lot` 同源證**（原樣 import·`W-G.9-40` §0 之 17° 傾斜測資）：")
    P("     甲 ⇒ %s ／ 乙 ⇒ %s ／ 合格 ⇒ %s ／ **已知不合格 ⇒ %s**（Δfront %+.3f·常設 8 之「否」輸入）⇒ %s"
      % (c1[0], c2[0], c3[3], c4[3], c4[2][0], "PASS" if r1 else "🔴 FAIL"))

    e_sq, _d = w82.ring_edges(w82.SQ_CCW)
    uu = _u((3.0, 4.0))
    ci = w82.chord_interval(e_sq, np.array([1.0, 2.0]), uu)
    ha, hb = -1.0 / float(uu[0]), (10.0 - 2.0) / float(uu[1])
    r2 = (abs(ci["lam_a"] - ha) <= 8 * math.ulp(abs(ha))
          and abs(ci["lam_b"] - hb) <= 8 * math.ulp(abs(hb)))
    ok &= r2
    P("  ② **`w82.chord_interval` 同源證**：λ=[%.12g, %.12g]／手算 [%.12g, %.12g]"
      "　殘差/ulp = %.2f／%.2f ⇒ %s"
      % (ci["lam_a"], ci["lam_b"], ha, hb,
         w82._ulp_ratio(ci["lam_a"] - ha, ha), w82._ulp_ratio(ci["lam_b"] - hb, hb),
         "PASS" if r2 else "🔴 FAIL"))
    r2b = w82.pred_chord(ci, 0.0) and (not w82.pred_chord(ci, 1e6))
    ok &= r2b
    P("     🔒 常設 8：`s*=0` ⇒ %s（期望 True）／`s*=1e6` ⇒ %s（期望 False）⇒ %s"
      % (w82.pred_chord(ci, 0.0), w82.pred_chord(ci, 1e6), "PASS" if r2b else "🔴 FAIL"))

    # ③ 🔒 `w83` 之模組級常數（其判定邏輯在 main() 內⛔ 不可 import·逐字具名）
    P("  ③ **`w83` 常數之原樣 import**：`D_MIN=%s`／`TOL_PAR=%.1e`／`SB=%s`／`OLD_LOG=%r`"
      % (w83.D_MIN, w83.TOL_PAR, w83.SB, w83.OLD_LOG))
    r3 = (w83.D_MIN == 2 and abs(w83.TOL_PAR - 1e-9) < 1e-18)
    ok &= r3
    P("     ⇒ %s（🔒 其判定式與本檔同為 `w40.eval_lot` ⇒ 同源可比）"
      % ("PASS" if r3 else "🔴 FAIL"))

    # ④ 🔒 shim 之機制自檢：平移一條線 δ ⇒ 其 FRONTLINE-s 恰移 δ
    p0, u0 = np.array([3.0, 1.0]), _u((0.4, 0.9))
    s_before = s_front_of_line(p0, u0, o, d)
    delta = 7.25
    s_after = s_front_of_line(p0 + delta * np.asarray(d, float), u0, o, d)
    res = abs((s_after - s_before) - delta)
    r4 = res <= 64 * math.ulp(abs(delta))
    ok &= r4
    P("  ④ **shim 之機制自檢**：沿 `d̂` 平移 δ=%.2f ⇒ FRONTLINE-`s` 位移 %.12f"
      "（殘差 %.3e·**殘差/ulp = %.2f**）⇒ %s"
      % (delta, s_after - s_before, res, w82._ulp_ratio(res, delta),
         "PASS" if r4 else "🔴 FAIL"))
    # 常設 8 之「否」輸入：平移 0 ⇒ 位移須為 0（若機制有偏，此處會露）
    s_zero = s_front_of_line(p0 + 0.0 * np.asarray(d, float), u0, o, d)
    r4b = (abs(s_zero - s_before) == 0.0)
    ok &= r4b
    P("     🔒 常設 8：δ=0 ⇒ 位移 %.3e（期望**恰 0**）⇒ %s"
      % (s_zero - s_before, "PASS" if r4b else "🔴 FAIL"))

    # ⑤ 🔒 常設 9：門檻之量級與 ulp
    P("  ⑤ **常設 9**：`TOL_PAR=%.1e`／`TOL_SAME=%.1e`（皆施於 `|sin|` ∈ [0,1]·`ulp(1.0)=%.3e`）；"
      "`TOL_MONO=%.1e`（施於 `s*` 之差·其量級於【D】表出艙）"
      % (TOL_PAR, TOL_SAME, math.ulp(1.0), TOL_MONO))
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
    P("【W-G.9-84 §二 A 組】`D-0` 之 2 宗 ＋ 充要約束 `S_req` ＋ 其與 `K-9-9 二` 下限之差")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向使差<u>偏大</u>**（甲/乙/丙 三條見 docstring）")
    P("  🔒 A-2-4 之 shim **僅平移一條界線**（⛔ 不改面積目標·⛔ 不解 `S`）⇒ ⛔ 非 §七-6 所禁者")
    P("  🔒 情境母體：A-2／A-3 ＝ **%s**（12 格）；A-1 ＝ **僅 %gm**（沿 `-40`／`-83`·具名）"
      % (SETBACKS, SB_A1))

    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    # ── 驅動（二情境·w81 之 spy）──────────────────────────────────────
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
    ERR = {}
    for sb in SETBACKS:
        w81.CUR["setback"] = sb
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p, sb, snapshot=snapshot)
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = \
            w81.spy_solve(o_solve), w81.spy_pool(o_pool)
        try:
            for lbl in blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, sb)
                    except Exception as e:                          # noqa: BLE001
                        ERR[(sb, lbl)] = "%s: %s" % (type(e).__name__, str(e)[:80])
        finally:
            ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(w81.CAP)
    P("")
    P("【驅動】%s × R1–R6——攔截 **%d 格**；生產碼 raise 之 (情境,街廓) ＝ %d 組"
      % (SETBACKS, len(REAL), len(ERR)))

    FL = cad.get("front_lines") or {}
    BL = cad.get("baselines") or {}

    def cell_frame(rec):
        lbl = rec["label"]
        fl, bl = FL.get(lbl) or {}, BL.get(lbl) or {}
        if not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            return None
        o_ = tuple(float(x) for x in fl["p1"])
        d_ = tuple(np.asarray(rec["d_hat"], float)[:2])
        n_ = (-d_[1], d_[0])
        bpt = tuple(float(x) for x in bl["point"])
        bang = math.radians(float(bl.get("angle_deg", 0.0)))
        bdir = (math.cos(bang), math.sin(bang))
        return o_, d_, n_, bpt, bdir

    def groups_of(rec, d_):
        IV = []
        for g in rec["biz"]:
            ss_ = [(x * d_[0] + y * d_[1]) for x, y in list(g.exterior.coords)]
            IV.append((min(ss_), max(ss_)))
        kb = None
        for k in range(1, len(IV)):
            if min(v[0] for v in IV[k:]) > max(v[1] for v in IV[:k]) + 1e-6:
                kb = k if kb is None else -1
        return ([("左", list(range(0, kb))), ("右", list(range(kb, len(IV))))]
                if isinstance(kb, int) and kb > 0
                else [("單組(未測得唯一分界)", list(range(len(IV))))])

    # ══ 【C／A-1】`D-0` 之 2 宗——二源各跑一次 ═══════════════════════════
    P("")
    P("【C／A-1】🛑 `D-0` 之 2 宗——**以二源各跑一次 `K-9-9 二` 判定**（🔴 本單第一項）")
    P("-" * W)
    P("  🔒 **二源之逐字定義**：")
    P("     **源甲 `w40`** ＝ `far_side_dir_and_pt(biz[i], d̂)`——自**宗地多邊形之邊**取"
      "「與 `d̂` 夾角最大之二邊」中 `s` 中點較大者。")
    P("     **源乙 `w81`** ＝ `faces_of(SOLVE[id(res)])[1]`——`_solve_G_one` 所回之"
      "`_alloc_dir_used`（⇒ `rot90` 後之**引擎實際切線方向**）＋ `baseline_pt + S·d̂`。")

    def walk(rec, src):
        """以指定源走完該格之 `K-9-9 二` 判定。src ∈ {'甲','乙'}。回 (judged, bad)。"""
        fr = cell_frame(rec)
        if fr is None:
            return [], []
        o_, d_, n_, bpt, bdir = fr
        judged, bad = [], []
        for side, idxs in groups_of(rec, d_):
            prev = None
            for i in idxs:
                if src == "甲":
                    uf, pf = w40.far_side_dir_and_pt(rec["biz"][i], d_)
                else:
                    r_ = (rec["ress"] or [None] * (i + 1))[i]
                    ff = w81.faces_of(w81.SOLVE.get(id(r_)))[1]
                    uf, pf = (None, None) if ff is None else (_u(ff[0]), ff[1])
                if uf is None:
                    judged.append((side, i, None, None, "⛔ 取不出遠側界"))
                    continue
                Pc = w40.line_isect(tuple(pf), tuple(uf), o_, d_)
                Bc = w40.line_isect(tuple(pf), tuple(uf), bpt, bdir)
                if Pc is None or Bc is None:
                    judged.append((side, i, None, None, "⛔ ∥FRONT 或 ∥BASE"))
                    prev = None
                    continue
                if prev is None:
                    judged.append((side, i, None, None, "（起點·本則不適用）"))
                    prev = (Pc, Bc)
                    continue
                case, st, df, code = w40.eval_lot(prev[0], prev[1], Pc, Bc, o_, d_, n_)
                judged.append((side, i, case, df, code))
                if code == "不合格":
                    bad.append((rec["label"], side, i, case, df, float(rec["biz"][i].area)))
                prev = (Pc, Bc)
        return judged, bad

    A1 = [rec for rec in REAL if abs(rec["setback"] - SB_A1) < 1e-9]
    BAD = {"甲": [], "乙": []}
    JUD = {"甲": {}, "乙": {}}
    for rec in A1:
        for src in ("甲", "乙"):
            j_, b_ = walk(rec, src)
            JUD[src][rec["label"]] = {(s, i): (c, df, cd) for (s, i, c, df, cd) in j_}
            BAD[src].extend(b_)
    P("")
    P("  **二源各自之違反宗數**：源甲 `w40` ＝ **%d**（倉內錨【倉】`-83` §D-1／`-40` log ＝ **35**）"
      "／源乙 `w81` ＝ **%d**" % (len(BAD["甲"]), len(BAD["乙"])))
    setA = {(b[0], b[1], b[2]) for b in BAD["甲"]}
    setB = {(b[0], b[1], b[2]) for b in BAD["乙"]}
    P("  **逐宗差集**：甲∖乙 ＝ %s ／ 乙∖甲 ＝ %s"
      % (sorted(setA - setB), sorted(setB - setA)))
    areaA = {(b[0], b[1], b[2]): b[5] for b in BAD["甲"]}
    areaB = {(b[0], b[1], b[2]): b[5] for b in BAD["乙"]}
    P("  **面積合計**：源甲 %.4f ㎡ ／ 源乙 %.4f ㎡"
      % (sum(areaA.values()), sum(areaB.values())))
    POP(len(setA | setB), len(setA | setB), "A-1 二源違反宗之聯集")

    # 🔴 D-0 之 2 宗逐宗
    TWO = [("R3", "右", 8), ("R1", "右", 3)]
    P("")
    P("  🔴 **`D-0` 之 2 宗逐宗**（⛔ 逐項具名）")
    P("  %-5s %-5s %-4s %-22s %-22s %11s %-10s %-10s %-8s"
      % ("街廓", "側", "i", "源甲 遠側界方向", "源乙 遠側界方向", "|sin|", "源甲 判", "源乙 判", "翻轉?"))
    flip = 0
    for lbl, side, i in TWO:
        rec = next((r for r in A1 if r["label"] == lbl), None)
        if rec is None:
            P("  🔴 查無 %s 之格" % lbl)
            continue
        fr = cell_frame(rec)
        o_, d_, n_, bpt, bdir = fr
        ua, pa = w40.far_side_dir_and_pt(rec["biz"][i], d_)
        r_ = (rec["ress"] or [None] * (i + 1))[i]
        ff = w81.faces_of(w81.SOLVE.get(id(r_)))[1]
        ub, pb = (None, None) if ff is None else (_u(ff[0]), ff[1])
        sn = _sin_between(ua, ub) if (ua is not None and ub is not None) else float("nan")
        ca = JUD["甲"][lbl].get((side, i), (None, None, "—"))
        cb = JUD["乙"][lbl].get((side, i), (None, None, "—"))
        fl_ = (ca[2] != cb[2])
        flip += int(fl_)
        P("  %-5s %-5s %-4d (%8.5f,%8.5f) (%8.5f,%8.5f) %11.3e %-10s %-10s %-8s"
          % (lbl, side, i, ua[0], ua[1], ub[0], ub[1], sn, ca[2], cb[2],
             "🔴 **是**" if fl_ else "否"))
        P("      源甲 通過點 (%.4f, %.4f)／源乙 通過點 (%.4f, %.4f)；夾角 %.4f°"
          % (pa[0], pa[1], float(pb[0]), float(pb[1]), math.degrees(math.asin(min(1.0, sn)))))
        for tag, cc in (("甲", ca), ("乙", cb)):
            if cc[1] is not None:
                P("      源%s：情形 %s　Δfront %+.4f　Δbase %+.4f　⇒ %s"
                  % (tag, cc[0], cc[1][0], cc[1][1], cc[2]))
        # 🔴 溯源：該宗多邊形之逐邊
        P("      🔴 **溯源**——該宗多邊形之逐邊（角度 ＝ 與 `d̂` 之夾角·`s中` ＝ 邊中點之 `s`）：")
        ext = list(rec["biz"][i].exterior.coords)
        rows_e = []
        for t in range(len(ext) - 1):
            uu2 = _u((ext[t + 1][0] - ext[t][0], ext[t + 1][1] - ext[t][1]))
            if uu2 is None:
                continue
            c_ = abs(float(uu2[0] * d_[0] + uu2[1] * d_[1]))
            cr_ = abs(float(uu2[0] * d_[1] - uu2[1] * d_[0]))
            ang = math.degrees(math.atan2(cr_, c_))
            mid = ((ext[t][0] + ext[t + 1][0]) / 2, (ext[t][1] + ext[t + 1][1]) / 2)
            rows_e.append((t, ang, w40.s_of(mid, o_, d_),
                           math.hypot(ext[t + 1][0] - ext[t][0], ext[t + 1][1] - ext[t][1]),
                           _sin_between(uu2, ub) if ub is not None else float("nan")))
        rows_e.sort(key=lambda e: -e[1])
        P("      %-5s %10s %12s %10s %14s %-10s" % ("邊", "∠d̂(°)", "s中", "邊長", "|sin(邊,源乙)|", "備註"))
        for t, ang, sm, ln_, sb_ in rows_e:
            note = ""
            if len(rows_e) >= 2 and (t == rows_e[0][0] or t == rows_e[1][0]):
                note = "（`w40` 之候選二邊）"
            if math.isfinite(sb_) and sb_ <= TOL_PAR:
                note += "🔒 **∥源乙**"
            P("      %-5d %10.4f %12.4f %10.4f %14.3e %-10s" % (t, ang, sm, ln_, sb_, note))
        POP(len(rows_e), len(rows_e), "A-1 溯源·%s %s i=%d 之逐邊（全列）" % (lbl, side, i))
    P("  🔒 **`P5` 之判**：`D-0` 之 2 宗中**翻轉者 ＝ %d ／ 2** ⇒ %s"
      % (flip, "✅ **至少一宗翻轉**（`P5` 成立）" if flip >= 1 else
         "🔴 **二宗皆不翻轉 ⇒「35」不受影響·具名**"))

    # 🔒 A-1 之判別力（常設 8）：對一個**已知二源相同**之宗，二源判定須完全相同
    P("")
    P("  🔒 **A-1 之判別力（常設 8·⛔ 不可省）**：對**已知二源相同**（`|sin| ≤ %.0e`）之宗同法跑一次"
      % TOL_SAME)
    same_tot = same_eq = 0
    ex = None
    for rec in A1:
        fr = cell_frame(rec)
        if fr is None:
            continue
        o_, d_, n_, bpt, bdir = fr
        for side, idxs in groups_of(rec, d_):
            for i in idxs:
                ua, _pa = w40.far_side_dir_and_pt(rec["biz"][i], d_)
                r_ = (rec["ress"] or [None] * (i + 1))[i]
                ff = w81.faces_of(w81.SOLVE.get(id(r_)))[1]
                ub = None if ff is None else _u(ff[0])
                if ua is None or ub is None:
                    continue
                if _sin_between(ua, ub) > TOL_SAME:
                    continue
                a_ = JUD["甲"][rec["label"]].get((side, i))
                b_ = JUD["乙"][rec["label"]].get((side, i))
                if a_ is None or b_ is None:
                    continue
                same_tot += 1
                if a_[2] == b_[2]:
                    same_eq += 1
                elif ex is None:
                    ex = (rec["label"], side, i, a_[2], b_[2])
    P("     母體（`|sin| ≤ %.0e` 之宗）＝ **%d**；二源判定**完全相同 ＝ %d**"
      % (TOL_SAME, same_tot, same_eq))
    P("     ⇒ %s"
      % ("✅ **「翻轉」之偵測⛔ 非恆真**（該類宗一個都沒翻）" if same_tot and same_eq == same_tot
         else ("🔴 **有例外：%s**" % (ex,)) if same_tot else "⚠️ **母體為 0 ⇒ 該判別力⛔ 未成立·具名**"))

    # ══ 【D／A-2】充要約束之導出與 shim 驗證 ═══════════════════════════
    P("")
    P("【D／A-2】使**全部** `(j,k)`（`d ≥ %d`）不重疊之**充要約束 `S_req`**" % D_MIN)
    P("-" * W)
    P("  🔒 **導出（⛔ 純算術·由 `W-G.9-82` 之閉式）**：")
    P("     `宗j × 宗k 重疊 ⟺ s*(j,k) ∈ [λ_a, λ_b]`（`λ` ＝ **線 j** 之弦區間·per (格, j) 常數）")
    P("     `宗k` 之近側界 ＝ `宗(k−1)` 之遠側界（`-83` 已實測界面距離 0.000000 m·4/4）")
    P("     ⇒ 首條須清出弦者 ＝ **`宗(j+1)` 之遠側界**（其即 `宗(j+2)` 之近側界·`d=2`）")
    P("     ⇒ **`S_req` ＝ 過「弦之出口端」且 ∥ALLOC 之直線與 FRONTLINE 之交點沿 `d̂` 之 `s`**")
    P("     🔒 **換算式逐字**：`X_end = p_j + λ_end · û_j`；"
      "`S_req = s_of( line(X_end, û_k) ∩ FRONTLINE , o, d̂ )`")

    CELLS = {}
    for rec in REAL:
        fr = cell_frame(rec)
        if fr is None or rec["block"] is None:
            continue
        o_, d_, n_, bpt, bdir = fr
        meta, rows = w81.analyse_cell(rec, strip_axis)
        edges, _dg = w82.ring_edges(list(rec["block"].exterior.coords))
        key = (rec["setback"], rec["label"])
        CELLS[key] = {"rec": rec, "meta": meta, "rows": rows, "edges": edges,
                      "o": o_, "d": d_, "n": n_, "bpt": bpt, "bdir": bdir}

    P("")
    P("  %-6s %-5s %-4s %-7s %12s %12s %-6s %-6s %-24s %-12s"
      % ("情境", "街廓", "j", "是街角?", "λ_a", "λ_b", "←邊a", "←邊b", "s*(j,k) 之 k 與值", "單調?"))
    A2 = []
    mono_ok = mono_bad = 0
    for key in sorted(CELLS):
        C = CELLS[key]
        rec, meta, rows, edges = C["rec"], C["meta"], C["rows"], C["edges"]
        js = sorted({r["j"] for r in rows if r.get("ok") and r["d"] >= D_MIN})
        for j in js:
            pj, uj = w82.pj_of(rec, j), w82.uj_of(rec, j)
            if pj is None or uj is None:
                continue
            ci = w82.chord_interval(edges, pj, uj)
            ks = sorted([(r["k"], r["s_star"]) for r in rows
                         if r.get("ok") and r["j"] == j and r["d"] >= D_MIN])
            diffs = [ks[t + 1][1] - ks[t][1] for t in range(len(ks) - 1)]
            mono = (all(x > TOL_MONO for x in diffs) or all(x < -TOL_MONO for x in diffs)
                    if diffs else None)
            if mono is True:
                mono_ok += 1
            elif mono is False:
                mono_bad += 1
            A2.append({"key": key, "j": j, "ci": ci, "ks": ks, "mono": mono,
                       "is_corner": j in meta["corners"], "diffs": diffs})
            P("  %-6s %-5s %-4d %-7s %12.4f %12.4f %-6s %-6s %-24s %-12s"
              % ("%gm" % key[0], key[1], j, "**是**" if j in meta["corners"] else "否",
                 ci["lam_a"], ci["lam_b"], ci["ia"], ci["ib"],
                 ",".join("%d:%.2f" % (k, v) for k, v in ks[:4]) + ("…" if len(ks) > 4 else ""),
                 {True: "✅ 單調", False: "🔴 **非單調**", None: "—(僅 1 個 k)"}[mono]))
    POP(len(A2), len(A2), "A-2 逐 (格, j)（全列）")
    P("  🔒 **`P3` 之判**：單調 **%d** ／ **非單調 %d** ／ 僅 1 個 k **%d** ⇒ %s"
      % (mono_ok, mono_bad, sum(1 for a in A2 if a["mono"] is None),
         "✅ **`s*(j,k)` 對 `k` 單調（`P3` 成立）**" if mono_bad == 0 else
         "🔴 **有非單調者 ⇒ 充要約束須改為全稱式·具名**"))
    if A2:
        allsd = [abs(x) for a in A2 for x in a["diffs"]]
        if allsd:
            P("     🔒 **常設 9**：`|Δs*|` 之量級 ∈ [%.4f, %.4f]；門檻 `TOL_MONO=%.1e`；"
              "**節 103 最接近翻面者 ＝ %.6f**" % (min(allsd), max(allsd), TOL_MONO, min(allsd)))

    # ── `S_req` 之計算 ＋ shim 驗證 ────────────────────────────────────
    P("")
    P("  🔴 **`S_req` 之計算 ＋ shim 驗證**（🔒 正對照 `S_req` ／ 負對照 `K-9-9 二` 下限）")
    P("  🔒 **`S_req` ＝ 全稱式**（越過**全部** `k` 之禁區間·A-0(甲) 之保守值）；"
      "`S_end` ＝ 端點式（單 `k` 讀法·僅單調時充分）")
    P("  🔒 **shim 之四個位置**：`現況`(δ=0)／`門檻+ε`／`門檻−ε`／`K-9-9 下限`；"
      "`EPS_SHIM = %.1e m`（🔒 常設 9：`s` 之量級 ~1e2·`math.ulp(1e2)=%.3e` ⇒ 門檻 » ulp）"
      % (EPS_SHIM, math.ulp(1e2)))
    P("  %-6s %-5s %-4s %-7s %11s %11s %11s %11s %-6s %-6s %-6s %-6s"
      % ("情境", "街廓", "j", "推進號", "s(宗j+1far)", "**S_req**", "S_end", "K-9-9下限",
         "現況", "**+ε**", "−ε", "→下限"))
    SHIM = []
    SIGN_SRC = []
    for a in A2:
        key, j, ci, ks = a["key"], a["j"], a["ci"], a["ks"]
        C = CELLS[key]
        rec, meta, rows = C["rec"], C["meta"], C["rows"]
        o_, d_, n_, bpt, bdir = C["o"], C["d"], C["n"], C["bpt"], C["bdir"]
        pj, uj = w82.pj_of(rec, j), w82.uj_of(rec, j)
        # `宗(j+1)` 之遠側界 ＝ `宗(j+2)` 之近側界；取 k=j+2 之列以得其 (p_k, u_k)
        rk = next((r for r in rows if r.get("ok") and r["j"] == j and r["k"] == j + 2), None)
        if rk is None or pj is None or uj is None:
            continue
        uk = rk["uk"]
        # 由 s* 之定義反推 `宗k` 近側界之通過點：p_k 於 `analyse_cell` 內為 nfk[1]
        r_k = (rec["ress"] or [None] * (j + 3))[j + 2]
        nf = w81.faces_of(w81.SOLVE.get(id(r_k)))[0]
        if nf is None:
            continue
        pk = np.asarray(nf[1], float)[:2]
        s_cur = s_front_of_line(pk, uk, o_, d_)
        # ── 🔒 推進號之**二源**（節 107·⛔ 不得靜默取 0）─────────────────────
        #    源甲 `sign_star` ＝ `s*(j,k)` 對 `k` 之增減（🩸 僅 1 個 `k` 時**無從定**）
        #    源乙 `sign_grp` ＝ **該側宗序**之 `s_front(宗i 遠側界)` 逐差之號（恆可定）
        #    🔒 primary ＝ 源乙；二者不合者逐項具名
        sign_star = 0.0
        if a["diffs"]:
            sign_star = 1.0 if a["diffs"][0] > 0 else -1.0
        sign_grp = 0.0
        for _sd2, _idxs2 in groups_of(rec, d_):
            if j not in _idxs2:
                continue
            seq = []
            for _i2 in _idxs2:
                _uf, _pf = w40.far_side_dir_and_pt(rec["biz"][_i2], d_)
                if _uf is None:
                    continue
                _sv = s_front_of_line(np.asarray(_pf, float), _uf, o_, d_)
                if _sv is not None:
                    seq.append(_sv)
            if len(seq) >= 2:
                _dd = [seq[t + 1] - seq[t] for t in range(len(seq) - 1)]
                sign_grp = 1.0 if sum(_dd) > 0 else -1.0
        sign = sign_grp if sign_grp != 0.0 else sign_star
        SIGN_SRC.append((key, j, sign_star, sign_grp, sign))
        # 弦之二端於 FRONTLINE-s 之投影（過端點且 ∥ û_k 之直線）
        sA = s_front_of_line(np.asarray(pj, float) + ci["lam_a"] * np.asarray(uj, float), uk, o_, d_)
        sB = s_front_of_line(np.asarray(pj, float) + ci["lam_b"] * np.asarray(uj, float), uk, o_, d_)
        if sA is None or sB is None or s_cur is None:
            continue
        # ── A-0(甲)：**端點式**（單 `k` 之讀法·僅於 `s*` 對 `k` 單調時充分）──────
        S_end = max(sA, sB) if sign >= 0 else min(sA, sB)

        # ── 🔴 **全稱式**（`P3` 否證後之正解·施工單 A-2-2 所令）───────────────
        #    `s*(δ)` 對 `δ` **仿射**：`s*(δ) = s*(0) + c_k·δ`，`c_k = cross(d̂,û_k)/sinα`
        #    ⇒ 每個 `k` 給一個**禁區間** `δ ∈ [lo_k, hi_k]`（由 `[λ_a, λ_b]` 反解）
        #    ⇒ 🔒 **A-0(甲)：取 `max_k hi_k`（推進為 +）／`min_k lo_k`（推進為 −）**
        #       ——⛔ 非「最小可行 δ」，係**越過全部禁區間**之保守值（⇒ 差偏大）
        forb, degen = [], []
        for r in rows:
            if not (r.get("ok") and r["j"] == j and r["d"] >= D_MIN):
                continue
            uk2 = _u(r["uk"])
            r_k2 = (rec["ress"] or [None] * (r["k"] + 1))[r["k"]]
            nf2 = w81.faces_of(w81.SOLVE.get(id(r_k2)))[0]
            if nf2 is None or uk2 is None:
                continue
            pk2 = np.asarray(nf2[1], float)[:2]
            uj_a = np.asarray(uj, float)
            sin_a = float(uj_a[0] * uk2[1] - uj_a[1] * uk2[0])
            if abs(sin_a) < 1e-15:
                degen.append((r["k"], "sinα≈0"))
                continue
            c_k = float(d_[0] * uk2[1] - d_[1] * uk2[0]) / sin_a
            dv0 = pk2 - np.asarray(pj, float)
            s0 = float(dv0[0] * uk2[1] - dv0[1] * uk2[0]) / sin_a
            if abs(c_k) < 1e-15:
                degen.append((r["k"], "c_k≈0（平移⛔ 不改 s*）"))
                continue
            e1 = (ci["lam_a"] - s0) / c_k
            e2 = (ci["lam_b"] - s0) / c_k
            forb.append((min(e1, e2), max(e1, e2), r["k"], c_k, s0))
        if forb:
            d_all = max(x[1] for x in forb) if sign >= 0 else min(x[0] for x in forb)
        else:
            d_all = 0.0
        S_all = s_cur + d_all
        S_req = S_all              # 🔒 **本檔之 `S_req` 一律採全稱式**（⛔ 端點式僅並陳）
        # `K-9-9 二` 之下限（對 `宗(j+1)`·以源甲走該側得之）
        lim = None
        fr_ok = True
        for side, idxs in groups_of(rec, d_):
            if j in idxs and (j + 1) in idxs:
                prev = None
                for i in idxs:
                    uf, pf = w40.far_side_dir_and_pt(rec["biz"][i], d_)
                    if uf is None:
                        continue
                    Pc = w40.line_isect(tuple(pf), tuple(uf), o_, d_)
                    Bc = w40.line_isect(tuple(pf), tuple(uf), bpt, bdir)
                    if Pc is None or Bc is None:
                        prev = None
                        continue
                    if prev is not None and i == j + 1:
                        _c, st, _df, _cd = w40.eval_lot(prev[0], prev[1], Pc, Bc, o_, d_, n_)
                        lim = st[0]
                    prev = (Pc, Bc)
        if lim is None:
            fr_ok = False

        def overlap_after(delta):
            """把 `宗(j+1)` 遠側界及其後各近側界沿 `d̂` 平移 `delta` 後之重疊對數／面積。

            🔒 平移之施用對象 ＝ **全部 `k ≥ j+2` 之近側界**（因其皆位於 `宗(j+1)` 遠側界之後·
              契約：接續性已由 `-83` 實測界面距離 0.000000 m 坐實）。⛔ 不改面積、⛔ 不解 `S`。
            """
            n_pair = 0
            for r in rows:
                if not (r.get("ok") and r["j"] == j and r["d"] >= D_MIN):
                    continue
                pk2 = np.asarray(r["pk"], float)[:2] if "pk" in r else None
                if pk2 is None:
                    r_k2 = (rec["ress"] or [None] * (r["k"] + 1))[r["k"]]
                    nf2 = w81.faces_of(w81.SOLVE.get(id(r_k2)))[0]
                    if nf2 is None:
                        continue
                    pk2 = np.asarray(nf2[1], float)[:2]
                pk2 = pk2 + delta * np.asarray(d_, float)
                uk2 = _u(r["uk"])
                sin_a = float(np.asarray(uj)[0] * uk2[1] - np.asarray(uj)[1] * uk2[0])
                if abs(sin_a) < 1e-15:
                    continue
                dv = pk2 - np.asarray(pj, float)
                d_signed = float(dv[0] * uk2[1] - dv[1] * uk2[0])
                s_star2 = d_signed / sin_a
                if w82.pred_chord(ci, s_star2):
                    n_pair += 1
            return n_pair

        d_req = S_req - s_cur
        d_lim = (lim - s_cur) if fr_ok else float("nan")
        n_now = overlap_after(0.0)
        n_req = overlap_after(d_req)                                   # 恰在門檻（閉區間 ⇒ 偏大）
        n_beyond = overlap_after(d_req + EPS_SHIM * (1.0 if sign >= 0 else -1.0))
        n_before = overlap_after(d_req - EPS_SHIM * (1.0 if sign >= 0 else -1.0))
        n_lim = overlap_after(d_lim) if fr_ok else -1
        SHIM.append({"key": key, "j": j, "sign": sign, "s_cur": s_cur, "S_req": S_req,
                     "S_end": S_end, "lim": lim, "n_now": n_now, "n_req": n_req,
                     "n_beyond": n_beyond, "n_before": n_before, "n_lim": n_lim,
                     "is_corner": a["is_corner"], "sA": sA, "sB": sB, "degen": degen,
                     "compliant": (sign * (s_cur - S_req)) >= 0})
        P("  %-6s %-5s %-4d %-7s %11.4f %11.4f %11.4f %11s %-6s %-6s %-6s %-6s"
          % ("%gm" % key[0], key[1], j, "+1" if sign >= 0 else "−1",
             s_cur, S_req, S_end, ("%.4f" % lim) if fr_ok else "—",
             "%d" % n_now, "**%d**" % n_beyond, "%d" % n_before,
             ("%d" % n_lim) if fr_ok else "—"))
    _sdis = [x for x in SIGN_SRC if x[2] != 0.0 and x[3] != 0.0 and x[2] != x[3]]
    _sonly = [x for x in SIGN_SRC if x[2] == 0.0]
    P("  🔒 **推進號之二源**（節 107）：`sign_star`（`s*` 逐差）vs `sign_grp`（宗序逐差）——**不合者 %d**；"
      "`sign_star` 無從定（僅 1 個 `k`）者 **%d**：%s" % (len(_sdis), len(_sonly), [(x[0], x[1]) for x in _sonly]))
    if _sdis:
        P("     🔴 **二源不合者逐項具名**：%s" % _sdis)
    POP(len(SHIM), len(SHIM), "A-2 shim 驗證（全列）")
    dg = [(x["key"], x["j"], x["degen"]) for x in SHIM if x["degen"]]
    if dg:
        P("  ⚠️ **退化之 `k`（`sinα≈0` 或 `c_k≈0`·⛔ 平移不改其 `s*`）逐項具名**：%s" % dg)
    brk = [x for x in SHIM if x["n_now"] > 0]
    P("  🔴 **現況即有重疊之 (格,j) ＝ %d**：%s"
      % (len(brk), [("%gm" % x["key"][0], x["key"][1], x["j"]) for x in brk]))
    # 🔒 全母體之**門檻銳利度**（⛔ 不只看破閘格）：+ε 須全 0；−ε 須 > 0
    n_bey0 = sum(1 for x in SHIM if x["n_beyond"] == 0)
    n_bef1 = sum(1 for x in SHIM if x["n_before"] > 0)
    P("  🔒 **門檻之銳利度（全母體 %d 格·⛔ 非只看破閘格）**："
      "`門檻+ε` 之重疊 ＝ 0 者 **%d／%d**；`門檻−ε` 之重疊 > 0 者 **%d／%d**"
      % (len(SHIM), n_bey0, len(SHIM), n_bef1, len(SHIM)))
    bad_bey = [(x["key"], x["j"], x["n_beyond"]) for x in SHIM if x["n_beyond"] != 0]
    bad_bef = [(x["key"], x["j"], x["n_before"]) for x in SHIM if x["n_before"] == 0]
    if bad_bey:
        P("     🔴 **`+ε` 仍 > 0 者逐項具名**：%s" % bad_bey)
    if bad_bef:
        P("     ⚠️ **`−ε` 為 0 者逐項具名**（⇒ 該格之門檻⛔ 非銳利·或其現況本即無 `k` 可落入弦）：%s"
          % bad_bef)
    if brk:
        ok_req = all(x["n_beyond"] == 0 for x in brk)
        pos_lim = all(x["n_lim"] > 0 for x in brk if x["n_lim"] >= 0)
        P("  🔒 **`P2` 之判（受詞 ＝ 破閘之 (格,j)·位置取 `S_req + ε`）**：重疊**全部 ＝ 0** ⇒ %s"
          % ("✅ **`P2` 成立**" if ok_req else "🔴 **仍 > 0·具名**"))
        P("     🔒 **負對照**：shim→`K-9-9 二` 下限之重疊**仍 > 0** ⇒ %s"
          % ("✅ **二者不同 ⇒ `S_req` 有判別力**" if pos_lim else
             "🔴 **負對照亦為 0 ⇒ `S_req` 無判別力·具名**"))
        for x in brk:
            P("     [%gm] %-4s j=%d：現況 %d 對 ／ `S_req+ε` %d 對 ／ `S_req−ε` %d 對 ／ →下限 %s 對"
              % (x["key"][0], x["key"][1], x["j"], x["n_now"], x["n_beyond"],
                 x["n_before"], x["n_lim"] if x["n_lim"] >= 0 else "—"))
    n_endeq = sum(1 for x in SHIM if abs(x["S_req"] - x["S_end"]) <= 1e-6)
    P("  🔒 **全稱式 vs 端點式**：二者相等（≤1e−6）者 **%d ／ %d**；"
      "不等者即 `P3` 之非單調格之後果（⇒ 端點式**不足**·具名）" % (n_endeq, len(SHIM)))

    # ══ 【E／A-3】`S_req` 與 `K-9-9 二` 下限之差 ═══════════════════════
    P("")
    P("【E／A-3】`S_req` 與 `K-9-9 二` 下限之**差**（🔒 含**號之聲明**·節 107）")
    P("-" * W)
    P("  🔒 **號之聲明（⛔ 二式並列·⛔ 只寫一式者視同半式）**：")
    P("     號 ＝ `sign` ＝ **推進方向於 FRONTLINE-`s` 之增減**，由 `s*(j,k)` 對 `k` 之增減定"
      "（⛔ 非由街廓名／側別硬編）。")
    P("     **式一（`sign = +1`）**：需 `s(宗j+1 far) ≥ S_req = max(sA, sB)`；"
      "「下限較鬆」⟺ **`S_req > 下限`** ⇒ 差 ＝ `S_req − 下限` **> 0**")
    P("     **式二（`sign = −1`）**：需 `s(宗j+1 far) ≤ S_req = min(sA, sB)`；"
      "「下限較鬆」⟺ **`S_req < 下限`** ⇒ 差 ＝ `S_req − 下限` **< 0**")
    P("     ⇒ 🔒 **統一之判準 ＝ `sign · (S_req − 下限) > 0`**（⇒ 正典下限較鬆）")
    P("")
    P("  %-6s %-5s %-4s %-8s %-7s %12s %12s %14s %14s %-12s"
      % ("情境", "街廓", "j", "推進號", "是街角?", "**S_req**", "K-9-9 下限",
         "差(S_req−下限)", "sign×差", "下限較鬆?"))
    n_loose = n_tot = 0
    rows_e3 = []
    for x in SHIM:
        if x["lim"] is None:
            continue
        diff = x["S_req"] - x["lim"]
        sd = x["sign"] * diff
        n_tot += 1
        n_loose += int(sd > 0)
        rows_e3.append((x, diff, sd))
        P("  %-6s %-5s %-4d %-8s %-7s %12.4f %12.4f %14.4f %14.4f %-12s"
          % ("%gm" % x["key"][0], x["key"][1], x["j"],
             "+1(增)" if x["sign"] >= 0 else "−1(減)",
             "**是**" if x["is_corner"] else "否",
             x["S_req"], x["lim"], diff, sd,
             "✅ 較鬆" if sd > 0 else "🔴 **較緊/相等**"))
    POP(n_tot, n_tot, "A-3 逐 (格,j)（全列）")
    P("  🔒 **`P4` 之判（受詞 ＝ 破閘之 (格,j)）**：")
    brk_keys = {(x["key"], x["j"]) for x in brk}
    b_loose = [t for t in rows_e3 if (t[0]["key"], t[0]["j"]) in brk_keys]
    if b_loose:
        for x, diff, sd in b_loose:
            P("     [%gm] %-4s j=%d：`S_req` %.4f ／ 下限 %.4f ／ **sign×差 ＝ %+.4f** ⇒ %s"
              % (x["key"][0], x["key"][1], x["j"], x["S_req"], x["lim"], sd,
                 "✅ 下限較鬆" if sd > 0 else "🔴 **下限⛔ 不較鬆 ⇒ 該格之重疊⛔ 非「下限太鬆」所致·具名**"))
        P("     ⇒ %s" % ("✅ **`P4` 成立**（破閘格皆 `sign×差 > 0`）"
                         if all(t[2] > 0 for t in b_loose) else "🔴 **`P4` 不成立·已逐格具名**"))
    else:
        P("     ⚠️ **破閘格之 `下限` 取不到 ⇒ `P4` ⛔ 無從判·具名**")
    P("  🔒 **全母體**：`sign×差 > 0` 者 ＝ **%d ／ %d**" % (n_loose, n_tot))
    if rows_e3:
        sds = sorted(t[2] for t in rows_e3)
        P("     🔒 **節 103**：最接近翻面者 ＝ **%+.6f**（次近 %+.6f）；`|sign×差|` 之量級 ∈ [%.4f, %.4f]"
          % (min(sds, key=abs), sorted(sds, key=abs)[1] if len(sds) > 1 else float("nan"),
             min(abs(t[2]) for t in rows_e3), max(abs(t[2]) for t in rows_e3)))

    # ══ 【F／A-4】出題資格現查 ═══════════════════════════════════════
    P("")
    P("【F／A-4】常設第 12 條 ③ 之落實——出題資格現查（`docs/rulings/` **全庫**）")
    P("-" * W)
    rul = os.path.join(REPO, "docs", "rulings")
    files_r = sorted(f for f in os.listdir(rul) if f.endswith(".md"))
    P("  母體 ＝ `docs/rulings/**.md` ＝ **%d 檔**：%s" % (len(files_r), files_r))
    A4KEYS = ["弦出口", "更強之下限", "非相鄰", "不相鄰", "跨宗", "間隔", "出口", "弦",
              "遠側境界線", "起算垂線"]
    P("  %-14s %8s %-46s" % ("字樣", "命中行數", "落點行號（全列）"))
    a4 = {}
    for fn in files_r:
        Lr = io.open(os.path.join(rul, fn), encoding="utf-8", errors="replace").read().split(chr(10))
        for kk in A4KEYS:
            idx = [i + 1 for i, l in enumerate(Lr) if kk in l]
            a4.setdefault(kk, []).extend(idx)
    for kk in A4KEYS:
        P("  %-14s %8d %-46s" % (kk, len(a4[kk]), str(a4[kk][:12])))
    POP(len(A4KEYS), len(A4KEYS), "A-4 逐字樣（全列）")
    core = ["弦出口", "更強之下限", "非相鄰", "不相鄰", "跨宗", "出口"]
    tot_core = sum(len(a4[k]) for k in core)
    P("  🔒 **`P6` 之判**：核心受詞（%s）之命中合計 ＝ **%d** ⇒ %s"
      % ("／".join(core), tot_core,
         "✅ **＝ 0（`P6` 成立）⇒ 下一批<u>得</u>就該受詞出裁定題**" if tot_core == 0 else
         "🔴 **≥ 1 ⇒ ⛔ 下一批不得就該受詞出題·改為落地狀態現查**"))
    P("     🔒 **判別力對照（常設 12 ①②）**：`K-9-5-4`／`K-9-2` 之命中須 > 0 ⇒ 見 §A（本檔⛔ 不重跑）")
    P("  ⚠️ **節 92：命中唯一 ≠ 該款仍有效** ⇒ 非零者逐處判其**是否仍有效**：")
    for kk in ("弦", "間隔"):
        for ln_no in a4[kk]:
            Lr = io.open(os.path.join(rul, files_r[0]), encoding="utf-8",
                         errors="replace").read().split(chr(10))
            P("     %-4s :%-6d %s" % (kk, ln_no, Lr[ln_no - 1].strip()[:110]))

    # ══ 【G／P7】第十法 ═══════════════════════════════════════════════
    P("")
    P("【G／P7】`run_all` 清單筆數之**第十法**（🔒 文件側對帳法·⛔ 與九法不同族）")
    P("-" * W)
    rows10 = run_all_count_method10()
    P("  母體 ＝ `docs/reports/**.md` 中**同時含** `run_all` 與（`夾具` 或 `清單`）之行；"
      "取其 10〜30 之數")
    P("  命中行數 ＝ **%d**" % len(rows10))
    for fn, ln_, vals in rows10:
        P("     %-46s %s  → %s" % (fn[:46], ln_[:80], vals))
    POP(len(rows10), len(rows10), "第十法之命中行（全列）")
    from collections import Counter
    allv = [v for _f, _l, vs in rows10 for v in vs]
    cnt10 = Counter(allv)
    P("  值之分布 ＝ %s" % dict(sorted(cnt10.items())))
    latest = rows10[-1] if rows10 else None
    P("  **最近一次宣告**（依檔名排序之末筆）＝ %s ⇒ 值 %s"
      % (latest[0] if latest else "—", latest[2] if latest else "—"))
    ans = cnt10.most_common(1)[0][0] if cnt10 else -1
    P("  ⇒ **第十法所得（最常見宣告值）＝ %d**（施工單 `P7` 期望 **15**）⇒ %s"
      % (ans, "✅ 相符" if ans == 15 else "🔴 **不符·⛔ 不調整預測·具名**"))
    P("  ⚠️ 🔒 **本法之失效模式（⛔ 須併出艙）**：本法量的是**紀錄**、⛔ 非碼——"
      "紀錄若集體寫錯，本法會**一致地錯** ⇒ 🔒 **只能作為第 10 支、⛔ 不得單獨採信。**")
    if 14 in cnt10:
        P("  🔒 **本法獨有之可見物**：紀錄中另有 **14** 之宣告 %d 次 ⇒ 其為 `W-G.9-73` 之"
          "「13 → 14 → 15」歷程（八九法皆看不見**紀錄側**之歷程）" % cnt10[14])

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
