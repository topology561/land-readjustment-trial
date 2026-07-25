# W-G.4 裁定 M — 施工 plan **v4**（Q-M5「准」＋ M-5 上位語意·全速施工）

> **取代 plan v3**（`706cb17`/`620eb50`）。canonical＝
> `docs/specs/W-G.4_KL域裁M_原位次小往大_街角winner更正.md`（**已含 §七 裁定 M-5**）。
> **BEFORE 錨＝`df9834c`**。基準 `2a7ea7d`。
> 併入：**plan v3 二審**（`docs/reports/W-G.4_裁定M_plan_v2_reviewer裁決.md` 之後之二審·
> BLOCKED×6/WARNING×9/NOTE×7）＋ **停機上呈**（`W-G.4_裁定M_停機上呈_救援池實測.md`）
> ＋ **KL 裁定 M-5**（Q-M5 准·上位語意）。
> 依 CLAUDE.md：plan 一寫完**立即送 reviewer**、不停等 KL；**僅真域邊界停機**。

---

## 〇、既裁不重議

| 題 | 裁決 | 落實 |
|---|---|---|
| Q-M1 | 全做（Q1＋M 同波·T1 零翻盤） | 全 plan |
| Q-M2 | 樂觀口徑 ＋ 落地一致性硬閘 | §三 3.1、§五 D-6 |
| Q-M3 | 合法重定錨（BEFORE `df9834c`／逐格歸因／**單獨 commit**／**禁改 `skip_cols`**） | §二 P-0c、§八 P-H、§七 |
| Q-M4 | 同一 `_solve_one` 整條含 fallback；loud raise 限輸入缺值 | §二 P-0b、§三 3.2 |
| **Q-M5** | **准**——街角自救**得**搶 F.0 級0 之被併宗（前態係中間態·非推翻裁定） | §五 P-D（**M-5 重寫**） |
| **Q-M6** | **canonical per-candidate ＋ 假設性帳面併入**（winner 定案才實體化） | §五 D-2/D-3 |

### 〇.1 🔴 概念更正（M-5(1)·**全 plan／報告／UI 措辭鐵律**）

**forced 街角解鎖 ≠ 抵費地減少。** 該面積**回歸中央調配池**（`抵費地總量`（全區）**不變**、
位置由**街角**移回**中間**；既鎖「池置中」則 **`reachable` 可及容量上升**）。

⇒ **禁再用「釋回 918.50㎡」「減少抵費地」語**（plan v1~v3／T1 §三／盤點表 §〇 之該措辭**全作廢**）。
改述：「forced 街角解鎖 → 面積回歸中央調配池 → 可及容量上升（抵費地總量不變）」。

> 容量拆解之 `forced鎖Σ`／`unreach自檢` 即「街角位」不可達量；街角由地主宗奪得後，
> 該量位置移入中央池（`reachable ↑`），全區抵費地總量不動。

### 〇.2 引表必連裁決段（`failure-archaeology #27`）

M-5 之靶（R3右 可解鎖）之前提＝**Q-M5 准 ＋ M-2「其他可建築街廓」要件不變**；
T1 §三「R2左 最易救」**已證偽作廢**（缺口 ≠ 可救性·池 ∅）。**「9 戶差 2 戶」之解繫於 M-5 重排序，非 Q1。**

---

## 〇.5、BEFORE 實測（`2a7ea7d`·治理碼同 `df9834c`）

`run_all` **42 PASS／22 FAIL**（`verify/out/M_before_runall.log`）。關鍵：`W-F F.0` 六格錨破
（`G007 359.43≠362.08`·0m；`369.41≠369.05`·3.5m）→ 級聯 F.1~F.4＋G.2。
`WV_BAKE` 非空 ⇒ `wf_f0.py:194-196` 降級 warning、`wf_f2` 可達。`run_step_g` 壁鐘 **0.21s**。

**容量拆解**（`M_before_capdecomp.log`·3.5m 需求群 **9**）：甲現況上界 **7**（短 2）；
乙釋三端 12；丙釋碎片 7。三端 forced：`R5左 300.52`／`R2左 309.05`／`R3右 308.93`＝Σ918.50
（此三數為**街角規定面積**·不再以「釋回抵費地」措辭引用·見 〇.1）。M-4 二 fixture 綠。

