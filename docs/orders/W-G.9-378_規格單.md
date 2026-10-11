# `W-G.9-378`　規格單：`GB-204` ① 之落地（段三、手冊先行、第一趟之重劃前面積之表減同一試算之入池閘之帳）＋ `GB-204` ② 之不可達之判 ＋ 舊註之改述（`W-G.9-373R` NOTE `1`）＋ 量測器之期之更新（`F27` 之 `B4`〜`B6`／`Y8`／`Y9` 與 `mutate` 之出艙碼〔`自誤 605`〕、`F28` 之 `D1`〜`D3`、五器之期）＋ 自誤 `605`／`606` ＋ 待落地清單之更新（新側支 `verify/W-G.9-378-gb204`）

> **本單建議等級 ＝ `high`**（生產碼 `2` 檔：`app.py` 之二新純函式與六函式之改〔`§三-2`〕；`verify/selection_pipeline.py` 之二函式之改；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單側窗八十·`2026-10-11`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-378-gb204`**，其起點 ＝ 主線之端 `02cc0cb`）。
> **流程 ＝ 規格單**（常態·附則甲〜丙施行）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `Fw14`／`Fw17`／`Fw23`／`Fw24`／`Fw25`／`Fw27`／`Fw28`·CC ⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之二生產碼檔之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `2` 檔；**本案之配地⛔ 變**——本案之入池閘無依手冊部分併入之宗 ⇒ 五處之試算之 `pool_out` 恆空、四表⛔ 變〔`§一` 項 `6`〕；`GB-204` ① 之行為由量測器 `F28` 之 `D1`〜`D3` 之合成對照量之）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」；發單側已自跑其二態·`§一` 項 `8`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `02cc0cb8e83a966f6193c41b02c6093e59f74f84`（`W-G.9-377` 工項三）；側支 `verify/W-G.9-375-k965` ＝ `96bd6fe5daa32bbbb82564f733e5ec875cd740ab`、`verify/W-G.9-373-k966` ＝ `cf08e23f11b3193a0bc2657bf7964562615ab5df`、`verify/W-G.9-370-selfchk` ＝ `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`、`verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`（皆⛔ 動）；遠端 heads `39`。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-378-gb204`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `Fw14`／`Fw17`／`Fw23`／`Fw24`／`Fw25`／`Fw27`／`Fw28`／`G13`／`E21`／`P31` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`自誤 479`）；Bash 之輸出路徑一律單引號之絕對路徑（`W-G.9-373` 補令二單首）。Bash 命令⛔ 含 heredoc（常設規則索引）。`<O>` ＝ CC 自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列（近例之形·`Co-Authored-By` 等）；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-378_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者照實載於報告（KL 日後同步主 checkout 時，依 `docs/orders/W-G.9-371_中量單.md` 工項三之撞檔前置處置·`自誤 542`）。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限**：各驗之命令得並行，唯 `parity`、`k6s3 run`、`F23 run`、`F24 run`、`F27 run`、`F29 run`、`F16 run`、`F14 run`、`F10 run`、`F8 run`、`F9 run`、`F21 run`、`F26 run`、`failclosed`、`F19 mut`、`F22 mut`、`F27 mutate`、`F25 mutate` 之同時並行數 ≤ `2`；逾時者，於⛔ 他負載之下重跑一次，首趟之出艙照實入報告。
> 🔑 **撰碼中之自跑**：CC 撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之頂層節點除 `§三-2` 所列之八者外之一字；`verify/selection_pipeline.py` 除 `_k6b_callbacks`、`run_k953` 外之一字；生產碼 `34` 檔之其餘 `32` 檔（含 `verify/stepg_pipeline.py`、`verify/run_verification.py`）；`k929_6_fixpoint`、`adj_intake`（`R-4`）之一字；`§三-3` 之禁改；既有量測器除塊 `Fw14`／`Fw17`／`Fw23`／`Fw24`／`Fw25`／`Fw27`／`Fw28` 所改之七檔外之一字；`verify/case_params_UC9898.json`、`verify/case_front_road_names_UC9898.json`、`verify/baselines`、`verify/out/`；`K-6` 典、`VR` 簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`GB` 簿、自誤簿、`CLAUDE.md` 除塊 `G13`／`E21`／`P31` 之純末端追加外之一字；任何他側支（含 `verify/W-G.9-375-k965`、`verify/W-G.9-373-k966`、`verify/W-G.9-370-selfchk`、`verify/W-G.9-367-adj4`）之推送、刪除或改寫；KL 主 checkout；`K-9-58` ④（`N0-9` 之擴）、`K-9-59`〜`K-9-63`、`W-G.9-375` 之【工】巳之三停機、規格步 `5`〜`8`、`GB-196`〜`198`／`202`。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `02cc0cb8e83a966f6193c41b02c6093e59f74f84`；四側支之 `git rev-parse` ＝ 單首之值；`git ls-remote --heads origin` 之列數 ＝ `39`（全 `39` 列存 `<O>\heads_before.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-378-gb204`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 604 603` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `589`／`MAX` `604`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `196`／`204`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `67`／`70`／`[44, 47]`（＝ `W-G.9-377` 收工閘 `7` 之期·發單側窗八十於 `02cc0cb` 重跑同）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態 `02cc0cb` 之 `docs/` 全檔 **`1006`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗八十實跑 `python verify/probes/wg9268_gate6_occupancy.py 02cc0cb W-G.9-378 W-G.9-377 W-G.9-397`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-378`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取（器另示「鬆框亦 `0` ⇒ ⛔ 漏框之虞」：`W-G.9-377` 唯稱「`GB-204` 之落地之單」·⛔ 書其號） |
| 對照甲［必非零］`W-G.9-377` | `2`／`4`／`5` | `2`／`4`／`5` | `9` | `2` | `3`／`42` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-397` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `22`／`34` | 🟢 宣告框之嚴格 `0`、鬆框非零（器之標籤「甲（須 ≥1）」依本表之角色讀之·同 `W-G.9-365R` ⑥ 自解 `1`） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`6` | `0`（寬式 `6`） | `0`（寬式 `3`） | `50`／`55` | 🟡 寬式 `D3` 非零：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `02cc0cb` 之追蹤檔 **`2831`** 檔·列框；發單側窗八十以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``〕於 `02cc0cb` 實算）：

| 號 | 裸（錨定）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 605` | `1115` | `0` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——`sha256`／blob／`commit` 之子字串、行號、bytes、面積等；其列之含「自誤」者唯 `docs/reports/W-G.9-205R_二檔入倉與VR088與自誤255_執行報告.md:40`〔blob 之子字串〕） |
| `自誤 606` | `217` | `0` | `0` | `0` | 🟢 可取（同上；其列之含「自誤」者皆面積〔`55.606`〕、blob 之子字串、行號〔`run_verification.py:606`〕） |
| 對照甲［必非零］`自誤 604` | `51` | `13` | `0` | `11` | 🟢 框非恆空 |

**塊名、新名**（母體同上·檔框／列框·`git grep -l`／`git grep -c` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fw14`／`Fw17`／`Fw23`／`Fw24`／`Fw25`／`Fw27`／`Fw28`／`G13`／`E21`／`P31`（逐名） | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`G12` | `2`／`5` | `2`／`12` | 🟢 框非恆空 |
| 對照甲［必非零］`E20` | `2`／`8` | `2`／`13` | 🟢 框非恆空 |
| 對照甲［必非零］`P30` | `2`／`8` | `2`／`15` | 🟢 框非恆空 |
| 報告名 `W-G.9-378R`、新側支之名 `W-G.9-378-gb204`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |
| 新名 `k967_pool_out`、`k967_pool_less`、`pool_out`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名 |

🔒 `Fv27`〜`Fv29` 已為 `W-G.9-377` 之塊名 ⇒ 本單之量測器之塊名用 `Fw`。

自誤 `MAX` ＝ `604`、`GB` `MAX` ＝ `204`、`K-9` `MAX` ＝ `70`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 605`、`606`（塊 `E21`）；⛔ 鑄 `GB`／`K-9`／`VR`（`GB-204` 之進度節〔塊 `G13`〕⛔ 鑄號）。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `02cc0cb`，或四側支之任一 ≠ 單首之值，或遠端 heads ≠ `39`、或已含 `refs/heads/verify/W-G.9-378-gb204`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fw14`／`Fw17`／`Fw23`／`Fw24`／`Fw25`／`Fw27`／`Fw28`／`G13`／`E21`／`P31` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或七個 `diff` 塊之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `10` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-378-gb204`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線、四側支於本批中有任何推進 |
| `8` | 工項三之三簿（`GB` 簿、自誤簿、`CLAUDE.md`）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或 CC 認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中（⛔ 加 `--no-index` 者對已追蹤之檔恆不報·⛔ 用） |
| `12` | 工項二之唯讀獨立 reviewer（附則丙）之發現涉域上判斷或規格之漏載 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `13`。

---

