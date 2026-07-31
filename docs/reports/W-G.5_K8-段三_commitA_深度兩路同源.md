# W-G.5 K-8 段三 **commit A**：深度取值兩路同源（U-K8-1 部分兌現）

> 施工單：《CC 施工單_K-8段三本體》§2（錨定 `32452af`）。**零幾何變更**；delta 源＝門檻
> （MinA／region_min／增配）。依施工單 §1「A 綠之前不得開始 B」，本報告只涵蓋 commit A。
> 行號一律綁 commit、引用時重 grep（🔒 行號衛生）。

---

## 一、KL 裁定與機制選擇

裁定（2026-07-31）：**只把街廓平均深度這一個數字**提前改成「app 與 harness 兩路皆當場自 CAD
現算 N-19′」；其餘快照維持 **U-K8-1＝乙**。

### 1.1 機制＝**快照層記憶體注入**（非逐消費點改寫）

- `verify/case_params_UC9898.json` **檔案零修改**（A-3）。
- `run_verification.load_snapshot()` 載入後，於**記憶體 dict** 內把
  `blocks[*].街廓分配深度_m` 覆寫為現算值。
- 因 `wf_f0~f4`／`wd4_tier_list`／`wd3_fragment_geom`／`stepg_pipeline`／`selection_pipeline`
  **全部以參數收 snapshot**（見 §二 清單），一處注入即全線同源，**無須逐處改寫算式**。

**為何不用「把 `SNAPSHOT` 常數指向 temp json」**（＝段二連帶量測所用之手法）：那會讓
`fixture_block_depth_n19p` T10 之**制度看守**也讀到注入值 → 誤報「制度乙：收斂態」，
而實際上檔案未換、baseline 未重烤。⇒ 另立 `load_snapshot_raw()` 供**制度看守與對照探針**專用。

### 1.2 算法單一真相源（🔴 禁在 `verify/` 另寫）

`app.py` 新增 module 級 **`n19p_depth_info_by_label`**（`grep -n "def n19p_depth_info_by_label" app.py`）
＋ **`_baseline_pts_from_manual`**，係自 app Step-G 之**內聯迴圈原樣抽出·零算式變更**；
app 改為呼叫之，harness 之 `run_verification.n19p_depth_by_block()` 呼叫**同一份碼**。
`round(D_avg, 2)` 之 2dp 法定鏈保留於 app 側（辦法 §3），harness 不再二次捨入。

---

## 二、A-0：深度消費點**窮盡清單**

### 2.1 識別字全集（N0-17-c）

| 識別字 | 角色 | py 命中數（`32452af`→本批後） |
|---|---|---|
| `街廓分配深度_m` | **快照鍵**（注入標的） | 29 |
| `街廓分配深度(m)` | 參數表欄名（≠快照鍵） | 4 |
| `f3_alloc_depth_by_label` | session 鍵（app-live／harness 孿生） | 12 |
| `f3_block_depth_by_label` | app session·診斷 dict（`D_min/D_max/note`） | 2 |
| `avg_depth`／`avg_depth_default`／`_avg_depth`／`_depth=` | 函式引數（下游消費） | — |
| `_compute_block_depth_alloc` | **算法本體** | 13 |
| `n19p_depth_info_by_label`／`n19p_depth_by_block` | 🆕 兩路之共用入口 | 6／6 |

### 2.2 逐落點：角色與處置

**A. 快照載入點（＝本批唯一改動層）**

| 落點 | 角色 | 處置 |
|---|---|---|
| `run_verification.py` `main()` | 主流程載入 | **`load_snapshot()`** |
| `wd4_tier_list`／`wd3_fragment_geom`／`b6_isomorphism`／`wg_g1_smoke`／`wg_g2_smoke`／`wg_g3` | 各自載入、跑同一批 pipeline | **`load_snapshot()`** |
| `fixture_cad_binding_order`／`fixture_baseline_candidates` | 載入後跑 `build_pipeline` | **`load_snapshot()`** |
| `probes/probe_corner_trueG`／`probe_jkstar_legitimacy`／`probe_ruling_K4_s_origin`／`probe_ruling_N_c7_sideline`／`probe_ruling_N_e1_touch`／`probe_ruling_N_recon`／`probe_ruling_N_p8`／`probe_ruling_K8_baseline_pairing`／`probe_ruling_K8_sideline_pairing` | 探針 | **`load_snapshot()`** |
| `probes/probe_ruling_N_depth` | 【B】欄比「本探針獨立 numpy 實作 vs app 實作」 | **`load_snapshot()`**＋註明係**兩份獨立實作**、差應 ≤0.005（app 側 2dp 捨入） |
| `tools/y_dump_diff` | Y 波 dump | **`load_snapshot()`** |
| **`fixture_block_depth_n19p`（T10）** | **制度看守**：現算 vs **檔案原值** | 🔒 **`load_snapshot_raw()`**——注入後兩邊同值＝看守靜默失效 |
| `archive/probe_ruling_K4_3_source` | 已封存（K-6 §四作廢·禁掛回） | **不動** |

