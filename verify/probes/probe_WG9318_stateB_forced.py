# -*- coding: utf-8 -*-
"""`W-G.9-318` `§三`（工項一）：**態乙**之 `forced` 旗標與 `W₀`／`Wf` 之**一次唯讀驅動**。

🛑 **唯讀**——本器**⛔ 改任何生產碼一字**、**⛔ 寫 `verify/baselines`**、**⛔ 設 `WV_BAKE`**、
   **⛔ 施任何替身**（`spy` 一律**原樣回傳**上游之回傳值·⛔ 改其實參）。
🛑 **⛔ 匯入即驅動**——一切驅動在 `main()` 內，且僅於 `__main__` 執行。

🔒 **受詞（單 `§三-1` 逐字）**
   「`WV_K6_STEP0=off`（＝ 態乙）下，`R4` 之 `left_forced_offset`／`right_forced_offset`，
     及該街廓左右側之 `W₀`／`Wf`（🛑 **未捨入**·⛔ `2dp`）。」

🔒 **⛔ 由倉內既有落檔得之**（`W-G.9-317R §四-g` 實掃：同檔具態乙標記 ⋀ 一列含 `R4` 與
   `right_forced_offset` ＝ **`0`** 檔；判別力[必非零] 態甲 ＝ **`7`** 檔 ⇒ 該檢⛔ 恆為零）。
🔒 **態甲之值⛔ 直接轉用**（`W-G.9-278R` 之 `False` 係態甲之量）。

🔒 **量之取法（⛔ 外部重建·一律自碼面之同一物取）**
   · `_forced_offset_map[<blk>]` ＝ `run_corner_pk` 之**第五**回傳（`selection_pipeline.py:364`
     之 `_forced_offset_map`），亦即 `run_step_g` 之 `forced_map` 實參
     ⇒ `stepg:341` `ss["f3L_forced_offset"] = forced_map`。
   · `_fo_left`／`_fo_right` ＝ `stepg:647`–`:648` 之**區域名**，經 `_select_pool_slot` 之
     spy **框內省**取得（app 之對應為 `app.py:21886`–`:21887`·⛔ 可 headless 驅動）。
   · `_b_L0`／`_b_R0` ＝ `_select_pool_slot` 之**實參** `left['b']`／`right['b']`
     （`stepg:1048`–`:1049` 所算者·⛔ 器內另算）。
   · `_adv_final['W0_left'/'W0_right'/'Wf_left'/'Wf_right']` ＝ 於 `_rw_from_width`
     （＝ `ns["rw_from_width"]`·`stepg:384`）之 spy **框內省** `_run_step_g_impl` 之區域名
     `_adv_final` 取之；**只採 `_sd_tag` 已綁定之呼叫**（＝ 結構閘 telescoping 之迴圈內·
     `stepg:1447`–`:1477`）⇒ 排除「前一街廓之殘值」（`自誤 418 ③` 之形）。

🔒 **判別力二造（單 `§三-2` 逐字）**
   · 造甲[必非零]：同受詞下**態甲**（`WV_K6_STEP0` 未設）之 `R4`
     ⇒ 須得 `left_forced_offset = True`／`right_forced_offset = False`。
   · 造乙[必為零]：一人造街廓名（**執行期組出**·字面⛔ 出艙）之命中 ＝ `0`。
   🛑 **二造異色方得採信**；同色 ⇒ 器紅 ⇒ 停機。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9318_stateB_forced.py [<倉根>]`
`rc`：`0` 正常／`5` **器紅**（判別力二造不成立）。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
STATE_B = "off"                 # 🔒 態乙（`K-9-29 二` 所令之態）
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
W = 132
NA = "【⛔ 可得】"


def say(s=""):
    print(s)


def _norm_side(s):
    if s is None:
        return None
    t = str(s)
    if "左" in t or t.lower().startswith("l"):
        return "left"
    if "右" in t or t.lower().startswith("r"):
        return "right"
    return None


def _climb(names, upto=20):
    """自呼叫端往上逐層取區域名（唯讀內省）。`+2` ＝ 補本函式與 spy 自身二層（坑 `bb`）。"""
    out = {k: None for k in names}
    seen = {k: False for k in names}
    for d in range(1, upto + 1):
        try:
            f = sys._getframe(d + 1)
        except ValueError:
            break
        for k in names:
            if not seen[k] and k in f.f_locals:
                out[k] = f.f_locals[k]
                seen[k] = True
    return out, seen


def drive(sb, state):
    """一 (態, 情境) 一次驅動。`state` ∈ {'B','A'}；`'B'` ＝ 態乙（`WV_K6_STEP0=off`）。

    🛑 **唯讀**：三 spy 皆原樣回傳上游之回傳值。
    """
    if state == "B":
        os.environ[ENV] = STATE_B
    else:
        os.environ.pop(ENV, None)          # 🔒 態甲 ＝ **未設**（⛔ 設為他值）
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    slots = []          # `_select_pool_slot` 之逐次實參（含 `_b_L0`／`_b_R0`／`_fo_*`）
    advf = {}           # blk -> `_adv_final` 之四鍵（僅採 telescoping 迴圈內之呼叫）
    _o_slot = ns["_select_pool_slot"]
    _o_rwf = ns["rw_from_width"]

    def _spy_slot(widths, left, right):
        out = _o_slot(widths, left, right)                      # 🛑 先呼叫·逐位原樣回傳
        p, _ = _climb(["blk_label", "_fo_left", "_fo_right",
                       "_left_buffer_S", "_right_buffer_S",
                       "_has_left_corner", "_has_right_corner"])
        slots.append({
            "blk": p.get("blk_label"),
            "fo_left": p.get("_fo_left"), "fo_right": p.get("_fo_right"),
            "buf_L": p.get("_left_buffer_S"), "buf_R": p.get("_right_buffer_S"),
            "has_L": p.get("_has_left_corner"), "has_R": p.get("_has_right_corner"),
            "b_L0": (left or {}).get("b"), "b_R0": (right or {}).get("b"),
        })
        return out

    def _spy_rwf(w):
        out = _o_rwf(w)                                         # 🛑 逐位原樣回傳
        p, seen = _climb(["_sd_tag", "_adv_final", "blk_label"])
        # 🔒 只採 `_sd_tag` 已綁定之呼叫 ⇒ 必在結構閘 telescoping 之迴圈內
        #    ⇒ `_adv_final` 必為**本街廓**之物（⛔ 前一街廓之殘值）
        if seen.get("_sd_tag") and seen.get("_adv_final") and seen.get("blk_label"):
            a = p["_adv_final"]
            if isinstance(a, dict):
                advf[p["blk_label"]] = {
                    "W0_left": a.get("W0_left"), "W0_right": a.get("W0_right"),
                    "Wf_left": a.get("Wf_left"), "Wf_right": a.get("Wf_right"),
                }
        return out

    ns["_select_pool_slot"] = _spy_slot
    ns["rw_from_width"] = _spy_rwf

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _off, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            sb, snapshot=snapshot)
    err, g_rows = None, []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e)
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    reached = []
    for r in g_rows:
        b = r.get("所屬街廓")
        if b and b not in reached:
            reached.append(b)
    return {"forced": forced or {}, "pk": _s or [], "off": list(_off or []),
            "slots": slots, "advf": advf, "err": err, "reached": reached,
            "g_rows": g_rows}


def _fmt(v):
    if v is None:
        return NA
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, float):
        return "%.10f" % v
    return str(v)


def main():
    say("=" * W)
    say("【`W-G.9-318` `§三`（工項一）】態乙之 `forced` 旗標與 `W₀`／`Wf` 之一次唯讀驅動")
    say("=" * W)
    say("\U0001f6d1 **唯讀**：⛔ 改生產碼一字·⛔ 寫 `verify/baselines`·⛔ 設 `WV_BAKE`·⛔ 施替身（spy 逐位原樣回傳）")
    say("\U0001f512 態乙 ＝ `%s=%s`；態甲 ＝ `%s` **未設**（＝ 判別力造甲）" % (ENV, STATE_B, ENV))
    say("\U0001f512 情境 ＝ %s；街廓母體 ＝ %s（`6` 街廓）" % ([("%gm" % s) for s in SBS], BLKS))
    say("\U0001f512 一切浮點**未捨入**（`%%.10f`）·⛔ `2dp`")

    R = {}
    for st_ in ("B", "A"):
        for sb in SBS:
            R[(st_, "%gm" % sb)] = drive(sb, st_)

    # ── 表 1：`_forced_offset_map[<blk>]`（六街廓 × 二情境 ＝ 12 格·逐態）────────
    say("")
    say("─" * W)
    say("【表 1】`_forced_offset_map[<blk>]` 之 `left_forced_offset`／`right_forced_offset`")
    say("　　框 ＝ `run_corner_pk` 之**第五**回傳（`selection_pipeline.py:364` `_forced_offset_map`）")
    say("　　母體 ＝ 六街廓 × 二情境 ＝ **12** 格（逐態各 12 格）")
    say("─" * W)
    say("| 態 | 情境 | 街廓 | left_forced_offset | right_forced_offset | left_has_side | right_has_side |")
    say("|---|---|---|---|---|---|---|")
    for st_, nm in (("B", "乙"), ("A", "甲")):
        for tag in ("0m", "3.5m"):
            fm = R[(st_, tag)]["forced"]
            for b in BLKS:
                d = fm.get(b)
                if d is None:
                    say("| %s | %s | `%s` | %s | %s | %s | %s |" % (nm, tag, b, NA, NA, NA, NA))
                else:
                    say("| %s | %s | `%s` | `%s` | `%s` | `%s` | `%s` |"
                        % (nm, tag, b, _fmt(d.get("left_forced_offset")),
                           _fmt(d.get("right_forced_offset")),
                           _fmt(d.get("left_has_side")), _fmt(d.get("right_has_side"))))

    # ── 表 2：`_fo_left`／`_fo_right` ＋ `_b_L0`／`_b_R0`（框內省）─────────────
    say("")
    say("─" * W)
    say("【表 2】`_fo_left`／`_fo_right`（`stepg:647`–`:648` 之區域名）＋ `_b_L0`／`_b_R0`")
    say("　　框 ＝ `_select_pool_slot` 之 spy 框內省 ＋ 其實參 `left['b']`／`right['b']`（`stepg:1048`–`:1049`）")
    say("　　🛑 `_select_pool_slot` **只在非退化枝**被呼叫（`_degenerate_order` 或 `_N <= 1` ⇒ ⛔ 呼叫）")
    say("　　　⇒ 未列之街廓一律 %s 並載其由" % NA)
    say("─" * W)
    say("| 態 | 情境 | 街廓 | _fo_left | _fo_right | _left_buffer_S | _right_buffer_S | _b_L0 | _b_R0 |")
    say("|---|---|---|---|---|---|---|---|---|")
    for st_, nm in (("B", "乙"), ("A", "甲")):
        for tag in ("0m", "3.5m"):
            got = {s["blk"]: s for s in R[(st_, tag)]["slots"]}
            for b in BLKS:
                s = got.get(b)
                if s is None:
                    say("| %s | %s | `%s` | %s | %s | %s | %s | %s | %s |"
                        % (nm, tag, b, NA, NA, NA, NA, NA, NA))
                else:
                    say("| %s | %s | `%s` | `%s` | `%s` | `%s` | `%s` | `%s` | `%s` |"
                        % (nm, tag, b, _fmt(s["fo_left"]), _fmt(s["fo_right"]),
                           _fmt(s["buf_L"]), _fmt(s["buf_R"]),
                           _fmt(s["b_L0"]), _fmt(s["b_R0"])))

    # ── 表 3：`_adv_final` 之 `W0`／`Wf` ─────────────────────────────────────
    say("")
    say("─" * W)
    say("【表 3】`_adv_final['W0_left'／'W0_right'／'Wf_left'／'Wf_right']`（**未捨入**）")
    say("　　框 ＝ `_rw_from_width` 之 spy 框內省（只採 `_sd_tag` 已綁定者 ⇒ telescoping 迴圈內）")
    say("　　母體 ＝ **管線可達之街廓**；⛔ 可達者一律 %s 並載其由" % NA)
    say("─" * W)
    say("| 態 | 情境 | 街廓 | W0_left | W0_right | Wf_left | Wf_right |")
    say("|---|---|---|---|---|---|---|")
    for st_, nm in (("B", "乙"), ("A", "甲")):
        for tag in ("0m", "3.5m"):
            d = R[(st_, tag)]
            for b in BLKS:
                a = d["advf"].get(b)
                if a is None:
                    why = ("管線已於 `%s` 中止" % (d["reached"][-1] if d["reached"] else "R1 之前")
                           if b not in d["reached"] else "本街廓未進入 telescoping 迴圈（無 corner 側）")
                    say("| %s | %s | `%s` | %s | %s | %s | %s |  ← %s"
                        % (nm, tag, b, NA, NA, NA, NA, why))
                else:
                    say("| %s | %s | `%s` | `%s` | `%s` | `%s` | `%s` |"
                        % (nm, tag, b, _fmt(a["W0_left"]), _fmt(a["W0_right"]),
                           _fmt(a["Wf_left"]), _fmt(a["Wf_right"])))

    # ── 表 4：【左】／【右】第 1 宗指配 之逐字 ───────────────────────────────
    say("")
    say("─" * W)
    say("【表 4】【左】／【右】**第 1 宗指配**之逐字（＝ `_l_forced`／`_r_forced` 之唯一判據）")
    say("　　框 ＝ `run_corner_pk` 之**第二**回傳 `_corner_select_results`（`selection_pipeline.py:571`／`:574`）")
    say("　　判準逐字 ＝ `'強制抵費地' in str(_r_pk.get('【左】第1宗指配', ''))`（`selection_pipeline.py:612`–`:613`）")
    say("─" * W)
    say("| 態 | 情境 | 街廓 | 【左】第1宗指配 | 【右】第1宗指配 | 【左】最小面積(㎡) | 【右】最小面積(㎡) |")
    say("|---|---|---|---|---|---|---|")
    for st_, nm in (("B", "乙"), ("A", "甲")):
        for tag in ("0m", "3.5m"):
            rows = {r.get("街廓"): r for r in R[(st_, tag)]["pk"]}
            for b in BLKS:
                r = rows.get(b)
                if r is None:
                    say("| %s | %s | `%s` | %s | %s | %s | %s |" % (nm, tag, b, NA, NA, NA, NA))
                else:
                    say("| %s | %s | `%s` | `%s` | `%s` | `%s` | `%s` |"
                        % (nm, tag, b, r.get("【左】第1宗指配"), r.get("【右】第1宗指配"),
                           r.get("【左】最小面積(㎡)"), r.get("【右】最小面積(㎡)")))

    # ── 管線可達與中止 ───────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【表 5】管線可達之街廓與中止閘（逐態逐情境）")
    say("─" * W)
    for st_, nm in (("B", "乙"), ("A", "甲")):
        for tag in ("0m", "3.5m"):
            d = R[(st_, tag)]
            e = (d["err"] or "（無·跑完）").split("\n")[0]
            say("· 態%s %s ⇒ 可達 %s｜中止閘逐字 ＝ %s" % (nm, tag, d["reached"], e))

    # ── 判別力二造 ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【判別力二造】（單 `§三-2` 逐字）")
    say("─" * W)
    okA = True
    for tag in ("0m", "3.5m"):
        fm = R[("A", tag)]["forced"].get("R4") or {}
        l = fm.get("left_forced_offset")
        r = fm.get("right_forced_offset")
        hit = (l is True and r is False)
        okA = okA and hit
        say("· 造甲[必非零] 態甲 %s `R4` ⇒ left_forced_offset ＝ `%s`（須 `True`）／"
            "right_forced_offset ＝ `%s`（須 `False`）⇒ %s"
            % (tag, _fmt(l), _fmt(r), "✅" if hit else "🔴"))
    fake = "R" + str(9000 + 318)                 # 🔒 執行期組出·字面⛔ 出艙
    nz = 0
    for k, d in R.items():
        if fake in (d["forced"] or {}):
            nz += 1
        nz += sum(1 for s in d["slots"] if s["blk"] == fake)
        nz += sum(1 for b in d["advf"] if b == fake)
    say("· 造乙[必為零] 人造街廓名（執行期組出·字面⛔ 出艙）之命中 ＝ **%d**（須 `0`）⇒ %s"
        % (nz, "✅" if nz == 0 else "🔴"))
    ok = bool(okA) and nz == 0
    say("· 二造異色 ⇒ 器非紅 ＝ **%s**" % ("✅ 是" if ok else "🔴 否 ⇒ 停機"))

    # ── 停機款之判 ───────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【`§三-3` 停機款之判】")
    say("─" * W)
    st1 = []
    st2 = []
    for tag in ("0m", "3.5m"):
        fm = R[("B", tag)]["forced"].get("R4")
        if fm is None:
            st2.append(tag)
            continue
        r = fm.get("right_forced_offset")
        if r is None:
            st2.append(tag)
        elif bool(r) is True:
            st1.append(tag)
    say("· `停-1`（態乙 `R4` `right_forced_offset = True`）⇒ 觸發之情境 ＝ %s ⇒ %s"
        % (st1 if st1 else "無", "🛑 **觸發**" if st1 else "🟢 **未觸發**"))
    say("· `停-2`（態乙 `R4` 二旗標 %s）⇒ 觸發之情境 ＝ %s ⇒ %s"
        % (NA, st2 if st2 else "無", "🛑 **觸發**" if st2 else "🟢 **未觸發**"))

    # ── 旁證（⛔ 充實測·單 `§三-3` 逐字）────────────────────────────────
    say("")
    say("─" * W)
    say("【旁證·⛔ 充實測】`run_corner_pk` 之**第三**回傳 `_off`（＝ `_offset_diag_rows`）")
    say("　　🛑 單 `§三-3` 逐字：其與 `left/right_forced_offset` **⛔ 經證為同一物** ⇒ ⛔ 以之代實測")
    say("─" * W)
    for st_, nm in (("B", "乙"), ("A", "甲")):
        for tag in ("0m", "3.5m"):
            rows = R[(st_, tag)]["off"]
            say("· 態%s %s ⇒ `_off` 列數 ＝ %d" % (nm, tag, len(rows)))
            for x in rows:
                say("    %r" % (x,))

    return 0 if ok else 5


if __name__ == "__main__":
    sys.exit(main())
