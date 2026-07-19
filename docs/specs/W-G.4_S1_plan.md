# W-G.4 S1 施工 plan **v3**（端部機制段·八項一次重烤：W 脫鉤＋step 0＋街角 band＋N0-20 末筆＋S0d＋查表化＋歸因閘）

> **v2 經 reviewer 退回 BLOCKED×5**（`7df38fe`）→ 本 v3 依 **KL 2026-07-17 補丁六**（W 正典＋首宗下限＋R4 裁＋查表化＋歸因閘）＋補丁五（N0-20 端部機制）全面改寫。
> 依據：規格 **W 正典**（§一.4 δ 精確式·CC 已內積驗證·見下 §1 註）／**N0-20**／**首宗下限**（補丁六 §二）／**R4 態樣**（§三）／**查表化**（§四）／**S1 G 重定歸因閘**（§五）／**§N3-0e S0d**／**§N1**／**N0-10**。
> 基準 HEAD：`5b479b6`+（補丁六＋δ 驗證入倉同 push）。**行號已依 `5b479b6` 全數重驗**（`a74fc28`→`5b479b6` 間無碼 commit·見 §0.1）。
> **狀態：plan v3·未動工**——波紀律＝plan → **reviewer 自動路由**（CLAUDE.md 已立·不停等 KL）→ claude.ai 複驗 → **KL 確認才動工**。
> **範圍：八項端部機制段·一次重烤**（補丁六 §六·權威清單）。**不動** §N2 名單（S2）／§N3 targeting（S3）／§N5 下游（S5·範圍隨 step 0＋N0-20 收縮）。

---

## 0. v2 → v3 之變更（BLOCKED×5 全數處置＋補丁六新增四項＋δ 發現）

| v2 之死因／缺 | v3 之改 |
|---|---|
| **BLOCKED-1** step 0 只消 R3 之 p2 楔形；R1/R6 楔形在 **p1 端**（`s_min<0`·`actual_max_proj` 碰不到） | **端型二分（補丁六 §六）**：**p1 端＝N0-20 末筆機制**（§4·非 step 0）／**p2 端＝街角+step 0**（§2-3）。step 0 **僅右組 s 域**·**不再宣稱消三楔形** |
| **BLOCKED-2** 閘③ R3 錨 `5.2719` 被 step 0 作廢（→`8.7290`） | **閘③ 錨 post-step0 重取**（§3·錨＝重烤後 `F.0` 抵費地列·非 pre-step0 值）；**禁湊 5.2719**（=回 #25） |
| **BLOCKED-3** 閘①「G 一字不變」為偽（0m 態 G 仍動 +8.19） | **閘① 失效並重立為 S1 G 重定歸因閘**（補丁六 §五·§7）——G 全數重定係四項落章之必然 |
| **BLOCKED-4** step 0 漏 `wf_f4:1124-1126`（第三處） | **step 0 三處同步**（§2·含 `wf_f4:1124`·verified） |
| **BLOCKED-5** ΔΣ池 基準 `2299.26`（pre-S0b/S0c） | **基準＝倉態 2298.80（3.5m）／2378.01（0m）**（§7·`d9a8b05`·引身分） |
| （v2 無）W 脫鉤 | **§1 W 脫鉤重構**（W 正典·直算 mp→遠側界線垂距·脫鉤碼 telescoping） |
| （v2 無）首宗下限／R4 | **§1 首宗 W 下限 loud 規制（≥7）＋R4 單街角宗態樣記錄** |
| （v2 無）N0-20 末筆機制 | **§4 R_end 構造＋勝者規則＋常數項 bisect** |
| （v2 無）查表化 | **§6 全庫寫死 3.5 → `get_min_lot_size`**（盤點三分類） |
| **W-1~W-8**（reviewer WARNING） | 逐項處置（§各節·行號重驗／`_WF_NS_NAMES` 16→18／S0d 下游位移據實陳述／`W_far` 量化退路徑／閘② 身分鍵／`wf_f1` right 全鷹架／N1 左帶吞 p1 楔形） |

