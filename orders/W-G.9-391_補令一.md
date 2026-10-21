# `W-G.9-391` 補令一：本補令入側支 ＋ 主線快轉（`a8657c4` → 本補令工項零″ 之 `commit`·`W-G.9-391`〔範圍依最小建築面積之擴大·短街廓之警示停止·`K-9-80` ④⑤⑥·`K-9-34`〕入主線）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字、⛔ 動帳本；受詞 ＝ 本補令之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-21`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-391_規格單.md`（「原單」）之 `§四-2`（入主線之短單）。原單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`；側支 `verify/W-G.9-391-k980x` ＝ `b95b44d9c352ae951492d9acca28b8f3e0260f00`（原單工項四）；遠端 heads **`51`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `a65e3c7`；發單端已於拋棄式 worktree 自倉從頭重跑原單之 `V-1`〜`V-9` 之 `77` 呼叫、前置 (甲)(乙) 之 `39` 呼叫與收工閘〔`§一″` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。
> **授權**（`ops/queue` 之 `README_自動化運作規則.md` 第一節·KL 之逐字）：「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」（`2026-10-17 07:23` 第 `3` 點）；「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」（`2026-10-17 07:58`）。本補令 ＝ 入主線之短單；原單（新規格單）之生產碼於本案之配地⛔ 變（`§一″` 項 `2`）⇒ README 第二節之自動處理第 `1` 款（停止條件 `2` ⛔ 成就：原單之 `expects_allocation_change` ＝ `false`、實量亦⛔ 變）。**`expects_allocation_change` ＝ `false`**。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：工項零″ 所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-391_補令一.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。施工樹之根之複本以 `.git/info/exclude` 免於 `git status`（其式以 `/` 起首：`/W-G.9-391_補令一.md`）。
> 🔑 **撇號**：「″」＝ U+2033（補令一），唯指本補令之條；無撇號者指原單之條。
> 🔑 **快轉前之記**（README 第二節「入主線之安全」·`W-G.9-390` 補令四之復驗所記之單式之疏之正）：主線之前值 → 後值，於**快轉之前**記於 `ops/queue` 之 `log.md`（增一列）與 `STATE.json` 之 `history`（增一筆·`from` ＝ `to` ＝ `running`）⇒ `commit`（首列 `ops: 執行端快轉前之記 W-G.9-391_補令一`）、推送 `ops/queue`（被拒 ⇒ 重取再推·⛔ `--force`）；推成之後方快轉（`§三″` 工項一″）。回報之列再記快轉後之實值。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-391-k980x` 之刪除或改寫（保留為歷史）；任何他側支；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零″`　開場（**先於工項零″**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`；`git rev-parse origin/verify/W-G.9-391-k980x` ＝ `b95b44d9c352ae951492d9acca28b8f3e0260f00`；`git ls-remote --heads origin` 之列數 ＝ **`51`**（全列存 `<O>/heads_before_391p1.txt`·收工閘 `5″` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-391-k980x` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 634 629` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `619`／`MAX` `634`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `b95b44d` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五″` 項 `3`）。

### `§零-1″`　停機款

