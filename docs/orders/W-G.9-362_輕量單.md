# `W-G.9-362`　輕量單：主線快轉（至 `924d916`·`W-G.9-361` 地籍相連之判之座標容差入主線）＋ 地籍相連之判之接線與突變之判別力（`W-G.9-361 §四-2` 之補寫·`F22`）＋ 攢批登記（`自誤 566`·`GB-197` 之立·`GB-195` 之失效）＋ `K-6` 典之註 ＋ 待落地清單之更新 ＋ 主 checkout 之同步

> **本單建議等級 ＝ `high`**（本單⛔ 令 CC 撰寫生產碼；受詞 ＝ 快轉、塊之原封入倉與實跑、四簿之末端追加、主 checkout 之同步）。
> **發單** ＝ 發單側窗六十三·`2026-10-02`。**受單** ＝ CC 新窗（工項零′〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**）。
> **級** ＝ **輕**（本批⛔ 新增生產碼：新量測器 `1` 檔 ＋ `K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md` 之純末端追加 ＋ 報告；工項零′ 之快轉使主線納入已於側支放行之生產碼 `commit` `1` 筆〔`f74f95e`〕·其入主線之放行見 `§二`；本批⛔ 跑 `run_all` 及 `run` 類之量——快轉後主線之生產碼 `34` 檔 ≡ 側支之端，`W-G.9-361R` `V-1‴`〜`V-8‴` 與發單側窗六十三之復驗〔`§一` 項 `4`／`5`〕已跑·KL 令：文件批⛔ 全套驗證儀式）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `caede209cb769fbea2986ffe712e835ff052549b`；側支 `verify/W-G.9-361-k954` ＝ `924d91634b1b36ea1d5fbbffd4a6791693ad3311`（`W-G.9-361` 補令二 工項四‴）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F22`／`K7`／`G6`／`E9`／`P16` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-362_輕量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項四之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F22`）與改動（`K7`／`G6`／`E9`／`P16`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）之一字；既有量測器（含 `F21`）之一字；任何錨之改；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿、`docs/配地計算總規格_v3.md`、恆常附款登記表之一字；`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md` 除塊 `K7`／`G6`／`E9`／`P16` 之純末端追加外之一字；任何側支之推送、刪除或改寫（`verify/W-G.9-361-k954` 留於 `924d916`·⛔ 再推）；`run_all` 之執行。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止；**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零′**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `caede209cb769fbea2986ffe712e835ff052549b`；`git rev-parse origin/verify/W-G.9-361-k954` ＝ `924d91634b1b36ea1d5fbbffd4a6791693ad3311`；`git ls-remote --heads origin` 之列數 ＝ `34`；施工樹 `git checkout --detach origin/verify/W-G.9-361-k954` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 565 557` ⇒ `rc 0`（其「項4′ 四簿·正典框」＝ `W-G.9-361` 收工閘 `7‴` 之值：自誤 `550`／`565`、`GB` `189`／`196`、`VR` `80`／`95`、`K-9` `51`／`54`）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊（**KL 之訊載之**）；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態（側支之端 `924d916`·即快轉後之主線）之 `docs/` 全檔 **`941`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗六十三實跑 `python verify/probes/wg9268_gate6_occupancy.py 924d916 W-G.9-362 W-G.9-361 W-G.9-396`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-362`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-361` | `8`／`29`／`4` | `8`／`29`／`4` | `33` | `11` | `11`／`177` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `11`／`17` | 🟢 宣告框 `0`、鬆框非零（漏框偵察有咬） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `25`／`28` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `924d916` 之追蹤檔 **`2754`** 檔·列框·B 形 ⋀ C 形並取；發單側窗六十三以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``／`-F "GB-<號>"`〕於 `924d916` 實算）：

| 號 | 裸（錨定 `(?<![0-9\-])<號>(?![0-9])`）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 566` | `52` | `0` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——行號、bytes、坐標等·⛔ 為自誤之引用） |
| 對照甲［必非零］`自誤 565` | `41` | `7` | `0` | `7` | 🟢 框非恆空 |
| `GB-197` | `83` | `2` | — | — | 🟢 可取（平形 `2` 列 ＝ `docs/orders/W-G.9-341_重量單.md:36`、`docs/orders/W-G.9-343_重量單.md:35` 之「對照乙［必為零］」所列之未取號·⛔ 占用） |
| 對照甲［必非零］`GB-196` | `311` | `19` | — | — | 🟢 框非恆空 |

