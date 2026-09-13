# -*- coding: utf-8 -*-
"""`W-G.9-272` `§三-3`：**`K-9-29` 子項 `1` 之備料**（零生產碼·**⛔ 落地·僅備料**）。

🔒 以 harness 路徑走完**二態**，逐情境（`0m`／`3.5m`）出艙（單 `§三-3` 逐字）：
   `1` **配地宗逐宗表**（`暫編地號`／`原地號`／`所屬街廓`／`位次`／`G(㎡)`／`a 面積(㎡)`／
      `幾何面積(㎡)`／`街角側別`）；
   `2` **二態對拍**：`(a)` 只在一態出現者逐筆具名；`(b)` 二態皆有而 `G` 相異者逐筆具名其**未捨入差**；
      `(c)` 抵費地列之逐片面積二態對拍；
   `3` **守恆式**：`Σ配地幾何面積 ＋ Σ抵費地面積` vs `街廓面積`，二態**各自**成立與否（逐街廓）；
   `4` 重述 `W-G.9-271` 已測之分母 `51`／`53` 與差集 `['628-28','628-48']`，
      並補出艙**該二筆原地號之** `所屬街廓`／`歸戶`／`面積`。

| 態 | 環境 |
|---|---|
| 甲 | `WV_K6_STEP0` **未設**（＝預設 `on`·**現行生產態**） |
| 乙 | `WV_K6_STEP0=off` |

🛑 **準據**：二態須有差（分母已測 `51` vs `53`）；**⛔ 有差 ⇒ loud 停**（`rc != 0`）。
🛑 **⛔ 判孰為正確態、⛔ 提落地與否之主張、⛔ 動 `k6_step0_enabled` 之預設一字**
   ——僅以環境變數驅動既有出口。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9272_step0_ab.py [倉根]`
`rc`：`0`／`6` 二態⛔ 有差（loud 停）／`5` 量測器紅。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"                 # ＝ `app.py` 之 `K6_STEP0_ENV`（逐字）
W = 126
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
COLS = ["暫編地號", "原地號", "所屬街廓", "位次", "G(㎡)", "a 面積(㎡)", "幾何面積(㎡)", "街角側別"]
# 🔒 `W-G.9-271` 已測（**重述**·⛔ 重算）
WG271_DENOM = {"甲": 51, "乙": 53}
WG271_DIFF = ["628-28", "628-48"]


def say(s=""):
    print(s)


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def drive(sb, mode):
    """`mode` ＝ `None`（態甲·未設）／`"off"`（態乙）。回 (rows, 街廓面積, 抵費地片, temp, groups)。"""
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
    pool = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label="", _depth=None, _verbose=True):
        out = _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                    _label=_label, _depth=_depth, _verbose=_verbose)
        pool[str(_label)] = {"blk_area": float(block_poly.area),
                             "pieces": [float(g.area) for g in out]}
        return out                  # 🛑 逐位原樣回傳

    ns["_pool_strips_for_block"] = _spy
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    groups = dict(fake_st.session_state.get("t8_ownership_groups") or {})
    own_map = dict(fake_st.session_state.get("t8_ownership_map") or {})
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    g_rows = []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return rows, pool, temp_p, groups, own_map


def main():
    say("=" * W)
    say("【`W-G.9-272` `§三-3`】**`K-9-29` 子項 `1` 之備料**（⛔ 落地·僅備料）")
    say("=" * W)
    say("🛑 **⛔ 判孰為正確態、⛔ 提落地與否之主張、⛔ 動 `k6_step0_enabled` 之預設一字。**")

    data = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in (("甲", None), ("乙", "off")):
            rows, pool, temp_p, groups, own_map = drive(sb, mode)
            data[(tag, lab)] = (rows, pool, temp_p, groups, own_map)
    os.environ.pop(ENV, None)       # 🔒 還原（⛔ 遺留）

    # 欄之在否（⛔ 靜默缺欄）
    sample = data[("0m", "甲")][0]
    have = set(sample[0].keys()) if sample else set()
    say("")
    say("🔒 `g_rows` 之欄（**正面列舉單所令之 `8` 欄**·⛔ 靜默缺欄）")
    for c in COLS:
        say("   %-14s ⇒ %s" % ("`" + c + "`", "✅ 在" if c in have else "🛑 **⛔ 在**（具名·⛔ 以他欄代之）"))
    miss = [c for c in COLS if c not in have]
    if miss:
        say("   🛑 缺欄 ＝ %s ⇒ 其格一律印 `（⛔ 在）`，**⛔ 以近義欄頂替**" % miss)

    rc = 0
    for sb in SBS:
        tag = "%gm" % sb
        say("")
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        for lab in ("甲", "乙"):
            rows, pool, temp_p, groups, own_map = data[(tag, lab)]
            biz = [r for r in rows if (r.get("推進側別") or "").strip() in ("left", "right")]
            say("")
            say("   ══ 態 %s（`%s` %s）══  `g_rows` %d 列｜配地宗 **%d**｜間諜所錄街廓 %d"
                % (lab, ENV, "未設（生產態）" if lab == "甲" else "= off",
                   len(rows), len(biz), len(pool)))
            say("   | %s |" % " | ".join(COLS))
            say("   |%s|" % "|".join(["---"] * len(COLS)))
            for r in sorted(biz, key=lambda x: (str(x.get("所屬街廓")), str(x.get("暫編地號")))):
                say("   | %s |" % " | ".join(
                    ("`%s`" % r.get(c)) if c in have else "（⛔ 在）" for c in COLS))

        # ── `2` 二態對拍 ──────────────────────────────────────────────
        ra = {str(r.get("暫編地號")): r for r in data[(tag, "甲")][0]
              if (r.get("推進側別") or "").strip() in ("left", "right")}
        rb = {str(r.get("暫編地號")): r for r in data[(tag, "乙")][0]
              if (r.get("推進側別") or "").strip() in ("left", "right")}
        say("")
        say("   ── `2(a)` 只在一態出現者（逐筆具名）")
        oa = sorted(set(ra) - set(rb))
        ob = sorted(set(rb) - set(ra))
        say("      甲∖乙 ＝ **%d** 筆：%s" % (len(oa), oa))
        say("      乙∖甲 ＝ **%d** 筆：%s" % (len(ob), ob))
        say("")
        say("   ── `2(b)` 二態皆有而 `G` 相異者（**未捨入差**）")
        both = sorted(set(ra) & set(rb))
        diffs = []
        for k in both:
            ga, gb = fnum(ra[k].get("G(㎡)")), fnum(rb[k].get("G(㎡)"))
            if ga is None or gb is None:
                say("      🛑 `%s` 之 `G` **⛔ 可得** ⇒ 具名（⛔ 以 `0` 代之）" % k)
                continue
            if ga != gb:
                diffs.append((k, ga, gb))
        say("      二態皆有 ＝ %d 筆；`G` 相異 ＝ **%d** 筆" % (len(both), len(diffs)))
        if diffs:
            say("      | 暫編地號 | 態甲 `G` | 態乙 `G` | **未捨入差（甲 − 乙）** |")
            say("      |---|---|---|---|")
            for k, ga, gb in diffs:
                say("      | `%s` | %.10f | %.10f | **%+.10f** |" % (k, ga, gb, ga - gb))
        say("")
        say("   ── `2(c)` 抵費地列之逐片面積（間諜所錄之池片·二態對拍）")
        pa, pb = data[(tag, "甲")][1], data[(tag, "乙")][1]
        say("      | 街廓 | 態甲 片數 | 態甲 逐片面積(㎡) | 態乙 片數 | 態乙 逐片面積(㎡) | Σ甲 − Σ乙 |")
        say("      |---|---|---|---|---|---|")
        for blk in BLKS:
            A = pa.get(blk)
            B = pb.get(blk)
            if not A or not B:
                say("      | `%s` | %s | %s | %s | %s | 🛑 **⛔ 可得** |"
                    % (blk, len(A["pieces"]) if A else "⛔ 在", "", len(B["pieces"]) if B else "⛔ 在", ""))
                continue
            say("      | `%s` | %d | %s | %d | %s | **%+.4f** |"
                % (blk, len(A["pieces"]), ", ".join("%.4f" % x for x in A["pieces"]),
                   len(B["pieces"]), ", ".join("%.4f" % x for x in B["pieces"]),
                   sum(A["pieces"]) - sum(B["pieces"])))

        # ── `3` 守恆式 ────────────────────────────────────────────────
        say("")
        say("   ── `3` 守恆式：`Σ配地幾何面積 ＋ Σ抵費地面積` vs `街廓面積`（二態各自·逐街廓）")
        say("      | 街廓 | 態 | Σ配地幾何 | Σ池片 | 合計 | 街廓面積 | 殘差 | 成立（|殘差| ≤ 0.01）|")
        say("      |---|---|---|---|---|---|---|---|")
        for blk in BLKS:
            for lab in ("甲", "乙"):
                rows, pool, _t, _g, _o = data[(tag, lab)]
                P = pool.get(blk)
                if not P:
                    say("      | `%s` | %s | —— | —— | —— | —— | —— | 🛑 **⛔ 可得** |" % (blk, lab))
                    continue
                sg = 0.0
                for r in rows:
                    if (r.get("所屬街廓") or "").strip() != blk:
                        continue
                    if (r.get("推進側別") or "").strip() not in ("left", "right"):
                        continue
                    v = fnum(r.get("幾何面積(㎡)"))
                    if v is not None:
                        sg += v
                sp = sum(P["pieces"])
                resid = (sg + sp) - P["blk_area"]
                say("      | `%s` | %s | %.4f | %.4f | %.4f | %.4f | **%+.4f** | %s |"
                    % (blk, lab, sg, sp, sg + sp, P["blk_area"], resid,
                       "🟢" if abs(resid) <= 0.01 else "🔴"))

    # ── `4` 分母與差集之重述 ＋ 二筆原地號之補出艙 ──────────────────────
    say("")
    say("─" * W)
    say("【`4`　`W-G.9-271` 已測之分母與差集（**重述**·⛔ 重算）＋ 二筆原地號之補出艙】")
    say("─" * W)
    say("   `W-G.9-271 §四` 已測：態甲 分母 **%d**／態乙 **%d**；差集（乙∖甲）＝ **%s**"
        % (WG271_DENOM["甲"], WG271_DENOM["乙"], WG271_DIFF))
    rows_b, _p, temp_b, groups_b, own_b = data[("0m", "乙")]
    say("")
    say("   | 原地號 | 所屬街廓 | 歸戶（`gid`） | `temp_parcels` 內之筆數 | Σ登記面積 | Σ幾何面積 | Σ分攤登記面積 |")
    say("   |---|---|---|---|---|---|---|")
    for op in WG271_DIFF:
        sel = [tp for tp in temp_b if str(tp.get("原地號")) == op]
        blks = sorted({str(tp.get("所屬街廓")) for tp in sel})
        gid = own_b.get(op, "🛑 **⛔ 在 `t8_ownership_map`**")

        def s(key):
            t = 0.0
            for tp in sel:
                v = fnum(tp.get(key))
                if v is not None:
                    t += v
            return t
        say("   | `%s` | %s | `%s` | %d | %.4f | %.4f | %.4f |"
            % (op, "／".join("`%s`" % b for b in blks) or "🛑 **⛔ 可得**", gid, len(sel),
               s("登記面積_m2"), s("幾何面積_m2"), s("分攤登記面積_m2")))
    say("")
    say("   🔒 其**歸戶內之其他原地號**（供對照·⛔ 判其應否合併）：")
    for op in WG271_DIFF:
        gid = own_b.get(op)
        if gid is None:
            continue
        mem = sorted(groups_b.get(gid, []))
        say("      · `%s` ⇒ `gid` ＝ `%s`｜該戶之原地號 ＝ %s" % (op, gid, mem))

    # ── 準據 ──────────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【🛑 準據：二態須有差】")
    say("─" * W)
    any_diff = False
    for sb in SBS:
        tag = "%gm" % sb
        ra = {str(r.get("暫編地號")) for r in data[(tag, "甲")][0]
              if (r.get("推進側別") or "").strip() in ("left", "right")}
        rb = {str(r.get("暫編地號")) for r in data[(tag, "乙")][0]
              if (r.get("推進側別") or "").strip() in ("left", "right")}
        d = (ra != rb)
        say("   情境 `%s`：配地宗之暫編地號集合 甲 %d／乙 %d ⇒ 相異 ＝ **%s**"
            % (tag, len(ra), len(rb), d))
        any_diff = any_diff or d
    say("   ⇒ %s" % ("🟢 **二態有差**（如期）" if any_diff else "🔴 **二態⛔ 有差**"))
    if not any_diff:
        say("   🛑 **loud 停**（`rc = 6`）——⛔ 靜默續。")
        return 6
    return rc


if __name__ == "__main__":
    sys.exit(main())
