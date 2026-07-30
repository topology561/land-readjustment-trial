# W-G.5 K-6-A【A】**MinA 消費點窮盡清單**（commit 錨定 `e583075`）

> 產生法：`docs/reports/` 內本檔由腳本掃 `app.py`／`tests`／`verify`（排除 `out/`、`__pycache__`）之
> 全部 `.py`，識別字＝`MinA`／`min_alloc_area`／`f3_min_alloc_area_by_label`／`_mina_by_block`／
> `mina_by_blk`／`最小分配面積`／`達標`／`未達標`／`mina[`／`_mina4`／`min_area_by_block`／
> `_min_area`／`min_area_to_apply`／`region_min`／`_valid_mins`／`corner_min_area`。
> 已濾**行首**為 `#`／`·`／`*`／`|`／`⚠`／`⛔`／`🔴`／`"""` 者。
> ⚠️ **本文之「窮盡」限於上列 16 個識別字**——該字集**漏了 `wf_f0_mina`**，
> 更正見**檔末附錄**（合計應為 **282**）。本體維持 `e583075` 錨定**不動**（快照，非活文件）。

> 🔒 **停機條件甲之判定**：**無任何無法歸類之消費點**（全部落入 A1/A2/B/C/D/E/F/G 七類）⇒ **不停機**。

## 角色分布

| 角色 | 筆數 | K-6-A 處置 |
|---|---|---|
| A1 街角規定面積（判準3·**不動**） | 36 | **不動**——判準 3（街角規定面積）自有依據，K-6 §零-3 僅補其寬度來源之解釋 |
| A2 街角PK診斷欄（源＝判準3·**不動**） | 17 | **不動**——街角 PK 診斷欄之『達標』其源即判準 3 |
| B 逐街廓達標判定（**改寬深雙檢**） | 89 | **改寬深雙檢**（K-6 §零-1） |
| C 池三則（**改寬深雙檢**） | 14 | **改寬深雙檢**（池亦當一宗量） |
| D region_min 推導／7-0a（**算式保留·用途收斂**） | 16 | 算式保留不動；加註唯一用途＋立閘禁其入達標/池三則路徑 |
| E 1/2 門檻（現金補償·**待 K-6 §零-4 收斂**） | 15 | ⚠️ K-6 §零-4 只述「合併後」之現金補償/增配二擇一；**1/2 門檻本身之去留未明示** ⇒ 標旗上呈 |
| F 僅顯示／報表 | 13 | 隨 B/C 之欄位語意同步改字 |
| G 文字敘述（docstring／UI 說明·**非消費點**） | 78 | 文字敘述——隨對應碼點同步改寫 |
| **合計** | **278** | |

## 逐點清單（依角色→檔→行）


### A1 街角規定面積（判準3·**不動**）

- `app.py:6222` — `corner_min_area=None, _label=''):`
- `app.py:6237` — `(Ⅰ) 街角規定範圍之**寬度即法規最小寬** ⇒ 「G ≥ 街角最小分配面積」**蘊含**`
- `app.py:6258` — `'_width_k4_threshold': (round(float(corner_min_area), 2)`
- `app.py:6259` — `if corner_min_area is not None else None),`
- `app.py:6867` — `'left_corner_min_area', 'right_corner_min_area'}`
- `app.py:6940` — `float(forced_offset.get('right_corner_min_area', 0) or 0)`
- `app.py:6943` — `float(forced_offset.get('left_corner_min_area', 0) or 0)`
- `app.py:9159` — `min_corner_area_p1   p1 端街角地最小分配面積`
- `app.py:9403` — `cand_p1['min_area_to_apply'] = float(min_corner_area_p1)`
- `app.py:9421` — `cand_p2['min_area_to_apply'] = float(min_corner_area_p2)`
- `app.py:9506` — `if cand_G < cand.get('min_area_to_apply', 0):`
- `app.py:9508` — `f"G 值 {cand_G:.2f} < 最小分配面積 {cand.get('min_area_to_apply', 0):.2f}"`
- `app.py:16261` — `'門檻(㎡)': round(float(_dc.get('min_area_to_apply', 0) or 0), 2),`
- `app.py:16264` — `- float(_dc.get('min_area_to_apply', 0) or 0)) < 0.5`
- `app.py:16376` — `'left_corner_min_area': (`
- `app.py:16379` — `'right_corner_min_area': (`
- `app.py:16486` — `"其**面積鎖定＝街角最小分配面積範圍面積**（§1.1 之 T-多邊形，即本表『抵費地面積＝range』）。\n\n"`
- `app.py:18738` — `corner_min_area=_thr_jw,`
- `app.py:18766` — `f"——(Ⅰ) 街角規定範圍之寬度**即**法規最小寬 ⇒ `G ≥ 街角最小分配面積`"`
- `tests/test_corner_priority_golden.py:63` — `"暫編地號": "1", "min_area_to_apply": 0.0, "G_value": 1e9,`
- `tests/test_corner_priority_golden.py:69` — `"暫編地號": "2", "min_area_to_apply": 0.0, "G_value": 1e9,`
- `verify/app_harvest.py:167` — `{"暫編地號": "1", "min_area_to_apply": 0.0, "G_value": 1e9,`
- `verify/app_harvest.py:170` — `{"暫編地號": "2", "min_area_to_apply": 0.0, "G_value": 1e9,`
- `verify/fixture_end_fallback.py:63` — `"left_corner_min_area": 0.0, "right_corner_min_area": 0.0})`
- `verify/fixture_end_winner.py:118` — `"left_corner_min_area": 0.0, "right_corner_min_area": 0.0}`
- `verify/m_rescue.py:34` — `- **T-5**：**全 data-driven**（跨占＝E-1.7 真交集>1.0㎡；未達＝`G<MinA[blk]`／`<街角規定面積`；`
- `verify/probes/probe_ruling_N_e1_touch.py:77` — `mina_by_blk, corner_area_by_blk):`
- `verify/probes/probe_ruling_N_e1_touch.py:81` — ``G ≥ 街角最小分配面積`（＝ (Ⅰ) 街角規定範圍面積）之**蘊含**。`
- `verify/probes/probe_ruling_N_e1_touch.py:101` — `corner_min_area=_thr,`
- `verify/selection_pipeline.py:479` — `'門檻(㎡)': round(float(_dc.get('min_area_to_apply', 0) or 0), 2),`
- `verify/selection_pipeline.py:481` — `- float(_dc.get('min_area_to_apply', 0) or 0)) < 0.5`
- `verify/selection_pipeline.py:581` — `'left_corner_min_area': (_fo_min_area(_r_pk.get('【左】最小面積(㎡)'))`
- `verify/selection_pipeline.py:583` — `'right_corner_min_area': (_fo_min_area(_r_pk.get('【右】最小面積(㎡)'))`
- `verify/wf_f1.py:218` — `float(fo.get("left_corner_min_area", 0.0) or 0.0), 'left', _label=f"{lbl}·F.1")`
- `verify/wf_f4.py:1303` — `float(fo.get("left_corner_min_area", 0.0) or 0.0),`
- `verify/wf_f4.py:1314` — `float(fo.get("right_corner_min_area", 0.0) or 0.0),`