**M-5 之救援池實測**（canonical §七 T-2·CC 親驗）：三 forced 端**只有 R3右**之救援池非空
（`R2左` 之 628-43(1) 同在 R2·`R5左` 之 628-7(1) 已達標 ⇒ 二端池 ∅·**維持 forced**）。

---

## 一、commit 序（每步獨立可驗）

| 步 | 名 | 性質 | 綠判準 |
|---|---|---|---|
| **P-0a** | `_compute_v3_finance` 抽出 | 純位移·零行為 | v3 baseline byte 零 diff＋FAIL 集逐字不變 |
| **P-0b** | `app._solve_G_one` 抽出（整條含 fallback） | 純位移·零行為 | 同上 |
| **P-0c** | F.0 六格錨＋f0 baseline 家族重烤（**既往連動**·非本波） | 重定錨 | `W-F F.0` 轉綠；歸因表**僅** W脫鉤＋S0d |
| **P-A** | `_corner_first_lot_G`（樂觀真 G） | 新增·未接線 | A-1~A-5 測；baseline 零 diff |
| **P-B** | `run_corner_pk(...,snapshot=)`×8＋`select_..v12`/`_pk_one_side_v12` 穿 `require_g_map` | 純加性 | 兩 golden 綠；baseline 零 diff |
| **P-C** | 達標吃真 G＋`真G(㎡)` 欄＋or-鏈消滅＋app 鏡射同 commit＋AST 欄集閘 | 行為改 | **預期紅 4 格**（C-4）·winner 零翻盤 |
| **P-D** | **M-5 同歸戶合併規劃（帶優先序·per-candidate·假設帳面）** | 行為改·主體 | 驗收預測閘 a/b/c（§七） |
| **P-E** | **F.0 整合（級0 重排）＋`F2_GROUPS` expand（不刪 `ROUTE_OUT`）** | 行為改 | 導出式同值斷言（趟0 快照） |
| **P-F** | M-4 交互驗證（實測·左右雙側） | 驗證 | 二 fixture 續綠＋歸因 |
| **P-G** | 容量拆解重跑＋報告（措辭依 〇.1） | 驗證 | 預測閘 d（§七） |
| **P-H** | baseline 重烤（獨立 commit·**M-5 重排序**成因·與 P-0c 分列） | 重定錨 | 清單見 §八·禁改 `skip_cols` |

**🔒 隔離鐵律**：P-0c（既往連動）先於 P-C/P-D/P-E；**P-H（M-5 重排序）與 P-0c 分兩次重烤、歸因分列**
（canonical §七.4·禁混）。P-0a/P-0b 不需等 P-0c。

---

## 二、P-0：純位移＋既往重烤

### P-0a — `stepg_pipeline._compute_v3_finance`（reviewer W-1 更正）

⚠️ **非連續位移**：`:170-177`（`_tab6_burden` 取值＋raise）夾在中間 ⇒ 切 `:90-169`＋`:178-192`，
`_tab6_burden` **留在 `run_step_g`**（PK 階段該 session 鍵未鋪底）。
**return dict 必涵蓋**（AST 逃逸分析·**含 v3 漏之 `SB`／`_build_blocks`**）：
`B_value`／`C_for_calc`／`SB`(196,201)／`_build_blocks`(197,202)／`sb_rows_by_label`(348)／
`post_price_by_block`／`pre_price_by_zone`。
**誠實聲明**（非零行為之唯一例外）：`globals()["_V3_FINANCE"]` 寫入前移至 `_tab6_burden` raise 之前
⇒ **僅錯誤路徑行為改**（正常路徑逐位零變·明載報告）。
**零行為證明**：FAIL 集逐字不變＋三 v3 baseline byte 零 diff＋`_V3_FINANCE` 逐鍵斷言（證畢即刪）。

### P-0b — `app._solve_G_one`（Q-M4·二審證可執行語句逐字全等）

