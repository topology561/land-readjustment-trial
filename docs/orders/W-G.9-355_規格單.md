# `W-G.9-355`　規格單：末端塊之合併再試（含 `K-9-50`）之畫面路徑（側支）＋ 待落地清單之更新 ＋ 恆常附款 `n③` 之試行期變通

> **本單建議等級 ＝ `xhigh`**（本單令 CC 依規格撰寫生產碼·新流程 `甲-7`）。
> **發單** ＝ 發單側窗五十一·`2026-09-28`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至側支 `verify/W-G.9-353-endmerge`**）。
> 🆕 **流程 ＝ 規格單**（新流程之首張·KL `2026-09-28 11:43` 令試行·`§二`）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `F14`／`F4p`·CC ⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py` blob（由 CC 回報、發單側復驗時自倉重算）；出單前⛔ 整套模擬（`恆常附款 n③` 之試行期變通 ＝ 塊 `H1`）。
> **級** ＝ **重**（生產碼 `1` 檔：`app.py`；土地後果：**本案⛔**——harness 之碼一字不動，其配地與 `run_all` 改前改後逐位同；畫面路徑與 harness 逐鍵同〔`parity`〕；**他案有**——畫面路徑之末端塊「各筆單獨皆未達」由停機改依 `K-9-49 ②`／`K-9-36 ③`／`K-9-50` 處之〔與 harness 同〕；段三之畫面試算遇該情形由試算中止改暫以強制抵費地計〔與 harness 同〕）。
> **開工態** ＝ 側支 `verify/W-G.9-353-endmerge` ＝ `f55935cb95b5e6c058231ee89d5dd19e3a291456`（`W-G.9-354` 之端）；主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`。🔒 **本批之五筆 `commit` 一律推至同一側支（皆快轉·承 `f55935c`）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F14`／`F4p`／`E5`／`P9`／`H1` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**。
> 🔑 **來源檔**（檔名逐字 `W-G.9-355_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 以外之生產碼一字（生產碼 `34` 檔之其餘 `33` 檔）；`§三-3` 之禁改；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4 之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿、`K-6` 典、`GB` 簿之一字；自誤簿、`CLAUDE.md` 與 `docs/reports/W-G.9波_恆常附款登記表.md` 除塊 `E5`／`P9`／`H1` 之純末端追加外之一字；既有量測器除塊 `F4p` 外之一字；任何既有側支之刪除或改寫；KL 主 checkout。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；`git rev-parse origin/verify/W-G.9-353-endmerge` ＝ `f55935cb95b5e6c058231ee89d5dd19e3a291456`；`git ls-remote --heads origin` 之列數 ＝ `31`；施工樹 `git checkout --detach origin/verify/W-G.9-353-endmerge` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 547 545` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`911`** 檔·器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十一實跑（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-355`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py f55935c W-G.9-355 W-G.9-354 W-G.9-399` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`5` | 🟢 可取（鬆框 `5` 列 ＝ `docs/orders/W-G.9-354_重量單.md:103`／`:1846`／`:1919`／`:1931` 與 `docs/rulings/K-6_街角地分配程序與可分配判準.md:4979` 之前瞻引用·依宣告框 `②`⛔ 占用） |
| 對照甲［必非零］`W-G.9-354` | `2`／`8`／`4` | `2`／`8`／`4` | `12` | `4` | `5`／`55` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-399` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`1` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `15`／`16` | 🟢 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態之追蹤檔 `2716` 檔〔讀不到 `24`〕·錨定框 `(?<![0-9\-])<號>(?![0-9])`·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取）：

