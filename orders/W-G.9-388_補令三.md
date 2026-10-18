# `W-G.9-388` 補令三：本補令入側支 ＋ 主線快轉（`fd88f64` → 本補令工項零⁗ 之 `commit`·`W-G.9-388`〔`K-9-61` ①②③⑥ 之落地·「另一側」扣路衝街廓〕入主線）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-19`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-388_規格單.md`（「原單」）之 `§四-2`、`docs/orders/W-G.9-388_補令一.md`（「補令一」）之 `§四-2″`、`docs/orders/W-G.9-388_補令二.md`（「補令二」）之 `§四-2‴`（入主線之短單）。原單、補令一、補令二留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `fd88f64793a373ab921999fbe5b325c44f0c2a4c`；側支 `verify/W-G.9-388-k961s3` ＝ `906a8ff0e0ca18c1679fa370e278b2f7b6e716d9`（補令一工項四″·補令二所續）；遠端 heads **`48`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `8fd9f8a`；發單端已於拋棄式 worktree 自倉從頭重跑補令一之 `V-1″`〜`V-9″` 之 `68` 呼叫與收工閘〔`§一⁗` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。本補令 ＝ 入主線之短單；本批之生產碼於本案之配地⛔ 變（`§一⁗` 項 `2`）⇒ README 第二節之自動處理第 `1` 款。**`expects_allocation_change` ＝ `false`**。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零⁗ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-388_補令三.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **撇號**：「⁗」＝ U+2057，唯指本補令之條；「‴」＝ U+2034，指補令二之條；「″」＝ U+2033，指補令一之條；無撇號者指原單之條。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-388-k961s3` 之刪除或改寫（保留為歷史）；任何他側支；`ops/queue` 除 `執行端.md` 所許外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零⁗`　開場（**先於工項零⁗**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `fd88f64793a373ab921999fbe5b325c44f0c2a4c`；`git rev-parse origin/verify/W-G.9-388-k961s3` ＝ `906a8ff0e0ca18c1679fa370e278b2f7b6e716d9`；`git ls-remote --heads origin` 之列數 ＝ **`48`**（全列存 `<O>/heads_before_388p3.txt`·收工閘 `5⁗` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-388-k961s3` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 629 623` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `614`／`MAX` `629`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（發單端於 `906a8ff` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五⁗` 項 `3`）。

### `§零-1⁗`　停機款

