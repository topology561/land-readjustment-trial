# W-G.4 S1 §3 街角 band recon ＋ side-參數化 approach（送 reviewer）＋ §4 N0-20 recon 狀態

- 日期：2026-07-20；branch `wip/s1-endpart`（基準 **`ca4985e`**＝三小項已 push·KL 已獨立 grep 驗過）
- 範圍：**§3 街角 band（本文 approach·待 reviewer）**＋**§4 N0-20（recon 未起·本文僅列待辦）**
- 波紀律：recon（禁假設）→ approach → **reviewer 獨立復現** → 施工 → push → KL 複驗 → 末端一次重烤

## 施工狀態（2026-07-20·補丁九定案後）

- **補丁九定案入倉**（`docs/specs/W-G.4_規格v3補丁九…md`·KL verbatim·三域裁 **①對 ②OK ③同意**）→ 三裁鎖如本 approach 所實作（裁1 band≡range 照實·裁2 左帶上界=`buf`+夾0·裁3 k* 屬 W-D.2）。
- **§3 已施工**（未 commit·reviewer 審 diff 中）：新增 `_corner_buffer_S`（side 參數化·方位契約 assert·約束1 缺 allocation_dir→loud raise）→ 接四處（app 左右／stepg 左右／wf_f1 左／wf_f4 左右·**wf_f4 傳 FRONT p1,+d̂**）→ ns 17→19 → `run_verification` ns 閘訊息去死字串。
- **施工判準 PASS**（實跑·range 取真 forced map·非寫死）：**R2-left buf=8.7157／R3-right 8.7290／R5-left 8.6774**（三獨立既有錨同時命中）·band≡range Δ=±0.0000·0m 無 forced（全空）·**未**得 BLOCKED-1 錯式解。py_compile 五檔綠·殘留矩形近似 grep **0**·ns=19。
- **施工核（約束1）PASS**：`_strip_axis`（`app:6851`）docstring 逐字證 `_pool_strips_for_block` 為 **∥ALLOC 斜交切**（`n_hat=rot90(allocation_dir)`·明文禁正交·實測正交殘差 346.89㎡→斜交 0.0000）；新 bisect 複用即繼承斜交。缺 allocation_dir 之正交退路→`_corner_buffer_S` **loud raise**（約束1「禁假設 d̂⊥â」）。
- **右側帳第三方坐實（取代未 commit probe·補丁九 §三·line 72）**：claude.ai 純 CAD 座標復現 forced band——R2 233.792／R3 **235.013**／R5 212.846（vs CC probe 233.788／235.017／212.836·殘差 <0.011㎡·座標精度級）；Σ 毛短留 **236.849 ≈ CC 236.859**·`s_min/s_max` 亦對上。**R3 右之 235.013 ≈ CC 235.017 ＝ 右側維度之獨立坐實**（#25 之封）。
- **約束3 註（out of §3 scope）**：`range`（309.05 等）由 `_build_corner_range_v2` 產（plan §8「S1 只消費·不動」）；其角落基準須 =截角前 SLIDELINE 中點——本案 range 值經 claude.ai CAD 復現坐實正確（我消費即正確）；基準一致性屬 `_build_corner_range_v2`／泛化波之責，非本 §3 施工標的。

## KL 三裁（2026-07-20·施工核·鎖）

- **① wf_f1 右支架 deferred（KL 裁·施工決定·非土地）**：本波以 **loud raise 取代 plan §3:99「補 right 全鷹架」**，真支架待**泛化波**補（該檔硬釘 `lbl="R1"`＋結構左向·R1 兩情境皆非 forced→右鷹架必死碼·#18④）。**碼裡留 TODO**（`wf_f1.py` loud raise 上方·逐字 KL 裁語）·免下一接手誤判漏做。補丁九＝KL verbatim·不動；此條歸報告施工核。
- **② 次序（KL OK）**：先 push §3 → claude.ai 複驗 → 停機③ 另段修（KL 複核 diff）→ 續 §4·皆末端重烤前完成。
- **③ 停機③ 修（KL 收此區·兩施工約束·KL 複核照此驗）**：
  1. **一致性判準**：凡算進 **ΣG 之地主宗**都須從池扣掉——**判準對齊「ΣG 成員」**，非單純把 `0.5` 改小。
  2. **先確認 `0.5` 無防退化碎片之職**（#26a）再動。
