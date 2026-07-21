# W-G.4 S1 §4 N0-20 末筆機制 approach（承 `205f3e6`·先錨已驗·送 reviewer）

- 日期：2026-07-20；branch `wip/s1-endpart`；基準含 §3/停機③/try/except/§4錨（皆 push＋KL 複驗）
- 依據：plan v3 §4＋補丁七（N0-20 幾何正典）＋補丁八（W₀=mp）；先錨 R6 252.28 已純幾何逐位重現（recon §1.5）
- 紀律：同 §3 泛用四約束（禁本案常數）；R_end 三塊構造顯式化·CAD-可重現 <0.01（KL/claude.ai 逐塊坐實）
- 狀態：**approach·未動工**。送 reviewer 實測爆炸半徑（v3 `628-4(1)`）→ 撞真域裁才上呈 KL → 施工。

---

## 0. 🔴 reviewer 活抓·approach 前提錯·REFRAMING（2026-07-20·CC grep 全坐實·上呈 KL）

reviewer 獨立審 approach（設計階段）撞出**本 approach 之「爆炸半徑」前提根本錯**·CC **grep 逐項坐實**（禁採信·同模型）：

| # | reviewer 主張 | CC grep 坐實 |
|---|---|---|
| 1 | **F.1 是下游死路** | `run_verification:999 _f4=wf_f4.compute(_ctx,_f0,_f2,_f3)`·`wf_f4:284 def compute(ctx,f0_out,f2_out,f3_out)`**無 f1 參數**；:867 f2 亦吃 f0 → F.1 輸出下游不消費 ✅ |
| 2 | **`_reshape_block` 已是通式** | `wf_f4:1096-1097` docstring 逐字「**wf_f1 R1 機制通用化（任意塊×左右側）·停機條款全同 F.1**」·對 R3/R6 生效 ✅ |
| 3 | **遞補錨閘對 §4 不敏感（恒綠陷阱）** | `wd4_tier_list:49 from stepg_pipeline import run_step_g`·**無 import wf_f1**·:189 跑 trunk-B → 改 wf_f1 不改 wd4 輸出 → `run_verification:707` 閘改前改後恒綠·零鑑別 ✅（我 approach §4「跑此閘證不越權」＝把綠當過·**作廢**）|
| 4 | **UC9898 終態 diff=0（收斂）** | `F.4_整形_退縮0m.csv:19` R6→628-4(1)·G=776.72·**S_new=14.65**；§4 通式 strip=776.72−85.71(未臨正街)=691.01→同 S_new=14.65·末端帶 166.57⊂strip → 吞·不改終態 ✅（R3 winner 628-45(2) G=614≫R_end 154·同理）|

**REFRAMING（正確理解·取代本報告 §4「爆炸半徑」全段）**：
- §4 之**整形通式已在 F.4 E3**（`_reshape_block`）。F.1 之 R3/R6 標記制是**死路**·「移回 F.1」（recon §3 語）**架構不可行**（F.1 死路→令 F.4 停手則終態失整形→R6 留 85.71 S=0 sliver→破裁示1(b)）**且抵觸裁示1(b)**（`wf_f1:10`「R3/R6 標記制·待 F.4·業主未離場」·KL 2026-07-11）。
- UC9898 之 R3/R6 winner G≫area(R_end) → winner 吃下 R_end（末端帶已含於 strip）→ **§4 對 UC9898 終態 diff=0**。N0-20 新語意（首筆 G<area(R_end)→**末筆抵費地嚴格=R_end**）只在**無 winner** 時咬合·UC9898 **不觸發**（latent·無夾具·reviewer C-2）。
- **⚠️ 上呈 KL（触及 F.1↔F.4 歸屬·裁示1(b)·＝ KL 指定停機條件）**：見文末 §7 是非題。
- 其餘 reviewer 判：**B 末端帶⊥垂距 PASS**（獨立逐位·R6 252.276）；**C-1** 投影排序**勿複用 `_projection_order`**（≠ target 搜尋語意·應複用 `_reshape_block` target 搜尋 wf_f4:1149-1161）；**C-2** winner 門檻「G≥R_end」係新增行為分岔（現 _reshape_block 無門檻）·末筆抵費地退路無夾具；**D** 設計泛用四約束 PASS·惟施工 B 盒須由 bounds 導（禁硬編 500）。

