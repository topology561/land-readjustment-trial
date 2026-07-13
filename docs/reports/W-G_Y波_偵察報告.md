# W-G Y 波「live 財務→§7」全鏈重烤 · 偵察報告

- 日期：2026-07-14；基準 HEAD＝`d665a61`；KL 裁定 2026-07-14（Y 路：重烤讓 harness 也吃 live 全精度）。
- 目的：偵察（禁假設）。實查 app.py `f3_G_values` 生成路徑、Patch B-2 位置、`g_tab` 內 ghost 列存在形式、
  `verify/stepg_pipeline.py` 現況與 f3_G_values 之具體差異點，為 Y 波施工提供**可執行**基礎。
- 產出：本報告（差異點清單＋子波序建議＋停機規則）；Plan 於下一步撰寫。

## 一、G.3 揭露之架構分歧（KL 質疑逼出）

`verify/wg_g3.py` 第 78-104 行 `_seed_ctx` 之當前實作：

```python
sg = run_step_g(ns, fake_st, ..., build, ..., setback)     # harness stepg 產出 g_rows
seed = dict(fake_st.session_state)
seed.pop("f3_total_burden_rate_from_finance", None)
seed.update({
    "f3_G_values": sg["g_rows"],                            # ← harness g_rows 灌入 seed
    ...
})
return ns["_build_wf_ctx"](seed, tag, ns["__file__"])       # app-path 出艙 ctx
```

**G.3 現況證的**：`_build_wf_ctx`（app-path）餵 **harness g_rows** → `wf_f0→f4` **byte-perfect** 對拍
harness baseline。二路皆用 harness 種子＝**假同源**（都用同源種子當然同源）。

**G.3 未證的**：app live 之 `f3_G_values`（`app.py:15471` 由 Step G 迴圈直寫、經 `app.py:16146-16198`
步驟 J Patch B-2 加工）→ `_build_wf_ctx`（app.py:8102-8108 手動還原 raw G）→ `wf_f0→f4`。

**KL localhost 實跑撞 G014/E0 錨破** ← 走的正是 G.3 未證的完整 live 鏈。

## 二、三大分歧點（file:line 引，禁憑記憶）

### 分歧 A：ghost 列排除

| 端 | 位置 | 行為 |
|---|---|---|
| app.py Step G | `app.py:14526-14529` | `for tp in build_parcels: parcels_by_block.setdefault(tp['所屬街廓'], []).append(tp)` — **不排 ghost** |
| harness stepg | `verify/stepg_pipeline.py:228-232` | `for tp in build_parcels: if tp.get("_is_ghost_sliver", False): continue; ...` — **排 ghost** |

ghost 列定義（`app.py:4213-4228`）：`_is_ghost_sliver=True`、`幾何面積_m2=0`、`面積_m2=0`、
`原地號='_GHOST'`、真面積存 `_ghost_area_m2`（已落池）。

**下游影響**：
- ghost 缺 `分攤登記面積_m2` 欄 → harness stepg L250-253 走 else 分支 → `a_m2=0`
- ghost 進 Step G → 產出 `推進側別='left'/'right'`、G=a=0、S=0 之 g_row（app.py:14528 未排）
- 進 `wf_f0` 之 `A = {r["暫編地號"]: r for r in gA if r.get("推進側別") in ("left", "right")}` (wf_f0:83、194)
  → **A dict 多 ghost 列**（G=a=0 → 級0/0' 決策雖不影響但列數異）
- `g_tab` CSV 序列化 → **列數異** → G.3 byte-perfect 破

**baseline 現況（wc -l）**：`F.0_G值_退縮0m.csv=56 行`、`退縮3.5m.csv=58 行`，`grep -c _GHOST=0` — **baseline 無 ghost 列**（因由 harness 產出）。

### 分歧 B：Patch B-2 效應（步驟 J 修飾）

`app.py:16146-16198` 於 `f3_G_values` 寫入後、於**步驟 J** 執行：

