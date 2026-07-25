# W-G.5 裁定 N — 偵察報告（**只量不改引擎**）

> **基準**：`HEAD == origin/wip/s1-endpart == 25342cd`（本批**未動引擎碼**）。
> **產出**：唯讀零注入探針 `verify/probes/probe_ruling_N_recon.py`
> ＋ `verify/out/probe_ruling_N_recon.log`／`.csv`。
> **規格本體**：`docs/specs/W-G.5_裁定N_分配起算點.md`。
> **行號紀律**：本檔一律**符號名＋可自癒 grep**；非用行號不可者同列記其成立之 commit。

---

## 〇、一句話

**近端起算點（s=0）與遠端起算點（真頂點）不同源，而池鋪滿又用真 `s_min`**——
三者不對稱使 `s<0` 之街廓片被鋪成**合法池片、帳面全綠、卻永遠沒人配得到**。
六塊實測**完整無例外**：唯二 `s_min<0` 者（R1／R6）恰為唯二有殘留楔形者，且**楔形 s 寬 ≡ |s_min|**。

---

## 一、§4.1-1　s 域／超界面積（六塊 × 兩情境）

**與交接文 §3.1（claude.ai 異機實測）逐字對照 ⇒ 全等·無停機。**

| 街廓 | s 域（本批實測） | §3.1 | 近端 `block∩{s<0}` | §3.1 楔形 | 對照 |
|---|---|---|---|---|---|
| R1 | [−0.3248, 87.7155] | 同 | **5.3255** | 5.3255 | ✅ |
| R2 | [+0.2677, 100.0274] | 同 | 0.0000 | 無 | ✅ |
| R3 | [−0.0000, 96.8032] | 同 | 0.0001 | 無 | ✅（≈0） |
| R4 | [+0.1759, 98.7170] | 同 | 0.0000 | 無 | ✅ |
| R5 | [+0.2685, 92.7995] | 同 | 0.0000 | 無 | ✅ |
| R6 | [−3.6068, 85.8549] | 同 | **85.7064** | 85.7064 | ✅ |

### 1.1 本批新增之三項事實

1. **s 域為純幾何量**：0m／3.5m **逐位相同**（探針明檢，輸出 `差異塊：（無）`）。
   ⇒ 交接文 §4.1-1 所求「兩情境」在 s 域上**不可能有差**，差異只可能出現在
   forced 與分配結果（本表已含 forced 欄）。
2. **遠端超界面積**（`block∩{s>s(p2)}`，本批新增欄）：R3 **75.7782㎡**、R1 6.5961㎡，餘為 0。
   該量**已由 step 0 `_oblique_s_max` 納入分配範圍**（分配上界＝`s_max`、非 `s(p2)`）⇒ **非漏配**。
   ⚠️ 與交接文 §3.1 附註所引 **78.24** 不等——**定義不同**（本欄嚴格為 `block∩{s>s(p2)}`）。
   依「交辦文與倉態不一致時照倉態走、標旗上呈、不自行調和」，**僅載明差異、不調和**。
3. **forced 分布**（解釋 §3.3 之覆蓋率洞）：

| 塊 | L forced 0m／3.5m | R forced 0m／3.5m | L 側街 | R 側街 |
|---|---|---|---|---|
| R1 | 否／否 | 否／否 | 有 | 有 |
| R2 | 否／**是** | 否／否 | 有 | 無 |
| R3 | 否／否 | 否／**是** | **無** | 有 |
| R4 | 否／否 | 否／否 | 有 | 有 |
| R5 | 否／**是** | 否／否 | 有 | 無 |
| R6 | 否／否 | 否／否 | **無** | 有 |

