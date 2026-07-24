# W-G.4 裁定 M — 施工 plan **v3**（Q1＋M 同波·全做）

> **取代 plan v2**（`docs/specs/W-G.4_裁定M_plan_v2.md`·`706cb17`）。
> canonical＝`docs/specs/W-G.4_KL域裁M_原位次小往大_街角winner更正.md`。
> **BEFORE 錨＝`df9834c`**（Q-M3）。基準 `706cb17`。
> 併入 **plan v2 reviewer 裁決**（`docs/reports/W-G.4_裁定M_plan_v2_reviewer裁決.md`）之
> **BLOCKED 6 項（B-3 經復驗駁回·維持原值）＋ WARNING 9 項 ＋ NOTE 4 項**。
> 依 CLAUDE.md：plan 一寫完**立即送 reviewer**、不停等 KL。

---

## 〇、既裁不重議

| 題 | 裁決 | 落實處 |
|---|---|---|
| **Q-M1** | (b) 先量後裁 → T1 零翻盤 ⇒ **全做** | 全 plan |
| **Q-M2** | **樂觀**口徑 ＋ **落地後一致性硬閘**（winner 實配 G < 街角規定面積 ⇒ loud 停機） | §三 3.1、§五 D-6 |
| **Q-M3** | **合法重定錨程序**：BEFORE 釘 `df9834c`／逐格歸因／**單獨 commit** 重烤／**禁改 `skip_cols`** | §二 P-0c、§八 P-H |
| **Q-M4** | 真 G 走**同一 `_solve_one` 整條含 fallback**；**loud raise 限輸入缺值** | §二 P-0b、§三 3.2 |

> ⚠️ **引表必連裁決段**（`failure-archaeology #27`）：T1 之 M-2(c) 三靶（R2左 8.65／R5左 52.56／
> R3右 103.66）之前提為 **Q-M2 樂觀口徑＋假設第 1 宗**，**不可**與 reviewer 之「實配 G」數列互代。
> 同理 §六 之「M-1 母體＝`{G011}`」係於 **`WV_BAKE` 過期錨**下量得 ⇒ **P-0c 後須重量**。

---

## 〇.5、BEFORE 實測狀態（`b5f1a86`／`706cb17`·功能上等同 `df9834c`）

`python verify/run_all.py` → **42 PASS ／ 22 FAIL**（log＝`verify/out/M_before_runall.log`）。
`git diff --stat df9834c b5f1a86` ＝ 10 檔全為 docs／skill／探針（治理碼零異動）⇒ BEFORE 錨同態。

**BEFORE FAIL 集合（22 項）**：`v3·G值/滑池槽/J表 ×2`(6)／`k* 六塊經驗錨3.5m`(1)／
`W-D.3 碎片幾何·逐邊CAD`(2)／`W-D.4 四梯清單/碎片遞補/跨占分配線 ×2`(6)／
`F.0 釋池對象＝梯3 二群`(1)／**`W-F F.0`**(1)／`W-F F.1~F.4` 級聯(4)／`W-G G.2` 級聯(1)。

### 六格錨之**正確歸因**（⚠️ v2 §〇.5 寫錯·此為更正）

| 項 | 事實 | 證據 |
|---|---|---|
| 錨落點 | `verify/wf_f0.py:55-59` `GSA_EXPECT`＝**每情境 6 格 × 2 情境**（非 v2 所寫「1 格」） | 直讀 |
| 錨字面設於 | **`7ce98e6`**（W-G Y 波收官·全鏈重烤） | `git log -S "362.08" -- verify/wf_f0.py` **唯一命中** |
| 最後全綠 | `verify/out/run_all_Y2.log`（07-16·G007 362.08 綠） | 倉內 log |
| **真兇** | **W脫鉤（07-19）＋ S0d（07-20）改了 G 之 W／S 輸入項 → 359.43 係預期新值** | **KL 2026-07-21 更正**·`docs/reports/W-G.4_run_all紅_working_xlsx資料阻斷_上呈.md:3`；另 `W-G.4_S1_§4_末端塊fallback_收尾.md:36` 同載 |
| **非** 真兇 | ❌ S0b/S0c（`3d946b7`·07-17·自帶重烤且未動錨字面）／❌ 兩階段落位 P2（07-23 開波·紅於 07-21 已現）／❌ **working xlsx 資料汙染**（該上呈已被 KL 標「誤判·勿據行動」·committed xlsx blob `80f75ee` 完好未變） | 同上 |

> 🔒 **Q-M3 之全部價值在「逐格歸因」**；歸因寫錯＝鑑別力歸零。v2 之錯誤歸因即
> `#27`（**搬數字不搬前提**）之變體，故本節連**裁決段**一併錄。

### `WV_BAKE` 旁路（v2 已更正·此處確認）

`wf_f0.py:194-196` 於 `WV_BAKE` 非空時**降級為 warning**（不 raise）⇒ `wf_f2` 可達。
⇒ **P-E 之測項於 P-0c 前即可驗**；P-0c 係「**收官之前置**」而非「P-E 之前置」。
（reviewer 另證：`wf_f2._decide` 為**純函式**（`wf_f2.py:76`·只吃 dict/float、無 I/O、無 ns）
⇒ 合成 fixture 可直呼——M-3(i) 三段測項本就走此路。）

### BEFORE 之 M-4 二 fixture（實跑）

