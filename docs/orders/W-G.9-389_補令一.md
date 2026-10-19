# `W-G.9-389` 補令一：本補令入側支 ＋ 主線快轉（`929ea20` → 本補令工項零″ 之 `commit`·`W-G.9-389`〔試算內之程式之停機之上拋〕入主線）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-19`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-389_規格單.md`（「原單」）之 `§四-2`（入主線之短單）。原單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`；側支 `verify/W-G.9-389-trialstop` ＝ `dbe21f5e98ac5a74a3852df8f6cab3a6f4ff7db9`（原單工項四）；遠端 heads **`49`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `a298a4f`；發單端已於拋棄式 worktree 自倉從頭重跑原單之 `V-1`〜`V-9` 之 `71` 呼叫與收工閘〔`§一″` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。本補令 ＝ 入主線之短單；本批之生產碼於本案之配地⛔ 變（`§一″` 項 `2`）⇒ README 第二節之自動處理第 `1` 款。**`expects_allocation_change` ＝ `false`**。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零″ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-389_補令一.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **撇號**：「″」＝ U+2033，唯指本補令之條；無撇號者指原單之條。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-389-trialstop` 之刪除或改寫（保留為歷史）；任何他側支；`ops/queue` 除 `執行端.md` 所許外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零″`　開場（**先於工項零″**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`；`git rev-parse origin/verify/W-G.9-389-trialstop` ＝ `dbe21f5e98ac5a74a3852df8f6cab3a6f4ff7db9`；`git ls-remote --heads origin` 之列數 ＝ **`49`**（全列存 `<O>/heads_before_389p1.txt`·收工閘 `5″` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-389-trialstop` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 629 623` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `614`／`MAX` `629`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（發單端於 `dbe21f5` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五″` 項 `3`）。

### `§零-1″`　停機款

