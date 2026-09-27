# `W-G.9-351`　重量單：新調配模組之首環——調配階段之輸入盤點（需調配之土地與合併單位·`K-9-45`／`K-9-46`·僅顯示）＋ 待落地清單之更新（新調配模組之單序）＋ 主 checkout 同步之撞檔前置

> **發單** ＝ 發單側窗四十七·`2026-09-27`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**；工項五於 **KL 之主 checkout**）。
> **級** ＝ **重**（生產碼 `1` 檔：`app.py`；**⛔ 土地後果**——僅增一覽之顯示，配地之出艙改前改後逐位同，見 `§一` 項 `7`／`8`／`9`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `2517c5133fe4b87d4508b513571dfb8391bdef8c`。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D1`／`F10`／`P5` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）。
> 🔑 **來源檔一**（檔名逐字 `W-G.9-351_重量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項五之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F10`）與改動（`D1`、`P5`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：塊 `D1` 以外之生產碼一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`K-6` 典／`VR` 簿／`GB` 簿／自誤簿之一字（本批⛔ 鑄任何號）；任何側支之刪除或改寫。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `2517c5133fe4b87d4508b513571dfb8391bdef8c`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 545 541` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔 **`903`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗四十七實跑 `python verify/probes/wg9268_gate6_occupancy.py 2517c51 W-G.9-351 W-G.9-350 W-G.9-398`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-351`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-350` | `2`／`6`／`6` | `2`／`6`／`6` | `12` | `3` | `4`／`46` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `3`／`5` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `9`／`9` | 🟢 |

**本批⛔ 鑄任何號**（自誤／`GB`／`VR`／`K-9` 皆⛔）；收工閘 `6`／`7` 以之驗其 `MAX` ⛔ 推進。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `2517c51`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`F10`／`P5` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二前置之任一期不符（尤：`F10` 三子命令之施前 `rc ≠ 1`） |
| `5` | 塊 `D1` 之 `git apply --check` 不過；或施後之 blob ≠ `§五-1` 項 `5` |
| `6` | 工項二之驗 `V-1`〜`V-5` 任一 ≠ 期（尤：`V-2` 之配地出艙改前改後有任一位元組相異；`V-5` 之相異項 ≠ `0`，或 `cmp` 之異列有非時戳／耗時者） |
| `7` | 工項二之 `push` 無 `§二` 之放行；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項三之 `CLAUDE.md` 之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項五：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒 |
| `11` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `12` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `7`。

---

## `§一`　態錨（發單側窗四十七自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `2517c5133fe4b87d4508b513571dfb8391bdef8c`；側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`30`**（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼（開工態 blob） | `app.py` `3ea96402e032f8f19f1af367d3428d16b5458bba`（`1518340` B） |
| `3` | `W-G.9-350` 之復驗 | 發單側窗四十七依交接文四十六 `§四-1` 逐項自倉重跑：逐 `commit` 對拍（單 ＝ 所發之第 `2` 版 `41a55040…`；`F9`／`D1`／`E3`／`G3`／`P4` 逐位同；`D1` 施於 `e7bad89` 得 `3ea96402…`）、三檔 bytes 與嚴格前綴、收工閘 `1`〜`13`、`F8 run` 二退縮改前改後 `cmp`、`run_all` 二態（`e7bad89` 對 `7202325`·同一倉外路徑·`cmp` 逐位同·`64` 項·PASS `28`／FAIL `36`·對帳 `22／36`）——**全數相符**；KL 主 checkout（經 KL 核准之唯讀存取）：`HEAD` → `wip/s1-endpart` ＝ `2517c51…`、`app.py` ＝ `3ea96402…`；其操作紀錄載 `2026-09-27 05:36` 由 KL 手動自 `88dc179` 快轉至 `981fd1f`、`08:21` 工項五自 `981fd1f` 快轉至 `2517c51` |
| `4` | 本批之受詞 | `docs/specs/調配階段_泛用規格_v1.md` 步 `1` 之尾〜步 `2`（合併單位之成立）與 `§二` 之「合併單位」「合併單位之原街廓」；正典 ＝ `K-9-45`（一）（受詞：不能於原街廓分配之土地，連同該歸戶位於公設地、道路上及其他建築街廓內不得分配之土地）、`K-9-46`（一）（兼有者屬建地軌；全無建築街廓內土地者屬公設軌）與（三）（原街廓 ＝ 其建築街廓內土地所在之街廓；分處二以上者取應分配面積較大者；全無者 ⇒ 無原街廓）；依賴序 ＝ `CLAUDE.md`「🔧 待落地清單之更新：正面道路識別符…（`W-G.9-350`）」節（其前置皆已落地） |
| `5` | 改後之盤點（harness·塊 `D1` 施後·`F10 run`） | 見下表；二退縮之全部切片皆 `126`（殘料 `8`）·原有面積 `34860.73 ㎡`；「建築街廓內不能分配」＝ `W-G.9-349` 之入池宗（`CLAUDE.md`「🔧 待落地清單之更新：閘二…（`W-G.9-349`）」節之「本案之土地後果」：`3.5 m` 入池 `22` 宗·`2363.40 ㎡`；`0 m` `23` 宗·`2513.70 ㎡`） |
| `6` | 施後 blob | `app.py` `cdbbbe08116c00c24f143050c590a3c61b485ac3`（`1535668` B·增 `262`／刪 `0`·純加性） |
| `7` | 配地⛔ 變（量測器 `F8` 之 `run`） | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5`／`… 0.0` 於工項一之端與工項二之 `commit` 各跑一次：二退縮之全部出艙**逐位相同**（`cmp`）；`rc 0`·末列 `⇒ 紅 []；rc 0` |
| `8` | 畫面對 harness（`verify/probes/probe_WG9345_screen.py parity <R> <退縮> on`） | 施後：`3.5` ⇒ `rc 0`（配地列 harness `36`／畫面 `35`·不符格 `0`）；`0.0` ⇒ `rc 0`（`37`／`36`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（同 `W-G.9-350 §一` 項 `8`） |
| `9` | `run_all`（同一倉外路徑·工項一之端 對 工項二之 `commit`） | 二份全檔**逐位相同**（`cmp`·各 `237412` B）：`64` 項·PASS `28`／FAIL `36`·對帳段「名目：凍存 `22`／現況 `36`」；`python verify/probes/probe_WG9343_step0_flag.py runall` ⇒ 相異項 `0`·末端夾具／golden 列 `21／21`·`rc 0` |

**`§一` 項 `5` 之表**（harness·`F10 run`·「應分配面積」＝ 原位次該趟之 `G`·㎡）：

| 退縮 | 合併單位（建地軌·公設軌） | 待同歸戶併入之歸戶 | 原位次配地 片／㎡ | 建築街廓內不能分配 片／㎡ | 共同負擔用地·入合併單位 片／㎡ | 共同負擔用地·待同歸戶併入 片／㎡ |
|---|---|---|---|---|---|---|
| `3.5 m` | `23`（`15`·`8`） | `9` | `43`／`21412.68` | `22`／`2363.40` | `40`／`8404.65` | `13`／`2680.00` |
| `0 m` | `24`（`16`·`8`） | `9` | `36`／`20216.35` | `23`／`2513.70` | `45`／`9251.13` | `14`／`2879.55` |

**建地軌之原街廓**（歸戶 ＝ 原街廓〔逐街廓之應分配面積〕）：
- `3.5 m`：`G001` ＝ `R1`〔R1 86.00〕；`G004` ＝ `R2`〔R2 71.59〕；`G006` ＝ `R2`〔R2 65.45〕；`G009` ＝ `R6`〔R3 44.90、R5 148.72、R6 153.19〕；`G011` ＝ `R3`〔R2 3.81、R3 92.46〕；`G014` ＝ `R3`〔R3 135.94〕；`G018` ＝ `R2`〔R2 146.58〕；`G020` ＝ `R2`〔R2 147.18〕；`G021` ＝ `R2`〔R2 58.95〕；`G025` ＝ `R5`〔R5 0.99、R6 0.26〕；`G026` ＝ `R5`〔R5 3.15〕；`G027` ＝ `R5`〔R5 10.72〕；`G030` ＝ `R3`〔R2 27.55、R3 28.34〕；`G032` ＝ `R6`〔R6 117.74〕；`G033` ＝ `R3`〔R3 72.78〕
- `0 m`：`G001` ＝ `R1`〔R1 86.00〕；`G004` ＝ `R2`〔R2 71.59〕；`G006` ＝ `R2`〔R2 65.45〕；`G007` ＝ `R2`〔R2 86.72〕；`G009` ＝ `R6`〔R3 44.90、R5 148.72、R6 153.19〕；`G011` ＝ `R3`〔R2 3.82、R3 87.94〕；`G014` ＝ `R3`〔R3 129.41〕；`G018` ＝ `R2`〔R2 146.58〕；`G020` ＝ `R2`〔R2 147.18〕；`G021` ＝ `R2`〔R2 58.95〕；`G025` ＝ `R5`〔R5 0.99、R6 0.26〕；`G026` ＝ `R5`〔R5 3.15〕；`G027` ＝ `R5`〔R5 10.72〕；`G030` ＝ `R2`〔R2 27.45、R3 24.22〕；`G032` ＝ `R6`〔R6 117.74〕；`G033` ＝ `R3`〔R3 72.78〕

---

## `§二`　KL 之語與射程

🔒 **KL 之語（`2026-09-27 11:30`·發單側窗四十七·逐字）**：「同意,繼續下一步」——所答者為發單側窗四十七前一則覆命之末段逐字「如同意，本窗即讀 `docs/specs/調配階段_泛用規格_v1.md` 全文並擬新調配模組之單；有土地後果者，附圖依格式請示。」
🔒 **所據之既裁**：`K-9-45`（KL `2026-09-22`）、`K-9-46`（KL `2026-09-23`）；規格 `docs/specs/調配階段_泛用規格_v1.md`（`W-G.9-332` 入倉·其【讀】皆經【通知】呈 KL、未示異議）。
🔒 **本單之讀法**（發單側之工程裁·⛔ 域裁·已以【通知】呈 KL）：
① 原街廓之比較所用之「應分配面積」＝ 原位次該趟之 `G`——不配地之宗 ＝ 其不配地紀錄之 `G`；入池之合併單元（`K-9-29 六`）以單元計一次（`K-9-46` 其一所呈【通知】第 `1` 則「以兩側之應分配面積比較」·KL 無異議）；並列 ⇒ 停機（【未裁】）。
② 同歸戶已有原位次配地、而無建築街廓內不能分配之土地者，其公設地、道路上之土地⛔ 先成合併單位，候規格步 `4`（道路五則、公設地併入·「兩側皆無」「超過剩餘池」者始轉合併單位）；全無建築街廓內土地者 ＝ 公設軌（規格步 `2`）。
③ 段三（`K-6 §二 段三`）所併出之片 ＝ 原位次配地（其配地街廓 ＝ 受併宗之街廓）。
④ 無地號之殘料（`_is_ghost_sliver`·原有面積恆 `0`）⛔ 入任何單位；非共同負擔／未分類之街廓上之切片、無歸戶之切片 ⇒ 停機（【未裁】·本案皆無）。
🔒 **【通知】（`K-9-46` 所載本案之例之現值·⛔ 追改該典一字）**：其例係態 `338bd08`·退縮 `0 m`；現態依同一規則——歸戶 `G025` 之原街廓 ＝ `R5`（`628-53(2)` 之應分配面積 `0.99` ＞ `628-53(1)` 之 `0.26`；例載 `R6`〔其時 `0.00`／`0.26`〕·二退縮同）；歸戶 `G030` ＝ 退縮 `0 m` `R2`（`27.45` ＞ `24.22`）、退縮 `3.5 m` `R3`（`28.34` ＞ `27.55`）（例載 `R3`〔其時 `20.52`／`26.54`〕）。本批只顯示、⛔ 據之配地。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項二之生產碼 `commit` 推入主線之放行，CC 將其逐字載入報告；**無之 ⇒ 工項二之驗畢後停於推送前，於對話請示 KL**。所答之【要你判斷】逐字：「同意將『調配階段之輸入盤點（需調配之土地與合併單位之一覽·只顯示）』之程式推入主線嗎？此改動不改變任何配地結果。（是／否）」

🔒 **逐筆放行清單**：本批動生產碼者恰 **`1`** 筆（工項二）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `app.py`（新 module 級常數 `ADJ_*`／`SS_ADJ_BUILD_FINAL`／`SS_ADJ_DROPPED` 與函式 `adj_intake`／`adj_intake_rows`；`K6B_SCREEN_TRIAL_KEYS` 增二鍵（置於其末項 `f3_k929_6_log` 之前）；`_k929_6_screen_gate` 於復原之後另寫末趟之不配地紀錄（其回傳⛔ 變）；`f3_screen_stepg_run` 之去／寫末態 build；`main()` 成果區之「🧩 調配階段之輸入」一覽） | 塊 `D1` | ⛔ 無（`§一` 項 `7`／`8`／`9`） |

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至主線；`(b)` 工項二之 `push` 以本節之放行為條件；`(c)` 工項五於 KL 本機之主 checkout·⛔ `commit`；`(d)` ⛔ 及其他任何生產碼、任何他錨；`(e)` ⛔ 建調配之任何後步（候選街廓名單、同歸戶合併、池之進入與落位、½ 之判）——另單；`(f)` ⛔ 動任何宗之 `G`、幾何、配地。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-351_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-351 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F10` 入倉（主線·零生產碼）

