# -*- coding: utf-8 -*-
"""`W-G.9-168` `M-A` 探針：`app:k6step0/_ordered` 之補量（⛔ 只讀·⛔ 零生產碼）。

`A-2` 母體逐次記錄（層疊 `ns["_proj_pop_assert_subset"]`）／`A-3` `_name` 逐次記錄／
`A-4` 二態對拍（現況 vs `VR-074` 模擬態·層疊 `ns["_projection_order"]`）／`A-6` 對照組。

🔒 `ghost3` 逐字綁 `K-9-19 一` 之三判準合取；⛔ 不綁 `_is_ghost_sliver`、⛔ 不綁名稱。
🔒 **層疊生效之自證**：本探針射程 ＝ `build_build_parcels`，其 PO 呼叫皆來自
   `k6_step0_merge` 之 `_mem`（合併群成員）⇒ 依構造⛔ 無 ghost ⇒ 「濾掉 `0` 列」係
   **受詞不在射程內**、⛔ 非層疊失效 ⇒ 另餵**正／負對照**自證（`ctrl`）。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "a98a99f"
sys.path.insert(0, VERIFY)

L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    import subprocess
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


def ghost3(x):
    return (str(x.get("原地號", "")) == "_GHOST"
            and float(x.get("G(㎡)", 0) or 0) == 0
            and float(x.get("a 面積(㎡)", 0) or 0) == 0)


K_GH = "R1 之 ghost3 數"
K_POS = "正對照（餵含 ghost 之 R1 全體）之濾掉數"
K_NEG = "負對照（餵已去 ghost 者）之濾掉數"


def build_once(vr074):
    """跑一趟 build_build_parcels，回傳 (rec, temp, build, selfcheck)。"""
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    PO_ORIG = ns["_projection_order"]
    SUB_ORIG = ns["_proj_pop_assert_subset"]
    selfcheck = (ns is PO_ORIG.__globals__)
    rec = {"calls": [], "po_calls": 0, "po_dropped": 0, "pending": None, "ctrl": {}}

    def _sub(tag, actual, base, blk=None):
        out = SUB_ORIG(tag, actual, base, blk=blk)
        if tag == "app:k6step0/_ordered":
            gh = [x for x in (actual or []) if ghost3(x)]
            rec["pending"] = {
                "序": len(rec["calls"]) + 1, "blk": blk,
                "len(_mem)": len(actual or []),
                "ghost3 命中": len(gh),
                "ghost3 之號": sorted(str(x.get("暫編地號", "")) for x in gh),
                "_mem 之暫編地號": sorted(str(x.get("暫編地號", "")) for x in (actual or [])),
                "len(base=TEMP_LAYER(blk))": len(base or []),
                "base 之 ghost3 命中": sum(1 for x in (base or []) if ghost3(x)),
            }
        return out

    def _po(parcels, p1, p2):
        src = list(parcels or [])
        keep = [t for t in src if not ghost3(t)] if vr074 else src
        rec["po_calls"] += 1
        rec["po_dropped"] += len(src) - len(keep)
        out = PO_ORIG(keep, p1, p2)
        if rec["pending"] is not None:
            d = rec["pending"]
            d["_ordered[0]"] = str(out[0].get("暫編地號", "")) if out else "<空>"
            d["_name"] = d["_ordered[0]"] + "+"
            rec["calls"].append(d)
            rec["pending"] = None
        return out

    ns["_proj_pop_assert_subset"] = _sub
    ns["_projection_order"] = _po
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _ = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)

    # ── 🔒 層疊之正／負對照（於還原**前**施測）──
    r1 = [t for t in temp if str(t.get("所屬街廓", "")) == "R1"]
    fl = (cad.get("front_lines") or {}).get("R1") or {}
    p1, p2 = fl.get("p1"), fl.get("p2")
    n_gh = sum(1 for t in r1 if ghost3(t))
    b0 = rec["po_dropped"]
    out_pos = ns["_projection_order"](r1, p1, p2)
    drop_pos = rec["po_dropped"] - b0
    r1c = [t for t in r1 if not ghost3(t)]
    b1 = rec["po_dropped"]
    out_neg = ns["_projection_order"](r1c, p1, p2)
    drop_neg = rec["po_dropped"] - b1
    rec["ctrl"] = {K_GH: n_gh, K_POS: drop_pos, K_NEG: drop_neg,
                   "正對照 入/出列數": [len(r1), len(out_pos)],
                   "負對照 入/出列數": [len(r1c), len(out_neg)]}

    ns["_proj_pop_assert_subset"] = SUB_ORIG
    ns["_projection_order"] = PO_ORIG
    return rec, temp, build, selfcheck


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    say("=" * 100)
    say("【W-G.9-168 M-A】`app:k6step0/_ordered` 之補量（⛔ 只讀）")
    say("=" * 100)
    say("  HEAD = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob = %s" % git1(["rev-parse", "HEAD:app.py"]))
    say("  WV_K6_STEP0 = %s" % os.environ.get("WV_K6_STEP0", "<未設·倉內預設 on>"))
    say("")

    recA, tempA, buildA, sc = build_once(False)
    say("  🔒 `A-4` 自證：`ns is _projection_order.__globals__` = **%s**" % sc)
    say("  🔒 現況態：PO 呼叫 %d 次（含二對照）／濾掉 %d 列（現況態應為 0）"
        % (recA["po_calls"], recA["po_dropped"]))
    recB, tempB, buildB, sc2 = build_once(True)
    say("  🔒 `VR-074` 態：PO 呼叫 %d 次（含二對照）／濾掉 %d 列"
        % (recB["po_calls"], recB["po_dropped"]))

    say("")
    say("  🔒 **層疊生效之正／負對照**（⛔ 不以「射程內濾掉 0 列」逕判失效）")
    say("     🔑 本探針射程 ＝ `build_build_parcels`；其 PO 呼叫皆來自 `k6_step0_merge` 之 `_mem`")
    say("        ⇒ 依構造⛔ 無 ghost ⇒ 射程內「濾掉 `0` 列」係**受詞不在射程內**、⛔ 非層疊失效。")
    for k in (K_GH, K_POS, K_NEG, "正對照 入/出列數", "負對照 入/出列數"):
        say("     `VR-074` 態｜%-34s = **%s**" % (k, recB["ctrl"].get(k)))
        say("     現況態    ｜%-34s = **%s**" % (k, recA["ctrl"].get(k)))
    ok_ctrl = (recB["ctrl"][K_GH] != 0
               and recB["ctrl"][K_POS] == recB["ctrl"][K_GH]
               and recB["ctrl"][K_NEG] == 0
               and recA["ctrl"][K_POS] == 0)
    say("     ⇒ 🔒 **層疊生效之自證 = %s**"
        "（正對照非零且＝受詞數・負對照零・現況態零 ⇒ 三造齊備）" % ok_ctrl)
    if not ok_ctrl:
        say("  🛑 層疊自證不過 ⇒ ⛔ 結論不得出艙")

    say("")
    say("=" * 100)
    say("§`A-6`　對照組（證量測器非紅·常規五／外部錨 ＝ `167R §三 M-1` 表）")
    say("=" * 100)
    gT = sum(1 for x in tempA if ghost3(x))
    gB = sum(1 for x in buildA if ghost3(x))
    say("  `TEMP_LAYER` 全體 `ghost3` 命中 = **%d**（外部錨期望 **8**）⇒ %s" % (gT, gT == 8))
    say("  `BUILD_LAYER` 全體 `ghost3` 命中 = **%d**（外部錨期望 **2**）⇒ %s" % (gB, gB == 2))
    say("  （總列數：`temp` = %d ／ `build` = %d）" % (len(tempA), len(buildA)))
    if gT == 0 or gB == 0:
        say("  🛑 對照組得 `0` ⇒ **先判量測器紅**、⛔ 不得逕報受詞綠")

    say("")
    say("=" * 100)
    say("§`A-2`／`A-3`　`app:k6step0/_ordered` 之逐次記錄（現況態）")
    say("=" * 100)
    say("  該 tag 之**執行次數** = **%d**" % len(recA["calls"]))
    if not recA["calls"]:
        say("  🛑 執行次數 `0` ⇒ 該點於本 harness **不可達**；成因須另查")
    for d in recA["calls"]:
        say("  ── 第 %d 次｜blk = %s" % (d["序"], d["blk"]))
        say("       len(_mem) = %d ／ **ghost3 命中 = %d** %s"
            % (d["len(_mem)"], d["ghost3 命中"], d["ghost3 之號"]))
        say("       _mem 之暫編地號 = %s" % d["_mem 之暫編地號"])
        say("       base ＝ TEMP_LAYER(%s)：len = %d ／ 其 ghost3 命中 = %d"
            % (d["blk"], d["len(base=TEMP_LAYER(blk))"], d["base 之 ghost3 命中"]))
        say("       `_ordered[0]` = %r ⇒ **`_name` = %r**" % (d["_ordered[0]"], d["_name"]))

    say("")
    say("=" * 100)
    say("§`A-4`　二態對拍（現況 vs `VR-074` 模擬態）")
    say("=" * 100)
    say("  執行次數：現況 = %d ／ `VR-074` = %d ⇒ %s"
        % (len(recA["calls"]), len(recB["calls"]),
           "相同" if len(recA["calls"]) == len(recB["calls"]) else "*** 相異 ***"))
    same = True
    for a, b in zip(recA["calls"], recB["calls"]):
        ok = (a["_name"] == b["_name"])
        same = same and ok
        say("  第 %d 次｜blk = %-6s｜現況 = %-16r／`VR-074` = %-16r ⇒ **%s**"
            % (a["序"], a["blk"], a["_name"], b["_name"], "相同" if ok else "*** 相異 ***"))
    ghost_zero = (all(d["ghost3 命中"] == 0 for d in recA["calls"])
                  and all(d["ghost3 命中"] == 0 for d in recB["calls"]))

    say("")
    say("=" * 100)
    say("§`A-5`　判準（二項須同時成立）")
    say("=" * 100)
    say("  ① `A-2` 之 `ghost3` 命中數逐次皆 `0` ⇒ **%s**" % ghost_zero)
    say("  ② `A-3` 之 `_name` 二態逐次相同 ⇒ **%s**" % same)
    say("  ⇒ 二項齊備 = **%s**（層疊自證 = %s）" % (ghost_zero and same, ok_ctrl))
    if ghost_zero and same and ok_ctrl:
        say("  ⇒ 🔒 (A) 與 (B) 於該點**等價** ⇒ `167R` 之 `16` 格預測集合**可轉用於 `169`**")
    else:
        say("  🛑 **`167R` 之 `16` 格預測集合作廢**（`S-2`）")

    out = {"base": BASE_REF, "self_check_ns_is_globals": sc,
           "counts": {"現況": len(recA["calls"]), "VR-074": len(recB["calls"])},
           "po_dropped": {"現況": recA["po_dropped"], "VR-074": recB["po_dropped"]},
           "overlay_control": {"現況": recA["ctrl"], "VR-074": recB["ctrl"],
                               "自證": ok_ctrl},
           "control": {"TEMP_LAYER_ghost3": gT, "BUILD_LAYER_ghost3": gB},
           "calls_現況": recA["calls"], "calls_VR074": recB["calls"],
           "A5": {"ghost3_all_zero": ghost_zero, "name_identical": same}}
    with open(os.path.join(OUTDIR, "probe_WG9168_k6step0_%s.log" % BASE_REF),
              "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(OUTDIR, "WG9168_k6step0_%s.json" % BASE_REF),
              "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("")
    print("log ⇒ %s" % os.path.join(OUTDIR, "probe_WG9168_k6step0_%s.log" % BASE_REF))
    return 0


if __name__ == "__main__":
    sys.exit(main())
