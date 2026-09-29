# `W-G.9-356`　輕量單：主線快轉（至 `1ef3bb5`·`W-G.9-353`〜`355` 末端塊之合併再試〔harness ＋ 畫面·含 `K-9-50`〕同批入主線）＋ 畫面路徑之接線檢查與 `main()` 之合成案（`W-G.9-355 §四-2` 之補寫）＋ 待落地清單之更新 ＋ 主 checkout 之同步

> **本單建議等級 ＝ `high`**（本單⛔ 令 CC 撰寫生產碼；受詞 ＝ 快轉、塊之原封入倉與實跑、主 checkout 之同步）。
> **發單** ＝ 發單側窗五十二·`2026-09-29`。**受單** ＝ CC 新窗（工項零′〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**）。
> **級** ＝ **輕**（本批⛔ 新增生產碼：新量測器 `1` 檔 ＋ `CLAUDE.md` 之純末端追加 ＋ 報告；工項零′ 之快轉使主線納入已於側支放行之生產碼 `commit` `3` 筆·其入主線之放行見 `§二`；本批⛔ 跑 `run_all` 及 `run` 類之量——快轉後主線之生產碼 `34` 檔 ≡ 側支之端，`W-G.9-355R` `V-5` 與發單側 `§一` 項 `5` 已跑〔KL 令：文件批⛔ 全套驗證儀式〕）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`（`W-G.9-355` 工項四）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F15`／`P10` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-356_輕量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項四之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F15`）與改動（`P10`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）之一字；既有量測器之一字；任何錨（`K_STAR_EXPECT`／`GSA_EXPECT`／`FLAGGED_EXPECT`／`TRACK_EXPECT`／`TIER_EXPECT`／`F.3 零遺漏` 之式）之改；`verify/baselines`；`verify/out/` 之二凍存名單；自誤簿、`GB` 簿、`VR` 簿、`K-6` 典、`docs/reports/W-G.9波_恆常附款登記表.md` 之一字；`CLAUDE.md` 除塊 `P10` 之純末端追加外之一字；任何側支之刪除或改寫（`verify/W-G.9-353-endmerge` 留於 `1ef3bb5`·⛔ 再推）；`run_all` 之執行。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止；**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零′**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；`git rev-parse origin/verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`；`git ls-remote --heads origin` 之列數 ＝ `31`；施工樹 `git checkout --detach origin/verify/W-G.9-353-endmerge` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 548 547` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態（側支之端 `1ef3bb5`·即快轉後之主線）之 `docs/` 全檔 **`913`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十二實跑 `python verify/probes/wg9268_gate6_occupancy.py 1ef3bb5 W-G.9-356 W-G.9-355 W-G.9-399`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-356`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-355` | `2`／`7`／`8` | `2`／`7`／`8` | `15` | `3` | `6`／`62` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-399` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`3` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `16`／`17` | 🟢 |

本單⛔ 鑄任何號（裁／`GB`／自誤／`VR`／`K-9` 皆 `0`）；四簿之相異數、`MAX` 與缺號集皆 ＝ 開工態（收工閘 `7`）。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `0b05925`，或側支 `verify/W-G.9-353-endmerge` ≠ `1ef3bb5`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `31` |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 工項零′ 前置之任一期不符 |
| `4` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成 |
| `5` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6` | 塊 `F15`／`P10` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `7` | 工項一之實跑任一 ≠ 期（尤：必過之態 ≠ `rc 0`、必破之態之末列 ≠ `§一` 項 `6` 之逐字、二態之全文與附錄丙之塊 `T1`／`T2` 不逐列相同） |
| `8` | `CLAUDE.md` 之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項四：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `11` | 工項零〜三之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `12` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者⛔ 屬之） |
| `13` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `4`。

---

## `§一`　態錨（發單側窗五十二自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`；主線為側支之祖（`git merge-base --is-ancestor` 真；`git rev-list --count 0b05925..1ef3bb5` ＝ `15`、反向 ＝ `0`）；其餘側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`31`**（`verify/` `26`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`·二態皆 `34`） | 主線 → 側支之端相異 **`3`** 檔：`app.py` `c99a3701608bb8aa2d218f3ae04e38757124fc24` → `e11232a6569bf33c7b2b7f15da989873a06ff28c`；`verify/selection_pipeline.py` `17fda1f94e786c413fc4691e247fe2ed26ecbdb0` → `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`；`verify/stepg_pipeline.py` `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373` → `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac` |
| `3` | `CLAUDE.md`（側支之端） | `295353` B（以換行結尾·CR `0`） |
| `4` | `W-G.9-355` 之復驗（發單側窗五十二·依交接文五十一 `§四-1`·全數自倉重跑） | **五 `commit` 逐筆對拍**：工項零之單 ＝ `8d9ec318…`（`93407` B·`SELF_SHA256` 經 `P-5` 自驗相符）；`F14`／`F4p`／`E5`／`P9`／`H1` 與單內塊逐位同；`F4p` 施於 `790060dc…` 得 `92f9dc4d…` ＝ `167e475` 之 `verify/probes/probe_WG9345_screen.py`；三檔嚴格前綴（自誤簿 `1075505→1077462`、`CLAUDE.md` `291243→295353`、恆常附款登記表 `59311→62376`）；工項二之 `app.py` ＝ `e11232a6…`（增 `214`／刪 `43`）。**量測**：`F14 selftest` ✅ `87`／🔴 `0`（`P0` 逐項擾動恰該項紅 `86／86`）；`F14 run` 全綠（✅ `16`／🔴 `0`·其數 ＝ 該單 `§一` 項 `6`）；`F4 parity` `3.5`／`0.0` 皆 `rc 0`（配地列 harness `35`／畫面 `34`、`36`／`35`·不符格 `0`·合併再試二鍵 ✅）；`F8 run` 二退縮改前（`167e475`）改後（`f173a4e`）`diff` 皆空；`run_all` 同一倉外路徑二態各 `236056` B·逐位同（`64` 項·PASS `28 → 28`·相異項 `0`·對帳 `22／36 → 22／36`）；收工閘 `1`〜`19` 皆符（閘 `7`：自誤 `533`／`548`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `47`／`50`，缺號集皆同開工態；閘 `8` `48／48／47`）。**逐段讀 `app.py` 之差異**：對 `R-1`〜`R-13`、`X-1`〜`X-8` 無偏差；自段三之畫面入口搬入 `k6b_screen_callbacks` 之三注入物（`a_prime`／`trial_winner`／`alloc_state`）與原碼之差恰為 `R-4` 之一列（程式實比）；CC 自解 `1` 件（`R-11`·僅訊息文字·零土地後果）**照准** |
| `5` | 快轉之淨效（主線 → 側支之端·本案） | `python verify/probes/probe_WG9349_k9296.py run <tree> 3.5`／`0.0`：主線 `0b05925` 與 `f173a4e`（其生產碼 `34` 檔 ＝ `1ef3bb5`）之出艙**逐位同**（二退縮）；`run_all` 同一倉外路徑 `0b05925` 對 `f173a4e`：二態各 `236056` B·`cmp` 逐位同（`64` 項·PASS `28 → 28`·相異項 `0`·末端夾具／golden 列 `21／21`·對帳 `22／36 → 22／36`；路徑 ＝ `/home/claude/wt_runall355v`，與 `§一` 項 `4` 之二態同一路徑；三份〔`0b05925`／`167e475`／`f173a4e`〕皆逐位同） ⇒ **本案之配地、街角、抵費地皆⛔ 變**（合併再試二退縮皆無標的）；他案之差 ＝ 末端塊各筆單獨皆未達時，由停機改為合併再試或強制抵費地（`K-9-49 ②`·`K-9-36 ③`·`K-9-50`） |
| `6` | 量測器 `F15`（附錄甲）之二態 | **必過**：`1ef3bb5` 之 `app.py`（`e11232a6…`）⇒ **`rc 0`**；本部 `W0`〜`W8`、`S1`、`S2` 皆 ✅；十四突變皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`。**必破**：`f55935c` 之 `app.py`（`dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`·`W-G.9-355` 開工態）⇒ **`rc 1`**；本部十一項皆 🔴、⛔ 施突變；末列逐字 `⇒ 紅 ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'S1', 'S2']；rc 1`。二態之全文 ＝ 附錄丙之塊 `T1`／`T2` |
| `7` | KL 主 checkout（倉外之物·發單側⛔ 實查） | 依 `W-G.9-352` 工項五 ＝ `wip/s1-endpart` 之 `0b05925`（`W-G.9-353`〜`355` 皆⛔ 動之）；其根或 `docs/orders/` 或有 `W-G.9-353`〜`356` 之來源檔（未追蹤）⇒ 依工項四之撞檔前置處置 |

---

## `§二`　KL 之語與射程

🔒 **所據**：`W-G.9-355 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：① 以程式字樣為錨之接線檢查（`R-1` 之三出口、`R-5` 之單一真相源、`R-6` 之鍵、`R-12` 之 `main()` 二處）及其突變之判別力；② `main()` 之顯示區塊與 `_f3L_invalidate_g_cache` 以假 st 實際執行之合成案（`自誤 517`）。」——本單之 `F15` 即其補寫；規格單流程之試行（KL `2026-09-28 11:43` 令）之首輪至此收束。
🔒 **`main()` 內之敘述**（`CLAUDE.md`「🔒 `main()` 內之敘述，`run_all` 不得單獨作為驗收依據」款·`自誤 517`）：`W-G.9-355` 於 `main()` 內之二處（成果區之顯示、`_f3L_invalidate_g_cache` 之二鍵）⛔ 為 `run_all`／`F14` 所執行 ⇒ `F15` 之 `S1`／`S2` 以假 st 實際執行之（體例同 `F10 wiring` 之 `W5`）。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：KL 已於發單側窗五十二（`2026-09-29 09:23`）就下列之問（【現況】至【要你判斷】逐字）答「放行，併於 356 辦理」——「【現況】W-G.9-353〜355（末端塊之合併再試：harness 與畫面二路徑）皆只在側支；主線與你本機介面仍是 352 之態。【要改成】於 356 之末併辦：主線快轉至側支之端（353〜356 同批入主線），並同步你的主 checkout。【對土地的影響】本案退縮 3.5 m／0 m 之配地面積、街角、抵費地皆不變（三批各自改前改後 run_all 逐位相同）；介面成果區多一區「末端塊之合併再試」，本案顯示「無標的」。他案才有差：末端塊各筆單獨皆未達時，由停機改為合併再試或強制抵費地。【要你判斷】是否放行 W-G.9-353〜356 同批入主線（併於 356 辦理）？」。CC 端之放行：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項零′（主線快轉）與工項四（主 checkout 之同步）之放行，CC 將其逐字載入報告；**無之 ⇒ 工項零′ 之前置畢後停於快轉前，於對話請示 KL**。所答之【要你判斷】逐字：「同意將側支（末端塊之合併再試：harness 與畫面二路徑·W-G.9-353〜355）併入主線，並請 CC 將您本機的程式資料夾同步至主線嗎？（是／否）」

