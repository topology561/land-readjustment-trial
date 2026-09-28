# `W-G.9-354`　重量單：`K-9-50`（數末端塊之合併再試相互競合）之入典與 harness 路徑（側支）＋ 攢批登記（`自誤 546`／`547`·`GB-194`）＋ 待落地清單之更新

> **發單** ＝ 發單側窗五十·`2026-09-28`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至側支 `verify/W-G.9-353-endmerge`**）。
> **級** ＝ **重**（生產碼 `1` 檔：`app.py`；土地後果：**本案⛔**〔合併再試無標的·配地與 `run_all` 改前改後逐位同·`§一` 項 `6`／`10`／`11`〕；他案有——數末端塊之合併再試相互競合，由停機改依 `K-9-50` 處之；段三與合併再試之後處理，合併群於本段無受併宗之街廓，由停機改為其依原位次配得之宗照配並承受·`§一` 項 `7`／`8`）。
> **開工態** ＝ 側支 `verify/W-G.9-353-endmerge` ＝ `928d2920702bc128cc973ddfb3b234d83a4b05bc`（`W-G.9-353` 之端）；主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`。🔒 **本批之五筆 `commit` 一律推至同一側支（皆為快轉·承 `928d292`）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D2`／`F12d`／`F13`／`K3`／`E4`／`G4`／`P8` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）。
> 🔑 **來源檔一**（檔名逐字 `W-G.9-354_重量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。本批之新檔（`F13`）與改動（`D2`、`F12d`、`K3`、`E4`、`G4`、`P8`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：主線 `wip/s1-endpart` 之任何推進；塊 `D2` 以外之生產碼一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿之一字；`K-6` 典、自誤簿、`GB` 簿與 `CLAUDE.md` 除塊 `K3`／`E4`／`G4`／`P8` 之純末端追加外之一字；`verify/probes/probe_WG9353_endmerge.py` 除塊 `F12d` 外之一字；任何既有側支之刪除或改寫（本批唯快轉 `verify/W-G.9-353-endmerge`）；KL 主 checkout（本批⛔ 同步·主線未動）。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；`git rev-parse origin/verify/W-G.9-353-endmerge` ＝ `928d2920702bc128cc973ddfb3b234d83a4b05bc`；`git ls-remote --heads origin` 之列數 ＝ `31`；施工樹 `git checkout --detach origin/verify/W-G.9-353-endmerge` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 545 545` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`909`** 檔·器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十實跑（皆 `rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-354`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py 928d292 W-G.9-354 W-G.9-353 W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-353` | `2`／`6`／`5` | `2`／`6`／`5` | `11` | `3` | `3`／`68` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `8`／`11` | 🟢 宣告框 `0` |
| `K-9-50`（本批所鑄之裁號）｜`python verify/probes/wg9268_gate6_occupancy.py 928d292 K-9-50 K-9-49 K-9-94` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`1` | 🟢 可取（鬆框 `1` 列 ＝ `docs/orders/W-G.9-333_重量單.md:34` 之「對照乙［必為零］」所列之未取號·⛔ 占用） |
| 對照甲［必非零］`K-9-49` | `0`／`14`／`0` | `0`／`14`／`2` | `14`（寬式 `16`） | `5` | `8`／`69` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`K-9-94` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`2` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `13`／`13` | 🟢 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態之追蹤檔·錨定框 `(?<![0-9\-])<號>(?![0-9])`·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取）：

| 號 | 裸（錨定）列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 546`／`547`（逐號） | 皆 `0` | 皆 `0` | 皆 `0` | 🟢 可取 |
| 對照甲［必非零］`自誤 545` | `4` | `0` | `4` | 🟢 C 形非空（B 形於本倉為量測器紅·`GB-158`） |
| `GB-194` | `0` | — | — | 🟢 可取 |
| 對照甲［必非零］`GB-193` | `13` | — | — | 🟢 框非恆空 |

自誤 `MAX` ＝ `545`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 546`／`547`；`GB` `MAX` ＝ `193` ⇒ 取 `GB-194`；`K-9` `MAX` ＝ `49` ⇒ 取 `K-9-50`；⛔ 鑄 `VR`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `0b05925`，或側支 `verify/W-G.9-353-endmerge` ≠ `928d292`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `31` |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D2`／`F12d`／`F13`／`K3`／`E4`／`G4`／`P8` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項一之 `git apply --check`（塊 `F12d`）不過，或施後 `verify/probes/probe_WG9353_endmerge.py` 之 blob ≠ `§五-1` 項 `9`；或工項二前置之任一期不符 |
| `5` | 塊 `D2` 之 `git apply --check` 不過；或施後 `app.py` 之 blob ≠ `§五-1` 項 `9` |
| `6` | 工項二之驗 `V-1`〜`V-5` 任一 ≠ 期（尤：`V-2` 之 `F8 run` 二份改前改後有**任一**異列；`V-5` 之 `run_all` 相異項 ≠ `0`） |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-353-endmerge`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之四檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `11`。

---

## `§一`　態錨（發單側窗五十自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `verify/W-G.9-353-endmerge` ＝ `928d2920702bc128cc973ddfb3b234d83a4b05bc`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`31`** |
| `2` | 生產碼（開工態 blob） | `app.py` `0c7739fde995fc77b75d2deccc3a7b78f575c91b`（`1566816` B）；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966` |
| `3` | `W-G.9-353` 之復驗 | 發單側窗五十依交接文四十九 `§四-1` 逐項自倉重跑：側支五 `commit`（`655c6e3`／`576708c`／`c970ae6`／`83d3420`／`928d292`）逐筆對拍（單 ＝ `33b69bd8…`·`SELF_SHA256` 自驗相符；`F12`／`D1`／`K2`／`P7` 與單內塊逐位同；`D1` 施於 `576708c` 得 `0c7739fd…`／`ca56b5c4…`／`8bb45920…` ＝ `c970ae6` 之三檔）；二檔之嚴格前綴（`K-6` `410740 → 412870`、`CLAUDE.md` `282537 → 286590`）；收工閘 `1`〜`16` 自跑皆符（閘 `7` 四簿同開工態；`wfns_ast` `48`／`48`／`47`）；`V-2`（`F8 run` 二退縮改前改後 `diff` 皆空）；`V-4`（`parity` 二退縮 `rc 0`；`F10 run`／`F11 run` 改前改後逐位同）；`V-5`（`run_all` 二態於同一倉外路徑自跑·`236032` B·`cmp` 逐位同）；`F12 run` 之數 ＝ 該單 `§一` 項 `6`／`7`——**全數相符**；主線仍 `0b05925…`、heads `31`。CC 回報之諸差異（`run_all` 於 Windows `238127` B；取號器第三引數之列·見 `自誤 546`；`V-4` 之比較端未列於前置·見 `自誤 547`；報告內嵌 log 之行尾）皆核實、無影響 |
| `4` | 本批之受詞 | `K-9-50`（KL 裁 `2026-09-28 00:30`·逐字見交接文四十九附錄甲·本批以塊 `K3` 入 `K-6` 典）；`K-9-48` 其二與讀法 `1` ⑤（後處理之承前）；`K-9-49 ②③`、`K-9-36 ③`（`W-G.9-353` 已落之合併再試與強制抵費地）；`K-9-24 二`、`K-9-27`（題二所比照）；依賴序 ＝ `CLAUDE.md`「🔧 待落地清單之更新：末端塊之合併再試與強制抵費地…（`W-G.9-353`）」節序 `3` |
| `5` | 現碼之行為（開工態） | ① 數末端塊之競合（同一合併群之未達候選分屬二末端塊）⇒ `end_block_merge_run` 停機（逐字「數末端塊之競合（⛔ 裁·K-9-49 射程 ③）」）；② 段三（及合併再試）之後處理，合併群之保留宗所在之街廓無本段之受併宗 ⇒ 停機（逐字「之保留宗而無本段之受併宗」·停機款 `9`）；③ 後處理 (b) 之道路片經中心線切分須恰得 `2` 片，否則停機（逐字「（期 2）」） |
| `6` | 本案（塊 `D2` 施後·harness·`python verify/probes/probe_WG9354_endcontest.py run <repo>`；`python verify/probes/probe_WG9353_endmerge.py run <repo>`） | 二退縮之合併再試紀錄皆 ＝ `{'退縮': <退縮>, '標的': [], '皆未達': {}}`（⛔ 載競合）、逐列 `0`；`R6` 左端仍由 `628-4(1)` 當選 ⇒ **本案不觸發** |
| `7` | 合成案（`F13 run`·退縮 `3.5`·注入於器內之 `ns`·⛔ 改檔；`R3` 左端與 `R5` 右端〔隔 `RD2` 相對〕以所給之寬構末端帶·⛔ 未臨正街） | `C`（競合之列與交面積）、`F`（`R3` 左端之強制抵費地）、`X`（逐列、後處理與鏈首宗 `G`）之甲乙丙皆 ✅——甲 ＝ 寬 `8`／`16`：競合（題一）＝ 地主 `G009` 之 `628(4)`（`R3` 左·交 `66.49`）與 `628(3)`（`R5` 右·交 `237.57`）；二端皆無本街廓內之相鄰土地；切半與整片皆二端未成（整片：`628(4)` `258.96` ＜ `351.70`、`628(3)` `363.44` ＜ `761.15`）⇒ 二端皆不併入；`R5` 右端由其他跨占者續試，`628-23(2)` 以 ① 併 `628-21(2)`、`628-22(2)` 而成，其道路片 `628-23(3)`、`628-22(3)` 全在中心線之一側 ⇒ 不切、全歸之（鏈首宗 `G` `1422.89`）；`R3` 左端 ⇒ 強制抵費地 `351.70 ㎡`。　乙 ＝ 寬 `8`／`5.5`（`628-23(2)` 假設跨占街角規定範圍、`G009` 他街廓之片上鎖）：同一競合（交 `66.49`／`217.29`）；切半二端未成；整片只 `R5` 成（`628(3)` `363.44` ≥ `263.02`·驗「不影響原位次」通過；`628(4)` `258.96` ＜ `351.70`）⇒ 道路土地歸 `628(3)`；`628(4)` 不能依原位次配地 ⇒ 併入 `628(3)`（後處理 (a)·鏈首宗 `G` `408.48`）；`R3` 左端 ⇒ 強制抵費地 `351.70 ㎡`。　丙 ＝ 寬 `8`／`5.0`（同乙）：交 `66.49`／`207.25`；切半只 `R5` 成（`628(3)` 併其半 `170.7953` ⇒ `256.03` ≥ `239.17`·驗通過；`628(4)` 併其半 `170.9947` ⇒ `151.98` ＜ `351.70`；`R5` 側之面積比 `0.4997`）⇒ `628(3)` 定案；`628(4)` 連同其半不能依原位次配地 ⇒ 併入 `628(3)`（題一 `4`·鏈首宗 `G` `408.48`）；`R3` 左端 ⇒ 強制抵費地 `351.70 ㎡`。　三案之 `R5` 宗地聯集 △ 街廓皆 `0.0000`、兩兩疊皆 `0.0000`；`R3` 之聯集 △ 街廓皆 `0.0001`、兩兩疊皆 `0.0000`；諸數皆與器內另寫之外部錨相符。 |
| `8` | 合成案（`F12 run`·同 `W-G.9-353 §一` 項 `7` 之四案） | 甲之停機點：開工態 ＝ 後處理之「之保留宗而無本段之受併宗」（其合併群之 `R1` 片依原位次配得而本段無受併宗）；塊 `D2` 施後 ＝ 其 `R1` 片照配，餘片 `628(3)` 不鄰任一配得之街廓 ⇒ 後處理 (a) 停機（逐字「`628(3)` 所鄰之 B 內街廓 ＝ []（期恰 1）（停機款 9）」·`K-9-48` 七項 `3`／`5`／`6` 之承前缺口）；乙丙丁之數與 `W-G.9-353 §一` 項 `7` 同（`437.18`／`252.28`／`779.93`） |
| `9` | 施後 blob | `app.py` `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`（`1589495` B·增 `431`／刪 `40`）；`verify/probes/probe_WG9353_endmerge.py` `c12d3f85f394662630e7edd8abc7ca90f98af086`（`42258` B·增 `10`／刪 `7`） |
| `10` | `F8 run`（`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5`／`… 0.0`·工項一之端 對 工項二之 `commit`） | 皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；二退縮之改前改後 `diff` **皆空**（逐位同）——發單側 Linux 實測（模擬之工項一之端 對 工項二） |
| `11` | `run_all`（同一倉外路徑·工項一之端 對 工項二之 `commit`） | 二份皆 `64` 項·PASS `28 → 28`／FAIL `36 → 36`；`python verify/probes/probe_WG9343_step0_flag.py runall` ⇒ `rc 0`，**相異項 `0`**（`64` 項之名目、狀態、違規數與本體逐項同）；末端夾具／golden 列 `21／21`·相異 `0`；對帳段「名目：凍存 `22`／現況 `36`」不變；二份 `cmp` 逐位同（各 `236050` B）——發單側 Linux 實測（同一倉外路徑·其 bytes 平台與路徑相依·⛔ 入判） |
| `12` | 畫面對 harness（`python verify/probes/probe_WG9345_screen.py parity <R> <退縮> on <json>`） | 施後：`3.5` ⇒ `rc 0`（配地列 harness `35`／畫面 `34`·不符格 `0`）；`0.0` ⇒ `rc 0`（`36`／`35`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（皆同開工態） |

---

## `§二`　KL 之語與射程

🔒 **所據之裁**：`K-9-50`——KL `2026-09-28 00:04` 逐字「兩個以上末端塊同時想併到同一位地主的土地時，附圖及說明給我裁示」；發單側窗四十九呈題一、題二（附圖二張）；KL `00:30` 逐字「題1、題2：都是」（其題與答逐字入塊 `K3`·取自交接文四十九〔修訂〕附錄甲·⛔ 憑記憶重寫）。另據 `K-9-48`（其二·讀法 `1` ⑤）、`K-9-49 ②③`、`K-9-36 ③`、`K-9-24 二`、`K-9-27`。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至側支⛔ 須放行；**主線之推進**（`W-G.9-353`〜`355` 同批）**另單·候 KL 逐字放行**。
🔒 **本單之讀法**（發單側之工程裁·⛔ 域裁·以【通知】呈 KL；其 ①〜⑧ 之定稿逐字見塊 `K3` 之「發單側之讀法」`1`〜`8`）：
① **競合之判定**：合併群（`K-6 §一`·`k6_merge_groups`·同地主 ∧ 地籍相連·⛔ 濾街廓）之未達候選分屬二末端塊 ⇒ 競合；二末端塊同街廓（左右端）⇒ 題二，分屬二街廓 ⇒ 題一。
② **時點**：競合之二端各以該合併群於該端之首個未達候選為其列；先至之列候其夥伴之列而二列並解（其間該端之後續列亦候之）；夥伴之端先由他人定案 ⇒ 競合消滅，依逐列辦理；未取得之一端之同群候選⛔ 再試。
③ **達標**：試算之當選者為該候選；經道路或公設地上之土地併入者並須通過「不影響原位次」之檢核（`K-9-48` 七項 `2`）。
④ **交之面積**：該地主之跨占候選各與該端 `R_end` 之交之和（評選紀錄之 `跨占R_end(㎡)`）；比較至小數二位。
⑤ **切半**：道路片依所屬道路之中心線切分（與後處理 (b) 同一函式 `_road_halves`）；片全在中心線之一側者不切、全歸該側；路口之道路片與公設地上之土地按面積平分；二端所需之道路、公設地上之土地互不相涉者，各以其整片試。
⑥ **題一 `4`**：未取得之一端之候選連其半試算配地，候選配得且該街廓之原位次不受影響 ⇒ 其半併之；否則候選連其半併入已取得之一端之受併宗，須通過「不影響原位次」之檢核（二街廓並驗），不過 ⇒ 停機（`K-9-48` 七項 `3`〜`5` 未落地）。
⑦ **後處理之承前**（`K-9-48` 其二·讀法 `1` ⑤）：合併群於本段無受併宗之街廓，其依原位次配得之宗照配，並承受分往該街廓之土地；該街廓配得之宗不唯一者 ⇒ 題一未取得之一端取其候選，其餘 ⇒ 停機（承受之宗未定）；本讀法亦及於段三之後處理。
⑧ **題二之層次**：二端分別先以同街廓內之相連土地試算（`K-9-49 ②` 之序），二端皆拿不下再及道路、公設地上之相連土地；某一層有一端以上拿得下即依該層定之。
⑨ **仍停機者**（`K-9-50` 之【通知】與射程 ③·`GB-194`）：一筆土地同時跨占同一街廓二末端塊之 `R_end`；同一末端塊屬二以上之競合；三個以上末端塊之競合。
⑩ **畫面路徑**：本批⛔ 及（`W-G.9-355`·同側支）。

🔒 **逐筆清單**：本批動生產碼者恰 **`1`** 筆（工項二·推側支）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `app.py`（`end_block_merge_run`：競合之判定與交付、三停機款；`k6b_stage3_run`：`contests` 參數、競合之處置〔題一 `_ct_cross`／題二 `_ct_same_block`〕與逐列之排程 `_k950_rows`、道路片之切分 `_road_halves`〔後處理 (b) 與題一共用·片全在一側者不切〕、後處理之承前〔`_stay`／`_recv_of`〕） | 塊 `D2` | 本案⛔（`§一` 項 `6`／`10`／`11`）；他案有（`§一` 項 `7`／`8`） |

🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至側支 `verify/W-G.9-353-endmerge`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及其他任何生產碼、任何他錨；`(d)` ⛔ 建畫面路徑之合併再試、`K-9-48` 七項 `3`／`5`／`6`、`GB-194` 之三停機款之處置、強制抵費地作調配池（`K-9-38`〜`40`）、調配之任何後步——另單。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（側支·零生產碼）

`docs/orders/W-G.9-354_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-354 工項零：本單原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`（快轉）；推後 `git ls-remote --heads origin` 之列數 ＝ `31`、主線仍 ＝ `0b05925…`。

### 工項一　量測器 `F13` 入倉 ＋ `F12` 之更新（側支·零生產碼）

塊 `F13` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9354_endcontest.py`（**新檔**）。塊 `F12d` 依圍欄之逐列索引抽出為 `<O>\F12d.diff`、對拍 `§五-1` 後，`git apply --check <O>\F12d.diff` ⇒ 過；`git apply <O>\F12d.diff`；`git hash-object verify/probes/probe_WG9353_endmerge.py` ＝ `§五-1` 項 `9` 之值（停機款 `4`）。`commit` 訊息逐字 `W-G.9-354 工項一：量測器 F13（數末端塊之競合·K-9-50）入倉 ＋ F12 之更新（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

