> ⚠️ **plan v1 經 reviewer 退回重寫（8ff6394）·規格已升 v3**。本檔保留為歷史·plan v2 依 v3 另出。

# W-G.4 終態幾何消解波 · 施工 plan（CC 撰·待 reviewer 審）

- 規格：`docs/specs/終態幾何消解波_規格.md` **v1.1**（KL 三張力全裁·唯一依據）
- 偵察：`docs/reports/W-G.4_終態幾何消解波_偵察報告.md`（HEAD 6552efe）
- 基準 HEAD：`2299260`（規格 v1.1 入倉後）

---

## §A 施工靶（REPL 坐實·禁心算·scratchpad/wg4_full_targets.py）

### A.1 3.5m 情境

**forced 街角池片 vs 街角規定範圍（§1.1 硬約束）**

| 街廓 | 側 | 街角規定範圍 | 實際街角池 | 判定 | MinA_區 |
|---|---|---|---|---|---|
| R2 | 左 forced | 309.05 | **233.74** | 🔴 **補 75.31** | 153.65 |
| R3 | 右 forced | 308.93 | 389.80 | ✅ 達標·不動 | 152.74 |
| R5 | 左 forced | 300.52 | **212.79** | 🔴 **補 87.73**（**規格 §2 未列**） | 157.64 |

**碎片（§1.3 消解）＋末筆規定範圍 Z（§1.4）**

| 街廓 | 碎片 | 面積 | 末筆端 | **Z** | MinA_區 |
|---|---|---|---|---|---|
| R1 | R1-抵費地-2 | 5.30 | p1(左) | **109.44** | 115.39 |
| R6 | R6-抵費地-2 | 85.66 | p1(左) | **166.03** | 156.06 |

**末筆第1宗（§1.4 選定·用既得 G）**
- R6 左組第1宗＝**628-4(1)**（累積S=16.49·已在末筆位）：G=776.72 **≥ Z=166.03** ✅ → 末筆第1宗（**無需位移**）。
- R1 左組第1宗：施工時依 §1.4 選定（G ≥ Z=109.44 首個滿足者）。

**街角補足機制坐實（R2 案·bisect）**
- 現 forced `buffer_S = rng/avg_depth`＝309.05/43.9＝**7.0399m**（矩形近似）→ 實切 **233.79**（≠309.05）。
- bisect 解 `buffer_S'` 使 `block ∩ strip(0, buffer_S').area == 309.05` → **S′=8.7157m**（ΔS=1.6758m），補 **75.31** ✅（錨點命中）。
- **成因**：`buffer_S = min_area/avg_depth` 為矩形近似；真實街廓幾何（截角/非矩形）使實切面積 ≠ 名目。

### A.2 0m 情境（REPL 坐實·scratchpad/wg4_0m_targets.py）

- **無 forced 街角**（街角皆有合格宗）→ **無街角補足**（§1.2 不觸發）。

**碎片（§1.3 消解）＋末筆規定範圍 Z（§1.4）**

| 街廓 | 碎片 | 面積 | 末筆端 | **Z** | MinA_區 |
|---|---|---|---|---|---|
| R1 | R1-抵費地-2 | 5.30 | p1(左) | **109.44** | 115.39 |
| R3 | R3-抵費地-2 | 78.19 | **p2(右)** | **151.13** | 152.74 |
| R6 | R6-抵費地-2 | 85.66 | p1(左) | **166.03** | 156.06 |

- **R3 於 0m 之碎片在右端**（3.5m 時該端為 forced 街角）→ 末筆端須**逐情境依碎片 s_rel 判定**（非寫死），plan §B.1 Step 2 之「末筆端＝無側街端」須以**碎片實際所在端**為準（通用機制）。
- 0m 池主體：R1 242.92／R2 785.22／R3 436.14／R4 394.10／R5 162.73／R6 187.69。

---

## §B 核心設計：E3 改造為統一「終態重切」（§1.8 收編）

§1.2 街角補足／§1.3 細碎片消解／§1.4 末筆選定／§1.5 末筆 G 重算 **高度耦合**（皆改同一街廓之 buffer／宗位／池片），必須在**同一次重切**中完成，否則互相覆蓋。

### B.1 新函式：`_resolve_block_final(ns, snap, cb_by, cad, forced, rows_E, blk, tag, mina)`（wf_f4）

對單一可建築街廓執行終態重切，回傳 `(new_lot_rows, new_pool_rows, events)`：

