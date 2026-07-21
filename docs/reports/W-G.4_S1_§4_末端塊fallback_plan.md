# W-G.4 S1 §4 末端塊 fallback 施工 plan（承 KL canonical 指令·送 reviewer）

- 日期：2026-07-21；branch `wip/s1-endpart`（**准紅碼**）；承 `445b18f`
- canonical 真相源：`docs/specs/W-G.4_規格v3補丁十_N0-20末端塊fallback定案.md` §一（KL 域＋claude.ai 規格）
- 依據：KL 指令 §二 A/B/C ＋ §三 柵欄 ＋ §四 靶；g-formula-rules（池重定位守恆）＋corner-selection-rules（winner 提末端位）
- 狀態：**plan·未動工**（[C] 已 held 於 working tree）。

---

## 0. 範圍（IN／OUT）

- **IN**：補丁十 §一 全部 ＋ §二 [A]/[B]/[C]。
- **OUT（勿動）**：`_build_corner_range_v2`／街角碼／§N2 名單／stepg 推進機（additive 除外）／F.0 錨 362.08（波末重烤）／`data/xlsx`／**R3 任何處理**（無未臨正街·不觸發）／D-右側 右端鏡像·probe R3 右段（作廢）。

---

## 1. [A] F.4 E3 末端塊機制形式化（生產碼·wf_f4）

### 1.1 新模組級純函式 `_end_region_R`（ns harvest·同 §3 `_corner_buffer_S` 先例）
```
_end_region_R(block_poly, d̂, end_pt, cad_alloc, min_width, frag_poly, _label)
  → {未臨正街: Polygon, 末端帶: Polygon, R_end: Polygon, area: float}
```
- **未臨正街「面積實體」＝ `frag_poly`**（＝`frag["poly"]`·`_poly_of` 之實際碎片·補丁十 §一「乙」）——**不用半平面構造**（半平面僅判別語意·approach §1 之 75.78 構造作廢）。
- **末端帶** ＝ 末端 ALLOCLINE 向街廓內 ⊥垂距平行帶（自 `end_pt`＝mp·W＝min_width·＝reviewer PASS 之 R6 166.57 式；`B` 由 block bounds 導·禁硬編 500）。
- `R_end ＝ frag_poly ∪ 末端帶`；`area ＝ R_end.area`。
- **缺 `cad_alloc` → loud raise**（同 `_corner_buffer_S`·no-silent-fallback）。**端別由 `frag["s"]` 定**（禁純幾何自偵）。

### 1.2 觸發／跳過（補丁十 §一 觸發條件·資料驅動）
- 於 `_reshape_block`（wf_f4:1096·側別已由 `frag["s"]` 定於 :1116）：該側末端邊 ∥ALLOCLINE（無未臨正街·如 R3）→ **乾淨跳過末端機制·不 raise**（R3 走現街角/§3 路徑·不觸本碼）。判準 ＝ 有 frag（frag 存在＝有未臨正街）。
- **禁硬編塊名/側別**——一律由 `frag`／`frag["s"]` 驅動。

### 1.3 勝者搜尋（補丁十 §一·§8-2 往後找·**複用現 target 搜尋·勿用 `_projection_order`**）
現 `_reshape_block` target 搜尋（wf_f4:1155-1161）＝`grp`（該側·累積S 序）首筆合格（S>0.01·寬≥mw·not flagged）。**改**：
1. **候選 ＝ 得以分配**（補丁十 §一）：`G ≥ 街廓最小分配面積`（＝`mina[blk]`·已入參；簡化式 分配後 W≥畸零寬＝現 `寬≥mw` 條件·對齊）。
2. **winner ＝ 首個 `G ≥ area(R_end)` 之合格候選·往後找**（現「首筆合格即取」→ 加 `G≥area(R_end)` 門檻·失則續搜下一合格·非嚴格首筆）。
3. winner 吃下整個 R_end（bisect ＝ 現 R1 逐字·`union(strip, wedge=frag).area==G_B`）並**提末端位**（現 `_reshape_block` 已將 target 整形吃 wedge＝提末端位語意·其餘內移）。
- **UC9898 diff=0（靶 a）**：R6/R1 winner G≫area(R_end)（R6 776.72≫252.28·R1 272.84≫115）→ 首筆合格即滿足 `G≥area(R_end)` → **選同現 target·終態不變**。門檻恆真·純加性。

