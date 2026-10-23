# `W-G.9-392` 補令三：本補令入側支 ＋ 主線快轉（`56c77fd` → 本補令工項零⁗ 之 `commit`·`W-G.9-392`〔每宗之應分配面積試算至穩定·取得之宗之自我檢查·評選之式之起算點〕入主線·KL `2026-10-23 07:39` 核可）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-23`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-392_規格單.md`（「原單」）之 `§四-2`（KL 核可 ⇒ 入主線之短單）；補令一（`docs/orders/W-G.9-392_補令一.md`）、補令二（`docs/orders/W-G.9-392_補令二.md`）之施作已畢。三單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`；側支 `verify/W-G.9-392-k980g` ＝ `0826577c9f54db002ffc2869459ec79b250491ec`（補令二工項四″）；遠端 heads **`52`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `d3d8f46`；發單端已於拋棄式 worktree 自倉從頭重跑補令一 `§五″` 項 `8` 之施後 `80` 呼叫、前態 `13` 呼叫與收工閘〔`§一⁗` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式（同原單）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。原單為新規格單而改本案之配地 ⇒ README 第二節停止條件 `2` 已成就、發單端已請示（`ops/queue` 之 `待KL/2026-10-22_392之配地核可與末端塊之認定.md`）；**KL `2026-10-23 07:39` 之答（逐字·`ops/queue` 之 `KL答覆/2026-10-23_0739.md`）：「是、是」**——其第一問逐字：「（一）將「試算至穩定、評選與實際配地同值」之成果（本案配地依上表微變）併入正式版本——**是／否**？」⇒ 本補令 ＝ 該核可之執行。**`expects_allocation_change` ＝ `true`**（主線之配地之改變 ＝ 原單 `§一` 項 `5`·KL 所核·本補令⛔ 增減）。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零⁗ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-392_補令三.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。施工樹之根之複本以 `.git/info/exclude` 免於 `git status`（其式以 `/` 起首：`/W-G.9-392_補令三.md`）。
> 🔑 **撇號**：「⁗」＝ U+2057（補令三），唯指本補令之條；「″」指補令一、「‴」指補令二；無撇號者指原單之條。
> 🔑 **快轉前之記**（README 第二節「入主線之安全」）：主線之前值 → 後值，於**快轉之前**記於 `ops/queue` 之 `log.md`（增一列）與 `STATE.json` 之 `history`（增一筆·`from` ＝ `to` ＝ `running`）⇒ `commit`（首列 `ops: 執行端快轉前之記 W-G.9-392_補令三`）、推送 `ops/queue`（被拒 ⇒ 重取再推·⛔ `--force`）；推成之後方快轉（`§三⁗` 工項一⁗）。回報之列再記快轉後之實值。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字（含 `verify/baselines/`·`§一⁗` 項 `4`）、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-392-k980g` 之刪除或改寫（保留為歷史）；任何他側支；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；KL `07:39` 之第二問（末端塊之認定·入次一規格單）。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零⁗`　開場（**先於工項零⁗**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`；`git rev-parse origin/verify/W-G.9-392-k980g` ＝ `0826577c9f54db002ffc2869459ec79b250491ec`；`git ls-remote --heads origin` 之列數 ＝ **`52`**（全列存 `<O>/heads_before_392p3.txt`·收工閘 `5⁗` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-392-k980g` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 636 634` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `621`／`MAX` `636`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `198`／`206`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `0826577` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五⁗` 項 `3`）。

### `§零-1⁗`　停機款

