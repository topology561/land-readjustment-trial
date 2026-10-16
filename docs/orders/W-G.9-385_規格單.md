# `W-G.9-385`　規格單：`K-9-74` 之落地（臨街地特別負擔之路寬：各可建築街廓之正面、左側、右側依其臨接之道路 `BLOCK`——勾新闢者全寬；未勾者以道路 `BLOCK` 扣除抵充地〔公有持分〕與 `JUNCTION` 框後之比例；中心線即區界者以垂距；一面臨二段以上者依臨接長度加權〔`K-9-79` ①〕；勾新闢而區內無其道路 `BLOCK` 者 `0` 並警示〔`K-9-79` ②〕）＋ `K-9-62` 之「第33條排除」「抵充地」二欄（讀取與檢核）＋ `W-G.9-384` 之入主線、`K-9-79` 之立（入典）＋ 自誤 `621` ＋ `W-G.9-384` 之唯讀審查之 (丙) 二之例（`F23` `K75`）＋ 待落地清單之更新（新側支 `verify/W-G.9-385-k974`）

> **本單建議等級 ＝ `high`**（生產碼 `1` 檔：`app.py` 之頂層之新名五〔`K974_PARAMS`、`k962_land_marks`、`k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`〕與二函式之增列〔`calc_special_burden_total`、`main`〕·`§三-2`；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單側窗八十七·`2026-10-16`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-385-k974`**，其起點 ＝ 主線之端 `158f7fe`）。
> **流程 ＝ 規格單**（常態·附則甲〜丙施行）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `Fy35`·CC ⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `1` 檔；**本案之配地⛔ 變**〔`§一` 項 `5`：本案之各面之尺度 ＝ 快照之負擔尺度之輸入；harness ⛔ 動〕——其效由量測器 `F30` 之合成之例與本案資料之複本之模擬量之〔KL `2026-10-16 12:25` 第 `4` 點〕）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`（`W-G.9-384` 補令一 工項一）；遠端 heads `44`（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-385-k974`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `Fy35`／`K25`／`E28`／`P38` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`自誤 479`）；Bash 之輸出路徑一律單引號之絕對路徑（`W-G.9-373` 補令二單首）。Bash 命令⛔ 含 heredoc（常設規則索引）。`<O>` ＝ CC 自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列（近例之形·`Co-Authored-By` 等）；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-385_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者照實載於報告。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限**（🆕 本單起·KL `2026-10-16` 之效率之令·`W-G.9-384` 之 `≤ 2` 改之）：各驗之命令得並行，其同時並行數 ≤ **`6`**（`parity`、`k6s3 run`、`F23 run`、`F24 run`、`F27 run`、`F29 run`、`F16 run`、`F14 run`、`F10 run`、`F8 run`、`F9 run`、`F21 run`、`F26 run`、`F30 run`、`failclosed`、`F19 mut`、`F22 mut`、`F27 mutate`、`F25 mutate` 亦同此限）；逾時或 `rc` ≠ 期者，於⛔ 他負載之下**重跑一次**，二趟之出艙皆照實入報告（重跑之趟 ＝ 期 ⇒ 該呼叫以重跑之趟為準·報告具名之）。
> 🔑 **撰碼中之自跑**：CC 撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之頂層節點除 `§三-2` 所列者外之一字（**頂層之新名唯 `K974_PARAMS`、`k962_land_marks`、`k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`**）；`calc_special_burden_total` 與 `main` 之既有之列之刪改（唯 `§三-1` `R-7` 所列之三列得易之）；生產碼 `34` 檔之其餘 `33` 檔（含 `verify/selection_pipeline.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py`）；`parse_cad_precision_layers`、`calc_frontage_burden_scale`、`calc_side_burden_scale`、`_line_block_overlap`、`r3_front_road_derive` 之一字；`§三-3` 之禁改；既有量測器除塊 `Fy35` 所改之 `3` 檔外之一字；`data/` 之一切檔（含 `data/地籍資料來源_匿名版.xlsx`·本案⛔ 加二欄·`§二`）、`verify/case_params_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、`GB` 簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`K-6` 典、自誤簿、`CLAUDE.md` 除塊 `K25`／`E28`／`P38` 之純末端追加外之一字；任何他側支之推送、刪除或改寫；KL 主 checkout；`K-9-62` 之指配（非共同負擔公共設施用地·`第33條排除` 之欄唯讀取與檢核）、`K-9-78`、`GB-205`、`K-9-59`〜`K-9-61`、`K-9-63`、規格步 `5`〜`8`、`GB-196`〜`198`／`202`。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`；`git ls-remote --heads origin` 之列數 ＝ `44`（全 `44` 列存 `<O>\heads_before.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-385-k974`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 620 619` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `605`／`MAX` `620`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `75`／`78`／`[44, 47]`（發單側窗八十七於 `158f7fe` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。

### `§零-1`　取號現查（宣告框）

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `158f7fe` 之追蹤檔 **`2866`** 檔·列框；發單側窗八十七以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``〕於 `158f7fe` 實算）：

| 號 | 裸（錨定）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 621` | `68` | `0` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——`sha256`／blob／`commit` 之子字串、行號、量測之值、閘 `6` 之判別力之 `621 620` 等） |
| `K-9-79` | `0` | — | — | — | 🟢 可取 |
| 對照甲［必非零］`K-9-78` | `23`（`5` 檔） | — | — | — | 🟢 框非恆空 |

**塊名、新名**（母體同上·檔框／列框·`git grep -l`／`git grep -c` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fy35`、`E28`、`P38`（逐名） | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| `K25` | `0`／`0` | `3`／`4` | 🟢 可取（諸列皆量測器之項名〔`F29`／`F16` 之 `K25` 等〕·⛔ 塊名） |
| 對照甲［必非零］`Fy34` | `2`／`14` | `3`／`17` | 🟢 框非恆空 |
| 對照甲［必非零］`K24` | `1`／`9` | `5`／`20` | 🟢 框非恆空 |
| 對照甲［必非零］`E27` | `1`／`4` | `2`／`9` | 🟢 框非恆空 |
| 對照甲［必非零］`P37` | `1`／`5` | `2`／`10` | 🟢 框非恆空 |
| 報告名 `W-G.9-385R`、新側支之名 `W-G.9-385-k974`、本單名 `W-G.9-385_規格單`、新器 `probe_WG9385_k974`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |

自誤 `MAX` ＝ `620`、`K-9` `MAX` ＝ `78`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 621`（塊 `E28`）、`K-9-79`（塊 `K25`）；量測器之新檔名 `F30`（`verify/probes/probe_WG9385_k974.py`）；⛔ 鑄 `GB`、`VR`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `158f7fe`，或遠端 heads ≠ `44`、或已含 `refs/heads/verify/W-G.9-385-k974`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy35`／`K25`／`E28`／`P38` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy35` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-385-k974`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
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
| `1` | 主線／refs | 主線 `158f7fe959697571d8179988cd4c192c0016ead9`（`W-G.9-384` 補令一 工項一·其父 `663a457`）；遠端 heads **`44`**（`git ls-remote --heads origin` 之列數）；追蹤檔 `2866`（`git ls-tree -r <主線> \| wc -l`）；`app.py` ＝ `261c5ac99f2b3b6e19152a689156378242d4c3a7`（`1818878` B）、`verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`（`60273` B）、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`（`121758` B）、`verify/run_verification.py` ＝ `f5b896e5a702c5d958e3ba27091d27832385efc4`（`103754` B）、`verify/run_all.py` ＝ `e5cf9a224517533b183b34e4fd0f5fbe35ee406b`（`24681` B）、`data/地籍資料來源_匿名版.xlsx` ＝ `875d75c8c395a7612477cc952abc8c98a0a7cfed`（`11482185` B·本批⛔ 動）；本批所改之 `3` 器之施前 blob ＝ `§五-1` 項 `2`；`K-6` 典 ＝ `78a4892a810b81d516ea176f3dfb85b38de47775`（`801055` B）、自誤簿 ＝ `3f06cffaccc5db2a1be036bd2815941c91e920ed`（`1196778` B）、`CLAUDE.md` ＝ `d1b1a1f2a6ee56fcdb7c9f65fd288be38b73e86c`（`408690` B）；皆以換行結尾·CR `0`（判別力：`data/V6.dxf` ＝ `12308`） |
| `2` | 受詞（`158f7fe`） | ① `calc_special_burden_total`：各面之尺度 ＝ 勾新闢 ⇒ `calc_frontage_burden_scale(路寬)`（側面 ⇒ `calc_side_burden_scale`）、未勾 ⇒ `0`——⛔ 讀道路 `BLOCK`、抵充地、中心線。② `main` 之步驟 H：`road_data` 唯取 `SS_ROAD` 之路寬、長度、新闢 ⇒ `calc_special_burden_total(road_data, C_for_calc)` ⇒ `f3_sb_rows`（G 值迭代之 `l₁`／`l₂` 之源·`_build_wf_ctx`）；步驟 E 之 `st.caption` 載「僅新闢道路計入臨街地特別負擔。」。③ `JUNCTION` 圖層⛔ 讀（`parse_cad_precision_layers` 之圖層之集 ＝ `BASELINE`、`CENTERLINE`、`FRONT_LINE`、`SIDE_LINE`、`ALLOC_LINE`）。④ 「重劃區地籍」工作表之二欄⛔ 讀；其表之欄（`data/地籍資料來源_匿名版.xlsx`）＝ `鄉鎮市`、`地段`、`地號`、`統編`、`所有權人`、`管理機關`……（D、E 欄 ＝「統編」「所有權人」·皆空）。⑤ harness（`verify/stepg_pipeline.py` 之 `114`〜`145` 列）之尺度 ＝ 快照之 `負擔尺度_輸入`、新闢 ＝ 其 ＞ `0`，並斷言 `calc_special_burden_total` 之尺度 ＝ 之（KL 四條件 ①）。`git grep -c -F` 於 `app.py`（列框）：「def k974_burden_scales」`0`、「JUNCTION」`0`、「僅新闢道路計入臨街地特別負擔」`1`、「sb = calc_special_burden_total(road_data, C_for_calc)」`1`、「f3_cad_junctions」`0` |
| `3` | 工項一之端（`158f7fe` ＋ 塊 `Fy35`·倉外實跑） | `V-1`〜`V-2` 之 `55` 呼叫中，其受詞（器或其所載之器）於塊 `Fy35` 有改者 `13` 呼叫（`F30`〔`selftest`／`wiring`／`run`〕、`F23`〔`selftest`／`wiring`／`run`〕、`F24`〔`selftest`／`wiring`／`run`〕、`F25`〔`wiring`／`mutate`〕、`F27 mutate`、`F28 selftest`〔後二者載 `F23` 之例〕；`F23 wiring`／`F24 wiring` 之 `W8`／`W7` 亦掃新器之字面）於工項一之端實跑：`3` 呼叫 ＝ `§四-1` 工項二前置 `1`（`F30` 之三·其末列逐字見該處）；其餘 `10` 呼叫皆 `rc 0`·末列 ＝ 開工態之同器之末列（`F23 selftest` `P0 75／75`·`K75` 綠）；此 `13` 呼叫之 `stderr` 合計 `0` B。其餘 `42` 呼叫之器與其受詞與開工態 `158f7fe` 逐位同——⛔ 於本窗重跑；其出艙 ＝ 開工態之出艙（發單側窗八十七於 `663a457`〔其 `app.py` 與 `verify/` 之一切檔 ≡ 主線 `158f7fe`〕自倉復驗：`52` 呼叫皆 `rc 0`）——CC 之前置 `2` 實跑之。🔒 撰器中之一形：`F30 run` 之初稿於新名缺時拋 `KeyError` ⇒ `rc 3`（無從判定）·`stderr` `428` B ⇒ 改為先查新名、缺則 `R0` 紅（`rc 1`） |
| `4` | 原型（發單側窗八十七·倉外·`158f7fe` ＋ 塊 `Fy35` ＋ `§三` 之一實作·⛔ 為 CC 之期） | 原型之 `app.py` ＝ `dc5b832b7ad1e648e22b806b2d6b0557ff64d3a5`（`1838088` B·對開工態 `+345`／`-3`）——⛔ 為期；頂層節點之相異（AST）＝ `{K974_PARAMS, k962_land_marks, k974_read_junctions, k974_burden_scales, k974_screen_scales, calc_special_burden_total, main}`，頂層之新名 ＝ 其前五；`R-9` 之字樣皆合（`V-8` 之期）。`V-1`〜`V-2` 之 `55` 呼叫（同 `§四-1` 之命令）於原型皆 `rc 0`，其末列 ＝ `§五-1` 項 `8` 之施後之列；諸器之 `stderr` 合計 `0` B。`F30 selftest` 之 `K1`〜`K16` 之期值皆發單側手算（各例之註）、原型實得與之逐值同。🔒 撰原型中 `F23 wiring` 之 `W8`／`F24 wiring` 之 `W7` 紅一次（巢狀之 `_perp` 與既有之同名者撞·`§三-3` 之 `2`）⇒ 改名避之；`F30 run` 之 `R1` 於原型之初稿紅（`R1` 右側之首段之偏移點距 `RD2` `0.005 m`·臨接比 `0.9975`）⇒ 增 `snap_m`（`§三-1` `R-4` ①）；`R3` 之容差由 `1e-6` 改為 `1e-4`（外部錨之「幾何面積_m2」捨入至 `0.01 ㎡`·器內之註）；🔒 定稿前另一審查者（唯讀·發單側窗八十七·⛔ 參與撰寫）以「受單側唯依 `§三` 撰碼能否過 `F30`」審之，所揭之五缺——`R-7` 三列之「須」易（`W7`）、`R-5` 之 `hexdigest()`（`R6`）、`R-7` ② 之警示與停機之置處（`road_data = []` 之前·`W5`）、`W5` 之實跑之名之限與 `_k974` 之列⛔ 附行末之註、`R-4` ⑤ 之 `detail` 之列數（`K7`）——與十一款之補（`df_uland` 為 `None`、`errors='coerce'`、勾新闢⛔ 求 `A`、法向之先取、線長 `0`、缺表之存、`notna()`、道路 BLOCK 之 `vertices`、警示之「0.5」⛔ 格式化、一面之尺度之逐道路一加等）皆已補入 `§三`（原型與之合·⛔ 改器） |
| `5` | 本案之量（主線之端與原型·二退縮） | **主線之端與原型**（harness 之圖資與地籍·`F30 run`）：`k974_screen_scales` 之各面之尺度 ＝ 快照之 `負擔尺度_輸入`——`R1` 正面 `0.0`／左側 `1.0`／右側 `1.0`；`R2` `2.0`／`1.0`／（無右側線）；`R3` `2.0`／（無左側線）／`1.0`；`R4` `0.0`／`1.0`／`1.0`；`R5` `2.0`／`1.0`／（無）；`R6` `2.0`／（無）／`1.0`；警示 `0`、錯誤 `0`；臨接之道路 ＝ `R1` 左 `RD1`、右 `RD2`；`R2` 正 `RD1`、左 `RD4`；`R3` 正 `RD2`、右 `RD4`；`R4` 左 `RD2`、右 `RD3`；`R5` 正 `RD2`、左 `RD4`；`R6` 正 `RD3`、右 `RD4`；`R1`／`R4` 之正面（中原路）⛔ 臨任何道路 `BLOCK`（區外·未勾 ⇒ ⛔ 警示）；臨接比皆 `1`（`R1` 右側之首段依 `snap_m` 計入）；垂距 × 2 ＝ `8.00`（`R1` 左 `7.9998`、`R2` 正 `7.9997`）；中心線之另一側之地籍之平均寬 `3.977`〜`4.000 m`（⛔ 區界）；比例皆 `1`；`calc_special_burden_total` 給尺度與否之列逐值同（臨街地特別負擔總面積 `741.76` ㎡·`C` ＝ `0.1`·長度以替身）。**二態之對拍**（前態 ＝ 工項一之端、後態 ＝ 原型·二退縮）：`k6s3 cmp` 二退縮 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 之落檔與 `stdout` 前後逐位同（發單側之二樹之 `HEAD` 皆 `158f7fe`·⛔ 須正規化）、末列皆 `⇒ rc 0（不符 0 項）`——配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`、手冊先行 session 鍵 `f3_k953_log` `37`／`46` 列；十二呼叫與二 `cmp` 之 `stderr` 合計 `0` B ⇒ **配地⛔ 變**（`V-4`〜`V-6`）。**模擬**（`F30 run`·資料檔之複本·記憶體）：`628-34` 填「抵充地」、臨 `RD1` 之二面改未勾 ⇒ `RD1` `1082.2651 ㎡`、該宗於其內之片 `131.60 ㎡` ⇒ 比例 `0.878403`·負擔路寬 `7.0272 m` ⇒ `R2` 正面 `1.513616`（外部錨 `1.513613`）、`R1` 左側 `0.756808`（`0.756806`）、他面⛔ 變；`628-37`（私有）填「是」⇒ 填列錯誤一則（逐字見 `F30`）；`JUNCTION` 框（`RD1` 之外接矩形之西端 `10 m`·框內 `89.6652 ㎡`）⇒ 比例 `0.867420` ⇒ `R2` 正面 `1.469679`（外部錨同）；換檔 ⇒ 重讀 |
| `6` | 判別力（發單側窗八十七·倉外·原型之上逐一施一突變） | （一）`F30 selftest`（新碼之突變·錨 ＝ 原型之字樣·⛔ 入器〔受單側之碼異〕·以受單側之碼之字樣為錨之突變另單補寫）十二種皆捕：M1 未勾新闢亦以比例 `1` ⇒ `K2`／`K3`／`K7`／`K10`；M2 勾新闢亦依比例 ⇒ `K2`；M3 區界仍以輸入路寬 ⇒ `K4`／`K5`；M4 `JUNCTION` 框內亦計 ⇒ `K10`；M5 一面取臨接最多之段 ⇒ `K7`；M6 小碎塊以「≤ 0.6」判 ⇒ `K6`；M7 無道路 `BLOCK` ⛔ 警示 ⇒ `K8`；M8 取樣⛔ 容差 ⇒ `K15`；M9 公私共有以全宗計 ⇒ `K12`；M10 `calc_special_burden_total` ⛔ 用呼叫端之尺度 ⇒ `K14`；M11 二地段同地號唯查註記者 ⇒ `K12`；M12 無宗地仍判區界 ⇒ `K16`。（二）`F30 wiring` 九種皆捕：錯誤之支⛔ `st.stop()` ⇒ `W5`；`temp_parcels` 以 `[]` 代之 ⇒ `W2`／`W5`；`main` 之既有一列刪之 ⇒ `W7`；`JUNCTION` ⛔ 存 ⇒ `W4`；`verify/stepg_pipeline.py` 呼新名 ⇒ `W6`；無其面亦增 `0` ⇒ `W5`；頂層增一輔助函式 ⇒ `W7`；新函式含案件字面 ⇒ `W1`；`calc_special_burden_total` 之既有一列改之 ⇒ `W7`。（三）`F30 run` 四種皆捕：取樣⛔ 容差 ⇒ `R1`／`R2`；二欄之結果⛔ 存 ⇒ `R6`；畫面⛔ 傳 `JUNCTION` ⇒ `R5`；畫面之未勾以勾計 ⇒ `R1`／`R3`／`R5`。（四）`F23` `K75`：令手冊先行之輪之道路之片亦再排（`_sort953(_tin953[_x]) != 'pub'`·`W-G.9-384R` ⑥-2 之 (丙) 二之突變）⇒ `K75` 紅（例外·道路 `BLOCK` 無五級之屬性）；其餘 `K1`〜`K74` 綠。（五）`F23 wiring`／`F24 wiring`／`F25 wiring` 之許之增：工項一之端（未施生產碼）皆綠、原型皆綠；⛔ 增許之原型 ⇒ `F23` `W6`／`W7`、`F24` `W5`、`F25` `X2` 紅（發單側撰器前實跑） |
| `7` | `run_all` | ⛔ 跑（單首之「級」·`§四-1` 工項二之「⛔ 跑之由」） |

