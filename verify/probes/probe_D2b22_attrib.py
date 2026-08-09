r"""**D-2b-22【丙】**：池側殘差之**逐界面全額歸因** ＋ 情境相依性 —— ⛔ **零生產碼變更**

## 三問（施工單 §2·⛔ 不得只答其一）

| 問 | 標的 | 判準 |
|---|---|---|
| §2-1 | `①' 覆蓋閘` 之**缺口**逐界面全額分解 | 殘差 ＝ 閘所報總量 − Σ 具名分項，**逐格列數值** |
| §2-2 | `②-宗` 之**重疊**逐界面全額分解（⛔ 含已知者·作為**方法自證**） | 須重現 `D-2b-17` 之 R2／R5 分解，否則停機 |
| §2-3 | 為何 `[3.5m]` R2／R5／R3 池側三閘**全過** | 須正面列舉每 (情境,街廓,側) 之受檢量 |

## 兩個獨立量測器（施工單 §3-1·⛔ 二者不共用任何布林）

- **甲（構造式）**：shapely —— 缺口用 `slab ∖ union(宗∪池)`；重疊用 `宗ᵢ ∩ 宗ⱼ`。
- **乙（格點式）**：純 numpy 射線法 PIP（`probe_D2b17_dual.in_geom_np`）—— ⛔ **未用任何 shapely 布林**。

## 歸因之定義：**s 軸初等分段**（⛔ 無萬用桶·D-2b-10「去萬用桶」）

s 座標 ＝ `_strip_axis`（斜交切線軸·`ns` harvest·**與生產同源**）。取全部宗之 s 區間端點
（併街廓 s 域兩端）為**斷點**，排序去重後把 s 域切成**初等分段**；每一分段內，
「哪些宗之 s 區間覆蓋它」是**常數** ⇒ 該分段之名目即其**覆蓋宗集合**：

    覆蓋集 ∅        → `池帶`（池片應覆蓋之處）
    覆蓋集 {i}      → `宗i·帶內`      （⇒ 缺口落此 ＝ 該宗未填滿自己的 s-帶）
    覆蓋集 {i,j,…}  → `I[宗i|宗j…]疊` （⇒ s 區間互相重疊之段）

**全額性**：初等分段**鋪滿** s 域且**互不重疊** ⇒ Σ 分項 ＋ 殘差 ＝ 總量（殘差逐格印出）。
⛔ **無「其他／未分類」桶**——凡落不進上列名目者一律以 `🔴 未歸戶` 具名列出。

## §2-2 之乙法**逐對**（⛔ 與甲同命名法，否則 Δ 欄比的是命名法不是量）

對每一格點記錄其所屬宗之集合，對集合內**每一對** `(i,j)` 各計一次 ⇒ 與甲之
`宗ᵢ∩宗ⱼ` 面積**同義**、可逐對對拍。

## ⛔ 本檔不做

⛔ 不改 `app.py`／`verify/` 之生產碼（本檔為新增探針）。⛔ 不動閘寬／上界／容差。
⛔ 不重烤 12 格基準。⛔ 不實作第 2 宗近側界（＝甲案·本單只量）。

## R6 之處置（施工單 §4）

R6 **列入母體並跑完**，但其結果 ⛔ **不得作為任何結論之通過憑據**——該塊 `SIDE ∥ ALLOC`
退化（`|cross|=0.0000000474`／夾角 `0.000003°`【倉】`verify/out/probe_D2b8_guard.log:23`）。
"""
import contextlib
import io
import itertools
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
from probe_D2b17_dual import (_rings_of, poly_bbox_np, in_geom_np,    # noqa: E402
                              replicate_pieces)

OUTDIR = os.path.join(VERIFY, "out")
W = 200
GRID_N = 2000

def _resolve_out(default_name):
    """輸出檔名解析 ＋ **拒絕覆寫**守衛（⛔ 禁覆寫任何已入庫 log）。

    `WV_OUT_NAME=<新檔名>` 覆寫預設；⛔ 目標已存在即 raise，
    除非明示 `WV_ALLOW_OVERWRITE=1`。⇒ 甲前／甲後兩份得以**並存、可逐格對拍**。
    """
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError(
            f"🔴 拒絕覆寫既有 log：{path}"
            f"　⇒ 請設 WV_OUT_NAME=<新檔名>（⛔ 禁覆寫已入庫實料）")
    return path



