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

---

## 🔧 就地加註：**工項二已落地（依 `(A)`）** ＋ 🔴 **新捕之紅**（KL 令 `2026-09-07`·⛔ 上文一字不刪·純末端追加）

🛑 本節 **⛔ 鑄任何號**。⛔ 追改上文任何一字（`常規四（九）五`）——上文之 `§三`「工項二停機」
係**當時之態**，其**解**由本節承載。

### 🔧 一　KL 之令（`2026-09-07`·逐字要旨）

> 工項二續辦：依 `(A)`。`app.py` 只得於 `_WF_NS_NAMES` 補列上開二名（`+2`／`−0`）；
> corner polys 依 fixture `:244`–`:263` 之呼叫形入 `ctx['corner_range_polys'][(blk, side)]`；
> `V-3` 同源證改為「fixture 與 `v12` 之 `min_width` **皆自 `get_min_lot_size` 逐街廓查表**」之錨。
> 同一側分支上新 commit（`-c1` 前進），⛔ 動主線。`V-C` 改為：**三檔變**（`app.py` `+2`／`−0`）、**七檔不變**。
> 工項一／三已由發單側逐行復驗綠，⛔ 回改。

### 🔧 二　落地（側分支 `verify/W-G.9-247-c1` ＝ `e147c9f` → **`61800b0`**·快轉）

| 檔 | `numstat` | `sha256[:16]`（`1c65320` → 現）|
|---|---|---|
| `app.py` | **`2` 增／`0` 刪** | `ad7a91dba08119f5` → `445585e238c26154` |
| `verify/stepg_pipeline.py` | `66` 增／`1` 刪 | `0260273350021311` → `508708b9c792f6a8` |
| `verify/run_verification.py` | `8` 增／`0` 刪 | `e48f24c84079f365` → `d0d531f7dc051b65` |
| 餘七檔 | — | **逐位不變** |

🔒 **`V-C` ＝ 變 `3` 檔／不變 `7` 檔 ✅**（與令相符）。
🔒 **`app.py` 之 `+2`／`−0` 逐字**：於 `"_proj_pop_ghost3",` 之後補 `"_make_chamfer_tri_wb",` 與
`"_baseline_pts_from_manual",` 二列；`_WF_NS_NAMES`（AST 取）**`29` → `31`** 筆，⛔ 動他處一字。
🔒 **「⛔ 回改工項一／三」之給證**：`e147c9f..61800b0` 之**唯一刪除列** ＝
`            'eff_keys': sorted(_eff_mba.keys())}`——其取代列**逐字含同一片段**
`'eff_keys': sorted(_eff_mba.keys()),` 並於其後**追加**二鍵（`corner_range_polys`／`corner_range_errors`）
⇒ **工項三之語意一字未改**，僅回傳 dict 多二鍵。

### 🔧 三　`V-3`：**已成立**（機驗·⛔ 以「呼叫形相同」推論）

🔒 **同源錨（依令改用）**：`min_width` 三處逐字——

| 路 | 逐字 | 性質 |
|---|---|---|
| fixture `:249`–`:250` | `ns["get_min_lot_size"](b["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))["min_width"]` | 逐街廓查表 |
| **本批 ctx** | `ns['get_min_lot_size'](_crp_b['category'], float(SB[_crp_lbl]['正面']['路寬_m']))['min_width']` | **同式** |
| `v12` ← `selection_pipeline.py:330`–`:332` | `ns["get_min_lot_size"](b.get('category',''), float(_row.get('正面路寬(m)', 0.0)))["min_width"]` | 逐街廓查表 |

⇒ **三者皆自 `get_min_lot_size` 逐街廓查表** ⇒ **同源證成立**。
⚠️ `run_verification.build_param_table` 之**第四路**取**全域常數** ⇒ **⛔ 採之**（已鑄 **`GB-151`**）。