- `_r_jw['實際寬度(m)'] = round(_w_jw, 2)`（每筆）
- 若 `_w_jw < _legal_w`：
  - `_r_jw['_below_min_width'] = True`
  - `_r_jw['_width_violation_note'] = f"寬度 {_w_jw:.2f}m < 法定最小 {_legal_w:.2f}m"`
  - 若 `_orig_G >= _min_a_jw`：
    - `_r_jw['_G_before_width_violation'] = _orig_G`
    - `_r_jw['G(㎡)'] = round(min(_orig_G, _min_a_jw - 0.01), 2)` ← **G 壓縮**

`_build_wf_ctx`（`app.py:8102-8108`）出艙時**手動還原 raw G**：

```python
"gA": [({**_r, "G(㎡)": _r["_G_before_width_violation"]}
        if _r.get("_G_before_width_violation") is not None else _r)
       for _r in _need("f3_G_values")],
```

**淨效應**：wf_f0 讀 gA 之 `G(㎡)` == raw G（與 harness 一致）。**但**其他 Patch B-2 加的欄位
（`_below_min_width`、`_width_violation_note`、`實際寬度(m)`、`_G_before_width_violation`）**照樣進 gA**。

**verify/ 完全無**引用（`grep _below_min_width|_width_violation|_G_before_width_violation|實際寬度 verify/` = 0 命中）
→ wf_f0~f4 忽略這些欄位、計算不受影響。

**但**：`g_tab` CSV 序列化（`stepg_pipeline.py:851-859` build_step_g_tables 之 `_cols` 聯集）→
若 gA 列有這些額外欄位、baseline 沒有 → **欄數異** → byte-perfect 破。

**baseline 現況**（`F.0_G值_退縮0m.csv` 頭列）＝28 欄，**無** `_below_min_width`／`實際寬度(m)`／`_G_before_width_violation`。

### 分歧 C：sub-cent 精度（潛藏處未定位）

handoff 明示「保留 sub-cent」——但實查未定位具體位置：

| 檢驗點 | app.py | harness stepg | 結果 |
|---|---|---|---|
| `_a_m2` 計算 | 14544-14547 `round(..., 2)` | 250-253 `round(..., 2)` | **一致** |
| `G(㎡)` rounding | 14567 `round(_res.get('G', 0.0), 2)` | 274 同上 | **一致** |
| `avg_depth_default` | 14629-14631 float 全精度 | 327-329 float 全精度 | **一致** |
| B/C 財務值 | 14550 `_build_wf_ctx` 前組（未查完）| 152-156/105 全精度 | **待跑對拍確認** |
| solve_G_binary 內部 | app 真函式（`solve_G_binary`）| 同一函式（走 ns） | **同源** |

**推測 C 潛藏處**（未證實）：
1. Ghost 列缺欄 → harness stepg 因 filter 未走到，app 走到後可能觸發 fallback 精度差
2. build_parcels 之「面積_m2」欄本身：app live 可能來自累加器（有 sub-cent 累積誤差），harness 從快照載入（rounded）
3. Patch E-1.6（S(m) 優先於 cut_coords）之 rounding chain：`實際寬度 = round(_w_jw, 2)`（app.py:16175）
   本身 sub-cent（2dp），若 wf_* 有讀（目前無）就會不一致

**Y 波施工時**：需**跑一次真對拍**（KL localhost 一手 g_rows dump vs harness 一手 dump）才能定位；
或在 Y.0 加**逐格 diff harness**（app_harvest 抽出 f3_G_values 與 harness g_rows 逐欄比對），逐格顯性化差異。

## 三、baseline 現況對照

| 檔 | 位置 | 現況 | Y 後預期 |
|---|---|---|---|
| v3 G 值/滑池槽/J 表 | `verify/baselines/v3/` | harness native（無 ghost·無 Patch B-2 欄）| 加 ghost 列（若 UC9898 產出 ghost）·仍無 Patch B-2 欄（Patch B-2 在步驟 J、非 Step G） |
| F.0～F.4 全表 | `verify/baselines/wf/f0~f4/` | harness native | 依 v3 重烤結果連鎖重烤 |
| 舊 baseline 凍存 | `verify/baselines/PRE勘誤_期日/` | v3 勘誤前 | **加一組凍存** `PRE-Y·凍存/`（不刪、只加） |

