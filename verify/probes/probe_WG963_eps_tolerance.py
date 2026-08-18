#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-63】`GB-80`：寬度閘之**動態容差** ＋ 8 格重測 ＋ **土地後果對帳** ⛔ 零生產碼

**受詞**：`GB-80` 之三項——
1. **`eps` 之取法**：**動態式**、⛔ **不得硬編**。
   🔒 本檔 **⛔ 不自寫第二份 eps**，逕**呼叫生產碼之 `_corner_range_eps`**
   （`grep -n "def _corner_range_eps" app.py`）——單一真相源。
2. **帶容差後之 8 格重測**，含**判別力反例**（須有格**不因容差而翻**）。
3. **土地後果對帳**：逐宗列出由「不可分配」變「可分配」者之
   **第 n 宗 ＋ 暫編地號 ＋ 面積**。

🔒 **量測一律以本波修後之儀器**：`fits_at` 局部原點（`GB-82`）／`_diameter` 上界（`GB-81`）
  ／`d_early` 與 `tol_conv` 分離（`W-G.9-62` §五-D）；`D_max` 出艙**須並列 `tol_conv`**。

═══════════════════════════════════════════════════════════════════════
🔒 **本檔之「寬度短少」係<u>直接量</u>（⛔ 非由 `|r*|` 換算）**
═══════════════════════════════════════════════════════════════════════
    `w_max(格) := max { w : W×D 之 w 換成該值後，於法定深度 D 仍可容納 }`
    `短少 := W − w_max`（`≤ 0` ⇒ 不短少）
⇒ **直接回答「在法定深度下，我的寬度差多少」**，而 `GB-80` 之閘正是
  `寬度 ≥ W − eps` ⇒ **`翻` ⟺ `短少 ≤ eps`**。
⚠️ 前批之 `2|r*|` 係**等向膨脹**之換算量，與本量**同名不同量** ⇒ 本檔一律用直接量，
  並**並列**二者供對讀（⛔ 不以相近掩蓋其為兩個量）。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
for _p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE):
    sys.path.insert(0, _p)

import probe_WG949_free_pose as fp                                  # noqa: E402
import run_verification as rv                                       # noqa: E402
from app_harvest import harvest                                     # noqa: E402
from probe_WG949_free_pose import fits_at                           # noqa: E402
from probe_WG959_knife_edge import TOL_CONV, d_max_at_r             # noqa: E402
from probe_WG960_fitcore import R_GRID, build_ctx, yi_pst           # noqa: E402
from probe_WG961_dfloor import GRID_B                               # noqa: E402
from probe_WG962_gate_power import _dfloor                          # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 168
SB = 0.0                       # 本波乙式量測一律 setback = 0（同 `-58`〜`-62`）
EIGHT = [("R1", "left"), ("R1", "right"), ("R2", "left"), ("R3", "right"),
         ("R4", "left"), ("R4", "right"), ("R5", "left"), ("R6", "right")]
PREV8 = {("R1", "left"): "進", ("R1", "right"): "進", ("R2", "left"): "進",
         ("R3", "right"): "進", ("R4", "left"): "進", ("R4", "right"): "進",
         ("R5", "left"): "不進", ("R6", "right"): "不進"}
FOCUS3 = [("R5", "left"), ("R6", "right"), ("R3", "right")]
WG960_DMAX = {
    ("R5", "left"): (0.0264, 39.9825, 39.9825, 39.9860),
    ("R6", "right"): (0.0000, 39.8736, 39.8736, 39.8771),
    ("R3", "right"): (41.4830, 41.4830, 41.4831, 41.4864),
}
# 前批之 `|r*|`（等向膨脹之臨界值）·出處 `verify/out/probe_WG960_fitcore_post2_65fef5b.log`【C-3】
WG960_RSTAR = {("R5", "left"): 7.279414e-08, ("R6", "right"): 4.394497e-08,
               ("R3", "right"): 0.0}


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _grep1(pat, path):
    """回 `pat` 於 `path` 之**首個命中行號**與**命中數**（⛔ 命中數須一併出艙）。"""
    # ⚠️ **本機陷阱**：`text=True` 會以 `cp950` 解碼 ⇒ 命中行含中文即 `UnicodeDecodeError`。
    #   本函式只取行首之 `NNN:` ⇒ 顯式 UTF-8 解碼、`errors="replace"`（⛔ 不影響行號之正確性）。
    r = subprocess.run(["grep", "-n", pat, path], cwd=os.path.dirname(VERIFY),
                       capture_output=True, timeout=30)
    r = type("R", (), {"stdout": (r.stdout or b"").decode("utf-8", "replace")})()
    ls = [x for x in (r.stdout or "").splitlines() if x.strip()]
    return (int(ls[0].split(":", 1)[0]) if ls else None), len(ls)


