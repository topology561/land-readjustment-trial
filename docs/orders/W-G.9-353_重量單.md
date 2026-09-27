# `W-G.9-353`　重量單：末端塊之合併再試與強制抵費地（`K-9-49 ②`·`K-9-36 ③`）之 harness 路徑（側支）＋ 待落地清單之更新

> **發單** ＝ 發單側窗四十九·`2026-09-27`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至側支**）。
> **級** ＝ **重**（生產碼 `3` 檔：`app.py`、`verify/stepg_pipeline.py`、`verify/selection_pipeline.py`；土地後果：**本案⛔**〔合併再試無標的·配地與 `run_all` 改前改後逐位同·`§一` 項 `6`／`9`／`10`〕；他案有——各筆單獨皆未達之末端塊，由停機改為合併再試，仍未達者以 `R_end` 為強制抵費地·`§一` 項 `7`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-353-endmerge`（自開工態起）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D1`／`F12`／`K2`／`P7` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）。
> 🔑 **來源檔一**（檔名逐字 `W-G.9-353_重量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。本批之新檔（`F12`）與改動（`D1`、`K2`、`P7`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：主線 `wip/s1-endpart` 之任何推進；塊 `D1` 以外之生產碼一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿／自誤簿／`GB` 簿之一字（本批⛔ 鑄號）；`K-6` 典與 `CLAUDE.md` 除塊 `K2`／`P7` 之純末端追加外之一字；任何既有側支之刪除或改寫；KL 主 checkout（本批⛔ 同步·主線未動）。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；`git ls-remote --heads origin` 之列數 ＝ `30`，且⛔ 含 `refs/heads/verify/W-G.9-353-endmerge`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 545 545` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`907`** 檔·讀不到 `20`）。發單側窗四十九實跑（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-353`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py 0b05925 W-G.9-353 W-G.9-352 W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-352` | `2`／`8`／`4` | `2`／`8`／`4` | `12` | `4` | `4`／`63` | 🟢 框非恆空 |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `11`／`11` | 🟢 |

**本批⛔ 鑄號**（自誤／`GB`／`VR`／`K-9` 皆⛔）；收工閘 `6`／`7` 以之驗。側支之名 `verify/W-G.9-353-endmerge` 於開工態之遠端⛔ 存（`§零-0` 項 `2`）。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `0b05925`，或施工樹之追蹤檔有變動，或遠端已有 `verify/W-G.9-353-endmerge`，或遠端 heads ≠ `30` |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`F12`／`K2`／`P7` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二前置之任一期不符（尤：`F12` 三子命令之施前 `rc ≠ 1`） |
| `5` | 塊 `D1` 之 `git apply --check` 不過；或施後之三 blob ≠ `§五-1` 項 `6` |
| `6` | 工項二之驗 `V-1`〜`V-5` 任一 ≠ 期（尤：`V-2` 之 `F8 run` 二份改前改後有**任一**異列；`V-5` 之 `run_all` 相異項 ≠ `0`） |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-353-endmerge`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之二檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `8`。

---

## `§一`　態錨（發單側窗四十九自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`30`**；`verify/W-G.9-353-endmerge` ⛔ 存 |
| `2` | 生產碼（開工態 blob） | `app.py` `c99a3701608bb8aa2d218f3ae04e38757124fc24`（`1556424` B）；`verify/stepg_pipeline.py` `b7b5d5ef908078b5ddf9ebd6c951242cc9c3f373`（`121159` B）；`verify/selection_pipeline.py` `17fda1f94e786c413fc4691e247fe2ed26ecbdb0`（`43030` B） |
| `3` | `W-G.9-352` 之復驗 | 發單側窗四十九依交接文四十八 `§四-1` 逐項自倉重跑：逐 `commit` 對拍（單 ＝ `7558e70f…`·`SELF_SHA256` 自驗相符；`F11`／`D1`／`K1`／`G4`／`P6` 與單內塊逐位同；`D1` 施於 `06d0bf3` 得 `c99a3701…`／`b7b5d5ef…` ＝ `e7cfc7b` 之二檔）、三檔之嚴格前綴（`K-6` `404828 → 410740`、`GB` 簿 `1019048 → 1020320`、`CLAUDE.md` `277812 → 282537`）、收工閘 `1`〜`15` 自跑皆符（閘 `7` 四簿同開工態；`wfns_ast` `46`／`46`／`45`）、`F8 run` 二退縮之異列 ＝ 該單 `§一` 項 `9`、`run_all` 二態（`06d0bf3` 對 `e7cfc7b`·同一倉外路徑·`237412 → 236032` B·相異 `9` 項 ＝ 該單 `§一` 項 `10`）、`F11 run` 之數 ＝ 該單 `§一` 項 `6`——**全數相符**；CC 回報之二差異（`run_all` 於 Windows `239414 → 238032` B；`F11` 器內參考值 `148.98` 對實得 `148.99`·器自判在容差內）皆核實、無影響。KL 主 checkout（經 KL 核准之唯讀存取）：`HEAD` → `wip/s1-endpart` ＝ `0b05925…`、`app.py` ＝ `c99a3701…`、追蹤檔無變動；根有 `W-G.9-352_重量單.md`（候 KL 自刪） |
| `4` | 本批之受詞 | `K-9-49 ②`（各筆單獨皆未達者比照街角地合併再試）、`K-9-36 ③`（仍未達 ⇒ `R_end` 為強制抵費地）；補丁十 §一（無勝者 fallback：面積嚴格 ＝ `area(R_end)`）；`K-9-48`（合併再試之機制·`k6b_stage3_run`）；`K-9-49 ③`（先後：街角〔含段三及其後處理〕定案之後；除外 ＝ 已上鎖、已併入或已分配予街角之土地）；依賴序 ＝ `CLAUDE.md`「🔧 待落地清單之更新：末端塊之評選與落位…（`W-G.9-352`）」節序 `2` |
| `5` | 現碼之行為（開工態） | 各筆單獨皆未達之端 ⇒ `end_block_pick` 停機（配地之首趟）；harness 段三之試算（`alloc_state`）遇之 ⇒ 記為 `err` ⇒ `k6b_stage3_run` 停機（停機款 `9`）；合併再試與強制抵費地⛔ 存 |
| `6` | 本案之合併再試（塊 `D1` 施後·harness·`python verify/probes/probe_WG9353_endmerge.py run <repo>`） | 二退縮之合併再試紀錄皆 ＝ `{'退縮': <退縮>, '標的': [], '皆未達': {}}`、逐列 `0`；`R6` 左端仍由 `628-4(1)` 當選 ⇒ **本案不觸發** |
| `7` | 合成案（同器·退縮 `3.5`·注入於器內之 `ns`·⛔ 改檔；假設 `628-4(1)` 跨占街角規定範圍 ⇒ ⛔ 為候選） | 甲 ⇒ 合併再試之 ② 由 `G009` 經道路併入而成，其合併群之 `R1` 片已配地而本段無受併宗 ⇒ **段三之後處理停機**（停機款 `9`·`K-9-48` 七項 `3`／`5`／`6` 之承前缺口·⛔ 靜默）；乙（＋ `628-1(3)` 上鎖）⇒ 逐列 `628(2) ① 未成`、`628-1(2) ① 未成`、`628-23(1) ① 成（免驗）` ⇒ `628-23(1)`（`G017`·併 `628-21(1)`、`628-22(1)`）當選、鏈首宗 `G` `437.18` ＝ 外部錨；丙（再 ＋ `628-21(1)`、`628-22(1)` 上鎖）⇒ 三者皆未成 ⇒ 紀錄 `皆未達 {'R6': ['left']}` ⇒ **強制抵費地** `R6-抵費地-2` `252.28 ㎡` ＝ 外部錨之 `R_end`、宗地與 `R_end` 之交 `0.000000`；丁（`R6` 左端之末端帶以 `13 m` 構之·`R_end` `701.29`）⇒ `628-4(1)` 以 ② 經道路併 `628-4(2)` 而成（驗「不影響原位次」通過）、鏈首宗 `G` `779.93` ＝ 外部錨；乙丙丁三者之 `R6` 宗地聯集 △ 街廓 `0.0000`、兩兩疊 `0.0000` |
| `8` | 施後 blob | `app.py` `0c7739fde995fc77b75d2deccc3a7b78f575c91b`（`1566816` B·增 `161`／刪 `11`）；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`（`121566` B·增 `4`／刪 `0`）；`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`（`47216` B·增 `103`／刪 `34`） |
| `9` | `F8 run`（`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5`／`… 0.0`·工項一之端 對 工項二之 `commit`） | 皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；二退縮之改前改後 `diff` **皆空**（逐位同）——發單側 Linux 實測（工項一之端之替身 對 工項二之替身） |
| `10` | `run_all`（同一倉外路徑·工項一之端 對 工項二之 `commit`） | 二份皆 `64` 項·PASS `28 → 28`／FAIL `36 → 36`；`python verify/probes/probe_WG9343_step0_flag.py runall` ⇒ `rc 0`，**相異項 `0`**（`64` 項之名目、狀態、違規數與本體逐項同）；末端夾具／golden 列 `21／21`·相異 `0`；對帳段「名目：凍存 `22`／現況 `36`」不變；二份 `cmp` 逐位同（各 `236050` B）——發單側 Linux 實測（同一倉外路徑·其 bytes 平台與路徑相依·⛔ 入判） |
| `11` | 畫面對 harness（`python verify/probes/probe_WG9345_screen.py parity <R> <退縮> on <json>`） | 施後：`3.5` ⇒ `rc 0`（配地列 harness `35`／畫面 `34`·不符格 `0`）；`0.0` ⇒ `rc 0`（`36`／`35`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（皆同開工態） |

---

## `§二`　KL 之語與射程

🔒 **所據之既裁**：`K-9-49 ②③`（KL 裁 `2026-09-27`·`16:20`／`16:34`·逐字見 `K-6` 典 `K-9-49` 節）、`K-9-36 ③`（KL `2026-09-17`）、補丁十 §一（`docs/specs/W-G.4_規格v3補丁十_N0-20末端塊fallback定案.md`）、`K-9-48`。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至側支⛔ 須放行；**主線之推進**（本批與次單〔畫面路徑〕同批）**另單·候 KL 逐字放行**。
🔒 **本單之讀法**（發單側之工程裁·⛔ 域裁·以【通知】呈 KL）：
① **時點**（`K-9-49 ③`）：合併再試於街角之段三（含其後處理）之後、配地之前；harness 入口 ＝ `run_corner_pk_k6b` 內、段三（或其不辦）之後恰一次（`run_end_block_merge`）。
② **標的**：以段三後之宗地試算配地（街角選位 ＋ 配地），取其首趟之評選各筆單獨皆未達之端；列 ＝ 各標的之未達候選依原投影序；交 `k6b_stage3_run`（① 同街廓相鄰 → ② 道路及公設地上相鄰·整筆；② 驗「不影響原位次」；後處理同段三）——⛔ 另寫合併之機制。
③ **除外**（`K-9-49 ③`）：段一上鎖 ∪ 街角第 `1` 宗 ∪ 段三已併出者⛔ 併入。
④ **試算與定案**：試算之配地（段三之試算與合併再試之試算·`SS_END_BLOCK_MODE` ＝ `'trial'`）遇各筆單獨皆未達之端 ⇒ 暫以強制抵費地計（⛔ 停機）；定案之配地唯合併再試之紀錄（`SS_END_BLOCK_MERGE`·同一退縮）所載「皆未達」之端得為強制抵費地，否則停機（合併再試未辦 ⇒ ⛔ 以強制抵費地靜默代之）。
⑤ **強制抵費地（末）**：`R_end` 全部（面積嚴格 ＝ `area(R_end)`）；該側之鏈起於 `R_end` 之內側界（∥ 分配線·`end_block_forced_buf`）；`R_end` 以強制帶入池（`end_block_forced_bands`）；其餘各宗依原位次序。
⑥ **競合**（`K-9-49` 射程 ③·⛔ 裁）：二以上標的之候選同屬一合併群（或同一候選跨占二以上 `R_end`）⇒ **停機**，⛔ 推其先後。
⑦ **承前缺口**：合併再試之後處理遇 `K-9-48` 七項 `3`／`5`／`6`（可拆分者之部分併入、剩餘土地之去處）之情形 ⇒ 同段三停機（停機款 `9`·⛔ 靜默）。
⑧ **畫面路徑**：本批⛔ 及（次單·同側支）；畫面遇各筆單獨皆未達之端 ⇒ 仍停機（⛔ 靜默·同開工態）。

🔒 **逐筆清單**：本批動生產碼者恰 **`1`** 筆（工項二·推側支）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `app.py`（新 module 級常數 `SS_END_BLOCK_MODE`／`SS_END_BLOCK_MERGE` 與函式 `end_block_forced_buf`／`end_block_forced_bands`／`end_block_merge_run`；`end_block_side_geom` 回 `buf`；`end_block_pick`／`end_block_apply` 之 `allow_forced`；`end_block_host` 之准否；`end_block_eval_rows`／`end_block_assert_head` 之強制抵費地；`f3_screen_stepg_run` 之二接線；`_WF_NS_NAMES` 增二名）、`verify/stepg_pipeline.py`（harness 之同構二接線）、`verify/selection_pipeline.py`（`_k6b_callbacks` 之抽出與 `alloc_eval`；`run_end_block_merge`；`run_corner_pk_k6b` 於段三之後呼叫之） | 塊 `D1` | 本案⛔（`§一` 項 `6`／`9`／`10`）；他案有（`§一` 項 `7`） |

🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至側支 `verify/W-G.9-353-endmerge`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及其他任何生產碼、任何他錨；`(d)` ⛔ 建畫面路徑之合併再試、`K-9-48` 七項 `3`／`5`／`6`、強制抵費地作調配池（`K-9-38`〜`40`）、調配之任何後步——另單。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（側支·零生產碼）

`docs/orders/W-G.9-353_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-353 工項零：本單原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-353-endmerge`（新建側支）；推後 `git ls-remote --heads origin` 之列數 ＝ `31`、主線仍 ＝ `0b05925…`。

### 工項一　量測器 `F12` 入倉（側支·零生產碼）

塊 `F12` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9353_endmerge.py`（**新檔**）。`commit` 訊息逐字 `W-G.9-353 工項一：量測器 F12（末端塊之合併再試與強制抵費地）入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

### 工項二　塊 `D1`：末端塊之合併再試與強制抵費地之 harness 路徑（🔴 生產碼·一 `commit`·推側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9353_endmerge.py selftest <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
2. `python verify/probes/probe_WG9353_endmerge.py wiring <repo>` ⇒ **`rc 1`**（`W1`〜`W7` 皆紅；突變 `N1`〜`N4` 皆「突變錨不存在」）。
3. `python verify/probes/probe_WG9353_endmerge.py run <repo>` ⇒ **`rc 1`**（末列 `⇒ 紅 ['受詞缺']；rc 1`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D1` 依圍欄之逐列索引抽出為 `<O>\D1.diff`、對拍 `§五-1` 後，`git apply --check <O>\D1.diff` ⇒ 過；`git apply <O>\D1.diff`；`git hash-object app.py` ＝ `0c7739fde995fc77b75d2deccc3a7b78f575c91b`、`git hash-object verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`、`git hash-object verify/selection_pipeline.py` ＝ `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-353 工項二：末端塊之合併再試與強制抵費地（K-9-49 ②·K-9-36 ③）之 harness 路徑 🔴 生產碼（側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9353_endmerge.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `S1`〜`S10i`（含 `S1b`／`S7b`／`S9a`〜`S9e`／`S10a`〜`S10i`）皆 ✅、`M0` ✅、`M1`〜`M8` 皆「轉紅」；`wiring` 之 `W1`〜`W7` 皆 ✅，`N1`〜`N4` 皆「轉紅」 |
| `V-2` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `diff` | 皆 **`rc 0`**、末列 `⇒ 紅 []；rc 0`；**二份之 `diff` 皆空**（`§一` 項 `9`） |
| `V-3` | `python verify/probes/probe_WG9353_endmerge.py run <repo>` | **`rc 0`**；末列 `⇒ 紅 []；rc 0`；`R1` 二退縮、`X1`〜`X4` 皆 ✅，其數 ＝ `§一` 項 `6`／`7` |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35.json`；同 `0.0`；`python verify/probes/probe_WG9348_harvest_key.py <repo>`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>`；`python verify/probes/probe_WG9340_main_synth.py <repo>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9350_frontroad.py selftest <repo>`；`… wiring <repo>`；`… run <repo>`；`python verify/probes/probe_WG9351_intake.py selftest <repo>`；`… wiring <repo>`；`… run <repo>`；`python verify/probes/probe_WG9352_endblock.py selftest <repo>`；`… wiring <repo>`；`… run <repo>` | 皆 **`rc 0`**；`parity` ＝ `§一` 項 `11`；`wfns_ast` **`48`／`48`／`47`**（開工態 `46`／`46`／`45`·增 `end_block_forced_buf`／`end_block_forced_bands`）；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F10 run`、`F11 run` 之出艙與前置之端（工項一之端）逐字同 |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**（`64` 項之名目、狀態、違規數與本體逐項同）；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（驗皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-353-endmerge`。

### 工項三　`K-9-49 ②`·`K-9-36 ③` 之落地狀態 ＋ 待落地清單之更新（側支·零生產碼·一 `commit`）

塊 `K2`、`P7` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位各**附於**下列二檔之末：`K2` → `docs/rulings/K-6_街角地分配程序與可分配判準.md`；`P7` → `CLAUDE.md`。二檔之刪除欄皆 `0`、改前全檔皆為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-353 工項三：K-9-49 ②·K-9-36 ③ 之落地狀態 ＋ 待落地清單之更新（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

### 工項四　執行報告入倉（側支·新檔 `docs/reports/W-G.9-353R_末端塊之合併再試與強制抵費地_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`11` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F12` 三子命令之全文、`F8 run` 二份之 `diff` 之結果、`parity` 二份之 `rc` 與末三列、`runall` 對拍之全文與 `diff` 之結果）；④ 四塊之實得（bytes／`sha256`）與二檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`（主線仍 `0b05925…`）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-353 工項四：執行報告入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-353-endmerge`。

---

## `§四`　收工閘（工項四之 `commit` 推後·於側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項二 ＝ `app.py` 增 `161`／刪 `11`、`verify/stepg_pipeline.py` 增 `4`／刪 `0`、`verify/selection_pipeline.py` 增 `103`／刪 `34`；其餘逐檔 **`0`** |
| `2` | 生產碼 `34` 檔對 `0b05925` | 相異恰 **`3`**（`app.py` ＝ `0c7739fde995fc77b75d2deccc3a7b78f575c91b`、`verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`、`verify/selection_pipeline.py` ＝ `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`8` 檔：本單、`F12`、`app.py`、`verify/stepg_pipeline.py`、`verify/selection_pipeline.py`、`K-6`、`CLAUDE.md`、報告） |
| `4` | 二檔之 bytes | `K-6` `410740 → 412870`、`CLAUDE.md` `282537 → 286590`；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`31`**；主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`（⛔ 變）；`verify/W-G.9-353-endmerge` ＝ 工項四之 `commit`；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 545 545 .` | **`rc 0`**（自誤 `MAX` 仍 `545`） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 545 545` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `530`／`MAX` `545`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `186`／`193`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `46`／`49`／`[44, 47]`（皆同開工態） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`48`／`48`／`47`**（開工態 `46`／`46`／`45`·增 `end_block_forced_buf`／`end_block_forced_bands`） |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9351_intake.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `15` | `python verify/probes/probe_WG9352_endblock.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `16` | `python verify/probes/probe_WG9353_endmerge.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之替身 ＋ 塊 `F12` ＋ 塊 `D1` ＋ 塊 `K2`／`P7` ＋ 報告之替身·五 `commit`）並實跑閘 `1`〜`4`、`6`〜`16` ⇒ 見 `§五-1` 項 `9`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D1` | `32497` B·`sha256` `137e96ed5d3a681531c630624f4e5d800064292e896ec907764c47c588202957`·`499` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F12` | `41852` B·`sha256` `033eca6e073dea622907533cb39ff1ebf18969cd62a6448353a1386a2817bf36`·`769` 列（圍欄內全文·末附換行） |
| `4` | 塊 `K2` | `2130` B·`sha256` `29d8e7862a37b52e9ed7a3e5abcd4c3dac84b053743a1a004d3b5e1332be5626`·`20` 列；附於 `K-6`（`410740` B）之末後，期末 ＝ `412870` B |
| `5` | 塊 `P7` | `4053` B·`sha256` `cc6d0a2f0ad048d687c94ac322e8aa67554389d0b27349cd84ac99a0faa5aae8`·`23` 列；附於 `CLAUDE.md`（`282537` B）之末後，期末 ＝ `286590` B |
| `6` | 施 `D1` 後之 blob | `app.py` `0c7739fde995fc77b75d2deccc3a7b78f575c91b`（`1566816` B）；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`（`121566` B）；`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`（`47216` B）（開工態 `c99a3701…`／`b7b5d5ef…`／`17fda1f9…`） |
| `7` | `F12` 之二態 | 開工態（工項一之端）`selftest`／`wiring`／`run` 皆 `rc 1`；施 `D1` 後皆 `rc 0` |
| `8` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十九實跑（態 `0b05925`）：🔴 機械 `0` 項／🟡 提示 `9` 項——`P-1` `:111`（工項二前置之段·所觸之字樣係前置 `2` 所引 `F12 wiring` 施前出艙之「突變錨不存在」及「⛔ `commit`」之用語，⛔ 全稱否定 ⇒ **具名豁免**）、`P-1` `:175`（本表·項 `8`／`9` 二格所引之預檢用語與收工閘模擬之述 ⇒ **具名豁免**）、`P-1` `:1034`／`:1168`（塊 `F12` 之碼·所觸之字樣係該器自身之出艙文字 ⇒ **具名豁免**）、`P-4` `:77`（`§二` 所據之既裁·所觸係「逐字見 `K-6` 典某節」之出處指引，⛔ 方向性轉引 ⇒ **具名豁免**）、`P-4` `:124`／`:148`（工項二之驗、`§四` 收工閘之表頭·其箭頭之座標系皆為「改前〔工項一之端／`0b05925`〕至改後〔工項二之 `commit`／工項四之端〕」，表內自載 ⇒ **具名豁免**）、`P-4` `:138`（工項三之段·其 `→` 係「塊 → 所附之檔」之對應、⛔ 方向性轉引 ⇒ **具名豁免**）、`P-4` `:391`（塊 `D1` 之碼·所觸者係生產碼之 docstring ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `19047`–`26704`）⇒ `rc 0` |
| `9` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`0b05925` ＋ 五 `commit`：本單之前稿〔僅 `§一` 項 `9`〜`11`、`V-4` 與閘 `8` 之 `wfns_ast`、本表項 `8`／`9` 未填〕＋ 塊 `F12` ＋ 塊 `D1`〔自前稿依抽取式抽出·`git apply` 過·施後三 blob ＝ 項 `6`〕＋ 塊 `K2`／`P7` ＋ 報告之替身）：閘 `1` 工項二 `app.py` 增 `161`／刪 `11`、`verify/stepg_pipeline.py` 增 `4`／刪 `0`、`verify/selection_pipeline.py` 增 `103`／刪 `34`，餘逐檔刪 `0`；閘 `2` 相異恰 `3`（`34` 檔）；閘 `3` `CR` 合計 `0`（`8` 檔·判別力 `12308`）；閘 `4` `410740 → 412870`、`282537 → 286590`（皆嚴格前綴）；閘 `6`〜`16` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `48`／`48`／`47`；「app 側宿主 ＝ f3_screen_stepg_run」；`F8` 二子命令、`F9`／`F10`／`F11`／`F12` 各三子命令之末列 `⇒ 紅 []；rc 0`；`F12 run` 約 `920` 秒）；另 `V-2`（`F8 run` 二退縮改前改後 `diff` 皆空）、`V-4`（`parity` 二退縮；`F10 run`／`F11 run` 與工項一之端逐字同）、`V-5`（`run_all` 二態 `cmp` 逐位同·相異 `0`）皆符；模擬之二 worktree 跑畢追蹤檔之變動 `0`（`run_all` 之拋棄式 worktree 另計）；工項一之端 `F12` 三子命令皆 `rc 1`（`selftest`／`run` 末列 `⇒ 紅 ['受詞缺']；rc 1`；`wiring` `W1`〜`W7`、`N1`〜`N4` 皆紅） |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 側支 `verify/W-G.9-353-endmerge`（工項二於驗皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D1`（`git apply` 之差異·`app.py` ＋ `verify/stepg_pipeline.py` ＋ `verify/selection_pipeline.py`）