module 級 `_solve_G_one(*, ..., B, C, tab6_burden, ...)` ＝ 現行 body 逐字（含 fallback）；
兩處內嵌 `_solve_one` 改薄殼（呼叫端零改）；入 `_WF_NS_NAMES`（`app.py:8971`）。
⚠️ **殘留分岔（載報告·backlog·本波不擴大）**：`_tab6_burden` 缺值 app（`:14437-14439`）**靜默退 `B+C`**、
stepg（`:172-177`）**raise**——**禁宣稱「完全同源」**。

### P-0c — F.0 六格錨＋baseline 重烤（**收官前置·既往連動·非本波**）

**範圍（reviewer W-6）**：`wf_f0.py:55-60` `GSA_EXPECT`（12 格）＋`verify/baselines/wf/f0/` **12 檔 CSV**
（`F.0_G值/合併決策/滑池槽診斷/逐槽J表/旗標消長/池差 × {0m,3.5m}`）。
**程序**：乾淨 `git worktree`（committed xlsx·blob `80f75ee`·記入 `PROVENANCE_F0.md`）→ `WV_BAKE=<scratch>`
產新值 → 逐格 diff 表人工核 → 覆寫。
**歸因（禁混·canonical §七.4）**：本步**僅** W脫鉤（07-19）＋S0d（07-20）；**G007 之 M-5 重排序連動屬 P-H**。
⚠️ **勿動 `data/xlsx`**（KL 2026-07-21：working xlsx 資料汙染論係「誤判·勿據行動」）。

---

## 三、P-A：`_corner_first_lot_G`（假設第 1 宗真 G·樂觀）

落點 app.py module 級·入 `_WF_NS_NAMES`·內呼 `_solve_G_one`（Q-M4）。

### 3.1 參數口徑（reviewer B-4/B-6/W-4/W-5 更正）

| 參數 | 值 | 依據 |
|---|---|---|
| `baseline_pt` | 左＝`corner_pt`；右＝`corner_pt + s_max_right·d̂` | Q-M2 樂觀（buf=0） |
| `S_max_limit` | 左＝`S_block_max`；右＝`_oblique_s_max` | B-6；二審 P5 證左端等價 `cum=0`·無漏 `_right_buffer_S` |
| `is_corner`／`W_prev` | `True`／`0.0` | 第 1 宗 |
| **`a`** | **`if '分攤登記面積_m2' in tp: round(分攤登記+面積_m2,2) else: round(面積_m2,2)`** | 🔴 B-4：**禁** `.get(A,.get(B,0))+B`（鍵缺重複計）。實配 7 處皆 `if in` 形。**併修 `probe_corner_trueG.py:120-122`** |
| **`a` 之來源** | **「即將餵給 `run_step_g` 的那份 parcels」**（非固定 `temp_parcels`） | 🔴 W-4：`sel:256-258` `build_parcels` 與 `temp_parcels` 同批 dict·deepcopy 後失聯 |
| `avg_depth`／`min_width` | **分寫兩路徑**（見下·reviewer 附帶） | — |
| `B`／`C`／`price` | `_compute_v3_finance`（P-0a） | `#20` |

**🔴 深度／最小寬之路徑分寫（reviewer 附帶必改）**：
- **harness 路徑**（`selection_pipeline`）：PK 時段 `f3_alloc_depth_by_label` 未鋪底（`stepg:196-202` 才寫）
  ⇒ **顯式自 `snapshot`** `街廓分配深度_m`／`get_min_lot_size`·缺值 loud。
- **app live 路徑**：`st.session_state['f3_alloc_depth_by_label']` 於 PK 區塊（`app.py:14860`）**之前**
  已鋪底（`app.py:14597/14599`）⇒ **讀 session·非 snapshot**（否則正常 UI 誤 raise）。

### 3.2 loud raise 邊界（Q-M4）
**raise**：`a`／`A`／`B`／`C`／`block_poly`／`d_hat`／`corner_pt`／`avg_depth`／`min_width` 缺或 ≤0；
被問到之側 `side_mid` 為 None。**不 raise**：`_solve_G_one` 幾何二分失敗 → `iterate_G_S`。