## `§一`　態錨（發單側窗八十自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`·Python `3.13.16`·`numpy 2.4.6`〔`GB-198`〕·`shapely 2.2.0`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `02cc0cb8e83a966f6193c41b02c6093e59f74f84`（`a3925f1` 之後四筆：`2aa9c03` 工項零 → `2167167` 工項一 → `cce6067` 工項二 → `02cc0cb` 工項三·`W-G.9-377`）；四側支 ＝ 單首；遠端 heads **`39`**；追蹤檔 `2831`；`app.py` ＝ `d6218273e0ba3cdf45598a37968eac6d907ebb58`（`1785667` B）、`verify/selection_pipeline.py` ＝ `96cbf3ffbdd36bbf4d02bf10e9635bbf69b5926c`（`58320` B）、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`（`121758` B）、`verify/run_verification.py` ＝ `f5b896e5a702c5d958e3ba27091d27832385efc4`、`verify/run_all.py` ＝ `e5cf9a224517533b183b34e4fd0f5fbe35ee406b`；本批所改之七器之施前 blob ＝ `§五-1` 項 `2`〜`8`；`GB` 簿 ＝ `7d56b5328c2c3968b9425992544848d92f70a503`（`1054032` B）、自誤簿 ＝ `4b8e995b6d1cd45f4f17da5479427e00d10d974c`（`1167087` B）、`CLAUDE.md` ＝ `ccb5269d17bf8527edb529bebb29efb87919c8ab`（`380931` B）、`K-6` 典 ＝ `5fab239a68b58ef042d38d7a731eb8b5eade5f03`（`684846` B·本批⛔ 動）；皆以換行結尾·CR `0`（判別力：`data/V6.dxf` ＝ `12308`） |
| `2` | `GB-204` 之受詞（`02cc0cb`·＝ `96bd6fe`） | 四表：`k6b_stage3_run` 之 `_pa`（`app.py:14847`·段三之第 `5` 項）、`k953_manual_run` 之 `_pre953`（`:15398`·計畫時·首次之試算 `C0`）與 `_pre951`（`:15844`·`K-9-51`）、`adj4_pass1_run` 之 `_pre_a4`（`:16302`·第一趟之各輪）——皆「分攤登記面積 − `段三部分併出` 之和」，⛔ 減入池閘之帳（`入池閘部分併出`／`入池閘成員部分併出`·`W-G.9-375` 規格單 `R-8` ③）；入池閘之內之重劃前面積已減之。五處之試算（`§三` 之用語）皆以 `k953_units_of(<末態之 build>)` 回 `members`（`app.py:22165`、`:22318`、`:16033`；`verify/selection_pipeline.py:761`、`:853`），⛔ 回入池閘之帳 |
| `3` | `GB-204` ① 之實量（`F28` 之 `D1`〜`D3`·工項一之端 ＝ `02cc0cb` ＋ 七個 `diff` 塊） | 工項一之端：`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['D1', 'D2', 'D3']；rc 1`——`D1` 得 `K-9-51` 之表 `X(1)` `5.6897`、計畫時之表 `X(1)` `55.0`（期 `3.6897`／`54.0`）；`D2` 得第 `2` 輪 `25.0`、第 `1` 輪 `55.0`（期 `23.0`／`54.0`）；`D3` 得 `65.0`（期 `63.0`）——三處之表皆⛔ 減其試算之入池閘之帳（差 ＝ 該試算之帳 `1` 或 `2`；無帳之 `Y(1)`／`Z(1)` 同期）；`L1`〜`L6` 等既有之例皆 ✅、`P0` `29／29`。期值手算（塊 `Fw28` 之各函式之說明文） |
| `4` | 原型（發單側窗八十·倉外·`02cc0cb` ＋ 七個 `diff` 塊 ＋ `§三` 之一實作·⛔ 為 CC 之期） | 原型之 `app.py` ＝ `ea3855a39ead0ace0253f3eb619a96ecf6b49401`（`1788414` B·對開工態 `+52`／`-7`）、`verify/selection_pipeline.py` ＝ `a9bf6eb0acbe5f8caff5e41189d78e63cc4e80a2`（`58794` B·`+8`／`-4`）——皆⛔ 為期；其頂層節點對 `02cc0cb` 之相異 ＝ `§三-2` 之八者與二者（增 `k967_pool_out`、`k967_pool_less`；改 `k6b_stage3_run`、`k953_manual_run`、`adj4_pass1_run`、`adj4_trial_state`、`k6b_screen_callbacks`、`f3_screen_k953`；`_k6b_callbacks`、`run_k953`）。`V-1`〜`V-3` 之諸器（同 `§四-1` 之命令）於原型皆 `rc 0`，其末列 ＝ `§五-1` 項 `12` 之施後之列；`V-4` 之 `cmp`（對工項一之端之同器之出艙）相異 `0` 項、`V-5`／`V-6` 之落檔逐位同；諸器之 `stderr` 合計 `0` B。判別力：見項 `7`。本單之前稿另經二輪唯讀獨立審查（倉外·未參與撰寫者），其所指皆處置：`Y8` 之漏（手冊先行之二試算之鍵名改之而諸器皆綠）⇒ 增「呼叫直書為 `return` 之鍵 `pool_out` 之值」之判（塊 `Fw27`·`R-2` 明書其形）；`R-1` 之帳空之成員 ⇒ 與 `adj_intake` 同略之、增 `B4` 之例；`R-6` 之七 docstring 之舊述 ⇒ 各增一列；`V-8` 之判別力 ⇒ 入前置 `4`；`R-3` 之停機之序 ⇒ 明書；`§一` 項 `5` 之射程（單趟）與二旁事 ⇒ 明書、其一列待查（塊 `P31` 序 `9`）；收工閘 `3` 之受詞 ⇒ blob；`§五-1` 項 `12` 之呼叫數、塊 `P31` 之態、並行之限 ⇒ 改正。原型之值皆為補後之值 |
| `5` | `GB-204` ② 之判（`02cc0cb`·倉外實查·`自誤 606`） | **單趟之管線之序**（末次之調配之輸入）：調配之輸入之 build ＝ 末次入池閘之出：畫面之 `SS_ADJ_BUILD_FINAL` 全檔唯一之寫在 `f3_screen_stepg_run` 之入池閘之關之後（`app.py:21825`·該關之呼叫 `:20325`）；畫面之 `main` 先跑段三（含末端塊合併再試、手冊先行、第一趟·`f3_screen_k6b_stage3` `:28236`），後跑 step G（含入池閘·`f3_screen_stepg_run` `:28613`）；harness 之 `main`（`verify/run_verification.py`）先 `run_corner_pk_k6b`（`:610`），後以其出之 build 跑 `run_step_g`（`:691`）⇒ 手冊先行等皆在末次入池閘之**前**；末次入池閘之後、調配之輸入之前⛔ 有去出 build 之步 ⇒ `GB-204` ②（「該片其後為下游〔手冊先行等〕整筆去出 build 者，其入池閘之帳⛔ 達調配之輸入」）於現行管線**不可達**；三處之試算中之入池閘之帳唯及其試算（⛔ 達調配之輸入·亦⛔ 須達）。其守 ＝ `F27` 之 `Y9`（工項一之端已綠·以源碼之序量之·⛔ 量控制流；管線之序或調配之輸入之 build 之源變 ⇒ 紅·`§一` 項 `7`）；`adj_intake` ⛔ 改（`R-4`）。另二事（皆非 ②·唯讀獨立審查所指）：規格步 `4` 乙（第一趟）之輸入之試算亦於其試算之入池閘之出上跑調配之輸入（`verify/selection_pipeline.py:929`）——其間亦⛔ 去出 build 之步；畫面於 step G 之後再跑段三而未再跑 step G 者，`SS_ADJ_BUILD_FINAL` ⛔ 清（唯 step G 之始清之·`app.py:20360`；段三之始唯清 `K6B_SCREEN_STAGE3_KEYS`·`:21949`／`:22473`），調配之輸入之顯示（`:28705`、`:28737` 等）或配前次之 build——既有之事、本單⛔ 及、未驗其可達，列入待查（塊 `P31` 序 `9`） |
| `6` | 本案之量（原型·harness 與畫面·二退縮） | 原型對工項一之端（二退縮·同命令）：`k6s3 cmp` 相異 `0` 項；`F8 run` 之落檔（`rows` `35`／`36`、入池閘之紀錄 `2`／`2` 列）**逐位同**；`parity` 之落檔逐位同、其 `stdout`（工作樹之路徑代以同一字樣後）逐位同——配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`；手冊先行之紀錄 `34`／`43` 列、第一趟 `1`／`1` 列、段三 `19`／`0` 列、段三後 build `45`／`46` 宗；`Z`（一側獨有之零面積池列）＝ `[('harness', 'R1-抵費地-2')]`（二退縮）；`F23 run`／`F24 run`／`F27 run`／`F29 run`／`F16 run`／`F14 run`／`F10 run`／`F21 run`／`F26 run`／`F9 run`／`failclosed` 之 `stdout` 亦逐位同（唯路徑）⇒ **配地⛔ 變**（`R-7`·`V-4`〜`V-6`）。**`pool_out` 恆空之實量**（倉外·原型之 `k967_pool_out` 包一層記其回傳之長）：`k6s3 run` `3.5 m` `13` 次、`0 m` `9` 次；`parity`（harness 與畫面）`3.5 m` `26` 次、`0 m` `18` 次——皆 `{}`（本案入池閘無依手冊部分併入之宗）。🔒 `probe_WG9375_k965.py cmp8` 係 `W-G.9-375` 之施前施後之比（其期 ＝ 施後之紀錄增「步」）·二態皆已有「步」⇒ 本批⛔ 用（`V-6` 以落檔之 blob 之同代之） |
| `7` | 判別力（發單側窗八十·倉外·原型之上逐一撤一處之改·量 `F28 selftest`、`F27 wiring`、`F14 selftest`、`F17 wiring`、`F24 selftest`） | 原型之上逐一撤一處之改或改其形（`20` 種·倉外之器）皆有其項轉紅：四表之減各撤 ⇒ `F28` 之 `D3`（段三）、`D1`（計畫時）、`D1`（`K-9-51`）、`D2`（第一趟）；`K-9-51` 之表改減 `C0`（他次之試算）之帳 ⇒ `D1`；五處之試算之 `pool_out` 各撤 ⇒ `F27` 之 `Y8`（另：畫面之段三 ⇒ `F14` 之 `T3d`／`T6d`／`T9d` 與 `F17` 之 `W8`；harness 之段三 ⇒ `W8`；第一趟 ⇒ `F24` 之 `K20`）；畫面之段三之 `pool_out` 改取試算之 build ⇒ `Y8`；手冊先行之二試算之 `pool_out` 改鍵名（`pool=`／`pool_x=`）⇒ `Y8`；harness 之段三之 `pool_out` 回空而其呼叫置於他鍵 ⇒ `Y8`、`W8`；畫面之手冊先行之 `pool_out` 回空而其呼叫置於他 `dict` ⇒ `Y8`；第一趟之呼叫先存於變數而後回（`R-2` ⛔ 許之形）⇒ `Y8`；`k967_pool_out` ⛔ 計成員之帳 ⇒ `F27` 之 `B4`／`B5`；帳空之成員⛔ 略 ⇒ `B4`；`k967_pool_less` 就地改表 ⇒ `B6`；harness 之 step G 之 build 改取他物（`verify/run_verification.py:692`）⇒ `Y9`。`F27 mutate` 於原型 ⇒ `rc 0`·末列逐字 `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（`57` 種之錨皆恰一見·`R-3` 之「其後另一句」使然）。出艙碼之分（`自誤 605`）：工項一之端（基準⛔ 全綠）⇒ `rc 3`·末列逐字 `⇒ 突變 57（另基準一）；紅 []；無從判定 ['N00']；rc 3`；原型之 `N01` 之錨之列末附一註（錨 `0` 見）⇒ `rc 3`·`無從判定 ['N01']`（餘 `56` 種與基準皆 ✅）。🔒 `Y8` 之「呼叫直書為 `return` 之鍵 `pool_out` 之值」與 `B4` 之帳空之成員、`R-6` ② 之七 docstring 之增列，係本單之前稿經唯讀獨立審查後所補（`§一` 項 `4`） |
| `8` | `run_all`（發單側窗八十·倉外之拋棄式 worktree·Linux） | 拋棄式 worktree（工項一之端；原型之前稿與定稿）·Linux·各跑 `python verify/run_all.py` 一次（各約 `36` 分）：皆 `rc 1`、`stderr` `0` B；其 `stdout` 以工作樹之路徑代以 `<W>` 後三者**逐位同**（`229150` B·`sha256` `1bb5b0c3c69bacc32f848336c4f1d7484b4c70619e127c3c81f3340311152b69`·`RESULT: FAIL` 既有·名目 凍存 `22`／現況 `36`）⇒ 本批於 `run_all` 之出艙⛔ 變 |

---

## `§二`　KL 之語與射程

🔒 **所據**（`GB` 簿·逐字·開工態 `02cc0cb`）：`GB-204` 之立項節之「失效條件」：「四表皆依 `_pre965` 之式減入池閘之帳（`入池閘部分併出` 與單元之 `入池閘成員部分併出`）；調配之輸入之帳兼及其後為下游去出 build 之片（或下游去出時保其帳）；量測器以合成之例量此二項（含其「⛔ 改」之對照）。」；「排程」：「另單（生產碼·⛔ 新域問：`K-9-69` 已裁）；於 `K-9-58` ④〜`K-9-63` 之落地之單之前」。`CLAUDE.md` 待落地清單 `W-G.9-377` 之節之序 `4`（`W-G.9-373R` NOTE `1`·舊註）、序 `5`（`GB-204`）。`K-9-69`（`K-6` 典·KL 已裁）：部分併出之剩下所含者唯其剩下。

🔒 **KL 之語**（逐字·`2026-10-11 15:11`·發單側窗八十請 KL 附主 checkout 之出艙之答）：

> C:\Users\admin\Desktop\land-readjustment-trial>git -C C:\Users\admin\Desktop\land-readjustment-trial log -1 --oneline
> 02cc0cb (HEAD -> wip/s1-endpart, origin/wip/s1-endpart) W-G.9-377 工項三：執行報告入倉 ⛔ 零生產碼

🔒 **發單側窗八十之通知**（皆於對話·其文之此段逐字）：
- `2026-10-11 15:04`（`W-G.9-377` 之復驗之通知·KL `15:11` 之訊之前·KL ⛔ 駁）：「**處置**：登記為發單側自誤 `605`。下一張 `GB-204` 的單本來就要更新這支程式，屆時一併改正，不另出單。」⇒ 塊 `Fw27` 之 `mutate` 之出艙碼、塊 `E21` 之 `自誤 605`。
- `2026-10-11 15:16`（KL `15:11` 之訊之後·本單擬定時 KL ⛔ 駁；交單之通知再陳之）：「2. **不會發生**：原本擔心「某宗被排配地部分併出後，又被手冊先行等步驟整宗移走，以致調配時查不到它的去處」。」「這件事是上一窗登記時沒有核對流程先後所致，我會登記為發單側自誤。」「本單另加一道檢查：日後若有人調動流程順序，檢查會亮紅。」「本單打算的內容：」「- 修第 1 件；」「- 改那句過時的註解；」「- 修正上一單驗證程式「算不出來」與「判定有錯」共用結果碼的問題。」⇒ `§三`（`R-1`〜`R-3`、`R-5`）、`R-4`（② ⛔ 改碼）、塊 `Fw27` 之 `Y9`、塊 `E21` 之 `自誤 606`。

🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 之畫面核對與逐字放行**。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支（附則甲〜丙）；`(c)` ⛔ 及主線、他側支、KL 主 checkout、入池閘（`k929_6_fixpoint`）、調配之輸入（`adj_intake`）、`K-9-58` ④、`K-9-59`〜`K-9-63`、`W-G.9-375` 之【工】巳、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**：
- 「**入池閘之帳**」＝ 入池閘（`k929_6_fixpoint`）所寫於其末態之 build 之二鍵（`W-G.9-375` 規格單 `R-8` ③·既有·⛔ 變）：宗上之 `入池閘部分併出`（該宗之暫編地號之片之帳·`{受併宗: 來源量}`）、單元上之 `入池閘成員部分併出`（`{片: {受併宗: 來源量}}`）。
- 「**試算**」＝ 下開五處之試算之函式（其回傳既有 `members`）：(a) `app.py` 之 `k6b_screen_callbacks` 之巢狀 `alloc_state`（段三·畫面）；(b) `verify/selection_pipeline.py` 之 `_k6b_callbacks` 之巢狀 `alloc_state`（段三·harness）；(c) `app.py` 之 `f3_screen_k953` 之巢狀 `_trial953s`（手冊先行·畫面）；(d) `verify/selection_pipeline.py` 之 `run_k953` 之巢狀 `_trial_k`（手冊先行·harness）；(e) `app.py` 之 `adj4_trial_state`（第一趟·二入口共用）。其「**末態之 build**」＝ 各處既有之 `k953_units_of(…)` 之引數（入池閘之末態 build；無則試算之 build）。
- 「**四表**」＝ 重劃前面積之表（`K-9-67` 之比較·`k967_pre_area` 之 `area_of`）：(甲) `k6b_stage3_run` 之 `_pa`（段三之第 `5` 項·配對之試算 ＝ `_cur`）；(乙) `k953_manual_run` 之 `_pre953`（計畫時·配對之試算 ＝ `C0`）；(丙) 同函式之 `_pre951`（`K-9-51`·配對之試算 ＝ `_cur`）；(丁) `adj4_pass1_run` 之 `_pre_a4`（第一趟之各輪·配對之試算 ＝ `_S`）。「配對之試算」＝ 其表之所據之態之同一次試算之回傳（`W-G.9-373` 補令二 `R-19″`·既有·⛔ 變）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | `app.py`·新頂層函式二（緊接 `k967_pre_area` 之後） | ① `def k967_pool_out(build_final):`——回 `{片: 已併出之量}`：`build_final` 為 `None` 或空 ⇒ `{}`；其每一元素 `u`（依序）：若 `u` 之 `入池閘部分併出` 非空 ⇒ 片 `str(u['暫編地號'])` 之量 ＝ 其值之和；`u` 之 `入池閘成員部分併出`（缺 ⇒ `{}`）之每一 `(片, 帳)`：帳非空 ⇒ 片 `str(片)` 之量 ＝ 帳之值之和（帳缺或空 ⇒ 該片⛔ 列·同自身之帳之空者·其減量與 `adj_intake` 之帳之表同〔帳空者量 `0`〕）。同一片見於二處（二元素、或一元素之自身與其成員）⇒ `RuntimeError`（訊息含「`GB-204`」與「二處」）；任一片之量⛔ `> 0` ⇒ `RuntimeError`（訊息含「`GB-204`」與「≤ 0」）。⛔ 改其輸入。② `def k967_pool_less(area_of, pool_out):`——`pool_out` 為 `None` ⇒ 視為 `{}`；非 `dict` ⇒ `RuntimeError`（訊息含「`GB-204`」與「`pool_out`」）；其鍵⛔ 在 `area_of` 者 ⇒ `RuntimeError`（訊息含「`GB-204`」與「不在重劃前面積之表」）；回**新** `dict` ＝ `{p: float(area_of[p]) − float(pool_out.get(p, 0)) for p in area_of}`（鍵與其序同 `area_of`）；⛔ 改 `area_of`。 |
| `R-2` | 五處之試算（用語 (a)〜(e)） | 其回傳於 `members` 之外另回 `pool_out` ＝ `k967_pool_out(<末態之 build>)`，其引數之式與同一函式之 `k953_units_of(…)` 之引數之式**逐 AST 同**（harness 二處以 `ns["k967_pool_out"]` 呼之）。以字面 `dict` 回傳者（(a)、(b)）其鍵 `'pool_out'`（(b) 為 `"pool_out"`）緊接 `members` 之後（為第六鍵）；以 `dict(…)` 回傳者（(c)、(d)、(e)）增關鍵字引數 `pool_out=`。`k967_pool_out(…)` 之呼叫**直書於該函式之 `return` 之式中**為其鍵之值（⛔ 先存於變數而後回之·⛔ 置於他 `dict`——`F27` 之 `Y8` 以之為形）。`k967_pool_out` 之呼叫於 `app.py` 與 `verify/selection_pipeline.py` 合計恰 **`5`**（即此五處）。他鍵與其值⛔ 變。 |
| `R-3` | 四表（用語 (甲)〜(丁)） | 各於其既有之建表之句（**逐字留之**·`§三-3` ①）之後，緊接一句重綁其表 ＝ `k967_pool_less(<表>, <配對之試算>.get('pool_out'))`（例：`_pa = k967_pool_less(_pa, _cur.get("pool_out"))`）；其後之一切用表之處（`k967_pre_area` 之呼叫等）⛔ 變；既有之「試算中止」之停機之檢（如 `adj4_pass1_run` 之 `_S.get('err')`）之位置⛔ 移——其試算中止而 `pool_out` 之算或減先觸 `GB-204` 之停機者，照實停機（二者皆停機·⛔ 改其序）。`app.py` 中子字串 `k967_pool_less(` 恰 **`5`** 見（定義 `1` ＋ 此四句·各在不同之列；docstring 與註⛔ 書此子字串）；`verify/selection_pipeline.py` 中 `0` 見。 |
| `R-4` | `adj_intake`、`k929_6_fixpoint` | ⛔ 改（`GB-204` ② 不可達·`§一` 項 `5`）。 |
| `R-5` | `adj4_pass1_run` 之 `_rkey_a4` 之上之註（`W-G.9-373R` NOTE `1`） | 其「重劃前面積〔成員之輸入之分攤登記面積〕」改述為現行之式（本輪之表 `_pre_a4`〔分攤登記面積 − `段三部分併出` 之和 − 同一試算之入池閘之帳〕之成員之和）；改後 `app.py` 中子字串「成員之輸入之分攤登記面積」`0` 見（`02cc0cb` 中恰 `1` 見·`:16334`）。唯註·⛔ 改碼。 |
| `R-6` | docstring 與註 | ① 二新函式各有 docstring（述其義與停機·受 `§三-3` ② 之限）。② 下開七函式之 docstring 之末（其閉之 `"""` 之前）**各增一列**（以 ``🔧 `W-G.9-378`（`GB-204`）：`` 起首·述本單之改·其前之文一字⛔ 改）：`k6b_stage3_run`（第 `5` 項之表再減入池閘之帳）、`k953_manual_run`（計畫時與 `K-9-51` 之表同）、`adj4_pass1_run`（各輪之表同）、`adj4_trial_state`、`k6b_screen_callbacks`、`_k6b_callbacks`（回傳另增 `pool_out`·第六鍵）、`run_k953`（同）——其既有之述（「重劃前面積之表之各片 ＝ 分攤登記面積 − `段三部分併出` 之和」「增第五鍵 `members`」等）因本單而不全，以增列補之（`R-5` 同旨）。③ `R-2`、`R-3` 之改處得各以一註述之（同起首）；他處之 docstring 與註⛔ 改。④ 新增之文⛔ 含子字串 `k967_pool_less(`（`R-3`）。 |
| `R-7` | 本案 | 二退縮之配地、街角得標與強制旗標、段三／手冊先行／第一趟之紀錄、入池閘之紀錄、調配之輸入、畫面與 harness 之對拍皆⛔ 變（本案五處之試算之 `pool_out` 恆空·`§一` 項 `6`）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `k967_pool_out`、`k967_pool_less` 之名與簽名 ＝ `R-1`；其行為：`F27` 之 `B4`〜`B6`（`selftest`）。
- 五處之試算之 `pool_out`：`F27` 之 `Y8`（`wiring`·`k953_units_of` 之呼叫恰 `5`，各與同一最內函式中之 `k967_pool_out` 之呼叫之首引數逐 AST 同、且該呼叫直書為該函式之 `return` 之式之鍵 `pool_out` 之值〔`dict(…, pool_out=…)` 或字面 `dict` 之鍵 `'pool_out'`／`"pool_out"`〕；`k967_pool_out` 之呼叫恰 `5`）；`F17` 之 `W8`（(a)(b) 之回傳之鍵·前四鍵之後 ＝ `['members', 'pool_out']`）；`F14` 之 `T3d`／`T9d`／`T6d`（(a) 之回傳之值）；`F24` 之 `K20`（(e) 之回傳之鍵）。
- 四表之減：`F28` 之 `D1`〜`D3`（三處之表·同一試算之配對）；`GB-204` ② 之守：`F27` 之 `Y9`。
- `app.py` 之頂層節點對 `02cc0cb` 相異者 ⊆ `{k967_pool_out, k967_pool_less, k6b_stage3_run, k953_manual_run, adj4_pass1_run, adj4_trial_state, k6b_screen_callbacks, f3_screen_k953}`（後六者唯 `R-2`／`R-3`／`R-5`／`R-6` 之改）；`verify/selection_pipeline.py` ⊆ `{_k6b_callbacks, run_k953}`（`F23` 之 `W6`／`W7`、`F24` 之 `W5`、`F25` 之 `X1`／`X2`／`X4` 依塊 `Fw23`／`Fw24`／`Fw25` 之許量之）。

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **突變之錨**（`F27 mutate`·`MUT377` 之 `N01`〜`N57`）：其錨（`app.py`／`verify/selection_pipeline.py` 之字樣·各須於其函式之區間恰一見）**一字⛔ 動、⛔ 重寫**——四表之既有建表之句（`_pa = {…}`、`_pre953 = {…}`、`_pre951 = {…}`、`_pre_a4 = {…}`）與其後之 `k967_pre_area` 之呼叫皆屬之 ⇒ `R-3` 以**其後另一句**重綁其表、⛔ 改其句。`F27 mutate` 之期：`57` 種皆捕、`無從判定 []`（`V-1`）。
2. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計·含引號）——新 docstring 與停機之訊息⛔ 重寫既有之字樣（例：`'members'`、`'kept'`、`'bad_pools'` 之單引號形於 (a) 之字面 `dict` 之外⛔ 增）。CC 撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
3. `F17 wiring` 之 `W8` 等諸項、`F25 wiring` 之 `X3`／`X5`、`F25 mutate` 之存留之突變之錨、`F10 wiring` 之 `W4`（`SS_ADJ_BUILD_FINAL` 之讀者）、`F27 wiring` 之 `Y1`〜`Y7`、`F29 wiring` 之 `Y1`〜`Y9`（`W-G.9-367`／`370`／`373`／`375 §三-3` 之餘款）⛔ 觸。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`K-9-67`、`K-9-69`、`K-9-70` 已裁；`GB-204` ① 之失效條件已載（`§二`）。撰碼中若見下列任一 ⇒ 停機上呈：四表中有其配對之試算⛔ 可定者；入池閘之帳之片⛔ 在其表（`R-1` ② 之停機）而於本案或量測器之例觸之；須改 `adj_intake` 或入池閘始能滿足 `§三-1`；本案之配地有任一改變。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-6`）：落於何處、其字樣；對 `§三-3` 各款之自查；附則乙之自查（五處之 `pool_out` 與 `members` 之 build 之同一、四表之配對之試算）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/selection_pipeline.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-378-gb204`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-378_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-378 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-378-gb204`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`40`**、主線仍 ＝ `02cc0cb…`、四側支仍 ＝ 單首。其後之工項一律 `git push origin HEAD:verify/W-G.9-378-gb204`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fw14`／`Fw17`／`Fw23`／`Fw24`／`Fw25`／`Fw27`／`Fw28` 各抽為 `<O>\<塊名>.diff`，對拍 `§五-1` 項 `2`〜`8` 後 `git apply --check` ⇒ 過、`git apply`；七檔之 `git hash-object` ＝ `§五-1` 項 `10`；`git diff --numstat` 唯此七檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-378 工項一：量測器之期之更新（F27 之 B4〜B6／Y8／Y9 與 mutate 之出艙碼·F28 之 D1〜D3·F14／F17／F23／F24／F25）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-378-gb204`。

**工項二　生產碼**（🔴 `app.py` ＋ `verify/selection_pipeline.py`·CC 依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`）：
1. 紅（**`rc 1`**·末列逐字 ＝ `§一` 項 `3` 與 `§五-1` 項 `12` 之工項一之端之列）：`python verify/probes/probe_WG9373_k966.py selftest <repo>` ⇒ `⇒ 紅 ['受詞缺']；rc 1`（其前列 `🔴 受詞缺：['k967_pool_out', 'k967_pool_less']`）；`… wiring <repo>` ⇒ `⇒ 紅 ['Y8']；rc 1`（`Y9` ✅）；`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` ⇒ `⇒ 紅 ['D1', 'D2', 'D3']；rc 1`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` ⇒ `⇒ 紅 ['T3d', 'T9d', 'T6d']；rc 1`；`python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` ⇒ `⇒ 紅 ['W8']；rc 1`；`python verify/probes/probe_WG9367_adj4.py selftest <repo>` ⇒ `⇒ 紅 ['K20']；rc 1`；`python verify/probes/probe_WG9370_adj4mut.py mutate <repo>` ⇒ `⇒ 突變 8（另基準一）；紅 ['M00']；rc 1`；另 `python verify/probes/probe_WG9373_k966.py mutate <repo>` ⇒ **`rc 3`**·末列逐字 `⇒ 突變 57（另基準一）；紅 []；無從判定 ['N00']；rc 3`（基準⛔ 全綠·`自誤 605` 之出艙碼之分）
2. 綠（**`rc 0`**·末列逐字 ＝ `§五-1` 項 `12` 之工項一之端之列）：`V-1`〜`V-3` 之其餘之呼叫（同 `§四-1` 之驗之命令）。
3. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`；`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_pre_35.json`；同 `0.0` ⇒ `<O>\f8_pre_00.json`；`python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_pre.json`；同 `0.0` ⇒ `<O>\parity00_pre.json`（皆 `rc 0`）。

