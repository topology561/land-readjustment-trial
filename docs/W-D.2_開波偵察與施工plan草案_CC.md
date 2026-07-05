# W-D.2 §3 滑池槽 — 開波偵察報告＋施工 plan 草案（CC → claude.ai 審）

> 新體制第一波。依驗收路徑：**本檔＝plan 階段產物**（含 §2 偵察答案），claude.ai 審後才實作。
> 碼證全部取自公倉 `1b290e4` 之 app.py（＝私倉 db14034＋W-V additive，G 引擎零差異）。

## 〇、換倉過渡回報（一次性，已完成）

- 開發基地已切至公倉工作副本；私倉封存不再 commit。
- CC memory 已搬至新專案本機路徑（`~/.claude/projects/...land-readjustment-trial/memory/`，
  倉外、天然不入 git）。
- 公倉樹內 `python verify/run_all.py` 綠（換倉後複驗）。

## 一、規格 vs 現碼不符清單（W-D plan 成文於 .1.3 五波前；上呈、不靜默改編）

| # | 規格所述 | 現碼實況（公倉 1b290e4） | 影響 |
|---|---|---|---|
| M1 | D-1 裁示語「`_select_pool_slot` 純函式**不變**、已預驗 8/8」 | **全樹不存在此函式**（grep 0 命中，app/tests/verify 皆無）——「預驗」係 claude.ai 規格層驗算 | §3 需**新建**該函式＋單測，非改造既有 |
| M2 | §3「候選槽位∈序列各間隙」擇 J 最大 | 現行池槽＝**N/2 人頭中點規則**（`_midpoint=(N+1)//2 or N//2`，app.py ~14822-14827，註記「KL 規範」）——按筆數對半、與寬度/Rw 無關 | §3 的取代對象即此段；J 最大化後 N/2 規則整段刪 |
| M3 | 守恆接線 hook：`_forced_offset_map` 之 `left/right_corner_min_area` 從不賦值 | 證實，且**雙缺**：①餵入端 `_forced_offset_map`（~14013）只有 forced/has_side 四鍵；②消費端 caller（~14805）只取 `'ordered'`，`_spatial_order_parcels_v2` 回傳之 `left/right_corner_offset_area` **無人讀** | 守恆接線要建兩端＋逐塊 ledger（見 P4） |
| M4 | plan 引 app.py:14990-14996（strip 放置）、:5734（v2） | 行號漂移：v2 def @5714、推進迴圈 ~14934-15106、池（幾何剩餘）@~15108-15192 | 錨一律用符號名（wave-discipline 交接紀律） |
| M5 | §3.1 之 `b`（forced 起始 W，⊥ALLOC） | 現碼 buffer＝`range 面積 ÷ D_avg` 進 **cum_S**（S 軸），②ΣRw 對拍表（~15608）同用此近似當起始 W | 軸近似沿用與否＝Q2 |
| M6 | — | `CLAUDE.md`（公倉版）仍寫舊分支 `claude/fix-cad-topology-mismatch-QfyPU`／私倉語境 | 建議 claude.ai 出換倉版 CLAUDE.md（CC 不逕改憲法層） |
| M7 | §3.1 STEP2 telescoping ΣRw | 已有現成同式對拍表（步驟 G「②各街廓角側 Rw 累積差額」~15608-15635） | 新診斷可重用其口徑，兩處必同源 |

## 二、§2 範圍偵察題（答案＋建議）

**§2 現況＝「落地一半」**：
- 已落地：`_spatial_order_parcels_v2`（app.py 5714）以 FRONT_LINE 投影序＋winner 最小擾動插入，
  `pre_position` 即原位次——Step G 實際位次**已是**投影序，§3 需要的輸入 `P=[p_1..p_n]` 現成。
- 未落地：投影序活在 Step G 當下 local 變數，**無單一真相源輸出**；街角 PK tiebreaker
  （`_pk_one_side_v12` ~7922-7927）與診斷欄（~13944-13947）用「距角序」暫行近似，
  `TODO(W-D §2)` 標記兩處（grep 可得）。雙套原位次並存。

**§2 是不是 §3 前置？——不是（演算法層）**。§3 只需投影序輸入，已有。
但 tiebreaker 換源有一個**凍結衝突**（本偵察的關鍵發現）：
> 診斷 CSV「原位次(距角序·暫行)」欄現值＝距離（42.06、22.03…）；換吃正典投影序後
> 該欄變 rank（1、2、3…）→ **W-D.1.2 診斷 baseline（v1，凍結）該欄必紅**。
> KL 已裁「既有 10 張 baselines 維持 v1、run_all 任一格紅＝停」→ tiebreaker 換源
> **在本波做必然撞凍結閘**；它天然屬於「KL 收波後新診斷轉正 baselines v2」那一刻。

**範圍建議（修正式 c）**：
- **(c′) §3 獨立先行**＋把「正典原位次」抽成具名純函式（`_projection_order(...)`，
  §3/Step G 同源消費）→ 單一真相源本波**誕生**；
- **PK tiebreaker 換源與診斷欄改 rank 排到 baselines v2 升版時刻**（W-D.2 收波、
  KL 域確認後）與新診斷一起轉正——屆時 TODO(W-D §2) 兩處一次消滅，v1 凍結閘全程不破。
- 備註：tiebreaker 僅同分(4dp)觸發，本案各端 winner 分數唯一（無同分案例）→ 換源
  預期零 winner 變化，風險僅在診斷欄顯示——正因如此它是「v2 隨波轉正」的完美搭車項。
- 不建議 (a)（§2 完整正典化＋§3 同波＝兩種驗收尺標糾纏、範圍膨脹）
  與 (b)（§2 先小波＝多一輪驗收成本卻不解除任何 §3 阻塞——本來就沒有阻塞）。

