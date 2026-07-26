# -*- coding: utf-8 -*-
"""W-G.5 裁定 N 二輪 · **P-8 實測**（只量不改）——R6 左組前三宗之 gid ／同歸戶可併量／承接門檻。

## 問題（KL 交辦 P-8）

裁定 N-2′ 下未臨正街三角地由「**當時緊鄰 p1 之該宗**」承接；吃不下者退出、下一順位遞補到
p1 位置。**三角地最終停在哪一宗？**（claude.ai 推測落 `628-4(1)`·**須實證**）

## 判準（N-10 承接門檻·泛用式·禁寫死）

    承接門檻 = 未臨正街真幾何面積 + (畸零地最小寬度 × 該端深度)

**全部查表／實測取得**：未臨正街面積＝`block∩{s<0}`（治理碼 `_block_strip`）；
最小寬＝`get_min_lot_size(category, 正面路寬)['min_width']`；深度＝下列**兩式併陳**
（**不自行擇一**·留待 plan/reviewer 裁）：
  (甲) `snapshot.blocks[blk]['街廓分配深度_m']`（現行 MinA 所用）
  (乙) 幾何實測：p1 端沿 **FRONT 法向量**（N-12 明定·**非** `alloc_normal_axis`）至 BASELINE 之垂距

## gid 口徑（**與治理碼同源·禁自造**）

`gid = t8_ownership_map[原地號]`（`grep -n "_gid_of = {p: _omap_m5.get" verify/run_verification.py`）。
「同歸戶可併量」＝**同 gid 之其他宗**（跨街廓）之 `a 面積`／`G`。

## 重跑
    WV_RULING_N_P8=1 python verify/probes/probe_ruling_N_p8.py

⚠️ **零注入·零引擎改動**（獨立 script）。輸出 `verify/out/probe_ruling_N_p8.log`。
⚠️ 基線係 P-H 凍結前之波前產物 ⇒ **絕對數值待解凍後複核**；**結構性結論**（停在哪一宗）穩健。
"""
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

OUT_LOG = os.path.join(VERIFY, "out", "probe_ruling_N_p8.log")
TARGET_BLK = "R6"          # KL 交辦指名之塊（**只此探針之觀察對象**·非碼內常數）


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_N_p8：{msg}（no-silent-fallback）")


def _front_normal_axis(poly, p1, d_hat):
    """FRONT 法向量（N-12 明定之量測軸·**非** `alloc_normal_axis`），取號指向街廓內。"""
    n = np.array([-d_hat[1], d_hat[0]], dtype=float)
    c = np.array(poly.centroid.coords[0], dtype=float)
    if float(np.dot(c - p1, n)) < 0:
        n = -n
    return n


def _chord_at(poly, p1, d_hat, n, s):
    """自 FRONT 上 s 處沿 `n` 之 block 內**弦長**（＝該處 FRONT→BASELINE 之垂距）。"""
    from shapely.geometry import LineString
    base = p1 + float(s) * d_hat
    ln = LineString([base - 1e4 * n, base + 1e4 * n]).intersection(poly)
    if ln.is_empty:
        return 0.0
    return float(ln.length)