| # | 款 |
|---|---|
| `1⁗` | 開工時主線 ≠ `fd88f64`，或側支 ≠ `906a8ff`，或遠端 heads ≠ `48`，或施工樹之追蹤檔有變動，或 `§零⁗` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2⁗` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗` | 工項一⁗ 前置之任一期不符 |
| `4⁗` | 工項一⁗ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5⁗` | 工項一⁗ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗` | 工項零⁗ 之 `push` 之目標非 `verify/W-G.9-388-k961s3`；工項一⁗ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零⁗ 之 `commit`；或推至他支 |
| `7⁗` | `§三-1⁗` 收工閘任一 ≠ 期 |
| `8⁗` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9⁗` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一⁗ 未成者主線⛔ 動。

---

## `§一⁗`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-388-k961s3` 對主線 `fd88f64` 唯八筆 `commit`（`git rev-list --count fd88f64..906a8ff` ＝ `8`、反向 ＝ `0`、`--merges` 空）：`347b3b4`（原單工項零·`1192`／`0`）、`9977c86`（原單工項一·`6` 器 `10/5`、`16/5`、`4/2`、`3/1`、`2/1`、`504/0`·blob ＝ 原單 `§五-1` 項 `5`）、`b250d63`（補令一工項零″·`419`／`0`）、`28f87ca`（補令一工項一″·`F32` `40`／`0`·blob `75411dc5…`）、`6973af4`（補令二工項零‴·`131`／`0`）、`8fd9f8a`（補令一工項二″·`app.py` `104`／`39`·blob `3f023996da947e45db08740313921c78f2f9e265`）、`c38fb71`（補令一工項三″·`K-6` 典 `136`／`0`、自誤簿 `66`／`0`、`docs/待落地清單.md` `46`／`0`）、`906a8ff`（補令一工項四″·報告二檔 `675`／`0`、`228`／`0`）。八筆之首列 ＝ 所令逐字（工項三″ 依補令二 `D-4`）。三單之倉內 blob ＝ `ops/queue` 之來源（`606428c4…`、`b42aa268…`、`37a35166…`）。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `8fd9f8a`（`app.py`）。
2. **發單端之獨立復驗**（`2026-10-19`·雲端 Linux `4` 核·倉外之拋棄式 worktree·殼無 `WV_`·Python `3.11.17`·`shapely 2.2.0`·⛔ 採執行端之自報）：
   - **差異之逐行讀**：`<回報第十節之差異>`（`16173` B·`b5eff4af…`·`225` 列）施於 `28f87ca` 之 `app.py`（`efae3a5a…`）⇒ `7c27fb35be5d5315db501dcddf1d4e9d736812da`（`R-0″`）；`git diff --no-index <R-0″ 之 app.py> <8fd9f8a 之 app.py>` 唯 `k6b_stage3_run` 之一處（`+7`／`-3`）：每一道路片之 `_road_halves` 唯呼一次、其諸半之 `_nbr_blocks` 列為 `_hv388`；近半（所臨含 `x` 之所屬街廓者）之所臨之聯集 `_n388`；遠半之所臨 ∩ `B` − `_n388` 者記 `_recv_of(該街廓, 該道路片)`；註一行引補令一與 `K-9-63` ⑩ ⇒ 合補令一 `R-6′`（`N` 以道路片為單位·⛔ 跨道路片累積）。`R-0″` 之 `225` 列逐條對原單 `§三-1` 之 `R-1`〜`R-9`：合。`V-8″` 之十字樣 ＝ 期（施前 `28f87ca` 之判別力：七字樣異）。
   - **`68` 呼叫之重跑**：補令一 `§五″` 之「項 `8` 之表」之命令（`<repo>` ＝ 各態之拋棄式 worktree 之絕對路徑）：後態（`906a8ff`·其 `app.py` 與 `verify/` 與 `8fd9f8a` 逐位同）之 `68` 呼叫 ＋ 前態（`28f87ca`·補令一工項一″ 之端）之 `11` 呼叫（`#26`、`#38`、`#39`、`#56`〜`#61`、`#65`、`#66`）＝ `79` 呼叫·並行 `2`·耗時之和 `11025` s：皆 `rc` ＝ 該表之同態之期、末列逐字同（`#56`／`#57` 之末列為 JSON 之摘要·⛔ 比）、`stderr` 合計 `0` B；前態之 `#26`、`#38`、`#39`、`#65`（`K1`〜`K31` 皆紅）、`#66` 紅 ＝ 期（對照組）；後態之 `P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`）
   - **本案配地⛔ 變**：`k6s3 cmp`（前態 `28f87ca` 對後態 `906a8ff`）二退縮皆 `rc 0`、末列 `相異 0 項 ⇒ ✅ 同`、`stderr` `0` B；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`，其落檔與 `stdout` 以同一字樣代 `HEAD` 之全值後前後逐位同（對照：⛔ 代之則異）
   - **收工閘**（補令一 `§四-3″`·依補令二 `D-5`〜`D-10`·於 `906a8ff`）：閘 `1″`（`D-5`）八筆之增刪 ＝ 項 `1`；閘 `2″`（`D-6`）生產碼相異 `1`（`app.py`）、`verify/` 相異 `6`（`M` `5`·`A` `1`）、新檔之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3″`（`D-7`）`15` 檔之 blob `CR` 合計 `0`（`data/V6.dxf` `12308`）；閘 `4″`（`D-8`）`K-6` 典 `837880` → `859830`、自誤簿 `1203451` → `1215603`·改前皆改後之嚴格前綴·其尾 ＝ 塊 `K30`＋`K31`、`E31`＋`E32`＋`E33`（自三單抽取·逐位同）·`docs/待落地清單.md` ＝ 塊 `P41`＋`P42`（`7351` B）·三 blob `a3f9d47a…`／`fb55b127…`／`76bc7135…`·`CLAUDE.md`、`GB` 簿、`VR` 簿、`.claude/` 對 `fd88f64` 相異 `0`；閘 `5″` heads `48`、主線 `fd88f64`、側支 `906a8ff`（祖含 `28f87ca`）；閘 `6″` `closegate 629 623 .` ⇒ `rc 0`（`✅ 二閘皆過`·判別力 `630 629` ⇒ `rc 7`）；閘 `7″` `rc 0`·四簿之值 ＝ `§零⁗` 項 `3`；閘 `8″` `checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`，`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·重生成之檔與倉內逐位同；差異檔（`docs/reports/W-G.9-388R_K-9-61之一二三六之落地_app差異.diff`）＝ `git diff fd88f64 8fd9f8a -- app.py` 逐位同
3. **快轉之受詞**：工項零⁗ 推後之側支之端（工項零⁗ 之 `commit`）；其祖含 `fd88f64` 與 `906a8ff`；`fd88f64..<工項零⁗>` 之 `commit` 數 ＝ `9`、`--merges` 空；生產碼之命中唯 `8fd9f8a`（項 `1`）。

---

## `§二⁗`　射程

🛑 `(a)` 工項零⁗（零生產碼）推至側支 `verify/W-G.9-388-k961s3`（快轉）；`(b)` 工項一⁗ 主線快轉至工項零⁗ 之 `commit`（**以前置皆符為條件**·⛔ `--force`）；`(c)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `fd88f64793a373ab921999fbe5b325c44f0c2a4c` → `<工項零⁗ 之全 40 碼>`」（README 第二節「入主線之安全」）；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(e)` ⛔ 及生產碼、`verify/`、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(f)` 執行報告⛔ 另立（補令一工項四″ 之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三⁗`　工項（依序）

### 工項零⁗　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-388_補令三.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-388_補令三.md` 與來源逐位同（停機款 `2⁗`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-388 補令三 工項零⁗：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-388-k961s3`（快轉）。

### 工項一⁗　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零⁗ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-388-k961s3` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `fd88f64793a373ab921999fbe5b325c44f0c2a4c`。
2. `git merge-base --is-ancestor fd88f64793a373ab921999fbe5b325c44f0c2a4c <C>` ⇒ `rc 0`；`git rev-list --count fd88f64..<C>` ＝ `9`；`git rev-list --count <C>..fd88f64` ＝ `0`；`git rev-list --merges fd88f64..<C>` ＝ 空。
3. `git rev-list fd88f64..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `8fd9f8a1d3879181f04435f9f7e49201522e89eb`（命中 `1` 列 `app.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `3f023996da947e45db08740313921c78f2f9e265`；`git diff --name-only 8fd9f8a1d3879181f04435f9f7e49201522e89eb <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3⁗`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4⁗`）；⛔ 刪側支 `verify/W-G.9-388-k961s3`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads ＝ **`48`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `8fd9f8a` 之相異 ＝ **`0`**；判別力［必非零］：vs `fd88f64` 之相異 ＝ **`1`**（`app.py`）；④ `git branch -r --contains 8fd9f8a1d3879181f04435f9f7e49201522e89eb` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-388-k961s3`）。