自誤 `MAX` ＝ `565`、`GB` `MAX` ＝ `196`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 566`（塊 `E9`）、`GB-197`（塊 `G6`）；⛔ 鑄 `VR`／`K-9`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `caede20`，或側支 `verify/W-G.9-361-k954` ≠ `924d916`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `34` |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 工項零′ 前置之任一期不符 |
| `4` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成 |
| `5` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6` | 塊 `F22`／`K7`／`G6`／`E9`／`P16`／`T1`／`T2` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `7` | 工項一之實跑任一 ≠ 期（尤：必過之態 ≠ `rc 0`、必破之態之末列 ≠ `§一` 項 `6` 之逐字、二態之全文與附錄己之塊 `T1`／`T2` 不逐列相同） |
| `8` | 四簿任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項四：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `11` | 工項零〜三之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `12` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者⛔ 屬之） |
| `13` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗六十三自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `caede209cb769fbea2986ffe712e835ff052549b`；側支 `verify/W-G.9-361-k954` ＝ `924d91634b1b36ea1d5fbbffd4a6791693ad3311`；主線為側支之祖（`git merge-base --is-ancestor` 真；`git rev-list --count caede20..924d916` ＝ `11`、反向 ＝ `0`；`git rev-list --merges caede20..924d916` ＝ 空）；其餘側支 `verify/W-G.9-359-cand` ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`、`verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`34`**（`verify/` `29`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`·二態皆 `34`） | 主線 → 側支之端相異 **`1`** 檔：`app.py` `cae25232047add2dc6703d9b2d1cee50d1601472` → `deaf07f750f40e8badf6cf4c8914e52d45e8d122`（`1639619` → `1647909` B）；`verify/run_verification.py` ＝ `3bd2b378368df204f0c0fca1734d597851e1252b`、`verify/selection_pipeline.py` ＝ `8d38e55013bec51ab81978336fe04e928f5baf98`、`verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`（二態同）；`verify/probes/probe_WG9361_k954.py` ＝ `9f93c3db560ef6350f2843bc2b4d83a8df4fea32`（側支之新檔） |
| `3` | 四簿（側支之端） | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `460072` B；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1027496` B；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `1102666` B；`CLAUDE.md` `321898` B（皆以換行結尾·CR `0`） |
| `4` | `W-G.9-361`（＋ 補令一、二）之復驗（發單側窗六十三·依交接文六十二 `§四-1`·全數自倉重跑） | **十一 `commit` 逐筆對拍**（`c93285b`／`055b31e`／`9935e8c`／`dcd40fe`／`c2d4286`／`b168a3a`／`9c232e7`／`3ae0ce7`／`f74f95e`／`94eb6cf`／`924d916`·線性·合併 `0`·補令二所令之五筆訊息首段逐字）：補令二 ＝ `6b7e5c6d…`（`46634` B）·`SELF_SHA256` `cdbbd813…` 經 `P-5` 自驗相符（補令一 `46619cfc…`、原單 `c1bbdd90…` 亦符）·入倉之 blob ＝ 來源；塊 `F21q`／`K6‴`／`E8‴`／`P15‴` 自倉內之補令二重抽 ＝ 補令二 `§四-1` 項 `2`〜`5`；`F21` ＝ `9f93c3db…`（`33711` B·與交接文六十二之倉外之 `F21_補令二後.py` 逐位同）；四簿之改後 ＝ 開工態 ＋ 塊 `K6′`＋`K6‴`／`G5′`／`E8′`＋`E8‴`／`P15′`＋`P15‴` 逐位（`460072`／`1027496`／`1102666`／`321898` B·CR `0`）；閘 `1‴`〜`5‴` 自倉重算皆符（刪除欄：`055b31e` `0`／`2`／`3`／`2`／`2`、`c2d4286` `12`、工項一‴ `55`／`7`、工項二‴ `app.py` `137`／`1`、餘皆 `0`；生產碼相異 `1`、`verify/` 相異 `5`〔`A` `1`·`M` `4`·blob ＝ 原單 `§五-1` 項 `11` 與 `9f93c3db…`〕、新檔九之 `git check-ignore` `0`；CR `0`〔`18` 檔·`V6.dxf` `12308`〕；heads `34`、主線 `caede20`、八側支⛔ 變、`924d916` 之祖含 `b168a3a` 與 `caede20`）。**逐段讀 `app.py` 之差異**（`git diff 3ae0ce7 f74f95e -- app.py`·`9943` B·`163` 列·`sha256` `9fb5ba80…` ＝ 報告 ⑧ 逐位）：對補令二 `R-2‴`（④‴-0′ 之型之檢以 `geom_type`／`is_empty`·⛔ 恃例外；④″-0〜④″-3；⑤ 之射程）、`R-3‴`、`I-3‴`（新增之模組層函式 `_k954_areal`／`_k954_all_finite`／`_k954_vtx_len` 皆為 `k6_shares_segment` 所直接呼叫）、`X-1‴`、`X-2`〜`X-7` 無偏差；先篩（外接矩形之距 `> ε` ⇒ 略）⛔ 改結果之證成立（去之或放寬至 `2ε` ⇒ `F21` 之例與 `F22` 之 `B` 皆⛔ 轉紅）。**獨立之核**（發單側之式·倉外·`shapely 2.1.2`）：補令二 `§三-1` 所列之九形二向之判 ＝ 界址點之讀法之獨立實作（交接文六十二之 `vtx2.py`）；隨機 `3000` 例（微米錯位·`MultiPolygon` 摻入）之判之相異 `0`、二向之異 `0`。**量測**：前置 `1` 三子命令皆 `rc 1`·末列 ＝ 補令二之期；前置 `1′`（`c2d4286` ＋ 停機上呈二之差異檔 ⇒ `9827066b…`）`selftest` ⇒ `rc 1`·`⇒ 紅 ['A22', 'A23', 'A27']；rc 1`·`P0` `28／28`；`V-1‴` 三子命令皆 `rc 0`，全文與報告 ③ 所嵌逐列同（`P0` `28／28`·`W5` 之相異 ＝ `['K6_SHARE_COORD_TOL', '_k954_all_finite', '_k954_areal', '_k954_vtx_len', 'k6_shares_segment']`·`R0` `19`／`15`）；`V-2‴` `F16`／`F12`／`F13` 之 `run` 之全文與報告所嵌逐列同、`F14 run` `rc 0`、`F3 run` `rc 0`（末列 `⇒ rc 0`）；`V-3‴` `k6s3 run` 段三紀錄 `19`／`0` 列，`cmp`（前置於 `3ae0ce7`）`3.5` ⇒ `rc 1`·相異恰 `11` 項（全文 ＝ 報告逐列）、`0.0` ⇒ `rc 0`·相異 `0` 項；`V-4‴` `F8 run` `0.0` 之 `diff` `0` B，`3.5` 之 `diff` 與 `F10 run` 之 `diff` ＝ 報告逐列；`V-5‴` `parity` 二退縮 `rc 0`·`35`／`34`、`36`／`35`·不符格 `0`·`Z` ＝ `[('harness', 'R1-抵費地-2')]`·末十列 ＝ 報告逐列；`V-6‴` `run_all` 同一倉外路徑（`3ae0ce7` 對 `924d916`·`stderr` 皆 `0` B）·`probe_WG9343_step0_flag.py runall` `rc 0`：項 `64`·PASS `28 → 28`·相異項恰 `#24 v3·G值3.5m`（`FAIL → FAIL`·`295 → 299`）·golden `21／21`·對帳 `22／36 → 22／36`（`diff` `268` 列·其 bytes 平台相依）；`V-7‴` 生產碼相異恰 `app.py`（`deaf07f7…`·`+137`／`-1`）、`verify/` 相異 `0`；`V-8‴` 閘 `8‴` 與原單 `§四-3` 閘 `9`〜`26` 之 `42` 命令（於 `924d916`·其生產碼與 `verify/` ≡ `f74f95e`）皆 `rc 0`（`F21` 三子命令末列 `⇒ 紅 []；rc 0`；`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F4 selftest` `10/10`、`pooltemp selftest` `13/13`、`k6s3 selftest` `9/9`；`F16 selftest` `P0` `25／25`；`F19 mut` 之 `Z0`〜`Z2` 與 `M1`〜`M41` 皆 ✅；`run` 類 `11` 命令與 `V-1‴`〜`V-5‴` 同一實跑；`stderr` 合計 `0` B）。**倉外之核對**（交接文六十二之 `instr_run2.py`·逐呼叫另以界址點之讀法之獨立實作重算並記受詞之型·`f74f95e` 之碼）：`13` 器（`F21 run`、`F16`／`F12`／`F13`／`F14`／`F3` 之 `run`、`k6s3 run` 二、`F8 run` 二、`F10 run`、`parity` 二）：呼叫 `53958` 次、重判 `47341` 次（相連 `632`）、受詞 `107916` 件皆 `Polygon`、判之相異 `0`、二向之異 `0`、重判之長之差之最大者 `1.8e-15` m——諸數與發單側窗六十二於補令一之碼（`9827066b…`）所得逐器同；諸器之出艙與無包裹之實跑逐位同（`k6s3` 之出艙唯其計時欄異）。CC 報告 ①〜⑪ 俱載，其數與自倉所算相符；唯讀獨立審查之發現 `9`（曲線之近切）自倉復現 ⇒ `自誤 566`／`GB-197`——**全數相符** |
| `5` | 快轉之淨效（主線 → 側支之端·本案） | ＝ `W-G.9-361 §一` 項 `6`（KL `2026-09-30 20:34` 已裁接受·`K-9-54`）——**退縮 `0 m`**：配地、段三、末端塊之合併再試、調配之輸入皆⛔ 變（`k6s3 cmp` `0.0` 相異 `0` 項；`F8 run` `0.0` 之出艙逐位同）。**退縮 `3.5 m`**：段三紀錄 `18 → 19` 列；地主甲（`G007`）之公園地 `628-45(3)` 與路口道路 `628-45(4)` 由 `R3`／`R5` 二街廓平分改為 `R3`／`R5`／`R6` 三街廓平分、道路 `628-20(3)` 併入 `R6` 之 `628-20(1)`；應分配面積 `628-45(2)` `950.91 → 902.52`、`628-45(1)` `572.05 → 525.28`、`628-20(1)` `336.56 → 461.06`、`628-18(2)` `213.51 → 212.98`、`628-7(2)` `254.64 → 253.56`；抵費地 `R3` `1834.68 → 1883.03`、`R5` `1694.57 → 1742.99`、`R6` `1901.82 → 1777.33`；街角得標、強制旗標⛔ 變（`k6s3 cmp` `3.5` 相異恰 `11` 項）；調配之輸入：待同歸戶併入之歸戶 `9 → 8`；`run_all` 唯 `#24 v3·G值3.5m` 一項相異（`FAIL → FAIL`·違規數 `295 → 299`）。畫面與 harness 同受（`parity` 二退縮不符格 `0`） |
| `6` | 量測器 `F22`（附錄甲）之二態 | **必過**：`924d916` 之 `app.py`（`deaf07f7…`）與 `F21`（`9f93c3db…`）⇒ **`rc 0`**；本部 `Z0`／`Z1` 皆 ✅（`F21` 之例 `28` 皆 ✅、`B1`〜`B4` 皆 ✅、`W1`〜`W4` 與 `V1`〜`V6` 皆 ✅）；二十一突變 `M1`〜`M21` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`。**必破**：`3ae0ce7d1e3efc74c6ca0a03c1c1bf8cea822527`（`W-G.9-361` 補令二 工項一‴ 之端：其 `F21` ＝ `9f93c3db…`、生產碼 `34` 檔 ≡ `caede20`）⇒ **`rc 1`**；`Z0` ✅、`Z1` 🔴（受詞缺、`A4`、`A8`、`A10`、`A12`、`A20`〜`A23`、`A27`、`B2`、`B4`、`W1`〜`W3`、`V1`〜`V6`）、⛔ 施突變；末列逐字 `⇒ 紅 ['Z1']；rc 1`。二態之全文 ＝ 附錄己之塊 `T1`／`T2`。🔒 **第三態**（發單側之佐證·⛔ 為 CC 之期·倉內無其 `commit`）：`c2d4286` 之上施 `docs/reports/W-G.9-361R_補令一_工項二_app差異.diff` 而得之 `app.py`（`9827066b…`·`W-G.9-361` 補令一之工項二″）＋ `F21`（`9f93c3db…`）⇒ `rc 1`，`Z1` 之紅 ＝ `['A22', 'A23', 'A27', 'B2', 'V1', 'V2', 'V3', 'V6']`（補令二之三例 ＋ 含洞之 `MultiPolygon` ＋ 補令二之字樣）。🔒 **等價之突變⛔ 入**：先篩從寬（外接矩形之距之閾 `tol → 2·tol`）或去之——先篩唯省計算、⛔ 改結果（`W-G.9-361R` `⑦-2`）⇒ 無例可使之轉紅 ⇒ ⛔ 入 `F22` |
| `7` | KL 主 checkout（倉外之物·發單側⛔ 實查） | 依 `W-G.9-360` 工項四 ＝ `wip/s1-endpart` 之 `caede20`（`W-G.9-361` ⛔ 動之）；其根或有 `W-G.9-361` 之來源檔（原單、補令一、補令二·未追蹤·`W-G.9-361` 補令二 `§四-2` 項 `3` 令 KL 自行移除）⇒ 依工項四之撞檔前置處置 |

---

## `§二`　KL 之語與射程

🔒 **所據**：`W-G.9-361 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之精確先、重判後；`R-2` ④ 之二向取小、相距之先篩；`R-2` ⑤ 之例外 ⇒ 不相連）及其突變之判別力；併入主線之請示（有土地後果·`K-9-54` 已裁接受·附畫面之核對）。」——接線與行為已由 `F21` 之 `wiring`（`W1`〜`W5`）與 `selftest`（`A1`〜`A27`）量之；本單之 `F22` 補 (一) 以 CC 之碼之字樣為錨之接線 `V1`〜`V6`（精確先、重判後；型之檢與有限性之檢先於相距；四長取小；Hausdorff 之四端；片之環；例外 ⇒ 不相連）、(二) `F21` 之例未及之行為 `B1`〜`B4`（例外 ⇒ 不相連；含洞之 `MultiPolygon`；洞之坐標非有限；長 `0` 之邊）、(三) 二十一突變之判別力。CC 之唯讀獨立審查之發現 `9`（`W-G.9-361R` `⑥-2`·歸 (C)）自倉復現 ⇒ `自誤 566`（塊 `E9`）、`GB-197`（塊 `G6`·另單）、`K-6` 典之 `🔧` 註（塊 `K7`）。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：發單側窗六十三於對話呈下列之問一。CC 端之放行：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項零′（主線快轉）與工項四（主 checkout 之同步）之放行，CC 將其逐字載入報告；**無之 ⇒ 工項零′ 之前置畢後停於快轉前，於對話請示 KL**。所答之【要你判斷】逐字 ＝ 問一之【要你判斷】。問一（發單側所呈·【現況】至【要你判斷】逐字）：

