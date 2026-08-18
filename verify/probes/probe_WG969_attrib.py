#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-69】重烤變動之**成因分解**：乙式（`K-9-5-14`） vs 街廓分配深度（`N-19′`）⛔ 零生產碼

**受詞**：`WV_BAKE` 側錄之 `街角最小面積` 逐格變動，其成因**不止一個**：
  · **乙式**（`K-9-5-14`·`W-G.9-67` 落地）改的是 `S1_perp`；
  · **深度**（`N-19′`·`K-8 §三 commit A` 之 `load_snapshot()` 記憶體注入）改的是 `block_depth`。
二者**同時**作用於 `_build_corner_range_v3` ⇒ 逐格差額**不可逕行歸因於乙式**。

🔒 **分解法（⛔ 非估計·係實跑）**：同一份現行生產碼，只換 `block_depth` 之來源：
  · `D_new` ＝ `rv.load_snapshot()` 之執行期值（＝側錄所用者）；
  · `D_old` ＝ `verify/case_params_UC9898.json` **檔案本體**之值（＝ baseline 烤時所用者）。
  ⇒ `(D_old, 現行碼)` 之值若**逐格回到 baseline**，則該格差額**全部**係深度所致、乙式為 0。

🔒 **儀器沿用既有者**（`build_ctx`／`build_range`／`EIGHT`）——⛔ 未新增第二份判定原語。
🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
for _p in (VERIFY, os.path.join(VERIFY, "fixtures"), HERE):
    sys.path.insert(0, _p)

import run_verification as rv                                       # noqa: E402
from probe_WG960_fitcore import build_ctx, build_range              # noqa: E402
from probe_WG963_eps_tolerance import EIGHT                         # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 132
SNAP_FILE = os.path.join(VERIFY, "case_params_UC9898.json")

# 🔒 **baseline 之現值⛔ 不寫死**——**逐格自 `verify/baselines/退縮{0m,3.5m}參數.csv`
#   之「【左/右】街角最小面積(㎡)」欄現讀**（`fixture-provenance`：期望值須有倉檔出處，
#   ⛔ 非本檔現跑回填、⛔ 更非憑假設寫下）。
#   🩸 **本檔首版曾把 `R6/right` 憑假設寫成 `None`**（實為 `146.38`／`299.13`）
#      ⇒ 已改為現讀，並保留本註記為戒。
BASE_CSV = {0.0: os.path.join(VERIFY, "baselines", "退縮0m參數.csv"),
            3.5: os.path.join(VERIFY, "baselines", "退縮3.5m參數.csv")}


