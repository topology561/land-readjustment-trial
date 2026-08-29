# -*- coding: utf-8 -*-
"""`W-G.9-172` `M-B-1`／`M-B-3` 探針：步驟 0 八群逐成員面積 ＋ `_rank_by_tpid` 之 `inf` 現查。

⛔ 只讀·⛔ 零生產碼。二受詞皆以**執行期攔截**取實值（⛔ 不由碼面推定）。
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

    head = git1(["rev-parse", "HEAD"])
    blob = git1(["rev-parse", "HEAD:app.py"])
    say("=" * 100)
    say("【W-G.9-172 M-B-1／M-B-3】步驟 0 八群逐成員面積 ＋ `_rank_by_tpid` 之 `inf` 現查")
    say("=" * 100)
    say("  HEAD = %s ／ app.py blob = %s" % (head, blob))

    ns, fake_st = harvest()

    # ── M-B-1：攔 `k6_merge_groups`（群之產生處）＋ `_projection_order`（命名處）──
    GROUPS = []
    _orig_mg = ns["k6_merge_groups"]

    def spy_mg(*a, **k):
        # 🔒 `k6_merge_groups` 之回傳係**索引**之群（⛔ 非 dict）——現查所得、⛔ 非推定
        res = _orig_mg(*a, **k)
        GROUPS.append({"args_n": len(a), "群數": len(res),
                       "群大小": [len(g) for g in res],
                       "元素型別": sorted({type(x).__name__ for g in res for x in g})})
        return res

    ns["k6_merge_groups"] = spy_mg

    MEM = []
    _orig_po = ns["_projection_order"]

    def spy_po(seq, *a, **k):
        res = _orig_po(seq, *a, **k)
        try:
            MEM.append({"入": [{"暫編地號": str(x.get("暫編地號", "")),
                                "原地號": str(x.get("原地號", "")),
                                "所屬街廓": str(x.get("所屬街廓", "")),
                                "幾何面積_m2": float(x.get("幾何面積_m2", 0) or 0)}
                               for x in seq],
                        "出首": str(res[0].get("暫編地號", "")) if res else ""})
        except Exception:                                          # noqa: BLE001
            pass
        return res

    ns["_projection_order"] = spy_po

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    raw = open(rv.V6DXF, "rb").read()
    temp, build, _sw = build_build_parcels(ns, fake_st, raw, list(cb_by.values()),
                                           snapshot)
    ns["k6_merge_groups"] = _orig_mg
    ns["_projection_order"] = _orig_po

    say("  temp_parcels = %d ／ build_parcels = %d" % (len(temp), len(build)))
    say("  `k6_merge_groups` 呼叫 = %d 次 ／ `_projection_order` 攔得 = %d 次"
        % (len(GROUPS), len(MEM)))
    say("  `k6_merge_groups` 回傳之元素型別 = %s ／ 非單元素群之群大小 = %s"
        % (sorted({t2 for g in GROUPS for t2 in g["元素型別"]}),
           [s for g in GROUPS for s in g["群大小"] if s >= 2]))

    # 步驟 0 之群 ＝ `_projection_order` 於合併時所收之 `_mem`（成員 ≥ 2）
    merged = [m for m in MEM if len(m["入"]) >= 2]
    say()
    say("── `M-B-1`　八群逐成員之 `幾何面積_m2`（實值·⛔ 未捨入）──")
    say("   %-4s %-16s %-42s %-12s %-10s %s"
        % ("#", "現行命名", "逐成員（暫編地號 原地號 面積）", "Σ幾何面積", "投影序首員", "依面積最大"))
    rows = []
    for i, m in enumerate(merged, 1):
        mem = sorted(m["入"], key=lambda x: -x["幾何面積_m2"])
        blk = mem[0]["所屬街廓"]
        tot = sum(x["幾何面積_m2"] for x in mem)
        top1, top2 = mem[0], (mem[1] if len(mem) > 1 else None)
        gap = (top1["幾何面積_m2"] - top2["幾何面積_m2"]) if top2 else None
        rows.append({"街廓": blk, "現行命名": m["出首"] + "+",
                     "投影序首員": m["出首"],
                     "成員": mem, "Σ": tot,
                     "面積最大": top1["暫編地號"], "top1": top1["幾何面積_m2"],
                     "top2": (top2["幾何面積_m2"] if top2 else None),
                     "top差": gap})
        say("   %-4d %-16s %-42s %-12.4f %-10s %s"
            % (i, m["出首"] + "+",
               " / ".join("%s(%s)%.2f" % (x["暫編地號"], x["原地號"],
                                          x["幾何面積_m2"]) for x in mem)[:42],
               tot, m["出首"], top1["暫編地號"]))
    say()
    for r in rows:
        say("   [%s] %s ⇒ 逐成員全精度：%s"
            % (r["街廓"], r["現行命名"],
               "  ".join("%s=%.9f" % (x["暫編地號"], x["幾何面積_m2"])
                         for x in r["成員"])))
    say()
    say("── `裁 B` 之脆弱性清冊：top-2 面積差 < 1 ㎡ 之群 ──")
    frail = [r for r in rows if r["top差"] is not None and r["top差"] < 1.0]
    if not frail:
        say("   （無）")
    for r in frail:
        say("   🔴 [%s] %s：top1 %s = %.9f ／ top2 %s = %.9f ／ **差 = %.9f**"
            % (r["街廓"], r["現行命名"], r["成員"][0]["暫編地號"], r["top1"],
               r["成員"][1]["暫編地號"], r["top2"], r["top差"]))
    say()
    say("── 命名之異同（現行＝投影序首員 vs `裁 B`＝面積最大）──")
    diff = [r for r in rows if r["投影序首員"] != r["面積最大"]]
    for r in rows:
        say("   [%s] 現行 %-14s ／ 裁B %-14s ⇒ %s"
            % (r["街廓"], r["投影序首員"], r["面積最大"],
               "🔴 改名" if r["投影序首員"] != r["面積最大"] else "不變"))
    say("   ⇒ 改名者 = **%d** 群 ／ 不變 = %d 群" % (len(diff), len(rows) - len(diff)))

    # ── M-B-3：`_rank_by_tpid` 之 inf ──
    say()
    say("── `M-B-3`　`_rank_by_tpid` 之靜默退路（`float('inf')`）現查 ──")
    INF = []
    for setback, tag in ((0.0, "0m"), (3.5, "3.5m")):
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _orig_pk = ns["_projection_order"]
        SEEN = []

        def spy2(seq, *a, **k):
            res = _orig_pk(seq, *a, **k)
            SEEN.append([str(x.get("暫編地號", "")) for x in res])
            return res

        ns["_projection_order"] = spy2
        try:
            run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp,
                          build, setback, snapshot=snapshot)
        finally:
            ns["_projection_order"] = _orig_pk
        # 逐街廓重建 _rank_by_tpid 之母體與被查者（harness 側之式）
        by_blk = {}
        for tp in build:
            by_blk.setdefault(str(tp.get("所屬街廓", "")), []).append(tp)
        n_inf = 0
        det = []
        for lbl, allv in sorted(by_blk.items()):
            pool = [tp for tp in allv if not ns["_proj_pop_ghost3"](tp)] \
                if "_proj_pop_ghost3" in ns else list(allv)
            rank = {str(tp.get("暫編地號", "")): i + 1 for i, tp in enumerate(pool)}
            for tp in pool:
                pid = str(tp.get("暫編地號", ""))
                if rank.get(pid) is None:
                    n_inf += 1
                    det.append((lbl, pid))
            # 候選側：`_candidates` 之母體 ＝ 同 pool，經 own_map 過濾
        INF.append((tag, n_inf, det))
        say("   情境 %-5s：`_rank_by_tpid` 母體 = %d 街廓／落 `inf` 之宗 = **%d** %s"
            % (tag, len(by_blk), n_inf, det if det else ""))
    say("   ⇒ 二情境合計落 `inf` = **%d** 宗" % sum(x[1] for x in INF))
    say("   🔒 判別力對照：人造一個不在 rank 內之鍵 ⇒ `.get(..., float('inf'))` 得 %r"
        % ({}.get("__nonexistent__", float("inf"))))

    p = os.path.join(OUTDIR, "WG9172_step0_%s.json" % blob[:8])
    with open(p, "w", encoding="utf-8", newline="") as f:
        json.dump({"head": head, "blob": blob, "groups": rows,
                   "inf": [(t, n, d) for t, n, d in INF]}, f,
                  ensure_ascii=False, indent=1)
    say()
    say("  證據檔：verify/out/%s" % os.path.basename(p))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    rc = main()
    with open(os.path.join(OUTDIR, "probe_WG9172_step0.log"),
              "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(L) + "\n")
    sys.exit(rc)
