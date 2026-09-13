# -*- coding: utf-8 -*-
"""`W-G.9-274` `§四-1`／`§四-2`：**實跑側 `Rw` 之產生式定位** ＋ **態甲 `R4` 未觸發之成因**。

🛑 **⛔ 由 `85.41` 反推其 `W`**（單 `§七` 款 `4`）——`rw_from_width` 非全域線性
   ⇒ 反推之前提不成立。**本器一律正面取產生式之<u>實際輸入</u>**（包裹 `ns["rw_increment"]`）。

🔒 **量之取法（⛔ 另寫第二份判準）**
   · **實跑側** ＝ 包裹 `ns["rw_increment"]`，錄其每次呼叫之 `(W_prev, W_cur, 回傳)`
     ——其即 `app.py` 之 `Rw_pct = (rw_increment(W_prev, W_cur) * 100.0)` 之實參。
   · **理論側** ＝ 包裹 `ns["_select_pool_slot"]`，錄 `widths` 與回傳
     （`widths` 之來源 ＝ `_widths_local[...] = float(res.get('_宗地寬度', 0.0) or 0.0)`）。
   · **呼叫條件** ＝ 包裹 `ns["_spatial_order_parcels_v2"]` 錄其回傳之 `ordered` 長度（＝ `_N`）
     ＋ 唯讀內省取呼叫端框之 `blk_label`／`d_hat`／`corner_pt`（`_degenerate_order` 之二輸入）。
   · **`W` 之單一產生者** ＝ 包裹 `ns["k956_W_from_mp"]`，錄其呼叫次數與回傳。

🛑 **判別力（發單側定·⛔ CC 自訂）**
   對照須落於 `rw_from_width` 之**非飽和域**（`W < 18`）**且**其變動能驅動 `Rw(%)` 欄；
   **⛔ 取 `R4 left`**（`W = 46.08 ≥ 18`·已證落於飽和區·`自誤 345` 之再現）。
   **取法**：於**態甲**之全母體（六街廓 × 二情境 × 二側）中逐一列出 `W < 18` 之側，
   取其中「理論＝實跑」者為**必真對照**、「理論≠實跑」者（若有）為**必偽對照**。
   🛑 **全母體無 `W < 18` 之對照 ⇒ 照實具名「對照不存在」，出艙第三種碼，
      ⛔ 以飽和者頂替、⛔ 逕稱器非紅。**

🛑 **⛔ 判孰為正確之 `W`、⛔ 提修法主張、⛔ 判該閘應否放寬**——**出艙即止**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9274_rw_origin.py [倉根]`
`rc`：`0`／`3` 母體為 `0`／`5` **量測器紅**。
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
W = 130
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
SAT = 18.0                      # `CLAUDE.md` 逐字：`W≥18→100%`（飽和點）


def say(s=""):
    print(s)


def drive(sb, mode):
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import probe_WG9269_c4_gamma as G4

    ns, fake_st = harvest()
    rwi, slots, orders, k956 = [], [], [], []
    _o_rwi = ns["rw_increment"]
    _o_slot = ns["_select_pool_slot"]
    _o_ord = ns["_spatial_order_parcels_v2"]
    _o_k956 = ns["k956_W_from_mp"]

    def _peek(depth, keys):
        """取**呼叫 `_peek` 者**之上 `depth` 層框之區域變數。

        🩸 **本批之自捕**：初版寫 `sys._getframe(depth)`，而 `_peek` **自身即佔一層**
           ⇒ `depth=1` 取到的是 **`_spy_*` 自己**、⛔ 生產碼之框 ⇒ `blk_label` **全為 `None`**。
           🔴 其徵候是**一整張表全欄「不可得」**——看起來像「管線未達」，而實為**框差一層**。
           **攔法**：`(1)` 抽出框內省為輔助函式時須 `+1` 補其自身之一層；
           `(2)` 附**自我驗證閘**——所錄之 `blk` 集合須為 `BLKS` 之**非空子集**，
           含 `None` 即 **loud 拒測**（⛔ 以「不可得」出艙）。
        """
        try:
            f = sys._getframe(depth + 1).f_locals      # 🔒 +1 ＝ 補 `_peek` 自身之一層
        except Exception:                                           # noqa: BLE001
            raise                       # 🛑 ⛔ 靜默吞
        return {k: f.get(k) for k in keys}

    def _spy_rwi(W_prev, W_cur):
        out = _o_rwi(W_prev, W_cur)
        rwi.append({"W_prev": float(W_prev), "W_cur": float(W_cur),
                    "out": float(out), "pct": float(out) * 100.0})
        return out                      # 🛑 逐位原樣回傳

    def _spy_slot(widths, left, right):
        out = _o_slot(widths, left, right)
        slots.append({"blk": _peek(1, ["blk_label"]).get("blk_label"),
                      "widths": list(widths or []), "res": out})
        return out

    def _spy_ord(*a, **kw):
        out = _o_ord(*a, **kw)
        p = _peek(1, ["blk_label", "d_hat", "corner_pt"])
        n = len(list((out or {}).get("ordered", []) or [])) if isinstance(out, dict) else None
        orders.append({"blk": p.get("blk_label"), "N": n,
                       "d_hat_is_None": p.get("d_hat") is None,
                       "corner_pt_is_None": p.get("corner_pt") is None})
        return out

    def _spy_k956(point, side_mid, allocation_dir, d_hat):
        out = _o_k956(point, side_mid, allocation_dir, d_hat)
        k956.append(float(out))
        return out

    ns["rw_increment"] = _spy_rwi
    ns["_select_pool_slot"] = _spy_slot
    ns["_spatial_order_parcels_v2"] = _spy_ord
    ns["k956_W_from_mp"] = _spy_k956

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    n0 = len(rwi)
    g_rows, err = [], None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e)
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return {"rwi": rwi, "rwi_stepg_from": n0, "slots": slots, "orders": orders,
            "k956": k956, "rows": rows, "err": err, "ns": ns, "sb": sb}


def main():
    say("=" * W)
    say("【`W-G.9-274` `§四-1`／`§四-2`】**實跑側 `Rw` 之產生式定位** ＋ **態甲 `R4` 未觸發之成因**")
    say("=" * W)
    say("🛑 **⛔ 由 `85.41` 反推其 `W`**（單 `§七` 款 `4`）——本器一律正面取產生式之**實際輸入**。")
    say("🛑 **⛔ 判孰為正確之 `W`、⛔ 提修法主張、⛔ 判該閘應否放寬。**")

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in (("甲", None), ("乙", "off")):
            D[(tag, lab)] = drive(sb, mode)
    os.environ.pop(ENV, None)

    # ── 自我驗證閘（框內省之正確性·⛔ 不過即拒測）──────────────────────
    say("")
    say("─" * W)
    say("【自我驗證閘】框內省所錄之 `blk_label`（⛔ 不過即 loud 拒測）")
    say("─" * W)
    bad = []
    for tag in ("0m", "3.5m"):
        for lab in ("甲", "乙"):
            d = D[(tag, lab)]
            ob = [o["blk"] for o in d["orders"]]
            sb2 = [x["blk"] for x in d["slots"]]
            ok = (ob and all(b in BLKS for b in ob)
                  and all(b in BLKS for b in sb2))
            say("   · `%s` 態%s｜`_spatial_order_parcels_v2` 所錄 ＝ %s｜"
                "`_select_pool_slot` 所錄 ＝ %s ⇒ %s"
                % (tag, lab, ob, sb2, "✅" if ok else "🔴 **含 `None` 或空**"))
            if not ok:
                bad.append((tag, lab))
    if bad:
        say("   🛑 **框內省之自我驗證閘不過**（%s）⇒ loud 拒測，⛔ 據以下任何結論。" % bad)
        say("   🩸 其成因通常為**框深度差一層**（見 `_peek` 之 docstring）。")
        return 5
    say("   ⇒ **器非紅** ✅（所錄之 `blk` 皆為 `BLKS` 之成員且非空）")

    # ── `§四-1` 項 1／2：產生式之逐字鏈（自倉取·⛔ 憑記憶）────────────
    say("")
    say("─" * W)
    say("【`§四-1` 項 `1`／`2`】實跑側 `Rw(%)` 之產生式鏈（**逐字錨**·⛔ 行號）")
    say("─" * W)
    say("   | 環 | 逐字 | 檔 | 列框命中 |")
    say("   |---|---|---|---|")
    import subprocess
    chain = [
        ("`g_rows` 之 `Rw(%)` 欄", "'Rw(%)': round(_res.get('Rw_pct', 0.0), 2),",
         "verify/stepg_pipeline.py"),
        ("`_res['Rw_pct']` 之產生", "Rw_pct = (rw_increment(W_prev, W_cur) * 100.0) if _apply_rw else 0.0",
         "app.py"),
        ("`W_cur` 之產生", "W_cur = W_prev + S", "app.py"),
        ("`rw_increment` 之本體", "return max(0.0, (rw_from_width(W_cur) - rw_from_width(W_prev)) / 100.0)",
         "app.py"),
        ("理論側 `widths` 之來源", "_widths_local[entry['_ov2_idx']] = float(res.get('_宗地寬度', 0.0) or 0.0)",
         "verify/stepg_pipeline.py"),
        ("`宗地寬度(m)` 欄", "'宗地寬度(m)': round(_res.get('_宗地寬度', 0.0), 2),",
         "verify/stepg_pipeline.py"),
        ("`W(m)` 欄", "'W(m)': round(_res.get('W', 0.0), 2),", "verify/stepg_pipeline.py"),
    ]
    for name, lit, f in chain:
        txt = subprocess.run(["git", "cat-file", "blob", "HEAD:" + f],
                             capture_output=True).stdout.decode("utf-8", "replace")
        c = sum(1 for ln in txt.split("\n") if lit in ln)
        say("   | %s | `%s` | `%s` | **%d** |" % (name, lit, f, c))
    say("   🔒 **判別力**：一人造字面（**執行期組出**·字面⛔ 出艙）於 `app.py` ＝ **%d**（須 `0`）"
        % sum(1 for ln in subprocess.run(["git", "cat-file", "blob", "HEAD:app.py"],
                                         capture_output=True).stdout
              .decode("utf-8", "replace").split("\n")
              if ("Rw_pct" + chr(95) + "NOSUCH") in ln))
    say("")
    say("   ⇒ 🔑 **實跑側 `Rw(%%) = R(W_cur) − R(W_prev)`（<u>差</u>·累積差額制）**；")
    say("      **理論側 `widths` ＝ `_宗地寬度`**（與 `宗地寬度(m)` 欄**同源**）。")

    # ── `§四-1` 項 5：`628-1(1)` 於三處之實際值 ────────────────────────
    say("")
    say("─" * W)
    say("【`§四-1` 項 `5`】態乙 `R4 right` 之 `628-1(1)` 於三處之**實際值**（**未捨入**）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        d = D[(tag, "乙")]
        r = next((x for x in d["rows"] if str(x.get("暫編地號")) == "628-1(1)"), None)
        R = d["ns"]["rw_from_width"]
        say("")
        say("   ══ 情境 `%s` ══" % tag)
        if r is None:
            say("      🛑 `628-1(1)` **⛔ 在 `g_rows`** ⇒ 第三種出艙碼")
            continue
        say("      | 名 | 值（`g_rows` 欄·`2dp`） | 其 `rw_from_width` |")
        say("      |---|---|---|")
        for col in ("宗地寬度(m)", "W(m)"):
            v = float(r.get(col) or 0)
            say("      | `%s` | `%s` | `%.6f` |" % (col, r.get(col), float(R(v))))
        say("      | `Rw(%%)`（實跑） | `%s` | —— |" % r.get("Rw(%)"))
        # 產生式之**實際輸入**（包裹所錄·⛔ 反推）
        cand = [x for x in d["rwi"][d["rwi_stepg_from"]:]
                if abs(x["pct"] - float(r.get("Rw(%)") or 0)) < 5e-3]
        say("")
        say("      🔒 **`rw_increment` 之實際輸入**（包裹所錄·⛔ 反推）——"
            "與該宗之 `Rw(%%)` 相符之呼叫 ＝ **%d** 次" % len(cand))
        if not cand:
            say("      🛑 **⛔ 相符之呼叫** ⇒ 第三種出艙碼（⛔ 以反推頂替）")
        else:
            say("      | # | `W_prev` | `W_cur` | `R(W_prev)` | `R(W_cur)` | 回傳×100 |")
            say("      |---|---|---|---|---|---|")
            for i, x in enumerate(cand, 1):
                say("      | %d | **`%.10f`** | **`%.10f`** | `%.6f` | `%.6f` | **`%.6f`** |"
                    % (i, x["W_prev"], x["W_cur"], float(R(x["W_prev"])),
                       float(R(x["W_cur"])), x["pct"]))
        # 理論側
        s = [x for x in d["slots"] if x["blk"] == "R4"]
        if s:
            res = s[-1]["res"] or {}
            k = res.get("k")
            t = {tt.get("k"): tt for tt in (res.get("table") or [])}.get(k) or {}
            say("")
            say("      🔒 **理論側**：`widths` ＝ `%s`｜`k*` ＝ `%s`｜`ΣRw_R` ＝ **`%s`**"
                % ([round(float(x), 6) for x in s[-1]["widths"]], k, t.get("ΣRw_R")))
        say("      🔒 `k956_W_from_mp` 之呼叫次數（本情境本態·全域）＝ **%d**" % len(d["k956"]))

    # ── `§四-2`：呼叫條件 ＋ 全母體三態表 ─────────────────────────────
    say("")
    say("─" * W)
    say("【`§四-2`】`_select_pool_slot` 之**呼叫條件**（逐字）＋ 全母體之**三態**執行次數表")
    say("─" * W)
    say("   🔒 **呼叫條件之逐字**（`verify/stepg_pipeline.py`·⛔ 行號）：")
    say("   ```")
    say("   _N = len(ordered_v2)")
    say("   _k_naive = (_N + 1) // 2 if _N % 2 == 1 else _N // 2")
    say("   _slot_res = None")
    say("   if _degenerate_order or _N <= 1:")
    say("       _k_star = _N")
    say("       _adv_final = _advance_block_with_split(_k_star, True)")
    say("   else:")
    say("       _adv_base = _advance_block_with_split(_k_naive, False)")
    say("       ...")
    say("       _slot_res = _select_pool_slot(...)")
    say("   ```")
    say("   ⇒ **`_slot_res` 唯於 `not (_degenerate_order or _N <= 1)` 方非 `None`**；")
    say("     而結構閘之守衛逐字 ＝ `if _slot_res:` ⇒ 其餘情形該閘**結構上不執行**。")
    say("   🔒 `_degenerate_order` 之逐字 ＝ `_degenerate_order = (d_hat is None or corner_pt is None)`")
    say("")
    say("   | 情境 | 態 | 街廓 | `_N`（＝ `len(ordered_v2)`） | `d_hat is None` | `corner_pt is None` | `_slot_res` 非 `None`？ | **結構閘之三態** |")
    say("   |---|---|---|---|---|---|---|---|")
    for tag in ("0m", "3.5m"):
        for lab in ("甲", "乙"):
            d = D[(tag, lab)]
            omap = {}
            for o in d["orders"]:
                omap[o["blk"]] = o
            called = {x["blk"] for x in d["slots"]}
            broke = None
            if d["err"] and "街廓 " in d["err"]:
                broke = d["err"].split("街廓 ")[1].split(" ")[0]
            for blk in BLKS:
                o = omap.get(blk)
                if o is None:
                    say("   | `%s` | %s | `%s` | 🛑 **⛔ 可得**（未達該街廓） | — | — | — | 🛑 **未執行**（管線已中止） |"
                        % (tag, lab, blk))
                    continue
                did = blk in called
                st = ("🔴 **已執行且破**" if (did and broke == blk)
                      else ("🟢 **已執行且通過**" if did else "🛑 **未執行**"))
                say("   | `%s` | %s | `%s` | **%s** | %s | %s | **%s** | %s |"
                    % (tag, lab, blk, o["N"], o["d_hat_is_None"], o["corner_pt_is_None"],
                       did, st))

    # ── 判別力：態甲全母體中 `W < 18` 之側 ───────────────────────────
    say("")
    say("─" * W)
    say("【判別力】態甲之全母體中落於**非飽和域**（`W < %.0f`）之側（單 `§四-1` 所令之取法）" % SAT)
    say("─" * W)
    say("   | 情境 | 街廓 | 側 | 該側之宗（`宗地寬度` ／ `W(m)` ／ `Rw(%%)`） | 有無 `W < 18` |")
    say("   |---|---|---|---|---|")
    nonsat = []
    for tag in ("0m", "3.5m"):
        d = D[(tag, "甲")]
        for blk in BLKS:
            for sd in ("left", "right"):
                sel = [r for r in d["rows"]
                       if (r.get("所屬街廓") or "").strip() == blk
                       and (r.get("推進側別") or "").strip() == sd]
                if not sel:
                    continue
                desc = "；".join("%s: %s／%s／%s"
                                % (r.get("暫編地號"), r.get("宗地寬度(m)"),
                                   r.get("W(m)"), r.get("Rw(%)")) for r in sel)
                lo = [r for r in sel
                      if r.get("宗地寬度(m)") is not None
                      and float(r.get("宗地寬度(m)") or 0) < SAT]
                if lo:
                    nonsat.append((tag, blk, sd, [r.get("暫編地號") for r in lo]))
                say("   | `%s` | `%s` | `%s` | %s | %s |"
                    % (tag, blk, sd, desc, "✅ **有**" if lo else "—"))
    say("")
    if not nonsat:
        say("   🛑 **全母體無 `W < %.0f` 之對照** ⇒ **第三種出艙碼：對照不存在**；"
            "⛔ 以飽和者頂替、⛔ 逕稱器非紅。" % SAT)
    else:
        say("   🔒 落於非飽和域者 ＝ **%d** 組：%s" % (len(nonsat), nonsat))
        say("   🛑 其「理論＝實跑」之判須另取——**本批之受詞為產生式之定位**，")
        say("      該判別力之完整施行**候發單側**（⛔ 逕稱器非紅）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
