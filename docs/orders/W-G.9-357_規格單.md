# `W-G.9-357`　規格單：段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`（剩餘土地之去處）（新側支 `verify/W-G.9-357-k948`）＋ `K-9-51` 之入典 ＋ 待落地清單之更新

> **本單建議等級 ＝ `xhigh`**（本單令 CC 依規格撰寫生產碼·規格單流程之次輪）。
> **發單** ＝ 發單側窗五十三·`2026-09-29`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-357-k948`**，其起點 ＝ 主線之端 `17624a1`）。
> **流程 ＝ 規格單**（試行之次輪·KL `2026-09-28 11:43` 令·`§二`）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `F16`／`F14p`·CC ⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py`／`verify/selection_pipeline.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **重**（生產碼 `2` 檔：`app.py`、`verify/selection_pipeline.py`；土地後果：**本案⛔**——本案之段三後處理皆整批通過〔`§一` 項 `6`〕，其路徑一字不動；**他案有**——段三後處理之整批不過者，由「整筆不併／未處置」改依 `K-9-48` 七項 `3`〜`6` 與 `K-9-51` 處之；`K-9-50` 題一 `4` 之合併不過者，由停機改同之）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `17624a19c48715bcb1bcfd6af1a851d756d6d473`（`W-G.9-356` 工項三）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-357-k948`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F16`／`F14p`／`K4`／`P11` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-357_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 與 `verify/selection_pipeline.py` 以外之生產碼一字（生產碼 `34` 檔之其餘 `32` 檔）；`§三-3` 之禁改；`def main` 之一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4 之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿、`GB` 簿、自誤簿、恆常附款登記表之一字；`K-6` 典與 `CLAUDE.md` 除塊 `K4`／`P11` 之純末端追加外之一字；既有量測器除塊 `F14p` 外之一字；任何既有側支之推送、刪除或改寫；KL 主 checkout。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `17624a19c48715bcb1bcfd6af1a851d756d6d473`；`git ls-remote --heads origin` 之列數 ＝ `31`，且⛔ 含 `refs/heads/verify/W-G.9-357-k948`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 548 547` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`915`** 檔·器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十三實跑（皆 `rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-357`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py 17624a1 W-G.9-357 W-G.9-356 W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-356` | `2`／`4`／`4` | `2`／`4`／`6` | `8`（寬式 `10`） | `2` | `2`／`22` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `3`／`4` | 🟢 宣告框 `0`、鬆框非零（漏框偵察有咬） |
| `K-9-51`（本批所鑄之裁號）｜`python verify/probes/wg9268_gate6_occupancy.py 17624a1 K-9-51 K-9-50 K-9-93` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`1` | 🟢 可取（鬆框 `1` 列 ＝ `docs/orders/W-G.9-338_重量單.md:35` 之「對照乙［必為零］」所列之未取號·⛔ 占用） |
| 對照甲［必非零］`K-9-50` | `0`／`16`／`0` | `0`／`16`／`0` | `16` | `7` | `9`／`92` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`K-9-93` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 宣告框 `0`（前批所用之 `K-9-94` 已為 `W-G.9-354 §零-1` 之表所引、嚴格 `D2` ＝ `2` ⇒ 改取未用之號） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `18`／`20` | 🟡 寬式 `D3` ＝ `2`：命中 `docs/reports/W-G.9-356R_入主線與畫面路徑之接線檢查_執行報告.md:113`／`:114`（該報告內嵌本器之出艙）；受詢之判⛔ 受影響（器之 `rc` 唯繫受詢）——**具名豁免**，記於塊 `P11` 之併記 |

本批⛔ 鑄自誤／`GB`／`VR`；`K-9` `MAX` ＝ `50` ⇒ 取 `K-9-51`（塊 `K4`）。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `17624a1`，或遠端 heads ≠ `31`，或遠端已有 `verify/W-G.9-357-k948`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `F16`／`F14p`／`K4`／`P11` 任一之 bytes／`sha256` 與 `§五-1` 不符；或工項一之 `git apply --check`（塊 `F14p`）不過，或施後 `verify/probes/probe_WG9355_screenmerge.py` 之 blob ≠ `§五-1` 項 `6` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-7` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變**（`V-2`〜`V-5` 任一相異） |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-357-k948`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之二檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `8`。

---

## `§一`　態錨（發單側窗五十三自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `17624a19c48715bcb1bcfd6af1a851d756d6d473`；側支 `verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`31`**（`verify/` `26`·`wip/` `3`·`claude/` `1`·`main` `1`）；`verify/W-G.9-357-k948` ⛔ 存 |
| `2` | 生產碼（開工態 blob） | `app.py` `e11232a6569bf33c7b2b7f15da989873a06ff28c`；`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；`CLAUDE.md` `299948` B；`K-6` 典 `427954` B |
| `3` | `W-G.9-356` 之復驗（發單側窗五十三·依交接文五十二 `§四-1`·全數自倉重跑） | 四 `commit`（`475414d`／`1cf82a9`／`4aa6b50`／`17624a1`）逐筆對拍：單 ＝ `3785118b…`（`68511` B·`SELF_SHA256` 經 `P-5` 自驗相符·pre-flight 🔴 `0`／🟡 `5` 同單 `§五-1` 項 `4`）；`F15` blob ＝ `c489e887…` ＝ 塊；`CLAUDE.md` `295353 → 299948` 嚴格前綴、所增 ＝ `P10` 逐位；報告 ①〜⑧ 俱載（⑥ 載 KL 貼單之訊息逐字 ＝ 檔路徑一列 ＋「是」）；收工閘 `1`〜`9` 自倉重跑皆符（`F15` 必過 ＝ `T1`、必破〔`f55935c`〕＝ `T2`；閘 `7` 四簿 ＝ 開工態）；工項四之出艙（CC 於對話）與自倉所算相符（新入之路徑 `12`、被覆寫之追蹤檔 `9`）——**全數相符** |
| `4` | 本批之受詞 | `CLAUDE.md` 諸「待落地清單之更新」節之 `K-9-48` 七項 `3`／`5`／`6`（`W-G.9-344` 起 ⬜）；`K-9-51`（KL `2026-09-29 12:20`）；`K-9-50` 讀法 `6` 之停機（題一 `4`） |
| `5` | 現碼之行為（開工態） | ① 段三後處理整批不過 ⇒ 不可拆分者「未成」（⛔ 第 `5` 項）；可拆分者整片「未處置」＋ `🔴`（⛔ 最大面積、⛔ 第 `5` 項·該片維持段三前之狀態）；② 題一 `4` 之合併不過 ⇒ `RuntimeError`「…`K-9-48` 七項 3〜5 未落地（停機款 9）」；③ 二 `alloc_state` 皆⛔ 回 `G`；④ `k6b_stage3_pool_temp` 去一切帶 `段三併出` 之片；⑤ `adj_intake`：帶 `段三併出` 者 ＝ 原位次配地；未併之共同負擔用地，其歸戶有原位次配地而無建築街廓內不能分配者 ⇒ 待同歸戶併入（`step4`）——皆由塊 `F16` 之 `selftest` 之 `K2`〜`K18` 證之（`§一` 項 `7`） |
| `6` | 本案（harness·開工態） | 段三之紀錄：退縮 `3.5` ⇒ `18` 列（序 `1`〜`13` ＋ 後處理 `5` 列：`628-30(2)` 後處理(a) 成·`628-45(5)`／`628-30(4)` 後處理(b) 成·`628-45(3)`／`628-45(4)` 後處理(c) 成·皆整批通過）；退縮 `0.0` ⇒ `0` 列（本案⛔ 觸發七項 `3`〜`6`）——`F16 run` 之 `R2` 所載即此 `18` 列（數值容差 `0.01`）。`alloc_state` 之保留：`3.5` ⇒ `28` 宗、`0.0` ⇒ `29` 宗（harness ＝ 畫面） |
| `7` | 量測器於工項一之端（`17624a1` ＋ 塊 `F16` ＋ 塊 `F14p`·發單側於拋棄式 clone 實跑） | `F16 selftest` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K10′', 'K11', 'K12', 'K13', 'K14', 'K14′', 'K17', 'K18']；rc 1`（對照 `K1`／`K15`／`K16` 皆 ✅；`P0` `20／20`）；`F16 run` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`（`R2` 二退縮皆 ✅·`R1` 之紅唯因 `G` 缺）；`F14 selftest` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['T3d', 'T9d', 'T6d']；rc 1`（`P0` `86／86`） |
| `8` | 發單側之原型（**⛔ 交付**·僅為量測器之必過之實例） | 發單側於倉外拋棄式工作樹依 `§三` 撰一原型（`app.py` 與 `verify/selection_pipeline.py`·⛔ 入倉·其 blob ⛔ 為本單之期），於其上：`F16 selftest` ⇒ `rc 0`（`K1`〜`K18` 皆 ✅·`P0` `20／20`）、`F16 run` ⇒ `rc 0`（`R1` 二退縮：保留 `28`／`29` 宗、`G` 之逐宗差 `0.0`；`R2` 二退縮皆 ✅）；`§四-3` 閘 `9`〜`22` 之諸器 皆 `rc 0`（`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F10 selftest` 之突變 `M1`〜`M4` 皆轉紅；`F14 selftest`〔施 `F14p` 後〕`P0` `86／86`；`parity` `3.5` ⇒ 配地列 `35`／`34`、`0.0` ⇒ `36`／`35`·不符格 `0`；`F8`〜`F15` 之 `run` 皆 `rc 0`）；`F8 run` 二退縮之出艙對開工態 `diff` 皆空。**CC 之碼⛔ 須同原型**；唯須滿足 `§三` 與 `§四` |
| `9` | `F8 run`／`run_all`（開工態之生產碼 ＝ `1ef3bb5`） | `W-G.9-356 §一` 項 `5`：`F8 run` 二退縮之出艙逐位同；`run_all` 於倉外路徑 ⇒ `64` 項·PASS `28`／FAIL `36`·末端夾具／golden 列 `21`·對帳段 `22／36`·`236056` B（其 bytes 平台與路徑相依·⛔ 入判） |

---

## `§二`　KL 之語與射程

🔒 **所據之裁**：
- `K-9-48` 其五（KL `2026-09-23`·逐字「1~7項全部同意」）之七項 `3`〜`7`（`K-6` 典逐字）：
  `3` 可拆分的土地（道路、公設）全部併入不符檢核 ⇒ 在「不影響」範圍內，併入所能容許的最大面積；其餘依第 `5` 項處理｜`4` 不可拆分的土地（他街廓建地）整筆併入不符檢核 ⇒ 不併入；依第 `5` 項處理｜`5` 第 `3`、`4` 項剩下的土地 ⇒ 先併入同一地主另一個已配得土地的街廓（同樣須通過檢核）；仍不行，則依 `K-9-45` 與該地主其他不能分配的土地合併，試配到其他街廓的調配池｜`6` 「另一側無法原位次配地 ⇒ 全數歸入已取得街角之一側」，但全數歸入不符檢核 ⇒ 同第 `3`〜`5` 項｜`7` 有多筆要併入、只能容納其中一部分時的先後 ⇒ 先不可拆分的建地，再道路片，最後公設片；同類中面積大者先。
