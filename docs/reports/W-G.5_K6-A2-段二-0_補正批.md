# W-G.5 — **K-6-A2 段二-0：補正批**

> **基準**：`9880164`　**分支**：`wip/s1-endpart`
> **性質**：八項補正。其中 **一-8 有行為變更**（K-9-2 警示遷出收合面板），
> 其餘為入庫、正典、登記、報告更正。
> ⚠️ 施工單所引之行號**全部當場重 grep 確認**，未沿用其數字；差異見 §九。

---

## 一-1 段一之 probe log 未入庫（**根因項**）

**查證**：`verify/probes/probe_ruling_K9_block_depth.py` 之 `LOG` 指向
`verify/out/probe_ruling_K9_block_depth.log`（`grep -n "^LOG = " verify/probes/probe_ruling_K9_block_depth.py`）。
`verify/out/` **已入庫 79 支 `.log`**；`.gitignore` 於該目錄**只擋** `verify/out/got_*`
與 `verify/out/W-D.4_*`（`cat .gitignore`）⇒ **本目錄係追蹤中、非未追蹤**
⇒ 段一未入庫該 log **確係偏離既有慣例**，非目錄設計使然。

**辦理**：以最終碼重跑該 probe，log 入庫。
**重跑輸出**：六街廓零警示、餘裕最緊者 R4 `+19.084m`（與段一同值——本批未動判準）。

---

## 一-2 對照靶 `K8_seg3_C.log` 全歷史從未入庫

**查證**：`git log --all --oneline -- verify/out/K8_seg3_C.log` ⇒ **空**。

**擇 (a)：把該輪 log 入庫。** 理由——**(b) 不可行**：
全部**已入庫**之 `verify/out/*.log` 中，132 名目者**清一色 130 PASS／2 FAIL**
（`K6A_E_after`／`K6A_patch`／`K8_seg1`／`K8_seg2`／`K8_seg3_EF`／`K8_seg3_pre`／
`M_D1_runall`／`M_P0c_main_verify`／`M_PC_full` 等），
唯一非此者為 `K8_seg2_cascade_ifsnapshot.log`（108／24·另一實驗）
⇒ **倉內無任何已入庫檔可充當 86／46 之靶**。

**哪一支才是現行 132／86／46 之產生輪**：**`verify/out/K8_seg3_C.log`**。證據二項（非推測）：

1. **時序**：其 mtime `2026-07-31 23:52:14`，K-8 §三 commit C（`56b345a`）之提交時刻
   `2026-07-31 23:56:55` ⇒ log **早 4 分鐘**，符合「跑完才 commit」。
2. **倉內既有文件已指認**：**已入庫**之 `docs/reports/W-G.5_K8-段三_commitC_重錨解封.md`
   §二 標題即「驗收（`verify/out/K8_seg3_C.log`·全母體 `K8_seg3_C_viol.csv`）」。

⇒ **現行 CLAUDE.md 所載之 86／46 基線，其產生輪之 log 在本次補正前從未入庫。**

**同類補正（一併辦理）**：`W-G.5_K8-段三_commitC_重錨解封.md` 另引
`K8_seg3_B.log`／`K8_seg3_C_bake.log`／`K8_seg3_C_viol.csv`，**三者亦未入庫**
⇒ 同屬「已入庫報告引用不存在檔案」之同一缺陷，**同批補入**。
（該報告另引 `verify/out/got_F.0_*`，係 `.gitignore` 明列之 harness 重生成物，**不入庫**。）

**尺寸慣例查核**：`K8_seg3_C.log` 1.7M；倉內已入庫最大者 `M_0725_PF_bake_diag.log` **3.1M**
⇒ **未逾慣例**。

### 一-2-1 全倉窮盡稽核：**本缺陷係系統性、非本批獨有**

既然施工單指此為「**根因項**」、且令「段二不得重犯」，遂對**全部已入庫報告**做窮盡掃描
（母體＝`git ls-files -z docs/` 之 **143** 支 `.md`）：