---

## 1. R_end 定案構造（**顯式·CAD-可重現**·KL 要 <0.01）

**基元**（同 §3·∥ALLOC 斜交·禁正投影·禁假設 ⊥）：
- `p1` ＝ 該塊 FRONTLINE 之末端點（`cad.front_lines[blk].p1`·s 域 s<0 之末端）。
- `cad_alloc` ＝ 該塊宗地分配線單位向量（`cad.alloc_dir_by_block[blk]` 正規化）＝地界線方向。
- `d̂` ＝ FRONTLINE 單位向量（p1→p2）。畸零寬 ＝ `get_min_lot_size(分區, 正面路寬).min_width`（查表·禁 3.5）。
- s 座標 ＝ `_strip_s_range(block, d̂, corner_pt=p1, allocation_dir=rot90(cad_alloc))`（§3 同源·恆等 `s(p1)=0`）。

**① 未臨正街**（補丁七 §一.1 半平面）：
> `未臨正街 = block ∩ {s < 0}`。**s=0 線** ＝ 過 `p1` 且 ∥`cad_alloc` 之直線（＝末端 ALLOCLINE）；`{s<0}` ＝ 該線**離街廓形心**之半平面。
> 實作：`_block_strip(block, d̂, bp=p1+s_min·d̂, S=−s_min, allocation_dir=rot90(cad_alloc))`（＝ block∩{s∈[s_min,0]}）。**驗**：_block_strip 與直接半平面 clip 逐位同（`probe_rend4` Δ=0.0000）。

**② 末端帶**（補丁七 §二.2 平移·**⊥垂距·非 s-strip**）：
> `末端帶 = block ∩ (末端 ALLOCLINE 與其 ⊥平移線 之帶)`。**⊥平移** ＝ 過 `p1` 之 s=0 線·沿 `rot90(cad_alloc)`（**指向街廓形心**）平移**垂距 W = 畸零寬**；帶 ＝ 兩平行線（皆 ∥`cad_alloc`）間之區域。
> 實作：`band = Polygon([p1−B·cad_alloc, p1+B·cad_alloc, p1+B·cad_alloc+W·n̂, p1−B·cad_alloc+W·n̂]) ∩ block`，`n̂ = rot90(cad_alloc)` 定號使 `(centroid−p1)·n̂>0`。
> **⚠️ 禁 s-strip**（`_block_strip S=畸零寬`）——斜交下差 `1/cos(∠(d̂,⊥ALLOCLINE))`（R6 差 0.54㎡·錨活抓·recon §1.5）。

**③ R_end** ＝ `未臨正街 ∪ 末端帶`（s<0 與 s≥0 側·共 s=0 界·**不疊**·union＝sum）。

**三塊錨（純幾何·`probe_rend3`·CAD-可重現）**——**approach 之權威為上文構造式·數字僅本案坐實（禁入碼）**：

| 塊 | 未臨正街(s<0) | 末端帶(⊥W=畸零寬) | R_end∪ | 錨 |
|---|---|---|---|---|
| **R6** | 85.7064 | 166.5696 | **252.2760** | plan §4-1 252.28 ✅（Δ−0.004）|
| R3 | 0.0001 | 153.7720 | 153.7721 | — |
| R1 | 5.3255 | 109.8135 | 115.1390 | R1 未臨正街＝`WEDGE_AREA_ANCHOR` 5.30 ✅ |

> claude.ai 先錨複驗：未臨正街構造✓（其 85.6883 vs 85.7064 Δ0.018＝block polygon 資料源差〔pipeline vs 原始 CAD〕·非構造·上文兩法逐位同已證）。`probe_rend3.py`/`probe_rend4.py` commit 入倉作次要參照。