🔒 **實測（拋棄式 clone·二情境·`ctx` 之實際多邊形面積·⛔ 由呼叫形推論）**

| 街角側 | `0m` | `3.5m` |
|---|---|---|
| `R1/left` | `114.939693` | `226.011400` |
| `R1/right` | `110.676142` | `227.128484` |
| `R2/left` | `152.986677` | `308.165400` |
| `R3/right` | `153.803947` | `307.793779` |
| `R4/left` | `116.079491` | `226.006436` |
| `R4/right` | `111.023779` | `225.423232` |
| `R5/left` | `146.503800` | `299.730991` |
| `R6/right` | `146.376462` | `299.134509` |

🔒 **`16` 格與本報告 `§三 c` 之獨立三路探針所測<u>逐位相同</u>**；**全部非空**（`110`–`308 ㎡`）。
🔒 `corner_range_keys` 二情境各 **`8`** 鍵（全部街角側）；`corner_range_errors` **未印** ⇒ **零失敗**。
🔒 **可觀測性**：`keys`／`areas`／`errors` **併掛 `_pcap`** 並於 `except` 分支印出
——依 `自誤 305` 之戒（出艙點須於現行已知中止點下**可達**），⛔ 只置於 `return`。

### 🔧 四　其餘驗收（現態·拋棄式 clone）

`V-1(a)` ✅ 改前 `6` 檔 `got_*.csv` 逐位 diff 空（相異 `0`）／`V-1(b)` ✅ `results` 列 `34 → 34` 逐位相同／
`V-2` ✅ partial 二檔仍產出（`21`／`24` 列·中止街廓 `R2`）／`V-4` ✅ 二情境 `eff_keys = []`／
`py_compile` 三檔 ✅。🔒 **所驗即所交**：工作區三檔（LF 正規化）`sha256[:16]` ＝ clone 內三檔（逐檔 `SAME`）
＝ 入倉 blob（逐位 `SAME`）。

### 🔴🔴 五　新捕之紅：**`verify/fixture_wf_ns_wiring.py` 由 `rc=0` 轉 `rc=1`**（**段乙所致·⛔ 工項二**）

🩸 **實測隔離（三態·皆自 origin clone·`core.autocrlf=false`）**

| 態 | 內容 | `rc` |
|---|---|---|
| `4521c04` | ⛔ 段乙、⛔ 工項二 | **`0`** ✅（逐字「✅ 夾具 PASS（rc=0）」）|
| `e147c9f` | **段乙 only** | 🔴 **`1`**（`IndexError` @ `:254`）|
| 現態 | 段乙 ＋ 工項二 | 🔴 `1`（同一 `IndexError`）|

⇒ 🔴 **段乙<u>單獨</u>即致之**，⛔ 工項二。

🔒 **根因（逐字·⛔ 推理）**：該器之 `_stepg_unpack_lines()`（`:185`–）之 docstring `:188`–`:189` 逐字：

> **「無條件」＝** 該節點至其最內層 `FunctionDef`（**須為 `run_step_g` 本身**）之
> 祖先鏈上，⛔ 無 `Try`／`If`／迴圈／`With`，且 ⛔ 無中介之巢狀 `FunctionDef`／`Lambda`。

⇒ 段乙之**薄殼／`_impl` 分離**使全部 `ns[...]` 解包點移入 **`_run_step_g_impl`**
⇒ `unpack` 母體**歸零** ⇒ `:254` 之 `unpack[0][0]` **解引用空 list** ⇒ `IndexError`。

🔴 **該夾具在 `run_all` 之名目集**（`verify/run_all.py:126`）⇒ **係 `run_all` 之新紅**、⛔ 僅屬本地。

⚠️ **併記（該器自身之瑕）**：其空集守衛 `if not unpack or not uncond: red(...)` 位於 `:255`——
**在 `:254` 之解引用之後** ⇒ 空集時**恆 `IndexError`**，其所欲之 `red("… 空真假綠")` **不可達**。