⚠️ **forced 欄之時序口徑（勿誤讀）**：上表 forced 取自 `run_corner_pk` 回傳之旗標＝**PK 階段態**。
**裁定 M 之 M-5 物化在其後**，會把部分 forced 端補足成**真 winner** ⇒ 終態 forced 更少
（本批 `run_all` 實見：`[M-5·3.5m] 物化：1 端街角補足`、`③ R3right：餘額 90.68㎡ 併入街角地 628-45(2)`
⇒ R3 右之 308.93 forced 帶於終態已不存在）。
**對 §3.2 之結論無影響**：M-5 只**解除**forced、不新增，故「R1／R6 兩情境左端皆非 forced」
於 PK 階段與終態**皆成立**。

**非分配街廓**（無 FRONT_LINE·不適用本裁定，明列非靜默跳過）：
`G1(鄰里公園)`／`RD1`–`RD4`(道路)。

---

## 二、§4.1-2　試算：左端改自 `s_min` 起算

口徑＝N-2「該宗 G 不變·以真幾何面積迭代」：左組逐宗沿用現行 G 目標，改自 `s_min` 起算、
以治理碼 `_block_strip` bisect 解各宗 S（**禁自行複刻切線式**·#20）。

| 塊 | 情境 | 楔形㎡ | 左組宗數 | 首宗 ΔS | **左組末宗前移量** | 左側街 |
|---|---|---|---|---|---|---|
| R1 | 0m | 5.3255 | 2 | +0.1687 | **−0.1538 m** | 有 🚩 |
| R1 | 3.5m | 5.3255 | 1 | +0.1686 | **−0.1562 m** | 有 🚩 |
| R3 | 0m／3.5m | 0.0001 | 7 | −0.0033 | **−0.0072 m** | 無 |
| R6 | 0m／3.5m | 85.7064 | 6 | +0.8977 | **−1.8621 m** | 無 |

**共通結構**：
- 前移量**全為負**（往近端縮）⇒ 遠端騰出等量空間、後續宗不被擠爆。
- **池片數 2 → 1**：楔形不再是孤立片，中央池整體前移等量。
- 逐宗明細見 `verify/out/probe_ruling_N_recon.log` §4.1-2 段與 `.csv`。

### 2.1 🚩 一階近似之殘留（**誠實載明**）

本試算**固定 G 目標**。R1 左**有側街** ⇒ 其 W 隨界線位置變動 ⇒ `Rw` ⇒ **G 可能微調**
（canonical solo G **位置相依**·W-F E2 已載）。故：

- **R3／R6**：左側街「無」⇒ 無側街負擔 ⇒ 不經 W 耦合 ⇒ **試算對該二塊精確**。
- **R1**：🚩 **G-W 耦合殘留·須引擎實跑定案**。本批**不猜耦合量**。

### 2.2 🚩 R6 首宗全落於楔形內（**上呈項·見 §五 Q1**）

R6 首宗 `628(2)` G 目標僅 **7.37㎡**，楔形達 **85.71㎡**。自 `s_min=−3.6068` 起算後
該宗迄 s ＝ **−2.5491**（仍為負）⇒ **整筆落在原「未臨正街」區內**；楔形實由**前 2 宗跨越**，
非由「最邊側該宗」單筆吸收。與 N-2 字面「納入**最邊側該宗**」（單數）存在**量級張力**。

---

## 三、§4.1-3　守恆自檢

| 項 | 結果 | 判 |
|---|---|---|
| ΣG（左組）舊 vs 新 | **逐塊逐情境全等** | ✅ |
| 池總量 | 差 **±0.01～0.03㎡** | ✅ ＝ 原「幾何面積 vs G」2dp 捨入殘差（**舊值本就有**·非本裁定所生） |
| bisect 可行性 | **6/6（塊×情境）全可行** | ✅ 無「吃到 s_max 仍不足」 |
| 前移方向 | **全負** | ✅ 遠端恆有餘裕 |

### 3.1 ⚠️ 舉證力聲明（**禁自我加碼**）

ΣG 守恆在本試算中**部分為構造性**：N-2 明定「該宗 G 不變」，我即以其 G 為 bisect 靶，
故 `ΣG 不變` 與 `池總量 = 街廓 − ΣG` **近乎恆真**（＝零舉證力·#21 恆真閘教訓）。

