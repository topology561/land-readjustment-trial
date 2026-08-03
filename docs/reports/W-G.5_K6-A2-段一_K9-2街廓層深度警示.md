# W-G.5 — **K-6-A2 段一：K-9-2 街廓層剖面深度警示**

> **性質**：本批為 **K-6-A2 之第一段**，係 K-6-A2 八項中**唯一可證明對本案零土地影響**者
> （六街廓餘裕 ≥ 19.08m）。選它打頭陣之目的＝**單獨驗證「接線正確」而不混入土地變動**。
> **起點 HEAD**：`7d21ec0`（＝ `origin/wip/s1-endpart`）
> **正典**：`grep -n "^## K-9 " docs/rulings/K-6_街角地分配程序與可分配判準.md`
> ⚠️ 本檔一切數字**皆由碼面自算**（`verify/out/probe_ruling_K9_block_depth.log`），
> **未抄交辦文之預期表**；抄來的數字不是驗證。

---

## 〇、開工前之偏離（先報）

交辦文 §〇 令 `git reset --hard origin/wip/s1-endpart`。**本批未執行該指令**，理由：

- `git rev-parse --short HEAD` ＝ `7d21ec0` ＝ `git rev-parse --short origin/wip/s1-endpart`
  ⇒ **本地已與 origin 同步**，reset 無收益。
- 工作區存有 **`data/地籍資料來源_匿名版.xlsx` 之未入 commit 異動**（W-G G.2 起即 **🚩上呈中**），
  `--hard` 會**逕行銷毀**之。

⇒ 以「HEAD 已等於 origin」取代 reset。**行號仍全部當場重 grep**（未沿用交辦文行號）。

---

## 一、實作內容（三處·**皆純加性**）

`git diff --stat` ⇒ `app.py | 134 +++…`（**134 insertions(+)、0 deletions(−)**）
＋新增 `verify/probes/probe_ruling_K9_block_depth.py`（探針·零土地後果）。

### 1-A `_compute_block_depth_alloc` — 新增三個剖面欄

（`grep -n "def _compute_block_depth_alloc" app.py`）

```
'd_front_p1': d1, 'd_front_p2': d2, 'D_k92_min': min(d1, d2),
```

**為什麼**：K-9-2 需「前緣線兩端垂距之 **min**」，而**現行回傳 dict 拿不到這個量**——
`D_avg` 是兩端**平均**、`D_min` 是**方法 A 取樣診斷**之極小值（**另一條軸**，
僅於方法 A 不可算時才退為 `min(d1,d2)`）。二者皆不可代。
`d1`／`d2` **本已在函式內算出**（`d1, d2 = abs(s1), abs(s2)`）⇒ 本改動**僅是把既有的量曝出來**，
**未新增任何算式**、**未動任何既有欄之值**。此即交辦文 §3.3「⛔ 禁自寫垂距算法」之遵法方式。

**同名不同量之戒**（docstring 已載·比照 K-9-6-a 體例）：
`D_k92_min` **≠** `D_min`——前者恆為 N-19′ 軸（垂直 BASELINE）且**恆不取樣**，
後者為方法 A（沿 `alloc_dir`）之**取樣**極值。**K-9-2 一律取 `D_k92_min`。**

**不 round 之理由**：門檻比較用**未 round 之原值**、`round()` 只在輸出層
（K-8 §二-1 WARNING-B 體例）。`D_avg` 之 `round(...,2)` 係其**進入乘積**之法定記載鏈（辦法 §3），
與本欄之**門檻比較**用途不同 ⇒ **不套用**。

### 1-B 新增 module 級 `k92_block_depth_check`

（`grep -n "def k92_block_depth_check" app.py`）

**為什麼抽為 module 級**（而非內聯於 UI）：比照 **K-8 §三 commit A** 對
`n19p_depth_info_by_label` 之處置——令 **harness 得呼叫同一份碼**、
**禁在 `verify/` 側另寫一套判準**。副效果：使本批之實測與反向對照**得以 headless 復現**
（UI 內聯之判準無法被獨立復現，等於只能自我採信）。

