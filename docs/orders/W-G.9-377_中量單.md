# `W-G.9-377`　中量單：以程式字樣為錨之接線與突變之判別力之補寫（`F27` 之 `mutate`／`Y7`／`T5`）＋ `W-G.9-373` 補令二 `§三` 之⛔ 量之二項（`F28` 之 `L4`〜`L6`）＋ 量測器 `F29` 之增例（`K50`·`自誤 603`）＋ `自誤 604` ＋ 待落地清單之更新 ＋ 主 checkout 之同步

> **本單建議等級 ＝ `high`**（本單⛔ 令 CC 撰寫生產碼；受詞 ＝ 量測器三檔之純增〔塊 `Fv27`／`Fv28`／`Fv29`·`git apply`〕、二簿之純末端追加〔塊 `E20`／`P30`〕、本單與報告二新檔、主 checkout 之同步）。
> **發單** ＝ 發單側窗八十·`2026-10-11`。**受單** ＝ CC 新窗（工項零〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**）。
> **級** ＝ **中**（⛔ 撰生產碼——生產碼 `34` 檔〔`app.py` ＋ `verify/` 頂層 `*.py`〕一字⛔ 動；`verify/probes/` 唯三器；⛔ 跑 `run_verification.py`／`run_all`——本批⛔ 動受測碼，配地⛔ 變；收工閘跑量測器之 `selftest`／`wiring`／`mutate` 與登記之器〔`closegate`、`issuer_anchor`、`checkidx`、`gen_fa_index`〕）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `a3925f1037f96277c690940303f0332df782e3d7`（`W-G.9-376` 工項二）；側支 `verify/W-G.9-375-k965` ＝ `96bd6fe5daa32bbbb82564f733e5ec875cd740ab`、`verify/W-G.9-373-k966` ＝ `cf08e23f11b3193a0bc2657bf7964562615ab5df`、`verify/W-G.9-370-selfchk` ＝ `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`、`verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`；遠端 heads `39`；KL 之主 checkout 停於 `a3925f1`（分支 `wip/s1-endpart`·`§二` 之 KL `07:43` 之出艙）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `Fv27`／`Fv28`／`Fv29`／`E20`／`P30` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`自誤 479`）；Bash 之輸出路徑一律單引號之絕對路徑（`W-G.9-373` 補令二單首）。Bash 命令⛔ 含 heredoc（常設規則索引）。`<O>` ＝ CC 自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`·本單起）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列（近例之形·`Co-Authored-By` 等）；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-377_中量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項四之撞檔前置必觸發，依其處置（`自誤 542`）。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔之一字；`verify/` 除 `verify/probes/probe_WG9373_k966.py`、`verify/probes/probe_WG9373p1_partrem.py`、`verify/probes/probe_WG9375_k965.py` 三檔之純增（塊 `Fv27`／`Fv28`／`Fv29`）外之一字；任何錨之改；`verify/baselines`；`K-6` 典、`GB` 簿、`VR` 簿、恆常附款登記表、常設規則索引、`docs/specs/`、`docs/配地計算總規格_v3.md`、`.claude/` 之一字；自誤簿、`CLAUDE.md` 除塊 `E20`／`P30` 之純末端追加外之一字；任何側支之推送、刪除或改寫（四側支皆留其值·⛔ 再推）。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止；塊之文字 CC ⛔ 改一字，認為其與倉之事實不符者照實回報（停機款 `12`）。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `a3925f1037f96277c690940303f0332df782e3d7`；四側支之 `git rev-parse` ＝ 單首之值；`git ls-remote --heads origin` 之列數 ＝ `39`（全 `39` 列存 `<O>\heads_before.txt`·收工閘 `5` 用）；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 603 599` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `588`／`MAX` `603`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `196`／`204`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `67`／`70`／`[44, 47]`（＝ `W-G.9-376` 收工閘 `7` 之期·發單側窗八十於 `a3925f1` 重跑同）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態 `a3925f1` 之 `docs/` 全檔 **`1004`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗八十實跑 `python verify/probes/wg9268_gate6_occupancy.py a3925f1 W-G.9-377 W-G.9-376 W-G.9-397`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-377`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取（器另示「鬆框亦 `0` ⇒ ⛔ 漏框之虞」：`W-G.9-376` 唯稱「次單」·⛔ 書其號） |
| 對照甲［必非零］`W-G.9-376` | `2`／`8`／`6` | `2`／`8`／`6` | `14` | `4` | `5`／`48` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-397` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `20`／`31` | 🟢 宣告框之嚴格 `0`、鬆框非零（器之標籤「甲（須 ≥1）」依本表之角色讀之·同 `W-G.9-365R` ⑥ 自解 `1`） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`6` | `0`（寬式 `6`） | `0`（寬式 `3`） | `48`／`53` | 🟡 寬式 `D3` 非零：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `a3925f1` 之追蹤檔 **`2829`** 檔·列框；發單側窗八十以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``〕於 `a3925f1` 實算）：

| 號 | 裸（錨定）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 604` | `32` | `0` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——`sha256`／`commit` 之子字串、行號、bytes 等） |
| 對照甲［必非零］`自誤 603` | `143` | `6` | `0` | `6` | 🟢 框非恆空 |

**塊名與新名**（母體同上·檔框／列框·`git grep -l`／`git grep -c` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fv27`／`Fv28`／`Fv29`／`E20`／`P30`（逐名） | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`E19` | `1`／`4` | `2`／`11` | 🟢 框非恆空 |
| 對照甲［必非零］`P29` | `2`／`11` | `2`／`18` | 🟢 框非恆空 |
| 報告名 `W-G.9-377R`（`-F`） | `0`／`0` | `0`／`0` | 🟢 ⛔ 撞名 |

🔒 `Fd28`、`Fd29` 已為他單之塊名（`W-G.9-373` 補令二、`W-G.9-375` 補令一·各 `2` 檔）⇒ 本單之量測器之塊名用 `Fv`。

自誤 `MAX` ＝ `603`、`GB` `MAX` ＝ `204`、`K-9` `MAX` ＝ `70`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 604`（塊 `E20`）；⛔ 鑄 `GB`／`K-9`／`VR`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `a3925f1`，或四側支之任一 ≠ 單首之值，或施工樹之追蹤檔有變動，或遠端 heads ≠ `39`，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fv27`／`Fv28`／`Fv29`／`E20`／`P30` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `git apply --check` 不過；或施後之 blob ≠ `§五-1` |
| `4` | 三器之任一之刪除欄 ≠ `0`；或二簿任一之刪除欄 ≠ `0`、改前全檔非改後之嚴格前綴、改後之尾 ≠ 其塊 |
| `5` | 工項一之驗（`§三` 工項一項 `4`）任一 ≠ 期 |
| `6` | 工項二之 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `7` | `§四` 收工閘任一 ≠ 期 |
| `8` | 工項四：主 checkout 之追蹤檔有變動；開工時其 `HEAD` ≠ `a3925f1…` 或其分支 ≠ `wip/s1-endpart`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9` | 工項零〜三之任一 `push` 之目標非 `wip/s1-endpart`、或須 `--force`；或任一 `push` 至側支 |
| `10` | `mutate` 之子程序逾時（單一突變逾 `600` 秒）或基準 `N00` 非全綠 |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中（⛔ 加 `--no-index` 者對已追蹤之檔恆不報·⛔ 用） |
| `12` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或 CC 認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `8`。

---

## `§一`　態錨（發單側窗八十自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`·Python `3.13.16`·`numpy 2.4.6`〔`GB-198`〕·`shapely 2.2.0`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `a3925f1037f96277c690940303f0332df782e3d7`（`96bd6fe` 之後三筆：`598e1ba` 工項零 → `ade6891` 工項一 → `a3925f1` 工項二·`W-G.9-376`）；四側支 ＝ 單首；遠端 heads **`39`**；`a3925f1` 之追蹤檔 `2829` |
| `2` | 生產碼 `34` 檔 | ＝ `96bd6fe`（`app.py` `d6218273e0ba3cdf45598a37968eac6d907ebb58`、`verify/stepg_pipeline.py` `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`、`verify/selection_pipeline.py` `96cbf3ffbdd36bbf4d02bf10e9635bbf69b5926c`）；對 `981f143` 相異 `3` 檔（`W-G.9-376` 收工閘 `2` 之判別力） |
| `3` | 三器（施前） | `verify/probes/probe_WG9373_k966.py`（`F27`）`64559114764758645af0f3ce1fa24643b855fb82`；`verify/probes/probe_WG9373p1_partrem.py`（`F28`）`1daec0ce619789b626e57c317658afe7f4e59f8d`；`verify/probes/probe_WG9375_k965.py`（`F29`）`1ea99b72e891a2c4d642b5fcdf9248e0c15e3e66` |
| `4` | 二簿（施前）與他簿 | `docs/reports/W-G.9波_claude.ai側自誤登記.md` `1165190` B（blob `5cf217beea6566f9d411eb7a408df9bcf7bc477d`）；`CLAUDE.md` `377034` B（`bb2a928103a571ec4ebf24b28b329c6c8fa944b4`）；`K-6` 典 `5fab239a68b58ef042d38d7a731eb8b5eade5f03`（`684846` B）、`GB` 簿 `7d56b5328c2c3968b9425992544848d92f70a503`（`1054032` B）——本批⛔ 動；皆以換行結尾·CR `0`（判別力：`data/V6.dxf` ＝ `12308`） |
| `5` | `W-G.9-376` 之復驗（發單側窗八十·倉外·⛔ 採 CC 之自報） | `W-G.9-376 §三` 工項零′ 之前置 `1`〜`3`（`8`／`0`·合併 `0`；`:(glob)` 形恰 `3` 列〔無之則 `10` 列〕；逐筆判命中者唯 `9fc8e5b`〔`3` 列〕）、快轉後 ③④、`§四` 收工閘 `1`〜`9` 皆 ＝ 期；四簿之尾 ＝ 自該單機械抽出之四塊（逐位）；`W-G.9-376R` 所載之 KL 之逐字 ＝ 交接文；KL 之主 checkout ＝ `a3925f1`（`§二` 之 KL `07:43` 之出艙） |
| `6` | 本批之所由（量測器之現況） | `W-G.9-373` 改寫三處（段三後處理 `k6b_stage3_run`、手冊先行 `k953_manual_run`、第一趟 `adj4_pass1_run`）而退 `F17` 之 `W2`／`W3`／`W12` 與其突變、`F25` 之 `M01`〜`M19`／`M28`／`M29`／`M31`（其錨已去）；其代「以 CC 之碼之字樣為錨補寫」迄未辦（`CLAUDE.md` 待落地清單 `W-G.9-376` 之節之序 `6`）。`W-G.9-375`（`K-9-65`）⛔ 改此三處 ⇒ 其錨 ＝ `a3925f1` 之碼。發單側窗八十於倉外施突變 `57` 種於現行之碼（`§五-1` 項 `10`）：施本單之前，其中 `8` 種（三處之趟中之帳之同一受併宗之覆寫 `3`、手冊先行與第一趟之「輸入之帳 ＋ 最末一次」`2`〔段三之同形既由 `F28` 之 `L1` 捕之〕、三處之重劃前面積之表取輸入之態 `3`）與 `1` 種（手冊先行之第 `1` 輪之來源量⛔ 除 κ）諸器皆綠——即 `W-G.9-373` 補令二 `§三` 所書之⛔ 量之二項與一漏量；本單之 `F28` 之 `L4`〜`L6` 與 `F27` 之 `T5` 捕之 |