**真正被檢驗**者為三項**非恆真**命題：
① 各宗 bisect 在 `[s_min, s_max]` 內**有解**；② 前移量**恆負**；③ **池片數 2→1**。
守恆之終局證明**須待引擎實跑 ＋ `run_all`**——本批不宣稱已證。

---

## 四、§4.1-4　`s` 起算點家族**全點清查**

判準：該點是否決定「分配推進之近端起算」。

### (A) 🔴 N-1 應改——分配 s 原點寫死 FRONT p1

| # | 位置（符號名） | 查法 | 語意 |
|---|---|---|---|
| A1 | `app.py`（Step G 路徑）`corner_pt = _np_d.array(_p1_fl,…)` | `grep -n "corner_pt = _np_d.array(_p1_fl" app.py` | 分配 s 原點 |
| A2 | `verify/stepg_pipeline.py` 同式 | `grep -n "corner_pt = _np_d.array(_p1_fl" verify/stepg_pipeline.py` | headless 同構 |
| A3 | `verify/wf_f1.py` `corner_pt = p1.copy()` | `grep -n "corner_pt = p1.copy()" verify/wf_f1.py` | F.1 幾何原語（硬釘 R1） |
| A4 | `verify/wf_f4.py` E3 `corner = p1.copy()`（left 支） | `grep -n "corner = p1.copy()" verify/wf_f4.py` | E3 重鋪原點 |

### (A′) 🔴 同一缺陷之消費端——左組自 `buffer`（無 forced ⇒ 0）起推

| # | 位置 | 查法 | 語意 |
|---|---|---|---|
| A′1 | `app.py`／`stepg` `left_cum_S = float(_left_buffer_S)` | `grep -rn "left_cum_S = float(_left_buffer_S)" --include=*.py .` | 左組起始累積 S |
| A′2 | `app.py`／`stepg` `baseline_pt = corner_pt + left_cum_S * d_hat` | `grep -rn "baseline_pt = (corner_pt + left_cum_S" --include=*.py .` | 首宗切帶起點 |
| A′3 | `wf_f4` `strip_at`：`corner + (buf + cum_S) * dh` | `grep -n "corner + (buf + cum_S)" verify/wf_f4.py` | E3 重鋪 |
| A′4 | `wf_f1` `strip_at`：`corner_pt + (left_buffer_S + cum_S) * d_hat` | `grep -n "corner_pt + (left_buffer_S + cum_S)" verify/wf_f1.py` | F.1 重鋪 |

### (B) 🟡 主動夾 0

| # | 位置 | 查法 | 語意 |
|---|---|---|---|
| B1 | `_corner_buffer_S`：`_lo = max(s_min, 0.0)` ＋ loud 黃字 | `grep -n "左帶下界夾 0" app.py` | 左帶下界夾 0。N-1 下 `_lo` 應為 `s_min` ⇒ 該夾與黃字一併廢 |

⚠️ **B1 之上界語意與本題無關**：同函式 `side='left'` 之帶上界＝`buf`（絕對 s 上界）、
`side='right'` 之 `buf`＝自 `s_max` 起之寬——**兩側刻意不對稱**、與消費端逐位對映（BLOCKED-1）。
**改 `_lo` 不得順手動上界**。

### (C) ✅ 已正確——遠端真頂點（N-1 明示不動）

`_oblique_s_max`：**1 個定義 ＋ 9 個呼叫點**
（`grep -rn "_oblique_s_max" --include=*.py .`：`app` ×3、`stepg` ×3、`wf_f4` ×1、
`selection_pipeline` ×1、`run_verification` ×1；後三者走 `ns["_oblique_s_max"](` 形）。

🔴 **行號衛生瑕疵（本批發現·未修）**：`_oblique_s_max` 之 docstring 自稱
「stepg（577＋外層 W₀ end_pt）／app（15499）／wf_f4（1124）**四處**」——
**行號與家數皆與 `25342cd` 倉態不符**（實為上列 9 處）。屬活碼註解內之過期行號錨。
**本批不改碼**（只量不改），列入 plan 波 backlog。

