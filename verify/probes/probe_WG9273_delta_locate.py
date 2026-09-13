# -*- coding: utf-8 -*-
"""`W-G.9-273` `§四-1`／`§四-2`／`§四-4`：**`Δ=2.425` 之值空間定位**（零生產碼·出艙即止）。

🛑 **⛔ 以 commit 空間二分跨越之**（其前提「全序可判」不成立）⇒ **值空間定位**：
   自**可求值之二端點**對拍，逐項縮小受詞。**準據由發單側明定**（單 `§四-1`）·⛔ CC 自訂。

🔒 **二端點**
   · **端點 A（可求值）** ＝ 態甲（`WV_K6_STEP0` 未設）之 `R4 right`——結構閘**未破**；
   · **端點 B（破）** ＝ 態乙（`WV_K6_STEP0=off`）之 `R4 right`——
     `理論@k*=87.83`／`實跑(階段1)=85.41`／`Δ=2.425`。

🔒 **量之取法（⛔ 另寫第二份判準）**
   · `理論@k*` ＝ **間諜所錄之 `ns["_select_pool_slot"]` 回傳**之 `table` 中 `k == k*` 之列
     之 `ΣRw_L`／`ΣRw_R`（＝ `verify/stepg_pipeline.py` 之 `_t_star` 同源）；
     其 `blk_label` 由**呼叫端框之區域變數**讀出（唯讀內省·⛔ 改碼）。
   · `實跑(階段1)` ＝ 以 `_rw_stage1_only` 之**逐字式**施於 `g_rows` 之同街廓列
     （`g_rows.extend(_adv_final['rows'])` ⇒ **同一物件**·⛔ 第二份判準）：
       `round(Σ Rw(%) | 推進側別==side ∧ F(m)>0 ∧ 暫編地號 ∉ _stage2_ids, 2)`；
     `_stage2_ids` 取自**同一資料驅動出處** `'配地階段' in tp`（`stepg_pipeline` 逐字）。
   · **界面** ＝ 生產所印之 `[Δ_i·<blk>·<side>·階段1]` 列（**逐字擷取**·⛔ 器內重算）。

🛑 **自我驗證閘（碼面自身之保證·`CLAUDE.md` 明令）**
   `(i)` 端點 B 之 `理論@k*` 須 ＝ **`87.83`** ⋀ `實跑` 須 ＝ **`85.41`**（**逐位**·碼面之 raise 所斷言）；
   `(ii)` 其餘三格（態甲 `right`／態甲 `left`／態乙 `left`）須 `|理論 − 實跑| ≤ 0.1`（閘已過）。
   ⛔ 不過 ⇒ `rc = 5` **loud 拒測**，**⛔ 據以下任何結論**。

🛑 **⛔ 判孰誤、⛔ 提修法主張、⛔ 判該閘應否放寬**——出艙即止。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9273_delta_locate.py [倉根]`
`rc`：`0`／`3` 母體為 `0`／`5` **量測器紅**。
"""
import contextlib
import hashlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 128
SBS = (0.0, 3.5)
BLK = "R4"
SIDES = ("left", "right")
# 🔒 碼面之 raise 所斷言之二值（**自我驗證閘之受詞**·⛔ CC 自訂）
ASSERT_B = {"理論": 87.83, "實跑": 85.41}
COLS5 = ["暫編地號", "原地號", "所屬街廓", "位次", "G(㎡)", "a 面積(㎡)", "幾何面積(㎡)",
         "街角側別", "第1筆街角", "宗地寬度(m)", "Rw(%)", "F(m)", "W(m)", "推進側別", "累積S(m)"]


def say(s=""):
    print(s)