**列數/欄數移動預期**：
- **列**：若 UC9898 之 build_parcels 含 ghost 列（進可建築土地分類），F.0 G 值 CSV 列數 +N（ghost 數）
- **欄**：若 harness stepg 也複製 Patch B-2 加欄位，g_tab 欄數 +4（`_below_min_width`／`_width_violation_note`／`實際寬度(m)`／`_G_before_width_violation`）；
  或者 harness 不加、Y.6 G.3 於序列化時**濾這 4 欄**保 byte-perfect（**推薦**）
- **值**：sub-cent 若定位到 app live 有而 harness 沒有的精度來源，harness 補齊後對應格 `G(㎡)`／`S(m)`／`W(m)` 可能微動（≤ 0.01 於 2dp 顯示層通常仍相同，但 byte 可異）

## 四、Y 波子波序建議（待 Plan 具體排）

**框架借鑒**：v3 勘誤重烤（HEAD b288446、報告 `docs/reports/W-G_v3勘誤重烤.md`）——
「單一輸入修正 → 全鏈機械性重烤 → 驗四 CSV 綠 → push」，Y 波性質同、範圍更廣（動輸入端 harness stepg）。

**建議序**：

| 子波 | 動作 | 對拍 | 交付 |
|---|---|---|---|
| Y.0 | `verify/stepg_pipeline.py` 拿掉 L228-232 ghost 濾除；補 sub-cent 精度對齊（依定位結果）；harness 也複製 Patch B-2 之非壓縮欄位（`實際寬度(m)` 等）——只加欄、不改計算 | 加 harness vs live g_rows 逐格 diff 工具（Y.0.1） | `stepg_pipeline.py` diff·對拍工具 |
| Y.1 | v3 baseline 重烤（v3 G值/滑池槽/J 表 × 雙情境 6 檔）；舊值凍存 `PRE-Y·凍存/` | `run_verification.py` 155 綠 | 新 v3 CSV · PROVENANCE_v3 加 Y 節 |
| Y.2 | F.0 baseline 重烤（6 檔 × 2 情境 = 12 檔） | `run_all.py` F.0 段綠 | 新 F.0 CSV · PROVENANCE_F0 加 Y 節 |
| Y.3 | F.1 重烤 | 同上 | F.1 CSV · PROVENANCE_F1 |
| Y.4 | F.2 重烤 | 同上 | F.2 CSV · PROVENANCE_F2 |
| Y.5 | F.3、F.4 重烤 | 同上 | F.3/F.4 CSV · PROVENANCE_F3/F4 |
| Y.6 | `wg_g3.py` 改：`_seed_ctx` 讀 **live 之 `f3_G_values`**（保留 Patch B-2 加欄位、由 `_build_wf_ctx` 還原 raw G），逐代對拍 Y 版 baseline | `wg_g3.py` byte-perfect | wg_g3.py diff · G.3 綠 |

**push 節奏**（KL 授權可分批）：Y.0 → push → claude.ai pull 分件驗 → Y.1 → push → ... 逐子波獨立收官。

## 五、風險與停機規則

### 風險

1. **sub-cent 移動幅度未知**：可能只有 0-2 格微動、也可能大量鏈式漂移。若後者，Y 波不只是「重烤」而是「引擎行為變動」——需上呈 KL 判定是否可接受。
2. **6 格 GSA 錨移動**：`wf_f0.py:54-59` GSA_EXPECT 六格錨（G006/G007/G009/G010/G014/G017）若因 sub-cent 移動 > 0.01，需**重寫錨**（如 v3 勘誤重烤同）。
3. **UC9898 stress test**：若 harness 帶 ghost 進 Step G 後產出新 g_row 撞其他錨（如 `MinA_QU=114.07`、`TIER3_LOTS`）—— 需獨立核實各錨仍成立。

