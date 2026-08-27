# -*- coding: utf-8 -*-
"""`W-G.9-147`【甲】 `V-3` 探針：`_projection_order` 各呼叫點之**第一實參母體**實測對拍。

只讀。⛔ 不改任何函式體——僅以 wrapper 包住 `ns["_projection_order"]` 並記錄
（呼叫端 `檔:行`、第一實參之 `暫編地號` 序列）。跑畢還原。

情境 `0m`／`STEP0=on`（`WV_K6_STEP0` 預設 `on`）。
"""
import collections
import inspect
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # verify/probes
VERIFY = os.path.dirname(HERE)                              # verify
REPO = os.path.dirname(VERIFY)                              # 倉根（⛔ 不寫死絕對路徑）
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "e9ad898"                    # 🔒 基座（log 檔名綁此·⛔ 不綁 HEAD·考古節 122）
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


REC = []          # [(site, seq)]
GUARD = collections.Counter()


def _blk_of(arg):
    """自實參元素之 `所屬街廓` 推得街廓鍵；缺鍵 ⇒ 具名回報（⛔ 不靜默兜底）。"""
    if not isinstance(arg, (list, tuple)) or not arg:
        return "<空或非序列>"
    labs = set()
    for x in arg:
        if isinstance(x, dict) and "所屬街廓" in x:
            labs.add(str(x["所屬街廓"]))
        else:
            labs.add("<無所屬街廓鍵>")
    return "/".join(sorted(labs))


