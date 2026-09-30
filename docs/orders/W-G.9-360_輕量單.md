# `W-G.9-360`　輕量單：主線快轉（至 `bd072eb`·`W-G.9-359` 調配之候選街廓名單入主線）＋ 候選街廓名單之突變之判別力（`W-G.9-359 §四-2` 之補寫·`F19`）＋ 攢批登記（`自誤 551`〜`557`）＋ 待落地清單之更新 ＋ 主 checkout 之同步

> **本單建議等級 ＝ `high`**（本單⛔ 令 CC 撰寫生產碼；受詞 ＝ 快轉、塊之原封入倉與實跑、二簿之末端追加、主 checkout 之同步）。
> **發單** ＝ 發單側窗五十八·`2026-09-30`。**受單** ＝ CC 新窗（工項零′〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**）。
> **級** ＝ **輕**（本批⛔ 新增生產碼：新量測器 `1` 檔 ＋ 自誤簿、`CLAUDE.md` 之純末端追加 ＋ 報告；工項零′ 之快轉使主線納入已於側支放行之生產碼 `commit` `1` 筆〔`e1b5b04`〕·其入主線之放行見 `§二`；本批⛔ 跑 `run_all` 及 `run` 類之量——快轉後主線之生產碼 `34` 檔 ≡ 側支之端，`W-G.9-359R` `V-2`〜`V-5` 與發單側窗五十八之復驗〔`§一` 項 `4`／`5`〕已跑·KL 令：文件批⛔ 全套驗證儀式）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`；側支 `verify/W-G.9-359-cand` ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`（`W-G.9-359` 工項四）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F19`／`E7`／`P14` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-360_輕量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項四之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F19`）與改動（`E7`／`P14`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）之一字；既有量測器（含 `F18`）之一字；任何錨之改；`verify/baselines`；`verify/out/` 之二凍存名單；`GB` 簿、`VR` 簿、`K-6` 典、`docs/配地計算總規格_v3.md`、恆常附款登記表之一字；自誤簿、`CLAUDE.md` 除塊 `E7`／`P14` 之純末端追加外之一字；任何側支之推送、刪除或改寫（`verify/W-G.9-359-cand` 留於 `bd072eb`·⛔ 再推）；`run_all` 之執行。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止；**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零′**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`；`git rev-parse origin/verify/W-G.9-359-cand` ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`；`git ls-remote --heads origin` 之列數 ＝ `33`；施工樹 `git checkout --detach origin/verify/W-G.9-359-cand` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 550 549` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態（側支之端 `bd072eb`·即快轉後之主線）之 `docs/` 全檔 **`931`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十八實跑 `python verify/probes/wg9268_gate6_occupancy.py bd072eb W-G.9-360 W-G.9-359 W-G.9-396`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-360`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-359` | `9`／`21`／`3` | `9`／`21`／`5` | `24`（寬式 `26`） | `11` | `13`／`202` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `7`／`11` | 🟢 宣告框 `0`、鬆框非零（漏框偵察有咬） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `22`／`25` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免（報告內嵌本器之出艙）·受詢之判⛔ 受影響 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `bd072eb` 之追蹤檔 **`2742`** 檔·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取；發單側窗五十八以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "`自誤 <號>`" ``〕於 `bd072eb` 實算）：

| 號 | 裸（錨定 `(?<![0-9\-])<號>(?![0-9])`）列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 551` | `103` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——行號、bytes、列數等·⛔ 為自誤之引用） |
| `自誤 552` | `31` | `0` | `0` | 🟢 可取（同上） |
| `自誤 553` | `1849` | `0` | `0` | 🟢 可取（同上） |
| `自誤 554` | `61` | `0` | `0` | 🟢 可取（同上） |
| `自誤 555` | `68` | `0` | `0` | 🟢 可取（同上） |
| `自誤 556` | `66` | `0` | `0` | 🟢 可取（同上） |
| `自誤 557` | `70` | `0` | `0` | 🟢 可取（同上） |
| 對照甲［必非零］`自誤 550` | `78` | `10` | `9` | 🟢 B 形、C 形皆非空 |