### 停機規則（Y 波專屬）

- **停機 Y1**（sub-cent 未定位）：Y.0 施工前若 sub-cent 差異點三處實查完仍不明，**停手上呈 claude.ai**，禁憑推理硬改。
- **停機 Y2**（錨移動）：任一硬寫錨（GSA_EXPECT／MINA_QU／TIER3_LOTS 或引擎其他錨）於 Y 版變動 > 0.01㎡ 或 > 5% 相對移動，**停手上呈 KL 域裁**（同 #14 刀口值不猜）。
- **停機 Y3**（守恆/⊥/位次結構閘破）：任一 Y 子波後 `run_all.py` 之結構不變量閘破，**停手不推**，回溯定位（非直接調容差湊靶）。
- **停機 Y4**（非 mechanical rebake）：若必須動 `wf_f0~f4` 引擎邏輯才能綠（非只換 baseline 值），**停手上呈**——這超出「機械性重烤」範疇、屬於引擎行為變。

### 收官前置（未 push 不得報收官·最高紀律）

`git rev-parse origin/main` 已含該 commit 才是收官；本地綠、gate 45/45、reviewer 部分過皆非收官。
Y 波完成後上呈之報告與 CLAUDE.md 更新，皆須驗 `origin/main` 已含後才寫、才報。

## 六、開工前檢核清單（Y.0 動工前逐項確認）

- [ ] `app.py` 未 commit 之 117 行 GIS 顯示變更（KL 2026-07-13 裁 A 原地號 dissolve）→ **與 Y 波無關、先保留**（不 stash 亦不 commit，Y.0 開檔案時避開這幾段）
- [ ] `.tmp.driveupload/` 未追蹤目錄——非本波產物、跳過
- [ ] Plan 由本報告延伸撰寫、reviewer 審 plan、KL/claude.ai 核可子波序後方動工
- [ ] Y.0 施工前先寫 harness vs live g_rows 逐格 diff 工具（sub-cent 定位器），供 Y.0 決策具體修法

## 七、附錄：關鍵行號索引

| 主題 | app.py | verify/ |
|---|---|---|
| build_parcels 過濾 | 13407-13410 | selection_pipeline.build_build_parcels |
| Step G 主迴圈 | 14526（parcels_by_block）～ 15466（碎片合併結束）| stepg_pipeline.run_step_g L81-848 |
| f3_G_values 寫入 | 15471 | 無（回傳 dict） |
| Patch B-2 於步驟 J | 16146-16198 | **無**（Y.0 補） |
| ghost 排除 | **無**（14528 不排）| 228-232（Y.0 移除） |
| `_build_wf_ctx` 出艙還原 raw G | 8102-8108 | 無（app 真函式）|
| ghost 定義 | 4213-4228 | 無 |
| Patch B-2 helper | 5288-5335 `_compute_strip_width` | 無 |
| wg_g3 `_seed_ctx` | 無 | wg_g3.py:78-104 |

---

## 八、三 Q 補完（2026-07-14 之二，claude.ai 裁定「未定位 sub-cent 前不進 Y.0」後補查）

### Q2 補完：Patch B-2 是否改寫 G 值本身

**證實**：Patch B-2 **確實改寫 G 值本身**——非純 tag。`app.py:16189-16191`：

```python
if _orig_G >= _min_a_jw and _min_a_jw > 0:
    _r_jw['_G_before_width_violation'] = _orig_G      # 存 raw
    _r_jw['G(㎡)'] = round(min(_orig_G, _min_a_jw - 0.01), 2)   # ← 壓縮 G(㎡)
```

**但**淨效應對 wf_f0~f4 消費 gA 而言為零，因 `_build_wf_ctx`（`app.py:8106-8108`）出艙時**逐列還原**：

```python
"gA": [({**_r, "G(㎡)": _r["_G_before_width_violation"]}
        if _r.get("_G_before_width_violation") is not None else _r)
       for _r in _need("f3_G_values")],
```