| fixture | 結果 | log |
|---|---|---|
| `verify/fixture_end_reserve.py` | **PASS**·**12 檢核項**（左 6＋右 6·全 `Δ=0.00e+00`） | `verify/out/M_before_end_reserve.log` |
| `verify/fixture_end_fallback.py` | **ALL GREEN（左右雙向）**·每側 **5 項**（0直測／①抵費地末=R_end／②帳池==幾何池／③非疊／④G守恆） | `verify/out/M_before_end_fallback.log` |

### BEFORE 容量拆解（P-G 之「前」）

`WV_CAPDECOMP=1 python verify/probes/probe_capacity_decomp.py` → `verify/out/M_before_capdecomp.log`

| 情境 | 需求群 | 甲現況 | 乙釋forced | 丙釋碎片 | 窮舉狀態 |
|---|---|---|---|---|---|
| **0m** | 6 | **13** | 13 | 14 | **可行**（真窮舉·出指派） |
| **3.5m** | **9** | **7 ⇒ 短 2**（＝「9 戶差 2 戶」） | **12** | 7 | **`space 559872>300000·未窮舉`** |

3.5m forced 三端：`R5左 300.52 s∈(0.269,8.677)`／`R2左 309.05 s∈(0.268,8.716)`／
`R3右 308.93 s∈(88.074,96.803)` ＝ **Σ918.50**（與盤點表 §〇、T1 靶**逐位吻合**）。
⇒ 甲 7<9、乙 12≥9、丙 7 ⇒ **解在 forced 釋回、不在碎片** ＝ M-2(c) 之靶。

---

## 一、總覽：commit 序

| 步 | 名 | 性質 | 綠判準 |
|---|---|---|---|
| **P-0a** | `_compute_v3_finance` 抽出 | 純位移·零行為 | 三張 v3 baseline **byte 零 diff**＋FAIL 集合逐字不變 |
| **P-0b** | `app._solve_G_one` 抽出（整條含 fallback） | 純位移·零行為 | 同上（全 baseline） |
| **P-0c** | **F.0 六格錨＋F.0 baseline 家族重烤** | **重定錨**（既有連動·**非本波**） | `W-F F.0` 轉綠、F.1~F.4 可執行；歸因表逐格 |
| **P-A** | `_corner_first_lot_G` | 新增·未接線 | ns 雙向閘＋A-1~A-4 測；baseline 零 diff |
| **P-B** | `run_corner_pk(..., snapshot=)`×8 ＋ `require_g_map` | 純加性 | 兩顆 golden 綠；baseline 零 diff |
| **P-C** | 達標吃真 G＋`真G(㎡)` 欄＋or-鏈消滅＋**app 鏡射同 commit**＋AST 欄集閘 | **行為改** | **預期打紅 4 格**（見 §四 C-4）·winner 零翻盤 |
| **P-D** | **M-2(c) 自救**＋registry＋全域序＋兩趟定點＋落地硬閘 | **行為改·主體** | 三 forced 端逐端報缺口補足來源 |
| **P-E** | **M-1／M-3 三段**（`F2_GROUPS`＋`ROUTE_OUT` expand-contract） | **行為改** | 三段各≥1 測；導出式同值斷言 |
| **P-F** | **M-4 交互驗證**（實測） | 驗證 | 二 fixture 續綠＋歸因 |
| **P-G** | 容量拆解重跑＋報告 | 驗證 | 「9 戶差 2 戶」＋**需求群成員差** |
| **P-H** | **baseline 重烤**（獨立 commit·逐格歸因） | 重定錨 | 清單見 §八·**禁改 `skip_cols`** |

**🔒 隔離鐵律**：P-0c 必須先於 P-C／P-D／P-E——先把「本波前之既有連動」烤進錨，
本波改動才是 P-H 歸因表所見之**唯一**變因。**禁**把 P-0c 與 P-H 併為一次重烤。
（reviewer 補強：P-0a/P-0b 落地後、P-0c 之前，**再跑一次 `run_all` 並凍存 FAIL 集合為新 BEFORE**，
以免位移波之殘差混入 P-H 歸因。）

**P-0a/P-0b 不需等 P-0c**（其判準與 F.0 紅無關·reviewer P13 實證）。

---

## 二、P-0：純位移抽出（零行為·各自單獨 commit）

### P-0a — `stepg_pipeline._compute_v3_finance`（R1）

⚠️ **v2 之「原封不動位移 `:90-192`」不成立**（reviewer W-1·我以 AST 逃逸分析復驗）。實情：

- `:170-177`（`_tab6_burden` 取值＋raise）**夾在中間** ⇒ 實為**兩段**：`:90-169` ＋ `:178-192`，
  **非連續位移**。`_tab6_burden` **留在 `run_step_g`**（PK 階段該 session 鍵未鋪底，移入會誤 raise）。
- **在 `:90-192` 賦值、於 `:193+` 被讀**之名字（AST 實測·return dict **必須全涵蓋**）：

  | 名 | 於 `:193+` 之讀取行 |
  |---|---|
  | `B_value` | 304, 319 |
  | `C_for_calc` | 304, 319 |
  | **`SB`** | **196, 201** ← v2 漏 |
  | **`_build_blocks`** | **197, 202** ← v2 漏 |
  | `sb_rows_by_label` | 348 |
  | `post_price_by_block` | 572, 643, 798 |
  | `pre_price_by_zone` | 573, 644, 799 |

  （`_tab6_burden`(323) 不移；`fcb`／`fin`／`road_data`／`sb`／`_C_avg_form` 逃逸計數為 0。）