> ⚠️ **首次掃描漏了 138 支**——`git ls-files docs/` 對**中文檔名**輸出**八進位跳脫**
> （`"docs/W-A.3_\347\264\260\351\203\250plan.md"`），致 `grep '\.md$'` 只中 **5** 支 ASCII 檔名者。
> 此即 `CLAUDE.md` 行號衛生節所載之陷阱（「中文檔名在 `git --stat` 會轉八進位跳脫 ⇒ grep 檔名會瞎」）。
> **改用 `git ls-files -z … | tr '\0' '\n'` 後方取得真母體 143。**
> 🔴 **記為本批之過程失誤**：若未複查，本節會以「零命中」結案——**與事實相反**。

**結果：11 支「已入庫報告引用、但未入庫」之檔（工作樹皆存在）**：

| 檔 | 被引於（已入庫報告） |
|---|---|
| `K6A2_seg1_runall.log` | 段一（本人） |
| `probe_ruling_K9_block_depth.log` | 段一（本人） |
| `K8_seg3_C.log` | 段一（本人）＋ K-8 段三 commitC |
| `K8_seg3_A.log`／`K8_seg3_A_viol.csv` | K-8 段三 commitA |
| `K8_seg3_B.log` | K-8 段三 commitB ＋ commitC |
| `K8_seg3_C_bake.log` | K-8 段三 commitC |
| `p2fg2_probe.log` | W-G.4 §4 P2 兩階段落位 f到g |
| `probe_stage_order_R1_3.5.log` | W-G.4 §4 兩階段落位 坐實 |
| `run_all_Y2.log` | W-G.4 run_all紅 xlsx 上呈 ＋ 裁定M plan_v3 |
| `run_all_rebake.log` | W-G.4 run_all紅 xlsx 上呈 |

**處置：11 支全數入庫。** 理由——留下任一支即「引用不存在檔案＝視同未驗」之殘留，
與施工單「段二不得重犯」直接牴觸；且該 11 支**皆已存在於工作樹**，入庫係零風險之補登。
⚠️ 其中 8 支係**前波之產物**（非本人所跑）⇒ 本批**只補入庫、不對其數字背書**；
其效力仍以各自報告之結論為準。

（另 `verify/out/got_F.0_*` 係 `.gitignore` 明列之 harness 重生成物 ⇒ **不入庫**，非缺漏。）

---

## 一-3 工作樹含未入庫之 harness 種子（**已查明·非「應該沒差」**）

`data/地籍資料來源_匿名版.xlsx` **確為 harness 實際輸入**：
`grep -n "ANON_XLSX = " verify/run_verification.py` →
`grep -n "build_ownership(ns, fake_st, ANON_XLSX)" verify/run_verification.py` →
`grep -n "def build_ownership" verify/selection_pipeline.py`（讀 `U_LAND`／`重劃區地籍` 兩表）。

**⇒ 段一之 `run_all` 確係以該未 commit 版本為輸入。**

**動了什麼**：

| 項 | HEAD 版 | 工作樹版 |
|---|---|---|
| 檔案大小 | 12,380,156 B | 11,482,185 B（**−898KB**）|
| zip 成員數 | 10 | 12 |
| 只在工作樹 | — | `xl/sharedStrings.xml`／`docProps/custom.xml` |
| `xl/worksheets/sheet1.xml` | 134,807,971 B | 113,721,481 B |
| `xl/theme/theme1.xml` | 10,140 B | 3,330 B |

**對 132／86／46 有無影響 ⇒ 無。已逐格證實**：

```
U_LAND      HEAD (64453, 76)  vs  WORK (64453, 76)
重劃區地籍   HEAD (53, 21)     vs  WORK (53, 21)
pandas.testing.assert_frame_equal(..., check_dtype=False, check_exact=True) ⇒ 兩表皆通過
```

⇒ 差異**全在容器層**（字串由 inline 改存 `sharedStrings` 而去重、theme／styles 置換）
——**於 Excel 重存過一次**，儲存格資料零變更。
`build_ownership` 以 `pd.read_excel` 取值、**只吃儲存格值不吃樣式** ⇒ **零影響**。

**且兩輪輸入一致**：xlsx mtime `2026-07-19 23:04` **早於**
`K8_seg3_C.log`（`2026-07-31 23:52`）與段一輪（`2026-08-03 14:04`）
⇒ §一-2 之集合比對兩側吃同一份 xlsx。