🛑 **CC ⛔ 修之**：單首行「⛔ 動 `verify/` 其他檔」，本次令**亦未放寬** ⇒ **停機上呈**。
🔒 **候發單側裁之三候選**（⛔ 由 CC 自裁）：
`(甲)` 授權改該夾具之受詞為「`run_step_g` **或** `_run_step_g_impl`」（並順修其空集守衛之位置）；
`(乙)` 改段乙之形使 `ns[...]` 留在 `run_step_g` 內（🔴 與「工項一／三 ⛔ 回改」衝突）；
`(丙)` 暫記為**已知紅**並登記，俟波末處置。

### 🔧 六　本報告 `§七` 候裁之現況更新（⛔ 追改該節）

| `§七` # | 受詞 | 現況 |
|---|---|---|
| `1` | 工項二之解 | ✅ **KL 已裁採 `(A)`**·已落地 |
| `2` | `min_width` 三源 | ✅ **已鑄 `GB-151`**（`97eec90`）|
| `3` | 三處單內缺陷是否鑄號 | ✅ **已鑄 `自誤 303`／`304`／`305`**（`97eec90`）|
| `4` | `V-1(c)` traceback 行號差 `6` 處（類 II）| ⬜ **未決**（本文已逐項具名；是否另需對帳器登記候裁）|
| 🆕 `5` | `fixture_wf_ns_wiring.py` 之新紅（段乙所致）| 🛑 **本節五 之三候選·候裁** |

---

## 🔧 就地加註二：**採 `(甲)` ＋ rebase ＋ `V-0`**（KL 令 `2026-09-07`·⛔ 上文一字不刪·純末端追加）

🛑 本節 **⛔ 鑄任何號**（`自誤 306` 鑄於同批之另一 commit）。⛔ 追改上文任何一字。
🔴 **本節鑄於<u>側分支</u>** `verify/W-G.9-247-c1`——KL 令「**主線 ⛔ 動**」。

### 🔧 一　KL 之令（逐字要旨）

> 採 `(甲)`：`fixture_wf_ns_wiring.py` **限改上開二事**；**判別力三造缺一即紅**。
> 依 `W-G.9-206 §八` rebase 側分支至 `28d62f3`，重推；**同一性閘** ＋ **`V-0`**
> （`run_all` 全名目 `rc` 前後相同·既有紅逐項具名）＋ `V-1`〜`V-4` ＋ `V-C`（四變六不變）於新 SHA 重跑。
> 段甲追加：鑄 `自誤 306`。**主線 ⛔ 動。**

### 🔧 二　rebase 與**同一性閘**

`61800b0` → rebase 至 `28d62f3` ⇒ `2391c1f`（段乙）／`7da3fb0`（工項二）。

| 檔 | rebase 前後之 blob `sha256[:16]` | 判 |
|---|---|---|
| `app.py` | `445585e238c26154` → 同 | ✅ |
| `verify/stepg_pipeline.py` | `508708b9c792f6a8` → 同 | ✅ |
| `verify/run_verification.py` | `d0d531f7dc051b65` → 同 | ✅ |

🔒 **樹差**（`61800b0` vs rebase 後）＝ **僅主線新增之三份文件**（`+287` 列·`0` 刪）
——`W-G.4_泛用阻塞項登記表.md`／`W-G.9-247R_…md`／`W-G.9波_…自誤登記.md`。
🔒 **判別力**：對照組（本報告檔）之 blob **確有不同**（`bb32e345ef13728c` → `1664ca7e9a299d4a`）⇒ 器非紅。
⇒ 🔒 **「工項一／三／二已復驗之內容一字未改」機械成立。**

### 🔧 三　夾具之修（**限二事**）＋ **判別力三造**

`verify/fixture_wf_ns_wiring.py`　`17` 增／`6` 刪（`fdcf65ff63eb3a70` → `b17826a6f7b98bf5`）：

