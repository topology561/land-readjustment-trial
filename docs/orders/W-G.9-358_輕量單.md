# `W-G.9-358`　輕量單：主線快轉（至 `4716f20`·`W-G.9-357` 段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51` 入主線）＋ 段三後處理之接線與突變之檢查（`W-G.9-357 §四-2` 之補寫·`F17`）＋ 攢批登記（`自誤 549`／`550`）＋ 待落地清單之更新 ＋ 主 checkout 之同步

> **本單建議等級 ＝ `high`**（本單⛔ 令 CC 撰寫生產碼；受詞 ＝ 快轉、塊之原封入倉與實跑、三簿之末端追加、主 checkout 之同步）。
> **發單** ＝ 發單側窗五十五·`2026-09-29`。**受單** ＝ CC 新窗（工項零′〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**）。
> **級** ＝ **輕**（本批⛔ 新增生產碼：新量測器 `1` 檔 ＋ 自誤簿、`CLAUDE.md` 與恆常附款登記表之純末端追加 ＋ 報告；工項零′ 之快轉使主線納入已於側支放行之生產碼 `commit` `1` 筆〔`898c31f`〕·其入主線之放行見 `§二`；本批⛔ 跑 `run_all` 及 `run` 類之量——快轉後主線之生產碼 `34` 檔 ≡ 側支之端，`W-G.9-357R` `V-2`〜`V-5` 與發單側窗五十五之復驗〔`§一` 項 `4`／`5`〕已跑·KL 令：文件批⛔ 全套驗證儀式）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `17624a19c48715bcb1bcfd6af1a851d756d6d473`；側支 `verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`（`W-G.9-357` 工項四）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F17`／`E6`／`P12`／`H2` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-358_輕量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項四之撞檔前置必觸發，依其處置（`自誤 542`）。本批之新檔（`F17`）與改動（`E6`／`P12`／`H2`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）之一字；既有量測器之一字；任何錨（`K_STAR_EXPECT`／`GSA_EXPECT`／`FLAGGED_EXPECT`／`TRACK_EXPECT`／`TIER_EXPECT`／`F.3 零遺漏` 之式）之改；`verify/baselines`；`verify/out/` 之二凍存名單；`GB` 簿、`VR` 簿、`K-6` 典之一字；自誤簿、`CLAUDE.md` 與 `docs/reports/W-G.9波_恆常附款登記表.md` 除塊 `E6`／`P12`／`H2` 之純末端追加外之一字；任何側支之推送、刪除或改寫（`verify/W-G.9-357-k948` 留於 `4716f20`·⛔ 再推）；`run_all` 之執行。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止；**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙·**先於工項零′**）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `17624a19c48715bcb1bcfd6af1a851d756d6d473`；`git rev-parse origin/verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`；`git ls-remote --heads origin` 之列數 ＝ `32`；施工樹 `git checkout --detach origin/verify/W-G.9-357-k948` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 548 547` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態（側支之端 `4716f20`·即快轉後之主線）之 `docs/` 全檔 **`920`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十五實跑 `python verify/probes/wg9268_gate6_occupancy.py 4716f20 W-G.9-358 W-G.9-357 W-G.9-396`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-358`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-357` | `5`／`11`／`3` | `5`／`11`／`3` | `14` | `6` | `6`／`99` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `4`／`6` | 🟢 宣告框 `0`、鬆框非零（漏框偵察有咬） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `19`／`22` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-357_規格單.md` `§零-1` 所載之具名豁免（報告內嵌本器之出艙）·受詢之判⛔ 受影響 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `4716f20` 之追蹤檔 `2728` 檔〔讀不到 `24`〕·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取）：

| 號 | 裸（錨定 `(?<![0-9\-])<號>(?![0-9])`）列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 549` | `86` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——行號、bytes、列數等·例 `docs/orders/W-G.9-357_規格單.md:232` 之「`549` 列」·⛔ 為自誤之引用） |
| `自誤 550` | `45` | `0` | `0` | 🟢 可取（同上） |
| 對照甲［必非零］`自誤 548` | `65` | `0` | `9` | 🟢 C 形非空（B 形於本倉為量測器紅·`GB-158`） |

自誤 `MAX` ＝ `548`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 549`／`550`（塊 `E6`）；⛔ 鑄 `GB`／`VR`／`K-9`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `17624a1`，或側支 `verify/W-G.9-357-k948` ≠ `4716f20`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `32` |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 工項零′ 前置之任一期不符 |
| `4` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成 |
| `5` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6` | 塊 `F17`／`E6`／`P12`／`H2`／`T1`／`T2` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `7` | 工項一之實跑任一 ≠ 期（尤：必過之態 ≠ `rc 0`、必破之態之末列 ≠ `§一` 項 `6` 之逐字、二態之全文與附錄戊之塊 `T1`／`T2` 不逐列相同） |
| `8` | 自誤簿、`CLAUDE.md` 或恆常附款登記表之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項四：主 checkout 之追蹤檔有變動；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `11` | 工項零〜三之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `12` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者⛔ 屬之） |
| `13` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗五十五自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `17624a19c48715bcb1bcfd6af1a851d756d6d473`；側支 `verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`；主線為側支之祖（`git merge-base --is-ancestor` 真；`git rev-list --count 17624a1..4716f20` ＝ `8`、反向 ＝ `0`）；其餘側支 `verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`32`**（`verify/` `27`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`·二態皆 `34`） | 主線 → 側支之端相異 **`2`** 檔：`app.py` `e11232a6569bf33c7b2b7f15da989873a06ff28c` → `d8938792ab09e71636dc6916b61432c522c847e5`；`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966` → `8d38e55013bec51ab81978336fe04e928f5baf98`；`verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`（二態同） |
| `3` | 三簿（側支之端） | `CLAUDE.md` `303630` B；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `1077462` B；`docs/reports/W-G.9波_恆常附款登記表.md` `62376` B（皆以換行結尾·CR `0`） |
| `4` | `W-G.9-357` 之復驗（發單側窗五十五·依交接文五十四 `§四-1`·全數自倉重跑） | **八 `commit` 逐筆對拍**（`84e5134`／`7165c22`／`47207e9`／`b41f305`／`3816a2f`／`898c31f`／`2009a78`／`4716f20`·線性·各訊息首段逐字 ＝ 單所令）：原單 ＝ `7055ae0d…`（`92860` B）；補令一 ＝ `becbb565…`（`42689` B·`SELF_SHA256` 經 `P-5` 自驗相符·pre-flight 🔴 `0`／🟡 `1` 同補令一 `§五` 項 `6`）；塊 `F16p` 施於 `c77be87…` 得 `c7515d3…` ＝ `3816a2f` 之 `F16`；`K-6` 典 `427954 → 435812`、`CLAUDE.md` `299948 → 303630` 嚴格前綴、所增 ＝ 塊 `K4′`／`P11` 逐位；閘 `1′`〜`5′` 自倉重算皆符（刪除欄；生產碼相異 `2`、`verify/` 相異 `3`；CR `0`〔`11` 檔·`V6.dxf` `12308`〕；heads `32`、主線 `17624a1`、六側支⛔ 變）；新檔之 `git check-ignore` 皆無命中。**逐段讀二檔之差異**（`git diff 17624a1 898c31f -- app.py verify/selection_pipeline.py`·`30517` B·`482` 列·`15` 段·`sha256` `f0a50408…` ＝ 報告 ⑧）：對原單 `R-1`〜`R-14`、`X-1`〜`X-7` 與補令一 `§二` 五款無偏差；**`V-8`**：以停機報告同目錄之差異檔施於 `7165c22` 重建首輪之碼（二 blob ＝ `63abb4b…`／`8d38e55…`），與 `898c31f` 之差 `13` 段皆落於補令一五款、與報告 ⑩ 逐段同（`verify/selection_pipeline.py` 二態同）。**量測**：`F16 selftest` 三態 ＝ `3816a2f` ⇒ `rc 1`（紅 `22` 項·末列 ＝ 補令一 `§四` 前置 `1`）／首輪之碼 ⇒ `rc 1`（`⇒ 紅 ['K19', 'K20', 'K21', 'K22']；rc 1`）／`898c31f` ⇒ `rc 0`（`P0` `25／25`）；另於 `898c31f` 逐款單獨還原之五突變（步驟 `10` 之 `R` 去 `- _t14_done`／去 `_t14_done.add(c)`／`_has357` 改 `> 1e-6`／距離改 `round`／`G` 改先查）各恰使 `K19`／`K19`／`K20`／`K21`／`K22` 一項轉紅；`F16 run` ⇒ `rc 0`（保留 `28`／`29` 宗·`G` 逐宗差 `0.0`·段三紀錄 `18`／`0` 列）；`F16 run`／`F14 selftest` 於 `3816a2f` ⇒ `rc 1`（末列 ＝ 補令一 `§四` 前置 `2`）；`V-2` `k6s3 cmp` 二退縮相異 `0` 項（json 唯耗時欄異）；`V-3` `F8 run` 二退縮 `diff` 皆空；`V-4` `parity` 二退縮 `rc 0`（配地列 `35`／`34`、`36`／`35`·不符格 `0`·`Z` ＝ `[('harness', 'R1-抵費地-2')]`）；`V-5` `run_all` 同一倉外路徑 `3816a2f` 對 `898c31f` ⇒ 二態各 `236002` B·`cmp` 逐位同（`64` 項·PASS `28 → 28`·相異項 `0`·末端夾具／golden 列 `21／21`·對帳 `22／36 → 22／36`）；`V-6` 生產碼相異 `2`、`verify/` 唯 `selection_pipeline.py`；收工閘 `6`（`rc 0`）／`7`（`rc 0`·自誤 `533`／`548`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `48`／`51`／`[44, 47]`）與 `8′`〜`22` 之 `34` 命令（於 `4716f20`·其生產碼與 `verify/` ≡ `898c31f`）皆 `rc 0`（`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F10 selftest` 之突變 `M1`〜`M4` 皆轉紅）。CC 報告 ①〜⑪ 俱載，其數與自倉所算相符——**全數相符** |
| `5` | 快轉之淨效（主線 → 側支之端·本案） | `python verify/probes/probe_WG9349_k9296.py run <tree> 3.5`／`0.0`：`3816a2f`（其生產碼 `34` 檔 ＝ `17624a1`）與 `898c31f`（其生產碼與 `verify/` ＝ `4716f20`）之出艙逐位同（二退縮）；`probe_WG9344_k6s3.py cmp` 二退縮相異 `0` 項；`probe_WG9345_screen.py parity` 二退縮不符格 `0`；`run_all` 同一倉外路徑（`/home/claude/wt/P`）二態各 `236002` B·`cmp` 逐位同 ⇒ **本案之配地、街角、抵費地皆⛔ 變**（段三後處理：退縮 `3.5 m` `5` 列整批通過、`0 m` 無段三之列·本批之新路徑⛔ 觸）；他案之差 ＝ 段三後處理整批不過者，由「整筆不併／未處置」改依 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`；`K-9-50` 題一 `4` 之合併不過由停機改同之 |
| `6` | 量測器 `F17`（附錄甲）之二態 | **必過**：`4716f20` 之 `app.py`（`d8938792…`）與 `verify/selection_pipeline.py`（`8d38e550…`）⇒ **`rc 0`**；本部 `W0`〜`W12` 皆 ✅；二十九突變 `M1`〜`M29` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`。**必破**：`17624a1` 之二檔（`e11232a6…`／`8bb45920…`·`W-G.9-357` 開工態）⇒ **`rc 1`**；本部十三項皆 🔴、⛔ 施突變；末列逐字 `⇒ 紅 ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12']；rc 1`。二態之全文 ＝ 附錄戊之塊 `T1`／`T2`。🔒 **第三態**（發單側之佐證·⛔ 為 CC 之期·倉內無其 `commit`）：首輪之工項二（`W-G.9-357` 停機報告同目錄之差異檔施於 `7165c22` 所得·二 blob `63abb4b14b2188d88fa8ea9f3bd30079db0665ec`／`8d38e55…`）⇒ `rc 1`，末列 `⇒ 紅 ['W0', 'W3', 'W4', 'W5', 'W6', 'W7', 'W11']；rc 1`——恰為補令一五款之所在（`R-15` 之 `_has357` 缺 ⇒ `W0`；`R-6′` ②③ ⇒ `W3`；`R-6′` ③ ⇒ `W4`；`R-7′` ⇒ `W5`；`X-3′` ⇒ `W6`；`R-15` ⇒ `W7`／`W11`），原單諸款之項（`W1`／`W2`／`W8`〜`W10`／`W12`）皆 ✅ |
| `7` | KL 主 checkout（倉外之物·發單側⛔ 實查） | 依 `W-G.9-356` 工項四 ＝ `wip/s1-endpart` 之 `17624a1`（`W-G.9-357` ⛔ 動之）；其根或有 `W-G.9-357` 之來源檔（原單、補令一·未追蹤·`W-G.9-357 §五-2` 項 `3` 令 KL 自行移除）⇒ 依工項四之撞檔前置處置 |

