# W-G.4 規格 v3 補丁十：N0-20 末端塊 fallback 定案（canonical ground truth）

- 日期：2026-07-21；源＝**KL 域裁 ＋ claude.ai 規格裁定**（S1 §4 末端塊 fallback 指令·逐字入倉為 reviewer/施工唯一真相源）。
- 效力：關閉 approach `W-G.4_S1_§4_N0-20_approach.md` §7/§8 之待裁三題（§8-1 守恆歸屬＝甲·§8-2 搜尋語意＝往後找）＋ D-右側 上呈（作廢·見下 §0）＋ 未臨正街面積源（＝實際 frag·乙）。施工一律以本補丁 §一 為準。

---

## 0. 兩則舊上呈之更正（勿據其行動）

- **[0-1] xlsx 上呈（`445b18f`）＝誤判**：committed xlsx（blob `80f75ee`·12.38MB）完好、整波未變；`run_all` 之 F.0 紅「G007 359.43≠錨 362.08」係**過期錨**（錨 362.08 由 `0c9b7e7`·07-17「不動錨」設；W脫鉤 07-19 ＋ S0d 07-20 之後改了 G 的 W／S 輸入項 → **359.43 是預期新值**）。**非資料壞、非 regression、非施工可致。勿動 `data/xlsx`、勿追此紅。** 錨待波末重烤（含 KL UI 錨）更新。
- **[0-2] D-右側 上呈＝掛錯波次**：R3 末端邊(D→E) **∥ALLOCLINE（實測 0.00°）→ R3 無未臨正街**；R3-右 78.24 係**街角(§3)碎片**、production 已用實際碎片正確處理。**D-右側 從 §4 剔除**：不補末端右端鏡像、作廢 probe 之 R3 右鏡像整段、不改任何街角碼。

---

## 一、域裁＋規格裁定（canonical·施工一律以此為準）

### 【觸發條件】（claude.ai 定稿·文字收緊防再誤讀）
末端塊機制僅於某側**二條件皆真**時觸發（缺一即跳過·**不 raise**）：
- **條件1（無 SIDELINE 那側）**：該側 `forced_offset['left/right_has_side']==False`（資料驅動）。
- **條件2（該側有未臨正街）**：該側 `block∩{s<0}` 半平面面積 `> ε`（＝補丁七 §一.1 **判別語意**；末端邊∥ALLOCLINE ⇒ ≈0 ⇒ 無·如 R3 末端側）。
- **釐清（防再誤摘）**：未臨正街之「存在」由**半平面判別**、**非「有 frag」**——街角側亦有 frag（如 R3 街角 78.24）會誤觸；`frag` 僅供**已確認存在**之未臨正街的**面積**（「半平面僅判別、不供面積」）。皆資料驅動·**禁硬編塊名／側別**。

### 【R_end 構造】
`R_end ＝ 未臨正街 ∪ 末端帶`。
- **未臨正街「面積實體」＝實際碎片 `frag["poly"]`**（`wf_f1 _poly_of`·＝production 所用者）；補丁七 §一.1 半平面（`block∩{s<0}`）**僅為判別語意、不供面積**（claude.ai 規格裁定）。
- **末端帶** ＝ 末端 ALLOCLINE 向街廓內平移「畸零寬」之 **⊥垂距平行帶**（自 mp 量·W＝S＝畸零寬；已 reviewer PASS·R6 166.57）。
- **側別／端別源 ＝ `frag["s"]`／`推進側別`**（＝production 同源·資料驅動），**禁純幾何自偵**（R1 兩端皆非零會誤判）。

### 【候選＋得以分配門檻】
候選 ＝「**跨占 R_end range 且得以分配**」之重劃前土地，依**投影序（末端側→內）**。
- **得以分配** ＝ 應分配 G ≥ 街廓最小分配面積（＝畸零寬 × 實際分配深度；若各段深度皆 > 畸零最小深度，簡化為分配後 W ≥ 畸零寬）。
- **中間宗 W** ＝「本宗與前宗之宗地分配線中點」⊥量至「本宗與下宗之宗地分配線」（＝W 脫鉤量法）。