| # | 款 |
|---|---|
| `1″` | 開工時主線 ≠ `a8657c4`，或側支 ≠ `b95b44d`，或遠端 heads ≠ `51`，或施工樹之追蹤檔有變動，或 `§零″` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2″` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3″` | 工項一″ 前置之任一期不符；或快轉前之記（單首 🔑）之推送不能成 |
| `4″` | 工項一″ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `5″` | 工項一″ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6″` | 工項零″ 之 `push` 之目標非 `verify/W-G.9-391-k980x`；工項一″ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項零″ 之 `commit`；或推至他支 |
| `7″` | `§三-1″` 收工閘任一 ≠ 期 |
| `8″` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本補令之新檔為 `git check-ignore -v --no-index` 所命中 |
| `9″` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項一″ 未成者主線⛔ 動（快轉前之記已推者，於回報中記「未快轉」）。

---

## `§一″`　所據

1. **本批之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-391-k980x` 對主線 `a8657c4` 唯五筆 `commit`（`git rev-list --count a8657c4..b95b44d` ＝ `5`、反向 ＝ `0`、`--merges` 空）：原單工項零 `65b1f25`（本單 `1346`／`0`·blob `sha256` ＝ 來源 `22ef8a8c…`）、一 `a749c78`（`12` 器·增刪 ＝ 原單閘 `1`·施後 blob ＝ 原單 `§五-1` 項 `5`·塊 `Fy46` 施於 `a8657c4` 之樹 ＝ `a749c78` 之樹〔唯本單一檔之異〕）、二 `a65e3c7`（`app.py` `201`／`17`·blob `b591d7605b932b42c9dc205bb8589ef04505045b`；`verify/run_verification.py` `1`／`0`·`ef043da43e69f236550d0f420f6684f2edd271e4`；`verify/stepg_pipeline.py` `9`／`0`·`b2f6622351d1bcdcdf7b603c7412a8f902aa2edc`）、三 `54812a4`（`K-6` 典 `57`／`0`、`docs/待落地清單.md` `21`／`0`）、四 `b95b44d`（報告二檔 `1322`／`0`、`423`／`0`）。五筆之首列 ＝ 所令逐字。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `a65e3c7`（`3` 列）。
2. **發單端之獨立復驗**（`2026-10-21`·雲端 Linux `4` 核·倉外之拋棄式 worktree·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`·⛔ 採執行端之自報）：
   - **差異之逐行讀**（`git diff a749c78 a65e3c7 -- app.py verify/stepg_pipeline.py verify/run_verification.py`·`423` 列·與倉內之差異檔逐位同）：逐條合 `R-1`〜`R-9`——`R-1` 三常數；`R-2` `k980_mba`（`session` 為 `None` ⇒ `{}`·二鍵缺 ⇒ `0`）；`R-3` `_build_corner_range_v3` 之末增 `min_build_area=None`，擴大之碼唯在 `return rng` 之前（`None`／`0`／已達 ⇒ 原物；`< 0` ⇒ `_stop`；全街廓扣截角仍未達 ⇒「K-9-80 ⑥ 短街廓」；二分 `[S1_par, 過最遠頂點之平移量]` 至多 `200` 次·⛔ 收斂 ⇒ `_stop`；切線 ∥ SIDE_LINE〔`(sux, suy)`〕·沿 `sigma·d̂` 平移·取距既有之 `_anchor` 最近之片扣截角；另「擴大後須含擴大前」之 `_stop`〔塊 `K37` 之六 `56`〕）；`R-4` `end_block_band_width`（倍增之上界 ＝ 外接矩形之對角線·二分 `200`）與 `_end_region_R`／`end_block_side_geom`／`end_block_apply`／`end_block_host` 之逐層照傳（`end_block_host` 之新列在 `trial=_trial, cache=_cache, allow_forced=_allow)` 之前一列）；`R-5` `_place_pool_parcels` 之末端保留之帶 ＝ `_end_region_R(…)[0]`、未臨正街之多邊形 ＝ 同處之 `_block_strip(…)[0]`、`_end_band` 之直呼去之；`R-6` 二宿主之 `end_block_host`／`_place_pool_parcels` 皆傳 `k980_mba(…)`、`end_block_host` 之後於同一 `if` 之內查四範圍（街角規定範圍之源 ＝ 傳予 `end_block_host` 之同物）、`_WF_NS_NAMES` 增二名；`R-7` 四處皆傳（`v12` 之 `_mba_pk` 於 `try` 之內立·`except` ⇒ `None`·二範圍建畢即查；`main` 唯增一列）；`R-8` 任二者 `distance ≤ 0.01` ⇒ 停機（訊息含「K-9-80 ⑥」「短街廓」、街廓名、二名、距、交之面積）；`R-9` 新增之區域名皆帶 `391`（`_mba_pk` 為單所令）。AST：`app.py` 頂層之增恰六、減 `0`、相異之節點 ＝ 此六 ∪ `§三-3` 第 `4` 款之十；stepg ＝ `{_run_step_g_impl}`、`run_verification` ＝ `{build_param_table}`；`verify/selection_pipeline.py` ⛔ 動。`V-8` 之四字樣：`app.py` 「K-9-80 ⑥」`4`、「k980_mba」`6`、「k980_range_touch_check」`4`、「end_block_band_width」`7`；`run_verification` 「k980_mba」`1`；stepg 「k980_mba」`3`、「k980_range_touch_check」`1`（`a749c78` 皆無出艙 `rc 1`）
   - **`116` 呼叫之重跑**：原單 `§五-1` 之「項 `8` 之表」之命令（`<repo>` ＝ 各態之拋棄式 worktree 之絕對路徑）：後態（`b95b44d`·其生產碼與 `verify/` 與 `a65e3c7` 逐位同）之 `77` 呼叫 ＋ 前態（`a749c78`·工項一之端）之前置 (甲)(乙) `39` 呼叫 ＝ `116` 呼叫·並行 `2`·耗時之和 `29867` s：皆 `rc` ＝ 該表之同態之期、末列逐字同（`#56`／`#57` 之末列為 JSON 之摘要·⛔ 比）、`stderr` 合計 `0` B；前態之 `#75` ＝ `⇒ 紅 ['受詞缺']；rc 1`、`#76` ＝ `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W8', 'W9']；rc 1`、`#77` ＝ `⇒ 紅 ['受詞缺']；rc 1`（對照組·⛔ 恆綠）；後態之 `F35 selftest` `C1`〜`C9`、`E1`〜`E6`、`T1`〜`T6`、`K1`／`P0 22／22`、`F35 wiring` `W1`〜`W9`、`F35 run` 之 `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0`（`R1` 街角 `8` 範圍·末端塊 `R6` 左 `252.28`；`R2` 諸源之範圍之面積 ＝ 輸入值）皆 ✅；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`、`F32`）、`29／29`（`F28`）、`16／16`（`F33`）、`14／14`（`F34`）、`22／22`（`F35`）。另於 `b95b44d` 之實碼作四突變（短街廓之判⛔ 停、末端保留之帶改傳 `None`、`_WF_NS_NAMES` 去 `k980_range_touch_check`、街角之擴大之切線改 ∥ 前緣線）⇒ `F35` 依序紅 `T2`／`T3`／`T4`／`T6`、`W8`、`W9`、`C5`／`C8`／`C9`（實碼之上之判別力）
   - **本案配地⛔ 變**：`k6s3 cmp`（前態 `a749c78` 對後態 `b95b44d`）二退縮皆 `rc 0`、末列 `相異 0 項 ⇒ ✅ 同`、`stderr` `0` B（對照：`k6s3_pre_35` 對 `k6s3_post_00` ⇒ `相異 18 項 ⇒ 🔴 異`）；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`，其落檔與 `stdout` 以同一字樣代 `HEAD` 之值後前後逐位同（對照：⛔ 代之則異）
   - **收工閘**（原單 `§四-3`·於 `b95b44d`）：閘 `1` 五筆之增刪 ＝ 項 `1`；閘 `2` 生產碼相異 `3`、`verify/` 相異 `14`（`M` `13`·`A` `1`）、新檔四之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `20` 檔之 blob `CR` 合計 `0`（`data/V6.dxf` `12308`）；閘 `4` `K-6` 典 `909964` → `919452`、`docs/待落地清單.md` `20188` → `23233`·改前皆改後之嚴格前綴·其尾 ＝ 塊 `K37`／`P48`（自本單抽取·逐位同）·`CLAUDE.md`、自誤簿、`GB` 簿、`VR` 簿、`.claude/`、`verify/selection_pipeline.py` 對 `a8657c4` 相異 `0`；閘 `5` heads `51`、主線 `a8657c4`、側支 `b95b44d`（祖含 `a8657c4`）、其餘之列對 `W-G.9-390` 補令三之回報之附錄唯 `W-G.9-390` 補令四所快轉之二列（主線、`verify/W-G.9-390-k961r` ＝ `a8657c4`）與 `ops/queue` 異；閘 `6` `closegate 634 629 .` ⇒ `rc 0`（`✅ 二閘皆過`·判別力 `635 634` ⇒ `rc 7`）；閘 `7` `rc 0`·四簿之值 ＝ `§零″` 項 `3`；閘 `8` `checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`，`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·重生成之檔與倉內逐位同
