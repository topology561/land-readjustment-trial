# `W-G.9-392`　規格單：`K-9-80` ③ 之微差之吸收之落地——每宗之應分配面積試算至穩定（求解之容差 `1e-6 ㎡`）後取至小數 2 位，評選與實配同值；取得之宗（街角第 1 宗、末端塊之當選者）之自我檢查（二次所算取至 2 位不同 ⇒ 停機·`GB-206`）；末端塊之評選之試算之單一真相源（KL `2026-10-22 05:22`「是」·甲）＋ 待落地清單之更新（新側支 `verify/W-G.9-392-k980g`·**本案配地改變 ⇒ ⛔ 入主線·待 KL 核**）

> **本單建議等級 ＝ `high`**（生產碼 `2` 檔：`app.py` 之頂層節點四之改與四新名、`verify/stepg_pipeline.py` 之 `_run_step_g_impl`〔`§三-1`〕；規格與量測器皆全；**本案之配地改變**〔`±0.01 ㎡`·`§一` 項 `5`〕）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-22`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本·工項零〜四之一切 `commit` 推至**新側支 `verify/W-G.9-392-k980g`**，其起點 ＝ 主線之端 `56c77fd`）。
> **流程 ＝ 規格單**（常態）：**生產碼由執行端依 `§三` 撰寫**；發單端給規格（`§三`）、量測器（塊 `Fy47`·執行端⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之生產碼之 blob（由執行端回報、發單端復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `2` 檔；**本案之配地改變**：`§一` 項 `5` 之表之 `6`／`5` 項〔3.5 m／0 m〕——其餘逐欄⛔ 變）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（`W-G.9-391` 入主線·補令一工項零″）；遠端 heads **`51`**（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-392-k980g`（工項零立之·其後皆快轉）；主線⛔ 動**（本批改本案之配地 ⇒ 入主線待 KL 核·`§四-2`）。
> 🔑 **通則** ＝ `ops/queue` 之 `README_自動化運作規則.md` 第六節（雲端·Linux）：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之**絕對路徑**；`<O>` ＝ 執行端自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）；`commit` 訊息一律 `git commit -F`；含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8；Bash 命令⛔ 含 heredoc。塊 `Fy47`／`K38`／`P49`／`G16` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ 遠端分支 `ops/queue` 之 `orders/W-G.9-392_規格單.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python3 -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限** ＝ README 第六節第 `3` 款：各驗之命令之同時並行數 ≤ **`2`**；逾時或 `rc` ≠ 期者，於⛔ 他負載之下**重跑一次**，二趟之出艙皆照實入報告（重跑之趟 ＝ 期 ⇒ 該呼叫以重跑之趟為準·報告具名之）。
> 🔑 **前置驗算之沿用**（`發單端.md` 丙 3之一·`執行端.md` 丙 4之一·KL `2026-10-18 19:57`）：前置之 (甲)(乙)(丙) 見 `§四-1` 工項二之前置；(丙) 之沿用以 `ops/queue` 之 `基準/56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81.md` 為準，其前提之比對（主線之端、`python3 --version`、`pip freeze` 之 `sha256`）之結果入回報。
> 🔑 **撰碼中之自跑**：執行端撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🔑 **⛔ 寫 `CLAUDE.md`**（雲端之分類器拒之·KL `2026-10-17 22:42` 同意）：待落地清單之更新寫於 `docs/待落地清單.md`（塊 `P49`·純末端追加）。本單⛔ 須 `CLAUDE.md` 之改。
> 🛑 **本單⛔ 及於**：主線之任何推進；`§三-1` 所列以外之生產碼之一字與行為；生產碼 `34` 檔之中 `app.py`、`verify/stepg_pipeline.py` 以外之 `32` 檔（含 `verify/selection_pipeline.py`、`verify/run_verification.py`、`verify/fixture_*.py`、`verify/wf_*.py`）；`§三-3` 之禁改；既有量測器除塊 `Fy47` 所改之 `11` 檔外之一字；`data/` 之一切檔、`verify/case_params_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、自誤簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/`、`CLAUDE.md` 之一字；`K-6` 典、`docs/待落地清單.md`、`GB` 簿除塊 `K38`／`P49`／`G16` 之純末端追加外之一字；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；任何他側支之推送、刪除或改寫；末端塊之義（KL `2026-10-22 05:40`·請示待呈）、`K-9-80` ⑦、`K-9-61` ⑤ 與 `GB-205`（`W-G.9-393`）、`K-9-60`、`K-9-59`、`K-9-63`、`K-9-62` 之指配、代數之退路（`iterate_G_S`）之精度、最小建築面積之畫面與 harness 之源之統一（序 `6`）——另單。
> 🔴 **本單⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本單未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量與本機之核數（`nproc`）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`；`git ls-remote --heads origin` 之列數 ＝ **`51`**（全列存 `<O>/heads_before_392.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-392-k980g`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 634 629` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `619`／`MAX` `634`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `56c77fd` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝之出艙存 `<O>`）；量測之殼之旗標之出艙 ＝ 單首 🔑 之期。🔎 依 `requirements.txt` 裝後，`pip freeze` 之 `certifi`、`pillow`、`streamlit`、`websockets` 四列或異於基準（發單端 `2026-10-22` 實見）⇒ 以 `python3 -m pip install certifi==2026.10.18 pillow==12.3.0 streamlit==1.66.0 websockets==17.2 --break-system-packages` 釘回基準之版（其出艙存 `<O>`·入回報）。
6. 版本之比對（前置 (丙) 之前提）：`python3 --version` 與 `python3 -m pip freeze` 之全文之 `sha256`，對 `ops/queue` 之 `基準/56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81.md` 之「一、環境之指紋」（`Python 3.11.17`、`ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`·發單端擬單之機亦同）；其結果入回報（相異 ⇒ 前置 (丙) 整份照跑·⛔ 停機）。

### `§零-1`　取號現查（宣告框）

**本批鑄 `GB-206`**（塊 `G16`·`GB` 簿之純末端追加）；`自誤`、`VR`、`K-9` 皆⛔ 鑄（塊 `K38` 之二 ＝ 發單端之【工】之讀法·⛔ 充裁；KL `05:22` 之答登記於 `K-9-80` ③ 之節·⛔ 另立號）。

**號、塊名、新名**（母體 ＝ 開工態 `56c77fd` 之追蹤檔 **`2911`** 檔·`git grep -l`／`git grep -h … | wc -l` ＋ `-F`·`自誤 588`）：

| 受詞 | 檔／列 | 判 |
|---|---|---|
| `GB-206`（`-F`） | `0`／`0`（錨定框 `(?<![0-9\-])GB-206(?![0-9])` 亦 `0`）；`GB` 簿之 `MAX` ＝ `205`（`§零-0` 項 `3`） | 🟢 可取 |
| `` 塊 `Fy47` ``、`` 塊 `K38` ``、`` 塊 `P49` ``、`` 塊 `G16` ``（逐名·`-F`） | 皆 `0`／`0`（裸名 `P49` `1`／`1`、`G16` `2`／`2` 皆二進位之資料檔〔`data/` 之 `.xlsx`、`docs/參考文件/` 之 `.pdf`〕之位元組·⛔ 塊名） | 🟢 可取 |
| 對照甲［必非零］`` 塊 `Fy46` ``、`` 塊 `K37` ``、`` 塊 `P48` ``、`` 塊 `G15` `` | `Fy46` `3`／`17`；`K37` `3`／`18`；`P48` `4`／`15`；`G15` `7`／`36`（裸名） | 🟢 框非恆空 |
| 報告名 `W-G.9-392R`、新側支之名 `W-G.9-392-k980g`、本單名 `W-G.9-392_規格單`、新器 `probe_WG9392`（`-F`·逐名） | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |
| 新頂層之名 `K980_G_TOL`、`K980_G_MAX_ITER`、`k980_acq_check`、`end_block_trial_G`；原型之區域之名 `_np392`、`_smr392`、`_sl392`、`_d392`、`_c392`、`_dd392`、`_bp392`、`_r392`、`_ge392`、`_ga392`（`-F`·逐名·後者⛔ 為期·執行端之名異者另自查其⛔ 撞） | 皆 `0` 檔 | 🟢 ⛔ 撞名 |

量測器之新檔名 `F36`（`verify/probes/probe_WG9392_k980g.py`）。收工閘 `6` 以 `634 629` 驗之（本批⛔ 鑄自誤）；閘 `7` 之 `GB` 之期 ＝ `198`／`206`。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `56c77fd`，或遠端 heads ≠ `51`、或已含 `refs/heads/verify/W-G.9-392-k980g`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期，或 `§零-0` 項 `5` 之環境於安裝後仍不能匯入 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本單不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy47`／`K38`／`P49`／`G16` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy47` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或執行端須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地之改變 ≠ `§一` 項 `5` 之表**（多一項、少一項、或其值異） |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-392-k980g`（工項零〜四）或 `ops/queue`（回報）；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之三檔（`K-6` 典、`docs/待落地清單.md`、`GB` 簿）：任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊，或寫出後之 blob ≠ `§五-1` 項 `5`；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | 執行端作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或執行端認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 |
| `13` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁：停機上呈之全文寫入 `ops/queue` 之 `reports/W-G.9-392_規格單_回報.md`（`result` ＝ `停機上呈`）；已推至新側支之 `commit` ⛔ 撤。

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python3 verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單端實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單端自倉實跑·雲端 Linux `4` 核·倉外工作樹·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（`W-G.9-391` 補令一工項零″·快轉自 `a8657c4`）；遠端 heads **`51`**；追蹤檔 `2911`；`app.py` ＝ `b591d7605b932b42c9dc205bb8589ef04505045b`（`1868868` B）；`verify/stepg_pipeline.py` ＝ `b2f6622351d1bcdcdf7b603c7412a8f902aa2edc`；`verify/selection_pipeline.py` ＝ `fec1d5c0f80584ab008612eec92ab540dfe44fdd`、`verify/run_verification.py` ＝ `ef043da43e69f236550d0f420f6684f2edd271e4`（本批皆⛔ 動）；`K-6` 典 ＝ `0fad1dafd3c6236b571969b1538170f8662d9ee6`（`919452` B）；`docs/待落地清單.md` ＝ `48b50c3da80dff7143b82fc9eeba00673750a158`（`23233` B）；`GB` 簿 ＝ `3cb60b424b60b56664734f8696ef8a53537331d6`（`1063208` B）；自誤簿 ＝ `c5406d05c024dae897beb3c1175934ece7c0819b`、`CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`（本批皆⛔ 動）；`probe_WG9270_closegate.py 634 629 .` ⇒ `rc 0`（對照 `635 634` ⇒ `rc 7`）；`probe_WG9321_issuer_anchor.py … 634 629` ⇒ `rc 0`（`§零-0` 項 `3` 之值）；基準 ＝ `ops/queue` 之 `基準/56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81.md`（`77` 呼叫皆合期）；本批所改之 `11` 器之施前 blob ＝ `§五-1` 項 `2` |
| `2` | 受詞（`56c77fd`） | 應分配面積之求解之唯一之入口 `_solve_G_one`（`solve_G_binary` 之生產呼叫全檔恰一）傳 `tol=0.01, max_iter=80`；評選之式：街角第 1 宗 ＝ `_corner_first_lot_G`（右側之上界 ＝ `_oblique_s_max`〔街廓於斜交軸之 s 域上界〕）、末端塊 ＝ `end_block_host` 之巢狀 `_trial`（上界 ＝ 正面之全長）；實配：二宿主（畫面 `f3_screen_stepg_run`、harness `_run_step_g_impl`）之左右鏈之 `_solve_one`（上界 ＝ 剩餘之長）——**二次所算⛔ 比**；本案 `R6` 右 `628-18(1)` 評選 `307.79`、實配 `307.78 ㎡`（`probe_WG9338_cornerG_attr.py` 之歸因：唯 `S_max` 之鍵） |
| `3` | 工項一之端（`56c77fd` ＋ 塊 `Fy47`·倉外實跑） | 前置 (甲) 之 `34` 呼叫之 `rc`／末列 ＝ `§五-1` 項 `8` 之工項一之端之列（`F36` 之三呼叫與更錨之四器之 `run` 紅如期·前態之對照組；其餘 ＝ 基準之值）；(乙) 之 `6` 呼叫 ＝ 基準之值（其器與其受詞之檔皆⛔ 為塊 `Fy47` 所動）；諸呼叫之 `stderr` 合計 `0` B；(丙) ＝ 基準之值 |
| `4` | 施後（原型 ＋ 塊 `Fy47`·倉外實跑·⛔ 入倉） | 原型之二檔 ＝ `app.py` `2b8b02efb11fa4a1d3b5a2619613ec9be4fe8d98`（`+75`／`−10`）、`verify/stepg_pipeline.py` `876b7404ee72c58009f38de893b71aa81dde856b`（`+33`／`−0`）——**⛔ 為期**（執行端之碼異則異·唯其行為以 `V-*` 量之）；`§五-1` 項 `8` 之 `80` 呼叫：皆 `rc 0`、末列皆 ＝ 該表之施後之列（`#56`／`#57` 除外·JSON）、`stderr` 合計 `0` B·耗時之和 `11685` s·並行 `2`；`F36 selftest` `G1`〜`G4`、`H1`〜`H5`、`E1`〜`E5` 與 `P0 14／14`、`F36 wiring` `W1`〜`W7`、`F36 run` `R1@3.5`／`R2@3.5`／`R1@0.0`／`R2@0.0` 皆 ✅ |
| `5` | 本案之配地（前態 ＝ 工項一之端〔＝ 基準〕·後態 ＝ 原型） | `F36 diff`（`k6s3` 之二落檔之逐欄全比·⛔ 容差）：**3.5 m** `全比相異 6 項` ＝ `宗 R5·628-18(2)·left G(㎡) 268.33 → 268.34`、`抵費地 R1-抵費地-1 面積 851.68 → 851.69`、`抵費地 R3-抵費地 面積 1651.41 → 1651.4`、`抵費地 R4-抵費地 面積 697.4 → 697.39`、`抵費地 R5-抵費地 面積 1221.44 → 1221.45`、`抵費地 R6-抵費地 面積 980.59 → 980.58`；**0 m** `全比相異 5 項` ＝ `抵費地 R1-抵費地-1 面積 851.67 → 851.69`、`抵費地 R3-抵費地 面積 1651.41 → 1651.4`、`抵費地 R4-抵費地 面積 697.4 → 697.39`、`抵費地 R5-抵費地 面積 1221.47 → 1221.46`、`抵費地 R6-抵費地 面積 980.59 → 980.58`（對照組：前態之 3.5 m 對 0 m ⇒ `全比相異 45 項`）——其值與 KL `05:22` 所核之請示表（`待KL/2026-10-22_街角地評選與實配之面積差.md`）之「甲」之欄逐位同；`628-18(1)` 仍 `307.78`（其評選亦 `307.78`）；他之宗之地號、地主、`a`、`G`、宗序、推進之側、街角之得標、強制抵費地、剔除皆⛔ 變（不配地之宗 `628-42(1)` 之試算 `G` `3.81` → `3.82` 唯見於 `F8` 之落檔·`k6s3` 之落檔⛔ 載剔除之宗之 `G`）。`k6s3 cmp`（容差 `0.01`）⇒ 二退縮皆 `rc 1`·`相異 1 項 ⇒ 🔴 異`（唯 `R1-抵費地-1` 之 `0.01` 逾其容差之浮點之邊·他項在其容差之內）。`F8` 之落檔前後 （`probe_WG9349_k9296.py run` 之落檔）：3.5 m `8be0160bc14dd92a5331f86eecc995cae0507376` → `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、0 m `6fb86647807f9744594071be25c522b6b506c230` → `884e91714a79288406faa4def6518847de36de39`；其逐欄之差唯 3.5 m 二欄（`/rows[16]/G(㎡)`〔`628-18(2)`〕`268.33` → `268.34`、`/dropped/R2/left[0]/G(㎡)`〔不配地之 `628-42(1)` 之試算 `G`〕`3.81` → `3.82`）、0 m 一欄（後者）；`parity` （畫面與 harness 之配地之比）二退縮皆 `rc 0`·`不符 0 項`，其落檔與 `stdout` 前後逐位同（發單端之二態同在 `56c77fd` 之 `HEAD`）。取得之宗之自我檢查：3.5 m `423` 次（相異之〔宗、值〕`17` 組）、0 m `324` 次（`18` 組）皆同值、⛔ 停機 ⇒ **本案之配地改變（上開之 `6`／`5` 項）**。 |
| `6` | 量測器之判別力（原型之上之突變·發單端實跑·`F36 selftest`／`wiring`） | 見下之「突變之表」：`11` 突變皆紅；未突變之原型皆綠；基準（`56c77fd`）之 `F36 selftest`／`wiring`／`run` 皆紅（`§五-1` 項 `8` 之 `#78`〜`#80` 之工項一之端之列） |
| `7` | 唯讀獨立審查（一輪·⛔ 參與撰題） | (A)「改配地或違裁示」：**無**。審查另證：容差 `1e-6` 下二次所算與不動點之差 ＜ `1e-6`（玩具之次數 `27`／舊 `15`·上限 `200` 足）；`solve_G_binary` 之生產呼叫全倉恰一（`_solve_G_one`）；自我檢查之停機於段三之試算之內確上拋（審查自建之突變〔容差回 `0.01`〕之 `run 3.5` ⇒ `🔴 [試算內之程式之停機·段三·harness 之試算] 🔴 [GB-206·K-9-80 ③ …R6·right] 街角第1宗 628-18(1)：評選之所算 307.79 ㎡ ≠ 實配之所算 307.78 ㎡`）；`_WF_NS_NAMES` 之齊全；本案 3.5 m 之 `a` 未變之街角第 1 宗 `10` 組之評選與檢查之輸入逐位同者 `9`、`R2` 左 `628-41(1)` 之正面之單位向量差 `1` ulp（二處之算法之別）。所揭而入（塊之文字）：段三之前之路徑之 `+0.01 ㎡` 四宗（塊 `K38` 之三）、基線之檔之重烤（`K38` 之四 `66`·`P49` 序 `28`）、右鏈之 `_adj` 之重試之形（`65`）、`iterate_G_S` 之⛔ 及為受詞之縮（`K38` 之二乙·呈 KL 時標明）、`wf_f1`／`wf_f4` 之二分之⛔ 及、`K38` 之二丁與 `59` 之措辭、`K38` 之六之數之出處與「末端塊無退縮」、`G16` 之「二宿主各四」。記而⛔ 改（留次單·交接）：`F36 wiring` 之 `W2` 之洞（`else` 支承 `if` 之判、`not _commit`、`kind` 之字面⛔ 驗、第 `6` 引數⛔ 驗）；諸器之許以節點為單位（`W392` 四節點）；`_BISECT_TOL`（`app.py` 之舊註「`solve_G_binary` 之收斂容差」）與 `solve_G_binary` 之預設之未同步；`_np392` 之位與 `_smr392` 之預算；評選之值有存（`_G_true`）而本單擇重算（讀法之擇）；三器之更錨之源非獨立（`fixture-provenance`·其源 ＝ 前態之碼而唯換 KL 所核之精度）。 |

