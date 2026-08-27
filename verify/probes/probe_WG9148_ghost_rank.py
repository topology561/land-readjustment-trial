# -*- coding: utf-8 -*-
"""`W-G.9-148` `M-2`／`M-3` 探針：ghost 之屬性表 ＋ **位次後果**（`n − r`）。

只讀。⛔ 不改任何生產碼、⛔ 不改任何函式體。

`M-3` 以**二法並列**（互為自我驗證閘）：
  甲　`K-9-17 三【更正】三` 之**定量律**：`n − r`（`n` ＝ 母體宗數·`r` ＝ ghost 之投影排名）
  乙　**直接對拍**：`PO(BASE)` vs `PO(BASE 去 ghost)` 之真實宗地排名逐筆比對
⛔ 二法不一致 ⇒ 出艙「不一致」並停，不得擇一。
"""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # verify/probes
VERIFY = os.path.dirname(HERE)                              # verify
REPO = os.path.dirname(VERIFY)                              # 倉根（⛔ 不寫死絕對路徑）
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "c9bce13"                     # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD）
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
    say("【W-G.9-148 M-2／M-3】ghost 之屬性表與位次後果")
    say("=" * 96)
    say("  HEAD = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob = %s" % git1(["rev-parse", "HEAD:app.py"]))
    say("  情境 = 0m ／ WV_K6_STEP0 = %s" % os.environ.get("WV_K6_STEP0", "on(預設)"))
    say("")

    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    PO = ns["_projection_order"]
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    say("  ✅ build_build_parcels 完成：temp=%d 宗／build=%d 宗" % (len(temp), len(build)))

    # ── 量測器自檢：ghost 於 build 中確實存在（否則後續全 0 係假綠）──
    gh_all = [t for t in build if t.get("_is_ghost_sliver")]
    say("  🔒 量測器自檢①　`build` 中 `_is_ghost_sliver` 之筆數 = **%d**（須 > 0）" % len(gh_all))
    if not gh_all:
        say("  🛑 零 ghost ⇒ 本次量測無受詞，⛔ 結論不得出艙")
        return 1

    # ═════════ M-2 ═════════
    say("")
    say("=" * 96)
    say("§M-2　ghost 列之屬性表（逐列）")
    say("=" * 96)
    say("  %-16s %-10s %-12s %-10s %-10s %-10s %s" %
        ("暫編地號", "原地號", "所有權人", "幾何面積", "面積_m2", "_ghost_area", "配地階段"))
    for t in gh_all:
        own = t.get("所有權人", t.get("所有權統一編號", "<無該鍵>"))
        say("  %-16s %-10s %-12s %-10s %-10s %-10s %s" % (
            t.get("暫編地號"), t.get("原地號"), own,
            t.get("幾何面積_m2"), t.get("面積_m2"),
            t.get("_ghost_area_m2"), t.get("配地階段", "<無該鍵>")))
    say("")
    say("  🔒 ghost 列之全部鍵（首列）：%s" % sorted(gh_all[0].keys()))
    say("  🔒 `重劃前地價區段` = %r／`_ghost_reason` = %r" %
        (gh_all[0].get("重劃前地價區段"), gh_all[0].get("_ghost_reason")))

    # ── 量測器自檢②：二種 ghost 識別法之集合是否相同 ──
    say("")
    g_flag = {t.get("暫編地號") for t in build if t.get("_is_ghost_sliver")}
    g_name = {t.get("暫編地號") for t in build
              if str(t.get("暫編地號", "")).startswith("_GHOST_")}
    say("  \U0001F512 量測器自檢②　ghost 二識別法之集合："
        "`_is_ghost_sliver` = %s ／ 名稱前綴 = %s ⇒ **%s**"
        % (sorted(g_flag), sorted(g_name),
           "相同" if g_flag == g_name else "*** 相異 ***"))
    say("      \u26A0\uFE0F `K-9-19 一` 明訂判準 ⛔ 不綁名稱、⛔ 不綁 `_is_ghost_sliver`"
        "（於 `g_row` 層恆假）⇒ 本探針所用二法皆 ⛔ 非正典判準；"
        "惟於本層（`build_parcels`）二者同集合。")
    t_flag = [t for t in temp if t.get("_is_ghost_sliver")]
    say("  \U0001F512 ghost 筆數：`temp_parcels` = **%d** ／ `build_parcels` = **%d**"
        % (len(t_flag), len(gh_all)))
    say("      （`K-9-19 四` 載「全部 ghost **8** 筆」⇒ 差額在非可建築街廓）")
    for t in t_flag:
        say("        %-16s 所屬街廓=%-6s _ghost_area_m2=%s"
            % (t.get("暫編地號"), t.get("所屬街廓"), t.get("_ghost_area_m2")))
    say("  \U0001F512 對 `K-9-19 四` 之交叉驗證：面積集合 = %s"
        % sorted((t.get("_ghost_area_m2") for t in t_flag), reverse=True))
    say("      正典 `K-9-19 四` 逐字 = [10.78, 8.09, 5.28, 1.34, 1.33, 1.07, 0.75, 0.45]")

    # ═════════ M-3 ═════════
    say("")
    say("=" * 96)
    say("§M-3　位次後果（甲＝定量律 `n − r`／乙＝直接對拍·⛔ 二法須一致）")
    say("=" * 96)
    by_blk = collections.OrderedDict()
    for t in build:
        by_blk.setdefault(t.get("所屬街廓"), []).append(t)

    tot_bad = 0
    agree = disagree = 0
    for blk in sorted(by_blk):
        BASE = by_blk[blk]
        fl = (cad.get("front_lines") or {}).get(blk) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        if p1 is None or p2 is None:
            say("  ── %-6s ⛔ 無 FRONT_LINE ⇒ 跳過（具名·⛔ 非靜默）" % blk)
            continue
        seq_all = [t.get("暫編地號") for t in PO(BASE, p1, p2)]
        n = len(seq_all)
        gh = [x for x in seq_all if str(x).startswith("_GHOST_")]
        say("")
        say("  ── 街廓 %s ── n = %d" % (blk, n))
        if not gh:
            say("     ghost：**無** ⇒ `r` = 無、`n − r` = 0")
            continue
        for g in gh:
            r = seq_all.index(g) + 1
            say("     ghost `%s`：r = **%d**／n = **%d** ⇒ 甲法 `n − r` = **%d**"
                % (g, r, n, n - r))
        # 乙法：直接對拍
        BASE2 = [t for t in BASE if not str(t.get("暫編地號", "")).startswith("_GHOST_")]
        seq_no = [t.get("暫編地號") for t in PO(BASE2, p1, p2)]
        rank_all = {x: i + 1 for i, x in enumerate(seq_all)}
        rank_no = {x: i + 1 for i, x in enumerate(seq_no)}
        changed = [(x, rank_all[x], rank_no[x]) for x in seq_no
                   if rank_all[x] != rank_no[x]]
        say("     乙法 直接對拍：真實宗地 %d 筆，**位次改變 %d 筆**" % (len(seq_no), len(changed)))
        for x, a, b in changed:
            say("        `%s`  含ghost位次 %d → 去ghost位次 %d" % (x, a, b))
        pred = sum(n - (seq_all.index(g) + 1) for g in gh)
        ok = (pred == len(changed))
        agree += ok
        disagree += (not ok)
        say("     🔒 二法一致？ 甲 = %d／乙 = %d ⇒ **%s**"
            % (pred, len(changed), "一致" if ok else "*** 不一致 ***"))
        tot_bad += len(changed)

    say("")
    say("=" * 96)
    say("§M-3 判讀")
    say("=" * 96)
    say("  二法一致之街廓 = %d／不一致 = %d" % (agree, disagree))
    say("  🔴 **全區受影響之真實宗數合計 = %d**" % tot_bad)
    if tot_bad == 0:
        say("  ⇒ 全部街廓 `n − r = 0`（或無 ghost）⇒ ghost 之去留 **⛔ 無位次後果**")
    else:
        say("  ⇒ 至少一街廓 `n − r > 0` ⇒ **有土地後果** ⇒ 須續辦 `M-3b`")

    # ═════════ M-3b ═════════
    say("")
    say("=" * 96)
    say("§M-3b　二態之投影序逐位並列（僅 ghost 街廓）")
    say("=" * 96)
    for blk in sorted(by_blk):
        BASE = by_blk[blk]
        if not any(str(t.get('暫編地號','')).startswith('_GHOST_') for t in BASE):
            continue
        fl = (cad.get('front_lines') or {}).get(blk) or {}
        p1, p2 = fl.get('p1'), fl.get('p2')
        sa = [t.get('暫編地號') for t in PO(BASE, p1, p2)]
        BASE2 = [t for t in BASE if not str(t.get('暫編地號','')).startswith('_GHOST_')]
        sb = [t.get('暫編地號') for t in PO(BASE2, p1, p2)]
        say('')
        say('  ── 街廓 %s ──' % blk)
        say('     含 ghost （n=%d）：%s' % (len(sa), sa))
        say('     去 ghost （n=%d）：%s' % (len(sb), sb))
        say('     第 1 位：含=%r／去=%r ⇒ **%s**'
            % (sa[0], sb[0], '相同' if sa[0] == sb[0] else '相異'))
        say('     第 2 位（「下一位」）：含=%r／去=%r ⇒ **%s**'
            % (sa[1] if len(sa) > 1 else None, sb[1] if len(sb) > 1 else None,
               '相同' if (len(sa) > 1 and len(sb) > 1 and sa[1] == sb[1]) else '相異'))

    out = os.path.join(OUTDIR, "probe_WG9148_ghost_rank_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    say("")
    say("log ⇒ %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