3. **快轉之受詞**：工項零″ 推後之側支之端（工項零″ 之 `commit`）；其祖含 `a8657c4` 與 `b95b44d`；`a8657c4..<工項零″>` 之 `commit` 數 ＝ `6`、`--merges` 空；生產碼之命中唯 `a65e3c7`（項 `1`）。

---

## `§二″`　射程

🛑 `(a)` 工項零″（零生產碼）推至側支 `verify/W-G.9-391-k980x`（快轉）；`(b)` 快轉前之記（單首 🔑）推至 `ops/queue`；`(c)` 工項一″ 主線快轉至工項零″ 之 `commit`（**以前置皆符、快轉前之記已推為條件**·⛔ `--force`）；`(d)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `a8657c4012d961eccebd77cd812c0ab6aeab030f` → `<工項零″ 之全 40 碼>`」（快轉後之實值）；`(e)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(f)` ⛔ 及生產碼、`verify/`、任何錨、帳本、`CLAUDE.md`、`.claude/`；`(g)` 執行報告⛔ 另立（原單工項四之報告已入倉；本補令之出艙與收工閘之實值唯載於回報）。

---

## `§三″`　工項（依序）

### 工項零″　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-391_補令一.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-391_補令一.md` 與來源逐位同（停機款 `2″`）；`git status --porcelain --untracked-files=no` 唯此 `1` 檔。`commit` 訊息之首列逐字 `W-G.9-391 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-391-k980x`（快轉）。