### 0.1 行號重驗（跨波必重驗·v2 之 6821 教訓）
`git log a74fc28..5b479b6 -- app.py verify/stepg_pipeline.py verify/wf_f1.py verify/wf_f4.py` = **空**（僅 docs commit）→ 碼行號自 `a74fc28` 未動。本 plan 所引行號皆已於 `5b479b6` `sed -n` 逐一坐實（見各節「✓verified」）。**⚠️ v2 之 `app:6821` 已作廢**——實切在 **`app:7209`**（`_S_cut = round(S_conv, 2)` ✓verified）。

---

## 1. 項① W 脫鉤重構（W 正典）＋首宗下限＋R4 態樣

**病灶**（`app.py:7143-7155` ✓verified·`solve_G_binary` 內）：
```python
W = W_prev + S_guess * _cos_dn          # 7147：telescoping·W_prev 由群起點 thread、首宗=0
Rw = rw_increment(W_prev, W)            # 7148
```
註 `7141`「不可從 SIDE_LINE 中點絕對量」＝**舊 (ii) 語意·W 正典已推翻**。此式**寄生於 S 累積器**（虛胖陷阱）。

**改法（W 正典·直算）**：`W_i ＝ mp → 第 i 宗遠側分配界線之垂距`（獨立幾何量測·脫鉤 S 累積）。**等價最小改動＝群起點 `W_prev` 初值由 `0` 改 `(群起點 − mp)·â_定向`（＝ −δ_block）**，其後 telescoping 照舊 → W 即成「自 mp 絕對量」。
- **δ_block ＝ (mp − 群起點)·â_定向**（**CC 已內積驗證·六塊 |Δ|≤0.006**·報告 §7·`delta_unified.py`）：群起點＝右組 `end_pt=p1+amp·d_hat`（`stepg:576`）／左組 `p1`；â_定向＝`alloc_normal_axis(alloc_dir)`（`app:5158`）沿群推進入街廓向定號（`adv·â>0`·adv=+d_hat 左／−d_hat 右）。
- **⚠️ W 為 intrinsic（reference-free）**：KL W＝perp dist mp→實際遠側界線·**與群起點/amp 無關**（step 0 改 group_start 時 cum_S 補償·KL W 不變）。故 **item① 與 item②（step 0）解耦**——W 量測不受 amp 影響。**施工須以此為準：直量實切遠邊到 mp 之垂距**（非賭 group_start）；`−δ_block` 初值法僅為「與現 telescoping 架構相容之等價實作」·**須以六塊 δ 錨驗證**。
- **零區（補丁六 §一.3）**：`R(W≤0)＝0` **碼已具**（`rw_from_width`·`app:5134` `if W <= 0: return 0.0` ✓verified〔reviewer 更正 5127→5134·5127 為 docstring〕·`W≥18→100%` `app:5138` ✓）→ **item① 無須改零區·僅確認 W 脫鉤後首宗 W 可為負而正確歸零**；`Rw=R(W_i)−R(W_{i−1})`·`ΣRw=R(W_末)−R(0)` 閉合。

**首宗下限規制（補丁六 §二·裁「行」·自由解非恰等）**：
- 達資格之街角首宗 `W₁ ≥ 側街退縮 ＋ 最小畸零寬`（本案 ≥7·查表 §6）——**碼中 loud 下限規制**（`W₁ < 下限 → 記錄/警示`·**禁硬釘 =7**）。
- **恰等於 range** 僅「皆不達資格 → forced band=range」路徑（§3）。
- 驗收斷言：重烤後首宗 KL W **≥7**（現值 6.92＝pre-重烤 artifact·報告 §2）。