### (D) ✅ 已用真 `s_min`——**非缺陷·正是不對稱之另一半**

| # | 位置 | 查法 | 語意 |
|---|---|---|---|
| D1 | `_pool_strips_for_block`：`cur = s_min` | `grep -n "cur = s_min" app.py` | 池補區間自**真** s 域下界起 ⇒ 楔形被鋪成合法池片 |
| D2 | `wf_f4` 末端 gate `_unfront_area` 用 `_smin0` | `grep -n "_unfront_area = " verify/wf_f4.py` | cond2。N 下語意須重定義（§五 Q3） |

### (E) ⚪ 下游連動（隨 N-1 變動·非獨立缺陷）

| # | 位置 | 查法 | 說明 |
|---|---|---|---|
| E1 | `_place_pool_parcels` 池窗 `[cum_left, s_max_blk − cum_right]` | `grep -n "def _place_pool_parcels" -A 40 app.py` | 階段2 落位窗隨 `cum_left` 連動 |
| E2 | PK「假設第 1 宗」真 G 之**呼叫鏈**：`_corner_block_true_G(corner_pt=p1, s_max_left=…, s_max_right=…)` → 內呼 `_corner_first_lot_G` | 生產端 **2 處**：`grep -rn "_corner_block_true_G(\|_corner_block_true_G\"\]" --include=*.py .`（`app.py` ×1、`verify/selection_pipeline.py` ×1）。`_corner_first_lot_G` 本身 5 處，其中 **2 處在 `_corner_block_true_G` 內**、另 3 處為 `run_verification`／probe／test | PK 資格閘。**左端 baseline 亦為 p1**、且 `s_max_left` ＝ `S_block_max`（FRONT 長·**非** oblique·reviewer B-6「左右不同源」）⇒ N-1 下二者皆須重定義 ⇒ **街角 winner 可能翻盤** ⇒ §五 Q2 |
| E3 | `_end_region_R(end_pt=…)`／`_endpt = p1 if side=="left"` | `grep -n "_endpt = p1 if side" verify/wf_f4.py` | 末端帶錨點（§五 Q3） |

---

## 五、🔴 上呈 KL（**本批不自決·未裁不得施工**）

| # | 題 | 為何須裁 |
|---|---|---|
| **Q1** | **楔形大於最邊側該宗全部 G 時，如何解 N-2？** | R6 楔形 85.71㎡ ≫ 首宗 G 7.37㎡；純移起算點之結果是楔形被**前 2 宗跨越**，非「納入最邊側該宗」單筆。且 7.37㎡ 之宗幾必不合最小分配面積 ⇒ **N-3 遞補立即觸發**。二者交互須裁 |
| **Q2** | **PK 資格之「假設第 1 宗」是否同步改自 `s_min` 起算？** | `_corner_first_lot_G` 左端 baseline 亦為 p1。若同步改，**街角 winner 可能翻盤**（裁定 M 之 T1 已證該閘刀口薄，最薄餘裕 +0.84㎡）⇒ 波及 forced 端與 918.50㎡ 之歸屬 |
| **Q3** | **`_unfront_area` 之 gate 角色**（交接文 §六(c)） | N 下近端「未臨正街」恆被納入分配 ⇒ 該面積是否恆為 0？若是，末端 gate cond2 失去判別力、角色須重新定義 |
| **Q4** | **N0-20 末端機制與 N-4 之衝突**（交接文 §六(a)） | 補丁九 裁 2 把 `s_min<0` 段路由給 §4 N0-20 之 `R_end`（winner-take-all·**條件**決定）；N-4 說歸「左邊第 1 宗」（**位置**決定）。兩者不同判準 |
| **Q5** | **左組為空（k\*=0）之塊如何處置？** | 探針已備該分支之 loud 標記。本案六塊未觸發，但泛用化（N-5）下必須有解——左組空時近端楔形無「左邊第 1 宗」可歸 |

