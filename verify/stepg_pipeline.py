# -*- coding: utf-8 -*-
"""
W-D.2 P6 — Step G headless driver（v2 轉正必要條件；KL 放行 2026-07-06）。

headless 重現 app.py 步驟 G（宗地分配 G 值迭代＋W-D.2 §3 滑池槽＋守恆 ledger），
產出三張表對拍 verify/out/wd2_run/（KL 2026-07-06 乾淨雙參數輪＝v2 準源）：
  G 值計算結果／W-D.2 §3 滑池槽診斷／逐槽 J 表 × 雙情境。

**參數裝配鐵則（KL 四條件①）**：路況負擔尺度一律消費快照 `blocks.*.負擔尺度_輸入`
（front/side_new＝輸入>0；calc_* 算出之尺度與輸入逐格斷言相等，破＝RuntimeError），
**不得吃 SS_ROAD 預設**。
街廓深度＝快照 `街廓分配深度_m`，惟該欄自 **K-8 §三 commit A** 起由
`run_verification.load_snapshot()` 於**記憶體內以現算 N-19′ 覆寫**（檔案零修改·U-K8-1＝乙
之其餘部分照舊）；本檔另以 `assert_depth_same_source` 逐塊看守兩路同源。

**🆕 v3 財務接線（KL 裁定 2026-07-09；廢 `StepG_v2_中間態`／`財務接線_全區_步驟F`／Tab4／Tab5）**：
全區財務一律消費快照 `財務接線_v3`。A/B/C 三者皆由**獨立於斷言錨的輸入現算**（禁反填）：
  - C ＝ (單位工程費×總面積精確 ＋ (拆遷費+行政費)×總面積精確 ＋ 貸款利息) ÷ Σ(後街廓面積×單價)
        〔**加總形**分母，KL 裁定；另斷言與 calc_C_value 均價形等價至 1e-8〕
  - B ＝ calc_B_value(一般負擔, 重劃前均價, 重劃後均價, 總面積精確, 已徵收公設)
        〔一般負擔 ＝ DXF 共同負擔街廓面積和 − 抵充地 − 特別負擔(C)〕
  - A ＝ 後街廓單價[所屬街廓] ÷ 重劃前區段單價[重劃前地價區段]（**逐宗**；zone 由 `_attach_pre_zone` 貼）
UC9898 錨：B=0.171043、C=0.091319（run_verification 全等斷言＋雙 reverse-test 證非寫死）。
**精度鐵律**：重劃後均價全精度參與乘除，禁先 round 2dp。

**J 非零看守（KL 四條件③）**：有 SIDE_LINE 之側 F×l₁ 必 >0，零＝RuntimeError
（app 側 warn-on-zero-weight 之 headless 對應、fail-hard）。

**🆕 結構不變量永久閘（KL 閘裁定 2026-07-09；破即 RuntimeError）**：守恆／⊥（ALLOC⊥FRONT）／
位次＝投影序／J(k*)≥J(naive)／理論＝實跑／telescoping（ΣRw_側 = R(W_final) − R(W₀_buffer)）。
取代舊「J/ΣRw 逐格不變」閘——後者僅成立於 Rw 飽和域，v3 換真值地價後配地寬縮約 24%、
離開飽和域故 J/ΣRw 合法變動（詳 baselines/v3/PROVENANCE_v3.md 註①②）。

🔧 維護耦合：本檔推進段＝app.py Step G orchestration（`_advance_block_with_split`／
選槽／抵費地幾何／ledger，約 14650-15450）之**逐行複刻**——該段波動必同波更新本檔。
真函式（solve_G_binary/iterate_G_S/calc_*/_select_pool_slot/_spatial_order_parcels_v2/
alloc_normal_axis/get_min_lot_size）全走 app_harvest。
"""


def compute_total_burden_rate(ns, cb, snapshot):
    """🆕 微波（KL 裁「翻」2026-07-10）：**重劃總負擔率現算**（非寫死、非抄錄截圖）。

    域定義（KL 裁示）＝公設用地負擔比 ＋ 費用負擔比；與 app Tab7（~10259-10263）同式：
        公設負擔比 = (公設共同負擔 − 抵充地) ÷ (總面積精確 − 抵充地)
        費用負擔比 = 費用總額 ÷ [重劃後平均地價 × (總面積精確 − 抵充地)]
        重劃總負擔率 = 公設負擔比 + 費用負擔比

    輸入全數取自 v3 快照既有欄 ＋ DXF 街廓面積（零新增料）。
    ⚠️ **公設共同負擔須用 DXF 實值 12146.5579**：改用截圖 rounded 12146.56 會得
    0.40712393（差第 7 位）。此即「現算 vs 抄錄」之刀口。

    UC9898 錨：公設負擔比 34.754211%、費用負擔比 5.958176%、**總 0.40712387**
    （run_verification 全等斷言 ＋ reverse-test：改單位工程費 → 率隨動）。

    消費者：`f3_total_burden_rate_from_finance` → `_estimate_G_for_qualification`（街角 PK 之 G估）
    ＋ `iterate_G_S` 之迭代初值。回傳 (rate, breakdown)。
    """
    fcb = ns["F3_CATEGORY_BURDEN"]
    fin = snapshot["財務接線_v3"]          # 缺節＝loud KeyError
    total = float(fin["重劃區總面積_m2_精確"])
    offset = float(fin["抵充地_m2"])
    denom = total - offset
    if denom <= 0:
        raise RuntimeError(f"🔴 重劃總負擔率：總面積精確({total}) − 抵充地({offset}) ≤ 0")
    public_common = sum(float(b.get("area_m2", 0.0) or 0.0) for b in cb
                        if fcb.get(b.get("category", ""), "") == "共同負擔")
    if public_common <= 0:
        raise RuntimeError("🔴 重劃總負擔率：DXF 共同負擔街廓面積和 ≤0（分類或圖層有誤）")
    eng = float(fin["單位工程費_元每m2"]) * total
    redev = (float(fin["拆遷費_元每m2"]) + float(fin["行政費_元每m2"])) * total
    cost_sum = eng + redev + float(fin["貸款利息_元"])
    price_after = float(fin["重劃後平均地價_元每m2"])
    if price_after <= 0:
        raise RuntimeError("🔴 重劃總負擔率：重劃後平均地價 ≤0")
    public_rate = (public_common - offset) / denom
    fee_rate = cost_sum / (price_after * denom)
    rate = public_rate + fee_rate
    return rate, {"公設負擔比": public_rate, "費用負擔比": fee_rate,
                  "公設共同負擔_DXF": public_common, "費用總額": cost_sum,
                  "總面積精確": total, "抵充地": offset}


def _compute_v3_finance(ns, snapshot, cb, cad):
    """🆕 P-0a（裁定M·reviewer R1）：v3 全區財務單一真相源——B／C／特別負擔尺度／地價。

    **純位移自 `run_step_g` 之財務前段**（現址 `grep -n "def _compute_v3_finance" verify/stepg_pipeline.py`）（算式、求值順序、兩處斷言〔條件① 尺度、C 兩形等價 1e-8〕
    逐字不動）。M-2/Q1 之「假設第 1 宗真 G」與實配共用本函式（避第三份抄寫·失敗考古 #20）。

    **不寫 globals**：`_V3_FINANCE` payload 以 dict 回傳、由呼叫端（`run_step_g`）於 `_tab6_burden`
    檢查後之原位寫入 globals（保序·true zero-behavior·錯誤路徑亦不變）。
    `_tab6_burden` 之取值與 raise **不在本函式**（PK 階段該 session 鍵未鋪底·reviewer W-1）。
    """
    fcb = ns["F3_CATEGORY_BURDEN"]
    SB = snapshot["blocks"]
    fin = snapshot["財務接線_v3"]      # 缺節＝loud KeyError，禁隱形預設
    # ── 🆕 v3：C 由 Tab7 輸入現算（加總形分母；獨立於 C 錨，禁反填） ──
    #   global.C_pct 僅供 §7-0a 地基檢查、非 Step G 之 C。
    _post_bp = fin["後街廓_面積單價"]
    _total_precise = float(fin["重劃區總面積_m2_精確"])          # 34949.888（非 34950/34949.90）
    _eng_cost = float(fin["單位工程費_元每m2"]) * _total_precise
    _redev_cost = (float(fin["拆遷費_元每m2"]) + float(fin["行政費_元每m2"])) * _total_precise
    _loan_interest = float(fin["貸款利息_元"])
    _cost_sum = _eng_cost + _redev_cost + _loan_interest
    # 加總形分母 Σ(後街廓面積×單價)（KL 裁定）＝ 1643176255.06
    _C_denom_sum = sum(float(v["面積_m2"]) * float(v["單價_元每m2"])
                       for v in _post_bp.values())
    if _C_denom_sum <= 0:
        raise RuntimeError("🔴 v3 C 分母（加總形 Σ後街廓面積×單價）≤0，快照 後街廓_面積單價 有誤")
    C_for_calc = _cost_sum / _C_denom_sum
    _build_blocks = [b for b in cb
                     if fcb.get(b.get("category", ""), "") == "可建築土地"]

    # ── 路況（條件①：快照 負擔尺度_輸入 消費；長度＝CAD） ──
    flen = cad.get("front_lengths", {}) or {}
    slbs = cad.get("side_lengths_by_side", {}) or {}
    road_data = []
    for b in _build_blocks:
        lbl = b["label"]
        blk = SB[lbl]
        sides = slbs.get(lbl, {}) or {}
        road_data.append({
            "label": lbl,
            "front_width": float(blk["正面"]["路寬_m"]),
            "front_length": float(flen.get(lbl, 0.0) or 0.0),
            "front_new": float(blk["正面"]["負擔尺度_輸入"]) > 0,
            "left_side_width": float(blk["左側"]["路寬_m"]),
            "left_side_length": float(sides.get("left", 0.0) or 0.0),
            "left_side_new": float(blk["左側"]["負擔尺度_輸入"]) > 0,
            "right_side_width": float(blk["右側"]["路寬_m"]),
            "right_side_length": float(sides.get("right", 0.0) or 0.0),
            "right_side_new": float(blk["右側"]["負擔尺度_輸入"]) > 0,
        })
    sb = ns["calc_special_burden_total"](road_data, C_for_calc)
    sb_rows_by_label = {r["街廓"]: r for r in sb["rows"]}
    # 條件① 斷言：calc 出之尺度 == 快照 負擔尺度_輸入（逐塊逐側；破＝fail loud）
    for r_sb in sb["rows"]:
        blk = SB[r_sb["街廓"]]
        for k_sb, k_snap in (("正街尺度", "正面"), ("左側尺度", "左側"), ("右側尺度", "右側")):
            exp = float(blk[k_snap]["負擔尺度_輸入"])
            got = float(r_sb[k_sb])
            if abs(got - exp) > 1e-9:
                raise RuntimeError(
                    f"條件① 尺度斷言破：{r_sb['街廓']} {k_snap} calc={got} ≠ 快照輸入={exp}"
                    "（路寬×新闢 與 負擔尺度_輸入 不相容，查快照/尺度表）")

    # ── B 值（app 步驟 H 複刻；v3 全區參數＝快照 財務接線_v3） ──
    public_common_total = sum(float(b.get("area_m2", 0.0) or 0.0) for b in cb
                              if fcb.get(b.get("category", ""), "") == "共同負擔")
    offset_area = float(fin["抵充地_m2"])
    preexisting_public = float(fin["已徵收公設_m2"])
    total_area = _total_precise
    price_before = float(fin["重劃前平均地價_元每m2"])
    price_after = float(fin["重劃後平均地價_元每m2"])
    # 特別負擔已吃 C（(正+側)×(1−C)）→ 一般負擔 → B。C 耦合 B，故 C 必先算。
    general_burden = max(public_common_total - offset_area - sb["special_total"], 0.0)
    B_value = ns["calc_B_value"](
        general_burden_area=general_burden,
        price_before=price_before, price_after=price_after,
        total_area=total_area, preexisting_public_area=preexisting_public,
    )
    # C 兩形等價斷言（reviewer 逮出之分岔顯性化）：加總形 vs app calc_C_value 均價形。
    #   分母差 ~7.21 元（第 7 位有效數字，源自 Σ後面積 22803.33 vs total−DXF公設 22803.3301），
    #   C 值差 ~4e-10。破 1e-8 ＝ 二形真分岔，須停查（勿靜默採其一）。
    _C_avg_form = ns["calc_C_value"](
        engineering_cost=_eng_cost, redev_cost=_redev_cost, loan_interest=_loan_interest,
        price_after=price_after, total_area=total_area,
        public_burden_total=public_common_total,
    )
    if abs(C_for_calc - _C_avg_form) > 1e-8:
        raise RuntimeError(
            f"🔴 C 兩形分岔：加總形={C_for_calc:.12f} vs 均價形(calc_C_value)={_C_avg_form:.12f}"
            f"，Δ={abs(C_for_calc - _C_avg_form):.3e} > 1e-8（快照 後街廓面積 與 DXF 公設面積不再互補？）")

    # ── 地價（v3：後街廓單價／重劃前區段單價；A 逐宗＝post/pre） ──
    post_price_by_block = {lbl: float(v["單價_元每m2"]) for lbl, v in _post_bp.items()}
    pre_price_by_zone = {z: float(v["單價_元每m2"])
                         for z, v in fin["重劃前區段_面積單價"].items()}
    return {
        "B": B_value, "C": C_for_calc, "_build_blocks": _build_blocks,
        "sb": sb, "sb_rows_by_label": sb_rows_by_label,
        "post_price_by_block": post_price_by_block,
        "pre_price_by_zone": pre_price_by_zone,
        # 財務中繼態（run_verification 財務閘消費；非計算鏈）·payload 逐鍵同本函式下方之 return dict
        "_V3_FINANCE": {
            "B": B_value, "C": C_for_calc, "C_avg_form": _C_avg_form,
            "eng": _eng_cost, "redev": _redev_cost, "loan": _loan_interest,
            "cost_sum": _cost_sum, "C_denom": _C_denom_sum,
            "general_burden": general_burden, "public_common": public_common_total,
            "special_total": sb["special_total"],
            "post_price_by_block": dict(post_price_by_block),
            "pre_price_by_zone": dict(pre_price_by_zone),
        },
    }


