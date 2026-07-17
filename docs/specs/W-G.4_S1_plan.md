# W-G.4 S1 施工 plan **v2**（S0d ＋ step 0 amp 斜交修 ＋ §N1 buffer 幾何化）

> **v1 經 reviewer 退回 BLOCKED**（`e367c71`）→ 本 v2 依 **KL 2026-07-17 補丁四**（N0-18b／S0d／三裁）全面改寫。
> 依據：規格 **N0-18b**／**N0-18a（升格為內部全精度通則）**／**§N3-0e S0d**／**§N1**／**N0-7 重述**／**N0-10**＋補丁四 §四。
> 基準 HEAD：`e367c71`+（補丁四入倉同 push）。
> **狀態：plan v2·未動工**——波紀律＝plan → reviewer → claude.ai 複驗 → **KL 確認才動工**。
> **範圍：S0d ＋ step 0 ＋ S1**（三者幾何連動 → **併一次重烤**·補丁四 §五）。**不動** §N2（S2）／§N3（S3）／§N5（S5）。

---

## 0. v1 → v2 之變更（reviewer BLOCKED 三項全數處置）

| v1 之錯 | v2 之改 |
|---|---|
| **BLOCKED-1** bisect 無 `side` 參數、自 `corner_pt` 量 → R3右 388.92（+79.99≈576萬）；**而完全複現規格錨 R2 8.7157（左側塊）** | **§2 helper `side` 參數化**；目標函式改**真實池帶**：left→`[s_min, buf]`／right→`[amp−buf, s_max]`。**#25 入正典** |
| **BLOCKED-2** 「S2 無縫承接」為偽（R1右/R6右 皆右側·誤差 −94.84/−182.21）；`wf_f1` 無 right 分支 | side 參數化即解；**`wf_f1` 補 right 分支**（§2 表 #3） |
| **BLOCKED-3** 閘② 套套邏輯（量 helper 內部收斂 ⇒ 恆綠）；`f(0)=0` 恆真且右側正解下為偽（R3 f_true(0)=78.24） | **閘② 錨改 `F.0_G值` 抵費地列「幾何面積(㎡)」**（`_pool_strips_for_block` 之真實產物）；**刪 `f(0)=0`**、留 `f(hi) ≥ range` loud raise |
| **W-1** 閘⑤「Σ池恆定」為偽 | **改 `ΔΣ池 = −ΔΣG` 恆等式閘**（N0-7 重述·散文閘轉真閘） |
| **W-3** 楔形歸屬未定 | **裁入 S1 為 step 0**（補丁四 §三-(b)） |
| **W-6** §N1 錨歸屬錯 | 規格錨句已改寫（389.85＝池片；標的＝buffer 帶 **311.61 → 308.93**） |

---

## 1. step 0：**amp 斜交修**（上游幾何域錯·補丁四 §三-(b)）

**病灶**：推進域用**正交**投影 `actual_max_proj = max(dot(v − corner_pt, d_hat))`（`stepg:563-569`／`app` 同構），
而池域用**斜交切線座標** `s_max`（`_strip_axis`）→ **R3 差 3.4571m** → 產生 `s 域 ⊄ [0, amp]` 之楔形。

**reviewer 坐實（三處·與 baseline 逐位相符）**：R1 `s_min=−0.3248`→楔 **5.3255**；R6 `s_min=−3.6068`→楔 **85.7064**；
R3 `s_max−amp=3.4571`→楔 **78.2363**。→ **此即 W-D.3 §4 積欠碎片清單之真因**（非 §N5 下游碎片）。

**改法**：`actual_max_proj` 改用**斜交切線座標**（＝`_strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)` 之 `s_max`）
——**複用 T2 之 helper**（plan §1.5 已證同型修法·斜交式 `t = ((p−bp)·m̂)/(d̂·m̂)`·**禁正交投影**）。
→ 推進域與池域**同座標系** → **`s 域 ⊂ [s_min, s_max]` by construction** → 三楔形消滅。

**⚠️ 但 side 參數化仍不可省**（補丁四 §三-(b) 明示）：**末端真楔形不因 step 0 消失**
（ALLOC 與 BLOCK/BASELINE 不平行之真實幾何·§N3-0 T2 已明）——**#25 教訓：通式不得賭在單側退化**。

**§N5 之範圍隨之收縮**：只留 step 0 後**真殘**之碎片。

---

## 2. S0d：S0c 修向反轉（§N3-0e·依 N0-18b-2）

| # | 標的 | 改法 |
|---|---|---|
| 1 | `app.py:6821` 實切 | **撤 `_S_cut`、回復未捨入 `S_conv`** |
| 2 | 推進 | **改吃未捨入 S**：`res` 增攜全精度值（如 `'S_raw'`）；`stepg:541/632` `_S_actual` 改取之；`547/638` `cum += _S_actual` |
| 3 | 顯示欄 | **`'S'`／`'累積S'` 照舊 `round(...,2)` 輸出**（N0-18：顯示 2dp） |
| 4 | `area_conv` | **＝全精度實切面積**（顯示 2dp）；`增減` 收斂至 bisect tol 級 |

