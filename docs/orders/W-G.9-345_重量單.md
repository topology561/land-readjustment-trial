# `W-G.9-345`　重量單：段三之畫面路徑（方案乙·通用化）——畫面「街角選位」「配地」二段之原封抽出 ＋ 段三畫面入口 ＋ 下游母體之分流（F.4 模式二 `p_avg`·七級調配 ctx·步驟 M）＋ `y_dump_diff.py` 之改接 ＋ 量測器入倉

> **發單** ＝ 發單側窗四十一·`2026-09-26`。**受單** ＝ CC 新窗（於 **CC 之施工樹**施工·⛔ 於 KL 之主 checkout）。
> **級** ＝ **重**（生產碼：`app.py`〔`def main()` 內二按鈕區之本體抽為模組層函式·其呼叫點·段三畫面入口·`_build_wf_ctx`·`_f3L_invalidate_g_cache`·七級調配之 F.4 呼叫·步驟 M 之宗地母體〕；`verify/selection_pipeline.py`；`verify/run_verification.py`；`verify/wg_g1_smoke.py`；`verify/wg_g2_smoke.py`；`verify/wg_g3.py`；`verify/tools/y_dump_diff.py`）。
> **開工態** ＝ 側支 `verify/W-G.9-343-k929b` ＝ `3914b6e76c45bfb0d9b6eff8a28af6020124e461`；主線 `wip/s1-endpart` ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`（**本單⛔ 動主線**）。
> **KL 放行** ＝ 見 `§二`（射程：本單之一切 `commit` 推至**側支** `verify/W-G.9-343-k929b`；**入主線另候 KL 放行**）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `P1` 以**檔案管線**、依**圍欄之逐列索引**機械抽取；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。Windows 下 `<repo>` 一律以反斜線傳入。
> 🔑 **三來源檔**（KL 置於 **CC 之施工樹之根**·檔名逐字）：`W-G.9-345_重量單.md`（本單）／`probe_WG9345_screen.py`（檔 `F4`）／`probe_WG9340_main_synth.py`（檔 `F5`·既有器之改版）。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **`run_all` 一律於倉外之拋棄式 worktree 跑，且改前、改後用<u>同一倉外路徑</u>**（`git worktree add --detach <P> <commit>`；跑畢 `git worktree remove --force <P>`；再以同一 `<P>` 建下一態）——⛔ 路徑相異，traceback 之路徑列即成假差（發單側窗四十一實見）。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0` 與 `WV_K6B_STAGE3`（先以 `python -c "import os;print(os.environ.get('WV_K6_STEP0'),os.environ.get('WV_K6B_STAGE3'))"` 出艙 `None None`）；器 `F2`／`F4` 於行程內自設旗標。
> 🛑 **本單⛔ 及於**：`verify/stepg_pipeline.py`；`verify/wf_f0.py`〜`wf_f4.py`；`verify/app_harvest.py`；`verify/run_all.py`；`verify/baselines/**`；既有量測器（`F5` 所替換者除外）；`K-9-48` 七項 `3`／`5`／`6` 之實作；入池閘；任何錨之改；`baselines` 之重烤；`K-6` 典／`GB` 簿／自誤簿／`VR` 簿／恆常附款簿；主線。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight・容量停

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量；預估不足以辦畢工項零〜七者，先辦至工項四止（見 `§零-4`）。
2. `git fetch origin`；`git rev-parse origin/verify/W-G.9-343-k929b` ＝ `3914b6e76c45bfb0d9b6eff8a28af6020124e461`、`git rev-parse origin/wip/s1-endpart` ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`；施工樹 `git checkout --detach origin/verify/W-G.9-343-k929b` 後 `git status --porcelain` 之追蹤檔變動 ＝ `0`（施工樹之根之三來源檔為未追蹤檔·⛔ 計）。
3. `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 523 522` ⇒ `rc 0`。

### `§零-1`　取號現查（宣告框·補款 `①`〜`⑨`）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態（`3914b6e`）之 `docs/` 全檔 **`891`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗四十一實跑 `python verify/probes/wg9268_gate6_occupancy.py 3914b6e W-G.9-345 W-G.9-344 W-G.9-395`：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-345`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-344` | `4`／`5`／`4` | `4`／`5`／`4` | `9` | `4` | `4`／`32` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-395` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`2` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 |

本單⛔ 鑄任何號（自誤／`GB`／`VR`／`K-9`）。本單入倉後，`W-G.9-345` 之命中當含本單自身（白名單 `1`·⛔ 撞號）。

### `§零-2`　停機款（三值·`n`）

| # | 款 | 初態 |
|---|---|---|
| `1` | 開工時側支 ≠ `3914b6e` 或主線 ≠ `6090a7f`，或追蹤檔有變動（接續時依 `§零-4`） | 🛑 未執行 |
| `2` | 本單或檔 `F4`／`F5` 之 bytes／`sha256` 與 `§五-1` 不符；或入倉後 `git cat-file blob` 與來源不逐位相同 | 🛑 未執行 |
| `3` | 塊 `P1` 之 bytes／`sha256` 與 `§五-1` 不符 | 🛑 未執行 |
| `4` | 工項二之任一期不符 | 🛑 未執行 |
| `5` | 工項三之 `commit` 改動 `app.py` 以外之檔，或 `VA-1`（`F4 ast`）⛔ `rc 0` | 🛑 未執行 |
| `6` | 工項四之任一閘不符（`§五` `VA-*`） | 🛑 未執行 |
| `7` | 工項五之 `commit` 觸及 `§三-6` 之⛔ 檔，或所改之檔 ⊄ `§三-6` 之許可集 | 🛑 未執行 |
| `8` | 工項六之任一閘不符（`§五` `VB-*`） | 🛑 未執行 |
| `9` | 段三（畫面或 harness）之執行遇 `W-G.9-344 §三-2` 未定之情形——一律 loud 停機，⛔ 自擬規則續辦 | 🛑 未執行 |
| `10` | `run_all` 二態對拍之 ✅→🔴 ≠ `0`（`VA-6`／`VB-12`）——⛔ 自判其當否，逐項出艙後停機 | 🛑 未執行 |
| `11` | CC 作任何「孰為正典」「應改為」之判，或改 `F4`／`F5`、塊、附錄、命令一字以求其過 | 🛑 未執行 |
| `12` | 任一 `commit` 推至**主線**；或工項三之 `commit` 之父 ≠ 工項一之 `commit`；或工項五之 `commit` 之父 ≠ 工項三之 `commit` | 🛑 未執行 |
| `13` | 本批任一新檔為 `git check-ignore` 所命中 | 🛑 未執行 |

### `§零-3`　pre-flight 機檢之逐項處置（`W-G.9-190R §九（甲）`·⛔ 靜默略過）

| 項 | 性質 | 實得 | 處置 |
|---|---|---|---|
| `P-3`／`P-5` | 機械可判·停機款 | 見 `§五-1` 項 `5` | 🟢 通過 |
| `P-1`／`P-2`／`P-4`／`P-6` | 文字啟發式·⛔ 停機款 | 見 `§五-1` 項 `5` | 逐項具名 |

