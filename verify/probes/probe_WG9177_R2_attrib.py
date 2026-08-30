r"""**W-G.9-177 `M-B-1`／`M-B-3`／`M-B-4`**：`R2` `0.1171` 之歸屬 — ⛔ **零生產碼變更**

## 受詞

`W-G.9-177 §一 N-3`：`0.1171` 落於池帶2 之**哪一端**（甲 ＝ `628-31(2)` `s` 訖／乙 ＝ `628-32(2)` `s` 起／丙 ＝ 二端分擔）。
🛑 **只歸因·⛔ 不修·⛔ 不判孰對孰錯。**

## `X-1` 停機款（**逐字·【單】·來源管線 ＝ KL 貼入之 `.md` 檔**）

> 新探針之**二共同錨**須與【倉】`verify/out/KL_UI_3.5m_2e08a41_stdout.log` 之 `[T2-DIAG]` `R2` 列逐位相符：
> 池帶1 `s` 寬 `8.4283`、`s` 域全寬 `99.7597`。**任一不符 ⇒ 先判量測器紅並停機上呈。**

## 量法

同 `-176` 探針：spy `ns["_pool_strips_for_block"]` 攔實收實參，以生產碼自身之
`ns["_strip_s_range"]`／`ns["_block_strip"]` 求量 ⇒ **⛔ 非外部重寫**。

`M-B-1`：以 `ns["_block_strip"]`（＝生產碼步驟 5 所用之同一支）切出甲／乙二候選薄片，
量其面積與平均深度，與【倉】池帶2 面積差 `1471.2568 − 1466.0294 = 5.2274`（± `0.0001`）對拍。
🛑 **判別力先報後判**：`|A甲 − A乙| ≥ 0.01` 方得擇一。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不修 `0.1171`。⛔ 不重跑 `run_all`。⛔ 不重產 baseline。
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
TARGET_BLK = "R2"
TARGET_SB = 3.5

# 【倉】verify/out/KL_UI_3.5m_2e08a41_stdout.log 之 [T2-DIAG] R2 列（4dp 顯示值）
APP = {"pool_w": [8.4283, 32.9640], "pool_a": [308.1700, 1466.0294],
       "degen_w": [1.27e-10, 1.83e-11, 4.23e-11], "s_dom": (0.2677, 100.0274),
       "n_biz": 14, "sum_pool_a": 1774.1994}
# X-1 之二共同錨
ANCHOR_POOL1_W = 8.4283
ANCHOR_S_SPAN = 99.7597


def _resolve_out(default_name):
    name = os.environ.get("WV_OUT_NAME") or default_name
    path = os.path.join(OUTDIR, name)
    if os.path.exists(path) and os.environ.get("WV_ALLOW_OVERWRITE") != "1":
        raise RuntimeError("拒絕覆寫既有 log：" + path + "　=> 請設 WV_OUT_NAME=<新檔名>")
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
    P("【W-G.9-177 M-B-1／M-B-3／M-B-4】R2 之 0.1171 歸屬 — ⛔ 零生產碼變更")
    P("=" * W)
    import shapely
    P("  環境：shapely " + shapely.__version__ + " | GEOS " + str(shapely.geos_version))

    ns, fake_st = harvest()
    _orig = ns["_pool_strips_for_block"]
    _strip_s_range = ns["_strip_s_range"]
    _block_strip = ns["_block_strip"]
    _S_EPS = ns["_S_EPS"]
    CAP = {}

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        if _label == TARGET_BLK and TARGET_BLK not in CAP:
            _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
            pids = []
            try:
                fr = sys._getframe(1)
                lr = fr.f_locals.get("left_results") or []
                rr = fr.f_locals.get("right_results") or []
                _SP_d = fr.f_locals.get("_SP_d")
                reb = []
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
                        reb.append((((_entry or {}).get("tp") or {}).get("暫編地號", "?"), _p))
                if len(reb) == len(_biz) and max(
                        abs(float(reb[i][1].area) - float(_biz[i].area))
                        for i in range(len(_biz))) == 0.0:
                    pids = [r[0] for r in reb]
            except Exception:                                         # noqa: BLE001
                pass
            CAP[TARGET_BLK] = {
                "block_poly": block_poly, "d_hat": d_hat, "corner_pt": corner_pt,
                "allocation_dir": allocation_dir, "biz": _biz, "pids": pids,
                "depth": _depth}
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
    ns["_pool_strips_for_block"] = _spy
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                           [tp for tp in build_p if tp.get("所屬街廓") == TARGET_BLK],
                           wins, forced, TARGET_SB)
            except Exception:                                         # noqa: BLE001
                pass
    finally:
        ns["_pool_strips_for_block"] = _orig

    if TARGET_BLK not in CAP:
        raise RuntimeError("🔴 母體為空（未攔到 " + TARGET_BLK + "）⇒ ⛔ 不得據此下任何結論")
    C = CAP[TARGET_BLK]
    bp_, dh, cp, ad = C["block_poly"], C["d_hat"], C["corner_pt"], C["allocation_dir"]

    # ── 複現步驟 1–4 ────────────────────────────────────────────
    s_min, s_max = _strip_s_range(bp_, dh, cp, ad)
    biz_iv = []
    for i, p in enumerate(C["biz"]):
        r = _strip_s_range(p, dh, cp, ad)
        biz_iv.append((r, float(p.area), C["pids"][i] if i < len(C["pids"]) else "?"))
    iv = sorted([b[0] for b in biz_iv if b[0] is not None])
    merged = []
    for a, b in iv:
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
    pool_iv = [(a, b) for a, b in pool_raw if (b - a) > _S_EPS]

    # ══ X-1：二共同錨（停機款）══
    P("")
    P("【X-1 停機款】二共同錨對拍（⛔ 不符即先判量測器紅並停機）")
    P("-" * W)
    got_p1 = pool_iv[0][1] - pool_iv[0][0]
    got_span = s_max - s_min
    a1 = abs(round(got_p1, 4) - ANCHOR_POOL1_W) < 5e-5
    a2 = abs(round(got_span, 4) - ANCHOR_S_SPAN) < 5e-5
    P("  池帶1 s 寬   期望 %10.4f   實得 %.10f   %s" % (ANCHOR_POOL1_W, got_p1, "✅" if a1 else "🔴"))
    P("  s 域全寬     期望 %10.4f   實得 %.10f   %s" % (ANCHOR_S_SPAN, got_span, "✅" if a2 else "🔴"))
    if not (a1 and a2):
        P("  🛑 X-1 不符 ⇒ 量測器紅 ⇒ 停機上呈")
        out = _resolve_out("probe_WG9177_R2_attrib_a44eb828.log")
        with open(out, "w", encoding="utf-8", newline="") as f:
            f.write("\n".join(L) + "\n")
        raise RuntimeError("🛑 X-1 二共同錨不符 ⇒ 停機")
    P("  ⇒ 2/2 ✅ 量測器非紅，續辦")

    # ══ M-B-1：深度剖面法 ══
    P("")
    P("【M-B-1】深度剖面法（甲／乙二候選薄片）")
    P("-" * W)
    p2_lo, p2_hi = pool_iv[1]
    wid = (APP["pool_w"][1])            # app 側池帶2 之 4dp 顯示寬
    dw = (p2_hi - p2_lo) - wid          # 寬差（shim − app）
    P("  shim 池帶2 s∈[%.10f, %.10f]  寬 %.10f" % (p2_lo, p2_hi, p2_hi - p2_lo))
    P("  app  池帶2 寬（4dp 顯示值）＝ %.4f" % wid)
    P("  ⇒ 寬差 ＝ %.10f　（🔒 app 側係 4dp 顯示 ⇒ 應記為 0.11707 ± 0.00005·⛔ 不得寫作恰為 0.1171）" % dw)

    def strip_area(a, b):
        bpt = np.asarray(cp, dtype=float) + a * np.asarray(dh, dtype=float)
        g, _ = _block_strip(bp_, dh, bpt, b - a, allocation_dir=ad)
        return (float(g.area) if (g is not None and not g.is_empty) else 0.0), g

    A_jia, g_jia = strip_area(p2_lo, p2_lo + dw)          # 甲：池帶2 之下端（628-31(2) 側）
    A_yi, g_yi = strip_area(p2_hi - dw, p2_hi)            # 乙：池帶2 之上端（628-32(2) 側）
    P("")
    P("  甲薄片  s∈[%.6f, %.6f]  面積 %.6f ㎡   平均深度 %.6f m" % (p2_lo, p2_lo + dw, A_jia, A_jia / dw))
    P("  乙薄片  s∈[%.6f, %.6f]  面積 %.6f ㎡   平均深度 %.6f m" % (p2_hi - dw, p2_hi, A_yi, A_yi / dw))
    P("")
    P("  🛑 判別力（先報後判）：|A甲 − A乙| = %.6f" % abs(A_jia - A_yi))
    TARGET_DA = APP["pool_a"][1]
    shim_p2_area = None
    P("  【倉】池帶2 面積差 ＝ 1471.2568 − 1466.0294 = 5.2274（二者皆 4dp ⇒ 差之不確定 ± 0.0001）")
    P("  殘差：甲 %.6f ／ 乙 %.6f" % (A_jia - 5.2274, A_yi - 5.2274))
    if abs(A_jia - A_yi) >= 0.01:
        pick = "甲" if abs(A_jia - 5.2274) < abs(A_yi - 5.2274) else "乙"
        P("  ⇒ ✅ 具判別力（≥ 0.01）⇒ 與 5.2274 相符者 ＝ %s" % pick)
    else:
        P("  ⇒ 🟡 **⛔ 判別力不足**（< 0.01）⇒ ⛔ 不得擇一，逕辦 M-B-2")

    # 對照：shim 池帶2 之實際面積
    _a, _g = strip_area(p2_lo, p2_hi)
    shim_p2_area = _a
    P("")
    P("  對照：shim 池帶2 實際面積 %.6f（【倉】shim 側 4dp ＝ 1471.2568·Δ=%.6f）"
      % (shim_p2_area, shim_p2_area - 1471.2568))
    P("        app  池帶2 面積（4dp 顯示）＝ %.4f" % TARGET_DA)
    P("        面積差（shim − app）＝ %.6f" % (shim_p2_area - TARGET_DA))

    # ══ M-B-3：退化帶指紋 ══
    P("")
    P("【M-B-3】退化帶指紋（輔證·⛔ 不得單獨作結）")
    P("-" * W)
    P("  shim：raw 帶 %d ＝ 池帶 %d ＋ 退化 %d　⇒ merged %d 段"
      % (len(pool_raw), len(pool_iv), len(degen), len(merged)))
    for i, (a, b) in enumerate(degen, 1):
        prv = nxt = "—"
        for (r, ar, pid) in biz_iv:
            if r is None:
                continue
            if abs(r[1] - a) < 1e-6:
                prv = pid
            if abs(r[0] - b) < 1e-6:
                nxt = pid
        P("    退化%d s∈[%.10f, %.10f] 寬 %.6e  前接 %s ／ 後接 %s" % (i, a, b, b - a, prv, nxt))
    P("  app （【倉】[T2-DIAG]）：池帶 %d ＋ 退化 %d ＝ raw %d ⇒ merged %d 段"
      % (len(APP["pool_w"]), len(APP["degen_w"]),
         len(APP["pool_w"]) + len(APP["degen_w"]),
         len(APP["pool_w"]) + len(APP["degen_w"]) - 1))
    P("  ⇒ app 較 shim **多切一刀**（merged 4 段 vs 3 段）")
    P("  app 退化帶寬：" + ", ".join("%.2e" % w for w in APP["degen_w"]))
    P("  shim 退化帶寬：" + ", ".join("%.2e" % (b - a) for a, b in degen))
    P("  🔒 可對之一格：app 4.23e-11 ↔ shim %.2e（皆 s 域上端點）"
      % (degen[-1][1] - degen[-1][0] if degen else float('nan')))

    # ══ M-B-1 附：merged 段與宗之對應 ══
    P("")
    P("【附】merged 段與其端點所屬之宗")
    P("-" * W)
    for i, (a, b) in enumerate(merged, 1):
        lo_pid = hi_pid = "—"
        for (r, ar, pid) in biz_iv:
            if r is None:
                continue
            if abs(r[0] - a) < 1e-9:
                lo_pid = pid
            if abs(r[1] - b) < 1e-9:
                hi_pid = pid
        P("  段%d s∈[%.6f, %.6f] 寬 %.10f   下界宗 %s ／ 上界宗 %s"
          % (i, a, b, b - a, lo_pid, hi_pid))

    # ══ M-B-4：收斂驗證（族③ 單獨） ══
    P("")
    P("【M-B-4】收斂驗證：於探針內把 shim 之 `_select_pool_slot['b']` 換成 **app 之舊式**")
    P("-" * W)
    P("  差異點（M-B-2 所得·同屬 app.py:9117 自陳之『族②③』）：")
    P("    族② `_W_prev_*` 初值：app `(buffer_S*_cos_dn) if has_corner else 0.0` vs stepg `0.0`")
    P("    族③ `_select_pool_slot['b']`：app `buffer_S*_cos_dn`（⛔ 無 forced 條件）"
      " vs stepg `_mp_base_W0(...) if _fo_* else 0.0`")
    P("  🛑 **族② ⛔ 不可由外部覆寫**（其為 `_advance_block_with_split` 之函式內局部初值）"
      "⇒ 本閘**只測族③**，族② 之影響**⛔ 未測**（具名·⛔ 不得讀為已排除）。")

    SPS = {}
    _orig_sps = ns["_select_pool_slot"]

    def _spy_sps(widths, left_side, right_side, rw_func=None):
        fr = sys._getframe(1)
        lb = fr.f_locals.get("_left_buffer_S")
        rb = fr.f_locals.get("_right_buffer_S")
        cd = fr.f_locals.get("_cos_dn")
        blk = fr.f_locals.get("blk_label")
        r_orig = _orig_sps(widths, left_side, right_side, rw_func)
        rec = {"blk": blk, "b_stepg": (left_side.get("b"), right_side.get("b")),
               "lb": lb, "rb": rb, "cos_dn": cd, "k_stepg": r_orig.get("k")}
        if lb is not None and rb is not None and cd is not None:
            ls2 = dict(left_side); ls2["b"] = float(lb) * float(cd)
            rs2 = dict(right_side); rs2["b"] = float(rb) * float(cd)
            r_app = _orig_sps(widths, ls2, rs2, rw_func)
            rec["b_app"] = (ls2["b"], rs2["b"])
            rec["k_app"] = r_app.get("k")
            rec["ret"] = r_app
        else:
            rec["b_app"] = rec["k_app"] = None
            rec["ret"] = r_orig
        SPS.setdefault(blk, []).append(rec)
        return rec["ret"] if rec["k_app"] is not None else r_orig

    CAP2 = {}

    def _spy2(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
              _label='', _depth=None, _verbose=True):
        if _label == TARGET_BLK and TARGET_BLK not in CAP2:
            _bz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
            _sm, _sx = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
            _iv = sorted([r for r in (_strip_s_range(p, d_hat, corner_pt, allocation_dir)
                                      for p in _bz) if r is not None])
            _mg = []
            for a, b in _iv:
                if _mg and a <= _mg[-1][1]:
                    _mg[-1] = (_mg[-1][0], max(_mg[-1][1], b))
                else:
                    _mg.append((a, b))
            _pr, _cu = [], _sm
            for a, b in _mg:
                if a > _cu:
                    _pr.append((_cu, min(a, _sx)))
                _cu = max(_cu, b)
            if _cu < _sx:
                _pr.append((_cu, _sx))
            CAP2[TARGET_BLK] = {
                "n_biz": len(_bz), "s_dom": (_sm, _sx), "merged": _mg,
                "degen": [(a, b) for a, b in _pr if (b - a) <= _S_EPS],
                "pool": [(a, b) for a, b in _pr if (b - a) > _S_EPS]}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)

    ns["_select_pool_slot"] = _spy_sps
    ns["_pool_strips_for_block"] = _spy2
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                           [tp for tp in build_p if tp.get("所屬街廓") == TARGET_BLK],
                           wins, forced, TARGET_SB)
            except Exception as _e2:                                  # noqa: BLE001
                pass
    finally:
        ns["_select_pool_slot"] = _orig_sps
        ns["_pool_strips_for_block"] = _orig

    P("")
    P("  _select_pool_slot 之實收（spy·⛔ 非由命名推定）")
    for blk, recs in SPS.items():
        for r in recs:
            P("    街廓 %-4s  _left_buffer_S=%s  _right_buffer_S=%s  _cos_dn=%s"
              % (blk, r["lb"], r["rb"], r["cos_dn"]))
            P("             b(stepg)=%s   ->   b(app 舊式)=%s" % (r["b_stepg"], r["b_app"]))
            P("             k*(stepg)=%s   ->   k*(app 舊式)=%s   %s"
              % (r["k_stepg"], r["k_app"],
                 "⇒ k* **相同**" if r["k_stepg"] == r["k_app"] else "⇒ 🔴 k* **相異**"))

    P("")
    P("  【閘 C】覆寫後之池帶2 s 寬")
    if TARGET_BLK not in CAP2:
        P("    🔴 未攔到 %s ⇒ ⛔ 不得下結論" % TARGET_BLK)
    else:
        C2 = CAP2[TARGET_BLK]
        P("    merged %d 段／池帶 %d／退化 %d" % (len(C2["merged"]), len(C2["pool"]), len(C2["degen"])))
        for i, (a, b) in enumerate(C2["pool"], 1):
            P("      池帶%d s∈[%.6f, %.6f] 寬 %.10f" % (i, a, b, b - a))
        if len(C2["pool"]) > 1:
            w2 = C2["pool"][1][1] - C2["pool"][1][0]
            d2 = abs(w2 - APP["pool_w"][1])
            P("    池帶2 寬 %.10f   vs  app 期望 %.4f   |Δ| = %.10f   %s"
              % (w2, APP["pool_w"][1], d2,
                 "✅ 閘 C 過（|Δ| ≤ 0.0001）⇒ 歸因成立" if d2 <= 0.0001
                 else "🔴 閘 C ⛔ 不過 ⇒ 照實回報·該差異點降為「候選」"))
        else:
            P("    🔴 池帶數 %d ≠ 2 ⇒ 閘 C ⛔ 不適用" % len(C2["pool"]))

    # ══ M-B-4b：族② 之收斂驗證（🔒 CC 自加·超出單之字面·仍在 N-3 受詞內） ══
    P("")
    P("【M-B-4b】族② 收斂驗證（🔒 **CC 自加**·⛔ 非單所令·仍在 `N-3` 受詞內）")
    P("-" * W)
    P("  作法：spy `ns[\"_solve_G_one\"]`（module 級·`probe_D2b24C_pool.py` 先例），")
    P("        凡 `side_mid is not None` ∧ `W_prev == 0.0` 者（＝該趟左組之首宗），把 `W_prev`")
    P("        由 stepg 之 `0.0` 改為 **app 舊式** `_left_buffer_S * _cos_dn`。")
    P("        🛑 判準已由**實收 spy** 定（⛔ 非由命名推定）：`side` 之相異實收值 ＝ ['無']")
    P("        （⛔ 非 'left'/'right'）；`W_prev==0.0` 者 16/28（右組無街角故恆 0）⇒ 單以")
    P("        `W_prev==0.0` 為框會誤咬 14 筆。加 `side_mid is not None` 後**期望命中恰 2**")
    P("        （＝ `_advance_block_with_split` 之 2 趟各一）；命中 ≠ 2 即判量測器紅。")
    P("  ⛔ **未動 `app.py` 一字**（⇒ ⛔ 不觸 `X-2`）。")

    B_APP_LEFT = None
    for _rl in SPS.get(TARGET_BLK, []):
        if _rl.get("b_app"):
            B_APP_LEFT = _rl["b_app"][0]
    P("  注入值 `_left_buffer_S * _cos_dn` ＝ %r" % B_APP_LEFT)

    CAP3 = {}
    HITS = {"n": 0, "vals": []}
    _origG = ns["_solve_G_one"]

    def _spyG(**kw):
        if (B_APP_LEFT is not None and kw.get("side_mid") is not None
                and float(kw.get("W_prev", 0.0) or 0.0) == 0.0):
            HITS["n"] += 1
            HITS["vals"].append(kw.get("a_m2"))
            kw = dict(kw)
            kw["W_prev"] = float(B_APP_LEFT)
        return _origG(**kw)

    def _spy3(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
              _label='', _depth=None, _verbose=True):
        if _label == TARGET_BLK and TARGET_BLK not in CAP3:
            _bz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
            _sm, _sx = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
            _iv = sorted([r for r in (_strip_s_range(p, d_hat, corner_pt, allocation_dir)
                                      for p in _bz) if r is not None])
            _mg = []
            for a, b in _iv:
                if _mg and a <= _mg[-1][1]:
                    _mg[-1] = (_mg[-1][0], max(_mg[-1][1], b))
                else:
                    _mg.append((a, b))
            _pr, _cu = [], _sm
            for a, b in _mg:
                if a > _cu:
                    _pr.append((_cu, min(a, _sx)))
                _cu = max(_cu, b)
            if _cu < _sx:
                _pr.append((_cu, _sx))
            CAP3[TARGET_BLK] = {
                "n_biz": len(_bz), "merged": _mg,
                "degen": [(a, b) for a, b in _pr if (b - a) <= _S_EPS],
                "pool": [(a, b) for a, b in _pr if (b - a) > _S_EPS]}
        return _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                     _label=_label, _depth=_depth, _verbose=_verbose)

    if B_APP_LEFT is None:
        P("  🔴 注入值不可得 ⇒ 本閘⛔ 不適用")
    else:
        ns["_solve_G_one"] = _spyG
        ns["_pool_strips_for_block"] = _spy3
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                               [tp for tp in build_p if tp.get("所屬街廓") == TARGET_BLK],
                               wins, forced, TARGET_SB)
                except Exception:                                     # noqa: BLE001
                    pass
        finally:
            ns["_solve_G_one"] = _origG
            ns["_pool_strips_for_block"] = _orig
        P("  注入命中次數 ＝ %d（期望 2）　%s" % (HITS["n"], "✅" if HITS["n"] == 2 else "🔴 量測器紅 ⇒ 結論不採信"))
        if TARGET_BLK not in CAP3:
            P("  🔴 未攔到 %s ⇒ ⛔ 不得下結論" % TARGET_BLK)
        else:
            C3 = CAP3[TARGET_BLK]
            P("  merged %d 段／池帶 %d／退化 %d"
              % (len(C3["merged"]), len(C3["pool"]), len(C3["degen"])))
            for i, (a, b) in enumerate(C3["pool"], 1):
                P("    池帶%d s∈[%.6f, %.6f] 寬 %.10f" % (i, a, b, b - a))
            for i, (a, b) in enumerate(C3["merged"], 1):
                P("    merged段%d s∈[%.6f, %.6f] 寬 %.10f" % (i, a, b, b - a))
            P("  【閘 C′】")
            if len(C3["pool"]) > 1:
                w2 = C3["pool"][1][1] - C3["pool"][1][0]
                d2 = abs(w2 - APP["pool_w"][1])
                P("    池帶2 寬 %.10f  vs app 期望 %.4f  |Δ| = %.10f  %s"
                  % (w2, APP["pool_w"][1], d2,
                     "✅ 閘 C′ 過 ⇒ 族② 歸因成立" if d2 <= 0.0001
                     else "🔴 閘 C′ ⛔ 不過 ⇒ 照實回報·族② 亦降為「候選」"))
            else:
                P("    🔴 池帶數 %d ≠ 2 ⇒ 閘 C′ ⛔ 不適用（照實回報）" % len(C3["pool"]))
            P("    退化帶數 %d（app 期望 3·shim 原 2）%s"
              % (len(C3["degen"]),
                 "⇒ 🔑 與 app 相同" if len(C3["degen"]) == 3 else "⇒ ⛔ 未收斂至 3"))

    P("")
    P("🛑 本檔只歸因·⛔ 未修·⛔ 未動生產碼一字。")
    P("=" * W)

    out = _resolve_out("probe_WG9177_R2_attrib_a44eb828.log")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("WROTE " + out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