**Step 1 — 街角 buffer 補足（§1.1/§1.2）**
```
for side in (left, right):
    if not forced[blk][f"{side}_forced_offset"]: buffer_S[side] = 0; continue
    rng = forced[blk][f"{side}_corner_min_area"]          # 街角規定範圍
    a_cur = _block_strip(bp, dh, corner, rng/avg_depth).area
    if a_cur >= rng - TOL:  buffer_S[side] = rng/avg_depth   # 已達標·不動（R3 案）
    else:
        buffer_S[side] = bisect(S → _block_strip(...,S).area == rng)   # 補足（R2/R5 案）
        補足量 = rng − a_cur   # 由同 Ri 池吸收（中央池縮小·守恆）
```
**§1.2 順位鏈**：本案補足量全由「同 Ri 最大池片」（中央主體池）吸收；若吸收後中央池 < MinA → **loud raise + escalate**（規格 Escalate 條件明列此歧義）。

**Step 2 — 末筆第1宗選定（§1.4）**
```
末筆端 = 無側街之端（由 forced[blk][f"{side}_has_side"] 判；本案 R1/R6 皆 p1 端）
Z = _block_strip(bp, d̂_末筆端, corner_末筆端, min_width).area      # 末筆規定範圍面積
候選 = 該端組宗地，依投影序（由末筆端向街角端）
末筆第1宗 = 首個 G(i) ≥ Z 者（用既得 G·§1.5-bis）
  → 若已在末筆位（本案 R6 628-4(1)）：無位移
  → 否則移至末筆位，其餘相對序不變（硬閘 2 明定允許之位移）
若皆 G < Z：抵費地充當末筆第1宗（面積 = Z·§1.4-4）
```

**Step 3 — 重切全街廓宗地**
```
cum = buffer_S[末筆端側]
for i, lot in enumerate(該側組·末筆第1宗優先):
    if lot is 末筆第1宗:
        # §1.5 + §1.5-bis（B 案）：a 不變、G 重算
        G_new, S_new = solve_G_binary(a=a_lot, ..., baseline_pt=corner+cum·d̂,
                                       front_len_fn=lambda cut: _front_len_of(cut, fseg, bp))
        ΔG = G_new − G_old   (≥0)   # 由同 Ri 池吸收
    else:
        # §1.3：等 G 滑動（G 不變）
        S_new = bisect(S → _block_strip(..., cum, S).area == G_lot)
    寬 = S_new × cos_dn;  若 寬 < min_width 且 非既有旗標 → loud raise（不得製造新畸零）
    cum += S_new
對側組：同法（若該側 buffer 未變且無末筆 → byte 不變）
```

**Step 4 — 池重算 + g_tab 回寫（§1.8）**
```
池 = block_poly − union(所有宗新形).buffer(0.001)
池片 = [g for g in 池 if g.area ≥ 1.0]
  → 街角 forced 片（≈ rng）、中央主體片
  → 碎片（S=0 片）應已消失（被末筆宗吞納）；若殘留 → loud raise
g_tab 回寫：
  宗地列：S(m)/G(㎡)/幾何面積(㎡)/宗地寬度(m)/累積S(m)/cut_coords ← 新值
  抵費地列：**重建**（碎片列刪除；池片依新幾何逐片列，面積 = 幾何面積）
F.4 帳證：pool_final[blk] = Σ池片面積；守恆 cons 重算
```

### B.2 app.py `solve_G_binary` 純加性參數（§1.5-2）

```python
def solve_G_binary(..., front_len_fn=None):     # 🆕 末筆分支（default None＝現行行為）
    ...
    # G_target 正街項：
    S_front = S_guess if front_len_fn is None else float(front_len_fn(cut))
    G_target = max(0.0, (a*(1-A*B) - Rw*F*l_side - S_front*l_front) * (1-C))
```
- **default None → byte 不變**（一般宗地全部路徑零影響·保 G.3 同源）。
- 末筆宗傳 `front_len_fn` → S_front ＝ `wf_f1._front_len_of(cut, fseg, block_poly)`（切割帶 ∩ FRONT_LINE 之實際臨街長；未臨正街段自動為 0）。
- **X3 已裁**：`l_front`＝正典 l₂（正街）·code 配對正確·不動。
- **no-silent-fallback（硬閘 8）**：末筆求解未收斂 → **loud raise**（禁退代數 fallback）。