def assert_depth_same_source(depth_from_snapshot):
    """🆕 **A-4 同源閘**（K-8 §三 commit A·KL 裁 2026-07-31）——不等 ⇒ loud raise。

    比的是**兩條插線**，不是同一條算式跑兩次：
      · 左：`f3_alloc_depth_by_label` ——由**快照**餵出之 session 鍵（app-live 同名鍵之孿生）
      · 右：`run_verification.n19p_depth_by_block()` ——當場自 CAD **現算**之 N-19′
    若改成「現算 vs 剛注入的現算」即成套套邏輯（`fixture-provenance` 禁令），故不那樣寫。

    ── 🔒 **誠實標籤：本閘現為「恆真閘」**（claude.ai 獨立複驗·commit C 標註）─────────
    複驗結果（窮盡·錨 `65ffd17`）：`run_step_g` 之 **19 個呼叫端**，其 `snapshot` **全部**
    來自 `rv.load_snapshot()`（已注入）；**無任何生產路徑餵 `load_snapshot_raw()`**。
    母體檢查亦然——`n19p_depth_by_block()` 與 `_build_blocks` 用**同一個**
    `F3_CATEGORY_BURDEN` 過濾，集合恆等。
    ⇒ **本閘在所有現行呼叫點恆真**，與 K-4-4 之 `s_max_left`／`front_p2` 閘同族
      （本專案第三次出現此形態）。**其價值在「凍結未來呼叫點」，不在「現在咬到了什麼」。**
    ⚠️ 人工餵原始快照之反例測試，證明的是「**若**有人這樣寫會被咬」，
       **不是**「現在有人這樣寫」——回報時不得以之充作判別力證據。
    🗄️ 泛化波觀察項：**恆真閘家族**（A4 registry／K-4-4／本閘）宜統一標註體例。

    🔒 **閘寬有機制依據、非實測殘差**：取 `0.005` ＝ 2dp 記載鏈之無差別半寬
      （辦法 §3 長度記至二位小數）。**禁改用 `1e-6`**——K-8 §一 判 BASELINE `#0`/`#2`
      為等價類、禁寫死單一實體，而 R4 之 N-19′ 等價類散布**實測 5.80e-06 > 1e-6**；
      硬比單值會把「禁寫死單一實體」之禁令從配對層漏到數值層。
    """
    import run_verification as _rv_ds        # 函式內 import：run_verification 於模組頂已 import 本檔
    _now = _rv_ds.n19p_depth_by_block()
    _TOL_2DP_HALF = 0.005
    if set(depth_from_snapshot) != set(_now):
        raise RuntimeError(
            f"🔴 A-4 同源閘：街廓母體不等——快照側 {sorted(depth_from_snapshot)} vs "
            f"現算 {sorted(_now)}（K-8 §三 commit A）")
    _bad = {k: (depth_from_snapshot[k], _now[k]) for k in _now
            if abs(float(depth_from_snapshot[k]) - float(_now[k])) > _TOL_2DP_HALF}
    if _bad:
        raise RuntimeError(
            f"🔴 A-4 同源閘：深度兩路不同源（閘寬 {_TOL_2DP_HALF}＝2dp 記載鏈半寬）"
            f"｛街廓: (快照側, 現算)｝＝{_bad}。"
            f"⛔ 深度是 MinA／G／街角面積／PK 勝負之共同上游，不得無聲分岔；"
            f"若係以原始快照呼叫，請改走 `run_verification.load_snapshot()`（K-8 §三 A-2）")


