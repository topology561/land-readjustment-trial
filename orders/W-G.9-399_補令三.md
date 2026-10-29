# `W-G.9-399` 補令三：本補令入側支 ＋ 主線快轉（`bd7da4d` → 本補令工項零⁗ 之 `commit`·`W-G.9-399`〔互相等待之二位地主之先後改以末端塊評選指數；臨端線之長之分配、端線之觸點、端線不可定之處置；臨端線之「臨」以該宗之土地判之〕入主線·**本案配地⛔ 變**）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-30`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-399_規格單.md`（「原單」）、`docs/orders/W-G.9-399_補令一.md`（「補令一」）與 `docs/orders/W-G.9-399_補令二.md`（「補令二」）之 `§四-2‴`（復驗皆符而本案之配地⛔ 變 ⇒ 入主線之短單）。三單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`；側支 `verify/W-G.9-399-k960x` ＝ `3a404b0343e20ef9823f9c3cb43806946f60df23`（補令二工項四‴）；遠端 heads（**排除出圖線之分支**·下之 🔑）＝ **`57`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `0c35403`；發單端已於拋棄式 worktree 自倉從頭重跑原單「項 `8` 之表」之施後 `97` 呼叫、前態 `9` 呼叫與收工閘〔`§一⁗` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring` 與滑池槽之測）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式（同原單）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。原單為新規格單而**本案之配地⛔ 變**（`§一⁗` 項 `2`）⇒ README 第二節停止條件 `2` ⛔ 成就 ⇒ 自動處理第 `1` 款（已有 KL 裁示之項：KL `2026-10-26 22:09`／`22:42`／`22:57`·`ops/queue` 之 `KL答覆/2026-10-26_2209.md`）。**`expects_allocation_change` ＝ `false`**（執行端之量得主線之生產碼與側支之 `0c35403` 有任何相異 ⇒ 停機款 `5⁗`）。
> 🔑 **遠端分支之閘之母體**（`發單端.md` 丙之 3·KL `2026-10-23 17:31` 立出圖線）：本補令之一切以 `git ls-remote --heads origin` 之列數或逐列之值為閘者，其母體一律 ＝ `git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"` 之出艙（排除出圖線之 `refs/heads/wip/plots` 與 `refs/heads/verify/W-P.*`·其由出圖線推送，與本補令無涉）；本補令所載之 heads 之數皆指此母體。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc〔倉外之輔助腳本與 `STATE.json` 之改亦以檔案之寫入為之〕；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零⁗ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-399_補令三.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。施工樹之根之複本以 `.git/info/exclude` 免於 `git status`（其式以 `/` 起首：`/W-G.9-399_補令三.md`）。
> 🔑 **撇號**：「⁗」（U+2057）＝ 補令三，唯指本補令之條；「‴」＝ 補令二；「″」＝ 補令一；無撇號者指原單之條。
> 🔑 **快轉前之記**（README 第二節「入主線之安全」）：主線之前值 → 後值，於**快轉之前**記於 `ops/queue` 之 `log.md`（增一列）與 `STATE.json` 之 `history`（增一筆·`from` ＝ `to` ＝ `running`）⇒ `commit`（首列 `ops: 執行端快轉前之記 W-G.9-399_補令三`）、推送 `ops/queue`（被拒 ⇒ `pull --rebase` 重取再推·⛔ `--force`）；推成之後方快轉（`§三⁗` 工項一⁗）。回報之列再記快轉後之實值。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字（含 `verify/baselines/`）、`tests/`、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-399-k960x` 之刪除或改寫（保留為歷史）；任何他側支（含出圖線之 `wip/plots`、`verify/W-P.*`）；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；`K-9-60` ②（`W-G.9-396`）、待落地序 `48`〜`52`——另單。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零⁗`　開場（**先於工項零⁗**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`；`git rev-parse origin/verify/W-G.9-399-k960x` ＝ `3a404b0343e20ef9823f9c3cb43806946f60df23`；`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"` 之列數 ＝ **`57`**（其全列存 `<O>/heads_before_399p3.txt`·收工閘 `5⁗` 用；另存未濾之全列 `<O>/heads_all_before_399p3.txt` 供記）；施工樹 `git checkout --detach origin/verify/W-G.9-399-k960x` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 646 645` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `631`／`MAX` `646`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `3a404b0` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝後之釘回同原單 `§零-0` 項 `5`〔七釘、`tzdata` 之去、`narwhals==2.27.1`、`fonttools==4.67.0`〕）；`python3 -m pip freeze` 之 `sha256` 入回報（期 ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`·異者照實記之·⛔ 停機）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五⁗` 項 `3`）。