### 3.3 測項
A-1 vs `_solve_G_one` 直呼逐位全等（**改測「與實配第 1 宗 trunk A 在 a 相同時同值」**·NOTE-5 之鑑別力補強）；
A-2 左右 `S_max` 不同源；A-3 缺值 loud；A-4 退化 poly 走 fallback 不 raise；
**A-5 `a` 之 `if in` 形**（合成 `tp` 無 `分攤登記面積_m2` ⇒ `a==面積_m2` 非 2×·B-4 守衛）。

---

## 四、P-B／P-C：接線

### P-B（純加性）
1. `run_corner_pk` 增 keyword-only `snapshot`（無預設）·**8 呼叫端**（`run_verification:423`／
   `wd3_fragment_geom:93`／`wd4_tier_list:187`／`wg_g1_smoke:56`／`wg_g2_smoke:35`／`wg_g3:81`／
   `tools/y_dump_diff:59`／`probes/probe_corner_trueG:93`）。清 `wf_f0.py:40` dead import。AST 靜態閘「==8」。
2. `_pk_one_side_v12` 增 `require_g_map: bool=False`（B-1 保 golden）＋消滅 or-鏈 falsy 陷阱。
   **🔴 穿線（reviewer WARNING-f）**：`select_corner_lots_both_sides_v12`（`app:8134`/`sel` 對應）
   **同步加 `require_g_map` 參並穿下** `:8455-8456` 之 `_pk_one_side_v12(...)`。
   ✅ 零行為（二審 P2/P3）：生產 `g_values_map` 恆 ≥0.5；兩 golden 走 `G_value=1e9`＋位置引數呼叫。
   **禁改兩 golden fixture**。

### P-C（行為改）
1. `run_corner_pk` 算 `_G_true = ns["_corner_first_lot_G"](...)`；`g_values_map` 餵 `_G_true`；
   v12/pk 以 `require_g_map=True`。`_estimate_G_for_qualification` **不刪**（B-2·3 消費端）。
2. **B-3 鏡射（W-3 擴充）**：`app.py:14860-14939` **＋ `:14958`** ↔ `sel:316-370` **＋ `:401`** 同 commit。
   AST 欄集閘（`app:14886` 15 鍵 == `sel:334` 15 鍵·二審證差集空）。

### C-4 誠實紅表（B-2·v2 之「續綠」為假）
`G估(㎡)` 直接來自 `g_values_map`（`app:8482 G_for_threshold`→`:14958`/`sel:401`）⇒ P-C 後：

| 閘 | 檔:行 | P-C 後 |
|---|---|---|
| `v3·診斷{0m,3.5m}`（無豁免） | `run_verification.py:433-435` | 🔴 紅 2 格 → P-H 重烤 |
| `率接線 G估 欄變動{0m,3.5m}` | `:451-456` | 🔴 紅 2 格 → P-H 重烤 |
| `率接線無串聯{0m,3.5m}`（`skip_cols` 含 `G估`） | `:441-444` | ✅ 續綠（達標/選中零翻盤·**惟 P-D 後見 WARNING-c**） |

新增 `真G(㎡)` 欄**本身不打紅**（`diff_rows` 只走 baseline 既有欄）·`_bake_csv` 追加於後（reviewer P14）。
**P-H 重烤清單補**：`verify/baselines/W-D.1.2 診斷_退縮{0m,3.5m}.csv`＋`verify/baselines/v3/…` ×2。

---

## 五、P-D：**M-5 同歸戶合併規劃（帶優先序）**（主體·canonical §七 重寫）

### D-0 機制定位（canonical §七 T-2·**取代 v3「PK 自救→registry 拿回 F.0」**）

M-5 **非**「PK 端自救後自 F.0 拿回」，而是**同歸戶合併之整體規劃帶優先序**。
F.0 級0 對「含①類宗之同歸戶」係**未帶優先序之中間態**；M-5 以正確優先序重排。
⇒ 同一同歸戶之合併為**單一規劃**（①→②→③）·**結構上無雙重消費**（B-6 幻影自消·源 a 只配一次）。

### D-1 兩趟定點（循環相依）

