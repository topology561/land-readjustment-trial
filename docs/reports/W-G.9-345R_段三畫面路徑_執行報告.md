# `W-G.9-345R`　段三之畫面路徑（方案乙·通用化）：執行報告

> **受單** ＝ CC（施工樹 `.claude/worktrees/wg9-287-construction-window-c202df`·detached）。**單** ＝ `docs/orders/W-G.9-345_重量單.md`（本批工項零入倉）。
> **開工態** ＝ 側支 `verify/W-G.9-343-k929b` ＝ `3914b6e76c45bfb0d9b6eff8a28af6020124e461`；主線 `wip/s1-endpart` ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`（**本批⛔ 動主線**；收工時仍 ＝ `6090a7f`）。
> **倉外出艙之所在** ＝ `C:\Users\admin\wg345out\`（⛔ 入倉·本報告所引之數皆為當場所量，其全文或摘要逐字載於本檔）。
> 本報告內之 `app.py` 列號一律綁 `b0c9edc`（工項五之 commit）；綁他態者另載。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 父 | 所改 | 推送 |
|---|---|---|---|---|
| 零 | `ac9aa8262075da4f01999dfd7c8a697d2192c27e` | `3914b6e` | `docs/orders/W-G.9-345_重量單.md`（新·`+346/−0`） | ✅ 側支 |
| 一 | `0ec1e429cbe7c8dcbe234a326aace73dd05a8a84` | `ac9aa82` | `CLAUDE.md`（`+16/−0`）；`verify/probes/probe_WG9340_main_synth.py`（替換·`+18/−11`）；`verify/probes/probe_WG9345_screen.py`（新·`+947/−0`） | ✅ 側支 |
| 三 | `877cbed464e27650a8138a6e626b21f826af1a24` | `0ec1e42` | `app.py`（`+2201/−2143`） | ✅ 側支（工項四全過後·分開之呼叫） |
| 五 | `b0c9edc999b8bc25ffa5f8615d65f87b8eba1a93` | `877cbed` | `app.py` `+333/−25`；`verify/run_verification.py` `+3/−2`；`verify/selection_pipeline.py` `+7/−0`；`verify/tools/y_dump_diff.py` `+3/−2`；`verify/wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py` 各 `+8/−5` | ✅ 側支（工項六全過後·分開之呼叫） |
| 七 | （本報告之 `commit`） | `b0c9edc` | 本檔（新） | ✅ 側支 |

逐 `commit` 生產碼判法（`git diff --name-only <父>..<commit>` 以四檔 regex 篩）：工項零／一 ⇒ 命中 `0` 行；工項三 ⇒ `app.py`；工項五 ⇒ `app.py`、`verify/run_verification.py`。
`commit` 訊息之首列皆與單逐字相同；另附 `Co-Authored-By` 尾列（承本側支 `W-G.9-344` 各 `commit` 之既例·見自解清單 `3`）。

---

## ② 停機款 `1`〜`13` 之三值

| # | 款（節略） | 期 | 實得 | 判 |
|---|---|---|---|---|
| `1` | 開工錨／追蹤檔變動 | 側支 `3914b6e`·主線 `6090a7f`·變動 `0` | `3914b6e…`／`6090a7f…`／`0`（施工樹 detach 後 `git status --porcelain --untracked-files=no` ＝ 空） | 🟢 未觸發 |
| `2` | 本單／`F4`／`F5` bytes·`sha256`；入倉 blob 逐位 | 單 `SELF_SHA256` 相符；`F4` `48501` B `e0c1c87c…`；`F5` `14971` B `9d2f461f…` | 單 `47371` B·`SELF_SHA256` 實算 ＝ 單載 `1bc28c14…`；`F4` `48501` B `e0c1c87c181c675d163226b9094f937b0b19e28faa6df4712046c50d305502b6` CR `0`；`F5` `14971` B `9d2f461ffd7c919b29e46fb991bdc5c4bdcc1060a0904250874110181f53271d` CR `0`；三者入倉後 `git cat-file blob`／`cmp` 逐位同 | 🟢 未觸發 |
| `3` | 塊 `P1` bytes·`sha256` | `2141` B `828643dd…` | `2141` B `828643dd730e3295253cc3a5c05708f2e81d76fbdb3cb065c8e10c68d593243c`（圍欄開列 `:217`·閉列 `:234`〔1-based〕） | 🟢 未觸發 |
| `4` | 工項二之任一期不符 | 見 ④ | 八項皆如期 | 🟢 未觸發 |
| `5` | 工項三改他檔／`VA-1` 非 `rc 0` | 恰 `app.py`；`rc 0` | 恰 `app.py`；`rc 0` | 🟢 未觸發 |
| `6` | 工項四任一閘不符 | 見 ④ | `VA-1`〜`VA-7` 全過 | 🟢 未觸發 |
| `7` | 工項五觸⛔ 檔／逾許可集 | ⊆ 許可集·⛔ 集交集 `∅` | 七檔皆在許可集；⛔ 集交集 `0` | 🟢 未觸發 |
| `8` | 工項六任一閘不符 | 見 ④ | `VB-1`〜`VB-13` 全過 | 🟢 未觸發 |
| `9` | 段三遇 `W-G.9-344 §三-2` 未定之情形 | 無 | 畫面／harness 之段三於 `3.5`／`0.0` 皆跑畢、無 `RuntimeError` | 🟢 未觸發 |
| `10` | `run_all` ✅→🔴 ≠ `0` | `0` | `VA-6` `0`；`VB-12` `0` | 🟢 未觸發 |
| `11` | CC 作「孰為正典」「應改為」之判，或改器／塊／命令 | 無 | 無（reviewer 所提三則 WARNING 照出艙·⛔ 據以改碼·見 ⑧） | 🟢 未觸發 |
| `12` | 推主線；工項三之父 ≠ 工項一；工項五之父 ≠ 工項三 | 否／`0ec1e42`／`877cbed` | 主線仍 `6090a7f`；`877cbed^` ＝ `0ec1e42`；`b0c9edc^` ＝ `877cbed` | 🟢 未觸發 |
| `13` | 新檔為 `git check-ignore` 所命中 | 否 | 單／`F4`／本報告之 `check-ignore` 皆 `rc 1`（未命中） | 🟢 未觸發 |

---

## ③ `F4`／`F5`／`P1` 之實得

- `F4`（`verify/probes/probe_WG9345_screen.py`）：`48501` B·`sha256` `e0c1c87c181c675d163226b9094f937b0b19e28faa6df4712046c50d305502b6`·CR `0`；入倉 blob 與來源逐位同。
- `F5`（`verify/probes/probe_WG9340_main_synth.py`·替換）：`14971` B·`sha256` `9d2f461ffd7c919b29e46fb991bdc5c4bdcc1060a0904250874110181f53271d`·CR `0`；被替換者之 blob（開工態）＝ `6c41d2a744ca26a2f42160fcb10b9640b9d81cea`（與單 `§一` 項 `3` 同）。
- `P1`：`2141` B·`sha256` `828643dd730e3295253cc3a5c05708f2e81d76fbdb3cb065c8e10c68d593243c`；`CLAUDE.md` `257775` → `259916` B；改前全檔為改後之嚴格前綴（`cmp` 同）、末 `2141` B 與 `P1` 逐位同；`numstat` 刪除欄 `0`。
- pre-flight（`probe_order_preflight.py docs/orders/W-G.9-345_重量單.md`）：`rc 0`；🔴 機械 `0` 項；🟡 `P-4` `3` 項（`:85`／`:289`／`:319`·與單 `§五-1` 項 `5` 所具名豁免者同列）；ℹ️ `P-5` 相符、`P-3` `def main` ＝ `15579`–`25246`（開工態）。
- 取號（`wg9268_gate6_occupancy.py 3914b6e W-G.9-345 W-G.9-344 W-G.9-395`·母體 全 `docs/` `891` 檔·讀不到 `20`＝git 失敗 `0`＋解碼失敗 `20`）：受詢 `W-G.9-345` 嚴格／寬式 `D1/D2/D3` 六數 ＝ `[0,0,0,0,0,0]`·鬆框 `0／0`；對照甲 `W-G.9-344` `4／5／4`·列框 `9`·檔框 `4`·鬆框 `4／32`；對照甲′ `W-G.9-395` 宣告框 `0`·鬆框 `2／2`；對照乙 `W-G.9-963` 全 `0` ⇒ 與單 `§零-1` 表逐格同。
- `issuer_anchor … 523 522`（開場）：`rc 0`。

---

## ④ 工項二、四、六之全部出艙

### 工項二（改前態·`<base>` ＝ `0ec1e42`）

| 項 | 命令 | 期 | 實得 |
|---|---|---|---|
| `1` | `F4 selftest` | `rc 0`·`10/10` | `rc 0`·`selftest 10/10 ⇒ ✅` |
| `2` | `F4 census <repo> <base>` | `rc 0`；去 `\r` 後除首列外與附錄甲逐位同 | `rc 0`；逐位同（`14`／`14` 列） |
| `3` | `F4 ast <repo> <base>` | `rc 1` | `rc 1`（`A1`×2、`A4` 紅；`A5` `294／294` ✅） |
| `4` | `parity 3.5 off`／`parity 3.5 on`／`wiring`／`f4ctx`／`wfctx 3.5` | 皆 `rc 3` | 皆 `rc 3`（受詞缺） |
| `5` | `F5 <repo>` | `rc 0`·「app 側宿主 ＝ main」 | `rc 0`·`ℹ️ app 側宿主 ＝ main`·丙部四突變 ✅·器紅 `0` |
| `6` | `F2 selftest` | `rc 0`·`9/9` | `rc 0`·`9/9` |
| `7` | `F2 run … 3.5 on`／`0.0 on` | 皆 `rc 0` | 皆 `rc 0`（`pre_on_3.5.json`／`pre_on_0.0.json`） |
| `8` | `run_all`（倉外 `C:\Users\admin\wg345P` @ `0ec1e42`） | `rc 1`；`64` 項 `30`／`34` | `rc 1`；`64` 項（框 `^\s*✅ PASS `／`^\s*🔴 FAIL `）`30`／`34`；`k* 六塊經驗錨3.5m {'R1': 1, 'R2': 8, 'R3': 7, 'R4': 1, 'R5': 7, 'R6': 6}` |

`census.txt` 全文：

```text
【F4 census】基準 0ec1e429cbe7c8dcbe234a326aace73dd05a8a84·app.py 1504096 B