- **#25 死因所在**：`_corner_buffer_S` 若不 side 參數化，左側退化為正確、右側錯 ~80㎡（≈576 萬元），而規格唯一錨（R2左 8.7157）**恰落左側子域、對右側零舉證力**

---

## 1. §3 recon（四處病灶·行號皆本次重驗·plan 原值已漂移）

**病灶＝矩形近似** `buffer_S = range_area ÷ avg_depth`（把真實斜交池帶當成 depth 等深矩形）。

| # | 檔:行（**本次實測**）| plan v3 原載 | 現碼 | 備註 |
|---|---|---|---|---|
| 1 | `app.py:15342`／`15349` | 15291/15298 | `_left/_right_buffer_S = float(_l/_r_min) / avg_depth_default` | `_l/_r_min`＝`f3L_corner_min_table` 之`【左/右】街角最小面積(㎡)`；幾何變數（`blk_poly/d_hat/corner_pt/allocation_dir_block`）**已在 scope**（15167-15204 定義）✓ |
| 2 | `verify/stepg_pipeline.py:422`／`429` | 421/428 | 同式 | 幾何變數同在 scope（~327/343/347）✓ |
| 3 | `verify/wf_f1.py:216` | 216 ✓ | `left_buffer_S = float(_ma) / avg_depth` | **🔴 僅左分支·無 right**（W-7／BLOCKED-2）→ 須補 **right 全鷹架**（`end_pt`／`d_hat_rev`），非只加變數 |
| 4 | `verify/wf_f4.py:1121`／`1128` | 1121/1128 ✓ | `buf = fo.get("left/right_corner_min_area") / avg_depth` | **已有 side 分支**（1116 `side = "left" if frag["s"]<0.5 else "right"`）；右支已用 step0 `_oblique_s_max`（`corner = p1 + s_max·d̂`／`dh = −d̂`）→ 與新通式框架**天然對映** ✓ |

**T2 既有真相源（新函式一律複用·禁另造）**：
- `_strip_s_range(geom, d_hat, corner_pt, allocation_dir)`（`app.py:6896`）→ `(s_min, s_max)`，**斜交切線座標**、相對 `corner_pt`；恆等 `s(corner_pt + s0·d̂) ≡ s0`。
- `_block_strip(block_poly, d_hat, baseline_pt, S, allocation_dir)`（`app.py:6739`）→ `(cut_geom, area)`。
- **s 區間→實帶** 之正典呼叫式（抄自 `_pool_strips_for_block:7026-7028`·同源不漂移）：
  ```python
  bp = corner_pt + a * d_hat
  g, area = _block_strip(block_poly, d_hat, bp, b - a, allocation_dir=allocation_dir)
  ```
- `_oblique_s_max`（`app.py:6921`·step0 已四處同源）→ 右組 `s_max`。

---

## 2. §3 approach：`_corner_buffer_S`（模組級純函式·**side 參數化**）

**落點**：`app.py` `_pool_strips_for_block` 鄰近（模組級·可 harvest）。

```
_corner_buffer_S(block_poly, d_hat, corner_pt, allocation_dir, range_area, side,
                 tol=0.01, _label='') -> float      # 全精度回傳（N0-18a·不 round）
```

**語意**：bisect 解 `buf` 使**真實池帶面積 == range_area**（|Δ| ≤ tol）。

**帶之構造（side 參數化＝#25 之修）**——`s_min, s_max = _strip_s_range(block_poly, …)`：