def load_base():
    """自 baseline CSV 現讀八格之街角最小面積；空字串 ⇒ None（該格 baseline 無錨）。"""
    import csv
    out = {}
    for sb, path in BASE_CSV.items():
        d = {}
        with io.open(path, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                for which, col in (("left", "【左】街角最小面積(㎡)"),
                                   ("right", "【右】街角最小面積(㎡)")):
                    v = (r.get(col) or "").strip()
                    d[(r["街廓"], which)] = float(v) if v else None
        out[sb] = d
    return out


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-69】重烤變動之成因分解：乙式（K-9-5-14） vs 街廓分配深度（N-19′）")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("  🔒 ⛔ 零生產碼變更；儀器沿用既有者；同一份碼只換 `block_depth` 之來源。")
    P("")

    ns, cb_by, cad, snapshot, wd, _t = build_ctx()
    d_new = {k: float(snapshot["blocks"][k]["街廓分配深度_m"]) for k in snapshot["blocks"]}
    with io.open(SNAP_FILE, encoding="utf-8") as f:
        d_old = {k: float(v["街廓分配深度_m"])
                 for k, v in (json.load(f)["blocks"]).items()
                 if "街廓分配深度_m" in v}

    P("=" * WID)
    P("【A】`block_depth` 之二源（⛔ 二者皆現查·非憑記憶）")
    P("=" * WID)
    P(f"  {'街廓':<6}{'D_old（快照檔本體）':>22}{'D_new（load_snapshot 執行期）':>30}{'Δ(m)':>12}")
    for k in sorted(d_new):
        P(f"  {k:<6}{d_old.get(k, float('nan')):>22.4f}"
          f"{d_new[k]:>30.4f}{d_new[k] - d_old.get(k, float('nan')):>12.4f}")
    P(f"  🔒 D_old 出處 ＝ `{os.path.relpath(SNAP_FILE, os.path.dirname(VERIFY))}`"
      "（檔案本體）；D_new 出處 ＝ `rv.load_snapshot()`（`K-8 §三` 之記憶體注入）")
    P("")

    P("=" * WID)
    P("【B】街角規定範圍面積之**三態對照**　⇒ 逐格成因分解")
    P("=" * WID)
    P("  🔒 `A(D_old)` ＝ 現行碼 ＋ 舊深度；`A(D_new)` ＝ 現行碼 ＋ 新深度（＝側錄所烤者）")
    P("  🔒 判：`A(D_old) ≈ baseline`（差 < 0.005）⇒ **該格差額全部係深度所致、乙式份額 ＝ 0**")
    P("")
    BASE = load_base()
    P(f"  🔒 baseline 之出處（逐格現讀·⛔ 非寫死）：{os.path.relpath(BASE_CSV[0.0], VERIFY)}"
      f"／{os.path.relpath(BASE_CSV[3.5], VERIFY)}")
    P("")
    tot = {"深度": 0, "混": 0, "乙式": 0, "無變動": 0, "無錨": 0}
    for sb in (0.0, 3.5):
        P(f"  ── setback = {sb:g} m " + "─" * 100)
        P(f"  {'街廓':<5}{'側':<7}{'baseline':>11}{'A(D_old)':>12}{'A(D_new)':>12}"
          f"{'Δ總(new−base)':>15}{'Δ深度':>11}{'Δ乙式(old−base)':>17}{'歸因':>10}")
        for lbl, which in EIGHT:
            snapshot["blocks"][lbl]["街廓分配深度_m"] = d_old[lbl]
            a_old = float(build_range(ns, cb_by, cad, snapshot, wd, lbl, which, sb).area)
            snapshot["blocks"][lbl]["街廓分配深度_m"] = d_new[lbl]
            a_new = float(build_range(ns, cb_by, cad, snapshot, wd, lbl, which, sb).area)
            b = BASE[sb][(lbl, which)]
            if b is None:
                tot["無錨"] += 1
                P(f"  {lbl:<5}{which:<7}{'（baseline 無此格）':>11}{a_old:>12.4f}"
                  f"{a_new:>12.4f}{'—':>15}{a_new - a_old:>11.4f}{'—':>17}{'無錨':>10}")
                continue
            d_yi, d_dep, d_all = a_old - b, a_new - a_old, a_new - b
            # 🔒 **先判「該格根本沒變」**（⛔ 不得由 `|Δ乙式|<ε` 逕標「純深度」——
            #   二者皆 ~0 時那是**無變動**、⛔ 非「深度所致」）。門檻取 baseline 之
            #   量測框：CSV 存 2dp ⇒ 半個最低位 ＝ 0.005。
            if abs(d_all) < 0.005:
                tag, key = "無變動", "無變動"
            elif abs(d_yi) < 0.005:
                tag, key = "純深度", "深度"
            elif abs(d_dep) < 0.005:
                tag, key = "純乙式", "乙式"
            else:
                tag, key = "🔴 混", "混"
            tot[key] += 1
            P(f"  {lbl:<5}{which:<7}{b:>11.2f}{a_old:>12.4f}{a_new:>12.4f}"
              f"{d_all:>15.4f}{d_dep:>11.4f}{d_yi:>17.4f}{tag:>10}")
    P("-" * WID)
    P("  ⇒ **" + "／".join(f"{k} {v} 格" for k, v in tot.items()) + "**")
    P("")
    P("=" * WID)
    P("【C】判")
    P("=" * WID)
    P("  🛑 **凡「純深度」或「混」之格，其成因⛔ 非施工單 §三 B-2-3 所訂之乙式因果鏈**")
    P("     （該鏈逐字：`乙式(K-9-5-14) ⇒ S1_perp … ⇒ 該格門檻由 X 變 Y ⇒ 本欄由 A 變 B`）")
    P("  🔒 深度之變動源 ＝ `K-8 §三 commit A` 之 `load_snapshot()` 記憶體注入（`N-19′`），")
    P("     其 baseline 重烤**經 KL 裁為待決**（`U-K8-1`·`run_all` 之『引擎↔快照 脫鉤清單』")
    P("     逐字：「**殘餘脫鉤項＝檔案本體與 v3 baseline 尚未重烤**（U-K8-1＝乙）」）")
    P("  ⇒ 🛑 **依施工單 §三 B-2-4，B-3（原地重烤）⛔ 不得執行；改為只報告。**")
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
    _log = os.path.join(OUTDIR, f"probe_WG969_attrib_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