受單側收單時須自倉重跑 `python verify/probes/probe_order_preflight.py docs/orders/W-G.9-345_重量單.md` 並逐項再處置；`rc ≠ 0` ⇒ **停機回報**。

### `§零-4`　容量停與接續

1. **觸發**：KL 告 CC「完成本項後停止」；或 CC 自判上下文將盡。
2. **處置**：完成當前工項（⛔ 留半套）⇒ 已完成且已過閘之 `commit` 推側支 ⇒ 於對話回報「已完成至工項 `k`」及逐 `commit` 之 hash。⛔ 寫報告檔。
3. **接續之證**：

| 工項 | 已落之證 |
|---|---|
| 零 | 側支有訊息「`W-G.9-345` 工項零」之 `commit`，且 `docs/orders/W-G.9-345_重量單.md` 之 blob 與來源逐位相同 |
| 一 | 側支有「`W-G.9-345` 工項一」之 `commit`，且 `F4`／`F5` 之 blob 與來源逐位相同、`CLAUDE.md` 之末端逐位等於塊 `P1` |
| 二 | ⛔ 產生 `commit`；出艙存倉外 ⇒ **接續時一律重做** |
| 三＋四 | 側支之端之訊息為「`W-G.9-345` 工項三」、其父 ＝ 工項一之 `commit`（已 `push` ⇒ 工項四已全過） |
| 五＋六 | 側支之端之訊息為「`W-G.9-345` 工項五」、其父 ＝ 工項三之 `commit` |
| 七 | 側支之端之訊息為「`W-G.9-345` 工項七」 |

4. 🛑 ⛔ 重辦已落之工項（工項二、四、六除外）；有疑 ⇒ 停機回報。

---

## `§一`　態錨（錨於 `3914b6e`·發單側窗四十一自倉實跑）

| # | 項 | 值 |
|---|---|---|
| `1` | 側支／主線 | 側支 `verify/W-G.9-343-k929b` ＝ `3914b6e76c45bfb0d9b6eff8a28af6020124e461`（其下 `a403842` ＝ `W-G.9-344` 工項三之生產碼）；主線 ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`；遠端 heads **`30`**（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`·`git ls-remote --heads origin` 實數） |
| `2` | 生產碼 blob | `app.py` ＝ `bbb6d1bf1cf72e18e9b0ff97f438f8e10d3afeef`；`verify/selection_pipeline.py` ＝ `fa27bb20d727e6982a24217fa9f3f64992594160`；`verify/run_verification.py` ＝ `3a2531c47178c07977f6afbbcc54580ef39504fa`；`verify/stepg_pipeline.py` ＝ `eb557b4bb3caeaf7ef2459dadc7919f3334a432e`；`verify/wg_g1_smoke.py` ＝ `960c3cbe3795e7e560caafcb2b15d2fe8eef2767`；`verify/wg_g2_smoke.py` ＝ `47f15388a23979db83c0a5aca53cc9be280c1c5a`；`verify/wg_g3.py` ＝ `9b33183ec995a243b635ee01480110e13d206392`；`verify/tools/y_dump_diff.py` ＝ `5ae0721aa1809b2fc650f3d62c54171c7c433226` |
| `3` | 既有量測器之 blob | `verify/probes/probe_WG9340_main_synth.py` ＝ `6c41d2a744ca26a2f42160fcb10b9640b9d81cea`（`F5` 所替換者）；`verify/probes/probe_WG9344_k6s3.py`（`F2`）＝ `f799e7487694c9270127f3e5ea689aece373dd5a`；`verify/probes/probe_WG9344p1_pooltemp.py`（`F3′`）`8877` B·`sha256` `1c47e17a773a5836835856e14fb26cb2475300c6b8275fb75dd1e60a3ac82fc1` |
| `4` | 收工閘（`W-G.9-344` `V-13`） | 於開工態自倉重跑皆 `rc 0`：`issuer_anchor … 523 522`／`closegate 523 522 .`／`wfns_ast`（`40`／`40`／`39`）／`main_synth`／`probe_WG9341_synth`；`F3′ selftest` `13/13`；`F2 selftest` `9/9` |
| `5` | `def main()` 與二按鈕區（`ast` 實查） | `def main` ＝ `15579`–`25246`；**街角選位**之 If（test 含字樣 `執行第 1 宗街角地優先權選位（左右側獨立）`）＝ `21154`–`21756`（非註解列 `528`）；**配地**之 If（test ＝ `_btn_clicked or _auto_recalc`）＝ `22110`–`23652`（非註解列 `1183`）；二者之本體皆⛔ 含區塊層級之 `return`／`break`／`continue`（`ast` 實查·巢狀函式與迴圈內者除外） |
| `6` | 二本體之介面（`F4 census` 之出艙·全文 ＝ 附錄甲） | main 區域自由變數：街角選位 `10`、配地 `13`（`symtable` 實查）；本體所寫之 session 鍵：`11`／`9`；可達之模組層函式中**經 streamlit 模組讀 session** 者：`select_corner_lots_both_sides_v12`（別名 `_st_B4`／`_st_cr6`／`_st_wb5`·並寫 `f3_corner_range_areas`／`f3_corner_range_polys`）、`_first_corner_alloc_dir`、`_estimate_G_for_qualification`、`bl_pts_by_label`；所改之模組層全域容器：`K917_DROPPED`（經 `k917_note_drop`） |
| `7` | `run_all`（倉外 worktree·`3914b6e`） | `rc 1`；名目 **`64`** 項（`✅ PASS` **`30`**／`🔴 FAIL` **`34`**·框 ＝ 列首 `^\s*✅ PASS `／`^\s*🔴 FAIL `）；其中 `k* 六塊經驗錨3.5m` 實得 `{R1 1, R2 8, R3 7, R4 1, R5 7, R6 6}`（發單側窗四十一實跑） |
| `8` | 段三 harness 之量（`F2 run … 3.5 on`／`0.0 on`） | 皆 `rc 0`；二態 `cmp` 之基線 ＝ 工項二步驟 `7` |
| `9` | `CLAUDE.md` | `257775` B（以換行結尾·CR `0`） |
| `10` | **`W-G.9-344` 之「F.4 模式二 `p_avg`」偏離**（交接文四十 `§一-5`·本窗自倉復現） | `3.5 m`：harness 送入 `wf_f4.compute` 之 ctx `"build"` ＝ 段三後（少 `628-20(2)`／`628-30(1)`／`628-30(2)`／`628-30(3)`）⇒ `wf_f2._block_pre_avg` 之 `R3` `37435.5100 → 37461.2777`、`R5` `37699.8699 → 37756.6769` 元/㎡，餘四塊不變；`0 m` 二者同（段三不動）。`verify/wf_f4.py` 讀 `"build"` 者唯字樣 `p_avg = wf_f2._block_pre_avg(snap, c["build"], pre_price)` 一處（框 ＝ 字樣 `"build"`·母體 ＝ `verify/wf_f4.py`）；其註逐字「模式二分母 p_avg：重劃前全集＝原始 build_parcels」 |