- 有 `_G_before_width_violation` → 還原 raw G
- 無 → 讀 f3_G_values 之 G(㎡)（未壓縮之原值，`_orig_G < _min_a_jw` 分支）

**且**：`grep _G_before_width_violation verify/` 零命中——harness 產出的 g_rows **從未有此欄位**，`_build_wf_ctx` 之還原分支對 harness 種子恆為 no-op。verify/ 4 處寫 `f3_G_values` 皆用 `sg["g_rows"]`（harness 直出）：
`wg_g2_smoke.py:43`、`run_verification.py:1072`、`wg_g1_smoke.py:65`、`wg_g3.py:88`。

**Q2 定案**：採 (b)——harness 不加 4 欄，g_rows 天生為 raw G。此結論**不依賴** Patch B-2 是否為 tag（已確認是**改寫 G**），而依賴「`_build_wf_ctx` 是所有 wf_* 之唯一入口」——證實。

### Q3 補完：wf_f1~f4 ghost-aware 邏輯 grep 實證

**非零命中**，具體：

| 檔 | 行 | 語境 | 屬性 |
|---|---|---|---|
| wf_f1.py | — | 無命中 | — |
| wf_f2.py | 51、55 | `_block_pre_avg` 迴圈內 `if tp.get("_is_ghost_sliver"): continue` | 幾何加權·**輸入端排 ghost** |
| wf_f2.py | 94 | `_proj_order` 內 `not tp.get("_is_ghost_sliver")` | 幾何投影序 |
| wf_f3.py | 77、107、115 | 類 `_proj_order`／幾何函式內 filter | 幾何 |
| wf_f4.py | 818、1281 | 類 `_proj_order`／終態幾何 | 幾何 |

**上列 filter 皆為輸入端讀 parcels 之保護**（避免 ghost 缺 polygon_coords 或零面積出錯）——Y.0 後
**應保留**（拿掉會撞幾何 NaN）。**改點不含這些**。

**但**更嚴重的發現——**12 處「推進側別 in ('left', 'right')」filter 皆未排 ghost**：

| 檔 | 行 | 語境 |
|---|---|---|
| wf_f0.py | 83、178、194 | A dict（gA/sgB）／B dict（sgB） |
| wf_f1.py | 140 | lots_B list |
| wf_f2.py | 128、187 | B（rows_B）、C（sgC） |
| wf_f3.py | 102、163 | C 家族／D（sgD）|
| wf_f4.py | 145、313、1068 | 多處 trunk B/C/D/E |
| run_verification.py | 542、1146 | 財務閘·A 逐宗閘 |

**若 Y.0 拿掉 stepg L228-232**，ghost 列進 g_rows 後：
- 進 Step G 迴圈（app.py:14528）→ 分至左右 group（14481-14520）→ 產出 `推進側別='left' or 'right'` 之 ghost 列
- 進 wf_f0:83 之 A dict → ghost 列 G=a=0、`原地號='_GHOST'`、`omap.get('_GHOST', '')=''`
- wf_f0:87 `cell.setdefault((gof(r["原地號"]), r["所屬街廓"]), []).append(r)` → gid='' 之空歸戶群，若 len ≥ 2 會觸發級 0/0' 決策——**污染路徑**

### Q3 定案

**改點清單**（Y.0 完整範圍）：

1. **改點 A**：`verify/stepg_pipeline.py:228-232` 拿掉 ghost 過濾（`if tp.get("_is_ghost_sliver", False): continue` 段）
2. **改點 B**：上列 **12 處**「推進側別 in ...」filter 補 `and not r.get("_is_ghost_sliver")`，防污染 A/B/C/D/E dict
3. **保留**：`wf_f0:141`、`wf_f2:94`、`wf_f3:77/107/115`、`wf_f4:818/1281` 之 `_proj_order` 家族內 filter（輸入端幾何保護，正確）

