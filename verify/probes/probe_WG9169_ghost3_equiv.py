# -*- coding: utf-8 -*-
"""`W-G.9-169` `D-6`／`D-1`／`D-2`／`D-4`／`D-5` 探針（⛔ 只讀·⛔ 不改任何生產碼）。

`D-6`　`L-1` 之 `_proj_pop_ghost3` 與 `g_row` 層既有三式之**等價自檢**
        （真值表 `2³ = 8` 格 ＋ 三鍵各自「缺鍵」之態 ⇒ `≥ 11` 樣本·逐樣本同值）——`GB-116` 之代償。
`D-5`　`L-3` 換源之**零變化**：`no_ghost` 新舊述詞於 `TEMP_LAYER`／`BUILD_LAYER` 之輸出逐位相同。
`D-1`　改宣告而不改實參 ⇒ 須 `raise`。
`D-2`　人造注入 `G(㎡)` 鍵 ⇒ `L-2` 守護斷言須 `raise`。
`D-4`　人造 `_mem` 含 `ghost3` 為真之成員 ⇒ `L-6` 之斷言須 `raise`。
🛑 全部於**記憶體複本／函式局部**為之，⛔ 不改倉內任何檔。
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
OUTDIR = os.path.join(VERIFY, "out")
BASE_REF = "a3c97aa"
sys.path.insert(0, VERIFY)
L = []


def say(s=""):
    print(s)
    L.append(s)


def git1(a):
    import subprocess
    return subprocess.run(["git"] + a, cwd=REPO, capture_output=True,
                          check=True).stdout.decode("utf-8").strip()


# ── `g_row` 層之既有三式（逐字複刻自 app.py·⛔ 未改該三處一字）──
def grow_a(r):                      # app.py:6289-6291（`_no` 之分流式）
    return (str(r.get('原地號', '')) == '_GHOST'
            and float(r.get('G(㎡)', 0) or 0) == 0.0
            and float(r.get('a 面積(㎡)', 0) or 0) == 0.0)


def grow_b(r):                      # app.py:6301-6303（`_c1`／`_c2`／`_c3` 之診斷式）
    _c1 = (str(r.get('原地號', '')) == '_GHOST')
    _c2 = (float(r.get('G(㎡)', 0) or 0) == 0.0)
    _c3 = (float(r.get('a 面積(㎡)', 0) or 0) == 0.0)
    return _c1 and _c2 and _c3


def grow_c(r):                      # app.py:6319-6321（`_bad_no` 之反面式·取其正面）
    return (str(r.get('原地號', '')) == '_GHOST'
            and float(r.get('G(㎡)', 0) or 0) == 0.0
            and float(r.get('a 面積(㎡)', 0) or 0) == 0.0)


def samples():
    """真值表 8 格 ＋ 三鍵各自缺鍵之態（3）＝ 11；另加 3 個邊界態 ⇒ 14。"""
    out = []
    for i, (c1, c2, c3) in enumerate([(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)], 1):
        out.append(("真值表#%d(①=%d②=%d③=%d)" % (i, c1, c2, c3),
                    {"暫編地號": "T%d" % i,
                     "原地號": "_GHOST" if c1 else "628-1",
                     "G(㎡)": 0.0 if c2 else 12.5,
                     "a 面積(㎡)": 0.0 if c3 else 7.25}))
    out.append(("缺鍵·無 原地號", {"暫編地號": "M1", "G(㎡)": 0.0, "a 面積(㎡)": 0.0}))
    out.append(("缺鍵·無 G(㎡)", {"暫編地號": "M2", "原地號": "_GHOST", "a 面積(㎡)": 0.0}))
    out.append(("缺鍵·無 a 面積(㎡)", {"暫編地號": "M3", "原地號": "_GHOST", "G(㎡)": 0.0}))
    out.append(("三鍵全缺（＝parcel 層之實態）", {"暫編地號": "M4", "原地號": "_GHOST"}))
    out.append(("空字串 G", {"暫編地號": "E1", "原地號": "_GHOST", "G(㎡)": "", "a 面積(㎡)": ""}))
    out.append(("None G", {"暫編地號": "E2", "原地號": "_GHOST", "G(㎡)": None, "a 面積(㎡)": None}))
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import build_ownership, build_build_parcels

    say("=" * 100)
    say("【W-G.9-169 D-1／D-2／D-4／D-5／D-6】落地後之判別力對照（⛔ 只讀）")
    say("=" * 100)
    say("  HEAD = %s" % git1(["rev-parse", "HEAD"]))
    say("  app.py blob（工作區·⛔ 已含本批之生產碼變更） = %s"
        % git1(["hash-object", os.path.join(REPO, "app.py")]))
    say("")

    ns, fake_st = harvest()
    G3 = ns["_proj_pop_ghost3"]
    FILT = ns["_proj_pop_filter"]
    GUARD = ns["_proj_pop_key_guard"]
    ASEQ = ns["_proj_pop_assert_seq"]
    DECL = ns["_PROJ_POP_DECL"]

    # ═════ D-6 ═════
    say("=" * 100)
    say("§`D-6`　`L-1` vs `g_row` 層既有三式之等價自檢（`GB-116` 之代償）")
    say("=" * 100)
    say("  %-30s %-8s %-8s %-8s %-8s %s" % ("樣本", "L-1", ":6289", ":6301", ":6319", "四式同值"))
    ok6 = True
    rows = []
    for name, s in samples():
        v = [G3(s), grow_a(s), grow_b(s), grow_c(s)]
        same = (len(set(v)) == 1)
        ok6 = ok6 and same
        rows.append({"樣本": name, "L-1": v[0], "6289": v[1], "6301": v[2], "6319": v[3],
                     "同值": same})
        say("  %-30s %-8s %-8s %-8s %-8s %s" % (name, v[0], v[1], v[2], v[3],
                                                "✅" if same else "*** 相異 ***"))
    say("  ⇒ 樣本數 = **%d**（須 ≥ 11）／**逐樣本同值 = %s**" % (len(rows), ok6))

    # ═════ D-5 ═════
    say("")
    say("=" * 100)
    say("§`D-5`　`L-3` 換源之零變化（`no_ghost` 新舊述詞·二層）")
    say("=" * 100)
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, 0.0)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _ = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    ok5 = True
    for lname, layer in (("TEMP_LAYER", temp), ("BUILD_LAYER", build)):
        new = [str(t.get("暫編地號", "")) for t in FILT("no_ghost", layer)]
        old = [str(t.get("暫編地號", "")) for t in layer if not t.get("_is_ghost_sliver")]
        same = (new == old)
        ok5 = ok5 and same
        say("  %-12s 入 %3d ⇒ 新述詞出 %3d ／ 舊述詞出 %3d ⇒ **逐位相同 = %s**"
            % (lname, len(layer), len(new), len(old), same))
        if not same:
            say("     對稱差 = %r" % sorted(set(new) ^ set(old)))
    say("  🔒 外部錨 ＝ `W-G.9-167R §三 M-1 d`（二層之對稱差為**空**）")
    say("  🔒 **判別力**：同層以 `identity` 濾 ⇒ 出 %d／%d（⛔ 未濾 ⇒ 證上表之 `no_ghost` 確有作用）"
        % (len(FILT("identity", temp)), len(FILT("identity", build))))

    # ═════ D-1 ═════
    say("")
    say("=" * 100)
    say("§`D-1`　改宣告而**不**改實參 ⇒ 須 `raise`")
    say("=" * 100)
    blk = "R1"
    base = [t for t in build if str(t.get("所屬街廓", "")) == blk]
    actual_ok = FILT("identity+no_ghost", base)
    try:
        ASEQ("sp:_rank_by_tpid", actual_ok, base, blk=blk)
        say("  ① 正對照（實參已同步）⇒ **未 raise** ✅")
        d1a = True
    except Exception as e:                                        # noqa: BLE001
        say("  ① 正對照 ⇒ *** 意外 raise ***：%s" % str(e)[:100])
        d1a = False
    try:
        ASEQ("sp:_rank_by_tpid", list(base), base, blk=blk)        # 實參未濾 ＝ 宣告改而實參未改
        say("  ② 負對照（實參未濾）⇒ *** 未 raise ***（🛑 判別力失效）")
        d1b = False
    except RuntimeError as e:
        say("  ② 負對照（實參未濾）⇒ **raise** ✅")
        say("     逐字（首 150）：%s" % str(e)[:150])
        d1b = True

    # ═════ D-2 ═════
    say("")
    say("=" * 100)
    say("§`D-2`　人造注入 `G(㎡)` 鍵 ⇒ `L-2` 守護斷言須 `raise`")
    say("=" * 100)
    clean = [dict(t) for t in base]
    try:
        GUARD("sp:_rank_by_tpid", clean, "BUILD_LAYER")
        say("  ① 正對照（未注入）⇒ **未 raise** ✅")
        d2a = True
    except Exception as e:                                        # noqa: BLE001
        say("  ① 正對照 ⇒ *** 意外 raise ***：%s" % str(e)[:100])
        d2a = False
    dirty = [dict(t) for t in base]
    dirty[0]["G(㎡)"] = 0.0
    try:
        GUARD("sp:_rank_by_tpid", dirty, "BUILD_LAYER")
        say("  ② 負對照（注入 `G(㎡)`）⇒ *** 未 raise ***（🛑 判別力失效）")
        d2b = False
    except RuntimeError as e:
        say("  ② 負對照（注入 `G(㎡)`）⇒ **raise** ✅")
        say("     逐字（首 150）：%s" % str(e)[:150])
        d2b = True

    # ═════ D-4 ═════
    say("")
    say("=" * 100)
    say("§`D-4`　人造 `_mem` 含 `ghost3` 為真之成員 ⇒ `L-6` 之斷言須 `raise`")
    say("=" * 100)
    say("  🔒 `L-6` 之斷言係 inline 於 `k6_step0_merge`（`app.py`）⇒ 此處以**同式**重演其判：")
    mem_clean = [t for t in temp if str(t.get("所屬街廓", "")) == "R2"][:2]
    gh = [t for t in temp if G3(t)]
    say("  ① 正對照（真實 `_mem`·`R2` 前二筆）：`ghost3` 命中 = **%d** ⇒ ⛔ 不 raise ✅"
        % sum(1 for t in mem_clean if G3(t)))
    mem_dirty = list(mem_clean) + [gh[0]]
    hit = [str(t.get("暫編地號", "")) for t in mem_dirty if G3(t)]
    say("  ② 負對照（注入 `%s`）：`ghost3` 命中 = **%d** ⇒ 條件 `if _gh3_mem:` 成立 ⇒ **raise** ✅"
        % (str(gh[0].get("暫編地號", "")), len(hit)))
    d4 = (sum(1 for t in mem_clean if G3(t)) == 0) and (len(hit) == 1)

    # ═════ 宣告表現況 ═════
    say("")
    say("=" * 100)
    say("§ 落地後之 `_PROJ_POP_DECL`（`14` tag·`filter` 欄）")
    say("=" * 100)
    for k, v in DECL.items():
        say("  %-26s %-18s %-14s %s" % (k, v.get("kind"), v.get("source"), v.get("filter")))

    out = {"base": BASE_REF, "D6": {"樣本數": len(rows), "逐樣本同值": ok6, "rows": rows},
           "D5": ok5, "D1": {"正對照未raise": d1a, "負對照raise": d1b},
           "D2": {"正對照未raise": d2a, "負對照raise": d2b}, "D4": d4,
           "DECL_filters": {k: v.get("filter") for k, v in DECL.items()}}
    say("")
    say("🔒 **總判**：`D-6` %s／`D-5` %s／`D-1` %s／`D-2` %s／`D-4` %s"
        % (ok6, ok5, d1a and d1b, d2a and d2b, d4))
    with open(os.path.join(OUTDIR, "probe_WG9169_ghost3_equiv_%s.log" % BASE_REF),
              "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(OUTDIR, "WG9169_controls_%s.json" % BASE_REF),
              "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("")
    print("log ⇒ %s" % os.path.join(OUTDIR, "probe_WG9169_ghost3_equiv_%s.log" % BASE_REF))
    return 0


if __name__ == "__main__":
    sys.exit(main())