4. `git grep -c -F "成員之輸入之分攤登記面積" -- app.py` ⇒ 出艙恰一列 `app.py:1`、`rc 0`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫二檔之改動；`python -m py_compile app.py verify/selection_pipeline.py`；`commit` 訊息之首列逐字 `W-G.9-378 工項二：GB-204 ① 之落地（段三、手冊先行、第一趟之重劃前面積之表減同一試算之入池閘之帳）＋ 舊註之改述 🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>\*_post.*`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9373_k966.py selftest <repo>`；`… wiring <repo>`；`… mutate <repo>`；`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | 皆 **`rc 0`**；`selftest` 之末列逐字 `⇒ 紅 []；rc 0`·`B4`〜`B6` ✅·`P0` `31／31`；`wiring` `Y1`〜`Y9` 皆 ✅；`mutate` 之末列逐字 `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`F28` 之末列逐字 `⇒ 紅 []；rc 0`·`D1`〜`D3` ✅·`P0` `29／29` |
| `V-2` | 塊所改之他五器：`F14`（`probe_WG9355_screenmerge.py selftest`；`run`）、`F17`（`probe_WG9358_k948_wiring.py wiring`）、`F23`（`probe_WG9363_k953.py selftest`；`wiring <repo> 7d8e954`；`run`）、`F24`（`probe_WG9367_adj4.py selftest`；`wiring <repo> d7a5ea4`；`run`）、`F25`（`probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`mutate`）；`F27 run`（`probe_WG9373_k966.py run`） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `12` 之施後之列 |
| `V-3` | 其餘之器（同命令·出艙存 `<O>\*_post.log`）：`F29`（`probe_WG9375_k965.py selftest`／`wiring`／`run`）、`F8`（`probe_WG9349_k9296.py selftest`／`wiring`）、`F4 wiring`（`probe_WG9345_screen.py`）、`F9`（`probe_WG9350_frontroad.py selftest`／`wiring`／`run`）、`F10`（`probe_WG9351_intake.py selftest`／`wiring`／`run`）、`probe_WG9352_endblock.py`／`probe_WG9353_endmerge.py`／`probe_WG9354_endcontest.py` 之 `selftest`／`wiring`、`F15 wiring`（`probe_WG9356_screenmerge_wiring.py`）、`F16`（`probe_WG9357_k948.py selftest`／`run`）、`F18`（`probe_WG9359_cand.py selftest`／`wiring`）、`F19 mut`（`probe_WG9360_cand_mut.py`）、`F21`（`probe_WG9361_k954.py selftest`／`wiring`／`run`）、`F22 mut`（`probe_WG9362_k954_mut.py`）、`F26`（`probe_WG9372_ww.py selftest`／`run`）、`probe_WG9344_k6s3.py selftest`、`probe_WG9344p1_pooltemp.py selftest`、`probe_WG9348_harvest_key.py`、`probe_WG9341_synth.py`、`probe_WG9340_main_synth.py`、`probe_WG9346_failclosed.py run <repo> 3.5`（皆以 `<repo>` 為末之引數〔`failclosed` 另附 `3.5`〕；`probe_WG9344_k6s3.py selftest`、`probe_WG9344p1_pooltemp.py selftest` 無之） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `12` 之施後之列（此等器本批⛔ 改·其末列 ＝ 工項一之端之同器之末列） |
| `V-4` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`… cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**·`R-7`） |
| `V-5` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json`；`git hash-object <O>\parity35_pre.json <O>\parity35_post.json`；同 `00` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；其 `stdout` 與前置 `3` 之同呼叫逐位同；二 `hash-object` 之出艙各二列相等（落檔逐位同）；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0` |
| `V-6` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_post_35.json`；同 `0.0` ⇒ `<O>\f8_post_00.json`；`git hash-object <O>\f8_pre_35.json <O>\f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同·`rows` `35`／`36`、入池閘之紀錄 `2`／`2` 列）（`cmp8` ⛔ 用·`§一` 項 `6`） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；二檔之增／刪之數與其 blob 出艙（發單側復驗時自倉重算·⛔ 預載）；`verify/` 之其餘一切檔對工項一之端相異 `0` |
| `V-8` | `git grep -c -F "k967_pool_less(" -- app.py verify/selection_pipeline.py`；`git grep -c -F "成員之輸入之分攤登記面積" -- app.py` | 前者之出艙恰一列 `app.py:5`（列數·`R-3` 之五見各在不同之列；`verify/selection_pipeline.py` 無列）；後者**無出艙**、`rc 1`（`R-5`·判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞（四表之減、五處之試算之 `pool_out`）於本案之配地⛔ 觸，其「⛔ 變」由 `V-4`〜`V-6` 直接量之；`run_all` 之相異項亦唯可由配地之變而生——發單側已於倉外之拋棄式 worktree 自跑工項一之端與原型之 `run_all`（`§一` 項 `8`）。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：五處之 `pool_out` 與 `members` 之 build 之同一（`R-2`）；四表之配對之試算（`R-3`）；二新函式之停機之支（`R-1`）；`R-5` 之註之文；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-378-gb204`。

**工項三　登記**（零生產碼·一 `commit`）：
1. 塊 `G13` 附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；塊 `E21` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P31` 附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；三檔之 blob ＝ `§五-1` 項 `10`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `11`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P31` 附後：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
4. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-378 工項三：GB-204 之進度（① 之落地·② 之不可達之判）＋ 自誤 605／606 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-378-gb204`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-378R_GB-204之落地_執行報告.md` ＋ 同目錄之 `W-G.9-378R_GB-204之落地_二檔差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 前置與驗之全部出艙（`F27` 之 `selftest`／`wiring`／`mutate` 之全文、`F28 selftest` 之全文、`F14`／`F17`／`F23`／`F24`／`F25` 之全文、`V-5`／`V-6` 之 `hash-object` 之出艙、`F24 run`／`F23 run` 之末十二列、`k6s3 cmp` 之全文、`parity` 之末十五列）；④ 塊之實得（bytes／`sha256`）與三簿之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **二檔之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-378 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-378-gb204`。

### `§四-2`　次單（⛔ 本單之期）