**R4 單街角宗態樣（補丁六 §三·裁 (a) 照實·loud）**：
- R4 街角側僅一宗（`628-1(1)`）·`W=13.98<18` → `ΣRw<100%`（碼 90.57%／KL 87.74%）→ **缺口由全區財務平衡吸收·不塊內歸一化·不重定影響帶**。
- **🔴 ΣRw 驗收斷言（補丁八 §一/§五·乙定案）＝「ΣRw 閉合」<u>不再列驗收斷言</u>**：ΣRw<100% 於**負 δ 塊（首宗 W₀=mp→corner>0）＋forced 帶＋單宗<18** 皆為誠實結果（W脫鉤打樣實測：R3右 0m 77.34/3.5m 34.75·R1左 97.20·R2/R5左 3.5m 54/56·R4 87.81）——**改列「負δ塊 ΣRw<100% 且 `ΔΣ池=−ΔΣG` 對帳」**（缺口內含吸收於池·池不會負）。**禁 clamp 首宗 W₀ 回 corner**（甲案＝#26 虛構法源·作廢）。
- **WATCH**：N0-20 端部機制施後 R4 末端處置是否吸收此殘（§4）。

**W-4 處置**：`W_far=round(W_conv,2)`（`app:7240` ✓verified）＝一長度量化仍在 W→Rw→G 路徑 → 影響 §7 歸因閘殘差寬（列量子項·量化×深度）。

---

## 2. 項② step 0：amp 正交→斜交（**僅右組 s 域**·三處同步）

**病灶**：推進域用**正交**投影 `actual_max_proj = max(dot(v − corner_pt, d_hat))`（三處 ✓verified）：`app:15475`／`stepg:573`／`wf_f4:1124-1126`（BLOCKED-4 第三處）。而池域用斜交切線座標 `s_max`（`_strip_s_range`·`app:6892`）→ 右組終點 `end_pt` 位移 → R3 之 p2 楔形 `78.24`。

**改法**：`actual_max_proj` 改用**斜交切線座標 `s_max`**（＝`_strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)` 之 `s_max`·複用 T2 helper·斜交式·禁正交）。**三處同步**（禁抄第三份漂移·#20）。

**⚠️ 範圍收縮（BLOCKED-1 修正）**：
- step 0 **僅界定右組 s 域終點**（`end_pt`·`d_hat_rev`）→ **只消 R3 之 p2 楔形（78.24）**。
- **R1/R6 之 p1 端楔形（5.33／85.71）＝N0-20 領域（§4）·非 step 0**（`s_min<0`·左端·`actual_max_proj` 物理碰不到·reviewer 已證 `app:15475` 於左組迴圈外）。
- **v2 之「step 0 消三楔形」宣稱作廢**；閘僅斷言「**R3 p2 楔形 → 0**」（§7）。
- **side 參數化仍不可省**（#25·末端真楔形不因 step 0 消·通式不得賭單側退化）。

**W-8 處置**：N1 左帶 `[s_min, buf]` 於 `s_min<0` 會吞 p1 楔形——現 forced 左側僅 R5(+0.27)/R2(+0.27)（不觸發）；**S1 left band 須夾 `[max(s_min,0), buf]` 或明示 p1 楔形歸 N0-20**（§4·與 §3 left band 邊界對齊）。

---

## 3. 項③ 街角 forced band：buffer_S′ 幾何 bisect（**side 參數化**·單一真相源）

**病灶四處 ✓verified**（矩形近似 `buffer_S = range ÷ avg_depth`·#20 同族）：`app:15291/15298`／`stepg:421/428`／`wf_f1:216`（**無 right 分支**·BLOCKED-2/W-7）／`wf_f4:1121/1128`。