> 【現況】361 做的是您 9/30 所裁的 `K-9-54`：兩筆土地的界線座標相差在 0.1 mm 以內者，視為共用同一段界線（相連）；程式並依工程上的補充，以界址點逐段比對，「一筆存成兩塊」的土地也一體適用。本窗已全數重跑復驗，結果與 CC 之報告一致；目前只在側支，主線與您本機介面仍是 360 之狀態。
> 【要改成】在 362 一併辦理：主線推進到側支之最新狀態，補入相連之判的突變檢查與登記，並同步您本機的程式資料夾。
> 【對土地的影響】與您 9/30 所接受者相同：退縮 0 m 之配地、街角、抵費地皆不變。退縮 3.5 m：地主甲的公園地 628-45(3)（273.09 ㎡）與路口道路 628-45(4)（224.60 ㎡）由 R3、R5 兩街廓平分改為 R3、R5、R6 三街廓平分，道路 628-20(3)（42.15 ㎡）併入 R6 之 628-20(1)；抵費地 R3 1834.68 → 1883.03 ㎡、R5 1694.57 → 1742.99 ㎡、R6 1901.82 → 1777.33 ㎡；街角不變。同步後，您可於退縮 3.5 m 按「🧮 執行 G 值迭代計算」，核對 R3、R5、R6 之抵費地為上列新值。
> 【要你判斷】是否同意將 361 併入主線，並請 CC 同步您本機的程式資料夾（併於 362 辦理）？（是／否）

🔒 **逐筆放行清單**（`恆常附款 y`·擬本單時自倉重導）：母體 ＝ `git rev-list caede20..924d916` ＝ **`11`** 筆；判準 ＝ 是否改動生產碼 `34` 檔之任一（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）。動生產碼者 **`1`** 筆（其餘 `10` 筆皆單、補令、停機上呈、量測器、入典與登記、報告）：

| `commit` | 訊息首段 | 所動之生產碼 | 側支之放行 | 本案之土地後果 |
|---|---|---|---|---|
| `f74f95e2cda03aff98ca96c9594b3285b6ec1db2` | `W-G.9-361 補令二 工項二‴：地籍相連之判之座標容差（K-9-54·GB-195·界址點之讀法·片之多邊形部分）🔴 生產碼（新側支）` | `app.py` | `W-G.9-361 §二`（原單）·補令一·補令二 | `§一` 項 `5`（`K-9-54`·KL 已裁接受；`W-G.9-361R` `V-2‴`〜`V-6‴`；發單側窗六十三自倉重跑 ＝ `§一` 項 `4`） |

🛑 **射程**：`(a)` 主線快轉至 `924d91634b1b36ea1d5fbbffd4a6791693ad3311`（工項零′·**以前置皆符且本節之放行成立為條件**）；`(b)` 工項零〜三（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項四於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、既有量測器、任何他錨、`VR` 簿；`(e)` ⛔ 及 `GB-196`（讀入時之坐標有限性之閘）、`GB-197`（曲線之近切）之修正、規格步 `4`（`K-9-53`）、畫面批——另單。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存倉外之目錄 `<O>`）：
1. `git merge-base --is-ancestor caede209cb769fbea2986ffe712e835ff052549b 924d91634b1b36ea1d5fbbffd4a6791693ad3311` ⇒ `rc 0`；`git rev-list --count caede20..924d916` ＝ `11`；`git rev-list --count 924d916..caede20` ＝ `0`。
2. `git diff --name-only caede20 924d916 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `1` 列：`app.py`（`§一` 項 `2`·🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 之檔）；`git rev-parse 924d916:app.py` ＝ `deaf07f750f40e8badf6cf4c8914e52d45e8d122`。
3. `git rev-list caede20..924d916` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `commit`（全 `40` 碼·命中 `1` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3`·⛔ 快轉。

**快轉**（前置皆符且 `§二` 之放行成立後·與前置為分開之呼叫）：

```
git push origin 924d91634b1b36ea1d5fbbffd4a6791693ad3311:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4`）；⛔ 改目標值（逐字 `924d91634b1b36ea1d5fbbffd4a6791693ad3311`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-361-k954`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `924d91634b1b36ea1d5fbbffd4a6791693ad3311`；
② 遠端 heads ＝ **`34`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `924d916` 之相異 ＝ **`0`**；判別力［必非零］：vs `caede20` 之相異 ＝ **`1`**（`app.py`）；
④ `git branch -r --contains f74f95e2cda03aff98ca96c9594b3285b6ec1db2` 含 `origin/wip/s1-endpart`。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `924d916…` 方續工項零。

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-362_輕量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-362 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F22` 入倉與實跑（主線·零生產碼）

1. 塊 `F22`（附錄甲）依圍欄之逐列索引抽出、對拍 `§五-1` 項 `2` 後，以二進位寫為 `verify/probes/probe_WG9362_k954_mut.py`（**新檔**）；`git check-ignore` 之⛔ 命中。
2. **必過之態**（施工樹·其 `app.py` ＝ `deaf07f7…`、`verify/probes/probe_WG9361_k954.py` ＝ `9f93c3db…`）：`python verify/probes/probe_WG9362_k954_mut.py mut <repo> > <O>\f22_pass.log` ⇒ **`rc 0`**；本部 `Z0`／`Z1` 皆 ✅；二十一突變 `M1`〜`M21` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`；全文與附錄己之塊 `T1` 逐列相同（比對前去 CR 及列尾空白）。🔒 本器唯讀、⛔ 寫檔（突變施於記憶體中之 `app.py` 之文字·以 `verify/app_harvest.py` 之 `_install_fake_streamlit`／`_filter_module` 於記憶體中 harvest）；發單側本機全程 `92` 秒。
3. **必破之態**：`git worktree add --detach <P> 3ae0ce7d1e3efc74c6ca0a03c1c1bf8cea822527`（`W-G.9-361` 補令二 工項一‴ 之端·`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑）；於施工樹 `python verify/probes/probe_WG9362_k954_mut.py mut <P> > <O>\f22_break.log` ⇒ **`rc 1`**，末列逐字 ＝ `§一` 項 `6` 之必破之末列；全文與附錄己之塊 `T2` 逐列相同（同上）；跑畢 `git worktree remove --force <P>`。

任一 ≠ 期 ⇒ 停機款 `7`（⛔ 改器）。`commit` 訊息逐字 `W-G.9-362 工項一：量測器 F22（地籍相連之判之接線與突變之判別力）入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　攢批登記、`K-6` 典之註與待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `K7`（附錄乙）附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `G6`（附錄丙）附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；塊 `E9`（附錄丁）附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P16`（附錄戊）附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-362 工項二：攢批登記（自誤 566·GB-197 之立·GB-195 之失效）＋ K-6 典之註 ＋ 待落地清單之更新（W-G.9-361 入主線 ＋ 突變之判別力）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-362R_入主線與地籍相連之判之突變_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ 工項一之二態之全文（`f22_pass.log`／`f22_break.log`）；⑤ 五塊之實得（bytes／`sha256`）與四簿之改前改後 bytes；⑥ `§二` 之放行（KL 之逐字或請示之經過）；⑦ CC 之自捕與自解；⑧ 各段耗時。收工閘之實測值與工項四之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-362 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項三 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `deaf07f750f40e8badf6cf4c8914e52d45e8d122`；`git -C <主 checkout> hash-object verify/probes/probe_WG9361_k954.py` ＝ `9f93c3db560ef6350f2843bc2b4d83a8df4fea32`；`git -C <主 checkout> hash-object verify/probes/probe_WG9362_k954_mut.py` ＝ `ca5f08f517dbd7c534bb8816e07dd7d90f8989b3`；`git -C <主 checkout> hash-object verify/run_verification.py` ＝ `3bd2b378368df204f0c0fca1734d597851e1252b`。