---

## `§二`　KL 之語與射程

🔒 **所據**：`W-G.9-376` 中量單 `§二`（逐字）「🔒 **原單 `§四-2` ② 之移**（塊 `P28` 序 `5`、`6`·零生產碼）：本單⛔ 辦，次於本單另單辦之（KL 之語「接續擬 `W-G.9-376`」之受詞 ＝ 請示文「七」之首項·其次項即此）；並增 `F29` 之例（`自誤 603`）——塊 `P29` 序 `6`、`7`。」；`CLAUDE.md` 待落地清單 `W-G.9-376` 之節之序 `6`、`7`。

🔒 **KL 之語**（逐字·`2026-10-11 07:43`·發單側窗八十請 KL 附主 checkout 之出艙之答）：

> C:\Users\admin\Desktop\land-readjustment-trial>   git -C C:\Users\admin\Desktop\land-readjustment-trial log -1 --oneline
> a3925f1 (HEAD -> wip/s1-endpart, origin/wip/s1-endpart) W-G.9-376 工項二：執行報告入倉 ⛔ 零生產碼

🔒 **發單側窗八十之通知**（同日·KL `07:43` 之訊之前·於對話·其文之此段逐字；KL ⛔ 駁）：「另有一點調整，屬通知，你不需判斷：待落地清單序 `7` 是程式裡一句註解已過時。改它仍算動程式檔，而它正好落在 `GB-204` 下一單要改的同一段，所以移到那一單一起改。」⇒ 序 `7`（`W-G.9-373R` NOTE `1`）改於 `GB-204` 之落地之單（塊 `P30` 序 `4`）。

🔒 **放行**：本批⛔ 撰生產碼、⛔ 動受測碼 ⇒ 工項零〜三由 CC 逕行 `push` 至主線（`CLAUDE.md` 之 `常規一`）；工項四於 KL 本機·⛔ `commit`·⛔ `push`。

🛑 **射程**：`(a)` 三器之純增（塊 `Fv27`／`Fv28`／`Fv29`）；`(b)` 二簿之純末端追加（塊 `E20`／`P30`）；`(c)` 本單與報告二新檔；`(d)` 主 checkout 之同步；`(e)` ⛔ 及生產碼、`verify/` 之他檔、任何錨、`.claude/`；`(f)` ⛔ 及塊 `P30` 序 `4`〜`7` 之事項——另單。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-377_中量單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-377 工項零：本單原封入倉 ⛔ 零生產碼`（其後依單首 🔑 之書法）⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　三器之純增（主線·`verify/probes/` 三檔·零生產碼·一 `commit`）

1. 自本單依 `§五-1` 末之抽取式抽出塊 `Fv27`（附錄甲）、`Fv28`（附錄乙）、`Fv29`（附錄丙）為 `<O>\Fv27.diff`、`<O>\Fv28.diff`、`<O>\Fv29.diff`，對拍 `§五-1` 項 `2`〜`4`（停機款 `3`）。
2. `git apply --check <O>\Fv27.diff <O>\Fv28.diff <O>\Fv29.diff` ⇒ `rc 0`；其後 `git apply <O>\Fv27.diff <O>\Fv28.diff <O>\Fv29.diff`。
3. 施後三器之 `git hash-object` ＝ `§五-1` 項 `5`；`git diff --numstat` 唯此三檔、刪除欄皆 `0`（停機款 `3`／`4`）。
4. 驗（皆於施工樹·`<repo>` ＝ 其絕對路徑；出艙存 `<O>`；停機款 `5`）：
   - `python verify/probes/probe_WG9373_k966.py selftest <repo>` ⇒ `rc 0`；末列逐字 `⇒ 紅 []；rc 0`；`T5` ✅；`P0 逐項擾動恰該項紅 28／28`；
   - `python verify/probes/probe_WG9373_k966.py wiring <repo>` ⇒ `rc 0`；`Y1`〜`Y7` 皆 ✅；
   - `python verify/probes/probe_WG9373_k966.py mutate <repo>` ⇒ `rc 0`；末列逐字 `⇒ 突變 57（另基準一）；紅 []；rc 0`（約 `5`〜`10` 分·二並行）；
   - `python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` ⇒ `rc 0`；`L4`〜`L6` ✅；`P0 逐項擾動恰該項紅 26／26`；
   - `python verify/probes/probe_WG9375_k965.py selftest <repo>` ⇒ `rc 0`；`K50` ✅；`P0 判式自驗 50／50`；
   - 諸呼叫之 stderr 合計 `0` B。
5. `commit` 訊息之首列逐字 `W-G.9-377 工項一：F27 之 mutate（N01〜N57）／wiring Y7／selftest T5 ＋ F28 之 L4〜L6 ＋ F29 之 K50 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　`自誤 604` 之登記、待落地清單之更新（主線·零生產碼·一 `commit`）

1. 塊 `E20`（附錄丁）附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P30`（附錄戊）附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 項 `6` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·施後之 blob ＝ `§五-1` 項 `6`·停機款 `3`／`4`）。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P30` 附後：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `6`）。
5. `commit` 訊息之首列逐字 `W-G.9-377 工項二：自誤 604 ＋ 待落地清單之更新（接線與突變之補寫·補令二之⛔ 量之二項·F29 之增例）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-377R_接線與突變之判別力之補寫_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 五塊之實得（bytes／`sha256`／列數）、三器之施前施後 blob 與 numstat、二簿之改前改後 bytes／blob；④ 工項一項 `4` 之全部出艙之末列與 `P0`；⑤ 工項二之 `checkidx`、`gen_fa_index` 之出艙；⑥ `§二` 之 KL 之逐字；⑦ pre-flight 之出艙與逐項之處置；⑧ CC 讀塊時認為與倉之事實不符之處（無則書「無」）；⑨ CC 之自捕與自解；⑩ 各段耗時。收工閘之實測值與工項四之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-377 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ `a3925f1037f96277c690940303f0332df782e3d7`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次將新入之路徑集 `A`（期 ＝ 本單、報告）；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8`）；不等 ⇒ 停機款 `8`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> rev-parse HEAD` ＝ 工項三 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object` 之 `app.py` ＝ `d6218273e0ba3cdf45598a37968eac6d907ebb58`（⛔ 變）、三器 ＝ `§五-1` 項 `5`、`CLAUDE.md` ＝ `§五-1` 項 `6` 之施後之 blob；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。

