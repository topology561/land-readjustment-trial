# -*- coding: utf-8 -*-
"""
W-V 選位半 driver — ownership（tab1 歸戶指紋）＋ parcels/candidates ＋ 街角 PK orchestration。

**additive-only：app.py 一字不改。**
真函式（parse_cadastral_geofile / validate_parcel_assignments_by_area /
overlay_polygons_to_blocks / _assign_four_column_areas / _annotate_temp_parcel_cut_type /
_estimate_G_for_qualification / select_corner_lots_both_sides_v12）全走 app_harvest。

兩段 **UI 內嵌邏輯無法 harvest（st.button 分支內 inline script）→ 逐行複刻**：
  1. tab1 歸戶 inline（app.py ~10800-10993）→ build_ownership()
  2. 街角 callback orchestration（app.py ~13799-14060 + 14107-14119）→ run_corner_pk()
🔧 維護耦合（README 嫌犯序 2）：未來波動到上述兩段 → 本檔必須同波更新。

Gxxx doctrine（KL 2026-07-04 更正）：群組號按重劃區地籍**迭代序（dict 插入序）**配發；
匿名化保列序 → 指紋劃分同構 → 首現序不變 → **Gxxx 應全同**。靶：
628-18→G005、628-45→G007、628→G009、628-37→G019、628-41→G023、628-36→G029。
"""


# ═══════════════ 1. ownership（tab1 歸戶 inline 複刻；app 10800-10993） ═══════════════

# Gxxx 全等定理鏈之靶組（diverge 時三環反查：列序/指紋複刻/迭代起點）
OWNERSHIP_TARGETS = {
    "628-18": "G005", "628-45": "G007", "628": "G009",
    "628-37": "G019", "628-41": "G023", "628-36": "G029",
}


