# W-G.9-247　驗證站之**量測基建**（harness 三件）＋ 自誤 `301`／`302`

> 🔴 **生產碼（harness 側·`verify/` 二檔）**：`verify/stepg_pipeline.py` ＋ `verify/run_verification.py`。**⛔ 動 `app.py`**、⛔ 動 `verify/` 其他檔。
> **零土地後果**：本批不動任何配地計算；只讓 harness (1) 中止時把已算完的逐宗表**存下來**、(2) 把**街角規定範圍**送進 harness 上下文、(3) 把**最小建築面積有效值**送進 harness 上下文。
> 🛑 **序**：本單**先於** `-246` 之續辦（二者同動 `stepg_pipeline.py`）；`-246` 續辦須在本單併線後之主線上施工。
> 段甲（工項零／四）零生產碼逕推；段乙（工項一–三）一 commit → 側分支 `verify/W-G.9-247-c1`，候發單側復驗、KL 放行。

---

## §零　開工閘（缺一即停）

**`S-0`**　最末 `SELF_SHA256` 依既有口徑重算。**`S-0b`** 依現行判別力款。

**`S-1`（宣告框·三數分列·補款 `⑤⑥`）**　發單側於 `blob@a313ebdde623e0f0f08d2f9c1b278e50ecca3029`／全 `docs/` **571** 檔（`19` 二進位）：

| 號 | `D1` | `D2` | `D3` | 宣告框 | 鬆框 | 角色 |
|---|---|---|---|---|---|---|
| **`W-G.9-247`** | 0 | 0 | 0 | **0／0** | 1／1 | ✅ 未占用 |
| `W-G.9-246` | 2 | 2 | 0 | 2／2 | 3／9 | 對照甲 ✅ |
| `W-G.9-248` | 0 | 0 | 0 | 0／0 | 0／0 | 對照乙 ✅ |

**`S-3`**　十檔同 `a313ebd`（`app.py ad7a91dba08119f5`／`run_verification.py e48f24c84079f365`／`stepg_pipeline.py 0260273350021311`／餘同前）。**本批只得動後二者**；餘八檔前後逐位不變。

---

## §一　工項零：本單原封入倉

`docs/orders/W-G.9-247_驗證站量測基建_harness三件.md`。

---

## §二　工項一：**中止時之部分落檔**（`g_rows` 例外安全）

### 案由（`-246R` 發現一·發單側復現）

`run_verification.py:667` `try: _sg = run_step_g(...)` → `:672` `_dump_csv(g_tab, …)` → `:696` `except RuntimeError`。
`run_step_g` 內有 **27** 個 `raise RuntimeError`（結構閘）；`R2` 一 raise，`:672` 永不執行 ⇒ `R1` 已算完之逐宗表**全丟**。
`-241R` 已證二情境皆於 `R2` 中止（`0m` ＝ `GB-67` ②-宗圍堵閘／`3.5m` ＝ telescoping）。

### 施工（⛔ 改 pass 路徑一字·⛔ 改 `results` 列）

1. **`stepg_pipeline.py`**：`run_step_g` 之本體以一層 `try/except RuntimeError as e` 包住（**只包、不吞**）：於 `e` 上掛
   `e.partial ＝ {'g_rows': g_rows, 'aborted_blk': <當時 blk_label>, 'aborted_gate': str(e)}` 後 **`raise`**（原例外、原訊息、原型別）。
   🔒 `g_rows` 係 `:336` 之同一 list 物件（掛引用即可）。⛔ 改 27 個 raise 點一字。
2. **`run_verification.py:696` `except` 分支**：若 `hasattr(_e_sg, 'partial')` ⇒ 以 `_dump_csv` 落
   `got_G值_退縮{tag}_partial.csv`（欄 ＝ `g_rows` 之既有欄 ＋ 末加二欄 `中止街廓`／`中止閘`，全列同值）。
   🔒 `results.append((f"v3·StepG{tag}（結構閘/看守觸發）", False, …))` **一字不動**——仍紅、仍 FAIL；`run_all` 之判法不受影響。
   🔒 `partial` 落檔失敗（如 `g_rows` 空）⇒ `print` 具名，⛔ 二次 raise、⛔ 蓋掉原例外。

---

## §三　工項二：**街角規定範圍進 harness ctx**（`-246R` 發現二之 `B`）

### 案由

app 側 `f3_corner_range_polys` 由 `select_corner_lots_both_sides_v12`（`app.py:12643`）於 `main()` 路徑寫入 `session_state`；
該函式**不在 `_WF_NS_NAMES`**、harness **未呼叫** ⇒ `verify/` 全域 `0` 命中 ⇒ `K-9-23` 藍影於 harness **恆不可判**。

### 施工（🔒 同源·⛔ 自創第三源）

1. 先讀 **`verify/fixture_corner_range_k8.py`**：其為 harness 側既有之街角範圍構造路徑（經 `ns["_build_corner_range_v3"]`·該函式**已在 `_WF_NS_NAMES`**）。
2. 於 `run_step_g` 之 ctx 組裝處（`_corner_buffer_S` 所在之 §3 街角 band 一帶·`stepg:~330`），以**與該 fixture 逐字相同之呼叫形**為每一街角側算 `corner_range_poly`，存入 `ctx['corner_range_polys'][(blk_label, side)]`。
3. 🛑 **停機款**：若該 fixture 之構造輸入與 `select_corner_lots_both_sides_v12` 所用者**不同源**（如 `_t_override`／`chamfer_tri`／`setback` 取值不同）⇒ **停機上呈**、⛔ 自行擇一。判法 ＝ 逐參數對讀二者之實參來源，於報告列表。
4. ⛔ 把 `select_corner_lots_both_sides_v12` 加進 `_WF_NS_NAMES`（會動 `app.py`·且其有 UI 耦合）。

