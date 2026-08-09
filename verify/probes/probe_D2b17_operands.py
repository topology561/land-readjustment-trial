# -*- coding: utf-8 -*-
r"""**D-2b-17 §f-3**：五處未判定運算元之判定（⛔ 以**實執行攔截**判定·非字面推定）。

## 方法
於 R1–R6 × 兩情境之**實跑**中，將 `BaseGeometry.intersection` 換為記錄用 shim，
以 `sys._getframe` 之 `(檔名, 行號)` **歸戶**每一次呼叫 ⇒ 直接回答：

  ① 該行**是否於 R1–R6 之 Step-G 路徑上被執行**（執行次數 0／>0·⛔ 非讀碼推測）；
  ② 其**兩個運算元之型態**（頂點數／面積／緊緻度 `4π·A/P²`）——逐次記錄、取分布。

## 判定基準（⛔ 不用絕對門檻·用**同倉已知類別**作參照）
`:9047`／`:9050`／`:9062` 為 `GB-50` **已判定為 sliver × sliver** 之三處 ⇒ 取其
緊緻度分布為**已知 sliver 參照類**；五處未判定者與之對照。
⛔ 不以變數命名或字面子字串推定（本波已有三次「固定 pattern 代窮舉」之失誤）。

⛔ 本批零生產碼變更。
"""
import io
import math
import os
import sys
import contextlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b17_operands.log")
W = 200

# §f-3 之五處未判定 ＋ GB-50 已判定三處（參照類）
TARGET = {4525: "§f-3 未判定", 9120: "§f-3 未判定", 11379: "§f-3 未判定",
          11391: "§f-3 未判定", 16238: "§f-3 未判定",
          9047: "GB-50 已判定 sliver×sliver", 9050: "GB-50 已判定 sliver×sliver",
          9062: "GB-50 已判定 sliver×sliver"}


def morph(g):
    """運算元型態指標。⛔ 面積／周長自算（shoelace）·不倚賴 shapely。"""
    gt = getattr(g, "geom_type", None)
    if gt == "Polygon":
        ps = [g]
    elif gt in ("MultiPolygon", "GeometryCollection"):
        ps = [p for p in getattr(g, "geoms", []) if getattr(p, "geom_type", None) == "Polygon"]
    else:
        return {"type": gt, "nv": 0, "A": 0.0, "P": 0.0, "cmp": float("nan")}
    nv = 0
    A = 0.0
    P = 0.0
    for p in ps:
        try:
            r = np.asarray(p.exterior.coords, dtype=float)
        except Exception:                                           # noqa: BLE001
            continue
        if len(r) >= 2 and abs(r[0, 0] - r[-1, 0]) < 1e-15 and abs(r[0, 1] - r[-1, 1]) < 1e-15:
            r = r[:-1]
        nv += len(r)
        if len(r) >= 3:
            x, y = r[:, 0], r[:, 1]
            A += abs(0.5 * float(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))))
            d = np.roll(r, -1, axis=0) - r
            P += float(np.hypot(d[:, 0], d[:, 1]).sum())
    cmp_ = (4 * math.pi * A / (P * P)) if P > 0 else float("nan")
    return {"type": gt, "nv": nv, "A": A, "P": P, "cmp": cmp_}


REC = {}


def install_shim():
    """換掉 `BaseGeometry.intersection`，以呼叫端 (檔, 行) 歸戶。"""
    from shapely.geometry.base import BaseGeometry
    orig = BaseGeometry.intersection

    def shim(self, other, *a, **kw):
        try:
            f = sys._getframe(1)
            ln = f.f_lineno
            fn = f.f_code.co_filename
        except Exception:                                           # noqa: BLE001
            ln, fn = -1, "?"
        if ln in TARGET:
            k = (fn, ln)
            d = REC.setdefault(k, {"n": 0, "L": [], "R": []})
            d["n"] += 1
            if len(d["L"]) < 400:
                d["L"].append(morph(self))
                d["R"].append(morph(other))
        return orig(self, other, *a, **kw)

    BaseGeometry.intersection = shim
    return orig


def restore(orig):
    from shapely.geometry.base import BaseGeometry
    BaseGeometry.intersection = orig


def _stat(vals):
    v = [x for x in vals if x == x]                                 # 去 NaN
    if not v:
        return "—"
    v = sorted(v)
    return f"{v[0]:.4f}／{v[len(v)//2]:.4f}／{v[-1]:.4f}"


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-17 §f-3】五處未判定運算元之判定（實執行攔截·⛔ 非字面推定）")
    P("=" * W)
    import shapely
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P("  🔒 歸戶法：`BaseGeometry.intersection` shim ＋ `sys._getframe(1)` 之 (檔, 行)。")
    P("  🔒 參照類：`:9047`／`:9050`／`:9062` ＝ `GB-50` **已判定** sliver×sliver 之三處。")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()

    _orig = install_shim()
    try:
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
        for setback in (0.0, 3.5):
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, wins, forced = run_corner_pk(
                ns, fake_st, cb_all, cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for lbl in _blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass
                print(f"    [{setback:g}m] {lbl} 完畢", file=sys.stderr)
    finally:
        restore(_orig)

    P("")
    P("【f-3】逐處實測（緊緻度 `4π·A/P²`：圓＝1·sliver→0；列 最小／中位／最大）")
    P("-" * W)
    P(f"  {'行':<8}{'類別':<26}{'執行次數':>9}  {'左運算元 緊緻度':<26}{'右運算元 緊緻度':<26}"
      f"{'左頂點':>7}{'右頂點':>7}")
    for ln in sorted(TARGET):
        hit = [(k, v) for k, v in REC.items() if k[1] == ln]
        if not hit:
            P(f"  :{ln:<7}{TARGET[ln]:<26}{0:>9}  "
              f"{'（未執行）':<26}{'':<26}{'—':>7}{'—':>7}")
            continue
        for (fn, _l), d in hit:
            P(f"  :{ln:<7}{TARGET[ln]:<26}{d['n']:>9}  "
              f"{_stat([m['cmp'] for m in d['L']]):<26}"
              f"{_stat([m['cmp'] for m in d['R']]):<26}"
              f"{max((m['nv'] for m in d['L']), default=0):>7}"
              f"{max((m['nv'] for m in d['R']), default=0):>7}")
            P(f"           檔＝{fn}")
            P(f"           左 面積 最小/中位/最大 = {_stat([m['A'] for m in d['L']])}"
              f"　右 面積 = {_stat([m['A'] for m in d['R']])}")
    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n→ {LOG}", file=sys.stderr)


if __name__ == "__main__":
    main()