**B. 下游消費點（皆以參數收 snapshot ⇒ 自動同源·本批零改動）**

`wf_f0:81`／`wf_f1:210`／`wf_f2:234`／`wf_f3:213`／`wf_f4:832,903,990,1304`／
`wd4_tier_list:81`／`wd3_fragment_geom:144`／`selection_pipeline:435`／
`stepg_pipeline:263`／`run_verification:219`（參數表 `街廓分配深度(m)` 欄）。

> ⚠️ 施工單 §2.1 種子表把 `stepg_pipeline:229`／`run_verification:128`／`selection_pipeline:435`
> 列為「**改現算**」。實測：這三處只是**下游讀者**，逐處改現算**不足以**產生 §2.6-2 所預測之
> 22 紅——因 MinA 係由 `wf_f0/wf_f4._mina_by_block` **直讀 snapshot** 算出，不經該三處。
> ⇒ 改採**快照層注入**（涵蓋全部 B 類），三處遂無須各自改寫。

**C. 合成測資（本就不吃 CAD·不動）**

`fixture_end_fallback:37`／`fixture_end_winner:64`／`fixture_end_reserve:115`／
`fixture_block_depth_n19p` T1–T7 之合成幾何。

**D. 刻意注入之反例測資**

`run_verification.py` 之 `W-D.4 MinA_區 reverse-test`（`grep -n "街廓分配深度_m.*20.0" verify/run_verification.py`）：
覆寫係在 `load_snapshot()` **之後**對記憶體 dict 為之 ⇒ **反例仍然有效**。
施工單 §2.1 之告誡（「改現算會使該注入失效」）**其前提為「在 `_mina_by_block` 內部改現算」**；
本批採快照層注入故不觸此雷。註解已同批更正（覆寫前之值 32.59 → **33.10**）。

**⇒ 無「無法歸類之落點」**（§6-4 停機條件未觸發）。

---

## 三、施工內容

| 項 | 落點（`32452af` 錨·請重 grep） | 內容 |
|---|---|---|
| A-2 算法源 | `app.py` `_baseline_pts_from_manual`／`n19p_depth_info_by_label` | 自 Step-G 內聯抽出·**零算式變更**；app 改呼叫 |
| A-1 | `run_verification.build_pipeline`／`stepg_pipeline.run_step_g` | `ss['f3_manual_baseline']` 由 `cad['baselines']` 鋪入；**空即 loud raise**（廢舊 `= {}`） |
| A-2 注入 | `run_verification.load_snapshot()`／`load_snapshot_raw()`／`n19p_depth_by_block()`／`_build_cb_cad()` | 快照層注入；`_build_cb_cad` 係自 `build_pipeline` 抽出之共用前段（避第二份街廓建構碼·#20） |
| A-4 同源閘 | `stepg_pipeline.assert_depth_same_source` | 逐塊比對·不等 loud raise |
| 註解更正 | `fixture_block_depth_n19p` T10 敘述／`run_all` 脫鉤清單註／`stepg_pipeline` docstring／reverse-test 註 | 血訓 #36：改機制時把舊機制的名字從註解一併改掉 |

### 3.1 A-4 閘：**閘寬依據** 與 **判別力實測**

閘寬 **0.005** ＝ 2dp 記載鏈之無差別半寬（辦法 §3 長度記至二位小數），**有機制依據、非實測殘差**。
🔒 **禁改用 `1e-6`**——K-8 §一 判 BASELINE `#0`/`#2` 為等價類、禁寫死單一實體，而 R4 之
N-19′ 等價類散布**實測 5.80e-06 > 1e-6**；硬比單值會把該禁令從配對層漏到數值層。

閘所比者為**兩條插線**（快照餵出之 `f3_alloc_depth_by_label` vs 當場現算），**非同一算式跑兩次**
——若寫成後者即成套套邏輯（`fixture-provenance` 禁令）。**判別力實測**：

| 餵入 | 結果 |
|---|---|
| 注入後之深度 | ✅ 通過 |
| **原始快照**之深度 | ✅ loud raise（列出 `{R4:(32.59,33.10), …}` 六塊） |
| 缺一塊之 dict | ✅ loud raise（母體不等） |

