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

## ⚠️ 未決事項（上呈中，不擋 v2）

- **[H-ghost]**：本輪 app 實跑之 Step G **無 `_GHOST` 邊界帶殘塊列**（如 R1 之 5.28㎡
  區域呈為 `R1-抵費地-2=5.3` 幾何剩餘），而 harness 標準管線之 overlay 會產出該類
  ghost 暫編。harness 以「排除 `_is_ghost_sliver`」為**對拍假說**重現本輪（全綠）。
  「app 該輪為何無 ghost」待 KL 看 Step C 畫面 👻 計數／claude.ai 追碼裁定後，
  假說轉正或改判（若改判＝v2 升版事由）。