def build_ownership(ns, fake_st, xlsx_path):
    """複刻 tab1 歸戶 inline：重劃區地籍 迭代（起點鐵律：非 U_LAND）→ match U_LAND
    → 歸戶指紋 → fp_to_group（插入序 Gxxx）→ t8_ownership_map（含正規化變體鍵）。
    寫入 fake session_state（t8_ownership_map / _full / _groups / t8_parcel_areas），
    回傳診斷 dict。"""
    import pandas as pd

    xl7 = pd.ExcelFile(xlsx_path, engine="openpyxl")
    if "U_LAND" not in xl7.sheet_names or "重劃區地籍" not in xl7.sheet_names:
        raise RuntimeError("xlsx 缺 U_LAND / 重劃區地籍 工作表")
    df_uland7 = pd.read_excel(xl7, sheet_name="U_LAND", header=0, engine="openpyxl")
    df_rezoning7 = pd.read_excel(xl7, sheet_name="重劃區地籍", header=0, engine="openpyxl")

    # ── 前處理 U_LAND（app 10807-10808 原樣） ──
    df_uland7["段名"] = df_uland7["段小段"].astype(str).str.replace(r"^\d+", "", regex=True)
    df_uland7["地號int"] = pd.to_numeric(df_uland7["地號"], errors="coerce")

    def 重劃地號轉ULAND整數(地號文字):
        s = str(地號文字).strip()
        if "-" in s:
            parts = s.split("-", 1)
            return int(parts[0]) * 10000 + int(parts[1])
        return int(s) * 10000

    rows_out = []
    rows_fail = []
    parcel_fp = {}   # {(地段, 地號): 歸戶指紋}；插入序＝重劃區地籍列序（Gxxx 之根）

    for _, rz_row in df_rezoning7.iterrows():
        seg = str(rz_row["地段"]).strip()
        landno_str = str(rz_row["地號"]).strip()
        city = str(rz_row["鄉鎮市"]).strip()
        try:
            target_int = 重劃地號轉ULAND整數(landno_str)
        except Exception:
            rows_fail.append({"鄉鎮市": city, "地段": seg, "地號": landno_str,
                              "原因": "地號格式無法解析"})
            continue
        matched = df_uland7[
            (df_uland7["段名"] == seg) & (df_uland7["地號int"] == target_int)
        ]
        if matched.empty:
            rows_fail.append({"鄉鎮市": city, "地段": seg, "地號": landno_str,
                              "原因": "U_LAND 無對應資料"})
            continue

        area7 = matched["面積"].dropna().iloc[0] if matched["面積"].notna().any() else None
        mort_rows7 = matched[matched["設定義務人"].notna()]

        # ── 歸戶指紋（app 10874-10913 原樣） ──
        own_fp_parts = []
        own_rows7 = matched.copy()
        own_rows7["_dedup_key"] = own_rows7.apply(
            lambda r: str(r.get("所有權統一編號", "")).strip()
            if pd.notna(r.get("所有權統一編號"))
            and str(r.get("所有權統一編號", "")).strip() not in ("", "nan")
            else str(r.get("姓名", "")).strip(),
            axis=1
        )
        own_rows7 = own_rows7.drop_duplicates(subset=["_dedup_key"])

        for _, owner in own_rows7.iterrows():
            uni = (str(owner.get("所有權統一編號", "")).strip()
                   if pd.notna(owner.get("所有權統一編號")) else "")
            name7_fp = str(owner.get("姓名", "")).strip() if pd.notna(owner.get("姓名")) else ""
            key_id = uni if uni else name7_fp
            d7fp = owner.get("權利範圍分母")
            n7fp = owner.get("權利範圍分子")
            ratio_fp = (f"{int(n7fp)}/{int(d7fp)}"
                        if pd.notna(d7fp) and pd.notna(n7fp) else "")
            own_fp_parts.append(f"{key_id}:{ratio_fp}")
        own_fp_parts.sort()

        mort_fp_parts = []
        seen_m = set()
        for _, mr in mort_rows7.iterrows():
            obligor = str(mr.get("設定義務人", "")) if pd.notna(mr.get("設定義務人")) else ""
            creditor = str(mr.get("姓名.2", "")) if pd.notna(mr.get("姓名.2")) else ""
            kind = str(mr.get("權利種類", "")) if pd.notna(mr.get("權利種類")) else ""
            dm = mr.get("債權權利範圍持分分母")
            nm = mr.get("債權權利範圍持分分子")
            mkey = (obligor, creditor, kind)
            if mkey in seen_m:
                continue
            seen_m.add(mkey)
            mratio = f"{int(nm)}/{int(dm)}" if pd.notna(dm) and pd.notna(nm) else ""
            mort_fp_parts.append(f"{obligor}→{creditor}[{kind}]{mratio}")
        mort_fp_parts.sort()

        fingerprint = "|".join(own_fp_parts) + "#" + ";".join(mort_fp_parts)
        parcel_fp[(seg, landno_str)] = fingerprint

        # ── 每位所有權人一列（供 t8_parcel_areas / B6 診斷） ──
        for _, owner in own_rows7.iterrows():
            uni = (str(owner.get("所有權統一編號", ""))
                   if pd.notna(owner.get("所有權統一編號")) else "")
            name7 = str(owner.get("姓名", "")) if pd.notna(owner.get("姓名")) else ""
            deno7 = owner.get("權利範圍分母")
            numer7 = owner.get("權利範圍分子")
            rows_out.append({
                "_parcel_key": (seg, landno_str),
                "地段": seg, "地號": landno_str,
                "統編": uni, "所有權人": name7,
                "土地面積㎡": area7,
                "持分分母": int(deno7) if pd.notna(deno7) else "",
                "持分分子": int(numer7) if pd.notna(numer7) else "",
            })

    # ── 歸戶分組（指紋相同→同群組；Gxxx＝parcel_fp 插入序） ──
    fp_to_group = {}
    g_counter = 1
    for pk, fp in parcel_fp.items():
        if fp not in fp_to_group:
            fp_to_group[fp] = f"G{g_counter:03d}"
            g_counter += 1
    for row in rows_out:
        pk = row.pop("_parcel_key")
        row["歸戶群組"] = fp_to_group.get(parcel_fp.get(pk, ""), "")

    # ── t8_ownership_map（app 10972-10993 原樣，含 _normalize_landno_module 變體鍵） ──
    _normalize = ns["_normalize_landno_module"]
    _own_map = {}
    _own_map_full = {}
    _own_groups = {}
    for (seg_k, landno_k), fp in parcel_fp.items():
        gid = fp_to_group.get(fp, "")
        if not gid:
            continue
        _own_map[landno_k] = gid
        _own_map_full[(seg_k, landno_k)] = gid
        _own_groups.setdefault(gid, []).append(landno_k)
        nk = _normalize(landno_k)
        if nk and nk != landno_k:
            _own_map.setdefault(nk, gid)
            _own_map_full.setdefault((seg_k, nk), gid)
        if '-' not in landno_k:
            _own_map.setdefault(f"{landno_k}-0", gid)

    # ── t8_parcel_areas（app 10997-11020 原樣） ──
    _parcel_areas = {}
    _seen_pk = set()
    for row in rows_out:
        seg_k = row.get('地段', '')
        landno_k = row.get('地號', '')
        if not landno_k:
            continue
        pk = (seg_k, landno_k)
        if pk in _seen_pk:
            continue
        _seen_pk.add(pk)
        try:
            a = float(row.get('土地面積㎡', 0) or 0)
        except Exception:
            a = 0.0
        if a > 0:
            _parcel_areas[landno_k] = a
            nk = _normalize(landno_k)
            if nk and nk != landno_k:
                _parcel_areas.setdefault(nk, a)
            if '-' not in landno_k:
                _parcel_areas.setdefault(f"{landno_k}-0", a)

    ss = fake_st.session_state
    ss["t8_ownership_map"] = _own_map
    ss["t8_ownership_map_full"] = _own_map_full
    ss["t8_ownership_groups"] = _own_groups
    ss["t8_parcel_areas"] = _parcel_areas

    # ── Gxxx 靶組核對（三環定理鏈 tripwire；PK 前先斷） ──
    target_report = {ln: (_own_map.get(ln), exp, _own_map.get(ln) == exp)
                     for ln, exp in OWNERSHIP_TARGETS.items()}
    return {
        "n_rezoning": len(df_rezoning7), "n_uland": len(df_uland7),
        "n_fail": len(rows_fail), "n_groups": len(fp_to_group),
        "rows_fail": rows_fail, "rows_out": rows_out,
        "target_report": target_report,
        "targets_ok": all(ok for _, _, ok in target_report.values()),
    }


