#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-37】相鄰性之校正 ＋ 破量交集形狀之實測（⛔ 零生產碼·新檔·⛔ 不改既有探針）

受詞（施工單 W-G.9-37 §1 甲組／§2 乙組）：
  A-2 逐宗量其**空間位置**（沿正街之投影區間／面積／頂點數／MultiPolygon）
  A-3 以**量得之位置**判「空間相鄰」——⛔ 不用編號減法
  B-1 印出破量之**交集多邊形本身**（外接框、投影區間、三算法互證面積）
  B-3 「多邊形面積 − G」逐宗並列

🔒 輸出檔名含產生它的 commit 短碼（`GB-68` 之失效條件方向）。
🔒 掃描母體⛔ 不含自身輸出。
🔒 ⛔ 不覆寫任何既有 log（檔名唯一）。

🔴 索引語意（A-1 現查實得·成立於 acddd6c）：
  `biz[i]` 之序 ＝ `app.py` 生產端 `for _entry, _res in (left_results + right_results)`
  ⇒ **分組串接序**（左組推進序 → 右組推進序），⛔ **非**沿正街之空間位置。
  探針側 `_biz = [p for p in (biz_polys or []) if …]` 僅濾空、**保序**、⛔ 不重排。
"""
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 170


def _short_sha():
    """產生本次執行之 commit 短碼（⛔ 若非 git 樹則回 'nogit'）。"""
    try:
        r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                           cwd=VERIFY, capture_output=True, text=True, timeout=20)
        s = (r.stdout or "").strip()
        return s if s else "nogit"
    except Exception:                                               # noqa: BLE001
        return "nogit"


# ── 幾何小工具（⛔ 不呼叫生產碼·供三算法互證用）────────────────────────────
def _rings(g):
    """回 [(exterior, [holes…])…]；支援 Polygon／MultiPolygon。"""
    out = []
    gt = getattr(g, "geom_type", "")
    if gt == "Polygon":
        out.append((list(g.exterior.coords), [list(r.coords) for r in g.interiors]))
    elif gt in ("MultiPolygon", "GeometryCollection"):
        for p in getattr(g, "geoms", []):
            if getattr(p, "geom_type", "") == "Polygon":
                out.append((list(p.exterior.coords), [list(r.coords) for r in p.interiors]))
    return out


def _shoelace(ring):
    n = len(ring)
    s = 0.0
    for i in range(n - 1):
        x1, y1 = ring[i][0], ring[i][1]
        x2, y2 = ring[i + 1][0], ring[i + 1][1]
        s += x1 * y2 - x2 * y1
    return abs(s) * 0.5


def area_shoelace(g):
    """獨立算法②：對每一環自算 shoelace（外環 − 內環）·⛔ 未用 `.area`。"""
    tot = 0.0
    for ext, holes in _rings(g):
        tot += _shoelace(ext)
        for h in holes:
            tot -= _shoelace(h)
    return tot


def area_grid(g, n=1400):
    """獨立算法③：格點法（bbox 均勻取樣 × 格面積）·⛔ 未用 `.area`。"""
    if g is None or g.is_empty:
        return 0.0, 0.0
    x0, y0, x1, y1 = g.bounds
    if x1 <= x0 or y1 <= y0:
        return 0.0, 0.0
    from shapely.geometry import Point
    dx, dy = (x1 - x0) / n, (y1 - y0) / n
    cell = dx * dy
    hit = 0
    prep = None
    try:
        from shapely.prepared import prep as _prep
        prep = _prep(g)
    except Exception:                                               # noqa: BLE001
        pass
    for i in range(n):
        px = x0 + (i + 0.5) * dx
        for j in range(n):
            py = y0 + (j + 0.5) * dy
            pt = Point(px, py)
            if (prep.contains(pt) if prep is not None else g.contains(pt)):
                hit += 1
    return hit * cell, cell


def proj_interval(g, d_hat):
    """沿 `d_hat`（正街方向）之投影區間 [s_min, s_max]（⛔ 相對座標·同一街廓內可比）。"""
    d = np.asarray(d_hat, dtype=float)
    d = d / (np.hypot(d[0], d[1]) or 1.0)
    ss = []
    for ext, _ in _rings(g):
        for (x, y) in ext:
            ss.append(x * d[0] + y * d[1])
    if not ss:
        return None
    return (min(ss), max(ss))


def nvert(g):
    return sum(len(e) - 1 for e, _ in _rings(g))


def bbox_along(g, d_hat):
    """回 (沿正街之寬, 垂直向之高)。"""
    d = np.asarray(d_hat, dtype=float)
    d = d / (np.hypot(d[0], d[1]) or 1.0)
    n = np.array([-d[1], d[0]])
    ss, ts = [], []
    for ext, _ in _rings(g):
        for (x, y) in ext:
            ss.append(x * d[0] + y * d[1])
            ts.append(x * n[0] + y * n[1])
    if not ss:
        return (0.0, 0.0)
    return (max(ss) - min(ss), max(ts) - min(ts))


def main():
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * W)
    P("【W-G.9-37】相鄰性之校正 ＋ 破量交集形狀之實測")
    P("=" * W)
    import shapely
    P(f"  產生於 commit：{sha}")
    P(f"  環境：shapely {shapely.__version__} | GEOS {shapely.geos_version}")
    P("  🔴 索引語意（A-1 實得）：biz[i] 之序 ＝ left_results + right_results（分組串接）"
      "，⛔ 非沿正街之空間位置")
    P("")

    # ── §0 量測器自檢（⛔ 先自檢後量測）────────────────────────────────────
    P("【0】量測器自檢（⛔ 先自檢後量測·對照組須紅）")
    P("-" * W)
    from shapely.geometry import Polygon as _Pg
    _sq = _Pg([(0, 0), (10, 0), (10, 4), (0, 4)])
    _dh = (1.0, 0.0)
    _iv = proj_interval(_sq, _dh)
    _ok1 = (abs(_iv[0] - 0.0) < 1e-9 and abs(_iv[1] - 10.0) < 1e-9)
    P(f"  ① 已知真：10×4 矩形沿 x 之投影 = [{_iv[0]:.6f}, {_iv[1]:.6f}]"
      f"  期望 [0, 10] ⇒ {'✅' if _ok1 else '🔴'}")
    _sq2 = _Pg([(7, 0), (17, 0), (17, 4), (7, 4)])
    _iv2 = proj_interval(_sq2, _dh)
    _ok2 = (abs(_iv2[0] - 7.0) < 1e-9 and abs(_iv2[1] - 17.0) < 1e-9)
    P(f"  ② 已知偽（平移 +7·區間須跟著變）：[{_iv2[0]:.6f}, {_iv2[1]:.6f}]"
      f"  期望 [7, 17] ⇒ {'✅' if _ok2 else '🔴'}")
    _a_sl = area_shoelace(_sq)
    _a_gr, _cell = area_grid(_sq, 600)
    _ok3 = abs(_a_sl - 40.0) < 1e-9 and abs(_a_gr - 40.0) < 0.05
    P(f"  ③ 三算法對已知 40.0：shapely {_sq.area:.6f}／shoelace {_a_sl:.6f}"
      f"／格點 {_a_gr:.6f}（格 {_cell:.2e}） ⇒ {'✅' if _ok3 else '🔴'}")
    _bw, _bh = bbox_along(_sq, _dh)
    _ok4 = abs(_bw - 10.0) < 1e-9 and abs(_bh - 4.0) < 1e-9
    P(f"  ④ 外接框沿/垂直：{_bw:.6f} × {_bh:.6f}  期望 10 × 4 ⇒ {'✅' if _ok4 else '🔴'}")
    _selftest = _ok1 and _ok2 and _ok3 and _ok4
    P(f"  ⇒ 量測器自檢：{'PASS' if _selftest else '🔴 FAIL ⇒ S-2 ⇒ 本次量測⛔ 不得出艙'}")
    if not _selftest:
        P("")
        P("🛑 量測器紅 ⇒ 停機，⛔ 未進行任何實測。")
        return L, sha

    # ── §1 驅動：spy 攔截 `_pool_strips_for_block` ────────────────────────
    ns, fake_st = harvest()
    CAP = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        key = (_spy.tag, _label, _spy.seq.get((_spy.tag, _label), 0))
        _spy.seq[(_spy.tag, _label)] = _spy.seq.get((_spy.tag, _label), 0) + 1
        _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
        CAP[key] = {"block": block_poly, "d_hat": np.asarray(d_hat, float),
                    "biz": list(_biz)}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)
    _spy.seq = {}
    _spy.tag = ""

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())

    import contextlib
    import io as _io
    G_ROWS = {}
    TARGET_BLK = "R2"
    for sb in (0.0,):                       # ⛔ 只跑 0m（本批受詞）
        _spy.tag = f"{sb:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        _d0, _s2, _o2, wins, forced = run_corner_pk(
            ns, fake_st, cb_all, cad, params, temp_p, build_p, sb, snapshot=snapshot)
        ns["_pool_strips_for_block"] = _spy
        # 🔴 `②-宗 圍堵閘` 於本案 R2 **必破**（正是本批之受詞）⇒ `run_step_g` 必 raise。
        #    spy 已於呼叫 `_orig` **之前**存好 `CAP` ⇒ A-2／A-3／B-1 之幾何量測不受影響；
        #    ⛔ 惟 `g_rows` 因而取不到 ⇒ B-3 之 G 值出艙碼為「未查」（**必然·非本探針之缺陷**）。
        _gerr = ""
        try:
            _buf = _io.StringIO()
            with contextlib.redirect_stdout(_buf):
                try:
                    res = run_step_g(
                        ns, fake_st, cb_all, cad, snapshot, params,
                        [tp for tp in build_p if tp.get("所屬街廓") == TARGET_BLK],
                        wins, forced, sb)
                    G_ROWS[_spy.tag] = (res or {}).get("g_rows") or []
                except Exception as e:                              # noqa: BLE001
                    _gerr = f"{type(e).__name__}: {e}"
                    G_ROWS[_spy.tag] = []
        finally:
            ns["_pool_strips_for_block"] = _orig
        G_ROWS["_err_" + _spy.tag] = _gerr

    # ── §2 A-2／A-3：逐宗位置 ＋ 空間相鄰判定 ────────────────────────────
    TARGET = "R2"
    key = None
    for k in CAP:
        if k[0] == "0m" and k[1] == TARGET:
            key = k
            break
    if key is None:
        P("")
        P(f"🛑 未攔到 {TARGET} 之 0m 呼叫 ⇒ ⛔ 無從量測")
        return L, sha

    blk = CAP[key]["block"]
    d_hat = CAP[key]["d_hat"]
    biz = CAP[key]["biz"]
    blk_iv = proj_interval(blk, d_hat)

    P("")
    P(f"【A-2】{TARGET} `0m` 逐宗位置（⛔ 相對投影座標·同街廓內可比）")
    P("-" * W)
    P(f"  街廓沿正街投影區間 = [{blk_iv[0]:.4f}, {blk_iv[1]:.4f}]  全長 {blk_iv[1]-blk_iv[0]:.4f}")
    P(f"  {'i':<4}{'s_min':>12}{'s_max':>12}{'寬':>10}{'面積':>12}{'頂點':>6}{'Multi':>7}"
      f"{'G值':>12}{'面積−G':>10}")
    IV = []
    grows = G_ROWS.get("0m") or []
    g_by_area = {}
    for r in grows:
        try:
            _ga = float(r.get("幾何面積(㎡)") or 0.0)
            if _ga > 0:
                g_by_area.setdefault(round(_ga, 2), []).append(r)
        except Exception:                                           # noqa: BLE001
            pass
    diffs = []
    for i, g in enumerate(biz):
        iv = proj_interval(g, d_hat)
        IV.append(iv)
        a = float(g.area)
        gt = getattr(g, "geom_type", "")
        cand = g_by_area.get(round(a, 2)) or []
        gv = None
        if len(cand) == 1:
            try:
                gv = float(cand[0].get("G(㎡)") or 0.0)
            except Exception:                                       # noqa: BLE001
                gv = None
        d = (a - gv) if gv is not None else None
        if d is not None:
            diffs.append(d)
        P(f"  {i:<4}{iv[0]:>12.4f}{iv[1]:>12.4f}{iv[1]-iv[0]:>10.4f}{a:>12.4f}"
          f"{nvert(g):>6}{('是' if gt!='Polygon' else '否'):>7}"
          f"{(f'{gv:.4f}' if gv is not None else '未對上'):>12}"
          f"{(f'{d:+.4f}' if d is not None else '—'):>10}")

    # 分界索引：以 s_min 之序是否單調判斷
    P("")
    P("【A-2-a】分組串接之分界索引（⛔ 由量得之位置推·非直讀）")
    P("-" * W)
    breaks = [i for i in range(1, len(IV)) if IV[i][0] < IV[i - 1][0]]
    P(f"  `s_min` 相對前一索引**下降**之處（＝序跳躍點）：{breaks if breaks else '無'}")
    P(f"  ⇒ 若恰 1 個跳躍點 k ⇒ 左組 ＝ i∈[0,k)、右組 ＝ i∈[k,n)；實得跳躍點數 ＝ {len(breaks)}")

    P("")
    P("【A-2 對照】全部宗之投影區間聯集 vs 街廓全長（已知為真之對照）")
    P("-" * W)
    _cov = sorted([iv for iv in IV if iv])
    _merged = []
    for a, b in _cov:
        if _merged and a <= _merged[-1][1] + 1e-9:
            _merged[-1] = (_merged[-1][0], max(_merged[-1][1], b))
        else:
            _merged.append((a, b))
    _len = sum(b - a for a, b in _merged)
    P(f"  聯集長 {_len:.4f} ／ 街廓全長 {blk_iv[1]-blk_iv[0]:.4f}"
      f" ＝ {100.0*_len/max(1e-9,(blk_iv[1]-blk_iv[0])):.2f}%")

    P("")
    P("【A-3】空間相鄰判定（⛔ 用量得之位置·⛔ 不用編號減法）")
    P("-" * W)
    P("  定義：兩宗**空間相鄰** ⇔ 其沿正街之投影區間相接或重疊，且中間無第三宗之區間隔開。")
    P(f"  {'對':<12}{'編號差':>7}{'區間相接?':>12}{'中間隔了哪幾宗':>34}{'空間相鄰?':>12}")
    EPS = 1e-6

    def between(i, j):
        lo = min(IV[i][1], IV[j][1])
        hi = max(IV[i][0], IV[j][0])
        if lo >= hi:                       # 重疊 ⇒ 中間無縫
            return []
        out = []
        for k in range(len(IV)):
            if k in (i, j):
                continue
            if IV[k][0] < lo - EPS or IV[k][1] > hi + EPS:
                # 部分落在間隙內即算隔開
                if IV[k][1] > hi + EPS and IV[k][0] < lo - EPS:
                    out.append(k)
                continue
            out.append(k)
        return out

    for (i, j) in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
        if max(i, j) >= len(IV):
            continue
        touch = not (IV[i][1] < IV[j][0] - EPS or IV[j][1] < IV[i][0] - EPS)
        mid = between(i, j)
        adj = touch and not mid
        P(f"  宗{i}×宗{j:<7}{abs(i-j):>7}{('是' if touch else '否'):>12}"
          f"{(str(mid) if mid else '（無）'):>34}{('是' if adj else '否'):>12}")

    # ── §3 B-1：交集形狀 ────────────────────────────────────────────────
    P("")
    P("【B-1】破量之交集多邊形本身（⛔ 不只印面積·三算法互證）")
    P("-" * W)
    P(f"  {'對':<12}{'shapely':>12}{'shoelace':>12}{'格點':>12}{'最大互差':>10}"
      f"{'頂點':>6}{'Multi':>7}{'框寬(沿街)':>12}{'框高':>10}{'面積/框':>9}"
      f"{'交集投影區間':>26}")
    PAIRS = []
    for i in range(len(biz)):
        for j in range(i + 1, len(biz)):
            v = float(biz[i].intersection(biz[j]).area)
            if v > 0:
                PAIRS.append((i, j, v))
    PAIRS.sort(key=lambda t: -t[2])
    for (i, j, v) in PAIRS:
        inter = biz[i].intersection(biz[j])
        a_sl = area_shoelace(inter)
        a_gr, cell = area_grid(inter, 1200)
        mx = max(abs(v - a_sl), abs(v - a_gr), abs(a_sl - a_gr))
        bw, bh = bbox_along(inter, d_hat)
        iv = proj_interval(inter, d_hat)
        ratio = v / (bw * bh) if bw * bh > 0 else 0.0
        P(f"  宗{i}×宗{j:<7}{v:>12.6f}{a_sl:>12.6f}{a_gr:>12.6f}{mx:>10.6f}"
          f"{nvert(inter):>6}{('是' if getattr(inter,'geom_type','')!='Polygon' else '否'):>7}"
          f"{bw:>12.4f}{bh:>10.4f}{ratio:>9.4f}"
          f"{f'[{iv[0]:.4f}, {iv[1]:.4f}]':>26}")

    # ── §4 B-3：面積 − G ────────────────────────────────────────────────
    P("")
    P("【B-3】「多邊形面積 − G」逐宗並列（⛔ 只量不判成因）")
    P("-" * W)
    _e = G_ROWS.get("_err_0m") or ""
    if _e:
        P(f"  🔴 `run_step_g` 於本案 R2 **必 raise**（正是本批受詞之閘）：{_e}")
        P("  ⇒ `g_rows` 取不到 ⇒ **本節出艙碼 ＝ 未查**（**必然·⛔ 非本探針之缺陷**）。")
        P("  ⚠️ spy 於呼叫 `_orig` **之前**已存好 `CAP` ⇒ A-2／A-3／B-1 之幾何量測**不受影響**。")
    if diffs:
        P(f"  可對上之宗數 ＝ {len(diffs)} ／ {len(biz)}")
        P(f"  帶號合計 ＝ {sum(diffs):+.4f}　絕對值合計 ＝ {sum(abs(x) for x in diffs):.4f}")
    else:
        P("  ⛔ 無可對上之列 ⇒ 本節出艙碼 ＝ **未查**（G 值對應失敗）")
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG937_adjacency_{_sha}.log")
    with open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