### A2 街角PK診斷欄（源＝判準3·**不動**）

- `app.py:16245` — `for _dg_pass, _dg_list in (('達標', _dg_res.get('qualified', [])),`
- `app.py:16246` — `('未達標', _dg_res.get('eliminated', []))):`
- `app.py:16272` — `'達標': _dg_pass,`
- `app.py:16422` — `"**選中**＝該端達標候選中總分最高者（位次 1 街角地）。\n\n"`
- `verify/probes/probe_corner_trueG.py:24` — `改讀既有診斷之 `總分`，只**重判達標**、再取達標中 `總分` 最大者為新 winner`
- `verify/probes/probe_corner_trueG.py:109` — `f"{'ΔG':>9}{'總分':>8} 舊達標 新達標")`
- `verify/probes/probe_corner_trueG.py:163` — `_dz = str(r.get("達標", "")).strip()`
- `verify/probes/probe_corner_trueG.py:164` — `if _dz not in ("達標", "未達標"):`
- `verify/probes/probe_corner_trueG.py:165` — `_fail(f"{pid} 『達標』欄非預期值 {_dz!r}（欄語意已變·禁猜）")`
- `verify/probes/probe_corner_trueG.py:166` — `old_ok = (_dz == "達標")`
- `verify/probes/probe_corner_trueG.py:177` — `score = _num(r.get("總分"))          # None ＝ 該候選原未達標·無三指數分數`
- `verify/probes/probe_corner_trueG.py:185` — `f"{'  🚩新達標但無三指數分數·需重算' if need_rescore else ''}")`
- `verify/selection_pipeline.py:463` — `for _dg_pass, _dg_list in (('達標', _dg_res.get('qualified', [])),`
- `verify/selection_pipeline.py:464` — `('未達標', _dg_res.get('eliminated', []))):`
- `verify/selection_pipeline.py:488` — `'達標': _dg_pass,`
- `verify/wf_f0.py:253` — `"達標": "—", "去向": "全達標·留置原位", "Δ非線性(㎡)": ""})`
- `verify/wf_f0.py:265` — `"達標": ("✅" if ok else "🔴"), "去向": dest,`

### B 逐街廓達標判定（**改寬深雙檢**）

