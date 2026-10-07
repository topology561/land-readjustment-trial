# `W-G.9-370`　規格單：`K-9-57` ⑧ 之落地——「併出前發現該建地已可配地」之三停機改列程式自我檢查（`S219`、`S238` 之訊息之改列 ＋ 第一趟之逐片之建地片之查 `R-10′`）＋ harness 之 session 之讀法之一致（`R-22`）＋ `W-G.9-367 §四-2` 之補寫（量測器 `F24` 增 `K23`〜`K27`·新器 `F25`·`F23` 之期之更新）＋ `GB-202` 之立 ＋ 自誤 `584`〜`587` ＋ `K-6` 典之註 ＋ 待落地清單之更新（新側支 `verify/W-G.9-370-selfchk`）

> **本單建議等級 ＝ `high`**（生產碼 `2` 檔之小改：`app.py` 之 `adj4_pass1_run` 增一巢狀函式與其一呼叫、二函式之停機訊息三則；`verify/selection_pipeline.py` 之二列；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單側窗七十一·`2026-10-07`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-370-selfchk`**，其起點 ＝ 主線之端 `3b35daa`）。
> **流程 ＝ 規格單**（常態·附則甲〜丙施行）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `F24t`／`F23w`／`F25`·CC ⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `2` 檔；**本案之配地⛔ 變**——三停機於本案皆⛔ 觸，第一趟之受詞唯道路片一·⛔ 經建地之逐片；`R-22` 於鍵在時逐位同）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `3b35daad5fbf1749b7b596b0013575ec4388202d`（`W-G.9-369` 工項二）；側支 `verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`；遠端 heads `36`。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-370-selfchk`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F24t`／`F23w`／`F25`／`K13`／`G11`／`E13`／`P23` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`自誤 479`）。Bash 命令⛔ 含 heredoc（常設規則索引）。`<O>` ＝ CC 自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-370_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限**（`W-G.9-367R` ③-8 之首趟之逾時·發單側窗六十九之裁）：各驗之命令得並行，唯 `parity`、`F24 run`、`k6s3 run` 之同時並行數 ≤ `2`；逾時（`600` s 之類）者，於⛔ 他負載之下重跑一次，首趟之出艙照實入報告。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之 `adj4_pass1_run`、`k953_manual_run` 以外之一字；`adj4_pass1_run` 之既有之列之改或刪（`S238` 之訊息之列除外）；`k953_manual_run` 之 `S219` 之訊息之列以外之一字；`verify/selection_pipeline.py` 之 `run_adj4` 之二列以外之一字；生產碼 `34` 檔之其餘 `32` 檔；`§三-3` 之禁改；既有量測器除塊 `F24t` 所改之 `verify/probes/probe_WG9367_adj4.py`、塊 `F23w` 所改之 `verify/probes/probe_WG9363_k953.py` 外之一字；`verify/case_params_UC9898.json`、`verify/case_front_road_names_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md` 除塊 `K13`／`G11`／`E13`／`P23` 之純末端追加外之一字；任何他側支（含 `verify/W-G.9-367-adj4`）之推送、刪除或改寫；KL 主 checkout。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `3b35daad5fbf1749b7b596b0013575ec4388202d`；`git rev-parse origin/verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`；`git ls-remote --heads origin` 之列數 ＝ `36`（全 `36` 列存 `<O>\heads_before.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-370-selfchk`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 583 579` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `568`／`MAX` `583`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `194`／`201`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `60`／`63`／`[44, 47]`。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態 `3b35daa` 之 `docs/` 全檔 **`975`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗七十一實跑 `python verify/probes/wg9268_gate6_occupancy.py 3b35daa W-G.9-370 W-G.9-369 W-G.9-397`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-370`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `4`／`16` | 🟢 可取（鬆框之 `16` 列皆既有之單、報告、典、簿對本單之預告·⛔ 占用） |
| 對照甲［必非零］`W-G.9-369` | `2`／`8`／`4` | `2`／`8`／`4` | `12` | `4` | `5`／`47` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-397` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `7`／`9` | 🟢 宣告框之嚴格 `0`、鬆框非零（器之標籤「甲（須 ≥1）」依本表之角色讀之·同 `W-G.9-365R` ⑥ 自解 `1`） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`4` | `0`（寬式 `4`） | `0`（寬式 `2`） | `37`／`41` | 🟡 寬式 `D3` 非零：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

**本批所鑄之號**（母體 ＝ 開工態 `3b35daa` 之追蹤檔 **`2795`** 檔·列框；發單側窗七十一以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``／`-F "GB-<號>"`〕於 `3b35daa` 實算）：

| 號 | 裸（錨定）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 584`〜`587`（逐號） | `55`／`239`／`76`／`29` | 皆 `0` | 皆 `0` | 皆 `0` | 🟢 可取（裸列皆數字之偶合——行號、bytes、坐標等·⛔ 為自誤之引用） |
| 對照甲［必非零］`自誤 583` | `72` | `5` | `0` | `5` | 🟢 框非恆空 |
| `GB-202` | — | `4` | — | — | 🟢 可取（`4` 列皆本項之預告：`CLAUDE.md` 待落地清單序 `4`、`docs/orders/W-G.9-369_中量單.md` 之三列） |
| `GB-203` | — | `15` | — | — | ⛔ 取（`K-9-57` ⑧ 記「⛔ 立」·其號視同已焚·塊 `G11` 記之） |
| 對照甲［必非零］`GB-201` | — | `93` | — | — | 🟢 框非恆空 |

新側支之名 `verify/W-G.9-370-selfchk`：`git ls-remote --heads origin` 無其列；`git grep -c -F "W-G.9-370-selfchk"` 於 `3b35daa` ＝ `0` 檔。新器之路徑 `verify/probes/probe_WG9370_adj4mut.py`：`git ls-files` ＝ `0`；`git grep -c -F "probe_WG9370"` ＝ `0` 檔。塊名 `F24t`／`F23w`／`K13`／`G11`／`E13`／`P23` 於 `3b35daa` 之 `` 塊 `<名>` `` 之命中皆 `0`（`F25` 之 `2` 檔皆本器之預告）。

自誤 `MAX` ＝ `583`、`GB` `MAX` ＝ `201`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 584`〜`587`（塊 `E13`）、`GB-202`（塊 `G11`）；⛔ 鑄 `VR`／`K-9`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `3b35daa`，或側支 `verify/W-G.9-367-adj4` ≠ `e7855ec`，或遠端 heads ≠ `36`、或已含 `refs/heads/verify/W-G.9-370-selfchk`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `F24t`／`F23w`／`F25`／`K13`／`G11`／`E13`／`P23` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或塊 `F24t`／`F23w` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `9` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-6` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-370-selfchk`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線、`verify/W-G.9-367-adj4` 於本批中有任何推進 |
| `8` | 工項三之四簿（`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md`）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或 CC 認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer（附則丙）之發現涉域上判斷或規格之漏載 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `12`。

---

## `§一`　態錨（發單側窗七十一自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`·Python `3.13`·`numpy 2.4.6`〔`GB-198`〕·`shapely 2.1.2`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `3b35daad5fbf1749b7b596b0013575ec4388202d`（`W-G.9-369` 工項二·其祖含 `e7855ec`）；`verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`；遠端 heads **`36`**；`app.py` ＝ `af2b8f397c71a0adee156c4fdb90696ef7dadf43`、`verify/selection_pipeline.py` ＝ `9e189d50a9c685589bef8df0389f0af597f2cc43`、`verify/probes/probe_WG9367_adj4.py` ＝ `1a984542a9e67799be6a2d7baa207776e1aa7d10`、`verify/probes/probe_WG9363_k953.py` ＝ `c0bc21aaa76d35b4b975cd1cf99b11b24f498b46`（二態 `7c4ecc2`／`3b35daa` 之 `app.py`、`verify/` 逐位同） |
| `2` | `W-G.9-369` 之復驗（發單側窗七十一·自倉重跑） | 收工閘 `1`〜`9` 逐項 ＝ 其期：四簿 `549713`／`1048012`／`1127630`／`348430`·blob 逐一同·嚴格前綴·其尾 ＝ 塊 `K12`／`G10`／`E12`／`P22`（自 `docs/orders/W-G.9-369_中量單.md` 依圍欄抽出）；生產碼 `34` 檔對 `e7855ec` 相異 `0`；`heads_before` 之重組（現 heads 之主線列還原為 `d7a5ea4…`）之 `sha256` ＝ `2316506d…`（＝ CC 所錄）；`closegate 583 579` `✅ 二閘皆過`；`issuer_anchor 583 579` ＝ `§零-0` 項 `3` 之值；`checkidx`／`gen_fa_index` ＝ 其期；`F24` 三子命令皆 `rc 0`（`run` `857` s） |
| `3` | 突變之判別力（發單側窗七十一·倉外·`3b35daa` ＋ 塊 `F25`·`F24` 為開工態之 `K1`〜`K22`） | `python verify/probes/probe_WG9370_adj4mut.py mutate <repo>` ⇒ 其 `M09`（`R-8` 之街廓之首之止）、`M13`（`R-9` 之 `T` 唯本街廓）、`M15`（`R-10` 之同類之序）、`M18`（`R-10` 之建地之 `T` 唯本街廓）、`M23`（`R-12` 之「併入後中止 ⇒ 不過」）之紅之集皆**空**（開工態之 `F24` ⛔ 察）；`M12`、`M19` 唯以 `K3`／`K4` 察之；塊 `F24t` 之 `K23`〜`K26` 察前五（`§一` 項 `5`）。`R-12` 之「`R` 之除」⛔ 列（其由見塊 `F25` 之 docstring） |
| `4` | 舊 `W-G.9-368` 規格單（發單側窗六十九·未發·`69486` B·`sha256` `ecf0ac40…1132`·KL `2026-10-07 08:56` 再附）之核 | 其塊六之 bytes／`sha256` ＝ 其 `§五-1`；其 `F24t` 於 `3b35daa` 仍 `git apply --check` 過。**其 `§一` 項 `5`／`6` 之「`F24 wiring <repo> d7a5ea4` ⇒ `rc 0`」⛔ 立**：舊 `F25` 置於 `verify/probes/` 後 `F24` 之 `W7` 紅（`自誤 587`）⇒ 本單塊 `F24t` 增 `W7_SKIP` |
| `5` | 原型（發單側窗七十一·倉外·`3b35daa` ＋ 塊 `F24t`／`F23w`／`F25` ＋ `§三` 之一實作·⛔ 為 CC 之期） | `F24 selftest` ⇒ `rc 0`·`K1`〜`K27`（含 `K4b`）皆 ✅·`P0` `28／28`；`F24 wiring <repo> d7a5ea4` ⇒ `rc 0`（`W1`〜`W7` 皆 ✅）；`F24 run`（二退縮）⇒ `rc 0`·`R1`〜`R5` 皆 ✅（`3.5 m` ΣΔG `+7.67`／ΣΔ抵費地 `-7.65`；`0 m` `+7.68`／`-7.64`·同 `W-G.9-369` 之主線）；`F23 selftest` ⇒ `rc 0`·`K1`〜`K40` 皆 ✅·`P0` `40／40`；`F23 wiring <repo> 7d8e954` ⇒ `rc 0`；`F25 wiring <repo> 3b35daa` ⇒ `rc 0`（`X1`〜`X5` 皆 ✅）；`F25 mutate <repo>` ⇒ `rc 0`·末列逐字 `⇒ 突變 30（另基準一）；紅 []；rc 0`；`F9 wiring`、`F10 wiring`、`F14 selftest` ⇒ 皆 `rc 0`；`k6s3 run`（二退縮）之 `cmp`（對工項一之端）⇒ 皆 `rc 0`·末列逐字 `相異 0 項 ⇒ ✅ 同`；`parity`（二退縮）⇒ 皆 `rc 0`·其值 ＝ `§四-1` `V-5` 之期。原型之 `app.py` 對開工態 `+20`／`-4`、blob `0d4305cad5c07c7eb7e38518dc9f99ad5382307b`（皆⛔ 為期）。判別力：於原型之 `k953_manual_run` 之他處增一列 ⇒ `F25` 之 `X2` 紅（`F24` 之 `W6` 許增列·二者互補）；改 `adj4_pass1_run` 之一既有列 ⇒ `X2` 紅 |
| `6` | 工項一之端（`3b35daa` ＋ 塊 `F24t`／`F23w`／`F25`）之量測器之態 | `F24 selftest` ⇒ **`rc 1`**·末列逐字 `⇒ 紅 ['K9', 'K27']；rc 1`（`P0` `28／28`）；`F23 selftest` ⇒ **`rc 1`**·末列逐字 `⇒ 紅 ['K36', 'K37', 'K39', 'K40']；rc 1`（`P0` `40／40`）；`F25 wiring <repo> 3b35daa` ⇒ **`rc 1`**·末列逐字 `⇒ 紅 ['X3', 'X4', 'X5']；rc 1`；`F25 mutate <repo>` ⇒ **`rc 1`**·末列逐字 `⇒ 突變 30（另基準一）；紅 ['M00', 'M31']；rc 1`（`M00` 之紅 ＝ `['K9', 'K27']`；`M31` 之錨 `0` 見）；`F24 wiring <repo> d7a5ea4`、`F23 wiring <repo> 7d8e954`、`F9 wiring <repo>`、`F10 wiring <repo>`、`F14 selftest <repo>` ⇒ 皆 `rc 0`（末列逐字 `⇒ 紅 []；rc 0`）；`k6s3 run`（二退縮）⇒ `rc 0` |

