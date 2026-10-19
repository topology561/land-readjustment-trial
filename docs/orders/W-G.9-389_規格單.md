# `W-G.9-389`　規格單：試算內之程式之停機之上拋（訊息帶 `GB-` 之號或【未裁】之停機，於試算〔併入之前後之配地、街角定案〕之內觸之者⛔ 判為「不過」「未成」「試算中止」而續辦——其全文上拋；他之配地中止照舊為「不過」）＋ `K-9-61` 之落地之單之再分（④⑤ ⇒ `W-G.9-390`）＋ 待落地清單之更新（新側支 `verify/W-G.9-389-trialstop`）

> **本單建議等級 ＝ `high`**（生產碼 `2` 檔：`app.py` 之頂層之新名 `5`〔`§三-2`〕與既有 `11` 頂層節點之內之二形之改〔換列與增列·`§三-1`〕、`verify/selection_pipeline.py` 之增列 `3` 對；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-19`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本·工項零〜四之一切 `commit` 推至**新側支 `verify/W-G.9-389-trialstop`**，其起點 ＝ 主線之端 `929ea20`）。
> **流程 ＝ 規格單**（常態）：**生產碼由執行端依 `§三` 撰寫**；發單端給規格（`§三`）、量測器（塊 `Fy41`·執行端⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py`／`verify/selection_pipeline.py` 之 blob（由執行端回報、發單端復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `2` 檔；**本案之配地⛔ 變**〔`§一` 項 `5`〕）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`（`W-G.9-388` 入主線·補令三工項零⁗）；遠端 heads **`48`**（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-389-trialstop`（工項零立之·其後皆快轉）；主線⛔ 動**（入主線另以短單·`§四-2`）。
> 🔑 **通則** ＝ `ops/queue` 之 `README_自動化運作規則.md` 第六節（雲端·Linux）：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之**絕對路徑**；`<O>` ＝ 執行端自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）；`commit` 訊息一律 `git commit -F`；含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8；Bash 命令⛔ 含 heredoc。塊 `Fy41`／`K32`／`P43` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ 遠端分支 `ops/queue` 之 `orders/W-G.9-389_規格單.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python3 -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限** ＝ README 第六節第 `3` 款：各驗之命令之同時並行數 ≤ **`2`**；逾時或 `rc` ≠ 期者，於⛔ 他負載之下**重跑一次**，二趟之出艙皆照實入報告（重跑之趟 ＝ 期 ⇒ 該呼叫以重跑之趟為準·報告具名之）。
> 🔑 **前置驗算之沿用**（`發單端.md` 丙 3之一·`執行端.md` 丙 4之一·KL `2026-10-18 19:57`）：前置之 (甲)(乙)(丙) 見 `§四-1` 工項二之前置；(丙) 之沿用以 `ops/queue` 之 `基準/929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb.md` 為準，其前提之比對（主線之端、`python3 --version`、`pip freeze` 之 `sha256`）之結果入回報。
> 🔑 **撰碼中之自跑**：執行端撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🔑 **⛔ 寫 `CLAUDE.md`**（雲端之分類器拒之·KL `2026-10-17 22:42` 同意）：待落地清單之更新寫於 `docs/待落地清單.md`（塊 `P43`·純末端追加）。本單⛔ 須 `CLAUDE.md` 之改。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之 `§三-1` 所列以外之一字（含 `§三-1` 所列之頂層節點內之他字、其 docstring 與註解〔`R-3` 所令之句之尾註除外〕）；生產碼 `34` 檔之 `app.py`、`verify/selection_pipeline.py` 以外之 `32` 檔；`§三-3` 之禁改；既有量測器除塊 `Fy41` 所改之 `7` 檔外之一字；`data/` 之一切檔、`verify/case_params_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、`GB` 簿、自誤簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/`、`CLAUDE.md` 之一字；`K-6` 典、`docs/待落地清單.md` 除塊 `K32`／`P43` 之純末端追加外之一字；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；任何他側支之推送、刪除或改寫；`K-9-61` ④⑤（取得街角之宗未保留之還原、`GB-205` 之還原）、`K-9-59`、`K-9-60`、`K-9-62` 之指配、`K-9-63`——另單。
> 🔴 **本單⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本單未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量與本機之核數（`nproc`）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`；`git ls-remote --heads origin` 之列數 ＝ **`48`**（全列存 `<O>/heads_before_389.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-389-trialstop`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 629 623` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `614`／`MAX` `629`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（發單端於 `929ea20` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝之出艙存 `<O>`）；量測之殼之旗標之出艙 ＝ 單首 🔑 之期。
6. 版本之比對（前置 (丙) 之前提）：`python3 --version` 與 `python3 -m pip freeze` 之全文之 `sha256`，對 `ops/queue` 之 `基準/929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb.md` 之「一、環境之指紋」（發單端於 `929ea20` 之值：`Python 3.11.17`、``ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac``）；其結果入回報（相異 ⇒ 前置 (丙) 整份照跑·⛔ 停機）。

### `§零-1`　取號現查（宣告框）

**本批⛔ 鑄號**（`自誤`、`GB`、`VR`、`K-9` 皆⛔ 鑄·塊 `K32` 之二 ＝ 發單端之【工】之讀法·⛔ 充裁）。

**塊名、新名**（母體 ＝ 開工態 `929ea20` 之追蹤檔 **`2893`** 檔·`git grep -l`／`git grep -h … | wc -l` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fy41`、`K32`、`P43`（逐名） | 皆 `0`／`0` | `Fy41` `0`／`0`；`K32` `30`／`122`；`P43` `2`／`2` | 🟢 可取（`K32` 之諸列皆量測器之項名或他物〔⛔ 塊名〕；`P43` 之二檔皆二進位〔`.xlsx`／`.pdf`〕之偶合） |
| 對照甲［必非零］`Fy40` | `2`／`10` | — | 🟢 框非恆空 |
| 對照甲［必非零］`K31` | `1`／`5` | — | 🟢 框非恆空 |
| 對照甲［必非零］`P42` | `1`／`4` | — | 🟢 框非恆空 |
| 報告名 `W-G.9-389R`、新側支之名 `W-G.9-389-trialstop`、本單名 `W-G.9-389_規格單`、新器 `probe_WG9389`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |
| 新頂層之名 `K6_PROGRAM_STOPS`、`K6_PROGRAM_STOP_RE`、`k6_program_stop`、`k6_trial_mark`、`k6_trial_raise_since`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名 |