---

## `§二`　KL 之語（逐字）與射程

> 否，採方案乙，意思是否即為「通用化」了，街角地若經過他街廓合併試算機制，街角地亦無人可達標，即以街角規定範圍作為強制抵費地而不暫停?若是這樣，當然採方案乙，直接以通用化目的進行

（KL·發單側窗四十一·`2026-09-26`。所答之【要你判斷】逐字：「本案以外之重劃區，畫面之「街角合併重試」暫於該步停下、待通用化階段再補（方案甲），可以嗎？（是／否；否 ⇒ 方案乙）」；同請示之【要改成】載方案乙逐字：「把畫面之街角選位與配地（逾一千七百列）改寫為可重複呼叫，試算即用畫面即時地價，任何重劃區皆可使用；工程大、改動風險高，須另附多組合成案驗證。」）

發單側即以「通知·不需判斷」答 KL 所問（要旨）：`K-6 §二 段三` 第 `6` 款逐字「某街角全部候選失敗 ⇒ **強制留設抵費地**，範圍**嚴格等於街角規定範圍**」、`K-9-48` 未改此款 ⇒ 方案乙下任何重劃區之畫面皆續辦、⛔ 暫停；仍停機者限於規則未定或無從判定之情形（本單停機款 `9`），`K-9-48` 七項 `3`／`5`／`6` 以紅字「未處置」列出而續辦；方案乙之通用化只及「街角合併重試」一步，**七級調配仍依裁定①只於本案執行**。

🔒 **生產碼之放行**：KL `2026-09-25` 之「是」（`W-G.9-344 §二` 逐字·「同意依上開改後之配地，將「段三」修入程式之側支（暫不併入主線…）」）之射程 `(d)` 明載「段三之**畫面路徑**（`def main()`）⛔ 在本單——次單辦之，主線之快轉須待其落地（使畫面與 harness 同構）」；本日之「採方案乙…直接以通用化目的進行」定其接法 ⇒ 本單之生產碼 `commit` 推**側支**在放行之內。
🛑 **射程**：`(a)` 工項三、五之生產碼 `commit` 推至**側支**；`(b)` 工項零、一、七同落該側支；`(c)` **主線之快轉⛔ 在本放行內**（與 `K-9-29 二` 同批，另呈 KL 放行）；`(d)` 本案之配地結果**⛔ 變**——畫面於段三後之配地，須逐位等於 harness 於段三後之配地（即 KL `2026-09-25` 所放行者·`W-G.9-344` 附錄甲／乙）。
🔒 **逐筆放行清單**（`恆常附款 y`）：本批之 `commit` ＝ 工項零、一、七（皆零生產碼）與工項三、五（生產碼）·**全數只落側支** `verify/W-G.9-343-k929b`（續於 `3914b6e` 之後）。

---

## `§三`　規格

### `§三-0`　接法之由（發單側窗四十一之判·⛔ 為 CC 之判）

1. 畫面之街角選位與配地係 `def main()` 內之行內碼；段三之「不影響原位次」檢核須以**畫面自身之選位與配地**重跑（`k6b_stage3_run` 之 `trial_winner`／`alloc_state`）。
2. harness 之 `run_corner_pk`／`run_step_g` 一律讀快照 `snapshot["財務接線_v3"]`；畫面若借用之，其快照只能是本案凍結檔（`_wf_load_snapshot` ⇒ `verify/case_params_UC9898.json`），而畫面自身之配地讀畫面即時之地價。以畫面即時資料組成同形快照之程式，查無：母體 ＝ 開工態全倉追蹤之 `*.py`；框 ＝ `git grep -nE` 之 regex `\[.財務接線_v3.\]\s*=|"財務接線_v3"\s*:|'財務接線_v3'\s*:|財務接線_v3.*setdefault`（⛔ `^` 錨）⇒ 得 `2` 列：`app.py` 之 `_build_wf_ctx`（其值取自凍結檔）與 `verify/wg_g1_smoke.py`（比較式 `==`·非賦值）；另 `app.py` 之七級調配區之說明逐字「app live 財務值無法逐位複現 KL 授權精度」。⇒ 借用之則段三只能於本案運作。KL 已採**方案乙**（`§二`）。
3. ⇒ 本單將二按鈕區之本體**原封**抽為模組層函式（零算式變更·`ast` 全等可證），段三之畫面入口以之為試算；抽出後二函式可經 `harvest()` 取得，故**首度可於無介面下執行畫面路徑**，與 harness 逐鍵對拍（`F4 parity`）。
4. 🔒 **試算須用真 session**：`select_corner_lots_both_sides_v12` 等四函式經 streamlit 模組讀 session（`§一` 項 `6`），且街角選位本體先寫後讀之（例：`f3_pk_alloc_depth`／`f3_pk_legal_min_width`）⇒ 試算之 st 代理之 `session_state` 須為**真 session 之同一物件**；隔離以「試算前存、試算後復」為之（`§三-2` 步驟 `6`）。發單側窗四十一以另立之 session 試之，街角選位即與 harness 不符（`R4` 二端、`R6` 右成強制抵費地·段二序為空），改用同一物件後逐鍵相符。

### `§三-1`　抽出（工項三·**零行為變更**·只動 `app.py`）

1. **受詞**：`def main()` 內之二 If——(甲) test 之原文含字樣 `執行第 1 宗街角地優先權選位（左右側獨立）` 者；(乙) test 之原文含字樣 `_btn_clicked or _auto_recalc` 者（各恰一·`F4` 以之定位）。
2. **新增**於模組層、緊接於 `def main():` 之前（先甲後乙）：
   - `def f3_screen_corner_pk_run(st, *, <甲之 main 區域自由變數>):`
   - `def f3_screen_stepg_run(st, *, <乙之 main 區域自由變數>):`
   參數集 ＝ 附錄甲所列（甲 `10` 名、乙 `13` 名；keyword-only·⛔ 預設值·⛔ 裝飾）。函式體 ＝ 一條 docstring（得省）＋ 該 If 之本體**原封**（統一去縮排；多列字串之內容⛔ 改一字）。
3. `def main()` 內二 If 之 test ⛔ 動；其本體各換為**單一呼叫**：`f3_screen_corner_pk_run(st, <名>=<名>, …)`／`f3_screen_stepg_run(st, <名>=<名>, …)`（關鍵字集 ＝ 參數集·次序不拘）。
4. 其餘一字不動。
5. **判**：`F4 ast` 之 `A1`〜`A6` 全綠（`§五` `VA-1`）。🔒 發單側窗四十一以倉外之機械抽出（⛔ 入倉）驗之：`A1`〜`A6` 全綠、`F4 parity` 二退縮皆 `rc 0`、`run_all` 與開工態逐項同（`§五-2`）。

### `§三-2`　段三之畫面入口（工項五·`app.py` 模組層新增·置於 `§三-1` 二函式之後、`def main():` 之前）

**名與簽名固定**（`F4` 以之呼叫）：