| side | s 區間 | 依據 |
|---|---|---|
| `'left'` | **`[max(s_min, 0), buf]`**（上界＝`buf`·**非** `lo+buf`）| 左組自 `corner_pt`(s=0) 沿 `+d̂`；消費端 `app:15447/15481` `left_cum_S=buf` → 首宗自 **s=buf** 起 ⇒ 保留區恆為 `[s_min, buf]`。**唯上界 load-bearing**（`_block_strip` 已與 block_poly 取交集·下界 ≤ s_min 即等價）|
| `'right'` | `[s_max − buf, s_max]` | 右組自 `end_pt`(s=`s_max`) 沿 `−d̂` 推進；**step 0 後 `amp == s_max`**（故用 `s_max`·非舊正交 `amp`） |

> 🔴 **BLOCKED-1 更正（reviewer 活抓·CC 原文錯·#25 逐字重演）**：本表 left 列原寫 `[lo, lo+buf]`——**與 plan §3:84 之 `[lo, buf]` 不同**，且錯的正是本波唯二 left-forced 塊（R2 `s_min=+0.2677`／R5 `+0.2685`）。reviewer 逐位坐實閘之錨源即 `[s_min, buf]`（R5 212.836≡F.0 `212.84`／R2 233.788≡`233.79`）。**兩式解出值**：plan 式 R2→`8.7157`（＝規格 §N1 唯一 buffer 錨）／R5→`8.6774`（＝#25 表值）／R3→`8.7290`（＝plan §3 post-step0 值）**三錨同時命中**；CC 錯式 →`8.4479`／`8.4088`（各差一個 `s_min`）。**且 R3 之 `s_min≈0` ⇒ 兩式在 R3 同值**——當初照出 #25 的那一塊，**對「s_min≠0」維度零舉證力**（#25① 逐字重演·代價 ~23.8㎡≈171 萬元）。
> **施工判準（釘死）**：解出 **R2=8.7157／R5=8.6774／R3=8.7290** 為對；若得 8.4479／8.4088 即錯式。

**右側非左側之鏡射**——原點不同（`s_max` vs `0`）、推進向反號。舊通式一律自 `corner_pt` 量 → 左側**退化為正確**、右側錯（#25）。**本設計以 `side` 顯式參數化該維度**。

**邊界/退化**：
- `range_area <= 0` → `return 0.0`（無 forced·不進 bisect）。
- **刪 `f(0)==0` 前置檢查**（恆真式·且 pre-step0 右側 `f_true(0)=78.24≠0` 會誤停）。
- 保留 **`f(hi) < range_area` → loud raise**（帶吃滿全街廓仍不足 → 幾何前提破·禁靜默回 hi）。
- `_strip_s_range` 回 None／`_strip_axis` denom 退化 → **loud 傳播**（no-silent-fallback·勿吞）。

**單調性**（bisect 適用之前提）：`strip(S₁) ⊆ strip(S₂)`（集合包含·斜交亦成立）→ 面積對 `buf` 單調遞增。plan §3 載 reviewer v2 已證（6 塊×4000 點·遞減 0）·**本波採認不重證**，惟施工時加 `assert` 於 bisect 端點。

**四處同步**（T2 同組·#20 單一真相源）：
| # | 檔 | 改 |
|---|---|---|
| 1 | `app.py:15342/15349` | `_corner_buffer_S(…, range_area=float(_l/_r_min), side='left'/'right')` |
| 2 | `stepg:422/429` | 同上（byte 級對映 app·N0-16） |
| 3 | `wf_f1:216` | 同上＋**補 right 全鷹架**（`end_pt = p1 + s_max·d̂`／`d_hat_rev = −d̂`·`_oblique_s_max` 同源） |
| 4 | `wf_f4:1121/1128` | 同上（`side` 已在 scope·框架天然對映） |

