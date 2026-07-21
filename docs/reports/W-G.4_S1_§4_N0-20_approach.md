# W-G.4 S1 §4 N0-20 末筆機制 approach（承 `205f3e6`·先錨已驗·送 reviewer）

- 日期：2026-07-20；branch `wip/s1-endpart`；基準含 §3/停機③/try/except/§4錨（皆 push＋KL 複驗）
- 依據：plan v3 §4＋補丁七（N0-20 幾何正典）＋補丁八（W₀=mp）；先錨 R6 252.28 已純幾何逐位重現（recon §1.5）
- 紀律：同 §3 泛用四約束（禁本案常數）；R_end 三塊構造顯式化·CAD-可重現 <0.01（KL/claude.ai 逐塊坐實）
- 狀態：**approach·未動工**。送 reviewer 實測爆炸半徑（v3 `628-4(1)`）→ 撞真域裁才上呈 KL → 施工。

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