| # | 所改 | 逐字 |
|---|---|---|
| `(i)` | **受詞** | `if fname == "run_step_g":` → `if fname in ("run_step_g", "_run_step_g_impl"):`；併改其 docstring 之定義句（否則碼與其自述相牴觸）|
| `(ii)` | **守衛位置** | 空集守衛 `if not unpack or not uncond:` **前移至** `print(f"…{unpack[0][0]}…")` **之前** |

🔒 **判別力三造（缺一即紅·全成立）**

| 造 | 受詞 | 實測 |
|---|---|---|
| `①` 竄改·**靜態** | 自 `_WF_NS_NAMES` 抽一名 ⇒ 須**因抽名而新出現**於差集 | 抽 `F3_CATEGORY_BURDEN` ⇒ 竄改態差集 `['F3_CATEGORY_BURDEN']`／還原態 `（空）` ⇒ ✅ |
| `②` 竄改·**動態** | 自受限 `ns` 抽一**無條件**名 ⇒ 須轉紅 | 抽 `get_min_lot_size`（`stepg:337`·無條件）⇒ `KeyError @ stepg_pipeline.py:337` ⇒ ✅ |
| `③` **空集守衛之可達性** 🆕 | 合成空母體（monkey-patch `_stepg_unpack_lines → []`·**⛔ 改受測檔**）⇒ 須印 `red` 而**⛔ `IndexError`** | 例外 ＝ `None`／`RC 0 → 1`／含「空真假綠」＝ `True`／**含「解包點 ＝」＝ `False`**（證守衛先於解引用）⇒ ✅ |
| `③` 之**反造** | 真實母體非空 ⇒ 守衛**⛔ 觸發**（證非恆紅）| 母體 `22` 處／無條件 `13` 處 ⇒ 守衛條件 ＝ `False` ⇒ ✅ |
| `③` 之**改前對照** | 舊碼於空集之行為 | `IndexError: list index out of range` ⇒ ✅ 該瑕確係本次所修 |

🔒 **夾具 `rc`**：PRE（`28d62f3` 純態）`rc=0`／POST（＋四檔）**`rc=0`**／
對照 `e147c9f`（段乙 only）`rc=1` ⇒ **本修確解該紅**。
🔒 POST 逐字：「`run_step_g`／`_run_step_g_impl` 內之 `ns[...]` 解包點 ＝ **`22`** 處（行 `337`–`1006`）；其中**無條件執行** **`13`** 處」。

### 🔧 四　**`V-0`**：`run_all` 全名目 `rc` 前後相同

🔒 **三軸**：來源 ＝ 二拋棄式 clone（皆自 origin·`core.autocrlf=false`·HEAD `28d62f3`；
POST 另覆蓋四檔）／母體 ＝ `run_all` 全 `stdout`（PRE `47936` B／`534` 列；POST `49036` B／`542` 列）／
粒度框 ＝ **名目**（`✅ PASS`／`🔴 FAIL` 形）與**列**。

| 量 | PRE | POST | 判 |
|---|---|---|---|
| `run_all` 整體 `rc` | **`1`** | **`1`** | ✅ 相同 |
| 名目數 | **`34`** | **`34`** | ✅ |
| `PASS` ／ `FAIL` | **`10` ／ `24`** | **`10` ／ `24`** | ✅ |
| 僅 PRE 有之名目 | — | — | **`0`** ✅ |
| 僅 POST 有之名目 | — | — | **`0`** ✅ |
| **判翻轉之名目** | — | — | **`0`** ✅ |
| 收尾列 | `W-V run_all: FAIL` ＋ `🔴 對帳 FAIL` | 同 | ✅ |