```
趟0：run_corner_pk(rescue_ctx=None) → run_step_g → trunk A₀
     U₀ = { 宗 : G(A₀) < MinA[所屬街廓] }              # 未達 MinA（源候選）
     Corner₀ = { (blk,side,cand) : forced 端 ∧ E-1.7 真交集>1.0㎡ ∧ 真G(cand)<街角規定面積 }  # ①候選
趟1：對每 gid 建**單一合併規劃**（D-2 優先序·假設帳面）→ winner 定案 → 實體化 parcels₁
     → run_step_g → trunk A₁
定點：由 A₁ 導出之規劃 ≠ A₀ 導出者 → 再迭（≤3 趟）；不收斂 ⇒ loud raise（禁取末趟）
```

決策置 **`verify/m_rescue.py`**；8 呼叫端除 `snapshot=` 外零改（未傳 `rescue_ctx`＝趟0）。
app 端經 §7 引擎 ctx 回灌 `_m_rescue_plan`（不在 app 重寫決策·CLAUDE.md §7）。
**成本（W-9 已測）**：+14 次 `run_step_g` ≈ +3.0s（<2%）·S-8 不觸發。

### D-2 單一合併規劃（M-5(2) ①②③·per-candidate·假設帳面）

對每 gid（其宗跨 ≥1 塊·**M-2「其他可建築街廓」來源要件不變**）：

```
① 街角優先：對 gid 之每個 ∈Corner₀ 候選 cand（per-candidate·Q-M6）：
     救援源 = { s : gid(s)==gid ∧ blk(s)!=blk(cand) ∧ 可建築 ∧ s∈U₀ ∧ registry.remaining(s)>0 }
              （M-2 其他街廓·未達地·單一結算）
     以救援源**補足為度**填 cand 至「該街角地在街角街廓應分配面積 = 街角規定面積」
     （補量＝D-3 重跑迭代求最小 a′；消費序＝Q3）
     → cand 之假設 G ≥ 街角規定面積 ⇒ 該 cand 取得候選資格（帳面·未實體化）
   合格候選 ≥2（同端）→ **三指數定 winner**（canonical·現行 _pk_one_side_v12 第二關）
   winner 定案 → **實體化**該端規劃；非 winner 之假設規劃**丟棄**（Q-M6）
② 餘額他併：①後源之餘 a → 併其他「較大但未達 MinA[blk]」之 gid 宗（至達 MinA·重跑迭代）
③ 餘額回街角：②後目標皆達標而仍有餘 a ⇒ 餘額併入該街角地（街角＝最後歸宿）
消費序（全程）：Q3 — 保住原位次分配處數最大化；tie → 救較大者
```

**F.0 級0 之覆蓋（Q-M5 准）**：gid 含 ①-winner 者，其 F.0 級0 集中被本規劃取代
（源宗改配街角·非配 級0 標的）。**無 ①-winner 之 gid ⇒ F.0 級0 不變**（如 G010·池∅·同塊無跨占源）。

**Q2（canonical §2.2·絕對地板）**：`E-1.7 真交集>1.0㎡` **不放寬**；①僅解 G 門檻。
測項落 `select_corner_lots_both_sides_v12`（E-1.7 在 `app:8402-8403`·先於 pk·reviewer W-6）。

### D-3 補量：只取所需（Q3）＋重跑迭代（W-2）＋單位統一（B-7）

自變數＝**a′（目標 zone 口徑）**；上界 `supply′ = Σ_i a_prime_mode1(a_源_i, z_src_i, z_tgt)`；
前置**改 guard 非 raise**（🔴 B-3′）：`supply′` 使 `G(a+supply′) < threshold` ⇒
**跳過該端·記錄「同歸戶救不動·維持強制抵費地」·不 raise**（canonical「最後手段」仍是手段）；
loud 只留「`supply′` 足夠卻二分 40 次不收斂」。回填源宗消費 `a_源_i = a′_i·p(z_tgt)/p(z_src_i)`。

### D-4 consumed registry（B-6′·源→target 對稱凍結）