### B.3 廢止 / 收編
- `_reshape_block`（wf_f4:1074）：其幾何 helper（終端 corner＋反向 d̂、bisect 等 G 重切、_fuse）**收編**入 `_resolve_block_final`；**整個函式刪除**（§1.8-3「只整形不記帳」語意廢止·no-silent-fallback 鐵律：舊路徑整段刪、不留 stub）。
- `reshape_polys`（wf_f4:818 / wf_f1:354）：**降級中間產物**——終態呈現改由 g_tab render。app.py `_wg_gen_figure(reshape_polys=...)` 之整形疊圖：**F.1/f1 世代圖保留**（前後對照用·中間產物），**E 終態圖改純 g_tab**（§1.8-2）。
- `wf_f1.compute` 之 R1 整形：F.1 為**中間世代**，其 reshape_polys 保留（世代圖用）；**終態消解一律於 E3**。

---

## §C 子波序與驗收

| 子波 | 內容 | 驗收 |
|---|---|---|
| **G.4-a** | app.py `solve_G_binary` 加 `front_len_fn=None` 純加性參數 | py_compile ✅ ＋ **run_all 155 綠**（證零行為變更·default 路徑 byte 不變） |
| **G.4-b** | wf_f4 新增 `_tail_range_Z` / `_select_tail_first` / `_resolve_block_final`（未接線） | py_compile ✅ ＋ 單元驗（Z=166.03/109.44·buffer_S′=8.7157 REPL 對拍） |
| **G.4-c** | E3 改造接線（收編 `_reshape_block`·刪除舊函式）＋ g_tab 回寫 ＋ F.4 帳證同步 | 雙情境跑通·守恆/位次/池三則 自檢 |
| **G.4-d** | §3 九硬閘入 run_all（街角第1宗／末筆 G≥Z／池三則／等G／末筆重算 ΔG 由池吸收／守恆） | 新閘全綠 |
| **G.4-e** | baseline 全鏈重烤（WV_BAKE·同 Y 波框架）＋ G.3 重跑 | **run_all 155+新閘 ALL GREEN** ＋ wg_g3 byte-perfect |
| **G.4-f** | app.py 抵費地 hover S（§1.7）＋ 正典入倉（skill 檔·§5） | py_compile ✅ |

**push 節奏**：G.4-a 獨立 push（零行為變更·可先驗）；G.4-b~e 為一體（baseline 變動）合併 push；G.4-f 獨立 push。

---

## §D 硬閘映射（§3 九閘 → 實作位置）

| # | 硬閘 | 實作位置 |
|---|---|---|
| 1 | 守恆（帳目+幾何） | `_resolve_block_final` Step 4 ＋ E4 `cons` ＋ run_all 新閘 |
| 2 | 位次不變（除末筆明定位移） | `_resolve_block_final` Step 3 後 `_projection_order` 對拍（末筆位移列白名單） |
| 3 | 街角第1宗 ≥ 範圍 | `_resolve_block_final` Step 1 後斷言（forced 池片面積 ≥ rng − TOL） |
| 4 | 末筆第1宗 G ≥ Z | Step 2 選定時斷言（抵費地充當時 面積 == Z） |
| 5 | 池三則 ∉ (0, MinA) | Step 4 後斷言（逐池片） |
| 6 | 等 G／末筆重算 | Step 3：一般宗 \|area−G\|≤0.01；末筆宗 a 不變 ＋ ΔG 由池扣（REPL 驗） |
| 7 | 合併 Σa 重解禁直加 | 既有（E1/E2 已守）·不動 |
| 8 | no-silent-fallback | Step 3 末筆求解未收斂 → `raise RuntimeError`（禁 fallback） |
| 9 | run_all 155+新閘 ALL GREEN | G.4-e |

---

## §E 風險與上呈

1. **⚠️ 規格缺口（上呈）**：**R5 左 forced 需補 87.73**，規格 §2 錨點表**未列**（只列 R2 75.31）。依硬閘 §3-3（街角第1宗·**全街廓通用閘**），R5 必須補足。plan 採**通用機制**（逐 forced 街角自動判補·不寫死 R2）→ R5 自動涵蓋。**錨點 87.73 待 claude.ai/KL 追認**。
2. **baseline 大幅變動**：R2/R5 街角補足使左組宗右移（等 G·位置變）；R1/R6 末筆 G 微增（ΔG 由池吸收）。→ v3/wf 全鏈重烤（G.4-e）。E2 最優指派**不受影響**（一般宗 G 不變；末筆 ΔG 僅由池吸收、不改配地資格）。
3. **§1.2 順位鏈未觸發**（本案中央池吸收後仍 ≥ MinA：R2 367.67>153.65；R5 待算）——若觸發 → loud raise + escalate（規格明列）。
4. **0m 情境 R3 碎片 78.19**：0m E3 分類確認中；若為碎片則同機制消解（§1.6）。