| 名 | 簽名 | 語意 |
|---|---|---|
| 常數 `K6B_SCREEN_TRIAL_KEYS` | tuple | 段三試算所改寫之 session 鍵 ＝ 附錄甲之「街角選位本體所寫」`11` ＋ 「可達函式所寫」`2`（`f3_corner_range_areas`／`f3_corner_range_polys`）＋「配地本體所寫」`9` ＋ 本單所增之 `f3_corner_cand_diag`，共 `23` |
| 常數 `K6B_SCREEN_STAGE3_KEYS` | tuple | `('f3_k6b_stage3_temp', 'f3_k6b_stage3_build', 'f3_k6b_stage3_fp')` |
| `k6b_stage3_fingerprint(build_parcels, setback)` | → `str` | `sha256`（`hexdigest`）of `json.dumps([round(float(setback or 0), 6), rows], ensure_ascii=False)` 之 UTF-8；`rows` ＝ 逐宗 `(str(暫編地號), str(所屬街廓 or ''), round(float(面積_m2 or 0), 6), round(float(分攤登記面積_m2 or 0), 6))` 依值排序之列表 |
| `k6b_stage3_selected(ss, build_parcels_pre, setback)` | → `None` 或 `(temp, build)` | `ss` 有鍵 `f3_k6b_stage3_error`（真值）⇒ `raise RuntimeError`；⛔ 有鍵 `f3_k6b_stage3_fp` ⇒ `None`；指紋 ≠ `k6b_stage3_fingerprint(build_parcels_pre, setback)` ⇒ `raise RuntimeError`；否則回 `(ss['f3_k6b_stage3_temp'], ss['f3_k6b_stage3_build'])`。二 `raise` 之訊息皆含字樣 `請重跑` |
| `k6b_screen_build_for_g(st, build_parcels)` | → list | `k6b_stage3_selected(st.session_state, build_parcels, st.session_state.get('f3L_setback_default'))`；`RuntimeError` ⇒ `st.error(訊息)` ＋ `st.stop()`；`None` ⇒ 回 `build_parcels`；否則回段三後之 build |
| `f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs)` | → dict | 見下列步驟；回傳鍵 ＝ `temp`／`build`／`log`／`order`／`ran` |

**試算用之 st 代理**（類別名由 CC 定）：`session_state` ＝ 所包之真 st 之 `session_state`（**同一物件**·`§三-0` 項 `4`）；一切顯示呼叫無作用（回傳可作 context manager 之物；`columns`／`tabs` 回等長之列）；`stop()` ⇒ 丟「試算中止」例外；`rerun()` ⇒ 丟「配地完成」例外（配地本體之末句即 `st.rerun()`）。

**`f3_screen_k6b_stage3` 之步驟**（`pk_kwargs` ＝ `f3_screen_corner_pk_run` 之 `10` 名；`g_kwargs` ＝ `f3_screen_stepg_run` 之 `13` 名去 `build_parcels`／`_new_params`／`_btn_clicked`／`_auto_recalc` 之 `9` 名；`temp0`／`build0` ＝ `pk_kwargs` 之 `temp_parcels`／`build_parcels`）：

1. 先自 session 去 `K6B_SCREEN_STAGE3_KEYS` 與 `f3_k6b_stage3_error`。
2. `k6b_stage3_enabled()` 為偽 ⇒ 以真 st 呼叫 `f3_screen_corner_pk_run`（`temp0`／`build0`）；`f3_k6b_stage3_log` ＝ `[]`、`f3_k6b_stage3_order_used` ＝ 其後之 `f3_k6b_stage2_order`；回 `ran ＝ False`（⛔ 存 `K6B_SCREEN_STAGE3_KEYS`）。
3. 否則以代理呼叫 `f3_screen_corner_pk_run`（首趟·寫真 session）；首趟中止 ⇒ 以真 st 再呼叫一次（使畫面現其中止訊息）後重拋。
4. `order` ＝ `f3_k6b_stage2_order`；為空 ⇒ 以真 st 呼叫 `f3_screen_corner_pk_run`（`temp0`／`build0`）；紀錄 `[]`；回 `ran ＝ False`。
5. 三注入物（語意同 `verify/selection_pipeline.py` 之 `run_corner_pk_k6b`）：
   - `a_prime(src, dst)` ＝ `(分攤登記面積_m2 ＋ 面積_m2)(src) × p(src) ÷ p(dst)`；`p(x)` ＝ `pk_kwargs['pre_price_by_zone'][x['重劃前地價區段']]`（畫面之宗地逐宗所帶者·即畫面之配地求 `A` 所用者）；區段空、不在表、或單價 `≤ 0` ⇒ `raise`（⛔ 退 `a′ ＝ a`）。🔒 本案之對照：開工態 harness 之可建築 `61` 宗，其 `重劃前地價區段` 與快照 `原地號_區段[原地號]` 相同者 `59`，餘 `2` 為 ghost（`''` 對 `None`·面積 `0`·⛔ 入合併群）。
   - `trial_winner(temp, build, 街廓, 端, 候選)`：深拷貝（build 為 temp 之同物件子集）後以代理呼叫 `f3_screen_corner_pk_run`；winner ＝ `f3_corner_winners[街廓][p1_end|p2_end]`（端 `左`／`右`）；試算G／門檻 ＝ `f3_corner_cand_diag` 中 `街廓`／`端`／`候選地號` 相符之列之 `真G(㎡)`／`門檻(㎡)`（無則 `None`）；試算中止 ⇒ `raise RuntimeError`（停機款 `9`）。
   - `alloc_state(temp, build)`：深拷貝；`K917_DROPPED.clear()`；以代理先呼叫 `f3_screen_corner_pk_run`、再呼叫 `f3_screen_stepg_run`（`g_kwargs` ＋ `_auto_recalc=False`、`_btn_clicked=True`、`build_parcels=` 拷貝之 build、`_new_params=dict(session[g_kwargs['_param_key']] 或 {})`）；「配地完成」例外 ⇒ 正常；「試算中止」例外或 `RuntimeError` ⇒ `err` ＝ 訊息、列為空；列 ＝ `f3_G_values`；「保留」宗集與「面積 > 0 而容不下內接矩形之配餘地」片數之算法**逐字同** harness 之 `alloc_state`（`get_min_lot_size(該街廓 category, 該街廓於 _corner_rows_init 之 正面路寬(m))`、`_rect_fits_free_pose`）。