- **副作用須加註（誠實·非零行為之唯一例外）**：兩段切法使
  `globals()["_V3_FINANCE"]` 之寫入**移到 `_tab6_burden` raise 之前**（現行在其後）
  ⇒ **僅錯誤路徑之行為改變**（缺 `f3_total_burden_rate_from_finance` 時，`_V3_FINANCE`
  會已被寫入才 raise）。**正常路徑逐位零變**。此點**明載於報告**、不宣稱「完全零行為」。

**零行為證明**：① `run_all` FAIL 集合逐字不變；② 三張 v3 baseline byte 零 diff；
③ 臨時斷言 `_V3_FINANCE` 逐鍵逐值相等（證畢即刪）。**不改 `run_step_g` 簽章**。

### P-0b — `app._solve_G_one`（Q-M4）

**抽出前提已由 reviewer 逐行對拍證成**：`app.py:15662-15700`（39 行）vs
`verify/stepg_pipeline.py:298-329`（32 行），dedent 後 **可執行語句逐字全等**
（差異僅 app 版多 6 行 docstring ＋ 1 行註解）。

- module 級 `_solve_G_one(*, ..., B, C, tab6_burden, ...)` ＝ 現行 body **逐字**
  （含 `try/except Exception: pass` → `iterate_G_S` → `area_geom`／`cut_coords`）。**不加 raise**。
- 兩處內嵌 `_solve_one` 改**薄殼**（原簽章與呼叫端零改）。
- 入 `_WF_NS_NAMES`（`app.py:8971`）；`stepg` 以 `ns["_solve_G_one"]` 取。
  ✅ reviewer 實證：`run_verification.py:1110-1132` 之反向掃描**明文排除 `selection_pipeline.py`**
  ⇒ P-A 於 selection_pipeline 用 `ns["_corner_first_lot_G"]` 不誤觸閘；新符號入清單安全。

⚠️ **殘留分岔（必載報告·列 backlog·本波不擴大）**：閉包 `_tab6_burden` 兩邊**不同源**——
`stepg:172-177` 缺值 **raise**；`app:14437-14439` 缺值 **靜默退 `B+C`**。
⇒ Q-M4「同一 `_solve_one` 整條」在該 session 鍵未鋪底時仍分岔。**禁宣稱「完全同源」。**

### P-0c — F.0 六格錨＋baseline 家族重烤（**收官前置**）

**範圍（reviewer W-6·目錄實查·v2 未列）**：
1. `verify/wf_f0.py:55-59` `GSA_EXPECT` **12 格字面**（6 格 × 雙情境）；
2. `verify/baselines/wf/f0/` **12 檔 CSV**——`F.0_G值`／`F.0_合併決策`／`F.0_滑池槽診斷`／
   `F.0_逐槽J表`／`F.0_旗標消長`／`F.0_池差` × `{0m, 3.5m}`（全走 `diff_rows`）；
3. f1~f4 baseline 是否連動 ⇒ **重烤後以實跑決定**，逐檔列入歸因表（**禁**先假設）。

**程序**：
- **不**直接 `WV_BAKE=<BASELINES>` 原地覆寫（覆寫後即無「前」）。先 `WV_BAKE=<scratch>` 產新值 →
  **逐格 diff 表** → 人工核 → 才覆寫。
- **資料源潔淨（`fixture-provenance`）**：`git status` 現仍 `M data/地籍資料來源_匿名版.xlsx`
  ⇒ 重烤須在 **committed xlsx** 下跑（`git worktree add` 乾淨樹），並把 **xlsx blob hash
  （`80f75ee`）記入 `PROVENANCE_F0.md`**。
  ⚠️ **理由是「baseline 須可由倉態復現」，不是「working xlsx 造成錨破」**——
  後者係已被 **KL 2026-07-21 標為「誤判·勿據行動」**之論（見 §〇.5）。**勿動 `data/xlsx`。**
- 歸因表每格須標成因＝ W脫鉤／S0d／其他（**逐格**），無法歸因者 ⇒ **停機**。

---

## 三、P-A：`_corner_first_lot_G`（假設第 1 宗真 G·樂觀口徑）

落點：app.py module 級，入 `_WF_NS_NAMES`。**內部呼叫 `_solve_G_one`**（Q-M4·非直呼 `solve_G_binary`）。

### 3.1 參數口徑

| 參數 | 值 | 依據 |
|---|---|---|
| `baseline_pt` | 左＝`corner_pt`；右＝`corner_pt + s_max_right·d̂` | Q-M2 樂觀（兩端 buf=0） |
| `d_hat` | 左＝`+d̂`；右＝`−d̂` | `stepg:576/647` |
| `S_max_limit` | 左＝**`S_block_max`**；右＝**`_oblique_s_max`** | reviewer B-6。✅ **P5 實證**：`stepg:575/646` 之 `S_remain = max(0.1, S_* − left_cum_S − right_cum_S)` ⇒ 左端取 `S_block_max` **確實等價於 `left_cum_S=right_cum_S=0`**、**無遺漏 `_right_buffer_S`** |
| `is_corner`／`W_prev` | `True`／`0.0` | 第 1 宗 |
| **`a`** | **`if '分攤登記面積_m2' in tp: round(分攤登記 + 面積_m2, 2) else: round(面積_m2, 2)`** | 🔴 **B-4 更正**：v2 之 `tp.get(A, tp.get(B,0)) + tp.get(B,0)` **鍵缺席時重複計 `面積_m2`**。實配 7 處一律 `if in` 形（`stepg:260/556/627`；`app:7462/15624/16044/16124`）。**同時修 `verify/probes/probe_corner_trueG.py:120-122`**（已寫入錯形·現潛伏） |
| **`a` 之來源** | **「即將餵給 `run_step_g` 的那份 parcels」**（非固定 `temp_parcels`） | 🔴 **W-4 更正**：`sel:255-258` `build_parcels` 與 `temp_parcels` 為**同一批 dict 物件**（無 copy）；P-D deepcopy `parcels₁` 後，讀 `temp_parcels` 會**看不到 a′ 注入** ⇒ D-6 硬閘與自救量測的不是同一批 a |
| `avg_depth`／`min_width` | 顯式自 snapshot·缺值 loud | reviewer W-5（PK 時段 `f3_alloc_depth_by_label` 未鋪底·`stepg:196-202` 才寫；fallback 差 R6 **6.05㎡**／R3 4.89㎡） |
| `B`／`C`／`price` | `_compute_v3_finance`（P-0a） | `#20` |