**ns**：`_WF_NS_NAMES`（`app.py:8432`）**17→19**（＋`_strip_s_range`＋`_corner_buffer_S`）；`run_verification:1110` 集合差閘＋`_wf_ns()` docstring 同步。
> ⚠️ **plan §3 載「16→18」已漂移**：本次實數 `_WF_NS_NAMES` ＝ **17**（plan 寫於 `5b479b6`·其後 step 0 增列 `_oblique_s_max` → 17）→ 正確目標為 **17→19**。另自查：**`_block_strip` 已在 ns**（:8436）、**`_oblique_s_max` 已在**（:8440）→ 本波僅需新增 2 名。

---

### 2.1 🔴 BLOCKED-2：方位契約須釘死（reviewer 活抓）

右側帶**數學已驗正確**（reviewer 獨立實測：與 `wf_f4` 右支既有式 symdiff ≤1.2e-8㎡·六塊；成立之理由＝`_block_strip` 之 `n_hat` 取自 `allocation_dir` **非** `d_hat`〔`app:6756-6765`〕，故 `d̂→−d̂` 只改繞向不改帶；且 `_oblique_s_max ≡ _strip_s_range.s_max` 六塊逐位 ⇒「step0 後 amp==s_max」成立）。

**但簽名未規定方位契約** → `wf_f4:1128-1129` 局部 scope 已放著 **reversed 對**（`corner = p1 + s_max·d̂`／`dh = −d̂`），順手傳入是最自然寫法。reviewer 實測若傳 reversed 對：R1/R3/R6 之帶**整個跑到 p1 端**（錯側）＝ #25 全額重演。

**釘死**：docstring 明載「`corner_pt`／`d_hat` **一律**傳 FRONT_LINE 之 `p1` 與 `+d̂`，**兩側皆同**；端之選擇**只由 `side` 決定**」＋ 函式內 `assert`（`side=='right'` 時斷言 `s_max>0` 且 `abs(s_min)<abs(s_max)`，可辨識反向傳入）。

### 2.2 其餘 reviewer 更正（全數採納）