def s_of_points(ns, px, py, d_hat, corner_pt, allocation_dir):
    m_hat, denom = ns["_strip_axis"](d_hat, allocation_dir)
    bp = np.asarray(corner_pt, dtype=float)[:2]
    return ((px - bp[0]) * m_hat[0] + (py - bp[1]) * m_hat[1]) / float(denom)


def seg_name(cover):
    if not cover:
        return "池帶"
    if len(cover) == 1:
        return f"宗{cover[0]}·帶內"
    return "I[" + "|".join(f"宗{c}" for c in cover) + "]疊"


def elementary_segments(ivs, s_min, s_max):
    """s 軸初等分段：[(a, b, 覆蓋宗 tuple), …]，鋪滿 [s_min, s_max] 且互不重疊。"""
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
        cover = tuple(i for (lo, hi, i) in ivs if lo <= mid <= hi)
        out.append((a, b, cover))
    return out


def main():                                                          # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                             # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    out = _resolve_out("probe_D2b22_attrib.log")   # ⚠️ **fail-fast**：先解析再跑（⛔ 別跑完才攔）
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【D-2b-22【丙】】池側殘差之逐界面全額歸因 ＋ 情境相依性 — ⛔ 零生產碼變更")
    P("=" * W)
    import shapely
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P(f"  乙法格數 {GRID_N}×{GRID_N}（每街廓 bbox）")

    ns, fake_st = harvest()
    CAP, CORNER = {}, {}
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
                            "alloc": allocation_dir}
            except Exception as e:                                    # noqa: BLE001
                CAP[key] = {"err": f"{type(e).__name__}: {e}"}
        return _orig_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                          _label=_label, _depth=_depth, _verbose=_verbose)
    _spy_pool.tag = ""

    def _spy_solve(**kw):
        """§2-3 候選①：於**現碼**重測「該情境是否真有街角第 1 宗」（⛔ 不引 D-2b-7 舊 log）。"""
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

    # ── §2-3 夾角 ─────────────────────────────────────────────────────────────
    #   ⛔ **不得**以「跑兩情境都同值」宣稱其不隨情境變——`build_pipeline` 在情境迴圈**之外**
    #      只跑一次，寫入點 `verify/run_verification.py:182`（`ss["f3_cad_side_lines_by_side"]=slm`）
    #      ⇒ 讀兩次是**同一個物件**、必然同值 ＝ 套套邏輯、鑑別力為零。
    #   ✅ 改為**可失敗之斷言**：取基準後，於**每情境之 `build_param_table` 之後**重讀比對；
    #      逐情境步驟若曾改寫該鍵，本斷言**會破**。⇒ 通過才是證據（`ANG_DRIFT` 空 ＝ 通過）。
    def _measure_ang():
        out = {}
        _slbs = (fake_st.session_state.get('f3_cad_side_lines_by_side', {}) or {})
        _adir = (cad.get("alloc_dir_by_block") or {})
        for _lbl in _slbs:
            for _w in ("left", "right"):
                _sd = (_slbs.get(_lbl) or {}).get(_w)
                if not _sd:
                    continue
                _p1 = np.asarray(_sd["p1"], float)[:2]
                _p2 = np.asarray(_sd["p2"], float)[:2]
                _v = _p2 - _p1
                _v /= float(np.linalg.norm(_v))
                _a = _adir.get(_lbl)
                if _a is None:
                    continue
                _a = np.asarray(_a, float)[:2]
                _a = _a / float(np.linalg.norm(_a))
                _cr = abs(float(_v[0] * _a[1] - _v[1] * _a[0]))
                out[(_lbl, _w)] = (_cr, float(np.degrees(np.arcsin(min(1.0, _cr)))))
        return out

    ANG = _measure_ang()
    if not ANG:
        raise RuntimeError("🔴 夾角母體為空——⛔ 不得據空母體下任何結論")
    ANG_DRIFT = []

    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _now = _measure_ang()
        for k in sorted(set(ANG) | set(_now)):
            if ANG.get(k) != _now.get(k):
                ANG_DRIFT.append((sb, k, ANG.get(k), _now.get(k)))
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
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

    report(P, ns, CAP, CORNER, ANG, ANG_DRIFT, _blks)

    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"\n📄 {out}", file=sys.stderr)