### 工項二　塊 `D2`：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑 ＋ 後處理之承前（🔴 生產碼·一 `commit`·推側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9354_endcontest.py selftest <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
2. `python verify/probes/probe_WG9354_endcontest.py wiring <repo>` ⇒ **`rc 1`**（`W1`／`W2`／`W4`／`W5` 紅、`W3`／`W6` 綠；突變 `N1`〜`N4` 皆「突變錨不存在」；末列 `⇒ 紅 ['W1', 'W2', 'W4', 'W5', 'N1', 'N2', 'N3', 'N4']；rc 1`）。
3. `python verify/probes/probe_WG9354_endcontest.py run <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
4. `python verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>` ⇒ 皆 **`rc 0`**；`python verify/probes/probe_WG9353_endmerge.py run <repo> > <O>\f12_run_pre.log` ⇒ **`rc 1`**（`X1` 紅·其停機之文 ＝ `§一` 項 `8` 之開工態；末列 `⇒ 紅 ['X1@甲']；rc 1`）。
5. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
6. `python verify/probes/probe_WG9351_intake.py run <repo> > <O>\f10_run_pre.log`；`python verify/probes/probe_WG9352_endblock.py run <repo> > <O>\f11_run_pre.log`（皆 `rc 0`·`自誤 547` 之攔法）。
7. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D2` 依圍欄之逐列索引抽出為 `<O>\D2.diff`、對拍 `§五-1` 後，`git apply --check <O>\D2.diff` ⇒ 過；`git apply <O>\D2.diff`；`git hash-object app.py` ＝ `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-354 工項二：數末端塊之合併再試相互競合（K-9-50）之 harness 路徑 ＋ 後處理之承前 🔴 生產碼（側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9354_endcontest.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`F13 selftest` 之 `TA`〜`TS`、`H1`〜`H3`、`P1`〜`P3`、`S1` 皆 ✅，`M1`〜`M14` 皆「轉紅」、`M0` ✅；`F13 wiring` 之 `W1`〜`W6` 皆 ✅，`N1`〜`N4` 皆「轉紅」；`F12 selftest` 之 `S1`〜`S10i`（⛔ `S10h`）皆 ✅、`M0` ✅、七突變皆「轉紅」 |
| `V-2` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `5` 之一份 `diff` | 皆 **`rc 0`**、末列 `⇒ 紅 []；rc 0`；**二份之 `diff` 皆空**（`§一` 項 `10`） |
| `V-3` | `python verify/probes/probe_WG9354_endcontest.py run <repo>`；`python verify/probes/probe_WG9353_endmerge.py run <repo> > <O>\f12_run_post.log` | 皆 **`rc 0`**；末列 `⇒ 紅 []；rc 0`；`F13` 之 `R1` 二退縮、`C`／`F`／`X` 之甲乙丙皆 ✅，其數 ＝ `§一` 項 `6`／`7`；`F12` 之 `R1` 二退縮、`X1`〜`X4` 皆 ✅，其數 ＝ `§一` 項 `6`／`8`；`<O>\f12_run_pre.log` 與 `<O>\f12_run_post.log` 之異列唯 `X1` 一列與末列 |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35.json`；同 `0.0`；`python verify/probes/probe_WG9348_harvest_key.py <repo>`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>`；`python verify/probes/probe_WG9340_main_synth.py <repo>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9350_frontroad.py selftest <repo>`；`… wiring <repo>`；`… run <repo>`；`python verify/probes/probe_WG9351_intake.py selftest <repo>`；`… wiring <repo>`；`… run <repo> > <O>\f10_run_post.log`；`python verify/probes/probe_WG9352_endblock.py selftest <repo>`；`… wiring <repo>`；`… run <repo> > <O>\f11_run_post.log` | 皆 **`rc 0`**；`parity` ＝ `§一` 項 `12`；`wfns_ast` **`48`／`48`／`47`**（同開工態）；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`<O>\f10_run_post.log`、`<O>\f11_run_post.log` 各與前置 `6` 之一份逐字同 |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**（`64` 項之名目、狀態、違規數與本體逐項同）；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（驗皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-353-endmerge`。

### 工項三　攢批登記 ＋ `K-9-50` 之入典 ＋ 待落地清單之更新（側支·零生產碼·一 `commit`）

塊 `K3`／`E4`／`G4`／`P8` 各依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位**附於**：
- `K3` ⇒ `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；
- `E4` ⇒ `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；
- `G4` ⇒ `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；
- `P8` ⇒ `CLAUDE.md` 之末。

四檔之刪除欄皆 `0`、改前全檔皆為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-354 工項三：K-9-50 之入典 ＋ 攢批登記（自誤 546／547·GB-194）＋ 待落地清單之更新（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

### 工項四　執行報告入倉（側支·新檔 `docs/reports/W-G.9-354R_數末端塊之合併再試相互競合_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`11` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F13` 三子命令與 `F12` 三子命令之全文、`F8 run` 二份之 `diff` 之結果、`F10 run`／`F11 run` 改前改後之 `diff` 之結果、`parity` 二份之 `rc` 與末三列、`runall` 對拍之全文與 `diff` 之結果）；④ 七塊之實得（bytes／`sha256`）與四檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`（主線仍 `0b05925…`）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-354 工項四：執行報告入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

---

## `§四`　收工閘（工項四之 `commit` 推後·於側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項一 ＝ `verify/probes/probe_WG9353_endmerge.py` 增 `10`／刪 `7`；工項二 ＝ `app.py` 增 `431`／刪 `40`；其餘逐檔 **`0`** |
| `2` | 生產碼 `34` 檔對 `928d292` | 相異恰 **`1`**（`app.py` ＝ `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`9` 檔：本單、`F13`、`verify/probes/probe_WG9353_endmerge.py`、`app.py`、`K-6`、自誤簿、`GB` 簿、`CLAUDE.md`、報告） |
| `4` | 四檔之 bytes | `K-6` `412870 → 427954`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `1072508 → 1075505`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1020320 → 1022244`；`CLAUDE.md` `286590 → 291243`；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`31`**；主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`（⛔ 變）；`verify/W-G.9-353-endmerge` ＝ 工項四之 `commit`；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 547 545 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 547 545` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `532`／`MAX` `547`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `47`／`50`／`[44, 47]`（缺號集皆 ＝ 開工態；開工態 ＝ 自誤 `530`／`545`、`GB` `186`／`193`、`K-9` `46`／`49`） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`48`／`48`／`47`**（同開工態） |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9351_intake.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `15` | `python verify/probes/probe_WG9352_endblock.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `16` | `python verify/probes/probe_WG9353_endmerge.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `17` | `python verify/probes/probe_WG9354_endcontest.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之前稿 ＋ 塊 `F13`／`F12d` ＋ 塊 `D2` ＋ 塊 `K3`／`E4`／`G4`／`P8` ＋ 報告之替身·五 `commit`）並實跑閘 `1`〜`4`、`6`〜`17` ⇒ 見 `§五-1` 項 `12`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D2` | `35704` B·`sha256` `6cbd863c748403ec38efcfd3f02716108be7e4aa4c4dee046dd9d124d130208c`·`591` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F12d` | `4768` B·`sha256` `03562d67ea657b51a7e42457e3d4a1c4c57ebb71588566f1b61633db84ff9778`·`56` 列（圍欄內全文·末附換行） |
| `4` | 塊 `F13` | `50537` B·`sha256` `2f47716e38b741fcceb767e8ff6c9d62d06bb5b193a9af6f6b19a9cb51d06ffe`·`848` 列（圍欄內全文·末附換行） |
| `5` | 塊 `K3` | `15084` B·`sha256` `1385e640e22fc918988f67dde35703755338ea75725d310a374c33ac555ffebc`·`118` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`412870` B）之末後，期末 ＝ `427954` B |
| `6` | 塊 `E4` | `2997` B·`sha256` `3f8b180992ada4323ad0600172b877a88f812dcbafe667e15d1407ecafc9f1c0`·`22` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1072508` B）之末後，期末 ＝ `1075505` B |
| `7` | 塊 `G4` | `1924` B·`sha256` `70641e304194f73957ff944b16cdf360534ef939a843e111566a86b55eb87a03`·`15` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1020320` B）之末後，期末 ＝ `1022244` B |
| `8` | 塊 `P8` | `4653` B·`sha256` `165a997974824f725460bd4b924afcd9653954805e5c4df61826eef54495f934`·`26` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`286590` B）之末後，期末 ＝ `291243` B |
| `9` | 施塊後之 blob | `verify/probes/probe_WG9353_endmerge.py` `c12d3f85f394662630e7edd8abc7ca90f98af086`（`42258` B·開工態 `6c3b10931d0c0b5eee7eaa8859eae2fac9b57343`）；`app.py` `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`（`1589495` B·開工態 `0c7739fd…`） |
| `10` | `F13`／`F12` 之二態 | 開工態 ＋ 工項一（工項一之端）：`F13` 三子命令皆 `rc 1`；`F12` 之 `selftest`／`wiring` `rc 0`、`run` `rc 1`（`X1`）；施 `D2` 後皆 `rc 0` |
| `11` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十實跑（態 `928d292`）：🔴 機械 `0` 項／🟡 提示 `9` 項——`P-1` `:127`（工項二前置之段·所觸之字樣係前置 `2` 所引 `F13 wiring` 施前出艙之「突變錨不存在」及「⛔ `commit`」之用語，⛔ 全稱否定 ⇒ **具名豁免**）、`P-1` `:200`（本表·項 `11`／`12` 二格所引之預檢用語與收工閘模擬之述 ⇒ **具名豁免**）、`P-1` `:1272`／`:1367`（塊 `F13` 之碼·所觸之字樣係該器自身之出艙文字 ⇒ **具名豁免**）、`P-4` `:72`／`:142`／`:172`（`§一` 態錨、工項二之驗、`§四` 收工閘之表頭·其箭頭之座標系皆為「改前〔開工態或工項一之端〕至改後〔工項二之 `commit` 或工項四之端〕」，表內自載 ⇒ **具名豁免**）、`P-4` `:321`／`:356`（塊 `D2` 之碼·所觸者係生產碼之註解 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `19197`–`26854`）⇒ `rc 0` |
| `12` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`928d292` ＋ 五 `commit`：本單之前稿〔`§一` 項 `7`／`9`／`11`／`12`、工項二之施之 blob 與 `V-5` 之期、`§四` 閘 `1`／`2`／`7`、本表項 `9`／`11`／`12` 未填〕＋ 塊 `F13`／`F12d`〔`git apply` 過·施後 blob ＝ 項 `9`〕＋ 塊 `D2`〔自前稿依抽取式抽出·`git apply` 過·施後 blob ＝ 項 `9`〕＋ 塊 `K3`／`E4`／`G4`／`P8` ＋ 報告之替身）：閘 `1` 工項一 `verify/probes/probe_WG9353_endmerge.py` 增 `10`／刪 `7`、工項二 `app.py` 增 `431`／刪 `40`，餘逐檔刪 `0`；閘 `2` 相異恰 `1`（`34` 檔）；閘 `3` `CR` 合計 `0`（`9` 檔·判別力 `12308`）；閘 `4` 四檔如 `§四`（皆嚴格前綴）；閘 `6`〜`17` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `48`／`48`／`47`；「app 側宿主 ＝ f3_screen_stepg_run」；`F8` 二子命令、`F9`〜`F13` 各三子命令之末列 `⇒ 紅 []；rc 0`）；另工項二之前置 `1`〜`7` 皆如期（`F13` 三子命令 `rc 1`；`F12` 之 `selftest`／`wiring` `rc 0`、`run` `rc 1`〔`X1`〕）、`V-1`〜`V-5` 皆符（`V-2` 二份 `diff` 皆空；`V-3` 之 `F12 run` 改前改後之異列唯 `X1` 與末列；`V-4` 之 `F10 run`／`F11 run` 改前改後逐位同；`V-5` `runall` 相異 `0`·二份 `cmp` 逐位同）；模擬之 worktree 跑畢追蹤檔之變動 `0`（`run_all` 之拋棄式 worktree 另計） |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 側支 `verify/W-G.9-353-endmerge`（工項二於驗皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D2`（`git apply` 之差異·`app.py`）

````diff
diff --git a/app.py b/app.py
index 0c7739f..dc3e52b 100644
--- a/app.py
+++ b/app.py
@@ -10802,13 +10802,16 @@ def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lot
     流程
       ① 以現宗地試算一次，取「各筆單獨皆未達」之端（標的）；無 ⇒ 逕回（同一物件）；試算中止 ⇒ 逕回並記其由
          （定案之配地將遇同一中止，或於標的之端因無紀錄而停機·⛔ 靜默）。
-      ② 競合（⛔ 裁·`K-9-49` 射程 ③）：二以上標的之候選同屬一合併群 ⇒ 🔴 停機。
+      ② 🆕 `W-G.9-354`（`K-9-50`·KL 裁 `2026-09-28`）：數末端塊之競合——同一合併群之候選分屬二末端塊 ⇒ 競合
+         （二末端塊分屬二街廓 ＝ 題一〔隔道路相對〕；同一街廓之左右端 ＝ 題二），交 `k6b_stage3_run` 依
+         `K-9-50` 處之；分屬三個以上之末端塊、一端屬二以上之競合、同一候選同時跨占二末端塊之 `R_end`
+         ⇒ 🔴 停機（逐案呈核·⛔ 推）。
       ③ 各標的之未達候選依原投影序為列，交 `k6b_stage3_run`（① 同街廓相鄰 → ② 道路及公設地上相鄰·整筆；
          ② 驗「不影響原位次」；後處理同段三）；併入之除外 ＝ `locked` ∪ `corner_lots` ∪ 段三已併出者
          （`K-9-49 ③`：已上鎖、已併入或已分配予街角之土地⛔ 再併入末端塊）。
       ④ 未成之標的 ⇒ 記「皆未達」（定案之配地據以強制抵費地·`K-9-36 ③`）。
     回 `(temp_out, build_out, log, rec)`；`rec` ＝ `{'退縮': setback, '標的': [[街廓, 端]…],
-    '皆未達': {街廓: [端…]}}`（試算中止 ⇒ `'標的'` ＝ `None`、另載 `'試算中止'`）。"""
+    '皆未達': {街廓: [端…]}}`（試算中止 ⇒ `'標的'` ＝ `None`、另載 `'試算中止'`；有競合 ⇒ 另載 `'競合'`）。"""
     _rec = {'退縮': setback, '標的': [], '皆未達': {}}
     try:
         _ev = alloc_eval(temp_parcels, build_parcels) or {}
@@ -10842,13 +10845,32 @@ def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lot
     _dup = {p: tg for p, tg in _cand_of.items() if len(tg) >= 2}
     if _dup:
         raise RuntimeError(f"🔴 [末端塊合併再試] 候選 {sorted(_dup)} 同時跨占二以上末端塊之 R_end——"
-                           "數末端塊之競合（⛔ 裁·K-9-49 射程 ③）")
+                           "一筆土地同時跨占二末端塊（K-9-50 射程 ③·逐案呈核）")
+    _ct, _tgc = [], {}
     for _g in k6_merge_groups(_pk, own_map):
         _ids = sorted(temp_parcels[i]['暫編地號'] for i in _g)
         _hit = sorted({x for p in _ids for x in _cand_of.get(p, ())})
         if len(_hit) >= 2:
-            raise RuntimeError(f"🔴 [末端塊合併再試] 同一合併群 {_ids} 之候選分屬 {len(_hit)} 個末端塊 {_hit}——"
-                               "數末端塊之競合（⛔ 裁·K-9-49 射程 ③）")
+            if len(_hit) >= 3:
+                raise RuntimeError(f"🔴 [末端塊合併再試] 同一合併群 {_ids} 之候選分屬 {len(_hit)} 個末端塊 {_hit}——"
+                                   "三個以上之末端塊（K-9-50 射程 ③·逐案呈核）")
+            _gid = own_map.get(str(temp_parcels[_g[0]].get('原地號', '')))
+            _ent = []
+            for _blk, _sd in _hit:
+                if (_blk, _sd) in _tgc:
+                    raise RuntimeError(
+                        f"🔴 [末端塊合併再試] 末端塊 {(_blk, _sd)} 屬二以上之競合（K-9-50 射程 ③·逐案呈核）")
+                _first = next(r for r in _rows if (r['街廓'], _SIDE[r['端']]) == (_blk, _sd)
+                              and r['暫編地號'] in set(_ids))
+                _area = sum(float(_c.get('跨占R_end(㎡)', 0) or 0) for _c in (_ev[_blk][_sd].get('候選') or [])
+                            if _gid is not None and own_map.get(str(_c.get('原地號', ''))) == _gid)
+                _ent.append((_first['最終序位'], (_blk, _END[_sd], _first['暫編地號'], round(_area, 2))))
+            for _blk, _sd in _hit:
+                _tgc[(_blk, _sd)] = len(_ct)
+            _ent.sort()
+            _ct.append({'形': ('二' if _hit[0][0] == _hit[1][0] else '一'), '列': [e for _, e in _ent]})
+    if _ct:
+        _rec['競合'] = [{'形': c['形'], '列': [list(e) for e in c['列']]} for c in _ct]
     _L = (set(locked or ()) | set(corner_lots or ())
           | {t['暫編地號'] for t in temp_parcels if t.get('段三併出')})
 
@@ -10858,7 +10880,8 @@ def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lot
         return _e.get('當選'), (_row or {}).get('試算G(㎡)'), _e.get('R_end(㎡)')
 
     _temp2, _build2, _log = k6b_stage3_run(_rows, _L, own_map, temp_parcels, build_parcels, blocks,
-                                           centerlines, a_prime, _trial, alloc_state, log_print=log_print)
+                                           centerlines, a_prime, _trial, alloc_state, log_print=log_print,
+                                           contests=(_ct or None))
     _won = {(r['街廓'], r['端']) for r in _log if r.get('結果') == '成' and r.get('序') != '後處理'}
     for _blk, _sd in _tg:
         if (_blk, _END[_sd]) not in _won:
@@ -12965,7 +12988,7 @@ def k6b_stage3_enabled():
 
 
 def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks, centerlines,
