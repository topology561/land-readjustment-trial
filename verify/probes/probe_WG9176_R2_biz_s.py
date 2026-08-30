r"""**W-G.9-176 `M-A-2`〜`M-A-4`**：`R2`（`3.5m`）之**逐宗 s 區間**全量 dump — ⛔ **零生產碼變更**

## 受詞

`W-G.9-176 §一 N-4`：`Σ(宗帶 s 寬)` 之 `0.1171 m` 差落在 `14` 宗之哪一宗，抑或係逐宗累積。
**本檔只定位、⛔ 不作結論、⛔ 不動生產碼。**

## 量法

spy `ns["_pool_strips_for_block"]`（單一真相源·`app.py` `def _pool_strips_for_block`），
攔其**實收實參**，再以**生產碼自身之 `ns["_strip_s_range"]`** 對每個 `biz_poly` 算 s 區間
——⛔ 非外部重寫，係對同一組輸入呼叫**同一支函式**。

逐字對照生產碼步驟 1–4（`grep -n "def _pool_strips_for_block" app.py` 後之
「1. s 域」「2. 業主宗之 s 區間」「3. 業主宗區間之聯集」「4. 補區間＝池 s-帶」）。

🔒 **框之具名（`W-G.9-176 P-2` 擴充式）**
  · `Σ(逐宗 s 寬)`  ＝ `Σ(b−a) over biz_iv`（**未聯集**·相鄰宗可重疊 ⇒ 可 > 覆蓋長）
  · `Σ(宗帶 s 寬)`  ＝ `Σ(b−a) over merged`（**聯集後**·與池帶互補）← 施工單自檢錨用此框

## 自我驗證閘（CLAUDE.md「探針還原內部幾何時須以碼面自身之保證當自我驗證閘」）

**閘 A（地號對應之保真）**：自 caller frame 重建之 `allocated_polys` 須與實收 `biz_polys`
  **個數相同 ＋ 逐一面積逐位相同**；不符即該格作廢。
**閘 B（外部錨·施工單 `M-A-2` 逐字）**：`Σ(宗帶 s 寬)＝58.2503`／第一池帶 `8.4283`／
  第二池帶 `33.0811`／三者和＋退化帶 ＝ `99.7597`（＝ `100.0274 − 0.2677`）。
  🛑 ⛔ 不符即**先判量測器紅**（常規五），⛔ 不得逕報受詞。

## ⛔ 本檔不做

⛔ 不改生產碼一字。⛔ 不解該 `0.1171`。⛔ 不重跑 `run_all`。⛔ 不重產 baseline。
⛔ 不改期望 FAIL 名單。⛔ 不寫死本機絕對路徑（`run_all.py` 之全倉機檢）。
"""
import contextlib
import io
import os
import sys

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

