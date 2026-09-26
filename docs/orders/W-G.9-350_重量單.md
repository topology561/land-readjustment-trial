# `W-G.9-350`　重量單：正面道路識別符（五級八鍵之 `r3`·幾何推導 ∪ 區外道路清單）之落地 ＋ 攢批登記 ＋ `GB-178` 之進度（四）（`R6` `85.71 ㎡` 之成因具名）＋ 待落地清單之更新 ＋ 主 checkout 同步之撞檔前置

> **發單** ＝ 發單側窗四十六·`2026-09-27`（**第 `2` 版**·取代同名之第 `1` 版〔`74747` B·`sha256` `9160ec810cd7ca2f…`·無塊 `G3`〕；受單側所持者為第 `1` 版 ⇒ 停機款 `2`）。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**；工項五於 **KL 之主 checkout**）。
> **級** ＝ **重**（生產碼 `1` 檔：`app.py`；**⛔ 土地後果**——配地之出艙改前改後逐位同，見 `§一` 項 `7`／`8`／`9`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `981fd1fc09a9fd22484bd3deeadd8a40be1e4a5e`。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D1`／`F9`／`E3`／`G3`／`P4` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）。
> 🔑 **來源檔一**（檔名逐字 `W-G.9-350_重量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項五之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F9`）與改動（`D1`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：塊 `D1` 以外之生產碼一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`K-6` 典／`VR` 簿；`GB` 簿除塊 `G3` 之末端追加外之一字；任何側支之刪除或改寫。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `981fd1fc09a9fd22484bd3deeadd8a40be1e4a5e`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 541 537` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔 **`901`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗四十六實跑 `python verify/probes/wg9268_gate6_occupancy.py 981fd1f W-G.9-350 W-G.9-349 W-G.9-398`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-350`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-349` | `2`／`10`／`3` | `2`／`10`／`3` | `13` | `4` | `5`／`51` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`3` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `8`／`8` | 🟢 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態之追蹤檔·錨定框 `(?<![0-9\-])<號>(?![0-9])`·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取）：

| 號 | 裸（錨定）列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 542`〜`545`（逐號） | 皆 `0` | 皆 `0` | 皆 `0` | 🟢 可取 |
| 對照甲［必非零］`自誤 541` | `4` | `0` | `4` | 🟢 C 形非空（B 形於本倉為量測器紅·`GB-158`） |

自誤 `MAX` ＝ `541`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 542`〜`545`；⛔ 鑄 `GB`／`VR`／`K-9`（塊 `G3` 係 `GB-178` 之進度·⛔ 新號）。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `981fd1f`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`F9`／`E3`／`G3`／`P4` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二前置之任一期不符（尤：`F9` 三子命令之施前 `rc ≠ 1`） |
| `5` | 塊 `D1` 之 `git apply --check` 不過；或施後之 blob ≠ `§五-1` 項 `7` |
| `6` | 工項二之驗 `V-1`〜`V-5` 任一 ≠ 期（尤：`V-2` 之配地出艙改前改後有任一位元組相異；`V-5` 之相異項 ≠ `0`，或 `cmp` 之異列有非時戳／耗時者） |
| `7` | 工項二之 `push` 無 `§二` 之放行；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項三之三檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項五：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒 |
| `11` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `12` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗四十六自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `981fd1fc09a9fd22484bd3deeadd8a40be1e4a5e`；側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`30`**（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼（開工態 blob） | `app.py` `8672b00d9b76f77c0cb3b9ca1487a42486d53653`（`1506634` B） |
| `3` | `W-G.9-349` 之復驗 | 發單側窗四十六依交接文四十五 `§四-1` 逐項自倉重跑：逐 `commit` 對拍（單 ＝ 所發之檔；`F8`／`D1`／`E2`／`G2`／`R1`／`P3` 逐位同）、施後三 blob、四檔 bytes 與嚴格前綴、收工閘 `1`〜`13`、`run_all` 二態（`762358d` 對 `5eeb95f`·同一倉外路徑）——**全數相符** |
| `4` | 本批之受詞（五級八鍵之 `r3`） | `docs/配地計算總規格_v3.md` 之「🔧 §7-1 級1/2/3 與 §7-4 之**區位順序**改採「五級（八鍵詞典序）」」節 ③（要旨：`r3` 正面道路相同為 `0`、否為 `1`；識別符 ＝ 幾何推導 ∪ 區外道路清單；幾何推導有值時使用者⛔ 覆寫、區外道路清單只填推導之空缺·KL 裁 `2026-09-05`）；幾何推導之定義 ＝ `CLAUDE.md`「🔧 道路側推導之幾何定義（`W-G.9-235` 工項一 `c`）」節；資料前提 ＝ `W-G.9-248` 之「正面道路名稱／識別符」欄（`SS_FRONT_ROAD_NAME`·迄今無消費端）；依賴序 ＝ `CLAUDE.md`「🔧 待落地清單之更新：閘二…（`W-G.9-349`）」節 |
| `5` | 改後之推導（harness·塊 `D1` 施後·`F9 run`） | 見下表；`R1`／`R4` ＝ 區外（區內道路沿其正面線者最多 `4.20%`／`3.75%`），餘四街廓各恰一道路（`96.04%`〜`96.46%`）；外部錨（`line ∩ polygon.buffer(1.0)`）之分類六街廓九對全同 |
| `6` | 施後 blob | `app.py` `3ea96402e032f8f19f1af367d3428d16b5458bba`（`1518340` B·增 `196`／刪 `0`·純加性） |
| `7` | 配地⛔ 變（量測器 `F8` 之 `run`） | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5`／`… 0.0` 於工項一之端與工項二之 `commit` 各跑一次：二退縮之全部出艙**逐位相同**（`cmp`）；`rc 0`·末列 `⇒ 紅 []；rc 0` |
| `8` | 畫面對 harness（`verify/probes/probe_WG9345_screen.py parity <R> <退縮> on`） | 施後：`3.5` ⇒ `rc 0`（配地列 harness `36`／畫面 `35`·不符格 `0`）；`0.0` ⇒ `rc 0`（`37`／`36`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（同 `W-G.9-349 §一` 項 `8`） |
| `9` | `run_all`（同一倉外路徑·工項一之端 對 工項二之 `commit`） | 二份全檔**逐位相同**（`cmp`）：`64` 項·PASS `28`／FAIL `36`·對帳段「名目：凍存 `22`／現況 `36`」；工項一之端之一份與 `W-G.9-349` 工項二之 `commit`（`5eeb95f`）之一份亦逐位同 |
| `10` | `GB-178` 之 `R6` `85.71 ㎡`（塊 `G3`、`E3` 之 `自誤 544`／`545` 之所據·發單側倉外實量·CC 之工項⛔ 及之） | `python verify/probes/wg9309/chk_wg9309.py <repo> 甲 3.5 <out.json>` 於 `babc64d`／`88dc179`／`981fd1f` 三態：片 `R6-抵費地-2` 之 `cut_coords` 逐位同（`85.706388 ㎡`·首頂點 ＝ `R6` 之 FRONT_LINE 端點 `p1`）；其 `47.68 m` 邊與左側推進之第 `1` 宗之近側界重合（Hausdorff `5.8e-10 m`·精確交集長 `0`）；以 `_verbose=True` 包裹 `_pool_strips_for_block` 之 `[T2-DIAG]`：`R6` 之 `s` 域 `[-3.6068, 85.8549]`、池帶首項 `s` 寬 `3.6068`／面積 `85.7064`、步驟 `5b`（幾何餘）無出艙 |

**`§一` 項 `5` 之表**（harness·比值 ＝ 該道路街廓與正面線之重疊長 ÷ 正面線長）：

| 街廓 | 正面線長（m） | 候選（重疊長 m／比值） | 狀態 | 識別符（區外道路清單為空時） |
|---|---|---|---|---|
| `R1` | `87.3131` | `RD1` `3.6682`／`4.20%`；`RD2` `3.3826`／`3.87%` | 區外 | （未填） |
| `R2` | `100.0274` | `RD1` `96.4832`／`96.46%` | 成功 | `RD1` |
| `R3` | `93.4051` | `RD2` `89.8392`／`96.18%` | 成功 | `RD2` |
| `R4` | `98.8938` | `RD2` `3.7114`／`3.75%`；`RD3` `3.5440`／`3.58%` | 區外 | （未填） |
| `R5` | `92.7995` | `RD2` `89.3363`／`96.27%` | 成功 | `RD2` |
| `R6` | `85.8549` | `RD3` `82.4534`／`96.04%` | 成功 | `RD3` |

---

## `§二`　KL 之語與射程

🔒 **KL 之語（`2026-09-27 05:39`·發單側窗四十六·逐字）**：「下一步」——所答者為發單側窗四十六前一則覆命之末句「本窗次一步即擬此單；您本機之同步不影響擬單之進行。」（其「此單」＝ 同則「五、次一實質：正面道路識別符」所述）。
🔒 **KL 之既裁（`2026-09-05`·五級·見 `§一` 項 `4`）**：`r3` 之識別符 ＝ 幾何推導 ∪ 區外道路清單；推導有值時使用者⛔ 覆寫；清單只填推導之空缺；`R1`／`R4` 臨同一條區外道路、指向同一項（`docs/orders/交接文_W-G.9-238.md` 之「`(三)` 之識別符」款）。
🔒 **KL 之語（`2026-09-27`·`R6` 之詢問·發單側窗四十六·逐字）**：「在執行app.py時，G值迭代之分配成果發現(上傳截圖) R6在末端塊部分(R6街廓左側，無SIDELINE側)，有塊85.7㎡未臨路之抵費地，該部分是程式尚未修改至此部分?」；KL 同訊息轉貼他窗之答覆，其末逐字「建議請另一個視窗在下一張單順便補登進 GB-178 的進度。這件事不動程式、不影響土地配置。」⇒ 塊 `G3`（`GB-178` 之進度（四）·純登記·⛔ 解除、⛔ 收窄）與塊 `E3` 之 `自誤 544`／`545`（`§一` 項 `10`）。
🔒 **本單之讀法**（發單側之工程裁·⛔ 域裁·本案三者皆⛔ 生差異；已以通知呈 KL）：
① 「沿線過半」**逐候選**量之——某一道路街廓**自身**之重疊長 ÷ 正面線長，**嚴格大於**具名常數 `R3_FRONT_ROAD_MAJORITY`（`0.5`）者入推導集；⛔ 以諸候選之合計量之（合計之讀法於「一條正面線橫跨二道路街廓」時使二者俱入而成歧義；逐候選之讀法使其落入區外、由清單指派）。
② 候選 ＝ **非可建築土地**之街廓（與 `parse_cad_precision_layers` 綁定所用之 `_buildable_blocks` 同一判準之補集·⛔ 分區名字面）。
③ 區外道路清單之載體 ＝ `W-G.9-248` 之「正面道路名稱／識別符」欄；名稱之正規形 ＝ `NFKC` ＋ 去首尾空白 ＋ 連續空白併一；**識別符字串相同即同一正面道路**——使用者於區外者填某區內道路街廓之名稱（如 `RD2`）即視為與之同一條道路。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項二之生產碼 `commit` 推入主線之放行，CC 將其逐字載入報告；**無之 ⇒ 工項二之驗畢後停於推送前，於對話請示 KL**。所答之【要你判斷】逐字：「同意將『正面道路識別（由圖推導每一街廓臨哪一條區內道路；推導不出者由您於畫面填名）』之程式推入主線嗎？此改動不改變任何配地結果。（是／否）」

🔒 **逐筆放行清單**：本批動生產碼者恰 **`1`** 筆（工項二）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `app.py`（`parse_cad_precision_layers` 之初值鍵、FRONT_LINE 綁定迴圈之頂點留存、推導之呼叫；新 module 級常數 `R3_FRONT_ROAD_MAJORITY`／`SS_FRONT_ROAD_DERIVE`／`R3_STATUS_*` 與函式 `r3_front_road_derive`／`r3_normalize_road_name`／`r3_front_road_identifier`／`r3_front_road_caption`／`r3_front_road_rows`；`main()` 之 session 寫入、步驟 E 之卡片說明句與「🧭 正面道路識別」一覽） | 塊 `D1` | ⛔ 無（`§一` 項 `7`／`8`／`9`） |

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至主線；`(b)` 工項二之 `push` 以本節之放行為條件；`(c)` 工項五於 KL 本機之主 checkout·⛔ `commit`；`(d)` ⛔ 及其他任何生產碼、任何他錨；`(e)` ⛔ 建 `r3` 之消費端（新調配模組另單）；`(f)` 塊 `G3` ⛔ 動生產碼、⛔ 動任何配地（`K-9-36` 之落地候新調配模組）。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-350_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-350 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F9` 入倉（主線·零生產碼）

