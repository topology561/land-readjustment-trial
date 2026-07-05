# W-V 驗證熔爐（verify/）

headless 重現 `app.py` 的街角地優先權選位管線，雙情境（退縮 0m / 3.5m），逐格對拍
`verify/baselines/`，作為「app 忠實重現」的回歸閘。**additive-only：`app.py` 一字不改。**

## 為何不 import app.py
`app.py` 是 Streamlit 單檔（模組級即跑 UI script、含 `st.set_page_config`），直接 import 會炸。
`app_harvest.py` 以 **AST 過濾**只留 top-level `def`/`class`/常數、跳過模組級 UI 語句，再注入
**fake streamlit** 後 exec → 取得 app.py 的**真函式**活命名空間（非複本）。手冊圖8 golden
在此命名空間下仍成立，即證 harvest 出的與 app 同一份函式。

## 執行
```
python verify/run_all.py          # golden ＋ 雙情境對拍，exit 0＝全綠
python verify/run_verification.py # 僅對拍
python tests/test_corner_priority_golden.py  # 僅 golden
```

## 快照（case_params_UC9898.json）
harness **禁吃 UI 預設**，一律載本快照（KL 域裁示、lock 2026-07-04）。一案一快照為日後標準。
關鍵值：R1/R4 正面路寬=12m（既成、正街尺度0）、重劃總負擔率=0.40（Tab7 未跑 fallback、baseline 反解）。

## 對拍鍵 doctrine（務必遵守；KL 2026-07-04 更正）
- **主鍵＝宗地地號＋持分結構**（縱深防禦，不變）。
- **歸戶群組編號 Gxxx＝逐一相同之預期**（更正前「依姓名筆劃重排」有誤，以追碼為準）：app tab1
  群組號按**宗地迭代序（dict 插入序）**配發、作業原則「以筆劃」app 未實作、匿名化未動列序
  → 迭代序不變 → **Gxxx 應全同**。
- 故 diff 引擎對 Gxxx＝**比對但列警告級**：若真不同，**不得正規化吃掉**，那本身即訊號
  （迭代序某處變了）→ 交 B6 仲裁。完全忽略 Gxxx 反而會藏掉真的迭代序 bug。
- **Gxxx 全等成立鏈（定理，diverge 時反查斷點）**：匿名化保留列序 → 指紋劃分同構（已證
  21,476 群）→ 群組**首次出現序**不變 → **Gxxx 逐一相同**。故 baseline 靶組
  **G005/G007/G009/G019/G023/G029**（628-18/628-45/628/628-37/628-41/628-36）driver 在匿名資料上
  **必原樣重現**；若 Gxxx 錯位，三環必斷其一：①列序被動過 ②指紋複刻偏差 ③**迭代起點不同**
  （如 driver 從 U_LAND 而非**重劃區地籍**起迭代——這是最可能的坑）。

## diff 引擎自檢（run_all 常設；KL 2026-07-05 裁示）
`run_all.py` 階段 [2/3] 每跑必先自檢：竄改 診斷0m baseline 副本（改值×2＋缺列×1）→
閘門必須咬出**恰 3** violation；`_classify_gxxx` 分流必須（Gxxx-only→警告級、實質差→hard）。
自檢不過 → 對拍結果不可信、直接 FAIL。目的：證「綠」非虛（防 diff 引擎自身壞掉造成假綠）。

## 已知缺口（記載待修；修復屬 UI/接線波，非 harness 範圍）
- **法定最小寬 3.5 恆走預設**：`f3L_sb_rows_by_label` 全 app 無人寫入 → v12 內法定最小寬
  恆 3.5。畸零地最小寬/深正典＝**二維查表：使用分區 × 面臨道路寬度**（花蓮縣畸零地使用
  規則附表）；本案住宅區×12m 與 ×8m 恰同檔 3.5m 是**巧合非常數**。任何（分區×路寬）查表
  ≠3.5 的案例（同案內臨寬路街廓亦可）即觸發：T 錯→range 錯→G-gate 錯。修復＝建
  「(分區,路寬)→最小寬/深」查表接線。harness 忠實重現 app 現行為（不餵該 key）＝正確；
  接線波落地時 baselines/快照升 v2。

## 正規化白名單（嚴格為預設，鬆綁記帳）
diff 引擎每加一條 `_norm` 等價＝鬆一格閘門。**現行白名單僅兩條**：
1. `None ↔ 空字串`：CSV 往返把 None 寫成空格；非遮真 diverge。
2. 浮點顯示正規化至 **2dp**：CSV 字串化之位數噪音；真數值差（≥0.005）仍會現形。
新增任何 norm 規則**必須在此列名＋說明「為何這不是在遮真 diverge」**。