| # | 更正 |
|---|---|
| 1 | **`wf_f4` 右側除法在 `1130`·非 1128**（1128＝`corner = p1 + _smax_f4·d̂`）——step 0 插入後漂 2 行；**plan 與 CC recon 皆載錯**（CC 已自驗坐實） |
| 2 | **「刪 f(0)==0」之<u>理由</u>錯（結論仍對）**：`_block_strip` 於 `S<=0` 直接 `return None,0.0`（`app:6750-6751`）→ **f_band(0) 恆為 0**（pre/post-step0 皆然）。`78.24` 係 **buf=0 時之池片**（帶`[amp,s_max]`＝p2 楔形）·**非** f_band(0)——CC 原文把 band 誤當 pool piece（與 BLOCKED-1 同一混淆·#25④）。改述為「**恆真式故刪**」；錯理由禁留（下一波會引為依據·#26(a)） |
| 3 | **R3 錨敘述更新**：CC 引「現值 389.85」係 **pre-step0 複合**（帶 311.61＋p2 楔形 78.24）；step 0 已落地 → **post-step0 R3 帶實測 235.017**、楔形歸 0。禁以複合物之數指涉其組件（#25④） |
| 4 | **0m 全無 forced**（forced 全集＝**僅 3.5m** 之 `R2-left／R5-left／R3-right`）→ 閘② **只在 3.5m 有意義**；報「雙情境全綠」時 0m 半屬**空集合真值**（`all([])==True`·#15③）→ 閘敘述須明寫 **「0m N/A」**，禁令其冒充舉證 |
| 5 | **W-8 夾 0 於本波恆不觸發**（R2/R5 之 `s_min` 皆正；`s_min<0` 之 R1/R6 **非 forced**）→ 夾 0 是「有寫沒被證」之分支（#18④ 死碼教訓）。**改靜默夾 0 為 loud**：`side=='left'` 且 `s_min<0` → warn/raise「p1 楔形須先由 §4 N0-20 切出·band 不得夾 0 靜默吞差」 |
| 6 | **恢復 plan §8 之中央池 WATCH**（CC recon 漏列）：`app:6053/6056` → `_corner_off_L/R` → **中央池以 range 記帳**，而 `_pool_total_blk` 為真幾何（現況中央池低估 R5 −87.68／R2 −75.26㎡）；§3 落地後 band==range 該帳方一致。**守恆不受影響**（`_resid_wd2` 只吃真幾何·`_corner_off` 不入守恆式） |
| 7 | **`wf_f1` right 鷹架將是死碼**：`wf_f1:195` 硬釘 `lbl="R1"`，而 R1 兩情境**兩側皆非 forced** → 該檔 buffer 恆 0、補 right 永不執行、**無法被閘證**。依 #18④「只准記已驗證生效者為根治」→ 明標 **unexercised**，或補合成 fixture；**禁**計入「機制已修」 |
| 8 | **建議加靜態閘**（現全庫無任何閘擋「四處之一偷留 `/ avg_depth`」——`run_verification:1110` 之 ns 集合差是**自我跟隨**、對 #20 漂移零效力）：四檔 `"/ avg_depth"` 計數 ==0 且 `_corner_buffer_S` 計數 ≥1（同 `run_verification:1173-1185` 既有靜態越界閘型）。另 `:1111` 訊息字面 `"ns 16 真符號不全"` 為**已過期死字串**（17 時即過期）→ 順修 |
| 9 | **單調性 reviewer 已獨立雙側復現**（6 塊×**兩側**×4000 點·遞減 0）——原 plan 採認之 v2 證產自**未 side 參數化**式（左原點）·對右側嚴格零舉證力（#25①）；今右側亦證 ⇒ 採認成立、bisect 前提安全。plateau（R1-left 14／R6-left 161 段）全在飽和尾段、不落目標區（f(hi) 4368.60/4150.21/4206.80 ≫ range 309.05/300.52/308.93）→ `f(hi)<range → loud raise` 不誤觸 |

### 2.3 ⚠️ buf 有**三條**消費路徑（reviewer 補·CC recon 只當幾何局部修）

1. **宗起點**（`app:15447`／`stepg:501`）
2. **W₀ → Rw → G**（`app:15450-15451` `_W_prev_left = buf·cos_dn`；`stepg:681-692` `_mp_base_W0(_gs,_buf,…)` 之 `_bp0 = _gs + buf·d̂`）
3. **`_select_pool_slot` 理論 ΣRw → k\***（`stepg:701-707`）＝**離散**輸出；buf 由 ~7.04→~8.72 足以**翻 k\***、令中央池換位

⇒ §3 **非幾何局部**，會走進 Rw/G 並可能改變一個**組合選擇**。**§7 歸因閘須涵蓋此三路徑**；只驗 band≡range 蓋不住。

**CC 對 reviewer 一項之更正（雙向紀律·#21⑤）**：reviewer 稱「`app:15450` 未遷 W 正典 → N0-16 已破·§3 會令 G.3 必翻」——**CC 自驗駁回其嚴重性**：`solve_G_binary` 明載「**W_prev（外層 thread）自此不入 W 計算**（保留簽章·回傳 'W_far' 供既有 thread）」（`app:7170`）⇒ `_W_prev` **post-W脫鉤 為 vestigial**、不入 W/G ⇒ app/stepg 該行之差**不影響 G、不威脅 G.3 byte-perfect**。惟 `app:15450` 續算已作廢值**確屬清理標的**（且易誤導後波），列 backlog、非 §3 阻斷。

---

## 2.4 🔴 停機③（S0d 閘活抓·**pre-existing bug·非 §3**·根因已定·CC 自驗）

