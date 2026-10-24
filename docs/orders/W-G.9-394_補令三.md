# `W-G.9-394` 補令三：本補令入側支 ＋ 主線快轉（`5d2a283` → 本補令工項零⁗ 之 `commit`·`W-G.9-394`〔候選之試算中受併宗須部分併出（`GB-205`）⇒ 該候選不過（`K-9-61` ⑤）·採用之配地照舊停機〕入主線·本案配地⛔ 變）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-24`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-394_規格單.md`（「原單」）、`docs/orders/W-G.9-394_補令一.md`（「補令一」）、`docs/orders/W-G.9-394_補令二.md`（「補令二」）之 `§四-2‴`（復驗皆符而本案之配地⛔ 變 ⇒ 入主線之短單）。原單、補令一、補令二留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`；側支 `verify/W-G.9-394-k9615` ＝ `b922ae0b9a07986136db38625ee6ffbafe393fe2`（補令一工項四″·補令二所續）；遠端 heads（**排除出圖線之分支**·下之 🔑）＝ **`54`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `3f36450`；發單端已於拋棄式 worktree 自倉從頭重跑補令一「項 `8` 之表」之施後 `87` 呼叫、前態 `14` 呼叫與收工閘〔`§一⁗` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式（同原單）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。原單 ＝ 待落地清單上已有 KL 裁示之項目（`K-9-61` ⑤·`GB-205`·待落地序 `8`／`9`）而本案之配地⛔ 變 ⇒ README 第二節自動處理第 `1` 款（入主線）。**`expects_allocation_change` ＝ `false`**。
> 🔑 **遠端分支之閘之母體**（`發單端.md` 丙之 3·KL `2026-10-23 17:31` 立出圖線）：本補令之一切以 `git ls-remote --heads origin` 之列數或逐列之值為閘者，其母體一律 ＝ `git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"` 之出艙（排除出圖線之 `refs/heads/wip/plots` 與 `refs/heads/verify/W-P.*`·其由出圖線推送，與本補令無涉）；本補令所載之 heads 之數皆指此母體。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零⁗ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-394_補令三.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。施工樹之根之複本以 `.git/info/exclude` 免於 `git status`（其式以 `/` 起首：`/W-G.9-394_補令三.md`）。
> 🔑 **撇號**：「⁗」（U+2057）＝ 補令三，唯指本補令之條；「‴」＝ 補令二；「″」＝ 補令一；無撇號者指原單之條。
> 🔑 **快轉前之記**（README 第二節「入主線之安全」）：主線之前值 → 後值，於**快轉之前**記於 `ops/queue` 之 `log.md`（增一列）與 `STATE.json` 之 `history`（增一筆·`from` ＝ `to` ＝ `running`）⇒ `commit`（首列 `ops: 執行端快轉前之記 W-G.9-394_補令三`）、推送 `ops/queue`（被拒 ⇒ `pull --rebase` 重取再推·⛔ `--force`）；推成之後方快轉（`§三⁗` 工項一⁗）。回報之列再記快轉後之實值。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字（含 `verify/baselines/`）、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-394-k9615` 之刪除或改寫（保留為歷史）；任何他側支（含出圖線之 `wip/plots`、`verify/W-P.*`）；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零⁗`　開場（**先於工項零⁗**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`；`git rev-parse origin/verify/W-G.9-394-k9615` ＝ `b922ae0b9a07986136db38625ee6ffbafe393fe2`；`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"` 之列數 ＝ **`54`**（其全列存 `<O>/heads_before_394p3.txt`·收工閘 `5⁗` 用；另存未濾之全列 `<O>/heads_all_before_394p3.txt` 供記）；施工樹 `git checkout --detach origin/verify/W-G.9-394-k9615` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 640 637` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `625`／`MAX` `640`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `b922ae0` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五⁗` 項 `3`）。

### `§零-1⁗`　停機款