---

## `§二`　KL 之語與射程

🔒 **所據**：`W-G.9-357 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之未處置不變、`R-5` 之「所施者恆已通過」、`R-6` 之候選與序、`R-7` 之 `raise` 已去、`R-10` 之二處同形、`R-11`／`R-12` 之落點）及其突變之判別力；併入主線之請示。」——本單之 `F17` 即其補寫，並及補令一 `§二` 之 `R-7′`／`X-3′`／`R-15`／`R-6′` 之落點；自誤甲／乙（補令一 `§六`·「候鑄·併次單……登記」）於本單鑄號（塊 `E6`）。
🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：KL 已於發單側窗五十五（`2026-09-29 20:20`）就下列之問一與問二同答「兩題問題：均"是"」（「兩題」＝ 問一與問二·問二見下款）。CC 端之放行：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項零′（主線快轉）與工項四（主 checkout 之同步）之放行，CC 將其逐字載入報告；**無之 ⇒ 工項零′ 之前置畢後停於快轉前，於對話請示 KL**。所答之【要你判斷】逐字 ＝ 問一之【要你判斷】。問一（發單側所呈·【現況】至【要你判斷】逐字）：

> 【現況】357 處理的是街角合併重試之後，地主剩下之土地往哪裡去，即七項 3〜6 與 K-9-51。目前只在側支，本窗已全數復驗；主線與您本機介面仍是 356 之狀態。
> 【要改成】在 358 一併辦理：主線推進到側支之最新狀態，補入接線檢查與兩則自誤登記，並同步您本機的程式資料夾。
> 【對土地的影響】本案退縮 3.5 m 與 0 m 之配地面積、街角、抵費地都不變，介面也沒有新增區塊。只有他案會不同：街角合併重試之後，若整批併入不能通過檢核，原本是「整筆不併、紅字未處置」，改為：
> - 道路、公設地上可拆分之土地，併入不影響原位次之最大面積（以 0.01 ㎡ 為單位）；
> - 剩下之土地，依距離由近到遠，試併入同一地主已配得土地之街廓；
> - 都不行才進調配。
>
> 兩端競合、只有一端成、另一端又併不進去的情形，原本會停機，也改為同樣處理。
> 【要你判斷】是否同意將 357 併入主線，並請 CC 同步您本機的程式資料夾（併於 358 辦理）？（是／否）

🔒 **逐筆放行清單**（`恆常附款 y`·擬本單時自倉重導）：母體 ＝ `git rev-list 17624a1..4716f20` ＝ **`8`** 筆；判準 ＝ 是否改動生產碼 `34` 檔之任一（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）。動生產碼者 **`1`** 筆（其餘 `7` 筆皆單、補令、停機報告、量測器、入典與登記、報告）：

| `commit` | 訊息首段 | 所動之生產碼 | 側支之放行 | 本案之土地後果 |
|---|---|---|---|---|
| `898c31fc6c18db156eb0eafe14366d3fb6f7ae30` | `W-G.9-357` 工項二：段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`（剩餘土地之去處）＋ 補令一 | `app.py`、`verify/selection_pipeline.py` | `W-G.9-357 §二`（原單）·補令一 | ⛔（`W-G.9-357R` `V-2`〜`V-5`；發單側窗五十五自倉重跑 ＝ `§一` 項 `5`） |

🔒 **規格單流程之試行·期滿之報告**（`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通（`W-G.9-355`）」節 ②「試行期 ＝ 自 `W-G.9-355` 起兩輪」·期滿由發單側向 KL 報告續否）：發單側窗五十五就下列之問二呈報，KL 答同上款（「兩題問題：均"是"」）⇒ **規格單流程自 `W-G.9-359` 起為常態**，其登記 ＝ 塊 `H2`（附於恆常附款登記表之末·附則甲〜丙）。問二（【現況】至【要你判斷】逐字）：

> 【現況】「chat 出規格、CC 寫生產碼」自 355 起試行兩輪，試行期已滿。
> - 首輪 355：一次就完成，沒有補令。
> - 次輪 357：CC 派出之獨立審查（只讀不改）攔下我這邊規格之一處漏載：兩端競合時轉去調配的那筆土地，後續又被處理一次。本案不會發生此情形。為此停機一次，出了補令一。另一處剩下面積之判斷門檻前後不一致，也是 CC 捕到的。
> - CC 寫程式本身很快（首輪 12 分鐘、補令 3 分鐘），時間主要花在驗證（22〜52 分鐘）。
> - 兩輪之本案配地都沒有變。
>
> 【要改成】規格單流程改為常態做法，並納入本輪兩則教訓：
> - 凡規格要求某筆土地「維持原狀」，要逐一查其後各步是否又會取到它；
> - 同一個量的判斷、寫出、讀取，要用同一個算式；
> - CC 之唯讀獨立審查列為常設步驟。
>
> 【對土地的影響】只是流程改變，本身不動任何配地。
> 【要你判斷】是否續行規格單流程？（是／否；答否就回到由發單側擬生產碼之舊流程）

🛑 **射程**：`(a)` 主線快轉至 `4716f202bfd9368d960b942025b2bb8da34c6dd6`（工項零′·**以前置皆符且本節之放行成立為條件**）；`(b)` 工項零〜三（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項四於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、既有量測器、任何他錨、`GB`／`VR`／`K-6` 典、恆常附款登記表之既有文字（唯塊 `H2` 之末端追加）；`(e)` ⛔ 及 `K-9-51` 射程 `③` 之二情形、`W-G.9-357` 待落地表序 `7`（畫面「自動計算公設分配」展開區）、規格步 `3`〜`8`、畫面批——另單。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存倉外之目錄 `<O>`）：
1. `git merge-base --is-ancestor 17624a19c48715bcb1bcfd6af1a851d756d6d473 4716f202bfd9368d960b942025b2bb8da34c6dd6` ⇒ `rc 0`；`git rev-list --count 17624a1..4716f20` ＝ `8`；`git rev-list --count 4716f20..17624a1` ＝ `0`。
2. `git diff --name-only 17624a1 4716f20 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `2` 列：`app.py`、`verify/selection_pipeline.py`（`§一` 項 `2`·🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 之檔，發單側實測得 `4` 列）；`git rev-parse 4716f20:app.py` ＝ `d8938792ab09e71636dc6916b61432c522c847e5`。
3. `git rev-list 17624a1..4716f20` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `commit`（全 `40` 碼·命中 `2` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3`·⛔ 快轉。

**快轉**（前置皆符且 `§二` 之放行成立後·與前置為分開之呼叫）：

```
git push origin 4716f202bfd9368d960b942025b2bb8da34c6dd6:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4`）；⛔ 改目標值（逐字 `4716f202bfd9368d960b942025b2bb8da34c6dd6`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-357-k948`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`；
② 遠端 heads ＝ **`32`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `4716f20` 之相異 ＝ **`0`**；判別力［必非零］：vs `17624a1` 之相異 ＝ **`2`**（`§一` 項 `2` 之 `2` 檔）；
④ `git branch -r --contains 898c31fc6c18db156eb0eafe14366d3fb6f7ae30` 含 `origin/wip/s1-endpart`。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `4716f20…` 方續工項零。

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-358_輕量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-358 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F17` 入倉與實跑（主線·零生產碼）

1. 塊 `F17`（附錄甲）依圍欄之逐列索引抽出、對拍 `§五-1` 項 `2` 後，以二進位寫為 `verify/probes/probe_WG9358_k948_wiring.py`（**新檔**）；`git check-ignore` 之⛔ 命中。
2. **必過之態**（施工樹·其 `app.py` ＝ `d8938792…`、`verify/selection_pipeline.py` ＝ `8d38e550…`）：`python verify/probes/probe_WG9358_k948_wiring.py wiring <repo> > <O>\f17_pass.log` ⇒ **`rc 0`**；本部 `W0`〜`W12` 皆 ✅；二十九突變 `M1`〜`M29` 皆 ✅（各轉其所指之項）；末列逐字 `⇒ 紅 []；rc 0`；全文與附錄戊之塊 `T1` 逐列相同（比對前去 CR 及列尾空白）。
3. **必破之態**：`git worktree add --detach <P> 17624a19c48715bcb1bcfd6af1a851d756d6d473`（`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑）；於施工樹 `python verify/probes/probe_WG9358_k948_wiring.py wiring <P> > <O>\f17_break.log` ⇒ **`rc 1`**，末列逐字 ＝ `§一` 項 `6` 之必破之末列；全文與附錄戊之塊 `T2` 逐列相同（同上）；跑畢 `git worktree remove --force <P>`。

任一 ≠ 期 ⇒ 停機款 `7`（⛔ 改器）。`commit` 訊息逐字 `W-G.9-358 工項一：量測器 F17（段三後處理之七項 3〜6 與 K-9-51 之接線與突變）入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　攢批登記、待落地清單之更新與規格單流程之續行（主線·零生產碼·一 `commit`）

塊 `E6`（附錄乙）附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P12`（附錄丙）附於 `CLAUDE.md` 之末；塊 `H2`（附錄丁）附於 `docs/reports/W-G.9波_恆常附款登記表.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-358 工項二：攢批登記（自誤 549／550）＋ 待落地清單之更新（W-G.9-357 入主線 ＋ 接線檢查）＋ 規格單流程之續行 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-358R_入主線與段三後處理之接線檢查_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ 工項一之二態之全文（`f17_pass.log`／`f17_break.log`）；⑤ 四塊之實得（bytes／`sha256`）與三簿之改前改後 bytes；⑥ `§二` 之放行（KL 之逐字或請示之經過）；⑦ CC 之自捕與自解；⑧ 各段耗時。收工閘之實測值與工項四之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-358 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次快轉將新入之路徑集 `A`；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `10`）；不等 ⇒ 停機款 `10`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項三 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `d8938792ab09e71636dc6916b61432c522c847e5`；`git -C <主 checkout> hash-object verify/selection_pipeline.py` ＝ `8d38e55013bec51ab81978336fe04e928f5baf98`；`git -C <主 checkout> hash-object verify/stepg_pipeline.py` ＝ `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`。