**替代方案**（決策上呈）：保留 stepg L228-232（不拿掉），改為 stepg 內另加**尾部空 ghost 標記列**（`推進側別='ghost'` 或不設）——優點：wf_f0~f4 之 12 處無需改；缺點：與「harness 吃 live」精神不完全對齊（live g_rows 之 ghost 列 `推進側別='left/right'`）。**傾向**：改點 A+B 完整方案（真同源）。上呈 claude.ai 裁定。

### Q1：dump 對拍工具草案（等 KL localhost live g_rows dump）

**dump 對拍工具骨架**（Y.0 前建置，等 KL live dump 執行）：

```
verify/tools/y_dump_diff.py（新建）
  - 讀 KL 提供之 live_g_rows.json（app localhost st.session_state['f3_G_values'] dump）
  - 跑 harness native pipeline 產 harness_g_rows.json（同雙情境）
  - 逐列（by 暫編地號）逐欄 diff
  - 分類：
    * 【tag 欄】（_below_min_width/_width_violation_note/實際寬度/_G_before_width_violation）
      → live 有、harness 無、預期
    * 【ghost 列】（_is_ghost_sliver=True 之列）
      → live 有、harness 無、預期
    * 【計算欄差異】（G(㎡)/S(m)/W(m)/迭代次數/area_geom/是否收斂）
      → **關鍵**：sub-cent 分岔點定位
  - 輸出：
    * y_dump_diff_退縮0m.csv（逐格）
    * y_dump_diff_退縮3.5m.csv（逐格）
    * y_dump_diff_摘要.md（分類統計＋top-20 顯著差異）
```

**Q1 診斷重點順序**（claude.ai 裁）：
1. **迭代次數/收斂路徑差異**（最可疑；14 宗迭代次數不同——查 `solve_G_binary` 之 S₀→S 中間量精度、收斂判據 `tol=0.01`）
2. **area_geom** 差異（shapely `buffer(0)`／版本相關；`_res['area_geom'] = round(_r.get('S', 0) * _avg_depth, 2)` 或 cut_coords 幾何差）
3. **Patch B-2 改寫 G**——已證：Q2 定案（純 tag/改 G 已明；`_G_before_width_violation` 還原鏈完備）

**KL 待辦**：localhost 跑一次至步驟 G 完成後，於 UI 或 debug console 執行 `st.session_state['f3_G_values']` dump 至檔（雙情境）→ 交 CC 進 Y.0 定位。

## 九、開工前檢核清單更新（Q3 補完後）

- [x] Q1：dump 對拍工具骨架設計完成、等 KL live dump 執行
- [x] Q2：定案 (b)（harness 不加 4 欄、序列化不濾——因 harness g_rows 天生無這 4 欄）
- [x] Q3：改點清單完整——A + B（12 處 filter 補），或替代方案（保留 stepg filter）上呈 claude.ai 裁
- [x] KL live dump 提供（2026-07-14）→ CC 建 `verify/tools/y_dump_diff.py` → **不是 sub-cent·財務同源性重大問題**（詳 §九）
- [x] Q3 定案（claude.ai 裁 2026-07-14）：改點僅 stepg 一處，wf_f0~f4 之 12 filter 一字不動，加閘顯性化「ghost 天然無推進側別」隱含前提。`failure-archaeology` 新一課：「多處 filter 共依同一隱含前提時、修法是把前提釘成一閘、非逐處加防禦」
- [ ] **上呈 KL 域裁**：後街廓單價之財務同源性衝突（§十）；未解前 Y.0 plan 撰寫暫停

---

## 九、Q1 對拍結果（2026-07-14 之三·KL live dump 提供後）

### 執行環境

- KL 於 localhost 分雙情境（退縮 0m / 3.5m）跑至步驟 G「G 值計算結果」dataframe 出現、按下 dump 按鈕（app.py:15607-15637 · Y 波診斷專用）→ 交 CC 兩份 JSON：
  - `verify/out/y_dump/f3_G_values_退縮0m_livedump.json`（81KB · 70 列 · 含 2 ghost + 9 抵費地）
  - `verify/out/y_dump/f3_G_values_退縮3.5m_livedump.json`（84KB · 72 列 · 含 2 ghost + 9 抵費地）