### 3.2 loud raise 之邊界（Q-M4）

- **raise**：`a`／`A`／`B`／`C`／`block_poly`／`d_hat`／`corner_pt`／`avg_depth`／`min_width`／
  snapshot 該塊節點缺值或 ≤0；被問到之側 `side_mid` 為 None（＝上游 bug）。
- **不 raise**：`_solve_G_one` 之幾何二分法失敗 → 照走 `iterate_G_S`。

### 3.3 P-A 測項

| 測 | 內容 | 期望 |
|---|---|---|
| A-1 | `_corner_first_lot_G` vs `_solve_G_one` 直呼（同參數） | 逐位全等（證同一路徑） |
| A-2 | 左右 `S_max_limit` 不同源 | 分別 == `S_block_max`／`_oblique_s_max` |
| A-3 | 缺值 loud | `a=None`／`depth=0`／`min_width=0` 各觸 `RuntimeError` |
| A-4 | fallback 覆蓋 | 退化 `block_poly` → **不 raise**、`solver_label=='代數迭代(fallback)'` |
| **A-5** | **`a` 之 `if in` 形** | 合成 `tp` **無** `分攤登記面積_m2` 鍵 ⇒ `a == 面積_m2`（**非 2×**）·B-4 回歸守衛 |

---

## 四、P-B／P-C：接線

### P-B（純加性·baseline 零 diff）

1. `run_corner_pk` 增 **keyword-only `snapshot`（無預設）**。**8 呼叫端**（reviewer P1 逐行號實證）：
   `run_verification:423`／`wd3_fragment_geom:93`／`wd4_tier_list:187`／`wg_g1_smoke:56`／
   `wg_g2_smoke:35`／`wg_g3:81`／`tools/y_dump_diff:59`／`probes/probe_corner_trueG:93`。
   （`wf_f0.py:40` **只 import 不呼叫**＝dead import·順手清·NOTE-1。）
   靜態閘：AST `Call` 掃描「`run_corner_pk(` 呼叫端 == 8 且全帶 `snapshot=`」。
2. `_pk_one_side_v12` 增 **`require_g_map: bool = False`**（B-1 修法·保 golden）＋**消滅 or-鏈 falsy 陷阱**：
   `require_g_map` → `g_values_map[pid]` 缺即 raise；否則 `in`-鏈 `g_values_map`→`G_value`→`G_estimated`，
   **全缺即 raise**（禁靜默視為 0）。
   ✅ **零行為經 reviewer 實證**（P2/P3）：`app:8687-8710` `G_est = a×(1−burden)+0.5`、
   `burden = max(0,min(0.95,·))` ⇒ **恆 ≥0.5 >0**、永不落 falsy；兩顆 golden 走
   `G_value=1e9` 分支且以 **3 個位置引數**呼叫 ⇒ 第 4 個具預設參數安全。
   **禁改兩顆 golden fixture**（`tests/test_corner_priority_golden.py:63,69,79`／`app_harvest.py:174`）。

### P-C（行為改）

1. `run_corner_pk` 對每候選算 `_G_true = ns["_corner_first_lot_G"](...)`；`g_values_map` 餵 `_G_true`；
   v12 以 `require_g_map=True` 呼叫。
2. `_estimate_G_for_qualification` **不刪**（B-2·3 真消費端：`app:14870` live UI／`sel:290`／`app_harvest:150`）。
   診斷表**新增 `真G(㎡)` 欄**。
3. **B-3 鏡射範圍（W-3 擴充·v2 under-scoped）**：`app.py:14860-14939` **＋ `:14958`**
   ↔ `selection_pipeline.py:316-370` **＋ `:401`** —— 逐項同改、**同 commit**。
   （`:14958`／`:401` 即 `'G估(㎡)': round(float(_dc.get('G_for_threshold',0) or 0), 2)` 之寫入點，
   亦即 `真G(㎡)` 新欄之落點。）
   **AST 欄集結構閘**：`app:14886` 之 `_candidates.append({...})` 鍵集 == `sel:334` 之鍵集
   ✅ reviewer 實作跑過：**各 15 鍵·差集空·EQUAL True**（`ast.parse` 不執行碼 ⇒ app 段在 `main()` 內不影響）。

### C-4｜**P-C 之誠實紅表**（🔴 v2 之「續綠」宣稱為假·B-2）

`G估(㎡)` **直接來自 `g_values_map`**（`app:8482 G_for_threshold` → `:14958`／`sel:401`），
**非**來自保留之 `G_estimated` 鍵 ⇒ 改餵真 G 該欄**必變**。三道閘 BEFORE **全綠**
（`M_before_runall.log:129-131, 175-177`），P-C 後：