任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之刪除欄 | 逐檔 **`0`** |
| `2` | 生產碼 `34` 檔 | 對 `4716f20` 相異 **`0`**；判別力［必非零］：對 `17624a1` 相異 **`2`**；`verify/` 之一切檔對 `4716f20` 相異恰 **`1`**（新檔 `verify/probes/probe_WG9358_k948_wiring.py`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`6` 檔：本單、`F17`、自誤簿、`CLAUDE.md`、恆常附款登記表、報告） |
| `4` | 三簿之 bytes | 自誤簿 `1077462` → **`1080872`**；`CLAUDE.md` `303630` → **`308508`**；恆常附款登記表 `62376` → **`65928`**；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`32`**；主線 ＝ 工項三之 `commit`，其祖含 `4716f20`；`verify/W-G.9-357-k948` ＝ `4716f20…`；`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 550 548 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 550 548` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`535`**／`MAX` **`550`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `48`／`51`／`[44, 47]`（`GB`／`VR`／`K-9` 皆 ＝ 開工態；自誤唯增 `549`／`550`） |
| `8` | `python verify/probes/probe_WG9358_k948_wiring.py wiring <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9357_k948.py selftest <repo 絕對路徑>`；`python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo 絕對路徑>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo 絕對路徑>`；`python verify/probes/probe_WG9345_screen.py wiring <repo 絕對路徑>`；`python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>`；`python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | 皆 **`rc 0`**；`F16` 末列逐字 `⇒ 紅 []；rc 0`（`P0` `25／25`）；`F15`／`F14` 末列逐字 `⇒ 紅 []；rc 0`；`F4` 末列逐字 `⇒ rc 0（不符 0·器紅 0）`；`wfns_ast` **`48`／`48`／`47`**；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零′〜三（快轉 ＋ 本單 ＋ 塊 `F17` ＋ 塊 `E6`／`P12`／`H2` ＋ 報告之替身）並實跑閘 `1`〜`9` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F17` | `36220` B·`sha256` `f1e1ec505f4c7c34a81bedca53637f8f0960ee6c1193f1113cf5a011dd1d5810`·`609` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9358_k948_wiring.py`（blob `755631288349fb04fd7b6d2b7cc1ad35ae14da0f`） |
| `3` | 塊 `E6` | `3410` B·`sha256` `1f1d8465397786ea4591df92efb8104a2ac10768d8d9e6966e72b074a906ad2e`·`24` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1077462` B）之末後，期末 ＝ `1080872` B |
| `4` | 塊 `P12` | `4878` B·`sha256` `0182cedff3dac36c5b8320956cab9746193ae2b096ed71316dd13f820099419c`·`21` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`303630` B）之末後，期末 ＝ `308508` B |
| `5` | 塊 `H2` | `3552` B·`sha256` `241ad43186b99874c98d66f4f579730455f292869cf96861dc196d0f98292458`·`48` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_恆常附款登記表.md`（`62376` B）之末後，期末 ＝ `65928` B |
| `6` | 附錄戊之塊 `T1`／`T2`（工項一之二態之出艙·發單側實跑） | `T1` `4270` B·`sha256` `d154545da58dcd38da690f11a1bdbb5690b923af369a228b17267f9c139fb476`·`45` 列；`T2` `2078` B·`sha256` `0e1c2fe4765961dedc19618072a6f4ce91c2fd84a660e6a22325bd88b7be44f6`·`16` 列（圍欄內全文·末附換行；比對時去 CR 及列尾空白） |
| `7` | 量測器之二態 | `§一` 項 `6` |
| `8` | 本單所載 KL 之語 | `§二` 之問一、問二與 KL 之答，皆發單側窗五十五之對話逐字（KL `2026-09-29 20:20`） |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十五實跑（態 `4716f20`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-4` `:71`（`§一` 態錨之表頭·所觸之箭頭係各項之改前改後〔項 `2`／`5` ＝ 主線 `17624a1` 至側支之端 `4716f20`；項 `4` ＝ `W-G.9-357` 之改前至改後〕，同格自載 ⇒ **具名豁免**）、`P-4` `:188`（`§四` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `4716f20` 至工項二之端，表內自載 ⇒ **具名豁免**）、`P-6` `:71`（`§一` 態錨之表頭·其所轄之數皆發單側窗五十五自倉實跑、各格具名其命令或出處 ⇒ **具名豁免**）、`P-6` `:892`（附錄丙塊 `P12` 內「前節之更新」列·所觸之數係待落地表之序號、⛔ 為實測之數 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `20014`–`27686`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux） | `git worktree add --detach <S> 4716f20`（拋棄式·⛔ `push`）＋ 本單 ＋ 塊 `F17` ＋ 塊 `E6`／`P12`／`H2` ＋ 報告之替身·四 `commit`：工項零′ 前置 `1`〜`3` 皆符（`8`／`0`；`:(glob)` 形恰 `2` 列；逐筆判命中者恰 `898c31f`〔`2` 列〕）；六塊之抽取與附錄逐位同；工項一二態 `rc 0`／`rc 1`、全文與塊 `T1`／`T2` 逐位同；閘 `1` 各檔之刪除欄皆 `0`；閘 `2` 對 `4716f20` 相異 `0`、對 `17624a1` `2`、`verify/` 相異恰 `1`；閘 `3` CR `0`（`V6.dxf` `12308`）；閘 `4` 自誤簿 `1077462 → 1080872`、`CLAUDE.md` `303630 → 308508`、恆常附款登記表 `62376 → 65928`（皆嚴格前綴）；閘 `6`〜`9` 皆 `rc 0`（閘 `7` 四簿 ＝ 自誤 `535`／`550`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `48`／`51`／`[44, 47]`；`F17`／`F16`／`F15`／`F14` 末列 `⇒ 紅 []；rc 0`；`F4` 末列 `⇒ rc 0（不符 0·器紅 0）`；`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」）；新檔之 `git check-ignore` 皆無命中 |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````markdown `` 或 `` ````text ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零′ ⇒ 依 `§二` 之放行、前置皆符後推主線；工項零〜三 ⇒ 逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）。
3. 收工後，主 checkout 之根之來源檔（本單、`W-G.9-357` 之原單與補令一，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F17`（新檔 `verify/probes/probe_WG9358_k948_wiring.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-358 量測器（發單側窗五十五擬·檔 F17·⛔ 由受單側改一字）：段三後處理之 `K-9-48` 七項 3〜6 與 `K-9-51`
（`W-G.9-357` ＋ 補令一）之接線——以程式字樣為錨。

緣由：`W-G.9-357 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之
未處置不變、`R-5` 之「所施者恆已通過」、`R-6` 之候選與序、`R-7` 之 `raise` 已去、`R-10` 之二處同形、`R-11`／`R-12`
之落點）及其突變之判別力」，並含補令一之 `R-7′`／`X-3′`／`R-15`／`R-6′` 之落點。受詞之行為已由 F16
（`probe_WG9357_k948.py`）之 `selftest`／`run` 量之；本器量**程式字樣**（防日後之漂移）。

受詞（工作樹）：app.py 之 k6b_stage3_run（含其巢狀 _has357／_res357／_max357／_dist357／_k951／_split357／_t14_357
與步驟 10）、adj_intake、k6b_screen_callbacks 之巢狀 alloc_state；verify/selection_pipeline.py 之 k6b_stage3_pool_temp、
_k6b_callbacks 之巢狀 alloc_state。

子命令（一律 python verify/probes/probe_WG9358_k948_wiring.py <子命令> <repo>）：
  wiring <repo>
    W0  受詞在：五模組層函式在；七巢狀 def 各恰 1 且皆在 k6b_stage3_run 內（app.py 他處⛔ 同名）。
    W1  `R-2` 未處置不變：k6b_stage3_run 內 `結果='未處置'` 恰 1，在 `if not _qs:` 之本體，同本體有
        log_print「…未處置：二半片皆不鄰 B 內街廓」且以 continue 終；「未處置：「不影響原位次」不過」之字樣 0。
    W2  `R-5`／`R-5′` 所施者恆已通過：_max357 內 `state =` 恰 2，各在 `if <其值> is not None:` 之本體，其值 ∈ {_t, _best}；
        `_t = _try(s)`；`_best` 除初值 None 外唯於 `if _tm is not None:` 內得 `_tm`，`_tm = _try(_mid / 100)`（格值 n / 100）；
        巢狀 _try 唯一 return ＝ `_t if _noaff(…) else None`；末句 `return _lo / 100`。
    W3  `R-6`／`R-6′` ②③ 候選與序：_k951 內 alloc_state(state['temp'], state['build']) 恰 1、其 err ⇒ raise；
        篩 ＝ `_p == x or _p in merged_out or _b in F or _p not in state['by']` ⇒ continue；歸戶 `!= _gx` ⇒ continue；
        `_G = _cur.get('G')` 恰 1 且在 `if _pre:` 內（含「未回 G」之 raise ≥ 2 皆在其內）；序之鍵 ＝
        `(_dist357(x, _b), -float(_G[_p]), _p, …)`；`_cands.sort()` 無 key。
    W4  `R-6′` ③ 距離：_dist357 之末句 ＝ `float(<Decimal>(repr(<d>)).quantize(<Decimal>('0.01'), rounding=<ROUND_HALF_UP>))`
        （別名依其 `from decimal import …` 解之）；_dist357 內⛔ round；街廓之聯集取 `_blk_of[p] == blk` 之全部切片。
    W5  `R-7`／`R-7′`：app.py 內「七項 3〜5 未落地」之字樣 0；`_r4 = None` 恰 1、在 `if _noaff(state, _t2, …):` 之 else；
        `_t14_357(…)` 恰 1、在 `if _r4 is not None:` 之 else；`_t14_done` 唯 `= set()` 一賦值、唯 `.add(c)` 一呼叫，
        其為 _t14_357 本體之頂層句且先於其首個 if（① 之結果不論）；_t14_357 內 c 之整筆不過 ⇒
        `_k951(c, _a357(c), {W['blk']}, True)`，其半之片 ⇒ `_max357(x, w, _s)` 與 `if _has357(_rem):` 之 `_k951(…, False)`。
    W6  `X-3′`：k6b_stage3_run 本體（⛔ 巢狀）之 `R =` 恰 2：`R = _mem - merged_out - set(_recv_by_blk.values()) - L -
        _t14_done`、`R = R - _stay`。
    W7  `R-15`：_has357 ＝ `return round(float(r), 4) > 0`；`_EPS357` 之名 0；_res357／_split357／_k951／_t14_357 與
        末之鍵之環內⛔ 以浮點小量（0 < |v| < 1e-3）比較；諸判之字樣各在其處（見 _R15）；_split357 之
        `if _has357(_s - _g):` 本體含 `_F.add(…)` 與 `_rem += _s - _g`。
    W8  `R-10` 二處同形：二 alloc_state 之 `elif _r.get('驗_總判') == '保留':` 本體逐 AST 同，含
        `_kept.setdefault(_blk, set()).add(_pid)` 與 `_G[_pid] = float(_r.get('G(㎡)', 0) or 0)`；末句皆回
        {'kept': _kept, 'bad_pools': _bad, 'err': _err, 'G': _G}；`_G` 之初值 {}。
    W9  `R-11` 落點：k6b_stage3_pool_temp 之諸句（見 _R11）皆在；`_tp = dict(tp)`（淺拷貝）；二面積欄各乘 _rho。
    W10 `R-12` 落點：adj_intake 內 X-4 四字樣各恰 1（全檔亦恰 1）；`_s3_ids.add(_k)` 恰 2；① 之 `_row.update(類=
        ADJ_DISP_COMMON_UNIT, 原有面積=_a(t) * _rho, 段三併出面積=_a(t) * (1.0 - _rho))` 在 `if '段三併出' in t:` 內；
        `_s3` 之分在 `if _pool or (_cm and not _al):` 之 else，另成之單位之 '軌' ＝ ADJ_TRACK_PUBLIC、'共同負擔用地' ＝ _s3；
        `_tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']`。
    W11 `R-8` 鍵：k6b_stage3_run 本體恰一 `for _pid in sorted(set(marks) | set(_left)):`，在 `for _pid, _rs in marks.items():`
        之後；三支：有剩下且在 marks ⇒ 寫二鍵；有剩下 ⇒ 去 段三部分併出、段三餘量 ＝ round(_a357(_pid), 4)；否則去二鍵。
    W12 `R-3`／`R-4` 步驟 10：`for p in _plan:` 之本體中 `if not _qs:` → `if not _batch_ok and not _whole:`（本體 ＝
        _split357(x, _qs, _lvl_name[_cl2], _extra)；continue）→ `if _batch_ok:` 依序；`if _ok:` 之 else ＝
        `_row(**_base, 結果='未成', 檢核='不過')`；`_k951(x, _a357(x), {…}, True)`。
    本部全綠時另施 29 種原始碼突變，每一突變須使其所指之項轉紅（器紅 ⇒ rc 1）。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import ast, contextlib, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FA, FS = "app.py", "verify/selection_pipeline.py"