def drive(sb, mode):
    """一情境一態。回 dict（含 slot 間諜、pool 間諜、`g_rows`、`build_p`、stdout）。"""
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
    slots = []
    pool = {}
    _orig_slot = ns["_select_pool_slot"]
    _orig_pool = ns["_pool_strips_for_block"]

    def _spy_slot(widths, left, right):
        out = _orig_slot(widths, left, right)
        # 🔒 唯讀內省：自呼叫端框取 `blk_label`（⛔ 改碼、⛔ 以序號推定）
        lab = None
        try:
            lab = sys._getframe(1).f_locals.get("blk_label")
        except Exception:                                           # noqa: BLE001
            raise                       # 🛑 ⛔ 靜默吞
        slots.append({"blk": lab, "widths": list(widths or []),
                      "left": dict(left or {}), "right": dict(right or {}),
                      "res": out})
        return out                      # 🛑 逐位原樣回傳

    def _spy_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                  _label="", _depth=None, _verbose=True):
        out = _orig_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                         _label=_label, _depth=_depth, _verbose=_verbose)
        pool[str(_label)] = {"poly": block_poly, "d_hat": d_hat, "corner_pt": corner_pt,
                             "alloc": allocation_dir, "biz": list(biz_polys or []),
                             "pieces": list(out)}
        return out

    ns["_select_pool_slot"] = _spy_slot
    ns["_pool_strips_for_block"] = _spy_pool

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    own_map = dict(fake_st.session_state.get("t8_ownership_map") or {})
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    buf = io.StringIO()
    g_rows, err = [], None
    try:
        with contextlib.redirect_stdout(buf):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e)
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return {"slots": slots, "pool": pool, "rows": rows, "build_p": build_p,
            "params": params, "out": buf.getvalue(), "err": err,
            "own_map": own_map, "sb": sb, "ns": ns}


def theo(d, blk, side):
    """`理論@k*`（＝ `_t_star['ΣRw_L'|'ΣRw_R']`·間諜所錄之同源）。回 (值, k*, 診斷)。"""
    hits = [s for s in d["slots"] if s["blk"] == blk]
    if not hits:
        # 🛑 **第三種出艙碼**：⛔ 與「鍵缺」共用（⛔ 「無從判定」＝「判定為偽」）
        return None, None, "未呼叫"
    s = hits[-1]
    res = s["res"] or {}
    k = res.get("k")
    tbl = {t.get("k"): t for t in (res.get("table") or [])}
    t = tbl.get(k) or {}
    key = "ΣRw_L" if side == "left" else "ΣRw_R"
    if key not in t:
        return None, k, "鍵缺:%s" % sorted(t)
    return float(t[key] or 0.0), k, "可得(呼叫 %d 次·取末一次)" % len(hits)


def real(d, blk, side):
    """`實跑(階段1)`（`_rw_stage1_only` 之**逐字式**·施於 `g_rows` 同街廓列）。"""
    s2 = {tp["暫編地號"] for tp in d["build_p"]
          if str(tp.get("所屬街廓")) == blk and "配地階段" in tp}
    tot = 0.0
    used = []
    for r in d["rows"]:
        if (r.get("所屬街廓") or "").strip() != blk:
            continue
        if (r.get("推進側別") or "").strip() != side:
            continue
        if float(r.get("F(m)", 0) or 0) <= 0:
            continue
        if r.get("暫編地號") in s2:
            continue
        v = float(r.get("Rw(%)", 0) or 0)
        tot += v
        used.append((r.get("暫編地號"), v))
    return round(tot, 2), used, sorted(s2)


def ifaces(d, blk, side):
    """生產所印之 `[Δ_i·<blk>·<side>·階段1]` 列（**逐字擷取**·⛔ 器內重算）。"""
    tag = "[Δ_i·%s·%s·階段1]" % (blk, side)
    for ln in d["out"].split("\n"):
        if ln.strip().startswith(tag):
            body = ln.strip()[len(tag):].strip()
            if body.startswith("（無界面）"):
                return 0, 0.0, body
            n = len(re.findall(r"Δ=([+-][\d.]+)", body))
            ssum = sum(float(x) for x in re.findall(r"／Δ=([+-][\d.]+)／", body))
            return n, ssum, body
    return None, None, "🛑 該列**⛔ 在 stdout**（其框逐字 ＝ `%s`）" % tag