### 【勝者（§8-2 ＝ 往後找）】
勝者 ＝ 投影序中**第一個 G ≥ area(R_end) 者**；前面吃不下就往後找（**非嚴格首筆**）。
- 勝者吃下整個 R_end（未臨正街＋末端帶），並**被提到末端位**（與街角第 1 宗同機制）；其餘末端-跨占候選依原相對序排其內側。
- （承 §4 三裁③：winner 需 **合格〔臨正街＋符畸零寬·補丁七 §二.4〕且 G ≥ area(R_end)**。）

### 【無勝者 fallback（§8-1 ＝ 甲·池重定位）】
候選全部 G < area(R_end) → 末端塊整塊 ＝ **抵費地(末)**，面積嚴格 ＝ `area(R_end)`，佔末端位；末端-跨占地依原序排其內側。
- **面積歸屬**：抵費地(末) ＝ **該街廓池面積重定位到末端**（**非額外面積、非從建地扣**）；建地各拿足 G、**不前移**；**守恆 ΣG ＋ 池 ＝ 街廓 恆成立**。
- 中間調配池 ＝ `街廓 − ΣG(全宗) − 抵費地(第1宗/街角) − 抵費地(末)`。
- （＝ g-formula 技能已鎖「**角落抵費地＝池面積重定位、非額外面積**」之同一原理，套到末端側。）

---

## 二、施工落點（承指令 §二·詳見 plan `W-G.4_S1_§4_末端塊fallback_plan.md`）

- **[A]** F.4 E3 末端塊形式化：新模組級純函式 `_end_region_R(block, d̂, p1, cad_alloc, min_width, _label)`（`_pool_strips_for_block` 鄰·ns harvest·同 §3 `_corner_buffer_S` 先例）；勝者搜尋**複用 `_reshape_block` target 搜尋**（wf_f4 ~1155-1161·**勿複用 `_projection_order`**）＋得以分配濾＋G≥area(R_end)＋往後找；無勝者→抵費地(末)嚴格＝area(R_end)。wf_f1 R3/R6 標記制係下游死路（F.4 讀 f0/trunk-E·不讀 f1）→通式落 F.4 E3。degenerate loud raise 勿打紅現行綠 winner 案。
- **[B]** 池重定位守恆：末端 抵費地(末) ＝ 池重定位（ΣG＋池＝街廓）。角落側 app path 已接線（`app.py:14622`·W-D.2 §3 M3·`_spatial_order_parcels_v2`→corner_offset_area→Step G ledger）→ **本波僅接末端側之 F.4 E3 守恆**，app-path 角落側標 WATCH（見 plan §B）。
- **[C]** §3 帳對閘註解／訊息小修（zero-behavior·S0d 後 `_acct_geom_tol_per_lot(depth,False)＝0.005`·深度項歸零）——已 held（`wf_f4:709-720`）·隨本波 push。

## 三、範圍柵欄（OUT·勿動）
`_build_corner_range_v2`（§3 range 源）／街角碼／§N2 名單／stepg 推進機（additive 除外）／F.0 錨（362.08 六格·波末重烤）／`data/xlsx`／**R3 任何處理**（R3 無未臨正街·不觸發）／D-右側 右端鏡像·probe R3 右段（作廢）。

## 四、正確性靶（§四）
(a) **UC9898 winner 路徑終態 diff＝0 不變**（R6/R1 winner G≫area(R_end)·fallback latent·不觸發）；(b) 守恆 ΣG＋池＝街廓 於觸發街廓成立；(c) 幾何閘不因新碼誤紅現行綠案。驗證走 harness／直讀 `verify/baselines/wf/f4/`（G值檔 S＝S_E·整形檔 S_new）；**no-silent-fallback**（缺值 loud raise）。

> **本補丁 §一 ＝ canonical spec anchor（KL 域＋claude.ai 規格）·施工／reviewer 唯一真相源。**