發單側復驗本批之碼（自倉重跑 `V-1`〜`V-9`）後：**入主線之請示**（本批·生產碼·配地⛔ 變）·附 KL 於畫面之核對（新側支之端之 `app.py` 於退縮 `3.5 m`／`0 m` 按「🧮 執行 G 值迭代計算」：其所見 ＝ 主線之端之同按·配地與諸紀錄⛔ 變）＋ 主 checkout 之同步（塊 `P31` 序 `5`）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9355_screenmerge.py` `6`／`2`、`probe_WG9358_k948_wiring.py` `5`／`2`、`probe_WG9363_k953.py` `3`／`0`、`probe_WG9367_adj4.py` `4`／`1`、`probe_WG9370_adj4mut.py` `4`／`0`、`probe_WG9373_k966.py` `159`／`7`、`probe_WG9373p1_partrem.py` `79`／`0`（唯此七檔）（增／刪）；工項二 ＝ `app.py`、`verify/selection_pipeline.py`（唯此二檔·其數出艙）；工項三 ＝ `GB` 簿 `23`／`0`、自誤簿 `20`／`0`、`CLAUDE.md` `24`／`0`（唯此三檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `02cc0cb` | 生產碼相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；`verify/` 之一切檔相異恰 **`8`**（`M`：`verify/selection_pipeline.py` 與塊所改之七器）；本批之新檔（本單、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc`〔不存之路徑亦可〕⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·⛔ 工作樹〔`core.autocrlf` 之故〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`15` 檔：本單、七器、二生產碼檔、`GB` 簿、自誤簿、`CLAUDE.md`、報告二檔） |
| `4` | 三簿之 bytes | `GB` 簿 `1054032` → **`1057151`**；自誤簿 `1167087` → **`1170235`**；`CLAUDE.md` `380931` → **`384142`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊；`K-6` 典 ＝ `5fab239a68b58ef042d38d7a731eb8b5eade5f03`（⛔ 變） |
| `5` | 自限 | 遠端 heads **`40`**；主線 ＝ `02cc0cb8e83a966f6193c41b02c6093e59f74f84`（⛔ 變）；四側支 ＝ 單首（皆⛔ 變）；`verify/W-G.9-378-gb204` ＝ 工項四之 `commit`，其祖含 `02cc0cb`；其餘 `39` 列逐列 ＝ `<O>\heads_before.txt` |
| `6` | `python verify/probes/probe_WG9270_closegate.py 606 604 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 607 606 .` ⇒ `rc 7` |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 606 604` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`591`**／`MAX` **`606`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `196`／`204`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `67`／`70`／`[44, 47]`（自誤唯增 `605`、`606`；餘 ＝ 開工態） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `14`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `Fw14` | `2897` B·`sha256` `5f6135bed4f52bdba32a648bad52d73a77cc6074eca6b6393d580bfbeae31a03`·`33` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw14.diff`，`git apply` 於 `verify/probes/probe_WG9355_screenmerge.py`（施前 blob `29104558640e21209c9c2f9217f4855d22406c52`） |
| `3` | 塊 `Fw17` | `2039` B·`sha256` `b18080d7599860969165a1dc8710b8b3d858afb341d26c38a1447516c8d855c9`·`25` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw17.diff`，`git apply` 於 `verify/probes/probe_WG9358_k948_wiring.py`（施前 blob `c32de6aaba5b6fc2f91816f283c80dcd778378ad`） |
| `4` | 塊 `Fw23` | `675` B·`sha256` `bb940a4d42903a5c0d09cfc8a16a8e174d309abe7091a41abd660a68267a97db`·`14` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw23.diff`，`git apply` 於 `verify/probes/probe_WG9363_k953.py`（施前 blob `a8d303f48c4406ea19b5cddb6c30b099f130f67a`） |
| `5` | 塊 `Fw24` | `1871` B·`sha256` `5a3aeaccd8621f686e3e6a34946603a907025c416142c1aa999e84e448d30111`·`23` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw24.diff`，`git apply` 於 `verify/probes/probe_WG9367_adj4.py`（施前 blob `c218603ace1e26664b4ec32c87112ad06f9c3861`） |
| `6` | 塊 `Fw25` | `813` B·`sha256` `ac5fd63b6fdd7b47181cf19530cf6b64742a6807b009493f63a2f9914e6f7630`·`15` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw25.diff`，`git apply` 於 `verify/probes/probe_WG9370_adj4mut.py`（施前 blob `85ba17c34ef0891c51afb99b7f8bedaa9f021114`） |
| `7` | 塊 `Fw27` | `13243` B·`sha256` `d96b257a70219e68cd9e26a0f65a0c8aeb68b0e940551307708646f95cb1d7af`·`220` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw27.diff`，`git apply` 於 `verify/probes/probe_WG9373_k966.py`（施前 blob `2e5c2203a6ac9eb185c12fc8aa1eeda6e5fe4770`） |
| `8` | 塊 `Fw28` | `7404` B·`sha256` `ae62037a8f85658baf1a248df3091a4ddb5ff8e61dff4051553c7345a26a7a4e`·`104` 列（圍欄內全文·末附換行）；抽為 `<O>\Fw28.diff`，`git apply` 於 `verify/probes/probe_WG9373p1_partrem.py`（施前 blob `cafa6ecb2b99a21c78db002b52df82b6a256244a`） |
| `9` | 塊 `G13`／`E21`／`P31` | 塊 `G13` `3119` B·`sha256` `98f5e106141908eaf90f7822d598fc7045e2d00cc39764e929e97a122c9d934b`·`23` 列；塊 `E21` `3148` B·`sha256` `302cb7edd3e53729c501046228d2779c10eed904560548d61465c454d245482d`·`20` 列；塊 `P31` `3211` B·`sha256` `1844f5b2be375e4ee8fdf084ae6d6cb825e5ec76d723a5cbef9f3ded32f2fadf`·`24` 列（皆圍欄內全文·末附換行·首列為空列；`P31` 之 payload 內 `⬜` 之子字串框 `8`·列框 `6`〔塊之自載〕）；附於 `GB` 簿（`1054032` B）、自誤簿（`1167087` B）、`CLAUDE.md`（`380931` B）之末，期末 ＝ `1057151`／`1170235`／`384142` B |
| `10` | 寫出後之 blob | 工項一之七器：`probe_WG9355_screenmerge.py` ＝ `413978d7f020919d584079efe6b1637b1b9d6c6f`（`37500` B）、`probe_WG9358_k948_wiring.py` ＝ `6bdc07df94523e29401f935dbef142c6812126b2`（`28996` B）、`probe_WG9363_k953.py` ＝ `68db65ebd3a147a337d594fd21cedd67130cc02b`（`85194` B）、`probe_WG9367_adj4.py` ＝ `3482ef5504fc6d9b50d32b8a0580e6b0062b9c90`（`70923` B）、`probe_WG9370_adj4mut.py` ＝ `6c1a637a1341d410a6c85caf799e148ecca4444a`（`18841` B）、`probe_WG9373_k966.py` ＝ `6cd33e7f37214437cf2a7480c5c42dab87e47200`（`76890` B）、`probe_WG9373p1_partrem.py` ＝ `c9834221cc9d07b9c23491728d73bc6ea6be2705`（`39060` B）；工項三之三簿：`GB` 簿 ＝ `220636eb1ab187d14bf93e3fdba37dffc31ae631`（`1057151` B）、自誤簿 ＝ `8ecca07591032157b9c54713de7d925e459d6bed`（`1170235` B）、`CLAUDE.md` ＝ `9ac3640a3875cd842fe9ed988606b5cf813ad007`（`384142` B）；`K-6` 典 ＝ `5fab239a68b58ef042d38d7a731eb8b5eade5f03`（⛔ 變）。🔒 `app.py`、`verify/selection_pipeline.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `11` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-377 §五-1` 項 `7`） |
| `12` | 量測器之二態（發單側窗八十實跑·倉外） | **工項一之端**（`02cc0cb` ＋ 七個 `diff` 塊）：`V-1`〜`V-3` 之 `52` 呼叫中，`8` 呼叫 ＝ `§四-1` 工項二前置 `1`（其末列逐字見該處）；餘 `44` 呼叫皆 `rc 0`·其末列 ＝ 下開施後之列。**施後**（原型）：`52` 呼叫皆 `rc 0`，末列逐字皆 `⇒ 紅 []；rc 0`，唯：`probe_WG9373_k966.py mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`probe_WG9370_adj4mut.py mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`；`probe_WG9345_screen.py wiring` ＝ `⇒ rc 0（不符 0·器紅 0）`；`probe_WG9344_k6s3.py selftest` ＝ `selftest 9/9 ⇒ ✅`；`probe_WG9344p1_pooltemp.py selftest` ＝ `selftest 13/13 ⇒ ✅`；`probe_WG9341_synth.py` ＝ `ε ＝ 0.0002｜rc 0`；`probe_WG9340_main_synth.py` ＝ `紅項 [] 器紅 0`。`P0`：`F27` `31／31`、`F28` `29／29`、`F23` `40／40`、`F24` `28／28`、`F14` `86／86`；`F27 wiring` `Y1`〜`Y9` ✅。二態之 `V-3` 之 `36` 呼叫之 `stdout` 逐位同（唯 `probe_WG9348_harvest_key.py` 之暫存之路徑、`probe_WG9340_main_synth.py` 所印之行號）；二態之諸呼叫之 `stderr` 合計 `0` B |
| `13` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗八十實跑（態 `02cc0cb`）：🔴 機械 `0` 項／🟡 提示 `3` 項——`P-4` `:87`（`§一` 之表頭·其箭頭係 `commit` 之先後〔時間序〕與推論〔⇒〕，表內自載 ⇒ **具名豁免**）、`P-4` `:217`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 改前至改後〔閘 `4`〕，表內自載 ⇒ **具名豁免**）、`P-4` `:400`（附錄己之塊 `Fw27` 之圍欄所起之段·其箭頭係量測器之差異之內文〔逐字之塊·⛔ 為本單之期〕⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `22630`–`30350`·本單⛔ 用） |
| `14` | 收工閘之模擬（發單側·本機 Linux·⛔ `push`） | `git worktree add --detach <S> 02cc0cb`（拋棄式）＋ 本單之定稿（`814` 列·其十塊即附錄甲〜癸）＋ 原型之二生產碼檔（代工項二）＋ 報告之替身·五 `commit`（首列 ＝ `§四-1` 所令逐字·其後空一列附尾列）：開場之器 `rc 0`（＝ `§零-0` 項 `3`）；工項零之 blob ＝ 來源；十塊之抽取 ＝ 項 `2`〜`9`；`git apply --check` `rc 0`；七器之施後 blob ＝ 項 `10`；前置 `1` 之八呼叫 ＝ 期（`rc 1` 七、`rc 3` 一）、前置 `4` ＝ `app.py:1`；`V-1` 之四呼叫與 `F14 selftest`、`F17`／`F23`／`F24`／`F25` 之 `wiring`、`F24 selftest`、`F25 mutate` 皆 `rc 0`·末列 ＝ 期（`P0` `31／31`、`29／29`；`Y1`〜`Y9` ✅）；`V-7` 相異 ＝ `app.py`（`+52`／`-7`）、`verify/selection_pipeline.py`（`+8`／`-4`）；`V-8` ＝ `app.py:5`／`rc 1`；stderr `0` B；三簿之施後 blob、bytes ＝ 項 `10`；`checkidx`／`gen_fa_index` ＝ 期·逐位同；閘 `1` ＝ 工項零 `814`／`0`、工項一 ＝ 該閘之期、工項二 `52`／`7`·`8`／`4`、工項三 ＝ 該閘之期、工項四（替身）二檔各 `1`／`0`；閘 `2` ＝ 生產碼相異 `2`、`verify/` 相異 `8`（皆 `M`）·新檔三之 `git check-ignore -v --no-index` 無命中（對照 `rc 0`）；閘 `3` `15` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `4` 三簿皆嚴格前綴、其尾 ＝ 塊、`K-6` 典⛔ 變；閘 `6` `rc 0`（判別力 `607 606` ⇒ `rc 7`）；閘 `7` `rc 0`（＝ 該閘之期）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-2`〜`V-6` 之長跑之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `4`／`6` 之實跑逐位同（七器 ＝ 項 `10`、二生產碼檔 ＝ 原型） |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄癸` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-378-gb204`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `Fw14`（`git apply` 之差異·`verify/probes/probe_WG9355_screenmerge.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9355_screenmerge.py b/verify/probes/probe_WG9355_screenmerge.py
index 2910455..413978d 100644
--- a/verify/probes/probe_WG9355_screenmerge.py
+++ b/verify/probes/probe_WG9355_screenmerge.py
@@ -24,6 +24,8 @@
            另 E1 試算旗標（`SS_END_BLOCK_MODE`）⛔ 外洩／E2 配地所用之宗地 ＝ 合併再試後／E3 正常出口無停機訊息。
   🔧 `W-G.9-373`（`K-9-67`·⛔ 上列一字不刪）：段三之 `alloc_state` 之出增 `members`（保留宗之成員·入池閘之末態 build·
            無之 ⇒ 試算之 build）——T3d／T9d／T6d 之期隨之（本器之樁⛔ 寫入池閘之末態 ⇒ 試算之 build 之各宗自為其成員）。