```python
class ConsumedRegistry:
    def claim(self, pid, amount, *, stage, target)   # 超額 loud
    def remaining(self, pid)
    def freeze_target(self, pid, *, stage)           # 受贈宗
    def freeze_source(self, pid, *, stage)           # 🆕 已為源者不得再當 target（對稱）
    def frozen(self)                                  # 源∪target·下游唯讀
```
**U 動態**：每次授予後即時自 U 移除「已消費至 0 之源」**與**「已成 target 者」（非固定 U₀）。
**下游唯讀**：`wf_f0._decide`／`wf_f2._decide`／`wf_f4` 母體先 `∖ registry.frozen()`；再 claim 超額 loud。
**materialisation**＝趟1 `parcels₁` 建構（`run_step_g` 前）：全額→移除；部分→扣減落 `面積_m2` 累加器欄
（`分攤登記面積_m2` 唯讀·四欄鐵律）·扣後 ≤0 視同全額·**加「`a` 不得 <0」硬閘**（WARNING-i）；
target `面積_m2 += Σa′`。**擴充語意（面積_m2 作扣減/讓出）明載報告**（WARNING-i）。

### D-5 守恆閘（`run_all` 新增·多 zone 修正·WARNING-a）

`Σ_i 消費_i·p(z_src_i)/p(z_tgt) == Σ target 面積_m2 增量`（逐 gid·tol 0.01㎡·**非單一換算比**）
＋ `無宗同時為源與 target` ＋ 既有 `每塊 ΣG+池 == 街廓 DXF 面積` 續綠。

### D-6 落地一致性硬閘（Q-M2）
trunk A₁ 後每街角 winner：`實配 G(A₁) < 街角規定面積` ⇒ **loud 停機**（非 warning·非降級）。
預期綠（T1 樂觀 vs 實配同號）。紅 ⇒ 停機上呈 Q-M2 重裁。

---

## 六、P-E：F.0 整合 ＋ `F2_GROUPS` expand（**不刪 `ROUTE_OUT`**·B-1′）

### E-1 F.0 級0 重排整合
`wf_f0._decide`／`_transform` 接 `rescue_ctx`：gid 含 ①-winner ⇒ 級0 標的與被併宗依 D-2 規劃重定
（源宗改配街角）。無 ①-winner ⇒ 現行 級0 不變。
**驗**：預測閘 b（G007 級0 重排·`628-20(2)` 回單獨 514.70；G010 級0 維持·五格零動）。

### E-2 `F2_GROUPS` expand（**contract 段不含 `ROUTE_OUT`**·B-1′）

🔴 二審 BLOCKED-1：`ROUTE_OUT`（`wf_f0:62-63`）**驅動控制流**（`:216 dest`／`:225 停機#4`），
且 E-1 導出式**第一項吃其產出之 `去向``（循環相依）⇒ **本波不刪**、列 backlog。

**導出式（二審雙路獨立同值 True）**：
```
F2_set = {gid : F.0「去向」以「轉F.2」開頭} ∪ {gid : F.0 未觸及 ∧ 跨≥2塊 ∧ qual 非空 ∧ 有非 qual 塊}
       = {G009} ∪ {G001,G021,G026,G027} = F2_GROUPS   ✅（雙情境）