**突變之表**（每種之所據：(a) 泛用化之目標／(b) 既裁之樣態或自誤之錯／(c) 出錯而變空而照樣亮綠；三法 ①「KL 所否之選項」：KL `05:22` 所否之「乙」（精度不變、實配沿用評選之上界）⇒ `M1`；② 換名、鏡射、旋轉 ＝ `F36 selftest` 之 `G1`、`G2`（原座標與旋轉 `37°`·鏡射·TWD97 之尺度之四解同）；③ 邊界 ＝ 恰等（`H1`）、取至 2 位恰差 `0.01`（`H4`）、未捨入異而取至 2 位同（`H3`）、不動點於半分之上下 `2e-5`（`G3`）、上界恰為 `0.1`（`E3`））：

| 突變 | 所據 | 所改（原型之上） | 紅 |
|---|---|---|---|
| `M1` | 三法 ①（KL 所否之「乙」） | 求解之容差回 `0.01`，實配之右側之街角第 1 宗之上界改用評選之上界（`_smr392`） | selftest `rc 1`·['G1', 'G2', 'G3', 'G4']；wiring `rc 0`·[] |
| `M2` | (b) 現狀（`56c77fd` 之精度） | 求解之容差回 `0.01` | selftest `rc 1`·['G1', 'G2', 'G3', 'G4']；wiring `rc 0`·[] |
| `M3` | (c) | 自我檢查恆過（比之判恆偽） | selftest `rc 1`·['H2', 'H4', 'H5']；wiring `rc 0`·[] |
| `M4` | (c) | harness 之四處之自我檢查去之 | selftest `rc 0`·[]；wiring `rc 1`·['W2', 'W4'] |
| `M5` | (a) 寫死側別 | 二宿主唯左鏈有自我檢查（右鏈去之） | selftest `rc 0`·[]；wiring `rc 1`·['W2'] |
| `M6` | 三法 ③（取至 2 位同而未捨入異） | 以未捨入之值比 | selftest `rc 1`·['H3']；wiring `rc 0`·[] |
| `M7` | (b) `W-G.9-389`（帶號之停機須經 `k6_program_stop`） | `raise RuntimeError(` 直拋 | selftest `rc 1`·['H2', 'H4']；wiring `rc 1`·['W6'] |
| `M8` | (b) 單一真相源（`#20`） | `end_block_host` 之評選留其舊之巢狀之解（⛔ 委派） | selftest `rc 0`·[]；wiring `rc 1`·['W3'] |
| `M9` | (b) `_WF_NS_NAMES` 之漏列（`W-G.9-391` 審查 A-1） | `_WF_NS_NAMES` 漏 `k980_acq_check` | selftest `rc 0`·[]；wiring `rc 1`·['W4'] |
| `M10` | 三法 ③（恰差 `0.01`） | 比之判改 `abs(差) ＞ 0.01` | selftest `rc 1`·['H4', 'H5']；wiring `rc 0`·[] |
| `M11` | (c) 自比 | 街角之自我檢查之評選之值改傳實配之 `G`（自比·恆同） | selftest `rc 0`·[]；wiring `rc 1`·['W2'] |

---

## `§二`　所據之語與射程

🔒 **所據**：`docs/待落地清單.md` 之「……`W-G.9-390` 入主線；`K-9-80` ④⑤⑥ 與 `K-9-34` 之落地（新側支）；序 `22` 之再分（③ ⇒ `W-G.9-392`）……」節之序 `25`（「`K-9-80` ③（上節之序 `22` 之二）·鎖定之宗之重算之微差之吸收：先查其源……二讀而土地後果相異者呈 KL」·落地之單 `W-G.9-392`）；`K-6` 典 `K-9-80` ③（`W-G.9-390` 補令三之節）之「其餘之重算之微差……二者之合讀……有二讀而土地後果相異者呈 KL」與同典 `W-G.9-391` 之節之二之辛。

發單端之請示（`ops/queue` 之 `待KL/2026-10-22_街角地評選與實配之面積差.md`·`2026-10-22 03:35`·監看窗 `05:2x` 審畢）之【要你判斷】（逐字）：「各宗之應分配面積（含評選與取得之街角地、末端塊），依「甲」（每宗試算至穩定後取兩位小數，評選與實際配地同值）辦理——**是／否**？（否者即依「乙」。）」；其甲（逐字）：「每一宗之應分配面積皆試算至穩定後，再取至小數點以下 2 位（第 3 位四捨五入）——評選與實際配地兩次應同值，其後重算亦不變（同一地主之併入除外）；並設自我檢查：取得之宗兩次所算若不同，即停下示訊。」

**KL 之語（`2026-10-22 05:22`·逐字·`ops/queue` 之 `KL答覆/2026-10-22_0522.md`）**：「是」。

🔒 **請示前之三關之甲**（已於請示時為之·見請示檔末）：〈段一〉（KL `2026-07-30`）「本段所有 G 與指數一次算定，全程不再重算」、〈§五〉、`K-9-80` ③、`2026-08-05` 之推論、`CLAUDE.md` §8 之註、手冊第 `4616`〜`4622` 列——KL 之擇（甲）即其合讀之定；本單之【工】（塊 `K38` 之二）唯定其量（容差 `1e-6`、自我檢查之時點與受詞），其土地之果 ＝ 請示表之甲之欄（`§一` 項 `5` 逐位同）⇒ **⛔ 新域問**。

🔒 **授權**（自動化之委任·`K-6` 典 `W-G.9-386` 之節之一之 KL 逐字）：KL `2026-10-17 07:23` 第 `3` 點「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目，畢竟討論到現在我覺得已經大多配地的幾何情況、分配成果檢驗機制(R_END,街角地檢驗,內接矩形,若有最小建築面積之檢核,配地要臨FRONTLINE及BASELINE等)及市地重劃扣除負擔之分配精神，已經大致都有說明與你討論過了，所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」；`07:58`「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」。本單 ＝ 待落地清單上已有 KL 裁示之項目（`K-9-80` ③·KL `05:22`）。**`expects_allocation_change` ＝ `true`**（`§一` 項 `5`）——README 第二節停止條件 `2`（新規格單使本案配地改變）⇒ 本批之側支保留、**⛔ 入主線**，待發單端復驗後呈 KL 核；執行端之量得本案配地之改變 ≠ `§一` 項 `5` 之表 ⇒ 停機款 `6`。

🔒 **【工】之讀法**（塊 `K38` 之二·以交付之通知告 KL）：甲 試算至穩定（容差 `1e-6 ㎡`·次數之上限 `200`）；乙 受詞（每一宗·`_solve_G_one` 之一切呼叫；強制抵費地之帶、範圍之擴大、代數之退路⛔ 及）；丙 評選之式（`_corner_first_lot_G`、`end_block_trial_G`）；丁 取得之宗之自我檢查（末趟·鏈首·以評選之式依實配之輸入重算·取至 2 位異 ⇒ `GB-206`）；戊 門檻邊緣以精算之值判之；己 本案之量之源。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由執行端逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支；`(c)` ⛔ 及主線（入主線待 KL 核·`§四-2`）、他側支、`data/` 之資料檔、末端塊之義、`K-9-80` ⑦、`K-9-61` ⑤、`GB-205`、`K-9-59`、`K-9-60`、`K-9-62` 之指配、`K-9-63`、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）。

---

