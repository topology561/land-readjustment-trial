# baselines v2 出處（PROVENANCE）— W-D.2 滑池槽三表

> v1（街角 PK 10 CSV）維持不動、閘門照舊；本目錄＝W-D.2 新診斷之 v2 準源轉正。

## 產出資訊

- **產出者**：KL（Streamlit UI 實跑；claude.ai 逐塊算術複判收案、裁定為準源）。
- **產出日期**：2026-07-06（「史上第一輪雙參數皆正確」輪：快照地價＋步驟 E 路況照正典）。
- **當時 app.py commit**：`3662c63`（W-D.2 P1-P5＋J-fix 之後）。
- **檔案**：G 值計算結果／W-D.2 §3 滑池槽診斷／逐槽 J 表 × 退縮{0m, 3.5m} 共 6 CSV。
- **對拍**：`verify/stepg_pipeline.py`（Step G headless）雙情境 cell-exact（run_all v2 段）。

## 參數身分（快照 `case_params_UC9898.json` 為單一真相源）

- 路況：`blocks.*.負擔尺度_輸入` 逐塊逐側（R1/R4 正面 12m 既成→尺度 0；其餘正面 8m
  新闢→2；有 SIDE_LINE 側 8m 新闢→1）。harness 條件①斷言 calc 尺度==輸入。
- 深度＝`街廓分配深度_m`；全區財務＝`財務接線_全區_步驟F`；B＝calc_B_value 現算
  （公設共同負擔 12,146.56㎡−抵充 0−臨街特別負擔）。
- **財務半中間態（快照 `StepG_v2_中間態`）**：Tab7 未跑→**C=0**（app 顯式警告路徑）、
  Tab5 區段未指派→**A 地價比=1**。非域終值；財務接線波升 v3 時本目錄整批升版、
  G 值合法變動（糾正波尺標）。
- **J 單位＝負擔面積㎡**（Rw 比率×F×l₁；KL 量級裁示，R2 全飽和≈44.95）。
- 守恆 ledger：角落抵費地＝range 規劃值**拆帳呈示**（池重定位、非新增面積）；
  「幾何片明細/片數」欄＝ledger vs 實際切片對照（KL 條件④，拆帳位移非漏帳）。

## [H-ghost]：已決（consistent，追碼可證，不升版）— KL 逐碼裁定 2026-07-06

CC 上呈時為黑箱假說，KL pull `5d24519` 逐碼裁定、CC 複核追至根本機制：

1. **ghost 天生零面積**：overlay（`overlay_polygons_to_blocks`，app＝harness 共用同一
   AST 抽出函式）之 UNC 殘料判定（`BOUNDARY_BAND_M=2.0`／`UNC_AREA_MIN=50.0`，
   ~app.py 4160-4179）把邊界帶碎屑標 `_is_ghost_sliver=True` 且 `幾何面積_m2=0`、
   `面積_m2=0`——真面積另存 `_ghost_area_m2`（已合至主體/落池）＝**零面積視覺列**。
2. **等價無條件**：因 ghost 零面積，生不生成、排不排除，`G/ΣRw/守恆/J/池` 全不變。
   守恆 <1㎡ 本就不含 ghost 面積（真面積落幾何剩餘、進池、計一次——R1 那 5.28㎡ ＝
   呈為 `R1-抵費地-2=5.3` 的同一片；R4 8.09㎡ 併入 640.68 池）。此即不升版之硬核。
3. **主因＝H-a 輸入差（CC 追碼精確化，KL 散文之「E-0.4 排除」修正）**：
   - E-0.4 排除點（`_allocate_three_tier_v1`，app.py 6745/6873）屬**三層調配**
     （W-E/W-F 階段，Step G **之後**）——**不是** Step G 前。
   - app 的 Step G（`build_parcels` 13545／`parcels_by_block` 14663）**皆不排除** ghost；
     R1/R4 邊界帶 ghost 街廓分類=住宅區 → 會進 build_parcels。故某輪 overlay 若生
     R1/R4 住宅 ghost，**app 的 Step G 亦會產零面積 `_GHOST` 列**（與 harness 未過濾前同）。
   - KL 準源輪六表**無** `_GHOST` 列 ⟹ **該輪 overlay 未生 R1/R4 住宅 ghost**
     （live DXF 精度／shapely 版本 vs repo V6.dxf 輸入差，未觸發邊界帶判定）。
     harness 輪（repo V6.dxf）生了 R1/R4 兩個零面積 ghost → `stepg_pipeline.py` 之
     `_is_ghost_sliver` 過濾對齊 KL 輪之無-ghost 狀態。
   - **故 harness 過濾之正當性＝「對齊 KL 輪＋零面積無條件安全」**（非「E-0.4 忠實移位」——
     app Step G 實不排除）。Step C 畫面 👻 計數對 KL 輪**預期 N=0**（確認性，非閘；
     即便 live 版本某輪 N>0，因零面積 v2 數字不動）。

**裁定**：consistent，收案，不升版。v2 三件套轉正生效、W-D.2 全線收官。

## backlog（穩健性，非本波、非 v2 阻擋；KL 2026-07-06 裁交下波）

- **ghost 零面積不變量斷言**：harness（overlay 後）若標記任何 `_is_ghost_sliver`，
  斷言其 `幾何面積_m2==0 且 面積_m2==0`（破＝零面積性質被 refactor 破壞＝真發散源，
  比「集合相等」更抓根本——因 app Step G 不排除 ghost，等價全靠零面積）。附記
  「app Step G 不排除 ghost、harness `stepg` 過濾為對齊 KL 輪」之事實，釘成可證等價。
  下波（W-D.3 或清理波）落地。

## W-D.3 診斷波追加（2026-07-06；診斷波，零幾何移動）

- **wd3_fragment_geom.csv／wd3_fragment_edges.csv**（本目錄）＝碎片三分類＋逐邊 CAD 分類 baseline，
  由 `verify/wd3_fragment_geom.py`（常設準源方法）產、run_all 逐格對拍。geom 之
  面積/沿街s/長寬比/緊湊度 錨定 `c1584a8` 附錄A（自檢 CLAIMED）；三分類/宗地寬度/深度/(a)(b)(c)
  為 W-D.3 新增診斷欄（harness 定義、git 錨定、byte-identical 凍結為回歸閘）。
- **三分類判準（KL 定稿）**：碎片＝(a)S=0 或 (b)宗地寬度<法定最小寬 或 (c)深度<法定最小深；
  面積門檻全廢（舊 Q3「法定最小分配面積」為 claude.ai 裁示錯誤、已更正）。面積+三候選值＝參考。
- **ghost 零面積不變量斷言**（run_all 常設）：任一 `_is_ghost_sliver` 面積≠0 → harness
  RuntimeError／app 純加性 warn（[H-ghost] H-a 等價之根基＝零面積）。
- **零幾何移動之證**：run_all 既有 18 閘（幾何半/選位半/Step G v2 三表）全程綠＝
  G/守恆/位次/J/k* 逐格未動；W-D.3 僅加診斷欄/分類/新對拍閘/app 純加性 warn。
- **WARNING-2 backlog（硬期限 W-D.4 開工前）**：min_width 查表硬編「住宅區」，須改吃真實 category。