任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之刪除欄 | 逐檔 **`0`** |
| `2` | 生產碼 `34` 檔 | 對 `924d916` 相異 **`0`**；判別力［必非零］：對 `caede20` 相異 **`1`**（`app.py`）；`verify/` 之一切檔對 `924d916` 相異恰 **`1`**（新檔 `verify/probes/probe_WG9362_k954_mut.py`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`7` 檔：本單、`F22`、`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md`、報告） |
| `4` | 四簿之 bytes | `K-6` 典 `460072` → **`461677`**；`GB` 簿 `1027496` → **`1030740`**；自誤簿 `1102666` → **`1105341`**；`CLAUDE.md` `321898` → **`324396`**；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`34`**；主線 ＝ 工項三之 `commit`，其祖含 `924d916`；`verify/W-G.9-361-k954` ＝ `924d916…`；`verify/W-G.9-359-cand` ＝ `bd072eb…`、`verify/W-G.9-357-k948` ＝ `4716f20…`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 566 565 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 566 565` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`551`**／`MAX` **`566`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；**`GB` `190`／`197`**／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `51`／`54`／`[44, 47]`（`VR`／`K-9` 皆 ＝ 開工態；自誤唯增 `566`、`GB` 唯增 `197`） |
| `8` | `python verify/probes/probe_WG9362_k954_mut.py mut <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9361_k954.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑> caede20`；`python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>`；`python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | 皆 **`rc 0`**；`F21` 二子命令之末列逐字 `⇒ 紅 []；rc 0`（`selftest` 之 `P0` `28／28`）；`wfns_ast` 末列 **`48`／`48`／`47`**；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零′〜三（快轉 ＋ 本單 ＋ 塊 `F22` ＋ 塊 `K7`／`G6`／`E9`／`P16` ＋ 報告之替身）並實跑閘 `1`〜`9` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `F22` | `18914` B·`sha256` `4bf85485e1ef8953d44e03b7a9b55b32f0fab08d6859719d9af2c2e2a871bd16`·`352` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9362_k954_mut.py`（blob `ca5f08f517dbd7c534bb8816e07dd7d90f8989b3`） |
| `3` | 塊 `K7` | `1605` B·`sha256` `d7a089ed876ea29a7963707c1030a438857f678222bf0cee6fdf578ca5db953b`·`8` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`460072` B）之末後，期末 ＝ `461677` B |
| `4` | 塊 `G6` | `3244` B·`sha256` `f10ef64df14442362459d1a5169b606e308d6675a8484c3521787fcba0926eaf`·`19` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1027496` B）之末後，期末 ＝ `1030740` B |
| `5` | 塊 `E9` | `2675` B·`sha256` `07ef19f80ba511d9139e9e5b857ccafb87f534d61efe6361ab871e085c8e84fc`·`12` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1102666` B）之末後，期末 ＝ `1105341` B |
| `6` | 塊 `P16` | `2498` B·`sha256` `7a83bd87a7fa7578a2b9910325beddf22320a98f0a4dc5e6999e2696e6d81d0c`·`20` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`321898` B）之末後，期末 ＝ `324396` B |
| `7` | 附錄己之塊 `T1`／`T2`（工項一之二態之出艙·發單側實跑） | `T1` `5743` B·`sha256` `8ea9014600d27ace3e33cd2b9ec4815a55b6eff03e04cf701d48e3246dfb5c13`·`72` 列（圍欄內全文·末附換行）；`T2` `4681` B·`sha256` `7339c76ce28444f101397e25856ffeebacf086214f7bfef35358514b6a1068f7`·`50` 列（圍欄內全文·末附換行）（圍欄內全文·末附換行；比對時去 CR 及列尾空白） |
| `8` | 本單所載 KL 之語 | `§二` 之問一，發單側窗六十三於對話所呈（KL 之答 ＝ 貼本單之同一訊息） |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗六十三實跑（態 `924d916`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-4` `:168`（`§四` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `924d916` 至工項二之端〔四簿之 bytes〕，表內自載 ⇒ **具名豁免**）、`P-4` `:651`／`:728`（附錄己塊 `T1`／`T2`·所觸之箭頭係 `F22` 之 `V2` 之名所載之檢之先後〔`k6_shares_segment` 內之序〕、⛔ 為方向性轉引 ⇒ **具名豁免**）、`P-6` `:641`（附錄戊塊 `P16` 內「前開……節之序 `5`」列·所觸之數係待落地表之序號、⛔ 為實測之數 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `20442`–`28162`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux） | `git worktree add --detach <S> 924d916`（拋棄式·⛔ `push`·即快轉後之主線）＋ 本單 ＋ 塊 `F22` ＋ 塊 `K7`／`G6`／`E9`／`P16` ＋ 報告之替身·四 `commit`（訊息 ＝ `§三` 所令逐字）：工項零′ 前置 `1`〜`3` 皆符（`11`／`0`；`:(glob)` 形恰 `1` 列〔無之則 `6` 列〕；逐筆判命中者恰 `f74f95e`〔`1` 列〕）；七塊之抽取與附錄逐位同；工項一二態 `rc 0`／`rc 1`、全文與塊 `T1`／`T2` 逐位同（去 CR 及列尾空白·`stderr` `0` B）；閘 `1` 各檔之刪除欄皆 `0`（`F22` `352`／`0`、`K-6` 典 `8`／`0`、`GB` 簿 `19`／`0`、自誤簿 `12`／`0`、`CLAUDE.md` `20`／`0`、本單與報告之替身唯增）；閘 `2` 對 `924d916` 相異 `0`、對 `caede20` `1`、`verify/` 相異恰 `1`（`A`）；閘 `3` CR `0`（`7` 檔·`V6.dxf` `12308`）；閘 `4` 四簿皆嚴格前綴、其末 ＝ 本表項 `3`〜`6`；閘 `5` 之祖含 `924d916`；閘 `6`〜`9` 皆 `rc 0`（閘 `6` 二閘皆過；閘 `7` 四簿 ＝ 自誤 `551`／`566`、`GB` `190`／`197`、`VR` `80`／`95`、`K-9` `51`／`54`／`[44, 47]`；閘 `8` 末列 `⇒ 紅 []；rc 0`；閘 `9` `F21` 二子命令末列 `⇒ 紅 []；rc 0`〔`P0` `28／28`〕、`wfns_ast` `48`／`48`／`47`、`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」）；新檔三之 `git check-ignore` 皆無命中 |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````markdown `` 或 `` ````text ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零′ ⇒ 依 `§二` 之放行、前置皆符後推主線；工項零〜三 ⇒ 逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）。
3. 收工後，主 checkout 之根之來源檔（本單、`W-G.9-361` 之原單、補令一、補令二，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F22`（新檔 `verify/probes/probe_WG9362_k954_mut.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-362 量測器（發單側窗六十三擬·檔 F22·⛔ 由受單側改一字）：地籍相連之判之座標容差（`W-G.9-361` ＋ 補令一、二·
`K-9-54`）之以程式字樣為錨之接線檢查與突變——量測器 `F21`（`verify/probes/probe_WG9361_k954.py`）之判別力。

緣由：`W-G.9-361 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之精確先、
重判後；`R-2` ④ 之二向取小、相距之先篩；`R-2` ⑤ 之例外 ⇒ 不相連）及其突變之判別力」；補令一、二所增之 ④″-0〜④″-3、④‴-0′
（型之檢·⛔ 恃例外）、片之環（各多邊形部分之 exterior 與 interiors）、Hausdorff 之四端，一併及之。接線與行為已由 `F21` 之
`wiring`（`W1`〜`W5`）與 `selftest`（`A1`〜`A27`·`28` 例）量之；本器補 (一) 以 CC 之碼（`f74f95e`·`app.py` blob
`deaf07f7…`）之字樣為錨之接線（`V1`〜`V6`）、(二) `F21` 之例未及之行為（`B1`〜`B4`）、(三) 其判別力：於記憶體中對工作樹之
`app.py` 之文字施以字樣為錨之突變（⛔ 寫檔、⛔ 符號連結），以 `F21` 之判式（`_cases`／`_report`／`_wiring_checks`）與本器之
`V`／`B` 量之。

子命令（一律 python verify/probes/probe_WG9362_k954_mut.py mut <repo>）：
  本部
    Z0  受詞在：<repo>/verify/probes/probe_WG9361_k954.py 可載，其 _cases／_report／_wiring_checks／FUNCS／CONSTS 皆在；
        <repo>/verify/app_harvest.py 之 _install_fake_streamlit／_filter_module 皆在；<repo>/app.py 可讀。
    Z1  未突變之態全綠：`F21` 之例（於記憶體中 harvest 之 app.py）皆 ✅（`28` 例）；`F21` 之 W1〜W4 皆 ✅；本器之
        V1〜V6、B1〜B4 皆 ✅。
  接線（字樣·各錨於其函式之源須恰命中 `1`）
    V1  精確先、重判後：k6_shares_segment 內 `_it = _ba.intersection(_bb)` → `if _tot >= _ml: return (True, _tot)` →
        `_tol = float(K6_SHARE_COORD_TOL)` → `try:` 之序。
    V2  重判之序（④‴-0′ → ④″-0 → ④″-1 → ④″-2 → ⑤ → ④″-3）：型之檢（`_k954_areal`·任一為 None ⇒ (False, _tot)）→
        有限性之檢（`_k954_all_finite`）→ 相距（`poly_a.distance(poly_b) > _tol`）→ `_k954_vtx_len` →
        `except Exception: return (False, _tot)` → `if _l >= _ml: return (True, _l)` → `return (False, _tot)`。
    V3  型之檢（④‴-0′·⛔ 恃例外）：`_k954_areal` 以 `geom_type` 屬 ('Polygon', 'MultiPolygon') 與 `is_empty` 判之，
        其內⛔ try。
    V4  四長取小：`_k954_vtx_len` 以二軸（`_axis(_SA, _SB)`、`_axis(_SB, _SA)`）得四長，回其最小者。
    V5  Hausdorff 之四端：`_h` ＝ s′ 之二端至 t′、t′ 之二端至 s′ 之距之最大者；`_h <= tol` 者計入。
    V6  片之環：`_k954_all_finite` 與 `_k954_vtx_len` 皆逐多邊形部分取 `[exterior] + interiors`。
  行為（`F21` 之例未及者·合成·⛔ 本案資料）
    B1  ④″-2 之運算拋例外（平方下溢之極短邊 ⇒ ZeroDivisionError）⇒ (False, 精確之長〔此形 1e-05〕)（⑤·⛔ 靜默改判相連）。
    B2  含洞之 MultiPolygon：洞之環與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 4。
    B3  MultiPolygon 之一部之洞之坐標含 NaN、其外環與他片微米錯位而共線 ⇒ 二向皆不相連（④″-0 及於 interiors）。
    B4  片之環含重複之相鄰頂點（長 0 之邊）、與他片微米錯位而共線 ⇒ 相連、其長 ≈ 1（長 0 之邊略）。
  判別力：本部全綠時另施 `21` 種突變（_muts），每一突變須使其所指之項轉紅（所指 ⊆ 轉紅）；突變之錨於 app.py 須恰命中 `1`。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import ast, contextlib, importlib.util, io, math, os, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FA = "app.py"
F21_REL = "verify/probes/probe_WG9361_k954.py"
NEED21 = ("_cases", "_report", "_wiring_checks", "FUNCS", "CONSTS")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


def _load(repo, rel, name):
    p = os.path.join(repo, *rel.split("/"))
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _harvest_src(ah, src):
    """app_harvest.harvest 之記憶體版（同其 _install_fake_streamlit／_filter_module·⛔ 快取·⛔ 寫檔）。"""
    with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ah._install_fake_streamlit()
        mod, _, _ = ah._filter_module(src)
        ns = {"__name__": "app_harvested_f22", "__file__": "<app.py:f22>"}
        exec(compile(mod, "<app.py:f22>", "exec"), ns)
    return ns


def _seg(src, name):
    tree = ast.parse(src)
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
    if len(fns) != 1:
        return None, None
    return ast.get_source_segment(src, fns[0]) or "", fns[0]


# ── 接線（字樣）──
_V1 = ["_it = _ba.intersection(_bb)",
       "    if _tot >= _ml:\n        return (True, _tot)",
       "    _tol = float(K6_SHARE_COORD_TOL)",
       "    try:\n        _pa, _pb = _k954_areal(poly_a), _k954_areal(poly_b)"]
_V2 = ["        _pa, _pb = _k954_areal(poly_a), _k954_areal(poly_b)\n        if _pa is None or _pb is None:\n"
       "            return (False, _tot)",
       "        if not (_k954_all_finite(_pa) and _k954_all_finite(_pb)):\n            return (False, _tot)",
       "        if poly_a.distance(poly_b) > _tol:\n            return (False, _tot)",
       "        _l = _k954_vtx_len(_pa, _pb, _tol)",
       "    except Exception:\n        return (False, _tot)",
       "    if _l >= _ml:\n        return (True, _l)\n    return (False, _tot)"]
_V4 = ["    _la_a, _lb_a = _axis(_SA, _SB)", "    _lb_b, _la_b = _axis(_SB, _SA)",
       "    return min(_la_a, _lb_a, _lb_b, _la_b)"]
