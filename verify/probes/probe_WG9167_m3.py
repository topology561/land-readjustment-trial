# -*- coding: utf-8 -*-
"""`W-G.9-167` `M-3` 補測：逐 filter 之 ghost 殘留 ＋ `無串聯` 閘之 `skip_cols` 是否失效（⛔ 只讀）"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "6b77b4a"
sys.path.insert(0, VERIFY)
L = []


def say(s=""):
    print(s)
    L.append(s)


def ghost3(tp):
    return (str(tp.get("原地號", "")) == "_GHOST"
            and float(tp.get("G(㎡)", 0) or 0) == 0.0
            and float(tp.get("a 面積(㎡)", 0) or 0) == 0.0)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _ = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    say("=" * 100)
    say("【W-G.9-167 M-3 補測】逐 filter 之 ghost 殘留（⛔ 只讀）")
    say("=" * 100)
    F = ns["_proj_pop_filter"]
    for fname in ("identity", "stage1", "no_ghost", "passthrough", "pseudo_of", "group_members"):
        for lname, layer in (("BUILD_LAYER", build), ("TEMP_LAYER", temp)):
            try:
                out = F(fname, layer)
            except Exception as e:                                   # noqa: BLE001
                say("  %-14s %-12s ⇒ **raise**：%s" % (fname, lname, type(e).__name__))
                say("       逐字：%s" % str(e)[:96])
                break
            g = [t for t in out if ghost3(t)]
            say("  %-14s %-12s 入 %3d ⇒ 出 %3d ・**殘留 ghost = %d** %s"
                % (fname, lname, len(layer), len(out), len(g),
                   sorted(t.get("暫編地號") for t in g)))
    say("")
    say("  🔒 **對照組**（必然非零）：`identity(BUILD_LAYER)` 之出列數 = %d" % len(F("identity", build)))
    say("  🔒 `_proj_pop_filter` 之**已實作**濾式 ＝ `identity`／`stage1`／`no_ghost`（其餘 raise）")
    say("     ⇒ `passthrough`／`pseudo_of`／`group_members` 由**他支斷言器**承載"
        "（`grep -n \"def _proj_pop_assert\" app.py`）")

    say("")
    say("=" * 100)
    say("【X-4 覆核】`無串聯` 閘之 `skip_cols` 是否對 `原位次` 失效")
    say("=" * 100)
    say("  `verify/run_verification.py:616` 逐字：skip_cols={\"原位次(距角序·暫行)\", \"G估(㎡)\"}")
    for p in ("verify/baselines/W-D.1.2 診斷_退縮0m.csv",
              "verify/baselines/W-D.1.2 診斷_退縮3.5m.csv",
              "verify/baselines/v3/W-D.1.2 診斷_退縮0m.csv",
              "verify/baselines/v3/W-D.1.2 診斷_退縮3.5m.csv"):
        h = io.open(os.path.join(REPO, p), encoding="utf-8-sig", newline="").readline().strip()
        cols = h.split(",")
        say("  %-52s 舊名『原位次(距角序·暫行)』在欄集 = **%s**／新名『原位次(投影序)』 = **%s**"
            % (p.split("/")[-2] + "/" + p.split("/")[-1],
               "原位次(距角序·暫行)" in cols, "原位次(投影序)" in cols))
    say("  ⇒ 🔴 `skip_cols` 所列之舊欄名於四檔**命中皆 0**（對照組：新欄名命中皆 True）"
        " ⇒ **該豁免對 `原位次(投影序)` 失效** ⇒ `無串聯` 閘亦會看見本批預測之 4 格差。")

    out = os.path.join(OUTDIR, "probe_WG9167_m3_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("")
    print("log ⇒ %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