## If@21154–21756（test 含 '執行第 1 宗街角地優先權選位（左右側獨立）'）
  main 區域自由變數（10）：['B_value', 'C_for_calc', '_build_blocks', '_corner_rows_init', '_pd', 'build_parcels', 'post_price_by_block', 'pre_price_by_zone', 'sb_rows_by_label', 'temp_parcels']
  本體所寫之 session 鍵（11）：['f3L_corner_side_warnings', 'f3L_corner_winners', 'f3L_forced_offset', 'f3_corner_winners', 'f3_current_pk_block', 'f3_k6b_dual_side_assign', 'f3_k6b_stage1_locked_by_block', 'f3_k6b_stage1_locks', 'f3_k6b_stage2_order', 'f3_pk_alloc_depth', 'f3_pk_legal_min_width']
  可達之模組層函式（36）中讀寫 session 者：{'_estimate_G_for_qualification': ['st'], '_first_corner_alloc_dir': ['_st_fc'], 'select_corner_lots_both_sides_v12': ['_st_B4', '_st_cr6', '_st_wb5']}
  可達之模組層函式所寫之 session 鍵：{'select_corner_lots_both_sides_v12': ['f3_corner_range_areas', 'f3_corner_range_polys']}
  可達之模組層函式所改之模組層全域容器：{}