塊 `F10` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9351_intake.py`（**新檔**）。`commit` 訊息逐字 `W-G.9-351 工項一：量測器 F10（調配之輸入盤點）入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項二　塊 `D1`：調配階段之輸入盤點（🔴 生產碼·一 `commit`·⛔ 土地後果）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9351_intake.py selftest <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
2. `python verify/probes/probe_WG9351_intake.py wiring <repo>` ⇒ **`rc 1`**（`W1`、`W2a`〜`W2c`、`W3`、`W5` 皆紅，`W4` 綠；突變 `N1`／`N2`／`N4`「突變錨不存在」、`N3` 轉紅 `['W4']`）。
3. `python verify/probes/probe_WG9351_intake.py run <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D1` 依圍欄之逐列索引抽出為 `<O>\D1.diff`、對拍 `§五-1` 後，`git apply --check <O>\D1.diff` ⇒ 過；`git apply <O>\D1.diff`；`git hash-object app.py` ＝ `cdbbbe08116c00c24f143050c590a3c61b485ac3`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-351 工項二：調配階段之輸入盤點（需調配之土地與合併單位·K-9-45／K-9-46·僅顯示）🔴 生產碼（⛔ 土地後果）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9351_intake.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `S1`〜`S18`、`R1`／`R2`、`M0` 皆 ✅，`M1`〜`M4` 皆「轉紅」；`wiring` 之 `W1`、`W2a`〜`W2c`、`W3`〜`W5` 皆 ✅，`N1`〜`N4` 皆「轉紅」 |
| `V-2` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `cmp` | 皆 **`rc 0`**；**`cmp` 皆逐位相同**（配地⛔ 變；發單側 Linux 實測如此·該器之出艙⛔ 含路徑與時戳） |
| `V-3` | `python verify/probes/probe_WG9351_intake.py run <repo>` | **`rc 0`**；`R1`〜`R5` 於二退縮皆 ✅；總句與逐類之數 ＝ `§一` 項 `5` 之表；建地軌之原街廓 ＝ 同項之列 |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35.json`；同 `0.0`；`python verify/probes/probe_WG9348_harvest_key.py <repo>`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>`；`python verify/probes/probe_WG9340_main_synth.py <repo>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9350_frontroad.py selftest <repo>`；`… wiring <repo>`；`… run <repo>` | 皆 **`rc 0`**；`parity` ＝ `§一` 項 `8`；`wfns_ast` `43`／`43`／`42`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」 |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `cmp <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`cmp` 期逐位相同（發單側 Linux 實測如此）——若不同，出艙其全部異列：異列皆為時戳／耗時者屬白名單 `8`（自解），否則停機款 `6` |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（`§二` 之放行成立後·與驗為分開之呼叫）：`git push origin HEAD:wip/s1-endpart`。

### 工項三　待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `P5` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位**附於** `CLAUDE.md` 之末。刪除欄 `0`、改前全檔為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-351 工項三：待落地清單之更新（新調配模組之首環與單序）⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項四　執行報告入倉（主線·新檔 `docs/reports/W-G.9-351R_調配之輸入盤點_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F10` 三子命令之全文、`F8 run` 二份之 `cmp` 結果、`parity` 二份之 `rc` 與末三列、`runall` 對拍之全文與 `cmp` 結果）；④ 三塊之實得（bytes／`sha256`）與 `CLAUDE.md` 之改前改後 bytes；⑤ `§二` 之放行（KL 之逐字或請示之經過）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-351 工項四：執行報告入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項五　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542` 之攔法·分開之呼叫）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、逐檔出艙其路徑、二 blob 與處置；`A ∩ U` 為空者出艙「空」。
   🔒 KL 主 checkout 之現態（發單側窗四十七經 KL 核准之唯讀存取·`§一` 項 `3`）＝ `2517c51`；其根有 `W-G.9-350_重量單.md`（未追蹤·與入倉 blob `370b2ea1…` 逐位同）——其路徑⛔ 在本次之 `A`，⛔ 動之；本單之複本若置於主 checkout 之 `docs/orders/`，即落於 `A ∩ U`——依丙處置之，⛔ 預設其態。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項四 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `cdbbbe08116c00c24f143050c590a3c61b485ac3`。
