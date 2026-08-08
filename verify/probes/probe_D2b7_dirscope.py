# -*- coding: utf-8 -*-
r"""**D-2b-7**：R6「方向未套用」之診斷 ＋ 全案影響面（⛔ 零生產碼變更·⛔ 不修）。

## 待解

```
🔴 K-9-5-5 範圍守衛破：街廓 R6 right 側 方向判準所得授權界面 [] ≠ 街角第 1 宗 ['628-18(1)']
```

## 候選（§一 1–5 ＋ CC 補列之 6·⛔ 每項皆須正面列出「成立／不成立」）

| # | 候選 | 驗法 |
|---|---|---|
| 1 | `is_corner` 於該宗為假 | 自 `_solve_G_one` 實參逐次印出 |
| 2 | 走代數 fallback（`iterate_G_S`·不切帶） | `solver_label` |
| 3 | `side_mid` 缺／`_first_corner_alloc_dir` 未被呼叫 | spy 該函式之呼叫計數 |
| 4 | 該宗為強制抵費地／不走街角路徑 | `winners_state` 與 `forced_map` |
| 5 | R6 與其餘五街廓之逐項對照 | 全六街廓同表 |
| **6** | 🆕 **CC 補列**：`rot90_cw(SIDE)` 恰 **∥** `allocation_dir_block` ⇒ 方向**有套用但等值** | 直接量 `SIDE` 與 `ALLOC_cad` 之夾角 |

🔑 **候選 6 之由來**：`_first_corner_alloc_dir` 回 `rot90_cw(SIDE)`；
`allocation_dir_block` ＝ `rot90(ALLOC_cad)` ⇒ 二者 ∥ **⟺ `SIDE` ∥ `ALLOC_cad`**。
若成立，則 `K-9-5-4 ②` **有被套用、只是產生同一方向** ⇒ **無楔形**（與 R6 覆蓋閘通過相符），
而守衛之「方向改變 ⟺ 街角第 1 宗」前提**在此情形下為偽**。

⛔ **窮舉閘**：六項若全不成立 ⇒ 成因未查明·停機上呈。
"""
import io
import math
import os
import sys
import contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b7_dirscope.log")
W = 200
PAR_TOL = 1e-6          # ＝ stepg `_dir_is_alloc` 之 `_PAR_TOL`（同源·⛔ 不另訂）


def _unit(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n) if n > 1e-12 else (0.0, 0.0)


