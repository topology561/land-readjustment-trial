r"""**W-G.9-182 `M-G-1`〜`M-G-3`**：`R1` 逐帶重建 ＋ 覆蓋自檢替代式之**驗證** — ⛔ **零生產碼變更**

## 受詞

`W-G.9-182 §一 N-3`：出艙 `R1` 之 `kept_iv` 逐帶（區間／面積／**來源**／span:實佔比）＋ `biz_iv` 逐宗；
閘 `F`（是否存在 `≤ 0.01㎡` 之宗）；`M-G-3` 三式之殘差。

🛑 **`M-G-3` 之三式係<u>受檢假說</u>**（`戒 35`）——其⛔ 不成立**⛔ 不構成停機**。

## 量法

spy `ns["_pool_strips_for_block"]` 攔實收實參，於 wrapper 內**逐字複現**生產碼步驟 1〜5b
（`app.py` 之 `def _pool_strips_for_block`），並**記錄每帶之來源**：
  · 步驟 5 之 `pieces`（由步驟 4 之互斥補區間 `pool_iv` 切出）⇒ 標 `補區間`
  · 步驟 5b 之追加（`K-9-5-7` 幾何餘）⇒ 標 `配餘`
🔒 **實佔長**依 `NOTE-1` 之法：**逐連通片**取 s 區間長再相加（`app.py` 之
`_pool_overlap_len_s` docstring 逐字：「先拆連通片、逐片取 s-區間長再相加」）。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不改任何既有自檢器。⛔ 不立任何新閘。⛔ 不跑 `run_all`／跨態。
⛔ 不寫死本機絕對路徑。
"""
import contextlib
import io
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

OUTDIR = os.path.join(VERIFY, "out")
W = 200
TARGET_SB = 3.5
BLKS = ["R1", "R4"]          # R4 併量（單 §四-8 令「R4 若未重建則具名」）


def _resolve_out(default_name):
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)
    return path