自誤 `MAX` ＝ `550`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 551`〜`557`（塊 `E7`）；⛔ 鑄 `GB`／`VR`／`K-9`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `1841914`，或側支 `verify/W-G.9-359-cand` ≠ `bd072eb`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `33` |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 工項零′ 前置之任一期不符 |
| `4` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成 |
| `5` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6` | 塊 `F19`／`E7`／`P14`／`T1`／`T2` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `7` | 工項一之實跑任一 ≠ 期（尤：必過之態 ≠ `rc 0`、必破之態之末列 ≠ `§一` 項 `6` 之逐字、二態之全文與附錄丁之塊 `T1`／`T2` 不逐列相同） |
| `8` | 自誤簿或 `CLAUDE.md` 之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項四：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `11` | 工項零〜三之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `12` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者⛔ 屬之） |
| `13` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗五十八自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`；側支 `verify/W-G.9-359-cand` ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`；主線為側支之祖（`git merge-base --is-ancestor` 真；`git rev-list --count 1841914..bd072eb` ＝ `11`、反向 ＝ `0`；`git rev-list --merges 1841914..bd072eb` ＝ 空）；其餘側支 `verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`33`**（`verify/` `28`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`·二態皆 `34`） | 主線 → 側支之端相異 **`2`** 檔：`app.py` `d8938792ab09e71636dc6916b61432c522c847e5` → `cae25232047add2dc6703d9b2d1cee50d1601472`；`verify/run_verification.py` `4d83d2c5a32c364021f26679a58172e1f1554dab` → `3bd2b378368df204f0c0fca1734d597851e1252b`；`verify/selection_pipeline.py` ＝ `8d38e55013bec51ab81978336fe04e928f5baf98`、`verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`（二態同） |
| `3` | 二簿（側支之端） | `docs/reports/W-G.9波_claude.ai側自誤登記.md` `1080872` B；`CLAUDE.md` `312493` B（皆以換行結尾·CR `0`） |
| `4` | `W-G.9-359`（＋ 補令一、二）之復驗（發單側窗五十八·依交接文五十七 `§四-1`·全數自倉重跑） | **十一 `commit` 逐筆對拍**（`ecef7f3`／`14a026b`／`b63ad7f`／`f82b43b`／`2432ae2`／`03910d8`／`47180af`／`51f082d`／`e1b5b04`／`e00f775`／`bd072eb`·線性·合併 `0`·單所令之九筆訊息首段逐字〔停機報告二筆之訊息依停機款〕）：原單 ＝ `8b3a0216…`（`105532` B）、補令一 ＝ `4d3a9325…`（`42197` B）、補令二 ＝ `b632d698…`（`49043` B），`SELF_SHA256` 皆經 `P-5` 自驗相符；塊 `F18q`（`7322` B·`64de4ee7…`）施於 `507def0d…` 得 `4fb5085b…`（增 `61`／刪 `3`）＝ `51f082d` 之 `F18`；`J1` ＝ `449d3755…`；`K-6` 典 `435812 → 445942`、`CLAUDE.md` `308508 → 312493`、`v3` `65433 → 67089` 皆嚴格前綴、所增 ＝ 塊 `K5″`／`P13`／`V1` 逐位；閘 `1″`〜`5″` 自倉重算皆符（刪除欄：工項一′ `36`／`1`、工項一″ `61`／`3`、工項二 `app.py` `343`／`3`·`verify/run_verification.py` `21`／`0`·`J1` `12`／`0`、餘皆 `0`；生產碼相異 `2`、`verify/` 相異 `3`；CR `0`〔`16` 檔·`V6.dxf` `12308`〕；heads `33`、主線 `1841914`、七側支⛔ 變）。**逐段讀二檔之差異**（`git diff 14a026b e1b5b04 -- app.py verify/run_verification.py`·`27367` B·`421` 列·`sha256` `4c6c2004…` ＝ 報告 ⑧ 逐位）：對原單 `R-1`〜`R-13`、`X-1`〜`X-7`、補令一 `§二` 五款、補令二 `§二` 二款與 `X-8` 無偏差；**`V-8′`**：以停機報告二同目錄之差異檔施於 `2432ae2` 重建補令一之工項二（二 blob ＝ `6e6d7e33…`／`3bd2b378…`），其與 `e1b5b04` 之差 `3` 段（`5202` B·`85` 列·`sha256` `2d93fa01…` ＝ 報告 ⑩ 逐位）皆落於 `adj_pool_anchor`／`adj_candidate_lists` 之內（含 docstring）、`verify/run_verification.py` 無差；`X-8`：模組層之名 `364` → `364`（增減 `0`）；二巢狀 `_coords_bad` 之 AST 逐同；兩段式（壞損之檢先於多邊形之建置）合補令二 `R-6″` ①「閱畢全部所取之列後」。**量測**：`F18 selftest` 三態 ＝ `51f082d` ⇒ `rc 1`（`受詞缺`）／重建之補令一之碼 ⇒ `rc 1`（`⇒ 紅 ['C23', 'C24', 'C25', 'C26']；rc 1`·`P0` `30／30`·四例之得逐項 ＝ 補令二 `§二` 末）／`bd072eb` ⇒ `rc 0`（`P0` `30／30`·全文與報告 ③ 所嵌逐位同）；`F18 wiring` ⇒ `rc 0`（全文與報告所嵌逐位同）；`F18 run` ⇒ `rc 0`（二退縮 `R0`〜`R5` 皆 ✅·`23`／`24` 單位），其出艙（`7953` B）與「補令一之碼 ＋ `F18`〔`507def0d`〕」之 `run` 逐位同、與報告所嵌逐位同；`V-2` `k6s3 cmp` 二退縮相異 `0` 項；`V-3` `F8 run` 二退縮與 `F9 run` 之 `diff` 皆 `0` B；`V-4` `parity` 二退縮 `rc 0`（配地列 `35`／`34`、`36`／`35`·不符格 `0`·`Z` ＝ `[('harness', 'R1-抵費地-2')]`）；`V-5` `run_all` 同一倉外路徑（`/home/claude/w58/P`）`51f082d` 對 `e1b5b04` ⇒ 二態各 `236008` B·`cmp` 逐位同（`64` 項·PASS `28 → 28`·相異項 `0`·末端夾具／golden 列 `21／21`·對帳 `22／36 → 22／36`·`probe_WG9343_step0_flag.py runall` `rc 0`）；收工閘 `6`（`rc 0`）／`7`（`rc 0`·自誤 `535`／`550`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `49`／`52`／`[44, 47]`）與 `8″`〜`24` 之 `38` 命令（於 `bd072eb`·其生產碼與 `verify/` ≡ `e1b5b04`）皆 `rc 0`（`F18` 三子命令末列 `⇒ 紅 []；rc 0`·`P0` `30／30`；`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F4 selftest` `10/10`、`pooltemp selftest` `13/13`、`k6s3 selftest` `9/9`；`F16` `P0` `25／25`）；另以程式字樣為錨於 `e1b5b04` 之碼施補令二 `§二` 末之十突變，各恰使所指之例轉紅（`10／10`·即 `F19` 之 `M18`〜`M27`）。CC 報告 ①〜⑫ 俱載，其數與自倉所算相符；第三輪審查之發現 `2`（`adj_q2` 於面積 `≥ 1e26 ㎡` 拋 `decimal.InvalidOperation`）自倉復現 ⇒ `自誤 557`——**全數相符** |
| `5` | 快轉之淨效（主線 → 側支之端·本案） | `verify/probes/probe_WG9349_k9296.py run <tree> 3.5`／`0.0` 與 `verify/probes/probe_WG9350_frontroad.py run <tree>`：`51f082d`（其生產碼 `34` 檔 ＝ `1841914`）與 `bd072eb` 之出艙逐位同（`diff` 皆 `0` B）；`verify/probes/probe_WG9344_k6s3.py cmp` 二退縮相異 `0` 項；`verify/probes/probe_WG9345_screen.py parity` 二退縮不符格 `0`；`run_all` 同一倉外路徑（`/home/claude/w58/P`）二態各 `236008` B·`cmp` 逐位同 ⇒ **本案之配地、街角、抵費地皆⛔ 變**（名單僅顯示·⛔ 消費端）；他案之差 ＝ 正面線唯沿公園、廣場等非道路之公共設施街廓者，其正面道路由推導改為使用者填名（`K-9-52` ①）；介面成果區多「🧭 調配之候選街廓名單」一區 |
| `6` | 量測器 `F19`（附錄甲）之二態 | **必過**：`bd072eb` 之 `app.py`（`cae25232…`）、`verify/run_verification.py`（`3bd2b378…`）與 `F18`（`4fb5085b…`）⇒ **`rc 0`**；本部 `Z0`〜`Z2` 皆 ✅；四十一突變 `M1`〜`M41` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`。**必破**：`51f082d`（`F18` ＝ `4fb5085b…`·生產碼 `34` 檔 ≡ `1841914`）⇒ **`rc 1`**；`Z0` ✅、`Z1`／`Z2` 🔴（受詞缺）、⛔ 施突變；末列逐字 `⇒ 紅 ['Z1', 'Z2']；rc 1`。二態之全文 ＝ 附錄丁之塊 `T1`／`T2`。🔒 **第三態**（發單側之佐證·⛔ 為 CC 之期·倉內無其 `commit`）：`51f082d` 之上置補令一之工項二之二檔（`6e6d7e33…`／`3bd2b378…`）⇒ `rc 1`，末列 `⇒ 紅 ['Z1', 'Z2']；rc 1`——`Z1` 之紅 ＝ `['C23', 'C24', 'C25', 'C26']`（補令二之四例）、`Z2` 以 `ValueError` 穿出（兩段式未施）。🔒 **等價之突變⛔ 入**：同深之容差之比改以浮點（`_tolq = float(tol)`）於 `0.1`／`0.5` 二容差下與原碼等價（`Decimal` 與 `float` 之比為精確比）⇒ 無例可使之轉紅 ⇒ ⛔ 入 `F19` |
| `7` | KL 主 checkout（倉外之物·發單側⛔ 實查） | 依 `W-G.9-358` 工項四 ＝ `wip/s1-endpart` 之 `1841914`（`W-G.9-359` ⛔ 動之）；其根或有 `W-G.9-359` 之來源檔（原單、補令一、補令二·未追蹤·`W-G.9-359` 補令二 `§七` 項 `3` 令 KL 自行移除）⇒ 依工項四之撞檔前置處置 |

---

## `§二`　KL 之語與射程

🔒 **所據**：`W-G.9-359 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之二條件、`R-7` 之八鍵與同深之判、`R-9` 之資料來源、`X-2` 之字樣）及其突變之判別力（`§一` 項 `8` 之十三突變之形）；併入主線之請示。」——接線與行為已由 `F18` 之 `wiring`（`W1`〜`W6`）與 `selftest`（`C1`〜`C26`）量之；本單之 `F19` 補其判別力：以原單 `§一` 項 `8` 之十三、補令一 `§二` 末之四、補令二 `§二` 末之十之突變之形，另加 `F18 wiring` 各項之突變與補令二 `R-6″` ① 之兩段式（`Z2`）之突變，共四十一，每一須使 `F18` 之所指之項轉紅。自誤甲〜丁（補令一 `§六`）、戊己（補令二 `§六`）於本單鑄號（塊 `E7`·`自誤 551`〜`556`），並鑄發單側窗五十八復驗所捕之一（`自誤 557`）。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：發單側窗五十八於對話呈下列之問一。CC 端之放行：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項零′（主線快轉）與工項四（主 checkout 之同步）之放行，CC 將其逐字載入報告；**無之 ⇒ 工項零′ 之前置畢後停於快轉前，於對話請示 KL**。所答之【要你判斷】逐字 ＝ 問一之【要你判斷】。問一（發單側所呈·【現況】至【要你判斷】逐字）：

> 【現況】359 做的是「調配之候選街廓名單」：每一個要調配的合併單位，依五級八鍵排出可以去的街廓之先後（只顯示，還沒有任何配地讀它）；並依您 9/29 所裁，正面道路只算「道路」類街廓、深度相差 0.1 m 以內視為同深。本窗已全數復驗；目前只在側支，主線與您本機介面仍是 358 之狀態。
> 【要改成】在 360 一併辦理：主線推進到側支之最新狀態，補入名單程式之突變檢查與七則自誤登記，並同步您本機的程式資料夾。
> 【對土地的影響】本案退縮 3.5 m 與 0 m 之配地面積、街角、抵費地都不變。介面成果區多一區「🧭 調配之候選街廓名單」：使用前須於步驟 E 為 R1、R4 填同一條正面道路名稱並按「✅ 儲存路寬資料」，未填則該區以紅字列出須填名之街廓。他案：正面線只沿公園、廣場等者，其正面道路由您填名。
> 【要你判斷】是否同意將 359 併入主線，並請 CC 同步您本機的程式資料夾（併於 360 辦理）？（是／否）

🔒 **逐筆放行清單**（`恆常附款 y`·擬本單時自倉重導）：母體 ＝ `git rev-list 1841914..bd072eb` ＝ **`11`** 筆；判準 ＝ 是否改動生產碼 `34` 檔之任一（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）。動生產碼者 **`1`** 筆（其餘 `10` 筆皆單、補令、停機報告、量測器、入典與登記、報告）：

| `commit` | 訊息首段 | 所動之生產碼 | 側支之放行 | 本案之土地後果 |
|---|---|---|---|---|
| `e1b5b04ac2957e1e732854f58f50f99d37bb8ea5` | `W-G.9-359` 工項二：調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）＋ 正面道路只限道路類 ＋ 驗證路徑之區外道路名稱 ＋ 補令一、二 | `app.py`、`verify/run_verification.py` | `W-G.9-359 §二`（原單）·補令一·補令二 | ⛔（`W-G.9-359R` `V-2`〜`V-5`；發單側窗五十八自倉重跑 ＝ `§一` 項 `5`） |