- **`K-9-51`**（KL `2026-09-29 12:20`·逐字「是」·本批入典·塊 `K4`）：第 `5` 項之街廓不只一個 ⇒ 距離該筆土地最近者先逐一試併（每次須通過檢核），距離相同者先試該地主配得面積較大者，都不行才進調配；【通知】二則（最大面積以 `0.01 ㎡` 為單位；公設地上之土地平分時通過之一側照收其一半，未通過之一側改收最大面積）KL 未駁。
- `K-9-50` 讀法 `6`（題一 `4`）之「不過 ⇒ 停機（`K-9-48` 七項 3〜5 未落地）」——自本批起依 `K-9-48` 七項 `3`〜`5` 與 `K-9-51` 處之（塊 `K4` 讀法 `4`）。
🔒 **流程之令**：KL `2026-09-28 11:43`（`W-G.9-355 §二` 逐字）令試行規格單流程；本單為其次輪（首輪 ＝ `W-G.9-355`·其評估見 `CLAUDE.md`「待落地清單之更新：末端塊之合併再試（harness ＋ 畫面·含 `K-9-50`）同批入主線；…（`W-G.9-356`）」節）。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 逐字放行**。
🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至新側支 `verify/W-G.9-357-k948`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及 `app.py`／`verify/selection_pipeline.py` 以外之生產碼、`§三-3` 之禁改、任何他錨；`(d)` ⛔ 及 `K-9-51` 射程 `③` 之二情形（不可拆分之建地之目標街廓非恰一 ⇒ 仍停機；道路片二半皆不鄰 ⇒ 仍「未處置」）、`main()` 之「自動計算公設分配」展開區、`GB-194`、調配之任何後步（規格步 `3`〜`8`）——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **受詞之總述**：`app.py` 之 `k6b_stage3_run`（段三·街角合併重試；亦為 `end_block_merge_run` 之單一真相源）之**步驟 10（後處理）**：某合併群之應處置之片（`R`）先**整批**試之；整批通過 ⇒ 全數成立（**本案之路徑**）；整批不過 ⇒ 逐片——現碼於此「不可拆分者不併入（結果 ＝ 未成）」「可拆分者記未處置（`🔴`）」，即止。**本批於「整批不過」之後補上 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`**；並將 `K-9-50` 題一 `4` 之「合併不過 ⇒ 停機」改依之；並使部分併出之片於其後各段有其表示。harness 與畫面二路徑皆經 `k6b_stage3_run`（harness `run_corner_pk_k6b`／`run_end_block_merge`；畫面 `f3_screen_k6b_stage3`／`f3_screen_end_block_merge`）⇒ 二路徑同受之；二宿主之碼⛔ 動。

**用語**（本節專用）：「**片**」＝ 後處理所處置之一筆重劃前切片 `x`；「**`a(x)`**」＝ `x` 於段三之輸入之 `分攤登記面積_m2 ＋ 面積_m2`；「**`k(x, r)`**」＝ 注入之 `a_prime(x, r) ÷ a(x)`（每 `1 ㎡` 來源面積於受併宗 `r` 之折算）；「**來源面積**」＝ 以 `a(x)` 計之量（`㎡`）；「**檢核**」＝ 現碼之「不影響原位次」（`_noaff`·`K-9-48` 其三：受檢街廓之原保留者〔扣本步被整筆併出者〕仍保留，且配餘地不合格之處數⛔ 增）；「**試併**」＝ 於現態之深拷貝施之、檢核通過始改現態。

### `§三-1`　行為要求（逐條·「給定何種情形、須得何種結果」）

| # | 給定 | 須得 |
|---|---|---|
| `R-1` | 某合併群之應處置之片**整批通過** | 一切（紀錄之列、`merged_out`、受併宗之 `面積_m2`、片之鍵）**逐位同現碼**。**本案（退縮 `3.5`／`0.0`）唯此路徑** |
| `R-2` | 整批不過 | 依現碼之 `_plan` 之序（不可拆分之建地〔(a)〕依面積大者先 → 道路片〔(b)〕→ 公設地上之土地與路口片〔(c)〕·各類內面積大者先·≡ `K-9-48` 七項 `7`）逐片處之（`R-3`／`R-4`）；`_plan` 內無受併宗之片（道路片之二半皆不鄰 `B` 內街廓）⇒ **現碼之「未處置」之列與其 `🔴` 印出，一字不變**（`K-9-51` 射程 `③`） |
| `R-3` | 不可拆分之片 `x`（(a)·整筆），其受併宗 `r` | 整筆試併入 `r`（受檢街廓 ＝ `r` 之街廓 ∪ `x` 之街廓；被整筆併出者 ＝ `{x}`）：通過 ⇒ 同現碼之「成」；不過 ⇒ 同現碼之「未成」之列（⛔ 併入·七項 `4`），**繼之以 `R-6`（整筆·已試之街廓 ＝ `{r 之街廓}`）** |
| `R-4` | 可拆分之片 `x`（(b)／(c)），其各受併宗之分 `[(r_i, q_i)]`（現碼之 `_plan` 所給·`q_i` 為 `r_i` 之折算量） | **逐分**（依 `_plan` 所給之序）：來源面積 `s_i ＝ q_i ÷ k(x, r_i)`；以 `R-5` 求其可併之來源面積 `g_i`（`g_i ＝ s_i` 即全收）並施之；逐分一列（`R-9`）；`g_i < s_i` 之分：其街廓入「已試之街廓」、其差 `s_i − g_i` 累入「剩下」。逐分畢，剩下 `> 1e-6 ㎡` ⇒ **`R-6`（可拆分·剩下之來源面積）**。通過之一側照收其分（`K-9-51` 【通知】二） |
| `R-5` | 最大面積（可拆分·七項 `3`）：片 `x`、受併宗 `r`、欲併之來源面積 `s` | 先試併 `s`（`r` 之 `面積_m2` 增 `k(x, r) × s`；受檢街廓 ＝ `r` 之街廓；被整筆併出者 ＝ 空）：通過 ⇒ 得 `s`。不過 ⇒ 於 `{n × 0.01 : n ＝ 0, 1, …, N}`（`N` ＝ 小於 `s` 之最大者·`0.01 ㎡` 之格·`K-9-51` ②）中以二分法求**通過之最大者** `g`（`n ＝ 0` 視為通過·⛔ 試）並施之；**所施者恆為已通過檢核之量**（⛔ 施未驗之量）。回 `g` |
| `R-6` | 第 `5` 項（`K-9-51`）：片 `x`、整筆或可拆分之剩下（來源面積 `s`）、已試之街廓 `F` | ① 以現態呼叫 `alloc_state`（其配地中止 ⇒ `RuntimeError`·停機款 `9` 之類·⛔ 靜默）；② **候選** ＝ 其 `kept` 之宗中，歸戶（`own_map` 以其 `原地號` 查）＝ `x` 之歸戶者，扣：`x` 本身、`merged_out` 者、所在街廓 ∈ `F` 者、不在現態之宗地（`temp`）者；`x` 之歸戶查無 ⇒ 候選為空；③ **序** ＝ （`x` 之重劃前幾何與候選宗所在街廓〔段三之輸入中該街廓之全部切片之幾何之聯集〕之最短距離·四捨五入至 `0.01 m`·小者先；候選宗於 `alloc_state` 所回 `G` 之值·大者先；暫編地號·字典序小者先）；`G` 缺 ⇒ `RuntimeError`，其訊息含字樣 **`未回 G`**；④ **整筆**：依序各整筆試併（受檢街廓 ＝ 候選之街廓 ∪ `x` 之街廓；被整筆併出者 ＝ `{x}`），首一通過 ⇒ 施之、`x` 入 `merged_out` 並自 build 移除，止；**可拆分**：依序各以 `R-5` 併之（欲併 ＝ 其時之剩下），剩下 `≤ 1e-6 ㎡` 即止；⑤ 候選試盡而仍有剩下（或整筆皆不過、或候選為空）⇒ 記一列「轉調配」（`R-9`），**⛔ `raise`、⛔ `🔴` 印出**；整筆者維持原狀（仍在 build）|
| `R-7` | `K-9-50` 題一 `4`：未取得之一端之候選 `c`（不可拆分）連同其分得之一半，併入已取得之一端之受併宗 `w` **不過**（現碼於此 `raise`「…`K-9-48` 七項 3〜5 未落地（停機款 9）」） | **⛔ `raise`**，改依序：① `c` 整筆試併入 `w`（受檢 ＝ `w` 之街廓 ∪ `c` 之街廓；被整筆併出者 ＝ `{c}`）——通過 ⇒ 施之、`c` 入 `merged_out`；不過 ⇒ `R-6`（整筆·`F ＝ {w 之街廓}`）；② 其後，該一半所涉之每一片 `x`（現碼之 `X`·依暫編地號之序·其分 `f ＞ 0`）：來源面積 `a(x) × f` 以 `R-5` 併入 `w`，其差 ⇒ `R-6`（可拆分·`F ＝ {w 之街廓}`·全收者免）。本路徑⛔ 記現碼之「題一 `4`·成」之列（改記 `R-9` 之列）；競合之二列（`_ct_log`）、`merged_out.update(X)`、`return [Lo]` 等其餘一切同現碼。**題一 `4` 之合併通過者，一切逐位同現碼** |
| `R-8` | 段三之出之片之鍵（`k6b_stage3_run` 之回傳 `temp_out`） | `段三併出` ＝ 本趟對該片有正之併入之受併宗之相異字典序列（同現碼）。**另**：可拆分之片經 `R-4`／`R-6`／`R-7` 而**仍有剩下**（`> 1e-6 ㎡`）者——有任一併入 ⇒ 加鍵 `段三部分併出` ＝ `{受併宗: 其所併之來源面積（㎡·四位小數）}`（含 `R-7` 中已取得之一端先前併入之一半）與 `段三餘量` ＝ 剩下之來源面積（㎡·四位小數）；全無併入 ⇒ 唯加 `段三餘量` ＝ `a(x)`（四位小數·⛔ `段三併出`）。本趟全收之片、及本趟有併入而無剩下之片 ⇒ 去其 `段三部分併出`／`段三餘量`（入段三時已帶者亦然）；本趟未觸之片之鍵⛔ 動。不可拆分之片「轉調配」者⛔ 加任何鍵 |
| `R-9` | 紀錄之列（`log`·`R-3`〜`R-7` 所新增者） | 每列皆含現碼 `_row` 之諸鍵；`序` ＝ `'後處理'`。① **逐分之列**（`R-4`）：`層級` ＝ 現碼之 `後處理(b)`／`後處理(c)`，`候選` ＝ `x`，`受併宗` ＝ `r_i`（字串），`併入量` ＝ `切分併入` ＝ `{r_i: k × g_i}`（四位小數·`g_i ＝ 0` ⇒ `{}`），`整筆併入` ＝ `[]`，`結果` ∈ {`成`（全收）／`部分成`（`0 ＜ g_i ＜ s_i`）／`未成`（`g_i ＝ 0`）}，`檢核` ∈ {`通過`／`部分通過`／`不過`}，另鍵 `全量` ＝ `q_i`（四位小數）；② **第 `5` 項之列**（`R-6` 之每一候選一列）：`層級` ＝ `'後處理·第5項'`，`街廓` ＝ `x` 之街廓，`候選` ＝ `x`，`受併宗` ＝ 該候選，`結果`／`檢核` 同 ①（整筆者唯 `成`／`未成`·`通過`／`不過`；整筆成者 `整筆併入` ＝ `[x]`、`併入量` ＝ `{候選: k × a(x)}`），另鍵 `距離`（m·二位小數）與 `G`；③ **轉調配之列**：`層級` ＝ `'後處理·第5項'`，`候選` ＝ `x`，`受併宗` ＝ `'—'`，`結果` ＝ `'轉調配'`，`檢核` ＝ `'—'`，`併入量` ＝ `{}`，另鍵 `餘量` ＝ 剩下之來源面積（整筆者 ＝ `a(x)`·四位小數）；④ **`R-7` 之列**：`層級` ＝ `'題一 4'`，`街廓` ＝ 未取得之一端之街廓，`端` ＝ 其端，`受併宗` ＝ `w`；`候選` ＝ `c` 之列同 ② 之整筆者（⛔ `距離`／`G`）；`候選` ＝ `x` 之列同 ①（`全量` ＝ `k(x, w) × a(x) × f`）。**列之序** ＝ 事件之序（逐片：其分之列 → 其第 `5` 項之列 → 其轉調配之列；`R-7`：`c` 之列 → `c` 之第 `5` 項 → 各 `x` 之列與其第 `5` 項） |
| `R-10` | `alloc_state` 之回傳（harness `verify/selection_pipeline.py` 之 `_k6b_callbacks`；畫面 `app.py` 之 `k6b_screen_callbacks`） | **增鍵** `'G'` ＝ `{暫編地號: float(r.get('G(㎡)', 0) or 0)}`（`r` ＝ 該列·式同現碼諸處之取 `G`），其鍵集 ＝ `kept` 諸值之聯集（同取 `驗_總判` ＝ `保留` 之列）；`kept`／`bad_pools`／`err` 之值**逐位同現碼**（`err` 非空者亦然·`G` 之鍵集恆 ＝ 同一回傳之 `kept` 諸值之聯集）。`k6b_stage3_run` 之 docstring 之 `alloc_state` 之約定增 `G` |
| `R-11` | `verify/selection_pipeline.py` 之 `k6b_stage3_pool_temp`（公設地調配〔F.3／F.4〕之 temp） | 帶 `段三併出` 且其 `段三餘量 ＞ 0` 之片 ⇒ 以**新 dict**（淺拷貝）入之，其 `分攤登記面積_m2`、`面積_m2` 各乘 `ρ ＝ 段三餘量 ÷ (分攤登記面積_m2 ＋ 面積_m2)`；帶 `段三併出` 而無 `段三餘量` ⇒ 去之（同現碼）；其餘 ⇒ 原物件（同現碼）；回傳新 list（同現碼）。簽名⛔ 變 |
| `R-12` | `app.py` 之 `adj_intake`（調配之輸入） | ① 帶 `段三併出` 且帶 `段三餘量` 之片 ⇒ 其列之 `類` ＝ `ADJ_DISP_COMMON_UNIT`，`原有面積` ＝ `分攤登記面積_m2 × ρ`（`ρ` 同 `R-11`），另鍵 `段三併出面積` ＝ `分攤登記面積_m2 × (1 − ρ)`（其受併宗未配地之停機同現碼）；② 帶 `段三餘量` 而無 `段三併出` 之片（共同負擔之街廓上）⇒ `類` ＝ `ADJ_DISP_COMMON_UNIT`；③ ①② 之列**恆入其歸戶之合併單位**（縱其歸戶有原位次配地、無建築街廓內不能分配者·`K-9-45`）：該歸戶依現碼成單位者 ⇒ 併入其 `共同負擔用地`（`原有面積合計` 含之）；依現碼不成單位者 ⇒ 另成一單位（`軌` ＝ `ADJ_TRACK_PUBLIC`、`原街廓` ＝ `None`、`原街廓之據` ＝ `{}`、`建築街廓內不能分配` ＝ `[]`、`共同負擔用地` ＝ ①② 之列、`原有面積合計` ＝ 其和、`同歸戶原位次配地之街廓` 同現碼之值），其餘之共同負擔用地之去處（`step4`）同現碼；④ `totals`：列數依其 `類`；① 之 `段三併出面積` 加入 `ADJ_DISP_ALLOC` 之面積（⛔ 加列數）⇒ 諸類面積之和恆 ＝ `all_area`。無 ①② 之片者，回傳**逐位同現碼** |
| `R-13` | 本案（harness·退縮 `3.5`／`0.0`） | 段三之紀錄與其出之宗地、其後之配地、末端塊之合併再試、調配之輸入、`run_all` ——**逐位同開工態**（`V-2`〜`V-5`） |
| `R-14` | 畫面路徑 | 經 `k6b_stage3_run`／`k6b_screen_callbacks` 同受 `R-1`〜`R-10`；`def main` 之一字⛔ 動（`X-1`）；`F4 parity` 二退縮 `rc 0`（`V-4`） |

### `§三-2`　介面（名與簽名·量測器 `F16` 以之為受詞）

| # | 名 | 簽名／回傳 | 呼叫端 |
|---|---|---|---|
| `I-1` | 改 `k6b_stage3_run` | 簽名⛔ 變；回傳之形⛔ 變（`temp_out` 之片增 `R-8` 之二鍵；`log` 增 `R-9` 之列） | `run_corner_pk_k6b`（harness）、`f3_screen_k6b_stage3`（畫面）、`end_block_merge_run`（⛔ 變） |
| `I-2` | 改 `alloc_state`（二處） | `(temp, build)` → `{'kept', 'bad_pools', 'err', 'G'}` | `k6b_stage3_run`（`R-6`）；餘之呼叫端⛔ 取 `G` |
| `I-3` | 改 `k6b_stage3_pool_temp` | `(temp_parcels)` → `list`（`R-11`） | `run_verification.py`、`app.py` 之 `_build_wf_ctx`（皆⛔ 變） |
| `I-4` | 改 `adj_intake` | 簽名⛔ 變；回傳之鍵⛔ 變（列增 `段三併出面積`；單位之形同現碼） | 二宿主（⛔ 變） |

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

| # | 禁 | 所護之閘 |
|---|---|---|
| `X-1` | `def main` 之一字（含「自動計算公設分配」展開區之 `段三併出` 之濾·`K-9-51` 射程外·塊 `P11` 序 `7`） | `main_synth`、`F15 wiring`、`F4 wiring` |
| `X-2` | `k6b_stage3_run` 之步驟 `1`〜`9`（含 `_sets`／`_ct_*`／`_contest`／`_k950_rows`／`_road_halves`／`_nbr_blocks`／`_is_crossing`）一字不動，**唯** `R-7` 所指之 `else` 分支（現碼之 `raise … 七項 3〜5 未落地` 一處）與其後之「題一 `4`·成」之列之記法得改；輔助之函式得增（其定義須先於步驟 `1`〜`8` 之環·因 `_ct_cross` 呼叫之） | `F12`／`F13` 之 `selftest`／`wiring`／`run` |
| `X-3` | 步驟 `10` 之 `_plan` 之組成（`_cls`、`_recv_of`、`_stay`、`B`、各停機）、整批之試（`_doable`／`_chk_blks`／`_removed`／`_batch_ok`）一字不動 | `F13 wiring` `W5`、`R-1` |
| `X-4` | `adj_intake` 內下列四字樣**各恰一處、逐字**：`float(_r['應分配面積'])`、`if _pool or (_cm and not _al):`、`if '段三併出' in t:`、`if len(_cands) != 1:`（`F10 selftest` 之突變錨 `M1`〜`M4`） | `F10 selftest` |
| `X-5` | `_WF_NS_NAMES` 一字不動 | `wfns_ast` `48`／`48`／`47` |
| `X-6` | `end_block_*`、`k6_merge_groups`、`solve_G_binary`、`_solve_G_one`、`k929_6_*`、`f3_screen_*`（`k6b_screen_callbacks` 之 `alloc_state` 之 `R-10` 除外）、`k6b_stage3_selected`、`adj_intake_rows` 一字不動；工項二於 `verify/` 唯動 `selection_pipeline.py`（`_k6b_callbacks` 之 `alloc_state`〔`R-10`〕與 `k6b_stage3_pool_temp`〔`R-11`〕二處），餘一字不動 | `F9`〜`F15`、`main_synth`、`parity` |
| `X-7` | 新碼⛔ 含案件字面（街廓名、側別、地號、分區名之字串常數·`F12`〜`F15 wiring` 之 `CASE_LIT_RE` 之形） | 泛化之鐵則 |

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`D-1`：本規格之任一條，其二讀法之後果**在土地上相異**（任一宗之面積、併入之量、受併宗之擇、轉調配之量）。
`D-2`：`R-6` 之候選、距離、`G` 於某情形無從依本規格定之（例：候選宗所在之街廓於段三之輸入中無切片）。
`D-3`：須動 `§三-3` 之任一字始能滿足 `§三-1`。
🔒 非域上之實作細節（函式之切分、區域名、註解、`RuntimeError` 之措辭〔`R-6` 所令之 `未回 G` 除外〕、二分法之寫法〔須滿足 `R-5` 之「所施者恆已通過」〕）由 CC 定之，並於報告 ⑦ 逐項具名其選擇與其由。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐 `R-1`〜`R-14`：落於何函式、何處；`§三-4` 末之實作細節之選擇及其由；對 `§三-3` 各款之自查（逐款具名「未觸」及其據）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/selection_pipeline.py` 之**全文**（報告內嵌或報告同目錄之 `.diff` 檔·⛔ 摘要）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-357_規格單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-357 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-357-k948`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`32`**、主線仍 ＝ `17624a1…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-357-k948`（快轉）。

**工項一　量測器入倉**（**先於生產碼**·新側支·零生產碼）：塊 `F16` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9357_k948.py`（**新檔**）；塊 `F14p` 抽為 `<O>\F14p.diff`、對拍後 `git apply --check <O>\F14p.diff` ⇒ 過；`git apply <O>\F14p.diff`；`git hash-object verify/probes/probe_WG9355_screenmerge.py` ＝ `§五-1` 項 `6`（停機款 `3`·`F14` 之 `T3d`／`T9d`／`T6d` 逐字比對 `alloc_state` 之回傳 ⇒ 其期增 `R-10` 之 `G`）。`commit` 訊息逐字 `W-G.9-357 工項一：量測器 F16（段三後處理之七項 3〜6 與 K-9-51）入倉 ＋ F14 之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-357-k948`。

