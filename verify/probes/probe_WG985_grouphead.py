# -*- coding: utf-8 -*-
r"""**W-G.9-85 §二 A 組**：組首與推進向 ／ 依 `K-9-14` 重界母體 ／ 左側跳號 ／ 錨點更正。

## 受詞（施工單 `W-G.9-85` §二·`VR-043` 七）
- **A-1**（🛑 第一項）**組首與推進向**——逐 (情境, 街廓, 側) 出艙宗序／組首／推進向／
  「現行前一宗」vs「依組內推進向之前一宗」之**逐宗對照**。
- **A-2** 依 **`K-9-14`** 重界母體並重量 35 宗（受詞 ＝ 街角宗之**次一宗**）。
- **A-3** **左側三組跳號**之另一機制。
- **A-4** **錨點更正**：起算垂線之錨由「前一宗之**起點**」改為「前一宗之**終點**」＋ 弦區間閉式重跑。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單將使違反宗數**由 35 大幅下降**。其瑕若使**下降過多** ⇒ 把本應不配地之宗放行
⇒ 🔴 **土地後果⛔ 非零**，且與現行結論一致 ⇒ **安靜**。
🔒 **事前選定：偏向<u>保留違反</u>**——落實為三條，⛔ 逐條具名：
  (甲) 「受詞內」之判定取**較寬**之門檻（`|sin| > 1e-9` 即入受詞·⛔ 非 `> 1e-3`）⇒ **受詞內之宗較多** ⇒ 違反較多；
  (乙) 「組首／推進向」之認定若二源不合，**取使該宗仍判違反**之認定並具名；
  (丙) `K-9-9 二` 之判定式沿用 `w40.eval_lot`（含其 `-1e-6` 容差）⇒ ⛔ 不放寬。

## 🔒 A-4 之 shim 與 §七-6 之區別（施工單所令之逐字聲明）
本檔之 shim **只改「起算垂線之錨點」**（前一宗之起點 → 終點）與**沿 `d̂` 平移一條界線之位置**，
⛔ **不改面積目標**、⛔ **不解 `S`**（`solve_G_binary` 未被呼叫）⇒ ⛔ **非** §七-6 所禁之「shim `S`」。

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
- `K-9-9 二` 判定式：**原樣 import** `probe_WG940_startperp` 之 `eval_lot`／`far_side_dir_and_pt`／
  `line_isect`／`s_of`（⛔ 未重寫一行）。
- 弦區間謂詞：**原樣 import** `probe_WG982_chord` 之 `ring_edges`／`chord_interval`／`pred_chord`／
  `pj_of`／`uj_of`。
- 逐格逐對之構造：**原樣 import** `probe_WG981_scope` 之 `analyse_cell`／`spy_solve`／`spy_pool`／`faces_of`。
- `probe_WG983_k99prep`／`probe_WG984_gap`：其量測邏輯**寫在 `main()` 內⛔ 不可 import**
  （🔒 逐字具名之差）；本檔**原樣 import 其模組級常數與 `s_front_of_line`**，
  且其判定式**與本檔同為 `w40.eval_lot`／`w82.pred_chord`** ⇒ 同源可比。

## ⛔ 本檔不做（施工單 §二 A-5 六款）
⛔ 零 `app.py` 變更；⛔ `data/` 零變更；⛔ 不落地 `K-9-9`／`K-9-14`；⛔ 不建遞補／合併／調配池介面；
⛔ 不換圖／不重烤／不改任何 baseline；⛔ **不判二源孰是孰非**（`D-0` 仍未結·本單只重定**前後宗**）；
⛔ 不出艙「應改領現金之宗」；⛔ **不得以「理論上恆真」代替實算**（A-2-3）。

## 🔒 常設條款
**8** 每個判準附「會使它為否」之輸入；**9** 門檻併出艙量級與 `math.ulp`、跨數量級**分層**；
**10** 每表末印 `POPULATION/PRINTED/SUPPRESSED`，報告中每一 ≥4dp 之數須可回指 log 行；
**11** 修法列動作清單（本檔「⛔ 不經 shell 傳字樣」**適用讀＋寫**·以 `Write` 落盤）；
**12／13** 搜尋規格含正典款號組＋**三類出處分類**——見報告 §A（⛔ 本檔不重跑擴搜）。
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

OUTDIR = os.path.join(VERIFY, "out")
W = 210
SB_MAIN = 0.0                  # 🔒 A-1〜A-4 之母體 ＝ `0m`（＝ `-40`／`-83` 之母體·⛔ 不擴·具名）
D_MIN = w83.D_MIN              # ＝ 2（原樣 import）
EPS_SHIM = w84.EPS_SHIM        # ＝ 1e-6（原樣 import）
TOL_PARA = 1e-9                # A-0(甲)：`|sin| > TOL_PARA` 即入受詞（**較寬** ⇒ 受詞內較多）
TOL_ORD = 1e-6                 # 索引序 vs `s` 序之對齊門檻（`s` 之量級 ~1e2）
ANCHOR_35 = 35                 # 【倉】`probe_WG940_startperp_834bce0.log`
ANCHOR_35_AREA = 5758.9879     # 【倉】同上（帶號合計）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG985_grouphead_%s.log" % COMMIT)
_u = w82._u
s_front_of_line = w84.s_front_of_line


def _sin(a, b):
    a, b = _u(a), _u(b)
    if a is None or b is None:
        return float("nan")
    return abs(float(a[0] * b[1] - a[1] * b[0]))


# ═══ P7 之第十一法：`run_all` 清單筆數 ═════════════════════════════════
def run_all_count_method11():
    r"""🔒 **第十一法：執行輸出側對帳法**（⛔ 與既用十法皆不同族）。

    既用十法之母體：`run_all.py` 之**語法／位元組**（①〜⑦）、**檔案系統**（⑧）、
    **git 增刪歷史**（⑨）、**人所寫下之報告宣告**（⑩）。
    🔴 本法之母體 ＝ **倉內既存之 `run_all` <u>執行 log</u>**——即該清單**實際被執行時**所印之
    「末端夾具 …」行。⇒ 🔒 **它量的是「碼跑起來做了幾件事」**，⛔ 非「原始碼寫了幾筆」。
    🔒 **其獨有之產出**：清單筆數之**執行側時間序**（⇒ 可見 `3 → … → 15` 之實際演進）。
    ⚠️ **失效模式（⛔ 併出艙）**：log 係**過去**之執行 ⇒ 若清單自最後一次執行後又變動，本法會**落後**
    ⇒ 🔒 **須以 git 之 commit 序取「最新且為 `HEAD` 祖先」之 log**，⛔ 不以 `mtime`（checkout 會全部改寫）。
    ⛔ **本法⛔ 不執行 `run_all`**（閘 7）。
    """
    outdir = os.path.join(VERIFY, "out")
    pat = re.compile(r'末端夾具 (\S+\.py)')
    rows = []
    for fn in sorted(os.listdir(outdir)):
        low = fn.lower()
        if ("runall" not in low) and ("run_all" not in low):
            continue
        try:
            txt = io.open(os.path.join(outdir, fn), encoding="utf-8", errors="replace").read()
        except Exception:                                           # noqa: BLE001
            continue
        n = len(pat.findall(txt))
        if not n:
            continue
        m = re.search(r'_([0-9a-f]{7,40})\b', fn)
        sha, order = (m.group(1) if m else None), None
        if sha:
            try:
                r = subprocess.run(["git", "rev-list", "--count", "%s..HEAD" % sha],
                                   cwd=REPO, capture_output=True)
                if r.returncode == 0:
                    order = int(r.stdout.decode().strip())
            except Exception:                                       # noqa: BLE001
                order = None
        rows.append({"fn": fn, "n": n, "sha": sha, "dist": order})
    dated = [r for r in rows if r["dist"] is not None]
    dated.sort(key=lambda r: -r["dist"])       # dist 越小 ＝ 離 HEAD 越近
    return rows, dated


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
          and abs(ci["lam_b"] - hb) <= 8 * math.ulp(abs(hb))
          and w82.pred_chord(ci, 0.0) and not w82.pred_chord(ci, 1e6))
    ok &= r2
    P("  ② **`w82.chord_interval`／`pred_chord` 同源證**：λ=[%.12g, %.12g]（手算同）；"
      "`s*=0` ⇒ %s／`s*=1e6` ⇒ %s（常設 8）⇒ %s"
      % (ci["lam_a"], ci["lam_b"], w82.pred_chord(ci, 0.0), w82.pred_chord(ci, 1e6),
         "PASS" if r2 else "🔴 FAIL"))

    P("  ③ **`w83`／`w84` 常數之原樣 import**：`D_MIN=%s`／`EPS_SHIM=%.1e`／"
      "`w84.TOL_MONO=%.1e`（其量測邏輯在 `main()` 內⛔ 不可 import·逐字具名之差）"
      % (D_MIN, EPS_SHIM, w84.TOL_MONO))
    r3 = (D_MIN == 2 and abs(EPS_SHIM - 1e-6) < 1e-15)
    ok &= r3
    P("     ⇒ %s" % ("PASS" if r3 else "🔴 FAIL"))

    p0, u0 = np.array([3.0, 1.0]), _u((0.4, 0.9))
    s_b = s_front_of_line(p0, u0, o, d)
    s_a = s_front_of_line(p0 + 7.25 * np.asarray(d, float), u0, o, d)
    res = abs((s_a - s_b) - 7.25)
    r4 = res <= 64 * math.ulp(7.25)
    ok &= r4
    P("  ④ **`w84.s_front_of_line` 之平移機制**：δ=7.25 ⇒ 位移 %.12f（殘差 %.3e·**殘差/ulp %.2f**）⇒ %s"
      % (s_a - s_b, res, w82._ulp_ratio(res, 7.25), "PASS" if r4 else "🔴 FAIL"))

    rows11, dated11 = run_all_count_method11()
    r5 = len(rows11) > 0
    ok &= r5
    P("  ⑤ **第十一法非空**：候選 `run_all` 執行 log ＝ %d 支（可定 commit 序者 %d 支）⇒ %s"
      % (len(rows11), len(dated11), "PASS" if r5 else "🔴 FAIL"))

    P("  ⑥ **常設 9**：`TOL_PARA=%.1e`（施於 `|sin|` ∈ [0,1]·`ulp(1.0)=%.3e`）；"
      "`TOL_ORD=%.1e`（施於 `s` 之差·量級 ~1e2·`ulp(1e2)=%.3e`）"
      % (TOL_PARA, math.ulp(1.0), TOL_ORD, math.ulp(1e2)))
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
    P("【W-G.9-85 §二 A 組】組首與推進向／依 `K-9-14` 重界母體／左側跳號／錨點更正")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向<u>保留違反</u>**（甲/乙/丙 三條見 docstring）")
    P("  🔒 情境母體 ＝ **僅 %gm**（＝ `-40`／`-83` 之母體·⛔ 不擴·具名）" % SB_MAIN)
    P("  🔒 A-5-4：⛔ **不判二源孰是孰非**——本檔以**源甲 `w40`**（＝ 35 宗之產生源）為主，"
      "源乙 `w81` 併列作交叉核。")

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
    w81.CUR["setback"] = SB_MAIN
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB_MAIN)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, SB_MAIN, snapshot=snapshot)
    ns["_solve_G_one"], ns["_pool_strips_for_block"] = w81.spy_solve(o_solve), w81.spy_pool(o_pool)
    try:
        for lbl in blks:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, SB_MAIN)
                except Exception:                                   # noqa: BLE001
                    pass
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(w81.CAP)
    FL = cad.get("front_lines") or {}
    BL = cad.get("baselines") or {}
    P("")
    P("【驅動】`%gm` × R1–R6——攔截 **%d 格**" % (SB_MAIN, len(REAL)))

    # ── 逐格逐宗之基礎量 ────────────────────────────────────────────
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
        # 🩸 **框架更正（本批 §I-1）**：`w40` 之 `IV` 係 `x·d̂x + y·d̂y`（**未扣原點**），
        #   其於 `w40` 內只作**相對**比較故無害；本檔另以其為 `s` 值 ⇒ **必須與 `w40.s_of` 同框**
        #   （即扣掉 `o_·d̂`）。⛔ 不扣者會得 ±2e6 之荒謬下限，且 shim 仍偶然得 0（＝**假 ✅**）。
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
            Pc = Bc = sfar = None
            if ua is not None:
                Pc = w40.line_isect(tuple(pa), tuple(ua), o_, d_)
                Bc = w40.line_isect(tuple(pa), tuple(ua), bpt, bdir)
                sfar = s_front_of_line(np.asarray(pa, float), ua, o_, d_)
            lots[i] = {"ua": ua, "pa": pa, "ub": ub, "pb": pb, "Pc": Pc, "Bc": Bc,
                       "s_far": sfar, "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area),
                       "is_corner": i in meta["corners"]}
        CELL[lbl] = {"rec": rec, "o": o_, "d": d_, "n": n_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "kb": kb, "lots": lots, "meta": meta, "rows": rows}

    # ══ 【C／A-1】組首與推進向 ═══════════════════════════════════════
    P("")
    P("【C／A-1】🛑 **組首與推進向**（驗 KL 之推測·⛔ 本單第一項）")
    P("-" * W)
    P("  🔒 **現行「組首／前一宗」之碼面依據逐字**（`probe_WG940_startperp.py` §2·`w40`）：")
    P("     `groups = [('左', list(range(0, k_break))), ('右', list(range(k_break, len(IV))))]`")
    P("     `for side, idxs in groups: prev = None` ⇒ `for i in idxs:` … `prev = (Pc, Bc)`")
    P("     ⇒ 🔒 **組首 ＝ `idxs[0]`（＝ 該組之<u>最小全域宗序</u>）；前一宗 ＝ <u>宗序 `i−1`</u>**"
      "（⛔ 非組內推進序）。")
    P("     🔒 `k_break` 之來源 ＝ 沿 `d̂` 之投影區間**首次完全分離**之索引（⛔ 非硬編）。")
    P("")
    P("  %-5s %-6s %-22s %-6s %-8s %-10s %-10s %-12s %-10s"
      % ("街廓", "側", "宗序清單", "組首", "s(組首)", "s(組末)", "推進向", "索引序vs s序", "二定義"))
    A1 = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for side, idxs in C["groups"]:
            ss = [C["lots"][i]["s_far"] for i in idxs if C["lots"][i]["s_far"] is not None]
            if len(ss) < 2:
                continue
            diffs = [ss[t + 1] - ss[t] for t in range(len(ss) - 1)]
            aligned = sum(diffs) > 0            # 索引序與 s 遞增同向?
            # 推進向：左組 ＝ +s（自左端往中間）／右組 ＝ −s（自右端往中間）
            #   🔒 左右由**該組之 s 位置**定（⛔ 非由名稱），二組推進**相向**
            allg = [(sd, ix) for sd, ix in C["groups"]]
            s_mid = {}
            for sd, ix in allg:
                v = [C["lots"][i]["s_far"] for i in ix if C["lots"][i]["s_far"] is not None]
                s_mid[sd] = (sum(v) / len(v)) if v else float("nan")
            is_low = all(not math.isfinite(s_mid[k2]) or s_mid[side] <= s_mid[k2]
                         for k2 in s_mid)
            adv = +1 if is_low else -1
            same = (aligned and adv > 0) or ((not aligned) and adv < 0)
            A1.append({"lbl": lbl, "side": side, "idxs": idxs, "aligned": aligned,
                       "adv": adv, "same": same, "s_first": ss[0], "s_last": ss[-1]})
            P("  %-5s %-6s %-22s %-6s %-8.3f %-10.3f %-10s %-12s %-10s"
              % (lbl, side, str(idxs)[:22], idxs[0], ss[0], ss[-1],
                 "+1(增·左)" if adv > 0 else "−1(減·右)",
                 "同向" if aligned else "**反向**",
                 "✅ 相同" if same else "🔴 **相反**"))
    POP(len(A1), len(A1), "A-1 逐 (街廓, 側)（全列）")
    P("")
    P("  🔴 **二定義之逐宗對照**（現行 `前一宗 = i−1` vs 依組內推進向之 `前一宗`）")
    P("  %-5s %-6s %-4s %-10s %-10s %-8s" % ("街廓", "側", "i", "現行前一宗", "修正前一宗", "不同?"))
    n_pair = n_diff = 0
    diff_by_side = {}
    for a in A1:
        idxs = a["idxs"]
        order = idxs if a["aligned"] == (a["adv"] > 0) else list(reversed(idxs))
        # 修正：依推進序，前一宗 ＝ 推進序中之前一個
        prev_fix = {}
        for t, i in enumerate(order):
            prev_fix[i] = order[t - 1] if t >= 1 else None
        for t, i in enumerate(idxs):
            cur = idxs[t - 1] if t >= 1 else None
            fix = prev_fix.get(i)
            if cur is None and fix is None:
                continue
            n_pair += 1
            dd = (cur != fix)
            n_diff += int(dd)
            diff_by_side.setdefault((a["lbl"], a["side"]), [0, 0])
            diff_by_side[(a["lbl"], a["side"])][0] += 1
            diff_by_side[(a["lbl"], a["side"])][1] += int(dd)
            if dd:
                P("  %-5s %-6s %-4d %-10s %-10s %-8s"
                  % (a["lbl"], a["side"], i, str(cur), str(fix), "🔴 **是**"))
    POP(n_pair, n_diff, "A-1 二定義逐宗對照（僅列**不同**者）")
    P("  ⇒ **不同者 %d ／ %d**" % (n_diff, n_pair))
    P("  逐 (街廓,側) 之不同數：")
    for k2 in sorted(diff_by_side):
        tot, dd = diff_by_side[k2]
        P("     %-4s %-6s  %d ／ %d %s" % (k2[0], k2[1], dd, tot,
                                           "🔴 **全部不同**" if dd == tot and tot else ""))
    POP(len(diff_by_side), len(diff_by_side), "A-1 逐 (街廓,側) 之不同數（全列）")
    右_all = [a for a in A1 if a["adv"] < 0]
    左_all = [a for a in A1 if a["adv"] > 0]
    右_rev = sum(1 for a in 右_all if not a["same"])
    左_same = sum(1 for a in 左_all if a["same"])
    P("  🔒 **必答**：右側 %d 組中**二定義相反**者 ＝ **%d**；左側 %d 組中**相同**者 ＝ **%d**"
      % (len(右_all), 右_rev, len(左_all), 左_same))
    _ctl = [a for a in A1 if a["adv"] > 0 and a["aligned"]]
    _ctl_diff = sum(diff_by_side.get((a["lbl"], a["side"]), [0, 0])[1] for a in _ctl)
    P("  🔒 **判別力（常設 8）**：對「`推進向 = +1` 且 `索引序同向`」之側（＝ 組首為最小宗序），"
      "二定義須**完全相同** ⇒ 該類側 ＝ **%d 組**（%s），其逐宗**不同數合計 ＝ %d** ⇒ %s"
      % (len(_ctl), [(a["lbl"], a["side"]) for a in _ctl], _ctl_diff,
         "✅ **對照器⛔ 非恆異**" if (_ctl and _ctl_diff == 0)
         else ("🔴 **該類側亦有不同·具名**" if _ctl else "⚠️ **該類側為 0 ⇒ 判別力⛔ 未成立·具名**")))

    # ══ 【D／A-2】依 `K-9-14` 重界母體 ═══════════════════════════════
    P("")
    P("【D／A-2】依 **`K-9-14`** 重界母體並重量 35 宗")
    P("-" * W)
    P("  🔒 **`K-9-14` 逐字**：受詞 ＝「前一宗之遠側境界線為 **∥SIDELINE**」之**次一宗**；"
      "其餘各宗**該款恆真**。")
    P("  🔒 **本檔之操作化**：`|sin(本宗遠側界, 前一宗遠側界)| > %.0e` ⇒ **受詞內**"
      "（A-0(甲)：門檻取**較寬** ⇒ 受詞內較多 ⇒ 違反較多）" % TOL_PARA)
    P("")
    P("  %-5s %-6s %-4s %-8s %-8s %13s %-10s %-10s %-10s %10s"
      % ("街廓", "側", "i", "前一宗", "前宗街角?", "|sin(本,前)|", "受詞內?", "K-9-9 判",
         "舊(35)中?", "面積"))
    A2 = []
    for a in A1:
        C = CELL[a["lbl"]]
        idxs = a["idxs"]
        order = idxs if a["aligned"] == (a["adv"] > 0) else list(reversed(idxs))
        prev_seq = None
        for t, i in enumerate(order):
            lt = C["lots"][i]
            if t == 0 or prev_seq is None:
                prev_seq = i
                A2.append({"lbl": a["lbl"], "side": a["side"], "i": i, "prev": None,
                           "sin": float("nan"), "inscope": False, "code": "（組首·本則不適用）",
                           "area": lt["area"], "is_corner_prev": None})
                continue
            pv = C["lots"][prev_seq]
            sn = _sin(lt["ua"], pv["ua"]) if (lt["ua"] is not None and pv["ua"] is not None) \
                else float("nan")
            inscope = math.isfinite(sn) and sn > TOL_PARA
            code = "—"
            if lt["Pc"] is not None and lt["Bc"] is not None and pv["Pc"] is not None \
                    and pv["Bc"] is not None:
                _c, _st, _df, code = w40.eval_lot(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"],
                                                  C["o"], C["d"], C["n"])
            A2.append({"lbl": a["lbl"], "side": a["side"], "i": i, "prev": prev_seq,
                       "sin": sn, "inscope": inscope, "code": code, "area": lt["area"],
                       "is_corner_prev": pv["is_corner"]})
            prev_seq = i
    OLD35 = set()
    old_path = os.path.join(OUTDIR, w83.OLD_LOG)
    if os.path.exists(old_path):
        txt = io.open(old_path, encoding="utf-8", errors="replace").read()
        seg = txt[txt.index("不合格宗之面積"):] if "不合格宗之面積" in txt else txt
        pt = re.compile(r'^\s+(R\d+)\s+(\S+)\s+(\d+)\s+([-+][\d.]+)\s+([-+][\d.]+)\s+([\d.]+)\s*$')
        for ln in seg.split(chr(10)):
            m = pt.match(ln)
            if m:
                OLD35.add((m.group(1), m.group(2), int(m.group(3))))
    shown = 0
    for r in A2:
        if not (r["inscope"] or r["code"] == "不合格"
                or (r["lbl"], r["side"], r["i"]) in OLD35):
            continue
        shown += 1
        P("  %-5s %-6s %-4d %-8s %-8s %13.3e %-10s %-10s %-10s %10.4f"
          % (r["lbl"], r["side"], r["i"], str(r["prev"]),
             ("**是**" if r["is_corner_prev"] else "否") if r["is_corner_prev"] is not None else "—",
             r["sin"], "**是**" if r["inscope"] else "否", r["code"],
             "是" if (r["lbl"], r["side"], r["i"]) in OLD35 else "否", r["area"]))
    POP(len(A2), shown, "A-2 逐宗（僅列**受詞內**或**不合格**或**舊 35 名單內**者）")

    inscope = [r for r in A2 if r["inscope"]]
    outscope = [r for r in A2 if (not r["inscope"]) and r["prev"] is not None]
    newbad = [r for r in inscope if r["code"] == "不合格"]
    P("")
    P("  🔴 **受詞內 ＝ %d 宗**；**受詞外 ＝ %d 宗**（另組首 %d 宗·本則不適用）"
      % (len(inscope), len(outscope), sum(1 for r in A2 if r["prev"] is None)))
    P("  🔴 **依 `K-9-14` 重界後之違反宗數 ＝ %d**（面積合計 **%.4f ㎡**）"
      % (len(newbad), sum(r["area"] for r in newbad)))
    for r in newbad:
        P("     🔴 %-4s %-6s i=%-3d（前一宗 %s·`|sin|`=%.3e）面積 %.4f ㎡"
          % (r["lbl"], r["side"], r["i"], r["prev"], r["sin"], r["area"]))
    POP(len(newbad), len(newbad), "A-2 新違反宗（全列）")
    newset = {(r["lbl"], r["side"], r["i"]) for r in newbad}
    P("  🔒 **與舊 35 之對照**（舊名單解析所得 %d 筆·錨【倉】`%s`）：" % (len(OLD35), w83.OLD_LOG))
    P("     **交集 ＝ %s**（%d）" % (sorted(newset & OLD35), len(newset & OLD35)))
    P("     **新∖舊 ＝ %s**（%d）" % (sorted(newset - OLD35), len(newset - OLD35)))
    P("     **舊∖新 ＝ %d 宗**（⇒ 依 `K-9-14` 轉為<u>恆真</u>者）" % len(OLD35 - newset))
    P("  🔒 **`P3` 之判**：實得 **%d** 宗（施工單期望 **4**·名單 `R1右3`／`R3右8`／`R5左1`／`R6右7`）⇒ %s"
      % (len(newbad),
         "✅ 相符" if sorted(newset) == sorted({("R1", "右", 3), ("R3", "右", 8),
                                                ("R5", "左", 1), ("R6", "右", 7)})
         else "🔴 **不符·二差集已逐宗列出·具名**"))

    # A-2-3：受詞外之宗**逐宗實算**（⛔ 不得以「理論上恆真」跳過）
    P("")
    P("  🔴 **A-2-3：受詞外之宗<u>逐宗實算</u>**（⛔ 不得以「理論上恆真」代替）")
    sins_out = [r["sin"] for r in outscope if math.isfinite(r["sin"])]
    sins_in = [r["sin"] for r in inscope if math.isfinite(r["sin"])]
    P("     受詞外 %d 宗之 `|sin|`：極大 **%.3e**／中位 %.3e／極小 %.3e"
      % (len(sins_out), max(sins_out) if sins_out else float("nan"),
         sorted(sins_out)[len(sins_out) // 2] if sins_out else float("nan"),
         min(sins_out) if sins_out else float("nan")))
    P("     受詞內 %d 宗之 `|sin|`：極小 **%.3e**／極大 %.3e"
      % (len(sins_in), min(sins_in) if sins_in else float("nan"),
         max(sins_in) if sins_in else float("nan")))
    p4a = all(x <= 1e-9 for x in sins_out) if sins_out else False
    p4b = all(x > 1e-3 for x in sins_in) if sins_in else False
    P("  🔒 **`P4` 之判**：受詞外皆 `≤ 1e-9` ⇒ %s；受詞內皆 `> 1e-3` ⇒ %s ⇒ %s"
      % (p4a, p4b, "✅ **二群完全分離**" if (p4a and p4b) else "🔴 **未完全分離·具名**"))
    if sins_out and sins_in:
        P("     🔒 **節 103（最接近翻面者及其餘裕）**：受詞外之**極大** ＝ **%.3e**"
          "（餘裕至 `1e-9` ＝ %.3e）；受詞內之**極小** ＝ **%.3e**（餘裕至 `1e-3` ＝ %.3e）"
          % (max(sins_out), 1e-9 - max(sins_out), min(sins_in), min(sins_in) - 1e-3))

    # ── 🔴 A-2 之**二源 × 二門檻**（CC 自補·⛔ 施工單未令·⛔ 不判孰是孰非）────────
    P("")
    P("  🔴 **A-2 之敏感度：二源 × 二門檻**（CC 自補·⛔ 施工單未令）")
    P("  🔒 **理由**：`|sin|` 之分布**非二分而是三層**——受詞外 `≤ 8.2e-10`、"
      "**中間層 `~1e-8`**、真 ∥SIDELINE `~1e-2`。A-0(甲) 之 `1e-9` 把中間層**納入**受詞內"
      "（⇒ 違反較多·保守）；施工單 `P4` 之界為 `1e-3`。⇒ 二者並陳。")

    def recount(src, thr):
        """以指定源與門檻重跑 A-2。回 (受詞內, 違反宗集合)。⛔ 不判孰是孰非。"""
        ins, bad = [], set()
        for aa in A1:
            CC = CELL[aa["lbl"]]
            idxs = aa["idxs"]
            order = idxs if aa["aligned"] == (aa["adv"] > 0) else list(reversed(idxs))
            pv_i = None
            for t, i in enumerate(order):
                lt2 = CC["lots"][i]
                uu, pp = (lt2["ua"], lt2["pa"]) if src == "甲" else (lt2["ub"], lt2["pb"])
                if t == 0 or pv_i is None:
                    pv_i = i
                    continue
                pv2 = CC["lots"][pv_i]
                uu_p, pp_p = (pv2["ua"], pv2["pa"]) if src == "甲" else (pv2["ub"], pv2["pb"])
                sn2 = _sin(uu, uu_p) if (uu is not None and uu_p is not None) else float("nan")
                if math.isfinite(sn2) and sn2 > thr:
                    ins.append((aa["lbl"], aa["side"], i, sn2))
                    Pc2 = w40.line_isect(tuple(pp), tuple(uu), CC["o"], CC["d"])
                    Bc2 = w40.line_isect(tuple(pp), tuple(uu), CC["bpt"], CC["bdir"])
                    Pp2 = w40.line_isect(tuple(pp_p), tuple(uu_p), CC["o"], CC["d"])
                    Bp2 = w40.line_isect(tuple(pp_p), tuple(uu_p), CC["bpt"], CC["bdir"])
                    if None not in (Pc2, Bc2, Pp2, Bp2):
                        _c2, _s2b, _d2b, cd2 = w40.eval_lot(Pp2, Bp2, Pc2, Bc2,
                                                            CC["o"], CC["d"], CC["n"])
                        if cd2 == "不合格":
                            bad.add((aa["lbl"], aa["side"], i))
                pv_i = i
        return ins, bad

    P("  %-6s %-10s %-10s %-14s %-46s"
      % ("源", "門檻", "受詞內", "違反宗數", "違反名單"))
    EXP = {("R1", "右", 3), ("R3", "右", 8), ("R5", "左", 1), ("R6", "右", 7)}
    for src in ("甲", "乙"):
        for thr, nm in ((TOL_PARA, "1e-9(A-0寬)"), (1e-3, "1e-3(P4界)")):
            ins2, bad2 = recount(src, thr)
            P("  %-6s %-10s %-10d %-14d %-46s"
              % ("源" + src, nm, len(ins2), len(bad2), str(sorted(bad2))[:46]))
    P("  🔒 **施工單 `P3` 之期望名單** ＝ %s" % sorted(EXP))
    for src in ("甲", "乙"):
        _i2, b2 = recount(src, 1e-3)
        P("     源%s @ `1e-3`：**交集 %s**／新∖期望 %s／期望∖新 %s ⇒ %s"
          % (src, sorted(b2 & EXP), sorted(b2 - EXP), sorted(EXP - b2),
             "✅ **與期望一致**" if b2 == EXP else "🔴 **不一致·已逐宗列出**"))
    P("  ⛔ **本表⛔ 不判二源孰是孰非**（施工單 §二 A-5-4·`D-0` 仍未結）——只出艙其**敏感度**。")

    # ══ 【E／A-3】左側三組跳號 ═══════════════════════════════════════
    P("")
    P("【E／A-3】**左側三組跳號**之另一機制（⛔ 右側之解釋不涵蓋此）")
    P("-" * W)
    TARGET = [("R2", "左"), ("R5", "左"), ("R6", "左")]
    P("  %-5s %-4s %-6s %13s %13s %11s %11s %10s %-8s %10s %10s"
      % ("街廓", "i", "舊35中?", "|sin|(源甲對前)", "|sin|(甲乙二源)", "Δfront", "Δbase",
         "面積", "w40 取邊", "候選邊s中1", "候選邊s中2"))
    e3 = 0
    for lbl, side in TARGET:
        C = CELL.get(lbl)
        if C is None:
            continue
        a = next((x for x in A1 if x["lbl"] == lbl and x["side"] == side), None)
        if a is None:
            continue
        idxs = a["idxs"]
        prev = None
        for i in idxs:
            lt = C["lots"][i]
            e3 += 1
            df = ("—", "—")
            if prev is not None and lt["Pc"] is not None and lt["Bc"] is not None:
                _c, _st, _d2, _cd = w40.eval_lot(C["lots"][prev]["Pc"], C["lots"][prev]["Bc"],
                                                 lt["Pc"], lt["Bc"], C["o"], C["d"], C["n"])
                df = ("%+.4f" % _d2[0], "%+.4f" % _d2[1])
            sn_prev = _sin(lt["ua"], C["lots"][prev]["ua"]) if prev is not None else float("nan")
            sn_2src = _sin(lt["ua"], lt["ub"]) if lt["ub"] is not None else float("nan")
            ext = list(C["rec"]["biz"][i].exterior.coords)
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
            P("  %-5s %-4d %-6s %13.3e %13.3e %11s %11s %10.4f %-8s %10.4f %10.4f"
              % (lbl, i, "**是**" if (lbl, side, i) in OLD35 else "否",
                 sn_prev, sn_2src, df[0], df[1], lt["area"],
                 str(two[1][1]) if len(two) > 1 else "—",
                 two[0][2] if two else float("nan"),
                 two[1][2] if len(two) > 1 else float("nan")))
            prev = i
    POP(e3, e3, "A-3 左側三組逐宗（中與不中皆列）")
    P("  🔒 **`P6` 之必答**：中與不中之分界，**是否可由單一量區辨**？")
    hit = [r for r in A2 if (r["lbl"], r["side"], r["i"]) in OLD35
           and (r["lbl"], r["side"]) in [("R2", "左"), ("R5", "左"), ("R6", "左")]]
    mis = [r for r in A2 if (r["lbl"], r["side"], r["i"]) not in OLD35
           and (r["lbl"], r["side"]) in [("R2", "左"), ("R5", "左"), ("R6", "左")]
           and r["prev"] is not None]
    for nm, f in (("`|sin|`(對前一宗)", lambda r: r["sin"]),
                  ("面積", lambda r: r["area"])):
        hv = [f(r) for r in hit if math.isfinite(f(r))]
        mv = [f(r) for r in mis if math.isfinite(f(r))]
        if hv and mv:
            sep = (max(hv) < min(mv)) or (min(hv) > max(mv))
            P("     %-18s 中者 ∈ [%.4e, %.4e]／不中者 ∈ [%.4e, %.4e] ⇒ %s"
              % (nm, min(hv), max(hv), min(mv), max(mv),
                 "✅ **完全分離**" if sep else "🔴 **重疊 ⇒ 該量⛔ 不能區辨**"))

    # ══ 【F／A-4】錨點更正 ═══════════════════════════════════════════
    P("")
    P("【F／A-4】**錨點更正**：起算垂線之錨由「前一宗之<u>起點</u>」改為「前一宗之<u>終點</u>」")
    P("-" * W)
    P("  🔒 **shim 之逐字聲明**：本項只改**錨點**與**沿 `d̂` 平移一條界線之位置**，"
      "⛔ 不改面積目標、⛔ 不解 `S` ⇒ ⛔ 非 §七-6 所禁者。")
    P("  🔒 **新錨之定式**：`前一宗之終點` ＝ 該宗多邊形沿 `d̂` 之 `s` **極值**"
      "（推進 `+1` 取 `max`／推進 `−1` 取 `min`）")
    P("")
    P("  %-5s %-6s %-4s %13s %13s %13s %13s %11s"
      % ("街廓", "側", "j", "原錨下限", "**新錨下限**", "`S_req`(-84)", "宗j s 域", "新錨−S_req"))
    F4 = []
    for r in inscope:
        lbl, side, i = r["lbl"], r["side"], r["i"]
        C = CELL[lbl]
        a = next((x for x in A1 if x["lbl"] == lbl and x["side"] == side), None)
        j = r["prev"]
        if j is None or a is None:
            continue
        pv, lt = C["lots"][j], C["lots"][i]
        if None in (pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"]):
            continue
        _c, st, _df, _cd = w40.eval_lot(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"],
                                        C["o"], C["d"], C["n"])
        lim_old = st[0]
        # 🩸 **框之更正（本批 §I-2）**：`下限`／`S_req` 皆係「**∥ALLOC 直線之 FRONTLINE 截距**」
        #   ——其等同**帶軸框**之 `s`（本檔【A-4 二框關係】已實證：`框乙(X_exit) == S_req`）。
        #   ⛔ **⛔ 不得取多邊形頂點之<u>框甲</u>投影極值**（首版之誤·得 4.2715 而非 7.4487）。
        m_hat0, denom0 = strip_axis(C["rec"]["d_hat"], C["rec"]["alloc"])
        m_hat0 = np.asarray(m_hat0, float)[:2]
        bp00 = np.asarray(C["rec"]["corner_pt"], float)[:2]
        sv0 = [float(np.dot(np.asarray(c, float)[:2] - bp00, m_hat0)) / denom0
               for c in list(C["rec"]["biz"][j].exterior.coords)]
        lim_new = max(sv0) if a["adv"] > 0 else min(sv0)
        # `S_req`：原樣以 `w82` 之弦區間重算（⛔ 不 import `w84.main` 內之邏輯）
        pj, uj = w82.pj_of(C["rec"], j), w82.uj_of(C["rec"], j)
        S_req = float("nan")
        ci = None
        if pj is not None and uj is not None and C["rec"]["block"] is not None:
            edges, _dg = w82.ring_edges(list(C["rec"]["block"].exterior.coords))
            ci = w82.chord_interval(edges, pj, uj)
            rk = next((x for x in C["rows"] if x.get("ok") and x["j"] == j
                       and x["k"] == j + 2), None)
            if rk is not None:
                uk = _u(rk["uk"])
                sA = s_front_of_line(np.asarray(pj, float) + ci["lam_a"] * np.asarray(uj, float),
                                     uk, C["o"], C["d"])
                sB = s_front_of_line(np.asarray(pj, float) + ci["lam_b"] * np.asarray(uj, float),
                                     uk, C["o"], C["d"])
                if sA is not None and sB is not None:
                    S_req = max(sA, sB) if a["adv"] > 0 else min(sA, sB)
        res = abs(lim_new - S_req) if math.isfinite(S_req) else float("nan")
        F4.append({"lbl": lbl, "side": side, "j": j, "i": i, "lim_old": lim_old,
                   "lim_new": lim_new, "S_req": S_req, "res": res, "ci": ci, "adv": a["adv"]})
        # 🔴 **雙框並量**（CC 自補·⛔ 施工單未令）：`VR-043` 二之 `[0.2677, 7.4487]` 係何框？
        #    框甲 ＝ FRONTLINE 框（`w40.s_of(pt, o, d̂)`·＝ `S_req`／`下限` 之框）
        #    框乙 ＝ 帶軸框（`analyse_cell` 之 `s_of(p) = ⟨p−corner_pt, m̂⟩ / denom`）
        m_hat, denom = strip_axis(C["rec"]["d_hat"], C["rec"]["alloc"])
        m_hat = np.asarray(m_hat, float)[:2]
        bp0 = np.asarray(C["rec"]["corner_pt"], float)[:2]
        sv = [float(np.dot(np.asarray(c, float)[:2] - bp0, m_hat)) / denom
              for c in list(C["rec"]["biz"][j].exterior.coords)]
        F4[-1]["strip_lo"], F4[-1]["strip_hi"] = min(sv), max(sv)
        P("  %-5s %-6s %-4d %13.4f %13.4f %13.4f %13s %11.3e  框乙[%.4f,%.4f]"
          % (lbl, side, j, lim_old, lim_new, S_req,
             "[%.3f,%.3f]" % (pv["s_lo"], pv["s_hi"]), res, min(sv), max(sv)))
    POP(len(F4), len(F4), "A-4 逐 (格,j)（全列）")
    P("")
    P("  🔴 **雙框對帳（CC 自補·⛔ 施工單未令）**：`VR-043` 二之決定性現查逐字為")
    P("     「`0m R2` 之 `宗0`（`628-41(1)`）之 `s` 域 ＝ **`[0.2677, 7.4487]`**、跨距 `7.1810`」")
    P("     ⇒ 本檔逐格出艙**二框**之 `宗j` `s` 域，以定該引用係何框：")
    P("  %-5s %-6s %-4s %-26s %-26s %-14s"
      % ("街廓", "側", "j", "框甲 FRONTLINE 框", "框乙 帶軸框", "何框 ≈ [0.2677,7.4487]?"))
    for x in F4:
        C2 = CELL[x["lbl"]]
        pv2 = C2["lots"][x["j"]]
        a_lo, a_hi = pv2["s_lo"], pv2["s_hi"]
        b_lo, b_hi = x.get("strip_lo", float("nan")), x.get("strip_hi", float("nan"))
        hitf = []
        for nm, lo, hi in (("甲", a_lo, a_hi), ("乙", b_lo, b_hi)):
            if math.isfinite(lo) and abs(lo - 0.2677) < 5e-4 and abs(hi - 7.4487) < 5e-4:
                hitf.append(nm)
        P("  %-5s %-6s %-4d %-26s %-26s %-14s"
          % (x["lbl"], x["side"], x["j"], "[%.4f, %.4f]" % (a_lo, a_hi),
             "[%.4f, %.4f]" % (b_lo, b_hi), (hitf or "—")))
    POP(len(F4), len(F4), "A-4 雙框對帳（全列）")
    P("  🔒 **本表只出艙<u>何框相符</u>**——⛔ 不判 `VR-043` 二之引用是否有誤"
      "（🔒 若二框皆不符，則該引用之出處須另查·具名為未答）。")
    P("")
    P("  🔴 **二框之關係（逐格·⛔ 純量測）**：以 `宗j` 之 `s` 域二端點求其**仿射比**"
      "（`跨距乙 / 跨距甲`）——若恆為 1 則二框只差平移；否則另有**尺度**（`denom`）")
    P("  %-5s %-6s %-4s %12s %12s %10s %14s %14s"
      % ("街廓", "側", "j", "跨距甲", "跨距乙", "比", "框甲(X_exit)", "框乙(X_exit)"))
    for x in F4:
        C2 = CELL[x["lbl"]]
        pv2 = C2["lots"][x["j"]]
        sp_a = pv2["s_hi"] - pv2["s_lo"]
        sp_b = x.get("strip_hi", float("nan")) - x.get("strip_lo", float("nan"))
        ratio = (sp_b / sp_a) if sp_a else float("nan")
        # `X_exit` ＝ 弦之出口端（＝ `宗j` 遠側界離開街廓之點）
        ga = gb = float("nan")
        if x["ci"] is not None:
            pj2, uj2 = w82.pj_of(C2["rec"], x["j"]), w82.uj_of(C2["rec"], x["j"])
            if pj2 is not None and uj2 is not None:
                lam = x["ci"]["lam_b"] if x["adv"] > 0 else x["ci"]["lam_a"]
                Xe = np.asarray(pj2, float) + lam * np.asarray(uj2, float)
                ga = w40.s_of(tuple(Xe), C2["o"], C2["d"])
                m2, dn2 = strip_axis(C2["rec"]["d_hat"], C2["rec"]["alloc"])
                m2 = np.asarray(m2, float)[:2]
                bp2 = np.asarray(C2["rec"]["corner_pt"], float)[:2]
                gb = float(np.dot(Xe - bp2, m2)) / dn2
        P("  %-5s %-6s %-4d %12.4f %12.4f %10.4f %14.4f %14.4f"
          % (x["lbl"], x["side"], x["j"], sp_a, sp_b, ratio, ga, gb))
    POP(len(F4), len(F4), "A-4 二框關係（全列）")
    P("  🔒 **⇒ 二框之比若 ≠ 1，則「某值 ＝ 某值」之比對<u>須先聲明框</u>**（本批 §I 之受詞）。")

    have = [x for x in F4 if math.isfinite(x["res"])]
    good = [x for x in have if x["res"] <= 1e-6 * max(1.0, abs(x["S_req"]))]
    P("  🔒 **母體之界定（⛔ 不得以 `len(F4)` 為分母）**：`S_req` 需 `k = j+2` 之對方能定義；"
      "**有 `S_req` 者 ＝ %d ／ %d**（其餘 %d 格之 `j` 為該組**末二宗**⇒ 無 `d≥2` 之對·逐格已具名）"
      % (len(have), len(F4), len(F4) - len(have)))
    P("  🔒 **`P5` 上半之判（受詞 ＝ 有 `S_req` 者）**：相對差 ≤ 1e-6 者 ＝ **%d ／ %d** ⇒ %s"
      % (len(good), len(have),
         "✅ **`P5` 上半成立**" if (have and len(good) == len(have)) else "🔴 **有不合者·具名**"))
    for x in F4:
        if math.isfinite(x["res"]):
            P("     %-4s %-6s j=%-3d 殘差 %.3e·**殘差/ulp ＝ %.2f**（`ulp(%.4f)=%.3e`）"
              % (x["lbl"], x["side"], x["j"], x["res"],
                 w82._ulp_ratio(x["res"], x["S_req"]) if x["S_req"] else float("nan"),
                 x["S_req"], math.ulp(abs(x["S_req"])) if x["S_req"] else float("nan")))

    # 弦區間閉式重跑（正對照 ＝ 新錨；負對照 ＝ 原錨）
    P("")
    P("  🔴 **弦區間閉式重跑**（🔒 正對照 ＝ **新錨**／負對照 ＝ **原錨**·⛔ 同源可比）")

    def overlap_at(C, j, ci, s_target):
        """把 `宗(j+1)` 遠側界及其後各近側界沿 `d̂` 平移至 `s_target`，回破量對數。

        🔒 `s_target is None` ⇒ **現況**（`delta = 0`·⛔ 不平移）。
        """
        rk = next((x for x in C["rows"] if x.get("ok") and x["j"] == j and x["k"] == j + 2), None)
        if rk is None or ci is None:
            return -1
        r_k = (C["rec"]["ress"] or [None] * (j + 3))[j + 2]
        nf = w81.faces_of(w81.SOLVE.get(id(r_k)))[0]
        if nf is None:
            return -1
        pk = np.asarray(nf[1], float)[:2]
        s_cur = s_front_of_line(pk, _u(rk["uk"]), C["o"], C["d"])
        if s_cur is None:
            return -1
        delta = 0.0 if s_target is None else (s_target - s_cur)
        pj2, uj2 = w82.pj_of(C["rec"], j), w82.uj_of(C["rec"], j)
        n2 = 0
        for x in C["rows"]:
            if not (x.get("ok") and x["j"] == j and x["d"] >= D_MIN):
                continue
            r_k2 = (C["rec"]["ress"] or [None] * (x["k"] + 1))[x["k"]]
            nf2 = w81.faces_of(w81.SOLVE.get(id(r_k2)))[0]
            if nf2 is None:
                continue
            pk2 = np.asarray(nf2[1], float)[:2] + delta * np.asarray(C["d"], float)
            uk2 = _u(x["uk"])
            sa = float(np.asarray(uj2)[0] * uk2[1] - np.asarray(uj2)[1] * uk2[0])
            if abs(sa) < 1e-15:
                continue
            dv = pk2 - np.asarray(pj2, float)
            if w82.pred_chord(ci, float(dv[0] * uk2[1] - dv[1] * uk2[0]) / sa):
                n2 += 1
        return n2

    P("  %-5s %-6s %-4s %-14s %-16s %-16s %-10s"
      % ("街廓", "側", "j", "現況破量對", "**新錨(+ε) 後**", "原錨 後（負對照）", "判"))
    ok_new, ok_old = 0, 0
    n_f4 = 0
    for x in F4:
        C = CELL[x["lbl"]]
        eps = EPS_SHIM * (1.0 if x["adv"] > 0 else -1.0)
        n_now = overlap_at(C, x["j"], x["ci"], None)
        n_new = overlap_at(C, x["j"], x["ci"], x["lim_new"] + eps)
        n_old = overlap_at(C, x["j"], x["ci"], x["lim_old"])
        if n_now < 0:
            P("  %-5s %-6s %-4d %-14s %-16s %-16s %-10s"
              % (x["lbl"], x["side"], x["j"], "—", "—", "—",
                 "⛔ **無 `k=j+2` 之對**（⇒ 該 `j` 無 `d≥2` 之弦約束·`S_req` 未定義）"))
            continue
        n_f4 += 1
        ok_new += int(n_new == 0)
        ok_old += int(n_old > 0)
        P("  %-5s %-6s %-4d %-14s %-16s %-16s %-10s"
          % (x["lbl"], x["side"], x["j"], "%d 對" % n_now, "**%d 對**" % n_new,
             "%d 對" % n_old,
             "✅" if (n_new == 0 and n_old > 0) else
             ("⚠️ 現況本即 0" if n_now == 0 else "🔴 **具名**")))
    POP(len(F4), n_f4, "A-4 弦區間重跑（僅列有 `k=j+2` 之對者）")
    brk5 = [x for x in F4 if x.get("_n_now", 0) > 0]
    P("  🔒 **`P5` 下半之判（受詞 ＝ 有 `d≥2` 之對者 %d 格）**：新錨後重疊 ＝ 0 者 **%d ／ %d**；"
      "**負對照**（原錨）重疊 > 0 者 **%d ／ %d** ⇒ %s"
      % (n_f4, ok_new, n_f4, ok_old, n_f4,
         "✅ **`P5` 下半成立**（二者不同 ⇒ 錨點有判別力）" if (n_f4 and ok_new == n_f4 and ok_old > 0)
         else "🔴 **具名**（⛔ 若二者同為 0 或同為 >0 ⇒ 錨點無判別力）"))

    # ══ 【G／P7】第十一法 ═══════════════════════════════════════════
    P("")
    P("【G／P7】`run_all` 清單筆數之**第十一法**（🔒 執行輸出側對帳法·⛔ 與十法不同族）")
    P("-" * W)
    rows11, dated11 = run_all_count_method11()
    P("  母體 ＝ 倉內既存之 `run_all` **執行 log**（檔名含 `runall`／`run_all`），"
      "受詞 ＝ 其「末端夾具 …」行之計數")
    P("  🔒 **序之來源 ＝ git `rev-list --count <sha>..HEAD`**（⛔ 非 `mtime`——checkout 會全部改寫）")
    P("  %-52s %-10s %-12s %-8s" % ("log", "夾具行數", "commit", "距 HEAD"))
    for r in dated11[:14]:
        P("  %-52s %-10d %-12s %-8s" % (r["fn"][:52], r["n"], r["sha"], r["dist"]))
    POP(len(rows11), min(14, len(dated11)), "第十一法之候選 log（依 commit 序·僅列最近 14）")
    P("  🔒 **不可定 commit 序者 ＝ %d 支**（檔名無 sha·⛔ 不計入結論）"
      % (len(rows11) - len(dated11)))
    ans11 = dated11[-1]["n"] if dated11 else -1
    P("  ⇒ **第十一法所得（最接近 `HEAD` 之 log）＝ %d**"
      "（log ＝ `%s`·距 HEAD %s commit）（施工單 `P7` 期望 **15**）⇒ %s"
      % (ans11, dated11[-1]["fn"] if dated11 else "—",
         dated11[-1]["dist"] if dated11 else "—",
         "✅ 相符" if ans11 == 15 else "🔴 **不符·⛔ 不調整預測·具名**"))
    ser = [(r["dist"], r["n"]) for r in dated11]
    P("  🔒 **本法獨有之可見物**：清單筆數之**執行側時間序** ＝ %s"
      % sorted(set(n for _d, n in ser)))
    P("  ⚠️ 🔒 **失效模式**：log 係**過去**之執行 ⇒ 若清單自最後一次執行後又變動，本法會**落後**"
      "⇒ 🔒 **只能作為第 11 支、⛔ 不得單獨採信**。")

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
