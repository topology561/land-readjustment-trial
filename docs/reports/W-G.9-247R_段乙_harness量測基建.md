# `W-G.9-247R`　段乙執行報告：harness 量測基建（工項一／三**已落地**·工項二**停機**）

> 🛑 本文 **⛔ 鑄任何號**。所有數字**現查於倉／當場實測**；三軸逐處載明（`VR-091`）。
> 🔴 **段乙之生產碼 commit ⛔ 推主線**——已推側分支 `verify/W-G.9-247-c1`，候發單側逐位復驗與 KL 逐字放行。

---

## §零　態錨

| 項 | 值 |
|---|---|
| 段甲末（主線）| `1c653205f96ce35c5005de74f211d6defa54f369` |
| 本報告之基座 | 同上 |
| 拋棄式 clone | `C:/Users/admin/AppData/Local/Temp/w247`（自 **origin** clone·`core.autocrlf=false`·HEAD ＝ `1c65320`·CR ＝ `0`）|
| 🔒 所驗即所交 | 工作區二檔（LF 正規化後）`sha256[:16]` **＝** clone 內二檔：`stepg c3fea857b912d865`／`rv a84285bf6121dd72` |

🔒 **⛔ 於主 checkout 跑長跑**（`CLAUDE.md` `常規六 三`·拋棄式 clone）。

---

## §一　工項零（段甲·已推主線 `2f04fda`）

`S-0` ✅ 逐位相符（受詞 `8436` B·判別力：全檔口徑 ≠ 單載）／
`S-1` ✅ `247` `D1 0`／`D2 0`／`D3 0`（鬆框 `1`／`1`·唯一落點 ＝ `-246` 單 `§零` 之對照乙列 ⇒ 依補款 `②` ⛔ 占用）·對照甲 `246` `2`／`2`／`0`·對照乙 `248` `0`／`0`／`0`／
`S-3` ✅ `10/10`／`S-0b` ✅ `rc=0`（`--selftest` 四造全成立）。母體 全 `docs/` **`571`** 檔 ⇒ 與單所載**逐格相符**。

## §二　工項四（段甲·已推主線 `1c65320`）

`自誤 301`（`V-A` 前提第二軸）／`302`（`_WF_NS_NAMES` 未令補列）已鑄。
鑄後：定義框列命中 `294→296`／重咬 `3`／純單筆 `291→293`／相異 `293→295`／**`MAX 300→302`**／缺號恆 `[106]`／恆等式 `True`。

---

## §三　🛑 工項二：**停機**（單內二條款互斥·`常規二` 取保守項）

### `a`　互斥之逐字

| 條款 | 逐字 |
|---|---|
| 單首行 | 「🔴 **生產碼（harness 側·`verify/` 二檔）**：… **⛔ 動 `app.py`**」 |
| `§三-2` | 「以**與該 fixture 逐字相同之呼叫形**為每一街角側算 `corner_range_poly`」 |

🔒 **fixture 之呼叫形**（`verify/fixture_corner_range_k8.py:244`–`:263`·逐字）**必用二個 `ns[…]`**：
`baseline_pts=ns["_baseline_pts_from_manual"](mb, b["vertices"])` ／ `chamfer_tri=ns["_make_chamfer_tri_wb"](b, which)`。

🔒 **現查（AST 取·`app.py` blob@`1c65320`）**：`_WF_NS_NAMES` ＝ **`29`** 筆，逐名如下——
`_build_corner_range_v3` ✅ 在／`get_min_lot_size` ✅ 在／
🔴 **`_make_chamfer_tri_wb` ⛔ 在**／🔴 **`_baseline_pts_from_manual` ⛔ 在**／`_cad_dxf_quantum` ⛔ 在。

⇒ 🔴 **`run_step_g` 於 <u>app 生產路徑</u>之 `ns` ＝ `_wf_ns()`，其母體即該 `29` 筆**
（`app.py:14180`–`:14188`·缺名逐字 `raise RuntimeError(f"🔴 七級調配接線：app 缺真符號 {n}…")`）
⇒ 依 `§三-2` 施工而**不動 `app.py`** ⇒ **app 生產路徑必 raise**，且 `verify/fixture_wf_ns_wiring.py`（為此專設·在倉 `16835` B）**轉紅**。

🩸 **同批第二度**：此正是本批工項四所鑄之 **`自誤 302`** 之受詞（倉內既有之戒·自誤簿 `:3717`），**於下一個工項再現**。

### `b`　`常規二` 之處置：**取保守項 ＝ 工項二停辦**

