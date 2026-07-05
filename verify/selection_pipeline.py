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

def build_build_parcels(ns, fake_st, v6_bytes, cb):
    """真函式管線：parse_cadastral_geofile → 面積交叉驗證換位 → overlay →
    四欄面積 → cut_type → build_parcels（可建築、未併公設）。"""
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
    fcb = ns["F3_CATEGORY_BURDEN"]
    build_parcels = [tp for tp in temp_parcels
                     if fcb.get(tp["街廓分類"], "") == "可建築土地"
                     and not tp.get("_merged_into_g", False)]
    return temp_parcels, build_parcels, swaps


# ═══════════════ 3. PK orchestration（app 13799-14060 + 14107-14119 複刻） ═══════════════

def run_corner_pk(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback):
    """一情境：對每可建築街廓跑 select_corner_lots_both_sides_v12，
    回傳 (診斷rows, 指配rows, 抵費地rows)。欄名/取值/四捨五入逐行同 app。"""
    ss = fake_st.session_state
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
    for b in _build_blocks:
        _lbl = b['label']
        _row = rows_by_lbl.get(_lbl)
        if _row is None:
            continue
        ss['f3_current_pk_block'] = _lbl
        _cad_fl_lstep = (ss.get('f3_cad_front_lines', {}) or {}).get(_lbl, {})
        _fl_p1_lstep = _cad_fl_lstep.get('p1') if _cad_fl_lstep else None
        _fl_p2_lstep = _cad_fl_lstep.get('p2') if _cad_fl_lstep else None
        _all_in_blk = by_blk.get(_lbl, [])
        _candidates_pool = _all_in_blk   # Patch D-1：候選池一律全自動 PK
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
        _g_map = {c['暫編地號']: c['G_estimated'] for c in _candidates}
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
                        '原位次(距角序·暫行)': round(float(_dc.get('_dist_to_corner_point',
                                                                  _dc.get('_dist_to_side_line', 0)) or 0), 2),
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

    return _corner_cand_diag, _corner_select_results, _offset_diag_rows