塊 `F9` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9350_frontroad.py`（**新檔**）。`commit` 訊息逐字 `W-G.9-350 工項一：量測器 F9（正面道路識別符）入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項二　塊 `D1`：正面道路識別符之落地（🔴 生產碼·一 `commit`·⛔ 土地後果）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9350_frontroad.py selftest <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
2. `python verify/probes/probe_WG9350_frontroad.py wiring <repo>` ⇒ **`rc 1`**（`W1`〜`W3c` 與 `W5` 皆紅、`W4` 綠；突變 `N1`／`N2`／`N4`「突變錨不存在」、`N3` 轉紅 `['W4']`）。
3. `python verify/probes/probe_WG9350_frontroad.py run <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D1` 依圍欄之逐列索引抽出為 `<O>\D1.diff`、對拍 `§五-1` 後，`git apply --check <O>\D1.diff` ⇒ 過；`git apply <O>\D1.diff`；`git hash-object app.py` ＝ `3ea96402e032f8f19f1af367d3428d16b5458bba`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-350 工項二：正面道路識別符（五級 r3·幾何推導 ∪ 區外道路清單）之落地 🔴 生產碼（⛔ 土地後果）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `S1`〜`S11`、`I1`〜`I8`、`M0` 皆 ✅，`M1`〜`M3` 皆「轉紅」；`wiring` 之 `W1`〜`W5` 皆 ✅，`N1`〜`N4` 皆「轉紅」 |
| `V-2` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `cmp` | 皆 **`rc 0`**；**`cmp` 皆逐位相同**（配地⛔ 變；發單側 Linux 實測如此·該器之出艙⛔ 含路徑與時戳） |
| `V-3` | `python verify/probes/probe_WG9350_frontroad.py run <repo>` | **`rc 0`**；逐街廓之狀態與推導 ＝ `§一` 項 `5` 之表；`R4` 外部錨九對皆 ✅；「組」＝ `正面道路「RD1」：R2；正面道路「RD2」：R3、R5；正面道路「RD3」：R6`；「待填」＝ `['R1', 'R4']` |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35.json`；同 `0.0`；`python verify/probes/probe_WG9348_harvest_key.py <repo>`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>`；`python verify/probes/probe_WG9340_main_synth.py <repo>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；`parity` ＝ `§一` 項 `8`；`wfns_ast` `43`／`43`／`42`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」 |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `cmp <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`cmp` 期逐位相同（發單側 Linux 實測如此）——若不同，出艙其全部異列：異列皆為時戳／耗時者屬白名單 `8`（自解），否則停機款 `6` |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（`§二` 之放行成立後·與驗為分開之呼叫）：`git push origin HEAD:wip/s1-endpart`。

### 工項三　攢批登記 ＋ `GB-178` 之進度（四）＋ 待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `E3`／`G3`／`P4` 各依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位**附於**：
- `E3` ⇒ `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；
- `G3` ⇒ `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；
- `P4` ⇒ `CLAUDE.md` 之末。

三檔之刪除欄皆 `0`、改前全檔為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-350 工項三：攢批登記（自誤 542〜545）＋ GB-178 之進度（四）＋ 待落地清單之更新（正面道路識別符）⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項四　執行報告入倉（主線·新檔 `docs/reports/W-G.9-350R_正面道路識別符_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F9` 三子命令之全文、`F8 run` 二份之 `cmp` 結果、`parity` 二份之 `rc` 與末三列、`runall` 對拍之全文與 `cmp` 結果）；④ 五塊之實得（bytes／`sha256`）與三檔之改前改後 bytes；⑤ `§二` 之放行（KL 之逐字或請示之經過）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-350 工項四：執行報告入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項五　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542` 之攔法·分開之呼叫）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、逐檔出艙其路徑、二 blob 與處置；`A ∩ U` 為空者出艙「空」。
   🔒 KL 主 checkout 之現態未經發單側實查：KL `2026-09-27` 所轉貼之他窗答覆載 KL 畫面之 `K-9-29 六` 合併紀錄與 `W-G.9-349` 版相符（間接之證）。若仍在 `88dc179`，其 `docs/orders/W-G.9-349_重量單.md` 之未追蹤複本即落於 `A ∩ U`；本單之複本若置於主 checkout 之 `docs/orders/`，亦落於 `A ∩ U`——皆依丙處置之，⛔ 預設其態。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項四 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `3ea96402e032f8f19f1af367d3428d16b5458bba`。
任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項四之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 逐檔 **`0`**（工項二 ＝ `app.py` 增 `196`／刪 `0`） |
| `2` | 生產碼 `34` 檔對 `981fd1f` | 相異恰 **`1`**（`app.py` ＝ `3ea96402…`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`7` 檔） |
| `4` | 三檔之 bytes | `docs/reports/W-G.9波_claude.ai側自誤登記.md` `1064143 → 1072508`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1013686 → 1019048`；`CLAUDE.md` `268881 → 272943`；三者改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`30`**；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 545 541 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 545 541` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `530`／`MAX` `545`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `186`／`193`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `45`／`48`／`[44, 47]`（缺號集皆 ＝ 開工態） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·`43`／`43`／`42` |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之替身 ＋ 塊 `F9` ＋ 塊 `D1` ＋ 三塊 ＋ 報告之替身·五 `commit`）並實跑閘 `1`〜`4`、`6`〜`13` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D1` | `15188` B·`sha256` `30c70bddb10fc87d4f21279f308d7ca7903b19cedcadaeb3a7a315248b556713`·`256` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F9` | `24254` B·`sha256` `6270cdf3a7e0492b721dae8e0854f6044964a0764ccce3e7505756043f93973d`·`482` 列（圍欄內全文·末附換行） |
| `4` | 塊 `E3` | `8365` B·`sha256` `d102fce77e469bce9a0cd09b0a15709c9da8cc8198cc41d4eb350d745e42957b`·`42` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1064143` B）之末後，期末 ＝ `1072508` B |
| `5` | 塊 `G3` | `5362` B·`sha256` `d49430c4c4426971ed0f71edb702af233152853f3cffdf0582c444dc7e88a731`·`22` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1013686` B）之末後，期末 ＝ `1019048` B |
| `6` | 塊 `P4` | `4062` B·`sha256` `7478481bdb4cc5395079207240201346bf3cf6aabc0385155e8a46d568db4631`·`21` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`268881` B）之末後，期末 ＝ `272943` B |
| `7` | 施 `D1` 後之 blob | `app.py` `3ea96402e032f8f19f1af367d3428d16b5458bba`（`1518340` B）（開工態 `8672b00d…`） |
| `8` | `F9` 之二態 | 開工態（工項一之端）`selftest`／`wiring`／`run` 皆 `rc 1`；施 `D1` 後皆 `rc 0` |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十六實跑（態 `981fd1f`）：🔴 機械 `0` 項／🟡 提示 `5` 項——`P-1` `:127`（工項二前置之段·所觸之字樣係 `F9 wiring` 施前出艙之「突變錨…」一語之引述，⛔ 全稱否定 ⇒ **具名豁免**）、`P-1` `:642`／`:842`（塊 `F9` 之碼·所觸之字樣係該器自身之出艙文字 ⇒ **具名豁免**）、`P-4` `:140`／`:182`（工項二之驗、`§四` 收工閘之表頭·其箭頭之座標系皆為「改前〔工項一之端／`981fd1f`〕至改後〔工項二之 `commit`／工項四之端〕」，表內自載 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `18336`–`25927`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`981fd1f` ＋ 五 `commit`·本單之替身 ＋ 塊 `F9` ＋ 塊 `D1` ＋ 三塊 ＋ 報告之替身）：閘 `1` 工項二 `app.py` 增 `196`／刪 `0`，餘逐檔刪 `0`；閘 `2` 相異恰 `1`（`34` 檔）；閘 `3` `CR` 合計 `0`（`7` 檔·判別力 `12308`）；閘 `4` 三檔如 `§四`（嚴格前綴）；閘 `6`〜`13` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `43`／`43`／`42`；「app 側宿主 ＝ f3_screen_stepg_run」；`F8` 二子命令與 `F9` 三子命令之末列 `⇒ 紅 []；rc 0`）；跑畢追蹤檔之變動 `0` |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零、一、三、四 ⇒ 逕行 `push` 主線；工項二 ⇒ 依 `§二` 之放行、驗皆符後推主線；工項五 ⇒ KL 本機之主 checkout。
3. 收工後，主 checkout 之根之來源檔（本單，及工項五所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D1`（`git apply` 之差異·`app.py`）