_V5 = ["                _h = max(_pt_seg(_s0[0], _s0[1], _t0, _t1), _pt_seg(_s1[0], _s1[1], _t0, _t1),\n"
       "                         _pt_seg(_t0[0], _t0[1], _s0, _s1), _pt_seg(_t1[0], _t1[1], _s0, _s1))",
       "                if _h <= tol:"]
_RING = "for _r in [_q.exterior] + list(_q.interiors):"


def _ordered(seg, anchors):
    """各錨恰命中 1 且依序 ⇒ (True, 位置)；否則 (False, 註)。"""
    pos = []
    for a in anchors:
        n = seg.count(a)
        if n != 1:
            return False, f"錨命中 {n}：{a.strip().splitlines()[0][:40]!r}"
        pos.append(seg.find(a))
    return pos == sorted(pos), f"位置 {pos}"


def _wiring_v(src):
    chk = []
    seg, _ = _seg(src, "k6_shares_segment")
    if seg is None:
        return [(f"V{i} k6_shares_segment 缺", False, "") for i in range(1, 7)]
    ok, note = _ordered(seg, _V1)
    chk.append(("V1 精確先、重判後", ok, note))
    ok, note = _ordered(seg, _V2)
    chk.append(("V2 重判之序（型之檢 → 有限性 → 相距 → 界址點之共線長 → 例外 ⇒ 不相連 → 門檻）", ok, note))
    s3, f3 = _seg(src, "_k954_areal")
    ok3, n3 = False, "無 _k954_areal"
    if s3 is not None:
        has_try = any(isinstance(x, ast.Try) for x in ast.walk(f3))
        ok3 = (s3.count("('Polygon', 'MultiPolygon')") == 1 and "geom_type" in s3 and "is_empty" in s3
               and not has_try)
        n3 = f"try {has_try}"
    chk.append(("V3 型之檢以 geom_type／is_empty（⛔ 恃例外）", ok3, n3))
    s4, _ = _seg(src, "_k954_vtx_len")
    ok4, n4 = (False, "無 _k954_vtx_len") if s4 is None else _ordered(s4, _V4)
    chk.append(("V4 四長取小（二軸 × 二片）", ok4, n4))
    ok5, n5 = (False, "無 _k954_vtx_len") if s4 is None else _ordered(s4, _V5)
    chk.append(("V5 Hausdorff 之四端", ok5, n5))
    s6, _ = _seg(src, "_k954_all_finite")
    n_fin = -1 if s6 is None else s6.count(_RING) + s6.count("    for _q in parts:\n")
    n_edg = -1 if s4 is None else s4.count(_RING) + s4.count("        for _q in _parts:\n")
    chk.append(("V6 片之環 ＝ 各多邊形部分之 exterior 與 interiors（有限性之檢、邊）", n_fin == 2 and n_edg == 2,
                f"有限性 {n_fin}／邊 {n_edg}（期 2／2）"))
    return chk


# ── 行為（合成·⛔ 本案資料）──
def _bt(res, nd=3):
    return (bool(res[0]), round(float(res[1]), nd))


def _cases_b(ns):
    from shapely.geometry import Polygon, MultiPolygon
    sh = ns["k6_shares_segment"]
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__)
        out.append((name, got, exp))

    # B1：極短邊（長 1e-170·其平方下溢為 0）⇒ ZeroDivisionError ⇒ ⑤
    a1 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0.5), (1e-170, 0.5)])
    b1 = Polygon([(1 + 1e-5, 0), (2, 0), (2, 1), (1 - 1e-5, 1)])
    run("B1 ④″-2 之運算拋例外（平方下溢之極短邊）⇒ 二向皆 (False, 精確之長)",
        lambda: (_bt(sh(a1, b1), 6), _bt(sh(b1, a1), 6)), ((False, 1e-05), (False, 1e-05)))
    # B2：含洞之 MultiPolygon，洞之上緣與他片之上緣微米錯位而共線（共線長 4）
    hole = Polygon([(0, 0), (10, 0), (10, -5), (0, -5)], [[(2, -1), (8, -1), (8, -4), (2, -4)]])
    far = Polygon([(20, 0), (25, 0), (25, -5), (20, -5)])
    mp2 = MultiPolygon([hole, far])
    inner = Polygon([(3, -1 - 1e-5), (7, -1 + 1e-5), (7, -3), (3, -3)])
    run("B2 含洞之 MultiPolygon：洞之環與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 4",
        lambda: (_bt(sh(mp2, inner)), _bt(sh(inner, mp2))), ((True, 4.0), (True, 4.0)))
    # B3：MultiPolygon 之一部之洞含 NaN；他部之外環與他片微米錯位而共線
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        bad = Polygon([(20, 0), (25, 0), (25, -5), (20, -5)], [[(21, -1), (22, -1), (float("nan"), -2), (21, -2)]])
        mp3 = MultiPolygon([Polygon([(0, 0), (1, 0), (1, -1), (0, -1)]), bad])
    nb3 = Polygon([(0, 1e-5), (1, -1e-5), (1, 1), (0, 1)])
    run("B3 MultiPolygon 之一部之洞之坐標含 NaN（他部之外環微米錯位而共線）⇒ 二向皆不相連",
        lambda: (bool(sh(mp3, nb3)[0]), bool(sh(nb3, mp3)[0])), (False, False))
    # B4：重複之相鄰頂點（長 0 之邊）
    a4 = Polygon([(0, 0), (1, 0), (1, 0), (1, 1), (0, 1)])
    b4 = Polygon([(0, -1), (1, -1), (1, 1e-5), (0, -1e-5)])
    run("B4 片之環含重複之相鄰頂點、與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 1",
        lambda: (_bt(sh(a4, b4)), _bt(sh(b4, a4))), ((True, 1.0), (True, 1.0)))
    return out


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def _all_red(f21, ah, src, verbose=False):
    red = []
    try:
        ns = _harvest_src(ah, src)
    except Exception as ex:  # noqa: BLE001
        return [f"harvest:{type(ex).__name__}"]
    miss = [n for n in list(f21.FUNCS) + list(f21.CONSTS) if n not in ns]
    if miss:
        red.append("受詞缺")
    if not [n for n in miss if n in f21.FUNCS]:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cases = f21._cases(ns)
        if verbose:
            print("── F21 之例（記憶體中 harvest 之 app.py）──")
        red += f21._report(cases, verbose=verbose)
        if verbose:
            print(f"  （{len(cases)} 例）")
        if verbose:
            print("── 本器之行為（B）──")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            red += _report(_cases_b(ns), verbose=verbose)
    try:
        w21 = f21._wiring_checks(src, None)
    except Exception as ex:  # noqa: BLE001
        w21 = [(f"W:{type(ex).__name__}", False, "")]
    wv = _wiring_v(src)
    if verbose:
        print("── F21 之接線（W1〜W4）與本器之接線（V1〜V6）──")
        for name, ok, note in w21 + wv:
            print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
    red += [n.split()[0] for n, ok, _ in w21 + wv if not ok]
    return red


# ── 突變 ── 各為 (名, 所指之項, [(錨, 代)])
_EARLY = "    if _tot >= _ml:\n        return (True, _tot)          # 精確之長達門檻 ⇒ 相連·其長 ＝ 精確之長（同本批前）\n"
_TYPE = "        if _pa is None or _pb is None:\n            return (False, _tot)\n"
_FIN = "        if not (_k954_all_finite(_pa) and _k954_all_finite(_pb)):\n            return (False, _tot)\n"
_DIST = "        if poly_a.distance(poly_b) > _tol:\n            return (False, _tot)\n"
_AREAL = ("    _gt = getattr(poly, 'geom_type', None)\n    if _gt not in ('Polygon', 'MultiPolygon') or poly.is_empty:\n"
          "        return None\n    return [poly] if _gt == 'Polygon' else list(poly.geoms)\n")
_FIN_LOOP = ("    for _q in parts:\n        for _r in [_q.exterior] + list(_q.interiors):\n"
             "            for _c in _r.coords:\n")
_EDG_LOOP = ("        for _q in _parts:\n            for _r in [_q.exterior] + list(_q.interiors):\n"
             "                _cs = [(float(_c[0]), float(_c[1])) for _c in _r.coords]\n")
_H4 = _V5[0]
_H2 = "                _h = max(_pt_seg(_s0[0], _s0[1], _t0, _t1), _pt_seg(_s1[0], _s1[1], _t0, _t1))"
_PRE = "                if (_gx * _gx + _gy * _gy) ** 0.5 > tol:\n                    continue\n"
_EXC = "    except Exception:\n        return (False, _tot)\n    if _l >= _ml:\n"
_TAIL = "    if _l >= _ml:\n        return (True, _l)\n    return (False, _tot)\n"


