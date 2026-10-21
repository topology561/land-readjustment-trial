# `W-G.9-390` 補令四：本補令入側支 ＋ 主線快轉（`2aa6302` → 本補令工項零⁗′ 之 `commit`·`W-G.9-390`〔取得即鎖定之宗之查·`K-9-50` 題一第 3 點之序〕入主線）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-21`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-390_補令三.md`（「補令三」）之 `§四-2⁗`（入主線之短單）。原單、補令一〜三留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `2aa63021da38632704519e05d53ced9f56e22659`；側支 `verify/W-G.9-390-k961r` ＝ `ca3ea9eb674ae5c411a4969f68398baf74be9745`（補令三工項四⁗）；遠端 heads **`50`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `a41022d`；發單端已於拋棄式 worktree 自倉從頭重跑補令三之 `V-1⁗`〜`V-9⁗` 之 `74` 呼叫、前置⁗ (甲)(乙) 之 `20` 呼叫與收工閘〔`§一⁗′` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。本補令 ＝ 入主線之短單；本批之生產碼於本案之配地⛔ 變（`§一⁗′` 項 `2`）⇒ README 第二節之自動處理第 `1`、`2` 款（補令三之 `expects_allocation_change` ＝ `false`、實量亦⛔ 變）。**`expects_allocation_change` ＝ `false`**。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零⁗′ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-390_補令四.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。施工樹之根之複本以 `.git/info/exclude` 免於 `git status`（其式以 `/` 起首：`/W-G.9-390_補令四.md`）。
> 🔑 **撇號**：「⁗′」＝ U+2057 U+2032（補令三之「⁗」之次·補令四），唯指本補令之條；「⁗」＝ 補令三之條；無撇號者指原單之條。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-390-k961r` 之刪除或改寫（保留為歷史）；任何他側支；`ops/queue` 除 `執行端.md` 所許外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零⁗′`　開場（**先於工項零⁗′**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `2aa63021da38632704519e05d53ced9f56e22659`；`git rev-parse origin/verify/W-G.9-390-k961r` ＝ `ca3ea9eb674ae5c411a4969f68398baf74be9745`；`git ls-remote --heads origin` 之列數 ＝ **`50`**（全列存 `<O>/heads_before_390p4.txt`·收工閘 `5⁗′` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-390-k961r` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 634 629` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `619`／`MAX` `634`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `ca3ea9e` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五⁗′` 項 `3`）。

### `§零-1⁗′`　停機款

| # | 款 |
|---|---|
| `1⁗′` | 開工時主線 ≠ `2aa6302`，或側支 ≠ `ca3ea9e`，或遠端 heads ≠ `50`，或施工樹之追蹤檔有變動，或 `§零⁗′` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2⁗′` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗′` | 工項一⁗′ 前置之任一期不符 |
| `4⁗′` | 工項一⁗′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5⁗′` | 工項一⁗′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗′` | 工項零⁗′ 之 `push` 之目標非 `verify/W-G.9-390-k961r`；工項一⁗′ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零⁗′ 之 `commit`；或推至他支 |
| `7⁗′` | `§三-1⁗′` 收工閘任一 ≠ 期 |
| `8⁗′` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9⁗′` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一⁗′ 未成者主線⛔ 動。

---