````diff
diff --git a/app.py b/app.py
index 8672b00..3ea9640 100644
--- a/app.py
+++ b/app.py
@@ -1225,6 +1225,8 @@ def parse_cad_precision_layers(doc, classified_blocks: list, dxf_bytes) -> dict:
         'side_lines_matched_count': 0,
         'alloc_dir_by_block': {},          # 🚨 W-B §1-3：宗地分配線方向 {blk: (ux, uy)}
         'side_unmatched_warnings': [],     # 🚨 W-B §1-1b：端點未吻合警示
+        # 🆕 `W-G.9-350`：正面道路之幾何推導（五級 `r3`）{block_label: {...}}·見 `r3_front_road_derive`
+        'front_road_derive': {},
         'diagnostics': {'layers_found': [], 'unbound': []},
     }
     if doc is None or not classified_blocks:
@@ -1446,6 +1448,7 @@ def parse_cad_precision_layers(doc, classified_blocks: list, dxf_bytes) -> dict:
                            'candidates': _rk[:4], 'chosen': None})
         return _rk[0]['block'], _rk[0]['overlap_m'], _rk
 
+    _front_pts_chosen = {}   # 🆕 `W-G.9-350`：各街廓所綁 FRONT_LINE 之全部頂點（折線不截為二端點）
     for _fr in _front_raw:
         _w, _ov, _rk = _best_block(_fr['pts'], 'FRONT_LINE', _fr['handle'])
         if _w is None:
@@ -1455,6 +1458,7 @@ def parse_cad_precision_layers(doc, classified_blocks: list, dxf_bytes) -> dict:
         if _ov <= result.get('_front_ovl', {}).get(_w, 0.0):
             continue
         result.setdefault('_front_ovl', {})[_w] = _ov
+        _front_pts_chosen[_w] = [(float(_q[0]), float(_q[1])) for _q in _fr['pts']]
         try:
             _ang_fl = _m.degrees(_m.atan2(_fr['pts'][-1][1] - _fr['pts'][0][1],
                                           _fr['pts'][-1][0] - _fr['pts'][0][0]))
@@ -1470,6 +1474,15 @@ def parse_cad_precision_layers(doc, classified_blocks: list, dxf_bytes) -> dict:
     result.pop('_front_ovl', None)
     result['front_lines_matched_count'] = len(result['front_lines'])
 
+    # ── 🆕 `W-G.9-350`：正面道路之幾何推導（五級八鍵之 `r3`·KL 裁 `2026-09-05`）──────
+    #   候選 ＝ 非「可建築土地」之街廓（與上方 `_buildable_blocks` 同一判準之補集·⛔ 分區名字面）；
+    #   量測原語與容差 ＝ `_best_block` 所用之 `_line_block_overlap`（`W-G.9-235` 工項一之裁）。
+    result['front_road_derive'] = r3_front_road_derive(
+        _front_pts_chosen,
+        {_lr: (_br.get('category', ''), _pr)
+         for _lr, (_br, _pr, _cr, _fr_dir) in blk_polys.items()
+         if _lr not in _buildable_blocks})
+
     # ── 🆕 W-G.5 C-6：SIDE_LINE 同判準綁定（街廓由重疊定·**側別仍由 FRONT p1→p2 導出**）──
     #
     # ⛔ 舊法（端點與 FRONTLINE 端點重合 ≤0.5m ＋ first-hit break）已廢：
@@ -10793,6 +10806,166 @@ K91_SS_MBA_EFFECTIVE = 'f3_min_build_area_effective_by_label'
 #   🔒 ⛔ 及於**側面**道路——`r3` 之受詞為**正面**道路（單 `§三 b`：擴及側面係射程外）。
 SS_FRONT_ROAD_NAME = 'f3_front_road_name_by_bid'
 