§3 reviewer 實跑真 `run_step_g` 撞出 **R2 停機③（守恆-帳幾何級破）**：`|Σ(G−幾何)|=0.28[0m]／0.29[3.5m] > 上界 0.225=15宗×0.015`（我 S0d 閘寬）。CC 逐層自驗**定根因**（非 reviewer 說詞·非「待重烤和解」）：

- **非 §3**：0m R2 **非 forced**、§3 碼從不執行，仍 0.28 → 與 §3 無涉。
- **非 double-rounding**：R2 owner 15 宗逐宗 `|G−cut_coords面積|` **全 ≤0.012**（max 628-52 0.0119）·Σ(G−cut)=+0.0124 ← 極小。
- **真因＝`area≥0.5` 濾網雙計**（`stepg:742`＝`app:15811`·#20 對）：建 `allocated_polys`（池之 owner 集）時 `if _p.area >= 0.5` **剔除合法小宗 `628-43(1)`**（G=0.26·cut=**0.2681㎡**·<0.5）→ 該宗 s 區間**未從池扣除** → 池吸收其 0.2681 → **在 ΣG（列為 owner）與池（列為未分配）雙計**。
- **算術定錨**：`_resid_wd2 = ΣG + 池 − 街廓 = (ΣG−Σowner_cut) + 628-43_cut = 0.0124 + 0.2681 = 0.2805 ≈ 0.28` ✓（逐位）。
- **潛伏數波·S0d 照出**：舊閘 `0.005×深度×15≈3.5` 遠寬於 0.28 → 藏；S0d 收至 0.225 → 露。**＝#21「原理閘照出潛伏 bug」正例·S0d 閘寬正確、非過緊**（0.28 非 irreducible 殘差·係真 bug）。
- **附帶**：`停機③` raise 訊息字面仍載舊式 `(0.005×深度43.90＋tol＋0.005)` 但值用 0.225（我 S0d 改值未改該字串·同 `_acct_geom_tol_block` docstring 之漂移）→ 順修。

**修已施＋驗（KL 2026-07-20 收此區·兩約束照驗·待 KL 複驗 diff）**：
- **約束2（#26a·先核 0.5 之職）✅**：`0.5` 係 `1b290e4 初始遷移`（零歷史）遺留·**無註解、無記載之職**；退化守衛係 **`len≥3`＋`is_valid/buffer(0)`＋`is_empty`**（與 0.5 相互獨立）→ 0.5 純 sliver-area 濾·**非退化守衛**·安全廢。
- **約束1（判準對齊 ΣG 成員）✅**：改「凡 `left_results+right_results`（＝ΣG 成員）之 owner cut，只要 valid 非空即入 `allocated_polys`」（**廢 area≥0.5**·非「改小」）；ΣG 成員若無可扣幾何（退化/失敗）→ **loud print `🔴 停機③-家族`**（no-silent·防靜默雙計）。
- **兩處同改（#20·byte-identical）**：`app.py:15811`＝`stepg:742`；殘留 `area>=0.5` 於 allocated_polys grep **0**（`15698/638` 之 `area_geom>=0.5` 係 retry-acceptance 別義·未觸）。
- **順修** `停機③` raise 訊息之過期字串（`0.005×深度…` → `tol 0.01＋G捨入 0.005`·S0d 後）。
- **驗（實跑）**：`run_step_g` 0m/3.5m **皆無 raise**；R2 殘差 **0.28 → +0.0200**（≪ 上界 0.225）·雙計 0.2681 已除。py_compile app/stepg 綠。
- **此屬 S0d 收尾（非 §3）·已 push 至 wip 供 KL grep 複驗**（KL 只驗 push 之碼·工作區 diff 不採信）。

**§3 之一 WATCH（KL 複驗給·非阻斷·CC 待辦）**：app/stepg 之 `_corner_buffer_S` 呼叫端外層 `try/except (TypeError,ValueError)→0.0`（四處）——若 range 值型別壞會**靜默跳過該街角**（實務前有 `is not None/!=inf` 擋·極罕觸·但嚴格係靜默路徑）。**CC 待改 loud/收窄**（no-silent-fallback）·bundle §4 前置或另小 commit。