🛑 **射程**：`(a)` 主線快轉至 `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`（工項零′·**以前置皆符且本節之放行成立為條件**）；`(b)` 工項零〜三（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項四於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、既有量測器、任何他錨、`GB`／`VR`／`K-6` 典；`(e)` ⛔ 及 `CLAUDE.md` 所載之「待落地清單之更新：調配之候選街廓名單（…）入側支（`W-G.9-359`）」節序 `6`（名單之消費·規格步 `4`〜`6`）、序 `7`（畫面所填名稱之持久化）、`GB-186` 之成因、`K-9-51` 射程 `③`、畫面批——另單。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存倉外之目錄 `<O>`）：
1. `git merge-base --is-ancestor 1841914ea4a89e8b2714100a0f5831fec5d3e3dd bd072eb8924d7139d1c1bb6e39129f8b8be93f8b` ⇒ `rc 0`；`git rev-list --count 1841914..bd072eb` ＝ `11`；`git rev-list --count bd072eb..1841914` ＝ `0`。
2. `git diff --name-only 1841914 bd072eb -- app.py ":(glob)verify/*.py"` ⇒ 恰 `2` 列：`app.py`、`verify/run_verification.py`（`§一` 項 `2`·🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 之檔，發單側實測得 `3` 列）；`git rev-parse bd072eb:app.py` ＝ `cae25232047add2dc6703d9b2d1cee50d1601472`。
3. `git rev-list 1841914..bd072eb` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `commit`（全 `40` 碼·命中 `2` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3`·⛔ 快轉。

**快轉**（前置皆符且 `§二` 之放行成立後·與前置為分開之呼叫）：

```
git push origin bd072eb8924d7139d1c1bb6e39129f8b8be93f8b:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4`）；⛔ 改目標值（逐字 `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-359-cand`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`；
② 遠端 heads ＝ **`33`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `bd072eb` 之相異 ＝ **`0`**；判別力［必非零］：vs `1841914` 之相異 ＝ **`2`**（`§一` 項 `2` 之 `2` 檔）；
④ `git branch -r --contains e1b5b04ac2957e1e732854f58f50f99d37bb8ea5` 含 `origin/wip/s1-endpart`。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `bd072eb…` 方續工項零。

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-360_輕量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-360 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F19` 入倉與實跑（主線·零生產碼）

1. 塊 `F19`（附錄甲）依圍欄之逐列索引抽出、對拍 `§五-1` 項 `2` 後，以二進位寫為 `verify/probes/probe_WG9360_cand_mut.py`（**新檔**）；`git check-ignore` 之⛔ 命中。
2. **必過之態**（施工樹·其 `app.py` ＝ `cae25232…`、`verify/run_verification.py` ＝ `3bd2b378…`、`verify/probes/probe_WG9359_cand.py` ＝ `4fb5085b…`）：`python verify/probes/probe_WG9360_cand_mut.py mut <repo> > <O>\f19_pass.log` ⇒ **`rc 0`**；本部 `Z0`〜`Z2` 皆 ✅；四十一突變 `M1`〜`M41` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`；全文與附錄丁之塊 `T1` 逐列相同（比對前去 CR 及列尾空白）。🔒 本器唯讀、⛔ 寫檔；四十一突變中所指含 `W` 者（`16` 種）另跑 `F18` 之 `wiring`（`AST` ＋ 畫面區塊之合成執行），發單側本機全程 `689` 秒（三流並行之下）。
3. **必破之態**：`git worktree add --detach <P> 51f082dbcf7255b071ff069410ebb7e63d4274f2`（`W-G.9-359` 補令二 工項一″ 之端：其 `F18` ＝ `4fb5085b…`、生產碼 `34` 檔 ≡ `1841914`·`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑）；於施工樹 `python verify/probes/probe_WG9360_cand_mut.py mut <P> > <O>\f19_break.log` ⇒ **`rc 1`**，末列逐字 ＝ `§一` 項 `6` 之必破之末列；全文與附錄丁之塊 `T2` 逐列相同（同上）；跑畢 `git worktree remove --force <P>`。

任一 ≠ 期 ⇒ 停機款 `7`（⛔ 改器）。`commit` 訊息逐字 `W-G.9-360 工項一：量測器 F19（調配之候選街廓名單之突變之判別力）入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　攢批登記與待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `E7`（附錄乙）附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P14`（附錄丙）附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-360 工項二：攢批登記（自誤 551〜557）＋ 待落地清單之更新（W-G.9-359 入主線 ＋ 突變之判別力）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-360R_入主線與候選街廓名單之突變_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ 工項一之二態之全文（`f19_pass.log`／`f19_break.log`）；⑤ 三塊之實得（bytes／`sha256`）與二簿之改前改後 bytes；⑥ `§二` 之放行（KL 之逐字或請示之經過）；⑦ CC 之自捕與自解；⑧ 各段耗時。收工閘之實測值與工項四之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-360 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項三 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `cae25232047add2dc6703d9b2d1cee50d1601472`；`git -C <主 checkout> hash-object verify/run_verification.py` ＝ `3bd2b378368df204f0c0fca1734d597851e1252b`；`git -C <主 checkout> hash-object verify/case_front_road_names_UC9898.json` ＝ `449d375530d8d2207f39aec9f9ac3ba7b524b1c7`；`git -C <主 checkout> hash-object verify/selection_pipeline.py` ＝ `8d38e55013bec51ab81978336fe04e928f5baf98`。

任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之刪除欄 | 逐檔 **`0`** |
| `2` | 生產碼 `34` 檔 | 對 `bd072eb` 相異 **`0`**；判別力［必非零］：對 `1841914` 相異 **`2`**；`verify/` 之一切檔對 `bd072eb` 相異恰 **`1`**（新檔 `verify/probes/probe_WG9360_cand_mut.py`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`5` 檔：本單、`F19`、自誤簿、`CLAUDE.md`、報告） |
| `4` | 二簿之 bytes | 自誤簿 `1080872` → **`1089994`**；`CLAUDE.md` `312493` → **`317190`**；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`33`**；主線 ＝ 工項三之 `commit`，其祖含 `bd072eb`；`verify/W-G.9-359-cand` ＝ `bd072eb…`；`verify/W-G.9-357-k948` ＝ `4716f20…`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 557 550 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 557 550` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`542`**／`MAX` **`557`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `49`／`52`／`[44, 47]`（`GB`／`VR`／`K-9` 皆 ＝ 開工態；自誤唯增 `551`〜`557`） |
| `8` | `python verify/probes/probe_WG9360_cand_mut.py mut <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9359_cand.py selftest <repo 絕對路徑>`；`… wiring …`；`python verify/probes/probe_WG9358_k948_wiring.py wiring <repo 絕對路徑>`；`python verify/probes/probe_WG9357_k948.py selftest <repo 絕對路徑>`；`python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>`；`python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | 皆 **`rc 0`**；`F18` 二子命令、`F17`、`F16` 之末列逐字 `⇒ 紅 []；rc 0`（`F18 selftest` 之 `P0` `30／30`；`F16` 之 `P0` `25／25`）；`wfns_ast` 末列 **`48`／`48`／`47`**；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零′〜三（快轉 ＋ 本單 ＋ 塊 `F19` ＋ 塊 `E7`／`P14` ＋ 報告之替身）並實跑閘 `1`〜`9` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F19` | `18223` B·`sha256` `bacc9373c5dd3e329f1c05faff3c70f713ea8c234e4c936bcc70654ce965ce09`·`291` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9360_cand_mut.py`（blob `11661d77904855635ee8073b0d8a22b50a8bd2b8`） |
| `3` | 塊 `E7` | `9122` B·`sha256` `19b601776468c8174313200c384e2dd05b1487ef01454d3eaa965f49278e5df4`·`79` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1080872` B）之末後，期末 ＝ `1089994` B |
| `4` | 塊 `P14` | `4697` B·`sha256` `a332307039900a959649584268973f5d9dbaed9f14e23475183e755b198ac2b9`·`22` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`312493` B）之末後，期末 ＝ `317190` B |
| `5` | 附錄丁之塊 `T1`／`T2`（工項一之二態之出艙·發單側實跑） | `T1` `3806` B·`sha256` `b7ce775887993a45a1321533e046dec7fb32b9a55271bc95adaa4f37f8315726`·`47` 列；`T2` `466` B·`sha256` `5f992aa12302894cfbce50d355a29844fbdba9f9549ef679f821a9b15c14522c`·`6` 列（圍欄內全文·末附換行；比對時去 CR 及列尾空白） |
| `6` | 量測器之二態 | `§一` 項 `6` |
| `7` | 本單所載 KL 之語 | `§二` 之問一，發單側窗五十八於對話所呈（KL 之答 ＝ 貼本單之同一訊息） |
| `8` | 自誤 `557` 之復現 | `decimal` 預設精度 `28`：`Decimal(repr(float(9.99e25))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)` ＝ `99900000000000000000000000.00`；同式以 `1e26` ⇒ `decimal.InvalidOperation`（`isinstance(…, ArithmeticError)` 真、`isinstance(…, RuntimeError)` 偽） |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十八實跑（態 `bd072eb`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-4` `:76`（`§一` 態錨之表頭·所觸之箭頭係各項之改前改後〔項 `2`／`5` ＝ 主線 `1841914` 至側支之端 `bd072eb`；項 `4` ＝ `W-G.9-359` 之改前至改後〕，同格自載 ⇒ **具名豁免**）、`P-4` `:172`（`§四` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `bd072eb` 至工項二之端，表內自載 ⇒ **具名豁免**）、`P-6` `:76`（`§一` 態錨之表頭·其所轄之數皆發單側窗五十八自倉實跑、各格具名其命令或出處 ⇒ **具名豁免**）、`P-6` `:615`（附錄丙塊 `P14` 內「前節之更新」列·所觸之數係待落地表之序號、⛔ 為實測之數 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `20306`–`28026`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux） | `git worktree add --detach <S> bd072eb`（拋棄式·⛔ `push`·即快轉後之主線）＋ 本單 ＋ 塊 `F19` ＋ 塊 `E7`／`P14` ＋ 報告之替身·四 `commit`（訊息 ＝ `§三` 所令逐字）：工項零′ 前置 `1`〜`3` 皆符（`11`／`0`；`:(glob)` 形恰 `2` 列；逐筆判命中者恰 `e1b5b04`〔`2` 列〕）；三塊之抽取與附錄逐位同；工項一二態 `rc 0`／`rc 1`、全文與塊 `T1`／`T2` 逐位同（去 CR 及列尾空白·`stderr` `0` B）；閘 `1` 各檔之刪除欄皆 `0`（本單 `687`／`0`、`F19` `291`／`0`、`CLAUDE.md` `22`／`0`、自誤簿 `79`／`0`、報告之替身 `1`／`0`）；閘 `2` 對 `bd072eb` 相異 `0`、對 `1841914` `2`、`verify/` 相異恰 `1`；閘 `3` CR `0`（`5` 檔·`V6.dxf` `12308`）；閘 `4` 自誤簿 `1080872 → 1089994`、`CLAUDE.md` `312493 → 317190`（皆嚴格前綴）；閘 `5` 之祖含 `bd072eb`；閘 `6`〜`9` 皆 `rc 0`（閘 `6` 之形之自證命中新號 `557`、`MAX` `550 → 557`；閘 `7` 四簿 ＝ 自誤 `542`／`557`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `49`／`52`／`[44, 47]`；閘 `8` `F19` 之全文與塊 `T1` 逐位同〔`722` s〕；`F18` 二子命令／`F17`／`F16` 末列 `⇒ 紅 []；rc 0`〔`F18` `P0` `30／30`·`F16` `P0` `25／25`〕；`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」）；新檔之 `git check-ignore` 皆無命中 |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````markdown `` 或 `` ````text ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零′ ⇒ 依 `§二` 之放行、前置皆符後推主線；工項零〜三 ⇒ 逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）。
3. 收工後，主 checkout 之根之來源檔（本單、`W-G.9-359` 之原單、補令一、補令二，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F19`（新檔 `verify/probes/probe_WG9360_cand_mut.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-360 量測器（發單側窗五十八擬·檔 F19·⛔ 由受單側改一字）：調配之候選街廓名單（`W-G.9-359` ＋ 補令一、二）之
以程式字樣為錨之突變——量測器 `F18`（`verify/probes/probe_WG9359_cand.py`）之判別力。