-                   a_prime, trial_winner, alloc_state, *, log_print=print):
+                   a_prime, trial_winner, alloc_state, *, log_print=print, contests=None):
     """`K-6 §二 段三`（逐一嘗試）＋ `K-9-48`（街角合併重試·後處理）——`W-G.9-344`。
 
     參數
@@ -12983,6 +13006,10 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
       alloc_state    `alloc_state(temp, build) -> {"kept": {街廓: set}, "bad_pools": {街廓: int}, "err": str|None}`：
                      以所給之宗地重跑街角選位與配地。
       log_print      未處置之 `🔴` 出艙所用之印出函式。
+      contests       🆕 `W-G.9-354`（`K-9-50`）：數末端塊合併再試之競合（唯 `end_block_merge_run` 給之；段三之呼叫恆
+                     `None` ⇒ 逐列依序·逐位同本批前）。`list[dict]`：`{'形': '一'|'二', '列': [(街廓, 端, 候選, 交面積),
+                     (…)]}`——二列 ＝ 同一合併群於二端之首個候選（依原投影序）；`交面積` ＝ 該地主原有土地與該端
+                     `R_end` 之交（㎡）；`形` ＝ `'一'`（隔道路相對·二街廓）／`'二'`（同一街廓兩端）。
     回傳 `(temp_out, build_out, log)`
       `order` 為空 ⇒ `(temp_parcels, build_parcels, [])`（同一物件·逐位同輸入）；
       否則 `temp_out` 為深拷貝，被段三「成」所消耗之片加鍵 `段三併出`（受併宗之相異字典序列表·補令一 裁三）；
@@ -13063,6 +13090,25 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         _nb = _nbr_blocks(_raw[pid], _blk_of[pid])
         return len(_nb) >= 3 and any(_blk_is_pub(b) for b in _nb)
 
+    def _road_halves(x, _stage):
+        # 道路片依中心線切分（後處理 (b) 與 `K-9-50` 題一之切半共用·單一真相源）；🆕 `W-G.9-354`：片全在中心線之
+        #   一側者不切（得 1 片·道路以中心線為界 ⇒ 全歸該側），3 片以上 ⇒ 停機
+        _rb = _blk_of[x]
+        _cl = (centerlines or {}).get(_rb) or []
+        if len(_cl) != 2:
+            raise RuntimeError(
+                f"🔴 [K-6-B 段三 {_stage}] {x} 所屬道路 {_rb} 之中心線頂點數 {len(_cl)}（期 2）（停機款 9）")
+        (x1, y1), (x2, y2) = _cl[0], _cl[-1]
+        _dx, _dy = x2 - x1, y2 - y1
+        _L = (_dx * _dx + _dy * _dy) ** 0.5
+        _ux, _uy = _dx / _L, _dy / _L
+        _line = _Ls([(x1 - _ux * 500, y1 - _uy * 500), (x2 + _ux * 500, y2 + _uy * 500)])
+        _parts = list(_split(_geo[x], _line).geoms)
+        if len(_parts) not in (1, 2):
+            raise RuntimeError(
+                f"🔴 [K-6-B 段三 {_stage}] {x} 經中心線切分得 {len(_parts)} 片（期 1 或 2）（停機款 9）")
+        return _parts
+
     # 合併群（K-6 §一·跨街廓·⛔ 濾分區）
     _pk = [{'原地號': t.get('原地號', ''), 'polygon': _raw[t['暫編地號']]} for t in _temp0]
     _group_of = {}
@@ -13079,6 +13125,8 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
     won = set()
     successes = []          # (群索引, 受併宗, 街廓)
     log = []
+    _closer = {}            # 🆕 `W-G.9-354`：群索引 → 題一只一端成之得失（後處理之地主土地去處）
+    _skip = {}              # 🆕 `W-G.9-354`：(街廓, 端) → 該端⛔ 再試之合併群成員（競合歸他端·`K-9-50`）
 
     def _apply(st, recv, items):
         # items: [(src_pid, qty, whole)]；qty ＝ 已折算之 a′
@@ -13113,16 +13161,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         log.append(_r)
         return _r
 
-    # ── 步驟 1〜8 ──
-    for _r in sorted(order, key=lambda r: r['最終序位']):
-        _blk, _end, c = _r['街廓'], _r['端'], _r['暫編地號']
-        _base = dict(序=_r['最終序位'], 街廓=_blk, 端=_end, 候選=c)
-        if (_blk, _end) in won:
-            _row(**_base, 結果='略·已定案')
-            continue
-        if c in merged_out:
-            _row(**_base, 結果='略·已併出')
-            continue
+    def _sets(c):
         _gi = _group_of.get(c)
         M = (set(_groups[_gi]) if _gi is not None else set()) - {c} - L - merged_out
         S, _stk = set(), [c]
@@ -13140,6 +13179,346 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                 if _adj(_u, _v):
                     U.add(_v)
                     _stk.append(_v)
+        return _gi, S, U
+
+    # ── 🆕 `W-G.9-354`（`K-9-50`）：數末端塊合併再試之競合 ──
+    def _ct_try(e, items, lvl):
+        # 一端之試算（於現態之深拷貝）；① 免驗、② 驗「不影響原位次」（同逐列之判）
+        _t = _clone(state)
+        _apply(_t, e['c'], items)
+        _w, _G, _thr = trial_winner(_t["temp"], _t["build"], e['blk'], e['end'], e['c'])
+        _ok = (_w == e['c'])
+        _chk = '—'
+        if _ok and lvl == '①':
+            _chk = '免'
+        elif _ok:
+            _ok = _noaff(state, _t, {e['blk']}, {x for x, _q, _w2 in items})
+            _chk = '通過' if _ok else '不過'
+        return {'ok': _ok, 'G': _G, 'thr': _thr, 'chk': _chk, 'items': items, 'lvl': lvl}
+
+    def _ct_whole(e, pids):
+        return [(x, _aprime(state, x, e['c']), True) for x in sorted(pids)]
+
+    def _ct_commit(pairs):
+        # pairs: [(e, res)]——自現態之深拷貝依序施之（各端之片互不相交）
+        nonlocal state
+        _t = _clone(state)
+        for e, res in pairs:
+            _apply(_t, e['c'], res['items'])
+        state = _t
+        for e, res in pairs:
+            won.add((e['blk'], e['end']))
+            for x, _q, _w2 in res['items']:
+                marks.setdefault(x, set()).add(e['c'])
+                if _w2:
+                    merged_out.add(x)
+            successes.append((e['gi'], e['c'], e['blk']))
+
+    def _ct_log(e, res, ok, note):
+        _qty = {}
+        for x, q, _w2 in (res or {}).get('items', []):
+            if not _w2:
+                _qty[x] = round(float(q), 4)
+        _row(**e['base'], 層級=(res or {}).get('lvl', '—'), 結果=('成' if ok else '未成'),
+             整筆併入=sorted(x for x, _q, _w2 in (res or {}).get('items', []) if _w2),
+             切分併入=_qty,
+             併入量=({e['c']: round(sum(q for _, q, _w2 in res['items']), 4)} if ok else {}),
+             受併宗=(e['c'] if ok else '—'), 試算G=(res or {}).get('G', '—'), 門檻=(res or {}).get('thr', '—'),
+             檢核=(res or {}).get('chk', '—'), 競合=note)
+
+    def _ct_pick(A, B, form):
+        # 二端皆拿得下：與 R_end 之交之面積大者；並列 ⇒ 題一取跨占者暫編地號（字典序）小者、題二取前緣線 p1 側
+        if round(float(A['area']), 2) != round(float(B['area']), 2):
+            return (A, B) if float(A['area']) > float(B['area']) else (B, A)
+        if form == '二':
+            return (A, B) if A['end'] == '左' else (B, A)
+        return (A, B) if A['c'] < B['c'] else (B, A)
+
+    def _ct_same_block(A, B):
+        # 題二（`K-9-50` 二·比照 `K-9-24 二`、`K-9-27`）：二端分別以地主相連之土地試（先同街廓，再及道路、公設地）；
+        #   土地⛔ 切開；只一端拿得下 ⇒ 歸該端；皆拿得下 ⇒ 交面積大者 → p1 側；皆拿不下 ⇒ 皆⛔ 併
+        _path = []
+        for _lvl in ('①', '②'):
+            _res = {}
+            for e in (A, B):
+                _ms = e['S'] if _lvl == '①' else (e['S'] | e['U'])
+                _need = e['S'] if _lvl == '①' else e['U']
+                _res[e['k']] = _ct_try(e, _ct_whole(e, _ms), _lvl) if _need else None
+            _oks = [e for e in (A, B) if _res[e['k']] is not None and _res[e['k']]['ok']]
+            _path.append(f"{_lvl}：" + "／".join(
+                f"{e['c']} {'—' if _res[e['k']] is None else ('成' if _res[e['k']]['ok'] else '未成')}" for e in (A, B)))
+            if _oks:
+                if len(_oks) == 2:
+                    W, Lo = _ct_pick(A, B, '二')
+                    _why = f"二端皆拿得下 ⇒ {W['c']}（交面積 {W['area']:.2f} ／ {Lo['area']:.2f}）"
+                else:
+                    W, Lo = _oks[0], (B if _oks[0] is A else A)
+                    _why = f"只一端拿得下 ⇒ {W['c']}"
+                _ct_commit([(W, _res[W['k']])])
+                _note = "題二｜" + "；".join(_path) + "｜" + _why
+                _ct_log(W, _res[W['k']], True, _note)
+                _ct_log(Lo, _res[Lo['k']], False, _note)
+                return [Lo]
+        _note = "題二｜" + "；".join(_path) + "｜二端皆拿不下 ⇒ 皆⛔ 併"
+        _ct_log(A, None, False, _note)
+        _ct_log(B, None, False, _note)
+        return [A, B]
+
+    def _ct_cross(A, B):
+        # 題一（`K-9-50` 一·比照 `K-9-48` 其二）：隔道路相對之二末端塊
+        nonlocal state
+        _path = []
+        _r1 = {e['k']: (_ct_try(e, _ct_whole(e, e['S']), '①') if e['S'] else None) for e in (A, B)}
+        _o1 = [e for e in (A, B) if _r1[e['k']] is not None and _r1[e['k']]['ok']]
+        _path.append("①：" + "／".join(
+            f"{e['c']} {'—' if _r1[e['k']] is None else ('成' if _r1[e['k']]['ok'] else '未成')}" for e in (A, B)))
+        if len(_o1) == 2:
+            _ct_commit([(A, _r1[A['k']]), (B, _r1[B['k']])])
+            _note = "題一｜" + "；".join(_path) + "｜二端皆以本街廓內之土地成"
+            _ct_log(A, _r1[A['k']], True, _note)
+            _ct_log(B, _r1[B['k']], True, _note)
+            return []
+        if len(_o1) == 1:
+            W = _o1[0]
+            Lo = B if W is A else A
+            _ct_commit([(W, _r1[W['k']])])
+            # 只一端需要道路／公設地 ⇒ 整片併入該端試（段三 ②）
+            _gi2, _S2, _U2 = _sets(Lo['c'])
+            _rL = _ct_try(Lo, _ct_whole(Lo, _S2 | _U2), '②') if _U2 else None
+            _path.append(f"只一端需要 ⇒ {Lo['c']} 整片 {'—' if _rL is None else ('成' if _rL['ok'] else '未成')}")
+            _note = "題一｜" + "；".join(_path)
+            _ct_log(W, _r1[W['k']], True, _note)
+            if _rL is not None and _rL['ok']:
+                _ct_commit([(Lo, _rL)])
+                _ct_log(Lo, _rL, True, _note)
+                return []
+            _ct_log(Lo, _rL, False, _note)
+            _closer[A['gi']] = {'勝': W, '敗': Lo}
+            return [Lo]
+        X = A['U'] & B['U']
+        if not X:
+            # 二端之道路／公設地互不相涉 ⇒ 各以其整片試
+            _rw = {e['k']: (_ct_try(e, _ct_whole(e, e['S'] | e['U']), '②') if e['U'] else None) for e in (A, B)}
+            _oks = [e for e in (A, B) if _rw[e['k']] is not None and _rw[e['k']]['ok']]
+            _path.append("整片（無共同之道路／公設地）：" + "／".join(
+                f"{e['c']} {'—' if _rw[e['k']] is None else ('成' if _rw[e['k']]['ok'] else '未成')}" for e in (A, B)))
+            _note = "題一｜" + "；".join(_path)
+            if _oks:
+                _ct_commit([(e, _rw[e['k']]) for e in _oks])
+            for e in (A, B):
+                _ct_log(e, _rw[e['k']], e in _oks, _note)
+            if len(_oks) == 1:
+                _closer[A['gi']] = {'勝': _oks[0], '敗': (B if _oks[0] is A else A)}
+            return [e for e in (A, B) if e not in _oks]
+        # 切半：道路片依中心線、公設片（含路口之道路片）按面積平分
+        _frac = {A['k']: {}, B['k']: {}}
+        for x in sorted(X):
+            if _kind(x) == 'road' and not _is_crossing(x):
+                for _q in _road_halves(x, 'K-9-50 題一'):
+                    _nb = set(_nbr_blocks(_q, _blk_of[x]))
+                    _s = [e for e in (A, B) if e['blk'] in _nb]
+                    if len(_s) != 1:
+                        raise RuntimeError(
+                            f"🔴 [K-6-B 段三 K-9-50 題一] {x} 之片（{_q.area:.4f}）所鄰之末端塊街廓 ＝ "
+                            f"{[e['blk'] for e in _s]}（期恰一）（停機款 9）")
+                    _frac[_s[0]['k']][x] = _frac[_s[0]['k']].get(x, 0.0) + float(_q.area) / float(_geo[x].area)
+            else:
+                _frac[A['k']][x] = 0.5
+                _frac[B['k']][x] = 0.5
+        _rh = {}
+        for e in (A, B):
+            _its = _ct_whole(e, e['S'] | (e['U'] - X)) + \
+                [(x, _aprime(state, x, e['c']) * _frac[e['k']][x], False) for x in sorted(X)
+                 if _frac[e['k']].get(x, 0.0) > 0.0]
+            _rh[e['k']] = _ct_try(e, _its, '②半')
+        _oh = [e for e in (A, B) if _rh[e['k']]['ok']]
+        _path.append("切半：" + "／".join(f"{e['c']} {'成' if _rh[e['k']]['ok'] else '未成'}" for e in (A, B)))
+        if len(_oh) == 2:
+            _ct_commit([(A, _rh[A['k']]), (B, _rh[B['k']])])
+            merged_out.update(X)
+            _note = "題一｜" + "；".join(_path) + "｜二端各配一宗"
+            _ct_log(A, _rh[A['k']], True, _note)
+            _ct_log(B, _rh[B['k']], True, _note)
+            return []
+        if len(_oh) == 1:
+            W = _oh[0]
+            Lo = B if W is A else A
+            _ct_commit([(W, _rh[W['k']])])
+            _closer[A['gi']] = {'勝': W, '敗': Lo}
+            # `K-9-50` 題一 4：未得之一端之候選連同分給該端之半——能依原位次配地 ⇒ 其半併之；否則併入已取得之一端
+            _lb = Lo['blk']
+            _its_L = [(x, _aprime(state, x, Lo['c']) * _frac[Lo['k']][x], False) for x in sorted(X)
+                      if _frac[Lo['k']].get(x, 0.0) > 0.0]
+            _t1 = _clone(state)
+            _apply(_t1, Lo['c'], _its_L)
+            _sb = alloc_state(state["temp"], state["build"])
+            _sa = alloc_state(_t1["temp"], _t1["build"])
+            if _sb.get("err") or _sa.get("err"):
+                raise RuntimeError(
+                    f"🔴 [K-6-B 段三 K-9-50 題一] 未得之一端之原位次無從判定（配地中止）：{_sb.get('err')!r}｜"
+                    f"{_sa.get('err')!r}（停機款 9）")
+            _kb0, _kb1 = set(_sb["kept"].get(_lb, set())), set(_sa["kept"].get(_lb, set()))
+            if (Lo['c'] in _kb1 and not (_kb0 - _kb1)
+                    and int(_sa["bad_pools"].get(_lb, 0)) <= int(_sb["bad_pools"].get(_lb, 0))):
+                state = _t1
+                for x in X:
+                    marks.setdefault(x, set()).add(Lo['c'])
+                _to = f"{Lo['c']} 依原位次配地，其半併之"
+                _r4 = dict(整筆併入=[], 切分併入={x: round(float(q), 4) for x, q, _w2 in _its_L},
+                           併入量={Lo['c']: round(sum(q for _, q, _w2 in _its_L), 4)}, 受併宗=Lo['c'], 檢核='通過')
+            else:
+                _its_W = [(x, _aprime(state, x, W['c']) * _frac[Lo['k']][x], False) for x in sorted(X)
+                          if _frac[Lo['k']].get(x, 0.0) > 0.0] + \
+                    [(Lo['c'], _aprime(state, Lo['c'], W['c']), True)]
+                _t2 = _clone(state)
+                _apply(_t2, W['c'], _its_W)
+                if not _noaff(state, _t2, {W['blk'], _lb}, {Lo['c']}):
+                    raise RuntimeError(
+                        f"🔴 [K-6-B 段三 K-9-50 題一] {Lo['c']}（{_lb}）連同其半既不能依原位次配地，併入 {W['c']}"
+                        "（已取得之一端）亦不過「不影響原位次」——`K-9-48` 七項 3〜5 未落地（停機款 9）")
+                state = _t2
+                merged_out.add(Lo['c'])
+                for x in list(X) + [Lo['c']]:
+                    marks.setdefault(x, set()).add(W['c'])
+                _to = f"{Lo['c']} 不能依原位次配地 ⇒ 連同其半併入 {W['c']}"
+                _r4 = dict(整筆併入=[Lo['c']],
+                           切分併入={x: round(float(q), 4) for x, q, _w2 in _its_W if not _w2},
+                           併入量={W['c']: round(sum(q for _, q, _w2 in _its_W), 4)}, 受併宗=W['c'], 檢核='通過')
+            merged_out.update(X)
+            _note = "題一｜" + "；".join(_path) + f"｜只一端成 ⇒ {W['c']}；{_to}"
+            _ct_log(W, _rh[W['k']], True, _note)
+            _ct_log(Lo, _rh[Lo['k']], False, _note)
+            # 未得之一端之地主土地之去處（`K-9-50` 題一 4）——列於後處理之序（⛔ 計入定案之端）
+            _row(序='後處理', 街廓=_lb, 端=Lo['end'], 候選=Lo['c'], 層級='題一 4', 結果='成', **_r4, 競合=_note)
+            return [Lo]
+        # 整片各試
+        _rw = {e['k']: _ct_try(e, _ct_whole(e, e['S'] | e['U']), '②') for e in (A, B)}
+        _ow = [e for e in (A, B) if _rw[e['k']]['ok']]
+        _path.append("整片：" + "／".join(f"{e['c']} {'成' if _rw[e['k']]['ok'] else '未成'}" for e in (A, B)))
+        if not _ow:
+            _note = "題一｜" + "；".join(_path) + "｜二端皆⛔ 併"
+            _ct_log(A, _rw[A['k']], False, _note)
+            _ct_log(B, _rw[B['k']], False, _note)
+            return [A, B]
+        if len(_ow) == 2:
+            W, Lo = _ct_pick(A, B, '一')
+            _why = (f"二端皆成 ⇒ {W['c']}（交面積 {W['area']:.2f} ／ {Lo['area']:.2f}"
+                    + ("·並列 ⇒ 暫編地號小者" if round(float(W['area']), 2) == round(float(Lo['area']), 2) else "") + "）")
+        else:
+            W = _ow[0]
+            Lo = B if W is A else A
+            _why = f"只一端成 ⇒ {W['c']}"
+        _ct_commit([(W, _rw[W['k']])])
+        _closer[A['gi']] = {'勝': W, '敗': Lo}
+        _note = "題一｜" + "；".join(_path) + "｜" + _why
+        _ct_log(W, _rw[W['k']], True, _note)
+        _ct_log(Lo, _rw[Lo['k']], False, _note)
+        return [Lo]
+
+    def _contest(ct, rX, rY):
+        _ends = []
+        for _r in (rX, rY):
+            _k = (_r['街廓'], _r['端'], _r['暫編地號'])
+            _ar = [float(e[3]) for e in ct['列'] if tuple(e[:3]) == _k]
+            if len(_ar) != 1:
+                raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] 列 {_k} 不在其競合之列（停機款 9）")
+            _gi, S, U = _sets(_r['暫編地號'])
+            _ends.append({'k': _k, 'blk': _r['街廓'], 'end': _r['端'], 'c': _r['暫編地號'], 'gi': _gi,
+                          'S': S, 'U': U, 'area': _ar[0],
+                          'base': dict(序=_r['最終序位'], 街廓=_r['街廓'], 端=_r['端'], 候選=_r['暫編地號'])})
+        A, B = _ends
+        if A['gi'] is None or A['gi'] != B['gi']:
+            raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] 競合之二候選 {A['c']}／{B['c']} 非同一合併群（停機款 9）")
+        if ct['形'] == '二':
+            if A['blk'] != B['blk'] or {A['end'], B['end']} != {'左', '右'}:
+                raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] 題二之二端須為同一街廓之左右端：{A['k']}／{B['k']}（停機款 9）")
+            _losers = _ct_same_block(A, B)
+        elif ct['形'] == '一':
+            if A['blk'] == B['blk']:
+                raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] 題一之二端須分屬二街廓：{A['k']}／{B['k']}（停機款 9）")
+            _losers = _ct_cross(A, B)
+        else:
+            raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] 競合之形 {ct.get('形')!r} 未定（停機款 9）")
+        _mem = set(_groups[A['gi']])
+        for e in _losers:
+            _skip.setdefault((e['blk'], e['end']), set()).update(_mem)
+
+    def _k950_rows(rows):
+        # 🆕 `W-G.9-354`（`K-9-50`）：無競合 ⇒ 逐列依序（逐位同本批前）；有競合 ⇒ 競合之列候其夥伴之列，二列並解；
+        #   夥伴之端先由他人定案 ⇒ 競合消滅，依逐列辦；未得之一端之同群候選⛔ 再試（其他跨占者依原投影序續試）
+        if not contests:
+            yield from rows
+            return
+        from collections import deque as _dq
+        _kf = lambda r: (r['街廓'], r['端'], r['暫編地號'])
+        _cmap, _tgc = {}, {}
+        for _ci, _ct in enumerate(contests):
+            if len(_ct.get('列') or []) != 2:
+                raise RuntimeError(
+                    f"🔴 [K-6-B 段三 K-9-50] 競合 {_ci} 之列數 ≠ 2（三個以上之末端塊·K-9-50 射程 ③·停機款 9）")
+            for _e in _ct['列']:
+                if tuple(_e[:3]) in _cmap or (tuple(_e[:2]) in _tgc and _tgc[tuple(_e[:2])] != _ci):
+                    raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] {tuple(_e[:3])} 屬二以上之競合（K-9-50 射程 ③·停機款 9）")
+                _cmap[tuple(_e[:3])] = _ci
+                _tgc[tuple(_e[:2])] = _ci
+        _ks = {_kf(r) for r in rows}
+        _pt = {}
+        for _k, _ci in _cmap.items():
+            if _k not in _ks:
+                raise RuntimeError(f"🔴 [K-6-B 段三 K-9-50] 競合之列 {_k} 不在 order（停機款 9）")
+            _pt[_k] = [tuple(e[:3]) for e in contests[_ci]['列'] if tuple(e[:3]) != _k][0]
+        _cdone, _susp = set(), {}
+        _q = _dq(rows)
+        while _q:
+            _r = _q.popleft()
+            _k = _kf(_r)
+            _tg = _k[:2]
+            _hold = [ci for ci, lst in _susp.items() if _kf(lst[0])[:2] == _tg]
+            if _hold:
+                _susp[_hold[0]].append(_r)
+                continue
+            if _r['暫編地號'] in _skip.get(_tg, ()):
+                _row(序=_r['最終序位'], 街廓=_r['街廓'], 端=_r['端'], 候選=_r['暫編地號'], 結果='略·競合歸他端')
+                continue
+            _ci = _cmap.get(_k)
+            if _ci is not None and _ci not in _cdone and _tg not in won and _r['暫編地號'] not in merged_out:
+                if _pt[_k][:2] in won:
+                    _cdone.add(_ci)
+                elif _ci not in _susp:
+                    _susp[_ci] = [_r]
+                    continue
+                else:
+                    _other = _susp.pop(_ci)
+                    _contest(contests[_ci], _other[0], _r)
+                    _cdone.add(_ci)
+                    for _x in reversed(_other[1:]):
+                        _q.appendleft(_x)
+                    continue
+            _was = _tg in won
+            yield _r
+            if (not _was) and _tg in won:
+                for _ci2 in sorted(_susp):
+                    _lst = _susp[_ci2]
+                    if _pt[_kf(_lst[0])][:2] == _tg:
+                        _cdone.add(_ci2)
+                        del _susp[_ci2]
+                        for _x in reversed(_lst):
+                            _q.appendleft(_x)
+        if _susp:
+            raise RuntimeError(
+                f"🔴 [K-6-B 段三 K-9-50] 競合之列 {[_kf(l[0]) for l in _susp.values()]} 候其夥伴而夥伴未至（停機款 9）")
+
+    # ── 步驟 1〜8 ──
+    for _r in _k950_rows(sorted(order, key=lambda r: r['最終序位'])):
+        _blk, _end, c = _r['街廓'], _r['端'], _r['暫編地號']
+        _base = dict(序=_r['最終序位'], 街廓=_blk, 端=_end, 候選=c)
+        if (_blk, _end) in won:
+            _row(**_base, 結果='略·已定案')
+            continue
+        if c in merged_out:
+            _row(**_base, 結果='略·已併出')
+            continue
+        _gi, S, U = _sets(c)
         _done = False
         _last = None
         for _lvl, _mset in (('①', S), ('②', S | U)):
@@ -13188,6 +13567,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                         f"🔴 [K-6-B 段三 後處理] 群 {sorted(_mem)} 於街廓 {_b2} 有二受併宗"
                         f"（{_recv_by_blk[_b2]}／{_c2}）⇒ 停機款 9")
                 _recv_by_blk[_b2] = _c2
+        _cl0 = _closer.get(_gi)
         R = _mem - merged_out - set(_recv_by_blk.values()) - L
         if not R:
             continue
@@ -13196,11 +13576,30 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             raise RuntimeError(f"🔴 [K-6-B 段三 後處理] 現態配地中止：{_cur['err']!r}（停機款 9）")
         B = sorted({_blk_of[m] for m in _mem
                     if _kind(m) == 'bld' and m in _cur["kept"].get(_blk_of[m], set())})
-        for b in B:
-            if b not in _recv_by_blk:
-                raise RuntimeError(
-                    f"🔴 [K-6-B 段三 後處理] 街廓 {b} 有群 {sorted(_mem)} 之保留宗而無本段之受併宗"
-                    "（停機款 9）")
+        # 🆕 `W-G.9-354`（`K-9-48` 其二·讀法 `1` ⑤·`K-9-50` 題一 4）：該群於本段無受併宗之街廓，其依原位次配得之宗
+        #   照配（⛔ 動）；分往該街廓之土地由其配得之宗承受（`_recv_of`）
+        _stay = {m for m in _mem if _kind(m) == 'bld' and _blk_of[m] in B and _blk_of[m] not in _recv_by_blk
+                 and m in _cur["kept"].get(_blk_of[m], set())}
+        R = R - _stay
+        _orig = {}
+
+        def _recv_of(b):
+            # 受併宗：本段之受併宗；無 ⇒ 題一未得之一端取其候選（現態配得者），他街廓唯恰一宗配得者；餘 ⇒ 停機
+            if b in _recv_by_blk:
+                return _recv_by_blk[b]
+            if b not in _orig:
+                _kb = sorted(m for m in _stay if _blk_of[m] == b)
+                if _cl0 is not None and b == _cl0['敗']['blk'] and _cl0['敗']['c'] in _kb:
+                    _orig[b] = _cl0['敗']['c']
+                elif len(_kb) == 1:
+                    _orig[b] = _kb[0]
+                else:
+                    raise RuntimeError(
+                        f"🔴 [K-6-B 段三 後處理] 街廓 {b} 有群 {sorted(_mem)} 之保留宗 {_kb} 而無本段之受併宗"
+                        "——承受之宗未定（停機款 9）")
+            return _orig[b]
+        if not R:
+            continue
         # 🔧 補令二 裁五 2：B 為空、或某受併宗之街廓 ∉ B ⇒ 停機款 9（⛔ 靜默略過·⛔ 除以 0）
         if not B:
             raise RuntimeError(
@@ -13222,6 +13621,10 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                     raise RuntimeError(
                         f"🔴 [K-6-B 段三 後處理] {x}（{_blk_of[x]}）為 B 內之保留建築片而非受併宗"
                         "——§三-2 未定（停機款 9）")
+                if _cl0 is not None and _blk_of[x] == _cl0['敗']['blk']:
+                    # 🆕 `W-G.9-354`（`K-9-50` 題一 4）：未得之一端之地主土地不能依原位次配地者 ⇒ 併入已取得之一端
+                    _cls['a'].append((x, _cl0['勝']['blk']))
+                    continue
                 _tb = sorted({b for b in B for m in _mem
                               if _blk_of[m] == b and m != x and _adj(x, m)})
                 if len(_tb) != 1:
@@ -13235,23 +13638,11 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             else:
                 raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {x} 之類別無從歸入 (a)(b)(c)（停機款 9）")
         for x, b in sorted(_cls['a'], key=lambda p: _ga(p[0])):
-            _plan.append(('a', x, [(_recv_by_blk[b], _aprime(state, x, _recv_by_blk[b]))], True,
+            _plan.append(('a', x, [(_recv_of(b), _aprime(state, x, _recv_of(b)))], True,
                           _nbr_blocks(_raw[x], _blk_of[x]), None))
         for x in sorted(_cls['b'], key=_ga):
             _rb = _blk_of[x]
-            _cl = (centerlines or {}).get(_rb) or []
-            if len(_cl) != 2:
-                raise RuntimeError(
-                    f"🔴 [K-6-B 段三 後處理 (b)] {x} 所屬道路 {_rb} 之中心線頂點數 {len(_cl)}（期 2）（停機款 9）")
-            (x1, y1), (x2, y2) = _cl[0], _cl[-1]
-            _dx, _dy = x2 - x1, y2 - y1
-            _L = (_dx * _dx + _dy * _dy) ** 0.5
-            _ux, _uy = _dx / _L, _dy / _L
-            _line = _Ls([(x1 - _ux * 500, y1 - _uy * 500), (x2 + _ux * 500, y2 + _uy * 500)])
-            _parts = list(_split(_geo[x], _line).geoms)
-            if len(_parts) != 2:
-                raise RuntimeError(
-                    f"🔴 [K-6-B 段三 後處理 (b)] {x} 經中心線切分得 {len(_parts)} 片（期 2）（停機款 9）")
+            _parts = _road_halves(x, '後處理 (b)')
             _halves = []
             for _q in _parts:
                 _nb = _nbr_blocks(_q, _rb)
@@ -13265,16 +13656,16 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             if not _ones:
                 _plan.append(('b', x, [], False, _nbr_blocks(_raw[x], _rb), _half_log))
             elif len(_ones) == 1:
-                _recv = _recv_by_blk[_ones[0][1][0]]
+                _recv = _recv_of(_ones[0][1][0])
                 _plan.append(('b', x, [(_recv, _aprime(state, x, _recv))], False,
                               _nbr_blocks(_raw[x], _rb), _half_log))
             else:
-                _qs = [(_recv_by_blk[h[1][0]],
-                        _aprime(state, x, _recv_by_blk[h[1][0]]) * (h[0].area / _geo[x].area))
+                _qs = [(_recv_of(h[1][0]),
+                        _aprime(state, x, _recv_of(h[1][0])) * (h[0].area / _geo[x].area))
                        for h in _halves]
                 _plan.append(('b', x, _qs, False, _nbr_blocks(_raw[x], _rb), _half_log))
         for x in sorted(_cls['c'], key=_ga):
-            _recvs = [_recv_by_blk[b] for b in B]
+            _recvs = [_recv_of(b) for b in B]
             _plan.append(('c', x, [(r, _aprime(state, x, r) / len(B)) for r in _recvs], False,
                           _nbr_blocks(_raw[x], _blk_of[x]), None))
 
````

## 附錄乙　塊 `F12d`（`git apply` 之差異·`verify/probes/probe_WG9353_endmerge.py`）

````diff
diff --git a/verify/probes/probe_WG9353_endmerge.py b/verify/probes/probe_WG9353_endmerge.py
index 6c3b109..c12d3f8 100644
--- a/verify/probes/probe_WG9353_endmerge.py
+++ b/verify/probes/probe_WG9353_endmerge.py
@@ -7,8 +7,10 @@
            合成對照（⛔ 讀本案資料·`harvest(app.py)` 取函式）：S1 評選之強制抵費地准否；S2〜S4 一街廓之落位
            （強制 ⇒ ⛔ 落位·紀錄·沿用·不准即停機）；S5 強制帶之 s 長；S6 強制帶之多邊形；S7 定案趟之檢；
            S8 顯示；S9 宿主之准否（試算恆准·定案唯同退縮之合併再試紀錄所載者准）；S10 合併再試（① 同街廓成·
-           ② 道路成且驗「不影響原位次」·該驗不過 ⇒ 未成·皆未達 ⇒ 記之·除外三類·競合停機·試算中止 ⇒ 逕回並記）。
-           另施八突變，每一突變須使至少一例轉紅（判別力）。
+           ② 道路成且驗「不影響原位次」·該驗不過 ⇒ 未成·皆未達 ⇒ 記之·除外三類·試算中止 ⇒ 逕回並記）。
+           另施七突變，每一突變須使至少一例轉紅（判別力）。
+           🔧 `W-G.9-354`：原 S10h（數末端塊之競合 ⇒ 停機）與其突變 M7 撤除——競合自該批起依 `K-9-50` 處之，
+           其對照移量測器 F13（`verify/probes/probe_WG9354_endcontest.py`）。
   wiring   <repo>
            AST／字樣查接線：W1 模組層之常數與函式、⛔ 案件字面；W2 二宿主之強制帶 s 長與池之強制帶；
            W3 宿主之准否；W4 harness 段三與末端塊合併再試之試算皆為 `'trial'`、`run_corner_pk_k6b` 於段三（或其
@@ -20,6 +22,8 @@
            甲 ＝ 假設 `628-4(1)` 跨占街角規定範圍；乙 ＝ 甲 ＋ `628-1(3)` 上鎖；丙 ＝ 乙 ＋ `628-21(1)`、`628-22(1)` 上鎖；
            丁 ＝ `R6` 左端之末端帶以 `13 m` 構之。外部錨 ＝ 本器另寫之幾何與 G 公式（⛔ 呼叫 `end_block_*`／
            `_end_region_R`／`solve_G_binary`）。
+           🔧 `W-G.9-354`：甲之停機點由「他街廓已配地而本段無受併宗」移至後處理 (a)（他街廓依原位次配得者照配·
+           `K-9-48` 其二·讀法 `1` ⑤；餘片不鄰任一配得之街廓·`K-9-48` 七項 3／5／6 之承前缺口）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, io, os, re, sys
@@ -292,8 +296,6 @@ def _cases(ns):
          ("C1(1)", "—", "未成", "—"))
     _run(out, "S10g 除外：段三已併出者⛔ 併入", lambda: m(150.0, a_c1b=60.0, mark="C1(2)")["rows"][0],
          ("C1(1)", "—", "未成", "—"))
-    _run(out, "S10h 競合：同一合併群之候選分屬二末端塊 ⇒ 停機",
-         lambda: m(500.0, both={"left": ["C1(1)"], "right": ["C1(2)"]}), ("例外", "RuntimeError"))
     _run(out, "S10i 試算中止 ⇒ 逕回並記其由",
          lambda: (lambda r: (r["same"], r["rec"]["標的"], "試算中止" in r["rec"]))(m(150.0, fail=True)),
          (True, None, True))
@@ -322,7 +324,6 @@ SELF_MUTS = [
     ("M5 強制⛔ 入池", "end_block_forced_bands", "            _out.append(_i['r_end'])", "            pass"),
     ("M6 段三已併出者⛔ 除外", "end_block_merge_run",
      "          | {t['暫編地號'] for t in temp_parcels if t.get('段三併出')})", "          | set())"),
-    ("M7 ⛔ 查競合", "end_block_merge_run", "        if len(_hit) >= 2:", "        if False:"),
     ("M8 試算中止⛔ 攔", "end_block_merge_run", "    except RuntimeError as _e:\n        _rec['標的'] = None",
      "    except KeyError as _e:\n        _rec['標的'] = None"),
 ]
@@ -668,8 +669,10 @@ def run(repo, sbs):
                 continue
             if scen == "甲":
                 e = P["err"]
-                ok = (e is not None and e[0] == "段三／合併再試" and "後處理" in e[1] and "停機款 9" in e[1])
-                print(("  ✅" if ok else "  🔴") + f" X1 甲：地主 G009 以道路併入成，其合併群之他街廓已配地而本段無受併宗 ⇒ 停機（{e}）")
+                ok = (e is not None and e[0] == "段三／合併再試" and "後處理 (a)" in e[1]
+                      and "所鄰之 B 內街廓 ＝ []" in e[1] and "停機款 9" in e[1])
+                print(("  ✅" if ok else "  🔴") + " X1 甲：地主 G009 以道路併入成，其合併群之他街廓依原位次配得者照配"
+                      f"（`W-G.9-354`·`K-9-48` 其二·讀法 `1` ⑤）；餘片不鄰任一配得之街廓 ⇒ 後處理 (a) 停機（{e}）")
                 if not ok:
                     red.append("X1@甲")
                 continue
````

## 附錄丙　塊 `F13`（新檔 `verify/probes/probe_WG9354_endcontest.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-354 量測器（發單側窗五十擬·檔 F13·⛔ 由受單側改一字）：數末端塊合併再試之競合（`K-9-50`）
＋ 段三後處理之承前（`K-9-48` 其二·讀法 `1` ⑤：無本段受併宗之街廓，其依原位次配得之宗照配並承受分往該街廓之土地；
道路片全在中心線之一側者不切）。

子命令（一律 python verify/probes/probe_WG9354_endcontest.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `end_block_merge_run`〔其內 `k6b_stage3_run` 為真〕）。
           玩具一（題一）：街廓 BX（上）與 BY（下）隔道路 RX 相對，地主甲（g1）之 X1(1)／X2(1)（BX）、X3(1)（RX）、
           Y1(1)／Y2(1)（BY）；道路中心線 y ＝ -4（X3 切為 0.4／0.6）。TA〜TM ＝ 題一之各支（① 二端成／① 一端成而
           他端整片成·不成（其候選配得／不配得）／切半二端成／切半一端成而他端之候選連其半配得／不配得／整片一端成／
           整片二端成而交面積大者／並列而暫編地號小者／皆不成而他人續試／夥伴之端先由他人定案〔逐列〕／夥伴之端於
           擱置中由他人定案〔釋出〕／公設片平分）。玩具二（題二）：一街廓 BZ 左右端，甲 Z1(1)／Z4(1)／Z2(1) 相連、
           道路片 Z3(1)。TN〜TR ＝ 題二之各支（① 只一端／① 二端而交面積大者／並列而 p1 側／② 只一端／皆不成）。
           H1〜H3 ＝ 停機（三個以上之末端塊／一筆土地同時跨占二末端塊／一端屬二競合）。P1〜P3 ＝ 後處理承前（他街廓
           依原位次配得之宗照配／須承受而配得者二筆 ⇒ 停機／唯一 ⇒ 承受公設平分之分）。S1 ＝ 道路片全在中心線之
           一側 ⇒ 不切、全歸該側。另施十四突變，每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST／字樣：W1 `end_block_merge_run` 交競合（`contests=(_ct or None)`）、三以上／一端二競合之停機；
           W2 `k6b_stage3_run` 之 `contests=None`、逐列之環經 `_k950_rows`、無競合 ⇒ 逐列依序（`yield from rows`）；
           W3 段三之二呼叫端（harness `run_corner_pk_k6b`、畫面 `f3_screen_k6b_stage3`）⛔ 給競合；W4 道路切分之
           單一真相源（`_road_halves` 之二呼叫）；W5 後處理之承受（`_stay`／`_recv_of`）；W6 ⛔ 案件字面。
           另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 無標的 ⇒ 紀錄⛔ 載競合。另於退縮 `3.5` 實跑三合成案（注入於
           harness 之 `ns`·⛔ 改檔）——`R3` 左端與 `R5` 右端（隔 `RD2` 相對）以所給之寬構末端帶（⛔ 未臨正街）：
           甲 ＝ 寬 `8`／`16`（地主 `G009` 之 `628(4)`／`628(3)` 競合·皆不成 ⇒ `R5` 右端由 `628-23(2)` 續試而成）；
           乙 ＝ 寬 `8`／`5.5`，`628-23(2)` 假設跨占街角規定範圍、`G009` 他街廓之片上鎖（整片只 `R5` 成）；
           丙 ＝ 寬 `8`／`5.0`，同乙（切半只 `R5` 成，`628(4)` 連其半併入 `628(3)`）。外部錨 ＝ 本器另寫之末端帶、
           交面積、切半之比與 G 公式（⛔ 呼叫 `end_block_*`／`_end_band`／`_end_region_R`／`solve_G_binary`）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _fn_src(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return ast.get_source_segment(src, n)
    return None


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__, str(ex)[:160])
    out.append((name, got, exp))


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    return red


# ── 玩具 ──
def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a, lot=None):
    return {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


H = "住宅區"


def _world1(a=None, extra=(), own_extra=None, x3_cat="道路", split_by=False, x5=False):
    """題一之玩具。道路 RX 之中心線 y ＝ -4 ⇒ X3(1)（y∈[-10,0]）切為上 0.4（鄰 BX）／下 0.6（鄰 BY）。"""
    a = dict(dict(X1=100, X2=60, X3=80, Y1=90, Y2=50, K1=70, K2=40, P=900, Q=900, R0=350, M1=30, M2=40, X5=20),
             **(a or {}))
    x3_blk = "RX" if x3_cat == "道路" else "PX"
    t = [_tp("X1(1)", "BX", H, _R(0, 5, 0, 30), a["X1"]), _tp("X2(1)", "BX", H, _R(5, 10, 0, 30), a["X2"]),
         _tp("K1(1)", "BX", H, _R(10, 15, 0, 30), a["K1"]), _tp("K2(1)", "BX", H, _R(15, 20, 0, 30), a["K2"]),
         _tp("P(1)", "BX", H, _R(20, 40, 0, 30), a["P"]),
         _tp("X3(1)", x3_blk, x3_cat, _R(0, 5, -10, 0), a["X3"]),
         _tp("Y1(1)", "BY", H, _R(0, 5, -40, -10), a["Y1"]), _tp("Y2(1)", "BY", H, _R(5, 10, -40, -10), a["Y2"])]
    if x5:
        t += [_tp("X5(1)", "RX", "道路", _R(5, 10, -3, 0), a["X5"]), _tp("R0(1)", "RX", "道路", _R(10, 40, -10, 0), a["R0"]),
              _tp("R9(1)", "RX", "道路", _R(5, 10, -10, -3), 5.0)]
    else:
        t += [_tp("R0(1)", "RX", "道路", _R(5, 40, -10, 0), a["R0"])]
    if split_by:
        t += [_tp("M1(1)", "BY", H, _R(10, 15, -40, -10), a["M1"]), _tp("M2(1)", "BY", H, _R(15, 20, -40, -10), a["M2"]),
              _tp("Q(1)", "BY", H, _R(20, 40, -40, -10), a["Q"])]
    else:
        t += [_tp("Q(1)", "BY", H, _R(10, 40, -40, -10), a["Q"])]
    t += [dict(e) for e in extra]
    own = {"X1": "g1", "X2": "g1", "X3": "g1", "X5": "g1", "Y1": "g1", "Y2": "g1", "K1": "gK", "K2": "gK",
           "P": "gP", "Q": "gQ", "R0": "gR", "R9": "gR", "M1": "gM", "M2": "gM"}
    own.update(own_extra or {})
    blocks = {"BX": {"category": H}, "BY": {"category": H}, "RX": {"category": "道路"}}
    if x3_cat != "道路":
        blocks["PX"] = {"category": x3_cat}
    for e in extra:
        blocks.setdefault(e["所屬街廓"], {"category": e["街廓分類"]})
    cl = {"RX": [(-10.0, -4.0), (50.0, -4.0)]}
    return t, own, blocks, cl


def _world2(a=None):
    """題二之玩具：一街廓 BZ（x∈[0,40]）；甲 Z1(1)[0,5]／Z4(1)[5,30]／Z2(1)[30,35]；他人 W1(1)[35,40]（右端最外）；
    道路 RZ：甲 Z3(1)[0,20]、他人 W3(1)[20,40]；他人 W2(1) 於 BW。"""
    a = dict(dict(Z1=100, Z4=200, Z2=80, W1=60, W2=90, Z3=70, W3=300), **(a or {}))
    t = [_tp("Z1(1)", "BZ", H, _R(0, 5, 0, 30), a["Z1"]), _tp("Z4(1)", "BZ", H, _R(5, 30, 0, 30), a["Z4"]),
         _tp("Z2(1)", "BZ", H, _R(30, 35, 0, 30), a["Z2"]), _tp("W1(1)", "BZ", H, _R(35, 40, 0, 30), a["W1"]),
         _tp("Z3(1)", "RZ", "道路", _R(0, 20, -10, 0), a["Z3"]), _tp("W3(1)", "RZ", "道路", _R(20, 40, -10, 0), a["W3"]),
         _tp("W2(1)", "BW", H, _R(35, 40, -40, -10), a["W2"])]
    own = {"Z1": "g1", "Z4": "g1", "Z2": "g1", "Z3": "g1", "W1": "gW", "W3": "gW", "W2": "gW"}
    blocks = {"BZ": {"category": H}, "RZ": {"category": "道路"}, "BW": {"category": H}}
    return t, own, blocks, {"RZ": [(-10.0, -5.0), (50.0, -5.0)]}


def _cbs(targets, drop=(), bad_if_grow=()):
    """玩具之回呼：`alloc_eval` 以 G ＝ 分攤登記面積 ＋ 面積（a′ 之累加）逐端依所給之候選序評選（門檻 ＝ R_end）；
    `alloc_state` 以 `drop` 為恆不配得之宗、`bad_if_grow` 之宗一旦受併即使其街廓之配餘地不合格。"""
    def g(t):
        return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)

    def a_prime(src, dst):
        return g(src)

    def alloc_eval(temp, build):
        by = {b["暫編地號"]: b for b in build}
        out = {}
        for (blk, sd), cfg in targets.items():
            rows, win = [], None
            for c in cfg["cands"]:
                if c not in by:
                    continue
                ok = g(by[c]) >= cfg["thr"]
                rows.append({"暫編地號": c, "原地號": by[c]["原地號"], "跨占R_end(㎡)": cfg.get("cross", {}).get(c, 10.0),
                             "試算G(㎡)": round(g(by[c]), 2), "臨正街寬(m)": 5.0, "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out.setdefault(blk, {})[sd] = {"觸發": True, "R_end(㎡)": cfg["thr"], "候選": rows, "當選": win}
        return out

    def alloc_state(temp, build):
        kept, bad = {}, {}
        for b in build:
            if b["暫編地號"] in drop:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            if b["暫編地號"] in bad_if_grow and float(b.get("面積_m2", 0) or 0) > 0:
                bad[b["所屬街廓"]] = bad.get(b["所屬街廓"], 0) + 1
        return {"kept": kept, "bad_pools": bad, "err": None}
    return a_prime, alloc_eval, alloc_state


def _go(ns, world, targets, **kw):
    temp, own, blocks, cl = world
    temp = copy.deepcopy(temp)
    build = [t for t in temp if t["街廓分類"] == H]
    ap, ev, st = _cbs(targets, **kw)
    t2, b2, log, rec = ns["end_block_merge_run"](temp, build, own, set(), set(), blocks, cl, ap, ev, st,
                                                 setback=3.5, log_print=lambda *x: None)
    by = {t["暫編地號"]: t for t in t2}
    main = [(x["候選"], x["層級"], x["結果"], x["檢核"]) for x in log if x.get("序") != "後處理"]
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]))
            for x in log if x.get("序") == "後處理"]
    ar = {k: round(float(v.get("面積_m2", 0) or 0), 4) for k, v in by.items() if float(v.get("面積_m2", 0) or 0)}
    bl = sorted(b["暫編地號"] for b in b2)
    return main, post, rec.get("皆未達"), ar, bl


def _halt(ns, world, targets, phrase, **kw):
    try:
        _go(ns, world, targets, **kw)
    except RuntimeError as e:
        return ("停機", phrase in str(e))
    return ("無停機",)


A1, B1 = ("BX", "left"), ("BY", "left")


def _T(thrA, thrB, cA=None, cB=None, ca=("X1(1)", "X2(1)", "K1(1)"), cb=("Y1(1)", "Y2(1)")):
    return {A1: dict(thr=thrA, cands=list(ca), cross=cA or {}), B1: dict(thr=thrB, cands=list(cb), cross=cB or {})}


L2, R2 = ("BZ", "left"), ("BZ", "right")


def _T2(thrL, thrR, cL=None, cR=None):
    return {L2: dict(thr=thrL, cands=["Z1(1)"], cross=cL or {}),
            R2: dict(thr=thrR, cands=["W1(1)", "Z2(1)"], cross=cR or {})}


_D = ("X2(1)", "—", "略·已定案", "—")
_K = ("K1(1)", "—", "略·已定案", "—")
_YD = ("Y2(1)", "—", "略·已定案", "—")
_YS = ("Y2(1)", "—", "略·競合歸他端", "—")


def _cases(ns):
    out = []
    w = _world1()
    # X1 100／X2 60／X3 80（上 32·下 48）／Y1 90／Y2 50；甲於 BX 之相連 ＝ 160，於 BY ＝ 140
    _run(out, "TA 題一 ① 二端皆以本街廓內之土地成 ⇒ 道路於後處理依中心線切分各歸",
         lambda: _go(ns, w, _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {}, {"X1(1)": 92.0, "Y1(1)": 98.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TB 題一 ① 只 A 成 ⇒ 只一端需要 ⇒ B 整片成",
         lambda: _go(ns, w, _T(160, 220)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "②", "成", "通過"), _D, _K, _YD], [], {},
          {"X1(1)": 60.0, "Y1(1)": 130.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TC 題一 ① 只 A 成、B 整片未成（Y1 配得）⇒ 道路之下半併 Y1、Y2 照配",
         lambda: _go(ns, w, _T(160, 300)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "②", "未成", "—"), _D, _K, _YS],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {"BY": ["left"]}, {"X1(1)": 92.0, "Y1(1)": 48.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TD 題一 ① 只 A 成、B 整片未成（Y1 不配得）⇒ Y1 併入 X1、道路之下半併 Y2",
         lambda: _go(ns, w, _T(160, 300), drop={"Y1(1)"}),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "②", "未成", "—"), _D, _K, _YS],
          [("Y1(1)", "後處理(a)", "成", "X1(1)"), ("X3(1)", "後處理(b)", "成", ("X1(1)", "Y2(1)"))], {"BY": ["left"]},
          {"X1(1)": 182.0, "Y2(1)": 48.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y2(1)"]))
    _run(out, "TE 題一 切半二端皆成（上 0.4／下 0.6）",
         lambda: _go(ns, w, _T(190, 185)),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "成", "通過"), _D, _K, _YD], [], {},
          {"X1(1)": 92.0, "Y1(1)": 98.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TF 題一 切半只 A 成、Y1 連其半配得 ⇒ 其半併 Y1",
         lambda: _go(ns, w, _T(190, 189)),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "未成", "—"), _D, _K, _YS],
          [("Y1(1)", "題一 4", "成", "Y1(1)")], {"BY": ["left"]}, {"X1(1)": 92.0, "Y1(1)": 48.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TG 題一 切半只 A 成、Y1 連其半不能配得 ⇒ 連同其半併入 X1",
         lambda: _go(ns, w, _T(190, 189), bad_if_grow={"Y1(1)"}),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "未成", "—"), _D, _K, _YS],
          [("Y1(1)", "題一 4", "成", "X1(1)")], {"BY": ["left"]}, {"X1(1)": 230.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y2(1)"]))
    _run(out, "TH 題一 整片只 A 成",
         lambda: _go(ns, w, _T(230, 225)),
         ([("X1(1)", "②", "成", "通過"), ("Y1(1)", "②", "未成", "—"), _D, _K, _YS], [], {"BY": ["left"]},
          {"X1(1)": 140.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TI 題一 整片二端皆成 ⇒ 交面積大者（B 30 ＞ A 15）；A 續試他人",
         lambda: _go(ns, w, _T(230, 210, cA={"X1(1)": 10, "X2(1)": 5}, cB={"Y1(1)": 20})),
         ([("Y1(1)", "②", "成", "通過"), ("X1(1)", "②", "未成", "通過"), ("X2(1)", "—", "略·競合歸他端", "—"),
           ("K1(1)", "①", "未成", "—"), _YD], [], {"BX": ["left"]}, {"Y1(1)": 130.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "X2(1)", "Y1(1)"]))
    _run(out, "TJ 題一 整片二端皆成·交面積並列 ⇒ 跨占者暫編地號小者",
         lambda: _go(ns, w, _T(230, 210, cA={"X1(1)": 10}, cB={"Y1(1)": 10})),
         ([("X1(1)", "②", "成", "通過"), ("Y1(1)", "②", "未成", "通過"), _D, _K, _YS], [], {"BY": ["left"]},
          {"X1(1)": 140.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TK 題一 皆不成 ⇒ 二端皆⛔ 併；A 由他人（K1 併 K2）續試而成",
         lambda: _go(ns, _world1({"K2": 200}), _T(250, 300, ca=("X1(1)", "K1(1)"))),
         ([("X1(1)", "②", "未成", "—"), ("Y1(1)", "②", "未成", "—"), ("K1(1)", "①", "成", "免"), _YS], [],
          {"BY": ["left"]}, {"K1(1)": 200.0}, ["K1(1)", "P(1)", "Q(1)", "X1(1)", "X2(1)", "Y1(1)", "Y2(1)"]))
    _run(out, "TL 題一 夥伴之端先由他人定案 ⇒ 競合消滅·逐列（B 整片成）",
         lambda: _go(ns, w, _T(105, 215, ca=("K1(1)", "X1(1)"))),
         ([("K1(1)", "①", "成", "免"), ("X1(1)", "—", "略·已定案", "—"), ("Y1(1)", "②", "成", "通過"), _YD], [], {},
          {"K1(1)": 40.0, "Y1(1)": 130.0}, ["K1(1)", "P(1)", "Q(1)", "X1(1)", "X2(1)", "Y1(1)"]))
    _run(out, "TM 題一 A 擱置中 B 由他人（M1 併 M2）定案 ⇒ 釋出·A 逐列成（Y2 不配得 ⇒ 併 Y1）",
         lambda: _go(ns, _world1({"M2": 100}, split_by=True), _T(150, 120, ca=("X1(1)",), cb=("M1(1)", "Y1(1)")),
                     drop={"Y2(1)"}),
         ([("M1(1)", "①", "成", "免"), ("X1(1)", "①", "成", "免"), ("Y1(1)", "—", "略·已定案", "—")],
          [("Y2(1)", "後處理(a)", "成", "Y1(1)"), ("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {},
          {"M1(1)": 100.0, "X1(1)": 92.0, "Y1(1)": 98.0}, ["K1(1)", "K2(1)", "M1(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    _run(out, "TN 題一 公設片平分（0.5／0.5）二端皆成",
         lambda: _go(ns, _world1(x3_cat="鄰里公園"), _T(200, 180)),
         ([("X1(1)", "②半", "成", "通過"), ("Y1(1)", "②半", "成", "通過"), _D, _K, _YD], [], {},
          {"X1(1)": 100.0, "Y1(1)": 90.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    w2 = _world2()
    # 甲相連 ＝ Z1 100 ＋ Z4 200 ＋ Z2 80 ＝ 380；＋ Z3 70 ＝ 450；W1 ＋ W3 ＝ 360
    _W1 = ("W1(1)", "②", "未成", "—")
    _run(out, "TO 題二 ① 只左拿得下",
         lambda: _go(ns, w2, _T2(380, 400)),
         ([_W1, ("Z1(1)", "①", "成", "免"), ("Z2(1)", "①", "未成", "—")], [("Z3(1)", "後處理(b)", "成", "Z1(1)")],
          {"BZ": ["right"]}, {"Z1(1)": 350.0}, ["W1(1)", "W2(1)", "Z1(1)"]))
    _run(out, "TP 題二 ① 二端皆拿得下 ⇒ 交面積大者（右 20 ＞ 左 10）",
         lambda: _go(ns, w2, _T2(380, 380, cL={"Z1(1)": 10}, cR={"Z2(1)": 20})),
         ([_W1, ("Z2(1)", "①", "成", "免"), ("Z1(1)", "①", "未成", "免")], [("Z3(1)", "後處理(b)", "成", "Z2(1)")],
          {"BZ": ["left"]}, {"Z2(1)": 370.0}, ["W1(1)", "W2(1)", "Z2(1)"]))
    _run(out, "TQ 題二 ① 二端皆拿得下·交面積並列 ⇒ 前緣線 p1 側（左）",
         lambda: _go(ns, w2, _T2(380, 380, cL={"Z1(1)": 10}, cR={"Z2(1)": 10})),
         ([_W1, ("Z1(1)", "①", "成", "免"), ("Z2(1)", "①", "未成", "免")], [("Z3(1)", "後處理(b)", "成", "Z1(1)")],
          {"BZ": ["right"]}, {"Z1(1)": 350.0}, ["W1(1)", "W2(1)", "Z1(1)"]))
    _run(out, "TR 題二 ② 只右拿得下",
         lambda: _go(ns, w2, _T2(460, 440)),
         ([_W1, ("Z2(1)", "②", "成", "通過"), ("Z1(1)", "②", "未成", "—")], [], {"BZ": ["left"]},
          {"Z2(1)": 370.0}, ["W1(1)", "W2(1)", "Z2(1)"]))
    _run(out, "TS 題二 二端皆拿不下 ⇒ 皆⛔ 併",
         lambda: _go(ns, w2, _T2(500, 500)),
         ([_W1, ("Z1(1)", "—", "未成", "—"), ("Z2(1)", "—", "未成", "—")], [], {"BZ": ["left", "right"]}, {},
          ["W1(1)", "W2(1)", "Z1(1)", "Z2(1)", "Z4(1)"]))
    # ── 停機 ──
    _run(out, "H1 同一合併群之候選分屬三個末端塊 ⇒ 停機",
         lambda: _halt(ns, w, {A1: dict(thr=500, cands=["X1(1)"]), B1: dict(thr=500, cands=["Y1(1)"]),
                               ("BY", "right"): dict(thr=500, cands=["Y2(1)"])}, "[末端塊合併再試] 同一合併群"),
         ("停機", True))
    _run(out, "H2 一筆土地同時跨占二末端塊 ⇒ 停機",
         lambda: _halt(ns, w, {A1: dict(thr=500, cands=["X1(1)"]), ("BX", "right"): dict(thr=500, cands=["X1(1)"])},
                       "一筆土地同時跨占二末端塊"), ("停機", True))
    wk = _world1(extra=[_tp("KR(1)", "RX", "道路", _R(40, 45, -10, 0), 20), _tp("K3(1)", "BY", H, _R(40, 45, -40, -10), 20),
                        _tp("K4(1)", "BX", H, _R(40, 45, 0, 30), 20)],
                 own_extra={"KR": "gK", "K3": "gK", "K4": "gK"})
    _run(out, "H3 一末端塊屬二競合 ⇒ 停機",
         lambda: _halt(ns, wk, {A1: dict(thr=500, cands=["X1(1)", "K4(1)"]), B1: dict(thr=500, cands=["Y1(1)"]),
                                ("BY", "right"): dict(thr=500, cands=["K3(1)"])}, "屬二以上之競合（K-9-50 射程 ③·逐案呈核）"),
         ("停機", True))
    # ── 後處理之承前 ──
    wp1 = _world1(extra=[_tp("W5(1)", "BW", H, _R(5, 10, -60, -40), 30)], own_extra={"W5": "g1"})
    _run(out, "P1 他街廓依原位次配得之宗照配（⛔ 動·⛔ 停機）",
         lambda: _go(ns, wp1, _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)"))], {}, {"X1(1)": 92.0, "Y1(1)": 98.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "W5(1)", "X1(1)", "Y1(1)"]))
    wp2 = _world1(extra=[_tp("G5(1)", "PK", "鄰里公園", _R(-10, 0, 0, 30), 90), _tp("W5(1)", "BW", H, _R(5, 10, -60, -40), 30),
                         _tp("W6(1)", "BW", H, _R(10, 15, -60, -40), 30)],
                  own_extra={"G5": "g1", "W5": "g1", "W6": "g1"})
    _run(out, "P2 公設片平分須由 BW 承受而其配得之宗二筆 ⇒ 停機（承受之宗未定）",
         lambda: _halt(ns, wp2, _T(160, 140), "承受之宗未定"), ("停機", True))
    wp3 = _world1(extra=[_tp("G5(1)", "PK", "鄰里公園", _R(-10, 0, 0, 30), 90), _tp("W5(1)", "BW", H, _R(5, 10, -60, -40), 30)],
                  own_extra={"G5": "g1", "W5": "g1"})
    _run(out, "P3 公設片三街廓平分，BW 由其唯一配得之宗承受",
         lambda: _go(ns, wp3, _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)")), ("G5(1)", "後處理(c)", "成", ("W5(1)", "X1(1)", "Y1(1)"))],
          {}, {"W5(1)": 30.0, "X1(1)": 122.0, "Y1(1)": 128.0},
          ["K1(1)", "K2(1)", "P(1)", "Q(1)", "W5(1)", "X1(1)", "Y1(1)"]))
    _run(out, "S1 道路片全在中心線之一側（X5）⇒ 不切、全歸該側",
         lambda: _go(ns, _world1(x5=True), _T(160, 140)),
         ([("X1(1)", "①", "成", "免"), ("Y1(1)", "①", "成", "免"), _D, _K, _YD],
          [("X3(1)", "後處理(b)", "成", ("X1(1)", "Y1(1)")), ("X5(1)", "後處理(b)", "成", "X1(1)")], {},
          {"X1(1)": 112.0, "Y1(1)": 98.0}, ["K1(1)", "K2(1)", "P(1)", "Q(1)", "X1(1)", "Y1(1)"]))
    return out


SELF_MUTS = [
    ("M1 ⛔ 交競合（逐列）", "end_block_merge_run", "contests=(_ct or None))", "contests=None)"),
    ("M2 交面積之比較反向", "k6b_stage3_run",
     "return (A, B) if float(A['area']) > float(B['area']) else (B, A)",
     "return (B, A) if float(A['area']) > float(B['area']) else (A, B)"),
    ("M3 並列取暫編地號大者", "k6b_stage3_run", "return (A, B) if A['c'] < B['c'] else (B, A)",
     "return (B, A) if A['c'] < B['c'] else (A, B)"),
    ("M4 並列取 p2 側", "k6b_stage3_run", "return (A, B) if A['end'] == '左' else (B, A)",
     "return (B, A) if A['end'] == '左' else (A, B)"),
    ("M5 ⛔ 切半", "k6b_stage3_run", "_rh[e['k']] = _ct_try(e, _its, '②半')",
     "_rh[e['k']] = dict(_ct_try(e, _its, '②半'), ok=False)"),
    ("M6 未得之一端恆併入已取得之一端", "k6b_stage3_run", "if (Lo['c'] in _kb1 and not (_kb0 - _kb1)",
     "if (False and Lo['c'] in _kb1 and not (_kb0 - _kb1)"),
    ("M7 ⛔ 查三以上", "end_block_merge_run", "            if len(_hit) >= 3:", "            if False:"),
    ("M8 ⛔ 查一端二競合", "end_block_merge_run", "                if (_blk, _sd) in _tgc:", "                if False:"),
    ("M9 未得之一端⛔ 略同群之候選", "k6b_stage3_run",
     "            _skip.setdefault((e['blk'], e['end']), set()).update(_mem)", "            pass"),
    ("M10 無受併宗街廓之配得者⛔ 照配", "k6b_stage3_run", "        R = R - _stay\n", "        R = R\n"),
    ("M11 未得之一端之土地⛔ 歸已取得之一端", "k6b_stage3_run",
     "                    _cls['a'].append((x, _cl0['勝']['blk']))\n                    continue",
     "                    pass"),
    ("M12 道路片須恰切二", "k6b_stage3_run", "        if len(_parts) not in (1, 2):", "        if len(_parts) != 2:"),
    ("M13 ⛔ 擱置（逐列）", "k6b_stage3_run",
     "                elif _ci not in _susp:\n                    _susp[_ci] = [_r]\n                    continue",
     "                elif False:\n                    pass"),
    ("M14 夥伴之端定案⛔ 釋出", "k6b_stage3_run", "            if (not _was) and _tg in won:",
     "            if False:"),
]


def selftest(repo):
    try:
        ns, _ = _harvest(repo)
    except Exception as ex:  # noqa: BLE001
        print(f"  🔴 harvest 失敗：{type(ex).__name__}")
        print("⇒ 紅 ['harvest']；rc 1")
        return 1
    src = _read(repo, "app.py")
    if "contests=None" not in (_fn_src(src, "k6b_stage3_run") or "")[:400]:
        print("  🔴 受詞缺：k6b_stage3_run 之 contests")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（harvest 之 end_block_merge_run〔其內 k6b_stage3_run 為真〕）──")
    red = _report(_cases(ns))
    base_red = set(red)
    print("── 判別力（突變之函式以其原始碼改一處後重綁於 ns·每一突變須使至少一例轉紅·畢即復原）──")
    for mname, fname, x, y in SELF_MUTS:
        fsrc = _fn_src(src, fname)
        if fsrc is None or fsrc.count(x) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{0 if fsrc is None else fsrc.count(x)}）")
            red.append(mname.split()[0])
            continue
        orig = ns[fname]
        try:
            exec(compile(fsrc.replace(x, y, 1), "<mut>", "exec"), ns)
            turned = [n.split()[0] for n in _report(_cases(ns), verbose=False) if n not in base_red]
        except Exception as ex:  # noqa: BLE001
            turned = [f"重綁拋 {type(ex).__name__}"]
        finally:
            ns[fname] = orig
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    m0 = _report(_cases(ns), verbose=False)
    print(("  ✅ " if m0 == [n for n in red if n in base_red] else "  🔴 ") + f"M0 復原後：紅 {m0}")
    if m0 != [n for n in red if n in base_red]:
        red.append("M0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
def _wiring_checks(app, sel):
    res = []
    mr = _fn_src(app, "end_block_merge_run") or ""
    ok1 = (mr.count("contests=(_ct or None))") == 1 and "if len(_hit) >= 3:" in mr and "if (_blk, _sd) in _tgc:" in mr
           and "'形': ('二' if _hit[0][0] == _hit[1][0] else '一')" in mr and "k6b_stage3_run(_rows, _L, own_map" in mr)
    res.append(("W1 `end_block_merge_run` 交競合、三以上與一端二競合停機、題一／題二依街廓之同異", ok1, ""))
    k6 = _fn_src(app, "k6b_stage3_run") or ""
    ok2 = False
    if k6:
        fn = ast.parse(k6).body[0]
        kws = [a.arg for a in fn.args.kwonlyargs]
        dflt = {a.arg: d for a, d in zip(fn.args.kwonlyargs, fn.args.kw_defaults)}
        inner = {n.name: ast.get_source_segment(k6, n) for n in ast.walk(fn) if isinstance(n, ast.FunctionDef)}
        g = inner.get("_k950_rows") or ""
        ok2 = ("contests" in kws and isinstance(dflt.get("contests"), ast.Constant) and dflt["contests"].value is None
               and k6.count("for _r in _k950_rows(sorted(order, key=lambda r: r['最終序位'])):") == 1
               and "if not contests:\n            yield from rows\n            return" in g)
    res.append(("W2 `k6b_stage3_run`：`contests=None`、逐列之環經 `_k950_rows`、無競合 ⇒ 逐列依序", ok2, ""))
    k6c = _fn_src(sel, "run_corner_pk_k6b") or ""
    scr = _fn_src(app, "f3_screen_k6b_stage3") or ""
    ci = k6c.find('ns["k6b_stage3_run"](')
    si = scr.find("k6b_stage3_run(")
    ok3 = (ci >= 0 and si >= 0 and "contests" not in k6c[ci:ci + 400].split("finally:")[0]
           and "contests" not in scr[si:si + 400].split("finally:")[0])
    res.append(("W3 段三之二呼叫端（harness／畫面）⛔ 給競合", ok3, ""))
    ok4 = (k6.count("_road_halves(x, '") == 2 and k6.count("def _road_halves(") == 1
           and "_split(_geo[x], _line)" in k6 and k6.count("_split(") == 1)
    res.append(("W4 道路片之中心線切分 ＝ 單一真相源（後處理 (b) 與題一之切半）", ok4, ""))
    ok5 = ("R = R - _stay" in k6 and k6.count("_recv_of(") >= 5 and "def _recv_of(b):" in k6)
    res.append(("W5 後處理：無本段受併宗之街廓之配得者照配、承受之宗經 `_recv_of`", ok5, ""))
    lits = []
    for name, src in (("end_block_merge_run", mr), ("k6b_stage3_run", k6)):
        if src:
            for n in ast.walk(ast.parse(src)):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value):
                    lits.append((name, n.value))
    res.append(("W6 二函式內⛔ 案件字面", not lits and bool(mr) and bool(k6), f"案件字面 {lits}"))
    return res


WIRE_MUTS = [
    ("N1 ⛔ 交競合", "app.py", "                                           contests=(_ct or None))",
     "                                           contests=None)", "W1"),
    ("N2 逐列之環⛔ 經 `_k950_rows`", "app.py",
     "    for _r in _k950_rows(sorted(order, key=lambda r: r['最終序位'])):",
     "    for _r in sorted(order, key=lambda r: r['最終序位']):", "W2"),
    ("N3 後處理 (b) 另切", "app.py", "            _parts = _road_halves(x, '後處理 (b)')",
     "            _parts = list(_split(_geo[x], _geo[x].exterior))", "W4"),
    ("N4 ⛔ 照配", "app.py", "        R = R - _stay\n", "        R = R\n", "W5"),
]


def wiring(repo):
    app = _read(repo, "app.py")
    sel = _read(repo, "verify/selection_pipeline.py")
    print("── 接線（AST／字樣·app.py ＋ verify/selection_pipeline.py）──")
    red = []
    base = _wiring_checks(app, sel)
    for name, ok, note in base:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    for mname, f, x, y, exp in WIRE_MUTS:
        src = {"app.py": app, "verify/selection_pipeline.py": sel}[f]
        n = src.count(x)
        if n != 1:
            print(f"  🔴 {mname}：突變錨不存在（{n}）")
            red.append(mname.split()[0])
            continue
        m = src.replace(x, y, 1)
        a2, l2 = (m if f == "app.py" else app), (m if f == "verify/selection_pipeline.py" else sel)
        turned = [nm.split()[0] for (nm, ok, _), (_, ok0, _) in zip(_wiring_checks(a2, l2), base) if ok0 and not ok]
        ok = exp in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本器另寫之幾何與 G 公式（外部錨·同 F11／F12 之法）──
def _s_of(x, p1, d, u):
    import numpy as np
    v = np.asarray(x, float) - p1
    den = d[0] * u[1] - d[1] * u[0]
    return (v[0] * u[1] - v[1] * u[0]) / den


def _halfplane(p1, d, u, s_lo, s_hi, big):
    from shapely.geometry import Polygon
    a = p1 + s_lo * d
    b = p1 + s_hi * d
    return Polygon([a - big * u, b - big * u, b + big * u, a + big * u])


def _frame(P, blk):
    import numpy as np
    from shapely.geometry import Polygon
    bp = Polygon(P["cb_by"][blk]["vertices"]).buffer(0)
    fl = P["cad"]["front_lines"][blk]
    p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
    L = float(np.linalg.norm(p2 - p1))
    d = (p2 - p1) / L
    u = np.array(P["cad"]["alloc_dir_by_block"][blk], float)
    u = u / np.linalg.norm(u)
    big = 4 * float(np.hypot(*(np.array(bp.bounds[2:]) - np.array(bp.bounds[:2]))))
    return bp, p1, p2, L, d, u, big


def _band(P, blk, side, wid):
    """外部錨：末端帶 ＝ 過該端之 FRONT 端點、∥ 分配線、向街廓內垂距 `wid` 之帶 ∩ 街廓（本器另寫）。"""
    import numpy as np
    from shapely.geometry import Polygon
    bp, p1, p2, L, d, u, big = _frame(P, blk)
    e = p1 if side == "left" else p2
    ca = u
    nrm = np.array([-ca[1], ca[0]])
    if float(np.dot(np.asarray(bp.centroid.coords[0]) - e, nrm)) < 0:
        nrm = -nrm
    return Polygon([e - big * ca, e + big * ca, e + big * ca + wid * nrm, e - big * ca + wid * nrm]).intersection(bp)


def _anchor_G(P, blk, a, fin, side, pre_zone):
    """外部錨：該端第 1 位之 G（無未臨正街·G 之 S ＝ 沿 FRONT 之寬）——本器另寫之二分法。"""
    bp, p1, p2, L, d, u, big = _frame(P, blk)
    l2 = float(fin["sb_rows_by_label"][blk]["正街尺度"])
    post = float(fin["post_price_by_block"][blk])
    pre = float(fin["pre_price_by_zone"].get(pre_zone, 0.0) or 0.0)
    A = post / pre if pre > 0 else 1.0
    B, C = fin["B"], fin["C"]
    smin = min(_s_of(v, p1, d, u) for v in bp.exterior.coords)
    smax = max(_s_of(v, p1, d, u) for v in bp.exterior.coords)
    lo, hi = 0.0, L
    for _ in range(100):
        m = (lo + hi) / 2
        hp = _halfplane(p1, d, u, smin - 1.0, m, big) if side == "left" else _halfplane(p1, d, u, L - m, smax + 1.0, big)
        if bp.intersection(hp).area - (a * (1 - A * B) - m * l2) * (1 - C) < 0:
            lo = m
        else:
            hi = m
    S = (lo + hi) / 2
    return round((a * (1 - A * B) - S * l2) * (1 - C), 2)


def _aprime(snapshot, src, dst):
    fv3 = snapshot["財務接線_v3"]
    z, p = fv3["原地號_區段"], fv3["重劃前區段_面積單價"]
    ps = float(p[z[src["原地號"]]]["單價_元每m2"])
    pd_ = float(p[z[dst["原地號"]]]["單價_元每m2"])
    return (float(src.get("分攤登記面積_m2", 0) or 0) + float(src.get("面積_m2", 0) or 0)) * ps / pd_


SCEN = {
    "甲": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 16.0}, lock=[], excl=[]),
    "乙": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 5.5},
              lock=["628(1)", "628(2)", "628(5)", "628-1(1)", "628-1(2)", "628-1(3)"], excl=["628-23(2)"]),
    "丙": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 5.0},
              lock=["628(1)", "628(2)", "628(5)", "628-1(1)", "628-1(2)", "628-1(3)"], excl=["628-23(2)"]),
}


def _pipeline(ns, fake_st, rv, sb, scen=None):
    import numpy as np
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from selection_pipeline import run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    saved = {k: ns[k] for k in ("end_block_host", "end_block_merge_run", "end_block_side_geom")}
    cfg = SCEN.get(scen) or dict(wid={}, lock=[], excl=[])
    hits = {"host": 0, "merge": 0, "geo": 0}

    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
        # 注入：所給之端 ⇒ 末端塊（⛔ 未臨正街），R_end ＝ 以所給之寬構之末端帶（經宿主之 `_end_band`）
        w = cfg["wid"].get((_label, side))
        if w is None:
            return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
                                                min_width, side, _label=_label)
        hits["geo"] += 1
        p1 = np.asarray(corner_pt, float)[:2]
        dd = np.asarray(d_hat, float)[:2]
        sp2 = float(np.dot(np.asarray(front_p2, float)[:2] - p1, dd))
        e = p1 if side == "left" else p1 + sp2 * dd
        band = ns["_end_band"](block_poly, cad_alloc, e, w, _label=_label)
        rr = ns["_strip_s_range"](band, d_hat, corner_pt, allocation_dir)
        buf = float(rr[1]) if side == "left" else float(sp2 - float(rr[0]))
        return {"gate": True, "unfront": 0.0, "s_back": 0.0, "r_end": band, "r_end_area": float(band.area),
                "band_area": float(band.area), "buf": buf}

    def host(ordered, **kw):
        if cfg["excl"]:
            crp = dict(kw["corner_range_polys"])
            fake = [Polygon(e["tp"]["polygon_coords"]).buffer(0) for e in ordered
                    if e["tp"].get("暫編地號") in cfg["excl"]]
            if fake:
                hits["host"] += 1
                for sd in ("left", "right"):
                    crp[sd] = unary_union(fake + ([crp[sd]] if crp.get(sd) is not None else []))
            kw["corner_range_polys"] = crp
        return saved["end_block_host"](ordered, **kw)

    def merge(temp, build, own, locked, corner, *a, **k):
        if cfg["lock"]:
            hits["merge"] += 1
        return saved["end_block_merge_run"](temp, build, own, set(locked) | set(cfg["lock"]), corner, *a, **k)
    ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            snapshot = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
            rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        out = dict(cb_by=cb_by, cad=cad, snapshot=snapshot, params=params, hits=hits, err=None, temp0=temp_p)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                    ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
        except RuntimeError as e:
            out["err"] = ("段三／合併再試", str(e).splitlines()[0][:400])
            return out
        ss = fake_st.session_state
        out["rec"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_MERGE"]))
        out["log"] = copy.deepcopy(ss.get("f3_end_block_merge_log") or [])
        out["temp"], out["build"] = tp3, bp3
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ns["K917_DROPPED"].clear()
                sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                eff_min_build_by_blk={})
        except RuntimeError as e:
            out["err"] = ("配地", str(e).splitlines()[0][:400])
            return out
        out["ev"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_EVAL"]) or {})
        out["rows"] = sg["g_rows"]
        return out
    finally:
        for k, v in saved.items():
            ns[k] = v


def _blk_check(P, blk):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    rows = [r for r in P["rows"] if r.get("所屬街廓") == blk]
    bp = Polygon(P["cb_by"][blk]["vertices"]).buffer(0)
    polys = [(r["暫編地號"], Polygon(r["cut_coords"]).buffer(0), r) for r in rows
             if r.get("cut_coords") and not isinstance(r.get("cut_coords"), str)]
    un = unary_union([p for _, p, _ in polys])
    ovl = sum(polys[i][1].intersection(polys[j][1]).area for i in range(len(polys)) for j in range(i + 1, len(polys)))
    return polys, un.symmetric_difference(bp).area, ovl


def _head(polys, side):
    cand = [r for _, _, r in polys if r.get("推進側別") == side and "抵費地" not in str(r.get("暫編地號"))]
    return sorted(cand, key=lambda r: float(r.get("累積S(m)", 0) or 0))[0] if cand else None


def run(repo, sbs):
    from shapely.geometry import Polygon, LineString
    from shapely.ops import split, unary_union
    import numpy as np
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        src = _read(repo, "app.py")
        if "contests=None" not in (_fn_src(src, "k6b_stage3_run") or "")[:400]:
            print("  🔴 受詞缺：k6b_stage3_run 之 contests")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from stepg_pipeline import _compute_v3_finance
        for sb in sbs:
            P = _pipeline(ns, fake_st, rv, sb)
            if P["err"]:
                print(f"🔴 執行中止（退縮 {sb}·{P['err'][0]}）：{P['err'][1]} ⇒ 無從判定")
                return 3
            ok = P["rec"] == {"退縮": sb, "標的": [], "皆未達": {}} and P["log"] == []
            print(("  ✅" if ok else "  🔴") + f" R1 退縮 {sb}：合併再試紀錄 {P['rec']}（⛔ 載競合）；逐列 {len(P['log'])}")
            if not ok:
                red.append(f"R1@{sb}")
        sb = 3.5
        fin = None
        for scen in ("甲", "乙", "丙"):
            P = _pipeline(ns, fake_st, rv, sb, scen)
            if fin is None:
                fin = _compute_v3_finance(ns, P["snapshot"], list(P["cb_by"].values()), P["cad"])
            cfg = SCEN[scen]
            print(f"══ 合成案{scen}（退縮 {sb}·注入 末端帶寬 {list(cfg['wid'].values())}、上鎖 {len(cfg['lock'])}、"
                  f"假設跨占街角 {cfg['excl']}·咬到 {P['hits']}）══")
            bit = P["hits"]["geo"] > 0 and (P["hits"]["merge"] > 0 if cfg["lock"] else True) and \
                (P["hits"]["host"] > 0 if cfg["excl"] else True)
            if not bit:
                print("  🔴 注入未咬到 ⇒ 無從判定")
                red.append(f"注入@{scen}")
                continue
            if P["err"]:
                print(f"  🔴 執行中止：{P['err']}")
                red.append(f"中止@{scen}")
                continue
            rec, log = P["rec"], P["log"]
            by0 = {t["暫編地號"]: t for t in P["temp0"]}
            by = {t["暫編地號"]: t for t in P["temp"]}
            own = fake_st.session_state.get("t8_ownership_map", {}) or {}
            main = [(r["候選"], r["層級"], r["結果"], r["檢核"]) for r in log if r.get("序") != "後處理"]
            post = [(r["候選"], r["層級"], r["結果"], r["受併宗"]) for r in log if r.get("序") == "後處理"]
            # 外部錨：地主 G009 原有土地與二端末端帶之交（競合之交面積）
            bA, bB = _band(P, "R3", "left", cfg["wid"][("R3", "left")]), _band(P, "R5", "right", cfg["wid"][("R5", "right")])
            gid = own.get("628")
            g9 = [Polygon(t["polygon_coords"]).buffer(0) for t in P["temp0"] if own.get(t.get("原地號")) == gid
                  and len(t.get("polygon_coords") or []) >= 3]
            xa = round(sum(p.intersection(bA).area for p in g9 if p.intersection(bA).area > 1.0), 2)
            xb = round(sum(p.intersection(bB).area for p in g9 if p.intersection(bB).area > 1.0), 2)
            ct = (rec or {}).get("競合") or []
            okc = (len(ct) == 1 and ct[0]["形"] == "一" and [e[:3] for e in ct[0]["列"]] == [["R3", "左", "628(4)"],
                                                                                               ["R5", "右", "628(3)"]]
                   and abs(ct[0]["列"][0][3] - xa) <= 0.02 and abs(ct[0]["列"][1][3] - xb) <= 0.02)
            print(("  ✅" if okc else "  🔴") + f" C{scen} 競合 ＝ {ct}；外部錨之交面積 R3 左 {xa}／R5 右 {xb}")
            if not okc:
                red.append(f"C@{scen}")
            polys3, d3, o3 = _blk_check(P, "R3")
            polys5, d5, o5 = _blk_check(P, "R5")
            pools3 = [(k, p) for k, p, r in polys3 if "抵費地" in k]
            fp = [(k, p) for k, p in pools3 if abs(p.area - bA.area) <= 0.05 and p.symmetric_difference(bA).area <= 0.05]
            lx = sum(p.intersection(bA).area for k, p, r in polys3 if "抵費地" not in k)
            okr3 = (rec["皆未達"].get("R3") == ["left"] and len(fp) == 1 and lx <= 1e-4 and d3 <= 0.05 and o3 <= 0.05)
            print(("  ✅" if okr3 else "  🔴") + f" F{scen} R3 左強制抵費地 {fp and fp[0][0]}（{fp and round(fp[0][1].area, 2)}·"
                  f"外部錨末端帶 {bA.area:.2f}）；宗地 ∩ 帶 {lx:.6f}；聯集 △ 街廓 {d3:.4f}、兩兩疊 {o3:.4f}")
            if not okr3:
                red.append(f"F@{scen}")
            h5 = _head(polys5, "right")
            if scen == "甲":
                exp_main = [("628(4)", "②", "未成", "—"), ("628(3)", "②", "未成", "—"), ("628-34(2)", "—", "未成", "—"),
                            ("628-23(2)", "①", "成", "免"), ("628-22(2)", "—", "略·已定案", "—")]
                exp_post = [("628-23(3)", "後處理(b)", "成", "628-23(2)"), ("628-22(3)", "後處理(b)", "成", "628-23(2)")]
                # 外部錨：628-23(3)／628-22(3) 全在 RD2 中心線之一側（切分得 1 片）
                clp = P["cad"]["centerlines"]["RD2"]
                (x1, y1), (x2, y2) = clp[0], clp[-1]
                dv = np.array([x2 - x1, y2 - y1]) / float(np.hypot(x2 - x1, y2 - y1))
                ln = LineString([tuple(np.array([x1, y1]) - 500 * dv), tuple(np.array([x2, y2]) + 500 * dv)])
                one = all(len(list(split(Polygon(by0[x]["polygon_coords"]).buffer(0), ln).geoms)) == 1
                          for x in ("628-23(3)", "628-22(3)"))
                recv = "628-23(2)"
                add = sum(_aprime(P["snapshot"], by0[x], by0[recv]) for x in ("628-21(2)", "628-22(2)", "628-23(3)", "628-22(3)"))
                ga = _anchor_G(P, "R5", round(float(by0[recv]["分攤登記面積_m2"]) + add, 2), fin, "right",
                               by0[recv].get("重劃前地價區段", ""))
                ok = (main == exp_main and post == exp_post and one and rec["皆未達"] == {"R3": ["left"]}
                      and h5 is not None and h5["暫編地號"] == recv and abs(float(h5["G(㎡)"]) - ga) <= 0.02
                      and d5 <= 0.05 and o5 <= 0.05)
                print(("  ✅" if ok else "  🔴") + f" X甲：逐列 {main}；後處理 {post}；二片皆全在中心線之一側 {one}；"
                      f"R5 右鏈首宗 {h5 and h5['暫編地號']} G {h5 and h5['G(㎡)']} ＝ 外部錨 {ga}；R5 聯集 △ 街廓 {d5:.4f}、"
                      f"兩兩疊 {o5:.4f}")
                if not ok:
                    red.append("X甲")
            else:
                recv, los = "628(3)", "628(4)"
                if scen == "乙":
                    exp_main = [("628(3)", "②", "成", "通過"), ("628(4)", "②", "未成", "—"), ("628-34(2)", "—", "未成", "—")]
                    exp_post = [("628(4)", "後處理(a)", "成", "628(3)")]
                    okh = True
                    hnote = ""
                else:
                    exp_main = [("628(3)", "②半", "成", "通過"), ("628(4)", "②半", "未成", "—"), ("628-34(2)", "—", "未成", "—")]
                    exp_post = [("628(4)", "題一 4", "成", "628(3)")]
                    # 外部錨：628(6) 依 RD2 中心線切二，鄰 R5 者之比 × a′(628(6)→628(3)) ＝ 切半所併之量
                    clp = P["cad"]["centerlines"]["RD2"]
                    (x1, y1), (x2, y2) = clp[0], clp[-1]
                    dv = np.array([x2 - x1, y2 - y1]) / float(np.hypot(x2 - x1, y2 - y1))
                    ln = LineString([tuple(np.array([x1, y1]) - 500 * dv), tuple(np.array([x2, y2]) + 500 * dv)])
                    g6 = Polygon(by0["628(6)"]["polygon_coords"]).buffer(0)
                    parts = list(split(g6, ln).geoms)
                    b5 = Polygon(P["cb_by"]["R5"]["vertices"]).buffer(0)
                    f5 = sum(q.area for q in parts if q.distance(b5) < 1e-6) / g6.area
                    q5 = _aprime(P["snapshot"], by0["628(6)"], by0[recv]) * f5
                    q3 = _aprime(P["snapshot"], by0["628(6)"], by0[recv]) * (1.0 - f5)
                    wr = next(r for r in log if r.get("候選") == recv and r.get("序") != "後處理")
                    lr = next(r for r in log if r.get("候選") == los and r.get("序") == "後處理")
                    okh = (len(parts) == 2 and abs(float(wr["切分併入"].get("628(6)", -1)) - q5) <= 0.02
                           and abs(float(lr["切分併入"].get("628(6)", -1)) - q3) <= 0.02 and lr["整筆併入"] == [los])
                    hnote = f"；切半之量 {wr['切分併入']}／{lr['切分併入']} ＝ 外部錨 {q5:.4f}／{q3:.4f}（R5 側之比 {f5:.4f}）"
                add = _aprime(P["snapshot"], by0["628(6)"], by0[recv]) + _aprime(P["snapshot"], by0[los], by0[recv])
                ga = _anchor_G(P, "R5", round(float(by0[recv]["分攤登記面積_m2"]) + add, 2), fin, "right",
                               by0[recv].get("重劃前地價區段", ""))
                ok = (main == exp_main and post == exp_post and okh and rec["皆未達"] == {"R3": ["left"]}
                      and h5 is not None and h5["暫編地號"] == recv and abs(float(h5["G(㎡)"]) - ga) <= 0.02
                      and d5 <= 0.05 and o5 <= 0.05 and los not in {b["暫編地號"] for b in P["build"]})
                print(("  ✅" if ok else "  🔴") + f" X{scen}：逐列 {main}；後處理 {post}{hnote}；R5 右鏈首宗 "
                      f"{h5 and h5['暫編地號']} G {h5 and h5['G(㎡)']} ＝ 外部錨 {ga}；R5 聯集 △ 街廓 {d5:.4f}、兩兩疊 {o5:.4f}")
                if not ok:
                    red.append(f"X{scen}")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], argv[2]
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring":
        return wiring(repo)
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄丁　塊 `K3`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-50` 之立 ＋ 其落地狀態（`W-G.9-354`·⛔ 上文一字不刪·純末端追加）

### 🔒 `K-9-50`　**數末端塊之合併再試相互競合：隔道路相對之二末端塊，先各以本街廓內之土地試算，二端皆須道路或公設地上之土地者，道路以中心線切半、公設地按面積平分各試，不成再以整片各試；同一街廓兩端之末端塊，比照一筆土地同時跨占左右兩街角之裁，土地⛔ 切開**（KL 裁 `2026-09-28`·canonical·**逐字**）

**編號之由**（`W-G.9-354 §零-1`）：`K-9-50` 於開工態 `928d292` 之宣告框 `0`；鬆框 `1` 列（`docs/orders/W-G.9-333_重量單.md:34`）係其時「對照乙［必為零］」所列之未取號·⛔ 占用 ⇒ 取之。
**出處**：發單側窗四十九（`2026-09-28`）；呈文附示意圖二張（題一、題二·⛔ 入倉）；轉錄自發單側交接文四十九（修訂·`18657` B·`sha256` `63285a5bbc2976e1ce1c08f3c5a7944c763f68a49eea7860fd1b3481d988bab3`·該文⛔ 入倉）之 `§二` 與附錄甲。

**KL 之令（`2026-09-28 00:04`·逐字）**：
> 兩個以上末端塊同時想併到同一位地主的土地時，附圖及說明給我裁示

**發單側所呈（逐字·⛔ 增刪一字）**：

> 本題屬域裁，須請您裁示；另有一項知會，不須裁示。本案不會發生此情形，是為通則需要而問。我已先查過正典，末端塊之間的競合確實尚未裁示（`K-9-49` 射程 ③ 明載「候另呈」）。附圖兩張，皆為示意。
>
> **何時會發生**：末端塊各筆單獨試算都未達標時，依 `K-9-49 ②` 把跨占者與同一地主相鄰的土地合併後再試：先併同街廓內的土地，再併道路、公設地上的土地。如果同一位地主的土地同時跨占兩個末端塊，兩端的合併再試就會搶用同一批土地。實際上有下列兩種形態。
>
> ### 題一　隔道路相對的兩個末端塊（圖一）
>
> **【現況】**
> - 甲、乙兩街廓隔道路相對，兩者靠同一側的端點都沒有側街，因此都是末端塊。
> - 地主甲有一筆重劃前土地被新設道路切成三片：
>   - 甲-1 在甲街廓的末端塊範圍內；
>   - 甲-3 在道路上；
>   - 甲-2 在乙街廓的末端塊範圍內。
> - 兩端各筆單獨都未達標時，兩端的合併再試都要用道路上的甲-3。程式遇到這種情形會停止計算，並提示「尚未裁示」，不會自行決定。
>
> **【要改成】**（比照您對街角地跨道路兩側所作的裁示 `K-9-48` 其二，以及手冊 p.192 第 1 款「道路以中心線為界」）
> 1. **先用自己街廓內的土地**：兩端各先只用地主甲在自己街廓內的相鄰土地試算。能達標的一端即定案，不再動用道路或公設地上的土地。
> 2. **仍須動用道路土地時**：
>    - 只有一端需要：道路上的土地整片併入該端試算。
>    - 兩端都需要：先依道路中心線切半（公設地上的土地按面積平分），各併入一半試算。兩端都達標時，地主甲在兩端各配得一宗（圖一②）。
> 3. **切半後仍無法兩端都達標**：
>    - 只有一端達標：該端定案，另一端不得（圖一③）。
>    - 兩端都未達標：改用整片道路土地各試一次。
>      - 只有一端能達標：道路土地歸該端。
>      - 兩端都能達標：歸「地主甲原有土地落在其末端塊範圍內面積較大」的一端（比照 `K-9-27` 第 ③ 階）。面積也相同時，歸跨占者暫編地號較小的一端。
>      - 兩端都不能達標：兩端皆不併入。
> 4. **未取得的一端**：
>    - 照常由其他跨占者依原投影序續試；都未達標時，該端末端塊範圍即為強制抵費地。
>    - 地主甲在該端的土地（含切半時分給該端的一半道路土地）：能在該街廓依原位次配地者照配；不能者併入已取得的一端（比照 `K-9-48` 其二，並須通過「不影響原位次」檢核）。
>
> **【對土地的影響】**
> - **本案**：無。
>   - 本案唯一的末端塊是 R6 左端，已由 628-4(1) 單獨達標，不進入合併再試。
>   - 本案 R3 左端與 R5 右端隔 RD2 相對，正是題一的形態（圖一④）。但兩端未臨正街的面積都不超過 0.0001 ㎡，不構成末端塊。
> - **他案**（以圖一的示意數字說明：甲街廓末端塊範圍 165 ㎡、乙街廓 150 ㎡）：
>   - 切半後兩端都達標：地主甲兩端各配一宗，兩處都不成為抵費地。
>   - 只有一端能達標：另一端若無他人達標，該 150 ㎡ 成為強制抵費地。
>   - 現行做法：停止計算，沒有配地結果。
>
> ### 題二　同一街廓左右兩端都是末端塊（圖二）
>
> **【現況】**
> - 同一街廓左右兩端都沒有側街。
> - 地主甲的土地從左端末端塊範圍一路相連到右端（甲-1、甲-4、甲-2）。
> - 兩端的合併再試都會把同一批土地併入。程式同樣停止計算。
>
> **【要改成】** 比照您對「一筆土地同時跨占左右兩街角」的裁示（`K-9-24` 二、`K-9-27`）：
> - 兩端分別以地主甲相連的土地試算。
> - 只有一端能達標：歸該端。
> - 兩端都能達標：歸「地主甲原有土地落在其末端塊範圍內面積較大」的一端；面積相同則歸前緣線 p1 側。這相當於 `K-9-27` 第 ③、④ 階；末端塊沒有街角指數，所以沒有第 ①、② 階。
> - 兩端都不能達標：兩端皆不併入，照原位次辦理。
> - 土地不切開。另一端視為未被地主甲跨占，照常由其他跨占者續試；都未達標時即為強制抵費地。
>
> **【對土地的影響】**
> - **本案**：無。R4 的地主 G009 雖然土地橫跨左右兩端，但 R4 兩端都有側街，屬於街角地，不是末端塊。
> - **他案**（圖二示意）：地主甲在左端取得一宗；右端 135 ㎡ 若無他人達標，即成為強制抵費地。
>
> **【通知】** 三個以上末端塊同時牽涉同一地主土地的情形極少見，程式仍維持停止計算並提示，遇到時再逐案呈核。
>
> **【要你判斷】**
> 一、隔道路相對的兩個末端塊，是否依題一第 1～4 點處理？（是／否）
> 二、同一街廓兩端的末端塊，是否比照「一筆土地同時跨占左右兩街角」的方式處理（題二）？（是／否）

**KL 之答（`2026-09-28 00:30`·逐字）**：
> 題1、題2：都是

**裁之內容**（KL「題1、題2：都是」＝ 所呈【要你判斷】一、二皆「是」）：
① **題一**（隔道路相對之二末端塊·同一地主之土地分處二街廓之 `R_end` 及其間之道路、公設地）＝ 所呈題一【要改成】第 `1`〜`4` 點：
1. 二端各先只以地主於自己街廓內之相鄰土地試算；能達標之一端即定案，不再動用道路或公設地上之土地。
2. 仍須動用道路上之土地者：只一端需要 ⇒ 道路上之土地整片併入該端試算；二端皆需要 ⇒ 先依道路中心線切半（公設地上之土地按面積平分），各併入一半試算；二端皆達標 ⇒ 地主於二端各配得一宗。
3. 切半後仍無法二端皆達標：只一端達標 ⇒ 該端定案、另一端不得；二端皆未達標 ⇒ 改以整片道路土地各試一次——只一端能達標 ⇒ 道路土地歸該端；二端皆能 ⇒ 歸地主原有土地落在其 `R_end` 內面積較大之一端（比照 `K-9-27` 第 ③ 階），面積亦同 ⇒ 跨占者暫編地號較小之一端；二端皆不能 ⇒ 皆不併入。
4. 未取得之一端：照常由其他跨占者依原投影序續試，都未達標 ⇒ 該端 `R_end` 為強制抵費地；地主於該端之土地（含切半時分給該端之一半道路土地）能在該街廓依原位次配地者照配，不能者併入已取得之一端（比照 `K-9-48` 其二·須通過「不影響原位次」之檢核）。
② **題二**（同一街廓左右兩端皆為末端塊·地主之土地自一端之 `R_end` 相連至另一端）＝ 比照 `K-9-24 二`、`K-9-27`：二端分別以地主相連之土地試算；只一端能達標 ⇒ 歸該端；二端皆能 ⇒ 歸地主原有土地落在其 `R_end` 內面積較大之一端，面積相同 ⇒ 前緣線 `p1` 側（相當於 `K-9-27` 第 ③、④ 階；末端塊無街角指數 ⇒ 無第 ①、② 階）；二端皆不能 ⇒ 皆不併入，照原位次辦理；土地⛔ 切開；另一端視為未被該地主跨占，照常由其他跨占者續試，都未達標 ⇒ 強制抵費地。
③ 三個以上末端塊同時牽涉同一地主之土地 ⇒ 程式維持停止計算並提示，遇到時逐案呈核（所呈之【通知】·KL 未駁）。

**射程**：① 及於**任一案件**；
② 競合之判定、各試之時點與層次、「達標」之檢核、切半之作法與題一 `4` 之「能依原位次配地」之判 ⇒ 發單側之讀法（下開·⛔ 充裁）；
③ **⛔ 及於**：一筆土地（同一暫編地號）同時跨占同一街廓二末端塊之 `R_end`；同一末端塊同時屬二以上之競合——⛔ 據本裁推，遇者停機（逐案呈核·`GB-194`）；`K-9-48` 七項 `3`／`5`／`6`（可拆分者之部分併入、剩餘土地之去處）仍為承前缺口，遇者停機。

**發單側之讀法**（⛔ 充裁·以【通知】呈 KL）：
1. **競合之判定**：以合併群（`K-6 §一`·同地主 ∧ 地籍相連·⛔ 濾街廓）為單位；同一合併群之未達候選分屬二末端塊 ⇒ 競合；二末端塊屬同一街廓（左右端）⇒ 題二，分屬二街廓 ⇒ 題一。
2. **時點**：競合之二端各以該合併群於該端之首個未達候選（依原投影序）為其列；先至之列候其夥伴之列而二列並解（其間該端之後續列亦候之）；夥伴之端於此前已由他人定案 ⇒ 競合消滅，依逐列辦理。未取得之一端，該合併群之其他候選⛔ 再試（視為未被該地主跨占）。
3. **達標**：試算之當選者為該候選（`G ≥ area(R_end)`）；經道路或公設地上之土地併入者，並須通過「不影響原位次」之檢核（`K-9-48` 七項 `2`）。
4. **交之面積**：該地主之跨占候選各與該端 `R_end` 之交之和；比較至小數二位。
5. **切半**：道路上之土地依所屬道路之中心線切分（與段三後處理 (b) 同一函式）；片全在中心線之一側者不切、全歸該側；路口之道路片（臨接三面以上·含公設）與公設地上之土地按面積平分。二端所需之道路、公設地上之土地互不相涉者，各以其整片試（⛔ 切半）。
6. **題一 `4` 之判**：未取得之一端之候選連同分給該端之一半試算配地，該候選配得且該街廓之原位次不受影響（他宗之保留、配餘地之內接矩形）⇒ 其半併之；否則候選連同其半併入已取得之一端之受併宗，須通過「不影響原位次」之檢核（二街廓並驗），不過 ⇒ 停機（`K-9-48` 七項 `3`〜`5` 未落地）。
7. **後處理之承前**（`K-9-48` 其二「若可以在R5原位次配得土地(當然此時已非街角地)，仍照手冊道路用地上土地以中心分往2側有配地的建築街廓內合併」、其讀法 `1` ⑤「兩側均配得土地（街角或原位次）」）：合併群於本段無受併宗之街廓，其依原位次配得之宗照配，並承受分往該街廓之土地（道路之半、公設地之平分）；該街廓配得之宗不唯一者 ⇒ 題一未取得之一端取其候選，其餘 ⇒ 停機（承受之宗未定）。本讀法亦及於段三（街角合併重試）之後處理。
8. **題二之層次**：二端分別先以同街廓內之相連土地試算（`K-9-49 ②` 之序），二端皆拿不下再及道路、公設地上之相連土地；某一層有一端以上拿得下即依該層定之（二端皆拿得下 ⇒ 交之面積大者 → 前緣線 `p1` 側）。

**本案之量**（⛔ 為裁之一部·發單側窗五十·態 `928d292` ＋ `W-G.9-354` 之塊·harness·退縮 `3.5 m`／`0 m`）：本案⛔ 觸發——唯一之末端塊 `R6` 左端各筆單獨已由 `628-4(1)` 當選（合併再試無標的·紀錄⛔ 載競合）；`R3` 左端與 `R5` 右端（隔 `RD2` 相對·題一之形態）之未臨正街皆 ≤ `0.0001 ㎡`，不構成末端塊。配地⛔ 變。

**落地狀態**：
- 題一、題二之 **harness 路徑** ＝ `W-G.9-354` 工項二（側支 `verify/W-G.9-353-endmerge`）：`end_block_merge_run` 以合併群判競合，交 `k6b_stage3_run`（`contests`）依本裁處之——取代 `W-G.9-353` 之「競合 ⇒ 停機」；段三之呼叫⛔ 給競合（逐列依序·逐位同本批前）。
- 讀法 `7` 之後處理之承前 ＝ 同批（段三與末端塊合併再試共用）。
- **畫面路徑** ⬜（次單·`W-G.9-355`）。
- 裁之內容 `③` 與射程 `③` 之前二者 ⇒ 碼面停機（`GB-194`）。

**合成案之量**（⛔ 為裁之一部·發單側窗五十·harness·退縮 `3.5 m`·器 `verify/probes/probe_WG9354_endcontest.py run`·注入於器內·⛔ 改檔）：`R3` 左端與 `R5` 右端以所給之寬構末端帶（⛔ 未臨正街）——
甲 ＝ 寬 `8`／`16`：競合（題一）＝ 地主 `G009` 之 `628(4)`（`R3` 左·交 `66.49`）與 `628(3)`（`R5` 右·交 `237.57`）；二端皆無本街廓內之相鄰土地；切半與整片皆二端未成（整片：`628(4)` `258.96` ＜ `351.70`、`628(3)` `363.44` ＜ `761.15`）⇒ 二端皆不併入；`R5` 右端由其他跨占者續試，`628-23(2)` 以 ① 併 `628-21(2)`、`628-22(2)` 而成，其道路片 `628-23(3)`、`628-22(3)` 全在中心線之一側 ⇒ 不切、全歸之（鏈首宗 `G` `1422.89`）；`R3` 左端 ⇒ 強制抵費地 `351.70 ㎡`。
乙 ＝ 寬 `8`／`5.5`（`628-23(2)` 假設跨占街角規定範圍、`G009` 他街廓之片上鎖）：同一競合（交 `66.49`／`217.29`）；切半二端未成；整片只 `R5` 成（`628(3)` `363.44` ≥ `263.02`·驗「不影響原位次」通過；`628(4)` `258.96` ＜ `351.70`）⇒ 道路土地歸 `628(3)`；`628(4)` 不能依原位次配地 ⇒ 併入 `628(3)`（後處理 (a)·鏈首宗 `G` `408.48`）；`R3` 左端 ⇒ 強制抵費地 `351.70 ㎡`。
丙 ＝ 寬 `8`／`5.0`（同乙）：交 `66.49`／`207.25`；切半只 `R5` 成（`628(3)` 併其半 `170.7953` ⇒ `256.03` ≥ `239.17`·驗通過；`628(4)` 併其半 `170.9947` ⇒ `151.98` ＜ `351.70`；`R5` 側之面積比 `0.4997`）⇒ `628(3)` 定案；`628(4)` 連同其半不能依原位次配地 ⇒ 併入 `628(3)`（題一 `4`·鏈首宗 `G` `408.48`）；`R3` 左端 ⇒ 強制抵費地 `351.70 ㎡`。
三案之 `R5` 宗地聯集 △ 街廓皆 `0.0000`、兩兩疊皆 `0.0000`；`R3` 之聯集 △ 街廓皆 `0.0001`、兩兩疊皆 `0.0000`；諸數皆與器內另寫之外部錨相符。

🛑 **⛔ 據本節推**：⛔ 推射程 `③` 之任一情形之處置、⛔ 推強制抵費地作調配池（`K-9-38`〜`40`）之任何事項。
````

## 附錄戊　塊 `E4`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-354 §零-1`）：本批取 `546`／`547`（`2` 號）；皆係發單側窗五十於復驗 `W-G.9-353` 時所捕（其形先已由 CC 於 `W-G.9-352R`／`W-G.9-353R` 之自解具名）。

### 🩸 `自誤 546`　**`W-G.9-352`／`W-G.9-353` 之 `§零-1` 取號表，漏列其命令所傳之第三引數（`W-G.9-398`／`K-9-94`·對照甲′）之列**

**形**：`docs/orders/W-G.9-353_重量單.md` `§零-1` 之表，首列逐字含「`python verify/probes/wg9268_gate6_occupancy.py 0b05925 W-G.9-353 W-G.9-352 W-G.9-398`」，而表只列受詢、對照甲（`W-G.9-352`）、對照乙（`W-G.9-963`）三列；器將第三引數以「甲（須 ≥1）」出艙，其六數皆 `0`（鬆框 `6` 檔／`9` 列·態 `0b05925`），器仍 `rc 0`。`docs/orders/W-G.9-352_重量單.md` `§零-1` 同形（`… ed6871a W-G.9-352 W-G.9-351 W-G.9-398`·鬆框 `4` 檔／`7` 列；`… ed6871a K-9-49 K-9-48 K-9-94`·鬆框 `0`／`0`）。既例（`W-G.9-349`〜`351`）之表有「對照甲′［鬆框之漏框偵察］`W-G.9-398`」一列，載其宣告框 `0` 與鬆框之數。
**後果之界**：CC 於二批皆須以自解判第三引數之角色（`W-G.9-352R` ⑥ 自解 `1`、`W-G.9-353R` ⑥ 自解 `2`·皆白名單類 `8`）；受詢之六數皆 `0` ⇒ 取號之判⛔ 受影響。零土地後果；零入倉之生產碼。
**根因**：擬表時以前單之表為範本而刪其甲′列，命令未同步刪其引數；表與命令未出自同一次之實跑出艙。
**後果之框**：🟢 零土地後果；🟡 CC 之判讀二批。攔點 ＝ **CC**（二批皆以自解具名）。
**攔法**：既有（`常規七` 款 `二`：三數與塊內文字須出自同一次抽取——表列與命令之引數同源）；`W-G.9-354 §零-1` 之表復列甲′。⛔ 新立款。

---

### 🩸 `自誤 547`　**`W-G.9-353` 工項二 `V-4` 令 `F10 run`、`F11 run` 之出艙與「前置之端（工項一之端）逐字同」，而其前置 `1`〜`5` 未令於工項一之端跑之**

**形**：`docs/orders/W-G.9-353_重量單.md` 工項二之驗 `V-4` 逐字「`F10 run`、`F11 run` 之出艙與前置之端（工項一之端）逐字同」；同工項之前置 `1`〜`5` 僅 `F12` 三子命令、`F8 run` 二退縮與 `run_all`。CC 於施塊 `D1` 前自行加跑二器於工項一之端（`W-G.9-353R` ③-1 末「附（⛔ 單之前置所列·為 `V-4` 之比較而加跑）」）。
**後果之界**：若先施 `D1` 而後察覺，比較之端須另立拋棄式 worktree 重建；本批 CC 於施前捕之 ⇒ 零後果。零土地後果；零入倉之生產碼。
**根因**：驗之比較端未逐一對回其前置之產生步；以「前置之端」一詞指稱而未檢其實有。
**後果之框**：🟢 零土地後果。攔點 ＝ **CC**（施 `D1` 前）。
**攔法**：凡驗以「前置之端」為比較端者，其產生步須列於前置（`W-G.9-354` 工項二之前置列 `F10 run`、`F11 run` 於工項一之端）。⛔ 新立款。
````

## 附錄己　塊 `G4`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-194` 之立（`W-G.9-354`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `928d2920702bc128cc973ddfb3b234d83a4b05bc`（本批開工態·側支 `verify/W-G.9-353-endmerge` 之端）。**取號**（`W-G.9-354 §零-1`）：`GB-194` 於開工態全倉 `0` 命中（錨定框·列框）。

### `GB-194` 🆕　**末端塊之合併再試：一筆土地同時跨占同一街廓二末端塊之 `R_end`、同一末端塊屬二以上之競合、三個以上末端塊之競合 ⇒ 停機（`K-9-50` 射程 ③）**

**受詞**：`app.py` 之 `end_block_merge_run`（字樣錨 `def end_block_merge_run`）之三停機款——甲 一筆土地（同一暫編地號）為二末端塊之未達候選（字樣錨 `同時跨占二以上末端塊之 R_end`）；乙 同一末端塊屬二以上之競合（字樣錨 `屬二以上之競合`·`k6b_stage3_run` 之逐列排程另有同旨之檢）；丙 同一合併群之候選分屬三個以上之末端塊（字樣錨 `三個以上之末端塊`）。另，同一筆土地於各筆單獨試算即為一端之當選者、又為他端所當選或列為他端合併再試之候選者 ⇒ 定案趟之檢（`end_block_assert_head`·字樣錨 `定案趟之鏈首宗`）停機【未證·⛔ 合成案】。
**實測**（發單側窗五十·harness·態 `928d292` ＋ `W-G.9-354` 之生產碼）：本案⛔ 觸發；甲、乙、丙之停機各由量測器 `F13`（`verify/probes/probe_WG9354_endcontest.py selftest`）之 `H2`、`H3`、`H1` 證之。
**與配地之關係**：停機（loud）·⛔ 錯配。
**與既有登記之界**：`K-9-50`（射程 ③·本批入典）；`K-9-24 二`（一片同時跨占同街廓左右兩街角 ⇒ 歸側四分支·街角之裁）——甲之處置是否比照之，⛔ 獲逐字。
**失效條件**：各經 KL 裁（附圖）而修入生產碼；或觸發時逐案呈核而結。
🔒 **排程**：觸發時逐案呈核。
````

## 附錄庚　塊 `P8`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：數末端塊之合併再試相互競合（`K-9-50`）之 harness 路徑入側支（`W-G.9-354`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `928d2920702bc128cc973ddfb3b234d83a4b05bc`（本批開工態·側支 `verify/W-G.9-353-endmerge` 之端）；本批之 `commit` 皆在同一側支（主線⛔ 動）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 數末端塊之合併再試相互競合·harness 路徑（`K-9-50`·KL 裁 `2026-09-28`） | `end_block_merge_run` 以合併群判競合（同一合併群之未達候選分屬二末端塊；同一街廓 ⇒ 題二、分屬二街廓 ⇒ 題一），交 `k6b_stage3_run`（`contests`）：題一 ＝ 先各以本街廓內之土地試 → 只一端需要者整片試；二端皆需要者道路依中心線切半、公設地平分各試 → 再以整片各試（二端皆成 ⇒ 交面積大者 → 暫編地號小者）；未取得之一端之候選連其半能依原位次配地者其半併之，否則連同其半併入已取得之一端（驗「不影響原位次」）；題二 ＝ 二端分別以相連之土地試（先同街廓，再及道路、公設地），皆成 ⇒ 交面積大者 → `p1` 側，土地⛔ 切開；段三之呼叫⛔ 給競合（逐位同本批前） | 🔶（側支·harness 路徑；畫面路徑 ⬜；入主線另候 KL 放行） | `docs/orders/W-G.9-354_重量單.md` |
| `2` | 後處理之承前（`K-9-48` 其二·讀法 `1` ⑤） | 合併群於本段無受併宗之街廓，其依原位次配得之宗照配並承受分往該街廓之土地；道路片全在中心線之一側者不切（段三與末端塊合併再試共用） | 🔶（同上） | 同上 |
| `3` | 末端塊之合併再試（含 `K-9-50`）·畫面路徑 | 畫面入口（段三之畫面入口之後）；須附畫面路徑之合成案（`自誤 517`） | ⬜ | 次單（`W-G.9-355`） |
| `4` | 一筆土地同時跨占同一街廓二末端塊之 `R_end`；同一末端塊屬二以上之競合；三個以上末端塊之競合 | 碼面停機（逐案呈核） | ⬜ | `GB-194`；`K-9-50` 射程 ③ |
| `5` | `K-9-48` 七項 `3`／`5`／`6` | 可拆分者之部分併入（最大面積）；剩餘土地之去處（另一已配地街廓 → `K-9-45`） | ⬜ | 「待落地清單之更新：段三之 harness 路徑入側支；畫面路徑與七項之餘列待辦（`W-G.9-344`）」節序 `3` |
| `6` | 規格步 `3` 候選街廓名單（五級八鍵·`r3` 之消費） | 同 `W-G.9-351` 節序 `3` | ⬜ | 規格步 `3` |
| `7` | 規格步 `4` 同歸戶合併（第一趟）：道路五則、公設地併入 | 同 `W-G.9-351` 節序 `4` | ⬜ | 規格步 `4` |
| `8` | 規格步 `5` 末端塊與中間調配池之進入與落位（`K-9-38`〜`40`） | 前置：`K-9-38` 射程 ④、`K-9-40` 射程 ④ 之附圖另呈；受詞之強制抵費地（末）＝ `W-G.9-353` 節序 `1` | ⬜ | 規格步 `5` |
| `9` | 規格步 `6` ½ 之判與出口（增配／現金補償·裁定 H、I、L、M） | — | ⬜ | 規格步 `6` |
| `10` | 規格步 `7`／`8` 終態與出艙 | — | ⬜ | 規格步 `7`／`8` |

🔒 **前節之更新**：「待落地清單之更新：末端塊之合併再試與強制抵費地（…）之 harness 路徑入側支（`W-G.9-353`）」節序 `3`（數末端塊之合併再試相互競合·「⬜（⛔ 裁·候另呈）」）自本批起 ＝ 已裁（`K-9-50`·KL `2026-09-28`）·harness 路徑 🔶（本表序 `1`）；⛔ 追改前節一字。
🔒 **本批之讀法**（發單側之工程裁·⛔ 域裁·已以【通知】呈 KL）＝ `K-6` 典「`K-9-50` 之立 ＋ 其落地狀態（`W-G.9-354`）」節之「發單側之讀法」`1`〜`8`。
🔒 **本案之量**：態 `928d292` ＋ 本批·harness·退縮 `3.5 m`／`0 m` ⇒ 合併再試無標的（紀錄⛔ 載競合）；配地⛔ 變。合成案之量見 `K-6` 典同節。
🔒 **依賴序**：序 `1`／`2`（本批·側支）→ 序 `3`（`W-G.9-355`·同側支）→ `W-G.9-353`〜`355` 同批入主線（另候 KL 放行）→ 序 `6` → 序 `7` → 序 `8`（其前置之附圖另呈）→ 序 `9` → 序 `10`；序 `4` 觸發時逐案呈核；序 `5` 另單；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級）。
🔒 **本機介面**：主線之生產碼⛔ 變（本批之生產碼只推側支）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `14`（子字串框·含圖例與本列）·列 ＝ `12`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

---

SELF_SHA256: 6186bddd5842f3f86617ae74197028007743109d11675275fd9d679bdd17aa32