| # | 款 |
|---|---|
| `1⁗` | 開工時主線 ≠ `56c77fd`，或側支 ≠ `0826577`，或遠端 heads ≠ `52`，或施工樹之追蹤檔有變動，或 `§零⁗` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2⁗` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗` | 工項一⁗ 前置之任一期不符；或快轉前之記（單首 🔑）之推送不能成 |
| `4⁗` | 工項一⁗ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5⁗` | 工項一⁗ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗` | 工項零⁗ 之 `push` 之目標非 `verify/W-G.9-392-k980g`；工項一⁗ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零⁗ 之 `commit`；或推至他支 |
| `7⁗` | `§三-1⁗` 收工閘任一 ≠ 期 |
| `8⁗` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9⁗` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一⁗ 未成者主線⛔ 動（快轉前之記已推者，於回報中記「未快轉」）。

---

## `§一⁗`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-392-k980g` 對主線 `56c77fd` 唯八筆 `commit`（`git rev-list --count 56c77fd..0826577` ＝ `8`、反向 ＝ `0`、`--merges` 空）：原單工項零 `c066161`（原單）、一 `c4666ab`（`12` 器）、補令一工項零″ `31208b0`（補令一）、一″ `f12824f`（`9` 器）、補令二工項零‴ `c0ec2a5`（補令二）、補令一工項二″ `d3d8f46`（生產碼：`app.py` blob `b4cee75a8d5bfc0564ef7c855eb1dc4463f56458`、`verify/stepg_pipeline.py` blob `0cd22fc9ad8a45dcde435c1af016b26a95e0bc6b`）、三″ `43ea230`（`K-6` 典、自誤簿、`GB` 簿、`docs/待落地清單.md`）、四″ `0826577`（報告二檔）。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `d3d8f46`（`2` 列）；`git diff --name-only d3d8f46 0826577 -- app.py verify/` ＝ 空。
2. **發單端之獨立復驗**（`2026-10-22`·雲端 Linux `4` 核·倉外之拋棄式 worktree·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報·`ops/queue` 之 `log.md` `2026-10-22T23:58:42+08:00` 之列·下之數之來源：發單端於拋棄式 worktree 之實跑）：生產碼 ＝ 原趟之碼（原單回報之附錄之差異施於 `56c77fd` ⇒ `app.py` `f12af112…`）＋ 補令一 `R-7″`（`_corner_first_lot_G` 之 `_solve_G_one` 增 `w0_start=0.0` 一 hunk）·逐行讀合原單 `§三` 與補令一 `§三″`；四簿皆純末端追加且其尾 ＝ 塊（`K38`＋`K39`、`P49`＋`P50`、`G16`、`E37`＋`E38`）；`12` 器 ＝ 塊 `Fy47`＋`Fy48`；施後 `80` ＋ 前態 `13` 呼叫之 `rc`／末列皆合期、`stderr` 合計 `0` B；`F36 diff` ＝ 原單 `§一` 項 `5` 逐字（`6`／`5` 項·對照組 `45`）；`F8` 之落檔 3.5 m `8be0160b…` → `47683d1c…`、0 m `6fb86647…` → `884e9171…`；`parity` 二退縮 `rc 0`；`closegate 636 634` `rc 0`（對照 `637 636` ⇒ `rc 7`）。
3. **KL 之核可**：`2026-10-23 07:39`「是、是」（單首「授權」）。其第二問（無側面道路之端一律為末端塊）⇒ 次一規格單；⛔ 本補令之受詞。
4. **驗證之基線之處置**（待落地清單序 `28`·`K-6` 典 `W-G.9-392` 之節之四 `66`·發單端之工序之定·README 第二節自動處理第 `4` 款）：**本補令⛔ 重烤**，留專單。其由：(i) KL 令⛔ 全套驗證儀式、⛔ 跑 `run_all`（原單單首之「級」；`W-G.9-370` 以來之各單同）；(ii) `verify/baselines/v3`、`verify/baselines/wf` 之末次重烤 ＝ `2466faf`（`2026-07-25`·`git log -1 -- verify/baselines/v3 verify/baselines/wf` 於 `0826577` 實查；其後 `verify/baselines/` 之 `commit` 唯 `PROVENANCE.md` 三筆與 `E系列實測快照` 二檔二筆〔`2026-07-27`〕），其後主線之 `run_all` 已為 `FAIL` 之常態（`docs/reports/W-G.9-367R_規格步4乙第一趟_執行報告.md` 前置 `5`：`項 64`·`PASS 28`／`FAIL 36`·對帳 名目 凍存／現況 `22／36`）——於今重烤，將以一次併入 `2026-07-25` 以來諸批之變，⛔ 能唯歸因於本批，其歸因須自成一單；(iii) 基線唯供驗證之對拍，⛔ 涉配地。本批對其之影響（`G 值計算結果` 之 `迭代次數` 與 `G` 之欄、`G` 之 `±0.01`）已載於 `K-6` 典 `W-G.9-392` 之節之四 `66`；序 `28` 之態之改述由次一規格單之待落地之塊登記（純登記之事併入他單）。
5. **快轉之受詞**：工項零⁗ 推後之側支之端（工項零⁗ 之 `commit`）；其祖含 `56c77fd` 與 `0826577`；`56c77fd..<工項零⁗>` 之 `commit` 數 ＝ `9`、`--merges` 空；生產碼之命中唯 `d3d8f46`（項 `1`）。