## 2. 勝者規則（plan §4-2·待 reviewer 覆核投影排序源）

- **候選** ＝ 與 R_end 有交集之重劃前土地（該塊·投影排序）。
- **勝者** ＝ 投影排序**首筆** `G ≥ area(R_end)` → **吃下整個 R_end**（末端帶＋未臨正街·一宗到底）。
- **皆不達** → **末筆為抵費地·面積嚴格 ＝ area(R_end)**。
- **未臨正街不單獨成筆**（必併勝者宗或隨末筆抵費地·補丁七 §一.3）。
- **投影排序**：擬複用 `_projection_order`（wf_f1:376 已有用例·送 reviewer 確認與現 F.1 target 搜尋〔wf_f1:268-279「沿分配序第一筆有效宗」〕之異同）。

## 3. 常數項 bisect（plan §4-3·＝現 F.1 R1 之泛化）

- 勝者 bisect：`strip_area(S) = G − 未臨正街_area`（實配 ＝ p1 起平行四邊形〔strip〕＋ 未臨正街〔常數〕）。
- **＝現 wf_f1 R1 機制**（`fuse(strip(S'),wedge).area==G_B` ⟺ `strip(S')==G_B−wedge`·wedge＝未臨正街）**逐字同形**（recon §1）。strip(S) ⊇ 末端帶（∵ G≥area(R_end) → strip=G−未臨正街 ≥ 末端帶）。
- **末端帶不另構**：其係 strip(S) 之一段（勝者吃下）；R_end 僅為「勝者須覆蓋之下限＋抵費地退路之嚴格值」。

## 4. 🔴 爆炸半徑（送 reviewer 實測·標的 v3 `628-4(1)`）

**標記制→通式＝碎片處置 F.1→F.4 之移轉**：
- 現 R3/R6＝標記制（零幾何·碎片 78.19/85.66 待 F.4 遞補）；R6 未臨正街 85.66 現為抵費地碎片 → **W-D.4 遞補錨 628-4(1)**（v3·非過期 628-1(2)）。
- 改通式：R6 之 R_end **252.28**（未臨正街 85.66＋末端帶 166.57）由勝者吃下**或**末筆抵費地嚴格＝252.28 → **碎片 85.66 不再殘留至 F.4** → **F.4 遞補錨 628-4(1) 之標的/存在可能變**。
- **reviewer 必測**（實跑·非推理）：改通式後跑 **W-D.4 遞補錨回歸閘**（`run_verification:707`）＋F.4 baseline（E3/E5 33 群）·**界定 diff 之爆炸半徑**·證**不越權**（#24-1）。標的一律 v3 `628-4(1)`。
- **停機上呈 KL 之唯一條件**：reviewer 實測 diff **真触及 F.1↔F.4 碎片歸屬**、需 KL 判斷（白話：現況/要改成/土地影響+數字/是非題）。**純技術 diff → 自行施工**。

## 5. 落點（施工·additive／改標記制）

- **新模組級純函式**（`app.py`·`_pool_strips_for_block` 鄰·ns harvest·同 §3 `_corner_buffer_S` 先例）：
  - `_end_region_R(block, d̂, p1, cad_alloc, min_width, _label)` → `(未臨正街, 末端帶, R_end)` 幾何＋area。**side/端顯式參數化**（末端由 s<0 之端定·禁寫死塊名/側別）。缺 cad_alloc → loud raise（同 `_corner_buffer_S`·約束1）。
- **wf_f1 R3/R6 標記制 → 通式**（:250-254）：以 `_end_region_R` 算 R_end → 勝者規則（`_projection_order` 首筆 G≥area(R_end)）→ 常數項 bisect（複用現 R1 之 `_bisect_area(union_area, G_B)` 泛化·wedge＝未臨正街）→ 或末筆抵費地嚴格＝area(R_end)。
- **W-8 邊界對齊**（補丁九 裁2）：§3 left band 之 `s_min<0` 段（現 loud print）→ 判別改末端 ALLOCLINE 半平面·歸此 R_end（§3/§4 同末端重烤前落地·中間態內部）。
- **不動**：`_build_corner_range_v2`（§3 range 源）／§N2 名單／stepg 推進機（additive）。

