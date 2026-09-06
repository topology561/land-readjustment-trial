# W-G.9-244R3（段乙）　`K-9-1` **資料層**（`app.py` 單檔）　執行報告

> 🔴 **生產碼**。本 commit **⛔ 推主線**——依改版單 `§五 f`：獨立 commit → 推側分支
> `verify/W-G.9-244-c1` → 發單側逐位復驗 → 復驗全綠後由發單側呈 KL 裁放行。
> 🔒 **只動 `app.py` 一檔**；其餘九檔逐位不變（`V-C`）。
> 🛑 **⛔ 接任何閘、⛔ 動 `verify/**`、⛔ 實作 `r2`、⛔ 動 `get_min_lot_size`**（`§五 d`·逐項給證於 §六）。

---

## §零　態錨

| 項 | 值 |
|---|---|
| 段甲′ 之終態（本段之父）| `ffb05446dff09bb92233d5809bd74f18da87b49a`（已 push 主線）|
| `app.py` 改前 `sha256` | `e3e464ea2493d0461b629941280c55238633cc57573d0837363d60eb3c85b7ca` |
| `app.py` 改後 `sha256` | `ad7a91dba08119f5…`（全值見 `V-C`）|
| `git diff --stat` | **`app.py` 單檔·110 增／6 刪** |
| `py_compile` | `rc = 0` ✅ |

---

## §一　落地（`§五 a`／`b`／`c`）

### `a`　三個 module 級純函式 ＋ 三個常數（置於 `HUALIEN_MIN_LOT_TABLE` 之後、`get_min_lot_size` 之前）

```
K91_SS_MBA_BY_CATEGORY = 'f3_min_build_area_by_category'
K91_SS_MBA_BY_LABEL    = 'f3_min_build_area_by_label'
K91_SS_MBA_EFFECTIVE   = 'f3_min_build_area_effective_by_label'

def k91_effective_min_build_area(label, category, by_label, by_category)   # ⑨ 裁丙之階梯
def k91_min_alloc_contrib_by_blk(min_alloc_area_by_blk, eff_min_build_by_blk)  # ⑧ 之逐街廓貢獻
```

🔒 **鍵名⛔ 自創**：`f3_min_build_area_by_label` 係**倉內自有提案名**
（`docs/specs/W-G.5_裁定N_乙案_plan_v1.md:204` 逐字「**純加性**·不動既有鍵」；
本批施工前現查 `git grep -- "*.py"` 命中 **0**）。
🔒 **module 級**之故 ＝ `app_harvest._filter_module` 保留 `_KEEP_TOP`（含 `FunctionDef`）
⇒ **`harvest()` 可取** ⇒ 單元對拍得測**真函式**、⛔ 抄本（`-243 V-2` 之工法）。

### `b`　UI（三段·置於既有逐街廓參數介面內）

分區底表（逐使用分區·**清單取自 `_build_blocks` 之實際 `category` 集合**·⛔ 硬編）／
逐街廓覆寫欄（預設 `0`）／**各街廓有效值之目檢表**（街廓・使用分區・分區底・街廓覆寫・有效值・規定?・畸零地寬×平均深度）。
資料源標示 ＝ **都市計畫書**（expander 標題與 caption 皆載）。

### `c`　`MinA` 新式之接算

於 `_min_alloc_area_by_blk` 匯總處：
`_k91_contrib = k91_min_alloc_contrib_by_blk(_min_alloc_area_by_blk, _k91_eff)` →
`_valid_mins = list(_k91_contrib.values())` → `_region_min = min(...)`；
`argmin_blk` 改自 `_k91_contrib.items()` 取，以與 `_region_min` **同源**。

---

## §二　`V-A`　預設迴歸（**照單跑·惟其空係<u>構造性</u>·零鑑別力**）

| 項 | 值 |
|---|---|
| 工法 | 拋棄式 clone 內 `python verify/run_verification.py`；改前／改後各一次；收 `verify/out/got_*`（`.gitignore` 已涵蓋·倉態零污染）|
| 產出 | 二次皆 **6** 檔（`診斷`／`指配`／`抵費地` × 退縮 `0m`／`3.5m`）|
| 結果 | `diff -r pre post` ⇒ **`rc=0`·輸出 `0` 列** ⇒ **逐位相同** |

