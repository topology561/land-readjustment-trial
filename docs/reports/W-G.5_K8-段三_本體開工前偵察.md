# W-G.5 K-8 段三【本體】開工前偵察（新 session·未動碼）

> 基準 `HEAD == origin/wip/s1-endpart == 3507b45`（本文寫入時）。
> 本批**零碼變更**。目的＝依血訓 #34／#36／#37「**動工前先量一次現況**」，
> 於施工前把 §三 之相依項、資料可及性、與**兩處未決之接線分歧**當場 grep 坐實。
> 行號一律綁 commit（🔒 行號衛生）；引用時請重 grep。

---

## 零、一分鐘定位

1. **§三 施工單全文不在倉內** —— 交接文 §五 載「施工單全文在 `262e5a0` 批之對話中」，
   全倉 `grep -rln "街角規定範圍新構造\|K-8 §三"` 僅命中三份**報告／裁定**（皆為摘要），
   無施工單本體。⇒ **本批不擅自重建規格**（分工鐵律：claude.ai 寫規格與 plan）。
2. 但**不依賴施工單細節**的部分已全部做完，見 §二〜§四。
3. **新發現兩項會改變施工順序的接線分歧**（§三、§四）＋**一項已作廢之相依項**（§五）。

---

## 一、現況錨（「新舊 delta」之**舊**側·倉內既有·非本批新量）

八街角現行**街角規定面積**（＝`_build_corner_range_v2` 之多邊形面積·2dp）：

| 街廓 | 左（0m） | 右（0m） | 左（3.5m） | 右（3.5m） |
|---|---|---|---|---|
| R1 | 109.79 | 110.56 | 226.18 | 226.88 |
| R2 | 151.44 | — | 309.05 | — |
| R3 | — | 152.82 | — | **308.93** |
| R4 | 109.20 | 109.70 | 225.25 | 225.67 |
| R5 | 146.93 | — | 300.52 | — |
| R6 | — | 146.38 | — | 299.13 |

源：`verify/baselines/退縮0m參數.csv`／`verify/baselines/退縮3.5m參數.csv`
（欄名 `【左】街角最小面積(㎡)`／`【右】街角最小面積(㎡)`）。
R3 右 `308.93` 與交接文 §5.3 所載一致。

同兩檔之 `街廓分配深度(m)` 欄現值 ＝ `32.97／43.90／43.64／32.59／45.04／44.59`
——**係舊快照值**，非 N-19′ 2dp 值（`33.15／44.47／44.34／33.10／45.71／45.51`，
見裁定檔 K-8 §二-1）。此即下述 §三 之分歧來源。

---

## 二、現行 (Ⅰ) 構造與其消費端（當場 grep·`3507b45`）

- 原語：`grep -n "def _shift_cut_block_range" app.py`（`:9039`）
- (Ⅰ)：`grep -n "def _build_corner_range_v2" app.py`（`:9104`）＝ 原語之具名 wrapper
- (Ⅱ)：`grep -n "def _build_burden_range" app.py`（`:9123`）＝ 同原語、`shift=Rw 飽和寬`、恆不扣截角

**現行 (Ⅰ) 之輸入不含深度**（`side_mid`／`block_vertices`／`block_centroid`／
`alloc_dir`／`shift_distance`／`chamfer_tri`）。⇒ 現行街角面積與 `D_avg` **無關**。

**活消費端共三處**（`grep -rn "_build_corner_range_v2" --include=*.py .`）：

| 端 | 落點 | 用途 |
|---|---|---|
| app 街角 PK | `app.py:9324/9328` → `_corner_range_left/right` → `_corner_poly_p1_B4/p2_B4`（`:9365/9366`） | 門檻＋跨占**同源**（交接文 §5.1-1 已坐實·本批重 grep 復驗命中） |
| app UI | `app.py:16026/16033` | 街廓互動分析之幾何面積顯示 |
| harness | `verify/run_verification.py:141`（`build_param_table.rng`） | 參數表 `【左/右】街角最小面積(㎡)` 欄 |

`_shift_cut_block_range` **除上述兩具名 wrapper 外無其他呼叫者**
（`grep -rn "_shift_cut_block_range" --include=*.py .` ⇒ 6 命中：定義 1、內部 `_tag` 1、
註解 2、wrapper 呼叫 2）⇒ §5.2「(Ⅰ) 不再用該原語」之作廢**不會殃及 (Ⅱ)**。

---

## 三、🔴 分歧一：§三 使街角面積**開始依賴深度**，而深度有兩條路

施工要點（交接文 §5.2）之「最小寬度帶 ＝ FRONTLINE 沿 BASELINE 法向平移 `round(D_avg,2)`」
＋「求 `t*` 使**帶內**最小寬 ＝ 退縮＋畸零地最小寬」
⇒ `t*` 依賴 `D_avg` ⇒ **街角規定面積依賴 `D_avg`**（現行構造不依賴·見 §二）。

而 `D_avg` 之兩條路徑（裁定檔 K-8 §二-2）在**同一個 session 鍵**上分岔：

| 路徑 | 寫入點 | 值（R4） |
|---|---|---|
| app-live | `app.py:15875` 呼叫 `_compute_block_depth_alloc` → `app.py:15904` 寫 `f3_alloc_depth_by_label` | **33.10**（N-19′ 2dp） |
| harness | `verify/stepg_pipeline.py:229` 由**快照** `SB[label]["街廓分配深度_m"]` 寫同一鍵 | **32.59**（舊快照） |