| # | 款 |
|---|---|
| `1″` | 開工時主線 ≠ `929ea20`，或側支 ≠ `dbe21f5`，或遠端 heads ≠ `49`，或施工樹之追蹤檔有變動，或 `§零″` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2″` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3″` | 工項一″ 前置之任一期不符 |
| `4″` | 工項一″ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5″` | 工項一″ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6″` | 工項零″ 之 `push` 之目標非 `verify/W-G.9-389-trialstop`；工項一″ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零″ 之 `commit`；或推至他支 |
| `7″` | `§三-1″` 收工閘任一 ≠ 期 |
| `8″` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9″` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一″ 未成者主線⛔ 動。

---

## `§一″`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-389-trialstop` 對主線 `929ea20` 唯五筆 `commit`（`git rev-list --count 929ea20..dbe21f5` ＝ `5`、反向 ＝ `0`、`--merges` 空）：`4d21a04`（工項零·`1350`／`0`·blob ＝ 來源 `8ba8c7bc…`）、`1689af8`（工項一·`8` 器 `8/4`、`5/0`、`4/0`、`5/0`、`7/0`、`10/0`、`12/1`、`662/0`·blob ＝ 原單 `§五-1` 項 `5`·塊 `Fy41` 施於 `929ea20` 之 `verify/` ≡ `1689af8` 之 `verify/`）、`a298a4f`（工項二·`app.py` `55`／`10`·blob `80d00d86155eddb843b3e3e2efa8e2e47c0db142`；`verify/selection_pipeline.py` `6`／`0`·blob `fec1d5c0f80584ab008612eec92ab540dfe44fdd`）、`b117fb3`（工項三·`K-6` 典 `53`／`0`、`docs/待落地清單.md` `20`／`0`）、`dbe21f5`（工項四·報告二檔 `989`／`0`、`250`／`0`）。五筆之首列 ＝ 所令逐字。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `a298a4f`（`app.py`、`verify/selection_pipeline.py`）。
2. **發單端之獨立復驗**（`2026-10-19`·雲端 Linux `4` 核·倉外之拋棄式 worktree·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報）：
   - **差異之逐行讀**（`git diff 1689af8 a298a4f -- app.py verify/selection_pipeline.py`）：`R-1` 五名於 `K917_DROPPED = {}` 之後、`def k917_should_drop` 之前，依序；號之式 ＝ `(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】`；`k6_program_stop` 無號 ⇒ 拋 `RuntimeError`（含 `W-G.9-389`、前 `200` 字之 `repr`·其字面⛔ 配號式）·⛔ 登記，有號 ⇒ 全文登記、回 `RuntimeError(全文)`；`k6_trial_raise_since` 上拋首一新登記者之全文。`R-2` 十處唯 `raise RuntimeError(` → `raise k6_program_stop(`（AST：施前帶號之 `raise` 恰 `10`·皆 `RuntimeError`；施後恰 `10`·皆 `k6_program_stop`；`verify/*.py` 之帶號之 `raise` 唯 `wv_reconcile.py:166`〔`GB-86`·對帳器·⛔ 在試算之路徑〕）。`R-3` 八處之 `_m389 = k6_trial_mark()`（harness 以 `ns["k6_trial_mark"]()`）與 `k6_trial_raise_since(_m389, '<where>')` 之位與 `<where>` 逐字合原單之表（`end_block_merge_run` 之 `except RuntimeError as _e:` 與 `_rec['標的'] = None` 之相接⛔ 斷）。頂層之名：新增恰五、⛔ 刪；相異之既有節點恰原單 `§三-2` 之 `11` 函式。號式、登記、巢狀之長度、首一新登記者、無號之拒，以五名之 AST 抽出另以 `21` 項之自測驗之：皆合。
   - **`71` 呼叫之重跑**：原單 `§五-1` 之「項 `8` 之表」之命令（`<repo>` ＝ 各態之拋棄式 worktree 之絕對路徑）：後態（`dbe21f5`·其 `app.py` 與 `verify/` 與 `a298a4f` 逐位同）之 `71` 呼叫 ＋ 前態（`1689af8`·工項一之端）之 `9` 呼叫（`#56`〜`#61`、`#69`〜`#71`）＝ `80` 呼叫·並行 `2`·耗時之和 `18044` s：皆 `rc` ＝ 該表之同態之期、末列逐字同（`#56`／`#57` 之末列為 JSON 之摘要·⛔ 比）、`stderr` 合計 `0` B；前態之 `#69`／`#71` ＝ `⇒ 紅 ['受詞缺']；rc 1`、`#70` ＝ `⇒ 紅 ['X1', 'X2', 'X3', 'X4']；rc 1`（對照組·⛔ 恆綠）；後態之 `F33 selftest` `K1`〜`K16`／`P0 16／16`、`F33 wiring` `X1`〜`X5`（帶號 `10`）、`F33 run` 之 `R1@3.5`（登記 `0`·G 值列 `35`）、`R1@0.0`（登記 `0`·G 值列 `36`）、`R2@3.5`（上拋含「試算內之程式之停機·手冊先行·harness 之試算」與 `GB-999 注入`）皆 ✅；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`）
   - **本案配地⛔ 變**：`k6s3 cmp`（前態 `1689af8` 對後態 `dbe21f5`）二退縮皆 `rc 0`、末列 `相異 0 項 ⇒ ✅ 同`、`stderr` `0` B；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`，其落檔與 `stdout` 以同一字樣代 `HEAD` 之全值後前後逐位同（對照：⛔ 代之則異）
   - **收工閘**（原單 `§四-3`·於 `dbe21f5`）：閘 `1` 五筆之增刪 ＝ 項 `1`；閘 `2` 生產碼相異 `2`、`verify/` 相異 `9`（`M` `8`·`A` `1`）、新檔四之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `15` 檔之 blob `CR` 合計 `0`（`data/V6.dxf` `12308`）；閘 `4` `K-6` 典 `859830` → `868268`、`docs/待落地清單.md` `7351` → `10814`·改前皆改後之嚴格前綴·其尾 ＝ 塊 `K32`／`P43`（自原單抽取·逐位同）·`CLAUDE.md`、自誤簿、`.claude/` 對 `929ea20` 相異 `0`；閘 `5` heads `49`、主線 `929ea20`、側支 `dbe21f5`（祖含 `929ea20`）；閘 `6` `closegate 629 623 .` ⇒ `rc 0`（`✅ 二閘皆過`·判別力 `630 629` ⇒ `rc 7`）；閘 `7` `rc 0`·四簿之值 ＝ `§零″` 項 `3`；閘 `8` `checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`，`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·重生成之檔與倉內逐位同
3. **快轉之受詞**：工項零″ 推後之側支之端（工項零″ 之 `commit`）；其祖含 `929ea20` 與 `dbe21f5`；`929ea20..<工項零″>` 之 `commit` 數 ＝ `6`、`--merges` 空；生產碼之命中唯 `a298a4f`（項 `1`）。

---

## `§二″`　射程

🛑 `(a)` 工項零″（零生產碼）推至側支 `verify/W-G.9-389-trialstop`（快轉）；`(b)` 工項一″ 主線快轉至工項零″ 之 `commit`（**以前置皆符為條件**·⛔ `--force`）；`(c)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb` → `<工項零″ 之全 40 碼>`」（README 第二節「入主線之安全」）；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(e)` ⛔ 及生產碼、`verify/`、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(f)` 執行報告⛔ 另立（原單工項四之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三″`　工項（依序）

### 工項零″　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-389_補令一.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-389_補令一.md` 與來源逐位同（停機款 `2″`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-389 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-389-trialstop`（快轉）。