def _muts():
    return [
        ("M1 去精確之判之早返（一律重判）", ["V1"], [(_EARLY, "")]),
        ("M2 型之檢改恃例外", ["V3"],
         [(_AREAL, "    return [poly] if poly.geom_type == 'Polygon' else list(poly.geoms)\n")]),
        ("M3 去型之檢之判（None ⇒ 例外）", ["V2"], [(_TYPE, "")]),
        ("M4 去有限性之檢", ["A19", "A24", "V2"], [(_FIN, "")]),
        ("M5 有限性之檢唯及第一部", ["A24", "V6"],
         [(_FIN_LOOP, _FIN_LOOP.replace("    for _q in parts:\n", "    for _q in parts[:1]:\n"))]),
        ("M6 有限性之檢唯及 exterior", ["B3", "V6"],
         [(_FIN_LOOP, _FIN_LOOP.replace("[_q.exterior] + list(_q.interiors)", "[_q.exterior]"))]),
        ("M7 去相距之檢", ["V2"], [(_DIST, "")]),
        ("M8 相距之檢先於型之檢與有限性之檢", ["V2"],
         [(_TYPE + _FIN + _DIST, _DIST + _TYPE + _FIN)]),
        ("M9 邊唯取第一部", ["A23", "V6"],
         [(_EDG_LOOP, _EDG_LOOP.replace("        for _q in _parts:\n", "        for _q in _parts[:1]:\n"))]),
        ("M10 邊唯取 exterior", ["B2", "V6"],
         [(_EDG_LOOP, _EDG_LOOP.replace("[_q.exterior] + list(_q.interiors)", "[_q.exterior]"))]),
        ("M11 長 0 之邊⛔ 略", ["B4"],
         [("                    if _cs[_i] != _cs[_i + 1]:\n", "                    if True:\n")]),
        ("M12 四長取大", ["V4"],
         [("    return min(_la_a, _lb_a, _lb_b, _la_b)", "    return max(_la_a, _lb_a, _lb_b, _la_b)")]),
        ("M13 唯一軸（二長取小）", ["V4"],
         [("    return min(_la_a, _lb_a, _lb_b, _la_b)", "    return min(_la_a, _lb_a)")]),
        ("M14 Hausdorff 唯 s′ 之二端", ["V5"], [(_H4, _H2)]),
        ("M15 H 之門檻減半", ["A21", "V5"],
         [("                if _h <= tol:\n", "                if _h <= tol / 2:\n")]),
        ("M16 先篩過嚴（外接矩形相離即略）", ["A27"], [(_PRE, _PRE.replace("> tol:", "> 0.0:"))]),
        ("M17 例外 ⇒ 相連", ["B1", "V2"],
         [(_EXC, "    except Exception:\n        return (True, _tot)\n    if _l >= _ml:\n")]),
        ("M18 重判相連而回精確之長", ["A4", "V2"],
         [(_TAIL, "    if _l >= _ml:\n        return (True, _tot)\n    return (False, _tot)\n")]),
        ("M19 重判不相連而回界址點之共線長", ["A6", "V2"],
         [(_TAIL, "    if _l >= _ml:\n        return (True, _l)\n    return (False, _l)\n")]),
        ("M20 容差以字面", ["W2", "W3", "V1"],
         [("    _tol = float(K6_SHARE_COORD_TOL)\n", "    _tol = 0.0001\n")]),
        ("M21 相距之檢之容差改 0", ["A27", "V2"],
         [(_DIST, _DIST.replace("> _tol:", "> 0.0:"))]),
    ]


def mut(repo):
    red = []
    print("── 本部 ──")
    try:
        src = _read(repo, FA)
        f21 = _load(repo, F21_REL, "probe_WG9361_k954_for_f22")
        sys.path.insert(0, os.path.join(repo, "verify"))
        ah = _load(repo, "verify/app_harvest.py", "app_harvest_for_f22")
        miss = [n for n in NEED21 if not hasattr(f21, n)] + \
               [n for n in ("_install_fake_streamlit", "_filter_module") if not hasattr(ah, n)]
    except Exception as ex:  # noqa: BLE001
        print(f"  🔴 Z0 受詞缺：{type(ex).__name__}: {ex}")
        print("⇒ 紅 ['Z0']；rc 1")
        return 1
    if miss:
        print(f"  🔴 Z0 受詞缺：{miss}")
        print("⇒ 紅 ['Z0']；rc 1")
        return 1
    print("  ✅ Z0 受詞在（F21 之判式、app_harvest 之二函式、app.py）")
    base = _all_red(f21, ah, src, verbose=True)
    ok1 = not base
    print(("  ✅" if ok1 else "  🔴") + f" Z1 未突變之態全綠（紅 {base}）")
    if not ok1:
        red.append("Z1")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（突變 ⇒ 所指之項轉紅）──")
    for name, want, edits in _muts():
        s = src
        bad = None
        for anc, rep in edits:
            n = s.count(anc)
            if n != 1:
                bad = f"錨命中 {n}"
                break
            s = s.replace(anc, rep)
        if bad:
            print(f"  🔴 {name}：{bad}")
            red.append(name.split()[0])
            continue
        got = _all_red(f21, ah, s)
        ok = set(want) <= set(got)
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：所指 {want}；轉紅 {got}")
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) == 3 and argv[1] == "mut":
        return mut(os.path.abspath(argv[2]))
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `K7`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-54` 之裁之內容 ① 末句之射程之註；入主線（`W-G.9-362`·⛔ 上文一字不刪·純末端追加）

**註**（發單側窗六十三·`2026-10-02`·【工】·⛔ 充裁·`自誤 566`）：上開「`K-9-54` 之讀法」節（`W-G.9-361`·補令一·裁一·工程裁）裁之內容 ① 末句「**⛔ 因容差而相連者**：只在一點相接（含二邊夾角甚小之近切）……」，其「近切」所驗者唯二直邊（量測器 `F21` 之 `A15`·斜率 `0.0087`）；以密點存之曲線界與他片只在一點相切者，依該句前之界址點之讀法判為相連（例：直邊之片與半徑 `20 m`、頂點間距 `5 cm` 之弧邊之片切於一點 ⇒ 共線長 `0.100 m`；間距 `0.2 m` ⇒ 不相連）——該句之「近切」以本註之射程讀之（二直邊之近切）；曲線之近切之處置 ＝ `GB-197`（另單）。`K-6 §一`「單點相接不算」⛔ 變。
**本案**：新判為相連之 `19` 對（`F21 run` 之 `R0`）中同歸戶之 `15` 對之共線長最短 `0.97 m`（`GB-195` 所列·皆界線重合之段）、餘 `4` 對涉殘料（無歸戶·⛔ 入任何群）；`data/V6_1.dxf` ⛔ 弧（`ARC`／`CIRCLE`／`LWPOLYLINE` 之 bulge 皆 `0`）、其 `LINE`／`POLYLINE` 之段 `409` 最短 `0.1004 m` ⇒ 本案之配地⛔ 受影響。
**落地狀態**：上開裁之內容 ①（連同補令二之補·片之多邊形部分）＝ `W-G.9-361` 工項二‴（`f74f95e2cda03aff98ca96c9594b3285b6ec1db2`）；入主線 ✅（`W-G.9-362` 工項零′·主線快轉至 `924d91634b1b36ea1d5fbbffd4a6791693ad3311`）。
````

## 附錄丙　塊 `G6`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-197` 之立；`GB-195` 之失效（`W-G.9-362`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `924d91634b1b36ea1d5fbbffd4a6791693ad3311`（本批開工態·即工項零′ 快轉後之主線）。**取號**（`W-G.9-362 §零-1`）：`GB-197` 於開工態之命中（母體 ＝ 追蹤檔 `2754` 檔·列框·`git grep -c -F "GB-197"`）`2` 列皆係前單之「對照乙［必為零］」所列之未取號（`docs/orders/W-G.9-341_重量單.md:36`、`docs/orders/W-G.9-343_重量單.md:35`·⛔ 占用）⇒ 取之。

### `GB-197` 🆕　**地籍相連之判之界址點之讀法（`K-9-54`）繫於頂點之疏密：以密點存之曲線界與他片只在一點相切者判為相連**

**受詞**：`app.py` 模組層 `_k954_vtx_len`（字樣錨 `def _k954_vtx_len`·`k6_shares_segment` 之重判所呼叫）——二片之邊兩兩相對、其互投影之重疊段之 Hausdorff 距 `≤ K6_SHARE_COORD_TOL` 者逐邊計入；相切處兩側之短邊各與他片之邊相距 `≤ 1e-4 m` ⇒ 其和得達 `K6_SHARE_MIN_LEN`（`0.01 m`）。
**實測**（發單側窗六十三·倉外·`shapely 2.1.2`／`GEOS 3.13.1`·`f74f95e` 之 `k6_shares_segment`）：二單位圓（頂點 `1025`）相距 `5e-5 m` 切於一點 ⇒ `(True, 0.01226)`、頂點 `257` ⇒ `(False, 0.0)`（CC 之唯讀獨立審查·`docs/reports/W-G.9-361R_地籍相連之判之座標容差_執行報告.md` `⑥-2` 發現 `9` 之復現）；直邊之片與弧邊之片（半徑 `5`／`10`／`20 m`）切於一點：頂點間距 `2 cm` ⇒ 皆相連（共線長 `0.040`〜`0.120 m`）；`5 cm` ⇒ 半徑 `20 m` 者相連（`0.100 m`）、餘否；`0.2 m`／`0.5 m` ⇒ 皆不相連。
**與配地之關係**：本案零——新判為相連之 `19` 對（`F21 run` 之 `R0`）中同歸戶之 `15` 對之共線長最短 `0.97 m`（`GB-195` 所列·皆界線重合之段）、餘 `4` 對涉殘料（無歸戶·⛔ 入任何群）；`data/V6_1.dxf` ⛔ 弧（`ARC`／`CIRCLE`／`LWPOLYLINE` 之 bulge 皆 `0`）、其 `LINE`／`POLYLINE` 之段 `409` 最短 `0.1004 m`；`app.py` 讀 `LWPOLYLINE` 唯取頂點（`get_points`·⛔ 展弧）。他案：曲線界以密點存者（例：自他系統轉出而弧經加密），只在一點相切之同歸戶片入同一合併群（段三之平分、入池閘、末端塊之合併再試隨之）——違 `K-6 §一`「單點相接不算」。
**與既有登記之界**：`自誤 566`（入典之全稱之失準）；`W-G.9-361` 補令二 裁四（`K-9-54` ⛔ 繫於圖形之存法·本項其同族：同一相切之形，頂點密者相連、疏者否）；`GB-196`（讀入之有限性之閘）。
**失效條件**：界址點之讀法於同一幾何之二種離散（頂點之疏密）同判、且只在一點相切者⛔ 相連之式落地入主線。
🔒 **排程**：另單（⛔ 急·本案⛔ 觸·其式屬工程裁；涉域上判斷者另呈）。

### `GB-195` 之失效

`GB-195` 之失效條件（「`K-9-54`〔KL 裁 `2026-09-30`〕之碼側落地〔`W-G.9-361` 工項二〕入主線」）於 `W-G.9-362` 工項零′ 成就：主線快轉至 `924d91634b1b36ea1d5fbbffd4a6791693ad3311`（其祖含 `f74f95e2cda03aff98ca96c9594b3285b6ec1db2`·工項二‴）。⛔ 刪其原文。
````

