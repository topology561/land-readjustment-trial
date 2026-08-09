r"""**D-2b-23【甲】commit A**：甲前量測 —— ⛔ **零生產碼變更**

## 兩件事

| # | 標的 | 施工單 | 停機條件 |
|---|---|---|---|
| **A-1** | **複現** claude.ai 之封閉式 `½ × 街廓深² × tan(夾角)`，逐處對拍實測楔形 | §3-3 | §9-1：無法複現 ⇒ 停機（⛔ 不得逕自照抄他人驗算） |
| **A-2** | 街角資格之**否決原因**（甲前基準）——丙只量到「有沒有」、⛔ 沒量到「為什麼沒有」 | §4 | — |

## A-1 之量測定義（⛔ 每一個選擇都寫明·不藏在碼裡）

- **夾角 θ**：該側 `SIDE_LINE` 單位向量 × 該街廓 `ALLOC_cad` 單位向量之 `|cross|` → `arcsin`
  （與 `verify/probes/probe_D2b7_dirscope.py`【A】**同判準**）。
- **街廓深 D**：⚠️ 「街廓深」有**兩個候選所指**，二者皆列、⛔ 不擇一：
    · `D_prod` ＝ **生產路徑實傳之 `_depth`**（`_pool_strips_for_block(..., _depth=avg_depth_default)`；
      算式見 `grep -n "avg_depth_default = float(" verify/stepg_pipeline.py`：
      `f3_alloc_depth_by_label[blk]` 優先，缺則 `blk_area / front_len`）
    · `D_ratio` ＝ `街廓面積 ÷ s 域跨距`（純幾何代理·⛔ 不經 session 參數）
- **實測楔形（該側）**：
    · **缺口型** ＝ 該側之 `宗·帶內` 分段面積（低 s 段 → **左**／高 s 段 → **右**；
      ∵ `d_hat` ＝ FRONT `p1→p2`、`p1` 為左 ⇒ s 遞增即由左而右）。
    · **重疊型** ＝ 該街角側之宗（＝ s 端點之宗）與其後各宗之交集**總和**。
- **封閉式** ＝ `0.5 * D**2 * tan(θ)`；**比值** ＝ `模型 ÷ 實測`（⛔ 與施工單同向：其云
  「六處落在實測的 0.92–1.02 倍」）。

## A-2 之量測定義

`_pk_one_side_v12`（`grep -n "def _pk_one_side_v12" app.py`）之兩條否決路徑：
`note == '該端無候選'`／`note == '🚫 無人達 G 值門檻 → 該端保留為抵費地'`，
後者逐候選記 `eliminated_reason`（`G 值 X < 最小分配面積 Y`）。
本檔自 `run_corner_pk` 之**診斷 rows** 原樣落地（⛔ 不重算、⛔ 不篩選）。

## ⛔ 本檔不做

⛔ 不改生產碼。⛔ 不動閘寬／容差。⛔ 不重烤基準。⛔ 不實作第 2 宗近側界（＝ commit B）。
⛔ R6 之結果不得作為任何結論之通過憑據（`SIDE ∥ ALLOC` 退化）。
"""
import contextlib
import io
import itertools
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                       # noqa: E402
import run_verification as rv                                         # noqa: E402
from selection_pipeline import run_corner_pk                          # noqa: E402
from stepg_pipeline import run_step_g                                 # noqa: E402
from probe_D2b17_dual import replicate_pieces                         # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 200