| 閘 | 檔:行 | P-C 後 | 處置 |
|---|---|---|---|
| `v3·診斷{0m,3.5m}`（全欄逐格·**無豁免**） | `run_verification.py:433-435` | 🔴 **紅 2 格** | P-H 重烤 |
| `率接線 G估 欄變動 N 格（期 0）{0m,3.5m}` | `:451-456` | 🔴 **紅 2 格** | P-H 重烤 |
| `率接線無串聯{0m,3.5m}`（`skip_cols` 含 `G估(㎡)`） | `:441-444` | ✅ **續綠**（T1 證達標/選中零翻盤） | — |

⇒ **P-H 重烤清單必須明列**（v2 漏）：`verify/baselines/W-D.1.2 診斷_退縮{0m,3.5m}.csv`
＋ `verify/baselines/v3/W-D.1.2 診斷_退縮{0m,3.5m}.csv`。
**禁改 `skip_cols`／`_exp_gd`／退役閘**（Q-M3）⇒ 唯一合法出口即重烤。

> 附帶更正：v2 稱「Q-M3 之紅只剩欄集」亦誤。`diff_rows` 只走 baseline 既有欄
> ⇒ **新增 `真G(㎡)` 欄本身不打紅**；紅的是 `G估` 之**值**。
> 且 `_bake_csv` 之欄序為 `[base 既有] + [got 新增]` ⇒ 新欄能進重烤後 baseline（reviewer P14）。

---

## 五、P-D：M-2(c) 合併自救（主體）

### D-1 兩趟定點（循環相依之解）

```
趟0：run_corner_pk(rescue_ctx=None) → run_step_g → trunk A₀ → U₀={宗: G(A₀) < MinA[blk]}
趟1：run_corner_pk(rescue_ctx={U, gid_map, mina, zone_price, registry})
     → winners₁／forced₁／registry → parcels₁ → run_step_g → trunk A₁
定點：U₁ 導出之決策 ≠ U₀ 導出者 → 再迭（上限 3 趟）；不收斂 ⇒ loud raise
```

- 決策邏輯置 **`verify/m_rescue.py`**，使 8 個 `run_corner_pk` 呼叫端**除加 `snapshot=` 外零改**
  （未傳 `rescue_ctx` ⇒ 趟0 語意＝Q1-only）。
- app 端接 `_m_rescue_plan`（經 §7 引擎 ctx 回灌），**不在 app 重寫決策**（CLAUDE.md §7 禁 fork）。
- **W-9 成本前置**：P-D 動工**前**先量單次 `run_step_g` 壁鐘。
  最壞成本＝P-D(+1) ＋ E-3(+6) × 雙情境 ＝ **+14 次**。
  若 `run_all` 因此**翻倍以上** ⇒ 先議（縮 E-3 迭代上限或改局部解）。

### D-2／D-4 之**需求量定義統一**（🔴 W-8：v2 內部不一致）

**寫死為**：需求量 ＝ **該端「真 G 最大之候選」之缺口**（＝`街角規定面積 − max(真G)`）。
理由：M-2(c) 只需**一個**候選過閘即可免 forced（canonical「合格者 ≥2 → 依指數定 winner」
係**過閘之後**的事）。⇒ D-2 之救援池**仍對每個未過閘候選建**（供 fallback），
但 **D-4 之排序鍵與實際配給量一律以「最強候選之缺口」為準**，二者不再脫節。

### D-3 自救母體（M-2 原文）與 Q2 硬約束

```
救援池(end) = { s ∈ parcels_目前 :
                gid(s)==gid(最強候選) ∧ blk(s)!=blk(end) ∧ 可建築(blk(s))
                ∧ s ∈ U(動態·見 D-5) ∧ registry.remaining(s) > 0 }
```

**Q2（canonical §2.2）**：`E-1.7 真交集 > 1.0㎡` **絕對地板照舊**；自救**僅解 G 門檻**。
E-1.7 在 `app.py:8402-8403`、**先於** `_pk_one_side_v12`（reviewer P10 實證）
⇒ 依 **W-6**，Q2 測項落點**上移**至 `select_corner_lots_both_sides_v12`（落 `_pk_one_side_v12` ＝套套邏輯）。

### D-4 注入量：只取所需（Q3）＋重跑迭代（W-2）＋**單位統一**（🔴 B-7）

v2 之二分搜尋**單位混用**（`supply` 為源 zone、`a` 為目標 zone）。**更正**：

```
自變數統一為 a′（**目標 zone 口徑**）
上界 supply′ = Σ_i wf_f2.a_prime_mode1(a_源_i, z_src_i, z_tgt)      # 逐源宗換算後加總
lo, hi = 0.0, supply′
前置斷言：G(a) < threshold ≤ G(a + supply′)                          # 區間有解·破即 loud
二分 40 次／tol 0.01㎡，每次評估**重呼 `_corner_first_lot_G`**（同一 solver·單一真相源）
回填：由 a′ 反算各源宗之 a_源 消費量 = a′_i × p(z_tgt)/p(z_src)      # registry 記帳用源口徑
```

- **禁** `缺口 ÷ 固定比率`（G 對 a 次線性·`G/a ∈ 0.5594–0.5828`）。
- 源宗取用序＝`(a_源 ↓, 暫編地號 ↑)`（大者先·減少被拆宗數）。

### D-5 **registry**（🔴 B-6：v2 只凍源、幻影未消）

```python
class ConsumedRegistry:
    def claim(self, pid, amount, *, stage, target)   # 超額 ⇒ loud raise
    def remaining(self, pid)                          # 原 a − 已消費
    def freeze_target(self, pid, *, stage)            # 🆕 受贈宗登記
    def is_target(self, pid)                          # 🆕
    def frozen(self)                                  # 源∪target·供 F.0/F.2/F.4 唯讀
```