緣由：`W-G.9-359 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之二
條件、`R-7` 之八鍵與同深之判、`R-9` 之資料來源、`X-2` 之字樣）及其突變之判別力（`§一` 項 `8` 之十三突變之形）；併入主線
之請示。」——接線與行為已由 `F18` 之 `wiring`（`W1`〜`W6`）與 `selftest`（`C1`〜`C26`·`30` 例）量之；本器補其判別力：
於記憶體中對工作樹之 `app.py`／`verify/run_verification.py` 之文字施以字樣為錨之突變（⛔ 寫檔、⛔ 符號連結），以 `F18`
之判式（`_extract_ns`／`_cases`／`_report`／`_wiring_checks`）量之。突變之形 ＝ 原單 `§一` 項 `8` 之十三、補令一 `§二`
末之四、補令二 `§二` 末之十，另加 `F18 wiring` 各項之突變與 `Z2` 之突變。

子命令（一律 python verify/probes/probe_WG9360_cand_mut.py mut <repo>）：
  本部
    Z0  受詞在：<repo>/verify/probes/probe_WG9359_cand.py 可載，其 _extract_ns／_cases／_report／_wiring_checks 皆在；
        <repo>/app.py、<repo>/verify/run_verification.py 可讀。
    Z1  未突變之態全綠：`F18` 之例（經 _extract_ns 自 app.py 之文字抽出受詞）皆 ✅（`30` 例）；`F18` 之 W1〜W6 皆 ✅。
    Z2  補令二 `R-6″` ①（「閱畢全部所取之列後」一次列出）：所取之列 ＝ [含 NaN 之列（QA／壞一）, 混維之環之列（QM／混維·
        其首二元皆有限·其多邊形之建置拋非 RuntimeError）] ⇒ adj_pool_anchor 拋 RuntimeError，其訊息含 QA、壞一，⛔ 含 QM。
  判別力：本部全綠時另施 `41` 種突變（_muts），每一突變須使其所指之項轉紅（所指 ⊆ 轉紅）；突變之錨於其檔須恰命中 `1`。
    所指之項唯含 C／P0 者 ⇒ 唯量 selftest（與 Z2）；含 W 者 ⇒ 另量 wiring。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import contextlib, importlib.util, io, os, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FA, FR = "app.py", "verify/run_verification.py"
F18_REL = "verify/probes/probe_WG9359_cand.py"
NEED = ("_extract_ns", "_cases", "_report", "_wiring_checks")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


def _load_f18(repo):
    p = os.path.join(repo, *F18_REL.split("/"))
    spec = importlib.util.spec_from_file_location("probe_WG9359_cand_for_f19", p)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _selftest_red(f18, app_src):
    """F18 之例經 _extract_ns 量之 ⇒ 紅項之名（抽出失敗 ⇒ ['抽出']）。"""
    try:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ns = f18._extract_ns(app_src)
            miss = [n for n in f18.FUNCS + f18.CONSTS if n not in ns]
            if miss:
                return ["受詞缺"], None
            cases = f18._cases(ns)
            red = f18._report(cases, verbose=False)
        return list(red), ns
    except Exception as ex:  # noqa: BLE001
        return [f"抽出:{type(ex).__name__}"], None


def _wiring_red(f18, app_src, rv_src):
    try:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = f18._wiring_checks(app_src, rv_src)
        return [n.split()[0] for n, ok, _ in res if not ok]
    except Exception as ex:  # noqa: BLE001
        return [f"W:{type(ex).__name__}"]


def _z2(ns):
    """補令二 R-6″ ①：壞損之一次列出⛔ 為他列之多邊形之建置所奪。"""
    if ns is None or "adj_pool_anchor" not in ns:
        return False, "受詞缺"
    rows = [{"推進側別": ns["ADJ_POOL_SIDE"], "所屬街廓": "QA", "暫編地號": "壞一",
             "cut_coords": [[10, -1], [12, -1], [float("nan"), float("nan")], [12, 1], [10, 1]]},
            {"推進側別": ns["ADJ_POOL_SIDE"], "所屬街廓": "QM", "暫編地號": "混維",
             "cut_coords": [[0, 0], [2, 0, 5], [2, 2], [0, 2]]}]
    try:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ns["adj_pool_anchor"](rows)
        return False, "未停"
    except RuntimeError as ex:
        m = str(ex)
        return ("QA" in m and "壞一" in m and "QM" not in m), f"RuntimeError：{m[:80]}"
    except Exception as ex:  # noqa: BLE001
        return False, f"非 RuntimeError 穿出：{type(ex).__name__}"


def _all_red(f18, app_src, rv_src, with_wiring):
    red, ns = _selftest_red(f18, app_src)
    ok2, _ = _z2(ns)
    if not ok2:
        red = red + ["Z2"]
    if with_wiring:
        red = red + _wiring_red(f18, app_src, rv_src)
    return red


# ── 突變 ── 各為 (名, 所指之項, [(檔, 錨, 代)])
_POOL_TWO = (
    "    _bad = [f\"{_r.get('所屬街廓')}／{_r.get('暫編地號')}\" for _r in _taken if _coords_bad(_r.get('cut_coords'))]\n"
    "    if _bad:\n"
    "        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值（非數、無窮大或缺·資料之瑕·\"\n"
    "                           \"位置無從定）：%s ⇒ 停機\" % '、'.join(_bad))\n"
    "    # ②③\n"
    "    _best = {}\n"
    "    for _r in _taken:\n"
    "        _p = Polygon(_r.get('cut_coords'))\n")
_POOL_ONE = (
    "    _bad = []\n"
    "    _best = {}\n"
    "    for _r in _taken:\n"
    "        if _coords_bad(_r.get('cut_coords')):\n"
    "            _bad.append(f\"{_r.get('所屬街廓')}／{_r.get('暫編地號')}\")\n"
    "            continue\n"
    "        _p = Polygon(_r.get('cut_coords'))\n")
_POOL_END = "    _out = {}\n    for _b, (_k, _p) in _best.items():\n"
_POOL_END_ONE = ("    if _bad:\n"
                 "        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值：%s ⇒ 停機\" % '、'.join(_bad))\n"
                 + _POOL_END)
_POOL_EXC = "        except (TypeError, ValueError, OverflowError, IndexError, KeyError):\n            return True\n\n    _taken"
_POOL_FIN = ("        # 補令二 `R-6″` ①（與 `adj_candidate_lists` 之錨點之坐標之檢同一式）\n        try:\n"
             "            return not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)")
_BAD = "    _bad = [f\"{_r.get('所屬街廓')}／{_r.get('暫編地號')}\" for _r in _taken if _coords_bad(_r.get('cut_coords'))]\n"
_ANCH = ("        if _coords_bad(_cs):\n"
         "            raise RuntimeError(f\"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之坐標含非數值\"")
_AREA = "        if adj_q2(_p.area) == 0:\n            continue\n"
_ANCH_POLY = ("        _p = Polygon(_cs)\n        if not _p.is_valid:\n            _p = _p.buffer(0)\n        if _p.is_empty:\n"
              "            raise RuntimeError(f\"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之多邊形為空 ⇒ 停機\")\n")


def _muts():
    return [
        # 原單 §一 項 8 之十三
        ("M1 同深改嚴格小於", ["C6"], [(FA, "                if abs(_dd) <= _tolq:\n", "                if abs(_dd) < _tolq:\n")]),
        ("M2 較寬者⛔ 排最後", ["C5"],
         [(FA, "_r5 = (0, _j5 - _i5) if _j5 >= _i5 else (1, _i5 - _j5)", "_r5 = (0, abs(_j5 - _i5))")]),
        ("M3 最小建築面積之級反向", ["C2"],
         [(FA, "_r2 = (0, _i2 - _j2) if _j2 <= _i2 else (1, _j2 - _i2)", "_r2 = (0, _j2 - _i2) if _j2 >= _i2 else (1, _i2 - _j2)")]),
        ("M4 原街廓⛔ 居首", ["C12"], [(FA, "            _items += _rest\n", "            _items = _rest + _items\n")]),
        ("M5 正面道路⛔ 比", ["C3"],
         [(FA, "_r3 = 0 if _c['正面道路'] == _s['正面道路'] else 1", "_r3 = 0")]),
        ("M6 較深與較淺同組", ["C6"],
         [(FA, "                    _r6, _dlab = (1, _dd), '較深'\n", "                    _r6, _dlab = (0, abs(_dd)), '較深'\n")]),
        ("M7 錨點取最小", ["C11"],
         [(FA, "_a = min(_sl, key=lambda _r: (-float(_r['原有面積']), str(_r['暫編地號'])))",
           "_a = min(_sl, key=lambda _r: (float(_r['原有面積']), str(_r['暫編地號'])))")]),
        ("M8 迄點取最小之抵費地", ["C14"],
         [(FA, "        _k = (-float(_p.area), str(_r.get('暫編地號')))\n", "        _k = (float(_p.area), str(_r.get('暫編地號')))\n")]),
        ("M9 偶數捨入", ["C17"],
         [(FA, "    from decimal import Decimal, ROUND_HALF_UP\n    return Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)\n",
           "    from decimal import Decimal, ROUND_HALF_EVEN\n    return Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)\n")]),
        ("M10 往大者⛔ 標第二趟排除", ["C2"], [(FA, "'第二趟排除': _r2[0] == 1})", "'第二趟排除': False})")]),
        ("M11 廣場得為正面道路", ["C15", "W2"], [(FA, "    \"廣場\": False,\n    \"綠地\": False,\n", "    \"廣場\": True,\n    \"綠地\": False,\n")]),
        ("M12 公設軌依街廓名", ["C10"], [(FA, "'鍵': (_r7[_t], _t), '使用分區': _dash,", "'鍵': (_t, _r7[_t]), '使用分區': _dash,")]),
        ("M13 深度差⛔ 取二位", ["C18"],
         [(FA, "        _d = _pos_q2((depth_by or {}).get(_l), '深度', _l)\n",
           "        _d = _pos_q2((depth_by or {}).get(_l), '深度', _l)\n        _d = (depth_by or {}).get(_l)\n")]),
        # 補令一 §二 末之四（其一依補令二 裁一改錨：退化 ＝ 面積以 adj_q2 計為 0）
        ("M14 退化之池列仍停機", ["C19", "C23"],
         [(FA, _AREA, "        if adj_q2(_p.area) == 0:\n            raise RuntimeError('🔴 退化之池列')\n")]),
        ("M15 錨點退化改取原多邊形", ["C20"],
         [(FA, _ANCH_POLY, _ANCH_POLY.replace(
             "        if _p.is_empty:\n            raise RuntimeError(f\"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之多邊形為空 ⇒ 停機\")\n",
             "        if _p.is_empty:\n            _p = Polygon(_cs)\n"))]),
        ("M16 錨點⛔ buffer(0)", ["C21"],
         [(FA, _ANCH_POLY, _ANCH_POLY.replace("        if not _p.is_valid:\n            _p = _p.buffer(0)\n", ""))]),
        ("M17 最小建築面積負值⛔ 停", ["C22"],
         [(FA, "            _ok = _q.is_finite() and _q >= 0\n", "            _ok = _q.is_finite()\n")]),
        # 補令二 §二 末之十
        ("M18 面積之判改 is_empty", ["C23"], [(FA, _AREA, "        if _p.is_empty:\n            continue\n")]),
        ("M19 面積之判改 area < 0.01", ["C23"], [(FA, _AREA, "        if _p.area < 0.01:\n            continue\n")]),
        ("M20 面積之判改 area <= 0.005", ["C23"], [(FA, _AREA, "        if _p.area <= 0.005:\n            continue\n")]),
        ("M21 去池片之坐標之檢", ["C24", "C25"],
         [(FA, "    if _bad:\n        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片",
           "    if False:\n        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片")]),
        ("M22 池片遇首個壞損即停", ["C25"], [(FA, _BAD, _BAD + "    _bad = _bad[:1]\n")]),
        ("M23 去錨點之坐標之檢", ["C26"], [(FA, _ANCH, _ANCH.replace("if _coords_bad(_cs):", "if False:"))]),
        ("M24 池片之檢唯判 NaN", ["C24", "C25"],
         [(FA, _POOL_FIN, _POOL_FIN.replace(
             "not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)",
             "any(_m.isnan(float(_pt[0])) or _m.isnan(float(_pt[1])) for _pt in _cs)"))]),
        ("M25 未滿 3 點之列亦檢", ["C25"],
         [(FA, _BAD, _BAD.replace("for _r in _taken if",
                                  "for _r in [_x for _x in (g_rows or []) if _x.get('推進側別') == ADJ_POOL_SIDE] if"))]),
        ("M26 轉換之例外唯攔 TypeError", ["C24"],
         [(FA, _POOL_EXC, _POOL_EXC.replace("(TypeError, ValueError, OverflowError, IndexError, KeyError)", "(TypeError,)"))]),
        ("M27 轉換之例外不攔 OverflowError", ["C24"], [(FA, _POOL_EXC, _POOL_EXC.replace("OverflowError, ", ""))]),
        # CC 依第三輪審查所改之兩段式（補令二 R-6″ ①·本器 Z2）
        ("M28 壞損之檢與多邊形之建置同迴圈", ["Z2"], [(FA, _POOL_TWO, _POOL_ONE), (FA, _POOL_END, _POOL_END_ONE)]),
        # F18 wiring 各項（R-2 之二條件、R-9 之資料來源、X-2 之字樣、具名常數、驗證路徑之名稱檔）
        ("M29 同深之容差改 0.5", ["W1"], [(FA, "\nADJ_DEPTH_TIE_TOL_M = 0.1\n", "\nADJ_DEPTH_TIE_TOL_M = 0.5\n")]),
        ("M30 名單之函式之預設改字面", ["W1"],
         [(FA, "def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPTH_TIE_TOL_M):",
           "def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=0.1):")]),
        ("M31 顯示列之函式之預設改字面", ["W1"],
         [(FA, "def adj_candidate_rows(cand, tol=ADJ_DEPTH_TIE_TOL_M):", "def adj_candidate_rows(cand, tol=0.1):")]),
        ("M32 正面道路推導⛔ 限道路類", ["W3"],
         [(FA, "         if _lr not in _buildable_blocks\n         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})",
           "         if _lr not in _buildable_blocks})")]),
        ("M33 正面道路推導⛔ 限非可建築", ["W3"],
         [(FA, "         if _lr not in _buildable_blocks\n         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})",
           "         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})")]),
        ("M34 新函式含 session 之字樣", ["W4"], [(FA, "    _dash = '—'\n    _out = []\n", "    _dash = '—'  # session_state\n    _out = []\n")]),
        ("M35 新函式含案件字面", ["W4"],
         [(FA, "    _n = len(cand or [])\n", "    _n = len(cand or []) + 0 * len('R1')\n")]),
        ("M36 名稱以 label 取", ["W5"],
         [(FA, "{b['label']: _adj359_names.get(b['id'], '') for b in _adj359_bb}",
           "{b['label']: _adj359_names.get(b['label'], '') for b in _adj359_bb}")]),
        ("M37 路寬取他欄", ["W5"],
         [(FA, "{_l: (_adj359_sb.get(_l) or {}).get('正面路寬(m)') for _l in _adj359_lbls}",
           "{_l: (_adj359_sb.get(_l) or {}).get('路寬(m)') for _l in _adj359_lbls}")]),
        ("M38 深度取他鍵", ["W5"],
         [(FA, "st.session_state.get('f3_alloc_depth_by_label', {}) or {})\n                                _adj359_view",
           "st.session_state.get('f3_depth_by_label', {}) or {})\n                                _adj359_view")]),
        ("M39 最小建築面積取他鍵", ["W5"],
         [(FA, "st.session_state.get(K91_SS_MBA_EFFECTIVE, {}) or {},\n                                    {_l: _adj359_ident",
           "{},\n                                    {_l: _adj359_ident")]),
        ("M40 驗證路徑之名稱檔改他檔", ["W6"],
         [(FR, "FRONT_ROAD_NAMES = os.path.join(HERE, \"case_front_road_names_UC9898.json\")",
           "FRONT_ROAD_NAMES = os.path.join(HERE, \"case_params_UC9898.json\")")]),
        ("M41 驗證路徑之讀名之函式改名", ["W6"],
         [(FR, "def load_front_road_names():", "def load_front_road_names_v0():")]),
    ]


def mut(repo):
    red = []
    print("── 本部 ──")
    try:
        src = {FA: _read(repo, FA), FR: _read(repo, FR)}
        f18 = _load_f18(repo)
        miss = [n for n in NEED if not hasattr(f18, n)]
    except Exception as ex:  # noqa: BLE001
        src, f18, miss = None, None, [f"{type(ex).__name__}: {ex}"]
    print(("  ✅ " if not miss else "  🔴 ") + f"Z0 受詞在（F18 之 {list(NEED)}；app.py；verify/run_verification.py）"
          + (f"（缺 {miss}）" if miss else ""))
    if miss:
        print("⇒ 紅 ['Z0']；rc 1")
        return 1
    st_red, ns = _selftest_red(f18, src[FA])
    w_red = _wiring_red(f18, src[FA], src[FR])
    ok1 = not st_red and not w_red
    print(("  ✅ " if ok1 else "  🔴 ") + f"Z1 未突變之態全綠（F18 之例之紅 {st_red}；W1〜W6 之紅 {w_red}）")
    if not ok1:
        red.append("Z1")
    ok2, note2 = _z2(ns)
    print(("  ✅ " if ok2 else "  🔴 ") + f"Z2 補令二 R-6″ ①：壞損之一次列出⛔ 為他列之多邊形之建置所奪（{note2}）")
    if not ok2:
        red.append("Z2")
    if red:
        print("── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（每一突變須使其所指之項轉紅·所指 ⊆ 轉紅）──")
    for mname, target, reps in _muts():
        m = dict(src)
        miss = []
        for f, a, b in reps:
            if m[f].count(a) != 1:
                miss.append(m[f].count(a))
                continue
            m[f] = m[f].replace(a, b, 1)
        if miss:
            print(f"  🔴 {mname}：突變錨之命中 {miss}（期 各 1）")
            red.append(mname.split()[0])
            continue
        turned = _all_red(f18, m[FA], m[FR], any(t.startswith("W") for t in target))
        ok = set(target) <= set(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}（須含 {target}）")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) != 3 or argv[1] != "mut":
        print(__doc__)
        return 2
    return mut(os.path.abspath(argv[2]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `E7`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-360 §零-1`）：本批取 `551`〜`557`（`7` 號）。前六號係發單側窗五十六、五十七於擬 `W-G.9-359` 補令一、二時所捕（全文逐字載於 `docs/orders/W-G.9-359_補令一.md` `§六` 甲〜丁、`docs/orders/W-G.9-359_補令二.md` `§六` 戊己·候鑄），本批依之鑄號（甲〜己 ⇒ `551`〜`556`）、⛔ 增刪其一字；第七號（`557`）係發單側窗五十八復驗 `W-G.9-359` 時據 CC 之唯讀獨立審查（第三輪）之發現 `2` 所捕；各條末之「字樣之錨」係本批所附。