任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項四之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 逐檔 **`0`**（工項二 ＝ `app.py` 增 `262`／刪 `0`） |
| `2` | 生產碼 `34` 檔對 `2517c51` | 相異恰 **`1`**（`app.py` ＝ `cdbbbe08…`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`5` 檔） |
| `4` | `CLAUDE.md` 之 bytes | `272943 → 277812`；改前為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`30`**；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 545 545 .` | **`rc 0`**（自誤 `MAX` 仍 `545`·本批⛔ 鑄） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 545 545` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `530`／`MAX` `545`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `186`／`193`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `45`／`48`／`[44, 47]`（皆 ＝ 開工態） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·`43`／`43`／`42` |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9351_intake.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之替身 ＋ 塊 `F10` ＋ 塊 `D1` ＋ 塊 `P5` ＋ 報告之替身·五 `commit`）並實跑閘 `1`〜`4`、`6`〜`14` ⇒ 見 `§五-1` 項 `8`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D1` | `20347` B·`sha256` `7d16a98b2a1d45177f2de2fc7ad4f0039ff845cc1c29288d33d7e91475bd8e33`·`315` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F10` | `30178` B·`sha256` `45b5dcc59ea69fea79b06e526f86a333b62f6aca3df9aa2b1ae25bc18c3335e6`·`558` 列（圍欄內全文·末附換行） |
| `4` | 塊 `P5` | `4869` B·`sha256` `00db0aeded3dbb97767b84c6c94b58ec9649159057a27e145c0991db40dbc840`·`23` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`272943` B）之末後，期末 ＝ `277812` B |
| `5` | 施 `D1` 後之 blob | `app.py` `cdbbbe08116c00c24f143050c590a3c61b485ac3`（`1535668` B）（開工態 `3ea96402…`） |
| `6` | `F10` 之二態 | 開工態（工項一之端）`selftest`／`wiring`／`run` 皆 `rc 1`；施 `D1` 後皆 `rc 0` |
| `7` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十七實跑（態 `2517c51`）：🔴 機械 `0` 項／🟡 提示 `5` 項——`P-1` `:120`（工項二前置之段·所觸之字樣係 `F10 wiring` 施前出艙之「突變錨…」一語之引述，⛔ 全稱否定 ⇒ **具名豁免**）、`P-1` `:705`／`:894`（塊 `F10` 之碼·所觸之字樣係該器自身之出艙文字 ⇒ **具名豁免**）、`P-4` `:133`／`:170`（工項二之驗、`§四` 收工閘之表頭·其箭頭之座標系皆為「改前〔工項一之端／`2517c51`〕至改後〔工項二之 `commit`／工項四之端〕」，表內自載 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `18509`–`26123`）⇒ `rc 0` |
| `8` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`2517c51` ＋ 五 `commit`：本單之前稿〔僅 `§一` 項 `9` 與本表項 `7`／`8` 三格未填〕＋ 塊 `F10` ＋ 塊 `D1`〔自前稿依抽取式抽出·`git apply` 過〕＋ 塊 `P5` ＋ 報告之替身）：閘 `1` 逐檔刪 `0`（工項二 `app.py` 增 `262`）；閘 `2` 相異恰 `1`（`34` 檔·`cdbbbe08…`）；閘 `3` `CR` 合計 `0`（`5` 檔·判別力 `12308`）；閘 `4` `272943 → 277812`（嚴格前綴）；閘 `6`〜`14` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `43`／`43`／`42`；「app 側宿主 ＝ f3_screen_stepg_run」；`F8` 二子命令、`F9` 三子命令與 `F10` 三子命令之末列 `⇒ 紅 []；rc 0`）；跑畢追蹤檔之變動 `0` |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零、一、三、四 ⇒ 逕行 `push` 主線；工項二 ⇒ 依 `§二` 之放行、驗皆符後推主線；工項五 ⇒ KL 本機之主 checkout。
3. 收工後，主 checkout 之根之來源檔（本單，及工項五所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D1`（`git apply` 之差異·`app.py`）

````diff
diff --git a/app.py b/app.py
index 3ea9640..cdbbbe0 100644
--- a/app.py
+++ b/app.py
@@ -10967,6 +10967,229 @@ def r3_front_road_rows(labels, derive_by_label, name_by_label):
     return {'rows': _rows, 'groups': _groups, 'group_lines': _lines, 'missing': _missing}
 
 
+# ── 🆕 `W-G.9-351`：調配階段之輸入（`docs/specs/調配階段_泛用規格_v1.md` 步 `1` 之尾〜步 `2`·`K-9-45`／`K-9-46`）──
+#   受詞 ＝ 原位次（含段三、入池閘）之末態：每一重劃前切片恰歸一類；同歸戶者組合併單位（軌、原街廓）。
+#   🔒 純函式·⛔ 讀 session；一切外部量由參數注入（畫面 ＝ `main()` 成果區；harness ＝ 量測器 `F10`）。
+#   🛑 本批⛔ 調配、⛔ 動任何宗之 `G` 與幾何、⛔ 建消費端（任何配地、G 式、判定⛔ 讀此值·步 `3` 起另單）。
+#   🔒 判別以**負擔屬性**（`F3_CATEGORY_BURDEN` 之值）為之，⛔ 以分區名之字面。
+ADJ_DISP_ALLOC = '原位次配地'
+ADJ_DISP_POOL = '建築街廓內不能分配'
+ADJ_DISP_COMMON_UNIT = '共同負擔用地·入合併單位'
+ADJ_DISP_COMMON_STEP4 = '共同負擔用地·待同歸戶併入'
+ADJ_DISP_GHOST = '無地號之殘料'
+ADJ_TRACK_BUILD = '建地軌'
+ADJ_TRACK_PUBLIC = '公設軌'
+ADJ_BURDEN_BUILD = '可建築土地'
+ADJ_BURDEN_COMMON = '共同負擔'
+ADJ_ALLOC_SIDES = ('left', 'right')
+ADJ_POOL_SIDE = '抵費地'
+#: 畫面之二鍵（旗標 on·非試算趟）：入池閘之末態 build（配地本體與 `f3_G_values` 同寫）與其末趟之不配地紀錄（入池閘之畫面入口寫）。
+SS_ADJ_BUILD_FINAL = 'f3_k929_6_build'
+SS_ADJ_DROPPED = 'f3_k929_6_dropped'
+
+
+def adj_intake(temp_parcels, build_final, g_rows, dropped, own_map, burden_by_block):
+    """`W-G.9-351`：調配階段之輸入盤點（純函式）。
+
+    參數
+      temp_parcels     段三後之全部重劃前切片（含共同負擔用地上者；段三所併出者帶鍵 `段三併出`）。
+      build_final      入池閘之末態 build（合併單元帶鍵 `入池閘併入`）。
+      g_rows           以 `build_final` 所跑之 G 值列（`推進側別` ∈ `left`／`right` ⇒ 原位次配地；`抵費地` ⇒ 池列）。
+      dropped          同一趟之不配地紀錄 `{(街廓, 側): [{暫編地號, G(㎡), 不配地由…}]}`。
+      own_map          `{原地號: 歸戶}`。
+      burden_by_block  `{街廓: 負擔屬性}`（`F3_CATEGORY_BURDEN` 之值）。
+    回傳 `{'slices', 'units', 'step4', 'totals'}`：
+      `slices` ＝ 逐切片之類（`ADJ_DISP_*`）；`units` ＝ 合併單位（`K-9-45`（一）·軌 `K-9-46`（一）·
+      原街廓 `K-9-46`（三）：其建築街廓內不能分配之土地所在之街廓，分處二以上者取應分配面積〔該趟之 `G`〕較大者）；
+      `step4` ＝ 同歸戶有原位次配地而無不能分配者之共同負擔用地（待同歸戶併入·候步 `4` 之道路五則／公設地併入）；
+      `totals` ＝ 逐類之切片數與原有面積（`分攤登記面積_m2`·⛔ 含 `a′` 累加器）。
+    停機（`RuntimeError`·⛔ 靜默略過）：切片或列之身分重複／缺漏；G 值列有未知之 `推進側別`；
+      build 之宗既非配地亦非不配地、或二者兼是；可建築土地上之切片不在 build；段三之受併宗未配地；
+      切片之街廓無負擔屬性、或屬非共同負擔／未分類（【未裁】）；非殘料之切片無歸戶；
+      殘料之原有面積 `> 0`；原街廓之應分配面積並列（【未裁】）。
+    🔒 殘料（`_is_ghost_sliver`）⛔ 入任何合併單位（無地號·無地主）；其於 build／G 值列者略之。
+    """
+    _EPS = 1e-9
+
+    def _pid(t):
+        return str(t.get('暫編地號'))
+
+    def _a(t):
+        return float(t.get('分攤登記面積_m2', 0) or 0)
+
+    _slices = list(temp_parcels or [])
+    _ghost = [t for t in _slices if t.get('_is_ghost_sliver')]
+    _real = [t for t in _slices if not t.get('_is_ghost_sliver')]
+    for t in _ghost:
+        if _a(t) > _EPS:
+            raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 殘料 {_pid(t)!r} 之原有面積 {_a(t)!r} > 0 ⇒ 停機")
+    _by = {}
+    for t in _real:
+        if _pid(t) in _by:
+            raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 切片 {_pid(t)!r} 重複 ⇒ 停機")
+        _by[_pid(t)] = t
+    _ghost_ids = {_pid(t) for t in _ghost}
+    _alloc, _odd = set(), set()
+    for _r in g_rows or []:
+        _s = _r.get('推進側別')
+        _k = str(_r.get('暫編地號'))
+        if _k in _ghost_ids:
+            continue
+        if _s in ADJ_ALLOC_SIDES:
+            if _k in _alloc:
+                raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] G 值列之 {_k!r} 重複 ⇒ 停機")
+            _alloc.add(_k)
+        elif _s != ADJ_POOL_SIDE:
+            _odd.add(str(_s))
+    if _odd:
+        raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] G 值列有未知之推進側別 {sorted(_odd)} ⇒ 停機（⛔ 臆其去向）")
+    _drop_g, _drop_why, _drop_blk = {}, {}, {}
+    for (_blk_d, _side_d), _lst in sorted((dropped or {}).items()):
+        for _e in _lst or []:
+            _k = str(_e.get('暫編地號'))
+            if _k in _drop_g:
+                raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 不配地紀錄之 {_k!r} 重複 ⇒ 停機")
+            _drop_g[_k] = float(_e.get('G(㎡)') or 0)
+            _drop_why[_k] = str(_e.get('不配地由', '—') or '—')
+            _drop_blk[_k] = str(_blk_d)
+    _unit_of, _bf_ids = {}, set()
+    for _u in build_final or []:
+        if _u.get('_is_ghost_sliver'):
+            continue
+        _up = _pid(_u)
+        if _up in _bf_ids:
+            raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] build 之 {_up!r} 重複 ⇒ 停機")
+        _bf_ids.add(_up)
+        for _m in (_u.get('入池閘併入') or [_up]):
+            _m = str(_m)
+            if _m in _unit_of:
+                raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 切片 {_m!r} 屬二以上之 build 單元 ⇒ 停機")
+            _unit_of[_m] = _up
+    _both = sorted(_bf_ids & _alloc & set(_drop_g))
+    _none = sorted(_bf_ids - _alloc - set(_drop_g))
+    if _both or _none:
+        raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] build 之宗兼為配地與不配地 {_both}／二者皆非 {_none} ⇒ 停機")
+    _stray = sorted((_alloc | set(_drop_g)) - _bf_ids)
+    if _stray:
+        raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] G 值列或不配地紀錄之 {_stray} 不在 build ⇒ 停機")
+    _rows = []
+    for t in _real:
+        _k, _bl = _pid(t), str(t.get('所屬街廓', ''))
+        if _bl not in (burden_by_block or {}) or not (burden_by_block or {}).get(_bl):
+            raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 切片 {_k!r} 之街廓 {_bl!r} 無負擔屬性 ⇒ 停機")
+        _bt = burden_by_block[_bl]
+        _g = str((own_map or {}).get(str(t.get('原地號', '')), '') or '')
+        if not _g:
+            raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入]【未裁】切片 {_k!r}（原地號 {t.get('原地號')!r}）無歸戶 ⇒ 停機")
+        _row = {'暫編地號': _k, '原地號': str(t.get('原地號', '')), '歸戶': _g, '所屬街廓': _bl,
+                '負擔屬性': _bt, '原有面積': _a(t), '重劃前地價區段': str(t.get('重劃前地價區段', '') or ''),
+                '所屬單元': '', '應分配面積': None, '不配地由': '', '配地街廓': []}
+        if '段三併出' in t:
+            _rcv = [str(_x) for _x in (t.get('段三併出') or [])]
+            if not _rcv or any(_x not in _alloc for _x in _rcv):
+                raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 段三所併出之 {_k!r} 之受併宗 {_rcv} 未配地 ⇒ 停機")
+            _row.update(類=ADJ_DISP_ALLOC, 所屬單元='段三併入 ' + '、'.join(_rcv),
+                        配地街廓=sorted({str((_by.get(_x) or {}).get('所屬街廓', '')) for _x in _rcv}))
+        elif _bt == ADJ_BURDEN_BUILD:
+            if _k not in _unit_of:
+                raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 可建築土地上之切片 {_k!r} 不在 build ⇒ 停機")
+            _up = _unit_of[_k]
+            _row['所屬單元'] = _up
+            if _up in _alloc:
+                _row.update(類=ADJ_DISP_ALLOC, 配地街廓=[_bl])
+            else:
+                if _drop_blk.get(_up) != _bl:
+                    raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] {_k!r} 之街廓 {_bl!r} 與其不配地紀錄之街廓 "
+                                       f"{_drop_blk.get(_up)!r} 不同 ⇒ 停機")
+                _row.update(類=ADJ_DISP_POOL, 應分配面積=_drop_g[_up], 不配地由=_drop_why[_up])
+        elif _bt == ADJ_BURDEN_COMMON:
+            _row['類'] = ADJ_DISP_COMMON_STEP4   # 暫記·依歸戶定之（下）
+        else:
+            raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入]【未裁】切片 {_k!r} 位於負擔屬性 {_bt!r} 之街廓 {_bl!r} ⇒ 停機"
+                               "（⛔ 臆其調配之處置）")
+        _rows.append(_row)
+    _missing = sorted(set(_unit_of) - {_r['暫編地號'] for _r in _rows})
+    if _missing:
+        raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] build 之成員 {_missing} 不在切片 ⇒ 停機")
+    _byg = {}
+    for _r in _rows:
+        _byg.setdefault(_r['歸戶'], []).append(_r)
+    _units, _step4 = [], []
+    for _g in sorted(_byg):
+        _rs = _byg[_g]
+        _pool = [_r for _r in _rs if _r['類'] == ADJ_DISP_POOL]
+        _al = [_r for _r in _rs if _r['類'] == ADJ_DISP_ALLOC]
+        _cm = [_r for _r in _rs if _r['負擔屬性'] == ADJ_BURDEN_COMMON and _r['類'] != ADJ_DISP_ALLOC]
+        _al_blk = sorted({_b for _r in _al for _b in _r['配地街廓']})
+        if _pool or (_cm and not _al):
+            for _r in _cm:
+                _r['類'] = ADJ_DISP_COMMON_UNIT
+            _track = ADJ_TRACK_BUILD if _pool else ADJ_TRACK_PUBLIC
+            _home, _basis = None, {}
+            if _pool:
+                _seen = set()
+                for _r in _pool:
+                    if _r['所屬單元'] in _seen:
+                        continue
+                    _seen.add(_r['所屬單元'])
+                    _basis[_r['所屬街廓']] = _basis.get(_r['所屬街廓'], 0.0) + float(_r['應分配面積'])
+                _top = max(_basis.values())
+                _cands = sorted(_b for _b, _v in _basis.items() if abs(_v - _top) <= _EPS)
+                if len(_cands) != 1:
+                    raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入]【未裁】歸戶 {_g} 之原街廓：應分配面積並列 {_cands} "
+                                       f"（{_top!r}）⇒ 停機（⛔ 自裁）")
+                _home = _cands[0]
+            _units.append({'歸戶': _g, '軌': _track, '原街廓': _home, '原街廓之據': _basis,
+                           '建築街廓內不能分配': _pool, '共同負擔用地': _cm,
+                           '原有面積合計': sum(_r['原有面積'] for _r in _pool + _cm),
+                           '同歸戶原位次配地之街廓': _al_blk})
+        elif _cm:
+            _step4.append({'歸戶': _g, '共同負擔用地': _cm, '原有面積合計': sum(_r['原有面積'] for _r in _cm),
+                           '同歸戶原位次配地之街廓': _al_blk})
+    _tot = {}
+    for _r in _rows:
+        _c = _tot.setdefault(_r['類'], [0, 0.0])
+        _c[0] += 1
+        _c[1] += _r['原有面積']
+    _tot[ADJ_DISP_GHOST] = [len(_ghost), sum(_a(t) for t in _ghost)]
+    return {'slices': _rows, 'units': _units, 'step4': _step4, 'totals': _tot,
+            'all_area': sum(_a(t) for t in _slices), 'all_count': len(_slices),
+            'n_alloc_units': len(_bf_ids & _alloc), 'n_drop_units': len(_bf_ids & set(_drop_g))}
+
+
+def adj_intake_rows(intake):
+    """`W-G.9-351`：調配之輸入之顯示列（純函式·各欄皆字串·⛔ 混型欄）。回 `{'units', 'step4', 'totals', 'lines'}`。"""
+    def _pc(_r):
+        return f"{_r['暫編地號']}〔{_r['所屬街廓']}·{_r['原有面積']:.2f}〕"
+
+    _u = []
+    for _x in intake['units']:
+        _u.append({
+            '歸戶': _x['歸戶'], '軌': _x['軌'], '原街廓': _x['原街廓'] or '—（無建築街廓內土地）',
+            '原街廓之據（應分配面積㎡）': '、'.join(f"{_b} {_v:.2f}" for _b, _v in sorted(_x['原街廓之據'].items())) or '—',
+            '建築街廓內不能分配之土地': '、'.join(_pc(_r) for _r in _x['建築街廓內不能分配']) or '—',
+            '公設地／道路上之土地': '、'.join(_pc(_r) for _r in _x['共同負擔用地']) or '—',
+            '原有面積合計(㎡)': f"{_x['原有面積合計']:.2f}",
+            '同歸戶原位次配地之街廓': '、'.join(_x['同歸戶原位次配地之街廓']) or '—',
+        })
+    _s4 = []
+    for _x in intake['step4']:
+        _s4.append({
+            '歸戶': _x['歸戶'], '公設地／道路上之土地': '、'.join(_pc(_r) for _r in _x['共同負擔用地']),
+            '原有面積合計(㎡)': f"{_x['原有面積合計']:.2f}",
+            '同歸戶原位次配地之街廓': '、'.join(_x['同歸戶原位次配地之街廓']),
+        })
+    _order = [ADJ_DISP_ALLOC, ADJ_DISP_POOL, ADJ_DISP_COMMON_UNIT, ADJ_DISP_COMMON_STEP4, ADJ_DISP_GHOST]
+    _t = [{'類': _k, '切片數': str(intake['totals'].get(_k, [0, 0.0])[0]),
+           '原有面積(㎡)': f"{intake['totals'].get(_k, [0, 0.0])[1]:.2f}"} for _k in _order]
+    _t.append({'類': '合計', '切片數': str(intake['all_count']), '原有面積(㎡)': f"{intake['all_area']:.2f}"})
+    _nb = sum(1 for _x in intake['units'] if _x['軌'] == ADJ_TRACK_BUILD)
+    _np = sum(1 for _x in intake['units'] if _x['軌'] == ADJ_TRACK_PUBLIC)
+    _lines = [f"合併單位 {len(intake['units'])}（{ADJ_TRACK_BUILD} {_nb}·{ADJ_TRACK_PUBLIC} {_np}）；"
+              f"待同歸戶併入之歸戶 {len(intake['step4'])}"]
+    return {'units': _u, 'step4': _s4, 'totals': _t, 'lines': _lines}
+
+
 def wg9248_stringify_mixed_cols(df, cols):
     """把指定欄轉為 `str`，以避 `pyarrow.lib.ArrowInvalid`（混型欄之 Arrow 轉換紅）。
 
@@ -16634,6 +16857,7 @@ def f3_screen_stepg_run(st, *,
     st.session_state.pop('f3_G_values', None)
     st.session_state.pop('f3_G_trace', None)
     st.session_state.pop('f3_k929_6_log', None)   # 🆕 `W-G.9-349`：同二產物之生命週期
+    st.session_state.pop(SS_ADJ_BUILD_FINAL, None)   # 🆕 `W-G.9-351`：同上（調配之輸入·其不配地紀錄由入池閘之畫面入口寫）
     st.session_state['f3_g_needs_rerun'] = True
     _params_for_g = dict(st.session_state.get(_param_key, _new_params))
 
@@ -18057,6 +18281,8 @@ def f3_screen_stepg_run(st, *,
     # 🆕 `W-G.9-349`：入池閘之合併紀錄（旗標 off 或試算趟 ⇒ ⛔ 寫）
     if _k929_6_log is not None:
         st.session_state['f3_k929_6_log'] = _k929_6_log
+        # 🆕 `W-G.9-351`：調配之輸入（入池閘之末態 build·同生命週期）
+        st.session_state[SS_ADJ_BUILD_FINAL] = build_parcels
     # 🚨 Phase 9.12 Issue 4：清除 rerun flag（G 值已重新計算完成）
     st.session_state.pop('f3_g_needs_rerun', None)
     _n_offset = sum(1 for r in g_rows if r.get('推進側別') == '抵費地')
@@ -18170,6 +18396,8 @@ K6B_SCREEN_TRIAL_KEYS = (
     'f3_k94_baseline_touch', 'f3_offset_fragments_merged', 'f3_stage2_placed', 'f3_wd2_pool_diag',
     # 本批所增（1）
     'f3_corner_cand_diag',
+    # 🆕 `W-G.9-351`：入池閘之末態 build 與其末趟之不配地紀錄（配地本體所寫·調配之輸入）
+    'f3_k929_6_build', 'f3_k929_6_dropped',
     # 🆕 `W-G.9-349`：入池閘之合併紀錄（配地本體所寫）
     'f3_k929_6_log',
 )
@@ -18459,6 +18687,7 @@ def _k929_6_screen_gate(st, g_kwargs):
     """🆕 `W-G.9-349`：入池閘之畫面入口（`f3_screen_stepg_run` 之首·旗標 on 且非試算趟時）。
     試算趟 ＝ `f3_screen_stepg_run(代理 st, …, _k929_6_inner=True)`（吃畫面即時之地價·⛔ 借用 harness）；
     隔離 ＝ 試算前存 `K6B_SCREEN_TRIAL_KEYS` 與 `K917_DROPPED`、試算後復。回 `(build_final, log)`。
+    🆕 `W-G.9-351`：復原之後另寫末趟之不配地紀錄於 `SS_ADJ_DROPPED`（調配之輸入·同 `f3_G_values` 之生命週期）。
     試算中止或 `k929_6_fixpoint` 停機 ⇒ `st.error` ＋ `st.stop()`（loud·⛔ 退回未閘之 build）。"""
     import copy as _cp_k9296s
     import contextlib as _cl_k9296s
@@ -18502,6 +18731,7 @@ def _k929_6_screen_gate(st, g_kwargs):
         st.error(_err)
         st.stop()
         raise RuntimeError(_err)
+    _ss[SS_ADJ_DROPPED] = _cp_k9296s.deepcopy(dict(_last[1]))   # 🆕 `W-G.9-351`：調配之輸入（末趟之不配地紀錄）
     return _bf, _log
 
 
@@ -24554,6 +24784,38 @@ def main():
                             else:
                                 st.caption("（本次無合併試算）")
 
+                    # 🆕 `W-G.9-351`：調配階段之輸入（步 1 之尾〜步 2·`K-9-45`／`K-9-46`）——僅盤點·⛔ 調配
+                    _adj351_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)
+                    if _adj351_bf is not None:
+                        with st.expander("🧩 調配階段之輸入：需調配之土地與合併單位（僅盤點·尚未調配）",
+                                         expanded=False):
+                            try:
+                                _adj351_s3 = k6b_stage3_selected(st.session_state, build_parcels,
+                                                                 st.session_state.get('f3L_setback_default'))
+                                _adj351_view = adj_intake_rows(adj_intake(
+                                    temp_parcels if _adj351_s3 is None else _adj351_s3[0], _adj351_bf,
+                                    st.session_state.get('f3_G_values') or [],
+                                    st.session_state.get(SS_ADJ_DROPPED) or {},
+                                    st.session_state.get('t8_ownership_map', {}) or {},
+                                    {b['label']: F3_CATEGORY_BURDEN.get(b.get('category', ''), '')
+                                     for b in classified_blocks}))
+                            except RuntimeError as _e_adj351:
+                                st.error(str(_e_adj351))
+                                _adj351_view = None
+                            if _adj351_view is not None:
+                                for _adj351_line in _adj351_view['lines']:
+                                    st.caption(_adj351_line)
+                                st.markdown("###### 合併單位（`K-9-45`：同歸戶之建築街廓內不能分配之土地，"
+                                            "連同其公設地、道路上之土地；`K-9-46`：軌與原街廓）")
+                                st.dataframe(_pd.DataFrame(_adj351_view['units']),
+                                             use_container_width=True, hide_index=True)
+                                st.markdown("###### 待同歸戶併入（同歸戶已有原位次配地者之公設地、道路上之土地·依道路五則與公設地併入之規定另辦）")
+                                st.dataframe(_pd.DataFrame(_adj351_view['step4']),
+                                             use_container_width=True, hide_index=True)
+                                st.markdown("###### 重劃前土地之盤點（每一筆暫編地號恰歸一類）")
+                                st.dataframe(_pd.DataFrame(_adj351_view['totals']),
+                                             use_container_width=True, hide_index=True)
+
                     # 🆕 W-G Y 波診斷專用（KL 2026-07-14 交辦·非產品功能）：
                     # live g_rows JSON dump 供 sub-cent 定位。
                     # 純加·輸出 st.session_state['f3_G_values'] 原始物件（全精度、未捨入、
````

## 附錄乙　塊 `F10`（新檔 `verify/probes/probe_WG9351_intake.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-351 量測器（發單側窗四十七擬·檔 F10·⛔ 由受單側改一字）：調配階段之輸入（步 1 之尾〜步 2）。

