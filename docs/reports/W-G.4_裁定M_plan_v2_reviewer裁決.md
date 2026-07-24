# W-G.4 裁定 M — plan v2 reviewer 裁決與 **CC 逐條復驗**

> reviewer（`redistribution-reviewer`·獨立復現）判 **BLOCKED×7 ＋ WARNING×9 ＋ NOTE×4**，總判「須改後再審」。
> 基準 `706cb17`。本檔＝**我逐條親自復驗**之結果（依 CLAUDE.md：**不採信 reviewer 文字**，
> 一律自跑 grep／CSV／AST／git 證之）。
> 結論：**BLOCKED 6 項成立（必辦）、1 項不成立（reviewer 誤·已駁）**；WARNING 9 項全成立，
> 惟 **W-7 之前提被倉內 KL 裁定推翻**（見 §三）。

---

## 一、BLOCKED 逐條復驗

| # | reviewer 主張 | **我的復驗** | 裁 |
|---|---|---|---|
| **B-1** | P-E 之 expand 述詞（`qual 非空 ∧ 跨≥2塊` == `F2_GROUPS`）**必破**；真規則須吃 F.0 `去向` | **成立**。我直讀倉內 `verify/baselines/wf/f0/F.0_合併決策_退縮{0m,3.5m}.csv`（**雙情境逐字相同**）：`G009→轉F.2(...)`、`G014→轉F.4(...)`、`G006/G007/G017→達標·留置原位`。⇒ G006/G007/G017 跨≥2 塊且 qual 非空**卻不在** `F2_GROUPS`——因 **F.0 已解決**。我的述詞漏掉「F.0 已觸及」這一維 | ✅ **必辦** |
| **B-2** | 「`G估(㎡)` 欄值不動 ⇒ `:451-456` 續綠」**為假** | **成立**。`app.py:8482 cand['G_for_threshold'] = round(cand_G, 2)`（`cand_G` 即 `g_values_map` 值）→ `app.py:14958`／`verify/selection_pipeline.py:401` 之 `'G估(㎡)': round(float(_dc.get('G_for_threshold',0) or 0), 2)`。**`G估(㎡)` 直接來自 `g_values_map`、非來自保留之 `G_estimated` 鍵** ⇒ 改餵真 G 該欄必變 | ✅ **必辦** |
| **B-3** | §七 F-2 行號錯：`_cond1` 應為 `wf_f4:1467`、`_end_gate` `:1480` | 🔴 **不成立·駁回**。實跑 `grep -n "_cond1\|_end_gate" verify/wf_f4.py` → `1325: _cond1 = not bool(fo.get(_has_side_key))`／`1338: _end_gate = _cond1 and (_unfront_area > 1e-3)`（另 1340／1350／1355 為消費端）。**全檔 1575 行，`1467`／`1480` 無此二符號**。plan v2 所寫 `1324-1325`／`1338` **正確** | ❌ **駁**（reviewer 誤） |
| **B-4** | §3.1 之 `a` 取值 `tp.get(A, tp.get(B,0)) + tp.get(B,0)` **鍵缺席時重複計 `面積_m2`** | **成立**。實配 7 處一律 `if '分攤登記面積_m2' in tp:` 形（`stepg:260/556/627`；`app:7462/15624/16044/16124`）。且 `verify/probes/probe_corner_trueG.py:120-122` 已把錯形寫進碼（現因 `app.py` 無條件寫該鍵而**潛伏**） | ✅ **必辦**（含修探針） |
| **B-5** | §〇.5 六格錨過期**歸因寫錯**；且實破 **6 格**非 1 格 | **成立**。`git log -S "362.08" -- verify/wf_f0.py` → **唯一命中 `7ce98e6`**。倉內 `docs/reports/W-G.4_run_all紅_working_xlsx資料阻斷_上呈.md:3` 載 **KL 2026-07-21 更正**：「錨 362.08 由 `0c9b7e7`（07-17）設，而 **W脫鉤(07-19)＋S0d(07-20)** 之後改了 G 之 W/S 輸入項 → 359.43 係**預期新值**。**非資料壞、非 regression**」。`GSA_EXPECT`（`wf_f0.py:55-59`）＝**每情境 6 格 × 2 情境**＝12 格母體 | ✅ **必辦** |
| **B-6** | D-5 registry 只凍**源宗**、未凍 **target** ⇒ B-5 幻影（+161.80／+98.00）未消 | **成立**（設計缺口·我承認）。`U` 取自趟0 且趟1 內不更新 ⇒ 「A 端之 target 仍 ∈ U₀ ∧ ∉ consumed」⇒ 可被 B 端當源 ⇒ 同一塊 a 算兩次 | ✅ **必辦** |
| **B-7** | D-3 二分搜尋**單位混用**（`supply` 為源 zone 口徑、`a` 為目標 zone 口徑） | **成立**。`wf_f2.a_prime_mode1` 之存在即證跨 zone 須換算 | ✅ **必辦** |