---

## §四　工項三：**最小建築面積有效值進 harness ctx**（`-246R` 發現二之 `C`·只鋪管線）

1. `run_verification.py` 之 `param_by_tag[tag]` 加鍵 `'eff_min_build_by_blk': {}`（二情境皆空）。
2. `run_step_g` 簽章加 `eff_min_build_by_blk=None`，入 ctx（`None ⇒ {}`）。
3. 🔒 **本批無消費端**（`_lot_gate` 屬 `-246`）——只證**管線通**：於 `pool_diag` 或既有診斷 dict 加一鍵 `eff_keys=sorted(eff.keys())`（二情境皆 `[]`）。⛔ 改任何既有鍵之值。
4. 合成 `eff` 之 fixture（證 `C` 分支）＝ `-246` 續辦之 `V-D`，⛔ 本單。

---

## §五　工項四：自誤二則（分鑄·段甲·號 CC 復算）

發單側於 `a313ebd` 實測 `MAX 300`／缺號 `[106]`／恆等式 `True` ⇒ `N ＝ 301`、`N+1 ＝ 302`。

### `自誤 N`｜`V-A` 之前提第二度不成立（`300` 同族·緊接其後）

🩸 `-246 §四` 立 `V-A`「Step G 之 `g_rows` 逐位 diff 空」，而 dump 在 `try` 內、`R2` 之 raise 在其前 ⇒ 不落檔。
`300` 之通則令查「產生路徑是否涵蓋本批所改之碼」——已查（harness 確跑到四掛載點），**未查落檔點是否在現行中止點之前**。
🔒 **受詞** ＝ 驗收前提之第二軸（落檔點 vs 中止點）。**族** ＝ `300` 同族·第二度。
🔒 **通則**（承 `300`·補一款）：凡以「某輸出可得」立驗收，須同格載 (a) 產生路徑涵蓋本批所改之碼、**(b) 落檔點位於現行已知中止點之前**（`try` 內之 dump 於 raise 時不執行，視同不落檔）；二者各附 `檔:列` 錨。**責** ＝ 發單側。

### `自誤 N+1`｜未令補列 `_WF_NS_NAMES`

🩸 `-246` 令新增 module 級 `_lot_gate` 供 `ns[...]` 取用，未令補列 `app.py:14119` 之 `_WF_NS_NAMES`（單內 `0` 命中）⇒ 生產路徑必 `raise`、`fixture_wf_ns_wiring.py` 轉紅。CC 偵察時自捕。
🔒 **受詞** ＝ 接線清單。**族** ＝ 未窮查（`294`／`298` 同族）。
🔒 **通則**：凡令新增供 `ns[...]` 取用之符號，單須同格令補列 `_WF_NS_NAMES`，並以 `fixture_wf_ns_wiring.py` 綠為驗收。**責** ＝ 發單側。

**鑄號收工閘**：`MAX 300 → 302`；缺號恆 `[106]`；號之零污染。

---

## 【驗收】

| 證 | 內容 | 判 |
|---|---|---|
| **`V-1` 既有輸出逐位不變** | 拋棄式 clone 改前／改後各實跑 UC9898 二情境至自然中止；**改前已存在之全部 `verify/out/got_*.csv` 逐位 diff 空**；`results` 列（含二 FAIL 列之文字）逐位相同 | 缺一即紅 |
| **`V-2` 部分落檔** | `got_G值_退縮0m_partial.csv`／`_退縮3.5m_partial.csv` 二檔存在、非空、含 `R1` 全部宗；`中止街廓` ＝ `R2`；`中止閘` 逐字含 `-241R` 所載之閘名（`0m`：`②-宗 圍堵閘`／`3.5m`：telescoping） | 缺一即紅 |
| **`V-3` corner polys** | ctx 中每一街角側各一非空多邊形；**同源證**：逐參數對讀表（fixture 路徑 vs `select_corner_lots_both_sides_v12`）無「不同源」列 | 有即停機 |
| **`V-4` eff 管線** | 二情境 `eff_keys ＝ []`；以拋棄式呼叫傳 `{'R1': 1.0}` 得 `eff_keys ＝ ['R1']` | 缺一即紅 |
| **`V-B`** | 二檔 diff 逐行人閱；**pass 路徑之 diff 須為空**（`:667`–`:695` 除加鍵外一字不動） | — |
| **`V-C`** | 十檔雜湊：僅 `run_verification.py`／`stepg_pipeline.py` 變；`app.py` 與餘七檔逐位不變 | — |
| 判別力自證 | `V-1` 對照組：故意改一 `got_*` 值須紅；`V-2` 對照組：移除 `e.partial` 掛載須紅 | — |

🔒 凡出數載三軸；宣告框三數分列。

---

## §六　產出與放行

段甲逕推。段乙 → `verify/W-G.9-247-c1` → 發單側復驗 → KL 放行 → 併線（快轉或 `-c2` 同一性閘）。
併線後 `-246` 續辦於新主線上施工（其 `S-3` 之 `stepg_pipeline.py` 雜湊須改用併線後之值）。

SELF_SHA256: ca4650586579dae48457b3401d0462bec6217892f3e8b49719758909507b7106