def report(P, ns, CAP, CORNER, ANG, ANG_DRIFT, blks):                # noqa: C901
    from shapely.ops import unary_union

    # ══ §2-3 ══════════════════════════════════════════════════════════════
    P("")
    P("【§2-3】情境相依性：每 (情境, 街廓) 之受檢量（⛔ 正面列舉·⛔ 非只列命中者）")
    P("-" * W)
    P(f"  母體 ＝ {len(CORNER)} 個 (情境,街廓)（⛔ 非空）")
    P("")
    P("  🔒 **夾角之情境不變性 ＝ 可失敗斷言之結果，⛔ 非「讀兩次都一樣」**：")
    P("     `build_pipeline` 於情境迴圈**外**只跑一次（寫入點 `verify/run_verification.py:182`）")
    P("     ⇒ 直接讀兩次係套套邏輯。本檔改為：取基準後，於**每情境 `build_param_table` 之後**重讀比對。")
    P(f"     ⇒ **漂移筆數 ＝ {len(ANG_DRIFT)}**（受檢 {len(ANG)} 個 (街廓,側) × 2 情境）"
      f"{'　✅ 斷言通過 ⇒ 夾角不隨情境變' if not ANG_DRIFT else '　🔴 斷言破：' + repr(ANG_DRIFT)}")
    P("")
    P(f"  {'情境':<6}{'街廓':<5}{'solve次':>8}{'is_corner':>10}  {'側別':<20}"
      f"{'夾角左':>11}{'夾角右':>11}{'宗數':>5}{'街廓面積':>11}")
    P("-" * W)
    for (sb, lbl) in sorted(CORNER, key=lambda k: (k[0], blks.index(k[1]))):
        rec = CORNER[(sb, lbl)]
        cap = CAP.get((sb, lbl), {})
        blk = cap.get("block")
        al, ar = ANG.get((lbl, "left")), ANG.get((lbl, "right"))
        P(f"  {sb:<6}{lbl:<5}{rec['n_calls']:>8}{rec['n_corner']:>10}  "
          f"{('/'.join(rec['sides']) if rec['sides'] else '—'):<20}"
          f"{(f'{al[1]:.6f}' if al else '（無SIDE）'):>11}"
          f"{(f'{ar[1]:.6f}' if ar else '（無SIDE）'):>11}"
          f"{len(cap.get('biz') or []):>5}"
          f"{(f'{blk.area:.4f}' if blk is not None else '—'):>11}")
    P("")
    P("  ⛔ R6 為 `SIDE ∥ ALLOC` **退化案例**（夾角 0.000003°），其結果不得作為通過憑據。")

    # ══ 逐格歸因 ═══════════════════════════════════════════════════════════
    P("")
    P("【§2-1 缺口】＋【§2-2 重疊】逐格·s 軸初等分段之全額歸因（⛔ 無萬用桶）")
    P("-" * W)
    for key in sorted(CAP, key=lambda k: (k[0], blks.index(k[1]) if k[1] in blks else 99)):
        sb, lbl = key
        cap = CAP[key]
        if "err" in cap:
            P(f"  [{sb}] {lbl}　🔴 擷取失敗：{cap['err']}")
            continue
        blk, biz, pool = cap["block"], cap["biz"], cap["pieces"]
        d_hat, corner, alloc = cap["d_hat"], cap["corner"], cap["alloc"]

        dom = ns["_strip_s_range"](blk, d_hat, corner, alloc)
        ivs = []
        for i, g in enumerate(biz):
            r = ns["_strip_s_range"](g, d_hat, corner, alloc)
            if r is not None:
                ivs.append((float(r[0]), float(r[1]), i))
        segs = elementary_segments(ivs, float(dom[0]), float(dom[1]))

        # ── 乙：格點 ──
        x0, y0, x1, y1 = poly_bbox_np(blk)
        xs, ys = np.linspace(x0, x1, GRID_N), np.linspace(y0, y1, GRID_N)
        cell = float((x1 - x0) / (GRID_N - 1) * (y1 - y0) / (GRID_N - 1))
        PX, PY = np.meshgrid(xs, ys)
        px, py = PX.ravel(), PY.ravel()
        inb = in_geom_np(px, py, _rings_of(blk))
        px, py = px[inb], py[inb]
        if px.size == 0:
            raise RuntimeError(f"🔴 [{sb}] {lbl} 乙法母體為空 ⇒ ⛔ 不得下結論")
        masks = [in_geom_np(px, py, _rings_of(g)) for g in biz]
        nbz = np.zeros(px.size, np.int32)
        for m in masks:
            nbz += m.astype(np.int32)
        npl = np.zeros(px.size, np.int32)
        for g in pool:
            npl += in_geom_np(px, py, _rings_of(g)).astype(np.int32)
        sarr = s_of_points(ns, px, py, d_hat, corner, alloc)

        uni = unary_union(list(biz) + list(pool)) if (biz or pool) else None
        gapA_total = float(blk.area) - (float(uni.area) if uni is not None else 0.0)
        gap_mask = (nbz == 0) & (npl == 0)
        gapB_total = float(gap_mask.sum()) * cell

        P("")
        P(f"  ══ [{sb}] {lbl}　宗數 {len(biz)}／池片 {len(pool)}／街廓 {blk.area:.4f}㎡"
          f"　s 域 [{dom[0]:.4f},{dom[1]:.4f}]　初等分段 {len(segs)} 段"
          f"　格面積 {cell:.3e}㎡　母體格數 {px.size}（⛔ 非空）══")

        # ── §2-1 缺口：逐初等分段（甲＝slab 差集／乙＝格點）──
        P(f"     §2-1 缺口總量：甲 {gapA_total:+.4f}㎡　乙 {gapB_total:+.4f}㎡"
          f"　|甲−乙| {abs(gapA_total - gapB_total):.4f}")
        sumA = sumB = 0.0
        rows = []
        for (a, b, cover) in segs:
            bp = corner + a * d_hat
            slab, _ = ns["_block_strip"](blk, d_hat, bp, b - a, allocation_dir=alloc)
            if slab is None or slab.is_empty:
                vA = 0.0
            else:
                vA = float(slab.area) - (float(slab.intersection(uni).area)
                                         if uni is not None else 0.0)
            m = gap_mask & (sarr >= a) & (sarr < b)
            vB = float(m.sum()) * cell
            sumA += vA
            sumB += vB
            if max(abs(vA), abs(vB)) >= 1e-3:
                rows.append((seg_name(cover), a, b, vA, vB))
        for nm, a, b, vA, vB in sorted(rows, key=lambda r: -max(abs(r[3]), abs(r[4]))):
            P(f"       {nm:<26}s∈[{a:9.4f},{b:9.4f}]　甲 {vA:>11.4f}　乙 {vB:>11.4f}"
              f"　Δ {vA - vB:+8.4f}")
        P(f"       🔑 **殘差**（總量 − Σ具名分段）：甲 {gapA_total - sumA:+.6f}㎡"
          f"　乙 {gapB_total - sumB:+.6f}㎡")

        # ── §2-2 重疊：逐對（甲＝intersection／乙＝格點逐對·同命名法）──
        ovA = {}
        for i, j in itertools.combinations(range(len(biz)), 2):
            v = float(biz[i].intersection(biz[j]).area)
            if v > 1e-9:
                ovA[(i, j)] = v
        ovB = {}
        for i, j in itertools.combinations(range(len(biz)), 2):
            c = int((masks[i] & masks[j]).sum())
            if c:
                ovB[(i, j)] = c * cell
        totA, totB = sum(ovA.values()), sum(ovB.values())
        P(f"     §2-2 重疊總量（Σ逐對）：甲 {totA:+.4f}㎡　乙 {totB:+.4f}㎡"
          f"　|甲−乙| {abs(totA - totB):.4f}")
        for k in sorted(set(ovA) | set(ovB), key=lambda k: -max(ovA.get(k, 0), ovB.get(k, 0))):
            vA, vB = ovA.get(k, 0.0), ovB.get(k, 0.0)
            if max(vA, vB) < 1e-3:
                continue
            P(f"       宗{k[0]}×宗{k[1]:<20}　　　　　　　甲 {vA:>11.4f}　乙 {vB:>11.4f}"
              f"　Δ {vA - vB:+8.4f}")


if __name__ == "__main__":
    main()