# 外部錨（【單】`W-G.9-176 M-A-2` 逐字·⛔ 非本探針所產）
ANCHOR = {"sum_merged": 58.2503, "pool1": 8.4283, "pool2": 33.0811, "total": 99.7597}
# app 側對照（【倉】`verify/out/KL_UI_3.5m_2e08a41_stdout.log` 之 [T2-DIAG] R2 列）
APP_SIDE = {"pool_w": [8.4283, 32.9640], "pool_a": [308.1700, 1466.0294],
            "degen_w": [1.27e-10, 1.83e-11, 4.23e-11],
            "s_dom": (0.2677, 100.0274), "n_biz": 14}


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
    P("【W-G.9-176 M-A-2〜M-A-4】R2（3.5m）逐宗 s 區間全量 dump — ⛔ 零生產碼變更")
    P("=" * W)
    import shapely
    P("  環境：shapely " + shapely.__version__ + " | GEOS " + str(shapely.geos_version))

    ns, fake_st = harvest()
    _orig = ns["_pool_strips_for_block"]
    _strip_s_range = ns["_strip_s_range"]
    _S_EPS = ns["_S_EPS"]
    CAP = {}

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label='', _depth=None, _verbose=True):
        if _label == TARGET_BLK and TARGET_BLK not in CAP:
            rec = {}
            _biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]
            rec["n_biz"] = len(_biz)

            # ── 閘 A：自 caller frame 重建地號對應 ──────────────────────
            pids, gateA = [], "⛔ 未取得 caller frame"
            try:
                fr = sys._getframe(1)
                lr = fr.f_locals.get("left_results") or []
                rr = fr.f_locals.get("right_results") or []
                _SP_d = fr.f_locals.get("_SP_d")
                reb = []
                for _entry, _res in (list(lr) + list(rr)):
                    _coords = _res.get("cut_coords") or []
                    _p = None
                    if len(_coords) >= 3 and _SP_d is not None:
                        try:
                            _p = _SP_d(_coords)
                            if not _p.is_valid:
                                _p = _p.buffer(0)
                        except Exception:
                            _p = None
                    if _p is not None and not _p.is_empty:
                        reb.append((((_entry or {}).get("tp") or {}).get("暫編地號", "?"), _p))
                if len(reb) == len(_biz):
                    diffs = [abs(float(reb[i][1].area) - float(_biz[i].area))
                             for i in range(len(_biz))]
                    if max(diffs) == 0.0:
                        pids = [r[0] for r in reb]
                        gateA = "✅ 個數 %d 相同 ＋ 逐一面積逐位相同（max|Δarea| = 0.0）" % len(reb)
                    else:
                        gateA = "🔴 面積不逐位相同 max|Δ| = %.12g" % max(diffs)
                else:
                    gateA = "🔴 個數不同：重建 %d vs 實收 %d" % (len(reb), len(_biz))
            except Exception as e:                                    # noqa: BLE001
                gateA = "🔴 " + type(e).__name__ + ": " + str(e)
            rec["gateA"] = gateA
            rec["pids"] = pids

            # ── 逐字複現生產碼步驟 1–4（同一支 _strip_s_range）─────────
            _dom = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
            s_min, s_max = _dom
            rec["s_dom"] = (s_min, s_max)

            biz_iv = []
            for i, p in enumerate(_biz):
                r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
                biz_iv.append((r, float(p.area), pids[i] if i < len(pids) else "?"))
            # 生產碼於此 sort（僅對有效 r）；本檔保留原序另存排序序
            rec["biz_raw"] = biz_iv
            iv_only = sorted([b[0] for b in biz_iv if b[0] is not None])
            rec["biz_iv_sorted"] = iv_only

            merged = []
            for a, b in iv_only:
                if merged and a <= merged[-1][1]:
                    merged[-1] = (merged[-1][0], max(merged[-1][1], b))
                else:
                    merged.append((a, b))
            rec["merged"] = merged

            pool_iv = []
            cur = s_min
            for a, b in merged:
                if a > cur:
                    pool_iv.append((cur, min(a, s_max)))
                cur = max(cur, b)
            if cur < s_max:
                pool_iv.append((cur, s_max))
            rec["pool_iv_raw"] = list(pool_iv)
            rec["degen_iv"] = [(a, b) for a, b in pool_iv if (b - a) <= _S_EPS]
            rec["pool_iv"] = [(a, b) for a, b in pool_iv if (b - a) > _S_EPS]
            rec["S_EPS"] = float(_S_EPS)
            CAP[TARGET_BLK] = rec
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
    rec = CAP[TARGET_BLK]

    # ══ 閘 A ══
    P("")
    P("【閘 A】地號對應之保真（重建 allocated_polys vs 實收 biz_polys）")
    P("-" * W)
    P("  " + rec["gateA"])

    # ══ M-A-2：逐宗全量 ══
    P("")
    P("【M-A-2】R2 逐宗 s 區間全量（框：s 起/訖 ＝ ns['_strip_s_range'] 之回傳·未捨入）")
    P("-" * W)
    P("  街廓 s 域 = [%.4f, %.4f]　全域寬 = %.10f" %
      (rec["s_dom"][0], rec["s_dom"][1], rec["s_dom"][1] - rec["s_dom"][0]))
    P("  宗數 = %d" % rec["n_biz"])
    P("")
    P("  %-3s %-16s %12s %12s %12s %14s" % ("#", "暫編地號", "s 起", "s 訖", "s 寬", "面積(㎡)"))
    sum_raw = 0.0
    for i, (r, ar, pid) in enumerate(rec["biz_raw"], 1):
        if r is None:
            P("  %-3d %-16s %12s %12s %12s %14.4f" % (i, pid, "None", "None", "None", ar))
            continue
        sum_raw += (r[1] - r[0])
        P("  %-3d %-16s %12.4f %12.4f %12.4f %14.4f" % (i, pid, r[0], r[1], r[1] - r[0], ar))
    P("")
    P("  Σ(逐宗 s 寬)【未聯集框】 = %.10f" % sum_raw)

    sum_merged = sum(b - a for a, b in rec["merged"])
    P("")
    P("  merged（聯集後·%d 段）：" % len(rec["merged"]))
    for i, (a, b) in enumerate(rec["merged"], 1):
        P("    段%d  s∈[%.4f, %.4f]  寬 %.10f" % (i, a, b, b - a))
    P("  Σ(宗帶 s 寬)【聯集框·施工單自檢錨用此框】 = %.10f" % sum_merged)
    P("  ⇒ 二框之差（重疊量） = %.10f" % (sum_raw - sum_merged))

    # ══ 池帶 ══
    P("")
    P("【M-A-2】池帶（濾除退化前 %d 帶 → 後 %d 帶）" %
      (len(rec["pool_iv_raw"]), len(rec["pool_iv"])))
    P("-" * W)
    for i, (a, b) in enumerate(rec["pool_iv"], 1):
        P("    池帶%d  s∈[%.4f, %.4f]  寬 %.10f" % (i, a, b, b - a))
    sum_pool = sum(b - a for a, b in rec["pool_iv"])
    P("  Σ(池帶 s 寬) = %.10f" % sum_pool)

    # ══ M-A-4：退化帶 ══
    P("")
    P("【M-A-4】退化帶逐帶具名（_S_EPS = %.6g）" % rec["S_EPS"])
    P("-" * W)
    P("  shim 側 %d 個：" % len(rec["degen_iv"]))
    for i, (a, b) in enumerate(rec["degen_iv"], 1):
        # 落於哪二宗之間
        prev_pid = nxt_pid = "—"
        for (r, ar, pid) in rec["biz_raw"]:
            if r is None:
                continue
            if abs(r[1] - a) < 1e-6:
                prev_pid = pid
            if abs(r[0] - b) < 1e-6:
                nxt_pid = pid
        P("    退化%d  s∈[%.10f, %.10f]  寬 %.6e   前接 %s ／ 後接 %s"
          % (i, a, b, b - a, prev_pid, nxt_pid))
    P("  app 側 %d 個（【倉】KL_UI_3.5m_2e08a41_stdout.log 之 [T2-DIAG]·⛔ 只有寬、無 s 位置）："
      % len(APP_SIDE["degen_w"]))
    P("    " + ", ".join("%.2e" % w for w in APP_SIDE["degen_w"]))
    P("  Σ(退化帶寬)shim = %.6e" % sum(b - a for a, b in rec["degen_iv"]))

    # ══ 閘 B：外部錨 ══
    P("")
    P("【閘 B】外部錨對拍（【單】W-G.9-176 M-A-2 逐字·⛔ 不符即先判量測器紅）")
    P("-" * W)
    got = {"sum_merged": sum_merged,
           "pool1": rec["pool_iv"][0][1] - rec["pool_iv"][0][0] if len(rec["pool_iv"]) > 0 else None,
           "pool2": rec["pool_iv"][1][1] - rec["pool_iv"][1][0] if len(rec["pool_iv"]) > 1 else None,
           "total": sum_merged + sum_pool + sum(b - a for a, b in rec["degen_iv"])}
    ok = 0
    for k in ("sum_merged", "pool1", "pool2", "total"):
        g = got[k]
        e = ANCHOR[k]
        hit = (g is not None) and (abs(round(g, 4) - e) < 5e-5)
        ok += 1 if hit else 0
        P("  %-11s 期望 %10.4f   實得 %s   %s"
          % (k, e, ("%.10f" % g) if g is not None else "None", "✅" if hit else "🔴"))
    P("  ⇒ 閘 B：%d/4 %s" % (ok, "✅ 全中" if ok == 4 else "🔴 未全中 ⇒ 先判量測器紅"))

    # ══ M-A-3：可比量之交集 ══
    P("")
    P("【M-A-3】二路徑可比量之交集（app 側缺者逐項標 ⚠️）")
    P("-" * W)
    P("  %-22s %18s %18s %12s" % ("量", "app（KL stdout）", "shim（本檔）", "Δ"))
    rows = [("街廓 s 域 下界", APP_SIDE["s_dom"][0], rec["s_dom"][0]),
            ("街廓 s 域 上界", APP_SIDE["s_dom"][1], rec["s_dom"][1]),
            ("宗數", float(APP_SIDE["n_biz"]), float(rec["n_biz"])),
            ("池帶1 s 寬", APP_SIDE["pool_w"][0], got["pool1"]),
            ("池帶2 s 寬", APP_SIDE["pool_w"][1], got["pool2"]),
            ("Σ(宗帶 s 寬)", 99.7597 - sum(APP_SIDE["pool_w"]), sum_merged),
            ("退化帶個數", float(len(APP_SIDE["degen_w"])), float(len(rec["degen_iv"])))]
    for nm, a, b in rows:
        P("  %-22s %18.4f %18.4f %12.4f" % (nm, a, b, b - a))
    P("")
    P("  ⚠️ app 側⛔ 無通道之量（`M-A-1` 四通道現查·逐項）：")
    for nm in ("逐宗 暫編地號↔s 起", "逐宗 s 訖", "逐宗 s 寬", "merged 分段",
               "退化帶之 s 位置", "池帶之 s 起訖"):
        P("      ⚠️ %-24s app 側⛔ 無通道（⛔ 不得以 shim 之值代填）" % nm)

    P("")
    P("🛑 本檔只定位、⛔ 不作結論、⛔ 未動生產碼一字。")
    P("=" * W)

    out = _resolve_out("probe_WG9176_R2_biz_s.log")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    print("WROTE " + out, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