| # | 款 |
|---|---|
| `1⁗` | 開工時主線 ≠ `5d2a283`，或側支 ≠ `b922ae0`，或遠端 heads（濾後）≠ `54`，或施工樹之追蹤檔有變動，或 `§零⁗` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2⁗` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗` | 工項一⁗ 前置之任一期不符；或快轉前之記（單首 🔑）之推送不能成 |
| `4⁗` | 工項一⁗ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5⁗` | 工項一⁗ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗` | 工項零⁗ 之 `push` 之目標非 `verify/W-G.9-394-k9615`；工項一⁗ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零⁗ 之 `commit`；或推至他支 |
| `7⁗` | `§三-1⁗` 收工閘任一 ≠ 期 |
| `8⁗` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9⁗` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一⁗ 未成者主線⛔ 動（快轉前之記已推者，於回報中記「未快轉」）。

---

## `§一⁗`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-394-k9615` 對主線 `5d2a283` 唯八筆 `commit`（`git rev-list --count 5d2a283..b922ae0` ＝ `8`、反向 ＝ `0`、`--merges` 空）：原單工項零 `866f2d5`（原單）、一 `9e25177`（`4` 器）、補令一工項零″ `bf363f4`（補令一）、一″ `9a952c9`（塊 `Fy51`·`F38`）、補令二工項零‴ `04d0757`（補令二）、補令一工項二″ `3f36450`（生產碼：`app.py` blob `b39dfc4598f48d4fa829df2b92ed023707bcd285`·`+18`／`−4`）、三″ `94b1280`（`K-6` 典、`docs/待落地清單.md`、自誤簿、`GB` 簿）、四″ `b922ae0`（報告二檔）。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `3f36450`（`1` 列：`app.py`）；`git diff --name-only 3f36450 b922ae0 -- app.py verify/` ＝ 空。
2. **發單端之獨立復驗**（`2026-10-24`·雲端 Linux `4` 核·倉外之拋棄式 worktree〔施後 ＝ `3f36450`、前態 ＝ 補令二工項零‴ 之端 `04d0757`〕·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報·`ops/queue` 之 `log.md` 之發單端之復驗之列·下之數之來源：發單端於拋棄式 worktree 之實跑）：生產碼唯 `app.py`（`+18`／`−4`·`b39dfc45…`·逐行讀合原單 `§三-1` `R-1`〜`R-6`〔`R-4` ⛔ 動〕；回報 ⑧ 之差異〔`4614` B·`82b505e6…`·`63` 列〕施於 `9e25177` ⇒ 同 blob·`git diff --no-index` `rc 0`；AST 頂層 `417`／`417`·名⛔ 增減·相異之節點恰四 ＝ `{end_block_merge_run, k6_trial_raise_since, k6b_stage3_run, k953_manual_run}`）；`4` 器之 blob ＝ 原單 `§五-1` 項 `5`（`F38` ＝ 補令一 `§五″` 項 `5` 之 `1a6f2b7c…`）；四簿皆純末端追加且其尾 ＝ 塊依序（`K41`＋`K42`、`P52`＋`P53`、`E40`＋`E41`＋`E42`、`G18`·blob ＝ `§三-1⁗` 閘 `4⁗`）；補令一「項 `8` 之表」之施後 `87` 呼叫 ＋ 前態 `14` 呼叫（`#5`、`#6`、`#56`〜`#61`、`#69`、`#73`、`#82`、`#85`〜`#87`）之 `rc`／末列皆合期（前態之 `#85`、`#86` `rc 1` 如期之紅）、`stderr` 合計 `0` B（耗時之和 `20870` s·並行 `2`）；`F38` 之 `T1`〜`T14`（`24` 項）、`W1`〜`W8`、`R1@3.5`／`R2@3.5`／`R1@0.0`／`R2@0.0` 皆 ✅；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`；`F36 diff` 二退縮 `全比相異 0 項`（對照組：前態之 3.5 m 對 0 m ⇒ `全比相異 44 項`）、`k6s3 cmp` 二退縮 `相異 0 項 ⇒ ✅ 同`；`F8` 之落檔前後逐位同（3.5 m `47683d1c…`、0 m `884e9171…`）；`parity` 二退縮之落檔與 `stdout` 以同一字樣代 `HEAD` 後逐位同（⛔ 代則異）；`V-8″` 「W-G.9-394」`6`、「K-9-61 ⑤」`7`（前 `5`）；收工閘 `1″`〜`4″`、`6″`〜`8″` 皆合（`closegate 640 637` `rc 0`·對照 `641 640` `rc 7`；anchor 自誤 `625`／`640`、`GB` `199`／`207`、`VR` `80`／`95`、`K-9` `77`／`80`；`checkidx` `索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` `則 124；加註節 14；列 158`·重生成之檔逐位同）；閘 `5″`：濾後 `54`、主線 `5d2a283`、側支 `b922ae0`（祖含 `9a952c9`）、他 `52` 列之末筆皆早於本批。
3. **入主線之依據**：補令二 `§四-2‴`（皆符而本案之配地⛔ 變 ⇒ 入主線之短單）；README 第二節自動處理第 `1` 款。
4. **快轉之受詞**：工項零⁗ 推後之側支之端（工項零⁗ 之 `commit`）；其祖含 `5d2a283` 與 `b922ae0`；`5d2a283..<工項零⁗>` 之 `commit` 數 ＝ `9`、`--merges` 空；生產碼之命中唯 `3f36450`（項 `1`）。

---

## `§二⁗`　射程

🛑 `(a)` 工項零⁗（零生產碼）推至側支 `verify/W-G.9-394-k9615`（快轉）；`(b)` 快轉前之記（單首 🔑）推至 `ops/queue`；`(c)` 工項一⁗ 主線快轉至工項零⁗ 之 `commit`（**以前置皆符、快轉前之記已推為條件**·⛔ `--force`）；`(d)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7` → `<工項零⁗ 之全 40 碼>`」（快轉後之實值）；`(e)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(f)` ⛔ 及生產碼、`verify/`（含基線）、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(g)` 執行報告⛔ 另立（原單之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三⁗`　工項（依序）

### 工項零⁗　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-394_補令三.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-394_補令三.md` 與來源逐位同（停機款 `2⁗`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-394 補令三 工項零⁗：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-394-k9615`（快轉）。

### 工項一⁗　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零⁗ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-394-k9615` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`。
2. `git merge-base --is-ancestor 5d2a2836617bc2aea57f0c7513e67d9b2313f7f7 <C>` ⇒ `rc 0`；`git rev-list --count 5d2a283..<C>` ＝ `9`；`git rev-list --count <C>..5d2a283` ＝ `0`；`git rev-list --merges 5d2a283..<C>` ＝ 空。
3. `git rev-list 5d2a283..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `3f36450aa2c3330bffa7f13e9662dfdeee9307a0`（命中 `1` 列：`app.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `b39dfc4598f48d4fa829df2b92ed023707bcd285`；`git diff --name-only 3f36450aa2c3330bffa7f13e9662dfdeee9307a0 <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3⁗`·⛔ 快轉。

**快轉前之記**（前置皆符後·單首 🔑）：`ops/queue` 之 `log.md` 增一列、`STATE.json` 之 `history` 增一筆，皆記「主線 `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7` → `<C>`（將快轉）」⇒ `commit`、推送 `ops/queue`。推成之後方行下款。

**快轉**（與前置、快轉前之記為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4⁗`）；⛔ 刪側支 `verify/W-G.9-394-k9615`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads（濾後·單首 🔑）＝ **`54`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `3f36450` 之相異 ＝ **`0`**；判別力［必非零］：vs `5d2a283` 之相異 ＝ **`1`**（`app.py`）；④ `git branch -r --contains 3f36450aa2c3330bffa7f13e9662dfdeee9307a0` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-394-k9615`）。

---

## `§三-1⁗`　收工閘（工項一⁗ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗` | 工項零⁗ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（`117`）／`0`·唯此一檔；首列 ＝ `§三⁗` 所令逐字 |
| `2⁗` | `git -c core.quotepath=false diff --name-status b922ae0 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-394_補令三.md`；生產碼與 `verify/` 之一切檔對 `b922ae0` 相異 **`0`**；判別力［必非零］：生產碼對 `5d2a283` 相異 **`1`**（`app.py`）、`verify/` 對 `5d2a283` 相異 **`4`**（`M` `3`·`A` `1`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md`、`verify/baselines/` | 對 `b922ae0` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `8aaf0433ebade3a3fa65a2fdb48457829771a3f3`；自誤簿 ＝ `f7a54a014b7b986fdffa26e83dd2641fbf28617d`；`GB` 簿〔`docs/reports/W-G.4_泛用阻塞項登記表.md`〕＝ `2d1a44b0de499d0c7d6ada72510882deb8660272`；`docs/待落地清單.md` ＝ `87205e000bbcf573313689798f0755e8bba0615d`） |
| `5⁗` | 自限（母體 ＝ 單首 🔑 之濾後之列） | 遠端 heads **`54`**；主線 ＝ `<C>`；側支 `verify/W-G.9-394-k9615` ＝ `<C>`；其餘 `52` 列中除 `ops/queue`（回報後可變）外之 `51` 列逐列 ＝ `<O>/heads_before_394p3.txt` 之同列 |
| `6⁗` | `python3 verify/probes/probe_WG9270_closegate.py 640 637 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 641 640 .` ⇒ `rc 7` |
| `7⁗` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 640 637` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零⁗` 項 `3` 之值（⛔ 變） |
| `8⁗` | 量測器（於主線之端·`33` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`… wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`… wiring <repo> 929ea20`；`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`；`… wiring <repo> 2aa6302`；`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`；`… wiring <repo> a8657c4`；`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`；`… wiring <repo> 56c77fd`；`python3 verify/probes/probe_WG9352_endblock.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`；`… wiring <repo> cf1b415`；`python3 verify/probes/probe_WG9394_k9615.py selftest <repo>`；`… wiring <repo> 5d2a283` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`、`F32`）、`29／29`（`F28`）、`16／16`（`F33`）、`14／14`（`F34`）、`22／22`（`F35`）、`17／17`（`F36`） |

---

## `§四⁗`　土地後果

**本案**：主線之配地⛔ 變（發單端之實測 ＝ `§一⁗` 項 `2`：`F36 diff` 二退縮 `全比相異 0 項`、`k6s3 cmp` `相異 0 項`、`F8` 之落檔前後逐位同、`parity` 之落檔與 `stdout` 代 `HEAD` 後逐位同）。**他案**：主線自此，候選之試算（段三之「不影響原位次」之檢核、`K-9-50` 題一 4 之「連同其半併入已取得之一端」之試算、手冊先行與第一趟之併入後之試算）中，已收受非其成員之土地（道路片等）之宗若須依手冊部分併出（`GB-205` 之形）⇒ 該候選判為不過（`K-9-61` ⑤ 回到收受之前·`K-9-48` 其三），其後依各處既有之不過之處置（`K-9-66` 按比例併入其容得下之部分等）續行（原為全區停機）；採用之配地之試算（併入前、現態、末端塊合併再試之現態、手冊先行之取代之試算、定案）中遇之者照舊停機示訊（其退回之機制未落地·待落地序 `34`）。

---

## `§五⁗`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `b922ae0` 之追蹤檔 `2929` 檔·`git grep -l -F`） | `W-G.9-394_補令三`、`W-G.9-394 補令三` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之 `*.md` 亦 `0`） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（態 `b922ae0` ＋ 本補令之定稿之前一版·其後唯本列與項 `4` 之文字與末列之填）：🔴 機械 `0` 項（定稿之前一版之 `P-5` 唯末列之占位〔全 `0`〕之不符·定稿以實算之值填之）／🟡 提示 `0` 項／ℹ️ 記錄（`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23826`–`31569`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `b922ae0`（雲端 Linux·⛔ `push`）＋ 本補令之定稿之前一版·一 `commit`（首列 ＝ 所令逐字）：工項零⁗ 之 blob ＝ 來源、`git status --porcelain` 唯此一檔；工項一⁗ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `9`·反向 `0`·`--merges` 空·命中唯 `3f36450`〔`1` 列〕·`app.py` 之 blob ＝ `b39dfc45…`·對 `3f36450` 相異空）；閘 `1⁗` ＝ 本補令 `117`／`0`·唯此一檔；閘 `2⁗` 恰一 `A`·生產碼與 `verify/` 對 `b922ae0` 相異 `0`、生產碼對 `5d2a283` 恰 `1`、`verify/` 對 `5d2a283` `4`（`M` `3`·`A` `1`）·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`）·`git ls-files ':(glob)verify/*.py'` `33` 檔；閘 `3⁗` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4⁗` 相異 `0`·五 blob ＝ 期；閘 `6⁗` `✅ 二閘皆過`·`641 640` ⇒ `rc 7`；閘 `7⁗` `rc 0`·四簿 ＝ `§零⁗` 項 `3`；閘 `8⁗` 三十三呼叫（於模擬之 `<C>`）皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B·`P0` ＝ 期（耗時之和 `675` s·並行 `2`·環境 `pip freeze` `ae1438da…`）；快轉前之記、工項一⁗ 之快轉、出艙 ①②④ 與閘 `5⁗` 須遠端·⛔ 模擬 |

SELF_SHA256: 2bb95ba78f561dfa06df950b052496d411a5e868348ba57967fc17f6a7469f27
