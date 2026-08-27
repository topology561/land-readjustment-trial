# -*- coding: utf-8 -*-
"""`W-G.9-149` 補測：`_projection_order` 之輸出是否 **stage-dependent**。

受詞：`W-G.9-148R` `M-3` 於 `build_build_parcels` **之後、`run_corner_pk` 之前**量得
`R1` 之 ghost 排名 `r = 2`；`W-G.9-149` `R-7` 探針於 `run_corner_pk` **之後**量得 `r = 6`（末位）。
二者輸入宗地集合相同 ⇒ 差異必在**幾何**或 **front_line**。本探針以同一次執行**逐階段**量之。

只讀。⛔ 不改任何生產碼。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "f71c147"
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s)
    L.append(s)


def snap(build, blk):
    """該街廓之 (暫編地號 -> polygon_coords 之 tuple) 快照。"""
    return {t["暫編地號"]: tuple(map(tuple, (t.get("polygon_coords") or [])))
            for t in build if t.get("所屬街廓") == blk}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    import subprocess
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                          capture_output=True, check=True).stdout.decode().strip()
    say("=" * 96)
    say("【W-G.9-149 補測】`_projection_order` 之 stage 相依性")
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

    BLKS = ["R1", "R4"]

    def measure(tag):
        say("")
        say("  ── 階段：%s ──" % tag)
        out = {}
        for blk in BLKS:
            fl = (cad.get("front_lines") or {}).get(blk) or {}
            pib = [t for t in build if t.get("所屬街廓") == blk]
            seq = [t["暫編地號"] for t in PO(pib, fl.get("p1"), fl.get("p2"))]
            gh = [x for x in seq if str(x).startswith("_GHOST_")]
            r = seq.index(gh[0]) + 1 if gh else None
            n = len(seq)
            say("     %-4s n=%-3d ghost r=%-4s n-r=%-4s" % (
                blk, n, r if r else "無", (n - r) if r else 0))
            say("        序 = %s" % seq)
            out[blk] = (seq, snap(build, blk), fl.get("p1"), fl.get("p2"))
        return out

    before = measure("A：build_build_parcels 之後（＝ W-G.9-148R M-3 之量測點）")

    _d, _s, _o, winners_state, forced_map = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, 0.0,
        snapshot=snapshot)

    after = measure("B：run_corner_pk 之後（＝ W-G.9-149 R-7 探針之量測點）")

    say("")
    say("=" * 96)
    say("§差異之歸因（⛔ 不臆測·逐項實測）")
    say("=" * 96)
    for blk in BLKS:
        sa, ga, p1a, p2a = before[blk]
        sb, gb, p1b, p2b = after[blk]
        say("")
        say("  ── %s ──" % blk)
        say("     序 A == 序 B ？ **%s**" % (sa == sb))
        say("     front_line p1 A==B ? %s ／ p2 A==B ? %s"
            % (p1a == p1b, p2a == p2b))
        keys = sorted(set(ga) | set(gb))
        chg = [k for k in keys if ga.get(k) != gb.get(k)]
        say("     polygon_coords **改變之宗 ＝ %d/%d**：%s" % (len(chg), len(keys), chg))
        for k in chg:
            say("        %-16s 頂點數 %s → %s" % (
                k, len(ga.get(k, ())), len(gb.get(k, ()))))

    # ── R-7：正典 K-6:3294 之 `R1右 → 628-36(1)` 於二態下之鑑別力 ──
    say("")
    say("=" * 96)
    say("§R-7　正典遞補格 `R1右 → 628-36(1)` 對「母體含不含 ghost」之鑑別力")
    say("=" * 96)
    TARGET = "628-34(3)"          # K-9-23-a 所載 R1右 之第 1 宗
    EXPECT = "628-36(1)"          # K-6:3294 所載之遞補宗
    fl = (cad.get("front_lines") or {}).get("R1") or {}
    for tag, sel in (("含 ghost", lambda t: True),
                     ("去 ghost", lambda t: not t.get("_is_ghost_sliver"))):
        pib = [t for t in build if t.get("所屬街廓") == "R1" and sel(t)]
        seq = [t["暫編地號"] for t in PO(pib, fl.get("p1"), fl.get("p2"))]
        i = seq.index(TARGET)
        nxt = seq[i + 1] if i + 1 < len(seq) else None      # 順投影序之下一位
        prv = seq[i - 1] if i - 1 >= 0 else None            # 逆投影序之下一位
        say("")
        say("  ── %s（n=%d）──" % (tag, len(seq)))
        say("     序 = %s" % seq)
        say("     `%s` 之索引 = %d" % (TARGET, i))
        say("     順投影序之下一位 = %r  ⇒ 重現正典 %r ？ **%s**"
            % (nxt, EXPECT, nxt == EXPECT))
        say("     逆投影序之下一位 = %r  ⇒ 重現正典 %r ？ **%s**"
            % (prv, EXPECT, prv == EXPECT))
    say("")
    say("  🔒 判：若二態之同一方向皆重現 `%s` ⇒ 該格對「母體含不含 ghost」**⛔ 無鑑別力**" % EXPECT)
    say("     ⇒ 正典八格表**⛔ 未編碼讀法甲**，亦**⛔ 不與 `W-G.9-148R` 互斥**。")

    out = os.path.join(OUTDIR, "probe_WG9149_stage_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    say("")
    say("log ⇒ %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