🛑 **本報告⛔ 以此為「無迴歸」之證據**，理由逐字：

1. **改動全在 `main()` 內**（`app.py` 之 `def main():` 起 `:14635`；三個 hunk 之二在其內），
   而 `app_harvest.harvest()`（`verify/app_harvest.py:128`–`141`）只 `exec` **`_filter_module` 過濾後之頂層定義**，
   **⛔ 呼叫 `main()`**。倉內二 fixture 逐字自證：
   `verify/fixture_klui_t2diag.py:10`–`11`「`run_all` 所掛 `21` 項中，其 `got` 端經 `app.py:main()` 產生者 ＝ **`0`**」；
   `verify/fixture_n14_feed_chain.py:7`–`9`「**`main()` 內之敘述從不被 `run_all` 執行**」。
2. ⇒ **該 diff 必然為空**，其空**⛔ 有任何鑑別力**（`-241 §二 c` 所警示之「退化案例無鑑別力」）。
3. 🔴 **併記**：`got_G值_退縮*.csv` 等 **Step G 自身之 dump**（`run_verification.py:672`–`:674`）
   **根本未產出**——Step G 於 `R2` 即 raise（`GB-67`／telescoping）；
   所收之 `6` 檔係 `:602`–`:604` 所產、**在 Step G <u>之前</u>**。
   ⇒ 單 `§五 e` 之「Step G 輸出可得」一語**於現態不成立**（**候裁**）。

🔒 **真正之鑑別力由 `V-D` 承擔**（見 §三）。

---

## §三　`V-D`　單元對拍（`§五 c` 所令 ＋ `常規五` 兩造對照組）✅ **GREEN**

🔒 **工法（兩端皆⛔ 抄本）**：
**舊式**自 `blob@845d08d` 之 `app.py` **逐字抽出**該三段運算式（`:19783`／`:19784`／`:19792`–`:19794`）再 `eval`；
**新式**經 `app_harvest.harvest()` 取**真函式**（`harvest stats kept=272`）。

| 檢 | 判準 | 實測 |
|---|---|---|
| ① **正對照** | 規定集為空（`{}`／全 `0.0`／全 `int 0`／`None` 四形）⇒ `_valid_mins`／`_region_min`／`argmin_blk` **逐位相同**（含元素型別）| **對拍 24 筆／不符 `0`** ✅ |
| ② **負對照** | 規定集非空 ⇒ 輸出**必須**改變（證非恆綠）| **3** 案確實改變 ✅（含一例 `region_min` 不動而 **`argmin` `R2`→`R6`**）|
| ③ 有效值階梯（⑨ 裁丙）| 覆寫`>0` → 分區底`>0` → `0`；鍵不存在／分區不符 ⇒ `0` | **5/5** ✅ |
| ④ widget 生命週期 | `value=` 之種**取自持久 dict**（須 `2`）·**⛔ 取自 widget key**（須 `0`）| `0` ／ `2`（`:19848`／`:19857`）✅ |
| ④ 之判別力自證 | 同檔既有之**深度覆寫欄**仍自 widget key 取種 ⇒ 本檢**非恆綠** | 命中 **1** ✅ |

**案例母體**：`UC9898-ish 六塊`（含**二對並列**）／含 `None`（`min_width ≤ 0`）／含 `0`／單塊／全 `None`／空。

---

## §四　🩸 反駁式審查所捕之缺陷與其修正（**⛔ 隱去**）

本批於出艙前跑一次**四視角反駁式審查 ＋ 逐項 judge 復核**（`8` agents·`0` error·`251` tool uses）。
judge 判為 **real** 者 **6** 則、判為 **not real** 者 **4** 則（後者含「⛔ 接任何閘被違反」「stale key 累積」
「app 側 MinA 與引擎分歧」「⑧ 邊角」——皆因觸發條件不可達或與改前同）。
**中心主張（規定集為空 ⇒ 逐位相同）於三個獨立 lens 各以 20 萬〜30 萬次差分測試<u>未被推翻</u>。**

