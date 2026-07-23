# W-G.4 P2 兩階段落位引擎化 — 新 session 施工交接文

> **給下一個 CC session**。P1／P5／W-8／B-5 已完成並 push；**P2（引擎兩階段化）未動**，本文即其施工細部。
> **行號基準＝`24d02ba`**（本文所有 檔:行 於該 commit 重新實測錨定，非沿用舊 plan 之數字）。
> 動工前先 `git log -1` 確認 HEAD；若已前進，**行號一律重新 grep**，禁憑本文數字施工。

## 〇、開機必讀（順序）

1. `CLAUDE.md` 全文——尤**守恆式最高鐵律**（`ΣG + 池 = 街廓 DXF 面積`）、未 push 不得報收官、no-silent-fallback。
2. `docs/specs/W-G.4_KL域裁_兩階段落位_部分面積拆分_Rw側選.md`——KL 裁定 A/B1–B5/C–K ＋手冊道路五原則（**canonical·原文**）。
3. `docs/specs/W-G.4_兩階段落位_plan_v3.md`——**尤 §十一（reviewer BLOCKED×5＋WARNING×10 之裁決）、§十二（上呈項）**。本文＝§十一 之可執行化。
4. `docs/reports/W-G.4_§4_兩階段落位_坐實.md`——root cause 實證（含重跑指令）。
5. `.claude/skills/`：`wave-discipline`（凍結欄框架）、`no-silent-fallback`、`stop-conditions`、`validation-runbook`、`failure-archaeology`。

## 一、現況（已完成·勿重做）

| commit | 內容 |
|---|---|
| `5599b25` | 裁定J（S-2 結案）＋手冊道路五原則（S-1 結案）＋修正一二三掃入 spec／plan |
| `bb78460` | `wf_f0` 孤兒常數 `MINA_QU` 刪（零讀取·全倉無 import） |
| `34274a0` | 修正一：`wf_f4` ½線口徑去字面硬編 → `mina_qu = min(mina.values())`（**零行為變更**·實測 min=114.07 argmin R4） |
| `904cfb0` | reviewer 裁決入 plan §十一／§十二 |
| `712ce59` | **P1** 階段旗標 ＋ **P5** 裁定K 單一類別佇列／裁定H/J 逐筆計價／RD 派工閘 |
| `24d02ba` | **W-8** `_WF_NS_NAMES` 補 `_strip_axis`/`_end_region_R`（app 路徑 latent KeyError）＋**B-5** 補 `_build_corner_range_v2`＋ns 閘改雙向 |

**P1 旗標已在但無消費端**：`wf_f4.add_syn` 產出之合成宗帶 `"配地階段": "池內"`；原生 `build_parcels` 不帶此鍵＝階段1。**P2 即是它的消費端。**

## 二、要解決什麼（一句話）

`run_step_g` 目前把**原地主宗**與 **wf_f4 池內遞補合成宗**混成**單一投影序列**推進，遞補插隊把原地主末宗擠爆（3.5m 之 `628-37(1)`：`S_remain=8.57 < 需 8.81` → `|G−幾何|=7.9`）。
P2＝**拆成兩階段**：階段1 只排原地主（定案並定出池範圍），階段2 才在**池範圍內**落位遞補宗。

## 三、施工步驟（依序·每步一 commit·每步 py_compile＋§六 驗證）

### P2-a　階段1 過濾（含 B-2 必辦）

- `verify/stepg_pipeline.py:382` `_spatial_order_parcels_v2(parcels_in_block=parcels_in_blk, …)`
  → 輸入改 **僅階段1宗**：`[tp for tp in parcels_in_blk if '配地階段' not in tp]`。
- ⚠️ **B-2（reviewer 活抓·漏了必 raise）**：`stepg:399-401` 之 `_proj_rank` 用的是**未過濾**的
  `parcels_in_blk` → 過濾後 `pre_position`（1,2,3,4）與 `_proj_rank`（1,2,4,9）對不上，`:407` 必 raise。
  → `_proj_rank` **母體同步過濾**（或直接以 `ordered_v2` 之 tp 清單建 rank）。
- 建議把「階段1宗清單」算一次存區域變數，兩處共用，杜絕再分岔。