---

## `§二`　KL 之語與射程

🔒 **所據**：
- `K-9-57` ⑧（`K-6` 典·逐字）：「**⛔ 生之題**：已不能分配之二片，⛔ 生「先併出一片、再試另一片可否配地」之問題（第 `5` 點）。發單側窗六十九原呈之「GB-203」之題其前提不成立，撤回，⛔ 立 `GB-203`。程式中「併出前發現該建地已可配地」之二停機（`S219`、`S238`）改列程式自我檢查：依既定機制不會發生，觸之即程式有錯。」
- `W-G.9-369 §二` 之入主線之請示（KL `2026-10-06 22:34`·逐字「是」）所答之表，其 `W-G.9-370` 之要旨（逐字）：「**W-G.9-370** ＝ 舊 368 之改正重發，於新側支施工；R-10′ 改列「程式自我檢查」；GB-203 不立；自誤 580 與 K-6 註之用語改正；其餘 R-22、F24 增 K23〜K27、F25 突變器、GB-202 照原設計——生產碼，本案配地不變。」
- `W-G.9-367 §四-2`（以 CC 之碼之字樣為錨之接線檢查及其突變之判別力）；`K-9-53` ①／② 與 `K-9-56`（KL 已裁）。

🔒 **`S219`、`S238` 之併辦**（發單側窗七十一於對話之通知·答 KL `2026-10-07 08:33` 之訊·逐字之要）：「**通知（非領域判斷，你已裁過）**：擬於 `370` 一併處理 `K-9-57` ⑧ 之兩個停機點 `S219`、`S238`。……依你的裁定，改為程式自我檢查之訊息……這只改訊息文字，**配地不變**。若你要分開辦，請告知；未告知即依此併入。」KL `2026-10-07 08:56` 附舊 `W-G.9-368` 規格單，⛔ 表異議 ⇒ 併入本單（`R-24`、`R-25`）。訊息之語取 `K-9-57` ⑧ 之「依既定機制不會發生，觸之即程式有錯」。

🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 之畫面核對與逐字放行**。

🔒 **`W-G.9-367` 之 `R-17`／`R-18` 之字面之改讀**（`自誤 586`）：`R-18` 之「`session_state[鍵]`」讀為「`session_state.get(鍵, {}) or {}`」（CC 之既取·⛔ 改碼）；`R-17` 之 `ss['t8_ownership_map']` 由 `R-22` 改之。

🔒 **舊稿之改正**（`W-G.9-369 §二` 之表）：舊 `R-10′` 之停機之由「分不到之前提不成立」⛔ 採，改列程式自我檢查（`R-10′`·`§三-2` 之模板）；⛔ 立 `GB-203`（塊 `G11` 記其號之焚）；舊 `自誤 580`〜`582` 改寫為 `584`〜`586`（`584` 與 `582` 之界分明）；舊塊 `K11` 之註改寫為塊 `K13`。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支（附則甲〜丙）；`(c)` ⛔ 及主線、`verify/W-G.9-367-adj4`、KL 主 checkout、`GB-196`〜`GB-198`、`GB-202` 之修、`K-9-57` ③④⑤ 與 `K-9-58`〜`K-9-63` 之落地、規格步 `5`——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**：「當下之態」「試算」「已配得之宗」「成員」之義同 `W-G.9-367 §三`（`adj4_pass1_run` 之 `state`、`_sim_a4`、`kept`、`members`·`members` 缺某宗者以 `[該宗]` 代之）；「已為已配得之宗或其成員」之判 ＝ `R-8` 之 `_inS` 之同一式（諸街廓之諸已配得之宗之成員之聯集·附則乙）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-10′` | `app.py` 之 `adj4_pass1_run`（`K-9-57` ⑧·新增之查） | 於 `R-10` 之**建地片**之逐片之整筆之試（既有之 `_c1 = _dup_a4(state)` 起之一段）**之前**：以當下之態試算（`_sim_a4`·同一態只試算一次）。其 `err` 非空 ⇒ 停機；其 `members` 非 `dict` ⇒ 停機（二者之訊息首 ＝ `_hd_a4`，且含 `x` 與「逐片」）。`x` 為該試算之任一街廓之任一已配得之宗之成員 ⇒ 停機，訊息 ＝ `§三-2` 之模板 `R-10′`（程式自我檢查）。其餘 ⇒ ⛔ 改任何物、續行既有之一段。停機一律 `RuntimeError`。⛔ 及於道路片與公設片之逐片、⛔ 及於整體（`R-9`）。 |
| `R-24` | `app.py` 之 `adj4_pass1_run` 之 `R-8` 之查（盤點 `S238`） | 其條件、位置、停機⛔ 變；唯其訊息改為 `§三-2` 之模板 `S238`（基準中此 `raise` 之列以外⛔ 改）。 |
| `R-25` | `app.py` 之 `k953_manual_run` 之 `_wpre953` 之「已為已配得之宗 `{_own953}` 或其成員」之查（盤點 `S219`） | 同 `R-24`；其訊息改為 `§三-2` 之模板 `S219`。`k953_manual_run` 之他列⛔ 改、⛔ 增。 |
| `R-22` | `verify/selection_pipeline.py` 之 `run_adj4`（`自誤 586`） | 其二處之 `ss["t8_ownership_map"]`（先篩之引數一、`_own_a4` 之賦值一）改為 `ss.get("t8_ownership_map", {}) or {}`；他字⛔ 改。 |
| `R-23` | 本案 | 二退縮之配地、第一趟之紀錄、手冊先行之紀錄、段三之紀錄、街角得標與強制旗標皆⛔ 變（三查於本案皆⛔ 觸）。 |

### `§三-2`　介面（名與形·量測器 `F25 wiring` 以之為受詞）

- `R-10′` 以 `adj4_pass1_run` 內之**巢狀函式**為之，其定義之列逐字 `def _bpre_a4(_x, _g):`（縮排 `4` 格·定義於 `for _sj in subjects:` 之前）；其呼叫恰一處、為一敘述，其列逐字 `_bpre_a4(_x, _g_str)`（去前導之空白後），其前一非空列 ＝ `if _cls[_x] == '建地':`、其後一非空列 ＝ `_c1 = _dup_a4(state)`（`F25` 之 `X3`）。
- 三停機之訊息之**模板**（逐字·`F25` 之 `X5`）。模板 ＝ 訊息之 f-string（含隱式相接之諸段）之常數段逐字、其代入段以 `{` ＋ 式之原文 ＋ `}` 代之；CC 得於任一處斷為隱式相接之二段以上，唯相接後須逐字同：

```
S238（adj4_pass1_run 之本體）：
{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g_str}）於第一趟沿名單至街廓 {_bk} 時，當下之試算已為已配得之宗或其成員——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機
R-10′（adj4_pass1_run 之巢狀 _bpre_a4）：
{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g}）於逐片之整筆之試之前，當下之試算已為已配得之宗或其成員——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機
S219（k953_manual_run 之巢狀 _wpre953）：
{_hdr953} 程式自我檢查：建地片 {_x}（{_blk953[_x]}）於整筆之主併入之前，當下之試算已為已配得之宗 {_own953} 或其成員——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機
```

- `app.py` 之頂層節點對 `3b35daa` 相異者唯 `adj4_pass1_run`、`k953_manual_run`；`adj4_pass1_run` 對 `3b35daa` 唯增列，唯基準中 `S238` 之 `raise` 之列得易；`k953_manual_run` 對 `3b35daa` 之差唯在基準中 `S219` 之 `raise` 之列之內（`F25` 之 `X2`）。
- `verify/selection_pipeline.py` 對 `3b35daa` 之差恰為 `R-22` 之二列（`F25` 之 `X4`）；其施後之 blob 由之而定 ＝ `a1d46f7d9a41a5d99808a7fdfe2bc27d8dfb86fb`。

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. 量測器 `F24 wiring` 之 `W7`：基準（`d7a5ea4`）之 `app.py` 中恰一見之既有量測器之錨，於工作樹仍須恰一見。**新寫之碼⛔ 得重寫其字樣**——例：單引號之 `'kept'` 於基準恰一見，新碼取試算之鍵須以他形（如 `_Sx.get("kept")`·同 `adj4_pass1_run` 既有之寫法）。
2. 量測器 `F24 wiring` 之 `W6`：`k953_manual_run` 對 `d7a5ea4` 唯增列，唯 `S219` 之基準二列（塊 `F24t` 之 `W6_REPL`·逐字）得易。
3. 量測器 `F23 wiring` 之 `W8`（基準 `7d8e954`）之錨，同款 `1`。
4. 量測器 `F25 mutate` 之突變之錨（塊 `F25` 之 `MUTS` 之第五欄）皆須於其函式之源碼段內仍恰一見（`M31` 之錨即 `R-10′` 之呼叫之列）。
5. `W-G.9-367 §三-3` 之全部。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

三停機皆程式自我檢查（`K-9-57` ⑧）：觸之即程式有錯，**碼唯停機**，⛔ 定其土地之去處。撰碼中若見「三查須及於道路片、公設片或整體」之必要，或「停機」以外之處置之必要，或模板之文與 `K-9-57` ⑧ 之義有違 ⇒ 停機上呈。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐條（`R-10′`／`R-24`／`R-25`／`R-22`）：落於何處、其字樣；對 `§三-3` 各款之自查；附則乙之自查（`R-10′` 之「已為已配得之宗之成員」之判與 `R-8` 之 `_inS` 之式是否同一）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/selection_pipeline.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-370-selfchk`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-370_規格單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-370 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-370-selfchk`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`37`**、主線仍 ＝ `3b35daa…`、`verify/W-G.9-367-adj4` 仍 ＝ `e7855ec…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-370-selfchk`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `F24t`、`F23w` 各抽為 `<O>\F24t.diff`、`<O>\F23w.diff`，對拍 `§五-1` 後各 `git apply --check` ⇒ 過、各 `git apply`；塊 `F25` 依圍欄之逐列索引抽出、對拍後以二進位寫為 `verify/probes/probe_WG9370_adj4mut.py`（**新檔**）；三檔之 `git hash-object` ＝ `§五-1` 項 `9`（停機款 `3`）。`commit` 訊息逐字 `W-G.9-370 工項一：量測器 F24 之增項（K23〜K27·K9 之期）＋ F23 之期之更新 ＋ 新器 F25（以 CC 之碼之字樣為錨之突變·接線）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-370-selfchk`。

**工項二　生產碼**（🔴 `app.py` ＋ `verify/selection_pipeline.py`·CC 依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`）：
1. `python verify/probes/probe_WG9367_adj4.py selftest <repo>`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python verify/probes/probe_WG9370_adj4mut.py mutate <repo>` ⇒ 皆 **`rc 1`**（末列逐字 ＝ `§一` 項 `6`）。
2. `python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`；`python verify/probes/probe_WG9350_frontroad.py wiring <repo>`；`python verify/probes/probe_WG9351_intake.py wiring <repo>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` ⇒ 皆 **`rc 0`**（末列逐字 `⇒ 紅 []；rc 0`）。
3. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`（皆 `rc 0`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫二檔之改動；`python -m py_compile app.py verify/selection_pipeline.py`；`commit` 訊息逐字 `W-G.9-370 工項二：K-9-57 ⑧ 之三停機改列程式自我檢查（S219·S238 之訊息·R-10′ 逐片之建地片之查）＋ harness 之 session 之讀法（R-22）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9367_adj4.py selftest <repo> > <O>\f24_self_post.log`；`… wiring <repo> d7a5ea4 > <O>\f24_wir_post.log`；`… run <repo> > <O>\f24_run_post.log` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `K1`〜`K27`（含 `K4b`）皆 ✅、`P0` `28／28`；`wiring` 之 `W1`〜`W7` 皆 ✅；`run` 之二退縮 `R1`〜`R5` 皆 ✅ |
| `V-2` | `python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa > <O>\f25_wir_post.log`；`python verify/probes/probe_WG9370_adj4mut.py mutate <repo> > <O>\f25_mut_post.log` | 皆 **`rc 0`**；`wiring` 之 `X1`〜`X5` 皆 ✅、末列逐字 `⇒ 紅 []；rc 0`；`mutate` 之 `M00`〜`M31`（`M22` 除外·`31` 列）皆 ✅、末列逐字 `⇒ 突變 30（另基準一）；紅 []；rc 0` |
| `V-3` | `python verify/probes/probe_WG9363_k953.py selftest <repo> > <O>\f23_self_post.log`；前置 `2` 之諸器（同命令·出艙存 `<O>\*_post.log`） | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`F23 selftest` 之 `K1`〜`K40` 皆 ✅、`P0` `40／40` |
| `V-4` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`python verify/probes/probe_WG9344_k6s3.py cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**·`R-23`） |
| `V-5` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；配地列 `3.5` ⇒ harness `35`／畫面 `34`、`0.0` ⇒ `36`／`35`，不符格 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`；「手冊先行 session 鍵 f3_k953_log」✅（`34`／`43` 列）；「第一趟 session 鍵 f3_adj4_log」✅（`1`／`1` 列）；「段三後 build 之暫編地號依序」`45`／`46`（皆 ＝ `W-G.9-367` `V-5`） |
| `V-6` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；`verify/selection_pipeline.py` 之增／刪 ＝ `2`／`2`、其 blob ＝ `a1d46f7d9a41a5d99808a7fdfe2bc27d8dfb86fb`；`app.py` 之刪 ≤ `4`（唯 `S219`、`S238` 之訊息之列）；`app.py` 之 blob 與增之數出艙（發單側復驗時自倉重算）；`verify/` 之其餘一切檔對工項一之端相異 `0` |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞（三停機之訊息、`R-10′`、`R-22`）於本案之配地⛔ 觸，其「⛔ 變」由 `V-1` 之 `run`、`V-4`、`V-5` 直接量之（性質 ＝ 配地與其紀錄之逐項同）；`run_all` 之相異項亦唯可由配地之變而生。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-6`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-370-selfchk`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K13` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `G11` 附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；塊 `E13` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P23` 附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；四檔之 blob ＝ `§五-1` 項 `9`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `8`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P23` 附後：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
4. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息逐字 `W-G.9-370 工項三：K-6 典之註（K-9-57 ⑧ 之落地）＋ GB-202 之立·GB-203 之號之焚 ＋ 自誤 584〜587 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-370-selfchk`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-370R_程式自我檢查之三停機_執行報告.md` ＋ 同目錄之 `W-G.9-370R_程式自我檢查之三停機_二檔差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 前置與驗之全部出艙（`F25 mutate` 之全文、`F24`／`F23` 之 `selftest`／`wiring` 之全文、`F24 run` 之末十二列、`k6s3 cmp` 之全文、`parity` 之末十五列）；④ 塊之實得（bytes／`sha256`）與四簿之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **二檔之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-370 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-370-selfchk`。