## 附錄丁　塊 `E9`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-362 §零-1`）：本批取 `566`（`1` 號）——CC 於 `W-G.9-361` 補令二工項二‴ 之唯讀獨立審查所記（歸 (C)·`docs/reports/W-G.9-361R_地籍相連之判之座標容差_執行報告.md` `⑥-2` 發現 `9`）、發單側窗六十三自倉復現而鑄者。

### 🩸 `自誤 566`　**`W-G.9-361` 補令一 裁一之入典之文（塊 `K6′` 裁之內容 ① 末句）與量測器 `F21` 之說明書，以全稱載「只在一點相接（含二邊夾角甚小之近切）……⛔ 因容差而相連」；所驗之否例（`A15`）唯二直邊——以密點存之曲線界與他片只在一點相切者，依其讀法判為相連**

**形**：發單側窗六十三以 `f74f95e` 之 `k6_shares_segment` 復現：二單位圓（頂點 `1025`）相距 `5e-5 m` 切於一點 ⇒ `(True, 0.01226)`（頂點 `257` ⇒ `(False, 0.0)`）；直邊之片與半徑 `20 m`、頂點間距 `5 cm` 之弧邊之片切於一點 ⇒ `(True, 0.100)`；間距 `2 cm` ⇒ 半徑 `5`／`10`／`20 m` 皆相連；間距 `0.2 m`／`0.5 m` ⇒ 皆不相連。相切處兩側之短邊各與他片之邊相距 `≤ 1e-4 m` ⇒ 逐邊計入、其和達 `0.01 m`。
**後果之界**：本案零——新判為相連之 `19` 對（`F21 run` 之 `R0`）中同歸戶之 `15` 對之共線長最短 `0.97 m`（`GB-195` 所列·皆界線重合之段）、餘 `4` 對涉殘料（無歸戶·⛔ 入任何群）；`data/V6_1.dxf` ⛔ 弧（`ARC`／`CIRCLE`／`LWPOLYLINE` 之 bulge 皆 `0`）、其 `LINE`／`POLYLINE` 之段 `409` 最短 `0.1004 m`。他案：曲線界以密點存者，只在一點相切之同歸戶片誤入同一合併群（`GB-197`）。入典之全稱失準（`K-6` 典·塊 `K6′` ① 末句）。
**根因**：`自誤 562` 之攔法（「須以原判準之性質逐項驗其否例：單點、近切、淺交、端點逾差」）於補令一施之，「近切」唯以一形（二直邊·斜率 `0.0087`）驗之而以全稱入典——以一形之驗代性質之全域；且未察界址點之讀法之判繫於頂點之疏密（同一相切之形，密者相連、疏者否），與補令二 裁四之所由（`K-9-54` ⛔ 繫於圖形之存法）同族。
**後果之框**：🟢 零（本案）。攔點 ＝ CC 之唯讀獨立審查（補令二·發現 `9`·CC 記之、⛔ 改）→ 發單側窗六十三復現。
**攔法**：`K-6` 典之 `🔧` 註（`W-G.9-362` 塊 `K7`·⛔ 改前文）；`GB-197`（另單）。通則：以容差放寬一判準而以「⛔ 因容差而……」入典者，其否例須以同一幾何之二種離散（頂點之疏密）各驗之；所驗唯一形者，入典之文具名其形、⛔ 作全稱。
````

## 附錄戊　塊 `P16`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：地籍相連之判之座標容差（`K-9-54`）入主線；其接線與突變之判別力（`W-G.9-362`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart`（`W-G.9-362` 工項零′ 快轉至 `924d91634b1b36ea1d5fbbffd4a6791693ad3311` 之後）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-54`（地籍界線之座標相差在 `0.1 mm` 以內者視為相連） | 「待落地清單之更新：地籍相連之判之座標容差（`K-9-54`·`GB-195`）入側支……」節序 `1` 及其補（片之多邊形部分）——`k6_shares_segment`（`f74f95e`） | ✅（主線） | `docs/orders/W-G.9-361_規格單.md`；`docs/orders/W-G.9-361_補令一.md`；`docs/orders/W-G.9-361_補令二.md` |
| `2` | `GB-195`（精確交集之判使合併群斷裂） | 失效（序 `1` 入主線） | ✅ | `docs/orders/W-G.9-362_輕量單.md` |
| `3` | 接線與突變之判別力（`W-G.9-361 §四-2`） | 量測器 `F22`（`verify/probes/probe_WG9362_k954_mut.py mut`）：以 CC 之碼之字樣為錨之接線 `V1`〜`V6`、行為 `B1`〜`B4`、二十一突變 `M1`〜`M21` 各轉其所指之項 | ✅ | 同序 `2` |
| `4` | `GB-197`（界址點之讀法繫於頂點之疏密·曲線之近切） | 本案⛔ 觸 | ⬜ | 另單 |
| `5` | `自誤 566` | 見自誤簿 | ✅ | 同序 `2` |
| `6` | 主 checkout 之同步 | — | ✅（工項四） | 同序 `2` |

🔒 前開「……入側支……」節之序 `5`（突變之判別力 ＋ 入主線 ＋ 主 checkout 之同步·⬜）⇒ 本節序 `1`／`3`／`6`；其序 `3`（`K-9-53`·規格步 `4`）、序 `4′`（`GB-196`）之態不變。
🔒 **依賴序**：規格步 `4`（`K-9-53`）→ `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-196`、`GB-197` 另單（⛔ 急）；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ `W-G.9-357` 節序 `7` ＋ `W-G.9-360` 節序 `5`）。
🔒 **本機介面**（同步後）：退縮 `3.5 m` 之「🧮 執行 G 值迭代計算」之成果，`R3`／`R5`／`R6` 三街廓依前開節之「本案之量」而變；退縮 `0 m`⛔ 變。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `6`（子字串框·含圖例與本列）·列 ＝ `4`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄己　工項一之二態之出艙（`F22 mut`·發單側窗六十三實跑）

塊 `T1`（必過之態·`924d916`）：

````text
── 本部 ──
  ✅ Z0 受詞在（F21 之判式、app_harvest 之二函式、app.py）
── F21 之例（記憶體中 harvest 之 app.py）──
  ✅ A1 精確共邊（長 1）⇒ (True, 1.0)·長度逐位
  ✅ A2 角點相接 ⇒ (False, 0.0)·長度逐位
  ✅ A3 精確共邊 0.005 ⇒ (False, 0.005)
  ✅ A4 微米級錯位而共線（精確交集為一點）⇒ 相連、其長 ≈ 1（三位小數）
  ✅ A4′ 同 A4·精確交集之線長 ＝ 0（受詞確為現碼判為不相連之形）
  ✅ A5 平行錯位 2e-4 m ⇒ (False, 0.0)
  ✅ A6 容差內而共線長 0.008 ⇒ (False, 0.0)
  ✅ A7 相距 0.01 m ⇒ (False, 0.0)
  ✅ A8 坐標 ~3e5／2.6e6 m 之微米錯位（共線長 12）⇒ 相連、其長 ≈ 12
  ✅ A9 缺片（None）⇒ (False, 0.0)
  ✅ A10 三片鏈（A–B 精確、B–C 微米錯位）⇒ 一群
  ✅ A11 三片鏈（B–C 平行錯位 2e-4）⇒ 二群
  ✅ A12 常數 K6_SHARE_COORD_TOL ＝ 1e-4、K6_SHARE_MIN_LEN ＝ 0.01
  ✅ A13 既有之 k6_merge_selftest() 仍過（S-1〜S-7）
  ✅ A14 精確共線 0.0099（容差不增其長）⇒ (False, 0.0099)
  ✅ A15 角點相接而二邊近切（斜率 0.0087）⇒ (False, 0.0)
  ✅ A16 二片重疊而邊界淺交（斜率 0.0087）⇒ (False, 0.0)
  ✅ A17 一端之界址點相差 1.5e-4、他端 5e-5（中段在容差內）⇒ (False, 0.0)
  ✅ A18 中間之界址點相差 2e-4 ⇒ (False, 0.0)
  ✅ A19 坐標含 NaN（共線之邊在容差內）⇒ 二向皆不相連
  ✅ A20 重判之長二向逐位同（A4 之形）
  ✅ A21 中間之界址點相差 5e-5（容差內）⇒ 相連、其長 ≈ 10（三位小數）
  ✅ A22 MultiPolygon 與他片微米錯位而共線（A4 之形）⇒ 二向皆相連、其長 ≈ 1
  ✅ A23 自觸之環經 buffer(0) 成 MultiPolygon（二部）、其一部與他片微米錯位而共線 ⇒ 相連、其長 ≈ 1
  ✅ A24 MultiPolygon 之他部之坐標含 NaN（共線之部在容差內）⇒ 二向皆不相連
  ✅ A25 MultiPolygon 之一部與他片平行錯位 2e-4 ⇒ (False, 0.0)
  ✅ A26 非面狀之受詞（線·沿 A1 之共邊微米錯位）二向與空片 ⇒ 皆 (False, 0.0)
  ✅ A27 以容差相連之二片之聯集（buffer(0) 後仍為 MultiPolygon）與第三片平行錯位 5e-5 ⇒ 相連、其長 ≈ 1
  （28 例）
── 本器之行為（B）──
  ✅ B1 ④″-2 之運算拋例外（平方下溢之極短邊）⇒ 二向皆 (False, 精確之長)
  ✅ B2 含洞之 MultiPolygon：洞之環與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 4
  ✅ B3 MultiPolygon 之一部之洞之坐標含 NaN（他部之外環微米錯位而共線）⇒ 二向皆不相連
  ✅ B4 片之環含重複之相鄰頂點、與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 1