🔒 **逐筆放行清單**（`恆常附款 y`·擬本單時自倉重導）：母體 ＝ `git rev-list 0b05925..1ef3bb5` ＝ **`15`** 筆；判準 ＝ 是否改動生產碼 `34` 檔之任一。動生產碼者 **`3`** 筆（其餘 `12` 筆皆單、報告、量測器、登記、`CLAUDE.md` 之末端追加）：

| `commit` | 訊息首段 | 所動之生產碼 | 側支之放行 | 本案之土地後果 |
|---|---|---|---|---|
| `c970ae60d092e8e803a3d156db2434c4f617c204` | `W-G.9-353` 工項二：末端塊之合併再試與強制抵費地（`K-9-49 ②`·`K-9-36 ③`）之 harness 路徑 | `app.py`、`verify/selection_pipeline.py`、`verify/stepg_pipeline.py` | `W-G.9-353 §二` | ⛔（`W-G.9-353R` `V-5`：改前改後 `run_all` 相異項 `0`） |
| `a44a3868342bf32e1c6f409ace79e61b82e83896` | `W-G.9-354` 工項二：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑 ＋ 後處理之承前 | `app.py` | `W-G.9-354 §二` | ⛔（發單側窗五十一復驗：改前改後 `run_all` 逐位同） |
| `f173a4e2a54d1ae036e14ecc35e88d0a9befdf31` | `W-G.9-355` 工項二：末端塊之合併再試（含 `K-9-50`）之畫面路徑 | `app.py` | `W-G.9-355 §二` | ⛔（`§一` 項 `4`）；三筆合計 ＝ `§一` 項 `5` |

🛑 **射程**：`(a)` 主線快轉至 `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`（工項零′·**以前置皆符且本節之放行成立為條件**）；`(b)` 工項零〜三（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項四於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、既有量測器、任何他錨；`(e)` ⛔ 建 `GB-194` 三停機款之處置、`K-9-48` 七項 `3`／`5`／`6`、調配之任何後步——另單。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存倉外之目錄 `<O>`）：
1. `git merge-base --is-ancestor 0b05925374f2de46c2493f5f56ef64667a2fed1d 1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f` ⇒ `rc 0`；`git rev-list --count 0b05925..1ef3bb5` ＝ `15`；`git rev-list --count 1ef3bb5..0b05925` ＝ `0`。
2. `git diff --name-only 0b05925 1ef3bb5 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `3` 列：`app.py`、`verify/selection_pipeline.py`、`verify/stepg_pipeline.py`（`§一` 項 `2`·🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 等子目錄之檔，發單側實測得 `7` 列）；`git rev-parse 1ef3bb5:app.py` ＝ `e11232a6569bf33c7b2b7f15da989873a06ff28c`。
3. `git rev-list 0b05925..1ef3bb5` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `3` 筆 ＝ `§二` 逐筆放行清單之三 `commit`（全 `40` 碼）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3`·⛔ 快轉。

**快轉**（前置皆符且 `§二` 之放行成立後·與前置為分開之呼叫）：

```
git push origin 1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4`）；⛔ 改目標值（逐字 `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-353-endmerge`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`；
② 遠端 heads ＝ **`31`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `1ef3bb5` 之相異 ＝ **`0`**；判別力［必非零］：vs `0b05925` 之相異 ＝ **`3`**（`§一` 項 `2` 之 `3` 檔）；
④ `git branch -r --contains f173a4e2a54d1ae036e14ecc35e88d0a9befdf31` 含 `origin/wip/s1-endpart`。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `1ef3bb5…` 方續工項零。

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-356_輕量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-356 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F15` 入倉與實跑（主線·零生產碼）

1. 塊 `F15`（附錄甲）依圍欄之逐列索引抽出、對拍 `§五-1` 項 `2` 後，以二進位寫為 `verify/probes/probe_WG9356_screenmerge_wiring.py`（**新檔**）；`git check-ignore` 之⛔ 命中。
2. **必過之態**（施工樹·其 `app.py` ＝ `e11232a6…`）：`python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo> > <O>\f15_pass.log` ⇒ **`rc 0`**；本部 `W0`〜`W8`、`S1`、`S2` 皆 ✅；十四突變 `M1`〜`M14` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`；全文與附錄丙之塊 `T1` 逐列相同（比對前去 CR 及列尾空白）。
3. **必破之態**：`git worktree add --detach <P> f55935cb95b5e6c058231ee89d5dd19e3a291456`（`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑）；於施工樹 `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <P> > <O>\f15_break.log` ⇒ **`rc 1`**，末列逐字 ＝ `§一` 項 `6` 之必破之末列；全文與附錄丙之塊 `T2` 逐列相同（同上）；跑畢 `git worktree remove --force <P>`。

