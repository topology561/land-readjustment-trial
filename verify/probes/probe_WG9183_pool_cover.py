r"""**W-G.9-183 `M-H-1`**：式(ii) 之**擴大驗證**（`R2`／`R3`／`R5`／`R6` ＋ 併量 `R1`／`R4`）— ⛔ **零生產碼變更**

## 受詞

`W-G.9-183 §一 N-3 M-H-1`：對 `R2`／`R3`／`R5`／`R6` 以 `-182` 探針之同法
（spy `ns["_pool_strips_for_block"]`·逐街廓 `run_step_g`）重建，逐街廓出艙
式(ii) 之殘差 ＋ `kept_iv` 逐帶（區間／面積／來源／span:實佔比）＋ `biz_iv` 逐宗。
`R1`／`R4` 併量以**復現** `-182R` 之值（母體 ＝ 六街廓）。

🔒 **式(ii)** ＝ `measure(∪kept_iv ∪ ∪biz_iv)` ＝ `s_max − s_min`。
🛑 **式(ii) 係<u>受檢假說</u>**（`戒 35`·單 `X-8`）——其⛔ 不成立**⛔ 不構成停機**。

## 🛑 停機款 `X-3`（單 `§二`·逐字）

> `M-H-1` 之任一帶若為單一 `Polygon` 而其 `span/實佔比 ≠ 1`（容差 `1e-9`）
> ⇒ **先判量測器紅並停機**（`W-G.9-182R §五-2` 所立之判準）。

⇒ 本檔逐帶印 `span/實佔比` 與其絕對差，並於末節出艙 `X-3` 之總判。

## 量法

與 `probe_WG9182_R1_bands.py` **同法**（逐字複現生產碼步驟 1〜5b·來源標 `補區間`／`配餘`）；
**實佔長**依 `NOTE-1`（`app.py` 之 `_pool_overlap_len_s` docstring 逐字：
「先拆連通片、逐片取 s-區間長再相加」）。
🔒 **軸須用該街廓自己之** `(d_hat, corner_pt, allocation_dir)`——共用鍵覆寫係
`-182R §六 8` 已具名之量測器紅（`span/實佔比 ≠ 1` 即其徵）。

## 【倉】對拍

`verify/out/KL_UI_3.5m_2e08a41_stdout.log` 之 `[T2-DIAG]`（**KL UI 態**·⛔ 非本態）。
⚠️ 該列之數為 **4dp 顯示值** ⇒ 對拍框 ＝ `4dp`，⛔ 非「逐位」。
🔴 `R5` 於該 log **⛔ 無 `[T2-DIAG]`**（其於該 log `:2985` 之 `K-9-4` BASELINE 臨接閘
`RuntimeError` 終止）⇒ `R5` 之【倉】錨**結構上不存在**，逐字具名、⛔ 不以推定代之。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不改任何既有自檢器。⛔ 不立任何新閘。⛔ 不跑 `run_all`／跨態。
⛔ 不寫死本機絕對路徑。
"""
import contextlib
import io
import os
import re
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
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
X3_TOL = 1e-9
T2LOG = os.path.join(OUTDIR, "KL_UI_3.5m_2e08a41_stdout.log")


def _resolve_out(default_name):
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path)
    return path