### 🩸 `自誤 551`　**`W-G.9-359` `R-6`／`R-7` 令取多邊形（無效者 `buffer(0)`）之質心，未定其經 `buffer(0)` 後為空之處置；量測器 `F18` 之外部錨亦然 ⇒ 規格與量測器於退化之片皆無定義**

**形**：原單 `R-6`「取多邊形（無效者 `buffer(0)`）面積最大者」之質心、`R-7` ②「錨點之多邊形之質心」；點數 `≥ 3` 而共線者 `buffer(0)` 後為空，其質心無定義（`shapely` 拋 `GEOSException`·非 `RuntimeError` ⇒ 若不攔則穿出 `R-9` 之 `except`）。CC 之碼取停機（一讀法）；`F18` 之 `_independent` 遇之拋 `GEOSException`。發單側窗五十六以塊 `F18p` 之 `C19`／`C20` 於首輪之碼復現：`C19` 紅（`RuntimeError`）、`C20` 綠。
**後果之界**：本案⛔ 觸（池列 `14` 列、錨點皆有效非空）；他案：某街廓之片皆退化者，全部單位之名單⛔ 出（讀法甲）或其先後依讀法而異。零入倉之生產碼（CC 停機·`78c1c6f` 未推）。
**根因**：擬 `R-6`／`R-7` 時只定「無效者 `buffer(0)`」一支，未窮舉 `buffer(0)` 之值域（空）；原型與 `F18` 之玩具皆為正常之多邊形（`C14` 之退化例唯「點數 `＜ 3`」一形）⇒ 量測器之母體亦漏之。
**後果之框**：🟢 本案零土地後果；🟡 他案之名單。攔點 ＝ CC 所派之唯讀獨立 reviewer（附則丙·`F-1`）→ CC 停機款 `12`。
**攔法**：本補令裁一、裁二、`R-6′`、`R-7′` ①；`F18` 之 `C19`／`C20`。通則：凡令「取某幾何之量」者，須窮舉其前處理（`buffer(0)` 等）之值域（含空），並於量測器造其形。
**字樣之錨**（`W-G.9-360`）：量測器 `F19`（`verify/probes/probe_WG9360_cand_mut.py mut <repo>`）之突變 `M14`（退化之池列仍停機 ⇒ `C19`／`C23`）、`M15`（錨點退化改取原多邊形 ⇒ `C20`）、`M16`（錨點⛔ `buffer(0)` ⇒ `C21`），皆以 `F18`（`verify/probes/probe_WG9359_cand.py`）之判式量之。

