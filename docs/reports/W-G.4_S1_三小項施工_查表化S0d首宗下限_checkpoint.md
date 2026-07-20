# W-G.4 S1 三小項施工 checkpoint（§6 查表化＋§5 S0d＋首宗下限）

- 日期：2026-07-20；branch `wip/s1-endpart`（基準 `0e50eac`）；**未 commit·未 push·未收官**
- 狀態：三小項施工完成·三檔 py_compile 綠；**redistribution-reviewer 獨立複驗 PASS（無 BLOCKED·三聚焦判斷 A/B/C 皆經 grep＋算術＋打樣報告交叉坐實）**；兩則 NOTE 已處置；run_all 現紅屬預期（W脫鉤/step0 致 G 全數重定·baseline/UC9898 硬錨未重烤·handoff §五·重烤解）
- 次步：KL 確認 → band(§3)＋N0-20(§4)（最大塊·#25 死因側參數化）

## reviewer verdict（redistribution-reviewer·獨立復現·全 PASS）

- **項A §6 PASS**：byte-identical for UC9898 係**構造性保證**（新注入之 `get_min_lot_size(分區,正面路寬)['min_width']` 與引擎既有 golden `f3_min_width_by_label`〔stepg:200／app:14035〕**同一 call**·非巧合）；兩注入點皆 precede v12（v12 全庫僅二呼叫端·皆有注入）；靜默 3.5 真刪·無 dangling。
- **項B §5 PASS**：app 四處補全（plan §5 漏列）**正確且完備**（grep 全引擎 `_S_actual`／`res.get('S'`＝唯四處餵 cum_S·全改 S_raw）；app 迴圈確 live 產 f3_G_values（15644→16015）；閘寬移項係**刪項非湊殘餘**（#21 自查過·變緊 14×·有鑑別力）；未誤改顯示/畸零寬之 2dp 消費端。
- **項C 首宗下限 PASS**：`res['W']==W_far` 坐實（同源 W_conv·≠W_near）；打樣 R3右0m「首宗W=6.31」≠near(1.75)·ΣRw=100−R(1.75)=77.34 對上表值 → 遠側量取正確；loud 非 raise·stepg-only 符 plan §8。
- **守恆/鐵則**：本 diff 未觸池/ledger/守恆彙總·四欄面積唯讀性·Rw 差額式·未偷做後波——皆完好。
- **NOTE 已處置**：①`_S_ROUND_HALF` 註明為 S0d 後不入閘之概念記錄（保留·供 docstring 引用）；②`_acct_geom_tol_block` docstring 陳舊公式更正（移除 0.005×深度 項）。③（泛化行為·UC9898 不觸·no-silent 方向·記錄不改）。
- **誠實邊界（reviewer 明列）**：數值綠（重烤後 0.015 閘、byte-perfect 逐格零 diff、守恆實測）**須待 plan step 7 重烤**方能算——本審只證碼面/算術/plan 相符·run_all 現紅屬預期外延、非 diff 瑕疵。域判斷（首宗遠側 W 之物理正當性、S0d G 微移屬預期中間態）交 KL＋claude.ai。

---

## 0. 進度盤點（plan v3 §9 八項）

| 項 | 態 | 本 checkpoint |
|---|---|---|
| §2 step 0 | ✅ 前波（0e50eac）| — |
| §1 W脫鉤（乙定案）| ✅ 前波 | — |
| **§6 查表化** | ✅ 本波 | v12 min_width 查表注入＋setback loud |
| **§5 S0d** | ✅ 本波 | 實切/推進全精度同源·四處推進·閘寬 |
| **§1/§2 首宗下限 loud** | ✅ 本波 | stepg 閘·res['W']≥退縮+min_width |
| §3 街角 band | ⏳ 次 | side 參數化（#25）|
| §4 N0-20 末筆 | ⏳ 次 | R_end／勝者／常數項 |
| 一次重烤 | ⏳ 末 | 逐一回綠·歸因閘 |

---

## 1. §6 查表化（plan §6·補丁六 §四）

**改動（3 edit·app==engine 同源）**：
- v12 `select_corner_lots_both_sides_v12`（`app.py` Patch B-4）：`_legal_min_width_B4` 舊 `_blk_param_B4.get('法定最小寬(m)', 3.5)`（`f3L_sb_rows_by_label` **全程無人寫入·selection_pipeline:272 坐實**→恆 3.5）→ 改讀 session `f3_pk_legal_min_width`（**loud raise 若缺·禁靜默 3.5**）。
- 注入兩處：`app.py` PK 迴圈＋`verify/selection_pipeline.py` run_corner_pk（`f3_current_pk_block` 設處旁）各以 `get_min_lot_size(分區, 正面路寬)['min_width']` 注入。
- v12 setback `f3L_setback_default` 舊靜默 3.5 兜底 → **loud raise**（保留 0.0 合法·0m 情境）。