```
**expand-contract**：expand（新增 `_f2_route`·保 `F2_GROUPS` 並斷言相等）→ migrate（`wf_f2:143` 吃現算·
`:146` raise 改分流）→ contract（**僅刪 `F2_GROUPS`**·`ROUTE_OUT` 留）。
🔴 **B-5′ 斷言時序**：expand 同值斷言**明訂於 `rescue_ctx=None` 趟0 快照**評估
（P-D 擾動後評估 ⇒ S-4 對合法變更誤停機）。

### E-3 三段測項（canonical·plan 必含·fixture 出處紀律）
`verify/fixture_m_rescue.py`：`test_topup_minimal`（①只取所需）／`test_remainder_to_m1`（②）／
`test_remainder_back_to_corner`（③）／`test_corner_precedence`（M-3(ii)·旗標單點可關）／
**`test_no_mutual_phantom`（B-6′·反例改 `G007`**——`G011/G030` 在 per-candidate 下仍可測，
但**須構造可失敗合成 fixture**·非恆綠·`fixture-provenance` 手算期望）。
✅ 可行：`wf_f2._decide`（`wf_f2.py:76`）純函式·合成 dict 直呼。

---

## 七、驗收預測閘（claude.ai 釘死·**落地必驗·不符即停機·不得改預測遷就實測**）

| # | 情境 | 預測（canonical §七.3） | 驗法 |
|---|---|---|---|
| **a** | 0m | F.0 決策表／六格錨／winner／forced **全零動**（0m R3右候選 628-45(2) 達標·倉內 baseline G=**195.25** ≥ 街角規定面積 **152.82**·優先序不觸發） | 0m 全 baseline byte 零 diff |
| **b** | 3.5m GSA | **僅 G007 一格連動**（`628-20(2)` 回單獨 **514.70**·引擎現算）；`G006/G009/G010/G014/G017` 零動；`G010` 級0（`628-43(1)→628-40(1)`）維持 | GSA 逐格 diff·僅 G007 |
| **c** | 3.5m forced | `R2左`/`R5左` 維持（池∅）；`R3右` 解鎖·面積入中央池·街角補足**恰=308.93＋餘額**（餘額實測） | 指配表 R3右 轉地主宗·capdecomp forced鎖 |
| **d** | 容量拆解 | 上界 **7→9**（vs 9）；**必標「上界·未窮舉·非可行性證明」**；可行性另以建構指派／真窮舉證 | capdecomp 重跑＋建構指派 |

> claude.ai 之「0m 205.27」係 3.5m 真G 之筆誤（0m baseline G＝195.25）；**≥152.82 關係兩者皆成立**·
> 結構結論（0m 全零動）不受影響。**預測數字不改·僅註明查得值**。

---

## 八、P-F／P-G／P-H

### P-F M-4（實測·左右雙側·`#25`）
F-1 3.5m 末端保留唯 R6 左·85.706㎡·`s∈[-0.0000,3.5114]`（`W-G.4_§4_P2_兩階段落位_f到g.md:102`）；
F-2 `_cond1`＝`wf_f4:1325`／`_end_gate`＝`:1338`（**二審 grep 定讞·`1467/1480` 不存在**），
惟 `_cond1` by-construction 近恆真 ⇒ **改對 `_end_gate` 之 `_unfront_area` ＋ `:1350` 末端 winner 前後集合斷言**
（WARNING-b·真正會被 M-1/M-2 打到者是 `G(㎡)`/`宗地寬度`/`flagged`）；
F-3 `fixture_end_reserve` 12 項續綠；F-4 `fixture_end_fallback` 左右各 5 項續綠；F-5 E3 latent；
F-6 被消費源宗若為末宗 → 重列 `_end_band` 窗·左右各驗·具體化（WARNING-c：P-D 後 diag 可能「缺列」非欄值差）。

### P-G 驗收（措辭依 〇.1·**禁「釋回抵費地」**）
重跑 capdecomp：報「合併後仍需調配群數 vs 可容上界」、**面積回歸中央調配池後可及容量**、
「9 戶差 2 戶」是否消失。**驗收靶（reviewer 附帶更正·非 918.50/三端）**：
**實測可行域 ≤ R3右一端**·街角補足 308.93＋餘額；R2左/R5左 維持 forced（池∅）。
**W-7 誠實註**：3.5m log 自述 `未窮舉` ⇒ 上界 9≥9 **非可行性證明**·另以建構指派/真窮舉證；
需求群成員差（BEFORE `{G003,G004,G014,G015,G016,G018,G020,G025,G033}`）並列。
`W-F F.4` 殘紅（E2 上界7<需求9）若遷移 ⇒ 誠實定位。

### P-H 合法重定錨（獨立 commit·**M-5 重排序**成因·與 P-0c 分列·Q-M3）
1. BEFORE `df9834c`；**禁改 `skip_cols`/`_exp_gd`/退役閘**。
2. **重烤清單（二審 B-2′·補齊）**：
   - `verify/baselines/wf/f0~f4` **44 檔**（M-1/M-2 落地後 trunk A→B→C→D→E 連動）
   - **`wf_f0.GSA_EXPECT` 第二次重定錨**（G007·**引擎現算·非硬編**·§九 改「P-0c＋P-H 兩次」）
   - `W-D.1.2 診斷{0m,3.5m}` ×2（v1）＋ `v3/…` ×2（B-2）
   - `第 1 宗街角地指配結果_退縮{0m,3.5m}`／`W-D.1.3-d 驗收`／Step G 三表／W-D.3／W-D.4（實跑逐檔列）
   - `F1_REVERIFY`（`wf_f4:61`）／UC9898 R1左 3.5m winner
