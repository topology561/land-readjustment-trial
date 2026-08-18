#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-67】乙式落地：**先證紅**（`pre`）／**修後之量**（`post`）

**受詞**：`K-9-5-14`（KL 裁 2026-08-17）＋ `K-9-5-15`（KL 裁 2026-08-18）——
街角規定範圍之內側界改為 **沿 SIDELINE <u>法向</u>平移**，其量為 **垂距**。

🔴 **施工單之內部矛盾（⛔ 具名·⛔ 未默默擇一）**：
  §三 **B-1-1**（不變式·＝受詞）令 `垂距 ＝ S1_perp = max(_seg_P0Ps·sinθ, T)`；
  §四-1 與 `P3` 則令 **「八格垂距 ＝ `T`」**。二者**僅於「`T` 支配」之格一致**。
  🔒 **本檔採 B-1-1**，理由三：
    ① B-1-1 是明訂之**不變式**（受詞），§四-1 係其**逐格出艙之敘述**；
    ② `P4` 之門檻表預測「**只有三格變、五格逐位不變**」**只與 B-1-1 相容**
       （八格垂距皆 ＝ `T` 會使 `seg` 支配之五格亦變）；
    ③ 若令 `seg` 支配之格垂距降為 `T`，其平移量**變小** ⇒ 分配線切進截角
       ⇒ 違反 **B-1-3 之硬約束**。
  ⇒ `P3` 之原文**逐字保留**，實得另列並具名偏差（報告 §F）。

**命題（本檔之靶）**：**八格之「平移後側界與 SIDELINE 之垂距」＝ `S1_perp`**
（`S1_perp = max(_seg_P0Ps·sinθ, T)`；`T = 退縮 + 畸零地最小寬 = 0 + 3.5`）。
- 🔴 **`pre`：該命題須為<u>假</u>**（且逐格具名哪幾格為假）⇒ 即「紅」。
- ✅ **`post`：該命題須為<u>真</u>**（`|Δ| ≤ 1e−9`）。

🔒 **判別力對照（⛔ 不得省）**：同表之「**路平行距 ≥ `T`**」**修前即八格皆真**
  ——⇒ 證本探針 **⛔ 非恆紅**（畸零地使用規則第四條第三款之最小寬度·現行已合規）。

🔒 **量之來源（⛔ 具名）**：`sinθ`／`_seg_P0Ps` 係本檔以**與生產碼同式**外部覆算
  （`geom()`：`s_Ps = (Ps−F1)·d̂`、`t_q` 同法、`seg = |s_Ps − t_q|`）。
  🔒 **自我驗證閘**（`CLAUDE.md`「探針還原內部幾何須設閘」）：
  同批呼叫**生產碼之 `_build_corner_range_v3`**，其**構造自檢**（`grep -n "構造自檢不合" app.py`）
  若不合即 `_stop` ⇒ **該函式回得出多邊形，即為本檔覆算之外部保證**；本檔逐格印出該事實。