- `app.py:8768` — `def merge_subparcels_by_parent(g_rows: list, min_area_by_block: dict) -> dict:`
- `app.py:8776` — `min_area_by_block  {街廓編號: 該街廓最小分配面積(㎡)}`
- `app.py:8819` — `min_area = float(min_area_by_block.get(blk, 0.0) or 0.0)`
- `app.py:8821` — `r['_min_area'] = round(min_area, 2)`
- `app.py:8863` — `'G(㎡)': r['G(㎡)'], '最小分配面積(㎡)': r['_min_area'],`
- `app.py:8871` — `r['最小分配面積(㎡)'] = r['_min_area']`
- `app.py:8877` — `'目前G(㎡)': r['G(㎡)'], '最小分配面積(㎡)': r['_min_area'],`
- `app.py:8909` — `r_out['最小分配面積(㎡)'] = r['_min_area']`
- `app.py:8919` — `r_out['最小分配面積(㎡)'] = r['_min_area']`
- `app.py:8930` — `p_out['最小分配面積(㎡)'] = primary['_min_area']`
- `app.py:8933` — `if primary['_min_area'] > 0 and new_G < primary['_min_area']:`
- `app.py:8938` — `'最小分配面積(㎡)': primary['_min_area'],`
- `app.py:16356` — `def _fo_min_area(_v):`
- `app.py:16377` — `_fo_min_area(_r_pk.get('【左】最小面積(㎡)'))`
- `app.py:16380` — `_fo_min_area(_r_pk.get('【右】最小面積(㎡)'))`
- `app.py:18666` — `_min_area_by_block = {}`
- `app.py:18679` — `_min_area_by_block[_lbl] = round(`
- `app.py:18682` — `_min_area_by_block[_lbl] = _info['min_area']  # fallback 法定值`
- `app.py:18779` — `st.session_state['f3_G_values'], _min_area_by_block)`
- `app.py:18806` — `st.session_state['f3_min_area_by_block'] = _min_area_by_block`
- `verify/m_rescue.py:39` — `U₀ = {宗: G(A₀) < MinA[blk]}；Corner₀ = {forced 端之跨占-未達候選}`
- `verify/m_rescue.py:211` — `def build_plan(*, tag, gA_rows, mina_by_blk, gid_of, corner_ctx, zone_of, pre_price,`
- `verify/m_rescue.py:217` — `mina_by_blk  {blk: MinA}`
- `verify/m_rescue.py:238` — `if source_g_a0(r, pid) < mina_by_blk.get(r.get("所屬街廓"), 0.0)}`
- `verify/m_rescue.py:340` — `if float(r2.get("G(㎡)", 0) or 0) < mina_by_blk.get(_blk2, 0.0):`
- `verify/m_rescue.py:342` — `"gap": mina_by_blk.get(_blk2, 0.0) - float(r2.get("G(㎡)", 0) or 0)})`
- `verify/probes/probe_capacity_decomp.py:104` — `gt = _valid_G(G, W, mw_by[b], mina[b])`
- `verify/probes/probe_capacity_decomp.py:110` — `cap = reach_fn(b) - mina[b] + 0.5`
- `verify/probes/probe_capacity_decomp.py:136` — `if all(cs <= reach_fn(b) - mina[b] + 0.5 for b, cs in by.items()):`
- `verify/probes/probe_capacity_decomp.py:152` — `_reach = reachable[b]; _cap = _reach - mina[b] + 0.5`
- `verify/probes/probe_capacity_decomp.py:162` — `f"{_un_self:9.2f}{_flag:>2} {_reach:9.2f} {mina[b]:7.2f} {_cap:6.2f} "`
- `verify/probes/probe_ruling_K4_3_source.py:109` — `mina_by_blk=ctx["mina"], gid_of=ctx["gid_of"],`
- `verify/probes/probe_ruling_N_e1_touch.py:120` — `_merged = ns["merge_subparcels_by_parent"](_rows, mina_by_blk)["merged_rows"]`
- `verify/run_verification.py:386` — `return wf_f0._mina_by_block(ns, snapshot, cb_by)`
- `verify/run_verification.py:581` — `tag=tag, gA_rows=_sg_a0["g_rows"], mina_by_blk=_mina_m5,`
- `verify/run_verification.py:1168` — `_, _mq2 = _w4._mina_by_block(ns, _snap2, cb_by, _bb4)`
- `verify/run_verification.py:1546` — `if gq < _mina4[blk] - 0.05:`
- `verify/run_verification.py:1547` — `_q3bad.append(f"{tag}/{r['歸戶']}@{blk}: 配額 {gq}<MinA {_mina4[blk]}")`
- `verify/selection_pipeline.py:565` — `def _fo_min_area(_v):`
- `verify/wd4_tier_list.py:72` — `def _mina_by_block(ns, snapshot, cb_by, build_blocks):`
- `verify/wd4_tier_list.py:83` — `mina[lbl] = round(depth * mw, 2)   # 正典 rounded`
- `verify/wd4_tier_list.py:237` — `elif any(sumG >= mina[l] for l in mina):`
- `verify/wd4_tier_list.py:258` — `_inc = round(mina[_tgt] - sumG, 2)`
- `verify/wd4_tier_list.py:310` — `"該側MinA(㎡)": round(mina.get(r["所屬街廓"], 0), 2),`
- `verify/wf_f0.py:75` — `def _mina_by_block(ns, snap, cb_by):`
- `verify/wf_f0.py:106` — `if float(l["G(㎡)"]) >= mina[blk] and not l["畸零地旗標"].strip()]`
- `verify/wf_f0.py:162` — `mina = _mina_by_block(ns, snap, cb_by)`
- `verify/wf_f0.py:252` — `"Σa(㎡)": "", "G(Σa)(㎡)": "", "MinA_街廓": mina[d["blk"]],`
- `verify/wf_f0.py:259` — `ok = G >= mina[d["blk"]]`
- `verify/wf_f0.py:264` — `"Σa(㎡)": sa, "G(Σa)(㎡)": round(G, 2), "MinA_街廓": mina[d["blk"]],`
- `verify/wf_f0.py:271` — `f"🔴 停機#4：{d['gid']} 合併後 G(Σa)={G:.2f}<MinA 且無下一級可走（§7 全鏈窮盡）")`
- `verify/wf_f2.py:81` — `if any(float(r["G(㎡)"]) >= mina[blk] and not r["畸零地旗標"].strip() for r in rows):`
- `verify/wf_f2.py:123` — `mina = wf_f0._mina_by_block(ns, snap, cb_by)`
- `verify/wf_f2.py:207` — `"MinA": mina[l],`
- `verify/wf_f2.py:240` — `if float(r["G(㎡)"]) < mina[r["所屬街廓"]]:`
- `verify/wf_f2.py:241` — `raise RuntimeError(f"🔴 [{tag}] 目標宗 {tid} 灌後 G={r['G(㎡)']}<MinA_{r['所屬街廓']}")`
- `verify/wf_f3.py:93` — `mina = wf_f0._mina_by_block(ns, snap, cb_by)`
- `verify/wf_f4.py:318` — `mina = wf_f0._mina_by_block(ns, snap, cb_by)`
- `verify/wf_f4.py:357` — `if any(float(x["G(㎡)"]) >= mina[blk] and not x["畸零地旗標"].strip()`
- `verify/wf_f4.py:363` — `if float(x["G(㎡)"]) >= mina[tb] and not x["畸零地旗標"].strip()],`
- `verify/wf_f4.py:570` — `return _reach(blk) - (mina[blk] + E1_MARGIN)`
- `verify/wf_f4.py:575` — `if _budget(blk) < mina[blk] - 0.5:       # 容不下一片 ≥MinA 且保殘池`
- `verify/wf_f4.py:577` — `if demG < mina[blk] - 0.5:               # 小片：概念4 以引擎 solo 實測`
- `verify/wf_f4.py:579` — `if G is None or a2p < a2 - 0.01 or G < mina[blk] - 0.01:`
- `verify/wf_f4.py:617` — `if _tgtG < mina[blk] - 0.01 or _a2_new <= TOL:`
- `verify/wf_f4.py:620` — `_why = f"縮至實可容 {_fit:.2f} 仍 <MinA {mina[blk]:.2f}"`
- `verify/wf_f4.py:682` — `small = [g for g in gs if shares[g] < mina[blk] - 0.01`
- `verify/wf_f4.py:698` — `and _budget(b) >= mina[b] - 0.5]`
- `verify/wf_f4.py:701` — `need = (mina[b2] + 0.5) / (_conv(g, b2) * _ratio(g, b2))`
- `verify/wf_f4.py:725` — `if filled and reach < mina[blk] + E1_MARGIN - 0.05:`
- `verify/wf_f4.py:731` — `a2fix = _bisect_G(eng, pid, g_now - (mina[blk] + E1_MARGIN - reach), TOL)`
- `verify/wf_f4.py:770` — `placed[(gid, blk)] = _bisect_valid(eng, pid, blk, _mw_e1[blk], mina[blk])`
- `verify/wf_f4.py:771` — `if _reach(blk) < mina[blk] - 0.05:`
- `verify/wf_f4.py:772` — `raise RuntimeError(f"🔴 [{tag}] E1 valid-width 後 {blk} 可達殘池<MinA（餘裕不足）")`
- `verify/wf_f4.py:848` — `if pid in E and float(E[pid]["G(㎡)"]) < mina[blk] - TOL:`
- `verify/wf_f4.py:849` — `raise RuntimeError(f"🔴 [{tag}] 概念4 破：{pid} G={E[pid]['G(㎡)']}<MinA_{blk}")`
- `verify/wf_f4.py:956` — `if float(r["G(㎡)"]) < mina[blk] - TOL:`
- `verify/wf_f4.py:957` — `e4_viol.append(f"{k}: G={r['G(㎡)']} < MinA_{blk}")`
- `verify/wf_f4.py:991` — `"MinA": mina[l],`
- `verify/wf_f4.py:1083` — `if reachable[b] < mina[b] - 0.5:`
- `verify/wf_f4.py:1112` — `gt = _valid_G(G, W, mw_by[b], mina[b])         # 合法基地目標 G（含 min_width）`
- `verify/wf_f4.py:1115` — `if consume > reachable[b] - mina[b] + 0.5:      # solo 已超容`
- `verify/wf_f4.py:1140` — `if any(cs > reachable[b] - mina[b] + 0.5 for b, cs in by_blk.items()):`
- `verify/wf_f4.py:1185` — `gt = _valid_G(G, W, mw_by[b], mina[b])     # 合法基地目標（含 min_width）`
- `verify/wf_f4.py:1191` — `if ok and all(csm[b] <= reachable[b] - mina[b] + 0.5 for b in csm):`
- `verify/wf_f4.py:1229` — `if W_ap >= mw_by[b] + WIDTH_MARGIN - 1e-6 and G_ap >= mina[b] - TOL:  # 已達合法基地：全額`
- `verify/wf_f4.py:1232` — `_bisect_valid(eng, pid, b, mw_by[b], mina[b])`
- `verify/wf_f4.py:1236` — `if eng.rows()[pid]["畸零地旗標"].strip() or G_fin < mina[b] - TOL:`
- `verify/wf_f4.py:1563` — `float(r["G(㎡)"]) >= mina[r["所屬街廓"]] - 0.05`