---

## 六、交互影響清單（**只列不處置**·交接文 §六原題 ＋ 本批補充）

| # | 項目 | 標記 | 本批實測補充 |
|---|---|---|---|
| (a) | N0-20 末端機制 vs N-4 | **須 KL 裁** | 見 §五 Q4 |
| (b) | F-1 錨 85.706㎡ | **須 KL 裁**（語意改變·不可只重烤） | 本批實測 R6 `block∩{s<0}` ＝ **85.7064**，與該錨同值 ⇒ 確認該錨即「R6 左未臨正街面積」 |
| (c) | `_unfront_area` gate 角色 | **須 KL 裁** | 見 §五 Q3 |
| (d) | BK-5「楔形與標的不相鄰」守衛 | **須 KL 裁**·勿逕刪 | ⚠️ **實為兩處**（`wf_f4` E3 ＋ `wf_f1`），交接文 §六(d) 僅列 `wf_f4`。處置時勿漏 |
| (e) | F.0→F.4 級聯（F.1 專司楔形補救） | **須 KL 裁** | 機制(B) 既廢（N-6），F.1 角色須重新定位 |
| (f) | W 量測基準是否連動 | **純技術·待 plan 波確認** | R3／R6 左無側街 ⇒ 該二塊 W 不受影響；**R1 左有側街 ⇒ 受影響**（§2.1 🚩） |
| (g) | `_oblique_s_max` docstring 過期行號錨 | **純技術** | 自稱「四處」實為 9 處、行號與 `25342cd` 不符。列 plan 波 backlog |

---

## 七、倉態與清點建議（**本批未動**）

- `HEAD == origin/wip/s1-endpart == 25342cd`
- `data/地籍資料來源_匿名版.xlsx` 未 commit 異動 ＝ **既有 🚩·本批未動未 commit**
- 本批新增：`verify/probes/probe_ruling_N_recon.py`、`verify/out/probe_ruling_N_recon.log`／`.csv`、
  `verify/out/N_recon_run.log`、本報告、`docs/specs/W-G.5_裁定N_分配起算點.md`
- 既存 untracked（`.agents/`、`.codex/`、`AGENTS.md`、`data/r3.dxf`、`.tmp.driveupload/`、
  大量 `verify/out/*.log`）**本批未動**。建議：`.tmp.driveupload/` 與 `.agents/`／`.codex/`
  若為工具暫存應入 `.gitignore`；`data/r3.dxf` 須 KL 確認來源後再定去留。**本批不自決。**

---

## 八、本批自身之教訓（記帳）

**「紅著卻報綠」我自己重演了一次**：首跑探針以
`python probe.py > log 2>&1; echo "EXIT=$?"` 收尾——**背景任務回報 exit 0，實則 python traceback**
（複合指令之退出碼取自最後的 `echo`）。已改為顯式 `rc=$?; …; exit $rc`。
⇒ 交接文 §8.1 之形狀「出事了，但退出碼／顯示層說沒事」**不限於引擎碼，工具鏈同樣會犯**。

另二錯（皆已修）：①誤把 `run_step_g` 當三元組解包（實回 dict，三元組者為 `build_step_g_tables`）——
已加**回傳型別 loud 檢查**而非靜默適配；②首版對無 FRONT_LINE 之街廓直接 loud 停——
改為**明列跳過清單**（`G1`／`RD1-4`）而非靜默跳過。

---

## 九、⛔ 凍結標記（已置）

`P-H 重烤全面凍結` 標記已置於三處：
`docs/reports/W-G.4_裁定M_重錨登記.md` §五／
`docs/reports/W-G.4_裁定M_PH前置_f4逐格歸因表.md`／
`docs/specs/W-G.4_裁定M_plan_v4.md` §八。

`docs/W-D.4_域裁鎖定.md` 裁示 2 機制(B) 已標作廢（**原文保留**）；
補丁九 裁 2 之 N0-20 路由已標記由裁定 N 取代。