---

### 🩸 `自誤 552`　**`W-G.9-359` `R-7` ① 未載錨點之多邊形「無效者 `buffer(0)`」，而 `R-6`、發單側之原型與塊 `F18` 之外部錨皆施之 ⇒ 規格之文字落後於原型**

**形**：停機報告 `§二-3`（`F-2`）；自交之蝴蝶形之原質心與 `buffer(0)` 之質心相異（CC 實測 `(2, 1.5)` 對 `(3.33, 1.5)`）⇒ 距離可相異。CC 依 `F18` 施之。
**後果之界**：零土地後果（本案⛔ 觸·碼 ＝ `F18`）。
**根因**：原型先成、規格後寫，未逐條對回原型之每一前處理。
**後果之框**：🟢。攔點 ＝ reviewer（`F-2`）。
**攔法**：本補令裁三、`R-7′` ①；`F18` 之 `C21`。通則：規格單之原型之每一前處理須於規格有其字。
**字樣之錨**（`W-G.9-360`）：量測器 `F19` 之突變 `M16`（錨點⛔ `buffer(0)` ⇒ `C21`）。

---

### 🩸 `自誤 553`　**`W-G.9-359` 塊 `K5` 之「裁之內容」② 書「較原街廓寬者排在全部較窄者之後」，未具名其射程（第（五）項之內·八鍵詞典序）⇒ 字面可讀為絕對排後**