量測器之新檔名 `F33`（`verify/probes/probe_WG9389_trialstop.py`）。收工閘 `6`／`7` 以 `629 623` 驗之（本批⛔ 鑄自誤·同 `W-G.9-388` 補令三之閘 `6⁗`／`7⁗`）。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `929ea20`，或遠端 heads ≠ `48`、或已含 `refs/heads/verify/W-G.9-389-trialstop`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期，或 `§零-0` 項 `5` 之環境於安裝後仍不能匯入 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本單不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy41`／`K32`／`P43` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy41` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或執行端須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-389-trialstop`（工項零〜四）或 `ops/queue`（回報）；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之二檔（`K-6` 典、`docs/待落地清單.md`）：任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊，或寫出後之 blob ≠ `§五-1` 項 `5`；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | 執行端作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或執行端認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 |
| `13` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁：停機上呈之全文寫入 `ops/queue` 之 `reports/W-G.9-389_規格單_回報.md`（`result` ＝ `停機上呈`）；已推至新側支之 `commit` ⛔ 撤。

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python3 verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單端實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單端自倉實跑·雲端 Linux `4` 核·倉外工作樹·殼無 `WV_`·Python `3.11.17`·`shapely 2.2.0`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`（`W-G.9-388` 補令三工項零⁗·快轉自 `fd88f64`）；遠端 heads **`48`**；追蹤檔 `2893`；`app.py` ＝ `3f023996da947e45db08740313921c78f2f9e265`（`1849244` B）；`verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`（`60273` B）；`K-6` 典 ＝ `a3f9d47a34edcb4942a03561c4fa6cd610e8d729`（`859830` B）；自誤簿 ＝ `fb55b127c8121ad98924965dab70ca5b55372738`（`1215603` B·本批⛔ 動）；`docs/待落地清單.md` ＝ `76bc7135a0cf59a9f1a5103cf1db0982184168c0`（`7351` B）；`CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`（本批⛔ 動）；`probe_WG9270_closegate.py 629 623 .` ⇒ `rc 0`（對照 `630 629` ⇒ `rc 7`）；`probe_WG9321_issuer_anchor.py … 629 623` ⇒ `rc 0`（`§零-0` 項 `3` 之值）；基準 ＝ `ops/queue` 之 `基準/929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb.md`（`68` 呼叫皆合期·`pip freeze` `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`）；本批所改之 `7` 器之施前 blob ＝ `§五-1` 項 `2` |
| `2` | 受詞（`929ea20`） | 帶號之 `raise`（AST·字串常數配用語之號）恰 `10`（`§三-1` `R-2` 之列）·皆 `raise RuntimeError(`；吞之處恰 `8`（`R-3` 之表·`F33 wiring` 之 `X2` 於 `929ea20` 實掃：`app.py` `5`〔`:10374`、`:11726`、`:22904`、`:23090`、`:23189`〕、`verify/selection_pipeline.py` `3`〔`:739`、`:861`、`:926`〕·皆⛔ 上拋）；`_try965`：`except RuntimeError as _e: return None, '併入後配地中止：' + str(_e).partition('\n')[0][:200]`；`_chk953`／`_chk_a4`：`if _sa.get('err'): return False, '併入後配地中止：' + str(_sa.get('err'))[:120]`。唯讀審查之窮查：試算之內可達之帶號之停機唯 `GB-104`、`GB-205`；試算之路徑上⛔ 有吞帶號之停機之他之 `except` |
| `3` | 工項一之端（`929ea20` ＋ 塊 `Fy41`·倉外實跑） | 前置 (甲)(乙) 之 `28` 呼叫之 `rc`／末列 ＝ `§五-1` 項 `8` 之工項一之端之列：`F33` 之三呼叫（`#69`〜`#71`）皆 `rc 1`（`#69`／`#71` ＝ `⇒ 紅 ['受詞缺']；rc 1`、`#70` ＝ `⇒ 紅 ['X1', 'X2', 'X3', 'X4']；rc 1`·前態之對照組紅如期）；餘 `25` 呼叫皆 `rc 0`（塊 `Fy41` 所改之 `7` 器於前態皆綠·其許唯增）；耗時之和 `6632` s；諸呼叫之 `stderr` 合計 `0` B；(丙) ＝ 基準之值 |
| `4` | 施後（原型 ＋ 塊 `Fy41`·倉外實跑·⛔ 入倉） | 原型之 `app.py` ＝ `c901b213e70aadbd59320fe9d33a26ca0185c0af`（`50`／`10`）、`verify/selection_pipeline.py` ＝ `e4ab6914ee68b8c3932dd59035c91b6f1b583aa6`（`6`／`0`）——**⛔ 為期**（執行端之碼異則異·唯其行為以 `V-*` 量之）；`§五-1` 項 `8` 之 `71` 呼叫：皆 `rc 0`、末列皆 ＝ 該表之施後之列（`#56`／`#57` 除外·JSON）、`stderr` 合計 `0` B·耗時之和 `11731` s·並行 `2`；`F33 selftest` `K1`〜`K16` 與 `P0 16／16`、`F33 wiring` `X1`〜`X5`、`F33 run` `R1@3.5`／`R1@0.0`（登記 `0`）／`R2@3.5`（上拋：「🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] …」）皆 ✅；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）、`31／31`（`F32`） |
| `5` | 本案之配地（前態 ＝ `929ea20`〔基準之落檔〕·後態 ＝ 原型） | `k6s3 cmp`（基準之落檔 `k6s3_929ea20_*` 對施後之 `k6s3_post_*`）二退縮皆 `rc 0`·末列 `相異 0 項 ⇒ ✅ 同`·`stderr` `0` B；`F8` 之落檔逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`·工項一之端之 `f8_pre_*` 亦同）；`parity` 二退縮之落檔逐位同、`stdout` 以同一字樣代路徑後逐位同；`F33 run` 之 `R1`：harness 之全程之登記二退縮皆 `0` ⇒ **本案之配地⛔ 變** |
| `6` | 量測器之判別力（原型之上之突變·發單端實跑·`F33 selftest`／`wiring`〔`M8` 另 `run 3.5`〕） | 見下之「突變之表」：`15` 突變皆紅；未突變之原型皆綠 |
| `7` | 唯讀獨立審查（一輪·⛔ 參與撰題） | (A)「改配地或違裁示」⛔ 有；WARNING-1（試算之內之無號之完整性之停機仍為不過）⇒ 待落地序 `18`（塊 `P43`）、塊 `K32` 之二之庚；WARNING-2（`GB-104` 於併入街角第 1 宗之後之試算之讀）⇒ 塊 `K32` 之二之己（讀為構造保證之破·上拋·以交付之通知告 KL）；(B) 之瑕之入：`X2` 之三誤綠（死支、他之 mark、lambda）⇒ 改以「`<mark 之名>` 為首引數之 Expr 之句」判之（`M13`／`M14` 證之）；`X1` 放過無號之 `raise k6_program_stop` ⇒ 增判（`M15`）；`K3` 增 `W-GB-1`、`1GB-2`、`GB-12a`；`k6_program_stop` 之 docstring 之折列與變數名；塊 `K32` 之三補引 `parity`。餘（`<where>` 之畫面四處之動態、`P0` 之性、巢狀之內層 `<where>`）⇒ 記之·⛔ 改 |

**突變之表**（每種之所據：(a) 泛用化之目標／(b) 既裁之樣態或自誤之錯／(c) 出錯而變空而照樣亮綠；三法 ①「KL 所否之選項」：本項⛔ 有 KL 之選項〔工程之缺·⛔ 鑄號〕⇒ ⛔ 用；② 換名、鏡射、旋轉 ＝ `F33 selftest` 之 `K9`〜`K12`；③ 邊界 ＝ `K3`〔號之二界〕、`K4`〔新登記之零／一／二〕）：

| 突變 | 所據 | 所改（原型之上） | 紅 |
|---|---|---|---|
| `M1` | (c) | `k6_program_stop` ⛔ 登記（登記恆空 ⇒ 一切上拋⛔ 觸） | selftest `rc 1`·['K1', 'K3', 'K4', 'K5', 'K6', 'K9', 'K10', 'K11', 'K12', 'K13', 'K15', 'K16']；wiring `rc 0`·[] |
| `M2` | (b)（`W-G.9-387` 之偵察：`_try965` 之吞） | `R-3` `1` 之 `k6_trial_raise_since` 去之 | selftest `rc 1`·['K6', 'K9', 'K10', 'K11', 'K12']；wiring `rc 1`·['X2'] |
| `M3` | (b)（同偵察：「`[:120]` 截去其 GB-205 之字樣」） | 登記截為前 `120` 字 | selftest `rc 1`·['K1', 'K16']；wiring `rc 0`·[] |
| `M4` | (a) | `R-3` `1` 之 mark 取於試算之後（處置之內） | selftest `rc 1`·['K6', 'K9', 'K10', 'K11', 'K12']；wiring `rc 1`·['X2'] |
| `M5` | (a) | `k6_program_stop` ⛔ 查其號（無號之訊息亦登記） | selftest `rc 1`·['K2', 'K3']；wiring `rc 0`·[] |
| `M6` | (a)（邊界） | 號之式去其前界（`GB-\d+`） | selftest `rc 1`·['K3']；wiring `rc 0`·[] |
| `M7` | (a) | 上拋新登記之末者（⛔ 首者） | selftest `rc 1`·['K4', 'K5']；wiring `rc 0`·[] |
| `M8` | (a) | `R-3` `7`（harness 之 `_trial_k`）之上拋去之 | selftest `rc 0`·[]；wiring `rc 1`·['X2']；run `rc 1`·['R2@3.5'] |
| `M9` | (b)（`GB-205` 之停機） | `R-2` 之 `_try965` 之 `GB-205` 之句留為 `raise RuntimeError(` | selftest `rc 0`·[]；wiring `rc 1`·['X1'] |
| `M10` | (b)（`K-6` 典之庚：他之配地中止 ⇒ 不過） | `R-3` `1` 之處置改為一律再拋（無號之中止亦停機） | selftest `rc 1`·['K6', 'K7', 'K9', 'K10', 'K11', 'K12', 'K15']；wiring `rc 1`·['X2', 'X3'] |
| `M11` | (c) | `R-3` `2` 之上拋置於 `return` 之後（不可達） | selftest `rc 1`·['K13']；wiring `rc 0`·[] |
| `M12` | (a) | `R-3` `4`（畫面之手冊先行）之上拋去之 | selftest `rc 0`·[]；wiring `rc 1`·['X2'] |
| `M13` | (c)（審查 B-1） | `R-3` `3` 之上拋置於 `if False:` 之內 | selftest `rc 0`·[]；wiring `rc 1`·['X2', 'X3'] |
| `M14` | (c)（審查 B-1） | `R-3` `3` 之上拋之首引數改為 `0`（他之 mark） | selftest `rc 0`·[]；wiring `rc 1`·['X2'] |
| `M15` | (a)（審查 B-2） | 一無號之停機（段三之「build 片 … 不在 temp_parcels」）改經 `k6_program_stop` | selftest `rc 0`·[]；wiring `rc 1`·['X1', 'X3'] |

---

## `§二`　所據之語與射程

🔒 **所據**：`docs/待落地清單.md` 之「……（`W-G.9-387` 入主線；……`W-G.9-388`）」節之序 `7`（「`K-9-61` ④⑤、`GB-205`；試算內之「程式未支援」之停機被吞為「不過」」·落地之單 `W-G.9-389`）；其源 ＝ 發單端擬 `W-G.9-387` 時之偵察（`2026-10-17 14:08`·`ops/queue` 之 `log.md` 該列與 `參考/交接封存_2026-10-18.md` 第 `34` 列·逐字）：

> 5. **試算內之停機被吞**（新發現·`GB` 候登）：`_chk953`（`:15937`）、`_chk_a4`（`:16890`）、`_try965`（`:10374`）於「併入後之試算中止」回「不過」（`W-G.9-363` `R-8` 所定·`K-6` 典 `:5345` 庚「併入後之試算中止 ⇒ 不過（⛔ 停機）」）——其後立之 `GB-205`（`:10383`）等「程式未支援」之停機於試算內觸者被吞為「未成」（且 `[:120]` 截去其「GB-205」之字樣）。387 擬分之：配地上不可（`配地中止`·無從判定）照舊為不過；程式之自我檢查與未支援（`GB-` 之停機）須上拋。須先以本案實跑量其是否已觸（手冊先行／第一趟之紀錄之「不過之由」含「併入後配地中止」者之數·二退縮）。

`K-6` 典之「`K-9-53` ① 之工程讀法」節之庚（`929ea20` 之第 `5325` 列·【工】）：「……併入後之試算中止 ⇒ 不過（⛔ 停機）……」——本單⛔ 改其於「配地上不可」之射程，唯將「程式之停機」（`§三` 用語）自其受詞除之（塊 `K32` 之二之甲）。`GB` 簿 `GB-205`（`W-G.9-380` 立·其「與配地之關係」逐字「觸之 ⇒ 停機（⛔ 靜默）」）。`CLAUDE.md` 之「工作紀律」與 `.claude/skills/no-silent-fallback`（缺值、未支援、未裁 ⇒ 停機·⛔ 靜默）。

🔒 **授權**（自動化之委任·`K-6` 典 `W-G.9-386` 之節之一之 KL 逐字）：KL `2026-10-17 07:23` 第 `3` 點「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目，畢竟討論到現在我覺得已經大多配地的幾何情況、分配成果檢驗機制(R_END,街角地檢驗,內接矩形,若有最小建築面積之檢核,配地要臨FRONTLINE及BASELINE等)及市地重劃扣除負擔之分配精神，已經大致都有說明與你討論過了，所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」；`07:58`「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」。本單 ＝ 待落地清單上之項目（程式之無靜默之缺·⛔ 涉域上之新判·塊 `K32` 之二）。**`expects_allocation_change` ＝ `false`**（`§一` 項 `5`）——執行端之量得本案配地有任一改變 ⇒ 停機款 `6`。

🔒 **【工】之讀法**（塊 `K32` 之二·以交付之通知告 KL）：甲 「程式之停機」之定義（訊息帶 `GB-` 之號或【未裁】）與其由；乙 登記與長度之機制（巢狀之試算以長度分之·⛔ 清）；丙 吞之處八（`§三-1` `R-3`）；丁 末端塊合併再試之試算中止亦上拋；戊 他之配地中止照舊為「不過」。

🔒 **單之分**（工程裁·唯序·⛔ 涉土地後果·塊 `K32` 之四）：待落地清單之序 `7` 分為二——本單（試算內之程式之停機之上拋）與 `W-G.9-390`（`K-9-61` ④⑤ 與 `GB-205` 之還原·同族之還原一單）；原定之 `W-G.9-390`（`K-9-60`）、`W-G.9-391`（`K-9-59`／`K-9-63`）各順延一號。其由：⑤ 之還原之量測須試算內之 `GB-205` 之停機⛔ 被吞（本單先之）；二者之族相異（`發單端.md` 戊「同族之缺陷一單併修」）。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由執行端逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支；`(c)` ⛔ 及主線（入主線另以短單·`§四-2`）、他側支、`data/` 之資料檔、`K-9-61` ④⑤、`GB-205` 之還原（其停機仍為停機·本單唯使其於試算之內⛔ 被吞）、`K-9-59`、`K-9-60`、`K-9-62` 之指配、`K-9-63`、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）。

---

## `§三`　規格（執行端依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**（`929ea20`）：
- 「**程式之停機**」＝ 其訊息之**全文**含 `GB-` 繼以一位以上之數字之號（其前一字⛔ 為英文字母、數字或連字號 `-`；其後一字⛔ 為數字）或「【未裁】」之 `RuntimeError`。其由（塊 `K32` 之二之甲）：`GB` 之號 ＝ 泛用阻塞項（程式未支援之形·其定義即「程式不能判」）；【未裁】＝ 須 KL 裁之形。
- 「**試算**」＝ 為判斷併入之可否、或取一態之配地之量，以宗地之某態跑街角選位與配地（或唯配地）之一次之呼叫（`§三-1` `R-3` 之八處之 `try` 之本體所呼者）。
- 「**吞之處**」＝ 試算之中止（`RuntimeError` 或畫面之代理 st 之 `_K6BTrialStop`）被捕、轉為 `err` 之字串、「不過」、「未成」或「試算中止」之紀錄而續辦之處（`R-3` 之八處·`929ea20` 之列號見其表）。
- 「**登記**」＝ `app.py` 之模組級之串列 `K6_PROGRAM_STOPS`（`R-1`）；「**長度**」＝ 其 `len`。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | 新之頂層（`app.py`·`K917_DROPPED = {}` 之後、`def k917_should_drop` 之前） | 立五名（皆頂層·依此序）：① `K6_PROGRAM_STOPS = []`；② `K6_PROGRAM_STOP_RE` ＝ 以既有之 `re` 編之式，其所配 ＝ 用語之「程式之停機」之號（`GB-` 號之二界依用語·【未裁】逐字）；③ `def k6_program_stop(msg):`——`str(msg)` 之全文⛔ 配 ② ⇒ `raise RuntimeError(…)`（其訊息含 `W-G.9-389`、含所給訊息之前 `200` 字之 `repr`，且其字串常數⛔ 配 ②——⛔ 書「【未裁】」與「`GB-` 繼以數字」之字樣）、⛔ 登記；配 ⇒ 以全文（⛔ 截）附於 ① 之末，回 `RuntimeError(全文)`（⛔ 拋·由呼叫端 `raise` 之）；④ `def k6_trial_mark():` ⇒ 回 ① 之長度；⑤ `def k6_trial_raise_since(mark, where):`——① 之長度 ＞ `int(mark)` ⇒ `raise RuntimeError(f"🔴 [試算內之程式之停機·{where}] {① 之第 int(mark) 項之全文}")`（**首一新登記者**·⛔ 截）；否則回 `None`。① 於任何處⛔ 清、⛔ 刪其項。五名各帶 docstring 或其前之註（形如既有之 `🆕 \`W-G.9-3xx\`` 之註·載其用）。 |
| `R-2` | 帶號之停機之立（`app.py`·`10` 處） | `app.py` 之一切 `raise` 其所拋者之字串常數（含 f-string 之字面部分）配用語之號者，其 `raise RuntimeError(` 改為 `raise k6_program_stop(`（引數與其折列逐字⛔ 動·唯此一換）。`929ea20` 之受詞恰 `10`：`evaluate_parcel_width_n14`（`:7496`·`GB-13`）、`k917_should_drop`（`:9800`·`GB-104`）、`k929_6_fixpoint` 之巢狀 `_try965`（`:10383`·`GB-205`）、`adj_intake`（`:12452`、`:12555`·【未裁】）、`k967_pool_out`（`:14607`、`:14610`·`GB-204`）、`k967_pool_less`（`:14622`、`:14625`·`GB-204`）、`k953_manual_run` 之巢狀 `_gb201_953`（`:16437`·`GB-201`）。 |
| `R-3` | 吞之處（`8` 處） | 每一處：其 `try` 之前（同一區塊；harness 之三處於其 `with` 之前）立 `_m389 = k6_trial_mark()`（harness 以 `ns["k6_trial_mark"]()`）；並依下表之位立 `k6_trial_raise_since(_m389, '<where>')`（harness 以 `ns["k6_trial_raise_since"](…)`），`<where>` 逐字依表；該句之尾得附一註（形如 `# 🆕 \`W-G.9-389\`：…`·⛔ 他列）。 |
| `R-4` | 其餘 | `R-1`〜`R-3` 以外之一字⛔ 動（docstring、註解、他之列·含 `R-2`／`R-3` 所在之函式之他字）；`verify/selection_pipeline.py` 唯 `R-3` 之增列（⛔ 換列、⛔ 刪列）。新增之區域名 ＝ `_m389`（各處同名·⛔ 撞所在函式之既有之名）。 |

**`R-3` 之八處**（`929ea20` 之列號·`<where>` 逐字）：

| # | 檔·函式 | `try` 之所呼 | `k6_trial_raise_since` 之位 | `<where>` |
|---|---|---|---|---|
| `1` | `app.py`·`k929_6_fixpoint` 之巢狀 `_try965`（`:10374`） | `trial(_nb)` | `except RuntimeError as _e:` 之本體之首句（其 `return None, '併入後配地中止：' …` 之前） | `入池閘·併入後之試算` |
| `2` | `app.py`·`end_block_merge_run`（`:11726`） | `alloc_eval(…)` | `except RuntimeError as _e:` 之本體之 `_rec['標的'] = None` 之次句（🔒 `§三-3` 之 `1`：其前二句之相接⛔ 斷） | `末端塊合併再試·試算` |
| `3` | `app.py`·`k6b_screen_callbacks` 之巢狀 `alloc_state`（`:22904`） | `f3_screen_stepg_run(…)` 等 | 該 `try` 之後之首句（其 `_rows = …` 之前） | `段三·畫面之試算` |
| `4` | `app.py`·`f3_screen_k953` 之巢狀之試算（`:23090`） | `f3_screen_stepg_run(…)` | 該 `try` 之後之首句 | `手冊先行·畫面之試算` |
| `5` | `app.py`·`f3_screen_adj4` 之巢狀之試算（`:23189`） | `f3_screen_stepg_run(…)` | 該 `try` 之後之首句 | `第一趟·畫面之試算` |
| `6` | `verify/selection_pipeline.py`·`alloc_state`（`:739`） | `run_step_g(…)` | 其 `with` 之後之首句（其 `_kept, _bad, _G = …` 之前） | `段三·harness 之試算` |
| `7` | `verify/selection_pipeline.py`·`run_k953` 之巢狀 `_trial_k`（`:861`） | `run_step_g(…)` | 其 `with` 之後之首句 | `手冊先行·harness 之試算` |
| `8` | `verify/selection_pipeline.py`·`run_adj4` 之巢狀 `_trial_a4`（`:926`） | `run_step_g(…)` | 其 `with` 之後之首句 | `第一趟·harness 之試算` |

🔒 **⛔ 及之處**（其試算之中止已上拋·⛔ 吞·本單⛔ 動）：段三之 `_noaff`、`K-9-50` 題一 4、步驟 `10` 之 `_cur`、手冊先行之 `C0`／`_chk953` 之併入前、第一趟之 `_S0_a4`／`_chk_a4` 之併入前（皆「無從判定 ⇒ 停機」）；畫面之 `trial_winner`／`alloc_eval`／`_k929_6_screen_gate` 之 `_trial`（`_K6BTrialStop` ⇒ `raise RuntimeError`）；harness 之 `trial_winner`／`alloc_eval`（⛔ 捕）。`_chk953`／`_chk_a4`／`_same953`／`_Lk4` 之「`err` ⇒ 不過」之句⛔ 動：程式之停機於其試算之外殼（`R-3` 之 `3`〜`8`）即上拋，⛔ 至其處。

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F33`（`verify/probes/probe_WG9389_trialstop.py`·新）：`selftest <repo>` 之 `K1`〜`K16` 與 `P0`；`wiring <repo> 929ea20` 之 `X1`〜`X5`；`run <repo>` 之 `R1@3.5`、`R1@0.0`、`R2@3.5`。其所量之名與形：`R-1` 之五名（`X3`：頂層之新名恰此五）；`R-2`（`X1`：帶號之 `raise` 皆 `raise k6_program_stop(`、`k6_program_stop` ⛔ 他用；`X3`：既有之頂層節點之差唯 `raise RuntimeError(` → `raise k6_program_stop(` 之換列與含 `k6_trial_` 之增列）；`R-3`（`X2`：每一吞之處之前有 `… = k6_trial_mark()`、其處置之內或其後之首句呼 `k6_trial_raise_since`；`X4`：`verify/` 頂層唯 `selection_pipeline.py` 異、其差唯含 `k6_trial_` 之增列）；`<where>` 之字樣（`K6`／`K13`／`R2`）。
- `app.py` 之頂層節點對 `929ea20` 相異者 ⊆ `{evaluate_parcel_width_n14, k917_should_drop, k929_6_fixpoint, end_block_merge_run, adj_intake, k967_pool_out, k967_pool_less, k953_manual_run, k6b_screen_callbacks, f3_screen_k953, f3_screen_adj4}`；頂層之名之集 ＝ `929ea20` 之集 ∪ `R-1` 之五名。
- 塊 `Fy41` 所改之既有之器（`7` 檔）：其「頂層之相異之許」「`verify/` 頂層之差之許」增本單之名與增列（各器之 docstring 之末另增一列 `🔧 \`W-G.9-389\`（⛔ 上列一字不刪）：…`）——細目見 `§五-1` 項 `2`。

### `§三-3`　禁改（既有閘之錨·執行端撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計·含註解）——🔒 例：`end_block_merge_run` 之 `"    except RuntimeError as _e:\n        _rec['標的'] = None"`（二句相接）⇒ `R-3` 之 `2` 之句⛔ 置於其間（原型之初稿置於其間而 `W8`／`W7` 紅）；新碼之註解⛔ 複寫既有之錨之字樣；**錨含「縮排之空白 ＋ 中文」之子字串**（例：`'    步'`〔四空白 ＋「步」〕）——新之 docstring、註解之折行⛔ 令一列以四個以上之空白繼以中文起首。基準中恰一之函式名（含巢狀）於工作樹仍恰一 ⇒ 新之頂層名與 `_m389` ⛔ 撞既有之名。執行端撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
2. **突變之錨**（`F13`／`F16`／`F17`／`F23`／`F27`／`F28`／`F29` 之突變）：其錨須仍於其函式內**恰一見**——`R-2`／`R-3` 之句⛔ 照抄既有之句（以子字串計）。
3. **頂層之名之許**：塊 `Fy41` 所改之器之許 ＝ `§三-2` 之集；`R-1` 之五名以外之新頂層名⛔ 立（頂層之輔助函式⛔ 立）。
4. **⛔ 案件字面**（`F33 wiring` 之 `X5`）：`R-1` 之三函式之字串常數⛔ 合 `^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$`。
5. `R-2` 之十處之訊息之字樣⛔ 改（其號、其文·既有之器以之為錨者 `F29`／`F23`／`F27` 等）。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

本單之行為 ＝ 塊 `K32` 之二之【工】之讀法（以交付之通知告 KL·⛔ 涉域上之新判）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地或任一紀錄有任一改變；`R-3` 之八處之外另有吞試算之中止之處（`F33 wiring` 之 `X2` 之計之外）；`R-2` 之十處之外另有帶號之停機（例：訊息由變數組之而 AST 之字面⛔ 見其號者）；某一帶號之停機於本案之試算之外即觸。

### `§三-5`　執行端之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-4`）：落於何處、其字樣；`R-3` 之八處各附其改後之前後三列；對 `§三-3` 各款之自查。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/selection_pipeline.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-389-trialstop`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-389_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-389 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-389-trialstop`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`49`**、主線仍 ＝ `929ea20…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-389-trialstop`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy41` 抽為 `<O>/Fy41.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`8` 檔（`7` 改·`1` 新）之 `git hash-object` ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `8` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-389 工項一：量測器（F33 之新器·F11、F23、F24、F25、F30、F31、F32 之改）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-389-trialstop`。

**工項二　生產碼**（🔴 `app.py`、`verify/selection_pipeline.py`·執行端依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`·`發單端.md` 丙 3之一之三份）：
1. **(甲) 本單新增或修改之量測器之呼叫**（照跑·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`§五-1` 項 `8` 之表之 `#1`, `#2`, `#3`, `#4`, `#5`, `#17`, `#6`, `#13`, `#18`, `#7`, `#19`, `#31`, `#32`, `#33`, `#62`, `#63`, `#64`, `#65`, `#66`, `#69`, `#70`, `#71`（`22` 呼叫·其命令逐字見該表）：`#69` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`#70` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['X1', 'X2', 'X3', 'X4']；rc 1`；`#71` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；其餘 `19` 呼叫 ⇒ `rc 0`·末列 ＝ 該表之同列；諸呼叫之 `stderr` 皆 `0` B。
2. **(乙) 本案配地之前後比對之前態**（照跑）：`python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_pre_35.json`；同 `0.0` ⇒ `<O>/k6s3_pre_00.json`；`python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_pre_35.json`；同 `0.0` ⇒ `<O>/f8_pre_00.json`；`python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_pre.json`；同 `0.0` ⇒ `<O>/parity00_pre.json`（皆 `rc 0`·末列 ＝ `§五-1` 項 `8` 之 `#56`〜`#61` 之工項一之端之列）。
3. **(丙) 本單未動之量測器之呼叫**（`§五-1` 項 `8` 之表之 `#1`〜`#68` 中 (甲)(乙) 以外者）：`§零-0` 項 `6` 之比對皆同（主線之端 ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb` ＝ 基準之 sha、`python3 --version`、`pip freeze` 之 `sha256` ＝ 基準所載）⇒ **沿用** `基準/929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb.md` 之值、⛔ 重跑；任一不同 ⇒ 整份照跑（其期 ＝ 該表之工項一之端之列·皆 `rc 0`）。回報記其比對與所為。
4. `git grep -c -F "<字樣>" -- <檔>`（逐一）：`app.py` 之「raise k6_program_stop(」「k6_trial_raise_since(_m389,」「_m389 = k6_trial_mark()」「K6_PROGRAM_STOPS = []」；`verify/selection_pipeline.py` 之「ns["k6_trial_raise_since"](_m389,」「_m389 = ns["k6_trial_mark"]()」⇒ 各**無出艙**、`rc 1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：執行端依 `§三` 撰寫 `app.py` 與 `verify/selection_pipeline.py` 之改動；`python3 -m py_compile app.py verify/selection_pipeline.py`；`commit` 訊息之首列逐字 `W-G.9-389 工項二：試算內之程式之停機之上拋（帶號之停機之登記·吞之處八之上拋）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>/*_post.*`·🔒 一律從頭整套照跑·⛔ 沿用基準）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy41` 所改、所增之器之呼叫（`22` 呼叫·`§五-1` 項 `8` 之表之 `#1`, `#2`, `#3`, `#4`, `#5`, `#17`, `#6`, `#13`, `#18`, `#7`, `#19`, `#31`, `#32`, `#33`, `#62`, `#63`, `#64`, `#65`, `#66`, `#69`, `#70`, `#71`） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F33 selftest` 之 `K1`〜`K16` 與 `P0`、`F33 wiring` 之 `X1`〜`X5`、`F33 run` 之 `R1@3.5`、`R1@0.0`、`R2@3.5` 皆 ✅ |
| `V-2` | 其餘之呼叫（`§五-1` 之「項 `8` 之表」之 `#1`〜`#68` 中 `V-1` 與 `#56`〜`#61` 以外者·其命令逐字見該表） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` |
| `V-3` | `V-1`〜`V-2` 之器之載入 | 本批所改、所增之器 `8` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_post_35.json`；同 `0.0`；`… cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**） |
| `V-5` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_post.json`；同 `0.0` ⇒ `<O>/parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置 `2` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異） |
| `V-6` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_post_35.json`；同 `0.0` ⇒ `<O>/f8_post_00.json`；`git hash-object <O>/f8_pre_35.json <O>/f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；其增／刪之數與其 blob 出艙（發單端復驗時自倉重算·⛔ 預載）；`verify/` 之他檔對工項一之端相異 `0`；`app.py` 之頂層節點之名之集 ＝ 工項一之端之集 ∪ `R-1` 之五名（AST）；其相異之既有節點 ⊆ `§三-2` 之集 |
| `V-8` | `R-1`〜`R-3` 之字樣（`git grep -c -F "<字樣>" -- <檔>`·逐一） | `app.py`：「raise k6_program_stop(」⇒ `app.py:10`；「k6_trial_raise_since(_m389,」⇒ `app.py:5`；「_m389 = k6_trial_mark()」⇒ `app.py:5`；「K6_PROGRAM_STOPS = []」⇒ `app.py:1`；`verify/selection_pipeline.py`：「ns["k6_trial_raise_since"](_m389,」⇒ `verify/selection_pipeline.py:3`；「_m389 = ns["k6_trial_mark"]()」⇒ `verify/selection_pipeline.py:3`（判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**；逾時之重跑依單首 🔑）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞（試算內之程式之停機）本案⛔ 觸（`§一` 項 `5`），其「⛔ 變」由 `V-4`〜`V-6` 與 `F33 run` 之 `R1` 直接量之。

**唯讀獨立審查**（驗皆符後、推前）：執行端另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：`R-1` 之式（號之二界、【未裁】、⛔ 帶號之訊息之停機、全文⛔ 截、首一新登記者）；`R-2` 之十處（⛔ 漏、⛔ 他字之改）；`R-3` 之八處之位與 `<where>` 之逐字（`end_block_merge_run` 之句之位與 `§三-3` 之 `1`）；吞之處⛔ 漏（試算之路徑之一切 `except` 之續辦者）；`§三-3` 之五款；以獨立之合成之例（`F33` 之外·至少二例：其一 ＝ 手冊先行之併入後之試算觸帶號之停機〔以 harness 之 `run_k953` 之玩具或注入〕；其二 ＝ 試算之內帶號之停機與無號之配地中止相繼〔先無號、後帶號〕）比改前、改後之行為；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ 執行端修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-389-trialstop`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K32` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `P43` 附於 `docs/待落地清單.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；二檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>/checkidx.py`、`<O>/gen_fa_index.py`（⛔ 入倉）。
3. 二塊寫後：`python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-389 工項三：試算內之程式之停機之上拋之讀法入典·待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-389-trialstop`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-389R_試算內之程式之停機之上拋_執行報告.md` ＋ 同目錄之 `W-G.9-389R_試算內之程式之停機之上拋_差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之諸呼叫之全文、`V-5` 之正規化之比與其對照、`V-6` 之 `hash-object` 之出艙、`k6s3 cmp` 之全文、`parity` 之末十五列、前置 (丙) 之版本之比對與所為、`71` 呼叫之 `rc`／`stderr`／耗時／末列之表〔前置與驗二態·沿用者具名·重跑者二趟並載〕）；④ 塊之實得（bytes／`sha256`）與二檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ 執行端之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **`app.py` 與 `verify/selection_pipeline.py` 之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**（並行之數）。收工閘之實測值出艙於回報（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-389 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-389-trialstop`。其後依 `執行端.md` 丁回報於 `ops/queue`。

### `§四-2`　次單（⛔ 本單之期）

發單端復驗本批（自倉從頭重跑 `V-1`〜`V-9` 與收工閘·⛔ 沿用）⇒ 皆符且本案配地⛔ 變 ⇒ **入主線之短單**（快轉 `929ea20` → 新側支之端·⛔ `--force`·自動化之委任之二之甲·前後值入 `ops/queue` 之 `log.md`）＋ 立 `基準/<新主線之全 sha>.md`；其後 `W-G.9-390`（`K-9-61` ④⑤ 與 `GB-205` 之還原）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `probe_WG9351_intake.py` `8`／`4`、`probe_WG9363_k953.py` `5`／`0`、`probe_WG9367_adj4.py` `4`／`0`、`probe_WG9370_adj4mut.py` `5`／`0`、`probe_WG9385_k974.py` `7`／`0`、`probe_WG9387_k961h.py` `10`／`0`、`probe_WG9388_k961s3.py` `12`／`1`、`probe_WG9389_trialstop.py` `662`／`0`（唯此 `8` 檔）（增／刪）；工項二 ＝ `app.py`、`verify/selection_pipeline.py`（唯此二檔·其數出艙·`verify/selection_pipeline.py` 之刪 ＝ `0`）；工項三 ＝ `K-6` 典 `53`／`0`、`docs/待落地清單.md` `20`／`0`（唯此二檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `929ea20` | 生產碼相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；`verify/` 之一切檔相異恰 **`9`**（`M` `8`：`probes/probe_WG9351_intake.py`、`probes/probe_WG9363_k953.py`、`probes/probe_WG9367_adj4.py`、`probes/probe_WG9370_adj4mut.py`、`probes/probe_WG9385_k974.py`、`probes/probe_WG9387_k961h.py`、`probes/probe_WG9388_k961s3.py`、`selection_pipeline.py`；`A` `1`：`probes/probe_WG9389_trialstop.py`）；本批之新檔（本單、新器、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`15` 檔：本單、`8` 器、`app.py`、`verify/selection_pipeline.py`、`K-6` 典、`docs/待落地清單.md`、報告二檔） |
| `4` | 二檔之 bytes | `K-6` 典 `859830` → **`868268`**；`docs/待落地清單.md` `7351` → **`10814`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊；`CLAUDE.md`、自誤簿、`GB` 簿、`VR` 簿、`.claude/` 對 `929ea20` 相異 `0` |
| `5` | 自限 | 遠端 heads **`49`**；主線 ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`（⛔ 變）；`verify/W-G.9-389-trialstop` ＝ 工項四之 `commit`，其祖含 `929ea20`；其餘 `48` 列中除 `ops/queue`（回報後可變）外之 `47` 列（含主線）逐列 ＝ `<O>/heads_before_389.txt` 之同列 |
| `6` | `python3 verify/probes/probe_WG9270_closegate.py 629 623 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 630 629 .` ⇒ `rc 7` |
| `7` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 629 623` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零-0` 項 `3` 之值（⛔ 變） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單端已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單端擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 塊 `Fy41` | `50521` B·`sha256` `3465cb3454435641b1e498dc0c24fc6819e2bb4631feac817610c23e6a6d29b6`·`880` 列（圍欄內全文·末附換行）；抽為 `<O>/Fy41.diff`，`git apply` 於 `verify/probes/` 之 `8` 檔（`7` 改·`1` 新），其施前 blob（B）：`probe_WG9351_intake.py` `eefa02fd805b7e08a54e64c1eae0e025a2051c38`（`34887`）、`probe_WG9363_k953.py` `ccdb11f3a0573c23c91a84e8b35b9735716058cc`（`127230`）、`probe_WG9367_adj4.py` `d76cf9fecab476ece3e3008c5c9727935b62214e`（`73058`）、`probe_WG9370_adj4mut.py` `b1ad31f5983ee0ef9373d4d60e6a23a01287cb47`（`20360`）、`probe_WG9385_k974.py` `8b85294d1d9d5c8e880abaf66b08543829d6e76f`（`42623`）、`probe_WG9387_k961h.py` `594c4cf3339167680a043008caf63113bc4231c3`（`22389`）、`probe_WG9388_k961s3.py` `75411dc5b667199c2429283aa948c850d7b58261`（`39383`）；`probe_WG9389_trialstop.py` 施前⛔ 存 |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K32`／`P43` | 塊 `K32` `8438` B·`sha256` `91350d1a24ad058ec428843e4d784709fb6ea151ad764c1072b9ca3857c4c729`·`53` 列；塊 `P43` `3463` B·`sha256` `fa89ba2932bfe6622e4a9f9e481180501863c90da45118f44f79d32fc41e0dfb`·`20` 列（二者皆圍欄內全文·末附換行·首列為空列）；`K32` 附於 `K-6` 典（`859830` B）之末 ⇒ `868268` B；`P43` 附於 `docs/待落地清單.md`（`7351` B）之末 ⇒ `10814` B |
| `5` | 寫出後之 blob | 工項一之 `8` 器（`verify/probes/`·B）：`probe_WG9351_intake.py` ＝ `43da36a7ce8481fbb5ad3d27b58809719b4396b8`（`35500`）、`probe_WG9363_k953.py` ＝ `468eb1faad6b2ec373829be90e56727898555104`（`127760`）、`probe_WG9367_adj4.py` ＝ `0e10ba31053f1368304817ffb764a0f039bab06f`（`73566`）、`probe_WG9370_adj4mut.py` ＝ `7aa267a87c9a7828d11f6c71b13573ab51655157`（`21032`）、`probe_WG9385_k974.py` ＝ `b44cd02b459b3a254cf8539a254170e9aa6d26f9`（`43431`）、`probe_WG9387_k961h.py` ＝ `4081e384dfa238d287d0604bd0a91e4864bd0ca3`（`23549`）、`probe_WG9388_k961s3.py` ＝ `d731fd350c57b6147d262fc05e568144282c0c58`（`40602`）、`probe_WG9389_trialstop.py` ＝ `da1bd8c5417453a55ab2be2cf6432ebdb2f81ce7`（`33146`·新）；工項三之二檔：`K-6` 典 ＝ `107182948b85fa9ada222ed1e418acc14989e5d6`（`868268` B）、`docs/待落地清單.md` ＝ `69c1bf339ad17e3195ee280da8bcc8d799251a1a`（`10814` B）。🔒 `app.py`／`verify/selection_pipeline.py` 之施後 blob **⛔ 預載**（規格單·由執行端回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-388` 規格單 `§五-1` 項 `7`） |
| `8` | 量測器之二態（發單端實跑·倉外·雲端 Linux `4` 核） | 見本節末之「項 `8` 之表」（`71` 呼叫·二態之 `rc`／`stderr`／末列） |
| `9` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本單>`·發單端實跑（態 `929ea20`·定稿之前一版·其後唯本列與項 `10` 之文字之填）：🔴 機械 `0` 項／🟡 提示 `3` 項——`P-4` 於 `§四-3` 之表之首列（其箭頭為改前至改後之 bytes〔閘 `4`〕）、附錄甲之圍欄之內（`F32` 之增列之註「其後之單之新名…」·非方向之轉引）；`P-6` 於附錄丙之圍欄之內（待落地清單之序之對照「其序 `6` ⇒ 本表序 `6`」·非停機款所繫之數）⇒ **具名豁免**／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23421`–`31163`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單端·⛔ `push`） | `git worktree add --detach <S> 929ea20`（拋棄式·雲端 Linux）＋ 本單（定稿之前一版·其三塊與定稿逐位同）＋ 原型之 `app.py`、`verify/selection_pipeline.py`（代工項二）＋ 報告之替身·五 `commit`：工項零之 blob ＝ 來源；塊 `Fy41` 之抽取 ＝ 項 `2`；`git apply --check` 過；`8` 器之施後 blob ＝ 項 `5`、`git status --porcelain` 唯此 `8` 檔；工項二 ＝ `app.py` `50`／`10`、`verify/selection_pipeline.py` `6`／`0`（原型）·`V-8` 之六字樣 ＝ 期；二檔之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·逐位同；閘 `1` 之五筆之增刪 ＝ 該閘之期（工項零 ＝ 本單之列數／`0`、工項四〔替身〕二檔各 `1`／`0`）·首列 ＝ 所令逐字；閘 `2` ＝ 生產碼相異 `2`、`verify/` 相異 `9`（`M` `8`·`A` `1`）·新檔四之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `15` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `4` 前綴皆真·`CLAUDE.md` 等相異 `0`；閘 `6` `rc 0`（判別力 `630 629` ⇒ `rc 7`）；閘 `7` `rc 0`（四簿 ＝ `§零-0` 項 `3`）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `3`〜`5` 之實跑逐位同（`8` 器 ＝ 項 `5`、`app.py`／`verify/selection_pipeline.py` ＝ 原型） |

**項 `8` 之表**（`#1`〜`#68` ＝ `W-G.9-388` 補令一 `§五″` 之「項 `8` 之表」之命令〔其序同之〕；`#69`〜`#71` ＝ `F33 selftest`／`F33 wiring`／`F33 run`；`#56`〜`#61` 之落檔之名：工項一之端 ⇒ `_pre`、施後 ⇒ `_post`；格 ＝ `rc`／`stderr` B／末列逐字；耗時（s）見括號·⛔ 為期。「工項一之端」之欄：前置 (甲)(乙) 之 `28` 呼叫 ＝ 發單端於 `929ea20` ＋ 塊 `Fy41` 之實跑；其餘 `43` 呼叫 ＝ `基準/929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb.md` 之值〔前置 (丙)·其樹與工項一之端唯塊 `Fy41` 之 `8` 器異、其 `8` 器之呼叫皆入 (甲)〕。「施後」＝ 原型 ＋ 塊 `Fy41`·發單端實跑·並行 `2`）：

| # | 命令 | 工項一之端 | 施後（原型） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（100） | `0`／`0`／`⇒ 紅 []；rc 0`（131） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（546） | `0`／`0`／`⇒ 紅 []；rc 0`（388） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（28） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（28） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·36） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·14） | `0`／`0`／`⇒ 紅 []；rc 0`（14） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·224） | `0`／`0`／`⇒ 紅 []；rc 0`（227） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·69） | `0`／`0`／`⇒ 紅 []；rc 0`（71） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（738） | `0`／`0`／`⇒ 紅 []；rc 0`（458） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1071） | `0`／`0`／`⇒ 紅 []；rc 0`（630） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（12） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（基準·63） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（63） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·414） | `0`／`0`／`⇒ 紅 []；rc 0`（384） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1734） | `0`／`0`／`⇒ 紅 []；rc 0`（1726） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·36） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·6） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（基準·23） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（21） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（14） | `0`／`0`／`⇒ 紅 []；rc 0`（20） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（403） | `0`／`0`／`⇒ 紅 []；rc 0`（236） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（565） | `0`／`0`／`⇒ 紅 []；rc 0`（325） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·34） | `0`／`0`／`⇒ 紅 []；rc 0`（34） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·33） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·6） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·21） | `0`／`0`／`⇒ 紅 []；rc 0`（21） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·14） | `0`／`0`／`⇒ 紅 []；rc 0`（14） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·11） | `0`／`0`／`⇒ 紅 []；rc 0`（10） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·182） | `0`／`0`／`⇒ 紅 []；rc 0`（191） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·47） | `0`／`0`／`⇒ 紅 []；rc 0`（52） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·805） | `0`／`0`／`⇒ 紅 []；rc 0`（862） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·154） | `0`／`0`／`⇒ 紅 []；rc 0`（157） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·99） | `0`／`0`／`⇒ 紅 []；rc 0`（116） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·325） | `0`／`0`／`⇒ 紅 []；rc 0`（352） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（基準·1） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（基準·9） | `0`／`0`／`紅項 [] 器紅 0`（9） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·339） | `0`／`0`／`⇒ 紅 []；rc 0`（362） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（328） | `0`／`0`／`（JSON 之摘要列·略）`（202） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（240） | `0`／`0`／`（JSON 之摘要列·略）`（151） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（332） | `0`／`0`／`⇒ 紅 []；rc 0`（202） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（237） | `0`／`0`／`⇒ 紅 []；rc 0`（146） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（708） | `0`／`0`／`⇒ rc 0（不符 0 項）`（438） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（498） | `0`／`0`／`⇒ rc 0（不符 0 項）`（312） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（547） | `0`／`0`／`⇒ 紅 []；rc 0`（354） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1197） | `0`／`0`／`⇒ 紅 []；rc 0`（1197） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1185） | `0`／`0`／`⇒ 紅 []；rc 0`（1141） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `1`／`0`／`⇒ 紅 ['X1', 'X2', 'X3', 'X4']；rc 1`（217） | `0`／`0`／`⇒ 紅 []；rc 0`（110） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（376） |

**二態之對拍**（發單端·上表之落檔）：`k6s3 cmp` 二退縮皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`·`stderr` `0` B；`F8` 之落檔 `git hash-object` 前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮之落檔逐位同、`stdout` 以同一字樣代路徑後逐位同（發單端之二態同在 `929ea20` 之 `HEAD`·執行端之二態之 `HEAD` 異 ⇒ 依 `V-5` 代之）⇒ **本案配地⛔ 變**。

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丙` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-389-trialstop`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 回報 ⇒ `ops/queue` 之 `reports/W-G.9-389_規格單_回報.md`（`執行端.md` 丁）。

---

## 附錄甲　塊 `Fy41`（`git apply` 之差異·`verify/probes/` 之 `8` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9351_intake.py b/verify/probes/probe_WG9351_intake.py
index eefa02fd805b7e08a54e64c1eae0e025a2051c38..43da36a7ce8481fbb5ad3d27b58809719b4396b8 100644
--- a/verify/probes/probe_WG9351_intake.py
+++ b/verify/probes/probe_WG9351_intake.py
@@ -25,6 +25,8 @@ rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等
   相同者，取重劃前面積之合計較大者，再同取分不到之土地中最小之暫編地號較小者（`k967_rank`·⛔ 停機）——抽出另含
   `k967_rank`、`adj_q2`（`ADJ_DEPS387`）；S6 之期改為重劃前面積較大之街廓；突變 M4（並列⛔ 停機）去之（其錨已去·新碼之判別力
   由 F31 量之）；run 之外部錨（R3）之原街廓依上開三鍵另寫。
+🔧 `W-G.9-389`（試算內之程式之停機之上拋·⛔ 上列一字不刪）：`adj_intake` 之【未裁】之停機改經 `k6_program_stop` ⇒ 抽出另含
+  `k6_program_stop`、`k6_trial_mark`、`k6_trial_raise_since` 與 `K6_PROGRAM_STOPS`／`K6_PROGRAM_STOP_RE`（`ADJ_DEPS389`·存者始取）。
 """
 import ast, contextlib, io, os, re, sys
 
@@ -35,6 +37,7 @@ except Exception:
 
 ADJ_FUNCS = ["adj_intake", "adj_intake_rows"]
 ADJ_DEPS387 = ["k967_rank", "adj_q2"]   # 🔧 `W-G.9-387`：`adj_intake` 所呼之函式（抽出用·⛔ 入 ADJ_FUNCS 之他判）
+ADJ_DEPS389 = ["k6_program_stop", "k6_trial_mark", "k6_trial_raise_since"]   # 🔧 `W-G.9-389`：同（存者始取）
 ADJ_KEYS = ["f3_k929_6_build", "f3_k929_6_dropped"]
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 
@@ -47,14 +50,15 @@ def _read(repo, rel):
 def _extract_ns(src):
     """自 `app.py` 以 AST 抽出 `ADJ_*`／`SS_ADJ_*` 常數與 `adj_*` 函式，於隔離之命名空間執行。"""
     tree = ast.parse(src)
-    parts = []
+    parts = ["import re"]      # 🔧 `W-G.9-389`：`K6_PROGRAM_STOP_RE` 之所需
     for node in tree.body:
-        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS + ADJ_DEPS387:
+        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS + ADJ_DEPS387 + ADJ_DEPS389:
             parts.append(ast.get_source_segment(src, node))
         elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
-                and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
+                and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")
+                     or node.targets[0].id in ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE")):
             parts.append(ast.get_source_segment(src, node))
-    if not parts:
+    if parts == ["import re"]:
         raise KeyError("受詞缺")
     ns = {}
     exec(compile("\n\n".join(parts), "<adj_extract>", "exec"), ns)
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index ccdb11f3a0573c23c91a84e8b35b9735716058cc..468eb1faad6b2ec373829be90e56727898555104 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -1508,6 +1508,11 @@ CHG384_SP = ("run_end_block_merge",)
 KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG384_APP)
 KEEP_SP = tuple(x for x in KEEP_SP if x not in CHG384_SP)
 APP_ALLOW |= {"k971_key5", "k971_blk5"} | set(CHG384_APP)
+# 🔧 `W-G.9-389`（試算內之程式之停機之上拋）：W7 之許增五新名與十一函式（其行為與接線由 F33 量之）
+W389_APP = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
+                "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+                "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+APP_ALLOW |= set(W389_APP)
 SP_ALLOW |= set(CHG384_SP)
 # 🔧 `W-G.9-385`（`K-9-74`／`K-9-79`）：步驟 H 之尺度（`main`）出 W6 之受詞；W7 之許增四新函式、`K974_PARAMS`、
 #   `calc_special_burden_total` 與之（其接線與二函式之唯增列由 F30 之 wiring 量之）
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index d76cf9fecab476ece3e3008c5c9727935b62214e..0e10ba31053f1368304817ffb764a0f039bab06f 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -768,6 +768,10 @@ ALLOW375_SP += ("run_end_block_merge",)
 B5_KW384 = re.compile(r", blk5=[^,()]+\)$")
 # 🔧 `W-G.9-385`（`K-9-74`／`K-9-79`）：W5 之許增四新函式、`K974_PARAMS` 與步驟 H 之尺度所改之二函式（其接線由 F30 之 wiring 量之）
 ALLOW375_APP += ("K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales", "calc_special_burden_total", "main")
+# 🔧 `W-G.9-389`（試算內之程式之停機之上拋）：W5 之許增五新名與十一函式（其行為與接線由 F33 量之）
+ALLOW375_APP += ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
+                "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+                "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
 
 
 def _git_show(repo, rev, rel):
diff --git a/verify/probes/probe_WG9370_adj4mut.py b/verify/probes/probe_WG9370_adj4mut.py
index b1ad31f5983ee0ef9373d4d60e6a23a01287cb47..7aa267a87c9a7828d11f6c71b13573ab51655157 100644
--- a/verify/probes/probe_WG9370_adj4mut.py
+++ b/verify/probes/probe_WG9370_adj4mut.py
@@ -108,6 +108,10 @@ ALLOW373_APP += ("k971_key5", "k971_blk5", "f3_screen_end_block_merge", "f3_scre
 ALLOW373_SP += ("run_end_block_merge", "run_corner_pk_k6b")
 # 🔧 `W-G.9-385`（`K-9-74`／`K-9-79`）：X2 之許增四新函式、`K974_PARAMS` 與步驟 H 之尺度所改之二函式（其接線由 F30 之 wiring 量之）
 ALLOW373_APP += ("K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales", "calc_special_burden_total", "main")
+# 🔧 `W-G.9-389`（試算內之程式之停機之上拋）：X2 之許增五新名與十一函式；X4 之差除含 `k6_trial_` 之增列（其行為與接線由 F33 量之）
+ALLOW373_APP += ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
+                "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+                "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
 
 
 def _strip_fns(src, names):
@@ -305,6 +309,7 @@ def wiring(repo, base):
     s1 = _strip_fns(open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read(),
                     ALLOW373_SP).splitlines()
     d = [x for x in difflib.unified_diff(s0, s1, n=0, lineterm="") if x[:1] in "+-" and x[:3] not in ("+++", "---")]
+    d = [x for x in d if not (x[:1] == "+" and "k6_trial_" in x)]     # 🔧 `W-G.9-389`：其增列（F33 之 X4 量之）
     want = ['-            temp_parcels, build_parcels, ss["t8_ownership_map"]):',
             '-    _own_a4 = ss["t8_ownership_map"]',
             '+            temp_parcels, build_parcels, ss.get("t8_ownership_map", {}) or {}):',
diff --git a/verify/probes/probe_WG9385_k974.py b/verify/probes/probe_WG9385_k974.py
index 8b85294d1d9d5c8e880abaf66b08543829d6e76f..b44cd02b459b3a254cf8539a254170e9aa6d26f9 100644
--- a/verify/probes/probe_WG9385_k974.py
+++ b/verify/probes/probe_WG9385_k974.py
@@ -41,6 +41,7 @@
            R5 模擬：`JUNCTION` 框疊於 `RD1` 之一端 ⇒ 比例之母體扣除之（外部錨）；R6 二欄之結果依檔之 sha256 存 session
            （同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）。
 🔧 `W-G.9-388`（⛔ 上列一字不刪）：W7 之頂層之相異之許增 `k6b_stage3_run`（`K-9-61` ①②③⑥·其行為由 F32 量之）。
+🔧 `W-G.9-389`（⛔ 上列一字不刪）：W7 之頂層之相異之許增試算內之程式之停機之上拋之五新名與十一函式（其行為與接線由 F33 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, os, sys
@@ -52,6 +53,10 @@ except Exception:
 
 NEW_FUNCS = ["k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales"]
 NEW_NAMES = ["K974_PARAMS"] + NEW_FUNCS
+# 🔧 `W-G.9-389`：其後之單之新名與所改之頂層節點（試算內之程式之停機之上拋·其行為與接線由 F33 量之）
+W389_APP = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
+                "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+                "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
 TOL = 1e-9
 
 
@@ -492,7 +497,9 @@ def wiring(repo, base):
                     dels.append((k, hashlib.sha256(ln[2:].encode("utf-8")).hexdigest()))
         # 🔧 `W-G.9-387`：其後之單所改之頂層節點亦許（`adj_intake`·`K-9-61` ⑧·其行為由 F31 量之）
         # 🔧 `W-G.9-388`：同（`k6b_stage3_run`·`K-9-61` ①②③⑥·其行為由 F32 量之）
+        # 🔧 `W-G.9-389`：同（試算內之程式之停機之上拋·F33 量之）
         ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
+               | set(W389_APP)
                and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
         res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
     except Exception as e:
diff --git a/verify/probes/probe_WG9387_k961h.py b/verify/probes/probe_WG9387_k961h.py
index 594c4cf3339167680a043008caf63113bc4231c3..4081e384dfa238d287d0604bd0a91e4864bd0ca3 100644
--- a/verify/probes/probe_WG9387_k961h.py
+++ b/verify/probes/probe_WG9387_k961h.py
@@ -21,6 +21,8 @@
            （⛔ 呼叫 `k967_rank`／`adj_q2`）；R3 每一合併單位之原街廓 ＝ 外部錨 `EXPECT_RUN`（主線 `34736ab` 之
            `probe_WG9351_intake.py run` 之出艙·發單端實跑·舊碼之值）——本案⛔ 遇並列 ⇒ 原街廓⛔ 變。
 🔧 `W-G.9-388`（⛔ 上列一字不刪）：X3 之許增 `k6b_stage3_run`（`K-9-61` ①②③⑥ 之落地·其行為由 F32 量之）。
+🔧 `W-G.9-389`（⛔ 上列一字不刪）：X3 之許增試算內之程式之停機之上拋之五新名（名之集唯增之）與十一函式；X5 之許增
+  `verify/selection_pipeline.py`（其增列·其行為與接線由 F33 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, os, re, subprocess, sys
@@ -33,6 +35,11 @@ except Exception:
 
 FN_AI = "adj_intake"
 EXTRACT_FUNCS = [FN_AI, "adj_intake_rows", "k967_rank", "adj_q2"]
+# 🔧 `W-G.9-389`：其後之單之新名與所改之頂層節點（試算內之程式之停機之上拋·F33 量之）
+NEW389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since")
+W389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
+            "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+            "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 # 外部錨（R3）：主線 `34736ab` 之 `probe_WG9351_intake.py run <repo>` 之「單位」列之原街廓（發單端 2026-10-17 實跑）
 EXPECT_RUN = {
@@ -262,6 +269,8 @@ def wiring(repo, base):
         bt, ct = _top(bsrc), _top(src)
         dif = sorted(k for k in set(bt) | set(ct) if bt.get(k) != ct.get(k))
         ok3 = set(bt) == set(ct) and set(dif) <= {FN_AI} | {"k6b_stage3_run"}    # 🔧 `W-G.9-388`：其後之單所改者亦許（F32 量之）
+        ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) and set(bt) <= set(ct)
+                      and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389))   # 🔧 `W-G.9-389`：同（F33 量之）
         res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", ok3,
                     f"增 {sorted(set(ct) - set(bt))}／去 {sorted(set(bt) - set(ct))}／相異 {dif}"))
         ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
@@ -277,6 +286,7 @@ def wiring(repo, base):
                 c = None
             if b != c:
                 chg.append(p)
+        chg = [p for p in chg if p != "verify/selection_pipeline.py"]   # 🔧 `W-G.9-389`：其增列（F33 之 X4 量之）
         res.append((f"X5 生產碼 app.py 以外之 {len(prod)} 檔對基準相異 0", not chg and len(prod) >= 1, f"相異 {chg}"))
     except Exception as e:  # noqa: BLE001
         res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", False, f"基準讀不到：{type(e).__name__}"))
diff --git a/verify/probes/probe_WG9388_k961s3.py b/verify/probes/probe_WG9388_k961s3.py
index 75411dc5b667199c2429283aa948c850d7b58261..d731fd350c57b6147d262fc05e568144282c0c58 100644
--- a/verify/probes/probe_WG9388_k961s3.py
+++ b/verify/probes/probe_WG9388_k961s3.py
@@ -32,10 +32,18 @@ KL 裁 `2026-10-06 01:29`；`2026-10-18 08:03`〔問二 ＝ 手冊道路用地
            之停機仍在；X2 `_recv_of` 之形 ＝ `def _recv_of(b, y):`，其呼叫皆二引數；X3 app.py 之頂層節點對基準之相異 ＝
            `{k6b_stage3_run}`、頂層之名之集⛔ 變；X4 `k6b_stage3_run` 內⛔ 案件字面；X5 `verify/` 之 `*.py`（頂層）對基準
            逐位同。
+🔧 `W-G.9-389`（⛔ 上列一字不刪）：X3 之許增試算內之程式之停機之上拋之五新名（名之集唯增之）與十一函式；X5 之許增
+           `verify/selection_pipeline.py`（其增列·其行為與接線由 F33 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, os, re, subprocess, sys
 
+# 🔧 `W-G.9-389`：其後之單之新名與所改之頂層節點（試算內之程式之停機之上拋·F33 量之）
+NEW389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since")
+W389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
+            "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+            "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+
 try:
     sys.stdout.reconfigure(encoding="utf-8")
 except Exception:  # noqa: BLE001
@@ -514,6 +522,9 @@ def wiring(repo, base):
     ta, tb = _top(app), _top(old)
     diff = sorted(k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k))
     ok3 = diff == ["k6b_stage3_run"] and set(ta) == set(tb)
+    # 🔧 `W-G.9-389`：其後之單之新名（名之集唯增之）與所改之頂層節點亦許（F33 量之）
+    ok3 = ok3 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW389) and set(tb) <= set(ta)
+                  and set(diff) <= {"k6b_stage3_run"} | set(W389))
     print(("  ✅" if ok3 else "  🔴") + f" X3 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
     if not ok3:
         red.append("X3")
@@ -523,7 +534,7 @@ def wiring(repo, base):
     if lits:
         red.append("X4")
     ch = [l for l in _git(repo, "diff", "--name-only", base, "--", "verify/").splitlines()
-          if l.count("/") == 1 and l.endswith(".py")]
+          if l.count("/") == 1 and l.endswith(".py") and l != "verify/selection_pipeline.py"]   # 🔧 `W-G.9-389`：其增列（F33 量之）
     print(("  ✅" if not ch else "  🔴") + f" X5 verify/ 頂層之 *.py 對基準逐位同（異 {ch}）")
     if ch:
         red.append("X5")
diff --git a/verify/probes/probe_WG9389_trialstop.py b/verify/probes/probe_WG9389_trialstop.py
new file mode 100644
index 0000000000000000000000000000000000000000..da1bd8c5417453a55ab2be2cf6432ebdb2f81ce7
--- /dev/null
+++ b/verify/probes/probe_WG9389_trialstop.py
@@ -0,0 +1,662 @@
+# -*- coding: utf-8 -*-
+"""W-G.9-389 量測器（發單端擬·檔 F33·⛔ 由受單側改一字）：試算內之程式之停機之上拋。
+
+所量之性質：程式之停機（訊息帶 `GB-` 之號或【未裁】者）於試算（街角定案、併入之前後之配地）之內觸之者，⛔ 判為
+  「不過」「未成」「試算中止」而續辦——其訊息之全文上拋（配地停機·loud）；他之試算中止（配地上不可）照舊為「不過」。
+  機制：`app.py` 之 `k6_program_stop`（登記於 `K6_PROGRAM_STOPS` 並回 `RuntimeError`）、`k6_trial_mark`、
+  `k6_trial_raise_since`；吞試算之中止之處，於試算之前取其長度、其後見有新登記者即上拋。
+
+子命令（一律 python3 verify/probes/probe_WG9389_trialstop.py <子命令> …）：
+  selftest <repo>
+           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取三函式、`k929_6_fixpoint`、`end_block_merge_run`；入池閘之玩具
+           借 F29〔`probe_WG9375_k965.py`〕之 `ToyLate`／`mk`／`BLK`，另以前緣線之軸定推進序〔`ToyAxis`·供旋轉、鏡射〕）：
+           K1〜K16（期值皆手算·見各例之註）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
+  wiring   <repo> <基準 commit>
+           AST 查接線：X1 `app.py` 之 `raise` 其字串常數帶 `GB-\\d+`／【未裁】者皆為 `raise k6_program_stop(…)`，
+           `raise k6_program_stop(…)` 之訊息皆帶號，`k6_program_stop` ⛔ 他用；X2 `app.py` 與 `verify/selection_pipeline.py` 之每一 `try`——其本體呼叫試算
+           （`f3_screen_stepg_run`／`run_step_g`／`trial`／`alloc_eval`）而有吞 `RuntimeError`／`_K6BTrialStop`／`Exception`
+           之處置（其本體無 `raise`）者——其前之同一區塊（或其所屬之 with 之區塊）以 `<名> = k6_trial_mark()` 取 mark，
+           且其每一吞之處置之本體之某句、或其後之首句，即 `k6_trial_raise_since(<該名>, …)` 之句（⛔ 於 if／lambda 之內）；X3 新頂層之名 ＝ 五；`app.py` 之頂層節點對基準之相異 ⊆ 本單之許，其差唯
+           `raise RuntimeError(`→`raise k6_program_stop(` 之換與含 `k6_trial_` 之增列；X4 `verify/` 頂層之 `*.py` 對基準
+           唯 `selection_pipeline.py` 異、其差唯含 `k6_trial_` 之增列；X5 三函式內⛔ 案件字面。
+  run      <repo> [<退縮> …]
+           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 街角選位至配地（`run_corner_pk_k6b` ＋ `run_step_g`）⛔ 停機、
+           且 `K6_PROGRAM_STOPS` 終為空（本案之一切試算⛔ 觸程式之停機 ⇒ 上拋之機制⛔ 觸 ⇒ 配地⛔ 變）；
+           R2（唯首一退縮）注入：手冊先行之內，入池閘自其第 2 次之呼叫起立程式之停機（`GB-999`）⇒ 須上拋至
+           `run_corner_pk_k6b`（訊息含 `GB-999` 與「試算內之程式之停機·手冊先行」）·⛔ 判為不過而續辦。
+rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
+"""
+import ast, contextlib, copy, difflib, io, math, os, re, subprocess, sys
+
+try:
+    sys.stdout.reconfigure(encoding="utf-8")
+except Exception:
+    pass
+
+FNS = ["k6_program_stop", "k6_trial_mark", "k6_trial_raise_since"]
+NEW_TOP = {"K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since"}
+# 本單之許（app.py 之頂層節點·其差唯 X3 之二形）
+ALLOW = {"evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
+         "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953",
+         "f3_screen_adj4"}
+TAG_RE = re.compile(r"(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】")
+TRIAL_CALLS = {"f3_screen_stepg_run", "run_step_g", "trial", "alloc_eval"}
+CATCH = {"RuntimeError", "_K6BTrialStop", "Exception"}
+CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
+
+
+def _harvest(repo):
+    sys.path.insert(0, os.path.join(repo, "verify"))
+    from app_harvest import harvest
+    with contextlib.redirect_stdout(io.StringIO()):
+        ns, fake_st = harvest(os.path.join(repo, "app.py"))
+    return ns, fake_st
+
+
+def _f29(repo):
+    sys.path.insert(0, os.path.join(repo, "verify", "probes"))
+    import probe_WG9375_k965 as F29
+    return F29
+
+
+# ───────────────────────── selftest ─────────────────────────
+
+def _toy_axis(F29):
+    class ToyAxis(F29.ToyLate):
+        """F29 之 ToyLate，而推進序依各街廓之前緣線之軸（p1→p2）之投影（⛔ 依 x）；`stop` ＝ (成員之集, 種類)：
+        build 含某單元之成員 ⊇ 所指者 ⇒ 試算立停機（種類 'prog' ＝ 程式之停機〔k6_program_stop〕；'plain' ＝ 配地中止）。"""
+
+        def __init__(self, blocks, fl, ns, stop=None, tag="GB-999 玩具"):
+            super().__init__(blocks)
+            self.fl, self.ns, self.stop, self.tag, self.hits = fl, ns, stop, tag, 0
+
+        def trial(self, build):
+            from shapely.geometry import Polygon
+            if self.stop is not None:
+                need, kind = self.stop
+                if any(frozenset(t.get("入池閘併入") or [t["暫編地號"]]) >= frozenset(need) for t in build):
+                    self.hits += 1
+                    if kind == "prog":
+                        raise self.ns["k6_program_stop"](f"🔴 [{self.tag}] 試算內之程式之停機（合成）")
+                    raise RuntimeError("🔴 [玩具] 配地中止（合成·⛔ 帶號）")
+            rows, dropped = [], {}
+            for blk, P in self.blocks.items():
+                (x1, y1), (x2, y2) = self.fl[blk]["p1"], self.fl[blk]["p2"]
+                L = math.hypot(x2 - x1, y2 - y1)
+                ux, uy = (x2 - x1) / L, (y2 - y1) / L
+                ps = [t for t in build if t["所屬街廓"] == blk]
+                pr = {}
+                for t in ps:
+                    q = Polygon(t["polygon_coords"]).centroid
+                    pr[t["暫編地號"]] = (q.x - x1) * ux + (q.y - y1) * uy
+                left = sorted([t for t in ps if pr[t["暫編地號"]] < P["split_x"]], key=lambda t: pr[t["暫編地號"]])
+                right = sorted([t for t in ps if pr[t["暫編地號"]] >= P["split_x"]], key=lambda t: -pr[t["暫編地號"]])
+                sumg = 0.0
+                for side, grp in (("left", left), ("right", right)):
+                    p = 0
+                    for t in grp:
+                        k = t["暫編地號"]
+                        a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
+                        corner = k in P["corner"]
+                        g = a * F29.RHO - (P["burden"] if (p == 0 and not corner) else 0.0)
+                        if not corner and g < P["m"]:
+                            dropped.setdefault((blk, side), []).append({"暫編地號": k, "G(㎡)": round(g, 4)})
+                            continue
+                        rows.append({"暫編地號": k, "所屬街廓": blk, "推進側別": side, "G(㎡)": round(g, 4),
+                                     "驗_宗序": "街角第1宗" if corner else "其後", "驗_總判": "保留"})
+                        sumg += g
+                        p += 1
+                w = max(0.01, (P["cap"] - sumg) / P["depth"])
+                rows.append({"暫編地號": f"{blk}-抵費地", "所屬街廓": blk, "推進側別": "抵費地", "G(㎡)": 0,
+                             "cut_coords": F29.rect(0, w, 0, P["depth"])})
+            return rows, dropped, None
+    return ToyAxis
+
+
+def _xf(pt, T):
+    # T ＝ (θ 度, 鏡射與否, 平移 (dx, dy))：先鏡射（x → −x）、次旋轉、再平移
+    th, mir, (dx, dy) = T
+    x, y = pt
+    if mir:
+        x = -x
+    c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
+    return (x * c - y * s + dx, x * s + y * c + dy)
+
+
+def _world(F29, T=(0.0, False, (0.0, 0.0)), names=None):
+    """示範街廓（F29 K6 之形）：街廓 A·前緣線 p1(0,0)→p2(30,0)·三宗由 p1 往 p2 依序：
+    C（歸戶甲·分攤 300·街角第 1 宗）、X（歸戶甲·60）、Z（歸戶丙·400）。玩具：G ＝ a × 0.6；各側首宗減側街負擔 9（街角
+    第 1 宗免、恆配地）；最小分配 100。手算：C 180；X 於 C 之後 36 ＜ 100 ⇒ 不配地；Z 240。入池閘：X 與同街廓同歸戶之
+    街角第 1 宗 C 相連 ⇒ ⛔ 合併、依手冊併入 C（`K-9-58` ①·併入之後試算以檢核之）⇒ 單元 C{C, X}：a ＝ 360 ⇒ 216。
+    `names` ＝ 換名之表（暫編地號、原地號、街廓、歸戶）。"""
+    n = dict(X="X", C="C", Z="Z", A="A", o1="o1", oc="oc", o9="o9", 甲="GA", 丙="GZ")
+    n.update(names or {})
+    b = [F29.mk(n["C"], n["oc"], n["A"], 300, 0, 10), F29.mk(n["X"], n["o1"], n["A"], 60, 10, 20),
+         F29.mk(n["Z"], n["o9"], n["A"], 400, 20, 30)]
+    for t in b:
+        cs = [_xf(c, T) for c in t["polygon_coords"]]
+        if T[1]:
+            cs = cs[::-1]
+        t["polygon_coords"] = cs
+    p1, p2 = _xf((0.0, 0.0), T), _xf((30.0, 0.0), T)
+    own = {n["oc"]: n["甲"], n["o1"]: n["甲"], n["o9"]: n["丙"]}
+    return b, own, {n["A"]: F29.BLK(split_x=1000.0, corner={n["C"]})}, {n["A"]: {"p1": p1, "p2": p2}}, n
+
+
+def _run_world(ns, F29, Toy, T=(0.0, False, (0.0, 0.0)), names=None, stop_kind=None):
+    b, own, blocks, fl, n = _world(F29, T, names)
+    toy = Toy(blocks, fl, ns, stop=((n["X"], n["C"]), stop_kind) if stop_kind else None)
+    kw = dict(temp_parcels=b, cat_of={k: "住宅區" for k in blocks}, front_rows={k: {"正面路寬(m)": 8} for k in blocks})
+    try:
+        bf, out, log = ns["k929_6_fixpoint"](b, toy.trial, own, {"z1": 1.0}, fl, **kw)
+    except RuntimeError as e:
+        return {"停機": str(e), "hits": toy.hits}, n
+    s = F29._summ(bf, out, log)
+    return {"alloc": s["alloc"], "units": s["units"], "drops": s["drops"], "hits": toy.hits}, n
+
+
+def _canon(res, n):
+    # 名之還原（換名之例與原例比）
+    inv = {v: k for k, v in n.items()}
+    if "停機" in res:
+        return {"停機含號": bool(TAG_RE.search(res["停機"])), "hits≥1": res["hits"] >= 1}
+    return {"alloc": {inv.get(k, k): v for k, v in res["alloc"].items()},
+            "units": {inv.get(k, k): sorted(inv.get(m, m) for m in v) for k, v in res["units"].items()},
+            "drops": sorted(inv.get(k, k) for k in res["drops"]), "hits": res["hits"]}
+
+
+def cases(ns, F29):
+    C = []
+    STOPS = ns["K6_PROGRAM_STOPS"]
+    ps, mark, since = ns["k6_program_stop"], ns["k6_trial_mark"], ns["k6_trial_raise_since"]
+
+    # K1 登記之全文：長訊（號在第 1500 字之後）⇒ 回 RuntimeError（⛔ 拋）·登記 ＋1·全文逐字（`自誤`／387 之註：截去號之誤）
+    m0 = len(STOPS)
+    long = "🔴 " + "長" * 1500 + "（GB-205）⇒ 停機"
+    e = ps(long)
+    C.append(("K1 程式之停機：回 RuntimeError·登記全文（⛔ 截）",
+              (type(e).__name__, str(e) == long, len(STOPS) - m0, (STOPS[-1] if STOPS else None) == long), ("RuntimeError", True, 1, True)))
+    # K2 ⛔ 帶號之訊息 ⇒ 停機（⛔ 登記）
+    m0 = len(STOPS)
+    try:
+        ps("🔴 一般之配地中止")
+        got = ("未停機", len(STOPS) - m0)
+    except RuntimeError as e2:
+        got = ("W-G.9-389" in str(e2), len(STOPS) - m0)
+    C.append(("K2 ⛔ 帶號 ⇒ 停機、⛔ 登記", got, (True, 0)))
+    # K3 邊界：號之前接英字（`XGB-12`、`MGB-1`）、連字號（`W-GB-1`）、數字（`1GB-2`）⇒ ⛔ 號；無數字（`GB-`）⇒ ⛔ 號；
+    #     數字後接英字（`GB-12a`）⇒ 號；【未裁】單獨 ⇒ 號
+    res = []
+    for s_ in ("XGB-12 停機", "GB- 停機", "(GB-13)", "【未裁】", "GB-2050", "·GB-201：", "MGB-1", "W-GB-1", "1GB-2",
+               "GB-12a"):
+        m0 = len(STOPS)
+        try:
+            ps(s_)
+            res.append((s_, len(STOPS) - m0))
+        except RuntimeError:
+            res.append((s_, "停"))
+    C.append(("K3 號之邊界（前接英數或連字號者⛔ 號；無數字者⛔ 號）", res,
+              [("XGB-12 停機", "停"), ("GB- 停機", "停"), ("(GB-13)", 1), ("【未裁】", 1), ("GB-2050", 1),
+               ("·GB-201：", 1), ("MGB-1", "停"), ("W-GB-1", "停"), ("1GB-2", "停"), ("GB-12a", 1)]))
+    # K4 零／一／二：mark 之後無新登記 ⇒ ⛔ 拋；一 ⇒ 拋其全文；二 ⇒ 拋其首者
+    k0 = mark()
+    try:
+        since(k0, "例")
+        z = "⛔ 拋"
+    except RuntimeError as e3:
+        z = str(e3)
+    ps("🔴 甲 GB-1")
+    try:
+        since(k0, "例")
+        o = "⛔ 拋"
+    except RuntimeError as e4:
+        o = str(e4)
+    ps("🔴 乙 GB-2")
+    try:
+        since(k0, "例")
+        t2 = "⛔ 拋"
+    except RuntimeError as e5:
+        t2 = str(e5)
+    C.append(("K4 新登記 零／一／二 ⇒ ⛔ 拋／拋其全文／拋其首者",
+              (z, o.endswith("🔴 甲 GB-1") and "例" in o, t2.endswith("🔴 甲 GB-1")), ("⛔ 拋", True, True)))
+    # K5 巢狀：外 mark → 登記 A → 內 mark → 登記 B ⇒ 內見 B、外見 A
+    k_out = mark()
+    ps("🔴 A GB-3")
+    k_in = mark()
+    ps("🔴 B GB-4")
+    got5 = []
+    for k_ in (k_in, k_out):
+        try:
+            since(k_, "巢")
+            got5.append("⛔ 拋")
+        except RuntimeError as e6:
+            got5.append(str(e6).split("] ", 1)[1])
+    C.append(("K5 巢狀之試算以長度分之", got5, ["🔴 B GB-4", "🔴 A GB-3"]))
+
+    Toy = _toy_axis(F29)
+    T0 = (0.0, False, (0.0, 0.0))
+    # K6 入池閘：依手冊併入後之試算（檢核）立程式之停機 ⇒ 上拋（含號）·⛔ 判為不過（手算：C{C,X} 之試算觸之）
+    r6, _n6 = _run_world(ns, F29, Toy, T0, stop_kind="prog")
+    C.append(("K6 入池閘之併入後之試算立程式之停機 ⇒ 上拋",
+              ("停機" in r6 and "GB-999 玩具" in r6["停機"] and "試算內之程式之停機·入池閘" in r6["停機"], r6["hits"]),
+              (True, 1)))
+    # K7 對照：同形而為配地中止（⛔ 帶號）⇒ 照舊：整筆之併入判為不過 ⇒ 依 `K-9-66` 按比例（`0.01 ㎡` 之格·玩具唯整筆之
+    #     單元觸之）⇒ 併入 59.99 ⇒ C (300 ＋ 59.99) × 0.6 ＝ 215.994 → 215.99；X 剩 0.01 不配地；⛔ 單元；Z 240
+    r7, n7 = _run_world(ns, F29, Toy, T0, stop_kind="plain")
+    EXP7 = {"alloc": {"C": 215.99, "Z": 240.0}, "units": {}, "drops": ["X"], "hits": 1}
+    C.append(("K7 對照：配地中止（⛔ 帶號）⇒ 照舊為不過", _canon(r7, n7), EXP7))
+    # K8 無停機之形（基底）：X 依手冊併入 C ⇒ C{C,X} 216、Z 240（同 F29 K6）
+    r8, n8 = _run_world(ns, F29, Toy, T0)
+    EXP8 = {"alloc": {"C": 216.0, "Z": 240.0}, "units": {"C": ["C", "X"]}, "drops": [], "hits": 0}
+    C.append(("K8 基底（無停機）：X 依手冊併入街角第 1 宗 C", _canon(r8, n8), EXP8))
+    # K9〜K12 換名、鏡射、旋轉（實座標之尺度 TWD97·任意角）：K6〜K8 之果除名稱外皆同
+    NM = dict(X="甲-01", C="甲-00", Z="丙-07", A="B-東", o1="1001-1", oc="1001", o9="1009-3", 甲="H甲", 丙="H丙")
+    for nm, T, names in (("K9 換名", T0, NM), ("K10 鏡射", (0.0, True, (0.0, 0.0)), None),
+                         ("K11 旋轉 37°·TWD97", (37.0, False, (302511.37, 2652874.91)), None),
+                         ("K12 鏡射 ＋ 旋轉 213°·TWD97·換名", (213.0, True, (302511.37, 2652874.91)), NM)):
+        gs = []
+        for sk in ("prog", "plain", None):
+            r_, n_ = _run_world(ns, F29, Toy, T, names, stop_kind=sk)
+            gs.append(_canon(r_, n_))
+        C.append((f"{nm}：K6／K7／K8 之果除名稱外同", gs,
+                  [{"停機含號": True, "hits≥1": True}, EXP7, EXP8]))
+    # K13 末端塊合併再試：試算立程式之停機 ⇒ 上拋（⛔ 記為試算中止）
+    def _ae_prog(t, b):
+        raise ps("🔴 [GB-998 玩具] 末端塊之試算內之程式之停機")
+
+    def _ae_plain(t, b):
+        raise RuntimeError("🔴 [玩具] 末端塊之試算之配地中止")
+    EBM = ns["end_block_merge_run"]
+    try:
+        EBM([], [], {}, set(), set(), {}, {}, None, _ae_prog, None, setback=3.5)
+        g13 = "⛔ 拋"
+    except RuntimeError as e7:
+        g13 = ("GB-998 玩具" in str(e7), "試算內之程式之停機·末端塊合併再試" in str(e7))
+    C.append(("K13 末端塊合併再試之試算立程式之停機 ⇒ 上拋", g13, (True, True)))
+    # K14 對照：配地中止 ⇒ 照舊（標的 None·記其由）
+    try:
+        _t, _b, _l, rec = EBM([], [], {}, set(), set(), {}, {}, None, _ae_plain, None, setback=3.5)
+        g14 = (rec.get("標的"), "末端塊之試算之配地中止" in str(rec.get("試算中止")), _l)
+    except RuntimeError as e8:
+        g14 = ("拋", str(e8)[:80])
+    C.append(("K14 對照：末端塊之試算之配地中止 ⇒ 照舊記試算中止", g14, (None, True, [])))
+    # K15 先前之登記（試算之前已在）⇒ ⛔ 致其後之試算上拋（以長度分之）：K1〜K5 所留之登記在，K7 仍照舊
+    C.append(("K15 試算之前之登記⛔ 波及（K7 於 K1〜K5 之登記之後）", len(STOPS) > 0 and _canon(r7, n7) == EXP7, True))
+    # K16 程式之停機上拋時，訊息之全文（含號之後之字）⛔ 截：長訊之號在第 1500 字之後
+    m0 = mark()
+    ps(long)
+    try:
+        since(m0, "長")
+        g16 = "⛔ 拋"
+    except RuntimeError as e9:
+        g16 = str(e9).endswith(long)
+    C.append(("K16 上拋之訊息為全文（號在 1500 字之後）", g16, True))
+    return C
+
+
+def selftest(repo):
+    try:
+        ns, _ = _harvest(repo)
+        F29 = _f29(repo)
+    except Exception as e:  # noqa: BLE001
+        print(f"  🔴 受詞之取得中止：{type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
+        print("⇒ 紅 ['受詞缺']；rc 1")
+        return 1
+    miss = [f for f in FNS + ["K6_PROGRAM_STOPS", "k929_6_fixpoint", "end_block_merge_run"] if f not in ns]
+    if miss:
+        print(f"  🔴 受詞缺 {miss}")
+        print("⇒ 紅 ['受詞缺']；rc 1")
+        return 1
+    ns["get_min_lot_size"] = lambda cat, w: {"min_width": 3.0, "min_depth": 10.0}
+    ns["_rect_fits_free_pose"] = lambda P, W, D, *a, **k: (P.bounds[2] - P.bounds[0]) >= W - 1e-9
+    red = []
+    try:
+        C = cases(ns, F29)
+    except Exception as e:  # noqa: BLE001
+        print(f"  🔴 例之執行中止：{type(e).__name__}：{str(e).splitlines()[0][:300] if str(e) else ''}")
+        print("⇒ 紅 ['執行中止']；rc 1")
+        return 1
+    for name, got, exp in C:
+        ok = got == exp
+        print(("  ✅ " if ok else "  🔴 ") + name)
+        if not ok:
+            print(f"       得 {got!r}"[:600])
+            print(f"       期 {exp!r}"[:600])
+            red.append(name.split()[0])
+    base = {j for j, (_, g2, e2) in enumerate(C) if g2 != e2}
+    p0 = 0
+    for i in range(len(C)):
+        bad = {j for j, (_, g2, e2) in enumerate(C) if g2 != (("擾動", e2) if j == i else e2)}
+        if bad == base | {i}:
+            p0 += 1
+    ok0 = p0 == len(C)
+    print(("  ✅ " if ok0 else "  🔴 ") + f"P0 判式自驗 {p0}／{len(C)}")
+    if not ok0:
+        red.append("P0")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+# ───────────────────────── wiring ─────────────────────────
+
+def _read(repo, rel):
+    with open(os.path.join(repo, rel), encoding="utf-8") as f:
+        return f.read()
+
+
+def _git_show(repo, base, rel):
+    return subprocess.run(["git", "-C", repo, "show", f"{base}:{rel}"], capture_output=True,
+                          check=True).stdout.decode("utf-8")
+
+
+def _consts(node):
+    return "".join(c.value for c in ast.walk(node) if isinstance(c, ast.Constant) and isinstance(c.value, str))
+
+
+def _callname(c):
+    f = c.func
+    if isinstance(f, ast.Name):
+        return f.id
+    if isinstance(f, ast.Attribute):
+        return f.attr
+    if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant) and isinstance(f.slice.value, str):
+        return f.slice.value     # ns["名"](…)
+    return None
+
+
+def _x1(tree):
+    bad, n_ok, other = [], 0, []
+    raises = set()
+    for n in ast.walk(tree):
+        if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call):
+            raises.add(id(n.exc))
+            if TAG_RE.search(_consts(n.exc)):
+                if _callname(n.exc) == "k6_program_stop":
+                    n_ok += 1
+                else:
+                    bad.append(n.lineno)
+            elif _callname(n.exc) == "k6_program_stop":
+                bad.append(n.lineno)          # ⛔ 帶號之訊息而經 k6_program_stop
+    for n in ast.walk(tree):
+        if isinstance(n, ast.Call) and _callname(n) == "k6_program_stop" and id(n) not in raises:
+            other.append(n.lineno)
+    return n_ok, bad, other
+
+
+def _blocks_of(tree):
+    # 每一語句之串列與其所屬之語句（函式之本體、if／for／while／with／try 之各支·處置之本體）→ [(串列, 所屬)]
+    out = []
+    for n in ast.walk(tree):
+        for fld in ("body", "orelse", "finalbody"):
+            v = getattr(n, fld, None)
+            if isinstance(v, list) and v and all(isinstance(s, ast.stmt) for s in v):
+                out.append((v, n))
+        if isinstance(n, ast.Try):
+            for h in n.handlers:
+                out.append((h.body, h))
+    return out
+
+
+def _catches(h):
+    t = h.type
+    if t is None:
+        return True
+    names = [t] if not isinstance(t, ast.Tuple) else list(t.elts)
+    return any((isinstance(x, ast.Name) and x.id in CATCH) for x in names)
+
+
+def _calls_in(nodes, names):
+    return any(isinstance(c, ast.Call) and _callname(c) in names for s in nodes for c in ast.walk(s))
+
+
+def _x2(tree):
+    """吞試算之中止之處：其前（同一串列、或其所屬之 with 之串列）有 `_m = k6_trial_mark()`；其每一吞之處置之內呼叫
+    `k6_trial_raise_since`，或 try（連同其所屬之 with·該 with 之本體以之為末句者）之後之首句呼叫之。"""
+    blocks = _blocks_of(tree)
+    where = {}
+    for lst, own in blocks:
+        for i, st in enumerate(lst):
+            where[id(st)] = (lst, i, own)
+    sites, bad = [], []
+    for lst, own in blocks:
+        for i, s in enumerate(lst):
+            if not isinstance(s, ast.Try) or not _calls_in(s.body, TRIAL_CALLS):
+                continue
+            sw = [h for h in s.handlers if _catches(h) and not any(isinstance(x, ast.Raise) for x in ast.walk(h))]
+            if not sw:
+                continue
+            sites.append(s.lineno)
+            chain = [(lst, i)]
+            cur_l, cur_i, cur_own = lst, i, own
+            while isinstance(cur_own, ast.With) and id(cur_own) in where:
+                pl, pi, po = where[id(cur_own)]
+                chain.append((pl, pi))
+                if cur_i != len(cur_l) - 1:
+                    break
+                cur_l, cur_i, cur_own = pl, pi, po
+            marks = {t.id for l_, j_ in chain for p in l_[:j_]
+                     if isinstance(p, ast.Assign) and isinstance(p.value, ast.Call)
+                     and _callname(p.value) == "k6_trial_mark" for t in p.targets if isinstance(t, ast.Name)}
+            pre = bool(marks)
+
+            def _is_rs(st):
+                # 句之本身 ＝ `k6_trial_raise_since(<mark 之名>, …)`（Expr·⛔ 於 if／lambda 之內·首引數 ＝ 其前所取之 mark）
+                return (isinstance(st, ast.Expr) and isinstance(st.value, ast.Call)
+                        and _callname(st.value) == "k6_trial_raise_since" and st.value.args
+                        and isinstance(st.value.args[0], ast.Name) and st.value.args[0].id in marks)
+            inh = all(any(_is_rs(x) for x in h.body) for h in sw)
+            after = False
+            l_, j_ = lst, i
+            k = 0
+            while True:
+                if j_ + 1 < len(l_):
+                    after = _is_rs(l_[j_ + 1])
+                    break
+                k += 1
+                if k >= len(chain):
+                    break
+                l_, j_ = chain[k]
+            if not (pre and (after or inh)):
+                bad.append(s.lineno)
+    return sites, bad
+
+
+def _top(src):
+    t = ast.parse(src)
+    out = {}
+    for n in t.body:
+        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
+            out[n.name] = ast.get_source_segment(src, n)
+        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
+            out[n.targets[0].id] = ast.get_source_segment(src, n)
+    return out
+
+
+def _diff_ok(a, b):
+    # 差唯：- `raise RuntimeError(` 之列 ↔ + 同列而換為 `raise k6_program_stop(`；+ 含 `k6_trial_` 之列
+    dl = [l for l in difflib.ndiff(a.split("\n"), b.split("\n")) if l[:2] in ("- ", "+ ")]
+    minus = [l[2:] for l in dl if l.startswith("- ")]
+    plus = [l[2:] for l in dl if l.startswith("+ ")]
+    conv = [l.replace("raise RuntimeError(", "raise k6_program_stop(", 1) for l in minus]
+    if any("raise RuntimeError(" not in l for l in minus):
+        return False, f"刪列非 raise RuntimeError：{[l for l in minus if 'raise RuntimeError(' not in l][:2]}"
+    rest = list(plus)
+    for c in conv:
+        if c in rest:
+            rest.remove(c)
+        else:
+            return False, f"換列之對無：{c[:80]}"
+    extra = [l for l in rest if "k6_trial_" not in l]
+    return (not extra), (f"增列非 k6_trial_：{extra[:2]}" if extra else f"換 {len(conv)}／增 {len(rest)}")
+
+
+def wiring(repo, base):
+    res = []
+    try:
+        src = _read(repo, "app.py")
+        tree = ast.parse(src)
+        bsrc = _git_show(repo, base, "app.py")
+        btree = ast.parse(bsrc)
+    except Exception as e:  # noqa: BLE001
+        print(f"  ⚠️ 受詞之讀取中止：{type(e).__name__}：{e}")
+        print("⇒ rc 3（無從判定）")
+        return 3
+    # X1
+    n_ok, bad, other = _x1(tree)
+    bn_ok, bbad, _bo = _x1(btree)
+    res.append(("X1 帶號之 raise 皆 k6_program_stop·⛔ 他用", (not bad) and (not other) and n_ok == bn_ok + len(bbad)
+                and n_ok > 0, f"帶號 {n_ok}（基準之帶號 {bn_ok + len(bbad)}）／非者 {bad}／他用 {other}"))
+    # X2
+    try:
+        ssrc = _read(repo, "verify/selection_pipeline.py")
+        sbsrc = _git_show(repo, base, "verify/selection_pipeline.py")
+        s1, b1 = _x2(tree)
+        s2, b2 = _x2(ast.parse(ssrc))
+        bs1, _ = _x2(btree)
+        bs2, _ = _x2(ast.parse(sbsrc))
+        ok2 = (not b1) and (not b2) and len(s1) == len(bs1) and len(s2) == len(bs2) and len(s1) + len(s2) > 0
+        res.append(("X2 吞試算之中止之處皆取 mark 並上拋", ok2,
+                    f"app.py 之處 {len(s1)}（基準 {len(bs1)}）未合 {b1}；selection_pipeline 之處 {len(s2)}"
+                    f"（基準 {len(bs2)}）未合 {b2}"))
+    except Exception as e:  # noqa: BLE001
+        res.append(("X2 吞試算之中止之處皆取 mark 並上拋", False, f"中止 {type(e).__name__}：{e}"))
+    # X3
+    bt, ct = _top(bsrc), _top(src)
+    add = set(ct) - set(bt)
+    gone = set(bt) - set(ct)
+    dif = sorted(k for k in set(bt) & set(ct) if bt[k] != ct[k])
+    why = []
+    for k in dif:
+        if k in ALLOW:
+            ok_, w_ = _diff_ok(bt[k], ct[k])
+            if not ok_:
+                why.append(f"{k}：{w_}")
+    ok3 = add == NEW_TOP and not gone and set(dif) <= ALLOW and not why
+    res.append(("X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形", ok3,
+                f"增 {sorted(add)}／去 {sorted(gone)}／相異 {dif}／不合 {why}"))
+    # X4
+    try:
+        ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
+                            check=True).stdout.decode("utf-8").split()
+        tops = sorted(p for p in ls if p.endswith(".py"))
+        diffs = [p for p in tops if _git_show(repo, base, p) != _read(repo, p)]
+        ok4a, w4 = _diff_ok(sbsrc, ssrc)
+        ok4 = diffs == ["verify/selection_pipeline.py"] and ok4a and "換 0" in w4
+        res.append(("X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列", ok4, f"異 {diffs}／{w4}"))
+    except Exception as e:  # noqa: BLE001
+        res.append(("X4 verify/ 頂層唯 selection_pipeline.py 異", False, f"中止 {type(e).__name__}：{e}"))
+    # X5
+    lits = []
+    for n in tree.body:
+        if isinstance(n, ast.FunctionDef) and n.name in FNS:
+            for c in ast.walk(n):
+                if isinstance(c, ast.Constant) and isinstance(c.value, str) and CASE_LIT_RE.match(c.value):
+                    lits.append((n.name, c.value))
+    res.append(("X5 三函式內⛔ 案件字面", not lits, f"{lits}"))
+    red = []
+    for name, ok, det in res:
+        print(("  ✅ " if ok else "  🔴 ") + f"{name}（{det}）")
+        if not ok:
+            red.append(name.split()[0])
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+# ───────────────────────── run ─────────────────────────
+
+def _pipeline(ns, fst, rv, sp, sb):
+    with contextlib.redirect_stdout(io.StringIO()):
+        snap = rv.load_snapshot()
+        cb_by, cad = rv.build_pipeline(ns, fst, snap)
+        rv.build_ownership(ns, fst, rv.ANON_XLSX)
+        v6 = open(rv.V6DXF, "rb").read()
+        tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
+        params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
+        res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
+        from stepg_pipeline import run_step_g
+        ns["K917_DROPPED"].clear()
+        sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
+                        eff_min_build_by_blk={})
+    return res, sg
+
+
+def run(repo, sbs):
+    ns, fst = _harvest(repo)
+    import run_verification as rv
+    import selection_pipeline as sp
+    if any(f not in ns for f in FNS + ["K6_PROGRAM_STOPS"]):
+        print("  🔴 受詞缺")
+        print("⇒ 紅 ['受詞缺']；rc 1")
+        return 1
+    red = []
+    for sb in sbs:
+        n0 = len(ns["K6_PROGRAM_STOPS"])
+        try:
+            _res, sg = _pipeline(ns, fst, rv, sp, sb)
+            ok1 = len(ns["K6_PROGRAM_STOPS"]) == n0 and bool(sg.get("g_rows"))
+            det = f"登記 {len(ns['K6_PROGRAM_STOPS']) - n0}·G 值列 {len(sg.get('g_rows') or [])}"
+        except Exception as e:  # noqa: BLE001
+            ok1, det = False, f"停機 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}"
+        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：本案⛔ 觸程式之停機（{det}）")
+        if not ok1:
+            red.append(f"R1@{sb}")
+    # R2 注入（首一退縮）
+    sb = sbs[0]
+    k953, k929 = ns["k953_manual_run"], ns["k929_6_fixpoint"]
+    st_ = {"in": False, "n": 0}
+
+    def k953_w(*a, **k):
+        st_["in"], st_["n"] = True, 0
+        try:
+            return k953(*a, **k)
+        finally:
+            st_["in"] = False
+
+    def k929_w(*a, **k):
+        if st_["in"]:
+            st_["n"] += 1
+            if st_["n"] >= 2:
+                raise ns["k6_program_stop"]("🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成）")
+        return k929(*a, **k)
+    ns["k953_manual_run"], ns["k929_6_fixpoint"] = k953_w, k929_w
+    try:
+        _pipeline(ns, fst, rv, sp, sb)
+        ok2, det = False, f"⛔ 上拋（手冊先行之入池閘之呼叫 {st_['n']}）"
+    except RuntimeError as e:
+        m = str(e)
+        ok2 = "GB-999 注入" in m and "試算內之程式之停機·手冊先行" in m and st_["n"] >= 2
+        det = f"上拋：{m.splitlines()[0][:160]}"
+    except Exception as e:  # noqa: BLE001
+        ok2, det = False, f"他之中止 {type(e).__name__}：{str(e).splitlines()[0][:160] if str(e) else ''}"
+    finally:
+        ns["k953_manual_run"], ns["k929_6_fixpoint"] = k953, k929
+    print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：手冊先行之試算內之程式之停機 ⇒ 上拋（{det}）")
+    if not ok2:
+        red.append(f"R2@{sb}")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def main(argv):
+    if len(argv) < 3:
+        print(__doc__)
+        return 2
+    cmd, repo = argv[1], os.path.abspath(argv[2])
+    if cmd == "selftest":
+        return selftest(repo)
+    if cmd == "wiring":
+        if len(argv) != 4:
+            print("用法：wiring <repo> <基準 commit>")
+            return 2
+        return wiring(repo, argv[3])
+    if cmd == "run":
+        sys.path.insert(0, os.path.join(repo, "verify"))
+        os.chdir(repo)
+        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
+        return run(repo, sbs)
+    print(__doc__)
+    return 2
+
+
+if __name__ == "__main__":
+    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `K32`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

---

## 🔧 `W-G.9-389`：試算內之程式之停機之上拋（訊息帶 `GB-` 之號或【未裁】者·【工】·⛔ 鑄號）；`K-9-61` 之落地之單之再分（④⑤ ⇒ `W-G.9-390`）；`ops/queue` 之規則檔之登記（⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`（`W-G.9-388` 入主線）之後；本節由 `W-G.9-389`（新側支 `verify/W-G.9-389-trialstop`）入典。**授權** ＝ `W-G.9-386` 之節之一之 KL 之逐字（自動化之委任）。⛔ 鑄 `K-9` 之號（本節之二 ＝ 發單端之【工】之讀法·⛔ 充裁·以交付之通知告 KL）。

### 一、所據

- 發單端擬 `W-G.9-387` 時之偵察（`2026-10-17 14:08`·`ops/queue` 之 `log.md` 該列·`參考/交接封存_2026-10-18.md` 第 `34` 列）：手冊先行之 `_chk953`、第一趟之 `_chk_a4`、入池閘之 `_try965` 於「併入後之試算中止」回「不過」——其後立之 `GB-205` 等程式未支援之停機於試算內觸者被吞為「未成」，且其理由之字串截於 `120` 字而失其號。
- 本典「`K-9-53` ① 之工程讀法」節之庚（【工】）：「併入後之試算中止 ⇒ 不過（⛔ 停機）」。
- `GB-205`（`W-G.9-380`）：「觸之 ⇒ 停機（⛔ 靜默）」；`CLAUDE.md` 之無靜默之鐵則（缺值、未支援、未裁 ⇒ 停機·⛔ 以預設或「不過」代之）。

### 二、【工】之讀法（`W-G.9-389`·發單端·⛔ 充裁）

- **甲 程式之停機**：訊息之全文含 `GB-` 繼以數字之號（其前一字⛔ 為英數字或連字號、其後一字⛔ 為數字）或「【未裁】」之停機。`GB` 之號 ＝ 泛用阻塞項（程式未支援之形）；【未裁】＝ 須 KL 裁之形。二者於試算之中被判為「不過」，即以「程式之不能判」代「土地之不能配」——其後之併入、按比例、轉調配皆以之為據（靜默）。⇒ 試算之內觸之者⛔ 判為「不過」「未成」「試算中止」，其全文上拋（配地停機·loud）。上開庚之「併入後之試算中止 ⇒ 不過」於**他之試算中止**（配地上不可·無號）照舊。
- **乙 機制**：帶號之停機一律經 `k6_program_stop` 立之（登記其全文於模組級之 `K6_PROGRAM_STOPS`）；吞試算之中止之處，於試算之前取登記之長度（`k6_trial_mark`）、其後見有新登記者即上拋其首者之全文（`k6_trial_raise_since`）。登記⛔ 清：巢狀之試算（入池閘之 `_try965` 在畫面或 harness 之試算之內）以長度分之；試算之前之登記⛔ 波及其後之試算。以登記（⛔ 以訊息之字樣）判之由：畫面之停機經 `st.error`／`st.stop` 與 `[:300]`、`[:500]` 之截而至外殼，字樣或失。
- **丙 吞之處**（`929ea20`）：入池閘之 `_try965`、末端塊合併再試之首次之試算、畫面之段三之 `alloc_state` 與手冊先行、第一趟之試算、harness 之 `alloc_state`、`_trial_k`、`_trial_a4`——八處。其餘之試算之中止已上拋（「無從判定 ⇒ 停機」或 `_K6BTrialStop` ⇒ `RuntimeError`）·⛔ 動。
- **丁 末端塊合併再試之首次之試算**：其中止原記為「試算中止」而逕回（定案之配地將遇同一中止）；程式之停機今亦上拋（與他七處一致·其土地之果同為停機）。
- **戊 帶號之停機之受詞** ＝ `app.py` 之一切 `raise` 其字串常數帶號者（`929ea20` 恰 `10`：`GB-13`、`GB-104`、`GB-205`、【未裁】×`2`、`GB-204`×`4`、`GB-201`）；其訊息⛔ 改。新立之帶號之停機一律經 `k6_program_stop`（`F33 wiring` 之 `X1` 守之）。
- **己 試算之內可達之帶號之停機**（唯讀審查之窮查·`929ea20`）：唯 `GB-104`（`k917_should_drop`：街角第 1 宗竟為閘一「不合格」——「其分配範圍係 winner 之 `G` 所單獨決定（構造保證）⇒ 此情狀⛔ 得發生」）與 `GB-205`（入池閘之部分併入而宗含非其成員之土地）。`GB-104` 之斷言於併入街角第 1 宗之後之試算中觸之者，讀為**程式之構造保證之破**（其文自定為「⛔ 得發生」之斷言·⛔ 為 `K-9-58` ③ 之「合併後反不能配」〔該款之受詞為配地之檢核之不過·⛔ 為程式之自我檢查〕）⇒ 上拋。本案⛔ 觸。若 KL 以其為土地之不能配，另單改之（其時須先證其可達）。
- **庚 無號之程式之完整性之停機**（例：harness 之守恆之破〔停機③〕、結構閘之位次之破、入池閘之 `a′` 缺地價）於試算之內觸之者，本單⛔ 及（照舊為「不過」）；其是否帶號（立 `GB`）待查（待落地清單之序 `18`）。

### 三、本案之量

本案之二退縮，harness 之街角選位至配地（`run_corner_pk_k6b` ＋ `run_step_g`）之全程中，登記恆為空（`F33 run` 之 `R1`）；畫面之路徑以 `parity` 之前後逐位同證之（`W-G.9-389` 規格單 `V-5`）⇒ 本案之一切試算⛔ 觸程式之停機 ⇒ 上拋之機制⛔ 觸 ⇒ **本案之配地⛔ 變**（`k6s3 cmp`／`F8`／`parity`·`W-G.9-389` 規格單 `§一` 項 `5`）。

### 四、`K-9-61` 之落地之單之再分（工程裁·唯序·⛔ 涉土地後果）

`docs/待落地清單.md` 之序 `7`（`K-9-61` ④⑤、`GB-205`、試算內之停機之上拋）分為二：`W-G.9-389` ＝ 試算內之程式之停機之上拋；`W-G.9-390` ＝ `K-9-61` ④（取得街角之宗未保留 ⇒ 還原、下一名續試）與 ⑤（已收受道路、公設地上土地之宗事後未配得 ⇒ 還原、依手冊併入·`GB-205`）之還原（同族·一單）。原定之 `W-G.9-390`（`K-9-60`）⇒ `W-G.9-391`；`W-G.9-391`（`K-9-59`、`K-9-63`）⇒ `W-G.9-392`。其由：⑤ 之量測須試算內之 `GB-205` 之停機⛔ 被吞（本單先之）；二者之族相異。

### 五、`ops/queue` 之規則檔之登記（`W-G.9-386` 之節之二之戊）

`W-G.9-388` 補令一之節之五之後之修訂（皆⛔ 放寬停止之條件·`ops/queue` 之 `log.md` 之監看窗之列記其由）：`發單端.md` 之乙 4之一（立基準）、丙 2（突變之限·三法·示範街廓）、丙 3之一（前置驗算之沿用）、首之本機模式之指引；`執行端.md` 之丙 4之一（版本之比對）、首之指引；新檔 `本機模式.md`（試跑稿·唯 `mode` ＝ `local` 適用）；新目錄 `基準/`。本節定稿時之 `sha256`：`README_自動化運作規則.md` `10652` B·`d775035e0b26087496f8e0b7221a11de42bec79f040d90f3ca6247cc87b5548b`；`執行端.md` `3912` B·`ce550ab5cbbabd22a9e1c6f3242dfd696294547c0fa33ebcaa4dc2f624f04395`；`發單端.md` `14192` B·`6ac5f25608c1c870f567c2ef251146b2bf75b8155a1360d5a535f058ee058c55`；`每日摘要.md` `768` B·`109cc9d5e0c0af604b01191809f19ef58ae8cb272c878f4b0d5797a0ff2f78b5`；`本機模式.md` `5491` B·`c36d70db25d4ea0f510398b333ea54f093409807ad2ef2aa6a82bae0b37d1940`；`ring.sh` `1223` B·`fef64a342611242a1205ec577ca4388beb8617635dc6e86b1576cc30997a0e1a`。

### 六、他案之形（泛用化·KL `2026-10-05`）

| # | 形 | 處置 |
|---|---|---|
| `1` | 入池閘之依手冊併入後之試算（檢核）觸程式之停機（例：`GB-205`） | 上拋（⛔ 判為不過、⛔ 轉按比例） |
| `2` | 手冊先行、第一趟之併入後之試算觸之 | 上拋（⛔ 判為不過） |
| `3` | 段三之試算觸之 | 上拋其全文（原已停機·今其訊息為全文·⛔ 截） |
| `4` | 末端塊合併再試之首次之試算觸之 | 上拋（⛔ 記為試算中止而逕回） |
| `5` | 試算內觸【未裁】之停機 | 上拋（⛔ 以「不過」代 KL 之裁） |
| `6` | 巢狀之試算（畫面或 harness 之試算之內之入池閘之試算）觸之 | 內外皆上拋其首者（以長度分之） |
| `7` | 試算之外觸之（定案之配地） | 照舊停機（⛔ 變） |
| `8` | 號在訊息之第 `300`／`500` 字之後 | 以登記之全文判（⛔ 以截後之字樣判） |
| `9` | 他之配地中止（無號·例：合併後之宗之寬不足致配地之程式中止） | 照舊為不過（庚） |
| `10` | 畫面之顯示之盤點（`main` 之調配之輸入之列表）觸【未裁】 | 照舊（`main` ⛔ 為試算） |

### 七、落地狀態

本節之二 🔶（新側支 `verify/W-G.9-389-trialstop`·候入主線之短單）。`K-9-61` 之「落地狀態」⛔ 變（④⑤ ⬜·`W-G.9-390`）。
````

## 附錄丙　塊 `P43`（附於 `docs/待落地清單.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`W-G.9-388` 入主線；試算內之程式之停機之上拋（新側支）；序 `7` 之分（`W-G.9-389`）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`（`W-G.9-388` 與其補令一〜三入主線）之後；本批之碼在新側支 `verify/W-G.9-389-trialstop`。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `6` | `K-9-61` ①②③⑥（前二節之序 `6`） | 段三後處理之承受之宗與分不到之建地之去處；「另一側」扣路衝街廓 | ✅（主線 `929ea20`） | `K-6` 典 `W-G.9-388` 之節、其補令一之節 |
| `7` | `K-9-61` ④⑤、`GB-205`（前二節之序 `7` 之二） | 取得街角之宗未保留 ⇒ 還原、下一名續試（④）；已收受道路、公設地上土地之宗事後未配得 ⇒ 還原、依手冊併入同一地主他宗（⑤·其還原跨段三、手冊先行、入池閘） | ⬜ | 落地之單 `W-G.9-390`（`K-6` 典 `W-G.9-389` 之節之四） |
| `8` | `K-9-60`（前二節之序 `8`） | 末端塊競合三形 | ⬜ | 落地之單 `W-G.9-391` |
| `9` | `K-9-59`、`K-9-63`（前二節之序 `9`） | 讀圖側；段三後處理 (b) 之路口之半片所鄰之已配得街廓二以上之停機；路衝街廓之 L 形之例（`W-G.9-388` 補令三之唯讀審查之 N2） | ⬜ | 落地之單 `W-G.9-392`（視規模得再分） |
| `16` | 試算內之程式之停機之上拋（前二節之序 `7` 之一·⛔ 鑄號） | 訊息帶 `GB-` 之號或【未裁】之停機於試算之內觸之者⛔ 判為「不過」「未成」「試算中止」，其全文上拋；他之配地中止照舊為「不過」 | 🔶（新側支·候入主線之短單） | `K-6` 典 `W-G.9-389` 之節；`docs/orders/W-G.9-389_規格單.md` |
| `17` | 段三之經道路片之迴圈之段一上鎖之除（`W-G.9-388` 補令三之唯讀審查之 N3） | 段一上鎖之受詞為建築街廓內跨占街角規定範圍之宗、道路片⛔ 入之 ⇒ 不可達；可加一斷言或註 | ⬜ | 另單（⛔ 急） |
| `18` | 試算之內之無號之程式之完整性之停機（`K-6` 典 `W-G.9-389` 之節之二之庚·該單之唯讀審查之 WARNING-1） | 守恆之破、結構閘之位次之破、入池閘之 `a′` 缺地價等⛔ 帶號者於試算之內仍判為「不過」；逐一查其可達與其為程式之停機或配地上不可，前者立 `GB` 之號（經 `k6_program_stop`） | ⬜ | 待查（另單·⛔ 急） |

🔒 **前節之更新**（上二節·⛔ 追改其一字）：其序 `6` ⇒ 本表序 `6`（✅·`W-G.9-388` 入主線）；其序 `7` ⇒ 本表序 `7`（④⑤、`GB-205`·`W-G.9-390`）與序 `16`（試算內之程式之停機之上拋·`W-G.9-389`）；其序 `8`、`9` ⇒ 本表序 `8`、`9`（單號各順延一）；其餘各序（`3`、`4`、`5`、`10`〜`15`）之態、出處⛔ 變。本表序 `16`、`17`、`18` 為新。
🔒 **本案之量**：本批⛔ 變配地（`W-G.9-389` 規格單 `§一` 項 `5`）。
🔒 **依賴序**：序 `16`（入主線之短單）→ 序 `7`（`W-G.9-390`）→ 序 `8`（`W-G.9-391`）→ 序 `9`（`W-G.9-392`）→ 序 `3` → 規格步 `5` → `6` → `7`／`8`（新調配模組·其畫面入口依序 `5`）；序 `4`、`10`〜`15`、`17`、`18` 與 `GB-196`、`GB-197`、`GB-198`、`GB-202` 另單（⛔ 急）。先後之定 ＝ 發單端（KL `2026-10-17 12:40`「先後由發單端依依賴決定」）。
````

## 附錄丁　示範街廓（改前、改後之配地並列·`F33 selftest` 之 `K6`〜`K12` 之形·非本案）

**街廓 A**（住宅區·前緣線 `p1`→`p2`·最小分配面積 `100 ㎡`·側街負擔 `9 ㎡`·玩具之應分配面積 ＝ 面積 × `0.6`）：

```
   p1 ────────────────── 前緣線（正面道路） ────────────────── p2
   ┌────────────┬────────────┬────────────┐
   │ C（甲）     │ X（甲）     │ Z（丙）     │
   │ 街角第 1 宗 │ 60 ㎡       │ 400 ㎡      │
   │ 300 ㎡      │            │            │
   └────────────┴────────────┴────────────┘
   （C 臨正面道路與側面道路·X 與 C 相鄰而同屬地主甲）
```

原位次：C `180`（街角第 1 宗·恆配地）、X `36` ＜ `100` ⇒ 分不到、Z `240`。入池閘：X 與同街廓同地主之街角第 1 宗 C 相連 ⇒ 依手冊併入 C，併入之後試算以檢核之（`K-9-58` ①）。

| 情形 | 改前（`929ea20`） | 改後（本單） |
|---|---|---|
| 併入後之試算無停機（基底·`K8`） | X 併入 C ⇒ **C `216`**、Z `240`；X ⛔ 入調配 | **同左** |
| 併入後之試算為**配地上不可**而中止（無號·`K7`） | 整筆之併入判為不過 ⇒ 按比例（`K-9-66`·`0.01 ㎡` 之格）併入 `59.99` ⇒ **C `215.99`**、X 剩 `0.01 ㎡` 入調配、Z `240` | **同左**（照舊） |
| 併入後之試算為**程式之停機**而中止（帶 `GB-` 之號或【未裁】·`K6`） | 同上列——**程式之不能判被當作土地之不能配**：C `215.99`、X 剩 `0.01 ㎡` 入調配、Z `240`；唯入池閘之紀錄記「併入後配地中止」，配地照常產出 | **配地停機**，訊息之全文上拋（例：「🔴 [試算內之程式之停機·入池閘·併入後之試算] 🔴 [GB-205] …」）；須程式支援其形後再跑 |

換名（地號、地主、街廓之名）、左右鏡射、旋轉（`37°`、`213°`·TWD97 之座標）之後，三列之結果除名稱外皆同（母體 ＝ `F33 selftest` 之 `K9`〜`K12` 之四變換 × 上表三列 ＝ `12` 果）。**本案**（UC9898·二退縮）：街角選位至配地之全程無任何程式之停機 ⇒ 配地⛔ 變（`§一` 項 `5`）。

SELF_SHA256: 0d30f02fc7df4183ce26a5cf25762555c09ae1c0f8af26efaf7f845fdf846fa9