## If@22110–23652（test 含 '_btn_clicked or _auto_recalc'）
  main 區域自由變數（13）：['B_value', 'C_for_calc', '_auto_recalc', '_btn_clicked', '_new_params', '_param_key', '_tab6_burden', 'block_meta_by_label', 'build_parcels', 'classified_blocks', 'post_price_by_block', 'pre_price_by_zone', 'sb_rows_by_label']
  本體所寫之 session 鍵（9）：['f3_G_trace', 'f3_G_values', 'f3_forced_offset_diag', 'f3_g_iter_diagnostics', 'f3_g_needs_rerun', 'f3_k94_baseline_touch', 'f3_offset_fragments_merged', 'f3_stage2_placed', 'f3_wd2_pool_diag']
  可達之模組層函式（63）中讀寫 session 者：{'_first_corner_alloc_dir': ['_st_fc'], 'bl_pts_by_label': ['st']}
  可達之模組層函式所寫之 session 鍵：{}
  可達之模組層函式所改之模組層全域容器：{'k917_note_drop': ['K917_DROPPED.setdefault']}
```

### 工項四（於 `877cbed` 量·`<base>` ＝ `0ec1e42`）

| 閘 | 期 | 實得 | 判 |
|---|---|---|---|
| `VA-1` `F4 ast` | `rc 0`；`12` 列全 ✅；`A2` `2`／`49`；`A3` `10`／`13`；`A5` `294`／`294` | `rc 0`；`12` 列全 ✅；`A2` `2`／`49`；`A3` `10`／`13`；`A5` `294`／`294`；`A6` 全域參照 `31`／`51` | ✅ |
| `VA-2` `parity 3.5 off`／`0.0 off` | 皆 `rc 0`；session 鍵 `10` 列 ✅；配地 `68／67`、`63／62`·不符 `0`；`Z` ＝ `[('harness','R1-抵費地-2')]` | 皆 `rc 0`；`10` 列 ✅；`68／67`、`63／62`·不符 `0`；`Z` 同 | ✅ |
| `VA-3` `parity 3.5 off --perturb` | `rc 1` | `rc 1`（配地列不符格 `287`·不符 `2` 項） | ✅ |
| `VA-4` `git diff --name-only 0ec1e42 877cbed` | 恰 `app.py` | 恰 `app.py` | ✅ |
| `VA-5` 五器 | 皆 `rc 0`；`wfns_ast` `40`／`40`／`39`；`F5` 宿主 ＝ `f3_screen_stepg_run`·丙部四 ✅ | `issuer_anchor` `0`／`closegate 523 522 .` `0`／`wfns_ast` `0`（`40`／`40`／`39`）／`F5` `0`（`ℹ️ app 側宿主 ＝ f3_screen_stepg_run`·丙1〜丙4 ✅·器紅 `0`）／`probe_WG9341_synth` `0` | ✅ |
| `VA-6` `run_all`（同一倉外路徑 `C:\Users\admin\wg345P` @ `877cbed`）＋ `runall` 對拍 | `run_all` `rc 1`；`runall` `rc 0`；相異 `0` | `run_all` `rc 1`（`30`／`34`）；`runall` `rc 0`；相異 `0`；另全 log `diff` 差 **`0` 列** | ✅ |
| `VA-7` `F2 run`＋`cmp`（`3.5`／`0.0`） | 二 `cmp` 皆 `rc 0` | 二 `cmp` 皆 `rc 0`（相異 `0` 項） | ✅ |

`runall_cmp_A.txt` 全文：

```text
【runall】項 64／64·PASS 30 → 30·FAIL 34 → 34
  相異項 0；其餘 64 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／34 → 22／34；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