````diff
diff --git a/app.py b/app.py
index c99a370..0c7739f 100644
--- a/app.py
+++ b/app.py
@@ -10499,10 +10499,19 @@ def _end_region_R(block_poly, cad_alloc, end_pt, min_width, frag_poly, _label=''
 #  皆未達 ⇒ 🔴 停機：合併再試（`K-9-49 ②`）與強制抵費地（`K-9-36 ③`）候次單（⛔ 靜默）。
 #  先後（`K-9-49 ③`）：本評選於配地之首趟為之——街角（含段三及其後處理）皆已定案；入池閘之試算趟與末趟
 #    沿用首趟之當選者（`SS_END_BLOCK_EVAL`），故「各筆單獨」之受詞 ＝ 入池閘合併前之宗。
+#  🆕 `W-G.9-353`（`K-9-49 ②`·`K-9-36 ③`）：上開「皆未達 ⇒ 停機」改為——
+#    ① 試算（`SS_END_BLOCK_MODE` ＝ `'trial'`：街角合併再試與末端塊合併再試所跑之配地）⇒ 暫以強制抵費地計；
+#    ② 定案（無 `'trial'`）⇒ 唯 `SS_END_BLOCK_MERGE` 載該端「合併再試皆未達」者以強制抵費地計，否則仍停機
+#      （合併再試未辦 ⇒ ⛔ 以強制抵費地靜默代之）。
+#    強制抵費地（末）＝ `R_end` 全部（面積嚴格 ＝ area(R_end)·補丁十 §一）：該側之鏈起於 `R_end` 之內側界
+#    （`end_block_forced_buf`），`R_end` 以強制帶入池（`end_block_forced_bands`）；其餘各宗依原位次序。
+#    合併再試 ＝ `end_block_merge_run`（段三之後·比照 `K-9-48`·單一真相源 `k6b_stage3_run`）。
 # ══════════════════════════════════════════════════════════════════════════
 END_BLOCK_UNFRONT_EPS = 1e-3        # ㎡·補丁十 §一 之 ε
 END_BLOCK_CROSS_MIN_AREA = 1.0      # ㎡·跨占之門檻（比照街角選位之跨占門檻）
 SS_END_BLOCK_EVAL = 'f3_end_block_eval'
+SS_END_BLOCK_MODE = 'f3_end_block_mode'      # 🆕 `W-G.9-353`：`'trial'` ⇒ 皆未達者暫以強制抵費地計
+SS_END_BLOCK_MERGE = 'f3_end_block_merge'    # 🆕 `W-G.9-353`：合併再試之紀錄 `{'標的': [...], '皆未達': {街廓: [端…]}}`
 
 
 def end_block_side_geom(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
@@ -10540,13 +10549,22 @@ def end_block_side_geom(block_poly, d_hat, corner_pt, front_p2, cad_alloc, alloc
         return {'gate': False, 'unfront': _unf}
     _band, _r_end, _a = _end_region_R(block_poly, cad_alloc, _end_pt, min_width, _unf_poly,
                                       _label=f"{_label}·{side}")
+    # 🆕 `W-G.9-353`：強制抵費地（末）之鏈起點——`R_end` 之內側界（∥ 分配線）於 s 軸之位置；
+    #   `buf` ＝ 該側之鏈須先讓出之 s 長（左 ＝ s_hi(R_end)；右 ＝ s(p2) − s_lo(R_end)）。
+    _rr = _strip_s_range(_r_end, d_hat, corner_pt, allocation_dir)
+    if _rr is None:
+        raise RuntimeError(f"🔴 end_block_side_geom[{_label}·{side}]：R_end 之 s 域不可定義")
+    _buf = float(_rr[1]) if side == 'left' else float(_sp2 - float(_rr[0]))
+    if not (_buf > 0.0):
+        raise RuntimeError(f"🔴 end_block_side_geom[{_label}·{side}]：R_end 之內側界未入街廓（buf={_buf!r}）")
     return {'gate': True, 'unfront': _unf, 's_back': float(_w), 'r_end': _r_end,
-            'r_end_area': float(_a), 'band_area': float(_band.area)}
+            'r_end_area': float(_a), 'band_area': float(_band.area), 'buf': _buf}
 
 
-def end_block_pick(side, geom, entries, corner_range_polys, trial, _label=''):
+def end_block_pick(side, geom, entries, corner_range_polys, trial, _label='', allow_forced=False):
     """評選（純函式·`trial(tp) -> (G, 臨正街寬)` 由呼叫端供）。`entries` ＝ 自該端起之原位次序列之宗。
-    回 `{'winner': 暫編地號, 'rows': [...]}`；皆未達 ⇒ 🔴 停機。"""
+    回 `{'winner': 暫編地號, 'rows': [...]}`；皆未達 ⇒ `allow_forced` 為真者回 `{'winner': None, 'rows': [...]}`
+    （強制抵費地·`W-G.9-353`），否則 🔴 停機。"""
     from shapely.geometry import Polygon as _P_eb
     _r_end = geom['r_end']
     _thr = float(geom['r_end_area'])
@@ -10576,9 +10594,11 @@ def end_block_pick(side, geom, entries, corner_range_polys, trial, _label=''):
         rows.append(_row)
         if _ok:
             return {'winner': _k, 'rows': rows}
+    if allow_forced:
+        return {'winner': None, 'rows': rows}
     raise RuntimeError(
         f"🔴 [末端塊·{_label}·{side}] 跨占 R_end（{_thr:.2f} ㎡）者各筆單獨試算皆未達：{rows}"
-        "——合併再試（K-9-49 ②）與強制抵費地（K-9-36 ③）候次單（⛔ 靜默）")
+        "——合併再試（K-9-49 ②）未辦或未載皆未達（⛔ 以強制抵費地靜默代之）")
 
 
 def end_block_pin(ordered, side, pid, _label=''):
@@ -10603,10 +10623,12 @@ def end_block_pin(ordered, side, pid, _label=''):
 
 def end_block_apply(ordered, *, blk_label, block_poly, d_hat, corner_pt, front_p2, cad_alloc,
                     allocation_dir, min_width, has_side_pk, has_side_cad, corner_range_polys,
-                    trial, cache):
+                    trial, cache, allow_forced=None):
     """一街廓之末端塊：評選（首趟）或沿用（`cache` 已有本街廓）＋ 落位。
     `trial(tp, side, s_back) -> (G, 臨正街寬)`；`cache` ＝ `SS_END_BLOCK_EVAL` 之 dict（就地寫）。
-    回 `(ordered′, {'left': {'s_back','winner'}|None, 'right': …})`。"""
+    🆕 `W-G.9-353`：`allow_forced(side) -> bool`（缺 ⇒ 恆偽）——各筆單獨皆未達者，真 ⇒ 強制抵費地（末）
+    （⛔ 落位·紀錄 `當選` ＝ `None`、`強制抵費地` ＝ 真），偽 ⇒ 停機。
+    回 `(ordered′, {'left': {'s_back','winner','forced','buf','r_end'}|None, 'right': …})`。"""
     _info = {'left': None, 'right': None}
     _cached = cache.get(blk_label)
     _rec = {}
@@ -10624,29 +10646,55 @@ def end_block_apply(ordered, *, blk_label, block_poly, d_hat, corner_pt, front_p
         if not _g['gate']:
             _rec[_sd] = {'觸發': False, '未臨正街(㎡)': round(float(_g['unfront']), 4)}
             continue
+        _allow = bool(allow_forced(_sd)) if allow_forced is not None else False
         if _cached is not None:
             _c = _cached.get(_sd) or {}
             if not _c.get('觸發'):
                 raise RuntimeError(f"🔴 end_block_apply[{blk_label}·{_sd}]：首趟未觸發而本趟觸發")
             _win = _c['當選']
+            if _win is None and not _allow:
+                raise RuntimeError(
+                    f"🔴 end_block_apply[{blk_label}·{_sd}]：首趟為強制抵費地而本趟不准（⛔ 靜默沿用）")
             _rec[_sd] = _c
         else:
             _seq = _out if _sd == 'left' else list(reversed(_out))
             _pk_res = end_block_pick(_sd, _g, _seq, corner_range_polys,
                                      (lambda tp, _s=_sd, _w=_g['s_back']: trial(tp, _s, _w)),
-                                     _label=blk_label)
+                                     _label=blk_label, allow_forced=_allow)
             _win = _pk_res['winner']
             _rec[_sd] = {'觸發': True, '未臨正街(㎡)': round(float(_g['unfront']), 2),
                          '末端帶(㎡)': round(float(_g['band_area']), 2),
                          'R_end(㎡)': round(float(_g['r_end_area']), 2),
                          '候選': _pk_res['rows'], '當選': _win}
-        _out = end_block_pin(_out, _sd, _win, _label=blk_label)
-        _info[_sd] = {'s_back': float(_g['s_back']), 'winner': _win}
+            if _win is None:
+                _rec[_sd]['強制抵費地'] = True
+        if _win is not None:
+            _out = end_block_pin(_out, _sd, _win, _label=blk_label)
+        _info[_sd] = {'s_back': float(_g['s_back']), 'winner': _win, 'forced': _win is None,
+                      'buf': float(_g['buf']), 'r_end': _g['r_end']}
     if _cached is None:
         cache[blk_label] = _rec
     return _out, _info
 
 
+def end_block_forced_buf(eb_info, side):
+    """🆕 `W-G.9-353`：強制抵費地（末）之該側鏈須先讓出之 s 長；非強制 ⇒ `0.0`（二宿主之單一真相源）。"""
+    _i = (eb_info or {}).get(side)
+    if not _i or not _i.get('forced'):
+        return 0.0
+    return float(_i['buf'])
+
+
+def end_block_forced_bands(eb_info):
+    """🆕 `W-G.9-353`：強制抵費地（末）之 `R_end` 多邊形（入池之強制帶·二宿主之單一真相源）。"""
+    _out = []
+    for _sd in ('left', 'right'):
+        _i = (eb_info or {}).get(_sd)
+        if _i and _i.get('forced'):
+            _out.append(_i['r_end'])
+    return _out
+
+
 def end_block_host(ordered, *, blk_label, blk_poly, d_hat, corner_pt, front_p2, alloc_dir_cad,
                    allocation_dir, session, corner_range_polys, solve_one, l_front, avg_depth,
                    S_block_max, post_price, pre_price_by_zone):
@@ -10661,6 +10709,15 @@ def end_block_host(ordered, *, blk_label, blk_poly, d_hat, corner_pt, front_p2,
     _has_pk = ({_sd: bool(_fo.get(f'{_sd}_has_side')) for _sd in ('left', 'right')}
                if ('left_has_side' in _fo and 'right_has_side' in _fo) else dict(_has_cad))
     _cache = session.setdefault(SS_END_BLOCK_EVAL, {})
+    # 🆕 `W-G.9-353`：強制抵費地（末）之准否——試算 ⇒ 恆准；定案 ⇒ 唯合併再試之紀錄（同一退縮）載該端皆未達者准。
+    _mode = session.get(SS_END_BLOCK_MODE)
+    _mrec = session.get(SS_END_BLOCK_MERGE) or {}
+    _msb, _ssb = _mrec.get('退縮'), session.get('f3L_setback_default')
+    _mfail = (((_mrec.get('皆未達') or {}).get(blk_label) or [])
+              if (_msb is not None and _ssb is not None and abs(float(_msb) - float(_ssb)) < 1e-9) else [])
+
+    def _allow(side):
+        return _mode == 'trial' or side in _mfail
     _d = np.asarray(d_hat, dtype=float)
     _cp = np.asarray(corner_pt, dtype=float)
 
@@ -10686,7 +10743,7 @@ def end_block_host(ordered, *, blk_label, blk_poly, d_hat, corner_pt, front_p2,
                            corner_pt=corner_pt, front_p2=front_p2, cad_alloc=alloc_dir_cad,
                            allocation_dir=allocation_dir, min_width=_mw, has_side_pk=_has_pk,
                            has_side_cad=_has_cad, corner_range_polys=corner_range_polys,
-                           trial=_trial, cache=_cache)
+                           trial=_trial, cache=_cache, allow_forced=_allow)
 
 
 def end_block_eval_rows(ev):
@@ -10702,7 +10759,9 @@ def end_block_eval_rows(ev):
                 lines.append(f"{_blk} {_nm[_sd]}端（無側街）：未臨正街 {_r.get('未臨正街(㎡)')} ㎡ ⇒ 未觸發")
                 continue
             lines.append(f"{_blk} {_nm[_sd]}端（無側街）：未臨正街 {_r['未臨正街(㎡)']} ＋ 末端帶 {_r['末端帶(㎡)']}"
-                         f" ＝ R_end {_r['R_end(㎡)']} ㎡；當選 {_r['當選']}")
+                         f" ＝ R_end {_r['R_end(㎡)']} ㎡；"
+                         + (f"當選 {_r['當選']}" if _r.get('當選') is not None
+                            else "各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）"))
             for _c in (_r.get('候選') or []):
                 rows.append({'街廓': _blk, '端': _nm[_sd],
                              **{_k: ('—' if _v is None else str(_v)) for _k, _v in _c.items()}})
@@ -10715,6 +10774,13 @@ def end_block_assert_head(blk_label, eb_info, left_results, right_results):
         _i = (eb_info or {}).get(_sd)
         if _i is None:
             continue
+        if _i.get('winner') is None:
+            # 🆕 `W-G.9-353`：強制抵費地（末）⇒ 該側之鏈⛔ 得有末端塊之宗（`R_end` 無人承受·由強制帶入池）
+            _bad = [_e['tp'].get('暫編地號') for _e, _r in (_res or []) if _e.get('is_end_block')]
+            if _bad:
+                raise RuntimeError(
+                    f"🔴 [末端塊·{blk_label}·{_sd}] 強制抵費地之側有末端塊之宗 {_bad}（⛔ 一地二用）")
+            continue
         if not _res or not _res[0][0].get('is_end_block'):
             _hd = (_res[0][0]['tp'].get('暫編地號') if _res else None)
             raise RuntimeError(
@@ -10722,6 +10788,84 @@ def end_block_assert_head(blk_label, eb_info, left_results, right_results):
                 "（未臨正街將無人承受·⛔ 靜默成池）")
 
 
+def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lots, blocks, centerlines,
+                        a_prime, alloc_eval, alloc_state, *, setback=None, log_print=print):
+    """🆕 `W-G.9-353`：末端塊之合併再試（`K-9-49 ②`·比照 `K-9-48`·單一真相源 `k6b_stage3_run`）。
+
+    時點（`K-9-49 ③`）：街角之段三（含其後處理）之後、配地之前。
+    參數
+      alloc_eval   `alloc_eval(temp, build) -> {街廓: {端: 評選紀錄}}`：以所給之宗地跑街角選位與配地
+                   （試算·`SS_END_BLOCK_MODE` ＝ `'trial'`），回配地首趟之末端塊評選（`SS_END_BLOCK_EVAL`）；
+                   配地中止 ⇒ `raise RuntimeError`。
+      alloc_state  ／`a_prime`／`blocks`／`centerlines` ＝ 同 `k6b_stage3_run`（其 `alloc_state` 亦須為試算）。
+      locked       段一上鎖集；`corner_lots` ＝ 街角第 1 宗之暫編地號集。
+    流程
+      ① 以現宗地試算一次，取「各筆單獨皆未達」之端（標的）；無 ⇒ 逕回（同一物件）；試算中止 ⇒ 逕回並記其由
+         （定案之配地將遇同一中止，或於標的之端因無紀錄而停機·⛔ 靜默）。
+      ② 競合（⛔ 裁·`K-9-49` 射程 ③）：二以上標的之候選同屬一合併群 ⇒ 🔴 停機。
+      ③ 各標的之未達候選依原投影序為列，交 `k6b_stage3_run`（① 同街廓相鄰 → ② 道路及公設地上相鄰·整筆；
+         ② 驗「不影響原位次」；後處理同段三）；併入之除外 ＝ `locked` ∪ `corner_lots` ∪ 段三已併出者
+         （`K-9-49 ③`：已上鎖、已併入或已分配予街角之土地⛔ 再併入末端塊）。
+      ④ 未成之標的 ⇒ 記「皆未達」（定案之配地據以強制抵費地·`K-9-36 ③`）。
+    回 `(temp_out, build_out, log, rec)`；`rec` ＝ `{'退縮': setback, '標的': [[街廓, 端]…],
+    '皆未達': {街廓: [端…]}}`（試算中止 ⇒ `'標的'` ＝ `None`、另載 `'試算中止'`）。"""
+    _rec = {'退縮': setback, '標的': [], '皆未達': {}}
+    try:
+        _ev = alloc_eval(temp_parcels, build_parcels) or {}
+    except RuntimeError as _e:
+        _rec['標的'] = None
+        _rec['試算中止'] = str(_e).split("\n")[0][:300]
+        return temp_parcels, build_parcels, [], _rec
+    _tg = []
+    for _blk in sorted(_ev):
+        for _sd in ('left', 'right'):
+            _r = (_ev.get(_blk) or {}).get(_sd) or {}
+            if _r.get('觸發') and _r.get('當選') is None:
+                _tg.append((_blk, _sd))
+    _rec['標的'] = [[_b, _s] for _b, _s in _tg]
+    if not _tg:
+        return temp_parcels, build_parcels, [], _rec
+    _END = {'left': '左', 'right': '右'}
+    _SIDE = {'左': 'left', '右': 'right'}
+    _rows, _cand_of = [], {}
+    for _blk, _sd in _tg:
+        for _c in (_ev[_blk][_sd].get('候選') or []):
+            if _c.get('結果') != '未達':
+                continue
+            _rows.append({'最終序位': len(_rows) + 1, '街廓': _blk, '端': _END[_sd],
+                          '暫編地號': _c['暫編地號']})
+            _cand_of.setdefault(_c['暫編地號'], set()).add((_blk, _sd))
+    from shapely.geometry import Polygon as _Pg_ebm
+    _pk = [{'原地號': t.get('原地號', ''),
+            'polygon': (_Pg_ebm(t['polygon_coords']) if len(t.get('polygon_coords') or []) >= 3 else None)}
+           for t in temp_parcels]
+    _dup = {p: tg for p, tg in _cand_of.items() if len(tg) >= 2}
+    if _dup:
+        raise RuntimeError(f"🔴 [末端塊合併再試] 候選 {sorted(_dup)} 同時跨占二以上末端塊之 R_end——"
+                           "數末端塊之競合（⛔ 裁·K-9-49 射程 ③）")
+    for _g in k6_merge_groups(_pk, own_map):
+        _ids = sorted(temp_parcels[i]['暫編地號'] for i in _g)
+        _hit = sorted({x for p in _ids for x in _cand_of.get(p, ())})
+        if len(_hit) >= 2:
+            raise RuntimeError(f"🔴 [末端塊合併再試] 同一合併群 {_ids} 之候選分屬 {len(_hit)} 個末端塊 {_hit}——"
+                               "數末端塊之競合（⛔ 裁·K-9-49 射程 ③）")
+    _L = (set(locked or ()) | set(corner_lots or ())
+          | {t['暫編地號'] for t in temp_parcels if t.get('段三併出')})
+
+    def _trial(temp, build, blk, end, cand):
+        _e = ((alloc_eval(temp, build) or {}).get(blk) or {}).get(_SIDE[end]) or {}
+        _row = next((r for r in (_e.get('候選') or []) if r.get('暫編地號') == cand), None)
+        return _e.get('當選'), (_row or {}).get('試算G(㎡)'), _e.get('R_end(㎡)')
+
+    _temp2, _build2, _log = k6b_stage3_run(_rows, _L, own_map, temp_parcels, build_parcels, blocks,
+                                           centerlines, a_prime, _trial, alloc_state, log_print=log_print)
+    _won = {(r['街廓'], r['端']) for r in _log if r.get('結果') == '成' and r.get('序') != '後處理'}
+    for _blk, _sd in _tg:
+        if (_blk, _END[_sd]) not in _won:
+            _rec['皆未達'].setdefault(_blk, []).append(_sd)
+    return _temp2, _build2, _log, _rec
+
+
 def solve_G_binary(a: float, A: float, B: float, C: float,
                    l_front: float, l_side: float, F: float,
                    block_poly, d_hat, baseline_pt,
@@ -15948,6 +16092,8 @@ _WF_NS_NAMES = [
     "k929_6_enabled", "k929_6_fixpoint", "K917_DROPPED",
     # 🆕 `W-G.9-352`：末端塊之三名（引擎 `verify/stepg_pipeline.py` 經 `ns` 消費）。
     "end_block_host", "end_block_assert_head", "SS_END_BLOCK_EVAL",
+    # 🆕 `W-G.9-353`：強制抵費地（末）之二名（引擎 `verify/stepg_pipeline.py` 經 `ns` 消費）。
+    "end_block_forced_buf", "end_block_forced_bands",
     # 🆕 B-5（plan v3 §四·D-3 寬度制）：平移切帶範圍多邊形**即算即用**之單一真相源。
     #   ⚠️ 走 ns 函式、**不**存 session 新鍵——session 資料走 `_WFSessionShim`，
     #      且 harness（run_verification）從不算負擔範圍，存鍵在 harness 路徑必缺。
@@ -17678,6 +17824,9 @@ def f3_screen_stepg_run(st, *,
             # 🆕 Phase C：若左側 forced_offset → 從 buffer 寬度起算（跳過街角）
             left_cum_S = float(_left_buffer_S)
             right_cum_S = float(_right_buffer_S)   # 同理右側
+            # 🆕 `W-G.9-353`：強制抵費地（末）⇒ 該側之鏈起於 `R_end` 之內側界（單一真相源·harness 同構）
+            left_cum_S += end_block_forced_buf(_eb_info, 'left')
+            right_cum_S += end_block_forced_buf(_eb_info, 'right')
             # 🆕 W-C §4：thread 累積 W_前（首筆=0；forced_offset 時=buffer 臨街寬）
             _W_prev_left = 0.0
             _W_prev_right = 0.0
@@ -18239,6 +18388,7 @@ def f3_screen_stepg_run(st, *,
                                                    far_line_dir=_fd)
                         if _gb is not None and not _gb.is_empty:
                             _fb_p2.append(_gb)
+                _fb_p2.extend(end_block_forced_bands(_eb_info))   # 🆕 `W-G.9-353`：強制抵費地（末）之 `R_end`
                 offset_geoms = _pool_strips_for_block(
                     blk_poly, d_hat, corner_pt, allocation_dir_block,
                     allocated_polys, _label=blk_label, _depth=avg_depth_default,
diff --git a/verify/selection_pipeline.py b/verify/selection_pipeline.py
index 17fda1f..8bb4592 100644
--- a/verify/selection_pipeline.py
+++ b/verify/selection_pipeline.py
@@ -643,40 +643,22 @@ def k6b_f4_ctx(ctx_by_tag, build_pre_by_tag):
     return {t: dict(c, build=build_pre_by_tag[t]) for t, c in ctx_by_tag.items()}
 
 
-def run_corner_pk_k6b(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback,
-                      *, snapshot):
-    """`W-G.9-344`：段三之 harness 入口。回傳七元組
-    `(診斷rows, 指配rows, 抵費地rows, winners, forced, temp_parcels_out, build_parcels_out)`。
-
-    1. 先跑 `run_corner_pk`（同參數）。
-    2. `k6b_stage3_enabled()` 為偽、或段二序（`ss['f3_k6b_stage2_order']`）為空 ⇒ 逕回其五值 ＋
-       原 `temp_parcels`／`build_parcels`（**同一物件**），`ss['f3_k6b_stage3_log'] ＝ []`。
-    3. 否則注入 `a_prime`／`trial_winner`／`alloc_state`（皆於深拷貝上試算）呼叫 `ns["k6b_stage3_run"]`，
-       其後以回傳之宗地再跑一次 `run_corner_pk`，回傳其五值 ＋ 段三後之宗地。
-    4. `ss['f3_k6b_stage3_log']` ＝ 紀錄；`ss['f3_k6b_stage3_order_used']` ＝ 所用之段二序。
-    5. 試算之副作用隔離：試算前深拷貝 `session_state` 與 `ns["K917_DROPPED"]`，段三畢（含例外）
-       於 `finally` 原地回復；最終重跑之 `run_corner_pk` 覆蓋 PK 諸鍵。
-       ⚠️ `stepg_pipeline._V3_FINANCE`（模組全域）亦被試算之 `run_step_g` 改寫——其值只依
-       `snapshot`／`cb`／`cad`（⛔ 依宗地），與最終之 `run_step_g` 所寫者同值 ⇒ ⛔ 回復（具名）。
-    """
+def _k6b_callbacks(ns, fake_st, cb, cad, param_rows, setback, snapshot):
+    """`W-G.9-344`／🆕 `W-G.9-353`：段三與末端塊合併再試所注入之試算回呼（原位於 `run_corner_pk_k6b` 內·
+    抽出以供二者共用；本體唯 `_p_of` 之快照查找改於呼叫時為之〔段三不辦時亦須建回呼·⛔ 預取〕，餘逐字未改）。
+    回 `{'a_prime', 'trial_winner', 'alloc_state', 'alloc_eval'}`。
+    🆕 `W-G.9-353`：`alloc_state`／`alloc_eval` 之配地一律為**試算**（`SS_END_BLOCK_MODE` ＝ `'trial'`·
+    各筆單獨皆未達之末端塊暫以強制抵費地計）；呼叫端須於其外層深拷貝並回復 `session_state`。"""
     import copy as _cp
     import contextlib as _cl
     import io as _io
-    ss = fake_st.session_state
-    res = run_corner_pk(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback,
-                        snapshot=snapshot)
-    order = list(ss.get('f3_k6b_stage2_order') or [])
-    if (not ns["k6b_stage3_enabled"]()) or not order:
-        ss['f3_k6b_stage3_log'] = []
-        ss['f3_k6b_stage3_order_used'] = order
-        return (*res, temp_parcels, build_parcels)
-
     from stepg_pipeline import run_step_g
     from shapely.geometry import Polygon as _Pg
-    _fv3 = snapshot["財務接線_v3"]
-    _zone_of, _price_of = _fv3["原地號_區段"], _fv3["重劃前區段_面積單價"]
+    ss = fake_st.session_state
 
     def _p_of(tp):
+        _fv3 = snapshot["財務接線_v3"]
+        _zone_of, _price_of = _fv3["原地號_區段"], _fv3["重劃前區段_面積單價"]
         _lot = tp.get("原地號", "")
         if _lot not in _zone_of:
             raise RuntimeError(f"🔴 [段三 a′] {tp.get('暫編地號')!r} 之原地號 {_lot!r} 不在 原地號_區段"
@@ -722,6 +704,7 @@ def run_corner_pk_k6b(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parc
         with _cl.redirect_stdout(_io.StringIO()):
             _d, _s, _o, _w, _f = run_corner_pk(ns, fake_st, cb, cad, param_rows, _t, _b, setback,
                                                snapshot=snapshot)
+            ss[ns["SS_END_BLOCK_MODE"]] = 'trial'   # 🆕 `W-G.9-353`：試算
             try:
                 _sg = run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, _b, _w, _f, setback,
                                  eff_min_build_by_blk={})
@@ -747,22 +730,108 @@ def run_corner_pk_k6b(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parc
                 _kept.setdefault(_blk, set()).add(_pid)
         return {"kept": _kept, "bad_pools": _bad, "err": _err}
 
+    def alloc_eval(temp, build):
+        """🆕 `W-G.9-353`：以所給之宗地試算街角選位與配地，回配地首趟之末端塊評選（深拷貝）；
+        配地中止 ⇒ `raise`（⛔ 以空評選代之）。"""
+        _t, _b = _copy_pair(temp, build)
+        ns["K917_DROPPED"].clear()
+        with _cl.redirect_stdout(_io.StringIO()):
+            _d, _s, _o, _w, _f = run_corner_pk(ns, fake_st, cb, cad, param_rows, _t, _b, setback,
+                                               snapshot=snapshot)
+            ss[ns["SS_END_BLOCK_MODE"]] = 'trial'
+            run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, _b, _w, _f, setback,
+                       eff_min_build_by_blk={})
+        return _cp.deepcopy(ss.get(ns["SS_END_BLOCK_EVAL"]) or {})
+
+    return {'a_prime': a_prime, 'trial_winner': trial_winner, 'alloc_state': alloc_state,
+            'alloc_eval': alloc_eval}
+
+
+def run_end_block_merge(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback,
+                        *, snapshot, callbacks):
+    """🆕 `W-G.9-353`：末端塊合併再試之 harness 入口（`ns["end_block_merge_run"]`·單一真相源在 `app.py`）。
+    回 `(temp_out, build_out)`（無標的或試算中止 ⇒ 同一物件）；並寫 `ss[SS_END_BLOCK_MERGE]` ＝ 紀錄、
+    `ss['f3_end_block_merge_log']` ＝ 逐列紀錄。試算之副作用隔離同段三（深拷貝 `session_state` 與
+    `ns["K917_DROPPED"]`·`finally` 原地回復）。"""
+    import copy as _cp
+    ss = fake_st.session_state
     _locked = set()
     for _v in (ss.get('f3_k6b_stage1_locked_by_block') or {}).values():
         _locked |= set(_v or [])
+    _corner = set()
+    for _w in (ss.get('f3_corner_winners') or {}).values():
+        for _pid in (_w or {}).values():
+            if _pid:
+                _corner.add(str(_pid))
     _blocks = {b["label"]: {"category": b.get("category", "")} for b in cb}
     _ss_saved = _cp.deepcopy(dict(ss))
     _k917_saved = _cp.deepcopy(ns["K917_DROPPED"])
     try:
-        temp2, build2, log = ns["k6b_stage3_run"](
-            order, _locked, ss.get("t8_ownership_map", {}) or {}, temp_parcels, build_parcels,
-            _blocks, cad.get("centerlines", {}) or {}, a_prime, trial_winner, alloc_state)
+        temp3, build3, log, rec = ns["end_block_merge_run"](
+            temp_parcels, build_parcels, ss.get("t8_ownership_map", {}) or {}, _locked, _corner, _blocks,
+            cad.get("centerlines", {}) or {}, callbacks['a_prime'], callbacks['alloc_eval'],
+            callbacks['alloc_state'], setback=setback)
     finally:
         ss.clear()
         ss.update(_ss_saved)
         ns["K917_DROPPED"].clear()
         ns["K917_DROPPED"].update(_k917_saved)
-    res2 = run_corner_pk(ns, fake_st, cb, cad, param_rows, temp2, build2, setback, snapshot=snapshot)
-    ss['f3_k6b_stage3_log'] = log
-    ss['f3_k6b_stage3_order_used'] = order
-    return (*res2, temp2, build2)
+    ss[ns["SS_END_BLOCK_MERGE"]] = rec
+    ss['f3_end_block_merge_log'] = log
+    return temp3, build3
+
+
+def run_corner_pk_k6b(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback,
+                      *, snapshot):
+    """`W-G.9-344`：段三之 harness 入口。回傳七元組
+    `(診斷rows, 指配rows, 抵費地rows, winners, forced, temp_parcels_out, build_parcels_out)`。
+
+    1. 先跑 `run_corner_pk`（同參數）。
+    2. `k6b_stage3_enabled()` 為偽、或段二序（`ss['f3_k6b_stage2_order']`）為空 ⇒ 段三不辦（宗地為
+       原 `temp_parcels`／`build_parcels`·**同一物件**），`ss['f3_k6b_stage3_log'] ＝ []`。
+    3. 否則注入 `a_prime`／`trial_winner`／`alloc_state`（皆於深拷貝上試算·`_k6b_callbacks`）呼叫
+       `ns["k6b_stage3_run"]`，其後以回傳之宗地再跑一次 `run_corner_pk`。
+    4. `ss['f3_k6b_stage3_log']` ＝ 紀錄；`ss['f3_k6b_stage3_order_used']` ＝ 所用之段二序。
+    5. 試算之副作用隔離：試算前深拷貝 `session_state` 與 `ns["K917_DROPPED"]`，段三畢（含例外）
+       於 `finally` 原地回復；最終重跑之 `run_corner_pk` 覆蓋 PK 諸鍵。
+       ⚠️ `stepg_pipeline._V3_FINANCE`（模組全域）亦被試算之 `run_step_g` 改寫——其值只依
+       `snapshot`／`cb`／`cad`（⛔ 依宗地），與最終之 `run_step_g` 所寫者同值 ⇒ ⛔ 回復（具名）。
+    6. 🆕 `W-G.9-353`：段三（或其不辦）之後，辦末端塊之合併再試（`run_end_block_merge`）；宗地有變 ⇒
+       再跑一次 `run_corner_pk`。回傳其五值 ＋ 末態之宗地。
+    """
+    import copy as _cp
+    ss = fake_st.session_state
+    res = run_corner_pk(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback,
+                        snapshot=snapshot)
+    order = list(ss.get('f3_k6b_stage2_order') or [])
+    _cbk = _k6b_callbacks(ns, fake_st, cb, cad, param_rows, setback, snapshot)
+    if (not ns["k6b_stage3_enabled"]()) or not order:
+        ss['f3_k6b_stage3_log'] = []
+        ss['f3_k6b_stage3_order_used'] = order
+        temp2, build2 = temp_parcels, build_parcels
+    else:
+        _locked = set()
+        for _v in (ss.get('f3_k6b_stage1_locked_by_block') or {}).values():
+            _locked |= set(_v or [])
+        _blocks = {b["label"]: {"category": b.get("category", "")} for b in cb}
+        _ss_saved = _cp.deepcopy(dict(ss))
+        _k917_saved = _cp.deepcopy(ns["K917_DROPPED"])
+        try:
+            temp2, build2, log = ns["k6b_stage3_run"](
+                order, _locked, ss.get("t8_ownership_map", {}) or {}, temp_parcels, build_parcels,
+                _blocks, cad.get("centerlines", {}) or {}, _cbk['a_prime'], _cbk['trial_winner'],
+                _cbk['alloc_state'])
+        finally:
+            ss.clear()
+            ss.update(_ss_saved)
+            ns["K917_DROPPED"].clear()
+            ns["K917_DROPPED"].update(_k917_saved)
+        res = run_corner_pk(ns, fake_st, cb, cad, param_rows, temp2, build2, setback, snapshot=snapshot)
+        ss['f3_k6b_stage3_log'] = log
+        ss['f3_k6b_stage3_order_used'] = order
+    # 🆕 `W-G.9-353`：末端塊之合併再試（`K-9-49 ②`·段三之後）
+    temp3, build3 = run_end_block_merge(ns, fake_st, cb, cad, param_rows, temp2, build2, setback,
+                                        snapshot=snapshot, callbacks=_cbk)
+    if temp3 is not temp2:
+        res = run_corner_pk(ns, fake_st, cb, cad, param_rows, temp3, build3, setback, snapshot=snapshot)
+    return (*res, temp3, build3)
diff --git a/verify/stepg_pipeline.py b/verify/stepg_pipeline.py
index b7b5d5e..ca56b5c 100644
--- a/verify/stepg_pipeline.py
+++ b/verify/stepg_pipeline.py
@@ -835,6 +835,9 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
 
             left_cum_S = float(_left_buffer_S)
             right_cum_S = float(_right_buffer_S)
+            # 🆕 `W-G.9-353`：強制抵費地（末）⇒ 該側之鏈起於 `R_end` 之內側界（單一真相源·app 同構）
+            left_cum_S += ns["end_block_forced_buf"](_eb_info, 'left')
+            right_cum_S += ns["end_block_forced_buf"](_eb_info, 'right')
             # W₀＝該側 Rw 累積起算點（telescoping 閘用：ΣRw_側 = R(W_final) − R(W₀)）。
             #   🆕 W 正典（脫鉤 S·da6acf1/補丁七）：W₀ 改＝**首宗近側 KL W**（mp→首宗近側界線＝
             #   res['W_near']）·非舊 `buffer·cos_dn`（群起點 telescoping 約定·已隨 W 脫鉤作廢）。
@@ -1290,6 +1293,7 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                                                          far_line_dir=_fd)
                         if _gb is not None and not _gb.is_empty:
                             _fb_p2.append(_gb)
+                _fb_p2.extend(ns["end_block_forced_bands"](_eb_info))   # 🆕 `W-G.9-353`：強制抵費地（末）之 `R_end`
                 offset_geoms = _pool_strips_for_block(
                     blk_poly, d_hat, corner_pt, allocation_dir_block,
                     allocated_polys, _label=blk_label, _depth=avg_depth_default,
````

## 附錄乙　塊 `F12`（新檔 `verify/probes/probe_WG9353_endmerge.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-353 量測器（發單側窗四十九擬·檔 F12·⛔ 由受單側改一字）：末端塊之合併再試與強制抵費地
（`K-9-49 ②`·`K-9-36 ③`·補丁十 §一 之無勝者 fallback）。

子命令（一律 python verify/probes/probe_WG9353_endmerge.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取函式）：S1 評選之強制抵費地准否；S2〜S4 一街廓之落位
           （強制 ⇒ ⛔ 落位·紀錄·沿用·不准即停機）；S5 強制帶之 s 長；S6 強制帶之多邊形；S7 定案趟之檢；
           S8 顯示；S9 宿主之准否（試算恆准·定案唯同退縮之合併再試紀錄所載者准）；S10 合併再試（① 同街廓成·
           ② 道路成且驗「不影響原位次」·該驗不過 ⇒ 未成·皆未達 ⇒ 記之·除外三類·競合停機·試算中止 ⇒ 逕回並記）。
           另施八突變，每一突變須使至少一例轉紅（判別力）。
  wiring   <repo>
           AST／字樣查接線：W1 模組層之常數與函式、⛔ 案件字面；W2 二宿主之強制帶 s 長與池之強制帶；
           W3 宿主之准否；W4 harness 段三與末端塊合併再試之試算皆為 `'trial'`、`run_corner_pk_k6b` 於段三（或其
           不辦）之後恰一次呼叫 `run_end_block_merge`；W5 `run_end_block_merge` 之隔離與紀錄；W6 `_WF_NS_NAMES`；
           W7 `end_block_merge_run` 之單一真相源（`k6b_stage3_run`）與競合之檢。另施四突變，每一突變須轉紅。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 無標的（`R6` 左端各筆單獨已有當選者·合併再試紀錄
           ＝ 無標的·無皆未達）。另於退縮 `3.5` 實跑四合成案（注入於 harness 之 `ns`·⛔ 改檔）：
           甲 ＝ 假設 `628-4(1)` 跨占街角規定範圍；乙 ＝ 甲 ＋ `628-1(3)` 上鎖；丙 ＝ 乙 ＋ `628-21(1)`、`628-22(1)` 上鎖；
           丁 ＝ `R6` 左端之末端帶以 `13 m` 構之。外部錨 ＝ 本器另寫之幾何與 G 公式（⛔ 呼叫 `end_block_*`／
           `_end_region_R`／`solve_G_binary`）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, io, os, re, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NEW_FUNCS = ["end_block_forced_buf", "end_block_forced_bands", "end_block_merge_run"]
NEW_CONSTS = ["SS_END_BLOCK_MODE", "SS_END_BLOCK_MERGE"]
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


# ── 合成幾何（同 F11）：FRONT 沿 x 軸 p1=(0,0)→p2=(40,0)；ALLOC ∥ y 軸；深 30；左端外斜 3 m（未臨正街 45 ㎡）──
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


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__)
    out.append((name, got, exp))


# ── S10 之玩具：一街廓 BX（住宅區）＋ 道路 RX；候選 C1(1)／C2(1)（依原投影序）──
def _toy(a_c1b=40.0, mark=None):
    bx = dict(所屬街廓="BX", 街廓分類="住宅區", 面積_m2=0.0)
    temp = [
        _tp("C1(1)", [(0, 0), (5, 0), (5, 30), (0, 30)], "C1", 分攤登記面積_m2=100.0, **bx),
        _tp("C1(2)", [(5, 0), (10, 0), (10, 30), (5, 30)], "C1B", 分攤登記面積_m2=a_c1b, **bx),
        _tp("C2(1)", [(10, 0), (15, 0), (15, 30), (10, 30)], "C2", 分攤登記面積_m2=90.0, **bx),
        _tp("R2(1)", [(10, -10), (15, -10), (15, 0), (10, 0)], "R2", 分攤登記面積_m2=70.0,
            所屬街廓="RX", 街廓分類="道路", 面積_m2=0.0),
        _tp("D(1)", [(15, 0), (40, 0), (40, 30), (15, 30)], "D", 分攤登記面積_m2=500.0, **bx),
    ]
    if mark:
        for t in temp:
            if t["暫編地號"] == mark:
                t["段三併出"] = ["X(1)"]
    build = [t for t in temp if t["所屬街廓"] == "BX" and not t.get("段三併出")]
    own = {"C1": "g1", "C1B": "g1", "C2": "g2", "R2": "g2", "D": "g3"}
    blocks = {"BX": {"category": "住宅區"}, "RX": {"category": "道路"}}
    return temp, build, own, blocks


def _toy_cb(thr, noaff_bad=False, both_ends=None, fail_probe=False):
    calls = {"eval": 0, "state": 0}

    def a_prime(src, dst):
        return float(src.get("分攤登記面積_m2", 0) or 0) + float(src.get("面積_m2", 0) or 0)

    def alloc_eval(temp, build):
        calls["eval"] += 1
        if fail_probe:
            raise RuntimeError("🔴 注入之配地中止")
        ids = {b["暫編地號"] for b in build}
        by = {b["暫編地號"]: b for b in build}
        out = {}
        for sd, cands in (both_ends or {"left": ["C1(1)", "C2(1)"]}).items():
            rows, win = [], None
            for c in cands:
                if c not in ids:
                    continue
                g = float(by[c].get("分攤登記面積_m2", 0) or 0) + float(by[c].get("面積_m2", 0) or 0)
                ok = g >= thr
                rows.append({"暫編地號": c, "試算G(㎡)": round(g, 2), "結果": "當選" if ok else "未達"})
                if ok:
                    win = c
                    break
            out[sd] = {"觸發": True, "R_end(㎡)": thr, "候選": rows, "當選": win}
        return {"BX": out}

    def alloc_state(temp, build):
        calls["state"] += 1
        by = {b["暫編地號"]: b for b in build}
        bad = 1 if (noaff_bad and float((by.get("C2(1)") or {}).get("面積_m2", 0) or 0) > 0) else 0
        return {"kept": {"BX": set(by)}, "bad_pools": {"BX": bad}, "err": None}
    return a_prime, alloc_eval, alloc_state, calls


def _cases(ns):
    from shapely.geometry import Polygon
    out = []
    G = _geo(ns)
    GM = _geo(ns, mirror=True)
    geo = ns["end_block_side_geom"]
    gg = geo(G["blk"], G["d"], G["p1"], G["p2"], G["cad"], G["ad"], 3.5, "left", _label="T")
    a = _tp("A(1)", [(-3, 30), (-1, 10), (5, 10), (5, 30)])
    b = _tp("B(1)", [(-1, 10), (0, 0), (5, 0), (5, 10)])
    seq = [_e(a), _e(b)]

    def trial(tp):
        return {"A(1)": 100.0, "B(1)": 120.0}[tp["暫編地號"]], 5.0
    pick = ns["end_block_pick"]
    _run(out, "S1 皆未達而准 ⇒ 無當選·列全留",
         lambda: (lambda r: (r["winner"], [x["結果"] for x in r["rows"]]))(
             pick("left", gg, seq, {}, trial, _label="T", allow_forced=True)),
         (None, ["未達", "未達"]))
    _run(out, "S1b 皆未達而不准 ⇒ 停機", lambda: pick("left", gg, seq, {}, trial, _label="T"),
         ("例外", "RuntimeError"))

    apply = ns["end_block_apply"]

    def ap(cache, allow, g=G, order=None, has=None):
        return apply(order or seq, blk_label="BX", block_poly=g["blk"], d_hat=g["d"], corner_pt=g["p1"],
                     front_p2=g["p2"], cad_alloc=g["cad"], allocation_dir=g["ad"], min_width=3.5,
                     has_side_pk=has or {"left": False, "right": True},
                     has_side_cad=has or {"left": False, "right": True},
                     corner_range_polys={}, trial=lambda tp, s, w: trial(tp), cache=cache,
                     allow_forced=allow)

    def s2():
        cache = {}
        o, i = ap(cache, lambda sd: True)
        L = i["left"]
        return ([x["tp"]["暫編地號"] for x in o], L["winner"], L["forced"], round(L["buf"], 4),
                round(L["r_end"].area, 4), cache["BX"]["left"]["當選"], cache["BX"]["left"].get("強制抵費地"),
                any(x.get("is_end_block") for x in o), i["right"])
    _run(out, "S2 強制 ⇒ ⛔ 落位·紀錄當選 None·強制抵費地·buf 3.5·R_end 150", s2,
         (["A(1)", "B(1)"], None, True, 3.5, 150.0, None, True, False, None))
    _run(out, "S3 首趟強制而本趟不准 ⇒ 停機",
         lambda: ap({"BX": {"left": {"觸發": True, "當選": None, "強制抵費地": True}}}, lambda sd: False),
         ("例外", "RuntimeError"))

    def s4():
        n = []
        o, i = apply(seq, blk_label="BX", block_poly=G["blk"], d_hat=G["d"], corner_pt=G["p1"], front_p2=G["p2"],
                     cad_alloc=G["cad"], allocation_dir=G["ad"], min_width=3.5,
                     has_side_pk={"left": False, "right": True}, has_side_cad={"left": False, "right": True},
                     corner_range_polys={}, trial=lambda tp, s, w: (n.append(1), trial(tp))[1],
                     cache={"BX": {"left": {"觸發": True, "當選": None, "強制抵費地": True}}},
                     allow_forced=lambda sd: True)
        return (i["left"]["forced"], len(n), [x["tp"]["暫編地號"] for x in o])
    _run(out, "S4 首趟強制而本趟准 ⇒ 沿用（⛔ 重評）", s4, (True, 0, ["A(1)", "B(1)"]))

    fb = ns["end_block_forced_buf"]

    def s5():
        _, iL = ap({}, lambda sd: True)
        cm = _tp("M(1)", [(35, 0), (40, 0), (43, 30), (35, 30)])
        _, iR = apply([_e(cm)], blk_label="BM", block_poly=GM["blk"], d_hat=GM["d"], corner_pt=GM["p1"],
                      front_p2=GM["p2"], cad_alloc=GM["cad"], allocation_dir=GM["ad"], min_width=3.5,
                      has_side_pk={"left": True, "right": False}, has_side_cad={"left": True, "right": False},
                      corner_range_polys={}, trial=lambda tp, s, w: (1.0, 0.0), cache={},
                      allow_forced=lambda sd: True)
        _, iW = ap({}, lambda sd: True, order=[_e(a), _e(b)])
        iW["left"]["forced"] = False
        return (round(fb(iL, "left"), 4), round(fb(iL, "right"), 4), round(fb(iR, "right"), 4),
                round(fb(iW, "left"), 4), round(fb(None, "left"), 4))
    _run(out, "S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）", s5, (3.5, 0.0, 3.5, 0.0, 0.0))

    bands = ns["end_block_forced_bands"]

    def s6():
        _, i = ap({}, lambda sd: True)
        bs = bands(i)
        i2 = dict(i)
        i2["left"] = dict(i["left"], forced=False)
        return (len(bs), round(bs[0].area, 4), len(bands(i2)), len(bands({"left": None, "right": None})))
    _run(out, "S6 強制帶 ＝ R_end（非強制⛔ 入）", s6, (1, 150.0, 0, 0))

    ah = ns["end_block_assert_head"]
    _run(out, "S7 定案趟：強制側有末端塊之宗 ⇒ 停機",
         lambda: ah("BX", {"left": {"winner": None, "forced": True}, "right": None},
                    [(_e(a, is_end_block=True), {})], []), ("例外", "RuntimeError"))
    _run(out, "S7b 定案趟：強制側無末端塊之宗 ⇒ 過",
         lambda: (ah("BX", {"left": {"winner": None, "forced": True}, "right": None}, [(_e(a), {})], []), "過")[1],
         "過")
    _run(out, "S8 顯示：強制抵費地之列",
         lambda: ns["end_block_eval_rows"]({"BX": {"left": {"觸發": True, "未臨正街(㎡)": 45.0, "末端帶(㎡)": 105.0,
                                                          "R_end(㎡)": 150.0, "當選": None, "強制抵費地": True,
                                                          "候選": []}}})["lines"],
         ["BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）"])

    host = ns["end_block_host"]

    def hs(sess_extra):
        sess = {"f3_min_width_by_label": {"BX": 3.5},
                "f3L_forced_offset": {"BX": {"left_has_side": False, "right_has_side": True}},
                "f3_cad_side_lines_by_side": {"BX": {"right": {"mid": (40.0, 15.0)}}}}
        sess.update(sess_extra)

        def solve_one(*args, **kw):
            return {"G": 100.0, "S_raw": 5.0}, "stub"
        o, i = host(list(seq), blk_label="BX", blk_poly=G["blk"], d_hat=G["d"], corner_pt=G["p1"], front_p2=G["p2"],
                    alloc_dir_cad=G["cad"], allocation_dir=G["ad"], session=sess, corner_range_polys={},
                    solve_one=solve_one, l_front=1.0, avg_depth=30.0, S_block_max=40.0, post_price=1.0,
                    pre_price_by_zone={})
        return (i["left"]["forced"], i["left"]["winner"])
    MODE, MERGE = ns["SS_END_BLOCK_MODE"], ns["SS_END_BLOCK_MERGE"]
    _run(out, "S9a 宿主：試算 ⇒ 准", lambda: hs({MODE: "trial"}), (True, None))
    _run(out, "S9b 宿主：定案而無紀錄 ⇒ 停機", lambda: hs({}), ("例外", "RuntimeError"))
    _run(out, "S9c 宿主：定案而紀錄（同退縮）載該端 ⇒ 准",
         lambda: hs({"f3L_setback_default": 3.5, MERGE: {"退縮": 3.5, "皆未達": {"BX": ["left"]}}}), (True, None))
    _run(out, "S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機",
         lambda: hs({"f3L_setback_default": 0.0, MERGE: {"退縮": 3.5, "皆未達": {"BX": ["left"]}}}),
         ("例外", "RuntimeError"))
    _run(out, "S9e 宿主：定案而紀錄只載他街廓 ⇒ 停機",
         lambda: hs({"f3L_setback_default": 3.5, MERGE: {"退縮": 3.5, "皆未達": {"BY": ["left"]}}}),
         ("例外", "RuntimeError"))

    mr = ns["end_block_merge_run"]

    def m(thr, a_c1b=40.0, noaff_bad=False, locked=(), corner=(), mark=None, both=None, fail=False):
        temp, build, own, blocks = _toy(a_c1b, mark)
        ap_, ev_, st_, calls = _toy_cb(thr, noaff_bad, both, fail)
        t2, b2, log, rec = mr(temp, build, own, set(locked), set(corner), blocks, {}, ap_, ev_, st_, setback=3.5,
                              log_print=lambda *x: None)
        main = [(r["候選"], r["層級"], r["結果"], r["檢核"]) for r in log if r.get("序") != "後處理"]
        return dict(same=(t2 is temp and b2 is build), rows=main, rec=rec, calls=dict(calls),
                    build=sorted(x["暫編地號"] for x in b2))
    _run(out, "S10a 無標的（C1(1) 單獨即達）⇒ 逕回（同一物件）",
         lambda: (lambda r: (r["same"], r["rec"]["標的"], r["rows"], r["calls"]["state"]))(m(95.0)),
         (True, [], [], 0))
    _run(out, "S10b ① 同街廓成（⛔ 驗不影響原位次）",
         lambda: (lambda r: (r["rows"], r["rec"]["皆未達"], r["calls"]["state"], r["build"]))(m(150.0, a_c1b=60.0)),
         ([("C1(1)", "①", "成", "免"), ("C2(1)", "—", "略·已定案", "—")], {}, 0, ["C1(1)", "C2(1)", "D(1)"]))
    _run(out, "S10c ② 道路成且驗不影響原位次",
         lambda: (lambda r: (r["rows"], r["rec"]["皆未達"], r["calls"]["state"]))(m(150.0)),
         ([("C1(1)", "①", "未成", "—"), ("C2(1)", "②", "成", "通過")], {}, 2))
    _run(out, "S10d ② 之驗不過 ⇒ 未成 ⇒ 皆未達",
         lambda: (lambda r: (r["rows"], r["rec"]["皆未達"]))(m(150.0, noaff_bad=True)),
         ([("C1(1)", "①", "未成", "—"), ("C2(1)", "②", "未成", "不過")], {"BX": ["left"]}))
    _run(out, "S10e 除外：上鎖者⛔ 併入", lambda: m(150.0, a_c1b=60.0, locked={"C1(2)"})["rows"][0],
         ("C1(1)", "—", "未成", "—"))
    _run(out, "S10f 除外：街角第 1 宗⛔ 併入", lambda: m(150.0, a_c1b=60.0, corner={"C1(2)"})["rows"][0],
         ("C1(1)", "—", "未成", "—"))
    _run(out, "S10g 除外：段三已併出者⛔ 併入", lambda: m(150.0, a_c1b=60.0, mark="C1(2)")["rows"][0],
         ("C1(1)", "—", "未成", "—"))
    _run(out, "S10h 競合：同一合併群之候選分屬二末端塊 ⇒ 停機",
         lambda: m(500.0, both={"left": ["C1(1)"], "right": ["C1(2)"]}), ("例外", "RuntimeError"))
    _run(out, "S10i 試算中止 ⇒ 逕回並記其由",
         lambda: (lambda r: (r["same"], r["rec"]["標的"], "試算中止" in r["rec"]))(m(150.0, fail=True)),
         (True, None, True))
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


SELF_MUTS = [
    ("M1 皆未達⛔ 理准否（恆停機）", "end_block_pick", "    if allow_forced:\n        return {'winner': None, 'rows': rows}",
     "    if False:\n        return {'winner': None, 'rows': rows}"),
    ("M2 宿主恆准", "end_block_host", "        return _mode == 'trial' or side in _mfail", "        return True"),
    ("M3 宿主⛔ 對退縮", "end_block_host",
     "if (_msb is not None and _ssb is not None and abs(float(_msb) - float(_ssb)) < 1e-9) else [])",
     "if True else [])"),
    ("M4 強制帶之 s 長恆 0", "end_block_forced_buf", "    return float(_i['buf'])", "    return 0.0"),
    ("M5 強制⛔ 入池", "end_block_forced_bands", "            _out.append(_i['r_end'])", "            pass"),
    ("M6 段三已併出者⛔ 除外", "end_block_merge_run",
     "          | {t['暫編地號'] for t in temp_parcels if t.get('段三併出')})", "          | set())"),
    ("M7 ⛔ 查競合", "end_block_merge_run", "        if len(_hit) >= 2:", "        if False:"),
    ("M8 試算中止⛔ 攔", "end_block_merge_run", "    except RuntimeError as _e:\n        _rec['標的'] = None",
     "    except KeyError as _e:\n        _rec['標的'] = None"),
]


def selftest(repo):
    try:
        ns, _ = _harvest(repo)
    except Exception as ex:  # noqa: BLE001
        print(f"  🔴 harvest 失敗：{type(ex).__name__}")
        print("⇒ 紅 ['harvest']；rc 1")
        return 1
    miss = [n for n in NEW_FUNCS + NEW_CONSTS if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    src = _read(repo, "app.py")
    print("── 合成對照（harvest 之 end_block_*／end_block_merge_run〔其內 k6b_stage3_run 為真〕）──")
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
            turned = [n for n in _report(_cases(ns), verbose=False) if n not in base_red]
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
def _wiring_checks(app, sg, sel):
    res = []
    tree = ast.parse(app)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    lits = []
    for f in NEW_FUNCS:
        if f in top:
            for n in ast.walk(top[f]):
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value):
                    lits.append((f, n.value))
    res.append(("W1 模組層之二常數與三函式、函式內⛔ 案件字面",
                all(c in consts for c in NEW_CONSTS) and all(f in top for f in NEW_FUNCS) and not lits,
                f"案件字面 {lits}"))
    scr = _fn_src(app, "f3_screen_stepg_run") or ""
    hsg = _fn_src(sg, "_run_step_g_impl") or ""

    def w2(src, fb, fbs):
        s_l = f"left_cum_S += {fb}(_eb_info, 'left')"
        s_r = f"right_cum_S += {fb}(_eb_info, 'right')"
        s_p = f"_fb_p2.extend({fbs}(_eb_info))"
        if not (src.count(s_l) == 1 and src.count(s_r) == 1 and src.count(s_p) == 1):
            return False
        i0, i1 = src.find("right_cum_S = float(_right_buffer_S)"), src.find(s_l)
        i2 = src.find("for entry in left_group:", i1)
        j1 = src.find(s_p)
        j2 = src.find("offset_geoms = _pool_strips_for_block(", j1)
        return 0 <= i0 < i1 < i2 and 0 <= j1 < j2 and "forced_bands=_fb_p2" in src[j2:j2 + 400]
    res.append(("W2 二宿主：強制帶之 s 長入鏈之起點（左鏈之前）、強制帶入池（`_pool_strips_for_block` 之前）",
                w2(scr, "end_block_forced_buf", "end_block_forced_bands")
                and w2(hsg, 'ns["end_block_forced_buf"]', 'ns["end_block_forced_bands"]'), ""))
    host = _fn_src(app, "end_block_host") or ""
    res.append(("W3 宿主之准否：讀 `SS_END_BLOCK_MODE`／`SS_END_BLOCK_MERGE`／退縮，傳 `allow_forced=_allow`",
                all(s in host for s in ("session.get(SS_END_BLOCK_MODE)", "session.get(SS_END_BLOCK_MERGE)",
                                        "session.get('f3L_setback_default')", "allow_forced=_allow"))
                and "allow_forced=_allow" in (_fn_src(app, "end_block_host") or ""), ""))
    cbk = _fn_src(sel, "_k6b_callbacks") or ""
    k6b = _fn_src(sel, "run_corner_pk_k6b") or ""

    def before_stepg(fsrc, fname):
        f = _fn_src(fsrc, fname) or ""
        i = f.find("""ss[ns["SS_END_BLOCK_MODE"]] = 'trial'""")
        j = f.find("run_step_g(ns, fake_st")
        return 0 <= i < j
    ok4 = False
    if cbk:
        inner = {n.name: ast.get_source_segment(cbk, n) for n in ast.walk(ast.parse(cbk))
                 if isinstance(n, ast.FunctionDef)}
        ok4 = all(before_stepg(inner.get(k, ""), k) for k in ("alloc_state", "alloc_eval"))
    kt = ast.parse(k6b) if k6b else None
    calls = []
    if kt is not None:
        fn = kt.body[0]
        for st_ in fn.body:
            for n in ast.walk(st_):
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "run_end_block_merge":
                    calls.append(type(st_).__name__)
    ok4 = ok4 and calls == ["Assign"] and "_cbk['alloc_state']" in k6b
    res.append(("W4 harness：`alloc_state`／`alloc_eval` 於配地前設 `'trial'`；`run_corner_pk_k6b` 於段三之 if／else 之後"
                "（頂層）恰一次呼叫 `run_end_block_merge`，段三亦用同一組回呼", ok4, f"頂層呼叫 {calls}"))
    rem = _fn_src(sel, "run_end_block_merge") or ""
    ok5 = all(s in rem for s in ('ns["end_block_merge_run"](', "finally:", "ss.update(_ss_saved)",
                                 'ns["K917_DROPPED"].update(_k917_saved)', 'ss[ns["SS_END_BLOCK_MERGE"]] = rec',
                                 "setback=setback")) and rem.find("finally:") < rem.find('ss[ns["SS_END_BLOCK_MERGE"]] = rec')
    res.append(("W5 `run_end_block_merge`：隔離（finally 復原 session 與 `K917_DROPPED`）後寫紀錄、帶退縮", ok5, ""))
    wf = None
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
            wf = ast.literal_eval(n.value)
    res.append(("W6 `_WF_NS_NAMES` 含 `end_block_forced_buf`／`end_block_forced_bands`",
                bool(wf) and "end_block_forced_buf" in wf and "end_block_forced_bands" in wf, ""))
    mr = _fn_src(app, "end_block_merge_run") or ""
    ok7 = ("k6b_stage3_run(_rows, _L, own_map" in mr and "k6_merge_groups(_pk, own_map)" in mr
           and "set(locked or ()) | set(corner_lots or ())" in mr)
    res.append(("W7 `end_block_merge_run`：交 `k6b_stage3_run`（單一真相源）、除外三類、競合以合併群查", ok7, ""))
    return res


WIRE_MUTS = [
    ("N1 harness 左鏈⛔ 讓出強制帶", "verify/stepg_pipeline.py",
     "            left_cum_S += ns[\"end_block_forced_buf\"](_eb_info, 'left')\n", "", "W2"),
    ("N2 harness 配地試算⛔ 設 trial", "verify/selection_pipeline.py",
     "            ss[ns[\"SS_END_BLOCK_MODE\"]] = 'trial'   # 🆕 `W-G.9-353`：試算\n", "", "W4"),
    ("N3 宿主⛔ 傳准否", "app.py", "trial=_trial, cache=_cache, allow_forced=_allow)", "trial=_trial, cache=_cache)", "W3"),
    ("N4 畫面⛔ 入池強制帶", "app.py",
     "                _fb_p2.extend(end_block_forced_bands(_eb_info))   # 🆕 `W-G.9-353`：強制抵費地（末）之 `R_end`\n",
     "", "W2"),
]


def wiring(repo):
    app = _read(repo, "app.py")
    sg = _read(repo, "verify/stepg_pipeline.py")
    sel = _read(repo, "verify/selection_pipeline.py")
    print("── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py ＋ verify/selection_pipeline.py）──")
    red = []
    base = _wiring_checks(app, sg, sel)
    for name, ok, note in base:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print("── 判別力（每一突變須使至少一項由綠轉紅）──")
    for mname, f, x, y, exp in WIRE_MUTS:
        src = {"app.py": app, "verify/stepg_pipeline.py": sg, "verify/selection_pipeline.py": sel}[f]
        n = src.count(x)
        if n != 1:
            print(f"  🔴 {mname}：突變錨不存在（{n}）")
            red.append(mname.split()[0])
            continue
        m = src.replace(x, y, 1)
        a2, s2, l2 = (m if f == "app.py" else app), (m if f == "verify/stepg_pipeline.py" else sg), \
            (m if f == "verify/selection_pipeline.py" else sel)
        turned = [nm.split()[0] for (nm, ok, _), (_, ok0, _) in zip(_wiring_checks(a2, s2, l2), base) if ok0 and not ok]
        ok = exp in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本器另寫之幾何與 G 公式（外部錨·同 F11 之法）──
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


SCEN = {
    "甲": dict(excl=["628-4(1)"], lock=[], mw=None),
    "乙": dict(excl=["628-4(1)"], lock=["628-1(3)"], mw=None),
    "丙": dict(excl=["628-4(1)"], lock=["628-1(3)", "628-21(1)", "628-22(1)"], mw=None),
    "丁": dict(excl=[], lock=[], mw=13.0),
}


def _pipeline(ns, fake_st, rv, sb, scen=None):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    from selection_pipeline import run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    saved = {k: ns[k] for k in ("end_block_host", "end_block_merge_run", "end_block_side_geom")}
    cfg = SCEN.get(scen) or dict(excl=[], lock=[], mw=None)
    hits = {"host": 0, "merge": 0, "geo": 0}

    def host(ordered, **kw):
        if kw.get("blk_label") == "R6" and cfg["excl"]:
            crp = dict(kw["corner_range_polys"])
            fake = [Polygon(e["tp"]["polygon_coords"]).buffer(0) for e in ordered
                    if e["tp"].get("暫編地號") in cfg["excl"]]
            if fake:
                hits["host"] += 1
                crp["left"] = unary_union(fake + ([crp["left"]] if crp.get("left") is not None else []))
            kw["corner_range_polys"] = crp
        return saved["end_block_host"](ordered, **kw)

    def merge(temp, build, own, locked, corner, *a, **k):
        if cfg["lock"]:
            hits["merge"] += 1
        return saved["end_block_merge_run"](temp, build, own, set(locked) | set(cfg["lock"]), corner, *a, **k)

    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
        if cfg["mw"] is not None and _label == "R6":
            hits["geo"] += 1
            min_width = cfg["mw"]
        return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
                                            min_width, side, _label=_label)
    ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            snapshot = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
            rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
        out = dict(cb_by=cb_by, cad=cad, snapshot=snapshot, params=params, hits=hits, err=None)
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
        out["mw"] = dict(ss.get("f3_min_width_by_label", {}) or {})
        return out
    finally:
        for k, v in saved.items():
            ns[k] = v


def _anchor_G(ns, P, blk, tp, add_a, rend, fin, snapshot, side="left"):
    """外部錨：末端位之 G（宗地 ＝ 未臨正街 ∪ 正街段之帶；G 之 S 只計正街段）——本器另寫之二分法。"""
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
    smin = min(_s_of(v, p1, d, u) for v in bp.exterior.coords)
    l2 = float(fin["sb_rows_by_label"][blk]["正街尺度"])
    post = float(fin["post_price_by_block"][blk])
    a = round(float(tp.get("分攤登記面積_m2", 0) or 0) + float(tp.get("面積_m2", 0) or 0) + add_a, 2)
    pre = float(fin["pre_price_by_zone"].get(tp.get("重劃前地價區段", ""), 0.0) or 0.0)
    A = post / pre if pre > 0 else 1.0
    B, C = fin["B"], fin["C"]
    w = -smin
    lo, hi = 0.0, L
    for _ in range(100):
        m = (lo + hi) / 2
        if bp.intersection(_halfplane(p1, d, u, -w, m, big)).area - (a * (1 - A * B) - m * l2) * (1 - C) < 0:
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


def run(repo, sbs):
    import numpy as np
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        if any(n not in ns for n in NEW_FUNCS + NEW_CONSTS):
            print("  🔴 受詞缺：end_block_merge_run 等")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from stepg_pipeline import _compute_v3_finance
        for sb in sbs:
            P = _pipeline(ns, fake_st, rv, sb)
            if P["err"]:
                print(f"🔴 執行中止（退縮 {sb}·{P['err'][0]}）：{P['err'][1]} ⇒ 無從判定")
                return 3
            rec, ev = P["rec"], P["ev"]
            ok = (rec == {"退縮": sb, "標的": [], "皆未達": {}} and P["log"] == []
                  and ((ev.get("R6") or {}).get("left") or {}).get("當選") == "628-4(1)")
            print(("  ✅" if ok else "  🔴") + f" R1 退縮 {sb}：合併再試紀錄 {rec}；逐列 {len(P['log'])}；"
                  f"R6 左當選 {((ev.get('R6') or {}).get('left') or {}).get('當選')}")
            if not ok:
                red.append(f"R1@{sb}")
        sb = 3.5
        fin = None
        for scen in ("甲", "乙", "丙", "丁"):
            P = _pipeline(ns, fake_st, rv, sb, scen)
            if fin is None:
                fin = _compute_v3_finance(ns, P["snapshot"], list(P["cb_by"].values()), P["cad"])
            print(f"══ 合成案{scen}（退縮 {sb}·注入 {SCEN[scen]}·咬到 {P['hits']}）══")
            bit = (P["hits"]["host"] > 0 if SCEN[scen]["excl"] else True) and \
                  (P["hits"]["merge"] > 0 if SCEN[scen]["lock"] else True) and \
                  (P["hits"]["geo"] > 0 if SCEN[scen]["mw"] else True)
            if not bit:
                print("  🔴 注入未咬到 ⇒ 無從判定")
                red.append(f"注入@{scen}")
                continue
            if scen == "甲":
                e = P["err"]
                ok = (e is not None and e[0] == "段三／合併再試" and "後處理" in e[1] and "停機款 9" in e[1])
                print(("  ✅" if ok else "  🔴") + f" X1 甲：地主 G009 以道路併入成，其合併群之他街廓已配地而本段無受併宗 ⇒ 停機（{e}）")
                if not ok:
                    red.append("X1@甲")
                continue
            if P["err"]:
                print(f"  🔴 執行中止：{P['err']}")
                red.append(f"中止@{scen}")
                continue
            rec, log, ev = P["rec"], P["log"], P["ev"]
            rows = [r for r in P["rows"] if r.get("所屬街廓") == "R6"]
            main = [(r["候選"], r["層級"], r["結果"], r["檢核"]) for r in log if r.get("序") != "後處理"]
            e6 = (ev.get("R6") or {}).get("left") or {}
            by = {t["暫編地號"]: t for t in P["temp"]}
            bp = Polygon(P["cb_by"]["R6"]["vertices"]).buffer(0)
            polys = [(r["暫編地號"], Polygon(r["cut_coords"]).buffer(0), r) for r in rows
                     if r.get("cut_coords") and not isinstance(r.get("cut_coords"), str)]
            un = unary_union([p for _, p, _ in polys])
            ovl = sum(polys[i][1].intersection(polys[j][1]).area for i in range(len(polys))
                      for j in range(i + 1, len(polys)))
            okg = un.symmetric_difference(bp).area <= 0.05 and ovl <= 0.05
            if scen == "乙":
                exp = [("628(2)", "①", "未成", "—"), ("628-1(2)", "①", "未成", "—"), ("628-23(1)", "①", "成", "免")]
                add = sum(_aprime(P["snapshot"], by[x], by["628-23(1)"]) for x in ("628-21(1)", "628-22(1)"))
                tp0 = dict(by["628-23(1)"], 面積_m2=0.0)
                ga = _anchor_G(ns, P, "R6", tp0, add, None, fin, P["snapshot"])
                head = sorted([r for _, _, r in polys if r["推進側別"] == "left"],
                              key=lambda r: float(r.get("累積S(m)", 0) or 0))[0]
                ok = (main == exp and rec["皆未達"] == {} and e6.get("當選") == "628-23(1)"
                      and head["暫編地號"] == "628-23(1)" and abs(float(head["G(㎡)"]) - ga) <= 0.02 and okg)
                print(("  ✅" if ok else "  🔴") + f" X2 乙：逐列 {main}；當選 {e6.get('當選')}；鏈首宗 {head['暫編地號']}"
                      f" G {head['G(㎡)']} ＝ 外部錨 {ga}；聯集 △ 街廓 {un.symmetric_difference(bp).area:.4f}、兩兩疊 {ovl:.4f}")
                if not ok:
                    red.append("X2@乙")
            elif scen == "丙":
                exp = [("628(2)", "①", "未成", "—"), ("628-1(2)", "①", "未成", "—"), ("628-23(1)", "—", "未成", "—")]
                fl = P["cad"]["front_lines"]["R6"]
                p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
                d = (p2 - p1) / float(np.linalg.norm(p2 - p1))
                u = np.array(P["cad"]["alloc_dir_by_block"]["R6"], float)
                u = u / np.linalg.norm(u)
                big = 4 * float(np.hypot(*(np.array(bp.bounds[2:]) - np.array(bp.bounds[:2]))))
                smin = min(_s_of(v, p1, d, u) for v in bp.exterior.coords)
                unf = bp.intersection(_halfplane(p1, d, u, smin - 1.0, 0.0, big))
                mw = float(P["mw"].get("R6", 0.0))
                band = bp.intersection(_halfplane(p1, d, u, 0.0, mw / abs(float(np.dot(d, np.array([-u[1], u[0]])))), big))
                rend = unary_union([unf, band])
                pools = [(k, p) for k, p, r in polys if "抵費地" in k]
                fp = [(k, p) for k, p in pools if abs(p.area - rend.area) <= 0.05 and p.symmetric_difference(rend).area <= 0.05]
                lots = [p for k, p, r in polys if "抵費地" not in k]
                lx = sum(p.intersection(rend).area for p in lots)
                ok = (main == exp and rec["皆未達"] == {"R6": ["left"]} and e6.get("當選") is None
                      and e6.get("強制抵費地") is True and len(fp) == 1 and lx <= 1e-4 and okg
                      and abs(float(e6.get("R_end(㎡)")) - round(rend.area, 2)) <= 0.011)
                print(("  ✅" if ok else "  🔴") + f" X3 丙：逐列 {main}；皆未達 {rec['皆未達']}；強制抵費地 {fp and fp[0][0]}"
                      f"（{fp and round(fp[0][1].area, 2)}·外部錨 R_end {rend.area:.2f}·紀錄 {e6.get('R_end(㎡)')}）；"
                      f"宗地 ∩ R_end {lx:.6f}；聯集 △ 街廓 {un.symmetric_difference(bp).area:.4f}、兩兩疊 {ovl:.4f}")
                if not ok:
                    red.append("X3@丙")
            else:
                exp_head = [("628(2)", "②", "未成", "—"), ("628-1(2)", "②", "未成", "—"),
                            ("628-23(1)", "①", "未成", "—"), ("628-4(1)", "②", "成", "通過")]
                add = _aprime(P["snapshot"], by["628-4(2)"], by["628-4(1)"])
                tp0 = dict(by["628-4(1)"], 面積_m2=0.0)
                ga = _anchor_G(ns, P, "R6", tp0, add, None, fin, P["snapshot"])
                head = sorted([r for _, _, r in polys if r["推進側別"] == "left"],
                              key=lambda r: float(r.get("累積S(m)", 0) or 0))[0]
                ok = (main[:4] == exp_head and all(x[2] == "略·已定案" for x in main[4:]) and rec["皆未達"] == {}
                      and e6.get("當選") == "628-4(1)" and head["暫編地號"] == "628-4(1)"
                      and abs(float(head["G(㎡)"]) - ga) <= 0.02 and okg)
                print(("  ✅" if ok else "  🔴") + f" X4 丁：逐列 {main}；當選 {e6.get('當選')}（R_end {e6.get('R_end(㎡)')}）；"
                      f"鏈首宗 {head['暫編地號']} G {head['G(㎡)']} ＝ 外部錨 {ga}；聯集 △ 街廓 "
                      f"{un.symmetric_difference(bp).area:.4f}、兩兩疊 {ovl:.4f}")
                if not ok:
                    red.append("X4@丁")
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

## 附錄丙　塊 `K2`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-49 ②`·`K-9-36 ③` 之落地狀態（`W-G.9-353`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`（本批開工態）；本批之 `commit` 皆在側支 `verify/W-G.9-353-endmerge`（主線⛔ 動）。⛔ 鑄號。

**落地狀態**：
- `K-9-49 ②`（合併再試）與 `K-9-36 ③`（強制抵費地）之 **harness 路徑** ＝ `W-G.9-353` 工項二（側支）：段三（含其後處理）之後、配地之前，以 `end_block_merge_run`（單一真相源 `k6b_stage3_run`·比照 `K-9-48`）辦末端塊之合併再試；仍未達之端，定案之配地以 `R_end` 全部為強制抵費地（面積嚴格 ＝ `area(R_end)`）。
- **畫面路徑** ⬜（次單）：畫面遇各筆單獨皆未達之端 ⇒ 仍停機（⛔ 靜默）。
- 本裁射程 ③ 之「數末端塊之合併再試相互競合」⇒ 碼面停機（⛔ 裁·⛔ 推）。
- 本案（態 `0b05925` ＋ 本批）不觸發：`R6` 左端各筆單獨已由 `628-4(1)` 當選 ⇒ 合併再試無標的；配地⛔ 變。

**合成案之量**（⛔ 為裁之一部·發單側窗四十九·harness·退縮 `3.5 m`·器 `verify/probes/probe_WG9353_endmerge.py run`·注入於器內·⛔ 改檔）：假設 `628-4(1)` 跨占街角規定範圍（⇒ ⛔ 為候選）——
甲 ＝ 合併再試之 ② 由地主 `G009` 經道路併入而成，其合併群之他街廓片已配地而本段無受併宗 ⇒ 段三之後處理停機（停機款 `9`·`K-9-48` 七項 `3`／`5`／`6` 之承前缺口）；
乙 ＝ 甲 ＋ `628-1(3)` 上鎖 ⇒ `628-23(1)`（`G017`）以 ① 同街廓併 `628-21(1)`、`628-22(1)` 而成（`G` `437.18`）；
丙 ＝ 乙 ＋ `628-21(1)`、`628-22(1)` 上鎖 ⇒ 皆未達 ⇒ `R_end` `252.28 ㎡` 為強制抵費地、宗地與 `R_end` 之交 `0`；
丁 ＝ `R6` 左端之末端帶以 `13 m` 構之（`R_end` `701.29`）⇒ `628-4(1)` 以 ② 經道路併 `628-4(2)` 而成（`G` `779.93`·驗「不影響原位次」通過）。

🛑 **⛔ 據本節推**任何域事項（尤：數末端塊競合之先後、強制抵費地作調配池之事項）。
````

## 附錄丁　塊 `P7`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：末端塊之合併再試與強制抵費地（`K-9-49 ②`·`K-9-36 ③`）之 harness 路徑入側支（`W-G.9-353`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`（本批開工態）；本批之 `commit` 皆在側支 `verify/W-G.9-353-endmerge`（主線⛔ 動）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 末端塊之合併再試與強制抵費地·harness 路徑（`K-9-49 ②`·`K-9-36 ③`） | `end_block_merge_run`：段三（含其後處理）之後，以段三後之宗地試算配地，取各筆單獨皆未達之端為標的；其未達候選依原投影序交 `k6b_stage3_run`（① 同街廓相鄰 → ② 道路及公設地上相鄰·整筆；② 驗「不影響原位次」；後處理同段三）；併入之除外 ＝ 段一上鎖 ∪ 街角第 `1` 宗 ∪ 段三已併出者；仍未達 ⇒ 紀錄（`SS_END_BLOCK_MERGE`）載之，定案之配地以 `R_end` 全部為強制抵費地（該側之鏈起於 `R_end` 之內側界；`R_end` 以強制帶入池）；harness 入口 ＝ `verify/selection_pipeline.py` 之 `run_end_block_merge`（`run_corner_pk_k6b` 內·段三之後） | 🔶（側支·harness 路徑；畫面路徑 ⬜；入主線另候 KL 放行） | `docs/orders/W-G.9-353_重量單.md` |
| `2` | 末端塊之合併再試·畫面路徑 | 畫面入口（段三之畫面入口之後）；須附畫面路徑之合成案（`自誤 517`） | ⬜ | 次單 |
| `3` | 數末端塊之合併再試相互競合 | 同一合併群之候選分屬二以上末端塊 ⇒ 碼面停機 | ⬜（⛔ 裁·候另呈） | `K-9-49` 射程 ③ |
| `4` | 規格步 `3` 候選街廓名單（五級八鍵·`r3` 之消費） | 同 `W-G.9-351` 節序 `3` | ⬜ | 規格步 `3` |
| `5` | 規格步 `4` 同歸戶合併（第一趟）：道路五則、公設地併入 | 同 `W-G.9-351` 節序 `4` | ⬜ | 規格步 `4` |
| `6` | 規格步 `5` 末端塊與中間調配池之進入與落位（`K-9-38`〜`40`） | 前置：`K-9-38` 射程 ④、`K-9-40` 射程 ④ 之附圖另呈；受詞之強制抵費地（末）＝ 本表序 `1` | ⬜ | 規格步 `5` |
| `7` | 規格步 `6` ½ 之判與出口（增配／現金補償·裁定 H、I、L、M） | — | ⬜ | 規格步 `6` |
| `8` | 規格步 `7`／`8` 終態與出艙 | — | ⬜ | 規格步 `7`／`8` |

🔒 **本批之讀法**（發單側之工程裁·⛔ 域裁·已以【通知】呈 KL）：① 合併再試之標的 ＝ 以段三後之宗地試算配地，其首趟之評選各筆單獨皆未達之端；列 ＝ 各標的之未達候選依原投影序；② 試算之配地（段三之試算與合併再試之試算）遇各筆單獨皆未達之端 ⇒ 暫以強制抵費地計（⛔ 停機）；③ 定案之配地唯合併再試之紀錄（同一退縮）所載之端得為強制抵費地，否則停機；④ 強制抵費地（末）＝ `R_end` 全部，該側之鏈起於 `R_end` 之內側界（∥ 分配線）；⑤ 合併再試中止於段三之後處理者（`K-9-48` 七項 `3`／`5`／`6` 之承前缺口）⇒ 停機（⛔ 靜默）。
🔒 **本案之量**：態 `0b05925` ＋ 本批·harness·退縮 `3.5 m`／`0 m` ⇒ 合併再試無標的；配地⛔ 變。合成案之量見 `K-6` 典「`K-9-49 ②`·`K-9-36 ③` 之落地狀態（`W-G.9-353`）」節。
🔒 **依賴序**：序 `1`（本批·側支）→ 序 `2`（次單·同側支）→ 二者同批入主線（另候 KL 放行）→ 序 `4` → 序 `5` → 序 `6`（其前置之附圖另呈）→ 序 `7` → 序 `8`；序 `3` 候 KL 另裁；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級）。
🔒 **本機介面**：主線之生產碼⛔ 變（本批之生產碼只推側支）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `12`（子字串框·含圖例與本列）·列 ＝ `10`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

---

SELF_SHA256: 99cef36e201331cbd22a624c99603200243acae8f10a713da4dd574a0ef42a79
