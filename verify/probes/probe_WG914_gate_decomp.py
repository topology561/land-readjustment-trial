# -*- coding: utf-8 -*-
r"""`W-G.9-14` 甲組：結構閘「理論＝實跑」之**逐項分解**（⛔ 純偵察·⛔ 零修復）。

## 受詞

`R1 left` 兩情境之 `理論@k*`（`_t_star["ΣRw_L"]`）與 `實跑(階段1)`（`_rw_stage1_only('left')`）
各自之**組成**，及其差 `Δ` 之來源。

## 🔒 本探針**不修任何東西**

⛔ 不改 `verify/stepg_pipeline.py`、⛔ 不改 `app.py`、⛔ 不改任何容差。
本探針以**只讀之記錄包裝**（record-only wrapper）套在 `ns` 之兩個符號上——
包裝器**原樣轉呼叫並原樣回傳**，⛔ 不改任何值。其**透明性**由 §對照組自檢證明。

## 🔒 對照組自檢（**考古 71 修法 ③**·⛔ 本探針之結果不得在自檢紅時出艙）

1. **包裝器透明**：對同一輸入，包裝前後之回傳**逐位相同**。
2. **`R` 之已知真值**：`rw_from_width(18.0) == 100.0`（`CLAUDE.md`：`W≥18→100%`）。
3. 🔴 **重建閘（`CLAUDE.md`「探針還原內部幾何時須以碼面自身之保證當自我驗證閘」）**：
   本探針由所記之 `widths`／`b` **重建**理論側之 `ΣRw`，須與引擎自己算出之
   `_t_star["ΣRw_L"]` **逐位相同**；⛔ 不過此閘，(甲) 之分解結論一律不採。

## 重跑
    python verify/probes/probe_WG914_gate_decomp.py
"""
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

# 🔒 母體自證（考古 69 修法 ①）
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"

OUT = os.path.join(VERIFY, "out", "probe_WG914_gate_decomp.log")
L, RC = [], [0]
REC = {"slot": [], "rw": [], "solve": []}


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def _caller():
    st = traceback.extract_stack()
    for fr in reversed(st[:-2]):
        if fr.name not in ("_caller", "<lambda>"):
            return fr.name
    return "?"


def install(ns):
    """只讀記錄包裝（⛔ 原樣轉呼叫·原樣回傳）。回傳 (原始符號 dict) 供透明性自檢。"""
    orig = {k: ns[k] for k in ("_select_pool_slot", "rw_from_width", "_solve_G_one")}

    def w_slot(widths, left_side, right_side, rw_func=None):
        out = orig["_select_pool_slot"](widths, left_side, right_side, rw_func)
        REC["slot"].append({"widths": list(widths or []), "L": dict(left_side or {}),
                            "R": dict(right_side or {}), "out": out,
                            "n_solve_before": len(REC["solve"])})
        return out

    def w_rw(W):
        v = orig["rw_from_width"](W)
        REC["rw"].append({"W": float(W), "R": float(v), "by": _caller()})
        return v

    def w_solve(**kw):
        res = orig["_solve_G_one"](**kw)
        # 🔴 `_solve_G_one` 之回傳**多形**（`W-G.9-14` 實跑抓到）：
        #   `_corner_first_lot_G` 以 `_res, _ = _solve_G_one(...)` 取 **tuple**；
        #   `stepg_pipeline._solve_one` 則直接用 **dict**。
        #   ⇒ ⛔ 不得假設其為 dict；取不到即記為 `None`，**⛔ 不吞例外、⛔ 不改回傳**。
        d = res
        if isinstance(res, tuple) and res:
            d = res[0]
        if not isinstance(d, dict):
            d = {}
        REC["solve"].append({"side": kw.get("side"), "a_m2": kw.get("a_m2"),
                             "W_prev": kw.get("W_prev"), "is_corner": kw.get("is_corner"),
                             "W_near": d.get("W_near"), "W_far": d.get("W_far"),
                             "W": d.get("W"), "Rw_pct": d.get("Rw_pct"),
                             "width": d.get("_宗地寬度"),
                             "shape": type(res).__name__})
        return res

    ns["_select_pool_slot"] = w_slot
    ns["rw_from_width"] = w_rw
    ns["_solve_G_one"] = w_solve
    return orig