── F21 之接線（W1〜W4）與本器之接線（V1〜V6）──
  ✅ W1 模組層 K6_SHARE_COORD_TOL = 0.0001 恰一處（賦值 1 處·值 0.0001）
  ✅ W2 k6_shares_segment 先算精確交集、其後引 K6_SHARE_COORD_TOL（精確交集之字樣於 1014·容差之引於 2205）
  ✅ W3 K6_SHARE_COORD_TOL 唯 k6_shares_segment 及其所呼叫之函式引之（引之者 ['k6_shares_segment']；許 ['_k954_all_finite', '_k954_areal', '_k954_vtx_len', 'k6_shares_segment']）
  ✅ W4 k6_shares_segment 及其所呼叫之函式⛔ 案件字面（[]）
  ✅ V1 精確先、重判後（位置 [1014, 1648, 2188, 2225]）
  ✅ V2 重判之序（型之檢 → 有限性 → 相距 → 界址點之共線長 → 例外 ⇒ 不相連 → 門檻）（位置 [2234, 2366, 2465, 2541, 2584, 2635]）
  ✅ V3 型之檢以 geom_type／is_empty（⛔ 恃例外）（try False）
  ✅ V4 四長取小（二軸 × 二片）（位置 [3744, 3779, 3814]）
  ✅ V5 Hausdorff 之四端（位置 [3204, 3394]）
  ✅ V6 片之環 ＝ 各多邊形部分之 exterior 與 interiors（有限性之檢、邊）（有限性 2／邊 2（期 2／2））
  ✅ Z1 未突變之態全綠（紅 []）
── 判別力（突變 ⇒ 所指之項轉紅）──
  ✅ M1 去精確之判之早返（一律重判）：所指 ['V1']；轉紅 ['V1']
  ✅ M2 型之檢改恃例外：所指 ['V3']；轉紅 ['V3']
  ✅ M3 去型之檢之判（None ⇒ 例外）：所指 ['V2']；轉紅 ['V2']
  ✅ M4 去有限性之檢：所指 ['A19', 'A24', 'V2']；轉紅 ['A19', 'A24', 'B3', 'V2']
  ✅ M5 有限性之檢唯及第一部：所指 ['A24', 'V6']；轉紅 ['A24', 'B3', 'V6']
  ✅ M6 有限性之檢唯及 exterior：所指 ['B3', 'V6']；轉紅 ['B3', 'V6']
  ✅ M7 去相距之檢：所指 ['V2']；轉紅 ['V2']
  ✅ M8 相距之檢先於型之檢與有限性之檢：所指 ['V2']；轉紅 ['V2']
  ✅ M9 邊唯取第一部：所指 ['A23', 'V6']；轉紅 ['A23', 'V6']
  ✅ M10 邊唯取 exterior：所指 ['B2', 'V6']；轉紅 ['B2', 'V6']
  ✅ M11 長 0 之邊⛔ 略：所指 ['B4']；轉紅 ['B4']
  ✅ M12 四長取大：所指 ['V4']；轉紅 ['V4']
  ✅ M13 唯一軸（二長取小）：所指 ['V4']；轉紅 ['A20', 'V4']
  ✅ M14 Hausdorff 唯 s′ 之二端：所指 ['V5']；轉紅 ['V5']
  ✅ M15 H 之門檻減半：所指 ['A21', 'V5']；轉紅 ['A21', 'V5']
  ✅ M16 先篩過嚴（外接矩形相離即略）：所指 ['A27']；轉紅 ['A27']
  ✅ M17 例外 ⇒ 相連：所指 ['B1', 'V2']；轉紅 ['B1', 'V2']
  ✅ M18 重判相連而回精確之長：所指 ['A4', 'V2']；轉紅 ['A4', 'A8', 'A21', 'A22', 'A23', 'A27', 'B2', 'B4', 'V2']
  ✅ M19 重判不相連而回界址點之共線長：所指 ['A6', 'V2']；轉紅 ['A6', 'V2']
  ✅ M20 容差以字面：所指 ['W2', 'W3', 'V1']；轉紅 ['W2', 'W3', 'V1']
  ✅ M21 相距之檢之容差改 0：所指 ['A27', 'V2']；轉紅 ['A27', 'V2']
⇒ 紅 []；rc 0
````

塊 `T2`（必破之態·`3ae0ce7`）：

````text
── 本部 ──
  ✅ Z0 受詞在（F21 之判式、app_harvest 之二函式、app.py）
── F21 之例（記憶體中 harvest 之 app.py）──
  ✅ A1 精確共邊（長 1）⇒ (True, 1.0)·長度逐位
  ✅ A2 角點相接 ⇒ (False, 0.0)·長度逐位
  ✅ A3 精確共邊 0.005 ⇒ (False, 0.005)
  🔴 A4 微米級錯位而共線（精確交集為一點）⇒ 相連、其長 ≈ 1（三位小數）：得 (False, 0.0)　期 (True, 1.0)
  ✅ A4′ 同 A4·精確交集之線長 ＝ 0（受詞確為現碼判為不相連之形）
  ✅ A5 平行錯位 2e-4 m ⇒ (False, 0.0)
  ✅ A6 容差內而共線長 0.008 ⇒ (False, 0.0)
  ✅ A7 相距 0.01 m ⇒ (False, 0.0)
  🔴 A8 坐標 ~3e5／2.6e6 m 之微米錯位（共線長 12）⇒ 相連、其長 ≈ 12：得 (False, 0.0)　期 (True, 12.0)
  ✅ A9 缺片（None）⇒ (False, 0.0)
  🔴 A10 三片鏈（A–B 精確、B–C 微米錯位）⇒ 一群：得 [[0, 1], [2]]　期 [[0, 1, 2]]
  ✅ A11 三片鏈（B–C 平行錯位 2e-4）⇒ 二群
  🔴 A12 常數 K6_SHARE_COORD_TOL ＝ 1e-4、K6_SHARE_MIN_LEN ＝ 0.01：得 ('例外', 'KeyError')　期 (0.0001, 0.01)
  ✅ A13 既有之 k6_merge_selftest() 仍過（S-1〜S-7）
  ✅ A14 精確共線 0.0099（容差不增其長）⇒ (False, 0.0099)
  ✅ A15 角點相接而二邊近切（斜率 0.0087）⇒ (False, 0.0)
  ✅ A16 二片重疊而邊界淺交（斜率 0.0087）⇒ (False, 0.0)
  ✅ A17 一端之界址點相差 1.5e-4、他端 5e-5（中段在容差內）⇒ (False, 0.0)
  ✅ A18 中間之界址點相差 2e-4 ⇒ (False, 0.0)
  ✅ A19 坐標含 NaN（共線之邊在容差內）⇒ 二向皆不相連
  🔴 A20 重判之長二向逐位同（A4 之形）：得 (False, True)　期 (True, True)
  🔴 A21 中間之界址點相差 5e-5（容差內）⇒ 相連、其長 ≈ 10（三位小數）：得 (False, 0.0)　期 (True, 10.0)
  🔴 A22 MultiPolygon 與他片微米錯位而共線（A4 之形）⇒ 二向皆相連、其長 ≈ 1：得 (False, 0.0, False)　期 (True, 1.0, True)
  🔴 A23 自觸之環經 buffer(0) 成 MultiPolygon（二部）、其一部與他片微米錯位而共線 ⇒ 相連、其長 ≈ 1：得 ('MultiPolygon', 2, (False, 0.0))　期 ('MultiPolygon', 2, (True, 1.0))
  ✅ A24 MultiPolygon 之他部之坐標含 NaN（共線之部在容差內）⇒ 二向皆不相連
  ✅ A25 MultiPolygon 之一部與他片平行錯位 2e-4 ⇒ (False, 0.0)
  ✅ A26 非面狀之受詞（線·沿 A1 之共邊微米錯位）二向與空片 ⇒ 皆 (False, 0.0)
  🔴 A27 以容差相連之二片之聯集（buffer(0) 後仍為 MultiPolygon）與第三片平行錯位 5e-5 ⇒ 相連、其長 ≈ 1：得 ('MultiPolygon', (False, 0.0))　期 ('MultiPolygon', (True, 1.0))
  （28 例）
── 本器之行為（B）──
  ✅ B1 ④″-2 之運算拋例外（平方下溢之極短邊）⇒ 二向皆 (False, 精確之長)
  🔴 B2 含洞之 MultiPolygon：洞之環與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 4：得 ((False, 0.0), (False, 0.0))　期 ((True, 4.0), (True, 4.0))
  ✅ B3 MultiPolygon 之一部之洞之坐標含 NaN（他部之外環微米錯位而共線）⇒ 二向皆不相連
  🔴 B4 片之環含重複之相鄰頂點、與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 1：得 ((False, 0.0), (False, 0.0))　期 ((True, 1.0), (True, 1.0))
── F21 之接線（W1〜W4）與本器之接線（V1〜V6）──
  🔴 W1 模組層 K6_SHARE_COORD_TOL = 0.0001 恰一處（賦值 0 處·值 None）
  🔴 W2 k6_shares_segment 先算精確交集、其後引 K6_SHARE_COORD_TOL（精確交集之字樣於 839·容差之引於 -1）
  🔴 W3 K6_SHARE_COORD_TOL 唯 k6_shares_segment 及其所呼叫之函式引之（引之者 []；許 ['k6_shares_segment']）
  ✅ W4 k6_shares_segment 及其所呼叫之函式⛔ 案件字面（[]）
  🔴 V1 精確先、重判後（錨命中 0：'if _tot >= _ml:'）
  🔴 V2 重判之序（型之檢 → 有限性 → 相距 → 界址點之共線長 → 例外 ⇒ 不相連 → 門檻）（錨命中 0：'_pa, _pb = _k954_areal(poly_a), _k954_ar'）
  🔴 V3 型之檢以 geom_type／is_empty（⛔ 恃例外）（無 _k954_areal）
  🔴 V4 四長取小（二軸 × 二片）（無 _k954_vtx_len）
  🔴 V5 Hausdorff 之四端（無 _k954_vtx_len）
  🔴 V6 片之環 ＝ 各多邊形部分之 exterior 與 interiors（有限性之檢、邊）（有限性 -1／邊 -1（期 2／2））
  🔴 Z1 未突變之態全綠（紅 ['受詞缺', 'A4', 'A8', 'A10', 'A12', 'A20', 'A21', 'A22', 'A23', 'A27', 'B2', 'B4', 'W1', 'W2', 'W3', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']）
⇒ 紅 ['Z1']；rc 1
````

SELF_SHA256: 3b197dd59ea1c4e6d7b2178b4a23e2955a65ae6fc6f7c31d5108ec97a9284a90