def run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
               winners_state, forced_map, setback):
    """一情境 Step G。回傳 {'g_rows','pool_diag','slot_rows'}（欄名/rounding 同 app）。"""
    import numpy as _np_d
    from shapely.geometry import Polygon as _SP_d
    # §N3-0 T2：`unary_union as _uunion_d` 已拆——其唯一用途為舊池片式
    #   `_uunion_d(allocated_polys).buffer(0.001)`（病灶·已廢）；留之即 dead import。

    ss = fake_st.session_state
    SB = snapshot["blocks"]
    # 🆕 P-0a（裁定M）：v3 財務（B/C/尺度/地價）純位移為 module 級 `_compute_v3_finance`
    #   （單一真相源·PK 階段真 G 共用·避第三份抄寫#20）。**true zero-behavior**：helper 不寫
    #   globals；`_V3_FINANCE` 由本函式於 `_tab6_burden` 檢查**後**之原位寫入（保序·錯誤路徑亦不變）。
    _fin3 = _compute_v3_finance(ns, snapshot, cb, cad)
    B_value = _fin3["B"]
    C_for_calc = _fin3["C"]
    _build_blocks = _fin3["_build_blocks"]
    sb_rows_by_label = _fin3["sb_rows_by_label"]
    post_price_by_block = _fin3["post_price_by_block"]
    pre_price_by_zone = _fin3["pre_price_by_zone"]
    # 重劃總負擔率＝`compute_total_burden_rate` 現算（build_pipeline 鋪底）。
    # 舊 `or 0.40` fallback 已廢（快照 global.重劃總負擔率 鍵一併刪）→ 缺值即 loud。
    #   ⚠️ 不移入 helper：PK 階段（selection_pipeline.run_corner_pk）此 session 鍵尚未鋪底，
    #      移入會使假設第 1 宗真 G 誤 raise（reviewer W-1）。
    _tab6_burden = ss.get("f3_total_burden_rate_from_finance")
    if _tab6_burden is None:
        raise RuntimeError(
            "🔴 f3_total_burden_rate_from_finance 未鋪底：須先 compute_total_burden_rate()"
            "（禁靜默退回 0.40 舊 fallback）")
    _tab6_burden = float(_tab6_burden)
    # 財務中繼態外拋（run_verification 之財務閘消費；非計算鏈）·保原位（於 _tab6_burden 檢查後）
    globals()["_V3_FINANCE"] = _fin3["_V3_FINANCE"]

    # ── session 鋪底（Step L/PK 產物＝快照/選位半 driver 餵入） ──
    ss["f3L_setback_default"] = setback
    ss["f3_alloc_depth_by_label"] = {b["label"]: float(SB[b["label"]]["街廓分配深度_m"])
                                     for b in _build_blocks}
    # 🆕 K-8 §三 A-4 同源閘（KL 裁 2026-07-31·commit A）
    assert_depth_same_source(ss["f3_alloc_depth_by_label"])
    # backlog②（WARNING-2）：min_width 逐塊吃**真實 category**（廢硬編「住宅區」）。
    ss["f3_min_width_by_label"] = {
        b["label"]: float(ns["get_min_lot_size"](
            b["category"], float(SB[b["label"]]["正面"]["路寬_m"])).get("min_width", 0.0) or 0.0)
        for b in _build_blocks}
    ss["f3_corner_winners"] = winners_state
    ss["f3L_forced_offset"] = forced_map
    ss["f3L_corner_min_table"] = param_rows
    # 🆕 K-8 §三 A-1：BASELINE 接線（舊態＝空 dict ⇒ harness 側算不出 N-19′、
    #   且 K-8 §三〜§五 之街角規定範圍以 BASELINE 為遠側邊界）。缺件 loud，禁空 dict。
    _bls_sg = cad.get("baselines")
    if not _bls_sg:
        raise RuntimeError(
            "🔴 run_step_g：`cad['baselines']` 為空——BASELINE 圖層未解析或配對全失敗。"
            "⛔ 禁以空 dict 兜底（K-8 §三 A-1·no-silent-fallback）")
    ss["f3_manual_baseline"] = _bls_sg
    ss.setdefault("f3_g_iter_params", {})
    _params_for_g = dict(ss.get("f3_g_iter_params", {}))
    rows_by_lbl = {r["街廓"]: r for r in param_rows}

    block_meta_by_label = {}
    for b in cb:
        _meta = dict(b)
        try:
            _sp = _SP_d(b["vertices"])
            if not _sp.is_valid:
                _sp = _sp.buffer(0)
            _meta["shapely"] = _sp
        except Exception:
            _meta["shapely"] = None
        block_meta_by_label[b["label"]] = _meta

    # [H-ghost] 已決（KL 逐碼裁定 2026-07-06，consistent 不升版；見 baselines/v2/PROVENANCE_v2）：
    #   ghost 天生零面積（幾何面積_m2=0、面積_m2=0，真面積另存 _ghost_area_m2 已落池）→
    #   生不生、排不排，G/守恆/J 全不變。app 的 Step G 實**不**排除 ghost（E-0.4 排除只在
    #   三層調配 _allocate_three_tier_v1，W-E/W-F 階段）；KL 準源輪 overlay 未生 R1/R4 住宅
    #   ghost（H-a 輸入差），harness 輪（repo V6.dxf）生了 → 此過濾**對齊 KL 輪**、零面積無條件安全。
    #   ⚠️ backlog（下波）：加零面積不變量斷言（見 PROVENANCE_v2 backlog 節）。
    parcels_by_block = {}
    for tp in build_parcels:
        if tp.get("_is_ghost_sliver", False):
            continue
        parcels_by_block.setdefault(tp["所屬街廓"], []).append(tp)

    solve_G_binary = ns["solve_G_binary"]
    iterate_G_S = ns["iterate_G_S"]
    alloc_normal_axis = ns["alloc_normal_axis"]
    _select_pool_slot = ns["_select_pool_slot"]
    _spatial_order_parcels_v2 = ns["_spatial_order_parcels_v2"]
    _rw_from_width = ns["rw_from_width"]      # 結構閘 telescoping 用
    _pool_strips_for_block = ns["_pool_strips_for_block"]   # §N3-0 T2：池片單一真相源
    _oblique_s_max = ns["_oblique_s_max"]                   # step 0（正交→斜交 s_max）單一真相源·#20
    _corner_buffer_S = ns["_corner_buffer_S"]               # §3 街角 band 幾何 bisect·side 參數化·單一真相源·#20
    _acct_geom_tol_per_lot = ns["_acct_geom_tol_per_lot"]   # §N3-0 帳對幾何閘：閘寬單一真相源
    _acct_geom_tol_block = ns["_acct_geom_tol_block"]
    # 🆕 W-G.9-4（expand）：**W 之單一產生者**（`K-9-5-6` intrinsic 直量·權威序第 1 級）。
    #   `_mp_base_W0` 自此純委派至本名；⛔ 不得於本檔另寫第二份 W 定義（`GB-48` 族）。
    _k956_W_from_mp = ns["k956_W_from_mp"]

    g_rows = []
    detail_trace = {}
    pool_diag = {}
    # 🆕 §4 P2-e／W-4 回饋通道：`{街廓: {暫編地號: 實際落位面積}}`。階段2 落位在 stepg（幾何層）、
    #   `a_rem`/`placed` 帳在 wf_f4（帳層）——「只裝得下一部分」之殘量若無回報通道，
    #   `placed` 會與實際落位分岔、a′ 帳漏（W-4）。**頂層鍵**（非塞 `pool_diag`，
    #   後者逐鍵攤成診斷表欄位、加 dict 值會污染 baseline 欄集）。
    _stage2_placed = {}

    # ── _build_g_row / _solve_one（app 內嵌 def 逐行複刻） ──
    def _build_g_row(_k, _tp, _blk_label, _blk_area, _front_len, _avg_depth,
                     _zone, _A_ratio, _l_front, _l_side, _F, _is_corner_mark,
                     _is_first_corner, _side, _res, _solver_label, _alloc_side):
        if '分攤登記面積_m2' in _tp:
            _a_m2 = round(float(_tp.get('分攤登記面積_m2', 0) or 0)
                          + float(_tp.get('面積_m2', 0) or 0), 2)
        else:
            _a_m2 = round(float(_tp.get('面積_m2', 0) or 0), 2)
        return {
            '暫編地號': _k, '原地號': _tp.get('原地號', ''),
            '所屬街廓': _blk_label,
            '重劃前區段': _zone,
            'a 面積(㎡)': _a_m2,
            '街廓面積(㎡)': round(_blk_area, 2),
            '正面長度(m)': round(_front_len, 2),
            '平均深度(m)': round(_avg_depth, 2),
            'A 地價比': round(_A_ratio, 4),
            'l₂ 正面尺度': round(_l_front, 2),
            'l₁ 側面尺度': round(_l_side, 2),
            '街角地': '是' if _is_corner_mark else '否',
            '第1筆街角': '是' if _is_first_corner else '否',
            '街角側別': _side if _is_corner_mark else '—',
            'F(m)': round(_F, 2),
            'W(m)': round(_res.get('W', 0.0), 2),
            'Rw(%)': round(_res.get('Rw_pct', 0.0), 2),
            'S(m)': round(_res.get('S', 0.0), 2),
            '幾何面積(㎡)': round(_res.get('area_geom', 0.0), 2),
            'G(㎡)': round(_res.get('G', 0.0), 2),
            '累積S(m)': round(float(_res.get('_alloc_cum_S', 0.0)), 2),
            '推進側別': _alloc_side,
            '解法': _solver_label,
            '迭代次數': _res.get('iterations', 0),
            '是否收斂': _res.get('是否收斂_override',
                                 '✅' if _res.get('converged') else '⚠️'),
            '負擔比率': round(1 - _res['G']/_a_m2, 4)
                       if _a_m2 > 0 and _res.get('G') else 0,
            '宗地寬度(m)': round(_res.get('_宗地寬度', 0.0), 2),
            '畸零地旗標': _res.get('_畸零旗標', ''),
            'cut_coords': _res.get('cut_coords', []) or [],
        }

    def _solve_one(_a_m2, _A, _l_front, _l_side, _F, _blk_poly, _d_hat,
                   _baseline_pt, _S_max, _is_corner, _side, _avg_depth,
                   _allocation_dir=None, _side_mid=None, _W_prev=0.0,
                   _near_dir=None):
        # 🆕 P-0b（裁定M·Q-M4）：薄殼委派 app module 級 `_solve_G_one`（單一真相源·經 ns）。
        #   B_value/C_for_calc（_compute_v3_finance 拆出）＋ _tab6_burden（本函式上方檢查）為閉包捕獲。
        return ns["_solve_G_one"](
            a_m2=_a_m2, A=_A, l_front=_l_front, l_side=_l_side, F=_F,
            blk_poly=_blk_poly, d_hat=_d_hat, baseline_pt=_baseline_pt,
            S_max=_S_max, is_corner=_is_corner, side=_side, avg_depth=_avg_depth,
            B=B_value, C=C_for_calc, tab6_burden=_tab6_burden,
            allocation_dir=_allocation_dir, side_mid=_side_mid, W_prev=_W_prev,
            near_dir=_near_dir)   # 🆕 D-2b-23【甲】：界面單線（薄殼直通·不推導）

    # ── 逐街廓（app Step G 迴圈逐行複刻；st.* 於 headless 為 fake no-op 故略） ──
    for blk_label, parcels_in_blk in parcels_by_block.items():
        blk_meta = block_meta_by_label.get(blk_label, {})
        blk_poly = blk_meta.get('shapely', None)
        blk_area = float(blk_meta.get('area_m2', 0.0) or 0.0)

        # ── 🆕 §4 P2-a 兩階段落位（裁定B）：階段分流 ───────────────────────────────
        #   階段1宗＝原地主宗（`build_parcels` 原生·**不帶** `配地階段` 鍵）——定案並定出池範圍。
        #   階段2宗＝wf_f4 池內遞補合成宗（`add_syn` 帶 `配地階段='池內'`·P1 旗標·`grep -n "def add_syn" verify/wf_f4.py`）——
        #     **不進** `ordered_v2`／**不進**位次閘母體，改由 `_place_pool_parcels` 於階段1 定案後
        #     之**池範圍內**落位。根因：遞補宗混入單一投影序列會插隊擠爆原地主末宗
        #     （3.5m `628-37(1)`：S_remain 8.57 < 需 8.81 → |G−幾何|=7.90）。
        #   **資料驅動**（禁 `74·` 名稱前綴／塊名／側別判別·泛用紀律）。
        #   ⚠️ B-2（reviewer 活抓）：`_proj_rank`（下方 :~410）母體**必須同步過濾**，否則
        #     `pre_position`(1,2,3,4) 與投影排名(1,2,4,9) 對不上 → 位次閘必 raise。兩處共用本清單。
        _stage1_parcels = [tp for tp in parcels_in_blk if '配地階段' not in tp]
        _stage2_parcels = [tp for tp in parcels_in_blk if '配地階段' in tp]

        sb_row = sb_rows_by_label.get(blk_label, {})
        front_len = float(sb_row.get('正面長度(m)', 0.0) or 0.0)
        l_front = float(sb_row.get('正街尺度', 0.0) or 0.0)
        avg_depth_default = float(
            (ss.get('f3_alloc_depth_by_label', {}) or {}).get(blk_label)
            or ((blk_area / front_len) if front_len > 0 else 0.0))

        d_hat = None; corner_pt = None; S_block_max = front_len or 100.0
        _cad_fl_blk = (ss.get('f3_cad_front_lines', {}) or {}).get(blk_label, {})
        if _cad_fl_blk and _cad_fl_blk.get('p1') and _cad_fl_blk.get('p2'):
            _p1_fl = _cad_fl_blk['p1']; _p2_fl = _cad_fl_blk['p2']
            _dx_fl = _p2_fl[0] - _p1_fl[0]; _dy_fl = _p2_fl[1] - _p1_fl[1]
            _L_fl = (_dx_fl ** 2 + _dy_fl ** 2) ** 0.5
            if _L_fl > 0.1:
                d_hat = _np_d.array([_dx_fl / _L_fl, _dy_fl / _L_fl])
                corner_pt = _np_d.array(_p1_fl, dtype=float)
                S_block_max = float(_L_fl)
        _alloc_dir_cad = (ss.get('f3_cad_alloc_dir', {}) or {}).get(blk_label)
        allocation_dir_block = alloc_normal_axis(_alloc_dir_cad)

        # ── 結構閘 ⊥：宗地分配線(ALLOC) ⊥ 正面臨路線(FRONT) ──
        #   機制不變量（純 CAD 幾何、價格無關）。容差 0.15 ≈ 8.6°（UC9898 實測 0.045–0.092
        #   ＝繪圖公差 2.6°–5.3°）。破＝ALLOC/FRONT 畫錯或配對錯（如 ALLOC 平行 FRONT → |dot|≈1）。
        if _alloc_dir_cad is not None and d_hat is not None:
            _u_alloc = _np_d.asarray(_alloc_dir_cad, dtype=float)
            _n_ua = float(_np_d.linalg.norm(_u_alloc))
            if _n_ua > 1e-9:
                _perp_dot = abs(float(_np_d.dot(_u_alloc / _n_ua, d_hat)))
                if _perp_dot >= 0.15:
                    raise RuntimeError(
                        f"🔴 結構閘 ⊥ 破：街廓 {blk_label} |û_alloc·d̂_front|={_perp_dot:.4f} ≥0.15"
                        f"（ALLOC 未垂直 FRONT，夾角 {90 - _np_d.degrees(_np_d.arccos(min(1.0, _perp_dot))):.1f}°"
                        f" 偏離；查 DXF 之 宗地分配線／FRONT_LINE 圖層）")

        # ordered_v2（app 同構）
        _v2_res = None
        _degenerate_order = (d_hat is None or corner_pt is None)
        # P2-a：退化序（缺 FRONT_LINE ⇒ 無 d_hat/corner_pt）下**無幾何可定池範圍** ⇒ 階段2 落位
        #   不可能。此時若仍有階段2宗，靜默丟棄＝a′ 帳漏、靜默沿用舊單序列＝兩階段化被繞過，
        #   二者皆違 no-silent-fallback → **loud raise**（UC9898 全塊皆有 FRONT_LINE·不觸）。
        if _degenerate_order and _stage2_parcels:
            raise RuntimeError(
                f"🔴 P2-a：街廓 {blk_label} 退化序（缺 d_hat/corner_pt）卻有階段2宗 "
                f"{[tp.get('暫編地號') for tp in _stage2_parcels]}——池範圍不可定義、"
                f"池內落位無法執行（禁靜默丟棄／禁退舊單序列），停")
        if _degenerate_order:
            ordered_v2 = []
            for tp in _stage1_parcels:
                _pm = _params_for_g.get(tp['暫編地號'], {})
                ordered_v2.append({
                    'tp': tp, 'pre_position': 0,
                    'is_corner_winner': bool(_pm.get('is_corner', False)),
                    'is_first_corner_marker': bool(_pm.get('is_corner', False)),
                    'side': '中段',
                })
            ordered_v2.sort(key=lambda e: (not e['is_corner_winner'],))
        else:
            _v2_pk_winners = (ss.get('f3_corner_winners', {}) or {}).get(blk_label, {}) or {}
            _v2_forced = (ss.get('f3L_forced_offset', {}) or {}).get(blk_label, {}) or {}
            _v2_fl_p1 = _cad_fl_blk.get('p1'); _v2_fl_p2 = _cad_fl_blk.get('p2')
            # 🆕 W-G.9-161 `L-3′`：透傳之**呼叫端**宣告（實參 ≡ stage1(BUILD_LAYER)）
            ns["_proj_pop_assert_seq"]("stepg:v2_caller",
                                       _stage1_parcels, parcels_in_blk, blk=blk_label)
            _v2_res = _spatial_order_parcels_v2(
                parcels_in_block=_stage1_parcels,   # P2-a：僅階段1宗（遞補宗改走 _place_pool_parcels）
                d_hat=d_hat,
                front_line_p1=_v2_fl_p1,
                front_line_p2=_v2_fl_p2,
                pk_winners=_v2_pk_winners,
                forced_offset=_v2_forced,
            )
            ordered_v2 = list(_v2_res.get('ordered', []) or [])
        for _i_ov2, _e_ov2 in enumerate(ordered_v2):
            _e_ov2['_ov2_idx'] = _i_ov2

        # ── 結構閘 位次＝投影序 ──
        #   ordered_v2 保留投影序（僅 PK winner 最小擾動上位），其 `pre_position` 必逐筆等於
        #   `_projection_order`（純幾何 representative_point 投影）之排名。此為位次價格無關之
        #   機制保證：任何使位次改吃 G/地價之 refactor 立即被逮。
        if not _degenerate_order:
            # 🆕 P2-a／B-2：母體**與 `ordered_v2` 同源**（皆 `_stage1_parcels`）。用未過濾之
            #   `parcels_in_blk` 會使排名把階段2宗一併編號 → 與 `pre_position` 對不上 → 本閘必 raise。
            # 🆕 W-G.9-161 `L-3′` `POP_SYNC`：實參 ≡ stage1(BUILD_LAYER)
            ns["_proj_pop_assert_seq"]("stepg:_proj_rank",
                                       _stage1_parcels, parcels_in_blk, blk=blk_label)
            _proj_rank = {tp['暫編地號']: _i + 1 for _i, tp in enumerate(
                ns["_projection_order"](_stage1_parcels, _cad_fl_blk.get('p1'),
                                        _cad_fl_blk.get('p2')))}
            _pos_bad = [(e['tp']['暫編地號'], e.get('pre_position'),
                         _proj_rank.get(e['tp']['暫編地號']))
                        for e in ordered_v2
                        if e.get('pre_position') != _proj_rank.get(e['tp']['暫編地號'])]
            if _pos_bad:
                raise RuntimeError(
                    f"🔴 結構閘 位次＝投影序 破：街廓 {blk_label} {len(_pos_bad)} 筆 pre_position "
                    f"≠ _projection_order 排名（暫編, pre_position, 投影排名）={_pos_bad[:3]}")

        # forced buffer（app Phase C 複刻）
        _fo_block = (ss.get('f3L_forced_offset', {}) or {}).get(blk_label, {})
        _fo_left = bool(_fo_block.get('left_forced_offset', False))
        _fo_right = bool(_fo_block.get('right_forced_offset', False))
        _row_for_buffer = rows_by_lbl.get(blk_label)
        _left_buffer_S = 0.0
        _right_buffer_S = 0.0
        if _row_for_buffer and avg_depth_default > 0:
            # 🆕 §3（plan v3 §3·補丁九）：廢矩形近似 `range ÷ avg_depth` → `_corner_buffer_S`
            #   幾何 bisect（真實斜交池帶面積 == range）·side 參數化（#25）·byte 級對映 app（N0-16）。
            if _fo_left:
                _l_min = _row_for_buffer.get('【左】街角最小面積(㎡)')
                try:
                    if _l_min is not None and _l_min != float('inf'):
                        _left_buffer_S = _corner_buffer_S(
                            blk_poly, d_hat, corner_pt, allocation_dir_block,
                            float(_l_min), 'left', _label=blk_label)
                except (TypeError, ValueError) as _e_cb:
                    # KL WATCH 2026-07-20（no-silent-fallback）：range 型別壞→靜默 0 改 loud（上游 is not None/!=inf 已擋·罕觸）
                    print(f"🔴 街廓 {blk_label} 左街角 range={_l_min!r} 型別異常（{_e_cb}）·buffer 退 0·入報告")
                    _left_buffer_S = 0.0
            if _fo_right:
                _r_min = _row_for_buffer.get('【右】街角最小面積(㎡)')
                try:
                    if _r_min is not None and _r_min != float('inf'):
                        _right_buffer_S = _corner_buffer_S(
                            blk_poly, d_hat, corner_pt, allocation_dir_block,
                            float(_r_min), 'right', _label=blk_label)
                except (TypeError, ValueError) as _e_cb:
                    # KL WATCH 2026-07-20（no-silent-fallback）：range 型別壞→靜默 0 改 loud（上游 is not None/!=inf 已擋·罕觸）
                    print(f"🔴 街廓 {blk_label} 右街角 range={_r_min!r} 型別異常（{_e_cb}）·buffer 退 0·入報告")
                    _right_buffer_S = 0.0

        # 角側常數（W-C §3；F/l₁ 與 J 權重三處一源）
        _side_lines_blk = (ss.get('f3_cad_side_lines_by_side', {}) or {}).get(blk_label, {}) or {}
        _sl_left = _side_lines_blk.get('left') or {}
        _sl_right = _side_lines_blk.get('right') or {}
        _side_mid_left = _sl_left.get('mid')
        _side_mid_right = _sl_right.get('mid')
        _has_left_corner = _side_mid_left is not None
        _has_right_corner = _side_mid_right is not None
        _F_left = float(sb_row.get('左側長度(m)', 0.0) or 0.0) if _has_left_corner else 0.0
        _lside_left = float(sb_row.get('左側尺度', 0.0) or 0.0) if _has_left_corner else 0.0
        _F_right = float(sb_row.get('右側長度(m)', 0.0) or 0.0) if _has_right_corner else 0.0
        _lside_right = float(sb_row.get('右側尺度', 0.0) or 0.0) if _has_right_corner else 0.0
        _n_alloc_blk = allocation_dir_block
        _cos_dn = 1.0
        if _n_alloc_blk is not None and d_hat is not None:
            try:
                _dh0 = _np_d.asarray(d_hat, dtype=float)
                _dl0 = float(_np_d.linalg.norm(_dh0))
                if _dl0 > 1e-9:
                    _cos_dn = abs(float(_np_d.dot(
                        _dh0 / _dl0, _np_d.asarray(_n_alloc_blk, dtype=float))))
            except Exception:
                _cos_dn = 1.0
        _mw_blk = float((ss.get('f3_min_width_by_label', {}) or {}).get(blk_label, 0.0) or 0.0)

        def _mark_zaling(_res):
            _pw = float(_res.get('S', 0.0)) * _cos_dn
            _res['_宗地寬度'] = round(_pw, 2)
            _res['_畸零旗標'] = ('⚠️移出/第1調配順位'
                                 if (_mw_blk > 0 and _pw < _mw_blk) else '')
            return _res

        # 條件③：J 非零看守（headless fail-hard 版 warn-on-zero-weight）
        for _side_nm_w2, _has_w2, _F_w2, _l1_w2 in (
                ('左', _has_left_corner, _F_left, _lside_left),
                ('右', _has_right_corner, _F_right, _lside_right)):
            if _has_w2 and (_F_w2 * _l1_w2) <= 0.0:
                raise RuntimeError(
                    f"條件③ J 非零看守破：街廓 {blk_label} {_side_nm_w2}側有 SIDE_LINE 但 "
                    f"F×l₁={_F_w2:.2f}×{_l1_w2:.2f}=0（快照 負擔尺度_輸入 未正確消費？）")

        # ── 可重入推進（app _advance_block_with_split 逐行複刻；headless 無 st 訊息） ──
        def _advance_block_with_split(_k_split, _commit):
            _N_f = len(ordered_v2)
            if _N_f == 0:
                left_group = []; right_group = []
            elif _degenerate_order or _k_split >= _N_f:
                left_group = list(ordered_v2); right_group = []
            elif _k_split <= 0:
                left_group = []; right_group = list(reversed(ordered_v2))
            else:
                left_group = list(ordered_v2[:_k_split])
                right_group = list(reversed(ordered_v2[_k_split:]))
            for _idx_l, _e in enumerate(left_group):
                if _idx_l == 0 and _e.get('is_first_corner_marker', False):
                    _e['side'] = '左側'
                else:
                    _e['side'] = '無'
            for _idx_r, _e in enumerate(right_group):
                if _idx_r == 0 and _e.get('is_first_corner_marker', False):
                    _e['side'] = '右側'
                else:
                    _e['side'] = '無'

            _rows_local = []
            _trace_local = {}
            _widths_local = [0.0] * _N_f

            left_cum_S = float(_left_buffer_S)
            right_cum_S = float(_right_buffer_S)
            # W₀＝該側 Rw 累積起算點（telescoping 閘用：ΣRw_側 = R(W_final) − R(W₀)）。
            #   🆕 W 正典（脫鉤 S·da6acf1/補丁七）：W₀ 改＝**首宗近側 KL W**（mp→首宗近側界線＝
            #   res['W_near']）·非舊 `buffer·cos_dn`（群起點 telescoping 約定·已隨 W 脫鉤作廢）。
            #   首宗解出後捕獲（首宗＝角落宗·其近側＝buffer 之遠緣）。
            _W0_left = 0.0; _W0_right = 0.0
            _W0_left_set = False; _W0_right_set = False
            _Wfirst_left = 0.0; _Wfirst_right = 0.0   # 首宗下限（補丁六 §二）：首宗角落宗 KL W（=res['W']=W_far）
            _W_prev_left = 0.0
            _W_prev_right = 0.0
            # 🆕 D-2b-23【甲】：**界面單線鏈**（與 `_W_prev` 同法 thread·⛔ 兩者不同物）。
            #   值 ＝ **前一宗**之 `res['_alloc_dir_used']`（＝其遠側界方向源）；
            #   首宗 None ⇒ 單線·逐位不變。⛔ **無條件 thread**（不看 `_has_*_corner`）。
            #   ⚠️ app 側鏡射：`grep -n "界面單線鏈" app.py`（#20 四處同改之同源要求）。
            _near_dir_left = None
            _near_dir_right = None
            first_corner_used_left = False
            left_results = []
            for entry in left_group:
                tp = entry['tp']
                k = tp['暫編地號']
                if '分攤登記面積_m2' in tp:
                    a_m2 = round(float(tp.get('分攤登記面積_m2', 0) or 0)
                                 + float(tp.get('面積_m2', 0) or 0), 2)
                else:
                    a_m2 = round(float(tp.get('面積_m2', 0) or 0), 2)
                side = entry.get('side', '無')
                is_corner_marked = bool(entry.get('is_corner_winner', False))
                is_first_corner_l = (
                    bool(entry.get('is_first_corner_marker', False))
                    and not first_corner_used_left
                )
                if _has_left_corner:
                    l_side_use = _lside_left; F_use = _F_left
                else:
                    l_side_use = 0.0; F_use = 0.0
                zone = tp.get('重劃前地價區段', '')
                post_p = post_price_by_block.get(blk_label, 0.0)
                pre_p = pre_price_by_zone.get(zone, 0.0)
                A_ratio = (post_p / pre_p) if (pre_p > 0 and post_p > 0) else 1.0
                S_remain = max(0.1, S_block_max - left_cum_S - right_cum_S)
                baseline_pt = (corner_pt + left_cum_S * d_hat
                               if (d_hat is not None and corner_pt is not None) else None)
                res, solver_label = _solve_one(
                    a_m2, A_ratio, l_front, l_side_use, F_use,
                    blk_poly, d_hat, baseline_pt, S_remain,
                    is_first_corner_l, side, avg_depth_default,
                    _allocation_dir=allocation_dir_block,
                    _side_mid=(_side_mid_left if _has_left_corner else None),
                    _W_prev=_W_prev_left,
                    _near_dir=_near_dir_left,   # 🆕 D-2b-23【甲】
                )
                if _has_left_corner:
                    if not _W0_left_set:
                        _W0_left = float(res.get('W_near', 0.0)); _W0_left_set = True
                        _Wfirst_left = float(res.get('W', 0.0))   # 首宗下限：首宗角落宗 KL W（=W_far）
                    _W_prev_left = float(res.get('W_far', _W_prev_left))
                # 🆕 D-2b-23【甲】：本宗之遠側界 ⇒ 下一宗之近側界（⛔ 無條件）
                _near_dir_left = res.get('_alloc_dir_used')
                _S_actual = float(res.get('S_raw', res.get('S', 0.0)))   # S0d：推進吃全精度 S_raw（補丁四 §二·#20 四處同改）
                _G_target = float(res.get('G', 0.0))
                _area_actual = float(res.get('area_geom', 0.0))
                if (abs(_S_actual - S_remain) < 0.05 and _G_target > 0
                    and _area_actual < _G_target * 0.95):
                    res['是否收斂_override'] = '⚠️ 空間不足(夾擠限制)'
                left_cum_S += _S_actual
                res['_alloc_cum_S'] = left_cum_S
                _mark_zaling(res)
                _widths_local[entry['_ov2_idx']] = float(res.get('_宗地寬度', 0.0) or 0.0)
                if is_first_corner_l:
                    first_corner_used_left = True
                _rows_local.append(_build_g_row(
                    k, tp, blk_label, blk_area, front_len, avg_depth_default,
                    zone, A_ratio, l_front, l_side_use, F_use, is_corner_marked,
                    is_first_corner_l, side, res, solver_label, 'left',
                ))
                _trace_local[k] = res.get('trace', [])
                left_results.append((entry, res))

            if d_hat is not None and corner_pt is not None and blk_meta.get('vertices'):
                # 🆕 step 0（正交→斜交 s_max·plan v3 §2·#20 四處同源 _oblique_s_max）
                _smax_a = _oblique_s_max(blk_meta['vertices'], d_hat, corner_pt, allocation_dir_block)
                actual_max_proj = _smax_a if _smax_a is not None else S_block_max
                end_pt = corner_pt + actual_max_proj * d_hat
                d_hat_rev = -d_hat
            else:
                actual_max_proj = S_block_max
                end_pt = None
                d_hat_rev = None

            first_corner_used_right = False
            right_results = []
            for entry in right_group:
                tp = entry['tp']
                k = tp['暫編地號']
                if '分攤登記面積_m2' in tp:
                    a_m2 = round(float(tp.get('分攤登記面積_m2', 0) or 0)
                                 + float(tp.get('面積_m2', 0) or 0), 2)
                else:
                    a_m2 = round(float(tp.get('面積_m2', 0) or 0), 2)
                side = entry.get('side', '無')
                is_corner_marked = bool(entry.get('is_corner_winner', False))
                is_first_corner_r = (
                    bool(entry.get('is_first_corner_marker', False))
                    and not first_corner_used_right
                )
                if _has_right_corner:
                    l_side_use = _lside_right; F_use = _F_right
                else:
                    l_side_use = 0.0; F_use = 0.0
                zone = tp.get('重劃前地價區段', '')
                post_p = post_price_by_block.get(blk_label, 0.0)
                pre_p = pre_price_by_zone.get(zone, 0.0)
                A_ratio = (post_p / pre_p) if (pre_p > 0 and post_p > 0) else 1.0
                S_remain = max(0.1, actual_max_proj - left_cum_S - right_cum_S)
                baseline_pt = (end_pt + right_cum_S * d_hat_rev
                               if (d_hat_rev is not None and end_pt is not None) else None)
                res, solver_label = _solve_one(
                    a_m2, A_ratio, l_front, l_side_use, F_use,
                    blk_poly, d_hat_rev, baseline_pt, S_remain,
                    is_first_corner_r, side, avg_depth_default,
                    _allocation_dir=allocation_dir_block,
                    _side_mid=(_side_mid_right if _has_right_corner else None),
                    _W_prev=_W_prev_right,
                    _near_dir=_near_dir_right,   # 🆕 D-2b-23【甲】
                )
                if (float(res.get('area_geom', 0)) < 0.5
                    and d_hat_rev is not None and baseline_pt is not None):
                    for _adj in (0.1, 0.3, 0.5):
                        _try_pt = baseline_pt + _adj * d_hat_rev
                        _try_S = max(0.1, S_remain - _adj)
                        _r2, _sl2 = _solve_one(
                            a_m2, A_ratio, l_front, l_side_use, F_use,
                            blk_poly, d_hat_rev, _try_pt, _try_S,
                            is_first_corner_r, side, avg_depth_default,
                            _allocation_dir=allocation_dir_block,
                            _side_mid=(_side_mid_right if _has_right_corner else None),
                            _W_prev=_W_prev_right,
                            _near_dir=_near_dir_right,   # 🆕 D-2b-23【甲】
                        )
                        if float(_r2.get('area_geom', 0)) >= 0.5:
                            res, solver_label = _r2, _sl2
                            break
                if _has_right_corner:
                    if not _W0_right_set:
                        _W0_right = float(res.get('W_near', 0.0)); _W0_right_set = True
                        _Wfirst_right = float(res.get('W', 0.0))   # 首宗下限：首宗角落宗 KL W（=W_far）
                    _W_prev_right = float(res.get('W_far', _W_prev_right))
                # 🆕 D-2b-23【甲】：本宗之遠側界 ⇒ 下一宗之近側界（⛔ 無條件）
                _near_dir_right = res.get('_alloc_dir_used')
                _S_actual = float(res.get('S_raw', res.get('S', 0.0)))   # S0d：推進吃全精度 S_raw（補丁四 §二·#20 四處同改）
                _G_target = float(res.get('G', 0.0))
                _area_actual = float(res.get('area_geom', 0.0))
                if (abs(_S_actual - S_remain) < 0.05 and _G_target > 0
                    and _area_actual < _G_target * 0.95):
                    res['是否收斂_override'] = '⚠️ 空間不足(夾擠限制)'
                right_cum_S += _S_actual
                res['_alloc_cum_S'] = right_cum_S
                _mark_zaling(res)
                _widths_local[entry['_ov2_idx']] = float(res.get('_宗地寬度', 0.0) or 0.0)
                if is_first_corner_r:
                    first_corner_used_right = True
                _rows_local.append(_build_g_row(
                    k, tp, blk_label, blk_area, front_len, avg_depth_default,
                    zone, A_ratio, l_front, l_side_use, F_use, is_corner_marked,
                    is_first_corner_r, side, res, solver_label, 'right',
                ))
                _trace_local[k] = res.get('trace', [])
                right_results.append((entry, res))

            return {
                'rows': _rows_local, 'trace': _trace_local,
                'widths': _widths_local,
                'left_cum_S': left_cum_S, 'right_cum_S': right_cum_S,
                'left_results': left_results, 'right_results': right_results,
                'W0_left': _W0_left, 'W0_right': _W0_right,
                'Wf_left': _W_prev_left, 'Wf_right': _W_prev_right,
                'Wfirst_left': _Wfirst_left, 'Wfirst_right': _Wfirst_right,   # 首宗下限（補丁六 §二）
            }

        # 選槽 orchestration（app 同構）
        _N = len(ordered_v2)
        _k_naive = (_N + 1) // 2 if _N % 2 == 1 else _N // 2
        _slot_res = None
        if _degenerate_order or _N <= 1:
            _k_star = _N
            _adv_final = _advance_block_with_split(_k_star, True)
        else:
            _adv_base = _advance_block_with_split(_k_naive, False)
            # 🆕 W 正典 W₀（補丁八 §一·脫鉤 S）：選槽理論之 forced 起始 W 改＝**首宗近側 KL W**
            #   ＝(群起點 + buffer·d̂ − mp)·â_定向·取代舊 `buffer·cos_dn`（群起點 telescoping 約定·已作廢）。
            #   使 _select_pool_slot 之理論 ΣRw 與實跑（solve_G_binary KL W）同源（理論＝實跑閘·禁 #20 脫鉤）。
            def _mp_base_W0(_gs, _buf, _dv, _mp, _adir):
                # 🔒 **W-G.9-4（expand）：改為<u>純委派</u>至 app 之單一產生者**
                #   `k956_W_from_mp`（`grep -n "def k956_W_from_mp" app.py`）。
                #   ⛔ **語意不變、簽章不變**——本處僅把「群起點沿 d̂ 推進 `_buf`」算成點，
                #   再交由單一產生者量 `W = dot(P − mp, â_定向)`。
                #   案由：`GB-48` 族（同述詞多處定義·無同步機制）⇒ **W 之定義只留一份**。
                #   ⚠️ `_du` 於此仍需自算（因 `P` 之構成需要它）；其式**逐字同原碼**，
                #      ⛔ 不得改為先正規化再傳（會改變 `_dn ≤ 1e-9` 之退化行為）。
                if _gs is None or _mp is None or _adir is None or _dv is None:
                    return 0.0
                _dv2 = _np_d.asarray(_dv, dtype=float); _dn = float(_np_d.linalg.norm(_dv2))
                _du = _dv2 / _dn if _dn > 1e-9 else _dv2
                _bp0 = _np_d.asarray(_gs, dtype=float) + float(_buf) * _du
                return float(_k956_W_from_mp(_bp0, _mp, _adir, _dv))
            # 右組群起點 end_pt 於外層重算（_advance_block_with_split 內 end_pt 為其局部·此處不可見）。
            #   🆕 step 0（正交→斜交 s_max·plan v3 §2）：與 app／wf_f4 **四處同源** `_oblique_s_max`（#20·`grep -n "_oblique_s_max" verify/stepg_pipeline.py`）。
            _end_pt_o = None; _dhr_o = None
            if d_hat is not None and corner_pt is not None and blk_meta.get('vertices'):
                _smax_o = _oblique_s_max(blk_meta['vertices'], d_hat, corner_pt, allocation_dir_block)
                if _smax_o is not None:
                    _end_pt_o = corner_pt + _smax_o * _np_d.asarray(d_hat, dtype=float)
                    _dhr_o = -_np_d.asarray(d_hat, dtype=float)
            # 🔒 K-9-5-12（五）-1「首宗起點一律為 0」＋ K-9-5-13 裁定二「起算一律用真正的地界」
            #    ⇒ 非 forced 之選槽起算點校回 0（施工單 W-G.9-27·影響估算見 W-G.9-23）。
            #    ⛔ forced 側維持原式——其目標為抵費地遠側界，卡「保留區之表示法」（W-G.9-19 D3）。
            _b_L0 = _mp_base_W0(corner_pt, _left_buffer_S, d_hat, _side_mid_left, allocation_dir_block) if _fo_left else 0.0
            _b_R0 = _mp_base_W0(_end_pt_o, _right_buffer_S, _dhr_o, _side_mid_right, allocation_dir_block) if _fo_right else 0.0
            _slot_res = _select_pool_slot(
                _adv_base['widths'],
                {'has': _has_left_corner, 'F': _F_left,
                 'l1': _lside_left, 'b': _b_L0},
                {'has': _has_right_corner, 'F': _F_right,
                 'l1': _lside_right, 'b': _b_R0},
            )
            _k_star = int(_slot_res['k'])
            _J_by_k = {t['k']: t['J'] for t in _slot_res['table']}
            if (_k_naive in _J_by_k
                    and _J_by_k.get(_k_star, 0.0) < _J_by_k[_k_naive] - 1e-9):
                raise RuntimeError(
                    f"停機②（J 下降）街廓 {blk_label}：J(k*)<J(naive)")
            _adv_final = _advance_block_with_split(_k_star, True)

        # ── 🆕 §4 P2-e 階段2 落位接線（B-1·**守恆核心**）────────────────────────────
        #   ⚠️ **W-10**：本區塊置於 if/else **匯流之後**——`_adv_final` 有**兩個**產生點
        #     （degenerate／`N≤1` 分支 與 正常分支）；置於 else 內會漏接前者，且兩階段化後
        #     `N≤1` 機率**上升**（過濾後 R4 僅餘 2 宗）。
        #   ⚠️ **B-1**：階段2 rows **必須就地擴充 `_adv_final`**、不可只 append 進 `g_rows`——
        #     `g_rows` 僅輸出容器；守恆帳來源是 `_adv_final['rows']`（§N3-0 逐宗主閘／
        #     守恆-帳幾何級）與 `allocated_polys`（← left/right_results）。三種錯法：
        #       · 只進 `g_rows`      ⇒ 池帶仍覆蓋階段2宗、抵費地列**重算一次**
        #                              ⇒ 守恆**實破** `+ΣG_階段2` 而**閘全綠**（最惡）
        #       · 只進 `_adv_final`  ⇒ 停機③ 立紅
        #       · 只進 allocated_polys ⇒ 停機③ 立紅
        #   ⇒ 池片結算（下方 `_pool_strips_for_block`）**自動**落在階段2 之後：其
        #     `allocated_polys` 由擴充後之 left/right_results 建 ⇒ 池＝階段1殘餘 − 階段2已落位。
        # 三閘合圍之輸入（claude.ai 裁定 2026-07-24·§五 (a) 修正版）：
        #   `_Wf_stage1`＝**階段2 落位前**之該側末 W ⇒ 階段2 恆等式閘之左端點。
        #   `_stage2_ids`＝階段2宗之暫編地號集，**其出處即 `配地階段` 旗標**（資料驅動·
        #     禁 `74·` 名稱前綴判別）；供「理論=實跑」閘過濾出**階段1子集**。
        #   ⚠️ 二者**不得**改動 `_rw_real_wd2` 之全域母體——該函式為 telescoping 閘與
        #     CSV 欄共用，其總量守備涵蓋階段1＋2，縮之即失守。
        _Wf_stage1 = {'left': float(_adv_final.get('Wf_left', 0.0) or 0.0),
                      'right': float(_adv_final.get('Wf_right', 0.0) or 0.0)}
        _stage2_ids = {tp['暫編地號'] for tp in _stage2_parcels}

        if _stage2_parcels:
            _smax_blk = None
            if d_hat is not None and corner_pt is not None and blk_meta.get('vertices'):
                _smax_blk = _oblique_s_max(blk_meta['vertices'], d_hat, corner_pt,
                                           allocation_dir_block)
            _s2 = ns["_place_pool_parcels"](
                stage2_parcels=_stage2_parcels,
                adv_final=_adv_final,
                blk_poly=blk_poly, blk_area=blk_area, blk_label=blk_label,
                blk_vertices=blk_meta.get('vertices'),
                blk_centroid=blk_meta.get('centroid'),
                d_hat=d_hat, corner_pt=corner_pt, s_max_blk=_smax_blk,
                allocation_dir=allocation_dir_block,
                alloc_dir_cad=_alloc_dir_cad,      # ⚠️ CAD 原始 ALLOC 方向（18m 範圍用）·非其 rot90
                front_len=front_len, l_front=l_front, avg_depth=avg_depth_default,
                side_mid_left=_side_mid_left, side_mid_right=_side_mid_right,
                l_side_left=_lside_left, F_left=_F_left,
                l_side_right=_lside_right, F_right=_F_right,
                post_price=post_price_by_block.get(blk_label, 0.0),
                pre_price_by_zone=pre_price_by_zone,
                solve_one=_solve_one, build_g_row=_build_g_row,
                mark_zaling=_mark_zaling,
                # 🆕 P2-f 末端保留（裁定C）：gate 條件1 之資料驅動來源＝`forced[blk]["{side}_has_side"]`
                #   （同 `wf_f4._reshape_block` 之 `_cond1`·`grep -n "_cond1 = not bool" verify/wf_f4.py`·**禁寫死**）；`s_front_p2`＝FRONT p2 之 s 座標，
                #   由恆等式 `s(p1 + L·d̂) ≡ L` 得 ＝ FRONT_LINE 長 `S_block_max`。
                has_side_left=bool(_fo_block.get('left_has_side', True)),
                has_side_right=bool(_fo_block.get('right_has_side', True)),
                min_width=_mw_blk, s_front_p2=S_block_max,
            )
            _adv_final['rows'] = list(_adv_final['rows']) + list(_s2['rows'])
            _adv_final['left_results'] = (list(_adv_final['left_results'])
                                          + list(_s2['left_results']))
            _adv_final['right_results'] = (list(_adv_final['right_results'])
                                           + list(_s2['right_results']))
            # W-3(b)：telescoping 之 `W_final` 須含階段2 落位宗（`ΣRw_側 == R(W_final) − R(W₀)`）；
            #   無跨占之階段2宗不推進該側鏈（其側街負擔=0），由 `_place_pool_parcels` 內把關。
            _adv_final['Wf_left'] = _s2['Wf_left']
            _adv_final['Wf_right'] = _s2['Wf_right']
            # 含階段2 之該側累積推進（app 鏡像據此作溢位警示；此處保持同構、勿分岔）
            _adv_final['left_cum_S'] = _s2['left_cum_S']
            _adv_final['right_cum_S'] = _s2['right_cum_S']
            _stage2_placed[blk_label] = _s2['placed_area']

        g_rows.extend(_adv_final['rows'])
        detail_trace.update(_adv_final['trace'])
        left_results = _adv_final['left_results']
        right_results = _adv_final['right_results']

        # 抵費地幾何（app Task D-3 複刻）
        _pool_total_blk = None
        offset_geoms = []
        if blk_poly is not None:
            try:
                allocated_polys = []
                _missing_owner = []   # 停機③ 修（KL 2026-07-20）：ΣG 成員但無可扣幾何→池雙計·no-silent
                for _entry, _res in (left_results + right_results):
                    _coords = _res.get('cut_coords') or []
                    _p = None
                    if len(_coords) >= 3:
                        try:
                            _p = _SP_d(_coords)
                            if not _p.is_valid:
                                _p = _p.buffer(0)
                        except Exception:
                            _p = None
                    # 停機③ 修（KL 2026-07-20·約束1「判準對齊 ΣG 成員」）：凡算進 ΣG 之 owner 宗皆須自
                    #   池扣其幾何——**廢 area≥0.5 sliver 濾**（1b290e4 遷移遺留·無職·退化守衛係
                    #   len≥3/is_valid/is_empty·非此常數·#26a 已核）。舊 area≥0.5 剔除合法小宗（R2 628-43(1)
                    #   0.27㎡）致池雙計 → 停機③ |Σ(G−幾何)|=0.28（=0.0124 owner 殘差＋0.2681 雙計宗·逐位）。
                    if _p is not None and not _p.is_empty:
                        allocated_polys.append(_p)
                    else:
                        _missing_owner.append(((_entry or {}).get('tp') or {}).get('暫編地號', '?'))
                if _missing_owner:
                    print(f"🔴 停機③-家族：街廓 {blk_label} ΣG 成員無可扣幾何 {_missing_owner}"
                          f"（實切退化/失敗→池將雙計其面積·no-silent-fallback）·入報告")
                # ── §N3-0 T2（主修法）：池片改用與業主宗**同機制·同切線**直接切出 ──
                #   廢：`_uunion_d(allocated_polys).buffer(0.001)` → `difference` → `area >= 1.0`
                #       （buf_leak／gap_union／sliver 三漏之源＋T1 面積判準之誤殺/放行）
                #   單一真相源＝app 之 `_pool_strips_for_block`（ns harvest·同 `_block_strip` 先例）
                #   → stepg／app／wf_f1／wf_f4 四處同源，根絕抄寫複本各自漂移（#20 根因）。
                #   回傳序＝面積遞減（逐字沿用舊慣例）→ g_rows 抵費地序號不因本波改（plan §11）。
                offset_geoms = _pool_strips_for_block(
                    blk_poly, d_hat, corner_pt, allocation_dir_block,
                    allocated_polys, _label=blk_label, _depth=avg_depth_default)
                _pool_total_blk = float(sum(_g.area for _g in offset_geoms))
                _min_block = min(50.0, blk_area * 0.05)
                for _i, _g in enumerate(offset_geoms):
                    _suffix = '' if len(offset_geoms) == 1 else f'-{_i+1}'
                    _conv_flag = ('🟡' if _g.area >= _min_block
                                  else '⚠️ < 最小分配')
                    try:
                        _coords_list = [[float(c[0]), float(c[1])]
                                        for c in list(_g.exterior.coords)]
                    except Exception:
                        _coords_list = []
                    g_rows.append({
                        '暫編地號': f'{blk_label}-抵費地{_suffix}',
                        '原地號': '—',
                        '所屬街廓': blk_label,
                        '重劃前區段': '—',
                        'a 面積(㎡)': 0.0,
                        '街廓面積(㎡)': round(blk_area, 2),
                        '正面長度(m)': round(front_len, 2),
                        '平均深度(m)': round(avg_depth_default, 2),
                        'A 地價比': 0.0,
                        'l₂ 正面尺度': 0.0,
                        'l₁ 側面尺度': 0.0,
                        '街角地': '—',
                        '第1筆街角': '—',
                        '街角側別': '—',
                        'F(m)': 0.0,
                        'W(m)': 0.0,
                        'Rw(%)': 0.0,
                        'S(m)': 0.0,
                        '幾何面積(㎡)': round(_g.area, 2),
                        'G(㎡)': 0.0,
                        '累積S(m)': 0.0,
                        '推進側別': '抵費地',
                        '解法': '幾何剩餘',
                        '迭代次數': 0,
                        '是否收斂': _conv_flag,
                        '負擔比率': 0.0,
                        'cut_coords': _coords_list,
                    })
            except Exception as _eOff:
                raise RuntimeError(f"街廓 {blk_label} 抵費地計算失敗：{_eOff}")

        # 守恆 ledger（app 同構，含 KL 條件④ 對照欄）
        _sum_G_blk = sum(float(r.get('G(㎡)', 0) or 0) for r in _adv_final['rows'])
        _sum_geom_blk = sum(float(r.get('幾何面積(㎡)', 0) or 0)
                            for r in _adv_final['rows'])

        # ── §N3-0 逐宗主閘（緊閘·KL 2026-07-16 裁·補丁三 §二）──────────────
        #   `|G_i − 幾何_i| ≤ 0.005×分配深度 ＋ tol(0.01) ＋ 0.005`
        #   成因＝S0c 令實切用捨入 S（N0-18 公分慣例）而 G 定於未捨入 S_conv → 兩者必差
        #   ≤ S 捨入半量子 × d(面積)/dS。**此差＝對照清冊「增減(㎡)」欄之法定常態**（N0-18 補記）。
        #   **作用＝非捨入成因之病灶於逐宗層立紅，不被下方街廓 Σ 之正負相消淹沒。**
        _tol_lot = _acct_geom_tol_per_lot(avg_depth_default)
        for _r_lot in _adv_final['rows']:
            _dev = abs(float(_r_lot.get('G(㎡)', 0) or 0)
                       - float(_r_lot.get('幾何面積(㎡)', 0) or 0))
            if _dev > _tol_lot:
                raise RuntimeError(
                    f"🔴 §N3-0 逐宗主閘破：街廓 {blk_label} 宗 {_r_lot.get('暫編地號', '?')}："
                    f"|G − 幾何| = {_dev:.4f} > 上界 {_tol_lot:.4f}"
                    f"（0.005×深度{avg_depth_default:.2f} ＋ tol 0.01 ＋ 0.005）"
                    f"——**超出捨入量子可解釋範圍＝另有病**，停")
        _corner_off_L = (float(_v2_res.get('left_corner_offset_area', 0.0) or 0.0)
                         if _v2_res else 0.0)
        _corner_off_R = (float(_v2_res.get('right_corner_offset_area', 0.0) or 0.0)
                         if _v2_res else 0.0)

        def _rw_real_wd2(_side_tag):
            # **全域母體（階段1＋2）·勿縮**：telescoping 閘（總量段）與 CSV 欄共用。
            return round(sum(float(r.get('Rw(%)', 0) or 0)
                             for r in _adv_final['rows']
                             if r.get('推進側別') == _side_tag
                             and float(r.get('F(m)', 0) or 0) > 0), 2)

        def _rw_stage1_only(_side_tag):
            """**僅供「理論＝實跑」閘**：階段1子集之 ΣRw（資料驅動·母體出處＝`配地階段` 旗標）。

            理論側 `_select_pool_slot` 之 `widths` 結構上**只可能**含階段1宗——選槽於階段2
            存在**之前**執行（裁定B 已鎖時序：k* 先於階段2）。故同類相比之對象即本子集。
            **不改 `_rw_real_wd2`**：階段2 之 Rw 仍由下方「階段2 恆等式閘」與「telescoping
            總量閘」兩道看守，守備零縮（三閘合圍）。
            """
            return round(sum(float(r.get('Rw(%)', 0) or 0)
                             for r in _adv_final['rows']
                             if r.get('推進側別') == _side_tag
                             and float(r.get('F(m)', 0) or 0) > 0
                             and r.get('暫編地號') not in _stage2_ids), 2)
        # ══ 🆕 D-2b-3 §二（`K-9-5-5`）：**逐界面鏈斷量 `Δ_i`** ＝ 三閘之<u>單一產生器</u> ══
        #   恆等式（telescoping 之**一般化**·⛔ 非放寬）：
        #       ΣRw_側 == [R(W_final) − R(W₀)] − Σ_i Δ_i      ，   Δ_i ≡ R(W_near,{i+1}) − R(W_far,i)
        #   推導：每宗 `Rw_i = R(W_far,i) − R(W_near,i)`（`grep -n "Rw = rw_increment" app.py`）
        #     ⇒ ΣRw = R(W_far,N) − R(W_near,1) − Σ_{i<N}[R(W_near,{i+1}) − R(W_far,i)]。
        #   ⇒ 鏈**連續**（`W_near,{i+1} == W_far,i`）時 `Δ_i ≡ 0`、**退化為原式**
        #     ⇒ ⛔ 未放寬 `0.1`、⛔ 未刪閘、⛔ 未整側豁免（僅把「鏈斷」由**隱式失敗**改為**顯式帳目**）。
        #   **授權界面判準 ＝ 方向**（`K-9-5-5`）：第 i 宗之**遠側界方向 ≠ 街廓 ALLOC 方向**。
        #     方向之來源 ＝ **生產路徑輸出** `res['_alloc_dir_used']`（`app.py` `_solve_G_one` 純加性欄）
        #     ——⛔ **不**由 harness 依 `is_corner` 重算：重算則「判準集合 == 標記集合」淪為**套套邏輯**
        #     （`fixture-provenance`：期望值不得由受測邏輯自產）。⛔ 禁以街廓名／側別字串／宗序號硬編。
        _IFACE_TOL = 0.1                 # ＝既有三閘之容差·🔒 本批未放寬
        _PAR_TOL = 1e-6                  # 方向平行判定（|cross| of unit vectors）

        def _dir_is_alloc(_d_used):
            """`_d_used` 是否 ∥ 街廓 ALLOC（含反向）。⛔ 資料驅動·不看名稱／序號。"""
            if _d_used is None or allocation_dir_block is None:
                return True              # 無方向資訊 ⇒ 視同未偏離（⛔ 不誤判為授權界面）
            _u = _np_d.asarray(_d_used, dtype=float)
            _v = _np_d.asarray(allocation_dir_block, dtype=float)
            _nu = float(_np_d.linalg.norm(_u)); _nv = float(_np_d.linalg.norm(_v))
            if _nu < 1e-12 or _nv < 1e-12:
                return True
            return abs(float(_np_d.cross(_u / _nu, _v / _nv))) <= _PAR_TOL

        def _chain(_side_tag, _stage=None):
            """該側之**推進鏈**（順序＝實際推進序）。`_stage`：None 全體／1 階段1／2 階段2。

            母體與 `_rw_real_wd2` 對齊（`推進側別==side` 且 `F>0`）——⛔ 鏈母體與 ΣRw 母體
            不同源即為假閘（同 `_rw_stage1_only` docstring 之「同類相比」紀律）。
            """
            _rw_by_id = {r.get('暫編地號'): r for r in _adv_final['rows']
                         if r.get('推進側別') == _side_tag}
            _out = []
            for _e, _r in (_adv_final.get(f'{_side_tag}_results', []) or []):
                _id = _e['tp'].get('暫編地號')
                _row = _rw_by_id.get(_id)
                if _row is None or float(_row.get('F(m)', 0) or 0) <= 0:
                    continue
                _is_s2 = _id in _stage2_ids
                if _stage == 1 and _is_s2:
                    continue
                if _stage == 2 and not _is_s2:
                    continue
                _out.append({'id': _id, 'res': _r, 'row': _row, 'stage2': _is_s2,
                             'marker': bool(_e.get('is_first_corner_marker', False))})
            return _out

        def _iface_deltas(_nodes, _w0_prev=None):
            """逐界面 `Δ_i`（⛔ §二-1：必逐筆計算並印出·不得只印總和／只印過否）。

            `_w0_prev` 非 None ⇒ 於鏈首**前置**一個虛擬界面（上一段之 `W_far`），
            供「階段2 段」量測其與階段1 末之銜接（三閘共用同一產生器·§二-4）。
            """
            _out = []
            _prev_far, _prev_id, _prev_dir = _w0_prev, '（上段末）', None
            _prev_marker = False
            for _n in _nodes:
                _wnear = float(_n['res'].get('W_near', 0.0) or 0.0)
                # 🆕 D-2b-4 §四(b)：`Δ_i` 改量**實際鏈起點**（`K-9-5-6` 之 `W_rw_start`），
                #   ⛔ 非本宗自量之 `W_near`。⇒ 鏈若真的續上，`Δ_i` 恆 0（**含授權界面**）。
                #   ⚠️ **非套套邏輯**：`W_rw_start` 由**生產路徑**（`solve_G_binary`）依外層 thread
                #     之 `W_prev` 決定；若推進迴圈漏 thread、或走錯分支，本式即非 0。
                _wstart = _n['res'].get('W_rw_start')
                _wstart = _wnear if _wstart is None else float(_wstart)
                if _prev_far is not None:
                    _out.append({
                        'lot': _prev_id, 'next': _n['id'],
                        'W_far_i': _prev_far, 'W_near_next': _wnear,
                        'W_start_next': _wstart,
                        'delta': _rw_from_width(_wstart) - _rw_from_width(_prev_far),
                        # 診斷：舊式（本宗自量近側）之鏈斷量＝`K-9-5-6` 所修之**帳務漏項**
                        'delta_self': _rw_from_width(_wnear) - _rw_from_width(_prev_far),
                        'authorized': (_prev_dir is not None
                                       and not _dir_is_alloc(_prev_dir)),
                        'dir_used': _prev_dir,
                        'marker': _prev_marker,
                    })
                _prev_far = float(_n['res'].get('W_far', 0.0) or 0.0)
                _prev_id = _n['id']
                _prev_dir = _n['res'].get('_alloc_dir_used')
                _prev_marker = bool(_n['marker'])
            return _out

        def _fmt_ifaces(_tag, _ifs):
            # §四(c)：逐界面必印 `W_far,i`／`W_near,{i+1}`／`Δ_i`／是否方向改變（⛔ 禁只印總和）
            return (f"[Δ_i·{blk_label}·{_tag}] " + ("（無界面）" if not _ifs else "　".join(
                f"{d['lot']}→{d['next']}: W_far={d['W_far_i']:.4f}"
                f"／W_near={d['W_near_next']:.4f}／W_start={d['W_start_next']:.4f}"
                f"／Δ={d['delta']:+.4f}／Δ_self={d['delta_self']:+.4f}"
                f"{'／🔄方向改變' if d['authorized'] else ''}"
                for d in _ifs)))

        def _side_alloc_degenerate(_side_tag):
            """🆕 **`K-9-5-8`（D-2b-8 §A-2）**：該側 `SIDE` 與街廓 `ALLOC` 是否**幾何上退化為平行**。

            KL 裁（逐字）：「**有可能使用者於該街廓就是依據某側的 SIDELINE 方向畫設 ALLOCLINE。**」
            ⇒ `SIDE ∥ ALLOC` 係**使用者畫設選擇**、**預期且合法**；退化時 `K-9-5-4 ②` 之
            `rot90_cw(SIDE)` **恰等於** `allocation_dir_block`（＝`rot90(ALLOC_cad)`）
            ⇒ 方向「**套用了但等值**」、**無楔形**、配地結果與未套用相同。
            ⛔ **不得視為異常、不得據以判定圖資有誤**（`K-9-5-8`）。

            🔒 **容差與 `_dir_is_alloc` 同源**（`_PAR_TOL`）——⛔ 不另立門檻。
            🔒 **由幾何算出**（量 `SIDE` 與 `ALLOC_cad` 之 `|cross|`），
               ⛔ **不是**「是否為街角第 1 宗」（那才是套套邏輯）。
            回傳 (是否退化, |cross|, 夾角度數)；缺 SIDE／ALLOC ⇒ (False, None, None)。
            """
            _sd = (_side_lines_blk.get(_side_tag) or {})
            _p1 = _sd.get('p1'); _p2 = _sd.get('p2')
            if _p1 is None or _p2 is None or _alloc_dir_cad is None:
                return False, None, None
            _v = _np_d.asarray(_p2, dtype=float)[:2] - _np_d.asarray(_p1, dtype=float)[:2]
            _a = _np_d.asarray(_alloc_dir_cad, dtype=float)[:2]
            _nv = float(_np_d.linalg.norm(_v)); _na = float(_np_d.linalg.norm(_a))
            if _nv < 1e-12 or _na < 1e-12:
                return False, None, None
            _c = abs(float(_np_d.cross(_v / _nv, _a / _na)))
            return (_c <= _PAR_TOL), _c, float(_np_d.degrees(_np_d.arcsin(min(1.0, _c))))

        def _guard_auth_scope(_side_tag, _nodes, _ifs):
            """**範圍守衛**（`K-9-5-5` 之範圍限制）：符合判準者須**恰為街角第 1 宗**；不符 ⇒ loud raise。

            ⛔ 非套套邏輯——`authorized` 由**生產輸出之方向**判定、退化由**幾何**判定，
            `marker` 由**選角流程**標記，三者來源不同 ⇒ 本斷言確實可能失敗。

            🆕 **D-2b-8 §A-2 修正**：原以「方向 ≠ ALLOC」為**充要**條件 ⇒ 於 `SIDE ∥ ALLOC`
            之合法退化（`K-9-5-8`）**誤報**（實測 R6/right 夾角 `0.000003°`）。
            改為：**「方向已改變」<u>或</u>「該側 SIDE 與 ALLOC 幾何退化為平行」**皆算符合。
            ⛔ **未**改成「是否為街角第 1 宗」。

            🔴 **D-2b-9 §A′-1 修正（承重·⛔ 勿再退回豁免）**：D-2b-8 之退化分支為
            `print(...)` 後**直接 `return`** ⇒ **整條斷言被跳過**＝該側守衛**全失效**。
            實料 `verify/out/probe_D2b8_guard.log`【A-2】逐字：該側
            `方向判準所得 []／街角第 1 宗 ['628-18(1)']` —— **兩者不等**，
            若無短路即會 raise ⇒ **短路是承重的、不是裝飾**。
            而 `K-9-5-8` 已裁 `SIDE ∥ ALLOC` 係**使用者畫設選擇**、**會重複出現**
            ⇒ 換案必然踩到 ⇒ 「豁免」等於把守衛在整類街廓上關掉。

            **改法（判準理由·⛔ 不得省略）**：退化側**兩方向等值**
            ⇒ 方向判準之**正確輸出即空集合**。故退化側改斷言 **`_auth_lots` 必為空**。
            此斷言**可證偽**，能抓到：`_alloc_dir_used` 來源錯誤／`_PAR_TOL` 與
            `_dir_is_alloc` 不同源／`rot90` 方向約定翻轉。
            ⛔ **不得**改以「是否為街角第 1 宗」判定（套套邏輯）。
            ⛔ **不得**把 `_expect` 納入本斷言——退化側**仍有**街角第 1 宗，
               `_expect` 非空**屬正常**。
            """
            _deg, _cx, _ang = _side_alloc_degenerate(_side_tag)
            _auth = [d for d in _ifs if d['authorized']]
            _auth_lots = [d['lot'] for d in _auth]
            _marked = [_n['id'] for _n in _nodes if _n['marker']]
            _expect = [_l for _l in _marked if any(d['lot'] == _l for d in _ifs)]
            if _deg:
                # 退化命中：印出**實測夾角**（⛔ 不得靜默略過·§A-2）
                print(f"[K-9-5-8] 街廓 {blk_label} {_side_tag} 側：SIDE ∥ ALLOC **退化**"
                      f"（|cross|={_cx:.10f}／夾角={_ang:.6f}°　≤ 容差 {_PAR_TOL:g}）"
                      f"⇒ `K-9-5-4 ②` 套用後方向等值、無楔形；"
                      f"方向判準所得 {_auth_lots}／街角第 1 宗 {_expect}"
                      f"——**合法組態·⛔ 非異常**（KL 裁 2026-08-08）")
                # 🔴 **D-2b-9 §A′-1**：退化側**仍須守衛**（⛔ 非豁免）——兩方向等值
                #   ⇒ 正確輸出即空集合；非空即代表方向來源或容差不同源。
                if _auth_lots:
                    raise RuntimeError(
                        f"🔴 K-9-5-5 範圍守衛破（退化側）：街廓 {blk_label} {_side_tag} 側 "
                        f"SIDE∥ALLOC 退化（|cross|={_cx:.10f}／夾角={_ang:.6f}°）"
                        f"⇒ `K-9-5-4 ②` 之遠側界方向與 ALLOC **等值**、"
                        f"不應有任何界面被判為「方向已改變」；"
                        f"實得授權界面 {_auth_lots}——方向來源或容差不同源（停機上呈）")
                return _auth
            if _auth_lots != _expect:
                raise RuntimeError(
                    f"🔴 K-9-5-5 範圍守衛破：街廓 {blk_label} {_side_tag} 側 "
                    f"方向判準所得授權界面 {_auth_lots} ≠ 街角第 1 宗 {_expect}"
                    f"（該側非 SIDE∥ALLOC 退化：|cross|="
                    f"{('%.10f' % _cx) if _cx is not None else '—'}）"
                    f"——`K-9-5-5` 限街角第 1 宗，⛔ 不得推廣至其他宗／界面（停機上呈）")
            return _auth

        _tbl_wd2 = (_slot_res or {}).get('table') or []
        _row_at = {t['k']: t for t in _tbl_wd2}
        _t_star = _row_at.get(_k_star, {})
        _t_naive = _row_at.get(_k_naive, {})

        # ── 結構閘 telescoping：ΣRw_側 == R(W_final) − R(W₀_buffer) ──
        #   附件二累積差額制之望遠鏡和（rw_increment 逐筆串接、W 單調不減故無 max(0,·) 夾斷）。
        #   W₀＝forced 角落鎖定之 buffer 起算點（無 forced → 0）。
        #   破＝Rw 累積鏈斷（W_prev thread 漏更新／W_far 消失／W 非單調）。
        for _sd_tag, _sd_has, _sd_W0, _sd_Wf in (
                ('left', _has_left_corner, _adv_final['W0_left'], _adv_final['Wf_left']),
                ('right', _has_right_corner, _adv_final['W0_right'], _adv_final['Wf_right'])):
            if not _sd_has:
                continue
            # 🆕 D-2b-3 §二：一般化為「兩端點差 − Σ逐界面鏈斷量」（`K-9-5-5`）
            _nodes_a = _chain(_sd_tag)
            _ifs_a = _iface_deltas(_nodes_a)
            print(_fmt_ifaces(f"{_sd_tag}·總量", _ifs_a))          # §二-1：逐界面印數值
            _guard_auth_scope(_sd_tag, _nodes_a, _ifs_a)           # §二-3 ➕ 範圍守衛
            # 🆕 D-2b-4 §四(b)：**所有界面**之 `Δ_i` 一律須為 0（**含方向改變之界面**）。
            #   ⚠️ 相對 D-2b-3 之**唯一驗收轉向**：前批容許授權界面 Δ_i≠0（`K-9-5-5` 半條），
            #     該半條已由 KL **撤回** ⇒ 依 `K-9-5-6` 鏈定式，缺口不應存在。
            #   ⛔ 容差 `0.1` 未放寬；⛔ `_guard_auth_scope`／方向識別**未刪**（降為守衛·仍印出）。
            _bad_a = [d for d in _ifs_a if abs(d['delta']) > _IFACE_TOL]
            if _bad_a:
                raise RuntimeError(
                    f"🔴 結構閘 telescoping 破（鏈斷·`K-9-5-6`）：街廓 {blk_label} {_sd_tag} 側 "
                    + "；".join(f"{d['lot']}→{d['next']} Δ={d['delta']:+.3f}"
                                f"（Δ_self={d['delta_self']:+.3f}）" for d in _bad_a)
                    + f"（>{_IFACE_TOL}）——鏈起點未續上前一宗之 W_far")
            # §四(a)：三閘**回原式**（⛔ 不再減 ΣΔ_i·`K-9-5-5` 半條已撤回）
            _sum_rw_side = _rw_real_wd2(_sd_tag)
            _tele_exp = _rw_from_width(_sd_Wf) - _rw_from_width(_sd_W0)
            if abs(_sum_rw_side - _tele_exp) > _IFACE_TOL:
                raise RuntimeError(
                    f"🔴 結構閘 telescoping 破：街廓 {blk_label} {_sd_tag} 側 "
                    f"ΣRw_實跑={_sum_rw_side:.2f} ≠ R(W_final={_sd_Wf:.2f})−R(W₀={_sd_W0:.2f})"
                    f"={_tele_exp:.2f}（Δ={abs(_sum_rw_side - _tele_exp):.3f} >{_IFACE_TOL}）"
                    f"｜逐界面：{_fmt_ifaces(_sd_tag, _ifs_a)}")

        # ── 🆕 結構閘 階段2 telescoping（三閘合圍之**中段**·claude.ai 裁定 2026-07-24 §五(a)修正版）──
        #   `ΣRw_階段2_側 == R(W_final) − R(W_階段1末)`，容差 0.1（同 telescoping 家族）。
        #   ⚠️ **刻意不採**「ΣRw_階段2 ≤ 100 − 理論@k*」之不等式版——`rw_from_width` 於 W≥18
        #     飽和 100 使該式幾近**恆真**＝文字閘（看似有守、實則不咬）。恆等式才咬得住。
        #   三閘合圍：階段1段＝「理論＝實跑」（母體＝階段1子集）／**階段2段＝本閘**／
        #             總量段＝上方 telescoping（母體＝全域 `_rw_real_wd2`）⇒ 守備零縮。
        #   無階段2宗時 `_rw_s2` 與 `_exp_s2` 恆為 0（左右端點同值）⇒ 不誤咬既有情境。
        for _sd_t2, _sd_has_t2, _W1_end_t2, _Wf_t2 in (
                ('left', _has_left_corner, _Wf_stage1['left'], _adv_final['Wf_left']),
                ('right', _has_right_corner, _Wf_stage1['right'], _adv_final['Wf_right'])):
            if not _sd_has_t2:
                continue
            # 🆕 D-2b-3 §二-4：**共用同一 `Δ_i` 產生器**（⛔ 不得各寫一份）。
            #   階段2 段之鏈首須銜接**階段1 末**之 `W_far` ⇒ 以 `_w0_prev` 前置虛擬界面。
            _nodes_b = _chain(_sd_t2, _stage=2)
            _ifs_b = _iface_deltas(_nodes_b, _w0_prev=float(_W1_end_t2))
            print(_fmt_ifaces(f"{_sd_t2}·階段2", _ifs_b))
            _bad_b = [d for d in _ifs_b if abs(d['delta']) > _IFACE_TOL]      # §四(b)：含授權界面
            if _bad_b:
                raise RuntimeError(
                    f"🔴 結構閘 階段2 telescoping 破（鏈斷·`K-9-5-6`）：街廓 {blk_label} "
                    f"{_sd_t2} 側 "
                    + "；".join(f"{d['lot']}→{d['next']} Δ={d['delta']:+.3f}"
                                f"（Δ_self={d['delta_self']:+.3f}）" for d in _bad_b)
                    + f"（>{_IFACE_TOL}）——池內落位之 Rw 鏈與 W 續推脫鉤")
            _rw_s2 = round(_rw_real_wd2(_sd_t2) - _rw_stage1_only(_sd_t2), 2)
            _exp_s2 = _rw_from_width(_Wf_t2) - _rw_from_width(_W1_end_t2)     # §四(a)：回原式
            if abs(_rw_s2 - _exp_s2) > _IFACE_TOL:
                raise RuntimeError(
                    f"🔴 結構閘 階段2 telescoping 破：街廓 {blk_label} {_sd_t2} 側 "
                    f"ΣRw_階段2={_rw_s2:.2f} ≠ R(W_final={_Wf_t2:.2f})−"
                    f"R(W_階段1末={_W1_end_t2:.2f})={_exp_s2:.2f}"
                    f"（Δ={abs(_rw_s2 - _exp_s2):.3f} >{_IFACE_TOL}）"
                    f"——池內落位之 Rw 鏈與 W 續推脫鉤｜逐界面：{_fmt_ifaces(_sd_t2, _ifs_b)}")

        # ── 首宗下限 loud（補丁六 §二·plan §1）：達資格街角首宗 KL W ≥ 側街退縮 ＋ 最小畸零寬 ──
        #   首宗 W₁ ＝ 首宗角落宗 res['W']（=W_far·打樣「首宗W」；非 W0=W_near）；
        #   下限＝setback（輸入欄）＋ 查表 min_width（f3_min_width_by_label·禁字面 7/3.5）。
        #   loud 下限規制·非恰等（bisect 於下限上自由解）·非硬釘＝7；不達＝loud 記錄/警示（禁靜默·禁 clamp）。
        #   驗收：重烤後應 ≥ 下限（現值 pre-重烤 artifact 6.92 待重生）。非 raise（合法邊界案不硬阻·補丁六 §二「記錄/警示」）。
        _mw_blk_z = float((ss.get('f3_min_width_by_label', {}) or {}).get(blk_label, 0.0) or 0.0)
        if _mw_blk_z > 0:
            _first_floor = float(setback) + _mw_blk_z
            for _sd_z, _has_z, _Wf1_z in (
                    ('left', _has_left_corner, _adv_final.get('Wfirst_left', 0.0)),
                    ('right', _has_right_corner, _adv_final.get('Wfirst_right', 0.0))):
                if not _has_z:
                    continue
                if float(_Wf1_z) + 1e-9 < _first_floor:
                    print(f"🔴 首宗下限未達（補丁六 §二）：街廓 {blk_label} {_sd_z} 側 首宗 KL W="
                          f"{float(_Wf1_z):.2f} < 退縮({float(setback):.2f})＋畸零寬({_mw_blk_z:.2f})"
                          f"={_first_floor:.2f}——loud 記錄·禁靜默/禁 clamp（重烤後應 ≥ 下限）")

        # ── 結構閘 â 定向雙判準（補丁八 §三·主判準推進方向＋交叉核形心·不一致 escalate 禁靜默）──
        #   主判準：â 沿推進向定號（右組 −d_hat／左組 +d_hat·`grep -n "d_hat_rev" verify/stepg_pipeline.py`）；交叉核：(街廓形心−mp)·â>0。
        #   δ 正負係 alloc_normal_axis 符號約定之產物·非幾何（#26②）；此閘證兩判準同源、方向不擲硬幣。
        if allocation_dir_block is not None and d_hat is not None and blk_meta.get('centroid'):
            _cen_a = _np_d.asarray(blk_meta['centroid'], dtype=float)
            for _sd_a, _has_a, _mp_a, _adv_a in (
                    ('left', _has_left_corner, _side_mid_left, d_hat),
                    ('right', _has_right_corner, _side_mid_right, -_np_d.asarray(d_hat, dtype=float))):
                if not _has_a or _mp_a is None:
                    continue
                _ah_a = _np_d.asarray(allocation_dir_block, dtype=float)
                _nrm_a = float(_np_d.linalg.norm(_ah_a))
                if _nrm_a < 1e-9:
                    continue
                _ah_a = _ah_a / _nrm_a
                _ah_a = _ah_a if float(_np_d.dot(_np_d.asarray(_adv_a, float), _ah_a)) >= 0 else -_ah_a
                _cross_a = float(_np_d.dot(_cen_a - _np_d.asarray(_mp_a, float), _ah_a))
                if _cross_a <= 0:
                    raise RuntimeError(
                        f"🔴 â 定向雙判準不一致（補丁八 §三）：街廓 {blk_label} {_sd_a} 側 "
                        f"推進定號後 (形心−mp)·â={_cross_a:.3f} ≤0 → escalate（禁靜默 fallback）")

        # ── 結構閘 理論＝實跑：滑池槽 k* 之理論 ΣRw 必等於實際推進之 ΣRw（逐側） ──
        #   破＝_select_pool_slot 之 widths 與實際推進不同源（選槽依據與落地結果脫鉤）。
        if _slot_res:
            for _th_key, _sd_tag2 in (('ΣRw_L', 'left'), ('ΣRw_R', 'right')):
                _th = float(_t_star.get(_th_key, 0.0) or 0.0)
                # 🆕 §4 P2：比對母體限**階段1子集**（`_rw_stage1_only`）。理論側之 widths
                #   結構上只含階段1宗（k* 先於階段2·裁定B 鎖時序）⇒ 拿全域母體比即非同類相比。
                #   階段2 之 Rw 改由下方「階段2 恆等式閘」看守（三閘合圍·守備零縮）。
                _re = _rw_stage1_only(_sd_tag2)
                # 🆕 D-2b-3 §二-4：**共用同一 `Δ_i` 產生器**（階段1 子鏈）——
                #   用於 ①逐界面印數值 ②未授權界面 Δ_i==0 之守衛 ③範圍守衛。
                # 🔴 **⛔ 本閘之恆等式<u>不</u>減 ΣΔ_i**（D-2b-3 實測**反證**·⛔ 非未想到）：
                #   首版曾寫 `理論@k* − ΣΔ_i == 實跑`，經實測**證偽**——
                #     `0m  R1 left`：ΣΔ_i=+0.912，減之使差由 1.92 惡化為 **2.829**（方向就錯）；
                #     `3.5m R1 left`：**ΣΔ_i=+0.000**（該側無授權界面）而差仍達 **2.446**
                #       ⇒ 該落差**與鏈斷量無關**，⛔ 不得以 ΣΔ_i 解釋或吸收。
                #   ⇒ 恢復原式（`理論@k* == 實跑`·容差 0.1 未動）；其破另行歸因、⛔ 不在本批以調整式掩蓋。
                _nodes_c = _chain(_sd_tag2, _stage=1)
                _ifs_c = _iface_deltas(_nodes_c)
                print(_fmt_ifaces(f"{_sd_tag2}·階段1", _ifs_c))
                _guard_auth_scope(_sd_tag2, _nodes_c, _ifs_c)
                _bad_c = [d for d in _ifs_c if abs(d['delta']) > _IFACE_TOL]   # §四(b)：含授權界面
                if _bad_c:
                    raise RuntimeError(
                        f"🔴 結構閘 理論＝實跑 破（鏈斷·`K-9-5-6`）：街廓 {blk_label} "
                        f"{_sd_tag2} 側 "
                        + "；".join(f"{d['lot']}→{d['next']} Δ={d['delta']:+.3f}"
                                    f"（Δ_self={d['delta_self']:+.3f}）" for d in _bad_c)
                        + f"（>{_IFACE_TOL}）")
                _sum_delta_c = sum(d['delta'] for d in _ifs_c)
                if abs(_th - _re) > _IFACE_TOL:
                    raise RuntimeError(
                        f"🔴 結構閘 理論＝實跑 破：街廓 {blk_label} {_sd_tag2} 側 "
                        f"理論@k*={_th:.2f} ≠ 實跑(階段1)={_re:.2f}"
                        f"（Δ={abs(_th - _re):.3f} >{_IFACE_TOL}）"
                        f"｜參考 ΣΔ_i={_sum_delta_c:+.3f}（**⛔ 未用於本式**·實測反證見碼註）"
                        f"｜逐界面：{_fmt_ifaces(_sd_tag2, _ifs_c)}")
        if _pool_total_blk is not None:
            # ── §N3-0 守恆-帳幾何級（逐街廓 Σ 閘·KL 2026-07-16 裁·補丁三 §二）──
            #   `|ΣG ＋ 池幾何 − 街廓| ≤ 宗數×(0.005×深度 ＋ tol ＋ 0.005)` ＝逐宗上界之和（三角不等式）。
            #   ⚠️ 舊 `<1.0` 廢（殘餘定閘·N0-17）；⚠️ 補丁一/二之 `宗數×0.005（＋圍堵界）` 亦廢
            #      （維度錯：以 G 面積量子冒充 S 長度量子×深度·≈45 倍 → 停機③ b68e7c1）。
            #   註：T2 令 `池幾何 = 街廓 − Σ宗幾何`（①' 覆蓋閘證之）→ 本殘差恆等於 `Σ(G−幾何)`
            #       ＝Σ增減；真幾何守恆另由 ①' 覆蓋閘（0.01·志向不變）把關。
            _resid_wd2 = round(_sum_G_blk + _pool_total_blk - blk_area, 2)
            _tol_blk = _acct_geom_tol_block(len(_adv_final['rows']), avg_depth_default)
            _verdict_wd2 = ('✅' if abs(_resid_wd2) <= _tol_blk else '🔴 守恆破')
        else:
            _resid_wd2 = None
            _verdict_wd2 = '—（無街廓幾何）'
        pool_diag[blk_label] = {
            'n': _N, 'k_naive': _k_naive, 'k*': _k_star,
            'J(naive)': round(float(_t_naive.get('J', 0.0)), 4),
            'J(k*)': round(float(_t_star.get('J', 0.0)), 4),
            'ΣRw_L理論@k*(%)': round(float(_t_star.get('ΣRw_L', 0.0)), 2),
            'ΣRw_R理論@k*(%)': round(float(_t_star.get('ΣRw_R', 0.0)), 2),
            'ΣRw_L實跑(%)': _rw_real_wd2('left'),
            'ΣRw_R實跑(%)': _rw_real_wd2('right'),
            'ΣG(㎡)': round(_sum_G_blk, 2),
            'Σ配地幾何(㎡)': round(_sum_geom_blk, 2),
            '池總=幾何剩餘(㎡)': (round(_pool_total_blk, 2)
                                  if _pool_total_blk is not None else None),
            '角落抵費地L(㎡)': round(_corner_off_L, 2),
            '角落抵費地R(㎡)': round(_corner_off_R, 2),
            '中央池(㎡)': (round(_pool_total_blk - _corner_off_L - _corner_off_R, 2)
                           if _pool_total_blk is not None else None),
            '守恆殘差(㎡)': _resid_wd2,
            '判定': _verdict_wd2,
            'note': ((_slot_res or {}).get('note', '') or
                     ('degenerate/N≤1 單趟' if (_degenerate_order or _N <= 1) else ''))
                    + ('；naive 切點不在合法域(pin)，停機②看守略過比較'
                       if (_slot_res and _k_naive not in _row_at) else ''),
            '幾何片明細(㎡)': (str([round(float(_g.area), 2) for _g in offset_geoms])
                               if _pool_total_blk is not None else ''),
            '片數': (len(offset_geoms) if _pool_total_blk is not None else 0),
            'slot_table': [dict(t) for t in _tbl_wd2],
        }
        if _verdict_wd2 == '🔴 守恆破':
            raise RuntimeError(
                f"停機③（守恆-帳幾何級破）街廓 {blk_label}：|Σ(G−幾何)| = {_resid_wd2:+.2f}㎡ "
                f"> 上界 {_tol_blk:.4f}＝宗數{len(_adv_final['rows'])}×(tol 0.01 ＋ G捨入 0.005)"
                f"〔S0d 後·S 量化退出計算路徑·舊 0.005×深度 項歸零·補丁四 §二〕")

    # `stage2_placed`＝W-4 回饋通道（P2-e 備·wf_f4 扣 `a_rem` 於 P2-g 接）。
    #   純加性頂層鍵——`build_step_g_tables` 只讀 `g_rows`/`pool_diag`，三表欄集不受影響。
    return {'g_rows': g_rows, 'pool_diag': pool_diag, 'stage2_placed': _stage2_placed}