---

## `§二`　KL 之語與射程

🔒 **所據**：`CLAUDE.md` 待落地清單 `W-G.9-384` 之節之序 `6`（`K-9-74`·落地之單 `W-G.9-385`·前置 ＝ `K-9-62` 之抵充地之欄）；`K-6` 典 `K-9-74` 之節（`W-G.9-382`·其【工】之讀法甲〜己）、`K-9-62`（`2026-10-06`·「重劃區地籍」工作表之二欄與填列錯誤）、`K-9-59` ⑤（`JUNCTION`·選用）；`W-G.9-384` 補令一單首之 🛑（待落地清單之「`W-G.9-384` 已入主線」、原單之唯讀審查之 (丙) 二之例 ⇒ 皆併本單）；`W-G.9-384R` 報告 ⑥-2 之 (丙) 二、三；KL 之語（下開）。

🔒 **KL 之語**（逐字）：
- `2026-10-13 21:48` 第 `6` 點、`23:06` 第 `3`、`4` 點、`23:21`（⇒ `K-9-74`·全文、所呈與其受詞見 `K-6` 典 `W-G.9-382` 之節之二）。
- `2026-10-06 03:06` 第 `3` 點（⇒ `K-9-62` 之二欄·全文見 `K-6` 典 `K-9-62` 之節）。
- `2026-10-16 11:19`：「核對無誤」（⇒ `W-G.9-384` 補令一·`W-G.9-384` 之入主線·塊 `K25` 之一）。
- `2026-10-16 12:25`（答發單側窗八十七之擬單前之請示·所問與所答見塊 `K25` 之二）：
  > 1. 問一：乙
  > 2. 問二：乙，併顯示警示文字，例如：「R1正面道路勾選新闢，但未臻側道路BLOCK」，"正面"可替換為"右側"或"左側"
  > 3. 確認一下，路口道路仍需劃設一個矩形BLOCK，再畫設一個JUNCTION圖層?(即2矩形圖層位置重疊)
  > 4. 本測試案雖沒有D 欄新增「第33條排除」、E 欄新增「抵充地」，但你還是要模擬相關情形，以為了未來泛用化的測試
- `2026-10-16`（發單側窗八十七之效率之令之答·對話）：CC 之並行之限由 `2` 調為 `6`（單首 🔑·KL「1,2 兩種方式都用」之其一）。

🔒 **【工】之讀法**（塊 `K25` 之三·以交付之通知告 KL）：甲 二欄之讀與檢核；乙 臨接之道路（取樣）；丙 比例；丁 中心線即區界；戊 一面之尺度（`K-9-79` ①）；己 警示與錯誤；庚 畫面（步驟 E／H）；辛 harness ⛔ 動；壬 本案；癸 `W-G.9-384` 之唯讀審查之 (丙) 二、三。

🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 之畫面核對與逐字放行**。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支（附則甲〜丙）；`(c)` ⛔ 及主線、他側支、KL 主 checkout、`data/` 之資料檔、`K-9-62` 之指配、`K-9-78`、`GB-205`、`K-9-59`〜`K-9-61`、`K-9-63`、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**：
- 「**面**」＝ 可建築街廓之正面（`front`）、左側（`left`）、右側（`right`）；其名 ＝ `正面`／`左側`／`右側`。其線 ＝ 正面線（`f3_cad_front_lines` 之 `{街廓: {'p1', 'p2', …}}`）、側面線（`f3_cad_side_lines_by_side` 之 `{街廓: {'left'|'right': {'p1', 'p2', …}}}`）；**無其線之面⛔ 計**（照舊之式·`R-6`）。
- 「**道路 BLOCK**」＝ `f3_classified_blocks` 之中 `_is_road_like_category(category)` 為真者（其 `label`、`vertices`）；「**中心線**」＝ `f3_manual_road_centerlines` 之 `{道路 BLOCK 之 label: [(x, y), …]}`（二點以上之折線）；「**宗地之片**」＝ `temp_parcels` 之各元（`原地號`、`所屬街廓`、`polygon_coords`）——**地籍**唯計原地號⛔ 以 `_GHOST` 起首者。
- 「**輸入**」＝ 步驟 E 之 `SS_ROAD` 之 `{街廓之 id: {'front_width', 'front_new', 'left_side_width', 'left_side_new', 'right_side_width', 'right_side_new', …}}`（左側缺鍵者依既有之 `side_width`／`side_new` 補之·同 `main` 之步驟 H 之舊式）。
- 「**正規化地號**」＝ `_normalize_landno_module(<地號>)`（既有·同 `t8_ownership_map` 之鍵）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | 新頂層常數 `K974_PARAMS`（`dict`·置於 `calc_special_burden_total` 之後） | 恰六鍵：`'sample_n': 400`、`'sample_offset_m': 0.5`、`'snap_m': 0.1`、`'width_warn_m': 0.5`、`'fragment_avg_m': 0.5`、`'side_name': {'front': '正面', 'left': '左側', 'right': '右側'}`。下列各條之數皆取自此（⛔ 另書其字面）。 |
| `R-2` | 新頂層 `k962_land_marks(df_rezoning, df_uland)`（純函式·置於 `K974_PARAMS` 之後） | 回 `{'抵充地': {正規化地號: 公有持分}, '第33條排除': {正規化地號: 公有持分}, 'errors': [訊息…]}`。① `df_rezoning` 為 `None` 或其欄⛔ 含「第33條排除」「抵充地」之任一 ⇒ 回三空（`{}`、`{}`、`[]`）；欄以**欄名**認之（⛔ 依位置）。② 逐列（原序）、逐欄（序 ＝ 「第33條排除」→「抵充地」）：其值去前後空白後為空、`None`、`NaN`、`'nan'` 或「否」⇒ 略；為「是」⇒ 註記；他值 ⇒ 錯誤 `f'填列錯誤：{地段} {地號}「{欄名}」欄填「{值}」，僅得填「是」或空白'`（`地段`、`地號` ＝ 該列之「地段」「地號」去前後空白·`值` ＝ 去前後空白者）。③ 註記者：`df_uland` 為 `None` ⇒ 公有持分 ＝ `0`（⇒ 下開「非公有地」之錯誤）；否則於 `df_uland` 取「段小段」去其前導之數字（`r"^\d+"`）＝ 地段、`pd.to_numeric(「地號」, errors='coerce')` ＝ 地號之整數（地號之文字 `'a-b'` ⇒ `a × 10000 ＋ b`、`'a'` ⇒ `a × 10000`；其轉換拋例外者視為無之）之列；無之 ⇒ 錯誤 `f'填列錯誤：{地段} {地號}「{欄名}」欄填「是」，但 U_LAND 無對應資料'`；有之 ⇒ 所有權人去重（鍵 ＝ 「所有權統一編號」去前後空白而非空、非 `'nan'` 者，否則「姓名」去前後空白·同 `build_ownership` 之歸戶指紋），公有持分 ＝ Σ（「公私別」去前後空白 ＝「公」之所有權人之「權利範圍分子」÷「權利範圍分母」）；其 ≤ `0` ⇒ 錯誤 `f'填列錯誤：{地段} {地號}「{欄名}」欄填「是」，但該地號非公有地（U_LAND 公私別）'`。④ 其正規化地號於 `df_rezoning` 之諸列見於二以上之相異地段（不論他地段之列有無註記）⇒ 錯誤 `f'填列錯誤：地號 {地號} 於 {"、".join(諸地段·依其於 df_rezoning 首見之序)} 皆有，「{欄名}」無從對應宗地'`。⑤ 餘 ⇒ `out[欄名][正規化地號] = min(公有持分, 1.0)`。錯誤之序 ＝ 逐列、逐欄之序；有錯誤之格⛔ 入 `out[欄名]`。 |
| `R-3` | 新頂層 `k974_read_junctions(doc)`（純函式·置於 `k962_land_marks` 之後） | `doc.modelspace().query('LWPOLYLINE POLYLINE')` 之中圖層名 `.upper() == 'JUNCTION'` 者，依其序各取頂點 `[(float(x), float(y)), …]`（`LWPOLYLINE` ＝ `get_points()` 之前二元；`POLYLINE` ＝ `vertices` 之 `dxf.location`）；三點以上者入回傳之 `list`；讀取之例外 ⇒ 略該實體（`query` 本身之例外 ⇒ 回 `[]`）。 |
| `R-4` | 新頂層 `k974_burden_scales(build_polys, road_polys, centerlines, front_lines, side_lines_by_side, pieces, offset_share, road_inputs, junctions=())`（純函式·置於 `k974_read_junctions` 之後） | 受：`build_polys` ＝ `{街廓: 頂點}`；`road_polys` ＝ `{道路 BLOCK: 頂點}`；`centerlines` ＝ `{道路 BLOCK: 折線}`；`front_lines`／`side_lines_by_side` ＝ 用語之形；`pieces` ＝ 宗地之片之 `list`；`offset_share` ＝ `{正規化地號: 公有持分}`（抵充地）；`road_inputs` ＝ `{街廓: {'front'|'left'|'right': (路寬, 新闢)}}`（缺者 `(0.0, False)`）；`junctions` ＝ `JUNCTION` 之頂點之 `list`。回 `{'scales': {街廓: {面: 尺度}}, 'detail': [列…], 'warnings': [訊息…], 'errors': [訊息…]}`。**逐街廓（`sorted`）、逐面（序 ＝ `front` → `left` → `right`·無其線者略）**：⓪ 線長為 `0` 之面略之（⛔ 入 `scales`、`detail`）。① **臨接**：其線 `p1 → p2` 均分 `sample_n` 段，第 `i` 段之中點（`t ＝ (i ＋ 0.5) ÷ sample_n`）沿線之單位法向往**街廓外**偏移 `sample_offset_m`（法向先取 `(−dy, dx) ÷ 線長`〔`dx`、`dy` ＝ `p2 − p1`〕；線之中點沿之偏移之點落於該街廓之多邊形〔`contains`〕者反其向；否則用之）；其點落於某道路 BLOCK（`contains`·依 label 之 `sorted` 取首見者）⇒ 該段臨之；皆⛔ 落而距某道路 BLOCK（`distance`）≤ `snap_m` ⇒ 臨其最近者（同距依 label 之序）；餘 ⇒ ⛔ 臨。② **皆⛔ 臨**（段數 `0`）：尺度 ＝ `0.0`；勾新闢 ⇒ 警示 `f'{街廓} {面名}道路勾選新闢，但未偵測到道路 BLOCK'`（`K-9-79` ②）；`detail` 增一列（`道路` ＝ `'（無）'`）。③ **各臨接之道路 BLOCK**（依 label 之 `sorted`）：無中心線或其點 ＜ `2` ⇒ 錯誤 `f'道路 BLOCK {label} 未繪 CENTERLINE（{街廓} {面名}臨之），請補畫'`、略之；**垂距** `d` ＝ 臨接之諸段之 `t` 之平均（`tm`）於線上之點至中心線之最近一節（`LineString` 之 `distance` 最小者·同者取先）之**直線**之距離（法向距·`|cross| ÷ 節長`），其側 ＝ 該叉積之號；**區界**：宗地之片（地籍）之聯集為空 ⇒ ⛔ 判（`False`）·另於函式之末增警示一則 `'尚無宗地資料（地籍），中心線是否為重劃區界⛔ 判（以輸入之路寬計）'`（全次唯一則）；否則 ⇒ 中心線之**另一側**（與該點異側）寬 `d` 之單側帶（`LineString(中心線).buffer(±d, single_sided=True)`·號依側）與地籍之聯集之交之面積 ÷ 中心線之長 ＜ `fragment_avg_m` ⇒ `True`；**比例** `r`：勾新闢 ⇒ `1.0`（⛔ 求 `A`、`B`·下開 `A` ≤ `0` 之錯誤亦⛔ 及之）；否則 ＝（`A` − `B`）÷ `A`，`A` ＝ 道路 BLOCK 之多邊形去 `JUNCTION` 之聯集（`difference`）之面積、`B` ＝ Σ（所屬街廓 ＝ 該 label 之宗地之片 ∩ 上開之去後之多邊形）之面積 × `offset_share.get(正規化原地號, 0.0)`；`A` ≤ `0` ⇒ 錯誤 `f'道路 BLOCK {label} 扣除路口後之面積為 0（{街廓} {面名}臨之）'`、略之；**警示**：路寬 ＞ `0` 且 `|2d − 路寬|` ＞ `width_warn_m` ⇒ `f'{街廓} {面名}：中心線垂距 × 2 ＝ {2d:.2f} m，與輸入路寬 {路寬:.2f} m 相差逾 {K974_PARAMS["width_warn_m"]} m，請確認'`（後者⛔ 格式化 ⇒ 「0.5」·⛔ 停機）；**負擔路寬** ＝（區界 ⇒ `d`；否則 ⇒ 路寬）× `r`；**該段之尺度** ＝ 正面 ⇒ `calc_frontage_burden_scale(負擔路寬)`、側面 ⇒ `calc_side_burden_scale(負擔路寬)`。④ **一面之尺度**（`K-9-79` ①）＝ Σ（該道路 BLOCK 之臨接段數 ÷ `sample_n`）× 該段之尺度（**權 ＝ 段數之比**·⛔ 以長度之浮點）——自 `0.0` 起，依道路 BLOCK 之 label 之 `sorted`，每一道路 BLOCK 恰加一次 `(段數 / sample_n) * 尺度`（⛔ 逐段累加；本案 `F30 run` 之 `R1` 以 `==` 比快照之輸入）。⑤ `detail` 之列：每一（面、臨接之道路 BLOCK〔③ 略之者除外〕）恰一列，皆⛔ 臨之面恰一列（`道路` ＝ `'（無）'`）；⛔ 他列（面之彙總等）。其鍵恰為 `'街廓'`、`'面'`、`'道路'`、`'臨接比'`（`round(·, 4)`）、`'基寬(m)'`、`'比例'`、`'區界在中心線'`、`'垂距×2(m)'`、`'負擔路寬(m)'`、`'尺度'`。⑥ 多邊形非 `is_valid` 者以 `buffer(0)` 正之。⛔ 讀 session、⛔ 停機（錯誤唯入回傳）。 |
| `R-5` | 新頂層 `k974_screen_scales(ss, build_blocks, temp_parcels, road_key)`（置於 `k974_burden_scales` 之後） | ① `ss.get('f7_saved')`（tab1 所存之 `(檔名, bytes)`）有之 ⇒ `h ＝ hashlib.sha256(<bytes>).hexdigest()`（十六進位之字串）＝ `ss.get('f3_k962_marks_cache')` 之元 `0`（`tuple`·長 `2`）⇒ 用其元 `1`；否則以 `pd.ExcelFile` 讀之：含「U_LAND」「重劃區地籍」二表者，讀「重劃區地籍」（`header=0`）；其二欄之任一有 `notna()` 之格 ⇒ 另讀「U_LAND」、否則以 `None` 代之；`k962_land_marks(<重劃區地籍>, <U_LAND 或 None>)`；缺表者 ⇒ 三空；其結果（缺表者之三空亦然）以 `ss['f3_k962_marks_cache'] = (h, 結果)` 存之。無 `f7_saved` ⇒ 三空（⛔ 存）。② 道路 BLOCK ＝ `{b['label']: b.get('vertices') for b in ss.get('f3_classified_blocks') or [] if _is_road_like_category(b.get('category', '')) and b.get('vertices')}`；`build_polys` ＝ `{b['label']: b.get('vertices') for b in build_blocks}`；`road_inputs` ＝ `{b['label']: {'front': (r.get('front_width', 0.0), bool(r.get('front_new', False))), 'left': (r.get('left_side_width', r.get('side_width', 0.0)), bool(r.get('left_side_new', r.get('side_new', False)))), 'right': (r.get('right_side_width', 0.0), bool(r.get('right_side_new', False)))}}`（`r` ＝ `(ss.get(road_key) or {}).get(b['id'], {}) or {}`）；呼 `k974_burden_scales(build_polys, <道路 BLOCK>, ss.get('f3_manual_road_centerlines') or {}, ss.get('f3_cad_front_lines') or {}, ss.get('f3_cad_side_lines_by_side') or {}, temp_parcels or [], <結果>['抵充地'], road_inputs, junctions=ss.get('f3_cad_junctions') or [])`。③ 回其回傳，唯 `errors` ＝ `k962_land_marks` 之 `errors` ＋ 其 `errors`（序依之）。 |
| `R-6` | `calc_special_burden_total` | **唯增列**（既有之列⛔ 刪改）：既有之 `fs`／`lss`／`rss` 之三列之後，列含鍵 `'front_scale'`／`'left_side_scale'`／`'right_side_scale'` 者，`fs`／`lss`／`rss` 各 ＝ 其值之 `float`（⛔ 依新闢）；無之者照舊。docstring 之末增一款（以 ``🔧 `W-G.9-385` `` 起首）述之。 |
| `R-7` | `main()` | **唯增列；下開三列須易之**（皆刪去·代以新文·其新文自定·須含「K-9-74」；三列皆易方合 `F30 wiring` 之 `W7`）：步驟 E 之 `st.caption` 之「路寬長度計算至……僅新闢道路計入臨街地特別負擔。」之列；步驟 H 之公式說明之「- 正面道路負擔面積 = 正街負擔尺度 × 正面長度（僅新闢道路）」「- 側面道路負擔面積 = 側街負擔尺度 × 側面長度（僅新闢道路）」之二列（`F30 wiring` 之 `W7` 以其 `sha256` 比之）。增：① CAD 精準圖層直讀之 `st.session_state['f3_cad_dxf_quantum'] = _cad_layers.get('dxf_quantum')` 之列之後，恰一句 `st.session_state['f3_cad_junctions'] = k974_read_junctions(_doc_cad_p7)`。② 步驟 H 之既有之 `road_data = []` 之列之前（同縮排·`8` 格），恰一列 `        _k974 = k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)`（逐字·⛔ 附行末之註·註另成列），其後、**仍在 `road_data = []` 之前**：`_k974['warnings']` 之各則 ⇒ `st.warning(f"⚠️ {訊息}")`；`_k974['errors']` 非空 ⇒ 各則 `st.error(f"⛔ {訊息}")` 後 `st.stop()`。③ 既有之 `road_data.append({…})` 之後（同一 `for b in build_blocks` 之內），依 `_k974['scales'].get(b['label'], {})` 之有之面，增其列之鍵 `'front_scale'`／`'left_side_scale'`／`'right_side_scale'`（無之面⛔ 增）。②③ 之段止於既有之 `        sb = calc_special_burden_total(road_data, C_for_calc)` 之列（`F30 wiring` 之 `W5` 抽之、唯給 `st`、`k974_screen_scales`、`build_blocks`、`temp_parcels`、`SS_ROAD`、`C_for_calc`、`calc_special_burden_total` 之名而實跑 ⇒ 其段之增列⛔ 用他名〔`K974_PARAMS`、`pd` 等〕，唯其段內自賦之名與 Python 之內建）。④ 既有之「各街廓臨街地負擔計算」之表之後，`_k974['detail']` 非空 ⇒ 一 `st.expander`（標題含「K-9-74」）內 `st.dataframe` 示之。⑤ 步驟 E 之 caption 之新文載：勾新闢者全寬；未勾者依道路 BLOCK 扣除抵充地後之比例；拓寬既有道路者不勾新闢（`K-9-74` 戊）；道路在區外者不計。 |
| `R-8` | docstring 與註 | 五新名各有 docstring（以 ``🆕 `W-G.9-385` `` 起首·述其 `R-*`）；`main` 之增列得各以一註述之（以 ``🆕 `W-G.9-385` `` 起首）。🔒 新書之 docstring、註與訊息⛔ 含 `§三-3` 之 `2` 所列之字樣、⛔ 重寫既有之字樣；他處之 docstring 與註⛔ 改。 |
| `R-9` | 字樣（列框·`git grep -c -F … -- app.py`） | 施後：「def k962_land_marks」「def k974_read_junctions」「def k974_burden_scales」「def k974_screen_scales」各恰 `1`；「K974_PARAMS = {」恰 `1`；「_k974 = k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)」恰 `1`；「k974_read_junctions(_doc_cad_p7)」恰 `1`；「僅新闢道路計入臨街地特別負擔」`0`；「sb = calc_special_burden_total(road_data, C_for_calc)」恰 `1`（同施前）。 |
| `R-10` | 本案 | 二退縮之配地、街角得標與強制旗標、段三／末端塊合併再試／手冊先行／第一趟之紀錄、入池閘之紀錄、調配之輸入、畫面與 harness 之對拍之結果皆⛔ 變（harness ⛔ 動·`§一` 項 `5`）；本案之圖資與地籍之 `k974_screen_scales` 之各面之尺度 ＝ 快照之 `負擔尺度_輸入`、警示與錯誤皆 `0`（`F30 run` 之 `R1`）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F30`（`verify/probes/probe_WG9385_k974.py`·新）：`selftest` 之 `K1`〜`K16`（`R-2`〜`R-4`、`R-6`）；`wiring` 之 `W1`〜`W7`（`R-1`〜`R-9`·其 `W7` 以 `158f7fe` 為基準）；`run` 之 `R1`〜`R6`（`R-5`、`R-10`·本案之圖資與地籍·資料檔之複本〔記憶體·⛔ 寫檔〕之二欄之模擬）。
- `F23`（`probe_WG9363_k953.py`）：增 `K75`（`W-G.9-384` 之唯讀審查之 (丙) 二·⛔ 涉本單之碼·新舊皆綠）；`W6` 之受詞去 `main`、`calc_special_burden_total`；`W7` 之許增五新名與二函式。`F24`（`probe_WG9367_adj4.py`）`W5` 之許、`F25`（`probe_WG9370_adj4mut.py`）`X2` 之許，同增之。
- `app.py` 之頂層節點對 `158f7fe` 相異者 ⊆ `{K974_PARAMS, k962_land_marks, k974_read_junctions, k974_burden_scales, k974_screen_scales, calc_special_burden_total, main}`，**頂層之新名唯其前五**；`verify/` 之生產碼⛔ 改。

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **突變之錨**（`F27 mutate`·`MUT377` 之 `N01`〜`N57`；`F25 mutate`；`F19 mut`；`F22 mut`）：其錨所在之函式本單⛔ 動（`§三-2` 之集外）⇒ 自然⛔ 觸；`main` 之既有之列⛔ 刪改（`R-7` 之三列除外）。`F27 mutate`、`F19 mut`、`F22 mut`、`F25 mutate` 之期 ＝ `§五-1` 項 `8`。
2. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計·含引號）；**基準中恰一之函式名（含巢狀）於工作樹仍恰一** ⇒ 新函式之巢狀之 `def` ⛔ 用既有之名（發單側之原型初稿之巢狀 `_perp` 與既有之同名者撞 ⇒ `W8`／`W7` 紅·改名避之）。CC 撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
3. **頂層之名之許**（`F23 wiring` 之 `W7`、`F24 wiring` 之 `W5`、`F25 wiring` 之 `X2`、`F30 wiring` 之 `W1`／`W7`）：塊 `Fy35` 所增之許 ＝ `§三-2` 之集 ⇒ **頂層之新名唯五**（輔助之函式一律巢狀）。
4. **⛔ 案件字面**（`F30 wiring` 之 `W1`）：四新函式之字串常數⛔ 含 `R1`〜`R6`、`RD1`〜`RD4`、`628-`、`G1`、`UC9898`、`德安` 之任一子字串。
5. `F17 wiring`、`F25 wiring` 之 `X3`／`X5`、`F10 wiring` 之 `W4`、`F27 wiring` 之 `Y1`〜`Y9`、`F29 wiring` 之 `Y1`〜`Y11`、`F14`／`F15`／`F9`／`F4` 之接線之項⛔ 觸。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`K-9-74`、`K-9-62`（二欄）、`K-9-79` 已裁（`K-6` 典）；其落地之讀法 ＝ 塊 `K25` 之三（【工】·以交付之通知告 KL）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地或諸紀錄有任一改變；本案之各面之尺度 ≠ 快照之 `負擔尺度_輸入`；`§三-1` 之式於某形無從定之（例：線之中點之二向之偏移點皆落於街廓內、中心線之最近之節有二而其側相異）。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-9`）：落於何處、其字樣；對 `§三-3` 各款之自查；附則乙之自查（`R-2` 之錯誤之序與其五形、`R-4` 之臨接之取樣與容差、垂距與其側、區界之帶、比例之母體〔`JUNCTION` 之去〕、權 ＝ 段數之比、警示與錯誤之字樣、`R-5` 之存與換檔、`R-6`／`R-7` 之唯增列與三易列）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-385-k974`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-385_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-385 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-385-k974`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`45`**、主線仍 ＝ `158f7fe…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-385-k974`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy35` 抽為 `<O>\Fy35.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`4` 檔（`3` 改·`1` 新）之 `git hash-object` ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `4` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-385 工項一：量測器（F30 之新器·F23 之 K75 與 W6／W7 之許·F24、F25 之許）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-385-k974`。

**工項二　生產碼**（🔴 `app.py`·CC 依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`）：
1. 紅（末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`python verify/probes/probe_WG9385_k974.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K0']；rc 1`（五新名皆缺）；`… wiring <repo> 158f7fe` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W7']；rc 1`（`W6` 綠）；`… run <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['R0']；rc 1`（新名缺 ⇒ ⛔ 起其後之量）；三呼叫之 `stderr` 皆 `0` B。🔒 `F23 selftest`（含 `K75`）於工項一之端 **`rc 0`**（`P0 逐項擾動恰該項紅 75／75`·`K75` 新舊皆綠）——屬前置 `2`。
2. 綠（**`rc 0`**·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`V-1`／`V-2` 之其餘之呼叫（同 `§四-1` 之驗之命令）。
3. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`；`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_pre_35.json`；同 `0.0` ⇒ `<O>\f8_pre_00.json`；`python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_pre.json`；同 `0.0` ⇒ `<O>\parity00_pre.json`（皆 `rc 0`）。
4. `git grep -c -F "def k974_burden_scales" -- app.py` ⇒ 無出艙、`rc 1`；`git grep -c -F "僅新闢道路計入臨街地特別負擔" -- app.py` ⇒ 出艙恰一列 `app.py:1`；`git grep -c -F "k974_read_junctions(_doc_cad_p7)" -- app.py` ⇒ 無出艙、`rc 1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫 `app.py` 之改動；`python -m py_compile app.py`；`commit` 訊息之首列逐字 `W-G.9-385 工項二：K-9-74 之落地（臨街地特別負擔之路寬：臨接之道路 BLOCK·抵充地之比例·中心線即區界·一面臨二段以上依臨接長度加權〔K-9-79〕）與 K-9-62 之二欄之讀取與檢核·步驟 H 之尺度 🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>\*_post.*`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy35` 所改、所增之器（`7` 呼叫）：`python verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`… run <repo>`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F30 selftest` 之 `K1`〜`K16`、`F30 wiring` 之 `W1`〜`W7`、`F30 run` 之 `R1`〜`R6` 皆 ✅；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` |
| `V-2` | 其餘之 `48` 呼叫（同 `W-G.9-384` 規格單 `§四-1` 之 `V-1`〜`V-2` 之命令·其中上列者除外）：`F29`（`probe_WG9375_k965.py selftest`／`wiring`／`run`）、`F23 run`、`F24`（`selftest`／`run`）、`F25 mutate`、`F27`（`probe_WG9373_k966.py selftest`／`wiring`／`mutate`／`run`）、`F28`（`probe_WG9373p1_partrem.py selftest`）、`F14`（`selftest`／`run`）、`F17 wiring`、`F8`（`selftest`／`wiring`）、`F4 wiring`、`F9`（`selftest`／`wiring`／`run`）、`F10`（`selftest`／`wiring`／`run`）、`probe_WG9352_endblock.py`／`probe_WG9353_endmerge.py`／`probe_WG9354_endcontest.py` 之 `selftest`／`wiring`、`F15 wiring`、`F16`（`selftest`／`run`）、`F18`（`selftest`／`wiring`）、`F19 mut`、`F21`（`selftest`／`wiring`／`run`）、`F22 mut`、`F26`（`selftest`／`run`）、`probe_WG9344_k6s3.py selftest`、`probe_WG9344p1_pooltemp.py selftest`、`probe_WG9348_harvest_key.py`、`probe_WG9341_synth.py`、`probe_WG9340_main_synth.py`、`probe_WG9346_failclosed.py run <repo> 3.5` | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列 |
| `V-3` | `V-1`〜`V-2` 之 `55` 呼叫之器之載入 | 本批所改、所增之器 `4` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`… cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**·`R-10`） |
| `V-5` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置 `3` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（CC 以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異）；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0` |
| `V-6` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_post_35.json`；同 `0.0` ⇒ `<O>\f8_post_00.json`；`git hash-object <O>\f8_pre_35.json <O>\f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`1`**（`app.py`）；其增／刪之數與其 blob 出艙（發單側復驗時自倉重算·⛔ 預載）；`verify/` 之一切檔對工項一之端相異 `0`；`app.py` 之頂層節點之名之集 ＝ 工項一之端之集 ∪ `{K974_PARAMS, k962_land_marks, k974_read_junctions, k974_burden_scales, k974_screen_scales}`（AST）；其相異之節點 ＝ 此五 ∪ `{calc_special_burden_total, main}` |
| `V-8` | `R-9` 之字樣（`git grep -c -F "<字樣>" -- app.py`·逐一） | 「def k962_land_marks」「def k974_read_junctions」「def k974_burden_scales」「def k974_screen_scales」「K974_PARAMS = {」「_k974 = k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)」「k974_read_junctions(_doc_cad_p7)」「sb = calc_special_burden_total(road_data, C_for_calc)」⇒ 各 `app.py:1`；「僅新闢道路計入臨街地特別負擔」⇒ **無出艙**、`rc 1`（判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**；逾時之重跑依單首 🔑）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞於本案之配地⛔ 觸（harness ⛔ 動·`§一` 項 `5`），其「⛔ 變」由 `V-4`〜`V-6` 與 `F23 run`／`F24 run`／`F27 run`／`F29 run`／`F16 run`／`F14 run` 直接量之；畫面之步驟 H 之尺度由 `F30 run` 之 `R1` 量之。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：`R-2` 之五形之錯誤之字樣與其序、去重之鍵、公有持分、二地段之判；`R-3` 之圖層與點數；`R-4` 之取樣（段數、中點、偏移之向）、容差（最近者·同距之序）、垂距（最近之節之直線·側）、區界之帶（另一側·寬 ＝ 垂距·地籍之聯集·`_GHOST` 除外·無宗地之警示）、比例之母體（`JUNCTION` 之去·片之交·公有持分）、權 ＝ 段數之比、勾新闢之比例 `1`、警示與錯誤之字樣；`R-5` 之存與換檔、`road_inputs` 之左側之補；`R-6` 之唯增列；`R-7` 之三易列與增列之置處、`st.stop()`、無其面之鍵⛔ 增；以獨立之合成之例（`F30` 之外·至少一例：一面臨三段、一段在區外）比 `k974_burden_scales` 與手算；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-385-k974`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K25` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `E28` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P38` 附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；三檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P38` 附後：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-385 工項三：W-G.9-384 之入主線·K-9-79 之立·K-9-74 與 K-9-62 二欄之落地之讀法入典 ＋ 自誤 621 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-385-k974`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-385R_K-9-74之落地_執行報告.md` ＋ 同目錄之 `W-G.9-385R_K-9-74之落地_app差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之七呼叫之全文、`V-2` 之 `F27 mutate`／`F25 mutate` 之全文、`V-5` 之正規化之比與其對照、`V-6` 之 `hash-object` 之出艙、`F23 run`／`F16 run`／`F29 run` 之末十四列、`k6s3 cmp` 之全文、`parity` 之末十五列、`55` 呼叫之 `rc`／`stderr`／耗時／末列之表〔重跑者二趟並載〕）；④ 塊之實得（bytes／`sha256`）與三簿之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **`app.py` 之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**（並行之數）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-385 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-385-k974`。