**byte-identical for UC9898（歸因閘＝ΔG≡0）**：全街廓住宅區·正面路寬 R1/R4=12m·R2/R3/R5/R6=8m（`case_params_UC9898.json`）；`HUALIEN_MIN_LOT_TABLE` 住宅區 8m→3.50·12m→3.50（同檔·`case_params:26` KL doctrine「巧合非常數」）＝舊硬編值 → v12 min_width 3.50→3.50、setback 0/3.5 保留 → 街角範圍不變 → PK 不變 → G 不變。**最終 byte 證於重烤歸因閘。**

---

## 2. §5 S0d（plan §5·補丁四 §二·S0c 修向反轉）

**改動**：
- 實切 `solve_G_binary`：`_S_cut = round(S_conv,2)` → `_S_cut = S_conv`（未捨入）。
- res dict：新增 `'S_raw': S_conv`（全精度）；`'S'` 仍 round 2dp（顯示）。
- 推進**四處**：`_S_actual = float(res.get('S', 0.0))` → `res.get('S_raw', res.get('S', 0.0))`。
- 閘寬單源 `_acct_geom_tol_per_lot`：移除 `_S_ROUND_HALF × depth` 項 → `tol(0.01)+G_round(0.005)=0.015`（S0d 後 S 量化退出計算路徑·#24）。

**🚩 發現一：plan §5 漏列 app 推進兩處（#20 同機制多實作點）**
plan §5 只列 stepg 推進兩處（550/636）。實測 `app.py:_advance_block_with_split`（~15486 左／~15586 右）為**平行複本**且 **live**（呼於 ~15638/15641/15662 → 產 `f3_G_values`＝app 權威 G）。G.3 已證 app-path==重烤 baseline byte-perfect → 若只改 stepg，app 推進仍吃 2dp S、app≠engine、G.3 破。**依 #20「修一機制須全庫掃同類」補全 app 兩處**（共四處）。wf_f1/wf_f4 `strip_at` 取 S 為 param（池重算·另一機制）→ 非 S0d 標的。此屬 plan 漏列之碼面補全（非域裁）·送 reviewer 覆核。

**第四源不重引（#23）**：S0d 之解＝推進與實切**同源於全精度**（非 S0c 之同源於捨入）→ 縫/疊 by construction 歸零·②-宗圍堵閘 ≤1e-6 不變。algebraic fallback（`iterate_G_S`·無 S_raw）之 `.get('S_raw', 'S')` 退 'S' 屬正確（algebraic 路徑無「切捨入 vs 推進未捨入」分裂·其 S 一致用於 area+推進）·且 app==engine 同退。

---

## 3. 首宗下限 loud（plan §1·補丁六 §二）

**改動（僅 stepg·5 edit）**：`run_step_g` telescoping 閘旁新增閘——達資格街角首宗 KL W ≥ 退縮＋min_width，不達 **loud print（非 raise·補丁六 §二「記錄/警示·禁硬釘」）**。量取＝`_advance_block_with_split` 捕獲首宗角落宗 `res['W']`（`Wfirst_left/right`）；下限＝`setback`（run_step_g 參數）＋`f3_min_width_by_label[blk]`（查表·禁字面 7/3.5）。

**🚩 判定二：「首宗 W₁」＝ `res['W']`（==`res['W_far']`·both round(W_conv,2)），非 W0=`res['W_near']`**
依據＝W脫鉤打樣報告表列「首宗W」（R3右0m=6.31）≠ telescoping W0(near·=−δ=1.75)；且 ΣRw=R(末far=30.15)−R(首near=1.75)=100−22.66=**77.34** 對上報告 R3右0m ΣRw=77.34 → 坐實「首宗W(表)＝far、非 near」。現值 UC9898 首宗 W≈7.03≥7（3.5m 下限）→ 閘靜默（斷言滿足）；6.92 係 pre-W脫鉤 artifact。**stepg-only** 正確（plan §8「app 無 telescoping 閘」·app 首宗資料經 G.3 app==engine 覆蓋）。**此判定送 reviewer 覆核**（若實應為 W_near 或 lot 寬度則量錯）。

---

## 4. WATCH（非本波標的·記錄供 reviewer/KL）

- **`_pw = round(S,2)×cos_dn`**（app:~15403／stepg:~459·畸零地寬度判定）仍讀 2dp `S`（非 S_raw）。S0d 只界定實切+推進；`_pw` 為另一量·app==engine 一致（不破 byte-perfect）·且 CLAUDE.md「判畸零用 W 不用 S」→ `_pw` 用 S 恐屬既存另一議題·非 S0d。未改·flag。
- **`iterate_G_S` fallback 無 S_raw**：罕用退路（幾何解失敗才走·UC9898 不觸）·`.get` 退 'S' 正確（見 §2）。

---

## 5. 未決／待辦

1. reviewer verdict（三項·特聚焦 §1 UC9898 byte-identical／§2 app 四處補全／§3 首宗量取 res['W']）。
2. reviewer 綠 → commit（**僅 3 碼檔·不含 data xlsx**·handoff §七 flag）→ KL 確認 → band+N0-20。
3. 重烤在末（八項齊備後一次）·非本 checkpoint。