🚩 **本批不代 KL 決定是否入庫該檔**——維持上呈狀態。

### 一-3-1 附帶：本量測**正面否證**了 `W-G.4_run_all紅_working_xlsx資料阻斷_上呈.md` §三 之假說

該（**已入庫**）報告就**同一次** 07-19 異動（其載 `12,380,156 → 11,482,185`·`−897,971 B`
——與本批實測**逐位元組相同**）曾推論：

> 「modified 檔 −900KB ＋ `.tmp.driveupload/` → 高度疑 **Drive 同步遺留之部分/截斷檔**
> → **缺列/缺欄** → run_all 診斷『快照漏參』」

**該假說今可正面否證**（非「查無證據」，係**反向證實**）：

- `U_LAND` **`(64453, 76)` 兩版全等**、`重劃區地籍` **`(53, 21)` 兩版全等** ⇒ **無缺列、無缺欄**。
- 兩表 `assert_frame_equal(check_exact=True)` **雙雙通過** ⇒ **無缺值、無截斷**。
- 多出之 `xl/sharedStrings.xml` 說明縮小之真因＝**字串由 inline 改為共用字串表而去重**，
  屬 Excel 重存之正常行為，**非檔案不完整**。

⚠️ 該報告**表頭已有 KL 2026-07-21 之更正**（「本上呈誤判·勿據行動」——真因係 **F.0 過期錨**，
`362.08` 由 `0c9b7e7` 設、其後 W脫鉤／S0d 改了 G 之 W/S 輸入項 ⇒ `359.43` 為預期新值）。
⇒ **本批之量測與 KL 之裁定同向**，並補上該裁定當時未有之**正面證據**
（KL 係由「錨之沿革」判定，本批係由「資料逐格全等」判定——**兩條互相獨立之路徑、同一結論**）。

⛔ 本批**不改該報告**（其結論已由 KL 更正在案），僅於此登記交叉指認。

---

## 一-4 段一報告數字對調

**查證**：該行實際位於 `grep -n "PASS 46 支與 FAIL 86 支" docs/reports/W-G.5_K6-A2-段一_*.md`
（施工單記為 `:175`·當時屬實），與同檔 §5-1 表之 PASS 86／FAIL 46 相反。
**已更正為「PASS 86 支與 FAIL 46 支」**，並就地註明原文之誤。

---

## 一-5 GB-21 登記（**只登記不改**）

`get_min_lot_size` 之區域變數 `non_buildable`（`grep -n "non_buildable = " app.py`）
所裝者為**住宅區／商業區／甲乙丙丁種建築用地／風景區／工業區**＝**可建築**分區，
**名稱與內容相反**。條件式
`if cat not in non_buildable and cat not in HUALIEN_MIN_LOT_TABLE`
（`grep -n "if cat not in non_buildable" app.py`）**寫法正確、行為無誤**（雙重否定抵銷）。

⇒ 登記 **GB-21**：觸發＝任何人照字面讀該變數；處置＝**波末批改名**；
本批不動之由＝改名會使 `app.py` diff 混入與本批議題無關之改動、破壞「一項一 commit
各自可獨立回退」（施工單 §二 紅線 1）⇒ 須自成一次可獨立回退之 commit。
⛔ **未順手改名。**

---

## 一-6 KL 裁定入正典：正面路寬未填 ⇒ **停機要求補填**

**(a) 正典新增** `K-9-5-1`
（`grep -n "^### 🔒 K-9-5-1 " docs/rulings/K-6_街角地分配程序與可分配判準.md`），逐字載明：

- 碼面成因：`w = float(front_road_width_m or 0.0)` ＋ `if w <= upper: return`
  ⇒ `w=0` 恆中附表第一列；住宅區落 `(3.00, 12.00)`。
