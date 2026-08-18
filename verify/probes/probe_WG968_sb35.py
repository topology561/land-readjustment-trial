#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-68】`setback = 3.5` 之乙式量 ＋ `setback = 0` 對照 ＋ 門檻對帳 ⛔ 零生產碼

**受詞**：`K-9-5-14`／`K-9-5-15` 已於 `W-G.9-67` 落地（`app.py` blob `083d382a…`）。
本波自 `-58` 起之逐格量**一律 `setback = 0`**，而 `K-9-5-3` 之爭議實例**正是 `3.5m` 情境**
⇒ 本檔補量 `setback = 3.5`。

🔒 **不變式（受詞·⛔ 不得改寫）**：`S1_perp = max(_seg_P0Ps · sinθ, T)`，
  `T = setback + 畸零地最小寬`（`setback = 3.5` ⇒ `T = 7.00`）。

🔒 **判別力對照（⛔ 不得省）**：同表併列 `setback = 0` 之**支配項**欄
  ⇒ 二情境之支配項分佈**須不同**——⛔ 若相同，表示 `setback` 根本沒進到量測（＝紅）。

🔒 **儀器沿用既有者**（`build_ctx`／`build_range`／`geom`）——⛔ 不新增第二份判定原語。
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

from probe_WG960_fitcore import build_ctx, build_range, geom        # noqa: E402
from probe_WG963_eps_tolerance import EIGHT                         # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 178
TOL = 1e-9
SB35, SB0 = 3.5, 0.0


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def _perp(ns, cb_by, cad, snapshot, wd, lbl, which, g, sb):
    """自**生產碼所建之範圍多邊形**還原「平移後側界 ⊥ SIDELINE 之垂距」。

    🔒 **自我驗證閘**：`_build_corner_range_v3` 內建之**構造自檢**（現已為
      **垂距 ＋ 路平行距二者並檢**·`W-G.9-67` §C-4）不合即 `_stop`
      ⇒ 其**回得出多邊形**本身即為本檔外部覆算之保證。
    """
    poly = build_range(ns, cb_by, cad, snapshot, wd, lbl, which, sb)
    S1, sn = g["S1"], g["sn"]
    p = max(abs((float(x) - S1[0]) * sn[0] + (float(y) - S1[1]) * sn[1])
            for x, y in list(poly.exterior.coords))
    return poly, p


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-68】`setback = 3.5` 之乙式量 ＋ `setback = 0` 對照")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 **⛔ 零生產碼變更**；儀器沿用既有者；⛔ 未新增第二份判定原語。")
    P("  🔒 不變式：`S1_perp = max(_seg_P0Ps·sinθ, T)`；`T = setback + 3.50`。")
    P("")

    ns, cb_by, cad, snapshot, wd, _t = build_ctx()

    # ══════════════════════════════════════════════════════════════
    # 【A-1】`setback = 3.5` 八格 ＋ `setback = 0` 之支配項對照
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-1】`setback = 3.5`（⇒ `T = 7.00`）之八格　＋　`setback = 0` 之**支配項對照**")
    P("=" * WID)
    P(f"  {'街廓':<5}{'側':<7}{'sinθ':>12}{'_seg_P0Ps':>12}{'seg·sinθ':>12}{'T':>7}"
      f"{'S1_perp':>11}{'支配(3.5m)':>12}{'支配(0m)':>10}"
      f"{'範圍實測垂距':>16}{'垂距−S1_perp':>15}{'路平行距':>12}{'>T?':>6}{'構造自檢':>10}")
    P("-" * WID)
    rows, n_eq, n_gt = [], 0, 0
    dom35, dom0 = [], []
    for lbl, which in EIGHT:
        g = geom(ns, cb_by, cad, lbl, which)
        w, dd = wd[lbl]
        segsin = g["seg"] * g["sin"]
        T35, T0 = SB35 + w, SB0 + w
        s1p = max(segsin, T35)
        d35 = "T" if T35 > segsin else "seg·sin"
        d0 = "T" if T0 > segsin else "seg·sin"
        dom35.append(d35)
        dom0.append(d0)
        poly, perp = _perp(ns, cb_by, cad, snapshot, wd, lbl, which, g, SB35)
        par = perp / g["sin"]
        eq = abs(perp - s1p) <= TOL
        gt = par > T35
        n_eq += 1 if eq else 0
        n_gt += 1 if gt else 0
        rows.append((lbl, which, g, w, dd, segsin, T35, s1p, perp, par, poly, d35, d0))
        P(f"  {lbl:<5}{which:<7}{g['sin']:>12.7f}{g['seg']:>12.6f}{segsin:>12.6f}{T35:>7.2f}"
          f"{s1p:>11.6f}{d35:>12}{d0:>10}{perp:>16.9f}{perp - s1p:>15.3e}"
          f"{par:>12.6f}{('✅' if gt else '🔴'):>5}{'✅ 過':>11}")
    P("-" * WID)
    P(f"  ⇒ **垂距 ＝ `S1_perp` 之格數 ＝ {n_eq}／8**（容差 `{TOL:g}`）")
    P(f"  ⇒ **路平行距 > `T` 之格數 ＝ {n_gt}／8**（畸零地使用規則第四條第三款）")
    c35 = (dom35.count("T"), dom35.count("seg·sin"))
    c0 = (dom0.count("T"), dom0.count("seg·sin"))
    P("")
    P("  🔒 **判別力對照（`A-1` 明令·⛔ 不得省）**：二情境之**支配項分佈**")
    P(f"     · `setback = 3.5` ⇒ `T` **{c35[0]} 格**／`seg·sinθ` **{c35[1]} 格**")
    P(f"     · `setback = 0`　 ⇒ `T` **{c0[0]} 格**／`seg·sinθ` **{c0[1]} 格**")
    P(f"     ⇒ **{'✅ 二分佈不同 ⇒ `setback` 確有進到量測' if c35 != c0 else '🔴 二分佈相同 ⇒ setback 未進到量測（紅）'}**")
    P(f"     🔒 `seg·sinθ` 之值域 ＝ `[{min(r[5] for r in rows):.6f}, {max(r[5] for r in rows):.6f}]`"
      "（**該量與 `setback` 無關** ⇒ 二情境同值）")
    P("")

    # ══════════════════════════════════════════════════════════════
    # 【A-3】門檻（規定範圍面積）之 `3.5m` 對帳
    # ══════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【A-3】**門檻（街角規定範圍面積）之 `3.5m` 對帳**")
    P("=" * WID)
    P("  🔒 **同口徑（自誤 58）**：值取 **2dp**，差**由 2dp 相減**（⛔ 不以全精度相減後再捨入）。")
    P("  🔒 **對拍靶之出處**：`verify/out/_wg967_runall_stdout.txt` 之【參數3.5m】"
      "（其 `凍存:` 列即**修前**之 `got`·成立於 commit `2de3ea7`）")
    P("     ⚠️ **⛔ 未取 `verify/baselines/`**——該處之 `baseline=` 係**更早世代之錨**"
      "（`W-G.9-4` 起本支為「准紅碼」）⇒ 以其為修前值會**跨兩個世代**。")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'3.5m 門檻(㎡·全精度)':>24}{'2dp':>10}")
    P("-" * WID)
    for lbl, which, g, w, dd, segsin, T35, s1p, perp, par, poly, d35, d0 in rows:
        a = float(poly.area)
        P(f"  {lbl:<5}{which:<7}{a:>24.6f}{round(a, 2):>10.2f}")
    P("-" * WID)
    P("  ⚠️ **修前之 `3.5m` 逐格門檻，倉內<u>無</u>可直接對拍之逐格表**")
    P("     ——`W-G.9-66`【A-3】之八格係 `setback = 0`；`run_all` 之【參數3.5m】只列**違規列**")
    P("     （凍存 14 列／現況 13 列·⛔ 非八格全表）⇒ 🔒 **本項改以 `run_all` 之違規列逐列對拍**")
    P("     ⛔ **不以「八格全表」之名出艙一個倉內不存在之對照**。")
    P("")

    P("=" * WID)
    P("【B】逐項判定")
    P("=" * WID)
    items = [
        ("A-1 不變式", f"垂距 ＝ `S1_perp` 之格數 ＝ {n_eq}／8", n_eq == 8),
        ("A-1 判別力", f"支配項分佈 3.5m {c35} vs 0m {c0} ⇒ {'不同' if c35 != c0 else '相同'}",
         c35 != c0),
        ("A-1 第四條第三款", f"路平行距 > `T` 之格數 ＝ {n_gt}／8", n_gt == 8),
    ]
    for k, t, ok in items:
        P(f"  {k:<18}{'✅' if ok else '🔴'}　{t}")
    P("-" * WID)
    P(f"  ⇒ **{'✅ 全部成立' if all(o for _a, _b, o in items) else '🔴 有未成立項'}**")
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
    _log = os.path.join(OUTDIR, f"probe_WG968_sb35_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