---

## 3. §3 驗收閘（**禁套套邏輯**自查·plan §7）

| 閘 | 判準 | 病灶未修時是否已恆綠？（#21/BLOCKED-0 自查）|
|---|---|---|
| **band≡range** | forced band 實際幾何面積 == range（0.01·N0-10）| **否·現在就紅**：錨源＝`F.0_G值` 抵費地列「幾何面積(㎡)」（`_pool_strips_for_block` **真實產物**）；現值 R5 212.84／R3 389.85 皆 ≠ range → 有鑑別力 ✓。**禁**用 helper 內部收斂值（＝套套邏輯） |
| **buffer_S′ 錨** | 命中 post-step0 實值（±0.001）| **錨 post-step0 重取**（BLOCKED-2）：v2 之 R3右 `5.2719` 係 pre-step0、已作廢；**禁湊 5.2719**（＝回 #25）。錨取重烤後 `F.0` 抵費地列實際值·**必含右側**（單點左側錨對 side 維度零舉證力） |
| **身分鍵** | 以 **s 區間**認 forced 帶 | `{blk}-抵費地-{i}` 序號係面積遞減 artifact（`_pool_strips_for_block` 回傳序）·**禁裸序號指涉**（W-6／N0-19／#25④）|

---

## 4. §4 N0-20 recon 狀態（**未起·次一步**）

已定位落點（未細讀）：`wf_f1` 之 R1 楔形機制＝`WEDGE_AREA_ANCHOR=5.30`（:31）／`_fuse_strict`（:46）／`_fuse`（:290）／bisect `fuse(strip(S′), wedge).area == G_B`（:284-306）；**R3/R6 楔形＝標記制·零幾何動作**（:10）。

**待 recon（施工前必補）**：
1. **末端 ALLOCLINE 半平面**之幾何源（補丁七 §一：過 FRONTLINE 末端點·法向＝ALLOCLINE 方向；**禁正投影/質心判別**）——app 內 ALLOCLINE／FRONTLINE 端點之現有取得路徑。
2. **末端帶**＝末端 ALLOCLINE 向內平移「畸零地寬」（查表·禁 3.5）之平行帶構造。
3. **勝者規則**投影排序是否複用 `_projection_order`（plan §4 列為 reviewer 待決）。
4. **標記制→通式之爆炸半徑**：R3/R6 現零幾何動作，改通式後動 F.4 遞補錨 → 須跑 **W-D.4 遞補錨回歸閘**證不越權（#24-1「正典條文只在其落點適用」之教訓：越權改動爆炸半徑大一個數量級）。
5. 與 §3 之 **W-8 邊界對齊**：left band 之 `s_min<0` 段判別**改用末端 ALLOCLINE 半平面**（非 `s<0`）→ 該段歸 N0-20、不歸 forced band。

---

## 5. 🚩 上呈 KL（域裁·reviewer 明示不拍板·施工前須裁）

1. **§3 落地之 band 增量＝`+236.859㎡`（毛量）**——KL 質疑 236.9 之推導基礎（是否含 §2/§4/0m），**CC 實跑坐實如下**（`probe_forced2.py`·本倉 HEAD `ca4985e` 實跑·非憑記憶）：

| 情境 | 側 | range | s_min／s_max | 矩形 buf | **現碼帶（實測）** | **Δ(現碼−range)** |
|---|---|---|---|---|---|---|
| 3.5m | **R2 left** | 309.050 | s_min=**+0.2677** | 7.0399 | 233.788 | **−75.262** |
| 3.5m | **R3 right** | 308.930 | s_max=96.8032 | 7.0791 | 235.017 | **−73.913** |
| 3.5m | **R5 left** | 300.520 | s_min=**+0.2685** | 6.6723 | 212.836 | **−87.684** |
| **0m** | — | — | — | — | **無 forced（全空）** | **0** |
|  |  |  |  |  | **Σ** | **−236.859** |