### C 池三則（**改寬深雙檢**）

- `app.py:19584` — `title="池終態（黃＝池/抵費地；池三則：各塊 0 或 ≥MinA）"),`
- `verify/run_verification.py:1482` — `_mina4 = wf_f0._mina_by_block(ns, snapshot, cb_by)   # 區塊 MinA（池三則/Q3 斷言）`
- `verify/run_verification.py:1509` — `_mid4 = [l for l, v in a4["pool_final"].items() if 0.5 < v < _mina4[l]]`
- `verify/run_verification.py:1510` — `results.append((f"F.4 池終態三則{tag}（各塊 0 或 ≥MinA）", not _mid4, _mid4))`
- `verify/wf_f2.py:202` — `if 0 < poolC[l] < mina[l]:`
- `verify/wf_f2.py:208` — `"三則": ("🔴落(0,MinA)" if 0 < poolC[l] < mina[l]`
- `verify/wf_f2.py:209` — `else ("歸零" if poolC[l] < 1 else "≥MinA"))})`
- `verify/wf_f3.py:169` — `mid = [l for l in poolD if 0 < poolD[l] < mina[l]]`
- `verify/wf_f3.py:184` — `"池差(㎡)": round(poolD[l] - poolC[l], 2), "MinA": mina[l],`
- `verify/wf_f4.py:23` — `- **池三則**（禁中間態）：cap＝池−MinA；「吃光歸零」僅限塊內無 S=0 殘片（strip 幾何不可達）；`
- `verify/wf_f4.py:921` — `mid = [l for l in pool_final if 0.5 < pool_final[l] < mina[l] - 0.05]`
- `verify/wf_f4.py:923` — `raise RuntimeError(f"🔴 [{tag}] 終態池落 (0,MinA)：{ {l: round(pool_final[l],2) for l in mid} }——停機上呈")`
- `verify/wf_f4.py:992` — `"三則": ("歸零" if pool_final[l] < 1 else "≥MinA")}`
- `verify/wf_f4.py:1056` — `- 池三則以容量約束（每塊 Σconsume ≤ reachable−MinA，留 ≥MinA 可達殘池；S=0 片入 unreach）。`

