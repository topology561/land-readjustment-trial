#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-43】§C 平行判測 ＋ §D 15 宗重分類 ＋ §F `S-9(二)` 三讀法並列（⛔ 零生產碼）

🔴 **⛔ 不改 `app.py` 任何一行**；一切幾何原語**呼叫**生產碼
（`_n14_band_geom`／`_n14_band_hi`／`parcel_min_width_n14`／`_baseline_normal_axis`／
`_baseline_pts_from_manual`／`get_min_lot_size`）。

**三組之受詞（⛔ 不得互代）**：
- **§C**：`K-9-6-h ④` 之「正街道路境界線與後側境界線**平行**」——受詞 ＝ **兩條線本身**。
  🔴 ⛔ **不得以「後緣角點之 t 差」反推**：該量之容差 ＝ `_EPS_TOUCH_FRONT`（**1 cm**），
  與待測之差**同數量級** ⇒ **判別力不足**（`W-G.9-43` §C-3）。
- **§D**：15 宗之重新分類——`K-9-11`（不配地＋遞補）／`K-9-6-h ④`（改寬度式）／`GB-65` 阻塞。
- **§F**：`S-9(二)` 之三讀法**並列**——⛔ 不擇一、⛔ 不加權、⛔ 不推薦。

🔒 **`GB-65` 之兩讀法⛔ 不擇一**（其擇一尚未定）：本檔**兩欄並列**，
兩讀法答案不同之街廓 ⇒ 出艙碼「`GB-65` 阻塞·無從判定」（`S-4`·⛔ 不停整批）。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
# 🔒 **單一真相源**：框／弦／斷點法一律取自 `W-G.9-42` 已通過 `C-1` 驗收閘之實作，
#   ⛔ 不在本檔另寫第二份（`GB-8`）。
from probe_WG941_bandbase import (st_frame, chord_at, min_width_band,   # noqa: E402
                                  normalize_ring)

OUTDIR = os.path.join(VERIFY, "out")
W = 178
SB = 0.0

# `GB-65` 兩讀法之門檻（⛔ 二者皆為**本檔明訂之讀法**，⛔ 非正典數字）
#   甲：單位向量分量差 < 5e-4（＝「小數點後第 3 位皆相同」之直譯·四捨五入半格）
#   乙：夾角上界 —— 由甲之最劣情形導出：兩分量各差 5e-4 ⇒ 角差上界 √2×5e-4
TH_A = 5e-4
TH_B = math.sqrt(2.0) * 5e-4


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def unit(vx, vy):
    L = math.hypot(vx, vy)
    return (vx / L, vy / L, L)


def _r3(v):
    """捨入至小數第 3 位（＋0.0 消 `-0.0`，使 `-0.0004` 與 `+0.0004` 同格）。"""
    return round(v, 3) + 0.0