用法：`WG967_STAGE=pre|post python verify/probes/probe_WG967_yi_landing.py`
🔒 輸出檔名含 stage ＋ 產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import math
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
from probe_WG960_fitcore import build_ctx, build_range, geom        # noqa: E402
from probe_WG961_dfloor import witness6                             # noqa: E402
from probe_WG963_eps_tolerance import EIGHT, w_max_at               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 176
SB = 0.0
FOCUS3 = [("R1", "right"), ("R5", "left"), ("R6", "right")]
TOL = 1e-9
# `W-G.9-66`【倉】之修前門檻（出處 `verify/out/probe_WG966_gate_locate_e8f1d34.log`【A-3】）
PRE_THRESH = {
    ("R1", "left"): 114.94, ("R1", "right"): 110.17,
    ("R2", "left"): 152.99, ("R3", "right"): 153.80,
    ("R4", "left"): 116.08, ("R4", "right"): 111.02,
    ("R5", "left"): 146.48, ("R6", "right"): 145.88,
}


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _perp_of_range(ns, cb_by, cad, snapshot, wd, lbl, which, g):
    """自**生產碼所建之範圍多邊形**還原「平移後側界與 SIDELINE 之垂距」。

    🔒 **不重建幾何**：取範圍多邊形之全部頂點，量其至 **SIDELINE 無限直線**之垂距，
      取 **max** ⇒ 即平移後側界所在之垂距（範圍之遠側界即該線）。
    🔒 **自我驗證閘**：本函式所呼叫之 `_build_corner_range_v3` 內建**構造自檢**，
      不合即 `_stop` ⇒ 其**回得出多邊形**本身即為外部覆算之保證。
    """
    poly = build_range(ns, cb_by, cad, snapshot, wd, lbl, which, SB)
    S1, sn = g["S1"], g["sn"]
    perp = max(abs((float(x) - S1[0]) * sn[0] + (float(y) - S1[1]) * sn[1])
               for x, y in list(poly.exterior.coords))
    return poly, perp


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    stage = os.environ.get("WG967_STAGE", "pre")
    P("=" * WID)
    P(f"【W-G.9-67】乙式落地——階段：**{stage}**")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P(f"  🔒 靶命題：**八格之「平移後側界 ⊥ SIDELINE 之垂距」＝ `T`**"
      f"（`pre` 須為**假**、`post` 須為**真**·容差 `{TOL:g}`）")
    P("")

    ns, cb_by, cad, snapshot, wd, _t = build_ctx()

    P("=" * WID)
    P(f"【A】八格之逐格表（`setback = {SB:g}`·`W = 3.50`·`D` 取查表值）")
    P("=" * WID)
    P("  🔒 `S1_perp = max(_seg_P0Ps·sinθ, T)`（B-1-1）；「支配項」欄示其由誰決定。")
    P(f"  {'街廓':<5}{'側':<7}{'sinθ':>12}{'_seg_P0Ps':>12}{'T':>7}"
      f"{'S1_perp':>12}{'支配項':>9}{'範圍實測垂距':>16}{'垂距−S1_perp':>16}"
      f"{'垂距 − T':>16}{'路平行距':>12}{'≥T?':>6}{'構造自檢':>10}")
    P("-" * WID)
    rows = []
    n_perp_eq = n_par_ge = 0
    bad_perp = []
    for lbl, which in EIGHT:
        g = geom(ns, cb_by, cad, lbl, which)
        w, dd = wd[lbl]
        T = SB + w
        s1_jia = max(g["seg"], T)
        poly, perp = _perp_of_range(ns, cb_by, cad, snapshot, wd, lbl, which, g)
        # 路平行距 ＝ 垂距 ÷ sinθ（同一條平移後側界之兩種量）
        par = perp / g["sin"]
        s1_perp = max(g["seg"] * g["sin"], T)      # 🔒 B-1-1 之不變式（＝受詞）
        eq = abs(perp - s1_perp) <= TOL
        eq_T = abs(perp - T) <= TOL               # §四-1／`P3` 之字面（逐格另列）
        ge = (par + TOL) >= T
        n_perp_eq += 1 if eq else 0
        n_par_ge += 1 if ge else 0
        if not eq:
            bad_perp.append(f"{lbl}/{which}")
        rows.append((lbl, which, g, w, dd, T, s1_jia, perp, par, eq, ge, poly, s1_perp, eq_T))
        P(f"  {lbl:<5}{which:<7}{g['sin']:>12.7f}{g['seg']:>12.6f}{T:>7.2f}"
          f"{s1_perp:>12.6f}{('T' if T > g['seg'] * g['sin'] else 'seg·sin'):>9}"
          f"{perp:>16.9f}{perp - s1_perp:>16.6e}{perp - T:>16.6e}{par:>12.6f}"
          f"{('✅' if ge else '🔴'):>5}{'✅ 過':>11}")
    P("-" * WID)
    n_eqT = sum(1 for r in rows if r[13])
    P(f"  ⇒ **垂距 ＝ `S1_perp` 之格數 ＝ {n_perp_eq}／8**"
      + (f"　🔴 **不等之格逐格具名：{'／'.join(bad_perp)}**" if bad_perp else "　（八格皆等）"))
    P(f"  ⇒ 〔另列·`P3` 之字面〕**垂距 ＝ `T` 之格數 ＝ {n_eqT}／8**"
      "（🔒 該命題只可能於「`T` 支配」之格成立·見檔頭之矛盾具名）")
    P(f"  ⇒ **判別力對照：路平行距 ≥ `T` 之格數 ＝ {n_par_ge}／8**"
      f"　{'✅ 八格皆真 ⇒ ⛔ 本探針非恆紅' if n_par_ge == 8 else '🔴 有格不真'}")
    P("  🔒 **末欄「構造自檢」**：`_build_corner_range_v3` 之內建自檢不合即 `_stop`；")
    P("     本表八格皆**回得出多邊形** ⇒ 該自檢**八格皆過** ⇒ 本檔之外部覆算有碼面保證。")
    P("")
    if stage == "pre":
        P("  🔴 **`pre` 之判**："
          f"命題「八格垂距 ＝ S1_perp」⇒ **{'🔴 為假（＝紅·符合先證紅之要求）' if n_perp_eq < 8 else '✅ 為真（⇒ 🛑 修前即已成立·與預測不符）'}**")
    else:
        P("  ✅ **`post` 之判**："
          f"命題「八格垂距 ＝ S1_perp」⇒ **{'✅ 為真' if n_perp_eq == 8 else '🔴 為假 ⇒ 修未達成'}**")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【B】門檻（規定範圍面積）之逐格
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【B】**門檻（街角規定範圍面積）** 之逐格　"
      "（對拍靶 ＝ `W-G.9-66`【倉】`probe_WG966_gate_locate_e8f1d34.log`【A-3】）")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'本階段面積 ㎡':>16}{'修前【倉】㎡':>16}{'Δ':>12}{'變?':>6}")
    P("-" * WID)
    n_chg = 0
    areas = {}
    for lbl, which, g, w, dd, T, s1_jia, perp, par, eq, ge, poly, s1_perp, eq_T in rows:
        a = float(poly.area)
        areas[(lbl, which)] = a
        ref = PRE_THRESH[(lbl, which)]
        d = round(a, 2) - ref
        chg = abs(d) > 0.0
        n_chg += 1 if chg else 0
        P(f"  {lbl:<5}{which:<7}{a:>16.6f}{ref:>16.2f}{d:>12.2f}"
          f"{('🔴 變' if chg else '—'):>7}")
    P("-" * WID)
    P(f"  ⇒ **變 {n_chg} 格／不變 {8 - n_chg} 格**（2dp 比對）；"
      f"**Δ 合計（帶號）＝ {sum(round(areas[k], 2) - PRE_THRESH[k] for k in areas):+.2f} ㎡**、"
      f"**Σ|Δ| ＝ {sum(abs(round(areas[k], 2) - PRE_THRESH[k]) for k in areas):.2f} ㎡**")
    P("  🔒 帶號合計與絕對值合計**並列**（`CLAUDE.md`「凡列合計，二者必須並列」）。")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【C】見證（三焦點格·⛔ 取內點 `w_max − 1e−06`）
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C】**見證**（三焦點格·⛔ 取**內點** `w_max − 1e−06`·逐角 `poly.covers`）")
    P("=" * WID)
    DELTA_W = 1e-06
    P(f"  {'街廓':<5}{'側':<7}{'w_max':>16}{'內點 w':>16}{'逐角':>10}{'四角全在':>10}"
      f"{'W=3.50 可容納?':>16}")
    P("-" * WID)
    n_w = n_wok = 0
    wit_detail = []
    for lbl, which, g, w, dd, T, s1_jia, perp, par, eq, ge, poly, s1_perp, eq_T in rows:
        if (lbl, which) not in FOCUS3:
            continue
        pst = _poly_st([(float(x), float(y)) for x, y in list(poly.exterior.coords)])
        wm = w_max_at(pst, g["theta"], dd, w + 1.0)
        at_W = fits_at(pst, w, dd, g["theta"], 0.0)[0]
        wt = witness(pst, wm - DELTA_W, dd, g["theta"])
        ins = ([bool(b) for b in wt["inside"]] if wt else None)
        if not (ins and all(ins)):
            ins, _n = witness6(pst, wm - DELTA_W, dd, g["theta"])
        ok = bool(ins and all(ins))
        n_w += 1
        n_wok += 1 if ok else 0
        wit_detail.append((lbl, which, wm - DELTA_W, wt))
        txt = ("[" + "".join("T" if b else "F" for b in ins) + "]") if ins else "（fits 偽）"
        P(f"  {lbl:<5}{which:<7}{wm:>16.9f}{wm - DELTA_W:>16.9f}{txt:>11}"
          f"{('是' if ok else '否'):>11}{('是' if at_W else '否'):>17}")
    P("-" * WID)
    P(f"  ⇒ **{n_wok}／{n_w}** 組內點見證之四角全在宗內")
    for lbl, which, ww, wt in wit_detail:
        if not wt:
            continue
        cs = "　".join(f"({x:.4f}, {y:.4f})" for x, y in wt["corners"])
        P(f"  {lbl}/{which} @ w={ww:.9f}　θ={wt['theta']:.6f}")
        P(f"     四角 ＝ {cs}")
    P("")

    P("=" * WID)
    P("【D】本階段之判定")
    P("=" * WID)
    want = (n_perp_eq < 8) if stage == "pre" else (n_perp_eq == 8)
    items = [
        (f"靶命題（{stage}）", f"垂距 ＝ S1_perp 之格數 ＝ {n_perp_eq}／8", want),
        ("判別力對照", f"路平行距 ≥ T 之格數 ＝ {n_par_ge}／8（須 8）", n_par_ge == 8),
        ("見證", f"內點見證 {n_wok}／{n_w}", n_wok == n_w),
    ]
    for k, t, ok in items:
        P(f"  {k:<16}{'✅' if ok else '🔴'}　{t}")
    P("-" * WID)
    P(f"  ⇒ **{'✅ 全部成立' if all(o for _a, _b, o in items) else '🔴 有未成立項'}**")
    if fp.LOCAL_ORIGIN is not True:
        raise RuntimeError("🔴 探針結束時 `LOCAL_ORIGIN` ⛔ 非 `True`。")
    P("  🔒 收束斷言：`LOCAL_ORIGIN is True` ✅")
    P("=" * WID)
    return L, sha, stage


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha, _st = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG967_{_st}_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