```

### 工項六（於 `b0c9edc` 量）

| 閘 | 期 | 實得 | 判 |
|---|---|---|---|
| `VB-1` `parity 3.5 on` | `rc 0`；紀錄 `18`、段二序 `13` ✅；temp `126`／build `57` ✅；`K917` ✅；回復 ✅；配地 `60／59`·不符 `0`；`Z` 同 | 全如期（`B_on_3.5.json`：`n_rows [60, 59]`·`bad 0`·`stage3_log` `18` 列） | ✅ |
| `VB-2` `parity 0.0 on` | `rc 0`；紀錄 `0`；`63／62`；`Z` 同 | 全如期（build `61`） | ✅ |
| `VB-3` `parity 3.5 s3off` | `rc 0`；紀錄 `0`；build `61`；`68／67` | 全如期（段二序 `13` 列） | ✅ |
| `VB-4` `parity 3.5 off`／`0.0 off` | 同 `VA-2` | `68／67`、`63／62`·不符 `0`·`Z` 同 | ✅ |
| `VB-5` `parity 3.5 on --perturb` | `rc 1` | `rc 1`（紀錄與段二序二鍵紅、配地列不符格 `273`·不符 `3` 項） | ✅ |
| `VB-6` `wiring` | `rc 0`；`W0`〜`W8` ✅（`W4` `5／5`；`W6` `2／4`）；丙部四突變皆 ✅ | 全如期；器紅 `0` | ✅ |
| `VB-7` `f4ctx`；`wfctx 3.5`／`0.0` | 皆 `rc 0`（T1 `116`／`126` 片） | 皆 `rc 0`；`T1` `116`／`126`；`T2`／`T2′`／`T3` 皆 raise 且含「重跑」；段三改動之 temp 片數 `10`／`0` | ✅ |
| `VB-8` `F2 selftest`；`run`＋`cmp`（對工項二） | `9/9`；二 `cmp` `rc 0` | `9/9`；二 `cmp` 相異 `0` | ✅ |
| `VB-9` `F3′ selftest`；`run … 3.5 on` | `13/13`；`rc 0` | `13/13`；`rc 0` | ✅ |
| `VB-10` 三 smoke（工項五樹 vs 工項一樹·後者 = 倉外 `C:\Users\admin\wg345Q` @ `0ec1e42`） | 最末例外逐字同（去 `File` 列之末 `12` 列）；行號差唯所改之 smoke 自身 | 三者皆 `rc 1`；末 `12` 列逐字同；最末列皆 `RuntimeError: 🔴 run_step_g：`cad['baselines']` 為空——…`；`File` 列 `5`／`5`，行號差唯 `wg_g1_smoke.py` `106/103`·`92/89`、`wg_g2_smoke.py` `113/110`·`61/58`、`wg_g3.py` `179/176`·`127/124`（皆 `+3`） | ✅ |
| `VB-11` 所改之檔；`+` 列 regex | ⊆ 許可集·⛔ 集 `∅`；regex `0` | 七檔 ⊆ 許可集；⛔ 集交集 `0`；regex 命中 `0` | ✅ |
| `VB-12` `run_all`（同一倉外路徑 @ `b0c9edc`）＋ `runall` 對拍 | `rc 1`；`rc 0`；`64／64`·`30→30`·`34→34`；✅→🔴 `0`；相異限於 `run_verification.py` 之 traceback 行號 | `run_all` `rc 1`；`runall` `rc 0`；`64／64`·`30→30`·`34→34`；✅→🔴 `0`；相異 `1` 項（`#64 W-G G.2`）——歸因見下 | ✅ |
| `VB-13` 五器 | 皆 `rc 0` | 皆 `rc 0`（`wfns_ast` `40／40／39`；`F5` 宿主 ＝ `f3_screen_stepg_run`·丙1〜丙4 ✅） | ✅ |

`runall_cmp_B.txt` 全文：

```text
【runall】項 64／64·PASS 30 → 30·FAIL 34 → 34
  #64 W-G G.2 世代幾何曝出契約 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  相異項 1；其餘 63 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／34 → 22／34；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
```

**`VB-12` 相異項之逐項歸因**：`runall_before.log` 對 `runall_B.log` 之全 log `diff` ＝ **`2` 處、各 `1` 列**，全文：

```text
1120c1120
<   File "C:\Users\admin\wg345P\verify\run_verification.py", line 1460, in main
---
>   File "C:\Users\admin\wg345P\verify\run_verification.py", line 1461, in main
1225c1225
<         現況:   File "verify/run_verification.py", line 1460, in main
---
>         現況:   File "verify/run_verification.py", line 1461, in main
```

