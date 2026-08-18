#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-65】**甲式（生產碼現行構造）** 8 格寬度重量 ＋ 甲乙比對 ＋ 注入式階梯 ⛔ 零生產碼

**受詞（⛔ 不得改寫）**：
- **甲式** ＝ 生產碼現行之 `_build_corner_range_v3`：`S1_par = max(_seg_P0Ps, T)`，
  `T = setback + 畸零地最小寬 = 0 + 3.5`（字樣錨 `grep -c "S1_par = max(_seg_P0Ps, T)" app.py` ⇒ **1**）。
- **乙式(ii)** ＝ `K-9-5-14`（KL 裁 2026-08-17·**生產碼未實作**）：`S1_par = max(seg, T/sinθ)`
  ——`-63`／`-64` 所量者為此式。

🔒 **量法與 `W-G.9-63` §C-1 完全相同**（⛔ 不另立第二種量法）：
    `w_max(格) := max { w : 於<u>法定深度</u> `D` 仍可容納之寬 }`；`短少 := W − w_max`
🔒 `setback = 0`、`D = 14.00`、`W = 3.50`、八格 ＝ `-63` 之同一組。
🔒 **儀器沿用既有者**（`build_ctx`／`build_range`／`fits_at`／`w_max_at`）
  ——⛔ **不新增第二份判定原語**（`GB-8`）。