**判準**：`warn = (D_k92_min <= min_depth_table)`
——🔒 用 `<=`、**禁 `<`**（正典：「**等於也警示**」）。

**解析·禁取樣**：前緣線與 BASELINE 皆直線 ⇒ 垂距沿弦線性 ⇒ min 必落兩端之一 ⇒ 取兩端 min。
**全函式無迴圈取樣、無二分、無迭代**。

**四條 loud raise**（禁靜默、**不得跳過該街廓**）：
缺深度資訊／缺 `D_k92_min`／**缺正面路寬（≤0）**／附表查無深度（≤0）。

### 1-C app 接線（落點＝ §7-0a 前置地基檢查之緊鄰上方）

（`grep -n "K-9-2 街廓層剖面深度警示" app.py`）

**落點之依據**：BASELINE 係**逐街廓設定**（`grep -n "f3_manual_baseline" app.py`），
DXF 匯入當下未必已有 ⇒ 不得置於匯入處。實際落點＝**BASELINE 設定完成後、開始配地之前**
（緊接 `f3_min_width_by_label` 寫入之後、§7-0a 之前），與交辦文 §3.2 之指示一致。

行為：`warn` 者逐格 `st.warning`（含街廓名／剖面最小深度／畸零地最小深度／餘裕／兩端垂距，
**土地語言**）；全過則 `st.caption` 報 PASS 並點名餘裕最緊者
（比照 §7-0a 之 PASS caption 體例）。另曝 `st.session_state['f3_k92_block_depth']`。

---

## 二、§3.5 實測（**碼面自算·非抄本文**）

實料：`verify/out/probe_ruling_K9_block_depth.log`【A】段
（重跑：`python verify/probes/probe_ruling_K9_block_depth.py`）

| 街廓 | 分區 | 正面路寬 | d(p1 左) | d(p2 右) | **剖面最小** | 附表門檻 | 餘裕 | 判定 |
|---|---|---|---|---|---|---|---|---|
| R1 | 住宅區 | 12.00 | 33.164 | 33.128 | **33.128** | 14.00 | +19.128 | ✅ 無警示 |
| R2 | 住宅區 | 8.00 | 44.954 | 43.981 | **43.981** | 14.00 | +29.981 | ✅ 無警示 |
| R3 | 住宅區 | 8.00 | 43.772 | 44.898 | **43.772** | 14.00 | +29.772 | ✅ 無警示 |
| R4 | 住宅區 | 12.00 | 33.126 | 33.084 | **33.084** | 14.00 | +19.084 | ✅ 無警示 |
| R5 | 住宅區 | 8.00 | 43.510 | 47.904 | **43.510** | 14.00 | +29.510 | ✅ 無警示 |
| R6 | 住宅區 | 8.00 | 47.657 | 43.361 | **43.361** | 14.00 | +29.361 | ✅ 無警示 |

⇒ **六街廓零警示**（＝交辦文 §3.5 之預期）。餘裕最緊者 **R4 +19.084m**。

**獨立對拍**：本表之兩端垂距與**正典 K-8 §二 兩端垂距表逐格相符**
（`grep -n "兩端垂距" docs/rulings/K-6_街角地分配程序與可分配判準.md`）
——該表係**本批之前即已存在**之獨立真相源，非由本批新碼回填。

---

## 三、§3.6 反向對照（**臨時·已還原·未入版控**）

把 `k92_block_depth_check` 之門檻**暫時**改為 `_md = 40.00` 重跑：

| 街廓 | 剖面最小 | 門檻 | 餘裕 | 判定 |
|---|---|---|---|---|
| R1 | 33.128 | 40.00 | −6.872 | 🔴 **警示** |
| R2 | 43.981 | 40.00 | +3.981 | ✅ 無警示 |
| R3 | 43.772 | 40.00 | +3.772 | ✅ 無警示 |
| R4 | 33.084 | 40.00 | −6.916 | 🔴 **警示** |
| R5 | 43.510 | 40.00 | +3.510 | ✅ 無警示 |
| R6 | 43.361 | 40.00 | +3.361 | ✅ 無警示 |

