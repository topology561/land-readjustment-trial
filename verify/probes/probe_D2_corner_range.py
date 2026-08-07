# -*- coding: utf-8 -*-
r"""**D-2 哨兵**：街角最小規定範圍面積 16 格（⛔ 零碼面·不切換）。

🔒 **正對照哨兵（`==` 反向式）**——切換前 16 格命中**舊值**、切換後命中**新值**。
   ⛔ 只斷言「與前次相同」者不合格（零 diff 有兩種相反解釋）。

🔴 **無鑑別力之 2 格（D-0b §二 明令標示）**：
`0m R6/right`（`145.8835 → 145.8834`）與 `3.5m R6/right`（`298.1445 → 298.1445`）
之舊新兩值**幾乎相同** ⇒ **標「無鑑別力·非通過」**。
⇒ **有效鑑別格 ＝ 14/16**，⛔ **禁記為 16/16**。

**期望值之出處（fixture-provenance·⛔ 非本檔現跑回填）**：
`docs/reports/W-G.7_K6-A2-GEO1_S1構造圖上驗證.md` §三 之 (7) 舊面積／(8) 新面積
（實料 `verify/out/probe_K9_geo1_S1_construction.log` @ `63ae86d`）。
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

OUTDIR = os.path.join(VERIFY, "out")
_TAG = os.environ.get("D_PHASE", "pre")
LOG = os.path.join(OUTDIR, "probe_D2_corner_range_切換前凍存.log" if _TAG == "pre"
                   else "probe_D2_corner_range.log")

# ── 期望值：(舊, 新)·出處見 docstring ────────────────────────────────────
EXP = {
    ("0m", "R1", "left"): (114.7072, 114.9397),
    ("0m", "R1", "right"): (116.8414, 110.1749),
    ("0m", "R2", "left"): (227.1050, 152.9867),
    ("0m", "R3", "right"): (226.6930, 153.8039),
    ("0m", "R4", "left"): (135.1873, 116.0784),
    ("0m", "R4", "right"): (137.0042, 111.0215),
    ("0m", "R5", "left"): (217.9702, 146.4818),
    ("0m", "R6", "right"): (145.8835, 145.8834),      # 🔴 無鑑別力
    ("3.5m", "R1", "left"): (230.8098, 225.4248),
    ("3.5m", "R1", "right"): (232.7931, 226.1260),
    ("3.5m", "R2", "left"): (384.1511, 308.1618),
    ("3.5m", "R3", "right"): (383.6669, 307.7486),
    ("3.5m", "R4", "left"): (251.1151, 225.0039),
    ("3.5m", "R4", "right"): (252.8551, 225.4208),
    ("3.5m", "R5", "left"): (371.1713, 299.6868),
    ("3.5m", "R6", "right"): (298.1445, 298.1445),    # 🔴 無鑑別力
}
# 🔴 無鑑別力之格（|舊−新| < 判準容差 ⇒ `==` 兩邊皆真 ⇒ 不能證明任何事）
BLIND = {("0m", "R6", "right"), ("3.5m", "R6", "right")}
TOL = 1e-4


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 190)
    L.append(f"【D-2 哨兵】街角最小規定範圍面積 16 格 — 相位 ＝ "
             f"**{'切換前（凍存）' if _TAG == 'pre' else '切換後'}**")
    L.append("=" * 190)
    L.append("  🔒 **正對照（`==` 反向式）**：切換前命中**舊值**、切換後命中**新值**。")
    L.append(f"  🔒 判準容差 `{TOL:g}`（**先行宣告**·⛔ 未由結果反推）。")
    L.append("  🔴 **無鑑別力 2 格**：`0m R6/right`／`3.5m R6/right`——舊新兩值差 < 容差"
             "⇒ `==` 兩邊皆真、**不能證明任何事** ⇒ 標「**無鑑別力·非通過**」。")
    L.append("     ⇒ **有效鑑別格 ＝ 14/16**，⛔ **禁記為 16/16**。")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    L.append("")
    L.append("【A】逐格（**16 格**）")
    L.append("-" * 190)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'實測面積':>13}{'期望(舊)':>12}{'期望(新)':>12}"
             f"{'|Δ舊|':>11}{'|Δ新|':>11}{'舊新間距':>11}  判定")
    L.append("-" * 190)
    _hit_old = _hit_new = _eff = 0
    _blindn = 0
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
                key = (sb, lbl, which)
                sd = sd_by[lbl][which]
                chi = ns["_make_chamfer_tri_wb"](b, which)
                try:
                    rng = ns["_build_corner_range_v3"](
                        b.get("vertices"), b.get("centroid"), [fl["p1"], fl["p2"]], bp,
                        [sd["p1"], sd["p2"]], al_by.get(lbl), depth, setback, legal_w, chi,
                        dxf_quantum=((bl_by.get(lbl) or {}).get("_match") or {}).get("q_detected"),
                        _label=lbl, _side=which)
                    _a = float(rng.area)
                except RuntimeError as e:
                    L.append(f"{sb:<6}{lbl + '/' + which:<12}  🔴 raise：{str(e).splitlines()[0][:70]}")
                    continue
                _o, _n = EXP.get(key, (float("nan"), float("nan")))
                _do, _dn = abs(_a - _o), abs(_a - _n)
                _gap = abs(_o - _n)
                _blind = key in BLIND
                if _blind:
                    _blindn += 1
                    _verd = "🔴 **無鑑別力·非通過**（舊新間距 < 容差）"
                else:
                    _eff += 1
                    if _do <= TOL and _dn > TOL:
                        _verd = "✅ 命中**舊值**（切換前態）"
                        _hit_old += 1
                    elif _dn <= TOL and _do > TOL:
                        _verd = "✅ 命中**新值**（切換後態）"
                        _hit_new += 1
                    else:
                        _verd = "🔴 兩者皆不命中（或皆命中）⇒ **異常·停查**"
                L.append(f"{sb:<6}{lbl + '/' + which:<12}{_a:>13.4f}{_o:>12.4f}{_n:>12.4f}"
                         f"{_do:>11.6f}{_dn:>11.6f}{_gap:>11.6f}  {_verd}")
    L.append("-" * 190)
    L.append(f"  **有效鑑別格 ＝ {_eff}/16**（無鑑別力 {_blindn} 格·⛔ 已排除·禁計入）")
    L.append(f"  命中**舊值** **{_hit_old}/{_eff}**　／　命中**新值** **{_hit_new}/{_eff}**")
    L.append("")
    L.append("【總判】")
    L.append("-" * 190)
    _pre = (_hit_old == _eff and _hit_new == 0)
    _post = (_hit_new == _eff and _hit_old == 0)
    L.append(f"  **切換前態**（有效格全命中舊值）＝ {'✅' if _pre else '🔴'}")
    L.append(f"  **切換後態**（有效格全命中新值）＝ {'✅' if _post else '🔴'}")
    L.append(f"  ⇒ **{'✅ 具鑑別力（恰一態成立）' if _pre != _post else '🔴 無鑑別力·須重設計'}**")
    L.append("  ⛔ 本批**未切換** ⇒ 期望為**切換前態成立**。")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
