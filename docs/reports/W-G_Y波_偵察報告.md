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