子命令（一律 python verify/probes/probe_WG9351_intake.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `ADJ_*` 常數與 `adj_intake`／`adj_intake_rows`）：
           逐切片之類、合併單位之軌與原街廓（應分配面積較大者·⛔ 原有面積）、入池閘之合併單元、段三所併出者、
           殘料、待同歸戶併入與八種停機；另施四突變（原街廓改以原有面積比、兼有配地者⛔ 成單位、段三所併出者當共同負擔、
           並列⛔ 停機），每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST 查接線：W1 模組層之常數與二函式、二函式內⛔ 案件字面；W2 入池閘之畫面入口於復原之後寫末趟之不配地紀錄、
           配地本體同生命週期去／寫末態 build；W3 二鍵 ∈ `K6B_SCREEN_TRIAL_KEYS` 且其末項仍為 `f3_k929_6_log`；
           W4 消費端 ＝ 生產碼 `34` 檔中除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內；W5 畫面路徑之合成案
           （`自誤 517`：抽出 `main()` 之盤點區塊，以假 st 與合成資料實際執行）。另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0` 二者）：以 `adj_intake` 盤點，並以本器**另寫之分類**（⛔ 呼叫
           `adj_intake`）逐切片對拍（外部錨）：R1 盤點⛔ 停機；R2 逐切片之類相同；R3 合併單位（歸戶·軌·原街廓·成員）
           相同；R4 逐類之切片數與原有面積之和 ＝ 全部切片；R5 入池閘之入池宗（不配地之 build 單元之成員）之數與
           原有面積 ＝ 類「建築街廓內不能分配」者。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ADJ_FUNCS = ["adj_intake", "adj_intake_rows"]
ADJ_KEYS = ["f3_k929_6_build", "f3_k929_6_dropped"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    """自 `app.py` 以 AST 抽出 `ADJ_*`／`SS_ADJ_*` 常數與 `adj_*` 函式，於隔離之命名空間執行。"""
    tree = ast.parse(src)
    parts = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
            parts.append(ast.get_source_segment(src, node))
    if not parts:
        raise KeyError("受詞缺")
    ns = {}
    exec(compile("\n\n".join(parts), "<adj_extract>", "exec"), ns)
    return ns


def _t(pid, lot, blk, a, **kw):
    d = {"暫編地號": pid, "原地號": lot, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0,
         "重劃前地價區段": "z"}
    d.update(kw)
    return d


BUR = {"B1": "可建築土地", "B2": "可建築土地", "C1": "共同負擔", "C2": "共同負擔", "N1": "非共同負擔"}


def _cases(ns):
    """回 [(名, 得, 期)]；任一例拋例外 ⇒ 以 ('例外', 型別名) 記之（⛔ 吞）。"""
    I, RW = ns["adj_intake"], ns["adj_intake_rows"]
    AL, PO, CU, C4, GH = (ns["ADJ_DISP_ALLOC"], ns["ADJ_DISP_POOL"], ns["ADJ_DISP_COMMON_UNIT"],
                          ns["ADJ_DISP_COMMON_STEP4"], ns["ADJ_DISP_GHOST"])
    TB, TP = ns["ADJ_TRACK_BUILD"], ns["ADJ_TRACK_PUBLIC"]
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as e:  # noqa: BLE001
            got = ("例外", type(e).__name__)
        out.append((name, got, exp))

    def rows(*pids):
        return [{"暫編地號": p, "推進側別": "left"} for p in pids] + [{"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]

    own = {"L1": "GA", "L2": "GA", "L3": "GB", "L4": "GC", "L5": "GD", "L6": "GD", "L7": "GE"}
    # 基本案：GA 有 x（配地）、y（不配地·B1）、r（道路）；GB 只有公設地；GC 有配地 z 與道路 s
    temp = [_t("x", "L1", "B1", 100.0), _t("y", "L2", "B1", 50.0), _t("r", "L2", "C1", 30.0),
            _t("p", "L3", "C2", 80.0), _t("z", "L4", "B2", 120.0), _t("s", "L4", "C1", 20.0)]
    build = [dict(t) for t in temp if BUR[t["所屬街廓"]] == "可建築土地"]
    drops = {("B1", "left"): [{"暫編地號": "y", "G(㎡)": 20.0, "不配地由": "內接矩形"}]}
    base = lambda: I(temp, build, rows("x", "z"), drops, own, BUR)  # noqa: E731
    cls = lambda d: {r["暫編地號"]: r["類"] for r in d["slices"]}  # noqa: E731
    run("S1 逐切片之類", lambda: cls(base()), {"x": AL, "y": PO, "r": CU, "p": CU, "z": AL, "s": C4})
    run("S2 合併單位（歸戶·軌·原街廓·成員）",
        lambda: [(u["歸戶"], u["軌"], u["原街廓"], sorted(r["暫編地號"] for r in u["建築街廓內不能分配"] + u["共同負擔用地"]))
                 for u in base()["units"]],
        [("GA", TB, "B1", ["r", "y"]), ("GB", TP, None, ["p"])])
    run("S3 待同歸戶併入（兼有配地者之共同負擔用地）",
        lambda: [(u["歸戶"], [r["暫編地號"] for r in u["共同負擔用地"]], u["同歸戶原位次配地之街廓"]) for u in base()["step4"]],
        [("GC", ["s"], ["B2"])])
    run("S4 盤點之和 ＝ 全部",
        lambda: (round(sum(v[1] for v in base()["totals"].values()), 6), round(base()["all_area"], 6)), (400.0, 400.0))
    # 原街廓：二街廓各有不能分配者 ⇒ 取應分配面積（G）較大者，⛔ 原有面積
    temp2 = [_t("u", "L5", "B1", 100.0), _t("v", "L6", "B2", 40.0)]
    b2 = [dict(t) for t in temp2]
    d2 = {("B1", "left"): [{"暫編地號": "u", "G(㎡)": 10.0}], ("B2", "right"): [{"暫編地號": "v", "G(㎡)": 25.0}]}
    run("S5 原街廓 ＝ 應分配面積較大者（⛔ 原有面積）",
        lambda: I(temp2, b2, [], d2, own, BUR)["units"][0]["原街廓"], "B2")
    d2t = {("B1", "left"): [{"暫編地號": "u", "G(㎡)": 25.0}], ("B2", "right"): [{"暫編地號": "v", "G(㎡)": 25.0}]}
    run("S6 應分配面積並列 ⇒ loud", lambda: I(temp2, b2, [], d2t, own, BUR), ("例外", "RuntimeError"))
    # 入池閘之合併單元：入池（不配地）與留置（配地）
    temp3 = [_t("m1", "L5", "B1", 60.0), _t("m2", "L6", "B1", 30.0), _t("k1", "L7", "B2", 70.0)]
    b3 = [dict(temp3[0], 入池閘併入=["m1", "m2"]), dict(temp3[2])]
    d3 = {("B1", "left"): [{"暫編地號": "m1", "G(㎡)": 40.0}]}
    run("S7 入池之合併單元 ⇒ 成員皆不能分配、其 G 只計一次",
        lambda: (cls(I(temp3, b3, rows("k1"), d3, own, BUR)),
                 I(temp3, b3, rows("k1"), d3, own, BUR)["units"][0]["原街廓之據"]),
        ({"m1": PO, "m2": PO, "k1": AL}, {"B1": 40.0}))
    run("S8 留置之合併單元 ⇒ 成員皆配地", lambda: cls(I(temp3, b3, rows("m1", "k1"), {}, own, BUR)),
        {"m1": AL, "m2": AL, "k1": AL})
    # 段三所併出者
    temp4 = [_t("c", "L1", "B1", 200.0), _t("q", "L1", "C1", 15.0, 段三併出=["c"])]
    run("S9 段三所併出者 ⇒ 配地（配地街廓 ＝ 受併宗之街廓）",
        lambda: [(r["暫編地號"], r["類"], r["配地街廓"]) for r in I(temp4, [dict(temp4[0])], rows("c"), {}, own, BUR)["slices"]],
        [("c", AL, ["B1"]), ("q", AL, ["B1"])])
    run("S10 段三之受併宗未配地 ⇒ loud",
        lambda: I(temp4, [dict(temp4[0])], [], {("B1", "left"): [{"暫編地號": "c", "G(㎡)": 1.0}]}, own, BUR),
        ("例外", "RuntimeError"))
    gh = {"暫編地號": "_GH_(B1)", "原地號": "_GH", "所屬街廓": "B1", "分攤登記面積_m2": 0.0, "_is_ghost_sliver": True}
    run("S11 殘料（可重名·a＝0）⇒ 另類、⛔ 入單位",
        lambda: (I(temp + [gh, dict(gh)], build + [dict(gh)], rows("x", "z"), drops, own, BUR)["totals"][GH],
                 len(I(temp + [gh, dict(gh)], build + [dict(gh)], rows("x", "z"), drops, own, BUR)["units"])),
        ([2, 0.0], 2))
    run("S12 殘料之原有面積 > 0 ⇒ loud", lambda: I(temp + [dict(gh, 分攤登記面積_m2=1.0)], build, rows("x", "z"), drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S13 build 之宗既非配地亦非不配地 ⇒ loud", lambda: I(temp, build, rows("x"), drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S14 G 值列之未知推進側別 ⇒ loud",
        lambda: I(temp, build, rows("x", "z") + [{"暫編地號": "w", "推進側別": "中間"}], drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S15 非共同負擔之街廓上之切片 ⇒ loud（【未裁】）",
        lambda: I(temp + [_t("n", "L3", "N1", 5.0)], build, rows("x", "z"), drops, own, BUR), ("例外", "RuntimeError"))
    run("S16 無歸戶之切片 ⇒ loud", lambda: I(temp + [_t("w2", "LX", "C1", 5.0)], build, rows("x", "z"), drops, own, BUR),
        ("例外", "RuntimeError"))
    run("S17 不配地紀錄之街廓與切片不同 ⇒ loud",
        lambda: I(temp, build, rows("x", "z"), {("B2", "left"): [{"暫編地號": "y", "G(㎡)": 20.0}]}, own, BUR),
        ("例外", "RuntimeError"))
    run("S18 兼有配地與不能分配者 ⇒ 建地軌（其共同負擔用地入單位）",
        lambda: [(u["歸戶"], u["軌"], u["同歸戶原位次配地之街廓"]) for u in base()["units"]][:1], [("GA", TB, ["B1"])])
    run("R1 顯示列各欄皆字串",
        lambda: all(isinstance(v, str) for k in ("units", "step4", "totals") for r in RW(base())[k] for v in r.values()),
        True)
    run("R2 顯示之總句", lambda: RW(base())["lines"], [f"合併單位 2（{TB} 1·{TP} 1）；待同歸戶併入之歸戶 1"])
    return out


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)
    return red


def selftest(repo):
    src = _read(repo, "app.py")
    try:
        ns = _extract_ns(src)
        ns["adj_intake"]
    except Exception:  # noqa: BLE001
        print(f"  🔴 受詞缺：{ADJ_FUNCS}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（AST 抽出之 adj_*）──")
    red = _report(_cases(ns))
    print("── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──")
    base_red = set(red)
    m0 = _report(_cases(_extract_ns(src)), verbose=False)
    print(("  ✅ " if m0 == red else "  🔴 ") + f"M0 未突變之抽出版：紅 {m0}（期 {red}）")
    if m0 != red:
        red.append("M0")
    muts = [
        ("M1 原街廓改以原有面積比", "float(_r['應分配面積'])", "float(_r['原有面積'])"),
        ("M2 兼有配地者⛔ 成單位", "if _pool or (_cm and not _al):", "if (_pool and not _al) or (_cm and not _al):"),
        ("M3 段三所併出者當共同負擔", "if '段三併出' in t:", "if False:"),
        ("M4 並列⛔ 停機", "if len(_cands) != 1:", "if len(_cands) < 1:"),
    ]
    for mname, a, b in muts:
        if src.count(a) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{src.count(a)}）")
            red.append(mname.split()[0])
            continue
        try:
            turned = [n for n in _report(_cases(_extract_ns(src.replace(a, b, 1))), verbose=False) if n not in base_red]
        except Exception as e:  # noqa: BLE001
            turned = [f"抽出拋 {type(e).__name__}"]
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


PROD_OTHERS_RE = re.compile(r"^verify/[^/]+\.py$")


class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.calls.append((name, a, k))
            return _NullCM()
        return rec


class _NullCM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _find_main_block(mn):
    for n in ast.walk(mn):
        for fld in ("body", "orelse", "finalbody"):
            body = getattr(n, fld, None)
            if not isinstance(body, list):
                continue
            for i, s in enumerate(body):
                if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) \
                        and s.targets[0].id == "_adj351_bf" and i + 1 < len(body) and isinstance(body[i + 1], ast.If):
                    return body[i:i + 2]
    return None


def _synth_screen(app_src, mn):
    """`自誤 517`：`main()` 內之敘述⛔ 為 run_all 所執行 ⇒ 抽出盤點區塊（自 `_adj351_bf` 之賦值起連續 `2` 句），
    以假 st ＋ 合成資料實際執行，驗其輸出。"""
    if mn is None:
        return False, "無 main()"
    blk = _find_main_block(mn)
    if blk is None:
        return False, "抽不到盤點區塊"
    try:
        import pandas as pd
        rns = _extract_ns(app_src)
        temp = [_t("x", "L1", "B1", 100.0), _t("y", "L2", "B1", 50.0), _t("r", "L2", "C1", 30.0),
                _t("p", "L3", "C2", 80.0)]
        build = [dict(temp[0]), dict(temp[1])]
        ss = {rns["SS_ADJ_BUILD_FINAL"]: build,
              rns["SS_ADJ_DROPPED"]: {("B1", "left"): [{"暫編地號": "y", "G(㎡)": 20.0}]},
              "f3_G_values": [{"暫編地號": "x", "推進側別": "left"}], "f3L_setback_default": 3.5,
              "t8_ownership_map": {"L1": "GA", "L2": "GA", "L3": "GB"}}
        fst = _FakeSt(ss)
        cats = {"B1": "住宅區", "C1": "道路", "C2": "鄰里公園"}
        g = dict(rns, st=fst, _pd=pd, build_parcels=build, temp_parcels=temp,
                 classified_blocks=[{"label": k, "category": v} for k, v in cats.items()],
                 F3_CATEGORY_BURDEN={"住宅區": "可建築土地", "道路": "共同負擔", "鄰里公園": "共同負擔"},
                 k6b_stage3_selected=lambda ss_, b_, s_: None)
        exec(compile(ast.Module(body=blk, type_ignores=[]), "<main_adj_block>", "exec"), g)
    except Exception as e:  # noqa: BLE001
        return False, f"執行拋 {type(e).__name__}: {e}"
    dfs = [c[1][0] for c in fst.calls if c[0] == "dataframe"]
    errs = [c for c in fst.calls if c[0] == "error"]
    caps = [c[1][0] for c in fst.calls if c[0] == "caption"]
    checks = {
        "無 st.error": not errs,
        "三表": len(dfs) == 3,
        "單位 2 列（GA 建地軌·GB 公設軌）": len(dfs) == 3 and list(dfs[0]["歸戶"]) == ["GA", "GB"],
        "待同歸戶併入 0 列": len(dfs) == 3 and len(dfs[1]) == 0,
        "盤點合計 260.00": len(dfs) == 3 and dfs[2].iloc[-1]["原有面積(㎡)"] == "260.00",
        "總句 1": len(caps) == 1 and caps[0].startswith("合併單位 2"),
    }
    bad = [k for k, v in checks.items() if not v]
    return (not bad), f"不符 {bad}"


def _wiring_checks(app_src, others):
    """回 [(名, 真偽, 註)]。`others` ＝ {路徑: 原始碼}（生產碼 34 檔中 app.py 以外者）。"""
    res = []
    tree = ast.parse(app_src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    ok1 = all(f in top for f in ADJ_FUNCS) and all(k in consts for k in ("SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED"))
    ok1k = ok1 and ast.literal_eval(consts["SS_ADJ_BUILD_FINAL"].value) == ADJ_KEYS[0] \
        and ast.literal_eval(consts["SS_ADJ_DROPPED"].value) == ADJ_KEYS[1]
    lits = sorted({n.value for f in ADJ_FUNCS if f in top for n in ast.walk(top[f])
                   if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value)})
    res.append(("W1 模組層之 ADJ 常數與二函式、二鍵之值、二函式內⛔ 案件字面", ok1k and not lits, f"案件字面 {lits}"))
    gate = top.get("_k929_6_screen_gate")
    ok2a = False
    if gate is not None:
        tries = [i for i, st_ in enumerate(gate.body) if isinstance(st_, ast.Try)]
        for st_ in gate.body[(tries[-1] + 1) if tries else len(gate.body):]:
            seg = ast.get_source_segment(app_src, st_) or ""
            if isinstance(st_, ast.Assign) and "_ss[SS_ADJ_DROPPED]" in seg and "dict(_last[1])" in seg:
                ok2a = True
    f = top.get("f3_screen_stepg_run")
    ok2b = ok2c = False
    if f is not None:
        seg_f = ast.get_source_segment(app_src, f) or ""
        i_gate = seg_f.find("_k929_6_screen_gate(st, dict(")
        i_pop = seg_f.find("st.session_state.pop(SS_ADJ_BUILD_FINAL, None)")
        ok2b = 0 <= i_gate < i_pop and "st.session_state.pop(SS_ADJ_DROPPED" not in seg_f
        for n in ast.walk(f):
            if isinstance(n, ast.If) and isinstance(n.test, ast.Compare) \
                    and getattr(n.test.left, "id", None) == "_k929_6_log":
                seg = ast.get_source_segment(app_src, n) or ""
                ok2c = "st.session_state[SS_ADJ_BUILD_FINAL] = build_parcels" in seg
    res.append(("W2a 入池閘之畫面入口於復原之後寫 SS_ADJ_DROPPED ＝ 末趟之不配地紀錄（_last[1]）", ok2a, ""))
    res.append(("W2b 配地本體於入池閘之後去 SS_ADJ_BUILD_FINAL（⛔ 去 SS_ADJ_DROPPED）", ok2b, ""))
    res.append(("W2c 配地本體於 _k929_6_log 非 None 時寫 SS_ADJ_BUILD_FINAL ＝ build_parcels", ok2c, ""))
    keys = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "K6B_SCREEN_TRIAL_KEYS"
                                             for t in n.targets):
            keys = ast.literal_eval(n.value)
    res.append(("W3 二鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log",
                bool(keys) and all(k in keys for k in ADJ_KEYS) and keys[-1] == "f3_k929_6_log", ""))
    toks = ADJ_FUNCS + ["SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED"] + ADJ_KEYS
    tok_re = re.compile("|".join(re.escape(t) for t in toks))
    other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
    allowed = set(ADJ_FUNCS) | {"main", "f3_screen_stepg_run", "_k929_6_screen_gate"}
    bad = []
    for fname, node in top.items():
        if fname in allowed:
            continue
        seg = ast.get_source_segment(app_src, node) or ""
        if tok_re.search(seg):
            bad.append(fname)
    res.append((f"W4 消費端：生產碼他檔（{len(others)} 檔）命中 0；app.py 只在許可之函式內",
                not other_hits and not bad, f"他檔 {other_hits}；app.py 非許可函式 {bad}"))
    ok5, note5 = _synth_screen(app_src, top.get("main"))
    res.append(("W5 畫面路徑之合成案：main() 之盤點區塊以假 st 實際執行", ok5, note5))
    return res


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
        ("N1 配地本體⛔ 寫 build", app_src.replace(
            "st.session_state[SS_ADJ_BUILD_FINAL] = build_parcels", "pass", 1), others),
        ("N2 入池閘之畫面入口寫空之紀錄", app_src.replace(
            "_ss[SS_ADJ_DROPPED] = _cp_k9296s.deepcopy(dict(_last[1]))",
            "_ss[SS_ADJ_DROPPED] = _cp_k9296s.deepcopy(dict())", 1), others),
        ("N3 注入 harness 消費者", app_src,
         dict(others, **{"verify/stepg_pipeline.py": others.get("verify/stepg_pipeline.py", "")
                         + "\n_adjx = ns['adj_intake']\n"})),
        ("N4 單位表只出首列", app_src.replace(
            "st.dataframe(_pd.DataFrame(_adj351_view['units']),",
            "st.dataframe(_pd.DataFrame(_adj351_view['units'][:1]),", 1), others),
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


def _independent(tp3, bfin, rows, drops, own, bur):
    """外部錨：本器另寫之分類（⛔ 呼叫 adj_intake）。回 ({暫編: 類名}, {歸戶: (軌, 原街廓, 成員)})。"""
    alloc = {str(r["暫編地號"]) for r in rows if r.get("推進側別") in ("left", "right")}
    dg = {str(e["暫編地號"]): (str(b), float(e.get("G(㎡)") or 0)) for (b, s), v in drops.items() for e in v}
    mem = {}
    for u in bfin:
        if u.get("_is_ghost_sliver"):
            continue
        for m in u.get("入池閘併入") or [u["暫編地號"]]:
            mem[str(m)] = str(u["暫編地號"])
    kind, owner = {}, {}
    for t in tp3:
        if t.get("_is_ghost_sliver"):
            continue
        k = str(t["暫編地號"])
        owner[k] = own[str(t["原地號"])]
        if "段三併出" in t:
            kind[k] = "配"
        elif bur[t["所屬街廓"]] == "可建築土地":
            kind[k] = "配" if mem[k] in alloc else "池"
        else:
            kind[k] = "公"
    per = {}
    for k, g in owner.items():
        per.setdefault(g, []).append(k)
    units = {}
    for g, ks in per.items():
        has_p = any(kind[k] == "池" for k in ks)
        has_a = any(kind[k] == "配" for k in ks)
        cm = [k for k in ks if kind[k] == "公"]
        if has_p:
            bl = {}
            for u in {mem[k] for k in ks if kind[k] == "池"}:
                bl[dg[u][0]] = bl.get(dg[u][0], 0.0) + dg[u][1]
            units[g] = ("建", max(bl, key=bl.get), sorted([k for k in ks if kind[k] == "池"] + cm))
            for k in cm:
                kind[k] = "公入"
        elif cm and not has_a:
            units[g] = ("公", None, sorted(cm))
            for k in cm:
                kind[k] = "公入"
        else:
            for k in cm:
                kind[k] = "公4"
    return kind, units


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        from app_harvest import harvest
        with contextlib.redirect_stdout(io.StringIO()):
            ns, fake_st = harvest(os.path.join(repo, "app.py"))
        if "adj_intake" not in ns:
            print("  🔴 受詞缺：adj_intake")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        MAP = {ns["ADJ_DISP_ALLOC"]: "配", ns["ADJ_DISP_POOL"]: "池", ns["ADJ_DISP_COMMON_UNIT"]: "公入",
               ns["ADJ_DISP_COMMON_STEP4"]: "公4"}
        TR = {ns["ADJ_TRACK_BUILD"]: "建", ns["ADJ_TRACK_PUBLIC"]: "公"}
        for sb in sbs:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
                    ns["K917_DROPPED"].clear()
                    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                    eff_min_build_by_blk={})
            except RuntimeError as e:
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            k9 = sg.get("k929_6")
            if k9 is None:
                print(f"🔴 退縮 {sb}：run_step_g 無 k929_6（入池閘未啟用？）⇒ 無從判定")
                return 3
            drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
            print(f"══ 退縮 {sb} ══")
            try:
                it = ns["adj_intake"](tp3, k9["build"], sg["g_rows"], drops, own, bur)
            except RuntimeError as e:
                print(f"  🔴 R1 盤點停機：{str(e)[:300]}")
                red.append(f"R1@{sb}")
                continue
            print("  ✅ R1 盤點⛔ 停機")
            view = ns["adj_intake_rows"](it)
            for ln in view["lines"]:
                print("  " + ln)
            for r in view["totals"]:
                print(f"     {r['類']}：{r['切片數']} 片·{r['原有面積(㎡)']} ㎡")
            for r in view["units"]:
                print(f"     單位 {r['歸戶']}｜{r['軌']}｜原街廓 {r['原街廓']}｜據 {r['原街廓之據（應分配面積㎡）']}｜"
                      f"建 {r['建築街廓內不能分配之土地']}｜公 {r['公設地／道路上之土地']}｜合 {r['原有面積合計(㎡)']}｜"
                      f"配 {r['同歸戶原位次配地之街廓']}")
            for r in view["step4"]:
                print(f"     待併 {r['歸戶']}｜{r['公設地／道路上之土地']}｜合 {r['原有面積合計(㎡)']}｜"
                      f"配 {r['同歸戶原位次配地之街廓']}")
            kind, units = _independent(tp3, k9["build"], sg["g_rows"], drops, own, bur)
            got_k = {r["暫編地號"]: MAP[r["類"]] for r in it["slices"]}
            dif = sorted(k for k in set(kind) | set(got_k) if kind.get(k) != got_k.get(k))
            print(("  ✅" if not dif else "  🔴") + f" R2 逐切片之類（{len(got_k)} 片）與外部錨相同：相異 {dif[:10]}")
            if dif:
                red.append(f"R2@{sb}")
            got_u = {u["歸戶"]: (TR[u["軌"]], u["原街廓"],
                                 sorted(r["暫編地號"] for r in u["建築街廓內不能分配"] + u["共同負擔用地"]))
                     for u in it["units"]}
            difu = sorted(g for g in set(units) | set(got_u) if units.get(g) != got_u.get(g))
            print(("  ✅" if not difu else "  🔴") + f" R3 合併單位（{len(got_u)}）與外部錨相同：相異 {difu}")
            if difu:
                red.append(f"R3@{sb}")
            s_all = sum(float(t.get("分攤登記面積_m2", 0) or 0) for t in tp3)
            s_cls = sum(v[1] for v in it["totals"].values())
            n_cls = sum(v[0] for v in it["totals"].values())
            ok4 = abs(s_all - s_cls) <= 1e-6 and n_cls == len(tp3)
            print(("  ✅" if ok4 else "  🔴") + f" R4 逐類之和 ＝ 全部：{n_cls}／{len(tp3)} 片；{s_cls:.4f}／{s_all:.4f} ㎡")
            if not ok4:
                red.append(f"R4@{sb}")
            bfid = {str(u["暫編地號"]): u for u in k9["build"] if not u.get("_is_ghost_sliver")}
            dmem = [m for (b, s), v in drops.items() for e in v for m in (bfid[str(e["暫編地號"])].get("入池閘併入")
                                                                           or [str(e["暫編地號"])])]
            by3 = {str(t["暫編地號"]): t for t in tp3 if not t.get("_is_ghost_sliver")}
            n5, a5 = len(dmem), sum(float(by3[m].get("分攤登記面積_m2", 0) or 0) for m in dmem)
            c5 = it["totals"].get(ns["ADJ_DISP_POOL"], [0, 0.0])
            ok5 = n5 == c5[0] and abs(a5 - c5[1]) <= 1e-6
            print(("  ✅" if ok5 else "  🔴") + f" R5 入池宗（不配地單元之成員）{n5} 宗·{a5:.2f} ㎡ ＝ "
                  f"類「{ns['ADJ_DISP_POOL']}」{c5[0]} 片·{c5[1]:.2f} ㎡")
            if not ok5:
                red.append(f"R5@{sb}")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("selftest", "wiring", "run"):
        print(__doc__)
        return 2
    repo = os.path.abspath(argv[2])
    if argv[1] == "selftest":
        return selftest(repo)
    if argv[1] == "wiring":
        return wiring(repo)
    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
    return run(repo, sbs)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄丙　塊 `P5`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：新調配模組之首環（調配之輸入盤點）＋ 新調配模組之單序（`W-G.9-351`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `2517c5133fe4b87d4508b513571dfb8391bdef8c`（本批開工態）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 調配之輸入（規格步 `1` 之尾〜步 `2`·`K-9-45`（一）·`K-9-46`（一）（三）） | `adj_intake`：原位次（含段三、入池閘）之末態之每一重劃前切片恰歸一類（原位次配地／建築街廓內不能分配／共同負擔用地·入合併單位／共同負擔用地·待同歸戶併入／無地號之殘料）；同歸戶者組合併單位（軌；原街廓 ＝ 其建築街廓內不能分配之土地所在之街廓，分處二以上者取應分配面積較大者）；畫面成果區之「🧩 調配階段之輸入」一覽（`adj_intake_rows`）；⛔ 消費端 | ✅ | `docs/orders/W-G.9-351_重量單.md` |
| `2` | 末端塊之評選與 `R_end`（`K-9-36` ①〜③·`N0-20`） | 原位次之尾：跨占 `R_end` 者依原投影序試算，第一個 `G ≥ area(R_end)` 者當選；均未達者 `R_end` 為強制抵費地（本案 `R6` 左端 `85.71 ㎡` 之片即其內部組成·`GB-178` 之進度（四）） | ⬜（有土地後果） | 次單 |
| `3` | 規格步 `3` 候選街廓名單（五級八鍵·`r3` 之消費） | 同單定之：harness 之區外道路名稱之來源（`W-G.9-350` 塊 `P4` 序 `3`）；畫面所填之正面道路名稱只存於該次畫面之工作階段（重啟須再填）；候選之類別（公園、廣場等非道路之公共設施街廓沿正面線過半者是否得為正面道路·`r3_front_road_derive` 現不分類別） | ⬜ | 規格步 `3` |
| `4` | 規格步 `4` 同歸戶合併（第一趟）：道路五則、公設地併入 | 受詞含序 `1` 之「共同負擔用地·待同歸戶併入」 | ⬜ | 規格步 `4` |
| `5` | 規格步 `5` 末端塊與中間調配池之進入與落位（`K-9-38`〜`40`） | 前置：`K-9-38` 射程 ④、`K-9-40` 射程 ④ 之附圖另呈 | ⬜ | 規格步 `5` |
| `6` | 規格步 `6` ½ 之判與出口（增配／現金補償·裁定 H、I、L、M） | — | ⬜ | 規格步 `6` |
| `7` | 規格步 `7`／`8` 終態與出艙 | — | ⬜ | 規格步 `7`／`8` |

🔒 **本批之讀法**（發單側之工程裁·⛔ 域裁·已以【通知】呈 KL）：① 原街廓之比較所用之「應分配面積」＝ 原位次該趟之 `G`（不配地之宗 ＝ 其不配地紀錄之 `G`；入池之合併單元以單元計一次）；② 同歸戶已有原位次配地、而無建築街廓內不能分配之土地者，其公設地、道路上之土地⛔ 先成合併單位，候規格步 `4`（道路五則、公設地併入）；全無建築街廓內土地者 ＝ 公設軌；③ 段三所併出之片 ＝ 原位次配地（其配地街廓 ＝ 受併宗之街廓）；④ 無地號之殘料（`_is_ghost_sliver`·原有面積 `0`）⛔ 入任何單位。
🔒 **本案之量**（態 `2517c51` ＋ 本批·harness·量測器 `F10`）：退縮 `3.5 m` ⇒ 合併單位 `23`（建地軌 `15`·公設軌 `8`）、待同歸戶併入之歸戶 `9`；建築街廓內不能分配 `22` 片·`2363.40 ㎡`（＝ 本檔「待落地清單之更新：閘二…（`W-G.9-349`）」節所載入池 `22` 宗·`2363.40 ㎡`）。退縮 `0 m` ⇒ `24`（`16`·`8`）、`9`；`23` 片·`2513.70 ㎡`（＝ 同節之 `23` 宗·`2513.70 ㎡`）。全部切片 `126`（殘料 `8`）·原有面積 `34860.73 ㎡`（二退縮同）。**配地⛔ 變**（量測器 `F8` 之 `run` 二退縮之出艙改前改後逐位同）。
🔒 **`K-9-46` 所載本案之例之現值**（其例係態 `338bd08`·退縮 `0 m`·⛔ 追改該典一字）：歸戶 `G025` 之原街廓現為 `R5`（`628-53(2)` 之應分配面積 `0.99` ＞ `628-53(1)` 之 `0.26`；例載 `R6`〔其時 `0.00`／`0.26`〕，二退縮同）；歸戶 `G030` 之原街廓現為退縮 `0 m` ⇒ `R2`（`27.45` ＞ `24.22`）、退縮 `3.5 m` ⇒ `R3`（`28.34` ＞ `27.55`）（例載 `R3`〔其時 `20.52`／`26.54`〕）。
🔒 **依賴序**：序 `1`（本批）→ 序 `2`（有土地後果·KL 逐 commit 放行）→ 序 `3` → 序 `4` → 序 `5`（其前置之附圖另呈）→ 序 `6` → 序 `7`；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級）。
🔒 **本機介面**：主 checkout 同步後，按「🧮 執行 G 值迭代計算」，其成果區於「K-9-29 六」合併紀錄之下多「🧩 調配階段之輸入」一覽（預設收合）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `10`（子字串框·含圖例與本列）·列 ＝ `8`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: b88332ba78264e09f6003f28c5e09a14f14840f59bf737fe96508e893d439ba8
