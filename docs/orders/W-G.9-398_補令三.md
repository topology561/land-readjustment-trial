# `W-G.9-398` 補令三：本補令入側支 ＋ 主線快轉（`20e03bf` → 本補令工項零⁗ 之 `commit`·`W-G.9-398`〔街角地側面道路負擔百分率改照手冊附表 25；寬度先四捨五入至公釐再內插、清冊之寬度記至公釐；地界線恰落於半公釐之跳處者取較接近者〕入主線·**本案配地之改變 ＝ KL 所核之請示表「戊」欄**）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-28`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-398_規格單.md`（「原單」）、`docs/orders/W-G.9-398_補令一.md`（「補令一」）之 `§四-2″` 與 `docs/orders/W-G.9-398_補令二.md`（「補令二」）之 `§四-2‴`（復驗皆符而本案之配地之改變 ＝ 補令一 `§一″` 項 `5`〔＝ 請示表戊欄〕⇒ 入主線之短單）。三單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`；側支 `verify/W-G.9-398-rw25` ＝ `0534828f62f02b1af4e1d309d637056179a9d5bd`（補令一工項四″）；遠端 heads（**排除出圖線之分支**·下之 🔑）＝ **`56`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `7c819b5`；發單端已於拋棄式 worktree 自倉從頭重跑原單「項 `8` 之表」之施後 `94` 呼叫、前態 `6`〔＋ 對照 `5`〕` 呼叫與收工閘〔`§一⁗` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring` 與滑池槽之測）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式（同原單）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。原單為新規格單而改本案之配地 ⇒ README 第二節停止條件 `2` 已成就、發單端已請示（`ops/queue` 之 `待KL/2026-10-27_側面道路負擔附表25之成果請核.md`、`待KL/2026-10-27_寬度先取至公分後界線落於半公分處之處置.md`、`待KL/2026-10-28_寬度記至公釐之本案結果與半公釐跳處之取法.md`）；**KL `2026-10-28 10:48` 之答（逐字·`ops/queue` 之 `KL答覆/2026-10-28_1048.md`）：「1. 第一問：是 2. 第2問：甲 3. 同意另陳之累積百分率列法」**——其第一問逐字（發單端之請示·⚠️ 非 KL 之語）：「本案依「戊」之結果（上表「戊」欄·與「乙」欄 11 處各差 0.01 ㎡、抵費地同「乙」）可否併入正式版本？」⇒ 本補令 ＝ 該核可之執行。**`expects_allocation_change` ＝ `true`**（主線之配地之改變 ＝ 請示表戊欄·KL 所核·本補令⛔ 增減）。
> 🔑 **遠端分支之閘之母體**（`發單端.md` 丙之 3·KL `2026-10-23 17:31` 立出圖線）：本補令之一切以 `git ls-remote --heads origin` 之列數或逐列之值為閘者，其母體一律 ＝ `git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"` 之出艙（排除出圖線之 `refs/heads/wip/plots` 與 `refs/heads/verify/W-P.*`·其由出圖線推送，與本補令無涉）；本補令所載之 heads 之數皆指此母體。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc〔倉外之輔助腳本亦以檔案之寫入為之〕；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零⁗ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-398_補令三.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。施工樹之根之複本以 `.git/info/exclude` 免於 `git status`（其式以 `/` 起首：`/W-G.9-398_補令三.md`）。
> 🔑 **撇號**：「⁗」（U+2057）＝ 補令三，唯指本補令之條；「‴」＝ 補令二；「″」＝ 補令一；無撇號者指原單之條。
> 🔑 **快轉前之記**（README 第二節「入主線之安全」）：主線之前值 → 後值，於**快轉之前**記於 `ops/queue` 之 `log.md`（增一列）與 `STATE.json` 之 `history`（增一筆·`from` ＝ `to` ＝ `running`）⇒ `commit`（首列 `ops: 執行端快轉前之記 W-G.9-398_補令三`）、推送 `ops/queue`（被拒 ⇒ `pull --rebase` 重取再推·⛔ `--force`）；推成之後方快轉（`§三⁗` 工項一⁗）。回報之列再記快轉後之實值。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字（含 `verify/baselines/`）、`tests/`、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-398-rw25` 之刪除或改寫（保留為歷史）；任何他側支（含出圖線之 `wip/plots`、`verify/W-P.*`）；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零⁗`　開場（**先於工項零⁗**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`；`git rev-parse origin/verify/W-G.9-398-rw25` ＝ `0534828f62f02b1af4e1d309d637056179a9d5bd`；`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"` 之列數 ＝ **`56`**（其全列存 `<O>/heads_before_398p3.txt`·收工閘 `5⁗` 用；另存未濾之全列 `<O>/heads_all_before_398p3.txt` 供記）；施工樹 `git checkout --detach origin/verify/W-G.9-398-rw25` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 644 641` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `629`／`MAX` `644`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `0534828` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝後之釘回同補令一 `§零-0″` 項 `5`〔原單之七釘、`tzdata` 之去、`narwhals==2.27.1`、`fonttools==4.67.0`〕）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五⁗` 項 `3`）。