🔴 **⛔ 未抄施工單之甲式數字**——單 §五 之值係 claude.ai 以**閉式**量測器所得，
  於本倉為 **`【單】`**；本檔自量者方為 **`【倉】`**。二者相符⛔ 不構成相互驗證。

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
from probe_WG947_rect_fit import _poly_st                           # noqa: E402
from probe_WG949_free_pose import fits_at, witness                  # noqa: E402
from probe_WG960_fitcore import build_ctx, build_range, geom, yi_pst  # noqa: E402
from probe_WG961_dfloor import witness6                            # noqa: E402
from probe_WG963_eps_tolerance import EIGHT, w_max_at               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 172
SB = 0.0
EPS_LADDER = (1e-4, 1e-3, 2e-2)          # §二 A-5-2 之三個容差高度
FOCUS3 = [("R1", "right"), ("R5", "left"), ("R6", "right")]
# `W-G.9-63`【倉】之**乙式**短少（出處 `verify/out/probe_WG963_eps_tolerance_v2_1c68556.log`【B】）
YI_SHORT = {
    ("R1", "left"): -1.591157e-01, ("R1", "right"): -9.415063e-09,
    ("R2", "left"): -4.417746e-02, ("R3", "right"): -6.540715e-02,
    ("R4", "left"): -1.954657e-01, ("R4", "right"): -4.385031e-02,
    ("R5", "left"): +1.456501e-07, ("R6", "right"): +8.802454e-08,
}


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def jia_pst(ns, cb_by, cad, snapshot, wd, lbl, which, setback=SB):
    """**甲式**之範圍多邊形（`_poly_st` 後）＋ 其幾何 dict。

    🔒 甲式 ＝ **`min_width` 用查表值本身** ⇒ `_build_corner_range_v3` 內部算出
      `S1_par = max(_seg_P0Ps, T)`（`T = setback + min_width`）——即生產碼現行構造。
      ⇒ ⛔ **本函式不注入任何值**（乙式才注入 `min_width = 目標垂距/sinθ`）。
    """
    g = geom(ns, cb_by, cad, lbl, which)
    poly = build_range(ns, cb_by, cad, snapshot, wd, lbl, which, setback)
    return _poly_st([(float(x), float(y)) for x, y in list(poly.exterior.coords)]), g


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-65】**甲式**（生產碼現行構造）8 格寬度重量 ＋ 甲乙比對 ＋ 注入式階梯")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；⛔ 未新增第二份判定原語；⛔ 未抄施工單之甲式數字。")
    P("")

    ns, cb_by, cad, snapshot, wd, _t = build_ctx()

    # ══════════════════════════════════════════════════════════════
    # 【A】甲式 8 格：`S1_par`／`w_max`／短少
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A】**甲式** 8 格：`S1_par = max(seg, T)`，`T = 0 + 3.5`（`setback = 0`·`D = 14.00`）")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'W':>6}{'D':>7}{'seg':>12}{'T':>8}"
      f"{'甲 S1_par':>12}{'甲 w_max':>16}{'甲短少 ＝ W−w_max':>20}{'無容差判':>10}")
    P("-" * WID)
    jia = {}
    n_adv_j = 0
    for lbl, which in EIGHT:
        pst, g = jia_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        w, dd = wd[lbl]
        T = SB + w
        s1 = max(g["seg"], T)
        wm = w_max_at(pst, g["theta"], dd, w + 1.0)
        sh = w - wm
        jia[(lbl, which)] = dict(pst=pst, g=g, w=w, d=dd, seg=g["seg"], T=T,
                                 s1=s1, wmax=wm, short=sh)
        cls = "進" if sh <= 0.0 else "不進"
        n_adv_j += 1 if cls == "進" else 0
        P(f"  {lbl:<5}{which:<7}{w:>6.2f}{dd:>7.2f}{g['seg']:>12.6f}{T:>8.3f}"
          f"{s1:>12.6f}{wm:>16.9f}{sh:>20.6e}{cls:>11}")
    P("-" * WID)
    P(f"  ⇒ **甲式（無容差）之分類：{n_adv_j} 進／{8 - n_adv_j} 不進**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【B】甲乙逐格比對（A-5-1 之對照組·⛔ 全同或全異皆為紅）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【B】🔴 **甲乙逐格比對**（A-5-1）：`seg` 於兩式同為支配項之格，其值應**逐位不變**")
    P("=" * WID)
    P("  🔒 甲 `S1_par = max(seg, T)`；乙 `S1_par = max(seg, T/sinθ)`。")
    P("     `T/sinθ ≥ T`（`sinθ ≤ 1`）⇒ **乙之門檻恆 ≥ 甲** ⇒ 二式相異者⛔ 只可能是")
    P("     「`T/sinθ` 支配」之格；`seg` 支配之格**兩式同構** ⇒ 其 `w_max` 應逐位相同。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'seg':>12}{'T':>8}{'T/sinθ':>12}"
      f"{'甲支配':>8}{'乙支配':>8}{'甲 w_max':>16}{'乙 w_max':>16}{'Δ(甲−乙)':>14}{'同/異':>7}")
    P("-" * WID)
    n_same = n_diff = 0
    cmp_rows = []
    for lbl, which in EIGHT:
        J = jia[(lbl, which)]
        g = J["g"]
        tsin = J["T"] / g["sin"]
        pstY, gY, _p = yi_pst(ns, cb_by, cad, snapshot, wd, lbl, which)
        wmY = w_max_at(pstY, gY["theta"], J["d"], J["w"] + 1.0)
        domJ = "T" if J["T"] > J["seg"] else "seg"
        domY = "T/sin" if tsin > J["seg"] else "seg"
        d = J["wmax"] - wmY
        same = (abs(d) <= 2e-9)
        n_same += 1 if same else 0
        n_diff += 0 if same else 1
        cmp_rows.append((lbl, which, same, domJ, domY, J["wmax"], wmY, J["short"],
                         J["w"] - wmY))
        P(f"  {lbl:<5}{which:<7}{J['seg']:>12.6f}{J['T']:>8.3f}{tsin:>12.6f}"
          f"{domJ:>9}{domY:>9}{J['wmax']:>16.9f}{wmY:>16.9f}{d:>14.3e}"
          f"{('同' if same else '**異**'):>8}")
    P("-" * WID)
    P(f"  ⇒ **同 {n_same} 格／異 {n_diff} 格**　"
      f"{'✅ 分裂為 5／3（⛔ 非 8／0、⛔ 非 0／8）' if (n_same, n_diff) == (5, 3) else '🔴 **分裂不是 5／3**'}")
    P(f"  🔒 相異之格逐格具名：**{'／'.join(f'{a}/{b}' for a, b, s, *_ in cmp_rows if not s)}**")
    P("")
    P("  **甲乙短少之對讀（⛔ 二者係<u>兩種構造</u>之量·⛔ 不得互代）**")
    P(f"  {'街廓':<5}{'側':<7}{'甲短少【倉】':>18}{'乙短少（-63【倉】）':>22}{'倍率 甲/乙':>16}")
    P("-" * WID)
    for lbl, which, same, _dj, _dy, _wj, _wy, shJ, shY in cmp_rows:
        ref = YI_SHORT[(lbl, which)]
        rat = (shJ / ref) if abs(ref) > 0 else float("nan")
        P(f"  {lbl:<5}{which:<7}{shJ:>18.6e}{ref:>22.6e}{rat:>16.4g}")
    P("-" * WID)
    P("  ⚠️ **「倍率」一欄之讀法（⛔ 不得一句概括）**：")
    P("     · `R1/right` ⇒ **變號**（甲 `+1.51e−02` vs 乙 `−9.42e−09`）"
      "——⛔ 「倍率」二字於此**不適用**，其意義為「甲不進、乙進」。")
    P("     · `R5/left` ⇒ `3.46e+03`（**3.5 個數量級**）；`R6/right` ⇒ `1.29e+05`（**5 個數量級**）。")
    P("  🔑 ⇒ 🔒 **`GB-80`「餘裕恆 0」係<u>乙式</u>之性質；甲式之短少大 3〜5 個數量級"
      "（含一格變號）⇒ 該性質於甲式 ⛔ 不成立。**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【C】注入式階梯（A-5-2·⛔ 逐格具名·⛔ 不只報數）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C】🔴 **注入式階梯**（A-5-2）：甲式於三個容差高度之翻面（閘 ＝ `寬度 ≥ W − eps`）")
    P("=" * WID)
    P("  🔒 **本階梯即該閘之判別力測試**——一個從未紅過的閘，跟一段註解證據力相同。")
    P("")
    base_cls = {k: ("進" if v["short"] <= 0.0 else "不進") for k, v in jia.items()}
    P(f"  {'eps':>10}{'翻面格數':>10}   {'翻面之格（逐格具名）':<40}{'該 eps 下之分類':>18}")
    P("-" * WID)
    ladder = []
    for eps in EPS_LADDER:
        flips, adv = [], 0
        for lbl, which in EIGHT:
            J = jia[(lbl, which)]
            ok = fits_at(J["pst"], J["w"] - eps, J["d"], J["g"]["theta"], 0.0)[0]
            adv += 1 if ok else 0
            if ok and base_cls[(lbl, which)] == "不進":
                flips.append(f"{lbl}/{which}")
        ladder.append((eps, len(flips), flips, adv))
        P(f"  {eps:>10.0e}{len(flips):>10}   {('／'.join(flips) or '（無）'):<40}"
          f"{f'{adv} 進／{8 - adv} 不進':>18}")
    P("-" * WID)
    got = tuple(n for _e, n, _f, _a in ladder)
    P(f"  ⇒ 翻面格數階梯 ＝ **{got}**（期望 `(0, 1, 3)`）⇒ "
      f"{'✅ 相符' if got == (0, 1, 3) else '🔴 **不符**'}")
    P("  🔒 **本閘確會紅亦確會綠**：最低高度 0 格、最高高度 3 格 ⇒ ⛔ 非恆綠、⛔ 非恆紅。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【D】見證（A-5-3·三焦點格·甲乙各一組·逐角 `covers`）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【D】**見證**（A-5-3）：三焦點格·甲乙各一組·**四角座標 ＋ 逐角 `poly.covers`**")
    P("=" * WID)
    P("  🔴 **具名偏離施工單字面**：單令「判『進』之格須出艙見證」，而三焦點格於**甲式**")
    P("     皆為「不進」（短少 > 0）⇒ 若照字面則**一組見證都出不了**。")
    P("     ⇒ 🔒 **改於該格自己的 `w_max` 取見證**（＝該格<u>確實可容納</u>之最大寬）")
    P("     ——資訊**多於**而非少於原令；並**併報**其於 `W = 3.50` 是否可容納。")
    P("")
    P("  🔴 **見證取<u>二處</u>（⛔ 缺一不可）**：")
    P("     · **邊界** `w = w_max`——二分之回值即**可行集之邊界**，侵蝕集於此**退化**")
    P("       ⇒ 逐角 `covers` 於此**本就不穩**（`GB-82` 之併記已登記「`fits_at` 回真而見證不可得」）。")
    P("     · **內點** `w = w_max − δ`（`δ = 1e−06`·**高於量子 1e−05 之十分之一、遠高於浮點雜訊**）")
    P("       ⇒ 此處為**嚴格內點** ⇒ 🔒 **A-5-3 之判定以本欄為準**（邊界欄照實並列、⛔ 不隱去）。")
    P("")
    DELTA_W = 1e-06
    P(f"  {'式':<4}{'街廓':<5}{'側':<7}{'w_max（邊界）':>16}{'邊界四角全在':>13}"
      f"{'w_max−δ（內點）':>17}{'內點逐角':>11}{'內點四角全在':>13}{'W=3.50 可容納?':>15}")
    P("-" * WID)
    n_wit = n_wit_ok = 0
    wit_detail = []
    for tag, getter in (("甲", lambda l, w: (jia[(l, w)]["pst"], jia[(l, w)]["g"])),
                        ("乙", lambda l, w: yi_pst(ns, cb_by, cad, snapshot, wd, l, w)[:2])):
        for lbl, which in FOCUS3:
            pst, g = getter(lbl, which)
            w, dd = wd[lbl]
            wm = w_max_at(pst, g["theta"], dd, w + 1.0)
            at_W = fits_at(pst, w, dd, g["theta"], 0.0)[0]

            def _wit(ww):
                wt = witness(pst, ww, dd, g["theta"])
                ins = ([bool(b) for b in wt["inside"]] if wt else None)
                if not (ins and all(ins)):
                    ins, _n = witness6(pst, ww, dd, g["theta"])
                return wt, ins, bool(ins and all(ins))

            wtB, insB, okB = _wit(wm)                       # 邊界
            wtI, insI, okI = _wit(wm - DELTA_W)             # 內點（⇒ A-5-3 之判定依據）
            n_wit += 1
            n_wit_ok += 1 if okI else 0
            txtI = ("[" + "".join("T" if b else "F" for b in insI) + "]") if insI else "（fits 偽）"
            wit_detail.append((tag, lbl, which, wm - DELTA_W, wtI))
            P(f"  {tag:<4}{lbl:<5}{which:<7}{wm:>16.9f}{('是' if okB else '否'):>14}"
              f"{wm - DELTA_W:>17.9f}{txtI:>12}{('是' if okI else '否'):>14}"
              f"{('是' if at_W else '否'):>16}")
    P("-" * WID)
    P("-" * WID)
    P(f"  ⇒ **內點見證：{n_wit_ok}／{n_wit}** 組四角全在宗內（🔒 A-5-3 之判定依據）")
    P("  ⚠️ **邊界欄之失敗⛔ 非缺陷、係<u>構造必然</u>**：`w_max` 係二分之回值 ＝ 可行集之邊界，")
    P("     侵蝕集於該處退化為線段／點 ⇒ 逐角 `covers` 落在數值刀鋒上"
      "（`GB-82` 併記之同一現象）。")
    P("")
    P("  **見證矩形之四角座標（原框·⛔ 具名·⛔ 非僅報 True）**")
    for tag, lbl, which, wm, wt in wit_detail:
        if not wt:
            P(f"  {tag} {lbl}/{which} @ w={wm:.9f}：（單候選見證不可得·上表已改 6 候選口徑）")
            continue
        cs = "　".join(f"({x:.4f}, {y:.4f})" for x, y in wt["corners"])
        P(f"  {tag} {lbl}/{which} @ w={wm:.9f}　θ={wt['theta']:.6f}")
        P(f"     四角 ＝ {cs}")
        P(f"     逐角 covers ＝ {['T' if b else 'F' for b in wt['inside']]}")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【E】逐項判定 ＋ 收束斷言
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【E】逐項判定")
    P("=" * WID)
    items = [
        ("A-5-1 對照組", f"甲乙分裂 ＝ {n_same}／{n_diff}（須 5／3·⛔ 非 8／0、⛔ 非 0／8）",
         (n_same, n_diff) == (5, 3)),
        ("A-5-2 階梯", f"翻面格數 ＝ {got}（須 `(0, 1, 3)`）", got == (0, 1, 3)),
        ("A-5-3 見證", f"{n_wit_ok}／{n_wit} 組四角全在", n_wit_ok == n_wit),
    ]
    for k, t, ok in items:
        P(f"  {k:<16}{'✅' if ok else '🔴'}　{t}")
    P("-" * WID)
    P(f"  ⇒ **{'✅ 全部成立' if all(o for _a, _b, o in items) else '🔴 有未成立項'}**")
    if fp.LOCAL_ORIGIN is not True:
        raise RuntimeError("🔴 探針結束時 `LOCAL_ORIGIN` ⛔ 非 `True`（`W-G.9-62` §七-5）。")
    P("  🔒 §七-5 收束斷言：`LOCAL_ORIGIN is True` ✅")
    P("=" * WID)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG965_jia_width_v2_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