⇒ 二處皆為 `#64 W-G G.2` 之 traceback 行號 `1460 → 1461`（其一在對帳段），由 `verify/run_verification.py` 之淨增 `1` 列（工項五之註解列）所致；與單 `§五-2` 項 `4` 之發單側雛形逐字相同。**他差 `0`。**

### 各 `parity` 之 `json` 摘要（`C:\Users\admin\wg345out\*.json`）

| 檔 | 態 | 退縮 | 模式 | `n_rows`（harness／畫面） | `Z` | `bad` | 段三紀錄 |
|---|---|---|---|---|---|---|---|
| `VA2_3.5_off.json` | `877cbed` | `3.5` | off | `68／67` | `[['harness','R1-抵費地-2']]` | `0` | — |
| `VA2_0.0_off.json` | `877cbed` | `0.0` | off | `63／62` | 同 | `0` | — |
| `B_on_3.5.json` | `b0c9edc` | `3.5` | on | `60／59` | 同 | `0` | `18` 列 |
| `B_on_0.0.json` | `b0c9edc` | `0.0` | on | `63／62` | 同 | `0` | `0` 列 |
| `B_s3off_3.5.json` | `b0c9edc` | `3.5` | s3off | `68／67` | 同 | `0` | `0` 列 |
| `B_off_3.5.json` | `b0c9edc` | `3.5` | off | `68／67` | 同 | `0` | — |
| `B_off_0.0.json` | `b0c9edc` | `0.0` | off | `63／62` | 同 | `0` | — |

（另 `pre_commit_on_3.5.json`：工項五改動未 commit 時之預檢，其 `head` 欄記 `877cbed`〔工作樹之 HEAD〕、內容為改後之工作樹；`60／59`·`bad 0`·`18` 列。⛔ 作閘。）

---

## ⑤ `§三-7` 呼叫端處置表

**母體** ＝ `b0c9edc` 之 `app.py` `def main()` 內：`Name` `temp_parcels`／`build_parcels` 之 `Load`，及字面 `'f3_temp_parcels'`／`'f3_build_parcels'` 之出現（`ast` 實查·共 **`47`** 處·含 `21401`／`23166` 二列之賦值右側）。分類：**甲** ＝ 段三後；**乙** ＝ 段三前（重劃前母數）；**丙** ＝ 段三前（顯示重劃前之地）。

| 列 | 受詞 | 步驟 | 類 | 由 |
|---|---|---|---|---|
| `21396`／`21400`／`21401` | `temp_parcels`；session `f3_temp_parcels` 之寫 | 步驟 C（暫編地號之產生） | 乙 | 段三前之 temp 之**生成**與存 session（段三之輸入） |
| `21414`／`21420`／`21501`／`21689`／`21723`／`21732`／`21775`／`21778` | `temp_parcels` | 步驟 C（產生數·ghost 診斷·問題宗·歸戶交叉檢核） | 丙 | 重劃前之地之檢核與顯示 |
| `21785`／`21794`／`21799`／`21831`／`21840`／`21865`／`21945`／`22161`／`22213` | `temp_parcels` | 步驟 C-2（圖面定位·高亮·點選） | 丙 | 重劃前之地之圖面 |
| `22090`／`22096` | session `f3_temp_parcels` 之讀寫 | 步驟 C-2 | 乙 | 段三前 temp 之手動修正（段三之輸入） |
| `22519`／`22530`／`22559`／`22573`／`22614`／`22624`／`22644`／`22746`／`22754` | `temp_parcels` | 步驟 D（重劃前地價區段標註） | 乙 | 重劃前地價區段（重劃前母數·`a′` 之單價來源） |
| `23093`／`23161` | `temp_parcels` | 步驟 G（build 之生成） | 乙 | 自段三前之 temp 篩出段三前之 build |
| `23166`／`23168` | `build_parcels`；session `f3_build_parcels` 之寫 | 步驟 G | 乙 | 段三前之 build 存 session（`_build_wf_ctx` 之指紋與 F.4 `p_avg` 之母體） |
| `23621`／`23625` | `build_parcels`／`temp_parcels`（`pk_kwargs`） | 步驟 L（街角選位 → `f3_screen_k6b_stage3`） | 乙 | 段三之輸入（`temp0`／`build0`） |
| `23687` | `build_parcels` | 步驟 L（街角點選圖之可點擊 trace） | 丙 | 街角點選之圖面（重劃前之宗地） |
| `23909` | `build_parcels` | 步驟 L（`_seed_rows`·逐宗參數表） | 丙 | 逐宗手動參數表之列（依段三前之 build 列出；配地以暫編地號查之） |
| `24000` | `build_parcels`（經 `k6b_screen_build_for_g`） | 配地 | 甲 | 段三後之 build（指紋不符 ⇒ loud） |
| `24823` | `build_parcels`（`k6b_stage3_selected` 之指紋受詞） | 步驟 M | 乙 | 指紋綁段三前之 build |
| `24829` | `temp_parcels`（`_tp_m` 之「無段三結果」分支） | 步驟 M | 乙 | 無段三結果 ⇒ 同改前 |
| `_tp_m` 之 `4` 讀（M-1 依街廓分組·M-1 歸戶持分·M-4 公設片選取·M-4 歸戶相鄰建地） | `_tp_m` | 步驟 M | 甲 | 段三後之 temp 去 `段三併出`（`W-G.9-344` 補令一 裁三） |
| `25295` | `temp_parcels` | 步驟 M（M-4「歸戶自有土地」圖示·其上三列含 `_gid_parcel_set`） | 丙 | 重劃前之地之圖示（單 `§三-3` 第 `5` 項明定照舊） |
| `25393` | `temp_parcels` | 步驟 I（推送至地價區段分析·區段彙總） | 乙 | 依重劃前地價區段彙總之重劃前面積 |
| `25523` | session `f3_build_parcels` | 七級調配（`k6b_f4_ctx`） | 乙 | F.4 模式二 `p_avg` 之母體 ＝ 重劃前 |