### `§零-1⁗`　停機款

| # | 款 |
|---|---|
| `1⁗` | 開工時主線 ≠ `bd7da4d`，或側支 ≠ `3a404b0`，或遠端 heads（濾後）≠ `57`，或施工樹之追蹤檔有變動，或 `§零⁗` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2⁗` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗` | 工項一⁗ 前置之任一期不符；或快轉前之記（單首 🔑）之推送不能成 |
| `4⁗` | 工項一⁗ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5⁗` | 工項一⁗ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗` | 工項零⁗ 之 `push` 之目標非 `verify/W-G.9-399-k960x`；工項一⁗ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零⁗ 之 `commit`；或推至他支 |
| `7⁗` | `§三-1⁗` 收工閘任一 ≠ 期 |
| `8⁗` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9⁗` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一⁗ 未成者主線⛔ 動（快轉前之記已推者，於回報中記「未快轉」）。

---

## `§一⁗`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-399-k960x` 對主線 `bd7da4d` 唯九筆 `commit`（`git rev-list --count bd7da4d..3a404b0` ＝ `9`、反向 ＝ `0`、`--merges` 空）：原單工項零 `6b159e2`（原單）、一 `23f3fc8`（`16` 器）；補令一工項零″ `31887d9`（補令一）、一″ `1612750`（`F42`）；補令二工項零‴ `bfdba99`（補令二）、一‴ `9e0eeb1`（`F42`）、二‴ `0c35403`（生產碼 `app.py`·blob `101a7a6a860522dd24b460e54aa8af48de84badd`〔對 `9e0eeb1` `+373`／`−14`〕）、三‴ `4c77eee`（`K-6` 典、`docs/待落地清單.md`、自誤簿）、四‴ `3a404b0`（報告二檔）。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰一筆：`0c35403cf144cff9627e80c9309d94fb2f169a17`（`1` 列：`app.py`）；`git diff --name-only 0c35403 3a404b0 -- app.py ":(glob)verify/*.py" verify/ tests/` ＝ 空。
2. **發單端之獨立復驗**（`2026-10-30`·雲端 Linux `4` 核·倉外之拋棄式 worktree〔施後 ＝ `0c35403`、前態 ＝ 補令二工項一‴ 之端 `9e0eeb1`〔生產碼 ＝ `bd7da4d`〕〕·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報·`ops/queue` 之 `log.md` 之發單端之復驗之列·下之數之來源：發單端於拋棄式 worktree 之實跑）：補令一之原趟之差異（`ops/queue` 之 `reports/W-G.9-399_補令一_回報_app.diff`·`16c561ff…`）施於 `9e0eeb1` ⇒ `app.py` `1158f83e…`；其對 `0c35403` 之 `app.py` 之差異唯三 hunk、皆在 `end_block_pick`（`ast` 頂層節點之相異 ＝ `{end_block_pick}`），逐行讀合補令二 `R-1‴`、`R-2‴`（多邊形之部之取、開運算 `1e-05 m` 斜接、切點取多邊形之部之頂點、歸屬之判用開運算之形、字樣 `` `W-G.9-399` 補令二 ‴ `` `2` 處）；`git diff bd7da4d 0c35403 -- app.py` ＝ 倉內 `W-G.9-399R_末端塊評選指數之互相等待之先後_差異.diff` 逐位同；三簿皆純末端追加且其尾 ＝ 塊依序（`K48`＋`K49`＋`K50`、`P59`＋`P60`＋`P61`、`E46`＋`E47`·blob ＝ `§三-1⁗` 閘 `4⁗`）；原單「項 `8` 之表」之施後 `97` 呼叫（`0c35403`·期 ＝ 補令二 `§五‴` 項 `8`）＋ 前態 `9` 呼叫（`9e0eeb1`·`#56`〜`#61` 與對照 `#95`〜`#97`〔紅如期：`#95` `rc 1`·其末列 ＝ 補令二之表之工項一‴ 之端之列；`#96` `⇒ 紅 ['W1', 'W2', 'W3', 'W4']；rc 1`；`#97` `⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`〕）之 `rc`／末列皆合期（不符 `0`／`106`）、`stderr` 合計 `0` B（施後之耗時之和 `25429` s·並行 `2`）；`F42 selftest` `P0 判式自驗 79／79`、`F42 wiring` `W1`〜`W6` ✅、`F42 run` 二退縮 `R1`〜`R3` ✅（端線 `R2` 右 `44.12`、`R3` 左 `43.91`、`R5` 右 `47.95`、`R6` 左 `47.71` m；當選 ＝ 主線；合併再試之標的 `[]`）；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`；`F36 diff`（前態 → 施後）二退縮皆 `全比相異 0 項`（對照組 `k6s3_pre_35` 對 `k6s3_pre_00` ⇒ `全比相異 43 項`）；`k6s3 cmp` 二退縮 `rc 0`·`相異 0 項 ⇒ ✅ 同`；`F8` 之落檔前後逐位同（3.5 m `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、0 m `186b090b68836f0ece2c0d23dad5573941995bf5`·＝ 基準）；`parity` 二退縮之落檔與 `stdout` 以同一字樣代 `HEAD` 後逐位同（⛔ 代則異）；發單端自撰之獨立之測（倉外·`F42` 之外·`end_block_apply` 之直呼·長 `40` 深 `30` 之街廓之左端·分割 `2`〜`4` 宗〔斜切〕·其一宗附寬 `0.002`〜`0.015 mm` 之 L 形之刺或沿端線之零寬之折返）：座標系之不變性（本地 vs TWD97 之旋轉 `0`〜`360°`·鏡射 `50%`）`2000` 例——`0c35403` 各列之臨端線之差逾 `0.01 m` 者 `0`、諸列之和逾端線者 `0`；刺與折返之有無之對照（同一分割去其刺、折返·二座標系各一·`1518` 比）——`0c35403` 異者 `0`（最大 `0.01`·取位）、補令一之原趟之碼（`1158f83e`）異者 `1006`（最大 `5.0 m`）；收工閘 `1‴`〜`4‴`、`6‴`〜`8‴` 皆合（`closegate 646 645` `rc 0`·對照 `647 646` `rc 7`；anchor 自誤 `631`／`646`、`GB` `199`／`207`、`VR` `80`／`95`、`K-9` `77`／`80`·缺號皆同；`checkidx` `索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` `則 124；加註節 14；列 158`·重生成之檔逐位同；`--selftest` `rc 0`；`CR` `0`／`25` 檔·對照 `12308`；新檔六之 `check-ignore` 皆 `rc 1`）；閘 `5‴`：濾後 `57`、主線 `bd7da4d`、側支 `3a404b0`（祖含 `1612750`）。
3. **快轉之受詞**：工項零⁗ 推後之側支之端（工項零⁗ 之 `commit`）；其祖含 `bd7da4d` 與 `3a404b0`；`bd7da4d..<工項零⁗>` 之 `commit` 數 ＝ `10`、`--merges` 空；生產碼之命中唯 `0c35403`（項 `1`）。