## 6. 送 reviewer 之問

1. **爆炸半徑實測**（最重）：R3/R6 標記制→通式後·W-D.4 遞補錨（628-4(1)）＋F.4 E3/E5 之 diff？触及 F.1↔F.4 歸屬否？
2. **投影排序源**：勝者複用 `_projection_order` 是否＝現 F.1 target 搜尋語意（有效宗·跳失格）？
3. **末端帶 ⊥垂距構造**（非 s-strip）之施工實作是否逐位重現三塊錨（R6 166.57）？缺 cad_alloc loud？
4. **常數項 bisect 泛化**：現 R1 之 `union_area(S)==G_B`（wedge＝未臨正街）推廣至 R3/R6·`_fuse` MultiPolygon 界（`_FUSE_EPS`）是否仍守？
5. **W-8 中間態**：§3 先落地之 `s_min<0` loud 段·與 §4 R_end 之邊界對齊·重烤前中間態是否破 ①' 覆蓋。

---

## 7. 🔴 上呈 KL＋claude.ai（reviewer 界定触及 F.1↔F.4／裁示1(b)＝KL 指定停機條件·白話是非題）

**現況**（CC grep 坐實·reviewer 活抓）：§4 之整形通式**已在 F.4 E3**（`_reshape_block`·R1 機制通用化·對 R3/R6 生效）。F.1 之 R3/R6 標記制是**下游死路**（F.4 讀 f0/trunk-E·不讀 f1）。UC9898 R3/R6 winner G=614/776 ≫ area(R_end) 154/252 → winner 吃下 R_end（末端帶已含於其 strip）。

**土地影響+數字**：**§4 對 UC9898 終態 diff＝0**（收斂·baseline S_new=14.65 佐證·守恆不動）。N0-20 新語意「首筆 G<area(R_end)→末筆抵費地嚴格＝area(R_end)」只在**無 winner** 時咬合·UC9898 winner G≫R_end **不觸發**（latent·無夾具）。

**我原以為錯了**：approach 以為 §4＝改 F.1 標記制→通式·爆炸半徑 via F.4 遞補錨。**全錯**（grep 坐實）：F.1 死路·遞補錨閘讀 trunk-B 恒綠不敏感·通式已在 F.4。

**是非題（請 KL／claude.ai 裁）**：
1. **波次歸屬**：R3/R6 末端整形續在 **F.4**（甲·符裁示1(b)「待 F.4·業主未離場」），**非**「移回 F.1」（乙·架構死路+抵觸裁示1(b)）——**確認甲？**（乙不可行·我不自裁·上呈）。
2. **§4 之實際交付**：既然 UC9898 終態 diff=0（通式已在 F.4 E3），§4 應是「**於 F.4 E3 `_reshape_block` 補完 explicit R_end／末端帶 構造＋末筆抵費地 fallback**（技術形式化·對 UC9898 終態不變·為未來/edge 案正確性＋補丁七 R_end 對齊）」，**對否**？抑或 §4 本應改變 UC9898 某處（若然·我理解仍有缺）？
3. **winner 門檻**：「首筆 G≥area(R_end) 方為 winner」是 **N0-20 正典本意**，還是通式化時**不加**（現 `_reshape_block` 無門檻·target 有效即吃碎片）？（此門檻引入 UC9898 未觸發之新分岔·spec 意思決定）。

**次步待裁**：KL/claude.ai 裁 1–3 後·我 revise approach（落點改 F.4 E3·刪爆炸半徑/遞補錨閘·winner 複用 `_reshape_block` target 搜尋·末筆抵費地 fallback 加合成夾具）→ 再送 reviewer → 施工。**純技術部分**（末端帶⊥垂距構造已 PASS·B 盒 bounds 導·投影排序改源）我可先備·惟 §4 之**範圍與交付**（1-3）係意思決定·裁前不施工（必答題未裁先施工＝停機）。