- **同源於全精度** → 縫與疊仍 by construction 歸零 → **②-宗 圍堵閘維持 ≤1e-6**。
- **閘① 不受影響**（G 為財務量·定於 `6792`/`6804`·在實切之前）。
- **🔴 閘寬連動（單源函式改係數·一處改五處生效）**：`_acct_geom_tol_per_lot|_block`
  → **`0.005×深度` 項歸零**：逐宗 `≤ tol(0.01) ＋ 0.005 = 0.015`；逐街廓 `≤ 宗數×0.015`；全區＝加總；
  **E3 `≤ 整形宗數×0.005`**（無 tol 項·整形不經 bisect）。
  **依據＝正典補條：量子項僅對「實際存在於計算路徑之量化」立項**——S0d 後 S 量化退出路徑。

---

## 3. §N1：buffer_S′ 幾何 bisect（**side 參數化**·單一真相源）

**新增模組級純函式**（`app.py` `_pool_strips_for_block` 鄰近·`ns` harvest）：

```
_corner_buffer_S(block_poly, d_hat, corner_pt, allocation_dir, range_area, side,
                 tol=0.01, _label='') -> float
  # §N1：bisect 解 buffer_S′ 使**真實池帶**面積 == range_area（|Δ| ≤ tol）
  #   side='left'  → band = block ∩ s∈[s_min, buf]
  #   side='right' → band = block ∩ s∈[amp − buf, s_max]     ← step 0 後 amp == s_max
  # s_min/s_max ← _strip_s_range(block_poly, ...)（斜交切線座標·與 _pool_strips_for_block 同源）
  # 回傳**全精度** float（N0-18a 升格後之通則：內部全精度·不捨入）
  # range_area ≤ 0 → 回傳 0.0（無 forced）
  # 斷言：**刪 f(0)=0**（恆真·且右側 f_true(0)=78.24≠0 會誤停）；
  #       留 `f(hi) < range_area` → **loud raise**（街廓容不下 range·N0-10 無吸收機制）
```

- **單調性（reviewer 已證·採認）**：strip ＝ `[0,S]×[−big,big]` 之像、`big` 只依 `block_poly.bounds`
  **與 S 無關** → `strip(S₁) ⊆ strip(S₂)` → 面積單調不減。**集合包含論證·不需凸性·斜交亦成立**
  （數值：6 塊×4000 點·遞減點 **0**）。→ bisect 適用 ✅
- **正解錨（reviewer 實跑·v2 施工後須命中）**：**R5左 8.6774／R2左 8.7157／R3右 5.2719**
  → 帶面積 **300.52／309.05／308.93**（＝range·±0.01）。
- **⚠️ R2 之 8.7157 對「side」零舉證力**（#25）→ **驗收<u>必含右側</u>**（R3右 5.2719）。

**四處同步**（與 T2 完全同組）：

| # | 檔:行 | 改為 |
|---|---|---|
| 1 | `app.py:15291`／`:15298` | `_corner_buffer_S(..., float(_l_min), side='left')`／`side='right'` |
| 2 | `stepg:421`／`:428` | 同上（**byte 級對映 app**·N0-16） |
| 3 | `wf_f1:216` | 同上·**併補 `right_buffer_S` 分支**（現無·BLOCKED-2） |
| 4 | `wf_f4:1121`／`:1128` | 同上（`_reshape_block` 內·`side` 已在 scope） |

- **通式·禁寫死**：依 `forced_map` 動態；**0m 零 forced → `range_area=0` → 回 0.0**。
- **`_WF_NS_NAMES` 16→17**；`run_verification:1111` 標籤 `ns 16`→`17`；`_wf_ns()` docstring（`app:8403`）「13」→「17」。

---

## 4. scope guard

- **不動** `_build_corner_range_v2`（range 之產生法·S1 只消費其面積）。
- **不動** §N2 街角資格／forced **名單**（S2）；**不動** §N3 targeting（S3）；**不動** §N5 下游（S5·範圍隨 step 0 收縮）。
- **不動** T2 之 `_pool_strips_for_block` **建構法**（step 0 令其 `s 域` 與推進同源·**值**變、法不變）。
- **⚠️ WATCH（既存·不改·reviewer 核可此界線）**：`app:16215` Rw 診斷讀 rounded buffer_S 且未乘 `cos_dn`
  → **診斷非閘**（出口 `st.dataframe`·無 raise；真 telescoping 閘在 `stepg:801-812`·用 raw `W0_*`）。
- **⚠️ 既存·列 backlog（非本波）**：**app 根本無 telescoping 閘**（`_W0_left/Wf_left` 僅 stepg 有）；
  `app:6053/6056` → 角落抵費地 L/R **以 range 記帳而幾何是 212.84**（**反向佐證 piece 讀法**）→ S1 後 `中央池` 值連動。

---

## 5. 驗收（②不變量閘＋③預測差量閘）