- CC 建 `verify/tools/y_dump_diff.py`（172 行），讀上述 JSON + 跑 harness `run_step_g` 逐列 diff。

### dump 之驚人發現：Patch B-2 未觸發（改寫 dump 位置解讀）

三 Patch B-2 附加欄 **全 0 命中**（`_below_min_width` / `_G_before_width_violation` / `實際寬度(m)`）——因 dump 按鈕位於**步驟 G**（app.py:15607）、**步驟 J**（app.py:16146-16198 之 Patch B-2）尚未執行時。

**結論修正**：dump 內容＝raw g_rows（step G 直出），Q2 (b) 定案更加穩固：**wf_f0~f4 之計算路徑上，Patch B-2 完全不出現**——即使 KL 之 localhost dump 已在按下 dump 按鈕前執行過完整 step J 而後又 rerun 只走到 step G，dump 也只反映當下 f3_G_values 之最新狀態（raw）。

### 對拍結果：**大範圍系統性差異、非 sub-cent**

| 情境 | live 列數 | harness 列數 | 交集 | only-live | 總欄差異 |
|---|---|---|---|---|---|
| 0m | 70 | 68 | 68 | 2 (ghost R1/R4) | **495** |
| 3.5m | 72 | 70 | 70 | 2 (ghost R1/R4) | **491** |

**分類統計（0m）**：

| 分類 | 差異數 |
|---|---|
| ①迭代/收斂 | 40 |
| ②area_geom | 64 |
| ③Patch B-2 | 0 |
| ④ghost | 0（ghost 於 only-live·不進交集） |
| ⑤其他（A/G/S/W/Rw/宗地寬度/累積S） | **391** |

**欄別 max abs diff（0m）**：

| 欄 | 差異列數 | max abs diff |
|---|---|---|
| 幾何面積(㎡) | 64 | **109.5** |
| A 地價比 | 59 | **0.1857** |
| G(㎡) | 57 | **32.05** |
| 累積S(m) | 58 | 1.26 |
| S(m) | 50 | 0.69 |
| 宗地寬度(m) | 50 | 0.69 |
| 迭代次數 | 40 | 7 |
| W(m) | 34 | 1.15 |
| Rw(%) | 24 | 1.82 |

**這絕對不是 sub-cent 範疇**——G 最大差 **32.05㎡**、A 最大差 **0.1857**、迭代次數最大差 **7 步**。

### 根因定位：**財務快照之後街廓單價分組錯**

per-block A 地價比之 diff（0m）：

| 街廓 | live A(a或b) | harness A（snap） | 差 |
|---|---|---|---|
| R1 (a) | 1.7364 | 1.7206 | +0.0158 |
| R2 (b) | 1.8386 | 1.9230 | **−0.0844** |
| R3 (a) | 1.6496 | 1.5486 | **+0.1010** |
| R4 (a) | 1.7364 | 1.7206 | +0.0158 |
| R5 (a) | 1.6496 | 1.5486 | **+0.1010** |
| R6 (a) | 1.5628 | 1.7206 | **−0.1578** |

**Snapshot 之後街廓單價（`verify/case_params_UC9898.json:財務接線_v3.後街廓_面積單價`）**：

| 街廓 | 面積(m²) | 單價(元/m²) |
|---|---|---|
| R1 | 2893.55 | **75551.12** |
| R2 | 4368.60 | 71773.56 |
| R3 | 4206.80 | 67996.00 |
| R4 | 3207.87 | **75551.12** ← 與 R1 同 |
| R5 | 4150.21 | 67996.00 ← 與 R3 同 |
| R6 | 3976.30 | **75551.12** ← 與 R1/R4 同 |

**Snap 之分組**：{R1, R4, R6} 同單價 75551.12；{R3, R5} 同單價 67996.00；R2 獨（71773.56）。