### 工項一″　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項零″ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-391-k980x` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`。
2. `git merge-base --is-ancestor a8657c4012d961eccebd77cd812c0ab6aeab030f <C>` ⇒ `rc 0`；`git rev-list --count a8657c4..<C>` ＝ `6`；`git rev-list --count <C>..a8657c4` ＝ `0`；`git rev-list --merges a8657c4..<C>` ＝ 空。
3. `git rev-list a8657c4..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `a65e3c78bdc2ab06328ce442358245ddb236f831`（命中 `3` 列：`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `b591d7605b932b42c9dc205bb8589ef04505045b`；`git rev-parse <C>:verify/run_verification.py` ＝ `ef043da43e69f236550d0f420f6684f2edd271e4`；`git rev-parse <C>:verify/stepg_pipeline.py` ＝ `b2f6622351d1bcdcdf7b603c7412a8f902aa2edc`；`git diff --name-only a65e3c78bdc2ab06328ce442358245ddb236f831 <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `3″`·⛔ 快轉。

**快轉前之記**（前置皆符後·單首 🔑）：`ops/queue` 之 `log.md` 增一列、`STATE.json` 之 `history` 增一筆，皆記「主線 `a8657c4012d961eccebd77cd812c0ab6aeab030f` → `<C>`（將快轉）」⇒ `commit`、推送 `ops/queue`。推成之後方行下款。

**快轉**（與前置、快轉前之記為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `4″`）；⛔ 刪側支 `verify/W-G.9-391-k980x`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5″`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads ＝ **`51`**（⛔ 增減）；③ 生產碼 `34` 檔（`app.py` 與 `git ls-files ':(glob)verify/*.py'` 之 `33` 檔）於新主線 vs `a65e3c7` 之相異 ＝ **`0`**；判別力［必非零］：vs `a8657c4` 之相異 ＝ **`3`**（`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）；④ `git branch -r --contains a65e3c78bdc2ab06328ce442358245ddb236f831` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-391-k980x`）。

---

## `§三-1″`　收工閘（工項一″ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1″` | 工項零″ 之 `commit` 之增刪（`git show --numstat`） | 本補令之增（`119`）／`0`·唯此一檔；首列 ＝ `§三″` 所令逐字 |
| `2″` | `git -c core.quotepath=false diff --name-status b95b44d HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`1`** 列：`A`␉`docs/orders/W-G.9-391_補令一.md`；生產碼與 `verify/` 之一切檔對 `b95b44d` 相異 **`0`**；判別力［必非零］：生產碼對 `a8657c4` 相異 **`3`**（`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）、`verify/` 對 `a8657c4` 相異 **`14`**（`M` `13`·`A` `1`）；本補令之 `git check-ignore -v --no-index` 無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3″` | 本補令之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4″` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` | 對 `b95b44d` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`；`K-6` 典 ＝ `0fad1dafd3c6236b571969b1538170f8662d9ee6`；自誤簿 ＝ `c5406d05c024dae897beb3c1175934ece7c0819b`；`docs/待落地清單.md` ＝ `48b50c3da80dff7143b82fc9eeba00673750a158`） |
| `5″` | 自限 | 遠端 heads **`51`**；主線 ＝ `<C>`；側支 `verify/W-G.9-391-k980x` ＝ `<C>`；其餘 `49` 列中除 `ops/queue`（回報後可變）外之 `48` 列逐列 ＝ `<O>/heads_before_391p1.txt` 之同列 |
| `6″` | `python3 verify/probes/probe_WG9270_closegate.py 634 629 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 635 634 .` ⇒ `rc 7` |
| `7″` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 634 629` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零″` 項 `3` 之值（⛔ 變） |
| `8″` | 量測器（於主線之端·`25` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`；`… wiring <repo> fd88f64`；`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`；`… wiring <repo> 929ea20`；`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`；`… wiring <repo> 2aa6302`；`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`；`… wiring <repo> a8657c4` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`）、`16／16`（`F33`）、`14／14`（`F34`）、`22／22`（`F35`）；`F32 selftest` `K1`〜`K31`、`F33 selftest` `K1`〜`K16`、`F34 selftest` `L1`〜`L14`、`F34 wiring` `X1`〜`X4`、`F35 selftest` `C1`〜`C9`／`E1`〜`E6`／`T1`〜`T6`／`K1`、`F35 wiring` `W1`〜`W9` 皆 ✅ |