### `§四-2`　次單（⛔ 本單之期）

發單側復驗本批之碼（自倉重跑 `V-1`〜`V-6`）後：**入主線之請示**（本批·生產碼·配地⛔ 變）·附 KL 於畫面之核對（新側支之端之 `app.py` 於退縮 `3.5 m`／`0 m` 按「🧮 執行 G 值迭代計算」：「📒 手冊先行」之紀錄 `34`／`43` 列、「🧭 規格步 4 乙（第一趟）」之紀錄各 `1` 列、`628-34(2)` `257.91 ㎡`、`R3` 之抵費地 `1651.41 ㎡`——皆 ＝ `W-G.9-369` 所記之畫面核對）＋ 主 checkout 之同步。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9367_adj4.py` `80`／`13`、`verify/probes/probe_WG9363_k953.py` `12`／`8`、`verify/probes/probe_WG9370_adj4mut.py` `339`／`0`（增／刪）；工項二 ＝ `app.py`（刪 ≤ `4`）、`verify/selection_pipeline.py` `2`／`2`；工項三 ＝ `docs/rulings/K-6_街角地分配程序與可分配判準.md` `13`／`0`、`docs/reports/W-G.4_泛用阻塞項登記表.md` `17`／`0`、`docs/reports/W-G.9波_claude.ai側自誤登記.md` `37`／`0`、`CLAUDE.md` `20`／`0`（唯此四檔）；工項四 ＝ 報告二檔之增（刪 `0`） |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `3b35daa` | 生產碼相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；`verify/` 之一切檔相異恰 **`4`**（`A` `1`：`verify/probes/probe_WG9370_adj4mut.py`；`M` `3`：`verify/selection_pipeline.py`、`verify/probes/probe_WG9367_adj4.py`、`verify/probes/probe_WG9363_k953.py`）；本批之新檔（本單、`F25`、報告二檔）之 `git check-ignore -v` 皆無命中 |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`12` 檔：本單、`F24`、`F23`、`F25`、`app.py`、`verify/selection_pipeline.py`、`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md`、報告二檔） |
| `4` | 四簿之 bytes | `K-6` 典 `549713` → **`551947`**；`GB` 簿 `1048012` → **`1050787`**；自誤簿 `1127630` → **`1134714`**；`CLAUDE.md` `348430` → **`351013`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊 |
| `5` | 自限 | 遠端 heads **`37`**；主線 ＝ `3b35daad5fbf1749b7b596b0013575ec4388202d`（⛔ 變）；`verify/W-G.9-367-adj4` ＝ `e7855ec…`（⛔ 變）；`verify/W-G.9-370-selfchk` ＝ 工項四之 `commit`，其祖含 `3b35daa`；其餘 `36` 列（除 `verify/W-G.9-370-selfchk`）逐列 ＝ `<O>\heads_before.txt` |
| `6` | `python verify/probes/probe_WG9270_closegate.py 587 583 .` | **`rc 0`**（末列 `✅ 二閘皆過`） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 587 583` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`572`**／`MAX` **`587`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` **`195`**／**`202`**／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `60`／`63`／`[44, 47]` |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項一〜三並實跑閘 `1`〜`8` 之可模擬者 ⇒ 見 `§五-1` 項 `11`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `F24t` | `14606` B·`sha256` `5461af709e6fe810d143d08cb68ab32e88f65d5c4127a12c58b274b74de9e298`·`184` 列（圍欄內全文·末附換行）；抽為 `<O>\F24t.diff`，`git apply` 於 `verify/probes/probe_WG9367_adj4.py`（施前 blob `1a984542a9e67799be6a2d7baa207776e1aa7d10`） |
| `3` | 塊 `F23w` | `5472` B·`sha256` `3bed0aa5866ee9b048603c63be9546353722a6b6962ca58321cc2944d430e58d`·`84` 列（圍欄內全文·末附換行）；抽為 `<O>\F23w.diff`，`git apply` 於 `verify/probes/probe_WG9363_k953.py`（施前 blob `c0bc21aaa76d35b4b975cd1cf99b11b24f498b46`） |
| `4` | 塊 `F25` | `19532` B·`sha256` `b66349e992d5e32f30428aa3295b141953674ead038f7cb5b402377cfdec0242`·`339` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9370_adj4mut.py` |
| `5` | 塊 `K13` | `2234` B·`sha256` `8e222a8b3fac1670f3c483e2ef7af20fadb67e7533708036cf8303d7d5a07d6b`·`13` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`549713` B）之末，期末 ＝ `551947` B |
| `6` | 塊 `G11` | `2775` B·`sha256` `cc7e594e3bf02b7f67b81265be771c1401dde113422a382460fb8bff2eed69aa`·`17` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1048012` B）之末，期末 ＝ `1050787` B |
| `7` | 塊 `E13` | `7084` B·`sha256` `4aa8dcfdd2111b0146952d2e21e65d8bb97d4701287ae269e28316efb608cfa0`·`37` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1127630` B）之末，期末 ＝ `1134714` B |
| `7′` | 塊 `P23` | `2583` B·`sha256` `21e192405d6f51f92fdd3a6188756cbb17ce07b0e2ac91aa80f41b635c478ad9`·`20` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`348430` B）之末，期末 ＝ `351013` B；其 payload 內 `⬜` 之子字串框 `6`·列框 `4`（塊之自載） |
| `8` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-369 §五-1` 項 `7`） |
| `9` | 寫出後之 blob | `verify/probes/probe_WG9367_adj4.py` `21e77d0c59e946d3b4b53f570986ff3c01c8e150`；`verify/probes/probe_WG9363_k953.py` `6a835e5f08b04d39e36fb38d20ebcb2a9728af56`；`verify/probes/probe_WG9370_adj4mut.py` `02546aab826f0bf87414f23576633e11dd44c654`（以上工項一）；`verify/selection_pipeline.py` `a1d46f7d9a41a5d99808a7fdfe2bc27d8dfb86fb`（工項二·`R-22` 所定）；`docs/rulings/K-6_街角地分配程序與可分配判準.md` `c8ad07d49292e380551cea55bb5f75563b0bc317`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `3461cdd803b48b85ec5c84a8f2e15f57f1ac2b78`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `638b105b09a1d54274ecd82b1ee1bc4f4cc1c50e`；`CLAUDE.md` `10861d8050acfa7a819336f457294baad56a7511`（以上工項三）。🔒 `app.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `10` | 量測器之二態 | 工項一之端 ＝ `§一` 項 `6`；工項二施後 ＝ `§一` 項 `5`（原型為其必過之實例） |
| `11` | 收工閘之模擬（發單側·本機 Linux·⛔ `push`） | `git worktree add --detach <S> 3b35daa`（拋棄式·⛔ `push`）＋ 本單之前稿（塊與本單逐位同）＋ 依 `§五-1` 末之抽取式自前稿抽出之七塊（bytes／`sha256`／列數 ＝ 項 `2`〜`7′`；`F24t`／`F23w` 之 `git apply --check` 過）＋ 原型之二檔 ＋ 報告之替身·五 `commit`：工項一之三檔之 blob 與工項三之四簿之 blob ＝ 項 `9`；閘 `1` 之增刪 ＝ 其期（工項二之原型 ＝ `app.py` `20`／`4`〔⛔ 為期〕、`verify/selection_pipeline.py` `2`／`2`）；閘 `2` 生產碼相異 `2`、`verify/` 相異 `4`（`A` `1`·`M` `3`）、新檔四之 `git check-ignore -v` 無命中；閘 `3` CR 合計 `0`（`12` 檔·`data/V6.dxf` `12308`）；閘 `4` 四簿皆嚴格前綴、其尾 ＝ 塊；閘 `6` `rc 0`（`✅ 二閘皆過`）；閘 `7` `rc 0`·四簿 ＝ 其期；閘 `8` ＝ 工項三項 `3`／`4` 之期（`FX` 逐位同） |
| `12` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗七十一實跑（態 `3b35daa`）：🔴 機械 `0` 項（`P-5` ✅·`P-3` 無受詞）／🟡 提示 `3` 項——`P-2` `:899`（塊 `G11` 之取號之 `git grep -c -F`·其受詞係完整之號 `GB-202`，以 `-P "(?<![0-9\-])GB-202(?![0-9])"` 重算亦 `4`〔⛔ 前綴之偶合〕 ⇒ **具名豁免**）、`P-2` `:932`（塊 `E13` 之 `自誤 585`·其受詞係完整之識別字 `f24_internal` 之全倉之有無，框之錨⛔ 涉 ⇒ **具名豁免**）、`P-4` `:537`（塊 `F25` 之 docstring·其箭頭係突變之字樣之換、⛔ 為方向之轉引 ⇒ **具名豁免**）；ℹ️ `P-3` 之 `def main` ＝ `21782`-`29502` |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·語言名不拘：本單用 `diff`、`python`、`markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；塊以附錄之標題列（以 `## 附錄` 起首之列）之後之第一個圍欄開列定位。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-370-selfchk`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F24t`（`git apply` 之差異·`verify/probes/probe_WG9367_adj4.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index 1a98454..21e77d0 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -8,14 +8,19 @@
            合成對照（⛔ 讀本案資料·`harvest(app.py)` 取受詞；`verify/selection_pipeline.py` 取 `run_adj4`）。玩具之回呼：
            `alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內之 `面積_m2` 之和 `>` 該街廓之容量 ⇒ 該街廓之配餘地
            不合格一處；`err_cap` 逾者 ⇒ 配地中止；`lose` ＝ `{宗: (門檻, 失者)}`（該宗之 `面積_m2` `>` 門檻 ⇒ 失者不保留）；
-           `G` ＝ 分攤登記面積 ＋ 面積（`gmap` 覆寫）；`a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓）。
-           K1〜K22 ＝ 各支（期值出自規格單 `§三`·⛔ 呼叫受測碼求期）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
+           `G` ＝ 分攤登記面積 ＋ 面積（`gmap` 覆寫）；`a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓）；
+           `tie` ＝ `{片: 失者}`（該片離 build ⇒ 失者不保留）；`bar` ＝ `{片: 受阻者}`（該片在 build ⇒ 受阻者不保留）
+           （二者皆 `W-G.9-370` 增）。
+           K1〜K27 ＝ 各支（K23〜K27 ＝ `W-G.9-370` 之增·以 CC 之碼之突變之判別力為據；K9 之期 ＝ `W-G.9-370` 之訊息）（期值出自規格單 `§三`·⛔ 呼叫受測碼求期）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
   wiring   <repo> <基準 commit>
            接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_adj4`）與 `run_corner_pk_k6b`
            之序；W3 畫面之入口（`f3_screen_adj4`）與 `f3_screen_k6b_stage3` 之序；W4 新碼⛔ 案件字面；W5 既有函式對基準
            一字未動（本單所改之三函式除外）·頂層節點之相異 ⊆ 本單之許；W6 本單所改之三函式對基準唯增列（⛔ 改既有一列）；
            W7 既有量測器之錨（其字串常數〔長 ≥ 4〕於基準之 app.py／selection_pipeline.py 恰一見者）於工作樹仍恰一見；
            基準中恰一之函式名（含巢狀）於工作樹仍恰一。（以 CC 之碼之字樣為錨之接線與突變之判別力 ＝ 復驗時補寫·另單。）