任一 ≠ 期 ⇒ 停機款 `7`（⛔ 改器）。`commit` 訊息逐字 `W-G.9-356 工項一：量測器 F15（末端塊合併再試之畫面路徑之接線與 main() 之合成案）入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　塊 `P10` 之末端追加（主線·零生產碼·一 `commit`）

塊 `P10`（附錄乙）依圍欄之逐列索引抽出、對拍 `§五-1` 項 `3` 後，以二進位附於 `CLAUDE.md` 之末（刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-356 工項二：待落地清單之更新（W-G.9-353〜355 入主線 ＋ 畫面路徑之接線檢查）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-356R_入主線與畫面路徑之接線檢查_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ 工項一之二態之全文（`f15_pass.log`／`f15_break.log`）；⑤ 二塊之實得（bytes／`sha256`）與 `CLAUDE.md` 之改前改後 bytes；⑥ `§二` 之放行（KL 之逐字或請示之經過）；⑦ CC 之自捕與自解；⑧ 各段耗時（規格單流程之試行評估之用）。收工閘之實測值與工項四之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-356 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項三 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `e11232a6569bf33c7b2b7f15da989873a06ff28c`；`git -C <主 checkout> hash-object verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；`git -C <主 checkout> hash-object verify/selection_pipeline.py` ＝ `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`。

任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之刪除欄 | 逐檔 **`0`** |
| `2` | 生產碼 `34` 檔 | 對 `1ef3bb5` 相異 **`0`**；判別力［必非零］：對 `0b05925` 相異 **`3`**；`verify/` 之一切檔對 `1ef3bb5` 相異恰 **`1`**（新檔 `verify/probes/probe_WG9356_screenmerge_wiring.py`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`4` 檔：本單、`F15`、`CLAUDE.md`、報告） |
| `4` | `CLAUDE.md` 之 bytes | `295353` → **`299948`**；改前為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`31`**；主線 ＝ 工項三之 `commit`；`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 548 547 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 548 547` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `533`／`MAX` `548`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `47`／`50`／`[44, 47]`（皆 ＝ 開工態） |
| `8` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9355_screenmerge.py selftest <repo 絕對路徑>`；`python verify/probes/probe_WG9345_screen.py wiring <repo 絕對路徑>`；`python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>`；`python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | 皆 **`rc 0`**；`F14` 末列逐字 `⇒ 紅 []；rc 0`；`F4` 末列逐字 `⇒ rc 0（不符 0·器紅 0）`；`wfns_ast` **`48`／`48`／`47`**；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」 |

