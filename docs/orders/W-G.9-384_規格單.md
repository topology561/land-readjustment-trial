# `W-G.9-384`　規格單：`K-9-71` 之落地（段三後處理之第 `5` 項之輪與手冊先行之 `K-9-51` 之輪：建地之片之候選——本街廓者恆先、他街廓者依五級與深度〔`k971_key5`〕→ 距離 → `k967_rank`；道路、公設地上之片照距離；五級之屬性 ＝ 調配之名單之同一處〔`k971_blk5`·畫面與 harness 之二回呼之 `blk5`·唯於須比時取之〕——段三、末端塊合併再試、手冊先行之關鍵字參數 `blk5`〔畫面三入口與 harness 三入口傳之〕）＋ `W-G.9-383` 之入主線、`K-9-78` 之立（調配之鍵併入 G 值迭代·甲·入典）＋ 自誤 `620` ＋ 審查 #9 之例 ＋ 待落地清單之更新（新側支 `verify/W-G.9-384-k971`）

> **本單建議等級 ＝ `high`**（生產碼 `2` 檔：`app.py` 之二新函式與七函式之改、`verify/selection_pipeline.py` 之四函式之改〔`§三-2`〕；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單側窗八十七·`2026-10-15`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-384-k971`**，其起點 ＝ 主線之端 `fffa397`）。
> **流程 ＝ 規格單**（常態·附則甲〜丙施行）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `Fy34`·CC ⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py`／`verify/selection_pipeline.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `2` 檔；**本案之配地⛔ 變**〔`§一` 項 `5`·`K-9-71` 於本案⛔ 觸〕——其效唯由量測器之合成之例量之）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`（`W-G.9-383` 補令二 工項一）；遠端 heads `43`（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-384-k971`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `Fy34`／`K24`／`E27`／`P37` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`自誤 479`）；Bash 之輸出路徑一律單引號之絕對路徑（`W-G.9-373` 補令二單首）。Bash 命令⛔ 含 heredoc（常設規則索引）。`<O>` ＝ CC 自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列（近例之形·`Co-Authored-By` 等）；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-384_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者照實載於報告。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限**：各驗之命令得並行，唯 `parity`、`k6s3 run`、`F23 run`、`F24 run`、`F27 run`、`F29 run`、`F16 run`、`F14 run`、`F10 run`、`F8 run`、`F9 run`、`F21 run`、`F26 run`、`failclosed`、`F19 mut`、`F22 mut`、`F27 mutate`、`F25 mutate` 之同時並行數 ≤ `2`；逾時者，於⛔ 他負載之下重跑一次，首趟之出艙照實入報告。
> 🔑 **撰碼中之自跑**：CC 撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之頂層節點除 `§三-2` 所列者外之一字（**頂層之新名唯 `k971_key5`、`k971_blk5`**）；`verify/selection_pipeline.py` 除 `§三-2` 所列之四函式外之一字；生產碼 `34` 檔之其餘 `32` 檔（含 `verify/stepg_pipeline.py`、`verify/run_verification.py`）；`adj_block_ctx`、`adj_candidate_lists`、`adj4_plan`、`adj4_pass1_run`、`k929_6_fixpoint`、`k966_block_merge`、`k967_rank`、`k967_pre_area`、`r3_front_road_identifier` 之一字；`§三-3` 之禁改；既有量測器除塊 `Fy34` 所改之 `7` 檔外之一字；`verify/case_params_UC9898.json`、`verify/case_front_road_names_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、`GB` 簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`K-6` 典、自誤簿、`CLAUDE.md` 除塊 `K24`／`E27`／`P37` 之純末端追加外之一字；任何他側支之推送、刪除或改寫；KL 主 checkout；`K-9-78` 之落地（新調配程式之規格單）、`K-9-74`（另單 `W-G.9-385`）、`GB-205`、`K-9-59`〜`K-9-63`、規格步 `5`〜`8`、`GB-196`〜`198`／`202`。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`；`git ls-remote --heads origin` 之列數 ＝ `43`（全 `43` 列存 `<O>\heads_before.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-384-k971`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 619 615` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `604`／`MAX` `619`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `74`／`77`／`[44, 47]`（發單側窗八十七於 `fffa397` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。

### `§零-1`　取號現查（宣告框）

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `fffa397` 之追蹤檔 **`2861`** 檔·列框；發單側窗八十七以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``〕於 `fffa397` 實算）：

| 號 | 裸（錨定）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 620` | `91` | `9` | `1` | `2` | 🟢 可取（平形 `9` 列 ＝ `docs/orders/W-G.9-383_補令二.md` 之 `:12`、`:46`〔補令一 `§一` 裁五之預留之轉述·C 形之 `2` 列即此二列〕＋ 子字串之偶合 `7` 列〔人造之號 `自誤 6205`·`W-G.9-180R` 之報告三列、`W-G.9-183R` 之報告一列、`W-G.9-183` 之 CC 交接文一列、自誤簿 `:4214`、`docs/驗證裁定登記表.md:4226`〕；B 形 `1` 列 ＝ `docs/reports/W-G.9-383R_K-9-75之落地_執行報告.md:103`〔「裁五：自誤 `620` 候鑄·併次單」〕；裸列皆數字之偶合——`sha256`／blob／`commit` 之子字串、行號、量測之值等） |
| `K-9-78` | `0` | — | — | — | 🟢 可取 |
| 對照甲［必非零］`K-9-77` | `89`（`12` 檔） | — | — | — | 🟢 框非恆空 |

**塊名、新名**（母體同上·檔框／列框·`git grep -l`／`git grep -c` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fy34`、`E27`、`P37`（逐名） | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| `K24` | `0`／`0` | `2`／`4` | 🟢 可取（諸列皆量測器之項名〔`F24` 之 `K24` 等〕·⛔ 塊名） |
| 對照甲［必非零］`Fy33` | `2`／`18` | `2`／`22` | 🟢 框非恆空 |
| 對照甲［必非零］`K23` | `4`／`18` | `10`／`36` | 🟢 框非恆空 |
| 對照甲［必非零］`E26` | `3`／`7` | `4`／`17` | 🟢 框非恆空 |
| 對照甲［必非零］`P36` | `1`／`5` | `4`／`16` | 🟢 框非恆空 |
| 報告名 `W-G.9-384R`、新側支之名 `W-G.9-384-k971`、本單名 `W-G.9-384_規格單`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |

自誤 `MAX` ＝ `619`、`K-9` `MAX` ＝ `77`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 620`（塊 `E27`）、`K-9-78`（塊 `K24`）；⛔ 鑄 `GB`、`VR`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `fffa397`，或遠端 heads ≠ `43`、或已含 `refs/heads/verify/W-G.9-384-k971`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy34`／`K24`／`E27`／`P37` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy34` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-384-k971`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之三簿（`K-6` 典、自誤簿、`CLAUDE.md`）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或 CC 認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer（附則丙）之發現涉域上判斷或規格之漏載 |

🔒 **`push` 被拒之預書**（`W-G.9-379R` ①／⑨·`W-G.9-382` 補令二·`W-G.9-383` 補令二）：本單之推皆至**新側支**（⛔ 主線），屬 KL `2026-09-02` 已放行之範圍（`§二`）。若仍為分類器所擋 ⇒ 停機款 `7` 之「被拒」：照實上呈其訊、⛔ 改推之目標、⛔ 以他法繞之；KL 親推之後 CC 續驗（`git ls-remote` 之實得）。

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗八十七自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`·Python `3.13.16`·`numpy 2.4.6`〔`GB-198`〕·`shapely 2.2.0`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`（`W-G.9-383` 補令二 工項一·其父 `8966ed3`、祖 `fa31382`）；遠端 heads **`43`**（`git ls-remote --heads origin` 之列數）；追蹤檔 `2861`（`git ls-tree -r <主線> \| wc -l`）；`app.py` ＝ `f4cb5910b9ebaf52e1030a686a28c162a592ea3f`（`1809341` B）、`verify/selection_pipeline.py` ＝ `cf1d8e41d81ad9e17f1bc3817df58302d8207176`（`59291` B）、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`（`121758` B）、`verify/run_verification.py` ＝ `f5b896e5a702c5d958e3ba27091d27832385efc4`（`103754` B）、`verify/run_all.py` ＝ `e5cf9a224517533b183b34e4fd0f5fbe35ee406b`（`24681` B）；本批所改之 `7` 器之施前 blob ＝ `§五-1` 項 `2`；`K-6` 典 ＝ `d02ae8ff207cd1f3d430664bcab661d12640449a`（`790469` B）、自誤簿 ＝ `7a0e35fe90ec480024def63808d00bd404483df2`（`1194351` B）、`CLAUDE.md` ＝ `98ab90dd491d4e0f40ab0f47b1208c1b7935e5f2`（`404646` B）、`GB` 簿 ＝ `3cb60b424b60b56664734f8696ef8a53537331d6`（`1063208` B·本批⛔ 動）；皆以換行結尾·CR `0`（判別力：`data/V6.dxf` ＝ `12308`） |
| `2` | 受詞（`fffa397`） | ① 段三之輪（`k6b_stage3_run` 之 `_p5_373`）：各片之候選 ＝ 同一地主之已配得之宗（扣片自身、已整筆併出者、⛔ 在當下之態者、該片之已試而未全收之街廓之宗），其序之鍵 ＝ `(_d, k967_rank(…))`（`_d` ＝ `_dist357`·片至該街廓之諸片之聯集·`0.01 m`）——本街廓之候選之距離 ＝ `0`，他街廓之候選之距離亦得為 `0`（唯點相接）而依 `k967_rank` 先於本街廓者；建地與道路、公設地之片同式（⛔ 五級）。② 手冊先行之輪（`k953_manual_run`）：其序之鍵 ＝ `(_dv, 本街廓 0／他 1, 相連 0／否 1, k967_rank(…))`；他街廓之候選唯依距離（⛔ 五級）；`_why951` ＝ `'K-9-51（剩餘土地·距離近者先）'`。③ 五級之屬性唯於第一趟（`adj4_plan` → `adj_block_ctx`／`adj_candidate_lists`）求之；段三、末端塊合併再試、手冊先行之簽名⛔ 受之（關鍵字參數 ＝ `log_print`〔、`contests`〕）；二回呼之回傳之鍵 ＝ `a_prime`、`trial_winner`、`alloc_state`、`alloc_eval`。`git grep -c -F` 於 `app.py`（列框）：「def k971_key5」`0`、「K-9-51（剩餘土地·距離近者先）」`1`、「contests=None)」`1`、「contests=(_ct or None))」`1`、「正面道路無識別符」`1`；於 `verify/selection_pipeline.py`：「blk5=」`0`、「試算中止」`1` |
| `3` | 工項一之端（`fffa397` ＋ 塊 `Fy34`·倉外實跑） | `V-1`〜`V-2` 之 `52` 呼叫中，其受詞（器或其所載之器）於塊 `Fy34` 有改者 `21` 呼叫（`F23`〔`selftest`／`wiring`／`run`〕、`F16`〔`selftest`／`run`〕、`F14`〔`selftest`／`run`〕、`F15 wiring`、`F9`〔`selftest`／`wiring`／`run`〕、`F24`〔`selftest`／`wiring`／`run`〕、`F25`〔`wiring`／`mutate`〕、`F27`〔`selftest`／`wiring`／`mutate`／`run`〕、`F28 selftest`）於工項一之端實跑：`6` 呼叫 ＝ `§四-1` 工項二前置 `1`（`F23 selftest`／`F23 wiring`／`F16 selftest`／`F14 selftest`／`F15 wiring` 之 `rc 1`、`F27 mutate` 之 `rc 3`；其末列逐字皆見該處）；其餘 `15` 呼叫皆 `rc 0`·末列 ＝ 開工態之同器之末列（`F23 run`、`F16 run`、`F14 run`、`F24 run`、`F27 run`、`F9 run` 之 `R` 諸項皆 ✅）；此 `21` 呼叫之 `stderr` 合計 `0` B。其餘 `31` 呼叫之器與其受詞（`app.py`、`verify/` 之他檔、他器）與開工態 `fffa397` 逐位同——⛔ 於本窗重跑；其出艙 ＝ 開工態之出艙（發單側窗八十六於側支之端 `fa31382`〔其 `app.py` 與 `verify/` 之一切檔 ≡ 主線 `fffa397`〕自倉復驗：`52` 呼叫皆 `rc 0`）——CC 之前置 `2` 實跑之 |
| `4` | 原型（發單側窗八十七·倉外·`fffa397` ＋ 塊 `Fy34` ＋ `§三` 之一實作·⛔ 為 CC 之期） | 原型之 `app.py` ＝ `c491636e6b70ed8fd520169af5681936d93159f2`（`1818782` B·對開工態 `+124`／`-10`）、`verify/selection_pipeline.py` ＝ `a9ec6cfacef8c2b92946409f96c2b0c47e1fef7e`（`60194` B·`+14`／`-5`）——⛔ 為期；頂層節點之相異（AST）＝ `{k971_key5, k971_blk5, k6b_stage3_run, end_block_merge_run, k953_manual_run, k6b_screen_callbacks, f3_screen_k6b_stage3, f3_screen_end_block_merge, f3_screen_k953}`／`{_k6b_callbacks, run_corner_pk_k6b, run_end_block_merge, run_k953}`，頂層之新名 ＝ `{k971_key5, k971_blk5}`；`R-9` 之字樣皆合（`V-8` 之期）。`V-1`〜`V-2` 之 `52` 呼叫（同 `§四-1` 之命令）於原型皆 `rc 0`，其末列 ＝ `§五-1` 項 `8` 之施後之列；諸器之 `stderr` 合計 `0` B。`F23 selftest` 之 `K61`〜`K74` 與 `F16 selftest` 之 `K23`〜`K32` 之期值皆發單側手算（各例之註）、原型實得與之逐值同。🔒 撰原型中 `F23 wiring` 之 `W8`／`F24 wiring` 之 `W7` 紅三次（`§三-3` 之 `2` 所列之錨：簽名之 `contests=None)`、末端塊合併再試之 `contests=(_ct or None))`、`k971_key5` 之初稿複製 `adj_candidate_lists` 之 `_r2`／`_r3`／`_r5` 之列；docstring 之「正面道路無識別符」；量測器之新字面「非 dict」於基準恰一見而成錨）——皆改原型或器之字面以避之 |
| `5` | 本案之量（主線之端與原型·harness 與畫面·二退縮） | **主線之端**（`fffa397`·harness `run_corner_pk_k6b`·二退縮 `3.5`／`0`·倉外之小器以 session 之紀錄計之）：段三之紀錄 `19`／`0` 列，其層級「後處理·第5項」之列 `0`／`0`；末端塊合併再試之紀錄 `0`／`0` 列；手冊先行之紀錄 `37`／`46` 列，其序「K-9-51」之列 `0`／`0`（序之集 ＝ 單元、手冊、整批、第31條第3款〔兩側皆配不到〕）；第一趟之紀錄 `1`／`1` 列 ⇒ **`K-9-71` 之四處於本案皆無片入其輪**（`K-9-71` 之所呈之「本案：上述四處有無「距離與五級排出不同結果」的情形」之答 ＝ 無）。**原型**（同器·同命令）：三紀錄與主線之端逐列同（`==`）、五級之屬性之回呼（`ns["k971_blk5"]` 之包裝計之）之呼數 `0`／`0`；`k6s3 cmp` 二退縮皆 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔逐位同（`3.5 m` `8be0160b…`、`0 m` `6fb86647…`·前後同）；`parity` 之落檔與 `stdout` 前後逐位同（發單側之二樹之 `HEAD` 皆 `fffa397`·⛔ 須正規化）、末列皆 `⇒ rc 0（不符 0 項）`——配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`、手冊先行 session 鍵 `f3_k953_log` `37`／`46` 列；`F23 run`、`F16 run`、`F14 run`、`F24 run`、`F27 run`、`F29 run`、`F10 run`、`F21 run`、`F26 run`、`F9 run`、`failclosed` 於原型皆綠 ⇒ **配地⛔ 變**（`V-4`〜`V-6`）。🔒 `R-5` ④ 之依據之字面唯見於手冊先行之 `K-9-51` 之列 ⇒ 本案⛔ 見 |
| `6` | 判別力（發單側窗八十七·倉外·原型之上逐一施一突變） | 二十二種（`F23 selftest`、`F16 selftest`、`F23 wiring` 逐種量之·皆捕）：① 段三之再排去之 ⇒ `F16` `K23`／`K24`／`K25`／`K28`／`K30`〜`K32`；② 手冊先行之再排去之 ⇒ `F23` `K61`／`K62`／`K64`／`K66`／`K67`／`K72`〜`K74`；③ 段三之本街廓⛔ 恆先（與他街廓同依五級排）⇒ `F16` `K24`；④ 手冊先行之他街廓唯一亦取五級之屬性 ⇒ `F23` `K65`／`K67`／`K70`；⑤ 段三之同 ⇒ `F16` `K26`；⑥ 使用分區之級反之 ⇒ `F23` `K61`／`K68`、`F16` `K23`；⑦ 深度⛔ 容差 ⇒ `F23` `K62`／`K68`；⑧ 手冊先行之往大者淘汰（他街廓二以上時濾去之）⇒ `F23` `K42`／`K63`；⑨ 段三之道路、公設地之片亦依五級 ⇒ `F16` `K2`〜`K5`／`K9`／`K10`／`K10′`／`K12`〜`K14`／`K21`／`K27`；⑩ 五級之屬性⛔ 存（每比一次呼一次）⇒ `F23` `K67`；⑪ 審查 #9：單元之取代未成仍寫入宿主之標記 ⇒ `F23` `K60`／`K69`；⑫ 畫面之段三⛔ 傳 `blk5` ⇒ `F23 wiring` `W9`；⑬ harness 之手冊先行⛔ 傳之 ⇒ `W9`；⑭ 畫面之回呼⛔ 以 `adj4_depth_of` 取深度 ⇒ `W9`；⑮ 末端塊合併再試⛔ 傳之予段三 ⇒ `W9`；⑯ 手冊先行之同鍵者依街廓名 ⇒ `F23` `K71`；⑰ 五級唯使用分區 ⇒ `F23` `K62`／`K68`／`K72`／`K73`、`F16` `K30`／`K31`；⑱ 段三之原街廓與候選互易 ⇒ `F16` `K30`；⑲ 五級去正面道路與路寬之三級 ⇒ `F23` `K68`／`K72`／`K73`、`F16` `K30`／`K31`；⑳ 畫面之回呼之道路之名以 label 取 ⇒ `W9`；㉑ 畫面之回呼之最小建築面積以 `{}` 代之 ⇒ `W9`；㉒ 手冊先行⛔ 查回呼之型 ⇒ `F23` `K74`。🔒 ③ 之初稿之突變（本街廓之鍵改 `(1,)`）⛔ 為突變（`(1,)` 仍小於 `(1, …)`）⇒ 改以「本街廓亦依五級」量之；⑧ 之初稿（往大者之鍵改極大）係排名而非淘汰 ⇒ 改以濾去量之。⑯〜㉒ 與 `K70`〜`K74`、`K30`〜`K32` 及 `W9` 之引數之查係另一審查者（唯讀·發單側窗八十七）所揭之補（初版之量測器於 ⑯〜㉒ 之突變皆綠）。`K69` 新舊皆綠（覆蓋之補·`W-G.9-383` 補令一之 `R-12` 已落地） |
| `7` | `run_all` | ⛔ 跑（單首之「級」·`§四-1` 工項二之「⛔ 跑之由」） |