+# ── 🆕 `W-G.9-350`：正面道路識別符（五級八鍵之 `r3`·`v3` 五級③）──────────────────
+#   識別符 ＝ 幾何推導 ∪ 區外道路清單（KL 裁 `2026-09-05`）：推導有值時使用者⛔ 覆寫；
+#   清單只填推導之空缺——本批以 `SS_FRONT_ROAD_NAME`（`W-G.9-248` 之欄）為清單之載體，
+#   填同一名稱之街廓即指向同一項。
+#   🔒 幾何推導 ＝ `_best_block` 之同一原語與容差（`_line_block_overlap`·預設 `2.0°`／`1.0 m`）
+#      ＋ 「沿線過半」（`W-G.9-235` 工項一之裁）：某一候選街廓之重疊長 ÷ 該 FRONT_LINE 長
+#      **嚴格大於** `R3_FRONT_ROAD_MAJORITY` 者入推導集。
+#   🛑 本批⛔ 建消費端：⛔ 任何判定式／`G` 式／配地讀此值（新調配模組另單）。
+R3_FRONT_ROAD_MAJORITY = 0.5
+SS_FRONT_ROAD_DERIVE = 'f3_cad_front_road_derive'
+R3_STATUS_DERIVED = '成功'
+R3_STATUS_OUTSIDE = '區外'
+R3_STATUS_AMBIGUOUS = '歧義'
+R3_STATUS_NO_FRONT = '無正面線'
+
+
+def r3_front_road_derive(front_pts_by_label, pool_by_label,
+                         majority=R3_FRONT_ROAD_MAJORITY):
+    """`W-G.9-350`：正面道路之**幾何推導**（純函式·⛔ 讀 session）。
+
+    `front_pts_by_label`  `{街廓 label: [(x, y), …]}`——各街廓所綁 FRONT_LINE 之**全部頂點**
+                          （折線逐段計·⛔ 截為二端點）。
+    `pool_by_label`       `{街廓 label: (category, shapely Polygon)}`——候選（非可建築土地之街廓）。
+    回傳 `{label: {'line_length_m', 'candidates', 'derived', 'status'}}`：
+      `candidates` ＝ 重疊長 `> 0` 之候選，逐項 `{'block','category','overlap_m','ratio'}`，
+                     依重疊長降冪、同長依 label 升冪（決定性）；
+      `derived`    ＝ `ratio > majority` 者之 label 串列；
+      `status`     ＝ 恰一 ⇒ `R3_STATUS_DERIVED`／空 ⇒ `R3_STATUS_OUTSIDE`／`≥ 2` ⇒ `R3_STATUS_AMBIGUOUS`。
+    🔒 FRONT_LINE 頂點不足 `2` 或線長為 `0` ⇒ **loud `ValueError`**（⛔ 靜默略過）。
+    """
+    import math as _m_r3
+    _out = {}
+    for _lbl in sorted(front_pts_by_label or {}):
+        _pts = [(float(_p[0]), float(_p[1])) for _p in (front_pts_by_label[_lbl] or [])]
+        if len(_pts) < 2:
+            raise ValueError(
+                "r3_front_road_derive：街廓 %r 之 FRONT_LINE 頂點不足 2（%d）" % (_lbl, len(_pts)))
+        _L = sum(_m_r3.hypot(_pts[_i + 1][0] - _pts[_i][0], _pts[_i + 1][1] - _pts[_i][1])
+                 for _i in range(len(_pts) - 1))
+        if not (_L > 1e-9):
+            raise ValueError("r3_front_road_derive：街廓 %r 之 FRONT_LINE 線長為 0" % (_lbl,))
+        _cands = []
+        for _k in sorted(pool_by_label or {}):
+            if _k == _lbl:
+                continue
+            _cat, _poly = pool_by_label[_k]
+            _o = float(_line_block_overlap(_pts, _poly))
+            if _o > 0:
+                _cands.append({'block': _k, 'category': _cat,
+                               'overlap_m': _o, 'ratio': _o / _L})
+        _cands.sort(key=lambda _c: (-_c['overlap_m'], _c['block']))
+        _derived = [_c['block'] for _c in _cands if _c['ratio'] > majority]
+        if len(_derived) == 1:
+            _st = R3_STATUS_DERIVED
+        elif not _derived:
+            _st = R3_STATUS_OUTSIDE
+        else:
+            _st = R3_STATUS_AMBIGUOUS
+        _out[_lbl] = {'line_length_m': _L, 'candidates': _cands,
+                      'derived': _derived, 'status': _st}
+    return _out
+
+
+def r3_normalize_road_name(text):
+    """`W-G.9-350`：使用者所填之正面道路名稱之正規形（`NFKC` ＋ 去首尾空白 ＋ 連續空白併一）。"""
+    import unicodedata as _ud_r3
+    return ' '.join(_ud_r3.normalize('NFKC', str(text or '')).split())
+
+
+def r3_front_road_identifier(labels, derive_by_label, name_by_label):
+    """`W-G.9-350`：正面道路**識別符** ＝ 幾何推導 ∪ 區外道路清單（純函式）。
+
+    `labels`          可建築街廓之 label 串列（逐一出艙·⛔ 靜默漏列）。
+    `derive_by_label` `r3_front_road_derive` 之回傳。
+    `name_by_label`   `{label: 使用者所填之名稱}`（區外道路清單之載體）。
+    回傳 `{label: {'id', 'source', 'status', 'user_text', 'user_text_ignored'}}`：
+      推導 `成功` ⇒ `id` ＝ 該道路街廓之 label、`source` ＝ `'圖推導'`；使用者所填者⛔ 採
+                    （`user_text_ignored` ＝ 有填與否）。
+      `區外`／`歧義` ⇒ `id` ＝ 正規化後之名稱（空 ⇒ `None`）、`source` ＝ `'使用者填'`（空 ⇒ `None`）。
+      無推導資料（未綁 FRONT_LINE）⇒ `status` ＝ `R3_STATUS_NO_FRONT`、`id` ＝ `None`。
+    🔒 二街廓之識別符**字串相同**即為同一正面道路（含使用者填一區內道路街廓之 label 者）。
+    """
+    _out = {}
+    for _lbl in labels or []:
+        _name = r3_normalize_road_name((name_by_label or {}).get(_lbl, ''))
+        _d = (derive_by_label or {}).get(_lbl)
+        if _d is None:
+            _out[_lbl] = {'id': None, 'source': None, 'status': R3_STATUS_NO_FRONT,
+                          'user_text': _name, 'user_text_ignored': bool(_name)}
+        elif _d['status'] == R3_STATUS_DERIVED:
+            _out[_lbl] = {'id': _d['derived'][0], 'source': '圖推導', 'status': _d['status'],
+                          'user_text': _name, 'user_text_ignored': bool(_name)}
+        else:
+            _out[_lbl] = {'id': (_name or None), 'source': ('使用者填' if _name else None),
+                          'status': _d['status'], 'user_text': _name,
+                          'user_text_ignored': False}
+    return _out
+
+
+def r3_front_road_caption(derive_entry):
+    """`W-G.9-350`：街廓卡片內「正面道路名稱／識別符」欄下之說明一句（純函式）。"""
+    if not derive_entry:
+        return "🧭 圖推導：本街廓無正面線（FRONT_LINE）之資料，無從推導。"
+    _c = derive_entry.get('candidates') or []
+    _st = derive_entry.get('status')
+    if _st == R3_STATUS_DERIVED:
+        _b = derive_entry['derived'][0]
+        _r = next(_x['ratio'] for _x in _c if _x['block'] == _b)
+        return ("🧭 圖推導：正面道路 ＝ %s（沿正面線 %.2f%%）——推導有值，本欄不採。"
+                % (_b, 100.0 * _r))
+    if _st == R3_STATUS_OUTSIDE:
+        _top = ("；區內道路沿正面線最多 %.2f%%（%s）" % (100.0 * _c[0]['ratio'], _c[0]['block'])
+                if _c else "；正面線未沿任何區內道路")
+        return ("🧭 圖推導：正面道路在重劃區外%s——請填本欄；臨同一條道路之街廓請填相同名稱。"
+                % _top)
+    return ("🧭 圖推導：沿正面線過半之道路不只一條（%s）——請填本欄。"
+            % "、".join(derive_entry.get('derived') or []))
+
+
+def r3_front_road_rows(labels, derive_by_label, name_by_label):
+    """`W-G.9-350`：「正面道路識別」一覽之列（純函式·各欄皆字串·⛔ 混型欄）。
+
+    回傳 `{'rows', 'groups', 'group_lines', 'missing'}`：
+      `groups`      ＝ `{識別符: [label, …]}`（識別符升冪；`None` 不入）；
+      `group_lines` ＝ 逐組一句；`missing` ＝ 識別符為 `None` 之 label 串列（依 `labels` 之序）。
+    """
+    _ident = r3_front_road_identifier(labels, derive_by_label, name_by_label)
+    _rows = []
+    for _lbl in labels or []:
+        _d = (derive_by_label or {}).get(_lbl)
+        _i = _ident[_lbl]
+        if _d is None:
+            _geo = '—（無正面線）'
+        elif _d['status'] == R3_STATUS_DERIVED:
+            _b = _d['derived'][0]
+            _r = next(_x['ratio'] for _x in _d['candidates'] if _x['block'] == _b)
+            _geo = '%s（沿正面線 %.2f%%）' % (_b, 100.0 * _r)
+        elif _d['status'] == R3_STATUS_OUTSIDE:
+            _geo = ('區外（區內道路最多 %.2f%%）' % (100.0 * _d['candidates'][0]['ratio'])
+                    if _d['candidates'] else '區外（未沿任何區內道路）')
+        else:
+            _geo = '歧義（%s）' % '、'.join(_d['derived'])
+        _rows.append({
+            '街廓': str(_lbl),
+            '圖推導': _geo,
+            '使用者所填': (_i['user_text'] or '—') + ('（不採）' if _i['user_text_ignored'] else ''),
+            '採用之識別符': _i['id'] if _i['id'] is not None else '（未填）',
+            '來源': _i['source'] or '—',
+            '狀態': _i['status'],
+        })
+    _groups = {}
+    for _lbl in labels or []:
+        _id = _ident[_lbl]['id']
+        if _id is not None:
+            _groups.setdefault(_id, []).append(_lbl)
+    _groups = {_k: _groups[_k] for _k in sorted(_groups)}
+    _lines = ['正面道路「%s」：%s' % (_k, '、'.join(_v)) for _k, _v in _groups.items()]
+    _missing = [_lbl for _lbl in labels or [] if _ident[_lbl]['id'] is None]
+    return {'rows': _rows, 'groups': _groups, 'group_lines': _lines, 'missing': _missing}
+
 
 def wg9248_stringify_mixed_cols(df, cols):
     """把指定欄轉為 `str`，以避 `pyarrow.lib.ArrowInvalid`（混型欄之 Arrow 轉換紅）。
@@ -21889,6 +22062,10 @@ def main():
                         st.session_state['f3_cad_front_lines'] = (
                             _cad_layers.get('front_lines', {}) or {}
                         )
+                        # 🆕 `W-G.9-350`：正面道路之幾何推導（五級 `r3`·⛔ 消費端·僅供顯示）
+                        st.session_state[SS_FRONT_ROAD_DERIVE] = (
+                            _cad_layers.get('front_road_derive', {}) or {}
+                        )
                         # 🆕 Hotfix：左/右側長度分開儲存
                         st.session_state['f3_cad_side_lengths_by_side'] = (
                             _cad_layers.get('side_lengths_by_side', {}) or {}
@@ -23146,6 +23323,9 @@ def main():
                                  "留空表示未填。",
                         )
                         _new_front_road_names[bid] = frn
+                        # 🆕 `W-G.9-350`：該欄下附圖推導之結果一句（`r3_front_road_caption`·純顯示）
+                        st.caption(r3_front_road_caption(
+                            (st.session_state.get(SS_FRONT_ROAD_DERIVE, {}) or {}).get(b['label'])))
 
                         # 🆕 `W-G.9-248` 工項一（**丙案**·KL 裁 `2026-09-07`）：
                         #   街廓**最小建築面積**之**唯讀顯示**（置於正面道路區塊**下方**）。
@@ -23265,6 +23445,22 @@ def main():
                 st.success("路寬資料已儲存（正面 + 左側 + 右側三組）")
                 st.rerun()
 
+            # 🆕 `W-G.9-350`：正面道路識別之一覽（五級 `r3` 之資料·⛔ 消費端）
+            #   列之組成全在 module 級純函式 `r3_front_road_rows`；此處只渲染。
+            _r3_names_persist = st.session_state.get(SS_FRONT_ROAD_NAME, {}) or {}
+            _r3_view = r3_front_road_rows(
+                [b['label'] for b in build_blocks],
+                st.session_state.get(SS_FRONT_ROAD_DERIVE, {}) or {},
+                {b['label']: _r3_names_persist.get(b['id'], '') for b in build_blocks})
+            st.markdown("##### 🧭 正面道路識別（五級第三鍵之資料·尚未接任何閘）")
+            st.dataframe(pd.DataFrame(_r3_view['rows']), hide_index=True)
+            for _r3_line in _r3_view['group_lines']:
+                st.caption(_r3_line)
+            if _r3_view['missing']:
+                st.info(
+                    "以下街廓之正面道路無從由圖推導，請於上方該街廓之「正面道路名稱／識別符」欄填名"
+                    "（臨同一條道路者填相同名稱）：" + "、".join(_r3_view['missing']))
+
         # ---------- 步驟 F：全區參數 ----------
         st.markdown("---")
         st.markdown("#### 💰 步驟 F：全區參數")
````

## 附錄乙　塊 `F9`（新檔 `verify/probes/probe_WG9350_frontroad.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-350 量測器（發單側窗四十六擬·檔 F9·⛔ 由受單側改一字）：正面道路識別符（五級八鍵之 `r3`）。

子命令（一律 python verify/probes/probe_WG9350_frontroad.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·只 harvest `app.py`）：`r3_front_road_derive` 之九例（成功·區外·恰半·
           過半·歧義·折線·自身排除·頂點不足·線長為 0）、`r3_front_road_identifier`／`r3_front_road_rows`／
           `r3_front_road_caption` 之八例；另以 AST 自 `app.py` 抽出同名函式施三突變（`>` → `>=`、折線改取二端點、
           推導有值仍採使用者所填），每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST 查接線：W1 具名常數；W2 `parse_cad_precision_layers` 之初值鍵、折線頂點之留存、推導之呼叫與候選集
           （非可建築土地之補集）；W3 `main()` 之 session 寫入與二顯示函式之呼叫；W4 消費端 ＝ 生產碼 `34` 檔中
           除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內；W5 畫面路徑之合成案（`自誤 517`：抽出 `main()`
           之一覽區塊與卡片說明句，以假 st 與合成資料實際執行）。另施四突變（刪推導之賦值、改 session 鍵、
           於 `verify/stepg_pipeline.py` 注入一消費者、一覽只出首列），每一突變須轉紅。
  run      <repo>
           harness 之 CAD 入口（`run_verification._build_cb_cad`）實跑本案；出艙逐街廓之推導與一覽，並驗：
             R1 可建築街廓皆有推導；R2 狀態與比值一致（入推導集 ⇔ 比值 > 具名常數）；
             R3 線長之自我驗證閘（＝ `front_lines` 之 `length`·`LineString.length`）；
             R4 外部錨：以 shapely 之 `line ∩ polygon.buffer(1.0)` 另算比值，逐一分類（> 具名常數與否）與 R2 相同。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, json, math, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

R3_FUNCS = ["r3_front_road_derive", "r3_normalize_road_name", "r3_front_road_identifier",
            "r3_front_road_caption", "r3_front_road_rows"]
R3_CONSTS = ["R3_FRONT_ROAD_MAJORITY", "SS_FRONT_ROAD_DERIVE", "R3_STATUS_DERIVED",
             "R3_STATUS_OUTSIDE", "R3_STATUS_AMBIGUOUS", "R3_STATUS_NO_FRONT"]


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    """自 `app.py` 原始碼以 AST 抽出 `_line_block_overlap`、R3 常數與 R3 函式，於隔離之命名空間執行。"""
    tree = ast.parse(src)
    want_f = set(R3_FUNCS) | {"_line_block_overlap"}
    parts = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in want_f:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id in R3_CONSTS:
            parts.append(ast.get_source_segment(src, node))
    ns = {}
    exec(compile("\n\n".join(parts), "<r3_extract>", "exec"), ns)
    return ns


def _band(x0, x1, y0=-10.0, y1=0.0):
    from shapely.geometry import Polygon
    return Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def _cases(ns):
    """回 [(名, 得, 期)]；任一例拋例外 ⇒ 以 ('例外', 型別名) 記之（⛔ 吞）。"""
    from shapely.geometry import Polygon
    D = ns["r3_front_road_derive"]
    I = ns["r3_front_road_identifier"]
    RW = ns["r3_front_road_rows"]
    C = ns["r3_front_road_caption"]
    OK, OUT, AMB, NOF = (ns["R3_STATUS_DERIVED"], ns["R3_STATUS_OUTSIDE"],
                         ns["R3_STATUS_AMBIGUOUS"], ns["R3_STATUS_NO_FRONT"])
    LINE = {"B": [(0.0, 0.0), (100.0, 0.0)]}
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as e:  # noqa: BLE001
            got = ("例外", type(e).__name__)
        out.append((name, got, exp))

    def st(d):
        return (d["B"]["status"], d["B"]["derived"])

    run("S1 全長臨一道路 ⇒ 成功", lambda: st(D(LINE, {"A": ("道路", _band(0, 100))})), (OK, ["A"]))
    run("S2 無候選 ⇒ 區外", lambda: st(D(LINE, {})), (OUT, []))
    run("S3 沿線 30% ⇒ 區外", lambda: st(D(LINE, {"A": ("道路", _band(0, 30))})), (OUT, []))
    run("S4 沿線恰 50% ⇒ 區外（嚴格大於）", lambda: st(D(LINE, {"A": ("道路", _band(0, 50))})), (OUT, []))
    run("S5 沿線 50.5% ⇒ 成功", lambda: st(D(LINE, {"A": ("道路", _band(0, 50.5))})), (OK, ["A"]))
    run("S6 二候選各過半 ⇒ 歧義（重疊長降冪）",
        lambda: st(D(LINE, {"A": ("道路", _band(0, 60)), "B2": ("道路", _band(30, 100))})), (AMB, ["B2", "A"]))
    L2 = {"B": [(0.0, 0.0), (50.0, 0.0), (50.0, 50.0)]}
    run("S7 折線：只臨首段（50／100）⇒ 區外", lambda: st(D(L2, {"A": ("道路", _band(0, 50))})), (OUT, []))
    Lsh = Polygon([(0, -10), (60, -10), (60, 50), (50, 50), (50, 0), (0, 0)])
    run("S8 折線：臨二段 ⇒ 成功", lambda: st(D(L2, {"A": ("道路", Lsh)})), (OK, ["A"]))
    run("S9 候選含自身 ⇒ 排除", lambda: st(D(LINE, {"B": ("道路", _band(0, 100))})), (OUT, []))
    run("S10 頂點不足 ⇒ loud", lambda: D({"B": [(0.0, 0.0)]}, {}), ("例外", "ValueError"))
    run("S11 線長為 0 ⇒ loud", lambda: D({"B": [(1.0, 1.0), (1.0, 1.0)]}, {}), ("例外", "ValueError"))

    dv = D({"P": [(0.0, 0.0), (100.0, 0.0)], "Q": [(0.0, 50.0), (100.0, 50.0)],
            "R": [(0.0, 100.0), (100.0, 100.0)]},
           {"RD1": ("道路", _band(0, 100))})
    labels = ["P", "Q", "R", "Z"]
    run("I1 推導有值 ⇒ 採推導、使用者所填不採",
        lambda: (I(labels, dv, {"P": "中山路"})["P"]["id"], I(labels, dv, {"P": "中山路"})["P"]["user_text_ignored"]),
        ("RD1", True))
    run("I2 區外 ⇒ 採正規化後之名稱", lambda: I(labels, dv, {"Q": "  中正　路 "})["Q"]["id"], "中正 路")
    run("I3 區外而未填 ⇒ None", lambda: I(labels, dv, {})["Q"]["id"], None)
    run("I4 無推導 ⇒ 無正面線", lambda: (I(labels, dv, {"Z": "X"})["Z"]["status"], I(labels, dv, {"Z": "X"})["Z"]["id"]),
        (NOF, None))
    run("I5 全形 ＲＤ１ ⇒ 與推導之 RD1 同組",
        lambda: RW(labels, dv, {"Q": "ＲＤ１", "R": "中正路"})["groups"], {"RD1": ["P", "Q"], "中正路": ["R"]})
    run("I6 未填者列入 missing", lambda: RW(labels, dv, {"Q": "中正路"})["missing"], ["R", "Z"])
    run("I7 一覽各欄皆字串",
        lambda: all(isinstance(v, str) for r in RW(labels, dv, {"Q": "X"})["rows"] for v in r.values()), True)
    run("I8 說明句三態",
        lambda: ("推導有值" in C(dv["P"]), "重劃區外" in C(dv["Q"]), "無正面線" in C(None)), (True, True, True))
    return out


def _mutate(src, fname, old, new):
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == fname:
            seg = ast.get_source_segment(src, node)
            if seg.count(old) != 1:
                return None
            return src.replace(seg, seg.replace(old, new), 1)
    return None


MUTS_FN = [
    ("M1 `>` → `>=`", "r3_front_road_derive",
     "if _c['ratio'] > majority]", "if _c['ratio'] >= majority]"),
    ("M2 折線改取二端點", "r3_front_road_derive",
     "for _i in range(len(_pts) - 1))",
     "for _i in range(len(_pts) - 1)) * 0 + _m_r3.hypot(_pts[-1][0] - _pts[0][0], _pts[-1][1] - _pts[0][1])"),
    ("M3 推導有值仍採使用者所填", "r3_front_road_identifier",
     "{'id': _d['derived'][0],", "{'id': (_name or _d['derived'][0]),"),
]


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in R3_FUNCS + R3_CONSTS if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    print("── 合成對照（harvest 之 app.py）──")
    for name, got, exp in _cases(ns):
        ok = (got == exp)
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    print("── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──")
    src = _read(repo, "app.py")
    base = _extract_ns(src)
    b_red = [n for n, g, e in _cases(base) if g != e]
    print(("  ✅ " if not b_red else "  🔴 ") + f"M0 未突變之抽出版：紅 {b_red}（期 []）")
    if b_red:
        red.append("M0")
    for mname, fname, old, new in MUTS_FN:
        msrc = _mutate(src, fname, old, new)
        if msrc is None:
            print(f"  🔴 {mname}：突變錨不存在或非唯一")
            red.append(mname)
            continue
        m_red = [n for n, g, e in _cases(_extract_ns(msrc)) if g != e]
        ok = bool(m_red)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {m_red}")
        if not ok:
            red.append(mname)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


PROD_OTHERS_RE = re.compile(r"^verify/[^/]+\.py$")


def _wiring_checks(app_src, others):
    """回 [(名, 真偽, 註)]。`others` ＝ {路徑: 原始碼}（生產碼 34 檔中 app.py 以外者）。"""
    res = []
    tree = ast.parse(app_src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    c = consts.get("R3_FRONT_ROAD_MAJORITY")
    ok1 = c is not None and isinstance(c.value, ast.Constant) and c.value.value == 0.5
    fd = top.get("r3_front_road_derive")
    ok1b = fd is not None and any(isinstance(d, ast.Name) and d.id == "R3_FRONT_ROAD_MAJORITY"
                                  for d in fd.args.defaults)
    lit = [n.lineno for f in R3_FUNCS if f in top for n in ast.walk(top[f])
           if isinstance(n, ast.Constant) and n.value == 0.5]
    res.append(("W1 具名常數 R3_FRONT_ROAD_MAJORITY ＝ 0.5、推導之預設引用之、R3 函式內⛔ 字面 0.5",
                ok1 and ok1b and not lit, f"字面 0.5 之列 {lit}"))
    pc = top.get("parse_cad_precision_layers")
    init_ok = keep_ok = call_ok = pool_ok = False
    if pc is not None:
        for n in ast.walk(pc):
            if isinstance(n, ast.Dict) and any(isinstance(k, ast.Constant) and k.value == "front_road_derive"
                                               for k in n.keys):
                init_ok = True
            if isinstance(n, ast.For) and isinstance(n.iter, ast.Name) and n.iter.id == "_front_raw":
                for m in ast.walk(n):
                    if isinstance(m, ast.Assign) and isinstance(m.targets[0], ast.Subscript) \
                            and isinstance(m.targets[0].value, ast.Name) \
                            and m.targets[0].value.id == "_front_pts_chosen":
                        keep_ok = True
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) \
                    and isinstance(n.targets[0].slice, ast.Constant) \
                    and n.targets[0].slice.value == "front_road_derive" \
                    and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) \
                    and n.value.func.id == "r3_front_road_derive":
                call_ok = True
                a = n.value.args
                if len(a) >= 2 and isinstance(a[0], ast.Name) and a[0].id == "_front_pts_chosen" \
                        and isinstance(a[1], ast.DictComp):
                    for g in a[1].generators:
                        for cond in g.ifs:
                            if isinstance(cond, ast.Compare) and isinstance(cond.ops[0], ast.NotIn) \
                                    and isinstance(cond.comparators[0], ast.Name) \
                                    and cond.comparators[0].id == "_buildable_blocks":
                                pool_ok = True
    res.append(("W2a 解析之回傳初值含 'front_road_derive'", init_ok, ""))
    res.append(("W2b FRONT_LINE 綁定迴圈內留存全部頂點（_front_pts_chosen[...] ＝ …）", keep_ok, ""))
    res.append(("W2c result['front_road_derive'] ＝ r3_front_road_derive(_front_pts_chosen, …)", call_ok, ""))
    res.append(("W2d 候選集 ＝ 非 _buildable_blocks 之補集", pool_ok, ""))
    mn = top.get("main")
    store_ok = cap_ok = rows_ok = False
    if mn is not None:
        for n in ast.walk(mn):
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) \
                    and isinstance(n.targets[0].slice, ast.Name) \
                    and n.targets[0].slice.id == "SS_FRONT_ROAD_DERIVE":
                for m in ast.walk(n.value):
                    if isinstance(m, ast.Call) and isinstance(m.func, ast.Attribute) and m.func.attr == "get" \
                            and m.args and isinstance(m.args[0], ast.Constant) \
                            and m.args[0].value == "front_road_derive":
                        store_ok = True
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                if n.func.id == "r3_front_road_caption":
                    cap_ok = True
                if n.func.id == "r3_front_road_rows":
                    rows_ok = True
    res.append(("W3a main()：st.session_state[SS_FRONT_ROAD_DERIVE] ＝ _cad_layers.get('front_road_derive', …)", store_ok, ""))
    res.append(("W3b main()：呼叫 r3_front_road_caption", cap_ok, ""))
    res.append(("W3c main()：呼叫 r3_front_road_rows", rows_ok, ""))
    toks = R3_FUNCS + ["SS_FRONT_ROAD_DERIVE", "front_road_derive", "R3_FRONT_ROAD_MAJORITY"]
    tok_re = re.compile("|".join(re.escape(t) for t in toks))
    other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
    allowed = set(R3_FUNCS) | {"parse_cad_precision_layers", "main"}
    bad = []
    for fname, node in top.items():
        if fname in allowed:
            continue
        seg = ast.get_source_segment(app_src, node) or ""
        if tok_re.search(seg):
            bad.append(fname)
    res.append((f"W4 消費端：生產碼他檔（{len(others)} 檔）命中 0；app.py 只在許可之函式內",
                not other_hits and not bad, f"他檔 {other_hits}；app.py 非許可函式 {bad}"))
    ok5, note5 = _synth_screen(app_src, mn)
    res.append(("W5 畫面路徑之合成案：main() 之一覽區塊與卡片說明句以假 st 實際執行", ok5, note5))
    return res


class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.calls.append((name, a, k))
        return rec


def _synth_screen(app_src, mn):
    """`自誤 517`：`main()` 內之敘述⛔ 為 run_all 所執行 ⇒ 抽出其一覽區塊（自 `_r3_names_persist` 之賦值起
    連續 `6` 句）與卡片說明句，以假 st ＋ 合成資料實際執行，驗其輸出。"""
    if mn is None:
        return False, "無 main()"
    blk = cap = None
    for n in ast.walk(mn):
        for fld in ("body", "orelse", "finalbody"):
            body = getattr(n, fld, None)
            if not isinstance(body, list):
                continue
            for i, s in enumerate(body):
                if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) \
                        and s.targets[0].id == "_r3_names_persist":
                    blk = body[i:i + 6]
                if isinstance(s, ast.Expr) and isinstance(s.value, ast.Call) \
                        and isinstance(s.value.func, ast.Attribute) and s.value.func.attr == "caption" \
                        and s.value.args and isinstance(s.value.args[0], ast.Call) \
                        and isinstance(s.value.args[0].func, ast.Name) \
                        and s.value.args[0].func.id == "r3_front_road_caption":
                    cap = s
    if blk is None or cap is None or not isinstance(blk[-1], ast.If):
        return False, "抽不到一覽區塊或說明句"
    try:
        import pandas as pd
        rns = _extract_ns(app_src)
        dv = rns["r3_front_road_derive"](
            {"P": [(0.0, 0.0), (100.0, 0.0)], "Q": [(0.0, 50.0), (100.0, 50.0)],
             "R": [(0.0, 100.0), (100.0, 100.0)]},
            {"RD1": ("道路", _band(0, 100))})
        bb = [{"id": 11, "label": "P"}, {"id": 12, "label": "Q"}, {"id": 13, "label": "R"}]
        ss = {rns["SS_FRONT_ROAD_DERIVE"]: dv, "f3_front_road_name_by_bid": {12: "中正路", 11: "甲路"}}
        fst = _FakeSt(ss)
        g = dict(rns, st=fst, pd=pd, build_blocks=bb, SS_FRONT_ROAD_NAME="f3_front_road_name_by_bid")
        exec(compile(ast.Module(body=blk, type_ignores=[]), "<main_r3_block>", "exec"), g)
        for b in bb:
            exec(compile(ast.Module(body=[cap], type_ignores=[]), "<main_r3_caption>", "exec"), dict(g, b=b))
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    dfs = [c for c in fst.calls if c[0] == "dataframe"]
    infos = [c for c in fst.calls if c[0] == "info"]
    caps = [c[1][0] for c in fst.calls if c[0] == "caption"]
    df = dfs[0][1][0] if len(dfs) == 1 else None
    checks = {
        "一覽 1 表 3 列": df is not None and len(df) == 3,
        "P 採 RD1（使用者所填不採）": df is not None and list(df["採用之識別符"]) == ["RD1", "中正路", "（未填）"],
        "組句 2": sum(1 for s in caps if s.startswith("正面道路「")) == 2,
        "待填 R": len(infos) == 1 and infos[0][1][0].endswith("R"),
        "卡片說明句 3": sum(1 for s in caps if s.startswith("🧭")) == 3,
    }
    bad = [k for k, v in checks.items() if not v]
    return (not bad), f"不符 {bad}"


def _prod_others(repo):
    out = {}
    vd = os.path.join(repo, "verify")
    for fn in sorted(os.listdir(vd)):
        p = "verify/" + fn
        if fn.endswith(".py") and PROD_OTHERS_RE.match(p):
            out[p] = _read(repo, p)
    return out


def wiring(repo):
    app_src = _read(repo, "app.py")
    others = _prod_others(repo)
    red = []
    print(f"── 接線（AST·app.py ＋ 生產碼他檔 {len(others)} 檔）──")
    base_red = set()
    for name, ok, note in _wiring_checks(app_src, others):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
            base_red.add(name.split()[0])
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    muts = [
        ("N1 刪推導之賦值", app_src.replace(
            "result['front_road_derive'] = r3_front_road_derive(", "_r3_unused = r3_front_road_derive(", 1), others),
        ("N2 main() 改寫他鍵", app_src.replace(
            "st.session_state[SS_FRONT_ROAD_DERIVE] = (", "st.session_state['f3_r3_other'] = (", 1), others),
        ("N3 注入 harness 消費者", app_src,
         dict(others, **{"verify/stepg_pipeline.py": others.get("verify/stepg_pipeline.py", "")
                         + "\n_r3x = (cad or {}).get('front_road_derive')\n"})),
        ("N4 一覽只出首列", app_src.replace(
            "st.dataframe(pd.DataFrame(_r3_view['rows']), hide_index=True)",
            "st.dataframe(pd.DataFrame(_r3_view['rows'][:1]), hide_index=True)", 1), others),
    ]
    for mname, msrc, moth in muts:
        if mname != "N3 注入 harness 消費者" and msrc == app_src:
            print(f"  🔴 {mname}：突變錨不存在")
            red.append(mname.split()[0])
            continue
        turned = [n.split()[0] for n, ok, _ in _wiring_checks(msrc, moth)
                  if not ok and n.split()[0] not in base_red]
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def run(repo):
    ns, _ = _harvest(repo)
    if "r3_front_road_rows" not in ns:
        print("  🔴 受詞缺：r3_front_road_rows")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        import run_verification as rv
        with contextlib.redirect_stdout(io.StringIO()):
            cb, cad = rv._build_cb_cad(ns)
    finally:
        os.chdir(cwd)
    from shapely.geometry import LineString, Polygon
    K = ns["R3_FRONT_ROAD_MAJORITY"]
    OK = ns["R3_STATUS_DERIVED"]
    d = cad.get("front_road_derive")
    labels = sorted(b["label"] for b in cb if b.get("burden_type") == "可建築土地")
    polys = {}
    for b in cb:
        v = b.get("vertices") or []
        if len(v) >= 3:
            p = Polygon(v)
            polys[b["label"]] = p if p.is_valid else p.buffer(0)
    red, undet = [], []
    print(f"── 推導（具名常數 ＝ {K}·可建築街廓 {len(labels)}）──")
    if d is None:
        print("  🔴 cad 無 'front_road_derive'")
        print("⇒ 紅 ['R1']；rc 1")
        return 1
    miss = [l for l in labels if l not in d]
    print(("  ✅ " if not miss else "  🔴 ") + f"R1 可建築街廓皆有推導：缺 {miss}")
    if miss:
        red.append("R1")
    for l in labels:
        e = d.get(l)
        if e is None:
            continue
        cands = ", ".join(f"{c['block']}({c['category']}) {c['overlap_m']:.4f} m／{100 * c['ratio']:.2f}%"
                          for c in e["candidates"]) or "—"
        print(f"  {l}　線長 {e['line_length_m']:.4f}　狀態 {e['status']}　推導 {e['derived']}　候選 {cands}")
        want = [c["block"] for c in e["candidates"] if c["ratio"] > K]
        st_ok = (want == e["derived"]) and ((e["status"] == OK) == (len(want) == 1))
        if not st_ok:
            red.append(f"R2:{l}")
        fl = (cad.get("front_lines") or {}).get(l) or {}
        gate = abs(float(fl.get("length", -1)) - e["line_length_m"]) <= 1e-6
        if not gate:
            red.append(f"R3:{l}")
            print(f"    🔴 R3 線長 {e['line_length_m']:.6f} ≠ front_lines.length {fl.get('length')}")
            continue
        p1, p2 = fl.get("p1"), fl.get("p2")
        if abs(math.hypot(p2[0] - p1[0], p2[1] - p1[1]) - e["line_length_m"]) > 1e-6:
            undet.append(f"R4:{l}（折線·外部錨以二端點不可行）")
            continue
        ln = LineString([p1, p2])
        for c in e["candidates"]:
            ext = ln.intersection(polys[c["block"]].buffer(1.0)).length / e["line_length_m"]
            agree = (ext > K) == (c["ratio"] > K)
            print(f"    {'✅' if agree else '🔴'} R4 外部錨 {c['block']}：{100 * ext:.2f}%（原語 {100 * c['ratio']:.2f}%）")
            if not agree:
                red.append(f"R4:{l}:{c['block']}")
    print("── 一覽（區外道路清單為空）──")
    v = ns["r3_front_road_rows"](labels, d, {})
    for r in v["rows"]:
        print("  " + json.dumps(r, ensure_ascii=False))
    print("  組：" + "；".join(v["group_lines"]))
    print(f"  待填：{v['missing']}")
    if undet:
        print(f"  ⚠️ 無從判定：{undet}")
    rc = 1 if red else (3 if undet else 0)
    print(f"⇒ 紅 {red}；rc {rc}")
    return rc


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring":
        return wiring(repo)
    if cmd == "run":
        return run(repo)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄丙　塊 `E3`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-350 §零-1`）：本批取 `542`〜`545`（`4` 號）；皆係發單側窗四十六於復驗 `W-G.9-349`、擬本單與答 KL 之 `R6` 詢問（`2026-09-27`）時所捕。

### 🩸 `自誤 542`　**`W-G.9-349` 工項五以「追蹤檔無變動」為前置（`--untracked-files=no`），看不見「未追蹤之檔恰在本批新入倉之路徑上」；KL 置單於主 checkout 之 `docs/orders/` 而 CC 取之，工項零入倉於同一路徑，快轉即被拒（停機款 `10`）**

**形**：`docs/orders/W-G.9-349_重量單.md` 工項五 `1` 逐字「`git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（根之來源檔為未追蹤檔·⛔ 計）。」，`2` 逐字「`git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。」。同單檔首令來源檔置於 CC 施工樹之根、無之則取 KL 主 checkout 之根；實況二根皆無，唯主 checkout 之 `docs/orders/W-G.9-349_重量單.md`（未追蹤）有之，CC 取之（`docs/reports/W-G.9-349R_入池閘與閘二接線_執行報告.md` ⑥ 自解 `1`），工項零入倉於同一路徑 ⇒ 工項五之 `merge --ff-only` 被拒，git 逐字「The following untracked working tree files would be overwritten by merge: docs/orders/W-G.9-349_重量單.md」（CC 之對話回報·`2026-09-26`·倉外）。該未追蹤檔與入倉之 blob 逐位同（`sha256` `6e775b1d…f3231`）。
**後果之界**：KL 之主 checkout 停於 `88dc179`、`app.py` 仍為 `f4c47af6…`，畫面未含 `W-G.9-349` 之改動，至 KL 移除該檔並快轉為止；倉與主線⛔ 受影響。零土地後果、零入倉之誤。
**根因**：工項五之前置閘繫於代理量（「已追蹤之檔無變動」），⛔ 繫於其所守之性質（「快轉可成」）；未追蹤之檔與本批新入倉之路徑之交集，正落於 `--untracked-files=no` 之盲區。來源檔之置處已於 `W-G.9-348R` 自解 `1` 顯示其會隨次而異，擬單時未據以設防。
**後果之框**：🟢 零土地後果；🟡 KL 本機之同步延宕一輪。攔點 ＝ **CC**（停機款 `10`·⛔ 自刪該檔）。
**攔法**：`W-G.9-350` 工項五增一前置——取「本批新入倉之路徑」（`git diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart`）與「未追蹤之路徑」（`git ls-files --others --exclude-standard -z`）之交集，逐檔比 blob：逐位同 ⇒ 移至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫）後續辦；不同 ⇒ 停機。通則承 `W-G.9-199` 裁 `H` 之一般式（閘須直接綁其所守之性質，⛔ 綁其代理）。⛔ 新立款。

---

### 🩸 `自誤 543`　**`W-G.9-349` 塊 `P3`（入 `CLAUDE.md` 之末）之末列自載「本節 payload 內含 `⬜` 字樣 ＝ `1`（子字串框）·列 ＝ `1`（列框）」；含圖例與該列自身之實數為字樣 `5`·列 `3`**

**形**：`CLAUDE.md`「🔧 待落地清單之更新：閘二（`K-9-12`／`K-9-13`）與臨正街寬（`K-9-33`）之接線；`K-9-29 六` 入池閘（`W-G.9-349`·…）」節之末列逐字如標題所引。實測（母體 ＝ 該節 payload ＝ `docs/orders/W-G.9-349_重量單.md` 之塊 `P3`·`17` 列）：含 `⬜` 之列 ＝ 態列之圖例（「⬜ 未落地」）、序 `3` 之列、該末列自身 ⇒ 列 `3`；字樣 ＝ `1` ＋ `1` ＋ `3` ＝ `5`。同檔「🔧 待落地清單之補登：調配階段之諸裁」節（`W-G.9-332`）之自載「列 `10`、字樣 `13`」係含圖例與自身之數（實測逐位相符）⇒ 塊 `P3` 之 `1`／`1` 只計序 `3` 一列，與既例之框不一。
**後果之界**：凡以 `CLAUDE.md` 之 `⬜` 全檔命中為量、依該節自載扣減者，將少扣字樣 `4`／列 `2`。待落地清單以三態表逐列讀之、⛔ 以全檔計數為量 ⇒ 零土地後果。零入倉之生產碼。
**根因**：自載之數未以同一框對其 payload 當場實算（圖例與自指之列漏計）；擬塊時未取既例之框為範本。
**後果之框**：🟢 零土地後果；🟡 自載之數失準一處。攔點 ＝ **發單側**（窗四十六·擬 `W-G.9-350` 之塊 `P4` 時以既例復算）。
**攔法**：既有（`常規七` 款 `二`：三數與塊內文字須出自同一次抽取；`W-G.9-214` 之「🔧 四」：閘之通過條件⛔ 內嵌未當場復現之數）。`W-G.9-350` 之塊 `P4` 之自載以抽取後之塊實算（含圖例與自身），並以一列更正前節（⛔ 追改前節一字）。⛔ 新立款。

---

### 🩸 `自誤 544`　**`GB-178` 之進度（一）（`W-G.9-338`·入 `GB` 簿）載 `R6` `85.71`「三頂點·與任一地主宗⛔ 共界」；實則其 `47.68 m` 之邊與左側推進之第 `1` 宗之近側界重合（於該進度之態 `babc64d` 即然）**

**形**：`docs/reports/W-G.4_泛用阻塞項登記表.md`「`GB-178` 之進度（⛔ 解除）」節 `(3)` 逐字「`R6` `85.71`（三頂點·與任一地主宗⛔ 共界）⇒ **成因未具名**」（同文 ＝ `docs/orders/W-G.9-338_重量單.md:157`）。實測（發單側窗四十六·倉外·器 `verify/probes/wg9309/chk_wg9309.py` 甲 `3.5 m`）：態 `babc64d`（該進度之態）本片之 `47.68 m` 邊與 `628(2)+` 之近側界之 Hausdorff 距 `5.8e-10 m`、以 `1e-9 m` 緩衝量之共界長 `47.6792 m`；態 `88dc179`（`628(2)`）、`981fd1f`（`628-21(1)`）同；精確之 boundary 交集長於三態皆 `0`。「三頂點」屬實。
**後果之界**：本片之鄰接被述為孤立，致其成因未循「左側推進之第 `1` 宗以過 `p1` 之宗地分配線為近側界」一線尋之（成因之具名 ＝ 本簿 `GB-178` 之進度（四））。零土地後果；零入倉之生產碼。
**根因**（該句未載其量法·發單側之讀）：判共界以精確之 boundary 交集長——二片由 boolean 差集與切線各自得來，共界處有浮點級之縫，精確交集長為 `0`（同現象見 `app.py` `_pool_strips_for_block` 步驟 `5b` 之 `GB-182` 註「實測 R1 甲 3.5 m 未吸附時共界長 0」；同批之器 `verify/probes/probe_WG9338_gapcheck.py` 之 `shared()` 即精確交集長）；未以容差或吸附復核。
**後果之框**：🟢 零土地後果；🟡 `GB` 簿之描述失準一處。攔點 ＝ **發單側**（窗四十六·答 KL 之 `R6` 詢問時以三態復量）。
**攔法**：既有（`GB-182` 之修所用之相接判準：以 `_S_EPS` 吸附後聯集為單一 Polygon）；凡載「共界／⛔ 共界」之句，須具其量法與容差。⛔ 新立款。

---

### 🩸 `自誤 545`　**`GB-178` 之進度（一）〜（三）三度載 `R6` `85.71`「成因未具名」；其成因於進度（一）之態已由倉內三規格具名（N0-20 之「未臨正街土地」·`R_end` 之內部組成）**

**形**：`docs/reports/W-G.4_泛用阻塞項登記表.md` 之 `GB-178` 進度（一）`(3)`「⇒ **成因未具名**」、進度（二）`(3)`「`R6` `85.71 ㎡` 成因未具名」、進度（三）`(3)`「`R6` `85.71` ⇒ 成因未具名」。而態 `babc64d`（進度（一）之態）已在倉者：`docs/specs/W-G.4_S1_plan.md`（逐字「R6 實例 85.71（未臨正街）＋166.57（末端帶）＝252.28㎡」「p1 端楔形（R1 5.33／R6 85.71／0m R3 78.19）＝R_end 內部組成·非「碎片」」）、`docs/specs/W-G.4_規格_v3.md`（同旨）、`docs/specs/W-G.5_裁定N_乙案_plan_v1.md`（`block∩{s<0}` 之面積 `R6` `85.7064` ＝「未臨正街真幾何面積」）；其處置之正典 `K-9-36`（`W-G.9-308`·KL 裁 `2026-09-17`）亦早於進度（一）。
**後果之界**：失效條件 `(3)` 之 `R6` 一項本可於進度（一）即具名；KL `2026-09-27` 於畫面見此片而另詢其是否為未修之處。零土地後果；零入倉之生產碼。
**根因**：「成因未具名」之判未先以該片之面積字樣（`85.71`／`85.706`）全倉查既有之具名；立項節之「⛔ 判其是否同因」被沿為「未具名」而三進度未復查。
**後果之框**：🟢 零土地後果；🟡 `GB` 簿之現況失準（三進度）。攔點 ＝ **發單側**（窗四十六·同上）。
**攔法**：既有（`GB-180` 立項節之「取代／限縮之查」·全倉字樣查）；凡於 `GB` 簿載某片「成因未具名」者，先以其面積字樣全倉查，命中者引之。⛔ 新立款。
````

## 附錄丁　塊 `G3`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-178` 之進度（四）（`W-G.9-350`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `981fd1fc09a9fd22484bd3deeadd8a40be1e4a5e`（本批開工態）。**授權** ＝ `docs/orders/W-G.9-350_重量單.md` 工項三。⛔ 鑄號。

### `GB-178` 之進度（四）（⛔ 解除）

**緣起**：KL `2026-09-27` 逐字「在執行app.py時，G值迭代之分配成果發現(上傳截圖) R6在末端塊部分(R6街廓左側，無SIDELINE側)，有塊85.7㎡未臨路之抵費地，該部分是程式尚未修改至此部分?」（截圖 ＝ 畫面之 `R6-抵費地-2`·倉外之物）。其片即失效條件 `(3)` 所列之 `R6` `85.71 ㎡`（進度（三）載「成因未具名」）。
**實測**（發單側窗四十六·倉外·器 `verify/probes/wg9309/chk_wg9309.py` 甲 `3.5 m`·三態 `babc64d`／`88dc179`／`981fd1f`）：
- 片 `R6-抵費地-2` 之 `cut_coords` 於三態逐位同；面積 `85.706388 ㎡`；三頂點（取至 `0.001 m`）`(310560.950, 2651846.720)`、`(310528.144, 2651881.355)`、`(310525.647, 2651878.766)`。
- 首頂點 ＝ `R6` 之 FRONT_LINE 端點 `p1`（harness `_build_cb_cad` 之 `front_lines['R6']['p1']` ＝ `(310560.95013, 2651846.71976)`）；自 `p1` 出二長邊：`47.71 m`（方位 `133.45°`·街廓左端之界）、`47.68 m`（`137.77°` ＝ 本街廓宗地分配線之方位）；短邊 `3.60 m`（方位 `46.03°`）在街廓之後界上 ⇒ 本片與正面線只交於 `p1` 一點（臨正街寬 `0`）。
- `app.py` `_pool_strips_for_block` 之診斷列（`[T2-DIAG]`·態 `981fd1f`）：`R6` 之 `s` 域 ＝ `[-3.6068, 85.8549]`（`s ＝ 0` 為 `p1`·`85.8549` ＝ 正面線長）；池帶 `s` 寬之首項 `3.6068`、面積 `85.7064` ⇒ 本片係**步驟 `5`（業主宗之 `s` 區間之補集）所切之池帶**，其 `s` 區間 ＝ `[-3.6068, 0]`；同函式步驟 `5b`（幾何餘）於 `R6` 無出艙。
- 本片之 `47.68 m` 邊與左側推進之第 `1` 宗之近側界重合（Hausdorff 距 `5.8e-10 m`；以 `1e-9 m` 緩衝量之共界長 `47.6792 m`）：`babc64d` ＝ `628(2)+`、`88dc179` ＝ `628(2)`、`981fd1f` ＝ `628-21(1)`；精確之 boundary 交集長為 `0`（浮點級之縫）。
**成因之具名**：`R6` 之左端無側街（末端塊）；左側推進之第 `1` 宗以過 `p1` 之宗地分配線為其近側界，而街廓左端之界（`133.45°`）與宗地分配線（`137.77°`）不平行（差 `4.32°`）⇒ 二線之間夾一三角形，頂點在 `p1`、底邊 `3.60 m` 在後界；步驟 `5` 取業主宗 `s` 區間之補集時，其 `s ∈ [-3.6068, 0]` 單獨成一池帶。此即 `docs/specs/W-G.4_S1_plan.md` 之 N0-20 所定之「**未臨正街土地**」（逐字·去粗體「沿 ALLOCLINE 方向作直線不與 FRONTLINE 相交之區域」「幾何實作＝末端 ALLOCLINE 半平面 ∩ block」）；同檔逐字「R6 實例 85.71（未臨正街）＋166.57（末端帶）＝252.28㎡」「p1 端楔形（R1 5.33／R6 85.71／0m R3 78.19）＝R_end 內部組成·非「碎片」」（KL 之圖 ＝ `docs/specs/figures/E_V6.jpg`）；`docs/specs/W-G.4_規格_v3.md` 同旨（逐字·去粗體與底線「端部殘片（R1 5.33／R3 78.24／R6 85.71 之類）自此非「碎片」——它們是 R_end 之內部組成」）；`docs/specs/W-G.5_裁定N_乙案_plan_v1.md` 載 `block∩{s<0}` 之面積 `R6` `85.7064` 為「未臨正街真幾何面積」。三檔於進度（一）之態 `babc64d` 皆已在倉。
**正典之處置**：`K-9-36`（末端塊之評選·KL 裁 `2026-09-17`）——跨占 `R_end` 者依原投影序試算，第一個 `G ≥ area(R_end)` 者當選；均未達者 `R_end` 範圍為強制抵費地，得作調配池而⛔ 拆分。其落地狀態（同裁逐字）：「①〜③ 之碼面現況候查（上開補丁十之落點 ＝ `verify/wf_f4.py` 之 `_reshape_block`；七級調配於現行驗證程式內未被執行）；④⑤ ⬜ **未實作**」。
**現碼之行為**（態 `981fd1f`）：`_end_gate` 於 `app.py` 僅見於註解（其判定在凍存之 `verify/wf_f4.py`）；`app.py` 之 `_end_region_R` 有定義而 `app.py` 內⛔ 呼叫（呼叫者 ＝ `verify/wf_f4.py`、`verify/fixture_end_*.py`）⇒ G 值迭代之配地路徑⛔ 構 `R_end`、⛔ 施評選；左側推進之第 `1` 宗自 `p1` 起，本片單獨成一片抵費地（畫面之 `R6-抵費地-2`）。發單側以 `_end_region_R`（帶寬 `3.5 m`）重算 ＝ 末端帶 `166.57`／`R_end` `252.28 ㎡`，與上開規格之「R6 實例」同。
🛑 **⛔ 據本進度推**：`R6` 左端之當選者、任何末端塊之面積（`K-9-36` 逐字「⛔ 推任何末端塊之面積」）、本片之最終歸屬；本片之處置候新調配模組落地 `K-9-36`。
**失效條件四項之現況**：`(1)`、`(2)`、`(4)` 同進度（三）；`(3)` **未成就**——`R6` `85.71` ⇒ **成因已具名**（上開·未臨正街土地·`R_end` 之內部組成）；`R1` `0.0046` ⇒ `GB-186`（成因【未證】）；其餘同進度（三）。
🔴 **進度（一）`(3)` 所載「`R6` `85.71`（三頂點·與任一地主宗⛔ 共界）」之後半與實測不符**（上開重合·態 `babc64d` 即然）⇒ `自誤 544`；**進度（一）〜（三）三度載「成因未具名」，而上開三規格於進度（一）之態已具名之** ⇒ `自誤 545`。
🛑 **⛔ 解除、⛔ 收窄**（`(3)` 未成就）。
````

## 附錄戊　塊 `P4`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：正面道路識別符（五級 `r3`·幾何推導 ∪ 區外道路清單）＋ `GB-178` 之併記（`W-G.9-350`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `981fd1fc09a9fd22484bd3deeadd8a40be1e4a5e`（本批開工態）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 正面道路之幾何推導（`v3` 五級③ `r3`·KL 裁 `2026-09-05`；定義 ＝ `W-G.9-235` 工項一之裁） | `parse_cad_precision_layers` 以所綁 FRONT_LINE 之全部頂點、對非可建築土地之街廓逐一量 `_line_block_overlap`；比值嚴格大於 `R3_FRONT_ROAD_MAJORITY`（`0.5`）者入推導集；恰一 ⇒ 成功、空 ⇒ 區外、`≥ 2` ⇒ 歧義（`r3_front_road_derive`·回傳鍵 `front_road_derive`·畫面與 harness 同一函式） | ✅ | `docs/orders/W-G.9-350_重量單.md` |
| `2` | 區外道路清單 | 載體 ＝ `W-G.9-248` 之「正面道路名稱／識別符」欄；推導有值者⛔ 採其所填；區外／歧義者採正規化後之名稱（`NFKC`·去首尾空白·連續空白併一）；識別符字串相同即同一正面道路（`r3_front_road_identifier`）；畫面步驟 E 之「🧭 正面道路識別」一覽（`r3_front_road_rows`） | ✅（畫面） | 同上 |
| `3` | harness 之區外道路名稱之來源 | 驗證路徑無畫面 ⇒ 區外者之識別符現為「未填」；其來源（資料檔或其他）候新調配模組之單定之 | ⬜ | 同上 `§二` |
| `4` | `r3` 之消費（五級八鍵之排序） | 新調配模組之候選街廓名單（`docs/specs/調配階段_泛用規格_v1.md` 步 `3`）；本批⛔ 建消費端 | ⬜ | 「調配階段之諸裁」節 |

🔒 **本批之讀法**（發單側之工程裁·⛔ 域裁·已以通知呈 KL）：① 「沿線過半」逐候選量之（某一道路街廓自身之重疊長 ÷ 正面線長），⛔ 以諸候選之合計量之；恰半⛔ 入。② 候選 ＝ 非可建築土地之街廓（與綁定用之 `_buildable_blocks` 同一判準之補集·⛔ 分區名字面）。③ 使用者於區外者所填之名稱若與某區內道路街廓之名稱相同（如 `RD2`），即視為與之同一條道路。
🔒 **本案之推導**（態 `981fd1f` ＋ 本批·harness）：`R2` ＝ `RD1`；`R3`、`R5` ＝ `RD2`；`R6` ＝ `RD3`；`R1`、`R4` ＝ 區外（區內道路沿其正面線者最多 `4.20%`／`3.75%`）。**配地⛔ 變**（量測器 `F8` 之 `run` 二退縮之出艙改前改後逐位同）。
🔒 **依賴序**（改自 `W-G.9-349` 之更新·其「正面道路識別符」一環已落地）：新調配模組（「調配階段之諸裁」節之序 `1`〜`8`；本表序 `3`、`4` 併入之）。
🔒 **本機介面**：主 checkout 同步後，步驟 E（可建築街廓路寬）之各街廓卡片於「正面道路名稱／識別符」欄下多一句圖推導之說明，其下多「🧭 正面道路識別」一覽；`R1`、`R4` 須於該欄填名（臨同一條區外道路者填相同名稱）並按「✅ 儲存路寬資料」。
🔒 **併記（`GB-178`）**：「待落地清單之更新：`GB-182` 之修入主線（…）（`W-G.9-342`）」節序 `2` 所列失效條件 `(3)` 未成就之 `R6` `85.71`，其成因已於 `GB` 簿 `GB-178` 之進度（四）具名（`R6` 左端〔無側街〕之未臨正街土地·`R_end` 之內部組成·處置候 `K-9-36` 於新調配模組之落地）；`(3)` 仍未成就（`R1` `0.0046`·`GB-186`）；`GB-178` 之態⛔ 變（🔶）。
🩸 **前節之自載更正**：「待落地清單之更新：閘二…（`W-G.9-349`）」節末列所載「`⬜` 字樣 ＝ `1`·列 ＝ `1`」係只計其序 `3` 一列；含圖例與該列自身之實數 ＝ 字樣 `5`·列 `3`（`自誤 543`·⛔ 追改前節一字）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `7`（子字串框·含圖例與本列）·列 ＝ `5`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: eff286693d8ff8e82dea5beccb22304329eb8ed715134e05816a65bb40b70d8d