## `§一⁗′`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-390-k961r` 對主線 `2aa6302` 唯十一筆 `commit`（`git rev-list --count 2aa6302..ca3ea9e` ＝ `11`、反向 ＝ `0`、`--merges` 空）：原單工項零 `7c171db`（`1160`／`0`）、一 `591b9c3`（五器 `4/2`、`5/3`、`10/5`、`4/1`、`561/0`）；補令一工項零″ `640a652`（`642`／`0`）、一″ `ddddfb8`（`149`／`5`）；補令二工項零‴ `320f967`（`725`／`0`）、一‴ `6d1e994`（`38/5`、`81/19`）；補令三工項零⁗ `e456b93`（`1070`／`0`·blob ＝ 來源 `9b74273c…`）、一⁗ `3cf4685`（`probe_WG9388_k961s3.py` `5/3`、`probe_WG9390_k961r.py` `105/372`·施後 blob ＝ 補令三 `§五⁗` 項 `5`·塊 `Fy45` 施於 `6d1e994` 之 `verify/` ≡ `3cf4685` 之 `verify/`）、二⁗ `a41022d`（`app.py` `57`／`15`·blob `82855efb31049c2d21146c2c6fc903182615f912`）、三⁗ `5bbe795`（`K-6` 典 `239`／`0`、自誤簿 `57`／`0`、`docs/待落地清單.md` `69`／`0`）、四⁗ `ca3ea9e`（報告二檔 `400`／`0`、`120`／`0`）。補令三之五筆之首列 ＝ 所令逐字。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `a41022d`（`app.py` `1` 列）。
2. **發單端之獨立復驗**（`2026-10-21`·雲端 Linux `4` 核·倉外之拋棄式 worktree·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報）：
   - **差異之逐行讀**（`git diff 3cf4685 a41022d -- app.py`·`+57`／`−15`）：差異九塊皆在 `k6b_stage3_run` 之內（AST：頂層之名之集同〔具名 `395`·無名 `12`〕、相異之節點恰 `{k6b_stage3_run}`）。`R-1⁗` ＝ 步驟 `1`〜`8` 之環之後、`# ── 步驟 10：後處理 ──` 之前：成者 `_won390` ＝ 紀錄中 `序` ≠ `後處理`、`結果` ＝ `成` 之列之（街廓, 端, 候選）——「成」之寫入窮查恰二處（`_ct_log` 之 `ok`〔`_ct_commit` 之 `successes.append` 與之同支〕與逐列之 `_row(**_base, 結果='成', …)`〔與 `successes.append((_gi, c, _blk))` 相鄰〕），題一 4 之照配之列（`序='後處理'`）濾去；其（街廓, 候選）之排序之多重集對 `successes` 之同、另判重複 ⇒ 不合即 `raise RuntimeError`；成者 ≥ `1` ⇒ `alloc_state` 一次（`_cur390`）：`err` ⇒ 停機（「取得即鎖定之宗之查：試算中止」）、未保留者（`_cur390["kept"]` 之該街廓）⇒ 停機（「…成者 <街廓> <端>端 <候選>、… 於試算⛔ 保留——程式錯誤 ⇒ 停機」·唯具未保留之成者）；步驟 `10` 之首次之 `_cur` ＝ `_cur390`（其間之碼唯求群與 `R`·⛔ 改 `state` ⇒ 與另呼同態；`successes` 空 ⇔ 成者空 ⇒ 步驟 `10` 之環⛔ 入）。還原、`_ban390`、`_grp390`、重試之殘留 `0`。`R-4⁗` ＝ `_recv_out` 之查與其註解整段刪（「於現態未保留」`1` → `0`）。`R-9‴` ＝ `_rk390`（內呼頂層 `k967_rank`／`k967_pre_area`·表 ＝ `state["by"]` 之分攤登記面積 − Σ段三部分併出·成員 ＝ 候選 ∪ 整筆併入之片）＋ `_ct_pick` 之第四參數（`form == '一'` ⇒ 序鍵小者先）＋ `_ct_cross` 之整片二端皆成之支——與補令二之回報附錄甲之同段（發單端 `2026-10-20 19:45` 已逐行讀合 `R-9‴`）語意同；`_ct_pick(A, B, '二')` 恰一見。`R-5⁗` ＝ docstring 增八列（折行皆以反引號、「→」「⇒」起首；新增之列之「四空白＋中文起首」者 `0`）。`py_compile` 過
   - **`94` 呼叫之重跑**：補令三 `§五⁗` 之「項 `8` 之表」之命令（`<repo>` ＝ 各態之拋棄式 worktree 之絕對路徑）：後態（`a41022d`·其 `app.py` 與 `verify/` 與 `ca3ea9e` 逐位同）之 `74` 呼叫 ＋ 前態（`3cf4685`·工項一⁗ 之端）之前置⁗ (甲)(乙) `20` 呼叫 ＝ `94` 呼叫·並行 `2`·耗時之和 `15869` s：皆 `rc` ＝ 該表之同態之期、末列逐字同（`#56`／`#57` 之末列為 JSON 之摘要·⛔ 比）、`stderr` 合計 `0` B；前態之 `#36` ＝ `⇒ 紅 ['S10b …', 'S10c …']；rc 1`、`#38` ＝ `⇒ 紅 ['TI …', 'TT …', 'TU …', 'M3', 'M15', 'M16']；rc 1`、`#65` ＝ `⇒ 紅 ['K13']；rc 1`、`#72` ＝ `⇒ 紅 ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L8', 'L9']；rc 1`、`#73` ＝ `⇒ 紅 ['X1', 'X2']；rc 1`（對照組·⛔ 恆綠）；後態之 `F34 selftest` `L1`〜`L14`／`P0 14／14`、`F34 wiring` `X1`〜`X4`、`F34 run` 之 `R1@3.5`（段三之成者 `3`·⛔ 停機·回原狀之列 `0`·G 值列 `35`）、`R1@0.0`（成者 `0`·G 值列 `36`）、`R0`（`[3, 0]`）、`F32 selftest` `K13`、`F13 selftest` `M0`〜`M16` 皆 ✅；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`、`F32`）、`29／29`（`F28`）、`16／16`（`F33`）、`14／14`（`F34`）
   - **本案配地⛔ 變**：`k6s3 cmp`（前態 `3cf4685` 對後態 `a41022d`）二退縮皆 `rc 0`、末列 `相異 0 項 ⇒ ✅ 同`、`stderr` `0` B（對照：`k6s3_pre_35` 對 `k6s3_post_00` ⇒ `相異 18 項 ⇒ 🔴 異`）；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`，其落檔與 `stdout` 以同一字樣代 `HEAD` 之值後前後逐位同（對照：⛔ 代之則異）
   - **收工閘**（補令三 `§四-3⁗`·於 `ca3ea9e`）：閘 `1⁗` 十一筆之增刪 ＝ 項 `1`；閘 `2⁗` 生產碼相異 `1`（`app.py`）、`verify/` 相異 `5`（`M` `4`·`A` `1`）、新檔三之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3⁗` `15` 檔之 blob `CR` 合計 `0`（`data/V6.dxf` `12308`）；閘 `4⁗` `K-6` 典 `868268` → `909964`、自誤簿 `1215603` → `1225486`、`docs/待落地清單.md` `10814` → `20188`·改前皆改後之嚴格前綴·其尾 ＝ 塊 `K33`＋`K34`＋`K35`＋`K36`、`E34`＋`E35`＋`E36`、`P44`＋`P45`＋`P46`＋`P47`（自倉內之四單抽取·逐位同）·`CLAUDE.md`、`GB` 簿、`VR` 簿、`.claude/`、`verify/selection_pipeline.py` 對 `2aa6302` 相異 `0`；閘 `5⁗` heads `50`、主線 `2aa6302`、側支 `ca3ea9e`（祖含 `6d1e994`）、其餘 `48` 列逐列 ＝ 補令三回報之附錄之同列；閘 `6⁗` `closegate 634 629 .` ⇒ `rc 0`（`✅ 二閘皆過`·判別力 `635 634` ⇒ `rc 7`）；閘 `7⁗` `rc 0`·四簿之值 ＝ `§零⁗′` 項 `3`；閘 `8⁗` `checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`，`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·重生成之檔與倉內逐位同；倉內之差異檔 ＝ `git diff 2aa6302 a41022d -- app.py` 逐位同
