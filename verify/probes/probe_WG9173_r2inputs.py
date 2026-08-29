# -*- coding: utf-8 -*-
"""`W-G.9-173` `M-A-2`：`R2` 池計算之**全部輸入**於 shim 路徑之實值（⛔ 只讀·⛔ 零生產碼）。

🛑 **可量者只有 shim 一側**（`W-G.9-172 M-A-1`：app `main()` 之呼叫端 `app.py:20892`
被 `app_harvest._filter_module` 濾除·結構上到不了）⇒ KL 側之對照僅有其實跑回報之**四則逐字事實**。
本探針把 shim 側之輸入**逐項出艙**，供與該四則逐字事實 ＋ **`verify/baselines/v3` 之 Step-G 基準**三方對拍。
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
sys.path.insert(0, VERIFY)
L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    import subprocess
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


def _h(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True,
                                     ensure_ascii=False).encode("utf-8")).hexdigest()[:16]


def main():
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    head, blob = git1(["rev-parse", "HEAD"]), git1(["rev-parse", "HEAD:app.py"])
    say("=" * 100)
    say("【W-G.9-173 M-A-2】`R2` 池計算之輸入（shim 路徑·情境 `3.5m`）")
    say("=" * 100)
    say("  HEAD = %s ／ app.py blob = %s" % (head, blob))

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    raw = open(rv.V6DXF, "rb").read()
    temp, build, _sw = build_build_parcels(ns, fake_st, raw, list(cb_by.values()),
                                           snapshot)
    setback, tag = 3.5, "3.5m"
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    diag, sel, off, winners_state, forced_map = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, setback,
        snapshot=snapshot)

    ss = fake_st.session_state
    say()
    say("── 步驟 L／街角 PK 之產物（shim 側）──")
    say("   winners_state = %r" % (winners_state,))
    say("   forced_map    = %r" % (forced_map,))
    say("   f3L_forced_offset(ss) = %r" % (ss.get("f3L_forced_offset"),))
    say("   f3_corner_winners(ss) = %r" % (ss.get("f3_corner_winners"),))
    _lock = ss.get("k6_step0_blocks_locked") or ss.get("blocks_locked_k921")
    say("   K-9-21 blocks_locked（二候選鍵）= %r ／ %r"
        % (ss.get("k6_step0_blocks_locked"), ss.get("blocks_locked_k921")))
    say("   ss 中含 'lock' 之鍵 = %r"
        % sorted(k for k in ss.keys() if "lock" in str(k).lower()))
    say("   ss 中含 'forced' 之鍵 = %r"
        % sorted(k for k in ss.keys() if "forced" in str(k).lower()))
    # 步驟 L 覆寫筆數（KL 側逐字 7 筆）
    pm = ss.get("f3_g_iter_params", {}) or {}
    n_corner = sum(1 for v in pm.values() if isinstance(v, dict) and v.get("is_corner"))
    say("   `f3_g_iter_params` 之 is_corner=True 筆數 = **%d**（KL 側逐字「步驟 L 覆寫 7 筆」）"
        % n_corner)
    say("   其明細 = %r"
        % {k: {kk: v.get(kk) for kk in ("is_corner", "side")}
           for k, v in pm.items() if isinstance(v, dict) and v.get("is_corner")})

    CAP = []
    orig = ns["_pool_strips_for_block"]

    def spy(*a, **k):
        lbl = k.get("_label", "") or (a[5] if len(a) >= 6 else "")
        rec = {"街廓": str(lbl),
               "block_poly_area": float(a[0].area) if a and a[0] is not None else None,
               "d_hat": [float(x) for x in a[1]] if a[1] is not None else None,
               "corner_pt": [float(x) for x in a[2]] if a[2] is not None else None,
               "allocation_dir": ([float(x) for x in a[3]]
                                  if a[3] is not None else None),
               "_depth": (float(k.get("_depth")) if k.get("_depth") is not None
                          else None),
               "biz_n": len(a[4]),
               "biz": [{"area": round(float(p.area), 9),
                        "npts": len(list(p.exterior.coords)),
                        "sha16": hashlib.sha256(
                            ("|".join("%.9f,%.9f" % (x, y)
                                      for x, y in p.exterior.coords)
                             ).encode("utf-8")).hexdigest()[:16]}
                       for p in a[4]]}
        try:
            res = orig(*a, **k)
            rec["狀態"] = "OK"
            rec["池片"] = [round(float(g.area), 9) for g in res]
            rec["Σ池"] = float(sum(g.area for g in res))
        except Exception as e:                                    # noqa: BLE001
            rec["狀態"] = "RAISE"
            rec["例外"] = repr(e)[:240]
            rec["池片"], rec["Σ池"] = [], None
            CAP.append(rec)
            return []
        CAP.append(rec)
        return res

    ns["_pool_strips_for_block"] = spy
    err = None
    try:
        run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build,
                   winners_state, forced_map, setback)
    except Exception as e:                                        # noqa: BLE001
        err = repr(e)[:200]
    finally:
        ns["_pool_strips_for_block"] = orig

    say()
    say("── 池呼叫之逐項輸入（run_step_g 期末例外 = %s）──" % (err or "（無）"))
    for r in CAP:
        say("   ══ 街廓 %s ══ 狀態 %s" % (r["街廓"], r["狀態"]))
        say("      block_poly.area = %.9f ／ _depth = %s" % (r["block_poly_area"], r["_depth"]))
        say("      d_hat = %s ／ corner_pt = %s ／ allocation_dir = %s"
            % (r["d_hat"], r["corner_pt"], r["allocation_dir"]))
        say("      biz_n = **%d** ／ Σbiz.area = %.9f"
            % (r["biz_n"], sum(b["area"] for b in r["biz"])))
        for i, b in enumerate(r["biz"]):
            say("         biz[%2d] area=%-14.6f npts=%-3d sha16=%s"
                % (i, b["area"], b["npts"], b["sha16"]))
        if r["狀態"] == "OK":
            say("      ⇒ 池片 = %s ／ **Σ池 = %.9f**" % (r["池片"], r["Σ池"]))
        else:
            say("      ⇒ 例外：%s" % r["例外"])

    # ── 三方對拍（shim ／ v3 Step-G baseline ／ KL 逐字）──
    import csv
    bp = os.path.join(VERIFY, "baselines", "v3", "G 值計算結果_退縮3.5m.csv")
    agg = {}
    with open(bp, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if "抵費地" in (row.get("暫編地號") or ""):
                agg.setdefault(row.get("所屬街廓"), []).append(
                    float(row.get("幾何面積(㎡)") or 0))
    KL = {"R1": 1175.10, "R2": 1774.20, "R4": 1228.36, "R6": 1628.71}
    shim = {r["街廓"]: r["Σ池"] for r in CAP if r["Σ池"] is not None}
    say()
    say("── 🔴 三方對拍（情境 `3.5m`·Step-G 階段）──")
    say("   %-5s %-16s %-16s %-16s %-12s %s"
        % ("街廓", "v3 baseline Σ", "KL app（2dp）", "shim Σ", "KL−base", "shim−base"))
    for k in ("R1", "R2", "R4", "R6"):
        b = sum(agg.get(k, [])) if k in agg else None
        s = shim.get(k)
        say("   %-5s %-16s %-16s %-16s %-12s %s"
            % (k,
               ("%.4f" % b) if b is not None else "—",
               ("%.2f" % KL[k]),
               ("%.6f" % s) if s is not None else "⛔ 不可達",
               ("%+.4f" % (KL[k] - b)) if b is not None else "—",
               ("%+.4f" % (s - b)) if (s is not None and b is not None) else "—"))
    for k in ("R1", "R2"):
        say("   %s 逐片：v3 baseline = %s ／ shim = %s"
            % (k, [round(x, 4) for x in agg.get(k, [])],
               [round(x, 4) for x in (next((r["池片"] for r in CAP
                                            if r["街廓"] == k), []))]))

    p = os.path.join(OUTDIR, "WG9173_r2inputs_%s.json" % blob[:8])
    with open(p, "w", encoding="utf-8", newline="") as f:
        json.dump({"head": head, "blob": blob, "cap": CAP,
                   "winners": winners_state, "forced": forced_map,
                   "baseline_v3": agg, "KL": KL, "err": err},
                  f, ensure_ascii=False, indent=1)
    say()
    say("  證據檔：verify/out/%s" % os.path.basename(p))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    rc = main()
    with open(os.path.join(OUTDIR, "probe_WG9173_r2inputs.log"),
              "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    sys.exit(rc)