def elementary_segments(ivs, s_min, s_max):
    cuts = {float(s_min), float(s_max)}
    for lo, hi, _ in ivs:
        if s_min < lo < s_max:
            cuts.add(float(lo))
        if s_min < hi < s_max:
            cuts.add(float(hi))
    ts = sorted(cuts)
    out = []
    for a, b in zip(ts[:-1], ts[1:]):
        if b - a <= 0:
            continue
        mid = (a + b) / 2.0
        out.append((a, b, tuple(i for (lo, hi, i) in ivs if lo <= mid <= hi)))
    return out


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                             # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-23【甲】commit A】甲前量測：A-1 封閉式複現 ＋ A-2 街角資格否決原因 — ⛔ 零生產碼")
    P("=" * W)
    import shapely
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")

    ns, fake_st = harvest()
    CAP, CORNER, DIAG = {}, {}, {}
    _orig_pool = ns["_pool_strips_for_block"]
    _orig_solve = ns["_solve_G_one"]

    def _spy_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                  _label='', _depth=None, _verbose=True):
        key = (_spy_pool.tag, _label)
        if key not in CAP:
            try:
                pieces, biz = replicate_pieces(ns, block_poly, d_hat, corner_pt,
                                               allocation_dir, biz_polys)
                CAP[key] = {"block": block_poly, "pieces": pieces, "biz": biz,
                            "d_hat": np.asarray(d_hat, float),
                            "corner": np.asarray(corner_pt, float),
                            "alloc": allocation_dir,
                            "depth_prod": (float(_depth) if _depth else None)}
            except Exception as e:                                    # noqa: BLE001
                CAP[key] = {"err": f"{type(e).__name__}: {e}"}
        return _orig_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                          _label=_label, _depth=_depth, _verbose=_verbose)
    _spy_pool.tag = ""

    def _spy_solve(**kw):
        rec = CORNER.setdefault((_spy_solve.tag, _spy_solve.blk),
                                {"n_calls": 0, "n_corner": 0, "sides": []})
        rec["n_calls"] += 1
        if kw.get("is_corner"):
            rec["n_corner"] += 1
            rec["sides"].append(kw.get("side"))
        return _orig_solve(**kw)
    _spy_solve.tag = ""
    _spy_solve.blk = ""

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

    ANG = {}
    _slbs = (fake_st.session_state.get('f3_cad_side_lines_by_side', {}) or {})
    _adir = (cad.get("alloc_dir_by_block") or {})
    for _lbl in _slbs:
        for _w in ("left", "right"):
            _sd = (_slbs.get(_lbl) or {}).get(_w)
            if not _sd:
                continue
            _v = np.asarray(_sd["p2"], float)[:2] - np.asarray(_sd["p1"], float)[:2]
            _v = _v / float(np.linalg.norm(_v))
            _a = _adir.get(_lbl)
            if _a is None:
                continue
            _a = np.asarray(_a, float)[:2]
            _a = _a / float(np.linalg.norm(_a))
            _cr = abs(float(_v[0] * _a[1] - _v[1] * _a[0]))
            ANG[(_lbl, _w)] = math.degrees(math.asin(min(1.0, _cr)))

    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        DIAG[sb] = d0
        for lbl in _blks:
            _spy_pool.tag = sb
            _spy_solve.tag = sb
            _spy_solve.blk = lbl
            ns["_pool_strips_for_block"] = _spy_pool
            ns["_solve_G_one"] = _spy_solve
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                                 # noqa: BLE001
                        pass
            finally:
                ns["_pool_strips_for_block"] = _orig_pool
                ns["_solve_G_one"] = _orig_solve
            print(f"    [{sb}] {lbl} 擷取完畢", file=sys.stderr)

    report(P, ns, CAP, CORNER, DIAG, ANG, _blks)
    out = os.path.join(OUTDIR, "probe_D2b23A_pre.log")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"\n📄 {out}", file=sys.stderr)