---

## `§二⁗`　射程

🛑 `(a)` 工項零⁗（零生產碼）推至側支 `verify/W-G.9-399-k960x`（快轉）；`(b)` 快轉前之記（單首 🔑）推至 `ops/queue`；`(c)` 工項一⁗ 主線快轉至工項零⁗ 之 `commit`（**以前置皆符、快轉前之記已推為條件**·⛔ `--force`）；`(d)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434` → `<工項零⁗ 之全 40 碼>`」（快轉後之實值）；`(e)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(f)` ⛔ 及生產碼、`verify/`（含基線）、`tests/`、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(g)` 執行報告⛔ 另立（原單之報告已由補令二入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三⁗`　工項（依序）

### 工項零⁗　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-399_補令三.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-399_補令三.md` 與來源逐位同（停機款 `2⁗`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-399 補令三 工項零⁗：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-399-k960x`（快轉）。

### 工項一⁗　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零⁗ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-399-k960x` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`。
2. `git merge-base --is-ancestor bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434 <C>` ⇒ `rc 0`；`git rev-list --count bd7da4d..<C>` ＝ `10`；`git rev-list --count <C>..bd7da4d` ＝ `0`；`git rev-list --merges bd7da4d..<C>` ＝ 空。
3. `git rev-list bd7da4d..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `0c35403cf144cff9627e80c9309d94fb2f169a17`（命中 `1` 列：`app.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `101a7a6a860522dd24b460e54aa8af48de84badd`；`git rev-parse <C>:verify/stepg_pipeline.py` ＝ `c9d347c28d41d8a9d59ce3367748e9ae783430ee`（⛔ 變）；`git diff --name-only 0c35403cf144cff9627e80c9309d94fb2f169a17 <C> -- app.py ":(glob)verify/*.py" verify/ tests/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3⁗`·⛔ 快轉。

**快轉前之記**（前置皆符後·單首 🔑）：`ops/queue` 之 `log.md` 增一列、`STATE.json` 之 `history` 增一筆，皆記「主線 `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434` → `<C>`（將快轉）」⇒ `commit`、推送 `ops/queue`。推成之後方行下款。

