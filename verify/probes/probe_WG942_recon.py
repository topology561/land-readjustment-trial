#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-42】§C 施工前之**純偵察**（⛔ 零判定·⛔ 零出艙碼·⛔ 不動任何生產碼）。

🔒 **立案理由**：`W-G.9-42` §C-2 令「近／遠側界之判別**⛔ 不得由形狀回推**」，
  並指 `solve_G_binary` 之 `near_dir` 為正解來源。惟 `near_dir` 係**求解當下**之引數，
  於**事後逐列掃描**之探針處是否可得，**⛔ 不得假設** ——
  `CLAUDE.md` 節奏第一條逐字：偵察（**禁假設**）。
  本檔只**印出實況**（母體形狀、欄位、排序、s 區間、街角旗標），
  供 §C 之修法據實選型；⛔ 不下任何結論。

🔒 **母體之界定**：沿用 `probe_K9_6_parcel_band.py` 之家法
  （`推進側別 ∈ {'left','right'}`·⛔ **非**以有無 `cut_coords` 為篩）
  ——⚠️ 抵費地有真幾何但不量寬度，以幾何為篩會稀釋分母。
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

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
SB = 0.0            # ＝ `W-G.9-41` 探針之情境（母體 59 宗之出處）


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def main():
    L = []

    def P(s=""):
        L.append(s)

    ns, fake_st = harvest()
    for _s in ("parcel_min_width_n14", "_n14_band_hi", "_n14_band_geom",
               "get_min_lot_size", "_baseline_pts_from_manual",
               "_baseline_normal_axis", "solve_G_binary"):
        P(f"  harvest 取得 {_s}：{callable(ns.get(_s))}")
    P(f"  _EPS_TOUCH_FRONT ＝ {ns.get('_EPS_TOUCH_FRONT')}")
    P("")

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
    # 🔴 **實測所迫之改法（⛔ 非原設計）**：整批 `run_step_g` 於 **R2** 之
    #   「②-宗 圍堵閘」raise ⇒ **整趟中止、`g_rows` 取不到**（`REAL_rc=1`·首版實證）。
    #   ⇒ 改**逐街廓**各自一個 `try`（同 `W-G.9-13` 考古 70 之家法），
    #     並**逐街廓具名**其成敗；⛔ 不以「取不到」一句帶過。
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
            ERR[lbl] = f"{type(e).__name__}: {str(e).splitlines()[0][:140]}"
    P("【A0】逐街廓 `run_step_g` 之成敗（⛔ 逐街廓具名·⛔ 不彙總）")
    for lbl in BLKS:
        P(f"    {lbl}: {'🔴 raise ' + ERR[lbl] if lbl in ERR else '✅ 成功'}")
    P(f"    ⇒ 成功 {len(BLKS)-len(ERR)}／{len(BLKS)} 街廓；`g_rows` 累計 {len(g_rows)} 列")
    P("")

    P("=" * 150)
    P(f"【A】`g_rows` 全量（setback ＝ {SB:g}m）⇒ **{len(g_rows)}** 列（⛔ 未過濾）")
    P("=" * 150)
    keys = set()
    for r in g_rows:
        keys |= set(r.keys())
    P("  欄位全集（排序後·⛔ 逐字）：")
    P("    " + " | ".join(sorted(keys)))
    P("")
    dist = {}
    for r in g_rows:
        dist[str(r.get("推進側別"))] = dist.get(str(r.get("推進側別")), 0) + 1
    P("  `推進側別` 之分布（⛔ 未過濾·含將被剔除者）：")
    for k, v in sorted(dist.items()):
        P(f"    `{k}`：{v} 列")
    P("")

    rows = [r for r in g_rows if str(r.get("推進側別")) in ("left", "right")]
    P(f"  母體（`推進側別 ∈ {{left,right}}`）＝ **{len(rows)}** 列")
    ncorner = sum(1 for r in rows if str(r.get("街角地", "")).strip() == "是")
    P(f"    其中 `街角地 == 是`：**{ncorner}** 列")
    P(f"    `cut_coords` 長度 < 3 者：{sum(1 for r in rows if len(r.get('cut_coords') or []) < 3)} 列")
    P("")

    P("=" * 150)
    P("【B】逐列（**依 `g_rows` 原序**·⛔ 未重排）：s 區間 ＝ 於該街廓 (s,t) 框沿 d̂ 之投影")
    P("=" * 150)
    P(f"  {'序':<4}{'街廓':<5}{'側別':<7}{'暫編地號':<14}{'街角':<5}"
      f"{'面積㎡':>11}{'角點':>5}{'s_min':>11}{'s_max':>11}{'s_中':>11}")
    P("-" * 150)
    for k, r in enumerate(rows):
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        side = str(r.get("推進側別") or "")
        cc = r.get("cut_coords") or []
        fl = fl_by.get(lbl) or {}
        smin = smax = float("nan")
        if fl.get("p1") and fl.get("p2") and len(cc) >= 2:
            p1, p2 = fl["p1"], fl["p2"]
            dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
            Lf = math.hypot(dx, dy)
            dh = (dx / Lf, dy / Lf)
            ss = [(float(p[0]) - float(p1[0])) * dh[0]
                  + (float(p[1]) - float(p1[1])) * dh[1] for p in cc]
            smin, smax = min(ss), max(ss)
        try:
            ar = float(r.get("幾何分配(㎡)") or 0.0)
        except Exception:                                           # noqa: BLE001
            ar = float("nan")
        P(f"  {k:<4}{lbl:<5}{side:<7}{gid:<14}"
          f"{('是' if str(r.get('街角地','')).strip()=='是' else '否'):<5}"
          f"{ar:>11.4f}{len(cc):>5}{smin:>11.4f}{smax:>11.4f}{(smin+smax)/2:>11.4f}")

    P("")
    P("=" * 150)
    P("【C】BASELINE／FRONT_LINE 之供給形狀（⛔ 只印·不判）")
    P("=" * 150)
    for lbl in sorted({str(r.get("所屬街廓")) for r in rows}):
        fl = fl_by.get(lbl) or {}
        bl = bl_by.get(lbl) or {}
        bp = None
        try:
            bp = ns["_baseline_pts_from_manual"](bl, (cb_by.get(lbl) or {}).get("vertices"))
        except Exception as e:                                       # noqa: BLE001
            bp = f"raise {type(e).__name__}"
        ax = None
        try:
            ax = ns["_baseline_normal_axis"](bp)
        except Exception as e:                                       # noqa: BLE001
            ax = f"raise {type(e).__name__}"
        P(f"  {lbl}: front_lines keys={sorted(fl.keys())}  baselines keys={sorted(bl.keys())}")
        P(f"        _baseline_pts_from_manual ⇒ {type(bp).__name__} "
          f"{(str(bp)[:90]) if not isinstance(bp,str) else bp}")
        P(f"        _baseline_normal_axis     ⇒ {ax if isinstance(ax,str) else [round(float(x),6) for x in ax]}")
    return L


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG942_recon_{_short_sha()}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