**工項二　生產碼**（🔴 `app.py` ＋ `verify/selection_pipeline.py`·CC 依 `§三` 撰寫·一 `commit`·推新側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9357_k948.py selftest <repo>` ⇒ **`rc 1`**（末列逐字 ＝ `§一` 項 `7` 之 `selftest` 末列）。
2. `python verify/probes/probe_WG9357_k948.py run <repo>` ⇒ **`rc 1`**（末列逐字 ＝ `§一` 項 `7` 之 `run` 末列）；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` ⇒ **`rc 1`**（末列逐字 `⇒ 紅 ['T3d', 'T9d', 'T6d']；rc 1`）。
3. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`（皆 `rc 0`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫二檔之改動；`python -m py_compile app.py verify/selection_pipeline.py`；`commit` 訊息逐字 `W-G.9-357 工項二：段三後處理之 K-9-48 七項 3〜6 與 K-9-51（剩餘土地之去處）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9357_k948.py selftest <repo> > <O>\f16_self_post.log`；`… run <repo> > <O>\f16_run_post.log` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `K1`〜`K18`（`20` 項）皆 ✅、`P0` 逐項擾動恰該項紅 `20／20`；`run` 之 `R1`／`R2` 二退縮皆 ✅，其數 ＝ `§一` 項 `6` |
| `V-2` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`python verify/probes/probe_WG9344_k6s3.py cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；二 `cmp` 皆 **`rc 0`**（逐宗、抵費地、街角得標、強制旗標皆同） |
| `V-3` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `diff` | 皆 **`rc 0`**、末列 `⇒ 紅 []；rc 0`；**二份之 `diff` 皆空** |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | 皆 **`rc 0`**；配地列 `3.5` ⇒ harness `35`／畫面 `34`、`0.0` ⇒ `36`／`35`，不符格 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]` |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |
| `V-6` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；二者之 blob 與增／刪之數出艙（發單側復驗時自倉重算）；`verify/` 之其餘一切檔對工項一之端相異 `0` |
| `V-7` | `§四-3` 閘 `8`〜`22` 之諸器（於工項二之 `commit`） | 皆 ＝ 其期 |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。

**推**（驗皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-357-k948`。

