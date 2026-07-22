# W-G.4 §4 波末：628-37(1) 守恆破 pinpoint（純診斷·勿改引擎/勿烤/勿收綠）

> bisect 收斂至 **{S0d `ca4985e`, §3 `5b80f9d`}**·§3 為機制主嫌（直改 wf_f4 reshape）。**揭「哪個幾何/量法才對」＝域判斷 → 停機上呈 KL／claude.ai。**

- 日期：2026-07-22；branch `wip/s1-endpart`（HEAD `5dea5e2`）；承軌A F.4 628-37 停機上呈。

## 一、bisect（worktree + WV_BAKE 跑到 F.4·記 628-37(1) 0m 吞楔形 Δ面積）

| commit | 步 | 628-37(1) 0m | 判 |
|---|---|---|---|
| （凍存 b2166b7 F.4 收官） | 波前 | G_E=272.84·新形=272.84·Δ=−0.003 | ✅ conserved |
| `d0d450d` | W脫鉤 | G_E=273.41·新形=273.41·**Δ=0.0** | ✅ conserved |
| `02eb4c2` | step-0 | G_E=273.41·新形=273.41·**Δ=0.0** | ✅ conserved（step-0＝右側 s_max·628-37＝R1 左·合理不動）|
| `ca4985e` | **S0d** | **F.4 blocked**（R2 `|Σ(G−幾何)|=0.28>0.225` 停機③·trunk A fail） | ⛔ 不可測 |
| `5b80f9d` | **§3** | **F.4 blocked**（同 R2 0.28·commit msg 自載） | ⛔ 不可測 |
| `3403ba1` | 停機③修 | R2 修 → F.4 跑 → 逐宗主閘 raise（新閘·此後 628-37 7.9） | — |
| `b4ba9d3` | §4（零行為） | 逐宗主閘 |G−幾何|=**7.9** | 🔴 broken |

- **W脫鉤／step-0 排除**（conserved）。**破在 {S0d `ca4985e`, §3 `5b80f9d`}**。
- **不可直接隔離 S0d vs §3**：二者皆被 **R2 停機③（0.28）** 擋 F.4（該 R2 破係 S0d 閘活抓之 pre-existing bug·3403ba1 方修）；且**逐宗主閘（per-宗）3403ba1 才加**·之前無 per-宗 gate。**KL 令「勿改引擎」→ 不可繞 R2 閘量 S0d/§3。**

## 二、機制（git diff 坐實·§3 為主嫌）

- **§3 `5b80f9d` 直改 `wf_f4` reshape（+15）**：新增 `_corner_buffer_S`·「四處接線：app 左右／stepg 左右／wf_f1 左／**wf_f4 左右**」——即 reshape 之 `buf`（forced 街角帶）。
- **628-37(1) ＝ R1 左側街角地 winner**（frozen：街角地=是·街角側別=左側·第1宗街角 winner 0.5741）→ reshape 之 `buf = _corner_buffer_S(...·left)`。**§3 改 _corner_buffer_S ⇒ 改 628-37(1) reshape buf ⇒ 動其幾何。**
- **S0d `ca4985e`（可能共因）**：改 S 全精度（「推進四處改讀 S_raw」·app＋stepg·**未觸 wf_f4**）→ 經 strip/run_step_g 之 G 重算間接影響。
- ⇒ **§3（直改 reshape 幾何·街角 band）＞ S0d（間接 S 量法）** 為主嫌；惟因 R2 閘擋·未能逐位隔離。

## 三、域判斷（KL／claude.ai·停機上呈）

**「哪個幾何/量法才對」**：628-37(1)（R1 左街角 winner·吞楔形）之 reshape 於本波後 |G−幾何|=7.9——
1. **§3 之側參數化 `_corner_buffer_S`（新街角 band 幾何）** 令 winner reshape 之 buf/strip 位移·G（run_step_g 重算）未跟 → 破？**新 band 幾何是否即正確**（則 G 重算/逐宗主閘須對齊），**抑或 §3 band 移錯了 winner 幾何**（則 §3 有 bug）？
2. **S0d 之 S_raw 量法** 是否令 run_step_g 之 G 定於未捨入 S、而 reshape 幾何用捨入 S → 差（惟該差應 ≤ 捨入量子·非 7.9）？
3. **是非題**：(甲) §3 街角 band 幾何為對·逐宗主閘/reshape-G 對齊即可（技術·非破）；(乙) §3 band 移錯 winner 幾何＝真 bug（須改 §3·惟 KL 令勿改引擎→需解凍）；(丙) S0d S_raw 或他因。

## 四、次步（原文·已由 §五 定案取代）

- ~~隔離 S0d-vs-§3 需繞 R2 停機③閘~~ → **§五已做**（診斷 cherry-pick·不入倉）。

## 五、定案（claude.ai 裁技術修·非域判斷；快查＋S0d 隔離·CC 純診斷）

> claude.ai 裁：**非域判斷**（band 幾何域鎖補丁九·逐宗主閘硬守恆·臨街負擔已在 G 公式）；(乙) 降級為**兩路對齊技術修**。

