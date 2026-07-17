# W-G.4 S1 施工 plan（§N1 buffer 幾何化：矩形近似 → bisect 幾何反解）

> 依據：規格 `§N1`（唯一施工依據）＋ **N0-18a**（KL 2026-07-17 落章）＋ S1 偵察報告 `a74fc28`。
> 基準 HEAD：`a74fc28`（S0b＋S0c 收官·run_all 155 ALL GREEN·病灶原封未動）。
> 範圍：**僅 S1**。**不動** §N2 街角確立（S2）、§N3 targeting（S3）、§N5 下游（S5）。
> **狀態：plan·未動工**——波紀律＝plan → reviewer → claude.ai 獨立複驗 → **KL 確認才動工**。

---

## 0. 標的與量化

**病灶**：`buffer_S = 街角最小面積 ÷ 平均深度`＝**矩形近似**。街角範圍係**真實多邊形**（`_build_corner_range_v2`：
SIDE_LINE 中點＋ALLOC 法向平移＋切 BLOCK＋扣截角），其面積**非** `深度×寬` → 以矩形反解必偏。

**量化（3.5m·實測·N0-10「forced＝range·嚴格等於（不足與超額皆違）」三處皆破·既存）**

| 街廓 | forced 帶實際 | range | 差 |
|---|---|---|---|
| R5左 | 212.84 | 300.52 | **−87.68** |
| R2左 | 233.79 | 309.05 | **−75.26** |
| R3右 | 389.85 | 308.93 | **+80.92** |
| **Σ\|差\|** | | | **243.86㎡ ≈ 17,572,213 元** |

**修法**：`buffer_S′ ← bisect` 使 **`_block_strip(block, d_hat, corner, buffer_S′).area == range`**（tol **0.01**）。

---

## 1. 精度與同源（N0-18a·硬約束）

- **`buffer_S′` ＝ 內部幾何構造參數 → 全精度、不捨入**（**不出報表欄**；forced 抵費地列 `S(m)`＝0.0·`stepg:748`）。
  **禁** `round(buffer_S′, 2)` 進入任何**幾何**路徑。
- **`tol = 0.01`**（幾何精度上限）——**非** `0.005×深度`（(b) 已駁回：**N0-10 為規制量、無差額地價找補可吸收**）。
- **🔴 同源紀律延伸（第四源之預防）**：**推進與實切必同源於同一全精度 `buffer_S′`**。
  - 推進：`left_cum_S = float(_left_buffer_S)`（`app:15396`／`stepg:500`）＝**raw** ✅ 現況已同源。
  - W₀：`_W0_left = (_left_buffer_S * _cos_dn)`（`stepg:504`／`app:15399`）＝**raw** ✅（telescoping **真閘**之來源）。
  - **∴ 現況之幾何路徑本即全精度同源** → S1 只換 `buffer_S′` 之**求值法**，**不動同源結構**。

---

## 2. 修法：單一真相源 helper（**循 T2 前例·禁抄第四份**）

**新增模組級純函式**（置於 `app.py` `_block_strip`／`_pool_strips_for_block` 鄰近·由 `ns` harvest）：

```
_corner_buffer_S(block_poly, d_hat, corner_pt, allocation_dir, range_area,
                 tol=0.01, _label='') -> float
  # §N1：bisect 解 buffer_S′ 使 _block_strip(block_poly, d_hat, corner_pt, buffer_S′,
  #      allocation_dir).area == range_area（|Δ| ≤ tol）
  # 回傳**全精度** float（N0-18a：構造參數·不捨入）
  # range_area ≤ 0 → 回傳 0.0（無 forced）
  # 內建：單調性斷言＋收斂 loud（不收斂＝raise·no-silent-fallback）
```

- **`_WF_NS_NAMES` 16→17**；`run_verification:1111` 標籤 `ns 16`→`ns 17` 同步。
- **四處同步改**（與 T2 之四處**完全同組**）：