### 1.4 無勝者 fallback（補丁十 §一·§8-1·現 :1162 raise → 改）
- 現 `target_row is None → raise`（:1162-1163）**擴為**：`target_row is None`（無合格候選）**或** 全合格候選 `G<area(R_end)`（往後找窮盡）→ **無 winner**。
- 無 winner → **抵費地(末) 嚴格 ＝ area(R_end)**（R_end 整塊成抵費地·佔末端位·末端-跨占地依原序內移）。**非 raise**。
- **degenerate/新失敗面**（`_end_region_R` 退化·缺 cad_alloc）→ loud raise·但**winner 路徑純加性**（fallback 判定僅消費 area·不打紅現行綠 winner 案·靶 c）。

### 1.5 合成夾具（UC9898 fallback latent·無案例）
- 建合成 fixture（`verify/` 下·同 #15 latent 分支法）：構造「全合格候選 G<area(R_end)」逼 fallback 分支·驗 抵費地(末)＝area(R_end)＋守恆（[B]）。UC9898 不觸發·此為 fallback 唯一驗路。

---

## 2. [B] 末端 fallback 池重定位守恆（補丁十 §一·§8-1 甲）

- **原理**（g-formula-rules 鎖）：抵費地(末) ＝ **池面積重定位到末端·非額外面積、非從建地扣**；建地拿足 G·不前移；**ΣG ＋ 池 ＝ 街廓 恆成立**。
- **F.4 E3 落點**：E3 池帳（wf_f4:705-721·現 `pool_final[blk]=poolE[blk]`）——fallback 觸發時 `中央池 ＝ 街廓 − ΣG(全宗) − 抵費地(第1宗/街角) − 抵費地(末)`；抵費地(末)＝area(R_end) 自池重定位（池減 area(R_end)·非新增面積）。
- **守恆閘**：E3 帳對幾何閘（wf_f4:716·`_acct_geom_tol_block`）於觸發街廓須 PASS（ΣG＋池＝街廓·靶 b）。
- **WATCH 界（KL 授權 CC 自理分界）**：角落側 app-path 池重定位**已接線**（`app.py:14622`·W-D.2 §3 M3·`_spatial_order_parcels_v2`→corner_offset_area→Step G ledger·非「恆餵 0」——g-formula-rules 技能記述已過期）。**本波僅接末端側之 F.4 E3 守恆**；app-path 角落側**已完成·標 WATCH（驗證其與末端側同源·不重寫）**。

---

## 3. [C] §3 帳對閘註解／訊息（zero-behavior·已 held）

- `wf_f4:709-720` 註解＋raise 訊息已改 `整形宗數 × 0.005`（S0d 後 `_acct_geom_tol_per_lot(depth,False)＝_G_ROUND_HALF＝0.005`·深度項歸零·`app.py:6808-6826` 坐實）·py_compile OK·**held working tree**。隨本波 commit+push（准紅碼）。

---

## 4. 驗證（§四·走 harness／直讀 baselines·**非 run_all 全綠**）

- **靶 a**：UC9898 winner 路徑終態 **diff=0**——直讀 `verify/baselines/wf/f4/`（整形檔 S_new 不變·R6 628-4(1)/R1 winner G≫area(R_end)）。
- **靶 b**：觸發街廓守恆 ΣG＋池＝街廓——合成夾具 + E3 帳對閘 PASS。
- **靶 c**：幾何閘不因新碼誤紅現行綠案——`_end_region_R` degenerate loud raise 僅 fallback 判定消費·winner 純加性。
- **run_all F.0 紅（G007 359.43≠362.08）＝過期錨·預期·勿追**（准紅碼·波末重烤處理）；驗「無**新**破（本碼所致）」而非「全綠」。
- **no-silent-fallback**：缺 cad_alloc／退化 loud raise。

---

## 5. 停機條件（僅此三類上呈·白話）
不變量破 / J 下降 / 守恆破 或 撞新域邊界／規格缺口。純技術一路 plan→reviewer→施工→push。

## 6. 送 reviewer 之問
1. **UC9898 diff=0（最重）**：加 `G≥area(R_end)` 門檻＋往後找·是否確保 R6/R1 選同現 target（首筆合格 G≫area(R_end)）→終態不變？直讀 baseline 佐證。
2. **fallback 守恆**：抵費地(末)＝area(R_end) 之池重定位·`中央池＝街廓−ΣG−抵費地(第1宗)−抵費地(末)`·E3 帳對閘是否守？合成夾具設計。
3. **範圍圍欄**：確無觸 R3/街角碼/`_build_corner_range_v2`/F.0 錨/xlsx？`_end_region_R` 未臨正街用 frag（非半平面構造·補丁十乙）？
4. **[B] WATCH 界**：角落側 app-path（14622）確已接線（非恆餵 0）？本波只接末端側·是否合理分界？