**app live A 之分組**：{R1, R4} 同 1.7364；{R3, R5} 同 1.6496；R6 獨（1.5628）；R2 獨（1.8386）。

**⚠️ 分歧點**：Snap 把 R6 分至 {R1/R4/R6} 同單價；app live 把 R6 分至獨立第四組（單價低於 R1/R4）。

（3.5m 情境 A 差之模式完全相同：R3/R5 同 +0.1010、R1/R4 同 +0.0158、R6 獨 −0.1578、R2 獨 −0.0844。）

### 下游連鎖（皆為果·非獨立分岔）

- **G(㎡) max 32.05㎡**：A 地價比為 G 公式之乘子（`solve_G_binary(A=A_ratio, ...)`），A 差 → G 差；R6 628-4(1) live=692.05 vs harn=660.00，差 +32.05 對應 R6 之 A 少 0.1578。
- **迭代次數 max 差 7**（R2 628-41(1)：live=18 vs harn=11）：因 G 目標值不同，binary search 收斂步數自然分岔。**非** solve_G_binary tol 之獨立問題。
- **幾何面積 max 109.5㎡**：`_res['area_geom'] = round(S × avg_depth, 2)`，S 差（0.69m max）× depth（30-45m）→ 差可達 100+㎡；**非** shapely 版本差。
- **W/Rw/宗地寬度/累積S**：皆隨 A → S 連鎖動。

**修財務快照分組 → 上列所有差異應歸零（僅留 sub-cent）**。

## 十、觸發停機 Y4：**上呈 KL 域裁**

依 CLAUDE.md「意思決定不自動裁、標旗呈 KL」與偵察報告 §五之停機規則 Y4（非機械性重烤 → 停手上呈）：

**核心問題**：`case_params_UC9898.json.財務接線_v3.後街廓_面積單價` 之**分組**與 app live 分歧——
snap 把 R6 分入 {R1/R4/R6} 同單價 75551.12；app live 把 R6 獨立為第四組（單價明顯較低）。

**兩個候選裁法**（KL 抉擇）：

- **裁 A（採 app live 值）**：`case_params_UC9898.json` 之後街廓單價**逐街廓獨立**（6 街廓 6 值），非 3 組（R1/R4/R6、R3/R5、R2）。若採此路：需 KL 提供 6 個街廓之各自 live 單價值（可由 dump 反推：`post_R? = live_A × pre_price`，pre_price 兩區段從 snap 讀），CC 更新 snap → 全鏈重烤（Y.1~Y.5）→ Y.6 G.3 重跑。
- **裁 B（採 snap 值）**：app live 於某處計算後街廓單價之邏輯**有 bug**（把 R6 分錯組），需修 app.py。若採此路：需 KL 提供 app live 之後街廓單價計算路徑（Tab 5 之土地開發分析法輸出？），CC 追查 app.py 是否誤把 R6 分入獨立組。

**衍伸問題**（KL 順裁）：

- Snap 之單價由何處而來？是「土地開發分析法」（Tab 5）之各街廓分析結果、抑或某階段之簡化平均？
- CLAUDE.md 已鎖定「重劃後均價源＝土地開發分析法」（KL 2026-07-12 裁定）——**均價**明確，但**逐街廓單價**是否也來自同源？

### 不是 sub-cent → Y 波原範疇修正

Y 波原界定為「機械性重烤」（框架借鑒 v3 勘誤重烤 b288446）——但**上列問題是財務快照分組結構性問題、非重烤能解**。修畢分歧後（無論 A/B 路）**才**是機械性重烤。

**建議 Y 波序修正**：Y.−1（新增·前置）解決財務快照分組（KL 裁 A 或 B）→ 原 Y.0~Y.6 續。KL 未裁前 Y.0 plan **不撰寫**。

### 收官前置（仍舊）

不變：`git rev-parse origin/main` 已含該 commit 才是收官。Y 波之財務快照修正屬**結構性差異修正**，比 v3 勘誤重烤更廣範圍。