**兩項修補（缺一即幻影復活）**：
1. **target 亦凍結**——受贈宗（收了 a′ 者）**不得再當源**。
2. **`U` 改動態**——每次授予後即時自 `U` 移除「已被消費至 0 之源」**與**「已成 target 者」，
   不再固定用趟0 之 `U₀`。

> **反例驗證（必列測項）**：`G011` 之 `628-42(1)@R2左` ↔ `628-42(2)@R3右` 對稱互救
> （reviewer 真資料·幻影 **+161.80㎡**）；`G030` 同構（**+98.00㎡**）。
> **測項**：跑完 P-D 後斷言此二群之 `Σ registry 消費 == Σ target 增量 ÷ 換算比`，
> 且**無任一宗同時為源與 target**。

**全域決定性序**（街角 vs 街角·技術補注·KL 可否決）：
`(缺口 ↑, blk 字典序 ↑, side ∈ {'左'<'右'})`——缺口小者先取（＝forced 端數最小化，
上位精神「強制抵費地為最後手段」之操作化）。單點可換之 `_RESCUE_ORDER_KEY`。

**materialisation**＝趟1 之 `parcels₁` 建構時（**`run_step_g` 之前**）：
全額消費 → 移除；部分消費 → 扣減落 **`面積_m2`** 累加器欄（四欄鐵律：`分攤登記面積_m2` 唯讀），
扣後 ≤0 視同全額；target 宗 `面積_m2 += Σa′`。
**下游唯讀**：`wf_f0._decide`／`wf_f2._decide`／`wf_f4` 母體先 `∖ registry.frozen()`；
再 `claim` 超額即 loud。

**守恆閘（`run_all` 新增）**：`Σ消費(源口徑) == Σ target 面積_m2 增量 ÷ 換算比`（逐 gid·tol 0.01㎡）
＋ `無宗同時為源與 target` ＋ 既有 `每塊 ΣG+池 == 街廓 DXF 面積` 續綠。

### D-6 落地一致性硬閘（Q-M2 對價）

trunk A₁ 產出後，對**每個**街角 winner：
`實配 G(A₁) < 該端街角規定面積` ⇒ **`raise`（loud 停機）**，非 warning、非自動降級 forced。
> 預期綠：T1 之最薄 `628(5)@R1右` 樂觀 **+13.51**／實配 **+0.84**，**同號**。紅 ⇒ 停機上呈 Q-M2 重裁。

---

## 六、P-E：M-1 ＋ M-3 三段

### E-1 **`F2_GROUPS` 之真導出式**（🔴 B-1：v2 述詞必破）

v2 述詞（`qual 非空 ∧ 跨≥2塊` == `F2_GROUPS`）**在真資料上必破**——我直讀
`verify/baselines/wf/f0/F.0_合併決策_退縮{0m,3.5m}.csv`（雙情境逐字相同）：

```
G006|R3|級0'      |✅|達標·留置原位        G009|R4|全達標  |—|全達標·留置原位
G007|R3|全達標    |—|全達標·留置原位      G009|R6|級0'    |🔴|轉F.2(...)
G007|R5|級0       |✅|達標·留置原位        G010|R2|級0     |✅|達標·留置原位
G017|R5|全達標    |—|全達標·留置原位      G014|R3|級0'    |🔴|轉F.4(...)
G017|R6|級0       |✅|達標·留置原位
```
⇒ G006／G007／G017 跨≥2 塊且 qual 非空、**卻不在 `F2_GROUPS`**——因 **F.0 已解決**。

**採 reviewer 之導出式**（其實跑證等·雙情境 `True`）：
```
F2_set = {gid : F.0「去向」以「轉F.2」開頭}
       ∪ {gid : F.0 未觸及 ∧ 跨≥2塊 ∧ qual 非空 ∧ 存在非 qual 塊}
     = {G009} ∪ {G001, G021, G026, G027} = F2_GROUPS   ✅
```

**expand-contract 三段**：

| 段 | 作法 | 綠判準 |
|---|---|---|
| **expand** | 新增 `_f2_route(byg, mina, f0_decisions)` 現算，**保留** `F2_GROUPS` 並斷言相等 | 斷言綠 |
| **migrate** | `wf_f2:143` 迴圈改吃現算集；`:146` 之 raise 改**分流**（qual 空 → M-1） | FAIL 集合不新增名目 |
| **contract** | 證等後刪 `F2_GROUPS`（`wf_f2.py:40`）**＋ `ROUTE_OUT`（`wf_f0.py:62-63`）**（grep 證零殘留） | grep 零命中 |

⚠️ **W-5：`ROUTE_OUT` 亦為決策常數**（`wf_f0:216` 決 `dest`、`:225` `not ok and gid not in ROUTE_OUT → 停機#4`
＝**驅動控制流**）。M-1/M-2 一旦使新 gid 在 F.0 轉不達標即炸 ⇒ **與 `F2_GROUPS` 同波處理**。
且 E-1 之導出式**正吃 `去向`** ⇒ 二者耦合、須同 commit。

### E-2 M-1 演算法（母體·目標函數）

**M-1 母體＝`{G011}`**（reviewer 實測·雙情境·跨 R2/R3）——**正是** plan v1 裁決 B-5 之
`628-42(1)@R2左 ↔ 628-42(2)@R3右` 對稱互救群 ⇒ **M-1 與 B-5 幻影同一標的、非兩件事**。
⚠️ 該量測於 `WV_BAKE`（過期錨）下取得 ⇒ **P-0c 後須重量**（`#27`）。