FN_S3, FN_AI, FN_CB = "k6b_stage3_run", "adj_intake", "k6b_screen_callbacks"
FN_PT, FN_HCB = "k6b_stage3_pool_temp", "_k6b_callbacks"
NEST = ("_has357", "_res357", "_max357", "_dist357", "_k951", "_split357", "_t14_357")
X4 = ("float(_r['應分配面積'])", "if _pool or (_cm and not _al):", "if '段三併出' in t:", "if len(_cands) != 1:")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


# ── AST 之小工具 ──
def _u(n):
    try:
        return ast.unparse(n)
    except Exception:  # noqa: BLE001
        return "<?>"


def _n(src):
    """期之字樣之正規形（以 ast.unparse 之形比較·例 `a and not b` ⇒ `a and (not b)`）。"""
    return ast.unparse(ast.parse(src, mode="eval").body)


def _top(tree):
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


def _walk_own(fn):
    """fn 之節點，⛔ 入巢狀之 def／lambda。"""
    todo = [s for s in fn.body if not isinstance(s, (ast.FunctionDef, ast.AsyncFunctionDef))]
    while todo:
        n = todo.pop()
        yield n
        for c in ast.iter_child_nodes(n):
            if not isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                todo.append(c)


def _defs(node, name):
    return [n for n in ast.walk(node) if isinstance(n, ast.FunctionDef) and n.name == name]


def _is_call(n, name):
    return isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == name


def _parents(root):
    return {c: p for p in ast.walk(root) for c in ast.iter_child_nodes(p)}


def _in_branch(node, par, test_src, branch):
    """node 之某祖為 If（其 test 之 unparse ＝ test_src），且 node 在其 branch（'body'／'orelse'）之下。"""
    cur = node
    while cur in par:
        p = par[cur]
        if isinstance(p, ast.If) and _u(p.test) == _n(test_src):
            if any(cur is s for s in getattr(p, branch)):
                return True
        cur = p
    return False


def _stmts(fn, own=True):
    it = _walk_own(fn) if own else ast.walk(fn)
    return [n for n in it if isinstance(n, ast.stmt)]


def _ifs(fn, own=True):
    return [n for n in (_walk_own(fn) if own else ast.walk(fn)) if isinstance(n, ast.If)]


def _strs(node):
    return [n.value for n in ast.walk(node) if isinstance(n, ast.Constant) and isinstance(n.value, str)]


class _Ctx:
    def __init__(self, sa, ss):
        self.ta, self.ts = ast.parse(sa), ast.parse(ss)
        self.top_a, self.top_s = _top(self.ta), _top(self.ts)
        self.s3 = self.top_a.get(FN_S3)
        self.n = {}
        if self.s3 is not None:
            for nm in NEST:
                d = _defs(self.s3, nm)
                if len(d) == 1:
                    self.n[nm] = d[0]


# ── 接線 ──
def _w0(c):
    miss = [f for f in (FN_S3, FN_AI, FN_CB) if f not in c.top_a] + [f for f in (FN_PT, FN_HCB) if f not in c.top_s]
    bad = []
    for nm in NEST:
        tot = len(_defs(c.ta, nm))
        ins = len(_defs(c.s3, nm)) if c.s3 is not None else 0
        if not (tot == 1 and ins == 1):
            bad.append((nm, tot, ins))
    return (not miss and not bad), f"缺 {miss}；巢狀（名, 全檔, 段三內）之不符 {bad}"


def _w1(c):
    s3 = c.s3
    kws = [n for n in ast.walk(s3) if isinstance(n, ast.keyword) and n.arg == "結果"
           and isinstance(n.value, ast.Constant) and n.value.value == "未處置"]
    ifs = [n for n in ast.walk(s3) if isinstance(n, ast.If) and _u(n.test) == "not _qs"]
    old = [s for s in _strs(s3) if "未處置：「不影響原位次」不過" in s]
    if len(kws) != 1 or len(ifs) != 1:
        return False, f"結果='未處置' {len(kws)}（期 1）；`if not _qs:` {len(ifs)}（期 1）"
    body = ifs[0].body
    in_body = any(kws[0] in list(ast.walk(s)) for s in body)
    lp = any(_is_call(n, "log_print") and any("未處置：二半片皆不鄰 B 內街廓" in v for v in _strs(n))
             for s in body for n in ast.walk(s))
    cont = isinstance(body[-1], ast.Continue)
    ok = in_body and lp and cont and not old
    return ok, f"在 `if not _qs:` {in_body}；log_print {lp}；continue {cont}；舊字樣 {len(old)}（期 0）"


def _div100(n):
    return (isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div) and isinstance(n.right, ast.Constant)
            and n.right.value in (100, 100.0))


def _w2(c):
    mx = c.n["_max357"]
    tr = _defs(mx, "_try")
    if len(tr) != 1:
        return False, f"_try {len(tr)}（期 1）"
    tr = tr[0]
    rets = [r for r in ast.walk(tr) if isinstance(r, ast.Return)]
    r_ok = (len(rets) == 1 and isinstance(rets[0].value, ast.IfExp) and _is_call(rets[0].value.test, "_noaff")
            and _u(rets[0].value.body) == "_t" and _u(rets[0].value.orelse) == "None")
    tr_src = [_u(s) for s in tr.body]
    clone = "_t = _clone(state)" in tr_src and any(s.startswith("_apply(_t, ") for s in tr_src)
    par = _parents(mx)
    own = list(_walk_own(mx))
    sa = [a for a in own if isinstance(a, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "state" for t in a.targets)]
    sa_ok = len(sa) == 2 and all(isinstance(a.value, ast.Name) and a.value.id in ("_t", "_best")
                                 and isinstance(par.get(a), ast.If) and any(a is s for s in par[a].body)
                                 and _u(par[a].test) == f"{a.value.id} is not None" for a in sa)
    t_from = any(isinstance(a, ast.Assign) and _u(a) == "_t = _try(s)" for a in own)
    tries = [n for n in own if _is_call(n, "_try")]
    tm = [a for a in own if isinstance(a, ast.Assign) and _u(a.targets[0]) == "_tm"]
    tm_ok = len(tm) == 1 and _is_call(tm[0].value, "_try") and len(tm[0].value.args) == 1 and _div100(tm[0].value.args[0])
    best = []
    for a in own:
        if isinstance(a, ast.Assign):
            for t in a.targets:
                if isinstance(t, ast.Name) and t.id == "_best":
                    best.append((a, _u(a.value)))
                if isinstance(t, ast.Tuple) and isinstance(a.value, ast.Tuple):
                    for te, ve in zip(t.elts, a.value.elts):
                        if isinstance(te, ast.Name) and te.id == "_best":
                            best.append((a, _u(ve)))
    b_ok = bool(best) and all(v == "None" or (v == "_tm" and _in_branch(a, par, "_tm is not None", "body"))
                              for a, v in best) and any(v == "_tm" for _, v in best)
    last = mx.body[-1]
    l_ok = (isinstance(last, ast.Return) and _div100(last.value) and _u(last.value.left) == "_lo")
    ok = r_ok and clone and sa_ok and t_from and len(tries) == 2 and tm_ok and b_ok and l_ok
    return ok, (f"_try 之 return {r_ok}；試算於拷貝 {clone}；state＝ {len(sa)}／受護 {sa_ok}；_t＝_try(s) {t_from}；"
                f"_try 呼 {len(tries)}（期 2）；_tm＝_try(n/100) {tm_ok}；_best 唯取已通過者 {b_ok}；return _lo/100 {l_ok}")


def _w3(c):
    k = c.n["_k951"]
    own = list(_walk_own(k))
    par = _parents(k)
    als = [n for n in own if _is_call(n, "alloc_state")]
    al_ok = len(als) == 1 and [_u(a) for a in als[0].args] == ["state['temp']", "state['build']"]
    err = any(isinstance(n, ast.If) and _u(n.test) == "_cur.get('err')" and isinstance(n.body[0], ast.Raise) for n in own)
    want = {"_p == x", "_p in merged_out", "_b in F", "_p not in state['by']"}
    flt = [n for n in own if isinstance(n, ast.If) and isinstance(n.test, ast.BoolOp) and isinstance(n.test.op, ast.Or)
           and {_u(v) for v in n.test.values} == want and len(n.body) == 1 and isinstance(n.body[0], ast.Continue)]
    gx = [n for n in own if isinstance(n, ast.If) and isinstance(n.test, ast.Compare)
          and isinstance(n.test.ops[0], ast.NotEq) and _u(n.test.comparators[0]) == "_gx"
          and len(n.body) == 1 and isinstance(n.body[0], ast.Continue)]
    gets = [n for n in own if isinstance(n, ast.Assign) and _u(n) == "_G = _cur.get('G')"]
    anyg = [n for n in own if isinstance(n, ast.Call) and _u(n.func) == "_cur.get" and n.args
            and isinstance(n.args[0], ast.Constant) and n.args[0].value == "G"]
    g_ok = len(gets) == 1 and len(anyg) == 1 and _in_branch(gets[0], par, "_pre", "body")
    rz = [n for n in own if isinstance(n, ast.Raise) and any("未回 G" in s for s in _strs(n))]
    rz_ok = len(rz) >= 2 and all(_in_branch(r, par, "_pre", "body") for r in rz)
    ap = [n for n in own if isinstance(n, ast.Call) and _u(n.func) == "_cands.append"]
    ap_ok = False
    if len(ap) == 1 and len(ap[0].args) == 1 and isinstance(ap[0].args[0], ast.Tuple):
        e = ap[0].args[0].elts
        ap_ok = (len(e) >= 3 and _is_call(e[0], "_dist357") and _u(e[1]) == "-float(_G[_p])" and _u(e[2]) == "_p"
                 and _in_branch(ap[0], par, "_pre", "body"))
    so = [n for n in own if isinstance(n, ast.Call) and _u(n.func) == "_cands.sort"]
    so_ok = len(so) == 1 and not so[0].args and not so[0].keywords
    ok = al_ok and err and len(flt) == 1 and len(gx) == 1 and g_ok and rz_ok and ap_ok and so_ok
    return ok, (f"alloc_state 一呼 {al_ok}；err ⇒ raise {err}；篩 {len(flt)}（期 1）；歸戶 {len(gx)}（期 1）；"
                f"取 G 唯於 `if _pre:` {g_ok}；未回 G 之 raise {len(rz)}／皆於其內 {rz_ok}；序之鍵 {ap_ok}；sort 無 key {so_ok}")