# ═══════════════ 2. parcels / build_parcels（app 11631-11722 + 13458） ═══════════════

def _attach_pre_zone(temp_parcels, snapshot):
    """🆕 v3 財務接線：逐宗貼 `重劃前地價區段`（A 地價比之分母查價鍵）。

    區段係**原地號級**（同原地號之各暫編同區段；快照 `財務接線_v3.原地號_區段` 53 筆）。
    no-silent-fallback：非-ghost 宗地之原地號不在表中 → loud RuntimeError（不靠 KeyError 兜、
    更不得靜默給 '' 使 A 悄悄退回 1.0）。ghost sliver（無原地號、四欄面積恆 0、Step G 前即被
    過濾）→ zone=''，不 raise。"""
    zone_map = snapshot["財務接線_v3"]["原地號_區段"]
    missing = sorted({tp.get("原地號", "") for tp in temp_parcels
                      if not tp.get("_is_ghost_sliver", False)
                      and tp.get("原地號", "") not in zone_map})
    if missing:
        raise RuntimeError(
            f"🔴 v3 A 查價：{len(missing)} 個非-ghost 原地號不在快照 財務接線_v3.原地號_區段"
            f"（{len(zone_map)} 筆）：{missing[:5]}。缺區段→A 無從查得，禁靜默退回 A=1。")
    for tp in temp_parcels:
        tp["重劃前地價區段"] = zone_map.get(tp.get("原地號", ""), "")
    return temp_parcels


def build_build_parcels(ns, fake_st, v6_bytes, cb, snapshot):
    """真函式管線：parse_cadastral_geofile → 面積交叉驗證換位 → overlay →
    四欄面積 → cut_type → 🆕 貼重劃前地價區段 → build_parcels（可建築、未併公設）。

    `snapshot` 為**必填**（禁預設 None）：v3 起 A 地價比逐宗查價需 `原地號_區段`，
    漏傳即 TypeError 當場炸，不容靜默略過 zone。"""
    cad_data = ns["parse_cadastral_geofile"](v6_bytes, "V6.dxf")
    parcel_polys = cad_data.get("parcel_polygons", []) or []
    _t1_areas = fake_st.session_state.get("t8_parcel_areas", {}) or {}
    swaps = []
    if _t1_areas:
        try:
            _res = ns["validate_parcel_assignments_by_area"](
                parcel_polys, _t1_areas,
                area_diff_threshold=0.30, max_swap_distance_m=30.0)
            parcel_polys = _res["parcel_polys"]
            swaps = _res["swaps"]
        except Exception:
            pass   # app 同樣 warning 後續走原配對
    temp_parcels = ns["overlay_polygons_to_blocks"](parcel_polys, cb)
    temp_parcels = ns["_assign_four_column_areas"](temp_parcels, _t1_areas)
    temp_parcels = ns["_annotate_temp_parcel_cut_type"](temp_parcels)
    temp_parcels = _attach_pre_zone(temp_parcels, snapshot)
    fcb = ns["F3_CATEGORY_BURDEN"]
    build_parcels = [tp for tp in temp_parcels
                     if fcb.get(tp["街廓分類"], "") == "可建築土地"
                     and not tp.get("_merged_into_g", False)]
    return temp_parcels, build_parcels, swaps