| 號 | 裸（錨定）列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 548` | `0` | `0` | `0` | 🟢 可取 |
| 對照甲［必非零］`自誤 547` | `4` | `0` | `4` | 🟢 C 形非空（B 形於本倉為量測器紅·`GB-158`） |

自誤 `MAX` ＝ `547`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 548`；⛔ 鑄 `GB`／`VR`／`K-9`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `0b05925`，或側支 `verify/W-G.9-353-endmerge` ≠ `f55935c`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `31` |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `F14`／`F4p`／`E5`／`P9`／`H1` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項一之 `git apply --check`（塊 `F4p`）不過，或施後 `verify/probes/probe_WG9345_screen.py` 之 blob ≠ `§五-1` 項 `7`；或工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-6` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變**（`V-3`〜`V-5` 任一相異·單⛔ 載其期） |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-353-endmerge`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之三檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗五十一自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `verify/W-G.9-353-endmerge` ＝ `f55935cb95b5e6c058231ee89d5dd19e3a291456`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`31`** |
| `2` | 生產碼（開工態 blob） | `app.py` `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`（`1589495` B）；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966` |
| `3` | `W-G.9-354` 之復驗 | 發單側窗五十一依交接文五十 `§四-1` 逐項自倉重跑：側支五 `commit`（`cd3c29f`／`758cfba`／`a44a386`／`9e744db`／`f55935c`）逐筆對拍（單 ＝ `5361bd49…`·`SELF_SHA256` 自驗相符；`D2`／`F12d`／`F13`／`K3`／`E4`／`G4`／`P8` 與單內塊逐位同；`F12d` 施於 `928d292` 得 `c12d3f85…`、`D2` 施於 `758cfba` 得 `dc3e52be…` ＝ `a44a386` 之 `app.py`）；四檔之嚴格前綴（`K-6` `412870 → 427954`、自誤簿 `1072508 → 1075505`、`GB` 簿 `1020320 → 1022244`、`CLAUDE.md` `286590 → 291243`）；收工閘 `1`〜`17` 自跑皆符（閘 `7` 四簿：自誤 `532`／`547`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `47`／`50`·缺號集皆同開工態；`wfns_ast` `48`／`48`／`47`）；工項二之前置（`F13` 三子命令 `rc 1`；`F12` 之 `selftest`／`wiring` `rc 0`、`run` `rc 1`〔`X1@甲`〕）；`V-2`（`F8 run` 二退縮改前改後 `diff` 皆空）；`V-3`（`F12 run` 改前改後之異列唯 `X1` 與末列；`F13 run` 之數 ＝ 該單 `§一` 項 `7`）；`V-4`（`parity` 二退縮 `rc 0`；`F10 run`／`F11 run` 改前改後逐位同）；`V-5`（`run_all` 二態於同一倉外路徑自跑·各 `236056` B·`cmp` 逐位同·相異項 `0`）——**全數相符**；主線仍 `0b05925…`、heads `31`。CC 回報之差異（Windows `run_all` `238037` B；報告內嵌 log 之行尾正規化）皆核實、無影響 |
| `4` | 本批之受詞 | 末端塊之合併再試（`K-9-49 ②`·`K-9-36 ③`·`K-9-50`）之畫面路徑（`CLAUDE.md`「…（`W-G.9-354`）」節序 `3`）；段三之畫面試算之 `'trial'`（harness 自 `W-G.9-353` 已然）；`main()` 成果區之顯示 |
| `5` | 現碼之行為（開工態·畫面路徑） | ① 段三之畫面入口之三出口皆⛔ 辦合併再試；session 之 `SS_END_BLOCK_MERGE`／`f3_end_block_merge_log` 畫面⛔ 寫、亦⛔ 去（`F14 selftest` 之 `T1d`／`T4d`／`T8b` 於開工態得前次之紀錄殘留）⇒ 畫面定案之配地遇各筆單獨皆未達之端 ⇒ 停機（`end_block_host` 之准否）；② 段三之畫面試算（`alloc_state`）之配地⛔ 設 `'trial'`（`T3c`／`T9c` 得 `[None]`）；③ `K6B_SCREEN_TRIAL_KEYS` ⛔ 含 `'f3_end_block_mode'`（`TK` 得 `(False, True)`） |
| `6` | 本案與合成案（harness·開工態·`python verify/probes/probe_WG9354_endcontest.py run <repo>`） | 二退縮之合併再試紀錄皆 ＝ `{'退縮': <退縮>, '標的': [], '皆未達': {}}`、逐列 `0`；合成案（退縮 `3.5`·注入於器內之 `ns`）：甲 ⇒ 競合 `R3` 左 `628(4)`（交 `66.49`）／`R5` 右 `628(3)`（交 `237.57`）、`R3` 左強制抵費地 `351.70 ㎡`、`R5` 右鏈首宗 `628-23(2)` `G` `1422.89`；乙 ⇒ 交 `66.49`／`217.29`、`351.70 ㎡`、鏈首宗 `628(3)` `G` `408.48`；丙 ⇒ 交 `66.49`／`207.25`、`351.70 ㎡`、切半 `628(6)` ⇒ `170.7953`／`170.9947`（`R5` 側之比 `0.4997`）、鏈首宗 `628(3)` `G` `408.48`；`R5` 之聯集 △ 街廓皆 `0.0000`、`R3` 皆 `0.0001`、兩兩疊皆 `0.0000`；末列 `⇒ 紅 []；rc 0`（皆 ＝ `W-G.9-354 §一` 項 `6`／`7`）——`F14 run` 以同一判式量畫面路徑，其期同此 |
| `7` | 畫面對 harness（開工態·`F4` 未改·`python verify/probes/probe_WG9345_screen.py parity <R> <退縮> on <json>`） | `3.5` ⇒ `rc 0`（配地列 harness `35`／畫面 `34`·不符格 `0`）；`0.0` ⇒ `rc 0`（`36`／`35`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`——本案合併再試無標的 ⇒ 開工態之畫面雖未辦合併再試，其配地仍與 harness 同 |
| `8` | 量測器於開工態（`f55935c` ＋ 塊 `F14` ＋ 塊 `F4p` ＝ 工項一之端之同內容） | `F14 selftest` ⇒ `rc 1`，末列逐字 `⇒ 紅 ['T1b', 'T1d', 'T1g', 'T1h', 'T1i', 'T1c4', 'T2b', 'T2c', 'T2d', 'T2e', 'T2f', 'T2g', 'T2c4', 'T3b', 'T3c', 'T3e', 'T3f', 'T3g', 'T3h', 'T3i', 'T3c4', 'T9b', 'T9c', 'T9e', 'T9h', 'T9c4', 'T4a', 'T4b', 'T4c', 'T4d', 'T4c4', 'T5a', 'T5b', 'T5c', 'T5d', 'T5c4', 'T8b', 'T8c4', 'TK', '受詞缺']；rc 1`（✅ `36`／🔴 `40` 列；`P0` ✅ `74／74`）；`F14 run` ⇒ `rc 1`，末列 `⇒ 紅 ['受詞缺']；rc 1`；`F4 parity`（塊 `F4p` 施後）`3.5`／`0.0` ⇒ 皆 `rc 1`（「不符 `2` 項」），其紅項**恰**「合併再試 session 鍵 `f3_end_block_merge`」與「`f3_end_block_merge_log`」二列（harness 側 ＝ `{'退縮': 3.5, '標的': [], '皆未達': {}}`／`[]`、`{'退縮': 0.0, …}`／`[]`；畫面側 ＝ `<缺>`），餘項皆 ✅（配地列 `35`／`34`、`36`／`35`·不符格 `0`） |
| `9` | 既有碼之預查（出單前·⛔ 模擬新碼） | 以 harness 之合併再試後之宗地與紀錄（合成案甲乙丙·退縮 `3.5`·注入同 `F13`），跑**既有**之畫面街角選位（真 st）與畫面配地，逐列對 harness 之配地（`F4` 之 `compare_rows`）：甲 ⇒ 配地列 harness `34`／畫面 `33`、不符格 `0`；乙 ⇒ `37`／`36`、`0`；丙 ⇒ `37`／`36`、`0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（同本案之既有同構差）——畫面之強制抵費地路徑（`W-G.9-353` 已入二宿主）與 harness 同；本批之受詞僅為畫面入口之編排與段三畫面試算之 `'trial'` |
| `10` | `F8 run`／`run_all`（開工態） | `python verify/probes/probe_WG9349_k9296.py run <R> 3.5`／`0.0` ⇒ 皆 `rc 0`（態 `f55935c` 與 `758cfba` 之出艙逐位同）；`run_all`（倉外路徑·態 `a44a386`〔`app.py` ＝ 開工態〕）⇒ `64` 項·PASS `28`／FAIL `36`·末端夾具／golden 列 `21`·對帳段 `22／36`·`236056` B（其 bytes 平台與路徑相依·⛔ 入判） |
| `11` | 既有量測器之器紅（`自誤 548`·塊 `E5`） | `python verify/probes/probe_WG9345_screen.py wiring <R>` 於開工態 ⇒ `rc 1`（唯 `W2` 紅：期之名集取 `f3_screen_stepg_run` 之全部 kwonly 參數〔`14`·含 `W-G.9-349` 所增之 `_k929_6_inner=False`〕、`main()` 之呼叫 `13`）；`5eeb95f^` ⇒ `rc 0`、`5eeb95f` ⇒ `rc 1`。塊 `F4p` 改期之名集為**無預設**之 kwonly 參數 ⇒ `f55935c`／`5eeb95f`／`5eeb95f^` 皆 `rc 0`（本部 `W0`〜`W8` 全綠·丙部四突變皆轉紅·器紅 `0`）；`selftest` ⇒ `rc 0`（`10/10`） |

## `§二`　KL 之語與射程

🔒 **流程之令**：KL `2026-09-28 11:43` 逐字：「-354 單貼給新CC施工窗後，CC結果連同交接文(本窗沒出，是否交接chat視窗請判斷)，然後流程改由上1輪討論的：「三、建議的改法（分工不變，只刪重複）」的做法，chat復驗並出規格(或plan)單，由CC依單出生產碼?這樣的流程可行?若可行，就嘗試由下1輪開始該流程」
發單側窗五十答「可行，自下一輪（`W-G.9-355`）試行」；本單即其首張。KL 同日另問 CC 之推理等級，發單側答依規格寫生產碼者 `xhigh`（交接文五十 `§一` 項 `3`）⇒ 本單首載「本單建議等級 ＝ `xhigh`」。
🔒 **所據之裁**：`K-9-49 ②`（KL 裁 `2026-09-27`·末端塊之合併再試）、`K-9-36 ③`（強制抵費地）、`K-9-50`（KL 裁 `2026-09-28 00:30`·數末端塊之相互競合）——harness 路徑已於 `W-G.9-353`／`354` 落地（側支）；`CLAUDE.md`「待落地清單之更新：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑入側支（`W-G.9-354`）」節序 `3`（末端塊之合併再試〔含 `K-9-50`〕·畫面路徑）載其態 ＝ ⬜、出處 ＝ 次單（`W-G.9-355`），其要旨並載「須附畫面路徑之合成案（`自誤 517`）」。本批⛔ 立新裁；`§三` 之諸條皆為「畫面 ＝ harness」之工程要求（⛔ 域裁）。
🔒 **`main()` 內之敘述**（`CLAUDE.md`「🔒 `main()` 內之敘述，`run_all` 不得單獨作為驗收依據」款·`自誤 517`）：本批於 `main()` 內之改動限於成果區之顯示與 `_f3L_invalidate_g_cache` 之二鍵（`R-12`）；其顯示函式 `end_block_merge_rows` 以 `F14 selftest`（`T7`）量之；`main()` 內之二處以假 st 實際執行之合成案，依規格單流程移至復驗（`恆常附款 n③` 之試行期變通·塊 `H1`）。畫面路徑之合成案（`自誤 517`）＝ `F14 run`（本案 ＋ 合成案甲乙丙於畫面路徑實跑·判式逕用 `F13`）。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至側支⛔ 須放行；**主線之推進**（`W-G.9-353`〜`355` 同批）**另單·候 KL 逐字放行**。
🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至側支 `verify/W-G.9-353-endmerge`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及 `app.py` 以外之生產碼、`§三-3` 之禁改、任何他錨；`(d)` ⛔ 建 `GB-194` 三停機款之處置、`K-9-48` 七項 `3`／`5`／`6`、調配之任何後步——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **受詞之總述**：harness 已於 `W-G.9-353`／`354` 辦末端塊之合併再試（`K-9-49 ②`·`K-9-36 ③`·`K-9-50`）——其入口 ＝ `verify/selection_pipeline.py` 之 `run_corner_pk_k6b`（段三之後、無條件）→ `run_end_block_merge` → `app.py` 之 `end_block_merge_run`（單一真相源）。**本批使畫面路徑同之**：畫面之街角選位按鈕（`main()` 內·其本體 ＝ 單一呼叫 `f3_screen_k6b_stage3`）所得之宗地、紀錄與其後之配地，須與 harness 之同名之量逐鍵相同（`F4 parity`）。harness 之碼⛔ 動一字。

### `§三-1`　行為要求（逐條·「給定何種情形、須得何種結果」）

| # | 給定 | 須得 |
|---|---|---|
| `R-1` | 段三之畫面入口 `f3_screen_k6b_stage3` 之三個**正常出口**：① 段三旗標 off；② 段三啟用而段二序為空；③ 段三實辦而成 | 各出口於其**真 st 之街角選位之後**，辦末端塊之合併再試一次（經 `app.py` 之 `end_block_merge_run`·以模組層之名呼叫·⛔ 別名、⛔ 預綁、⛔ 另寫其任何一步）；其輸入之宗地 ＝ 該出口之宗地（③ ＝ 段三之出；①② ＝ 入口之輸入）。段三停機（含其試算中止·現碼之「未產出 winners 表」等）⇒ 合併再試⛔ 辦。 |
| `R-2` | 合併再試之輸入 | 同 harness `run_end_block_merge`：上鎖 ＝ 其時 session `f3_k6b_stage1_locked_by_block` 各值之聯集；街角第 1 宗 ＝ 其時 session `f3_corner_winners` 各值中之非空者；街廓 ＝ `g_kwargs['classified_blocks']` 之 `{label: {'category': category}}`；道路中心線 ＝ session `f3_manual_road_centerlines`（同段三之畫面入口）；歸戶 ＝ session `t8_ownership_map`；退縮 ＝ session `f3L_setback_default`（以 `setback=` 傳入）。「其時」＝ 該出口之真 st 之街角選位之後。 |
| `R-3` | 合併再試之試算（`alloc_eval`／`alloc_state`） | 以畫面自身之二段（`f3_screen_corner_pk_run`／`f3_screen_stepg_run`·代理 st·吃畫面即時之地價·⛔ 借用 harness）為之；**其配地一律於 session `SS_END_BLOCK_MODE` ＝ `'trial'` 下為之**（各筆單獨皆未達之端暫以強制抵費地計·同 harness）。`alloc_eval` 回配地首趟之末端塊評選（session `SS_END_BLOCK_EVAL`）之**深拷貝**；試算中止（代理 st 之 `st.stop`、`RuntimeError`、街角選位未產出 winners 表）⇒ `alloc_eval` 拋 `RuntimeError`（⛔ 以空評選代之·`end_block_merge_run` 之契約）。 |
| `R-4` | 段三之畫面試算（`alloc_state`） | **其配地亦於 `'trial'` 下為之**（harness 自 `W-G.9-353` 已然；現碼之畫面⛔ 設 ⇒ 試算遇各筆單獨皆未達之端即中止·`§一` 項 `5`）。 |
| `R-5` | 段三與合併再試之注入物 | 四注入物（`a_prime`／`trial_winner`／`alloc_state`／`alloc_eval`）由**同一**模組層函式 `k6b_screen_callbacks` 供之（⛔ 二處各寫·單一真相源·體例同 harness `_k6b_callbacks`）；`a_prime`／`trial_winner`／`alloc_state` 之行為，除 `R-4` 外，同本批前之段三畫面入口（逐位）。 |
| `R-6` | 合併再試之試算之隔離 | 試算前存 `K6B_SCREEN_TRIAL_KEYS` 之鍵與 `K917_DROPPED`，試算後（含例外）復原（同段三之畫面入口）。`K6B_SCREEN_TRIAL_KEYS` 增 **`SS_END_BLOCK_MODE` 之值**，使試算旗標於畫面入口結束後（含例外）⛔ 留存於 session（定案之配地 ⇒ 無 `'trial'`）。 |
| `R-7` | 合併再試之紀錄 | 於**復原之後**寫入 session：`SS_END_BLOCK_MERGE` ＝ 其紀錄 `rec`、`'f3_end_block_merge_log'` ＝ 其逐列 `log`（鍵與值之形同 harness）。段三之畫面入口之首（去前次段三之結果處）**一併去此二鍵**——段三或合併再試停機之後，二鍵皆⛔ 在 session（⛔ 殘留前次之紀錄）。 |
| `R-8` | 合併再試之出 | **有變**（回傳之宗地非其輸入之同一物件）⇒ 以真 st 再跑一次街角選位，所用 ＝ 合併再試之出；**無變 ⇒ ⛔ 重跑**。段三之畫面入口之回傳 `temp`／`build` ＝ **末態**（有變 ⇒ 合併再試之出；無變 ⇒ 該出口之宗地·皆同一物件）；其回傳之鍵⛔ 增減（仍 `temp`／`build`／`log`／`order`／`ran`·`log` 仍 ＝ 段三之紀錄）。 |
| `R-9` | 其後之配地所取之宗地 | `k6b_stage3_selected`／`k6b_screen_build_for_g` 所回 ＝ 末態（同一物件）：段三實辦**或**合併再試有變 ⇒ 末態存於 `K6B_SCREEN_STAGE3_KEYS`，其指紋 ＝ `k6b_stage3_fingerprint(<段三前之 build>, 退縮)`（他 build 或他退縮 ⇒ loud·同現碼）；二者皆無 ⇒ ⛔ 存（`k6b_stage3_selected` 回 `None`·同本批前）。 |
| `R-10` | 合併再試停機（拋 `RuntimeError`：`GB-194` 之三情形、段三後處理之停機等） | session `f3_k6b_stage3_error` ＝ 其訊息之首列（含原訊息）、`st.error` ＋ `st.stop()`（同段三之停機）；其後之配地 loud（`k6b_screen_build_for_g` 停）。 |
| `R-11` | 合併再試進行中之中斷（非 `RuntimeError`） | 合併再試開始前，session `f3_k6b_stage3_error` ＝ 未完成之標記，**其文含「末端塊合併再試」**；唯合併再試正常完成（`R-7` 之紀錄已寫）撤之；段三實辦者，段三之未完成標記延至合併再試正常完成始撤。非 `RuntimeError` 之例外 ⇒ 上拋、標記留存（其後之配地 loud）。 |
| `R-12` | 成果區之顯示 | 模組層純函式 `end_block_merge_rows(rec, log)` → `{'lines': [...], 'rows': [...]}`：`rows` ＝ `log` 之逐列（鍵同 `log`、值一律字串，`None` ⇒ `'—'`）；`lines` 載退縮、標的逐端（街廓 ＋「左」／「右」）、競合逐組（其形與各列之街廓、端、候選、交面積〔二位小數〕）、皆未達逐端（＋「強制抵費地」）；標的為空 ⇒ 含「無標的」之一行；有 `試算中止` ⇒ 含「試算中止」與其訊息之一行；`rec` 為 `None` ⇒ `{'lines': [], 'rows': []}`。`main()` 之成果區以之顯示（expander·`rec` 為 `None` ⇒ ⛔ 顯示；位置 ＝ 「🧱 末端塊之評選」之 `if` 句之後、`_adj351_bf` 之賦值之前）；`main()` 之 `_f3L_invalidate_g_cache` 一併去 `R-7` 之二鍵。 |
| `R-13` | harness 與其餘（工項二之 `commit`） | `verify/**` 之一切檔、`app.py` 之 `end_block_*`／`k6b_stage3_run`／`k6_merge_groups`／`solve_G_binary`／`_solve_G_one`／`k929_6_fixpoint`、`f3_screen_corner_pk_run`／`f3_screen_stepg_run`／`_k929_6_screen_gate` 一字不動；harness 之配地與 `run_all` 逐位同（`V-3`／`V-5`）。 |

### `§三-2`　介面（名與簽名·量測器 `F14` 以之為受詞）

| # | 名 | 簽名與回傳 | 呼叫點 |
|---|---|---|---|
| `I-1` | 🆕 `f3_screen_end_block_merge` | `(st, *, pk_kwargs, g_kwargs)` → `{'temp', 'build', 'log', 'rec'}`；`pk_kwargs['temp_parcels']`／`['build_parcels']` ＝ 合併再試之輸入；`g_kwargs` ＝ 同段三之畫面入口之 `g_kwargs` | `f3_screen_k6b_stage3` 之三個正常出口（`R-1`） |
| `I-2` | 🆕 `k6b_screen_callbacks` | `(st, *, pk_kwargs, g_kwargs)` → `{'a_prime', 'trial_winner', 'alloc_state', 'alloc_eval'}` | `f3_screen_k6b_stage3`（段三）與 `f3_screen_end_block_merge`（合併再試）（`R-5`） |
| `I-3` | 🆕 `end_block_merge_rows` | `(rec, log)` → `{'lines': [...], 'rows': [...]}`（純函式） | `main()` 之成果區（`R-12`） |
| `I-4` | 改 `f3_screen_k6b_stage3` | 簽名⛔ 變；回傳之鍵⛔ 變（`R-8`） | `main()` 之街角選位按鈕（⛔ 變） |
| `I-5` | 改 `K6B_SCREEN_TRIAL_KEYS` | 增 `SS_END_BLOCK_MODE` 之值（`R-6`·其形見 `X-3`） | — |

🔒 三新函式皆置於模組層（`harvest` 可取）；函式內⛔ 含案件字面（街廓名、暫編地號、歸戶號等·泛化之約束）。

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

| # | 禁改 | 守之閘 |
|---|---|---|
| `X-1` | `main()` 之街角選位按鈕與配地按鈕二 `If` 之本體一字不動（仍各為單一呼叫 `f3_screen_k6b_stage3(st, pk_kwargs=dict(…10 名…), g_kwargs=dict(…9 名…))`／`f3_screen_stepg_run(st, …, build_parcels=k6b_screen_build_for_g(st, build_parcels))`） | `F4 wiring` `W1`／`W2` 及其突變 |
| `X-2` | `main()` 之 `_f3L_invalidate_g_cache` 仍以 `K6B_SCREEN_STAGE3_KEYS` 與 `'f3_k6b_stage3_error'` 失效（`R-12` 之二鍵係**增列**） | `F4 wiring` `W3` 及突變 `m4` |
| `X-3` | `K6B_SCREEN_TRIAL_KEYS` 之值仍為**可 `ast.literal_eval` 之字串字面之 tuple**；新鍵以字串字面 `'f3_end_block_mode'` 寫入，**插於 `'f3_k929_6_log',` 一列之前**；該列（逐字 `    'f3_k929_6_log',`）與其次列之 `)` 一字不動（末項仍 `f3_k929_6_log`） | `F9 wiring` `W4` 與突變 `M1`；`F10 wiring` `W3`；`F11 wiring` `W7` |
| `X-4` | `main()` 內 `_eb352 = st.session_state.get(SS_END_BLOCK_EVAL)` 與 `end_block_eval_rows(_eb352)` 二句一字不動；`_adj351_bf` 之賦值與其次句（`if`）仍相鄰 | `F11 wiring` `W10`；`F10 wiring` `W5`（其抽取區塊 ＝ 自 `_adj351_bf` 之賦值起連續 `2` 句） |
| `X-5` | `f3_screen_k6b_stage3` 之原文（含 docstring 與註解）中，首個 `k6b_stage3_run(` 字樣即段三之呼叫；自該處至其後首個 `finally:` 之間⛔ 含 `contests` 字樣（段三之呼叫⛔ 給競合） | `F13 wiring` `W3` |
| `X-6` | 新碼⛔ 引 `SS_ADJ_BUILD_FINAL`／`SS_ADJ_DROPPED`／`adj_intake`／`adj_intake_rows`／`'f3_k929_6_build'`／`'f3_k929_6_dropped'`（`main()` 外） | `F10 wiring` `W4` |
| `X-7` | `_WF_NS_NAMES` 一字不動 | `wfns_ast` `48`／`48`／`47` |
| `X-8` | `R-13` 所列之函式一字不動 | `F9`〜`F13 wiring`／`main_synth`／`F12` 之突變錨 |

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`D-1`：本規格之任一條，其二讀法之後果**在土地上相異**（任一宗之 `G`、面積、街角歸屬、抵費地、配地幾何）。
`D-2`：畫面與 harness 之配地、紀錄或宗地有任一相異（`V-1` 之 `F14 run`、`V-2` 之 `parity`），而其成因⛔ 在本單之規格內者。
`D-3`：須動 `R-13`／`§三-3` 之任一字始能滿足 `§三-1`。
🔒 非域上之實作細節（函式內之結構、區域名、註解、錯誤訊息之措辭〔`R-10`／`R-11`／`R-12` 所令之字樣除外〕）由 CC 定之，並於報告 ⑦ 逐項具名其選擇與其由。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐 `R-1`〜`R-13`：落於何函式、何處；`§三-4` 末之實作細節之選擇及其由；對 `§三-3` 各款之自查（逐款具名「未觸」及其據）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py` 之**全文**（報告內嵌或報告同目錄之 `.diff` 檔·⛔ 摘要）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`）

**工項零　本單原封入倉**（側支·零生產碼）：`docs/orders/W-G.9-355_規格單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-355 工項零：本單原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`（快轉）；推後 heads ＝ `31`、主線仍 ＝ `0b05925…`。

**工項一　量測器入倉**（**先於生產碼**·側支·零生產碼）：塊 `F14` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9355_screenmerge.py`（**新檔**）；塊 `F4p` 抽為 `<O>\F4p.diff`、對拍後 `git apply --check <O>\F4p.diff` ⇒ 過；`git apply <O>\F4p.diff`；`git hash-object verify/probes/probe_WG9345_screen.py` ＝ `§五-1` 項 `7`（停機款 `4`）。`commit` 訊息逐字 `W-G.9-355 工項一：量測器 F14（末端塊合併再試之畫面路徑）入倉 ＋ F4 之更新（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

**工項二　生產碼**（🔴 `app.py`·CC 依 `§三` 撰寫·一 `commit`·推側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` ⇒ **`rc 1`**（末列逐字 ＝ `§一` 項 `8` 之 `selftest` 末列）。
2. `python verify/probes/probe_WG9355_screenmerge.py run <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
3. `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_pre.json`；同 `0.0` ⇒ `<O>\parity00_pre.json` ⇒ 皆 **`rc 1`**，其紅項**恰**「合併再試 session 鍵」二列（`§一` 項 `8`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` ⇒ `rc 0`。
6. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫 `app.py` 之改動；`python -m py_compile app.py`；`commit` 訊息逐字 `W-G.9-355 工項二：末端塊之合併再試（含 K-9-50）之畫面路徑 🔴 生產碼（側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9355_screenmerge.py selftest <repo>`；`… run <repo> > <O>\f14_run_post.log` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之諸項（`T1`〜`T9`、`TK`、`TS`、`P0`）皆 ✅；`run` 之 `F13` 判式（`R1` 二退縮、`C`／`F`／`X` 之甲乙丙）皆 ✅，其數 ＝ `§一` 項 `6`；`E` 五列皆 ✅ |
| `V-2` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | 皆 **`rc 0`**；配地列 `3.5` ⇒ harness `35`／畫面 `34`、`0.0` ⇒ `36`／`35`，不符格 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`；「合併再試 session 鍵」二列 ✅ |
| `V-3` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `diff` | 皆 **`rc 0`**、末列 `⇒ 紅 []；rc 0`；**二份之 `diff` 皆空** |
| `V-4` | `python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9345_screen.py wiring <repo>`；`python verify/probes/probe_WG9345_screen.py selftest`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>`；`python verify/probes/probe_WG9340_main_synth.py <repo>`；`python verify/probes/probe_WG9349_k9296.py wiring <repo>`；`python verify/probes/probe_WG9351_intake.py wiring <repo>`；`python verify/probes/probe_WG9352_endblock.py wiring <repo>`；`python verify/probes/probe_WG9353_endmerge.py wiring <repo>`；`python verify/probes/probe_WG9354_endcontest.py wiring <repo>` | 皆 **`rc 0`**；`wfns_ast` **`48`／`48`／`47`**；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F4 wiring` 之 `W0`〜`W8` 皆 ✅ 且四突變皆轉紅 |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |
| `V-6` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`1`**（`app.py`）；其 blob 與增／刪之數出艙（發單側復驗時自倉重算）；`verify/` 之一切檔對工項一之端相異 `0` |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。

**推**（驗皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-353-endmerge`。

**工項三　登記**（側支·零生產碼·一 `commit`）：塊 `E5` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P9` 附於 `CLAUDE.md` 之末；塊 `H1` 附於 `docs/reports/W-G.9波_恆常附款登記表.md` 之末（皆二進位·嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-355 工項三：攢批登記（自誤 548）＋ 待落地清單之更新 ＋ 恆常附款 n③ 之試行期變通（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

**工項四　執行報告入倉**（側支·新檔 `docs/reports/W-G.9-355R_末端塊合併再試之畫面路徑_執行報告.md`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`11` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F14` 二子命令之全文、`parity` 四份之末十列、`F8 run` 二份 `diff` 之結果、`runall` 對拍之全文與 `diff` 之結果）；④ 五塊之實得（bytes／`sha256`）與三檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解；⑦ **設計說明**（`§三-5`）；⑧ **`app.py` 之全文差異**（`§三-5`）；⑨ **各段耗時**（讀單／撰碼／前置／驗／登記／報告·規格單流程之試行評估）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-355 工項四：執行報告入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

### `§四-2`　復驗時補寫者（規格單流程·⛔ 本單之期）

發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：① 以程式字樣為錨之接線檢查（`R-1` 之三出口、`R-5` 之單一真相源、`R-6` 之鍵、`R-12` 之 `main()` 二處）及其突變之判別力；② `main()` 之顯示區塊與 `_f3L_invalidate_g_cache` 以假 st 實際執行之合成案（`自誤 517`）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項一 ＝ `verify/probes/probe_WG9345_screen.py` 增 `15`／刪 `4`；工項二 ＝ `app.py`（增／刪 ＝ 工項二之 `V-6` 所出艙）；其餘逐檔 **`0`** |
| `2` | 生產碼 `34` 檔對 `f55935c` | 相異恰 **`1`**（`app.py` ＝ 工項二之 `V-6` 所出艙之 blob） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`8` 檔：本單、`F14`、`verify/probes/probe_WG9345_screen.py`、`app.py`、自誤簿、`CLAUDE.md`、恆常附款登記表、報告） |
| `4` | 三檔之 bytes | `docs/reports/W-G.9波_claude.ai側自誤登記.md` `1075505` → `1077462`；`CLAUDE.md` `291243` → `295353`；`docs/reports/W-G.9波_恆常附款登記表.md` `59311` → `62376`；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`31`**；主線 ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`（⛔ 變）；`verify/W-G.9-353-endmerge` ＝ 工項四之 `commit`；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 548 547 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 548 547` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `533`／`MAX` `548`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `47`／`50`／`[44, 47]`（缺號集皆 ＝ 開工態；開工態 ＝ 自誤 `532`／`547`） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`48`／`48`／`47`** |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest …`；`… wiring …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9350_frontroad.py selftest …`；`… wiring …`；`… run …` | 同上 |
| `14` | `python verify/probes/probe_WG9351_intake.py selftest …`；`… wiring …`；`… run …` | 同上 |
| `15` | `python verify/probes/probe_WG9352_endblock.py selftest …`；`… wiring …`；`… run …` | 同上 |
| `16` | `python verify/probes/probe_WG9353_endmerge.py selftest …`；`… wiring …`；`… run …` | 同上 |
| `17` | `python verify/probes/probe_WG9354_endcontest.py selftest …`；`… wiring …`；`… run …` | 同上 |
| `18` | `python verify/probes/probe_WG9355_screenmerge.py selftest …`；`… run …` | 同上 |
| `19` | `python verify/probes/probe_WG9345_screen.py parity … 3.5 on <json>`；同 `0.0`；`… wiring …`；`python verify/probes/probe_WG9345_screen.py selftest` | 皆 **`rc 0`**（`parity` 之數 ＝ `V-2`） |

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F14` | `35946` B·`sha256` `324a15099b6e5cbe75872e3f6e426d47877f955748d921b30d33358b80cd38a1`·`736` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9355_screenmerge.py` |
| `3` | 塊 `F4p` | `4752` B·`sha256` `afbe07170647acbd624788dab2d0e49930a9c96d259cfa5216945467584c400b`·`59` 列（圍欄內全文·末附換行）；`git apply` 於 `verify/probes/probe_WG9345_screen.py`（開工態 blob `790060dc315d4f57fc97c09ac48efe006c95ec32`·`48501` B） |
| `4` | 塊 `E5` | `1957` B·`sha256` `51c97be27c199c6f2bab0642fba54a9f6b1972de9e1cc40ceafb12fc729fb500`·`12` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1075505` B）之末後，期末 ＝ `1077462` B |
| `5` | 塊 `P9` | `4110` B·`sha256` `42e0521fd381e9670a1b4e38582e8bb5efc31215b99c8fd3aa0d08671c76ee59`·`22` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`291243` B）之末後，期末 ＝ `295353` B |
| `6` | 塊 `H1` | `3065` B·`sha256` `ce0956460049bfe456c54a2c1ef4e6f0f0aa7588a70ddaec3e324736ca60cfdc`·`31` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_恆常附款登記表.md`（`59311` B）之末後，期末 ＝ `62376` B |
| `7` | 施塊後之 blob（量測器） | `verify/probes/probe_WG9345_screen.py` `92f9dc4d979e37b2967f2a144c5752ee871ee921`（`49785` B·增 `15`／刪 `4`）；`verify/probes/probe_WG9355_screenmerge.py` `3648cd6c6cd13e8b5c6f73ecb95fd2a1feb5d29c`（`35946` B）。🔒 `app.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `8` | 量測器之二態 | 工項一之端：`F14 selftest`／`run` 皆 `rc 1`（`§一` 項 `8`）；`F4 parity` `3.5`／`0.0` 皆 `rc 1`（紅項恰二）；工項二施後：皆 `rc 0` |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十一實跑（態 `f55935c`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-4` `:69`（`§一` 態錨之表頭·所觸之箭頭係項 `3` 所引 `W-G.9-354` 四檔之改前改後 bytes，其座標系 ＝ 該批之改前至改後，同格自載 ⇒ **具名豁免**）、`P-4` `:178`／`:201`（`§四-1` 工項二之驗、`§四-3` 收工閘之表頭·其箭頭之座標系皆為改前〔開工態或工項一之端〕至改後〔工項二之 `commit` 或工項四之端〕，表內自載 ⇒ **具名豁免**）、`P-4` `:1083`（塊 `P9` 之表頭·所觸者係待落地清單之依賴序·其座標系 ＝ 依賴之先後，同節自載 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `19588`–`27245`）⇒ `rc 0` |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````diff `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 側支 `verify/W-G.9-353-endmerge`（工項二於驗皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F14`（新檔 `verify/probes/probe_WG9355_screenmerge.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-355 量測器（發單側窗五十一擬·檔 F14·⛔ 由受單側改一字）：末端塊之合併再試（含 `K-9-50`）之**畫面路徑**。

受詞（`app.py` 模組層·`W-G.9-355` 規格單 `§三` 之介面）：
  f3_screen_end_block_merge(st, *, pk_kwargs, g_kwargs)  合併再試之畫面入口（段三之畫面入口之各正常出口呼之）
  k6b_screen_callbacks(st, *, pk_kwargs, g_kwargs)       段三與合併再試共用之四注入物
                                                          （回 {'a_prime', 'trial_winner', 'alloc_state', 'alloc_eval'}）
  end_block_merge_rows(rec, log)                         成果區之顯示（純函式·回 {'lines': [...], 'rows': [...]}）
  ＋ 既有 `f3_screen_k6b_stage3`（回傳之宗地 ＝ 合併再試後）、`k6b_stage3_selected`、`k6b_screen_build_for_g`、
    `K6B_SCREEN_TRIAL_KEYS`（含 `SS_END_BLOCK_MODE` 之值·末項仍 `f3_k929_6_log`）。

子命令（一律 python verify/probes/probe_WG9355_screenmerge.py <子命令> …）：
  selftest <repo>
           以樁（stub）代畫面二段（`f3_screen_corner_pk_run`／`f3_screen_stepg_run`）、段三本體（`k6b_stage3_run`）與
           合併再試本體（`end_block_merge_run`），⛔ 讀本案資料，量畫面入口之編排（期值出自規格單 `§三`·⛔ 呼叫受測碼求期）：
           T1 段三「段二序為空」之出口 × 合併再試無變／T2 段三旗標 off × 合併再試有變／T3 段三實辦且有變 × 合併再試有變／
           T9 段三實辦且有變 × 合併再試無變／T4 合併再試停機（RuntimeError）／T5 合併再試中斷（非 RuntimeError·旗標 off）／
           T8 段三停機 ⇒ 合併再試⛔ 辦／T6 四注入物（a′、試算選位、試算配地之 `'trial'`、中止即 RuntimeError）／
           T7 顯示／TK 試算隔離之鍵／TS 介面之簽名。P0 ＝ 判式自驗（期值記錄須全綠、逐項擾動須恰該項紅）。
  run      <repo> [<退縮> …]
           畫面路徑實跑本案（預設退縮 `3.5`、`0.0`）與合成案甲乙丙（退縮 `3.5`）：載入 F13
           （`verify/probes/probe_WG9354_endcontest.py`），以本器之畫面管線替其 `_pipeline`，逕用 F13 `run` 之全部判式
           （R1／C／F／X·外部錨由 F13 另寫·⛔ 呼叫受測函式）；注入（末端帶之寬、上鎖、假設跨占街角）同 F13。
           另 E1 試算旗標（`SS_END_BLOCK_MODE`）⛔ 外洩／E2 配地所用之宗地 ＝ 合併再試後／E3 正常出口無停機訊息。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import contextlib, copy, importlib.util, inspect, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

NEW = ("f3_screen_end_block_merge", "k6b_screen_callbacks", "end_block_merge_rows")
SB = 3.5


def _load(repo, rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(repo, *rel.split("/")))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _report(cases):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


# ── 啞 st（selftest 用）──
class _Stop(Exception):
    pass


class _Rerun(Exception):
    pass


class _CM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __call__(self, *a, **k):
        return _CM()

    def __getattr__(self, n):
        return _CM()

    def __iter__(self):
        return iter(())


class _St:
    def __init__(self, ss):
        object.__setattr__(self, "session_state", ss)
        object.__setattr__(self, "msgs", [])

    def stop(self):
        raise _Stop("st.stop")

    def rerun(self, *a, **k):
        raise _Rerun("st.rerun")

    def columns(self, spec, *a, **k):
        return [_CM() for _ in range(spec if isinstance(spec, int) else len(spec))]

    def tabs(self, names, *a, **k):
        return [_CM() for _ in names]

    def __getattr__(self, name):
        def _f(*a, **k):
            self.msgs.append((name, str(a[0])[:300] if a else ""))
            return _CM()
        return _f


# ── 玩具（⛔ 本案資料）──
PPZ = {"Z1": 1000.0, "Z2": 500.0}
CL = {"RD": [(0.0, -5.0), (50.0, -5.0)]}
OWN = {"A": "g1", "B": "g2", "C": "g3", "D": "g1"}
CB = [{"label": "B1", "category": "住宅區"}, {"label": "RD", "category": "道路"}]
EV = {"B1": {"left": {"觸發": True, "R_end(㎡)": 50.0, "候選": [], "當選": "A(1)"}}}
ORDER = [{"最終序位": 1, "街廓": "B1", "端": "左", "暫編地號": "A(1)"}]
L3 = {"序": 1, "街廓": "B1", "端": "左", "候選": "A(1)", "結果": "成"}
LOGM = [{"序": 1, "街廓": "B1", "端": "右", "候選": "B(1)", "結果": "成"}]
RECM = {"標的": [["B1", "right"]], "皆未達": {}}


def _tp(pid, blk, zone, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "所屬街廓": blk, "街廓分類": "住宅區",
            "分攤登記面積_m2": float(a), "面積_m2": 0.0, "重劃前地價區段": zone,
            "polygon_coords": [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]}


def _world():
    t = [_tp("A(1)", "B1", "Z1", 100), _tp("B(1)", "B1", "Z1", 80), _tp("C(1)", "B1", "Z2", 60),
         _tp("D(1)", "RD", "Z2", 30)]
    return t, [t[0], t[1], t[2]]


def _kw(t, b):
    pk = dict(B_value=0.3, C_for_calc=0.1, _build_blocks=[], _corner_rows_init=[{"街廓": "B1", "正面路寬(m)": 8.0}],
              _pd=None, build_parcels=b, post_price_by_block={"B1": 2000.0}, pre_price_by_zone=dict(PPZ),
              sb_rows_by_label={}, temp_parcels=t)
    g = dict(_param_key="p_key", B_value=0.3, C_for_calc=0.1, _tab6_burden=0.4, block_meta_by_label={},
             sb_rows_by_label={}, post_price_by_block={"B1": 2000.0}, pre_price_by_zone=dict(PPZ),
             classified_blocks=copy.deepcopy(CB))
    return pk, g


def _reset(ns, ss):
    ss.clear()
    ss.update({"f3L_setback_default": SB, "t8_ownership_map": dict(OWN), "f3_manual_road_centerlines": copy.deepcopy(CL),
               "p_key": {}, "f3_G_values": ["SENT_G"], ns["SS_END_BLOCK_EVAL"]: {"SENT": 1},
               ns["SS_END_BLOCK_MERGE"]: {"舊紀錄": 1}, "f3_end_block_merge_log": ["舊紀錄"]})
    ns["K917_DROPPED"].clear()
    ns["K917_DROPPED"]["SENT"] = 1


class _Rig:
    """樁：畫面二段、段三本體、合併再試本體。逐次呼叫記錄於 `calls`。"""
    def __init__(self, ns, ss, cfg):
        self.ns, self.ss, self.cfg = ns, ss, cfg
        self.calls, self.merge_n, self.s3_n = [], 0, 0
        self.merge_args = self.merge_ret = self.s3_ret = self.s3_state = None
        self.ev_got = self.ev_same_obj = None
        self.in_s3 = False

    def _real(self, st):
        return not isinstance(st, self.ns["_K6BTrialSt"])

    def pk(self, st, **kw):
        ss = st.session_state
        ids = [t["暫編地號"] for t in kw["temp_parcels"]]
        bids = [b["暫編地號"] for b in kw["build_parcels"]]
        real = self._real(st)
        self.calls.append(("pk", real, ids, bids, kw["temp_parcels"], kw["build_parcels"]))
        ss["f3_corner_winners"] = {"B1": {"p1_end": ids[0], "p2_end": None}}
        ss["f3L_corner_winners"] = {"B1": {"p1_end": ids[0]}}
        ss["f3_corner_cand_diag"] = [{"街廓": "B1", "端": "左", "候選地號": ids[0], "真G(㎡)": 123.45, "門檻(㎡)": 100.0}]
        ss["f3L_forced_offset"] = {}
        ss["f3_corner_range_polys"] = {}
        ss["f3_k6b_stage1_locked_by_block"] = {"B1": [ids[-1]]}
        ss["f3_k6b_stage2_order"] = copy.deepcopy(self.cfg.get("order", []))
        ss["f3_pk_alloc_depth"] = ("real" if real else "trial", len(self.calls), tuple(ids))
        return None

    def g(self, st, **kw):
        ss = st.session_state
        ids = [b["暫編地號"] for b in kw["build_parcels"]]
        self.calls.append(("g", ss.get(self.ns["SS_END_BLOCK_MODE"]), ids, self._real(st), self.in_s3))
        if self.cfg.get("g_stop"):
            st.stop()
        ss["f3_G_values"] = [{"暫編地號": ids[0], "所屬街廓": "B1", "驗_總判": "保留"}]
        ss[self.ns["SS_END_BLOCK_EVAL"]] = copy.deepcopy(EV)
        self.ns["K917_DROPPED"]["X"] = 1
        st.rerun()

    def s3(self, order, locked, own_map, temp_parcels, build_parcels, blocks, centerlines, a_prime, trial_winner,
           alloc_state, *, log_print=print, contests=None):
        self.s3_n += 1
        self.in_s3 = True
        try:
            self.s3_state = alloc_state(temp_parcels, build_parcels)
        finally:
            self.in_s3 = False
        m = self.cfg.get("s3", "same")
        if m == "raise_rt":
            raise RuntimeError("🔴 [K-6-B 段三] 樁之停機 Q8")
        if m == "same":
            self.s3_ret = (temp_parcels, build_parcels)
            return temp_parcels, build_parcels, [dict(L3)]
        t2 = copy.deepcopy(temp_parcels)[:-1]
        by = {x["暫編地號"]: x for x in t2}
        b2 = [by[b["暫編地號"]] for b in build_parcels]
        self.s3_ret = (t2, b2)
        return t2, b2, [dict(L3)]

    def merge(self, temp_parcels, build_parcels, own_map, locked, corner_lots, blocks, centerlines, a_prime,
              alloc_eval, alloc_state, *, setback=None, log_print=print):
        self.merge_n += 1
        self.merge_args = dict(temp=temp_parcels, build=build_parcels, own=dict(own_map or {}), locked=set(locked or ()),
                               corner=set(corner_lots or ()), blocks=copy.deepcopy(blocks),
                               cl=copy.deepcopy(centerlines), setback=setback)
        self.ev_got = alloc_eval(temp_parcels, build_parcels)
        self.ev_same_obj = self.ev_got is self.ss.get(self.ns["SS_END_BLOCK_EVAL"])
        m = self.cfg.get("merge", "same")
        if m == "raise_rt":
            raise RuntimeError("🔴 [末端塊合併再試] 樁之停機 Q9")
        if m == "raise_key":
            raise KeyError("樁之中斷 Q7")
        if m == "same":
            return temp_parcels, build_parcels, [], {"退縮": setback, "標的": [], "皆未達": {}}
        t2 = copy.deepcopy(temp_parcels)
        by = {x["暫編地號"]: x for x in t2}
        b2 = [by[b["暫編地號"]] for b in build_parcels][:-1]
        self.merge_ret = (t2, b2)
        return t2, b2, copy.deepcopy(LOGM), dict(RECM, 退縮=setback)


STUBS = ("f3_screen_corner_pk_run", "f3_screen_stepg_run", "k6b_stage3_run", "end_block_merge_run")


@contextlib.contextmanager
def _rigged(ns, ss, cfg, env):
    rig = _Rig(ns, ss, cfg)
    saved = {k: ns[k] for k in STUBS}
    old_env = os.environ.get("WV_K6B_STAGE3")
    os.environ["WV_K6B_STAGE3"] = env
    ns["f3_screen_corner_pk_run"], ns["f3_screen_stepg_run"] = rig.pk, rig.g
    ns["k6b_stage3_run"], ns["end_block_merge_run"] = rig.s3, rig.merge
    try:
        yield rig
    finally:
        ns.update(saved)
        if old_env is None:
            os.environ.pop("WV_K6B_STAGE3", None)
        else:
            os.environ["WV_K6B_STAGE3"] = old_env


def _enter(ns, ss, pk, g):
    st = _St(ss)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ret = ns["f3_screen_k6b_stage3"](st, pk_kwargs=pk, g_kwargs=g)
        return st, ret, None
    except BaseException as e:  # noqa: BLE001  （含 _Stop）
        return st, None, e


def _selected(ns, ss, b, sb=SB):
    try:
        r = ns["k6b_stage3_selected"](ss, b, sb)
    except RuntimeError as e:
        return ("raise", "請重跑" in str(e))
    if r is None:
        return None
    return ("tuple", r[0], r[1])


def _common(ns, ss, rig, tag):
    """各正常／停機出口共通之期：試算旗標不外洩、試算所改之鍵復原、試算配地一律 'trial'。"""
    gs = [c for c in rig.calls if c[0] == "g"]
    reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
    return [
        (f"{tag}c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）", ns["SS_END_BLOCK_MODE"] in ss, False),
        (f"{tag}c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）",
         (ss.get("f3_G_values"), ss.get(ns["SS_END_BLOCK_EVAL"]), dict(ns["K917_DROPPED"])),
         (["SENT_G"], {"SENT": 1}, {"SENT": 1})),
        (f"{tag}c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫",
         (ss.get("f3_pk_alloc_depth") or ("<缺>",))[0], "real" if reals else "<缺>"),
        (f"{tag}c4 試算配地皆 'trial'（其數 ≥ 1）", (len(gs) >= 1, sorted({c[1] for c in gs}, key=str)), (True, ["trial"])),
    ]


def _stopc(ns, ss, rig, tag):
    """停機出口之共通期（⛔ 含 c3：停機出口未必有真 st 之街角選位）。"""
    c = _common(ns, ss, rig, tag)
    return [c[0], c[1], c[3]]


def _t1(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], merge="same"), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
        a = rig.merge_args or {}
        out = [
            ("T1a 段二序為空之出口：正常結束、ran False", (exc is None, (ret or {}).get("ran")), (True, False)),
            ("T1b 合併再試恰一次、段三本體⛔ 呼", (rig.merge_n, rig.s3_n), (1, 0)),
            ("T1c 無變 ⇒ 回傳之宗地 ＝ 輸入（同一物件）", (ret is not None and ret["temp"] is t0, ret is not None and ret["build"] is b0),
             (True, True)),
            ("T1d 紀錄與逐列入 session", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             ({"退縮": SB, "標的": [], "皆未達": {}}, [])),
            ("T1e 無變 ⇒ 段三之結果⛔ 存（k6b_stage3_selected ＝ None）、無停機訊息",
             (_selected(ns, ss, b0), ss.get("f3_k6b_stage3_error")), (None, None)),
            ("T1f 無變 ⇒ 真 st 之街角選位⛔ 重跑（恰一）", len(reals), 1),
            ("T1g 合併再試之輸入：宗地 ＝ 段三之出（此出口 ＝ 原宗地）",
             (a.get("temp") is t0, a.get("build") is b0), (True, True)),
            ("T1h 合併再試之輸入：上鎖 ＝ 末一次真 st 街角選位之段一上鎖、街角第 1 宗 ＝ 其 winners、街廓／中心線／退縮／歸戶",
             (a.get("locked"), a.get("corner"), a.get("blocks"), a.get("cl"), a.get("setback"), a.get("own")),
             ({"D(1)"}, {"A(1)"}, {"B1": {"category": "住宅區"}, "RD": {"category": "道路"}}, CL, SB, OWN)),
            ("T1i alloc_eval 回試算配地之評選（深拷貝）", (rig.ev_got, rig.ev_same_obj), (EV, False)),
        ]
        out += _common(ns, ss, rig, "T1")
    return out


def _t2(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=ORDER, merge="change"), "off") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
        mr = rig.merge_ret or (None, None)
        sel = _selected(ns, ss, b0)
        _, b_other = _world()
        out = [
            ("T2a 段三旗標 off 之出口：正常結束、ran False", (exc is None, (ret or {}).get("ran")), (True, False)),
            ("T2b 合併再試恰一次、段三本體⛔ 呼", (rig.merge_n, rig.s3_n), (1, 0)),
            ("T2c 有變 ⇒ 回傳之宗地 ＝ 合併再試之出（同一物件）",
             (ret is not None and ret["temp"] is mr[0], ret is not None and ret["build"] is mr[1]), (True, True)),
            ("T2d 紀錄與逐列入 session", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             (dict(RECM, 退縮=SB), LOGM)),
            ("T2e 配地所用之宗地 ＝ 合併再試之出（k6b_stage3_selected·同一物件）",
             (sel is not None and sel[0] == "tuple" and sel[1] is mr[0], sel is not None and sel[0] == "tuple" and sel[2] is mr[1]),
             (True, True)),
            ("T2f 所存之結果繫於段三前之宗地與退縮（他 build 或他退縮 ⇒ loud）",
             (_selected(ns, ss, b_other[:2]), _selected(ns, ss, b0, 0.0)), (("raise", True), ("raise", True))),
            ("T2g 有變 ⇒ 真 st 之街角選位重跑一次、所用 ＝ 合併再試之出",
             (len(reals), bool(reals) and reals[-1][4] is mr[0] and reals[-1][5] is mr[1]), (2, True)),
            ("T2h 無停機訊息", ss.get("f3_k6b_stage3_error"), None),
        ]
        out += _common(ns, ss, rig, "T2")
    return out


def _t3(ns, ss, merge):
    tag = "T3" if merge == "change" else "T9"
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=ORDER, s3="change", merge=merge), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
        s3r = rig.s3_ret or (None, None)
        fin = (rig.merge_ret or (None, None)) if merge == "change" else s3r
        a = rig.merge_args or {}
        gs3 = [c for c in rig.calls if c[0] == "g" and c[4]]
        sel = _selected(ns, ss, b0)
        out = [
            (f"{tag}a 段三實辦之出口：正常結束、ran True、段三紀錄", (exc is None, (ret or {}).get("ran"), (ret or {}).get("log"),
                                                         ss.get("f3_k6b_stage3_log"), ss.get("f3_k6b_stage3_order_used")),
             (True, True, [L3], [L3], ORDER)),
            (f"{tag}b 段三本體與合併再試各恰一次", (rig.s3_n, rig.merge_n), (1, 1)),
            (f"{tag}c 段三之試算配地亦 'trial'", [c[1] for c in gs3], ["trial"]),
            (f"{tag}d 段三之 alloc_state 之出", rig.s3_state, {"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None}),
            (f"{tag}e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位",
             (a.get("temp") is s3r[0], a.get("build") is s3r[1], a.get("locked")), (True, True, {"C(1)"})),
            (f"{tag}f 回傳之宗地 ＝ 末態（同一物件）", (ret is not None and ret["temp"] is fin[0], ret is not None and ret["build"] is fin[1]),
             (True, True)),
            (f"{tag}g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）",
             (sel is not None and sel[0] == "tuple" and sel[1] is fin[0], sel is not None and sel[0] == "tuple" and sel[2] is fin[1]),
             (True, True)),
            (f"{tag}h 紀錄入 session", ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"),
             dict(RECM, 退縮=SB) if merge == "change" else {"退縮": SB, "標的": [], "皆未達": {}}),
            (f"{tag}i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）",
             (len(reals), bool(reals) and reals[-1][4] is fin[0]), (2 if merge == "change" else 1, True)),
            (f"{tag}j 無停機訊息", ss.get("f3_k6b_stage3_error"), None),
        ]
        out += _common(ns, ss, rig, tag)
    return out


def _t4(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], merge="raise_rt"), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        err = str(ss.get("f3_k6b_stage3_error") or "")
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ns["k6b_screen_build_for_g"](_St(ss), b0)
            bfg = "未擋"
        except _Stop:
            bfg = "st.stop"
        except BaseException as e:  # noqa: BLE001
            bfg = type(e).__name__
        out = [
            ("T4a 合併再試停機 ⇒ 畫面 st.error ＋ st.stop", (type(exc).__name__ if exc else None,
                                                   any(n == "error" and "Q9" in m for n, m in st.msgs)), ("_Stop", True)),
            ("T4b 停機訊息入 session（含合併再試之原訊息）", "Q9" in err, True),
            ("T4c 其後之配地 loud（k6b_stage3_selected raise「請重跑」；k6b_screen_build_for_g ⇒ st.stop）",
             (_selected(ns, ss, b0), bfg), (("raise", True), "st.stop")),
            ("T4d 前次之紀錄已去、本次⛔ 寫", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             ("<缺>", "<缺>")),
        ]
        out += _stopc(ns, ss, rig, "T4")
    return out


def _t5(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], merge="raise_key"), "off") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        err = str(ss.get("f3_k6b_stage3_error") or "")
        out = [
            ("T5a 合併再試中斷（KeyError）⇒ 例外上拋", type(exc).__name__ if exc else None, "KeyError"),
            ("T5b 未完成之標記留存（其文含「末端塊合併再試」）", "末端塊合併再試" in err, True),
            ("T5c 其後之配地 loud（k6b_stage3_selected raise「請重跑」）", _selected(ns, ss, b0), ("raise", True)),
            ("T5d 前次之紀錄已去", ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), "<缺>"),
        ]
        out += _stopc(ns, ss, rig, "T5")
    return out


def _t8(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=ORDER, s3="raise_rt", merge="same"), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        out = [
            ("T8a 段三停機 ⇒ st.stop；合併再試⛔ 辦", (type(exc).__name__ if exc else None, rig.merge_n), ("_Stop", 0)),
            ("T8b 前次之紀錄已去（⛔ 殘留舊紀錄）", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             ("<缺>", "<缺>")),
            ("T8c 停機訊息含段三之原訊息", "Q8" in str(ss.get("f3_k6b_stage3_error") or ""), True),
        ]
        out += _stopc(ns, ss, rig, "T8")
    return out


def _t6(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    out = []
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[]), "on") as rig:
        st = _St(ss)
        cb = ns["k6b_screen_callbacks"](st, pk_kwargs=pk, g_kwargs=g)
        out.append(("T6a 四注入物之名", sorted(cb), ["a_prime", "alloc_eval", "alloc_state", "trial_winner"]))
        out.append(("T6b a′ ＝ a(src) × p(src) ÷ p(dst)（100 × 1000 ÷ 500）", round(cb["a_prime"](t0[0], t0[2]), 9), 200.0))
        with contextlib.redirect_stdout(io.StringIO()):
            tw = cb["trial_winner"](t0, b0, "B1", "左", "A(1)")
        out.append(("T6c 試算選位回 (winner, 真G, 門檻)", tw, ("A(1)", 123.45, 100.0)))
        n0 = len(rig.calls)
        with contextlib.redirect_stdout(io.StringIO()):
            stt = cb["alloc_state"](t0, b0)
        gs = [c for c in rig.calls[n0:] if c[0] == "g"]
        out.append(("T6d 試算配地（alloc_state）之出與其 'trial'", (stt, [c[1] for c in gs]),
                    ({"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None}, ["trial"])))
        n0 = len(rig.calls)
        with contextlib.redirect_stdout(io.StringIO()):
            ev = cb["alloc_eval"](t0, b0)
        gs = [c for c in rig.calls[n0:] if c[0] == "g"]
        out.append(("T6e 試算配地（alloc_eval）回評選之深拷貝、其 'trial'",
                    (ev, ev is ss.get(ns["SS_END_BLOCK_EVAL"]), [c[1] for c in gs]), (EV, False, ["trial"])))
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], g_stop=True), "on") as rig:
        cb = ns["k6b_screen_callbacks"](_St(ss), pk_kwargs=pk, g_kwargs=g)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                cb["alloc_eval"](t0, b0)
            got = "無例外"
        except RuntimeError:
            got = "RuntimeError"
        except BaseException as e:  # noqa: BLE001
            got = type(e).__name__
        out.append(("T6f 試算配地中止（st.stop）⇒ alloc_eval 拋 RuntimeError", got, "RuntimeError"))
    _reset(ns, ss)
    return out


REC_D = {"退縮": 3.5, "標的": [["RA", "left"], ["RB", "right"]], "皆未達": {"RA": ["left"]},
         "競合": [{"形": "一", "列": [["RA", "左", "P(4)", 66.49], ["RB", "右", "P(3)", 237.57]]}]}
LOG_D = [{"序": 1, "街廓": "RB", "端": "右", "候選": "P(3)", "結果": "成", "檢核": None},
         {"序": "後處理", "街廓": "RB", "端": "右", "候選": "P(4)", "結果": "成", "檢核": "通過"}]


def _t7(ns):
    f = ns["end_block_merge_rows"]
    v = f(copy.deepcopy(REC_D), copy.deepcopy(LOG_D))
    txt = "\n".join(v.get("lines") or [])
    need = ["RA", "RB", "左", "右", "P(4)", "P(3)", "66.49", "237.57", "強制抵費地", "3.5"]
    v2 = f({"退縮": 0.0, "標的": [], "皆未達": {}}, [])
    v3 = f({"退縮": 3.5, "標的": None, "皆未達": {}, "試算中止": "🔴 樁之中止 Q6"}, [])
    t3 = "\n".join(v3.get("lines") or [])
    return [
        ("T7a 逐列 ＝ 紀錄之列（值一律字串·None ⇒ —）", v.get("rows"),
         [{k: ("—" if x is None else str(x)) for k, x in r.items()} for r in LOG_D]),
        ("T7b 行內載標的之街廓與端、競合之候選與交面積、皆未達 ⇒ 強制抵費地、退縮", [s for s in need if s not in txt], []),
        ("T7c 無標的 ⇒ 行含「無標的」、逐列空", (any("無標的" in s for s in (v2.get("lines") or [])), v2.get("rows")),
         (True, [])),
        ("T7d 試算中止 ⇒ 行含「試算中止」與其訊息", ("試算中止" in t3, "Q6" in t3), (True, True)),
        ("T7e 無紀錄 ⇒ 空", f(None, None), {"lines": [], "rows": []}),
    ]


def _tk(ns):
    keys = tuple(ns.get("K6B_SCREEN_TRIAL_KEYS") or ())
    return [("TK 試算隔離之鍵含 SS_END_BLOCK_MODE 之值、末項仍 f3_k929_6_log",
             (ns["SS_END_BLOCK_MODE"] in keys, keys[-1:] == ("f3_k929_6_log",)), (True, True))]


def _ts(ns):
    def sig(fn):
        p = inspect.signature(ns[fn]).parameters.values()
        return ([x.name for x in p if x.kind in (x.POSITIONAL_ONLY, x.POSITIONAL_OR_KEYWORD)],
                sorted(x.name for x in p if x.kind == x.KEYWORD_ONLY))
    return [("TS 三介面之簽名", [sig(f) for f in NEW],
             [(["st"], ["g_kwargs", "pk_kwargs"]), (["st"], ["g_kwargs", "pk_kwargs"]), (["rec", "log"], [])])]


def _perturb(v):
    if isinstance(v, bool):
        return not v
    return ("<擾>", repr(v)[:40])


def selftest(repo):
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        ns, fake_st = _harvest(repo)
        ss = fake_st.session_state
        miss = [n for n in NEW if n not in ns]
        print(f"── 受詞：{list(NEW)} ⇒ 缺 {miss} ──")
        cases = []
        for tag, fn in (("T1", _t1), ("T2", _t2), ("T3", lambda a, b: _t3(a, b, "change")),
                        ("T9", lambda a, b: _t3(a, b, "same")), ("T4", _t4), ("T5", _t5), ("T8", _t8)):
            try:
                cases += fn(ns, ss)
            except Exception as e:  # noqa: BLE001
                cases.append((f"{tag}例外", ("例外", type(e).__name__, str(e)[:160]), "無例外"))
        cases += _tk(ns)
        if not miss:
            try:
                cases += _t6(ns, ss)
            except Exception as e:  # noqa: BLE001
                cases.append(("T6 例外", ("例外", type(e).__name__, str(e)[:160]), "無例外"))
            try:
                cases += _t7(ns)
            except Exception as e:  # noqa: BLE001
                cases.append(("T7 例外", ("例外", type(e).__name__, str(e)[:160]), "無例外"))
            cases += _ts(ns)
        print("── 合成對照（樁·期值出自規格單 §三）──")
        red = _report(cases)
        if miss:
            print(f"  🔴 受詞缺：{miss}（T6／T7／TS 無從量）")
            red.append("受詞缺")
        print("── P0 判式自驗（期值記錄須全綠；逐項擾動須恰該項紅）──")
        p0 = [n for n, g, e in cases if e != e]                        # 期值自身須自等
        flips = 0
        for i, (n, g, e) in enumerate(cases):
            alt = [(m, (_perturb(ee) if j == i else ee), ee) for j, (m, gg, ee) in enumerate(cases)]
            bad = [m for m, gg, ee in alt if gg != ee]
            flips += (bad == [n])
        ok0 = not p0 and flips == len(cases)
        print(("  ✅" if ok0 else "  🔴") + f" P0 期值記錄全綠 {not p0}；逐項擾動恰該項紅 {flips}／{len(cases)}")
        if not ok0:
            red.append("P0")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：畫面路徑之管線（注入同 F13·判式逕用 F13）──
def _screen_pipeline_factory(f13, f4, extra):
    def _pipeline(ns, fake_st, rv, sb, scen=None):
        import numpy as np
        from shapely.geometry import Polygon
        from shapely.ops import unary_union
        saved = {k: ns[k] for k in ("end_block_host", "end_block_merge_run", "end_block_side_geom")}
        cfg = f13.SCEN.get(scen) or dict(wid={}, lock=[], excl=[])
        hits = {"host": 0, "merge": 0, "geo": 0}
        msig = inspect.signature(saved["end_block_merge_run"])

        def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
            w = cfg["wid"].get((_label, side))
            if w is None:
                return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
                                                    min_width, side, _label=_label)
            hits["geo"] += 1
            p1 = np.asarray(corner_pt, float)[:2]
            dd = np.asarray(d_hat, float)[:2]
            sp2 = float(np.dot(np.asarray(front_p2, float)[:2] - p1, dd))
            e = p1 if side == "left" else p1 + sp2 * dd
            band = ns["_end_band"](block_poly, cad_alloc, e, w, _label=_label)
            rr = ns["_strip_s_range"](band, d_hat, corner_pt, allocation_dir)
            buf = float(rr[1]) if side == "left" else float(sp2 - float(rr[0]))
            return {"gate": True, "unfront": 0.0, "s_back": 0.0, "r_end": band, "r_end_area": float(band.area),
                    "band_area": float(band.area), "buf": buf}

        def host(ordered, **kw):
            if cfg["excl"]:
                crp = dict(kw["corner_range_polys"])
                fake = [Polygon(e["tp"]["polygon_coords"]).buffer(0) for e in ordered
                        if e["tp"].get("暫編地號") in cfg["excl"]]
                if fake:
                    hits["host"] += 1
                    for sd in ("left", "right"):
                        crp[sd] = unary_union(fake + ([crp[sd]] if crp.get(sd) is not None else []))
                kw["corner_range_polys"] = crp
            return saved["end_block_host"](ordered, **kw)

        def merge(*a, **k):
            ba = msig.bind(*a, **k)
            if cfg["lock"]:
                hits["merge"] += 1
                ba.arguments["locked"] = set(ba.arguments["locked"] or ()) | set(cfg["lock"])
            return saved["end_block_merge_run"](*ba.args, **ba.kwargs)
        ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            out = dict(cb_by=cb_by, cad=cad, snapshot=snapshot, params=params, hits=hits, err=None, temp0=temp_p)
            ss = fake_st.session_state
            pk, g = f4._screen_inputs(ns, fake_st, snapshot, list(cb_by.values()), cad, params, temp_p, build_p, sb)
            qs = f4.QuietSt(ss)
            ns["K917_DROPPED"].clear()
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    ret = ns["f3_screen_k6b_stage3"](qs, pk_kwargs=pk, g_kwargs=g)
            except f4._Stop:
                out["err"] = ("畫面·段三／合併再試", str(qs.msgs[-3:])[:400])
                return out
            except RuntimeError as e:
                out["err"] = ("畫面·段三／合併再試", str(e).splitlines()[0][:400])
                return out
            out["rec"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_MERGE"]))
            out["log"] = copy.deepcopy(ss.get("f3_end_block_merge_log") or [])
            out["temp"], out["build"] = ret["temp"], ret["build"]
            e1 = ns["SS_END_BLOCK_MODE"] not in ss
            e3 = "f3_k6b_stage3_error" not in ss
            try:
                sel = ns["k6b_stage3_selected"](ss, build_p, sb)
                bfg = build_p if sel is None else sel[1]
            except RuntimeError:
                bfg = None
            e2 = bfg is not None and bfg is ret["build"]
            extra.append((sb, scen, e1, e2, e3))
            if bfg is None:
                out["err"] = ("畫面·配地前", "k6b_stage3_selected 停機")
                return out
            ns["K917_DROPPED"].clear()
            rows = f4._run_screen_g(ns, qs, g, bfg, lambda s: None)
            if rows is None:
                out["err"] = ("畫面·配地", str(qs.msgs[-3:])[:400])
                return out
            out["ev"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_EVAL"]) or {})
            out["rows"] = rows
            return out
        finally:
            for k, v in saved.items():
                ns[k] = v
    return _pipeline


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    ns, _ = _harvest(repo)
    miss = [n for n in NEW if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    f13 = _load(repo, "verify/probes/probe_WG9354_endcontest.py", "f13_for_f14")
    f4 = _load(repo, "verify/probes/probe_WG9345_screen.py", "f4_for_f14")
    extra = []
    f13._pipeline = _screen_pipeline_factory(f13, f4, extra)
    print("── F13 之判式施於畫面路徑（R1 本案·C／F／X 合成案甲乙丙）──")
    rc13 = f13.run(repo, sbs)
    if rc13 == 3:
        print("⇒ rc 3（F13 之判式無從判定·畫面路徑執行中止）")
        return 3
    red = [] if rc13 == 0 else [f"F13判式 rc {rc13}"]
    print("── E：畫面路徑之專項 ──")
    for sb, scen, e1, e2, e3 in extra:
        tag = f"{sb}{'·' + scen if scen else ''}"
        ok = e1 and e2 and e3
        print(("  ✅" if ok else "  🔴") + f" E@{tag}：試算旗標⛔ 外洩 {e1}；配地所用之宗地 ＝ 合併再試後 {e2}；無停機訊息 {e3}")
        if not ok:
            red.append(f"E@{tag}")
    n_exp = len(sbs) + 3
    if len(extra) != n_exp:
        print(f"  🔴 E 之量 {len(extra)}（期 {n_exp}·畫面入口未全數跑畢）")
        red.append("E量")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], argv[2]
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `F4p`（`git apply` 之差異·`verify/probes/probe_WG9345_screen.py`）

````diff
diff --git a/verify/probes/probe_WG9345_screen.py b/verify/probes/probe_WG9345_screen.py
index 790060d..92f9dc4 100644
--- a/verify/probes/probe_WG9345_screen.py
+++ b/verify/probes/probe_WG9345_screen.py
@@ -21,6 +21,9 @@
            on ：畫面（f3_screen_k6b_stage3 → f3_screen_stepg_run〔段三後之 build〕）對 harness
                 （run_corner_pk_k6b → run_step_g〔段三後之 build〕）；另驗 session 之回復與 K917_DROPPED。
            s3off：同 on 之二路徑，惟旗標 WV_K6B_STAGE3=off（二側皆須回到段三前·紀錄為空）。
+           🔧 `W-G.9-355`（發單側窗五十一·⛔ 上列一字不刪）：on／s3off 另驗末端塊合併再試之二 session 鍵
+           （`SS_END_BLOCK_MERGE` 之值／`f3_end_block_merge_log`）與 harness 同；二鍵係畫面入口之正當輸出，
+           ⛔ 計入「session 之回復」之外洩；試算旗標 `SS_END_BLOCK_MODE` 仍計入（⛔ 外洩）。
            配地列以暫編地號對齊；一側獨有之列須「幾何面積 0 且 G 0」（零面積池列·逐一出艙為 Z），餘須全等；
            cut_coords 以環（去閉合點·容旋轉與反向）比對。--perturb：將畫面側之 B 值乘 1.0001（必紅造）。
   wiring   <repo>
@@ -29,6 +32,7 @@
            W3 _f3L_invalidate_g_cache 失效段三之鍵；W4 wf_f4.compute 之五呼叫點皆以 k6b_f4_ctx 為首參；
            W5 _build_wf_ctx 依段三取 build／temp（ctx 仍 14 鍵）；W6 步驟 M 之讀；W7 過時之說明已去；W8 候選診斷表入 session。
            本部全綠時另施四種 AST 突變，須逐一轉紅（器紅 ⇒ rc 1）。
+           🔧 `W-G.9-355`（`自誤 548`·⛔ 上列一字不刪）：W1／W2 之期之名集取**無預設**之 kwonly 參數。
   f4ctx    <repo>        verify/selection_pipeline.py 之 k6b_f4_ctx 之單元檢。
   wfctx    <repo> <退縮>  _build_wf_ctx 之四情形：無段三之鍵／段三仍適用／指紋不符（二造）／前次停機。
   selftest 合成對照（⛔ 讀倉）：ast 之四種突變皆紅、原封者綠；列比對之擾動紅、環旋轉綠、零面積列入 Z。
@@ -543,6 +547,11 @@ def cmd_parity(repo, sb, mode, out=None, perturb=False):
             ok = _same(REF.get(k, "<缺>"), ssS_pk.get(k, "<缺>"))
             bad += (not ok)
             say(f"  {'✅' if ok else '🔴'} 段三 session 鍵 {k}（{len(REF.get(k) or [])} 列）")
+        EBM = (ns["SS_END_BLOCK_MERGE"], "f3_end_block_merge_log")   # 🔧 `W-G.9-355`：末端塊合併再試之二鍵
+        for k in EBM:
+            ok = _same(REF.get(k, "<缺>"), ssS_pk.get(k, "<缺>"))
+            bad += (not ok)
+            say(f"  {'✅' if ok else '🔴'} 合併再試 session 鍵 {k}（harness {REF.get(k, '<缺>')!r:.80}）")
         idsH = [(t["暫編地號"], t.get("段三併出")) for t in tH]
         idsS = [(t["暫編地號"], t.get("段三併出")) for t in tS2]
         ok = idsH == idsS
@@ -563,9 +572,9 @@ def cmd_parity(repo, sb, mode, out=None, perturb=False):
         bad += (not ok)
         say(f"  {'✅' if ok else '🔴'} K917_DROPPED（段三畢·與 harness 同）")
         leak = [k for k in pre if k not in PK_WRITES and not k.startswith("f3_k6b_stage3")
-                and k != "f3_corner_cand_diag" and not _same(pre.get(k), ssS_pk.get(k))]
+                and k != "f3_corner_cand_diag" and k not in EBM and not _same(pre.get(k), ssS_pk.get(k))]
         newk = sorted(k for k in ssS_pk if k not in pre and k not in PK_WRITES and not k.startswith("f3_k6b_stage3")
-                      and k != "f3_corner_cand_diag")
+                      and k != "f3_corner_cand_diag" and k not in EBM)
         ok = not leak and not newk
         bad += (not ok)
         say(f"  {'✅' if ok else '🔴'} session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵"
@@ -625,8 +634,10 @@ def wiring_check(srcs, say):
         chk(fn in fns, f"W0 模組層有 def {fn}")
     if not all(fn in fns for fn in (FN_PK, FN_G, FN_S3)):
         return bad
-    pk10 = [a.arg for a in fns[FN_PK].args.kwonlyargs]
-    g13 = [a.arg for a in fns[FN_G].args.kwonlyargs]
+    # 🔧 `W-G.9-355`（`自誤 548`）：期之名集 ＝ **無預設**之 kwonly 參數（`W-G.9-349` 於 FN_G 增有預設之
+    #   `_k929_6_inner=False`〔入池閘之試算趟專用·main() ⛔ 傳〕⇒ 舊式以全部 kwonly 為期，W2 自 `5eeb95f` 起恆紅）。
+    pk10 = [a.arg for a, d in zip(fns[FN_PK].args.kwonlyargs, fns[FN_PK].args.kw_defaults) if d is None]
+    g13 = [a.arg for a, d in zip(fns[FN_G].args.kwonlyargs, fns[FN_G].args.kw_defaults) if d is None]
     # W1
     ifn = _target_if(main, lines, KEY_PK)
     ok = False
````

## 附錄丙　塊 `E5`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-355 §零-1`）：本批取 `548`（`1` 號）；係發單側窗五十一於擬 `W-G.9-355` 時，以開工態實跑既有量測器所捕。

### 🩸 `自誤 548`　**`W-G.9-349` 於 `f3_screen_stepg_run` 增有預設之 kwonly 參數 `_k929_6_inner`，未同批更新檔 `F4`（`verify/probes/probe_WG9345_screen.py`）之 `wiring` ⇒ 其 `W2` 自 `5eeb95f` 起恆紅**

**形**：`F4 wiring` 之 `W2` 以 `f3_screen_stepg_run` 之**全部** kwonly 參數為 `main()` 配地按鈕區之單一呼叫之期之名集；`W-G.9-349` 工項二（`5eeb95f`）增 `_k929_6_inner=False`（入池閘之試算趟專用·`main()` ⛔ 傳）⇒ 期之名集 `14`、呼叫之關鍵字 `13` ⇒ `W2` 紅、`rc 1`（其丙部之突變因「本部已紅」而略）。發單側窗五十一實跑（`python verify/probes/probe_WG9345_screen.py wiring <R>`·`<R>` ＝ 各態之 `app.py` 與四呼叫點檔）：`5eeb95f^` ⇒ `rc 0`（本部全綠·四突變皆轉紅）；`5eeb95f` ⇒ `rc 1`（唯 `W2` 紅）；`f55935c` ⇒ `rc 1`（唯 `W2` 紅）。`W-G.9-349`〜`354` 之驗與收工閘皆⛔ 含 `F4 wiring`（唯 `F4 parity`），故未觸。
**後果之界**：`main()` 之二按鈕區於其間未改——`W-G.9-355` 塊 `F4p`（期之名集取**無預設**之 kwonly 參數）施後，`f55935c` ⇒ `rc 0`（本部全綠·四突變皆轉紅）、`5eeb95f` 與 `5eeb95f^` 亦皆 `rc 0` ⇒ 其間⛔ 漏捕任何接線之變。零土地後果；零入倉之生產碼。
**根因**：改宿主函式之簽名時，未以該函式名全倉查以之為受詞之量測器並實跑之；收工閘所列之器未含其 `wiring`。
**後果之框**：🟢 零土地後果；🟡 一器之一項於六批間失其判別力（其受詞未變）。攔點 ＝ **發單側窗五十一**（擬 `W-G.9-355` 時以開工態實跑）。
**攔法**：`W-G.9-355` 塊 `F4p`；`W-G.9-355` 之驗 `V-4` 與收工閘 `19` 含 `F4 wiring`。⛔ 新立款。
````

## 附錄丁　塊 `P9`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：末端塊之合併再試（含 `K-9-50`）之畫面路徑入側支；規格單流程之試行（`W-G.9-355`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `f55935cb95b5e6c058231ee89d5dd19e3a291456`（本批開工態·側支 `verify/W-G.9-353-endmerge` 之端）；本批之 `commit` 皆在同一側支（主線⛔ 動）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 末端塊之合併再試（`K-9-49 ②`·`K-9-36 ③`·`K-9-50`）·畫面路徑 | 段三之畫面入口 `f3_screen_k6b_stage3` 之三個正常出口皆辦合併再試（`f3_screen_end_block_merge`·單一真相源 `end_block_merge_run`）；段三與合併再試之畫面試算共用 `k6b_screen_callbacks`，其配地一律 `'trial'`（段三之畫面試算自本批起亦然）；紀錄入 `SS_END_BLOCK_MERGE`／`f3_end_block_merge_log`；其後之配地依合併再試後之宗地；成果區「末端塊之合併再試」（`end_block_merge_rows`） | 🔶（側支·harness 與畫面二路徑皆入；入主線另候 KL 放行） | `docs/orders/W-G.9-355_規格單.md` |
| `2` | 畫面路徑之接線檢查與 `main()` 內之敘述之合成案（`自誤 517`） | 以程式字樣為錨之接線與突變檢查（含 `main()` 之顯示區塊與 `_f3L_invalidate_g_cache` 之二鍵以假 st 實際執行）——規格單流程下，發單側讀 CC 之碼後補寫，另以零生產碼之單入倉 | ⬜ | 次單 |
| `3` | `W-G.9-353`〜`355` 同批入主線 | 候 KL 逐字放行（主 checkout 同步後，執行介面之環境 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6` 皆須未設） | ⬜ | — |
| `4` | 一筆土地同時跨占同一街廓二末端塊之 `R_end`；同一末端塊屬二以上之競合；三個以上末端塊之競合 | 碼面停機（逐案呈核）；畫面路徑同之（本表序 `1`） | ⬜ | `GB-194`；`K-9-50` 射程 ③ |
| `5` | `K-9-48` 七項 `3`／`5`／`6` | 同「待落地清單之更新：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑入側支（`W-G.9-354`）」節序 `5` | ⬜ | 同左 |
| `6` | 規格步 `3`〜`8`（候選街廓名單 → 同歸戶合併 → 末端塊與中間調配池之進入與落位 → ½ 之判與出口 → 終態與出艙） | 同上節序 `6`〜`10` | ⬜ | 規格步 `3`〜`8` |

🔒 **前節之更新**：「待落地清單之更新：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑入側支（`W-G.9-354`）」節序 `3`（末端塊之合併再試〔含 `K-9-50`〕·畫面路徑·「⬜ 次單（`W-G.9-355`）」）自本批起 ＝ 🔶（本表序 `1`）；⛔ 追改前節一字。
🔒 **規格單流程之試行**（KL `2026-09-28 11:43` 令·自本批起兩輪）：生產碼由 CC 依規格單撰寫；發單側出規格、量測器與驗收，復驗後補接線檢查；出單前⛔ 整套模擬——其與 `恆常附款 n③` 之關係 ＝ `docs/reports/W-G.9波_恆常附款登記表.md` 之「恆常附款 `n③` 之試行期變通（`W-G.9-355`）」節。
🔒 **本案之量**：態 `f55935c` ＋ 本批·harness 之碼⛔ 動 ⇒ 其配地與 `run_all` 逐位同；畫面路徑之配地與 harness 逐鍵同（`verify/probes/probe_WG9345_screen.py parity`·退縮 `3.5`／`0.0`）；合併再試二退縮皆無標的。合成案之量（畫面路徑）＝ `verify/probes/probe_WG9355_screenmerge.py run`（判式逕用 `verify/probes/probe_WG9354_endcontest.py` 之 `run`）。
🔒 **依賴序**：序 `1`（本批·側支）→ 序 `2`（次單·零生產碼）→ 序 `3`（另候 KL 放行）→ 序 `6`；序 `4` 觸發時逐案呈核；序 `5` 另單；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級）。
🔒 **本機介面**：主線之生產碼⛔ 變（本批之生產碼只推側支）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `10`（子字串框·含圖例與本列）·列 ＝ `8`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄戊　塊 `H1`（附於 `docs/reports/W-G.9波_恆常附款登記表.md` 之末）

````markdown

---

## 🔧 恆常附款 `n③` 之試行期變通（`W-G.9-355`·⛔ 上文一字不刪·純末端追加）

🛑 **本節⛔ 鑄任何號**——其⛔ 新立款、⛔ 修訂 `n③` 之字面；係**試行期之變通**之登記（期滿由發單側向 KL 報告續否）。
🔒 **態** ＝ `f55935cb95b5e6c058231ee89d5dd19e3a291456`（`W-G.9-355` 開工態）。

### ① 緣由

KL `2026-09-28 11:43` 逐字：「-354 單貼給新CC施工窗後，CC結果連同交接文(本窗沒出，是否交接chat視窗請判斷)，然後流程改由上1輪討論的：「三、建議的改法（分工不變，只刪重複）」的做法，chat復驗並出規格(或plan)單，由CC依單出生產碼?這樣的流程可行?若可行，就嘗試由下1輪開始該流程」
發單側窗五十答可行、自 `W-G.9-355` 試行。規格單流程下，生產碼由 CC 依規格單撰寫 ⇒ **受詞為本單新寫之生產碼之閘**，其「出單前以一個既知必過之實例跑一次」（`n③`）於出單時**結構上不可得**（受詞尚未存在）；歷批單 `§五-1` 之「收工閘之模擬」（發單側於拋棄式 worktree 預施其自擬之生產碼塊）亦隨「發單側⛔ 寫生產碼」而無所施。

### ② 變通（試行期 ＝ 自 `W-G.9-355` 起兩輪）

| 閘之類 | 必破之實例 | 必過之實例 |
|---|---|---|
| 受詞為本單新寫之生產碼者 | **仍於出單前實跑**：量測器於開工態須紅，其出艙載於單內（⛔ 變） | ① **出單前**：判式自驗——以期值記錄餵判式須全綠、逐項擾動須恰該項紅（「依閘之字面構造之」）；② 其判式與既有閘同者，以既有路徑之已綠實跑為證，並於單內具名；③ 受詞之實跑 ＝ CC 施工時之實跑 ＋ 發單側復驗時自倉重跑 |
| 其餘之閘（既有閘、登記之嚴格前綴、取號等） | 同 `n③` | 同 `n③` |

🔒 **⛔ 變者**：恆紅與恆綠同判為器紅；⛔ 以散文論證「應可滿足」代之——本變通只移受詞為新碼之閘之**必過之實例**之時點，⛔ 免之。
🔒 **試行期之停機款（CC）**：量測器紅而須改量測器始能過 ⇒ 停機（⛔ 改器）；規格有歧義而涉域上判斷 ⇒ 停機；本案配地有任一改變而單未載其期 ⇒ 停機。
🔒 **以程式字樣為錨之接線與突變檢查**：須待碼成方能寫 ⇒ 移至復驗（發單側讀 CC 之碼後補寫，另以零生產碼之單入倉）；其判別力（突變須轉紅）仍依 `n③`。

### ③ 款數之算式（`恆常附款 f`·⛔ 直接寫一個數）

期初 ＝ **`28`** 款（列舉 ＝ `a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab`）＋ 本節新立 `0`／修訂 `0` ⇒ 期末 ＝ **`28`**。

### ④ `恆常附款 a`／`ab①` 對本節之施行

本節之變通，已於出單前對 `W-G.9-355` **本單全文**施行一次：本單之量測器 `F14` 於開工態之紅、其判式自驗（`P0`）、其 `run` 所逕用之 `F13` 判式於 harness 路徑之已綠實跑，皆載於該單 `§一`。
````

SELF_SHA256: d26d5120682792893d36cc1a8f32662f4008b252660cf31c028376d3f1b53f48