def main():
    say("=" * W)
    say("【`W-G.9-273` `§四-1`】**`Δ=2.425` 之值空間定位**（⛔ 二分·出艙即止）")
    say("=" * W)
    say("🛑 **⛔ 判孰誤、⛔ 提修法主張、⛔ 判該閘應否放寬。**")

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in (("甲", None), ("乙", "off")):
            D[(tag, lab)] = drive(sb, mode)
    os.environ.pop(ENV, None)

    # ── 自我驗證閘 ────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【自我驗證閘】（碼面自身之保證·⛔ 不過即拒測）")
    say("─" * W)
    d0a, d0b = D[("0m", "甲")], D[("0m", "乙")]
    tB, kB, dgB = theo(d0b, BLK, "right")
    rB, _u, _s2 = real(d0b, BLK, "right")
    say("   `(i)` 端點 B（`0m` 態乙 `R4 right`）：理論@k* 實得 **%s**（期 `%s`）／"
        "實跑 實得 **%s**（期 `%s`）"
        % (tB, ASSERT_B["理論"], rB, ASSERT_B["實跑"]))
    ok_i = (tB is not None and abs(tB - ASSERT_B["理論"]) < 5e-3
            and abs(rB - ASSERT_B["實跑"]) < 5e-3)
    say("        ⇒ %s" % ("✅ 逐位相符" if ok_i else "🔴 **⛔ 相符**"))
    say("   🔒 **間諜所錄之 `_select_pool_slot` 呼叫**（母體之正面列舉）")
    for tg in ("0m", "3.5m"):
        for lb in ("甲", "乙"):
            blks = [x["blk"] for x in D[(tg, lb)]["slots"]]
            say("      · `%s` 態%s ⇒ **%d** 次：%s" % (tg, lb, len(blks), blks))
    ok_ii = True
    n_ok, n_third = 0, 0
    for (tg, lb, sd) in (("0m", "甲", "right"), ("0m", "甲", "left"), ("0m", "乙", "left")):
        t, k, dg = theo(D[(tg, lb)], BLK, sd)
        r, _u2, _s3 = real(D[(tg, lb)], BLK, sd)
        if dg == "未呼叫":
            n_third += 1
            say("   `(ii)` `%s` 態%s `%s`：🛑 **第三種出艙碼**——`_select_pool_slot` 於該街廓"
                "**未被呼叫** ⇒ 其結構閘（`if _slot_res:`）**結構上不執行**；"
                "⛔ 量測器紅、⛔ 判定為偽。實跑(階段1) ＝ %s（**照實**）" % (tg, lb, sd, r))
            continue
        if dg.startswith("鍵缺"):
            ok_ii = False
            say("   `(ii)` `%s` 態%s `%s`：🔴 **量測器紅**——`_t_star` 之鍵缺（%s）" % (tg, lb, sd, dg))
            continue
        good = abs(t - r) <= 0.1
        ok_ii = ok_ii and good
        n_ok += 1
        say("   `(ii)` `%s` 態%s `%s`：理論 %s／實跑 %s ⇒ |Δ| = %.3f ⇒ %s（%s）"
            % (tg, lb, sd, t, r, abs(t - r), "✅" if good else "🔴", dg))
    say("   🔒 **判別力**：可得之對照格 ＝ **%d**（須 ≥ 1·否則先判量測器紅）／"
        "第三種出艙碼 ＝ **%d**" % (n_ok, n_third))
    if n_ok < 1:
        ok_ii = False
    if not (ok_i and ok_ii):
        say("   🛑 **自我驗證閘不過 ⇒ loud 拒測**，⛔ 據以下任何結論。")
        return 5
    say("   ⇒ **器非紅** ✅（重建之二量與碼面之斷言逐位相符，且未破側之 |Δ| ≤ 0.1）")

    # ── 逐項並列 ─────────────────────────────────────────────────────
    for sb in SBS:
        tag = "%gm" % sb
        say("")
        say("─" * W)
        say("【情境 `退縮 %s`】逐項並列（端點 A ＝ 態甲／端點 B ＝ 態乙·⛔ 二分）" % tag)
        say("─" * W)
        for sd in SIDES:
            mark = "🔑 **受詞**" if sd == "right" else "🔒 **判別力對照**（二態皆未破）"
            say("")
            say("   ══ `%s %s` ══  %s" % (BLK, sd, mark))
            say("   | 項 | 受詞 | 態甲（端點 A） | 態乙（端點 B） | 差（未捨入） |")
            say("   |---|---|---|---|---|")
            A, B = D[(tag, "甲")], D[(tag, "乙")]
            # `1` 宗序列
            def seq(d):
                return [r.get("暫編地號") for r in d["rows"]
                        if (r.get("所屬街廓") or "").strip() == BLK
                        and (r.get("推進側別") or "").strip() == sd]
            sa, sb2 = seq(A), seq(B)
            say("   | `1` | `%s %s` 之宗序列（推進序）｜筆數 | %s｜**%d** | %s｜**%d** | — |"
                % (BLK, sd, sa, len(sa), sb2, len(sb2)))
            # `2` 逐宗
            def per(d):
                o = []
                for r in d["rows"]:
                    if (r.get("所屬街廓") or "").strip() != BLK:
                        continue
                    if (r.get("推進側別") or "").strip() != sd:
                        continue
                    o.append("%s: G=%s W宗=%s 累積S=%s Rw=%s F=%s"
                             % (r.get("暫編地號"), r.get("G(㎡)"), r.get("宗地寬度(m)"),
                                r.get("累積S(m)"), r.get("Rw(%)"), r.get("F(m)")))
                return o
            say("   | `2` | 逐宗 `G`／`宗地寬度`／`累積S`／`Rw`／`F` | %s | %s | — |"
                % ("<br>".join(per(A)) or "（空）", "<br>".join(per(B)) or "（空）"))
            # `3` k*
            ta, ka, dga = theo(A, BLK, sd)
            tb, kb, dgb = theo(B, BLK, sd)
            say("   | `3` | **`k*`**｜`理論@k*` | `k*` ＝ **%s**｜%s | `k*` ＝ **%s**｜%s | k* 差 %s／理論差 %s |"
                % (ka, ta, kb, tb,
                   (kb - ka) if (ka is not None and kb is not None) else "——",
                   ("%+.4f" % (tb - ta)) if (ta is not None and tb is not None) else "——"))
            # `3'` k* 之輸入
            def sin(d):
                h = [s for s in d["slots"] if s["blk"] == BLK]
                if not h:
                    return "🛑 ⛔ 錄到"
                s = h[-1]
                return ("`widths`（**%d**）＝ %s<br>`left` ＝ %s<br>`right` ＝ %s"
                        % (len(s["widths"]),
                           [round(float(x), 4) for x in s["widths"]],
                           {k: (round(float(v), 6) if isinstance(v, (int, float)) else v)
                            for k, v in s["left"].items()},
                           {k: (round(float(v), 6) if isinstance(v, (int, float)) else v)
                            for k, v in s["right"].items()}))
            say("   | `3′` | `_select_pool_slot` 之**各輸入**逐項 | %s | %s | — |"
                % (sin(A), sin(B)))
            # `4` 實跑累積式逐項
            ra, ua, s2a = real(A, BLK, sd)
            rb, ub, s2b = real(B, BLK, sd)
            def acc(u):
                t = 0.0
                o = []
                for nm, v in u:
                    t += v
                    o.append("%s +%s → %.2f" % (nm, v, t))
                return "<br>".join(o) or "（空·Σ ＝ 0.00）"
            say("   | `4` | **實跑(階段1)** 之累積式逐項（`Rw(%%)` 之逐步累加） | %s<br>**Σ ＝ %.2f** | %s<br>**Σ ＝ %.2f** | **%+.4f** |"
                % (acc(ua), ra, acc(ub), rb, rb - ra))
            say("   | `4′` | `_stage2_ids`（`'配地階段' in tp`·資料驅動） | %s | %s | — |"
                % (s2a or "（空）", s2b or "（空）"))
            # `5` 界面
            na, sma, bda = ifaces(A, BLK, sd)
            nb, smb, bdb = ifaces(B, BLK, sd)
            say("   | `5` | **界面數**（框逐字 ＝ `[Δ_i·%s·%s·階段1]`） | **%s** | **%s** | — |"
                % (BLK, sd, na, nb))
            say("   | `5′` | 該列之**逐字** | `%s` | `%s` | — |" % (bda, bdb))
            # `6` ΣΔ_i
            say("   | `6` | `ΣΔ_i`（🛑 碼註逐字：「**⛔ 未用於本式**·實測反證見碼註」） | **%s** | **%s** | — |"
                % (("%+.4f" % sma) if sma is not None else "——",
                   ("%+.4f" % smb) if smb is not None else "——"))
            # 判
            if ta is not None and tb is not None:
                say("   | **判** | `|理論 − 實跑|`（容差 `_IFACE_TOL` ＝ `0.1`·⛔ 器內另定） | **%.3f** %s | **%.3f** %s | — |"
                    % (abs(ta - ra), "🟢" if abs(ta - ra) <= 0.1 else "🔴",
                       abs(tb - rb), "🟢" if abs(tb - rb) <= 0.1 else "🔴"))

    # ── `§四-2` 態乙 `R4` 逐片二情境逐位相同之成因 ────────────────────
    say("")
    say("─" * W)
    say("【`§四-2`】態乙 `R4` 逐片面積二情境**逐位相同**之成因（🛑 出艙即止·⛔ 判其為缺陷）")
    say("─" * W)
    say("   | 態 | 情境 | `setback` 實際取值（`params` 內之逐字） | `blk_poly` 面積／質心（逐位） | `blk_poly` WKB `sha256` | 逐片面積 |")
    say("   |---|---|---|---|---|---|")
    for lab in ("甲", "乙"):
        for sb in SBS:
            tag = "%gm" % sb
            d = D[(tag, lab)]
            P = d["pool"].get(BLK)
            if not P:
                say("   | %s | `%s` | %s | 🛑 **⛔ 可得**（間諜未錄 `%s`） | —— | —— |"
                    % (lab, tag, d["sb"], BLK))
                continue
            g = P["poly"]
            c = g.centroid
            say("   | %s | `%s` | `%s` | `%.10f` ／ `(%.10f, %.10f)` | `%s` | %s |"
                % (lab, tag, d["sb"], float(g.area), float(c.x), float(c.y),
                   hashlib.sha256(g.wkb).hexdigest()[:32],
                   ", ".join("%.4f" % float(x.area) for x in P["pieces"])))
    say("")
    say("   🔒 **中止之時點**（逐字·`err`）")
    for lab in ("甲", "乙"):
        for sb in SBS:
            tag = "%gm" % sb
            e = D[(tag, lab)]["err"]
            say("      · 態%s `%s`：%s" % (lab, tag, ("**未 raise**" if not e else "`%s`" % e[:190])))
    say("   🔒 **`setback` 生效之時點**：`params` ＝ `build_param_table(…, setback)`，"
        "其於 `run_step_g` **之前**已算畢 ⇒ **中止發生於 `setback` 生效<u>之後</u>**（照實·⛔ 推定）。")

    # ── `§四-4` `R4` 二態逐宗全欄 ────────────────────────────────────
    say("")
    say("─" * W)
    say("【`§四-4`】`R4` 二態**逐宗全欄**之出艙（供發單側轉土地語言·🛑 ⛔ 判、⛔ 呈 KL）")
    say("─" * W)
    have = set(D[("0m", "甲")]["rows"][0].keys()) if D[("0m", "甲")]["rows"] else set()
    miss = [c for c in COLS5 if c not in have]
    say("   🔒 欄之在否（**正面列舉**·⛔ 靜默缺欄）：缺欄 ＝ %s" % (miss or "（無）"))
    for sb in SBS:
        tag = "%gm" % sb
        for lab in ("甲", "乙"):
            d = D[(tag, lab)]
            sel = [r for r in d["rows"] if (r.get("所屬街廓") or "").strip() == BLK]
            say("")
            say("   ══ `%s` 態%s ══ `%s` 之列 ＝ **%d**" % (tag, lab, BLK, len(sel)))
            say("   | %s | 歸戶 | 強制抵費地(片數／面積) |" % " | ".join(COLS5))
            say("   |%s|---|---|" % "|".join(["---"] * len(COLS5)))
            P = d["pool"].get(BLK)
            pdesc = (", ".join("%.4f" % float(x.area) for x in P["pieces"])
                     if P else "🛑 ⛔ 可得")
            for r in sel:
                gid = d["own_map"].get(str(r.get("原地號")), "（⛔ 在 `t8_ownership_map`）")
                say("   | %s | `%s` | %s |"
                    % (" | ".join(("`%s`" % r.get(c)) if c in have else "（⛔ 在）"
                                  for c in COLS5), gid,
                       "%d 片：%s" % (len(P["pieces"]), pdesc) if P else pdesc))
    say("")
    say("   🔒 `628-28`／`628-48`（`W-G.9-271` 之差集）之補出艙")
    d = D[("0m", "乙")]
    say("   | 原地號 | 所屬街廓 | 歸戶 | `build_p` 內之筆數 | Σ登記面積 | Σ幾何面積 | Σ分攤登記面積 |")
    say("   |---|---|---|---|---|---|---|")
    for op in ("628-28", "628-48"):
        s = [tp for tp in d["build_p"] if str(tp.get("原地號")) == op]
        def tot(k):
            return sum(float(tp.get(k, 0) or 0) for tp in s)
        say("   | `%s` | %s | `%s` | %d | %.4f | %.4f | %.4f |"
            % (op, "／".join(sorted({str(tp.get("所屬街廓")) for tp in s})) or "🛑 ⛔ 可得",
               d["own_map"].get(op, "（⛔ 在）"), len(s),
               tot("登記面積_m2"), tot("幾何面積_m2"), tot("分攤登記面積_m2")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