```
cur[b]=Σ G(trunk B) of gid 在塊 b；need[b]=max(0, MinA[b]−cur[b])
供給者＝cur 最小之塊（「最小者優先」）；受益者依 need ↑（貪婪最大化處數）
tie（同處數多解）→ 優先救較大者（Q3-tb 補注）
部分拆分不可行 → 整筆連同乙′併入最大之丙（canonical 退路）
  「不可行」＝ 供給 < min(need[b])，或拆分之處數增益 ≤ 0
```

### E-3 注入量之重跑迭代（W-2）＋成本

M-1 受益宗**非**街角第 1 宗 ⇒ G 由整條推進序列決定 ⇒ **批次外迭代**（單趟算全部群）：
初值 `need/(G/a)` → `run_step_g` 量 `G_real` → 割線法修正 → 收斂判 `MinA ≤ G_real ≤ MinA+0.5`；
**6 趟不收斂 ⇒ loud raise**（禁取末趟）。既有 `wf_f2:238-241`「目標宗灌後 G ≥ MinA」為最終看守。

### E-4 M-3(i) 三段測項（canonical **plan 必須含**）

| 段 | 測項 | 落點 | 判準 |
|---|---|---|---|
| ① 補足量 | 注入 ≤ 補足街角規定面積之最小量＋0.01 | `verify/fixture_m_rescue.py::test_topup_minimal` | 源 a 遠大於缺口 ⇒ 只取缺口 |
| ② 餘額他併 | 餘額**先**依 M-1 往同歸戶其他較大地 | `::test_remainder_to_m1` | 餘額恰救一塊 ⇒ 該塊達 MinA、街角不多吃 |
| ③ 餘額回流街角 | 仍任一塊未達 MinA ⇒ 餘額**亦併入街角地** | `::test_remainder_back_to_corner` | 餘額救不了任何塊 ⇒ 全回街角、源宗全額消費 |
| M-3(ii) | 遠地同時可救街角與 M-1 → **街角優先** | `::test_corner_precedence` | 旗標 `_M3II_CORNER_FIRST`·**單點可關** |
| **B-6 反例** | 對稱互救**不得**產生幻影 | `::test_no_mutual_phantom` | 無宗同時為源與 target；Σ消費==Σ增量÷比 |

**fixture 出處紀律**（`fixture-provenance`）：期望值**禁**由新碼跑一次回填；
合成 fixture 之期望以**手算**列於檔頭（面積／單價皆合成常數）。
✅ 可行性已證：`wf_f2._decide`（`wf_f2.py:76`）為**純函式**、合成 dict 可直呼。

---

## 七、P-F：M-4 末端塊交互驗證（實測）

| # | 項 | BEFORE | AFTER 判準 |
|---|---|---|---|
| **F-1** | 3.5m 末端保留觸發集 | **唯 R6 左端**·未臨正街 **85.706㎡**·末端帶 `s∈[-0.0000, 3.5114]`（倉內 `docs/reports/W-G.4_§4_P2_兩階段落位_f到g.md:102`） | 不得無故消失／位移；變動須逐項歸因並載明 |
| **F-2** | `_end_gate` 之 `_cond1` | `_cond1 = not bool(fo.get(_has_side_key))`＝**`verify/wf_f4.py:1325`**；`_end_gate`＝**`:1338`**（**本次實 grep 覆核·維持 plan v2 值**；reviewer 主張之 `1467/1480` 該檔**無此二符號**·已駁） | M-2 改 `forced_offset`／`corner_min_area`、**非** `has_side` ⇒ `_cond1` 逐塊逐側全等·斷言之 |
| **F-3** | `fixture_end_reserve.py` | **12 檢核項**（左 6＋右 6·全 Δ=0）·PASS | 必續綠 |
| **F-4** | `fixture_end_fallback.py` | **左右各 5 項**（0直測／①抵費地末=R_end／②帳池==幾何池／③非疊／④G守恆）·ALL GREEN | 必續綠 |
| **F-5** | E3 `_reshape_block` fallback | 全案 **latent** | 仍 latent；觸發須誠實報（塊/側/量） |
| **F-6** | **交互**：被消費源宗若為某塊**末宗** | BEFORE 逐塊列末宗清單 | 末宗改變 ⇒ 重列 `_end_band` 窗與 `cond2` 半平面量、逐項歸因（`#25`：**左右兩側各驗**） |

---

## 八、P-G／P-H

### P-G 首要驗收讀數

重跑 `probe_capacity_decomp` 家族 → 3.5m「合併後仍需調配群數 vs 可容上界」、「9 戶差 2 戶」是否消失；
附帶：三端 forced 是否轉地主宗（918.50㎡ 釋回），**逐端報缺口是否補足／由哪些源宗補**
（T1 靶：R2左 8.65／R5左 52.56／R3右 103.66）。

⚠️ **W-7 誠實註（BEFORE 已坐實）**：3.5m 之 log **自述** `窮舉=space 559872>300000·未窮舉`
（0m 則為真窮舉並出指派）⇒ **二情境證據強度不同級、禁並列引用**；
且 M-1/M-2 會改變「需求群」集合本身 ⇒ **前後不可當獨立對比**。
報告須同列**需求群成員差**（BEFORE 3.5m ＝
`{G003,G004,G014,G015,G016,G018,G020,G025,G033}`）。

`W-F F.4` 殘紅（3.5m E2 上界 7 < 需求 9）若遷移 ⇒ **誠實定位**（既有 or 新引入），禁以「本波前即紅」帶過。