三個候選皆有硬阻：
`(A)` 補列 `_WF_NS_NAMES` ⇒ **違單首行「⛔ 動 `app.py`」**；
`(B)` `ns.get(...)` 加兜底 ⇒ **違 `no-silent-fallback`／`GB-60` 病灶族**（`CLAUDE.md` 逐字「⛔ 禁改為 `ns.get(...)` 加自算 fallback」）；
`(C)` 於 `stepg` 自寫 `baseline_pts`／`chamfer_tri` ⇒ **違單 `§三` 之「⛔ 自創第三源」**。
⇒ **保守項 ＝ 不施工、逐字回報**（`常規二`）。

### `c`　`§三-3` 所令之**逐參數對讀表**（已辦·三路·⛔ 二路）

🔒 **三軸**：來源 ＝ `blob@1c65320` ＋ `data/V6_1.dxf` 之解析結果／母體 ＝ 六街廓 × `8` 街角側／粒度框 ＝ **實參來源** ＋ **面積（㎡）**。

| 參數 | `(a)` fixture | `(b)` `build_param_table:242-250`（**其輸出即 `run_step_g:529/540` 之消費者**）| `(c)` `select_corner_lots_both_sides_v12` |
|---|---|---|---|
| `block_vertices`／`centroid` | `cb_by[lbl]` | 同 | `f3_classified_blocks` 之同源 |
| `front_pts` | `cad["front_lines"]` | 同 | `ss['f3_cad_front_lines']` |
| `baseline_pts` | `_baseline_pts_from_manual(cad["baselines"])` | 同 | 同（`ss['f3_manual_baseline']`）|
| `side_line_pts`／`alloc_dir` | `cad[…]` | 同 | `ss['f3_cad_…']` |
| `setback`／`chamfer_tri` | 參數／`_make_chamfer_tri_wb` | 同 | 同 |
| **`block_depth`** | `snap["blocks"][lbl]["街廓分配深度_m"]`（**raw**）| 同（raw）| 🔴 `ss['f3_pk_alloc_depth']` ＝ `round(同值, 2)` |
| **`min_width`** | `get_min_lot_size(category, 路寬)`（**逐街廓**）| 🔴 `snapshot["global"]["法定最小寬_m"]`（**全域常數**）| `get_min_lot_size(category, round(路寬,2))`（逐街廓）|
| **`dxf_quantum`** | `(mb["_match"])["q_detected"]`（街廓級）| 同 | 🔴 `_cad_dxf_quantum()`（**檔案級優先**）|

🔒 **實測（本案）**：三路 `min_width` **皆 `3.5000`**；`depth` **raw ＝ round2**（六街廓逐格）；
`f3_cad_dxf_quantum` 於 harness `ss` **不存在**（其唯一設定處 ＝ `app.py:18191`·在 `main()` 內）⇒ `_cad_dxf_quantum` **必回退**至街廓級。
⇒ **三路構造之面積於 `8` 街角側 × 二退縮 ＝ `16` 格，最大差 `0.000e+00`**。

🔴 **惟 `(b)` 之 `min_width` 係<u>全域常數</u>** ——`CLAUDE.md` 明文警告「本案六街廓寬皆 `3.50` ⇒ 同解；**換案會分家**」
⇒ 🛑 **本案之全等係<u>巧合</u>、⛔ 結構保證**。此為**既有**之三源並存，⛔ 本批所引入；候發單側裁其是否登記。

---

## §四　工項一：**中止時之部分落檔**（已落地）

### `a`　施工形之偏離（`常規二`·逐字回報）

單 `§二-1` 逐字令「`run_step_g` 之**本體**以一層 `try/except RuntimeError as e` **包住**」。
🔴 **該逐字形與本單【驗收】`V-1` 互斥**：實測 `run_step_g` 本體含 **`33`** 個跨列字串常數，
其中 **`7`** 個為**跨列 docstring**（`:1038-1044`／`:1076-1080`／`:1099-1103`／`:1144-1156`／`:1170-1195` 等）
⇒ 整體縮排會改變其**內容**；且 diff 將達 **~1190 列**，使 `V-B`「逐行人閱」不可行。
⇒ **保守項 ＝ 內外分離**（`run_step_g` 薄殼 ＋ `_run_step_g_impl` 本體）——**語意同一、字串內容零變更**。

### `b`　落地之形

- `run_step_g`（薄殼·**⛔ 吞**）：`_pcap = {'g_rows': [], 'aborted_blk': None}` → `try: return _run_step_g_impl(…)` →
  `except RuntimeError as _e_partial:` 掛 `_e_partial.partial = {'g_rows','aborted_blk','aborted_gate','eff_keys'}` → **bare `raise`**（原物件·原型別·原訊息·原 traceback）。
