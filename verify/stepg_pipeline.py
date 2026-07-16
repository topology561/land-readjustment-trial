# -*- coding: utf-8 -*-
"""
W-D.2 P6 — Step G headless driver（v2 轉正必要條件；KL 放行 2026-07-06）。

headless 重現 app.py 步驟 G（宗地分配 G 值迭代＋W-D.2 §3 滑池槽＋守恆 ledger），
產出三張表對拍 verify/out/wd2_run/（KL 2026-07-06 乾淨雙參數輪＝v2 準源）：
  G 值計算結果／W-D.2 §3 滑池槽診斷／逐槽 J 表 × 雙情境。

**參數裝配鐵則（KL 四條件①）**：路況負擔尺度一律消費快照 `blocks.*.負擔尺度_輸入`
（front/side_new＝輸入>0；calc_* 算出之尺度與輸入逐格斷言相等，破＝RuntimeError），
**不得吃 SS_ROAD 預設**。街廓深度＝快照 `街廓分配深度_m`。

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


def run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
               winners_state, forced_map, setback):
    """一情境 Step G。回傳 {'g_rows','pool_diag','slot_rows'}（欄名/rounding 同 app）。"""
    import numpy as _np_d
    from shapely.geometry import Polygon as _SP_d
    # §N3-0 T2：`unary_union as _uunion_d` 已拆——其唯一用途為舊池片式
    #   `_uunion_d(allocated_polys).buffer(0.001)`（病灶·已廢）；留之即 dead import。

    ss = fake_st.session_state
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
    # 重劃總負擔率＝`compute_total_burden_rate` 現算（build_pipeline 鋪底）。
    # 舊 `or 0.40` fallback 已廢（快照 global.重劃總負擔率 鍵一併刪）→ 缺值即 loud。
    _tab6_burden = ss.get("f3_total_burden_rate_from_finance")
    if _tab6_burden is None:
        raise RuntimeError(
            "🔴 f3_total_burden_rate_from_finance 未鋪底：須先 compute_total_burden_rate()"
            "（禁靜默退回 0.40 舊 fallback）")
    _tab6_burden = float(_tab6_burden)

    # ── 地價（v3：後街廓單價／重劃前區段單價；A 逐宗＝post/pre） ──
    post_price_by_block = {lbl: float(v["單價_元每m2"]) for lbl, v in _post_bp.items()}
    pre_price_by_zone = {z: float(v["單價_元每m2"])
                         for z, v in fin["重劃前區段_面積單價"].items()}
    # 財務中繼態外拋（run_verification 之財務閘消費；非計算鏈）
    globals()["_V3_FINANCE"] = {
        "B": B_value, "C": C_for_calc, "C_avg_form": _C_avg_form,
        "eng": _eng_cost, "redev": _redev_cost, "loan": _loan_interest,
        "cost_sum": _cost_sum, "C_denom": _C_denom_sum,
        "general_burden": general_burden, "public_common": public_common_total,
        "special_total": sb["special_total"],
        "post_price_by_block": dict(post_price_by_block),
        "pre_price_by_zone": dict(pre_price_by_zone),
    }

    # ── session 鋪底（Step L/PK 產物＝快照/選位半 driver 餵入） ──
    ss["f3L_setback_default"] = setback
    ss["f3_alloc_depth_by_label"] = {b["label"]: float(SB[b["label"]]["街廓分配深度_m"])
                                     for b in _build_blocks}
    # backlog②（WARNING-2）：min_width 逐塊吃**真實 category**（廢硬編「住宅區」）。
    ss["f3_min_width_by_label"] = {
        b["label"]: float(ns["get_min_lot_size"](
            b["category"], float(SB[b["label"]]["正面"]["路寬_m"])).get("min_width", 0.0) or 0.0)
        for b in _build_blocks}
    ss["f3_corner_winners"] = winners_state
    ss["f3L_forced_offset"] = forced_map
    ss["f3L_corner_min_table"] = param_rows
    ss["f3_manual_baseline"] = {}
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

    g_rows = []
    detail_trace = {}
    pool_diag = {}

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
                   _allocation_dir=None, _side_mid=None, _W_prev=0.0):
        if _blk_poly is not None and _d_hat is not None and _baseline_pt is not None:
            try:
                _r = solve_G_binary(
                    a=_a_m2, A=_A, B=B_value, C=C_for_calc,
                    l_front=_l_front, l_side=_l_side, F=_F,
                    block_poly=_blk_poly, d_hat=_d_hat,
                    baseline_pt=_baseline_pt,
                    S_max_limit=_S_max,
                    is_corner=_is_corner,
                    side_label=_side if _side in ('左側', '右側') else '左側',
                    tol=0.01, max_iter=80,
                    allocation_dir=_allocation_dir,
                    side_mid=_side_mid, W_prev=_W_prev,
                )
                return _r, '幾何二分法'
            except Exception:
                pass
        _r = iterate_G_S(
            a=_a_m2, A=_A, B=B_value, C=C_for_calc,
            l_front=_l_front, l_side=_l_side, F=_F, W=0.0,
            avg_depth=_avg_depth,
            is_corner=_is_corner,
            tab6_total_burden=_tab6_burden,
            W_prev=_W_prev,
        )
        _r['area_geom'] = round(_r.get('S', 0) * _avg_depth, 2)
        _r['cut_coords'] = []
        return _r, '代數迭代(fallback)'

    # ── 逐街廓（app Step G 迴圈逐行複刻；st.* 於 headless 為 fake no-op 故略） ──
    for blk_label, parcels_in_blk in parcels_by_block.items():
        blk_meta = block_meta_by_label.get(blk_label, {})
        blk_poly = blk_meta.get('shapely', None)
        blk_area = float(blk_meta.get('area_m2', 0.0) or 0.0)
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
        if _degenerate_order:
            ordered_v2 = []
            for tp in parcels_in_blk:
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
            _v2_res = _spatial_order_parcels_v2(
                parcels_in_block=parcels_in_blk,
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
            _proj_rank = {tp['暫編地號']: _i + 1 for _i, tp in enumerate(
                ns["_projection_order"](parcels_in_blk, _cad_fl_blk.get('p1'),
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
            if _fo_left:
                _l_min = _row_for_buffer.get('【左】街角最小面積(㎡)')
                try:
                    if _l_min is not None and _l_min != float('inf'):
                        _left_buffer_S = float(_l_min) / avg_depth_default
                except (TypeError, ValueError):
                    _left_buffer_S = 0.0
            if _fo_right:
                _r_min = _row_for_buffer.get('【右】街角最小面積(㎡)')
                try:
                    if _r_min is not None and _r_min != float('inf'):
                        _right_buffer_S = float(_r_min) / avg_depth_default
                except (TypeError, ValueError):
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
            # W₀＝該側 Rw 累積起算點：forced 角落鎖定時＝buffer 之臨街投影，否則 0
            #   （telescoping 閘用：ΣRw_側 = R(W_final) − R(W₀)）
            _W0_left = (_left_buffer_S * _cos_dn) if _has_left_corner else 0.0
            _W0_right = (_right_buffer_S * _cos_dn) if _has_right_corner else 0.0
            _W_prev_left = _W0_left
            _W_prev_right = _W0_right
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
                )
                if _has_left_corner:
                    _W_prev_left = float(res.get('W_far', _W_prev_left))
                _S_actual = float(res.get('S', 0.0))
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
                try:
                    _proj_pts = [
                        float(_np_d.dot(
                            _np_d.array([v[0] - corner_pt[0], v[1] - corner_pt[1]]),
                            d_hat
                        )) for v in blk_meta['vertices']
                    ]
                    actual_max_proj = max(_proj_pts) if _proj_pts else S_block_max
                except Exception:
                    actual_max_proj = S_block_max
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
                        )
                        if float(_r2.get('area_geom', 0)) >= 0.5:
                            res, solver_label = _r2, _sl2
                            break
                if _has_right_corner:
                    _W_prev_right = float(res.get('W_far', _W_prev_right))
                _S_actual = float(res.get('S', 0.0))
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
            _slot_res = _select_pool_slot(
                _adv_base['widths'],
                {'has': _has_left_corner, 'F': _F_left,
                 'l1': _lside_left, 'b': _left_buffer_S * _cos_dn},
                {'has': _has_right_corner, 'F': _F_right,
                 'l1': _lside_right, 'b': _right_buffer_S * _cos_dn},
            )
            _k_star = int(_slot_res['k'])
            _J_by_k = {t['k']: t['J'] for t in _slot_res['table']}
            if (_k_naive in _J_by_k
                    and _J_by_k.get(_k_star, 0.0) < _J_by_k[_k_naive] - 1e-9):
                raise RuntimeError(
                    f"停機②（J 下降）街廓 {blk_label}：J(k*)<J(naive)")
            _adv_final = _advance_block_with_split(_k_star, True)
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
                for _entry, _res in (left_results + right_results):
                    _coords = _res.get('cut_coords') or []
                    if len(_coords) >= 3:
                        try:
                            _p = _SP_d(_coords)
                            if not _p.is_valid:
                                _p = _p.buffer(0)
                            if not _p.is_empty and _p.area >= 0.5:
                                allocated_polys.append(_p)
                        except Exception:
                            continue
                # ── §N3-0 T2（主修法）：池片改用與業主宗**同機制·同切線**直接切出 ──
                #   廢：`_uunion_d(allocated_polys).buffer(0.001)` → `difference` → `area >= 1.0`
                #       （buf_leak／gap_union／sliver 三漏之源＋T1 面積判準之誤殺/放行）
                #   單一真相源＝app 之 `_pool_strips_for_block`（ns harvest·同 `_block_strip` 先例）
                #   → stepg／app／wf_f1／wf_f4 四處同源，根絕抄寫複本各自漂移（#20 根因）。
                #   回傳依 s 起點排序（N0-19 身分鍵；較舊「面積 desc」穩定）。
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
        _corner_off_L = (float(_v2_res.get('left_corner_offset_area', 0.0) or 0.0)
                         if _v2_res else 0.0)
        _corner_off_R = (float(_v2_res.get('right_corner_offset_area', 0.0) or 0.0)
                         if _v2_res else 0.0)

        def _rw_real_wd2(_side_tag):
            return round(sum(float(r.get('Rw(%)', 0) or 0)
                             for r in _adv_final['rows']
                             if r.get('推進側別') == _side_tag
                             and float(r.get('F(m)', 0) or 0) > 0), 2)
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
            _sum_rw_side = _rw_real_wd2(_sd_tag)
            _tele_exp = _rw_from_width(_sd_Wf) - _rw_from_width(_sd_W0)
            if abs(_sum_rw_side - _tele_exp) > 0.1:
                raise RuntimeError(
                    f"🔴 結構閘 telescoping 破：街廓 {blk_label} {_sd_tag} 側 "
                    f"ΣRw_實跑={_sum_rw_side:.2f} ≠ R(W_final={_sd_Wf:.2f})−R(W₀={_sd_W0:.2f})"
                    f"={_tele_exp:.2f}（Δ={abs(_sum_rw_side - _tele_exp):.3f} >0.1）")

        # ── 結構閘 理論＝實跑：滑池槽 k* 之理論 ΣRw 必等於實際推進之 ΣRw（逐側） ──
        #   破＝_select_pool_slot 之 widths 與實際推進不同源（選槽依據與落地結果脫鉤）。
        if _slot_res:
            for _th_key, _sd_tag2 in (('ΣRw_L', 'left'), ('ΣRw_R', 'right')):
                _th = float(_t_star.get(_th_key, 0.0) or 0.0)
                _re = _rw_real_wd2(_sd_tag2)
                if abs(_th - _re) > 0.1:
                    raise RuntimeError(
                        f"🔴 結構閘 理論＝實跑 破：街廓 {blk_label} {_sd_tag2} 側 "
                        f"理論@k*={_th:.2f} ≠ 實跑={_re:.2f}（Δ={abs(_th - _re):.3f} >0.1）")
        if _pool_total_blk is not None:
            _resid_wd2 = round(_sum_G_blk + _pool_total_blk - blk_area, 2)
            _verdict_wd2 = ('✅' if abs(_resid_wd2) < 1.0 else '🔴 守恆破')
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
                f"停機③（守恆破）街廓 {blk_label}：殘差 {_resid_wd2:+.2f}㎡ ≥1㎡")

    return {'g_rows': g_rows, 'pool_diag': pool_diag}


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
