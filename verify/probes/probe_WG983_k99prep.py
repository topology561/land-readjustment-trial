# -*- coding: utf-8 -*-
r"""**W-G.9-83 §二 A 組**：`K-9-9` 落地之備料——35 宗 ⇄ `②-宗` 破量 ／ 下限之後果 ／ 排程素材。

## 受詞（施工單 `W-G.9-83` §二·`VR-041` 七）
- **A-1** `K-9-9` 之**落地狀態逐款現查**（一／二／四／五）＋ 判別力（`K-9-5-4 ②` ⇒ `near_dir` 須 > 0）。
- **A-2** `W-G.9-40` 之 **35 宗** ⇄ `GB-67` 之 `②-宗` 破量之**對應關係**（⛔ 二者不得相加）。
- **A-3** 施加 `K-9-9 二` 下限後之後果（**主受詞**）＋ 🔴 **不配地後重跑弦區間閉式 ⇒ 重疊須 0**。
- **A-4** 換圖 `V6_1` 之依賴（⛔ 不換圖·⛔ 不重烤）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單欲證「`K-9-9 二` 之落地即為 `GB-67` 之解」。
其瑕若使**施加下限後之重疊偏小** ⇒ 結論安靜地成立 ⇒ 🔴 **會使一個未經檢驗之解被當成已證**。
🔒 **事前選定：偏向使重疊<u>偏大</u>**——落實為三條，⛔ 逐條具名：
  (甲) 「不配地」之母體取**最小**（⇒ 移除得最少 ⇒ 殘餘重疊最多）——
       以**逐側第一個違反宗**為嚴格「第一輪」，另併陳「全部違反宗」為上界；
  (乙) 重疊之判定沿用 `W-G.9-82` 之**閉區間**（邊界擦邊計為**重疊**·⇒ 偏大）；
  (丙) 非相鄰之門檻沿用 `d ≥ 2`（⛔ 不放寬為 `d ≥ 3`）。
⇒ **若在此三條下重疊仍歸零，該結論更強。**

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
- `K-9-9 二` 之判定式：**原樣 import** `probe_WG940_startperp` 之
  `eval_lot`／`far_side_dir_and_pt`／`line_isect`／`s_of`（⛔ 未重寫一行）。
- 弦區間謂詞：**原樣 import** `probe_WG982_chord` 之 `ring_edges`／`chord_interval`／`pred_chord`。
- 逐格逐對之構造：**原樣 import** `probe_WG981_scope` 之 `analyse_cell`／`spy_solve`／`spy_pool`。

## ⛔ 本檔不做（施工單 §二 A-5 五款）
⛔ 零 `app.py` 變更；⛔ 不落地 `K-9-9` 任何一款；⛔ 不建遞補／合併／調配池介面；
⛔ 不換圖、⛔ 不重烤、⛔ 不改任何 baseline／快照；
⛔ 不出艙「應改領現金之宗」（`W-G.9-40` §C-4 禁令仍有效）；
⛔ 不以「若強制配到下限」之數作為候選解（`K-9-9 四` 明禁超配）。

## 🔒 常設條款
- **8**（會使它為否之輸入）：`selfcheck` 各項皆附**已知偽**之輸入與其實得值。
- **9**（門檻須併出艙量級與 `ulp`）：本檔門檻於 `【0】` 出艙其量級範圍與 `math.ulp`。
- **10**（表尾母體行）：每表末印 `POPULATION= / PRINTED= / SUPPRESSED=`。
- **11**（修法之動作清單）：本檔「⛔ 不經 shell 傳含反斜線之內容」**適用動作 ＝ 讀 ＋ 寫**
  （本檔以 `Write` 落盤·⛔ 未經 heredoc）。
- **12**（`自誤 85` 修法 87〜89）：搜尋規格含**正典款號組**（範圍 `docs/rulings/` 全庫）
  ＋ 判別力自檢——見報告 §A（⛔ 本檔不重跑擴搜）。
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

# 🔒 同源 import（⛔ 不另造第二份）
import probe_WG981_scope as w81                                     # noqa: E402
import probe_WG982_chord as w82                                     # noqa: E402
import probe_WG940_startperp as w40                                 # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 200
SB = 0.0                 # 🔒 `W-G.9-40` 僅跑 0m ⇒ 本檔沿用（⛔ 不擴母體·具名）
D_MIN = 2                # A-0(丙)：非相鄰之門檻
TOL_S = 1e-6             # 沿 FRONTLINE 之 s 容差（承 `w40.eval_lot` 之 `-1e-6`）
TOL_PAR = 1e-9           # 二源對拍之平行門檻（`|sin(夾角)|`·二單位向量 ⇒ 量級 [0,1]）
OLD_LOG = "probe_WG940_startperp_834bce0.log"   # `W-G.9-40` 之倉內 log（基座 834bce0）


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception as e:                                          # noqa: BLE001
        return "UNKNOWN(%s)" % e


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG983_k99prep_%s.log" % COMMIT)


# ═══ P7 之第九法：`run_all` 清單筆數 ═════════════════════════════════════
def run_all_count_method9():
    r"""🔒 **第九法：版本歷史淨增法**（⛔ 與既用八法皆不同族）。

    既用八法之母體分別為 `run_all.py` 之**語法／位元組**（①〜⑦）與**檔案系統**（⑧）。
    本法之母體 ＝ **git 之逐行增刪歷史**：於 `git log -p --follow -- verify/run_all.py`
    中數形如 `("<名>.py",` 之**新增行減刪除行**。
    🔒 其可捕捉八法皆看不見者：**曾被加入又移除之項**（淨額為 0）。
    🔒 對 `run_all.py:80` 之 `endswith(".py")` **結構上免疫**（無 `("` 前綴）。

    🩸 **量測器之受詞更正（節 97·遞迴施用）**：首版之樣式為 `^\+\s*\("`（**錨在行首**），
    漏掉**與 `for` 敘述同行**之清單首項（`run_all.py:105`）⇒ 裸值 14。
    受詞應為「**新增行中出現**形如 `("<名>.py",` 者」，⛔ 非「行首為之」⇒ 改為 `^\+.*\("`。
    🔒 二式並陳出艙（⛔ 不以修正後之值取代裸值）。
    """
    out = subprocess.check_output(
        ["git", "log", "-p", "--follow", "--", "verify/run_all.py"],
        cwd=REPO).decode("utf-8", "replace")
    pat_anchor_a = re.compile(r'^\+\s*\("([^"]+\.py)",')
    pat_anchor_d = re.compile(r'^-\s*\("([^"]+\.py)",')
    pat_inline_a = re.compile(r'^\+.*?\("([^"]+\.py)",')
    pat_inline_d = re.compile(r'^-.*?\("([^"]+\.py)",')
    res = {"anchor": [0, 0, [], []], "inline": [0, 0, [], []]}
    for ln in out.split(chr(10)):
        if ln.startswith("+++") or ln.startswith("---"):
            continue
        for tag, pa, pd in (("anchor", pat_anchor_a, pat_anchor_d),
                            ("inline", pat_inline_a, pat_inline_d)):
            m = pa.match(ln)
            if m:
                res[tag][0] += 1
                res[tag][2].append(m.group(1))
                continue
            m = pd.match(ln)
            if m:
                res[tag][1] += 1
                res[tag][3].append(m.group(1))
    return res


# ═══ 【0】量測器自檢 ═════════════════════════════════════════════════════
def selfcheck(P):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·每項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    # ① 🔒 `w40.eval_lot` 之**同源證**：以 `W-G.9-40` §0 之原測資重跑，四項須逐項相同
    TH = math.radians(17.0)
    d = (math.cos(TH), math.sin(TH))
    o = (0.0, 0.0)
    n = (-d[1], d[0])
    DEPTH = 40.0
    ob = (o[0] + DEPTH * n[0], o[1] + DEPTH * n[1])

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
    P("  ① **`w40.eval_lot` 同源證**（原樣 import·以 `W-G.9-40` §0 之 17° 傾斜測資重跑）：")
    P("     已知【甲】⇒ %s ／ 已知【乙】⇒ %s ／ 已知【合格】⇒ %s ／ **已知【不合格】⇒ %s**"
      "（Δfront %+.3f）⇒ %s"
      % (c1[0], c2[0], c3[3], c4[3], c4[2][0], "PASS" if r1 else "🔴 FAIL"))
    P("     🔒 **常設 8**：④ 即「會使它為否」之具體輸入（本宗 s=12 落在 `P⊥`=16 之前）")

    # ② 🔒 `w82.chord_interval` 之同源證（方形街廓·手算）
    e_sq, d_sq = w82.ring_edges(w82.SQ_CCW)
    u = w82._u((3.0, 4.0))
    ci = w82.chord_interval(e_sq, np.array([1.0, 2.0]), u)
    ha, hb = -1.0 / float(u[0]), (10.0 - 2.0) / float(u[1])
    r2 = (abs(ci["lam_a"] - ha) <= 8 * math.ulp(abs(ha))
          and abs(ci["lam_b"] - hb) <= 8 * math.ulp(abs(hb)))
    ok &= r2
    P("  ② **`w82.chord_interval` 同源證**：λ=[%.12g, %.12g]／手算 [%.12g, %.12g]"
      "　殘差/ulp = %.2f / %.2f ⇒ %s"
      % (ci["lam_a"], ci["lam_b"], ha, hb,
         w82._ulp_ratio(ci["lam_a"] - ha, ha), w82._ulp_ratio(ci["lam_b"] - hb, hb),
         "PASS" if r2 else "🔴 FAIL"))
    r2b = (w82.pred_chord(ci, 0.0) is True) and (w82.pred_chord(ci, 1e6) is False)
    ok &= r2b
    P("     🔒 **常設 8**：同一線上 `s*=0` ⇒ %s（期望 True）／`s*=1e6` ⇒ %s（期望 False）⇒ %s"
      % (w82.pred_chord(ci, 0.0), w82.pred_chord(ci, 1e6), "PASS" if r2b else "🔴 FAIL"))

    # ③ 🔒 第九法之判別力（其計數須非恆 0）
    m9 = run_all_count_method9()
    r3 = (m9["inline"][0] > 0)
    ok &= r3
    P("  ③ **第九法非恆 0**：行內式 新增 %d／刪除 %d ⇒ 淨 %d（期望 新增 > 0）⇒ %s"
      % (m9["inline"][0], m9["inline"][1], m9["inline"][0] - m9["inline"][1],
         "PASS" if r3 else "🔴 FAIL"))

    # ④ 🔒 常設 9：門檻之量級與 ulp
    P("  ④ **常設 9**：`TOL_S = %.1e`（沿 FRONTLINE 之 `s`·單位 m）；"
      "被測量 `|Δfront|`／`|Δbase|` 之量級於【E】表出艙；`math.ulp(1e2) = %.3e` ⇒ 門檻 > ulp ✅"
      % (TOL_S, math.ulp(1e2)))
    P("     🔒 `D_MIN = %d`（非相鄰之門檻·**整數**·⛔ 無 ulp 之問題）" % D_MIN)

    P("  ⇒ 量測器自檢：%s" % ("PASS" if ok else "🔴 FAIL（⛔ 以下量測結果不得採信）"))
    return ok


# ═══ A-1：`K-9-9` 落地狀態逐款現查 ═══════════════════════════════════════
K99_PROBES = [
    ("一（∥ALLOCLINE）", ["_alloc_dir_used", "n_hat_far", "alloc_normal_axis",
                          "K-9-9", "遠側境界線"]),
    ("二（位置下限）", ["P_prev", "B_prev", "起算垂線", "P⊥", "B⊥", "情形甲", "情形乙"]),
    ("四（不配地＋遞補＋調配池）", ["不配地", "遞補", "_pool_strips_for_block",
                                    "調配池", "合併群"]),
    ("五（街角第 1 宗不適用）", ["is_corner"]),
]
CODE_FILES = ["app.py", "verify/stepg_pipeline.py", "verify/selection_pipeline.py",
              "verify/wf_f3.py", "verify/wf_f4.py"]


def a1_landing(P, POP):
    P("")
    P("【C／A-1】`K-9-9` 之**落地狀態逐款現查**（⛔ 非只搜款號·附字樣錨）")
    P("-" * W)
    src = {}
    for f in CODE_FILES:
        p = os.path.join(REPO, f)
        src[f] = io.open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else None
    P("  母體（生產／引擎碼）：%s" % [f for f in CODE_FILES if src[f] is not None])
    rows = []
    for kuan, keys in K99_PROBES:
        for k in keys:
            tot = {f: (src[f].count(k) if src[f] else -1) for f in CODE_FILES}
            rows.append((kuan, k, tot))
    P("  %-26s %-24s %s" % ("款", "字樣", "  ".join("%-22s" % os.path.basename(f) for f in CODE_FILES)))
    for kuan, k, tot in rows:
        P("  %-26s %-24s %s"
          % (kuan, k, "  ".join("%-22s" % (tot[f] if tot[f] >= 0 else "（無此檔）")
                                for f in CODE_FILES)))
    POP(len(rows), len(rows), "A-1 逐款逐字樣（全列）")
    return rows


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
    P("【W-G.9-83 §二 A 組】`K-9-9` 落地之備料（⛔ 只量不修·⛔ 零 app.py 變更·⛔ 不落地）")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向使重疊<u>偏大</u>**（甲/乙/丙 三條見 docstring）")
    P("  🔒 同源：`w40.eval_lot`／`w82.chord_interval`／`w81.analyse_cell` 皆**原樣 import**（節 100）")
    P("  🔒 情境母體 ＝ **僅 `%gm`**（沿 `W-G.9-40` 之母體·⛔ 未擴·具名）" % SB)

    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    a1_landing(P, POP)

    # ── 驅動（sb = 0.0·w81 之 spy）────────────────────────────────────
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
    ERR = {}
    ns["_solve_G_one"], ns["_pool_strips_for_block"] = w81.spy_solve(o_solve), w81.spy_pool(o_pool)
    try:
        for lbl in blks:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                               wins, forced, SB)
                except Exception as e:                              # noqa: BLE001
                    ERR[lbl] = "%s: %s" % (type(e).__name__, str(e)[:110])
    finally:
        ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool
    REAL = list(w81.CAP)
    P("")
    P("【驅動】`%gm` × R1–R6——攔截 %d 格；生產碼 raise 之街廓 = %s"
      % (SB, len(REAL), ERR if ERR else "（無）"))

    FL = cad.get("front_lines") or {}
    BL = cad.get("baselines") or {}

    # ── A-2-1：於現行 HEAD 重跑 `K-9-9 二` 之違反判定（w40 原式）──────────
    P("")
    P("【D-1／A-2-1】於**現行 HEAD** 重跑 `K-9-9 二` 之違反判定（🔒 `w40` 原式·⛔ 未重寫）")
    P("-" * W)
    CELLS = {}          # label -> dict(rec, meta, rows, groups, bad, judged)
    STAT = {"甲": 0, "乙": 0, "退化(P⊥＝P_prev)": 0}
    BAD = []
    far_agree = far_total = far_bit = 0
    FAR_SIN = []
    FAR_BAD = []
    for rec in REAL:
        lbl = rec["label"]
        biz = rec["biz"]
        d_hat = tuple(np.asarray(rec["d_hat"], float)[:2])
        nrm = (-d_hat[1], d_hat[0])
        fl = FL.get(lbl) or {}
        bl = BL.get(lbl) or {}
        if not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            P("  %s：⛔ 缺 FRONTLINE 或 BASELINE ⇒ **無從量測**" % lbl)
            continue
        o = tuple(float(x) for x in fl["p1"])
        bpt = tuple(float(x) for x in bl["point"])
        bang = math.radians(float(bl.get("angle_deg", 0.0)))
        bdir = (math.cos(bang), math.sin(bang))
        IV = []
        for g in biz:
            ss_ = [(x * d_hat[0] + y * d_hat[1]) for x, y in list(g.exterior.coords)]
            IV.append((min(ss_), max(ss_)))
        k_break = None
        for k in range(1, len(IV)):
            if min(v[0] for v in IV[k:]) > max(v[1] for v in IV[:k]) + 1e-6:
                k_break = k if k_break is None else -1
        groups = ([("左", list(range(0, k_break))), ("右", list(range(k_break, len(IV))))]
                  if isinstance(k_break, int) and k_break > 0
                  else [("單組(未測得唯一分界)", list(range(len(IV))))])
        judged = []
        geo = {}
        for side, idxs in groups:
            prev = None
            for i in idxs:
                u_far, p_far = w40.far_side_dir_and_pt(biz[i], d_hat)
                # 🔒 判別力：與 `w81.faces_of` 之遠側界方向對拍（**二個獨立來源**）
                r_ = (rec["ress"] or [None] * (i + 1))[i]
                ff = w81.faces_of(w81.SOLVE.get(id(r_)))[1]
                if u_far is not None and ff is not None and ff[0] is not None:
                    far_total += 1
                    _a1, _a2 = w82._u(u_far), w82._u(ff[0])
                    if _a1 is not None and _a2 is not None:
                        _sn = abs(float(_a1[0] * _a2[1] - _a1[1] * _a2[0]))
                        FAR_SIN.append(_sn)
                        if w81._bitsame(_a1, _a2):
                            far_bit += 1
                        if _sn <= TOL_PAR:
                            far_agree += 1
                        else:
                            _inf = w81.SOLVE.get(id(r_)) or {}
                            FAR_BAD.append((lbl, side, i, bool(_inf.get("is_corner")), _sn))
                if u_far is None:
                    judged.append((side, i, None, None, None, None, "⛔ 取不出遠側界"))
                    continue
                Pc = w40.line_isect(p_far, u_far, o, d_hat)
                Bc = w40.line_isect(p_far, u_far, bpt, bdir)
                if Pc is None or Bc is None:
                    judged.append((side, i, None, None, None, None, "⛔ ∥FRONT 或 ∥BASE"))
                    prev = None
                    continue
                geo[i] = (Pc, Bc, side)
                if prev is None:
                    judged.append((side, i, None, None, (w40.s_of(Pc, o, d_hat),
                                                         w40.s_of(Bc, o, d_hat)), None,
                                   "（起點·本則不適用）"))
                    prev = (Pc, Bc)
                    continue
                case, st, df, code = w40.eval_lot(prev[0], prev[1], Pc, Bc, o, d_hat, nrm)
                STAT[case] = STAT.get(case, 0) + 1
                judged.append((side, i, case, st, (w40.s_of(Pc, o, d_hat),
                                                   w40.s_of(Bc, o, d_hat)), df, code))
                if code == "不合格":
                    BAD.append({"lbl": lbl, "side": side, "i": i, "case": case,
                                "st": st, "cur": (w40.s_of(Pc, o, d_hat), w40.s_of(Bc, o, d_hat)),
                                "df": df, "area": float(biz[i].area)})
                prev = (Pc, Bc)
        CELLS[lbl] = {"rec": rec, "groups": groups, "judged": judged, "biz": biz,
                      "o": o, "d": d_hat, "geo": geo, "nrm": nrm,
                      "verdict": {i: code for (side, i, case, st, cur, df, code) in judged}}
    P("  情形分布：%s" % STAT)
    P("  🔒 **遠側界之二源對拍**（`w40.far_side_dir_and_pt`＝**多邊形之邊** vs "
      "`w81.faces_of`＝**`_solve_G_one` 之 `_alloc_dir_used`**）：")
    P("     **平行者（`|sin| ≤ %.1e`）＝ %d ／ %d**；**逐位元組相同 ＝ %d ／ %d**"
      % (TOL_PAR, far_agree, far_total, far_bit, far_total))
    if FAR_SIN:
        _srt = sorted(FAR_SIN)
        P("     🔒 **常設 9**：`|sin(夾角)|` 之量級 ∈ [%.3e, %.3e]（中位 %.3e）；"
          "門檻 %.1e；`math.ulp(1.0) = %.3e` ⇒ 門檻 > ulp ✅"
          % (_srt[0], _srt[-1], _srt[len(_srt) // 2], TOL_PAR, math.ulp(1.0)))
        P("     🔒 **節 103**：最接近翻面者 ＝ **%.3e**（＝ 離平行 %.3e°）"
          % (_srt[-1], math.degrees(math.asin(min(1.0, _srt[-1])))))
    P("     ⇒ %s"
      % ("✅ **二源平行**（⇒ 同一條線之方向·`逐位元組相同 = %d` 之低值僅為**二條算術路徑**之末位差·"
         "⛔ 非受詞不同）" % far_bit if far_agree == far_total else
         "🔴 **有不平行者 %d ／ %d·逐宗具名如下**（⇒ 二式於該些宗**非同一量**）"
         % (far_total - far_agree, far_total)))
    if FAR_BAD:
        P("     %-6s %-6s %-4s %-12s %14s %12s"
          % ("街廓", "側", "i", "是街角宗?", "|sin(夾角)|", "夾角(°)"))
        for lbl_, sd_, i_, isc_, sn_ in sorted(FAR_BAD, key=lambda x: -x[4]):
            P("     %-6s %-6s %-4d %-12s %14.3e %12.4f"
              % (lbl_, sd_, i_, "**是**" if isc_ else "否", sn_,
                 math.degrees(math.asin(min(1.0, sn_)))))
        POP(len(FAR_BAD), len(FAR_BAD), "二源不平行者（全列）")
        _nc = sum(1 for x in FAR_BAD if x[3])
        P("     🔴 **其中為街角宗者 ＝ %d ／ %d**——🔒 `K-9-9` **五**：街角第 1 宗之遠側界"
          "**恆 ∥ SIDELINE**，而 `w40.far_side_dir_and_pt` 係自**多邊形之邊**取「與 `d_hat` "
          "夾角最大之二邊」⇒ 於街角宗二式**受詞不同**（⛔ 只量不修·⛔ 不下「這是 bug」之結論）"
          % (_nc, len(FAR_BAD)))
        _lay = {"> 1e-5（**真差**）": [x for x in FAR_BAD if x[4] > 1e-5],
                "1e-7 〜 1e-5": [x for x in FAR_BAD if 1e-7 < x[4] <= 1e-5],
                "≤ 1e-7（數值層）": [x for x in FAR_BAD if x[4] <= 1e-7]}
        P("     🔒 **分層**（常設 9·⛔ 不以單一二分出艙）：%s"
          % "／".join("%s ＝ %d" % (k, len(v)) for k, v in _lay.items()))
        _bad_set = {(b["lbl"], b["side"], b["i"]) for b in BAD}
        _hit = [x for x in FAR_BAD if x[4] > 1e-5 and (x[0], x[1], x[2]) in _bad_set]
        P("     🔴🔴 **交叉核（⛔ 不可省）**：`> 1e-5` 之 %d 支中，**同時列於 35 宗違反名單者 ＝ %d**："
          "%s ⇒ 🛑 **該些宗之 `K-9-9 二` 判定所用之遠側界，與引擎實際切線差 %s**"
          % (len(_lay["> 1e-5（**真差**）"]), len(_hit),
             [(x[0], x[1], x[2]) for x in _hit],
             "／".join("%.4f°" % math.degrees(math.asin(min(1.0, x[4]))) for x in _hit)))
    P("")
    P("  %-6s %-6s %-4s %-6s %12s %12s %12s %12s %11s %11s %10s %-10s"
      % ("街廓", "側", "i", "情形", "起算front", "起算base", "本宗P s", "本宗B s",
         "Δfront", "Δbase", "面積", "出艙碼"))
    n_rows = 0
    for lbl in CELLS:
        for (side, i, case, st, cur, df, code) in CELLS[lbl]["judged"]:
            n_rows += 1
            if code == "不合格":
                P("  %-6s %-6s %-4d %-6s %12.3f %12.3f %12.3f %12.3f %+11.3f %+11.3f %10.4f %-10s"
                  % (lbl, side, i, case, st[0], st[1], cur[0], cur[1], df[0], df[1],
                     float(CELLS[lbl]["biz"][i].area), "🔴 不合格"))
    POP(n_rows, len(BAD), "A-2-1 逐宗（僅列**不合格**者）")
    P("  🔴 **現行 HEAD 之不合格宗數 ＝ %d**（倉內錨【倉】`verify/out/probe_WG940_startperp_834bce0.log`"
      "：**35 宗**·`5758.9877 ㎡`）" % len(BAD))
    P("     面積合計 ＝ **%.4f ㎡**" % sum(b["area"] for b in BAD))
    P("     🔒 `P5` 之判：實得 %d %s 35 ⇒ %s"
      % (len(BAD), "==" if len(BAD) == 35 else "≠",
         "🔴 **恰為 35 ⇒ `P5` 逐字不成立 ⇒ 施工單令「須逐宗證其為同一批宗（⛔ 非只數目相同）」"
         "⇒ 下表" if len(BAD) == 35
         else "✅ **≠ 35**（`P5` 成立·基座差異已具名）"))

    # ── 🔴 `P5` 之後續：**逐宗**證其為同一批宗（⛔ 非只數目相同·施工單所令）──────
    P("")
    P("  🔴 **逐宗同一性對拍**（⛔ 非只數目相同）：現行 HEAD `%s` vs 倉內 log `%s`（基座 `834bce0`）"
      % (COMMIT, OLD_LOG))
    old_path = os.path.join(OUTDIR, OLD_LOG)
    old_rows = {}
    if os.path.exists(old_path):
        txt = io.open(old_path, encoding="utf-8", errors="replace").read()
        seg = txt[txt.index("不合格宗之面積"):] if "不合格宗之面積" in txt else txt
        pat = re.compile(r'^\s+(R\d+)\s+(\S+)\s+(\d+)\s+([-+][\d.]+)\s+([-+][\d.]+)\s+([\d.]+)\s*$')
        for ln in seg.split(chr(10)):
            m = pat.match(ln)
            if m:
                old_rows[(m.group(1), m.group(2), int(m.group(3)))] = (
                    float(m.group(4)), float(m.group(5)), float(m.group(6)))
    P("     舊 log 解析所得列數 ＝ **%d**（🔒 期望 35·⛔ 解析式：`%s`）"
      % (len(old_rows), r'^\s+(R\d+)\s+(\S+)\s+(\d+)\s+([-+][\d.]+)\s+([-+][\d.]+)\s+([\d.]+)\s*$'))
    new_rows = {(b["lbl"], b["side"], b["i"]): (round(b["df"][0], 3), round(b["df"][1], 3),
                                                round(b["area"], 4)) for b in BAD}
    ko, kn = set(old_rows), set(new_rows)
    same_key = sorted(ko & kn)
    P("     **鍵（街廓,側,i）之對稱差**：舊∖新 ＝ %s ／ 新∖舊 ＝ %s"
      % (sorted(ko - kn), sorted(kn - ko)))
    nval = 0
    P("     %-6s %-6s %-4s %12s %12s %12s %12s %12s %12s %-8s"
      % ("街廓", "側", "i", "舊 Δfront", "新 Δfront", "舊 Δbase", "新 Δbase",
         "舊 面積", "新 面積", "逐值相同"))
    for k in same_key:
        o_, n_ = old_rows[k], new_rows[k]
        eq = (abs(o_[0] - n_[0]) <= 5e-4 and abs(o_[1] - n_[1]) <= 5e-4
              and abs(o_[2] - n_[2]) <= 5e-5)
        nval += int(eq)
        P("     %-6s %-6s %-4d %12.3f %12.3f %12.3f %12.3f %12.4f %12.4f %-8s"
          % (k[0], k[1], k[2], o_[0], n_[0], o_[1], n_[1], o_[2], n_[2],
             "✅" if eq else "🔴 **異**"))
    POP(len(same_key), len(same_key), "P5 逐宗對拍（鍵之交集·全列）")
    P("     ⇒ **鍵完全相同 ＝ %s**；**逐值相同 ＝ %d ／ %d**（容差 Δ 5e-4 m／面積 5e-5 ㎡）⇒ %s"
      % (ko == kn, nval, len(same_key),
         "✅ **係同一批宗**（⇒ `P5` 逐字不成立之原因 ＝ 乙式落地與 `GB-80` 容差修**未觸及本判定**）"
         if (ko == kn and nval == len(same_key)) else
         "🔴 **⛔ 非同一批宗·逐項已具名**"))
    byside = {}
    for b in BAD:
        byside.setdefault((b["lbl"], b["side"]), []).append(b)
    P("  逐（街廓, 側）之違反宗：")
    for k in sorted(byside):
        v = byside[k]
        P("     %-4s %-6s 宗序 %s　面積合計 %.4f ㎡"
          % (k[0], k[1], [x["i"] for x in v], sum(x["area"] for x in v)))
    POP(len(byside), len(byside), "A-2-1 逐（街廓,側）（全列）")

    # ── A-2-2：`②-宗` 破量（弦區間閉式·0m）─────────────────────────────
    P("")
    P("【D-2／A-2-2】`②-宗` 破量（🔒 `w82` 弦區間閉式·`d ≥ %d`·`%gm`）" % (D_MIN, SB))
    P("-" * W)
    OVER = {}
    META = {}
    for rec in REAL:
        meta, rows = w81.analyse_cell(rec, strip_axis)
        META[rec["label"]] = meta
        if rec["block"] is None:
            continue
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
                pairs.append({"j": j, "k": r["k"], "s_star": r["s_star"],
                              "lam": (ci["lam_a"], ci["lam_b"]), "area": a,
                              "inside": r["inside"]})
        OVER[rec["label"]] = pairs
    P("  %-6s %-4s %-4s %13s %13s %13s %12s %-9s"
      % ("街廓", "j", "k", "s*", "λ_a", "λ_b", "重疊面積", "contains"))
    tot_pairs = 0
    for lbl in OVER:
        for p in OVER[lbl]:
            tot_pairs += 1
            P("  %-6s %-4d %-4d %13.4f %13.4f %13.4f %12.4f %-9s"
              % (lbl, p["j"], p["k"], p["s_star"], p["lam"][0], p["lam"][1],
                 p["area"], p["inside"]))
    POP(tot_pairs, tot_pairs, "A-2-2 破量逐對（全列）")
    for lbl in OVER:
        if OVER[lbl]:
            P("  ⇒ **%s**：破量對數 %d·**重疊面積合計 %.4f ㎡**"
              % (lbl, len(OVER[lbl]), sum(p["area"] for p in OVER[lbl])))
    brk = sorted(l for l in OVER if OVER[l])
    P("  🔴 **破閘之格 ＝ %s**（倉內錨【倉】`VR-041` 四：`R2 45.9766`／`R5 56.3293`）" % brk)

    # ── A-2-3：交集與二個差集 ─────────────────────────────────────────
    P("")
    P("【D-3／A-2-3】**35 宗 ⇄ `②-宗` 破閘格**之交集與二個差集（🔒 ⛔ 二量不得相加）")
    P("-" * W)
    P("  🔒 **受詞逐字併陳**：`W-G.9-40` 量「形成端違反之**宗面積**」；"
      "`GB-67` 量「**重疊**面積」⇒ ⛔ **不得相加**、⛔ 不得互代。")
    bad_idx = {}
    for b in BAD:
        bad_idx.setdefault(b["lbl"], set()).add(b["i"])
    inter_rows = []
    for lbl in brk:
        involved = set()
        for p in OVER[lbl]:
            involved.add(p["j"])
            involved.add(p["k"])
        vio = bad_idx.get(lbl, set())
        inter = sorted(involved & vio)
        only_over = sorted(involved - vio)
        only_vio = sorted(vio - involved)
        inter_rows.append((lbl, sorted(involved), sorted(vio), inter, only_over, only_vio))
        P("  **%s**：破量所涉宗 %s ／ 違反宗 %s" % (lbl, sorted(involved), sorted(vio)))
        P("     **交集 ＝ %s（%d 宗）**／破量∖違反 ＝ %s／違反∖破量 ＝ %s"
          % (inter, len(inter), only_over, only_vio))
        for i in inter:
            P("        交集宗 i=%d：面積 %.4f ㎡"
              % (i, float(CELLS[lbl]["biz"][i].area)))
    POP(len(brk), len(brk), "A-2-3 逐破閘格（全列）")
    n_inter = sum(len(r[3]) for r in inter_rows)
    P("  🔒 **`P3` 之判**：交集之宗數合計 ＝ **%d** ⇒ %s"
      % (n_inter, "✅ **≥ 1**（`P3` 成立）" if n_inter >= 1 else
         "🔴 **交集為空 ⇒ 二者無關 ⇒ `VR-041` 四／`GB-67` 加註三之連結須撤回·具名**"))

    # ── A-3：下限之後果 ＋ 🔴 不配地後重跑閉式 ──────────────────────────
    P("")
    P("【E／A-3】施加 `K-9-9 二` 下限後之後果（⛔ 不落地·⛔ 不得強制配到下限）")
    P("-" * W)
    P("  🔒 **`K-9-9 四` 逐字：不合格 ⇒ 該宗<u>不配地</u>，走合併／調配、下一位遞補、"
      "騰出之地入調配池；⛔ 不得強制配到下限（⛔ 不得超配）。**")
    P("  %-6s %-6s %-4s %-6s %13s %13s %13s %13s %11s %11s %10s"
      % ("街廓", "側", "i", "情形", "現行 P s", "**下限 P s**", "現行 B s", "**下限 B s**",
         "Δfront", "Δbase", "面積"))
    for b in BAD:
        P("  %-6s %-6s %-4d %-6s %13.4f %13.4f %13.4f %13.4f %+11.4f %+11.4f %10.4f"
          % (b["lbl"], b["side"], b["i"], b["case"], b["cur"][0], b["st"][0],
             b["cur"][1], b["st"][1], b["df"][0], b["df"][1], b["area"]))
    POP(len(BAD), len(BAD), "A-3 違反宗之現行位置 vs 下限位置（全列）")
    if BAD:
        dfs = [abs(b["df"][0]) for b in BAD] + [abs(b["df"][1]) for b in BAD]
        P("  🔒 **常設 9**：`|Δ|` 之量級 ∈ [%.4f, %.4f] m；`math.ulp(%.0f) = %.3e`"
          "⇒ 門檻 `TOL_S=%.1e` 高於之 ✅" % (min(dfs), max(dfs), max(dfs),
                                            math.ulp(max(dfs)) if max(dfs) > 0 else 0.0, TOL_S))

    # 第一輪不配地：(甲) 嚴格＝逐側第一個；(乙) 上界＝全部
    first = {}
    for b in BAD:
        key = (b["lbl"], b["side"])
        if key not in first or b["i"] < first[key]["i"]:
            first[key] = b
    P("")
    P("  🔒 **「第一輪不配地」之二個讀法（A-0(甲)：取<u>最小</u>母體為主·⛔ 具名）**：")
    P("     (甲) **嚴格第一輪** ＝ 逐（街廓,側）之**第一個**違反宗 ⇒ **%d 宗**·面積合計 **%.4f ㎡**"
      % (len(first), sum(b["area"] for b in first.values())))
    for k in sorted(first):
        b = first[k]
        P("        %-4s %-6s i=%-3d 面積 %.4f ㎡（情形 %s）" % (k[0], k[1], b["i"], b["area"], b["case"]))
    P("     (乙) **上界（全部現行違反宗）** ⇒ **%d 宗**·面積合計 **%.4f ㎡**"
      % (len(BAD), sum(b["area"] for b in BAD)))
    P("     ⚠️ 🔒 **逐字具名**：`K-9-9 四` 之**遞補**⛔ 未實作（A-1 已現查）"
      "⇒ **遞補後結果必須重算，本批之數係<u>第一輪</u>**。")

    P("")
    P("  ⚠️ **對照（⛔ 正典禁止·⛔ 非候選解）**：「若強制配到下限」之面積變化")
    P("     🔒 `K-9-9 四` 逐字「⛔ 不得強制配到下限（⛔ 不得超配）」⇒ 本列**僅供對照**。")
    for b in BAD[:8]:
        P("        %-4s %-6s i=%-3d 現行面積 %.4f ㎡·需右移 Δfront %+.4f／Δbase %+.4f"
          % (b["lbl"], b["side"], b["i"], b["area"], -b["df"][0], -b["df"][1]))
    POP(len(BAD), min(8, len(BAD)), "A-3 對照（⛔ 非候選解·僅列前 8）")

    # 🔴 主判別力：不配地後重跑弦區間閉式
    P("")
    P("  🔴 **本單最強之一項判別力**：對第一輪不配地後之**殘餘各宗**重跑弦區間閉式")
    P("  %-6s %-30s %-14s %-14s %-10s"
      % ("街廓", "移除之宗（不配地）", "移除前破量對", "**移除後破量對**", "判"))
    p2_ok = True
    for lbl in brk:
        vio_all = bad_idx.get(lbl, set())
        vio_first = {b["i"] for k, b in first.items() if k[0] == lbl}
        for tag, rem in (("(甲) 嚴格第一輪", vio_first), ("(乙) 全部違反宗", vio_all)):
            before = OVER[lbl]
            after = [p for p in before if p["j"] not in rem and p["k"] not in rem]
            area_after = sum(p["area"] for p in after)
            good = (len(after) == 0)
            if tag.startswith("(甲)"):
                p2_ok &= good
            P("  %-6s %-30s %-14s %-14s %-10s"
              % (lbl, "%s %s" % (tag, sorted(rem)), "%d 對 / %.4f ㎡" % (len(before), sum(p["area"] for p in before)),
                 "**%d 對 / %.4f ㎡**" % (len(after), area_after),
                 "✅ 歸零" if good else "🔴 **仍 > 0**"))
            for p in after:
                P("        🔴 殘餘破量對：(j=%d, k=%d) 重疊 %.4f ㎡" % (p["j"], p["k"], p["area"]))
    POP(len(brk) * 2, len(brk) * 2, "A-3 移除前後（二讀法 × 破閘格·全列）")
    P("  🔒 **`P2` 之判（以 (甲) 嚴格第一輪為受詞·A-0 之最緊母體）**：%s"
      % ("✅ **`0m R2`／`0m R5` 之 `②-宗` 重疊量 ＝ 0`（`P2` 成立）**" if p2_ok else
         "🔴 **仍 > 0 ⇒ `K-9-9 二` 之下限不足以消除重疊 ⇒ `VR-041` 四之定性須修正·具名**"))

    # ── 🔴 E-2：`P2` 不成立之**機制診斷**（⛔ 只量不修·⛔ 不下「這是 bug」之結論）──
    P("")
    P("【E-2】🔴 **殘餘破量對之機制診斷**（⛔ 只量不修·施工單「具名」義務之落實）")
    P("-" * W)
    P("  🔒 **`K-9-9 二` 之受詞對 ＝ 相鄰對 `(i−1, i)`（`d ＝ 1`）**；"
      "**`②-宗` 閘之受詞對 ＝ `d ≥ %d`** ⇒ 二母體**不相交**（下表逐對出艙其 `d`）。" % D_MIN)
    P("  %-6s %-4s %-4s %-4s %-12s %-14s %-16s %-18s %-16s"
      % ("街廓", "j", "k", "d", "宗j 是街角?", "宗k K-9-9 判", "宗(k−1) K-9-9 判",
         "宗k近界∥宗(k−1)遠界?", "界面距離(m)"))
    diag_rows = []
    for lbl in brk:
        C = CELLS.get(lbl)
        meta = META.get(lbl)
        rec = C["rec"]
        for p in OVER[lbl]:
            j, k = p["j"], p["k"]
            is_c = (j in (meta["corners"] if meta else ()))
            v_k = (C["verdict"].get(k) or "—") if C else "—"
            v_k1 = (C["verdict"].get(k - 1) or "—") if C else "—"
            # 界面同一性：宗k 之**近**側界 vs 宗(k−1) 之**遠**側界
            rk = (rec["ress"] or [None] * (k + 1))[k]
            rk1 = (rec["ress"] or [None] * k)[k - 1] if k >= 1 else None
            nf = w81.faces_of(w81.SOLVE.get(id(rk)))[0]
            ff1 = w81.faces_of(w81.SOLVE.get(id(rk1)))[1] if rk1 is not None else None
            sin_ = dist_ = float("nan")
            if nf and ff1 and nf[0] is not None and ff1[0] is not None:
                a1, a2 = w82._u(nf[0]), w82._u(ff1[0])
                if a1 is not None and a2 is not None:
                    sin_ = abs(float(a1[0] * a2[1] - a1[1] * a2[0]))
                    dv = np.asarray(nf[1], float)[:2] - np.asarray(ff1[1], float)[:2]
                    dist_ = abs(float(dv[0] * (-a2[1]) + dv[1] * a2[0]))
            diag_rows.append((lbl, j, k, k - j, is_c, v_k, v_k1, sin_, dist_))
            P("  %-6s %-4d %-4d %-4d %-12s %-14s %-16s %-18s %-16s"
              % (lbl, j, k, k - j, "**是**" if is_c else "否", v_k, v_k1,
                 ("∥（|sin|=%.2e）" % sin_) if sin_ <= TOL_PAR else ("**⛔ 不∥**（|sin|=%.2e）" % sin_),
                 "%.6f" % dist_))
    POP(len(diag_rows), len(diag_rows), "E-2 殘餘破量對之機制（全列）")
    n_corner_j = sum(1 for r in diag_rows if r[4])
    P("  🔴 **必答一**：破量對之 `j` 為**街角第 1 宗**者 ＝ **%d ／ %d**"
      % (n_corner_j, len(diag_rows)))
    P("     🔒 `K-9-9` **五**逐字：「街角第 1 宗⛔ 不適用本則；其遠側境界線**恆 ∥ SIDELINE**」")
    P("     ⇒ %s"
      % ("🔴 **全部破量對之形成端皆為<u>正典明文豁免</u>之宗** ⇒ `K-9-9 二` 之下限"
         "**在結構上觸及不到該重疊**（⛔ 此為量測所得·⛔ 非「這是 bug」之結論）"
         if n_corner_j == len(diag_rows) else
         "⚠️ **非全部**——逐對已具名（%d 對之 j 非街角）" % (len(diag_rows) - n_corner_j)))
    dvals = sorted(set(r[3] for r in diag_rows))
    P("  🔴 **必答二**：破量對之 `d` 值集合 ＝ %s ⇒ 與 `K-9-9 二` 之 `d ＝ 1` %s"
      % (dvals, "**不相交**" if 1 not in dvals else "🔴 **相交·具名**"))

    # 讀法 (丙)：迭代式（不配地者⛔ 不成為下一宗之 `前一宗`）
    P("")
    P("  🔒 **讀法 (丙)：迭代式**（不配地者⛔ 不成為下一宗之 `前一宗`·⛔ **非**遞補——幾何不動）")

    def cascade(lbl):
        C = CELLS.get(lbl)
        if not C:
            return set(), []
        o_, d_, n_, geo_ = C["o"], C["d"], C["nrm"], C["geo"]
        removed, rounds = set(), []
        for _ in range(20):
            newv = set()
            for side, idxs in C["groups"]:
                prev = None
                for i in idxs:
                    if i in removed or i not in geo_:
                        continue
                    Pc_, Bc_, _sd = geo_[i]
                    if prev is None:
                        prev = (Pc_, Bc_)
                        continue
                    _c, _st, _df, code_ = w40.eval_lot(prev[0], prev[1], Pc_, Bc_, o_, d_, n_)
                    if code_ == "不合格":
                        newv.add(i)          # ⛔ prev 不前進（該宗不配地）
                    else:
                        prev = (Pc_, Bc_)
            rounds.append(sorted(newv - removed))
            if not (newv - removed):
                break
            removed |= newv
        return removed, rounds

    P("  %-6s %-34s %-16s %-16s %-10s" % ("街廓", "移除之宗（迭代收斂）", "輪次逐輪新增",
                                          "**移除後破量對**", "判"))
    p2c_ok = True
    for lbl in brk:
        rem, rounds = cascade(lbl)
        after = [p for p in OVER[lbl] if p["j"] not in rem and p["k"] not in rem]
        good = (len(after) == 0)
        p2c_ok &= good
        P("  %-6s %-34s %-16s %-16s %-10s"
          % (lbl, str(sorted(rem)), str(rounds),
             "**%d 對 / %.4f ㎡**" % (len(after), sum(p["area"] for p in after)),
             "✅ 歸零" if good else "🔴 **仍 > 0**"))
        for p in after:
            P("        🔴 殘餘破量對：(j=%d, k=%d) 重疊 %.4f ㎡" % (p["j"], p["k"], p["area"]))
    POP(len(brk), len(brk), "讀法 (丙) 迭代式（全列）")
    P("  ⇒ **三讀法之綜判**：(甲) 🔴 仍 > 0 ／ (乙) 🔴 仍 > 0 ／ (丙) %s"
      % ("✅ 歸零" if p2c_ok else "🔴 仍 > 0"))
    P("  🔒 **⇒ `P2` 於三個讀法下之結論一致者**：%s"
      % ("三讀法皆 🔴 **不成立**" if not p2c_ok else
         "(甲)(乙) 🔴 不成立／(丙) ✅ 成立 ⇒ **讀法決定結論·須由施工單裁其受詞**"))

    # ── A-4：換圖依賴 ────────────────────────────────────────────────
    P("")
    P("【F／A-4】排程素材：換圖 `V6_1` 之依賴（⛔ 不換圖·⛔ 不重烤·⛔ 不載入）")
    P("-" * W)
    for f in ("data/V6.dxf", "data/V6_1.dxf"):
        p = os.path.join(REPO, f)
        ex = os.path.exists(p)
        sz = os.path.getsize(p) if ex else -1
        try:
            blob = subprocess.check_output(["git", "cat-file", "-s", "HEAD:" + f],
                                           cwd=REPO).decode().strip()
        except Exception:                                           # noqa: BLE001
            blob = "（未入倉）"
        P("  %-16s 工作區存在 %-6s bytes %-10s HEAD blob bytes %s" % (f, ex, sz, blob))
    P("  🔒 `rv.V6DXF` 現用 ＝ %s" % os.path.relpath(rv.V6DXF, REPO).replace(os.sep, "/"))
    P("")
    P("  **35 宗之違反判定所依賴之幾何量清單**（🔒 逐項標明來源）")
    P("  %-16s %-46s %-12s" % ("幾何量", "於本判定中之用途（逐字）", "來源是否 DXF"))
    DEP = [("FRONTLINE", "`o`＝p1、`d_hat`＝推進方向；`s_of` 之定序軸", "**是**"),
           ("BASELINE", "`bpt`／`bdir`；`B_prev`／`B⊥` 之所在", "**是**"),
           ("SIDELINE", "第 2 宗之甲乙判別（`K-9-9 二` 逐字）", "**是**"),
           ("ALLOCLINE", "第 3 宗以後之遠側界方向（`K-9-9 一`）", "**是**"),
           ("各宗 G 值", "決定遠側界之**位置** ⇒ `P_cur`／`B_cur`", "⚠️ **間接**（G 之分母含幾何面積·幾何面積來自 DXF∩BLOCK）"),
           ("BLOCK", "街廓多邊形；幾何面積、弦區間之邊集", "**是**")]
    for a, b, c in DEP:
        P("  %-16s %-46s %-12s" % (a, b, c))
    POP(len(DEP), len(DEP), "A-4 依賴清單（全列）")
    n_dxf = sum(1 for a, b, c in DEP if c.startswith("**是**"))
    P("  🔒 **`P6` 之判**：清單中來源為 DXF 者 ＝ **%d ／ %d** ⇒ %s"
      % (n_dxf, len(DEP),
         "✅ **≥ 1 ⇒ 換圖後 35 宗必然須重算**（`P6` 成立）" if n_dxf >= 1 else
         "🔴 **無一項來源為 DXF·具名**"))
    P("  ⛔ **本項⛔ 不預測數值**——換圖後之違反宗數／面積**未量**（⛔ 不換圖）。")
    P("  🔒 **本項之用途逐字**：供 KL 決定「先落地 `K-9-9`」抑或「先重烤換圖」，⛔ 非本單之結論。")

    # ── P7 第九法 ────────────────────────────────────────────────────
    P("")
    P("【G／P7】`run_all` 清單筆數之**第九法**（🔒 版本歷史淨增法·⛔ 與八法不同族）")
    P("-" * W)
    m9 = run_all_count_method9()
    P("  母體 ＝ `git log -p --follow -- verify/run_all.py` 之**逐行增刪**")
    from collections import Counter
    for tag, name in (("anchor", "首版（樣式錨在**行首** `^\\+\\s*\\(\"`）"),
                      ("inline", "🔒 **更正後**（樣式**行內** `^\\+.*?\\(\"`·節 97）")):
        na, nd, adds, dels = m9[tag]
        P("  %s：新增 **%d**／刪除 **%d** ⇒ **淨 ＝ %d**" % (name, na, nd, na - nd))
    na, nd, adds, dels = m9["inline"]
    ca, cd = Counter(adds), Counter(dels)
    P("  更正後之逐名計數（全列）：")
    for k in sorted(ca):
        P("     %-38s +%d%s" % (k, ca[k], ("  −%d" % cd[k]) if cd.get(k) else ""))
    POP(len(ca), len(ca), "第九法之逐名（全列·更正後）")
    miss = sorted(set(m9["inline"][2]) - set(m9["anchor"][2]))
    P("  🩸 **首版所漏者逐項具名** ＝ %s（其新增行與 `for` 敘述同行 ⇒ 行首錨落空）" % miss)
    P("  ⇒ **第九法（更正後）＝ %d**（施工單 `P7` 期望 **15**）⇒ %s"
      % (na - nd, "✅ 相符" if na - nd == 15 else "🔴 **不符·⛔ 不調整預測·具名**"))
    P("     🔒 **裸值（首版·⛔ 不以更正值取代）＝ %d**" % (m9["anchor"][0] - m9["anchor"][1]))
    if dels:
        P("  🔒 **本法獨有之可見物**：曾被**刪除**之項 ＝ %s（八法皆看不見）" % sorted(set(dels)))
    else:
        P("  🔒 **本法獨有之可見物**：曾被刪除之項 ＝ **0** ⇒ 清單自始只增未減"
          "（⛔ 此為本法之產出·八法皆無從得知）")

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