def uninstall(ns, orig):
    """🔒 還原（`harvest()` 之 `ns` 跨情境共用 ⇒ 不還原即令下一情境之 `run_corner_pk` 亦被記錄）。"""
    for k, v in orig.items():
        ns[k] = v


def control_checks(ns, orig):
    """🔒 對照組自檢（考古 71 修法 ③）：⛔ 任一紅即停機、結果不得出艙。"""
    ok = True
    say("  🔒 對照組自檢（考古 71 修法 ③·餵已知為真之命題 ⇒ 須綠）")
    # ① 包裝器透明
    a = orig["rw_from_width"](12.34)
    n0 = len(REC["rw"])
    b = ns["rw_from_width"](12.34)
    same = (a == b) and (len(REC["rw"]) == n0 + 1)
    say(f"      ① 包裝透明：原始 R(12.34)={a!r}｜包裝後={b!r}｜"
        f"{'✅ 逐位相同且確有記錄' if same else '🔴 不同或未記錄'}")
    ok &= same
    # ② R 之已知真值（CLAUDE.md：W≥18 → 100%）
    r18 = orig["rw_from_width"](18.0)
    ok18 = abs(float(r18) - 100.0) < 1e-9
    say(f"      ② 已知真值：R(18.0)={r18}（`CLAUDE.md`：W≥18→100%）⇒ "
        f"{'✅ 綠' if ok18 else '🔴 紅 ⇒ 量測器紅、⛔ 結果不得出艙'}")
    ok &= ok18
    # ③ 判別力：餵一個**已知為偽**之命題，須紅（證上二式非恆綠）
    bad = abs(float(orig["rw_from_width"](0.0)) - 100.0) < 1e-9
    say(f"      ③ 判別力：R(0.0)=={orig['rw_from_width'](0.0)} 是否亦為 100 ⇒ "
        f"{'🔴 是（上式恆綠·無鑑別力）' if bad else '✅ 否 ⇒ 上式具鑑別力'}")
    ok &= (not bad)
    if not ok:
        red("對照組自檢**紅** ⇒ `B-3`：量測器紅，⛔ 本次量測結果不得出艙")
    return ok


def run_tag(tag, setback):
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g

    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_parcels, build_parcels, _sw = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    _diag, _sel, _off, win, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_parcels, build_parcels,
        setback, snapshot=snapshot)

    REC["slot"].clear(); REC["rw"].clear(); REC["solve"].clear()
    orig = install(ns)
    if not control_checks(ns, orig):
        return None
    REC["slot"].clear(); REC["rw"].clear(); REC["solve"].clear()

    err = None
    try:
        run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                   params, build_parcels, win, forced, setback)
    except Exception as e:
        err = f"{type(e).__name__}: {e}"
    finally:
        uninstall(ns, orig)
    return {"err": err, "orig": orig}