### 🔴 已修一：**Streamlit widget 生命週期致使用者輸入被靜默清零**（serious）

- **機制**：`value=` 之種原取自 **widget key**（`f3L_mba_cat_{cat}`／`f3L_mba_ov_{lbl}`），
  而**分支未渲染之輪 Streamlit 丟棄 widget key、持久鍵存活**
  ⇒ 回渲染時 widget 顯 `0`，並以 `0` **覆寫**持久 dict、再寫回 session_state。
- **後果（審查方以 `streamlit.testing.v1.AppTest` 於 Streamlit `1.56.0` <u>活體重現</u>·二個 lens 各一次）**：
  都市計畫書所填之值**永久遺失且無警告**；`_k91_eff` 退化為全 `0`
  ⇒ `_region_min`／`f3_70a['pass']` 靜默回退，`§7-0a` 之紅色橫幅消失。
- 🩸 **此係本倉<u>已付學費</u>之同一機制**（`W-G.9-219R`／`-226` `G4`）——CC 明知而重踩。
- **修**：`value=` 之種改**取自持久 dict**（`_k91_by_cat.get(...)`／`_k91_by_lbl.get(...)`），
  並於碼內逐字註明理由與先例。機驗：自 widget key 取種者 **`0`**、自持久 dict 取種者 **`2`**。

### 🔴 已修二：`argmin_blk` 之 caption 失真（nit·但係本改動所致）

`argmin_blk` 現可能係**依規定值**選出之街廓，而二處 caption 仍逐字印「**最淺乘積街廓**」
（`app.py` 之 `§7-0a` PASS caption ＋ 步驟診斷表）⇒ 改為「**MinA 來源街廓**」。
機驗：`最淺乘積街廓` 殘留 **`0`**／`MinA 來源街廓` **`2`**。

### 🔴 已修三：`k91_region_min_alloc_area` **建置未接線**（minor）

全倉 `grep` 呼叫點 **`0`**（僅其 `def` 自身）⇒ 依本倉對「建置未接線」之一貫紅判**逕刪**。
機驗：殘留 **`0`**；單元對拍加一 `assert "k91_region_min_alloc_area" not in ns`。

### 🔴 已修四：UI caption 之「尚未接任何閘」不精確

`_k91_eff` 同一輪即入 `§7-0a` 之 `_region_min`。二 judge 對「是否構成接閘」**判定相左**
（一方指 `§7-0a` **零強制消費端**——僅 `st.error`／`st.caption`，無 `raise`／`return`／短路）。
⇒ caption 改為載明實情：「其值已入 `§7-0a` 之全區 `MinA`（**僅顯示**，該檢無任何強制消費端），
**尚未接任何分配之閘**（⑩⑪ 之驗另批）」。機驗：`尚未接任何閘` 殘留 **`0`**。

### 🔴 未修·**具名為已知失效**：`GB-144` `G2` 之現態命中集

本改動使該節 `現態命中集@d2d3692` 之 **13 個 `app.py:NNN` 錨全部位移**
（`< 19774` 者 `+46`、其後者 `+104`；逐點內容比對確認舊行號現皆為無關文字）。
🛑 依 `-228` 之維護義務「每次位移須**新增**一列（⛔ 改舊列），**未新增 ＝ 已知失效須具名**」
——**新行號須待本段併入主線後方穩定** ⇒ **本批具名為已知失效**，
**併線批必辦**：於 `GB-144` 節末新增一列 `現態命中集@<併線後之 commit>`。

---

## §五　`V-B`　diff 逐行人閱

`git diff --stat` ＝ **`app.py` 單檔·110 增／6 刪**；三個 hunk：

| hunk | 增／刪 | 內容 |
|---|---|---|
| `@@ HUALIEN_MIN_LOT_TABLE 之後 @@` | ＋常數 3 ／函式 2 | 三常數 ＋ `k91_effective_min_build_area` ＋ `k91_min_alloc_contrib_by_blk` |
| `@@ 逐街廓深度覆寫迴圈之後 @@` | ＋ UI expander | 分區底表／逐街廓覆寫／有效值目檢表 ＋ 三 session 鍵之寫回 |
| `@@ §7-0a 匯總處 @@` | ＋4／−4 | `_k91_contrib` → `_valid_mins`／`_region_min`；`argmin_blk` 改自 `_k91_contrib.items()`；二 caption 之措辭 |