---

## `§四″`　土地後果

**本案**：配地⛔ 變（`§一″` 項 `2`·`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔逐位同、`parity` 不符 `0`；本案之驗證⛔ 輸入最小建築面積 ⇒ 範圍逐位⛔ 變·短街廓之查⛔ 觸）。**他案**：主線自此，有最小建築面積之輸入（街廓覆寫或分區底·有效值 ＞ `0`）之街廓，其街角規定範圍（遠側界線續 ∥ SIDE_LINE 平移）與末端塊範圍（末端帶之內側界沿宗地分配線內移·無退縮）擴至 `[最小建築面積, ＋0.01 ㎡]`；街角選位之跨占之名單與門檻、參數表之街角最小面積（強制抵費地之面積之源）、末端塊之評選之 `R_end` 與末端保留皆以擴大後之範圍（`K-9-80` ⑤）；一街廓之二範圍之距 ≤ `0.01 m`（相接或重疊）、或擴至他端仍未達 ⇒ 警示停止（`K-9-80` ⑥·**未輸入而二範圍本即相接或重疊者亦停**——塊 `K37` 之二之己）。

---

## `§五″`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `b95b44d` 之追蹤檔 `2910` 檔·`git grep -l -F`） | `W-G.9-391_補令一`、`W-G.9-391 補令一` ＝ 皆 `0` 檔 ⇒ 可取（`ops/queue` 之全部 `*.md` 亦 `0`·發單端實查） |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（態 `b95b44d` ＋ 本補令之定稿之前一版·其後唯本列與項 `4` 之文字與末列之填）：🔴 機械 `0` 項（定稿之前一版之 `P-5` 唯末列之占位〔全 `0`〕之不符·定稿以實算之值填之）／🟡 提示 `0` 項／ℹ️ 記錄（`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23691`–`31434`·本補令⛔ 用·唯記錄） |
| `4` | 模擬 | 拋棄式 worktree `b95b44d`（雲端 Linux·⛔ `push`）＋ 本補令之定稿之前一版·一 `commit`（首列 ＝ 所令逐字）：工項零″ 之 blob ＝ 來源；工項一″ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `6`·反向 `0`·`--merges` 空·命中唯 `a65e3c7`〔`3` 列〕·三檔之 blob ＝ 期·對 `a65e3c7` 相異空）；閘 `1″` ＝ 本補令 `119`／`0`·唯此一檔；閘 `2″` 恰一 `A`·生產碼與 `verify/` 對 `b95b44d` 相異 `0`、生產碼對 `a8657c4` 恰 `3`、`verify/` 對 `a8657c4` `14`（`M` `13`·`A` `1`）·本補令之 `git check-ignore -v --no-index` 無命中（`rc 1`）；閘 `3″` `CR` `0`；閘 `4″` 相異 `0`·四 blob ＝ 期；閘 `6″` `✅ 二閘皆過`·`635 634` ⇒ `rc 7`；閘 `7″` `rc 0`·四簿 ＝ `§零″` 項 `3`；閘 `8″` 二十五呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B；快轉前之記、工項一″ 之快轉、出艙 ①②④ 與閘 `5″` 須遠端·⛔ 模擬 |

SELF_SHA256: acb99fd38776a34669a3330edfd365662ba82ecb2d0f7ed4c87f085b717eddda