def _w4(c):
    d = c.n["_dist357"]
    al = {}
    for n in list(ast.walk(d)) + list(c.ta.body):
        if isinstance(n, ast.ImportFrom) and n.module == "decimal":
            for a in n.names:
                al[a.asname or a.name] = a.name
    dec = {k for k, v in al.items() if v == "Decimal"}
    hu = {k for k, v in al.items() if v == "ROUND_HALF_UP"}
    last = d.body[-1]
    ok_ret = False
    if isinstance(last, ast.Return) and _is_call(last.value, "float") and len(last.value.args) == 1:
        q = last.value.args[0]
        if isinstance(q, ast.Call) and isinstance(q.func, ast.Attribute) and q.func.attr == "quantize":
            inner = q.func.value
            ok_ret = (isinstance(inner, ast.Call) and isinstance(inner.func, ast.Name) and inner.func.id in dec
                      and len(inner.args) == 1 and _is_call(inner.args[0], "repr")
                      and len(q.args) == 1 and isinstance(q.args[0], ast.Call) and isinstance(q.args[0].func, ast.Name)
                      and q.args[0].func.id in dec and _u(q.args[0].args[0]) == "'0.01'"
                      and [(kw.arg, _u(kw.value)) for kw in q.keywords] in ([("rounding", h)] for h in hu))
    rnd = [n for n in ast.walk(d) if _is_call(n, "round")]
    un = any(isinstance(n, ast.Assign) and _u(n.targets[0]) == "_gs" and "_blk_of[p] == blk" in _u(n.value)
             and "_geo" in _u(n.value) for n in ast.walk(d))
    ok = ok_ret and not rnd and un
    return ok, f"ROUND_HALF_UP 之式 {ok_ret}；round 之呼 {len(rnd)}（期 0）；街廓之全部切片 {un}"


def _w5(c):
    s3, t = c.s3, c.n["_t14_357"]
    old = [s for s in _strs(c.ta) if "七項 3〜5 未落地" in s]
    par = _parents(s3)
    r4 = [n for n in ast.walk(s3) if isinstance(n, ast.Assign) and _u(n) == "_r4 = None"]
    r4_ok = len(r4) == 1 and _in_branch(r4[0], par, "_noaff(state, _t2, {W['blk'], _lb}, {Lo['c']})", "orelse")
    cl = [n for n in ast.walk(s3) if _is_call(n, "_t14_357")]
    cl_ok = len(cl) == 1 and _in_branch(cl[0], par, "_r4 is not None", "orelse")
    asg = [n for n in ast.walk(s3) if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign))
           and "_t14_done" in [_u(x) for x in (n.targets if isinstance(n, ast.Assign) else [n.target])]]
    asg_ok = len(asg) == 1 and _u(asg[0]) == "_t14_done = set()" and any(asg[0] is s for s in s3.body)
    mut = [n for n in ast.walk(s3) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
           and _u(n.func.value) == "_t14_done"]
    add = [s for s in t.body if isinstance(s, ast.Expr) and _u(s) == "_t14_done.add(c)"]
    first_if = next((i for i, s in enumerate(t.body) if isinstance(s, ast.If)), len(t.body))
    add_ok = len(mut) == 1 and len(add) == 1 and t.body.index(add[0]) < first_if
    tp = _parents(t)
    kc = [n for n in ast.walk(t) if isinstance(n, ast.Call) and _u(n) == "_k951(c, _a357(c), {W['blk']}, True)"]
    kc_ok = len(kc) == 1 and _in_branch(kc[0], tp, "_noaff(state, _t, {W['blk'], _blk_of[c]}, {c})", "orelse")
    mx = [n for n in ast.walk(t) if isinstance(n, ast.Call) and _u(n) == "_max357(x, w, _s)"]
    kx = [n for n in ast.walk(t) if isinstance(n, ast.Call) and _u(n) == "_k951(x, _rem, {W['blk']}, False)"]
    kx_ok = len(kx) == 1 and _in_branch(kx[0], tp, "_has357(_rem)", "body")
    ok = not old and r4_ok and cl_ok and asg_ok and add_ok and kc_ok and len(mx) == 1 and kx_ok
    return ok, (f"舊 raise 之字樣 {len(old)}（期 0）；_r4＝None 於合併不過 {r4_ok}；_t14_357 一呼於其 else {cl_ok}；"
                f"_t14_done 唯 set() {asg_ok}；唯 .add(c) 於頂層先於 if {add_ok}（方法呼 {len(mut)}）；"
                f"c 不過 ⇒ 第 5 項 {kc_ok}；半之最大面積 {len(mx)}（期 1）；半之剩下 ⇒ 第 5 項 {kx_ok}")


def _w6(c):
    rs = [_u(n) for n in _walk_own(c.s3) if isinstance(n, ast.Assign) and _u(n.targets[0]) == "R"]
    want = ["R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done", "R = R - _stay"]
    return sorted(rs) == sorted(want), f"R 之賦值 {rs}"


_R15 = {"_res357": {"not _has357(s - g)"}, "_split357": {"_has357(_s - _g)", "_has357(_rem)"},
        "_k951": {"not _has357(_rem)", "_has357(_rem)"}, "_t14_357": {"_has357(_rem)"}}


def _keyloop(s3):
    return [n for n in _walk_own(s3) if isinstance(n, ast.For) and _u(n.iter) == "sorted(set(marks) | set(_left))"]


def _tiny(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Compare):
            for x in [n.left] + list(n.comparators):
                v = x.operand.value if (isinstance(x, ast.UnaryOp) and isinstance(x.operand, ast.Constant)) else \
                    (x.value if isinstance(x, ast.Constant) else None)
                if isinstance(v, float) and 0 < abs(v) < 1e-3:
                    out.append(_u(n))
    return out


def _w7(c):
    h = c.n["_has357"]
    h_ok = [a.arg for a in h.args.args] == ["r"] and len(h.body) >= 1 and _u(h.body[-1]) == "return round(float(r), 4) > 0" \
        and all(isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) for s in h.body[:-1])
    eps = [n for n in ast.walk(c.ta) if isinstance(n, ast.Name) and n.id == "_EPS357"]
    kl = _keyloop(c.s3)
    places = [(nm, c.n[nm]) for nm in _R15] + [("鍵之環", kl[0])] if len(kl) == 1 else [(nm, c.n[nm]) for nm in _R15]
    tiny = {nm: _tiny(fn) for nm, fn in places if _tiny(fn)}
    need = dict(_R15)
    need["鍵之環"] = {"_has357(_rm) and _pid in marks", "_has357(_rm)"}
    miss = {}
    for nm, fn in places:
        tests = {_u(n.test) for n in ast.walk(fn) if isinstance(n, ast.If)}
        lack = {_n(x) for x in need[nm]} - tests
        if lack:
            miss[nm] = sorted(lack)
    sp = [n for n in ast.walk(c.n["_split357"]) if isinstance(n, ast.If) and _u(n.test) == "_has357(_s - _g)"]
    sp_ok = len(sp) == 1 and any(_u(s).startswith("_F.add(") for s in sp[0].body) and \
        any(_u(s) == "_rem += _s - _g" for s in sp[0].body)
    ok = h_ok and not eps and len(kl) == 1 and not tiny and not miss and sp_ok
    return ok, (f"_has357 之式 {h_ok}；_EPS357 {len(eps)}（期 0）；浮點小量之比較 {tiny}；缺判 {miss}；"
                f"分之剩下始入已試之街廓 {sp_ok}")


def _alloc_parts(fn):
    a = _defs(fn, "alloc_state")
    if len(a) != 1:
        return None
    a = a[0]
    el = [n for n in ast.walk(a) if isinstance(n, ast.If) and _u(n.test) == "_r.get('驗_總判') == '保留'"]
    init = [n for n in ast.walk(a) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple)
            and "_G" in [_u(x) for x in n.targets[0].elts]]
    g0 = None
    if len(init) == 1 and isinstance(init[0].value, ast.Tuple):
        m = dict(zip([_u(x) for x in init[0].targets[0].elts], [_u(x) for x in init[0].value.elts]))
        g0 = m.get("_G")
    last = a.body[-1]
    ret = None
    if isinstance(last, ast.Return) and isinstance(last.value, ast.Dict):
        ret = [(_u(k), _u(v)) for k, v in zip(last.value.keys, last.value.values)]
    return ([ast.dump(s) for s in el[0].body] if len(el) == 1 else None), \
        ([_u(s) for s in el[0].body] if len(el) == 1 else None), g0, ret


def _w8(c):
    pa, ps = _alloc_parts(c.top_a[FN_CB]), _alloc_parts(c.top_s[FN_HCB])
    if pa is None or ps is None:
        return False, f"alloc_state 之巢狀 def 不恰 1（app {pa is not None}／harness {ps is not None}）"
    want_ret = [("'kept'", "_kept"), ("'bad_pools'", "_bad"), ("'err'", "_err"), ("'G'", "_G")]
    need = {"_kept.setdefault(_blk, set()).add(_pid)", "_G[_pid] = float(_r.get('G(㎡)', 0) or 0)"}
    same = pa[0] is not None and pa[0] == ps[0]
    has = pa[1] is not None and need <= set(pa[1])
    ok = same and has and pa[2] == "{}" and ps[2] == "{}" and pa[3] == want_ret and ps[3] == want_ret
    return ok, (f"保留之支逐 AST 同 {same}；含 kept 與 G {has}；_G 之初值 {pa[2]}／{ps[2]}；"
                f"回傳之鍵 app {pa[3] == want_ret}／harness {ps[3] == want_ret}")


_R11 = ["_out = []", "_out.append(tp)", "_rem = float(tp.get('段三餘量', 0) or 0)",
        "_a = float(tp.get('分攤登記面積_m2', 0) or 0) + float(tp.get('面積_m2', 0) or 0)", "_rho = _rem / _a",
        "_tp = dict(tp)", "_tp['分攤登記面積_m2'] = float(tp.get('分攤登記面積_m2', 0) or 0) * _rho",
        "_tp['面積_m2'] = float(tp.get('面積_m2', 0) or 0) * _rho", "_out.append(_tp)", "return _out"]


def _w9(c):
    f = c.top_s[FN_PT]
    st = [_u(s) for s in ast.walk(f) if isinstance(s, ast.stmt) and not isinstance(s, (ast.For, ast.If))]
    miss = [s for s in _R11 if s not in st]
    tests = [(_u(n.test), [_u(s) for s in n.body]) for n in ast.walk(f) if isinstance(n, ast.If)]
    t1 = ("'段三併出' not in tp", ["_out.append(tp)", "continue"]) in tests
    t2 = ("not _rem > 0", ["continue"]) in tests
    return (not miss and t1 and t2), f"缺句 {miss}；無段三併出 ⇒ 原物件 {t1}；無剩下 ⇒ 去 {t2}"