**工項三　入典與登記**（新側支·零生產碼·一 `commit`）：塊 `K4` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `P11` 附於 `CLAUDE.md` 之末（皆二進位·嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-357 工項三：K-9-51 之入典 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-357-k948`。

**工項四　執行報告入倉**（新側支·新檔 `docs/reports/W-G.9-357R_段三後處理之七項3至6與K-9-51_執行報告.md`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`11` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F16` 二子命令之全文、`k6s3 cmp` 二份、`F8 run` 二份 `diff` 之結果、`parity` 二份之末十列、`runall` 對拍之全文與 `diff` 之結果）；④ 三塊之實得（bytes／`sha256`）與二檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解；⑦ **設計說明**（`§三-5`）；⑧ **二檔之全文差異**（`§三-5`）；⑨ **各段耗時**（讀單／撰碼／前置／驗／登記／報告·規格單流程之試行評估）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-357 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-357-k948`。

### `§四-2`　復驗時補寫者（規格單流程·⛔ 本單之期）

發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之未處置不變、`R-5` 之「所施者恆已通過」、`R-6` 之候選與序、`R-7` 之 `raise` 已去、`R-10` 之二處同形、`R-11`／`R-12` 之落點）及其突變之判別力；併入主線之請示。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項一 ＝ `verify/probes/probe_WG9355_screenmerge.py` 增 `3`／刪 `2`；工項二 ＝ `app.py`／`verify/selection_pipeline.py`（增／刪 ＝ 工項二之 `V-6` 所出艙）；其餘逐檔 **`0`** |
| `2` | 生產碼 `34` 檔對 `17624a1` | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py` ＝ 工項二之 `V-6` 所出艙之 blob）；`verify/` 之一切檔相異恰 **`3`**（`verify/selection_pipeline.py`、`verify/probes/probe_WG9355_screenmerge.py`〔塊 `F14p`〕＋ 新檔 `verify/probes/probe_WG9357_k948.py`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`8` 檔：本單、`F16`、`verify/probes/probe_WG9355_screenmerge.py`、`app.py`、`verify/selection_pipeline.py`、`K-6` 典、`CLAUDE.md`、報告） |
| `4` | 二檔之 bytes | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `427954` → **`435245`**；`CLAUDE.md` `299948` → **`303630`**；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`32`**；主線 ＝ `17624a19c48715bcb1bcfd6af1a851d756d6d473`（⛔ 變）；`verify/W-G.9-357-k948` ＝ 工項四之 `commit`，其祖含 `17624a1`；`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 548 547 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 548 547` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `533`／`MAX` `548`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；**`K-9` `48`／`51`**／`[44, 47]`（自誤／`GB`／`VR` 皆 ＝ 開工態；`K-9` 唯增 `51`） |
| `8` | `python verify/probes/probe_WG9357_k948.py selftest <repo 絕對路徑>`；`… run <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`48`／`48`／`47`** |
| `10` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `11` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `12` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest …`；`… wiring …` | 皆 **`rc 0`** |
| `14` | `python verify/probes/probe_WG9350_frontroad.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `15` | `python verify/probes/probe_WG9351_intake.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`**（`selftest` 之突變 `M1`〜`M4` 皆轉紅·`X-4`） |
| `16` | `python verify/probes/probe_WG9352_endblock.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `17` | `python verify/probes/probe_WG9353_endmerge.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `18` | `python verify/probes/probe_WG9354_endcontest.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `19` | `python verify/probes/probe_WG9355_screenmerge.py selftest …`；`… run …` | 皆 **`rc 0`** |
| `20` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring …` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `21` | `python verify/probes/probe_WG9345_screen.py parity … 3.5 on <json>`；同 `0.0`；`… wiring …`；`python verify/probes/probe_WG9345_screen.py selftest` | 皆 **`rc 0`**（`parity` 之數 ＝ `V-4`） |
| `22` | `python verify/probes/probe_WG9344p1_pooltemp.py run <repo 絕對路徑> 3.5 on`；`… selftest`；`python verify/probes/probe_WG9344_k6s3.py selftest` | 皆 **`rc 0`** |

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F16` | `32592` B·`sha256` `5e321d797997c70d465905dbfd4c813b978207b3de9412dee47c8e97ef6fe8ed`·`549` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9357_k948.py` |
| `3` | 塊 `F14p` | `1819` B·`sha256` `95d5614e0833c29b5c3f580d2b355e4e37ad9de9206b6af65ca8cdf87b9ee62c`·`23` 列（圍欄內全文·末附換行）；`git apply` 於 `verify/probes/probe_WG9355_screenmerge.py`（開工態 blob `3648cd6c6cd13e8b5c6f73ecb95fd2a1feb5d29c`·`35946` B） |
| `4` | 塊 `K4` | `7291` B·`sha256` `e9eee06922ca6c1f0f3a81f545dea7d92d6eb9766e5c1b4dffa26afec38ddfbf`·`63` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`427954` B）之末後，期末 ＝ `435245` B |
| `5` | 塊 `P11` | `3682` B·`sha256` `a23f8d3b80aa20ae423c8abdc60577dd817725dfcef96cc10705463005ddc640`·`22` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`299948` B）之末後，期末 ＝ `303630` B |
| `6` | 施塊後之 blob（量測器） | `verify/probes/probe_WG9357_k948.py` `c77be87a1b2a0d094cb5ff1aee4edad43ad2c726`（`32592` B）；`verify/probes/probe_WG9355_screenmerge.py` `a78216399a6a5c708cff4d0b9f8bf14fa462f841`（`36045` B·增 `3`／刪 `2`）。🔒 `app.py`／`verify/selection_pipeline.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `7` | 量測器之二態 | 工項一之端：`F16 selftest`／`run`、`F14 selftest` 皆 `rc 1`（`§一` 項 `7`）；工項二施後：皆 `rc 0`（`§一` 項 `8` 之原型為其必過之實例） |
| `8` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十三實跑（態 `17624a1`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-1` `:100`（`§三-1` 之表頭·所觸之全稱否定〔「⛔ 動」「一字不變」「逐位同」等〕其母體皆為同列所具名之函式、鍵、路徑或紀錄 ⇒ **具名豁免**）、`P-4` `:65`（`§一` 態錨之表頭·所觸之箭頭係項 `3` 所引 `W-G.9-356` 之改前改後 bytes，其座標系 ＝ 該批之改前至改後，同格自載 ⇒ **具名豁免**）、`P-4` `:174`／`:198`（`§四-1` 工項二之驗、`§四-3` 收工閘之表頭·其箭頭之座標系皆為改前〔工項一之端或開工態〕至改後〔工項二之 `commit` 或工項四之端〕，表內自載 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `19744`–`27416`）⇒ `rc 0` |
| `9` | 收工閘之模擬（發單側·本機 Linux·原型之工作樹 ＋ 塊 `F16`／`F14p`／`K4`／`P11`·⛔ `push`） | 拋棄式 clone（`17624a1` ＋ 本單 ＋ 塊 `F16`／`F14p` ＋ 原型之二檔 ＋ 塊 `K4`／`P11` ＋ 報告之替身·五 `commit`·⛔ `push`）：閘 `1` 之刪除欄（工項一 ＝ `F14` 增 `3`／刪 `2`；工項二 ＝ 原型之數·⛔ 為期；餘皆 `0`）；閘 `2` 生產碼相異 `2`（`app.py`、`verify/selection_pipeline.py`）、`verify/` 相異 `3`；閘 `3` CR `0`（`V6.dxf` `12308`）；閘 `4` `427954 → 435245`、`299948 → 303630`（皆嚴格前綴）；閘 `6` `rc 0`（二閘皆過）；閘 `7` `rc 0`·四簿 ＝ 自誤 `533`／`548`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `48`／`51`／`[44, 47]`；新檔之 `git check-ignore` 皆無命中；工項一之端之三器之末列 ＝ `§一` 項 `7` |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````diff `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-357-k948`（工項二於驗皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F16`（新檔 `verify/probes/probe_WG9357_k948.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-357 量測器（發單側窗五十三擬·檔 F16·⛔ 由受單側改一字）：段三後處理之 `K-9-48` 七項 `3`〜`6` 與
`K-9-51`（剩餘土地之去處：同一地主已配得土地之街廓，距離該筆土地最近者先；同距離者配得面積大者先）。

子命令（一律 python verify/probes/probe_WG9357_k948.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6b_stage3_run`／`adj_intake`；`verify/selection_pipeline.py`
           取 `k6b_stage3_pool_temp`）。玩具：B3（X2(1)／X1(1)）、公園 PK（P1(1)）、B5（Y1(1)／K5(1)／Y2(1)）、道路 RD、
           B7（Z1(1)／Q7(1)）、BW（W1(1)）；歸戶 g1 ＝ X1／X2／Y1／Y2／Z1／W1（P1 依例）。段三：B3 右端之候選 X1(1)
           以同街廓之 X2(1) 於 ① 成；後處理之受詞 ＝ P1(1)（公設地上·平分入 X1／Y1）或 W1(1)（他街廓建地·整筆）。
           回呼：街廓內受併之累加 `>` 該街廓之容量 ⇒ 配餘地不合格（「不影響原位次」不過）。
           K1〜K15 ＝ 各支（整批通過／最大面積／第 5 項之距離序／同距離之 G 序／整筆之第 5 項／轉調配／0.01 ㎡／
           a′ 之折算／停機／舊鍵之重寫／公設地調配之 temp／調配之輸入）；K16〜K18 ＝ `K-9-50` 題一 4 之承前（玩具二：
           BX／BY 隔道路 RX 相對，只 BX 成，Y1 不能依原位次配地·其與其半併入 X1 不過 ⇒ 七項 3〜5）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  run      <repo> [<退縮> …]
           harness ＋ 畫面實跑本案（預設退縮 `3.5`、`0.0`）：R1 `alloc_state` 之 `G`（harness 之 `_k6b_callbacks` 與
           畫面之 `k6b_screen_callbacks`·同一宗地）——二者之保留集相同、`G` 之鍵 ＝ 保留集之聯集、逐宗差 ≤ `0.01`；
           R2 段三（harness `run_corner_pk_k6b`）之紀錄逐列 ＝ 開工態之實測（本器所載·數值容差 `0.01`），且其出之
           宗地⛔ 帶 `段三部分併出`／`段三餘量`（本案⛔ 觸發七項 `3`〜`6`）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import contextlib, copy, importlib.util, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _load(repo, rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(repo, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__, str(ex)[:160])
    out.append((name, got, exp))


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


# ── 玩具（⛔ 本案資料）──
H, PK, RDC = "住宅區", "鄰里公園", "道路"


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


def _world(a=None, p_owner="g1", w1=False):
    """B3（x∈[0,20]）：X2(1)[0,10]／X1(1)[10,20]；公園 PK（x∈[20,30]）：P1(1)；B5（x∈[30,50]）：Y1(1)[30,40]／
    K5(1)[40,45]／Y2(1)[45,50]；道路 RD（y∈[-10,0]）：R0(1)；B7（y∈[-40,-10]）：Z1(1)[30,40]／Q7(1)[40,50]；
    （w1）BW（y∈[30,40]·x∈[0,20]）：W1(1)。歸戶 g1 ＝ X1／X2／Y1／Y2／Z1／W1（P1 依 p_owner）。"""
    a = dict(dict(X1=100, X2=60, P1=200, Y1=100, K5=80, Y2=50, R0=500, Z1=100, Q7=90, W1=50), **(a or {}))
    t = [_tp("X2(1)", "B3", H, _R(0, 10, 0, 30), a["X2"]), _tp("X1(1)", "B3", H, _R(10, 20, 0, 30), a["X1"]),
         _tp("P1(1)", "PK", PK, _R(20, 30, 0, 30), a["P1"]),
         _tp("Y1(1)", "B5", H, _R(30, 40, 0, 30), a["Y1"]), _tp("K5(1)", "B5", H, _R(40, 45, 0, 30), a["K5"]),
         _tp("Y2(1)", "B5", H, _R(45, 50, 0, 30), a["Y2"]),
         _tp("R0(1)", "RD", RDC, _R(0, 50, -10, 0), a["R0"]),
         _tp("Z1(1)", "B7", H, _R(30, 40, -40, -10), a["Z1"]), _tp("Q7(1)", "B7", H, _R(40, 50, -40, -10), a["Q7"])]
    if w1:
        t.append(_tp("W1(1)", "BW", H, _R(0, 20, 30, 40), a["W1"]))
    own = {"X1": "g1", "X2": "g1", "Y1": "g1", "Y2": "g1", "Z1": "g1", "W1": "g1", "P1": p_owner,
           "K5": "gK", "R0": "gR", "Q7": "gQ"}
    blocks = {"B3": {"category": H}, "PK": {"category": PK}, "B5": {"category": H}, "RD": {"category": RDC},
              "B7": {"category": H}, "BW": {"category": H}}
    return t, own, blocks, {"RD": [(-10.0, -5.0), (60.0, -5.0)]}


def _g(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(cap, price=None, drop=(), no_g=False):
    """玩具之回呼：`alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內受併之累加（`面積_m2` 之和）
    `>` `cap[街廓]` ⇒ 該街廓之配餘地不合格一處；`G` ＝ 分攤登記面積 ＋ 面積（`no_g` ⇒ ⛔ 回 `G`）。
    `a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓)（`price` 缺者 ＝ 1）。`trial_winner` ＝ G ≥ 門檻即當選。"""
    price = price or {}

    def a_prime(src, dst):
        return _g(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)

    def alloc_state(temp, build):
        kept, bad, G, acc = {}, {}, {}, {}
        for b in build:
            acc[b["所屬街廓"]] = acc.get(b["所屬街廓"], 0.0) + float(b.get("面積_m2", 0) or 0)
            if b["暫編地號"] in drop:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
            G[b["暫編地號"]] = _g(b)
        for blk, v in acc.items():
            if v > cap.get(blk, 1e9) + 1e-9:
                bad[blk] = 1
        out = {"kept": kept, "bad_pools": bad, "err": None}
        if not no_g:
            out["G"] = G
        return out

    def trial_winner(temp, build, blk, end, cand):
        by = {b["暫編地號"]: b for b in build}
        g = _g(by[cand]) if cand in by else 0.0
        return (cand if g >= 150.0 else None), round(g, 2), 150.0
    return a_prime, trial_winner, alloc_state


ORDER = [{"最終序位": 1, "街廓": "B3", "端": "右", "暫編地號": "X1(1)"}]
KEYS3 = ("段三併出", "段三部分併出", "段三餘量")


def _go(ns, cap, price=None, drop=(), no_g=False, a=None, p_owner="g1", w1=False, pre=None):
    temp, own, blocks, cl = _world(a, p_owner, w1)
    for pid, kv in (pre or {}).items():
        next(t for t in temp if t["暫編地號"] == pid).update(kv)
    build = [t for t in temp if t["街廓分類"] == H]
    ap, tw, st = _cbs(cap, price, drop, no_g)
    t2, b2, log = ns["k6b_stage3_run"](ORDER, set(), own, temp, build, blocks, cl, ap, tw, st,
                                       log_print=lambda *x: None)
    by = {t["暫編地號"]: t for t in t2}
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
             tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
            for x in log if x.get("序") == "後處理"]
    acc = {k: round(float(v.get("面積_m2", 0) or 0), 2) for k, v in sorted(by.items())
           if float(v.get("面積_m2", 0) or 0)}
    keys = {k: {kk: (v[kk] if not isinstance(v[kk], dict) else dict(sorted((a2, round(b2_, 2)) for a2, b2_ in v[kk].items())))
                for kk in KEYS3 if kk in v} for k, v in sorted(by.items()) if any(kk in v for kk in KEYS3)}
    for k, v in keys.items():
        if "段三餘量" in v:
            v["段三餘量"] = round(float(v["段三餘量"]), 2)
    return post, acc, keys, sorted(b["暫編地號"] for b in b2), (t2, b2, own, blocks)


def _world4(a=None):
    """題一（`K-9-50`）之玩具：BX（X1(1)[0,10]／PX(1)）與 BY（Y1(1)[0,10]／QY(1)）隔道路 RX（X3(1)[0,10]／R0(1)·中心線
    y ＝ -5 ⇒ X3 切為上下各半）相對；B7：Z1(1)（x∈[60,70]·距 BY 50.99）。歸戶 g1 ＝ X1／X3／Y1／Z1。"""
    a = dict(dict(X1=100, X3=80, Y1=90, Z1=100, PX=500, QY=500, R0=300), **(a or {}))
    t = [_tp("X1(1)", "BX", H, _R(0, 10, 0, 30), a["X1"]), _tp("PX(1)", "BX", H, _R(10, 40, 0, 30), a["PX"]),
         _tp("X3(1)", "RX", RDC, _R(0, 10, -10, 0), a["X3"]), _tp("R0(1)", "RX", RDC, _R(10, 40, -10, 0), a["R0"]),
         _tp("Y1(1)", "BY", H, _R(0, 10, -40, -10), a["Y1"]), _tp("QY(1)", "BY", H, _R(10, 40, -40, -10), a["QY"]),
         _tp("Z1(1)", "B7", H, _R(60, 70, 0, 30), a["Z1"])]
    own = {"X1": "g1", "X3": "g1", "Y1": "g1", "Z1": "g1", "PX": "gP", "R0": "gR", "QY": "gQ"}
    blocks = {"BX": {"category": H}, "RX": {"category": RDC}, "BY": {"category": H}, "B7": {"category": H}}
    return t, own, blocks, {"RX": [(-10.0, -5.0), (60.0, -5.0)]}


def _go4(ns, cap, thr=None, drop=("Y1(1)",)):
    """二末端塊之競合（題一）：BX 左端 X1(1) 以其半（40）達門檻 130；BY 左端 Y1(1) 連其半（130）未達 200 ⇒ 只 BX 成；
    Y1 恆⛔ 保留（不能依原位次配地）⇒ 題一 4：Y1 連同其半併入 X1。"""
    thr = thr or {("BX", "左"): 130.0, ("BY", "左"): 200.0}
    temp, own, blocks, cl = _world4()
    build = [t for t in temp if t["街廓分類"] == H]
    ap, _tw, st = _cbs(cap, None, drop)

    def tw(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        g = _g(by[cand]) if cand in by else 0.0
        return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]
    order = [{"最終序位": 1, "街廓": "BX", "端": "左", "暫編地號": "X1(1)"},
             {"最終序位": 2, "街廓": "BY", "端": "左", "暫編地號": "Y1(1)"}]
    ct = [{"形": "一", "列": [("BX", "左", "X1(1)", 10.0), ("BY", "左", "Y1(1)", 10.0)]}]
    t2, b2, log = ns["k6b_stage3_run"](order, set(), own, temp, build, blocks, cl, ap, tw, st,
                                       log_print=lambda *x: None, contests=ct)
    by = {t["暫編地號"]: t for t in t2}
    post = [(x["候選"], x["層級"], x["結果"], x["受併宗"] if isinstance(x["受併宗"], str) else tuple(x["受併宗"]),
             tuple(sorted((k, round(v, 2)) for k, v in (x.get("併入量") or {}).items())))
            for x in log if x.get("序") == "後處理"]
    acc = {k: round(float(v.get("面積_m2", 0) or 0), 2) for k, v in sorted(by.items())
           if float(v.get("面積_m2", 0) or 0)}
    keys = {k: {kk: (v[kk] if not isinstance(v[kk], dict) else dict(sorted((a2, round(b2_, 2)) for a2, b2_ in v[kk].items())))
                for kk in KEYS3 if kk in v} for k, v in sorted(by.items()) if any(kk in v for kk in KEYS3)}
    for k, v in keys.items():
        if "段三餘量" in v:
            v["段三餘量"] = round(float(v["段三餘量"]), 2)
    return post, acc, keys, sorted(b["暫編地號"] for b in b2)


def _halt(ns, phrase, **kw):
    try:
        _go(ns, **kw)
    except RuntimeError as e:
        return ("停機", phrase in str(e))
    return ("無停機",)


C_ALL = {"B3": 1000.0, "B5": 1000.0, "B7": 1000.0}
_X2 = {"X2(1)": {"段三併出": ["X1(1)"]}}
_BL = ["K5(1)", "Q7(1)", "X1(1)", "Y1(1)", "Y2(1)", "Z1(1)"]


def _cap(**kw):
    return dict(C_ALL, **kw)


def _pool(sp, t2):
    pool = sp.k6b_stage3_pool_temp(t2)
    by0 = {t["暫編地號"]: t for t in t2}
    return ([(t["暫編地號"], t is by0[t["暫編地號"]], round(float(t["分攤登記面積_m2"]), 2)) for t in pool],
            pool is not t2)


def _intake(ns, world):
    t2, b2, own, blocks = world
    burden = {b: ns["F3_CATEGORY_BURDEN"][v["category"]] for b, v in blocks.items()}
    g_rows = [{"暫編地號": b["暫編地號"], "推進側別": "left"} for b in b2]
    r = ns["adj_intake"](t2, b2, g_rows, {}, own, burden)
    rows = {x["暫編地號"]: (x["類"], round(float(x["原有面積"]), 2), round(float(x.get("段三併出面積") or 0), 2))
            for x in r["slices"] if x["暫編地號"] in ("P1(1)", "R0(1)", "X2(1)")}
    units = [(u["歸戶"], u["軌"], round(float(u["原有面積合計"]), 2), sorted(x["暫編地號"] for x in u["共同負擔用地"]))
             for u in r["units"]]
    step4 = [(s["歸戶"], sorted(x["暫編地號"] for x in s["共同負擔用地"])) for s in r["step4"]]
    tot = {k: round(v[1], 2) for k, v in sorted(r["totals"].items()) if v[1]}
    cons = abs(sum(v[1] for v in r["totals"].values()) - float(r["all_area"])) <= 1e-6
    return rows, units, step4, tot, cons


def _cases(ns, sp):
    out = []
    # K1 整批通過 ⇒ 逐位同本批前（對照·新舊碼皆綠）
    _run(out, "K1 整批通過 ⇒ 一列、二受併宗各 100、⛔ 新鍵",
         lambda: _go(ns, C_ALL)[:4],
         ([("P1(1)", "後處理(c)", "成", ("X1(1)", "Y1(1)"), (("X1(1)", 100.0), ("Y1(1)", 100.0)))],
          {"X1(1)": 160.0, "Y1(1)": 100.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}, _BL))
    # K2 七項 3：X1 之分只容 60（最大面積）；Y1 之分 100 通過；餘 40 依第 5 項 ⇒ 距離最近之 B5（Y1·G 200 ＞ Y2·G 50）
    _run(out, "K2 最大面積 60 ＋ 第 5 項併入 Y1（距 0·G 大者）⇒ 全數併出",
         lambda: _go(ns, _cap(B3=120.0))[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 40.0),))],
          {"X1(1)": 120.0, "Y1(1)": 140.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}, _BL))
    # K3 第 5 項之序：B5（距 0）之 Y1 只容 20、Y2 不容 ⇒ 次 B7（距 10）之 Z1 收 20
    _run(out, "K3 第 5 項依距離：B5 之 Y1 部分 20、Y2 未成 ⇒ B7 之 Z1 收 20",
         lambda: _go(ns, _cap(B3=120.0, B5=120.0))[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "部分成", "Y1(1)", (("Y1(1)", 20.0),)),
           ("P1(1)", "後處理·第5項", "未成", "Y2(1)", ()),
           ("P1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),))],
          {"X1(1)": 120.0, "Y1(1)": 120.0, "Z1(1)": 20.0},
          {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)", "Z1(1)"]}, **_X2}, _BL))
    # K4 皆不能全收 ⇒ 餘 15 轉調配；三鍵
    _run(out, "K4 餘 15 轉調配：段三併出＋段三部分併出＋段三餘量",
         lambda: _go(ns, _cap(B3=120.0, B5=120.0, B7=5.0))[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "部分成", "Y1(1)", (("Y1(1)", 20.0),)),
           ("P1(1)", "後處理·第5項", "未成", "Y2(1)", ()),
           ("P1(1)", "後處理·第5項", "部分成", "Z1(1)", (("Z1(1)", 5.0),)),
           ("P1(1)", "後處理·第5項", "轉調配", "—", ())],
          {"X1(1)": 120.0, "Y1(1)": 120.0, "Z1(1)": 5.0},
          {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)", "Z1(1)"],
                     "段三部分併出": {"X1(1)": 60.0, "Y1(1)": 120.0, "Z1(1)": 5.0}, "段三餘量": 15.0}, **_X2}, _BL))
    # K5 同距離（B5）⇒ 配得面積（G）大者先：Y2（300）先於 Y1（200）
    _run(out, "K5 同距離者 G 大者先 ⇒ Y2 收 40",
         lambda: _go(ns, _cap(B3=120.0), a={"Y2": 300})[:4],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y2(1)", (("Y2(1)", 40.0),))],
          {"X1(1)": 120.0, "Y1(1)": 100.0, "Y2(1)": 40.0},
          {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)", "Y2(1)"]}, **_X2}, _BL))
    # K6 七項 4：不可拆分之建地 W1 整筆併入 X1 不過 ⇒ 未成 ⇒ 第 5 項：B5（距 10）之 Y1（G 100 ＞ Y2 50）整筆通過
    _run(out, "K6 整筆不過 ⇒ 未成；第 5 項整筆併入 Y1；W1 出 build",
         lambda: _go(ns, _cap(B3=90.0), p_owner="gP", w1=True, drop=("W1(1)",))[:4],
         ([("W1(1)", "後處理(a)", "未成", "X1(1)", (("X1(1)", 50.0),)),
           ("W1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 50.0),))],
          {"X1(1)": 60.0, "Y1(1)": 50.0}, {"W1(1)": {"段三併出": ["Y1(1)"]}, **_X2}, _BL))
    # K7 整筆皆不過 ⇒ 轉調配；W1 留於 build、⛔ 新鍵
    _run(out, "K7 整筆皆不過 ⇒ 轉調配；W1 留 build",
         lambda: _go(ns, _cap(B3=90.0, B5=0.0, B7=0.0), p_owner="gP", w1=True, drop=("W1(1)",))[:4],
         ([("W1(1)", "後處理(a)", "未成", "X1(1)", (("X1(1)", 50.0),)),
           ("W1(1)", "後處理·第5項", "未成", "Y1(1)", ()),
           ("W1(1)", "後處理·第5項", "未成", "Y2(1)", ()),
           ("W1(1)", "後處理·第5項", "未成", "Z1(1)", ()),
           ("W1(1)", "後處理·第5項", "轉調配", "—", ())],
          {"X1(1)": 60.0}, dict(_X2), sorted(_BL + ["W1(1)"])))
    # K8 可拆分者一分未併 ⇒ 未成二列；第 5 項（B3／B5 已不過 ⇒ 唯 B7）未成 ⇒ 轉調配；唯 段三餘量 ＝ 200
    _run(out, "K8 一分未併 ⇒ 段三餘量 200、⛔ 段三併出",
         lambda: _go(ns, _cap(B3=60.0, B5=0.0, B7=0.0))[:4],
         ([("P1(1)", "後處理(c)", "未成", "X1(1)", ()), ("P1(1)", "後處理(c)", "未成", "Y1(1)", ()),
           ("P1(1)", "後處理·第5項", "未成", "Z1(1)", ()), ("P1(1)", "後處理·第5項", "轉調配", "—", ())],
          {"X1(1)": 60.0}, {"P1(1)": {"段三餘量": 200.0}, **_X2}, _BL))
    # K9 最大面積以 0.01 ㎡ 為單位（容量 120.005 ⇒ 60.00·⛔ 60.01）
    _run(out, "K9 0.01 ㎡ 之格：容 60.005 ⇒ 收 60.00",
         lambda: _go(ns, _cap(B3=120.005))[:2],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 60.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 100.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 40.0),))],
          {"X1(1)": 120.0, "Y1(1)": 140.0}))
    # K10 a′ 之折算（PK 之地價為住宅區之 2 倍）：受併宗之增 ＝ 2 × 源之面積；段三部分併出以源之面積計
    _run(out, "K10 a′ 折算：X1 收 120（源 60）、Y1 收 200＋80",
         lambda: _go(ns, _cap(B3=180.0), price={"PK": 2.0})[:3],
         ([("P1(1)", "後處理(c)", "部分成", "X1(1)", (("X1(1)", 120.0),)),
           ("P1(1)", "後處理(c)", "成", "Y1(1)", (("Y1(1)", 200.0),)),
           ("P1(1)", "後處理·第5項", "成", "Y1(1)", (("Y1(1)", 80.0),))],
          {"X1(1)": 180.0, "Y1(1)": 280.0}, {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2}))
    _run(out, "K10′ a′ 折算之餘：B5／B7 亦滿 ⇒ 段三部分併出 {X1: 60, Y1: 100}（源）、段三餘量 40",
         lambda: _go(ns, _cap(B3=180.0, B5=200.0, B7=0.0), price={"PK": 2.0})[2],
         {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"], "段三部分併出": {"X1(1)": 60.0, "Y1(1)": 100.0},
                    "段三餘量": 40.0}, **_X2})
    # K11 第 5 項須 alloc_state 回 G；缺 ⇒ 停機（⛔ 以他量代之）
    _run(out, "K11 alloc_state 未回 G ⇒ 停機",
         lambda: _halt(ns, "未回 G", cap=_cap(B3=120.0), no_g=True), ("停機", True))
    # K12 入段三時已帶舊鍵者，本趟全數併出 ⇒ 舊鍵去之
    _run(out, "K12 舊之 段三餘量 於全數併出後去之",
         lambda: _go(ns, _cap(B3=120.0), pre={"P1(1)": {"段三餘量": 200.0, "段三部分併出": {"Q": 1.0}}})[2],
         {"P1(1)": {"段三併出": ["X1(1)", "Y1(1)"]}, **_X2})
    # K13 公設地調配之 temp：全數併出者去之；部分併出者以其餘量之比縮之（新物件）；未觸者同一物件
    _run(out, "K13 k6b_stage3_pool_temp：P1 以 15 入（新物件）、X2 去、餘同一物件",
         lambda: _pool(sp, _go(ns, _cap(B3=120.0, B5=120.0, B7=5.0))[4][0]),
         ([("X1(1)", True, 100.0), ("P1(1)", False, 15.0), ("Y1(1)", True, 100.0), ("K5(1)", True, 80.0),
           ("Y2(1)", True, 50.0), ("R0(1)", True, 500.0), ("Z1(1)", True, 100.0), ("Q7(1)", True, 90.0)], True))
    # K14 調配之輸入：部分併出之餘與一分未併者 ⇒ 入合併單位（K-9-45）——縱其歸戶有原位次配地
    _run(out, "K14 adj_intake：P1 之餘 15 入合併單位（公設軌）；守恆",
         lambda: _intake(ns, _go(ns, _cap(B3=120.0, B5=120.0, B7=5.0))[4]),
         ({"P1(1)": ("共同負擔用地·入合併單位", 15.0, 185.0), "R0(1)": ("共同負擔用地·入合併單位", 500.0, 0.0),
           "X2(1)": ("原位次配地", 60.0, 0.0)},
          [("g1", "公設軌", 15.0, ["P1(1)"]), ("gR", "公設軌", 500.0, ["R0(1)"])], [],
          {"原位次配地": 765.0, "共同負擔用地·入合併單位": 515.0}, True))
    _run(out, "K14′ adj_intake：一分未併之 P1（200）入合併單位",
         lambda: _intake(ns, _go(ns, _cap(B3=60.0, B5=0.0, B7=0.0))[4])[:2],
         ({"P1(1)": ("共同負擔用地·入合併單位", 200.0, 0.0), "R0(1)": ("共同負擔用地·入合併單位", 500.0, 0.0),
           "X2(1)": ("原位次配地", 60.0, 0.0)},
          [("g1", "公設軌", 200.0, ["P1(1)"]), ("gR", "公設軌", 500.0, ["R0(1)"])]))
    # K15 對照：整批通過之出，其公設地調配之 temp 與調配之輸入同本批前（P1 去之·入原位次配地）
    _run(out, "K15 對照：整批通過 ⇒ P1 ⛔ 入公設地調配之 temp；adj_intake 歸原位次配地",
         lambda: (sorted(t["暫編地號"] for t in sp.k6b_stage3_pool_temp(_go(ns, C_ALL)[4][0])),
                  _intake(ns, _go(ns, C_ALL)[4])[0]["P1(1)"]),
         (["K5(1)", "Q7(1)", "R0(1)", "X1(1)", "Y1(1)", "Y2(1)", "Z1(1)"], ("原位次配地", 200.0, 0.0)))
    # K16 對照：題一 4 之合併通過（逐位同本批前）
    _run(out, "K16 題一 4 對照：Y1 連同其半併入 X1 通過 ⇒ 一列",
         lambda: _go4(ns, {"BX": 1000.0, "BY": 1000.0, "B7": 1000.0}),
         ([("Y1(1)", "題一 4", "成", "X1(1)", (("X1(1)", 130.0),))], {"X1(1)": 170.0},
          {"X3(1)": {"段三併出": ["X1(1)"]}, "Y1(1)": {"段三併出": ["X1(1)"]}}, ["PX(1)", "QY(1)", "X1(1)", "Z1(1)"]))
    # K17 題一 4 之合併不過 ⇒ 七項 4：Y1 整筆不併入 X1 ⇒ 第 5 項 ⇒ Z1；Y1 之半（40）：七項 3 ⇒ X1 只容 20 ⇒ 餘 20 ⇒ Z1
    _run(out, "K17 題一 4 不過 ⇒ Y1 整筆經第 5 項入 Z1；其半 X1 收 20、餘 20 入 Z1（⛔ 停機）",
         lambda: _go4(ns, {"BX": 60.0, "BY": 1000.0, "B7": 1000.0}),
         ([("Y1(1)", "題一 4", "未成", "X1(1)", ()), ("Y1(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 90.0),)),
           ("X3(1)", "題一 4", "部分成", "X1(1)", (("X1(1)", 20.0),)),
           ("X3(1)", "後處理·第5項", "成", "Z1(1)", (("Z1(1)", 20.0),))],
          {"X1(1)": 60.0, "Z1(1)": 110.0},
          {"X3(1)": {"段三併出": ["X1(1)", "Z1(1)"]}, "Y1(1)": {"段三併出": ["Z1(1)"]}}, ["PX(1)", "QY(1)", "X1(1)", "Z1(1)"]))
    # K18 同上而 B7 只容 100 ⇒ X3 之餘 10 轉調配；段三部分併出含已取得一端之半（40 ＋ 20）
    _run(out, "K18 題一 4 之餘 10 轉調配：X3 段三部分併出 {X1: 60, Z1: 10}、段三餘量 10",
         lambda: _go4(ns, {"BX": 60.0, "BY": 1000.0, "B7": 100.0})[2],
         {"X3(1)": {"段三併出": ["X1(1)", "Z1(1)"], "段三部分併出": {"X1(1)": 60.0, "Z1(1)": 10.0}, "段三餘量": 10.0},
          "Y1(1)": {"段三併出": ["Z1(1)"]}})
    return out


def _perturb(v):
    if isinstance(v, bool):
        return not v
    if isinstance(v, (int, float)):
        return v + 1
    if isinstance(v, str):
        return v + "′"
    if isinstance(v, tuple):
        return (v + ("′",)) if not v else (_perturb(v[0]),) + v[1:]
    if isinstance(v, list):
        return v + ["′"]
    if isinstance(v, dict):
        return dict(v, **{"′": 0})
    return ("′", v)


def selftest(repo):
    ns, _ = _harvest(repo)
    import selection_pipeline as sp
    need = [n for n in ("k6b_stage3_run", "adj_intake", "F3_CATEGORY_BURDEN") if n not in ns]
    if need or not hasattr(sp, "k6b_stage3_pool_temp"):
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    cases = _cases(ns, sp)
    print("── 段三後處理之七項 3〜6 與第 5 項之序（K-9-51）──")
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    hits = 0
    for i in range(len(cases)):
        pert = [(n, g, (_perturb(e) if j == i else e)) for j, (n, g, e) in enumerate(cases)]
        r = _report(pert, verbose=False)
        base = set(red)
        code = cases[i][0].split()[0]
        if (set(r) - base) == {code} or (code in base and set(r) == base):
            hits += 1
    ok0 = hits == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {hits}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本案（harness ＋ 畫面）──
R2_EXPECT = {
    3.5: [
        (1, 'R5', '左', '628-18(2)', '②', '未成', '—', ()),
        (2, 'R3', '右', '628-45(2)', '①', '成', '628-45(2)', (('628-45(2)', 783.29),)),
        (3, 'R2', '左', '628-41(1)', '②', '成', '628-41(1)', (('628-41(1)', 241.7),)),
        (4, 'R3', '右', '628-42(2)', '—', '略·已定案', '—', ()),
        (5, 'R5', '左', '628-45(1)', '①', '成', '628-45(1)', (('628-45(1)', 541.69),)),
        (6, 'R2', '左', '628-42(1)', '—', '略·已定案', '—', ()),
        (7, 'R3', '右', '628-28(1)', '—', '略·已定案', '—', ()),
        (8, 'R2', '左', '628-27(1)', '—', '略·已定案', '—', ()),
        (9, 'R5', '左', '628-53(2)', '—', '略·已定案', '—', ()),
        (10, 'R2', '左', '628-40(1)', '—', '略·已定案', '—', ()),
        (11, 'R5', '左', '628-7(2)', '—', '略·已定案', '—', ()),
        (12, 'R3', '右', '628-27(2)', '—', '略·已定案', '—', ()),
        (13, 'R3', '右', '628-29(1)', '—', '略·已定案', '—', ()),
        ('後處理', 'R2', '—', '628-30(2)', '後處理(a)', '成', '628-45(2)', (('628-45(2)', 150.3),)),
        ('後處理', 'RD2', '—', '628-45(5)', '後處理(b)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 105.0325), ('628-45(2)', 101.1875))),
        ('後處理', 'RD2', '—', '628-30(4)', '後處理(b)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 48.7553), ('628-45(2)', 51.6647))),
        ('後處理', 'G1', '—', '628-45(3)', '後處理(c)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 136.545), ('628-45(2)', 136.545))),
        ('後處理', 'RD4', '—', '628-45(4)', '後處理(c)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 112.3), ('628-45(2)', 112.3))),
    ],
    0.0: [],
}


def _norm_log(log):
    out = []
    for r in log or []:
        rv = r.get("受併宗")
        rv = rv if isinstance(rv, str) else tuple(rv)
        q = tuple(sorted((k, round(float(v), 4)) for k, v in (r.get("併入量") or {}).items()))
        s = r.get("序")
        out.append((s if isinstance(s, str) else int(s), r.get("街廓"), r.get("端"), r.get("候選"), r.get("層級"),
                    r.get("結果"), rv, q))
    return out


def _same_log(a, b):
    if len(a) != len(b):
        return False
    for x, y in zip(a, b):
        if x[:7] != y[:7] or [k for k, _ in x[7]] != [k for k, _ in y[7]]:
            return False
        if any(abs(u - v) > TOL for (_, u), (_, v) in zip(x[7], y[7])):
            return False
    return True


def run(repo, sbs):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if "k6b_screen_callbacks" not in ns or not hasattr(sp, "_k6b_callbacks"):
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    f4 = _load(repo, "verify/probes/probe_WG9345_screen.py", "f4_for_f16")
    red = []
    for sb in sbs:
        ss = fst.session_state
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                snap = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fst, snap)
                rv.build_ownership(ns, fst, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
                params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
            cb = list(cb_by.values())
            saved, k917 = copy.deepcopy(dict(ss)), copy.deepcopy(ns["K917_DROPPED"])
            with contextlib.redirect_stdout(io.StringIO()):
                H = sp._k6b_callbacks(ns, fst, cb, cad, params, sb, snap)["alloc_state"](tp, bp)
            ss.clear(); ss.update(copy.deepcopy(saved))
            ns["K917_DROPPED"].clear(); ns["K917_DROPPED"].update(copy.deepcopy(k917))
            pk, g = f4._screen_inputs(ns, fst, snap, cb, cad, params, tp, bp, sb)
            qs = f4.QuietSt(ss)
            with contextlib.redirect_stdout(io.StringIO()):
                S = ns["k6b_screen_callbacks"](qs, pk_kwargs=pk, g_kwargs=g)["alloc_state"](tp, bp)
            ss.clear(); ss.update(copy.deepcopy(saved))
            ns["K917_DROPPED"].clear(); ns["K917_DROPPED"].update(copy.deepcopy(k917))
            with contextlib.redirect_stdout(io.StringIO()):
                _d, _s, _o, _w, _f, t3, b3 = sp.run_corner_pk_k6b(ns, fst, cb, cad, params, tp, bp, sb, snapshot=snap)
            log = copy.deepcopy(ss.get("f3_k6b_stage3_log") or [])
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {sb}：執行中止 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
            print("⇒ rc 3（無從判定）")
            return 3
        kept_h = {b: sorted(v) for b, v in sorted((H.get("kept") or {}).items())}
        kept_s = {b: sorted(v) for b, v in sorted((S.get("kept") or {}).items())}
        allk = sorted(p for v in kept_h.values() for p in v)
        gh, gs = H.get("G"), S.get("G")
        e1 = H.get("err") is None and S.get("err") is None and kept_h == kept_s and len(allk) > 0
        e2 = isinstance(gh, dict) and isinstance(gs, dict) and sorted(gh) == allk and sorted(gs) == allk
        dmax = max((abs(float(gh[p]) - float(gs[p])) for p in allk), default=0.0) if e2 else None
        e3 = e2 and dmax <= TOL and all(float(gh[p]) > 0 for p in allk)
        ok1 = e1 and e2 and e3
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：保留集 harness ＝ 畫面 {e1}（{len(allk)} 宗）；G 之鍵 ＝ 保留集 {e2}；"
              f"逐宗差 max {dmax}（≤ {TOL}）{e3}")
        if not ok1:
            red.append(f"R1@{sb}")
        got = _norm_log(log)
        e4 = _same_log(got, R2_EXPECT.get(sb, []))
        nk = sorted(t["暫編地號"] for t in t3 if "段三部分併出" in t or "段三餘量" in t)
        nr = sorted({r[5] for r in got} & {"部分成", "轉調配"})
        ok2 = e4 and not nk and not nr
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：段三紀錄 {len(got)} 列 ＝ 開工態 {e4}；新鍵之片 {nk}；新結果 {nr}")
        if not ok2:
            red.append(f"R2@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], argv[2]
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `F14p`（`git apply` 之差異·`verify/probes/probe_WG9355_screenmerge.py`）

````diff
diff --git a/verify/probes/probe_WG9355_screenmerge.py b/verify/probes/probe_WG9355_screenmerge.py
index 3648cd6..a782163 100644
--- a/verify/probes/probe_WG9355_screenmerge.py
+++ b/verify/probes/probe_WG9355_screenmerge.py
@@ -374,7 +374,8 @@ def _t3(ns, ss, merge):
              (True, True, [L3], [L3], ORDER)),
             (f"{tag}b 段三本體與合併再試各恰一次", (rig.s3_n, rig.merge_n), (1, 1)),
             (f"{tag}c 段三之試算配地亦 'trial'", [c[1] for c in gs3], ["trial"]),
-            (f"{tag}d 段三之 alloc_state 之出", rig.s3_state, {"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None}),
+            (f"{tag}d 段三之 alloc_state 之出", rig.s3_state, {"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None,
+                                                           "G": {"A(1)": 0.0}}),
             (f"{tag}e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位",
              (a.get("temp") is s3r[0], a.get("build") is s3r[1], a.get("locked")), (True, True, {"C(1)"})),
             (f"{tag}f 回傳之宗地 ＝ 末態（同一物件）", (ret is not None and ret["temp"] is fin[0], ret is not None and ret["build"] is fin[1]),
@@ -471,7 +472,7 @@ def _t6(ns, ss):
             stt = cb["alloc_state"](t0, b0)
         gs = [c for c in rig.calls[n0:] if c[0] == "g"]
         out.append(("T6d 試算配地（alloc_state）之出與其 'trial'", (stt, [c[1] for c in gs]),
-                    ({"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None}, ["trial"])))
+                    ({"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None, "G": {"A(1)": 0.0}}, ["trial"])))
         n0 = len(rig.calls)
         with contextlib.redirect_stdout(io.StringIO()):
             ev = cb["alloc_eval"](t0, b0)
````

## 附錄丙　塊 `K4`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-51` 之立 ＋ `K-9-48` 七項 `3`〜`6` 之落地狀態（`W-G.9-357`·⛔ 上文一字不刪·純末端追加）

### 🔒 `K-9-51`　**段三後處理之剩餘土地（`K-9-48` 七項 `5`）：同一地主已配得土地之街廓不只一個者，依距離該筆土地最近者先逐一試併，每次皆須通過「不影響原位次」之檢核；距離相同者，先試該地主配得面積較大者；都不行才與該地主其他不能分配之土地合併進調配（`K-9-45`）**（KL 裁 `2026-09-29`·canonical·**逐字**）

**編號之由**（`W-G.9-357 §零-1`）：`K-9-51` 於開工態 `17624a1` 之宣告框 `0`；鬆框 `1` 列（`docs/orders/W-G.9-338_重量單.md:35`）係其時「對照乙［必為零］」所列之未取號·⛔ 占用 ⇒ 取之。
**出處**：發單側窗五十三（`2026-09-29`）；呈文附示意圖一張（`K-9-48第5項_剩餘土地之去處_示意.png`·⛔ 入倉）。

**發單側所呈（逐字·⛔ 增刪一字）**：

> 依 `CLAUDE.md` 之依賴序，下一張單是 `K-9-48` 七項之 `3`／`5`／`6`。讀典後發現第 `5` 項有一處尚未裁示，需請您判斷（**真需域專業判斷**），示意圖已附上。
>
> **【現況】**
> 街角合併重試之後，地主在道路、公設地上的土地，要分往他已配得土地的街廓。若整筆併入會影響原位次，程式目前是整筆都不併，並以紅字標示「未處置」。這筆土地維持原狀，留待其後調配。
>
> **【要改成】**
> 依您已裁之七項辦理：
> - **第 `3` 項**：可拆分之土地（道路、公設地上）只併入不影響原位次之最大面積，如圖中 R3 只收 `60 ㎡`。
> - **第 `4` 項**：不可拆分之建地，整筆不併入。
> - **第 `5` 項**：剩下之土地先併入同一地主另一個已配得土地之街廓，並須通過檢核。都不行時，才與該地主其他不能分配之土地合併進調配（`K-9-45`）。
>
> 第 `5` 項沒有說明：這種街廓若不只一個，要先試哪一個。我的提案是**距離該筆土地最近者先**，如圖中先試 R5，不過再試 R7。距離相同時，先試甲配得面積較大者。
>
> **【對土地的影響】**
> - **本案**：無。退縮 `3.5 m` 之街角合併重試後處理 `5` 筆全數通過；退縮 `0 m` 沒有街角合併重試。
> - **他案**：依提案，剩下之 `40 ㎡` 依地價折算後併入甲在 R5 之宗，R7 不動。若改採「配得面積大者先」，則併入甲在 R7 之宗，R5 不動。
>
> **【要你判斷】**
> 第 `5` 項之剩餘土地，若同一地主已配得土地之街廓不只一個，是否依「距離該筆土地最近者先」逐一試併（每次都須通過不影響原位次之檢核），都不行才進調配？（是／否；若否，請示先後順序）
>
> **【通知】**（只是知會，點頭即可）
> - 「最大面積」以 `0.01 ㎡` 為單位求得。
> - 公設地上之土地平分時，通過檢核之一側照收其一半；只有未通過之一側改收最大面積，其差額依第 `5` 項處理。
>
> 您裁示後，我即依此擬 `K-9-48` 七項 `3`／`5`／`6` 之規格單，作為規格單流程之次輪。

**KL 之答（`2026-09-29 12:20`·逐字）**：
> 是

**裁之內容**（KL「是」＝ 所呈【要你判斷】為「是」；【通知】二則 KL 未駁）：
① `K-9-48` 七項 `3`／`4` 剩下之土地（含七項 `6` 所指「全數歸入不符檢核」者之剩下之土地），先併入**同一地主另一個已配得土地之街廓**；此種街廓不只一個 ⇒ 依**距離該筆土地最近者先**逐一試併，**距離相同者先試該地主配得面積較大者**；每次併入皆須通過「不影響原位次」之檢核（`K-9-48` 其三·檢核之作法）；都不行 ⇒ 與該地主其他不能分配之土地合併進調配（`K-9-45`）。
② 七項 `3` 之「最大面積」以 `0.01 ㎡` 為單位求得（【通知】一）。
③ 公設地上之土地平分時，通過檢核之一側照收其一半；只有未通過之一側改收最大面積，其差額依 ① 處理（【通知】二）。

**射程**：① 及於**任一案件**；
② 距離、配得面積、候選之範圍、可拆分之土地於第 `5` 項之分次併入、`K-9-50` 題一 `4` 之承前、剩下之土地於其後各段之表示 ⇒ 發單側之讀法（下開·⛔ 充裁）；
③ **⛔ 及於**：不可拆分之建地（七項 `4`）之併入目標街廓無從決定（所鄰之已配得街廓非恰一）⇒ 仍停機（`W-G.9-344` 原單停機款 `9`·候另呈）；道路片之二半皆不鄰該地主已配得之街廓 ⇒ 仍記「未處置」（手冊五則之「兩側皆無」·候調配之單）。

**發單側之讀法**（⛔ 充裁·以【通知】呈 KL）：
1. **同一地主** ＝ 同一歸戶（`t8_ownership_map`·`K-6 §一` 之「同地主」）；**已配得土地** ＝ 現態（本筆試併之前·含本段已併入者）之配地中「保留」之宗；**候選之範圍** ＝ 該地主一切保留之宗，扣除本筆已試而未全收之街廓（含其原受併宗所在之街廓）之宗。
2. **距離** ＝ 該筆土地之重劃前幾何與候選宗所在街廓（段三之輸入中該街廓之全部重劃前切片之聯集）之最短距離，相鄰者為 `0`，比較至 `0.01 m`；**配得面積** ＝ 候選宗於現態之應分配面積（配地之 `G`）；二者皆同 ⇒ 暫編地號字典序小者先。
3. **分次併入**：可拆分之土地於第 `5` 項之每一候選，先試其剩下之全部；不過 ⇒ 依 ② 求最大面積併入之，其餘續試下一候選；不可拆分之建地於每一候選一律整筆，過即止。
4. **`K-9-50` 題一 `4` 之承前**（該裁讀法 `6` 之「不過 ⇒ 停機（`K-9-48` 七項 3〜5 未落地）」自本批起依本裁處之）：未取得之一端之候選（不可拆分）先整筆試併入已取得之一端之受併宗，不過 ⇒ 依 ① 另試；其分得之一半（可拆分）先以最大面積併入已取得之一端之受併宗，餘依 ①。
5. **剩下之土地於其後各段**：可拆分之土地部分併入者，其併出之量記於該片（依來源之面積），其餘量入調配之輸入之合併單位（縱其地主已有原位次配地·`K-9-45`「與該地主其他不能分配的土地合併」）；公設地調配（舊 W-F·F.3／F.4）所取之宗地以其餘量之比計之；已部分併出之片⛔ 再入末端塊之合併再試（`K-9-49 ③`「已併入」）。不可拆分之建地都不行者，維持原狀（其後依原位次配地之判入調配）。

**本案之量**（⛔ 為裁之一部·發單側窗五十三·態 `17624a1`·harness·退縮 `3.5 m`／`0 m`）：本案⛔ 觸發——退縮 `3.5 m` 之段三後處理 `5` 列（`628-30(2)`／`628-45(5)`／`628-30(4)`／`628-45(3)`／`628-45(4)`）整批通過；退縮 `0 m` 無段三之列。配地⛔ 變。

**落地狀態**：
- 七項 `3`〜`6` 與本裁之 **harness 路徑與畫面路徑** ＝ `W-G.9-357` 工項二（側支 `verify/W-G.9-357-k948`·二路徑共用 `k6b_stage3_run`）；讀法 `4`（題一 `4` 之承前）同批。
- 入主線 ⬜（另候 KL 放行）。
- 射程 `③` 之二情形 ⬜（候另呈／調配之單）。
````

## 附錄丁　塊 `P11`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`（剩餘土地之去處）入側支（`W-G.9-357`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-357-k948`（本批新立·起於主線 `17624a19c48715bcb1bcfd6af1a851d756d6d473`）；主線⛔ 動。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-48` 七項 `3`〜`6` ＋ `K-9-51`（段三後處理·harness ＋ 畫面·二路徑共用 `k6b_stage3_run`） | 整批不過 ⇒ 逐項：不可拆分者整筆、不過 ⇒ 未成 ⇒ 第 `5` 項；可拆分者逐受併宗、不過 ⇒ 最大面積（`0.01 ㎡` 之格）⇒ 其餘第 `5` 項；第 `5` 項 ＝ 同一歸戶之保留宗，距離（至其街廓）近者先、同距離者 `G` 大者先；都不行 ⇒ 轉調配 | 🔶（側支；入主線另候 KL 放行） | `docs/orders/W-G.9-357_規格單.md` |
| `2` | `K-9-50` 題一 `4` 之承前（該裁讀法 `6` 之停機） | 未取得之一端之候選與其半併入已取得之一端不過 ⇒ 依序 `1` 處之（⛔ 停機） | 🔶（同上） | 同上 |
| `3` | 部分併出之表示與其後各段 | 片之 `段三部分併出`（依來源之面積）／`段三餘量`；調配之輸入：其餘量與一分未併者入合併單位（縱其地主有原位次配地）；公設地調配之 temp（`k6b_stage3_pool_temp`）以餘量之比計之；末端塊之合併再試⛔ 取已部分併出之片 | 🔶（同上） | 同上 |
| `4` | 試算之 `alloc_state` 增回 `G`（harness `_k6b_callbacks`·畫面 `k6b_screen_callbacks`） | 保留宗之應分配面積（第 `5` 項同距離之序） | 🔶（同上） | 同上 |
| `5` | 以程式字樣為錨之接線檢查及其突變（規格單流程·復驗時補寫） | 序 `1`〜`4` 之落點 | ⬜ | 次單 |
| `6` | 入主線 ＋ 主 checkout 之同步 | — | ⬜（候 KL 放行） | 次單 |
| `7` | 畫面「自動計算公設分配」展開區（`main()`·舊 W-F 之顯示）之 temp | 仍以 `段三併出` 濾之 ⇒ 部分併出之片之餘量⛔ 顯示於該區（他案始有） | ⬜ | 畫面批 |
| `8` | 不可拆分之建地之併入目標街廓無從決定（所鄰之已配得街廓非恰一）⇒ 停機 | `K-9-51` 射程 `③` | ⬜（候另呈） | — |

🔒 **本案之量**（發單側窗五十三實測·態 `17624a1`·harness·器 `verify/probes/probe_WG9357_k948.py run` 之 `R2`）：本案⛔ 觸發（退縮 `3.5 m` 之段三後處理 `5` 列整批通過；`0 m` 無段三之列）⇒ 配地⛔ 變（其驗 ＝ `W-G.9-357` 之 `V-2`〜`V-5`）。
🔒 **依賴序**：本批（側支）→ 序 `5`／`6`（次單·零生產碼 ＋ 入主線）→ 規格步 `3` → `4` → `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ 本表序 `7`）。
🔒 **併記（取號器之對照乙）**：`verify/probes/wg9268_gate6_occupancy.py` 於 `17624a1` 之人造對照 `W-G.9-963`（「須 `=0`」）之寬式 `D3` ＝ `2`——命中 `docs/reports/W-G.9-356R_入主線與畫面路徑之接線檢查_執行報告.md` 所內嵌之該器出艙二列（`:113`／`:114`）；受詢之號之判⛔ 受影響（器之 `rc` 唯繫受詢）。凡報告內嵌該器之出艙者皆將使之，候驗證框架之殘項批處之。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `8`（子字串框·含圖例與本列）·列 ＝ `6`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: 233e0a31a5fbd7f440f86b9c5b73a698b382f5e01de6c18cc3bb588f0b4e6b9e