**新增模組級純函式**（`app.py` `_pool_strips_for_block`〔`app:6917` ✓verified〕鄰近·`ns` harvest）：
```
_corner_buffer_S(block_poly, d_hat, corner_pt, allocation_dir, range_area, side,
                 tol=0.01, _label='') -> float           # 全精度回傳（N0-18a）
  # bisect 解 buffer_S′ 使**真實池帶**面積 == range_area（|Δ|≤tol）
  #   side='left'  → band = block ∩ s∈[max(s_min,0), buf]      ← W-8：夾 0·防吞 p1 楔形
  #   side='right' → band = block ∩ s∈[amp − buf, s_max]       ← step 0 後 amp==s_max
  #   s_min/s_max ← _strip_s_range（斜交·與 _pool_strips_for_block 同源）
  #   range_area ≤ 0 → 0.0（無 forced）
  #   刪 f(0)=0（恆真·右側 f_true(0)=78.24≠0 誤停）；留 f(hi)<range_area → loud raise
```
- **單調性**（reviewer v2 已證·採認）：strip(S₁)⊆strip(S₂)·集合包含·斜交亦成立（6 塊×4000 點·遞減 0）→ bisect 適用。
- **⚠️ 錨 post-step0 重取（BLOCKED-2）**：v2 之 `R3右 5.2719` 係 pre-step0·**step 0 後位移至 `8.7290`**。**閘③ 錨改＝重烤後 `F.0_G值` 抵費地列之實際 buffer_S′**（非 pre-step0 硬值·**禁湊 5.2719**）；**必含右側**（#25·R2 左之 8.7157 對 side 零舉證力）。
- **band≡range 幾何比對閘**（0.01·N0-10）：錨源＝`F.0_G值` 抵費地列「幾何面積(㎡)」（`_pool_strips_for_block` 真實產物·**禁 helper 內部收斂值**＝套套邏輯）；**身分鍵**（W-6）＝以 **s 區間** 認 forced 帶（`{blk}-抵費地-{i}` 係面積遞減 artifact·`app:6934`·禁裸序號）。

**四處同步**（T2 同組）：
| # | 檔:行 ✓verified | 改 |
|---|---|---|
| 1 | `app:15291/15298` | `_corner_buffer_S(..., side='left'/'right')` |
| 2 | `stepg:421/428` | 同上（byte 級對映 app·N0-16） |
| 3 | `wf_f1:216` | 同上·**補 right 全鷹架**（`end_pt`/`d_hat_rev`/`max(proj)`·非只加變數·W-7） |
| 4 | `wf_f4:1121/1128` | 同上（`_reshape_block` 內·side 已在 scope） |

- **`_WF_NS_NAMES` 16→18**（W-2·非 17）：`_strip_s_range`＋`_corner_buffer_S` 皆須入 ns；`run_verification:1111` 標籤／`_wf_ns()` docstring（`app:8403`）同步。

---

## 4. 項④ N0-20 末筆機制（p1 端·R_end 構造＋勝者規則＋常數項 bisect）

**域裁**（N0-20·補丁五 §一）：**p1 端（無 SIDE_LINE）之端部機制**·與街角機制對稱（同族抽象＝端部規定範圍多邊形＋勝者規則＋嚴格等於之抵費地退路）。

1. **R_end 構造（🔴 補丁七 §一/§二·幾何正典·取代原位置語）**：`R_end = 未臨正街土地 ∪ 末端帶`。
   - **未臨正街土地**＝**沿 ALLOCLINE 方向作直線不與 FRONTLINE 相交之區域**（過 FRONTLINE 末端點之「末端 ALLOCLINE」外側·BASELINE 圍成殘區）——**🔴 禁正投影/質心判別**（`ALLOCLINE_1` 圖：質心正投影落 p1–p3 內仍屬未臨正街）。**幾何實作＝末端 ALLOCLINE 半平面 ∩ block**（半平面法向＝ALLOCLINE 方向·過 FRONTLINE 末端點）。
   - **末端帶**＝**末端 ALLOCLINE 向街廓內平移「畸零地寬」之平行帶**（W=S=畸零寬·查表 §6·禁 3.5）。
   - R6 實例 85.71（未臨正街）＋166.57（末端帶）＝252.28㎡（**θ=90° 特例**故 p1–pz 弦長對得上·非通式）。p1 端楔形（R1 5.33／R6 85.71／0m R3 78.19）＝R_end 內部組成·非「碎片」。