**形**：停機報告 `§四` `N-6`；原單 `R-7` ③ 之明文與現碼皆為詞典序（`r5` 為第五鍵），而入典之文字未載之。
**後果之界**：零（未入典·本補令以 `K5′` 代之）。
**根因**：摘 KL 之答入「裁之內容」時，沿用呈文之語而未補其於八鍵中之位。
**後果之框**：🟢。攔點 ＝ reviewer（`N-6`）。
**攔法**：本補令裁四、塊 `K5′` 之讀法 `6`。
**字樣之錨**（`W-G.9-360`）：無程式之錨——入典之文 ＝ `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之塊 `K5″`（`W-G.9-359` 補令二·代 `K5′`）之「發單側之讀法」`6`。

---

### 🩸 `自誤 554`　**`W-G.9-359` `R-5` ② 對正面路寬、深度令其檢（缺或 `≤ 0` ⇒ 停機），對最小建築面積未令 ⇒ 非數或 `NaN` 以非 `RuntimeError` 穿出 `R-9` 之 `except`**

**形**：停機報告 `§四` `F-4`（reviewer 以非數、`NaN` 實得 `ValueError`、`decimal.InvalidOperation`）。
**後果之界**：零（現之來源 `number_input`〔`≥ 0`〕與 harness 之 `{}` 皆到不了）。
**根因**：同一函式之三個數量之檢未對齊（附則乙之「同一式」未及於檢）。
**後果之框**：🟢。攔點 ＝ reviewer。
**攔法**：本補令 `R-5′` ②；`F18` 之 `C22`。
**字樣之錨**（`W-G.9-360`）：量測器 `F19` 之突變 `M17`（最小建築面積負值⛔ 停 ⇒ `C22`）。

---

### 🩸 `自誤 555`　**`W-G.9-359` 補令一 裁一以「`buffer(0)` 後為空」為退化之判準，未核本倉已知之退化實例（`GB-186` 之非空細縫·`自誤 537` 已載其全精度之值）⇒ 裁一之由 ③ 所欲涵之態落於其判準之外**

**形**：停機報告二 `§零` `B-1`；發單側窗五十七以 `3edca01` 之碼復現（街廓 `A` 之唯一片為 `0.0046 ㎡` 之細縫 ⇒ 依距離居第 `2`；為共線三點 ⇒ 排末）。
**後果之界**：本案⛔ 觸（`R1` 之細縫非其最大片）；他案之名單先後。零入倉之生產碼（`3edca01` 未推）。
**根因**：以幾何函式庫之值域（空）定土地之性質（無可容之地），而未以既裁之池面積定式（`K-6` 典·KL `2026-08-05`）量之；擬裁前未於倉內搜既有之退化實例（`GB-186`／`自誤 537`）。
**後果之框**：🟢 本案零；🟡 他案之名單。攔點 ＝ CC 所派之唯讀獨立 reviewer（第二輪·`B-1`）→ CC 停機款 `12`。
**攔法**：本補令裁一、`R-6″` ②；`F18` 之 `C23`。通則：凡以幾何量定土地之有無者，依既裁之面積定式（兩位小數）判之，並以倉內已知之實例（細縫）入量測器之例。
**字樣之錨**（`W-G.9-360`）：量測器 `F19` 之突變 `M18`〜`M20`（面積之判改 `is_empty`／`area < 0.01`／`area <= 0.005` ⇒ `C23`）。

---

### 🩸 `自誤 556`　**`W-G.9-359` 補令一 `R-6′`／`R-7′` ① 未窮舉坐標之值域（非數、非有限）⇒ 坐標壞損之池片被靜默略去或視同無抵費地**

**形**：停機報告二 `B-2`；發單側窗五十七復現：`NaN` 頂點被略而以餘形取迄點；三點其一為 `NaN` 則整片視同無抵費地；`inf` 同；字串頂點以 `ValueError` 穿出 `R-9` 之 `except RuntimeError`；錨點之側同。
**後果之界**：本案⛔ 觸（發單側窗五十七以含坐標之檢之原型與外部錨實跑 `F18 run` ⇒ `rc 0`）；他案。
**根因**：補令一 自誤甲之通則「窮舉前處理之值域」只及 `buffer(0)` 之輸出，未及其輸入（坐標）。
**後果之框**：🟢。攔點 ＝ reviewer（`B-2`）。
**攔法**：本補令裁二、`R-6″` ①、`R-7″` ①；`F18` 之 `C24`〜`C26`。通則（補甲）：窮舉值域須及於幾何量之輸入（坐標之非數、非有限、缺）。
**字樣之錨**（`W-G.9-360`）：量測器 `F19` 之突變 `M21`〜`M27`（池片、錨點之坐標之檢之諸形 ⇒ `C24`〜`C26`）與 `M28`（壞損之檢與多邊形之建置同迴圈 ⇒ `F19` 之 `Z2`）。

---

### 🩸 `自誤 557`　**`W-G.9-359` 補令二 單首之射程載「坐標皆有限而其面積溢出為非有限者（`|坐標| ≳ 1e154`）」，未核同一流程中 `adj_q2` 之 `decimal` 精度 ⇒ 所載之界不確（實界 ＝ 面積 `1e26 ㎡`）**

**形**：`W-G.9-359R` ⑥-2 第三輪唯讀審查之發現 `2`；發單側窗五十八復現（本機 Linux·`decimal` 預設精度 `28`）：`adj_q2(9.99e25)` ＝ `99900000000000000000000000.00`；`adj_q2(1e26)` ⇒ `decimal.InvalidOperation`（`ArithmeticError` 之子類·⛔ 為 `RuntimeError`）；邊長 `1e13 m` 之方形（坐標有限）其面積 ＝ `1e26` ⇒ 經 `R-6″` ② 之 `adj_q2(_p.area)` 穿出 `R-9` 之 `except RuntimeError`。
**後果之界**：零（地表約 `5.1e14 ㎡`·物理上不可達）；唯補令二所載之界不確（低估其發生之早）。
**根因**：擬射程時唯以浮點之溢位（`float` 之 `inf`）量「面積非有限」之界，未核同一流程中 `Decimal.quantize` 於精度 `28` 之界（整數部 `27` 位以上即拋）。
**後果之框**：🟢 零。攔點 ＝ CC 所派之唯讀獨立 reviewer（第三輪·發現 `2`·CC 記之、⛔ 改）。
**攔法**：記之（`W-G.9-360` ⛔ 改生產碼·補令二之射程外）。通則：凡載「某情形之界」者，須以該流程之全部算子（含 `Decimal` 之精度）量之。
**字樣之錨**（`W-G.9-360`）：無（記之）。
````

## 附錄丙　塊 `P14`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）入主線；候選街廓名單之突變之判別力（`W-G.9-360`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線快轉至 `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`（原主線 `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`·所納 `11` 筆 `commit`，其中動生產碼者 `1` 筆：`e1b5b04`〔`W-G.9-359` 工項二·含補令一、二〕）；本批之零生產碼 `commit` 皆在主線；側支 `verify/W-G.9-359-cand` 留於 `bd072eb`（歷史·⛔ 再推）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-52` ①〜④ ＋ 驗證路徑之區外道路名稱 ＋ 規格步 `3` 候選街廓名單（harness ＋ 畫面·僅排序） | 同「待落地清單之更新：調配之候選街廓名單（…）入側支（`W-G.9-359`）」節序 `1`〜`3`；補令一、二之諸款（抵費地之片其面積以池面積之定式為 `0.00 ㎡` 者⛔ 計、錨點退化停機、錨點無效者 `buffer(0)`、最小建築面積之檢、抵費地之片與錨點之坐標含非數值者停機並一次列出）同批 | ✅（入主線） | `docs/orders/W-G.9-359_規格單.md`、`docs/orders/W-G.9-359_補令一.md`、`docs/orders/W-G.9-359_補令二.md` |
| `2` | 以程式字樣為錨之突變之判別力（規格單流程·復驗時補寫） | 量測器 `F19`（`verify/probes/probe_WG9360_cand_mut.py mut <repo>`）：本部 `Z0`〜`Z2` ＋ 四十二突變（以 `F18` 之判式量之） | ✅（入主線） | `docs/orders/W-G.9-360_輕量單.md` |
| `3` | `自誤 551`〜`557`（`W-G.9-359` 補令一 `§六` 甲〜丁、補令二 `§六` 戊己之鑄號 ＋ 復驗所捕之一） | 見自誤簿 | ✅ | 同上 |
| `4` | 名單之消費（規格步 `4` 同歸戶合併〔第一趟〕→ `5` 末端塊與中間調配池〔第二趟〕→ `6` ½ 之判） | 第二趟排除最小建築面積往大者（`v3` 五級③ `r2`） | ⬜ | 規格步 `4`〜`6` |
| `5` | 畫面所填之正面道路名稱只存於該次工作階段（重啟須再填） | — | ⬜ | 畫面批 |
| `6` | 抵費地之細縫之成因（`GB-186`） | 名單已不受其擾（`W-G.9-359` 補令二 裁一）；其生成 | ⬜ | `GB-186` |
| `7` | 錨點之多邊形為非空之細縫者；坐標有限而面積 `≥ 1e26 ㎡` 者（`adj_q2` 之 `decimal` 精度·`自誤 557`）；混維之環之多邊形之例外；`原有面積` 缺之 `KeyError` 等（停機報告二 `N-4` 之餘形） | 皆無實際來源·以非 `RuntimeError` 穿出畫面區塊 | —（記） | `docs/reports/W-G.9-359R_調配之候選街廓名單_執行報告.md` ⑥-2、⑫ |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：調配之候選街廓名單（…）入側支（`W-G.9-359`）」節序 `1`〜`3` ⇒ ✅（本表序 `1`）；序 `4` ⇒ ✅（本表序 `2`）；序 `5` ⇒ ✅（本批之快轉與主 checkout 之同步）；序 `6`、`7` 之態⛔ 變（本表序 `4`、`5`）。
🔒 **本案之量**：主線 `1841914` → `bd072eb` 之配地（退縮 `3.5 m`／`0 m`）⛔ 變——`W-G.9-359R` `V-2`〜`V-5` 與發單側窗五十八之自倉重跑：`verify/probes/probe_WG9344_k6s3.py cmp` 二退縮相異 `0` 項；`verify/probes/probe_WG9349_k9296.py run` 二退縮與 `verify/probes/probe_WG9350_frontroad.py run` 之出艙逐位同；`verify/probes/probe_WG9345_screen.py parity` 二退縮不符格 `0`；`run_all` 同一倉外路徑之出艙逐位同（`docs/orders/W-G.9-360_輕量單.md` `§一` 項 `5`）。名單僅顯示（⛔ 消費端）。
🔒 **本機介面**（主 checkout 同步後）：執行介面之環境 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6` 皆須**未設**；成果區於「🧩 調配階段之輸入」之下多「🧭 調配之候選街廓名單」一區；步驟 E 須先填 `R1`、`R4` 之正面道路名稱（同一名稱）並按「✅ 儲存路寬資料」，否則該區以紅字列出須填名之街廓。
🔒 **依賴序**：規格步 `4`（同歸戶合併·第一趟：沿名單找同歸戶、`a ＋ a′` 後算 `G`、道路五則、公設地併入·其前置之域問之查）→ `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ `W-G.9-357` 節序 `7` ＋ 本表序 `5`）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `7`（子字串框·含圖例與本列）·列 ＝ `5`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄丁　工項一之二態之出艙（`F19 mut`·發單側窗五十八實跑）