6. **隔離**：試算前存 `K6B_SCREEN_TRIAL_KEYS` 中已在 session 者之深拷貝、及 `K917_DROPPED` 之深拷貝；呼叫 `k6b_stage3_run(order, 上鎖集, t8_ownership_map, temp0, build0, {label: {"category": …}}〔取自 g_kwargs['classified_blocks']〕, session['f3_manual_road_centerlines'] 或 {}, a_prime, trial_winner, alloc_state, log_print=<收集>)`（上鎖集 ＝ `f3_k6b_stage1_locked_by_block` 各值之聯集）；**`finally`** 內：`K6B_SCREEN_TRIAL_KEYS` 逐鍵復原（原有者復其值、原無者刪之），`K917_DROPPED` 復原。
7. `k6b_stage3_run` 丟 `RuntimeError` ⇒ session 存 `f3_k6b_stage3_error` ＝ 訊息（首列·`≤ 500` 字）；`st.error(…)` ＋ `st.stop()`（其後之配地由 `k6b_screen_build_for_g` 擋下）。
8. 否則以真 st 呼叫 `f3_screen_corner_pk_run`（`temp2`／`build2`·終趟）；收集之「未處置」訊息逐則 `st.error`；以 `st.expander`（展開）列紀錄表；session 存 `f3_k6b_stage3_log` ＝ 紀錄、`f3_k6b_stage3_order_used` ＝ `order`、`f3_k6b_stage3_temp` ＝ `temp2`、`f3_k6b_stage3_build` ＝ `build2`、`f3_k6b_stage3_fp` ＝ `k6b_stage3_fingerprint(build0, session['f3L_setback_default'])`；回 `ran ＝ True`。

**`f3_screen_corner_pk_run` 之增改**（二處·⛔ 他改）：
- 字樣 `st.session_state['f3L_corner_winners'] = _corner_select_results` 之次列增 `st.session_state['f3_corner_cand_diag'] = _corner_cand_diag`（恰一）。
- 二則過時之說明改寫：
  - 段二表下之說明（原文「🛑 **唯讀**：本表僅供檢視，**不被任何分配邏輯消費**——段三（逐一嘗試／集中規則／跨街廓合併）尚未落地。」）⇒ 「🔗 本表為「街角合併重試」（段三·`K-6 §二 段三`／`K-9-48`）之處理順序：依序逐一試算，成者定案；某街角全部候選未成 ⇒ 留設強制抵費地（範圍＝街角規定範圍）。」
  - 上鎖表下之首則說明（原文始於「🛑 **唯讀**：本表僅供檢視，**不被任何分配邏輯消費**——上鎖之受詞係」、止於「（`K-9-24 一`）且完成於段一之前。」）⇒ 「🔒 上鎖者於「街角合併重試」（段三）既不被併出、亦不作為合併標的（`K-6 §二 段三 1`「取該合併群中**未上鎖**之其他片」）。」

### `§三-3`　`def main()` 內之接線（工項五）

1. **街角選位**之 If 之本體 ⇒ 單一呼叫 `f3_screen_k6b_stage3(st, pk_kwargs=dict(<甲之 10 名>=<名>…), g_kwargs=dict(_param_key=_param_key, B_value=B_value, C_for_calc=C_for_calc, _tab6_burden=_tab6_burden, block_meta_by_label=block_meta_by_label, sb_rows_by_label=sb_rows_by_label, post_price_by_block=post_price_by_block, pre_price_by_zone=pre_price_by_zone, classified_blocks=classified_blocks))`。
2. **配地**之 If 之本體 ⇒ 同 `§三-1` 之呼叫，惟 `build_parcels=k6b_screen_build_for_g(st, build_parcels)`。
3. `_f3L_invalidate_g_cache`（`def main()` 內之巢狀函式）另自 session 去 `K6B_SCREEN_STAGE3_KEYS` 與 `f3_k6b_stage3_error`。
4. **七級調配**：字樣 `_f4r = _wf4.compute(_cbt, _f0r, _f2r, _f3r)` ⇒ 首參改 `k6b_f4_ctx(_cbt, {_tag: _wg_ss['f3_build_parcels']})`（`k6b_f4_ctx` 自 `verify/selection_pipeline.py` 匯入·`§三-5`；得以別名）。
5. **步驟 M**（字樣 `步驟 M：公共設施用地分配` 之標題起、字樣 `步驟 I：推送資料至下游分頁` 之標題止）：於字樣 `with st.expander("📋 自動計算公設分配` 之前立 `_tp_m` ＝（`k6b_stage3_selected(st.session_state, build_parcels, st.session_state.get('f3L_setback_default'))` 為 `None` ⇒ `temp_parcels`；否則段三後之 temp 去帶鍵 `段三併出` 者）；`RuntimeError` ⇒ `st.error` ＋ `st.stop()`。區內 `temp_parcels` 之四處讀（M-1 之依街廓分組、M-1 之歸戶持分、M-4 之公設片選取、M-4 之歸戶相鄰建地）改讀 `_tp_m`；M-4 之「歸戶自有土地」圖示（其上三列含字樣 `_gid_parcel_set`）照舊讀 `temp_parcels`（重劃前之地）。🔒 依據 ＝ `W-G.9-344` 補令一 裁三（段三所併出之片⛔ 再入公設地之調配）之同一規則。

### `§三-4`　`_build_wf_ctx`（`app.py` 模組層·工項五）

於 `return` 之前：`_s3 = k6b_stage3_selected(ss, _need("f3_build_parcels"), _need("f3L_setback_default"))`。回傳之 ctx：`_s3` 為 `None` ⇒ `"build"` ＝ `_need("f3_build_parcels")`、`"temp"` ＝ `_need("f3_temp_parcels")`（同改前）；否則 `"build"` ＝ `_s3[1]`、`"temp"` ＝ `k6b_stage3_pool_temp(_s3[0])`（`k6b_stage3_pool_temp` 自 `verify/selection_pipeline.py` 匯入）。`k6b_stage3_selected` 之 `raise` ⛔ 攔（loud）。⛔ 增減 ctx 之鍵（仍 `14`）。

### `§三-5`　harness 側（工項五）

1. `verify/selection_pipeline.py` 新增（置於 `def run_corner_pk_k6b` 之前）：`def k6b_f4_ctx(ctx_by_tag, build_pre_by_tag): return {t: dict(c, build=build_pre_by_tag[t]) for t, c in ctx_by_tag.items()}`（docstring 載其由 ＝ `wf_f4` 讀 `"build"` 者唯模式二 `p_avg`·其母體 ＝ 重劃前）。
2. **`wf_f4.compute` 之五呼叫點**（開工態全倉·框 ＝ 呼叫之 func 為 `wf_f4.compute` 或 `_wf4.compute`·母體 ＝ `app.py`、`verify/run_verification.py`、`verify/wg_g1_smoke.py`、`verify/wg_g2_smoke.py`、`verify/wg_g3.py`）其首參一律 `k6b_f4_ctx(<原 ctx>, {<情境>: <段三前之 build>})`：`run_verification.py` ＝ `build_parcels`（原始）；三 smoke ＝ 呼叫 `run_corner_pk_k6b` 前之 build；`app.py` ＝ `§三-3` 第 `4` 項。
3. **三 smoke 之 seed**（`wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py`）改為與畫面同形：`f3_temp_parcels` ＝ 段三前之 temp、`f3_build_parcels` ＝ 段三前之 build；另加 `f3_k6b_stage3_temp` ＝ 段三後之 temp、`f3_k6b_stage3_build` ＝ 段三後之 build、`f3_k6b_stage3_fp` ＝ `ns["k6b_stage3_fingerprint"](段三前之 build, setback)` ⇒ `_build_wf_ctx` 所出之 ctx 與改前同（其驗 ＝ `VB-7` 之 `wfctx`；三 smoke 於開工態即終止於此前·`VB-10`）。
4. `verify/tools/y_dump_diff.py`（`W-G.9-344` 補令二 裁四）：`_run_harness` 改走 `run_corner_pk_k6b`，其後之 `run_step_g` 吃段三後之 build。
5. `verify/run_verification.py` 之 G.1 閘之 seed（`0m`·段三不動）⛔ 改。