2. **勝者規則**：與 R_end 有交集之重劃前土地·依投影排序·**首筆 `G ≥ area(R_end)` 吃下整個 R_end**（端帶＋未臨正街地·一宗到底）；**皆不達 → 末筆為抵費地·面積嚴格 = area(R_end)**。**未臨正街土地不能單獨成一筆**（必併勝者宗或隨末筆抵費地·§二.3）。
3. **常數項 bisect**：勝者之 bisect 改解 `strip_area(S) = G − wedge_area`（＝實配 = p1 起平行四邊形 ＋ 未臨正街地〔常數〕）。**現碼落點**：`wf_f1` 之楔形處理（`WEDGE_AREA_ANCHOR=5.30`〔`wf_f1:31`〕·`_fuse` strip∪wedge〔`wf_f1:47`〕·R3/R6 標記制〔`wf_f1:10`〕）→ **改為 N0-20 通式**（`R_end` 驅動·勝者/常數項）。
4. **與 §3/§2 W-8 邊界對齊（🔴 補丁七 §五）**：left band 之 `s_min<0` 段判別**改用末端 ALLOCLINE 半平面**（非 `s<0`）→ 該段歸 N0-20·不歸 forced band。

**✅ 施工細節已由補丁七關閉**：未臨正街幾何源＝末端 ALLOCLINE 半平面（§一.1·非正投影）。**餘待 reviewer**：勝者「投影排序」是否複用 `_projection_order`；標記制→通式之爆炸半徑（R3/R6 現零幾何動作·改通式後動 F.4 遞補錨·須跑 W-D.4 遞補錨回歸閘證不越權）。

---

## 5. 項⑤ S0d：S0c 修向反轉（實切回未捨入·同源全精度）

| # | 標的 ✓verified | 改 |
|---|---|---|
| 1 | `app:7209`（`_S_cut = round(S_conv,2)`） | **撤 `_S_cut`·回復未捨入 `S_conv`** |
| 2 | 推進（`stepg:545` `_S_actual=res.get('S')`／`stepg:636` 同·`551`/`642` `cum_S += _S_actual`） ✓verified | **`res` 增攜全精度 `'S_raw'`·`545/636` `_S_actual` 改取之·`551/642` cum += 全精度**（行號 W-1 更正確認：541/632→**545/636**·547/638→**551/642**） |
| 3 | 顯示欄 `'S'`（`app:7239` `round(S_conv,2)`） | **照舊 2dp 輸出**（N0-18 顯示） |
| 4 | `area_conv` | **＝全精度實切面積**（`6793` 收斂／`6807` 未收斂**兩路徑皆改**·後者現與 S_conv 不同源） |

- **W-3 據實**：本宗 G 不動（G 定於實切前）✓；但「推進改吃未捨入 S」→ `cum_S` 動 ≤0.005·n → **下游宗 baseline_pt 位移 → S/W/Rw/G 全動**（量小·但**陳述須含此**·非「閘① 不受影響」）。
- **W-4/W-5**：`W_far=round(W_conv,2)` 仍量化（S 之量化未全退路徑·通稱改「**S 之量化退出路徑**」）；`_acct_geom_tol_per_lot` docstring（`app:6818` 待核）之**作廢域框架須刪**（單源函式內留作廢法理＝下輪引用源）。
- **閘寬連動**（單源函式改係數·一處生效）：`_acct_geom_tol_per_lot|_block` → `0.005×深度` 項歸零：逐宗 `≤tol(0.01)+0.005=0.015`；逐街廓 `≤宗數×0.015`；E3 `≤整形宗數×0.005`。**依據＝量子項僅對實在路徑之量化立項**（#24）。

---

## 6. 項⑥ 查表化（補丁六 §四·全庫寫死 3.5 → get_min_lot_size）