3. **快轉之受詞**：工項零⁗′ 推後之側支之端（工項零⁗′ 之 `commit`）；其祖含 `2aa6302` 與 `ca3ea9e`；`2aa6302..<工項零⁗′>` 之 `commit` 數 ＝ `12`、`--merges` 空；生產碼之命中唯 `a41022d`（項 `1`）。

---

## `§二⁗′`　射程

🛑 `(a)` 工項零⁗′（零生產碼）推至側支 `verify/W-G.9-390-k961r`（快轉）；`(b)` 工項一⁗′ 主線快轉至工項零⁗′ 之 `commit`（**以前置皆符為條件**·⛔ `--force`）；`(c)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `2aa63021da38632704519e05d53ced9f56e22659` → `<工項零⁗′ 之全 40 碼>`」（README 第二節「入主線之安全」）；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(e)` ⛔ 及生產碼、`verify/`、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(f)` 執行報告⛔ 另立（補令三工項四⁗ 之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三⁗′`　工項（依序）

### 工項零⁗′　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-390_補令四.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-390_補令四.md` 與來源逐位同（停機款 `2⁗′`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-390 補令四 工項零⁗′：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-390-k961r`（快轉）。

### 工項一⁗′　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零⁗′ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-390-k961r` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `2aa63021da38632704519e05d53ced9f56e22659`。
2. `git merge-base --is-ancestor 2aa63021da38632704519e05d53ced9f56e22659 <C>` ⇒ `rc 0`；`git rev-list --count 2aa6302..<C>` ＝ `12`；`git rev-list --count <C>..2aa6302` ＝ `0`；`git rev-list --merges 2aa6302..<C>` ＝ 空。
3. `git rev-list 2aa6302..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `a41022ddec898a454489dc36c8e23a6535f046c6`（命中 `1` 列 `app.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `82855efb31049c2d21146c2c6fc903182615f912`；`git diff --name-only a41022ddec898a454489dc36c8e23a6535f046c6 <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3⁗′`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4⁗′`）；⛔ 刪側支 `verify/W-G.9-390-k961r`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗′`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads ＝ **`50`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `a41022d` 之相異 ＝ **`0`**；判別力［必非零］：vs `2aa6302` 之相異 ＝ **`1`**（`app.py`）；④ `git branch -r --contains a41022ddec898a454489dc36c8e23a6535f046c6` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-390-k961r`）。

---

## `§三-1⁗′`　收工閘（工項一⁗′ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗′` | 工項零⁗′ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（`116`）／`0`·唯此一檔；首列 ＝ `§三⁗′` 所令逐字 |
| `2⁗′` | `git -c core.quotepath=false diff --name-status ca3ea9e HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-390_補令四.md`；生產碼與 `verify/` 之一切檔對 `ca3ea9e` 相異 **`0`**；判別力［必非零］：生產碼對 `2aa6302` 相異 **`1`**（`app.py`）、`verify/` 對 `2aa6302` 相異 **`5`**（`M` `4`·`A` `1`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗′` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗′` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` | 對 `ca3ea9e` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `8ae87d473218de9ff2efd19ef5890502da8fbfa6`；自誤簿 ＝ `c5406d05c024dae897beb3c1175934ece7c0819b`；`docs/待落地清單.md` ＝ `adf906d43045f365cec15fc345666c9c874faed5`） |
| `5⁗′` | 自限 | 遠端 heads **`50`**；主線 ＝ `<C>`；側支 `verify/W-G.9-390-k961r` ＝ `<C>`；其餘 `48` 列中除 `ops/queue`（回報後可變）外之 `47` 列逐列 ＝ `<O>/heads_before_390p4.txt` 之同列 |
| `6⁗′` | `python3 verify/probes/probe_WG9270_closegate.py 634 629 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 635 634 .` ⇒ `rc 7` |
| `7⁗′` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 634 629` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零⁗′` 項 `3` 之值（⛔ 變） |
| `8⁗′` | 量測器（於主線之端·`23` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`… wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`… wiring <repo> 929ea20`；`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`；`… wiring <repo> 2aa6302` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`）、`16／16`（`F33`）、`14／14`（`F34`）；`F32 selftest` `K1`〜`K31`、`F33 selftest` `K1`〜`K16`、`F34 selftest` `L1`〜`L14`、`F34 wiring` `X1`〜`X4` 皆 ✅ |

---

## `§四⁗′`　土地後果

**本案**：配地⛔ 變（`§一⁗′` 項 `2`·`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔逐位同、`parity` 不符 `0`；`F34 run`：`3.5 m` 之段三之成者 `3` 皆保留 ⇒ ⛔ 停機，`0 m` 之段三之成者 `0`）。**他案**：主線自此，段三（街角合併重試與末端塊合併再試）之取得之宗（末端塊、街角地）**取得即鎖定**（`K-9-80`）——步驟 1〜8 畢後以一次之試算查一切取得之宗之保留，未保留或試算中止 ⇒ 停機（程式之自我檢查），⛔ 再「回原狀而由名單之下一名續試」；鎖定之宗仍受同一地主之併入而原地變寬（後處理照舊）；`K-9-50` 題一第 3 點（末端塊整片各試而二端皆成）之歸屬 ＝ `G` 大 → 重劃前面積大 → 暫編地號小（KL `2026-10-20 09:11`·⛔ 再以與末端塊範圍之交之面積為首鍵）；題二⛔ 變。