def main():                                                          # noqa: C901
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
    P("【W-G.9-182 M-G-1〜M-G-3】R1（併 R4）逐帶重建與覆蓋自檢替代式之驗證 — ⛔ 零生產碼")
    P("=" * W)
    import shapely
    P("  環境：shapely " + shapely.__version__ + " | GEOS " + str(shapely.geos_version))

    ns, fake_st = harvest()
    _orig = ns["_pool_strips_for_block"]
    _strip_s_range = ns["_strip_s_range"]
    _block_strip = ns["_block_strip"]
    _S_EPS = ns["_S_EPS"]
    CAP = {}

    def occ_len(g, ax):
        """實佔長：依 NOTE-1 逐連通片取 s 長再相加（⛔ 非整體 span）。
        🛑 `ax` ＝ 該街廓**自己**之 (d_hat, corner_pt, allocation_dir)——首版誤用共用鍵
        致印 R1 時吃到 R4 之軸（span/實佔比 ≠ 1 即其徵）⇒ 量測器紅·已修。"""
        parts = list(g.geoms) if hasattr(g, "geoms") else [g]
        tot = 0.0
        for q in parts:
            r = _strip_s_range(q, ax[0], ax[1], ax[2])
            if r is not None:
                tot += (r[1] - r[0])
        return tot

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        if _label in BLKS and _label not in CAP:
            _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
            # 地號／G／a 面積：自 caller frame 之 left/right_results 重建
            meta = []
            try:
                fr = sys._getframe(1)
                lr = fr.f_locals.get("left_results") or []
                rr = fr.f_locals.get("right_results") or []
                _SP_d = fr.f_locals.get("_SP_d")
                for _entry, _res in (list(lr) + list(rr)):
                    _c = _res.get("cut_coords") or []
                    _p = None
                    if len(_c) >= 3 and _SP_d is not None:
                        try:
                            _p = _SP_d(_c)
                            if not _p.is_valid:
                                _p = _p.buffer(0)
                        except Exception:
                            _p = None
                    if _p is not None and not _p.is_empty:
                        tp = (_entry or {}).get("tp") or {}
                        meta.append({
                            "pid": tp.get("暫編地號", "?"),
                            "G": _res.get("G"),
                            "a": tp.get("分攤登記面積_m2", tp.get("面積_m2")),
                            "geom_area": float(_p.area)})
            except Exception:                                         # noqa: BLE001
                pass

            # ── 逐字複現步驟 1〜5b ──────────────────────────────
            s_min, s_max = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
            biz_iv = []
            for p in _biz:
                r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
                if r is not None:
                    biz_iv.append(r)
            biz_iv.sort()
            merged = []
            for a, b in biz_iv:
                if merged and a <= merged[-1][1]:
                    merged[-1] = (merged[-1][0], max(merged[-1][1], b))
                else:
                    merged.append((a, b))
            pool_raw, cur = [], s_min
            for a, b in merged:
                if a > cur:
                    pool_raw.append((cur, min(a, s_max)))
                cur = max(cur, b)
            if cur < s_max:
                pool_raw.append((cur, s_max))
            degen = [(a, b) for a, b in pool_raw if (b - a) <= _S_EPS]
            pool_iv4 = [(a, b) for a, b in pool_raw if (b - a) > _S_EPS]
            # 步驟 5
            bands = []
            for (a, b) in pool_iv4:
                bp = np.asarray(corner_pt, dtype=float) + a * np.asarray(d_hat, dtype=float)
                g, _ = _block_strip(block_poly, d_hat, bp, b - a, allocation_dir=allocation_dir)
                if g is None or g.is_empty or g.buffer(-1e-4).is_empty:
                    continue
                bands.append({"src": "補區間", "iv": (a, b), "g": g})
            # 步驟 5b
            from shapely.ops import unary_union
            _resid_src = _biz + [x["g"] for x in bands]
            if _resid_src:
                _resid = block_poly.difference(unary_union(_resid_src))
                for _rg in (list(_resid.geoms) if hasattr(_resid, "geoms") else [_resid]):
                    if _rg is None or _rg.is_empty or _rg.buffer(-1e-4).is_empty:
                        continue
                    _riv = _strip_s_range(_rg, d_hat, corner_pt, allocation_dir)
                    bands.append({"src": "配餘", "iv": _riv or (s_min, s_max), "g": _rg})
            CAP[_label] = {"ax": (d_hat, corner_pt, allocation_dir),
                           "s": (s_min, s_max), "biz": _biz, "biz_iv": biz_iv,
                           "merged": merged, "degen": degen, "pool_iv4": pool_iv4,
                           "bands": bands, "meta": meta}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, TARGET_SB)
    _d0, _s2, _o2, wins, forced = run_corner_pk(
        ns, fake_st, cb_all, cad, params, temp_p, build_p, TARGET_SB, snapshot=snapshot)
    for blk in BLKS:
        ns["_pool_strips_for_block"] = _spy
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == blk],
                               wins, forced, TARGET_SB)
                except Exception:                                     # noqa: BLE001
                    pass
        finally:
            ns["_pool_strips_for_block"] = _orig
        print("  [%s] 擷取 %s" % (blk, "✅" if blk in CAP else "🔴 未攔到"), file=sys.stderr)

    for blk in BLKS:
        if blk not in CAP:
            P("")
            P("🔴 【%s】**⛔ 未攔到** ⇒ 逐字具名為射程外，⛔ 不以推定代之。" % blk)
            continue
        C = CAP[blk]
        s_min, s_max = C["s"]
        span_all = s_max - s_min
        P("")
        P("=" * W)
        P("■ 街廓 %s　s 域 [%.10f, %.10f]　全寬 %.10f　宗數 %d"
          % (blk, s_min, s_max, span_all, len(C["biz"])))
        P("=" * W)

        # ── M-G-1 逐帶 ──
        P("")
        P("【M-G-1】`kept_iv` 逐帶（區間未捨入／面積／來源／span:實佔比）")
        P("  %-3s %-8s %16s %16s %14s %14s %14s %8s %-14s %6s"
          % ("#", "來源", "s 起", "s 訖", "span", "實佔長", "面積(㎡)", "span/實佔", "geom_type", "頂點"))
        tot_span = tot_occ = tot_area = 0.0
        for i, bd in enumerate(C["bands"], 1):
            a, b = bd["iv"]
            sp = b - a
            oc = occ_len(bd["g"], C["ax"])
            ar = float(bd["g"].area)
            tot_span += sp
            tot_occ += oc
            tot_area += ar
            try:
                nv = len(bd["g"].exterior.coords)
            except Exception:
                nv = -1
            P("  %-3d %-8s %16.10f %16.10f %14.10f %14.10f %14.6f %8.4f %-14s %6d"
              % (i, bd["src"], a, b, sp, oc, ar, (sp / oc if oc > 1e-12 else float("nan")),
                 bd["g"].geom_type, nv))
        P("  ── Σ span = %.10f ／ Σ 實佔長 = %.10f ／ Σ 面積 = %.6f" % (tot_span, tot_occ, tot_area))
        P("  ── 步驟 4 之互斥補區間數 = %d ／ 5b 配餘數 = %d ／ 退化帶 = %d"
          % (sum(1 for x in C["bands"] if x["src"] == "補區間"),
             sum(1 for x in C["bands"] if x["src"] == "配餘"), len(C["degen"])))

        # ── biz_iv 逐宗 ──
        P("")
        P("【M-G-1】`biz_iv` 逐宗（暫編地號／s 起訖／G(㎡)／a 面積(㎡)／幾何面積(㎡)）")
        P("  %-3s %-16s %16s %16s %12s %14s %14s %14s"
          % ("#", "暫編地號", "s 起", "s 訖", "s 寬", "G(㎡)", "a 面積(㎡)", "幾何面積(㎡)"))
        for i, p in enumerate(C["biz"], 1):
            r = _strip_s_range(p, C["ax"][0], C["ax"][1], C["ax"][2])
            m = C["meta"][i - 1] if i - 1 < len(C["meta"]) else {}
            P("  %-3d %-16s %16.10f %16.10f %12.6f %14s %14s %14.6f"
              % (i, m.get("pid", "?"), r[0], r[1], r[1] - r[0],
                 ("%.4f" % m["G"]) if isinstance(m.get("G"), (int, float)) else str(m.get("G")),
                 ("%.4f" % m["a"]) if isinstance(m.get("a"), (int, float)) else str(m.get("a")),
                 float(p.area)))

        # ── M-G-2 閘 F ──
        P("")
        P("【M-G-2 問乙·閘 F】是否存在 `a 面積(㎡)` 或幾何面積 ≤ 0.01 之宗？")
        small_a = [(m.get("pid"), m.get("a")) for m in C["meta"]
                   if isinstance(m.get("a"), (int, float)) and float(m["a"]) <= 0.01]
        small_g = [(C["meta"][i]["pid"] if i < len(C["meta"]) else "?", float(p.area))
                   for i, p in enumerate(C["biz"]) if float(p.area) <= 0.01]
        P("  a 面積 ≤ 0.01 之宗 = %d %s" % (len(small_a), small_a))
        P("  幾何面積 ≤ 0.01 之宗 = %d %s" % (len(small_g), small_g))
        P("  ⇒ 閘 F：%s" % ("✅ 有（支持 (甲)）" if (small_a or small_g) else "🔴 **無**（⛔ 不支持 (甲)）"))

        # ── M-G-3 三式 ──
        P("")
        P("【M-G-3】覆蓋自檢替代式（🛑 **受檢假說**·⛔ 非停機款·不成立⛔ 不停機）")
        w4 = sum(b - a for a, b in C["pool_iv4"])
        wbiz_m = sum(b - a for a, b in C["merged"])
        wdeg = sum(b - a for a, b in C["degen"])
        r_i = span_all - (w4 + wbiz_m + wdeg)
        P("  式(i) 步驟4補區間 ＋ merged宗帶 ＋ 退化帶 ＝ s 域全寬")
        P("      %.10f + %.10f + %.10e = %.10f   vs %.10f   殘差 %.10e  %s"
          % (w4, wbiz_m, wdeg, w4 + wbiz_m + wdeg, span_all, r_i,
             "✅ 成立" if abs(r_i) <= 0.001 else "🔴 ⛔ 不成立"))

        def measure_union(ivs):
            xs = sorted([(a, b) for a, b in ivs if b > a])
            tot, cur_a, cur_b = 0.0, None, None
            for a, b in xs:
                if cur_a is None:
                    cur_a, cur_b = a, b
                elif a <= cur_b:
                    cur_b = max(cur_b, b)
                else:
                    tot += cur_b - cur_a
                    cur_a, cur_b = a, b
            if cur_a is not None:
                tot += cur_b - cur_a
            return tot

        u = measure_union([bd["iv"] for bd in C["bands"]] + C["biz_iv"])
        r_ii = span_all - u
        P("  式(ii) measure(∪kept_iv ∪ ∪biz_iv) ＝ s 域全寬")
        P("      %.10f   vs %.10f   殘差 %.10e  %s"
          % (u, span_all, r_ii, "✅ 成立" if abs(r_ii) <= 0.001 else "🔴 ⛔ 不成立"))

        occ_bands = sum(occ_len(bd["g"], C["ax"]) for bd in C["bands"])
        occ_biz = sum(occ_len(p, C["ax"]) for p in C["biz"])
        r_iii = span_all - (occ_bands + occ_biz)
        P("  式(iii) Σ(逐帶實佔長) ＋ Σ(逐宗實佔長) ＝ s 域全寬")
        P("      %.10f + %.10f = %.10f   vs %.10f   殘差 %.10e  %s"
          % (occ_bands, occ_biz, occ_bands + occ_biz, span_all, r_iii,
             "✅ 成立" if abs(r_iii) <= 0.001 else "🔴 ⛔ 不成立"))

        # 附：舊 X-3 之形（池帶寬和 ≤ s 域全寬）
        P("  【附】舊 `X-3` 之形：Σ(kept_iv span) = %.10f  vs s 域全寬 %.10f  ⇒ %s"
          % (tot_span, span_all, "✅ ≤" if tot_span <= span_all else "🔴 **>**（超出 %.4f）" % (tot_span - span_all)))

    # ══ 加驗 (甲)：自 build_p 直接查 ghost（⛔ 不需跨態）══
    P("")
    P("=" * W)
    P("【M-G-2 問乙·加驗】自 `build_p` 直查 `R1`／`R4` 之全部宗（含<u>被 VR-074 排除者</u>）")
    P("=" * W)
    P("  🔒 由：現基座已落地 `VR-074`（ghost ⛔ 不入投影序母體）⇒ 消失之第 6 宗於 `biz_iv` 已不可見；")
    P("     惟其於 `build_p` **仍存在** ⇒ 得直接查其面積，**⛔ 不需跨態重跑**。")
    for blk in BLKS:
        rows = [tp for tp in build_p if tp.get("所屬街廓") == blk]
        P("")
        P("  ■ %s：`build_p` 之宗數 = %d" % (blk, len(rows)))
        P("    %-3s %-16s %-12s %-14s %14s %14s %14s"
          % ("#", "暫編地號", "原地號", "重劃前區段", "幾何面積_m2", "分攤登記面積", "登記面積_m2"))
        for i, tp in enumerate(rows, 1):
            P("    %-3d %-16s %-12s %-14s %14s %14s %14s"
              % (i, str(tp.get("暫編地號")), str(tp.get("原地號")), repr(tp.get("重劃前區段")),
                 tp.get("幾何面積_m2"), tp.get("分攤登記面積_m2"), tp.get("登記面積_m2")))
        gh = [tp for tp in rows if str(tp.get("原地號")) == "_GHOST"]
        P("    ⇒ `原地號 == '_GHOST'` 之宗 = %d" % len(gh))
        for tp in gh:
            ga = tp.get("幾何面積_m2")
            P("       %s  幾何面積_m2 = %s  ⇒ %s"
              % (tp.get("暫編地號"), ga,
                 ("✅ ≤ 0.01 ⇒ **支持 (甲)**" if isinstance(ga, (int, float)) and float(ga) <= 0.01
                  else "🔴 > 0.01 ⇒ **⛔ 不支持 (甲)**")))

    P("")
    P("🛑 本檔只重建與檢驗·⛔ 未修·⛔ 未動生產碼一字·⛔ 未立任何新閘。")
    P("=" * W)
    out = _resolve_out("probe_WG9182_R1_bands_9fe070a2.log")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("WROTE " + out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