---

## `§三-1⁗`　收工閘（工項一⁗ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗` | 工項零⁗ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（``116``）／`0`·唯此一檔；首列 ＝ `§三⁗` 所令逐字 |
| `2⁗` | `git -c core.quotepath=false diff --name-status 906a8ff HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-388_補令三.md`；生產碼與 `verify/` 之一切檔對 `906a8ff` 相異 **`0`**；判別力［必非零］：生產碼對 `fd88f64` 相異 **`1`**（`app.py`）、`verify/` 對 `fd88f64` 相異 **`6`**（`M` `5`·`A` `1`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` | 對 `906a8ff` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `a3f9d47a34edcb4942a03561c4fa6cd610e8d729`；自誤簿 ＝ `fb55b127c8121ad98924965dab70ca5b55372738`；`docs/待落地清單.md` ＝ `76bc7135a0cf59a9f1a5103cf1db0982184168c0`） |
| `5⁗` | 自限 | 遠端 heads **`48`**；主線 ＝ `<C>`；側支 `verify/W-G.9-388-k961s3` ＝ `<C>`；其餘 `46` 列中除 `ops/queue`（回報後可變）外之 `45` 列逐列 ＝ `<O>/heads_before_388p3.txt` 之同列 |
| `6⁗` | `python3 verify/probes/probe_WG9270_closegate.py 629 623 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 630 629 .` ⇒ `rc 7` |
| `7⁗` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 629 623` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零⁗` 項 `3` 之值（⛔ 變） |
| `8⁗` | 量測器（於主線之端·`15` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`… wiring <repo> fd88f64` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`35／35`（`F16`）、`74／74`（`F29`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`）；`F32 selftest` `K1`〜`K31`、`F32 wiring` `X1`〜`X5` 皆 ✅ |