| # | 檔:行 | 現況 | 改為 |
|---|---|---|---|
| 1 | `app.py:15291`／`:15298` | `float(_l_min) / avg_depth_default` | `_corner_buffer_S(blk_poly, d_hat, corner_pt, allocation_dir_block, float(_l_min), _label=...)` |
| 2 | `stepg:421`／`:428` | 同構逐字 | 同上（**byte 級對映 app**·N0-16 同源同碼） |
| 3 | `wf_f1:216` | `float(_ma) / avg_depth` | `ns["_corner_buffer_S"](block_poly, d_hat, corner_pt, alloc_dir, float(_ma), _label=...)` |
| 4 | `wf_f4:1121`／`:1128` | `float(fo.get(...)) / avg_depth` | 同上（`_reshape_block` 內·`block_poly`/`d_hat`/`corner`/`alloc_dir` 皆在 scope） |

- **通式·禁寫死**：一律依 `forced_map`（`f3L_forced_offset`）動態；**0m 零 forced → `range_area=0` → 回 0.0**
  → **S1 於 0m 零行為變更**（＝天然回歸閘·見 §4）。**S2 擴為 5 時無縫承接。**

### 2.1 bisect 之定義域與單調性（reviewer 覆核點）

- `f(S) = _block_strip(block_poly, d_hat, corner_pt, S, allocation_dir).area` 於 `S ∈ [0, S_max]` **單調不減**
  （切帶隨 S 只增不減）→ bisect 適用。**須於 helper 內斷言** `f(0)=0` 且 `f(hi) ≥ range_area`；
  `f(hi) < range_area` ⇒ **街廓容不下該 range** → **loud raise**（非靜默夾）。
- `hi` 之取法：`_strip_s_range(block_poly, ...)` 之 `s_max − s_min`（**複用 T2 之 helper**·斜交切線座標·**禁正交投影**）。
- **錨（規格 §N1·施工後須命中）**：**R2左 `buffer_S′ = 8.7157m` → 實切 `309.05`**（＝range·±0.01）。

---

## 3. scope guard（不觸清單）

- **不動** `_build_corner_range_v2`（range 之產生法·S1 只**消費**其面積）。
- **不動** §N2 街角資格／門檻（原生 G）＝**S2**；**不動** forced **名單**（S1 只改**已 forced 者之帶寬**）。
- **不動** T2 之 `_pool_strips_for_block`（forced 帶於 T2 下**已是池 s-帶**·S1 只改其 s 寬之**值**）→ **二者正交**。
- **不動** 推進／W₀ 之同源結構（§1·現況已全精度同源）。
- **不動** `solve_G_binary`（S0c 不重開·N0-18a 明定）。
- **⚠️ WATCH（既存·非 S1 標的·標旗不改）**：`app.py:16215` 之 Rw 診斷讀 **rounded** `_buffer_S` 作 `_w_start`
  **且未乘 `cos_dn`**，而真 W₀ ＝ `buffer_S × cos_dn`（`stepg:504`）→ **該診斷之 `_expect` 本即近似**。
  **屬診斷非閘**（真 telescoping 閘走 `_adv_final['W0_*']`＝raw ✅）。S1 後 buffer_S′ 值變 → 該診斷之偏差量變、
  **但其性質不變**。**列入 §N5／後波之「診斷正確性」backlog，S1 不改**（避免逾越 scope＝#24 之教訓）。

---

## 4. 驗收（②不變量閘＋③預測差量閘）

**py_compile**：`app.py verify/stepg_pipeline.py verify/wf_f1.py verify/wf_f4.py verify/run_verification.py`

**grep 坐實**：四處 `/ avg_depth` 之矩形近似**歸零**；`_corner_buffer_S` 出現於四處＋`_WF_NS_NAMES`；`ns 17` 標籤同步。

**預測差量閘（單次重烤·逐格）**