def parallel_judgements(f_vec, b_vec):
    """回 `(甲判, 乙判, 丙判, 明細 dict)`。

    🩸 **`W-G.9-44` 之更正（⛔ 具名·`W-G.9-43` 之判準錯）**：
      `W-G.9-43` 只列**甲**（分量差 < 5e-4）與**乙**（夾角 < √2×5e-4），並以「兩讀法一致」
      稱 `S-4` 未觸發。🔴 **二者⛔ 非獨立**——乙之門檻**由甲之最劣情形導出**
      （該報告 §C 逐字自承）⇒ **`n` 份佐證若共用同一門檻之換算，則 `n = 1`**。
      ⇒ 「一致」什麼也沒證。

    🔒 **丙（`W-G.9-44` 新增）＝ 正典逐字之直譯**：`K-9-6-h ④` 逐字
      「兩線之 X、Y 向量分量於**小數點後第 3 位皆相同**，即視為平行。
        **原則性依據：KL 繪圖系統之座標顯示精度為小數點後第 3 位。**」
      ⇒ 立則之由係「**顯示精度**」⇒ 直譯為「**在 KL 的畫面上顯示成同一個數**」
      ＝ **各分量捨入至小數第 3 位後相等**，⛔ **非**「差值小於半格」。
      🔴 **二者不等價之實例（本案 R1）**：`0.687378` 與 `0.687675` 差僅 `2.97e-04`
      （< 半格 `5e-4` ⇒ 甲判平行），卻**跨格**（`0.687` vs `0.688` ⇒ 丙判不平行）。

    🔒 **號規之處置（⛔ 不可省）**：一條「線」之方向向量有 **±兩種**表示，
      而 `K-9-6-h ④` 之判準寫「兩線之 X、Y 向量分量**皆相同**」
      ⇒ 若二者號規相反，逐分量比會得出「不平行」而其實平行。
      ⇒ 本檔**兩種號規皆算**、取**較有利於「判平行」者**（⛔ 不預設號規），
        並把兩者之值都印出來讓讀者自行覆核。**丙式亦兩號規皆試。**
    """
    fx, fy, fL = unit(*f_vec)
    bx, by, bL = unit(*b_vec)
    cands = []
    for sgn in (1.0, -1.0):
        dx, dy = abs(fx - sgn * bx), abs(fy - sgn * by)
        cands.append((max(dx, dy), sgn, dx, dy))
    cands.sort()
    dmax, sgn, dx, dy = cands[0]
    # 夾角（取線與線之夾角 ⇒ 摺入 [0, π/2]）
    cosv = max(-1.0, min(1.0, fx * bx + fy * by))
    ang = math.acos(abs(cosv))
    # 丙：各分量捨入至小數第 3 位後相等（兩號規任一相等即平行）
    F3 = (_r3(fx), _r3(fy))
    Bp3, Bn3 = (_r3(bx), _r3(by)), (_r3(-bx), _r3(-by))
    c = (F3 == Bp3) or (F3 == Bn3)
    return (dmax < TH_A), (ang < TH_B), c, dict(
        fx=fx, fy=fy, bx=bx, by=by, fL=fL, bL=bL,
        sgn=sgn, dx=dx, dy=dy, dmax=dmax, ang=ang,
        dx_pos=abs(fx - bx), dy_pos=abs(fy - by),
        dx_neg=abs(fx + bx), dy_neg=abs(fy + by),
        F3=F3, Bp3=Bp3, Bn3=Bn3)