**KL 之 162.94 ＝ 75.262＋87.684 ＝ 162.946 ＝ 左側二塊（R2＋R5）小計**；差額 **73.913 ＝ R3 <u>右</u>側**。

**四問逐答（皆實測·非推論）**：
- **是否毛量？** **是**——236.859 ＝ Σ(range − 現碼帶) 之**毛增量**。⚠️ **中央池之淨變動 ≠ −236.859**：buf 另經 **W₀→Rw→G** 路徑（`app:15450-15451`／`stepg:681-692`）改 ΣG → 池依 `ΔΣ池=−ΔΣG`（閘⑤）連動。**精確淨值須待重烤**，不可先報為淨額。
- **是否含 step-0 楔形？** **否**。R3 右帶係以 **post-step0 原點 `s_max`** 量得（`p1+s_max·d̂`）；step 0 之效（p2 楔形 78.24→0）已於 `02eb4c2` 落地、**係另一量**，不在此 236.859 內。
- **是否含 N0-20 p1 楔形？** **否**。p1 楔形在 `s_min` 端；R2/R5 之 `s_min` **皆為正**（+0.2677／+0.2685·根本無 p1 楔形），R3 之 forced 側為**右**（`s_max` 端）、不觸 `s_min`。
- **是否含 0m？** **否**。0m **全無 forced**（probe 該段全空）→ 236.859 **全屬 3.5m**。

**故 R3 右之 73.913 係<u>純 §3 效應</u>**（右側矩形近似 `range÷depth` 之短留），**非 §2/§4**——檔:行：右側病灶 `app.py:15349`／`stepg:429`／`wf_f4:1130`（皆 `range ÷ avg_depth`），與左側 `app.py:15342` **同一病灶式、只是側別不同**。
> ⚠️ **若以 162.94（左側 only）認知，等同把右側排除在 §3 之外——正是 #25 的形狀**（右側維度被漏算）。§3 side-參數化之全部意義即在此側。

**待 KL 裁**：此 236.859（毛）之歸屬移轉係**「法定 range 本該如此·矩形近似一直少留」**照實落地，抑或需就財務/分配影響另裁？（守恆不破——`_resid_wd2` 只吃真幾何。）
2. **`s_min < 0` 之 left forced 歸屬**（p1 楔形入 band 抑或歸 §4 N0-20）＝**波次歸屬/域裁**。現況惰性（`s_min<0` 之 R1/R6 **非 forced**），但 §4 若改變 forced 名單即承重。plan §2 W-8 與補丁七 §五指向「歸 N0-20」，惟 **§3 先落地時之中間態語意未定**。
3. **§3 是否可能翻 `k\*`**（buf→`_select_pool_slot` 理論 ΣRw·離散輸出）→ 中央池換位。屬 **W-D.2 既有裁定域**之跨波架構取捨。

## 6. 送 reviewer 之問（§3·**已回·全數採納**，存查）

1. **side 參數化是否真封住 #25**：右側以 `s_max` 為原點、`[s_max−buf, s_max]` 是否確為右組實際 forced 帶（對照 `wf_f4:1128` 右支 `corner + buf·dh` 之等價性）？
2. **W-8 夾 0**（`max(s_min,0)`）於 §4 未施工前是否安全——`s_min<0` 段暫留池、待 §4 收歸 N0-20，中間態是否破 ①' 覆蓋閘？
3. **band≡range 閘之錨源**是否確非套套邏輯（`F.0` 真實產物 vs helper 內部收斂值）？
4. `_WF_NS_NAMES` 16→18 是否漏（`_block_strip` 是否已在 ns？`_oblique_s_max` 已在？）。
5. 單調性採認（不重證）＋端點 assert 是否足夠。