- `_run_step_g_impl`：本體**逐字位移**，僅加二處 `_pcap` 純賦值。
- `run_verification.py` `except` 分支：`results.append(...)` **一字不動**（仍紅、仍 FAIL），其**後**加部分落檔；
  落檔失敗 ⇒ **具名 `print`**、⛔ 二次 raise、⛔ 蓋原例外。

### `c`　`V-B` 機械證明（AST·敘述層）

| 檢 | 結果 |
|---|---|
| `py_compile` 二檔 | ✅ |
| `_run_step_g_impl` **主迴圈體** vs 基座 | 敘述 `91 → 92`；**改刪 `0`**；新增 `1`（`if _pcap is not None: _pcap['aborted_blk'] = blk_label`）|
| `Raise` 節點逐字集合（impl vs 基座）| **相同 ＝ `True`**（`19` 節點·**27 處 `raise RuntimeError` 一字未動**）|
| 薄殼之 `Raise` 節點 | **`1`** ＝ bare `raise` |
| `run_verification.main()` 頂層敘述 | `62 → 62`；唯一被改者 ＝ 含 StepG 之 `(setback, tag)` 迴圈 |
| **pass 路徑**（`try` body）| 敘述 `15 → 15`；**唯一相異 ＝ 加具名引數 `eff_min_build_by_blk={}`** |
| `except` 首列 | **逐位相同**（`results.append((f'v3·StepG{tag}（結構閘/看守觸發）', False, [f'[StepG{tag}] {_e_sg}']))`）|
| **全體被刪之列 ＝ `4`**（逐列具名）| ① rv 之呼叫末列（→ 加引數後之新列）② stepg `def` 之第 2 列（→ 薄殼＋impl 簽章）③ 舊單列 docstring（→ 移入 impl）④ `return {...}`（→ 同式 ＋ `'eff_keys'`）⇒ **⛔ 有任何算式被刪而未以等價物取代** |

`numstat`：`verify/stepg_pipeline.py` **`67` 增／`3` 刪**；`verify/run_verification.py` **`35` 增／`1` 刪**。

---

## §五　工項三：**`eff_min_build_by_blk` 管線**（已落地·含二處偏離）

### `a`　`§四-1` 之受詞型別錯誤（`常規二`·逐字回報）

單逐字令「`run_verification.py` 之 `param_by_tag[tag]` **加鍵** `'eff_min_build_by_blk': {}`」。
🔴 `param_by_tag[tag]` ＝ `build_param_table(...)` 之回傳 ＝ **`list[dict]`（列）**、**⛔ `dict`** ⇒ 「加鍵」**結構上不可能**；
且縱使加欄，必破 `參數{tag}` 之 baseline diff（`run_verification.py:523`）。
⇒ **保守項 ＝ 於呼叫端傳<u>顯式具名引數</u>** `eff_min_build_by_blk={}`（效果同「二情境皆空」）。

### `b`　`§四-3` 之出艙點不可觀測（**`自誤 301` 同族·第三度**）

單令 `eff_keys` 置於**回傳值／`pool_diag`**，惟二者**皆在 `return` 之後**，而現態二情境皆於 `R2` `raise`
⇒ 該出艙**結構上不可觀測**——與 `V-A` **同一病**。
⇒ **保守項 ＝ 二路並存**：回傳值之 `'eff_keys'` **⛔ 移除**，**併掛 `partial`** 並於 `except` 分支印出。
🔒 **⛔ 塞 `pool_diag`**——後者逐鍵攤成診斷表欄位，加鍵會污染 baseline 欄集（同 `_stage2_placed` 之既例）。

### `c`　🩸 **判別力對照當場捕得 CC 自身之實作缺口**

`_eff_mba` 初置於 `g_rows` 一帶，而 `f3_total_burden_rate_from_finance` 未鋪底之 `raise` 落在其**前**
⇒ 早期中止之 `partial['eff_keys']` **恆 `None`** ⇒ 對照組 `{'R1': 1.0}` 與 `{}` **得數相同** ⇒ **該檢判別力為零**。
⇒ 已將該二敘述**前移至函式體之最首**（純賦值·⛔ 有行為後果），並於碼內註明其**由判別力對照所迫**。
🔒 **若無此對照，本缺口會以「看起來正常之 `None`」出艙。**

---

## §六　【驗收】逐項