🔒 **刪除之 6 列**逐行具名：舊 `_valid_mins` 生成式 **1** 列／舊 `argmin_blk` 三元式 **3** 列／
二處 caption 之 `最淺乘積街廓` 各 **1** 列。**⛔ 有任何算式被刪而未以等價物取代。**

---

## §六　`V-C` ＋ `§五 d` 之逐項給證

**`V-C` 十檔雜湊前 16 位**

| 檔 | 改前 | 改後 | 判 |
|---|---|---|---|
| **`app.py`** | `e3e464ea2493d046` | **`ad7a91dba08119f5`** | 🔴 唯一得變者 |
| `verify/wf_f0.py` | `6758ea766b001b95` | 同左 | ✅ |
| `verify/wf_f1.py` | `30e19048dfd781bc` | 同左 | ✅ |
| `verify/wf_f2.py` | `f974724d7e694ad7` | 同左 | ✅ |
| `verify/wf_f3.py` | `226c7c5fa00464f3` | 同左 | ✅ |
| `verify/wf_f4.py` | `b36aeca6c4f6b364` | 同左 | ✅ |
| `verify/selection_pipeline.py` | `6c6783420dbc635c` | 同左 | ✅ |
| `verify/run_verification.py` | `e48f24c84079f365` | 同左 | ✅ |
| `verify/stepg_pipeline.py` | `0260273350021311` | 同左 | ✅ |
| `verify/run_all.py` | `4ba89fef90979491` | 同左 | ✅ |

**`§五 d`（⛔ 動者）之逐項**

| 禁令 | 給證 |
|---|---|
| `verify/**` 一字不動 | `git diff --numstat` **僅 `app.py`** |
| ⛔ 接任何閘 | `§7-0a` 之 `f3_70a` **零強制消費端**（僅 `st.error`／`st.caption`；`'pass'` 只用於選字串）；本批⛔ 新增任何 `raise`／`return`／短路 |
| ⛔ 實作 `r2` | 本批⛔ 有任何排序／級距碼；`_SORT_KEYS` 一字未動 |
| ⛔ 動 `get_min_lot_size` | 該函式在 diff 中僅為**上下文列**（新碼插於其**前**）|

---

## §七　🔴 上呈（**⛔ 由 CC 自裁**）

1. **UI 掛載點偏離單之逐字**（單 `§五 a-2`：「正面路寬所在處」）——實掛於**深度覆寫所在之逐街廓介面**。
   理由已於碼內註解具名：前者在 `st.form` 內（`submit_road = st.form_submit_button("✅ 儲存路寬資料")`）
   ⇒ **須按鈕方生效**，且以 `bid` 為鍵；本欄之消費端以 **label** 為鍵且需即時生效。
   審查亦獨立指出此偏離（judge 判 real·minor·「plan deviation, not a runtime bug」）。**候裁。**
2. **`V-A` 之空係構造性、零鑑別力**（§二）；且單所稱「Step G 輸出可得」於現態不成立。
   **是否須另立可鑑別之驗收 ＝ 意思決定。**
3. **`GB-144` `G2` 現態命中集已知失效**（§四末）——併線批必辦。
4. **`GB-143` 計數器**：本波 CC **四度**誤送 heredoc（皆未被攔·後果實測為零）；計數器現 `3`。**是否計入 ＝ 意思決定。**

---

## §八　⛔ 未辦

- **⛔ 推主線**——本 commit 只推側分支 `verify/W-G.9-244-c1`；`wip/s1-endpart` **一字不動**。
- **⛔ 接任何閘、⛔ 動 `verify/**`、⛔ 實作 `r2`／五級／驗證站**。
- **⛔ 於本批修 `GB-144` 之現態命中集**（新行號未穩定·已具名為已知失效）。
- **⛔ 以段甲已綠為由自行併線**（改版單 `§五 f` 明文）。