+           🔧 `W-G.9-370`：W6 許 `k953_manual_run` 之 `S219` 之停機訊息之基準二列（`W6_REPL`·逐字）易之（`K-9-57` ⑧·
+           程式自我檢查），唯此二列；其新文由 F25 之 `X5` 量之。W7 之錨之母體⛔ 含 F25（`W7_SKIP`）：其突變之錨為函式之段內
+           之錨（其恰一之判於其函式之段內·F25 之 `mutate` 自量之），⛔ 為全檔之錨。
   run      <repo> [<退縮> …]
            harness 實跑本案（預設退縮 `3.5`、`0.0`）：同一行程先設 `WV_ADJ4=off`、再去之，各跑一次：R1 第一趟之紀錄逐列 ＝
            本器所載；R2 街角第 1 宗 ＝ off 之實跑；R3 配地之變（G 之差 ＞ 容差 `0.01` 之宗、各街廓之抵費地之差）＝ 本器所載，
@@ -86,9 +91,10 @@ def _a(t):
     return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)
 
 
-def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, lose=None, calls=None):
+def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, lose=None, calls=None, tie=None, bar=None):
     """玩具之回呼（`calls` ＝ list ⇒ 每次試算附一筆）。"""
     cap, price, gmap, err_cap, lose = cap or {}, price or {}, gmap or {}, err_cap or {}, lose or {}
+    tie, bar = tie or {}, bar or {}
 
     def a_prime(src, dst):
         return _a(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)
@@ -108,6 +114,12 @@ def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, lose=None, call
         for h, (thr, lost) in lose.items():
             if h in by and float(by[h].get("面積_m2", 0) or 0) > thr + 1e-9:
                 gone.add(lost)
+        for p, lost in tie.items():                 # 🆕 `W-G.9-370`：該片離 build ⇒ 失者不保留
+            if p not in by:
+                gone.add(lost)
+        for p, lost in bar.items():                 # 🆕 `W-G.9-370`：該片在 build ⇒ 受阻者不保留
+            if p in by:
+                gone.add(lost)
         kept, bad, G, mem = {}, {}, {}, {}
         for b in build:
             p = b["暫編地號"]
@@ -144,7 +156,7 @@ _NS = {}
 
 
 def _go(*, sj=None, cap=None, price=None, drop=("X1(1)",), gmap=None, err_cap=None, lose=None, own_upd=None,
-        pre=None, lot_upd=None, temp_geom=None, geom_extra=None, geom_rm=(), calls=None, raw=False):
+        pre=None, lot_upd=None, temp_geom=None, geom_extra=None, geom_rm=(), calls=None, raw=False, tie=None, bar=None):
     t, own = _w()
     own = dict(own, **(own_upd or {}))
     by = {x["暫編地號"]: x for x in t}
@@ -160,7 +172,7 @@ def _go(*, sj=None, cap=None, price=None, drop=("X1(1)",), gmap=None, err_cap=No
     for pid, kv in (pre or {}).items():
         by[pid].update(copy.deepcopy(kv))
     build = [x for x in t if x["街廓分類"] == H]
-    ap, st = _cbs(cap, price, drop, gmap, err_cap, lose, calls)
+    ap, st = _cbs(cap, price, drop, gmap, err_cap, lose, calls, tie, bar)
     subj = [dict(SJ, **(sj or {}))] if sj is not False else []
     res = _NS["fn"](t, build, own, subj, geom, ap, st, log_print=lambda *x: None)
     return (res, t, build) if raw else res
@@ -514,8 +526,9 @@ def _cases(ns, sp):
            ("剩下", "g1", "R1(1)", REMAIN, (("R1(1)", 10.0),))],
           {"R1(1)": {"段三併出": ("Q9(1)", "X1(2)"), "段三部分併出": (("Q9(1)", 40.0), ("X1(2)", 50.0)),
                      "段三餘量": 10.0}}))
-    _run(out, "K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（其分不到之前提不成立）", lambda: _halt(lambda: _go(drop=()),
-                                                                          ["X1(1)", "分不到之前提不成立"]), ("停機", True))
+    _run(out, "K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（程式自我檢查·K-9-57 ⑧·`W-G.9-370` 之訊息）",
+         lambda: _halt(lambda: _go(drop=()), ["X1(1)", "程式自我檢查", "沿名單至街廓 BA", "依既定機制不會發生",
+                                              "觸之即程式有錯"]), ("停機", True))
     _run(out, "K10 現態之配地中止 ⇒ 停機", lambda: _halt(lambda: _go(err_cap={"BB": -1.0}), ["現態之配地中止"]),
          ("停機", True))
     _run(out, "K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ "
@@ -575,6 +588,51 @@ def _cases(ns, sp):
          lambda: _k21(ns), (True, False, False, False, True, False, False))
     _run(out, "K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st",
          lambda: _k22(ns, sp), (True, True, [], True, True, [], [], []))
+    # ── 🆕 `W-G.9-370`（`W-G.9-367 §四-2`·以 CC 之碼之突變之判別力為據·期值出自規格單 `§三`·⛔ 呼叫受測碼求期）──
+    r23 = lambda: _go(lose={"X1(2)": (150.0, "Q1(1)")}, sj={"名單": ["BB", "BD"]})  # noqa: E731
+    _run(out, "K23 R-8 之止：整體不過（他街廓之原保留之宗失·非單調之玩具）而逐片皆成 ⇒ 諸片皆無剩下 ⇒ 止於本街廓"
+              "（⛔ 往名單之次街廓 BD）",
+         lambda: (_rows(r23()), _acc(r23())),
+         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
+           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
+           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 100.0),), "成"),
+           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 200.0),), "成")],
+          {"X1(2)": 360.0}))
+    r24 = lambda: _go(tie={"X1(1)": "Q1(1)"}, sj={"名單": ["BB"]})  # noqa: E731
+    _run(out, "K24 R-9／R-10 之 T 含建地片之所屬街廓：建地片去 build 使其所屬街廓 BA 之原保留之宗失 ⇒ 整體與該片之逐片"
+              "皆不過",
+         lambda: (_rows(r24()), r24()[2][0].get("不過之由"), r24()[2][1].get("不過之由")),
+         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
+           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (), "未成"),
+           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 100.0),), "成"),
+           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 200.0),), "成"),
+           ("剩下", "g1", "X1(1)", REMAIN, (("X1(1)", 60.0),))],
+          "BA 原保留之宗 ['Q1(1)'] 不保留", "BA 原保留之宗 ['Q1(1)'] 不保留"))
+    s25 = {"名單": ["BB"], "片": ["X1(1)", "R1(1)", "R9(1)"]}
+    r25 = lambda: _go(own_upd={"R9": "g1"}, cap={"BB": 250.0}, sj=s25)  # noqa: E731
+    _run(out, "K25 R-10 之序：同類之片依剩下大者先（R9(1) 200 先於 R1(1) 100）",
+         lambda: _rows(r25()),
+         [("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
+          ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
+          ("逐片", "g1", "BB", "R9(1)", "道路", "X1(2)", (("X1(2)", 190.0),), "部分成"),
+          ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (), "未成"),
+          ("剩下", "g1", "R1(1)、R9(1)", REMAIN, (("R1(1)", 100.0), ("R9(1)", 10.0)))])
+    r26 = lambda: _go(err_cap={"BB": 200.0}, sj={"名單": ["BB"]})  # noqa: E731
+    _run(out, "K26 R-12：併入後之配地中止 ⇒ 不過（記其由）；整體不過 ⇒ 逐片（公設片取最大面積）",
+         lambda: (_rows(r26()), r26()[2][0].get("不過之由")),
+         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
+           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
+           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 100.0),), "成"),
+           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 40.0),), "部分成"),
+           ("剩下", "g1", "P1(1)", REMAIN, (("P1(1)", 160.0),))],
+          "併入後配地中止：玩具之配地中止（BB）"))
+    s27 = {"名單": ["BB"], "片": ["Q1(1)", "X1(1)", "R1(1)"]}
+    _run(out, "K27 R-10′（K-9-57 ⑧·程式自我檢查）：逐片之建地片之整筆之試之前，以當下之試算查之——前一建地片併出後該片已"
+              "為已配得之宗（依既定機制不會發生·玩具以非單調之回呼造之）⇒ 停機（⛔ 靜默併出）",
+         lambda: _halt(lambda: _go(drop=("Q1(1)",), bar={"Q1(1)": "X1(1)"}, own_upd={"Q1": "g1"}, cap={"BB": 360.0},
+                                   sj=s27), ["X1(1)", "程式自我檢查", "逐片之整筆之試之前", "依既定機制不會發生",
+                                             "觸之即程式有錯"]),
+         ("停機", True))
     return out
 
 