| # | 閘 | 判準 |
|---|---|---|
| **①** | **0m 全譜系一字不變**（**絕對閘**） | 0m 零 forced → `buffer_S′≡0`≡現況 → **0m 之 baseline 逐格 byte 相同**·一格不符即停 |
| ② | **3.5m forced 帶面積 == range**（±0.01） | R5左→**300.52**／R2左→**309.05**／R3右→**308.93**（N0-10 由破轉綠） |
| ③ | R2左 `buffer_S′` 命中 **8.7157m**（±0.001） | 規格 §N1 錨 |
| ④ | 3.5m 業主宗 G／幾何之位移**逐宗可歸因** | buffer_S′ 變 → 推進起點變 → **下游宗全體位移**（**非** bug·係 §N1 之內生）；須與 `Δbuffer_S′` 一致 |
| ⑤ | **Σ池恆定＝2299.26**（N0-7·3.5m） | forced 帶漲/縮由中央池吸收·**全區池總量不變** |

**不變量閘（②層·絕對）**：①' 覆蓋 0.01／②-池 1e-6／②-宗 1e-6／逐宗主閘／守恆兩級／**N0-10 forced＝range**（新綠）。

**⚠️ 閘④ 之量級預告（reviewer 注意）**：R5左 +87.68／R2左 +75.26／R3右 −80.92 之帶寬變動
→ **該側全體宗之起點位移**（R5左 buffer 由 ~4.7m 增至 ~6.7m 級）→ **3.5m 之 baseline 將大幅重定**。
**此為 §N1 之標的本身、非回歸**；惟**須逐宗可歸因**（閘④），且 **0m 必須一字不變**（閘①）作為對照。

---

## 5. 施工序

1. helper `_corner_buffer_S` 立（§2）＋單調性/收斂 loud → py_compile。
2. 四處接線（app／stepg 逐字同構；wf_f1／wf_f4 經 ns）＋`_WF_NS_NAMES` 16→17＋`ns 17` 標籤。
3. **0m 先驗（閘①·絕對）**：run_verification 之 0m 全段**逐格 byte 相同** → 破即停（證通式未誤傷零 forced 路徑）。
4. 3.5m 驗閘②③（forced＝range／buffer_S′ 錨）。
5. **PRE 凍存** → **單次重烤** → 預測差量閘①~⑤＋不變量閘全綠 → run_all 綠。
6. py_compile → grep 異動清單對照本 plan → **push**（嚴格 `git rev-parse origin/main` 驗）。
7. 報告入倉 `docs/reports/W-G.4_S1_修漏報告.md`·聊天僅 ping。

---

## 6. 送 reviewer 之設計裁決／WATCH

1. **helper 置放**：`app.py`（ns harvest·同 `_block_strip`／`_pool_strips_for_block` 先例）——**傾向**，求覆核。
2. **`hi` 之取法**：複用 `_strip_s_range` 之 `s_max−s_min`（斜交切線座標）vs 另立——**傾向前者**（單一真相源）。
3. **`f(hi) < range_area`（街廓容不下 range）之處置**：**loud raise**（傾向）vs 夾至 `hi`＋warn。
   **傾向 raise**：夾即靜默違反 N0-10（且 N0-10 無吸收機制·N0-18a 已明）。**本案不觸發**（三塊 range 皆 < 街廓）。
4. **閘④ 之「逐宗可歸因」判準**：以 `Δ起點 == Δbuffer_S′` 逐宗驗（傾向）vs 僅驗總量。
5. **WATCH**：`app.py:16215` 之診斷（§3）——**S1 不改**，求覆核此界線是否正確。

**本 plan 之 KL 域裁題：無**（N0-18a 已裁定精度與 tol；N0-10 之「嚴格等於」不因量子而鬆）。
若施工中撞出未涵蓋之真實違規（如某塊 `f(hi) < range`），**§N8 停機上呈**。