def build_step_g_tables(res):
    """把 run_step_g 結果攤成三張對拍表（欄名/rounding 同 app UI 匯出）。
    g_rows 欄位聯集補空（app 端 DataFrame 化時抵費地列缺鍵→NaN→CSV 空，等效之）。"""
    _cols = []
    for r in res['g_rows']:
        for k in r:
            if k != 'cut_coords' and k not in _cols:
                _cols.append(k)
    g_rows = [{k: r.get(k, '') for k in _cols} for r in res['g_rows']]
    diag_rows = []
    for lbl in sorted(res['pool_diag']):
        d2 = res['pool_diag'][lbl]
        diag_rows.append({'街廓': lbl,
                          **{k: v for k, v in d2.items() if k != 'slot_table'}})
    slot_rows = []
    for lbl in sorted(res['pool_diag']):
        for t2 in (res['pool_diag'][lbl].get('slot_table') or []):
            slot_rows.append({
                '街廓': lbl, 'k': t2['k'],
                'J': round(float(t2['J']), 4),
                'dev(m)': round(float(t2['dev']), 2),
                'ΣRw_L(%)': round(float(t2['ΣRw_L']), 2),
                'ΣRw_R(%)': round(float(t2['ΣRw_R']), 2),
            })
    return g_rows, diag_rows, slot_rows