**harness 側**：

| 所在 | 受詞 | 類 | 由 |
|---|---|---|---|
| `app.py` 七級調配之 `_wf4.compute` | `k6b_f4_ctx(_cbt, {_tag: _wg_ss['f3_build_parcels']})` | 乙 | 模式二 `p_avg` |
| `verify/run_verification.py` F.4 | `k6b_f4_ctx(_ctx, {_t: build_parcels for _t in _ctx})` | 乙 | 原始 `build_parcels` |
| `verify/wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py` 之 `wf_f4.compute` | `k6b_f4_ctx(cbt, {tag: build})`（`build` ＝ 呼叫 `run_corner_pk_k6b` 前者） | 乙 | 同上 |
| 三 smoke 之 seed | `f3_temp_parcels`／`f3_build_parcels` ＝ 段三前；`f3_k6b_stage3_temp`／`_build` ＝ 段三後；`f3_k6b_stage3_fp` ＝ `k6b_stage3_fingerprint(段三前之 build, setback)` | 甲／乙 | 與畫面同形 ⇒ `_build_wf_ctx` 所出之 `build`／`temp` 與改前同（`VB-7` `wfctx` `T1` 承擔判別力；三 smoke 於開工態即終止於 `run_step_g`·`VB-10`） |
| `verify/run_verification.py` G.1 之 seed | 未改 | — | 單 `§三-5` 項 `5` |

---

## ⑥ `§三-2` 步驟 `6` 之隔離鍵實數與其驗

- `K6B_SCREEN_TRIAL_KEYS` ＝ **`23`** 鍵（相異 `23`）＝ 街角選位本體所寫 `11` ＋ `select_corner_lots_both_sides_v12` 所寫 `2` ＋ 配地本體所寫 `9` ＋ `f3_corner_cand_diag` `1`。
- **實測**（倉外腳本·harvest·`3.5 on`·包 `k6b_stage3_run` 記其進入時之 session、於終趟 `f3_screen_corner_pk_run` 進入時比對）：試算前 session 已有者 **`14`**（存其深拷貝：街角選位所寫 `11` ＋ `f3_corner_range_areas`／`f3_corner_range_polys` ＋ `f3_corner_cand_diag`）；未有者 **`9`**（配地所寫之 `9`·試算後刪之）；**試算後（終趟前）逐鍵回復 `23／23`**；`K917_DROPPED` 回復 `True`；`ran` ＝ `True`·紀錄 `18` 列·段二序 `13` 列。
- `VB-1` 之「session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵」 ✅（`F4` 之判準）。

---

## ⑦ 抽出之機械法（腳本⛔ 入倉）

1. 以 `F4` 之 `free_main_locals` 定位二 If 與其自由變數（甲 `10`／乙 `13`·與附錄甲同）。
2. 本體範圍 ＝ `If.test.end_lineno + 1` 至 `If.end_lineno`（含本體首句前之註解；二 If 皆無 `orelse`）。
3. 去縮排量 ＝ 本體首句之 `col_offset` − `4`（二者皆 `20 − 4 ＝ 16`）；以 `tokenize` 標出多列字串（含 f-string 之 `FSTRING_START…END`）之續列 `2880` 列，**續列一字不動**，餘列統一去 `16` 格。
4. 新函式 ＝ `def f(st, *, <自由變數·依名排序>):` ＋ 一列 docstring ＋ 本體；置於 `# ============ 主程式 ============` 橫幅之上（見自解清單 `2`）。
5. `main()` 內二 If 之本體換為單一呼叫 `f(st, <名>=<名>, …)`（由後往前換，免行號位移）。
6. 抽出前另查二類 `ast` 盲點（`F4 ast` 之 `A1`〜`A6` 不及者）：(a) 本體所賦之名於 If 之後被 `main()` 所讀而其間無再賦值 ⇒ **`0`**（`353` 處讀皆有其後之再賦值）；(b) 本體內「先讀後賦」之 `main()` 區域名 ⇒ **`0`**；(c) 二 If 之祖先鏈無迴圈（皆為 `10` 層 If）。
7. 工項五以另一腳本施之：每處替換皆斷言命中恰 `1`；`main()` 內之 `g_kwargs` `9` 名與步驟 M 之 `build_parcels`／`temp_parcels`，另以祖先鏈支配查其於呼叫點皆已賦值（皆 ✅）。