任一不符 ⇒ 停機款 `8`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之增刪（`git show --numstat`） | 工項零 ＝ 本單 `783`／`0`；工項一 ＝ `verify/probes/probe_WG9373_k966.py` `316`／`0`、`verify/probes/probe_WG9373p1_partrem.py` `97`／`0`、`verify/probes/probe_WG9375_k965.py` `15`／`0`（唯此三檔）；工項二 ＝ `docs/reports/W-G.9波_claude.ai側自誤登記.md` `12`／`0`、`CLAUDE.md` `24`／`0`（唯此二檔）；工項三 ＝ 報告之增／`0`；四筆之首列 ＝ `§三` 所令逐字 |
| `2` | `git diff --name-status a3925f1 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`7`** 列：`A` 本單、`M` 三器、`M` 二簿、`A` 報告；生產碼 `34` 檔對 `a3925f1` 相異 **`0`**（判別力［必非零］：對 `981f143` 相異 **`3`**）；`verify/` 對 `a3925f1` 相異恰三器；本批之新檔（本單、報告）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc`〔不存之路徑亦可〕⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批七檔之 `CR`（真 `0x0D`·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4` | 二簿之 bytes 與三器之 blob | 自誤簿 `1165190` → **`1167087`**；`CLAUDE.md` `377034` → **`380931`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊；三器之 blob ＝ `§五-1` 項 `5` |
| `5` | 自限 | 遠端 heads **`39`**；主線 ＝ 工項三之 `commit`，其祖含 `a3925f1`；四側支皆 ＝ 單首（⛔ 變）；其餘 `34` 列（除 `wip/s1-endpart` 與四側支）逐列 ＝ `<O>\heads_before.txt` |
| `6` | `python verify/probes/probe_WG9270_closegate.py 604 603 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 605 604 .` ⇒ `rc 7` |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 604 603` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`589`**／`MAX` **`604`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `196`／`204`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `67`／`70`／`[44, 47]`（自誤唯增 `604`；餘 ＝ 開工態） |
| `8` | 量測器（於主線之端·`<repo>` ＝ 施工樹之絕對路徑）：`F27` 之 `selftest`／`wiring`／`mutate`；`F28 selftest`；`F29` 之 `selftest`／`wiring`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`（`F23`）；`python verify/probes/probe_WG9367_adj4.py selftest <repo>`（`F24`）；`python verify/probes/probe_WG9357_k948.py selftest <repo>`（`F16`）；`python verify/probes/probe_WG9349_k9296.py selftest <repo>`（`F8`） | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`（`mutate` 之末列逐字 `⇒ 突變 57（另基準一）；紅 []；rc 0`）；`P0` ＝ `28／28`（`F27`）、`26／26`（`F28`）、`50／50`（`F29`）、`40／40`（`F23`）、`28／28`（`F24`）、`25／25`（`F16`）；`F8` 無 `P0`（其 ✅ `37` 列）；`F27 wiring` `Y1`〜`Y7` ✅、`F29 wiring` `Y1`〜`Y9` ✅；stderr 合計 `0` B |
| `8′` | `mutate` 之判別力（倉外之拋棄式工作樹·⛔ `commit`）：`git worktree add --detach <S> HEAD`；`git -C <S> checkout a3925f1 -- verify/probes/probe_WG9373p1_partrem.py`（`F28` 回施前之碼）；`python <S>\verify\probes\probe_WG9373_k966.py mutate <S>`；其後 `git worktree remove --force <S>` | `rc 1`；末列逐字 `⇒ 突變 57（另基準一）；紅 ['N22', 'N23', 'N25', 'N38', 'N39', 'N41', 'N46', 'N47', 'N49']；rc 1`（恰新例 `L4`〜`L6` 所量之九種；餘 `48` 種與基準皆 ✅） |
| `9` | 工項二之項 `3`／`4` 於主線之端重跑 | 同其期 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜三並實跑閘 `1`〜`4`、`6`〜`9` 與 `8′` ⇒ 見 `§五-1` 項 `9`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `Fv27` | `25827` B·`sha256` `2be2129177828b3129ad4ce89f82b2ed59e3dd42c309f0e07cb08c066d168950`·`365` 列（圍欄內全文·末附換行）；`git apply` 於 `verify/probes/probe_WG9373_k966.py`（施前 blob `64559114764758645af0f3ce1fa24643b855fb82`） |
| `3` | 塊 `Fv28` | `8617` B·`sha256` `27d95e356f48efa5fa7cf5c2e4eda86fd429773783bb6e098e4c782c71a94eed`·`122` 列（同上）；`git apply` 於 `verify/probes/probe_WG9373p1_partrem.py`（施前 blob `1daec0ce619789b626e57c317658afe7f4e59f8d`） |
| `4` | 塊 `Fv29` | `2875` B·`sha256` `401bf8ba5a316a141d95ff9860faaafb3e5c6cf8bf5b79ffa35104bd15a50396`·`33` 列（同上）；`git apply` 於 `verify/probes/probe_WG9375_k965.py`（施前 blob `1ea99b72e891a2c4d642b5fcdf9248e0c15e3e66`） |
| `5` | 三器之施後之 blob | `verify/probes/probe_WG9373_k966.py` `2e5c2203a6ac9eb185c12fc8aa1eeda6e5fe4770`（`67226` B）；`verify/probes/probe_WG9373p1_partrem.py` `cafa6ecb2b99a21c78db002b52df82b6a256244a`（`33337` B）；`verify/probes/probe_WG9375_k965.py` `684fd5797e799b8b3932bc03d61a4a87717d8d84`（`69977` B） |
| `6` | 塊 `E20`／`P30` 與二簿之施後之 blob | 塊 `E20` `1897` B·`sha256` `29f69167063309b0333a07484167fa00a32400cf5579a1c2c7bcb7deb6141eb8`·`12` 列（圍欄內全文·末附換行·首列為空列）；塊 `P30` `3897` B·`sha256` `a60ed730899c4e81e5ae3f664dd87f64f83e5c93d3942f9388d58f39ac09f836`·`24` 列（同上·其 payload 內 `⬜` 之子字串框 `9`·列框 `7`〔塊之自載〕）；施後：自誤簿 `4b8e995b6d1cd45f4f17da5479427e00d10d974c`（`1167087` B）、`CLAUDE.md` `ccb5269d17bf8527edb529bebb29efb87919c8ab`（`380931` B） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-376 §五-1` 項 `7`） |
| `8` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗八十實跑（態 `a3925f1`）：🔴 機械 `0` 項／🟡 提示 `2` 項——`P-4` `:158`（`§四` 收工閘之表頭·其箭頭之座標系 ＝ 改前至改後〔閘 `4`〕，表內自載 ⇒ **具名豁免**）、`P-6` `:775`（塊 `P30` 之「前節之更新」·其數皆待落地清單之序號之對應·⛔ 為停機款所繫之實測數 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `22630`–`30350`·本單⛔ 用） |
| `9` | 收工閘之模擬（發單側·本機 Linux·⛔ `push`） | `git worktree add --detach <S> a3925f1`（拋棄式）＋ 本單之定稿（`783` 列·其五塊即附錄甲〜戊）＋ 報告之替身·四 `commit`（首列 ＝ `§三` 所令逐字·其後空一列附尾列）：開場之器 `rc 0`（＝ `§零-0` 項 `3`）；工項零之 blob ＝ 來源；五塊之抽取 ＝ 項 `2`〜`4`、`6`；`git apply --check` `rc 0`；三器之施後 blob ＝ 項 `5`、numstat `316`／`0`、`97`／`0`、`15`／`0`；工項一項 `4` 之五呼叫皆 `rc 0`（`selftest` 之 `P0` `28／28`、`26／26`、`50／50`；`wiring` `Y1`〜`Y7`；`mutate` 末列 `⇒ 突變 57（另基準一）；紅 []；rc 0`）·stderr `0` B；二簿之施後 blob ＝ 項 `6`；`checkidx`／`gen_fa_index` ＝ 期·逐位同；閘 `1` ＝ 工項零 `783`／`0`、工項一 `316`／`97`／`15`（刪皆 `0`）、工項二 `12`／`24`（刪皆 `0`）、工項三（替身）`1`／`0`；閘 `2` ＝ `7` 列·生產碼對 `a3925f1` 相異 `0`、對 `981f143` `3`·`verify/` 對 `a3925f1` `3`·新檔二之 `git check-ignore -v --no-index` 無命中（對照 `rc 0`）；閘 `3` 七檔 `CR` `0`（`data/V6.dxf` `12308`）；閘 `4` 二簿皆嚴格前綴、其尾 ＝ 塊；閘 `6` `rc 0`（判別力 `605 604` ⇒ `rc 7`）；閘 `7` `rc 0`（＝ `§四` 閘 `7` 之期）；閘 `8` 十呼叫皆 `rc 0`·末列皆 ＝ 期·`P0` 皆 ＝ 期·stderr `0` B；閘 `8′` `rc 1`·末列 ＝ 期；閘 `9` ＝ 工項二之項 `3`／`4`；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空 |
| `10` | 突變之判別力（發單側窗八十·倉外·⛔ 為 CC 之期） | ① 本單之 `MUT377` 之 `57` 種施於 `a3925f1` 之碼、以施前之五器之 `selftest` 量之：`48` 種各有其項轉紅；`9` 種諸器皆綠（`N22`、`N25`、`N38`、`N39`、`N41`、`N46`、`N47`、`N49`、`N42`）——前八種為 `W-G.9-373` 補令二 `§三` 之⛔ 量之二項、`N42` 為手冊先行之第 `1` 輪之來源量⛔ 除 κ（玩具之地價皆同·κ ＝ `1`）；施本單之塊後 `57` 種皆有其所指之項轉紅（閘 `8′` 即其反面）。② ⛔ 列者：手冊先行之 `K-9-51` 之候選之序「距離 → 本街廓者先」之對調（等價·`Fv27` 之說明文）；致無窮迴圈之三種（`k966_block_merge` 之二分法之中點改取下整、段三與手冊先行之候選之指標⛔ 前進）——其察唯繫於逾時而非所指之項，⛔ 列。③ `K50` 之判別力：`k929_6_fixpoint` 改為「回原狀時記相連否、①′ 於判時以（所記之相連否, 判時之 `k967_rank`）重排帳之序」（二處之改）⇒ `F29 selftest` 唯 `K50` 紅（餘 `49` 例皆綠·`P0` `50／50`）——即 `自誤 603` 所書之未量之性質。④ `L4`〜`L6` 之期值手算（各函式之說明文）；其同形而⛔ 帶前帳者（倉外）之表值各為 `8.0`／`30.0`／`70.0`（＝ `60 − 52`、`60 − 30`、`90 − 20`），亦與手算同 |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`／`## 附錄乙`／`## 附錄丙`／`## 附錄丁`／`## 附錄戊` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜三 ⇒ 逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）。
3. 收工後，主 checkout 之根之來源檔（本單，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `Fv27`（`git apply` 之差異·`verify/probes/probe_WG9373_k966.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9373_k966.py b/verify/probes/probe_WG9373_k966.py
index 6455911..2e5c220 100644
--- a/verify/probes/probe_WG9373_k966.py
+++ b/verify/probes/probe_WG9373_k966.py
@@ -28,9 +28,21 @@
            `G014`）之 `628-28(1)`／`628-29(1)` 應分配面積並列（`0.01 ㎡`），其重劃前面積亦同（`114.00`）⇒ 取暫編地號小者
            `628-28(1)`（＝ 現行）；`R6` 之代表宗 ＝ `628-21(1)`（G 最大·非並列）；R3 段三之試算（harness 與畫面·同一宗地）
            之 `members` 相同，且含入池閘之單元之成員。
+  🔧 `W-G.9-377`（⛔ 上列一字不刪）：
+  selftest 增 T5（手冊先行之第 1 輪之來源量 ＝ 計畫之量 ÷ κ·玩具之地價 BB 為 BA 之半）；P0 隨之 28 項。
+  wiring   增 Y7（三處之 `k966_block_merge` 皆以 `state` 為前態、以其回傳之態承接·`F17` 之 W2 之代）。
+  mutate   <repo>
+           以受測碼之字樣為錨之突變 N01〜N57（`MUT377`·`F17` 之 W2／W3／W12 與 `F25` 之 M01〜M19／M28／M29／M31 之代·
+           `k966_block_merge`、`k967_rank`／`k967_pre_area`、三處之試施·輪·候選·趟中之帳·表之取態·段三步驟 10、調配之輸入）：
+           每一突變於 `app.py` 之所指函式之區間錨恰一見，施之於倉外之暫存之 `app.py`，以子程序跑本器、F28、F23、F24、F16
+           之 selftest 之項，其「所指之項」皆須紅；另跑基準一（⛔ 突變·五器之項皆綠）。受測碼之該段改寫者其錨隨之更新（另單）。
+           ⛔ 列者（明書之）：手冊先行之 K-9-51 之候選之序「距離 → 本街廓者先」之對調——距離取片至街廓之形（該街廓之片之
+           聯集）之距離，本街廓者恆為 0 ⇒ 對調為等價之突變（行為⛔ 異）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, importlib.util, io, os, re, sys, warnings
+import json, shutil, subprocess, tempfile                            # 🆕 `W-G.9-377`（mutate）
+from concurrent.futures import ThreadPoolExecutor                    # 🆕 `W-G.9-377`（mutate）
 
 try:
     sys.stdout.reconfigure(encoding="utf-8")
@@ -272,6 +284,23 @@ def _t3(ns):
     return ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, st, log_print=lambda *x: None)
 
 
+def _t5(ns):
+    """🆕 `W-G.9-377`：`T1` 之形而 BB 之地價為 BA 之半（併入 BB 者 a′ ＝ 2a·κ ＝ 2）：第 1 輪之要求之來源量 ＝ 計畫之量 ÷ κ
+    （X 60／Y 50／Z 40）；BB 之容量 130 ⇒ 2 × Σv ≤ 130 ⇒ 比例 130 ÷ 300 ＝ 0.433333：X 26（A1 得 52）、Y 21.67（B1 得 43.33）、
+    Z 17.33（C1 得 34.67）；甲之剩下 34 依距離全入 BD 之 A2（κ ＝ 1）；乙丙之剩下入合併單位。"""
+    t = [_tp("X(1)", "BA", H, _R(0, 10, 0, 30), 60), _tp("Y(1)", "BA", H, _R(10, 20, 0, 30), 50),
+         _tp("Z(1)", "BA", H, _R(20, 30, 0, 30), 40),
+         _tp("A1(1)", "BB", H, _R(0, 10, 30, 60), 300), _tp("B1(1)", "BB", H, _R(10, 20, 30, 60), 300),
+         _tp("C1(1)", "BB", H, _R(20, 30, 30, 60), 300), _tp("A2(1)", "BD", H, _R(40, 50, 0, 30), 300)]
+    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
+    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
+    _ap, st = _cbs({"BB": 130.0}, drop=("X(1)", "Y(1)", "Z(1)"))
+
+    def ap(src, dst):
+        return _a(src) * (2.0 if dst.get("所屬街廓") == "BB" else 1.0)
+    return ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, st, log_print=lambda *x: None)
+
+
 def _rows953(res):
     return [(r.get("序"), r.get("片"), r.get("受併宗") if isinstance(r.get("受併宗"), str) else tuple(r.get("受併宗")),
              _q(r), r.get("結果")) for r in res[2] if r.get("序") in ("K-9-66", "手冊", "K-9-51")]
@@ -456,6 +485,21 @@ def _cases(ns, sp):
           {"X(1)": {"段三併出": ("A1(1)", "A2(1)"), "段三部分併出": (("A1(1)", 30.0), ("A2(1)", 15.0))},
            "Y(1)": {"段三併出": ("B1(1)", "B2(1)"), "段三部分併出": (("B1(1)", 20.0), ("B2(1)", 10.0))}},
           {"A1(1)": 30.0, "A2(1)": 15.0, "B1(1)": 20.0, "B2(1)": 10.0, "X(1)": -45.0, "Y(1)": -30.0}))
+    # 🆕 `W-G.9-377`
+    _run(out, "T5 手冊先行·第 1 輪之來源量 ＝ 計畫之量 ÷ κ（BB 之 κ ＝ 2）⇒ 比例 0.433333：A1 52／B1 43.33／C1 34.67；"
+              "甲之剩下 34 全入 A2；帳以來源量計（Y 21.67／Z 17.33）",
+         lambda: (lambda r: (_rows953(r), _keys(r[0]), _acc(r[0])))(_t5(ns)),
+         ([("K-9-66", "3 片", "—", (), "整體未成；建地部分成（0.433333）"),
+           ("手冊", "X(1)", "A1(1)", (("A1(1)", 52.0),), "部分成"),
+           ("手冊", "Y(1)", "B1(1)", (("B1(1)", 43.33),), "部分成"),
+           ("手冊", "Z(1)", "C1(1)", (("C1(1)", 34.67),), "部分成"),
+           ("K-9-51", "X(1)", "A2(1)", (("A2(1)", 34.0),), "成"),
+           ("K-9-51", "Y(1)", "—", (), "入合併單位"),
+           ("K-9-51", "Z(1)", "—", (), "入合併單位")],
+          {"X(1)": {"段三併出": ("A1(1)", "A2(1)")},
+           "Y(1)": {"段三併出": ("B1(1)",), "段三部分併出": (("B1(1)", 21.67),)},
+           "Z(1)": {"段三併出": ("C1(1)",), "段三部分併出": (("C1(1)", 17.33),)}},
+          {"A1(1)": 52.0, "A2(1)": 34.0, "B1(1)": 43.33, "C1(1)": 34.67, "Y(1)": -21.67, "Z(1)": -17.33}))
     # ── U ──
     _run(out, "U0 段三後處理·對照：整批即過 ⇒ 二列皆成（⛔ K-9-66 之列）",
          lambda: _u(ns, {"B3": 1000.0})[0],
@@ -631,6 +675,19 @@ def _wiring_checks(app):
             if isinstance(x, ast.Constant) and isinstance(x.value, str) and "應分配面積並列" in x.value:
                 old.append(nm)
     chk.append(("Y6 擇宗⛔ 以「並列 ⇒ 停機」", not old, f"{old}"))
+    # 🆕 `W-G.9-377`（`F17` 之 W2 之代·所施者 ＝ 末次通過之試所回之態）：三處之 k966_block_merge 之呼叫皆為
+    #   `state, … = k966_block_merge(state, …)`（以其前態為輸入、以其回傳之態承接）
+    thr = {}
+    for nm in PLACES[:3]:
+        f = top.get(nm)
+        asg = [a for a in ast.walk(f) if isinstance(a, ast.Assign) and isinstance(a.value, ast.Call)
+               and isinstance(a.value.func, ast.Name) and a.value.func.id == "k966_block_merge"] if f else []
+        thr[nm] = [len(a.targets) == 1 and isinstance(a.targets[0], ast.Tuple) and len(a.targets[0].elts) == 3
+                   and isinstance(a.targets[0].elts[0], ast.Name) and a.targets[0].elts[0].id == "state"
+                   and bool(a.value.args) and isinstance(a.value.args[0], ast.Name) and a.value.args[0].id == "state"
+                   for a in asg]
+    chk.append(("Y7 三處之 k966_block_merge 皆以 state 為前態、以其回傳之態承接（state, … ＝ …(state, …)）",
+                all(v == [True] for v in thr.values()), f"{thr}"))
     return chk
 
 
@@ -645,6 +702,261 @@ def wiring(repo):
     return 1 if red else 0
 
 
+# ── 🆕 `W-G.9-377` mutate：以受測碼之字樣為錨之突變（`F17` 之 W2／W3／W12 與 `F25` 之 M01〜M19／M28／M29／M31 之代）──
+#   各為 (號, 條, 述, 函式, 錨, 換, 所指之項)；錨須於該函式之區間恰一見；所指之項 ＝ 「器:項」（F27 本器、F28、F23、F24、F16
+#   之 selftest 之項），施突變後其皆須紅。受測碼之該段改寫者，其錨隨之更新（另單）。
+_BM, _RK, _PA = "k966_block_merge", "k967_rank", "k967_pre_area"
+_S3, _MN, _A4, _AI = "k6b_stage3_run", "k953_manual_run", "adj4_pass1_run", "adj_intake"
+MUT377 = [
+    ("N01", "K-9-66 ①", "整體成而⛔ 回", _BM,
+     "    if _new966 is not None:\n        return _new966, list(_s966)",
+     "    if False:\n        return _new966, list(_s966)",
+     {"F27:A3"}),
+    ("N02", "K-9-66 ②", "唯一類者亦以該類之全量再試", _BM, "        if len(_have966) > 1:\n", "        if len(_have966) >= 1:\n",
+     {"F27:A4"}),
+    ("N03", "K-9-66 ②", "類之序反之", _BM, "    for _j966, _k966 in enumerate(_have966):",
+     "    for _j966, _k966 in enumerate(_have966[::-1]):", {"F27:A2", "F27:A6"}),
+    ("N04", "K-9-66 通知 2", "格改 0.1", _BM, "def k966_block_merge(state, claims, try_apply, *, grid=K966_GRID):",
+     "def k966_block_merge(state, claims, try_apply, *, grid=K966_GRID * 10):", {"F27:A5"}),
+    ("N05", "K-9-66 ②", "按比例之後仍試次類", _BM,
+     "'由': f'{_k966}未全入（K-9-66）'})\n        break\n", "'由': f'{_k966}未全入（K-9-66）'})\n", {"F27:A1", "F27:A7"}),
+    ("N06", "K-9-66", "回傳輸入之態（⛔ 末次通過之態）", _BM, "    return _cur966, _got966, _steps966",
+     "    return state, _got966, _steps966", {"F27:A9"}),
+    ("N07", "K-9-66 ②", "二分法之支反之", _BM, "            if _new966 is None:\n                _hi966",
+     "            if _new966 is not None:\n                _hi966", {"F27:A1"}),
+    ("N08", "K-9-66", "要求之類之停機去之", _BM, "        if _c966.get('cls') not in K966_CLASSES:", "        if False:",
+     {"F27:A8"}),
+    ("N09", "K-9-66 ②", "二分法⛔ 記通過之態", _BM, "                _lo966, _win966 = _md966, _new966",
+     "                _lo966 = _md966", {"F27:A9"}),
+    ("N10", "K-9-66 ②", "試之量與所記之量不一", _BM, "_s966[_i966] * (_md966 * grid) / _sum966)",
+     "_s966[_i966] * (_md966 * grid) / _sum966 * 1.0001)", {"F27:A1"}),
+    ("N11", "K-9-66 ②", "類之全量成而⛔ 承接其態", _BM, "                _cur966 = _new966\n                for _i966 in _ix966:",
+     "                for _i966 in _ix966:", {"F27:A2", "F27:A6"}),
+    ("N12", "K-9-67", "去重劃前面積之鍵", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
+     "return (-adj_q2(g), str(pid))", {"F27:C1"}),
+    ("N13", "K-9-67", "應分配面積⛔ 以 0.01 ㎡ 量化", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
+     "return (-float(g), -adj_q2(pre_area), str(pid))", {"F27:C2"}),
+    ("N14", "K-9-67", "重劃前面積之序反之", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
+     "return (-adj_q2(g), adj_q2(pre_area), str(pid))", {"F27:B1", "F27:C1"}),
+    ("N15", "K-9-67", "重劃前面積先於應分配面積", _RK, "return (-adj_q2(g), -adj_q2(pre_area), str(pid))",
+     "return (-adj_q2(pre_area), -adj_q2(g), str(pid))", {"F27:B1"}),
+    ("N16", "K-9-67", "成員缺⛔ 取自身", _PA, "    for _m967 in (members or [pid]):", "    for _m967 in (members or []):",
+     {"F27:B3"}),
+    ("N17", "K-9-68", "段三：一輪之要求⛔ 依受併之街廓分組", _S3,
+     "            _b = _blk_of[e['r']]\n            if _b not in _bg:",
+     "            _b = _blk_of[e['r']]\n            _bg.pop(_b, None)\n            if _b not in _bg:", {"F27:U1"}),
+    ("N18", "K-9-51", "段三：第 5 項之候選⛔ 扣已試而未全收之街廓", _S3,
+     "if _p == x or _p in merged_out or _b in F.get(x, set()) or _p not in state[\"by\"]:",
+     "if _p == x or _p in merged_out or _p not in state[\"by\"]:", {"F27:U2"}),
+    ("N19", "K-9-51", "段三：第 5 項之候選之序以 k967_rank 先於距離", _S3,
+     "_cands.append(((_d, k967_rank(_G[_p], k967_pre_area(_p, _cm.get(_p), _pa), _p)), _p, _d,",
+     "_cands.append(((k967_rank(_G[_p], k967_pre_area(_p, _cm.get(_p), _pa), _p), _d), _p, _d,", {"F16:K3"}),
+    ("N20", "K-9-66", "段三：K-9-66 之列⛔ 記", _S3,
+     "for e in _cs}) >= 2 and not (", "for e in _cs}) >= 9 and not (", {"F27:U1"}),
+    ("N21", "K-9-68", "段三：第 5 項之輪之剩下⛔ 減其所併", _S3,
+     "                if F is None:\n                    rem[x] -= g",
+     "                if F is None:\n                    pass",
+     {"F16:K2"}),
+    ("N22", "R-17″", "段三：趟中之帳同一受併宗⛔ 累加（覆寫）", _S3,
+     "                    _lg373[e['r']] = float(_lg373.get(e['r'], 0.0)) + float(v)",
+     "                    _lg373[e['r']] = float(v)", {"F28:L6"}),
+    ("N23", "R-17″", "段三：趟中之帳取輸入之帳 ＋ 最末一次", _S3,
+     "                    _lg373 = dict(_dx.get('段三部分併出') or {})",
+     "                    _lg373 = dict(_by0[x].get('段三部分併出') or {})", {"F28:L1", "F28:L6"}),
+    ("N24", "R-17″", "段三：趟中之帳⛔ 寫", _S3,
+     "                    _dx.update({'段三部分併出': _lg373, '段三併出': sorted(set(_dx.get('段三併出') or ()) | {e['r']})})",
+     "                    pass", {"F28:L1"}),
+    ("N25", "R-19″", "段三：第 5 項之重劃前面積之表取輸入之態", _S3,
+     "               for p, t in state[\"by\"].items()}", "               for p, t in _by0.items()}", {"F28:L6"}),
+    ("N26", "K-9-66", "段三：試施之受併宗之量⛔ 乘 κ", _S3,
+     "            _apply(_tt, e['r'], [(x, e['k'] * float(v), False)])",
+     "            _apply(_tt, e['r'], [(x, float(v), False)])", {"F16:K10"}),
+    ("N27", "K-9-68", "段三：第 1 輪⛔ 記已試而未全收之街廓", _S3,
+     "                elif _has357(e['s'] - g):\n                    F.setdefault(x, set()).add(_b)",
+     "                elif _has357(e['s'] - g):\n                    pass", {"F27:U2"}),
+    ("N28", "R-7 ③", "段三：題一 4 之半之片⛔ 入第 5 項之輪", _S3,
+     "        _rnd373(_rq, _rem, _F)\n        _p5_373([c] + _hv, _rem, _F)",
+     "        _rnd373(_rq, _rem, _F)\n        _p5_373([c], _rem, _F)",
+     {"F16:K17"}),
+    ("N29", "K-9-66", "段三：⛔ 以 k966_block_merge 之回傳之態承接", _S3,
+     "            state, _gs, _steps = k966_block_merge(state, _cs, _try373)",
+     "            _s0, _gs, _steps = k966_block_merge(state, _cs, _try373)", {"F27:U1"}),
+    ("N30", "R-7 ②", "段三步驟 10：第 1 輪之來源量⛔ 除 κ", _S3,
+     "            _rq10.append({'cls': _cls373[_kind(x)], 's': float(_q) / _kq,",
+     "            _rq10.append({'cls': _cls373[_kind(x)], 's': float(_q),", {"F16:K10"}),
+    ("N31", "R-7 ②", "段三步驟 10：非建地之片之剩下⛔ 記", _S3,
+     "                _left[x] = max(0.0, _rem10.get(x, 0.0))", "                pass", {"F27:U1"}),
+    ("N32", "R-7 ②", "段三步驟 10：剩下⛔ 入第 5 項之輪", _S3, "        _p5_373(_xs10, _rem10, _F10)", "        pass",
+     {"F27:U2"}),
+    ("N33", "K-9-66 R-5 (a)", "段三：建地之部分併出⛔ 留 build", _S3,
+     "                if _has357(float(_dx.get('分攤登記面積_m2', 0) or 0) + float(_dx.get('面積_m2', 0) or 0) - float(v)):",
+     "                if False:", {"F16:K7", "F16:K19"}),
+    ("N34", "K-9-68", "手冊先行：一輪之要求⛔ 依受併之街廓分組", _MN,
+     "            if _e953['bk'] not in _bg953:\n",
+     "            _bg953.pop(_e953['bk'], None)\n            if _e953['bk'] not in _bg953:\n",
+     {"F27:T1"}),
+    ("N35", "K-9-51", "手冊先行：候選⛔ 扣已試而未全收之街廓", _MN,
+     "                    if str(_bk) in _F953.get(_x, set()):\n                        continue\n",
+     "                    if False:\n                        continue\n", {"F27:T2"}),
+    ("N36", "K-9-66", "手冊先行：K-9-66 之列⛔ 記", _MN,
+     "for _e953 in _cs953}) >= 2 and not (", "for _e953 in _cs953}) >= 9 and not (", {"F27:T1"}),
+    ("N37", "K-9-68", "手冊先行：K-9-51 之輪之剩下⛔ 減其所併", _MN,
+     "                if not _first:\n                    _rem953[_x] -= _gv",
+     "                if not _first:\n                    pass",
+     {"F27:T1"}),
+    ("N38", "R-17″", "手冊先行：趟中之帳同一受併宗⛔ 累加（覆寫）", _MN,
+     "                    _lg953[_e953['r']] = float(_lg953.get(_e953['r'], 0.0)) + float(_v)",
+     "                    _lg953[_e953['r']] = float(_v)", {"F28:L4"}),
+    ("N39", "R-17″", "手冊先行：趟中之帳取輸入之帳 ＋ 最末一次", _MN,
+     "                    _lg953 = dict(_dx.get('段三部分併出') or {})",
+     "                    _lg953 = dict(_tin953[_x].get('段三部分併出') or {})", {"F28:L4"}),
+    ("N40", "R-17″", "手冊先行：趟中之帳⛔ 寫", _MN,
+     "                    _dx.update({'段三部分併出': _lg953, '段三併出': sorted(set(_dx.get('段三併出') or ()) | {_e953['r']})})",
+     "                    pass", {"F28:L2"}),
+    ("N41", "R-19″", "手冊先行：K-9-51 之重劃前面積之表取輸入之態", _MN,
+     "                       for _pk953, _tq in state[\"by\"].items()}",
+     "                       for _pk953, _tq in _tin953.items()}",
+     {"F28:L4"}),
+    ("N42", "K-9-66 R-5", "手冊先行：第 1 輪之來源量⛔ 除 κ", _MN,
+     "                _rq953.append({'cls': _kind953[_sort953(_tin953[_x])], 's': float(_qv) / _kv,",
+     "                _rq953.append({'cls': _kind953[_sort953(_tin953[_x])], 's': float(_qv),", {"F27:T5"}),
+    ("N43", "R-18″", "手冊先行：趟末之前帳取當下之態", _MN,
+     "            _pp953 = dict((str(_k), float(_v)) for _k, _v in (_tin953[_x].get('段三部分併出') or {}).items())",
+     "            _pp953 = dict((str(_k), float(_v)) for _k, _v in (_d.get('段三部分併出') or {}).items())", {"F27:T1"}),
+    ("N44", "K-9-66", "手冊先行：⛔ 以 k966_block_merge 之回傳之態承接", _MN,
+     "            state, _gs953, _stp953 = k966_block_merge(state, _cs953, _try953k)",
+     "            _s0, _gs953, _stp953 = k966_block_merge(state, _cs953, _try953k)", {"F27:T1"}),
+    ("N45", "K-9-68", "第一趟：一輪之要求⛔ 依受併之街廓分組", _A4,
+     "            if _e['bk'] not in _bg_a4:\n",
+     "            _bg_a4.pop(_e['bk'], None)\n            if _e['bk'] not in _bg_a4:\n",
+     {"F27:V1"}),
+    ("N46", "R-17″", "第一趟：趟中之帳同一受併宗⛔ 累加（覆寫）", _A4,
+     "                    _lg_a4[_e['r']] = float(_lg_a4.get(_e['r'], 0.0)) + float(_v)",
+     "                    _lg_a4[_e['r']] = float(_v)", {"F28:L5"}),
+    ("N47", "R-17″", "第一趟：趟中之帳取輸入之帳 ＋ 最末一次", _A4,
+     "                    _lg_a4 = dict(_dx.get('段三部分併出') or {})",
+     "                    _lg_a4 = dict(_tin_a4[_x].get('段三部分併出') or {})", {"F28:L5"}),
+    ("N48", "R-17″", "第一趟：趟中之帳⛔ 寫", _A4,
+     "                    _dx.update({'段三部分併出': _lg_a4, '段三併出': sorted(set(_dx.get('段三併出') or ()) | {_e['r']})})",
+     "                    pass", {"F28:L3"}),
+    ("N49", "R-19″", "第一趟：各輪之重劃前面積之表取輸入之態", _A4,
+     "- sum(float(_v) for _v in (_t.get('段三部分併出') or {}).values()) for _p, _t in state[\"by\"].items()}",
+     "- sum(float(_v) for _v in (_t.get('段三部分併出') or {}).values()) for _p, _t in _tin_a4.items()}", {"F28:L5"}),
+    ("N50", "K-9-66", "第一趟：K-9-66 之列⛔ 記", _A4,
+     "for _e in _cs_a4}) >= 2 and not _all_ok:", "for _e in _cs_a4}) >= 9 and not _all_ok:", {"F27:V1"}),
+    ("N51", "K-9-68", "第一趟：剩下⛔ 減其所併（記為 0）", _A4, "                    _L[_x] = _e['s'] - _g",
+     "                    _L[_x] = 0.0", {"F27:V1"}),
+    ("N52", "K-9-68", "第一趟：受詞每輪沿名單⛔ 止於首一有其宗之街廓", _A4,
+     "                break\n        _bo_a4, _bg_a4 = [], {}", "\n        _bo_a4, _bg_a4 = [], {}", {"F27:V2"}),
+    ("N53", "K-9-66", "第一趟：同類之片之序（剩下大者先）反之", _A4,
+     "key=lambda _y: (_rank_a4[_cls[_y]], -_L[_y], _y)):", "key=lambda _y: (_rank_a4[_cls[_y]], _L[_y], _y)):",
+     {"F24:K25"}),
+    ("N54", "K-9-67", "第一趟：受併宗之序去 k967_rank", _A4,
+     "            k967_rank(_S['G'][_h], k967_pre_area(_h, _ms, _pre_a4), _h))", "            _h)", {"F24:K7"}),
+    ("N55", "R-18″", "第一趟：趟末之前帳取當下之態", _A4,
+     "            _pp_a4 = dict((str(_k), float(_v)) for _k, _v in (_tin_a4[_x].get('段三部分併出') or {}).items())",
+     "            _pp_a4 = dict((str(_k), float(_v)) for _k, _v in (_d.get('段三部分併出') or {}).items())", {"F27:V1"}),
+    ("N56", "K-9-66", "第一趟：⛔ 以 k966_block_merge 之回傳之態承接", _A4,
+     "            state, _gs_a4, _st_a4 = k966_block_merge(state, _cs_a4, _try_a4k)",
+     "            _s0, _gs_a4, _st_a4 = k966_block_merge(state, _cs_a4, _try_a4k)", {"F27:V1"}),
+    ("N57", "K-9-66 通知 3", "調配之輸入：建地之部分併出之原有面積⛔ 依剩下之比", _AI,
+     "            _row.update(所屬單元=_up, 原有面積=_a(t) * _rho_b, 段三併出面積=_a(t) * (1.0 - _rho_b))",
+     "            _row.update(所屬單元=_up, 原有面積=_a(t), 段三併出面積=0.0)", {"F27:W1", "F27:W2"}),
+]
+
+
+def _fn_spans(src):
+    ls = src.splitlines(keepends=True)
+    out = {}
+    for n in ast.parse(src).body:
+        if isinstance(n, ast.FunctionDef):
+            out[n.name] = (sum(len(x) for x in ls[:n.lineno - 1 - len(n.decorator_list)]),
+                           sum(len(x) for x in ls[:n.end_lineno]))
+    return out
+
+
+def _child(repo, app):
+    """（內部）以 `app` 取受詞，跑 F27／F28／F23／F24／F16 之 selftest 之項，印 {器: 紅項} 之 JSON（末列）。"""
+    sys.path.insert(0, os.path.join(repo, "verify"))
+    from app_harvest import harvest
+    import selection_pipeline as sp
+    with contextlib.redirect_stdout(io.StringIO()):
+        ns, _ = harvest(app)
+    me = sys.modules[__name__]
+    P = "verify/probes/"
+    f12 = _load(repo, P + "probe_WG9353_endmerge.py", "f12_377")
+    f16 = _load(repo, P + "probe_WG9357_k948.py", "f16_377")
+    f23 = _load(repo, P + "probe_WG9363_k953.py", "f23_377")
+    f24 = _load(repo, P + "probe_WG9367_adj4.py", "f24_377")
+    f28 = _load(repo, P + "probe_WG9373p1_partrem.py", "f28_377")
+    out = {}
+    for k, fn in (("F27", lambda: _cases(ns, sp)), ("F28", lambda: f28._cases(ns, f12, f16, me, f23)),
+                  ("F23", lambda: f23._cases(ns, sp)), ("F24", lambda: f24._cases(ns, sp)),
+                  ("F16", lambda: f16._cases(ns, sp))):
+        try:
+            with contextlib.redirect_stdout(io.StringIO()):
+                cs = fn()
+            out[k] = _report(cs, verbose=False)
+        except Exception as ex:  # noqa: BLE001
+            out[k] = ["執行中止", type(ex).__name__]
+    print(json.dumps(out, ensure_ascii=False))
+    return 0
+
+
+def mutate(repo):
+    src = _read(repo, "app.py")
+    spans = _fn_spans(src)
+    tmp = tempfile.mkdtemp(prefix="wg9377mut_")
+    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")
+
+    def one(m):
+        mid, cl, desc, fn, old, new, want = m
+        if mid == "N00":
+            n, text = 1, src
+        else:
+            a, b = spans.get(fn, (0, 0))
+            n = src[a:b].count(old)
+            if n != 1:
+                return m, n, None
+            text = src[:a] + src[a:b].replace(old, new, 1) + src[b:]
+        p = os.path.join(tmp, f"app_{mid}.py")
+        with open(p, "w", encoding="utf-8", newline="\n") as f:
+            f.write(text)
+        try:
+            r = subprocess.run([sys.executable, os.path.abspath(__file__), "_child", repo, p], capture_output=True,
+                               text=True, encoding="utf-8", env=env, timeout=600)
+        except subprocess.TimeoutExpired:
+            return m, n, ("逾時",)
+        try:
+            red = json.loads((r.stdout.strip().splitlines() or ["null"])[-1])
+        except Exception:  # noqa: BLE001
+            red = None
+        if r.returncode != 0 or not isinstance(red, dict):
+            return m, n, ("例外", (r.stderr.strip().splitlines() or ["?"])[-1][:200])
+        return m, n, red
+
+    todo = [("N00", "—", "基準（⛔ 突變）", None, None, None, set())] + MUT377
+    bad = []
+    try:
+        with ThreadPoolExecutor(2) as ex:
+            res = list(ex.map(one, todo))
+    finally:
+        shutil.rmtree(tmp, ignore_errors=True)          # 暫存之 app_*.py（每份約 1.8 MB）⛔ 遺留
+    for m, n, red in res:
+        mid, cl, desc, fn, old, new, want = m
+        got = {f"{k}:{i}" for k, v in red.items() for i in v} if isinstance(red, dict) else None
+        if mid == "N00":
+            ok = got == set()
+        else:
+            ok = n == 1 and got is not None and bool(want) and want <= got
+        if not ok:
+            bad.append(mid)
+        shown = sorted(got) if got is not None else red
+        print(f"  {'✅' if ok else '🔴'} {mid} {cl}·{desc}：錨 {n} 見；所指 {sorted(want)}；紅 {shown}")
+    print(f"⇒ 突變 {len(MUT377)}（另基準一）；紅 {bad}；rc {1 if bad else 0}")
+    return 1 if bad else 0
+
+
 # ── run：本案 ──
 R2_EXPECT = {3.5: [("R3", ["628-28(1)", "628-29(1)"], "628-28(1)", 69.2, 114.0), ("R6", ["628-21(1)", "628-22(1)",
                                                                                          "628-23(1)"], "628-21(1)", None, None)],
@@ -766,6 +1078,10 @@ def main(argv):
         print(__doc__)
         return 2
     cmd, repo = argv[1], os.path.abspath(argv[2])
+    if cmd == "mutate":                                       # 🆕 `W-G.9-377`
+        return mutate(repo)
+    if cmd == "_child" and len(argv) == 4:                    # 🆕 `W-G.9-377`（mutate 之子程序·內部）
+        return _child(repo, os.path.abspath(argv[3]))
     if cmd == "selftest":
         return selftest(repo)
     if cmd == "wiring":
````

## 附錄乙　塊 `Fv28`（`git apply` 之差異·`verify/probes/probe_WG9373p1_partrem.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9373p1_partrem.py b/verify/probes/probe_WG9373p1_partrem.py
index 1daec0c..cafa6ec 100644
--- a/verify/probes/probe_WG9373p1_partrem.py
+++ b/verify/probes/probe_WG9373p1_partrem.py
@@ -29,6 +29,11 @@
            期值出自 KL 之裁（甲案）、`K-9-49`、`K-9-66` 通知 `3` 與補令一 `§二`（發單側手算·⛔ 呼叫受測碼求期）；
            等面積之對照（⛔ 帶前帳而面積同其剩下·其配地之結果須同）：E1／E2、E3／E4、E6／E7、S3／S5、S4／S6、M1／M2、Q1／Q2；
            S2 ＝ ⛔ 帶前帳之同片（非等面積）、I2 ＝ ⛔ 其後受併入之同片（非等面積）。