## 🔧 維護耦合：首跑不符 baseline 的嫌犯序（必讀）
1. **快照漏參數**（第一嫌犯）：harness 首跑不符 → 先比對 `case_params_UC9898.json` 是否漏餵某參數，
   **勿動引擎**。幾何量（真交集/範圍/G估/截角/街角最小面積）已證 cell-exact，非引擎問題。
1.5. **dtype 形式陷阱（法人統編）**：保留之 468 法人統編原檔可能存**數字**、匿名檔一律存**字串**；
   pandas 讀數字欄若落 float → `str()` 出 `'12345678.0'`，字串版則 `'12345678'`。**檔內一致故分群結構
   不受影響**（同構證明成立之因），但 ownership 段若法人群組現怪異 → **先查此形式差、再查邏輯**
   （一行 `df[col].astype(str).str.replace(r'\.0$','')` 類 debug 即可排除，省時間）。
2. **driver orchestration 漂移**：未來任何波動到**街角 callback**（`app.py` ~13765-14107）或
   **tab1 歸戶 inline**（~10844-11049）→ **必須同波更新 `verify/selection_pipeline.py`**
   （該二段為逐行複刻，不是 harvest 真函式）。該類波後 harness diverge，
   嫌犯序＝driver orchestration 漂移 ＞ 快照漏參 ＞ 引擎（引擎幾乎永遠不是元兇）。
3. **匿名化因素排除**：診斷/指配 diverge 時，先跑縮小版歸戶同構——只對「街角候選宗地」比對
   真資料 vs 匿名版之歸戶群組（持分結構、達標）；同構 → 排除匿名化、往 orchestration 查。

## 現況
- ✅ 幾何半：參數表（截角/街角最小面積）＋ -a 診斷（front_idx/截角idx/閘），雙情境 cell-exact。
- ✅ 選位半（2026-07-05 綠）：`selection_pipeline.py` 三段 driver →
  診斷（key=街廓+端+候選地號）/ 指配（key=街廓）/ 抵費地（key=街廓+端）三張 CSV
  雙情境全綠；0m 抵費地表驗「應空」。ownership Gxxx 靶組
  （G005/G007/G009/G019/G023/G029）於 PK 前先驗（三環定理鏈 tripwire）。
  driver 生成表落 `verify/out/got_*.csv` 供逐格勘查。
- ✅ B5 reviewer per-diff 過（additive-only 零 diff、六處複刻逐字忠實、白名單無偷加）。
- ✅ B6 真vs匿名歸戶同構（`b6_isomorphism.py`，真檔本機只讀不進 repo）：街角候選宗地
  34 筆，Gxxx 34/34 逐筆同、劃分同構 True、靶組於真檔重現 → 匿名化因素**永久排除**
  （嫌犯序 3 封閉）。報告：`out/b6_report.md`（零 PII）。
- baseline 出處：見 `baselines/PROVENANCE.md`（產出日、當時 app.py commit、UI 參數清單）。

## 選位半 driver 結構（selection_pipeline.py）
- `build_ownership()`＝**逐行複刻** app.py tab1 歸戶 inline（~10800-10993；st.button 分支內
  script 無法 harvest）：重劃區地籍迭代（起點鐵律，非 U_LAND）→ U_LAND match →
  指紋 → fp_to_group（插入序 Gxxx）→ `t8_ownership_map`（含 `_normalize_landno_module`
  變體鍵）＋ `t8_parcel_areas`。
- `build_build_parcels()`＝真函式管線：`parse_cadastral_geofile` →
  `validate_parcel_assignments_by_area(0.30, 30m)` → `overlay_polygons_to_blocks` →
  `_assign_four_column_areas` → `_annotate_temp_parcel_cut_type` → 可建築過濾。
- `run_corner_pk()`＝**逐行複刻**街角 callback orchestration（~13799-14060、14107-14119）；
  `select_corner_lots_both_sides_v12` 為 harvest 真函式。
- 忠實性紅線：`f3L_sb_rows_by_label` 在 app 全程無人寫入（v12 讀到 `{}` → 法定寬走 3.5
  預設）→ harness **同樣不餵**；退縮由 `f3L_setback_default` 逐情境設定（0.0 不被 `or` 竄改）。
- Gxxx 警告級：指配欄若「僅 Gxxx 群組號」不同 → `_classify_gxxx` 標警告級（不正規化吃掉、
  仍列 FAIL、導向 B6 仲裁）；已負向單測。診斷 diff 引擎已做竄改測試（改值/缺列/多列全咬）。