def _front_normal_depth_min(poly, p1, d_hat, n, s_lo, s_hi, nstep=400):
    """N-12：**垂直距離最小值**，量測範圍 `s∈[s_lo, s_hi]`（沿 FRONT）。
    ⚠️ 舊版取『全街廓頂點於 n 軸之**最大**投影』＝**與 N-12 定義相反**（reviewer BLOCKED-3）·已廢。
    範圍端點落街廓外 ⇒ 弦長 0，故以 >1e-6 濾（0 表該處無街廓·非深度為 0）。"""
    vals = []
    for i in range(nstep + 1):
        s = s_lo + (s_hi - s_lo) * i / nstep
        c = _chord_at(poly, p1, d_hat, n, s)
        if c > 1e-6:
            vals.append(c)
    return (min(vals) if vals else 0.0), (max(vals) if vals else 0.0)


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if os.environ.get("WV_RULING_N_P8") != "1":
        print("🔴 本探針須 WV_RULING_N_P8=1 明示啟用。")
        return 2
    os.makedirs(os.path.dirname(OUT_LOG), exist_ok=True)
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    L = []

    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        ns, fake_st = harvest()
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(
            ns, fake_st, v6, list(cb_by.values()), snapshot)
        _diag, _sel, _off, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp, build,
            setback, snapshot=snapshot)
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                        params, build, winners, forced, setback)
        g_rows = sg["g_rows"]

        # ── gid 對照（與 run_verification 同源）──
        omap = fake_st.session_state.get("t8_ownership_map", {}) or {}
        if not omap:
            _fail("t8_ownership_map 空（build_ownership 未鋪底）")
        bp_by = {b.get("暫編地號"): b for b in build}
        gid_of = {p: omap.get((bp_by.get(p) or {}).get("原地號", ""), "") for p in bp_by}

        # ── R6 幾何：未臨正街面積／最小寬／兩式深度 ──
        blk = TARGET_BLK
        fl = (cad.get("front_lines") or {}).get(blk) or _fail(f"{blk} 缺 FRONT_LINE")
        p1 = np.array(fl["p1"], float); p2 = np.array(fl["p2"], float)
        d_hat = (p2 - p1) / float(np.linalg.norm(p2 - p1))
        poly = Polygon(cb_by[blk]["vertices"])
        if not poly.is_valid:
            poly = poly.buffer(0)
        alloc_axis = ns["alloc_normal_axis"](
            (cad.get("alloc_dir_by_block") or {}).get(blk) or _fail(f"{blk} 缺 ALLOC"))
        dom = ns["_strip_s_range"](poly, d_hat, p1, alloc_axis) or _fail("s 域不可定義")
        s_min = float(dom[0])
        unfront = (float(ns["_block_strip"](poly, d_hat, p1 + s_min * d_hat, -s_min,
                                            allocation_dir=alloc_axis)[1] or 0.0)
                   if s_min < -1e-6 else 0.0)
        road_w = float(snapshot["blocks"][blk]["正面"]["路寬_m"])
        mls = ns["get_min_lot_size"](cb_by[blk]["category"], road_w)
        mw = float(mls.get("min_width", 0) or 0)
        md = float(mls.get("min_depth", 0) or 0)
        depth_snap = float(snapshot["blocks"][blk]["街廓分配深度_m"])
        nf = _front_normal_axis(poly, p1, d_hat)
        s_max_fl = float(np.linalg.norm(p2 - p1))
        # N-12 之「量測範圍」尚未定讞（reviewer 交回 KL）⇒ **三種範圍併陳·不自行擇一**
        d_all, d_all_max = _front_normal_depth_min(poly, p1, d_hat, nf, 0.0, s_max_fl)
        d_mw, _ = _front_normal_depth_min(poly, p1, d_hat, nf, 0.0, mw)
        # 🔴 p1 端退化偵測：弦長於 p1 恰為 0（街廓真實起點在 s_min<0、p1 之後方）
        #    ⇒「該端深度」在 N-12 字面下**不可定義**；d_mw 之數值純為取樣解析度產物。
        _c0 = _chord_at(poly, p1, d_hat, nf, 0.0)
        _prof = [(s, _chord_at(poly, p1, d_hat, nf, s))
                 for s in (0.0, 0.0088, 0.05, 0.2, 0.5, 1.0, 2.0, mw)]
        _p1_degenerate = (_c0 <= 1e-6)
        depth_variants = [
            ("甲 街廓分配深度_m（snapshot）", depth_snap),
            ("乙1 FRONT法向 min·全 FRONT", d_all),
            ("乙2 FRONT法向 min·p1端 0~min_width 段 ⚠️退化", d_mw),
            ("丙 FRONT法向 max（⚠️ 與 N-12 相反·僅供對照）", d_all_max),
        ]
        thr_snap = unfront + mw * depth_snap
        thr_geom = unfront + mw * d_all       # 主判準改採 N-12 字面（全 FRONT 之 min）

        L.append("=" * 112)
        L.append(f"【P-8·{tag}】{blk} 承接門檻（N-10 泛用式·全查表／實測）")
        L.append("-" * 112)
        L.append(f"  未臨正街真幾何面積 block∩{{s<0}} = {unfront:.4f}㎡（s_min={s_min:.4f}）")
        L.append(f"  畸零地最小寬 min_width = {mw:.2f}m｜最小深 min_depth = {md:.2f}m"
                 f"（分區 {cb_by[blk]['category']}·正面路寬 {road_w:.1f}m·查表 {mls.get('table_key','')}）")
        L.append("  ⚠️ N-12「量測範圍」未定讞（reviewer 交回 KL）⇒ **四讀併陳·不自行擇一**：")
        for _nm, _d in depth_variants:
            L.append(f"      {_nm:44} 深度 {_d:8.4f}m ⇒ 門檻 "
                     f"{unfront + mw * _d:9.3f}㎡")
        L.append(f"  對照：KL 手繪 E_V6 之 R_end = 252.28㎡（=85.71+166.57）"
                 f"｜claude.ai 實算 251.738㎡")
        L.append("  🔴 **禁以此對照反推軸別**（reviewer BLOCKED-3）：166.57 即 `_end_band` "
                 "（**ALLOC 軸**）之輸出 ⇒ 該『源』非獨立；且 FRONT/ALLOC 夾角僅 4.6° "
                 "（cos=0.9968）⇒ 兩軸差 ≈0.15m < 各源散布，**原理上無鑑別力**。")
        if _p1_degenerate:
            L.append("  🔴🔴 **端部深度為超敏感階躍（上呈 U3/U9）**：沿 FRONT 法向之弦長剖面 —— "
                     + "；".join(f"s={s:.4f}→{c:.4f}" for s, c in _prof))
            L.append("        本塊 chord 於 p1 為 0，並在極短區間內竄至滿值"
                     "（R6：[0, 0.24] 由 0→47.7·斜率 ≈199）。")
            L.append("        ⚠️ **禁推論『恆退化為 0』**（該通則不成立·plan v3 §3.2 已撤回）："
                     "本塊 chord(p1)=0 之因為左封邊向 +d̂ 傾、與 n_front 差 0.287° 落在內角錐外；"
                     "若封邊反向傾則 chord(p1) 立為滿值，**而楔形仍存在**"
                     "（楔形充要條件＝封邊傾角 < ALLOC 傾角，與傾向無關）⇒ 本塊係碰巧。")
            L.append("        **可成立之結論**：端部區間內 min 為超敏感階躍 ⇒ "
                     "**任何無排除帶之 min 皆隨取樣→0**（乙1／乙2 同病·實測 step 0.215/0.01/0.001 "
                     "得 40.2776／1.9943／0.1994）；**加排除帶 s≥0.5 則跨三個數量級穩定於 40.2776**。")
            L.append("        ⇒ ① N-12 之 min **必須附排除帶定義**方可實作（寬度須有法源／工程依據·"
                     "禁由 CC 挑數）；② 排除退化帶後真正的 min 落在 **p2 端**，"
                     "用它當『p1 端深度』語意上是拿街廓另一端幾何定門檻 ⇒ "
                     "**N-10 之『該端深度』真義須 KL 裁**。")

        # ── R6 左組逐宗：gid／a／G／可併量／是否過門檻 ──
        left = sorted([r for r in g_rows
                       if r.get("所屬街廓") == blk and r.get("推進側別") == "left"],
                      key=lambda x: float(x.get("累積S(m)", 0) or 0))
        if not left:
            _fail(f"{blk} 左組為空")
        # 同歸戶可併量：同 gid 之**其他**宗（跨街廓·全域）
        by_gid = {}
        for r in g_rows:
            if r.get("推進側別") not in ("left", "right"):
                continue
            g = gid_of.get(r.get("暫編地號"), "")
            by_gid.setdefault(g, []).append(r)

        L.append("")
        L.append(f"  {blk} 左組逐宗（推進序）：")
        L.append(f"    {'宗':14}{'gid':>10}{'a面積':>9}{'G':>9}{'S':>8}{'寬':>7}"
                 f"{'同戶其他宗':>11}{'可併ΣG':>10}{'G+可併':>10}  過(甲)/過(乙)")
        for r in left:
            pid = r.get("暫編地號")
            g = gid_of.get(pid, "")
            sibs = [x for x in by_gid.get(g, []) if x.get("暫編地號") != pid] if g else []
            sib_g = sum(float(x.get("G(㎡)", 0) or 0) for x in sibs)
            Gv = float(r.get("G(㎡)", 0) or 0)
            tot = Gv + sib_g
            L.append(f"    {str(pid):14}{str(g):>10}{float(r.get('a 面積(㎡)',0) or 0):9.2f}"
                     f"{Gv:9.2f}{float(r.get('S(m)',0) or 0):8.2f}"
                     f"{float(r.get('宗地寬度(m)',0) or 0):7.2f}{len(sibs):11d}{sib_g:10.2f}"
                     f"{tot:10.2f}"
                     f"   {'✅' if tot >= thr_snap else '❌'}   /   "
                     f"{'✅' if tot >= thr_geom else '❌'}")
            if sibs:
                for x in sibs:
                    L.append(f"      └ 同戶 {x.get('暫編地號')}@{x.get('所屬街廓')}"
                             f" a={float(x.get('a 面積(㎡)',0) or 0):.2f}"
                             f" G={float(x.get('G(㎡)',0) or 0):.2f}")

        # ── 結論：首個過門檻者·**兩讀併印**（reviewer NOTE-16：舊版只算讀法(二)、結論相反）──
        #   讀法(一) solo G      ＝原位次階段之自然讀法（不計同歸戶可併量）
        #   讀法(二) G＋同歸戶可併ΣG ＝**上界**（未套四級合併要件·跨街廓者未必可實現）
        L.append("")
        L.append("  ⇒ 首個承接者（**兩讀併陳·KL 未裁·禁擇一**）：")
        for _nm, _d in depth_variants:
            _thr = unfront + mw * _d
            _res_line = []
            for _rk, _use_sib in (("一 solo G", False), ("二 含可併", True)):
                hit = None
                for r in left:
                    pid = r.get("暫編地號")
                    g = gid_of.get(pid, "")
                    sibs = ([x for x in by_gid.get(g, []) if x.get("暫編地號") != pid]
                            if (g and _use_sib) else [])
                    tot = float(r.get("G(㎡)", 0) or 0) + sum(
                        float(x.get("G(㎡)", 0) or 0) for x in sibs)
                    if tot >= _thr:
                        hit = (pid, tot)
                        break
                _res_line.append(f"讀法{_rk}→{hit[0] if hit else '（無人可承接）'}"
                                 f"{f'({hit[1]:.2f})' if hit else ''}")
            L.append(f"      門檻 {_thr:9.3f}㎡（{_nm}）：　" + "　｜　".join(_res_line))
    L.append("=" * 112)
    out = "\n".join(L)
    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write(out + "\n")
    print(out)
    print(f"\n📄 {OUT_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