+  🔧 `W-G.9-378`（`GB-204`·⛔ 上列一字不刪）：段三之 `alloc_state` 之出另增 `pool_out`（入池閘之帳·與 `members` 取同一 build）
+           ——T3d／T9d／T6d 之期隨之（本器之樁⛔ 帶入池閘之帳 ⇒ `{}`）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import contextlib, copy, importlib.util, inspect, io, os, sys
@@ -387,7 +389,8 @@ def _t3(ns, ss, merge):
             (f"{tag}b 段三本體與合併再試各恰一次", (rig.s3_n, rig.merge_n), (1, 1)),
             (f"{tag}c 段三之試算配地亦 'trial'", [c[1] for c in gs3], ["trial"]),
             (f"{tag}d 段三之 alloc_state 之出", rig.s3_state, {"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None,
-                                                           "G": {"A(1)": 0.0}, "members": MEM373}),
+                                                           "G": {"A(1)": 0.0}, "members": MEM373,
+                                                           "pool_out": {}}),     # 🔧 `W-G.9-378`
             (f"{tag}e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位",
              (a.get("temp") is s3r[0], a.get("build") is s3r[1], a.get("locked")), (True, True, {"C(1)"})),
             (f"{tag}f 回傳之宗地 ＝ 末態（同一物件）", (ret is not None and ret["temp"] is fin[0], ret is not None and ret["build"] is fin[1]),
@@ -484,7 +487,8 @@ def _t6(ns, ss):
             stt = cb["alloc_state"](t0, b0)
         gs = [c for c in rig.calls[n0:] if c[0] == "g"]
         out.append(("T6d 試算配地（alloc_state）之出與其 'trial'", (stt, [c[1] for c in gs]),
-                    ({"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None, "G": {"A(1)": 0.0}, "members": MEM373},
+                    ({"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None, "G": {"A(1)": 0.0}, "members": MEM373,
+                      "pool_out": {}},                                          # 🔧 `W-G.9-378`
                      ["trial"])))
         n0 = len(rig.calls)
         with contextlib.redirect_stdout(io.StringIO()):
````

## 附錄乙　塊 `Fw17`（`git apply` 之差異·`verify/probes/probe_WG9358_k948_wiring.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9358_k948_wiring.py b/verify/probes/probe_WG9358_k948_wiring.py
index c32de6a..6bdc07d 100644
--- a/verify/probes/probe_WG9358_k948_wiring.py
+++ b/verify/probes/probe_WG9358_k948_wiring.py
@@ -55,6 +55,8 @@ _k6b_callbacks 之巢狀 alloc_state。
     量 `_has357`／`_res357`／鍵之環；W8 之回傳之鍵增 `'members'`（`K-9-67`·第五鍵）；W11 之三支取鍵之環中測試為
     `_has357(_rm) and _pid in marks` 之 if（建地之支另立於其前·⛔ 計）。突變去 M2〜M9、M14、M16、M19、M22、M28、M29
     （其錨已去·M2 之錨之縮排隨步驟 10 之重排而異），餘 15 種。
+  🔧 `W-G.9-378`（`GB-204`·⛔ 上列一字不刪）：W8 之回傳之鍵於 `'members'` 之後增 `'pool_out'`（入池閘之帳·第六鍵·其值與
+    `members` 取同一 build·F27 之 Y8 量之）。
 rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
 """
 import ast, contextlib, io, os, sys
@@ -318,8 +320,9 @@ def _w8(c):
     same = pa[0] is not None and pa[0] == ps[0]
     has = pa[1] is not None and need <= set(pa[1])
     # 🔧 `W-G.9-373`（`K-9-67`）：回傳之鍵 ＝ 前四鍵 ＋ 'members'（其值之式二處各異·⛔ 比）
-    ra = pa[3] is not None and pa[3][:4] == want_ret and [k for k, _ in pa[3][4:]] == ["'members'"]
-    rs = ps[3] is not None and ps[3][:4] == want_ret and [k for k, _ in ps[3][4:]] == ["'members'"]
+    # 🔧 `W-G.9-378`（`GB-204`）：其後增 'pool_out'（入池閘之帳·與 members 取同一 build·F27 之 Y8 量之）
+    ra = pa[3] is not None and pa[3][:4] == want_ret and [k for k, _ in pa[3][4:]] == ["'members'", "'pool_out'"]
+    rs = ps[3] is not None and ps[3][:4] == want_ret and [k for k, _ in ps[3][4:]] == ["'members'", "'pool_out'"]
     ok = same and has and pa[2] == "{}" and ps[2] == "{}" and ra and rs
     return ok, (f"保留之支逐 AST 同 {same}；含 kept 與 G {has}；_G 之初值 {pa[2]}／{ps[2]}；"
                 f"回傳之鍵 app {ra}／harness {rs}")
````

## 附錄丙　塊 `Fw23`（`git apply` 之差異·`verify/probes/probe_WG9363_k953.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index a8d303f..68db65e 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -1060,6 +1060,9 @@ CHG375_SP = ("build_build_parcels",)
 KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG375_APP)
 APP_ALLOW |= set(CHG375_APP)
 SP_ALLOW |= set(CHG375_SP)
+# 🔧 `W-G.9-378`（`GB-204`）：W7 之許增 `k967_pool_out`、`k967_pool_less`（重劃前面積之表減入池閘之帳·其行為由 F27 之 B4〜B6、
+#   F28 之 D1〜D3 量之、其接線由 F27 之 Y8 量之）
+APP_ALLOW |= {"k967_pool_out", "k967_pool_less"}
 
 
 def _top_dump(tree):
````

## 附錄丁　塊 `Fw24`（`git apply` 之差異·`verify/probes/probe_WG9367_adj4.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index c218603..3482ef5 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -596,7 +596,7 @@ def _cases(ns, sp):
          lambda: (lambda r: (sorted(r), r["kept"], r["err"], r["members"], sorted(r["units"]),
                              r["units"]["u(1)"] is not bu[0]))(
              ns["adj4_trial_state"]({"kept": {"B1": {"u(1)"}}, "bad_pools": {}, "G": {"u(1)": 1.0}}, None, bu)),
-         (["G", "bad_pools", "err", "kept", "members", "units"], {"B1": {"u(1)"}}, None,
+         (["G", "bad_pools", "err", "kept", "members", "pool_out", "units"], {"B1": {"u(1)"}}, None,   # 🔧 `W-G.9-378`
           {"u(1)": ["u(1)", "u(2)"], "v(1)": ["v(1)"]}, ["u(1)"], True))
     _run(out, "K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True",
          lambda: _k21(ns), (True, False, False, False, True, False, False))
@@ -741,6 +741,9 @@ W6_SKIP373 = ("k953_manual_run",)
 # 🔧 `W-G.9-375`（`K-9-65`）：W5 之許增入池閘之畫面入口（注入）與 harness 之 `build_build_parcels`（session 鍵）
 ALLOW375_APP = ("_k929_6_screen_gate",)
 ALLOW375_SP = ("build_build_parcels",)
+# 🔧 `W-G.9-378`（`GB-204`）：W5 之許增重劃前面積之表減入池閘之帳之二函式與五處之試算之所改（其接線由 F27 之 Y8 量之）
+ALLOW375_APP += ("k967_pool_out", "k967_pool_less", "f3_screen_k953")
+ALLOW375_SP += ("run_k953",)
 ANC_SKIP373 = ("_out.append(tp)", "member", "members")
 FN_GONE373 = ("_k951", "_max357", "_split357", "_try", "_fill953", "_probe953", "_remain953")
 # 🆕 `W-G.9-370`（K-9-57 ⑧）：W6 之許——`k953_manual_run` 之 `S219` 之停機訊息之基準二列（逐字）得易之（唯此二列）
````

## 附錄戊　塊 `Fw25`（`git apply` 之差異·`verify/probes/probe_WG9370_adj4mut.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9370_adj4mut.py b/verify/probes/probe_WG9370_adj4mut.py
index 85ba17c..6c1a637 100644
--- a/verify/probes/probe_WG9370_adj4mut.py
+++ b/verify/probes/probe_WG9370_adj4mut.py
@@ -90,6 +90,10 @@ ALLOW373_SP = ("_k6b_callbacks", "k6b_stage3_pool_temp")
 ALLOW375_FILES = ("verify/stepg_pipeline.py",)
 ALLOW373_APP += ("_k929_6_screen_gate",)
 ALLOW373_SP += ("build_build_parcels",)
+# 🔧 `W-G.9-378`（`GB-204`）：X2 之許增重劃前面積之表減入池閘之帳之二函式與五處之試算之所改；X4 之除外增 `run_k953`
+#   （其試算之回傳增 pool_out）——本單之接線另由 F27 之 Y8 量之
+ALLOW373_APP += ("k967_pool_out", "k967_pool_less", "adj4_trial_state", "f3_screen_k953")
+ALLOW373_SP += ("run_k953",)
 
 
 def _strip_fns(src, names):
````

## 附錄己　塊 `Fw27`（`git apply` 之差異·`verify/probes/probe_WG9373_k966.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9373_k966.py b/verify/probes/probe_WG9373_k966.py
index 2e5c220..6cd33e7 100644
--- a/verify/probes/probe_WG9373_k966.py
+++ b/verify/probes/probe_WG9373_k966.py
@@ -38,6 +38,16 @@
            之 selftest 之項，其「所指之項」皆須紅；另跑基準一（⛔ 突變·五器之項皆綠）。受測碼之該段改寫者其錨隨之更新（另單）。
            ⛔ 列者（明書之）：手冊先行之 K-9-51 之候選之序「距離 → 本街廓者先」之對調——距離取片至街廓之形（該街廓之片之
            聯集）之距離，本街廓者恆為 0 ⇒ 對調為等價之突變（行為⛔ 異）。
+  🔧 `W-G.9-378`（`GB-204`·`自誤 605`·⛔ 上列一字不刪）：
+  selftest 增 B4〜B6（`k967_pool_out`：入池閘之末態 build 之各片已部分併出之量〔帳缺或空者⛔ 列〕；`k967_pool_less`：重劃前面積之表減之·
+           其停機）；NEED 增此二名；P0 隨之 31 項。
+  wiring   增 Y8（五處之試算〔段三·手冊先行之 harness 與畫面、第一趟之共用之 `adj4_trial_state`〕皆以同一 build 回
+           `members` 與 `pool_out`·`k967_pool_out` 之呼叫須直書為該函式之 return 之鍵 `pool_out` 之值〔關鍵字引數或字面 dict〕）、Y9（單趟之管線
+           之序：末次之調配之輸入之 build ＝ 末次入池閘之出——`SS_ADJ_BUILD_FINAL` 恰一寫於 `f3_screen_stepg_run` 之入池閘
+           之後；畫面之 `main` 與 harness 之 `main` 之段三〔含手冊先行·第一趟〕皆先於 step G·harness 之 step G 之 build ＝
+           段三之出——`GB-204` ② 之不可達所繫·以源碼之序量之·⛔ 量控制流）。
+  mutate   之出艙碼：突變未被捕 ⇒ 1；錨數 ≠ 1、子程序逾時或例外、基準⛔ 全綠 ⇒ 3（無從判定·⛔ 與 1 共用·`CLAUDE.md`
+           之「無從判定與判定為偽⛔ 共用同一出艙碼」）；二者並見 ⇒ 1；末列 `⇒ 突變 N（另基準一）；紅 […]；無從判定 […]；rc …`。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, importlib.util, io, os, re, sys, warnings
@@ -156,6 +166,41 @@ def _b3(ns):
             _halt(lambda: pa("u", ["a", "z"], {"a": 10.0}), ["z"]))
 
 
+# 🆕 `W-G.9-378`（`GB-204`）：入池閘之帳（`k967_pool_out`）與重劃前面積之表之減（`k967_pool_less`）
+def _pb(pid, own=None, mem=None, ms=None):
+    b = {"暫編地號": pid, "入池閘併入": ms or [pid]}
+    if own is not None:
+        b["入池閘部分併出"] = own
+    if mem is not None:
+        b["入池閘成員部分併出"] = mem
+    return b
+
+
+def _b4(ns):
+    po = ns["k967_pool_out"]
+    bf = [_pb("A(1)", {"R(1)": 3.0, "S(1)": 2.0}, {"B(1)": {"R(1)": 4.0}}, ["A(1)", "B(1)"]), _pb("C(1)"),
+          _pb("D(1)", None, {"E(1)": {"S(1)": 1.5, "T(1)": 0.5}}, ["D(1)", "E(1)"])]
+    return (po(bf), po([]), po(None), po([_pb("C(1)", {}, {})]), po([_pb("F(1)", {}, {"G(1)": {}}, ["F(1)", "G(1)"])]))
+
+
+def _b5(ns):
+    po = ns["k967_pool_out"]
+    return (_halt(lambda: po([_pb("A(1)", None, {"B(1)": {"R(1)": 1.0}}), _pb("C(1)", None, {"B(1)": {"S(1)": 1.0}})]),
+                  ["GB-204", "二處"]),
+            _halt(lambda: po([_pb("A(1)", {"R(1)": 2.0}, {"A(1)": {"S(1)": 1.0}})]), ["GB-204", "二處"]),
+            _halt(lambda: po([_pb("A(1)", {"R(1)": 0.0})]), ["GB-204", "≤ 0"]),
+            _halt(lambda: po([_pb("A(1)", None, {"B(1)": {"R(1)": -1.0}})]), ["GB-204", "≤ 0"]))
+
+
+def _b6(ns):
+    pl = ns["k967_pool_less"]
+    t = {"A(1)": 10.0, "B(1)": 5.0}
+    r = pl(t, {"A(1)": 3.0})
+    return (r, t == {"A(1)": 10.0, "B(1)": 5.0}, pl(t, None), pl(t, {}),
+            _halt(lambda: pl(t, {"Z(1)": 1.0}), ["GB-204", "不在重劃前面積之表"]),
+            _halt(lambda: pl(t, [("A(1)", 1.0)]), ["GB-204", "pool_out"]))
+
+
 # ── C：入池閘之代表宗（`K-9-67`）──
 def _rect(x0, x1, y0=0.0, y1=30.0):
     return [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
@@ -440,6 +485,14 @@ def _cases(ns, sp):
          lambda: _b2(ns), ["A(1)", "A(2)", "B(1)"])
     _run(out, "B3 k967_pre_area：成員之分攤登記面積之和；成員缺 ⇒ 自身；取不到 ⇒ 停機",
          lambda: _b3(ns), (30.5, 10.0, ("停機", True)))
+    # 🆕 `W-G.9-378`（`GB-204`）
+    _run(out, "B4 k967_pool_out：單元自身之片取入池閘部分併出之和、他成員之片取入池閘成員部分併出［片］之和；無帳者（缺或空）⛔ 列",
+         lambda: _b4(ns), ({"A(1)": 5.0, "B(1)": 4.0, "E(1)": 2.0}, {}, {}, {}, {}))
+    _run(out, "B5 k967_pool_out：同一片之帳見於二處（二單元·或自身與成員）⇒ 停機；量 ≤ 0 ⇒ 停機",
+         lambda: _b5(ns), (("停機", True), ("停機", True), ("停機", True), ("停機", True)))
+    _run(out, "B6 k967_pool_less：表減其量（新表·原表⛔ 動）；None／空 ⇒ 同值；表外之片 ⇒ 停機；非 dict ⇒ 停機",
+         lambda: _b6(ns), ({"A(1)": 7.0, "B(1)": 5.0}, True, {"A(1)": 10.0, "B(1)": 5.0}, {"A(1)": 10.0, "B(1)": 5.0},
+                           ("停機", True), ("停機", True)))
     # ── C ──
     _run(out, "C1 入池閘之代表宗：G 並列（60.00）⇒ 重劃前面積大者 Y2（100 ＞ 80）",
          lambda: _c(ns, 80.0, 20.0), ["Y2"])
@@ -579,6 +632,7 @@ def _perturb(v):
 
 NEED = ("K966_CLASSES", "K966_GRID", "k966_block_merge", "k967_rank", "k967_pre_area", "k929_6_fixpoint",
         "k953_manual_run", "k6b_stage3_run", "adj4_pass1_run", "adj_intake", "F3_CATEGORY_BURDEN")
+NEED += ("k967_pool_out", "k967_pool_less")                        # 🆕 `W-G.9-378`（`GB-204`）
 
 
 def selftest(repo):
@@ -691,8 +745,100 @@ def _wiring_checks(app):
     return chk
 
 
+# 🆕 `W-G.9-378`（`GB-204`）：Y8 五處之試算之 pool_out；Y9 調配之輸入之 build 為末次入池閘之出（`GB-204` ② 之不可達）
+def _call_name(n):
+    f = n.func
+    if isinstance(f, ast.Name):
+        return f.id
+    if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant) and isinstance(f.slice.value, str):
+        return f.slice.value
+    return None
+
+
+def _inner_fns(tree):
+    """{呼叫節點之 id: 其最內之 FunctionDef}。"""
+    out = {}
+
+    def walk(node, fn):
+        for ch in ast.iter_child_nodes(node):
+            nf = ch if isinstance(ch, ast.FunctionDef) else fn
+            if isinstance(ch, ast.Call):
+                out[id(ch)] = fn
+            walk(ch, nf)
+    walk(tree, None)
+    return out
+
+
+def _wiring378(repo):
+    chk = []
+    srcs = {"app.py": _read(repo, "app.py"), "verify/selection_pipeline.py": _read(repo, "verify/selection_pipeline.py")}
+    pairs, n_po = [], 0
+    for rel, src in srcs.items():
+        with warnings.catch_warnings():
+            warnings.simplefilter("ignore")
+            tree = ast.parse(src)
+        fns = _inner_fns(tree)
+        calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
+        n_po += sum(1 for c in calls if _call_name(c) == "k967_pool_out")
+        # 其值須為該函式之 return 之式之鍵 pool_out 之值（dict(…, pool_out=…) 或字面 dict 之鍵 'pool_out'·直書於 return）
+        #   ——⛔ 唯呼叫而⛔ 回之、⛔ 置於他處之 dict
+        def _keyed(fn):
+            out = set()
+            for r in ast.walk(fn):
+                v = r.value if isinstance(r, ast.Return) else None
+                if isinstance(v, ast.Call):
+                    out |= {id(k.value) for k in v.keywords if k.arg == "pool_out"}
+                elif isinstance(v, ast.Dict):
+                    out |= {id(x) for kk, x in zip(v.keys, v.values) if isinstance(kk, ast.Constant) and kk.value == "pool_out"}
+            return out
+        for c in calls:
+            if _call_name(c) != "k953_units_of":
+                continue
+            fn = fns.get(id(c))
+            arg = ast.dump(c.args[0]) if c.args else None
+            kf = _keyed(fn) if fn is not None else set()
+            ok = fn is not None and any(_call_name(d) == "k967_pool_out" and d.args and ast.dump(d.args[0]) == arg
+                                        and id(d) in kf for d in ast.walk(fn) if isinstance(d, ast.Call))
+            pairs.append((rel, fn.name if fn else None, c.lineno, ok))
+    chk.append(("Y8 五處之試算（段三·手冊先行之 harness 與畫面、第一趟之共用）皆以同一 build 回 members 與 pool_out"
+                "（k967_pool_out 之呼叫直書為 return 之鍵 pool_out 之值）",
+                len(pairs) == 5 and all(p[3] for p in pairs) and n_po == 5,
+                f"k953_units_of 之呼叫 {[(p[0].split('/')[-1], p[1], p[3]) for p in pairs]}；k967_pool_out 之呼叫 {n_po}"))
+    app = srcs["app.py"]
+    with warnings.catch_warnings():
+        warnings.simplefilter("ignore")
+        at = ast.parse(app)
+    top = {n.name: n for n in at.body if isinstance(n, ast.FunctionDef)}
+    st_fn = top.get("f3_screen_stepg_run")
+    asg = [(n.lineno, fnm) for fnm, f in top.items() for n in ast.walk(f)
+           if isinstance(n, ast.Assign) and any(isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Name)
+                                                and t.slice.id == "SS_ADJ_BUILD_FINAL" for t in n.targets)]
+    gate = [n.lineno for n in ast.walk(st_fn) if isinstance(n, ast.Call) and _call_name(n) == "_k929_6_screen_gate"] \
+        if st_fn else []
+    ok_a = len(asg) == 1 and asg[0][1] == "f3_screen_stepg_run" and bool(gate) and min(gate) < asg[0][0]
+    mn = top.get("main")
+    l_s3 = [n.lineno for n in ast.walk(mn) if isinstance(n, ast.Call) and _call_name(n) == "f3_screen_k6b_stage3"] if mn else []
+    l_g = [n.lineno for n in ast.walk(mn) if isinstance(n, ast.Call) and _call_name(n) == "f3_screen_stepg_run"] if mn else []
+    ok_b = bool(l_s3) and bool(l_g) and min(l_s3) < min(l_g)
+    with warnings.catch_warnings():
+        warnings.simplefilter("ignore")
+        rt = ast.parse(_read(repo, "verify/run_verification.py"))
+    rmain = next((n for n in rt.body if isinstance(n, ast.FunctionDef) and n.name == "main"), None)
+    r_pk = [n for n in ast.walk(rmain) if isinstance(n, ast.Call) and _call_name(n) == "run_corner_pk_k6b"] if rmain else []
+    r_g = [n for n in ast.walk(rmain) if isinstance(n, ast.Call) and _call_name(n) == "run_step_g"] if rmain else []
+    g1 = min(r_g, key=lambda n: n.lineno) if r_g else None
+    ok_c = bool(r_pk) and g1 is not None and min(n.lineno for n in r_pk) < g1.lineno and len(g1.args) >= 7 \
+        and ast.unparse(g1.args[6]) == "s3_by_tag[tag]['build']"
+    chk.append(("Y9 調配之輸入之 build ＝ 末次入池閘之出：SS_ADJ_BUILD_FINAL 恰一寫於 f3_screen_stepg_run 之入池閘之後；"
+                "畫面與 harness 之段三（含手冊先行·第一趟）皆先於 step G", ok_a and ok_b and ok_c,
+                f"寫 {asg}·入池閘 {gate[:1]}；畫面 段三 {l_s3[:1]} ＜ step G {l_g[:1]}；harness run_corner_pk_k6b "
+                f"{[n.lineno for n in r_pk][:1]} ＜ run_step_g {g1.lineno if g1 else None}"
+                f"（build ＝ {ast.unparse(g1.args[6]) if g1 is not None and len(g1.args) >= 7 else None}）"))
+    return chk
+
+
 def wiring(repo):
-    chk = _wiring_checks(_read(repo, "app.py"))
+    chk = _wiring_checks(_read(repo, "app.py")) + _wiring378(repo)
     red = []
     for name, ok, note in chk:
         print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
@@ -942,19 +1088,25 @@ def mutate(repo):
             res = list(ex.map(one, todo))
     finally:
         shutil.rmtree(tmp, ignore_errors=True)          # 暫存之 app_*.py（每份約 1.8 MB）⛔ 遺留
+    und = []                    # 🔧 `W-G.9-378`（`自誤 605`）：無從判定 ⛔ 與「未捕」共用出艙碼
     for m, n, red in res:
         mid, cl, desc, fn, old, new, want = m
         got = {f"{k}:{i}" for k, v in red.items() for i in v} if isinstance(red, dict) else None
         if mid == "N00":
-            ok = got == set()
+            ok, nd = got == set(), got != set()
         else:
-            ok = n == 1 and got is not None and bool(want) and want <= got
-        if not ok:
+            nd = n != 1 or got is None
+            ok = not nd and bool(want) and want <= got
+        if nd:
+            und.append(mid)
+        elif not ok:
             bad.append(mid)
         shown = sorted(got) if got is not None else red
-        print(f"  {'✅' if ok else '🔴'} {mid} {cl}·{desc}：錨 {n} 見；所指 {sorted(want)}；紅 {shown}")
-    print(f"⇒ 突變 {len(MUT377)}（另基準一）；紅 {bad}；rc {1 if bad else 0}")
-    return 1 if bad else 0
+        mark = "✅" if ok else ("⚠️" if nd else "🔴")
+        print(f"  {mark} {mid} {cl}·{desc}：錨 {n} 見；所指 {sorted(want)}；紅 {shown}")
+    rc = 1 if bad else (3 if und else 0)
+    print(f"⇒ 突變 {len(MUT377)}（另基準一）；紅 {bad}；無從判定 {und}；rc {rc}")
+    return rc
 
 
 # ── run：本案 ──
````

## 附錄庚　塊 `Fw28`（`git apply` 之差異·`verify/probes/probe_WG9373p1_partrem.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9373p1_partrem.py b/verify/probes/probe_WG9373p1_partrem.py
index cafa6ec..c983422 100644
--- a/verify/probes/probe_WG9373p1_partrem.py
+++ b/verify/probes/probe_WG9373p1_partrem.py
@@ -34,6 +34,9 @@
            「面積_m2 ＋ 段三部分併出之和」恆 ＝ 0·⛔ 以「最末一次」或「輸入之帳 ＋ 最末一次」代之）；⑧ `R-19″` 之重劃前面積之表之
            **取態**（受測碼呼叫 `k967_pre_area` 時所傳之表，其受詞之片之值 ＝ 分攤登記面積 − 當下之帳之和·⛔ 取輸入之態）——以
            包一層之 `k967_pre_area`（`ns` 即受測碼之 globals）記每次所傳之表之受詞之值。期值手算（各例之註）。
+           🔧 `W-G.9-378`（`GB-204` ①·⛔ 上列一字不刪）：增 D1〜D3（三處各一·L4〜L6 之形）——試算包一層而回 `pool_out`
+           （入池閘之帳之代用·其值隨受詞之片當下是否已再部分併出而異 ⇒ 表若取他次之試算之帳其值必異），量 ⑨ 重劃前面積之
+           表減其**同一試算**之入池閘之帳（`k967_pool_less`）；其試算⛔ 回 `pool_out` 者（L4〜L6 等）⇒ 表⛔ 減（同值）。
 rc：0 相符／1 不符／2 用法錯。
 """
 import contextlib, copy, importlib.util, io, os, sys
@@ -343,6 +346,74 @@ def _l6(ns, f16):
                                                                       log_print=lambda *a: None, contests=ct))
 
 
+# 🆕 `W-G.9-378`（`GB-204` ①）：重劃前面積之表減同一試算之入池閘之帳（pool_out）
+def _pool(st, pid, thr):
+    """試算包一層：其回傳增 pool_out（入池閘之帳之代用）——當下 build 之 pid 之 面積_m2 ＜ thr ⇒ {pid: 2.0}，否則 {pid: 1.0}
+    （同一受詞於受測碼之各次試算之值相異 ⇒ 表若取他次之試算之帳，其值必異）。"""
+    def wrapped(temp, build):
+        r = dict(st(temp, build))
+        a = next((float(b.get("面積_m2", 0) or 0) for b in build if b["暫編地號"] == pid), 0.0)
+        r["pool_out"] = {pid: 2.0 if a < thr else 1.0}
+        return r
+    return wrapped
+
+
+def _d1(ns, f27):
+    """手冊先行（L4 之形）：首次之試算（C0·X(1) 之 面積_m2 ＝ −5）之 pool_out {X(1): 1}；K-9-51 之試算（X(1) 已再部分併出）
+    之 pool_out {X(1): 2} ⇒ 計畫時之表 X 55 − 1 ＝ 54、K-9-51 之表 X 5.6897 − 2 ＝ 3.6897；Y／Z 無帳 ⇒ 同 L4。"""
+    tp, R, H = f27._tp, f27._R, f27.H
+    x = tp("X(1)", "BA", H, R(0, 10, 0, 30), 60)
+    x.update({"面積_m2": -5.0, "段三併出": ["A1(1)"], "段三部分併出": {"A1(1)": 5.0}})
+    t = [x, tp("Y(1)", "BA", H, R(10, 20, 0, 30), 50), tp("Z(1)", "BA", H, R(20, 30, 0, 30), 40),
+         tp("A1(1)", "BB", H, R(0, 10, 30, 60), 300), tp("B1(1)", "BB", H, R(10, 20, 30, 60), 300),
+         tp("C1(1)", "BB", H, R(20, 30, 30, 60), 300), tp("A2(1)", "BD", H, R(40, 50, 0, 30), 300)]
+    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
+    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
+    ap, st = f27._cbs({"BB": 130.0, "BD": 5.0}, drop=("X(1)", "Y(1)", "Z(1)"))
+    st = _pool(st, "X(1)", -5.5)
+    return _with_spy(ns, {"X(1)", "Y(1)", "Z(1)"},
+                     lambda seen: ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, _rec(st, {"X(1)"}, seen),
+                                                        log_print=lambda *a: None))[1]
+
+
+def _d2(ns, f27):
+    """第一趟（L5 之形）：第 1 輪之試算之 pool_out {X1(1): 1}、第 2 輪（X1(1) 已部分併出）{X1(1): 2} ⇒ 表 ＝ 55 − 1 ＝ 54、25 − 2 ＝ 23。"""
+    tp, R, H = f27._tp, f27._R, f27.H
+    x = tp("X1(1)", "BA", H, R(0, 10, 0, 30), 60.0)
+    x.update({"面積_m2": -5.0, "段三併出": ["X1(2)"], "段三部分併出": {"X1(2)": 5.0}})
+    t = [x, tp("X1(2)", "BB", H, R(0, 10, 30, 60), 300), tp("X1(3)", "BC", H, R(20, 30, 0, 30), 300)]
+    geom = {q["暫編地號"]: [list(c) for c in q["polygon_coords"]] for q in t}
+    ap, st = f27._cbs({"BB": 30.0, "BC": 10.0}, drop=("X1(1)",))
+    st = _pool(st, "X1(1)", -5.5)
+    subj = [{"歸戶": "g1", "軌": "建地軌", "錨點": "X1(1)", "名單": ["BB", "BC"], "片": ["X1(1)"], "原有面積合計": 60.0}]
+    return _with_spy(ns, {"X1(1)"}, lambda seen: ns["adj4_pass1_run"](t, list(t), {"X1": "g1"}, subj, geom, ap,
+                                                                      _rec(st, {"X1(1)"}, seen),
+                                                                      log_print=lambda *a: None))[1]
+
+
+def _d3(ns, f16):
+    """段三（L6 之形）：第 5 項之試算（題一 4 之後·Y1(1) 已再部分併出）之 pool_out {Y1(1): 2} ⇒ 表 ＝ 65 − 2 ＝ 63。"""
+    temp, own, blocks, cl = f16._world4()
+    for q in temp:
+        if q["暫編地號"] == "Y1(1)":
+            q.update({"面積_m2": -5.0, "段三併出": ["X1(1)"], "段三部分併出": {"X1(1)": 5.0}})
+    build = [q for q in temp if q["街廓分類"] == f16.H]
+    ap, _tw, st = f16._cbs({"BX": 60.0, "BY": 1000.0, "B7": 50.0}, None, ("Y1(1)",))
+    st = _pool(st, "Y1(1)", -5.5)
+    thr = {("BX", "左"): 130.0, ("BY", "左"): 200.0}
+
+    def tw(temp_, build_, blk, end, cand):
+        b_ = {b["暫編地號"]: b for b in build_}
+        g = f16._g(b_[cand]) if cand in b_ else 0.0
+        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
+    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
+             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
+    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
+    return _with_spy(ns, {"Y1(1)"}, lambda seen: ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap,
+                                                                      tw, _rec(st, {"Y1(1)"}, seen),
+                                                                      log_print=lambda *a: None, contests=ct))[1]
+
+
 def _cases(ns, f12, f16, f27, f23):
     out = []
     # E（門檻 150）：C1(1)（a 100）以 ① 同街廓併 C1(2)；C1(2) 部分併出之剩下 50（分攤 60·已併出 10）≡ 一分未併而 a 50
