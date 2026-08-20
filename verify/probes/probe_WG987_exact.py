# -*- coding: utf-8 -*-
r"""**W-G.9-87 §二 A 組**：`K-9-9 二` 之**精確實作**（實算垂足 ＋ 推進向定序 ＋ 對應端點）
＋ **三項更正之消融** ＋ **斜跨距之來源** ＋ `D-0` 二項補辦。

## 受詞（施工單 `W-G.9-87` §二·`VR-045` 七）
- **A-1**（🛑 第一項）依 `K-6:2115–2132` 逐字實作**三項更正**並重判；**負對照 ＝ 舊形**（`w40.eval_lot` 原樣）。
- **A-2** 三項更正之**消融**（`2³` 中至少 5 組）——右側 `22／22` 之簽名由哪一項消除？
- **A-3** **斜跨距之來源**：`∠(BASELINE, FRONTLINE)` 與逐宗斜跨距分布。
- **A-4** 左側三組跳號（`-85` `P6`）＋ `R1 左 j=0` 之雙重異常（`VR-044` 六-4）。

## 🔒 A-0　錯誤方向之**事前選定**（節 98·⛔ 寫碼前寫入本 docstring）
本單欲驗「以正典逐字重判 ⇒ 違反宗數是否為 `0`」。其瑕若使**違反數偏低** ⇒ 得一乾淨之 `0`
⇒ **安靜**、且與本裁之期待一致 ⇒ 🔴 **會安靜地放過真違反之宗（土地後果⛔ 非零）**。
🔒 **事前選定：偏向<u>保留違反</u>**——落實為三條，⛔ 逐條具名：
  (甲) 垂足／定序／端點配對之取捨不確定者，一律取**使該宗仍判違反**之解讀並具名；
  (乙) 出艙碼之容差沿用 `w40` 之 `-1e-6`（⛔ 不另立），**並同批出艙「改以嚴格 `>= 0` 判」之翻面筆數**
       ——⛔ 不以較寬之容差吸收違反；
  (丙) `adv`（推進向）二源不一致者，取**使該宗仍判違反**之號並具名；二源皆取不到者⛔ 不判、具名。

## 🔒 同源聲明（節 100·⛔ 不另造第二份）
`w40.eval_lot`／`far_side_dir_and_pt`／`line_isect`／`s_of`、`w82.chord_interval`／`ring_edges`／
`pj_of`／`uj_of`、`w81.analyse_cell`／`spy_solve`／`spy_pool`／`faces_of`、
`w86._par_tol_from_code`／`_sin`、`w84.s_front_of_line` 皆**原樣 import**。
`w83`／`w84`／`w85`／`w86` 之量測邏輯寫在 `main()` 內⛔ 不可 import（🔒 逐字具名之差）；
本檔 import 其**模組級**符號。
🔒 **新判定式 `eval_exact` 之三旗全關時，須與 `w40.eval_lot` 逐位相同**——本檔逐宗斷言之
⇒ ⛔ 非重造判定式，係**在同一式上逐項掛更正**。

## ⛔ 本檔不做（施工單 §二 A-5 七款）
⛔ 零 `app.py` 變更；⛔ `data/`／`docs/rulings/` 零變更；⛔ 不落地 `K-9-9`／`K-9-14`；
⛔ 不建遞補／合併／調配池介面；⛔ 不換圖／不重烤／不改任何 baseline；
⛔ **不另立平行判定之門檻**（`K-6:1010`）、⛔ **不另立座標框**（`K-6:2426`）；
⛔ 不出艙「應改領現金之宗」；⛔ 不以「理論上恆真」代替實算；⛔ 不以空母體之全過充作通過；
⛔ 不下「這是 bug」之結論；🔴 ⛔ **不得就 `K-9-9 二` 之實作提出任何「正典應如何修改」之主張**。

## 🔒 常設條款
**8** 每判準附「會使它為否」之輸入；**9** 門檻併出艙量級與 `math.ulp`、跨數量級**分層**；
**10** 每表末印 `POPULATION/PRINTED/SUPPRESSED`，報告中 ≥4dp 之數可回指 log 行；
**11** 修法列動作清單（本檔「⛔ 不經 shell 傳字樣」**適用讀＋寫**·以 `Write` 落盤）；
**12／13** 搜尋規格含正典款號組＋三類出處分類——見報告 §A；
**14** 分離之宣稱一律**單一門檻**＋未定義帶筆數；門檻**先查正典**；`m／n` 須併出艙判別力為零者幾筆；
**15**（`自誤 90` 修法 102〜104）受詞之標題⛔ 不含未證之因果限定語；凡受詞含屬性 `X` 須同批出艙
「**不具 `X`**」之對照（本檔 `A-2` 消融即其落實）。
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

OUTDIR = os.path.join(VERIFY, "out")
W = 210
SB = 0.0                       # 🔒 情境母體 ＝ 僅 0m（⛔ 不擴·具名）

PAR_TOL = w86.PAR_TOL          # 🔴 正典容差（`K-6:1010`）·⛔ 不另立（原樣自 `w86` 取）
EPS_DEG = 1e-9                 # 🔒 甲乙判別之退化容差 ＝ `w40.eval_lot` 逐字（⛔ 不另立）
TOL_ORD = 1e-6                 # 🔒 出艙碼容差 ＝ `w40.eval_lot` 逐字（⛔ 不另立）

_u = w86._u
_sin = w86._sin
s_front_of_line = w86.s_front_of_line


def _short_head():
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO,
                              capture_output=True, text=True).stdout.strip() or "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG987_exact_%s.log" % COMMIT)


# ══════════════════════════════════════════════════════════════════════════
#  🔒 `K-9-9 二` 之**可掛更正**判定式（三旗全關 ⇒ 逐位 == `w40.eval_lot`）
# ══════════════════════════════════════════════════════════════════════════
def eval_exact(P_prev, B_prev, P_cur, B_cur, o, d, n, bpt, bdir, adv,
               use_adv=False, use_foot=False, use_pair=False, strict=False):
    """依 `K-6:2115–2132` 逐字之判定式；三旗逐一掛上「更正」。

    - `use_adv`   ＝ **甲**：`之前／之後／max` 依**推進方向**定序（`K-6:2115–2116`／`:2158`）
    - `use_foot`  ＝ **乙**：**實算垂足**（`K-6:2119–2120`）·⛔ 不壓成 `s(P_prev)`／`s(B_prev)`
    - `use_pair`  ＝ **丙**：**逐端點對應比較**（`K-6:2121–2122`／`:2126–2132`）·⛔ 非 `min` 對 `max`
    - `strict`    ＝ A-0 (乙) 之嚴格判（`>= 0`·⛔ 非另立門檻，係同批併呈之保留違反解讀）

    回 `(情形, (front 端 s_adv, base 端 s_adv), (Δ_front′, Δ_base′), 出艙碼, 垂足坐標 dict)`。
    """
    sgn = (1.0 if adv > 0 else -1.0) if use_adv else 1.0

    def sa(pt):
        return sgn * w40.s_of(pt, o, d)

    feet = {"Bperp": None, "Pperp": None, "res_B": float("nan"), "res_P": float("nan")}
    if use_foot:
        # 🔒 `B⊥` ＝ 自 `P_prev` 沿 **FRONTLINE 法向** 至 BASELINE 之垂足（`K-6:2119`）
        # 🔒 `P⊥` ＝ 自 `B_prev` 沿**同一法向**至 FRONTLINE 之垂足（`K-6:2120`）
        Bp = w40.line_isect(P_prev, n, bpt, bdir)
        Pp = w40.line_isect(B_prev, n, o, d)
        if Bp is None or Pp is None:
            return None, None, None, "⛔ 垂足求不出（法向 ∥ 目標線）", feet
        feet["Bperp"], feet["Pperp"] = Bp, Pp
        s_Bperp, s_Pperp = sa(Bp), sa(Pp)
        # 🔒 與「壓成 `s`」之殘差（⛔ 供出艙·⛔ 不入判準）
        feet["res_B"] = abs(s_Bperp - sa(P_prev))
        feet["res_P"] = abs(s_Pperp - sa(B_prev))
    else:
        s_Pperp = sa(B_prev)        # `B_prev` 沿法向投影至 FRONTLINE ⇒ `s` 不變（舊形之壓縮）
        s_Bperp = sa(P_prev)        # `P_prev` 沿法向投影至 BASELINE ⇒ `s` 不變（舊形之壓縮）

    s_Pprev, s_Bprev = sa(P_prev), sa(B_prev)
    if s_Pperp < s_Pprev - EPS_DEG:
        case, front_end, base_end = "甲", s_Pprev, s_Bperp
    elif s_Pperp > s_Pprev + EPS_DEG:
        case, front_end, base_end = "乙", s_Pperp, s_Bprev
    else:
        case, front_end, base_end = "退化(P⊥＝P_prev)", s_Pprev, s_Bprev

    s_Pcur, s_Bcur = sa(P_cur), sa(B_cur)
    if use_pair:
        d_front, d_base = s_Pcur - front_end, s_Bcur - base_end
    else:
        # 🔒 ⓪ 之形 ＝ `-86` 恆等式乙：`min(本宗二交點) − max(前宗二交點)`（於當前定序下）
        m = min(s_Pcur, s_Bcur) - max(s_Pprev, s_Bprev)
        d_front = d_base = m
    lim = 0.0 if strict else -TOL_ORD
    code = "合格" if (d_front >= lim and d_base >= lim) else "不合格"
    return case, (front_end, base_end), (d_front, d_base), code, feet


# ══════════════════════════════════════════════════════════════════════════
#  🔒 第十三法：位元組碼之**行號映射**（`co_lines()`）× 原始碼文本之交叉法
#     ⛔ 與既用十二法皆不同族——受詞 ＝ **`offset → lineno` 之映射表**，
#     ⛔ 非常數池（④⑥）、⛔ 非運算元（⑫）、⛔ 非 AST（②）、⛔ 非全檔文本（①）。
# ══════════════════════════════════════════════════════════════════════════
def _strip_comment(line):
    """剝除行末註解（引號感知）——🔒 ⛔ 不用 `tokenize`（其為既用**第三法**之族）。"""
    q = None
    for i, ch in enumerate(line):
        if q:
            if ch == q:
                q = None
        elif ch in "'" + '"':
            q = ch
        elif ch == "#":
            return line[:i]
    return line


def run_all_count_method13(src=None, path=None):
    """回 (筆數, 名單, 迴圈之來源行區間)。⛔ 僅 `compile`·⛔ 未 `exec`。"""
    import dis
    if src is None:
        path = os.path.join(VERIFY, "run_all.py")
        src = io.open(path, encoding="utf-8").read()
    code = compile(src, path or "<src>", "exec")
    lines = src.split("\n")
    best = None
    stack = [code]
    while stack:
        c = stack.pop()
        for k in c.co_consts:
            if hasattr(k, "co_code"):
                stack.append(k)
        # 🔒 `co_lines()` 回 **(start, end, lineno) 區間** ⇒ 以**區間包含**查表。
        #    🩸 ⛔ **不得**以 `offset` 精確相等查（實測 16 個 `FOR_ITER` 全回 `None`
        #       ⇒ **假 0**·`W-G.9-87` §I 記之）。
        lm = [(a, b, ln) for a, b, ln in c.co_lines() if ln is not None]

        def _line_at(off):
            for a, b, ln in lm:
                if a <= off < b:
                    return ln
            return None

        for ins in dis.get_instructions(c):
            if ins.opname != "FOR_ITER":
                continue
            ln_for = _line_at(ins.offset)
            if ln_for is None:
                continue
            # 🔒 受詞 ＝ 迴圈**標頭**之來源行區間：自 `for` 行往下，
            #    以**括號平衡**（⛔ 註解先剝除·引號感知）決定其止行。
            depth, end = 0, ln_for
            for t in range(ln_for - 1, len(lines)):
                code_ = _strip_comment(lines[t])
                depth += (code_.count("(") + code_.count("[")
                          - code_.count(")") - code_.count("]"))
                end = t + 1
                if depth <= 0:
                    break
            head = "\n".join(_strip_comment(x)
                             for x in lines[ln_for - 1:end])
            names = re.findall(r'["\']([A-Za-z0-9_./]+\.py)["\']', head)
            if names and (best is None or len(names) > len(best[0])):
                best = (names, (ln_for, end))
    if best is None:
        return 0, [], None
    return len(best[0]), best[0], best[1]


# ══════════════════════════════════════════════════════════════════════════
def selfcheck(P):                                                   # noqa: C901
    ok = {}
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·每項皆附**已知真／已知偽**對照）")
    P("-" * W)

    # ① `eval_exact` 三旗全關 == `w40.eval_lot`（⛔ 非重造判定式之證）
    TH = math.radians(17.0)
    d = (math.cos(TH), math.sin(TH))
    n = (-d[1], d[0])
    o = (0.0, 0.0)
    ob = (o[0] + 40.0 * n[0], o[1] + 40.0 * n[1])

    def fp(s):
        return (o[0] + s * d[0], o[1] + s * d[1])

    def bp(s):
        return (ob[0] + s * d[0], ob[1] + s * d[1])

    same = tot = 0
    detail = []
    for (sp, sb, sc, sd_) in [(10, 4, 20, 20), (10, 16, 20, 20), (10, 16, 30, 30),
                              (10, 16, 12, 12), (10, 10, 20, 20), (10, 4, 8, 8)]:
        a = w40.eval_lot(fp(sp), bp(sb), fp(sc), bp(sd_), o, d, n)
        b = eval_exact(fp(sp), bp(sb), fp(sc), bp(sd_), o, d, n, ob, d, +1,
                       use_adv=False, use_foot=False, use_pair=True)
        tot += 1
        eq = (a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3])
        same += int(eq)
        detail.append((sp, sb, sc, a[0], a[3], b[3], eq))
    ok["①"] = (same == tot)
    P("  ① **三旗全關 == `w40.eval_lot`**（⛔ 非重造判定式）：逐格四項全同 ＝ **%d ／ %d** ⇒ %s"
      % (same, tot, "PASS" if ok["①"] else "🔴 FAIL"))
    P("     🔒 已知【甲】(P_prev=10,B_prev=4) ⇒ %s／已知【乙】(10,16) ⇒ %s／"
      "已知【合格】(本宗 30) ⇒ %s／**已知【不合格】(本宗 12)** ⇒ %s"
      % (detail[0][3], detail[1][3], detail[2][4], detail[3][4]))

    # ② **推進向定序**之判別力：造一組「右側鏡像」，舊形判不合格、新形判合格
    #    ⛔ 且須另造一組新形**仍判不合格**者 ⇒ 證新形之計數非恆 0（常設 8）
    #    右側：推進 ＝ s 遞減 ⇒ adv = −1
    a_old = w40.eval_lot(fp(100), bp(96), fp(88), bp(85), o, d, n)
    a_new = eval_exact(fp(100), bp(96), fp(88), bp(85), o, d, n, ob, d, -1,
                       use_adv=True, use_foot=True, use_pair=True)
    b_old = w40.eval_lot(fp(100), bp(96), fp(98), bp(95), o, d, n)
    b_new = eval_exact(fp(100), bp(96), fp(98), bp(95), o, d, n, ob, d, -1,
                       use_adv=True, use_foot=True, use_pair=True)
    ok["②"] = (a_old[3] == "不合格" and a_new[3] == "合格"
               and b_old[3] == "不合格" and b_new[3] == "不合格")
    P("  ② **推進向定序之判別力**（右側鏡像·`adv=−1`）：")
    P("     (a) 已推進過頭 (P_cur s=88 < B_prev s=96)：舊 **%s** ／ 新 **%s**（期望 不合格／合格）"
      % (a_old[3], a_new[3]))
    P("     (b) **未推進足夠** (P_cur s=98 > B_prev s=96)：舊 **%s** ／ 新 **%s**（期望 不合格／**不合格**）"
      % (b_old[3], b_new[3]))
    P("     ⇒ 🔒 **新形之「不合格」計數⛔ 非恆 0**（(b) 即會使它為否之輸入）⇒ %s"
      % ("PASS" if ok["②"] else "🔴 FAIL"))

    # ③ **實算垂足**之自檢：垂足須保 `s`（已知真）；沿**非法向**之投影則不保（已知偽）
    Pv = fp(10.0)
    Bf = w40.line_isect(Pv, n, ob, d)
    res_ok = abs(w40.s_of(Bf, o, d) - w40.s_of(Pv, o, d))
    skew = _u((n[0] + 0.30 * d[0], n[1] + 0.30 * d[1]))
    Bs = w40.line_isect(Pv, skew, ob, d)
    res_bad = abs(w40.s_of(Bs, o, d) - w40.s_of(Pv, o, d))
    ulp_s = math.ulp(10.0)
    ok["③"] = (res_ok <= 10 * ulp_s and res_bad > 1.0)
    P("  ③ **實算垂足**：沿 **FRONTLINE 法向**之垂足 ⇒ `|Δs|` ＝ **%.3e**（`ulp(10)=%.3e`·**殘差/ulp ＝ %.2f**）"
      % (res_ok, ulp_s, res_ok / ulp_s))
    P("     🔒 **已知偽之對照**（沿偏 0.30 之非法向）⇒ `|Δs|` ＝ **%.3e**（須 ≫ 0）⇒ %s"
      % (res_bad, "PASS" if ok["③"] else "🔴 FAIL"))

    # ④ `_PAR_TOL` 自 `w86` 原樣取（⛔ 不重造·⛔ 不抄寫）
    t_ast, t_re = w86._par_tol_from_code()
    ok["④"] = (t_ast == t_re == PAR_TOL == 1e-6)
    P("  ④ **`_PAR_TOL` 原樣自 `w86` 取**（⛔ 不重造）：`ast` ＝ %.1e ／ `regex` ＝ %.1e ／ 本檔用 %.1e ⇒ %s"
      % (t_ast, t_re, PAR_TOL, "PASS" if ok["④"] else "🔴 FAIL"))

    # ⑤ 第十三法之判別力（合成模組：迴圈標頭 2 筆 ＋ **誘餌 3 筆在迴圈體與他處**）
    syn = (
        "DECOY = ('d1.py', 'd2.py')\n"
        "def main():\n"
        "    for f in ('fixture_a.py',\n"
        "              'fixture_b.py'):\n"
        "        run('decoy_in_body.py')\n"
        "    return DECOY\n"
    )
    n13, l13, _rng = run_all_count_method13(syn, "<syn>")
    n_all = len(re.findall(r'["\']([A-Za-z0-9_./]+\.py)["\']', syn))
    ok["⑤"] = (n13 == 2 and n_all == 5)
    P("  ⑤ **第十三法之判別力（常設 8）**：合成模組（迴圈**標頭** 2 筆 ＋ **誘餌 3 筆**於迴圈體與模組級）")
    P("     ⇒ **第十三法 ＝ %d**（期望 2·名單 %s）／全檔文本法（① 族）＝ **%d**（期望 5）⇒ %s"
      % (n13, l13, n_all, "PASS" if ok["⑤"] else "🔴 FAIL"))
    P("     🔒 ⇒ **二法之受詞確實不同**（⛔ 非同族）——本法之受詞 ＝ `co_lines()` 之 `offset→lineno` 映射")

    # ⑥ 常設 9：門檻之量級與 ulp
    P("  ⑥ **常設 9**：`PAR_TOL = %.1e` 施於 `|sin|` ∈ [0,1]（`ulp(1.0) = %.3e`）⇒ 門檻/ulp ＝ %.3e；"
      "`TOL_ORD = %.1e` 施於 `s` 之差（量級 ~1e2·`ulp(1e2) = %.3e`）⇒ 門檻/ulp ＝ %.3e"
      % (PAR_TOL, math.ulp(1.0), PAR_TOL / math.ulp(1.0),
         TOL_ORD, math.ulp(1e2), TOL_ORD / math.ulp(1e2)))

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
    P("【W-G.9-87 §二 A 組】`K-9-9 二` 之精確實作／三項更正之消融／斜跨距之來源／`D-0` 二項補辦")
    P("=" * W)
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s | numpy %s"
      % (shapely.__version__, shapely.geos_version, np.__version__))
    P("  🔒 A-0 **事前選定：偏向<u>保留違反</u>**（甲/乙/丙 三條見 docstring）")
    P("  🔴 **門檻 ＝ 正典之 `_PAR_TOL = %.1e`**（`K-6:1010`·原樣自 `w86` 取·⛔ 不另立）" % PAR_TOL)
    P("  🔒 情境母體 ＝ **僅 %gm**（⛔ 不擴·具名）" % SB)

    if not selfcheck(P):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    # ── 驅動（同 `-86` 之構造·其寫在 `main()` 內⛔ 不可 import·逐字具名之差）──
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
    P("【驅動】`%gm` × R1–R6——攔截 **%d 格**；`side_lines_by_side` 之街廓數 ＝ **%d**"
      % (SB, len(REAL), len(SLM)))

    CELL = {}
    for rec in REAL:
        lbl = rec["label"]
        fl, bl = FL.get(lbl) or {}, BL.get(lbl) or {}
        if not (fl.get("p1") and fl.get("p2")) or bl.get("point") is None:
            continue
        o_ = tuple(float(x) for x in fl["p1"])
        p2_ = tuple(float(x) for x in fl["p2"])
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
            Pc = Bc = None
            if ua is not None:
                Pc = w40.line_isect(tuple(pa), tuple(ua), o_, d_)
                Bc = w40.line_isect(tuple(pa), tuple(ua), bpt, bdir)
            lots[i] = {"ua": ua, "pa": pa, "Pc": Pc, "Bc": Bc,
                       "s_lo": IV[i][0], "s_hi": IV[i][1],
                       "area": float(rec["biz"][i].area), "is_corner": i in meta["corners"]}
        CELL[lbl] = {"rec": rec, "o": o_, "p2": p2_, "d": d_, "n": n_, "bpt": bpt, "bdir": bdir,
                     "groups": groups, "lots": lots, "meta": meta, "rows": rows,
                     "sl": SLM.get(lbl) or {}}

    # ══ 推進向 `adv`：二源 ＋ 逐格對拍（⛔ 禁硬編街廓名／側別）═════════════
    P("")
    P("【A-1-0】**推進向 `adv` 之二源對拍**（`K-6:2115`／`:2158`·⛔ 禁硬編）")
    P("-" * W)
    P("  🔒 **源甲**（＝ `-85` 之法·原樣）：同格二組中，**平均 `s` 較小者** ＝ 左組 ⇒ `adv=+1`；另一組 `adv=−1`")
    P("  🔒 **源乙**（本批新取·⛔ 獨立資料）：`cad['side_lines_by_side'][街廓]` 之 `left`／`right`"
      "（其側別由 `app.py` 依 **FRONT p1→p2** 導出）⇒ 組之平均 `s` 距何側之 SIDE_LINE 較近")
    P("  %-5s %-8s %-9s %-11s %-11s %-11s %-9s %-9s %-8s"
      % ("街廓", "側", "宗數", "組平均 s", "SIDE左 s", "SIDE右 s", "源甲 adv", "源乙 adv", "一致?"))
    ADV = {}
    adv_rows = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        s_mid = {}
        for sd, ix in C["groups"]:
            v = [(C["lots"][i]["s_lo"] + C["lots"][i]["s_hi"]) / 2.0 for i in ix]
            s_mid[sd] = (sum(v) / len(v)) if v else float("nan")
        sl_s = {}
        for key in ("left", "right"):
            e = (C["sl"] or {}).get(key)
            if not e:
                continue
            pts = e.get("pts") or [e.get("p1"), e.get("p2")]
            pts = [p for p in pts if p is not None]
            if not pts:
                continue
            vv = [w40.s_of((float(p[0]), float(p[1])), C["o"], C["d"]) for p in pts]
            sl_s[key] = sum(vv) / len(vv)
        # 🔒 **源乙逐格決定**（⛔ 不得靜默取號·反靜默退路）：
        #    二側皆有 SIDE_LINE ⇒ 各組取較近之側；只有一側 ⇒ 較近之組取該側、另一組取其反；
        #    單組 ＋ 單側 ⇒ ⛔ **不判**（`adv_b = None`）·具名。
        gk = [sd for sd, _ix in C["groups"]]
        advb = {}
        if len(sl_s) == 2:
            for sd in gk:
                advb[sd] = (+1 if abs(s_mid[sd] - sl_s["left"])
                            <= abs(s_mid[sd] - sl_s["right"]) else -1)
        elif len(sl_s) == 1 and len(gk) == 2:
            key = next(iter(sl_s))
            near = min(gk, key=lambda z: abs(s_mid[z] - sl_s[key]))
            other = [z for z in gk if z != near][0]
            advb[near] = +1 if key == "left" else -1
            advb[other] = -advb[near]
        for sd, ix in C["groups"]:
            is_low = all(not math.isfinite(s_mid[k2]) or s_mid[sd] <= s_mid[k2] for k2 in s_mid)
            adv_a = +1 if is_low else -1
            adv_b = advb.get(sd)
            agree = (adv_b is None) or (adv_a == adv_b)
            # 🔒 A-0 (丙)：二源不一致 ⇒ 取**使該宗仍判違反**之號 ⇒ 於本案即取 `+1`（＝ 舊形之定序）
            use = adv_a if agree else +1
            ADV[(lbl, sd)] = {"a": adv_a, "b": adv_b, "use": use, "agree": agree}
            adv_rows.append((lbl, sd, len(ix), s_mid[sd], sl_s.get("left"), sl_s.get("right"),
                             adv_a, adv_b, agree))
            P("  %-5s %-8s %-9d %-11.4f %-11s %-11s %-9s %-9s %-8s"
              % (lbl, sd, len(ix), s_mid[sd],
                 ("%.4f" % sl_s["left"]) if "left" in sl_s else "—",
                 ("%.4f" % sl_s["right"]) if "right" in sl_s else "—",
                 "+1" if adv_a > 0 else "−1",
                 ("—" if adv_b is None else ("+1" if adv_b > 0 else "−1")),
                 "✅" if agree else "🔴 **不一致**"))
    POP(len(adv_rows), len(adv_rows), "A-1-0 逐 (街廓, 側)（全列）")
    n_b = sum(1 for r in adv_rows if r[7] is not None)
    n_ag = sum(1 for r in adv_rows if r[8] and r[7] is not None)
    P("  🔒 **二源皆可取者 ＝ %d ／ %d**；其中**一致 ＝ %d**；⛔ 源乙取不到者 ＝ %d（該格缺 SIDE_LINE·具名）"
      % (n_b, len(adv_rows), n_ag, len(adv_rows) - n_b))
    P("  🔒 **常設 14 ③（判別力為零者）**：源乙取不到之格，對「二源是否一致」之判別力 ＝ **0** ⇒ %d 筆"
      % (len(adv_rows) - n_b))

    # ══ 逐宗之基礎列（含 `-86` 之舊形·負對照）═══════════════════════════
    ROWS = []
    same_old = tot_old = 0
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
                    continue
                pv = C["lots"][prev]
                adv = ADV[(lbl, side)]["use"]
                old = w40.eval_lot(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"], o_, d_, n_)
                ref = eval_exact(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"], o_, d_, n_,
                                 C["bpt"], C["bdir"], adv, False, False, True)
                tot_old += 1
                same_old += int(old[0] == ref[0] and old[1] == ref[1]
                                and old[2] == ref[2] and old[3] == ref[3])
                r = {"lbl": lbl, "side": side, "i": i, "prev": prev, "adv": adv,
                     "area": lt["area"], "old": old,
                     "sin": _sin(lt["ua"], pv["ua"]),
                     "s_Pprev": w40.s_of(pv["Pc"], o_, d_), "s_Bprev": w40.s_of(pv["Bc"], o_, d_),
                     "s_Pcur": w40.s_of(lt["Pc"], o_, d_), "s_Bcur": w40.s_of(lt["Bc"], o_, d_)}
                r["slant_prev"] = abs(r["s_Pprev"] - r["s_Bprev"])
                r["slant_cur"] = abs(r["s_Pcur"] - r["s_Bcur"])
                for tag, (fa, fb, fc) in (("000", (0, 0, 0)), ("100", (1, 0, 0)),
                                          ("010", (0, 1, 0)), ("001", (0, 0, 1)),
                                          ("110", (1, 1, 0)), ("101", (1, 0, 1)),
                                          ("011", (0, 1, 1)), ("111", (1, 1, 1))):
                    r[tag] = eval_exact(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"], o_, d_, n_,
                                        C["bpt"], C["bdir"], adv, bool(fa), bool(fb), bool(fc))
                r["111s"] = eval_exact(pv["Pc"], pv["Bc"], lt["Pc"], lt["Bc"], o_, d_, n_,
                                       C["bpt"], C["bdir"], adv, True, True, True, strict=True)
                ROWS.append(r)
                prev = i
    P("")
    P("  🔒 **`eval_exact(000·丙)` 與 `w40.eval_lot` 之逐位對拍**：逐宗四項全同 ＝ **%d ／ %d** ⇒ %s"
      % (same_old, tot_old, "✅ **⛔ 非重造判定式**" if same_old == tot_old
         else "🔴 **有不同 ⇒ 本檔之判定⛔ 不得採信·具名**"))

    inscope = [r for r in ROWS if math.isfinite(r["sin"]) and r["sin"] > PAR_TOL]
    outscope = [r for r in ROWS if not (math.isfinite(r["sin"]) and r["sin"] > PAR_TOL)]

    # ══ 【C／A-1】精確實作與重判 ═══════════════════════════════════════
    P("")
    P("【C／A-1】🛑 **`K-9-9 二` 之精確實作與重判**（母體 ＝ **%d 宗**·⛔ 不縮）" % len(ROWS))
    P("-" * W)
    P("  🔒 **三項更正**（逐字錨）：甲 定序依推進方向（`:2115–2116`／`:2158`）／"
      "乙 實算垂足（`:2119–2120`）／丙 逐端點對應比較（`:2121–2122`／`:2126–2132`）")
    P("  🔒🔒 **本表之一切 `s` 皆為 `s_adv`（推進向框·右組 ＝ 原 `s` 之負）**"
      "——⛔ 不得與 `-86` 之原框 `s` 直接相減（`-85` §I-2 之框錯教訓）")
    P("  %-5s %-5s %-4s %-4s %-6s %12s %12s %13s %13s %13s %13s %12s %12s %-8s"
      % ("街廓", "側", "i", "前", "情形", "s(P_prev)", "s(B_prev)", "B⊥ 之 s", "P⊥ 之 s",
         "起算front", "起算base", "Δ_front′", "Δ_base′", "出艙碼"))
    bad111 = [r for r in ROWS if r["111"][3] == "不合格"]
    for r in ROWS:
        c, st, df, code, feet = r["111"]
        if c is None:
            P("  %-5s %-5s %-4d %-4d ⛔ %s" % (r["lbl"], r["side"], r["i"], r["prev"], code))
            continue
        _sg = 1.0 if r["adv"] > 0 else -1.0
        _C = CELL[r["lbl"]]
        P("  %-5s %-5s %-4d %-4d %-6s %12.4f %12.4f %13.6e %13.6e %13.6e %13.6e %12.6e %12.6e %-8s"
          % (r["lbl"], r["side"], r["i"], r["prev"], c,
             _sg * r["s_Pprev"], _sg * r["s_Bprev"],
             _sg * w40.s_of(feet["Bperp"], _C["o"], _C["d"]),
             _sg * w40.s_of(feet["Pperp"], _C["o"], _C["d"]),
             st[0], st[1], df[0], df[1],
             ("🔴 不合格" if code == "不合格" else "✅ 合格")))
    POP(len(ROWS), len(ROWS), "A-1 正典逐字重判（全列）")

    P("")
    P("  🔒 **垂足之<u>坐標</u>（施工單 A-1 明令『含垂足坐標』·⛔ 非只給 `s`）**")
    P("  %-5s %-5s %-4s %-4s %26s %26s"
      % ("街廓", "側", "i", "前", "B⊥ (x, y)", "P⊥ (x, y)"))
    _nf = 0
    for r in ROWS:
        ft = r["111"][4]
        if ft["Bperp"] is None or ft["Pperp"] is None:
            _nf += 1
            P("  %-5s %-5s %-4d %-4d ⛔ 垂足求不出·具名"
              % (r["lbl"], r["side"], r["i"], r["prev"]))
            continue
        P("  %-5s %-5s %-4d %-4d %26s %26s"
          % (r["lbl"], r["side"], r["i"], r["prev"],
             "(%.4f, %.4f)" % (ft["Bperp"][0], ft["Bperp"][1]),
             "(%.4f, %.4f)" % (ft["Pperp"][0], ft["Pperp"][1])))
    POP(len(ROWS), len(ROWS), "A-1 垂足坐標（全列）")
    P("     🔒 **垂足求不出者 ＝ %d**（⛔ 靜默退路之反面：計數為 0 亦須印出）" % _nf)

    P("")
    P("  🔒 **垂足實算 vs 舊形之壓縮**（`|s(B⊥) − s(P_prev)|`／`|s(P⊥) − s(B_prev)|`·**應為零**）：")
    fb = [r["111"][4]["res_B"] for r in ROWS if r["111"][4]["Bperp"] is not None]
    fpp = [r["111"][4]["res_P"] for r in ROWS if r["111"][4]["Pperp"] is not None]
    if fb:
        P("     極大 `|Δs(B⊥)|` ＝ **%.3e**（`ulp(1e2) = %.3e`·**殘差/ulp ＝ %.2f**）；"
          "極大 `|Δs(P⊥)|` ＝ **%.3e**（**殘差/ulp ＝ %.2f**）"
          % (max(fb), math.ulp(1e2), max(fb) / math.ulp(1e2),
             max(fpp), max(fpp) / math.ulp(1e2)))
        P("     ⇒ 🔒 **法向投影保 `s`** ⇒ **更正乙⛔ 不改任何 `s`**（⇒ 其單獨施用之效果見 §D 組②）")
    P("")
    bad_in = [r for r in inscope if r["111"][3] == "不合格"]
    P("  🔴 **必答：`K-9-9 二`（受詞經 `K-9-14` 限縮）之違反宗數 ＝ %d**"
      "（受詞內 ＝ %d 宗／受詞外 ＝ %d 宗）" % (len(bad_in), len(inscope), len(outscope)))
    for r in bad_in:
        c, st, df, code, _f = r["111"]
        ends = []
        if df[0] < -TOL_ORD:
            ends.append("`P` 端")
        if df[1] < -TOL_ORD:
            ends.append("`B` 端")
        P("     🔴 %-4s %-4s i=%-3d（前 %d·情形 %s）違反端 ＝ **%s**；"
          "`Δ_front′` ＝ %.6e／`Δ_base′` ＝ %.6e；面積 %.4f ㎡"
          % (r["lbl"], r["side"], r["i"], r["prev"], c, "／".join(ends) or "（無·容差內）",
             df[0], df[1], r["area"]))
    POP(len(inscope), len(bad_in), "A-1 受詞內之違反宗（全列）")
    P("     面積合計（帶號）＝ **%.4f ㎡**／（絕對值）＝ **%.4f ㎡**"
      % (sum(r["area"] for r in bad_in), sum(abs(r["area"]) for r in bad_in)))
    P("  🔒 **受詞外之違反宗數 ＝ %d**（⛔ 非本則之受詞·`K-9-14` 已排除·具名）"
      % sum(1 for r in outscope if r["111"][3] == "不合格"))
    P("  🔒 **A-0 (乙) 之保留違反解讀**：改以**嚴格 `>= 0`** 判 ⇒ 受詞內違反 ＝ **%d**／全體 ＝ **%d**"
      "（現行容差 `-1e-6` 下為 %d／%d）⇒ 翻面 **%d** 筆"
      % (sum(1 for r in inscope if r["111s"][3] == "不合格"),
         sum(1 for r in ROWS if r["111s"][3] == "不合格"),
         len(bad_in), len(bad111),
         sum(1 for r in ROWS if r["111s"][3] != r["111"][3])))

    # 負對照
    bad_old_in = [r for r in inscope if r["old"][3] == "不合格"]
    P("")
    P("  🔒 **負對照（常設 8·⛔ 不可省）**：以**舊形**（`w40.eval_lot` 原樣）重跑同一母體")
    P("     ⇒ 受詞內之違反 ＝ **%d 宗**：%s"
      % (len(bad_old_in), "／".join("%s%s%d" % (r["lbl"], r["side"], r["i"]) for r in bad_old_in)))
    P("     面積合計 ＝ **%.4f ㎡** ⇒ %s"
      % (sum(r["area"] for r in bad_old_in),
         "✅ **仍得 3 宗 ⇒ 改動確實改變結果·同源可比**" if len(bad_old_in) == 3
         else "🔴 **⛔ 非 3 宗 ⇒ 負對照不成立·具名**"))

    # ══ 【D／A-2】三項更正之消融 ═══════════════════════════════════════
    P("")
    P("【D／A-2】🔴 **三項更正之消融**（`2³ = 8` 組·⛔ 全出艙）")
    P("-" * W)
    P("  %-6s %-7s %-7s %-9s %11s %11s %11s %11s %-28s"
      % ("組", "甲定序", "乙垂足", "丙對應端點", "違反(全體)", "違反(受詞內)",
         "違反(左側)", "違反(右側)", "與 ⓪ 之差"))
    COMB = [("⓪", "000"), ("①", "100"), ("②", "010"), ("③", "001"),
            ("④", "110"), ("⑤", "101"), ("⑥", "011"), ("⑦", "111")]
    base_n = None
    abl = {}
    for nm, tag in COMB:
        bad = [r for r in ROWS if r[tag][3] == "不合格"]
        bin_ = [r for r in inscope if r[tag][3] == "不合格"]
        bl_ = [r for r in bad if r["side"] == "左"]
        br_ = [r for r in bad if r["side"] == "右"]
        if base_n is None:
            base_n = len(bad)
        abl[tag] = {"all": len(bad), "in": len(bin_), "L": len(bl_), "R": len(br_),
                    "names": ["%s%s%d" % (r["lbl"], r["side"], r["i"]) for r in bad]}
        P("  %-6s %-7s %-7s %-9s %11d %11d %11d %11d %-28s"
          % (nm, "✓" if tag[0] == "1" else "✗", "✓" if tag[1] == "1" else "✗",
             "✓" if tag[2] == "1" else "✗", len(bad), len(bin_), len(bl_), len(br_),
             ("＝ ⓪" if len(bad) == base_n else "%+d" % (len(bad) - base_n))))
    POP(len(COMB), len(COMB), "A-2 消融（8 組全列·施工單只令 5 組）")
    P("")
    P("  🔴 **必答：右側 `22／22` 之簽名由哪一項更正消除？**")
    r0 = abl["000"]["R"]
    for nm, tag in COMB[:4]:
        P("     組 %s（%s）：右側違反 ＝ **%d ／ %d**（⓪ 為 %d）⇒ %s"
          % (nm, tag, abl[tag]["R"], sum(1 for r in ROWS if r["side"] == "右"), r0,
             "**已消除**" if abl[tag]["R"] < r0 else "⛔ 未消除"))
    solo = [nm for nm, tag in COMB[1:4] if abl[tag]["all"] != abl["000"]["all"]]
    P("  🔒 **判別力（施工單 §二 A-2）**：①②③ 三組中，**違反宗數 ≠ ⓪** 者 ＝ %s"
      % (("／".join(solo)) if solo else "**無**（三項各自無效·僅其交互有效 ⇒ 具名）"))
    P("  🔒 **名單差集**（⓪ ∖ ⑦ ／ ⑦ ∖ ⓪）：")
    s0, s7 = set(abl["000"]["names"]), set(abl["111"]["names"])
    P("     ⓪ ∖ ⑦ ＝ %d 宗：%s" % (len(s0 - s7), sorted(s0 - s7)))
    P("     ⑦ ∖ ⓪ ＝ %d 宗：%s" % (len(s7 - s0), sorted(s7 - s0)))

    # ══ 【E／A-3】斜跨距之來源 ═════════════════════════════════════════
    P("")
    P("【E／A-3】🔴 **斜跨距之來源：`BASELINE ∦ FRONTLINE` 之量**")
    P("-" * W)
    P("  %-5s %14s %12s %-9s %14s %14s %14s %-6s"
      % ("街廓", "|sin(BASE,FRONT)|", "夾角(°)", "> PAR_TOL?",
         "斜跨距 min", "斜跨距 中位", "斜跨距 max", "宗數"))
    e3 = []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        sn = abs(C["d"][0] * C["bdir"][1] - C["d"][1] * C["bdir"][0])
        sl = sorted([abs(w40.s_of(C["lots"][i]["Pc"], C["o"], C["d"])
                         - w40.s_of(C["lots"][i]["Bc"], C["o"], C["d"]))
                     for i in C["lots"]
                     if C["lots"][i]["Pc"] is not None and C["lots"][i]["Bc"] is not None])
        if not sl:
            P("  %-5s ⛔ 無可算之宗 ⇒ 具名" % lbl)
            continue
        med = sl[len(sl) // 2] if len(sl) % 2 else (sl[len(sl) // 2 - 1] + sl[len(sl) // 2]) / 2
        e3.append({"lbl": lbl, "sin": sn, "min": sl[0], "med": med, "max": sl[-1], "n": len(sl)})
        P("  %-5s %14.6e %12.6f %-9s %14.6e %14.6e %14.6e %-6d"
          % (lbl, sn, math.degrees(math.asin(min(1.0, sn))),
             "✅ 是" if sn > PAR_TOL else "🔴 否(平行)", sl[0], med, sl[-1], len(sl)))
    POP(len(e3), len(e3), "A-3 逐街廓（全列）")
    par = [x for x in e3 if x["sin"] <= PAR_TOL]
    P("  🔒 **判別力（常設 8）**：`∠(BASELINE, FRONTLINE) ≤ PAR_TOL`（真平行）之街廓 ＝ **%d 格**" % len(par))
    if par:
        for x in par:
            P("     🔒 %s：`|sin|` ＝ %.3e（平行）而**斜跨距仍 ＝ [%.6e, %.6e]** ⇒ "
              "✅ **斜跨距⛔ 非僅由 `BASELINE ∦ FRONTLINE` 而來**"
              % (x["lbl"], x["sin"], x["min"], x["max"]))
    else:
        P("     ⛔ **六格皆不平行 ⇒ 該判別力<u>無母體</u>·具名**（⛔ 不得以「無反例」充作已證）")
        P("     🔒 併出艙**最接近翻面者**（節 103）：`|sin|` 之極小 ＝ **%.6e**（%s·門檻 %.1e·餘裕 %.3e）"
          % (min(x["sin"] for x in e3),
             min(e3, key=lambda x: x["sin"])["lbl"], PAR_TOL,
             min(x["sin"] for x in e3) - PAR_TOL))
    P("  🔒 **與 `-86` 之對照**：`-86` §C-4 表身之 `本宗斜跨距` 域 ＝ [%.6e, %.6e]（本批全體）"
      % (min(x["min"] for x in e3), max(x["max"] for x in e3)))

    # 🔴 **CC 自補（⛔ 施工單未令）**：以**閉式恆等式**直接判斜跨距之來源
    P("")
    P("  🔴 **CC 自補（⛔ 施工單未令）：斜跨距之<u>閉式</u>**——上開判別力無母體，"
      "改以恆等式直接判其來源：")
    P("     🔒 **精確式**：`B_cur − P_cur ＝ t·û` ⇒ `Δs ＝ t⟨û,d̂⟩`、`h ＝ t⟨û,n̂⟩`"
      "（`h` ＝ **`B_cur` 相對 FRONTLINE 之法向距**）⇒ `斜跨距 ≡ |h(B_cur)| × |⟨û,d̂⟩| / |⟨û,n̂⟩|`")
    P("     🔒 **該式⛔ 不含 `∠(BASELINE, FRONTLINE)`** ⇒ 殘差 ≈ 0 即證斜跨距源自"
      "**遠側界自身相對 FRONTLINE 之傾斜**，⛔ 非 BASELINE 之不平行")
    P("     🩸 **首版之誤（記入 §I）**：我原取 `D_local`（自 **`P_cur`** 量之垂距）⇒ 殘差極大 `1.943e-02`；"
      "🔒 **該殘差正是 `BASELINE ∦ FRONTLINE` 之貢獻**（`P_cur` 與 `B_cur` 二點之法向距不等）⇒ 本表一併出艙之")
    P("  %-5s %-4s %14s %14s %14s %14s %14s %14s"
      % ("街廓", "i", "斜跨距(實測)", "精確式", "精確式殘差", "|h|",
         "**BASE不平行項**", "殘差/ulp(座標)"))
    e3b, e3b_res = [], []
    for lbl in sorted(CELL):
        C = CELL[lbl]
        for i in sorted(C["lots"]):
            lt = C["lots"][i]
            if lt["Pc"] is None or lt["Bc"] is None or lt["ua"] is None:
                continue
            uu = lt["ua"]
            ud = uu[0] * C["d"][0] + uu[1] * C["d"][1]
            un = uu[0] * C["n"][0] + uu[1] * C["n"][1]
            if abs(un) < 1e-15:
                P("  %-5s %-4d ⛔ `⟨û, n̂⟩` ≈ 0（遠側界 ∥ FRONTLINE）⇒ 閉式不適用·具名" % (lbl, i))
                continue
            Xp, Xb = lt["Pc"], lt["Bc"]
            # 🔒 `h` ＝ **`B_cur`** 相對 FRONTLINE 之法向距（⛔ 非自 `P_cur` 量者）
            h = ((Xb[0] - C["o"][0]) * C["n"][0] + (Xb[1] - C["o"][1]) * C["n"][1])
            # 🔒 `D_local` ＝ 自 `P_cur` 沿 `n̂` 至 BASELINE 之垂距（首版所用者·⛔ 非精確式之項）
            Bfoot = w40.line_isect(Xp, C["n"], C["bpt"], C["bdir"])
            D_local = (math.hypot(Bfoot[0] - Xp[0], Bfoot[1] - Xp[1])
                       if Bfoot is not None else float("nan"))
            meas = abs(w40.s_of(lt["Pc"], C["o"], C["d"])
                       - w40.s_of(lt["Bc"], C["o"], C["d"]))
            pred = abs(h) * abs(ud) / abs(un)
            res = abs(meas - pred)
            base_term = abs(abs(h) - D_local) * abs(ud) / abs(un)
            # 🔒 **分層（常設 9）**：本量係由**絕對座標**上之二次直線求交所得
            #    ⇒ 分母取 `ulp(座標量級)`，⛔ 非 `ulp(結果量級)`（首版之框錯·§I）
            coord = max(abs(Xp[0]), abs(Xp[1]), abs(Xb[0]), abs(Xb[1]))
            up = math.ulp(coord)
            e3b.append((lbl, i, meas, pred, res, abs(h), base_term, res / up))
            e3b_res.append(res / up)
    for row in e3b[:8]:
        P("  %-5s %-4d %14.6e %14.6e %14.3e %14.6f %14.3e %12.2f" % row)
    POP(len(e3b), min(8, len(e3b)), "A-3 斜跨距閉式（前 8 列·全體統計見下）")
    if e3b:
        _mx = max(e3b, key=lambda z: z[4])
        _mb = max(e3b, key=lambda z: z[6])
        P("     🔒 **常設 9（分層）**：殘差之分母 ＝ `ulp(座標量級 ~3.1e+05) ≈ %.3e`"
          "（⛔ 非 `ulp(斜跨距 ~1e0)`——本量係由絕對座標上之二次直線求交所得）"
          % math.ulp(3.1e5))
        P("     🔒 **精確式之逐宗殘差極大 ＝ %.3e**（%s i=%d·**殘差/ulp(座標) ＝ %.2f**）⇒ %s"
          % (_mx[4], _mx[0], _mx[1], _mx[7],
             "✅ **閉式成立**" if max(e3b_res) <= 1e3 else "🔴 **閉式不成立·具名**"))
        P("     🔴 **二來源之佔比**：`BASELINE ∦ FRONTLINE` 項之極大 ＝ **%.3e**（%s i=%d），"
          "而該宗之斜跨距 ＝ **%.6e** ⇒ 佔 **%.4f%%**"
          % (_mb[6], _mb[0], _mb[1], _mb[2], 100.0 * _mb[6] / _mb[2]))
        P("     ⇒ 🔒 **斜跨距之 %.2f%% 以上來自遠側界之傾斜**，`BASELINE` 之不平行**至多佔 %.4f%%**"
          % (100.0 - 100.0 * _mb[6] / _mb[2], 100.0 * _mb[6] / _mb[2]))
        P("     🔒 **判別力（常設 8·會使它為否之輸入）**：以**錯誤之閉式**"
          "（`|h| × |⟨û,n̂⟩| / |⟨û,d̂⟩|`·分子分母對調）重算 ⇒ 見下列殘差極大")
        _wrong = []
        for lbl in sorted(CELL):
            C = CELL[lbl]
            for i in sorted(C["lots"]):
                lt = C["lots"][i]
                if lt["Pc"] is None or lt["Bc"] is None or lt["ua"] is None:
                    continue
                uu = lt["ua"]
                ud = uu[0] * C["d"][0] + uu[1] * C["d"][1]
                un = uu[0] * C["n"][0] + uu[1] * C["n"][1]
                if abs(ud) < 1e-15 or abs(un) < 1e-15:
                    continue
                Xb2 = lt["Bc"]
                h2 = ((Xb2[0] - C["o"][0]) * C["n"][0] + (Xb2[1] - C["o"][1]) * C["n"][1])
                meas = abs(w40.s_of(lt["Pc"], C["o"], C["d"])
                           - w40.s_of(lt["Bc"], C["o"], C["d"]))
                _wrong.append(abs(meas - abs(h2) * abs(un) / abs(ud)))
        P("     🔒 **錯式之殘差極大 ＝ %.3e**（須 ≫ 正式之 %.3e）⇒ %s"
          % (max(_wrong), _mx[4],
             "✅ 該閘非恆綠" if max(_wrong) > 1e3 * max(_mx[4], 1e-15) else "🔴 判別力不足·具名"))
        P("     🔴 **⇒ 斜跨距之來源 ＝ 遠側界相對 FRONTLINE 之傾斜**"
          "（`|⟨û,d̂⟩| / |⟨û,n̂⟩|` ＝ `cot∠(û, FRONTLINE)`）；"
          "`BASELINE ∦ FRONTLINE` **只使 `D_local` 隨位置變**（⇒ `-86` §I-1 之「斜跨距隨位置變」）")

    # ══ 【F／A-4-1】左側三組跳號 ═══════════════════════════════════════
    P("")
    P("【F／A-4-1】🔴 **左側三組跳號**（`-85` `P6` 之補辦·**中與不中者皆列**）")
    P("-" * W)
    TRI = [("R2", "左"), ("R5", "左"), ("R6", "左")]
    P("  %-5s %-5s %-4s %-4s %14s %14s %14s %-10s %-10s"
      % ("街廓", "側", "i", "前", "推進量", "前宗斜跨距", "推進量−前宗斜跨距", "舊形出艙碼", "⑦ 出艙碼"))
    f1 = []
    for lbl, side in TRI:
        for r in ROWS:
            if r["lbl"] != lbl or r["side"] != side:
                continue
            sgn = 1.0 if r["adv"] > 0 else -1.0
            cur_min = min(sgn * r["s_Pcur"], sgn * r["s_Bcur"])
            prv_min = min(sgn * r["s_Pprev"], sgn * r["s_Bprev"])
            advq = cur_min - prv_min
            gap = advq - r["slant_prev"]
            f1.append({"lbl": lbl, "side": side, "i": r["i"], "adv": advq,
                       "slant": r["slant_prev"], "gap": gap,
                       "old": r["old"][3], "new": r["111"][3]})
            P("  %-5s %-5s %-4d %-4d %14.6e %14.6e %14.6e %-10s %-10s"
              % (lbl, side, r["i"], r["prev"], advq, r["slant_prev"], gap,
                 r["old"][3], r["111"][3]))
    POP(len(f1), len(f1), "A-4-1 左側三組（全列·中與不中皆列）")
    hit = [x for x in f1 if x["old"] == "不合格"]
    mis = [x for x in f1 if x["old"] == "合格"]
    exc_hit = [x for x in hit if not (x["gap"] < 0)]
    exc_mis = [x for x in mis if not (x["gap"] >= 0)]
    P("  🔒 **`P5` 之判**：中者（舊形不合格·%d 宗）須 `推進量 < 前宗斜跨距`（＝ `gap < 0`）⇒ 例外 **%d**；"
      "不中者（%d 宗）須 `gap >= 0` ⇒ 例外 **%d**"
      % (len(hit), len(exc_hit), len(mis), len(exc_mis)))
    for x in exc_hit + exc_mis:
        P("     🔴 例外具名：%s%s i=%d　`gap` ＝ %.6e　舊形 ＝ %s" % (x["lbl"], x["side"], x["i"], x["gap"], x["old"]))
    if hit and mis:
        P("  🔒 **節 103**：中者之 `gap` **極大** ＝ %.6e／不中者之 `gap` **極小** ＝ %.6e"
          % (max(x["gap"] for x in hit), min(x["gap"] for x in mis)))
        P("  🔒 **常設 14 ①（單一門檻）**：本節之分離宣稱以**單一門檻 `gap = 0`** 表述 ⇒ ⛔ 無未定義帶")
    P("  🔒 **常設 14 ③**：`gap` 於二群值域重疊處之筆數（判別力為零者）＝ **%d**"
      % sum(1 for x in hit for y in mis if abs(x["gap"] - y["gap"]) < 1e-12))

    # ══ 【F／A-4-2】`R1 左 j=0` 之雙重異常 ═════════════════════════════
    P("")
    P("【F／A-4-2】🔴 **`R1 左 j=0` 之雙重異常**（`VR-044` 六-4·`-86` §F-2 具名為未答者）")
    P("-" * W)
    P("  🔒 **本批新量之受詞 ＝ `殘差之<u>分子</u>`**（`-86` 只量了 `ulp` 之比·⛔ 未量分子）")
    P("  %-5s %-5s %-4s %13s %13s %14s %13s %12s %13s %13s %-12s"
      % ("街廓", "側", "j", "`S_req`", "殘差(分子)", "殘差/ulp",
         "|sin(uj,uk)|", "|s*|", "d_signed", "|sin(uk,d̂)|", "**破量對/可算對**"))
    f2 = []
    _seen_j = set()
    for r in ROWS:
        lbl, side, j = r["lbl"], r["side"], r["prev"]
        if (lbl, side, j) in _seen_j:
            continue
        _seen_j.add((lbl, side, j))
        C = CELL[lbl]
        a = ADV[(lbl, side)]["use"]
        pj, uj = w82.pj_of(C["rec"], j), w82.uj_of(C["rec"], j)
        if pj is None or uj is None or C["rec"]["block"] is None:
            continue
        edges, _dg = w82.ring_edges(list(C["rec"]["block"].exterior.coords))
        ci = w82.chord_interval(edges, pj, uj)
        rk = next((x for x in C["rows"] if x.get("ok") and x["j"] == j and x["k"] == j + 2), None)
        if rk is None:
            continue
        uk = _u(rk["uk"])
        sA = s_front_of_line(np.asarray(pj, float) + ci["lam_a"] * np.asarray(uj, float),
                             uk, C["o"], C["d"])
        sB = s_front_of_line(np.asarray(pj, float) + ci["lam_b"] * np.asarray(uj, float),
                             uk, C["o"], C["d"])
        if sA is None or sB is None:
            continue
        S_req = max(sA, sB) if a > 0 else min(sA, sB)
        m_hat0, denom0 = strip_axis(C["rec"]["d_hat"], C["rec"]["alloc"])
        m_hat0 = np.asarray(m_hat0, float)[:2]
        bp00 = np.asarray(C["rec"]["corner_pt"], float)[:2]
        sv0 = [float(np.dot(np.asarray(c, float)[:2] - bp00, m_hat0)) / denom0
               for c in list(C["rec"]["biz"][j].exterior.coords)]
        lim_new = max(sv0) if a > 0 else min(sv0)
        res = abs(lim_new - S_req)
        up = math.ulp(abs(S_req)) if math.isfinite(S_req) and S_req else float("nan")
        sn_jk = abs(rk.get("sin_a", float("nan")))
        st_ = abs(rk.get("s_star", float("nan")))
        if a > 0:
            lam_used = ci["lam_b"] if sB >= sA else ci["lam_a"]
        else:
            lam_used = ci["lam_b"] if sB <= sA else ci["lam_a"]
        sin_kd = abs(float(uk[0]) * C["d"][1] - float(uk[1]) * C["d"][0])
        # 🔒 **異常①之量**：該格 `j` 之「現況破量對」數（`s* ∈ λ` 者）／可算對數
        _oks = [x for x in C["rows"] if x["j"] == j and x.get("ok") and x["d"] >= 2]
        _brk = [x for x in _oks if ci["lam_a"] <= x["s_star"] <= ci["lam_b"]]
        f2.append({"lbl": lbl, "side": side, "j": j, "S_req": S_req, "res": res,
                   "ulp": up, "ratio": res / up if up == up and up else float("nan"),
                   "sin_jk": sn_jk, "s_star": st_,
                   "dsig": abs(float(rk.get("d_signed", float("nan")))),
                   "sin_kd": sin_kd, "lam": lam_used,
                   "brk": len(_brk), "pairs": len(_oks)})
        P("  %-5s %-5s %-4d %13.4f %13.3e %14.2f %13.3e %12.4f %13.4f %13.3e %-12s"
          % (lbl, side, j, S_req, res, res / up if up == up and up else float("nan"),
             sn_jk, st_, abs(float(rk.get("d_signed", float("nan")))), sin_kd,
             "%d ／ %d" % (len(_brk), len(_oks))))
    POP(len(f2), len(f2), "A-4-2 有 `S_req` 之格（全列）")
    if f2:
        f2s = sorted(f2, key=lambda x: -x["res"])
        top = f2s[0]
        rest = f2s[1:]
        P("  🔴 **必答①：何以「現況本即 0 對」**——`R1 左 j=0` 之逐對 `s*` 與弦區間：")
        C = CELL["R1"]
        pj0, uj0 = w82.pj_of(C["rec"], 0), w82.uj_of(C["rec"], 0)
        if pj0 is not None and uj0 is not None:
            edges0, _d0g = w82.ring_edges(list(C["rec"]["block"].exterior.coords))
            ci0 = w82.chord_interval(edges0, pj0, uj0)
            P("     弦區間 λ ＝ [%.6f, %.6f]" % (ci0["lam_a"], ci0["lam_b"]))
            npair = 0
            for x in C["rows"]:
                if x["j"] != 0 or not x.get("ok"):
                    continue
                npair += 1
                P("     (0,%d) d=%d  `s*` ＝ %14.4f  `|sin(uj,uk)|` ＝ %.3e  ⇒ `s* ∈ λ` ＝ %s"
                  % (x["k"], x["d"], x["s_star"], abs(x["sin_a"]),
                     ci0["lam_a"] <= x["s_star"] <= ci0["lam_b"]))
            P("     ⇒ 🔒 **可算對 ＝ %d·全部之 `s*` 皆<u>遠在 λ 外</u>** ⇒ 現況即 0 對" % npair)
        P("  🔴 **必答②：`殘差/ulp` 之量級**——🔒 **分子已量**：")
        P("     極大者 ＝ %s%s j=%d：殘差 **%.3e**（`ulp` %.3e·比 %.2f）"
          % (top["lbl"], top["side"], top["j"], top["res"], top["ulp"], top["ratio"]))
        P("     其餘 %d 格之殘差 ∈ [**%.3e**, **%.3e**]（`ulp` ∈ [%.3e, %.3e]）"
          % (len(rest), min(x["res"] for x in rest), max(x["res"] for x in rest),
             min(x["ulp"] for x in rest), max(x["ulp"] for x in rest)))
        P("     🔒 **分子之比 ＝ %.4g**；🔒 **`ulp` 之比 ＝ %.4g** ⇒ **量級差之主因 ＝ 分子**"
          % (top["res"] / max(x["res"] for x in rest),
             top["ulp"] / max(x["ulp"] for x in rest)))
        same_ulp = [x for x in rest if x["ulp"] == top["ulp"]]
        if same_ulp:
            P("     🔒🔒 **判別力（⛔ 不可省）**：`ulp` **與極大者相同**之格 ＝ %d（%s）——"
              "其殘差/ulp ＝ %s ⇒ 🔴 **同 `ulp` 而比值差 %.4g 倍 ⇒ `ulp` ⛔ 不解釋該量級差**"
              % (len(same_ulp), "／".join("%s%s j=%d" % (x["lbl"], x["side"], x["j"]) for x in same_ulp),
                 "／".join("%.2f" % x["ratio"] for x in same_ulp),
                 top["ratio"] / max(x["ratio"] for x in same_ulp)))
        P("  🔒 **`P6` 之判（二異常是否同源）**——🔒 **交叉表**（⛔ 不以「序」暗示因果）：")
        P("     %-14s %-16s %-18s %-16s"
          % ("格", "異常①(破量對＝0?)", "異常②(殘差 > 1e-9?)", "`|sin(uj,uk)|`"))
        a1 = a2 = both = neither = 0
        for x in f2s:
            e1 = (x["brk"] == 0)
            e2 = (x["res"] > 1e-9)
            a1 += int(e1)
            a2 += int(e2)
            both += int(e1 and e2)
            neither += int((not e1) and (not e2))
            P("     %-14s %-16s %-18s %-16.3e"
              % ("%s%s j=%d" % (x["lbl"], x["side"], x["j"]),
                 "✅ 是" if e1 else "⛔ 否", "🔴 是" if e2 else "⛔ 否", x["sin_jk"]))
        P("     🔒 **①成立 ＝ %d 格／②成立 ＝ %d 格／二者皆成立 ＝ %d 格**" % (a1, a2, both))
        cex = [x for x in f2s if x["brk"] == 0 and not (x["res"] > 1e-9)]
        if cex:
            c0 = min(cex, key=lambda z: z["res"])
            P("     🔴🔴 **反例（⇒ ⛔ 不同源）**：%s%s j=%d **①成立（破量對 0／%d）而②不成立**"
              "（殘差 %.3e ＝ 全體**極小**·`|sin(uj,uk)|` %.3e ＝ 全體**極小**）"
              % (c0["lbl"], c0["side"], c0["j"], c0["pairs"], c0["res"], c0["sin_jk"]))
            P("     ⇒ 🔒 **`P6` 🔴 不成立**——①之候選前提（`|sin| 特小` ⇒ `|s*|` 巨大 ⇒ 交點遠在 λ 外）"
              "於該格**成立到極致**，而②**反而最小** ⇒ ⛔ 二異常無共同前提")
        else:
            P("     ⛔ **無反例 ⇒ 判別力無母體·具名**（⛔ 不得以「無反例」充作已證同源）")
        P("     🔒 **常設 14 ③（判別力為零者）**：①②**同時為否**之格 ＝ %d" % neither)

    # 🔒 **與 `-85` log 之逐值對拍**（【倉】錨·⛔ 非抄寫·本檔獨立重算）
    P("")
    P("  🔒 **與 `-85` log 之逐格對拍**（【倉】`verify/out/probe_WG985_grouphead_67cd1a4.log`"
      "·⛔ 本檔獨立重算·⛔ 非抄寫）")
    _p85 = os.path.join(OUTDIR, "probe_WG985_grouphead_67cd1a4.log")
    if os.path.exists(_p85):
        _txt = io.open(_p85, encoding="utf-8", errors="replace").read()
        _pt = re.compile(r'^\s+(R\d+)\s+(\S+)\s+j=(\d+)\s+殘差 ([\d.e+-]+)'
                         r'·\*\*殘差/ulp ＝ ([\d.]+)\*\*', re.M)
        _old = {(m.group(1), m.group(2), int(m.group(3))):
                (float(m.group(4)), float(m.group(5))) for m in _pt.finditer(_txt)}
        P("     舊 log 解析所得格數 ＝ **%d**（🔒 期望 5）" % len(_old))
        _same = _diff = 0
        for x in f2:
            k = (x["lbl"], x["side"], x["j"])
            if k not in _old:
                continue
            o_res, o_rat = _old[k]
            eq = (abs(x["res"] - o_res) <= 5e-4 * max(o_res, 1e-30)
                  and abs(x["ratio"] - o_rat) <= 0.51)
            _same += int(eq)
            _diff += int(not eq)
            P("     %-4s %-4s j=%d  舊 殘差 %.3e／比 %.2f　新 殘差 %.3e／比 %.2f　⇒ %s"
              % (x["lbl"], x["side"], x["j"], o_res, o_rat, x["res"], x["ratio"],
                 "✅ 相符" if eq else "🔴 **不符·具名**"))
        P("     🔒 **相符 ＝ %d ／ %d**（⇒ %s）"
          % (_same, _same + _diff,
             "✅ **獨立復現成立**" if _diff == 0 else "🔴 **有不符 ⇒ 具名**"))
    else:
        P("     ⛔ **`-85` log 不在倉內 ⇒ 無從對拍·具名**")

    # ══ 【G／P7】run_all ＝ 15（第十三法）═══════════════════════════════
    P("")
    P("【G／P7】`run_all` 清單筆數之**第十三法**（🔒 位元組碼**行號映射** × 原始碼文本·⛔ 與十二法不同族）")
    P("-" * W)
    n13, l13, rng = run_all_count_method13()
    P("  母體 ＝ `run_all.py` 之位元組碼；受詞 ＝ **`co_lines()` 之 `offset→lineno` 映射**所定位之"
      "`FOR_ITER` **迴圈標頭**之來源行區間 %s" % (str(rng)))
    P("  🔒 **⛔ 未 `exec`**（僅 `compile`）⇒ ⛔ 未執行 `run_all`（閘 7）")
    for x in l13:
        P("     %s" % x)
    POP(len(l13), len(l13), "第十三法之逐項（全列）")
    P("  ⇒ **第十三法所得 ＝ %d**（施工單 `P7` 期望 **15**）⇒ %s"
      % (n13, "✅ 相符" if n13 == 15 else "🔴 **不符·具名**"))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