### D region_min 推導／7-0a（**算式保留·用途收斂**）

- `app.py:15757` — `_depth_info_by_blk = {}; _depth_use_by_blk = {}; _min_alloc_area_by_blk = {}`
- `app.py:15813` — `_min_alloc_area_by_blk[_lbl] = (round(_depth_use_by_blk[_lbl] * _mw_d, 2)`
- `app.py:15817` — `st.session_state['f3_min_alloc_area_by_label'] = _min_alloc_area_by_blk`
- `app.py:15821` — `_valid_mins = [v for v in _min_alloc_area_by_blk.values() if v is not None and v > 0]`
- `app.py:15822` — `_region_min = min(_valid_mins) if _valid_mins else None`
- `app.py:15828` — `'region_min': _region_min, 'total_area': round(_total_area_70a, 2),`
- `app.py:15830` — `'argmin_blk': (min(((k, v) for k, v in _min_alloc_area_by_blk.items()`
- `app.py:15832` — `key=lambda kv: kv[1])[0] if _valid_mins else None),`
- `app.py:15833` — `'pass': (_region_min is None) or (_C_70a <= 0) or (_region_min <= _pool_70a),`
- `app.py:15835` — `if _region_min is not None and _C_70a > 0 and _region_min > _pool_70a:`
- `app.py:15837` — `f"🔴 §7-0a 前置地基檢查未過：全區最小分配面積 {_region_min:.2f}㎡ "`
- `app.py:15841` — `elif _region_min is not None and _C_70a > 0:`
- `app.py:15843` — `f"✅ §7-0a 地基檢查 PASS：全區最小分配面積 {_region_min:.2f}㎡（最淺乘積街廓 "`
- `app.py:18228` — `_ma = st.session_state.get('f3_min_alloc_area_by_label', {}) or {}`
- `app.py:18244` — `f"**⑥ 7-0a 前置地基檢查：{_pf}**　region_min = "`
- `app.py:18245` — `f"{_70.get('region_min')}㎡（最淺乘積街廓 {_70.get('argmin_blk')}）"`

### E 1/2 門檻（現金補償·**待 K-6 §零-4 收斂**）

- `app.py:8788` — `'cash_compensation': 未達最小分配面積 1/2 的暫編地號（建議現金補償）,`
- `app.py:8864` — `'狀態': '未達最小分配面積 1/2（建議現金補償）',`
- `app.py:8881` — `for k in ('_min_area', '_need_merge', '_half_min'):`
- `app.py:8912` — `for k in ('_min_area', '_need_merge', '_half_min'):`
- `app.py:8922` — `for k in ('_min_area', '_need_merge', '_half_min'):`
- `app.py:8944` — `for k in ('_min_area', '_need_merge', '_half_min'):`
- `app.py:18660` — `1. 暫編地號 G 值 **< 最小分配面積 1/2** → 建議**現金補償**`
- `app.py:18798` — `st.warning(f"⚠️ 共 {len(_merge_res['cash_compensation'])} 筆暫編地號未達最小分配面積 1/2，建議現金補償：")`
- `verify/run_verification.py:1123` — `[] if _ok_der else [f"MinA_區={_d0['mina_qu']} ½顯示={_d0['half_disp']}"]))`
- `verify/wd4_tier_list.py:158` — `mina, mina_qu = _mina_by_block(ns, snapshot, cb_by, build_blocks)`
- `verify/wd4_tier_list.py:159` — `half_disp = _half_display(mina_qu)   # 僅顯示；判定式用 2×ΣG≥MinA_區`
- `verify/wd4_tier_list.py:275` — `_path = ("公設軌·達標門檻＝區標準 " + f"{mina_qu}" +`
- `verify/wd4_tier_list.py:402` — `print(f"[{tag}] MinA_區={d['mina_qu']}(期114.07) ½顯示={d['half_disp']}(期57.04) "`
- `verify/wf_f4.py:504` — `half_r0[gid] = (G0, 2 * G0 >= mina_qu)     # ½線＝MinA_區（區內標準·非 mina[blk]）`
- `verify/wf_f4.py:845` — `if GE > 0 and 2 * GE < mina_qu:            # ½線＝MinA_區（同 :458）`

### F 僅顯示／報表