🔒 **既有紅逐項具名（`24` 項·POST 皆仍 `FAIL`）**
`W-D.3 碎片`／`W-D.4`／`W-F F.0`／`F.1`／`F.2`／`F.3`／`F.4`／
`W-G G.1 接線層 ctx-builder 同源`／`W-G G.2 世代幾何曝出契約`／`v3 財務接線閘`／
`v3·StepG0m（結構閘/看守觸發）`／`v3·StepG3.5m（結構閘/看守觸發）`／
`v3·診斷0m（全欄逐格·無豁免）`／`v3·診斷3.5m（全欄逐格·無豁免）`／
`參數0m`／`參數3.5m`／`抵費地0m(應空)`／`抵費地3.5m`／`指配0m`／`指配3.5m`／
`率接線 G估 欄變動0m 8 格（期 0·Y 波後 baseline 同源）`／`率接線 G估 欄變動3.5m 12 格（期 0·Y 波後 baseline 同源）`／
`率接線無串聯0m（vs v1 原錨，豁免 G估 後逐格全等）`／`率接線無串聯3.5m（vs v1 原錨，豁免 G估 後逐格全等）`。

🔒 **`[D]` 全 `stdout` 之相異列 ＝ `64`（`24` 區塊）·逐項歸類**

| 類 | 內容 | 列數 |
|---|---|---|
| **類 I**（絕對路徑差·自動視為同）| `w0pre` → `w0post`（clone 目錄名）| 混於下列各項 |
| **類 II**（traceback 行號差·**已逐項具名**）| `run_verification.py` **`743→785`／`952→994`／`1029→1071`／`1080→1122`／`1146→1188`／`1213→1255`／`1312→1354`／`1411→1453`** ——**八處位移皆 `+42`**；自洽驗算：該檔 LF 淨增 **`+42`**（`numstat` `43` 增／`1` 刪）✅ | `16` |
| **類 II**（同上）| `stepg_pipeline.py` **`1003→1127`**（`+124`）；該檔 LF 淨增 **`+129`**（`132`／`3`）——差 `5` 係 `1003` **之後**尚有 `5` 列新增 ✅ | `2`〜`4` |
| **本批之刻意結構**（⛔ 類 III）| `in run_step_g` → `in _run_step_g_impl` ＋ 薄殼多出之 `1` 個 `File` frame 及其 `4` 列呼叫式；`nners, forced, setback)` → `lk, _pcap=_pcap)` | `6` |
| **本批之新增診斷** | `🟡 [StepG*] 部分落檔／eff_keys／corner_range_keys／corner_range_areas` 共 **`8`** 列 | `8` |
| 🔴 **顯示窗尾切之衍生**（**⛔ 例外鏈滅失**·見下）| PRE 之 `RuntimeError: 🔴 ②-宗…`／空列／`During handling of the above exception…`／空列／`Traceback (most recent call last):` **`5` 列**於 POST 不見 | `5` |

🛑 **末項之機械證（⛔ 推論）**——其為**固定尾切之顯示窗**，⛔ 例外鏈之滅失：

1. **尾切碼逐字**：`verify/run_all.py:315`（同形另見 `:202`／`:252`／`:274`／`:297`）
   `for _ln in ((_r8.stdout or "") + (_r8.stderr or "")).strip().splitlines()[-14:]:`
   ⇒ **固定 `14` 列尾窗**。
2. **該名目（`E 系列實測快照閘`）之輸出列數**：PRE **`14`**／POST **`14`** ⇒ **相等**。
3. **`File` frame 數**：PRE `3`／POST `4`（**`+1`** ＝ 薄殼之 frame）；其呼叫式另佔 `4` 列 ⇒ 共 **`+5`**
   ⇒ 頂端**恰被擠掉 `5` 列** ＝ 上表所列之 `5` 列。
4. **末列逐字相同**：二者皆 `RuntimeError: 街廓 R2 抵費地計算失敗：🔴 ②-宗 圍堵閘破[R2]：宗-宗重疊 = 45.9766 > 上界 2.8906（(宗數14−1)×0.005×深度44.47）…`
   ⇒ **最終例外之型別與訊息一字未變**。