### 3.2 注入前後實測（`load_snapshot` smoke）

| 塊 | 檔案原值 | 注入後（現算 N-19′ 2dp） |
|---|---|---|
| R1 | 32.97 | **33.15** |
| R2 | 43.90 | **44.47** |
| R3 | 43.64 | **44.34** |
| R4 | 32.59 | **33.10** |
| R5 | 45.04 | **45.71** |
| R6 | 44.59 | **45.51** |

逐格等同段二連帶量測 log 檔頭所載之覆寫值；**檔案本體重讀仍為原值**（A-3 成立）。

---

## 四、驗收（施工單 §2.6·三層＋靶對帳）

跑法（全母體落檔·非 `viol[:12]`）：

```bash
python verify/tools/k8_seg3_A_runall.py K8_seg3_A > verify/out/K8_seg3_A.log 2>&1; rc=$?; echo "REAL_EXIT=$rc" >> verify/out/K8_seg3_A.log; exit $rc
```

對帳：`python verify/tools/k8_seg3_A_recon.py verify/out/K8_seg3_EF.log verify/out/K8_seg3_A.log verify/out/K8_seg2_cascade_ifsnapshot.log` ⇒ **rc=0**

| § | 判準 | 實測 |
|---|---|---|
| 2.6-1 | 132 名目不變（雙向 diff） | ✅ **132**；基準∖實測 0、實測∖基準 0 |
| 2.6-2 | 狀態翻轉逐項對帳·新增紅 ⊆ 預測 | ✅ **108 PASS／24 FAIL**（22 翻轉）；**超出預測 0、預測而未出現 0** |
| 2.6-3 | G 值 delta 應為 0 | ✅ G 閘違規 **442 列／442 列（100%）皆為欄「平均深度(m)」**（顯示欄）⇒ **G 未動·不停機** |
| 2.6-4 | 脫鉤清單 | ⚠️ 見 §六-1（**執行期脫鉤已解除**；清單續顯**檔案層**Δ） |
| 2.6-5 | golden 段 15 支逐支 rc | ✅ **15 支全綠**（基準 15 → 實測 15·紅 0） |
| 2.6-6 | 不重烤 | ✅ `git status -- verify/case_params_UC9898.json verify/baselines/` **零輸出** |
| 2.6-7 | 全母體落檔 | ✅ `verify/out/K8_seg3_A_viol.csv`·**588 列**（打印層僅 104 列 ⇒ 若照打印讀會漏 484 列） |
| 2.6-8 | 禁過濾引擎自報診斷 | ✅ log 未過濾 `T2-DIAG`／`S0d`；本報告以 `sed` 取段 |

### 4.1 §2.6-2 具名數字逐項對帳（全部**逐位相符**）

**逐塊 MinA（`round(D_avg,2) × 3.5`）**——預測 **+0.63〜+3.22**：

| 塊 | 舊 | 新 | Δ |
|---|---|---|---|
| R1 | 115.40 | 116.03 | **+0.63** ← 區間下界 |
| R2 | 153.65 | 155.64 | +1.99 |
| R3 | 152.74 | 155.19 | +2.45 |
| R4 | **114.07** | **115.85** | +1.78 |
| R5 | 157.64 | 159.99 | +2.35 |
| R6 | 156.06 | 159.28 | **+3.22** ← 區間上界 |

（R2–R6 之值取自 `verify/out/K8_seg3_A_viol.csv` 欄「MinA_街廓」實測列；
R1 無群落於該表故不現列，其值由同一 2dp 鏈導出。）

**`MinA_區` / ½ 顯示**（log `W-D.4 MinA_區==114.07…` 之 FAIL 明細）：
`MinA_區=115.85 ½顯示=57.93` ⇒ 預測 `114.07→115.85`／`57.04→57.93` ✅

**三個增配群**（欄「增配a′(㎡)」·兩情境）：

| 群 | 0m 舊→新 | 3.5m 舊→新 | Δ |
|---|---|---|---|
| G004 | 42.47 → 44.25 | 42.47 → 44.25 | **+1.78** |
| G011 | 24.30 → 26.08 | 23.73 → 25.51 | **+1.78** |
| G033 | 41.30 → 43.08 | 41.30 → 43.08 | **+1.78** |

**＝ΔMinA_區（115.85−114.07＝1.78）逐位相等** ✅

**§52-1 差額地價**（欄「差額地價(元)§52-1」）：