---

## `§五⁗′`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `ca3ea9e` 之追蹤檔 `2905` 檔·`git grep -l -F`） | `W-G.9-390_補令四`、`W-G.9-390 補令四` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之全部 `*.md` 亦 `0`·發單端實查） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（拋棄式樹·態 `ca3ea9e` ＋ 本補令之定稿之前一版·其後唯本列與項 `4` 之文字與末列之填）：🔴 機械 `0` 項（定稿之前一版之 `P-5` 唯末列之占位〔全 `0`〕之不符·定稿以實算之值填之）／🟡 提示 `0` 項／ℹ️ 記錄（`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23508`–`31250`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `ca3ea9e`（雲端 Linux·⛔ `push`）＋ 本補令之定稿之前一版·一 `commit`（首列 ＝ 所令逐字）：工項零⁗′ 之 blob ＝ 來源；工項一⁗′ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `12`·反向 `0`·`--merges` 空·命中唯 `a41022d`〔`1` 列〕·`app.py` 之 blob ＝ `82855efb…`·對 `a41022d` 相異空）；閘 `1⁗′` ＝ 本補令 `116`／`0`·唯此一檔；閘 `2⁗′` 恰一 `A`·生產碼與 `verify/` 對 `ca3ea9e` 相異 `0`、生產碼對 `2aa6302` 恰 `1`、`verify/` 對 `2aa6302` `5`（`M` `4`·`A` `1`）·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`）；閘 `3⁗′` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4⁗′` 相異 `0`·四 blob ＝ 期；閘 `6⁗′` `✅ 二閘皆過`·`635 634` ⇒ `rc 7`；閘 `7⁗′` `rc 0`·四簿 ＝ `§零⁗′` 項 `3`；閘 `8⁗′` 二十三呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B·`P0` ＝ 期；工項一⁗′ 之快轉、出艙 ①②④ 與閘 `5⁗′` 須遠端·⛔ 模擬 |

SELF_SHA256: 9ead1ba9444ceafcbb0c556324343b2409f2b17321734a871099f7e0f062dafb