3. **逐格歸因**：{Q1 口徑／M-5 重排序／M-1 搬移／連動}·**無法歸因 ⇒ 停機不重烤**·**與 P-0c 之 W脫鉤+S0d 分列**。
4. commit `rebake(裁定M): M-5 重排序之合法重定錨`；報告獨立節載前後值。
5. ⚠️ golden 圖 8（0.6685/0.3315）變動＝**實作 bug**。V2/V3/V8/V9 維持待烤。
6. 🚩 **「無串聯 vs v1 原錨」閘之重烤＝治理判斷·上呈**（WARNING-h·不自決）。

---

## 九、泛用四約束逐項自查（優先序機制 data-driven）

| 約束 | 自查 |
|---|---|
| 禁塊名 | 跨占＝E-1.7 真交集；未達＝`G<MinA[blk]`/`<街角規定面積`；同歸戶＝`gid`·**禁 G007 入碼** |
| 禁側別 | 左右差異僅 `S_max_limit`/`d_hat`·`side` 驅動·A-2 守衛 |
| 禁常數 | MinA/街角規定面積/深度/寬**現算或自 snapshot**；容差明列報告 |
| 換案成立 | 全走資料旗標（`has_side`/`forced_offset`/可建築/`gid`/F.0 `去向`）；`_RESCUE_ORDER_KEY` 單點可換 |

**常數二分**：**決策常數⇒刪**：`wf_f2.F2_GROUPS`(:40)〔`wf_f0.ROUTE_OUT`(:62-63) **本波不刪·backlog**·B-1′〕；
**對拍錨⇒不動**：`F1_REVERIFY`/`E0_EXPECT`/`E2_NAMED`/`COMP_EXPECT`/`F1_TARGET`；
`GSA_EXPECT`**⇒ P-0c（既往）＋P-H（M-5）兩次重定錨**。

---

## 十、⛔ 停機條件（真域邊界）

| # | 觸發 | 動作 |
|---|---|---|
| S-1 | D-6 落地一致性閘紅 | 停機上呈 Q-M2 重裁 |
| S-2 | M-3(ii) 被實測打破 | 停機上呈 |
| S-3 | E-1.7 須放寬方可行 | 停機上呈（Q2 前哨） |
| S-4 | E-2 導出式同值斷言破（趟0 快照下 ≠ `F2_GROUPS`） | 印差集·loud·🚩上呈 |
| S-5 | 兩趟定點 3 趟／M-1 注入 6 趟不收斂 | loud raise |
| S-6 | P-0c 或 P-H 有無法歸因之差異格 | 停機不重烤 |
| S-7 | 圖 8 golden 變動 | 停機修碼 |
| **S-9** | **驗收預測閘 a/b/c/d 任一不符** | **停機查因·不得改預測遷就實測**（canonical §七.3） |

---

## 十一、🚩 上呈（CC 不拍板·**不阻施工**）

1. **`F2_GROUPS` 為何排除 G006／G007**（二群於 R2 尚有非達標宗·刻意留 F.4 抑或漏網）＝規則本意。
2. **`W-F F.4` 3.5m E2「上界 7 < 需求 9」**是否本波處理（現標「既有·誠實定位」）。
3. **P-0b 殘留分岔**（`_tab6_burden` app 靜默退 B+C）本波順修抑或 backlog。
4. **「無串聯 vs v1 原錨」閘重烤**是否等於自廢該閘（治理判斷·WARNING-h）。

---

## 十二、次步
1. 立即送 reviewer（第三輪）·不停等。2. 綠後依 §一 施工·每步 `py_compile`＋grep＋`run_all`·FAIL 集不新增名目。
3. 報告 `docs/reports/W-G.4_裁定M_施工報告.md`·聊天＝ping。4. **未 push 不報收官**。