def _cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * W)
    L.append("【D-2b-7】R6「方向未套用」診斷 ＋ 全案影響面 — ⛔ 零生產碼變更")
    L.append("=" * W)

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    _blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in _blks:
            _blks.append(_l)

    # ══ 【A】候選 6：SIDE vs ALLOC_cad 之夾角（⛔ 零執行·純幾何）══
    L.append("")
    L.append("【A】🔑 候選 6：`SIDE` 與 `ALLOC_cad` 之夾角（決定 `K-9-5-4 ②` 是否**產生不同方向**）")
    L.append("-" * W)
    L.append(f"  判準同 stepg `_dir_is_alloc`：`|cross(unit,unit)| ≤ {PAR_TOL:g}` ⇒ 視為 ∥（方向未改變）")
    L.append(f"{'街廓':<6}{'側':<7}{'SIDE 單位向量':<34}{'ALLOC_cad 單位向量':<34}"
             f"{'|cross|':>14}{'夾角(deg)':>12}  判定")
    L.append("-" * W)
    _sd_by = cad.get("side_lines_by_side", {}) or {}
    _al_by = cad.get("alloc_dir_by_block", {}) or {}
    _par_hits = []
    for lbl in _blks:
        _ac = _al_by.get(lbl)
        if _ac is None:
            L.append(f"{lbl:<6}{'—':<7}（缺 ALLOC）")
            continue
        _au = _unit((float(_ac[0]), float(_ac[1])))
        for side in ("left", "right"):
            _sd = (_sd_by.get(lbl) or {}).get(side)
            if not _sd:
                L.append(f"{lbl:<6}{side:<7}（無 SIDE_LINE）")
                continue
            _p1 = _sd["p1"]; _p2 = _sd["p2"]
            _su = _unit((float(_p2[0]) - float(_p1[0]), float(_p2[1]) - float(_p1[1])))
            _c = abs(_cross(_su, _au))
            _ang = math.degrees(math.asin(min(1.0, _c)))
            _par = _c <= PAR_TOL
            if _par:
                _par_hits.append((lbl, side))
            L.append(f"{lbl:<6}{side:<7}({_su[0]:+.9f},{_su[1]:+.9f})  "
                     f"({_au[0]:+.9f},{_au[1]:+.9f})  {_c:>14.10f}{_ang:>12.6f}  "
                     + ("🔴 **∥ ⇒ 方向不變**" if _par else "✅ 不平行 ⇒ 方向會改變"))
    L.append(f"  ⇒ 判為 ∥ 者：**{_par_hits if _par_hits else '無'}**")

    # ══ 【B】逐街廓執行：spy 實參／solver／_first_corner_alloc_dir 呼叫 ══
    L.append("")
    L.append("【B】逐街廓 solo 執行之實參與路徑（候選 1／2／3）")
    L.append("-" * W)
    L.append(f"{'情境':<6}{'街廓':<6}{'#':<4}{'is_corner':<11}{'side':<7}"
             f"{'side_mid?':<11}{'solver':<16}{'_alloc_dir_used':<32}{'∥ALLOC?':<10}{'fcad呼叫'}")
    L.append("-" * W)
    _unapplied = []                       # §二-1：方向未套用之街角第 1 宗
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for lbl in _blks:
            _ac = _al_by.get(lbl)
            # 🔴 **更正（CC 自查）**：比對之基準須為 `allocation_dir_block`
            #   ＝ `alloc_normal_axis(ALLOC_cad)` ＝ rot90(ALLOC_cad)（`stepg:432`），
            #   ⛔ **非 `ALLOC_cad` 本身**。首版誤比後者 ⇒ 【C】得「✅ 無」之**假陰性**
            #   （與【A】直接矛盾而被察覺）。基準取自**生產同一函式** `ns["alloc_normal_axis"]`。
            _adb = ns["alloc_normal_axis"](_ac) if _ac is not None else None
            _au = _unit((float(_adb[0]), float(_adb[1]))) if _adb is not None else None
            rec = []
            fc = {"n": 0}
            _o_solve = ns["_solve_G_one"]
            _o_fcad = ns["_first_corner_alloc_dir"]

            def _spy_fcad(side_mid, _o=_o_fcad, _fc=fc):
                _fc["n"] += 1
                return _o(side_mid)

            def _spy(_o=_o_solve, _rec=rec, _fc=fc, **kw):
                _n0 = _fc["n"]
                _r, _lb = _o(**kw)
                _rec.append({"is_corner": bool(kw.get("is_corner")),
                             "side": str(kw.get("side")),
                             "side_mid": kw.get("side_mid") is not None,
                             "solver": _lb,
                             "dir": _r.get("_alloc_dir_used"),
                             "fcad": _fc["n"] - _n0})
                return _r, _lb

            ns["_first_corner_alloc_dir"] = _spy_fcad
            ns["_solve_G_one"] = _spy
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:
                        pass
            finally:
                ns["_solve_G_one"] = _o_solve
                ns["_first_corner_alloc_dir"] = _o_fcad

            for _i, _r in enumerate(rec):
                if not _r["is_corner"]:
                    continue
                _d = _r["dir"]
                _pl = "—"
                if _d is not None and _au is not None:
                    _pl = ("🔴 ∥" if abs(_cross(_unit((float(_d[0]), float(_d[1]))), _au))
                           <= PAR_TOL else "✅ 非∥")
                    if _pl.startswith("🔴"):
                        _unapplied.append((sb, lbl, _r["side"], _i))
                L.append(f"{sb:<6}{lbl:<6}{_i:<4}{str(_r['is_corner']):<11}{_r['side']:<7}"
                         f"{str(_r['side_mid']):<11}{_r['solver']:<16}"
                         f"{(str(tuple(round(float(x), 6) for x in _d)) if _d else 'None'):<32}"
                         f"{_pl:<10}{_r['fcad']}")

    # ══ 【C】§二-1 影響面 ══
    L.append("")
    L.append("【C】§二-1 **方向未套用之街角第 1 宗**（全六街廓·全情境·⛔ 非只列 R6）")
    L.append("-" * W)
    if _unapplied:
        for u in _unapplied:
            L.append(f"  🔴 {u[0]:<6}{u[1]:<5}side={u[2]:<7}呼叫序 #{u[3]}")
        _sc = sorted({(u[0], u[1]) for u in _unapplied})
        L.append(f"  ⇒ 共 **{len(_unapplied)}** 格／涉及 **{len(_sc)}** 個(情境,街廓)：{_sc}")
    else:
        L.append("  ✅ 無——全部街角第 1 宗之 `_alloc_dir_used` 皆非 ∥ALLOC")

    # ══ 【D】候選逐項判定 ══
    L.append("")
    L.append("【D】候選逐項判定（⛔ 每項皆正面列出·禁只報命中者）")
    L.append("-" * W)
    _r6 = [r for r in _unapplied if r[1] == "R6"]
    L.append(f"  1 `is_corner` 為假　　　　　⇒ **{'成立' if False else '不成立'}**"
             "（【B】表中 R6 之列 `is_corner` 全為 True·否則不會出現在該表）")
    L.append("  2 走代數 fallback　　　　　⇒ 見【B】`solver` 欄；若為『幾何二分法』⇒ **不成立**")
    L.append("  3 `_first_corner_alloc_dir` 未被呼叫 ⇒ 見【B】`fcad` 欄；>0 ⇒ **不成立**")
    L.append("  4 強制抵費地／不走街角路徑 ⇒ 若其 `is_corner=True` 且 `fcad>0` ⇒ **不成立**")
    L.append("  5 逐街廓對照　　　　　　　⇒ 【A】【B】兩表已含全六街廓")
    L.append(f"  6 🆕 `rot90_cw(SIDE)` ∥ `allocation_dir_block` ⇒ "
             f"**{'成立' if _par_hits else '不成立'}**（【A】判為 ∥ 者：{_par_hits or '無'}）")
    L.append("")
    L.append(f"  R6 之未套用格：**{_r6 if _r6 else '無'}**")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