@@ -459,6 +530,14 @@ def _cases(ns, f12, f16, f27, f23):
          lambda: _l5(ns, f27), ([0.0], [(("X1(1)", 25.0),), (("X1(1)", 55.0),)], True))
     _run(out, "L6 趟中之帳之累加與第 5 項之表之取態·段三：Y1(1) 帶前帳、題一 4 再併入同一受併宗 ⇒ 所見恆 0；表 ＝ 65",
          lambda: _l6(ns, f16), ([0.0], [(("Y1(1)", 65.0),)], True))
+    # 🆕 `W-G.9-378`（`GB-204` ①）
+    _run(out, "D1 手冊先行：二表各減其同一試算之入池閘之帳 ⇒ 計畫時 54／50／40、K-9-51 時 3.6897／5.1724／4.1379",
+         lambda: _d1(ns, f27), [(("X(1)", 3.6897), ("Y(1)", 5.1724), ("Z(1)", 4.1379)),
+                                (("X(1)", 54.0), ("Y(1)", 50.0), ("Z(1)", 40.0))])
+    _run(out, "D2 第一趟：各輪之表減該輪之試算之入池閘之帳 ⇒ 54、23",
+         lambda: _d2(ns, f27), [(("X1(1)", 23.0),), (("X1(1)", 54.0),)])
+    _run(out, "D3 段三：第 5 項之表減其試算之入池閘之帳 ⇒ 63",
+         lambda: _d3(ns, f16), [(("Y1(1)", 63.0),)])
     return out
 
 
