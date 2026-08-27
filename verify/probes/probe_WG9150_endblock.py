# -*- coding: utf-8 -*-
"""`W-G.9-150′` `3-4`／`3-5` 探針：`R4` 之「⛔ 無第 1 宗」成因 ＋ 左側跳號。

`T-1` 逐側母體／winner；`T-2` `R4` 之 SIDELINE 條數；`T-3` 與 ghost 之關聯（二態並列）。
只讀。⛔ 不改任何生產碼。
"""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "8bdb3e3"
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s)
    L.append(s)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    import subprocess
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                          capture_output=True, check=True).stdout.decode().strip()
    say("=" * 96)
    say("【W-G.9-150′ 3-4／3-5】R4 之「無第 1 宗」成因 ＋ SIDELINE 現查")
    say("=" * 96)
    say("  HEAD = %s" % head)
    say("  情境 = 0m ／ WV_K6_STEP0 = %s" % os.environ.get("WV_K6_STEP0", "on(預設)"))

    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    PO = ns["_projection_order"]
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

    # ── T-2：SIDELINE 之現查（全街廓·⛔ 只 R4 會誤讀為特例）──
    say("")
    say("=" * 96)
    say("§T-2　各街廓之 SIDELINE 條數（判是否為末端塊街廓）")
    say("=" * 96)
    sl = cad.get("side_lines_by_side") or {}
    say("  cad['side_lines_by_side'] 之鍵 = %s" % sorted(sl.keys()))
    for blk in sorted(sl):
        d = sl[blk] or {}
        present = {k: (v is not None and v != {} and v != []) for k, v in d.items()}
        say("     %-6s 側別鍵 = %-24s 有值者 = %s"
            % (blk, sorted(d.keys()), sorted(k for k, v in present.items() if v)))
    slen = cad.get("side_lengths_by_side") or {}
    say("")
    say("  cad['side_lengths_by_side']（長度·0 或缺 ⇒ 該側無 SIDELINE）：")
    for blk in sorted(slen):
        say("     %-6s %s" % (blk, slen[blk]))

    # ── T-1／T-3：R4 之母體與 winner ──
    say("")
    say("=" * 96)
    say("§T-1／T-3　R4 之母體、winner、與 ghost 二態")
    say("=" * 96)
    for blk in ("R4", "R1"):
        fl = (cad.get("front_lines") or {}).get(blk) or {}
        say("")
        say("  ── 街廓 %s ──" % blk)
        say("     winners_state[%s] = %r" % (blk, (winners_state or {}).get(blk)))
        for tag, sel in (("含 ghost", lambda t: True),
                         ("去 ghost", lambda t: not t.get("_is_ghost_sliver"))):
            pib = [t for t in build if t.get("所屬街廓") == blk and sel(t)]
            seq = [t["暫編地號"] for t in PO(pib, fl.get("p1"), fl.get("p2"))]
            say("     %s  n=%-3d 序 = %s" % (tag, len(seq), seq))
    say("")
    say("  🔒 `K-9-23-a` 載 `R4左`／`R4右` 皆「⛔ 無第 1 宗」——本探針以母體宗數判：")
    n4 = len([t for t in build if t.get("所屬街廓") == "R4"
              and not t.get("_is_ghost_sliver")])
    say("     R4 之**真實宗**（去 ghost）＝ **%d** 宗" % n4)
    say("     ⇒ 若二側各需 winner（第 0 宗）＋ 第 1 宗 ＝ 4 宗，而實有 %d 宗" % n4)

    # ── 3-4：左側跳號 ──
    say("")
    say("=" * 96)
    say("§3-4　左側三組跳號之現查（R2左[2,4,5]／R5左[1,2,5]／R6左[1,2,4]）")
    say("=" * 96)
    say("  🛑 本項之受詞（「組」與「跳號」之定義）源自 `K-9-14 四`（`2026-08-20` 前窗），")
    say("     其**機制⛔ 未實證**（`K-9-14 四` 自陳）。本探針只報可自倉內取得之量：")
    for blk in ("R2", "R5", "R6"):
        fl = (cad.get("front_lines") or {}).get(blk) or {}
        pib = [t for t in build if t.get("所屬街廓") == blk
               and not t.get("_is_ghost_sliver")]
        seq = [t["暫編地號"] for t in PO(pib, fl.get("p1"), fl.get("p2"))]
        say("     %-4s n=%-3d 投影序 = %s" % (blk, len(seq), seq))
    say("")
    say("  ⛔ **未能判定**：「組」之切分規則於碼面**無具名實作**（`組首`／`組末`／`起算端` 於")
    say("     `app.py` ＋ `verify/**/*.py` 之命中皆 `0`·對照組 `_block_strip` ＝ 98）")
    say("     ⇒ 只讀下**無法**自倉內重建該三組之成員與其編號 ⇒ 依單 `3-4` 報「⛔ 未能判定」。")

    out = os.path.join(OUTDIR, "probe_WG9150_endblock_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    say("")
    say("log ⇒ %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