### B-3 之駁回意義（**非文字之爭**）

plan v2 §七 F-2 之「**reviewer 更正**」標記係引 **plan v1 裁決 §二**（前手 reviewer 之更正）。
本次 reviewer 反以 `1467/1480` 覆蓋之，並斥「把錯的數字包裝成 reviewer 更正·風險更高」。
**實查證明原值正確、新值不存在** ⇒ **維持 `1324-1325`／`1338`**。

> 📌 此即 CLAUDE.md「**不採信實作者說詞**」之對偶：**亦不採信 reviewer 說詞**。
> 若照單全收，本波會把一個**正確**的行號改成**不存在**的行號，且下一波再被「更正」回來——
> 錨在兩份文件間來回擺盪、無人知何者為真。**檔行號一律以當場 grep 為準。**

---

## 二、WARNING 逐條（全成立·併入 plan v3）

| # | 內容 | 我的復驗 |
|---|---|---|
| **W-1** | P-0a「原封不動位移 `:90-192`」**不成立**：return dict 漏 `SB`／`_build_blocks`；且 `:170-177` 夾在中間 ⇒ 實為**兩段**非連續位移 | **成立**。我跑 AST 逃逸分析（在 `:90-192` 賦值、於 `:193+` 被讀）：`B_value`／`C_for_calc`／**`SB`(196,201)**／**`_build_blocks`(197,202)**／`_tab6_burden`(323)／`post_price_by_block`／`pre_price_by_zone`／`sb_rows_by_label`。plan 之 return dict 確實漏兩個 |
| **W-2** | P-0b 兩份 `_solve_one` **可執行語句逐字全等**（抽出前提成立 ✅），**但**閉包 `_tab6_burden` 兩邊不同源：`stepg:172-177` 缺值 raise ／ `app:14437-14439` 缺值靜默退 `B+C` | 成立·**須於報告載明殘留分岔**（no-silent-fallback 之既有違例·非本波引入 ⇒ 列 backlog、不擴大） |
| **W-3** | B-3 鏡射範圍 under-scoped：`G估(㎡)`／新 `真G(㎡)` 之寫入點在 `app.py:14958`／`sel:401`，**兩範圍皆未涵蓋** | 成立（我實 grep 確認行號） |
| **W-4** | §3.1 把 `a` 源釘死 `temp_parcels`，而 `build_parcels` 與之**同一批 dict 物件**（`sel:255-258` 無 copy）⇒ P-D deepcopy 後 a′ 注入不被看見 | 成立·**須改綁「即將餵給 `run_step_g` 的那份 parcels」** |
| **W-5** | §九 常數二分法漏 `wf_f0.ROUTE_OUT`（`:62-63`）——**驅動 raise（控制流）**、與 `F2_GROUPS` 同族 | 成立。`:216` 決 `dest`、`:225` `not ok and gid not in ROUTE_OUT → 停機#4`。M-1/M-2 使新 gid 在 F.0 轉不達標即炸 |
| **W-6** | P-0c 範圍未明：`GSA_EXPECT` 字面之外，`verify/baselines/wf/f0/` **六份 CSV** 全走 `diff_rows` | 成立（目錄實查：`F.0_G值/合併決策/滑池槽診斷/逐槽J表/旗標消長/池差` × 雙情境＝12 檔） |
| **W-7** | 重烤會把**未 commit 之 working xlsx** 烤進 baseline | **程序要求成立**（見 §三 之重要保留） |
| **W-8** | D-2（每個候選建池）與 D-4（只用最強候選之缺口排序）**內部不一致** | 成立·須擇一寫死 |
| **W-9** | 成本未量測：P-D(+1)／E-3(+6) × 雙情境＝最壞 **+14 次 `run_step_g`** | 成立·**P-D 前先量單次壁鐘** |

---

## 三、⚠️ W-7 之**前提被倉內 KL 裁定推翻**（reviewer 犯 `failure-archaeology #27`）