**基礎設施 ✓verified**：`get_min_lot_size(category, front_road_width_m)`（`app:7267`）回傳 `{'min_width','min_depth','min_area','table_key'}`（**`min_width`＝欲取代硬編 3.5 者**）；`HUALIEN_MIN_LOT_TABLE`（`app:7252`）**外層 key＝使用分區·路寬選<u>列</u>（tuple[0] 上限）**——**⚠️ 補丁六 §四「表以正街道路寬為鍵」措辭不精確**（外層鍵是分區·非路寬·列記上呈）。

**窮盡盤點（subagent·`3.5` 全庫 74 命中·識別子 12 項·N0-17-c 附後）**——真消費三分類：

**A. min_width 真消費（→ `get_min_lot_size(...)['min_width']`·本波改）**：
| 檔:行 ✓verified | 現碼 | 註 |
|---|---|---|
| **`app:7652/7653/7655`** ★ | `_lmw_raw = _blk_param_B4.get('法定最小寬(m)', 3.5)`＋else/except 兜底 | **★實際生效中**（`f3L_sb_rows_by_label` 全程無人寫入·`selection_pipeline:272` 坐實）→ `select_corner_lots_both_sides_v12` Patch B-4 街角範圍前置篩選之 min_width。**改查表**（分區＋正面路寬）。 |
| §1/§2 之首宗下限畸零寬項 | （新碼·§1） | `≥ 退縮 + min_width`·min_width 走查表·**禁寫死 7** |
| `MinA = min_width × 深度` 之 min_width | （凡硬編 3.5 因子處） | 走查表 |

**B. 側街退縮（補丁六 §四「沿用既有輸入欄」·<u>不</u>查表·惟廢靜默 3.5 兜底）**：
| 檔:行 ✓verified | 現碼 | 改 |
|---|---|---|
| `app:7629/7630/7632` | `_setback_raw = ...get('f3L_setback_default', 3.5)`＋else/except | 退縮源＝輸入欄（`f3L_setback_default`）**保留**；**`, 3.5)` 靜默兜底廢**（no-silent-fallback·W-B `or 3.5` 陷阱）→ 缺值 loud 警示·非編造 3.5 |
| `app:13920` | `number_input` 起始 `get('f3L_setback_default', 3.5)` | 同上（UI 起始預設·弱） |
| `app:16113/16599` | dump／Excel 匯出檔名 tag 讀退縮 fallback | **弱（僅檔名）**·列 WATCH·可留 |

**C. UC9898 凍結／耦合（<u>勿</u>查表化·上呈 KL）**：
- `app:8524` `_wf_tag_of`：`abs(setback−3.5)<1e-9 → "3.5m"`·否則 `raise`（硬對應 UC9898 雙情境 0/3.5）→ **退縮若改查表得非 3.5·此派發須同步處理**（上呈 KL）。
- `verify` 之 `(3.5,"3.5m")` 情境驅動迴圈 6 處（`run_verification:350/422`·`wg_g3:118`·`wd4_tier_list:185`·`wd3_fragment_geom:90`·`y_dump_diff:291`）＝UC9898 凍結雙情境·**勿動**。
- `run_verification:838` `_a["w_new"] >= 3.5`＝F.1 錨閘硬編 min-width 門檻·**改查表或標 UC9898 凍結**（上呈）。

**D. 引擎層已查表化（✓·非本波·佐證方向）**：`wf_f0/f1/f4`·`wd3`·`wd4`·`stepg` 皆已 `ns["get_min_lot_size"](...)["min_width"]` 逐塊查表；app `16729`（判去留寬度）＋`13990-13993`（`f3_min_width_by_label`）亦已查表。**非硬編·非目標**。

**其餘 55 命中**＝註解／docstring／tag 字串／表本體（`7254-7263` 正典值·勿改）／plotly 線寬（`17095` 無關）。

**✅ 補丁七 §五 已裁（保守解·鎖）**：① 退縮＝既有輸入欄＋**loud 兜底**（廢靜默 3.5）·非 min_width 查表值；② `verify:108` param table 單一 global `法定最小寬_m`＋`:838` 門檻 **標凍結**（UC9898·不逐塊查表化）；③ `app:8524` `_wf_tag_of` **維持 0/3.5 雙情境**（退縮不改查表·派發不觸 raise）。