def _parse_t2diag():
    """自【倉】log 解 `[T2-DIAG]`。⛔ 缺檔即響亮拋出（⛔ 不以空 dict 靜默代之）。"""
    if not os.path.exists(T2LOG):
        raise RuntimeError("🔴 【倉】對拍源不存在：" + T2LOG)
    txt = open(T2LOG, encoding="utf-8", errors="replace").read()
    out = {}
    for ln in txt.splitlines():
        if "[T2-DIAG]" not in ln:
            continue
        blk = re.search(r"街廓 (\S+?)｜", ln).group(1)
        out[blk] = {
            "w": [float(x) for x in re.search(r"池帶 s 寬 \[([^\]]*)\]", ln).group(1).split()],
            "a": [float(x) for x in re.search(r"池帶面積 \[([^\]]*)\]", ln).group(1).split()],
            "pool": float(re.search(r"Σ池 ([0-9.\-]+)", ln).group(1)),
            "s": [float(x) for x in re.search(r"s 域 \[([-0-9.e]+),([-0-9.e]+)\]", ln).groups()],
        }
    return out


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
    P("【W-G.9-183 M-H-1】式(ii) 之擴大驗證（六街廓）— ⛔ 零生產碼")
    P("=" * W)
    import shapely
    P("  環境：shapely " + shapely.__version__ + " | GEOS " + str(shapely.geos_version))
    T2 = _parse_t2diag()
    P("  【倉】對拍源：verify/out/KL_UI_3.5m_2e08a41_stdout.log ⇒ [T2-DIAG] 街廓 = %s"
      % sorted(T2.keys()))
    P("  🔴 六街廓中⛔ 無 [T2-DIAG] 者 = %s（其【倉】錨結構上不存在）"
      % [b for b in BLKS if b not in T2])

    ns, fake_st = harvest()
    _orig = ns["_pool_strips_for_block"]
    _strip_s_range = ns["_strip_s_range"]
    _block_strip = ns["_block_strip"]
    _S_EPS = ns["_S_EPS"]
    CAP = {}

    def occ_len(g, ax):
        """實佔長：依 NOTE-1 逐連通片取 s 長再相加（⛔ 非整體 span）。
        🛑 `ax` ＝ 該街廓**自己**之軸（`-182R §六 8` 之共用鍵覆寫戒）。"""
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

            # -- 逐字複現步驟 1~5b --------------------------------
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
            bands = []
            for (a, b) in pool_iv4:
                bp = np.asarray(corner_pt, dtype=float) + a * np.asarray(d_hat, dtype=float)
                g, _ = _block_strip(block_poly, d_hat, bp, b - a, allocation_dir=allocation_dir)
                if g is None or g.is_empty or g.buffer(-1e-4).is_empty:
                    continue
                bands.append({"src": "補區間", "iv": (a, b), "g": g})
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
                           "bands": bands, "meta": meta,
                           "block_area": float(block_poly.area)}
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

    ERRS = {}
    for blk in BLKS:
        ns["_pool_strips_for_block"] = _spy
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == blk],
                               wins, forced, TARGET_SB)
                except Exception as e:                                # noqa: BLE001
                    ERRS[blk] = "%s: %s" % (type(e).__name__, str(e)[:220])
        finally:
            ns["_pool_strips_for_block"] = _orig
        print("  [%s] capture %s%s" % (blk, "OK" if blk in CAP else "MISS",
                                       ("  err=" + ERRS[blk][:80]) if blk in ERRS else ""),
              file=sys.stderr)

    P("")
    P("  逐街廓 run_step_g 之終止情形（⛔ 非停機款·照實載）：")
    for blk in BLKS:
        P("    %-3s 擷取 %-6s %s" % (blk, "✅" if blk in CAP else "🔴 未攔到",
                                     ("｜例外 " + ERRS[blk]) if blk in ERRS else "｜⛔ 無例外"))

    X3_BAD = []          # X-3：單一 Polygon 而 span/實佔比 != 1
    SUM = {}

    for blk in BLKS:
        if blk not in CAP:
            P("")
            P("=" * W)
            P("🔴 ■ 街廓 %s：**⛔ 未攔到** ⇒ 逐字具名為射程外，⛔ 不以推定代之。" % blk)
            P("=" * W)
            continue
        C = CAP[blk]
        s_min, s_max = C["s"]
        span_all = s_max - s_min
        P("")
        P("=" * W)
        P("■ 街廓 %s　s 域 [%.10f, %.10f]　全寬 %.10f　宗數 %d　街廓面積 %.4f㎡"
          % (blk, s_min, s_max, span_all, len(C["biz"]), C["block_area"]))
        P("=" * W)

        P("")
        P("【M-H-1】`kept_iv` 逐帶（區間未捨入／面積／來源／span:實佔比）")
        P("  %-3s %-8s %16s %16s %14s %14s %14s %14s %12s %-14s %6s"
          % ("#", "來源", "s 起", "s 訖", "span", "實佔長", "面積(㎡)",
             "span/實佔", "|span-實佔|", "geom_type", "頂點"))
        tot_span = tot_occ = tot_area = 0.0
        for i, bd in enumerate(C["bands"], 1):
            a, b = bd["iv"]
            sp = b - a
            oc = occ_len(bd["g"], C["ax"])
            ar = float(bd["g"].area)
            tot_span += sp
            tot_occ += oc
            tot_area += ar
            ratio = (sp / oc) if oc > 1e-12 else float("nan")
            single = (bd["g"].geom_type == "Polygon")
            if single and (not (abs(ratio - 1.0) <= X3_TOL)):
                X3_BAD.append((blk, i, bd["src"], sp, oc, ratio))
            try:
                nv = len(bd["g"].exterior.coords)
            except Exception:
                nv = -1
            P("  %-3d %-8s %16.10f %16.10f %14.10f %14.10f %14.6f %14.10f %12.3e %-14s %6d"
              % (i, bd["src"], a, b, sp, oc, ar, ratio, abs(sp - oc), bd["g"].geom_type, nv))
        P("  ── Σ span = %.10f ／ Σ 實佔長 = %.10f ／ Σ 面積 = %.6f"
          % (tot_span, tot_occ, tot_area))
        P("  ── 步驟 4 之互斥補區間數 = %d ／ 5b 配餘數 = %d ／ 退化帶 = %d"
          % (sum(1 for x in C["bands"] if x["src"] == "補區間"),
             sum(1 for x in C["bands"] if x["src"] == "配餘"), len(C["degen"])))

        P("")
        P("【M-H-1】`biz_iv` 逐宗（暫編地號／s 起訖／G(㎡)／a 面積(㎡)／幾何面積(㎡)）")
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

        P("")
        P("【M-H-1】覆蓋自檢替代式（🛑 **受檢假說**·單 `X-8`：⛔ 不成立亦⛔ 不停機）")
        w4 = sum(b - a for a, b in C["pool_iv4"])
        wbiz_m = sum(b - a for a, b in C["merged"])
        wdeg = sum(b - a for a, b in C["degen"])
        r_i = span_all - (w4 + wbiz_m + wdeg)
        P("  式(i)   %.10f + %.10f + %.10e = %.10f  vs %.10f  殘差 %.10e  %s"
          % (w4, wbiz_m, wdeg, w4 + wbiz_m + wdeg, span_all, r_i,
             "✅ 成立" if abs(r_i) <= 0.001 else "🔴 ⛔ 不成立"))
        u = measure_union([bd["iv"] for bd in C["bands"]] + C["biz_iv"])
        r_ii = span_all - u
        P("  式(ii)  measure(∪kept_iv ∪ ∪biz_iv) = %.10f  vs %.10f  殘差 %.10e  %s"
          % (u, span_all, r_ii, "✅ 成立" if abs(r_ii) <= 0.001 else "🔴 ⛔ 不成立"))
        occ_bands = sum(occ_len(bd["g"], C["ax"]) for bd in C["bands"])
        occ_biz = sum(occ_len(p, C["ax"]) for p in C["biz"])
        r_iii = span_all - (occ_bands + occ_biz)
        P("  式(iii) %.10f + %.10f = %.10f  vs %.10f  殘差 %.10e  %s"
          % (occ_bands, occ_biz, occ_bands + occ_biz, span_all, r_iii,
             "✅ 成立" if abs(r_iii) <= 0.001 else "🔴 ⛔ 不成立"))
        P("  【附】舊 `X-3` 之形：Σ(kept_iv span) = %.10f  vs s 域全寬 %.10f  ⇒ %s"
          % (tot_span, span_all,
             "✅ ≤" if tot_span <= span_all else "🔴 **>**（超出 %.4f）" % (tot_span - span_all)))

        # -- 【倉】對拍（4dp 框）--
        P("")
        P("【M-H-1】與【倉】`[T2-DIAG]` 之對拍（框 ＝ **4dp 顯示值**·⛔ 非逐位）")
        if blk not in T2:
            P("  🔴 **⛔ 無【倉】錨**——該 log 內無 %s 之 [T2-DIAG]（其於 K-9-4 閘終止）"
              "⇒ 本街廓⛔ 不對拍，逐字具名。" % blk)
        else:
            t = T2[blk]
            mine_w = ["%.4f" % (b - a) for a, b in [bd["iv"] for bd in C["bands"]]]
            mine_a = ["%.4f" % float(bd["g"].area) for bd in C["bands"]]
            mine_p = sum(float(bd["g"].area) for bd in C["bands"])
            ref_w = ["%.4f" % x for x in t["w"]]
            ref_a = ["%.4f" % x for x in t["a"]]
            P("  帶數    本探針 %d ／【倉】%d   %s"
              % (len(C["bands"]), len(t["w"]),
                 "✅" if len(C["bands"]) == len(t["w"]) else "🔴 不符"))
            P("  池帶s寬 本探針 %s" % mine_w)
            P("          【倉】 %s   %s" % (ref_w, "✅ 相符" if mine_w == ref_w else "🔴 **不符**"))
            P("  池帶面積 本探針 %s" % mine_a)
            P("          【倉】 %s   %s" % (ref_a, "✅ 相符" if mine_a == ref_a else "🔴 **不符**"))
            P("  Σ池     本探針 %.4f ／【倉】%.4f   Δ %+.4f   %s"
              % (mine_p, t["pool"], mine_p - t["pool"],
                 "✅ 相符" if abs(mine_p - t["pool"]) < 5e-5 else "🔴 **不符**"))
            P("  s 域    本探針 [%.4f,%.4f] ／【倉】[%.4f,%.4f]   %s"
              % (s_min, s_max, t["s"][0], t["s"][1],
                 "✅ 相符" if ("%.4f" % s_min == "%.4f" % t["s"][0]
                              and "%.4f" % s_max == "%.4f" % t["s"][1]) else "🔴 **不符**"))

        SUM[blk] = {"span_all": span_all, "r_ii": r_ii, "r_i": r_i, "r_iii": r_iii,
                    "tot_span": tot_span, "nb": len(C["bands"]), "nbiz": len(C["biz"])}

    # == 總判 ==
    P("")
    P("=" * W)
    P("【M-H-1 總表】六街廓")
    P("=" * W)
    P("  %-4s %8s %8s %16s %18s %18s %18s %14s"
      % ("街廓", "帶數", "宗數", "s 域全寬", "式(i) 殘差", "式(ii) 殘差", "式(iii) 殘差", "Σspan−全寬"))
    for blk in BLKS:
        if blk not in SUM:
            P("  %-4s %8s %8s %16s %18s %18s %18s %14s"
              % (blk, "—", "—", "⛔ 未攔到", "—", "—", "—", "—"))
            continue
        s = SUM[blk]
        P("  %-4s %8d %8d %16.10f %18.10e %18.10e %18.10e %+14.4f"
          % (blk, s["nb"], s["nbiz"], s["span_all"], s["r_i"], s["r_ii"], s["r_iii"],
             s["tot_span"] - s["span_all"]))
    got = [b for b in BLKS if b in SUM]
    ok_ii = [b for b in got if abs(SUM[b]["r_ii"]) <= 0.001]
    P("")
    P("  ⇒ 式(ii) 之驗證母體 ＝ %d／%d 街廓（%s）；殘差 ≤ 1e-3 者 ＝ %d（%s）"
      % (len(got), len(BLKS), got, len(ok_ii), ok_ii))
    P("  ⇒ 式(iii) 不成立者 ＝ %s"
      % [b for b in got if abs(SUM[b]["r_iii"]) > 0.001])
    P("  ⇒ 舊 `X-3`（Σspan ≤ 全寬）之反例 ＝ %s"
      % [b for b in got if SUM[b]["tot_span"] > SUM[b]["span_all"]])

    P("")
    P("=" * W)
    P("【停機款 `X-3` 之判】單一 `Polygon` 而 span/實佔比 ≠ 1（容差 %.0e）" % X3_TOL)
    P("=" * W)
    if X3_BAD:
        P("  🔴 **命中 %d 帶 ⇒ 量測器紅 ⇒ 停機**" % len(X3_BAD))
        for r in X3_BAD:
            P("    %s #%d %s  span=%.10f 實佔=%.10f 比=%.12f" % r)
    else:
        n_single = sum(1 for blk in got for bd in CAP[blk]["bands"]
                       if bd["g"].geom_type == "Polygon")
        n_multi = sum(1 for blk in got for bd in CAP[blk]["bands"]
                      if bd["g"].geom_type != "Polygon")
        P("  ✅ **⛔ 無命中** ⇒ ⛔ 不停機。單一 `Polygon` 之帶 = %d（皆 |比−1| ≤ %.0e）；"
          "非單一片之帶 = %d（⛔ 不受本款拘束）" % (n_single, X3_TOL, n_multi))

    P("")
    P("🛑 本檔只重建與檢驗·⛔ 未修·⛔ 未動生產碼一字·⛔ 未立任何新閘。")
    P("=" * W)
    out = _resolve_out("probe_WG9183_pool_cover_9f4b8301.log")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("WROTE " + out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