- `app.py:10151` — `'備註': f'按比例發還 {ratio:.2%}（不受最小分配面積限制）'`
- `app.py:15987` — `st.info("無可建築土地街廓 → 不需計算街角地最小分配面積")`
- `app.py:18227` — `st.markdown("**⑤ 街廓深度（沿 ALLOC，方法A主用/B驗證）+ 最小分配面積（D_avg×min_width）**")`
- `app.py:18654` — `st.markdown("#### 🧮 步驟 J：最小分配面積判斷 + 同原地號合併")`
- `app.py:18693` — `with st.expander("📑 各街廓最小分配面積對照（依畸零地附表）", expanded=False):`
- `app.py:18810` — `st.info(f"ℹ️ 共 {len(_merge_res['cross_block_needed'])} 個原地號於所屬街廓合併後仍未達最小分配面積 → 需進行**跨街廓調配**（§31 機制）")`
- `verify/m_rescue.py:240` — `L.append(f"[{tag}] U₀（未達 MinA·可出資）＝{len(U0)} 宗")`
- `verify/m_rescue.py:353` — `L.append(f"  ② {aw['blk']}{aw['side']}·{gid}：無「較大但未達 MinA」目標（給者≠受者）⇒ 全額轉③")`
- `verify/probes/probe_capacity_decomp.py:148` — `L.append("塊    pool    碎片Σ  forced鎖Σ unreach自檢  reachable   MinA   容量  最小cons 可容上界")`
- `verify/probes/probe_corner_trueG.py:215` — `L.append(f"  {blk} {end}：🚩 **無法判定**——新達標集合含未算三指數者 "`
- `verify/probes/probe_corner_trueG.py:247` — `L.append("  （無餘裕 <20㎡ 之新達標候選）")`
- `verify/probes/probe_ruling_N_depth.py:240` — `L.append(f"  ⇒ **N-16(b) 區內最小分配面積 ＝ {_mw_min:.2f} × {avg_by[_shallow]:.4f}"`
- `verify/selection_pipeline.py:444` — `_g_map = {c['暫編地號']: c['G_estimated'] for c in _candidates}   # estG（診斷 G估欄·非達標）`

### G 文字敘述（docstring／UI 說明·**非消費點**）