# ═══════════════ 3. PK orchestration（app 13799-14060 + 14107-14119 複刻） ═══════════════

def run_corner_pk(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback,
                  *, snapshot):
    """一情境：對每可建築街廓跑 select_corner_lots_both_sides_v12，
    回傳 (診斷rows, 指配rows, 抵費地rows)。欄名/取值/四捨五入逐行同 app。

    🆕 P-C（裁定M·Q1）：`snapshot`（keyword-only·無預設⇒漏傳即 TypeError·非靜默）——供
    「假設第 1 宗真 G」驅動資格閘（`require_g_map=True`）。真 G 走 `_corner_block_true_G`→
    `_corner_first_lot_G`→`_solve_G_one`（Q-M4 同 solve 路徑）。"""
    ss = fake_st.session_state
    # 🆕 P-C：財務單一真相源（B/C/尺度/地價）＋幾何底料·供逐候選逐側真 G。
    from stepg_pipeline import _compute_v3_finance
    import numpy as _np_pc
    from shapely.geometry import Polygon as _Poly_pc
    _fin3 = _compute_v3_finance(ns, snapshot, cb, cad)
    _B_pc, _C_pc = _fin3["B"], _fin3["C"]
    _sb_rows_pc = _fin3["sb_rows_by_label"]
    _post_price_pc = _fin3["post_price_by_block"]
    _pre_price_pc = _fin3["pre_price_by_zone"]
    _SB_pc = snapshot["blocks"]
    _zof_pc = snapshot["財務接線_v3"]["原地號_區段"]
    _tab6_pc = float(fake_st.session_state.get("f3_total_burden_rate_from_finance") or 0.0)
    _side_lines_pc = cad.get("side_lines_by_side", {}) or {}
    _alloc_by_blk_pc = cad.get("alloc_dir_by_block", {}) or {}
    _tp_by_pid_pc = {t.get('暫編地號'): t for t in (temp_parcels or [])}
    _bp_by_pid_pc = {b.get('暫編地號'): b for b in (build_parcels or [])}
    ss["f3L_setback_default"] = setback              # v12 內部讀（W-B 0 陷阱已修，0.0 不被竄改）
    ss["f3_cad_front_lengths"] = cad.get("front_lengths", {}) or {}
    ss["f3_cad_side_lengths"] = cad.get("side_lengths", {}) or {}
    ss.setdefault("f3_g_iter_params", {})
    # 注意：f3L_sb_rows_by_label 在 app 全程無人寫入（v12 讀到 {} → 法定寬走 3.5 預設），
    # 忠實重現 → 不餵。

    _own_map = ss.get("t8_ownership_map", {}) or {}
    if not _own_map:
        raise RuntimeError("t8_ownership_map 空 — 先跑 build_ownership")

    fcb = ns["F3_CATEGORY_BURDEN"]
    _build_blocks = [b for b in cb
                     if fcb.get(b.get("category", ""), "") == "可建築土地"]
    rows_by_lbl = {r["街廓"]: r for r in param_rows}

    _g_rows = build_parcels
    by_blk = {}
    for r in _g_rows:
        by_blk.setdefault(r['所屬街廓'], []).append(r)

    v12 = ns["select_corner_lots_both_sides_v12"]
    estG = ns["_estimate_G_for_qualification"]

    _corner_select_results = []
    _corner_cand_diag = []
    _winners_state = {}   # 🆕 W-D.2 P6：鏡射 app f3_corner_winners
    for b in _build_blocks:
        _lbl = b['label']
        _row = rows_by_lbl.get(_lbl)
        if _row is None:
            continue
        ss['f3_current_pk_block'] = _lbl
        # 🆕 S1 §6 查表化：注入本塊法定最小寬（get_min_lot_size 分區×正面路寬）供 v12 B-4（app==engine 同源）
        ss['f3_pk_legal_min_width'] = float(
            ns["get_min_lot_size"](b.get('category', ''), float(_row.get('正面路寬(m)', 0.0) or 0.0))
            .get('min_width', 0.0) or 0.0)
        # 🆕 K-8 §三：同型注入街廓分配深度（N-19′ 2dp）供街角規定範圍新構造。
        #   PK 跑在 Step-G 之前 ⇒ session 尚無 `f3_alloc_depth_by_label`（reviewer W-5 同坑）。
        #   源＝參數列之 `街廓分配深度(m)`（與 app 之 `_corner_rows_init` 同欄·app==engine）。
        ss['f3_pk_alloc_depth'] = float(_row.get('街廓分配深度(m)', 0.0) or 0.0)
        _cad_fl_lstep = (ss.get('f3_cad_front_lines', {}) or {}).get(_lbl, {})
        _fl_p1_lstep = _cad_fl_lstep.get('p1') if _cad_fl_lstep else None
        _fl_p2_lstep = _cad_fl_lstep.get('p2') if _cad_fl_lstep else None
        _all_in_blk = by_blk.get(_lbl, [])
        _candidates_pool = _all_in_blk   # Patch D-1：候選池一律全自動 PK
        # 🆕 W-D.2 v2（鏡射 app tiebreaker 換源）：§2 正典原位次 rank（投影序）
        # 🆕 W-G.9-161 `L-3′` `POP_SYNC`：實參 ≡ identity(BUILD_LAYER)
        ns["_proj_pop_assert_seq"]("sp:_rank_by_tpid",
                                   _all_in_blk, by_blk.get(_lbl, []), blk=_lbl)
        _rank_by_tpid = {
            tp.get('暫編地號'): _i_rk + 1
            for _i_rk, tp in enumerate(
                ns["_projection_order"](_all_in_blk, _fl_p1_lstep, _fl_p2_lstep))
        }
        _candidates = []
        for r in _candidates_pool:
            _parent = r.get('原地號', '')
            _gid = _own_map.get(_parent, '')
            if not _gid:
                continue
            _tp = next((tp for tp in (temp_parcels or [])
                        if tp.get('暫編地號') == r.get('暫編地號')), None)
            _cen_x = float(_tp.get('centroid_x', 0)) if _tp else 0.0
            _cen_y = float(_tp.get('centroid_y', 0)) if _tp else 0.0
            _G_est = estG(float(r.get('幾何面積_m2', r.get('面積_m2', 0.0)) or 0.0))
            _cad_fl_priority = (ss.get('f3_cad_front_lengths', {}) or {}).get(_lbl, 0.0)
            _cad_sl_priority = (ss.get('f3_cad_side_lengths', {}) or {}).get(_lbl, 0.0)
            _front_len_priority = (
                _cad_fl_priority if _cad_fl_priority > 0
                else float(_row.get('正面長度(m)', _row.get('正面路寬(m)', 0.0)) or 0.0)
            )
            _side_len_priority = (_cad_sl_priority if _cad_sl_priority > 0 else 0.0)
            _candidates.append({
                '歸戶群組': _gid,
                '歸戶': _gid,
                '暫編地號': r.get('暫編地號', ''),
                '原地號': _parent,
                'centroid': (_cen_x, _cen_y),
                'polygon_coords': (_tp.get('polygon_coords') if _tp else None),
                'G_estimated': _G_est,
                'G_value': _G_est,
                'front_length': _front_len_priority,
                'side_length': _side_len_priority,
                'physical_overlap_area': float(r.get('幾何面積_m2', r.get('面積_m2', 0.0)) or 0.0),
                '臨正街長度_m': _front_len_priority,
                '臨側街長度_m': _side_len_priority,
                '跨占街角面積_m2': float(r.get('幾何面積_m2', r.get('面積_m2', 0.0)) or 0.0),
                '_pre_position_rank': _rank_by_tpid.get(r.get('暫編地號', ''), float('inf')),
            })
        _bf = max((c['臨正街長度_m'] for c in _candidates), default=1.0) or 1.0
        _bs = max((c['臨側街長度_m'] for c in _candidates), default=1.0) or 1.0
        _l_min_val = _row.get('【左】街角最小面積(㎡)')
        _r_min_val = _row.get('【右】街角最小面積(㎡)')
        _use_v13 = (_fl_p1_lstep is not None and _fl_p2_lstep is not None)
        if not _use_v13:
            # app O1 裁定：缺 FRONT_LINE → 停機警告、跳過（不 append 假結果）
            continue
        _min_p1 = float(_l_min_val) if _l_min_val is not None else float('inf')
        _min_p2 = float(_r_min_val) if _r_min_val is not None else float('inf')

        def _safe_cutoff(v):
            try:
                if v is None or v == '' or v == '—':
                    return 0.0
                return float(v)
            except (TypeError, ValueError):
                return 0.0
        _cutoff_p1_for_pk = _safe_cutoff(_row.get('【左】截角(㎡)'))
        _cutoff_p2_for_pk = _safe_cutoff(_row.get('【右】截角(㎡)'))
        # 🆕 P-C（裁定M·Q1）：逐候選逐側「假設第 1 宗真 G」→ 存 cand._G_true_p1/p2（供 v12 側特定資格閘）
        _p1_pc = _np_pc.array(_fl_p1_lstep, float); _p2_pc = _np_pc.array(_fl_p2_lstep, float)
        _sblkL_pc = float(_np_pc.linalg.norm(_p2_pc - _p1_pc))
        _dh_pc = (_p2_pc - _p1_pc) / (_sblkL_pc or 1.0)
        _verts_pc = b['vertices']
        _bpoly_pc = _Poly_pc(_verts_pc)
        if not _bpoly_pc.is_valid:
            _bpoly_pc = _bpoly_pc.buffer(0)
        _alloc_cad_pc = _alloc_by_blk_pc.get(_lbl)
        _alloc_axis_pc = ns["alloc_normal_axis"](_alloc_cad_pc) if _alloc_cad_pc else None
        _sblkR_pc = (ns["_oblique_s_max"](_verts_pc, _dh_pc, _p1_pc, _alloc_axis_pc) or _sblkL_pc) \
            if _alloc_axis_pc is not None else _sblkL_pc
        _sbr_pc = _sb_rows_pc.get(_lbl, {})
        _slb_pc = _side_lines_pc.get(_lbl, {}) or {}
        _smL_pc = (_slb_pc.get("left") or {}).get("mid")
        _smR_pc = (_slb_pc.get("right") or {}).get("mid")
        _a_by_pc = {}; _zone_by_pc = {}
        for _c_pc in _candidates:
            _pid_pc = _c_pc['暫編地號']
            _bp_pc = _bp_by_pid_pc.get(_pid_pc)
            # 🔴 W-4（reviewer·P-D 修正）：`a` 之來源＝**即將餵給 run_step_g 的那份 parcels**
            #   （＝`build_parcels`），**非** `temp_parcels`。二者於未改動時**係同一批 dict 物件**
            #   （`build_parcels` 過濾式無 copy·`grep -n "build_parcels = .tp for tp" verify/selection_pipeline.py`）⇒ 趟0 逐位同（P-C 130/2 不變）；但 M-5 物化係對
            #   **deepcopy 之 parcels₁** 注入 a′ ⇒ 讀 temp_parcels 會**看不到 a′**、
            #   使 winner 於趟1 仍以舊 a 評閘（實測：628-45(2) a 632.38 卻用 362.38 → 仍 forced）。
            _src_pc = _bp_pc if _bp_pc is not None else _tp_by_pid_pc.get(_pid_pc)
            if _src_pc is not None:
                _a_by_pc[_pid_pc] = (round(float(_src_pc.get('分攤登記面積_m2', 0) or 0)
                                           + float(_src_pc.get('面積_m2', 0) or 0), 2)
                                     if '分攤登記面積_m2' in _src_pc
                                     else round(float(_src_pc.get('面積_m2', 0) or 0), 2))
            _zone_by_pc[_pid_pc] = _zof_pc.get((_bp_pc or {}).get('原地號', ''), '')
        _true_map_pc = ns["_corner_block_true_G"](
            candidates=_candidates, a_by_pid=_a_by_pc, zone_by_pid=_zone_by_pc,
            blk_poly=_bpoly_pc, corner_pt=_p1_pc, d_hat=_dh_pc,
            s_max_left=_sblkL_pc, s_max_right=_sblkR_pc, alloc_dir=_alloc_axis_pc,
            side_mid_left=_smL_pc, side_mid_right=_smR_pc,
            l_front=float(_sbr_pc.get("正街尺度", 0) or 0),
            l_side_left=float(_sbr_pc.get("左側尺度", 0) or 0),
            l_side_right=float(_sbr_pc.get("右側尺度", 0) or 0),
            F_left=float(_sbr_pc.get("左側長度(m)", 0) or 0),
            F_right=float(_sbr_pc.get("右側長度(m)", 0) or 0),
            B=_B_pc, C=_C_pc, post_price_blk=float(_post_price_pc.get(_lbl, 0.0) or 0.0),
            pre_price_by_zone=_pre_price_pc, avg_depth=float(_SB_pc[_lbl]["街廓分配深度_m"]),
            tab6_burden=_tab6_pc, has_left=(_smL_pc is not None),
            has_right=(_smR_pc is not None),
            # 🔒 K-4 第 5 條前提：**獨立**自 cad front_lines 讀 p2（非由 _sblkL_pc 反推）
            front_p2=_p2_pc, _blk=_lbl)
        for _c_pc in _candidates:
            _gp_pc = _true_map_pc.get(_c_pc['暫編地號'], {})
            _c_pc['_G_true_p1'] = _gp_pc.get('p1')
            _c_pc['_G_true_p2'] = _gp_pc.get('p2')
        _g_map = {c['暫編地號']: c['G_estimated'] for c in _candidates}   # estG（診斷 G估欄·非達標）
        _v13 = v12(
            candidates=_candidates,
            front_line_p1=_fl_p1_lstep,
            front_line_p2=_fl_p2_lstep,
            cutoff_p1_end=_cutoff_p1_for_pk,
            cutoff_p2_end=_cutoff_p2_for_pk,
            base_front_len_m=_bf,
            base_side_len_m_p1=_bs,
            base_side_len_m_p2=_bs,
            min_corner_area_p1=_min_p1,
            min_corner_area_p2=_min_p2,
            g_values_map=_g_map,
            require_g_map=True,   # 🆕 P-C：真 G 驅動資格閘（側特定·來自 _G_true_p1/p2）
        )
        _l_v13 = _v13['p1_end']; _r_v13 = _v13['p2_end']
        # ── W-D.1.2 診斷 rows（app 13904-13949 原樣） ──
        for _dg_side, _dg_res in (('左', _l_v13), ('右', _r_v13)):
            _dg_win = ((_dg_res.get('winner') or {}).get('暫編地號'))
            for _dg_pass, _dg_list in (('達標', _dg_res.get('qualified', [])),
                                       ('未達標', _dg_res.get('eliminated', []))):
                for _dc in (_dg_list or []):
                    _corner_cand_diag.append({
                        '街廓': _lbl,
                        '端': _dg_side,
                        '候選地號': _dc.get('暫編地號', ''),
                        '原地號': _dc.get('原地號', ''),
                        '真交集(㎡)': round(float(_dc.get('_corner_intersection_area', 0) or 0), 2),
                        '整筆幾何(㎡)': round(float(_dc.get('_full_parcel_area',
                                                          _dc.get('physical_overlap_area', 0)) or 0), 2),
                        '範圍面積(㎡)': round(float(_dc.get('_corner_range_area', 0) or 0), 2),
                        'G估(㎡)': round(float(_dc.get('G_for_threshold', 0) or 0), 2),
                        # 🆕 P-C（裁定M·Q1）：達標決策所用之側特定真 G（G估欄保 estG·此為真 G）
                        '真G(㎡)': (round(float(_dc.get('_G_true', 0) or 0), 2)
                                    if _dc.get('_G_true') is not None else ''),
                        '門檻(㎡)': round(float(_dc.get('min_area_to_apply', 0) or 0), 2),
                        '範圍=門檻?': ('✅' if abs(float(_dc.get('_corner_range_area', 0) or 0)
                                                  - float(_dc.get('min_area_to_apply', 0) or 0)) < 0.5
                                      else '🔴異源·停查'),
                        '項三比(≤1)': ('🔴>1' if (float(_dc.get('_corner_intersection_area', 0) or 0)
                                                  > float(_dc.get('_corner_range_area', 0) or 0) + 0.01
                                                  and float(_dc.get('_corner_range_area', 0) or 0) > 0)
                                       else round(float(_dc.get('_corner_intersection_area', 0) or 0)
                                                  / max(float(_dc.get('_corner_range_area', 0) or 0), 1e-9), 4)),
                        '達標': _dg_pass,
                        '截角邊(range)': round(float(_dc.get('_corner_cut_den', 0) or 0), 3),
                        '臨截角': round(float(_dc.get('_corner_cut_len', 0) or 0), 3),
                        '側街邊(range)': round(float(_dc.get('_side_line_den', 0) or 0), 3),
                        '臨側街': round(float(_dc.get('_side_line_len', 0) or 0), 3),
                        '正街角分(0.4)': (round(float(_dc.get('_score_corner_cut', 0) or 0), 4)
                                          if '_score_corner_cut' in _dc else '—'),
                        '側街分(0.2)': (round(float(_dc.get('_score_side', 0) or 0), 4)
                                        if '_score_side' in _dc else '—'),
                        '跨占分(0.4)': (round(float(_dc.get('_score_overlap', 0) or 0), 4)
                                        if '_score_overlap' in _dc else '—'),
                        '總分': (round(float(_dc.get('priority_index', 0) or 0), 4)
                                 if 'priority_index' in _dc else '—'),
                        '原位次(投影序)': int(_dc.get('_pre_position_rank', 0) or 0),
                        '選中': ('✅' if (_dg_win and _dc.get('暫編地號') == _dg_win) else ''),
                    })
        # ── 指配 rows（app 13950-14009 原樣） ──
        _l_disp_min = ('無此側' if _min_p1 == float('inf') else f"{round(_min_p1, 2)}")
        _r_disp_min = ('無此側' if _min_p2 == float('inf') else f"{round(_min_p2, 2)}")
        _l_winner = _l_v13.get('winner')
        _r_winner = _r_v13.get('winner')
        _l_disp_winner = (
            '無此側' if _l_disp_min == '無此側'
            else (f"{_l_winner['歸戶群組']}（{_l_winner.get('原地號','')}）"
                  f"[{_l_winner.get('暫編地號','')}]"
                  if _l_winner else '⚠️ 強制抵費地')
        )
        _r_disp_winner = (
            '無此側' if _r_disp_min == '無此側'
            else (f"{_r_winner['歸戶群組']}（{_r_winner.get('原地號','')}）"
                  f"[{_r_winner.get('暫編地號','')}]"
                  if _r_winner else '⚠️ 強制抵費地')
        )
        _l_disp_score = (round(float(_l_winner.get('priority_index', 0)), 4)
                         if (_l_winner and _l_disp_min != '無此側') else '—')
        _r_disp_score = (round(float(_r_winner.get('priority_index', 0)), 4)
                         if (_r_winner and _r_disp_min != '無此側') else '—')
        _l_qcount = (len(_l_v13.get('qualified', [])) if _l_disp_min != '無此側' else '—')
        _r_qcount = (len(_r_v13.get('qualified', [])) if _r_disp_min != '無此側' else '—')
        # 🆕 W-D.2 P6：winners_state（鏡射 app f3_corner_winners；Step G driver 消費）
        _winners_state[_lbl] = {
            'p1_end': (_l_winner.get('暫編地號', '') if _l_winner else None),
            'p2_end': (_r_winner.get('暫編地號', '') if _r_winner else None),
            'method': 'V13_spatial_binding',
        }
        _corner_select_results.append({
            '街廓': _lbl,
            '演算法': ('V13' if _use_v13 else 'V12'),
            '候選來源': '🤖 自動 PK',
            '候選數': len(_candidates),
            '【左】最小面積(㎡)': _l_disp_min,
            '【右】最小面積(㎡)': _r_disp_min,
            '【左】達資格候選': _l_qcount,
            '【左】第1宗指配': _l_disp_winner,
            '【左】優先權指數': _l_disp_score,
            '【右】達資格候選': _r_qcount,
            '【右】第1宗指配': _r_disp_winner,
            '【右】優先權指數': _r_disp_score,
        })

    # ── W-D.1.3-d 抵費地驗收 rows（app 14107-14119 原樣） ──
    _offset_diag_rows = []
    for _r_off in (_corner_select_results or []):
        for _end_lbl_off, _min_key_off, _win_key_off in (
                ('左', '【左】最小面積(㎡)', '【左】第1宗指配'),
                ('右', '【右】最小面積(㎡)', '【右】第1宗指配')):
            if '強制抵費地' in str(_r_off.get(_win_key_off, '')):
                _offset_diag_rows.append({
                    '街廓': _r_off.get('街廓', ''),
                    '端': _end_lbl_off,
                    '抵費地面積＝range(㎡)': _r_off.get(_min_key_off),
                    '指配': '強制抵費地',
                })

    # ── 🆕 W-D.2 P6：forced_offset_map（鏡射 app f3L_forced_offset，含 W-D.2 min_area 鍵）──
    _forced_offset_map = {}

    def _fo_min_area(_v):
        try:
            return float(_v)
        except (TypeError, ValueError):
            return 0.0
    for _r_pk in (_corner_select_results or []):
        _lbl_pk = _r_pk.get('街廓', '')
        _l_forced = ('強制抵費地' in str(_r_pk.get('【左】第1宗指配', '')))
        _r_forced = ('強制抵費地' in str(_r_pk.get('【右】第1宗指配', '')))
        _l_has_side = (_r_pk.get('【左】最小面積(㎡)') != '無此側')
        _r_has_side = (_r_pk.get('【右】最小面積(㎡)') != '無此側')
        _forced_offset_map[_lbl_pk] = {
            'left_forced_offset': bool(_l_forced and _l_has_side),
            'right_forced_offset': bool(_r_forced and _r_has_side),
            'left_has_side': bool(_l_has_side),
            'right_has_side': bool(_r_has_side),
            'left_corner_min_area': (_fo_min_area(_r_pk.get('【左】最小面積(㎡)'))
                                     if (_l_forced and _l_has_side) else 0.0),
            'right_corner_min_area': (_fo_min_area(_r_pk.get('【右】最小面積(㎡)'))
                                      if (_r_forced and _r_has_side) else 0.0),
        }

    return (_corner_cand_diag, _corner_select_results, _offset_diag_rows,
            _winners_state, _forced_offset_map)