### `§四-2`　次單（⛔ 本單之期）

發單側復驗本批之碼（自倉重跑 `V-1`〜`V-9`）後：**入主線之請示**（本批·生產碼·配地⛔ 變）·附 KL 於畫面之核對（新側支之端之 `app.py`·退縮 `3.5 m`·全新視窗：步驟 E 之說明之新文；步驟 H 之「各街廓臨街地負擔計算」之正街／左側／右側尺度 ＝ 主線之端之同表；其下之「K-9-74」之明細之展開；B 值與 G 值迭代之配地 ＝ 主線之端）＋ 主 checkout 之同步（塊 `P38` 之依賴序）；其後待落地清單序 `9`（其序另呈 KL）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9363_k953.py` `17`／`0`、`probe_WG9367_adj4.py` `5`／`0`、`probe_WG9370_adj4mut.py` `5`／`0`、`probe_WG9385_k974.py` `563`／`0`（唯此 `4` 檔）（增／刪）；工項二 ＝ `app.py`（唯此一檔·其數出艙）；工項三 ＝ `K-6` 典 `120`／`0`、自誤簿 `13`／`0`、`CLAUDE.md` `27`／`0`（唯此三檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `158f7fe` | 生產碼相異恰 **`1`**（`app.py`）；`verify/` 之一切檔相異恰 **`4`**（`M` `3`：`probe_WG9363_k953.py`、`probe_WG9367_adj4.py`、`probe_WG9370_adj4mut.py`；`A` `1`：`probe_WG9385_k974.py`）；本批之新檔（本單、新器、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`11` 檔：本單、`4` 器、`app.py`、`K-6` 典、自誤簿、`CLAUDE.md`、報告二檔） |
| `4` | 三簿之 bytes | `K-6` 典 `801055` → **`815930`**；自誤簿 `1196778` → **`1198828`**；`CLAUDE.md` `408690` → **`413291`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊 |
| `5` | 自限 | 遠端 heads **`45`**；主線 ＝ `158f7fe959697571d8179988cd4c192c0016ead9`（⛔ 變）；`verify/W-G.9-385-k974` ＝ 工項四之 `commit`，其祖含 `158f7fe`；其餘 `44` 列逐列 ＝ `<O>\heads_before.txt` |
| `6` | `python verify/probes/probe_WG9270_closegate.py 621 620 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 622 621 .` ⇒ `rc 7` |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 621 620` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`606`**／`MAX` **`621`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` **`76`**／**`79`**／`[44, 47]`（自誤唯增 `621`；`K-9` 唯增 `79`；餘 ＝ 開工態） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `Fy35` | `42206` B·`sha256` `971c7f3a4403b947d4ae1e9e0055d2668fc281c308f7da8638bcd5977adb90ba`·`657` 列（圍欄內全文·末附換行）；抽為 `<O>\Fy35.diff`，`git apply` 於 `verify/probes/` 之 `4` 檔（`3` 改·`1` 新），其施前 blob（B）：`probe_WG9363_k953.py` `abe2f7fabe818bda5b71ef41a8b59aa3335be85b`（`125317`）、`probe_WG9367_adj4.py` `2992e4ff721e642b913bd86416177daad6ae2271`（`72408`）、`probe_WG9370_adj4mut.py` `396bdcf6368be58119e812ba2885d6c3ab56bde7`（`19733`）；`probe_WG9385_k974.py` 施前⛔ 存 |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K25`／`E28`／`P38` | 塊 `K25` `14875` B·`sha256` `c59cedd22abee5a8a44f3844772010807b20120c5b54d19867bcaff0f4f1fb68`·`120` 列；塊 `E28` `2050` B·`sha256` `a10594d9f595844607cb1c49e9481a67f97491145863862f5664adb85142dbba`·`13` 列；塊 `P38` `4601` B·`sha256` `4ab9a278cb3225ea2e87dcbf1bc99648eb27c7d82fca71902b202e59fdf05050`·`27` 列（皆圍欄內全文·末附換行·首列為空列；`P38` 之 payload 內 `⬜` 之子字串框 `11`·列框 `9`〔塊之自載〕）；附於 `K-6` 典（`801055` B）、自誤簿（`1196778` B）、`CLAUDE.md`（`408690` B）之末，期末 ＝ `815930`／`1198828`／`413291` B |
| `5` | 寫出後之 blob | 工項一之 `4` 器（`verify/probes/`·B）：`probe_WG9363_k953.py` ＝ `ccdb11f3a0573c23c91a84e8b35b9735716058cc`（`127230`）、`probe_WG9367_adj4.py` ＝ `d76cf9fecab476ece3e3008c5c9727935b62214e`（`73058`）、`probe_WG9370_adj4mut.py` ＝ `b1ad31f5983ee0ef9373d4d60e6a23a01287cb47`（`20360`）、`probe_WG9385_k974.py` ＝ `c21b66763a9f1ce549efdd957433013abd760511`（`34459`·新）；工項三之三簿：`K-6` 典 ＝ `f06fe785b133fffefbfcb66c687cbcd734ddb60b`（`815930` B）、自誤簿 ＝ `a7bc25b02002c7b2b600d8c3311239b9d230afd5`（`1198828` B）、`CLAUDE.md` ＝ `6a2ff2ce9d296903f8e19ba8d194c642556f6639`（`413291` B）。🔒 `app.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-384 §五-1` 項 `7`） |
| `8` | 量測器之二態（發單側窗八十七實跑·倉外） | **工項一之端**（`158f7fe` ＋ 塊 `Fy35`）：見 `§一` 項 `3`（其 `3` 呼叫之末列 ＝ 前置 `1`；他 `10` 呼叫 ＝ `⇒ 紅 []；rc 0`·`F25 mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`·`F27 mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`）。**施後**（原型）：`55` 呼叫皆 `rc 0`，末列逐字皆 `⇒ 紅 []；rc 0`，唯：`probe_WG9373_k966.py mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`probe_WG9370_adj4mut.py mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`；`probe_WG9345_screen.py wiring` ＝ `⇒ rc 0（不符 0·器紅 0）`；`probe_WG9344_k6s3.py selftest` ＝ `selftest 9/9 ⇒ ✅`；`probe_WG9344p1_pooltemp.py selftest` ＝ `selftest 13/13 ⇒ ✅`；`probe_WG9341_synth.py` ＝ `ε ＝ 0.0002｜rc 0`；`probe_WG9340_main_synth.py` ＝ `紅項 [] 器紅 0`。`P0`：`F23` `75／75`、`F16` `35／35`、`F29` `74／74`、`F27` `31／31`、`F28` `29／29`、`F24` `28／28`、`F14` `86／86`；`F30 selftest` `K1`〜`K16` ✅、`F30 wiring` `W1`〜`W7` ✅、`F30 run` `R1`〜`R6` ✅。諸呼叫（含 `k6s3 run`／`F8 run`／`parity` 之二態十二呼叫）之 `stderr` 合計 `0` B；`55` 呼叫之耗時之和 ≈ `7638` s（本機 `2` 核·並行 `2`）。🔒 本表之施後：`F30` 之三呼叫與 `F23 wiring`／`F24 wiring`（其 `W8`／`W7` 掃 `F30` 之字面）以定稿之器重跑（`F30` 之自 `R0` 之補與 `selftest` 之突變之移出之後）；他器於其間⛔ 改 |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗八十七實跑（態 `158f7fe`）：🔴 機械 `0` 項／🟡 提示 `3` 項——`P-4` `:124`（`§三-1` 之表頭·其箭頭係序〔逐列 → 逐欄、`p1 → p2`、`front → left → right`〕之述 ⇒ **具名豁免**）、`:216`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 改前至改後〔閘 `4`〕⇒ **具名豁免**）、`:348`（塊 `Fy35` 之碼·逐字之塊 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `22986`–`30706`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單側·本機 Linux·⛔ `push`） | `git worktree add --detach <S> 158f7fe`（拋棄式）＋ 本單之定稿（`1095` 列·其四塊即附錄甲〜丁）＋ 原型之 `app.py`（代工項二）＋ 報告之替身·五 `commit`（工項零之首列 ＝ 所令逐字；工項一〜四以模擬之首列代之·其後空一列附尾列）：工項零之 blob ＝ 來源；四塊之抽取 ＝ 項 `2`／`4`；`git apply --check` `rc 0`；`4` 器之施後 blob ＝ 項 `5`；工項二 ＝ `app.py` `345`／`3`；三簿之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx`／`gen_fa_index` ＝ 期·逐位同；閘 `1` ＝ 工項零 `1095`／`0`、工項一 ＝ 該閘之期、工項二 ＝ 上開、工項三 ＝ 該閘之期、工項四（替身）二檔各 `1`／`0`；閘 `2` ＝ 生產碼相異 `1`、`verify/` 相異 `4`（`M` `3`·`A` `1`）·新檔四之 `git check-ignore -v --no-index` 無命中（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `11` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `6` `rc 0`（判別力 `622 621` ⇒ `rc 7`）；閘 `7` `rc 0`（自誤 `606`／`621`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `76`／`79`·缺號 ＝ 該閘之期）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `4`／`5` 之實跑逐位同（`4` 器 ＝ 項 `5`、`app.py` ＝ 原型） |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丁` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-385-k974`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `Fy35`（`git apply` 之差異·`verify/probes/` 之 `4` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index abe2f7f..ccdb11f 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -92,6 +92,10 @@
            `f3_screen_end_block_merge`→末端塊合併再試、`f3_screen_k953`→手冊先行）與 harness 之三入口（`run_corner_pk_k6b`、
            `run_end_block_merge`、`run_k953`）各恰一處以 `blk5=` 傳 `k6b_screen_callbacks`／`_k6b_callbacks` 之 `'blk5'`；二回呼之
            回傳之 dict 含鍵 `'blk5'`，其值為其巢狀 `blk5`，其內恰一處呼 `k971_blk5`、以 `adj4_depth_of` 取深度；二新函式⛔ 案件字面。
+           🔧 `W-G.9-385`（`K-9-74`／`K-9-79`·⛔ 上列一字不刪）：增 K75（`W-G.9-384` 之唯讀審查之 (丙) 2·覆蓋之補）——手冊先行之
+           輪之道路之片之剩下⛔ 依五級再排（照距離）；P0 隨之 75 項。W6 之受詞去 `main`；W7 之許增 `K974_PARAMS`、`k962_land_marks`、
+           `k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`、`calc_special_burden_total` 與 `main`（其接線與
+           `main`／`calc_special_burden_total` 之唯增列由 F30 之 wiring 量之）。
   run      <repo> [<退縮> …]
            harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 手冊先行之紀錄逐列 ＝ 本器所載；R2 街角第 1 宗之宗 ＝ 旗標 off 之
            實跑（街角定案·`v3` §8）；R3 配地之全部（各宗之街廓·推進側·G）與各街廓之抵費地 ＝ 本器所載（容差 `0.01`）且
@@ -710,6 +714,14 @@ def _cases(ns, sp):
          ("K-9-51", "X1(1)", "a", "Z1(1)", (("Z1(1)", 50.0),), "成"))
     _run(out, "K74 五級之屬性之回呼回非 dict ⇒ 停機",
          lambda: _halt(lambda: _go(W, b5=lambda: [], **K14W), "五級之屬性非 dict"), ("停機", True))
+    # 🆕 `W-G.9-385`（`W-G.9-384` 之唯讀審查之 (丙) 2·覆蓋之補）：手冊先行之輪之道路之片⛔ 依五級再排（`K-9-71`·唯建地）
+    _run(out, "K75 （K-9-71）道路之片 R1(1)（RD）之北半部分併入 X1(2)（BB 容 33.333）後，剩下 16.67 之他街廓之候選 ＝ "
+              "C1(1)（BC·距 0·使用分區 商業區）、Z1(1)（BD·距 10）⇒ 道路之片照距離 ⇒ C1(1)（⛔ 依五級排 Z1(1) 先）",
+         lambda: _rows(_go(W, own_upd={"Z1": "g1"}, rm=("X1(1)", "P1(1)"), drop=(), cap={"BB": 33.333},
+                           b5={"BC": {"使用分區": "商業區"}})),
+         [("手冊", "R1(1)", "b", "C1(1)", (("C1(1)", 50.0),), "成"),
+          ("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 33.33),), "部分成"),
+          ("K-9-51", "R1(1)", "b", "C1(1)", (("C1(1)", 16.67),), "成")])
     return out
 
 
@@ -1497,6 +1509,11 @@ KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG384_APP)
 KEEP_SP = tuple(x for x in KEEP_SP if x not in CHG384_SP)
 APP_ALLOW |= {"k971_key5", "k971_blk5"} | set(CHG384_APP)
 SP_ALLOW |= set(CHG384_SP)
+# 🔧 `W-G.9-385`（`K-9-74`／`K-9-79`）：步驟 H 之尺度（`main`）出 W6 之受詞；W7 之許增四新函式、`K974_PARAMS`、
+#   `calc_special_burden_total` 與之（其接線與二函式之唯增列由 F30 之 wiring 量之）
+CHG385_APP = ("main", "calc_special_burden_total")
+KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG385_APP)
+APP_ALLOW |= {"K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales"} | set(CHG385_APP)
 
 
 def _top_dump(tree):
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index 2992e4f..d76cf9f 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -41,6 +41,9 @@
            二 offsnap 之摘要逐項同（第一趟之紀錄唯出艙·⛔ 入判）。
   🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：wiring 之 W5 之許增 `k971_key5`、`k971_blk5`、`f3_screen_end_block_merge`、
            `run_end_block_merge`；W6 比之前，工作樹之列去其末之「, blk5=…)」（段三之呼叫增 `blk5=`·其接線由 F23 之 W9 量之）。