---

## `§四⁗`　土地後果

**本案**：配地⛔ 變（`§一⁗` 項 `2`·`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔逐位同、`parity` 不符 `0`）。**他案**：主線自此，段三後處理（街角合併再試後，同一合併群之未能併出之土地之去處）：① 某街廓之承受之宗 ＝ 該群於該街廓之受併宗（左右兩端可二）∪ 依原位次配得而保留之宗；二以上 ⇒ 與所承受之片相鄰者先 → 應分配面積大 → 重劃前面積大 → 暫編地號小；② 分不到之建地所鄰之已配得街廓二以上 ⇒ 本街廓先，否則承受之宗之應分配面積較大之一側；③ 所鄰為零 ⇒ 本街廓有同一地主之已配得之宗者依第 `5` 項之輪（本街廓之候選之間 ＝ 應分配面積大者先·`K-9-73` ①），否則經與之共邊之同群之道路片（⛔ 已併出·⛔ 穿越）之遠半臨另一側之已配得街廓者向該側併（隨其道路片之受者·手冊道路用地分配原則第 `2` 點），其「另一側」扣該道路片之近半亦臨之街廓（路衝街廓·`K-9-63` ⑩·以道路片為單位），仍為零 ⇒ 第 `5` 項之輪；④ 以上之四停機（二受併宗、承受之宗未定、B 內保留建築片、所鄰 ≠ 1）去之，受併宗於試算未保留之停機改以逐受併宗判。路口片之按面積平分（`K-9-59` ④）仍照舊停機（待落地之序 `9`）。

---

## `§五⁗`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `906a8ff` 之追蹤檔 `2892` 檔·`git grep -l -F`） | `W-G.9-388_補令三` ＝ `0` 檔 ⇒ 可取（`ops/queue` 之全部 `*.md` 亦 `0`·發單端實查） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（態 `906a8ff`·定稿之前一版·其後唯本列與項 `4` 之文字之填）：🔴 機械 `0` 項／🟡 提示 `0` 項／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23421`–`31163`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `906a8ff`（雲端 Linux·⛔ `push`）＋ 本補令之定稿·一 `commit`（首列 ＝ 所令逐字）：工項零⁗ 之 blob ＝ 來源；工項一⁗ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `9`·反向 `0`·`--merges` 空·命中唯 `8fd9f8a`·`app.py` 之 blob ＝ `3f023996…`·對 `8fd9f8a` 相異空）；閘 `1⁗` ＝ 本補令 `116`／`0`·唯此一檔；閘 `2⁗` 恰一 `A`·生產碼與 `verify/` 對 `906a8ff` 相異 `0`、生產碼對 `fd88f64` 恰 `app.py`、`verify/` 對 `fd88f64` `6`（`M` `5`·`A` `1`）·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`）；閘 `3⁗` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4⁗` 相異 `0`·四 blob ＝ 期；閘 `6⁗` `✅ 二閘皆過`·`630 629` ⇒ `rc 7`；閘 `7⁗` `rc 0`·四簿 ＝ `§零⁗` 項 `3`；閘 `8⁗` 十五呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B·`P0` ＝ 期；工項一⁗ 之快轉、出艙 ①②④ 與閘 `5⁗` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空 |

SELF_SHA256: 85607ee4357f5f2287b5dbd1ce1f42454ea39bbcb7005030f06bf2bb21260623