**三軸**：來源 ＝ 上開 clone（`blob@1c65320` ＋ 二檔 patch）／母體 ＝ `verify/out/got_*.csv` ＋ `stdout` 全文／粒度框 ＝ **bytes**（`cmp`）與**列**。

| 證 | 判 | 實測 |
|---|---|---|
| **`V-1(a)`** 改前已存在之 `got_*.csv` 逐位 diff 空 | ✅ | 改前 `6` 檔（**⛔ 含 `got_G值_退縮*.csv`**——`自誤 301` 之實跑坐實）；改後同 `6` 檔 **相異 `0`** |
| **`V-1(b)`** `results` 列逐位相同 | ✅ | `34 → 34` 列·`cmp` 逐位相同（新增之 `🟡` 二列係**新增訊息**、⛔ `results` 列）|
| **`V-1(c)`** 全 `stdout` 之相異 | ✅ 已逐項具名 | 僅 ① 新增之 `partial`／`eff_keys` 四列 ② **traceback 行號差 `6` 處**（類 II·逐項具名）③ 一處函式名 `run_step_g → _run_step_g_impl` |
| **`V-2`** 部分落檔 | ✅ | `got_G值_退縮0m_partial.csv` **`21` 列**（`R1` `7`／`R2` `14`）／`_退縮3.5m_partial.csv` **`24` 列**（`R1` `8`／`R2` `16`）；欄 `31`（原 `29` ＋ `中止街廓`／`中止閘`）；`中止街廓` 相異值 ＝ `['R2']` |
| ├ `0m` `中止閘` 逐字 | ✅ | `街廓 R2 抵費地計算失敗：🔴 ②-宗 圍堵閘破[R2]：宗-宗重疊 = 45.9766 > 上界 2.8906…` ⇒ **與交接文 `§五` 所載 `45.9766` 相符** |
| └ `3.5m` `中止閘` 逐字 | ✅ | `🔴 結構閘 telescoping 破：街廓 R2 left 側 ΣRw_實跑=100.02 ≠ …=44.41（Δ=55.606 >0.1）` ⇒ **與交接文所載三數相符** |
| **`V-3`** corner polys | 🛑 **停機**（見 `§三`）| 逐參數對讀表已出艙；**⛔ 施工** |
| **`V-4`** eff 管線 | ✅ | 二情境 `eff_keys = []`；判別力 **4/4**：`None→[]`／`{}→[]`／`{'R1':1.0}→['R1']`／`{'R4':…,'R1':…}→['R1','R4']` |
| **`V-B`** | ✅ | 見 `§四 c`（敘述層 AST 證明·四列刪除逐列具名）|
| **`V-C`** 十檔雜湊 | ✅ | 僅 `run_verification.py`（`e48f24c84079f365 → a84285bf6121dd72`）與 `stepg_pipeline.py`（`0260273350021311 → c3fea857b912d865`）變；**`app.py` 與餘七檔逐位不變** |
| **判別力自證 `V-1`** | ✅ | 改前／改後 `stdout` **不同** ⇒ 證量測非恆同 |
| **判別力自證 `V-2`** | ✅ | 注入「移除 `e.partial` 掛載」（咬到 `1`）⇒ 印 `🔴 例外未帶 partial`、**partial 檔數 `0`** ⇒ **該檢非恆綠**；受測檔已還原 |
| 併證（薄殼⛔ 過度捕捉）| ✅ | 非 `RuntimeError` 之例外（`AttributeError`）**⛔ 掛 `partial`** |

---

## §七　候發單側裁

| # | 受詞 |
|---|---|
| `1` | 🛑 **工項二之解**：`(A)` 授權補列 `_WF_NS_NAMES`（須放寬「⛔ 動 `app.py`」）／`(B)` 改由 `build_param_table` 之 `rng()` 保留多邊形並經新出參送入（⛔ 動 `app.py`·惟須確認 `min_width` 之源）／`(C)` 暫不辦 |
| `2` | `min_width` **三源並存**（逐街廓查表 ×2 vs `snapshot["global"]["法定最小寬_m"]`）——本案全等係巧合；是否鑄 `GB` 登記 |
| `3` | 是否鑄號登記 `§四 a`／`§五 a`／`§五 b` 之三處單內缺陷（`§五 b` 為 `自誤 301` 同族**第三度**）|
| `4` | `V-1(c)` 之 traceback 行號差 `6` 處（類 II）——依 `CLAUDE.md` 須**逐項具名確認**，本文已列；是否另需對帳器登記 |

---

🛑 **本批⛔ 動 `app.py` 一字**；⛔ 推主線。側分支 ＝ `verify/W-G.9-247-c1`。