- **土地後果**：`min_width` `3.50 → 3.00` ⇒ `region_min` `33.10×3.50 = 115.85`
  → `33.10×3.00 = 99.30` ⇒ **½ 門檻 `57.93 → 49.65`**
  ⇒ **G 介於 `49.65〜57.93㎡` 之地主在「現金補償」與「得申請增配」之間換邊**
  ⇒ 係**權利歸屬之改變**、非顯示瑕疵 ⇒ **故不得降為警示。**

**(b) GB-20 條目已標註**：新碼分支（`k92_block_depth_check` 之 loud raise）
**已經 KL 裁定確認**；**既有消費端仍待波末批**。
⛔ 現行 loud raise **即為正解、未動**。

---

## 一-7 MinA 定義確認入正典（**確認·非變更**）

`region_min` 維持「各可建築街廓 `round(D_avg,2) × min_width` 之最小值」，**碼與正典皆未動**。
新增防混註**兩條**，落三處：

- 正典 `K-9-6-0`（`grep -n "^### 🔒 K-9-6-0 " docs/rulings/K-6_街角地分配程序與可分配判準.md`）
- 正典 §零-4 之 `region_min` 條目下（`grep -n "重劃區內最小分配面積 \`region_min\`" docs/rulings/K-6_街角地分配程序與可分配判準.md`）
- `CLAUDE.md` 之 WARNING-C 第 2 項下（`grep -n "重劃區內最小分配面積 \`region_min\`" CLAUDE.md`）

**防混一**：「最淺街廓」**≠**「最淺乘積街廓」——`min_width` 逐街廓查表，
寬不同時二者指向不同街廓、給出不同 `region_min`。
本案六街廓皆住宅區、正面路寬 8／12m **同落附表「超過七公尺至十五公尺」列**
⇒ 寬一律 `3.50`、二者同解（皆 R4）；**換案會分家**。

**防混二**：**附表深度（14.00／12.00）永不進 MinA 之乘積**。
深度項係 **N-19′ 實測平均深度**或 KL 逐街廓覆寫值
（`grep -n "_depth_use_by_blk\[_lbl\] = float" app.py`）；
附表深度**只供 K-9-2 之可建築門檻**用（K-9-6-a 同名不同量之戒）。

---

## 一-8 K-9-2 警示搬出收合面板（**有行為變更**）

**遷位前**：K-9-2 之呼叫與 `st.warning`／`st.caption` 落在
`with st.expander("⚙️ 街角地參數（共用設定 + 各街廓微調）", expanded=False)`
（`grep -n '"⚙️ 街角地參數（共用設定 + 各街廓微調）"' app.py`）**之內**。

**遷位後**：移至該 expander **之外**、`🏁 執行第 1 宗街角地優先權選位` 按鈕**之前**
（`grep -n "_k92_rows = k92_block_depth_check" app.py`）。

**落點仍合規**：街角 PK 與 Step G 配地**均在其後** ⇒ 仍為
「**BASELINE 設定完成後、開始配地之前**」。

**⛔ 判準與資料未動**：`k92_block_depth_check` 之**函式本體一字未改**；
`f3_k92_block_depth` 之**欄位與內容完全相同**。本次**只改呈現位置**。

**作用域**：`_build_blocks`／`_depth_info_by_blk`／`sb_rows_by_label` 均於 expander 主體內賦值；
Python 之 `with` **不建立作用域** ⇒ 出 expander 後仍在 `main()` 之函式作用域內可用。

**遷位確證（AST·非縮排目測）**——縮排掃描會被多行字串誤導，故以 `ast` 取包含該行之所有區塊：

```
包含 K-9-2 呼叫行之區塊（由外而內）：
  FunctionDef  def main():
  If           elif selected_tab == TAB_BLOCK_INTERACT:
  If           if temp_parcels:
  If           if not build_parcels:
🔴 仍包住 K-9-2 之 st.expander： 無 ✅
```

---

## 二、段二-0 驗收

實料：`verify/out/K6A2_seg2_0_runall.log`（`cd verify && python run_all.py`·`EXIT=1`·一般模式）

### 2-1 計數

`132 名目／86 PASS／46 FAIL` ——與段一輪、與基線輪皆同。

### 2-2 **名目集合 diff 之實際輸出行**（施工單 §三-3：不是計數）

比對**兩組**（一組不足以區辨「相對段一未變」與「相對基線未變」）：