- `app.py:7707` — `差額地價法定範圍窄（僅歸戶合併後未達 MinA/2 者），非一般性帳-幾何差吸收機制。`
- `app.py:8770` — `同原地號合併：將未達所屬街廓最小分配面積的暫編地號，併入該原地號之最大暫編地號`
- `app.py:8780` — `2. 每筆暫編地號 G 值若 < 所屬街廓最小分配面積，標為「待合併」`
- `app.py:8781` — `3. 同原地號內：將所有「待合併」G 值加總後，併入「面積最大且 G ≥ 最小分配面積」的暫編地號`
- `app.py:8782` — `4. 若同原地號合計 G 值仍未達「主要暫編地號所屬街廓最小分配面積」，則該原地號整體標記`
- `app.py:8979` — `（範圍面積暴增數十倍 ⇒ 街角地最小分配面積門檻整個失真）。`
- `app.py:8983` — `三者**皆直接污染街角地最小分配面積門檻** ⇒ no-silent-fallback：一律 loud。`
- `app.py:9019` — `f"使最小分配面積門檻整個失真。上游幾何有誤，停") from _e_split`
- `app.py:9030` — `f"街角地最小分配面積門檻。停") from _e_ch`
- `app.py:9147` — `🚨 強化點 2：第一關用 G 值（非物理跨占面積）做最小分配面積門檻判斷`
- `app.py:9958` — `min_area_m2                       最小分配面積閾值`
- `app.py:10065` — `min_area_m2                    最小分配面積閾值`
- `app.py:10106` — `此發還面積不受最小分配面積限制。`
- `app.py:10114` — `min_area_m2             最小分配面積閾值（此處供參考；按比例發還不受限制）`
- `app.py:15720` — `- **街角地最小分配面積** = (街角地最小分配寬度 × 街廓分配深度) − 截角面積`
- `app.py:16414` — `f"（{len(_corner_cand_diag)} 筆候選 · 三分項 0.4/0.2/0.4 · 達標/選中）",`
- `app.py:16421` — `"**達標**＝過第一關門檻（G估 ≥ 街角地最小分配面積）；未達標不計分（顯示 —）。"`
- `app.py:16426` — `"winner＝達標候選中真交集最大者（項一/項二仍常數 0.4/0.2，per-parcel 為 -c）；"`
- `app.py:18235` — `'法': _d.get('method'), '最小分配面積(㎡)': _ma.get(_lbl),`
- `app.py:18657` — `查得最小分配寬度 × 深度 → 最小分配面積。`
- `app.py:18661` — `2. 暫編地號 G 值 **≥ 1/2 但 < 最小分配面積** → 合併至**同原地號面積最大之暫編地號**`
- `app.py:18662` — `3. 若同原地號所有暫編地號 G 值**加總後仍未達最小分配面積** → 需**跨街廓調配**（§31 機制）`
- `app.py:18689` — `'最小分配面積(㎡)': _info['min_area'],`
- `app.py:18787` — `'G(㎡)', '合併後G(㎡)', '最小分配面積(㎡)',`
- `app.py:18792` — `'最小分配面積(㎡)') if c in _df_merge.columns}`
- `tests/test_corner_priority_golden.py:82` — `assert set(by_id) == {"1", "2"}, f"兩候選皆應達標，實得 {sorted(by_id)}"`
- `verify/m_rescue.py:12` — `② 餘額再併其他「**較大但未達該街廓 MinA**」土地（**至達 MinA**）；`
- `verify/m_rescue.py:13` — `③ 目標皆達標而仍有餘額 ⇒ 餘額併入**該街角地**（街角＝**最後歸宿**）。`
- `verify/m_rescue.py:150` — `return 0.0, g_fn(a_base)                 # 本已達標（不應進①·防禦）`
- `verify/m_rescue.py:262` — `continue        # 本已達標（非①母體·由既有 PK 處理）`
- `verify/m_rescue.py:350` — `f"🔴 M-5 ②（{aw['blk']}{aw['side']}·{gid}）：存在「較大但未達 MinA」目標 "`
- `verify/probes/probe_capacity_decomp_solve.py:14` — `逐塊表（pool／碎片／forced鎖定／reachable／MinA）＋完整 consume matrix。`
- `verify/probes/probe_capacity_decomp_solve.py:22` — `容量 `cap(b) = reachable(b) − MinA(b) + 0.5`（治理碼 `wf_f4._e2_optimal` 同式·`grep -n "def _e2_optimal" verify/wf_f4.py`）。`
- `verify/probes/probe_ruling_N_depth.py:209` — `" ＋ N-16(b) 區內最小分配面積")`
- `verify/probes/probe_ruling_N_depth.py:230` — `"與區內最小分配面積**皆為暫定**、補圖後須重算。")`
- `verify/probes/probe_ruling_N_p8.py:16` — `(甲) `snapshot.blocks[blk]['街廓分配深度_m']`（現行 MinA 所用）`
- `verify/run_verification.py:1122` — `results.append(("W-D.4 MinA_區==114.07(正典rounded)·½顯示==57.04(Decimal非round)", _ok_der,`
- `verify/run_verification.py:1170` — `results.append(("W-D.4 MinA_區 reverse-test(改深度→隨動·非寫死)", _ok_rev,`
- `verify/run_verification.py:1171` — `[] if _ok_rev else [f"改 R4 深度20→MinA_區={_mq2}(期70)"]))`
- `verify/run_verification.py:1277` — `results.append(("F.0 不達標二格 G009→F.2·G014→F.4（先併再標旗轉出）", _ok_rt,`
- `verify/run_verification.py:1554` — `results.append(("F.4 Q3＋裁示1(a)（配額=合法基地·達標·帳表一致·禁超額）", not _q3bad, _q3bad[:5]))`
- `verify/wd4_tier_list.py:20` — `- **公設軌不判梯次**（`梯次="—"`）、撤出梯3；達標門檻＝**區標準 MinA_區**（手冊 宗地分配原則(三)）；`
- `verify/wd4_tier_list.py:31` — `- WARNING-B：MinA 斷言用**未 round 原始乘積**（abs<0.01；round(114.065,2)=114.06 會 FAIL）。`
- `verify/wd4_tier_list.py:89` — `（Python round(57.035,2)=57.03 之 banker's/float 刀口；MinA_區 114.07→½ 顯示 57.04）。`
- `verify/wd4_tier_list.py:90` — `判定式一律用 `2×ΣG ≥ MinA_區`（整數倍、無除法無二次 round），本值僅供顯示。"""`
- `verify/wf_f0.py:18` — `達標宗 = G_i ≥ MinA_blk 且無畸零旗標。`
- `verify/wf_f0.py:19` — `有達標宗 → 級0：標的=達標宗 G 最大者；被併=全部未達標宗。`
- `verify/wf_f0.py:20` — `無達標宗 → 級0'：標的=全格 G 最大者；被併=其餘。`
- `verify/wf_f0.py:22` — `合併後仍不達標＝標旗轉出（G009→F.2、G014→F.4；停機#4「下一級」＝§7 全鏈），不停機。`
- `verify/wf_f0.py:66` — `ROUTE_OUT = {"G009": "轉F.2(同歸戶R4有達標宗·級1相鄰街廓)",`
- `verify/wf_f0.py:67` — `"G014": "轉F.4(逃生門·2×G≥MinA_區·7-5≥½增配)"}`
- `verify/wf_f0.py:109` — `kind, target, merged = "全達標·無須併", None, []`
- `verify/wf_f0.py:228` — `f"改判『全達標·無須併』或該塊宗數<2）；確認係合法連動（如 M-5 提前合併）"`
- `verify/wf_f0.py:260` — `dest = ("達標·留置原位" if ok else ROUTE_OUT.get(d["gid"], "🔴無下一級·停機"))`
- `verify/wf_f2.py:24` — `停機：池落 (0,MinA)；G 迭代不收斂（run_step_g 內）；跨街廓守恆破；F.1 正交破（628-37(1) 變）。`
- `verify/wf_f2.py:146` — `raise RuntimeError(f"🔴 [{tag}] {gid} 無達標塊，不應在 F.2 名單（應 F.4）")`
- `verify/wf_f2.py:211` — `raise RuntimeError(f"🔴 [{tag}] 停機②：池落 (0,MinA) 開區間：{mid_state}")`
- `verify/wf_f3.py:171` — `raise RuntimeError(f"🔴 [{tag}] 停機：池落 (0,MinA)：{mid}")`
- `verify/wf_f3.py:185` — `"三則": ("歸零" if poolD[l] < 1 else "≥MinA")}`
- `verify/wf_f4.py:27` — `公設軌無原街廓→全塊，手冊(三)）；**Q3 禁超額**（配額＝max(G(a′),MinA)、增配＝max(0,MinA−G(a′))）；`
- `verify/wf_f4.py:30` — `- **E3**：純幾何等 G 重切＋前移（wf_f1 機制通用化任意塊×側；池總量不變）；整形後池落 (0,MinA)`
- `verify/wf_f4.py:83` — `E1_MARGIN = 5.0                        # E1 灌配保留餘裕：可達殘池 ≥ MinA+MARG（中央殘池寬>min_width，避浮點邊界）`
- `verify/wf_f4.py:213` — `呼叫端保證 target_G 距池牆 ≥MinA 級餘裕，G−area 殘差不會觸守恆閘）。回傳 a″。"""`
- `verify/wf_f4.py:249` — `（二者皆隨 a″ 單調增）。回傳 a″。裁示1(a)＋終極驗收＝合法可建築最小基地（非僅 area 達標）。"""`
- `verify/wf_f4.py:569` — `def _budget(blk):                            # 可灌量＝可達池 − 保留有效殘池(MinA+餘裕)`
- `verify/wf_f4.py:676` — `budget = _budget(blk)            # 可灌量＝可達池 − (MinA+餘裕)；rule3 保有效殘池`
- `verify/wf_f4.py:1050` — `公設軌無原街廓 → 全可建築塊（達標門檻用區標準、手冊(三)）。`
- `verify/wf_f4.py:1054` — `- **Q3＋裁示1(a)**：配額＝合法最小建築基地（寬≥min_width 且 G≥MinA）；增配＝max(0,該目標−G(a′))；`
- `verify/wf_f4.py:1218` — `for g in gids:                                        # commit 真最優（bisect 增配至 MinA）`
- `verify/wf_f4.py:1231` — `else:                                             # 增配至合法基地（寬≥min_width 且 G≥MinA）`
- `verify/wf_f4.py:1498` — `for pref, cat in (("F.0梯3", "F0釋池"), ("F.0全達標", "全達標"), ("F.0級0", "F0併"),`
- `verify/wf_f4.py:1515` — `("建地軌", "0"): {"F0併", "全達標", "F2跨併", "F3併入", "E0級1", "E2七五"},`
- `verify/wf_f4.py:1516` — `("建地軌", "1"): {"零動作", "F3併入", "全達標"},`
- `verify/wf_f4.py:1517` — `("建地軌", "2"): {"F3併入", "E0級1", "E2七五", "全達標"},`
- `verify/wf_f4.py:1532` — `chain[r["歸戶"]].append(f"F.0{r['級別']}→{r['去向']}" if r["級別"] != "全達標·無須併"`
- `verify/wf_f4.py:1533` — `else "F.0全達標·無須併")`
- `verify/wf_f4.py:1557` — `ch = ["零動作·達標留置"]`
- `verify/wf_f4.py:1560` — `if exp == ("建地軌", "1"):                    # 梯1 另須實測群內宗全達標`


