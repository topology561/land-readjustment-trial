# -*- coding: utf-8 -*-
r"""**D-2 §二**：切換**之前**之凍存（⛔ 必須於 §一 切換前執行）。

凍存三項：
1. 街角最小規定範圍面積 **16 格**（現值 ＝ 舊構造）
2. `right_forced_offset` 現況（**應 `3.5m R1/right = True`**·D-1 之後果）
3. `run_all` 名目數／PASS／FAIL（自**已入庫**之 `verify/out/D1_runall.log` 現讀·⛔ 不重跑）

🔒 本檔輸出 `verify/out/probe_D2切換前凍存.log`——**一字不得改**。
⛔ 與 D-0b 之 `probe_D2_corner_range_切換前凍存.log` **不同檔**（該檔凍的是 D-1 之前）。
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
# 🔒 檔名帶批次識別（⛔ 禁寫入他批已入庫之 log 檔名）——由 `FREEZE_TAG` 指定
_FT = os.environ.get("FREEZE_TAG", "D2")
LOG = os.path.join(OUTDIR, f"probe_{_FT}切換前凍存.log")
RUNALL = os.path.join(OUTDIR, os.environ.get("FREEZE_RUNALL", "D1_runall.log"))


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 190)
    L.append("【D-2 §二】**切換前**凍存（⛔ 執行於 §一 切換之前·⛔ 本檔一字不得改）")
    L.append("=" * 190)

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    # ── 1. 街角規定範圍面積 16 格 ──────────────────────────────────────
    L.append("")
    L.append("【1】街角最小規定範圍面積 **16 格**（現值 ＝ 舊構造·`_build_corner_range_v3`）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'面積(現值)':>16}")
    L.append("-" * 190)
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            fl = fl_by.get(lbl) or {}
            if not (fl.get("p1") and fl.get("p2")):
                continue
            bp = ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices"))
            depth = float((snapshot["blocks"].get(lbl) or {}).get("街廓分配深度_m") or 0.0)
            for which in ("left", "right"):
                if which not in (sd_by.get(lbl) or {}):
                    continue
                sd = sd_by[lbl][which]
                chi = ns["_make_chamfer_tri_wb"](b, which)
                try:
                    rng = ns["_build_corner_range_v3"](
                        b.get("vertices"), b.get("centroid"), [fl["p1"], fl["p2"]], bp,
                        [sd["p1"], sd["p2"]], al_by.get(lbl), depth, setback, legal_w, chi,
                        dxf_quantum=((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected"),
                        _label=lbl, _side=which)
                    L.append(f"{sb:<6}{lbl + '/' + which:<12}{float(rng.area):>16.4f}")
                except RuntimeError as e:
                    L.append(f"{sb:<6}{lbl + '/' + which:<12}  🔴 raise：{str(e).splitlines()[0][:70]}")
    L.append("-" * 190)

    # ── 2. right_forced_offset 現況 ────────────────────────────────────
    L.append("")
    L.append("【2】`forced_offset` 現況（**應 `3.5m R1` 之 `right_forced_offset = True`**）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓':<6}{'left_forced_offset':>22}{'right_forced_offset':>22}")
    L.append("-" * 190)
    _hit = []
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, _win, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in sorted(cb_by):
            fo = (forced or {}).get(lbl) or {}
            _l = bool(fo.get("left_forced_offset", False))
            _r = bool(fo.get("right_forced_offset", False))
            if _l or _r:
                _hit.append(f"{sb} {lbl}（左={_l}／右={_r}）")
            L.append(f"{sb:<6}{lbl:<6}{str(_l):>22}{str(_r):>22}")
    L.append("-" * 190)
    L.append(f"  ⇒ **forced 為真者 {len(_hit)}**：" + ("；".join(_hit) if _hit else "（無）"))

    # ── 3. run_all 名目數（自已入庫之 log 現讀·⛔ 不重跑）──────────────
    L.append("")
    L.append("【3】`run_all` 名目數／PASS／FAIL（**自已入庫之 log 現讀**·⛔ 未重跑）")
    L.append("-" * 190)
    _t = io.open(RUNALL, encoding="utf-8").read()
    _p = _t.count("✅ PASS")
    _f = _t.count("🔴 FAIL")
    L.append(f"  來源：`{os.path.relpath(RUNALL, REPO)}`（D-1 切換後之 run_all）")
    L.append(f"  PASS ＝ **{_p}**　FAIL ＝ **{_f}**　名目總數 ＝ **{_p + _f}**")
    # 🔒 期望值**隨批次而異** ⇒ 由 env 指定；⛔ 不得寫死（寫死者於另一批即自相矛盾·考古節 50）
    _eP = os.environ.get("FREEZE_EXP_PASS")
    _eF = os.environ.get("FREEZE_EXP_FAIL")
    if _eP is None or _eF is None:
        L.append("  ⚠️ 未指定本批之期望值（`FREEZE_EXP_PASS`／`FREEZE_EXP_FAIL`）⇒ **只記錄實測·不作比較**")
    else:
        _eP, _eF = int(_eP), int(_eF)
        L.append(f"  （本批期望：名目數 {_eP + _eF}／{_eP} PASS／{_eF} FAIL）")
        L.append(f"  ⇒ 相符？ PASS {_p == _eP}／FAIL {_f == _eF}／總數 {_p + _f == _eP + _eF}")

    L.append("")
    L.append("🔒 **本檔為切換前之凍存·⛔ 一字不得改。** 切換後之對照見 D-2 §三 哨兵。")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