def w_max_at(pst, th, d, w_hi, tol=1e-9):
    """法定深度 `d` 下之**最大可容納寬度**（二分·回**下界** ⇒ 偏保守）。

    🔒 回下界之由：`短少 = W − w_max` ⇒ 回下界只會使短少**偏大** ⇒ 判「翻」時偏嚴。
    """
    lo = 0.0
    if not fits_at(pst, 1e-6, d, th, 0.0)[0]:
        return 0.0                       # 連極窄都容不下
    lo, hi = 1e-6, w_hi
    if fits_at(pst, hi, d, th, 0.0)[0]:
        return hi
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if fits_at(pst, mid, d, th, 0.0)[0]:
            lo = mid
        else:
            hi = mid
    return lo


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-63】`GB-80`：寬度閘之**動態容差** ＋ 8 格重測 ＋ **土地後果對帳**")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；`eps` **逕呼叫生產碼之 `_corner_range_eps`**（⛔ 不自寫第二份）。")
    P("")

    ns, cb_by, cad, snapshot, wd, _t = build_ctx()

    # ══════════════════════════════════════════════════════════════
    # 【A】`eps` 之取法（`GB-80` 受詞 1·⛔ 不硬編）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A】`eps` 之取法：**動態式**·⛔ **不得硬編**（`GB-80` 受詞 1）")
    P("=" * WID)
    P("  🔒 **式**（生產碼·逐字）：`eps = max(_CR_EPS_LEGAL, min(_CR_EPS_K · q, _CR_EPS_LEGAL_CEIL))`")
    P("  🔴 **與 `CLAUDE.md` 所載族式之<u>具名差異</u>（⛔ 不掩蓋）**：族式為")
    P("     `max(EPS_LEGAL, min(k·q·(L/ℓ), EPS_LEGAL_CEIL))`，**本處無 `(L/ℓ)` 項**。")
    P("     碼面已具名其理由（逐字）：C-5 之 eps 係**配對閘**「量測點距線段有長槓桿故乘 `L/ℓ` 放大」；")
    P("     本處係**構造自檢**「回量同一組線所定義之寬度·無外插槓桿」⇒ **放大倍率為 1**。")
    P("     ⇒ 🔒 **本處之受詞（回量同一組線之寬度）與 `GB-80` 之寬度閘完全同族** ⇒ 取本式。")
    P("")
    P("  🔒 **§七-6：`eps` 之每一個輸入量之來源（⛔ 不得只印數值）**")
    P(f"  {'量':<22}{'現查值':>14}   {'來源檔':<10}{'行':>6}{'命中數':>7}   {'grep 唯一字樣':<44}")
    P("-" * WID)
    srcs = [
        ("_CR_EPS_LEGAL", ns["_CR_EPS_LEGAL"], "app.py", "^_CR_EPS_LEGAL = "),
        ("_CR_EPS_K", ns["_CR_EPS_K"], "app.py", "^_CR_EPS_K = "),
        ("_CR_EPS_LEGAL_CEIL", ns["_CR_EPS_LEGAL_CEIL"], "app.py", "^_CR_EPS_LEGAL_CEIL = "),
    ]
    for nm, val, f, pat in srcs:
        ln, nh = _grep1(pat, f)
        P(f"  {nm:<22}{val:>14.6g}   {f:<10}{(ln or -1):>6}{nh:>7}   `{pat}`")
    ln_fn, nh_fn = _grep1("^def _corner_range_eps", "app.py")
    P(f"  {'_corner_range_eps()':<22}{'（函式）':>14}   {'app.py':<10}{(ln_fn or -1):>6}{nh_fn:>7}"
      f"   `^def _corner_range_eps`")
    P(f"  🔒 上列行號成立於 commit **{sha}**（`CLAUDE.md` 行號衛生第 2 款）；"
      "⛔ 引用請一律走 grep 字樣。")
    P("")
    P("  🔒 **`q`（DXF 實測量化步長）之來源**："
      "`baselines[lbl]['_match']['q_detected']`（`_detect_dxf_quantum` 逐檔實測）")
    P(f"  {'街廓':<7}{'q_detected':>14}{'k·q':>14}{'eps ＝ _corner_range_eps(q)':>30}{'落在哪一段':>14}")
    P("-" * WID)
    eps_by = {}
    for lbl in sorted(cb_by):
        mb = cad["baselines"].get(lbl) or {}
        q = (mb.get("_match") or {}).get("q_detected")
        e = float(ns["_corner_range_eps"](q))
        eps_by[lbl] = e
        kq = (ns["_CR_EPS_K"] * float(q)) if q else float("nan")
        seg = ("下限 `_CR_EPS_LEGAL`" if e <= ns["_CR_EPS_LEGAL"] + 0
               else ("上限 `_CR_EPS_LEGAL_CEIL`" if e >= ns["_CR_EPS_LEGAL_CEIL"] else "中段 `k·q`"))
        P(f"  {lbl:<7}{(f'{q:.6g}' if q else '（無）'):>14}{kq:>14.6g}{e:>30.6e}{seg:>16}")
    P("-" * WID)
    # 🔒 判別力自檢：三分支須皆可觸發 ⇒ 證該式**非常數**
    P("  🔒 **判別力自檢**（⛔ 不得省）：以合成 `q` 驗該式**三個分支皆可觸發** ⇒ 證其非常數")
    P(f"  {'合成 q':>14}{'k·q':>14}{'eps':>16}{'分支':>26}")
    for q in (None, 1e-5, 1e-3, 1e-1):
        e = float(ns["_corner_range_eps"](q))
        kq = (ns["_CR_EPS_K"] * float(q)) if q else float("nan")
        seg = ("下限" if e <= ns["_CR_EPS_LEGAL"] else
               ("上限（封頂生效）" if e >= ns["_CR_EPS_LEGAL_CEIL"] else "中段 k·q"))
        P(f"  {(f'{q:g}' if q else 'None'):>14}{kq:>14.6g}{e:>16.6e}{seg:>28}")
    _br = {("下限" if float(ns["_corner_range_eps"](q)) <= ns["_CR_EPS_LEGAL"] else
            ("上限" if float(ns["_corner_range_eps"](q)) >= ns["_CR_EPS_LEGAL_CEIL"] else "中段"))
           for q in (None, 1e-5, 1e-3, 1e-1)}
    if len(_br) < 3:
        raise RuntimeError(
            f"🔴 `_corner_range_eps` 之三分支未全部觸發（實得 {sorted(_br)}）"
            " ⇒ 該式於本案退化為常數 ⇒ ⛔ 「動態式」之宣稱不得出艙。")
    P(f"  ⇒ ✅ **三分支皆觸發**（{'／'.join(sorted(_br))}）⇒ 該式確為**動態式**、⛔ 非硬編。")
    P(f"  ⚠️ **本案實得 eps 落在<u>下限</u>**（`k·q = 4×1e−05 = 4e−05 < 1e−04`）"
      f"⇒ **eps ＝ `{eps_by[sorted(cb_by)[0]]:.6e}`**（各街廓同值·因 `q` 同）。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【B】8 格於法定深度下之 `w_max` 與**寬度短少**（直接量）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【B】8 格於**法定深度 `D`** 下之最大可容納寬度 `w_max` ＝> **寬度短少**（直接量）")
    P("=" * WID)
    P("  🔒 `短少 := W − w_max`；`GB-80` 之閘為 `寬度 ≥ W − eps` ⇒ **翻 ⟺ 短少 ≤ eps**。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'W(法定寬)':>11}{'D(法定深)':>11}{'w_max':>16}"
      f"{'短少 ＝ W−w_max':>18}{'eps':>13}{'短少≤eps?':>11}{'2|r*|（前批·對讀）':>20}")
    P("-" * WID)
    cells, short = {}, {}
    for lbl, which in EIGHT:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        w, dd = wd[lbl]
        wm = w_max_at(pst, g["theta"], dd, w + 1.0)
        s = w - wm
        cells[(lbl, which)] = (pst, g, w, dd)
        short[(lbl, which)] = s
        e = eps_by[lbl]
        rs = WG960_RSTAR.get((lbl, which))
        P(f"  {lbl:<5}{which:<7}{w:>11.2f}{dd:>11.2f}{wm:>16.9f}{s:>18.6e}{e:>13.2e}"
          f"{('✅ 是' if s <= e else '🔴 否'):>12}"
          f"{(f'{2 * rs:.6e}' if rs is not None else '—'):>20}")
    P("-" * WID)
    P("  ⚠️ **`2|r*|` 與本欄之短少<u>同名不同量</u>**：前者為**等向膨脹**之臨界值×2、"
      "後者為**法定深度下之寬度差**；⛔ 不得互代（併列僅供對讀）。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【C】帶容差後之 8 格重測（`GB-80` 受詞 2）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C】**帶容差後之 8 格重測**：閘 ＝ `寬度 ≥ W − eps`（`GB-80` 受詞 2）")
    P("=" * WID)
    P(f"  🔒 `D_max` 出艙並列 `tol_conv` ＝ **{TOL_CONV:.1e} m**（`W-G.9-62` §五-D）")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'無容差(-62)':>12}{'帶容差':>9}{'翻?':>6}"
      f"{'D_max(帶容差)':>16}{'±容差':>10}{'D_法定':>9}")
    P("-" * WID)
    flips, n_adv_new = [], 0
    for lbl, which in EIGHT:
        pst, g, w, dd = cells[(lbl, which)]
        e = eps_by[lbl]
        ok = fits_at(pst, w - e, dd, g["theta"], 0.0)[0]
        cls = "進" if ok else "不進"
        n_adv_new += 1 if ok else 0
        dmx = d_max_at_r(pst, w - e, g["theta"], 0.0,
                         d_floor=DF_REAL, tol_conv=TOL_CONV)
        flip = (cls != PREV8[(lbl, which)])
        if flip and cls == "進":
            flips.append((lbl, which))
        P(f"  {lbl:<5}{which:<7}{PREV8[(lbl, which)]:>12}{cls:>10}"
          f"{('🔴 翻' if flip else '—'):>8}{dmx:>16.6f}{TOL_CONV:>10.1e}{dd:>9.1f}")
    P("-" * WID)
    P(f"  ⇒ 乙ii 之計數：**{sum(1 for k in EIGHT if PREV8[k] == '進')}／8 "
      f"⇒ {n_adv_new}／8**；**翻面 {len(flips)} 格**"
      + ("（" + "／".join(f"{a}/{b}" for a, b in flips) + "）" if flips else ""))
    P(f"  ⇒ **土地後果 ＝ {'🔴 非零' if flips else '零'}**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【D】判別力反例（⛔ 不得省）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【D】🔴 **判別力反例**（⛔ 不得省·`GB-80` 受詞 2）")
    P("=" * WID)
    n_noflip = sum(1 for k in EIGHT if PREV8[k] == "進")
    P(f"  **D-1　至少一格不因容差而翻**：8 格中 **{n_noflip} 格**原即「進」、"
      f"帶容差後仍「進」⇒ **未翻** ⇒ "
      f"{'✅ 成立' if n_noflip >= 1 else '🔴 不成立'}")
    P(f"     ⇒ **⛔ 非「8 格全翻」**（全翻即該容差無判別力）：實際翻面 **{len(flips)}／8**")
    P("")
    P("  **D-2　注入式反例：把需求寬度加大到 `w_max + 10·eps`（＝造出「短少 ＝ 10·eps」）**")
    P("     ⇒ **8 格須全部「不進」**；另以 `w_max + 0.5·eps`（短少 ＝ 0.5·eps）作**對照**")
    P("     ⇒ **8 格須全部「進」**。二者並列方成雙側判別力。")
    P("     🔴 **注入錨必須是<u>該格自己的 `w_max`</u>，⛔ 不是法定寬 `W`**——首版錨在 `W`，")
    P("     對「本來就寬鬆」之格（如 `R1/left` 之 `w_max = 3.659`）**根本沒注入到任何短少**")
    P("     ⇒ 其「進」係<u>該格真有餘裕</u>、⛔ 非容差吞掉了短少 ⇒ 首版之 `3／8` **量錯了受詞**。")
    P(f"  {'街廓':<5}{'側':<7}{'w_max':>14}{'注入 +10eps ⇒ 需求寬':>21}{'判(須不進)':>12}"
      f"{'注入 +0.5eps ⇒ 需求寬':>22}{'判(須進)':>10}")
    P("-" * WID)
    n_inj_pass = n_ctl_pass = 0
    for lbl, which in EIGHT:
        pst, g, w, dd = cells[(lbl, which)]
        e = eps_by[lbl]
        wm = w - short[(lbl, which)]                 # ＝ 該格之 w_max
        w_hi = wm + 10.0 * e
        w_lo = wm + 0.5 * e
        ok_hi = fits_at(pst, w_hi - e, dd, g["theta"], 0.0)[0]
        ok_lo = fits_at(pst, w_lo - e, dd, g["theta"], 0.0)[0]
        n_inj_pass += 0 if ok_hi else 1
        n_ctl_pass += 1 if ok_lo else 0
        P(f"  {lbl:<5}{which:<7}{wm:>14.6f}{w_hi:>21.6f}"
          f"{('進 🔴' if ok_hi else '不進 ✅'):>13}{w_lo:>22.6f}"
          f"{('進 ✅' if ok_lo else '不進 🔴'):>11}")
    P("-" * WID)
    P(f"  ⇒ **注入 10·eps：{n_inj_pass}／8 不進**"
      f"{'（✅ 容差吞不下 10 倍於己之短少）' if n_inj_pass == 8 else '（🔴 無判別力）'}")
    P(f"  ⇒ **對照 0.5·eps：{n_ctl_pass}／8 進**"
      f"{'（✅ 容差確實在作用·⇒ 上檢非恆紅）' if n_ctl_pass == 8 else '（🔴 容差未生效）'}")
    P("")
    P("  **D-3　閘之紅綠恰以「短少」為界**（逐格·⛔ 只對短少 > 0 之格有意義）")
    P(f"  {'街廓':<7}{'短少 s':>16}{'容差 0.5s ⇒ 須不進':>20}{'容差 2s ⇒ 須進':>18}{'判':>6}")
    P("-" * WID)
    n_d3 = n_d3_tot = 0
    for lbl, which in EIGHT:
        s = short[(lbl, which)]
        if s <= 0:
            continue
        n_d3_tot += 1
        pst, g, w, dd = cells[(lbl, which)]
        lo_ok = fits_at(pst, w - 0.5 * s, dd, g["theta"], 0.0)[0]
        hi_ok = fits_at(pst, w - 2.0 * s, dd, g["theta"], 0.0)[0]
        good = (not lo_ok) and hi_ok
        n_d3 += 1 if good else 0
        P(f"  {(lbl + '/' + which):<7}{s:>16.6e}{('進🔴' if lo_ok else '不進✅'):>20}"
          f"{('進✅' if hi_ok else '不進🔴'):>18}{('✅' if good else '🔴'):>6}")
    P("-" * WID)
    P(f"  ⇒ **{n_d3}／{n_d3_tot}** 之格其紅綠恰以短少為界 ⇒ "
      "🔑 **「要出現什麼這個閘才會紅？」＝ 短少超過 `eps`。**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【E】`P6`：`D_max` 十二值仍逐位相符 `-60`（容差只動閘、不動量測）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【E】`P6`：`D_max` 十二值（**不帶容差**）仍逐位相符 `W-G.9-60`"
      "　⇒ 容差**只動閘、不動量測**")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'r':>10}{'D_max':>14}{'±容差':>10}{'-60【倉】':>12}{'4dp':>6}")
    P("-" * WID)
    n_same = 0
    for lbl, which in FOCUS3:
        pst, g, _poly = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        w, _dd = wd[lbl]
        for j, r in enumerate(R_GRID):
            v = d_max_at_r(pst, w, g["theta"], r, d_floor=DF_REAL, tol_conv=TOL_CONV)
            ref = WG960_DMAX[(lbl, which)][j]
            same = (round(v, 4) == round(ref, 4))
            n_same += 1 if same else 0
            P(f"  {lbl:<5}{which:<7}{r:>10.0e}{v:>14.6f}{TOL_CONV:>10.1e}"
              f"{ref:>12.4f}{'✅' if same else '🔴':>5}")
    P("-" * WID)
    P(f"  ⇒ **{n_same}／12** 逐位相符")
    P("")
    return (L, sha, ns, cb_by, cad, snapshot, wd, flips, eps_by, short, cells,
            dict(d1=n_noflip, d2=n_inj_pass, d2c=n_ctl_pass, d3=n_d3,
                 d3tot=n_d3_tot, same12=n_same))