def selfcheck(P):
    """§C-2 判別力自檢：人造平行線 ／ 人造 0.01 rad 夾角線。"""
    P("【C-2】平行判準之判別力自檢（⛔ 附實際輸出）")
    P("-" * W)
    rows, ok = [], []
    th = math.radians(23.7)                       # ⛔ 非軸向
    base = (math.cos(th), math.sin(th))
    def _mk(x):
        return (x, math.sqrt(max(0.0, 1.0 - x * x)))
    cases = [
        ("人造·完全平行", base, base, True, True, True),
        ("人造·反向平行", base, (-base[0], -base[1]), True, True, True),
        ("人造·0.01 rad", base, (math.cos(th + 0.01), math.sin(th + 0.01)), False, False, False),
        ("人造·4e-4 rad", base, (math.cos(th + 4e-4), math.sin(th + 4e-4)), True, True, None),
        ("人造·1e-3 rad", base, (math.cos(th + 1e-3), math.sin(th + 1e-3)), False, False, None),
        # ── 丙之**專屬**對照物（⛔ 不與甲乙共用·**兩方向各一**，證甲丙不等價）──────
        # 🩸 **首版之同格測資是錯的（⛔ 具名·測資之錯·非量測器之錯）**：
        #   取 `_mk(0.6871)` / `_mk(0.6874)`，只控了 **x** 同格（0.687／0.687），
        #   而 **y** 由 `sqrt(1−x²)` 導出、**跨格**（0.726563→0.727 vs 0.726279→0.726）
        #   ⇒ 丙判不平行、與期望不符。依 `S-2`「**先疑測資、再疑量測器**」⇒ 換測資。
        # 🔒 現用測資由**數值搜尋**取得（θ=0.4595 rad·dθ=1.116e−03）：
        #   F=(0.896274360, 0.443500025)／B=(0.895778856, 0.444499991)
        #   **兩分量皆捨入為 (0.896, 0.444)**（同格）而**分量差 max ＝ 9.9997e−04 > 5e−4**
        #   ⇒ **甲判不平行 ∧ 丙判平行**（與跨格例**方向相反**）。
        ("丙·同格(1e-3)", (0.896274360, 0.443500025),
         (0.895778856, 0.444499991), False, False, True),
        ("丙·跨格(2e-5)", _mk(0.68749), _mk(0.68751), True, True, False),
    ]
    for tag, fv, bv, wa, wb, wc in cases:
        a, b, c, d = parallel_judgements(fv, bv)
        good = (a == wa and b == wb and (wc is None or c == wc))
        ok.append(good)
        rows.append((tag, a, b, c, d["dmax"], d["ang"], wa, wb, wc, good))
    def _p(z):
        return ("平行" if z else "不平行") if z is not None else "—"
    P(f"  {'項':<16}{'甲':>6}{'乙':>6}{'丙':>6}{'分量差max':>13}{'夾角(rad)':>13}"
      f"{'期甲':>6}{'期乙':>6}{'期丙':>6}  判")
    for tag, a, b, c, dm, ag, wa, wb, wc, good in rows:
        P(f"  {tag:<16}{_p(a):>6}{_p(b):>6}{_p(c):>6}"
          f"{dm:>13.3e}{ag:>13.3e}{_p(wa):>6}{_p(wb):>6}{_p(wc):>6}  {'✅' if good else '🔴'}")
    P(f"  🔒 門檻：甲 分量差 < {TH_A:.1e}（**CC 明訂**）"
      f"／乙 夾角 < √2×5e-4 ＝ {TH_B:.3e} rad（**由甲導出**）"
      f"／丙 **捨入至 3 位後相等**（**正典逐字之直譯**）")
    P("  🔴 **甲與乙⛔ 非獨立佐證**——乙之門檻由甲之最劣情形導出")
    P("     ⇒ `n` 份佐證若共用同一門檻之換算，則 `n = 1`")
    P("     ⇒ `W-G.9-43` 之「兩讀法一致 ⇒ `S-4` 未觸發」**不成立**（`W-G.9-44` 更正）。")
    P("  🔒 **丙式之判別力（⛔ 專屬對照物）**：")
    # 🩸 **`W-G.9-49` §G-1 修**：原印 6 位（`0.443500`／`0.444500`），讀者據以重算
    #   `y = sqrt(1−x²)` 得 `0.444` vs `0.445`（**跨格**）⇒ **與所述「丙判平行」相反**
    #   （half-up 與 half-even 兩慣例皆然）⇒ **印出之位數不足以重現結論**。
    #   ⇒ 改印 **9 位**（實值 `0.443500025`／`0.444499991`）。
    P("     · 同格例 `(0.896274360, 0.443500025)` vs `(0.895778856, 0.444499991)`"
      "：差 **9.9997e-04**（**> 甲門檻**）")
    P("       🔒 **⛔ 須印 9 位**：若只印 6 位（`0.443500`／`0.444500`），"
      "讀者重算 `y` 會得 `0.444` vs `0.445`（**跨格**）⇒ 與本項之「丙判平行」相反。")
    P("       而兩分量**皆同格 (0.896, 0.444)** ⇒ **甲判不平行 ∧ 丙判平行**")
    P("     · 跨格例 `0.68749` vs `0.68751`：差 **2.0e-05**（≪ 甲門檻）而**跨格**")
    P("       ⇒ **甲判平行 ∧ 丙判不平行**")
    P("     ⇒ 丙式**非恆真亦非恆假**；且二例使甲丙**各自互為相反**（兩方向各一）")
    P("       ⇒ **甲與丙不等價**係**雙向坐實**，⛔ 非單向舉例。")
    return all(ok)


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * W)
    P("【W-G.9-43】§C 平行判測 ＋ §D 15 宗重分類 ＋ §F 三讀法並列")
    P("=" * W)
    P(f"  產生於 commit：{sha}")
    P("  🔴 ⛔ 零生產碼——幾何原語全為呼叫；框／弦／斷點法取自 `probe_WG941_bandbase`（已過 C-1 閘）")
    P("")

    if not selfcheck(P):
        P("")
        P("🛑 判別力自檢紅 ⇒ `S-2` ⇒ 停機·本次量測⛔ 不出艙。")
        return L, sha
    P("  ⇒ 自檢：PASS")
    P("")

    ns, fake_st = harvest()
    eps_touch = float(ns["_EPS_TOUCH_FRONT"])
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d, _s, _o, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        SB, snapshot=snapshot)
    BLKS = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in BLKS:
            BLKS.append(_l)
    g_rows, ERR = [], {}
    for lbl in BLKS:
        try:
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                             [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                             winners, forced, SB)
            g_rows.extend(_sg["g_rows"])
        except Exception as e:                                       # noqa: BLE001
            ERR[lbl] = f"{type(e).__name__}: {str(e).splitlines()[0][:130]}"
    rows = [r for r in g_rows if str(r.get("推進側別")) in ("left", "right")]
    OKB = [b for b in BLKS if b not in ERR]

    # ══════════════════════════════════════════════════════════════════
    # §C-1 逐街廓平行判測
    # ══════════════════════════════════════════════════════════════════
    P("=" * W)
    P("【C-1】`K-9-6-h ④` 平行判準之逐街廓實測（⛔ 只取 `run_step_g` 成功者）")
    P("=" * W)
    P("  🔴 **受詞 ＝ 兩條線本身**（FRONTLINE 之 p1→p2 ／ BASELINE 之 `_baseline_pts_from_manual`）")
    P("  🔴 ⛔ **未以「後緣角點之 t 差」反推**——該量之容差 ＝ `_EPS_TOUCH_FRONT` ＝ "
      f"{eps_touch} m，與待測之差同數量級 ⇒ 判別力不足（§C-3）。")
    P("")
    PAR = {}
    for lbl in OKB:
        fl = fl_by.get(lbl) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl),
                                             (cb_by.get(lbl) or {}).get("vertices"))
        fv = (float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1]))
        bv = (float(bp[1][0]) - float(bp[0][0]), float(bp[1][1]) - float(bp[0][1]))
        a, b, c, d = parallel_judgements(fv, bv)
        PAR[lbl] = (a, b, c, d)
        P(f"  ── {lbl} ──")
        P(f"     FRONTLINE 原始向量 = ({fv[0]:+.9f}, {fv[1]:+.9f})　長 {d['fL']:.9f}")
        P(f"     BASELINE  原始向量 = ({bv[0]:+.9f}, {bv[1]:+.9f})　長 {d['bL']:.9f}")
        P(f"     單位化    FRONT    = ({d['fx']:+.12f}, {d['fy']:+.12f})")
        P(f"     單位化    BASE     = ({d['bx']:+.12f}, {d['by']:+.12f})")
        P(f"     分量差 同號 |Δx|={d['dx_pos']:.6e} |Δy|={d['dy_pos']:.6e}"
          f"　｜ 反號 |Δx|={d['dx_neg']:.6e} |Δy|={d['dy_neg']:.6e}")
        P(f"     ⇒ 採號規 {d['sgn']:+.0f}（較有利於判平行）·分量差 max ＝ **{d['dmax']:.6e}**"
          f"　夾角 ＝ **{d['ang']:.6e} rad**（＝ {math.degrees(d['ang']):.6f}°）")
        P(f"     捨入至 3 位：F {d['F3']}　B(同號) {d['Bp3']}　B(反號) {d['Bn3']}")
        P(f"     【甲】分量差 < {TH_A:.1e} ⇒ **{'平行' if a else '不平行'}**"
          f"　｜【乙】夾角 < {TH_B:.3e} ⇒ **{'平行' if b else '不平行'}**"
          f"　｜【丙】捨入後相等 ⇒ **{'平行' if c else '不平行'}**")
        _ag = (a == b == c)
        P(f"     ⇒ {'✅ 三讀法一致' if _ag else '🛑 **三讀法不一致 ⇒ `GB-65` 阻塞·無從判定（S-4）**'}"
          + ("" if _ag else "　🔴 甲乙非獨立（乙由甲導出）⇒ 實為「甲乙」vs「丙」之二分"))
        P("")
    for lbl in BLKS:
        if lbl in ERR:
            P(f"  ⛔ {lbl}：`run_step_g` raise ⇒ **未量**（{ERR[lbl]}）")

    # ══════════════════════════════════════════════════════════════════
    # §D-1 逐宗量：|I_F| / |I_B| / 傾移 / 法定最小寬 / GB-70 旗標
    # ══════════════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【D-1】15 宗（`I_F ∩ I_B = ∅` 者）之逐宗量 ＋ 全母體之 `GB-70` 旗標")
    P("=" * W)
    P(f"  {'街廓':<5}{'側':<6}{'暫編地號':<14}{'面積㎡':>10}{'|I_F|':>10}{'|I_B|':>10}"
      f"{'min':>10}{'傾移近':>10}{'傾移遠':>10}{'法定寬':>8}{'零條?':>7}{'GB-70旗':>9}  分類")
    D1, GB70, FRAG, SHEAR_MATCH = [], [], [], []
    for r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
        cc = r.get("cut_coords") or []
        if str(r.get("街角地", "")).strip() == "是" or len(cc) < 3:
            continue
        try:
            area = float(r.get("幾何面積(㎡)") or 0.0)
        except Exception:                                            # noqa: BLE001
            area = float("nan")
        fl = fl_by.get(lbl) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        if not (p1 and p2):
            continue
        dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        Lf = math.hypot(dx, dy)
        dh = (dx / Lf, dy / Lf)
        bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl),
                                             (cb_by.get(lbl) or {}).get("vertices"))
        mw = ns["get_min_lot_size"](cb_by[lbl]["category"],
                                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        lw = float(mw.get("min_width", 0.0) or 0.0)   # ⛔ 無 `or 3.5` 兜底
        try:
            rear = ns["_n14_band_geom"](cc, dh, p1, bp, _label=f"{lbl}/{gid}")[1]
            ring, t_lo, sg, dd, nn, fe = st_frame(cc, dh, p1, eps_touch)
        except Exception:                                            # noqa: BLE001
            continue
        fs = sorted({ring[i][0] for i in fe} | {ring[i + 1][0] for i in fe})
        IF = (fs[0], fs[-1])
        bs = sorted(r2[2] for r2 in rear)
        IB = (bs[0], bs[-1])
        wF, wB = IF[1] - IF[0], IB[1] - IB[0]
        # 🔒 **傾移** ＝ 側界於 `t=0` 與 `t=D` 之 `s` 差之絕對值（＝該側之剪移量）。
        #   近側／遠側由 `推進側別` 定（同 `W-G.9-42` §C-2·⛔ 非由形狀回推）。
        if side == "left":
            sf_near, sb_near, sf_far, sb_far = IF[0], IB[0], IF[1], IB[1]
        else:
            sf_near, sb_near, sf_far, sb_far = IF[1], IB[1], IF[0], IB[0]
        sh_near, sh_far = abs(sb_near - sf_near), abs(sb_far - sf_far)
        zero = (min(IF[1], IB[1]) < max(IF[0], IB[0]))
        flag = (min(wF, wB) >= lw - 1e-9) and zero      # `GB-70`：法定寬合格 ∧ 零條合格垂線
        if flag:
            GB70.append((lbl, gid, area, min(wF, wB), lw))
        if zero:
            # 🔒 **碎片宗先分流**（`W-G.9-42` §D-2·正規化後 ≤3 邊）：其出艙碼為
            #   「**上游狀態不合規**」，⛔ **不得**改列 `K-9-11` 之不配地＋遞補
            #   ——`K-9-11` 之受詞是「**G 值所形成之面寬**」，而碎片宗之病在**上游**。
            if len(normalize_ring([tuple(map(float, q)) for q in cc], 0.01)) <= 3:
                FRAG.append((lbl, gid, area, wF, wB))
                P(f"  {lbl:<5}{side:<6}{gid:<14}{area:>10.2f}{wF:>10.4f}{wB:>10.4f}"
                  f"{min(wF, wB):>10.4f}{sh_near:>10.4f}{sh_far:>10.4f}{lw:>8.2f}"
                  f"{'是':>7}{'—':>9}  **上游狀態不合規**（碎片·⛔ 不改列 `K-9-11`）")
                continue
            D1.append((lbl, gid, area, wF, wB, sh_near, sh_far, lw))
            if lbl in PAR:
                a, b, c, _ = PAR[lbl]
                cls = ("`K-9-11`：不配地·由下一投影序號遞補" if not (a or b or c)
                       else ("①②停用·改適用 `K-9-6-h ④` 之寬度式" if (a and b and c)
                             else "🛑 `GB-65` 阻塞·無從判定"))
            else:
                cls = "⛔ 街廓未量"
            P(f"  {lbl:<5}{side:<6}{gid:<14}{area:>10.2f}{wF:>10.4f}{wB:>10.4f}"
              f"{min(wF, wB):>10.4f}{sh_near:>10.4f}{sh_far:>10.4f}{lw:>8.2f}"
              f"{'是':>7}{('🔴 是' if flag else '否'):>9}  {cls}")
    P("-" * W)
    P(f"  零條合格垂線之宗（**扣除碎片後**）＝ **{len(D1)}** 宗／面積合計 **{sum(x[2] for x in D1):.4f} ㎡**")
    P(f"  ＋ 碎片宗（**上游狀態不合規**·⛔ 不改列 `K-9-11`）＝ **{len(FRAG)}** 宗／"
      f"**{sum(x[2] for x in FRAG):.4f} ㎡** ⇒ 二者⛔ 不得相加為一個結論")
    for _l, _g, _a, _f, _b in FRAG:
        P(f"      {_l}/{_g}　面積 {_a:.4f}　|I_F| {_f:.4f}　|I_B| {_b:.4f}")
    P(f"  🔴 `GB-70` 旗標（法定寬合格 ∧ 零條合格垂線）＝ **{len(GB70)}** 宗")
    if not GB70:
        P("     🔒 零計數之構造證：旗標式 ＝ `min(|I_F|,|I_B|) ≥ 法定寬` ∧ `零條`；")
        P("       二子句於本母體皆各自出現過（零條 15 宗；min 寬 ≥ 3.50 者見上表 R3/R6 多宗）")
        P("       ⇒ 其合取非結構恆假，僅本案無宗同時滿足。")

    # §D-3 對拍 claude.ai 之表
    P("")
    P("【D-3】對拍施工單 §D-3 之表（⛔ 未逕抄·自行重算後逐格比）")
    P("-" * W)
    REF = {
        "628-34(3)": (86.00, 2.3945, 2.7969, 2.6813),
        "628(2)": (7.38, 0.1552, 0.1546, 3.8315),
        "628-1(2)": (145.82, 3.0737, 3.0613, 3.8309),
        "628-23(1)": (71.03, 1.5010, 1.4950, 3.8185),
        "628-22(1)": (152.21, 3.2754, 3.2623, 3.7531),
        "628-38(1)": (117.73, 2.6960, 2.6851, 3.5261),
        "628(4)": (44.89, 1.0265, 1.0254, 4.0520),
        "628-47(1)": (143.38, 3.2715, 3.2679, 4.0596),
        "628-46(1)": (72.77, 1.6592, 1.6574, 4.0632),
        "628-48(1)": (143.40, 3.2675, 3.2638, 4.0650),
        "628-49(2)": (79.05, 1.8000, 1.7980, 4.0687),
        "628-42(2)": (87.90, 0.2651, 3.6551, 4.1511),
        "628-27(2)": (25.94, 0.5792, 0.5785, 4.1504),
        "628-28(1)": (63.52, 1.4186, 1.4170, 4.1488),
        "628-29(1)": (63.72, 1.4234, 1.4219, 4.1473),
    }
    got = {x[1]: x for x in D1}
    P(f"  {'暫編地號':<14}{'欄':<8}{'單載':>12}{'實得':>12}{'差':>12}  判")
    nbad = 0
    for gid, (ra, rf, rb, rs) in REF.items():
        if gid not in got:
            P(f"  {gid:<14}{'—':<8}{'':>12}{'（不在本批 15 宗內）':>12}{'':>12}  🔴")
            nbad += 1
            continue
        _, _, ar, wF, wB, shn, shf, _lw = got[gid]
        for name, ref, cur in (("面積", ra, ar), ("|I_F|", rf, wF), ("|I_B|", rb, wB)):
            d = cur - ref
            bad = abs(d) > 5e-4 if name != "面積" else abs(d) > 5e-3
            nbad += bad
            P(f"  {gid:<14}{name:<8}{ref:>12.4f}{cur:>12.4f}{d:>+12.6f}  {'🔴' if bad else '✅'}")
        # 🔴 **「傾移」欄⛔ 不逐格比單一值**——單之取法與本檔之近／遠參數化**不同**：
        #   本檔依 `推進側別` 分「近側／遠側」二值；單則**未參數化**。
        #   ⇒ 併列二值，並具名**單所載者等於哪一個**（⛔ 不強行取一個去湊）。
        which = ("近" if abs(shn - rs) <= 5e-4 else
                 ("遠" if abs(shf - rs) <= 5e-4 else "🔴 皆不符"))
        SHEAR_MATCH.append((gid, which))
        nbad += (which == "🔴 皆不符")
        P(f"  {gid:<14}{'傾移':<8}{rs:>12.4f}"
          f"{('近=' + f'{shn:.4f}' + ' 遠=' + f'{shf:.4f}'):>26}"
          f"　單所載 ＝ **{which}**")
    P(f"  ⇒ 不符格數 ＝ **{nbad}**（面積 5e-3／`|I_F|`·`|I_B|` 5e-4／傾移採二值併列）")
    P("")
    P("  🔴 **「傾移」之取法：單與本檔不一致（⛔ 具名·⛔ 非算錯）**")
    _near = sum(1 for _, w in SHEAR_MATCH if w == "近")
    _far = sum(1 for _, w in SHEAR_MATCH if w == "遠")
    _non = sum(1 for _, w in SHEAR_MATCH if w.startswith("🔴"))
    P(f"     單所載之值：等於本檔之**近側** {_near} 宗／**遠側** {_far} 宗／**皆不符** {_non} 宗")
    P("     ⇒ 單之取法**⛔ 非** 「一律近側」亦**⛔ 非**「一律遠側」")
    P("       ——逐格檢視為「**`s` 較小之側**」（⛔ 未依推進側別參數化）。")
    P("     🔒 **本檔⛔ 不改採該取法**：`W-G.9-42` 缺陷 ⑤ 之受詞正是")
    P("       「以固定 `s` 大小定側別 ⇒ 鏡像組整組反向」；改回去即重蹈之。")
    P("     ⚠️ **惟本欄之差⛔ 不影響本批任一分類**——`零條合格垂線` 之判係由")
    P("       **`I_F ∩ I_B = ∅` 直接判定**（區間不相交），⛔ 非由「傾移 > |I_F|」推得。")
    P("       「傾移」只是**平行四邊形情形下**之等價敘述；於楔形（`628-42(2)`）已不等價。")

    # ══════════════════════════════════════════════════════════════════
    # §F　`S-9(二)` 之三讀法並列（⛔ 不擇一、⛔ 不加權、⛔ 不推薦）
    # ══════════════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【F】`S-9(二)` 三讀法並列（`W-G.9-42` 只列兩支·本批補第三支）")
    P("=" * W)
    P("  甲：帶底照舊（`min(最淺有效, 近側界終止)`），該段之弦照量　⇒ 不牴觸 `K-9-10 六`")
    P("  乙：帶底再加 `min(…, 遠側界終止)`　⇒ 🔴 **牴觸六**（新帶恆不深於舊帶）")
    P("  丙：帶底照舊，但第五款之 min **只在第四款有定義之 `t` 上取**（`t ≤ 遠側界終止`）")
    P("      ⇒ 不牴觸六之**字面**；惟使六於其所指之形狀上**無實效**")
    P("")
    P(f"  {'街廓':<5}{'暫編地號':<14}{'面積㎡':>10}{'法定寬':>8}{'t_hi舊':>10}{'遠側終止':>10}"
      f"{'t_band新':>10}{'甲寬':>10}{'乙寬':>10}{'丙寬':>10}{'甲判':>7}{'乙判':>7}{'丙判':>7}")
    NF = 0
    for r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
        cc = r.get("cut_coords") or []
        if str(r.get("街角地", "")).strip() == "是" or len(cc) < 3:
            continue
        fl = fl_by.get(lbl) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        if not (p1 and p2):
            continue
        dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        Lf = math.hypot(dx, dy)
        dh = (dx / Lf, dy / Lf)
        bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl),
                                             (cb_by.get(lbl) or {}).get("vertices"))
        mw = ns["get_min_lot_size"](cb_by[lbl]["category"],
                                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        lw = float(mw.get("min_width", 0.0) or 0.0)
        try:
            from probe_WG941_bandbase import analyse as _an
            a = _an(ns, cc, dh, p1, bp, side, eps_touch, f"{lbl}/{gid}")
        except Exception:                                            # noqa: BLE001
            continue
        if a["s9"] or not a["canon_gap"]:
            continue
        NF += 1
        w_a, _, _, _ = min_width_band(a["ring"], a["t_lo"], a["t_band"])
        w_b, _, _, _ = min_width_band(a["ring"], a["t_lo"], min(a["t_band"], a["t_far"]))
        w_c, _, _, _ = min_width_band(a["ring"], a["t_lo"], a["t_far"])
        try:
            ar = float(r.get("幾何面積(㎡)") or 0.0)
        except Exception:                                            # noqa: BLE001
            ar = float("nan")

        def _j(w):
            return "—" if w is None else ("合格" if w >= lw - 1e-9 else "不合格")
        P(f"  {lbl:<5}{gid:<14}{ar:>10.2f}{lw:>8.2f}{a['t_hi_old']:>10.4f}"
          f"{a['t_far']:>10.4f}{a['t_band']:>10.4f}"
          f"{w_a:>10.4f}{w_b:>10.4f}{w_c:>10.4f}{_j(w_a):>7}{_j(w_b):>7}{_j(w_c):>7}")
        # F-2：`t ∈ (遠側界終止, t_band]` 之弦長區間起訖
        c1 = chord_at(a["ring"], a["t_far"])
        c2 = chord_at(a["ring"], a["t_band"])
        P(f"        F-2　弦長於 t={a['t_far']:.4f} ⇒ "
          f"{('無交點' if c1 is None else f'{c1[0]:.4f}')}"
          f"　於 t={a['t_band']:.4f} ⇒ {('無交點' if c2 is None else f'{c2[0]:.4f}')}"
          f"　（區間長 {a['t_band']-a['t_far']:+.4f} m）")
    P("-" * W)
    P(f"  `S-9(二)` 之宗 ＝ **{NF}** 宗")
    P("  🔒 **⛔ 三支不擇一、⛔ 不加權、⛔ 不推薦**——由 KL 裁（`U-VR14-2`）。")
    P("  🔒 **⛔ 不得**把甲支下之任一數字寫成結論（`W-G.9-43` §F-3）。")

    # ══════════════════════════════════════════════════════════════════
    # §D-4　遞補連鎖（⛔ 靜態預測·⛔ 不冒充實測）
    # ══════════════════════════════════════════════════════════════════
    P("")
    P("=" * W)
    P("【D-4】遞補連鎖 ⇒ 🛑 **只出靜態預測·⛔ 非實測**（依 §D-4(d)）")
    P("=" * W)
    P("  🔴 **為何只出預測（⛔ 具名·非偷懶）**：`K-9-11` 之遞補須**改變投影序次並重跑配地**")
    P("     ——其實作屬 **`K-6-A2`**，而本單 §K-1 逐字「⛔ 不實作 `K-9-11` 於生產」。")
    P("     ⇒ (a) 輪數、(b) 最終不配地宗數與面積、(c) 每輪入池面積與守恆殘差")
    P("       **皆⛔ 無從實測**——它們是**遞補實作之輸出**，⛔ 不是現況之量。")
    P("")
    P("  **靜態預測（⛔ 標明為預測·⛔ 不得下游引用為實測）**：")
    P(f"  · 第 1 輪之候選 ＝ 現況零條合格垂線且街廓**三讀法一致判不平行**者 ＝ "
      f"**{sum(1 for x in D1 if x[0] in PAR and not any(PAR[x[0]][:3]))}** 宗"
      f"　（⛔ `GB-65` 阻塞之街廓不計入）")
    P("  · **⛔ 不預測輪數**：遞補者之 G 值改變後其面寬亦改變（`K-9-11 四` 須重測），")
    P("    而新 G 值須由引擎重跑方得 ⇒ **⛔ 無從以現況之數外推**。")
    P("  · 🔒 **⛔ 不得逕以「15 宗」或「16 宗」當作最終不配地數**（§D-4(b) 明文）。")
    P("  · 守恆式 `ΣG + 調配池 = 街廓 DXF 面積` 之殘差：**⛔ 本批未量**"
      "（其量測需遞補後之終態）。")

    # ── 出艙碼 ────────────────────────────────────────────────────────
    P("")
    P("=" * W)
    P("  🔒 出艙碼（⛔ 各類不得互代、不得相加）")
    for lbl in OKB:
        a, b, c, _ = PAR[lbl]
        n = sum(1 for x in D1 if x[0] == lbl)
        code = ("`K-9-11`：不配地·由下一投影序號遞補" if not (a or b or c)
                else ("`K-9-6-h ④`：①②停用·改適用其寬度式" if (a and b and c)
                      else "🛑 `GB-65` 阻塞·無從判定"))
        st = ("平行(三讀法一致)" if (a and b and c)
              else ("不平行(三讀法一致)" if not (a or b or c) else "🛑 三讀法不一致"))
        P(f"    {lbl}（{st}）：零條合格垂線 {n} 宗 ⇒ **{code}**")
    for lbl in BLKS:
        if lbl in ERR:
            P(f"    {lbl}：**上游狀態不合規·⛔ 不作寬度判定**（`run_step_g` raise）")
    P(f"    碎片宗 {len(FRAG)} 宗：**上游狀態不合規**")
    P(f"    `S-9(二)` {NF} 宗：**正典未裁·待 KL**（`U-VR14-2`·三讀法已並列）")
    P("=" * W)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _r = main()
    _L, _sha = _r[0], _r[1]
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG943_parallel_recount_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
