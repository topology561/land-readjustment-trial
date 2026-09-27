# `W-G.9-352`　重量單：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49 ①③`）＋ `K-9-49` 之登錄 ＋ `GB-178` 之進度（五）＋ 待落地清單之更新

> **發單** ＝ 發單側窗四十八·`2026-09-27`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**；工項五於 **KL 之主 checkout**）。
> **級** ＝ **重**（生產碼 `2` 檔：`app.py`、`verify/stepg_pipeline.py`；**🔴 土地後果**——`R6` 左端之末端塊，見 `§一` 項 `6`〜`10`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `ed6871af9ce2bf352ff8c5a7916ddccfca1ebc0a`。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D1`／`F11`／`K1`／`G4`／`P6` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）。
> 🔑 **來源檔一**（檔名逐字 `W-G.9-352_重量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項五之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F11`）與改動（`D1`、`K1`、`G4`、`P6`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：塊 `D1` 以外之生產碼一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿／自誤簿之一字（本批⛔ 鑄自誤、⛔ 鑄 `VR`、⛔ 鑄 `GB`；只鑄 `K-9-49`）；`K-6` 典與 `GB` 簿除塊 `K1`／`G4` 之純末端追加外之一字；任何側支之刪除或改寫。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `ed6871af9ce2bf352ff8c5a7916ddccfca1ebc0a`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 545 545` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`905`** 檔）。發單側窗四十八實跑（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-352`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py ed6871a W-G.9-352 W-G.9-351 W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-351` | `2`／`4`／`3` | `2`／`4`／`3` | `7` | `2` | `2`／`41` | 🟢 框非恆空 |
| `K-9-49`（本批所鑄之裁號）｜`python verify/probes/wg9268_gate6_occupancy.py ed6871a K-9-49 K-9-48 K-9-94` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`2` | 🟢 可取（鬆框 `2` 列 ＝ `docs/orders/W-G.9-332_輕量單.md:28`、`docs/reports/W-G.9-332R_CC交接文.md:88` 之「對照乙［必為零］」所列之未取號·⛔ 占用） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `10`／`10` | 🟢 |

**本批只鑄 `K-9-49`**（自誤／`GB`／`VR` 皆⛔）；收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `ed6871a`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`F11`／`K1`／`G4`／`P6` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二前置之任一期不符（尤：`F11` 三子命令之施前 `rc ≠ 1`） |
| `5` | 塊 `D1` 之 `git apply --check` 不過；或施後之二 blob ≠ `§五-1` 項 `7` |
| `6` | 工項二之驗 `V-1`〜`V-5` 任一 ≠ 期（尤：`V-2` 之 `F8 run` 出艙之異列 ≠ `§一` 項 `9` 所列；`V-5` 之 `run_all` 相異項 ≠ `§一` 項 `10` 所列） |
| `7` | 工項二之 `push` 無 `§二` 之放行；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項三之三檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項五：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒 |
| `11` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `12` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗四十八自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `ed6871af9ce2bf352ff8c5a7916ddccfca1ebc0a`；側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`30`** |
| `2` | 生產碼（開工態 blob） | `app.py` `cdbbbe08116c00c24f143050c590a3c61b485ac3`（`1535668` B）；`verify/stepg_pipeline.py` `21b9cb341a17b17f05c4ce487c26b40ccdc32747`（`118225` B） |
| `3` | `W-G.9-351` 之復驗 | 發單側窗四十八依交接文四十七 `§四-1` 逐項自倉重跑：逐 `commit` 對拍（單 ＝ `02552c68…`·`SELF_SHA256` 自驗相符；`D1`／`F10`／`P5` 逐位同；`D1` 施於 `f40b028` 得 `cdbbbe08…` ＝ `101c645` 之 `app.py`）、`CLAUDE.md` `272943 → 277812`（嚴格前綴·所增 ＝ `P5`）、收工閘 `1`〜`14`、`F8 run` 二退縮改前改後 `cmp` 逐位同、`run_all` 二態（`f40b028` 對 `101c645`·同一倉外路徑·各 `237412` B·`cmp` 逐位同·`64` 項·PASS `28`／FAIL `36`·對帳 `22／36`）——**全數相符**；CC 回報之二差異（`run_all` 於 Windows `239419` B·根之 `W-G.9-350_重量單.md` 已不在）皆核實、無影響。KL 主 checkout（經 KL 核准之唯讀存取）：`HEAD` → `wip/s1-endpart` ＝ `ed6871a…`、`app.py` ＝ `cdbbbe08…`、`CLAUDE.md` ＝ 倉內；其操作紀錄載 `2026-09-27 13:51` 自 `2517c51` 快轉至 `ed6871a`；根有 `W-G.9-351_重量單.md`（＝ 入倉之單·候 KL 自刪） |
| `4` | 本批之受詞 | `K-9-36 ①②`（末端塊之評選與未當選者之位次）、`K-9-49 ①③`（本批所鑄·各筆單獨試算；街角優先與先後）；補丁十 §一（觸發條件、`R_end` 之構造）；`K-9-31 ③`（末端塊之裡側界線 ＝ 街廓界）；`K-9-33` 射程 ④（末端塊之 `S` 由構造保證）；依賴序 ＝ `CLAUDE.md`「🔧 待落地清單之更新：新調配模組之首環…（`W-G.9-351`）」節序 `2` |
| `5` | 現碼之行為（開工態） | 配地路徑⛔ 構 `R_end`、⛔ 施評選（`_end_region_R` 於 `app.py` 內⛔ 呼叫）；無側街之端之鏈自 FRONT 端點起，未臨正街單獨成一片抵費地（本案 `R6-抵費地-2` `85.71 ㎡`·`GB-178` 之進度（四）） |
| `6` | 本案之評選（塊 `D1` 施後·harness·退縮 `3.5 m`／`0 m` 同） | `R6` 左端（無側街）：未臨正街 `85.71` ＋ 末端帶 `166.57` ＝ `R_end` `252.28 ㎡`；跨占者依原投影序各筆單獨試算：`628(2)`（`G009`）`7.65` 未達、`628-1(2)`（`G009`）`148.99` 未達、`628-23(1)`（`G017`）`73.76` 未達、`628-4(1)`（`G008`）`695.38` **當選**；`R2` 右、`R3` 左、`R5` 右之未臨正街 ＝ `0.0001`／`0.0001`／`0.0000 ㎡` ⇒ 不觸發；`R1`、`R4` 二端皆有側街 |
| `7` | 施後 blob | `app.py` `c99a3701608bb8aa2d218f3ae04e38757124fc24`（`1556424` B·增 `329`／刪 `10`）；`verify/stepg_pipeline.py` `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373`（`121159` B·增 `40`／刪 `6`） |
| `8` | 本案之土地後果（配地列·施前 → 施後·二退縮同·唯 `R6`） | 見下表 |
| `9` | `F8 run`（`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5`／`… 0.0`·工項一之端 對 工項二之 `commit`） | 皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；二份之異列恰各 `2`（`diff` 之 `<`／`>` 各 `2` 列·其餘逐位同）：`R6/left 628-1(2) G 153.19 由 內接矩形、臨正街寬` → `… G 153.11 …`；逐街廓之 `R6 5·2071.22` → `R6 5·2074.46`（他街廓之數同） |
| `10` | `run_all`（同一倉外路徑·工項一之端 對 工項二之 `commit`） | 二份皆 `64` 項·PASS `28 → 28`／FAIL `36 → 36`；`python verify/probes/probe_WG9343_step0_flag.py runall` ⇒ `rc 0`，**相異項恰 `9`**（皆 FAIL → FAIL）：`#15` v3·滑池槽0m（違規數 `62 → 63`）、`#16` v3·J表0m（`107 → 107`·本體異）、`#25` v3·滑池槽3.5m（`76 → 77`）、`#26` v3·J表3.5m（`144 → 144`·本體異）、`#39` W-D.3 碎片幾何/三分類（v3）（`92 → 80`）、`#40` W-D.3 碎片逐邊CAD（v3）（`52 → 50`）、`#42` W-D.4 碎片遞補0m（`3 → 2`）、`#45` W-D.4 碎片遞補3.5m（`3 → 2`）、`#55` W-D.4 遞補錨 R6 85.66→628-4(1)（跳過 628(2);628-1(2);628-23(1)）（`0 → 0`·本體異）；其餘 `55` 項之名目、狀態、違規數與本體逐項同；末端夾具／golden 列 `21／21`·相異 `0`；對帳段「名目：凍存 `22`／現況 `36`」不變；二份之 bytes `237412 → 236032`（`diff` 之異列 `<`／`>` 合 `100`·皆 `R6` 之池帶診斷列與上開九項之本體）——發單側 Linux 實測（態 `ed6871a` 對 `ed6871a` ＋ 塊 `D1`·同一倉外路徑） |
| `11` | 畫面對 harness（`verify/probes/probe_WG9345_screen.py parity <R> <退縮> on`） | 施後：`3.5` ⇒ `rc 0`（配地列 harness `35`／畫面 `34`·不符格 `0`）；`0.0` ⇒ `rc 0`（`36`／`35`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]` |

**`§一` 項 `8` 之表**（harness·`R6`·`G`／`S` ＝ 配地列之 `G(㎡)`／`S(m)`〔臨正街寬·`G` 公式之 `S`〕）：

| 宗 | 地主 | 施前 | 施後 |
|---|---|---|---|
| `628-4(1)` | `G008` | 左鏈第 `2` 宗·`G 691.92`·`S 14.82`·宗地寬度 `14.77` | **末端塊**（左鏈第 `1` 宗·宗地含 `R_end` 全部）·`G 695.38`·`S 12.92`·宗地寬度 `12.88` |
| `628-21(1)`（入池閘合併單元：`628-21(1)`、`628-22(1)`、`628-23(1)`） | `G017` | 左鏈第 `1` 宗·`G 433.99`·`S 9.18`·宗地寬度 `9.15` | 左鏈第 `2` 宗·`G 433.77`·`S 9.30`·宗地寬度 `9.27` |
| `628-1(2)`（入池閘之入池單元：`628(2)`、`628-1(2)`） | `G009` | 不配地（不配地紀錄 `G 153.19`·由 內接矩形、臨正街寬） | 不配地（`G 153.11`·同由） |
| 抵費地 | — | `R6-抵費地-1` `1819.35`、`R6-抵費地-2` `85.71`（未臨正街） | `R6-抵費地` `1901.82`（一片） |
| `628-18(1)`、`628-7(1)`、`628-20(1)`（右鏈） | — | — | `G`／`S` 不變；二分法之收斂步數隨右鏈之剩餘長度變 ⇒ 宗地之形差 `0.002`／`0.003`／`0.006 ㎡`（`迭代次數` 等欄隨之） |

`R6` 之 `ΣG` `2071.22 → 2074.46`；他街廓之配地列逐欄同（harness 二退縮·`cut_coords` 逐點同）。

---

## `§二`　KL 之語與射程

🔒 **KL 之語（`2026-09-27`·發單側窗四十八·逐字）**：
- `15:41`：「是」——所答者為發單側窗四十八前一則覆命之末段【要你判斷】逐字「同意本窗即讀末端塊之正典，量測本案現況並擬次單？土地後果將依格式附圖另呈，程式逐筆經您放行後才推入主線。（是／否）」
- 發單側呈【要你判斷】（附平面圖·`R6` 左端之兩讀法）逐字：「末端塊的評選，跨占 R_end 的土地以「各筆單獨試算」（讀法甲，R6 左端由 G008 當選）？（是／否；否即採讀法乙，由 G017 當選）」
- `16:11`：「若讀法甲，各筆單獨試算後，跨占R_end者均無合格者，是將R_end做為抵費地?」
- `16:20`：「採各筆單獨試算都沒有達標時，比照街角地，把跨占者與同地主相鄰的土地（同街廓內，再及道路、公設地）合併後，依原投影序再試一次，仍未達才以 R_end 為強制抵費地。／但是延伸一個問題你想想看，跨占R_end者進入同地主相鄰的土地（同街廓內，再及道路、公設地）合併機制，會不會有與他街廓（或同街廓）的街角（sideline側）地主有競合關係，若有與有sideline的街角地順序上競合的關係話，要以sideline的街角地為優先，因為sideline側才有雙面臨路，位置地段較好／目前程式邏輯上，若採比照街角地，把跨占者與同地主相鄰的土地（同街廓內，再及道路、公設地）合併機制，會產生問題?」
- `16:34`：「是」——所答者為發單側所呈【要你判斷】逐字「末端塊的評選（含合併再試）一律在全案街角地（含合併再試及其後的道路、公設地分配）都定案後才辦理；已上鎖、已併入或已分配給街角的土地不再併入末端塊；同時跨占兩者的土地歸街角側？（是／否）」
🔒 **所據之既裁**：`K-9-36`（KL `2026-09-17`）、`K-9-31`、`K-9-33`、`K-9-48`；補丁十 §一（`docs/specs/W-G.4_規格v3補丁十_N0-20末端塊fallback定案.md`）。本批鑄 `K-9-49`（塊 `K1`·全文逐字）。
🔒 **本單之讀法**（發單側之工程裁·⛔ 域裁·以【通知】呈 KL）：
① 各筆單獨試算之受詞 ＝ 入池閘合併**前**之宗——評選於配地之首趟為之（`SS_END_BLOCK_EVAL`），入池閘之試算趟與本體沿用首趟之當選者；當選者嗣後為入池閘合併單元之成員者，移該單元（`end_block_pin`）。
② 試算之 `G` 與配地同一解算路徑（`_solve_G_one`·`solve_G_binary` 之 `s_back`）：宗地 ＝ 未臨正街 ∪ 正街段之帶；`G` 公式之 `S` ＝ 正街段之寬（未臨正街⛔ 計臨街·`K-9-33`「`S` ＝ 臨 FRONTLINE 之寬」）。
③ 跨占之門檻 ＝ `1.0 ㎡`（比照街角選位之跨占門檻）；未臨正街之 ε ＝ `1e-3 ㎡`（補丁十 §一）；「無側街」須街角選位表之 `{側}_has_side` 與 CAD 之 SIDELINE 二源一致，不一致 ⇒ 停機。
④ 「同時跨占二者歸街角側」：跨占本街廓任一街角規定範圍（＞ `1.0 ㎡`）者⛔ 為末端塊之候選（含強制抵費地之街角）。
⑤ 右端之末端塊對稱實作（鏈起於 FRONT `p2`、首宗向外延伸未臨正街）——本案無右端觸發，其正確性由 `F11 selftest` 之鏡像例與 `F11 wiring` 保之。
⑥ 各筆單獨皆未達 ⇒ **停機**（`K-9-49 ②` 合併再試與 `K-9-36 ③` 強制抵費地候次單·⛔ 靜默）——本案不觸發。
⑦ 定案趟之檢：觸發之端之鏈首宗須為當選者，否則停機；選槽（`_select_pool_slot`）以 `pin` 使末端塊恆屬該側之鏈（同街角第 `1` 宗）。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項二之生產碼 `commit` 推入主線之放行，CC 將其逐字載入報告；**無之 ⇒ 工項二之驗畢後停於推送前，於對話請示 KL**。所答之【要你判斷】逐字：「同意將『末端塊之評選與落位（R6 左端由 G008〔628-4〕當選末端塊，其宗地含未臨路之 85.71 ㎡；G017 改居其次；中間配餘地增 82.47 ㎡）』之程式推入主線嗎？（是／否）」

🔒 **逐筆放行清單**：本批動生產碼者恰 **`1`** 筆（工項二）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `app.py`（新 module 級常數 `END_BLOCK_UNFRONT_EPS`／`END_BLOCK_CROSS_MIN_AREA`／`SS_END_BLOCK_EVAL` 與函式 `end_block_side_geom`／`end_block_pick`／`end_block_pin`／`end_block_apply`／`end_block_host`／`end_block_eval_rows`／`end_block_assert_head`；`solve_G_binary`／`_solve_G_one` 之 `s_back`；`_select_pool_slot` 之 `pin`；`f3_screen_stepg_run` 之接線；`_k929_6_screen_gate` 於復原之後帶出評選；`K6B_SCREEN_TRIAL_KEYS` 增一鍵（置於其末項 `f3_k929_6_log` 之前）；`_WF_NS_NAMES` 增三名；`main()` 成果區之「🧱 末端塊之評選」一覽）、`verify/stepg_pipeline.py`（harness 之同構接線） | 塊 `D1` | 🔴 有（`§一` 項 `6`／`8`／`9`／`10`） |

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至主線；`(b)` 工項二之 `push` 以本節之放行為條件；`(c)` 工項五於 KL 本機之主 checkout·⛔ `commit`；`(d)` ⛔ 及其他任何生產碼、任何他錨；`(e)` ⛔ 建 `K-9-49 ②`（合併再試）、`K-9-36 ③`（強制抵費地）、調配之任何後步——另單。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-352_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-352 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F11` 入倉（主線·零生產碼）