---

## 🔴 更正附錄（claude.ai 2026-07-30 覆核·CC 復現）

### 一、識別字集漏 `wf_f0_mina`：278 → **282**

本體之 16 字集**未含 `wf_f0_mina`**。以原 16 字集於 `e583075` 重跑，**278 完全複現**
（⇒ 清單本體正確、可稽核）。補入 `wf_f0_mina` 後為 **282**，漏 4 點：

| 落點（`e583075`） | 於 `de64885` 之狀態 | 歸類 |
|---|---|---|
| `verify/run_verification.py:383`（`def wf_f0_mina`） | **仍活** | **B 逐街廓達標判定** |
| `verify/run_verification.py:568` | 已隨 M-5 區塊刪除 ⇒ 消滅 | — |
| `verify/probes/probe_ruling_N_e1_touch.py:448`（餵 `merge_subparcels_by_parent`） | **仍活** | **B 逐街廓達標判定** |
| `verify/probes/probe_ruling_K4_3_source.py:139` | 已封存至 `verify/archive/` ⇒ 死碼 | — |

**⇒ 停機條件甲之判定不受影響**：2 個仍活落點**皆可歸 B 類**，**無不可歸類點**。

### 二、CC 之復現（實測輸出）

```
新字集（17 字·補 wf_f0_mina）於 de64885 掃描合計 = 280
wf_f0_mina 命中：
   verify/archive/probe_ruling_K4_3_source.py:147  mina = rv.wf_f0_mina(ns, snap, cb_by)
   verify/probes/probe_ruling_N_e1_touch.py:448  rv.wf_f0_mina(ns, snapshot, cb_by),
   verify/run_verification.py:383  def wf_f0_mina(ns, snapshot, cb_by):
```
```
  verify/run_verification.py: e583075=16 de64885=14 Δ=-2
  de64885 現態 = 280；Δ(de64885−e583075) = -2；⇒ e583075 = 282
```
⇒ **`e583075 = 282` 復現無誤**；現態 280 之差 **全部**來自 `run_verification.py` 之 M-5 區塊刪除。

### 三、連動註記

本體 `:303` 引用之 `verify/wf_f0.py` 錯誤訊息原文（含「如 M-5 提前合併」）
**已於 `de64885+` 更新**——改指向 K-6 §二 段三／七級調配 F.0·F.2，並註明 M-5 已封存。
本體為 `e583075` 快照，**不隨之改**。

### 四、教訓（已入失敗考古 #33）

`wf_f0_mina` 是 `mina` 之**複合縮寫**；字集有 `_mina_by_block`／`mina_by_blk`／`mina[`
**卻獨漏它** ⇒ **N0-17-c 型**：**縮寫使 regex 瞎掉**，而「窮盡」宣稱正建立在該 regex 上。