---

## 7. 項⑦ 驗收閘（歸因閘為新絕對層＋不變量閘＋禁套套邏輯）

| # | 閘 | 判準 |
|---|---|---|
| **①→歸因** | **~~業主宗 G 一字不變~~ 失效並重立（補丁六 §五）** | **逐宗 ΔG 須由附件二鏈逐項解釋**：`ΔG ≈ −ΔRw·F·l₁·(1−C)`〔W 路徑·**ΔRw 由 W 脫鉤後新垂距<u>獨立</u>量·非重跑 G solve**〕＋S/幾何路徑項〔step 0 amp／S0d／端部 wedge〕。**殘差寬**依「量子項僅對實在路徑之量化立項」（#24·含 `W_far` 量化×深度·§5）。**無法歸因 = 停機**（第 N 源） |
| ② | **N0-10 幾何比對閘**：forced band 面積 == range（0.01） | 錨 **post-step0** 重取（BLOCKED-2）·**必含右側**·身分鍵＝s 區間（W-6） |
| ③ | `buffer_S′` 命中 post-step0 錨（±0.001） | 重烤後 `F.0` 抵費地列實值（**禁湊 5.2719**） |
| ③' | **step 0：R3 p2 楔形 → 0**（**僅此一楔·非三**） | R3 78.24 → 0（`s 域 ⊂ [s_min,s_max]` 右組 by construction）。**R1/R6 p1 楔形歸 N0-20〔§4〕·不在此閘** |
| ④ | **N0-20 勝者規則＋band≡range**（0.01） | R_end 面積 == 252.28（R6）·勝者宗 G≥area(R_end) 或末筆抵費地嚴格=area |
| ⑤ | **`ΔΣ池 = −ΔΣG` 恆等式閘**（N0-7·散文轉真閘） | **基準 2298.80（3.5m）／2378.01（0m）**〔`d9a8b05`·引身分·**非 2299.26**〕；逐街廓亦恆等。ΔΣG 之量待重烤實測（W 全數重定） |
| ⑥ | **帳對幾何閘收緊**（S0d） | 逐宗 `≤0.015`／逐街廓 `≤宗數×0.015`／E3 `≤整形宗數×0.005` |

**不變量閘**：①' 覆蓋 0.01／②-池 1e-6／②-宗 ≤1e-6（S0d 後）／逐宗主閘／守恆兩級／N0-10（新綠）。

**🔴 禁套套邏輯自查（reviewer 必查·v1 閘②／v2 閘③' 前科）**——逐閘答「**病灶未修時此閘是否已恆綠**」：
- **歸因閘**：預測 ΔRw **獨立於** G solve（W 脫鉤後直接垂距）→ 有鏈外源時預測對不上實際 baseline-diff → 紅（非恆綠）✓。**⚠️ 若預測改由重跑引擎 Rw 得出＝退化恆等式＝恆綠＝作廢**——施工須證預測路徑與 G solve 不共用 Rw。
- **閘③'**：v2 之「`s 域⊂[s_min,s_max]` by construction」在楔形還在時**今天就真**（`app:6984-6990` 無條件夾）→ **零舉證力**（BLOCKED-0 教訓）。**v3 改斷言「R3 p2 楔形面積 78.24→0」**（一具體幾何量·病灶在時 =78.24·修後 =0·有鑑別力）。
- **②/N0-10**：錨源 `F.0` 抵費地列為真實產物（R5 212.84／R3 389.85 皆≠range → 現在就紅·有鑑別力）✓·非套套邏輯。

---

## 8. scope guard

- **不動** `_build_corner_range_v2`（range 產生法·S1 只消費面積）／§N2 名單（S2）／§N3 targeting（S3）。
- **不動** T2 `_pool_strips_for_block` 建構法（step 0 令 s 域與推進同源·**值變法不變**）。
- **WATCH（既存·不改）**：`app:16215` Rw 診斷讀 rounded buffer_S 未乘 cos_dn（**診斷非閘**·真閘在 `stepg:801-812`）；app 無 telescoping 閘（僅 stepg）；`app:6053/6056` 角落抵費地以 range 記帳而幾何 212.84 → S1 後 `中央池` 值連動。