⇒ **恰 R1／R4 觸發、其餘四格不觸發**（＝交辦文 §3.6 之預期）⇒ **本接線具鑑別力**，
非「零警示 ≡ 沒接線」。

**還原證明**：門檻已改回 `get_min_lot_size(_cat, _fw).get('min_depth', ...)`；
`git diff -- app.py | grep "40.00\|臨時反向對照"` ⇒ **0 命中**。
⛔ 反向對照**未加開關、未留碼裡**。

---

## 四、邊界與 loud raise 實測（合成輸入·**期望值由裁定文義手訂**）

⚠️ **臨時檢查·未入版控**（`scratchpad/tmp_k92_edge.py`）。合成輸入、不碰 DXF；
期望值來自**裁定條文**與**畸零地附表**，**非**由新碼回填。

| # | 檢 | 結果 |
|---|---|---|
| E1a | 剖面 13.99 < 14.00 ⇒ warn | ✅ True |
| **E1b** | **剖面 14.00 == 14.00 ⇒ warn（「等於也警示」）** | ✅ **True** |
| E1c | 剖面 14.01 > 14.00 ⇒ 不 warn | ✅ False |
| E1d | 門檻確為附表值 14.00（非常數兜底） | ✅ 14.0 |
| E1e | 路寬 12m 亦落 (7,15] 列 ⇒ 14.00 | ✅ 14.0 |
| **E1f** | **路寬 20m 落 (15,25] 列 ⇒ 16.00**（證門檻**真隨路寬查表**、非硬寫 14.00） | ✅ 16.0 |
| E2a | 缺深度資訊 ⇒ loud raise | ✅ RuntimeError |
| E2b | 缺 `D_k92_min` ⇒ loud raise | ✅ RuntimeError |
| E2c | 缺正面路寬（0）⇒ loud raise（**禁以附表最窄列兜底**） | ✅ RuntimeError |
| E2d | 非可建築分區（道路）⇒ 附表查無深度 ⇒ loud raise | ✅ RuntimeError |
| E3a/b | 回傳僅街廓級、無宗地級欄位（K-9-3） | ✅ |

**E1b 與 E1f 為本節重點**：前者鎖「等於也警示」（`<=` 非 `<`）；
後者證門檻係**真查表**——若有人日後把 14.00 硬寫進碼，E1f 立即翻。

---

## 五、`run_all` 逐項差異

實料：`verify/out/K6A2_seg1_runall.log`（`cd verify && python run_all.py`·EXIT=1）

### 5-1 計數

| | 跑前現況（CLAUDE.md 載） | 本批實跑 | 差異 |
|---|---|---|---|
| 名目總計 | 132 | **132** | **0** |
| PASS | 86 | **86** | **0** |
| FAIL | 46 | **46** | **0** |
| golden 支 | 16（1 紅＝E 系列實測快照閘） | **16（1 紅＝同一支）** | **0** |

### 5-2 逐項差異（**非僅比計數·比集合**）

計數相同不足以證明「同一組紅」（換一支紅、換一支綠亦得同數）⇒ **逐名目對集合**。
對照組＝`verify/out/K8_seg3_C.log`（＝現行 132／86／46 基線之產生輪·K-8 §三 commit C）：

```
diff <(舊 FAIL 名目 sort) <(新 FAIL 名目 sort)   ⇒ 空
diff <(舊 PASS 名目 sort) <(新 PASS 名目 sort)   ⇒ 空
```

⇒ **PASS 46 支與 FAIL 86 支之名目集合逐字相同、零進零出。**
⇒ **本批對 `run_all` 之逐項差異＝零**，無新增紅、無消失紅、無翻綠。
**故無須逐格歸因**（歸因之母體為空）。

### 5-3 與本批最相關之名目