def report(P, ns, CAP, CORNER, DIAG, ANG, blks):                     # noqa: C901
    from shapely.ops import unary_union

    P("")
    P("【A-1】封閉式 `½·D²·tan(θ)` 之複現（⛔ 正面列舉全部有街角之 (情境,街廓,側)）")
    P("-" * W)
    P("  D 有兩個所指，二者皆列（⛔ 不擇一）：D_prod ＝ 生產實傳 `_depth`／D_ratio ＝ 街廓面積 ÷ s 域跨距")
    P("")
    P(f"  {'情境':<6}{'街廓':<5}{'側':<6}{'θ(deg)':>10}{'D_prod':>9}{'D_ratio':>9}"
      f"{'實測楔形':>11}{'模型(D_prod)':>13}{'比值':>8}{'模型(D_ratio)':>14}{'比值':>8}  型")
    P("-" * W)
    rows = []
    for key in sorted(CAP, key=lambda k: (k[0], blks.index(k[1]) if k[1] in blks else 99)):
        sb, lbl = key
        cap = CAP[key]
        if "err" in cap:
            P(f"  [{sb}] {lbl}　🔴 擷取失敗：{cap['err']}")
            continue
        if CORNER.get((sb, lbl), {}).get("n_corner", 0) == 0:
            continue                       # 無街角第 1 宗 ⇒ 本表不適用（⛔ 非略過·見 A-2）
        blk, biz, pool = cap["block"], cap["biz"], cap["pieces"]
        d_hat, corner, alloc = cap["d_hat"], cap["corner"], cap["alloc"]
        dom = ns["_strip_s_range"](blk, d_hat, corner, alloc)
        span = float(dom[1]) - float(dom[0])
        D_prod = cap["depth_prod"]
        D_ratio = float(blk.area) / span if span > 0 else float("nan")

        ivs = []
        for i, g in enumerate(biz):
            r = ns["_strip_s_range"](g, d_hat, corner, alloc)
            if r is not None:
                ivs.append((float(r[0]), float(r[1]), i))
        segs = elementary_segments(ivs, float(dom[0]), float(dom[1]))
        uni = unary_union(list(biz) + list(pool)) if (biz or pool) else None

        # 缺口：逐段量；低 s → 左、高 s → 右
        gap_by_side = {"left": 0.0, "right": 0.0}
        mid_s = (float(dom[0]) + float(dom[1])) / 2.0
        for (a, b, cover) in segs:
            if len(cover) != 1:
                continue
            bp = corner + a * d_hat
            slab, _ = ns["_block_strip"](blk, d_hat, bp, b - a, allocation_dir=alloc)
            if slab is None or slab.is_empty:
                continue
            v = float(slab.area) - (float(slab.intersection(uni).area) if uni is not None else 0.0)
            if v < 1e-3:
                continue
            gap_by_side["left" if (a + b) / 2.0 < mid_s else "right"] += v

        # 重疊：以宗之 s 中點定側
        ov_by_side = {"left": 0.0, "right": 0.0}
        for i, j in itertools.combinations(range(len(biz)), 2):
            v = float(biz[i].intersection(biz[j]).area)
            if v <= 1e-9:
                continue
            ri = ns["_strip_s_range"](biz[i], d_hat, corner, alloc)
            rj = ns["_strip_s_range"](biz[j], d_hat, corner, alloc)
            cs = min((ri[0] + ri[1]) / 2.0, (rj[0] + rj[1]) / 2.0) \
                if (ri and rj) else mid_s
            ov_by_side["left" if cs < mid_s else "right"] += v

        for side in ("left", "right"):
            th = ANG.get((lbl, side))
            meas = gap_by_side[side] + ov_by_side[side]
            if th is None and meas < 1e-3:
                continue
            kind = ("缺口" if gap_by_side[side] >= ov_by_side[side] else "重疊")
            m_p = (0.5 * D_prod ** 2 * math.tan(math.radians(th))
                   if (th is not None and D_prod) else float("nan"))
            m_r = (0.5 * D_ratio ** 2 * math.tan(math.radians(th))
                   if th is not None else float("nan"))
            rp = (m_p / meas) if meas > 1e-9 else float("nan")
            rr = (m_r / meas) if meas > 1e-9 else float("nan")
            rows.append((sb, lbl, side, th, D_prod, D_ratio, meas, m_p, rp, m_r, rr, kind))
            P(f"  {sb:<6}{lbl:<5}{('左' if side == 'left' else '右'):<6}"
              f"{(f'{th:.6f}' if th is not None else '（無SIDE）'):>10}"
              f"{(f'{D_prod:.4f}' if D_prod else '—'):>9}{D_ratio:>9.4f}"
              f"{meas:>11.4f}{m_p:>13.4f}{rp:>8.3f}{m_r:>14.4f}{rr:>8.3f}  {kind}")

    P("")
    P(f"  母體 ＝ {len(rows)} 列（⛔ 非空）")
    band = [r for r in rows if r[8] == r[8] and 0.92 <= r[8] <= 1.02]
    outb = [r for r in rows if r[8] == r[8] and not (0.92 <= r[8] <= 1.02)]
    P(f"  以 **D_prod** 計：落於施工單 §3-3 所稱 `0.92–1.02` 帶內 ＝ **{len(band)}** 列／"
      f"帶外 ＝ **{len(outb)}** 列")
    for r in outb:
        P(f"     🔴 帶外：{r[0]} {r[1]} {'左' if r[2] == 'left' else '右'}"
          f"　比值 {r[8]:.3f}　實測 {r[6]:.4f}　模型 {r[7]:.4f}　差 {r[6] - r[7]:+.4f}")
    band2 = [r for r in rows if r[10] == r[10] and 0.92 <= r[10] <= 1.02]
    outb2 = [r for r in rows if r[10] == r[10] and not (0.92 <= r[10] <= 1.02)]
    P(f"  以 **D_ratio** 計：帶內 ＝ **{len(band2)}** 列／帶外 ＝ **{len(outb2)}** 列")
    for r in outb2:
        P(f"     🔴 帶外：{r[0]} {r[1]} {'左' if r[2] == 'left' else '右'}"
          f"　比值 {r[10]:.3f}　實測 {r[6]:.4f}　模型 {r[9]:.4f}　差 {r[6] - r[9]:+.4f}")

    P("")
    P("【A-2】街角資格之否決原因（甲前基準·⛔ 原樣落地·未重算未篩選）")
    P("-" * W)
    for sb in sorted(DIAG):
        for lbl in blks:
            rec = CORNER.get((sb, lbl), {})
            if rec.get("n_corner", 0) != 0:
                continue
            P("")
            P(f"  ── [{sb}] {lbl}　`is_corner` ＝ 0（`_solve_G_one` 呼叫 {rec.get('n_calls')} 次）──")
            drs = [r for r in DIAG[sb] if r.get("街廓") == lbl]
            P(f"     診斷 rows 母體 ＝ {len(drs)} 列"
              f"{'（⛔ 非空）' if drs else '　🔴 **空母體** ⇒ ⛔ 不得據此下結論'}")
            for r in drs:
                P("     " + "　".join(f"{k}={v}" for k, v in r.items()
                                      if not str(k).startswith("_")))


if __name__ == "__main__":
    main()