### P2-b　新函式 `_place_pool_parcels`（單一真相源）

- **放 `app.py` module 級**（`_pool_strips_for_block` 附近），**加入 `_WF_NS_NAMES`**，stepg 經 `ns` 取用。
  **禁 fork**（同 `_oblique_s_max`／`_corner_buffer_S` 先例）。
- 職責：於**池範圍內**逐筆落位階段2宗，回傳 rows ＋ **實際落位面積**（見 W-4）。
- 幾何：帶軸＝`_strip_axis`（app.py:6851 家族）；S 預算＝**池 s-區間**，非全街廓。
  面積→G 仍走既有 `solve_G_binary`。

### P2-c　B-5：18m 範圍即算即用（D-3 寬度制）

- `ns["_build_corner_range_v2"](side_mid, verts, centroid, alloc, 18.0, None)` **即算即用**——
  **禁**存 session 新鍵（session 走 `_WFSessionShim`、與 ns 無關；且 harness 從不算 18m）。
- 輸入引擎側齊備：`cb_by[lbl]["vertices"]/["centroid"]`＋`cad["side_lines_by_side"][lbl][w]["mid"]`＋`cad["alloc_dir_by_block"][lbl]`。
- **跨占寬度**＝`池範圍 ∩ 該側18m多邊形` 於 `_strip_axis` 之 **s-區間長**。
  ⚠️ **NOTE-1**：`_strip_s_range` 回的是**全體 span** 非實占長（雙片池會虛胖）→ 須取**各連通片 s-區間長之和**。
- **一次交集、二處消費**（B5 側選用其長度；裁定F 用其 >0 與否），**禁兩套幾何**。

### P2-d　B5 側選＋裁定F 負擔（W-2 必辦）

- 側選：跨占大之側先配；每配一筆**重算兩側跨占**；兩側皆 0 → tie-break：**池 s-區間較長之側；再同 → 左**（決定性·禁擲硬幣）。
- **W-2 契約（漏了 4/6 塊 G 暴跌）**：裁定F 之 Rw 必須是**單一 `if 跨占>0` 分支**。
  中央池宗 W≫18m ⇒ `rw_from_width(W)=100%`；若誤走「先查 W→Rw 再看跨占」會被多掛滿額側街負擔。
  **無跨占 ⇒ 傳 `l_side_use=0, F_use=0`** ⇒ `'F(m)'=0`（`stepg:274` 家族）⇒ 自動被
  `_rw_real_wd2` 之 `F>0` 濾掉（`stepg:842` 家族）、telescoping 鏈亦不推進。
- 正街負擔**無條件掛**（G 公式既有 S 項）。

### P2-e　B-1：接線（**最險·錯了靜默破守恆且閘抓不到**）

> reviewer 實證：`g_rows` **只是輸出容器**；守恆帳來源是 `_adv_final['rows']`（`stepg:814/:824/:923` 家族）與 `allocated_polys`（`:738/:755` → `:767`）。

- `_place_pool_parcels` 必須**就地擴充 `_adv_final`**：`rows` / `left_results` / `right_results` / `Wf_left` / `Wf_right`（`_adv_final` 結構見 `stepg:670-677`）。
- **插入點＝`stepg:728`（`g_rows.extend(_adv_final['rows'])` 之前）**。
  ⚠️ **W-10**：`_adv_final` 有**兩個**產生點——`:686`（degenerate／`N≤1` 分支）與 `:727`（正常分支）；
  插入點須在 **if/else 匯流之後**（即 `:728` 位置），否則 degenerate 分支漏接。
  兩階段化後 `N≤1` 機率**上升**（過濾後 R4 只剩 2 宗）。
- 三種錯法的後果（reviewer 算術）：只進 `g_rows` ⇒ 池帶仍覆蓋階段2宗、抵費地列**重算一次** ⇒ 守恆實破 `+ΣG_階段2` 而**閘全綠**；只進 `_adv_final` 或只進 `allocated_polys` ⇒ 停機③ 立紅。
- 池片結算（`:767`）改於階段2 落位**之後**（池＝階段1殘餘 − 階段2已落位）。

### P2-f　B-3：末端塊時序（**原 plan 寫法幾何上不可能**）