def _w10(c, sa):
    ai = c.top_a[FN_AI]
    seg = ast.get_source_segment(sa, ai) or ""
    x4 = [(s, sa.count(s), seg.count(s)) for s in X4]
    x4_ok = all(a == 1 and b == 1 for _, a, b in x4)
    par = _parents(ai)
    adds = [n for n in ast.walk(ai) if isinstance(n, ast.Call) and _u(n) == "_s3_ids.add(_k)"]
    ini = [n for n in ast.walk(ai) if isinstance(n, ast.Assign) and _u(n) == "_s3_ids = set()"]
    up = [n for n in ast.walk(ai) if isinstance(n, ast.Expr) and _u(n) ==
          "_row.update(類=ADJ_DISP_COMMON_UNIT, 原有面積=_a(t) * _rho, 段三併出面積=_a(t) * (1.0 - _rho))"]
    up_ok = len(up) == 1 and _in_branch(up[0], par, "'段三併出' in t", "body")
    rho = any(isinstance(n, ast.Assign) and _u(n) == "_rho = _rem3 / _den" for n in ast.walk(ai))
    s3 = [n for n in ast.walk(ai) if isinstance(n, ast.Assign) and _u(n) ==
          "_s3 = [_r for _r in _cm if _r['暫編地號'] in _s3_ids]"]
    s3_ok = len(s3) == 1 and _in_branch(s3[0], par, "_pool or (_cm and not _al)", "orelse")
    un = []
    for n in ast.walk(ai):
        if isinstance(n, ast.Call) and _u(n.func) == "_units.append" and n.args and isinstance(n.args[0], ast.Dict):
            d = {_u(k): _u(v) for k, v in zip(n.args[0].keys, n.args[0].values)}
            if d.get("'共同負擔用地'") == "_s3":
                un.append(d)
    un_ok = len(un) == 1 and un[0].get("'軌'") == "ADJ_TRACK_PUBLIC" and un[0].get("'原街廓'") == "None"
    tot = any(isinstance(n, ast.AugAssign) and _u(n) == "_tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']"
              for n in ast.walk(ai))
    ok = x4_ok and len(adds) == 2 and len(ini) == 1 and up_ok and rho and s3_ok and un_ok and tot
    return ok, (f"X-4（字樣, 全檔, adj_intake）{x4 if not x4_ok else '皆 1'}；_s3_ids 之加 {len(adds)}（期 2）；"
                f"① 之落點 {up_ok}；ρ {rho}；不成單位者之分 {s3_ok}；另成單位（公設軌） {un_ok}；總計之面積 {tot}")


def _w11(c):
    s3 = c.s3
    kl = _keyloop(s3)
    if len(kl) != 1:
        return False, f"鍵之環 {len(kl)}（期 1）"
    kl = kl[0]
    mk = [n for n in s3.body if isinstance(n, ast.For) and _u(n.iter) == "marks.items()"]
    order_ok = len(mk) == 1 and kl in s3.body and s3.body.index(mk[0]) < s3.body.index(kl)
    ifs = [s for s in kl.body if isinstance(s, ast.If)]
    ok3 = False
    if len(ifs) == 1 and _u(ifs[0].test) == "_has357(_rm) and _pid in marks":
        a = [_u(s) for s in ifs[0].body]
        e = ifs[0].orelse
        if len(e) == 1 and isinstance(e[0], ast.If) and _u(e[0].test) == "_has357(_rm)":
            b = [_u(s) for s in e[0].body]
            z = [_u(s) for s in e[0].orelse]
            ok3 = (any(s.startswith("_tp['段三部分併出'] = ") for s in a) and "_tp['段三餘量'] = round(_rm, 4)" in a
                   and b == ["_tp.pop('段三部分併出', None)", "_tp['段三餘量'] = round(_a357(_pid), 4)"]
                   and z == ["_tp.pop('段三部分併出', None)", "_tp.pop('段三餘量', None)"])
    return order_ok and ok3, f"序於 段三併出 之後 {order_ok}；三支 {ok3}"


def _w12(c):
    s3 = c.s3
    lp = [n for n in _walk_own(s3) if isinstance(n, ast.For) and _u(n.target) == "p" and _u(n.iter) == "_plan"]
    if len(lp) != 1:
        return False, f"`for p in _plan:` {len(lp)}（期 1）"
    body = lp[0].body
    ix = {_u(s.test): i for i, s in enumerate(body) if isinstance(s, ast.If)}
    i1, i2, i3 = ix.get(_n("not _qs")), ix.get(_n("not _batch_ok and not _whole")), ix.get(_n("_batch_ok"))
    seq = None not in (i1, i2, i3) and i1 < i2 < i3
    sp = seq and [_u(s) for s in body[i2].body] == ["_split357(x, _qs, _lvl_name[_cl2], _extra)", "continue"]
    ko = [s for s in body if isinstance(s, ast.If) and _u(s.test) == "_ok"]
    k_ok = False
    if len(ko) == 1:
        e = [_u(s) for s in ko[0].orelse]
        k_ok = (len(e) == 2 and e[0] == "_row(**_base, 結果='未成', 檢核='不過')"
                and e[1] == "_k951(x, _a357(x), {_blk_of[r] for r, _ in _qs}, True)")
    return bool(seq and sp and k_ok), f"三 if 之序 {seq}；可拆分 ⇒ _split357 {bool(sp)}；整筆不過 ⇒ 第 5 項 {k_ok}"


def _checks(sa, ss):
    try:
        c = _Ctx(sa, ss)
    except SyntaxError as e:
        return [("W0 可剖析", False, f"{e}")]
    res = []
    items = (("W0 受詞在", lambda: _w0(c)), ("W1 R-2 未處置不變", lambda: _w1(c)),
             ("W2 R-5 所施者恆已通過", lambda: _w2(c)), ("W3 R-6 候選與序", lambda: _w3(c)),
             ("W4 R-6′ 距離之取捨", lambda: _w4(c)), ("W5 R-7／R-7′ 題一 4", lambda: _w5(c)),
             ("W6 X-3′ 步驟 10 之 R", lambda: _w6(c)), ("W7 R-15 剩下之判準", lambda: _w7(c)),
             ("W8 R-10 二處同形", lambda: _w8(c)), ("W9 R-11 公設地調配之 temp", lambda: _w9(c)),
             ("W10 R-12 調配之輸入", lambda: _w10(c, sa)), ("W11 R-8 片之鍵", lambda: _w11(c)),
             ("W12 R-3／R-4 步驟 10 之逐片", lambda: _w12(c)))
    for name, fn in items:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ok, note = fn()
        except Exception as e:  # noqa: BLE001
            ok, note = False, f"器拋 {type(e).__name__}: {e}"
        res.append((name, ok, note))
    return res


# ── 突變（每一須使其所指之項轉紅）── 各為 (名, 所指之項, [(檔, 錨, 代)])
def _mut_list():
    return [
        ("M1 無受併宗之片改記未成", "W1",
         [(FA, "_row(**{**_base, '受併宗': '—'}, 結果='未處置', 檢核='—')", "_row(**{**_base, '受併宗': '—'}, 結果='未成', 檢核='—')")]),
        ("M2 無受併宗之片⛔ continue", "W1",
         [(FA, "（{_blk_of[x]}）未處置：二半片皆不鄰 B 內街廓\")\n                continue\n",
           "（{_blk_of[x]}）未處置：二半片皆不鄰 B 內街廓\")\n")]),
        ("M3 二分法取未通過之格", "W2",
         [(FA, "            if _tm is not None:\n                _lo, _best = _mid, _tm",
           "            if _tm is not None or _mid == _hi:\n                _lo, _best = _mid, _tm")]),
        ("M4 所施者⛔ 受護", "W2",
         [(FA, "        if _best is not None:\n            state = _best\n", "        state = _best or state\n")]),
        ("M5 格值改 n × 0.01", "W2", [(FA, "_tm = _try(_mid / 100.0)", "_tm = _try(_mid * 0.01)")]),
        ("M6 序之鍵以 G 先", "W3",
         [(FA, "_cands.append((_dist357(x, _b), -float(_G[_p]), _p, _b))", "_cands.append((-float(_G[_p]), _dist357(x, _b), _p, _b))")]),
        ("M7 候選⛔ 扣已試之街廓", "W3",
         [(FA, "if _p == x or _p in merged_out or _b in F or _p not in state[\"by\"]:",
           "if _p == x or _p in merged_out or _p not in state[\"by\"]:")]),
        ("M8 候選為空亦取 G", "W3", [(FA, "        _cands = []\n        if _pre:\n", "        _cands = []\n        if True:\n")]),
        ("M9 候選⛔ 扣已併出者", "W3",
         [(FA, "if _p == x or _p in merged_out or _b in F or _p not in state[\"by\"]:",
           "if _p == x or _b in F or _p not in state[\"by\"]:")]),
        ("M10 距離以 round", "W4",
         [(FA, "return float(_Dec357(repr(_d)).quantize(_Dec357('0.01'), rounding=_HU357))", "return round(_d, 2)")]),
        ("M11 距離以 Decimal(float)", "W4", [(FA, "_Dec357(repr(_d))", "_Dec357(_d)")]),
        ("M12 距離以 ROUND_HALF_EVEN", "W4",
         [(FA, "from decimal import Decimal as _Dec357, ROUND_HALF_UP as _HU357",
           "from decimal import Decimal as _Dec357, ROUND_HALF_EVEN as _HU357")]),
        ("M13 R-7 之候選⛔ 入已處置之集", "W5", [(FA, "        _t14_done.add(c)    #", "        pass    #")]),
        ("M14 R-7 之候選於第 5 項後出集", "W5",
         [(FA, "            _k951(c, _a357(c), {W['blk']}, True)\n",
           "            _k951(c, _a357(c), {W['blk']}, True)\n            _t14_done.discard(c)\n")]),
        ("M15 題一 4 之合併不過復停機", "W5",
         [(FA, "                    _r4 = None\n",
           "                    raise RuntimeError(\"🔴 [K-6-B 段三 K-9-50 題一] `K-9-48` 七項 3〜5 未落地（停機款 9）\")\n")]),
        ("M16 候選之整筆不過⛔ 第 5 項", "W5", [(FA, "            _k951(c, _a357(c), {W['blk']}, True)\n", "            pass\n")]),
        ("M17 步驟 10 之 R ⛔ 扣已處置之候選", "W6",
         [(FA, "R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done", "R = _mem - merged_out - set(_recv_by_blk.values()) - L")]),
        ("M18 有剩下以 1e-6 判", "W7", [(FA, "return round(float(r), 4) > 0", "return float(r) > 1e-6")]),
        ("M19 分之剩下以 g < s 判", "W7", [(FA, "            if _has357(_s - _g):\n", "            if _g < _s:\n")]),
        ("M20 鍵之環以 1e-6 判", "W7",
         [(FA, "        if _has357(_rm) and _pid in marks:\n", "        if _rm > 1e-6 and _pid in marks:\n")]),
        ("M21 畫面之 G 取他欄", "W8", [(FA, "_G[_pid] = float(_r.get('G(㎡)', 0) or 0)", "_G[_pid] = float(_r.get('G', 0) or 0)")]),
        ("M22 harness 之 alloc_state ⛔ 回 G", "W8",
         [(FS, "return {\"kept\": _kept, \"bad_pools\": _bad, \"err\": _err, \"G\": _G}",
           "return {\"kept\": _kept, \"bad_pools\": _bad, \"err\": _err}")]),
        ("M23 公設地調配之 temp 改原物件", "W9", [(FS, "_tp = dict(tp)", "_tp = tp")]),
        ("M24 面積_m2 ⛔ 乘 ρ", "W9",
         [(FS, "_tp[\"面積_m2\"] = float(tp.get(\"面積_m2\", 0) or 0) * _rho", "_tp[\"面積_m2\"] = float(tp.get(\"面積_m2\", 0) or 0)")]),
        ("M25 一分未併者⛔ 入合併單位", "W10",
         [(FA, "            _row['類'] = ADJ_DISP_COMMON_UNIT\n            _s3_ids.add(_k)\n", "            _row['類'] = ADJ_DISP_COMMON_UNIT\n")]),
        ("M26 已併出之量⛔ 計入原位次配地", "W10",
         [(FA, "            _tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']\n", "            pass\n")]),
        ("M27 剩下全收者⛔ 去 段三餘量", "W11",
         [(FA, "            _tp.pop('段三部分併出', None)\n            _tp.pop('段三餘量', None)\n",
           "            _tp.pop('段三部分併出', None)\n")]),
        ("M28 可拆分者⛔ 經 _split357", "W12",
         [(FA, "                _split357(x, _qs, _lvl_name[_cl2], _extra)\n                continue\n", "                pass\n")]),
        ("M29 整筆不過⛔ 第 5 項", "W12",
         [(FA, "                _k951(x, _a357(x), {_blk_of[r] for r, _ in _qs}, True)\n", "                pass\n")]),
    ]