塊 `F11` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9352_endblock.py`（**新檔**）。`commit` 訊息逐字 `W-G.9-352 工項一：量測器 F11（末端塊之評選與落位）入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項二　塊 `D1`：末端塊之評選與落位（🔴 生產碼·一 `commit`·🔴 土地後果）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9352_endblock.py selftest <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
2. `python verify/probes/probe_WG9352_endblock.py wiring <repo>` ⇒ **`rc 1`**（`W1`〜`W10` 皆紅；突變 `N1`〜`N4` 皆「突變錨不存在」）。
3. `python verify/probes/probe_WG9352_endblock.py run <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D1` 依圍欄之逐列索引抽出為 `<O>\D1.diff`、對拍 `§五-1` 後，`git apply --check <O>\D1.diff` ⇒ 過；`git apply <O>\D1.diff`；`git hash-object app.py` ＝ `c99a3701608bb8aa2d218f3ae04e38757124fc24`、`git hash-object verify/stepg_pipeline.py` ＝ `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-352 工項二：末端塊之評選與落位（K-9-36 ①②·K-9-49 ①③）🔴 生產碼（🔴 土地後果）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9352_endblock.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `S1`〜`S18`（含 `S10b`／`S11b`／`S15b`）皆 ✅、`M0` ✅、`M1`〜`M7` 皆「轉紅」；`wiring` 之 `W1`〜`W10` 皆 ✅，`N1`〜`N4` 皆「轉紅」 |
| `V-2` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `diff` | 皆 **`rc 0`**、末列 `⇒ 紅 []；rc 0`；**異列恰 ＝ `§一` 項 `9`**（每份 `<`／`>` 各 `2` 列：`R6/left 628-1(2) G 153.19 → 153.11`；逐街廓之 `R6 5·2071.22 → 5·2074.46`）；他列逐位同 |
| `V-3` | `python verify/probes/probe_WG9352_endblock.py run <repo>` | **`rc 0`**；二退縮之 `R1`〜`R5` 皆 ✅；`R6` 左之候選與試算 ＝ `§一` 項 `6` |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35.json`；同 `0.0`；`python verify/probes/probe_WG9348_harvest_key.py <repo>`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>`；`python verify/probes/probe_WG9340_main_synth.py <repo>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9350_frontroad.py selftest <repo>`；`… wiring <repo>`；`… run <repo>`；`python verify/probes/probe_WG9351_intake.py selftest <repo>`；`… wiring <repo>`；`… run <repo>` | 皆 **`rc 0`**；`parity` ＝ `§一` 項 `11`；`wfns_ast` `46`／`46`／`45`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F10 run` 之總句與逐類之數同 `W-G.9-351 §一` 項 `5`，唯 `G009` 單位之「據」由 `R6 153.19` 為 `R6 153.11`（二退縮） |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項恰 ＝ `§一` 項 `10` 所列之 `9` 項**（名目、狀態 FAIL → FAIL、違規數逐項同所列）；其餘 `55` 項逐項同；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（`§二` 之放行成立後·與驗為分開之呼叫）：`git push origin HEAD:wip/s1-endpart`。

### 工項三　`K-9-49` 之登錄 ＋ `GB-178` 之進度（五）＋ 待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `K1`、`G4`、`P6` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位各**附於**下列三檔之末：`K1` → `docs/rulings/K-6_街角地分配程序與可分配判準.md`；`G4` → `docs/reports/W-G.4_泛用阻塞項登記表.md`；`P6` → `CLAUDE.md`。三檔之刪除欄皆 `0`、改前全檔皆為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-352 工項三：K-9-49 之登錄 ＋ GB-178 之進度（五）＋ 待落地清單之更新 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項四　執行報告入倉（主線·新檔 `docs/reports/W-G.9-352R_末端塊之評選與落位_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F11` 三子命令之全文、`F8 run` 二份之 `diff` 全文、`parity` 二份之 `rc` 與末三列、`runall` 對拍之全文與 `diff` 之結果）；④ 五塊之實得（bytes／`sha256`）與三檔之改前改後 bytes；⑤ `§二` 之放行（KL 之逐字或請示之經過）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-352 工項四：執行報告入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項五　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542` 之攔法·分開之呼叫）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、逐檔出艙其路徑、二 blob 與處置；`A ∩ U` 為空者出艙「空」。
   🔒 KL 主 checkout 之現態（發單側窗四十八經 KL 核准之唯讀存取·`§一` 項 `3`）＝ `ed6871a`；其根有 `W-G.9-351_重量單.md`（未追蹤·與入倉 blob 逐位同）——其路徑⛔ 在本次之 `A`，⛔ 動之；本單之複本若置於主 checkout 之 `docs/orders/`，即落於 `A ∩ U`——依丙處置之，⛔ 預設其態。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項四 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `c99a3701608bb8aa2d218f3ae04e38757124fc24`；`git -C <主 checkout> hash-object verify/stepg_pipeline.py` ＝ `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373`。
任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項四之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項二 ＝ `app.py` 增 `329`／刪 `10`、`verify/stepg_pipeline.py` 增 `40`／刪 `6`；其餘逐檔 **`0`** |
| `2` | 生產碼 `34` 檔對 `ed6871a` | 相異恰 **`2`**（`app.py` ＝ `c99a3701608bb8aa2d218f3ae04e38757124fc24`、`verify/stepg_pipeline.py` ＝ `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`8` 檔：本單、`F11`、`app.py`、`verify/stepg_pipeline.py`、`K-6`、`GB` 簿、`CLAUDE.md`、報告） |
| `4` | 三檔之 bytes | `K-6` `404828 → 410740`、`GB` 簿 `1019048 → 1020320`、`CLAUDE.md` `277812 → 282537`；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`30`**；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 545 545 .` | **`rc 0`**（自誤 `MAX` 仍 `545`） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 545 545` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `530`／`MAX` `545`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `186`／`193`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` **`46`／`49`**／`[44, 47]` |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`46`／`46`／`45`** |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9351_intake.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `15` | `python verify/probes/probe_WG9352_endblock.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之替身 ＋ 塊 `F11` ＋ 塊 `D1` ＋ 塊 `K1`／`G4`／`P6` ＋ 報告之替身·五 `commit`）並實跑閘 `1`〜`4`、`6`〜`15` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D1` | `42982` B·`sha256` `d6737f0e8736a06fb2fd24a04fe734f0990781ac71e254bebe9a29652e2f20b8`·`655` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F11` | `34994` B·`sha256` `a132d67ea8199310f74f35a7856a45289778b73ec986e2121d664ad6416fcd6d`·`614` 列（圍欄內全文·末附換行） |
| `4` | 塊 `K1` | `5912` B·`sha256` `bebe87c87a950d12126f512351ede2b2dcf09e288bd0f48acab353f10efcad08`·`49` 列；附於 `K-6`（`404828` B）之末後，期末 ＝ `410740` B |
| `5` | 塊 `G4` | `1272` B·`sha256` `c032f291e836264e8755ec6ecde03d18b24ac82d1ece73891dbfb5b4670e646b`·`13` 列；附於 `GB` 簿（`1019048` B）之末後，期末 ＝ `1020320` B |
| `6` | 塊 `P6` | `4725` B·`sha256` `0a276fcf806118fb8a20fef5b44e93e89a0ff94a91ded432d8527782b90dd75f`·`22` 列；附於 `CLAUDE.md`（`277812` B）之末後，期末 ＝ `282537` B |
| `7` | 施 `D1` 後之 blob | `app.py` `c99a3701608bb8aa2d218f3ae04e38757124fc24`（`1556424` B）；`verify/stepg_pipeline.py` `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373`（`121159` B）（開工態 `cdbbbe08…`／`21b9cb34…`） |
| `8` | `F11` 之二態 | 開工態（工項一之端）`selftest`／`wiring`／`run` 皆 `rc 1`；施 `D1` 後皆 `rc 0` |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十八實跑（態 `ed6871a`）：🔴 機械 `0` 項／🟡 提示 `10` 項——`P-1` `:130`（工項二前置之段·所觸之字樣係工項二前置 `2` 所引 `F11 wiring` 施前出艙之「突變錨不存在」及「⛔ `commit`」之用語，⛔ 全稱否定 ⇒ **具名豁免**）、`P-1` `:206`（本表·項 `9`／`10` 二格所引之預檢用語與收工閘模擬之述 ⇒ **具名豁免**）、`P-1` `:1132`／`:1257`（塊 `F11` 之碼·所觸之字樣係該器自身之出艙文字 ⇒ **具名豁免**）、`P-4` `:143`／`:180`（工項二之驗、`§四` 收工閘之表頭·其箭頭之座標系皆為「改前〔工項一之端／`ed6871a`〕至改後〔工項二之 `commit`／工項四之端〕」，表內自載 ⇒ **具名豁免**）、`P-4` `:157`（工項三之段·其 `→` 係「塊 → 所附之檔」之對應、⛔ 方向性轉引 ⇒ **具名豁免**）、`P-4` `:252`（塊 `D1` 之碼·所觸者係生產碼之註解 ⇒ **具名豁免**）、`P-4` `:1600` 與 `P-6` `:1600`（塊 `P6` 之「本批之讀法」列·其箭頭與數之出處 ＝ 本單 `§一` 項 `8` 之表 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `18739`–`26385`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`ed6871a` ＋ 五 `commit`：本單之前稿〔僅本表項 `9`／`10` 二格未填〕＋ 塊 `F11` ＋ 塊 `D1`〔自前稿依抽取式抽出·`git apply` 過·施後二 blob ＝ 項 `7`〕＋ 塊 `K1`／`G4`／`P6` ＋ 報告之替身）：閘 `1` 工項二 `app.py` 增 `329`／刪 `10`、`verify/stepg_pipeline.py` 增 `40`／刪 `6`，餘逐檔刪 `0`；閘 `2` 相異恰 `2`（`34` 檔）；閘 `3` `CR` 合計 `0`（`8` 檔·判別力 `12308`）；閘 `4` `404828 → 410740`、`1019048 → 1020320`、`277812 → 282537`（皆嚴格前綴）；閘 `6`〜`15` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `46`／`46`／`45`；「app 側宿主 ＝ f3_screen_stepg_run」；`F8` 二子命令、`F9`／`F10`／`F11` 各三子命令之末列 `⇒ 紅 []；rc 0`）；跑畢追蹤檔之變動 `0`；另於工項一之端實跑 `F11` 三子命令皆 `rc 1`（`selftest`／`run` 末列 `⇒ 紅 ['受詞缺']；rc 1`；`wiring` `W1`〜`W10`、`N1`〜`N4` 皆紅） |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零、一、三、四 ⇒ 逕行 `push` 主線；工項二 ⇒ 依 `§二` 之放行、驗皆符後推主線；工項五 ⇒ KL 本機之主 checkout。
3. 收工後，主 checkout 之根之來源檔（本單，及工項五所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D1`（`git apply` 之差異·`app.py` ＋ `verify/stepg_pipeline.py`）

