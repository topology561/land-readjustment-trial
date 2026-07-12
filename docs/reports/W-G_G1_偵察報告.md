# W-G G.1 偵察報告：§7 引擎接線之 ctx 合約 vs app live session_state

- 波次：W-G 子波 G.1（§7 引擎接線）
- 日期：2026-07-12
- 性質：**偵察上呈**（禁假設）。交付＝ctx 合約盤點＋**注入映射表（plan 必審件）**＋缺口分析。
- **本報告不含實作**。映射表須經審＋兩項架構裁定後方施工（見七）。
- 證據等級：引擎側 CC 逐檔讀碼；app 側 general-purpose agent 逐行驗證，CC 抽驗 4 項承載主張全中（gA@14999、34949.888 無 live 源、均價成熟度覆寫、build_parcels local）。

## 一、引擎入口與 trunk 鏈（run_verification.py 呼叫點）
- `wf_f0.compute(ctx_by_tag)`→f0；`wf_f1.compute(ctx,f0)`；`wf_f2.compute(ctx,f0)`→f2；`wf_f3.compute(ctx,f2)`→f3；`wf_f4.compute(ctx,f0,f2,f3)`→終態。
- 鏈式依賴：f0→(f1,f2)；f2→f3；{f0,f2,f3}→f4。app 接線須按序串接。
- `ctx_by_tag={tag:ctx}`，tag＝退縮情境。app 單情境→單 tag。

## 二、核心機制——**「禁 fork」成立、無引擎改動需求**
1. **ns＝app 模組符號**：引擎經 ns 呼叫 **13 個 app.py 真函式/常數**（`calc_B_value/calc_C_value/calc_special_burden_total/solve_G_binary/iterate_G_S/rw_from_width/get_min_lot_size/_select_pool_slot/_projection_order/_spatial_order_parcels_v2/alloc_normal_axis/_block_strip/F3_CATEGORY_BURDEN`）。**全在 app.py** → app 傳 `globals()` 即可、跑 app 真函式、零 fork。
2. **fake_st＝streamlit shim**：app 傳真 `st`（或曝 `st.session_state` 之 shim）。`run_step_g` 寫 7 Step-G 輸入鍵（`f3L_setback_default/f3_alloc_depth_by_label/f3_min_width_by_label/f3_corner_winners/f3L_forced_offset/f3L_corner_min_table/f3_manual_baseline`），in-app 寫真 session（callback 內合法）。
3. **run_step_g（stepg_pipeline）＝harness 編排器**：呼叫 app 真公式（ns），但**財務輸入由 snapshot 重建**（`snap["財務接線_v3"]/["blocks"]`）→ app 須組出 snapshot 形狀之 `ctx["snap"]`（見五）。
4. **匯入零副作用**：run_verification 有 `__main__` guard、模組級零執行；wf 零用 `rv.*`。app `import wf_f0` 安全。

## 三、【重大發現】引擎為 UC9898-凍結（設計如此，非缺陷）
- **67 個 `raise RuntimeError` 斷言**（f0:4 / f1:15 / f2:5 / f3:3 / f4:40），多繫 UC9898 硬寫錨：
  `GSA_EXPECT`（六格 G(Σa)）、`WEDGE_AREA_ANCHOR=5.30`、`SNAP_WAVG=72058.60964443642`（wf_f4:86 `|w−SNAP_WAVG|>1e-6→raise`）、
  `TIER3_LOTS/STRADDLE/E0_EXPECT/TARGET_ANCHOR/F1_TARGET`（硬寫暫編地號 628-37(1) 等）、`MINA_QU=114.07`、`COMP_EXPECT`。
- **意涵**：live-inject **UC9898** session_state → 錨吻合、正常跑（錨＝護欄，保證複現法定終態）。餵**任何非 UC9898** → 斷言 `raise`（引擎＝凍結真相，不為別案妥協）。
- **精度耦合**：即使 UC9898，若 `ctx["snap"]` 財務值不逐位複現快照（如 SNAP_WAVG 1e-6、B/C 錨 round6），斷言即 trip。

## 四、注入映射表（欄位級；app 側逐行驗證）
**可直接接線（✅，無缺口）**

| ctx 欄 | app live 來源（鍵＠行） | 結構要點 |
|---|---|---|
| gA | `f3_G_values` ＠14999 | list[dict]；`推進側別`∈{left,right,抵費地,孤立公設地,現金補償}；含 G(㎡)/a 面積(㎡) |
| winners | `f3_corner_winners` ＠13499 | {label:{p1_end,p2_end,method}}；**p1_end/p2_end 鍵與引擎精確吻合** |
| forced | `f3L_forced_offset` ＠13530 | {label:{left/right_forced_offset,left/right_has_side,left/right_corner_min_area}} |
| params | `f3L_corner_min_table` ＠13222 | list[{街廓,分類,正面路寬,左/右路寬,街廓分配深度,法定最小寬/深,左/右截角,左/右街角最小面積}] |
| temp | `f3_temp_parcels` ＠11287 | list[dict]；四欄面積唯讀＋polygon_coords＋_is_ghost_sliver |
| omap | `t8_ownership_map` ＠10555 | dict 歸戶 |
| poolA | `f3_wd2_pool_diag` ＠14148/14808 | {label:{k*,J,ΣRw,ΣG,池總…}} |
| p1/p2 | `f3_cad_front_lines` ＠11463 | **引擎讀 cad.front_lines，非 snap.blocks**；{p1,p2,angle_deg,length} |
| 單位工程/拆遷/行政費 | `b_cost/k_cost/c_cost`（_read_persisted ＠9340-9342） | 元/㎡ |
| 抵充地/已徵收公設 | `f3_offset_area/f3_preexisting_public` ＠12793/12792 | m² |
| 前均價 | `pre_land_price_sqm` ＠8799 | **全精度**存檔 |
| 截角/深度/最小寬/MinA | `f3L_corner_min_table` / `f3_alloc_depth_by_label`＠13053 / `f3_min_width_by_label`＠13055 / `f3_min_alloc_area_by_label`＠13054 | dict{label:float} |