🔒 **必過之實例**：發單側已於拋棄式 clone 模擬工項零′〜三（快轉 ＋ 本單 ＋ 塊 `F15` ＋ 塊 `P10` ＋ 報告之替身）並實跑閘 `1`〜`9` ⇒ 見 `§五-1` 項 `6`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F15` | `30405` B·`sha256` `d56a954a30900009c9146b665958ec05a2c8b690eba02886a786e0c5acfef45a`·`605` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9356_screenmerge_wiring.py`（blob `c489e887300d29b90c14791024bc215709390749`） |
| `3` | 塊 `P10` | `4595` B·`sha256` `1302e3b8a18d2069ddc36b5fe5ae0fb11e107c85bcd0acf2ee4d0d43363ad4cb`·`20` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`295353` B）之末後，期末 ＝ `299948` B |
| `4` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十二於模擬態（`1ef3bb5` ＋ 本單之初稿）實跑：🔴 機械 `0` 項／🟡 提示 `5` 項——`P-4` `:63`（`§一` 態錨之表頭·所觸之箭頭係各項之改前改後〔項 `2`／`5` ＝ 主線 `0b05925` 至側支之端；項 `4` ＝ `W-G.9-355` 之改前至改後〕，同格自載 ⇒ **具名豁免**）、`P-4` `:157`（`§四` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `1ef3bb5` 至工項三之端，表內自載 ⇒ **具名豁免**）、`P-4` `:330`（附錄甲塊 `F15` 內之 Python 註解列 `# ── 接線 ──` 為器所誤認之標題·所觸之箭頭係器之出艙字串 ⇒ **具名豁免**）、`P-4` `:835`（附錄丙塊 `T1` 之圍欄·所觸之箭頭係器之出艙原文 ⇒ **具名豁免**）、`P-6` `:63`（`§一` 態錨之表頭·其所轄之數皆發單側窗五十二自倉實跑、各格具名其命令或出處 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `19744`–`27416`）⇒ `rc 0` |
| `5` | 附錄丙之塊 `T1`／`T2`（工項一之二態之出艙·發單側實跑） | `T1` `2576` B·`sha256` `46dbc8e7946eaaa5790f199966834afb8ef8aa803f4b95af4a6188ac8986eb8d`·`28` 列；`T2` `1279` B·`sha256` `9e97cae7ec7c7cfe4f2b4506415529f96efd47532e1ee27266a43c96e3b98947`·`14` 列（圍欄內全文·末附換行；比對時去 CR 及列尾空白） |
| `6` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 clone（`1ef3bb5`〔即快轉後之主線〕＋ 本單 ＋ 塊 `F15` ＋ 塊 `P10` ＋ 報告之替身·四 `commit`·⛔ `push`）：工項零′ 前置 `1`〜`3` 皆符（`15`／`0`；`:(glob)` 形恰 `3` 列；逐筆判命中者恰 `c970ae6`〔`3` 列〕、`a44a386`〔`1`〕、`f173a4e`〔`1`〕）；塊之抽取與 `§五-1` 項 `2`／`3` 逐位同；工項一二態 `rc 0`／`rc 1`、全文與塊 `T1`／`T2` 逐列同；閘 `1` 四檔之刪除欄皆 `0`；閘 `2` 對 `1ef3bb5` 相異 `0`、對 `0b05925` `3`、`verify/` 相異恰 `1`；閘 `3` CR `0`（`V6.dxf` `12308`）；閘 `4` `295353 → 299948`（嚴格前綴）；閘 `6`〜`9` 皆 `rc 0`（閘 `7` 四簿 ＝ 開工態；`F15`／`F14` 末列 `⇒ 紅 []；rc 0`；`F4` 末列 `⇒ rc 0（不符 0·器紅 0）`；`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」）；新檔之 `git check-ignore` 皆無命中 |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````markdown `` 或 `` ````text ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零′ ⇒ 依 `§二` 之放行、前置皆符後推主線；工項零〜三 ⇒ 逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）。
3. 收工後，主 checkout 之根之來源檔（本單，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F15`（新檔 `verify/probes/probe_WG9356_screenmerge_wiring.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-356 量測器（發單側窗五十二擬·檔 F15·⛔ 由受單側改一字）：末端塊之合併再試之畫面路徑之接線與 `main()` 之合成案。

緣由：`W-G.9-355`（規格單流程之首張）之 `§四-2`——以程式字樣為錨之接線檢查須待碼成方能寫 ⇒ 發單側讀 CC 之碼
（`f173a4e`）後補寫。受詞之行為（三出口之編排、四注入物、顯示函式）已由 F14（`probe_WG9355_screenmerge.py`）之
`selftest`／`run` 量之；本器量**程式字樣**（防日後之漂移）與 `main()` 內之二處（`run_all`／F14 皆⛔ 執行之·`自誤 517`）。

受詞（`app.py`·工作樹）：
  f3_screen_k6b_stage3／f3_screen_end_block_merge／k6b_screen_callbacks／end_block_merge_rows（模組層）、
  K6B_SCREEN_TRIAL_KEYS／SS_END_BLOCK_MODE／SS_END_BLOCK_MERGE（模組層常數）、main() 內之 _f3L_invalidate_g_cache 與
  成果區「末端塊之合併再試」之區塊。

子命令（一律 python verify/probes/probe_WG9356_screenmerge_wiring.py <子命令> <repo>）：
  wiring <repo>
    W1 `R-1` 三出口：段三之畫面入口（巢狀 def 之外）之 return 恰 3，各 ＝ 呼叫同一巢狀函式，該函式呼
       f3_screen_end_block_merge(st, …) 恰 1；各 return 之前、同一敘述列中有真 st 之 f3_screen_corner_pk_run(st, …)，
       且 return 所傳之宗地 ＝ 該次街角選位所用之宗地（`**pk_kwargs` ⇒ temp0／build0；`**dict(…, temp_parcels=X, build_parcels=Y)` ⇒ X／Y）。
    W2 `R-1` 單一真相源：end_block_merge_run 於 app.py 中唯以名呼叫（⛔ 別名、⛔ 作引數傳遞、⛔ 預綁）、呼叫恰 1、
       且在 f3_screen_end_block_merge 內；f3_screen_end_block_merge 之呼叫恰 1、在段三之畫面入口內。
    W3 `R-5` 單一真相源：k6b_screen_callbacks 內有巢狀 a_prime／trial_winner／alloc_state／alloc_eval 且回此四鍵；app.py 他處
       ⛔ 有同名之巢狀 def；段三之畫面入口與合併再試之入口各呼 k6b_screen_callbacks 恰 1；k6b_stage3_run 之第 8〜10 引數
       ＝ 其回傳之 a_prime／trial_winner／alloc_state，end_block_merge_run 之第 8〜10 引數 ＝ a_prime／alloc_eval／alloc_state。
    W4 `R-3`／`R-4` 試算：alloc_state 與 alloc_eval 內，`<session>[SS_END_BLOCK_MODE] = 'trial'` 先於同一敘述列中之
       f3_screen_stepg_run(<代理 st>, …)（代理 st ＝ 同函式內 `_K6BTrialSt(st)` 之所賦）。
    W5 `R-6` 隔離：SS_END_BLOCK_MODE 之值 ∈ K6B_SCREEN_TRIAL_KEYS（literal_eval）；合併再試之入口於呼叫 end_block_merge_run
       之 try 之前以 K6B_SCREEN_TRIAL_KEYS 存、其 finally 以 K6B_SCREEN_TRIAL_KEYS 復並復 K917_DROPPED。
    W6 `R-7` 紀錄：合併再試之入口於該 try 之後寫 `[SS_END_BLOCK_MERGE] ＝ rec`、`['f3_end_block_merge_log'] ＝ log`（rec／log ＝
       end_block_merge_run 之第 4／3 回傳）；段三之畫面入口於其首個 if 之前去此二鍵。
    W7 `R-12` 失效：main() 內 _f3L_invalidate_g_cache 去 SS_END_BLOCK_MERGE 與 'f3_end_block_merge_log'。
    W8 `R-12` 顯示之接線：main() 內同一敘述列中，`X = st.session_state.get(SS_END_BLOCK_MERGE)` 緊接 `if X is not None:`，其本體呼
       end_block_merge_rows(X, st.session_state.get('f3_end_block_merge_log'))；位置 ＝ 末端塊之評選（_eb352）之 if 之後、_adj351_bf
       之賦值之前。
    S1 `自誤 517`：W8 之二句（賦值 ＋ if）自 main() 抽出，以假 st 實際執行三情形（有標的而有逐列／無標的而無逐列／無紀錄），
       期值為本器另寫之字面（⛔ 呼叫受測函式求期）。
    S2 `自誤 517`：main() 內之 _f3L_invalidate_g_cache 抽出以假 st 實際執行：所列之鍵皆去、他鍵留、f3_g_needs_rerun ＝ True
       （該函式以 `except Exception: pass` 包裹 ⇒ 以結果判、⛔ 以「未拋」判）。
    本部全綠時另施 14 種原始碼突變，每一突變須使其所指之項轉紅（器紅 ⇒ rc 1）。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import ast, contextlib, copy, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FN_S3, FN_EBM, FN_CB, FN_ROWS = ("f3_screen_k6b_stage3", "f3_screen_end_block_merge", "k6b_screen_callbacks",
                                 "end_block_merge_rows")
CB4 = ("a_prime", "trial_winner", "alloc_state", "alloc_eval")
LOGK = "f3_end_block_merge_log"


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


# ── AST 之小工具 ──
def _top(tree):
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


def _consts(tree):
    return {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign) and len(n.targets) == 1
            and isinstance(n.targets[0], ast.Name)}


def _walk_own(fn):
    """fn 之節點，⛔ 入巢狀之 def／lambda。"""
    todo = [s for s in fn.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))]
    while todo:
        n = todo.pop()
        yield n
        for c in ast.iter_child_nodes(n):
            if not isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                todo.append(c)


def _nested(fn):
    return {n.name: n for n in ast.walk(fn) if isinstance(n, ast.FunctionDef) and n is not fn}


def _is_call(n, name):
    return isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name


def _calls(node, name, own=False):
    it = _walk_own(node) if own else ast.walk(node)
    return [n for n in it if _is_call(n, name)]


def _stmt_lists(node):
    for n in ast.walk(node):
        for fld in ("body", "orelse", "finalbody"):
            b = getattr(n, fld, None)
            if isinstance(b, list) and b and isinstance(b[0], ast.stmt):
                yield b
        for h in getattr(n, "handlers", []) or []:
            yield h.body


def _uparse(n):
    try:
        return ast.unparse(n)
    except Exception:  # noqa: BLE001
        return "<?>"


def _is_sub(n, key_name=None, key_str=None):
    """n ＝ `<x>[Name key_name]` 或 `<x>['key_str']`。"""
    if not isinstance(n, ast.Subscript):
        return False
    s = n.slice
    if key_name is not None:
        return isinstance(s, ast.Name) and s.id == key_name
    return isinstance(s, ast.Constant) and s.value == key_str


def _is_pop(n, key_name=None, key_str=None):
    if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "pop" and n.args):
        return False
    a = n.args[0]
    if key_name is not None:
        return isinstance(a, ast.Name) and a.id == key_name
    return isinstance(a, ast.Constant) and a.value == key_str


def _main_of(tree):
    return _top(tree).get("main")


# ── 接線 ──
def _w1(top):
    s3 = top.get(FN_S3)
    if s3 is None:
        return False, "段三之畫面入口缺"
    rets = [n for n in _walk_own(s3) if isinstance(n, ast.Return)]
    nest = _nested(s3)
    tgt = {n.value.func.id for n in rets if isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name)}
    if len(rets) != 3 or len(tgt) != 1 or next(iter(tgt)) not in nest:
        return False, f"return {len(rets)}（期 3）；所呼 {sorted(tgt)}（期 恰 1 且為巢狀函式）"
    em = nest[next(iter(tgt))]
    ebm = _calls(em, FN_EBM)
    if len(ebm) != 1 or not ebm[0].args or not (isinstance(ebm[0].args[0], ast.Name) and ebm[0].args[0].id == "st"):
        return False, f"{em.name} 內 {FN_EBM}(st, …) 之呼叫 {len(ebm)}（期 1·首參 st）"
    # temp0／build0 之源
    src0 = [n for n in s3.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple)
            and [_uparse(e) for e in n.targets[0].elts] == ["temp0", "build0"]
            and _uparse(n.value) == "(pk_kwargs['temp_parcels'], pk_kwargs['build_parcels'])"]
    if len(src0) != 1:
        return False, "temp0／build0 ＝ pk_kwargs 之 temp_parcels／build_parcels 之賦值缺"
    bad = []
    for lst in _stmt_lists(s3):
        for i, st_ in enumerate(lst):
            if not (isinstance(st_, ast.Return) and st_ in rets):
                continue
            pk = None
            for prev in reversed(lst[:i]):
                if isinstance(prev, ast.Return):
                    break
                if isinstance(prev, ast.Expr) and _is_call(prev.value, "f3_screen_corner_pk_run"):
                    pk = prev.value
                    break
            if pk is None or not (pk.args and isinstance(pk.args[0], ast.Name) and pk.args[0].id == "st"):
                bad.append(f"L{st_.lineno}：前無真 st 之街角選位")
                continue
            kw = pk.keywords
            if len(kw) == 1 and kw[0].arg is None and _uparse(kw[0].value) == "pk_kwargs":
                exp = ["temp0", "build0"]
            elif len(kw) == 1 and kw[0].arg is None and _is_call(kw[0].value, "dict"):
                d = {k.arg: _uparse(k.value) for k in kw[0].value.keywords}
                exp = [d.get("temp_parcels"), d.get("build_parcels")]
            else:
                bad.append(f"L{st_.lineno}：街角選位之引數形未識")
                continue
            got = [_uparse(a) for a in st_.value.args[:2]]
            if got != exp:
                bad.append(f"L{st_.lineno}：合併再試之宗地 {got} ≠ 街角選位所用 {exp}")
    return (not bad), f"{bad}" if bad else f"三出口皆經 {em.name} → {FN_EBM}(st, …)"


def _w2(tree, top):
    loads = [n for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "end_block_merge_run"]
    calls = [n for n in ast.walk(tree) if _is_call(n, "end_block_merge_run")]
    as_func = {id(c.func) for c in calls}
    stray = [n.lineno for n in loads if id(n) not in as_func]
    ebm = top.get(FN_EBM)
    in_ebm = len(_calls(ebm, "end_block_merge_run")) if ebm else 0
    c_ebm = [n for n in ast.walk(tree) if _is_call(n, FN_EBM)]
    s3 = top.get(FN_S3)
    in_s3 = len(_calls(s3, FN_EBM)) if s3 else 0
    ok = not stray and len(calls) == 1 and in_ebm == 1 and len(c_ebm) == 1 and in_s3 == 1
    return ok, (f"end_block_merge_run：呼叫 {len(calls)}（期 1）·在合併再試之入口 {in_ebm}·非呼叫之引用列 {stray}；"
                f"{FN_EBM} 之呼叫 {len(c_ebm)}（期 1）·在段三之畫面入口 {in_s3}")


def _cb_var(fn):
    for n in ast.walk(fn):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
                and _is_call(n.value, FN_CB):
            return n.targets[0].id
    return None


def _slot_keys(call, var, idx):
    out = []
    for i in idx:
        a = call.args[i] if len(call.args) > i else None
        if isinstance(a, ast.Subscript) and isinstance(a.value, ast.Name) and a.value.id == var \
                and isinstance(a.slice, ast.Constant):
            out.append(a.slice.value)
        else:
            out.append(_uparse(a) if a is not None else None)
    return out


def _w3(tree, top):
    cb = top.get(FN_CB)
    if cb is None:
        return False, f"{FN_CB} 缺"
    nest = _nested(cb)
    rets = [n for n in _walk_own(cb) if isinstance(n, ast.Return)]
    ret_ok = (len(rets) == 1 and isinstance(rets[0].value, ast.Dict)
              and {k.value: _uparse(v) for k, v in zip(rets[0].value.keys, rets[0].value.values)
                   if isinstance(k, ast.Constant)} == {k: k for k in CB4})
    dup = sorted({f"{f.name}.{n.name}" for f in top.values() if f is not cb
                  for n in ast.walk(f) if isinstance(n, ast.FunctionDef) and n is not f and n.name in CB4})
    notes = []
    s3, ebm = top.get(FN_S3), top.get(FN_EBM)
    ok_s3 = ok_ebm = False
    if s3 is not None:
        v = _cb_var(s3)
        k3 = _calls(s3, "k6b_stage3_run")
        ok_s3 = (len(_calls(s3, FN_CB)) == 1 and v is not None and len(k3) == 1
                 and _slot_keys(k3[0], v, (7, 8, 9)) == ["a_prime", "trial_winner", "alloc_state"])
        notes.append(f"段三：{_slot_keys(k3[0], v, (7, 8, 9)) if k3 and v else '—'}")
    if ebm is not None:
        v = _cb_var(ebm)
        km = _calls(ebm, "end_block_merge_run")
        ok_ebm = (len(_calls(ebm, FN_CB)) == 1 and v is not None and len(km) == 1
                  and _slot_keys(km[0], v, (7, 8, 9)) == ["a_prime", "alloc_eval", "alloc_state"])
        notes.append(f"合併再試：{_slot_keys(km[0], v, (7, 8, 9)) if km and v else '—'}")
    ok = set(CB4) <= set(nest) and ret_ok and not dup and ok_s3 and ok_ebm
    return ok, f"巢狀 {sorted(set(CB4) & set(nest))}；回四鍵 {ret_ok}；他處同名 {dup}；" + "；".join(notes)


def _w4(top):
    cb = top.get(FN_CB)
    if cb is None:
        return False, f"{FN_CB} 缺"
    nest = _nested(cb)
    res = {}
    for nm in ("alloc_state", "alloc_eval"):
        f = nest.get(nm)
        if f is None:
            res[nm] = "缺"
            continue
        px = {n.targets[0].id for n in ast.walk(f) if isinstance(n, ast.Assign) and len(n.targets) == 1
              and isinstance(n.targets[0], ast.Name) and _is_call(n.value, "_K6BTrialSt")
              and [_uparse(a) for a in n.value.args] == ["st"]}
        hit = False
        for lst in _stmt_lists(f):
            for i, s in enumerate(lst):
                if isinstance(s, ast.Expr) and _is_call(s.value, "f3_screen_stepg_run") and s.value.args \
                        and isinstance(s.value.args[0], ast.Name) and s.value.args[0].id in px:
                    hit = hit or any(isinstance(p, ast.Assign) and len(p.targets) == 1
                                     and _is_sub(p.targets[0], key_name="SS_END_BLOCK_MODE")
                                     and isinstance(p.value, ast.Constant) and p.value.value == "trial"
                                     for p in lst[:i])
        res[nm] = hit
    return all(v is True for v in res.values()), f"{res}"


def _w5(tree, top):
    c = _consts(tree)
    try:
        mode = ast.literal_eval(c["SS_END_BLOCK_MODE"].value)
        keys = ast.literal_eval(c["K6B_SCREEN_TRIAL_KEYS"].value)
    except Exception as e:  # noqa: BLE001
        return False, f"常數無從取：{type(e).__name__}"
    ebm = top.get(FN_EBM)
    if ebm is None:
        return False, f"{FN_EBM} 缺"
    tries = [(i, s) for i, s in enumerate(ebm.body) if isinstance(s, ast.Try) and _calls(s, "end_block_merge_run")]
    if len(tries) != 1:
        return False, f"含 end_block_merge_run 之 try {len(tries)}（期 1）"
    i, t = tries[0]
    saved = any(isinstance(n, ast.DictComp) and any(isinstance(g.iter, ast.Name) and g.iter.id == "K6B_SCREEN_TRIAL_KEYS"
                                                    for g in n.generators)
                for s in ebm.body[:i] for n in ast.walk(s))
    fin = t.finalbody
    rest = any(isinstance(s, ast.For) and isinstance(s.iter, ast.Name) and s.iter.id == "K6B_SCREEN_TRIAL_KEYS"
               for s in fin)
    k917 = {_uparse(s.value.func) for s in fin if isinstance(s, ast.Expr) and isinstance(s.value, ast.Call)}
    ok = mode in keys and saved and rest and {"K917_DROPPED.clear", "K917_DROPPED.update"} <= k917
    return ok, f"SS_END_BLOCK_MODE＝{mode!r} ∈ 鍵 {mode in keys}；try 前存 {saved}；finally 復 {rest}；K917 {sorted(k917)}"


def _w6(top):
    ebm, s3 = top.get(FN_EBM), top.get(FN_S3)
    if ebm is None or s3 is None:
        return False, "受詞缺"
    ti = [i for i, s in enumerate(ebm.body) if isinstance(s, ast.Try) and _calls(s, "end_block_merge_run")]
    if len(ti) != 1:
        return False, "try 無從定"
    t = ebm.body[ti[0]]
    asg = [n for n in ast.walk(t) if isinstance(n, ast.Assign) and _calls(n, "end_block_merge_run")]
    tgt = [_uparse(e) for e in asg[0].targets[0].elts] if asg and isinstance(asg[0].targets[0], ast.Tuple) else []
    if len(tgt) != 4:
        return False, f"end_block_merge_run 之回傳之受值 {tgt}"
    after = ebm.body[ti[0] + 1:]
    w_rec = any(isinstance(s, ast.Assign) and _is_sub(s.targets[0], key_name="SS_END_BLOCK_MERGE")
                and _uparse(s.value) == tgt[3] for s in after)
    w_log = any(isinstance(s, ast.Assign) and _is_sub(s.targets[0], key_str=LOGK)
                and _uparse(s.value) == tgt[2] for s in after)
    before = ebm.body[:ti[0]]
    in_try = any(isinstance(n, ast.Assign) and (_is_sub(n.targets[0], key_name="SS_END_BLOCK_MERGE")
                                                or _is_sub(n.targets[0], key_str=LOGK))
                 for s in before + [t] for n in ast.walk(s))
    fi = next((i for i, s in enumerate(s3.body) if isinstance(s, ast.If)), len(s3.body))
    head = s3.body[:fi]
    pop_rec = any(_is_pop(n, key_name="SS_END_BLOCK_MERGE") for s in head for n in ast.walk(s))
    pop_log = any(_is_pop(n, key_str=LOGK) for s in head for n in ast.walk(s))
    ok = w_rec and w_log and not in_try and pop_rec and pop_log
    return ok, (f"try 後寫 rec {w_rec}／log {w_log}；try 內或其前寫 {in_try}；"
                f"段三之畫面入口之首去 rec {pop_rec}／log {pop_log}")


def _inv_of(main):
    inv = [n for n in ast.walk(main) if isinstance(n, ast.FunctionDef) and n.name == "_f3L_invalidate_g_cache"]
    return inv[0] if len(inv) == 1 else None


def _w7(main):
    if main is None:
        return False, "main 缺"
    inv = _inv_of(main)
    if inv is None:
        return False, "_f3L_invalidate_g_cache 缺或非唯一"
    a = any(_is_pop(n, key_name="SS_END_BLOCK_MERGE") for n in ast.walk(inv))
    b = any(_is_pop(n, key_str=LOGK) for n in ast.walk(inv))
    return a and b, f"去 SS_END_BLOCK_MERGE {a}；去 {LOGK} {b}"


def _get_call(n, key_name=None, key_str=None):
    """n ＝ st.session_state.get(<key>)。"""
    if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "get"
            and _uparse(n.func.value) == "st.session_state" and len(n.args) == 1 and not n.keywords):
        return False
    a = n.args[0]
    if key_name is not None:
        return isinstance(a, ast.Name) and a.id == key_name
    return isinstance(a, ast.Constant) and a.value == key_str


def _find_disp(main):
    """回 (敘述列, 賦值之 idx) 或 None。"""
    for lst in _stmt_lists(main):
        for i, s in enumerate(lst):
            if isinstance(s, ast.Assign) and len(s.targets) == 1 and isinstance(s.targets[0], ast.Name) \
                    and _get_call(s.value, key_name="SS_END_BLOCK_MERGE") and i + 1 < len(lst) \
                    and isinstance(lst[i + 1], ast.If):
                return lst, i
    return None


def _w8(main):
    if main is None:
        return False, "main 缺"
    f = _find_disp(main)
    if f is None:
        return False, "`X = st.session_state.get(SS_END_BLOCK_MERGE)` ＋ if 之二句缺"
    lst, i = f
    x = lst[i].targets[0].id
    t = lst[i + 1].test
    t_ok = (isinstance(t, ast.Compare) and isinstance(t.left, ast.Name) and t.left.id == x
            and len(t.ops) == 1 and isinstance(t.ops[0], ast.IsNot)
            and isinstance(t.comparators[0], ast.Constant) and t.comparators[0].value is None)
    rc = [n for n in ast.walk(lst[i + 1]) if _is_call(n, FN_ROWS)]
    r_ok = (len(rc) == 1 and len(rc[0].args) == 2 and isinstance(rc[0].args[0], ast.Name) and rc[0].args[0].id == x
            and _get_call(rc[0].args[1], key_str=LOGK))
    eb = [j for j, s in enumerate(lst) if isinstance(s, ast.Assign) and _uparse(s.targets[0]) == "_eb352"]
    ad = [j for j, s in enumerate(lst) if isinstance(s, ast.Assign) and _uparse(s.targets[0]) == "_adj351_bf"]
    p_ok = (len(eb) == 1 and len(ad) == 1 and eb[0] + 1 < i and isinstance(lst[eb[0] + 1], ast.If)
            and i + 1 < ad[0])
    return t_ok and r_ok and p_ok, f"if 之式 {t_ok}；{FN_ROWS}(X, …get('{LOGK}')) {r_ok}；位置 {p_ok}"


# ── 合成案（自誤 517）──
class _NullCM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def _f(*a, **k):
            self.calls.append((name, a, k))
            return _NullCM()
        return _f


REC = {"退縮": 3.5, "標的": [["QA", "left"], ["QB", "right"]], "皆未達": {"QA": ["left"]},
       "競合": [{"形": "一", "列": [["QA", "左", "K(4)", 66.49], ["QB", "右", "K(3)", 237.57]]}]}
LOG = [{"序": 1, "街廓": "QB", "端": "右", "候選": "K(3)", "結果": "成", "檢核": None},
       {"序": "後處理", "街廓": "QB", "端": "右", "候選": "K(4)", "結果": "成", "檢核": "通過"}]
ROWS_EXP = [{"序": "1", "街廓": "QB", "端": "右", "候選": "K(3)", "結果": "成", "檢核": "—"},
            {"序": "後處理", "街廓": "QB", "端": "右", "候選": "K(4)", "結果": "成", "檢核": "通過"}]
NEED = ["QA", "QB", "K(4)", "K(3)", "66.49", "237.57", "強制抵費地", "3.5"]


def _ns_for(src, tree):
    c = _consts(tree)
    top = _top(tree)
    parts = [ast.get_source_segment(src, c[k]) for k in ("SS_END_BLOCK_MERGE", "K6B_SCREEN_STAGE3_KEYS") if k in c]
    if FN_ROWS in top:
        parts.append(ast.get_source_segment(src, top[FN_ROWS]))
    ns = {}
    exec(compile("\n\n".join(parts), "<f15_extract>", "exec"), ns)
    return ns


def _s1(src, tree):
    main = _main_of(tree)
    f = _find_disp(main) if main is not None else None
    if f is None:
        return False, "抽不到顯示區塊"
    lst, i = f
    try:
        import pandas as pd
        base = _ns_for(src, tree)
        code = compile(ast.Module(body=lst[i:i + 2], type_ignores=[]), "<main_ebm_block>", "exec")
        out = {}
        for tag, ss in (("有", {base["SS_END_BLOCK_MERGE"]: copy.deepcopy(REC), LOGK: copy.deepcopy(LOG)}),
                        ("空", {base["SS_END_BLOCK_MERGE"]: {"退縮": 0.0, "標的": [], "皆未達": {}}, LOGK: []}),
                        ("無", {"其他": 1})):
            fst = _FakeSt(ss)
            g = dict(base, st=fst, _pd=pd)
            exec(code, g)
            out[tag] = fst.calls
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    have = out["有"]
    exps = [c for c in have if c[0] == "expander"]
    caps = "\n".join(str(c[1][0]) for c in have if c[0] == "caption")
    dfs = [c[1][0] for c in have if c[0] == "dataframe"]
    empty = out["空"]
    checks = {
        "有·expander 1（展開）": len(exps) == 1 and "末端塊之合併再試" in str(exps[0][1][0]) and exps[0][2].get("expanded") is True,
        "有·行載標的／競合／皆未達／退縮": not [s for s in NEED if s not in caps],
        "有·逐列表 1 ＝ 紀錄之列（字串·None ⇒ —）": len(dfs) == 1 and dfs[0].to_dict("records") == ROWS_EXP,
        "有·無 st.error": not [c for c in have if c[0] == "error"],
        "空·expander 1（收合）·含無標的·無逐列表": ([c[2].get("expanded") for c in empty if c[0] == "expander"] == [False]
                                   and any("無標的" in str(c[1][0]) for c in empty if c[0] == "caption")
                                   and not [c for c in empty if c[0] == "dataframe"]),
        "無·⛔ 顯示": out["無"] == [],
    }
    bad = [k for k, v in checks.items() if not v]
    return (not bad), f"不符 {bad}" if bad else "三情形皆符"


def _s2(src, tree):
    main = _main_of(tree)
    inv = _inv_of(main) if main is not None else None
    if inv is None:
        return False, "抽不到 _f3L_invalidate_g_cache"
    try:
        base = _ns_for(src, tree)
        mk, s3k = base["SS_END_BLOCK_MERGE"], tuple(base["K6B_SCREEN_STAGE3_KEYS"])
        gone = ["f3_G_values", "f3_G_trace", "f3_corner_winners", "f3L_corner_winners", *s3k,
                "f3_k6b_stage3_error", mk, LOGK]
        ss = {k: "舊" for k in gone}
        ss["留"] = "留"
        fst = _FakeSt(ss)
        g = dict(base, st=fst)
        exec(compile(ast.Module(body=[inv], type_ignores=[]), "<main_inv>", "exec"), g)
        g["_f3L_invalidate_g_cache"]()
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    left = [k for k in gone if k in ss]
    ok = not left and ss.get("留") == "留" and ss.get("f3_g_needs_rerun") is True
    return ok, f"未去 {left}；他鍵留 {ss.get('留') == '留'}；f3_g_needs_rerun {ss.get('f3_g_needs_rerun')!r}"


def _checks(src):
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [("W0 可剖析", False, f"{e}")]
    top = _top(tree)
    main = _main_of(tree)
    miss = [n for n in (FN_S3, FN_EBM, FN_CB, FN_ROWS) if n not in top]
    res = [("W0 受詞在模組層", not miss, f"缺 {miss}")]
    for name, fn in (("W1 R-1 三出口", lambda: _w1(top)), ("W2 R-1 單一真相源", lambda: _w2(tree, top)),
                     ("W3 R-5 四注入物之單一真相源", lambda: _w3(tree, top)), ("W4 R-3／R-4 試算 'trial'", lambda: _w4(top)),
                     ("W5 R-6 隔離", lambda: _w5(tree, top)), ("W6 R-7 紀錄", lambda: _w6(top)),
                     ("W7 R-12 失效之二鍵", lambda: _w7(main)), ("W8 R-12 顯示之接線", lambda: _w8(main)),
                     ("S1 自誤517 顯示區塊之合成案", lambda: _s1(src, tree)),
                     ("S2 自誤517 失效函式之合成案", lambda: _s2(src, tree))):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ok, note = fn()
        except Exception as e:  # noqa: BLE001
            ok, note = False, f"器拋 {type(e).__name__}: {e}"
        res.append((name, ok, note))
    return res


# ── 突變（每一須使其所指之項轉紅）──
def _mut_list():
    T = "K6B_SCREEN_TRIAL_KEYS"
    return [
        ("M1 出口①⛔ 辦合併再試", "W1",
         [("        return _end_merge(temp0, build0, [], _order, False)",
           "        return {'temp': temp0, 'build': build0, 'log': [], 'order': _order, 'ran': False}")]),
        ("M2 出口③以段三前之宗地辦合併再試", "W1",
         [("    return _end_merge(temp2, build2, log, order, True)",
           "    return _end_merge(temp0, build0, log, order, True)")]),
        ("M3 以別名呼叫單一真相源", "W2",
         [("temp3, build3, log, rec = end_block_merge_run(", "temp3, build3, log, rec = globals()['end_block_merge_run']("),
          ]),
        ("M4 合併再試另寫 alloc_eval", "W3",
         [("    _cb = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)\n    _saved = {k: _cp_ebm",
           "    _cb = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)\n\n"
           "    def alloc_eval(temp, build):\n        return {}\n    _saved = {k: _cp_ebm"),
          ("_cb['a_prime'], _cb['alloc_eval'], _cb['alloc_state'],", "_cb['a_prime'], alloc_eval, _cb['alloc_state'],")]),
        ("M5 合併再試之注入物錯位", "W3",
         [("_cb['a_prime'], _cb['alloc_eval'], _cb['alloc_state'],", "_cb['a_prime'], _cb['alloc_state'], _cb['alloc_state'],")]),
        ("M6 段三之試算配地⛔ 設 'trial'", "W4",
         [("_ss[SS_END_BLOCK_MODE] = 'trial'   # 🆕", "pass   # 🆕")]),
        ("M7 合併再試之試算配地⛔ 設 'trial'", "W4",
         [("                _ss[SS_END_BLOCK_MODE] = 'trial'\n                f3_screen_stepg_run(_px, **dict(",
           "                f3_screen_stepg_run(_px, **dict(")]),
        ("M8 試算旗標⛔ 入隔離之鍵", "W5", [("    'f3_end_block_mode',\n", "")]),
        ("M9 合併再試之 finally ⛔ 復原", "W5",
         [("        for _k in " + T + ":\n            if _k in _saved:\n                _ss[_k] = _saved[_k]\n"
           "            else:\n                _ss.pop(_k, None)\n        K917_DROPPED.clear()\n"
           "        K917_DROPPED.update(_k917_saved)\n    _ss[SS_END_BLOCK_MERGE] = rec",
           "        pass\n    _ss[SS_END_BLOCK_MERGE] = rec")]),
        ("M10 逐列紀錄⛔ 寫", "W6", [("    _ss['f3_end_block_merge_log'] = log\n", "")]),
        ("M11 段三之畫面入口之首⛔ 去前次之紀錄", "W6",
         [("    _ss.pop(SS_END_BLOCK_MERGE, None)\n    _ss.pop('f3_end_block_merge_log', None)\n\n    def _end_merge",
           "\n    def _end_merge")]),
        ("M12 失效函式⛔ 去紀錄", "S2",
         [("                            _st_inv.session_state.pop(SS_END_BLOCK_MERGE, None)\n", "")]),
        ("M13 顯示⛔ 傳逐列", "S1",
         [("end_block_merge_rows(_ebm355, st.session_state.get('f3_end_block_merge_log'))",
           "end_block_merge_rows(_ebm355, [])")]),
        ("M14 顯示⛔ 出逐列表", "S1",
         [("                                st.dataframe(_pd.DataFrame(_ebm355_v['rows']),",
           "                                st.write(_pd.DataFrame(_ebm355_v['rows']),")]),
    ]


def wiring(repo):
    src = _read(repo, "app.py")
    red = []
    print("── 接線與合成案（AST·工作樹之 app.py）──")
    base = _checks(src)
    for name, ok, note in base:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    if red:
        print("── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（每一突變須使其所指之項轉紅）──")
    for mname, target, reps in _mut_list():
        m = src
        miss = []
        for a, b in reps:
            if m.count(a) != 1:
                miss.append(m.count(a))
                continue
            m = m.replace(a, b, 1)
        if miss:
            print(f"  🔴 {mname}：突變錨之命中 {miss}（期 各 1）")
            red.append(mname.split()[0])
            continue
        turned = [n.split()[0] for n, ok, _ in _checks(m) if not ok]
        ok = target in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}（須含 {target}）")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) != 3 or argv[1] != "wiring":
        print(__doc__)
        return 2
    return wiring(argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `P10`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：末端塊之合併再試（harness ＋ 畫面·含 `K-9-50`）同批入主線；畫面路徑之接線檢查與 `main()` 之合成案（`W-G.9-356`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線快轉至 `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`（原主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`·所納 `15` 筆 `commit`，其中動生產碼者 `3` 筆：`c970ae6`〔`W-G.9-353`〕／`a44a386`〔`W-G.9-354`〕／`f173a4e`〔`W-G.9-355`〕）；本批之零生產碼 `commit` 皆在主線；側支 `verify/W-G.9-353-endmerge` 留於 `1ef3bb5`（歷史·⛔ 再推）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 末端塊之合併再試與強制抵費地·harness 路徑（`K-9-49 ②`·`K-9-36 ③`） | 同「待落地清單之更新：末端塊之合併再試與強制抵費地（`K-9-49 ②`·`K-9-36 ③`）之 harness 路徑入側支（`W-G.9-353`）」節序 `1` | ✅（入主線） | `docs/orders/W-G.9-353_重量單.md` |