---

## `§二`　KL 之語與射程

🔒 **所據**：`CLAUDE.md` 待落地清單 `W-G.9-383` 之節之序 `7`（`K-9-71`·`W-G.9-384`）；`K-6` 典 `K-9-71` 之節（`W-G.9-380`·其【工】之讀法甲〜丁）與其後諸節之 `K-9-71` 之引（`K-9-73` ⑧、`K-9-75` ①、`W-G.9-381` 之節之二之乙〔「`K-9-71` 之射程 ＝ 後段」〕）；`W-G.9-383` 補令一 `§一` 裁五（`自誤 620`·候鑄·併次單）與其重派之審查之 🟠 #9（覆蓋之缺）；發單側窗八十六之交接文 `§四` 項 `3`（KL 之效率之令：純登記⛔ 單出）；KL 之語（下開）。

🔒 **KL 之語**（逐字）：
- `2026-10-12 16:37`：「是，建地都先依五級排序，道路用地、公設地上的土地則仍只依距離」（⇒ `K-9-71`·全文、所呈與其受詞見 `K-6` 典 `W-G.9-380` 之節之二）。所呈之「本案：上述四處有無「距離與五級排出不同結果」的情形，我在擬單時以原型實跑後回報，不先推測」之答 ＝ `§一` 項 `5`（無·四處皆無片入其輪）。
- `2026-10-15 14:40`：「383 畫面核對無誤，准入主線」（⇒ `W-G.9-383` 補令二·塊 `K24` 之一）。
- `2026-10-15 16:07`：「按鍵要併入 G 值迭代（甲）」（⇒ `K-9-78`·所問與所呈見塊 `K24` 之二）。

🔒 **【工】之讀法**（塊 `K24` 之三·以交付之通知告 KL）：甲 處（二輪之候選之序）；乙 序（建地：本街廓恆先；他街廓：五級與深度 → 距離 → `k967_rank`；道路、公設地：照舊）；丙 五級之屬性（調配之名單之同一處）；丁 何時取之（他街廓之候選二以上始取·其停機照拋·未給 ⇒ 停機）；戊 往大不淘汰；己 紀錄之依據之字面；庚 審查 #9 之例；辛 本案（⛔ 觸）。

🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 之畫面核對與逐字放行**。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支（附則甲〜丙）；`(c)` ⛔ 及主線、他側支、KL 主 checkout、`K-9-78` 之落地、`K-9-74`（`W-G.9-385`）、`GB-205`、`K-9-59`〜`K-9-63`、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**：
- 「**段三之輪**」＝ `k6b_stage3_run` 之巢狀 `_p5_373`（第 `5` 項之輪）之「各片之候選之序」之段（`_seq[x] = _cands` 之前）；「**手冊先行之輪**」＝ `k953_manual_run` 之「④ 剩下（`K-9-51`·`K-9-68`）」之段之 `_seq953[_x] = _list` 之前。
- 「**建地之片**」：段三 ＝ `_kind(x) == 'bld'`；手冊先行 ＝ `_sort953(_tin953[_x]) == 'bld'`（皆既有之判）。「**本街廓**」＝ 片之所屬街廓（段三 ＝ `_blk_of[x]`；手冊先行 ＝ `_blk953[_x]`）；候選之街廓 ＝ 段三 ＝ `_pre` 之該候選之 `_b`；手冊先行 ＝ `_list` 之元之第 `3` 項（`str(_bk)`）。
- 「**五級之屬性**」＝ `adj_block_ctx` 之回傳之形（`{街廓: {'使用分區', '最小建築面積', '正面道路', '正面路寬', '深度'}}`）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | 新頂層 `k971_key5(blk_ctx, home, t, tol=ADJ_DEPTH_TIE_TOL_M)`（純函式·置於 `adj_candidate_lists` 之後、`adj_candidate_rows` 之前） | 回 `(r1, r2, r3, r4, r5, r6)` ＝ `adj_candidate_lists` 之建地軌之八鍵之前六之同式，其原街廓 ＝ `home`、候選街廓 ＝ `t`：最小建築面積之級 ＝ `blk_ctx` 之全部街廓之相異值之升序、正面路寬之級 ＝ 其相異值之降序；`r1` 使用分區同 `0`／異 `1`；`r2` 往小或同級 `(0, n)`、往大 `(1, n)`；`r3` 正面道路同 `0`／異 `1`；`r4` 正面路寬同 `0`／異 `1`；`r5` 往窄或同級 `(0, n)`、往寬 `(1, n)`；`r6` 深度差 `Δ` ＝ 候選 − 原：`|Δ| ≤ tol`（`Decimal(repr(float(tol)))`）⇒ `(0, Decimal('0'))`、`Δ < 0` ⇒ `(0, −Δ)`、否則 `(1, Δ)`（`n`、`Δ` 之型與 `adj_candidate_lists` 同）。`home` 或 `t` 不在 `blk_ctx` ⇒ `RuntimeError`（訊息含「無五級之屬性」）。⛔ 淘汰任何街廓。 |
| `R-2` | 新頂層 `k971_blk5(classified_blocks, eff_min_build_by, front_derive_by, front_name_by, width_by, depth_by)`（純函式·置於 `k971_key5` 之後） | 可建築街廓 ＝ `classified_blocks` 中 `F3_CATEGORY_BURDEN[category] == ADJ_BURDEN_BUILD` 者（原序）；正面道路 ＝ `r3_front_road_identifier(<其 label>, front_derive_by or {}, front_name_by or {})` 之各 `['id']`（**⛔ 佔位**·`ADJ4_IDENT_UNUSED` ⛔ 用）；回 `adj_block_ctx(<label 之列>, {label: category}, eff_min_build_by or {}, {label: id}, {label: (width_by or {}).get(label)}, depth_by or {})`——與 `adj4_plan` 之街廓屬性之同式（唯佔位之異）。所呼之函式之停機照拋。 |
| `R-3` | `k6b_stage3_run`（段三之輪） | ① 簽名之關鍵字參數改為 `*, log_print=print, blk5=None, contests=None`（`blk5` 置於 `contests` 之前·`§三-3` 之 `2`）。② 函式內（`_p5_373` 之外·其前）立「五級之屬性之取」：首次須比時，`blk5 is None` ⇒ `RuntimeError`（訊息含「未給五級之屬性」）；否則呼 `blk5()` 一次，其回傳非 `dict` ⇒ `RuntimeError`（訊息含「非 dict」）；存之，其後同一次之 `k6b_stage3_run` 之內皆用之（⛔ 再呼）；其鍵 ＝ `k971_key5(<所存>, <本街廓>, <候選之街廓>)`。③ 段三之輪：既有之 `_cands.sort(key=lambda c_: c_[0])` 之後，建地之片且 `_cands` 非空 ⇒ 以穩定之排序再排之，其鍵 ＝ 候選之街廓 ＝ 本街廓 ⇒ `(0,)`；否則 ⇒ 他街廓之候選之相異街廓數 ≥ `2` 時 `(1, <五級之鍵>)`、`< 2` 時 `(1,)`（**唯數 ≥ `2` 時取五級之屬性**·其數 ＝ 他街廓之**相異街廓**之數，⛔ 候選之數）；鍵⛔ 增他元（街廓名等·同鍵者依既有之序）。道路、公設地之片⛔ 再排。他一切（`_pre` 之濾、`G` 之查、距離、輪、紀錄）⛔ 變。 |
| `R-4` | `end_block_merge_run` | 簽名之關鍵字參數增 `blk5=None`（`log_print` 之後）；其呼 `k6b_stage3_run` 之處增 `blk5=blk5`，**以獨立之一列置於既有之 `contests=(_ct or None))` 之列之前**（該列之字面⛔ 動·`§三-3` 之 `2`）。 |
| `R-5` | `k953_manual_run`（手冊先行之輪） | ① 簽名之關鍵字參數改為 `*, log_print=print, blk5=None`。② 「五級之屬性之取」同 `R-3` ②（訊息冠 `_hdr953`·含「未給五級之屬性」／「非 dict」）。③ 手冊先行之輪：既有之 `_list.sort(key=lambda _t: _t[0])` 之後，建地之片且 `_list` 非空 ⇒ 以穩定之排序再排之，其鍵同 `R-3` ③（本街廓 ⇒ `(0,)`；他街廓 ⇒ 其相異街廓數 ≥ `2` 時 `(1, <五級之鍵>)`、否則 `(1,)`）。④ `_why951` 之值改為 `'K-9-51／K-9-71（剩餘土地·本街廓先·建地之他街廓依五級 → 距離）'`（他處⛔ 改）。他一切⛔ 變。 |
| `R-6` | 二回呼（畫面 `k6b_screen_callbacks`、harness `_k6b_callbacks`） | 各增巢狀（函式之本體之頂層）`def blk5():`，回 `dict` 增鍵 `'blk5': blk5`（他鍵⛔ 變）。畫面：`k971_blk5(g_kwargs['classified_blocks'], st.session_state.get(K91_SS_MBA_EFFECTIVE, {}) or {}, …get(SS_FRONT_ROAD_DERIVE, {}) or {}, {cb['label']: <SS_FRONT_ROAD_NAME 之 dict>.get(cb.get('id'), '') for cb in g_kwargs['classified_blocks']}, {cr['街廓']: cr.get('正面路寬(m)') for cr in pk_kwargs['_corner_rows_init']}, adj4_depth_of(st.session_state))`（同 `f3_screen_adj4` 之 `adj4_plan` 之引數之源）；harness：`ns["k971_blk5"](cb, {}, cad.get("front_road_derive") or {}, run_verification.load_front_road_names(), {r["街廓"]: r.get("正面路寬(m)") for r in param_rows}, ns["adj4_depth_of"](fake_st.session_state))`（同 `run_adj4`）。皆於**呼叫時**取之（⛔ 預取）；其內恰一處呼 `k971_blk5`，以六個位置引數依上列之序傳之（`F23 wiring` 之 `W9` 逐引數查其源之字樣）。 |
| `R-7` | 六入口 | 各以關鍵字參數 `blk5=` 傳之（`F23 wiring` 之 `W9` 以其式之 `ast.unparse` 逐字比之）：畫面 `f3_screen_k6b_stage3` 之 `k6b_stage3_run` ⇒ `blk5=_cb['blk5']`；`f3_screen_end_block_merge` 之 `end_block_merge_run` ⇒ `blk5=_cb['blk5']`；`f3_screen_k953` 之 `k953_manual_run` ⇒ `blk5=_b5953s`，其 `_b5953s` 以**新增之一列** `_b5953s = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)['blk5']` 定之（既有之 `_a953s` 之列⛔ 改）；harness `run_corner_pk_k6b` 之 `k6b_stage3_run` ⇒ `blk5=_cbk['blk5']`；`run_end_block_merge` 之 `end_block_merge_run` ⇒ `blk5=callbacks['blk5']`；`run_k953` 之 `k953_manual_run` ⇒ `blk5=callbacks['blk5']`。皆附於該呼叫之末之關鍵字（`F24 wiring` 之 `W6` 以「去其末之 `, blk5=…)`」比之）。 |
| `R-8` | docstring 與註 | `k6b_stage3_run`、`end_block_merge_run`、`k953_manual_run`、`k6b_screen_callbacks` 與 `verify/selection_pipeline.py` 之 `_k6b_callbacks` 之 docstring 之末各增一款（以 ``🔧 `W-G.9-384` `` 起首·得多列）述 `R-3`〜`R-6`（段三與手冊先行之款明載上文「距離 → `k967_rank`」〔段三〕／「距離 → 本街廓者先」〔手冊先行〕於建地之片之他街廓之候選不再適用）；`R-1`〜`R-7` 之改處得各以一註述之（同起首）。🔒 新書之 docstring、註與停機之訊息⛔ 含 `§三-3` 之 `2` 所列之字樣、⛔ 重寫既有之字樣；他處之 docstring 與註⛔ 改。 |
| `R-9` | 字樣（列框·`git grep -c -F … -- <檔>`） | 施後：`app.py` 之「def k971_key5」「def k971_blk5」各恰 `1`；「未給五級之屬性」恰 `2`（`R-3`／`R-5` 之訊息·docstring 與註⛔ 書之）；「K-9-51（剩餘土地·距離近者先）」`0`；「contests=None)」「contests=(_ct or None))」「正面道路無識別符」各恰 `1`（同施前）；`verify/selection_pipeline.py` 之「blk5=callbacks['blk5']」恰 `2`、「blk5=_cbk['blk5']」恰 `1`、「試算中止」恰 `1`（同施前）。 |
| `R-10` | 本案 | 二退縮之配地、街角得標與強制旗標、段三／末端塊合併再試／手冊先行／第一趟之紀錄、入池閘之紀錄、調配之輸入、畫面與 harness 之對拍之結果皆⛔ 變（`K-9-71` 於本案⛔ 觸·`§一` 項 `5`）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F23`（`probe_WG9363_k953.py`）：`K61`〜`K67`、`K70`〜`K74`（手冊先行之輪·`R-5`）、`K68`（`R-1` ＝ `adj_candidate_lists` 之鍵之前六）、`K69`（審查 #9·⛔ 涉本單之碼·新舊皆綠）；玩具之 `_go` 之 `b5`、`_fn384`（受測函式受 `blk5` 時補「皆同」）；`wiring` 之 `W1`（`k953_manual_run` 之關鍵字參數 ＝ `log_print`、`blk5`）、`W6`／`W7`（許）、`W9`（`R-3`〜`R-7` 之接線與二新函式之⛔ 案件字面）。
- `F16`（`probe_WG9357_k948.py`）：`K23`〜`K32`（段三之輪·`R-3`）；段三之呼叫經 `_s3384`（受測函式受 `blk5` 時補「皆同」）。
- `F14`（`probe_WG9355_screenmerge.py`）：段三與末端塊合併再試之樁之簽名增 `blk5`；`T6a` 之期增 `'blk5'`。`F15`（`probe_WG9356_screenmerge_wiring.py`）`W3` 之回鍵之期增 `blk5`。`F9`（`probe_WG9350_frontroad.py`）`W4` 之許增 `k971_blk5`、`k6b_screen_callbacks`、`_k6b_callbacks`。`F24`（`probe_WG9367_adj4.py`）`W5` 之許、`W6` 之「去其末之 `, blk5=…)`」。`F25`（`probe_WG9370_adj4mut.py`）`X2` 之許、`X4` 之除外。
- `app.py` 之頂層節點對 `fffa397` 相異者 ⊆ `{k971_key5, k971_blk5, k6b_stage3_run, end_block_merge_run, k953_manual_run, k6b_screen_callbacks, f3_screen_k6b_stage3, f3_screen_end_block_merge, f3_screen_k953}`，**頂層之新名唯 `k971_key5`、`k971_blk5`**；`verify/selection_pipeline.py` 之頂層節點相異者 ⊆ `{_k6b_callbacks, run_corner_pk_k6b, run_end_block_merge, run_k953}`；`verify/` 之他生產碼⛔ 改。

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **突變之錨**（`F27 mutate`·`MUT377` 之 `N01`〜`N57`；`F25 mutate`；`F19 mut`；`F22 mut`）：其錨（`app.py` 之字樣·各須於其函式之區間恰一見）**一字⛔ 動、⛔ 重寫**——段三之輪與手冊先行之輪之既有之碼（含 `_cands.append(((_d, k967_rank(…` 之列、`_cands.sort(key=lambda c_: c_[0])`、`_list.append(((_dv, …`、`_list.sort(key=lambda _t: _t[0])`）、`_rnd953`、`_try953k`、`_seq953`、趟末之帳、`adj_candidate_lists` 之八鍵之式（`_r2 = …`、`_r3 = 0 if …`、`_r5 = …` 等）皆屬之；`R-3`／`R-5` 之再排**附於其後**、`R-1` 之式**⛔ 複製**其列之字面（另以他名書之）。`F27 mutate` 之期：`57` 種皆捕、`無從判定 []`；`F19 mut`、`F22 mut`、`F25 mutate` 之期 ＝ `§五-1` 項 `8`。
2. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計·含引號）。發單側之原型所遇者（皆須避之）：`'contests=None)'`（⇒ `R-3` ① 之序）、`'contests=(_ct or None))'` 與其前綴之空白（⇒ `R-4` 之獨立之列）、`'正面道路無識別符'`（⇒ 新書之 docstring 與訊息⛔ 書之）、`adj_candidate_lists` 之 `'_r2 = (0, _i2 - _j2) if _j2 <= _i2 else (1, _j2 - _i2)'`／`'_r3 = 0'`／`"_r3 = 0 if _c['正面道路'] == _s['正面道路'] else 1"`／`'_r5 = (0, _j5 - _i5) if _j5 >= _i5 else (1, _i5 - _j5)'`（⇒ `R-1` 以他名、他式書之）。CC 撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
3. **頂層之名之許**（`F23 wiring` 之 `W7`、`F24 wiring` 之 `W5`、`F25 wiring` 之 `X2`）：塊 `Fy34` 所增之許 ＝ `§三-2` 之集 ⇒ **頂層之新名唯二**。
4. `F17 wiring`、`F25 wiring` 之 `X3`／`X5`、`F10 wiring` 之 `W4`、`F27 wiring` 之 `Y1`〜`Y9`、`F29 wiring` 之 `Y1`〜`Y11`、`F14`／`F15`／`F9` 之接線之項⛔ 觸（`F14` 之樁唯受 `blk5`、⛔ 呼之）。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`K-9-71` 已裁（`K-6` 典 `W-G.9-380` 之節）；其落地之讀法 ＝ 塊 `K24` 之三（【工】·以交付之通知告 KL）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地或諸紀錄有任一改變；建地之片之判、本街廓之判於二輪之間不一致而 `§三` 之用語無從定之。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-9`）：落於何處、其字樣；對 `§三-3` 各款之自查；附則乙之自查（`R-1` 之式與 `adj_candidate_lists` 之八鍵之前六之同〔`F23` `K68` 之實得〕、`R-3`／`R-5` 之再排之置處〔既有之排序之後〕與其鍵之三支、五級之屬性之取之一次與二停機、`R-4` 之獨立之列、`R-6` 之二回呼之引數之源與 `f3_screen_adj4`／`run_adj4` 之同、`R-7` 之六處之式）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/selection_pipeline.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-384-k971`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-384_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-384 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-384-k971`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`44`**、主線仍 ＝ `fffa397…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-384-k971`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy34` 抽為 `<O>\Fy34.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`7` 檔之 `git hash-object` ＝ `§五-1` 項 `5`；`git diff --numstat` 唯此 `7` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-384 工項一：量測器之期之更新（F23 之 K61〜K74 與 W1／W9；F16 之 K23〜K32；F14、F15、F9、F24、F25 之許與期）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-384-k971`。

**工項二　生產碼**（🔴 `app.py`、`verify/selection_pipeline.py`·CC 依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`）：
1. 紅（末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`probe_WG9363_k953.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K61', 'K62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68', 'K70', 'K72', 'K73', 'K74']；rc 1`（`K69`、`K71` 綠·防護之例）；`… wiring <repo> 7d8e954` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['W1', 'W9']；rc 1`；`probe_WG9357_k948.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K23', 'K24', 'K25', 'K26', 'K27', 'K28', 'K29', 'K30', 'K31', 'K32']；rc 1`；`probe_WG9355_screenmerge.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['T6a']；rc 1`；`probe_WG9356_screenmerge_wiring.py wiring <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['W3']；rc 1`；`probe_WG9373_k966.py mutate <repo>` ⇒ **`rc 3`**·末列逐字 `⇒ 突變 57（另基準一）；紅 []；無從判定 ['N00']；rc 3`（其 `N00`〔基準·⛔ 突變〕之紅 ＝ `F16` 之 `K23`〜`K32` 與 `F23` 之 `K61`〜`K68`、`K70`、`K72`〜`K74`——此器之子程序載 `F16`／`F23` 之例，其新期於開工態之 `app.py` 本紅 ⇒ 基準⛔ 綠 ⇒ 諸突變無從判定；工項二之後 `N00` 綠 ⇒ `rc 0`）。🔒 `probe_WG9373p1_partrem.py selftest <repo>`（亦載 `F16`／`F23`）於工項一之端 **`rc 0`**（`P0` `29／29`·末列 `⇒ 紅 []；rc 0`）——屬前置 `2`。
2. 綠（**`rc 0`**·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`V-1`／`V-2` 之其餘之呼叫（同 `§四-1` 之驗之命令）。
3. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`；`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_pre_35.json`；同 `0.0` ⇒ `<O>\f8_pre_00.json`；`python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_pre.json`；同 `0.0` ⇒ `<O>\parity00_pre.json`（皆 `rc 0`）。
4. `git grep -c -F "def k971_key5" -- app.py` ⇒ 無出艙、`rc 1`；`git grep -c -F "K-9-51（剩餘土地·距離近者先）" -- app.py` ⇒ 出艙恰一列 `app.py:1`；`git grep -c -F "blk5=callbacks['blk5']" -- verify/selection_pipeline.py` ⇒ 無出艙、`rc 1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫 `app.py`、`verify/selection_pipeline.py` 之改動；`python -m py_compile app.py verify/selection_pipeline.py`；`commit` 訊息之首列逐字 `W-G.9-384 工項二：K-9-71 之落地（段三後處理之第 5 項之輪與手冊先行之 K-9-51 之輪：建地之片之候選依本街廓 → 五級與深度 → 距離；五級之屬性 ＝ 調配之名單之同一處·blk5 與六入口）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>\*_post.*`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy34` 所改之器（快）：`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python verify/probes/probe_WG9357_k948.py selftest <repo>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>`；`python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>`；`python verify/probes/probe_WG9350_frontroad.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9367_adj4.py selftest <repo>`；`… wiring <repo> d7a5ea4`；`python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 74／74`；`F16 selftest` 之 `P0 逐項擾動恰該項紅 35／35`；`F23 wiring` 之 `W1`〜`W9` 皆 ✅ |
| `V-2` | 其餘之 `42` 呼叫（同 `W-G.9-383` 規格單 `§四-1` 之 `V-1`〜`V-3` 之命令·其中上列者除外）：`F29`（`probe_WG9375_k965.py selftest`／`wiring`／`run`）、`F23 run`、`F24 run`、`F25 mutate`、`F27`（`probe_WG9373_k966.py selftest`／`wiring`／`mutate`／`run`）、`F28`（`probe_WG9373p1_partrem.py selftest`）、`F14 run`、`F17 wiring`、`F8`（`selftest`／`wiring`）、`F4 wiring`、`F9 run`、`F10`（`selftest`／`wiring`／`run`）、`probe_WG9352_endblock.py`／`probe_WG9353_endmerge.py`／`probe_WG9354_endcontest.py` 之 `selftest`／`wiring`、`F16 run`、`F18`（`selftest`／`wiring`）、`F19 mut`、`F21`（`selftest`／`wiring`／`run`）、`F22 mut`、`F26`（`selftest`／`run`）、`probe_WG9344_k6s3.py selftest`、`probe_WG9344p1_pooltemp.py selftest`、`probe_WG9348_harvest_key.py`、`probe_WG9341_synth.py`、`probe_WG9340_main_synth.py`、`probe_WG9346_failclosed.py run <repo> 3.5` | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列（`F27 mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`） |
| `V-3` | `V-1`〜`V-2` 之 `52` 呼叫之器之載入 | 本批所改之器 `7` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`… cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**·`R-10`） |
| `V-5` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置 `3` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（CC 以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異）；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0` |
| `V-6` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_post_35.json`；同 `0.0` ⇒ `<O>\f8_post_00.json`；`git hash-object <O>\f8_pre_35.json <O>\f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；其增／刪之數與其 blob 出艙（發單側復驗時自倉重算·⛔ 預載）；`verify/` 之他檔對工項一之端相異 `0`；`app.py` 之頂層節點之名之集 ＝ 工項一之端之集 ∪ `{k971_key5, k971_blk5}`（AST）、`verify/selection_pipeline.py` 之集⛔ 變 |
| `V-8` | `R-9` 之字樣（`git grep -c -F "<字樣>" -- <檔>`·逐一） | `app.py`：「def k971_key5」「def k971_blk5」⇒ 各 `app.py:1`；「未給五級之屬性」⇒ `app.py:2`；「K-9-51（剩餘土地·距離近者先）」⇒ **無出艙**、`rc 1`；「contests=None)」「contests=(_ct or None))」「正面道路無識別符」⇒ 各 `app.py:1`；`verify/selection_pipeline.py`：「blk5=callbacks['blk5']」⇒ `verify/selection_pipeline.py:2`、「blk5=_cbk['blk5']」⇒ `verify/selection_pipeline.py:1`、「試算中止」⇒ `verify/selection_pipeline.py:1`（判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞於本案之配地⛔ 觸（`§一` 項 `5`），其「⛔ 變」由 `V-4`〜`V-6` 與 `F23 run`／`F24 run`／`F27 run`／`F29 run`／`F16 run`／`F14 run` 直接量之；`run_all` 之相異項亦唯可由配地之變而生。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：`R-1` 之式與 `adj_candidate_lists` 之八鍵之前六之同（含往大／往寬之 `(1, n)`、深度之容差與其型）與停機；`R-2` 與 `adj4_plan` 之街廓屬性之同（唯佔位之異）；`R-3`／`R-5` 之再排之置處、穩定、其鍵之三支（本街廓 `(0,)`·他街廓二以上 `(1, 五級)`·他街廓唯一 `(1,)`）、建地之判、五級之屬性之取之一次與二停機；`R-4` 之獨立之列；`R-6` 之二回呼之引數之源（與 `f3_screen_adj4`／`run_adj4` 逐一對照）、呼叫時取之；`R-7` 之六處；`R-8` 之 docstring 之「不再適用」之款；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-384-k971`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K24` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `E27` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P37` 附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；三檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P37` 附後：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-384 工項三：W-G.9-383 之入主線·K-9-78 之立·K-9-71 之落地之讀法入典 ＋ 自誤 620 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-384-k971`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-384R_K-9-71之落地_執行報告.md` ＋ 同目錄之 `W-G.9-384R_K-9-71之落地_app差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之十呼叫之全文、`V-2` 之 `F27 mutate`／`F25 mutate` 之全文、`V-5` 之正規化之比與其對照、`V-6` 之 `hash-object` 之出艙、`F23 run`／`F16 run`／`F29 run` 之末十四列、`k6s3 cmp` 之全文、`parity` 之末十五列、`52` 呼叫之 `rc`／`stderr`／耗時／末列之表）；④ 塊之實得（bytes／`sha256`）與三簿之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **`app.py`／`verify/selection_pipeline.py` 之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-384 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-384-k971`。

### `§四-2`　次單（⛔ 本單之期）

發單側復驗本批之碼（自倉重跑 `V-1`〜`V-9`）後：**入主線之請示**（本批·生產碼·配地⛔ 變）·附 KL 於畫面之核對（新側支之端之 `app.py` 於退縮 `3.5 m`／`0 m`〔各以全新視窗·先 `3.5 m`〕按「🧮 執行 G 值迭代計算」：其所見 ＝ 主線之端之同按·配地與諸紀錄⛔ 變）＋ 主 checkout 之同步（塊 `P37` 之依賴序）；其後 `K-9-74`（`W-G.9-385`·前置 `K-9-62` 之抵充地之欄）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9350_frontroad.py` `5`／`0`、`probe_WG9355_screenmerge.py` `8`／`3`、`probe_WG9356_screenmerge_wiring.py` `5`／`1`、`probe_WG9357_k948.py` `141`／`3`、`probe_WG9363_k953.py` `221`／`4`、`probe_WG9367_adj4.py` `9`／`1`、`probe_WG9370_adj4mut.py` `6`／`0`（唯此 `7` 檔）（增／刪）；工項二 ＝ `app.py`、`verify/selection_pipeline.py`（唯此二檔·其數出艙）；工項三 ＝ `K-6` 典 `74`／`0`、自誤簿 `13`／`0`、`CLAUDE.md` `25`／`0`（唯此三檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `fffa397` | 生產碼相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；`verify/` 之一切檔相異恰 **`8`**（`M`：`verify/selection_pipeline.py` 與塊所改之 `7` 器）；本批之新檔（本單、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`15` 檔：本單、`7` 器、`app.py`、`verify/selection_pipeline.py`、`K-6` 典、自誤簿、`CLAUDE.md`、報告二檔） |
| `4` | 三簿之 bytes | `K-6` 典 `790469` → **`801055`**；自誤簿 `1194351` → **`1196778`**；`CLAUDE.md` `404646` → **`408690`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊 |
| `5` | 自限 | 遠端 heads **`44`**；主線 ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`（⛔ 變）；`verify/W-G.9-384-k971` ＝ 工項四之 `commit`，其祖含 `fffa397`；其餘 `43` 列逐列 ＝ `<O>\heads_before.txt` |
| `6` | `python verify/probes/probe_WG9270_closegate.py 620 619 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 621 620 .` ⇒ `rc 7` |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 620 619` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`605`**／`MAX` **`620`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` **`75`**／**`78`**／`[44, 47]`（自誤唯增 `620`；`K-9` 唯增 `78`；餘 ＝ 開工態） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `Fy34` | `46859` B·`sha256` `81f226d08f34062f06b13002c217897fb23c6f92e0e0aca257f8984035edc914`·`657` 列（圍欄內全文·末附換行）；抽為 `<O>\Fy34.diff`，`git apply` 於 `verify/probes/` 之 `7` 器，其施前 blob（B）：`probe_WG9350_frontroad.py` `20580605bcbde90316bc7780f5e2575a2b2015d9`（`25272`）、`probe_WG9355_screenmerge.py` `413978d7f020919d584079efe6b1637b1b9d6c6f`（`37500`）、`probe_WG9356_screenmerge_wiring.py` `c489e887300d29b90c14791024bc215709390749`（`30405`）、`probe_WG9357_k948.py` `5efb835eafe0ab340846e01759493595d31e8709`（`41687`）、`probe_WG9363_k953.py` `083e8a0b2ecf275a7fad2992ddd60769fbedcef1`（`108036`）、`probe_WG9367_adj4.py` `903249f3556872047dff96a750b54fb2e9b53842`（`71535`）、`probe_WG9370_adj4mut.py` `b6a65f265cb44a9556ceadcb1e9b240661f6c036`（`19070`） |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K24`／`E27`／`P37` | 塊 `K24` `10586` B·`sha256` `4877110c41cef76e73c7383b4b63e4d991ff5bd6edb9f8cdbe7afb67af1d5939`·`74` 列；塊 `E27` `2427` B·`sha256` `fdb529d57d1fb06c2bdc51111b98a53f63278472e79910099dcfd330b18b0ba0`·`13` 列；塊 `P37` `4044` B·`sha256` `2ef301c41dc215f1830ede09320fb1fb4a2850cf2a6273a1d26fa7308037928f`·`25` 列（皆圍欄內全文·末附換行·首列為空列；`P37` 之 payload 內 `⬜` 之子字串框 `10`·列框 `8`〔塊之自載〕）；附於 `K-6` 典（`790469` B）、自誤簿（`1194351` B）、`CLAUDE.md`（`404646` B）之末，期末 ＝ `801055`／`1196778`／`408690` B |
| `5` | 寫出後之 blob | 工項一之 `7` 器（`verify/probes/`·B）：`probe_WG9350_frontroad.py` ＝ `5689c92ed891c95b09f5450ad3c443383b4f6ce1`（`25956`）、`probe_WG9355_screenmerge.py` ＝ `776cddce3b0ec99468ce1a6c33cc71deb5241d57`（`38127`）、`probe_WG9356_screenmerge_wiring.py` ＝ `f38120402ece474a69dcbdfdc726a2d14347a4a2`（`30819`）、`probe_WG9357_k948.py` ＝ `e5a867a2eede82090e5889842d450a026481e139`（`50175`）、`probe_WG9363_k953.py` ＝ `abe2f7fabe818bda5b71ef41a8b59aa3335be85b`（`125317`）、`probe_WG9367_adj4.py` ＝ `2992e4ff721e642b913bd86416177daad6ae2271`（`72408`）、`probe_WG9370_adj4mut.py` ＝ `396bdcf6368be58119e812ba2885d6c3ab56bde7`（`19733`）；工項三之三簿：`K-6` 典 ＝ `78a4892a810b81d516ea176f3dfb85b38de47775`（`801055` B）、自誤簿 ＝ `3f06cffaccc5db2a1be036bd2815941c91e920ed`（`1196778` B）、`CLAUDE.md` ＝ `d1b1a1f2a6ee56fcdb7c9f65fd288be38b73e86c`（`408690` B）。🔒 `app.py`、`verify/selection_pipeline.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-383 §五-1` 項 `7`） |
| `8` | 量測器之二態（發單側窗八十七實跑·倉外） | **工項一之端**（`fffa397` ＋ 塊 `Fy34`）：見 `§一` 項 `3`（其 `6` 呼叫之末列 ＝ 前置 `1`；他 `15` 呼叫 ＝ `⇒ 紅 []；rc 0`·`F25 mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`）。**施後**（原型）：`52` 呼叫皆 `rc 0`，末列逐字皆 `⇒ 紅 []；rc 0`，唯：`probe_WG9373_k966.py mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`probe_WG9370_adj4mut.py mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`；`probe_WG9345_screen.py wiring` ＝ `⇒ rc 0（不符 0·器紅 0）`；`probe_WG9344_k6s3.py selftest` ＝ `selftest 9/9 ⇒ ✅`；`probe_WG9344p1_pooltemp.py selftest` ＝ `selftest 13/13 ⇒ ✅`；`probe_WG9341_synth.py` ＝ `ε ＝ 0.0002｜rc 0`；`probe_WG9340_main_synth.py` ＝ `紅項 [] 器紅 0`。`P0`：`F23` `74／74`、`F16` `35／35`、`F29` `74／74`、`F27` `31／31`、`F28` `29／29`、`F24` `28／28`、`F14` `86／86`；`F23 wiring` `W1`〜`W9` ✅、`F29 wiring` `Y1`〜`Y11` ✅、`F27 wiring` `Y1`〜`Y9` ✅。諸呼叫（含 `k6s3 run`／`F8 run`／`parity` 之二態十二呼叫）之 `stderr` 合計 `0` B；`52` 呼叫之耗時之和 ≈ `10023` s（本機 `2` 核·並行 `2`）。🔒 本表之施後：`F23`、`F16` 之 `selftest`／`run`、`F23`／`F24` 之 `wiring`、`F27` 之四模式、`F28 selftest` 以定稿之器重跑（另一審查者所揭之補〔`K70`〜`K74`、`K30`〜`K32`、`W9` 之引數〕與二字面之改〔「五級之屬性非 dict」〕之後）；他器於其間⛔ 改 |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗八十七實跑（態 `fffa397`）：🔴 機械 `0` 項／🟡 提示 `6` 項——`P-4` `:79`（`§一` 之表頭·其箭頭係推論〔⇒〕與工項一之端至施後之序，表內自載 ⇒ **具名豁免**）、`:117`（`§三-1` 之表頭·其箭頭係候選之序〔本街廓 → 五級 → 距離〕之述 ⇒ **具名豁免**）、`:172`（工項二之「施」·其箭頭係 `commit` 訊息之首列之逐字〔候選之序〕⇒ **具名豁免**）、`:209`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 改前至改後〔閘 `4`〕⇒ **具名豁免**）、`:520`、`:771`（塊 `Fy34` 之碼·逐字之塊 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `22870`–`30590`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單側·本機 Linux·⛔ `push`） | `git worktree add --detach <S> fffa397`（拋棄式）＋ 本單之定稿（`1040` 列·其四塊即附錄甲〜丁）＋ 原型之 `app.py`／`verify/selection_pipeline.py`（代工項二）＋ 報告之替身·五 `commit`（工項零之首列 ＝ 所令逐字；工項一〜四以模擬之首列代之·其後空一列附尾列）：工項零之 blob ＝ 來源；四塊之抽取 ＝ 項 `2`／`4`；`git apply --check` `rc 0`；`7` 器之施後 blob ＝ 項 `5`；工項二 ＝ `app.py` `124`／`10`、`verify/selection_pipeline.py` `14`／`5`；三簿之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx`／`gen_fa_index` ＝ 期·逐位同；閘 `1` ＝ 工項零 `1040`／`0`、工項一 ＝ 該閘之期、工項二 ＝ 上開、工項三 ＝ 該閘之期、工項四（替身）二檔各 `1`／`0`；閘 `2` ＝ 生產碼相異 `2`、`verify/` 相異 `8`（皆 `M`）·新檔三之 `git check-ignore -v --no-index` 無命中（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `15` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `6` `rc 0`（判別力 `621 620` ⇒ `rc 7`）；閘 `7` `rc 0`（自誤 `605`／`620`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `75`／`78`·缺號 ＝ 該閘之期）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `4`／`5` 之實跑逐位同（`7` 器 ＝ 項 `5`、`app.py`／`verify/selection_pipeline.py` ＝ 原型） |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丁` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-384-k971`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `Fy34`（`git apply` 之差異·`verify/probes/` 之 `7` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9350_frontroad.py b/verify/probes/probe_WG9350_frontroad.py
index 2058060..5689c92 100644
--- a/verify/probes/probe_WG9350_frontroad.py
+++ b/verify/probes/probe_WG9350_frontroad.py
@@ -19,6 +19,8 @@
              R1 可建築街廓皆有推導；R2 狀態與比值一致（入推導集 ⇔ 比值 > 具名常數）；
              R3 線長之自我驗證閘（＝ `front_lines` 之 `length`·`LineString.length`）；
              R4 外部錨：以 shapely 之 `line ∩ polygon.buffer(1.0)` 另算比值，逐一分類（> 具名常數與否）與 R2 相同。
+  🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：W4 之許另含 app.py 之 `k971_blk5`／`k6b_screen_callbacks` 與 harness 之
+           `_k6b_callbacks`（手冊先行與段三之依距離併入之五級讀正面道路·街廓屬性）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, json, math, os, re, sys
@@ -259,9 +261,12 @@ def _wiring_checks(app_src, others):
     tok_re = re.compile("|".join(re.escape(t) for t in toks))
     # 🔧 `W-G.9-367`（發單側窗六十八）：harness 之 `run_adj4`（規格步 4 乙之 harness 入口）許可——除其原文而後計他檔之命中
     others = {p: (_drop_fn367(s, "run_adj4") if p == "verify/selection_pipeline.py" else s) for p, s in others.items()}
+    # 🔧 `W-G.9-384`（`K-9-71`）：harness 之 `_k6b_callbacks`（其 `blk5` 讀正面道路〔五級之街廓屬性〕）許可——除其原文
+    others = {p: (_drop_fn367(s, "_k6b_callbacks") if p == "verify/selection_pipeline.py" else s) for p, s in others.items()}
     other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
     allowed = set(R3_FUNCS) | {"parse_cad_precision_layers", "main"}
     allowed |= {"f3_screen_adj4", "adj4_plan"}   # 🔧 `W-G.9-367`（發單側窗六十八）：規格步 4 乙之畫面入口與受詞之純函式讀正面道路（名單之街廓屬性）
+    allowed |= {"k971_blk5", "k6b_screen_callbacks"}   # 🔧 `W-G.9-384`（`K-9-71`）：五級之街廓屬性之純函式與畫面之回呼（`blk5`）
     bad = []
     for fname, node in top.items():
         if fname in allowed:
diff --git a/verify/probes/probe_WG9355_screenmerge.py b/verify/probes/probe_WG9355_screenmerge.py
index 413978d..776cddc 100644
--- a/verify/probes/probe_WG9355_screenmerge.py
+++ b/verify/probes/probe_WG9355_screenmerge.py
@@ -26,6 +26,8 @@
            無之 ⇒ 試算之 build）——T3d／T9d／T6d 之期隨之（本器之樁⛔ 寫入池閘之末態 ⇒ 試算之 build 之各宗自為其成員）。
   🔧 `W-G.9-378`（`GB-204`·⛔ 上列一字不刪）：段三之 `alloc_state` 之出另增 `pool_out`（入池閘之帳·與 `members` 取同一 build）
            ——T3d／T9d／T6d 之期隨之（本器之樁⛔ 帶入池閘之帳 ⇒ `{}`）。
+  🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：段三與末端塊合併再試之樁之簽名增 `blk5`（五級之街廓屬性之回呼·其接線由 F23 之
+           W9 量之）；T6a 之期增 `blk5`（`k6b_screen_callbacks` 之回傳）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import contextlib, copy, importlib.util, inspect, io, os, sys
@@ -199,8 +201,9 @@ class _Rig:
         st.rerun()
 
     def s3(self, order, locked, own_map, temp_parcels, build_parcels, blocks, centerlines, a_prime, trial_winner,
-           alloc_state, *, log_print=print, contests=None):
+           alloc_state, *, log_print=print, contests=None, blk5=None):
         self.s3_n += 1
+        self.s3_blk5 = blk5                 # 🔧 `W-G.9-384`（`K-9-71`）：五級之屬性之回呼（其接線由 F23 之 W9 量之）
         self.in_s3 = True
         try:
             self.s3_state = alloc_state(temp_parcels, build_parcels)
@@ -219,8 +222,9 @@ class _Rig:
         return t2, b2, [dict(L3)]
 
     def merge(self, temp_parcels, build_parcels, own_map, locked, corner_lots, blocks, centerlines, a_prime,
-              alloc_eval, alloc_state, *, setback=None, log_print=print):
+              alloc_eval, alloc_state, *, setback=None, log_print=print, blk5=None):
         self.merge_n += 1
+        self.merge_blk5 = blk5              # 🔧 `W-G.9-384`（`K-9-71`）
         self.merge_args = dict(temp=temp_parcels, build=build_parcels, own=dict(own_map or {}), locked=set(locked or ()),
                                corner=set(corner_lots or ()), blocks=copy.deepcopy(blocks),
                                cl=copy.deepcopy(centerlines), setback=setback)
@@ -477,7 +481,8 @@ def _t6(ns, ss):
     with _rigged(ns, ss, dict(order=[]), "on") as rig:
         st = _St(ss)
         cb = ns["k6b_screen_callbacks"](st, pk_kwargs=pk, g_kwargs=g)
-        out.append(("T6a 四注入物之名", sorted(cb), ["a_prime", "alloc_eval", "alloc_state", "trial_winner"]))
+        # 🔧 `W-G.9-384`（`K-9-71`）：注入物增 `blk5`（五級之街廓屬性·呼叫時取之）
+        out.append(("T6a 注入物之名（四 ＋ blk5）", sorted(cb), ["a_prime", "alloc_eval", "alloc_state", "blk5", "trial_winner"]))
         out.append(("T6b a′ ＝ a(src) × p(src) ÷ p(dst)（100 × 1000 ÷ 500）", round(cb["a_prime"](t0[0], t0[2]), 9), 200.0))
         with contextlib.redirect_stdout(io.StringIO()):
             tw = cb["trial_winner"](t0, b0, "B1", "左", "A(1)")
diff --git a/verify/probes/probe_WG9356_screenmerge_wiring.py b/verify/probes/probe_WG9356_screenmerge_wiring.py
index c489e88..f381204 100644
--- a/verify/probes/probe_WG9356_screenmerge_wiring.py
+++ b/verify/probes/probe_WG9356_screenmerge_wiring.py
@@ -35,6 +35,7 @@
     S2 `自誤 517`：main() 內之 _f3L_invalidate_g_cache 抽出以假 st 實際執行：所列之鍵皆去、他鍵留、f3_g_needs_rerun ＝ True
        （該函式以 `except Exception: pass` 包裹 ⇒ 以結果判、⛔ 以「未拋」判）。
     本部全綠時另施 14 種原始碼突變，每一突變須使其所指之項轉紅（器紅 ⇒ rc 1）。
+  🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：W3 之回鍵之期 ＝ 四注入物 ∪ {blk5}（五級之街廓屬性·其接線由 F23 之 W9 量之）。
 rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
 """
 import ast, contextlib, copy, io, os, sys
@@ -47,6 +48,9 @@ except Exception:  # noqa: BLE001
 FN_S3, FN_EBM, FN_CB, FN_ROWS = ("f3_screen_k6b_stage3", "f3_screen_end_block_merge", "k6b_screen_callbacks",
                                  "end_block_merge_rows")
 CB4 = ("a_prime", "trial_winner", "alloc_state", "alloc_eval")
+# 🔧 `W-G.9-384`（`K-9-71`）：`k6b_screen_callbacks` 之回傳增 `blk5`（五級之街廓屬性·其接線由 F23 之 W9 量之）⇒ W3 之回鍵之期
+#   ＝ CB4 ∪ {blk5}（巢狀之同名之查⛔ 變）
+CB5_384 = CB4 + ("blk5",)
 LOGK = "f3_end_block_merge_log"
 
 
@@ -222,7 +226,7 @@ def _w3(tree, top):
     rets = [n for n in _walk_own(cb) if isinstance(n, ast.Return)]
     ret_ok = (len(rets) == 1 and isinstance(rets[0].value, ast.Dict)
               and {k.value: _uparse(v) for k, v in zip(rets[0].value.keys, rets[0].value.values)
-                   if isinstance(k, ast.Constant)} == {k: k for k in CB4})
+                   if isinstance(k, ast.Constant)} == {k: k for k in CB5_384})
     dup = sorted({f"{f.name}.{n.name}" for f in top.values() if f is not cb
                   for n in ast.walk(f) if isinstance(n, ast.FunctionDef) and n is not f and n.name in CB4})
     notes = []
diff --git a/verify/probes/probe_WG9357_k948.py b/verify/probes/probe_WG9357_k948.py
index 5efb835..e5a867a 100644
--- a/verify/probes/probe_WG9357_k948.py
+++ b/verify/probes/probe_WG9357_k948.py
@@ -24,6 +24,13 @@
            逐受併之街廓：先一次全部、次 建地 → 道路 → 公設地 逐類全併，不過之類按比例（各片乘同一百分比·類之合計每
            `0.01 ㎡` 一格）、其後之類⛔ 併入本街廓；建地可拆分（部分併出者留 build、`面積_m2` 減其量、帶 `段三部分併出`·
            ⛔ `段三餘量`）；剩下依 `K-9-51` 逐輪（`K-9-68`：同一輪到達同一街廓者一起依 `K-9-66`·其距離與 G 取該輪之試算）。
+           🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：段三之 `blk5`（五級之街廓屬性之回呼）——本器之段三之呼叫一律經 `_s3384`：
+           受測函式受之 ⇒ 預設給「可建築街廓之五級與深度皆同」（`_b5`·⇒ 其序同前·K1〜K22 之期⛔ 變）。增 K23〜K29（第 5 項之
+           建地之片·`_go384`·K6 之形〔W1(1)·BW〕）：K23 他街廓之候選依五級（B5 之使用分區異 ⇒ 排後 ⇒ B7 之 Z1）；K24 本街廓之
+           候選恆先（W2(1)·BW·G 20）——縱他街廓之候選距離同為 0（U1(1)·BU·唯一點相接·G 500）；K25 他街廓之候選二以上而⛔ 給
+           五級之屬性 ⇒ 停機；K26 他街廓唯一 ⇒ ⛔ 須其屬性；K27 公設地之片（P1(1)·K3 之形）照距離（⛔ 呼其回呼）；K28 其回呼
+           唯呼一次（K23 之形）；K29 段三之 `blk5` 缺省 ＝ `None`（簽名）；K30 正面路寬之級（往窄先於往寬·原街廓與候選之向）；
+           K31 正面道路；K32 回呼回非 dict ⇒ 停機（唯讀審查之補）。期值出自本器之玩具之手算（發單側窗八十七）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import contextlib, copy, importlib.util, io, os, sys
@@ -149,7 +156,7 @@ def _go(ns, cap, price=None, drop=(), no_g=False, a=None, p_owner="g1", w1=False
         next(t for t in temp if t["暫編地號"] == pid).update(kv)
     build = [t for t in temp if t["街廓分類"] == H]
     ap, tw, st = _cbs(cap, price, drop, no_g)
-    t2, b2, log = ns["k6b_stage3_run"](ORDER, set(), own, temp, build, blocks, cl, ap, tw, st,
+    t2, b2, log = _s3384(ns)(ORDER, set(), own, temp, build, blocks, cl, ap, tw, st,
                                        log_print=lambda *x: None)
     by = {t["暫編地號"]: t for t in t2}
     post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
@@ -193,7 +200,7 @@ def _go4(ns, cap, thr=None, drop=("Y1(1)",)):
     order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
              {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
     ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
-    t2, b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, st,
+    t2, b2, log = _s3384(ns)(order, set(), own, temp, build, blocks, cl, ap, tw, st,
                                        log_print=lambda *x: None, contests=ct)
     by = {t["暫編地號"]: t for t in t2}
     post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
@@ -233,7 +240,7 @@ def _go5(ns, cap):
     order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
              {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
     ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
-    _t2, _b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, st,
+    _t2, _b2, log = _s3384(ns)(order, set(), own, temp, build, blocks, cl, ap, tw, st,
                                          log_print=lambda *x: None, contests=ct)
     post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
              tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
@@ -243,6 +250,80 @@ def _go5(ns, cap):
     return post, d5
 
 
+def _b5(blocks, over=None):
+    """🆕 `W-G.9-384`（`K-9-71`）：玩具之五級之街廓屬性（`adj_block_ctx` 之回傳之形）——可建築街廓（類 ＝ 住宅區）皆
+    使用分區 住宅區·最小建築面積 0·正面道路 RD·正面路寬 8·深度 30；`over` 覆寫之。"""
+    from decimal import Decimal
+    out = {b: {"使用分區": H, "最小建築面積": Decimal("0"), "正面道路": "RD", "正面路寬": Decimal("8"),
+               "深度": Decimal("30")} for b, v in blocks.items() if v.get("category") == H}
+    for b, kv in (over or {}).items():
+        out[b] = dict(out[b], **{k: (Decimal(str(x)) if isinstance(x, (int, float)) else x) for k, x in kv.items()})
+    return out
+
+
+def _s3384(ns):
+    """🆕 `W-G.9-384`：段三之呼叫——受測函式受 `blk5` 之時，呼叫端未給者補「皆同」（`_b5`）。"""
+    import inspect
+    f = ns["k6b_stage3_run"]
+    if "blk5" not in inspect.signature(f).parameters:
+        return f
+
+    def g(order, locked, own, temp, build, blocks, *a, **kw):
+        kw.setdefault("blk5", lambda: _b5(blocks))
+        return f(order, locked, own, temp, build, blocks, *a, **kw)
+    return g
+
+
+def _world384(u1=False, w2=False):
+    """🆕 `W-G.9-384`：`_world(w1=True)`（K6 之形）＋（w2）BW 之 W2(1)（x∈[60,65]·g1·20·⛔ 與他片相接）＋（u1）BU
+    （x∈[20,30]·y∈[40,50]）之 U1(1)（g1·500·與 W1(1) 唯一點相接 ⇒ 距離 0 而⛔ 地籍相連）。"""
+    t, own, blocks, cl = _world(None, "gP", True)
+    if w2:
+        t.append(_tp("W2(1)", "BW", H, _R(60, 65, 30, 40), 20))
+        own["W2"] = "g1"
+    if u1:
+        t.append(_tp("U1(1)", "BU", H, _R(20, 30, 40, 50), 500))
+        own["U1"] = "g1"
+        blocks["BU"] = {"category": H}
+    return t, own, blocks, cl
+
+
+def _go384(ns, cap, b5="eq", own_upd=None, u1=False, w2=False, n5=None):
+    """🆕 `W-G.9-384`：K6 之形（W1(1) 整筆不過 ⇒ 按比例部分併入 X1；剩下依第 5 項）·`b5`：`"eq"` ⇒ 皆同；`dict` ⇒ 覆寫；
+    `None` ⇒ ⛔ 給；`n5` ＝ 計回呼之呼數之 list。回後處理之列。"""
+    temp, own, blocks, cl = _world384(u1, w2)
+    own = dict(own, **(own_upd or {}))
+    build = [t for t in temp if t["街廓分類"] == H]
+    ap, tw, st = _cbs(cap, None, ("W1(1)",))
+    if b5 is None:
+        f5 = None
+    else:
+        def f5():
+            if n5 is not None:
+                n5.append(1)
+            return _b5(blocks, None if b5 == "eq" else b5)
+    _t2, _b2, log = ns["k6b_stage3_run"](ORDER, set(), own, temp, build, blocks, cl, ap, tw, st,
+                                         log_print=lambda *x: None, blk5=f5)
+    return [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
+             tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
+            for x in log if x.get("序") == "後處理"]
+
+
+def _k27(ns):
+    """🆕 `W-G.9-384`：公設地之片（P1(1)·K3 之形）於他街廓之五級異時之列與回呼之呼數。"""
+    n5 = []
+    temp, own, blocks, cl = _world()
+    build = [t for t in temp if t["街廓分類"] == H]
+    ap, tw, st = _cbs(_cap(B3=120.0, B5=120.0))
+
+    def f5():
+        n5.append(1)
+        return _b5(blocks, {"B5": {"使用分區": "商業區"}})
+    _t2, _b2, log = ns["k6b_stage3_run"](ORDER, set(), own, temp, build, blocks, cl, ap, tw, st,
+                                         log_print=lambda *x: None, blk5=f5)
+    return ([(x["候選"], x["層級"], x["結果"], x["受併宗"]) for x in log if x.get("層級") == "後處理·第5項"], len(n5))
+
+
 def _halt(ns, phrase, **kw):
     try:
         _go(ns, **kw)
@@ -463,9 +544,66 @@ def _cases(ns, sp):
                      drop=("W1(1)", "Y1(1)", "Y2(1)", "Z1(1)"))[0],
          # 🔧 `W-G.9-373`（`K-9-66`）：W1 按比例部分併入 X1 30
          [("W1(1)", "後處理(a)", "部分成", "X1(1)", (("X1(1)", 30.0),)), ("W1(1)", "後處理·第5項", "轉調配", "—", ())])
+    # 🆕 `W-G.9-384`（`K-9-71`·KL 裁 `2026-10-12 16:37`）：第 5 項之建地之片——本街廓者先；他街廓依五級 → 深度 → 距離 →
+    #   配得面積 → 重劃前面積 → 暫編地號（K6 之形：W1(1) 部分併入 X1 30 後剩下 20）
+    W30 = ("W1(1)", "後處理(a)", "部分成", "X1(1)", (("X1(1)", 30.0),))
+    _run(out, "K23 （K-9-71）B5 之使用分區（商業區）異於 W1 之所屬街廓 BW ⇒ 五級排後：剩下 20 併入 B7 之 Z1（⛔ 距離近之 B5）",
+         lambda: _go384(ns, _cap(B3=90.0), b5={"B5": {"使用分區": "商業區"}}),
+         [W30, ("W1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),))])
+    _run(out, "K24 （K-9-71）本街廓之候選恆先：BW 之 W2(1)（G 20）先於 BU 之 U1(1)（距離同為 0·G 500）",
+         lambda: _go384(ns, _cap(B3=90.0), u1=True, w2=True),
+         [W30, ("W1(1)", "後處理·第5項", "成", "W2(1)", (("W2(1)", 20.0),))])
+    _run(out, "K25 他街廓之候選二以上（B5、B7）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）",
+         lambda: _halt384(ns, "未給五級之屬性"), ("停機", True))
+    _run(out, "K26 他街廓之候選唯一（B5·Z1 非 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（同 K6）",
+         lambda: _go384(ns, _cap(B3=90.0), b5=None, own_upd={"Z1": "gZ"}),
+         [W30, ("W1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 20.0),))])
+    _run(out, "K27 公設地之片（P1(1)·K3 之形）照距離（B5 之五級雖異）、⛔ 呼其回呼",
+         lambda: _k27(ns),
+         ([("P1(1)", "後處理·第5項", "部分成", "Y1(1)"), ("P1(1)", "後處理·第5項", "未成", "Y2(1)"),
+           ("P1(1)", "後處理·第5項", "成", "Z1(1)")], 0))
+    _run(out, "K28 五級之屬性之回呼唯呼一次（K23 之形）",
+         lambda: (lambda n5: (_go384(ns, _cap(B3=90.0), b5={"B5": {"使用分區": "商業區"}}, n5=n5), len(n5))[1])([]), 1)
+    _run(out, "K29 段三之關鍵字參數 blk5 之缺省 ＝ None",
+         lambda: _sig384(ns), "None")
+    # 🆕 `W-G.9-384`（唯讀審查之補）：正面路寬之級（原街廓與候選之向）、正面道路；回呼之型
+    _run(out, "K30 （K-9-71）正面路寬：BW 8、B5 15（往寬）、B7 6（往窄）⇒ 二者皆異、級距 B7 先 ⇒ Z1",
+         lambda: _go384(ns, _cap(B3=90.0), b5={"B5": {"正面路寬": 15}, "B7": {"正面路寬": 6}})[-1],
+         ("W1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),)))
+    _run(out, "K31 （K-9-71）正面道路：B5 臨他路（RX）⇒ 排後 ⇒ Z1",
+         lambda: _go384(ns, _cap(B3=90.0), b5={"B5": {"正面道路": "RX"}})[-1],
+         ("W1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),)))
+    _run(out, "K32 五級之屬性之回呼回非 dict ⇒ 停機",
+         lambda: _halt384b(ns), ("停機", True))
     return out
 
 
+def _halt384b(ns):
+    temp, own, blocks, cl = _world384()
+    build = [t for t in temp if t["街廓分類"] == H]
+    ap, tw, st = _cbs(_cap(B3=90.0), None, ("W1(1)",))
+    try:
+        ns["k6b_stage3_run"](ORDER, set(), own, temp, build, blocks, cl, ap, tw, st, log_print=lambda *x: None,
+                             blk5=lambda: [])
+    except RuntimeError as e:
+        return ("停機", "五級之屬性非 dict" in str(e))
+    return ("無停機",)
+
+
+def _halt384(ns, phrase):
+    try:
+        _go384(ns, _cap(B3=90.0), b5=None)
+    except RuntimeError as e:
+        return ("停機", phrase in str(e))
+    return ("無停機",)
+
+
+def _sig384(ns):
+    import inspect
+    p = inspect.signature(ns["k6b_stage3_run"]).parameters.get("blk5")
+    return repr(p.default) if p is not None else "缺"
+
+
 def _perturb(v):
     if isinstance(v, bool):
         return not v
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index 083e8a0..abe2f7f 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -66,6 +66,18 @@
            單元之成員 ⇒ 入池閘之合併單元之取代之後，宿主之單元帶 `第31條第3款併入`〔其值 ＝ 所併入之片〕·受併之片之 temp 之鍵
            照舊）。期值出自本器之玩具之手算（發單側窗八十六）。
            P0 隨之 60 項。
+           🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：受測函式增關鍵字參數 `blk5`（五級之街廓屬性之回呼）——本器之玩具一律
+           給之（`_go` 之 `b5`：缺 ⇒ 可建築街廓〔類 ＝ 住宅區〕之五級與深度皆同〔`_b5`·⇒ 其序同前·K1〜K60 之期⛔ 變〕；`dict`
+           ⇒ 逐街廓覆寫其屬性；`None` ⇒ ⛔ 給；可呼 ⇒ 逕用之）；他世界之直呼經 `_fn384` 補之。增 K61〜K69：K61 建地之剩下依
+           五級（他街廓之使用分區異者排後）先於距離；K62 深度（較深者排後）·同深之容差 0.1 m 內 ⇒ 依距離；K63 最小建築面積
+           往大之街廓排後而⛔ 淘汰（前者不過 ⇒ 續試之）；K64 他街廓之候選二以上而⛔ 給五級之屬性 ⇒ 停機；K65 他街廓唯一 ⇒
+           ⛔ 比五級、⛔ 須其屬性；K66 屬性缺片之所屬街廓 ⇒ 停機；K67 其回呼唯於須比時呼一次；K68 `k971_key5` ＝
+           `adj_candidate_lists` 之建地軌之八鍵之前六（合成之屬性·逐對）；K69（`W-G.9-383` 補令一之審查 #9）再試成之標記之聯集
+           非空而入池閘之合併單元之取代未成 ⇒ 當下之態⛔ 變：受併之片仍在 build 且帶標記、宿主⛔ 帶鍵。期值出自本器之玩具之
+           手算（發單側窗八十七）。P0 隨之 69 項。
+           🔧 `W-G.9-384`（唯讀審查之補·⛔ 上列一字不刪）：增 K70〜K74：K70 他街廓唯一而其宗二以上 ⇒ ⛔ 須其屬性；K71 五級與深度
+           皆同 ⇒ 依距離（名序最後而距離最近之街廓先·⛔ 以街廓名定之）；K72 正面路寬之級（往窄先於往寬·原街廓與候選之向）；
+           K73 正面道路；K74 回呼回非 dict ⇒ 停機。P0 隨之 74 項。W9 另查二回呼之 `k971_blk5` 之六引數之源（依序之字樣）。
   wiring   <repo> <基準 commit>
            接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_k953`）與 `run_corner_pk_k6b`
            之序（末端塊合併再試之後、以 winners／forced 呼叫、其後⛔ 重跑街角選位）；W3 畫面之入口（`f3_screen_k953`·
@@ -73,6 +85,13 @@
            地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）對基準一字未動；W7 頂層節點之相異 ⊆ 本單之許；
            W8 既有量測器之錨（其字串常數〔長 ≥ 4〕於基準之 app.py／selection_pipeline.py 恰一見者）於工作樹仍恰一見；
            基準中恰一之函式名（含巢狀）於工作樹仍恰一（新碼⛔ 同名）。
+           🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：W1 之 `k953_manual_run` 之關鍵字參數 ＝ `log_print`、`blk5`；W6 之受詞去
+           `f3_screen_end_block_merge`、`run_end_block_merge`；W7 之許增 `k971_key5`、`k971_blk5`、`f3_screen_end_block_merge`
+           與 `run_end_block_merge`；增 W9 五級之接線——`k953_manual_run`／`k6b_stage3_run`／`end_block_merge_run` 之關鍵字參數
+           `blk5`（預設 `None`）；後者呼段三恰一處傳 `blk5=blk5`；畫面之三入口（`f3_screen_k6b_stage3`→段三、
+           `f3_screen_end_block_merge`→末端塊合併再試、`f3_screen_k953`→手冊先行）與 harness 之三入口（`run_corner_pk_k6b`、
+           `run_end_block_merge`、`run_k953`）各恰一處以 `blk5=` 傳 `k6b_screen_callbacks`／`_k6b_callbacks` 之 `'blk5'`；二回呼之
+           回傳之 dict 含鍵 `'blk5'`，其值為其巢狀 `blk5`，其內恰一處呼 `k971_blk5`、以 `adj4_depth_of` 取深度；二新函式⛔ 案件字面。
   run      <repo> [<退縮> …]
            harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 手冊先行之紀錄逐列 ＝ 本器所載；R2 街角第 1 宗之宗 ＝ 旗標 off 之
            實跑（街角定案·`v3` §8）；R3 配地之全部（各宗之街廓·推進側·G）與各街廓之抵費地 ＝ 本器所載（容差 `0.01`）且
@@ -241,7 +260,7 @@ def _w1():
 
 def _go(world, *, own_upd=None, a_upd=None, drop=("X1(1)",), cap=None, price=None, gmap=None, err_cap=None,
         units=None, unit_g=None, pre=None, extra=None, rm=(), blk_upd=None, geom_upd=None, cl_upd=None, orig_upd=None,
-        need=None, nodg=False, units_if=None):
+        need=None, nodg=False, units_if=None, b5="eq"):
     t, own, blocks, cl = world()
     for e in (extra or []):
         t.append(copy.deepcopy(e))
@@ -259,12 +278,48 @@ def _go(world, *, own_upd=None, a_upd=None, drop=("X1(1)",), cap=None, price=Non
         next(x for x in t if x["暫編地號"] == pid).update(kv)
     build = [x for x in t if x["街廓分類"] == H]
     ap, st = _cbs(cap, price, drop, gmap, err_cap, units, unit_g, need, nodg, units_if)
-    return _NS["fn"](t, build, own, blocks, cl, ap, st, log_print=lambda *x: None), t, build
+    kw5 = {} if (b5 == "eq" and not _takes_b5(_NS["fn"])) else {"blk5": _b5fn(blocks, b5)}
+    return _NS["fn"](t, build, own, blocks, cl, ap, st, log_print=lambda *x: None, **kw5), t, build
 
 
 _NS = {}
 
 
+def _b5(blocks, over=None):
+    """🆕 `W-G.9-384`（`K-9-71`）：玩具之五級之街廓屬性（`adj_block_ctx` 之回傳之形）——可建築街廓（類 ＝ 住宅區）皆
+    使用分區 住宅區·最小建築面積 0·正面道路 RD·正面路寬 8·深度 30；`over` ＝ `{街廓: {'使用分區'|…: 值}}` 覆寫之。"""
+    from decimal import Decimal
+    out = {b: {"使用分區": H, "最小建築面積": Decimal("0"), "正面道路": "RD", "正面路寬": Decimal("8"),
+               "深度": Decimal("30")} for b, v in blocks.items() if v.get("category") == H}
+    for b, kv in (over or {}).items():
+        out[b] = dict(out[b], **{k: (Decimal(str(x)) if isinstance(x, (int, float)) else x) for k, x in kv.items()})
+    return out
+
+
+def _b5fn(blocks, b5):
+    """🆕 `W-G.9-384`：`_go` 之 `b5` ⇒ 受測函式之 `blk5`（`"eq"` ⇒ 皆同；`dict` ⇒ 覆寫；`None` ⇒ ⛔ 給；可呼 ⇒ 逕用）。"""
+    if b5 is None or callable(b5):
+        return b5
+    return lambda: _b5(blocks, None if b5 == "eq" else b5)
+
+
+def _takes_b5(f):
+    """🆕 `W-G.9-384`：受測函式（或 `_fn384` 所包者）之參數含 `blk5`？——預設之「皆同」唯於受測函式受之時給之（開工態之碼
+    ⛔ 受之 ⇒ K1〜K60 於開工態照舊可量；K61〜K67 之明給者恆給之 ⇒ 開工態紅）。"""
+    import inspect
+    return "blk5" in inspect.signature(getattr(f, "__wrapped384__", f)).parameters
+
+
+def _fn384(f):
+    """🆕 `W-G.9-384`：他世界之直呼（⛔ 經 `_go`）補 `blk5`（皆同·`_b5`·唯於受測函式受之時）。"""
+    def g(temp, build, own, blocks, cl, ap, st, **kw):
+        if _takes_b5(f):
+            kw.setdefault("blk5", lambda: _b5(blocks))
+        return f(temp, build, own, blocks, cl, ap, st, **kw)
+    g.__wrapped384__ = f
+    return g
+
+
 def _rows(res):
     """手冊之列（序 ＝ 手冊／K-9-51）之 (片, 類, 受併宗, ((受併宗, 併入量 2 位)…), 結果)。"""
     t2, b2, log = res[0]
@@ -330,7 +385,7 @@ def _sel(res, pid):
 
 def _cases(ns, sp):
     out = []
-    _NS["fn"] = ns[FN]
+    _NS["fn"] = _fn384(ns[FN])            # 🔧 `W-G.9-384`（`K-9-71`）：他世界之直呼補 blk5（皆同）
     W = _w1
     G1 = {"C1": "gC1"}          # 地主 g1 之已配得唯 BB 之 X1(2)
     BE = {"blk_upd": {"BE": H}, "extra": [_tp("E1(1)", "BE", H, _R(10, 20, 30, 50), 300)]}
@@ -602,9 +657,97 @@ def _cases(ns, sp):
                  units_if={"Y1(1)": (["X1(2)", "Y1(1)"], "X1(2)", 360.0)})),
          ([("X1(1)", "X1(2)", (("X1(2)", 60.0),), "成", None)], [("Y1(1)", "取代")],
           ({"X1(2)": ["X1(1)"], "Y1(1)": ["X1(1)"]}, ["C8(1)", "C9(1)", "Q1(1)", "Q2(1)", "Y1(1)", "Z1(1)"])))
+    # 🆕 `W-G.9-384`（`K-9-71`·KL 裁 `2026-10-12 16:37`）：建地之片依距離併入同一地主他處已配得之宗——本街廓者先；他街廓
+    #   依五級 → 深度 → 距離 → 配得面積 → 重劃前面積 → 暫編地號。世界一·K14 之形：X1(1)（BA）部分併入 X1(2)（BB 容 10）後，
+    #   剩下 50 之他街廓之候選 ＝ C1(1)（BC·距 10）、Z1(1)（BD·距 20）
+    K14W = dict(own_upd={"Z1": "g1"}, cap={"BB": 10.0}, rm=("R1(1)", "P1(1)"))
+    P14 = ("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 10.0),), "部分成")
+    _run(out, "K61 （K-9-71）BC 之使用分區（商業區）異於片之所屬街廓 BA ⇒ 五級排後：剩下 50 併入 BD 之 Z1(1)（⛔ 距離近之 C1(1)）",
+         lambda: _rows(_go(W, b5={"BC": {"使用分區": "商業區"}}, **K14W)),
+         [P14, ("K-9-51", "X1(1)", "a", "Z1(1)", (("Z1(1)", 50.0),), "成")])
+    _run(out, "K62 （K-9-71）五級皆同而 BC 較深（40）⇒ 排後 ⇒ Z1(1)；BC 深 30.1（同深之容差 0.1 m 內）⇒ 依距離 ⇒ C1(1)",
+         lambda: (_rows(_go(W, b5={"BC": {"深度": 40}}, **K14W))[-1],
+                  _rows(_go(W, b5={"BC": {"深度": 30.1}}, **K14W))[-1]),
+         (("K-9-51", "X1(1)", "a", "Z1(1)", (("Z1(1)", 50.0),), "成"),
+          ("K-9-51", "X1(1)", "a", "C1(1)", (("C1(1)", 50.0),), "成")))
+    _run(out, "K63 （K-9-71）BD 之最小建築面積往大（100）⇒ 排後而⛔ 淘汰：C1(1)（BC 容 0）不過 ⇒ 續試 Z1(1) 成",
+         lambda: _rows(_go(W, b5={"BD": {"最小建築面積": 100}}, **dict(K14W, cap={"BB": 10.0, "BC": 0.0}))),
+         [P14, ("K-9-51", "X1(1)", "a", "C1(1)", (), "未成"), ("K-9-51", "X1(1)", "a", "Z1(1)", (("Z1(1)", 50.0),), "成")])
+    _run(out, "K64 他街廓之候選二以上（BC、BD）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）",
+         lambda: _halt(lambda: _go(W, b5=None, **K14W), "未給五級之屬性"), ("停機", True))
+    _run(out, "K65 他街廓之候選唯一（BB·C1 去之）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（K42 之形）",
+         lambda: _sel(_go(W, own_upd={"Q1": "g1", "XB": "g1"}, cap={"BA": 0.0}, orig_upd={"X1(2)": "XB"},
+                          rm=("C1(1)",), b5=None), "X1(1)"),
+         [("手冊", "X1(1)", "a", "Q1(1)", (), "未成"), ("K-9-51", "X1(1)", "a", "X1(2)", (("X1(2)", 60.0),), "成")])
+    _run(out, "K66 五級之屬性缺片之所屬街廓（BA）⇒ 停機",
+         lambda: _halt(lambda: _go(W, b5=lambda: {k: v for k, v in _b5(_w1()[2]).items() if k != "BA"}, **K14W),
+                       "無五級之屬性"), ("停機", True))
+    _run(out, "K67 五級之屬性之回呼唯於須比時呼之、且一次（K61 之形 ⇒ 1；Z1 非 g1 ⇒ 他街廓唯一 ⇒ 0）",
+         lambda: _k67(W, K14W), (1, 0))
+    _run(out, "K68 k971_key5 ＝ adj_candidate_lists 之建地軌之八鍵之前六（合成之屬性三組·七街廓·逐對 126）",
+         lambda: _k68(ns), (126, 0))
+    # 🆕 `W-G.9-384`（`W-G.9-383` 補令一之審查 #9·覆蓋之補）：標記之聯集非空而單元之取代未成
+    _run(out, "K69 再試成而受併之片 X1(2) 為 Y1(1) 之單元之成員；取代後之配地相異（未取代）⇒ 當下之態⛔ 變：X1(2) 仍在 build 且帶"
+              "標記、宿主 Y1(1)⛔ 帶鍵",
+         lambda: (lambda r: (_rows4(r), _unit_rows(r), _mark4(r)))(
+             _go(W, drop=("X1(1)", "X1(2)", "Y1(1)"), rm=RM4, own_upd={"Y1": "g1"}, unit_g=999.0,
+                 units_if={"Y1(1)": (["X1(2)", "Y1(1)"], "X1(2)", 360.0)})),
+         ([("X1(1)", "X1(2)", (("X1(2)", 60.0),), "成", None)], [("Y1(1)", "未取代（取代後之配地相異）")],
+          ({"X1(2)": ["X1(1)"]}, ["C8(1)", "C9(1)", "Q1(1)", "Q2(1)", "X1(2)", "Y1(1)", "Z1(1)"])))
+    # 🆕 `W-G.9-384`（唯讀審查之補）：他街廓唯一而其宗二以上；同鍵者依距離（⛔ 依街廓名）；正面路寬之級、正面道路；回呼之型
+    _run(out, "K70 他街廓唯一（BC）而其候選二宗（C1(1)、C9(1)·皆 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行 ⇒ C1(1)",
+         lambda: _rows(_go(W, b5=None, own_upd={"C9": "g1"}, cap={"BB": 10.0}, rm=("R1(1)", "P1(1)")))[-1],
+         ("K-9-51", "X1(1)", "a", "C1(1)", (("C1(1)", 50.0),), "成"))
+    _run(out, "K71 五級與深度皆同之他街廓 BC（距 10）、BD（距 20）、BZ（距 1·名序最後）⇒ 依距離 ⇒ BZ 之 Z9(1)（⛔ 依街廓名）",
+         lambda: _rows(_go(W, extra=[_tp("Z9(1)", "BZ", H, _R(10, 20, 31, 35), 300)], blk_upd={"BZ": H},
+                           own_upd={"Z1": "g1", "Z9": "g1"}, cap={"BB": 10.0}, rm=("R1(1)", "P1(1)")))[-1],
+         ("K-9-51", "X1(1)", "a", "Z9(1)", (("Z9(1)", 50.0),), "成"))
+    _run(out, "K72 （K-9-71）正面路寬：BA 8、BC 15（往寬）、BD 6（往窄）⇒ 二者皆異、級距 BD 先（往窄先於往寬）⇒ Z1(1)",
+         lambda: _rows(_go(W, b5={"BC": {"正面路寬": 15}, "BD": {"正面路寬": 6}}, **K14W))[-1],
+         ("K-9-51", "X1(1)", "a", "Z1(1)", (("Z1(1)", 50.0),), "成"))
+    _run(out, "K73 （K-9-71）正面道路：BC 臨他路（RX）⇒ 排後 ⇒ Z1(1)",
+         lambda: _rows(_go(W, b5={"BC": {"正面道路": "RX"}}, **K14W))[-1],
+         ("K-9-51", "X1(1)", "a", "Z1(1)", (("Z1(1)", 50.0),), "成"))
+    _run(out, "K74 五級之屬性之回呼回非 dict ⇒ 停機",
+         lambda: _halt(lambda: _go(W, b5=lambda: [], **K14W), "五級之屬性非 dict"), ("停機", True))
     return out
 
 
+def _k67(W, K14W):
+    """🆕 `W-G.9-384`：五級之屬性之回呼之呼數（須比 ⇒ 一次；⛔ 須 ⇒ 零）。"""
+    n = [0, 0]
+
+    def f(i):
+        def g():
+            n[i] += 1
+            return _b5(_w1()[2], {"BC": {"使用分區": "商業區"}})
+        return g
+    _go(W, b5=f(0), **K14W)
+    _go(W, b5=f(1), **dict(K14W, own_upd={}))
+    return tuple(n)
+
+
+def _k68(ns):
+    """🆕 `W-G.9-384`：`k971_key5` 與 `adj_candidate_lists` 之建地軌之鍵之前六逐對比（合成之屬性三組·七街廓）。"""
+    import random
+    tot = bad = 0
+    for seed in (1, 2, 3):
+        rg = random.Random(seed)
+        labs = [f"T{i}" for i in range(7)]
+        ctx = ns["adj_block_ctx"](labs, {x: rg.choice([H, "商業區"]) for x in labs},
+                                  {x: rg.choice([0, 100, 200]) for x in labs}, {x: rg.choice(["A", "B"]) for x in labs},
+                                  {x: rg.choice([6, 8, 10, 15]) for x in labs},
+                                  {x: rg.choice([20, 25, 25.05, 30]) for x in labs})
+        for h in labs:
+            unit = {"歸戶": "g", "軌": ns["ADJ_TRACK_BUILD"], "原街廓": h,
+                    "建築街廓內不能分配": [{"暫編地號": "Q", "原有面積": 1.0}], "共同負擔用地": []}
+            lst = ns["adj_candidate_lists"]({"units": [unit]}, ctx, {}, {"Q": [(0, 0), (1, 0), (1, 1), (0, 1)]})
+            for it in lst[0]["名單"][1:]:
+                tot += 1
+                bad += tuple(it["鍵"][:6]) != ns["k971_key5"](ctx, h, it["街廓"])
+    return tot, bad
+
+
 def _k32(W):
     def one(q_owner, cap):
         r = _go(W, own_upd={"Q1": q_owner, "C1": "gC1", "E1": "g1", "E9": "gE"}, geom_upd={"Q1(1)": _R(0, 8, 0, 30)},
@@ -1120,7 +1263,9 @@ def _wiring_checks(repo, base):
     sd, stree = _defs(spp)
     # W1 新名與簽名
     f = ad.get(FN)
-    ok = f is not None and [a.arg for a in f.args.args] == SIG and [a.arg for a in f.args.kwonlyargs] == ["log_print"]
+    # 🔧 `W-G.9-384`（`K-9-71`）：關鍵字參數增 `blk5`
+    ok = f is not None and [a.arg for a in f.args.args] == SIG and [a.arg for a in f.args.kwonlyargs] == ["log_print",
+                                                                                                         "blk5"]
     consts = {}
     for n in atree.body:
         if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
@@ -1226,9 +1371,73 @@ def _wiring_checks(repo, base):
         chk.append((f"W8 {nm_}：既有量測器之錨（{len(anc)}）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·"
                     f"{sum(1 for v in fb.values() if v == 1)}）仍恰一", not moved and not dup,
                     f"錨之異 {moved[:6]}；函式名之異 {dup[:8]}"))
+    chk.append(_w9_384(ad, sd))
     return chk
 
 
+def _w9_384(ad, sd):
+    """🆕 `W-G.9-384`（`K-9-71`）：W9 五級之接線（AST）。"""
+    bad = []
+
+    def _kwd(fn):
+        return {a.arg: (ast.unparse(d) if d is not None else None)
+                for a, d in zip(fn.args.kwonlyargs, fn.args.kw_defaults)} if fn is not None else {}
+    for nm in (FN, "k6b_stage3_run", "end_block_merge_run"):
+        if _kwd(ad.get(nm)).get("blk5", "缺") != "None":
+            bad.append(f"{nm} 之 blk5")
+    eb = ad.get("end_block_merge_run")
+    cs = [c for c in (_calls(eb) if eb is not None else []) if c[0] == "k6b_stage3_run"]
+    if not (len(cs) == 1 and [ast.unparse(k.value) for k in cs[0][3].keywords if k.arg == "blk5"] == ["blk5"]):
+        bad.append("end_block_merge_run → 段三")
+    for tree_, fn_, callee, pat in (
+            (ad, "f3_screen_k6b_stage3", "k6b_stage3_run", r"^_cb\['blk5'\]$"),
+            (ad, "f3_screen_end_block_merge", "end_block_merge_run", r"^_cb\['blk5'\]$"),
+            (ad, "f3_screen_k953", FN, r"^_b5953s$"),
+            (sd, "run_corner_pk_k6b", "k6b_stage3_run", r"^_cbk\['blk5'\]$"),
+            (sd, "run_end_block_merge", "end_block_merge_run", r"^callbacks\['blk5'\]$"),
+            (sd, "run_k953", FN, r"^callbacks\['blk5'\]$")):
+        node = tree_.get(fn_)
+        cs = [c for c in (_calls(node) if node is not None else []) if c[0] == callee]
+        kv = [ast.unparse(k.value) for c in cs for k in c[3].keywords if k.arg == "blk5"]
+        if not (len(cs) == 1 and len(kv) == 1 and re.match(pat, kv[0])):
+            bad.append(f"{fn_} → {callee}（{kv}）")
+    fk = ad.get("f3_screen_k953")
+    if fk is not None:
+        src = [ast.unparse(n.value) for n in ast.walk(fk) if isinstance(n, ast.Assign)
+               and [getattr(t, "id", None) for t in n.targets] == ["_b5953s"]]
+        if src != ["k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)['blk5']"]:
+            bad.append(f"f3_screen_k953 之 _b5953s（{src}）")
+    for tree_, nm in ((ad, "k6b_screen_callbacks"), (sd, "_k6b_callbacks")):
+        cb = tree_.get(nm)
+        rets = [n for n in (cb.body if cb is not None else []) if isinstance(n, ast.Return)]
+        ok_r = (len(rets) == 1 and isinstance(rets[0].value, ast.Dict)
+                and any(isinstance(k, ast.Constant) and k.value == "blk5" and ast.unparse(v) == "blk5"
+                        for k, v in zip(rets[0].value.keys, rets[0].value.values)))
+        nest = [n for n in (cb.body if cb is not None else []) if isinstance(n, ast.FunctionDef) and n.name == "blk5"]
+        nc = [x for x in (_calls(nest[0]) if len(nest) == 1 else [])]
+        kb = [c[3] for c in nc if c[0] == "k971_blk5"]
+        # 🔧 唯讀審查之補：`k971_blk5` 之六引數之源（依序·其式之 `ast.unparse` 含之字樣；巢狀之全文含 `SS_FRONT_ROAD_NAME` 與 `g_kwargs['classified_blocks']`〔畫面〕）
+        want = (((), ("K91_SS_MBA_EFFECTIVE",), ("SS_FRONT_ROAD_DERIVE",), (".get(", "'id'"),
+                 ("_corner_rows_init", "正面路寬(m)"), ("adj4_depth_of",)) if nm == "k6b_screen_callbacks" else
+                (("cb",), ("{}",), ("front_road_derive",), ("load_front_road_names",), ("param_rows", "正面路寬(m)"),
+                 ("adj4_depth_of",)))
+        ok_a = (len(kb) == 1 and len(kb[0].args) == 6 and not kb[0].keywords
+                and all(all(t in ast.unparse(a) for t in w) for a, w in zip(kb[0].args, want))
+                and (nm != "k6b_screen_callbacks" or all(t in ast.unparse(nest[0]) for t in (
+                    "SS_FRONT_ROAD_NAME", "g_kwargs['classified_blocks']")))
+                and (nm == "k6b_screen_callbacks" or ast.unparse(kb[0].args[1]) == "{}"))
+        ok_n = (len(nest) == 1 and sum(1 for c in nc if c[0] == "k971_blk5") == 1
+                and any(c[0] == "adj4_depth_of" for c in nc) and ok_a)
+        if not (ok_r and ok_n):
+            bad.append(f"{nm} 之 blk5（回 {ok_r}／巢狀 {ok_n}）")
+    lits = [(nm, x.value) for nm in ("k971_key5", "k971_blk5") if nm in ad for x in ast.walk(ad[nm])
+            if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value)]
+    if not all(nm in ad for nm in ("k971_key5", "k971_blk5")) or lits:
+        bad.append(f"二新函式（{[nm in ad for nm in ('k971_key5', 'k971_blk5')]}·案件字面 {lits}）")
+    return ("W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）", not bad,
+            f"不合 {bad}")
+
+
 def _fn_names(src):
     out = {}
     for n in ast.walk(ast.parse(src)):
@@ -1280,6 +1489,14 @@ APP_ALLOW |= {"k967_pool_out", "k967_pool_less"}
 # 🔧 `W-G.9-380`（巳 ①）：W7 之許增 `k965_part_split`（合併之宗之部分併入之帳·其行為由 F29 之 K33／K51〜K54 量之、
 #   其接線由 F29 之 Y10 量之）
 APP_ALLOW |= {"k965_part_split"}
+# 🔧 `W-G.9-384`（`K-9-71`）：傳 `blk5` 之畫面之末端塊合併再試之入口與 harness 之同入口出 W6 之受詞；W7 之許增五級之二純函式與之
+#   （其接線由本器之 W9 量之）
+CHG384_APP = ("f3_screen_end_block_merge",)
+CHG384_SP = ("run_end_block_merge",)
+KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG384_APP)
+KEEP_SP = tuple(x for x in KEEP_SP if x not in CHG384_SP)
+APP_ALLOW |= {"k971_key5", "k971_blk5"} | set(CHG384_APP)
+SP_ALLOW |= set(CHG384_SP)
 
 
 def _top_dump(tree):
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index 903249f..2992e4f 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -39,6 +39,8 @@
            段三紀錄、末端塊紀錄、手冊先行之紀錄、配地列、入池閘紀錄、不配地紀錄、調配之輸入，寫 out。
   offcmp   <a.json> <b.json>
            二 offsnap 之摘要逐項同（第一趟之紀錄唯出艙·⛔ 入判）。
+  🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：wiring 之 W5 之許增 `k971_key5`、`k971_blk5`、`f3_screen_end_block_merge`、
+           `run_end_block_merge`；W6 比之前，工作樹之列去其末之「, blk5=…)」（段三之呼叫增 `blk5=`·其接線由 F23 之 W9 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, difflib, io, os, re, subprocess, sys, warnings
@@ -756,6 +758,11 @@ FN_GONE373 = ("_k951", "_max357", "_split357", "_try", "_fill953", "_probe953",
 W6_REPL = {"k953_manual_run": (
     '            raise RuntimeError(f"{_hdr953} 建地片 {_x}（{_blk953[_x]}）於當下之試算已為已配得之宗 {_own953}"',
     '                               "或其成員——K-9-53 ① 之「分不到」不立、K-9-51 之「剩餘土地」不立 ⇒ 停機")')}
+# 🔧 `W-G.9-384`（`K-9-71`）：W5 之許增五級之二純函式與傳 `blk5` 之畫面與 harness 之入口；W6 比之前，工作樹之列去其末之
+#   「, blk5=…)」之關鍵字參數（⛔ 他改·其接線由 F23 之 W9 量之·⛔ 以逐字之列為許〔其字樣即 W7／F23 W8 之錨〕）
+ALLOW375_APP += ("k971_key5", "k971_blk5", "f3_screen_end_block_merge")
+ALLOW375_SP += ("run_end_block_merge",)
+B5_KW384 = re.compile(r", blk5=[^,()]+\)$")
 
 
 def _git_show(repo, rev, rel):
@@ -930,7 +937,8 @@ def _wiring_checks(repo, base, app=None, spp=None):
         if cur is None or old is None:
             w6.append((nm, False, 0, "缺"))
             continue
-        ok_, k_, note_ = _insert_only(ast.get_source_segment(src_o, old), ast.get_source_segment(src_c, cur),
+        _seg384 = "\n".join(B5_KW384.sub(")", x) for x in ast.get_source_segment(src_c, cur).splitlines())
+        ok_, k_, note_ = _insert_only(ast.get_source_segment(src_o, old), _seg384,     # 🔧 `W-G.9-384`
                                       W6_REPL.get(nm, ()))
         w6.append((nm, ok_, k_, note_))
     chk.append(("W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列"
diff --git a/verify/probes/probe_WG9370_adj4mut.py b/verify/probes/probe_WG9370_adj4mut.py
index b6a65f2..396bdcf 100644
--- a/verify/probes/probe_WG9370_adj4mut.py
+++ b/verify/probes/probe_WG9370_adj4mut.py
@@ -26,6 +26,8 @@
            `wiring`：X2 唯量頂層之相異 ⊆ {二函式} ∪ 本單之許（二函式之逐列之限退·本單重寫）；X3 改量 `_bpre_a4` 之新施點
            （其呼叫恰一、與 `k966_block_merge` 之呼叫同在一 `for` 之內且先之）；X4 之差除本單所改之二函式（`_k6b_callbacks`、
            `k6b_stage3_pool_temp`）之段；X5 之 `R-10′` 之模板改為新施點之文（「於第一趟併入街廓 {_bk} 之前」）。
+  🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：`wiring` 之 X2 之許增 `k971_key5`、`k971_blk5`、`f3_screen_end_block_merge`、
+           `f3_screen_k6b_stage3`；X4 之差另除 `run_end_block_merge`、`run_corner_pk_k6b` 之段（傳 `blk5`）。
 rc：0 相符／1 不符／2 用法錯。
 """
 import ast, contextlib, difflib, io, json, os, re, subprocess, sys, tempfile, textwrap
@@ -97,6 +99,10 @@ ALLOW373_SP += ("run_k953",)
 # 🔧 `W-G.9-380`（`W-G.9-375` 之【工】巳 ①）：X2 之許增 `k965_part_split`（合併之宗之部分併入之帳·其行為與接線由 F29 之
 #   K33／K51〜K54、Y10 量之）
 ALLOW373_APP += ("k965_part_split",)
+# 🔧 `W-G.9-384`（`K-9-71`）：X2 之許增五級之二純函式與傳 `blk5` 之二畫面入口；X4 之除外增傳 `blk5` 之二 harness 入口
+#   （本單之行為與接線由 F23 之 K61〜K68、W9 與 F16 之 K23〜K29 量之）
+ALLOW373_APP += ("k971_key5", "k971_blk5", "f3_screen_end_block_merge", "f3_screen_k6b_stage3")
+ALLOW373_SP += ("run_end_block_merge", "run_corner_pk_k6b")
 
 
 def _strip_fns(src, names):
````

## 附錄乙　塊 `K24`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

---

## 🔧 `W-G.9-383` 之入主線；`K-9-78` 之立（調配之畫面入口：新調配程式落地後，「執行七級調配」之鍵併入「G 值迭代計算」·甲）；`K-9-71` 之落地之【工】之讀法；`W-G.9-383` 補令一之審查 #9 之例（`W-G.9-384`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`（`W-G.9-383` 補令二 工項一）之後；本節之碼入新側支 `verify/W-G.9-384-k971`（`W-G.9-384` 工項二）。**授權** ＝ `docs/orders/W-G.9-384_規格單.md` `§二`。

**編號之由**（`W-G.9-384 §零-1`）：`K-9` 之 `MAX` ＝ `77`（開工態 `fffa397`·`probe_WG9321_issuer_anchor.py` 之「項4′」）；`K-9-78` 於開工態之全倉追蹤檔（`git grep -c -P "(?<![0-9\-])K-9-78(?![0-9])"`·列框）＝ `0` ⇒ 取之。

### 一、`W-G.9-383` 之入主線

- 上開「`W-G.9-382` 之入主線；……（`W-G.9-383`）」節之 `K-9-75`〜`K-9-77` 與 `K-9-73` ④ 之「落地狀態」逐字「🔶（新側支 `verify/W-G.9-383-k975`·`W-G.9-383` 工項二·候入主線之請示）」——其碼（原單與補令一〔`R-12`〕·側支之端 `fa31382`）經發單側窗八十六自倉復驗、KL 之畫面核對與放行（**逐字**「383 畫面核對無誤，准入主線」·`2026-10-15 14:40`）⇒ `W-G.9-383` 補令二（主線快轉至 `fa31382` ＋ 主 checkout 之同步）⇒ 主線 ＝ `fffa397`。⇒ `K-9-73` ④、`K-9-75`〜`K-9-77`、唯註之二處（C-1）、`R-12`：✅（主線）。
- 補令一裁一之 `R-12`（入池閘之合併單元之取代時，自 build 去之成員之標記併入單元之同鍵）隨之 ✅；其「標記之聯集非空而取代未成」之支之例（補令一之重派之審查 🟠 #9·覆蓋之缺）⇒ 本單之 `F23` `K69`（下開三之庚）。

### 二、`K-9-78` 之出處

**KL 之問**（`2026-10-15 04:55`·**逐字**·節錄）：

> 1. 問題：目前程式為 按街角地計算確認街角地後，再按 G值迭代計算，但按照上面討論配地方式(合併或進5級)及邊試配邊驗方式，原先程式還有一個七級調配的按鍵，還有需要?邊試配邊厭世程式自己跑，使用者僅須按一次"G值迭代計算"?

**發單側窗八十五之答**（對話·**逐字**之四欄；其全文亦錄於倉外之交接文 `交接文_發單側窗八十五至八十六.md` 之 `§七` 項 `3`）：

> 【現況】畫面上的配地要依序按三個鍵：
> 1. **「執行第 1 宗街角地優先權選位」**：按一次，程式會自動跑完以下步驟：
>    - 選出街角地；
>    - 處理跨分配線的土地；
>    - 手冊先行的各項併入，包括第 31 條第 3 款、這次 383 的「兩側都配不到再試」，以及道路用地分配原則。
> 2. **「執行 G 值迭代計算」**：依第 1 鍵的結果正式配地。同街廓同地主的合併、邊試配邊檢查，都會自動反覆跑到結果穩定。
> 3. **「執行七級調配」**：處理前兩鍵跑完後仍配不到的土地，並消耗調配池。
>    - 這個鍵目前接的是已停用、留存備查的舊版調配程式。先前以程式模擬跑本案，會停在程式內部的一項檢查，沒有產出結果；直接在畫面上按的情形，尚未實際驗證。
>    - 依先前定案，新的調配程式寫好之後，這個鍵改接新程式。
>
> 所以，您這次定的合併、再試、回復原狀，都已包含在前兩鍵裡，會自動跑完，不需另外按。但調配這個階段仍然需要：五級（W-G.9-384）之後仍配不到的土地，以及調配池的消耗，都在這裡處理。
>
> 【要改成】按鍵的安排有兩種做法：
> - 甲：新的調配程式寫好後，併入「G 值迭代計算」。按一次就跑到調配完成，各步驟的紀錄仍可逐段展開查看。
> - 乙：保留獨立的按鍵。先看過 G 值迭代的結果，再按調配。
>
> 【對土地的影響】兩種做法的配地結果相同，只差在操作的步數，以及能否在中途停下來查看。新的調配程式寫好之前，兩種做法都不需要動。
>
> 【要你判斷】採甲或乙？不急，可以等擬新調配程式的規格單時再定。這一項已記入交接文第七節。

**KL 之文**（`2026-10-15 16:07`·**逐字**）：

> 按鍵要併入 G 值迭代（甲）

其受詞 ＝ 上開之【要你判斷】。

### 🔒 `K-9-78`　**調配之畫面入口：新調配程式落地後，「執行七級調配」之鍵去之，調配併入「執行 G 值迭代計算」——按一次即跑至調配完成，各步驟之紀錄仍逐段展開可查；新調配程式落地之前，畫面之鍵⛔ 動**（KL 裁 `2026-10-15 16:07`·canonical·**逐字**「按鍵要併入 G 值迭代（甲）」）

**裁之內容** ＝ 所呈之甲（逐字見上開二）。

**與既有正典之關係**（⛔ 改原文·依本裁讀之）：
- `CLAUDE.md`「🔧 待落地清單之補登：調配階段之諸裁（`K-9-35`〜`40`／`K-9-45`／`K-9-46`）（`W-G.9-332`）」節之「新調配程式落地後，畫面「執行七級調配」改接新程式」與 `docs/specs/調配階段_泛用規格_v1.md` 之同旨之句（「新調配程式落地後，畫面「執行七級調配」按鈕改接新程式」）——讀為：新調配程式之入口 ＝ 「執行 G 值迭代計算」之一按之末段，「執行七級調配」之鍵去之。
- `CLAUDE.md`「🔧 待落地清單之更新：錨之重量收窄（W-F／W-D.4 凍存·⛔ 重錨）；……（`W-G.9-348`）」節之序 `4`（畫面「執行七級調配」之現況·⬜）——其落地之形依本裁。
- 配地之結果⛔ 涉（所呈之【對土地的影響】）。

**射程**：及於**任一案件**。

**落地狀態**：⬜（落地之單 ＝ 新調配程式之規格單〔規格步 `5`〜`8`〕；其前畫面⛔ 動）。

### 三、`K-9-71` 之落地之【工】之讀法（`W-G.9-384`·發單側窗八十七·⛔ 充裁·以交付之通知告 KL）

上開「`W-G.9-375` 之【工】巳之三停機之處置；`K-9-71` 之立……（`W-G.9-380`）」節之 `K-9-71` 之【工】之讀法甲〜丁沿用；本節補其落地之形：
- **甲 處**：段三後處理之第 `5` 項之輪（`k6b_stage3_run` 之 `_p5_373`）與手冊先行之 `K-9-51` 之輪（`k953_manual_run`）之「各片之候選之序」（`K-9-71` 之讀法丙·「上列四處皆由之」）；輪（`K-9-68`）、每次之「不影響原位次」之檢核、`K-9-66` 之按比例、諸輪畢之轉調配／入合併單位皆⛔ 變。
- **乙 序**：建地之片（片之街廓分類之負擔屬性 ＝ 可建築土地）——① 本街廓之候選恆先；其間照舊（段三 ＝ `k967_rank`〔距離皆 `0`〕；手冊先行 ＝ 相連者先 → `k967_rank`·`W-G.9-380` 讀法丙）。② 他街廓之候選依五級與深度（`k971_key5` ＝ 調配之候選街廓名單〔`adj_candidate_lists`〕之建地軌之八鍵之前六之同式；原街廓 ＝ 片之所屬街廓；最小建築面積與正面路寬之級取全部可建築街廓之相異值；同深之容差 `0.1 m`·`K-9-52` ③）；其同者依舊之序（距離〔該片至該街廓·`0.01 m`〕→ `k967_rank`〔配得面積大 → 重劃前面積大 → 暫編地號小·`K-9-67`〕）。道路用地、公設地上之片：照舊（距離 → `k967_rank`）。🔒 段三之第 `5` 項之舊之序（距離 → `k967_rank`）於他街廓之候選距離亦為 `0`（唯點相接）而其配得面積較大者，可先於本街廓之候選——`K-9-71` 之「本街廓已配得之宗仍最先」改之（`F16` `K24`）。
- **丙 五級之屬性**：與調配之名單（`adj4_plan`·第一趟）之街廓屬性同一處——`k971_blk5`（可建築街廓之使用分區、最小建築面積、正面道路之識別符〔`r3_front_road_identifier`·⛔ 佔位〕、正面路寬、深度 ⇒ `adj_block_ctx`）；畫面 ＝ `k6b_screen_callbacks` 之 `blk5`（session 之最小建築面積〔`K91_SS_MBA_EFFECTIVE`〕、正面道路之推導與步驟 E 之名、街角之初列之正面路寬、`adj4_depth_of` 之深度·同 `f3_screen_adj4`）；harness ＝ `_k6b_callbacks` 之 `blk5`（同 `run_adj4`：最小建築面積 `{}`、`cad` 之推導、`load_front_road_names()`、`param_rows` 之正面路寬、`adj4_depth_of`）。
- **丁 何時取之**：他街廓之候選唯一 ⇒ ⛔ 比五級、⛔ 取其屬性（其序與舊同·無屬性亦照行）；二以上 ⇒ 取之一次（同一次之段三或手冊先行之內共用）；其停機照拋——正面道路無識別符者一次列出、須於步驟 E 填名（`K-9-52` 通知 `3`·`K-9-71` 讀法丁）、深度或路寬缺等（`adj_block_ctx`）；片之所屬街廓或候選街廓不在其表 ⇒ 停機；呼叫端未給之 ⇒ 停機（⛔ 以距離代之）。
- **戊 往大**：最小建築面積較片之所屬街廓大者排於全部較小者之後、⛔ 淘汰（KL `2026-10-12` 所核之文「這幾項都是排名條件，不淘汰任何街廓：容不下就往名單下一名試」；`K-9-71` 讀法甲）。
- **己 紀錄**：手冊先行之 `K-9-51` 之列之「依據」之字面改為「K-9-51／K-9-71（剩餘土地·本街廓先·建地之他街廓依五級 → 距離）」；他欄與段三之紀錄之欄⛔ 變。
- **庚 審查 #9 之例**（`W-G.9-383` 補令一之重派之審查之 🟠 #9）：`F23` `K69`——再試成而受併之片為同地主他宗之單元之成員，入池閘之合併單元之取代未成（取代後之配地相異）⇒ 當下之態⛔ 變：受併之片仍在 build 且帶標記、宿主⛔ 帶鍵（其判別力：取代未成仍寫入宿主之標記之突變 ⇒ `K60`／`K69` 紅）。
- **辛 本案**（發單側窗八十七·主線之端 `fffa397`·harness·二退縮）：段三後處理之第 `5` 項之列 ＝ `0`（`3.5 m` 段三之紀錄 `19` 列·`0 m` `0` 列）、末端塊合併再試之紀錄 ＝ `0` 列（⇒ 其第 `5` 項之列 `0`）、手冊先行之 `K-9-51` 之列 ＝ `0`（手冊先行之紀錄 `37`／`46` 列·整批成）⇒ `K-9-71` 於本案⛔ 觸；所呈之「本案：上述四處有無「距離與五級排出不同結果」的情形」之答 ＝ **無**（四處皆無片入其輪）。原型之實跑：配地、諸紀錄⛔ 變，五級之屬性之回呼於二退縮皆⛔ 呼（`W-G.9-384` 規格單 `§一` 項 `5`）。

**落地狀態**：`K-9-71` 🔶（新側支 `verify/W-G.9-384-k971`·`W-G.9-384` 工項二·候入主線之請示）；`K-9-78` ⬜（新調配程式之規格單）。
````

## 附錄丙　塊 `E27`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末·工項三）

````markdown

---

**取號**（`W-G.9-384 §零-1`）：本批取 `620`（`1` 號）——`W-G.9-383` 補令一 `§一` 裁五之預留（「擬 `620`·候鑄·併次單」）。

### 🩸 `自誤 620`　**`W-G.9-383` 規格單 `R-3` 定「帶標記」之受詞為入池閘之輸入之 build 之片（`_inb965`），而未及手冊先行之「入池閘之合併單元之取代」（以單元代宿主、自 build 去其成員）——再試成而受併之片為同地主他宗之單元之成員（非宿主）者，取代之後其標記隨之失（CC 之唯讀獨立審查 #13·停機上呈）**

**形**：原單 `R-3` 逐字（節錄）「「**帶標記**」＝ 宗之成員中有**輸入之 build** 之片（`_inb965`）帶標記之鍵且其值為真」；原單塊 `K23` 四之戊（再試成者之標記於其後之試算存續）；CC 之停機報告 `docs/reports/W-G.9-383R_工項二停機上呈_唯讀審查之發現.md`（#13）：受併之片 `L` 為他宗之單元之成員時，手冊先行之單元之取代自 build 去 `L`，其標記隨之失。
**後果之界**：零土地後果（本案之再試三筆二退縮皆未成 ⇒ 無片帶標記）；他案：受併之片為成員者，其後同街廓同地主配不到之他宗可依第 `1` 步捲入之（違 `K-9-75` ①）——`W-G.9-383` 補令一 `R-12` 補之（入主線之前）。
**根因**：定受詞（「帶標記」）唯循入池閘之讀之一路（輸入之 build），⛔ 逐一列出生產碼中改 build 之成員之他處（手冊先行之單元之取代·`git grep -n -F "['units'][" -- app.py` 恰一列）；量測器之例皆以受併之片為宿主（單元 ＝ 其 dict 之深拷貝 ⇒ 標記本即存續），⛔ 造成員之形。
**後果之框**：🟢 CC 之唯讀獨立審查（附則丙·工項二之推前）捕之 ⇒ 停機款 `12`·停機上呈（`51ca5d8`）。
**裁**：`W-G.9-383` 補令一 `§一` 裁一（`R-12`·停機報告四之第二形·由二：第一形〔自片之表讀之〕於畫面之入池閘⛔ 有效）、裁五（本號）；`F23` `K60`（成員之形·補令一）與 `K69`（取代未成之形·`W-G.9-384`·審查 #9）補其例。
**攔法**：凡以「某鍵存續於其後之試算」為規格者，以 `git grep` 逐一列出生產碼中自 build 去片、以他物代宗之處，逐處定其鍵之去留；量測器之例須含受詞為宿主與為成員之二形，及取代成與未成之二支。
````

## 附錄丁　塊 `P37`（附於 `CLAUDE.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`W-G.9-383` 入主線；`K-9-71` 入新側支；`K-9-78` 之立（調配之鍵併入 G 值迭代·甲）；`自誤 620`；審查 #9 之例（`W-G.9-384`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`（`W-G.9-383` 補令二 工項一）之後；本批之碼在新側支 `verify/W-G.9-384-k971`。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-73` ④；`K-9-75`〜`K-9-77`；唯註之二處（C-1）；`R-12`（前節序 `3`〜`5`） | 入主線（KL `2026-10-15 14:40`·`W-G.9-383` 補令二之快轉·主線 `fffa397`） | ✅ | `K-6` 典 `W-G.9-384` 之節之一 |
| `2` | `K-9-71`（前節序 `7`·`K-9-73` ⑧） | 依手冊、依距離併入同地主他處已配得之宗（段三後處理之第 `5` 項之輪、手冊先行之 `K-9-51` 之輪）：建地 ⇒ 本街廓者恆先；他街廓者依五級與深度（`k971_key5`）→ 距離 → `k967_rank`；道路、公設地上者照距離；五級之屬性 ＝ 調配之名單之同一處（`k971_blk5`·二回呼之 `blk5`·唯於須比時取之） | 🔶（新側支·候入主線之請示） | `K-6` 典 `W-G.9-384` 之節之三；`docs/orders/W-G.9-384_規格單.md` |
| `3` | `K-9-78` | 調配之畫面入口：新調配程式落地後，「執行七級調配」之鍵去之、併入「執行 G 值迭代計算」一按跑完（各段之紀錄逐段展開可查）；其前畫面⛔ 動——「🔧 待落地清單之補登：調配階段之諸裁」節（`W-G.9-332`）之「改接新程式」依之讀 | ⬜ | 落地之單 ＝ 新調配程式之規格單（規格步 `5`〜`8`） |
| `4` | `自誤 620` | 見自誤簿 | ✅ | 同序 `2` |
| `5` | `W-G.9-383` 補令一之審查 #9（覆蓋之缺） | `F23` `K69`：標記之聯集非空而單元之取代未成 ⇒ 當下之態⛔ 變 | ✅（量測器·新側支） | 同序 `2` |
| `6` | `K-9-74`（前節序 `8`） | 臨街地特別負擔之路寬 | ⬜ | 落地之單 **`W-G.9-385`**（前置 ＝ `K-9-62` 之抵充地之欄） |
| `7` | `GB-205`（前節序 `9`） | `K-9-61` ⑤ 之還原之機制（手冊先行之部分仍待） | ⬜ | 另單 |
| `8` | `K-9-59`〜`K-9-63`（前節序 `10`） | — | ⬜ | 落地之單（其序另呈 KL） |
| `9` | 畫面於 step G 之後再跑段三而未再跑 step G 者之調配之輸入之顯示（前節序 `11`） | 審查者之警示·可達與否未驗·⛔ 鑄號 | ⬜ | 待查（另單·⛔ 急） |
| `10` | 清冊之顯示（前節序 `12`） | 清冊依原地號合併顯示，與配地時之合併不一定相同；核對時以暫編地號為準 | ⬜ | 另單（⛔ 急） |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：`W-G.9-382` 入主線；……（`W-G.9-383`）」節之序 `3`、`4`、`5` ⇒ 本表序 `1`（✅）；其序 `7` ⇒ 本表序 `2`（🔶）；其序 `8`〜`12` ⇒ 本表序 `6`〜`10`（態⛔ 變）；其序 `1`、`2`、`6` ✅ ⇒ 本表⛔ 載。本表序 `3`、`4`、`5` 為新。
🔒 **本案之量**：本批⛔ 變配地（`K-9-71` 於本案⛔ 觸：二退縮之段三後處理之第 `5` 項、末端塊合併再試之第 `5` 項、手冊先行之 `K-9-51` 之輪皆無片·`W-G.9-384` 規格單 `§一` 項 `5`）。
🔒 **依賴序**：序 `2`（`W-G.9-384`·入主線之請示）→ 序 `6`（`W-G.9-385`·其前置 `K-9-62` 之抵充地之欄）→ 序 `8`（其序另呈 KL）→ 規格步 `5` → `6` → `7`／`8`（新調配模組·其畫面入口依序 `3`）；序 `7` 於序 `8` 之前或併之；`GB-196`、`GB-197`、`GB-198`、`GB-202` 與序 `9`、`10` 另單（⛔ 急）。
🔒 **本機介面**：同前節（⛔ 變）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `10`（子字串框·含圖例與本列）·列 ＝ `8`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: 5ac5dd16e7a1283643c8a99536b5d225da20d22a0a92c5b918ae710ef8017bfa