塊 `T1`（必過之態·`bd072eb`）：

````text
── 本部 ──
  ✅ Z0 受詞在（F18 之 ['_extract_ns', '_cases', '_report', '_wiring_checks']；app.py；verify/run_verification.py）
  ✅ Z1 未突變之態全綠（F18 之例之紅 []；W1〜W6 之紅 []）
  ✅ Z2 補令二 R-6″ ①：壞損之一次列出⛔ 為他列之多邊形之建置所奪（RuntimeError：🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值（非數、無窮大或缺·資料之瑕·位置無從定）：QA／壞一 ⇒ 停機）
── 判別力（每一突變須使其所指之項轉紅·所指 ⊆ 轉紅）──
  ✅ M1 同深改嚴格小於：轉紅 ['C6', 'C7', 'C18']（須含 ['C6']）
  ✅ M2 較寬者⛔ 排最後：轉紅 ['C5']（須含 ['C5']）
  ✅ M3 最小建築面積之級反向：轉紅 ['C2', 'C16']（須含 ['C2']）
  ✅ M4 原街廓⛔ 居首：轉紅 ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C11', 'C12', 'C16', 'C18', 'C19', 'C21', 'C23']（須含 ['C12']）
  ✅ M5 正面道路⛔ 比：轉紅 ['C3']（須含 ['C3']）
  ✅ M6 較深與較淺同組：轉紅 ['C6']（須含 ['C6']）
  ✅ M7 錨點取最小：轉紅 ['C11']（須含 ['C11']）
  ✅ M8 迄點取最小之抵費地：轉紅 ['C14']（須含 ['C14']）
  ✅ M9 偶數捨入：轉紅 ['C17', 'C23']（須含 ['C17']）
  ✅ M10 往大者⛔ 標第二趟排除：轉紅 ['C2', 'C16']（須含 ['C2']）
  ✅ M11 廣場得為正面道路：轉紅 ['C15', 'W2']（須含 ['C15', 'W2']）
  ✅ M12 公設軌依街廓名：轉紅 ['C10']（須含 ['C10']）
  ✅ M13 深度差⛔ 取二位：轉紅 ['C6', 'C18']（須含 ['C18']）
  ✅ M14 退化之池列仍停機：轉紅 ['C19', 'C23']（須含 ['C19', 'C23']）
  ✅ M15 錨點退化改取原多邊形：轉紅 ['C20']（須含 ['C20']）
  ✅ M16 錨點⛔ buffer(0)：轉紅 ['C20', 'C21']（須含 ['C21']）
  ✅ M17 最小建築面積負值⛔ 停：轉紅 ['C22']（須含 ['C22']）
  ✅ M18 面積之判改 is_empty：轉紅 ['C23']（須含 ['C23']）
  ✅ M19 面積之判改 area < 0.01：轉紅 ['C23']（須含 ['C23']）
  ✅ M20 面積之判改 area <= 0.005：轉紅 ['C23']（須含 ['C23']）
  ✅ M21 去池片之坐標之檢：轉紅 ['C24', 'C25', 'Z2']（須含 ['C24', 'C25']）
  ✅ M22 池片遇首個壞損即停：轉紅 ['C25']（須含 ['C25']）
  ✅ M23 去錨點之坐標之檢：轉紅 ['C26']（須含 ['C26']）
  ✅ M24 池片之檢唯判 NaN：轉紅 ['C24', 'C25']（須含 ['C24', 'C25']）
  ✅ M25 未滿 3 點之列亦檢：轉紅 ['C25']（須含 ['C25']）
  ✅ M26 轉換之例外唯攔 TypeError：轉紅 ['C24']（須含 ['C24']）
  ✅ M27 轉換之例外不攔 OverflowError：轉紅 ['C24']（須含 ['C24']）
  ✅ M28 壞損之檢與多邊形之建置同迴圈：轉紅 ['Z2']（須含 ['Z2']）
  ✅ M29 同深之容差改 0.5：轉紅 ['C6', 'C16', 'C18', 'W1']（須含 ['W1']）
  ✅ M30 名單之函式之預設改字面：轉紅 ['W1']（須含 ['W1']）
  ✅ M31 顯示列之函式之預設改字面：轉紅 ['W1']（須含 ['W1']）
  ✅ M32 正面道路推導⛔ 限道路類：轉紅 ['W3']（須含 ['W3']）
  ✅ M33 正面道路推導⛔ 限非可建築：轉紅 ['W3']（須含 ['W3']）
  ✅ M34 新函式含 session 之字樣：轉紅 ['W4']（須含 ['W4']）
  ✅ M35 新函式含案件字面：轉紅 ['W4']（須含 ['W4']）
  ✅ M36 名稱以 label 取：轉紅 ['W5']（須含 ['W5']）
  ✅ M37 路寬取他欄：轉紅 ['W5']（須含 ['W5']）
  ✅ M38 深度取他鍵：轉紅 ['W5']（須含 ['W5']）
  ✅ M39 最小建築面積取他鍵：轉紅 ['W5']（須含 ['W5']）
  ✅ M40 驗證路徑之名稱檔改他檔：轉紅 ['W6']（須含 ['W6']）
  ✅ M41 驗證路徑之讀名之函式改名：轉紅 ['W6']（須含 ['W6']）
⇒ 紅 []；rc 0
````

塊 `T2`（必破之態·`51f082d`）：

````text
── 本部 ──
  ✅ Z0 受詞在（F18 之 ['_extract_ns', '_cases', '_report', '_wiring_checks']；app.py；verify/run_verification.py）
  🔴 Z1 未突變之態全綠（F18 之例之紅 ['受詞缺']；W1〜W6 之紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']）
  🔴 Z2 補令二 R-6″ ①：壞損之一次列出⛔ 為他列之多邊形之建置所奪（受詞缺）
── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──
⇒ 紅 ['Z1', 'Z2']；rc 1
````

SELF_SHA256: 9ba6c2f510f4e381faf929f6eb56ffa525978bbb71fe06adda08bf55420e7ea0
