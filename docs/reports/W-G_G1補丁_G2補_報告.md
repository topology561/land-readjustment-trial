# W-G G.1 補丁（ctx 合約缺口）＋ G.2 補（濾 ghost／圍欄區段列）補丁報告

- 日期：2026-07-12；基準 HEAD 前＝`059418d`（G.2 收官）
- 觸發：KL 於 localhost 驗視活抓兩缺口——① G.1 live 停機（`f3_total_burden_rate_from_finance` 未鋪底）；② G.2 圍欄均價全綠卻區段漂移。

## 一、G.1 ctx-builder 合約缺口修（live 停機）

**停機事實**：真 app（localhost、非 harness）跑七級調配 → `run_step_g` 於 `f3_total_burden_rate_from_finance` 未鋪底時 **loud 停機**（stepg:171-176「須先 compute_total_burden_rate()、禁靜默退回 0.40」）。**閘正確咬合**——no-silent-fallback 之生產路徑首次兌現（記 failure-archaeology **#17 正面案例**）。

**根因**：harness 由 `build_pipeline`（run_verification:100-102）主動鋪底該率；真 app 無此鋪底路徑（僅財務分析 Tab 之 C 值流程會寫），使用者未點該 Tab → 鍵缺 → 引擎 loud。

**修法**（`_build_wf_ctx`，app.py，純加性）：組 shim 後**主動鋪底**——呼叫 harness 同一 `compute_total_burden_rate(_ns, list(cb_by.values()), snap_full)`（app 真符號 ns、β 快照 財務接線_v3 輸入），現算後寫入 shim.session_state。與 harness 同源同式、決定性（UC9898 錨 0.40712387）。**禁**要求先點某 Tab（#11 脆弱路徑）、**禁**靜默 0.40 fallback。

**閘補**（run_verification G.1 閘）：抹去 seed 之既有率值（複現 live 缺鍵）→ 呼叫 `_build_wf_ctx` → 斷言 shim 含 `f3_total_burden_rate_from_finance` 且 ==快照斷言錨 重劃總負擔率（0.40712387，|Δ|<1e-6）。閘名尾綴「/率鋪底」。

**smoke 補**：wg_g1/g2_smoke 於組 seed 後 `pop("f3_total_burden_rate_from_finance")`（複現 live 缺鍵）→ 證 `_build_wf_ctx` 主動鋪底、全鏈無崩。

### 全鏈 loud 前置鍵掃描結果（禁假設；別讓 KL 一鍵一鍵踩地雷）
掃 stepg/wf 全鏈「讀 session 鍵、缺則 raise」之點：
| 讀點 | 鍵 | 缺則 | 判定 |
|---|---|---|---|
| stepg:171 | `f3_total_burden_rate_from_finance` | **raise**（is None）| 🔴 **唯一缺口→本補丁鋪底** |
| stepg:207 | `f3_g_iter_params` | `.get({})` 無 raise | 自寫（setdefault@206）|
| stepg:194-205 | setback/alloc_depth/min_width/corner_winners/forced_offset/corner_min_table/manual_baseline | — | **run_step_g 自寫**（從 args）|
| stepg:328-451 | `f3_cad_front_lines/alloc_dir/side_lines_by_side` | `.get({})` 無 raise | live 有（Step G 寫）＋build_pipeline 鋪 |
| stepg:62/66/72/104/166 | 快照 財務接線_v3 值 | raise | β 快照凍結值恆有效（非 session 鍵）|
| wf_f0~f4 其餘 raise | — | 幾何/守恆計算失敗 | 非 session 前置鍵 |

**結論**：唯一 session-鍵-缺-即-raise 者＝`f3_total_burden_rate_from_finance`，本補丁已鋪；餘皆 run_step_g 自寫、`.get(default)`、或快照凍結值。