| 名目 | 結果 | 說明 |
|---|---|---|
| `fixture_block_depth_n19p.py`（K-8 §二 N-19′·**直接覆蓋本批所改函式**） | ✅ PASS | 新增三欄為**純加性**，六塊 `D_avg`／`region_min` 115.85 @ R4／½ 57.93 全數不動 |
| `stepg_pipeline.assert_depth_same_source`（A-4 深度兩路同源） | ✅ 未 raise | 深度鏈未被本批擾動 |
| `W-D.4 MinA_區 reverse-test(改深度→隨動·非寫死)` | ✅ PASS | — |
| 46 紅之組成 | 不變 | 仍為 2 既有 ＋ 22（門檻源）＋ 22（街角幾何源），**全數已歸因、待波末重烤消化** |

⚠️ **WV_BAKE 未使用**——本輪係一般模式（`diff_rows` 未短路），故其綠具證據力。

---

## 六、只登記不改之落差

### 6-A 🆕 **GB-20**：`get_min_lot_size` 於**正面路寬 ≤ 0** 時**靜默取附表最窄列**

- **是什麼**：`get_min_lot_size(cat, 0.0)` 之迴圈為 `if w <= upper: return`，
  `w=0.0` 恆滿足**第一列**（`upper=7.0`）⇒ 住宅區回 `(3.00, 12.00)`
  ——即「**路寬未填**」被靜默當成「**路寬 ≤7m**」。
  （`grep -n "HUALIEN_MIN_LOT_TABLE = " app.py`；`grep -n "def get_min_lot_size" app.py`）
- **現行消費端**（**皆未防**）：
  `grep -n "_mw_d = float(get_min_lot_size" app.py`（→ `f3_min_alloc_area_by_label`／
  `f3_min_width_by_label`）、`grep -n "_size_info = get_min_lot_size" app.py`
  （→ 街角參數表之「法定最小寬/深」欄）。
- **與 GB-9／GB-13 之分野**：
  **GB-9** ＝ app 與 engine **兩個來源**可能脫鉤（無看守）；
  **GB-13** ＝ 附表值被誤用為**量測帶深**；
  **GB-20** ＝ **單一來源之缺值**被靜默代換為最窄列 ⇒ **三者互不涵蓋**。
- **本批處置**：**只登記不改既有消費端**。
  惟 **`k92_block_depth_check` 自身已 loud raise**（E2c）——本批新碼不承襲該靜默。
  ⚠️ 副作用：**正面路寬未填時，Step L 會於 K-9-2 處硬停**（訊息具名、指向臨街負擔步驟）。
  此為 no-silent-fallback 之刻意選擇（門檻無法源即不得比較），**請 KL 知悉**。

### 6-B ⚠️ **警示落在收合之 expander 內**（體例繼承·非本批引入）

本批接線與既有 §7-0a 同處
`with st.expander("⚙️ 街角地參數（共用設定 + 各街廓微調）", expanded=False)` **之內**
（`grep -n '"⚙️ 街角地參數（共用設定 + 各街廓微調）"' app.py`）
⇒ `st.warning` 須 KL **展開該面板**方得見。

- 交辦文 §3.2 明令「比照既有 §7-0a 之**體例與落點**」⇒ **本批照辦、未擅自搬家**。
- 惟「警示」之本意係**主動告知**；換案若真觸發而 KL 未展開該面板，該警示形同未達。
- **本批不改**（改之即動 UI 架構、逾段一之界）。**上呈 KL**：是否於段二（K-9-4）
  一併處理「有警示時自動展開／提至面板外」。

### 6-C 📌 **GB-10 之標注時機尚未到**

GB-10 載「`parcel_min_width_n14` 之 E-2′ 宗地深度閘自 **K-9-4** 起成為恆真閘」，
其觸發條件為 **K-9-4 上線**。本批只落 **K-9-2**（K-9-4 屬段二）
⇒ **GB-10 之誠實標注不在本批**、其「✅ 現況仍具鑑別力」之欄位**維持不動**。
⚠️ 段二（K-9-4）落地時**必須同批**處理 GB-10 之標注，勿漏。

---

## 七、紅線遵循自查

