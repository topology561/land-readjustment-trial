# -*- coding: utf-8 -*-
"""`W-G.9-149` `N-2` ＋ `R-7` 探針。

`N-2`：五份實作（`wf_f0`／`f2`／`f3`／`f4` 之 `_proj_order` ＋ `app._projection_order` 直呼）
       於**同一輸入**之輸出序列對拍；併跑**判別力對照**（注入反轉比較子）。
`R-7`：`W-G.9-142` 之遞補鏈模擬所用母體不可自倉內現查（其報告與探針⛔ 不在倉）
       ⇒ **改以重導**：對 `R1` 之含／去 ghost 二態，各求 `ordered_v2` 之右側序列，
       判其「第 1 宗之下一位」何者重現正典 `K-6:3294` 所載之 `R1右 → 628-36(1)`。

只讀。⛔ 不改任何生產碼。
"""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # verify/probes
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "f71c147"                     # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD）
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
    sys.stdout.reconfigure(encoding="utf-8")
    say("=" * 96)
    say("【W-G.9-149 N-2／R-7】五份 _proj_order 之等價性 ＋ 遞補鏈母體之重導")
    say("=" * 96)
    say("  HEAD = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob = %s" % git1(["rev-parse", "HEAD:app.py"]))
    say("  情境 = 0m ／ WV_K6_STEP0 = %s" % os.environ.get("WV_K6_STEP0", "on(預設)"))
    say("")

    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    import wf_f0, wf_f2, wf_f3, wf_f4

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    PO = ns["_projection_order"]
    SOP2 = ns["_spatial_order_parcels_v2"]
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    _d, _s, _o, winners_state, forced_map = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, 0.0,
        snapshot=snapshot)
    say("  ✅ 管線至 run_corner_pk 完成：build=%d 宗" % len(build))

    blocks = sorted({t.get("所屬街廓") for t in build})
    say("  街廓母體 = %s" % blocks)

    # ═════════ N-2 ═════════
    say("")
    say("=" * 96)
    say("§N-2　五份實作於同一輸入之輸出對拍")
    say("=" * 96)
    IMPLS = [("wf_f0._proj_order", wf_f0._proj_order),
             ("wf_f2._proj_order", wf_f2._proj_order),
             ("wf_f3._proj_order", wf_f3._proj_order),
             ("wf_f4._proj_order", wf_f4._proj_order)]

    def direct(nsx, cadx, parcels, blk):
        """第 5 份：直呼 app._projection_order（母體同乙類之濾式）。"""
        fl = (cadx.get("front_lines") or {}).get(blk) or {}
        pib = [tp for tp in parcels if tp["所屬街廓"] == blk
               and not tp.get("_is_ghost_sliver")]
        return [tp["暫編地號"] for tp in
                nsx["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]

    IMPLS.append(("app._projection_order(直呼)", direct))

    n_same = n_tot = 0
    for blk in blocks:
        outs = [(nm, fn(ns, cad, build, blk)) for nm, fn in IMPLS]
        base = outs[0][1]
        ok = all(o == base for _, o in outs)
        n_tot += 1
        n_same += ok
        say("  %-6s n=%-3d 五份 ⇒ **%s**" % (blk, len(base),
                                            "逐位相同" if ok else "*** 相異 ***"))
        if not ok:
            for nm, o in outs:
                say("     %-28s %s" % (nm, o))
    say("")
    say("  🔒 **%d/%d 街廓 五份逐位相同**" % (n_same, n_tot))

    # 判別力對照：注入反轉比較子
    say("")
    say("  ── 判別力對照（注入必然改序之擾動·戒 12）──")
    orig_po = ns["_projection_order"]

    def reversed_po(parcels, p1, p2):
        return list(reversed(orig_po(parcels, p1, p2)))

    ns["_projection_order"] = reversed_po
    try:
        n_red = 0
        for blk in blocks:
            outs = [(nm, fn(ns, cad, build, blk)) for nm, fn in IMPLS]
            base_now = outs[0][1]
            base_before = [t["暫編地號"] for t in orig_po(
                [tp for tp in build if tp["所屬街廓"] == blk
                 and not tp.get("_is_ghost_sliver")],
                (cad.get("front_lines") or {}).get(blk, {}).get("p1"),
                (cad.get("front_lines") or {}).get(blk, {}).get("p2"))]
            if base_now != base_before and len(base_now) > 1:
                n_red += 1
        say("  🔒 注入反轉後**轉紅之街廓 ＝ %d/%d**（須 ≥ 1 ⇒ 本對拍有判別力）" % (n_red, n_tot))
    finally:
        ns["_projection_order"] = orig_po

    # ═════════ R-7 ═════════
    say("")
    say("=" * 96)
    say("§R-7　遞補鏈母體之重導（正典 K-6:3294 載 `R1右 → 628-36(1)`）")
    say("=" * 96)
    blk = "R1"
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pk = (winners_state or {}).get(blk) or {}
    say("  pk_winners[%s] 之鍵 = %s" % (blk, sorted(pk.keys()) if isinstance(pk, dict) else type(pk).__name__))
    for tag, sel in (("含 ghost", lambda t: True),
                     ("去 ghost", lambda t: not t.get("_is_ghost_sliver"))):
        pib = [t for t in build if t["所屬街廓"] == blk and sel(t)]
        try:
            res = SOP2(pib, fl.get("p1"), fl.get("p2"),
                       pk_winners=pk, forced_offset=(forced_map or {}).get(blk))
        except TypeError:
            res = SOP2(pib, fl.get("p1"), fl.get("p2"), pk)
        od = res.get("ordered") or []
        say("")
        say("  ── %s（n=%d）──" % (tag, len(pib)))
        for e in od:
            say("     side=%-4s pre_position=%-3s %s"
                % (e.get("side"), e.get("pre_position"),
                   (e.get("tp") or {}).get("暫編地號")))
        for sd in ("右", "左"):
            seq = [(e.get("tp") or {}).get("暫編地號") for e in od
                   if str(e.get("side", "")).startswith(sd)]
            say("     %s側序列 = %s" % (sd, seq))

    out = os.path.join(OUTDIR, "probe_WG9149_projorder_equiv_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    say("")
    say("log ⇒ %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