---

## ⑧ reviewer 之出艙

### 工項三（`877cbed`·獨立 reviewer·唯讀）

判：**7 項全 PASS**；「nothing I found would change runtime behaviour」。要點：`A2` 本體 ast 全等（`2`／`49`）；參數集以其自寫之 symtable 算得 `10`／`13` 恰同；`main()` 以呼叫替換後 ast 全等；模組層其餘 `294` 節點同序；(6a) 本體所賦而其後被讀之名，每讀皆有其後之再賦值；(6b) 先讀後賦 `0`；(6c) 無 `global`／`nonlocal`／`yield`／區塊層 `return`／`break`／`continue`；(6d) 無迴圈祖先；(6e) `st` 為模組全域；(6f) 新函式之全域參照 `31`／`51` 皆有定義。字串常數 `12666 → 12668`（唯二 docstring）；f-string `1520` 同多重集；變更列皆恰去 `16` 格。NOTE：錯誤分支之 `format_exc()` 文字因多一層函式框而異（僅顯示）；`st.stop()`／`st.rerun()` 之例外多穿一層框（無語意影響）；6a 係列序＋人工抽讀，非完整支配證明；本變更在 `main()` 內，**靜態檢查不代替驅動二按鈕之合成案或 UI 實跑**。

### 工項五（`b0c9edc`·獨立 reviewer·唯讀）

判：**8 項皆 PASS（依單之字面）**；另具名三則 WARNING（照錄要旨·⛔ 據以改碼·候發單側）：

- **W-A**：`k6b_stage3_run` 丟出 `RuntimeError` 以外之例外（如 `KeyError`、shapely 之錯），或首趟／終趟之 `st.stop()`，皆⛔ 留 `f3_k6b_stage3_error`、亦無指紋 ⇒ 下一次按「配地」時 `k6b_screen_build_for_g` 得 `None`，即以段三前之 build 配地而**無警示**。（該例外本身於當次會以 traceback 現於畫面。）
- **W-B**：試算之 winner／候選列自 session 讀回（harness 取 `run_corner_pk` 之回傳值）。街角選位本體於「土地歸戶為空」時**⛔ 寫任何鍵**，步驟 `1` 亦⛔ 去 `f3_k6b_stage2_order` ⇒ 該情形下段三可能吃前次之段二序。
- **W-C**：段三後 `finally` 回復舊之配地輸出（`f3_G_values` 等·算於段三前之 build），而 `_build_wf_ctx` 今以段三後之 build 配之（改前亦可不重跑配地，惟今宗地集不同）；步驟 M 之 `st.stop()` 於指紋不符時每次重跑皆停住其後之頁面，直至重跑街角選位。

其餘 NOTE：`alloc_state` 對試算中止回空列（harness 回 partial）——`k6b_stage3_run` 於 `err` 時必 raise ⇒ 列從不被讀，無影響；代理對 widget 回傳真值之物——二本體今⛔ 用任何 widget 之回傳值（`ast` `0` 處），為潛在風險；`app.py` 增 `333`／刪 `25`（雛形 `268`／`15`·非閘）。

---

## ⑨ 執行時間

| 項 | 秒 |
|---|---|
| `run_all` 改前（`0ec1e42`） | `624` |
| `run_all` A（`877cbed`） | `577` |
| `run_all` B（`b0c9edc`） | `596` |
| `parity 3.5 off`／`0.0 off`（`VA-2`） | `33`／`32` |
| `parity 3.5 off --perturb`（`VA-3`） | `30` |
| `parity 3.5 on`（預檢／`VB-1`） | `75`／`85` |
| `parity 0.0 on`／`3.5 s3off`／`3.5 off`／`0.0 off`（`VB-2`〜`VB-4`） | `31`／`31`／`32`／`32` |
| `parity 3.5 on --perturb`（`VB-5`） | `87` |
| `F2 run 3.5 on`／`0.0 on`（工項二） | `63`／`32` |
| 三 smoke（各樹各支） | `22`〜`23` |

---

## ⑩ CC 之自捕