def wiring(repo):
    src = {FA: _read(repo, FA), FS: _read(repo, FS)}
    red = []
    print("── 接線（AST·工作樹之 app.py ＋ verify/selection_pipeline.py）──")
    for name, ok, note in _checks(src[FA], src[FS]):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    if red:
        print("── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（每一突變須使其所指之項轉紅）──")
    for mname, target, reps in _mut_list():
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
        turned = [n.split()[0] for n, ok, _ in _checks(m[FA], m[FS]) if not ok]
        ok = target in turned
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}（須含 {target}）")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) != 3 or argv[1] != "wiring":
        print(__doc__)
        return 2
    return wiring(argv[2])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `E6`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-358 §零-1`）：本批取 `549`／`550`（`2` 號）；皆係發單側窗五十四於擬 `W-G.9-357` 補令一時所捕（全文逐字載於 `docs/orders/W-G.9-357_補令一.md` `§六` 甲／乙·候鑄），本批依之鑄號、⛔ 增刪其一字；各條末之「字樣之錨」係本批所附。

### 🩸 `自誤 549`　**`W-G.9-357` `R-7` 令題一 `4` 之候選 `c` 轉調配時「整筆者維持原狀（仍在 build）」，未查步驟 `10` 之取片之式仍取 `c` ⇒ 同一筆土地於一趟之內被處置二次**

**形**：原單 `R-6` ⑤「整筆者維持原狀（仍在 build）」、`R-7` ①「不過 ⇒ `R-6`」；步驟 `10` 之 `R = _mem - merged_out - set(_recv_by_blk.values()) - L`（`X-3` 所護）⛔ 扣之 ⇒ `c` 經 `_cls['a']` 之 `_cl0['敗']` 分支再度計劃整筆併入 `w`，再經 `R-3`／`R-6`，再記一列「轉調配」。發單側窗五十四以 `F16` 之 `_go4`（容量 `BX 60`／`BY 1000`／`B7 50`）於首輪之碼復現：`Y1` 之列 `6`、「轉調配」`2`。
**後果之界**：本案⛔ 觸（無題一之競合）；他案：同一土地之紀錄重複，且其第二次之試於另一現態為之（檢核非單調時土地結果可異）。零入倉之生產碼（CC 停機·`f099d04` 未推）。
**根因**：擬 `R-7` 時，未以步驟 `10` 之取片之式逐一核 `R-7` 各出口之成員（通過 ⇒ `merged_out`；第 `5` 項成 ⇒ `merged_out`；轉調配 ⇒ 仍在 build ⇒ 入 `R`）；原型與 `F16` 之 `K17`／`K18` 皆為第 `5` 項成之形，未造轉調配之形 ⇒ 量測器之母體亦漏之。
**後果之框**：🟢 本案零土地後果；🟡 他案之紀錄與土地結果。攔點 ＝ CC 所派之獨立 reviewer（唯讀）→ CC 停機款 `5`。
**攔法**：本補令 `R-7′`／`X-3′`、`F16` 之 `K19`。通則：凡規格令某片「維持原狀」者，須逐一查其後各步之取片之式是否再取之，並於量測器造其形。
**字樣之錨**（`W-G.9-358`）：量測器 `F17`（`verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`）之 `W5`（`R-7′`·突變 `M13`〜`M16`）與 `W6`（`X-3′`·突變 `M17`）。

---

### 🩸 `自誤 550`　**`W-G.9-357` 以 `1e-6 ㎡` 判剩下（`R-4`／`R-6`／`R-8`），而以四位小數寫之（`R-8`／`R-9`）、以 `＞ 0` 讀之（`R-11`／`R-12`）⇒ 剩下 `∈ (1e-6, 5e-5)` 時三者不一**

**形**：CC 報告 `§六-2`（常規二·取保守項）；reviewer 以 `P1 ＝ 200.00006` 等之合成案實得「轉調配 `餘量 0.0`」與 `段三餘量 0.0` 並存、調配之輸入歸原位次配地。發單側窗五十四以 `F16` 之 `_go`（`B3 160`／`B5 100.00003`／`B7 0`·`P1 200.00006`）於首輪之碼復現：`部分成` ＋ 第 `5` 項三列 ＋ 轉調配、鍵 `段三餘量 0.0`。
**後果之界**：未滿 `0.00005 ㎡` 之量之去處；紀錄與調配之輸入不一。零土地後果（本案⛔ 觸）。
**根因**：同一「剩下」之判以三式分寫於三條，未核其同義（門檻 `1e-6` 與寫出之四位小數之間之縫）。
**後果之框**：🟢 零土地後果。攔點 ＝ CC（常規二）與 reviewer。
**攔法**：本補令 `R-15`、`F16` 之 `K20`／`K20′`。通則：一量之判、寫、讀須出自同一式。
**字樣之錨**（`W-G.9-358`）：量測器 `F17` 之 `W7`（`R-15`·突變 `M18`〜`M20`）與 `W11`（`R-8`·突變 `M27`）。
````

## 附錄丙　塊 `P12`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`（剩餘土地之去處）入主線；段三後處理之接線與突變之檢查；規格單流程之試行期滿（`W-G.9-358`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線快轉至 `4716f202bfd9368d960b942025b2bb8da34c6dd6`（原主線 `17624a19c48715bcb1bcfd6af1a851d756d6d473`·所納 `8` 筆 `commit`，其中動生產碼者 `1` 筆：`898c31f`〔`W-G.9-357` 工項二·含補令一〕）；本批之零生產碼 `commit` 皆在主線；側支 `verify/W-G.9-357-k948` 留於 `4716f20`（歷史·⛔ 再推）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-48` 七項 `3`〜`6` ＋ `K-9-51`（段三後處理·harness ＋ 畫面） | 同「待落地清單之更新：段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`（剩餘土地之去處）入側支（`W-G.9-357`）」節序 `1`〜`4`；補令一之諸款（題一 `4` 之候選經其處置即終局·剩下之判準 `round(r, 4) ＞ 0`·距離之四捨五入·候選為空⛔ 查 `G`）同批 | ✅（入主線） | `docs/orders/W-G.9-357_規格單.md`、`docs/orders/W-G.9-357_補令一.md` |
| `2` | 段三後處理之接線與突變之檢查（規格單流程·復驗時補寫） | 量測器 `F17`（`verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`）：`W1`〜`W12`（`R-2`／`R-5`／`R-6`／`R-6′`／`R-7`·`R-7′`／`X-3′`／`R-15`／`R-10`／`R-11`／`R-12`／`R-8`／`R-3`·`R-4`）＋ 二十九突變 | ✅（入主線） | `docs/orders/W-G.9-358_輕量單.md` |
| `3` | `自誤 549`／`550`（`W-G.9-357` 補令一 `§六` 甲／乙之鑄號） | 見自誤簿 | ✅ | 同上 |
| `4` | 第 `5` 項之受併宗其後於末端塊之合併再試被整筆併出 ⇒ 調配之輸入「受併宗未配地」停機 | 既有之明示停機（`W-G.9-351`）·⛔ 靜默；補令一裁四五事 `1` | ⬜（候他案觸發時呈） | `docs/orders/W-G.9-357_補令一.md` `§一` |
| `5` | 最大面積之二分法於非單調之檢核下未必得絕對之最大 | 所施者恆已通過檢核；已記於 `K-6` 典 `K-9-51` 讀法 `3`（塊 `K4′`）並向 KL 知會 | —（記） | 同上 |

🔒 **前節之更新**（⛔ 追改前節一字）：`W-G.9-357` 節序 `1`〜`4` ⇒ ✅（本表序 `1`）；序 `5` ⇒ ✅（本表序 `2`）；序 `6` ⇒ ✅（本批）；序 `7`（畫面「自動計算公設分配」展開區）與序 `8`（`K-9-51` 射程 `③`）之態⛔ 變。
🔒 **規格單流程之試行·期滿**（`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通（`W-G.9-355`）」節 ②：試行期 ＝ 自 `W-G.9-355` 起兩輪）：首輪 ＝ `W-G.9-355`（往返 `1`·⛔ 補令、⛔ 退件）；次輪 ＝ `W-G.9-357`（停機 `1`〔CC 之唯讀獨立 reviewer 攔發單側之漏載·`自誤 549`〕＋ 補令 `1`；另一處門檻之不一由 CC 捕·`自誤 550`；CC 撰碼首輪 `12` 分、補令 `3` 分，驗 `22`〜`52` 分）。二輪本案配地皆⛔ 變；發單側復驗全數相符。期滿之報告與 KL 之答 ＝ `docs/orders/W-G.9-358_輕量單.md` `§二`：KL 答「是」（`2026-09-29 20:20`·逐字「兩題問題：均"是"」）⇒ 規格單流程自 `W-G.9-359` 起為常態（`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通之期滿與續行（`W-G.9-358`）」節·附則甲〜丙）。
🔒 **本案之量**：主線 `17624a1` → `4716f20` 之配地（退縮 `3.5 m`／`0 m`）⛔ 變——`verify/probes/probe_WG9349_k9296.py run` 二退縮之出艙逐位同；`verify/probes/probe_WG9344_k6s3.py cmp` 二退縮相異 `0` 項；`verify/probes/probe_WG9345_screen.py parity` 二退縮不符格 `0`；`run_all` 同一倉外路徑之出艙逐位同（`docs/orders/W-G.9-358_輕量單.md` `§一` 項 `5`）；段三後處理二退縮皆⛔ 觸本批之新路徑。
🔒 **本機介面**：主 checkout 同步後，執行介面之環境 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6` 皆須**未設**；成果區⛔ 增區塊（本案之段三後處理整批通過·紀錄同前）。
🔒 **依賴序**：規格步 `3`（候選街廓名單·五級八鍵·其前置之域問：公園、廣場等非道路之公共設施街廓沿正面線過半者是否得為正面道路；harness 之區外道路名稱之來源）→ `4` → `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ `W-G.9-357` 節序 `7`）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `5`（子字串框·含圖例與本列）·列 ＝ `3`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄丁　塊 `H2`（附於 `docs/reports/W-G.9波_恆常附款登記表.md` 之末）

````markdown

---

## 🔧 恆常附款 `n③` 之試行期變通之期滿與續行（`W-G.9-358`·⛔ 上文一字不刪·純末端追加）