**需 app 端組裝（⚠️，接線層工作，非引擎改）**

| ctx 欄 | 現況 | 組裝 |
|---|---|---|
| cb_by | `f3_classified_blocks` 為 **list**＠11089 | 轉 `{b['label']:b}` dict |
| cad | 散在 **7 鍵** `f3_cad_*`＠11460-11475 | 組回引擎單一 `cad` dict（front_lengths/side_lengths_by_side/front_lines/side_lines_by_side/alloc_dir_by_block） |
| build | **local 變數** ＠12937（未入 session） | Step G 後同幀擷取，或加一行寫 session |
| 負擔尺度_輸入/期望長度/期望負擔面積 | **`sb['rows']` local**（Step H ＠12827，`calc_special_burden_total` 現算） | 擷取 sb['rows']（正/左/右尺度＝4377-4381），或寫 session |
| 後街廓/前區段_面積單價 | `post_block_results`＠9160 / `pre_zone_results`＠9265 為 **list**，單價全精度 | 轉 `{R1..R6:{面積_m2,單價_元每m2,相對比率_pct}}`／`{a,b}`；**街廓名須 R1..R6、區段名須 a/b** |
| 原地號_區段 | `f3_parcel_zones`＠11824 keyed by 原地號 | 區段名為使用者 Step D 標記（預設「甲段」）→ **需名稱映射 a/b** |
| setback+街角最小面積{0,3.5} | 單 setback（`f3L_setback_default`＠12981） | 快照雙情境須**切換 setback 各跑一次** |

## 五、【缺口熱區】ctx["snap"] 財務精度——app live 無法逐位複現 KL 授權凍結值
| snap 欄 | 快照值（KL 授權） | app live | 判定 |
|---|---|---|---|
| `重劃區總面積_m2_精確` | **34949.888**（＝工程費122324608÷單位費3500 反推） | `total_area_t5`＝Σ面積≈34950（8989）／`f3_total_area` number_input；**無反推源** | 🔴 **缺口**：app 之工程費＝單位費×總面積（循環），無 KL 獨立工程費 122324608 → 無 34949.888 |
| `貸款利息_元` | **5011064**（KL Tab7 精確元） | `total_interest`（NPV，萬元 round2）×10000≈百元精度（9789） | ⚠️ 模型/精度不同源（差 64 元） |
| `重劃後平均地價` | **72058.60964…**（純 60/40 blend） | `weighted_price_sqm`（8493，全精度 blend）**但成熟度折現開啟時被覆寫為特定價格**（8469 `enable_maturity`，預設關） | ⚠️ 需確認成熟度關；未折現值無獨立 session 鍵 |

> 耦合三之精度斷言：`SNAP_WAVG`(1e-6)、B/C 錨(round6)、GSA_EXPECT(0.01)。上列精度差 → 斷言 trip → 「七級調配」區 `raise`。

## 六、缺口分類（是否需改引擎＝停機？）——**均不需改引擎**
- ⚠️ 組裝類（cb_by/cad/build/sb/後街廓/區段/setback）：**app 接線層工作**，無引擎改。
- 🔴 財務精度（34949.888/利息/均價）：可由**方案 β**（載快照 `財務接線_v3`）解，無引擎改、無邏輯 fork（僅輸入來源）。
- **無「需改引擎側」硬停機**。惟涉兩項**規格缺口**須裁（見七）→ 依鐵律 G.1 偵察上呈、裁後施工。

## 七、上呈裁定（兩項；施工前必答）
**裁定 1（範圍）**：引擎 UC9898-凍結（67 斷言）。G.1「七級調配」live 接線之範圍是否＝**UC9898 複現**（對齊 G.3「同快照參數下」對拍）、通用化（去錨）列未來波/禁為 UI 妥協？
- CC 建議：**是，範圍＝UC9898 複現**。非 UC9898 資料時該區以旗標告知「§7 引擎為凍結法定真相、僅適用本案」，不硬跑觸斷言。

**裁定 2（財務 ctx 來源）**：app live 財務值無法逐位複現快照 KL 授權精度（34949.888 反推、利息元值、純 blend 均價）。三案：
- (α) 純 live 財務 → 引擎 67 斷言 trip → 崩。需 app 新增 KL 獨立財務輸入（大改、複現不確定）。
- (β) **混源**：live 幾何/宗地/Step-G 輸出 ＋ 快照 `財務接線_v3`（載 `case_params_UC9898.json`）為財務 ctx。引擎斷言過、複現 baseline、對齊 G.3「同快照參數下」；**非引擎改、非邏輯 fork**（僅輸入來源）。
- (γ) 去引擎錨 → **禁**（引擎為 UI 妥協）。
- CC 建議：**β**。純 live 財務精度另立「app 財務精度波」，不在 G.1。

**停機**：本報告即 G.1 偵察上呈。裁定 1、2 未定 → **不施工**（映射表為 plan 必審件，須連同裁定核可）。

## 八、裁後施工預告（僅供判讀，未動工）
app 新「七級調配」區（Step G 後）：組 ctx（§四映射＋§七裁定之財務來源）→ 依序 wf_f0→f4 → 呈池/碎片/整形/雙出口/33群；意思決定項（合議/§53-2放棄/增配>0/拆單）照旗標呈現不自動裁。驗收：run_all 154 全綠＋wf/f4 baseline 逐格零 diff＋app smoke 證據入倉。G.3 雙路同源終驗留該子波。