> `_end_region_R`（app.py:7214 家族）第 5 參數即 `frag_poly`，空即 raise；`frag`／`side` 嚴格**下游**於 `_pool_strips_for_block`（`wf_f1` 只從池片列取碎片）。故**不能**放在「池片結算前」。

- 正確時序：**階段1 定案 → 先算一次池片 → 分類碎片 → 末端塊判定/落位 → 階段2 → 重算池片**。
- 兩次 `_pool_strips_for_block` 的守恆帳：**以第二次為準**；第一次**僅供碎片分類**，不得進帳。
- 可前移者僅 `_end_gate` 之**判定**（`_cond1` ＝ `fo['{side}_has_side']`＋`_unfront_area`）；
  winner 門檻 `G ≥ area(R_end)` 與 fallback 落位**不可**前移。
- `wf_f4:1242` `_end_gate` / `:1165 _reshape_block` / `:1209 strip_at` 為現落點。
- ⚠️ **NOTE-3**：E3 `strip_at` 自角落**連續重鋪**——階段2 與階段1 末宗間若留空隙，E3 會**吃掉並前移**
  （只驗 G 全等、不驗位置）。⇒ **硬約束：階段2 落位必須與該側階段1 鏈連續。**

### P2-g　W-3／W-4／W-5（帳與收斂）

- **W-3 telescoping**：`ΣRw_側 == R(W_final) − R(W₀)`（`stepg:848-863`）代數成立，但依賴
  (a) W **單調不減** ⇒ 階段2 必**自該側自己的池邊界往街廓內**推進（禁從對側起切，否則 W 倒退、閘立破）；
  (b) `Wf_left/Wf_right` 由 `_place_pool_parcels` **續推並寫回**（同 B-1）。
- **W-4 回饋通道（原 plan 缺）**：`spill_75`（`wf_f4:540`）是**單向出口**（`:517-518` 家族：進了永不回 `act`），
  **不是**回佇列；真正「溢往下一塊」＝`while` 輪＋`border[gid]` 逐塊試＋`a_rem`（`:537`）遞減。
  ⇒ `_place_pool_parcels` 若「只裝得下一部分」，**殘量必須回報**給 wf_f4 扣 `a_rem`，
  否則 `placed` 與實際落位分岔、a′ 帳漏。**介面須明訂回傳「實際落位面積」。**
- **W-5 零進度守則**：E1 輪有既有「零進度 → 撞 `MAX_ROUNDS`(`wf_f4:64/:581`) raise」路徑；
  D-4「任一不過即整筆溢」是**新增拒絕路徑**且不改 `a_rem` → 放大之。
  ⇒ **本輪零進度 ⇒ 剩餘 `a_rem` 全數 `spill_75`**（非撞上限停機）。

### P2-h　P3 app 鏡像（#20 四處同改鐵律）

同構點（`24d02ba` 實測）：

| 環節 | stepg | app 鏡像 |
|---|---|---|
| ordered_v2 呼叫 | `:382` | `app.py:15469` |
| `_advance_block_with_split` | `:486` | `app.py:15584` |
| `_adv_final` 產生 | `:686`／`:727` | `app.py:15818` |
| `g_rows.extend` ← **插入點** | `:728` | `app.py:15843` |
| `allocated_polys` | `:738`／`:755` | `app.py:15862`／`:15880` |
| `_pool_strips_for_block` | `:767` | `app.py:15892` |
| §N3-0 逐宗主閘 | `:818-832` | `app.py:15959-15966` |
| 守恆-帳幾何級 | `:915-959` | `app.py:15986` 起 |

- ⚠️ **W-9（既有債·非本波引入·已上呈未裁）**：`stepg:712-719` 用補丁八 W 正典 `_mp_base_W0`，
  `app.py:15818` 一帶仍用舊式 `_left_buffer_S*cos_dn`（stepg 註解自稱「已作廢」）。
  **本波勿順手改**（屬 §十二 上呈項）；但改 app 時**勿使其惡化**。
- ⚠️ **W-6 殘留舊邏輯**：`pool_cen`（`wf_f4:439`）／`d_off`（`:445`）／`_trial`（`:467`）之
  **池質心＋0.6m 偏移**錨點機制，於兩階段後與「池邊界切帶」不同源；
  `POS_SLACK_AREA` 之位置相依誤差假設須重驗。依「不留 fallback 舊邏輯、舊函式整個刪」**須明列處置**（刪或改）。