@@ -646,6 +704,12 @@ CHG_APP = ("k953_manual_run", "f3_screen_k6b_stage3")
 RA_SIG = ["ns", "fake_st", "cb", "cad", "param_rows", "temp_parcels", "build_parcels", "setback"]
 RA_KW = ["snapshot", "callbacks", "winners", "forced", "slices"]
 CHG_SP = ("run_corner_pk_k6b",)
+# 🆕 `W-G.9-370`：W7 之錨之母體⛔ 含 F25（突變器·其錨為函式之段內之錨·由其 `mutate` 自量之）
+W7_SKIP = ("probe_WG9370_adj4mut.py",)
+# 🆕 `W-G.9-370`（K-9-57 ⑧）：W6 之許——`k953_manual_run` 之 `S219` 之停機訊息之基準二列（逐字）得易之（唯此二列）
+W6_REPL = {"k953_manual_run": (
+    '            raise RuntimeError(f"{_hdr953} 建地片 {_x}（{_blk953[_x]}）於當下之試算已為已配得之宗 {_own953}"',
+    '                               "或其成員——K-9-53 ① 之「分不到」不立、K-9-51 之「剩餘土地」不立 ⇒ 停機")')}
 
 
 def _git_show(repo, rev, rel):
@@ -700,11 +764,13 @@ def _kw(call, name):
     return None
 
 
-def _insert_only(old, new):
-    """old → new 之差唯增列（⛔ 改、⛔ 刪既有一列）且增段 ≥ 1。回 (ok, 增段數, 說明)。"""
+def _insert_only(old, new, repl=()):
+    """old → new 之差唯增列（⛔ 改、⛔ 刪既有一列·`repl` 所列之基準之列除外〔`W-G.9-370`〕）且增段 ≥ 1。
+    回 (ok, 增段數, 說明)。"""
     a, b = old.splitlines(), new.splitlines()
     ops = difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
-    bad = [(t, i1 + 1, i2) for t, i1, i2, _j1, _j2 in ops if t not in ("equal", "insert")]
+    bad = [(t, i1 + 1, i2) for t, i1, i2, _j1, _j2 in ops
+           if t not in ("equal", "insert") and not (repl and set(a[i1:i2]) <= set(repl))]
     ins = [j2 - j1 for t, _i1, _i2, j1, j2 in ops if t == "insert"]
     return (not bad and len(ins) > 0), len(ins), f"非增之段（基準之列）{bad[:3]}"
 
@@ -818,16 +884,17 @@ def _wiring_checks(repo, base, app=None, spp=None):
         if cur is None or old is None:
             w6.append((nm, False, 0, "缺"))
             continue