### `§三-6`　許可集與⛔ 動之檔

- 工項三 ＝ `app.py` 唯一。
- 工項五 ⊆ `app.py`、`verify/selection_pipeline.py`、`verify/run_verification.py`、`verify/wg_g1_smoke.py`、`verify/wg_g2_smoke.py`、`verify/wg_g3.py`、`verify/tools/y_dump_diff.py`。
- ⛔：`verify/stepg_pipeline.py`；`verify/wf_f0.py`〜`verify/wf_f4.py`；`verify/app_harvest.py`；`verify/run_all.py`；`verify/baselines/**`；`verify/probes/**`（工項一之 `F4`／`F5` 除外）；`docs/rulings/**`；`docs/reports/W-G.4_泛用阻塞項登記表.md`；`docs/reports/W-G.9波_claude.ai側自誤登記.md`；`docs/驗證裁定登記表.md`。
- 🔒 **通用化**：工項五於 `app.py` 所增之列（`git diff -U0 <工項三> <工項五> -- app.py` 之 `+` 列）⛔ 含街廓名、地號、案名（框 ＝ regex `['"]R\d['"]|628-|UC9898|_is_uc9898`）。

### `§三-7`　呼叫端處置表（CC 於報告出艙）

`def main()` 內 `temp_parcels`／`build_parcels`／session `f3_temp_parcels`／`f3_build_parcels` 之一切讀（工項五後·`ast` 實查·列號）逐處列「段三後／段三前（重劃前母數）／段三前（顯示重劃前之地）」三分類與其由；harness 側之 `wf_f4.compute` 五呼叫點與三 smoke 之 seed 同表。

---

## `§四`　工項（依序·全數於側支）

### 工項零　本單原封入倉（側支·零生產碼）

`docs/orders/W-G.9-345_重量單.md`（**新檔**）。自施工樹之根二進位複製；`SELF_SHA256` 依 `P-5` 原口徑自驗。`commit` 訊息逐字 `W-G.9-345 工項零：本單原封入倉（側支）⛔ 零生產碼` ⇒ `push origin HEAD:verify/W-G.9-343-k929b`。

### 工項一　量測器入倉 ＋ 塊 `P1` 之末端追加（側支·零生產碼·一 `commit`）

1. `verify/probes/probe_WG9345_screen.py`（**新檔**）＝ 檔 `F4` 之二進位複製。
2. `verify/probes/probe_WG9340_main_synth.py`（**替換**）＝ 檔 `F5` 之二進位複製（改版之由：抽出後「app 側宿主」自 `main()` 移至 `f3_screen_stepg_run`；其檔首新增之註逐字載之；受詞與判準一字未改）。
3. 塊 `P1` 依圍欄之逐列索引抽出（圍欄內全文·末附換行）、對拍 `§五-1` 之 bytes／`sha256`（停機款 `3`）後，以二進位附於 `CLAUDE.md` 之末；`CLAUDE.md` 之刪除欄 `0`。
4. `commit` 訊息逐字 `W-G.9-345 工項一：量測器入倉 ＋ 待落地清單之更新（側支）⛔ 零生產碼` ⇒ `push origin HEAD:verify/W-G.9-343-k929b`。

**塊 `P1`**：

````markdown

---

## 🔧 待落地清單之更新：段三之畫面路徑（方案乙·通用化）；畫面二段之抽出；F.4 模式二 `p_avg` 之母體（`W-G.9-345`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `3914b6e76c45bfb0d9b6eff8a28af6020124e461`（本批開工態·側支 `verify/W-G.9-343-k929b` 之端）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 段三·畫面路徑（KL `2026-09-26` 採方案乙） | 畫面之街角選位與配地二段原封抽為模組層（`f3_screen_corner_pk_run`／`f3_screen_stepg_run`）；段三之畫面入口 `f3_screen_k6b_stage3` 以之試算（真 session·試算後復原）；配地、七級調配、步驟 M 依段三後之宗地（指紋不符 ⇒ loud） | ⬜（本批落側支後 🔶；入主線另候 KL 放行） | `docs/orders/W-G.9-345_重量單.md` |
| `2` | F.4 模式二 `p_avg` 之母體 | `wf_f4.compute` 之五呼叫點以 `k6b_f4_ctx` 送入段三前之 build（`W-G.9-344` 原單 `§三-4` 之未落實者） | ⬜（同上） | 同上 |
| `3` | 畫面路徑之活體對拍 | `verify/probes/probe_WG9345_screen.py parity`：畫面二函式（harvest）對 harness 之 `run_corner_pk`／`run_step_g` 逐鍵；既有之同構差 ＝ harness 多一「幾何面積 `0`」之池列（二退縮皆 `R1-抵費地-2`）——待登記 | ⬜（待登記） | 同上 `§五-2` |
| `4` | harness 之逐行複刻 | 畫面二段既已成函式，`verify/stepg_pipeline.py`／`verify/selection_pipeline.py` 之複刻與之之單一真相源化，列泛化波之議 | ⬜ | — |

🔒 **依賴序**：段三 harness 路徑（`W-G.9-344`·側支）→ 段三畫面路徑（本批·同側支）→ `K-9-29 二` ＋ 段三同批入主線（另候 KL 放行）→ `K-9-29 六` 入池閘 → 五級。
🔒 **量測器**：`verify/probes/probe_WG9345_screen.py`（`census`／`ast`／`parity`／`wiring`／`f4ctx`／`wfctx`／`selftest`）；`verify/probes/probe_WG9340_main_synth.py` 之「app 側宿主」自本批起為 `f3_screen_stepg_run`（抽出前為 `main()`）。
````

### 工項二　改前態之量測（⛔ `commit`·出艙存倉外）

於工項一之 `commit`（其生產碼 ＝ 開工態）之施工樹（`F4` 之量測取 `<base>` ＝ 工項一之 `commit`）：