**快轉**（與前置、快轉前之記為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4⁗`）；⛔ 刪側支 `verify/W-G.9-399-k960x`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads（濾後·單首 🔑）＝ **`57`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `0c35403` 之相異 ＝ **`0`**；判別力［必非零］：vs `bd7da4d` 之相異 ＝ **`1`**（`app.py`）；④ `git branch -r --contains 0c35403cf144cff9627e80c9309d94fb2f169a17` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-399-k960x`）。

---

## `§三-1⁗`　收工閘（工項一⁗ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗` | 工項零⁗ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（`116`）／`0`·唯此一檔；首列 ＝ `§三⁗` 所令逐字 |
| `2⁗` | `git -c core.quotepath=false diff --name-status 3a404b0 HEAD`；生產碼 `34` 檔、`verify/`、`tests/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-399_補令三.md`；生產碼、`verify/`、`tests/` 之一切檔對 `3a404b0` 相異 **`0`**；判別力［必非零］：生產碼對 `bd7da4d` 相異 **`1`**（`app.py`）、`verify/` 對 `bd7da4d` 相異 **`16`**（`M` `15`·`A` `1`）；`tests/` 對 `bd7da4d` 相異 **`0`**（本批⛔ 動之）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md`、`verify/baselines/` | 對 `3a404b0` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `38571c5af27da6062a06d631bbf0263eae8ba35c`；自誤簿 ＝ `5166afa5da77ea018d964536b764fa3755c8e93e`；`GB` 簿〔`docs/reports/W-G.4_泛用阻塞項登記表.md`〕＝ `2a07e78d81c65d9144fe80316e66965aa45f5022`；`docs/待落地清單.md` ＝ `c2b98093b93e889b2a23845d5d411868a53640bb`） |
| `5⁗` | 自限（母體 ＝ 單首 🔑 之濾後之列） | 遠端 heads **`57`**；主線 ＝ `<C>`；側支 `verify/W-G.9-399-k960x` ＝ `<C>`；其餘 `55` 列中除 `ops/queue`（回報後可變）外之 `54` 列逐列 ＝ `<O>/heads_before_399p3.txt` 之同列 |
| `6⁗` | `python3 verify/probes/probe_WG9270_closegate.py 646 645 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 647 646 .` ⇒ `rc 7` |
| `7⁗` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 646 645` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零⁗` 項 `3` 之值（⛔ 變） |
| `8⁗` | 量測器（於主線之端·`41` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`；`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>`；`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`；`python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302`；`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`；`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`；`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`；`python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd`；`python3 verify/probes/probe_WG9352_endblock.py selftest <repo>`；`python3 verify/probes/probe_WG9352_endblock.py wiring <repo>`；`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`；`python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415`；`python3 verify/probes/probe_WG9394_k9615.py selftest <repo>`；`python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283`；`python3 verify/probes/probe_WG9395_k960.py selftest <repo>`；`python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4`；`python3 verify/probes/probe_WG9398_rw25.py selftest <repo>`；`python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf`；`python3 verify/probes/probe_WG9399_k960x.py selftest <repo>`；`python3 verify/probes/probe_WG9399_k960x.py wiring <repo> bd7da4d`；`python3 tests/test_pool_slot.py`；`python3 verify/probes/probe_order_preflight.py --selftest` | 前 `39` 呼叫皆 **`rc 0`**、末列皆逐字 `⇒ 紅 []；rc 0`；`python3 tests/test_pool_slot.py` ⇒ **`rc 0`**、末列逐字 `✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`；末之 `--selftest` ⇒ **`rc 0`**、末列逐字 `判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`probe_WG9363_k953.py selftest`）、`74／74`（`probe_WG9375_k965.py selftest`）、`35／35`（`probe_WG9357_k948.py selftest`）、`31／31`（`probe_WG9373_k966.py selftest`、`probe_WG9388_k961s3.py selftest`）、`29／29`（`probe_WG9373p1_partrem.py selftest`）、`16／16`（`probe_WG9389_trialstop.py selftest`、`probe_WG9398_rw25.py selftest`）、`14／14`（`probe_WG9390_k961r.py selftest`）、`22／22`（`probe_WG9391_k980x.py selftest`）、`17／17`（`probe_WG9392_k980g.py selftest`）、`79／79`（`probe_WG9399_k960x.py selftest`） |

---

## `§四⁗`　土地後果

**本案**：主線之配地⛔ 變（`§一⁗` 項 `2`：`F36 diff`／`k6s3 cmp` 二退縮皆相異 `0` 項、`F8` 之落檔前後逐位同、`parity` 同；本案之互相等待⛔ 發生）——本案之四個末端（`R2` 右、`R3` 左、`R5` 右、`R6` 左）之評選之紀錄增「端線(m)」「臨端線(m)」「評選指數」三欄（端線 `44.12`／`43.91`／`47.95`／`47.71` m·兩退縮同），其當選者與主線同。**他案**：主線自此，① 二位地主互相等待（各待對方之末端塊之結果）時，其先後改依**末端塊評選指數**（端線之長之比 `0.4` ＋ 跨占範圍面積之比 `0.6`·⛔ 計正面道路·分母為該末端塊範圍；唯計二人共同跨占之端），先後之序照街角 `K-9-28`（有第 `1` 名者先〔第 `1` 名之端多者先；再 重劃前面積大；再 指數之和大；再 暫編地號小〕；皆無第 `1` 名者名次之和小者先〔再 同上之序〕）；三位以上輪流互等者兩兩比較，兩兩皆先者先，成圈或某二位無共同之端者依應分配面積大 → 重劃前面積大 → 暫編地號小（KL `2026-10-26 22:09`／`22:42`／`22:57`·原單塊 `K48` 之三之丁、戊）；② 臨端線之長，每一小段唯歸原位次最先之一宗（各宗之和不逾端線之長）；③ BASELINE 微偏（`2°` 以內）者，沿之而行之外框之二端視為觸及；④ 端線量不出者，該端之評選指數為空並記其誤，唯真有互相等待時方停機；⑤ 臨端線之「臨」以該宗之土地判之——地籍圖上零寬之折返、寬不及 `0.02 mm` 之刺⛔ 計（同一地籍於旋轉、平移、鏡射之座標之量相同）。

---

## `§五⁗`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `3a404b0` 之追蹤檔 `2951` 檔·`git grep -l -F`） | `W-G.9-399_補令三`、`W-G.9-399 補令三` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之 `*.md` 唯 `交接.md` 之預記 `1` 檔·其為發單端之接續之記、⛔ 占號）；對照［必非零］`W-G.9-399_補令二` ⇒ `2` 檔 |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`（`3a404b0` 之器）·發單端實跑（受詞 ＝ 本補令之定稿之前一版·其後唯本列與項 `4` 之文字與末列之填·其列號⛔ 移）：🔴 機械 `0` 項／🟡 提示 `1` 項——具名豁免：`P-7` `:91`（閘 `2⁗` 之以 `3a404b0` 與 `HEAD` 為二端之差異——其區間**有意**含工項零⁗ 之單之入倉之一筆，其期即「恰 `1` 列：`A`␉`docs/orders/W-G.9-399_補令三.md`」·`W-G.9-398` 補令三之同形）／ℹ️ 記錄 `2` 項（`P-5` ✅；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `24403`–`32147`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `3a404b0`（雲端 Linux·⛔ `push`）＋ 本補令之定稿之前一版·一 `commit`（首列 ＝ 所令逐字）：工項零⁗ 之 blob ＝ 來源、`git status --porcelain` 空；工項一⁗ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `10`·反向 `0`·`--merges` 空·命中唯 `0c35403`〔`1` 列：`app.py`〕·`app.py`／`verify/stepg_pipeline.py` 之 blob ＝ `101a7a6a…`／`c9d347c2…`·對 `0c35403` 相異空）；閘 `1⁗` ＝ 本補令 `116`／`0`·唯此一檔·首列 ＝ 所令；閘 `2⁗` 恰一 `A`·生產碼、`verify/`、`tests/` 對 `3a404b0` 相異 `0`、生產碼對 `bd7da4d` 恰 `1`、`verify/` 對 `bd7da4d` `16`（`M` `15`·`A` `1`）、`tests/` 對 `bd7da4d` `0`·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`）·`git ls-files ':(glob)verify/*.py'` `33` 檔；閘 `3⁗` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4⁗` 相異 `0`（`CLAUDE.md` ＝ `00e627af…`）；閘 `6⁗` `✅ 二閘皆過`·`647 646` ⇒ `rc 7`；閘 `7⁗` `rc 0`·四簿 ＝ `§零⁗` 項 `3`；閘 `8⁗` 四十一呼叫（於模擬之 `<C>`）皆 `rc 0`·末列皆合期·`stderr` `0` B·`P0` ＝ 期（耗時之和 `1032` s·並行 `2`·環境 `pip freeze` `ae1438da…`）；結束時 `git status --porcelain` 空；快轉前之記、工項一⁗ 之快轉、出艙 ①②④ 與閘 `5⁗` 須遠端·⛔ 模擬 |

SELF_SHA256: 1dcd70491df91a5e256a558c0838fa611c0c50d1ec33c59f59f43782ee42c21f
