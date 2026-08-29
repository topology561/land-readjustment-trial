# -*- coding: utf-8 -*-
"""`W-G.9-172` `M-A` 探針：抵費地池面積之逐街廓量測（⛔ 只讀·⛔ 零生產碼）。

`M-A-1`　可行性現查：以 `verify/app_harvest.py` 之 `harvest()` shim 驅動池面積計算鏈。
`M-A-2`　逐街廓池面積之**未捨入**實值（`>= 6` 位小數）＋ 逐池片面積。
🛑 **具名之偏離**（`M-A-1` 所令之「逐項具名差異」）：
  ① 池之**呼叫端**係 `verify/stepg_pipeline.run_step_g`，⛔ 非 `app.py:main()`
     ——`main()` 內之敘述被 `app_harvest._filter_module` 濾除，shim **結構上到不了**。
     二呼叫端之實參式**逐字相同**（`app.py` 之呼叫 vs `stepg_pipeline` 之呼叫），
     惟其上游之組裝碼分屬二份 ⇒ 本探針所量者係 **harness 呼叫端**之值。
  ② `②-宗 圍堵閘` 於某街廓 `raise` 時，本探針之 spy **記錄該例外並回傳 `[]`**，
     使迴圈得續行至其後之街廓（否則 `R4`／`R5`／`R6` 一筆不產生·`GB-118`）。
     🛑 該吞例外**僅於 spy 內**、⛔ 不改 `app.py` 一字；受影響之街廓於報表標 `RAISE`。
"""
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


def main():
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    head = git1(["rev-parse", "HEAD"])
    blob = git1(["rev-parse", "HEAD:app.py"])
    say("=" * 100)
    say("【W-G.9-172 M-A】抵費地池面積之逐街廓量測（⛔ 只讀）")
    say("=" * 100)
    say("  HEAD = %s" % head)
    say("  app.py blob = %s" % blob)

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    raw = open(rv.V6DXF, "rb").read()
    temp, build, _sw = build_build_parcels(ns, fake_st, raw, list(cb_by.values()),
                                           snapshot)
    say("  harvest stats = %r" % (ns.get("__harvest_stats__"),))
    say("  temp_parcels = %d ／ build_parcels = %d" % (len(temp), len(build)))

    out = {"head": head, "blob": blob, "by_tag": {}}
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        diag, sel, off, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp, build,
            setback, snapshot=snapshot)

        rec = []
        orig = ns["_pool_strips_for_block"]

        def spy(*a, **k):
            lbl = k.get("_label", "")
            if not lbl and len(a) >= 6:
                lbl = a[5]
            try:
                res = orig(*a, **k)
            except Exception as e:                                # noqa: BLE001
                rec.append({"街廓": str(lbl), "狀態": "RAISE",
                            "例外": repr(e)[:220], "池片": [], "Σ池": None})
                return []
            rec.append({"街廓": str(lbl), "狀態": "OK", "例外": None,
                        "池片": [float(g.area) for g in res],
                        "Σ池": float(sum(g.area for g in res))})
            return res

        ns["_pool_strips_for_block"] = spy
        err = None
        try:
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build, winners_state, forced_map, setback)
        except Exception as e:                                    # noqa: BLE001
            err = repr(e)[:300]
        finally:
            ns["_pool_strips_for_block"] = orig

        out["by_tag"][tag] = {"pool": rec, "run_step_g_err": err}
        say()
        say("── 情境 %s ──（run_step_g 期末例外 = %s）" % (tag, err))
        say("   %-6s %-6s %-22s %s" % ("街廓", "狀態", "Σ池（未捨入）", "逐池片面積"))
        for r in rec:
            say("   %-6s %-6s %-22s %s"
                % (r["街廓"], r["狀態"],
                   ("%.9f" % r["Σ池"]) if r["Σ池"] is not None else "—",
                   "  ".join("%.6f" % x for x in r["池片"]) or "—"))
            if r["例外"]:
                say("          例外逐字：%s" % r["例外"])
        say("   ⇒ 本情境之池呼叫 = %d 次／街廓集合 = %s"
            % (len(rec), sorted({r["街廓"] for r in rec})))

    p = os.path.join(OUTDIR, "WG9172_pool_%s.json" % blob[:8])
    with open(p, "w", encoding="utf-8", newline="") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    say()
    say("  證據檔：verify/out/%s" % os.path.basename(p))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    rc = main()
    blob = git1(["rev-parse", "HEAD:app.py"])
    with open(os.path.join(OUTDIR, "probe_WG9172_pool_%s.log" % blob[:8]),
              "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    sys.exit(rc)