### P-H 合法重定錨（獨立 commit·Q-M3）

1. BEFORE 釘 `df9834c`；**禁改 `skip_cols`（`run_verification.py:441-444`）／`_exp_gd`／禁退役閘**。
2. **重烤清單（v2 漏兩組·B-2 補）**：
   - `verify/baselines/W-D.1.2 診斷_退縮{0m,3.5m}.csv` ＋ `verify/baselines/v3/W-D.1.2 診斷_退縮{0m,3.5m}.csv` 🆕
   - `第 1 宗街角地指配結果_退縮{0m,3.5m}.csv`／`W-D.1.3-d 驗收_退縮3.5m.csv`
   - Step G 三表 × 雙情境（v3）／W-D.3／W-D.4 家族（依實跑決定·逐檔列歸因）
   - `F1_REVERIFY`（`wf_f4:61`）／UC9898 R1左 3.5m winner
3. **逐格歸因表**：每格歸因於 {Q1 口徑／M-2 winner 更正／M-1 搬移／連動}；**無法歸因 ⇒ 停機、不得重烤**。
4. commit message 標 `rebake(裁定M): 域裁後果之合法重定錨`；報告**獨立節**載前後值。
5. ⚠️ **golden 圖 8（0.6685／0.3315）為手冊語意錨**——變動＝**實作 bug**、非重定錨。
6. V2/V3/V8/V9 維持「未驗·待波末重烤」。
7. `docs/specs/W-G.4_CC交辦_v3.md:105`「3.5m forced 擴為 5」**已過期**（現況 3 端）——引用前標作廢。

---

## 九、泛用四約束逐項自查

| 約束 | 新碼 | 自查 |
|---|---|---|
| 禁硬編塊名 | `_corner_first_lot_G`／`m_rescue`／M-1 全 by `blk` 變數 | ✅；**淨改善**：主動刪 `F2_GROUPS`（`wf_f2:40`）**＋ `ROUTE_OUT`（`wf_f0:62-63`）** 兩顆決策常數 |
| 禁硬編側別 | 左右差異僅 `S_max_limit` 與 `d_hat` 正負·**參數化** | ✅ 由 `side` 驅動；A-2 守衛 |
| 禁硬編常數 | `MinA`／街角規定面積／深度／最小寬**現算或自 snapshot**；容差（`tol_over=0.5`／二分 tol 0.01）**明列報告** | ✅ |
| 換案仍成立 | 判別走資料驅動旗標（`has_side`／`forced_offset`／可建築分類／`gid`／F.0 `去向`） | ✅；`_RESCUE_ORDER_KEY` 單點可換 |

**常數二分法**：
- **決策常數（驅動控制流）⇒ 刪**：`wf_f2.F2_GROUPS`(:40)、**`wf_f0.ROUTE_OUT`(:62-63)** 🆕
- **對拍錨常數（只進斷言）⇒ 本波不動**：`wf_f4.F1_REVERIFY`(:61)／`E0_EXPECT`／`E2_NAMED`／
  `COMP_EXPECT`／`wf_f2.F1_TARGET`(:42)／`wf_f0.GSA_EXPECT`（P-0c 依重定錨程序更新）

---

## 十、⛔ 停機條件

| # | 觸發 | 動作 |
|---|---|---|
| S-1 | **D-6 落地一致性閘紅** | 停機上呈 Q-M2 重裁（逐端 樂觀G／實配G／門檻） |
| S-2 | M-3(ii) 被實測打破 | 停機上呈（canonical §五.5） |
| S-3 | M-2 與既有街角雙條件裁定衝突（E-1.7 須放寬方可行） | 停機上呈（Q2 前哨） |
| S-4 | **E-1 導出式同值斷言破**（現算 ≠ `F2_GROUPS`） | 印差集·loud FAIL·🚩上呈 |
| S-5 | 兩趟定點 3 趟／M-1 注入 6 趟不收斂 | loud raise（禁取末趟） |
| S-6 | P-0c 或 P-H 有**無法歸因**之 baseline 差異格 | 停機·**不得重烤** |
| S-7 | 圖 8 golden 變動 | ＝實作 bug·停機修碼 |
| **S-8** | **`run_all` 壁鐘因 P-D/E-3 翻倍以上**（W-9） | 先議（縮迭代上限或改局部解） |

---

## 十一、🚩 上呈 KL／claude.ai（CC 不拍板·**不阻施工**）

1. **`F2_GROUPS` 為何排除 G006／G007**——二群於 R2 尚有非達標宗，係**刻意留 F.4** 抑或**既有漏網**？
   ＝**規則本意**問題（reviewer 與 CC 同模型同盲區，不宜自裁）。**M-1 母體是否應含此二群，取決於此答。**
2. **`W-F F.4` 3.5m E2「上界 7 < 需求 9」結構性不可行**是否本波處理（現標「既有·誠實定位」）。
3. **P-0b 之殘留分岔**：`_tab6_burden` 於 app 缺值時**靜默退 `B+C`**（`app:14437-14439`）
   vs stepg **raise**——違 no-silent-fallback、**非本波引入**，列 backlog 抑或本波順修？

---

## 十二、次步

1. 本 plan **立即送 reviewer**（第二輪）——不停等 KL。
2. 綠後依 §一 commit 序施工；每步 `py_compile` ＋ grep ＋ `run_all`，FAIL 集合不得新增名目。
3. 報告本體 `docs/reports/W-G.4_裁定M_施工報告.md`；聊天＝ping。
4. **未 push 不報收官**（`git rev-parse origin/wip/s1-endpart` 須含該 commit）。