| 群 | 0m Δ | 3.5m Δ |
|---|---|---|
| G004 | **+135,717** | +135,717 |
| G011 | **+135,718** | +135,718 |
| G033 | **+135,718** | +135,718 |

⇒ 預測 **+135,717〜718** ✅

### 4.2 其餘翻轉之欄位歸因（全母體·非打印層）

| 測項群 | 欄 | 列數 |
|---|---|---|
| `v3/F.0/F.2/F.3 · G值`（8 閘×2 情境） | 平均深度(m) | 442 |
| `F.0·決策` | MinA_街廓 | 9＋9 |
| `F.2/F.3·池流向` | MinA | 6×4 |
| `W-D.4 跨占` | 該側MinA(㎡) | 21＋21 |
| `W-D.4 清單` | 增配a′(㎡)／差額地價(元)§52-1／路徑標註 | 3＋3＋8（×2 情境） |
| `碎片幾何` | 參考_depth×mw | 19 |
| `參數{0m,3.5m}` | 街廓分配深度(m) | 6＋6 |

**全部落在「深度 → 門檻」之因果鏈上，無一落在 G 值本身。**

---

## 五、A-4 同源閘之現地輸出

`run_all` 每趟於 `[1/3]` 顯示之脫鉤清單（`sed -n '/引擎↔快照 脫鉤清單/,/└/p'`）：

```
【T10】現算 N-19′ vs **快照檔案原值**：檔案層制度看守（🆕 commit A 後執行期已同源·本格只看檔案）
  街廓      app N-19′(2dp)      快照檔案         Δ
  R1               33.15     32.97     +0.18
  R2               44.47     43.90     +0.57
  R3               44.34     43.64     +0.70
  R4               33.10     32.59     +0.51
  R5               45.71     45.04     +0.67
  R6               45.51     44.59     +0.92
  ⇒ **制度甲：檔案仍為凍結舊值**（＝K-8 §三 commit A 後之正常態）　✅
```

---

## 六、🚩 上呈 KL

### 6-1 施工單 §2.6-4「脫鉤清單應顯示零脫鉤」——**字面未達成，實質已達成**（請裁是否需再動）

- **執行期脫鉤已解除**：`load_snapshot()` 注入 ＋ `assert_depth_same_source` loud 閘
  ⇒ app 與 harness 逐塊同值（R4 皆 33.10）。
- **清單仍顯示 Δ≠0**，因其看守對象為**檔案**（T10 制度看守）——而檔案不換正是
  **U-K8-1＝乙**（KL 已裁）。⇒ 要讓該清單字面顯示「零脫鉤」，**必須換檔＋重烤 v3 baseline**，
  與 §2.6-6「不重烤」直接衝突。
- **本批處置**：保留清單、改寫其敘述為「制度甲：檔案仍凍結·執行期已同源」，
  並具名列出**殘餘項＝換檔＋重烤**。**未自行擴權去換檔。**

### 6-2 施工單 §2.1 種子表之兩處更正（已於 §二 記載）

1. 三個「改現算」種子點實為**下游讀者**；逐處改之**不足以**產生預測之 22 紅
   （MinA 由 `wf_f0/wf_f4._mina_by_block` 直讀 snapshot）。⇒ 改採**快照層注入**。
2. `R4=20.0` 反例注入**未失效**（注入在 `load_snapshot()` 之後）。施工單之告誡其前提
   為「在 `_mina_by_block` 內部改現算」，本批未採該路徑。

### 6-3 陳舊註解一則（本批**未改**·屬 commit B 範圍）

`_shift_cut_block_range` docstring 稱「`difference(chamfer_tri)` 失敗 ⇒ 靜默保留未扣截角
（**R3 右實測差 6.2㎡**）」。**本批實測：該扣除於八街角**皆為 no-op**——
街廓多邊形 ∩ 截角三角形 ＝ **0.0000㎡**（八側逐一實測），且 `_build_corner_range_v2`
帶／不帶 `chamfer_tri` 之面積差為 **0.0000**（兩情境×八側）。
⇒ 街廓多邊形本身即**截角後**（與前置 B 之重疊率／缺口量測一致）。
該敘述屬 commit B（§三〜§五）之改寫範圍，**本批不動**（避免混入 A 之 delta 源）。

### 6-4 既有紅（非本批引入）

`W-F F.4`（3.5m E2 結構性不可行）＋ `W-G G.2`（F.4 純連坐）——早已待域裁，
本批後仍在 24 紅之內、**未擴大**。

### 6-5 停機條件檢視

施工單 §6 之四項＋§2.6-3 之 G 條款：**均未觸發**（G delta＝0；消費點清單無不可歸類落點）。