（`grep -rn "f3_alloc_depth_by_label" --include=*.py .`；
`grep -n "def _compute_block_depth_alloc" app.py` ⇒ `:5755`，其唯一活呼叫者在 Step-G UI。）

⇒ **一旦 §三 落地**，同一份碼在 app 與 harness 會得到**不同的街角規定面積**，
直到 U-K8-1（＝乙·快照留到 K-8 全案完成後一次換）執行為止。

**連帶效應**：段二之換快照連帶量測（`verify/out/K8_seg2_cascade_ifsnapshot.log`）當時結論
「**街角 PK 勝負與街角規定面積 delta = 0**」，**成立之前提正是「現行街角構造不吃深度」**。
§三 之後該前提消滅 ⇒ 該筆量測**對 §三 後之世界不再有效**，換快照時會出現**新的、尚未量測之連帶**。

**這不是純技術項**（動 §三 之取值來源 ＝ 動街角面積 ⇒ 動 PK 勝負 ⇒ 動面積歸屬），
且與**既有裁定 U-K8-1＝乙**互相牽動 ⇒ **上呈**，見 §六 Q1。

---

## 四、🔴 分歧二：harness 之 BASELINE **未接線**（`f3_manual_baseline` 為空）

§三 之新構造需 BASELINE 兩用（① 最小寬度帶之法向；② 範圍多邊形之遠側邊界）。

- app-live：`app.py:14260-14263`（`3507b45`）由 `_cad_layers['baselines']` 寫入 `f3_manual_baseline`（有值）。
- harness：`verify/stepg_pipeline.py:239` ⇒ **`ss["f3_manual_baseline"] = {}`（空 dict）**。
- `verify/run_verification.py:100-103` 之 fake session 只鋪
  `f3_cad_front_lines`／`f3_cad_side_lines_by_side`／`f3_cad_alloc_dir`／`f3_classified_blocks`
  ——**無 baseline**。

資料本身**存在**於 CAD 層（`cad["baselines"]`＝`{label: {'point','angle_deg',...}}`，
消費實例見 `verify/fixture_block_depth_n19p.py:235`、
`verify/probes/probe_ruling_K8_baseline_pairing.py:161`），只是**沒有鋪進 harness session**。

⇒ §三 施工**必含**「把 `baselines` 接進 harness 之 fake session／`build_param_table`」一項；
否則新構造在 harness 端會缺件（依 no-silent-fallback 應 loud raise，即**每趟必炸**）。
此為**純技術項**，不上呈，但**須在施工單／plan 內具名**，勿當成順手改。

---

## 五、已作廢之相依項（勿照舊施工）

`docs/reports/W-G.5_K8-段三_前置ABCD.md` §七-1 載
「**U-K8-5 併批**——本體改街角範圍構造時，`_legal_depth_B4` 之來源必須一併修正，
否則新構造仍吃 `14.0`」。

**該項已因前置 E 作廢**：`_legal_depth_B4` 鏈已於 `85e1c56` 整段刪除（死碼·U-K8-5 上半撤銷）。
本批復驗：`grep -n "_legal_depth_B4\|_blk_param_B4\|_sb_rows_B4" app.py`
⇒ **非註解 0 命中**（尚有 3 命中，`3507b45` 之 `:9275`／`:9279`／`:9287`，**皆為考古註解**、
無任何可執行引用）。⚠️ 本文初稿曾誤寫「0 命中」——**當場 grep 才是判準**（#36）。
⇒ **下一手勿再依 §七-1 施工**（同一份報告內前後兩節不一致·此處以後者為準）。

---

## 六、🚩 上呈 KL

| # | 題 | 性質 |
|---|---|---|
| **Q0** | **§三 施工單全文不在倉內**（見 §零-1）。請補貼全文，或授權由 CC 依交接文 §5.2 摘要＋裁定檔擬 plan 後逕送 reviewer。 | 程序（分工鐵律） |
| **Q1** | §三 之 `D_avg` 取值：(甲) 讀 `f3_alloc_depth_by_label`（⇒ app 走 N-19′、harness 走舊快照·**app≠harness** 直到換快照）／(乙) 兩路皆由 CAD **現算** N-19′（⇒ app==engine，但參數 CSV 之 `街廓分配深度(m)` 欄與實採值不一致、且 baseline 需重烤）。二者皆牽動 U-K8-1＝乙 之時序。 | **域**（面積歸屬·牽既有裁定） |
| — | 分歧二（harness BASELINE 未接線·§四） | 純技術·不上呈·僅登記 |
| `W-F F.4` | 3.5m E2 結構性不可行 | 既有紅·早已待域裁 |

---

## 七、驗收

本批**零碼變更**，故不跑 `run_all`（無可能之狀態翻轉）。
倉態核對：`git status --short` 之既有 🚩（`data/地籍資料來源_匿名版.xlsx`、
`verify/out/probe_capacity_decomp.log`）與大量既存 untracked **本批自始未觸碰**。

現行綠態仍為 `verify/out/K8_seg3_EF.log` 所載
**132 名目／130 PASS／2 FAIL**（`W-F F.4`＋`W-G G.2` 純連坐）｜golden 段 15 支全綠。