def _tpids(arg):
    """第一實參之暫編地號序列（逐位·含重複·保序）。非 list ⇒ 具名回報。"""
    if not isinstance(arg, (list, tuple)):
        return ["<非序列:%s>" % type(arg).__name__]
    out = []
    for x in arg:
        if isinstance(x, dict):
            out.append(str(x.get("暫編地號", "<無暫編地號鍵>")))
        else:
            out.append("<非dict:%s>" % type(x).__name__)
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    head = git1(["rev-parse", "HEAD"])
    blob = git1(["rev-parse", "HEAD:app.py"])
    say("=" * 96)
    say("【W-G.9-147【甲】 V-3】`_projection_order` 呼叫點之第一實參母體實測")
    say("=" * 96)
    say("  HEAD = %s" % head)
    say("  app.py blob = %s" % blob)
    say("  情境 = 0m ／ WV_K6_STEP0 = %s" % os.environ.get("WV_K6_STEP0", "on(預設)"))
    say("")

    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import (build_ownership, build_build_parcels,
                                    run_corner_pk)
    from stepg_pipeline import run_step_g

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()

    # ── 量測器自檢①：ns 是否即 app 之 module globals（決定能否攔到 app 內部直呼）──
    po = ns["_projection_order"]
    app_globals = getattr(po, "__globals__", None)
    is_same = (app_globals is ns)
    say("  🔒 量測器自檢①　`ns is _projection_order.__globals__` = **%s**" % is_same)
    say("      （True ⇒ 覆寫 `ns[...]` 亦攔得到 `app.py` 內部之直接呼叫）")
    if not is_same:
        say("  🛑 自檢① 為 False ⇒ app 內部直呼**攔不到** ⇒ 本次量測之母體不完整，逐字回報。")

    orig = po

    def wrapped(parcels, p1, p2):
        fr = inspect.stack()[1]
        site = "%s:%d" % (os.path.relpath(fr.filename, REPO).replace("\\", "/"),
                          fr.lineno)
        GUARD[site] += 1
        REC.append((site, _tpids(parcels), _blk_of(parcels)))
        return orig(parcels, p1, p2)

    ns["_projection_order"] = wrapped

    # ── 量測器自檢②：已知必被呼叫之一次（直接呼叫 wrapper 之持有者）──
    n0 = len(REC)
    _ = ns["_projection_order"]([], None, None)
    say("  🔒 量測器自檢②　人造呼叫後 REC 增量 = **%d**（須 1）" % (len(REC) - n0))
    REC.pop()
    GUARD.subtract({list(GUARD)[-1]: 1})

    try:
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        setback = 0.0
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(
            ns, fake_st, v6, list(cb_by.values()), snapshot)
        say("  ✅ build_build_parcels 完成（步驟 0 於此路徑內）")
        _d, _s, _o, winners_state, forced_map = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp, build,
            setback, snapshot=snapshot)
        say("  ✅ run_corner_pk 完成")
        run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                   params, build, winners_state, forced_map, setback)
        say("  ✅ run_step_g 完成")
    except Exception as exc:                                   # noqa: BLE001
        say("  🛑 管線中止：%s: %s" % (type(exc).__name__, exc))
        say("     ⇒ 其後之呼叫點**未被觀測**（⛔ 非「不存在」）")
    finally:
        ns["_projection_order"] = orig

    say("")
    say("=" * 96)
    say("§A　觀測到之呼叫點與呼叫次數")
    say("=" * 96)
    if not GUARD:
        say("  🔴 零觀測 ⇒ 量測器紅或管線未跑 ⇒ ⛔ 結論不得出艙")
    for site, cnt in sorted(GUARD.items()):
        say("  %-46s 呼叫 %d 次" % (site, cnt))

    say("")
    say("=" * 96)
    say("§B　各呼叫點之第一實參母體（去重後之相異序列）")
    say("=" * 96)
    by_site = collections.OrderedDict()
    for site, seq, _b in REC:
        by_site.setdefault(site, []).append(seq)
    for site, seqs in by_site.items():
        uniq = []
        for s in seqs:
            if s not in uniq:
                uniq.append(s)
        say("")
        say("  ── %s ── 呼叫 %d 次／相異序列 %d 個" % (site, len(seqs), len(uniq)))
        for i, s in enumerate(uniq):
            say("     [%d] n=%-3d %s" % (i, len(s), s if len(s) <= 14
                                         else s[:14] + ["…(共%d)" % len(s)]))

    say("")
    say("=" * 96)
    say("§C　兩兩對拍（以各呼叫點之**聯集集合**為受詞·三態）")
    say("=" * 96)
    sets = {site: set(x for s in seqs for x in s) for site, seqs in by_site.items()}
    sites = list(sets)
    for i in range(len(sites)):
        for j in range(i + 1, len(sites)):
            a, b = sites[i], sites[j]
            sa, sb = sets[a], sets[b]
            if sa == sb:
                # 序之比較：取各自首次呼叫之序列
                fa, fb = by_site[a][0], by_site[b][0]
                verdict = "逐位相同" if fa == fb else "集合相同但序不同"
                say("  %-40s vs %-40s ⇒ **%s**" % (a, b, verdict))
            else:
                say("  %-40s vs %-40s ⇒ **集合相異**" % (a, b))
                only_a = sorted(sa - sb)
                only_b = sorted(sb - sa)
                say("       只在前者 (%d)：%s" % (len(only_a), only_a[:12]))
                say("       只在後者 (%d)：%s" % (len(only_b), only_b[:12]))

    say("")
    say("=" * 96)
    say("§D　逐街廓對拍（⭐ 可分辨「真母體差」與「覆蓋差」）")
    say("=" * 96)
    per = {}
    for site, seq, blk in REC:
        per.setdefault(blk, {}).setdefault(site, []).append(seq)
    for blk in sorted(per):
        sset = per[blk]
        say("")
        say("  ── 街廓 %s ── 呼叫點 %d 個" % (blk, len(sset)))
        for site, seqs in sset.items():
            say("     %-42s n=%s" % (site, [len(x) for x in seqs]))
        ks = list(sset)
        for i in range(len(ks)):
            for j in range(i + 1, len(ks)):
                a, b = ks[i], ks[j]
                fa, fb = sset[a][0], sset[b][0]
                if fa == fb:
                    v = "逐位相同"
                elif set(fa) == set(fb):
                    v = "集合相同但序不同"
                else:
                    v = "集合相異"
                say("     %s  vs  %s  ⇒ **%s**" % (a, b, v))
                if v == "集合相異":
                    say("        只在前者：%s" % sorted(set(fa) - set(fb)))
                    say("        只在後者：%s" % sorted(set(fb) - set(fa)))

    out = os.path.join(OUTDIR, "probe_WG9147_projorder_%s.log" % BASE_REF)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    say("")
    say("log ⇒ %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