| `2` | 數末端塊之合併再試相互競合（`K-9-50`）·harness 路徑；後處理之承前（`K-9-48` 其二） | 同「待落地清單之更新：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑入側支（`W-G.9-354`）」節序 `1`／`2` | ✅（入主線） | `docs/orders/W-G.9-354_重量單.md` |
| `3` | 末端塊之合併再試（含 `K-9-50`）·畫面路徑 | 同「待落地清單之更新：末端塊之合併再試（含 `K-9-50`）之畫面路徑入側支；規格單流程之試行（`W-G.9-355`）」節序 `1` | ✅（入主線） | `docs/orders/W-G.9-355_規格單.md` |
| `4` | 畫面路徑之接線檢查與 `main()` 內之敘述之合成案（`自誤 517`） | 量測器 `F15`（`verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>`）：`W1`〜`W8`（`R-1` 三出口／`R-1` 單一真相源／`R-5` 四注入物／`R-3`·`R-4` 試算／`R-6` 隔離／`R-7` 紀錄／`R-12` 失效與顯示之接線）、`S1`／`S2`（`main()` 之顯示區塊與 `_f3L_invalidate_g_cache` 以假 st 實際執行）＋ 十四突變 | ✅（入主線） | `docs/orders/W-G.9-356_輕量單.md` |