## `§三`　規格（執行端依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**（`56c77fd`）：
- 「**求解之入口**」＝ `_solve_G_one`（`solve_G_binary` 之唯一之生產呼叫者）；「**評選之式**」＝ 街角第 1 宗之 `_corner_first_lot_G`、末端塊之 `end_block_trial_G`（`R-3`）；「**實配**」＝ 二宿主之左右鏈之 `_solve_one`（含右鏈之 `_adj` 之重試）。
- 「**末趟**」＝ 二宿主之 `_advance_block_with_split(_k_split, _commit)` 之 `_commit` 為真之趟；「**鏈首之取得之宗**」＝ 該趟之 `is_first_corner_l`／`is_first_corner_r` 為真之宗（街角第 1 宗），或該側之鏈之第 `0` 宗而 `entry.get('is_end_block')` 為真、且該側之 `_eb_info[<側>]` 非 `None` 者（末端塊之當選者）。
- 「**取至 2 位**」＝ Python 之 `round(x, 2)`（`solve_G_binary` 之回傳之 `G` 之同式·⛔ 改其式）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | 常數與求解之入口 | `app.py` 之頂層增二常數：`K980_G_TOL = 1e-6`（㎡·應分配面積之二分之收斂之容差）、`K980_G_MAX_ITER = 200`（其次數之上限）；各附註其義與所據（`K-9-80` ③·KL `2026-10-22 05:22`「甲」）。`_solve_G_one` 之 `solve_G_binary(…)` 之呼叫改傳 `tol=K980_G_TOL, max_iter=K980_G_MAX_ITER`（舊 `tol=0.01, max_iter=80`）；他之引數一字⛔ 動；`solve_G_binary` 一字⛔ 動。 |
| `R-2` | 自我檢查之函式 | 頂層新函式 `k980_acq_check(kind, blk_label, side, pid, g_eval, g_actual)`：`round(float(g_eval), 2)` ≠ `round(float(g_actual), 2)` ⇒ `raise k6_program_stop(<訊息>)`（訊息含「GB-206」「K-9-80 ③」、`kind`、`blk_label`、`side`、`pid` 與二值〔各取至 2 位·`:.2f`〕·其首帶 `🔴`）；同 ⇒ 回 `None`、⛔ 登記。⛔ 以 `RuntimeError` 直拋（`W-G.9-389`：帶號之停機一律經 `k6_program_stop` 立之 ⇒ 試算之內亦上拋）。 |
| `R-3` | 末端塊之評選之試算之單一真相源 | 頂層新函式 `end_block_trial_G(solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max, avg_depth, allocation_dir, side, s_back)`：`side` ∉ {`'left'`, `'right'`} ⇒ `raise RuntimeError`；左 ⇒ 方向 `d̂`、起點 `corner_pt`；右 ⇒ 方向 `−d̂`、起點 `corner_pt ＋ S_block_max·d̂`；呼叫 `solve_one(a_m2, A_ratio, l_front, 0.0, 0.0, blk_poly, <方向>, <起點>, max(0.1, float(S_block_max)), False, '無', avg_depth, _allocation_dir=allocation_dir, _side_mid=None, _W_prev=0.0, _w0_start=0.0, _near_dir=None, _is_chain_head=True, _s_back=s_back)`；回 `(float(G), float(S_raw 或 S))`（與 `56c77fd` 之 `end_block_host` 之巢狀 `_trial` 之解之式逐位同）。`end_block_host` 之 `_trial` 改為：`a` 與 `A` 之算照舊，其餘以 `return end_block_trial_G(solve_one, …, side, s_back)` 為之（`end_block_host` 內⛔ 直呼 `solve_one`）。 |
| `R-4` | 取得之宗之自我檢查之四處 | 二宿主（`app.py` 之 `f3_screen_stepg_run`、`verify/stepg_pipeline.py` 之 `_run_step_g_impl`）之左鏈、右鏈各二：鏈首之取得之宗之實配之 `res` 定後（右鏈 ＝ `_adj` 之重試之後）、`k917_should_drop` 之 `continue` 之後、該側之宗序之推進（`_lg_idx_left += 1`／`_lg_idx_right += 1`）之前：① `if _commit and <is_first_corner_l／_r>:` ⇒ `k980_acq_check('街角第1宗', blk_label, '<left／right>', k, _corner_first_lot_G(a_m2=a_m2, A_ratio=A_ratio, B=B_value, C=C_for_calc, l_front=l_front, l_side=l_side_use, F=F_use, block_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt, s_max_left=‖front_p2 − corner_pt‖, s_max_right=<評選之右側之上界>, side='<左／右>', allocation_dir=allocation_dir_block, side_mid=<該側之 SIDE_LINE 之中點>, avg_depth=avg_depth_default, tab6_burden=_tab6_burden, front_p2=_front_p2_blk, _label=…), res.get('G', 0.0))`；② `elif _commit and <該側之宗序> == 0 and entry.get('is_end_block') and _eb_info['<left／right>'] is not None:` ⇒ `k980_acq_check('末端塊', blk_label, '<left／right>', k, end_block_trial_G(_solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max, avg_depth_default, allocation_dir_block, '<left／right>', float(_eb_info['<left／right>']['s_back']))[0], res.get('G', 0.0))`。「評選之右側之上界」＝ 評選處之同式：`(_oblique_s_max(<街廓之頂點>, d_hat, corner_pt, allocation_dir_block) or ‖front_p2 − corner_pt‖) if allocation_dir_block is not None else ‖front_p2 − corner_pt‖`，於每街廓、`_advance_block_with_split` 之定義之前算一次（`verify/stepg_pipeline.py` 經 `ns['_oblique_s_max']`）。harness 之側經 `ns['k980_acq_check']`、`ns['_corner_first_lot_G']`、`ns['end_block_trial_G']` 取之。 |
| `R-5` | 引擎之注入之名 | `app.py` 之 `_WF_NS_NAMES`（app 之七級調配之路注入引擎之名）增 `"k980_acq_check", "end_block_trial_G"`（引擎經 `ns[…]` 取之·漏列即 `KeyError`）。 |
| `R-6` | 訊息與他 | `R-2` 之訊息帶 `GB-206`（`K6_PROGRAM_STOP_RE` 之號）；`R-3` 之側別之停機⛔ 帶 `GB-` 之號或【未裁】；新增之 docstring 載 `W-G.9-392` 與所據之條；`R-1`〜`R-6` 以外之一字⛔ 動；新增之區域名皆帶 `392`（⛔ 撞所在函式與全檔之既有之名）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F36`（`verify/probes/probe_WG9392_k980g.py`·新）：`selftest <repo>` 之 `G1`〜`G4`、`H1`〜`H5`、`E1`〜`E5` 與 `P0`；`wiring <repo> 56c77fd` 之 `W1`〜`W7`；`run <repo>` 之 `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0`；`diff <pre.json> <post.json>`（`k6s3` 之二落檔之逐欄全比）。其所量之名與形：`R-1` 之二常數與 `R-2`／`R-3` 之二新函式之名與簽名（以 harvest 呼之）；`W1` `_solve_G_one` 之 `solve_G_binary(` 恰一而以二常數之名傳 `tol`／`max_iter`、`app.py` 全檔之 `solve_G_binary(` 恰一；`W2` 二宿主之 `k980_acq_check(` 各恰四（街角 × 左右以 `_corner_first_lot_G(…)` 為其第 `5` 個位置引數、末端塊 × 左右以 `end_block_trial_G(…)[0]` 為之），各在一判式含 `_commit` 之 `if`／`elif` 之下，其第 `3` 個位置引數為側別之字面；`W3` `end_block_host` 內 `end_block_trial_G(` 恰一、`solve_one(` 之直呼為零；`W4` 引擎經 `ns[…]` 取之新名皆在 `_WF_NS_NAMES`；`W5` 頂層之名之增恰四、無減；`W6` `k980_acq_check` 內呼叫 `k6_program_stop` 且含字面「GB-206」；`W7` ⛔ 案件字面。
- 塊 `Fy47` 所改之既有之器（`11` 檔·其判式⛔ 變）：`probe_WG9385_k974.py`（`W7`）、`probe_WG9363_k953.py`（`W7`）、`probe_WG9367_adj4.py`（`W5`）、`probe_WG9370_adj4mut.py`（`X2`）、`probe_WG9387_k961h.py`（`X3`）、`probe_WG9388_k961s3.py`（`X3`）、`probe_WG9389_trialstop.py`（`X1`〔帶號之 raise 之數 ＝ 基準 ＋ `k980_acq_check` 內之恰一〕、`X3`）、`probe_WG9390_k961r.py`（`X2`）、`probe_WG9391_k980x.py`（`W6`）——各增 `NEW392`（四新名）、`W392`（四新名 ＋ `_solve_G_one`、`end_block_host`、`f3_screen_stepg_run`、`_WF_NS_NAMES`）之許；另四器之本案之錨以追加之句更之（⛔ 上列一字不刪）：`probe_WG9363_k953.py` 之 `R3_EXPECT` 之 `R1` 之抵費地（`851.68`／`851.67` → `851.69`）、`probe_WG9367_adj4.py` 之 `R3_EXPECT` 之 `R3` 之抵費地（3.5 m `(1659.06, 1651.41)` → `(1659.06, 1651.40)`；0 m `(1659.05, 1651.41)` → `(1659.06, 1651.40)`）、`probe_WG9375_k965.py` 之 `run` 之配地列（3.5 m `628-22(2)` `520.43`、`628-37(1)` `214.98`、`628-47(1)` `365.83`；0 m `628-47(1)` `365.83`）、`probe_WG9361_k954.py` 之 `run` 之 `R4` 之抵費地（3.5 m `R3` `1883.03` → `1883.05`、`R5` `1742.99` → `1742.98`）——其源 ＝ 主線 `56c77fd` 之碼而唯其求解之容差換為 `1e-6`（KL `05:22` 之甲）之發單端之實跑（其終態之子集 ＝ KL 所核之請示表之甲之欄）；四器之 `run` 於前態紅、施後綠；細目見 `§五-1` 項 `2`。

### `§三-3`　禁改（既有閘之錨·執行端撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計·含註解與 docstring）。🔒 本單之受詞之例（發單端以原型實測）：`end_block_host` 之 `_trial` 之舊之解之句去之而⛔ 移入 `end_block_trial_G` 之逐字（其變數之名須異·原型用 `_dd392`／`_bp392`／`_r392`）；四處之自我檢查⛔ 照抄鏈之既有之句；新之註解、docstring 之折行⛔ 令一列以四個以上之空白繼以中文起首（錨含「縮排之空白 ＋ 中文」之子字串）；基準中恰一之函式名（含巢狀）於工作樹仍恰一。執行端撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
2. **突變之錨**（`F13`／`F16`／`F17`／`F23`／`F27`／`F28`／`F29` 之突變）：其錨須仍於其函式內**恰一見**——新碼⛔ 照抄既有之句（以子字串計）。
3. **`main` ⛔ 動**（`F30 wiring` 之 `W7`）。
4. **頂層**：`app.py` 之頂層之名之增恰 `{K980_G_TOL, K980_G_MAX_ITER, k980_acq_check, end_block_trial_G}`、無減；頂層節點之相異 ＝ 此四 ∪ `{_WF_NS_NAMES, _solve_G_one, end_block_host, f3_screen_stepg_run}`；`verify/stepg_pipeline.py` 之頂層節點之相異 ＝ `{_run_step_g_impl}`（其頂層之名⛔ 變·簽名⛔ 變）；`verify/selection_pipeline.py`、`verify/run_verification.py` 一字⛔ 動。
5. **⛔ 案件字面**（`F36 wiring` 之 `W7`）：新增或改之頂層節點內⛔ 新增合 `^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$` 之字串常數。
6. 既有之函式之簽名之既有參數、回傳之形⛔ 改。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

本單之行為 ＝ 塊 `K38` 之二之【工】之讀法（以交付之通知告 KL·⛔ 涉域上之新判）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地之改變 ≠ `§一` 項 `5` 之表（含多一項、少一項）；本案之二退縮之任一取得之宗觸 `R-2` 之停機；應分配面積另有不經 `_solve_G_one` 之求解（全倉之生產碼 `34` 檔）、或評選另有 `R-3`／`R-4` 未及之式；取得之宗之於實配另有 `R-4` 未及之處（如鏈首以外之取得之宗）。

### `§三-5`　執行端之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-6`）：落於何處、其字樣；`R-4` 之四處之所在（函式、列）與其評選之式之引數之源（逐一對照 `app.py` 之 Step L 之 `_corner_block_true_G` 之呼叫、`verify/selection_pipeline.py` 之 `run_corner_pk` 之同呼叫、`end_block_host` 之 `_trial`·附其列）；`_solve_G_one`、`_corner_first_lot_G`、`end_block_trial_G` 之一切呼叫處之全列；對 `§三-3` 各款之自查。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/stepg_pipeline.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-392-k980g`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-392_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-392 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-392-k980g`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`52`**、主線仍 ＝ `56c77fd…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-392-k980g`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy47` 抽為 `<O>/Fy47.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`12` 檔（`11` 改·`1` 新）之 `git hash-object` ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `12` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-392 工項一：量測器（F36 之新器·既有之器十一之增許與更錨）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-392-k980g`。

**工項二　生產碼**（🔴 `app.py`、`verify/stepg_pipeline.py`·執行端依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`·`發單端.md` 丙 3之一之三份）：
1. **(甲) 本單新增或修改之量測器之呼叫**（照跑·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`§五-1` 項 `8` 之表之 `#1`, `#2`, `#3`, `#4`, `#5`, `#17`, `#6`, `#13`, `#18`, `#7`, `#19`, `#14`, `#15`, `#16`, `#44`, `#45`, `#46`, `#62`, `#63`, `#64`, `#65`, `#66`, `#69`, `#70`, `#71`, `#72`, `#73`, `#74`, `#75`, `#76`, `#77`, `#78`, `#79`, `#80`（`34` 呼叫·其命令逐字見該表）：`#78` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`#79` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']；rc 1`；`#80` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`#16`、`#17`、`#18`、`#46` ⇒ `rc 1`·末列逐字 ＝ 該表之工項一之端之列（其錨已更·前態之對照組）；其餘 `27` 呼叫 ⇒ `rc 0`·末列 ＝ 該表之同列；諸呼叫之 `stderr` 皆 `0` B。
2. **(乙) 本案配地之前後比對之前態**（照跑）：`python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_pre_35.json`；同 `0.0` ⇒ `<O>/k6s3_pre_00.json`；`python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_pre_35.json`；同 `0.0` ⇒ `<O>/f8_pre_00.json`；`python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_pre.json`；同 `0.0` ⇒ `<O>/parity00_pre.json`（皆 `rc 0`·末列 ＝ `§五-1` 項 `8` 之 `#56`〜`#61` 之工項一之端之列；`f8_pre_35.json`、`f8_pre_00.json` 之 `git hash-object` ＝ `8be0160bc14dd92a5331f86eecc995cae0507376`、`6fb86647807f9744594071be25c522b6b506c230`）。
3. **(丙) 本單未動之量測器之呼叫**（`§五-1` 項 `8` 之表之 `#1`〜`#77` 中 (甲)(乙) 以外之 `40` 呼叫）：`§零-0` 項 `6` 之比對皆同（主線之端 ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81` ＝ 基準之 sha、`python3 --version`、`pip freeze` 之 `sha256` ＝ 基準所載）⇒ **沿用** `基準/56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81.md` 之值、⛔ 重跑；任一不同 ⇒ 整份照跑（其期 ＝ 該表之工項一之端之列·皆 `rc 0`）。回報記其比對與所為。
4. `git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py`（逐一）：「GB-206」「k980_acq_check」「end_block_trial_G」「K980_G_TOL」⇒ 各**無出艙**、`rc 1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：執行端依 `§三` 撰寫二檔之改動；`python3 -m py_compile app.py verify/stepg_pipeline.py`；`commit` 訊息之首列逐字 `W-G.9-392 工項二：每宗之應分配面積試算至穩定·取得之宗之自我檢查（K-9-80 ③·KL 05:22 甲）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>/*_post.*`·🔒 一律從頭整套照跑·⛔ 沿用基準）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy47` 所改、所增之器之呼叫（`34` 呼叫·前置 `1` 之列） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F36 selftest` 之 `G1`〜`G4`、`H1`〜`H5`、`E1`〜`E5` 與 `P0 14／14`、`F36 wiring` 之 `W1`〜`W7`、`F36 run` 之 `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0` 皆 ✅ |
| `V-2` | 其餘之呼叫（`§五-1` 之「項 `8` 之表」之 `#1`〜`#77` 中 `V-1` 與 `#56`〜`#61` 以外者·其命令逐字見該表） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` |
| `V-3` | `V-1`〜`V-2` 之器之載入 | 本批所改、所增之器 `12` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_post_35.json`；同 `0.0`；`python3 verify/probes/probe_WG9392_k980g.py diff <O>/k6s3_pre_35.json <O>/k6s3_post_35.json`；同 `00`；`… probe_WG9344_k6s3.py cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json`；同 `00` | `run` 皆 `rc 0`；`F36 diff` 皆 `rc 0`，其出艙之全文（項之列與末列）＝ `§一` 項 `5` 之逐字（3.5 m `全比相異 6 項`、0 m `全比相異 5 項`）；`cmp` 皆 `rc 1`、末列逐字 `相異 1 項 ⇒ 🔴 異`（其項 ＝ `R1-抵費地-1`）——**本案之配地之改變 ＝ `§一` 項 `5`** |
| `V-5` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_post.json`；同 `0.0` ⇒ `<O>/parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`（畫面與 harness 之配地同）；落檔與 `stdout` 對前置 `2` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異） |
| `V-6` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_post_35.json`；同 `0.0` ⇒ `<O>/f8_post_00.json`；`git hash-object <O>/f8_pre_35.json <O>/f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列**相異**：施後 ＝ 3.5 m `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、0 m `884e91714a79288406faa4def6518847de36de39`（雲端 Linux·README 第六節第 5 款；異平台者以下之逐欄之差為準）；二落檔以 JSON 之逐欄比（`python3 -c` 讀二檔、遞迴比其鍵與值·其式與出艙入報告）之差唯：3.5 m `/rows[16]/G(㎡)` `268.33` → `268.34`、`/dropped/R2/left[0]/G(㎡)` `3.81` → `3.82`；0 m `/dropped/R2/left[0]/G(㎡)` `3.81` → `3.82` |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/stepg_pipeline.py`）；其增／刪之數與其 blob 出艙（發單端復驗時自倉重算·⛔ 預載）；`verify/` 之一切檔對工項一之端相異唯 `verify/stepg_pipeline.py`；二檔之頂層之名與相異之節點 ＝ `§三-3` 第 `4` 款（AST） |
| `V-8` | `R-1`〜`R-5` 之字樣（`git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py`·逐一） | 「GB-206」⇒ `app.py` ≥ `1`；「k980_acq_check」⇒ `app.py` ≥ `4`、`verify/stepg_pipeline.py` ≥ `2`；「end_block_trial_G」⇒ `app.py` ≥ `4`、`verify/stepg_pipeline.py` ≥ `2`；「K980_G_TOL」⇒ `app.py` ≥ `2`（其數出艙·判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**；逾時之重跑依單首 🔑）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞（求解之精度與取得之宗之自我檢查）之本案之果由 `V-4`〜`V-6` 與 `F36 run` 直接量之。

**唯讀獨立審查**（驗皆符後、推前）：執行端另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：`R-1` 之受詞之全（應分配面積之求解之他路之窮查·全倉生產碼 `34` 檔）；`R-4` 之四處之評選之式之引數與評選之處（`app.py` 之 Step L、`verify/selection_pipeline.py` 之 `run_corner_pk`、`end_block_host`）之逐一同源；自我檢查之停機於段三、入池閘、末端塊之合併再試之試算之內確上拋（`k6_trial_mark`／`k6_trial_raise_since` 之處）；右鏈之 `_adj` 之重試與自我檢查之交；`§三-3` 之六款；以獨立之合成之例（`F36` 之外·至少二例：其一 ＝ 一街廓之右側之街角第 1 宗之評選之上界 ≠ 實配之上界而舊碼二次之 `G` 異者；其二 ＝ 末端塊之當選者）比改前、改後之行為；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ 執行端修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-392-k980g`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K38` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `P49` 附於 `docs/待落地清單.md` 之末；塊 `G16` 附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；三檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>/checkidx.py`、`<O>/gen_fa_index.py`（⛔ 入倉）。
3. 三塊寫後：`python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-392 工項三：試算至穩定與取得之宗之自我檢查之讀法入典·GB-206 之立·待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-392-k980g`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-392R_試算至穩定與取得之宗之自我檢查_執行報告.md` ＋ 同目錄之 `W-G.9-392R_試算至穩定與取得之宗之自我檢查_差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之諸呼叫之全文、`V-4` 之 `F36 diff` 與 `cmp` 之全文、`V-5`／`V-6` 之比與其出艙、前置 (丙) 之版本之比對與所為、`80` 呼叫之 `rc`／`stderr`／耗時／末列之表〔前置與驗二態·沿用者具名·重跑者二趟並載〕）；④ 塊之實得（bytes／`sha256`）與三檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ 執行端之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **二檔之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**（並行之數）。收工閘之實測值出艙於回報（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-392 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-392-k980g`。其後依 `執行端.md` 丁回報於 `ops/queue`。

### `§四-2`　次單（⛔ 本單之期）

發單端復驗本批（自倉從頭重跑 `V-1`〜`V-9` 與收工閘·⛔ 沿用）⇒ 皆符而本案之配地之改變 ＝ `§一` 項 `5` ⇒ **`await_kl`**（README 第二節停止條件 `2`·新規格單而改本案配地）：請示 KL 核本案之配地之改變（附前後之比對）；KL 核可 ⇒ 入主線之短單（快轉 `56c77fd` → 新側支之端·⛔ `--force`·快轉前於 `ops/queue` 之 `log.md` 與 `STATE.json` 之 `history` 記前後值）＋ 立 `基準/<新主線之全 sha>.md`；其後 `W-G.9-393`（`K-9-61` ⑤、`GB-205`）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `probe_WG9361_k954.py` `3`／`0`、`probe_WG9363_k953.py` `9`／`0`、`probe_WG9367_adj4.py` `9`／`0`、`probe_WG9370_adj4mut.py` `4`／`0`、`probe_WG9375_k965.py` `9`／`0`、`probe_WG9385_k974.py` `5`／`1`、`probe_WG9387_k961h.py` `5`／`0`、`probe_WG9388_k961s3.py` `6`／`0`、`probe_WG9389_trialstop.py` `13`／`2`、`probe_WG9390_k961r.py` `6`／`0`、`probe_WG9391_k980x.py` `2`／`0`、`probe_WG9392_k980g.py` `567`／`0`（唯此 `12` 檔）（增／刪）；工項二 ＝ `app.py`、`verify/stepg_pipeline.py`（唯此二檔·其數出艙）；工項三 ＝ `K-6` 典 `61`／`0`、`docs/待落地清單.md` `21`／`0`、`GB` 簿 `12`／`0`（唯此三檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `56c77fd` | 生產碼相異恰 **`2`**（`app.py`、`verify/stepg_pipeline.py`）；`verify/` 之一切檔相異恰 **`13`**（`M` `12`：`stepg_pipeline.py`、`probes/probe_WG9361_k954.py`、`probes/probe_WG9363_k953.py`、`probes/probe_WG9367_adj4.py`、`probes/probe_WG9370_adj4mut.py`、`probes/probe_WG9375_k965.py`、`probes/probe_WG9385_k974.py`、`probes/probe_WG9387_k961h.py`、`probes/probe_WG9388_k961s3.py`、`probes/probe_WG9389_trialstop.py`、`probes/probe_WG9390_k961r.py`、`probes/probe_WG9391_k980x.py`；`A` `1`：`probes/probe_WG9392_k980g.py`）；本批之新檔（本單、新器、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`20` 檔：本單、`12` 器、生產碼二檔、`K-6` 典、`docs/待落地清單.md`、`GB` 簿、報告二檔） |
| `4` | 三檔之 bytes | `K-6` 典 `919452` → **`929829`**；`docs/待落地清單.md` `23233` → **`26144`**；`GB` 簿 `1063208` → **`1065227`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊；`CLAUDE.md`、自誤簿、`VR` 簿、`.claude/`、`verify/selection_pipeline.py`、`verify/run_verification.py` 對 `56c77fd` 相異 `0` |
| `5` | 自限 | 遠端 heads **`52`**；主線 ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（⛔ 變）；`verify/W-G.9-392-k980g` ＝ 工項四之 `commit`，其祖含 `56c77fd`；其餘 `51` 列中除 `ops/queue`（回報後可變）外之 `50` 列（含主線）逐列 ＝ `<O>/heads_before_392.txt` 之同列 |
| `6` | `python3 verify/probes/probe_WG9270_closegate.py 634 629 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 635 634 .` ⇒ `rc 7` |
| `7` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 634 629` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 `619`／`634`／缺號同 `§零-0` 項 `3`；**`GB` `198`／`206`**／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR`、`K-9` ＝ `§零-0` 項 `3` 之值（⛔ 變） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單端已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單端擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 塊 `Fy47` | `49006` B·`sha256` `4afe0b6e9fecb2a7374991f24c50eb983a4f03caef8e31ded159f36ff0379302`·`839` 列（圍欄內全文·末附換行）；抽為 `<O>/Fy47.diff`，`git apply` 於 `verify/probes/` 之 `12` 檔（`11` 改·`1` 新），其施前 blob（B）：`probe_WG9361_k954.py` `a115501330c198b1ce40f18289336f6d0f2ae108`（`34028`）、`probe_WG9363_k953.py` `2ce4dd5bb5f330c084e4667c44b13ddcd36f7825`（`128437`）、`probe_WG9367_adj4.py` `67af34857e44ed3b186091e096f28ef18c6ffb70`（`74366`）、`probe_WG9370_adj4mut.py` `1f1118b7457feb7aaa4c06d0abb3f361320075fa`（`21675`）、`probe_WG9375_k965.py` `e68ebe10ae39bdd5a697e52315f00d8d80e995a6`（`107446`）、`probe_WG9385_k974.py` `c5cf831b8b872c21987a370984e4eba985fca44a`（`44341`）、`probe_WG9387_k961h.py` `cf1d143df2ca188070a6787903753fe56e0798e5`（`24486`）、`probe_WG9388_k961s3.py` `a24ddf7e29c20ed6547e1fa847457881e76774e6`（`42532`）、`probe_WG9389_trialstop.py` `72ff303cb761bdc12a4402f70b7d8beb133512d0`（`34486`）、`probe_WG9390_k961r.py` `40b4b1b73f6aefd24bf8080c8da054fb8b3588d5`（`29744`）、`probe_WG9391_k980x.py` `80f6326ef5dea32b769e2423da0338cd86553fea`（`33297`）；`probe_WG9392_k980g.py` 施前⛔ 存 |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K38`／`P49`／`G16` | 塊 `K38` `10377` B·`sha256` `4221620f982d1cea9421d17fd0da27321b008b0c533172ca15681445da5a15df`·`61` 列；塊 `P49` `2911` B·`sha256` `85d8def1d73db3c126ccb80d1aae4deeefb8a3f2b2db1961a6513f858abeb8e3`·`21` 列；塊 `G16` `2019` B·`sha256` `f94b797c518d99da29d346b9236c3185e9399acb4fc92eba21e4d8a5371ac0c1`·`12` 列（三者皆圍欄內全文·末附換行·首列為空列）；`K38` 附於 `K-6_街角地分配程序與可分配判準.md`（`919452` B）之末 ⇒ `929829` B；`P49` 附於 `待落地清單.md`（`23233` B）之末 ⇒ `26144` B；`G16` 附於 `W-G.4_泛用阻塞項登記表.md`（`1063208` B）之末 ⇒ `1065227` B |
| `5` | 寫出後之 blob | 工項一之 `12` 器（`verify/probes/`·B）：`probe_WG9361_k954.py` ＝ `b39c2b0e7e10dbcf6ad7030b473d4111f4de2907`（`34375`）、`probe_WG9363_k953.py` ＝ `9f9fbd320236a2aa47ea33491d6e5bdae92ed92a`（`129271`）、`probe_WG9367_adj4.py` ＝ `16ecbec27c1799b4584710fa4c2bab7984eb07fd`（`75400`）、`probe_WG9370_adj4mut.py` ＝ `928509f813829fcf7e2461cef3f051a5ff63c5ae`（`22024`）、`probe_WG9375_k965.py` ＝ `4d74ea35066e4fcc3fa9f5df6e119a07c4ba5c63`（`108166`）、`probe_WG9385_k974.py` ＝ `e7ce70231f9656244577149db2088315634036b1`（`44777`）、`probe_WG9387_k961h.py` ＝ `8d018089a904d59c21258e942ee0ee85350f68de`（`25067`）、`probe_WG9388_k961s3.py` ＝ `68b165a039eea656b5a8340513dd2e15be84b3cf`（`43127`）、`probe_WG9389_trialstop.py` ＝ `f16fffc660975e63c3f684d4e512ee61fef00946`（`35586`）、`probe_WG9390_k961r.py` ＝ `d27f1c30a2f3fc48c3cdce0d8133140481ef9e86`（`30313`）、`probe_WG9391_k980x.py` ＝ `d99f637c563a56dc60abb74d993b4dfffa3c5640`（`33525`）、`probe_WG9392_k980g.py` ＝ `52d3c1c170f2441ca30d7b986d5f4d047aaf3caa`（`28529`·新）；工項三之三檔：`K-6_街角地分配程序與可分配判準.md` ＝ `e4ee674e22d70b16b97846526f3ff8f9afb3ce7a`（`929829` B）、`待落地清單.md` ＝ `be9a0229e6e230928708401d8e68cc013c4817ce`（`26144` B）、`W-G.4_泛用阻塞項登記表.md` ＝ `240317a7c1bac742607302bb987a031ca597d4a6`（`1065227` B）。🔒 生產碼二檔之施後 blob **⛔ 預載**（規格單·由執行端回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-391` 規格單 `§五-1` 項 `7`） |
| `8` | 量測器之二態（發單端實跑·倉外·雲端 Linux `4` 核） | 見本節末之「項 `8` 之表」（`80` 呼叫·二態之 `rc`／`stderr`／末列） |
| `9` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本單>`·發單端實跑（態 `56c77fd`·定稿之前一版·其後唯本列與項 `10` 之文字之填）：🔴 機械 `0` 項／🟡 提示 `8` 項——`P-2` 於塊 `G16` 之取號之列（其錨定框之式照 `GB-205` 之立項節之既有之形·二框〔錨定框、裸框 `-F`〕之數已並報）、`P-4` 六處（`§一`、`§三-2`、`§四-1` 之驗、`§四-3`、`§五-1` 之二態之對拍、塊 `K38` 之二甲——其箭頭皆為「改前 → 改後」之值或呼叫之鏈〔`_solve_G_one` → `solve_G_binary`〕·非方向之轉引）、`P-6` 於塊 `K38` 之四之表（其數 ＝ 本單之二甲之容差 `1e-6`、`_adj` 之 `0.5 ㎡` 之既有之碼之值·其出處皆具名於同節）⇒ **具名豁免**；ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23691`–`31434`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單端·⛔ `push`） | `git worktree add --detach <S> 56c77fd`（拋棄式·雲端 Linux）＋ 本單（定稿之前一版·其四塊與定稿逐位同）＋ 原型之二檔（代工項二）＋ 報告之替身·五 `commit`：塊之抽取 ＝ 項 `2`／`4`、塊 `CK`／`GF` ＝ 項 `7`；`git apply --check` 過；`12` 器之施後 blob ＝ 項 `5`、`git status --porcelain` 唯此 `12` 檔；前置 `4` 之四字樣皆 `rc 1`；工項二 ＝ `app.py` `75`／`10`、`verify/stepg_pipeline.py` `33`／`0`（原型）·`V-8` 之四字樣 ＝ 期（`app.py` 「GB-206」`2`、「k980_acq_check」`6`、「end_block_trial_G」`6`、「K980_G_TOL」`2`；`verify/stepg_pipeline.py` 「k980_acq_check」`4`、「end_block_trial_G」`2`）；三檔之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·逐位同；閘 `1` 之五筆之增刪 ＝ 該閘之期·首列 ＝ 所令逐字；閘 `2` ＝ 生產碼相異 `2`、`verify/` 相異 `13`（`M` `12`·`A` `1`）·新檔四之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `20` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `4` 前綴皆真·`CLAUDE.md` 等相異 `0`；閘 `6` `rc 0`（判別力 `635 634` ⇒ `rc 7`）；閘 `7` `rc 0`（自誤 `619`／`634`、**`GB` `198`／`206`**、`VR` `80`／`95`、`K-9` `77`／`80`）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `3`〜`5` 之實跑逐位同（`12` 器 ＝ 項 `5`、生產碼二檔 ＝ 原型） |

**項 `8` 之表**（`#1`〜`#77` ＝ `基準/56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81.md` 之呼叫〔其序與命令同之〕；`#78`〜`#80` ＝ `F36 selftest`／`F36 wiring`／`F36 run`；`#56`〜`#61` 之落檔之名：工項一之端 ⇒ `_pre`、施後 ⇒ `_post`；格 ＝ `rc`／`stderr` B／末列逐字；耗時（s）見括號·⛔ 為期。「工項一之端」之欄：前置 (甲) 之 `34` 呼叫 ＝ 發單端於 `56c77fd` ＋ 塊 `Fy47` 之實跑；其餘 `46` 呼叫 ＝ 基準之值〔前置 (乙)(丙)·其樹與工項一之端唯塊 `Fy47` 之 `12` 器異、其 `12` 器之呼叫皆入 (甲)〕。「施後」＝ 原型 ＋ 塊 `Fy47`·發單端實跑·並行 `2`）：

| # | 命令 | 工項一之端 | 施後（原型） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（106） | `0`／`0`／`⇒ 紅 []；rc 0`（108） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（347） | `0`／`0`／`⇒ 紅 []；rc 0`（364） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（35） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（35） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·45） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·18） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·286） | `0`／`0`／`⇒ 紅 []；rc 0`（203） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `1`／`0`／`⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1`（63） | `0`／`0`／`⇒ 紅 []；rc 0`（66） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `1`／`0`／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（398） | `0`／`0`／`⇒ 紅 []；rc 0`（433） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `1`／`0`／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（540） | `0`／`0`／`⇒ 紅 []；rc 0`（586） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（12） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（基準·80） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（91） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·483） | `0`／`0`／`⇒ 紅 []；rc 0`（362） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2221） | `0`／`0`／`⇒ 紅 []；rc 0`（1659） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·39） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·6） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（基準·25） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（24） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·25） | `0`／`0`／`⇒ 紅 []；rc 0`（19） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·298） | `0`／`0`／`⇒ 紅 []；rc 0`（220） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·424） | `0`／`0`／`⇒ 紅 []；rc 0`（308） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·42） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·42） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·8） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·27） | `0`／`0`／`⇒ 紅 []；rc 0`（24） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·19） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·13） | `0`／`0`／`⇒ 紅 []；rc 0`（11） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·231） | `0`／`0`／`⇒ 紅 []；rc 0`（173） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·59） | `0`／`0`／`⇒ 紅 []；rc 0`（44） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1131） | `0`／`0`／`⇒ 紅 []；rc 0`（739） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `1`／`0`／`⇒ 紅 ['R4']；rc 1`（135） | `0`／`0`／`⇒ 紅 []；rc 0`（138） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·136） | `0`／`0`／`⇒ 紅 []；rc 0`（110） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·499） | `0`／`0`／`⇒ 紅 []；rc 0`（306） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（基準·2） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（基準·12） | `0`／`0`／`紅項 [] 器紅 0`（10） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·497） | `0`／`0`／`⇒ 紅 []；rc 0`（313） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（基準·265） | `0`／`0`／`（JSON 之摘要列·略）`（176） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（基準·188） | `0`／`0`／`（JSON 之摘要列·略）`（124） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·257） | `0`／`0`／`⇒ 紅 []；rc 0`（172） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·183） | `0`／`0`／`⇒ 紅 []；rc 0`（125） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（基準·547） | `0`／`0`／`⇒ rc 0（不符 0 項）`（380） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（基準·387） | `0`／`0`／`⇒ rc 0（不符 0 項）`（270） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（292） | `0`／`0`／`⇒ 紅 []；rc 0`（312） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1584） | `0`／`0`／`⇒ 紅 []；rc 0`（1116） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1549） | `0`／`0`／`⇒ 紅 []；rc 0`（1094） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（111） | `0`／`0`／`⇒ 紅 []；rc 0`（112） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（383） | `0`／`0`／`⇒ 紅 []；rc 0`（406） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（290） | `0`／`0`／`⇒ 紅 []；rc 0`（304） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／`⇒ 紅 []；rc 0`（23） | `0`／`0`／`⇒ 紅 []；rc 0`（29） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（126） | `0`／`0`／`⇒ 紅 []；rc 0`（128） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']；rc 1`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（22） | `0`／`0`／`⇒ 紅 []；rc 0`（303） |

**二態之對拍**（發單端·上表之落檔）：`F36 diff`（`k6s3` 之二落檔之逐欄全比）二退縮之出艙 ＝ `§一` 項 `5` 之逐字（3.5 m `全比相異 6 項`、0 m `全比相異 5 項`）；`k6s3 cmp` 二退縮皆 `rc 1`·`相異 1 項 ⇒ 🔴 異`（`R1-抵費地-1`）；`F8` 之落檔 （`probe_WG9349_k9296.py run` 之落檔）：3.5 m `8be0160bc14dd92a5331f86eecc995cae0507376` → `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、0 m `6fb86647807f9744594071be25c522b6b506c230` → `884e91714a79288406faa4def6518847de36de39`；其逐欄之差唯 3.5 m 二欄（`/rows[16]/G(㎡)`〔`628-18(2)`〕`268.33` → `268.34`、`/dropped/R2/left[0]/G(㎡)`〔不配地之 `628-42(1)` 之試算 `G`〕`3.81` → `3.82`）、0 m 一欄（後者）；`parity` 二退縮之落檔與 `stdout` 前後逐位同（發單端之二態同在 `56c77fd` 之 `HEAD`·執行端之二態之 `HEAD` 異 ⇒ 依 `V-5` 代之） ⇒ **本案配地之改變 ＝ `§一` 項 `5`**。

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丁` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-392-k980g`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 回報 ⇒ `ops/queue` 之 `reports/W-G.9-392_規格單_回報.md`（`執行端.md` 丁）。

---

## 附錄甲　塊 `Fy47`（`git apply` 之差異·`verify/probes/` 之 `12` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9361_k954.py b/verify/probes/probe_WG9361_k954.py
index a115501330c198b1ce40f18289336f6d0f2ae108..b39c2b0e7e10dbcf6ad7030b473d4111f4de2907 100644
--- a/verify/probes/probe_WG9361_k954.py
+++ b/verify/probes/probe_WG9361_k954.py
@@ -77,6 +77,9 @@ S3_ROWS_35 = [
 NEW_PAIRS = (19, 15)   # 段三之輸入之切片中，新判為相連之對之數與其中同歸戶者之數（本案）
 G_35 = {"628-45(2)": 902.52, "628-45(1)": 525.28, "628-20(1)": 461.06}
 POOL_35 = {"R3": 1883.03, "R5": 1742.99, "R6": 1777.33}
+# 🔧 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「甲」·⛔ 上列一字不刪）：每宗之應分配面積試算至穩定（求解之容差 `1e-6 ㎡`）之後之抵費地之錨之更
+#   （源 ＝ 主線 `56c77fd` 之碼而唯其求解之容差換為 `1e-6`·發單端之實跑）。
+POOL_35 = dict(POOL_35, R3=1883.05, R5=1742.98)
 
 
 def _read(repo, rel):
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index 2ce4dd5bb5f330c084e4667c44b13ddcd36f7825..9f9fbd320236a2aa47ea33491d6e5bdae92ed92a 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -1526,6 +1526,11 @@ W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 KEEP_APP = tuple(x for x in KEEP_APP if x not in W391)
 APP_ALLOW |= set(W391)
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
+KEEP_APP = tuple(x for x in KEEP_APP if x not in W392)
+APP_ALLOW |= set(W392)
 
 
 def _top_dump(tree):
@@ -1668,6 +1673,10 @@ R3_EXPECT = {
         '628-7(1)': ('R6', 'right', 1007.91), '628-7(2)': ('R5', 'left', 712.26),
     }, {'R1': 851.67, 'R2': 1823.3, 'R3': 1659.05, 'R4': 697.4, 'R5': 1221.47, 'R6': 980.59}),
 }
+# 🔧 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「甲」·⛔ 上列一字不刪）：每宗之應分配面積試算至穩定（求解之容差 `1e-6 ㎡`）之後，
+#   `R1` 之抵費地逾本器之容差者之更（源 ＝ 主線 `56c77fd` 之碼而唯其求解之容差換為 `1e-6`·發單端之實跑；＝ KL 所核之請示表之甲之欄）。
+R3_EXPECT[3.5][1]['R1'] = 851.69
+R3_EXPECT[0.0][1]['R1'] = 851.69
 # 調配之輸入之類（切片數, 原有面積合計 ㎡）
 R4_EXPECT = {
     3.5: {'共同負擔用地·入合併單位': (32, 7116.89), '原位次配地': (73, 26311.71), '建築街廓內不能分配': (13, 1432.13), '無地號之殘料': (8, 0.0)},
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index 67af34857e44ed3b186091e096f28ef18c6ffb70..16ecbec27c1799b4584710fa4c2bab7984eb07fd 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -45,6 +45,7 @@
            `k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`、`calc_special_burden_total`、`main`（其接線與
            二函式之唯增列由 F30 之 wiring 量之）。
   🔧 `W-G.9-391`（`K-9-34`·`K-9-80` ④⑥·⛔ 上列一字不刪）：wiring 之 W5 之許增範圍之擴大之六新名與九函式（其行為與接線由 F35 量之）。
+  🔧 `W-G.9-392`（`K-9-80` ③·⛔ 上列一字不刪）：wiring 之 W5 之許增試算至穩定與取得之宗之自我檢查之四新名與四節點（其行為與接線由 F36 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, difflib, io, os, re, subprocess, sys, warnings
@@ -779,6 +780,10 @@ W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels
                  "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 ALLOW375_APP += W391
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
+ALLOW375_APP += W392
 
 
 def _git_show(repo, rev, rel):
@@ -1009,6 +1014,10 @@ R3_EXPECT = {
     3.5: ({"628-34(2)": (250.24, 257.91)}, {"R3": (1659.06, 1651.41)}),
     0.0: ({"628-34(2)": (250.24, 257.91)}, {"R3": (1659.05, 1651.41)}),
 }
+# 🔧 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「甲」·⛔ 上列一字不刪）：每宗之應分配面積試算至穩定（求解之容差 `1e-6 ㎡`）之後之 `R3` 之抵費地之錨之更
+#   （源 ＝ 主線 `56c77fd` 之碼而唯其求解之容差換為 `1e-6`·發單端之實跑；on 之值 ＝ KL 所核之請示表之甲之欄）。
+R3_EXPECT[3.5] = (R3_EXPECT[3.5][0], {"R3": (1659.06, 1651.40)})
+R3_EXPECT[0.0] = (R3_EXPECT[0.0][0], {"R3": (1659.06, 1651.40)})
 # 調配之輸入之類（切片數, 原有面積合計 ㎡）與合併單位數；off → on 之去者（歸戶）
 _R4_TOT = {"共同負擔用地·入合併單位": (31, 7103.74), "原位次配地": (74, 26324.86),
            "建築街廓內不能分配": (13, 1432.13), "無地號之殘料": (8, 0.0)}
diff --git a/verify/probes/probe_WG9370_adj4mut.py b/verify/probes/probe_WG9370_adj4mut.py
index 1f1118b7457feb7aaa4c06d0abb3f361320075fa..928509f813829fcf7e2461cef3f051a5ff63c5ae 100644
--- a/verify/probes/probe_WG9370_adj4mut.py
+++ b/verify/probes/probe_WG9370_adj4mut.py
@@ -119,6 +119,10 @@ W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 ALLOW373_APP += W391
 ALLOW375_FILES += F391
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
+ALLOW373_APP += W392
 
 
 def _strip_fns(src, names):
diff --git a/verify/probes/probe_WG9375_k965.py b/verify/probes/probe_WG9375_k965.py
index e68ebe10ae39bdd5a697e52315f00d8d80e995a6..4d74ea35066e4fcc3fa9f5df6e119a07c4ba5c63 100644
--- a/verify/probes/probe_WG9375_k965.py
+++ b/verify/probes/probe_WG9375_k965.py
@@ -1316,6 +1316,15 @@ EXP_ALLOC_DROPS[0.0] = (
     ],
 )
 
+# 🔧 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「甲」·⛔ 上列一字不刪）：每宗之應分配面積試算至穩定（求解之容差 `1e-6 ㎡`）之後之錨之更
+#   （源 ＝ 主線 `56c77fd` 之碼而唯其求解之容差換為 `1e-6`·發單端之實跑；同法之 `k6s3` 之終態之子集 ＝ KL 所核之請示表之甲之欄）。
+_U392 = {3.5: {("628-22(2)", "R5", "right"): 520.43, ("628-37(1)", "R1", "right"): 214.98, ("628-47(1)", "R3", "left"): 365.83},
+         0.0: {("628-47(1)", "R3", "left"): 365.83}}
+for _sb392, _u392 in _U392.items():
+    for _row392 in EXP_ALLOC_DROPS[_sb392][0]:
+        if tuple(_row392[:3]) in _u392:
+            _row392[3] = _u392[tuple(_row392[:3])]
+
 
 if __name__ == "__main__":
     sys.exit(main(sys.argv))
diff --git a/verify/probes/probe_WG9385_k974.py b/verify/probes/probe_WG9385_k974.py
index c5cf831b8b872c21987a370984e4eba985fca44a..e7ce70231f9656244577149db2088315634036b1 100644
--- a/verify/probes/probe_WG9385_k974.py
+++ b/verify/probes/probe_WG9385_k974.py
@@ -63,6 +63,9 @@ NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_wi
 W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                  "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
 TOL = 1e-9
 
 
@@ -505,8 +508,9 @@ def wiring(repo, base):
         # 🔧 `W-G.9-388`：同（`k6b_stage3_run`·`K-9-61` ①②③⑥·其行為由 F32 量之）
         # 🔧 `W-G.9-389`：同（試算內之程式之停機之上拋·F33 量之）
         # 🔧 `W-G.9-391`：同（範圍依最小建築面積之擴大·F35 量之）
+        # 🔧 `W-G.9-392`：同（試算至穩定與取得之宗之自我檢查·F36 量之）
         ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
-               | set(W389_APP) | set(W391)
+               | set(W389_APP) | set(W391) | set(W392)
                and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
         res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
     except Exception as e:
diff --git a/verify/probes/probe_WG9387_k961h.py b/verify/probes/probe_WG9387_k961h.py
index cf1d143df2ca188070a6787903753fe56e0798e5..8d018089a904d59c21258e942ee0ee85350f68de 100644
--- a/verify/probes/probe_WG9387_k961h.py
+++ b/verify/probes/probe_WG9387_k961h.py
@@ -45,6 +45,9 @@ NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_wi
 W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                  "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 # 外部錨（R3）：主線 `34736ab` 之 `probe_WG9351_intake.py run <repo>` 之「單位」列之原街廓（發單端 2026-10-17 實跑）
 EXPECT_RUN = {
@@ -278,6 +281,8 @@ def wiring(repo, base):
                       and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389))   # 🔧 `W-G.9-389`：同（F33 量之）
         ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) | set(NEW391) and set(bt) <= set(ct)
                       and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389) | set(W391))   # 🔧 `W-G.9-391`：同（F35 量之）
+        ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) | set(NEW391) | set(NEW392) and set(bt) <= set(ct)
+                      and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389) | set(W391) | set(W392))   # 🔧 `W-G.9-392`：同（F36 量之）
         res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", ok3,
                     f"增 {sorted(set(ct) - set(bt))}／去 {sorted(set(bt) - set(ct))}／相異 {dif}"))
         ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
diff --git a/verify/probes/probe_WG9388_k961s3.py b/verify/probes/probe_WG9388_k961s3.py
index a24ddf7e29c20ed6547e1fa847457881e76774e6..68b165a039eea656b5a8340513dd2e15be84b3cf 100644
--- a/verify/probes/probe_WG9388_k961s3.py
+++ b/verify/probes/probe_WG9388_k961s3.py
@@ -52,6 +52,9 @@ NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_wi
 W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                  "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
 
 try:
     sys.stdout.reconfigure(encoding="utf-8")
@@ -540,6 +543,9 @@ def wiring(repo, base):
     # 🔧 `W-G.9-391`：同（F35 量之）
     ok3 = ok3 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW389) | set(NEW391) and set(tb) <= set(ta)
                   and set(diff) <= {"k6b_stage3_run"} | set(W389) | set(W391))
+    # 🔧 `W-G.9-392`：同（F36 量之）
+    ok3 = ok3 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW389) | set(NEW391) | set(NEW392)
+                  and set(tb) <= set(ta) and set(diff) <= {"k6b_stage3_run"} | set(W389) | set(W391) | set(W392))
     print(("  ✅" if ok3 else "  🔴") + f" X3 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
     if not ok3:
         red.append("X3")
diff --git a/verify/probes/probe_WG9389_trialstop.py b/verify/probes/probe_WG9389_trialstop.py
index 72ff303cb761bdc12a4402f70b7d8beb133512d0..f16fffc660975e63c3f684d4e512ee61fef00946 100644
--- a/verify/probes/probe_WG9389_trialstop.py
+++ b/verify/probes/probe_WG9389_trialstop.py
@@ -47,6 +47,9 @@ NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_wi
 W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                  "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
 TAG_RE = re.compile(r"(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】")
 TRIAL_CALLS = {"f3_screen_stepg_run", "run_step_g", "trial", "alloc_eval"}
 CATCH = {"RuntimeError", "_K6BTrialStop", "Exception"}
@@ -512,8 +515,13 @@ def wiring(repo, base):
     # X1
     n_ok, bad, other = _x1(tree)
     bn_ok, bbad, _bo = _x1(btree)
-    res.append(("X1 帶號之 raise 皆 k6_program_stop·⛔ 他用", (not bad) and (not other) and n_ok == bn_ok + len(bbad)
-                and n_ok > 0, f"帶號 {n_ok}（基準之帶號 {bn_ok + len(bbad)}）／非者 {bad}／他用 {other}"))
+    # 🔧 `W-G.9-392`：其後之單之 `k980_acq_check`（`GB-206`）之帶號之 raise 恰一亦許（其行為由 F36 量之）
+    _kc392 = next((n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "k980_acq_check"), None)
+    _n392 = 0 if _kc392 is None else sum(1 for n in ast.walk(_kc392) if isinstance(n, ast.Raise)
+                                         and isinstance(n.exc, ast.Call) and getattr(n.exc.func, "id", None) == "k6_program_stop")
+    res.append(("X1 帶號之 raise 皆 k6_program_stop·⛔ 他用", (not bad) and (not other)
+                and (n_ok == bn_ok + len(bbad) or (_n392 == 1 and n_ok == bn_ok + len(bbad) + 1))
+                and n_ok > 0, f"帶號 {n_ok}（基準之帶號 {bn_ok + len(bbad)}·k980_acq_check {_n392}）／非者 {bad}／他用 {other}"))
     # X2
     try:
         ssrc = _read(repo, "verify/selection_pipeline.py")
@@ -542,6 +550,9 @@ def wiring(repo, base):
     ok3 = add == NEW_TOP and not gone and set(dif) <= ALLOW | ALLOW390 and not why
     # 🔧 `W-G.9-391`：其新名與所改之頂層節點亦許（⛔ 及 ALLOW 之二形之查·F35 量之）
     ok3 = ok3 or (add == NEW_TOP | set(NEW391) and not gone and set(dif) <= ALLOW | ALLOW390 | set(W391) and not why)
+    # 🔧 `W-G.9-392`：同（F36 量之）
+    ok3 = ok3 or (add == NEW_TOP | set(NEW391) | set(NEW392) and not gone
+                  and set(dif) <= ALLOW | ALLOW390 | set(W391) | set(W392) and not why)
     res.append(("X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形", ok3,
                 f"增 {sorted(add)}／去 {sorted(gone)}／相異 {dif}／不合 {why}"))
     # X4
diff --git a/verify/probes/probe_WG9390_k961r.py b/verify/probes/probe_WG9390_k961r.py
index 40b4b1b73f6aefd24bf8080c8da054fb8b3588d5..d27f1c30a2f3fc48c3cdce0d8133140481ef9e86 100644
--- a/verify/probes/probe_WG9390_k961r.py
+++ b/verify/probes/probe_WG9390_k961r.py
@@ -50,6 +50,9 @@ NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_wi
 W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                  "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
 F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
+NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
+W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
 
 
 def _harvest(repo):
@@ -409,6 +412,9 @@ def wiring(repo, base):
     # 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點亦許（F35 量之）
     ok2 = ok2 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW391) and set(tb) <= set(ta)
                   and set(diff) <= {"k6b_stage3_run"} | set(W391))
+    # 🔧 `W-G.9-392`：同（F36 量之）
+    ok2 = ok2 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW391) | set(NEW392) and set(tb) <= set(ta)
+                  and set(diff) <= {"k6b_stage3_run"} | set(W391) | set(W392))
     print(("  ✅" if ok2 else "  🔴") + f" X2 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
     if not ok2:
         red.append("X2")
diff --git a/verify/probes/probe_WG9391_k980x.py b/verify/probes/probe_WG9391_k980x.py
index 80f6326ef5dea32b769e2423da0338cd86553fea..d99f637c563a56dc60abb74d993b4dfffa3c5640 100644
--- a/verify/probes/probe_WG9391_k980x.py
+++ b/verify/probes/probe_WG9391_k980x.py
@@ -53,6 +53,7 @@ except Exception:  # noqa: BLE001
 
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 K6 = "K-9-80 ⑥"
+NEW392 = {"K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check"}   # 🔧 `W-G.9-392`
 NEW_TOP = {"K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check",
            "k980_mba"}
 
@@ -396,6 +397,7 @@ def wiring(repo, base):
     tn, tb = _top(srcs["app.py"]), _top(old)
     add, rem = set(tn) - set(tb), set(tb) - set(tn)
     ok6 = add == NEW_TOP and not rem
+    ok6 = ok6 or (add == NEW_TOP | NEW392 and not rem)   # 🔧 `W-G.9-392`：其後之單之四新名亦許（F36 量之）
     print(("  ✅" if ok6 else "  🔴") + f" W6 頂層之名之增 {sorted(add)}（期 {sorted(NEW_TOP)}）、減 {sorted(rem)}")
     if not ok6:
         red.append("W6")
diff --git a/verify/probes/probe_WG9392_k980g.py b/verify/probes/probe_WG9392_k980g.py
new file mode 100644
index 0000000000000000000000000000000000000000..52d3c1c170f2441ca30d7b986d5f4d047aaf3caa
--- /dev/null
+++ b/verify/probes/probe_WG9392_k980g.py
@@ -0,0 +1,567 @@
+# -*- coding: utf-8 -*-
+"""W-G.9-392 量測器（發單端擬·檔 F36·⛔ 由受單側改一字）：每宗之應分配面積之試算至穩定（`K-9-80` ③·KL `2026-10-22 05:22`
+「甲」）與取得之宗（街角第 1 宗、末端塊之當選者）之自我檢查。
+
+所量之性質：G 之二分求解收斂至 `K980_G_TOL`（㎡）後取至小數 2 位 ⇒ 其值⛔ 依二分之上界（`S_max`）而異（評選與實配之二次
+所算同值）；取得之宗於實配之末趟（`_commit`）以評選之式重算之值與實配之值取至 2 位不同 ⇒ 停機（`GB-206`·經
+`k6_program_stop` 登記·試算之內亦上拋·⛔ 靜默取其一）。
+
+子命令（一律 python3 verify/probes/probe_WG9392_k980g.py <子命令> …）：
+  selftest <repo>
+           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式）。玩具街廓 GA：矩形 x∈[0,60]、y∈[0,D]，正面 y ＝ 0、宗地分配線 ∥ y 軸，
+           無側街（`Rw` ＝ 0）⇒ 宗地之面積 ＝ `S·D`，法定式 `G ＝ (a(1−A·B) − S·l₂)(1−C)` 之不動點有解析解：
+           `S* ＝ a(1−A·B)(1−C) ／ (D ＋ l₂(1−C))`、`G* ＝ D·S*`（期值之源·⛔ 由受測之碼產）。A ＝ 1.2、B ＝ 0.3、C ＝ 0.25。
+           G1 D ＝ 15、l₂ ＝ 6、a ＝ 150 ＋ 1.37k（k ＝ 0〜299）：`_solve_G_one` 之 G 於二上界（街廓全長 60；`1.07·S* ＋ 0.31`）、
+              二座標系（原座標；旋轉 37°、鏡射、移至 TWD97 之尺度）之四解皆 ＝ `round(G*, 2)`（G* 距 0.005 之倍數 ＜ 1e-4 者略之·其數記之·量 ≥ 270）；
+           G2 同 G1 而 D ＝ 25、l₂ ＝ 2；
+           G3 邊界：G* ＝ 某值之半分之上 ＋2e-5、之下 −2e-5（由 G* 反求 a）⇒ 四解皆 ＝ `round(G*, 2)`（進、捨各一）；
+           G4 常數：`K980_G_TOL` ≤ 1e-6、`K980_G_MAX_ITER` ≥ 100。
+           H1 `k980_acq_check` 二值同（307.78、307.78）⇒ 回 None、登記⛔ 增；H2 二值異（307.79、307.78）⇒ RuntimeError，訊息含
+              「GB-206」「K-9-80 ③」與宗之暫編地號、二值，且 `K6_PROGRAM_STOPS` 增恰一（其全文 ＝ 訊息）；H3 未捨入異而取至 2 位同
+              （307.7849、307.7751）⇒ None；H4 取至 2 位恰差 0.01（300.02、300.01·浮點之差 ≤ 0.01）⇒ 停；H5 末端塊、右側之形 ⇒
+              停且訊息含「末端塊」「right」。
+           E1 `end_block_trial_G` 之左端：以替身之 `solve_one` 錄其引數 ⇒ (a, A, l₂, 0, 0, 街廓, d̂, p1, max(0.1,S), False, '無', 深度)
+              與 `_allocation_dir`、`_side_mid=None`、`_W_prev=0`、`_w0_start=0`、`_near_dir=None`、`_is_chain_head=True`、`_s_back`；
+           E2 右端 ⇒ 方向 −d̂、起點 p1 ＋ S·d̂；E3 S ＝ 0.05 ⇒ 上界 0.1；E4 側別非 left／right ⇒ 停機；E5 回 (G, S_raw)。
+           P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
+  wiring   <repo> <基準 commit>
+           W1 `_solve_G_one` 之 `solve_G_binary(` 之呼叫恰一，以 `tol=K980_G_TOL`、`max_iter=K980_G_MAX_ITER` 傳之；`app.py` 全檔之
+              `solve_G_binary(` 之呼叫恰一；
+           W2 `k980_acq_check(` 之呼叫：`f3_screen_stepg_run`（`app.py`）與 `_run_step_g_impl`（`verify/stepg_pipeline.py`）內各恰四
+              （街角第 1 宗、末端塊 × 左、右），各在一 `if`／`elif` 之下而其判式含 `_commit`；街角之二之評選之值 ＝
+              `_corner_first_lot_G(…)`、末端塊之二 ＝ `end_block_trial_G(…)[0]`；側別之字面 left／right 各二；
+           W3 `end_block_host` 內 `end_block_trial_G(` 之呼叫恰一、`solve_one(` 之直呼為零；
+           W4 `verify/stepg_pipeline.py` 經 `ns[…]` 取之新名皆在 `app.py` 之 `_WF_NS_NAMES`；
+           W5 `app.py` 之頂層之名之增恰 `{K980_G_TOL, K980_G_MAX_ITER, end_block_trial_G, k980_acq_check}`、無減；
+           W6 `k980_acq_check` 之內呼叫 `k6_program_stop` 且含字面「GB-206」；
+           W7 新增或改之頂層節點內⛔ 新增案件字面。
+  run      <repo> [<退縮> …]
+           harness 實跑本案（預設退縮 `3.5`、`0.0`·段三之入口 `run_corner_pk_k6b` ＋ `run_step_g`）：
+           R1 取得之宗之自我檢查之呼叫 ≥ 1（街角第 1 宗、末端塊各 ≥ 1）且皆過、⛔ 停機；評選（`_corner_first_lot_G` 之所錄）與
+              終態之街角第 1 宗以（暫編地號、側、a）配對者皆同值（配對 ≥ 1）；末端塊之評選之紀錄之當選者之試算 G 與終態同（其 a 未變者·其數記之·本案之當選者皆已受同一地主之併入 ⇒ `0`·其一致由自我檢查之「末端塊」之呼叫量之）；
+           R2 本案之錨（KL `2026-10-22 05:22` 所核之請示表〔`ops/queue` 之 `待KL/2026-10-22_街角地評選與實配之面積差.md`〕
+              之「甲」之欄）：`628-18(1)` 307.78（二退縮）、`628-18(2)` 268.34（3.5 m）／259.13（0 m）、抵費地 R1 851.69、R3 1651.40、
+              R4 697.39、R5 1221.45（3.5 m）／1221.46（0 m）、R6 980.58（二退縮）。
+  diff     <pre.json> <post.json>
+           `probe_WG9344_k6s3.py run` 之二落檔之逐欄之全比（⛔ 容差）：逐宗（街廓、暫編地號、推進之側）之 `a 面積(㎡)`、`G(㎡)`、
+           `驗_總判`、`驗_宗序`、`歸戶`，抵費地之 `面積`、`容納內接矩形`，`wins`、`forced`、`dropped`、`err`；逐項出艙一列、末列
+           `全比相異 <n> 項`（rc 0·其項之期由單定之）。
+rc：0 相符／1 不符／2 用法錯。
+"""
+import ast, contextlib, copy, io, math, os, re, subprocess, sys
+
+try:
+    sys.stdout.reconfigure(encoding="utf-8")
+except Exception:  # noqa: BLE001
+    pass
+
+CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
+NEW_TOP = {"K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check"}
+GB = "GB-206"
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
+# ───────────────────────── selftest ─────────────────────────
+
+def _xf(ang_deg, mirror, tx, ty):
+    import numpy as np
+    c, s = math.cos(math.radians(ang_deg)), math.sin(math.radians(ang_deg))
+
+    def f(p):
+        x, y = float(p[0]), float(p[1])
+        if mirror:
+            x = -x
+        return np.array((c * x - s * y + tx, s * x + c * y + ty))
+
+    def v(d):
+        x, y = float(d[0]), float(d[1])
+        if mirror:
+            x = -x
+        return np.array((c * x - s * y, s * x + c * y))
+    return f, v
+
+
+_A, _B, _C, _L = 1.2, 0.3, 0.25, 60.0
+
+
+def _gstar(a, D, lf):
+    s = a * (1 - _A * _B) * (1 - _C) / (D + lf * (1 - _C))
+    return D * s, s
+
+
+def _solve(ns, a, smax, frame, D, lf):
+    from shapely.geometry import Polygon
+    f, v = frame
+    poly = Polygon([f(p) for p in [(0, 0), (_L, 0), (_L, D), (0, D)]])
+    ad = ns["alloc_normal_axis"](v((0, 1)))
+    r, _ = ns["_solve_G_one"](a_m2=a, A=_A, l_front=lf, l_side=0.0, F=0.0, blk_poly=poly, d_hat=v((1, 0)),
+                              baseline_pt=f((0, 0)), S_max=smax, is_corner=False, side="左側", avg_depth=D, B=_B, C=_C,
+                              tab6_burden=_B + _C, allocation_dir=ad, side_mid=None, W_prev=0.0, near_dir=None,
+                              w0_start=0.0, is_chain_head=True, s_back=0.0)
+    return float(r["G"])
+
+
+def _sweep(ns, D, lf, avals):
+    fr0 = _xf(0, False, 0.0, 0.0)
+    fr1 = _xf(37, True, 307123.4, 2654321.7)
+    bad, skip, n = [], 0, 0
+    for a in avals:
+        g, s = _gstar(a, D, lf)
+        if abs(((g * 100.0) % 1.0) - 0.5) < 1e-2:      # G* 距 0.005 之倍數 ＜ 1e-4 ⇒ 略（期值之捨入不穩）
+            skip += 1
+            continue
+        exp = round(g, 2)
+        got = [_solve(ns, a, sm, fr, D, lf) for sm in (_L, 1.07 * s + 0.31) for fr in (fr0, fr1)]
+        n += 1
+        if any(x != exp for x in got):
+            bad.append((round(a, 4), exp, got))
+    return n, skip, bad
+
+
+def selftest(repo):
+    ns, _ = _harvest(repo)
+    need = ["_solve_G_one", "k980_acq_check", "end_block_trial_G", "K980_G_TOL", "K980_G_MAX_ITER",
+            "k6_program_stop", "K6_PROGRAM_STOPS", "alloc_normal_axis"]
+    miss = [n for n in need if n not in ns]
+    if miss:
+        print(f"  🔴 受詞缺 {miss}")
+        print("⇒ 紅 ['受詞缺']；rc 1")
+        return 1
+    C = []
+    av = [150.0 + 1.37 * k for k in range(300)]
+    n1, sk1, b1 = _sweep(ns, 15.0, 6.0, av)
+    C.append(("G1 D 15·l₂ 6：二上界 × 二座標系之 G ＝ round(G*, 2)", (n1 >= 270, b1[:3]), (True, [])))
+    n2, sk2, b2 = _sweep(ns, 25.0, 2.0, av)
+    C.append(("G2 D 25·l₂ 2：同 G1", (n2 >= 270, b2[:3]), (True, [])))
+    g3 = []
+    for base_, sgn in ((431.235, 1.0), (431.245, -1.0)):           # 半分之上（進）、之下（捨）
+        gt = base_ + sgn * 2e-5
+        a = gt / 15.0 * (15.0 + 6.0 * (1 - _C)) / ((1 - _A * _B) * (1 - _C))
+        g, s = _gstar(a, 15.0, 6.0)
+        fr1 = _xf(37, True, 307123.4, 2654321.7)
+        got = [_solve(ns, a, sm, fr, 15.0, 6.0) for sm in (_L, 1.07 * s + 0.31) for fr in (_xf(0, False, 0, 0), fr1)]
+        g3.append((round(g, 2), got))
+    C.append(("G3 邊界：G* 於半分之上 2e-5 ⇒ 進、之下 2e-5 ⇒ 捨（四解皆同）",
+              [(e, all(x == e for x in got)) for e, got in g3], [(431.24, True), (431.24, True)]))
+    C.append(("G4 常數：K980_G_TOL ≤ 1e-6、K980_G_MAX_ITER ≥ 100",
+              (float(ns["K980_G_TOL"]) <= 1e-6, int(ns["K980_G_MAX_ITER"]) >= 100), (True, True)))
+    chk = ns["k980_acq_check"]
+    stops = ns["K6_PROGRAM_STOPS"]
+
+    def call(*a):
+        n0 = len(stops)
+        try:
+            r = chk(*a)
+            return ("過", r, len(stops) - n0, "")
+        except RuntimeError as e:
+            m = str(e)
+            reg = (len(stops) - n0, (stops[-1] == m) if len(stops) > n0 else False)
+            return ("停", None, reg, m)
+    h1 = call("街角第1宗", "GA", "right", "X-1(1)", 307.78, 307.78)
+    C.append(("H1 二值同 ⇒ 過（回 None·登記⛔ 增）", h1[:3], ("過", None, 0)))
+    h2 = call("街角第1宗", "GA", "right", "X-1(1)", 307.79, 307.78)
+    C.append(("H2 二值異 ⇒ 停（GB-206·K-9-80 ③·宗·二值·登記增恰一而全文同）",
+              (h2[0], h2[2], all(t in h2[3] for t in (GB, "K-9-80 ③", "X-1(1)", "307.79", "307.78"))),
+              ("停", (1, True), True)))
+    h3 = call("街角第1宗", "GA", "left", "X-2(1)", 307.7849, 307.7751)
+    C.append(("H3 取至 2 位同 ⇒ 過", h3[:3], ("過", None, 0)))
+    h4 = call("街角第1宗", "GA", "left", "X-3(1)", 300.02, 300.01)
+    C.append(("H4 取至 2 位恰差 0.01 ⇒ 停", (h4[0], h4[2]), ("停", (1, True))))
+    h5 = call("末端塊", "GA", "right", "X-4(1)", 500.00, 500.01)
+    C.append(("H5 末端塊·右 ⇒ 停（訊息含末端塊、right）", (h5[0], "末端塊" in h5[3], "right" in h5[3]), ("停", True, True)))
+    import numpy as np
+    rec = []
+
+    def stub(*a, **k):
+        rec.append((a, k))
+        return ({"G": 123.456, "S_raw": 7.89, "S": 7.89}, "替身")
+    tg = ns["end_block_trial_G"]
+    d = np.array((0.6, 0.8)); p1 = np.array((307000.0, 2654000.0)); ad = np.array((-0.8, 0.6))
+    rec.clear()
+    r1 = tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 42.0, 18.0, ad, "left", 3.25)
+    a1, k1 = rec[0]
+    C.append(("E1 左端之引數", (a1[:5], a1[5], tuple(np.round(a1[6], 9)), tuple(np.round(a1[7], 6)), a1[8:],
+                             (tuple(np.round(k1.get("_allocation_dir"), 9)), k1.get("_side_mid"), k1.get("_W_prev"),
+                              k1.get("_w0_start"), k1.get("_near_dir"), k1.get("_is_chain_head"), k1.get("_s_back"))),
+              ((321.5, 1.25, 0.7, 0.0, 0.0), "POLY", (0.6, 0.8), (307000.0, 2654000.0), (42.0, False, "無", 18.0),
+               ((-0.8, 0.6), None, 0.0, 0.0, None, True, 3.25))))
+    rec.clear()
+    tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 42.0, 18.0, ad, "right", 0.0)
+    a2, k2 = rec[0]
+    C.append(("E2 右端：方向 −d̂、起點 p1 ＋ S·d̂", (tuple(np.round(a2[6], 9)), tuple(np.round(a2[7], 6)), k2.get("_s_back")),
+              ((-0.6, -0.8), (307025.2, 2654033.6), 0.0)))
+    rec.clear()
+    tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 0.05, 18.0, ad, "left", 0.0)
+    C.append(("E3 S ＝ 0.05 ⇒ 上界 0.1", rec[0][0][8], 0.1))
+    try:
+        tg(stub, 321.5, 1.25, 0.7, "POLY", d, p1, 42.0, 18.0, ad, "中段", 0.0)
+        e4 = "過"
+    except RuntimeError:
+        e4 = "停"
+    C.append(("E4 側別非 left／right ⇒ 停機", e4, "停"))
+    C.append(("E5 回 (G, S_raw)", tuple(r1), (123.456, 7.89)))
+    red = []
+    for name, got, exp in C:
+        ok = got == exp
+        print(("  ✅ " if ok else "  🔴 ") + name)
+        if not ok:
+            print(f"       得 {got!r}"[:700])
+            print(f"       期 {exp!r}"[:700])
+            red.append(name.split()[0])
+    print(f"  ℹ️ G1 量 {n1}·略 {sk1}；G2 量 {n2}·略 {sk2}")
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
+def _git(repo, *a):
+    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
+    return r.stdout.decode("utf-8") if r.returncode == 0 else ""
+
+
+def _callee(n):
+    f = n.func
+    if isinstance(f, ast.Name):
+        return f.id
+    if isinstance(f, ast.Attribute):
+        return f.attr
+    if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant) and isinstance(f.slice.value, str):
+        return f.slice.value
+    return None
+
+
+def _calls(tree, name):
+    return [n for n in ast.walk(tree) if isinstance(n, ast.Call) and _callee(n) == name]
+
+
+def _fn_node(tree, name):
+    for n in tree.body:
+        if isinstance(n, ast.FunctionDef) and n.name == name:
+            return n
+    return None
+
+
+def _top(src):
+    out = {}
+    for n in ast.parse(src).body:
+        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
+            out[n.name] = ast.dump(n)
+        elif isinstance(n, ast.Assign):
+            for t in n.targets:
+                if isinstance(t, ast.Name):
+                    out[t.id] = ast.dump(n)
+    return out
+
+
+def _guarded(fn):
+    """{呼叫節點: 其所在之 if 之判式之名之集}（最近之一層 if／elif）。"""
+    out = {}
+
+    def walk(node, test_names):
+        for ch in ast.iter_child_nodes(node):
+            if isinstance(ch, ast.If):
+                names = {x.id for x in ast.walk(ch.test) if isinstance(x, ast.Name)}
+                for b in ch.body:
+                    walk_one(b, names)
+                for b in ch.orelse:
+                    walk_one(b, names if not (len(ch.orelse) == 1 and isinstance(b, ast.If)) else test_names)
+            else:
+                walk_one(ch, test_names)
+
+    def walk_one(node, names):
+        if isinstance(node, ast.Call) and _callee(node) == "k980_acq_check":
+            out[node] = names
+        if isinstance(node, ast.If):
+            walk(ast.Module(body=[node], type_ignores=[]), names)
+            return
+        walk(node, names)
+    walk(fn, set())
+    return out
+
+
+def wiring(repo, base):
+    paths = ("app.py", "verify/stepg_pipeline.py")
+    srcs = {p: open(os.path.join(repo, p), encoding="utf-8").read() for p in paths}
+    old = _git(repo, "show", f"{base}:app.py")
+    if not old:
+        print(f"  🔴 基準 {base} 之 app.py 取不到")
+        print("⇒ 紅 ['基準缺']；rc 1")
+        return 1
+    trees = {p: ast.parse(s) for p, s in srcs.items()}
+    ta = trees["app.py"]
+    red = []
+    # W1
+    sg1 = _fn_node(ta, "_solve_G_one")
+    cs = _calls(sg1, "solve_G_binary") if sg1 else []
+    kw = {k.arg: k.value for k in cs[0].keywords} if len(cs) == 1 else {}
+    ok1 = (len(cs) == 1 and isinstance(kw.get("tol"), ast.Name) and kw["tol"].id == "K980_G_TOL"
+           and isinstance(kw.get("max_iter"), ast.Name) and kw["max_iter"].id == "K980_G_MAX_ITER"
+           and len(_calls(ta, "solve_G_binary")) == 1)
+    print(("  ✅" if ok1 else "  🔴") + f" W1 _solve_G_one 之 solve_G_binary 以 K980_G_TOL／K980_G_MAX_ITER（呼叫 {len(cs)}·全檔 {len(_calls(ta, 'solve_G_binary'))}）")
+    if not ok1:
+        red.append("W1")
+    # W2
+    w2 = []
+    for p, fname in (("app.py", "f3_screen_stepg_run"), ("verify/stepg_pipeline.py", "_run_step_g_impl")):
+        fn = _fn_node(trees[p], fname)
+        g = _guarded(fn) if fn else {}
+        combos = []
+        for c, names in g.items():
+            side = c.args[2].value if len(c.args) >= 3 and isinstance(c.args[2], ast.Constant) else None
+            ev = c.args[4] if len(c.args) >= 5 else None
+            kind = None
+            if isinstance(ev, ast.Call) and _callee(ev) == "_corner_first_lot_G":
+                kind = "街角"
+            elif (isinstance(ev, ast.Subscript) and isinstance(ev.value, ast.Call) and _callee(ev.value) == "end_block_trial_G"
+                  and isinstance(ev.slice, ast.Constant) and ev.slice.value == 0):
+                kind = "末端"
+            combos.append((str(kind), str(side), "_commit" in names))
+        ok_ = (len(g) == 4 and sorted(combos) == sorted([("街角", "left", True), ("街角", "right", True),
+                                                          ("末端", "left", True), ("末端", "right", True)]))
+        w2.append((p, len(g), ok_))
+    ok2 = all(x[2] for x in w2)
+    print(("  ✅" if ok2 else "  🔴") + f" W2 取得之宗之自我檢查之四處（{[(a, b) for a, b, _ in w2]}）")
+    if not ok2:
+        red.append("W2")
+    # W3
+    eh = _fn_node(ta, "end_block_host")
+    n_tg = len(_calls(eh, "end_block_trial_G")) if eh else -1
+    n_so = len(_calls(eh, "solve_one")) if eh else -1
+    ok3 = n_tg == 1 and n_so == 0
+    print(("  ✅" if ok3 else "  🔴") + f" W3 end_block_host 之評選經 end_block_trial_G（{n_tg}）·solve_one 之直呼 {n_so}")
+    if not ok3:
+        red.append("W3")
+    # W4
+    wf = next((n.value for n in ta.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
+               and t.id == "_WF_NS_NAMES" for t in n.targets)), None)
+    wfn = {e.value for e in getattr(wf, "elts", []) if isinstance(e, ast.Constant)}
+    used = {n.slice.value for n in ast.walk(trees["verify/stepg_pipeline.py"]) if isinstance(n, ast.Subscript)
+            and isinstance(n.value, ast.Name) and n.value.id == "ns" and isinstance(n.slice, ast.Constant)
+            and n.slice.value in NEW_TOP}
+    ok4 = bool(used) and used <= wfn
+    print(("  ✅" if ok4 else "  🔴") + f" W4 引擎經 ns 取之新名 {sorted(used)} ⊆ _WF_NS_NAMES（漏 {sorted(used - wfn)}）")
+    if not ok4:
+        red.append("W4")
+    # W5
+    tb, tn = _top(old), _top(srcs["app.py"])
+    add, rem = set(tn) - set(tb), set(tb) - set(tn)
+    ok5 = add == NEW_TOP and not rem
+    print(("  ✅" if ok5 else "  🔴") + f" W5 頂層之名之增 {sorted(add)}·減 {sorted(rem)}")
+    if not ok5:
+        red.append("W5")
+    # W6
+    kc = _fn_node(ta, "k980_acq_check")
+    ok6 = bool(kc) and len(_calls(kc, "k6_program_stop")) >= 1 and any(
+        isinstance(c, ast.Constant) and isinstance(c.value, str) and GB in c.value for c in ast.walk(kc))
+    print(("  ✅" if ok6 else "  🔴") + " W6 k980_acq_check 經 k6_program_stop 立 GB-206 之停機")
+    if not ok6:
+        red.append("W6")
+    # W7
+    chg = sorted(k for k in tn if tn.get(k) != tb.get(k))
+    lits = []
+    tbo = ast.parse(old)
+    for n in ta.body:
+        nm = getattr(n, "name", None) or (n.targets[0].id if isinstance(n, ast.Assign)
+                                          and isinstance(n.targets[0], ast.Name) else None)
+        if nm in chg:
+            ob = _fn_node(tbo, nm)
+            newc = {c.value for c in ast.walk(n) if isinstance(c, ast.Constant) and isinstance(c.value, str)
+                    and CASE_LIT_RE.match(c.value)}
+            oldc = {c.value for c in ast.walk(ob) if isinstance(c, ast.Constant) and isinstance(c.value, str)
+                    and CASE_LIT_RE.match(c.value)} if ob is not None else set()
+            lits += sorted((nm, x) for x in newc - oldc)
+    ok7 = not lits
+    print(("  ✅" if ok7 else "  🔴") + f" W7 新增或改之頂層節點（{len(chg)}）內新增之案件字面 {lits}")
+    if not ok7:
+        red.append("W7")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+# ───────────────────────── run ─────────────────────────
+
+# 本案之錨：KL `2026-10-22 05:22` 所核之請示表之「甲」之欄（⛔ 由受測之碼產）
+ANCHOR = {
+    3.5: ({"628-18(1)": 307.78, "628-18(2)": 268.34},
+          {"R1-抵費地-1": 851.69, "R3-抵費地": 1651.40, "R4-抵費地": 697.39, "R5-抵費地": 1221.45, "R6-抵費地": 980.58}),
+    0.0: ({"628-18(1)": 307.78, "628-18(2)": 259.13},
+          {"R1-抵費地-1": 851.69, "R3-抵費地": 1651.40, "R4-抵費地": 697.39, "R5-抵費地": 1221.46, "R6-抵費地": 980.58}),
+}
+
+
+def _one(repo, sb):
+    probes = os.path.join(repo, "verify", "probes")
+    if probes not in sys.path:
+        sys.path.insert(0, probes)
+    os.environ["WV_K6B_STAGE3"] = "on"
+    import probe_WG9344_k6s3 as K
+    ns, fst, snap, cb_by, cad, tp, bp, params = K._boot(repo, sb)
+    if "k980_acq_check" not in ns:
+        return None
+    import selection_pipeline as sp
+    calls, ev = [], []
+    o_chk = ns["k980_acq_check"]
+
+    def w_chk(kind, blk, side, pid, ge, ga):
+        calls.append((kind, blk, side, pid, round(float(ge), 2), round(float(ga), 2)))
+        return o_chk(kind, blk, side, pid, ge, ga)
+    ns["k980_acq_check"] = w_chk
+    o_cf = ns["_corner_first_lot_G"]
+    phase = {"p": "pk"}
+
+    def w_cf(**kw):
+        g = o_cf(**kw)
+        if phase["p"] == "pk":
+            lab = str(kw.get("_label", ""))
+            ev.append((lab.split("·")[1] if lab.count("·") >= 2 else None, {"左": "left", "右": "right"}.get(kw.get("side")),
+                       round(float(kw.get("a_m2")), 2), round(float(g), 2)))
+        return g
+    ns["_corner_first_lot_G"] = w_cf
+    with contextlib.redirect_stdout(io.StringIO()):
+        _d, _s, _o, wins, forced, _tp2, bp2 = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
+                                                                   snapshot=snap)
+    phase["p"] = "sg"
+    res = K._materialize(ns, fst, snap, cb_by, cad, params, tp, bp2, wins, forced, sb)
+    ebv = copy.deepcopy(fst.session_state.get(ns["SS_END_BLOCK_EVAL"]) or {})
+    a0 = {t["暫編地號"]: round(float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0), 2) for t in tp}
+    ns["k980_acq_check"] = o_chk
+    ns["_corner_first_lot_G"] = o_cf
+    return res, calls, ev, ebv, a0
+
+
+def run(repo, sbs):
+    red = []
+    for sb in sbs:
+        try:
+            got = _one(repo, sb)
+        except Exception as e:  # noqa: BLE001
+            print(f"  🔴 R1@{sb} 例外 {type(e).__name__}：{str(e)[:200]}")
+            red.append(f"R1@{sb}")
+            continue
+        if got is None:
+            print("  🔴 受詞缺（k980_acq_check）")
+            print("⇒ 紅 ['受詞缺']；rc 1")
+            return 1
+        res, calls, ev, ebv, a0 = got
+        rows = res["rows"]
+        # R1
+        kinds = {c[0] for c in calls}
+        bad_c = sorted({c for c in calls if c[4] != c[5]})
+        firsts = [r for r in rows if r.get("驗_宗序") == "街角第1宗"]
+        pairs, bad_p = 0, []
+        for r in firsts:
+            key = (r["暫編地號"], r["推進側別"], round(float(r["a 面積(㎡)"]), 2))
+            m = [e for e in ev if (e[0], e[1], e[2]) == key]
+            if m:
+                pairs += 1
+                if any(e[3] != round(float(r["G(㎡)"]), 2) for e in m):
+                    bad_p.append((key, sorted({e[3] for e in m}), r["G(㎡)"]))
+        eb_pairs, bad_e = 0, []
+        byk = {r["暫編地號"]: r for r in rows}
+        for blk, e in ebv.items():
+            for sd, v in e.items():
+                w = v.get("當選") if isinstance(v, dict) else None
+                if not w or w not in byk:
+                    continue
+                if round(float(byk[w]["a 面積(㎡)"]), 2) != a0.get(w):
+                    continue
+                gw = [c.get("試算G(㎡)") for c in v.get("候選", []) if c.get("暫編地號") == w]
+                eb_pairs += 1
+                if not gw or round(float(gw[0]), 2) != round(float(byk[w]["G(㎡)"]), 2):
+                    bad_e.append((blk, sd, w, gw, byk[w]["G(㎡)"]))
+        ok1 = (res["err"] is None and {"街角第1宗", "末端塊"} <= kinds and not bad_c and pairs >= 1 and not bad_p
+               and not bad_e)
+        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb} 自我檢查 {len(calls)} 次（{sorted(kinds)}·異 {bad_c[:3]}）；"
+              f"評選對終態之街角第 1 宗 配對 {pairs}·異 {bad_p[:3]}；末端塊 配對 {eb_pairs}·異 {bad_e[:3]}；err {res['err']}")
+        if not ok1:
+            red.append(f"R1@{sb}")
+        # R2
+        lots, pools = ANCHOR[sb]
+        gl = {r["暫編地號"]: r["G(㎡)"] for r in rows}
+        gp = {p["池"]: p["面積"] for p in res["pools"]}
+        bad2 = [(k, gl.get(k), v) for k, v in lots.items() if gl.get(k) != v] + \
+               [(k, gp.get(k), v) for k, v in pools.items() if gp.get(k) != v]
+        ok2 = not bad2
+        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb} 本案之錨（KL 05:22 所核之甲）不合 {bad2}")
+        if not ok2:
+            red.append(f"R2@{sb}")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def diff(pre, post):
+    import json
+    a = json.load(open(pre, encoding="utf-8"))
+    b = json.load(open(post, encoding="utf-8"))
+    out = []
+
+    def key(r):
+        return (str(r.get("所屬街廓")), str(r.get("暫編地號")), str(r.get("推進側別")))
+    ra = {key(r): r for r in a.get("rows") or []}
+    rb = {key(r): r for r in b.get("rows") or []}
+    for k in sorted(set(ra) | set(rb)):
+        x, y = ra.get(k) or {}, rb.get(k) or {}
+        for f in ("a 面積(㎡)", "G(㎡)", "驗_總判", "驗_宗序", "歸戶"):
+            if x.get(f) != y.get(f) or (k in ra) != (k in rb):
+                out.append(f"宗 {k[0]}·{k[1]}·{k[2]} {f} {x.get(f)!r} → {y.get(f)!r}")
+    pa = {p["池"]: p for p in a.get("pools") or []}
+    pb = {p["池"]: p for p in b.get("pools") or []}
+    for k in sorted(set(pa) | set(pb)):
+        for f in ("面積", "容納內接矩形"):
+            if (pa.get(k) or {}).get(f) != (pb.get(k) or {}).get(f):
+                out.append(f"抵費地 {k} {f} {(pa.get(k) or {}).get(f)!r} → {(pb.get(k) or {}).get(f)!r}")
+    for f in ("wins", "forced", "dropped", "err"):
+        if a.get(f) != b.get(f):
+            out.append(f"{f} 異")
+    for l in out:
+        print("  " + l)
+    print(f"全比相異 {len(out)} 項")
+    return 0
+
+
+def main(argv):
+    if len(argv) < 3:
+        print(__doc__)
+        return 2
+    cmd, repo = argv[1], os.path.abspath(argv[2])
+    if cmd == "diff":
+        if len(argv) != 4:
+            print("用法：diff <pre.json> <post.json>")
+            return 2
+        return diff(argv[2], argv[3])
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

## 附錄乙　塊 `K38`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

## 🔧 `W-G.9-392`：`K-9-80` ③ 之微差之吸收之落地——每宗之應分配面積試算至穩定後取至小數 2 位（評選與實配同值）、取得之宗之自我檢查（KL `2026-10-22 05:22`「是」·甲）（⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（`W-G.9-391` 入主線）之後；本節由 `W-G.9-392` 規格單（新側支 `verify/W-G.9-392-k980g`）入典，緊接上節（`W-G.9-391` 之節）之後。**授權** ＝ `W-G.9-386` 之節之一之 KL 之逐字（自動化之委任）。本節⛔ 鑄 `K-9` 之號：KL `05:22` 之答為 `K-9-80` ③ 之「其餘之重算之微差」之處置之擇（上節之二之辛之受詞），登記於本節；其是否另立一號，留 KL 或監看窗定之。

### 一、所據（KL 之語·逐字）

- 發單端之請示（`ops/queue` 之 `待KL/2026-10-22_街角地評選與實配之面積差.md`·`2026-10-22 03:35`）之【要你判斷】：「各宗之應分配面積（含評選與取得之街角地、末端塊），依「甲」（每宗試算至穩定後取兩位小數，評選與實際配地同值）辦理——**是／否**？（否者即依「乙」。）」
- 同檔之【要改成】之甲：「每一宗之應分配面積皆試算至穩定後，再取至小數點以下 2 位（第 3 位四捨五入）——評選與實際配地兩次應同值，其後重算亦不變（同一地主之併入除外）；並設自我檢查：取得之宗兩次所算若不同，即停下示訊。」
- **KL `2026-10-22 05:22`**（`ops/queue` 之 `KL答覆/2026-10-22_0522.md`·監看窗錄）：「是」。
- 所否之選項（乙）：「試算之精度不變，實際配地沿用評選時之算法（兩次正面可取之最長寬度一致）——兩次同值，所鎖定者為評選時之值。」

### 二、【工】之讀法（`W-G.9-392`·發單端·⛔ 充裁）

- **甲 試算至穩定**：應分配面積（`G`）之求解（`_solve_G_one` → `solve_G_binary`·其唯一之入口）之二分之收斂之容差 ＝ `1e-6 ㎡`（舊 `0.01 ㎡`）、次數之上限 ＝ `200`（舊 `80`）；收斂之後取至小數 2 位（`solve_G_binary` 之 `round(·, 2)` 照舊）。由：容差 `0.01` 之下，二分之上界不同（評選：右側之街角第 1 宗之上界為街廓於斜交軸之 s 域上界；實配：為扣除左側已配之寬之餘）則所停之處不同，`G` 之末位可差 `0.01`（本案 `R6` 右 `628-18(1)` 評選 `307.79`、實配 `307.78`）；容差 `1e-6` 之下，二次所算與其不動點之差皆 ≤ 約 `1e-6`，取至 2 位相異者唯其不動點落於半分（`…5`）之 `±1e-6` 之內者——其形由己之自我檢查停之。
- **乙 受詞**：每一宗（街角第 1 宗、末端塊、其餘一切之宗·`_solve_G_one` 之一切呼叫）。⛔ 及：街角之強制抵費地之帶之面積之二分（`_corner_buffer_S`·其受詞為抵費地之範圍、非應分配面積）、範圍之擴大（`K980_AREA_TOL`·`W-G.9-391`）、代數之退路（`iterate_G_S`·唯幾何求解失敗時·其精度另議·他案之形 `59`）、依已定之 `G` 擬合幾何形之二分（`verify/wf_f1.py` 之 `_bisect_area`）、反求 `a″` 之二分（`verify/wf_f4.py` 之 `_bisect_G`·其 `G` 仍經 `_solve_G_one`）。🔶 代數之退路之⛔ 及，為「每一宗」之受詞之縮，於呈 KL 核本單之配地時標明。
- **丙 評選之式**：街角第 1 宗 ＝ `_corner_first_lot_G`（假設第 1 宗之真 G·其右側之上界 ＝ `_oblique_s_max`）；末端塊 ＝ `end_block_trial_G`（新·`end_block_host` 之評選之試算之單一真相源·舊之巢狀 `_trial` 委派之）。
- **丁 取得之宗之自我檢查**（甲之「自我檢查」）：配地之末趟（`_advance_block_with_split` 之 `_commit`）中，鏈首之街角第 1 宗、鏈首之末端塊之當選者，於其實配之 `G` 定後，以評選之式依該宗於實配之輸入（應分配面積之 `a`、`A`、負擔之尺度、街廓之幾何·與評選處之輸入之差至多為浮點之末位〔如正面之單位向量之算法之別·`1` ulp〕）重算之，二者取至 2 位不同 ⇒ 停機（`GB-206`·經 `k6_program_stop` 立之·試算之內亦上拋·⛔ 靜默取其一）。「評選之所算」之讀：評選之式為決定性，同一之輸入重算之值即評選時之值；評選之後有同一地主之併入者，其 `a` 已變（KL「同一地主之併入除外」之受詞 ＝ 值之變），二式皆以新之 `a` 算之而仍須同值。
- **戊 門檻邊緣之取得**：評選之式亦經 `_solve_G_one` ⇒ 以精算之值判之（請示檔之「他案」之例）。
- **己 本案之量之源**：請示表之甲之欄之數出自發單端之暫存之原型（容差 `1e-4`）；本單之容差 `1e-6` 之原型之實跑（二退縮）與之逐位同（`W-G.9-392` 規格單 `§一` 項 `5`）。

### 三、本案之量（二退縮·`k6s3` 之落檔之逐欄之全比·發單端之原型）

| 項 | 3.5 m（改前 → 改後） | 0 m（改前 → 改後） |
|---|---|---|
| `628-18(1)`（`R6` 右·街角第 1 宗） | `307.78` → `307.78`（評選 `307.79` → `307.78`） | 同左 |
| `628-18(2)`（`R5` 左） | `268.33` → `268.34` | `259.13` → `259.13` |
| 抵費地 `R1-抵費地-1` | `851.68` → `851.69` | `851.67` → `851.69` |
| 抵費地 `R3-抵費地` | `1651.41` → `1651.40` | `1651.41` → `1651.40` |
| 抵費地 `R4-抵費地` | `697.40` → `697.39` | `697.40` → `697.39` |
| 抵費地 `R5-抵費地` | `1221.44` → `1221.45` | `1221.47` → `1221.46` |
| 抵費地 `R6-抵費地` | `980.59` → `980.58` | `980.59` → `980.58` |

他之宗之地號、地主、應分配面積、宗序、推進之側、街角之得標、強制抵費地、剔除皆⛔ 變（以上皆終態·段三之入口）；不配地之宗 `628-42(1)`（`R2` 左·剔除·其地照舊入調配池）之試算 `G` `3.81` → `3.82`（二退縮）。段三之前之路徑（`run_corner_pk` ＋ 入池閘·量測器 `probe_WG9375_k965.py` 之受詞）另有 `+0.01 ㎡`：3.5 m `628-22(2)` `520.42` → `520.43`、`628-37(1)` `214.97` → `214.98`、`628-47(1)` `365.82` → `365.83`；0 m `628-47(1)` `365.82` → `365.83`；手冊先行之前之態（`probe_WG9361_k954.py` 之受詞）之 3.5 m 之抵費地 `R3` `1883.03` → `1883.05`、`R5` `1742.99` → `1742.98`——皆非終態（段三、手冊先行於配地恆施之），⛔ 入請示表。每宗之求解之次數（`迭代次數`）皆增（如 `15` → `27`）。取得之宗之自我檢查於本案二退縮皆過（3.5 m `17`、0 m `18` 組相異之〔宗、值〕·皆同值）。⇒ **本案配地改變（`±0.01 ㎡`）**：新規格單 ⇒ 側支保留、⛔ 入主線，待 KL 核（README 第二節停止條件 `2`）。

### 四、他案之形（泛用化·上節之六之續）

| # | 形 | 處置 |
|---|---|---|
| `57` | 不動點落於半分（`…5`）之 `±1e-6` 之內 | 二次所算取至 2 位可異 ⇒ 自我檢查停機（`GB-206`）；⛔ 靜默取其一 |
| `58` | 評選之後同一地主之併入（段三之後處理、手冊先行等） | 二式皆以併入後之 `a` 算之、須同值（本案如 `R4` 左 `628(1)` `1521.05` → `1788.69`·二退縮之自我檢查皆過） |
| `59` | 幾何求解失敗而走代數之退路（`iterate_G_S`） | 取得之宗於實配走之者既有之停機（`w0_start`／`s_back` 之守）；他宗之精度⛔ 及（`tol 0.005`·他單） |
| `60` | 換名、鏡射、旋轉、實座標之尺度 | `G` 同（`F36 selftest` 之 `G1`、`G2`） |
| `61` | 右鏈首宗之上界隨左鏈之變而變 | 精算後 `G` ⛔ 隨之變（`G1`／`G2` 之二上界） |
| `62` | 該側為強制抵費地（無取得之宗） | 該側⛔ 查 |
| `63` | 自我檢查於試算之內（段三、入池閘、合併再試）觸之 | 上拋（`W-G.9-389` 之機制·⛔ 判為「不過」） |
| `64` | 門檻邊緣（精算之值 ＜ 範圍之面積 ≤ 舊之評選之值） | 以精算之值判之 ⇒ 未達（由次一候選續試；皆未達 ⇒ 強制抵費地） |
| `65` | 右鏈之首宗之面積 ＜ `0.5 ㎡` 而起點挪移重解（`_adj`） | 評選之式無此挪移 ⇒ 自我檢查停機（`GB-206`·其訊息之歸因為二式之差·實為挪移）；⛔ 靜默 |
| `66` | 驗證之基線之檔（`verify/baselines/v3`、`verify/baselines/wf`）之 `迭代次數` 與 `G` 之欄 | 隨本節而變 ⇒ 入主線時須重烤（`run_all` 之 `diff_rows`）並記其所據（待落地清單序 `28`） |

### 五、`ops/queue` 之規則檔之登記

本節定稿時之值與上節之五逐位同（`README_自動化運作規則.md` `d775035e…`、`發單端.md` `69a1e952…`、`執行端.md` `ce550ab5…`、`每日摘要.md` `a24cd157…`、`ring.sh` `fef64a34…`、`本機模式.md` `ea16425b…`·皆 `sha256` 之首）——⛔ 變。

### 六、上節之六 `55` 之續（⛔ 裁·僅記）

KL `2026-10-22 05:28`／`05:40`／`05:49`（`ops/queue` 之 `KL答覆/2026-10-22_0528.md`、`_0540.md`）陳末端塊之義（臨 FRONTLINE 及 BASELINE、臨正面之寬合畸零地寬、街廓最左右之第 `1` 宗；⛔ 以未臨正街之三角地為要件；末端塊無退縮）；監看窗交發單端先實量本案無側街而未臨正街 ≈ `0` 之端作末端塊之果再請示確認。發單端之實量（暫存之原型·⛔ 入倉·其數將附於請示·倉內⛔ 錨）：此形之端為 `R3` 左（未臨正街 `0.000122 ㎡`）、`R5` 右（`0`）、`R2` 右（`0.000073 ㎡`）；依 KL 之義作末端塊者，其 `R_end`（＝ 末端帶·末端塊無退縮·本案全區之二組參數〔3.5 m／0 m〕之二跑同值）各 `153.77`、`167.54`、`154.49 ㎡`，其終趟之當選者 `628-34(2)`、`628-23(2)`、`628-34(1)` 皆即該端之現之第 `1` 宗，`k6s3` 之落檔零差（唯 `R2` 之三宗之頂點之移 ≤ `3.3e-6 m`）；與他端之範圍皆⛔ 相接。其請示待本單之配地之核併呈；項 `55` 之前提隨之（⛔ 於本節定之）。

### 七、落地狀態

`K-9-80` ③ 之微差之吸收 🔶（新側支 `verify/W-G.9-392-k980g`·`W-G.9-392` 規格單·**本案配地改變 ⇒ 待 KL 核**·⛔ 入主線）。`K-9-80` ⑦ ⬜（調配模組）。`K-9-61` ⑤ ⬜（`W-G.9-393`）。末端塊之義（KL `05:40`）⬜（請示待呈）。
````

## 附錄丙　塊 `P49`（附於 `docs/待落地清單.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`W-G.9-391` 入主線；`K-9-80` ③ 之微差之吸收之落地（新側支·本案配地改變·待 KL 核）；末端塊之義（KL `2026-10-22 05:40`）之請示之序

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（`W-G.9-391` 與其補令一入主線）之後；本批之碼在新側支 `verify/W-G.9-392-k980g`。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `22` | `K-9-80` ④⑤⑥ 與 `K-9-34`（同上節） | 同上節 | ✅（主線 `56c77fd`） | `K-6` 典 `W-G.9-391` 之節 |
| `25` | `K-9-80` ③（同上節） | 每宗之應分配面積試算至穩定後取至小數 2 位（評選與實配同值）；取得之宗之自我檢查（`GB-206`）——KL `2026-10-22 05:22`「是」（甲） | 🔶（新側支·**本案配地改變 `±0.01 ㎡` ⇒ 待 KL 核**·⛔ 入主線） | `K-6` 典 `W-G.9-392` 之節 |
| `27` | 末端塊之義（KL `2026-10-22 05:40`／`05:49`） | 無側街而未臨正街 ≈ `0` 之端（本案 `R3` 左、`R5` 右、`R2` 右）是否作末端塊；發單端已實量（本案配地零差）——請示待呈（併序 `25` 之核） | ⬜（請示） | `K-6` 典 `W-G.9-392` 之節之六 |
| `19` | `K-9-61` ⑤、`GB-205`（同上節） | 同上節 | ⬜ | 落地之單 `W-G.9-393` |
| `8` | `K-9-60`（同上節） | 同上節 | ⬜ | 落地之單 `W-G.9-394` |
| `9` | `K-9-59`、`K-9-63`（同上節） | 同上節 | ⬜ | 落地之單 `W-G.9-395` |
| `28` | 驗證之基線之重烤（`K-6` 典 `W-G.9-392` 之節之四 `66`） | `verify/baselines/v3`、`verify/baselines/wf` 之 `G` 值計算結果之檔含 `迭代次數` 與 `G` 之欄 ⇒ 本批之後 `run_all` 之 `diff_rows` 必異；入主線時重烤並記 PROVENANCE（KL 令⛔ 跑 `run_all`·其處置併入主線之短單） | ⬜ | `K-6` 典 `W-G.9-392` 之節之四 |
| `26` | `W-G.9-391` 之唯讀審查之記而⛔ 改（同上節） | 同上節；其 `55`（一側之範圍擴大而他端無範圍）之前提隨序 `27` | ⬜（候查） | `K-6` 典 `W-G.9-391` 之節之六、`W-G.9-392` 之節之六 |

🔒 **前節之更新**（上節·⛔ 追改其一字）：其序 `22` ⇒ 本表序 `22`（✅·`W-G.9-391` 入主線）；其序 `25` ⇒ 本表序 `25`（🔶）；其序 `26` 之 `55` 改隨序 `27`；其餘各序（含 `20`、`23`、`24`）之態、出處⛔ 變。本表序 `27`、`28` 為新。
🔒 **本案之量**：本批改配地（`±0.01 ㎡`·`K-6` 典 `W-G.9-392` 之節之三）。
🔒 **依賴序**：序 `25`（KL 核 ⇒ 入主線之短單）與序 `27`（請示）→ 序 `19`（`W-G.9-393`）→ 序 `8`（`W-G.9-394`）→ 序 `9`（`W-G.9-395`）→ 序 `3` → 規格步 `5`〜`8`（含序 `20`、`23`）；序 `24`、`26` 與序 `4`、`6`、`10`〜`15`、`17`、`18` 另單（⛔ 急）。先後之定 ＝ 發單端（KL `2026-10-17 12:40`）。
````

## 附錄丁　塊 `G16`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末·工項三）

````markdown

## 🔧 `GB-206` 之立（`W-G.9-392`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 新側支 `verify/W-G.9-392-k980g`（主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81` ⛔ 動）。**取號**（`W-G.9-392 §零-1`）：`GB-206` 於 `56c77fd` 之追蹤檔之命中 `0` 列（錨定框 `(?<![0-9\-])GB-206(?![0-9])`·列框；裸框 `-F` 亦 `0` 列）；本簿 `MAX` ＝ `205`（`W-G.9-392 §零-0` 項 `3`）⇒ 取之。

### `GB-206` 🆕　**取得之宗（街角第 1 宗、末端塊之當選者）之評選之式之所算與實配之所算取至小數 2 位不同 ⇒ 停機**

**受詞**：`app.py`（新側支·`W-G.9-392` 工項二）之頂層 `k980_acq_check`——配地之末趟（`_commit`）中鏈首之取得之宗，以評選之式（`_corner_first_lot_G`／`end_block_trial_G`）依該宗於實配之輸入重算之值與實配之值取至 2 位不同者；其呼叫之處 ＝ 畫面之 `f3_screen_stepg_run` 與 harness 之 `verify/stepg_pipeline.py` 之 `_run_step_g_impl` 之左右二鏈（二宿主各四）。經 `k6_program_stop` 立之（試算之內亦上拋·`W-G.9-389`）。
**情形**：`K-9-80` ③ 之落地（KL `2026-10-22 05:22`「是」·甲：每宗試算至穩定後取至 2 位·評選與實配同值·二次不同即停下示訊）之後，二式之差唯餘：其不動點落於半分之 `±1e-6` 之內（容差 `1e-6` 之下二次所算之末位可異）；或二式之輸入另有不一（程式之錯）。本案二退縮⛔ 觸（`W-G.9-392` 規格單 `§一` 項 `5`）。
**與配地之關係**：觸之 ⇒ 停機（⛔ 靜默取其一·⛔ 自動改容差重算）；配地之法（評選與實配同值）已裁，唯其數值之邊之形未支援。
**失效條件**：求解之止以「取至 2 位之值已定」為判（二分之區間之兩端之應分配面積取至 2 位相同）而證二式必同值，或以量測器證其不可達。
🔒 **排程**：⛔ 急（他案觸之 ⇒ 停機示訊 ⇒ 依其形另單）。
````

## 附錄戊　示範街廓（改前、改後並列·`F36 selftest` 之玩具·非本案）

> 供監看窗與 KL 一眼看出土地之變。玩具街廓 `GA`：矩形，正面寬 `60 m`、深 `15 m`，正街尺度 `6`，`A ＝ 1.2`、`B ＝ 0.3`、`C ＝ 0.25`，無側街；各宗之應分配面積之真值 ＝ 法定式之不動點之解析解（`F36 selftest` 之期值之源）。「評選」以正面之全長 `60 m` 為求解之上界、「實配」以剩餘之長（此處示以 `1.07 × 真寬 ＋ 0.31 m`）為上界——同本案之右側街角第 1 宗之二次之上界不同之形。

| 宗（重劃前面積 `a`） | 真值（不動點） | 改前：評選 | 改前：實配 | 改後：評選 ＝ 實配 |
|---|---|---|---|---|
| 甲（`152.74 ㎡`） | `56.3963…` | `56.39` | `56.40` | `56.40` |
| 乙（`166.44 ㎡`） | `61.4548…` | `61.45` | `61.46` | `61.45` |
| 丙（`206.17 ㎡`） | `76.1243…` | `76.13` | `76.13` | `76.12` |
| 丁（`213.02 ㎡`） | `78.6535…` | `78.66` | `78.65` | `78.65` |

**讀法**：改前，同一宗之評選與實配可差 `0.01 ㎡`（甲、乙、丁），或二者同而與真值之四捨五入差 `0.01 ㎡`（丙）；改後，每宗之二次所算皆 ＝ 真值取至 2 位（`F36 selftest` 之 `G1`：`300` 宗之中 `290` 宗量之·其餘 `10` 宗之真值距半分 ＜ `1e-4 ㎡` 而略之·皆合）。街角之取得以精算之值判之：若某街角規定範圍之面積為 `56.40 ㎡`，宗甲改前之評選 `56.39` ⇒ 未達；改後 `56.40` ⇒ 達（門檻邊緣之取得可異·請示檔之「他案」）。二次所算若仍不同（真值落於半分之 `±1e-6 ㎡` 之內）⇒ 停機示訊（`GB-206`·`F36 selftest` 之 `H2`、`H4`）。

**本案**（`§一` 項 `5`）：地號、地主、街角、末端塊、宗序皆⛔ 變；`R5` `628-18(2)` 增 `0.01 ㎡`（3.5 m）；抵費地 `R1`／`R3`／`R4`／`R5`／`R6` 各 `±0.01`〜`0.02 ㎡`。

SELF_SHA256: 124adb779367ed1b8b213af56e0742a00c5ba1cb6a7d7207b26326e0169c91a1