## 二、G.2 ① GIS 濾 ghost
`_wg_is_ghost(r)`＝列旗標 `_is_ghost_sliver` 或 幾何面積(㎡)≤0（**皆列既有值、非重算**，禁重算鐵律守）。套於 `_wg_gen_figure`／`_wg_theme_exit`／`_wg_theme_ledger` 三繪宗迴圈。ghost＝零面積虛編（app Step G **不**排 ghost、真面積已落池；harness stepg:230 排除）→ 真 app `v3` 代（gA=f3_G_values）帶 ghost、GIS 應濾。
> **驗證邊界**：smoke 之 gA＝`run_step_g` 產物（ghost 已於 stepg:230 排除）→ smoke 無 ghost 可濾、濾器於 smoke 為 no-op（10/10 PNG 無回歸）。濾器**效果域＝live gA**（app Step G 不排 ghost），reviewer 以邏輯核（旗標/零面積列值判定、三迴圈落點）證正確。

## 三、G.2 ② 誠實圍欄補區段級列（#11 家族新變體，記 failure-archaeology #16）
圍欄原僅比**均價**（重劃前/後平均地價）→ 均價層看不見 per-zone 漂移（區段間搬移不改總量→均價恆等、圍欄假全綠）。**補**：前區段 a/b 單價＋後街廓 R1-R6 六價**逐格並列**（快照 財務接線_v3 vs live `pre_zone_results`/`post_block_results`），漂移即 `⚠️ 漂移`。粒度對齊引擎（A 逐宗吃 per-zone/per-block 單價）。

## 四、驗收
| 項 | 結果 |
|---|---|
| py_compile（app/run_verification/兩 smoke）| ✅ |
| run_all | ✅ **155 ALL GREEN／0 FAIL**（G.1 閘＋率鋪底斷言、全代 baseline 零 diff）|
| G.1 smoke（率鍵 pop 後）| ✅ 全鏈跑通、ledger=33（證主動鋪底）|
| G.2 PNG smoke | ✅ 10/10 重出（ghost 濾生效）|
| 引擎/baseline/stepg/selection 觸動 | 零（本補丁純 app.py＋run_verification＋smoke＋failure-archaeology）|

## 五、③ 基準日（另令待辦）
KL：基準日裁定後「重烤或修鏈二擇一另令」——本補丁未涉，待裁。

## 六、failure-archaeology 兩記
- **#16**：圍欄比對粒度 < 引擎消費粒度（#11 家族；聚合均價掩蓋 per-zone 漂移）。
- **#17 正面案例**：no-silent-fallback loud 閘於生產路徑首次兌現（G.1 率鍵停機＝可見、非隱形錯值）。

## 七、上呈 KL（reviewer 逮之判斷層旗標，非本補丁引入、非阻擋）
1. **既有靜默 0.40 fallback 兩處（另路徑）**：`app.py:7666`（`_estimate_G_for_qualification`，街角 PK 資格 G估）與 `app.py:15232`（孤立公設 G）皆
   `st.session_state.get('f3_total_burden_rate_from_finance', 0.40) or 0.40`——**讀真 st、非本 shim**、且**不在 live wf_f0~f4 引擎路徑**（live 用預算 winners、引擎不重跑街角 PK）。
   潛在不一致：若使用者於財務分頁鋪底率**之前**跑街角 PK，winner 資格判定用 0.40，而引擎 G 解用 0.40712387。
   屬**既有行為**（非本補丁引入），是否修（同 stepg 廢 fallback 改 loud／或鋪底前禁跑 PK）＝**上呈 KL 裁**。本補丁已修正誤導註解（8017-8023：明標此二消費者讀真 st、非 shim）。
2. **ghost 濾器 live 生效未經 smoke 覆蓋**（見 §二驗證邊界）：harness gA 於 stepg:230 已排 ghost→smoke 為 no-op；效果域＝live gA。reviewer 附證：live g_rows 帶 `幾何面積(㎡)` 但**不帶** `_is_ghost_sliver`（旗標在原始 ghost dict、用底線 `幾何面積_m2`）→ 本濾器雙條件 OR 恰 belt-and-suspenders 涵蓋兩種列形（純顯示、無守恆風險）。