1. **`main()` 盲區之補查**：`F4 wiring`／`parity` 皆⛔ 執行 `main()`（`CLAUDE.md`「`main()` 內之敘述，`run_all` 不得單獨作為驗收依據」）。工項五接線前，另以 `ast` 祖先鏈支配查 `main()` 內街角選位呼叫點之 `pk_kwargs` `10` 名與 `g_kwargs` `9` 名（`_param_key` 等原僅供配地者）、步驟 M 之 `build_parcels`，皆於呼叫點前已賦值 ⇒ 真 UI 下⛔ 生 `UnboundLocalError`。🔴 **惟本批仍⛔ 附驅動真 Streamlit 之合成案**——畫面路徑之活體驗證僅及 harvest 之二函式與段三入口（`F4 parity`），`main()` 內之接線本身僅有 `AST` 級之證（`W1`〜`W8`）。
2. **抽出之 `ast` 盲點**（見 ⑦ 項 `6`）：`A1`〜`A6` 不查「本體所賦之名於其後被 `main()` 讀」與「先讀後賦」；本批自查皆 `0`，reviewer 獨立復現同。
3. **`VA-6` 改前 vs 工項三之全 log `diff` ＝ `0` 列**（同一倉外路徑之效）。

### 本批之自解清單（`作業常規之追加五`）

| # | 疑義（逐字） | 讀法 | 所取 | 機械證據 | 所棄之由 |
|---|---|---|---|---|---|
| `1` | 「三來源檔（KL 置於 **CC 之施工樹之根**·檔名逐字）」 | (a) 本施工樹（worktree）之根；(b) 倉之主 checkout 之根 | (b)：自 `C:\Users\admin\Desktop\land-readjustment-trial\` 二進位複製（⛔ 改該處任何檔） | 本施工樹之根無此三檔（`ls` 實查）；三檔 bytes／`sha256` 與 `§五-1` 逐位符 ⇒ 傳輸保真未破 | (a) 無檔可取 |
| `2` | 「新增於模組層、**緊接於 `def main():` 之前**」 | (a) `def main():` 之正上一列（使 `# ============ 主程式 ============` 橫幅與 `main` 分離）；(b) 該橫幅之上 | (b) | `F4 ast` `A5` `294／294` ✅、`A1`〜`A6` 全綠；二讀法之 `ast` 全同（註解非節點）；reviewer 證橫幅仍緊貼 `def main():` | (a) 使橫幅所標之「主程式」改指新函式 |
| `3` | 「`commit` 訊息逐字 …」 | (a) 僅該列；(b) 該列 ＋ `Co-Authored-By` 尾列 | (b) | 首列與單逐字同；本側支 `W-G.9-344` 各 `commit` 皆附同一尾列（`git log -5 3914b6e` 實查） | (a) 與側支既例相異 |
| `4` | 「`_new_params=dict(session[g_kwargs['_param_key']] 或 {})`」 | (a) 下標（鍵缺 ⇒ `KeyError`）；(b) `.get(…) or {}` | (b) | `F4` 之畫面側亦以 `.get(…, {}) or {}` 組之；`VB-1` ✅ | (a) 首次開頁時該鍵可能尚未寫入（`main()` 之寫入點在街角選位之後），將使段三於首輪即 `KeyError` |
| `5` | 倉外 `run_all` 之路徑 `<P>` 與 `VB-10` 之「工項一之施工樹」未具名 | — | `<P>` ＝ `C:\Users\admin\wg345P`（三跑同一路徑·跑畢 `git worktree remove --force`）；工項一樹 ＝ `C:\Users\admin\wg345Q`（跑畢移除） | `VA-6` 全 log 差 `0`；`VB-12` 差唯行號 | — |

（規格未定而屬實作細節者，非自解、照實具名：① `k6b_screen_build_for_g`、步驟 M、段三入口步驟 `7` 之 `st.stop()` 之後另 `raise`——真 Streamlit 之 `st.stop()` 恆不返回 ⇒ 無作用，僅防代理之 `stop` 返回時靜默續行；② 試算代理將 `error`／`warning` 之訊息記於 `msgs`（⛔ 顯示），供停機訊息；③ 三試算以 `redirect_stdout` 收其印出（同 harness）；④ 段三紀錄表以逐格 `str()` 後交 `st.dataframe`（紀錄含 list／dict 與 `'—'`／int 混型）。）

---

## ⑪ 下一 CC 窗須知

1. **側支之端** ＝ 本報告之 `commit`（其父 `b0c9edc`）；主線仍 `6090a7f`。**入主線須另候 KL 放行**（與 `K-9-29 二` 同批·單 `§二` 射程 `(c)`）。
2. 🔴 **畫面路徑之真 UI 驗收未做**：本批證據止於 harvest 之二函式與段三入口（`F4 parity`·與 harness 逐鍵同）及 `main()` 接線之 `AST`（`F4 wiring`）。KL 以 UI 實跑前，須先令其對拍 `git hash-object app.py`（主 checkout 之 `git status` 對 `app.py` 之變動可能全盲）。
3. reviewer 之 **W-A／W-B／W-C**（⑧）待發單側裁；本批⛔ 據以改碼。
4. `F5`（`probe_WG9340_main_synth.py`）之「app 側宿主」自本批起為 `f3_screen_stepg_run`。
5. `run_all` 之 `#64 W-G G.2` traceback 行號已為 `1461`（原 `1460`）；以行號對拍之既有紀錄須知此移。
6. 倉外之出艙（`C:\Users\admin\wg345out\`）⛔ 入倉；本報告已載其全文或摘要。