## 四、⛔ 未裁·勿自決（碰到即停機上呈）

`plan v3 §十二` 之上呈項：**W-1 政策含意**（reviewer 實測 3.5m 六塊中央池 **4/6 塊兩側跨占皆 0**，
僅 R1 左 0.312m、R4 右 4.000m ⇒ 裁定F 在本案幾等於「一律無側街負擔」、B5 主規則實質不觸發）；
**W-9** app/stepg `b` 分岔。**B-4 已由裁定K 消滅、W-7 已由 claude.ai 順解（剔除＝佇列末位·已實作）。**

## 五、驗收（⚠️ §11.3：現行 baseline 絕對比對**不可用**）

**先讀 plan v3 §11.3。** 現行 `run_all` 於 `W-F F.0` 即因**六格錨過期**（`G007 G(Σa)=359.43 ≠ 錨 362.08`）紅、
級聯 F.1–F.4 全數「存在性守衛」跳過 ⇒ **V2/V3/V8/V9 量不出來**，且「勿烤 baseline」與「baseline zero-diff 驗收」互斥。

**本波處置（已核可）**：施工期改 **WV_BAKE 側目錄＋探針相對比對**（同一 commit 前後自比），
baseline 絕對比對**留待波末重烤**。此為**量測方法變更、非放寬判準**。

可直接跑：
```bash
WV_PROBE=1 python verify/probes/probe_stage_order.py --setback 3.5 --block R1 --lot "628-37(1)"
```
（~10 分鐘；`exit 66`＝破命中早停；`--no-break` 跑完整輪；`--setback 0.0` 對照。
探針會**暫時注入純 print 再逐位還原**原檔，引擎零常駐改動。）

**主症解除靶（V1）**：3.5m `628-37(1)` 之 `|G−幾何| ≤ 0.015` **且** `S_remain` 足額（非踩 0.1 下限）。
施工前後各跑一次探針對比，序列表中該宗應由 `|Δ|=7.90` 轉為 `≤0.015`，且**遞補宗不再插在原地主宗之間**。

其餘靶見 plan v3 §七 V1–V13（V11 裁定H 零差**已於 `712ce59` 實算驗證**：G013 2,594,110／G024 887,762／G028 3,747,048 逐位相同）。

**V7 fixture 必須構造 synthetic 案例**（兩側跨占 >0 且不等、兩側皆 0、池<最小畸零、池非單片、拆分邊界、左右雙向）——
餵 UC9898 真資料**測不到主規則**（4/6 塊跨占皆 0），會重演 `fixture_end_fallback.py` 舊 tautology。
新 fixture 期望值出處依 `.claude/skills/fixture-provenance`（**禁跑一次回填**）。

## 六、施工紀律

- **錨全家族施工期零動**：`COMP_EXPECT`(`wf_f4:59`)、`F1_REVERIFY`(`:61`)、`SNAP_WAVG`(`:58`)、`GSA_EXPECT`(`wf_f0`)、六格錨——變動一律留**波末重烤**。
- 泛用為本：**禁硬編塊名／側別／常數**；判別走**資料驅動**旗標（`配地階段`／`類`），**禁** `74·` 名稱前綴。禁新增案例錨。
- 一步一 commit、每步 py_compile；**不綠不推、未 push 不報收官**（`git rev-parse origin/wip/s1-endpart` 須含該 commit）。
- 寬幅重構走 `.claude/skills/expand-contract-refactor`；期望值走 `fixture-provenance`。
- 只有真觸及**域邊界**（KL 域裁）才停機上呈；純技術自理。

## 七、交接者自評（誠實記錄）

P2 未動之原因**非**域問題，係**餘裕不足**：P2 是動守恆核心的整包架構件，B-1 已證**半套會靜默破守恆且現有閘全部抓不到**，
而 §11.3 又使 V2/V3/V8/V9 當下量不動 ⇒ 改完也驗不動。依「不綠不推」，選擇不推半套。
已 push 之四項（`712ce59`／`24d02ba` 等）**各自獨立、可單獨 revert，無半完成狀態**。