1. `python verify/probes/probe_WG9345_screen.py selftest` ⇒ `rc 0`（`10/10`）。
2. `… census <repo> <base> > <倉外>/census.txt` ⇒ `rc 0`；去 `\r` 後除首列外與附錄甲逐位相同。
3. `… ast <repo> <base>` ⇒ **`rc 1`**（抽出未落之必紅）。
4. `… parity <repo> 3.5 off`、`… parity <repo> 3.5 on`、`… wiring <repo>`、`… f4ctx <repo>`、`… wfctx <repo> 3.5` ⇒ 皆 **`rc 3`**（受詞缺）。
5. `python verify/probes/probe_WG9340_main_synth.py <repo>`（`F5`）⇒ `rc 0`（出艙「app 側宿主 ＝ main」）。
6. `python verify/probes/probe_WG9344_k6s3.py selftest` ⇒ `rc 0`（`9/9`）。
7. `… probe_WG9344_k6s3.py run <repo> 3.5 on <倉外>/pre_on_3.5.json`、`… run <repo> 0.0 on <倉外>/pre_on_0.0.json` ⇒ 皆 `rc 0`。
8. **`run_all` 改前**：倉外路徑 `<P>`（工項一之 `commit`）跑 `python verify/run_all.py > <倉外>/runall_before.log 2>&1` 一次。期：`rc 1`；名目 **`64`** 項（`✅ PASS` **`30`**／`🔴 FAIL` **`34`**）（出處 ＝ `§一` 項 `7`）。跑畢移除該 worktree（**`<P>` 留作工項四、六之同一路徑**）。

（發單側窗四十一於開工態實跑上列 `1`〜`8`，皆如期；`3`／`4` 之 `rc` 見 `§五-2`。）

### 工項三　抽出（側支·**一** `commit`·只動 `app.py`）

依 `§三-1` 實作（得以腳本機械施之；腳本⛔ 入倉）。CC 之 plan 送 reviewer；reviewer 之出艙併入報告。`commit` 訊息逐字 `W-G.9-345 工項三：畫面「街角選位」「配地」二按鈕區之本體原封抽為模組層函式（零行為變更）🔴 生產碼`；**先於本機 `commit`，待工項四之閘全過後方 `push origin HEAD:verify/W-G.9-343-k929b`**（閘之量測與 `push` 為分開之呼叫）。

### 工項四　抽出之閘（⛔ `commit`·於工項三之本機 `commit` 量）

依 `§五` 之 `VA-1`〜`VA-7` 逐項實跑，逐項出艙三值（期／實得／判）。全過 ⇒ `push`；任一不過 ⇒ 停機款 `6`（或 `5`／`10`），⛔ `push`、回報。

### 工項五　段三之畫面接線與下游之分流（側支·**一** `commit`）

依 `§三-2`〜`§三-5` 實作；plan 送 reviewer。`commit` 訊息逐字 `W-G.9-345 工項五：段三之畫面入口（方案乙）＋ 配地／七級調配／步驟 M 依段三後之宗地 ＋ F.4 模式二 p_avg 之母體 ＋ y_dump_diff 之改接 🔴 生產碼`；先本機 `commit`，待工項六之閘全過後方 `push`。

### 工項六　接線之閘（⛔ `commit`·於工項五之本機 `commit` 量）

依 `§五` 之 `VB-1`〜`VB-13` 逐項實跑、出艙三值。全過 ⇒ `push`；任一不過 ⇒ 停機款 `8`（或 `7`／`9`／`10`），⛔ `push`、回報。

### 工項七　執行報告入倉（側支·零生產碼）

`docs/reports/W-G.9-345R_段三畫面路徑_執行報告.md`（新檔）。須載：① 逐 `commit` 之 hash 與工項之對應；② 停機款 `1`〜`13` 之三值；③ `F4`／`F5`／`P1` 之實得；④ 工項二、四、六之全部出艙（`census.txt`、各 `parity` 之 `json` 摘要、`runall_cmp_A.txt`／`runall_cmp_B.txt` 全文）；⑤ `§三-7` 之處置表；⑥ `§三-2` 步驟 `6` 之隔離鍵實數與其驗（`VB-1` 之「session 之回復」列）；⑦ 抽出之機械法（若用腳本·其要旨）；⑧ reviewer 之出艙；⑨ 執行時間（`run_all` 三份、`parity` 各份）；⑩ CC 之自捕；⑪ 下一 CC 窗須知。`commit` 訊息逐字 `W-G.9-345 工項七：執行報告入倉（側支）⛔ 零生產碼` ⇒ `push origin HEAD:verify/W-G.9-343-k929b`。

---

## `§五`　【驗收】

### 工項四（抽出·於工項三之 `commit` 量·`<base>` ＝ 工項一之 `commit`）

| 閘 | 受詞 | 期 |
|---|---|---|
| `VA-1` | `F4 ast <repo> <base>` | `rc 0`；`A1`〜`A6` 之 `12` 列全 ✅（`A2` 之敘述數 ＝ 甲 `2`／乙 `49`；`A3` 之參數數 ＝ `10`／`13`；`A5` ＝ `294`／`294`） |
| `VA-2` | `F4 parity <repo> 3.5 off`；`F4 parity <repo> 0.0 off` | 皆 `rc 0`；街角選位 session 鍵 `10` 列全 ✅；配地列 ＝ `harness 68／畫面 67`、`harness 63／畫面 62`，不符格 `0`；`Z` ＝ `[('harness', 'R1-抵費地-2')]`（二退縮同） |
| `VA-3` | `F4 parity <repo> 3.5 off --perturb` | **`rc 1`**（畫面側 `B` 乘 `1.0001` 之必紅造） |
| `VA-4` | `git diff --name-only <工項一> <工項三>` | 恰 `app.py` |
| `VA-5` | `issuer_anchor … 523 522`；`closegate 523 522 .`；`wfns_ast <repo>`；`F5 <repo>`；`probe_WG9341_synth <repo>` | 皆 `rc 0`；`wfns_ast` 仍 `40`／`40`／`39`；`F5` 出艙「app 側宿主 ＝ f3_screen_stepg_run」、丙部四突變皆 ✅ |
| `VA-6` | 同一倉外路徑 `<P>`（工項三之 `commit`）跑 `python verify/run_all.py > <倉外>/runall_A.log 2>&1`；`python verify/probes/probe_WG9343_step0_flag.py runall <倉外>/runall_before.log <倉外>/runall_A.log > <倉外>/runall_cmp_A.txt` | `run_all` `rc 1`；`runall` `rc 0`；**相異項 `0`**（名目、狀態、違規數、本體逐項同）；✅→🔴 ≠ `0` ⇒ 停機款 `10` |
| `VA-7` | `F2 run <repo> 3.5 on <倉外>/A_on_3.5.json`；`F2 cmp <倉外>/A_on_3.5.json <倉外>/pre_on_3.5.json`；同 `0.0` | 二 `cmp` 皆 `rc 0`（harness 未受影響） |