---

## `§二⁗`　射程

🛑 `(a)` 工項零⁗（零生產碼）推至側支 `verify/W-G.9-392-k980g`（快轉）；`(b)` 快轉前之記（單首 🔑）推至 `ops/queue`；`(c)` 工項一⁗ 主線快轉至工項零⁗ 之 `commit`（**以前置皆符、快轉前之記已推為條件**·⛔ `--force`）；`(d)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81` → `<工項零⁗ 之全 40 碼>`」（快轉後之實值）；`(e)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(f)` ⛔ 及生產碼、`verify/`（含基線·`§一⁗` 項 `4`）、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(g)` 執行報告⛔ 另立（原單之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三⁗`　工項（依序）

### 工項零⁗　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-392_補令三.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-392_補令三.md` 與來源逐位同（停機款 `2⁗`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-392 補令三 工項零⁗：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-392-k980g`（快轉）。

### 工項一⁗　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零⁗ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-392-k980g` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`。
2. `git merge-base --is-ancestor 56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81 <C>` ⇒ `rc 0`；`git rev-list --count 56c77fd..<C>` ＝ `9`；`git rev-list --count <C>..56c77fd` ＝ `0`；`git rev-list --merges 56c77fd..<C>` ＝ 空。
3. `git rev-list 56c77fd..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `d3d8f46e9a067ecb45e93374ec8bd0ce4cb68458`（命中 `2` 列：`app.py`、`verify/stepg_pipeline.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `b4cee75a8d5bfc0564ef7c855eb1dc4463f56458`；`git rev-parse <C>:verify/stepg_pipeline.py` ＝ `0cd22fc9ad8a45dcde435c1af016b26a95e0bc6b`；`git diff --name-only d3d8f46e9a067ecb45e93374ec8bd0ce4cb68458 <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3⁗`·⛔ 快轉。

**快轉前之記**（前置皆符後·單首 🔑）：`ops/queue` 之 `log.md` 增一列、`STATE.json` 之 `history` 增一筆，皆記「主線 `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81` → `<C>`（將快轉）」⇒ `commit`、推送 `ops/queue`。推成之後方行下款。

**快轉**（與前置、快轉前之記為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4⁗`）；⛔ 刪側支 `verify/W-G.9-392-k980g`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads ＝ **`52`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `d3d8f46` 之相異 ＝ **`0`**；判別力［必非零］：vs `56c77fd` 之相異 ＝ **`2`**（`app.py`、`verify/stepg_pipeline.py`）；④ `git branch -r --contains d3d8f46e9a067ecb45e93374ec8bd0ce4cb68458` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-392-k980g`）。

---