+  🔧 `W-G.9-385`（`K-9-74`／`K-9-79`·⛔ 上列一字不刪）：wiring 之 W5 之許增 `K974_PARAMS`、`k962_land_marks`、
+           `k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`、`calc_special_burden_total`、`main`（其接線與
+           二函式之唯增列由 F30 之 wiring 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, difflib, io, os, re, subprocess, sys, warnings
@@ -763,6 +766,8 @@ W6_REPL = {"k953_manual_run": (
 ALLOW375_APP += ("k971_key5", "k971_blk5", "f3_screen_end_block_merge")
 ALLOW375_SP += ("run_end_block_merge",)
 B5_KW384 = re.compile(r", blk5=[^,()]+\)$")
+# 🔧 `W-G.9-385`（`K-9-74`／`K-9-79`）：W5 之許增四新函式、`K974_PARAMS` 與步驟 H 之尺度所改之二函式（其接線由 F30 之 wiring 量之）
+ALLOW375_APP += ("K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales", "calc_special_burden_total", "main")
 
 
 def _git_show(repo, rev, rel):
diff --git a/verify/probes/probe_WG9370_adj4mut.py b/verify/probes/probe_WG9370_adj4mut.py
index 396bdcf..b1ad31f 100644
--- a/verify/probes/probe_WG9370_adj4mut.py
+++ b/verify/probes/probe_WG9370_adj4mut.py
@@ -28,6 +28,9 @@
            `k6b_stage3_pool_temp`）之段；X5 之 `R-10′` 之模板改為新施點之文（「於第一趟併入街廓 {_bk} 之前」）。
   🔧 `W-G.9-384`（`K-9-71`·⛔ 上列一字不刪）：`wiring` 之 X2 之許增 `k971_key5`、`k971_blk5`、`f3_screen_end_block_merge`、
            `f3_screen_k6b_stage3`；X4 之差另除 `run_end_block_merge`、`run_corner_pk_k6b` 之段（傳 `blk5`）。
+  🔧 `W-G.9-385`（`K-9-74`／`K-9-79`·⛔ 上列一字不刪）：`wiring` 之 X2 之許增 `K974_PARAMS`、`k962_land_marks`、
+           `k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`、`calc_special_burden_total`、`main`（其接線由 F30 之
+           wiring 量之）。
 rc：0 相符／1 不符／2 用法錯。
 """
 import ast, contextlib, difflib, io, json, os, re, subprocess, sys, tempfile, textwrap
@@ -103,6 +106,8 @@ ALLOW373_APP += ("k965_part_split",)
 #   （本單之行為與接線由 F23 之 K61〜K68、W9 與 F16 之 K23〜K29 量之）
 ALLOW373_APP += ("k971_key5", "k971_blk5", "f3_screen_end_block_merge", "f3_screen_k6b_stage3")
 ALLOW373_SP += ("run_end_block_merge", "run_corner_pk_k6b")
+# 🔧 `W-G.9-385`（`K-9-74`／`K-9-79`）：X2 之許增四新函式、`K974_PARAMS` 與步驟 H 之尺度所改之二函式（其接線由 F30 之 wiring 量之）
+ALLOW373_APP += ("K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales", "calc_special_burden_total", "main")
 
 
 def _strip_fns(src, names):
diff --git a/verify/probes/probe_WG9385_k974.py b/verify/probes/probe_WG9385_k974.py
new file mode 100644
index 0000000..c21b667
--- /dev/null
+++ b/verify/probes/probe_WG9385_k974.py
@@ -0,0 +1,563 @@
+# -*- coding: utf-8 -*-
+"""W-G.9-385 量測器（發單側窗八十七擬·檔 F30·⛔ 由受單側改一字）：`K-9-74`／`K-9-79`（臨街地特別負擔之路寬）
+與 `K-9-62` 之「第33條排除」「抵充地」二欄。
+
+子命令（一律 python verify/probes/probe_WG9385_k974.py <子命令> …）：
+  selftest <repo>
+           合成之例（⛔ 讀本案資料·只 harvest `app.py`·期值皆發單側手算·各例之註）：
+             K1 全寬新闢（正面 15 m ⇒ 3.75；左側 8 m ⇒ 1.0）；K2 未勾新闢·抵充地占道路 40% ⇒ 2.25；
+             K3 公私共有（公有持分 1/2）之抵充地占 40% ⇒ 比例 0.8 ⇒ 3.0；K4 中心線即區界（半寬 7.5 m）
+             ⇒ 未勾／勾皆 1.75、⛔ 警示；K5 另一側之小碎塊平均寬 0.4 m ⇒ 仍為區界 1.75；K6 平均寬 0.6 m
+             ⇒ ⛔ 區界 3.75；K7 一面臨二段（60 m 比例 1·40 m 比例 0.6）⇒ 加權 3.15（`K-9-79` ①）；
+             K8 勾新闢而無道路 BLOCK ⇒ 0 ＋ 警示之字樣（`K-9-79` ②）、未勾 ⇒ 0 ⛔ 警示；K9 垂距 × 2 ＝ 12 m
+             與輸入 15 m 不符 ⇒ 警示之字樣、尺度仍以輸入計 3.75；K10 `JUNCTION` 框內⛔ 計 ⇒ 比例
+             1050／1275 ⇒ 3.0882352941…；K11 道路 BLOCK 無中心線 ⇒ 錯誤之字樣；K12 二欄之讀取與檢核
+             （是／空白／否／他值·公有／私有／公私共有·U_LAND 無之·同一所有權人之重複列〔持分 1/2 二列 ⇒ 1/2〕·註記之地號見於
+             二地段〔他地段者未註記亦然〕）；
+             K13 `JUNCTION` 圖層之讀取；K14 `calc_special_burden_total` 之呼叫端之尺度；K15 取樣之容差
+             （首一取樣點距道路 BLOCK 0.005 m ⇒ 仍計）；K16 無宗地 ⇒ 區界⛔ 判 ＋ 警示。
+           （新碼之突變之判別力：發單側於原型施之〔`W-G.9-385` 規格單 `§一` 項 `6`〕；以受單側之碼之字樣為錨之突變另單補寫。）
+  wiring   <repo> <基準>
+           AST 查接線（其式以 `ast.unparse` 比之）：W1 頂層之新名 ＝ `K974_PARAMS`、`k962_land_marks`、`k974_read_junctions`、
+           `k974_burden_scales`、`k974_screen_scales`，且其內⛔ 案件字面（街廓名、地號）；W2 `main()` 恰一處呼
+           `k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)`、其值賦予 `_k974`；
+           W3 `main()` 含 `road_data` 之三鍵 `front_scale`／`left_side_scale`／`right_side_scale`；
+           W4 `JUNCTION` 存 session 鍵 `f3_cad_junctions`（恰一賦值）；W5 抽出 `main()` 之步驟 H 之該段（自 `_k974` 之賦值之列
+           至既有之 `sb = calc_special_burden_total(road_data, C_for_calc)` 之列）以假 st 實際執行（警示 ⇒ `st.warning`、
+           尺度入列〔唯回傳所有之面〕、錯誤 ⇒ 逐則 `st.error` 後 `st.stop()`）；W6 `verify/` 之生產碼⛔ 呼四新函式（harness 照舊消費快照之負擔尺度）；
+           W7 `main`、`calc_special_burden_total` 對基準唯增列——刪去之列唯步驟 E 之說明與步驟 H 之公式說明之三列
+           （以其 sha256 比之·⛔ 載其字面）；`app.py` 之他頂層節點之相異 ⊆ 四新函式 ∪ `K974_PARAMS`。
+  run      <repo>
+           harness 之圖資與地籍（本案）實跑 `k974_screen_scales`：R1 各面之尺度 ＝ 快照之 `負擔尺度_輸入`
+           （無其線之面⛔ 列）、警示與錯誤皆 `0`；R2 `calc_special_burden_total` 給尺度與否之列逐值同；
+           R3 模擬：資料檔之複本之「重劃區地籍」增「抵充地」欄、`628-34`（公有·位 `RD1`）填「是」、臨 `RD1` 之二面改未勾新闢
+           ⇒ 其尺度 ＝ 外部錨（`RD1` 之 BLOCK 面積與該宗之幾何面積之比）；R4 模擬：私有地填「是」⇒ 填列錯誤；
+           R5 模擬：`JUNCTION` 框疊於 `RD1` 之一端 ⇒ 比例之母體扣除之（外部錨）；R6 二欄之結果依檔之 sha256 存 session
+           （同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）。
+rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
+"""
+import ast, contextlib, io, os, sys
+
+try:
+    sys.stdout.reconfigure(encoding="utf-8")
+except Exception:
+    pass
+
+NEW_FUNCS = ["k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales"]
+NEW_NAMES = ["K974_PARAMS"] + NEW_FUNCS
+TOL = 1e-9
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
+def _read(repo, rel):
+    with open(os.path.join(repo, rel), encoding="utf-8") as f:
+        return f.read()
+
+
+def _rect(x0, y0, x1, y1):
+    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
+
+
+def _piece(no, blk, x0, y0, x1, y1):
+    return {"原地號": no, "所屬街廓": blk, "polygon_coords": _rect(x0, y0, x1, y1)}
+
+
+def _toy(road_y1=15.0, far=True, cl_y=None, extra=(), roads=None, cls=None):
+    """街廓 B1 ＝ x∈[0,100]、y∈[−40,0]；正面線 y＝0（(0,0)→(100,0)）；正面之道路 RA ＝ y∈[0,road_y1]。"""
+    cl_y = road_y1 / 2 if cl_y is None else cl_y
+    build = {"B1": _rect(0, -40, 100, 0)}
+    rd = {"RA": _rect(0, 0, 100, road_y1)} if roads is None else roads
+    cl = {"RA": [(0.0, cl_y), (100.0, cl_y)]} if cls is None else cls
+    fl = {"B1": {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}}
+    pcs = [_piece("1", "B1", 0, -40, 100, 0)]
+    if roads is None:
+        pcs += [_piece("10", "RA", 0, 0, 60, road_y1), _piece("11", "RA", 60, 0, 100, road_y1)]
+    if far:
+        pcs.append(_piece("2", "O1", 0, road_y1, 100, road_y1 + 40))
+    pcs += list(extra)
+    return build, rd, cl, fl, pcs
+
+
+def _call(ns, toy, share, inputs, sides=None, junctions=()):
+    build, rd, cl, fl, pcs = toy
+    return ns["k974_burden_scales"](build, rd, cl, fl, sides or {}, pcs, share, inputs, junctions=junctions)
+
+
+def _close(a, b):
+    return a is not None and b is not None and abs(float(a) - float(b)) <= TOL
+
+
+def _ul(rows):
+    import pandas as pd
+    cols = ["段小段", "地號", "所有權統一編號", "姓名", "公私別", "權利範圍分子", "權利範圍分母"]
+    return pd.DataFrame([dict(zip(cols, r)) for r in rows], columns=cols)
+
+
+def _rz(rows, cols=("第33條排除", "抵充地")):
+    import pandas as pd
+    base = ["鄉鎮市", "地段", "地號"] + list(cols)
+    return pd.DataFrame([dict(zip(base, r)) for r in rows], columns=base)
+
+
+def _cases(ns):
+    """回 [(名, 是否相符, 實得之述)]。期值皆手算（各例之註）。"""
+    out = []
+    W = "B1 正面道路勾選新闢，但未偵測到道路 BLOCK"
+    # K1：正面 15 m 新闢 ⇒ 15／4 ＝ 3.75；左側 8 m 新闢（道路 x∈[−8,0]·中心線 x＝−4）⇒ 8／4 ÷ 2 ＝ 1.0
+    b, rd, cl, fl, pcs = _toy()
+    rd = dict(rd, RL=_rect(-8, -40, 0, 0))
+    cl = dict(cl, RL=[(-4.0, -40.0), (-4.0, 0.0)])
+    pcs = pcs + [_piece("12", "RL", -8, -40, 0, 0), _piece("3", "O2", -48, -40, -8, 0)]
+    sides = {"B1": {"left": {"p1": (0.0, -40.0), "p2": (0.0, 0.0)}}}
+    r = _call(ns, (b, rd, cl, fl, pcs), {}, {"B1": {"front": (15.0, True), "left": (8.0, True)}}, sides)
+    s = r["scales"].get("B1", {})
+    out.append(("K1", _close(s.get("front"), 3.75) and _close(s.get("left"), 1.0) and not r["warnings"] and not r["errors"],
+                f"{s}／{r['warnings']}／{r['errors']}"))
+    # K2：未勾·抵充地（宗地 11 ＝ x∈[60,100]·占 RA 之 40%·公有持分 1）⇒ 比例 0.6 ⇒ 9 m ⇒ 9／4 ＝ 2.25；
+    #     同面勾新闢 ⇒ 比例 1 ⇒ 3.75
+    r = _call(ns, _toy(), {"11": 1.0}, {"B1": {"front": (15.0, False)}})
+    r2 = _call(ns, _toy(), {"11": 1.0}, {"B1": {"front": (15.0, True)}})
+    out.append(("K2", _close(r["scales"]["B1"]["front"], 2.25) and _close(r2["scales"]["B1"]["front"], 3.75),
+                f"{r['scales']}／{r2['scales']}"))
+    # K3：公私共有（公有持分 1/2）⇒ 抵充地 ＝ 600 × 0.5 ＝ 300 ⇒ 比例 0.8 ⇒ 12 m ⇒ 3.0
+    r = _call(ns, _toy(), {"11": 0.5}, {"B1": {"front": (15.0, False)}})
+    out.append(("K3", _close(r["scales"]["B1"]["front"], 3.0), f"{r['scales']}"))
+    # K4：區界在中心線（RA ＝ y∈[0,7.5]·中心線 y＝7.5·另一側無地籍）⇒ 基寬 ＝ 垂距 7.5 ⇒ (7.5−4)／2 ＝ 1.75；
+    #     勾新闢亦然；垂距 × 2 ＝ 15 ＝ 輸入 ⇒ ⛔ 警示
+    t4 = _toy(road_y1=7.5, far=False, cl_y=7.5)
+    r = _call(ns, t4, {}, {"B1": {"front": (15.0, False)}})
+    r2 = _call(ns, t4, {}, {"B1": {"front": (15.0, True)}})
+    out.append(("K4", _close(r["scales"]["B1"]["front"], 1.75) and _close(r2["scales"]["B1"]["front"], 1.75)
+                and not r["warnings"] and not r2["warnings"], f"{r['scales']}／{r2['scales']}／{r['warnings']}"))
+    # K5：另一側之碎塊 y∈[7.5,7.9]（100 × 0.4 ⇒ 平均寬 0.4 ＜ 0.5）⇒ 仍為區界 ⇒ 1.75
+    r = _call(ns, _toy(road_y1=7.5, far=False, cl_y=7.5, extra=[_piece("4", "O1", 0, 7.5, 100, 7.9)]), {},
+              {"B1": {"front": (15.0, True)}})
+    out.append(("K5", _close(r["scales"]["B1"]["front"], 1.75), f"{r['scales']}"))
+    # K6：碎塊 y∈[7.5,8.1]（平均寬 0.6 ≥ 0.5）⇒ ⛔ 區界 ⇒ 基寬 15 ⇒ 3.75
+    r = _call(ns, _toy(road_y1=7.5, far=False, cl_y=7.5, extra=[_piece("4", "O1", 0, 7.5, 100, 8.1)]), {},
+              {"B1": {"front": (15.0, True)}})
+    out.append(("K6", _close(r["scales"]["B1"]["front"], 3.75), f"{r['scales']}"))
+    # K7：一面臨二段：RW ＝ x∈[0,60]（比例 1）、RE ＝ x∈[60,160]（宗地 21 ＝ x∈[120,160] 抵充地 ⇒ 600／1500 ⇒ 比例 0.6）；
+    #     未勾 15 m ⇒ RW 3.75、RE 9 m ⇒ 2.25；臨接 60／40 ⇒ 0.6 × 3.75 ＋ 0.4 × 2.25 ＝ 3.15
+    roads7 = {"RW": _rect(0, 0, 60, 15), "RE": _rect(60, 0, 160, 15)}
+    cls7 = {"RW": [(0.0, 7.5), (60.0, 7.5)], "RE": [(60.0, 7.5), (160.0, 7.5)]}
+    t7 = _toy(roads=roads7, cls=cls7, extra=[_piece("20", "RW", 0, 0, 60, 15), _piece("22", "RE", 60, 0, 120, 15),
+                                             _piece("21", "RE", 120, 0, 160, 15), _piece("5", "O3", 100, 15, 160, 55)])
+    r = _call(ns, t7, {"21": 1.0}, {"B1": {"front": (15.0, False)}})
+    rows7 = sorted((d["道路"], d["臨接比"]) for d in r["detail"])
+    out.append(("K7", _close(r["scales"]["B1"]["front"], 0.6 * 3.75 + 0.4 * 2.25) and rows7 == [("RE", 0.4), ("RW", 0.6)],
+                f"{r['scales']}／{rows7}"))
+    # K8：無道路 BLOCK：勾新闢 ⇒ 0 ＋ 警示（字樣逐字）；未勾 ⇒ 0、⛔ 警示
+    t8 = _toy(roads={}, cls={})
+    r = _call(ns, t8, {}, {"B1": {"front": (12.0, True)}})
+    r2 = _call(ns, t8, {}, {"B1": {"front": (12.0, False)}})
+    out.append(("K8", r["scales"]["B1"]["front"] == 0.0 and r["warnings"] == [W] and not r["errors"]
+                and r2["scales"]["B1"]["front"] == 0.0 and r2["warnings"] == [],
+                f"{r['scales']}／{r['warnings']}／{r2['warnings']}"))
+    # K9：道路寬 12（中心線 y＝6）而輸入 15 ⇒ 警示（字樣逐字）；尺度以輸入 15 ⇒ 3.75
+    r = _call(ns, _toy(road_y1=12.0), {}, {"B1": {"front": (15.0, True)}})
+    w9 = "B1 正面：中心線垂距 × 2 ＝ 12.00 m，與輸入路寬 15.00 m 相差逾 0.5 m，請確認"
+    out.append(("K9", _close(r["scales"]["B1"]["front"], 3.75) and r["warnings"] == [w9] and not r["errors"],
+                f"{r['scales']}／{r['warnings']}"))
+    # K10：JUNCTION 框 x∈[85,100]（225 ㎡）⛔ 計；抵充地 ＝ 宗地 13 ＝ x∈[70,100]（450 ㎡·其 225 在框內）
+    #      ⇒ 母體 1275、抵充地 225 ⇒ 比例 1050／1275 ⇒ 15 × 0.82352941… ＝ 12.3529… ⇒ ÷4 ＝ 3.0882352941…
+    t10 = _toy(roads={"RA": _rect(0, 0, 100, 15)}, cls={"RA": [(0.0, 7.5), (100.0, 7.5)]},
+               extra=[_piece("10", "RA", 0, 0, 70, 15), _piece("13", "RA", 70, 0, 100, 15)])
+    r = _call(ns, t10, {"13": 1.0}, {"B1": {"front": (15.0, False)}}, junctions=[_rect(85, 0, 100, 15)])
+    r0 = _call(ns, t10, {"13": 1.0}, {"B1": {"front": (15.0, False)}})
+    out.append(("K10", _close(r["scales"]["B1"]["front"], 15 * (1050 / 1275) / 4)
+                and _close(r0["scales"]["B1"]["front"], 15 * 0.7 / 4), f"{r['scales']}／{r0['scales']}"))
+    # K11：道路 BLOCK 無中心線 ⇒ 錯誤（字樣逐字）
+    r = _call(ns, _toy(cls={}), {}, {"B1": {"front": (15.0, True)}})
+    out.append(("K11", r["errors"] == ["道路 BLOCK RA 未繪 CENTERLINE（B1 正面臨之），請補畫"], f"{r['errors']}"))
+    # K12：二欄之讀取與檢核
+    ul = _ul([("0001甲段", 1000001, "A1", "某縣", "公", 1, 1),
+              ("0001甲段", 1000002, "P1", "王某", "私", 1, 1),
+              ("0001甲段", 1000003, "A1", "某縣", "公", 1, 2), ("0001甲段", 1000003, "P2", "李某", "私", 1, 2),
+              ("0001甲段", 1000004, "A1", "某縣", "公", 1, 2), ("0001甲段", 1000004, "A1", "某縣", "公", 1, 2),
+              ("0002乙段", 1000001, "A2", "某鄉", "公", 1, 1)])
+    mk = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1", None, "是"), ("某市", "甲段", "100-3", "", "是"),
+                                    ("某市", "甲段", "100-4", "否", " 是 ")]), ul)
+    ok_a = mk["抵充地"] == {"100-1": 1.0, "100-3": 0.5, "100-4": 0.5} and mk["第33條排除"] == {} and mk["errors"] == []
+    mk2 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-2", "是", "是"), ("某市", "甲段", "100-1", "Y", ""),
+                                     ("某市", "甲段", "100-9", "", "是")]), ul)
+    e2 = ["填列錯誤：甲段 100-2「第33條排除」欄填「是」，但該地號非公有地（U_LAND 公私別）",
+          "填列錯誤：甲段 100-2「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）",
+          "填列錯誤：甲段 100-1「第33條排除」欄填「Y」，僅得填「是」或空白",
+          "填列錯誤：甲段 100-9「抵充地」欄填「是」，但 U_LAND 無對應資料"]
+    mk3 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1", "", "是"), ("某市", "乙段", "100-1", "", "")]), ul)
+    e3 = ["填列錯誤：地號 100-1 於 甲段、乙段 皆有，「抵充地」無從對應宗地"]
+    mk4 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1")], cols=()), ul)
+    out.append(("K12", ok_a and mk2["errors"] == e2 and mk2["抵充地"] == {} and mk3["errors"] == e3 and mk3["抵充地"] == {}
+                and mk4 == {"抵充地": {}, "第33條排除": {}, "errors": []},
+                f"{mk}／{mk2['errors']}／{mk3['errors']}／{mk4}"))
+    # K13：JUNCTION 圖層（四點之多節線一；二點者、他圖層者⛔ 取）
+    import ezdxf
+    doc = ezdxf.new()
+    msp = doc.modelspace()
+    msp.add_lwpolyline(_rect(0, 0, 10, 10), close=True, dxfattribs={"layer": "JUNCTION"})
+    msp.add_lwpolyline([(0, 0), (5, 5)], dxfattribs={"layer": "junction"})
+    msp.add_lwpolyline(_rect(20, 0, 30, 10), close=True, dxfattribs={"layer": "BLOCK"})
+    jr = ns["k974_read_junctions"](doc)
+    out.append(("K13", jr == [[(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]], f"{jr}"))
+    # K14：calc_special_burden_total：給 front_scale 者用之（⛔ 依新闢）；未給者照舊
+    row = {"label": "B1", "front_width": 15.0, "front_length": 100.0, "front_new": False,
+           "left_side_width": 8.0, "left_side_length": 40.0, "left_side_new": True}
+    a = ns["calc_special_burden_total"]([dict(row, front_scale=2.25)], 0.0)["rows"][0]
+    b0 = ns["calc_special_burden_total"]([row], 0.0)["rows"][0]
+    c = ns["calc_special_burden_total"]([dict(row, left_side_scale=0.0)], 0.0)["rows"][0]
+    out.append(("K14", a["正街尺度"] == 2.25 and a["左側尺度"] == 1.0 and b0["正街尺度"] == 0.0 and b0["左側尺度"] == 1.0
+                and c["左側尺度"] == 0.0, f"{a['正街尺度']}／{b0['正街尺度']}／{c['左側尺度']}"))
+    # K15：取樣點之容差：道路 BLOCK 之一端退縮 0.13 m（x∈[0.13,100]）⇒ 首一取樣點（x＝0.125）距之 0.005 ⇒ 仍計 ⇒ 3.75
+    t15 = _toy(roads={"RA": _rect(0.13, 0, 100, 15)}, cls={"RA": [(0.0, 7.5), (100.0, 7.5)]},
+               extra=[_piece("10", "RA", 0.13, 0, 100, 15)])
+    r = _call(ns, t15, {}, {"B1": {"front": (15.0, True)}})
+    out.append(("K15", r["scales"]["B1"]["front"] == 3.75, f"{r['scales']}"))
+    # K16：無宗地（pieces 空）⇒ 中心線之區界⛔ 判 ⇒ 基寬 ＝ 輸入 15 ⇒ 3.75 ＋ 警示一則（字樣逐字）
+    b16, rd16, cl16, fl16, _ = _toy()
+    r = ns["k974_burden_scales"](b16, rd16, cl16, fl16, {}, [], {}, {"B1": {"front": (15.0, True)}})
+    out.append(("K16", r["scales"]["B1"]["front"] == 3.75
+                and r["warnings"] == ["尚無宗地資料（地籍），中心線是否為重劃區界⛔ 判（以輸入之路寬計）"],
+                f"{r['scales']}／{r['warnings']}"))
+    return out
+
+
+def selftest(repo):
+    ns, _ = _harvest(repo)
+    miss = [n for n in NEW_NAMES if n not in ns]
+    if miss:
+        print(f"  ❌ 新名缺 {miss}")
+        print(f"⇒ 紅 ['K0']；rc 1")
+        return 1
+    red = []
+    for nm, ok, got in _cases(ns):
+        print(f"  {'✅' if ok else '❌'} {nm}：{got}")
+        if not ok:
+            red.append(nm)
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+CASE_LIT = ("R1", "R2", "R3", "R4", "R5", "R6", "RD1", "RD2", "RD3", "RD4", "628-", "G1", "UC9898", "德安")
+
+
+def _mainfn(tree):
+    for node in tree.body:
+        if isinstance(node, ast.FunctionDef) and node.name == "main":
+            return node
+    return None
+
+
+def _step_h_snippet(src):
+    a = src.index("        _k974 = k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)\n")
+    end_s = "        sb = calc_special_burden_total(road_data, C_for_calc)\n"
+    b = src.index(end_s, a) + len(end_s)
+    return src[a:b]
+
+
+class _Stop(Exception):
+    pass
+
+
+class _FakeSt:
+    def __init__(self, ss):
+        self.session_state = ss
+        self.msgs = []
+
+    def warning(self, m):
+        self.msgs.append(("warning", m))
+
+    def error(self, m):
+        self.msgs.append(("error", m))
+
+    def stop(self):
+        raise _Stop()
+
+
+def _run_snippet(snip, scales, warnings, errors):
+    import textwrap
+    st = _FakeSt({"ROADK": {"b1": {"front_width": 15.0, "front_new": False}}})
+    called = []
+
+    def _k(ss, bb, tp, key):
+        called.append((ss is st.session_state, [b["label"] for b in bb], tp, key))
+        return {"scales": scales, "detail": [], "warnings": list(warnings), "errors": list(errors)}
+
+    g = {"st": st, "k974_screen_scales": _k, "build_blocks": [{"id": "b1", "label": "B1"}], "temp_parcels": ["TP"],
+         "SS_ROAD": "ROADK", "C_for_calc": 0.0,
+         "calc_special_burden_total": lambda rd, c: {"rows": rd}}
+    stopped = False
+    try:
+        exec(compile(textwrap.dedent(snip), "<snip>", "exec"), g)
+    except _Stop:
+        stopped = True
+    return called, st.msgs, stopped, g.get("road_data"), g.get("sb")
+
+
+def wiring(repo, base):
+    src = _read(repo, "app.py")
+    tree = ast.parse(src)
+    res = []
+    top = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
+    assigns = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
+    lits = []
+    for nm in NEW_FUNCS:
+        if nm in top:
+            for x in ast.walk(top[nm]):
+                if isinstance(x, ast.Constant) and isinstance(x.value, str) and any(c in x.value for c in CASE_LIT):
+                    lits.append((nm, x.value[:40]))
+    ok1 = all(n in top for n in NEW_FUNCS) and "K974_PARAMS" in assigns and not lits
+    res.append(("W1 頂層之新名與⛔ 案件字面", ok1, f"{[n in top for n in NEW_FUNCS]}／K974_PARAMS {'K974_PARAMS' in assigns}／字面 {lits}"))
+    mn = _mainfn(tree)
+    calls = [x for x in ast.walk(mn) if isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
+             and x.func.id == "k974_screen_scales"] if mn else []
+    want = "k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)"
+    ok2 = len(calls) == 1 and ast.unparse(calls[0]) == want
+    seg = ast.get_source_segment(src, mn) if mn else ""
+    asg = [x for x in ast.walk(mn) if isinstance(x, ast.Assign) and isinstance(x.value, ast.Call)
+           and isinstance(x.value.func, ast.Name) and x.value.func.id == "k974_screen_scales"] if mn else []
+    ok2 = ok2 and len(asg) == 1 and ast.unparse(asg[0].targets[0]) == "_k974"
+    res.append(("W2 main() 恰一處呼之", ok2, f"{[ast.unparse(c) for c in calls]}"))
+    kst = {x.value for x in ast.walk(mn) if isinstance(x, ast.Constant) and isinstance(x.value, str)} if mn else set()
+    ok3 = {"front_scale", "left_side_scale", "right_side_scale"} <= kst
+    res.append(("W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）", ok3, ""))
+    ok4 = sum(1 for x in ast.walk(mn) if isinstance(x, ast.Assign) and ast.unparse(x) ==
+              "st.session_state['f3_cad_junctions'] = k974_read_junctions(_doc_cad_p7)") == 1 if mn else False
+    res.append(("W4 JUNCTION 存 session", ok4, ""))
+    try:
+        snip = _step_h_snippet(src)
+        c1, m1, s1, rd1, _ = _run_snippet(snip, {"B1": {"front": 2.25, "left": 0.5}}, ["警示甲"], [])
+        c2, m2, s2, rd2, sb2 = _run_snippet(snip, {}, [], ["錯甲", "錯乙"])
+        ok5 = (c1 == [(True, ["B1"], ["TP"], "ROADK")] and m1 == [("warning", "⚠️ 警示甲")] and not s1
+               and rd1 and rd1[0].get("front_scale") == 2.25 and rd1[0].get("left_side_scale") == 0.5
+               and "right_side_scale" not in rd1[0] and rd1[0]["front_width"] == 15.0
+               and s2 and m2 == [("error", "⛔ 錯甲"), ("error", "⛔ 錯乙")] and rd2 is None and sb2 is None)
+        res.append(("W5 步驟 H 之段以假 st 實跑", ok5, f"{rd1}／{m1}／{m2}／停 {s1}/{s2}"))
+    except Exception as e:
+        res.append(("W5 步驟 H 之段以假 st 實跑", False, f"{type(e).__name__}: {e}"))
+    others = []
+    vdir = os.path.join(repo, "verify")
+    for fn in sorted(os.listdir(vdir)):
+        if fn.endswith(".py"):
+            t = _read(repo, os.path.join("verify", fn))
+            if any(n in t for n in NEW_NAMES):
+                others.append(fn)
+    res.append(("W6 verify/ 之生產碼⛔ 呼之", others == [], f"{others}"))
+    try:
+        import subprocess
+        bsrc = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True, check=True).stdout.decode("utf-8")
+        btree = ast.parse(bsrc)
+        btop = {}
+        for n in btree.body:
+            k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
+                n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) else None)
+            if k:
+                btop[k] = ast.get_source_segment(bsrc, n)
+        ctop = {}
+        for n in tree.body:
+            k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
+                n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) else None)
+            if k:
+                ctop[k] = ast.get_source_segment(src, n)
+        dif = sorted(k for k in set(btop) | set(ctop) if btop.get(k) != ctop.get(k))
+        import difflib, hashlib
+        dels = []
+        for k in ("main", "calc_special_burden_total"):
+            for ln in difflib.ndiff((btop.get(k) or "").split("\n"), (ctop.get(k) or "").split("\n")):
+                if ln.startswith("- "):
+                    dels.append((k, hashlib.sha256(ln[2:].encode("utf-8")).hexdigest()))
+        ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"}
+               and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
+        res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
+    except Exception as e:
+        res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", False, f"{type(e).__name__}: {e}"))
+    red = []
+    for nm, ok, got in res:
+        print(f"  {'✅' if ok else '❌'} {nm}：{got}")
+        if not ok:
+            red.append(nm.split()[0])
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+# 基準之 `main` 之三列（步驟 E 之說明「……不計道路截角。僅新闢……」與步驟 H 之公式說明之正面、側面之二列）之 sha256
+REPL385 = ("0bc0330faf15a1f5543f5c9b9147da2ec7b73d04d15dbf03c0857ae07605345e",
+           "7dbfbc005f4c147f0de70d370597bf7de038fc5bf22adb8dd145bdf3cef87db5",
+           "217d50a6c215b275aa66e89ea33b87d0ad51bde2e3e7a4d75bf8202b5051e13e")
+
+
+def _case(repo):
+    os.environ["WV_K6_STEP0"] = os.environ.get("WV_K6_STEP0", "") or "off"
+    sys.path.insert(0, os.path.join(repo, "verify"))
+    from app_harvest import harvest
+    import run_verification as rv
+    with contextlib.redirect_stdout(io.StringIO()):
+        ns, fake_st = harvest(os.path.join(repo, "app.py"))
+        snap = rv.load_snapshot()
+        cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
+        v6 = open(rv.V6DXF, "rb").read()
+        tp, _, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snap)
+    return ns, snap, cb_by, cad, tp, rv.ANON_XLSX
+
+
+def _ss(cb_by, cad, snap, xbytes, junctions=(), unchecked=()):
+    road = {}
+    blds = []
+    for lb, b in cb_by.items():
+        if b.get("burden_type") != "可建築土地":
+            continue
+        blds.append(b)
+        bs = snap["blocks"][lb]
+
+        def _w(k):
+            v = bs[k]["路寬_m"]
+            return float(v) if isinstance(v, (int, float)) else 0.0
+        road[b["id"]] = {"front_width": _w("正面"), "front_new": float(bs["正面"]["負擔尺度_輸入"]) > 0 and (lb, "front") not in unchecked,
+                         "left_side_width": _w("左側"), "left_side_new": float(bs["左側"]["負擔尺度_輸入"]) > 0 and (lb, "left") not in unchecked,
+                         "right_side_width": _w("右側"), "right_side_new": float(bs["右側"]["負擔尺度_輸入"]) > 0 and (lb, "right") not in unchecked}
+    ss = {"f3_classified_blocks": list(cb_by.values()), "f3_manual_road_centerlines": cad["centerlines"],
+          "f3_cad_front_lines": cad["front_lines"], "f3_cad_side_lines_by_side": cad["side_lines_by_side"],
+          "f3_cad_junctions": list(junctions), "f7_saved": ("x.xlsx", xbytes), "ROADK": road}
+    return ss, blds
+
+
+def _xlsx_with(path, marks):
+    """資料檔之複本（記憶體）：「重劃區地籍」增「第33條排除」「抵充地」二欄，依 marks ＝ {(欄, 地號): 值} 填之。"""
+    import pandas as pd
+    xl = pd.ExcelFile(path, engine="openpyxl")
+    ul = pd.read_excel(xl, "U_LAND", header=0, engine="openpyxl")
+    rz = pd.read_excel(xl, "重劃區地籍", header=0, engine="openpyxl")
+    for col in ("第33條排除", "抵充地"):
+        rz[col] = [marks.get((col, str(n).strip()), None) for n in rz["地號"]]
+    bio = io.BytesIO()
+    with pd.ExcelWriter(bio, engine="openpyxl") as w:
+        ul.to_excel(w, sheet_name="U_LAND", index=False)
+        rz.to_excel(w, sheet_name="重劃區地籍", index=False)
+    return bio.getvalue()
+
+
+def run(repo):
+    ns, snap, cb_by, cad, tp, xpath = _case(repo)
+    miss = [n for n in NEW_NAMES if n not in ns]
+    if miss:
+        print(f"  ❌ 新名缺 {miss}")
+        print("⇒ 紅 ['R0']；rc 1")
+        return 1
+    xb = open(xpath, "rb").read()
+    res = []
+    ss, blds = _ss(cb_by, cad, snap, xb)
+    r = ns["k974_screen_scales"](ss, blds, tp, "ROADK")
+    bad = []
+    for b in blds:
+        lb = b["label"]
+        for sd, k in (("front", "正面"), ("left", "左側"), ("right", "右側")):
+            exp = float(snap["blocks"][lb][k]["負擔尺度_輸入"])
+            got = r["scales"].get(lb, {}).get(sd)
+            has_line = (sd == "front" and lb in cad["front_lines"]) or (sd != "front" and sd in (cad["side_lines_by_side"].get(lb) or {}))
+            if (got is None) == has_line or (got is not None and got != exp):
+                bad.append((lb, sd, exp, got))
+    print("  各面之尺度：" + "；".join(f"{b['label']} " + "／".join(f"{sd} {r['scales'].get(b['label'], {}).get(sd)}"
+                                                                    for sd in ("front", "left", "right")) for b in blds))
+    res.append(("R1 尺度 ＝ 快照之負擔尺度_輸入", not bad and not r["warnings"] and not r["errors"],
+                f"不符 {bad}／警示 {r['warnings']}／錯誤 {r['errors']}"))
+    rd = []
+    for b in blds:
+        x = ss["ROADK"][b["id"]]
+        rd.append({"label": b["label"], "front_width": x["front_width"], "front_length": cad["front_lengths"].get(b["label"], 0.0),
+                   "front_new": x["front_new"], "left_side_width": x["left_side_width"], "left_side_length": 10.0,
+                   "left_side_new": x["left_side_new"], "right_side_width": x["right_side_width"], "right_side_length": 10.0,
+                   "right_side_new": x["right_side_new"]})
+    rd2 = []
+    for row in rd:
+        s = r["scales"].get(row["label"], {})
+        row2 = dict(row)
+        for sd, ky in (("front", "front_scale"), ("left", "left_side_scale"), ("right", "right_side_scale")):
+            if sd in s:
+                row2[ky] = s[sd]
+        rd2.append(row2)
+    a = ns["calc_special_burden_total"](rd, 0.1)
+    b2 = ns["calc_special_burden_total"](rd2, 0.1)
+    res.append(("R2 calc 之列給尺度與否逐值同", a == b2, f"{a['special_total']}／{b2['special_total']}"))
+    # R3：628-34（公有·RD1 內）填「是」；臨 RD1 之二面（R1 左側、R2 正面）改未勾新闢
+    #     外部錨：RD1 之 BLOCK 面積（area_m2）、628-34 於 RD1 之片之幾何面積（幾何面積_m2）⇒ 比例 ⇒ 8 × 比例 ⇒ 尺度表
+    rd1 = float(cb_by["RD1"]["area_m2"])
+    a34 = sum(float(t["幾何面積_m2"]) for t in tp if t["所屬街廓"] == "RD1" and str(t["原地號"]) == "628-34")
+    ratio = (rd1 - a34) / rd1
+    bw = 8.0 * ratio
+    fsc = ns["calc_frontage_burden_scale"](bw)
+    ss3, _ = _ss(cb_by, cad, snap, _xlsx_with(xpath, {("抵充地", "628-34"): "是"}),
+                 unchecked={("R1", "left"), ("R2", "front")})
+    r3 = ns["k974_screen_scales"](ss3, blds, tp, "ROADK")
+    g1, g2 = r3["scales"]["R1"]["left"], r3["scales"]["R2"]["front"]
+    others_same = all(r3["scales"][lb][sd] == r["scales"][lb][sd] for lb in r["scales"] for sd in r["scales"][lb]
+                      if (lb, sd) not in (("R1", "left"), ("R2", "front")))
+    # 容差 1e-4：外部錨之「幾何面積_m2」捨入至 0.01 ㎡（⇒ 比例之差 ≤ 0.005／RD1 ≈ 5e-6 ⇒ 尺度之差 ≤ 2e-5）
+    ok3 = (abs(g2 - fsc) <= 1e-4 and abs(g1 - fsc / 2) <= 1e-4 and 0 < a34 < rd1 and others_same
+           and not r3["errors"] and not r3["warnings"])
+    res.append(("R3 抵充地之模擬（628-34·RD1）", ok3,
+                f"RD1 {rd1:.4f}／628-34 之片 {a34:.4f}／比例 {ratio:.6f}／負擔路寬 {bw:.4f}／期 {fsc:.6f}、{fsc / 2:.6f}"
+                f"／得 {g2:.6f}、{g1:.6f}"))
+    # R4：私有地填「是」⇒ 填列錯誤（628-37 ＝ 私有·RD1 內）；第33條排除填於公有地（628-34）⇒ 無錯
+    ss4, _ = _ss(cb_by, cad, snap, _xlsx_with(xpath, {("抵充地", "628-37"): "是", ("第33條排除", "628-34"): "是"}))
+    r4 = ns["k974_screen_scales"](ss4, blds, tp, "ROADK")
+    e4 = ["填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）"]
+    res.append(("R4 私有地填「是」⇒ 填列錯誤", r4["errors"] == e4, f"{r4['errors']}"))
+    # R6：二欄之結果依檔之 sha256 存 session（同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）
+    import hashlib
+    h4 = hashlib.sha256(ss4["f7_saved"][1]).hexdigest()
+    r6a = ns["k974_screen_scales"](ss4, blds, tp, "ROADK")
+    c6 = ss4.get("f3_k962_marks_cache")
+    ss4["f7_saved"] = ("x.xlsx", xb)
+    r6b = ns["k974_screen_scales"](ss4, blds, tp, "ROADK")
+    ok6 = (r6a["errors"] == e4 and isinstance(c6, tuple) and c6[0] == h4 and r6b["errors"] == []
+           and ss4["f3_k962_marks_cache"][0] == hashlib.sha256(xb).hexdigest())
+    res.append(("R6 二欄之結果之存與換檔", ok6, f"{r6a['errors']}／{r6b['errors']}"))
+    # R5：JUNCTION 框 ＝ RD1 之頂點之外接矩形與 RD1 之一端 10 m 之交（外部錨：框內之 RD1 面積以 shapely 另算）
+    from shapely.geometry import Polygon, box
+    p = Polygon(cb_by["RD1"]["vertices"])
+    x0, y0, x1, y1 = p.bounds
+    jb = box(x0, y0, x0 + 10.0, y1)
+    jpoly = [tuple(c) for c in list(jb.exterior.coords)[:-1]]
+    inj = float(p.intersection(jb).area)
+    a34j = sum(float(Polygon(t["polygon_coords"]).intersection(p.difference(jb)).area) for t in tp
+               if t["所屬街廓"] == "RD1" and str(t["原地號"]) == "628-34")
+    ratio5 = ((float(p.area) - inj) - a34j) / (float(p.area) - inj)
+    ss5, _ = _ss(cb_by, cad, snap, _xlsx_with(xpath, {("抵充地", "628-34"): "是"}), junctions=[jpoly],
+                 unchecked={("R1", "left"), ("R2", "front")})
+    r5 = ns["k974_screen_scales"](ss5, blds, tp, "ROADK")
+    f5 = ns["calc_frontage_burden_scale"](8.0 * ratio5)
+    ok5 = abs(r5["scales"]["R2"]["front"] - f5) <= 1e-6 and inj > 0 and not r5["errors"]
+    res.append(("R5 JUNCTION 之模擬（RD1 之一端）", ok5, f"框內 {inj:.4f}／比例 {ratio5:.6f}／期 {f5:.6f}／得 {r5['scales']['R2']['front']:.6f}"))
+    red = []
+    for nm, ok, got in res:
+        print(f"  {'✅' if ok else '❌'} {nm}：{got}")
+        if not ok:
+            red.append(nm.split()[0])
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def main(argv):
+    if not ((len(argv) == 3 and argv[1] in ("selftest", "run")) or (len(argv) == 4 and argv[1] == "wiring")):
+        print(__doc__)
+        return 2
+    try:
+        if argv[1] == "wiring":
+            return wiring(argv[2], argv[3])
+        return {"selftest": selftest, "run": run}[argv[1]](argv[2])
+    except Exception as e:
+        import traceback
+        traceback.print_exc()
+        print(f"⇒ 無從判定（{type(e).__name__}）；rc 3")
+        return 3
+
+
+if __name__ == "__main__":
+    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `K25`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

---

## 🔧 `W-G.9-384` 之入主線；`K-9-79` 之立（臨街地特別負擔：一面臨二段以上之道路 `BLOCK` 者依臨接長度加權平均·乙；勾新闢而區內未偵測到其道路 `BLOCK` 者以 `0` 計並警示·乙；路口之畫法依 `K-9-59` ⑤；他案之情形以模擬驗之）；`K-9-74`、`K-9-62`（二欄）之落地之【工】之讀法；`W-G.9-384` 之唯讀審查之 (丙) 二、三（`W-G.9-385`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`（`W-G.9-384` 補令一 工項一）之後；本節之碼入新側支 `verify/W-G.9-385-k974`（`W-G.9-385` 工項二）。**授權** ＝ `docs/orders/W-G.9-385_規格單.md` `§二`。

**編號之由**（`W-G.9-385 §零-1`）：`K-9` 之 `MAX` ＝ `78`（開工態 `158f7fe`·`probe_WG9321_issuer_anchor.py` 之「項4′」）；`K-9-79` 於開工態之全倉追蹤檔（`git grep -c -P "(?<![0-9\-])K-9-79(?![0-9])"`·列框）＝ `0` ⇒ 取之。

### 一、`W-G.9-384` 之入主線

- 上開「`W-G.9-383` 之入主線；`K-9-78` 之立……（`W-G.9-384`）」節之三之 `K-9-71` 之「落地狀態」逐字「🔶（新側支 `verify/W-G.9-384-k971`·`W-G.9-384` 工項二·候入主線之請示）」——其碼（CC 依規格單 `§三` 所撰·側支之端 `663a457`）經發單側窗八十七自倉復驗、KL 之畫面核對與放行（**逐字**「核對無誤」·`2026-10-16 11:19`）⇒ `W-G.9-384` 補令一（主線快轉至 `663a457` ＋ 主 checkout 之同步·其工項一 ＝ 報告入倉）⇒ 主線 ＝ `158f7fe`。⇒ `K-9-71`：✅（主線）。

### 二、`K-9-79` 之出處

**發單側所呈**（發單側窗八十七·擬 `W-G.9-385` 之前之請示·對話·`2026-10-16`·附圖 `圖_W-G.9-385_臨街負擔之路段.png`·其二問之受詞·**逐字**·節錄）：

> ### 問一：街廓的一面臨接兩段道路 BLOCK（圖一）
>
> 【現況】
> - 每一個街廓的正面、左側、右側，各只有一個負擔尺度。
> - K-9-74 定的是：比例以「兩路口之間的那一段道路 BLOCK」計。
> - 道路對面有丁字路口時，道路會在路口切成兩段。這時街廓的同一面，會同時臨接兩段比例不同的道路。
> - 本案沒有這種情形：每一面都只臨一段。
>
> 【要改成】以圖一為例：既成道路 15 m，未勾新闢。
> - 街廓甲有 60 m 臨 RD-西（無抵充地，比例 100%，負擔路寬 15 m，尺度 3.75）。
> - 另 40 m 臨 RD-東（抵充地占 40%，比例 60%，負擔路寬 9 m，尺度 2.25）。
> - 路口那一段，以路口中線為界，一半歸西段、一半歸東段。
>
> 兩種算法：
> - **甲 分段計算**：臨西段的宗地用 3.75，臨東段的宗地用 2.25。跨在分界上的宗地，依它在兩段的臨街長度分別計算。正面負擔合計 60×3.75＋40×2.25＝315 ㎡。
> - **乙 整面平均**：整面用同一個尺度，依臨接長度加權平均，315÷100＝3.15，每一宗都用 3.15。合計同樣是 315 ㎡。
>
> 【對土地的影響】
> - 兩種做法的全區負擔總額相同，所以 B 值相同。
> - 差別在各宗地之間的分擔：
>   - 甲：臨抵充地那段的宗地負擔較輕。
>   - 乙：整面平均分攤。
>
> 【要你判斷】採甲或乙？我建議甲：每一宗依它實際臨接的那段道路計算負擔，比較符合臨街地特別負擔的精神。
>
> ### 問二：勾了新闢，區內卻沒有這條路的道路 BLOCK（圖二）
>
> 【現況】
> - 程式只看步驟 E 的勾選：勾了新闢，就照路寬計負擔。
> - 依 K-9-74 第丁點，區內沒有該路的道路 BLOCK 者，負擔為 0。但那一點講的是未勾新闢的情形，例如本案 R1、R4 正面的中原路。
> - 「勾了新闢，但區內找不到它的道路 BLOCK」這種情形，還沒有定。
> - 可能的原因有兩種：
>   - 那條路真的整條在區外，例如由其他計畫開闢；
>   - 使用者漏畫了道路 BLOCK，或畫的位置沒有貼齊側面線。
>
> 【要改成】
> - **甲 停下來列出**：列出這一面，請使用者補畫道路 BLOCK；若那條路確實在區外，就取消勾選新闢，再往下算。
> - **乙 負擔以 0 計，並列出警示**：繼續往下算。
>
> 【對土地的影響】
> - 若是漏畫，採乙會使這一面少算負擔，全區的 B 值與各宗的 G 值跟著偏掉，而且警示容易被略過。
> - 若那條路確實在區外，兩種做法的結果相同，都是 0。
>
> 【要你判斷】採甲或乙？我建議甲。

其通知六則（「兩個新欄的位置」「填錯的處理」「路口」「中心線找不到時」「本案實測」「步驟 E 的畫面」）之要旨見下開三之甲、己、庚、壬。

**KL 之文**（`2026-10-16 12:25`·**逐字**）：

> 1. 問一：乙
> 2. 問二：乙，併顯示警示文字，例如：「R1正面道路勾選新闢，但未臻側道路BLOCK」，"正面"可替換為"右側"或"左側"
> 3. 確認一下，路口道路仍需劃設一個矩形BLOCK，再畫設一個JUNCTION圖層?(即2矩形圖層位置重疊)
> 4. 本測試案雖沒有D 欄新增「第33條排除」、E 欄新增「抵充地」，但你還是要模擬相關情形，以為了未來泛用化的測試

**發單側之答**（發單側窗八十七·對話·`2026-10-16`·附圖 `圖三_路口之畫法.png`·**逐字**·節錄·其第 `1` 點〔問一採乙之覆述〕略）：

> **2. 問二採乙**
> 這種情形負擔以 0 計，並顯示警示文字，例如：「R1 正面道路勾選新闢，但未偵測到道路 BLOCK」。「正面」依實際情形換成「左側」或「右側」。
> 來文寫的是「未臻側道路BLOCK」，我讀為「未偵測到道路 BLOCK」。若原意不是這樣，請告知。
>
> **3. 路口的畫法（見附圖「圖三_路口之畫法.png」）**
> 不需要另外畫一個矩形道路 BLOCK。依 10/05 K-9-59 ⑤ 的規定：
> - **道路 BLOCK 的畫法**：穿越路口的那條道路畫成一個道路 BLOCK，路口範圍包含在裡面；本案的 RD4 就是這樣畫的。接進來的道路 BLOCK，畫到它的邊線為止。每一個道路 BLOCK 只有一條中心線。
> - **JUNCTION 是選用的**：要框出路口時，只在 JUNCTION 圖層畫一個框，疊在那條道路 BLOCK 上。所以會有兩個圖層的位置重疊，但路口本身不是另一個道路 BLOCK。
> - **不另畫矩形的原因**：路口若另外畫成一個道路 BLOCK，它沒有自己的中心線。依 K-9-59，沒有中心線屬於圖資缺漏，程式會停下來，路口片的分配也會跟著改變。
> - **框的作用**：計算抵充地比例時，框內的面積不計入。
>
> 若您要的是另一種畫法（路口另成一個道路 BLOCK），這會改到 K-9-59，請告知，我再另行請示。
>
> **4. 模擬他案的情形**
> 遵示辦理。規格單會要求執行端用本案的複本，加上以下各種情形，逐一驗算。結果要與我事先手算的數值相符：

（其後所列之八種情形從略·其落地 ＝ `W-G.9-385` 規格單 `§三-2` 之 `F30`；下開三之壬。）

### 🔒 `K-9-79`　**臨街地特別負擔之一面之尺度：一面臨接二段以上之道路 `BLOCK` 者，各段依 `K-9-74` 之式求其尺度，整面以臨接長度加權平均為一個尺度（乙）；勾新闢而區內未偵測到其道路 `BLOCK` 者，負擔以 `0` 計並顯示警示（乙）；路口依 `K-9-59` ⑤ 畫之（`JUNCTION` 為疊於道路 `BLOCK` 之選用之框·⛔ 另成道路 `BLOCK`）；本案無之情形以合成之例與本案資料之複本模擬驗之**（KL 裁 `2026-10-16 12:25`·canonical·**逐字**見上開二）

**裁之內容**：
① **一面臨二段以上**（第 `1` 點「問一：乙」）：整面一個負擔尺度 ＝ Σ（各段之臨接長度 × 該段之尺度）÷ 該面之長；臨接之段之外（區外·無道路 `BLOCK`）之長之尺度為 `0`（`K-9-74` 丁）。各宗地皆用其面之此一尺度。
② **勾新闢而無道路 `BLOCK`**（第 `2` 點「問二：乙」）：負擔 `0`；顯示警示「`<街廓> <面>道路勾選新闢，但未偵測到道路 BLOCK`」（`<面>` ＝ 正面／左側／右側）——KL 之例文之「未臻側道路BLOCK」讀為「未偵測到道路 BLOCK」（發單側之答·通知·KL 未駁之前依之）。⛔ 停機。
③ **路口之畫法**（第 `3` 點之確認）：依 `K-9-59` ⑤——穿越路口之道路為一個道路 `BLOCK`（路口包含在內），接入之道路 `BLOCK` 畫至其邊線；`JUNCTION` 為選用之框、疊於該道路 `BLOCK`；路口⛔ 另成道路 `BLOCK`（另成者無其中心線 ⇒ `K-9-59` 之圖資缺漏）。發單側之答已呈；KL 若欲改為「路口另成道路 `BLOCK`」⇒ 改 `K-9-59`·另請示。
④ **模擬**（第 `4` 點）：本案之「重劃區地籍」無二欄、亦無抵充地與區界在中心線之道路；其各形以量測器 `F30` 之合成之例（`selftest`）與本案資料之複本（記憶體·二欄之增·`run`）驗之，期值皆發單側手算或外部錨。

**與既有正典之關係**：`K-9-74` 之【工】之讀法甲（「正街、側街之負擔尺度依之」）之「一面一尺度」沿用，① 補其臨二段以上之受詞；`K-9-74` 丁（區內無其道路 `BLOCK` ⇒ `0`）之受詞擴及勾新闢者（②）；`K-9-59` ⑤ 沿用（③）。

**射程**：及於**任一案件**。

**落地狀態**：🔶（新側支 `verify/W-G.9-385-k974`·`W-G.9-385` 工項二·候入主線之請示）。

### 三、`K-9-74`、`K-9-62`（二欄）之落地之【工】之讀法（`W-G.9-385`·發單側窗八十七·⛔ 充裁·以交付之通知告 KL）

上開 `K-9-74` 之【工】之讀法甲〜己沿用；本節補其落地之形：
- **甲 二欄之讀與檢核**（`K-9-62` 第 `3` 點·通知「兩個新欄的位置」「填錯的處理」）：「重劃區地籍」工作表之「第33條排除」「抵充地」二欄以**欄名**認之（KL 所定之 D、E 欄現為「統編」「所有權人」·位置不拘）；無其欄者視為全空白。格 ＝「是」⇒ 註記；空白或「否」⇒ 未註記；他值 ⇒ 填列錯誤。註記之地號須於 `U_LAND` 有其列且其公有持分（「公私別」＝「公」之所有權人之權利範圍之和·所有權人依統一編號〔無則姓名〕去重）＞ `0`；否則填列錯誤。公私共有者以公有持分計入（`K-9-74` 丙）。宗地以地號認之（同 `t8_ownership_map`·⛔ 分地段）⇒ 註記之地號見於二以上之地段 ⇒ 填列錯誤（無從對應宗地）。有填列錯誤 ⇒ 列出、停止計算（步驟 H）。「第33條排除」本單唯讀取與檢核；其指配（`K-9-62` 之本旨）另單。
- **乙 臨接之道路**：各面之線均分 `400` 段，各段之中點往街廓外偏移 `0.5 m`，落於何道路 `BLOCK` 即該段臨之；不落於任何道路 `BLOCK` 而距某道路 `BLOCK` 不逾 `0.1 m` 者（線之端點與道路 `BLOCK` 之邊界之量化之差·本案 `R1` 右側之首段距 `RD2` `0.005 m`）視為臨其最近者；餘 ⇒ 不臨（區外）。
- **丙 比例**：勾新闢 ⇒ `1`；未勾 ⇒（道路 `BLOCK` 去 `JUNCTION` 框後之面積 − 其內各宗地之片之面積 × 該地號之抵充地之公有持分）÷ 道路 `BLOCK` 去 `JUNCTION` 框後之面積。
- **丁 中心線即區界**：垂距 ＝ 臨接該道路之諸段之平均位置之點至其中心線（最近之一節之直線）之距離；中心線之另一側、寬 ＝ 垂距之帶內之地籍（宗地之片·`_GHOST` 除外）之面積 ÷ 中心線之長 ＜ `0.5 m` ⇒ 區界 ⇒ 基寬 ＝ 垂距；否則基寬 ＝ 輸入之路寬。尚無宗地資料者 ⇒ ⛔ 判（基寬 ＝ 輸入）並警示一則。
- **戊 一面之尺度**（`K-9-79` ①）：Σ（臨接該道路之段數 ÷ `400`）×（正面 ⇒ 正街之尺度表；側面 ⇒ 其半）（基寬 × 比例）。
- **己 警示與錯誤**：警示（⛔ 停機）＝ `K-9-79` ②；垂距 × `2` 與輸入路寬相差逾 `0.5 m`（`K-9-74` 之【工】乙）；尚無宗地資料。錯誤（停止計算）＝ 填列錯誤（甲）；臨接之道路 `BLOCK` 無中心線（`K-9-59`·通知「中心線找不到時」）；道路 `BLOCK` 去路口後之面積為 `0`。
- **庚 畫面**：步驟 H 求各面之尺度（`k974_screen_scales`）而入臨街地特別負擔之計算（`calc_special_burden_total`）；其明細（臨接之道路、臨接比、基寬、比例、區界、垂距 × 2、負擔路寬、尺度）以展開之表示之；步驟 E 之說明改載 `K-9-74`（勾新闢者全寬；未勾者依比例；拓寬既有道路者不勾新闢；區外不計）。`JUNCTION` 圖層於讀 CAD 精準圖層時存之。二欄之讀取之結果依地籍資料來源之檔存之（換檔即重讀）。
- **辛 harness ⛔ 動**：harness 之負擔尺度仍消費快照之 `負擔尺度_輸入`（KL 四條件 ①·`verify/stepg_pipeline.py`）；他案之快照須載步驟 H 依本裁所得之尺度。
- **壬 本案**（發單側窗八十七·主線之端 `158f7fe`·原型·二退縮）：各面之尺度 ＝ 快照之 `負擔尺度_輸入`（正面 `R2`、`R3`、`R5`、`R6` ＝ `2`；臨 `RD1`〜`RD4` 之側 ＝ `1`；`R1`、`R4` 之正面〔中原路·區內無其道路 `BLOCK`〕＝ `0`·未勾 ⇒ ⛔ 警示）；垂距 × `2` ＝ `8.00 m`（`R1` 左側 `7.9998`、`R2` 正面 `7.9997`）＝ 輸入；中心線之另一側之地籍之平均寬 `3.977`〜`4.000 m` ⇒ ⛔ 區界；`RD1`〜`RD4` 皆無抵充地 ⇒ 比例 `1`；`R1` 右側之首段（距 `RD2` `0.005 m`）依乙之容差計入 ⇒ 臨接比 `1`；警示、錯誤皆 `0` ⇒ **本案之配地⛔ 變**。模擬（`F30 run`·資料檔之複本）：`628-34`（公有·於 `RD1` 之片 `131.60 ㎡`）填「抵充地」、臨 `RD1` 之二面改未勾 ⇒ `RD1` 之比例 `0.878403`、負擔路寬 `7.0272 m` ⇒ `R2` 正面 `1.5136`、`R1` 左側 `0.7568`；私有地（`628-37`）填「是」⇒ 填列錯誤。
- **癸 `W-G.9-384` 之唯讀審查之 (丙) 二、三**：(丙) 二（手冊先行之輪之道路之片之再排，`F23` 無判別力）⇒ `F23` `K75`（道路之片之剩下之他街廓之候選二而五級異 ⇒ 照距離；令道路之片亦再排之突變 ⇒ `K75` 紅·發單側於原型實施）；(丙) 三（harness 之 `blk5` 之最小建築面積 ＝ `{}`、畫面取 session 之有效值）⇒ 已知之差（照 `run_adj4`·`K-9-71` 於某案觸發且街廓間最小建築面積相異時畫面與 harness 之序可異）·登記於待落地清單·⛔ 改。

**落地狀態**：`K-9-74`、`K-9-62`（二欄之讀取與檢核）、`K-9-79` 🔶（新側支 `verify/W-G.9-385-k974`·`W-G.9-385` 工項二·候入主線之請示）；`K-9-62` 之指配 ⬜（另單）。
````

## 附錄丙　塊 `E28`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末·工項三）

````markdown

---

**取號**（`W-G.9-385 §零-1`）：本批取 `621`（`1` 號）。

### 🩸 `自誤 621`　**擬 `W-G.9-385` 前之請示之圖一（一面臨接兩段道路 `BLOCK`），將路口畫為介於 `RD-西` 與 `RD-東` 之間、不屬任何道路 `BLOCK` 之斜線框——與 `K-9-59` ⑤（穿越路口之道路為一個道路 `BLOCK`、路口包含在內；`JUNCTION` 為疊於其上之選用之框）不合；KL 因而問「路口道路仍需劃設一個矩形BLOCK，再畫設一個JUNCTION圖層?」（發單側窗八十七）**

**形**：倉外之圖 `圖_W-G.9-385_臨街負擔之路段.png` 之圖一：道路 `RD-西`（`x∈[0,70]`）與 `RD-東`（`x∈[85,160]`）之間 `x∈[70,85]` 畫一斜線框而標「路口（JUNCTION）」，其下之道路面積不屬二者之任一；並以「路口那一段，以路口中線為界，一半歸西段、一半歸東段」述之。KL `2026-10-16 12:25` 第 `3` 點之問即指此。
**後果之界**：零土地後果（請示之問一、問二之受詞與 KL 之答〔乙／乙〕⛔ 涉路口之畫法；本案無 `JUNCTION`）；KL 須另問一次，發單側另附 `圖三_路口之畫法.png` 答之（`K-6` 典 `W-G.9-385` 之節之二）。若 KL 依圖一之畫法畫他案之圖：路口另成之道路 `BLOCK` 無中心線 ⇒ `K-9-59` 之圖資缺漏而停機（非靜默之誤）。
**根因**：繪示意圖時循 KL `2026-10-13 21:48` 之心像（「交叉路口會畫出一個矩形RD」）而⛔ 先查 `K-9-59` ⑤ 之圖層之約；呈 KL 之圖之 CAD 圖層之畫法未逐一對 `K-9-59`／`K-9-63` 之約。
**後果之框**：🟡 KL 之問捕之（同窗·擬單之前）。
**裁**：⛔ 涉 KL 之裁（`K-9-79` ③ 依 `K-9-59` ⑤）；本號唯登記。
**攔法**：呈 KL 之圖凡含 CAD 之圖層（`BLOCK`、`CENTERLINE`、`JUNCTION`、`FRONT_LINE`、`SIDE_LINE`、`JOINLINE` 等）者，出圖前逐一對 `K-9-59` ⑤、`K-9-63` ⑫ 之畫法之約；示意之簡化（如路口之歸屬）須合其約，或於圖上明註「示意·非畫法」。
````

## 附錄丁　塊 `P38`（附於 `CLAUDE.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`W-G.9-384` 入主線；`K-9-74`、`K-9-62`（二欄）、`K-9-79` 入新側支；`自誤 621`；`W-G.9-384` 之唯讀審查之 (丙) 二之例與 (丙) 三之登記；並行之限（`W-G.9-385`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`（`W-G.9-384` 補令一 工項一）之後；本批之碼在新側支 `verify/W-G.9-385-k974`。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-71`（前節序 `2`） | 入主線（KL `2026-10-16 11:19`「核對無誤」·`W-G.9-384` 補令一之快轉·主線 `158f7fe`） | ✅ | `K-6` 典 `W-G.9-385` 之節之一 |
| `2` | `K-9-74`（前節序 `6`）；`K-9-62` 之「第33條排除」「抵充地」二欄之讀取與檢核；`K-9-79` | 臨街地特別負擔之路寬：各面依其臨接之道路 `BLOCK`——勾新闢全寬、未勾依扣除抵充地（公有持分）與 `JUNCTION` 框後之比例、中心線即區界者以垂距；一面臨二段以上者依臨接長度加權；勾新闢而無道路 `BLOCK` 者 `0` 並警示；二欄以欄名讀之、註記非公有地者等為填列錯誤（停止計算）；畫面之步驟 H 求之、harness ⛔ 動 | 🔶（新側支·候入主線之請示） | `K-6` 典 `W-G.9-385` 之節之二、三；`docs/orders/W-G.9-385_規格單.md` |
| `3` | `K-9-62` 之指配（非共同負擔公共設施用地·「第33條排除」之用） | 公有土地依類別序指配、抵費地、按比例 | ⬜ | 另單 |
| `4` | `自誤 621` | 見自誤簿 | ✅ | 同序 `2` |
| `5` | `W-G.9-384` 之唯讀審查之 (丙) 二（覆蓋之缺） | `F23` `K75`：手冊先行之輪之道路之片之剩下⛔ 依五級再排（照距離） | ✅（量測器·新側支） | 同序 `2` |
| `6` | `W-G.9-384` 之唯讀審查之 (丙) 三（已知之差） | harness 之 `blk5` 之最小建築面積 ＝ `{}`（照 `run_adj4`）、畫面取 session 之有效值 ⇒ `K-9-71` 於某案觸發且街廓間最小建築面積相異時，畫面與 harness 之序可異（本案⛔ 觸）；⛔ 改 | ⬜ | 另單（二者之源之統一·⛔ 急） |
| `7` | `K-9-78`（前節序 `3`） | 調配之畫面入口（新調配程式落地後併入「執行 G 值迭代計算」） | ⬜ | 新調配程式之規格單（規格步 `5`〜`8`） |
| `8` | `GB-205`（前節序 `7`） | `K-9-61` ⑤ 之還原之機制（手冊先行之部分仍待） | ⬜ | 另單 |
| `9` | `K-9-59`〜`K-9-61`、`K-9-63`（前節序 `8`·`K-9-62` 之二欄 ⇒ 序 `2`、其指配 ⇒ 序 `3`） | — | ⬜ | 落地之單（其序另呈 KL） |
| `10` | 畫面於 step G 之後再跑段三而未再跑 step G 者之調配之輸入之顯示（前節序 `9`） | 審查者之警示·可達與否未驗·⛔ 鑄號 | ⬜ | 待查（另單·⛔ 急） |
| `11` | 清冊之顯示（前節序 `10`） | 清冊依原地號合併顯示，與配地時之合併不一定相同；核對時以暫編地號為準 | ⬜ | 另單（⛔ 急） |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：`W-G.9-383` 入主線；……（`W-G.9-384`）」節之序 `2` ⇒ 本表序 `1`（✅）；其序 `6` ⇒ 本表序 `2`（🔶）；其序 `3`、`7`〜`10` ⇒ 本表序 `7`〜`11`（態⛔ 變·序 `8` 之 `K-9-62` 析入本表序 `2`、`3`）；其序 `1`、`4`、`5` ✅ ⇒ 本表⛔ 載。本表序 `3`〜`6` 為新。
🔒 **本案之量**：本批⛔ 變配地（本案之各面之尺度 ＝ 快照之負擔尺度之輸入·`W-G.9-385` 規格單 `§一` 項 `5`）；本案之「重劃區地籍」⛔ 加二欄（其形以 `F30` 之模擬驗之·KL `2026-10-16 12:25` 第 `4` 點）。
🔒 **依賴序**：序 `2`（`W-G.9-385`·入主線之請示）→ 序 `9`（其序另呈 KL）／序 `3` → 規格步 `5` → `6` → `7`／`8`（新調配模組·其畫面入口依序 `7`）；序 `8` 於序 `9` 之前或併之；`GB-196`、`GB-197`、`GB-198`、`GB-202` 與序 `6`、`10`、`11` 另單（⛔ 急）。
🔒 **並行之限**（KL `2026-10-16` 之效率之令）：自 `W-G.9-385` 起，CC 之驗之命令之同時並行數 ≤ `6`；逾時或 `rc` ≠ 期者於⛔ 他負載之下重跑一次、二趟皆入報告。
🔒 **本機介面**：同前節（⛔ 變）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `11`（子字串框·含圖例與本列）·列 ＝ `9`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: a654119304826be66b4c50326ed304109e8754383689b228377c8db3041f20d2