5. 🔒 **PRE 自身即已被切**——其首列為 `RuntimeError: 🔴 ②-宗…`（＝內層例外之**末**列），
   其 `Traceback` 標頭與各 frame **本即不在窗內** ⇒ 該窗**本來就在切**，⛔ 本批所致。

⇒ 🔒 **`V-0` 之判：全名目與其判逐項相同、既有紅逐項具名、無類 III 之實質差 ⇒ ✅ 綠。**

### 🔧 五　`V-1`〜`V-4`（於 `run_all` `[3/3]` 段之 `run_verification` 產物）

| 證 | 判 | 實測 |
|---|---|---|
| `V-1(a)` | ✅ | PRE `got_*.csv` **`6`** 檔；POST 逐位 diff **相異 `0`**（判別力：PRE 檔數 `> 0`）|
| `V-2` | ✅ | POST `got_G值_退縮0m_partial.csv` **`21`** 列（`R1` `7`／`R2` `14`）／`_3.5m_partial.csv` **`24`** 列（`R1` `8`／`R2` `16`）；欄 **`31`**；`中止街廓` ＝ `['R2']`。**PRE 之 partial 檔數 ＝ `0`**（判別力）|
| `V-3` | ✅ | 二情境 `corner_range_keys` 各 **`8`** 鍵（全街角側）；`corner_range_errors` 未印 ⇒ 零失敗。PRE 之同字樣命中 **`0`**（判別力）|
| `V-4` | ✅ | 二情境 `eff_keys = []` |

### 🔴 六　`V-C`：**實測與令所稱之「四變六不變」不符**（照實·⛔ 湊數）

🔒 **十檔之定義**（交接文 `§一`）＝ **閘 `P` 五檔 ＋ `wf_f*` 五檔**——
`app.py`／`verify/selection_pipeline.py`／`verify/run_verification.py`／`verify/stepg_pipeline.py`／`verify/run_all.py`／`wf_f0`〜`wf_f4`。
🔴 **`verify/fixture_wf_ns_wiring.py` ⛔ 屬十檔。**

| 母體 | 變 | 不變 |
|---|---|---|
| **十檔** | **`3`**（`app.py`／`run_verification.py`／`stepg_pipeline.py`）| **`7`** |
| **十檔 ∪ {該夾具} ＝ `11` 檔** | **`4`** | **`7`** |

⇒ 🛑 **二讀皆非 `4`／`6`**。研判令之算式係**假定該夾具屬十檔**所致（`4 + 6 = 10`）。
🔒 **CC ⛔ 湊數、⛔ 逕自改十檔之定義**；照實出艙二數，候發單側裁其取何母體。

🔒 **逐檔實測（`28d62f3` → 本批）**
`app.py` `ad7a91dba08119f5` → `445585e238c26154`／
`verify/run_verification.py` `e48f24c84079f365` → `d0d531f7dc051b65`／
`verify/stepg_pipeline.py` `0260273350021311` → `508708b9c792f6a8`／
`verify/fixture_wf_ns_wiring.py` `fdcf65ff63eb3a70` → `b17826a6f7b98bf5`；
`selection_pipeline`／`run_all`／`wf_f0`〜`wf_f4` **七檔逐位不變**。

### 🔧 七　候發單側裁

| # | 受詞 |
|---|---|
| `1` | `V-C` 之母體：取**十檔**（`3`／`7`）抑或**十一檔**（`4`／`7`）？「四變六不變」之算式須修 |
| `2` | `自誤 306` 之落點：本批依 `常規二` 取保守項置於**側分支**（因「主線 ⛔ 動」與「段甲追加」互斥）；是否於放行後另行搬至主線 |
| `3` | 本報告 `§七` 之 `4`（`V-1(c)` traceback 行號差·類 II）——本節 `四` 已擴為 `V-0` 之全量逐項歸類，是否即結案 |