reviewer 引 `docs/reports/W-G.4_run_all紅_working_xlsx資料阻斷_上呈.md` 之 **:25／:29／:31**
（「committed→362.08；modified→359.43 ⇒ F.0 之 359.43 係**資料驅動**」）佐證「working xlsx 汙染」。

**但同檔 :3 即為該上呈之撤回**：

> ❌ **KL 2026-07-21 更正·本上呈誤判·勿據行動**：F.0 紅係**過期錨**…
> **非資料壞、非 regression、非施工可致**。committed xlsx（blob `80f75ee`·12.38MB）**完好、整波未變**。
> **勿動 data/xlsx、勿追此紅**

⇒ reviewer **只讀證據表、未讀裁決段**，正是 `#27`（誤 J／誤 M／誤 N 同族）之再現：
**數字逐位無誤，但把「已被撤回之前提下才成立之量」當無條件事實引用。**

**分辨（重要·勿混）**：
- **「working xlsx 造成六格錨破」＝假**（KL 已裁·勿再引·勿追）。
- **「重烤須自 committed 資料產出」＝真**，但其依據是 `fixture-provenance`（**baseline 須可由倉態復現**）、
  **不是**那份已撤回的資料汙染論。⇒ **W-7 之作法照辦、理由改寫**。

---

## 四、NOTE

1. `verify/wf_f0.py:40` import `run_corner_pk` 卻從不呼叫＝dead import（順手清·不影響閘）。✅ 採
2. `fixture_end_fallback` 每側實為 **5** 項（漏「①抵費地末=R_end」），plan 列 4。✅ 採
3. reviewer 稱 plan §七 F-1 括號內「R6 池帶第二片 `36.4339`／`1651.0218`」與其實跑不符（其得 `34.0515`／`1542.9818`）。**我引處為本波 BEFORE `run_all` 之 T2-DIAG（`M_before_runall.log`）**，reviewer 引處為其 trunk A —— **二者不同快照、非矛盾**。惟該括號對 F-1 之判準**無舉證作用**（F-1 之錨是「未臨正街 85.706／末端帶 s∈[0,3.5114]」，倉內 `W-G.4_§4_P2_兩階段落位_f到g.md:102` 已載）⇒ **plan v3 刪該括號**（避 `#25` 之「單點錨掩護未參數化維度」）。
4. 「G/a ∈ 0.5594–0.5828」僅作「禁固定比率」之論據、不入算式 ⇒ 可接受。✅

---

## 五、reviewer 之**正面產出**（採納·入 plan v3）

1. **`F2_GROUPS` 之真導出式**（reviewer 實跑證等·雙情境 `True`）：
   ```
   F2_set = {gid : F.0「去向」以「轉F.2」開頭}
          ∪ {gid : F.0 未觸及 ∧ 跨≥2塊 ∧ qual 非空 ∧ 存在非 qual 塊}
   ```
2. **M-1 母體實為 `{G011}`**（雙情境·跨 R2/R3）——**正是** plan v1 裁決 B-5 所舉之
   `628-42(1)@R2左 ↔ 628-42(2)@R3右` 對稱互救群。⇒ M-1 與 B-5 幻影**同一標的**、非兩件事。
   ⚠️ 該量測係於 `WV_BAKE`（過期錨）下所得 ⇒ **P-0c 後須重量**（`#27`：量連著前提搬）。
3. **AST 欄集結構閘可行且現為綠**（reviewer 實作跑過：`app:14886` 15 鍵 ／ `sel:334` 15 鍵·差集空）。
4. **P-0a/P-0b 不需等 P-0c**（其判準與 F.0 紅無關）。

---

## 六、reviewer 交回不判之三題（我同意不由 CC 拍板·**上呈**）

1. **`F2_GROUPS` 為何排除 G006／G007**——「這兩群在 R2 尚有非達標宗，是刻意留 F.4 還是既有漏網？」＝**規則本意**。
2. **樂觀口徑（Q-M2）是否合附件二本意**——已由 KL 裁定，CC/reviewer 只驗算術一致性。
3. **`W-F F.4` 3.5m E2「上界 7 < 需求 9」結構性不可行**是否本波處理——plan 標「既有·誠實定位」係正確做法。

---

## 七、次步

依本裁決寫 **plan v3**（6 項 BLOCKED ＋ 9 項 WARNING 全併入；B-3 維持原值）→ **再送 reviewer** → 施工。
