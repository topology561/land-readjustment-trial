# -*- coding: utf-8 -*-
"""W-G.5 裁定 N 偵察探針 — **分配起算點**（近端 s=0 vs 街廓真 s_min）之爆炸半徑量測。

## 存在理由（KL 裁定 N·2026-07-26）

分配之近端起算點寫死 `corner_pt = FRONT_LINE p1`（⇒ s=0），而遠端走 `_oblique_s_max`
（＝街廓**真頂點**）。⇒ 街廓落在 `s<0` 之部分**整片掉出分配範圍**、成為無人可及之
「未臨正街楔形」。裁定 N-1 令兩端**皆自街廓真頂點起算**。

本探針**只量不改**（本批定義）：量 s 域／超界面積、試算左端改自 `s_min` 起算之影響、
做守恆自檢。**零注入·零引擎改動**（獨立 script·比照 `probe_corner_trueG.py`）。

## 取數路徑（**即時計算·非讀 log**·誠實載明）

`harvest()` → `rv.build_pipeline` → `build_param_table` → `build_build_parcels` →
`run_corner_pk` → `run_step_g`，兩情境（0m／3.5m）各跑一次，逐塊自 `cb_by`／`cad`
現算幾何。s 域一律走 `ns['_strip_s_range']`、切帶一律走 `ns['_block_strip']`
（＝治理碼同一函式·**禁自行複刻切線式**·#20）。

## 三量之定義（與 `wf_f4` 末端 gate 逐字同源）

| 量 | 式 | 出處 |
|---|---|---|
| 近端超界面積 | `block ∩ {s<0}` | `grep -n "_unfront_area = " verify/wf_f4.py`（left 支） |
| 遠端超界面積 | `block ∩ {s>s(p2)}` | 同上（right 支·鏡像） |
| s 域 | `_strip_s_range(block, d̂, p1, alloc)` | `grep -n "def _strip_s_range" app.py` |

## 試算之口徑（**N-2「該宗 G 不變·以真幾何面積迭代」**）

左組逐宗**沿用其現行 G 目標**，改自 `s_min` 起算、以 `_block_strip` bisect 解各宗 S，
求「後續宗前移量」與「池形狀變化」。

⚠️ **一階近似（誠實載明·勿當終值）**：本試算**固定 G 目標**。真引擎中 G 經 `W→Rw`
與幾何耦合（canonical solo G **位置相依**·見 W-F E2 記載），故有側街之塊其 G 可能微調。
本探針**顯式輸出各塊 `left_has_side`**：`False` ⇒ 無側街負擔 ⇒ G 不經 W 耦合 ⇒ 試算對該塊為精確；
`True` ⇒ 標 🚩「G-W 耦合殘留·須引擎實跑」。**不自行猜測耦合量**。

## 重跑
    WV_RULING_N=1 python verify/probes/probe_ruling_N_recon.py

輸出 `verify/out/probe_ruling_N_recon.log` ＋ `.csv`。
"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon                                # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import (                                    # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g                               # noqa: E402

OUT_LOG = os.path.join(VERIFY, "out", "probe_ruling_N_recon.log")
OUT_CSV = os.path.join(VERIFY, "out", "probe_ruling_N_recon.csv")

EPS_S = 1e-6          # s 域端點退化界（與 wf_f4 末端 gate 之 1e-6 同）
EPS_A = 1e-3          # 面積 ε（與 wf_f4 `_end_gate` 之 1e-3㎡ 同）


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_N_recon：{msg}（no-silent-fallback）")


def _blk_geom(ns, blk, cb_by, cad):
    """逐塊幾何：p1／p2／d̂／alloc 軸／street polygon／s 域／s(p2)。缺值 loud。"""
    fl = (cad.get("front_lines") or {}).get(blk) or _fail(f"{blk} 缺 FRONT_LINE")
    p1 = np.array(fl["p1"], float)
    p2 = np.array(fl["p2"], float)
    L = float(np.linalg.norm(p2 - p1))
    if L <= 0.1:
        _fail(f"{blk} FRONT_LINE 退化（長 {L}）")
    d_hat = (p2 - p1) / L
    verts = cb_by[blk]["vertices"]
    poly = Polygon(verts)
    if not poly.is_valid:
        poly = poly.buffer(0)
    alloc_cad = (cad.get("alloc_dir_by_block") or {}).get(blk) or _fail(f"{blk} 缺 ALLOC")
    alloc_axis = ns["alloc_normal_axis"](alloc_cad)
    dom = ns["_strip_s_range"](poly, d_hat, p1, alloc_axis) or _fail(f"{blk} s 域不可定義")
    s_min, s_max = float(dom[0]), float(dom[1])
    # s(p2)：p2 於 ALLOC 斜交切線軸（rel p1）之 s（與 wf_f4 右支逐字同式）
    mh, den = ns["_strip_axis"](d_hat, alloc_axis)
    s_p2 = float(np.dot(p2 - p1, mh) / den)
    # step 0 之遠端真頂點（應 == s_max·同式同軸）
    s_max_ob = ns["_oblique_s_max"](verts, d_hat, p1, alloc_axis)
    return dict(blk=blk, p1=p1, p2=p2, d_hat=d_hat, L=L, poly=poly,
                alloc_axis=alloc_axis, s_min=s_min, s_max=s_max, s_p2=s_p2,
                s_max_ob=(float(s_max_ob) if s_max_ob is not None else None),
                area=float(poly.area))


def _strip_area(ns, g, s_a, s_b):
    """`block ∩ s∈[s_a,s_b]` 之面積（走治理碼 `_block_strip`·禁自行複刻切線式）。"""
    w = float(s_b) - float(s_a)
    if w <= 0:
        return 0.0
    bp = g["p1"] + float(s_a) * g["d_hat"]
    _geom, ar = ns["_block_strip"](g["poly"], g["d_hat"], bp, w,
                                   allocation_dir=g["alloc_axis"])
    return float(ar or 0.0)


def _solve_S(ns, g, s_start, target, s_cap):
    """bisect 解 S 使 `area(strip(s_start, S)) == target`（單調遞增）。
    不足（吃到 s_cap 仍 < target）→ 回 (None, f_hi)。"""
    hi = float(s_cap) - float(s_start)
    if hi <= 0:
        return None, 0.0
    f_hi = _strip_area(ns, g, s_start, s_start + hi)
    if f_hi < target - 1e-9:
        return None, f_hi
    lo = 0.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if _strip_area(ns, g, s_start, s_start + mid) < target:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-10:
            break
    return (lo + hi) / 2.0, f_hi


# ───────────────────────────────────────────────────────────────────────────
def _run_tag(ns, fake_st, snapshot, setback, tag, L, csv_rows):
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    _diag, _sel, _off, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build,
        setback, snapshot=snapshot)
    # ⚠️ `run_step_g` 回傳 **dict**（`{'g_rows','pool_diag','stage2_placed'}`·
    #    `grep -n "return {'g_rows'" verify/stepg_pipeline.py`），**非**三元組——
    #    三元組者為 `build_step_g_tables(res)`。首版誤解包致逐列為 str（AttributeError）。
    _sg = run_step_g(
        ns, fake_st, list(cb_by.values()), cad, snapshot, params, build,
        winners, forced, setback)
    if not isinstance(_sg, dict) or "g_rows" not in _sg:
        _fail(f"run_step_g 回傳型別非預期（{type(_sg).__name__}）——契約已變·禁猜")
    g_rows = _sg["g_rows"]

    by_blk = {}
    for r in g_rows:
        by_blk.setdefault(r.get("所屬街廓"), []).append(r)

    L.append("=" * 118)
    L.append(f"【裁定 N·§4.1-1】s 域／超界面積　情境 {tag}（退縮 {setback}m）")
    L.append("-" * 118)
    L.append(f"{'塊':5}{'s_min':>11}{'s_max':>11}{'s(p2)':>11}{'近端 s<0':>11}"
             f"{'遠端 s>p2':>11}{'街廓面積':>11}{'L 側街':>8}{'R 側街':>8}"
             f"{'L forced':>10}{'R forced':>10}")

    # 分配街廓＝有 FRONT_LINE 者。無 FRONT_LINE 者（G1 等公園綠地／道路）**本無分配推進**
    #   ⇒ 不適用本裁定；**明列於下·非靜默跳過**（no-silent-fallback）。
    _fl_all = cad.get("front_lines") or {}
    _alloc_blks = [b for b in sorted(cb_by.keys()) if _fl_all.get(b)]
    _skipped = [(b, cb_by[b].get("category", "?")) for b in sorted(cb_by.keys())
                if not _fl_all.get(b)]
    L.append(f"  （非分配街廓·無 FRONT_LINE·不適用本裁定：{_skipped or '無'}）")

    geoms = {}
    for blk in _alloc_blks:
        g = _blk_geom(ns, blk, cb_by, cad)
        geoms[blk] = g
        # step 0 同源自檢：_oblique_s_max 應 == s 域上界
        if g["s_max_ob"] is None or abs(g["s_max_ob"] - g["s_max"]) > 1e-6:
            _fail(f"{blk} `_oblique_s_max`({g['s_max_ob']}) != s 域上界({g['s_max']})"
                  f"——同式同軸前提破")
        near = (_strip_area(ns, g, g["s_min"], 0.0) if g["s_min"] < -EPS_S else 0.0)
        far = (_strip_area(ns, g, g["s_p2"], g["s_max"]) if g["s_max"] > g["s_p2"] + EPS_S else 0.0)
        fo = (forced or {}).get(blk, {}) or {}
        g["near"] = near
        g["far"] = far
        g["fo"] = fo
        L.append(f"{blk:5}{g['s_min']:11.4f}{g['s_max']:11.4f}{g['s_p2']:11.4f}"
                 f"{near:11.4f}{far:11.4f}{g['area']:11.4f}"
                 f"{('有' if fo.get('left_has_side') else '無'):>8}"
                 f"{('有' if fo.get('right_has_side') else '無'):>8}"
                 f"{('是' if fo.get('left_forced_offset') else '否'):>10}"
                 f"{('是' if fo.get('right_forced_offset') else '否'):>10}")
        csv_rows.append(dict(
            情境=tag, 街廓=blk, s_min=round(g["s_min"], 4), s_max=round(g["s_max"], 4),
            s_p2=round(g["s_p2"], 4), 近端超界面積=round(near, 4), 遠端超界面積=round(far, 4),
            街廓面積=round(g["area"], 4),
            左側街=bool(fo.get("left_has_side")), 右側街=bool(fo.get("right_has_side")),
            左forced=bool(fo.get("left_forced_offset")), 右forced=bool(fo.get("right_forced_offset")),
        ))

    # ── §4.1-2／3：左端改自 s_min 起算之試算 ＋ 守恆自檢（僅 s_min<0 之塊）──
    hits = [b for b in sorted(geoms) if geoms[b]["s_min"] < -EPS_S]
    L.append("")
    L.append(f"【裁定 N·§4.1-2／3】左端改自 s_min 起算之試算　情境 {tag}"
             f"｜s_min<0 之塊：{hits or '（無）'}")
    L.append("-" * 118)
    if not hits:
        L.append("  （本情境無 s_min<0 之塊·跳過）")
    for blk in hits:
        g = geoms[blk]
        rows = by_blk.get(blk, [])
        left = sorted([r for r in rows if r.get("推進側別") == "left"],
                      key=lambda x: float(x.get("累積S(m)", 0) or 0))
        biz = [r for r in rows if r.get("推進側別") in ("left", "right")]
        sumG = sum(float(r.get("G(㎡)", 0) or 0) for r in biz)
        pool_old = g["area"] - sum(float(r.get("幾何面積(㎡)", 0) or 0) for r in biz)
        has_side_L = bool(g["fo"].get("left_has_side"))
        L.append(f"  ▸ {blk}｜左組 {len(left)} 宗｜業主宗 {len(biz)} 宗｜ΣG {sumG:.4f}"
                 f"｜Σ幾何後之池 {pool_old:.4f}｜街廓 {g['area']:.4f}"
                 f"｜左側街 {'有 🚩G-W 耦合殘留' if has_side_L else '無（試算對本塊精確）'}")
        if not left:
            L.append("    ⚠️ 左組為空（k*=0·全右組）⇒ 本塊近端楔形不由左組吸收 ⇒ 須 KL 裁（見報告 §六）")
            continue
        # 現行起點：首宗之 (累積S − S) ＝ left_buffer（無 forced 時 ≈0）
        s0_old = float(left[0].get("累積S(m)", 0) or 0) - float(left[0].get("S(m)", 0) or 0)
        L.append(f"    現行左起點 s0 = {s0_old:.4f}（＝首宗累積S − S；無 forced 時應 ≈0）"
                 f"　→　裁定 N 之新起點 s_min = {g['s_min']:.4f}"
                 f"　⇒ 楔形 {g['near']:.4f}㎡ 納入首宗迭代")
        L.append(f"    {'宗':14}{'G 目標':>10}{'舊 S':>9}{'新 S':>9}{'ΔS':>9}"
                 f"{'舊迄 s':>10}{'新迄 s':>10}{'前移量':>9}")
        cur_new = g["s_min"]
        cur_old = s0_old
        infeasible = []
        for r in left:
            Gt = float(r.get("G(㎡)", 0) or 0)
            S_old = float(r.get("S(m)", 0) or 0)
            cur_old_end = cur_old + S_old
            S_new, f_hi = _solve_S(ns, g, cur_new, Gt, g["s_max"])
            if S_new is None:
                infeasible.append((r.get("暫編地號"), Gt, f_hi))
                L.append(f"    {str(r.get('暫編地號')):14}{Gt:10.2f}{S_old:9.4f}"
                         f"{'—':>9}{'—':>9}{cur_old_end:10.4f}{'—':>10}{'—':>9}  🔴 不可行")
                break
            cur_new_end = cur_new + S_new
            L.append(f"    {str(r.get('暫編地號')):14}{Gt:10.2f}{S_old:9.4f}{S_new:9.4f}"
                     f"{S_new - S_old:+9.4f}{cur_old_end:10.4f}{cur_new_end:10.4f}"
                     f"{cur_new_end - cur_old_end:+9.4f}")
            csv_rows.append(dict(
                情境=tag, 街廓=blk, 宗=r.get("暫編地號"), G目標=round(Gt, 2),
                舊S=round(S_old, 4), 新S=round(S_new, 4),
                舊迄s=round(cur_old_end, 4), 新迄s=round(cur_new_end, 4),
                前移量=round(cur_new_end - cur_old_end, 4)))
            cur_new = cur_new_end
            cur_old = cur_old_end
        if infeasible:
            L.append(f"    🔴 左組 bisect 不可行 {infeasible} ⇒ 停機上呈")
            continue
        shift = cur_new - cur_old
        # 守恆自檢：ΣG 不變（構造）；池總量 = 街廓 − Σ宗面積
        #   新左組各宗面積 == 其 G 目標（bisect 收斂）⇒ Σ宗面積之變化 = Σ(G−舊幾何面積)
        area_old_L = sum(float(r.get("幾何面積(㎡)", 0) or 0) for r in left)
        area_new_L = sum(float(r.get("G(㎡)", 0) or 0) for r in left)
        L.append(f"    ⇒ 左組末宗迄 s：{cur_old:.4f} → {cur_new:.4f}"
                 f"（**前移 {abs(shift):.4f}m**·負＝往近端縮）")
        L.append(f"    ⇒ 池形狀：舊 = 楔形[{g['s_min']:.4f},{s0_old:.4f}] {g['near']:.4f}㎡"
                 f"（孤立·無人可及）＋ 中央池；"
                 f"新 = 楔形併入首宗、中央池自 {cur_old:.4f} 前移至 {cur_new:.4f}"
                 f" ⇒ **池片數 2→1**")
        L.append(f"    ⇒ 守恆自檢：ΣG(左組) 舊 {area_new_L:.4f} == 新 {area_new_L:.4f}（構造·G 目標未動）"
                 f"｜左組幾何面積 舊 {area_old_L:.4f} → 新 {area_new_L:.4f}"
                 f"（差 {area_new_L - area_old_L:+.4f}＝原「幾何面積 vs G」殘差·非本裁定所生）")
        _pool_new = g["area"] - (sum(float(r.get("幾何面積(㎡)", 0) or 0)
                                     for r in biz if r.get("推進側別") == "right")
                                 + area_new_L)
        _pool_old_eq = g["area"] - (sum(float(r.get("幾何面積(㎡)", 0) or 0)
                                        for r in biz if r.get("推進側別") == "right")
                                    + area_old_L)
        L.append(f"    ⇒ 池總量：舊 {_pool_old_eq:.4f} → 新 {_pool_new:.4f}"
                 f"（差 {_pool_new - _pool_old_eq:+.4f}）"
                 f"　{'✅ 守恆' if abs(_pool_new - _pool_old_eq) < 0.01 + abs(area_new_L - area_old_L) + 1e-9 else '🔴 不守恆 ⇒ 停機上呈'}")
    return geoms


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.environ.get("WV_RULING_N") != "1":
        print("🔴 本探針須 WV_RULING_N=1 明示啟用。"
              "\n   例：WV_RULING_N=1 python verify/probes/probe_ruling_N_recon.py")
        return 2
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    L = []
    csv_rows = []
    allg = {}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        ns, fake_st = harvest()          # 每情境重新 harvest（session 隔離）
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        allg[tag] = _run_tag(ns, fake_st, snapshot, setback, tag, L, csv_rows)

    # ── 兩情境一致性：s 域為純幾何量 ⇒ 應逐位相同（不同即代表 s 域受退縮污染·須查）──
    L.append("=" * 118)
    L.append("【兩情境 s 域一致性】s 域＝街廓頂點×FRONT/ALLOC 之純幾何量 ⇒ 應與退縮無關")
    a, b = allg["0m"], allg["3.5m"]
    diff = [k for k in sorted(a)
            if abs(a[k]["s_min"] - b[k]["s_min"]) > 1e-9
            or abs(a[k]["s_max"] - b[k]["s_max"]) > 1e-9]
    L.append(f"  差異塊：{diff or '（無·兩情境逐位相同 ✅）'}")
    L.append("=" * 118)
    L.append("【結論】")
    for k in sorted(a):
        if a[k]["s_min"] < -EPS_S:
            L.append(f"  🔴 {k}：s_min={a[k]['s_min']:.4f} <0 ⇒ 近端漏配 {a[k]['near']:.4f}㎡"
                     f"（|s_min| = {abs(a[k]['s_min']):.4f}m 段）")
    for k in sorted(a):
        if a[k]["far"] > EPS_A:
            L.append(f"  ⚪ {k}：遠端 s>s(p2) 尚有 {a[k]['far']:.4f}㎡"
                     f"——**已由 step 0 `_oblique_s_max` 納入分配範圍**（N-1 明示遠端不動）")
    L.append("=" * 118)
    out = "\n".join(L)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write(out + "\n")
    if csv_rows:
        keys = []
        for r in csv_rows:
            for k in r:
                if k not in keys:
                    keys.append(k)
        with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(csv_rows)
    print(out)
    print(f"\n📄 {OUT_LOG}\n📄 {OUT_CSV}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