### 工項六（接線·於工項五之 `commit` 量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `VB-1` | `F4 parity <repo> 3.5 on <倉外>/B_on_3.5.json` | `rc 0`；段三紀錄 `18` 列、段二序 `13` 列皆 ✅；段三後 temp `126`／build `57` 逐元素 ✅；`K917_DROPPED` ✅；session 之回復 ✅；配地列 `harness 60／畫面 59`·不符格 `0`；`Z` ＝ `[('harness', 'R1-抵費地-2')]` |
| `VB-2` | `F4 parity <repo> 0.0 on` | `rc 0`；段三紀錄 `0` 列；配地列 `63／62`；`Z` 同上 |
| `VB-3` | `F4 parity <repo> 3.5 s3off` | `rc 0`；段三紀錄 `0` 列；build `61`；配地列 `68／67` |
| `VB-4` | `F4 parity <repo> 3.5 off`；`… 0.0 off` | 皆 `rc 0`（同 `VA-2`） |
| `VB-5` | `F4 parity <repo> 3.5 on --perturb` | **`rc 1`** |
| `VB-6` | `F4 wiring <repo>` | `rc 0`；`W0`〜`W8` 全 ✅（`W4` ＝ `5`／`5`；`W6` ＝ `2`／`4`）；丙部四突變皆 ✅（器紅 `0`） |
| `VB-7` | `F4 f4ctx <repo>`；`F4 wfctx <repo> 3.5`；`F4 wfctx <repo> 0.0` | 皆 `rc 0`（`wfctx 3.5` 之 T1 ＝ `116` 片；`0.0` ＝ `126` 片） |
| `VB-8` | `F2 selftest`；`F2 run … 3.5 on`／`0.0 on` 與工項二之 `cmp` | `rc 0`（`9/9`）；二 `cmp` 皆 `rc 0` |
| `VB-9` | `python verify/probes/probe_WG9344p1_pooltemp.py selftest`；`… run <repo> 3.5 on` | `13/13`；`rc 0` |
| `VB-10` | `python verify/wg_g1_smoke.py`、`python verify/wg_g2_smoke.py`、`python verify/wg_g3.py`（於工項五之施工樹與工項一之施工樹各跑一次） | 三者之最末例外之型別與訊息，與工項一之跑逐字同（去 `File "…", line N` 列後之末 `12` 列對拍）；`File` 列之行號差唯所改之 smoke 檔自身。🔒 三者於開工態即終止於 `run_step_g` 之 `cad['baselines']` 為空（發單側窗四十一實跑）⇒ 其 seed 之改由 `VB-7` 之 `wfctx` 承擔判別力 |
| `VB-11` | `git diff --name-only <工項三> <工項五>`；`git diff -U0 <工項三> <工項五> -- app.py` 之 `+` 列以 `§三-6` 之 regex 篩 | 所改之檔 ⊆ `§三-6` 許可集、與⛔ 集交集 `∅`；regex 命中 `0` |
| `VB-12` | 同一倉外路徑 `<P>`（工項五之 `commit`）跑 `run_all > <倉外>/runall_B.log`；`probe_WG9343_step0_flag.py runall <倉外>/runall_before.log <倉外>/runall_B.log > <倉外>/runall_cmp_B.txt` | `run_all` `rc 1`；`runall` `rc 0`；項 `64`／`64`·PASS `30 → 30`·FAIL `34 → 34`；✅→🔴 ＝ `0`；相異項限於「本體之差唯 traceback 中 `verify/run_verification.py` 之行號」者（`§三-5` 之增列所致·發單側雛形 ＝ `#64 W-G G.2` 之 `1460 → 1461`），逐項出艙歸因；他差 ⇒ 停機款 `8` |
| `VB-13` | `VA-5` 之五器 | 皆 `rc 0` |

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 檔 `F4`（`probe_WG9345_screen.py`） | `48501` B·`sha256` `e0c1c87c181c675d163226b9094f937b0b19e28faa6df4712046c50d305502b6`·CR `0` |
| `3` | 檔 `F5`（`probe_WG9340_main_synth.py`·改版） | `14971` B·`sha256` `9d2f461ffd7c919b29e46fb991bdc5c4bdcc1060a0904250874110181f53271d`·CR `0` |
| `4` | 塊 `P1` | `2141` B·`sha256` `828643dd730e3295253cc3a5c05708f2e81d76fbdb3cb065c8e10c68d593243c`；附於 `CLAUDE.md`（`257775` B）之末後，期末 ＝ `259916` B |
| `5` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十一於開工態實跑：🔴 機械 `0` 項／🟡 提示 `3` 項（皆 `P-4`：列 `85`〔`§一` 項 `10` 之 `p_avg` 改前改後之數值〕、列 `289`〔`§五` 工項六表之計數與行號之改前改後〕、列 `319`〔`§五-2` 之同類〕——皆為數值之改前改後、⛔ 方向性之轉引 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `15579`–`25246`）⇒ `rc 0` |

抽取式 ＝ 圍欄開列（`` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　發單側窗四十一之雛形實跑（倉外·⛔ 入倉·供受單側對照·⛔ 為閘）

1. **抽出**（倉外腳本·機械施 `§三-1`）：`F4 ast` `rc 0`（`12` 列全 ✅）；`symtable` 查新函式之全域參照：甲 `31`、乙 `51`，其中未定義名 `0`、原為 `main()` 區域名者 `0`。
2. **抽出後之活體對拍**：`F4 parity 3.5 off` ／ `0.0 off` 皆 `rc 0`（配地列 `68／67`、`63／62`；`Z` 皆 `[('harness','R1-抵費地-2')]`；該列 harness 側之 `幾何面積(㎡)` ＝ `0.0`、`G(㎡)` ＝ `0.0`；`R1-抵費地-1` 二側之環僅起點不同·對稱差面積 `0`）；`--perturb` ⇒ `rc 1`（配地列不符格 `287`）；工作樹為開工態時 `parity` ⇒ `rc 3`。
3. **抽出後之 `run_all`**：`64` 項 `30`／`34`；與開工態對拍相異 `1` 項（`#58 W-F F.0` 之本體），其差唯 traceback 之倉外路徑（二跑之路徑不同）⇒ 本單令同一路徑。
4. **段三接線之參考實作**（倉外·⛔ 入倉）：`F4 parity 3.5 on` ／ `0.0 on` ／ `3.5 s3off` ／ `3.5 off` 皆 `rc 0`（見 `VB-1`〜`VB-4` 之期）；`F4 wiring` `rc 0`（丙部四突變皆轉紅）；`F4 f4ctx` `rc 0`；`F4 wfctx 3.5`／`0.0` 皆 `rc 0`；`F2 run 3.5 on` 與開工態 `cmp` 相異 `0`；`F5`／`wfns_ast`／`probe_WG9341_synth` 皆 `rc 0`；`F3′ selftest` `13/13`、`F2 selftest` `9/9`；`app.py` 於抽出之後所增 `268` 列、所刪 `15` 列（`diff` 實數），其 `+` 列以 `§三-6` regex 篩 ⇒ `0`。`run_all`：`64` 項 `30`／`34`；與開工態對拍相異 `2` 項——`#58 W-F F.0`（唯倉外路徑之差·二跑之路徑不同）、`#64 W-G G.2`（唯 `verify/run_verification.py` 之 traceback 行號 `1460 → 1461`）；末端夾具／golden `21`／`21` 相異 `0`；三 smoke 之最末例外逐字同。
5. **試算不可另立 session 之實證**：`§三-0` 項 `4`。

---

## 附錄甲　`F4 census <repo> 3914b6e` 之出艙（發單側窗四十一·去首列外逐位）

```text

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

SELF_SHA256: 1bc28c14e976441166cb0070122c74fd94ecf22d44e14b3e23e7ffe8cf381b90