| # | 閘 | 判準 |
|---|---|---|
| **①** | **業主宗 G 一字不變**（**絕對**） | G 為財務量·S0d/step0/S1 皆不動之 → **逐格 byte 相同**·一格不符即停 |
| **①-0m** | **0m 全譜系一字不變**（**絕對**·reviewer 證成） | 0m 零 forced（病灶行在 `if _fo_left:` 內·`app:15287`／`left_forced_offset` 於 0m 恆 False）→ **step 0 除外**（amp 修影響全情境·見註） |
| ② | **N0-10 幾何比對閘**：forced **帶**面積 == range（**0.01**） | R5左→300.52／R2左→309.05／**R3右→308.93**。**錨源＝`F.0_G值` 抵費地列「幾何面積(㎡)」**（禁用 helper 內部收斂值＝套套邏輯） |
| ③ | `buffer_S′` 命中正解錨（±0.001） | R5 8.6774／R2 8.7157／**R3 5.2719**（**必含右側**·#25） |
| ③' | **step 0：三楔形消滅** | R1 5.3255／R6 85.7064／R3 78.2363 → **0**（`s 域 ⊂ [s_min,s_max]` by construction） |
| ④ | **`ΔΣ池 = −ΔΣG` 恆等式閘**（**N0-7 重述·散文閘轉真閘**） | 預測 ΔΣG **+3.62** → Σ池 2299.26 → **2295.64**；**逐街廓亦須恆等** |
| ⑤ | T1 新留片／片數差異**逐片可歸因** | step 0 後楔形消滅 → 片數應**減**；須逐片對上 |
| ⑥ | **帳對幾何閘收緊**（S0d） | 逐宗 `≤0.015`／逐街廓 `≤宗數×0.015`／E3 `≤整形宗數×0.005` |

**不變量閘**：①' 覆蓋 0.01／②-池 1e-6／**②-宗 ≤1e-6**（S0d 後·非 0.005×深度）／逐宗主閘／守恆兩級／**N0-10（新綠）**。

**⚠️ 註（閘①-0m 之範圍）**：**step 0 之 amp 斜交修影響<u>全情境</u>**（0m 亦有楔形：R1 5.3255／R6 85.7064）
→ **0m 非零行為變更**！**閘①-0m 僅適用於「S1 之 buffer 段」，不適用於 step 0**。
**改**：0m 之 **buffer 相關欄**（`角落抵費地L/R`）須一字不變；0m 之**池片幾何**則依 ③' 變動且須可歸因。
**（此為 v1 之閘① 於 v2 下之範圍收縮——reviewer 證成之「0m 零 forced ⇒ 零行為變更」僅對 buffer 段成立。）**

**⚠️ 量級預告**：3.5m forced 帶 R5 +87.68／R2 +75.26／R3 −80.92（對 range）→ 該側全體宗起點位移
→ **3.5m baseline 大幅重定**；**0m 亦因 step 0 而動**。**此為標的本身、非回歸**——惟須逐項可歸因。

---

## 6. 施工序（**S0d ＋ step 0 ＋ S1 併一次重烤**·補丁四 §五）

1. **S0d**（§2）→ 閘寬單源函式改係數 → py_compile。
2. **step 0**（§1·amp 改斜交）→ 驗 ③'（三楔形消滅）。
3. **S1 helper `_corner_buffer_S`**（§3·side 參數化）＋四處接線＋`wf_f1` right 分支＋ns 17。
4. 驗 ②③（含**右側** R3 5.2719）。
5. **PRE 凍存** → **併一次重烤** → 閘①③'④⑤⑥＋不變量閘全綠 → run_all 綠。
6. py_compile → grep 對照本 plan → **push**（嚴格 `git rev-parse origin/main` 驗）。
7. 報告入倉·聊天僅 ping → claude.ai 複驗 → **KL 重新 UI 實跑錨定**（**幾何已動·前錨降級為歷史對照**·乙匯出照 trunk A′ 版）。

---

## 7. 送 reviewer（v2 之設計裁決／WATCH）

1. **step 0 之落點**：`actual_max_proj` 於 `stepg:563-569`＋app 同構——**改為 `_strip_s_range` 之 `s_max`**。
   求驗：①是否**全部**消費端皆改（`end_pt`／`d_hat_rev`／`right_cum_S` 之基準）？②`app` 側同構是否逐字？
2. **S0d 之 `S_raw` 攜帶**：`res` 增鍵（`'S_raw'`）vs 改 `'S'` 為全精度＋顯示層 round——**傾向前者**（顯示欄契約不動·baseline 欄名不變）。求覆核。
3. **閘①-0m 之範圍收縮**（§5 註）：是否正確？0m 因 step 0 而動，**是否仍有「絕對閘」可用**？
   （**傾向**：以 `G(㎡)` 欄之 0m 逐格 byte 相同為絕對閘——G 不隨幾何動。）
4. **`ΔΣ池 = −ΔΣG` 閘之落點**：`run_verification` 之重烤驗收段 vs `stepg` ledger——**傾向前者**（跨代量·非代內）。
5. **step 0 之爆炸半徑**：amp 改斜交 → `right_cum_S` 之基準變 → **右組全體宗位移**？求驗此預測。

**本 plan 之 KL 域裁題：無**（補丁四已裁 N0-18b／S0d／三題）。撞出未涵蓋之真實違規 → **§N8 停機上呈**。