🛑 **本節⛔ 鑄任何號**——其⛔ 新立款、⛔ 修訂 `n③` 之字面；係前節（`W-G.9-355`）之變通之**期滿之報告與 KL 之答**之登記。
🔒 **態** ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`（`W-G.9-358` 開工態·側支 `verify/W-G.9-357-k948` 之端·即快轉後之主線）。

### ① 期滿之報告（發單側窗五十五·`2026-09-29`）

| 輪 | 單 | 往返 | 攔點 | 本案配地 |
|---|---|---|---|---|
| 首輪 | `W-G.9-355` | `1`（⛔ 補令、⛔ 退件） | — | ⛔ 變 |
| 次輪 | `W-G.9-357` | 停機 `1` ＋ 補令 `1` | CC 之唯讀獨立 reviewer 攔發單側之漏載（`自誤 549`）；CC 捕門檻之不一（`自誤 550`） | ⛔ 變 |

耗時（`docs/reports/W-G.9-357R_段三後處理之七項3至6與K-9-51_執行報告.md` ⑨）：CC 撰碼首輪 `12` 分、補令一 `3` 分；驗 `22`〜`52` 分。以程式字樣為錨之接線與突變檢查 ＝ 復驗時補寫（首輪 `F15`·`W-G.9-356`；次輪 `F17`·`W-G.9-358`）。

### ② KL 之答（逐字）

發單側窗五十五所呈之問二（【現況】至【要你判斷】逐字）：

> 【現況】「chat 出規格、CC 寫生產碼」自 355 起試行兩輪，試行期已滿。
> - 首輪 355：一次就完成，沒有補令。
> - 次輪 357：CC 派出之獨立審查（只讀不改）攔下我這邊規格之一處漏載：兩端競合時轉去調配的那筆土地，後續又被處理一次。本案不會發生此情形。為此停機一次，出了補令一。另一處剩下面積之判斷門檻前後不一致，也是 CC 捕到的。
> - CC 寫程式本身很快（首輪 12 分鐘、補令 3 分鐘），時間主要花在驗證（22〜52 分鐘）。
> - 兩輪之本案配地都沒有變。
>
> 【要改成】規格單流程改為常態做法，並納入本輪兩則教訓：
> - 凡規格要求某筆土地「維持原狀」，要逐一查其後各步是否又會取到它；
> - 同一個量的判斷、寫出、讀取，要用同一個算式；
> - CC 之唯讀獨立審查列為常設步驟。
>
> 【對土地的影響】只是流程改變，本身不動任何配地。
> 【要你判斷】是否續行規格單流程？（是／否；答否就回到由發單側擬生產碼之舊流程）

KL（`2026-09-29 20:20`·問一〔`W-G.9-357` 入主線〕與問二同答）：「兩題問題：均"是"」

### ③ 續行之內容

1. 前節 ② 之變通自 `W-G.9-359` 起**⛔ 設期**（規格單流程為常態）；前節 ② 之表與其下三款（⛔ 變者、試行期之停機款、以程式字樣為錨之接線與突變檢查移至復驗）照舊，其「試行期之停機款」自此為規格單之停機款。
2. 附則（皆既有自誤之攔法之施行·⛔ 新立款）：
   - 甲　凡規格令某片「維持原狀」者，擬單時須逐一查其後各步之取片之式是否再取之，並於量測器造其形（`自誤 549` 之攔法）；
   - 乙　一量之判、寫、讀須出自同一式（`自誤 550` 之攔法）；
   - 丙　CC 之唯讀獨立 reviewer 列為規格單之工項二之常設步（驗後、推前）；其發現涉域上判斷或規格之漏載 ⇒ 停機上呈（⛔ 自裁）。

### ④ 款數之算式（`恆常附款 f`·⛔ 直接寫一個數）

期初 ＝ **`28`** 款（列舉 ＝ `a b c d e f g h i j k l m n o p q r s t u v w x y z aa ab`）＋ 本節新立 `0`／修訂 `0` ⇒ 期末 ＝ **`28`**。
````

## 附錄戊　工項一之二態之出艙（`F17 wiring`·發單側窗五十五實跑）

**塊 `T1`**（必過之態·`4716f20` 之二檔·`rc 0`）：

````text
── 接線（AST·工作樹之 app.py ＋ verify/selection_pipeline.py）──
  ✅ W0 受詞在（缺 []；巢狀（名, 全檔, 段三內）之不符 []）
  ✅ W1 R-2 未處置不變（在 `if not _qs:` True；log_print True；continue True；舊字樣 0（期 0））
  ✅ W2 R-5 所施者恆已通過（_try 之 return True；試算於拷貝 True；state＝ 2／受護 True；_t＝_try(s) True；_try 呼 2（期 2）；_tm＝_try(n/100) True；_best 唯取已通過者 True；return _lo/100 True）
  ✅ W3 R-6 候選與序（alloc_state 一呼 True；err ⇒ raise True；篩 1（期 1）；歸戶 1（期 1）；取 G 唯於 `if _pre:` True；未回 G 之 raise 2／皆於其內 True；序之鍵 True；sort 無 key True）
  ✅ W4 R-6′ 距離之取捨（ROUND_HALF_UP 之式 True；round 之呼 0（期 0）；街廓之全部切片 True）
  ✅ W5 R-7／R-7′ 題一 4（舊 raise 之字樣 0（期 0）；_r4＝None 於合併不過 True；_t14_357 一呼於其 else True；_t14_done 唯 set() True；唯 .add(c) 於頂層先於 if True（方法呼 1）；c 不過 ⇒ 第 5 項 True；半之最大面積 1（期 1）；半之剩下 ⇒ 第 5 項 True）
  ✅ W6 X-3′ 步驟 10 之 R（R 之賦值 ['R = R - _stay', 'R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done']）
  ✅ W7 R-15 剩下之判準（_has357 之式 True；_EPS357 0（期 0）；浮點小量之比較 {}；缺判 {}；分之剩下始入已試之街廓 True）
  ✅ W8 R-10 二處同形（保留之支逐 AST 同 True；含 kept 與 G True；_G 之初值 {}／{}；回傳之鍵 app True／harness True）
  ✅ W9 R-11 公設地調配之 temp（缺句 []；無段三併出 ⇒ 原物件 True；無剩下 ⇒ 去 True）
  ✅ W10 R-12 調配之輸入（X-4（字樣, 全檔, adj_intake）皆 1；_s3_ids 之加 2（期 2）；① 之落點 True；ρ True；不成單位者之分 True；另成單位（公設軌） True；總計之面積 True）
  ✅ W11 R-8 片之鍵（序於 段三併出 之後 True；三支 True）
  ✅ W12 R-3／R-4 步驟 10 之逐片（三 if 之序 True；可拆分 ⇒ _split357 True；整筆不過 ⇒ 第 5 項 True）
── 判別力（每一突變須使其所指之項轉紅）──
  ✅ M1 無受併宗之片改記未成：轉紅 ['W1']（須含 W1）
  ✅ M2 無受併宗之片⛔ continue：轉紅 ['W1']（須含 W1）
  ✅ M3 二分法取未通過之格：轉紅 ['W2']（須含 W2）
  ✅ M4 所施者⛔ 受護：轉紅 ['W2']（須含 W2）
  ✅ M5 格值改 n × 0.01：轉紅 ['W2']（須含 W2）
  ✅ M6 序之鍵以 G 先：轉紅 ['W3']（須含 W3）
  ✅ M7 候選⛔ 扣已試之街廓：轉紅 ['W3']（須含 W3）
  ✅ M8 候選為空亦取 G：轉紅 ['W3']（須含 W3）
  ✅ M9 候選⛔ 扣已併出者：轉紅 ['W3']（須含 W3）
  ✅ M10 距離以 round：轉紅 ['W4']（須含 W4）
  ✅ M11 距離以 Decimal(float)：轉紅 ['W4']（須含 W4）
  ✅ M12 距離以 ROUND_HALF_EVEN：轉紅 ['W4']（須含 W4）
  ✅ M13 R-7 之候選⛔ 入已處置之集：轉紅 ['W5']（須含 W5）
  ✅ M14 R-7 之候選於第 5 項後出集：轉紅 ['W5']（須含 W5）
  ✅ M15 題一 4 之合併不過復停機：轉紅 ['W5']（須含 W5）
  ✅ M16 候選之整筆不過⛔ 第 5 項：轉紅 ['W5']（須含 W5）
  ✅ M17 步驟 10 之 R ⛔ 扣已處置之候選：轉紅 ['W6']（須含 W6）
  ✅ M18 有剩下以 1e-6 判：轉紅 ['W7']（須含 W7）
  ✅ M19 分之剩下以 g < s 判：轉紅 ['W7']（須含 W7）
  ✅ M20 鍵之環以 1e-6 判：轉紅 ['W7', 'W11']（須含 W7）
  ✅ M21 畫面之 G 取他欄：轉紅 ['W8']（須含 W8）
  ✅ M22 harness 之 alloc_state ⛔ 回 G：轉紅 ['W8']（須含 W8）
  ✅ M23 公設地調配之 temp 改原物件：轉紅 ['W9']（須含 W9）
  ✅ M24 面積_m2 ⛔ 乘 ρ：轉紅 ['W9']（須含 W9）
  ✅ M25 一分未併者⛔ 入合併單位：轉紅 ['W10']（須含 W10）
  ✅ M26 已併出之量⛔ 計入原位次配地：轉紅 ['W10']（須含 W10）
  ✅ M27 剩下全收者⛔ 去 段三餘量：轉紅 ['W11']（須含 W11）
  ✅ M28 可拆分者⛔ 經 _split357：轉紅 ['W12']（須含 W12）
  ✅ M29 整筆不過⛔ 第 5 項：轉紅 ['W12']（須含 W12）
⇒ 紅 []；rc 0
````

**塊 `T2`**（必破之態·`17624a1` 之二檔·`rc 1`）：

````text
── 接線（AST·工作樹之 app.py ＋ verify/selection_pipeline.py）──
  🔴 W0 受詞在（缺 []；巢狀（名, 全檔, 段三內）之不符 [('_has357', 0, 0), ('_res357', 0, 0), ('_max357', 0, 0), ('_dist357', 0, 0), ('_k951', 0, 0), ('_split357', 0, 0), ('_t14_357', 0, 0)]）
  🔴 W1 R-2 未處置不變（結果='未處置' 2（期 1）；`if not _qs:` 1（期 1））
  🔴 W2 R-5 所施者恆已通過（器拋 KeyError: '_max357'）
  🔴 W3 R-6 候選與序（器拋 KeyError: '_k951'）
  🔴 W4 R-6′ 距離之取捨（器拋 KeyError: '_dist357'）
  🔴 W5 R-7／R-7′ 題一 4（器拋 KeyError: '_t14_357'）
  🔴 W6 X-3′ 步驟 10 之 R（R 之賦值 ['R = R - _stay', 'R = _mem - merged_out - set(_recv_by_blk.values()) - L']）
  🔴 W7 R-15 剩下之判準（器拋 KeyError: '_has357'）
  🔴 W8 R-10 二處同形（保留之支逐 AST 同 True；含 kept 與 G False；_G 之初值 None／None；回傳之鍵 app False／harness False）
  🔴 W9 R-11 公設地調配之 temp（缺句 ['_out = []', '_out.append(tp)', "_rem = float(tp.get('段三餘量', 0) or 0)", "_a = float(tp.get('分攤登記面積_m2', 0) or 0) + float(tp.get('面積_m2', 0) or 0)", '_rho = _rem / _a', '_tp = dict(tp)', "_tp['分攤登記面積_m2'] = float(tp.get('分攤登記面積_m2', 0) or 0) * _rho", "_tp['面積_m2'] = float(tp.get('面積_m2', 0) or 0) * _rho", '_out.append(_tp)', 'return _out']；無段三併出 ⇒ 原物件 False；無剩下 ⇒ 去 False）
  🔴 W10 R-12 調配之輸入（X-4（字樣, 全檔, adj_intake）皆 1；_s3_ids 之加 0（期 2）；① 之落點 False；ρ False；不成單位者之分 False；另成單位（公設軌） False；總計之面積 False）
  🔴 W11 R-8 片之鍵（鍵之環 0（期 1））
  🔴 W12 R-3／R-4 步驟 10 之逐片（三 if 之序 False；可拆分 ⇒ _split357 False；整筆不過 ⇒ 第 5 項 False）
── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──
⇒ 紅 ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12']；rc 1
````

SELF_SHA256: 564daf683158a9b028b9dc836714063688dde5b1ca30e7da83ff5194565695ac