### 5.1 快查：兩路 `_corner_buffer_S` 實參 **全一致**（非 §3 接線 arg 差）
| arg | stepg（G·:425） | wf_f4（幾何·:1131） | 判 |
|---|---|---|---|
| front_p1 | `corner_pt`＝`_p1_fl`＝`cad.front_lines[blk].p1` | `p1`＝`cad.front_lines[blk].p1` | **一致** |
| range_area | `【左】街角最小面積(㎡)`（raw） | `left_corner_min_area`＝`round(【左】街角最小面積,2)`（`_l_disp_min`→`_fo_min_area`）| **一致（≤2dp）** |
| allocation_dir | `alloc_normal_axis(f3_cad_alloc_dir[blk])` | `alloc_normal_axis(alloc_dir_by_block[blk])` | **一致**（`run_verification:96`：`f3_cad_alloc_dir = alloc_dir_by_block`）|
| block_poly/d_hat/side | 同 | 同 | 一致 |
→ **|Δbuf|≈0（args 同源）·非 §3 之 front_p1/range_area 接線差**。

### 5.2 S0d 隔離（診斷 cherry-pick `3403ba1` R2 修 onto `ca4985e`·不入倉·compile OK）
- **S0d 單（無 §3）→ 628-37(1) `Δ=0.0` conserved**（F.4 baked·`G_E=273.41=新形273.41`）。
- ⇒ **S0d 非兇**（S_raw 假設 refuted）。**§3 `5b80f9d` 為兇**（S0d-iso conserved·b4ba9d3〔含§3〕7.9）。

### 5.3 收斂結論
- **兇＝§3 `5b80f9d`**（bisect＋S0d 隔離定案）。**非** front_p1/range_area/allocation_dir arg 差（5.1 全一致）·**非** S0d（5.2 conserved）。
- ⇒ **§3 之新 `_corner_buffer_S` buf 值**（幾何 bisect·取代舊 `range÷avg_depth`）令 628-37(1)（R1 左街角 winner）之 **E3-reshape 幾何 與 F.4-run_step_g G 重算 不一致**（7.9）——非兩路 arg 差、係**新 buf 值在 F.4 兩階段（E3 整形 vs run_step_g）之套用不一致**。確切不一致點（哪階段用新 buf、哪階段未跟）→ **claude.ai grep 兩路 F.4 用 buf 處＋CAD 坐實 628-37(1) 幾何**·寫定點修。
- 未修前：不動引擎·不烤 F.4·不收綠·G006 錨不動。

## 六、run-time 實測（決定性·claude.ai 令·診斷 dump·不入倉·已還原）

> 診斷 dump 兩路 buf ＋ E3-vs-run_step_g（main tree 加 print·跑 WV_BAKE→F.4·讀·`git checkout` 還原）。**§五之「buf 值差」假設 refuted**。

### 6.1 buf ＝ 0（兩路·**非 `_corner_buffer_S`**）
- wf_f4（幾何）dump：`R1-left range_area(fo.left_corner_min_area)=0.0 buf=0.000000`。
- stepg（G）dump：**未印**（在 `if _fo_left:` 內·R1 `left_forced_offset=False`）。
- ⇒ **628-37(1) 係 winner·無 forced 街角帶·兩路 buf=0**。**兇非 `_corner_buffer_S`／range_area**（claude.ai arg-diff 與 §五 buf 假設**皆 refuted**）。

### 6.2 破在 run_step_g 之**幾何面積**（非 E3·非 G·非 buf）
- **E3 整形 conserved**：`628-37(1) G_B=273.41·tgt_shape.area(E3幾何)=273.4101`（|Δ|=0.0001）→ E3 reshape 幾何無誤。
- **run_step_g 破**（F.4 某 call）：`628-37(1) G(㎡)=291.93·幾何面積(㎡)=284.03·|Δ|=7.90`（a=457.0·S=8.57·累積S=45.85）；**對照 conserved call `G=291.93·幾何=291.93`**。
- ⇒ **task 2 答：幾何動了（291.93→284.03·−7.9）·G 沒跟（守 291.93）**。**7.9 落在 run_step_g 對 628-37(1) 之「幾何面積」計算**（該 call 之切幾何比 G 少 7.9），**非 E3 整形（守恆）·非 buf（=0）·非 G 公式**。

### 6.3 待 claude.ai 定點
- **兇＝令 run_step_g 之 628-37(1)「幾何面積」較 G 少 7.9 之變**（幾何路·非 G 路·非 buf）。§3 `5b80f9d` 於該 call 動了切幾何而 G 未跟？（惟 buf=0·故非 _corner_buffer_S·係 §3 之他改·或該 call 之 s-域/切帶）。**claude.ai grep run_step_g 內「幾何面積」計算處（該宗 累積S=45.85·a=457.0 之切帶）＋§3 對之改＋CAD 坐實 628-37(1) 幾何** → 定確切一步·寫定點修。
- **⚠️ §五「新 buf 值兩階段不一致」修正為：buf=0·兇在 run_step_g 幾何面積計算（幾何動 G 沒跟）·非 buf。**
- 未修前：不動引擎·不烤·不收綠·G006 錨不動。