-        ok_, k_, note_ = _insert_only(ast.get_source_segment(src_o, old), ast.get_source_segment(src_c, cur))
+        ok_, k_, note_ = _insert_only(ast.get_source_segment(src_o, old), ast.get_source_segment(src_c, cur),
+                                      W6_REPL.get(nm, ()))
         w6.append((nm, ok_, k_, note_))
     chk.append(("W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列"
-                "（⛔ 改、⛔ 刪既有一列）", all(x[1] for x in w6), "；".join(f"{a} {b}·增段 {c}" + ("" if b else f"（{d}）")
+                "（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）", all(x[1] for x in w6), "；".join(f"{a} {b}·增段 {c}" + ("" if b else f"（{d}）")
                                                        for a, b, c, d in w6)))
     # W7 既有量測器之錨仍恰一見；基準中恰一之函式名仍恰一
     lits8 = set()
     pdir = os.path.join(repo, "verify", "probes")
     for p8 in sorted(os.listdir(pdir)):
-        if not p8.endswith(".py") or p8 == SELF_NAME:
+        if not p8.endswith(".py") or p8 == SELF_NAME or p8 in W7_SKIP:
             continue
         try:
             with warnings.catch_warnings():
````

## 附錄乙　塊 `F23w`（`git apply` 之差異·`verify/probes/probe_WG9363_k953.py`·工項一）

````diff
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index c0bc21a..6a835e5 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -26,6 +26,8 @@
            🔧 `W-G.9-364`（⛔ 上列一字不刪）：K39 ＝ 同時點，x 於當下之試算為他街廓之已配得之宗（同歸戶、他歸戶）之成員
            ⇒ 停機；K40 ＝ 同時點，x 為本街廓之他歸戶之已配得之宗之成員 ⇒ 停機——K37 之 (ii) 之廣度（一切街廓·一切歸戶）。
            P0 隨之 40 項。
+           🔧 `W-G.9-370`（⛔ 上列一字不刪）：K36／K37／K39／K40 之停機之期改為 `S219` 之新訊息（`K-9-57` ⑧·程式自我檢查·
+           `S219_PH`）；項數⛔ 變。
   wiring   <repo> <基準 commit>
            接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_k953`）與 `run_corner_pk_k6b`
            之序（末端塊合併再試之後、以 winners／forced 呼叫、其後⛔ 重跑街角選位）；W3 畫面之入口（`f3_screen_k953`·
@@ -61,6 +63,8 @@ FN = "k953_manual_run"
 SIG = ["temp_parcels", "build_parcels", "own_map", "blocks", "centerlines", "a_prime", "alloc_state"]
 RK_SIG = ["ns", "fake_st", "cb", "cad", "param_rows", "temp_parcels", "build_parcels", "setback"]
 RK_KW = ["snapshot", "callbacks", "winners", "forced"]
+# 🆕 `W-G.9-370`（K-9-57 ⑧）：`S219`（`_wpre953`·整筆之主併入之前之查）之停機訊息之期（程式自我檢查）
+S219_PH = ("程式自我檢查", "依既定機制不會發生", "觸之即程式有錯")
 
 
 def _harvest(repo):
@@ -370,12 +374,12 @@ def _cases(ns, sp):
               "後者⛔ 與 x 相接 ⇒ 併入 G 較大者",
          lambda: _k35(),
          (("停機", True), [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 300.0),), "成")]))
-    _run(out, "K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（K-9-51 之「剩餘土地」不立）；皆非 ⇒ 併入",
+    _run(out, "K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入",
          lambda: _k36(),
          (("停機", True), ("停機", True), [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 300.0),), "成")]))
     # 🔧 補令四（⛔ 上列一字不刪）
     _run(out, "K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機"
-              "（K-9-53 ① 之「分不到」不立）；皆非 ⇒ 併入其計畫之受併宗",
+              "（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入其計畫之受併宗",
          lambda: _k37(),
          (("停機", True), ("停機", True), [("手冊", "X(1)", "a", "B1(1)", (("B1(1)", 300.0),), "成")]))
     _run(out, "K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連 ⇒ 停機"
@@ -386,11 +390,11 @@ def _cases(ns, sp):
           [("手冊", "X(1)", "a", "B1(1)", (("B1(1)", 300.0),), "成")]))
     # 🔧 W-G.9-364（⛔ 上列一字不刪）
     _run(out, "K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、"
-              "他歸戶（BD 之 D9(1)）⇒ 皆停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）",
+              "他歸戶（BD 之 D9(1)）⇒ 皆停機（程式自我檢查·K-9-57 ⑧）",
          lambda: _k39(),
          (("停機", True), ("停機", True)))
     _run(out, "K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ "
-              "停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）",
+              "停機（程式自我檢查·K-9-57 ⑧）",
          lambda: _k40(),
          ("停機", True))
     return out
@@ -517,7 +521,7 @@ def _k36():
                 return dict(r, members=dict(r["members"], **{"A1(1)": ["A1(1)", "X(1)"]}))
             return r
         return _go3((), after)
-    return (_halt2(lambda: one("kept"), ("「剩餘土地」不立",)), _halt2(lambda: one("member"), ("「剩餘土地」不立",)),
+    return (_halt2(lambda: one("kept"), S219_PH), _halt2(lambda: one("member"), S219_PH),
             [x for x in _rows(one("none")) if x[0] == "K-9-51"])
 
 
@@ -550,7 +554,7 @@ def _k37():
                 return dict(r, members=dict(r["members"], **{"A1(1)": ["A1(1)", "X(1)"]}))
             return r
         return _go4((), after)
-    return (_halt2(lambda: one("kept"), ("「分不到」不立",)), _halt2(lambda: one("member"), ("「分不到」不立",)),
+    return (_halt2(lambda: one("kept"), S219_PH), _halt2(lambda: one("member"), S219_PH),
             _sel(one("none"), "X(1)"))
 
 
@@ -590,12 +594,12 @@ def _mem4(host):
 
 
 def _k39():
-    ph = ("「分不到」不立", "「剩餘土地」不立")
+    ph = S219_PH
     return (_halt2(lambda: _mem4("D1(1)"), ph), _halt2(lambda: _mem4("D9(1)"), ph))
 
 
 def _k40():
-    return _halt2(lambda: _mem4("O1(1)"), ("「分不到」不立", "「剩餘土地」不立"))
+    return _halt2(lambda: _mem4("O1(1)"), S219_PH)
 
 
 def _k28(W):
````

## 附錄丙　塊 `F25`（新檔 `verify/probes/probe_WG9370_adj4mut.py`·工項一）

````python
# -*- coding: utf-8 -*-
"""W-G.9-370 量測器（發單側窗六十九擬·窗七十一改·檔 F25·⛔ 由受單側改一字）：規格步 4 乙之第一趟（`adj4_pass1_run`）與
手冊先行之 `GB-201` 之防護（`k953_manual_run`）——以 CC 之碼之字樣為錨之突變之判別力（`W-G.9-367 §四-2`），及 `W-G.9-370`
之改動之接線（`R-10′`、`R-22`、`K-9-57` ⑧ 之三停機訊息）。

子命令（一律 python verify/probes/probe_WG9370_adj4mut.py <子命令> …）：
  mutate <repo>
           逐突變：於其函式（`adj4_pass1_run`／`k953_manual_run`）之源碼段內，其錨恰一見 ⇒ 換之、寫出倉外之暫存檔，另一行程
           以之 harvest、跑 F24（`verify/probes/probe_WG9367_adj4.py`）之 `_cases` ⇒ 紅之集；判 ＝ 錨恰一見 且 其所指之項 ⊆ 紅之集。
           基準 M00（⛔ 突變）之紅之集須為空。
           ⛔ 列之突變：`R-12` 之「`R` 之除」（`(前保留 − R) − 後保留` → `前保留 − 後保留`）——`R-8` 之查（街廓之首）與 `R-10′` 之查
           （逐片之建地之整筆之試之前）使每一 `R ≠ ∅` 之檢核之 `R` 與其前態之已配得之宗之成員⛔ 交 ⇒ 等價之突變。
  wiring <repo> <基準 commit>
           X1 生產碼 `34` 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}；X2 app.py 之頂層節點對基準相異者 ⊆
           {adj4_pass1_run, k953_manual_run}；`adj4_pass1_run` 對基準唯增列，唯基準中訊息含 `TOK` 之 raise 之列得易；
           `k953_manual_run` 對基準之差唯在基準中訊息含 `TOK` 之 raise 之列之內（⛔ 他處增列）；X3 `def _bpre_a4(_x, _g):` 於
           `adj4_pass1_run` 恰一見、其呼叫 `_bpre_a4(_x, _g_str)` 恰一見，其前一非空列 ＝ `if _cls[_x] == '建地':`、其後一非空列 ＝
           `_c1 = _dup_a4(state)`；X4 verify/selection_pipeline.py 對基準之差恰為 `run_adj4` 之二列（`ss["t8_ownership_map"]` →
           `ss.get("t8_ownership_map", {}) or {}`）；X5 三停機訊息（`K-9-57` ⑧·程式自我檢查）：`MSGS` 之三模板各於其處（`S238` ＝
           `adj4_pass1_run` 之本體、`R-10′` ＝ 其巢狀之 `_bpre_a4`、`S219` ＝ `k953_manual_run` 之巢狀之 `_wpre953`）之 raise 之訊息
           恰一見，且二函式中訊息含 `TOK` 之 raise 皆屬之（舊訊息⛔ 存）。模板 ＝ 訊息之 f-string 之常數段逐字、其代入段
           以 `{` ＋ 式之 `ast.unparse` ＋ `}` 代之。
rc：0 相符／1 不符／2 用法錯。
"""
import ast, contextlib, difflib, io, json, os, re, subprocess, sys, tempfile, textwrap
from concurrent.futures import ThreadPoolExecutor

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

A4, K953 = "adj4_pass1_run", "k953_manual_run"
# (號, 條, 述, 函式, 錨, 換, 所指之項)
MUTS = [
    ("M01", "R-8", "受併宗之鍵：同原地號居先去之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)", {"K7"}),
    ("M02", "R-8", "受併宗之鍵：距離之序反之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0 if _same else 1, -float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)", {"K7"}),
    ("M03", "R-8", "受併宗之鍵：同距離之 G 序反之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), float(_S['G'][_h]), _h)", {"K7"}),
    ("M04", "R-8", "受併宗之鍵：末鍵（暫編地號）反之", A4,
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), _h)",
     "return (0 if _same else 1, float(adj_q2(_anc_a4.distance(_cen))), -float(_S['G'][_h]), "
     "[-ord(_c) for _c in _h])", {"K7"}),
    ("M05", "R-8", "受併宗之候選⛔ 限同歸戶", A4,
     "if str(_h) in state[\"by\"] and _gw_a4(state[\"by\"][str(_h)]) == _g_str)",
     "if str(_h) in state[\"by\"])", {"K3"}),
    ("M06", "R-8", "受併宗之成員之形改取當下之 temp 之形（GB-199）", A4,
     "_cen = _uu_a4([_orig_a4(_m, '受併宗之成員') for _m in _ms]).centroid",
     "_cen = _uu_a4([_Pg_a4(state['by'][_m]['polygon_coords']).buffer(0) for _m in _ms if _m in state['by']])"
     ".centroid", {"K12"}),
    ("M07", "R-8", "街廓之首之「建地片已為已配得」之查去之", A4,
     "if _cls[_x] == '建地' and _pos_a4(_L[_x]) and _x in _inS:", "if False:", {"K9"}),
    ("M08", "R-9", "整體成而⛔ 止", A4,
     "                    _L[_x] = 0.0\n                break\n", "                    _L[_x] = 0.0\n", {"K3"}),
    ("M09", "R-8", "街廓之首之止（諸片皆無剩下）去之", A4,
     "            if not any(_pos_a4(_L[_x]) for _x in _pcs):\n                break\n",
     "            if False:\n                break\n", {"K23"}),
    ("M10", "R-9", "live 改為全部之片", A4,
     "_live = [_x for _x in _pcs if _pos_a4(_L[_x])]", "_live = list(_pcs)", {"K4"}),
    ("M11", "R-9", "整體之併入量改以原面積（⛔ 剩下）", A4,
     "_q_all = sum(_kv_a4[_x] * _L[_x] for _x in _live)",
     "_q_all = sum(_kv_a4[_x] * _amt_a4(_tin_a4[_x]) for _x in _live)", {"K4"}),
    ("M12", "R-9", "整體之建地片⛔ 自 build 去", A4,
     "_c_all[\"build\"] = [_b for _b in _c_all[\"build\"] if str(_b['暫編地號']) not in set(_blds)]", "pass",
     {"K3", "K24"}),
    ("M13", "R-9", "整體之檢核之 T 唯本街廓", A4,
     "_ok, _why = _chk_a4(state, _c_all, {_bk} | {str(_tin_a4[_x].get('所屬街廓', '') or '') for _x in _blds},",
     "_ok, _why = _chk_a4(state, _c_all, {_bk},", {"K24"}),
    ("M14", "R-10", "逐片之類之序反之", A4,
     "_rank_a4 = {'建地': 0, '道路': 1, '公設地': 2}", "_rank_a4 = {'建地': 2, '道路': 1, '公設地': 0}", {"K4"}),
    ("M15", "R-10", "逐片之同類之序（剩下大者先）反之", A4,
     "key=lambda _y: (_rank_a4[_cls[_y]], -_L[_y], _y)", "key=lambda _y: (_rank_a4[_cls[_y]], _L[_y], _y)", {"K25"}),
    ("M16", "R-10", "最大面積之格改 0.1", A4,
     "_got = _probe_a4(_n_md / 100.0)", "_got = _probe_a4(_n_md // 10 * 10 / 100.0)", {"K4"}),
    ("M17", "R-10", "最大面積⛔ 先試全量", A4, "_whole_st = _probe_a4(_s)\n", "_whole_st = None\n", {"K13"}),
    ("M18", "R-10", "逐片之建地之檢核之 T 唯本街廓", A4,
     "_ok1, _why1 = _chk_a4(state, _c1, {_bk, str(_tin_a4[_x].get('所屬街廓', '') or '')}, {_x})",
     "_ok1, _why1 = _chk_a4(state, _c1, {_bk}, {_x})", {"K24"}),
    ("M19", "R-10", "逐片之建地片⛔ 自 build 去", A4,
     "_c1[\"build\"] = [_b for _b in _c1[\"build\"] if str(_b['暫編地號']) != _x]", "pass", {"K24"}),
    ("M20", "R-12", "原保留之宗之判去之", A4,
     "            if _lost:\n                _why.append(", "            if False:\n                _why.append(", {"K14"}),
    ("M21", "R-12", "配餘地不合格之判去之", A4,
     "if int(_sa[\"bad_pools\"].get(_t, 0)) > int(_sb[\"bad_pools\"].get(_t, 0)):", "if False:", {"K4b"}),
    ("M23", "R-12", "併入後之配地中止改為過", A4,
     "            return False, '併入後配地中止：' + str(_sa.get('err'))[:120]\n", "            return True, ''\n",
     {"K26"}),
    ("M24", "R-13", "段三併出⛔ 合既有", A4,
     "_d['段三併出'] = sorted(set(str(_y) for _y in (_d.get('段三併出') or [])) | _marks_a4[_x])",
     "_d['段三併出'] = sorted(_marks_a4[_x])", {"K8"}),
    ("M25", "R-13", "段三部分併出⛔ 合既有", A4,
     "_acc_a4 = {str(_k): float(_v) for _k, _v in (_d.get('段三部分併出') or {}).items()}", "_acc_a4 = {}", {"K8"}),
    ("M26", "R-13", "全併⛔ 去部分二鍵", A4,
     "            _d.pop('段三部分併出', None)\n            _d.pop('段三餘量', None)\n", "            pass\n", {"K8"}),
    ("M27", "R-13", "段三餘量之值誤", A4,
     "_d['段三餘量'] = round(_rm_a4, 4)", "_d['段三餘量'] = round(_rm_a4 + 0.01, 4)", {"K8"}),
    ("M28", "R-16", "施點甲（可拆分之片之最大面積之試之前）去之", K953,
     "        _gb201_953(_x, _r)              # 🆕 `W-G.9-367`（R-16）：可拆分之片",
     "        pass                            # 🆕 `W-G.9-367`（R-16）：可拆分之片", {"K15"}),
    ("M29", "R-16", "施點乙（整筆之主併入之前）去之", K953,
     "            _gb201_953(_x, _r)          # 🆕 `W-G.9-367`（R-16）：整筆之主併入之前",
     "            pass                        # 🆕 `W-G.9-367`（R-16）：整筆之主併入之前", {"K15"}),
    ("M30", "R-16", "GB-201 之判恆過", K953,
     "if not any(str(_r) in {str(_h) for _h in _hs} for _hs in (_Sg953.get(" + "\"kept\"" + ") or {}).values()):",
     "if False:", {"K15"}),
    ("M31", "R-10′", "逐片之建地之整筆之試之前之查（K-9-57 ⑧·程式自我檢查）去之", A4,
     "                    _bpre_a4(_x, _g_str)\n", "                    pass\n", {"K27"}),
]


# 🆕 `W-G.9-370`（K-9-57 ⑧）：三停機訊息之模板（逐字）。`TOK`（「已為已配得」）拆字書之，以免他器以全檔之錨（長 ≥ 4 之
# 字串常數）收之。
TOK = "已為" + "已配得"
MSGS = [
    ("S238", A4, None,
     "{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g_str}）於第一趟沿名單至街廓 {_bk} 時，當下之試算已為已配得之宗或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
    ("R-10′", A4, "_bpre_a4",
     "{_hd_a4} 程式自我檢查：建地片 {_x}（歸戶 {_g}）於逐片之整筆之試之前，當下之試算已為已配得之宗或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
    ("S219", K953, "_wpre953",
     "{_hdr953} 程式自我檢查：建地片 {_x}（{_blk953[_x]}）於整筆之主併入之前，當下之試算已為已配得之宗 {_own953} 或其成員"
     "——依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯 ⇒ 停機"),
]


def _span(src, fn):
    a = src.index("\ndef " + fn + "(") + 1
    m = re.search(r"\n(def |class |[A-Za-z_])", src[a:])
    return a, (a + m.start() + 1 if m else len(src))


def _child(repo, app):
    sys.path.insert(0, os.path.join(repo, "verify", "probes"))
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, _ = harvest(app)
    import probe_WG9367_adj4 as F
    import selection_pipeline as sp
    need = F._need(ns, sp)
    if need:
        print(json.dumps(["受詞缺"] + need, ensure_ascii=False))
        return 0
    with contextlib.redirect_stdout(io.StringIO()):
        cases = F._cases(ns, sp)
    print(json.dumps(F._report(cases, verbose=False), ensure_ascii=False))
    return 0


def mutate(repo):
    src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    tmp = tempfile.mkdtemp(prefix="wg9368mut_")
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONDONTWRITEBYTECODE="1")

    def one(m):
        mid, cl, desc, fn, old, new, want = m
        if mid == "M00":
            n, text = 1, src
        else:
            a, b = _span(src, fn)
            n = src[a:b].count(old)
            if n != 1:
                return m, n, None
            text = src[:a] + src[a:b].replace(old, new, 1) + src[b:]
        p = os.path.join(tmp, f"app_{mid}.py")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        r = subprocess.run([sys.executable, os.path.abspath(__file__), "_child", repo, p], capture_output=True,
                           text=True, encoding="utf-8", env=env)
        try:
            red = json.loads((r.stdout.strip().splitlines() or ["null"])[-1])
        except Exception:  # noqa: BLE001
            red = None
        if r.returncode != 0 or not isinstance(red, list):
            return m, n, ("例外", (r.stderr.strip().splitlines() or ["?"])[-1][:200])
        return m, n, red

    todo = [("M00", "—", "基準（⛔ 突變）", None, None, None, set())] + MUTS
    bad = []
    with ThreadPoolExecutor(2) as ex:
        for m, n, red in ex.map(one, todo):
            mid, cl, desc, fn, old, new, want = m
            if mid == "M00":
                ok = red == []
            else:
                ok = n == 1 and isinstance(red, list) and bool(want) and want <= set(red)
            if not ok:
                bad.append(mid)
            print(f"  {'✅' if ok else '🔴'} {mid} {cl}·{desc}：錨 {n} 見；紅 {red}；所指 {sorted(want)}")
    print(f"⇒ 突變 {len(MUTS)}（另基準一）；紅 {bad}；rc {1 if bad else 0}")
    return 1 if bad else 0


def _git_show(repo, rev, rel):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{rel}"], capture_output=True, check=True
                          ).stdout.decode("utf-8")


def _top(src):
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out[n.name] = ast.dump(n)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out[t.id] = ast.dump(n)
    return out


def _tpl(e):
    """raise 之訊息之模板：f-string 之常數段逐字、代入段以 `{式}` 代之；字串常數照錄；他形 ⇒ None。"""
    if isinstance(e, ast.Constant) and isinstance(e.value, str):
        return e.value
    if isinstance(e, ast.JoinedStr):
        out = []
        for v in e.values:
            if isinstance(v, ast.Constant):
                out.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                cv = {-1: "", 114: "!r", 115: "!s", 97: "!a"}[v.conversion]
                out.append("{" + ast.unparse(v.value) + cv + "}")
            else:
                return None
        return "".join(out)
    return None


def _raise_tpls(node):
    """node 之內（含巢狀）一切 `raise X(<訊息>, …)` 之訊息之模板。"""
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) and n.exc.args:
            t = _tpl(n.exc.args[0])
            if t is not None:
                out.append(t)
    return out


def _tok_raise_lines(src):
    """函式之源碼段（自 `def` 列起）中，訊息含 `TOK` 之 raise 之列之索引（0 起·該段內）之集。"""
    t = ast.parse(textwrap.dedent(src))
    lines = set()
    for n in ast.walk(t):
        if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call) and n.exc.args:
            m = _tpl(n.exc.args[0])
            if m is not None and TOK in m:
                lines |= set(range(n.lineno - 1, n.end_lineno))
    return lines


def _fn_src(src, fn):
    a, b = _span(src, fn)
    return src[a:b]


def wiring(repo, base):
    res = []
    r = subprocess.run(["git", "-C", repo, "diff", "--name-only", base, "--", "app.py", ":(glob)verify/*.py"],
                       capture_output=True, text=True, encoding="utf-8")
    chg = sorted(x for x in r.stdout.split() if x)
    res.append(("X1", f"生產碼 34 檔對基準相異者 ⊆ {{app.py, verify/selection_pipeline.py}}（相異 {chg}）",
                r.returncode == 0 and set(chg) <= {"app.py", "verify/selection_pipeline.py"}))
    a0, a1 = _git_show(repo, base, "app.py"), open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    t0, t1 = _top(a0), _top(a1)
    dif = sorted(k for k in set(t0) | set(t1) if t0.get(k) != t1.get(k))
    ok2, notes = set(dif) <= {A4, K953}, []
    for fn in (A4, K953):
        src0 = _fn_src(a0, fn)
        f0, f1 = src0.splitlines(), _fn_src(a1, fn).splitlines()
        rl = _tok_raise_lines(src0)
        ops = [o for o in difflib.SequenceMatcher(a=f0, b=f1, autojunk=False).get_opcodes() if o[0] != "equal"]
        if fn == A4:
            bad = [o for o in ops if o[0] != "insert" and not set(range(o[1], o[2])) <= rl]
        else:
            bad = [o for o in ops if not (rl and min(rl) <= o[1] and o[2] <= max(rl) + 1)]
        ok2 = ok2 and not bad
        notes.append(f"{fn}：差之段 {len(ops)}、逾許者 {[(o[0], o[1] + 1, o[2]) for o in bad][:3]}、許易之列 {len(rl)}")
    res.append(("X2", f"app.py 之頂層節點對基準相異者 ⊆ {{{A4}, {K953}}}（相異 {dif}）；" + "；".join(notes), ok2))
    body = _fn_src(a1, A4)
    lines = [x for x in body.splitlines() if x.strip()]
    nd = sum(1 for x in lines if x.strip() == "def _bpre_a4(_x, _g):")
    calls = [i for i, x in enumerate(lines) if x.strip() == "_bpre_a4(_x, _g_str)"]
    pos = (len(calls) == 1 and lines[calls[0] - 1].strip() == "if _cls[_x] == '建地':"
           and lines[calls[0] + 1].strip() == "_c1 = _dup_a4(state)")
    res.append(("X3", f"_bpre_a4：定義 {nd} 見、呼叫 {len(calls)} 見、其位 ＝ 建地之支之首 {pos}",
                nd == 1 and len(calls) == 1 and pos))
    s0 = _git_show(repo, base, "verify/selection_pipeline.py").splitlines()
    s1 = open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read().splitlines()
    d = [x for x in difflib.unified_diff(s0, s1, n=0, lineterm="") if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    want = ['-            temp_parcels, build_parcels, ss["t8_ownership_map"]):',
            '-    _own_a4 = ss["t8_ownership_map"]',
            '+            temp_parcels, build_parcels, ss.get("t8_ownership_map", {}) or {}):',
            '+    _own_a4 = ss.get("t8_ownership_map", {}) or {}']
    res.append(("X4", f"verify/selection_pipeline.py 對基準之差 ＝ run_adj4 之二列之 .get 化（差之列 {len(d)}）",
                sorted(d) == sorted(want)))
    tree = ast.parse(a1)
    tops = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    x5, ok5 = [], True
    for tag, fn, inner, tpl in MSGS:
        node = tops.get(fn)
        if node is not None and inner is not None:
            node = next((n for n in ast.walk(node) if isinstance(n, ast.FunctionDef) and n.name == inner), None)
        got = [t for t in (_raise_tpls(node) if node is not None else []) if t == tpl]
        x5.append(f"{tag} {len(got)} 見")
        ok5 = ok5 and len(got) == 1
    stray = []
    for fn in (A4, K953):
        for t in (_raise_tpls(tops[fn]) if fn in tops else []):
            if TOK in t and t not in {m[3] for m in MSGS}:
                stray.append((fn, t[:60]))
    res.append(("X5", f"三停機訊息（K-9-57 ⑧）之模板：{'、'.join(x5)}；含 TOK 而⛔ 屬模板之 raise {stray[:3]}",
                ok5 and not stray))
    red = [c for c, _, ok in res if not ok]
    for c, msg, ok in res:
        print(f"  {'✅' if ok else '🔴'} {c} {msg}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) >= 4 and argv[1] == "_child":
        return _child(os.path.abspath(argv[2]), os.path.abspath(argv[3]))
    if len(argv) == 3 and argv[1] == "mutate":
        return mutate(os.path.abspath(argv[2]))
    if len(argv) == 4 and argv[1] == "wiring":
        return wiring(os.path.abspath(argv[2]), argv[3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄丁　塊 `K13`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-57` ⑧ 之落地：「併出前發現該建地已可配地」之三停機改列程式自我檢查；規格步 `4` 乙（第一趟）之逐片之建地片之查（`W-G.9-370`·⛔ 上文一字不刪·純末端追加）

**註**（發單側窗七十一·`2026-10-07`·【工】·⛔ 充裁·⛔ 新域問）：依 `K-9-57` ⑧（KL `2026-10-05 09:17` 第 `5` 點），已不能分配之建地片，依既定之配地機制⛔ 因他片之併出而變為可配地。程式於下列三處以當下之試算查「該建地片已為已配得之宗或其成員」，觸之即程式有錯而停機——**程式自我檢查，⛔ 為土地之情形、⛔ 呈為土地之題**：
- ① 手冊先行（`K-9-53` ①）之逐片之整筆之主併入之前（盤點 `S219`·既有之查·其訊息改列）；
- ② 第一趟（`K-9-53` ②）沿名單至每一街廓時（盤點 `S238`·既有之查·其訊息改列）；
- ③ 第一趟之逐片，每一建地片之整筆之試之前（新增之查·`W-G.9-370` `R-10′`）——② 之查於此未及：同一街廓內前一建地片併出後，當下之態已變。
三處之停機訊息皆首揭「程式自我檢查」，並載「依既定機制不會發生（K-9-57 ⑧），觸之即程式有錯」（`K-9-57` ⑧ 之語）；⛔ 再以「分不到之前提不成立」「『分不到』不立」「『剩餘土地』不立」為停機之由。
**與既有正典之關係**：上開「`K-9-56` 之立」節之工程讀法丑（停機）之首款「建地片於當下之試算已為已配得之宗或其成員」，其性質自此讀為程式自我檢查（`K-9-57` ⑧），其施點及於 ③。發單側窗六十九之舊 `W-G.9-368` 規格單（未入倉）之同形之補（以「分不到之前提不成立」為停機之由）⛔ 採（`自誤 582`、`自誤 584`）。
**本案之量**：⛔ 變（三處於本案皆⛔ 觸；第一趟之受詞唯道路片一·⛔ 經建地之逐片）。
**落地狀態**：🔶 側支 `verify/W-G.9-370-selfchk`（`W-G.9-370` 工項二）；入主線另候 KL 之畫面核對與放行。上開「`K-9-57`〜`K-9-63` 之立」節之 `K-9-57` 之落地狀態「⑧ 之 `S219`、`S238` 之改列 ⬜」⇒ 🔶（同上）。
````

## 附錄戊　塊 `G11`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-202` 之立；`GB-203` 之號之焚（`W-G.9-370`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-370-selfchk`（`W-G.9-370` 工項三·起於主線 `3b35daad5fbf1749b7b596b0013575ec4388202d`）；主線⛔ 變。**取號**（`W-G.9-370 §零-1`）：`GB-202` 於 `3b35daa` 之命中 `4` 列（母體 ＝ 追蹤檔·列框·`git grep -c -F`），皆本項之預告（`CLAUDE.md` 待落地清單、`docs/orders/W-G.9-369_中量單.md`）⇒ 取之。

### `GB-202` 🆕　**harness 未建模街廓之最小建築面積之有效值（`K-9-1` 裁丙）：凡試算皆以 `eff_min_build_by_blk={}` 跑，畫面則取 `K91_SS_MBA_EFFECTIVE` ⇒ 以最小建築面積為鍵或為驗之處，二路徑可異而 parity ⛔ 察**

**受詞**：harness——`verify/selection_pipeline.py` 之試算（字樣錨 `eff_min_build_by_blk={})`·四處）、`verify/run_verification.py` 之一處、`verify/stepg_pipeline.py` 之「主跑二情境為 `{}`」之註（`W-G.9-247` 起）；`run_adj4` 予 `adj4_plan` 之 `eff_min_build_by` 為 `{}`（`W-G.9-367` `R-17`）。畫面——`f3_screen_adj4` 與 `W-G.9-359` 之候選名單區塊（`main()`）皆讀 `K91_SS_MBA_EFFECTIVE`。
**情形**：受詞為建地軌時，`adj4_plan` 之名單之序（五級之第二鍵 `r2`·最小建築面積）於二路徑可異；`_lot_gate` 之面積驗亦然。量測器 `F4 parity` 之畫面 session ⛔ 設 `K91_SS_MBA_EFFECTIVE`，`.get` 後為 `{}`，恰與 harness 同 ⇒ 缺口被遮。CC 之唯讀獨立審查（`docs/reports/W-G.9-367R_規格步4乙第一趟_執行報告.md` ⑥-2 (C) `6`）所揭。
**實測**：本案⛔ 觸（第一趟之受詞唯公設軌·`F24 run` 之 `R1` 之 `軌` ＝ `公設軌`）。
**與配地之關係**：畫面為準；harness 之名單與驗可與之異 ⇒ 驗證之結論⛔ 及於「街廓有最小建築面積之規定、且受詞為建地軌」之案。
**失效條件**：harness 以 `k91_effective_min_build_area` 自案件參數求各街廓之有效值並傳入諸試算與 `adj4_plan`；或 `F4 parity` 之畫面 session 注入同值而二路徑之名單逐列同。
🔒 **排程**：另單（⛔ 急·本案⛔ 觸·純工程·⛔ 新域問）；最遲於第一個建地軌之受詞出現之單之前。

**`GB-203` 之號**：`K-9-57` ⑧ 記「⛔ 立 `GB-203`」（發單側窗六十九呈 KL 之題之前提⛔ 成立·`自誤 582`）；其號已見於 `K-6` 典、`CLAUDE.md`、`docs/orders/W-G.9-368_輕量單.md`、`docs/orders/W-G.9-369_中量單.md` 與自誤簿（見 `W-G.9-370 §零-1`）⇒ **視同已焚，⛔ 另作他用**；本簿之次號自 `GB-204` 起。其所指之情形依 `K-9-57` ⑧ 改列程式自我檢查（`K-6` 典「`K-9-57` ⑧ 之落地……」節）。
````

## 附錄己　塊 `E13`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-370 §零-1`）：本批取 `584`〜`587`（`4` 號）——發單側窗六十九所擬之舊 `W-G.9-368` 規格單（`69486` B·`sha256` `ecf0ac40bf0c0c1289b5be0abddae793de0a92596fe4737215174d4dee3d1132`·未入倉）所擬之三則（其舊號 `580`／`581`／`582` ⛔ 沿用·`W-G.9-369` 塊 `E12` 之取號節）之改寫（`584`〜`586`），及發單側窗七十一擬 `W-G.9-370` 時自察之一則（`587`）。

### 🩸 `自誤 584`　**`W-G.9-367` 規格單之程式自我檢查之施點未全：「建地片於當下之試算已為已配得之宗或其成員 ⇒ 停機」唯於沿名單之每一街廓之首查之（`R-8`），⛔ 推及逐片之每一建地片之整筆之試之前（`R-10`）；手冊先行之同形之查（`_wpre953`）則每施點皆查**

**形**：`R-10` 之建地片依序逐一整筆試併；前一建地片之併出改當下之態，而規格⛔ 令其後之片之試之前再查。其檢核（`R-12`）以 `R ＝ {x}` 除之，故該片若已為已配得之宗，檢核⛔ 察之。
**後果之界**：依 `K-9-57` ⑧，已不能分配之建地片⛔ 因他片之併出而變為可配地，其情形唯程式有錯時始生；施點未全 ⇒ 程式若有錯，第一趟將靜默併出而⛔ 停機（自我檢查之漏）。本案之配地零（受詞唯道路片一·⛔ 經建地之逐片）。
**與 `582` 之界**：`582` ＝ 將本形呈 KL 為土地之題（其前提⛔ 成立·🟠）；本則 ＝ 程式自我檢查之施點之漏（🟡），其補（`W-G.9-370` `R-10′`）⛔ 涉土地之判斷。舊稿之同則以「分不到之前提⛔ 立之建地片被併出 ⇒ 錯配」書其後果，係 `582` 之誤之延續，本則⛔ 採。
**根因**：擬 `R-8`／`R-10` 時，`自誤 573`〜`575` 之通則（計畫或判取自前態、施於當下之態者，於每一施點查之）唯施於 `R-16`（`GB-201` 之防護），⛔ 全掃第一趟自身之施點。
**後果之框**：🟡 規格之漏一則；碼依規格。攔點 ＝ 發單側窗六十九（`W-G.9-367 §四-2` 之復驗·突變 `R-12` 之「`R` 之除」之等價之查）。
**攔法**：`W-G.9-370` `R-10′`（`_bpre_a4`）、量測器 `F24` 之 `K27`、`F25` 之 `M31`／`X3`／`X5`。通則：規格中凡「於某時點之試算查某性質」之停機款，逐一列其施點；施點之間當下之態可變者，每施點各查之。

### 🩸 `自誤 585`　**交接文六十八（倉外·⛔ 入倉）之待辦 `2`（逐字「§四-2 復驗補寫：以 CC 碼之字樣為錨之突變（可由 F24 之 f24_internal 重生）。」）所稱之 `f24_internal` 於倉內⛔ 存**

**形**：發單側窗六十九於 `7c4ecc2` 以 `git grep -n "f24_internal"`（母體 ＝ 該態之追蹤檔全部）得 `0` 列；`verify/probes/probe_WG9367_adj4.py` 之頂層與巢狀之名皆⛔ 含之。發單側窗七十一於 `3b35daa` 重查亦 `0`。交接文以倉外之物為下窗之工具。交接文之原文經發單側窗七十一回對話（窗六十九·KL 所貼之交接文）核之。
**後果之界**：零（窗六十九另擬突變之器 `F25`·入倉於 `W-G.9-370` 工項一）；交接之可承性之減一則。
**根因**：發單側之量測之器未入倉而交接文引之（已登之常見型「發單側之量測之器⛔ 入倉」之再見）。
**後果之框**：🟡 交接文一處之指涉⛔ 存。攔點 ＝ 發單側窗六十九（開窗後之全倉搜）。
**攔法**：通則：交接文所引之器、檔、函式，須具名其倉內之路徑與其所在之 `commit`；倉外之物⛔ 得為下窗之待辦之前提。

### 🩸 `自誤 586`　**`W-G.9-367` 規格單 `R-18` 之字面令畫面以 `session_state[鍵]` 直取 `t8_ownership_map`、`K91_SS_MBA_EFFECTIVE`、`SS_FRONT_ROAD_DERIVE`、`SS_FRONT_ROAD_NAME`，而同單之量測器 `F4 parity` 之畫面 session ⛔ 設後三鍵 ⇒ 規格之字面與其量測器互斥；`R-17` 令 harness 直取 `t8_ownership_map`，與其同鏈之鄰（`run_k953`、段三）之 `.get` 不一**

**形**：CC 取 `.get(鍵, {}) or {}` 以過器（`docs/reports/W-G.9-367R_規格步4乙第一趟_執行報告.md` ⑦-2 項 `7`·⑥-2 (C) `1`）；harness 依字面直取 ⇒ 二路徑之讀法不對稱。
**後果之界**：零土地後果（鍵在時二讀法逐位同；harness 恆寫 `t8_ownership_map`）。
**根因**：擬 `R-17`／`R-18` 時⛔ 查既有之讀法（`app.py` 讀 `t8_ownership_map` 皆 `.get`；`verify/selection_pipeline.py` 之 `run_k953`／段三亦然）與 `F4` 之畫面 session 之鍵。
**後果之框**：🟡 規格之字面一則與其器互斥（常規二）。攔點 ＝ CC（取能過器之形）與其唯讀獨立審查。
**攔法**：`W-G.9-370` `R-22`（harness 二列之 `.get` 化）與 `F25` 之 `X4`；`R-18` 之字面以 `W-G.9-370 §二` 改讀為 `.get` 形。通則：規格令讀 session 之鍵者，先查同檔同鏈之既有讀法與量測器之 session 之鍵。

### 🩸 `自誤 587`　**舊 `W-G.9-368` 規格單（發單側窗六十九·未發）`§一` 項 `5`／`6` 載量測器 `F24` 之 `wiring <repo> d7a5ea4` 於工項一之端與施後皆 `rc 0`——實則新器 `F25` 入 `verify/probes/` 後即為 `F24` 之 `W7` 之錨之母體之一員，其錨 `5` 個於基準 `d7a5ea4` 之 `app.py` 恰一見而於工作樹二見以上 ⇒ `W7` 紅**

**形**：`W7` 之錨 ＝ `verify/probes/*.py`（`F24` 自身除外）之字串常數〔長 ≥ 4〕中，於基準之 `app.py` 恰一見者，須於工作樹仍恰一見。舊 `F25` 之突變之錨取自 `adj4_pass1_run`（`W-G.9-367` 新增），其中與 `k953_manual_run` 同形之碼四（`if _lost:` 繼以 `_why.append(`；`return False, '併入後配地中止：'…`；`if int(_sa["bad_pools"]…`；`_d.pop('段三部分併出', None)` 繼以 `_d.pop('段三餘量'…`）於 `d7a5ea4` 恰一見、於 `7c4ecc2` 二見；條名 `'R-16'` 於 `d7a5ea4` 恰一見、於 `7c4ecc2` 四見。發單側窗七十一於拋棄式 worktree（`7c4ecc2` ＋ 舊塊 `F24t` ＋ 舊塊 `F25` 置於 `verify/probes/probe_WG9368_adj4mut.py`）實跑 `python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` ⇒ 末列 `⇒ 紅 ['W7']；rc 1`；去該檔 ⇒ `⇒ 紅 []；rc 0`。
**後果之界**：舊單⛔ 發（KL `2026-10-05` 令暫緩）⇒ 零。若發，CC 於工項二之前置即觸停機款。
**根因**：擬新器時⛔ 以「既有量測器之錨」之全倉之母體重跑既有之接線檢查——新器入倉即為其母體之一員；`§一` 之原型之量測⛔ 置新器於其最終之路徑。
**後果之框**：🟡 單之態錨二項失準（未生效）。攔點 ＝ 發單側窗七十一（擬 `W-G.9-370`·於拋棄式 worktree 以最終之路徑重跑）。
**攔法**：`W-G.9-370` 塊 `F24t` 之 `W7_SKIP`（突變器之錨為函式之段內之錨，其恰一之判由其 `mutate` 自量之，⛔ 為全檔之錨）。通則：新增量測器之單，其「工項一之端」之諸器之態，須於新器置於最終之路徑後實跑；新器之字串常數須查其是否成為他器之錨之母體。
````

## 附錄庚　塊 `P23`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：`K-9-57` ⑧ 之三停機改列程式自我檢查、第一趟之突變之判別力之補寫、harness 之讀法之一致入側支（`W-G.9-370`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-370-selfchk`（`W-G.9-370` 之五 `commit`·起於主線 `3b35daad5fbf1749b7b596b0013575ec4388202d`）；主線⛔ 動。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-57` ⑧（「併出前發現該建地已可配地」改列程式自我檢查） | `S219`、`S238` 之停機訊息之改列；第一趟之逐片之建地片之查（`R-10′`·`adj4_pass1_run` 之 `_bpre_a4`）；量測器 `F24` 之 `K9`／`K27`、`F23` 之 `K36`／`K37`／`K39`／`K40`、`F25` 之 `X5` | 🔶（側支） | `docs/orders/W-G.9-370_規格單.md` |
| `2` | `W-G.9-367 §四-2` 之補寫（以 CC 之碼之字樣為錨之接線與突變之判別力） | `F24` 增 `K23`〜`K27`；新器 `F25`（`verify/probes/probe_WG9370_adj4mut.py`·突變 `30`·接線 `X1`〜`X5`） | 🔶（側支） | 同上 |
| `3` | harness 之 session 之讀法（`自誤 586`） | `run_adj4` 二列之 `.get` 化（`R-22`） | 🔶（側支） | 同上 |
| `4` | `GB-202`（harness 之最小建築面積之有效值） | — | ⬜ | `GB` 簿 `GB-202` |
| `5` | 序 `1`〜`3` 之入主線 ＋ KL 之畫面核對 ＋ 主 checkout 之同步 | 配地⛔ 變 ⇒ 核對之紀錄逐列同 | ⬜（候 KL 放行） | 次單 |
| `6` | `自誤 584`〜`587` | 見自誤簿 | 🔶（側支） | 同序 `1` |

🔒 **前節之更新**（⛔ 追改前節一字）：前開「待落地清單之更新：規格步 `4` 乙（第一趟·`K-9-56`）與 `K-9-57`〜`K-9-63` 入主線；`GB-201` 之解除」節之序 `4` ⇒ 本節序 `2`、`3`、`4`（其「改列程式自我檢查」之部 ⇒ 本節序 `1`）；其序 `7` ⇒ 本節序 `1`；其餘各序之態⛔ 變。
🔒 **本案之量**：本批⛔ 變配地（三停機於本案皆⛔ 觸；`.get` 化於鍵在時逐位同）。
🔒 **依賴序**：本批 → 序 `5`（次單）→ 前節序 `6`（弱弱聯合之實測）→ `K-9-58`〜`K-9-63` 之落地之單（其序另呈 KL）→ 規格步 `5` → `6` → `7`／`8`；`GB-196`、`GB-197`、`GB-198`、`GB-202` 另單（⛔ 急）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `6`（子字串框·含圖例與本列）·列 ＝ `4`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: edada37831ff9956cd60f41bf701ef07dffaadfbbc8b5c16f53959e05a1fb638