+           🔧 `W-G.9-377`（`W-G.9-373` 補令二 `§三` 之⛔ 量之二項·⛔ 上列一字不刪）：增 L4〜L6（三處各一）——受詞之片帶前帳
+           （向本趟亦併入之受併宗）且同一趟之內部分併出二次（L4／L5）或於其後之輪仍見（L6）：⑦ 趟中之帳之**累加**（其後之試算所見之
+           「面積_m2 ＋ 段三部分併出之和」恆 ＝ 0·⛔ 以「最末一次」或「輸入之帳 ＋ 最末一次」代之）；⑧ `R-19″` 之重劃前面積之表之
+           **取態**（受測碼呼叫 `k967_pre_area` 時所傳之表，其受詞之片之值 ＝ 分攤登記面積 − 當下之帳之和·⛔ 取輸入之態）——以
+           包一層之 `k967_pre_area`（`ns` 即受測碼之 globals）記每次所傳之表之受詞之值。期值手算（各例之註）。
 rc：0 相符／1 不符／2 用法錯。
 """
 import contextlib, copy, importlib.util, io, os, sys
@@ -256,6 +261,88 @@ def _l3(ns, f27):
     return sorted(set(seen)), len(seen) > 0
 
 
+# 🆕 `W-G.9-377`：趟中之帳之累加（⑦）與 `R-19″` 之表之取態（⑧）
+def _pre_spy(ns, ids, rec):
+    """回 (原函式, 包一層者)：每次呼叫記其所傳之表中 `ids` 之值（依暫編地號排序之 tuple）。"""
+    orig = ns["k967_pre_area"]
+
+    def wrapped(pid, members, area_of):
+        rec.append(tuple((x, round(float(area_of[x]), 4) + 0.0) for x in sorted(ids) if x in area_of))
+        return orig(pid, members, area_of)
+    return orig, wrapped
+
+
+def _with_spy(ns, ids, fn):
+    seen, rec = [], []
+    orig, w = _pre_spy(ns, ids, rec)
+    ns["k967_pre_area"] = w
+    try:
+        fn(seen)
+    finally:
+        ns["k967_pre_area"] = orig
+    return sorted(set(seen)), sorted(set(rec)), len(seen) > 0
+
+
+def _l4(ns, f27):
+    """手冊先行（F27 T1 之形）：X(1)（甲·分攤 60）帶前帳（A1(1) 5·面積_m2 −5）。第 1 輪 BB（容 130）三片按比例 130 ÷ 145
+    （X 55／Y 50／Z 40）⇒ X 再併入 A1(1) 49.3103；剩下 5.6897 於 K-9-51 之輪至 BD 之 A2(1)（容 5）⇒ 部分 5。
+    ⑦ 第 2 輪之試算所見之 X(1)：面積_m2 −59.3103 −v ＋ 帳 {A1(1) 54.3103, A2(1) v} ＝ 0；⑧ 計畫之表（輸入之態）X 55／Y 50／Z 40；
+    K-9-51 之表（第 1 輪之後）X 60 − 5 − 49.3103 ＝ 5.6897、Y 50 × 15 ÷ 145 ＝ 5.1724、Z 40 × 15 ÷ 145 ＝ 4.1379。"""
+    tp, R, H = f27._tp, f27._R, f27.H
+    x = tp("X(1)", "BA", H, R(0, 10, 0, 30), 60)
+    x.update({"面積_m2": -5.0, "段三併出": ["A1(1)"], "段三部分併出": {"A1(1)": 5.0}})
+    t = [x, tp("Y(1)", "BA", H, R(10, 20, 0, 30), 50), tp("Z(1)", "BA", H, R(20, 30, 0, 30), 40),
+         tp("A1(1)", "BB", H, R(0, 10, 30, 60), 300), tp("B1(1)", "BB", H, R(10, 20, 30, 60), 300),
+         tp("C1(1)", "BB", H, R(20, 30, 30, 60), 300), tp("A2(1)", "BD", H, R(40, 50, 0, 30), 300)]
+    own = {"X": "甲", "A1": "甲", "A2": "甲", "Y": "乙", "B1": "乙", "Z": "丙", "C1": "丙"}
+    blocks = {b: {"category": H} for b in ("BA", "BB", "BD")}
+    ap, st = f27._cbs({"BB": 130.0, "BD": 5.0}, drop=("X(1)", "Y(1)", "Z(1)"))
+    ids = {"X(1)", "Y(1)", "Z(1)"}
+    return _with_spy(ns, ids, lambda seen: ns["k953_manual_run"](t, list(t), own, blocks, {}, ap, _rec(st, ids, seen),
+                                                                log_print=lambda *a: None))
+
+
+def _l5(ns, f27):
+    """第一趟（F27 V1 之形）：X1(1)（g1·分攤 60）帶前帳（X1(2) 5·面積_m2 −5）；名單 BB → BC。第 1 輪至 BB 之 X1(2)（容 30）
+    ⇒ 部分 30；第 2 輪至 BC 之 X1(3)（容 10）⇒ 部分 10；剩下 15 留於合併單位。⑦ 第 2 輪之試算所見之 X1(1)：
+    面積_m2 −35 −v ＋ 帳 {X1(2) 35, X1(3) v} ＝ 0；⑧ 各輪之表：第 1 輪 60 − 5 ＝ 55、第 2 輪 60 − 5 − 30 ＝ 25。"""
+    tp, R, H = f27._tp, f27._R, f27.H
+    x = tp("X1(1)", "BA", H, R(0, 10, 0, 30), 60.0)
+    x.update({"面積_m2": -5.0, "段三併出": ["X1(2)"], "段三部分併出": {"X1(2)": 5.0}})
+    t = [x, tp("X1(2)", "BB", H, R(0, 10, 30, 60), 300), tp("X1(3)", "BC", H, R(20, 30, 0, 30), 300)]
+    own = {"X1": "g1"}
+    geom = {q["暫編地號"]: [list(c) for c in q["polygon_coords"]] for q in t}
+    ap, st = f27._cbs({"BB": 30.0, "BC": 10.0}, drop=("X1(1)",))
+    subj = [{"歸戶": "g1", "軌": "建地軌", "錨點": "X1(1)", "名單": ["BB", "BC"], "片": ["X1(1)"], "原有面積合計": 60.0}]
+    return _with_spy(ns, {"X1(1)"}, lambda seen: ns["adj4_pass1_run"](t, list(t), own, subj, geom, ap,
+                                                                      _rec(st, {"X1(1)"}, seen),
+                                                                      log_print=lambda *a: None))
+
+
+def _l6(ns, f16):
+    """段三（F28 L1 之形）：Y1(1)（分攤 90）帶前帳（X1(1) 5·面積_m2 −5）；題一 4 再部分併入 X1(1) 20，剩下於第 5 項之輪至
+    Z1(1)（部分 50）。⑦ 其後之試算所見之 Y1(1)：面積_m2 ＋ 帳之和 ＝ 0（帳 {X1(1) 25, Z1(1) …}）；⑧ 第 5 項之表（題一 4 之後）
+    Y1(1) ＝ 90 − 5 − 20 ＝ 65。"""
+    temp, own, blocks, cl = f16._world4()
+    for q in temp:
+        if q["暫編地號"] == "Y1(1)":
+            q.update({"面積_m2": -5.0, "段三併出": ["X1(1)"], "段三部分併出": {"X1(1)": 5.0}})
+    build = [q for q in temp if q["街廓分類"] == f16.H]
+    ap, _tw, st = f16._cbs({"BX": 60.0, "BY": 1000.0, "B7": 50.0}, None, ("Y1(1)",))
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
+                                                                      log_print=lambda *a: None, contests=ct))
+
+
 def _cases(ns, f12, f16, f27, f23):
     out = []
     # E（門檻 150）：C1(1)（a 100）以 ① 同街廓併 C1(2)；C1(2) 部分併出之剩下 50（分攤 60·已併出 10）≡ 一分未併而 a 50
@@ -362,6 +449,16 @@ def _cases(ns, f12, f16, f27, f23):
          lambda: _l2(ns, f27), ([0.0], True))
     _run(out, "L3 趟中之帳·第一趟（F27 V1 之形）：X1(1)／Y1(1) 於 BB 按比例部分併出之試施，其試算所見者皆帶其帳",
          lambda: _l3(ns, f27), ([0.0], True))
+    # 🆕 `W-G.9-377`
+    _run(out, "L4 趟中之帳之累加與 K-9-51 之表之取態·手冊先行：X(1) 帶前帳、同一趟部分併出二次 ⇒ 所見恆 0；"
+              "表 ＝ 計畫時 55／50／40、K-9-51 時 5.6897／5.1724／4.1379",
+         lambda: _l4(ns, f27),
+         ([0.0], [(("X(1)", 5.6897), ("Y(1)", 5.1724), ("Z(1)", 4.1379)),
+                  (("X(1)", 55.0), ("Y(1)", 50.0), ("Z(1)", 40.0))], True))
+    _run(out, "L5 趟中之帳之累加與各輪之表之取態·第一趟：X1(1) 帶前帳、二輪各部分併出 ⇒ 所見恆 0；表 ＝ 第 1 輪 55、第 2 輪 25",
+         lambda: _l5(ns, f27), ([0.0], [(("X1(1)", 25.0),), (("X1(1)", 55.0),)], True))
+    _run(out, "L6 趟中之帳之累加與第 5 項之表之取態·段三：Y1(1) 帶前帳、題一 4 再併入同一受併宗 ⇒ 所見恆 0；表 ＝ 65",
+         lambda: _l6(ns, f16), ([0.0], [(("Y1(1)", 65.0),)], True))
     return out
 
 
````

## 附錄丙　塊 `Fv29`（`git apply` 之差異·`verify/probes/probe_WG9375_k965.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9375_k965.py b/verify/probes/probe_WG9375_k965.py
index 1ea99b7..684fd57 100644
--- a/verify/probes/probe_WG9375_k965.py
+++ b/verify/probes/probe_WG9375_k965.py
@@ -13,6 +13,8 @@
            `K-9-64`、`K-9-66`、`K-9-67`、`K-9-69` 與 `K-6` 典之 `W-G.9-375` 之讀法一〜十三；K43 之期與 K44〜K49 ＝
            `W-G.9-375` 補令一〔回原狀後之併入逐宗·回原狀之帳跨回溯而存；調配之輸入之段三之受併宗〕）；P0 ＝ 判式自驗（逐項
            擾動其期須恰該項紅）。
+           🔧 `W-G.9-377`（`自誤 603`·⛔ 上列一字不刪）：增 K50（回原狀之帳之序以該次合併時之應分配面積定：非相連之二候選，
+           其後應分配面積之大小已易者⛔ 於判時重排）——期值手算（發單側窗七十九·倉外之玩具 `T2`）；P0 隨之 `50` 項。
   wiring   <repo>
            接線（AST·字樣）：Y1 `k929_6_fixpoint` 之簽名；Y2 harness 之注入（`run_step_g`）；Y3 畫面之注入
            （`_k929_6_screen_gate`）；Y4 harness 之 session 鍵（`build_build_parcels`）；Y5 `k929_6_fixpoint` 內之呼叫
@@ -603,6 +605,19 @@ def cases(ns):
                "drops": [],
                "steps": [("第1步", "r1", "u1", "回原狀（K-9-58 ③）"), (S1R, "r1", "r1", "續併"), ("第3步", "r1", "r1", "留置"),
                          (S1R, "r2", "r2", "留置")]}))
+    # 🆕 `W-G.9-377`（`自誤 603`）K50 回原狀之帳之序以該次合併時之應分配面積定（⛔ 於判時重排）：r1 280｜u1 60｜u2 60｜u3 60｜r2 300
+    #     試算一：r1 168−9＝159、u1／u2／u3 36 ✗、r2 180（p=1）；分量 {r1,u1,u2,u3,r2}·標的 r2·佔位 r1（x0 0）⇒ 回原狀
+    #     帳：u1 → [r1（相連）, r2]；u2 → [r2（G 180）, r1（159）]（皆⛔ 相連）；u3 → [r2（相連）, r1]
+    #     u1→r1：a 340 ⇒ 204−9＝195（＞ r2 之 180：若於判時重排，u2 改向 r1）；u2→r2（帳之首）：a 360 ⇒ 216；u3→r2：a 420 ⇒ 252
+    b = [mk("r1", "a1", "A", 280, 0, 10), mk("u1", "a2", "A", 60, 10, 20), mk("u2", "a3", "A", 60, 20, 30),
+         mk("u3", "a4", "A", 60, 30, 40), mk("r2", "a5", "A", 300, 40, 50)]
+    C.append(("K50 回原狀之帳之序以該次合併時之應分配面積定",
+              _fxs(ns, b, {"a1": "GA", "a2": "GA", "a3": "GA", "a4": "GA", "a5": "GA"}, {"A": BLK()},
+                   fail_first=[(["r1", "r2", "u1", "u2", "u3"], 0.0)]),
+              {"alloc": {"r1": 195.0, "r2": 252.0}, "units": {"r1": ["r1", "u1"], "r2": ["r2", "u2", "u3"]},
+               "drops": [],
+               "steps": [("第1步", "r2", "r1", "回原狀（K-9-58 ③）"), (S1R, "r1", "r1", "留置"), (S1R, "r2", "r2", "續併"),
+                         (S1R, "r2", "r2", "留置")]}))
     return C
 
 
````

## 附錄丁　塊 `E20`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末·工項二）

````markdown

---

**取號**（`W-G.9-377 §零-1`）：本批取 `604`（`1` 號）——發單側窗八十之復驗所察（`W-G.9-376R` ⑨ 之自解之一點）。

### 🩸 `自誤 604`　**單令 `commit` 訊息「逐字」而⛔ 及倉之慣例之尾列（`Co-Authored-By`）——受單側每單須以自解處之（`docs/reports/` 中 `18` 檔）**

**形**：`W-G.9-376` 中量單 `§三` 工項零〜二逐字「`commit` 訊息逐字 `…`」（`docs/orders/` 中含此令之單 `48` 檔·最早 `W-G.9-341`）；倉之慣例：主線 `wip/s1-endpart`（`a3925f1`）之 `commit` 中訊息以 `W-G.9-` 起首者 `1107` 筆，其訊息含 `Co-Authored-By:` 之尾列者 `1096` 筆（`git log --format=%H --grep='^W-G.9-' a3925f1`；另加 `--grep='^Co-Authored-By:' --all-match`）；其最近 `150` 筆中 `146` 筆為「首列 ＋ 空列 ＋ 唯尾列」之形（逐筆以 `git log -1 --format=%B` 判）。
**後果之界**：零土地後果；受單側每單須自擇「唯首列」或「首列 ＋ 尾列」並於報告之自解載之——`docs/reports/` 中提及該尾列之報告 `18` 檔（`git grep -l -i 'co-authored' a3925f1 -- docs/reports`·`W-G.9-345R`〜`W-G.9-376R`），同一歧義反覆耗費受單側之自解與發單側之判。
**根因**：單之「逐字」以首列為受詞立言，⛔ 對受單側之環境（其 `commit` 恆附尾列）與倉之既例核其全形。
**後果之框**：🟢 受單側每次皆以「首列逐字 ＋ 尾列」處之、⛔ 停機；發單側窗八十於 `W-G.9-376` 之復驗判之（照受單側之做法·⛔ 改歷史）。
**攔法**：自 `W-G.9-377` 起，單之 `commit` 訊息之令書為「首列逐字 `…`；其後空一列，附受單側之環境所附之尾列（近例之形）；⛔ 他列」。通則：令「逐字」者，明書其受詞之範圍（首列／全文），並對受單側之環境之既定行為核之。
````

## 附錄戊　塊 `P30`（附於 `CLAUDE.md` 之末·工項二）

````markdown

---

## 🔧 待落地清單之更新：以程式字樣為錨之接線與突變之判別力之補寫 ＋ `W-G.9-373` 補令二 `§三` 之⛔ 量之二項 ＋ 量測器 `F29` 之增例（`W-G.9-377`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart`（`W-G.9-377` 工項二之後）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 前節序 `6`：以程式字樣為錨之接線與突變之判別力之補寫（`F17` 之 `W2`／`W3`／`W12`、`F25` 之 `M01`〜`M19`／`M28`／`M29`／`M31` 之代） | `F27`（`verify/probes/probe_WG9373_k966.py`）之 `mutate`（`N01`〜`N57`·錨 ＝ 受測碼之字樣·所指之項 ＝ `F27`／`F28`／`F23`／`F24`／`F16` 之 `selftest` 之項）、`wiring` 之 `Y7`、`selftest` 之 `T5`（手冊先行之第 `1` 輪之來源量 ÷ κ） | ✅（主線） | `docs/orders/W-G.9-377_中量單.md` |
| `2` | 前節序 `6`：`W-G.9-373` 補令二 `§三` 之⛔ 量之二項（`R-19″` 之三表之取態；手冊先行與第一趟之同一趟之內同一片二次以上部分併出之帳之累加） | `F28`（`verify/probes/probe_WG9373p1_partrem.py`）之 `L4`〜`L6`（三處各一·以包一層之 `k967_pre_area` 記所傳之表）；`F27 mutate` 之 `N22`〜`N25`、`N38`〜`N41`、`N46`〜`N49` | ✅（主線） | 同序 `1` |
| `3` | 前節序 `6`：量測器 `F29` 之增例（`自誤 603`） | `F29` 之 `K50`（回原狀之帳之序以該次合併時之應分配面積定） | ✅（主線） | 同序 `1` |
| `4` | 前節序 `7`：`W-G.9-373R` 之 NOTE `1`（`adj4_pass1_run` 之 `_rkey_a4` 之上之註之「成員之輸入之分攤登記面積」·`R-19″` 後已舊） | 零行為；其註在生產碼之檔，且與序 `5` 所改之重劃前面積之表同段 ⇒ 改於 `GB-204` 之落地之單（KL 已獲通知·`2026-10-11`） | ⬜ | `GB-204` 之落地之單 |
| `5` | `GB-204`（入池閘之帳⛔ 達下游之重劃前面積之表與調配之輸入） | 前節序 `8` | ⬜ | 另單（生產碼） |
| `6` | `W-G.9-375` 之【工】巳之三停機 | 前節序 `9`：逐一附圖呈 KL 其處置 | ⬜ | 另單 |
| `7` | `K-9-58` ④、`K-9-59`〜`K-9-63` | 前節序 `10` | ⬜ | `K-9-58` ④〜`K-9-63` 之落地之單（其序另呈 KL） |
| `8` | 單之 `commit` 訊息之令之書法（`自誤 604`） | 首列逐字；其後空一列附受單側之環境所附之尾列；⛔ 他列 | ✅（自 `W-G.9-377` 起） | 自誤簿 |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：`K-9-65`（……）入主線；`GB-204` 之立（`W-G.9-376`）」節之序 `6` ⇒ 本表序 `1`〜`3`（✅）；其序 `7` ⇒ 本表序 `4`（⬜·改於 `GB-204` 之單）；其序 `8`、`9`、`10` ⇒ 本表序 `5`、`6`、`7`（態⛔ 變）；其餘之序之態⛔ 變。「`W-G.9-374`」之節之序 `10`（NOTE `2` 之族·另案）、序 `11`（畫面之二既有之警告·併畫面批）之態⛔ 變。
🔒 **⛔ 列之突變**（明書之）：手冊先行之 `K-9-51` 之候選之序「距離 → 本街廓者先」之對調——其距離取片至街廓之形（該街廓之片之聯集）之距離，本街廓者恆為 `0` ⇒ 對調為等價之突變（行為⛔ 異）。
🔒 **本案之量**：本批⛔ 動生產碼 ⇒ 配地⛔ 變。
🔒 **依賴序**：序 `5`（`GB-204`·含序 `4`）→ 序 `6`（三停機之處置·逐一附圖呈 KL）→ 序 `7`（其序另呈 KL）→ 規格步 `5` → `6` → `7`／`8`；`GB-196`、`GB-197`、`GB-198`、`GB-202` 另單（⛔ 急）。
🔒 **本機介面**：同前節（⛔ 變）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `9`（子字串框·含圖例與本列）·列 ＝ `7`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: 388516fa69a199c27e85c59fff3fccae0d6774c189adce36024e23bb76ff1374