---

## 9. 施工序（八項·一次重烤·補丁四 §五＋補丁六 §六）

1. **查表化**（§6）→ 3.5 真消費點改 `get_min_lot_size` → py_compile。
2. **S0d**（§5）→ 閘寬單源函式改係數。
3. **step 0**（§2·僅右組 s 域·三處）→ 驗 ③'（R3 p2 楔形→0）。
4. **W 脫鉤**（§1·`W_prev` 初值 −δ_block／直量 mp→遠側）＋首宗下限＋R4 態樣 → 驗六塊 δ 錨。
5. **街角 band `_corner_buffer_S`**（§3·side 參數化）＋四處＋`wf_f1` right 鷹架＋ns 18。
6. **N0-20 末筆機制**（§4·R_end／勝者／常數項）。
7. **PRE 凍存** → **併一次重烤** → 歸因閘＋②③③'④⑤⑥＋不變量閘全綠 → run_all 綠。
8. py_compile → grep 對照本 plan → **push**（`git rev-parse origin/main` 嚴格驗）。
9. 報告入倉·聊天僅 ping → claude.ai 複驗 → **KL 重新 UI 實跑錨定**（幾何全動·前錨降歷史對照）。

---

## 10. 送 reviewer（設計裁決／WATCH）＋上呈 KL（域裁題）

**送 reviewer（碼面·自動路由）**：
1. **W 脫鉤之落點**：`W_prev` 初值 −δ_block vs 直量遠邊——**傾向直量**（intrinsic·step0-robust）；求驗六塊 δ 錨命中＋首宗下限 loud 位置＋`R(W≤0)=0` 分支（`app:5123`）。
2. **step 0 三處同步**：`app:15475`/`stepg:573`/`wf_f4:1124` 是否**全部**消費端改（`end_pt`/`d_hat_rev`/`right_cum_S` 基準）？
3. **閘③ post-step0 重錨**：是否正確避開 #25（禁湊 5.2719·錨取重烤後實值）？
4. **N0-20 標記制→通式之爆炸半徑**（§4）：R3/R6 現零幾何動作·改通式後 F.4 遞補錨動——求驗不越權（`W-D.4 遞補錨` 回歸閘）。
5. **歸因閘之非套套邏輯**（§7）：預測 ΔRw 是否真獨立於 G solve？
6. **S0d 下游位移**（§5·W-3）：`cum_S` 未捨入 → 下游宗 baseline 位移之量級與可歸因性。
7. **`_WF_NS_NAMES` 16→18**（W-2）＋`wf_f1` right 全鷹架（W-7）。

**上呈 KL（域裁題）——✅ 補丁七（2026-07-19）四題全裁·鎖**：
1. **δ 精確式**：✅鎖（補丁七 §四·`(mp−p2)·â`→`(mp−群推進起點)·â_定向`·純記錄更正·診斷量）。
2. **R4 單街角宗 ΣRw<100%**：✅鎖（照實 (a)＋WATCH·N0-20 施後觀察 R4 末端吸收）。
3. **N0-20「未臨正街土地」幾何源**：✅鎖（補丁七 §一·**末端 ALLOCLINE 半平面·正投影判別作廢**）。
4. **退縮查表／UC9898 耦合**：✅鎖（補丁七 §五保守解·退縮＝輸入欄＋loud 兜底〔廢靜默 3.5〕；`verify:108`/`:838` 標凍結；`app:8524` 維持 0/3.5 雙情境）。

**本 plan 之未裁域裁題**：**無**（補丁七全裁）。**KL 已授權動工**（依 plan v3 八項一次重烤·施工對照補丁七 §五）。撞出未涵蓋之真實違規 → 停機上呈。