## `§三-1⁗`　收工閘（工項一⁗ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗` | 工項零⁗ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（`117`）／`0`·唯此一檔；首列 ＝ `§三⁗` 所令逐字 |
| `2⁗` | `git -c core.quotepath=false diff --name-status 0826577 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-392_補令三.md`；生產碼與 `verify/` 之一切檔對 `0826577` 相異 **`0`**；判別力［必非零］：生產碼對 `56c77fd` 相異 **`2`**（`app.py`、`verify/stepg_pipeline.py`）、`verify/` 對 `56c77fd` 相異 **`13`**（`M` `12`·`A` `1`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md`、`verify/baselines/` | 對 `0826577` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `bb1f801424c698e392cfa5c289a14d509ac772d7`；自誤簿 ＝ `043851e0ea12bb1956d32836aff0edae306802bc`；`GB` 簿〔`docs/reports/W-G.4_泛用阻塞項登記表.md`〕＝ `240317a7c1bac742607302bb987a031ca597d4a6`；`docs/待落地清單.md` ＝ `0f71f2a4691bf2e7434a064f9d104cd58cdb6162`） |
| `5⁗` | 自限 | 遠端 heads **`52`**；主線 ＝ `<C>`；側支 `verify/W-G.9-392-k980g` ＝ `<C>`；其餘 `50` 列中除 `ops/queue`（回報後可變）外之 `49` 列逐列 ＝ `<O>/heads_before_392p3.txt` 之同列 |
| `6⁗` | `python3 verify/probes/probe_WG9270_closegate.py 636 634 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 637 636 .` ⇒ `rc 7` |
| `7⁗` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 636 634` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零⁗` 項 `3` 之值（⛔ 變） |
| `8⁗` | 量測器（於主線之端·`27` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`… wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`… wiring <repo> 929ea20`；`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`；`… wiring <repo> 2aa6302`；`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`；`… wiring <repo> a8657c4`；`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`；`… wiring <repo> 56c77fd` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`、`F32`）、`29／29`（`F28`）、`16／16`（`F33`）、`14／14`（`F34`）、`22／22`（`F35`）、`17／17`（`F36`） |

---

## `§四⁗`　土地後果

**本案**：主線之配地自此改變 ＝ 原單 `§一` 項 `5`（KL `07:39` 所核·本補令⛔ 增減·發單端之實測 ＝ `§一⁗` 項 `2` 之 `F36 diff`）——**退縮 3.5 m**（`6` 項）：宗 `R5`·`628-18(2)` 之應分配面積 `268.33` → `268.34 ㎡`；抵費地 `R1-抵費地-1` `851.68` → `851.69`、`R3` `1651.41` → `1651.40`、`R4` `697.40` → `697.39`、`R5` `1221.44` → `1221.45`、`R6` `980.59` → `980.58 ㎡`；**退縮 0 m**（`5` 項）：抵費地 `R1-抵費地-1` `851.67` → `851.69`、`R3` `1651.41` → `1651.40`、`R4` `697.40` → `697.39`、`R5` `1221.47` → `1221.46`、`R6` `980.59` → `980.58 ㎡`；他之宗之地號、地主、宗序、推進之側、街角之得標、強制抵費地、剔除皆⛔ 變。**他案**：主線自此，每宗之應分配面積試算至穩定（容差 `1e-6`）後取至小數 `2` 位；街角第 1 宗與末端塊之當選者，實配時以評選之式重算而比，取至 `2` 位相異 ⇒ 停機（`GB-206`）；街角第 1 宗之評選之側街負擔之起算點 ＝ 側面道路邊線（`0 m`·`K-9-41` ①）。

---

## `§五⁗`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `0826577` 之追蹤檔 `2917` 檔·`git grep -l -F`） | `W-G.9-392_補令三`、`W-G.9-392 補令三` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之 `*.md` 唯 `log.md` 之發單端上鎖之列命中·⛔ 占號） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（態 `0826577` ＋ 本補令之定稿之前一版·其後唯本列與項 `4` 之文字與末列之填）：🔴 機械 `0` 項（定稿之前一版之 `P-5` 唯末列之占位〔全 `0`〕之不符·定稿以實算之值填之）／🟡 提示 `0` 項（初稿之 `P-4`〔`§一⁗` 項 `2` 之數之來源〕、`P-6`〔`§四⁗` 之實測出處〕二項已於文中具名而消）／ℹ️ 記錄（`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23759`–`31502`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `0826577`（雲端 Linux·⛔ `push`）＋ 本補令之定稿之前一版·一 `commit`（首列 ＝ 所令逐字）：工項零⁗ 之 blob ＝ 來源；工項一⁗ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `9`·反向 `0`·`--merges` 空·命中唯 `d3d8f46`〔`2` 列〕·二檔之 blob ＝ 期·對 `d3d8f46` 相異空）；閘 `1⁗` ＝ 本補令 `117`／`0`·唯此一檔；閘 `2⁗` 恰一 `A`·生產碼與 `verify/` 對 `0826577` 相異 `0`、生產碼對 `56c77fd` 恰 `2`、`verify/` 對 `56c77fd` `13`（`M` `12`·`A` `1`）·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`）·`git ls-files ':(glob)verify/*.py'` `33` 檔；閘 `3⁗` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4⁗` 相異 `0`·五 blob ＝ 期；閘 `6⁗` `✅ 二閘皆過`·`637 636` ⇒ `rc 7`；閘 `7⁗` `rc 0`·四簿 ＝ `§零⁗` 項 `3`；閘 `8⁗` 二十七呼叫（於 `0826577`·其 `verify/` 與生產碼與模擬之 `<C>` 逐位同）皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B（耗時之和 `452` s·環境 `pip freeze` `ae1438da…`）；快轉前之記、工項一⁗ 之快轉、出艙 ①②④ 與閘 `5⁗` 須遠端·⛔ 模擬 |

SELF_SHA256: 581148fdf00859525d2a59c6eff831031343aafc937f6cd2dc416fb645403a67