| 交辦文 §二 紅線 | 本批 |
|---|---|
| 1. 一項一 commit、各自可獨立回退 | ✅ 本 commit 僅 K-9-2 一項 |
| 2. 禁自訂容差 | ✅ **本批零容差**——判準為 `<=` 之直接比較，未引入任何 ε |
| 3. 禁二分／取樣／迭代兜底 | ✅ 解析取兩端 min，函式內無取樣迴圈 |
| 4. 虛擬量測塊禁取交集／禁進面積帳 | ✅ **不適用**（本批未動虛擬塊；亦未觸任何面積帳） |
| 5. 禁動 baseline CSV、禁重烤 | ✅ `git status -- verify/baselines/` 零異動 |
| 6. 禁靜默 fallback | ✅ 四條 loud raise（§四 E2a–E2d 實測） |
| 7. `WIDTH_VERDICT_CORNER_K4` 不動 | ✅ 未觸（`git diff` 無該字串） |

**守恆式**：本批**未觸任何面積、G 值、調配池、分配結果**——
新碼只讀深度與附表、只寫 `st.warning`／`st.caption`／一個新 session 鍵。
⇒ `ΣG ＋ 調配池 ＝ 街廓面積` **不受擾**。

---

## 八、未動之既有 `.py`（A1＝True）

倉內既有 `.py` 共 **52** 支（`git ls-files '*.py' | wc -l`），
本批**僅動 `app.py`**，其餘 **51 支逐檔 A1＝True**：

```
docs/reports/probes/probe_§4_R_end.py, docs/reports/probes/probe_§4_s0_pin.py,
tests/test_corner_priority_golden.py, tests/test_pool_slot.py,
verify/app_harvest.py, verify/archive/m_rescue.py, verify/archive/probe_ruling_K4_3_source.py,
verify/b6_isomorphism.py, verify/fixture_baseline_candidates.py, verify/fixture_block_depth_n19p.py,
verify/fixture_cad_binding_order.py, verify/fixture_corner_range_k8.py, verify/fixture_end_fallback.py,
verify/fixture_end_reserve.py, verify/fixture_end_winner.py, verify/fixture_n14_min_width.py,
verify/probes/probe_capacity_decomp.py, verify/probes/probe_capacity_decomp_solve.py,
verify/probes/probe_corner_trueG.py, verify/probes/probe_jkstar_legitimacy.py,
verify/probes/probe_ruling_K4_s_origin.py, verify/probes/probe_ruling_K8_baseline_pairing.py,
verify/probes/probe_ruling_K8_sideline_pairing.py, verify/probes/probe_ruling_K9_corner_width.py,
verify/probes/probe_ruling_N_c7_sideline.py, verify/probes/probe_ruling_N_depth.py,
verify/probes/probe_ruling_N_e1_touch.py, verify/probes/probe_ruling_N_p8.py,
verify/probes/probe_ruling_N_recon.py, verify/probes/probe_stage_order.py,
verify/run_all.py, verify/run_verification.py, verify/selection_pipeline.py, verify/stepg_pipeline.py,
verify/test_corner_first_lot_G.py, verify/tools/anonymize_cadastre.py, verify/tools/k8_seg3_A_recon.py,
verify/tools/k8_seg3_A_runall.py, verify/tools/scan_embedded_numeric_names.py,
verify/tools/verify_dxf_v6_1.py, verify/tools/y_dump_diff.py,
verify/wd3_fragment_geom.py, verify/wd4_tier_list.py,
verify/wf_f0.py, verify/wf_f1.py, verify/wf_f2.py, verify/wf_f3.py, verify/wf_f4.py,
verify/wg_g1_smoke.py, verify/wg_g2_smoke.py, verify/wg_g3.py
```

新增（非「既有」）：`verify/probes/probe_ruling_K9_block_depth.py`。

---

## 九、次步（**供 KL 裁·本批不執行**）

依交辦文 §六 之建議序，段二＝**K-9-4 BASELINE 臨接閘**（預期零觸發）。
⚠️ 段二落地時**必須同批**處理 **GB-10 之誠實標注**（見 §6-C）。

**上呈 KL 二事**：
1. **§6-A** ——K-9-2 於正面路寬未填時**硬停**，是否照此（or 降為警示）。
2. **§6-B** ——警示落在收合面板內，是否於段二一併改為「有警示即展開」。