````diff
diff --git a/app.py b/app.py
index cdbbbe0..c99a370 100644
--- a/app.py
+++ b/app.py
@@ -7936,8 +7936,9 @@ def _select_pool_slot(widths, left_side, right_side, rw_func=None, widths_R=None
     b_R = float(_Rt.get('b', 0.0) or 0.0)
     note = ''
     # STEP 1：候選槽 K（有左街角 → 左群至少含 p_1；有右街角 → 右群至少含 p_n）
-    k_min = 1 if has_L else 0
-    k_max = (n - 1) if has_R else n
+    # 🆕 `W-G.9-352`：末端塊（`pin`）同街角第 1 宗⛔ 被池頂掉（該端之第 1 位恆屬該側之鏈）
+    k_min = 1 if (has_L or bool(_L.get('pin'))) else 0
+    k_max = (n - 1) if (has_R or bool(_Rt.get('pin'))) else n
     if k_min > k_max:
         # 退化（如 n=1 且雙側 pin 衝突）：無合法槽 → 全域比較、具名註記（不靜默）
         K = list(range(0, n + 1))
@@ -10483,6 +10484,244 @@ def _end_region_R(block_poly, cad_alloc, end_pt, min_width, frag_poly, _label=''
     return band, r_end, float(r_end.area)
 
 
+# ══════════════════════════════════════════════════════════════════════════
+#  🆕 `W-G.9-352`：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49`〔KL 裁 `2026-09-27`〕·補丁十 §一）
+#
+#  觸發（該端·二條件皆真）：① 該端無側街（街角選位表之 `{側}_has_side` 與 CAD 之 SIDELINE 二源須一致·
+#    不一致 ⇒ 停機）；② 該端之未臨正街土地（左 ＝ block∩{s<0}、右 ＝ block∩{s>s(p2)}·s 相對 FRONT p1）
+#    ＞ `END_BLOCK_UNFRONT_EPS`。
+#  R_end ＝ 未臨正街 ∪ 末端帶（`_end_region_R`·帶寬 ＝ 畸零地寬）。
+#  候選 ＝ 本街廓原位次序列之宗，其重劃前多邊形 ∩ R_end ＞ `END_BLOCK_CROSS_MIN_AREA`；
+#    跨占本街廓任一街角規定範圍（＞ 同門檻）者⛔ 為候選（`K-9-49 ③`：同時跨占二者之土地歸街角側）。
+#  評選（`K-9-36 ①`·`K-9-49 ①`）：依原投影序自該端起，**各筆單獨**於末端位試算 G——其宗地 ＝ 未臨正街 ∪
+#    正街段之帶、G 公式之 S ＝ 正街段之寬（未臨正街不計臨街）；第一個 G ≥ area(R_end) 者當選（往後找）。
+#  落位（`K-9-36 ②`）：當選者移至該端之第 1 位，其餘保持原相對序；配地時其宗地同上（`solve_G_binary` 之 `s_back`）。
+#  皆未達 ⇒ 🔴 停機：合併再試（`K-9-49 ②`）與強制抵費地（`K-9-36 ③`）候次單（⛔ 靜默）。
+#  先後（`K-9-49 ③`）：本評選於配地之首趟為之——街角（含段三及其後處理）皆已定案；入池閘之試算趟與末趟
+#    沿用首趟之當選者（`SS_END_BLOCK_EVAL`），故「各筆單獨」之受詞 ＝ 入池閘合併前之宗。
+# ══════════════════════════════════════════════════════════════════════════
+END_BLOCK_UNFRONT_EPS = 1e-3        # ㎡·補丁十 §一 之 ε
+END_BLOCK_CROSS_MIN_AREA = 1.0      # ㎡·跨占之門檻（比照街角選位之跨占門檻）
+SS_END_BLOCK_EVAL = 'f3_end_block_eval'
+
+
+def end_block_side_geom(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
+                        min_width, side, _label=''):
+    """一端之末端塊幾何（純函式）。回 dict：`gate`、`unfront`（未臨正街面積）；`gate` 真另有
+    `s_back`（未臨正街沿 s 之寬）、`r_end`（多邊形）、`r_end_area`、`band_area`。"""
+    import numpy as np
+    if side not in ('left', 'right'):
+        raise RuntimeError(f"🔴 end_block_side_geom[{_label}]：side={side!r}（只接受 left／right）")
+    if block_poly is None or d_hat is None or corner_pt is None or front_p2 is None:
+        raise RuntimeError(f"🔴 end_block_side_geom[{_label}·{side}]：缺街廓／FRONT 之幾何（no-silent-fallback）")
+    _dom = _strip_s_range(block_poly, d_hat, corner_pt, allocation_dir)
+    if _dom is None:
+        raise RuntimeError(f"🔴 end_block_side_geom[{_label}·{side}]：街廓之 s 域不可定義")
+    _smin, _smax = float(_dom[0]), float(_dom[1])
+    _p1 = np.asarray(corner_pt, dtype=float)[:2]
+    _v = np.asarray(front_p2, dtype=float)[:2] - _p1
+    _d = np.asarray(d_hat, dtype=float)[:2]
+    _sp2 = float(np.dot(_v, _d))                      # s(p2)：恆等 s(p1 + s0·d̂) ≡ s0
+    if not (_sp2 > 0.0) or abs(float(_v[0] * _d[1] - _v[1] * _d[0])) > 1e-6:
+        raise RuntimeError(f"🔴 end_block_side_geom[{_label}·{side}]：FRONT p2 不在 p1 沿 d̂ 之射線上")
+    if side == 'left':
+        _w = (-_smin) if _smin < -1e-6 else 0.0
+        _start = _p1 + _smin * _d
+        _end_pt = _p1
+    else:
+        _w = (_smax - _sp2) if _smax > _sp2 + 1e-6 else 0.0
+        _start = _p1 + _sp2 * _d
+        _end_pt = _p1 + _sp2 * _d
+    if _w <= 0.0:
+        return {'gate': False, 'unfront': 0.0}
+    _unf_poly, _unf = _block_strip(block_poly, d_hat, _start, _w, allocation_dir=allocation_dir)
+    _unf = float(_unf or 0.0)
+    if _unf <= END_BLOCK_UNFRONT_EPS:
+        return {'gate': False, 'unfront': _unf}
+    _band, _r_end, _a = _end_region_R(block_poly, cad_alloc, _end_pt, min_width, _unf_poly,
+                                      _label=f"{_label}·{side}")
+    return {'gate': True, 'unfront': _unf, 's_back': float(_w), 'r_end': _r_end,
+            'r_end_area': float(_a), 'band_area': float(_band.area)}
+
+
+def end_block_pick(side, geom, entries, corner_range_polys, trial, _label=''):
+    """評選（純函式·`trial(tp) -> (G, 臨正街寬)` 由呼叫端供）。`entries` ＝ 自該端起之原位次序列之宗。
+    回 `{'winner': 暫編地號, 'rows': [...]}`；皆未達 ⇒ 🔴 停機。"""
+    from shapely.geometry import Polygon as _P_eb
+    _r_end = geom['r_end']
+    _thr = float(geom['r_end_area'])
+    _crs = [p for p in (corner_range_polys or {}).values() if p is not None]
+    rows = []
+    for _e in entries:
+        _tp = _e['tp']
+        _k = str(_tp.get('暫編地號', ''))
+        _cs = _tp.get('polygon_coords') or []
+        if len(_cs) < 3:
+            continue
+        _pg = _P_eb(_cs)
+        if not _pg.is_valid:
+            _pg = _pg.buffer(0)
+        _ov = float(_pg.intersection(_r_end).area)
+        if _ov <= END_BLOCK_CROSS_MIN_AREA:
+            continue
+        _row = {'暫編地號': _k, '原地號': str(_tp.get('原地號', '')), '跨占R_end(㎡)': round(_ov, 2)}
+        if any(float(_pg.intersection(_c).area) > END_BLOCK_CROSS_MIN_AREA for _c in _crs):
+            _row.update({'試算G(㎡)': None, '臨正街寬(m)': None, '結果': '跨占街角規定範圍·歸街角側'})
+            rows.append(_row)
+            continue
+        _g, _s = trial(_tp)
+        _ok = float(_g) >= _thr
+        _row.update({'試算G(㎡)': round(float(_g), 2), '臨正街寬(m)': round(float(_s), 2),
+                     '結果': '當選' if _ok else '未達'})
+        rows.append(_row)
+        if _ok:
+            return {'winner': _k, 'rows': rows}
+    raise RuntimeError(
+        f"🔴 [末端塊·{_label}·{side}] 跨占 R_end（{_thr:.2f} ㎡）者各筆單獨試算皆未達：{rows}"
+        "——合併再試（K-9-49 ②）與強制抵費地（K-9-36 ③）候次單（⛔ 靜默）")
+
+
+def end_block_pin(ordered, side, pid, _label=''):
+    """落位（`K-9-36 ②`）：當選者移至該端之第 1 位（左 ＝ 首、右 ＝ 末），其餘保持原相對序；回新序列。
+    `pid` 不在序列而為某入池閘合併單元之成員者 ⇒ 移該單元；找不到或不唯一 ⇒ 停機。"""
+    _idx = [i for i, e in enumerate(ordered) if str(e['tp'].get('暫編地號', '')) == pid]
+    if not _idx:
+        _idx = [i for i, e in enumerate(ordered) if pid in (e['tp'].get('入池閘併入') or [])]
+    if len(_idx) != 1:
+        raise RuntimeError(f"🔴 end_block_pin[{_label}·{side}]：當選者 {pid} 於序列中 {len(_idx)} 筆（期恰 1）")
+    _out = list(ordered)
+    _e = _out.pop(_idx[0])
+    if _e.get('is_corner_winner'):
+        raise RuntimeError(f"🔴 end_block_pin[{_label}·{side}]：當選者 {pid} 為街角第 1 宗")
+    _e['is_end_block'] = True
+    if side == 'left':
+        _out.insert(0, _e)
+    else:
+        _out.append(_e)
+    return _out
+
+
+def end_block_apply(ordered, *, blk_label, block_poly, d_hat, corner_pt, front_p2, cad_alloc,
+                    allocation_dir, min_width, has_side_pk, has_side_cad, corner_range_polys,
+                    trial, cache):
+    """一街廓之末端塊：評選（首趟）或沿用（`cache` 已有本街廓）＋ 落位。
+    `trial(tp, side, s_back) -> (G, 臨正街寬)`；`cache` ＝ `SS_END_BLOCK_EVAL` 之 dict（就地寫）。
+    回 `(ordered′, {'left': {'s_back','winner'}|None, 'right': …})`。"""
+    _info = {'left': None, 'right': None}
+    _cached = cache.get(blk_label)
+    _rec = {}
+    _out = list(ordered)
+    for _sd in ('left', 'right'):
+        _pk = bool((has_side_pk or {}).get(_sd))
+        _cad = bool((has_side_cad or {}).get(_sd))
+        if _pk != _cad:
+            raise RuntimeError(
+                f"🔴 end_block_apply[{blk_label}·{_sd}]：有無側街之二源不一致（街角選位表 {_pk}／CAD {_cad}）")
+        if _pk:
+            continue
+        _g = end_block_side_geom(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
+                                 min_width, _sd, _label=blk_label)
+        if not _g['gate']:
+            _rec[_sd] = {'觸發': False, '未臨正街(㎡)': round(float(_g['unfront']), 4)}
+            continue
+        if _cached is not None:
+            _c = _cached.get(_sd) or {}
+            if not _c.get('觸發'):
+                raise RuntimeError(f"🔴 end_block_apply[{blk_label}·{_sd}]：首趟未觸發而本趟觸發")
+            _win = _c['當選']
+            _rec[_sd] = _c
+        else:
+            _seq = _out if _sd == 'left' else list(reversed(_out))
+            _pk_res = end_block_pick(_sd, _g, _seq, corner_range_polys,
+                                     (lambda tp, _s=_sd, _w=_g['s_back']: trial(tp, _s, _w)),
+                                     _label=blk_label)
+            _win = _pk_res['winner']
+            _rec[_sd] = {'觸發': True, '未臨正街(㎡)': round(float(_g['unfront']), 2),
+                         '末端帶(㎡)': round(float(_g['band_area']), 2),
+                         'R_end(㎡)': round(float(_g['r_end_area']), 2),
+                         '候選': _pk_res['rows'], '當選': _win}
+        _out = end_block_pin(_out, _sd, _win, _label=blk_label)
+        _info[_sd] = {'s_back': float(_g['s_back']), 'winner': _win}
+    if _cached is None:
+        cache[blk_label] = _rec
+    return _out, _info
+
+
+def end_block_host(ordered, *, blk_label, blk_poly, d_hat, corner_pt, front_p2, alloc_dir_cad,
+                   allocation_dir, session, corner_range_polys, solve_one, l_front, avg_depth,
+                   S_block_max, post_price, pre_price_by_zone):
+    """`W-G.9-352`：二宿主（畫面 `f3_screen_stepg_run`／harness `_run_step_g_impl`）之共同入口（單一真相源·#20）。
+    讀 session 之畸零地寬、街角選位表之有無側街、CAD 之 SIDELINE；試算之 G 經宿主之 `_solve_one`
+    （與配地同一解算路徑）。回 `end_block_apply` 之回傳。"""
+    import numpy as np
+    _mw = float((session.get('f3_min_width_by_label', {}) or {}).get(blk_label, 0.0) or 0.0)
+    _fo = (session.get('f3L_forced_offset', {}) or {}).get(blk_label, {}) or {}
+    _sl = (session.get('f3_cad_side_lines_by_side', {}) or {}).get(blk_label, {}) or {}
+    _has_cad = {_sd: ((_sl.get(_sd) or {}).get('mid') is not None) for _sd in ('left', 'right')}
+    _has_pk = ({_sd: bool(_fo.get(f'{_sd}_has_side')) for _sd in ('left', 'right')}
+               if ('left_has_side' in _fo and 'right_has_side' in _fo) else dict(_has_cad))
+    _cache = session.setdefault(SS_END_BLOCK_EVAL, {})
+    _d = np.asarray(d_hat, dtype=float)
+    _cp = np.asarray(corner_pt, dtype=float)
+
+    def _trial(tp, side, s_back):
+        if '分攤登記面積_m2' in tp:
+            _a = round(float(tp.get('分攤登記面積_m2', 0) or 0) + float(tp.get('面積_m2', 0) or 0), 2)
+        else:
+            _a = round(float(tp.get('面積_m2', 0) or 0), 2)
+        _pre = float(pre_price_by_zone.get(tp.get('重劃前地價區段', ''), 0.0) or 0.0)
+        _post = float(post_price or 0.0)
+        _A = (_post / _pre) if (_pre > 0 and _post > 0) else 1.0
+        if side == 'left':
+            _dd, _bp = _d, _cp
+        else:
+            _dd, _bp = -_d, _cp + float(S_block_max) * _d
+        _res, _ = solve_one(_a, _A, l_front, 0.0, 0.0, blk_poly, _dd, _bp, max(0.1, float(S_block_max)),
+                            False, '無', avg_depth,
+                            _allocation_dir=allocation_dir, _side_mid=None, _W_prev=0.0,
+                            _w0_start=0.0, _near_dir=None, _is_chain_head=True, _s_back=s_back)
+        return float(_res.get('G', 0.0)), float(_res.get('S_raw', _res.get('S', 0.0)))
+
+    return end_block_apply(ordered, blk_label=blk_label, block_poly=blk_poly, d_hat=d_hat,
+                           corner_pt=corner_pt, front_p2=front_p2, cad_alloc=alloc_dir_cad,
+                           allocation_dir=allocation_dir, min_width=_mw, has_side_pk=_has_pk,
+                           has_side_cad=_has_cad, corner_range_polys=corner_range_polys,
+                           trial=_trial, cache=_cache)
+
+
+def end_block_eval_rows(ev):
+    """`W-G.9-352`：末端塊評選之顯示（純函式·表列之值皆字串）。回 `{'lines': [...], 'rows': [...]}`。"""
+    _nm = {'left': '左', 'right': '右'}
+    lines, rows = [], []
+    for _blk in sorted(ev or {}):
+        for _sd in ('left', 'right'):
+            _r = (ev.get(_blk) or {}).get(_sd)
+            if _r is None:
+                continue
+            if not _r.get('觸發'):
+                lines.append(f"{_blk} {_nm[_sd]}端（無側街）：未臨正街 {_r.get('未臨正街(㎡)')} ㎡ ⇒ 未觸發")
+                continue
+            lines.append(f"{_blk} {_nm[_sd]}端（無側街）：未臨正街 {_r['未臨正街(㎡)']} ＋ 末端帶 {_r['末端帶(㎡)']}"
+                         f" ＝ R_end {_r['R_end(㎡)']} ㎡；當選 {_r['當選']}")
+            for _c in (_r.get('候選') or []):
+                rows.append({'街廓': _blk, '端': _nm[_sd],
+                             **{_k: ('—' if _v is None else str(_v)) for _k, _v in _c.items()}})
+    return {'lines': lines, 'rows': rows}
+
+
+def end_block_assert_head(blk_label, eb_info, left_results, right_results):
+    """`W-G.9-352`：定案趟之檢——觸發之端，其鏈之首宗須為末端塊之當選者（含入池閘合併單元）；否則停機。"""
+    for _sd, _res in (('left', left_results), ('right', right_results)):
+        _i = (eb_info or {}).get(_sd)
+        if _i is None:
+            continue
+        if not _res or not _res[0][0].get('is_end_block'):
+            _hd = (_res[0][0]['tp'].get('暫編地號') if _res else None)
+            raise RuntimeError(
+                f"🔴 [末端塊·{blk_label}·{_sd}] 定案趟之鏈首宗 {_hd!r} 非當選者 {_i['winner']!r}"
+                "（未臨正街將無人承受·⛔ 靜默成池）")
+
+
 def solve_G_binary(a: float, A: float, B: float, C: float,
                    l_front: float, l_side: float, F: float,
                    block_poly, d_hat, baseline_pt,
@@ -10494,7 +10733,8 @@ def solve_G_binary(a: float, A: float, B: float, C: float,
                    allocation_dir=None,
                    side_mid=None, W_prev: float = 0.0,
                    w0_start=None,
-                   near_dir=None) -> dict:
+                   near_dir=None,
+                   s_back: float = 0.0) -> dict:
     """
     幾何驅動的二分法解 S：
       每輪猜 S_guess → 從 baseline_pt 沿 d_hat 切出 block strip 多邊形 → 計算 area_geom；
@@ -10568,11 +10808,25 @@ def solve_G_binary(a: float, A: float, B: float, C: float,
         _near_ad = _nd
         _far_nhat = np.array([-_ad_f[1], _ad_f[0]])   # ＝ `_block_strip` 內之 rot90(allocation_dir)
 
+    # 🆕 `W-G.9-352`（末端塊·`K-9-36 ②`）：`s_back` ＞ 0 ⇒ 本宗之帶向後延伸 `s_back`（未臨正街），
+    #   宗地 ＝ 未臨正街 ∪ [baseline, baseline + S]；G 公式之 S 仍為正街段之寬（未臨正街不計臨街）。
+    #   `s_back == 0` ⇒ 原式一字未動（逐位不變）。
+    _s_back = float(s_back or 0.0)
+    if _s_back < 0.0:
+        raise RuntimeError(f"🔴 solve_G_binary：s_back={s_back!r} < 0")
+    if _s_back > 0.0 and (_near_ad is not None or side_mid is not None):
+        raise RuntimeError(
+            "🔴 solve_G_binary：s_back ＞ 0（末端塊）而 near_dir／side_mid 有值——末端塊⛔ 臨側街、⛔ 承前一宗之界")
+
     def _cut_strip(_S):
         """本函式**唯一**之切帶入口（⛔ 兩處呼叫共用·避免同式分岔·#20）。
 
         `_near_ad is None` ⇒ **原式一字未動**（逐位不變）；否則走 `_block_strip` 雙線分支。
         """
+        if _near_ad is None and _s_back > 0.0:
+            return _block_strip(block_poly, d_hat,
+                                np.asarray(baseline_pt, dtype=float) - _s_back * np.asarray(d_hat, dtype=float),
+                                _S + _s_back, allocation_dir=allocation_dir)
         if _near_ad is None:
             return _block_strip(block_poly, d_hat, baseline_pt, _S,
                                 allocation_dir=allocation_dir)
@@ -15168,7 +15422,8 @@ def _solve_G_one(*, a_m2, A, l_front, l_side, F, blk_poly, d_hat, baseline_pt,
                  S_max, is_corner, side, avg_depth, B, C, tab6_burden,
                  allocation_dir=None, side_mid=None, W_prev=0.0, near_dir=None,
                  w0_start=None,
-                 is_chain_head=False):
+                 is_chain_head=False,
+                 s_back=0.0):
     """🆕 P-0b（裁定M·Q-M4）：G 解算**單一真相源**——幾何二分法優先，失敗 fallback 至代數迭代。
 
     app 內嵌 `_solve_one`（`main()` 內）與 `verify/stepg_pipeline.py` 之 `_solve_one` 皆改**薄殼**
@@ -15212,12 +15467,17 @@ def _solve_G_one(*, a_m2, A, l_front, l_side, F, blk_poly, d_hat, baseline_pt,
                 side_mid=side_mid, W_prev=W_prev,
                 near_dir=near_dir,                       # 🆕 D-2b-23【甲】：界面單線（⛔ 不在此推導）
                 w0_start=w0_start,                       # 🆕 W-G.9-318：K-9-41 ① 起算點（薄殼直通·⛔ 在此推導）
+                s_back=s_back,                           # 🆕 W-G.9-352：末端塊之未臨正街（薄殼直通·⛔ 在此推導）
             )
             _r['_alloc_dir_used'] = _alloc_dir_used      # D-2b-3 §二-3（純加性）
             return _r, '幾何二分法'
         except Exception:
             pass
     # fallback：代數迭代（同樣攜帶 W_prev 累積差額，§4）
+    if float(s_back or 0.0) > 0.0:
+        raise RuntimeError(
+            "🔴 W-G.9-352：solve_G_binary 失敗而落入 iterate_G_S，該路徑未實作末端塊之未臨正街"
+            "（s_back）⇒ ⛔ 靜默改以矩形估算")
     if w0_start is not None and (is_corner or is_chain_head):
         raise RuntimeError(
             "🔴 K-9-41 ①：solve_G_binary 失敗而落入 iterate_G_S，"
@@ -15686,6 +15946,8 @@ _WF_NS_NAMES = [
     "k917_should_drop", "k917_note_drop",
     # 🆕 `W-G.9-349`：`K-9-29 六` 入池閘之三名（引擎 `verify/stepg_pipeline.py` 之 `run_step_g` 經 `ns` 消費）。
     "k929_6_enabled", "k929_6_fixpoint", "K917_DROPPED",
+    # 🆕 `W-G.9-352`：末端塊之三名（引擎 `verify/stepg_pipeline.py` 經 `ns` 消費）。
+    "end_block_host", "end_block_assert_head", "SS_END_BLOCK_EVAL",
     # 🆕 B-5（plan v3 §四·D-3 寬度制）：平移切帶範圍多邊形**即算即用**之單一真相源。
     #   ⚠️ 走 ns 函式、**不**存 session 新鍵——session 資料走 `_WFSessionShim`，
     #      且 harness（run_verification）從不算負擔範圍，存鍵在 harness 路徑必缺。
@@ -16821,6 +17083,10 @@ def f3_screen_stepg_run(st, *,
     # 🆕 `W-G.9-349`（`K-9-29 六` 入池閘·KL 放行 `2026-09-26`）：旗標 on 且非試算趟 ⇒ 先以試算趟（代理 st）求末態之
     #   build，再以之跑本體（真 st）；合併紀錄於本體末與 `f3_G_values` 同寫（`f3_k929_6_log`）。旗標 off ⇒ 本段⛔ 執行。
     _k929_6_log = None
+    # 🆕 `W-G.9-352`：末端塊之評選於本趟之首趟為之（入池閘之試算趟與本體沿用·`SS_END_BLOCK_EVAL`）
+    #   ⇒ 非試算趟先清前次之評選（⛔ 列入 `K6B_SCREEN_TRIAL_KEYS`：入池閘之復原⛔ 得清之）。
+    if not _k929_6_inner:
+        st.session_state.pop(SS_END_BLOCK_EVAL, None)
     if (not _k929_6_inner) and k929_6_enabled():
         build_parcels, _k929_6_log = _k929_6_screen_gate(st, dict(
             B_value=B_value, C_for_calc=C_for_calc, _auto_recalc=_auto_recalc, _btn_clicked=_btn_clicked,
@@ -16978,7 +17244,7 @@ def f3_screen_stepg_run(st, *,
                    _baseline_pt, _S_max, _is_corner, _side, _avg_depth,
                    _allocation_dir=None, _side_mid=None, _W_prev=0.0,
                    _w0_start=None,
-                   _near_dir=None, _is_chain_head=False):
+                   _near_dir=None, _is_chain_head=False, _s_back=0.0):
         """求解單筆宗地 — 薄殼委派 module 級 `_solve_G_one`（P-0b·單一真相源·Q-M4）。
 
                         🆕 W-C §0.5-B/§4：_allocation_dir = rot90(f3_cad_alloc_dir)（臨街向）；
@@ -16993,7 +17259,8 @@ def f3_screen_stepg_run(st, *,
             allocation_dir=_allocation_dir, side_mid=_side_mid, W_prev=_W_prev,
             near_dir=_near_dir,   # 🆕 D-2b-23【甲】：界面單線（薄殼直通·不推導）
             w0_start=_w0_start,   # 🆕 W-G.9-318：K-9-41 ①（薄殼直通·⛔ 在此推導）
-            is_chain_head=_is_chain_head)   # 🆕 W-G.9-261：鏈頭旗標（薄殼直通·不推導）
+            is_chain_head=_is_chain_head,   # 🆕 W-G.9-261：鏈頭旗標（薄殼直通·不推導）
+            s_back=_s_back)   # 🆕 W-G.9-352：末端塊之未臨正街（薄殼直通·⛔ 在此推導）
 
     st.session_state['f3_wd2_pool_diag'] = {}   # 🆕 W-D.2 §3：每輪重建（防殘留舊塊）
     for blk_label, parcels_in_blk in parcels_by_block.items():
@@ -17202,6 +17469,24 @@ def f3_screen_stepg_run(st, *,
             )
             ordered_v2 = list(_v2_res.get('ordered', []) or [])
 
+        # 🆕 `W-G.9-352`：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49`）——原位次序列定後、`_ov2_idx` 前
+        #   （單一真相源 `end_block_host`·harness 同構）。
+        _eb_info = {'left': None, 'right': None}
+        if (not _degenerate_order) and _front_p2_blk is not None:
+            from shapely.geometry import Polygon as _SP_eb
+            _eb_crp_raw = (st.session_state.get('f3_corner_range_polys', {}) or {}).get(blk_label) or {}
+            _eb_crp = {_w_eb: (_SP_eb(_eb_crp_raw[_w_eb])
+                               if (_eb_crp_raw.get(_w_eb) and len(_eb_crp_raw[_w_eb]) >= 3) else None)
+                       for _w_eb in ('left', 'right')}
+            ordered_v2, _eb_info = end_block_host(
+                ordered_v2, blk_label=blk_label, blk_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt,
+                front_p2=_front_p2_blk, alloc_dir_cad=_alloc_dir_cad,
+                allocation_dir=allocation_dir_block, session=st.session_state,
+                corner_range_polys=_eb_crp, solve_one=_solve_one, l_front=l_front,
+                avg_depth=avg_depth_default, S_block_max=S_block_max,
+                post_price=post_price_by_block.get(blk_label, 0.0),
+                pre_price_by_zone=pre_price_by_zone)
+
         # 🆕 W-D.2 §3：註記原位次 index（基準趟寬度→_select_pool_slot 映射用）。
         #   k 切分與 side 標籤依 k 而變 → 移入 _advance_block_with_split（趟內建）。
         for _i_ov2, _e_ov2 in enumerate(ordered_v2):
@@ -17508,6 +17793,9 @@ def f3_screen_stepg_run(st, *,
                     _near_dir=_near_dir_left,   # 🆕 D-2b-23【甲】
                     _is_chain_head=(_lg_idx_left == 0),   # 🆕 W-G.9-261：本側鏈頭
                     _w0_start=(0.0 if not _fo_left else None),   # 🆕 K-9-41 ①前段（W-G.9-318 補令一）
+                    _s_back=(float(_eb_info['left']['s_back'])   # 🆕 W-G.9-352：末端塊（左）
+                             if (_eb_info['left'] is not None and _lg_idx_left == 0
+                                 and entry.get('is_end_block')) else 0.0),
                 )
                 # 🆕 `W-G.9-246′` 工項二 **站 1／4（app 左鏈）**：`res` 定案後、鏈推進前。
                 #   🛑 只做二事：呼叫、寫欄（`I-5`）——⛔ 依其 verdict 寫任何 `if`。
@@ -17579,6 +17867,8 @@ def f3_screen_stepg_run(st, *,
                                          has_side_right=_has_right_corner,
                                          forced_right=_fo_right)
                 actual_max_proj = _smax_g if _smax_g is not None else S_block_max
+                if _eb_info['right'] is not None:   # 🆕 W-G.9-352：末端塊（右）⇒ 鏈起於 FRONT p2、首宗向外延伸未臨正街
+                    actual_max_proj = S_block_max
                 end_pt = corner_pt + actual_max_proj * d_hat
                 d_hat_rev = -d_hat
             else:
@@ -17632,6 +17922,9 @@ def f3_screen_stepg_run(st, *,
                     _near_dir=_near_dir_right,   # 🆕 D-2b-23【甲】
                     _is_chain_head=(_lg_idx_right == 0),   # 🆕 W-G.9-261：本側鏈頭
                     _w0_start=(0.0 if not _fo_right else None),  # 🆕 K-9-41 ①前段（W-G.9-318 補令一）
+                    _s_back=(float(_eb_info['right']['s_back'])   # 🆕 W-G.9-352：末端塊（右）
+                             if (_eb_info['right'] is not None and _lg_idx_right == 0
+                                 and entry.get('is_end_block')) else 0.0),
                 )
                 # 極端防呆 2 後援：右側起點數值微修
                 if (float(res.get('area_geom', 0)) < 0.5
@@ -17649,6 +17942,9 @@ def f3_screen_stepg_run(st, *,
                             _near_dir=_near_dir_right,   # 🆕 D-2b-23【甲】
                             _is_chain_head=(_lg_idx_right == 0),   # 🆕 W-G.9-261：本側鏈頭
                             _w0_start=(0.0 if not _fo_right else None),  # 🆕 K-9-41 ①前段（W-G.9-318 補令一）
+                            _s_back=(float(_eb_info['right']['s_back'])   # 🆕 W-G.9-352：末端塊（右）
+                                     if (_eb_info['right'] is not None and _lg_idx_right == 0
+                                         and entry.get('is_end_block')) else 0.0),
                         )
                         if float(_r2.get('area_geom', 0)) >= 0.5:
                             res, solver_label = _r2, _sl2
@@ -17708,6 +18004,10 @@ def f3_screen_stepg_run(st, *,
                 _trace_local[k] = res.get('trace', [])
                 right_results.append((entry, res))
 
+            # 🆕 `W-G.9-352`：定案趟之末端塊須為該側鏈之首宗（⛔ 靜默讓未臨正街成池）
+            if _commit:
+                end_block_assert_head(blk_label, _eb_info, left_results, right_results)
+
             return {
                 'rows': _rows_local, 'trace': _trace_local,
                 'widths': _widths_local,
@@ -17788,8 +18088,8 @@ def f3_screen_stepg_run(st, *,
             # 🆕 `W-G.9-333` `c3`（`GB-168` 之修·`K-9-43`）：估算寬度改取**各側全鏈**
             #   （左 ＝ 推進至 k_max、右 ＝ 推進至 k_min 之試推進）之逐宗 `W` 差；
             #   居中平手仍用基準趟之宗地寬度。與 `verify/stepg_pipeline.py` 同構（#20）。
-            _kmin_c = 1 if _has_left_corner else 0
-            _kmax_c = (_N - 1) if _has_right_corner else _N
+            _kmin_c = 1 if (_has_left_corner or _eb_info['left'] is not None) else 0   # 🆕 W-G.9-352：末端塊同 pin
+            _kmax_c = (_N - 1) if (_has_right_corner or _eb_info['right'] is not None) else _N
             _wL_c = [0.0] * _N; _wR_c = [0.0] * _N
             _bL_c = _b_L0; _bR_c = _b_R0
             if _kmin_c <= _kmax_c:
@@ -17809,9 +18109,9 @@ def f3_screen_stepg_run(st, *,
             _slot_res = _select_pool_slot(
                 _wL_c,
                 {'has': _has_left_corner, 'F': _F_left,
-                 'l1': _lside_left, 'b': _bL_c},
+                 'l1': _lside_left, 'b': _bL_c, 'pin': _eb_info['left'] is not None},
                 {'has': _has_right_corner, 'F': _F_right,
-                 'l1': _lside_right, 'b': _bR_c},
+                 'l1': _lside_right, 'b': _bR_c, 'pin': _eb_info['right'] is not None},
                 widths_R=_wR_c, dev_widths=_adv_base['widths'],
             )
             _k_star = int(_slot_res['k'])
@@ -17844,6 +18144,8 @@ def f3_screen_stepg_run(st, *,
                     blk_meta['vertices'], d_hat, corner_pt,
                     allocation_dir_block, front_p2=_front_p2_blk,
                     has_side_right=_has_right_corner, forced_right=_fo_right)
+                if _eb_info['right'] is not None:   # 🆕 W-G.9-352：右鏈起於 FRONT p2（同推進）
+                    _smax_blk = S_block_max
             _s2 = _place_pool_parcels(
                 stage2_parcels=_stage2_parcels,
                 adv_final=_adv_final,
@@ -18398,6 +18700,8 @@ K6B_SCREEN_TRIAL_KEYS = (
     'f3_corner_cand_diag',
     # 🆕 `W-G.9-351`：入池閘之末態 build 與其末趟之不配地紀錄（配地本體所寫·調配之輸入）
     'f3_k929_6_build', 'f3_k929_6_dropped',
+    # 🆕 `W-G.9-352`：末端塊之評選（配地本體之首趟所寫·`SS_END_BLOCK_EVAL`；入池閘之畫面入口於復原之後帶出）
+    'f3_end_block_eval',
     # 🆕 `W-G.9-349`：入池閘之合併紀錄（配地本體所寫）
     'f3_k929_6_log',
 )
@@ -18713,10 +19017,12 @@ def _k929_6_screen_gate(st, g_kwargs):
         return list(_ss.get('f3_G_values') or []), _cp_k9296s.deepcopy(dict(K917_DROPPED)), None
 
     _err = None
+    _ev352 = None
     try:
         _bf, _last, _log = k929_6_fixpoint(
             g_kwargs['build_parcels'], _trial, _ss.get('t8_ownership_map', {}) or {},
             g_kwargs['pre_price_by_zone'], _ss.get('f3_cad_front_lines', {}) or {})
+        _ev352 = _cp_k9296s.deepcopy(_ss.get(SS_END_BLOCK_EVAL))   # 🆕 `W-G.9-352`：首趟之末端塊評選（本體沿用）
     except RuntimeError as _e_g:
         _err = str(_e_g).split("\n")[0][:500]
     finally:
@@ -18732,6 +19038,8 @@ def _k929_6_screen_gate(st, g_kwargs):
         st.stop()
         raise RuntimeError(_err)
     _ss[SS_ADJ_DROPPED] = _cp_k9296s.deepcopy(dict(_last[1]))   # 🆕 `W-G.9-351`：調配之輸入（末趟之不配地紀錄）
+    if _ev352 is not None:
+        _ss[SS_END_BLOCK_EVAL] = _ev352   # 🆕 `W-G.9-352`：本體沿用首趟之當選者（⛔ 以末態之合併單元重評）
     return _bf, _log
 
 
@@ -24784,6 +25092,17 @@ def main():
                             else:
                                 st.caption("（本次無合併試算）")
 
+                    # 🆕 `W-G.9-352`：末端塊之評選（無側街之端·`K-9-36`／`K-9-49`）——跨占者、各筆單獨試算之 G、當選者
+                    _eb352 = st.session_state.get(SS_END_BLOCK_EVAL)
+                    if _eb352 is not None:
+                        _eb352_v = end_block_eval_rows(_eb352)
+                        with st.expander("🧱 末端塊之評選（無側街之端·K-9-36／K-9-49）", expanded=False):
+                            for _eb352_l in _eb352_v['lines']:
+                                st.caption(_eb352_l)
+                            if _eb352_v['rows']:
+                                st.dataframe(_pd.DataFrame(_eb352_v['rows']),
+                                             use_container_width=True, hide_index=True)
+
                     # 🆕 `W-G.9-351`：調配階段之輸入（步 1 之尾〜步 2·`K-9-45`／`K-9-46`）——僅盤點·⛔ 調配
                     _adj351_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)
                     if _adj351_bf is not None:
diff --git a/verify/stepg_pipeline.py b/verify/stepg_pipeline.py
index 21b9cb3..b7b5d5e 100644
--- a/verify/stepg_pipeline.py
+++ b/verify/stepg_pipeline.py
@@ -258,6 +258,9 @@ def run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
     #   `k929_6_fixpoint` 求末態之 build（試算趟 ＝ 本函式 `_k929_6_inner=True`）；回末趟之結果（即以末態 build
     #   所跑者·⛔ 重跑）並掛 `k929_6`（`build`／`log`）。`K917_DROPPED` ＝ 呼叫前之內容 ＋ 末趟所記（同單趟之累加）。
     #   🔒 旗標 off ⇒ 本段⛔ 執行（逐位同本批前）。
+    # 🆕 `W-G.9-352`：末端塊之評選於本趟之首趟為之（入池閘之試算趟沿用·`SS_END_BLOCK_EVAL`）⇒ 非試算趟先清前次之評選。
+    if not _k929_6_inner:
+        fake_st.session_state.pop(ns["SS_END_BLOCK_EVAL"], None)
     if not _k929_6_inner and ns["k929_6_enabled"]():
         import copy as _cp_k9296
         _k917 = ns["K917_DROPPED"]
@@ -543,7 +546,7 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                    _baseline_pt, _S_max, _is_corner, _side, _avg_depth,
                    _allocation_dir=None, _side_mid=None, _W_prev=0.0,
                    _w0_start=None,
-                   _near_dir=None, _is_chain_head=False):
+                   _near_dir=None, _is_chain_head=False, _s_back=0.0):
         # 🆕 P-0b（裁定M·Q-M4）：薄殼委派 app module 級 `_solve_G_one`（單一真相源·經 ns）。
         #   B_value/C_for_calc（_compute_v3_finance 拆出）＋ _tab6_burden（本函式上方檢查）為閉包捕獲。
         return ns["_solve_G_one"](
@@ -554,7 +557,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
             allocation_dir=_allocation_dir, side_mid=_side_mid, W_prev=_W_prev,
             near_dir=_near_dir,   # 🆕 D-2b-23【甲】：界面單線（薄殼直通·不推導）
             w0_start=_w0_start,   # 🆕 W-G.9-318：K-9-41 ①（薄殼直通·⛔ 在此推導）
-            is_chain_head=_is_chain_head)   # 🆕 W-G.9-261：鏈頭旗標（薄殼直通·⛔ 不推導）
+            is_chain_head=_is_chain_head,   # 🆕 W-G.9-261：鏈頭旗標（薄殼直通·⛔ 不推導）
+            s_back=_s_back)   # 🆕 W-G.9-352：末端塊之未臨正街（薄殼直通·⛔ 在此推導）
 
     # ── 逐街廓（app Step G 迴圈逐行複刻；st.* 於 headless 為 fake no-op 故略） ──
     for blk_label, parcels_in_blk in parcels_by_block.items():
@@ -653,6 +657,19 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                 forced_offset=_v2_forced,
             )
             ordered_v2 = list(_v2_res.get('ordered', []) or [])
+        # 🆕 `W-G.9-352`：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49`）——原位次序列定後、`_ov2_idx` 前
+        #   （單一真相源 `end_block_host`·app 同構）。
+        _eb_info = {'left': None, 'right': None}
+        if (not _degenerate_order) and _front_p2_blk is not None:
+            ordered_v2, _eb_info = ns["end_block_host"](
+                ordered_v2, blk_label=blk_label, blk_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt,
+                front_p2=_front_p2_blk, alloc_dir_cad=_alloc_dir_cad,
+                allocation_dir=allocation_dir_block, session=ss,
+                corner_range_polys={_w_eb: ctx['corner_range_polys'].get((blk_label, _w_eb))
+                                    for _w_eb in ('left', 'right')},
+                solve_one=_solve_one, l_front=l_front, avg_depth=avg_depth_default,
+                S_block_max=S_block_max, post_price=post_price_by_block.get(blk_label, 0.0),
+                pre_price_by_zone=pre_price_by_zone)
         for _i_ov2, _e_ov2 in enumerate(ordered_v2):
             _e_ov2['_ov2_idx'] = _i_ov2
 
@@ -871,6 +888,9 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     _near_dir=_near_dir_left,   # 🆕 D-2b-23【甲】
                     _is_chain_head=(_lg_idx_left == 0),   # 🆕 W-G.9-261：本側鏈頭
                     _w0_start=(0.0 if not _fo_left else None),   # 🆕 K-9-41 ①前段（W-G.9-318 補令一）
+                    _s_back=(float(_eb_info['left']['s_back'])   # 🆕 W-G.9-352：末端塊（左）
+                             if (_eb_info['left'] is not None and _lg_idx_left == 0
+                                 and entry.get('is_end_block')) else 0.0),
                 )
                 # 🆕 `W-G.9-246′` 工項二 **站 3／4（harness 左鏈）**：`res` 定案後、鏈推進前。
                 #   🛑 只做二事：呼叫、寫欄（`I-5`）——⛔ 依其 verdict 寫任何 `if`。
@@ -931,6 +951,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                                                 front_p2=_front_p2_blk, has_side_right=_has_right_corner,
                                                 forced_right=_fo_right)
                 actual_max_proj = _smax_a if _smax_a is not None else S_block_max
+                if _eb_info['right'] is not None:   # 🆕 W-G.9-352：末端塊（右）⇒ 鏈起於 FRONT p2、首宗向外延伸未臨正街
+                    actual_max_proj = S_block_max
                 end_pt = corner_pt + actual_max_proj * d_hat
                 d_hat_rev = -d_hat
             else:
@@ -981,6 +1003,9 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     _near_dir=_near_dir_right,   # 🆕 D-2b-23【甲】
                     _is_chain_head=(_lg_idx_right == 0),   # 🆕 W-G.9-261：本側鏈頭
                     _w0_start=(0.0 if not _fo_right else None),  # 🆕 K-9-41 ①前段（W-G.9-318 補令一）
+                    _s_back=(float(_eb_info['right']['s_back'])   # 🆕 W-G.9-352：末端塊（右）
+                             if (_eb_info['right'] is not None and _lg_idx_right == 0
+                                 and entry.get('is_end_block')) else 0.0),
                 )
                 if (float(res.get('area_geom', 0)) < 0.5
                     and d_hat_rev is not None and baseline_pt is not None):
@@ -997,6 +1022,9 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                             _near_dir=_near_dir_right,   # 🆕 D-2b-23【甲】
                             _is_chain_head=(_lg_idx_right == 0),   # 🆕 W-G.9-261：本側鏈頭
                             _w0_start=(0.0 if not _fo_right else None),  # 🆕 K-9-41 ①前段（W-G.9-318 補令一）
+                            _s_back=(float(_eb_info['right']['s_back'])   # 🆕 W-G.9-352：末端塊（右）
+                                     if (_eb_info['right'] is not None and _lg_idx_right == 0
+                                         and entry.get('is_end_block')) else 0.0),
                         )
                         if float(_r2.get('area_geom', 0)) >= 0.5:
                             res, solver_label = _r2, _sl2
@@ -1053,6 +1081,10 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                 _trace_local[k] = res.get('trace', [])
                 right_results.append((entry, res))
 
+            # 🆕 `W-G.9-352`：定案趟之末端塊須為該側鏈之首宗（app 同構）
+            if _commit:
+                ns["end_block_assert_head"](blk_label, _eb_info, left_results, right_results)
+
             return {
                 'rows': _rows_local, 'trace': _trace_local,
                 'widths': _widths_local,
@@ -1107,8 +1139,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
             # 🆕 `W-G.9-333` `c3`（`GB-168` 之修·`K-9-43`）：估算寬度改取**各側全鏈**
             #   （左 ＝ 推進至 k_max、右 ＝ 推進至 k_min 之試推進）之逐宗 `W` 差（單一真相源
             #   `ns['_slot_side_chain_widths']`）；居中平手仍用基準趟之宗地寬度。app 同構（#20）。
-            _kmin_c = 1 if _has_left_corner else 0
-            _kmax_c = (_N - 1) if _has_right_corner else _N
+            _kmin_c = 1 if (_has_left_corner or _eb_info['left'] is not None) else 0   # 🆕 W-G.9-352：末端塊同 pin
+            _kmax_c = (_N - 1) if (_has_right_corner or _eb_info['right'] is not None) else _N
             _wL_c = [0.0] * _N; _wR_c = [0.0] * _N
             _bL_c = _b_L0; _bR_c = _b_R0
             if _kmin_c <= _kmax_c:
@@ -1128,9 +1160,9 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
             _slot_res = _select_pool_slot(
                 _wL_c,
                 {'has': _has_left_corner, 'F': _F_left,
-                 'l1': _lside_left, 'b': _bL_c},
+                 'l1': _lside_left, 'b': _bL_c, 'pin': _eb_info['left'] is not None},
                 {'has': _has_right_corner, 'F': _F_right,
-                 'l1': _lside_right, 'b': _bR_c},
+                 'l1': _lside_right, 'b': _bR_c, 'pin': _eb_info['right'] is not None},
                 widths_R=_wR_c, dev_widths=_adv_base['widths'],
             )
             _k_star = int(_slot_res['k'])
@@ -1170,6 +1202,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                 _smax_blk = _right_chain_origin_s(blk_meta['vertices'], d_hat, corner_pt,
                                                   allocation_dir_block, front_p2=_front_p2_blk,
                                                   has_side_right=_has_right_corner, forced_right=_fo_right)
+                if _eb_info['right'] is not None:   # 🆕 W-G.9-352：右鏈起於 FRONT p2（同推進）
+                    _smax_blk = S_block_max
             _s2 = ns["_place_pool_parcels"](
                 stage2_parcels=_stage2_parcels,
                 adv_final=_adv_final,
````

## 附錄乙　塊 `F11`（新檔 `verify/probes/probe_WG9352_endblock.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-352 量測器（發單側窗四十八擬·檔 F11·⛔ 由受單側改一字）：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49`）。

子命令（一律 python verify/probes/probe_WG9352_endblock.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `END_BLOCK_*`／`SS_END_BLOCK_EVAL` 與 `end_block_*`、
           `solve_G_binary`、`_select_pool_slot` 及其幾何基元）：觸發（左、右鏡像、未臨正街 ≤ ε 不觸發）、R_end 之面積、
           評選（往後找、等號當選、跨占 ≤ 門檻者非候選、跨占街角規定範圍者歸街角側、皆未達停機）、落位（左首、右末、
           入池閘合併單元、街角第 1 宗停機）、首趟評選之沿用、二源不一致停機、選槽之 pin、顯示、定案趟之檢、
           `s_back`（宗地 ＝ 未臨正街 ∪ 正街段；G 公式之 S 只計正街段；`s_back=0` 逐位同）。
           另施七突變，每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST／字樣查接線（app.py 與 verify/stepg_pipeline.py 二宿主）：W1 模組層之常數與函式、⛔ 案件字面；
           W2 二宿主於 `_ov2_idx` 之前恰一次呼叫 `end_block_host`（`solve_one=_solve_one`）；W3 左鏈一處、右鏈二處之
           `_solve_one` 帶 `_s_back`（取 `_eb_info`）；W4 定案趟呼叫 `end_block_assert_head`；W5 選槽之 `pin` 與
           `_kmin_c`／`_kmax_c`；W6 非試算趟先清 `SS_END_BLOCK_EVAL`；W7 入池閘之畫面入口於復原之後帶出評選、
           `K6B_SCREEN_TRIAL_KEYS` 含其鍵且末項仍為 `f3_k929_6_log`；W8 `_WF_NS_NAMES` 含三名；W9 `solve_G_binary`／
           `_solve_G_one` 之 `s_back` 與 fallback 停機；W10 `main()` 之顯示。另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：以本器**另寫之幾何與 G 公式**（⛔ 呼叫 `end_block_*`／
           `_end_region_R`／`solve_G_binary`）為外部錨：R1 各無側街之端之觸發與 R_end；R2 候選（跨占者依原投影序）、
           各筆單獨試算之 G 與當選者；R3 配地列：觸發之端之鏈首宗 ＝ 當選者、其宗地 ⊇ R_end、其 G ＝ 試算 G；
           R4 無抵費地與未臨正街相交；R5 本街廓之宗地與抵費地之聯集 ＝ 街廓、兩兩⛔ 疊。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

EB_FUNCS = ["end_block_side_geom", "end_block_pick", "end_block_pin", "end_block_apply",
            "end_block_host", "end_block_eval_rows", "end_block_assert_head"]
DEP_FUNCS = ["_strip_axis", "_strip_s_range", "_block_strip", "_end_band", "_end_region_R",
             "alloc_normal_axis", "solve_G_binary", "_select_pool_slot", "rw_from_width"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    tree = ast.parse(src)
    parts = []
    names = set(EB_FUNCS) | set(DEP_FUNCS)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id.startswith("END_BLOCK_") or node.targets[0].id == "SS_END_BLOCK_EVAL"
                     or node.targets[0].id in ("RW_SATURATION_WIDTH_M", "_STRIP_PARALLEL_TOL")):
            parts.append(ast.get_source_segment(src, node))
    got = {n.name for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in EB_FUNCS}
    if got != set(EB_FUNCS):
        raise KeyError("受詞缺")
    ns = {}
    exec(compile("\n\n".join(parts), "<eb_extract>", "exec"), ns)
    return ns


# ── 合成幾何：FRONT 沿 x 軸 p1=(0,0)→p2=(40,0)；ALLOC ∥ y 軸；深 30；左端外斜 3 m（未臨正街 45 ㎡）──
def _geo(ns, mirror=False):
    from shapely.geometry import Polygon
    import numpy as np
    if not mirror:
        blk = Polygon([(0, 0), (40, 0), (40, 30), (-3, 30)])
    else:
        blk = Polygon([(0, 0), (40, 0), (43, 30), (0, 30)])
    cad = (0.0, 1.0)
    return dict(blk=blk, d=np.array([1.0, 0.0]), p1=np.array([0.0, 0.0]), p2=np.array([40.0, 0.0]),
                cad=cad, ad=ns["alloc_normal_axis"](cad))


def _tp(pid, coords, lot=None, **kw):
    d = {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in coords]}
    d.update(kw)
    return d


def _e(tp, **kw):
    d = {"tp": tp, "pre_position": 0, "is_corner_winner": False, "side": "中段"}
    d.update(kw)
    return d


def _cases(ns):
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__)
        out.append((name, got, exp))

    G = _geo(ns)
    GM = _geo(ns, mirror=True)
    geo = ns["end_block_side_geom"]

    def gl(g, side):
        r = geo(g["blk"], g["d"], g["p1"], g["p2"], g["cad"], g["ad"], 3.5, side, _label="T")
        return (r["gate"], round(r["unfront"], 4), round(r.get("s_back", 0.0), 4),
                round(r.get("r_end_area", 0.0), 4), round(r.get("band_area", 0.0), 4))

    run("S1 左端觸發（未臨正街 45·s_back 3·末端帶 105·R_end 150）", lambda: gl(G, "left"),
        (True, 45.0, 3.0, 150.0, 105.0))
    run("S2 右端觸發（鏡像）", lambda: gl(GM, "right"), (True, 45.0, 3.0, 150.0, 105.0))
    run("S3 未臨正街 0 ⇒ 不觸發（左端鉛直）", lambda: gl(GM, "left")[0], False)

    gg = geo(G["blk"], G["d"], G["p1"], G["p2"], G["cad"], G["ad"], 3.5, "left", _label="T")
    # 原位次序列（自左端起）：a 跨占 R_end（6 ㎡）、b 跨占（G 恰 150）、c 跨占、d 不跨占
    a = _tp("A(1)", [(-3, 30), (-1, 10), (5, 10), (5, 30)])
    b = _tp("B(1)", [(-1, 10), (0, 0), (5, 0), (5, 10)])
    c = _tp("C(1)", [(3.4, 0), (10, 0), (10, 30), (3.4, 30)])
    dd = _tp("D(1)", [(20, 0), (30, 0), (30, 30), (20, 30)])
    tiny = _tp("T(1)", [(3.0, 0), (3.49, 0), (3.49, 1.0), (3.0, 1.0)])
    Gv = {"A(1)": 100.0, "B(1)": 150.0, "C(1)": 500.0, "D(1)": 900.0, "T(1)": 999.0}
    calls = []

    def trial(tp):
        calls.append(tp["暫編地號"])
        return Gv[tp["暫編地號"]], 5.0

    pick = ns["end_block_pick"]
    seq = [_e(a), _e(b), _e(c), _e(dd)]
    run("S4 往後找·等號當選（A 未達、B ＝ 150 當選）",
        lambda: (pick("left", gg, seq, {}, trial, _label="T")["winner"],
                 [r["結果"] for r in pick("left", gg, seq, {}, trial, _label="T")["rows"]]),
        ("B(1)", ["未達", "當選"]))
    run("S5 跨占 ≤ 門檻者非候選（T 跨占 0.49 ㎡）",
        lambda: pick("left", gg, [_e(tiny), _e(c)], {}, trial, _label="T")["winner"], "C(1)")
    from shapely.geometry import Polygon as _P
    run("S6 跨占街角規定範圍者歸街角側（⛔ 候選）",
        lambda: [(r["暫編地號"], r["結果"]) for r in pick("left", gg, [_e(b), _e(c)], {"right": _P([(-1, 0), (1, 0), (1, 12), (-1, 12)])},
                                                         trial, _label="T")["rows"]],
        [("B(1)", "跨占街角規定範圍·歸街角側"), ("C(1)", "當選")])
    run("S7 皆未達 ⇒ 停機", lambda: pick("left", gg, [_e(a)], {}, trial, _label="T"), ("例外", "RuntimeError"))

    pin = ns["end_block_pin"]
    run("S8 落位（左）：當選者移至首·餘者原序",
        lambda: [(x["tp"]["暫編地號"], bool(x.get("is_end_block"))) for x in pin(seq, "left", "C(1)", _label="T")],
        [("C(1)", True), ("A(1)", False), ("B(1)", False), ("D(1)", False)])
    run("S9 落位（右）：當選者移至末",
        lambda: [x["tp"]["暫編地號"] for x in pin(seq, "right", "B(1)", _label="T")],
        ["A(1)", "C(1)", "D(1)", "B(1)"])
    u = _tp("U(1)", [(0, 0), (1, 0), (1, 1)], 入池閘併入=["U(1)", "B(1)"])
    run("S10 落位：當選者為入池閘合併單元之成員 ⇒ 移該單元",
        lambda: [x["tp"]["暫編地號"] for x in pin([_e(a), _e(u)], "left", "B(1)", _label="T")], ["U(1)", "A(1)"])
    run("S10b 落位：當選者為街角第 1 宗 ⇒ 停機",
        lambda: pin([_e(a, is_corner_winner=True)], "left", "A(1)", _label="T"), ("例外", "RuntimeError"))

    apply = ns["end_block_apply"]

    def ap(cache, trial_fn, has_pk=None, has_cad=None, g=G, order=None):
        return apply(order or seq, blk_label="BX", block_poly=g["blk"], d_hat=g["d"], corner_pt=g["p1"],
                     front_p2=g["p2"], cad_alloc=g["cad"], allocation_dir=g["ad"], min_width=3.5,
                     has_side_pk=has_pk or {"left": False, "right": True},
                     has_side_cad=has_cad or {"left": False, "right": True},
                     corner_range_polys={}, trial=trial_fn, cache=cache)

    def s11():
        cache = {}
        calls.clear()
        o1, i1 = ap(cache, lambda tp, s, w: trial(tp))
        n1 = len(calls)
        calls.clear()
        o2, i2 = ap(cache, lambda tp, s, w: (0.0, 0.0), order=[_e(dd), _e(c), _e(b), _e(a)])
        return (o1[0]["tp"]["暫編地號"], n1, o2[0]["tp"]["暫編地號"], len(calls), round(i1["left"]["s_back"], 4),
                cache["BX"]["left"]["當選"], i1["right"])
    run("S11 首趟評選、次趟沿用（⛔ 重評）", s11, ("B(1)", 2, "B(1)", 0, 3.0, "B(1)", None))
    run("S11b 二源不一致 ⇒ 停機",
        lambda: ap({}, lambda tp, s, w: trial(tp), has_pk={"left": False, "right": True},
                   has_cad={"left": True, "right": True}), ("例外", "RuntimeError"))
    run("S12 首趟未觸發而本趟觸發 ⇒ 停機",
        lambda: ap({"BX": {"left": {"觸發": False}}}, lambda tp, s, w: trial(tp)), ("例外", "RuntimeError"))

    sps = ns["_select_pool_slot"]
    run("S13 選槽之 pin（左 pin ⇒ k≥1；右 pin ⇒ k≤n−1）",
        lambda: (min(t["k"] for t in sps([1, 1, 1], {"has": False, "pin": True}, {"has": False})["table"]),
                 max(t["k"] for t in sps([1, 1, 1], {"has": False}, {"has": False, "pin": True})["table"]),
                 min(t["k"] for t in sps([1, 1, 1], {"has": False}, {"has": False})["table"])),
        (1, 2, 0))
    run("S14 顯示（值皆字串·未觸發之端具名）",
        lambda: (ns["end_block_eval_rows"]({"BX": {"left": {"觸發": True, "未臨正街(㎡)": 45.0, "末端帶(㎡)": 105.0,
                                                           "R_end(㎡)": 150.0, "當選": "B(1)",
                                                           "候選": [{"暫編地號": "A(1)", "試算G(㎡)": None}]},
                                                  "right": {"觸發": False, "未臨正街(㎡)": 0.0}}})),
        {"lines": ["BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；當選 B(1)",
                   "BX 右端（無側街）：未臨正街 0.0 ㎡ ⇒ 未觸發"],
         "rows": [{"街廓": "BX", "端": "左", "暫編地號": "A(1)", "試算G(㎡)": "—"}]})
    ah = ns["end_block_assert_head"]
    run("S15 定案趟之檢：首宗非當選者 ⇒ 停機；是 ⇒ 過",
        lambda: ((lambda: (ah("BX", {"left": {"winner": "B(1)"}, "right": None}, [(_e(a), {})], []), "過")[1])(),),
        ("例外", "RuntimeError"))
    run("S15b 定案趟之檢：首宗為當選者 ⇒ 過",
        lambda: (ah("BX", {"left": {"winner": "B(1)"}, "right": None}, [(_e(b, is_end_block=True), {})], []), "過")[1],
        "過")

    sgb = ns["solve_G_binary"]
    a_, A_, B_, C_, l2 = 700.0, 1.2, 0.2, 0.1, 2.0

    def s16():
        r = sgb(a=a_, A=A_, B=B_, C=C_, l_front=l2, l_side=0.0, F=0.0, block_poly=G["blk"], d_hat=G["d"],
                baseline_pt=G["p1"], S_max_limit=40.0, allocation_dir=G["ad"], s_back=3.0)
        cut = _P(r["cut_coords"])
        S = float(r["S_raw"])
        Gf = (a_ * (1 - A_ * B_) - S * l2) * (1 - C_)
        wedge = _P([(0, 0), (0, 30), (-3, 30)])
        return (abs(r["G"] - round(Gf, 2)) <= 0.01, abs(cut.area - Gf) <= 0.02,
                round(wedge.difference(cut).area, 6), round(cut.bounds[0], 4), abs(cut.bounds[2] - S) <= 1e-6)
    run("S16 s_back：宗地 ＝ 未臨正街 ∪ [0,S]；G 之 S 只計正街段", s16, (True, True, 0.0, -3.0, True))

    def s17():
        kw = dict(a=a_, A=A_, B=B_, C=C_, l_front=l2, l_side=0.0, F=0.0, block_poly=G["blk"], d_hat=G["d"],
                  baseline_pt=G["p1"], S_max_limit=40.0, allocation_dir=G["ad"])
        r0 = sgb(**kw)
        r1 = sgb(**kw, s_back=0.0)
        return (r0["cut_coords"] == r1["cut_coords"], r0["G"] == r1["G"], r0["S_raw"] == r1["S_raw"])
    run("S17 s_back＝0 ⇒ 逐位同", s17, (True, True, True))
    run("S18 s_back 與 side_mid 並存 ⇒ 停機",
        lambda: sgb(a=a_, A=A_, B=B_, C=C_, l_front=l2, l_side=0.0, F=0.0, block_poly=G["blk"], d_hat=G["d"],
                    baseline_pt=G["p1"], S_max_limit=40.0, allocation_dir=G["ad"], side_mid=(0, 15), s_back=3.0),
        ("例外", "RuntimeError"))
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
    except Exception:  # noqa: BLE001
        print(f"  🔴 受詞缺：{EB_FUNCS}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（AST 抽出之 end_block_*／solve_G_binary／_select_pool_slot）──")
    red = _report(_cases(ns))
    print("── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──")
    base_red = set(red)
    m0 = _report(_cases(_extract_ns(src)), verbose=False)
    print(("  ✅ " if m0 == red else "  🔴 ") + f"M0 未突變之抽出版：紅 {m0}（期 {red}）")
    if m0 != red:
        red.append("M0")
    muts = [
        ("M1 當選改為嚴格大於", "_ok = float(_g) >= _thr", "_ok = float(_g) > _thr"),
        ("M2 首筆跨占者即當選（⛔ 往後找）", "        rows.append(_row)\n        if _ok:",
         "        rows.append(_row)\n        if True:"),
        ("M3 跨占街角規定範圍者⛔ 排除",
         "if any(float(_pg.intersection(_c).area) > END_BLOCK_CROSS_MIN_AREA for _c in _crs):", "if False:"),
        ("M4 落位⛔ 移至首", "        _out.insert(0, _e)", "        _out.insert(_idx[0], _e)"),
        ("M5 未臨正街計入臨街", "                             - S_guess * l_front) * (1.0 - C))",
         "                             - (S_guess + _s_back) * l_front) * (1.0 - C))"),
        ("M6 首趟評選⛔ 沿用", "        if _cached is not None:\n            _c = _cached.get(_sd) or {}",
         "        if False:\n            _c = _cached.get(_sd) or {}"),
        ("M7 選槽⛔ 理 pin", "    k_min = 1 if (has_L or bool(_L.get('pin'))) else 0", "    k_min = 1 if has_L else 0"),
    ]
    for mname, x, y in muts:
        if src.count(x) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{src.count(x)}）")
            red.append(mname.split()[0])
            continue
        try:
            turned = [n for n in _report(_cases(_extract_ns(src.replace(x, y, 1))), verbose=False) if n not in base_red]
        except Exception as ex:  # noqa: BLE001
            turned = [f"抽出拋 {type(ex).__name__}"]
        ok = bool(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
def _fn_src(src, name):
    for n in ast.parse(src).body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return ast.get_source_segment(src, n)
    return None


def _wiring_checks(app, sg):
    res = []
    tree = ast.parse(app)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    lits = []
    for f in EB_FUNCS:
        if f in top:
            for n in ast.walk(top[f]):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value):
                    lits.append((f, n.value))
    ok1 = all(f in top for f in EB_FUNCS) and {"END_BLOCK_UNFRONT_EPS", "END_BLOCK_CROSS_MIN_AREA",
                                                 "SS_END_BLOCK_EVAL"} <= consts and not lits
    res.append((f"W1 模組層之常數與七函式、函式內⛔ 案件字面（案件字面 {lits}）", ok1, ""))
    scr = _fn_src(app, "f3_screen_stepg_run") or ""
    hsg = _fn_src(sg, "_run_step_g_impl") or ""
    outer = _fn_src(sg, "run_step_g") or ""

    def host_ok(h, call):
        i = h.find(call)
        j = h.find("['_ov2_idx'] = ")
        return h.count(call) == 1 and 0 <= i < j and "solve_one=_solve_one" in h[i:i + 1200]
    res.append(("W2 二宿主於 `_ov2_idx` 前恰一次呼叫 end_block_host（solve_one=_solve_one）",
                host_ok(scr, "end_block_host(") and host_ok(hsg, 'ns["end_block_host"]('), ""))
    pl = "_s_back=(float(_eb_info['left']['s_back'])"
    pr = "_s_back=(float(_eb_info['right']['s_back'])"
    res.append(("W3 左鏈一處、右鏈二處之 `_solve_one` 帶 `_s_back`（二宿主）",
                scr.count(pl) == 1 and scr.count(pr) == 2 and hsg.count(pl) == 1 and hsg.count(pr) == 2, ""))
    res.append(("W4 定案趟呼叫 end_block_assert_head（二宿主）",
                re.search(r"if _commit:\s*\n\s*end_block_assert_head\(blk_label, _eb_info, left_results, right_results\)", scr)
                is not None and
                re.search(r'if _commit:\s*\n\s*ns\["end_block_assert_head"\]\(blk_label, _eb_info, left_results, right_results\)', hsg)
                is not None, ""))
    pin = ("'pin': _eb_info['left'] is not None", "'pin': _eb_info['right'] is not None",
           "_kmin_c = 1 if (_has_left_corner or _eb_info['left'] is not None) else 0",
           "_kmax_c = (_N - 1) if (_has_right_corner or _eb_info['right'] is not None) else _N")
    res.append(("W5 選槽之 pin 與 _kmin_c／_kmax_c（二宿主）", all(scr.count(p) == 1 and hsg.count(p) == 1 for p in pin), ""))
    res.append(("W6 非試算趟先清 SS_END_BLOCK_EVAL（二宿主）",
                re.search(r"if not _k929_6_inner:\s*\n\s*st\.session_state\.pop\(SS_END_BLOCK_EVAL, None\)", scr) is not None
                and re.search(r'if not _k929_6_inner:\s*\n\s*fake_st\.session_state\.pop\(ns\["SS_END_BLOCK_EVAL"\], None\)', outer)
                is not None, ""))
    gate = _fn_src(app, "_k929_6_screen_gate") or ""
    keys = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "K6B_SCREEN_TRIAL_KEYS" for t in n.targets):
            keys = ast.literal_eval(n.value)
    ig = gate.find("_ss[SS_END_BLOCK_EVAL] = _ev352")
    res.append(("W7 入池閘之畫面入口於復原之後帶出評選；鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log",
                ig > gate.find("finally:") > 0 and "_ev352 = _cp_k9296s.deepcopy(_ss.get(SS_END_BLOCK_EVAL))" in gate
                and bool(keys) and "f3_end_block_eval" in keys and keys[-1] == "f3_k929_6_log", ""))
    wf = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
            wf = ast.literal_eval(n.value)
    res.append(("W8 _WF_NS_NAMES 含 end_block_host／end_block_assert_head／SS_END_BLOCK_EVAL",
                bool(wf) and {"end_block_host", "end_block_assert_head", "SS_END_BLOCK_EVAL"} <= set(wf), ""))
    sgb = _fn_src(app, "solve_G_binary") or ""
    sgo = _fn_src(app, "_solve_G_one") or ""
    res.append(("W9 solve_G_binary／_solve_G_one 之 s_back 與 fallback 停機",
                "s_back: float = 0.0" in sgb and "_S + _s_back, allocation_dir=allocation_dir)" in sgb
                and "s_back=s_back," in sgo and "if float(s_back or 0.0) > 0.0:" in sgo, ""))
    mn = _fn_src(app, "main") or ""
    res.append(("W10 main() 之顯示（end_block_eval_rows 讀 SS_END_BLOCK_EVAL）",
                "_eb352 = st.session_state.get(SS_END_BLOCK_EVAL)" in mn and "end_block_eval_rows(_eb352)" in mn, ""))
    return res


def wiring(repo):
    app = _read(repo, "app.py")
    sg = _read(repo, "verify/stepg_pipeline.py")

    def rep(r):
        red = []
        for n, ok, note in r:
            print(("  ✅ " if ok else "  🔴 ") + n + (f"（{note}）" if note else ""))
            if not ok:
                red.append(n.split()[0])
        return red
    print("── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py）──")
    red = rep(_wiring_checks(app, sg))
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    base = {n.split()[0] for n, ok, _ in _wiring_checks(app, sg) if not ok}
    muts = [
        ("N1 harness 左鏈去 _s_back", "sg", "_s_back=(float(_eb_info['left']['s_back'])", "_s_bak=(float(_eb_info['left']['s_back'])"),
        ("N2 入池閘之畫面入口⛔ 帶出評選", "app", "        _ss[SS_END_BLOCK_EVAL] = _ev352", "        pass"),
        ("N3 畫面選槽去 pin", "app", "'l1': _lside_left, 'b': _bL_c, 'pin': _eb_info['left'] is not None},",
         "'l1': _lside_left, 'b': _bL_c},"),
        ("N4 harness 非試算趟⛔ 清評選", "sg", '        fake_st.session_state.pop(ns["SS_END_BLOCK_EVAL"], None)', "        pass"),
    ]
    for mname, which, x, y in muts:
        s_app, s_sg = app, sg
        tgt = s_app if which == "app" else s_sg
        if tgt.count(x) != 1:
            print(f"  🔴 {mname}：突變錨不存在（{tgt.count(x)}）")
            red.append(mname.split()[0])
            continue
        if which == "app":
            s_app = app.replace(x, y, 1)
        else:
            s_sg = sg.replace(x, y, 1)
        turned = sorted({n.split()[0] for n, ok, _ in _wiring_checks(s_app, s_sg) if not ok} - base)
        print(("  ✅ " if turned else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not turned:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本器另寫之幾何與 G 公式（外部錨）──
def _s_of(x, p1, d, u):
    """點 x 之 s 座標（沿 d，切線 ∥ u）：x = p1 + s·d + t·u。"""
    import numpy as np
    v = np.asarray(x, float) - p1
    den = d[0] * u[1] - d[1] * u[0]
    return (v[0] * u[1] - v[1] * u[0]) / den


def _halfplane(p1, d, u, s_lo, s_hi, big):
    """{s_lo ≤ s ≤ s_hi} 之平行四邊形（切線 ∥ u）。"""
    from shapely.geometry import Polygon
    import numpy as np
    a = p1 + s_lo * d
    b = p1 + s_hi * d
    return Polygon([a - big * u, b - big * u, b + big * u, a + big * u])


def run(repo, sbs):
    import numpy as np
    from shapely.geometry import Polygon, LineString
    from shapely.ops import unary_union
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        from app_harvest import harvest
        with contextlib.redirect_stdout(io.StringIO()):
            ns, fake_st = harvest(os.path.join(repo, "app.py"))
        if "end_block_host" not in ns:
            print("  🔴 受詞缺：end_block_host")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g, _compute_v3_finance
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
            ss = fake_st.session_state
            ev = ss.get(ns["SS_END_BLOCK_EVAL"]) or {}
            fin = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)
            B, C = fin["B"], fin["C"]
            print(f"══ 退縮 {sb} ══")
            rows = sg["g_rows"]
            mwmap = ss.get("f3_min_width_by_label", {}) or {}
            slbs = cad.get("side_lines_by_side", {}) or {}
            for blk, fo in sorted(forced.items()):
                bm = cb_by[blk]
                bp = Polygon(bm["vertices"])
                bp = bp if bp.is_valid else bp.buffer(0)
                fl = cad["front_lines"][blk]
                p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
                L = float(np.linalg.norm(p2 - p1))
                d = (p2 - p1) / L
                u = np.array(cad["alloc_dir_by_block"][blk], float)
                u = u / np.linalg.norm(u)
                big = 4 * float(np.hypot(*(np.array(bp.bounds[2:]) - np.array(bp.bounds[:2]))))
                svals = [_s_of(v, p1, d, u) for v in bp.exterior.coords]
                smin, smax = min(svals), max(svals)
                mw = float(mwmap.get(blk, 0.0) or 0.0)
                for side in ("left", "right"):
                    has = bool(fo.get(f"{side}_has_side")) or ((slbs.get(blk) or {}).get(side) or {}).get("mid") is not None
                    if has:
                        continue
                    rec = (ev.get(blk) or {}).get(side)
                    if side == "left":
                        unf = bp.intersection(_halfplane(p1, d, u, smin - 1.0, 0.0, big)) if smin < -1e-6 else Polygon()
                        endp = p1
                    else:
                        unf = bp.intersection(_halfplane(p1, d, u, L, smax + 1.0, big)) if smax > L + 1e-6 else Polygon()
                        endp = p2
                    trig = unf.area > 1e-3
                    ok1 = rec is not None and bool(rec.get("觸發")) == trig
                    if not trig:
                        print(("  ✅" if ok1 else "  🔴") + f" R1 {blk} {side}：未臨正街 {unf.area:.4f} ㎡ ⇒ 不觸發（評選紀錄 {rec}）")
                        if not ok1:
                            red.append(f"R1@{sb}:{blk}{side}")
                        continue
                    nrm = np.array([-u[1], u[0]])
                    if np.dot(np.asarray(bp.centroid.coords[0]) - endp, nrm) < 0:
                        nrm = -nrm
                    band = bp.intersection(Polygon([endp - big * u, endp + big * u, endp + big * u + mw * nrm,
                                                    endp - big * u + mw * nrm]))
                    rend = unary_union([unf, band])
                    ok1 = ok1 and abs(rec["R_end(㎡)"] - round(rend.area, 2)) <= 0.011 \
                        and abs(rec["未臨正街(㎡)"] - round(unf.area, 2)) <= 0.011
                    print(("  ✅" if ok1 else "  🔴") + f" R1 {blk} {side}：未臨正街 {unf.area:.2f}＋末端帶 {band.area:.2f}"
                          f"＝R_end {rend.area:.2f}（紀錄 {rec['未臨正街(㎡)']}／{rec['末端帶(㎡)']}／{rec['R_end(㎡)']}）")
                    if not ok1:
                        red.append(f"R1@{sb}:{blk}{side}")
                    # R2：候選與試算（外部錨：本器之帶與 G 公式）
                    l2 = float(fin["sb_rows_by_label"][blk]["正街尺度"])
                    post = float(fin["post_price_by_block"][blk])
                    crps = [Polygon(c) for c in ((ss.get("f3_corner_range_polys", {}) or {}).get(blk) or {}).values()
                            if c and len(c) >= 3]
                    # 原位次：本器以代表點投影於 FRONT 線（p1→p2）排序（外部錨·⛔ 呼叫 _projection_order）
                    lots = [t for t in bp3 if t.get("所屬街廓") == blk and len(t.get("polygon_coords") or []) >= 3
                            and str(t.get("原地號", "")) != "_GHOST"]
                    fln = LineString([p1, p2])
                    lots.sort(key=lambda t: fln.project(Polygon(t["polygon_coords"]).representative_point()))
                    if side == "right":
                        lots = lots[::-1]
                    exp_rows = []
                    winner = None
                    for t in lots:
                        pg = Polygon(t["polygon_coords"])
                        pg = pg if pg.is_valid else pg.buffer(0)
                        ov = pg.intersection(rend).area
                        if ov <= 1.0:
                            continue
                        if any(pg.intersection(c).area > 1.0 for c in crps):
                            exp_rows.append((t["暫編地號"], "跨占街角規定範圍·歸街角側"))
                            continue
                        a = round(float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0), 2)
                        pre = float(fin["pre_price_by_zone"].get(t.get("重劃前地價區段", ""), 0.0) or 0.0)
                        A = post / pre if pre > 0 else 1.0
                        w = (-smin) if side == "left" else (smax - L)

                        def area_at(S):
                            if side == "left":
                                return bp.intersection(_halfplane(p1, d, u, -w, S, big)).area
                            return bp.intersection(_halfplane(p1, d, u, L - S, L + w, big)).area
                        lo, hi = 0.0, L
                        for _ in range(100):
                            m = (lo + hi) / 2
                            if area_at(m) - (a * (1 - A * B) - m * l2) * (1 - C) < 0:
                                lo = m
                            else:
                                hi = m
                        S = (lo + hi) / 2
                        g = (a * (1 - A * B) - S * l2) * (1 - C)
                        res_ = "當選" if round(g, 2) >= rec["R_end(㎡)"] - 1e-9 else "未達"
                        exp_rows.append((t["暫編地號"], res_, round(g, 2)))
                        if res_ == "當選":
                            winner = t["暫編地號"]
                            break
                    got_rows = [(r["暫編地號"], r["結果"]) + ((r["試算G(㎡)"],) if r["試算G(㎡)"] is not None else ())
                                for r in rec["候選"]]
                    ok2 = winner == rec["當選"] and len(got_rows) == len(exp_rows) and all(
                        gr[:2] == er[:2] and (len(er) < 3 or abs(gr[2] - er[2]) <= 0.02)
                        for gr, er in zip(got_rows, exp_rows))
                    print(("  ✅" if ok2 else "  🔴") + f" R2 {blk} {side}：候選與試算 {got_rows} ＝ 外部錨 {exp_rows}")
                    if not ok2:
                        red.append(f"R2@{sb}:{blk}{side}")
                    # R3：配地列
                    chain = sorted([r for r in rows if r["所屬街廓"] == blk and r["推進側別"] == side],
                                   key=lambda r: float(r.get("累積S(m)", 0) or 0))
                    head = chain[0] if chain else None
                    hp = Polygon(head["cut_coords"]) if head and head.get("cut_coords") else Polygon()
                    trial_g = next((x[2] for x in exp_rows if x[0] == winner and len(x) > 2), None)
                    ok3 = (head is not None and head["暫編地號"] == winner and rend.difference(hp).area <= 1e-6
                           and trial_g is not None and abs(float(head["G(㎡)"]) - trial_g) <= 0.02)
                    print(("  ✅" if ok3 else "  🔴") + f" R3 {blk} {side}：鏈首宗 {head and head['暫編地號']}"
                          f"（G {head and head['G(㎡)']}·試算 {trial_g}）⊇ R_end（差 {rend.difference(hp).area:.6f}）")
                    if not ok3:
                        red.append(f"R3@{sb}:{blk}{side}")
                    pools = [Polygon(r["cut_coords"]) for r in rows if r["所屬街廓"] == blk
                             and r["推進側別"] not in ("left", "right") and r.get("cut_coords")]
                    pw = sum(p.intersection(unf).area for p in pools)
                    ok4 = pw <= 1e-6
                    print(("  ✅" if ok4 else "  🔴") + f" R4 {blk} {side}：抵費地 ∩ 未臨正街 ＝ {pw:.6f} ㎡")
                    if not ok4:
                        red.append(f"R4@{sb}:{blk}{side}")
                    allp = [Polygon(r["cut_coords"]) for r in rows if r["所屬街廓"] == blk and r.get("cut_coords")]
                    un = unary_union(allp)
                    ovl = sum(allp[i].intersection(allp[j]).area for i in range(len(allp)) for j in range(i + 1, len(allp)))
                    ok5 = un.symmetric_difference(bp).area <= 0.05 and ovl <= 0.05
                    print(("  ✅" if ok5 else "  🔴") + f" R5 {blk}：宗地與抵費地之聯集 △ 街廓 {un.symmetric_difference(bp).area:.4f} ㎡、"
                          f"兩兩疊 {ovl:.4f} ㎡")
                    if not ok5:
                        red.append(f"R5@{sb}:{blk}")
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

## 附錄丙　塊 `K1`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-49` 之立 ＋ `K-9-36` 之落地狀態（`W-G.9-352`·⛔ 上文一字不刪·純末端追加）

### 🔒 `K-9-49`　**末端塊之評選之補明：跨占 `R_end` 者先各筆單獨試算；皆未達者比照街角地，將跨占者與同地主相鄰之土地（同街廓內，再及道路、公設地）合併後依原投影序再試一次，仍未達始以 `R_end` 為強制抵費地；與有側街之街角競合者街角優先——末端塊之評選（含合併再試）一律於全案街角（含合併再試及其後之分配）定案後辦理**（KL 裁 `2026-09-27`·canonical·**逐字**）

**編號之由**（`W-G.9-352 §零-1`）：`K-9-49` 於開工態 `ed6871a` 之宣告框 `0`；鬆框 `2` 列（`docs/orders/W-G.9-332_輕量單.md:28`、`docs/reports/W-G.9-332R_CC交接文.md:88`）係其時「對照乙［必為零］」所列之未取號·⛔ 占用 ⇒ 取之。
**出處**：發單側窗四十八（`2026-09-27`）；呈文附平面圖二幀（`R6` 左端之兩讀法、末端塊與街角之競合示意·⛔ 入倉）。

**發單側所呈之題與 KL 原文（逐字·⛔ 增刪一字）**

其一（發單側所呈【要你判斷】）：
> 末端塊的評選，跨占 R_end 的土地以「各筆單獨試算」（讀法甲，R6 左端由 G008 當選）？（是／否；否即採讀法乙，由 G017 當選）

KL 之問（`16:11`）：
> 若讀法甲，各筆單獨試算後，跨占R_end者均無合格者，是將R_end做為抵費地?

其二（發單側所呈【要你判斷】）：
> 一、末端塊的評選，跨占 R_end 的土地以「各筆單獨試算」（讀法甲，R6 左端由 G008 當選）？（是／否）
> 二、各筆單獨試算都沒有達標時，是否比照街角地，把跨占者與同地主相鄰的土地（同街廓內，再及道路、公設地）合併後，依原投影序再試一次，仍未達才以 R_end 為強制抵費地？（是／否；否即不合併再試，直接以 R_end 為強制抵費地）

KL 之答（`16:20`）：
> 採各筆單獨試算都沒有達標時，比照街角地，把跨占者與同地主相鄰的土地（同街廓內，再及道路、公設地）合併後，依原投影序再試一次，仍未達才以 R_end 為強制抵費地。
> 但是延伸一個問題你想想看，跨占R_end者進入同地主相鄰的土地（同街廓內，再及道路、公設地）合併機制，會不會有與他街廓（或同街廓）的街角（sideline側）地主有競合關係，若有與有sideline的街角地順序上競合的關係話，要以sideline的街角地為優先，因為sideline側才有雙面臨路，位置地段較好
> 目前程式邏輯上，若採比照街角地，把跨占者與同地主相鄰的土地（同街廓內，再及道路、公設地）合併機制，會產生問題?

其三（發單側所呈【要你判斷】）：
> 末端塊的評選（含合併再試）一律在全案街角地（含合併再試及其後的道路、公設地分配）都定案後才辦理；已上鎖、已併入或已分配給街角的土地不再併入末端塊；同時跨占兩者的土地歸街角側？（是／否）

KL 之答（`16:34`）：
> 是

**裁之內容**：
① **評選之受詞與次序**（`K-9-36 ①` 之補明）：跨占 `R_end` 之重劃前土地，依原投影序**各筆單獨**試算，第一個 `G ≥ area(R_end)` 者當選（讀法甲；KL `16:20` 之語以「採各筆單獨試算都沒有達標時」起句，發單側覆命載「已記下您的裁示：1. 跨占 R_end 的土地先各筆單獨試算（讀法甲）」，KL 其後答「是」未駁）；
② **皆未達**：比照街角地（`K-9-48` 其一），將跨占者與同地主相鄰之土地（先同街廓內，次道路、公設地）合併後，依原投影序再試一次；仍未達 ⇒ `R_end` 範圍為強制抵費地（`K-9-36 ③`）；
③ **競合與先後**：與有側街之街角地競合者，**街角優先**（KL 逐字「因為sideline側才有雙面臨路，位置地段較好」）⇒ 末端塊之評選（含合併再試）一律於全案街角地（含合併再試及其後之道路、公設地分配）皆定案後辦理；已上鎖、已併入或已分配予街角之土地⛔ 再併入末端塊；同時跨占街角規定範圍與 `R_end` 之土地歸街角側（其三「是」）。

**射程**：① 及於**任一案件**；
② 合併再試之細節（跨道路兩側之順序、「不影響原位次」之檢核、合併群其餘片之分配）比照 `K-9-48`——發單側之讀法（⛔ 充裁）；
③ **⛔ 及於**：數末端塊之合併再試相互競合（同一地主之同一片同時可入二以上末端塊）之先後——⛔ 獲逐字 ⇒ **⛔ 據本裁推**，候另呈；末端塊之強制抵費地作調配池（`K-9-38`〜`40`）之任何事項。

**本案之量**（⛔ 為裁之一部·發單側窗四十八·態 `ed6871a` ＋ `W-G.9-352` 之塊·harness·退縮 `3.5 m`／`0 m` 同）：`R6` 左端（無側街）未臨正街 `85.71` ＋ 末端帶 `166.57` ＝ `R_end` `252.28 ㎡`；跨占者依原投影序各筆單獨試算：`628(2)`（`G009`）`7.65`、`628-1(2)`（`G009`）`148.99`、`628-23(1)`（`G017`）`73.76` 皆未達；`628-4(1)`（`G008`）`695.38` 當選；`R2` 右、`R3` 左、`R5` 右之未臨正街皆 ≤ `0.0001 ㎡` ⇒ 不觸發。

**落地狀態**：
- `K-9-36 ①②`、本裁 `①③` ＝ `W-G.9-352` 落地（`③` 之「全案街角先定案」：評選置於配地之首趟、街角選位〔含段三及其後處理〕之後；「同時跨占二者歸街角側」：跨占本街廓任一街角規定範圍者⛔ 為候選）；
- 本裁 `②`、`K-9-36 ③` ⬜ **未落地**（現碼：皆未達 ⇒ 停機·⛔ 靜默）；`K-9-36 ④⑤`、`K-9-38`〜`40` ⬜。

🛑 **⛔ 據本裁推**：⛔ 推數末端塊競合之先後、⛔ 推合併再試之實作形、⛔ 推任何強制抵費地之面積。
````

## 附錄丁　塊 `G4`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-178` 之進度（五）（`W-G.9-352`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `ed6871af9ce2bf352ff8c5a7916ddccfca1ebc0a`（本批開工態）。**授權** ＝ `docs/orders/W-G.9-352_重量單.md` 工項三。⛔ 鑄號。

### `GB-178` 之進度（五）（⛔ 解除）

**所據**：`K-9-36 ①②` 與 `K-9-49 ①③`（KL 裁 `2026-09-27`）之碼側落地 ＝ `W-G.9-352` 工項二（`app.py`、`verify/stepg_pipeline.py`）。
**實測**（發單側窗四十八·倉外·harness·態 `ed6871a` ＋ 塊 `D1`·退縮 `3.5 m`／`0 m`·器 `verify/probes/probe_WG9352_endblock.py run`）：`R6` 左端（無側街）之未臨正街 `85.71 ㎡` 併入末端塊之當選者 `628-4(1)`（`G008`）之宗地（其宗地 ⊇ `R_end`·差 `0.000000 ㎡`）；`R6` 之抵費地與未臨正街之交 ＝ `0.000000 ㎡`；`R6` 之抵費地由二片（`R6-抵費地-1` `1819.35`／`R6-抵費地-2` `85.71`）成一片（`R6-抵費地` `1901.82 ㎡`）。
**失效條件四項之現況**：`(1)`、`(2)`、`(4)` 同進度（三）；`(3)` **未成就**——`R6` `85.71` ⇒ **已消除**（上開）；`R1` `0.0046` ⇒ `GB-186`（成因【未證】）；其餘同進度（三）。
🛑 **⛔ 解除、⛔ 收窄**（`(3)` 未成就）。
````

## 附錄戊　塊 `P6`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：末端塊之評選與落位（`K-9-36 ①②`·`K-9-49 ①③`）＋ 新調配模組之單序（`W-G.9-352`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `ed6871af9ce2bf352ff8c5a7916ddccfca1ebc0a`（本批開工態）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 末端塊之評選與落位（`K-9-36 ①②`·`K-9-49 ①③`·補丁十 §一） | `end_block_*`：無側街之端（街角選位表與 CAD 二源一致）且未臨正街 ＞ `END_BLOCK_UNFRONT_EPS` ⇒ `R_end` ＝ 未臨正街 ∪ 末端帶；跨占 `R_end`（＞ `END_BLOCK_CROSS_MIN_AREA`）之原位次序列之宗依原投影序各筆單獨試算（首宗含未臨正街·`G` 之 `S` 只計正街段），第一個 `G ≥ area(R_end)` 者當選並移至該端第 `1` 位；跨占本街廓任一街角規定範圍者⛔ 為候選；評選於配地之首趟為之（入池閘之試算趟與本體沿用）；畫面成果區「🧱 末端塊之評選」 | ✅ | `docs/orders/W-G.9-352_重量單.md` |
| `2` | 末端塊之合併再試與強制抵費地（`K-9-49 ②`·`K-9-36 ③`） | 各筆單獨皆未達 ⇒ 比照街角地（`K-9-48`）合併再試；仍未達 ⇒ `R_end` 為強制抵費地（面積嚴格 ＝ `area(R_end)`·占末端位）；現碼 ⇒ 停機（⛔ 靜默）；數末端塊之競合 ⛔ 獲逐字（候另呈） | ⬜ | 次單 |
| `3` | 規格步 `3` 候選街廓名單（五級八鍵·`r3` 之消費） | 同 `W-G.9-351` 節序 `3` | ⬜ | 規格步 `3` |
| `4` | 規格步 `4` 同歸戶合併（第一趟）：道路五則、公設地併入 | 同 `W-G.9-351` 節序 `4` | ⬜ | 規格步 `4` |
| `5` | 規格步 `5` 末端塊與中間調配池之進入與落位（`K-9-38`〜`40`） | 前置：`K-9-38` 射程 ④、`K-9-40` 射程 ④ 之附圖另呈；受詞之強制抵費地（末）待序 `2` | ⬜ | 規格步 `5` |
| `6` | 規格步 `6` ½ 之判與出口（增配／現金補償·裁定 H、I、L、M） | — | ⬜ | 規格步 `6` |
| `7` | 規格步 `7`／`8` 終態與出艙 | — | ⬜ | 規格步 `7`／`8` |

🔒 **本批之讀法**（發單側之工程裁·⛔ 域裁·已以【通知】呈 KL）：① 各筆單獨試算之受詞 ＝ 入池閘合併**前**之宗（評選於配地之首趟·其後各趟沿用首趟之當選者；當選者嗣後為入池閘合併單元之成員者，移該單元）；② 試算之 `G` 與配地同一解算路徑（`_solve_G_one`）：宗地 ＝ 未臨正街 ∪ 正街段之帶，`G` 公式之 `S` ＝ 正街段之寬（未臨正街⛔ 計臨街）；③ 跨占之門檻 ＝ `1.0 ㎡`（比照街角選位之跨占門檻）、未臨正街之 ε ＝ `1e-3 ㎡`（補丁十 §一）；④ 右端之末端塊對稱實作（鏈起於 FRONT `p2`、首宗向外延伸未臨正街）——本案無右端觸發；⑤ 定案趟之檢：觸發之端之鏈首宗須為當選者，否則停機；選槽（`_select_pool_slot`）以 `pin` 使末端塊恆屬該側之鏈。
🔒 **本案之土地後果**（態 `ed6871a` → 本批·harness·退縮 `3.5 m`／`0 m` 同·唯 `R6`）：`R6` 左端 `R_end` `252.28 ㎡`（未臨正街 `85.71` ＋ 末端帶 `166.57`）；`628-4(1)`（`G008`）當選末端塊：應分配面積 `691.92 → 695.38`、臨正街寬（`G` 公式之 `S`）`14.82 → 12.92 m`（宗地寬度 `14.77 → 12.88`）；`628-21(1)`（`G017`·`628-21`、`628-22`、`628-23` 之入池閘合併單元）改居其次：`433.99 → 433.77`、臨正街寬 `9.18 → 9.30 m`（宗地寬度 `9.15 → 9.27`）；抵費地 `R6-抵費地-1` `1819.35`、`R6-抵費地-2` `85.71` ⇒ `R6-抵費地` `1901.82 ㎡`；`R6` 之 `ΣG` `2071.22 → 2074.46`；`G009` 之 `628-1(2)`（入池閘之入池宗）之應分配面積 `153.19 → 153.11`（仍入池）；`R6` 右側三宗之 `G`／`S` 不變（其二分法之收斂步數隨右鏈之剩餘長度變·形差 ≤ `0.006 ㎡`）；他街廓⛔ 變。
🔒 **依賴序**：序 `1`（本批）→ 序 `2` → 序 `3` → 序 `4` → 序 `5`（其前置之附圖另呈）→ 序 `6` → 序 `7`；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級）。
🔒 **本機介面**：主 checkout 同步後，按「🧮 執行 G 值迭代計算」，成果區於「🧩 調配階段之輸入」之上多「🧱 末端塊之評選」一覽（預設收合）：各無側街之端之觸發與否、`R_end`、跨占者及各筆單獨試算之 `G`、當選者。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `10`（子字串框·含圖例與本列）·列 ＝ `8`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

---

SELF_SHA256: 0caf4f635822991287ca036b81bffd5cbdefb767c7b3d8f711e67f1ace66101d