### `§零-1⁗`　停機款

| # | 款 |
|---|---|
| `1⁗` | 開工時主線 ≠ `20e03bf`，或側支 ≠ `0534828`，或遠端 heads（濾後）≠ `56`，或施工樹之追蹤檔有變動，或 `§零⁗` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2⁗` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗` | 工項一⁗ 前置之任一期不符；或快轉前之記（單首 🔑）之推送不能成 |
| `4⁗` | 工項一⁗ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5⁗` | 工項一⁗ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗` | 工項零⁗ 之 `push` 之目標非 `verify/W-G.9-398-rw25`；工項一⁗ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零⁗ 之 `commit`；或推至他支 |
| `7⁗` | `§三-1⁗` 收工閘任一 ≠ 期 |
| `8⁗` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9⁗` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一⁗ 未成者主線⛔ 動（快轉前之記已推者，於回報中記「未快轉」）。

---

## `§一⁗`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-398-rw25` 對主線 `20e03bf` 唯十一筆 `commit`（`git rev-list --count 20e03bf..0534828` ＝ `11`、反向 ＝ `0`、`--merges` 空）：原單工項零 `96c06e9`（原單）、一 `07d1202`（`17` 檔）、二 `c35d32a`（生產碼 `app.py`）、三 `0dad1a00`（`K-6` 典、`docs/待落地清單.md`）、四 `f748370`（報告二檔）；補令一工項零″ `ce6912d`（補令一）、一″ `8bc2add`（塊 `Fy56` 之 `18` 檔）；補令二工項零‴ `d3b6a7e`（補令二）；補令一工項二″ `7c819b5`（生產碼：`app.py` blob `ca9f917e15a036922889783bff1b1049edb388f6`〔對 `f748370` `+78`／`−12`〕、`verify/stepg_pipeline.py` blob `c9d347c28d41d8a9d59ce3367748e9ae783430ee`〔`+1`／`−1`〕）、三″ `c112df1`（`K-6` 典、自誤簿、`docs/待落地清單.md`）、四″ `0534828`（報告二檔）。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰二筆：`c35d32a3cd43da5bdcb1c197d16b5757a1b39861`（`1` 列：`app.py`）、`7c819b53038f14109693ce8c572a029f361e97e7`（`2` 列：`app.py`、`verify/stepg_pipeline.py`）；`git diff --name-only 7c819b5 0534828 -- app.py ":(glob)verify/*.py" verify/` ＝ 空。
2. **發單端之獨立復驗**（`2026-10-28`·雲端 Linux `4` 核·倉外之拋棄式 worktree〔施後 ＝ `0534828`、前態 ＝ 補令一工項一″ 之端 `8bc2add`〕·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報·`ops/queue` 之 `log.md` 之發單端之復驗之列·下之數之來源：發單端於拋棄式 worktree 之實跑）：生產碼之差異（`git diff f748370 7c819b5 -- app.py verify/stepg_pipeline.py`·`204` 列 ＝ 倉內 `W-G.9-398R1_寬度取至公釐與跳處_差異.diff` 逐位同）逐行讀合補令一 `R-1″`〜`R-7″`（AST：對 `f748370` 增 `{rw_width_mm, rw_pct_2dp}`、對 `20e03bf` 增 `{RW_TABLE_25, rw_width_mm, rw_pct_2dp}`·無減·相異之節點 ＝ 其增 ∪ `{rw_from_width, iterate_G_S, solve_G_binary, f3_screen_stepg_run, main}`；`stepg` 之差唯 `W(m)` 之一列）；三簿皆純末端追加且其尾 ＝ 塊依序（`K47`、`E44`＋`E45`、`P58`·blob ＝ `§三-1⁗` 閘 `4⁗`）；原單「項 `8` 之表」之施後 `94` 呼叫（`0534828`）＋ 前態 `6` 呼叫（`8bc2add`·`#56`〜`#61`）＋ 對照 `5` 呼叫（`8bc2add`·`#16`、`#80`、`#92`、`#93`、`#94` 紅如期）之 `rc`／末列皆合期、施後與前態之 `stderr` 合計 `0` B（耗時之和 `23584` s·並行 `2`）；`F41` 之 `T1`〜`T13`（含 `T2′`、`T7′`、`T9′`）與 `P0 16／16`、`X1`〜`X9` 皆 ✅；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`；`F36 diff`（前態 → 施後）＝ 補令一 `§一″` 項 `5` 逐字（3.5 m `3` 項、0 m `7` 項）；`k6s3 cmp` 二退縮 `rc 1`·`相異 1 項 ⇒ 🔴 異`（＝ 所載）；`F8` 之落檔 3.5 m `13c04b45…` → `4aca01db…`、0 m `f27849f5…` → `186b090b…`，逐欄之差 ＝ 補令一 `V-6″`（`3`／`7` 欄）；`parity` 二退縮之落檔與 `stdout` 以同一字樣代 `HEAD` 後逐位同（⛔ 代則唯 `/head` 異）；發單端自建之獨立模型：`rw_from_width` 對手冊附表 25 之 `Fraction` 模型（`W` 依十進位字面四捨五入至公釐）`93250` 點之最大差 `1.9e-14`、`rw_pct_2dp` 對精確十進位之四捨五入 `20000` 例不符 `0`；跳處之獨立之例（`45 × 18 m`·旋轉 `112°`·TWD97 之尺度·跳點 `9.9995 m`·左右二側·`t` ＝ `0.3`／`0.7`）：`jump398` ＝ `進`／`捨`、`W_far` ＝ `10.000`／`9.999`、`G` ＝ 期、次宗之 `W_rw_start_raw` ＝ 前宗 `W_far` 之公釐值、次宗之 `G` ＝ 獨立之不動點（`10`／`10` 合）；收工閘 `1″`〜`8″` 皆合（`closegate 644 641` `rc 0`·對照 `645 644` `rc 7`；anchor 自誤 `629`／`644`、`GB` `199`／`207`、`VR` `80`／`95`、`K-9` `77`／`80`；`checkidx` `索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` `則 124；加註節 14；列 158`·重生成之檔逐位同；`--selftest` `rc 0`）；閘 `5″`：濾後 `56`、主線 `20e03bf`、側支 `0534828`（祖含 `8bc2add`）、除 `ops/queue` 與側支外之 `54` 列之末筆皆早於本批（最晚 `2026-10-25`）。
3. **KL 之核可**：`2026-10-28 10:48`「1. 第一問：是 2. 第2問：甲 3. 同意另陳之累積百分率列法」（單首「授權」）；其第 `4` 點（無街角得標側之起算寬度之問）＝ 問而非裁（監看窗已答）⇒ 待落地序 `42`·⛔ 本補令之受詞。
4. **執行端之審查之二揭**（`ops/queue` 之 `reports/W-G.9-398_補令二_回報.md` 五；發單端之定·⛔ 涉土地後果）：`F-1`（跳處之判⛔ 有區間之寬之守門·以 `max_iter 4` 之合成例可誤判；生產碼之唯一之呼叫處之二分止於區間 ＜ `1e-9 m` ⇒ 現行之一切路徑不可達）與 `F-2`（負值之四捨五入遠離 `0`·唯及 `'W_near'` 之顯示與 `W₀` 之閘·`R(W ≤ 0) ＝ 0`）皆⛔ 改配地 ⇒ 依 `發單端.md` 丙之 2「其所揭⛔ 改配地、⛔ 違裁示者，記於 `交接.md` 留次單」，⛔ 阻本補令。
5. **快轉之受詞**：工項零⁗ 推後之側支之端（工項零⁗ 之 `commit`）；其祖含 `20e03bf` 與 `0534828`；`20e03bf..<工項零⁗>` 之 `commit` 數 ＝ `12`、`--merges` 空；生產碼之命中唯 `c35d32a`、`7c819b5`（項 `1`）。

---

## `§二⁗`　射程

🛑 `(a)` 工項零⁗（零生產碼）推至側支 `verify/W-G.9-398-rw25`（快轉）；`(b)` 快轉前之記（單首 🔑）推至 `ops/queue`；`(c)` 工項一⁗ 主線快轉至工項零⁗ 之 `commit`（**以前置皆符、快轉前之記已推為條件**·⛔ `--force`）；`(d)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f` → `<工項零⁗ 之全 40 碼>`」（快轉後之實值）；`(e)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(f)` ⛔ 及生產碼、`verify/`（含基線）、`tests/`、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(g)` 執行報告⛔ 另立（原單與補令一之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三⁗`　工項（依序）

### 工項零⁗　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-398_補令三.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-398_補令三.md` 與來源逐位同（停機款 `2⁗`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-398 補令三 工項零⁗：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-398-rw25`（快轉）。

### 工項一⁗　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零⁗ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-398-rw25` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`。
2. `git merge-base --is-ancestor 20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f <C>` ⇒ `rc 0`；`git rev-list --count 20e03bf..<C>` ＝ `12`；`git rev-list --count <C>..20e03bf` ＝ `0`；`git rev-list --merges 20e03bf..<C>` ＝ 空。
3. `git rev-list 20e03bf..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `2` 筆 ＝ `c35d32a3cd43da5bdcb1c197d16b5757a1b39861`（命中 `1` 列：`app.py`）與 `7c819b53038f14109693ce8c572a029f361e97e7`（命中 `2` 列：`app.py`、`verify/stepg_pipeline.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `ca9f917e15a036922889783bff1b1049edb388f6`；`git rev-parse <C>:verify/stepg_pipeline.py` ＝ `c9d347c28d41d8a9d59ce3367748e9ae783430ee`；`git diff --name-only 7c819b53038f14109693ce8c572a029f361e97e7 <C> -- app.py ":(glob)verify/*.py" verify/ tests/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3⁗`·⛔ 快轉。

**快轉前之記**（前置皆符後·單首 🔑）：`ops/queue` 之 `log.md` 增一列、`STATE.json` 之 `history` 增一筆，皆記「主線 `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f` → `<C>`（將快轉）」⇒ `commit`、推送 `ops/queue`。推成之後方行下款。

**快轉**（與前置、快轉前之記為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4⁗`）；⛔ 刪側支 `verify/W-G.9-398-rw25`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads（濾後·單首 🔑）＝ **`56`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `7c819b5` 之相異 ＝ **`0`**；判別力［必非零］：vs `20e03bf` 之相異 ＝ **`2`**（`app.py`、`verify/stepg_pipeline.py`）；④ `git branch -r --contains 7c819b53038f14109693ce8c572a029f361e97e7` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-398-rw25`）。

---

## `§三-1⁗`　收工閘（工項一⁗ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗` | 工項零⁗ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（`118`）／`0`·唯此一檔；首列 ＝ `§三⁗` 所令逐字 |
| `2⁗` | `git -c core.quotepath=false diff --name-status 0534828 HEAD`；生產碼 `34` 檔、`verify/`、`tests/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-398_補令三.md`；生產碼、`verify/`、`tests/` 之一切檔對 `0534828` 相異 **`0`**；判別力［必非零］：生產碼對 `20e03bf` 相異 **`2`**（`app.py`、`verify/stepg_pipeline.py`）、`verify/` 對 `20e03bf` 相異 **`18`**（`M` `17`·`A` `1`）、`tests/` 對 `20e03bf` 相異 **`1`**（`M`：`tests/test_pool_slot.py`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md`、`verify/baselines/` | 對 `0534828` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `78a2cdee2224c1bb2ac24fe7d7afb375345c770f`；自誤簿 ＝ `98815489490f87a32c1989dbf8e706d74c34f7dc`；`GB` 簿〔`docs/reports/W-G.4_泛用阻塞項登記表.md`〕＝ `2a07e78d81c65d9144fe80316e66965aa45f5022`；`docs/待落地清單.md` ＝ `cd213761710396c688fcbb306f4bedc0b173f708`） |
| `5⁗` | 自限（母體 ＝ 單首 🔑 之濾後之列） | 遠端 heads **`56`**；主線 ＝ `<C>`；側支 `verify/W-G.9-398-rw25` ＝ `<C>`；其餘 `54` 列中除 `ops/queue`（回報後可變）外之 `53` 列逐列 ＝ `<O>/heads_before_398p3.txt` 之同列 |
| `6⁗` | `python3 verify/probes/probe_WG9270_closegate.py 644 641 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 645 644 .` ⇒ `rc 7` |
| `7⁗` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 644 641` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零⁗` 項 `3` 之值（⛔ 變） |
| `8⁗` | 量測器（於主線之端·`39` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`；`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>`；`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`；`python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302`；`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`；`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`；`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`；`python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd`；`python3 verify/probes/probe_WG9352_endblock.py selftest <repo>`；`python3 verify/probes/probe_WG9352_endblock.py wiring <repo>`；`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`；`python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415`；`python3 verify/probes/probe_WG9394_k9615.py selftest <repo>`；`python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283`；`python3 verify/probes/probe_WG9395_k960.py selftest <repo>`；`python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4`；`python3 verify/probes/probe_WG9398_rw25.py selftest <repo>`；`python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf`；`python3 tests/test_pool_slot.py`；`python3 verify/probes/probe_order_preflight.py --selftest` | 前 `37` 呼叫皆 **`rc 0`**、末列皆逐字 `⇒ 紅 []；rc 0`；`python3 tests/test_pool_slot.py` ⇒ **`rc 0`**、末列逐字 `✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`；末之 `--selftest` ⇒ **`rc 0`**、末列逐字 `判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`probe_WG9363_k953.py selftest`）、`74／74`（`probe_WG9375_k965.py selftest`）、`35／35`（`probe_WG9357_k948.py selftest`）、`31／31`（`probe_WG9373_k966.py selftest`、`probe_WG9388_k961s3.py selftest`）、`29／29`（`probe_WG9373p1_partrem.py selftest`）、`16／16`（`probe_WG9389_trialstop.py selftest`、`probe_WG9398_rw25.py selftest`）、`14／14`（`probe_WG9390_k961r.py selftest`）、`22／22`（`probe_WG9391_k980x.py selftest`）、`17／17`（`probe_WG9392_k980g.py selftest`） |

---

## `§四⁗`　土地後果

**本案**：主線之配地自此改變 ＝ 請示表戊欄（KL `10:48` 所核·本補令⛔ 增減·發單端之實測 ＝ `§一⁗` 項 `2`）——**退縮 3.5 m**（對主線 `20e03bf`·`6` 項）：宗 `R1`·`628(5)`（右·街角第 1 宗）之應分配面積 `376.12` → `376.11 ㎡`、`R2`·`628-41(1)`（左·街角第 1 宗）`313.51` → `313.50`、`R2`·`628-40(1)` `359.59` → `359.60`、`R2`·`628-39(1)` `289.43` → `289.42`、`R5`·`628-45(1)`（左·街角第 1 宗）`525.28` → `525.27`；抵費地 `R1-抵費地-1` `851.69` → `851.70 ㎡`；**退縮 0 m**（`10` 項）：宗 `R1`·`628(5)` `376.12` → `376.11`、`R1`·`628-37(1)`（左·街角第 1 宗）`272.83` → `272.82`、`R2`·`628-41(1)` `313.51` → `313.50`、`R2`·`628-40(1)` `359.59` → `359.60`、`R2`·`628-39(1)` `289.43` → `289.42`、`R3`·`628-45(2)`（右·街角第 1 宗）`343.46` → `343.45`、`R3`·`628-30(3)` `562.01` → `562.02`、`R5`·`628-20(2)` `534.47` → `534.49 ㎡`；抵費地 `R1-抵費地-1` `851.69` → `851.70`、`R5-抵費地` `1221.46` → `1221.45 ㎡`（＝ 請示表「戊」對「現行」之全部：3.5 m `5` 宗、0 m `8` 宗與抵費地；`F36 diff` 之二落檔：主線 `20e03bf` 與側支 `0534828` 之 `k6s3 run`·發單端實跑）；他之宗之地號、地主、宗序、推進之側、街角之得標、強制抵費地、剔除皆⛔ 變。**他案**：主線自此，① 街角地之側面道路負擔百分率依手冊附表 25（每 `0.1 m` 一格·其間線性內插·`W ≥ 18 m` 為 `100`·`0 ＜ W ＜ 1 m` 自 `0` 線性至 `1 m` 之格值）；② 寬度 `W` 先四捨五入至公釐再內插，次一宗之起算 ＝ 前一宗遠側寬度之公釐值，分配計算表之 `W(m)` 記至公釐；③ 側街負擔百分率之顯示依十進位四捨五入至二位；④ 地界線恰落於半公釐之跳處之宗，取應分配面積與實際面積較接近之一值（等距者取進位）。

---

## `§五⁗`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `0534828` 之追蹤檔 `2944` 檔·`git grep -l -F`） | `W-G.9-398_補令三`、`W-G.9-398 補令三` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之 `*.md` 亦 `0`） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`（`0534828` 之器）·發單端實跑（受詞 ＝ 本補令之定稿之前一版·其後唯本列與項 `4` 之文字與末列之填）：🔴 機械 `0` 項／🟡 提示 `1` 項——具名豁免：`P-7` 一處（閘 `2⁗` 之以 `0534828` 與 `HEAD` 為二端之差異——其區間**有意**含工項零⁗ 之單之入倉之一筆，其期即「恰 `1` 列：`A`␉`docs/orders/W-G.9-398_補令三.md`」·`W-G.9-395` 補令二之同形）／ℹ️ 記錄 `2` 項（`P-5` ✅；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `24044`–`31788`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `0534828`（雲端 Linux·⛔ `push`）＋ 本補令之定稿之前一版·一 `commit`（首列 ＝ 所令逐字）：工項零⁗ 之 blob ＝ 來源、`git status --porcelain` 空；工項一⁗ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `12`·反向 `0`·`--merges` 空·命中唯 `c35d32a`〔`1` 列〕與 `7c819b5`〔`2` 列〕·`app.py`／`verify/stepg_pipeline.py` 之 blob ＝ `ca9f917e…`／`c9d347c2…`·對 `7c819b5` 相異空）；閘 `1⁗` ＝ 本補令 `118`／`0`·唯此一檔；閘 `2⁗` 恰一 `A`·生產碼、`verify/`、`tests/` 對 `0534828` 相異 `0`、生產碼對 `20e03bf` 恰 `2`、`verify/` 對 `20e03bf` `18`（`M` `17`·`A` `1`）、`tests/` `1`·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`）·`git ls-files ':(glob)verify/*.py'` `33` 檔；閘 `3⁗` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4⁗` 相異 `0`；閘 `6⁗` `✅ 二閘皆過`·`645 644` ⇒ `rc 7`；閘 `7⁗` `rc 0`·四簿 ＝ `§零⁗` 項 `3`；閘 `8⁗` 三十九呼叫（於模擬之 `<C>`）皆 `rc 0`·末列皆合期·`stderr` `0` B·`P0` ＝ 期（耗時之和 `823` s·並行 `2`·環境 `pip freeze` `ae1438da…`）；`checkidx` `索引列數 124；內部字樣 122；外部指標 9；不合 0`、`gen_fa_index` `則 124；加註節 14；列 158`·重生成之檔逐位同；快轉前之記、工項一⁗ 之快轉、出艙 ①②④ 與閘 `5⁗` 須遠端·⛔ 模擬 |

SELF_SHA256: 6d037a3eff13ca18d7aec90b9daeb6a409327a0ea344d5c69e83a8e80bd2f6fc