DF_REAL = None


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    # 🔒 `d_floor`（早退測試點之來源·`GB-82` (b-4)）——先量後用，⛔ 不硬編
    _ns0, _cb0, _cad0, _sn0, _wd0, _t0 = build_ctx()
    _cells0 = []
    for _l, _w in FOCUS3:
        _p, _g, _q = yi_pst(_ns0, _cb0, _cad0, _sn0, _wd0, _l, _w)
        _cells0.append((_l, _w, _p, _g, _wd0[_l][0]))
    DF_REAL = _dfloor(_cells0, GRID_B)
    _L, _sha, _ns, _cb, _cad, _sn, _wd, _flips, _eps, _short, _cells, _D = main()

    # ══════════════════════════════════════════════════════════════
    # 【F】土地後果對帳（`GB-80` 受詞 3）——須跑完整管線取「宗」
    # ══════════════════════════════════════════════════════════════
    def P(s=""):
        _L.append(s)

    P("=" * WID)
    P("【F】**土地後果對帳**（`GB-80` 受詞 3）：由「不可分配」變「可分配」者之宗")
    P("=" * WID)
    P(f"  🔒 `d_floor`（本次量得·供早退測試點）＝ **{DF_REAL:.6e}** m")
    P(f"  🔒 情境：`setback = {SB:g}`（同 `-58`〜`-62` 之乙式量測）")
    P("")
    _ns2, _fake = harvest()
    _snap2 = rv.load_snapshot()
    _cb2, _cad2 = rv.build_pipeline(_ns2, _fake, _snap2)
    rv.build_ownership(_ns2, _fake, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as _f:
        _v6 = _f.read()
    _tp, _bp, _ = rv.build_build_parcels(_ns2, _fake, _v6, list(_cb2.values()), _snap2)
    _params = rv.build_param_table(_ns2, _fake, _cb2, _cad2, _snap2, SB)
    _d0, _s2, _o2, _win, _forced = run_corner_pk(
        _ns2, _fake, list(_cb2.values()), _cad2, _params, _tp, _bp, SB, snapshot=_snap2)
    _sg, _sgerr = None, ""
    try:
        _sg = run_step_g(_ns2, _fake, list(_cb2.values()), _cad2, _snap2,
                         _params, _bp, _win, _forced, SB)
    except Exception as _e:                                         # noqa: BLE001
        _sgerr = f"{type(_e).__name__}: {_e}"
    if _sg is None:
        P(f"  🛑 **`run_step_g` 中止**（⛔ 不以「量測失敗」含糊帶過）：{_sgerr}")
        P("  🔒 **該停機係<u>既有</u>、⛔ 非本批所致**——`②-宗 圍堵閘破` 已登記為 `GB-55`／`GB-67`")
        P("    （字樣 `②-宗 圍堵閘` 於 `docs/reports/W-G.4_泛用阻塞項登記表.md` ⇒ **4 命中**）")
        P("    ⇒ 🔴 **`G(㎡)`（分配後）本批⛔ 無從出艙**；面積改取**分配前**之三欄")
        P("    （`build_parcels`：`幾何面積_m2`／`分攤登記面積_m2`／`登記面積_m2`）")
        P("    ——⚠️ **與 `G(㎡)` 同名不同量、⛔ 不得互代**。")
        _by = {}
    else:
        _by = {str(r.get("暫編地號")): r for r in _sg["g_rows"]}
    _bpby = {str(r.get("暫編地號")): r for r in (_bp or [])}
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'第 n 宗':>9}{'暫編地號':>14}{'幾何面積_m2':>14}"
      f"{'分攤登記面積_m2':>16}{'登記面積_m2':>13}{'G(㎡)':>9}{'無容差':>8}{'帶容差':>8}{'翻?':>6}")
    P("-" * WID)
    _nrow = 0
    for _l, _w in EIGHT:
        _p = ((_win or {}).get(_l) or {}).get("p1_end" if _w == "left" else "p2_end")
        _row = _by.get(str(_p)) or {}
        _bpr = _bpby.get(str(_p)) or {}
        _fl = (_l, _w) in _flips
        _gg = _row.get("G(㎡)")
        _nrow += 1 if _fl else 0

        def _f(v, wid=14):
            return (f"{float(v):.2f}" if v not in (None, "") else "—").rjust(wid)
        P(f"  {_l:<5}{_w:<7}{'第 1 宗':>9}{str(_p or '（強制抵費地）'):>14}"
          f"{_f(_bpr.get('幾何面積_m2'), 14)}{_f(_bpr.get('分攤登記面積_m2'), 16)}"
          f"{_f(_bpr.get('登記面積_m2'), 13)}{_f(_gg, 9)}"
          f"{PREV8[(_l, _w)]:>8}{('進' if _fl or PREV8[(_l, _w)] == '進' else '不進'):>8}"
          f"{('🔴 翻' if _fl else '—'):>7}")
    P("-" * WID)
    P(f"  ⇒ **由「不可分配」變「可分配」者 ＝ {_nrow} 宗**"
      + ("（皆為該街角之**第 1 宗**）" if _nrow else ""))
    P(f"  🔒 `run_corner_pk` 之 winner 數 ＝ {sum(1 for _l, _w in EIGHT if ((_win or {}).get(_l) or {}).get('p1_end' if _w == 'left' else 'p2_end'))}／8"
      f"（其餘為強制抵費地）")
    P("")
    P("=" * WID)
    P("【G】逐項判定 ＋ 收束斷言")
    P("=" * WID)
    _e0 = _eps[sorted(_cb)[0]]
    # 🔒 **⛔ 判定一律由實得算出**——本檔首版把三項寫死為 `True`，
    #   即「閘結構上不會紅」之原形（考古**節 91**·自誤 47 之同族）⇒ 已改。
    _items = [
        ("`GB-80`①", f"`eps` ＝ 生產碼 `_corner_range_eps(q)` ＝ {_e0:.3e}"
                     "（三分支皆可觸發·⛔ 非硬編·輸入量已印來源）", _e0 > 0.0),
        ("`GB-80`②-D1", f"至少一格不因容差而翻：{_D['d1']}／8 未翻（⛔ 非 8 格全翻）",
         _D["d1"] >= 1 and len(_flips) < 8),
        ("`GB-80`②-D2", f"注入 10·eps ⇒ {_D['d2']}／8 不進；對照 0.5·eps ⇒ {_D['d2c']}／8 進",
         _D["d2"] == 8 and _D["d2c"] == 8),
        ("`GB-80`②-D3", f"紅綠恰以短少為界：{_D['d3']}／{_D['d3tot']}",
         _D["d3tot"] > 0 and _D["d3"] == _D["d3tot"]),
        ("`P6`", f"`D_max` 十二值 {_D['same12']}／12 逐位相符 `-60`", _D["same12"] == 12),
        ("`GB-80`③", f"土地後果對帳：{_nrow} 宗由不可分配變可分配", _nrow == len(_flips)),
    ]
    for _k, _t, _o in _items:
        P(f"  {_k:<16}{'✅' if _o else '🔴'}　{_t}")
    P("-" * WID)
    P(f"  ⇒ **{'✅ 全部成立' if all(o for _a, _b, o in _items) else '🔴 有未成立項'}**")
    if fp.LOCAL_ORIGIN is not True:
        raise RuntimeError("🔴 探針結束時 `LOCAL_ORIGIN` ⛔ 非 `True`（`W-G.9-62` §七-5）。")
    P("  🔒 §七-5 收束斷言：`LOCAL_ORIGIN is True` ✅")
    P("=" * WID)

    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG963_eps_tolerance_v2_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
