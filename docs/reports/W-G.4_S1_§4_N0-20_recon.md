# W-G.4 S1 §4 N0-20 末筆機制 recon（禁假設·approach 前置）

- 日期：2026-07-20；branch `wip/s1-endpart`（基準含 §3 `5b80f9d`＋停機③ `3403ba1`·皆 KL 獨立複驗 PASS）
- 依據：plan v3 §4＋補丁七（N0-20 幾何正典·未臨正街＝末端 ALLOCLINE 半平面·正投影作廢）＋補丁八（W₀=mp）
- 狀態：**recon 中·approach 未成·未動工**。§4 為本波最大塊·觸 F.4 遞補錨（爆炸半徑）→ recon→approach→reviewer→（KL 域裁 爆炸半徑）→施工。

---

## 1. 現碼落點（wf_f1·已讀·禁假設）

**F.1 現機制**（`wf_f1.py`·KL 縮圍裁定 2026-07-11）：
- **R1**（雙情境錨 0m→628-37(1)／3.5m→628-36(1)·左角勝者）：**等 G 幾何重切＋後續宗前移**。
  - `wedge = r1_frag["poly"]`（p1 端碎片·`WEDGE_AREA_ANCHOR=5.30`·:257-259）。
  - bisect：`union_area(S) = _fuse(strip(0,S), wedge).area`·解 `== G_B`（:305-310）。
  - **🔑 關鍵發現**：`fuse(strip(S'),wedge).area == G_B` ⟺ `strip(S').area == G_B − wedge.area` ＝ **plan §4「常數項 bisect `strip(S)=G−wedge`」逐字同形**。→ **現 R1 機制即 N0-20 之特例**（wedge＝R_end 之退化＝僅一碎片）。
- **R3/R6＝標記制**（裁示 1(b)·:250-254·**零幾何動作**）：標記「待 F.4 終態遞補整形」；角落失格業主（R3 628-42(2)/628-29(1)·R6 …）尚未離場·碎片地景屆時重生。
- 幾何源（wf_f1 內·:200-205）：`front_lines`(p1,p2)／`alloc_dir_by_block`／`alloc_normal_axis`／`_projection_order`(:376) **皆可得** → 末端 ALLOCLINE 半平面可建。
- `strip_at(cum_S,S)` 走 `_block_strip`（∥ALLOC 斜交·同 §3）。

## 2. N0-20 目標機制（plan §4＋補丁七·待落地）

`R_end ＝ 未臨正街土地 ∪ 末端帶`：
- **未臨正街**＝**末端 ALLOCLINE 半平面外側 ∩ block**（過 FRONTLINE 末端點·法向＝ALLOCLINE 方向·**禁正投影/質心**·補丁七 §一.2 `ALLOCLINE_1` 鑑別案）。
- **末端帶**＝末端 ALLOCLINE 向街廓內平移「畸零寬」（自 mp 往內量·W=S=畸零寬·查表 §6·禁 3.5）。
- **勝者規則**：與 R_end 交集之重劃前土地·投影排序·**首筆 `G ≥ area(R_end)` 吃整塊**；皆不達→末筆抵費地嚴格＝`area(R_end)`；未臨正街土地不單獨成筆。
- **常數項 bisect**：勝者 bisect 解 `strip_area(S) = G − wedge_area`（＝現 R1 之 `union.area==G_B` 之等價式·§1 已證同形）。

## 3. 🔴 爆炸半徑（§4 最大風險·已定位·待評/域裁）

**R3/R6 標記制（零幾何）→ N0-20 通式（實幾何）＝把碎片處置由 F.4 移回 F.1**：
- 現 p1 端碎片 **5.30(R1)／78.19(R3)／85.66(R6)** 由 **F.1 標記＋F.4 遞補**處置（`run_verification:619`「碎片列 5.30/78.19/85.66 原封不動」）。
- **W-D.4 遞補錨閘**（`wd4_tier_list:315-342`）錨定：**R6 85.66→628-1(2)**（跳過 628(2) S=0.19·有效＝S≠0 且 寬≥min_width）；F.4 E3 終態遞補整形（`wf_f4:682`·純幾何·池不變）。
- **改通式後**：R3/R6 於 F.1 即以 R_end 實幾何被勝者吃下 → **F.4 遞補錨之標的可能變**（碎片不再殘留至 F.4）→ 須跑 **W-D.4 遞補錨回歸閘**證**不越權**（plan §4/§10 既有機制·#24-1「正典條文只在其落點適用·越權爆炸半徑大一數量級」）。
- **待決**：(a) 勝者「投影排序」是否複用 `_projection_order`（plan §4 列 reviewer 待決·wf_f1:376 已有用例）；(b) R3/R6 由標記→通式後·F.4 遞補錨/E3 整形/總決算(E5 33 群) 之連動——**須 reviewer 實跑界定爆炸半徑·可能須 KL 域裁**（碎片處置波次歸屬：F.1 vs F.4）。

## 4. 與 §3 W-8 邊界對齊（補丁九 裁2）

§3 left band 之 `s_min<0` 段（現 loud print·§3 已裝）→ **判別改用末端 ALLOCLINE 半平面**·歸 N0-20。本案現況 forced 塊（R2/R5 左·s_min>0）不觸；`s_min<0` 之 R1/R6 非 forced → §3/§4 落地後該段歸 R_end。

## 5. 待續 recon（approach 前）

1. **未臨正街半平面**之精確建構（過哪個 FRONTLINE 末端點·p1 抑或依 side·法向定號）＋與 block 交集之 shapely 實作。
2. **末端帶** mp 之取得（末端 ALLOCLINE 之中點？）＋平移畸零寬之帶構造。
3. **R_end ＝ 未臨正街 ∪ 末端帶** 之聯集面積 vs 現碎片錨（R6 85.66 是否＝area(R_end)·或 R_end 更大含末端帶 166.57→252.28·plan §4-1 R6 實例）。
4. **勝者規則** 與現 F.1 target 搜尋（:268-279）之異同·投影排序源。
5. **爆炸半徑實測**：改通式後跑 W-D.4 遞補錨閘＋F.4 baseline·界定 diff（reviewer）。

## 6. 次步

approach（依上·側/端顯式參數化·禁本案常數·同 §3 泛用四約束精神）→ 送 reviewer（focus：爆炸半徑實測／未臨正街半平面幾何／勝者規則）→ 撞出域裁（碎片波次歸屬）上呈 KL → 施工 → 併末端一次重烤。