## 三、§3 施工 plan 草案（待審）

**P1 `_select_pool_slot` 純函式＋golden 單測**
§3.1 STEP1-3 全式落地（K 域含雙側/單側/無側、R 飽和、ε=1e-6·J*、dev tie-break、
pinned 不可頂掉）。`tests/test_pool_slot.py`：w=[12,24,6] 雙側等權 → k*=1（J=180）
＋8/8 預驗全表（AST 抽函式、比照 golden 模式）。此測併入 `run_all.py` 常設。

**P2 D-1 bootstrap（推進抽可重入函式）**
每塊推進抽成可重入函式：**基準趟**（暫定 k=naïve N/2）不 append g_rows、不寫
session_state → 取真 w_i（⊥ALLOC cut 幾何）→ 餵 `_select_pool_slot` 得 k* →
**正式趟**才落 g_rows。防重複 append 為 reviewer 必驗項。

**P3 N/2 規則替換**
`left_group/right_group` 改按 k* 切分；N/2 中點段**整段刪**（無 fallback、無雙路徑）。

**P4 守恆接線（本波必做 hook）**
① `_forced_offset_map` 增 `left/right_corner_min_area`（值＝PK 之 range 面積，
＝指配表【左/右】最小面積同源）；② caller 消費 `_v2_res` 之 corner_offset_area；
③ 逐塊守恆 ledger：`ΣG ＋ 中央池 ＋ 角落抵費地 ＝ 街廓 DXF 面積`（<1㎡），其中
角落抵費地/中央池＝幾何剩餘之**拆帳呈示**（池重定位、非新增面積——g-formula skill 池規則）。
3.5m 之 R5左/R2左/R3右 三塊必過。需先驗：buffer 區幾何確實落在 `offset_land`
（幾何剩餘）內、無雙計。

**P5 新診斷輸出（可變/新增欄；D-2 對照表）**
逐塊：`naïve k vs k*`／各候選槽 J 表／`舊vs新 ΣRw_L,R`／池槽位／
`ΣG＋池 vs 街廓面積`／角落抵費地重定位帳。UI expander＋輸出 CSV。
凍結欄：10 張 v1 baselines＋run_all 11/11 全程綠（§1 上游不受擾之證）。

**P6 harness 擴充（範圍見 Q4）**
verify/ 新增 Step G headless 段 → 新診斷 dump 至 `verify/out/got_wd2_*.csv`（先無
baseline，供 claude.ai pull 判讀）；KL 收波後轉正 baselines v2＋PROVENANCE v2。

**停機（D-2 三種）**：真不變量破（a／深度／ALLOC⊥FRONT／白縫／守恆<1㎡）／
J 下降（k* 之 J < naïve k 之 J，最佳化反變糟）／守恆破。
**預期變（不停）**：逐筆 G、各側 ΣRw（R1右 81.49%→↑、R4右 90.56%→↑ 為靶方向）、
池大小與槽位、筆寬位次。

## 四、上呈問題（claude.ai 裁）

- **Q1（§2 範圍）**：採 (c′)？——§3 先行＋正典投影序函式誕生；tiebreaker 換源與
  診斷欄改 rank 隨 baselines v2 轉正。
- **Q2（b 軸近似）**：forced 起始 W 沿用現行 `range面積÷D_avg`（S 軸近似、與②表同源）
  或改真 ⊥ALLOC 量測？CC 建議**沿用**（本案 ALLOC⊥FRONT≈90°、斜差 <1%；兩處口徑
  一致優先），列為已知近似記入規格。
- **Q3（F×l₁ 來源）**：F＝該側 SIDE_LINE 全長（`f3_cad_side_lengths_by_side`）、
  l₁＝側街路寬查負擔尺度表（取半）——與 Step G 現行 g_rows 之 `F(m)`/`l₁ 側面尺度`
  同源即可？（快照側街尺度＝1、8m 路。）
- **Q4（harness 範圍）**：Step G headless 化＝把推進迴圈（~14554-15200，含
  solve_G_binary、A 地價比、B/C）納 driver——工程量另成一坨。CC 建議**同波但分段**：
  P1-P5 先行（新診斷由 KL 跑 app 出 CSV、claude.ai 判），P6 緊接同波內完成
  （快照升 v2 需接財務參數：Tab4/Tab5 地價、C%——快照已預埋、標「本波 harness
  不消費」者屆時轉正消費）。若 claude.ai 認 P6 應獨立小波（W-V.2），CC 無異議。

## 五、驗收靶先行（wave-discipline；動工前具名）

- **凍結**：10 張 v1 baselines 逐格（run_all 11/11）；a（628-18(2)=381.09）；
  深度（R2=43.9）；ALLOC⊥FRONT≈90；Tier1 gate=False；`面積_m2`=0；不跨塊搬地。
- **具名靶（方向）**：R1右（末筆 W 12.37m、ΣRw 81.49%）與 R4右（14.79m、90.56%）
  ＝「未滿側」，左側大幅溢出（42.7m／46.87m）→ k* 應左移餵右側、ΣRw_R ↑；
  R5左/R2左/R3右（3.5m forced）守恆 ledger <1㎡；w=[12,24,6] 單測 k*=1。
  J(k*) ≥ J(naïve) 逐塊恆成立（等號僅平坦段）。
- **可判定規則**：k* 變動塊之 J 表可複算（純函式、輸入輸出全 dump）；
  ΣRw 對拍沿用②表口徑 telescoping。

——以上。claude.ai 審後（Q1-Q4 裁定＋plan 修訂），CC 進 plan mode 施工。