```
$ diff <(段一輪 FAIL 名目 sort) <(段二-0輪 FAIL 名目 sort)
  (無輸出)
$ diff <(段一輪 PASS 名目 sort) <(段二-0輪 PASS 名目 sort)
  (無輸出)
$ diff <(K8_seg3_C 基線輪 FAIL 名目 sort) <(段二-0輪 FAIL 名目 sort)
  (無輸出)
$ diff <(K8_seg3_C 基線輪 PASS 名目 sort) <(段二-0輪 PASS 名目 sort)
  (無輸出)
```

⇒ **四組 diff 皆空** ⇒ PASS 86 支與 FAIL 46 支之名目集合**逐字零進零出**。
⇒ 一-8 之遷位**確為純呈現層改動**，未觸任何受閘覆蓋之行為。

### 2-3 `fixture_block_depth_n19p.py`

```
末端夾具 fixture_block_depth_n19p.py（🆕 K-8 §二 N-19′ 街廓平均深度·app 真符號 vs 裁定靶(六塊+region_min)）rc=0
```

⇒ **仍 PASS**。

### 2-4 所引之每一支 log 皆已入庫

本報告與段一報告所引之 `verify/out/*` **全數於本 commit 入庫**（清單見 §一-2-1）。
入庫後複驗：`git ls-files --error-unmatch` 對每一支皆成功（見 §二-5）。

### 2-5 ⚠️ 未入庫之工作樹髒檔（**刻意保留·非遺漏**）

| 檔 | 為何不入本批 |
|---|---|
| `data/地籍資料來源_匿名版.xlsx` | 🚩 上呈中·KL 資料·施工單 §〇-2 明令不得逕行處置（本批僅**查明其無影響**，見 §一-3）|
| `verify/out/probe_capacity_decomp.log` | mtime `2026-07-26`·**本 session 開工前即髒**、非本批所改 |
| `verify/out/probe_ruling_K4_s_origin.log`／`probe_ruling_N_e1_touch.log` | **`run_all` 自身會改寫之已入庫 log**（mtime `2026-08-03 15:14–15:15`＝本批第二輪 run_all）。二者**開工前即已與 HEAD 分歧** ⇒ 逕行 commit 會把「前 session 之既有分歧」與「本批之重跑結果」混為一談 ⇒ **本批不動、留待波末重烤批一併處理** |

📌 **附帶觀察（非阻塞·供波末批參考）**：`run_all` 會就地改寫上述兩支**已入庫**之 log
⇒ **每跑一次 `run_all`，工作樹必髒兩支**。此使「工作樹乾淨」無法作為驗收訊號。
（**只登記、不改**——改之涉 `run_all` 之輸出策略，逾本批之界。）

---

## 九、施工單與倉內實況之差異（§三-4）

| 施工單所載 | 倉內實況（`9880164` 當場 grep） | 處置 |
|---|---|---|
| 一-4 報告 `:175` | 屬實 | 照辦 |
| 一-5 `app.py:9018` `non_buildable`／`:9020` 條件 | 屬實 | 照辦 |
| 一-6 `app.py:9015`／`:9027` | 屬實 | 照辦 |
| 一-7 `app.py:16303` 深度覆寫取值 | 屬實 | 照辦 |
| 一-8 `app.py:16240` expander | 屬實 | 照辦 |
| §二 `app.py:6305` `_EPS_TOUCH_FRONT = 0.01` | 屬實 | 段二-1 用 |
| 正典 `K-6…md:343`／`:388-389` | 屬實 | 段二-1 用 |
| 一-2 「擇 (a) 或 (b)」 | **(b) 不可行**——倉內無已入庫之 86／46 靶 | 擇 **(a)** |
| 一-2 僅列 `K8_seg3_C.log` | 另有 `K8_seg3_B.log`／`K8_seg3_C_bake.log`／`K8_seg3_C_viol.csv` 同屬未入庫且被已入庫報告引用 | **同批補入**（載於一-2） |
| 一-1 僅列段一 probe log | 段一報告另引 `K6A2_seg1_runall.log`，亦未入庫 | **同批補入** |