````

## 附錄辛　塊 `G13`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末·工項三）

````markdown

---

## 🔧 `GB-204` 之進度（新側支·⛔ 解除）：① 之落地；② 之不可達之判（`W-G.9-378`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 新側支 `verify/W-G.9-378-gb204`（`W-G.9-378` 工項二之後）；主線 ＝ `02cc0cb8e83a966f6193c41b02c6093e59f74f84`（⛔ 動）。**授權** ＝ `docs/orders/W-G.9-378_規格單.md`。本節⛔ 鑄號。

### ① 之落地（新側支）

失效條件（本簿 `GB-204` 立項節逐字之前段）：「四表皆依 `_pre965` 之式減入池閘之帳（`入池閘部分併出` 與單元之 `入池閘成員部分併出`）」。
**現況**：五處之試算（段三之 harness 與畫面之 `alloc_state`、手冊先行之 harness 與畫面之試算、第一趟之 `adj4_trial_state`）之回傳於 `members` 之外另回 `pool_out`（`app.py` 之新純函式 `k967_pool_out`·其 build 與 `members` 同）；四表（段三之第 `5` 項、手冊先行之計畫時與 `K-9-51`、第一趟之各輪）建成之後各以 `k967_pool_less` 減其**同一試算**之 `pool_out`（`W-G.9-378` 規格單 `R-1`〜`R-4`）。量測器：`F27` 之 `B4`〜`B6`（二純函式）、`Y8`（五處之接線）；`F28` 之 `D1`〜`D3`（三處之表·同一試算之配對）。本案⛔ 觸（本案入池閘無依手冊部分併入之宗 ⇒ `pool_out` 恆空·`W-G.9-378` 規格單 `§一` 項 `6`）。
⇒ 前段於新側支成就；**入主線時（次單）解除 ①**。

### ② 之判（現行管線中不可達）

立項節之 ② 逐字：「該片其後為下游整筆去出 build 者，其帳⛔ 達調配之輸入 ⇒ 配地街廓缺其受併宗之街廓」；其「情形」逐字：「該片其後為下游（手冊先行等）整筆去出 build 者」。
**實查**（`02cc0cb`）：
- （單趟之管線之序·末次之調配之輸入）調配之輸入之 build ＝ 末次入池閘之出：畫面之 `SS_ADJ_BUILD_FINAL` 全檔唯一之寫在 `f3_screen_stepg_run` 之入池閘之關（`_k929_6_screen_gate`）之後（`app.py:21825`·該關 `:20325`）；
- 畫面之 `main` 先跑段三（含末端塊合併再試、手冊先行、第一趟·`f3_screen_k6b_stage3` `:28236`），後跑 step G（含入池閘·`f3_screen_stepg_run` `:28613`）；
- harness 之 `main`（`verify/run_verification.py`）先 `run_corner_pk_k6b`（`:610`），後以其出之 build 跑 `run_step_g`（`:691`）。
⇒ 手冊先行等皆在末次入池閘之**前**；末次入池閘之後、調配之輸入之前⛔ 有去出 build 之步。三處之試算中之入池閘之帳唯及其試算（⛔ 達調配之輸入·亦⛔ 須達）。
⇒ **② 於現行管線不可達**；其守 ＝ `F27` 之 `Y9`（以源碼之序量之；管線之序或調配之輸入之 build 之源變 ⇒ 紅）。畫面之段三於 step G 之後重跑而 step G 未重跑之顯示之事（審查者之警示·非 ②）另列待查（`CLAUDE.md` 待落地清單 `W-G.9-378` 之節之序 `9`）。立項節之此一情形之前提有誤（`自誤 606`）。
🔒 **`GB-204` 之解除** 唯繫於 ①（入主線）；② 以 `Y9` 守之，⛔ 另立失效條件。
````

## 附錄壬　塊 `E21`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末·工項三）

````markdown

---

**取號**（`W-G.9-378 §零-1`）：本批取 `605`、`606`（`2` 號）——發單側窗八十之自捕。

### 🩸 `自誤 605`　**`W-G.9-377` 塊 `Fv27` 之 `mutate` 以「過／不過」二分回出艙碼：錨數 ≠ `1`、子程序逾時或例外、基準⛔ 全綠（皆無從判定）與「突變未被捕」（判定為偽）同回 `rc 1`——違 `CLAUDE.md` 之常規與該器之說明文**

**形**：`W-G.9-377` 塊 `Fv27`（`verify/probes/probe_WG9373_k966.py` 之 `mutate`）之末逐字「`return 1 if bad else 0`」，其 `bad` 兼收上開四態；該器之說明文逐字「`3 無從判定`」；`CLAUDE.md`（`02cc0cb`·`:207`）逐字「「**無從判定**」與「**判定為偽**」⛔ **不得共用同一出艙碼**」。
**後果之界**：零土地後果；唯生假紅（⛔ 假綠）——一次「算不出」得被讀為「量測器漏量」而送出假警報；`W-G.9-377` 之實跑⛔ 見此三態。
**根因**：新器之出艙碼以「過／不過」二分撰之，⛔ 對倉之常設規則（「我算不出」與「為偽」之分）與本器自身之說明文逐支核之。
**後果之框**：🟡 CC 之唯讀 reviewer 察之（`W-G.9-377R` ⑨·⛔ 停機·呈發單側）；發單側窗八十判之（成立）。
**攔法**：`W-G.9-378` 塊 `Fw27`：無從判定 ⇒ `rc 3`、末列另載「無從判定 […]」；二者並見 ⇒ `rc 1`。通則：新器之每一失敗之支，先定其屬「判定為偽」或「無從判定」，二者之出艙碼與末列之字樣分立。

### 🩸 `自誤 606`　**`GB-204` 立項節以「手冊先行等」為入池閘之下游而立其 ②（部分併出之片其後整筆去出 build ⇒ 其帳⛔ 達調配之輸入）——⛔ 實查管線之序；手冊先行等皆在末次入池閘之前，② 不可達**

**形**：`W-G.9-376` 塊 `G12`（`GB-204` 立項節）逐字「該片其後為下游（手冊先行等）整筆去出 build 者，其入池閘之帳⛔ 達調配之輸入」；實查（`02cc0cb`）：畫面之 `main` 先段三（含手冊先行、第一趟·`app.py:28236`）後 step G（含入池閘·`:28613`）；harness 之 `main` 先 `run_corner_pk_k6b`（`verify/run_verification.py:610`）後 `run_step_g`（`:691`）；調配之輸入之 build（`SS_ADJ_BUILD_FINAL`）唯一寫於入池閘之關之後（`app.py:21825`）。
**後果之界**：零土地後果；阻塞項登記一不可達之情形，致落地之單須另核之（`W-G.9-378` 規格單 `§一` 項 `5`）；若照立項節之「失效條件」之後段實作，將於調配之輸入增一無受詞之支。
**根因**：承唯讀審查（`W-G.9-375` 停機報告 `§三` B3）之警示而登記，唯核「四表之式」與「調配之輸入之帳之源」，⛔ 以呼叫之序實查「下游」之存否（存在之斷言⛔ 經全倉之查）。
**後果之框**：🟢 發單側窗八十擬落地之單時自捕。
**攔法**：本簿 `GB-204` 之進度節之「② 之判」；量測器 `F27` 之 `Y9`。通則：登記「其後」「下游」之情形者，先以呼叫之序（畫面之 `main` 與 harness 之 `main`）實查其先後並書其處。
````

## 附錄癸　塊 `P31`（附於 `CLAUDE.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`GB-204` ①（重劃前面積之表減入池閘之帳）入新側支；`GB-204` ② 之不可達之判；量測器 `F27 mutate` 之出艙碼（`W-G.9-378`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `02cc0cb8e83a966f6193c41b02c6093e59f74f84`（⛔ 動）；新側支 `verify/W-G.9-378-gb204`（`W-G.9-378` 工項零〜四）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `GB-204` ①（前節序 `5`） | 五處之試算回 `pool_out`（`k967_pool_out`）；四表減其同一試算之帳（`k967_pool_less`）；量測器 `F27` `B4`〜`B6`／`Y8`、`F28` `D1`〜`D3` | 🔶（新側支） | `docs/orders/W-G.9-378_規格單.md`；`GB` 簿 `GB-204` 之進度節 |
| `2` | `GB-204` ② | 現行管線中不可達（手冊先行等皆在末次入池閘之前）；以 `F27` 之 `Y9` 守之；`自誤 606` | 🔶（新側支·判·⛔ 改碼；其守 `Y9` 在新側支） | 同序 `1` |
| `3` | 前節序 `4`（`W-G.9-373R` NOTE `1`·`adj4_pass1_run` 之 `_rkey_a4` 之上之舊註） | 改述為現行之重劃前面積之式（`規格單 R-5`） | 🔶（新側支） | 同序 `1` |
| `4` | 量測器 `F27 mutate` 之出艙碼（`自誤 605`） | 無從判定 ⇒ `3`、未捕 ⇒ `1`、並見 ⇒ `1` | 🔶（新側支） | 同序 `1` |
| `5` | 入主線 ＋ KL 之畫面核對 ＋ 主 checkout 之同步 | 本批·生產碼·本案之配地⛔ 變 | ⬜ | 次單 |
| `6` | `W-G.9-375` 之【工】巳之三停機（前節序 `6`） | 逐一附圖呈 KL 其處置 | ⬜ | 另單 |
| `7` | `K-9-58` ④、`K-9-59`〜`K-9-63`（前節序 `7`） | — | ⬜ | `K-9-58` ④〜`K-9-63` 之落地之單（其序另呈 KL） |
| `8` | `自誤 605`、`606` | 見自誤簿 | 🔶（新側支之自誤簿） | 同序 `1` |
| `9` | 畫面於 step G 之後再跑段三而未再跑 step G 者，調配之輸入之顯示或配前次之入池閘之末態 build（`SS_ADJ_BUILD_FINAL` 唯 step G 之始清之） | 唯讀獨立審查之警示（`W-G.9-378` 擬單時）·非 `GB-204` ②·可達與否未驗·⛔ 鑄號 | ⬜ | 待查（另單·⛔ 急） |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：以程式字樣為錨之接線與突變之判別力之補寫（……）（`W-G.9-377`）」節之序 `4`、`5` ⇒ 本表序 `3`、`1`（🔶 新側支）；其序 `6`、`7` ⇒ 本表序 `6`、`7`（態⛔ 變）；其餘之序之態⛔ 變。
🔒 **本案之量**：本批⛔ 變配地（本案入池閘無依手冊部分併入之宗 ⇒ `pool_out` 恆空、四表⛔ 變·`W-G.9-378` 規格單 `§一` 項 `6`）。
🔒 **依賴序**：序 `5`（入主線）→ 序 `6` → 序 `7`（其序另呈 KL）→ 規格步 `5` → `6` → `7`／`8`；`GB-196`、`GB-197`、`GB-198`、`GB-202` 與序 `9` 另單（⛔ 急）。
🔒 **本機介面**：同前節（⛔ 變）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `8`（子字串框·含圖例與本列）·列 ＝ `6`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: 6bad5a086700444b83a0448da8a7b0954a3619d44d64b204215e8d3f2a7fb118