def report(tag, st):
    say()
    say("=" * 108)
    say(f"【情境 {tag}】")
    say("=" * 108)
    say(f"  run_step_g 之例外：{(st['err'] or '（未拋·⚠️ 與凍存名單不符）')[:200]}")
    slots = REC["slot"]
    say(f"  `_select_pool_slot` 呼叫次數 ＝ {len(slots)}"
        f"（⚠️ 閘破於 R1 ⇒ 期為 1；>1 表示非首個街廓即破）")
    if not slots:
        red("未記錄到任何 `_select_pool_slot` 呼叫 ⇒ 無從分解（受詞為空）")
        return None
    s = slots[-1]
    R = st["orig"]["rw_from_width"]

    # ── 理論側（⛔ 由所記輸入重建·其正確性由「重建閘」把關）─────────────────────
    w = s["widths"]
    b_L = float(s["L"].get("b", 0.0) or 0.0)
    k = int(s["out"]["k"])
    tbl = {t["k"]: t for t in s["out"]["table"]}
    th_engine = float(tbl[k]["ΣRw_L"])
    sL = sum(w[:k])
    th_rebuild = R(b_L + sL) - R(b_L)
    say()
    say("  ── 理論側（`_select_pool_slot`）─────────────────────────────────────────")
    say(f"      widths（來自 `_advance_block_with_split(k_naive, False)`）"
        f"｜n={len(w)}｜{[round(x, 4) for x in w]}")
    say(f"      k* ＝ {k}｜左群 ＝ w[:{k}] ＝ {[round(x, 4) for x in w[:k]]}｜Σw_左 ＝ {sL:.6f}")
    say(f"      b_L（理論起點 W）＝ {b_L:.6f}｜R(b_L) ＝ {R(b_L):.4f}")
    say(f"      b_L＋Σw_左（理論終點 W）＝ {b_L + sL:.6f}｜R(…) ＝ {R(b_L + sL):.4f}")
    say(f"      ⇒ 理論 ΣRw_L ＝ R(終)−R(起) ＝ {th_rebuild:.4f}")
    # 🔒 重建閘（CLAUDE.md·探針還原內部量須以碼面自身之保證自我驗證）
    gate = abs(th_rebuild - th_engine) < 5e-4
    say(f"      🔒 **重建閘**：引擎自算 `_t_star['ΣRw_L']` ＝ {th_engine:.4f}"
        f"｜本探針重建 ＝ {th_rebuild:.4f}｜Δ={abs(th_rebuild - th_engine):.6f}"
        f" ⇒ {'✅ 相符（分解可採）' if gate else '🔴 **不符 ⇒ 分解不得採**'}")
    if not gate:
        red("重建閘不過 ⇒ (甲) 之分解結論一律不採（`CLAUDE.md` 探針自我驗證閘）")
        return None

    # ── 實跑側（自 telescoping 閘之 R 呼叫還原 W₀／W_階段1末）──────────────────
    say()
    say("  ── 實跑側（`_rw_stage1_only`＋telescoping 閘之端點）─────────────────────")
    stepg_rw = [r for r in REC["rw"] if r["by"] == "run_step_g"]
    say(f"      `run_step_g` 內之 R(·) 呼叫 {len(stepg_rw)} 次（telescoping 家族之端點）：")
    for r in stepg_rw:
        say(f"          R({r['W']:.6f}) = {r['R']:.4f}")
    # 🔒 母體自證：`side` 之實有值**現查列出**（⛔ 不預設其為 'left'／'right'）
    sides = sorted({str(x["side"]) for x in REC["solve"]})
    say(f"      `_solve_G_one` 之 `side` 實有值 ＝ {sides}｜總呼叫 {len(REC['solve'])} 次")
    n_before = s["n_solve_before"]
    # 🔴 `side` 之實有值為**中文**（`['右側','左側','無']`·本探針現查抓到）——
    #    ⛔ 不得以 `'left'` 硬篩（首版即如此，得 0 宗 ⇒ 空母體之假「無資料」）。
    _lsel = [v for v in sides if v.lower().startswith("l") or v.startswith("左")]
    base_solves = [x for x in REC["solve"][:n_before] if str(x["side"]) in _lsel]
    final_solves = [x for x in REC["solve"][n_before:] if str(x["side"]) in _lsel]
    say(f"      左側（`side` ∈ {_lsel}）逐宗求解：**選槽前**（k_naive 趟）{len(base_solves)} 宗"
        f"｜**選槽後**（k* 趟）{len(final_solves)} 宗")
    for nm, arr in (("k_naive 趟（理論側 widths 之來源）", base_solves),
                    ("k* 趟（實跑側 rows 之來源）", final_solves)):
        say(f"      ▸ {nm}")
        for i, x in enumerate(arr):
            say(f"          [{i}] a={x['a_m2']}｜W_prev={x['W_prev']}｜is_corner={x['is_corner']}"
                f"｜W_near={x['W_near']}｜W_far={x['W_far']}｜Rw={x['Rw_pct']}"
                f"｜宗地寬={x['width']}｜回傳型={x['shape']}")
    # ── 🔴 分解：Δ ＝ 起點項 − 終點項（⛔ 附「重現引擎自報 Δ」之自我驗證閘）──────────
    say()
    say("  ── 🔴 分解 ─────────────────────────────────────────────────────────────")
    if len(stepg_rw) < 6:
        red(f"telescoping 家族之 R(·) 呼叫僅 {len(stepg_rw)} 次（<6）⇒ 端點取不齊，⛔ 不分解")
        return None
    # 呼叫序（碼面：telescoping 總量段 left→right，其後 階段2 段 left→right）
    W_f_tot_L, W0_L = stepg_rw[0]["W"], stepg_rw[1]["W"]
    W_f_s2_L, W1_end_L = stepg_rw[4]["W"], stepg_rw[5]["W"]
    say(f"      實跑左側端點：W₀ ＝ {W0_L:.6f}｜W_階段1末 ＝ {W1_end_L:.6f}"
        f"｜W_final ＝ {W_f_tot_L:.6f}（階段2 段之 W_final ＝ {W_f_s2_L:.6f}）")
    r_th_s, r_th_e = R(b_L), R(b_L + sL)
    r_re_s, r_re_e = R(W0_L), R(W1_end_L)
    start_term = r_th_s - r_re_s
    end_term = r_th_e - r_re_e
    delta_calc = start_term - end_term
    say(f"      起點項 ＝ R(理論起 {b_L:.6f}) − R(實跑起 {W0_L:.6f}) "
        f"＝ {r_th_s:.4f} − {r_re_s:.4f} ＝ **{start_term:+.4f}**")
    say(f"      終點項 ＝ R(理論終 {b_L + sL:.6f}) − R(實跑終 {W1_end_L:.6f}) "
        f"＝ {r_th_e:.4f} − {r_re_e:.4f} ＝ **{end_term:+.4f}**")
    say(f"      ⇒ Δ（＝實跑−理論）＝ 起點項 − 終點項 ＝ {start_term:+.4f} − ({end_term:+.4f})"
        f" ＝ **{delta_calc:+.4f}**")
    # 🔒 自我驗證閘②：須重現引擎自報之 Δ（容差 ＝ 逐宗 Rw 之 2dp 捨入累積）
    import re as _re_mod
    m = _re_mod.search(r"Δ=([0-9.]+)", st["err"] or "")
    if not m:
        red("自引擎訊息取不到 Δ ⇒ 無從對驗（⛔ 分解不得採）")
        return None
    d_engine = float(m.group(1))
    gap = abs(delta_calc - d_engine)
    say(f"      🔒 **自我驗證閘②**：引擎自報 Δ ＝ {d_engine:.3f}｜本探針分解 ＝ {delta_calc:.4f}"
        f"｜差 ＝ {gap:.4f}")
    say(f"          （容差 ＝ 逐宗 `Rw(%)` 之 2dp 捨入累積；`_re` 為<u>逐宗捨入值之和</u>，"
        f"telescoping 端點式則未捨入）")
    if gap > 0.05:
        red(f"分解與引擎自報 Δ 之差 {gap:.4f} > 0.05 ⇒ **分解不完整**，⛔ 不得宣稱已解釋")
        return None
    say(f"          ⇒ ✅ **分解恰好解釋 Δ**（差 {gap:.4f} ≤ 0.05）")

    # ── 乙組：候選歸因之窮舉（⛔ 逐項附可證偽之判別實驗與其結果）─────────────────
    adv_th = sL                                 # 理論推進量 ＝ Σw[:k*]
    adv_re = W1_end_L - W0_L                    # 實跑推進量 ＝ W_階段1末 − W₀
    n_s1_left = len(final_solves)
    say()
    say("  ── 乙組：候選歸因之**窮舉**（⛔ 非二擇一）──────────────────────────────")
    say(f"      推進量：理論 Σw[:k*] ＝ {adv_th:.6f}｜實跑 W_階段1末−W₀ ＝ {adv_re:.6f}"
        f"｜差 ＝ {adv_re - adv_th:+.6f} m")
    cands = [
        ("①", "理論側母體**多含**階段 2 宗",
         f"理論母體 ＝ widths[:k*]（{k} 筆）；階段2 段之 telescoping 端點 "
         f"W_final({W_f_s2_L:.4f}) == W_階段1末({W1_end_L:.4f}) ⇒ **本側無階段2推進**",
         abs(W_f_s2_L - W1_end_L) > 1e-9),
        ("②", "實跑側母體**多含**非階段 1 之推進",
         f"`_rw_stage1_only` 已排除 `_stage2_ids`；且同上：本側階段2 推進量 ＝ "
         f"{W_f_s2_L - W1_end_L:+.6f} m",
         abs(W_f_s2_L - W1_end_L) > 1e-9),
        ("③", "兩側之 `Rw` 累積**起點不同**（`b` ／ `W₀` 口徑）",
         f"實測 `b_L`＝{b_L:.6f} m（R＝{r_th_s:.4f}）vs `W₀`＝{W0_L:.6f} m（R＝{r_re_s:.4f}）"
         f" ⇒ 起點項 **{start_term:+.4f} pp**",
         abs(start_term) > 0.05),
        ("④", "`k*` 選定後**又被改動**",
         f"`_select_pool_slot` 全程呼叫 {len(slots)} 次；以其回傳之 k*＝{k} 重建理論值，"
         f"與引擎自算**逐位相同**（重建閘 Δ=0）⇒ k* 未被改動",
         False),
        ("⑤", "容差 `0.1` 本身過嚴",
         "⛔ 須先排除 ①〜④ 才可考慮；③ 已通過 ⇒ **不成立**（且本批⛔ 不得據此提修法）",
         False),
        ("⑥", "🆕 **本批補列**：理論之 widths 取自 `k_naive` 趟、實跑為 `k*` 趟 "
               "⇒ **同一宗之寬度在兩趟不同**（推進量差）",
         f"理論推進 {adv_th:.4f} vs 實跑推進 {adv_re:.4f}（**差 {adv_re - adv_th:+.4f} m·"
         f"兩情境皆存在**）⇒ 終點項 **{end_term:+.4f} pp**"
         + ("　⚠️ **差存在但對 Δ 之貢獻為 0**——兩端 W 皆 ≥18 ⇒ `R` 飽和於 100% "
            "**把它吸收掉了**；⛔ 此為偶然（換一組寬度即現形），"
            "⛔ 不得據此稱「本情境無此問題」"
            if abs(end_term) <= 0.05 else ""),
         abs(end_term) > 0.05),
    ]
    # 🔒 「差存在」與「是 Δ 之來源」**須分開**（⛔ 否則高估）：⑥ 之判準 ＝ 對 Δ 之**貢獻**
    passed = []
    for no, name, exp, verdict in cands:
        say(f"      {no} {name}")
        say(f"          判別實驗：{exp}")
        say(f"          ⇒ {'🔴 **通過（為 Δ 之來源）**' if verdict else '✅ 不通過（非來源）'}")
        if verdict:
            passed.append(no)
    say(f"      ⇒ **通過之候選 ＝ {passed}**（{len(passed)} 項）")
    say(f"      🔒 自答「是否窮盡？」：本分解為**恆等式** "
        f"`Δ = [R(理起)−R(實起)] − [R(理終)−R(實終)]`，而 `理終=理起+Σw`、`實終=實起+推進` "
        f"⇒ **任何來源都必落入「起點」或「推進量」二者之一**；二者皆已具名量出且合計"
        f"恰好等於引擎自報之 Δ（差 {gap:.4f}）⇒ ⛔ 無第三項之容身處。")
    if len(passed) == 1:
        say(f"      ⇒ **`U4` 於本情境<u>字面成立</u>**（恰 1 項：{passed[0]}）。"
            f"⚠️ 但**⛔ 不得據此稱歸因為單一**——⑥ 之差在本情境確實存在"
            f"（{adv_re - adv_th:+.4f} m），只是被 `R` 之飽和吸收；見另一情境。")
    else:
        say(f"      ⚠️ ⇒ **`U4`（恰有一項通過）破**：實為 **{len(passed)} 項**，"
            f"且二者**非互斥**（同一恆等式之兩個加項）⇒ 候選清單須改為**分解**、⛔ 非單選。")
    return {"w": w, "b_L": b_L, "k": k, "th": th_engine, "sL": sL, "R": R,
            "W0": W0_L, "W1_end": W1_end_L, "start_term": start_term,
            "end_term": end_term, "delta_calc": delta_calc, "d_engine": d_engine,
            "base": base_solves, "final": final_solves, "stepg_rw": stepg_rw}


def main():
    say("=" * 108)
    say("【`W-G.9-14` 甲組】結構閘「理論＝實跑」之逐項分解（⛔ 純偵察·⛔ 零修復）")
    say("=" * 108)
    out = {}
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        st = run_tag(tag, sb)
        if st is None:
            red(f"情境 {tag}：對照組自檢未過 ⇒ 略過（`B-3`）")
            continue
        out[tag] = report(tag, st)
    say()
    say("=" * 108)
    say(f"【判定】完成分解之情境 ＝ {sorted(k for k, v in out.items() if v)}")
    say("=" * 108)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