### 工項一″　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零″ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-389-trialstop` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`。
2. `git merge-base --is-ancestor 929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb <C>` ⇒ `rc 0`；`git rev-list --count 929ea20..<C>` ＝ `6`；`git rev-list --count <C>..929ea20` ＝ `0`；`git rev-list --merges 929ea20..<C>` ＝ 空。
3. `git rev-list 929ea20..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `a298a4f3e364705a780447294dc9459e096ed4fd`（命中 `2` 列 `app.py`、`verify/selection_pipeline.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `80d00d86155eddb843b3e3e2efa8e2e47c0db142`；`git rev-parse <C>:verify/selection_pipeline.py` ＝ `fec1d5c0f80584ab008612eec92ab540dfe44fdd`；`git diff --name-only a298a4f3e364705a780447294dc9459e096ed4fd <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3″`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4″`）；⛔ 刪側支 `verify/W-G.9-389-trialstop`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5″`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads ＝ **`49`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `a298a4f` 之相異 ＝ **`0`**；判別力［必非零］：vs `929ea20` 之相異 ＝ **`2`**（`app.py`、`verify/selection_pipeline.py`）；④ `git branch -r --contains a298a4f3e364705a780447294dc9459e096ed4fd` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-389-trialstop`）。

---

## `§三-1″`　收工閘（工項一″ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1″` | 工項零″ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（``116``）／`0`·唯此一檔；首列 ＝ `§三″` 所令逐字 |
| `2″` | `git -c core.quotepath=false diff --name-status dbe21f5 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-389_補令一.md`；生產碼與 `verify/` 之一切檔對 `dbe21f5` 相異 **`0`**；判別力［必非零］：生產碼對 `929ea20` 相異 **`2`**（`app.py`、`verify/selection_pipeline.py`）、`verify/` 對 `929ea20` 相異 **`9`**（`M` `8`·`A` `1`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3″` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4″` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` | 對 `dbe21f5` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `107182948b85fa9ada222ed1e418acc14989e5d6`；自誤簿 ＝ `fb55b127c8121ad98924965dab70ca5b55372738`；`docs/待落地清單.md` ＝ `69c1bf339ad17e3195ee280da8bcc8d799251a1a`） |
| `5″` | 自限 | 遠端 heads **`49`**；主線 ＝ `<C>`；側支 `verify/W-G.9-389-trialstop` ＝ `<C>`；其餘 `47` 列中除 `ops/queue`（回報後可變）外之 `46` 列逐列 ＝ `<O>/heads_before_389p1.txt` 之同列 |
| `6″` | `python3 verify/probes/probe_WG9270_closegate.py 629 623 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 630 629 .` ⇒ `rc 7` |
| `7″` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 629 623` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零″` 項 `3` 之值（⛔ 變） |
| `8″` | 量測器（於主線之端·`17` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`… wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`… wiring <repo> 929ea20` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`35／35`（`F16`）、`74／74`（`F29`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`）、`16／16`（`F33`）；`F32 selftest` `K1`〜`K31`、`F32 wiring` `X1`〜`X5`、`F33 selftest` `K1`〜`K16`、`F33 wiring` `X1`〜`X5` 皆 ✅ |

---

## `§四″`　土地後果

**本案**：配地⛔ 變（`§一″` 項 `2`·`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔逐位同、`parity` 不符 `0`；`F33 run` 之 `R1`：harness 之全程，二退縮之程式之停機之登記皆 `0`）。**他案**：主線自此，併入之可否之試算（入池閘之併入後、末端塊合併再試、段三、手冊先行、第一趟之畫面與 harness 之試算）之內所觸之「程式未支援之形」（訊息帶 `GB-` 之號）或「須 KL 裁之形」（【未裁】）之停機，⛔ 再被當作「不過」「未成」「試算中止」而續辦——改為停機並示其全文；他之配地中止（配地上不可）照舊為「不過」。`GB-104`（街角第 1 宗之構造保證）於併入街角第 1 宗之後之試算中觸之者，讀為程式之破而停機（`K-6` 典 `W-G.9-389` 之節之二之己）。

---

## `§五″`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `dbe21f5` 之追蹤檔 `2897` 檔·`git grep -l -F`） | `W-G.9-389_補令一`、`W-G.9-389 補令一` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之全部 `*.md` 亦 `0`·發單端實查） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（態 `dbe21f5`·定稿之前一版·其後唯本列與項 `4` 之文字之填）：🔴 機械 `0` 項／🟡 提示 `0` 項／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23466`–`31208`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `dbe21f5`（雲端 Linux·⛔ `push`）＋ 本補令之定稿·一 `commit`（首列 ＝ 所令逐字）：工項零″ 之 blob ＝ 來源；工項一″ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `6`·反向 `0`·`--merges` 空·命中唯 `a298a4f`〔`2` 列〕·`app.py`／`verify/selection_pipeline.py` 之 blob ＝ `80d00d86…`／`fec1d5c0…`·對 `a298a4f` 相異空）；閘 `1″` ＝ 本補令 `116`／`0`·唯此一檔；閘 `2″` 恰一 `A`·生產碼與 `verify/` 對 `dbe21f5` 相異 `0`、生產碼對 `929ea20` 恰 `2`、`verify/` 對 `929ea20` `9`（`M` `8`·`A` `1`）·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`）；閘 `3″` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4″` 相異 `0`·四 blob ＝ 期；閘 `6″` `✅ 二閘皆過`·`630 629` ⇒ `rc 7`；閘 `7″` `rc 0`·四簿 ＝ `§零″` 項 `3`；閘 `8″` 十七呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B·`P0` ＝ 期；工項一″ 之快轉、出艙 ①②④ 與閘 `5″` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空 |

SELF_SHA256: 67fbbb0c74af89e5ab041449cca41d9c9006d876c6bb24f3b334c6f6be82efb7