🔒 **前三節之更新**（⛔ 追改前節一字）：`W-G.9-353` 節序 `1`、`W-G.9-354` 節序 `1`／`2`、`W-G.9-355` 節序 `1` ⇒ ✅（本表序 `1`〜`3`）；`W-G.9-353` 節序 `2`（畫面路徑）與 `W-G.9-354` 節序 `3`（同）⇒ ✅（本表序 `3`）；`W-G.9-355` 節序 `2` ⇒ ✅（本表序 `4`）；`W-G.9-355` 節序 `3`（同批入主線）⇒ ✅（本批）。三節其餘之序之態⛔ 變（`GB-194` 三停機款、`K-9-48` 七項 `3`／`5`／`6`、規格步 `3`〜`8`）。
🔒 **規格單流程之試行**（`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通（`W-G.9-355`）」節）：首輪（`W-G.9-355`）收束——往返 `1`（⛔ 補令、⛔ 退件）；受詞之必過之實例 ＝ CC 施工時之實跑 ＋ 發單側窗五十二自倉重跑（`docs/orders/W-G.9-356_輕量單.md` `§一` 項 `4`）；以程式字樣為錨之接線與突變檢查 ＝ 本表序 `4`（必破 ＝ `f55935c` 之 `app.py` ⇒ `rc 1`；必過 ＝ `1ef3bb5` 之 `app.py` ⇒ `rc 0`·十四突變皆轉其所指之項）。次輪 ＝ 次一張規格單；期滿由發單側向 KL 報告續否。
🔒 **本案之量**：主線 `0b05925` → `1ef3bb5` 之配地（退縮 `3.5 m`／`0 m`）⛔ 變——`verify/probes/probe_WG9349_k9296.py run` 二退縮之出艙逐位同；`run_all` 同一倉外路徑之出艙逐位同（`docs/orders/W-G.9-356_輕量單.md` `§一` 項 `5`）；合併再試二退縮皆無標的。
🔒 **本機介面**：主 checkout 同步後，執行介面之環境 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6` 皆須**未設**；按「🧮 執行 G 值迭代計算」後，成果區於「🧱 末端塊之評選」之後、「🧩 調配階段之輸入」之前多「🔗 末端塊之合併再試」一區（有逐列紀錄者展開；本案二退縮皆「無標的」·收合）。
🔒 **依賴序**：`K-9-48` 七項 `3`／`5`／`6`（另單）→ 規格步 `3` → `4` → `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `4`（子字串框·含圖例與本列）·列 ＝ `2`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄丙　工項一之二態之出艙（`F15 wiring`·發單側窗五十二實跑）

**塊 `T1`**（必過之態·`1ef3bb5` 之 `app.py`·`rc 0`）：

````text
── 接線與合成案（AST·工作樹之 app.py）──
  ✅ W0 受詞在模組層（缺 []）
  ✅ W1 R-1 三出口（三出口皆經 _end_merge → f3_screen_end_block_merge(st, …)）
  ✅ W2 R-1 單一真相源（end_block_merge_run：呼叫 1（期 1）·在合併再試之入口 1·非呼叫之引用列 []；f3_screen_end_block_merge 之呼叫 1（期 1）·在段三之畫面入口 1）
  ✅ W3 R-5 四注入物之單一真相源（巢狀 ['a_prime', 'alloc_eval', 'alloc_state', 'trial_winner']；回四鍵 True；他處同名 []；段三：['a_prime', 'trial_winner', 'alloc_state']；合併再試：['a_prime', 'alloc_eval', 'alloc_state']）
  ✅ W4 R-3／R-4 試算 'trial'（{'alloc_state': True, 'alloc_eval': True}）
  ✅ W5 R-6 隔離（SS_END_BLOCK_MODE＝'f3_end_block_mode' ∈ 鍵 True；try 前存 True；finally 復 True；K917 ['K917_DROPPED.clear', 'K917_DROPPED.update']）
  ✅ W6 R-7 紀錄（try 後寫 rec True／log True；try 內或其前寫 False；段三之畫面入口之首去 rec True／log True）
  ✅ W7 R-12 失效之二鍵（去 SS_END_BLOCK_MERGE True；去 f3_end_block_merge_log True）
  ✅ W8 R-12 顯示之接線（if 之式 True；end_block_merge_rows(X, …get('f3_end_block_merge_log')) True；位置 True）
  ✅ S1 自誤517 顯示區塊之合成案（三情形皆符）
  ✅ S2 自誤517 失效函式之合成案（未去 []；他鍵留 True；f3_g_needs_rerun True）
── 判別力（每一突變須使其所指之項轉紅）──
  ✅ M1 出口①⛔ 辦合併再試：轉紅 ['W1']（須含 W1）
  ✅ M2 出口③以段三前之宗地辦合併再試：轉紅 ['W1']（須含 W1）
  ✅ M3 以別名呼叫單一真相源：轉紅 ['W2', 'W3', 'W5', 'W6']（須含 W2）
  ✅ M4 合併再試另寫 alloc_eval：轉紅 ['W3']（須含 W3）
  ✅ M5 合併再試之注入物錯位：轉紅 ['W3']（須含 W3）
  ✅ M6 段三之試算配地⛔ 設 'trial'：轉紅 ['W4']（須含 W4）
  ✅ M7 合併再試之試算配地⛔ 設 'trial'：轉紅 ['W4']（須含 W4）
  ✅ M8 試算旗標⛔ 入隔離之鍵：轉紅 ['W5']（須含 W5）
  ✅ M9 合併再試之 finally ⛔ 復原：轉紅 ['W5']（須含 W5）
  ✅ M10 逐列紀錄⛔ 寫：轉紅 ['W6']（須含 W6）
  ✅ M11 段三之畫面入口之首⛔ 去前次之紀錄：轉紅 ['W6']（須含 W6）
  ✅ M12 失效函式⛔ 去紀錄：轉紅 ['W7', 'S2']（須含 S2）
  ✅ M13 顯示⛔ 傳逐列：轉紅 ['W8', 'S1']（須含 S1）
  ✅ M14 顯示⛔ 出逐列表：轉紅 ['S1']（須含 S1）
⇒ 紅 []；rc 0
````

**塊 `T2`**（必破之態·`f55935c` 之 `app.py`·`rc 1`）：

````text
── 接線與合成案（AST·工作樹之 app.py）──
  🔴 W0 受詞在模組層（缺 ['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows']）
  🔴 W1 R-1 三出口（return 3（期 3）；所呼 []（期 恰 1 且為巢狀函式））
  🔴 W2 R-1 單一真相源（end_block_merge_run：呼叫 0（期 1）·在合併再試之入口 0·非呼叫之引用列 []；f3_screen_end_block_merge 之呼叫 0（期 1）·在段三之畫面入口 0）
  🔴 W3 R-5 四注入物之單一真相源（k6b_screen_callbacks 缺）
  🔴 W4 R-3／R-4 試算 'trial'（k6b_screen_callbacks 缺）
  🔴 W5 R-6 隔離（f3_screen_end_block_merge 缺）
  🔴 W6 R-7 紀錄（受詞缺）
  🔴 W7 R-12 失效之二鍵（去 SS_END_BLOCK_MERGE False；去 f3_end_block_merge_log False）
  🔴 W8 R-12 顯示之接線（`X = st.session_state.get(SS_END_BLOCK_MERGE)` ＋ if 之二句缺）
  🔴 S1 自誤517 顯示區塊之合成案（抽不到顯示區塊）
  🔴 S2 自誤517 失效函式之合成案（未去 ['f3_end_block_merge', 'f3_end_block_merge_log']；他鍵留 True；f3_g_needs_rerun True）
── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──
⇒ 紅 ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'S1', 'S2']；rc 1
````

SELF_SHA256: 3460118bc977366c7c339ce4d98c67a59f963b4fb11ae34577e04bf92899181d
