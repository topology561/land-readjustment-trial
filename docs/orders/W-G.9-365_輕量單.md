# `W-G.9-365`　輕量單：指令檔之載入改制（`CLAUDE.md`／`AGENTS.md` 不自動載入 ＋ 常設規則索引 ＋ 技能之載入設定與失準之更正 ＋ 審查代理之更正）＋ 主 checkout 之同步 ⛔ 零生產碼

> **本單建議等級 ＝ `medium`**（本單⛔ 令 CC 撰碼；受詞 ＝ `.claude/` 之設定、規則、技能與審查代理，`AGENTS.md`，`CLAUDE.md` 之末端追加，主 checkout 之同步）。
> **發單** ＝ 發單側窗六十八·`2026-10-04`。**受單** ＝ CC 新窗（工項零〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**）。
> **級** ＝ **輕**（零生產碼；⛔ 動 `verify/` 之一字與任何宗地之配地；⛔ 跑 `run_verification.py`／`run_all`。受詞為 CC 之載入設定與文件之末端追加，其驗為機械之逐位對拍，故取輕級；KL 之放行見 `§二`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `0e0edb3a40e68efd6748c08c198eaa51851b603c`（`W-G.9-364` 工項四）；遠端 heads `35`；KL 之主 checkout 於 `wip/s1-endpart` ＝ `0e0edb3…`（`W-G.9-364` 工項五）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`。塊 `S`／`R1`／`R2`／`FX`／`C1`〜`C8`／`P19`／`AG`／`AM`／`GF`／`CK` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**。
> 🔑 **來源檔**（檔名逐字 `W-G.9-365_輕量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。本批之一切改動皆自本單之塊抽出。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔與 `verify/` 之一字；`docs/` 下除本單與報告二新檔外之一字；`CLAUDE.md` 除塊 `P19` 之純末端追加外之一字；`.claude/skills/` 下既有之檔除塊 `C1`〜`C8` 之純末端追加外之一字（`failure-archaeology/SKILL.md` 等其餘技能檔⛔ 動）；`.claude/output-styles/`、`.claude/launch.json`；任何側支之推送、刪除或改寫。
> 🔴 **本單⛔ 令 CC 判「孰為正典」**；塊之文字 CC ⛔ 改一字——CC 認為塊之文字有誤者，照實回報（停機款 `9`）。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `0e0edb3a40e68efd6748c08c198eaa51851b603c`；`git ls-remote --heads origin` 之列數 ＝ `35`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 577 566` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `562`／`MAX` `577`、`GB` `194`／`201`、`VR` `80`／`95`、`K-9` `52`／`55`（＝ `W-G.9-364` 收工閘 `7`）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。
5. **放行**：KL 貼本單之同一訊息須逐字答問一「是」（`§二`）；未答或答「否」⇒ 停機款 `11`。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態 `0e0edb3` 之 `docs/` 全檔 **`964`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗六十八實跑 `python verify/probes/wg9268_gate6_occupancy.py 0e0edb3 W-G.9-365 W-G.9-364 W-G.9-396`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-365`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-364` | `2`／`8`／`5` | `2`／`8`／`7` | `13`（寬式 `15`） | `4` | `5`／`54` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `16`／`25` | 🟢 宣告框 `0`、鬆框非零 |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `28`／`31` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

本批⛔ 鑄自誤／`GB`／`VR`／`K-9` 之號；收工閘 `7` 以四簿之值不變驗之。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `0e0edb3`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `35`，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 任一塊之 bytes／`sha256` 與 `§五-1` 不符；或 `git apply --check` 不過；或施後之 blob ≠ `§五-1` |
| `4` | 末端追加之受詞（塊 `C1`〜`C8`、`P19` 之九檔）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 塊 |
| `5` | 工項一之驗（塊 `GF` 重生成 ≠ 塊 `FX` 逐位；塊 `CK` 之 `rc` ≠ `0`；`.claude/settings.json` 之 JSON 不可解或其 `hooks` ≠ 開工態） |
| `6` | `§四` 收工閘任一 ≠ 期 |
| `7` | 任一 `push` 之目標非 `wip/s1-endpart`，或被拒，或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項四：主 checkout 之追蹤檔有變動；其 `HEAD` ≠ `0e0edb3…` 或其分支 ≠ `wip/s1-endpart`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過；或 CC 認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `10` | 本批任一新檔為 `git check-ignore` 所命中 |
| `11` | KL 貼本單之同一訊息未逐字答問一「是」 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `21`。

---

## `§一`　態錨（發單側窗六十八自倉實取·本機 Linux·倉外工作樹）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `wip/s1-endpart` ＝ `0e0edb3a40e68efd6748c08c198eaa51851b603c`；遠端 heads **`35`**（`verify/` `30`·`wip/` `3`·`claude/` `1`·`main` `1`）；十側支 ＝ `W-G.9-364` 收工閘 `5` 所列（皆⛔ 變） |
| `2` | `W-G.9-364` 之復驗（發單側窗六十八·依交接文六十七 `§四-2`） | 五 `commit`（`e14d2ef`／`c4820a0`／`aa94de3`／`0f106ce`／`0e0edb3`）之訊息首列 ＝ 該單所令逐字；收工閘 `1`〜`5` 自倉重算皆符（逐 `commit` 之 numstat、生產碼 `34` 檔對 `cb5490a` 相異唯 `verify/run_verification.py` ＝ `f5b896e5…`、對 `7d8e954` 相異 `3`、八檔 CR `0`〔`V6.dxf` `12308`〕、四簿嚴格前綴且其尾 ＝ 塊 `K9`／`G8`／`E10`／`P18` 逐位、heads `35`、十側支⛔ 變）；塊 `F23t`／`RV1` 施於 `cb5490a` ⇒ `de0a7e06…`／`f5b896e5…`；閘 `6`〜`8` 自跑皆 `rc 0`（`F23` `selftest` `K1`〜`K40`·`P0` `40／40`；`run` 二退縮 `R1`〜`R4` 皆 ✅·紀錄 `34`／`43` 列）；閘 `9` 抽驗 `11` 命令（`wfns_ast` `48`／`48`／`47`、`main_synth`、`probe_WG9341_synth`、`harvest_key`、`endmerge` 之 `selftest`／`wiring`、`k948_wiring`、`F21` 之 `selftest`／`wiring`、`F22 mut`）皆 `rc 0`·stderr `0` B；報告之 `run_all` 之前後比 ＝ 該單 `§一` 項 `8`——**全數相符** |
| `3` | 本批之受詞之開工態（`git rev-parse 0e0edb3:<檔>`·bytes） | `.claude/settings.json` `cfb137cea18617e541e3cf1e96636613ab2117a7`（`267` B）；`.claude/agents/redistribution-reviewer.md` `a2f6d140a63b98738c465a92803353336dc9c37a`（`4840` B）；`AGENTS.md` `35e7b6aa2fffa17f7c598422ff4ee808bf513918`（`3307` B）；`CLAUDE.md` `ae21c3cdde364c274eddcda72e1442089102fd93`（`334109` B）；`.claude/skills/README.md` `9d51bbe79cfc7b343e872779139636c19d6a8a6f`（`2386` B）；`.claude/skills/cad-layer-semantics/SKILL.md` `ed9835b6c28307f4fb48bdfd7297dfdde4e6ad17`（`17201` B）；`.claude/skills/corner-selection-rules/SKILL.md` `7790528bf3cc001731c647c86e216d7efca9928f`（`7915` B）；`.claude/skills/fixture-provenance/SKILL.md` `88b5d12e3f777d6e682c0c3e3bfe4536f5186a78`（`5852` B）；`.claude/skills/g-formula-rules/SKILL.md` `ba8b9e89d5369abed55622255a4503ca421c13dc`（`3440` B）；`.claude/skills/stop-conditions/SKILL.md` `f0c8ef73d013f2a09f3191cf0ed76e2ccac96260`（`2651` B）；`.claude/skills/validation-runbook/SKILL.md` `9c0557a456b89e63bfe33ab9e1dd4008bda15edb`（`8292` B）；`.claude/skills/wave-discipline/SKILL.md` `f77a2074f6835387210bd4f8a731198448302b40`（`2960` B）；`git ls-tree 0e0edb3` 無 `.claude/rules/` 與 `.claude/skills/failure-archaeology-index/`；皆以換行結尾·CR `0` |
| `4` | 載入之機制（Claude Code 之文件·發單側窗六十八查） | 專案之 `CLAUDE.md` 於每個工作階段之始全文載入，**上層目錄之 `CLAUDE.md` 亦載入**（CC 於主 checkout 之下之 worktree 開工時，主 checkout 之 `CLAUDE.md` 一併載入）；`claudeMdExcludes`（設定之鍵·可置於專案之 `.claude/settings.json`）以 glob 比對絕對路徑而略過之，亦施於 `AGENTS.md`；`.claude/rules/*.md` 無 `paths` 者於開工時載入，有 `paths` 者於讀寫相符之檔時載入；`skillOverrides` 之 `"user-invocable-only"` ⇒ 該技能不列於 Claude、唯 `/` 選單可叫用；技能之全文唯叫用時載入，其後留於 context |

---

## `§二`　KL 之語與射程

KL `2026-10-04 06:08`（逐字）：「1. 刪除 ruflo-core」「2. 因現在我會常駐Opus 5.5 模型，所以參考prompt-audit 第 1、2 項指出：`CLAUDE.md `約 87% 是舊紀錄，行號錨已失效...協助修改相關檔案以匹配最新 Opus5.5 模型」「3. 若效益不高舊部要用 /plugin enable cc-plugin-you-should-know@builtin 的功能好了」「4. 繼續 交接文 §四-2 的復驗」。

- 其 `1`：`ruflo-core` 係 KL 本機之 Claude Code 外掛，⛔ 在倉內（本倉 `.claude/settings.json` 無之）⇒ ⛔ 屬本單；由 KL 於本機卸載（發單側另告其法）。
- 其 `2` ⇒ 本單。`CLAUDE.md` 與 `.claude/skills/**` 屬 `常規一 ②` 補款③ (2) 之正典檔（`deletions` 恆 ＝ `0`）⇒ 本單⛔ 刪改其既有之一字：`CLAUDE.md` 改為不自動載入、另立自動載入之索引；技能之失準處以末端追加之更正節處之，或以設定停止其自動叫用。審查代理與 `AGENTS.md` ⛔ 在該列 ⇒ 逐處更正其過時之句。
- 其 `3`：發單側之評估係效益有限 ⇒ ⛔ 啟用；⛔ 屬本單。
- 其 `4`：`W-G.9-364` 之復驗 ⇒ `§一` 項 `2`（全數相符）。

**問一**（KL 於貼本單之同一訊息答之）：

> 【現況】CC 每次開工，會先把整份專案總則（`CLAUDE.md`，約 3,500 列，大部分是歷次施工的更正紀錄）全文讀進記憶。CC 的工作區若在您的程式資料夾之下（上一張單 364 即是如此，見其執行報告所載之工作區位置），同一份會被讀進兩次。新舊規定並列、互相矛盾。另外，舊的「停機條件」「波段紀律」說明已過時；審查員的說明仍把「公設地補償」「同歸戶合併」當成後面波次才能做的事，會把現在正在做的工作判為違規。
> 【要改成】總則全文保留、一字不刪，照舊只在末端追加。CC 開工時改讀一份約 120 列的「常設規則索引」，需要細節時再依索引查原文；日後新增或修改規則的施工單，須同時更新索引。兩份過時、一份過長（失敗考古，約 4,800 列）的技能說明不再自動讀入，需要時仍可手動叫出；其餘技能說明的過時之處，在各檔末尾補一節更正；審查員改以裁定正典與當期施工單為準。完成後同步您本機的程式資料夾。附帶一點：您電腦上若日後另建「個人共用的總則檔」，在本專案也不會自動讀入（CC 之前的檢查回報您目前沒有此檔）。
> 【對土地的影響】無。不改任何程式、任何配地結果、任何驗證用的數字。
> 【要你判斷】是否同意依本單調整 CC 開工時讀入的規則檔，並同步您本機的程式資料夾？（是／否）

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

本單（二進位複製）入 `docs/orders/W-G.9-365_輕量單.md`；入倉之 blob ＝ 來源逐位（停機款 `2`）。`commit` 訊息逐字 `W-G.9-365 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　`.claude/` 之載入改制（主線·零生產碼·一 `commit`）

1. 抽出塊 `S`／`R1`／`R2`／`FX`／`C1`〜`C8`／`AG`／`GF`／`CK`（`GF`／`CK` 抽至 `<O>`·⛔ 入倉），逐塊對拍 `§五-1`（停機款 `3`）。
2. 塊 `S` 以二進位**全檔取代** `.claude/settings.json`；塊 `R1` 寫為新檔 `.claude/rules/常設規則索引.md`；塊 `R2` 寫為新檔 `.claude/rules/配地碼之領域指引.md`；塊 `FX` 寫為新檔 `.claude/skills/failure-archaeology-index/SKILL.md`。
3. 塊 `C1`〜`C8` 各以二進位附於其受詞（`§五-1` 之受詞欄·七技能檔與 `.claude/skills/README.md`）之末（刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `4`）。
4. `git apply --check <O>\AG.diff` ⇒ 過；`git apply <O>\AG.diff`。
5. **驗**（停機款 `5`·出艙存 `<O>`）：
   - `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同。
   - `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ 於本工項之態**必紅**：`rc 1`，不合恰一列 `L88 命中列數=0: '指令檔之載入改制'`，末列 `索引列數 123；內部字樣 120；外部指標 9；不合 1`（其字樣待工項二之塊 `P19` 方入 `CLAUDE.md`·判別力之必紅對照）；工項二後重跑 ⇒ `rc 0`（收工閘 `9`）。
   - `python -c "import json;d=json.load(open(r'<repo>\.claude\settings.json',encoding='utf-8'));print(sorted(d))"` ⇒ `['claudeMdExcludes', 'hooks', 'skillOverrides']`；其 `hooks` 與 `git show 0e0edb3:.claude/settings.json` 之 `hooks` 相等。
6. 施後之 blob ＝ `§五-1` 項 `19` 中本工項之 `13` 檔（即除 `AGENTS.md`、`CLAUDE.md` 外者·逐檔·停機款 `3`）；`git status --porcelain --untracked-files=all` ＝ 唯本工項之受詞：`M` `10` 列（`.claude/settings.json`、`.claude/agents/redistribution-reviewer.md` 與塊 `C1`〜`C8` 之八受詞）、`??` `3` 列（`.claude/rules/常設規則索引.md`、`.claude/rules/配地碼之領域指引.md`、`.claude/skills/failure-archaeology-index/SKILL.md`）；施工樹之根之來源檔（本單）若在，不計（⛔ `add`）。`commit` 訊息逐字 `W-G.9-365 工項一：.claude/ 之載入改制（claudeMdExcludes·常設規則索引·技能之載入設定與失準之更正·審查代理之更正）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　`AGENTS.md` 之更正 ＋ `CLAUDE.md` 之載入改制之記（主線·零生產碼·一 `commit`）

塊 `AM`、`P19` 之 bytes／`sha256` 對拍 `§五-1`（停機款 `3`）。塊 `AM`：`git apply --check` ⇒ 過；`git apply`。塊 `P19` 以二進位附於 `CLAUDE.md` 之末（停機款 `4`）。重跑 `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ **`rc 0`**·末列 `索引列數 123；內部字樣 120；外部指標 9；不合 0`。施後之 blob ＝ `§五-1` 項 `19`。`commit` 訊息逐字 `W-G.9-365 工項二：AGENTS.md 之更正 ＋ CLAUDE.md 之載入改制之記（末端追加）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-365R_指令檔之載入改制_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`11` 之三值（款·期·實）；③ 塊之實得（bytes／`sha256`）與九個末端追加之受詞之改前改後 bytes；④ 工項一之驗之出艙（含 `checkidx` 之必紅與工項二後之必綠）；⑤ `§二` 之放行（KL 之逐字）；⑥ CC 之自捕與自解；⑦ 各段耗時。收工閘之實測值與工項四之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-365 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ `0e0edb3a40e68efd6748c08c198eaa51851b603c`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。
2. **撞檔前置**（`自誤 542`）：甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 集 `A`；乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 集 `U`；丙、`A ∩ U` 逐檔：`hash-object` 對 `rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8`）；不等 ⇒ 停機款 `8`·⛔ 動；丁、甲乙丙之出艙存 `<O>`。
3. `git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`branch --show-current` ＝ `wip/s1-endpart`；`rev-parse HEAD` ＝ 工項三之 `commit` 之全 `40` 碼；`hash-object .claude/settings.json` ＝ `§五-1` 項 `19` 之值；`hash-object CLAUDE.md` ＝ 同；`hash-object app.py` ＝ `176f90c96f6c13ede5c0c4e2425bebbbe827bf51`；`status --porcelain --untracked-files=no` ＝ 空。

**KL 之核對**（工項四之後·於對話回報發單側）：於主 checkout 新開 CC 工作階段，輸入 `/context`，看其記憶檔之列——**不含** `CLAUDE.md` 與 `AGENTS.md`，**含** `.claude/rules/常設規則索引.md`。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之增刪（`git show --numstat`） | 工項零 ＝ 本單之增／`0`；工項一 ＝ `.claude/agents/redistribution-reviewer.md` `9`／`9`；`.claude/rules/常設規則索引.md` `123`／`0`；`.claude/rules/配地碼之領域指引.md` `18`／`0`；`.claude/settings.json` `9`／`0`；`.claude/skills/README.md` `9`／`0`；`.claude/skills/cad-layer-semantics/SKILL.md` `11`／`0`；`.claude/skills/corner-selection-rules/SKILL.md` `13`／`0`；`.claude/skills/failure-archaeology-index/SKILL.md` `158`／`0`；`.claude/skills/fixture-provenance/SKILL.md` `6`／`0`；`.claude/skills/g-formula-rules/SKILL.md` `11`／`0`；`.claude/skills/stop-conditions/SKILL.md` `12`／`0`；`.claude/skills/validation-runbook/SKILL.md` `11`／`0`；`.claude/skills/wave-discipline/SKILL.md` `13`／`0`（`13` 檔）；工項二 ＝ `AGENTS.md` `3`／`3`、`CLAUDE.md` `8`／`0`；工項三 ＝ 報告之增／`0` |
| `2` | 生產碼 `34` 檔、`verify/` 與 `docs/` | 生產碼 `34` 檔與 `verify/` 之一切檔對 `0e0edb3` 相異 **`0`**；`docs/` 對 `0e0edb3` 相異恰 **`2`**（`A`：本單、報告）；本批之新檔（本單、報告、`.claude/` 之三新檔）之 `git check-ignore` 皆無命中 |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 本批所動之 `17` 檔（本單、報告、`§五-1` 項 `19` 之 `15` 檔）合計 **`0`** |
| `4` | 末端追加之九檔 | 改前（`0e0edb3`）皆為改後之嚴格前綴，其尾 ＝ 塊 `C1`〜`C8`／`P19` 逐位；改後之 bytes ＝ `§五-1` 項 `19` |
| `5` | 施後之 blob | `§五-1` 項 `19` 之 `15` 檔逐檔相符 |
| `6` | 自限 | 遠端 heads **`35`**；主線 ＝ 工項三之 `commit`，其祖含 `0e0edb3`；十側支⛔ 變（值 ＝ `W-G.9-364` 收工閘 `5`） |
| `7` | `python verify/probes/probe_WG9270_closegate.py 577 566 .`；`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔> 577 566` | 皆 **`rc 0`**；四簿之值 ＝ `§零-0` 項 `3`（本批⛔ 鑄號） |
| `8` | `python verify/tools/wg942_append_audit.py 0e0edb3` | **`rc 0`**；末列 `結論：✅ 全部成立`（受檢 `77` 筆） |
| `9` | `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md`；`python <O>\gen_fa_index.py <repo> <O>\FX_regen2.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同 | `rc 0`·末列 `索引列數 123；內部字樣 120；外部指標 9；不合 0`；逐位同 |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項一〜二（`0e0edb3` ＋ 本批之全部塊）並實跑閘 `2`〜`5`、`7`〜`9` 之器 ⇒ 見 `§五-1` 項 `20`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `S` | `503` B·`sha256` `0fc742bddfed9d161e48c028f982f951ba2268b191e4bcf7208f74cf9970b248`·`24` 列（圍欄內全文·末附換行）；全檔取代 `.claude/settings.json` |
| `3` | 塊 `R1` | `24624` B·`sha256` `b8d436b50ad5e1bda0a2978390cd17e5489b96fdf84a33dd62a43619a6f9eeb9`·`123` 列（圍欄內全文·末附換行）；新檔 `.claude/rules/常設規則索引.md` |
| `4` | 塊 `R2` | `1365` B·`sha256` `256e1249497dfa5c78706dd6177023085755b4a14d0aebdb619efa47e473b086`·`18` 列（圍欄內全文·末附換行）；新檔 `.claude/rules/配地碼之領域指引.md` |
| `5` | 塊 `FX` | `21080` B·`sha256` `df14158df94ff8d94ee12cfd802c5d7fc1f4b213fd53ee891087a8490b666b1c`·`158` 列（圍欄內全文·末附換行）；新檔 `.claude/skills/failure-archaeology-index/SKILL.md` |
| `6` | 塊 `C1` | `1292` B·`sha256` `42cceb7b4e62e70d364bed753949c9a9650ac482fa6a1100f88355346c745084`·`11` 列（圍欄內全文·末附換行）；附於 `.claude/skills/g-formula-rules/SKILL.md` 之末 |
| `7` | 塊 `C2` | `2081` B·`sha256` `ea084f79db2a7047485b765ef128fdb10d9cdbd06c229eb9e79b6188e7777997`·`13` 列（圍欄內全文·末附換行）；附於 `.claude/skills/corner-selection-rules/SKILL.md` 之末 |
| `8` | 塊 `C3` | `1047` B·`sha256` `960d3e7b4752f192168207bb0b7469b38f35878b974aa126e92769c830ff5ecc`·`11` 列（圍欄內全文·末附換行）；附於 `.claude/skills/cad-layer-semantics/SKILL.md` 之末 |
| `9` | 塊 `C4` | `1080` B·`sha256` `b2c5281ccd435807610c9859e262b6e44ed3e7d625b007c100c1cd09514c1ead`·`11` 列（圍欄內全文·末附換行）；附於 `.claude/skills/validation-runbook/SKILL.md` 之末 |
| `10` | 塊 `C5` | `351` B·`sha256` `7defdb1f5720e62a0d743bad3a7ea229163742f48dabb915a2133e06226a6e04`·`6` 列（圍欄內全文·末附換行）；附於 `.claude/skills/fixture-provenance/SKILL.md` 之末 |
| `11` | 塊 `C6` | `750` B·`sha256` `5bc151571c9a8a7ec9fa86bb60c050d038bc8cbfd685fe1580028ffe9ee168b3`·`9` 列（圍欄內全文·末附換行）；附於 `.claude/skills/README.md` 之末 |
| `12` | 塊 `C7` | `1182` B·`sha256` `d39951237e9d41bc4e3ed1c3984b64b1d71e29e1f34b4502526ce29d6d20a226`·`12` 列（圍欄內全文·末附換行）；附於 `.claude/skills/stop-conditions/SKILL.md` 之末 |
| `13` | 塊 `C8` | `997` B·`sha256` `421246f2f2441eb7d75fa05c62929d491831376846657ff05ac07fd51a49a810`·`13` 列（圍欄內全文·末附換行）；附於 `.claude/skills/wave-discipline/SKILL.md` 之末 |
| `14` | 塊 `AG` | `5592` B·`sha256` `db2aef49c0ac2af60c9d7bbbe67a832fd40bb8e6787f555cb3291c030df8f149`·`56` 列（圍欄內全文·末附換行）；`git apply` 於 `.claude/agents/redistribution-reviewer.md`（`git apply --numstat` ＝ `9`／`9`） |
| `15` | 塊 `AM` | `2025` B·`sha256` `faff54de82aeccae369f9bd1749461b9641bb485b10561e33058b2709f9123c4`·`24` 列（圍欄內全文·末附換行）；`git apply` 於 `AGENTS.md`（`git apply --numstat` ＝ `3`／`3`） |
| `16` | 塊 `P19` | `2640` B·`sha256` `3a1b8c5bd76d41fd75d76ba23111f599a60d87517d6dc85d0b68f8509b5bf380`·`8` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md` 之末（工項二） |
| `17` | 塊 `GF` | `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（圍欄內全文·末附換行）；倉外 `<O>\gen_fa_index.py`（⛔ 入倉·塊 `FX` 之重生成器） |
| `18` | 塊 `CK` | `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列（圍欄內全文·末附換行）；倉外 `<O>\checkidx.py`（⛔ 入倉·索引之定位字樣檢） |
| `19` | 施後之 blob（`git hash-object`·bytes） | `.claude/agents/redistribution-reviewer.md` `db57d498ef8bcac0239ff431eeb7064457adabd3`（`5278` B）；`.claude/rules/常設規則索引.md` `ee0685a144f62ffcc9e0c8ab0eafb3ef946f4b5a`（`24624` B）；`.claude/rules/配地碼之領域指引.md` `5e0310b6fce85a1da26572e5d1783c3b0054e919`（`1365` B）；`.claude/settings.json` `4e33f016f12c07eb56dc93d49daab0445a33899b`（`503` B）；`.claude/skills/README.md` `1166bd9a4dafb79b3012d6389186ad20ab9b5abe`（`3136` B）；`.claude/skills/cad-layer-semantics/SKILL.md` `b241ce9295072369e0788b926a00b77dfa3da199`（`18248` B）；`.claude/skills/corner-selection-rules/SKILL.md` `93fd90c8df28c7b9718b9af663d60cae0bad5817`（`9996` B）；`.claude/skills/failure-archaeology-index/SKILL.md` `8eca25c7edbd54175e4c03d82d4bfe8f3d97c1b3`（`21080` B）；`.claude/skills/fixture-provenance/SKILL.md` `5ca21b71c7eabd79183f9e47b6e6ee7076929d96`（`6203` B）；`.claude/skills/g-formula-rules/SKILL.md` `b54e350be0dc49727230bc178de0c46792a5fd7c`（`4732` B）；`.claude/skills/stop-conditions/SKILL.md` `f251d400f26719bdd1803e1520b67f306eaf19f9`（`3833` B）；`.claude/skills/validation-runbook/SKILL.md` `07c502d3d41dee888b1c80ea10299dd5f596589d`（`9372` B）；`.claude/skills/wave-discipline/SKILL.md` `f82fabb30b4214759af9d9a631a94be880441f55`（`3957` B）；`AGENTS.md` `b3917925a617f5bb1e20e4bdb56c24bba54682c2`（`3483` B）；`CLAUDE.md` `b85cd9c20801be24faa3e1a9a88e3be9b9bb50ea`（`336749` B） |
| `20` | 模擬（發單側·本機 Linux·`git worktree add --detach <S> 0e0edb3`·⛔ `push`） | 本批之全部塊施於 `<S>`：九個末端追加之受詞皆嚴格前綴且其尾 ＝ 塊；`.claude/settings.json` 之 JSON 可解、其 `hooks` ＝ 開工態；施後之 blob ＝ 項 `19`；`git diff --numstat` ＝ 閘 `1` 之工項一、二之列；`gen_fa_index.py` 之重生成與塊 `FX` 逐位同（`則 124；加註節 14；列 158`）；`checkidx.py` ⇒ `索引列數 123；內部字樣 120；外部指標 9；不合 0`（`rc 0`）；`wg942_append_audit.py 0e0edb3` ⇒ `rc 0`·`結論：✅ 全部成立`（受檢 `77`）；`probe_WG9270_closegate.py 577 566 .` ⇒ `rc 0`；生產碼 `34` 檔與 `verify/` 對 `0e0edb3` 相異 `0`；新檔三之內⛔ 含 `<檔名>:<行號>` 之錨 |
| `21` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗六十八實跑（態 `0e0edb3`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-1` `:807`（附錄午塊 `CK` 之器內之錯誤訊息字串·非斷言 ⇒ **具名豁免**）、`P-4` `:642`（附錄丑塊 `C8` 之「開工序」·其箭頭之座標系 ＝ 閱讀之先後·塊內自載 ⇒ **具名豁免**）、`P-4` `:669`（附錄寅塊 `AG` 之刪除列所載原文·其箭頭 ＝ 條件之後果 ⇒ **具名豁免**）、`P-4` `:720`（附錄卯塊 `AM` 之差異之上下文·`AGENTS.md` 原文之表 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `21232`–`28952`）⇒ `rc 0` |

抽取式 ＝ 圍欄開列（`` ````json ``、`` ````markdown ``、`` ````diff `` 或 `` ````python ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。塊 `C1`〜`C8`、`P19` 之首列為空列（其抽取之首位元組 ＝ `\n`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜三 ⇒ 依 `§二` 之放行、各驗皆符後逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）。
3. 收工後，主 checkout 之根之來源檔（本單，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `S`（全檔取代 `.claude/settings.json`）

````json
{
  "claudeMdExcludes": [
    "**/CLAUDE.md",
    "**/AGENTS.md"
  ],
  "skillOverrides": {
    "failure-archaeology": "user-invocable-only",
    "stop-conditions": "user-invocable-only",
    "wave-discipline": "user-invocable-only"
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python \"$CLAUDE_PROJECT_DIR/verify/tools/wg9237_heredoc_guard.py\""
          }
        ]
      }
    ]
  }
}
````

## 附錄乙　塊 `R1`（新檔 `.claude/rules/常設規則索引.md`）

````markdown
# 常設規則索引（每次開工自動載入）

自 `W-G.9-365` 起，倉根之 `CLAUDE.md`（約 3,500 行）與 `AGENTS.md` 不再自動載入（`.claude/settings.json` 之 `claudeMdExcludes`），以免每個工作階段先吃掉大量 context、且新舊條文並陳而互相牴觸。`CLAUDE.md` 仍是規則之全文與紀錄簿，照舊只作末端追加；本檔是它的索引。

讀法：
- 每條末〔〕內為定位字樣。要讀全文時，以 `grep -nF "<字樣>" CLAUDE.md` 找到該列，再以 Read 讀其前後。標「外：檔」者於該檔 grep。
- 施工單引用 `CLAUDE.md` 之某節時，一律讀該節原文，不以本索引代替。
- 本索引不另立規則。與 `CLAUDE.md` 全文或裁定正典有出入時，以後者為準。`CLAUDE.md` 是 append-only：後節可取代前節而前節原文不刪，所以同一事以最後之節為準。
- 本檔不記行號（行號衛生）；本檔之更動須經施工單。
## 一、權威序與讀法
- 權威序：docs/rulings/（裁定正典）→ CLAUDE.md →《配地計算總規格_v3.md》→ 104 手冊。與正典衝突以正典為準；v3 與手冊衝突以手冊為準並報 KL。〔權威序（上位優先）〕
- 街角規定範圍、可分配判準、街廓平均深度、最小分配面積、面積歸屬：一律以 docs/rulings/K-6_街角地分配程序與可分配判準.md 為準，本檔不重述。〔裁定正典（先讀〕
- 「§」＝裁定節，「段」＝施工階段，不得互代；技能在 .claude/skills/。〔節號體系（禁互代）〕〔常駐技能規則見〕
- 技能之載入（`W-G.9-365`）：`failure-archaeology`（約 4,800 行）不自動叫用，先讀 `failure-archaeology-index` 再依其指示讀單則；`stop-conditions`、`wave-discipline` 之內容已過時（停機與流程以本索引第四、五組為準），亦不自動叫用。各技能檔末之「失準之更正」節優先於其上文。
- 純程式結構（射程、母體、粒度、框、工序、批之切分、量測器設計）得由發單側自裁，判準為不動任何宗地之配地結果；改變準據本身恆須 KL。〔外：docs/orders/W-G.9-265_自解款與開工閘三級_五則未決之裁_覆蓋帳與逐款對位.md「授權之界（逐字重述）」〕
- 落地與否以碼為準，不以文書時序為準。〔以碼定正本〕
- 守恆式恆成立：ΣG（街廓內所有分配地）＋調配池＝街廓 DXF 面積；任何調配都消耗調配池。〔### 守恆式（最高鐵律）〕
- 四欄面積中「登記面積_m2」「幾何面積_m2」「分攤登記面積_m2」為唯讀欄，寫入後永不改動；「面積_m2」為 a′ 之累加器。〔### 四欄面積（唯讀欄寫入後永不改動）〕
- 禁靜默兜底：缺值應警示或 loud raise，不得以案件值編造（如 `or 3.5` 會吃掉合法之 0）。〔不得靜默編造〕
- 調配階段之流程與已停止適用之舊條款（含舊七級之序、W-F 之處置）見調配規格。〔外：docs/specs/調配階段_泛用規格_v1.md「已停止適用之條款」〕
## 二、三方分工與傳遞
- KL＝域裁定者（裁定具約束力）與 UI 操作者；claude.ai（發單側）＝規格、量測器、驗收與覆核，不寫生產碼；CC＝實作，push 後才回報。〔三方分工鐵律**：〕
- 發單側可讀公開倉；獨立復現由 CC 之閘與發單側之覆核共同承擔；單中之倉側事實斷言仍標「待 CC 復現」（理由：出單時未必已量）。〔發單側<u>有</u>倉之存取權〕
- 人之攔截是這條鏈唯一實測有效之守備，不得把發單→施工→報告接成無人流水線。〔### 🔧 三　🛑 **⛔ 不得據此把整條鏈接成無人流水線**〕
- claude.ai 新窗自行 clone 現查（`git -c core.autocrlf=false clone --branch wip/s1-endpart`，拋棄式），先對 HEAD 全 40 碼與 app.py blob，不符即停；入正典或登記表之倉側斷言仍須 CC 現查方為【倉】。〔**常規六（倉為公開·後續窗自行現查）**〕
- 施工單入 docs/orders/，CC 自倉讀單；報告 push 入倉，發單側自倉讀。〔傳遞媒介 ＝ 倉〕
- 發單側稱「已產出／已建檔」之檔，KL 見檔案卡方採信。〔### 🔧 四　KL 側之一條規則〕
- 報告本體寫 docs/reports/W-*.md 並 commit，聊天只作通知；完工回報＝push 後單獨跑 `git log -1 --format="%h %s"` 原樣貼出並附報告路徑。〔倉內報告＝唯一本體〕〔完工聊天回報〕
- 規格單流程自 W-G.9-359 起為常態：發單側出規格、量測器與驗收，CC 依規格寫生產碼；CC 之唯讀獨立 reviewer 為常設步（驗後、推前），其發現涉域判斷或規格漏載即停機上呈。另有恆常附款 a〜ab（擬單之常設條款）登記於同簿。〔規格單流程之試行·期滿〕〔外：docs/reports/W-G.9波_恆常附款登記表.md「期滿與續行」「## `§一`　款之總表」〕
## 三、收官、push 與放行
- 未 push 不得報收官：`git rev-parse origin/wip/s1-endpart` 須已含該 commit（不是 origin/main）。不綠不推、不推不報。〔未 push 不得報收官（最高紀律〕
- 交接文不得把未 push 之 commit 記為倉態；接手者先以 `git ls-remote` 實查，不以交接文所載 commit 為錨。〔**常規九　交接文之倉態宣告**〕
- 零生產碼 commit 逕行 push；生產碼 commit 須請示。生產碼＝app.py、verify/stepg_pipeline.py、verify/run_all.py、verify/run_verification.py 任一字（含註解），逐 commit 以 `git diff --name-only` 判並出艙其輸出（含空輸出）。〔「生產碼」之**機械界定**〕
- 此款只放寬「誰批准 push」，不放寬禁改清單；常規一之四項於零生產碼側不再拘束。〔### 🔧 三　與 `常規一` 之關係〕
- 生產碼 commit 先推側分支 `verify/<單號>-c<n>`，發單側逐位元組復驗、請示 KL，KL 放行後主線才前進；主線其間前進則 rebase、重推、重驗。〔`W-G.9-206` 補款　側分支復驗〕
- 閘之量測與其守護之動作（commit／push）分開呼叫，量測結果先出艙判讀；單令之 commit 順序若使報告推不出去，先推報告並逐字回報偏離。〔### 常規補款 `一`〕〔### 🔧 裁 四〕
- 同時交付多張單時，後單之開工閘須經「倉內先多一個零生產碼 commit 是否轉紅」之自檢；會紅者改綁性質，不綁 commit 身分。〔### 常規補款 `三`〕
- 「生產碼 34 檔」（app.py＋verify/ 頂層 *.py）係 blob 期初＝期末之受檢母體，與上列四檔（push 授權）為二事；「十一檔」一語停用。〔十一檔」一語之廢止〕
## 四、停機、自解與上呈
- CC 遇疑義得自解續辦，須五項全滿足：零土地後果（任一讀法皆不動任一宗地之 G／面積／街角歸屬／抵費地／配地幾何）、零生產碼（含註解）、可機驗且當批跑必紅／必綠對照、可逆（append-only 或新檔）、寫入報告「本批之自解清單」。缺一即停機上呈。〔### 一　自解款〕
- 白名單八類（非窮盡）得自解；黑名單恆停機：動任一宗地之 G／面積／街角歸屬／抵費地／配地幾何、動生產碼、二讀法之土地後果相異、須新訂準據或廢止／放寬既有閘、涉 KL 已裁之款而二讀法相斥。〔#### 一-2　黑名單〕
- 未寫入自解清單者視同未自解（驗收不過）；停機回報恆為正確程序，本款不得作為放寬判準之依據。〔### 一　自解款〕
- 必答題未裁先施工＝停機上呈；意思決定不自動裁，標旗呈 KL。〔必答題未裁先施工＝停機〕
- 施工單內部互斥：發單側當場裁並記自誤，不上呈 KL；CC 取保守項續辦並逐字回報。〔**常規二（施工單自相矛盾）**〕
- 無土地後果之程序事項（檔名、欄名、節號、格式、目錄位置）：有倉之一方提 2–3 候選，發單側核可，不上呈 KL；逐字使用正典術語之命名例外。〔**常規三（無土地後果之事項）**〕
- 上呈裁定題前先搜前窗並令 CC 搜正典，皆查無方得上呈。〔併記之修法〕
- 停機上呈前先以已知真／已知偽之對照證量測器非紅；「算不出」與「判為偽」不得共用同一出艙碼。〔停機上呈之前，必先自證〕
- 規格單之停機款（CC）：量測器紅而須改量測器始能過；規格有歧義而涉域上判斷；本案配地有任一改變而單未載其期。〔外：docs/reports/W-G.9波_恆常附款登記表.md「試行期之停機款（CC）」〕
## 五、開工閘三級與驗收
- 施工單於開工閘節自載級（依該批所能破壞之物定）：輕＝純登記（不跑 run_verification）；中＝純診斷（全批跑一次 run_verification）；重＝動生產碼或配地幾何（完整儀式：二態對拍、run_all 名目差集、逐 commit 放行）。〔### 二　開工閘三級〕
- 中途觸及更高級之受詞者，不得就地升級續辦，須停機上呈；任何級不得略去必紅／必綠對照；觸及 verify/out/ 落檔或以宗地號為受詞者不得用輕級。〔### 二　開工閘三級〕
- 本分支為「准紅碼」：驗收＝與凍存之期望 FAIL 名單逐項相同（名目＋正規化原因，verify/wv_reconcile.py 於每次 run_all 對帳），不是全綠；類 III 之判準為「組成相對基座有變」。〔本分支 `wip/s1-endpart` 現為「准紅碼」〕〔### 🔧 裁 一〕
- 驗收判準之比較端不得繫於倉態（HEAD、index、--cached、git status），須為具名 commit 之 blob。〔一般式（併記·考古節 `123`）〕
- main() 內之敘述 run_all 從不執行 ⇒ 改動須另附合成案。〔`main()` 內之敘述，`run_all` 不得單獨作為驗收依據〕
- 節奏：偵察（禁假設）→ plan → reviewer → 實作 → 量測 → push → 回報；plan 寫完即送 reviewer，不停等 KL；plan 不是交付物；自評之閘綠不能替代獨立復現。〔plan 完成即自動路由 reviewer〕〔🔒 自評 gate 綠不可替代獨立復現〕
## 六、施工單
- 施工單須自足：不得引用 code block 外之「本訊息／上文」；入倉之逐字內容全寫在 block 內。單內查無某物即照實回報請補，不得編造。〔施工單必須自足〕
- CC 收單第一工項：原封入倉 docs/orders/（不改一字、不改行尾），驗入倉 blob 之 sha256＝來源；不過即停，不續辦其餘工項。〔作業常規之追加四：**施工單之入倉**〕
- 入倉前先查單號占用（宣告框，見第九組），已占即停並回報，不得自行改號；發單側出單前亦須自查下一未占用號。〔之補款：**入倉前之號占用閘**〕
- 作廢單不刪：檔首前置標記列（作廢＋取代單號），原文不改；完整性驗為二合取：(i) 原文為新檔之嚴格後綴 (ii) 後綴依原口徑重算 SELF_SHA256 相符；後綴無 SELF_SHA256 者 loud 標「不可驗」。〔作廢標記之形 ＋ 完整性驗〕
- 收單機檢 S-0b：`python verify/probes/probe_order_preflight.py <單.md>`；P-3／P-5 為停機款，P-1／P-2／P-4／P-6 為提示（逐項採納或具名豁免）。〔### 🔧 二　收單時之機檢〕
- 施工單須含【驗收】段，由發單側撰，CC 不得代擬。〔（`W-G.9-225` 工項三 `c`〕
- 閘之受詞須由獨立於受測物者給定；受詞缺漏時 loud 拒測；「無從回測」不等於「回測不過」，出艙須載其義。〔閘之受詞⛔ 由受測方提供〕
- 逐字交付塊須由檔案管線直接抽取，三數與塊內文字出自同一次抽取；覆核用逐位 diff。〔**常規七（逐字交付塊之產生方式）**〕
- 撰寫施工單、規格或負向宣稱前，先 clone／pull 對現況。〔動筆前先對現況〕
## 七、證據與量測
- 數字一律錨引倉檔，禁憑記憶；與倉態衝突以倉為準。〔數字錨引倉檔**〕
- 【倉】＝現查之倉內值並附出處；【單】＝僅見於單或對話；來源不明預設【單】，【單】不得被下游引為事實。兩近似值相符不等於互證。〔`【倉】`／`【單】` 出處標注〕
- 命中數出艙須同格載三軸：來源 commit（blob@40 碼）／母體檔數或檔長／粒度框（字元、列、檔）。〔### 🔧 一　出艙命中數之〕
- 「命中 0」之斷言須同格報：所用之框（逐字）、命中數、對照組（必非零之近義詞）。〔**常規四（`W-G.9-NNN` 之取號與占用）**〕
- 判別力對照之判準＝命中逐筆歸類，不是命中數；母體不得扣除本單；命中非 0 而未逐筆歸類即停機。〔### 裁 `H`〕
- 閘之判準直接綁性質，不綁計數代理；通過條件不得內嵌未於同會期復現之數，改寫為「復算並回報實算值」。〔### 🔧 四　閘之通過條件〕
- 證據 grep 須正面列舉受檢檔，不得「全倉 grep 再 grep -v 排除」；多 -e 改用 BRE 交替。〔證據指令一律「正面列舉」〕
- 量倉之母體以 `git ls-tree -r <態>` 或 `git ls-files` 取得，不用 `grep -r .`。〔### 常規補款 `二`〕
- 探針在外部重建內部量，須以碼面既有之斷言作自我驗證閘並印出，不過不得下結論。〔探針還原內部幾何時，須以〕
- N/N 自證只證一致、不證正確；原始量須另備外部錨（獨立來源對拍、判別力對照、界限檢查）；幾何布林運算須顯式處理退化態。〔**常規八　`N/N` 之自證〕
- 修完後重看該閘之輸出數字，不以 rc=0 代替；patch／wrapper 附「咬到／退回」計數，計數為 0 先當作未生效。〔修完之後那個閘要再看一次〕
- 凡列合計，帶號合計 ΣX 與絕對值合計 Σ|X| 並列。〔凡列合計，帶號合計與絕對值合計〕
- 訂不變條件時，同時指明其守護之預測與該量於何處被讀；射程外之變動仍須記。〔不變條件之射程〕
- 「逐字節相同」以 diff 為據；位元組數須聲明量測框（工作樹或 blob）；指控他方前先確認量同一側。〔「逐字節相同」之宣稱一律以 `diff` 為據〕
- 以「倉內無痕跡」推「未發生」前，先問該事是否必然在倉內留痕；轉引含方向（箭頭）之記述須先確定其座標系。〔凡以「某物於倉內無痕跡」推「其未發生」者〕〔凡轉引含箭頭之記述者〕
- 新立之戒，次批須逐條自檢並列「已套用」；本倉之詞依本倉之定義，不依外部直覺（如「在 verify/ 下所以是測試」）。〔立戒者在下一批最容易違反自己的戒〕〔倉內本體論優先於外部常識〕
## 八、文件紀律
- append-only：CLAUDE.md、docs/rulings/**、.claude/skills/**、自誤登記表與基座已存在之 docs/reports/**，其 deletions 恆須為 0；以具名基座比對（不用 --cached），並以 verify/tools/wg942_append_audit.py 驗嚴格前綴。〔常規一 `②` 之補款③〕
- 更正一律末端追加；後節得宣告前節「不再適用」而不改前節；既出之數與既有標題形不追改。〔本標記之**體例依據**〕
- 活文件（CLAUDE.md、.claude/skills/、交接文）不得以行號為錨，一律用可 grep 之唯一字樣並附判別力自檢；不得作「某檔無某行」之否定存在主張。既有之失準行號只作引述。〔行號衛生（KL 2026-07-25 立）〕
- 不可變文件（批次報告、事前登記、交接文）不記可變檔之雜湊，雜湊記於該檔自身檔頭；中文檔名在 git --stat 會轉八進位跳脫，改以內容 grep 或 `git show --name-only -z`。〔不可變文件不得記載可變檔之雜湊〕〔中文檔名在 `git --stat`〕
- 本索引隨規則而動：凡施工單新增或取代常設規則者，同單須一併更新本索引之對應條，否則新規則不會進入 CC 開工時之 context。〔指令檔之載入改制〕
## 九、號之取號與占用
- 編號與倉內衝突時一律以倉內為準，新則取下一個未占用號，不得改編既有正典編號。〔編號衝突一律以倉內為準〕
- W-G.9-NNN 為發單側與 CC 共用之單一序；發出即占用（含未執行、已停機者）；CC 之報告用「單號＋R」，不另取號；CC 自行起事須先向發單側取最後單號。〔**常規四（`W-G.9-NNN` 之取號與占用）**〕
- 單號占用之判準＝宣告框：D1 檔名含號 ∪ D2 標題列含號（限所在檔之檔名之號＝該號）∪ D3 自稱形（列首即該號，嚴格式；或同列含「本單」且該號＝檔名之號）；皆帶數字邊界；母體＝全 docs/（倉側 blob）。〔號占用閘之框**改**宣告框〕〔宣告框 `D3` **自稱形之邊界**〕〔宣告框補款 `⑧`〕〔宣告框補款 `⑨`〕
- 計算式、引用、對照表、待辦清單之提及不構成占用；鬆框只作漏框偵察。出艙同格載 D1 檔數、D2 列數、D3 列數、雙屬列數、列框＝|D2∪D3|、檔框，及依 ⑨ 排除之 D2 列數。未決：作廢單現仍計入（同號重發之單過不了自己的閘），是否排除候發單側／KL。〔宣告框補款 `⑦`〕
- 各號類（自誤、GB、VR、戒、常規）求 MAX 一律用該類之定義列式並逐字列出；裸框只用於查意指占用；並扣「已作廢之人造受詞清單」，未扣／已扣二數並報。〔**常規四（八）　取號之現查〕〔`常規四（八）` 之補款〕
- 意指占用：號已被任何 payload（含未入倉之停機 payload、待鑄項、已發未執行之單）占用即為已占，順延並回報；框用錨定框 `(?<![0-9\-])<完整號>(?![0-9])`；B 形與 C 形並取，對照組全 0 之形不得單獨採信；零對照／判別力對照之出艙不構成占用。〔**常規四（七）　占用之受詞〕〔B 形於本倉為量測器紅〕〔### 🔧 二　**零對照〕
- 求 MAX 之母體＝該類登記表單檔（自誤：docs/reports/W-G.9波_claude.ai側自誤登記.md；GB：docs/reports/W-G.4_泛用阻塞項登記表.md；VR：docs/驗證裁定登記表.md）；查占用之母體＝全倉；鬆框只作漏框偵察，不得用於鑄號。〔### 🔧 一　`自誤` 之取號母體〕〔### 🔧 三　**鑄號母體唯一**〕
- 自誤之框＝定義框＋範圍框，舊寬形停用，缺號集取 [MIN..MAX]；定義框逐字見驗證裁定登記表 VR-091 四與其補款二（二者於倉內並用，使用前現查並載明所用之框）。〔寬形之**廢止標記**〕〔外：docs/驗證裁定登記表.md「`VR-091` 之補款二」「`VR-092`　缺號集」〕
- 新鑄之號：標題形取該類最末一則逐字為範本；收工閘證定義列式命中新號且 MAX 由 N−1 進為 N，不過即停。自誤：缺號永不重用，範圍形標題不再新增。〔**常規四（九）　新鑄之號〕〔### 🔧 二　`自誤` 之**定義框**〕
- 靜態清單之號係已鑄，不得列為缺號或重用：自誤 1–6、K-9-1、VR-1–13、戒 1–15 與 21–23；無編號之戒 9 則有拘束力但不占號。〔自誤簿首六則之靜態清單：〕〔簿內首則〕〔簿內低端〕〔### 🔧 類 ②〕〔類 ③ —— **無編號之戒**〕
- 非鑄號之補款／加註不得採號類之定義列式標題形（體例：🔧 起首）。〔`戒` 之定義列式〕
## 十、待落地清單
- 每輪結束前自問有無經驗收而未落地之結論，有則排入落地單；定期檢視 ⬜ 項並主動向 KL 報告清單與依賴序（KL 2026-08-24）。〔爾後你要記得〕
- 清單一律三態：✅ 已落地／🔶 部分落地（具名已落與未落）／⬜ 未落地；以「⬜ 全檔命中數」為量者須扣各節自載之自指增量。〔爾後之清單一律用本節之<u>三態</u>〕〔須自扣本節所增之量**（其量列於 `docs/reports/W-G.9-218R〕
- 提及 K-6-A2 者須同格載「已廢二項（K-9-5、K-9-5-2 ①⑤）／存續四項（K-9-1、K-9-3、K-9-6 宗地層 min_depth、K-9-8 之 GB-18）」，不得稱已結案。〔`K-6-A2` 之**部分廢止標記**〕
- 調配模組主鏈之現行清單與依賴序，以 `CLAUDE.md` 檔末最後一個「待落地清單之更新」節為準（`grep -n "待落地清單之更新" CLAUDE.md` 取末列）；但該系列節不重述「更正五」正本表之舊項（K-6-A2 存續四項、K-9-27／28 碼面、通用化波、序 9／11〜14 等），未經明文結案者仍為未落地。〔爾後之清單一律用本節之<u>三態</u>〕
- 九份 baseline 重產之時點由 KL 決；重產時須將 `指數名次` 自 verify/run_verification.py 之 `_DECLARED_EXTRAS` 移除。〔三　`_DECLARED_EXTRAS`〕
## 十一、執行環境
- `python verify/run_all.py` 為長跑（原載 15–20 分；W-G.9-364R 實測 1708／1958 秒）⇒ 背景跑並等通知，收尾 `exit $rc`；run_verification 會寫 CSV，兩支長跑不可併跑；pip 一律加 `--break-system-packages`。〔`python verify/run_all.py` 約〕
- run_all 會改寫已追蹤之 verify/out/probe_ruling_*.log 並新生 E系列實測快照 CSV ⇒ 一律於倉外之拋棄式 worktree 跑；單載其數須具名平台。〔`run_all` 之副作用〕
- 長跑期間不得修改 app.py 與 verify/ 下任何檔。〔長跑期間不得動受測物〕
- verify/out/ 禁 `git add -A`／`.`，一律逐檔 add；commit 前以 `git show --name-status`（或 `git status --porcelain`）對照異動清單；宣稱「應入庫而未入庫」前先讀 .gitignore。〔禁 `git add -A`／`.`（CC 立〕
- 含 emoji 之稽核工具在 cp950 主控台會 rc=1：先設 `PYTHONIOENCODING=utf-8`；rc≠0 先判量測器紅或受詞紅。〔**常規五（登記／稽核工具之編碼）**〕
- core.autocrlf 不得逕引；須當場分層（system／global／local）現查。KL 本機倉 local＝false；拋棄式 clone 未設 local 會繼承 system 之 true，工作區即為 CRLF。〔`core.autocrlf` 之**記述更正**〕
- heredoc：Bash 命令不得含 `<<`（PreToolUse hook verify/tools/wg9237_heredoc_guard.py 阻斷）；腳本一律以 Write 工具落檔再以路徑執行；hook 僅在 session 之專案目錄含 .claude/settings.json 與該腳本時生效。〔外：docs/reports/W-G.4_泛用阻塞項登記表.md「之補款：**硬閘化**」「補款之補款三」〕
- GB-198（⬜ 未修）：numpy ≥ 2.5 之 np.cross 拒收二維向量 ⇒ harness（verify/stepg_pipeline.py）中止；requirements.txt 無上界；登記之實跑以 numpy 2.4.6 為之；失效條件＝設上界 < 2.5 或改明式二維叉積。〔W-G.9-364`·〕〔外：docs/reports/W-G.4_泛用阻塞項登記表.md「### `GB-198` 🆕」〕
- 畫面執行環境之 WV_K6_STEP0／WV_K6B_STAGE3／WV_K929_6 須未設（設之即回舊行為）；主 checkout 同步後須重啟介面。〔W-G.9-358`·〕
- 生產與驗證讀同一份圖資，現行為 data/V6_1.dxf；data/V6.dxf 僅供溯源，不刪不覆蓋。〔外：docs/rulings/K-6_街角地分配程序與可分配判準.md「### 🔒 K-9-20　」〕
## 十二、讀起來像現行、其實已被取代（讀全文時注意）
- 「發單側⛔ 有倉之存取權」節之結論全部作廢〔發單側<u>有</u>倉之存取權〕；常規一四項於零生產碼側已不拘束〔「生產碼」之**機械界定**〕；B 形單獨使用不可信〔B 形於本倉為量測器紅〕。
- 自誤寬形停用〔寬形之**廢止標記**〕；占用母體改全 docs/、列框改聯集、D3 改嚴格式〔宣告框補款 `⑦`〕〔宣告框補款 `⑧`〕；「戒之次號仍為 40」已過時（戒 40 已鑄於 W-G.9-206 單，次號須現查）。
- 「core.autocrlf=true」「-text 僅涵蓋 *.dxf／*.dwg」已更正（.gitattributes 另含 *.cnt、*.lin、*.jpg）〔`core.autocrlf` 之**記述更正**〕；「verify/out/*.log 為 untracked」已不成立（大量 log 已入庫）。
- 「目前進度（2026-07-31）」之表與「更正二／更正三」清單之 ⬜ 字面 → 依「更正五」正本表及其後各節讀之；「技術環境」之 data/V6.dxf 與 `ezdxf.readfile(..., encoding="cp950")` → 驗證讀 data/V6_1.dxf，app.py 以 `_read_dxf_any_encoding` 依 big5／cp950／utf-8／latin-1 試讀。
- region_min「115.85 @ R4」→ 於 V6_1.dxf 為 115.88（碼面形）／115.885（正典形），候 GB-7 擇一〔外：docs/rulings/K-6_街角地分配程序與可分配判準.md「波末遷移項之更正」〕；「七級調配」與 wf_f0〜f4 分工 → W-F 凍存為史料，調配改依五級與新調配模組〔W-F（`verify/wf_f0.py`〜`wf_f4.py`）凍存為史料〕。
````

## 附錄丙　塊 `R2`（新檔 `.claude/rules/配地碼之領域指引.md`）

````markdown
---
paths:
  - "app.py"
  - "verify/**/*.py"
---

# 配地碼之領域指引（讀寫 app.py 或 verify/ 下之 Python 檔時載入）

動配地之碼以前，先讀下列原文；本檔只指出位置，不重述內容。

- 裁定正典：`docs/rulings/K-6_街角地分配程序與可分配判準.md`。街角規定範圍、可分配判準、街廓平均深度、最小分配面積、面積歸屬皆以此為準；同典之內，後節取代前節。
- `CLAUDE.md` 之領域核心各節（以 `grep -nF` 取其標題列再讀）：「CAD 圖層規範（v3.1 定稿」、「調配池兩階段（勿混淆）」、「v3 核心鐵律（每次施工都要遵守）」、「驗收對拍基準（」、「分頁權威序與歷史鍵名對照」、「§7 引擎接線鐵律」。
- 調配階段之流程與已停止適用之舊條款：`docs/specs/調配階段_泛用規格_v1.md`「已停止適用之條款」。
- 上列核心各節成文於 2026-07，其後已有更動，讀時留意：
  - 生產與驗證之圖資現為 `data/V6_1.dxf`（K-9-20）；`data/V6.dxf` 僅供溯源。
  - W-F（`verify/wf_f0.py`〜`wf_f4.py`）已凍存為史料，調配改依五級與新調配模組。
  - 其他已被取代之敘述見常設規則索引第十二組。
- 落地與否以碼為準，不以文書所載為準；文書與碼不符時照實回報，不自行擇一。
````

## 附錄丁　塊 `FX`（新檔 `.claude/skills/failure-archaeology-index/SKILL.md`）

````markdown
---
name: failure-archaeology-index
description: 診斷任何幾何/評分/守恆異常、審查別人（或自己）的修法、或發現「數字不對但不知為何」時必讀。本專案已付學費的系統性失敗模式，每條含症狀→根因→通則，防止重踩。（本技能為失敗考古之目錄；依標題擇則，再只讀該則之全文）
---

# 失敗考古之目錄

`failure-archaeology/SKILL.md` 共 124 則，全文約 4,800 行，自 `W-G.9-365` 起不自動叫用，以免一次載入全文。用法：

1. 依下列標題找出與眼前症狀相關之則（可多則）。
2. 讀該則：`grep -n "^## <則號>\. " .claude/skills/failure-archaeology/SKILL.md` 取其起列，以 Read 自該列讀至下一個 `## ` 標題為止。
3. 某則另有加註節（下列「加註節」）者，讀該則時以 `grep -n "節 <則號> 之"` 一併取之。
4. 該檔所載之 `檔名:行號` 錨多成文於 2026-08-22 以前，多已漂移，只作史料；現況以符號名與現碼為準。
5. 該檔自 2026-08-22 起未再增補；其後之失誤與教訓見 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 與 `docs/reports/W-G.4_泛用阻塞項登記表.md`。

## 目錄

- 1. 15m 框（W-D.1.3-b 修除）
- 2. 端點配對六塊全滅（-a 修除）
- 3. front_idx 假警報（-a 切換前排除）
- 4. 行號 ≠ 執行序
- 5. 解析期陳舊副本
- 6. 繞向擲硬幣（-c.1，本專案最貴的一課）
- 7. 單測全綠、整合翻船（-c.1 同案）
- 8. 容差過細漏量
- 9. 靜默歸零掩蓋事故（-a W1 與 -c.1 兩度）
- 10. 快取污染
- 11. UI session 殘留＝隱形變因（W-D.2 J-fix／R2 殘差雙案例）
- 12. 寫死時間參數＝靜默過期（no-silent-fallback 遠親）
- 13. 同名不同量（「最小分配面積」CLAUDE.md vs 域裁§五）
- 14. 刀口值不猜、進 REPL 驗（float round／banker's rounding）
- 15. 報表層分類器之輸入域 ≠ 引擎作用域（W-F 缺口D，最貴的一次「靜默 else」）
- 16. 圍欄比對粒度 < 引擎消費粒度（#11 家族新變體；W-G G.2 活抓）
- 17. 正面案例：no-silent-fallback loud 閘於生產路徑首次兌現（W-G G.1 live 停機）
- 18. plotly_events 點選判定綁 curveNumber-by-z＝脆弱（W-G GIS 步驟D跳位；KL localhost 活抓）
- 19. 同類 bug 藏多個獨立消費端·修一處後須全函式掃描（W-G GIS 區段點選第二破口；KL localhost 活抓）
- 20. 同機制病灶散在多檔·「找到就以為找齊」（W-G.4 S0b 定位·claude.ai 進倉抓漏）
- 21. 以殘餘定閘寬·「閘全綠」的效力上限＝閘寬依據強度（W-G.4 撞出·claude.ai 坐實·CC 自驗）
- 22. （保留·N0-17-c 否定存在斷言須附窮盡搜尋清單）
- 23. 「挾持」：多筆同分類候選＋取最後一筆 → 錯誤物件冒充錨標的（W-G.4 S0b／S0c 活抓·CC 自驗）
- 24. 「規格假設幾何精確·浮點說不」＋正典條文越過其落點適用（W-G.4 S0b/S0c·CC 自驗·五次現形）
- 25. 單點錨對「未被通式參數化之維度」零舉證力——**對的單點掩護錯的全域**（W-G.4 S1 plan·reviewer 活抓·KL 核可入正典）
- 26. 偏「令 ΣRw 閉合」之判讀三連錯——虛構法源／符號約定冒充物理／引廢註解（W-G.4 W脫鉤打樣·CC＋claude.ai 皆犯·KL 補丁八 §四拆穿）
- 27. 引倉內文件為據卻只讀證據表、未讀其裁決段——**證據表脫離裁決即失真**（誤J／誤M／誤N 同族·KL 立）
- 28. 配對計數當成配對正確性之證據——`baselines_matched_count` 4/4 全中卻 3 對 1 錯（W-G.5 裁定N 第二批·KL 立·**KL 交辦文以 `#38` 指涉本條**）
- 29. 用「當輪剛判定為致命」的判準去診斷該判準自身——端點重合法診斷端點重合法（W-G.5 C-6·claude.ai 犯·KL 立·**KL 交辦文以 `#41` 指涉本條**）
- 30. 以「會觸發的子集」之上界冒充「全體」之上界——據以宣稱閘寬有 40 倍餘量（W-G.5 E-1′·CC 犯·claude.ai 複驗活抓）
- 31. GEOS 於大地座標量級之精度損失被當成「資料本身的幾何殘差」（W-G.5 E-6·CC 誤診·reviewer 活抓·CC 復現後再修正）
- 32. 歸因連錯三次——每次都少做「只變一個變因」的對照（W-G.5 E-10·CC 犯三版·KL/claude.ai 兩度令改）
- 33. 縮寫使 regex 瞎掉——「窮盡清單」之窮盡性建立在一個漏了字的字集上（W-G.5 K-6-A1·CC 犯·claude.ai 覆核抓出）
- 34. 「改完零 diff」有兩種**完全相反**的解釋，而它們共用同一個觀測值（W-G.5 K-8 段二·CC 事前攔下）
- 35. 名目集合雙向 diff 為空，仍可有 22 項 PASS→FAIL（W-G.5 K-8 段二·連帶量測實證）
- 36. 跨 commit 引錨未重 grep ＋ 陳舊註解變成下一個人的錯誤前提（W-G.5 K-8 段二/段三·claude.ai 犯·CC 實測翻案）
- 37. 一個從未生效的 patch，其註解會取得與生效者相同的可信度（W-G.5 K-8 前置 C→E·claude.ai 追下游翻案）
- 38. 同一份施工單內，兩節對同一個碼面事實給出相反認定——限定詞在轉述時掉了（W-G.5 K-6-A2 段四(c)·claude.ai 犯·CC 動工前擋下）
- 39. 拿一個「已被自己覆蓋過」的檔案當對照組——差異是自己造成的（W-G.5 K-6-A2 段四(c) §0-1·claude.ai 犯·CC 實測翻案）
- 40. 於**非正交基底**上以內積取係數——方向沒選錯，錯在誤以為內積能取出分量（W-G.5 K-6-A2 段四(c)-2(a′)·claude.ai 施工單缺陷·CC 動工前擋下）
- 41. 驗收線與變更範圍自「規格層」直接落筆，未追碼面之產生鏈、精度與消費鏈（W-G.5 K-6-A2 段四(c)-2〜(c)·claude.ai **模式級**缺陷·CC／KL 逐一擋下）
- 42. 抄用**衍生表列**而未與同檔上方之**逐字法規原文**對讀受詞——並在下一輪把該錯誤**誤診為另一個錯誤**（W-G.5 K-6-A2 段五(a)〜(c)-0·claude.ai 犯·KL 圖示裁定翻案）
- 43. 偵察報告之母體以「有無幾何」為篩，未追早退閘之**真篩準** ⇒ 分母被稀釋（W-G.5 K-6-A2 段五·claude.ai 犯·次輪自查抓出）
- 44. 窮盡 grep 漏大小寫——據以宣稱「該函式不知 X 存在」（W-G.5 K-6-A2 段五·claude.ai 犯·次輪自查抓出）
- 45. 施工單指定之號規與極值**兩者皆反**——內積定號後恆負、`min` 挑到最深端點（W-G.5 K-6-A2 段五(a)·claude.ai 施工單缺陷·CC 動工前擋下）
- 46. 施工單指定了「算什麼」，未指定**座標框與號規** ⇒ 帶朝反方向長（W-G.5 K-6-A2 段五(a)·claude.ai 施工單缺陷·CC 動工前擋下）
- 47. 把**單一情形之圖示**升格為**全稱條款**，且未與同檔既有逐字紅線對讀 ⇒ 新條款與舊紅線互斥（W-G.5 K-6-A2 段五(c)-1·claude.ai 犯·**KL 活抓**）
- 48. 據自身容器之讀數斷定他方數字有誤——而二者只是**量測框**不同（working tree vs git blob）（W-G.5 K-6-A2 段五(c)-1〜(c)-2·**claude.ai 犯·CC 活抓**）
- 49. 「範圍」與「精度」之四個洞——同一批內 CC 與 claude.ai 各犯二則（W-G.5 K-6-A2 段六前置·KL 逐則活抓）
- 50. 節 40 之**再現**——同一個「非正交基底上以內積取係數」換了個變數名又寫一次（W-G.7 K-6-A2 S6-2-B·**CC 犯·自設之閘擋下**）
- 51. 施工單設下**正典早已裁過**之停機條件——落筆前未 grep 四處（W-G.7 GEO-1／S6-1 等·**claude.ai 犯·KL 活抓**）
- 52. 交付物落在施工單之**外**——連續兩批「待補件」，而執行者從未看見那段（W-G.8 D-0／D-0b·**claude.ai 犯·KL 活抓**）
- 53. 以**固定 regex** 代窮舉、以及**比錯基準向量**——同一族之兩個新實例（W-G.8 D-2b-6／-7·**claude.ai 與 CC 各犯一次**）
- 54. 施工單之六類失誤——最危險者係**編造精度**（W-G.8 D-2b-8〜-17·**claude.ai 犯·CC 現查抓出**）
- 55. 執行側之四類——**空真假綠**三例 ＋ 一則應仿效之處置（W-G.8 D-2b-8〜-17·**CC 犯**）
- 56. 以**壞掉的量測器**判定他人資料有誤，並據以**下令更正正確之物**（W-G.8 D-2b-18·**claude.ai 犯·CC 停機擋下**）
- 57. **假說之方向即為錯**——把「界線外之楔形」當成「被吃掉的自家面積」（W-G.8 D-2b-23·**claude.ai 犯·CC 現查抓出**）
- 58. **不變條件只點變數名、未點讀取位置**——射程界定不足（W-G.8 D-2b-23·**claude.ai 犯·CC 現查抓出**）
- 59. **在讀實作／查正典時序之前就先下結構性斷言**（W-G.8 D-2b-25·**claude.ai 犯·KL 域裁與 CC 現查各抓出一部分**）
- 60. **否定性結構宣稱，以射程小於命題之工具作成**（W-G.8 D-2b-29·**claude.ai 犯·同一 session 三例·皆自糾**）
- 61. **把 chat 側素材當作倉內事實，並據以要求 CC 更正**（W-G.8 D-2b-30·**claude.ai 犯·CC 現查抓出**）
- 62. **量測題目設在錯的構造上 ⇒ 交付一個不存在的取捨**（W-G.8 D-2b-31·**claude.ai 犯·<u>KL</u> 現查抓出**）
- 63. **出艙之數與寫進文件之指令，係<u>兩次不同的執行</u>**（W-G.9-1 §3-1·**claude.ai 犯·CC 現查抓出**）
- 64. **以「正典無此規定」停機，而只查了權威序<u>一級</u>、字樣又只寫一種**（W-G.9-2·**claude.ai 主責·CC 併責**）
- 65. **接了供給端就當接完了——「我只給 X 用」是<u>用途推定</u>，不是呼叫端現查**（W-G.9-4·**CC 犯·claude.ai 現查抓出**）
- 66. **「有閘」與「在守」之落差是<u>可量的</u>——量出來是 80／107**（W-G.9-6·**CC 量測·claude.ai 定式**）
- 67. **比較器之一端「不存在／為空」時，它仍會給你一個看起來有意義的答案**（W-G.9-6〜7·**CC 犯·CC 自查抓出**·**同一 session 三次**）
- 68. **工具回報「成功」而檔案未變——「已完成」與「已落地」是兩件事**（W-G.9-8·**CC 犯·CC 自查抓出**）
- 69. **壞掉的檢查器，吐出的正好是你期望的那個值**（W-G.9-9·**CC 犯·CC 自查抓出**）
- 70. **一個 `try` 把「要管線的」與「不要管線的」判定綁在一起——上游一崩，連不需要它的也陪葬**（W-G.9-10·**CC 拆解·claude.ai 定式**）
- 71. **把「我算不出這個命題」寫成「這個命題為偽」——一個 `except: return False` 就足以把技術故障變成送到 KL 面前的假域警報**（W-G.9-13·**CC 差點犯·CC 自查抓出**）
- 72. **以「量級差一個數量級」排除一個候選——而那兩個數<u>單位不同</u>**（W-G.9-14·**施工單方警告·CC 現查推翻**）
- 73. **一份<u>工作方式設定檔</u>差一點抽掉八批的驗證憑據——而它不會讓任何一道閘變紅**（W-G.9-14 後·**施工單方現查抓出**）
- 74. **判別實驗量的是「有沒有這個差」，而我把它記成「是<u>這個原因</u>造成的差」**（W-G.9-14·**CC 犯·CC 自查抓出**）
- 75. **拿一個沒查過的前提，換到了一個域裁——而免責標記一點作用都沒有**（W-G.9-14 後·**施工單方先犯·CC 承接·KL 實試撞牆**）
- 76. **套套邏輯之自我驗證閘——它不可能失敗，所以它什麼也沒驗**（W-G.9-16·**CC 犯·CC 自查抓出**）
- 77. **「受詞取錯一層」——我在<u>糾正這個形狀的同一批裡</u>，又犯了同一個形狀**（`W-G.9-19`〜`W-G.9-21`·**CC 犯·CC 自查抓出**）
- 78. **陽性對照組挑了一個「機制在那裡是平的」的值——於是它什麼也證明不了**（`W-G.9-23`·**CC 犯·CC 自查抓出**）
- 79. **判準把「對照組之預期碼」訂在<u>該工具結構上不可達</u>的地方——於是對照組什麼也證不了**（`W-G.9-25`·**施工單方犯·CC 現查抓出**）
- 80. **量測不可見字元時，跳脫寫錯不會報錯——它靜默回 `0`，而 `0` 正好是我想看到的那個答案**（`W-G.9-26`〜`W-G.9-27`·**施工單方犯·連續二次·自查抓出**）
- 81. **「逐字全文」區塊裡塞了一個「須現查之值」——一個說不容判斷、一個說必須判斷**（`W-G.9-29`·**施工單方犯·CC 現查抓出**）
- 82. **「查到」不等於「已占用」——前瞻引用會讓一個空號看起來像滿的**（`W-G.9-30`·**施工單方犯·CC 現查抓出**）
- 83. **一次無瑕的徹底列舉，證出了一個假的「做不到」——因為母體選錯了，而復現只會把同一個母體再走一遍**（`W-G.9-32`〜`W-G.9-34`·**claude.ai 犯·KL 追問後自查抓出**）
- 84. **以顯示精度下的「恰好相等」推出「其餘恰為零」——而同一份報告的另一段已經證明它們不是零**（`W-G.9-35`·**CC 犯·claude.ai 覆核抓出**）
- 85. **一個由構造保證為空的集合，被當成量測結果出艙——而它恰好是判準中唯一有資訊的那一半**（`W-G.9-37`·**CC 犯·claude.ai 讀原始碼抓出**）
- 86. **同義詞集之單字差——三個詞是同一次查詢的三份複本，而正典用的是第四個詞**（`W-G.9-42`／`W-G.9-43`·**claude.ai 犯·CC 承接·KL 抓出**）
- 87. **佐證之獨立性：`n` 份佐證若共用同一組查詢字樣／同一門檻之換算，則 `n = 1`**（`W-G.9-42`〜`W-G.9-44`·**claude.ai 與 CC 各犯一次·互相抓出**）
- 88. **跑過而誤報——輸出就在眼前，而出艙句與它相牴觸**（`W-G.9-43`·**claude.ai 犯·CC 逐行貼原始輸出抓出**）
- 89. **儀器之解析度與被測量同量級——「可行」只是把違反量吃進了容差**（`W-G.9-59`／`W-G.9-60`·**claude.ai 犯·倉內既有之見證家法抓出**）
- 90. **函式簽章沒變 ⇒ 誤以為契約沒變——改的是內部座標框，外洩的是回傳幾何**（`W-G.9-60`·**claude.ai 開單·CC 拒絕照辦並具名**）
- 91. **閘之受詞域由「被測缺陷之量」界定 ⇒ 該閘結構上不會紅**（`W-G.9-61`／`W-G.9-62`·**claude.ai 設計·claude.ai 以注入式變異自行測出**）
- 92. **`grep` 錨命中唯一 ≠ 該款仍有效；「不需上呈」之宣告從未被要求舉證**（`W-G.9-58`〜`-64`·**新窗 claude.ai 於三件前置中測出**·自誤 50）
- 93. **待裁項之受詞不是現況——「已被取代的條文／尚未存在的閘／另一種距離」**（`GB-80`〜`GB-84`·八批·**claude.ai 自測·四則自誤 50／52／54／55 之共同形狀**）
- 94. **施工單自身內含互不相容之二陳述，而<u>停機條件掛在錯的那一側</u>**（`W-G.9-67`·claude.ai 發·**CC 於先證紅時撞見並具名上呈**·自誤 56）
- 95. **靜默的部分覆蓋——工具「跑完了、沒報錯」，但它只看了一部分**（`W-G.9-69`·CC 二例 ＋ claude.ai 一例·同批三例）
- 96. **機制是對的，壞的是餵給它的字——「顯示形態」被當成「原始形態」凍存**（`W-G.9-70`·claude.ai 自誤 64·`GB-86`）
- 97. **量測器之修正必須<u>遞迴</u>施用——離譜的數字會自己求救，合理的數字不會**（`W-G.9-72`·CC 二戒 ＋ claude.ai 第三戒）
- 98. **偵測器之錯誤<u>方向</u>——往「多報」錯會吵，往「少報」錯會安靜**（`W-G.9-73`·**CC 自測**·`VR-031` 二）
- 99. **一份看起來嚴謹的普查，可以完全不回答原問題**（`W-G.9-74`·claude.ai 自誤 72·`VR-032` 二）
- 100. **同族之量測器彼此一致——證據力等同一支**（`W-G.9-76`·claude.ai 覆核測出·`VR-034` 二）
- 101. **抽象化⛔ 不等於窮舉——不全被往上挪了一層，而上一層更難看見**（`W-G.9-77`·claude.ai 自誤 77·CC 自行增補後具名）
- 102. **一個量可以「在表內、且看起來是零」——被<u>顯示格式</u>壓成零，於是表頭之計數與表身同頁矛盾而無人察覺**（`W-G.9-78`·claude.ai 覆核測出·`VR-036` 三-甲）
- 103. **「完全分離」⛔ 不等於「分得很開」——分離之<u>寬度</u>不出艙，`3 m` 與 `12 萬 m` 在報告上長得一模一樣**（`W-G.9-78`／`-79`·claude.ai 覆核測出·`VR-037` 二-甲）
- 104. **交辦之「明確」⛔ 不等於「可執行」——當它要求收單者去<u>代筆</u>不屬於他的內容**（`VR-037` §四·CC 於 `W-G.9-79b` §I-2 退回·claude.ai 自誤 80）
- 105. **工具已經把警語用中文印在同一頁上了，而讀的人在數行數**（`W-G.9-79` 覆核·CC 於 `W-G.9-80` §0-3 更正·claude.ai 自誤 81）
- 106. **「前提倒了」⛔ 不等於「就是它害的」——<u>失去支撐</u>與<u>已知成因</u>是兩件事**（`VR-039` 四·由 `W-G.9-81` A-3／A-5 推翻·claude.ai 自誤 83）
- 107. **「號」是一個獨立的受詞——帶號量之比較若未先固定號向，該式只在一半的情形成立**（`VR-039` 三-(a) ＋ `W-G.9-82` `P7`·claude.ai 自誤 84·**同一形連續二批**）
- 108. **「在宣告 X 之前必須先查」——而修法只寫了 X 的<u>一個值</u>**（節 92 修法 2 之射程更正·claude.ai 自誤 85·`VR-041` 五）
- 109. **用<u>自己造的詞</u>去搜別人寫的規範——搜尋規格若全部出自我方新造語，其判別力接近零**（`W-G.9-84` `A-4`·KL 於 2026-08-20 駁回·claude.ai 自誤 88）
- 110. **用「這條規矩<u>是為了什麼</u>」去讀「這條規矩<u>說了什麼</u>」——會讀出條文裡沒有的東西**（2026-08-20 呈 KL 之幾何示意·由 `W-G.9-87` 否證·claude.ai 自誤 91）
- 111. **讚揚一個對照物的<u>具體字樣</u>，等於毀掉它**——哨兵一旦入倉，就進了它自己要搜的乾草堆（`VR-050` 記功 5·由 `W-G.9-91` 機檢自捕·claude.ai 自誤 95）
- 112. **復發形：判準綁「代理」而非綁「性質」**——我寫下的條件，不是那個提醒真正要保證的事（`W-G.9-95Z` §Z-1·同形第三次·claude.ai 自誤 97）
- 113. **引述之真值源須可判**——讀者要能就地判定它是倉內錨，抑或只活在聊天／施工單（`W-G.9-95Z` §Z-2·二機制）
- 114. **`ast` 之 `col_offset` ＝ `utf-8` 位元組偏移**——與 `str.index()` 之字元索引混用即偏移，且只在該行含 CJK 時發作（`W-G.9-95Z` §Z-3·`-94` `A-4` 預宣自捕）
- 115. **複製既有量測：先逐位重現，⛔ 不在複製未對之前談差**（`W-G.9-95Z` §Z-4·claude.ai 自誤 98）
- 116. **「介面」之判準 ＝ 可執行下游 ≥ 1**——下游為 `0` ⇒ 它是報表、⛔ 不是介面（`W-G.9-95Z` §Z-5·`W-D.4 碎片遞補` 實例）
- 117. **出艙之自足性：「差為零」與「值等於 X」⛔ 非同一出艙**（`W-G.9-95Z` §Z-6·claude.ai 自誤 99）
- 118. **雙盲交接：⛔ 指標不足，須逐字帶出**——CC 有倉無決定權、發單側有決定權無倉（`W-G.9-95Z` §Z-7）
- 119. **略過須計數**——`略過 > 0` 而未具名 ⇒ 該量測⛔ 不成立（`W-G.9-95Z` §Z-8·`-95Z` 檢① 靜默吞 4 條）
- 120. **⛔ 不得以肉眼切 `grep -n` 之輸出**——`行號:內容` 於內容以數字起頭時視覺黏連（`W-G.9-95Z` §Z-9·`-95Zr` 同一格連錯二次）
- 121. **自誤之歸屬與真值源**——歸屬按「誰犯」，⛔ 非按誰寫入、誰捕獲、誰入倉（`W-G.9-95Z` §Z-10·claude.ai 自誤 100）
- 122. **宣告 `SELF` ⛔ 不等於扣除 `SELF`**——量測器須自母體扣除自身，且扣除數計入 `略過`（`W-G.9-97 補正②` §五-3·節 119 之補款②·CC 自誤）
- 123. **驗收之受詞⛔ 不得繫於「倉態」**——`HEAD`／`index`／`--cached` 隨入倉而變 ⇒ 檢入倉一次即失效（`W-G.9-97 補正②b`·CC 自捕 2 則 ＋ claude.ai 自誤 `105`）
- 124. **更正批是高風險批**——更正一個未證立之命題時，最容易植入另一個未證立之命題（二例·`W-G.9-97 補正②`／`W-G.9-98`）

## 加註節

- 🔧 節 85 之再犯實例加註（`W-G.9-41`·⛔ 上文原句一字未刪）
- 🔧 節 87 之**第三次**實例加註（`W-G.9-49`·⛔ 上文原句一字不刪）
- 🔧 節 87 之**第四／五次**實例加註（`W-G.9-53`·⛔ 上文原句一字不刪）
- 🔧 節 87 之**第六／七次**實例加註（`W-G.9-56`·⛔ 上文原句一字不刪）
- 🔧 節 88 之**第二次**實例加註（`W-G.9-56`·⛔ 上文原句一字不刪）
- 🔧 節 87 之**第八次**實例加註（`W-G.9-57`·⛔ 上文原句一字不刪）
- 🔧 節 88 之**未遂**實例加註（`W-G.9-57`·⛔ 上文原句一字不刪·⛔ 不與既遂並列計數）
- 🔧 CC 本批之**未遂**（`W-G.9-57`·⛔ 上文原句一字不刪）
- 🔧 節 87 之**第九次**實例加註（`W-G.9-58`·⛔ 上文原句一字不刪）
- 🔧 節 86 之**再一次**實例加註（`W-G.9-58`·⛔ 上文原句一字不刪）
- 🔧 節 87 之**第十次**實例加註（`W-G.9-59`·⛔ 上文原句一字不刪）
- 🔧 節 86 之**第三次**實例加註（`W-G.9-59`·⛔ 上文原句一字不刪）
- 🔧 節 87 之**第十一次**實例加註（`W-G.9-60`·⛔ 上文原句一字不刪）
- 🔧 節 91 之**第一次**實例加註（`W-G.9-62`／`W-G.9-63`·⛔ 上文原句一字不刪）
````

## 附錄戊　塊 `C1`（附於 `.claude/skills/g-formula-rules/SKILL.md` 之末）

````markdown

---

## 🔧 失準之更正（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

本節取代上文之對應敘述，上文原句只作史料。各點經發單側窗六十八於 `0e0edb3` 自倉實查。

- 上文「街角 G-gate 用估值」一條不再適用。真 G 由 `_corner_first_lot_G` 算，`_pk_one_side_v12(…, require_g_map=True)` 以側特定之真 G 驅動資格閘（裁定 M P-B／P-C：`334dfb4`／`de3ad2b`；真 G 之 fallback 改硬停：`9435bc2`）；`G估` 只作診斷欄。
- 上文「W-D.2 已知接線缺口」已修：`_forced_offset_map` 已賦值 `left/right_corner_min_area`（`f2dab43`，W-D.2 §3）。
- 上文「參數紀律」節之「已知缺口（修復屬 UI/接線波）」已修：法定最小寬改由 `f3_pk_legal_min_width` 供（依分區×正面路寬查表，缺值即報錯；`ca4985e`，S1 §6 查表化）。正面路寬另有輸入來源之殘題見 `GB-9`（`docs/reports/W-G.4_泛用阻塞項登記表.md`）。
- 上文「W-D 波次的預期輸出（不是 bug）」一節不再適用。停機與自解之現行規則見 `CLAUDE.md`「作業常規之追加五」與 `docs/reports/W-G.9波_恆常附款登記表.md`「試行期之停機款（CC）」：配地有任何施工單未載其期之改變，即停機上呈。
````

## 附錄己　塊 `C2`（附於 `.claude/skills/corner-selection-rules/SKILL.md` 之末）

````markdown

---

## 🔧 失準之更正（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

本節取代上文之對應敘述，上文原句只作史料。各點經發單側窗六十八於 `0e0edb3` 自倉實查。

- 本技能之說明與上文所稱之 `_build_corner_range_v2` 已刪除（`CLAUDE.md` 載「舊符號 `_build_corner_range_v2` **已刪除**」）。街角規定範圍之構造以 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 為準：K-8 §五 之「作廢」廢止上文之條帶構造，其後 `K-9-5-13` 改遠側界為 SIDELINE 平移 `S1`。現行之碼：(Ⅰ) `_build_corner_range_v3`，(Ⅱ) `_build_burden_range`。
- 上文「Winner 判定」第 2 點之「G估 ≥ 門檻」改為真 G：真 G 由 `_corner_first_lot_G` 算，`_pk_one_side_v12(…, require_g_map=True)` 驅動資格閘（見 `g-formula-rules` 末節）。E-1.7 之 1.0㎡ 絕對地板仍適用。
- 上文「Tiebreaker」之暫行實作與硬 hook 已落地：同分以重劃前原位次（`_pre_position_rank`）判之（`5d24519`）。
- 回歸錨：圖 8 golden（`tests/test_corner_priority_golden.py`）仍為每波必跑。上文之 UC9898 實座標錨（0.5741、0.2427、全覆蓋 1.0 整等）與截角面積表係舊基線之值；K-8 之範圍構造與 `data/V6_1.dxf`（`K-9-20`）已使引擎現值改變（例：R4 右截角於 V6_1 為 6.28，見 K-6 典）。九份基線之重產時點由 KL 決；重產前以 `verify/run_verification.py` 之現行期值與對帳名單為準，不以上文之舊數為期。
- 上文「第 3 條 vs M-5 ①」之停機已結：K-6 典載「K-4-3 整套街角救援作廢」（M-5 ①②③ 等），M-5 已歸檔於 `verify/archive/`；街角合併重試現依 K-6 §二 段三與 `K-9-48`（其落地狀態見 `CLAUDE.md` 之待落地清單）。上文之 `_fo_ends`、`ConsumedRegistry` 僅存於 `verify/archive/` 與註解。
- 上文「K-2(Ⅲ) 量測用虛擬範圍…不建」：其後 `K-9-8` 之 `k98_virtual_measure_block` 已實作；本條是否仍成立，以 K-6 典之 `K-9-8` 與現碼為準。
````

## 附錄庚　塊 `C3`（附於 `.claude/skills/cad-layer-semantics/SKILL.md` 之末）

````markdown

---

## 🔧 失準之更正（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

本節取代上文之對應敘述，上文原句只作史料。各點經發單側窗六十八於 `0e0edb3` 自倉實查。

- 上文「街角 side_mid ＝ SIDE 子段…之子段中點（非全線中點）」不再適用：補丁六（`docs/specs/W-G.4_規格v3補丁六_W正典_S1v3範圍.md`「W 正典」）定 mp ＝ SIDE_LINE 全段之中點，以之為準。
- 上文「現況 (Ⅰ)(Ⅱ) 共用 `_build_corner_range_v2`」已不成立：該符號已刪除；(Ⅰ) 為 `_build_corner_range_v3`，(Ⅱ) 為 `_build_burden_range`，二者不再共用（K-6 典 K-8 §五）。
- 上文「失敗考古 #38」：所指之教訓今在 `failure-archaeology` 第 28 則（該則之標題自載 `#38` 為其別稱）。
- 上文「本案實測角度（claude.ai 由 `data/V6.dxf` 坐實）」：生產與驗證之圖資現為 `data/V6_1.dxf`（`K-9-20`），V6_1 改動了 R1／R4 之 FRONT／SIDE 線；上列角度如需引用，須於 V6_1 重量。
````

## 附錄辛　塊 `C4`（附於 `.claude/skills/validation-runbook/SKILL.md` 之末）

````markdown

---

## 🔧 失準之更正（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

本節取代上文之對應敘述，上文原句只作史料。各點經發單側窗六十八於 `0e0edb3` 自倉實查。

- 驗收之判準：本分支為「准紅碼」，驗收＝與凍存之期望 FAIL 名單逐項相同（名目＋正規化原因；`verify/wv_reconcile.py` 於每次 `run_all` 對帳），不是全綠（`CLAUDE.md`「准紅碼」）。
- UC9898 oracle 中之街角範圍值（例「R5左 300.52／R2左 309.05／R3右 308.93」）與全覆蓋錨係 K-8 以前之值，已隨 K-8 之範圍構造與 `data/V6_1.dxf` 改變；不以上文之數為期，以現行 harness 之期值與對帳名單為準。
- 上文「現況清單」之「末端夾具 ×7」已過時：`verify/run_all.py` 現跑之夾具與探針較多，清單以 `verify/run_all.py` 之現碼為準。
- `run_all` 會改寫已追蹤之 `verify/out/probe_ruling_*.log` 並新生 E 系列實測快照 CSV，一律於倉外之拋棄式 worktree 跑（`CLAUDE.md`「`run_all` 之副作用」）。
````

## 附錄壬　塊 `C5`（附於 `.claude/skills/fixture-provenance/SKILL.md` 之末）

````markdown

---

## 🔧 失準之更正（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

- 上文「✅ 有出處」之示例值 `114.07`（R4 深度 `32.59`）係 N-19′ 以前之值，`CLAUDE.md` 已載勿再使用。示例只示範註記之寫法，不得作為現行期值引用；現行值以 K-6 典與 harness 之現行期值為準。
````

## 附錄癸　塊 `C6`（附於 `.claude/skills/README.md` 之末）

````markdown

---

## 🔧 現況之補記（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

- 技能現有十一項：上表十項，加 `failure-archaeology-index`（失敗考古之目錄）。
- 自 `W-G.9-365` 起，`failure-archaeology`（因其長）、`stop-conditions` 與 `wave-discipline`（因其過時）不自動叫用（`.claude/settings.json` 之 `skillOverrides`）；需要時以 `/` 選單手動叫用。失敗考古先讀其目錄；停機與流程之現行規則見 `.claude/rules/常設規則索引.md`。
- 「已知後續 hook」之前二項皆已落地：tiebreaker 改吃原位次（`5d24519`）；`left/right_corner_min_area` 已接線（`f2dab43`）。
- 各技能檔末之「失準之更正」節優先於其上文。
````

## 附錄子　塊 `C7`（附於 `.claude/skills/stop-conditions/SKILL.md` 之末）

````markdown

---

## 🔧 本技能已停止自動叫用（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

上文入倉於 2026-07-05，其「停機條件（僅此三種）」、「這些「不是 bug」（別誤停）」、「預先武裝的裁決規則（優先於裸停機）」與「例外邊界」皆已被取代，不得據以判斷。其中截角面積之裁決表亦已失準：R4 右截角於 `data/V6_1.dxf` 為 6.28（K-6 典 `K-9-20`），不是 6.25。現行之停機與自解規則：

- `CLAUDE.md`「作業常規之追加五」：CC 遇疑義時，自解須五項全滿足；黑名單五項恆停機——動任一宗地之 G／面積／街角歸屬／抵費地／配地幾何；動生產碼一字（含註解）；二讀法之土地後果相異；須新訂準據或廢止／放寬既有之閘；涉 KL 已裁之款而二讀法相斥。
- `docs/reports/W-G.9波_恆常附款登記表.md`「試行期之停機款（CC）」：量測器紅而須改量測器始能過、規格有歧義而涉域上判斷、配地有任一改變而單未載其期，皆停機。
- 各施工單之 `§零-2` 停機款。

索引見 `.claude/rules/常設規則索引.md` 第四組。
````

## 附錄丑　塊 `C8`（附於 `.claude/skills/wave-discipline/SKILL.md` 之末）

````markdown

---

## 🔧 本技能已停止自動叫用（`W-G.9-365`·2026-10-04·上文一字不刪·純末端追加）

上文入倉於 2026-07-05，其流程已被取代，不得據以施工。現行之流程：

- 施工單在 `docs/orders/`，由 CC 於第一工項原封入倉（`CLAUDE.md`「作業常規之追加四」）。上文所稱之 `*_細部plan.md` 最近一次改動在 2026-07-31，其後之施工皆以 `docs/orders/` 之單行之。
- 自 `W-G.9-359` 起以規格單流程為常態，CC 之唯讀獨立審查為常設步（`docs/reports/W-G.9波_恆常附款登記表.md`「期滿與續行」）。
- 零生產碼之 commit 逕行 push；生產碼之 commit 先推側分支、經復驗與 KL 放行（`CLAUDE.md`「「生產碼」之**機械界定**」與「`W-G.9-206` 補款　側分支復驗」）。
- 開工序：讀 `.claude/rules/常設規則索引.md` → 當前施工單 → 單所引之原文。

索引見 `.claude/rules/常設規則索引.md` 第二、三、五、六組。
````

## 附錄寅　塊 `AG`（`git apply` 於 `.claude/agents/redistribution-reviewer.md`（`git apply --numstat` ＝ `9`／`9`））

````diff
diff --git a/.claude/agents/redistribution-reviewer.md b/.claude/agents/redistribution-reviewer.md
index a2f6d14..db57d49 100644
--- a/.claude/agents/redistribution-reviewer.md
+++ b/.claude/agents/redistribution-reviewer.md
@@ -1,6 +1,6 @@
 ---
 name: redistribution-reviewer
-description: 市地重劃配地程式的「驗證導向」審查員。每次實作 diff 後、或計畫核可前主動呼叫。不採信實作者說詞，一律自己跑 grep / py_compile / 守恆算術，證明「宣稱的改動真的落地、沒破守恆、沒違反 CLAUDE.md 與當前波次 plan 的鎖定鐵則」。
+description: 市地重劃配地程式的「驗證導向」審查員。每次實作 diff 後、或計畫核可前主動呼叫。不採信實作者說詞，一律自己跑 grep / py_compile / 守恆算術，證明「宣稱的改動真的落地、沒破守恆、沒違反裁定正典、CLAUDE.md 與當前施工單的鎖定鐵則」。
 tools: Read, Grep, Glob, Bash
 model: opus
 ---
@@ -8,9 +8,9 @@ model: opus
 你是這個市地重劃配地專案的**獨立驗證審查員**。你只驗證、不改任何檔案。
 立場：吹毛求疵、不放水、**絕不採信實作者的口頭宣稱**——凡是「我已經改了 X」都要自己用 grep / 讀檔 / 算術證明。你的價值是把人類現在手動在做的驗證（grep、py_compile、守恆算術、actual-vs-planned）自動化，而不是記住規則。
 
-## 規則來源（唯一權威）
-- `CLAUDE.md` 與「當前波次的 `*_細部plan.md`」是鐵則的唯一權威。
-- 你的工作不是背規則，是**驗證這次改動有沒有違反它們**。改動與 CLAUDE.md / plan 衝突 → BLOCKED，並引出衝突的那一條。
+## 規則來源（權威序）
+- 裁定正典 `docs/rulings/K-6_街角地分配程序與可分配判準.md` → `CLAUDE.md` → 當前施工單（`docs/orders/`）。`CLAUDE.md` 不自動載入：先讀 `.claude/rules/常設規則索引.md`，再依其定位字樣以 grep 讀原文。`*_細部plan.md` 最近一次改動在 2026-07-31，已非現行之單。
+- 你的工作不是背規則，是**驗證這次改動有沒有違反它們**。改動與上列衝突 → BLOCKED，並引出衝突的那一條。
 
 ## 被呼叫時，依序執行（每步都要真的跑，把證據貼進報告）
 
@@ -30,18 +30,18 @@ model: opus
 - 各街廓：`ΣG_lot + Σ抵費地 = 街廓 DXF 面積`，差應 **< 1㎡**。若改動宣稱不動守恆，就用最新輸出/報表算一遍證明。
 - 檢查面積有無**重複計入**（例：公設地被算進建地又算進池）、四捨五入累積誤差、單位（㎡/公頃）與小數位是否全程一致。
 
-### 4. 比對當前波次 plan 的鎖定鐵則（讀 plan 逐項對；以 plan 實際條文為準）
+### 4. 比對當前施工單與裁定正典的鎖定鐵則（逐項對；以其實際條文為準）
 這些是「最容易默默算錯」的點，確認改動沒違反：
 - **方向**：一切方向以 `f3_cad_alloc_dir`（ALLOC_LINE）為基準；W = ⊥ALLOC；推進向 d_hat = FRONT_LINE；**不得**退回 MBR 長邊。
 - **兩個量別混**：單筆宗地寬度 `w_i`（判去留用）≠ W累積（只給 Rw 差額）。grep 確認判去留比的是 `w_i`、Rw 用的是累積。
-- **Rw**：差額式、`ΣRw_側 = R(末筆W) − R(起始W)`（forced 側起始W = buffer 寬）；法定 Rw 表（**W=4=37.8** 等）為常數，**不可改**。
+- **Rw**：差額式、`ΣRw_側 = R(末筆W) − R(起始W)`（起始 W 以現碼與 K-6 典為準：現碼以 `_adv_final['Wf_left']`／`_adv_final['Wf_right']` 供之，舊稿之「buffer 寬」已不適用）；法定 Rw 表（**W=4=37.8** 等）為常數，**不可改**。
 - **深度**：D_avg = FRONT 逐點對 BASELINE 的 ⊥ 垂距、長度加權均值；方法 B（面積÷寬）僅矩形捷徑。
-- **a 與波次邊界**：W-C 建地 a = `分攤登記面積_m2`，`面積_m2`(a') = 0；公設地補償（Tier 1 a_prime）、同歸戶合併、池消化、實際搬地一律延 W-E/W-F。**檢查改動有沒有把後波的事偷做進當前波**。
+- **範圍**：改動須在當前施工單之射程內；單未載其期之改動（尤其改變任一宗地之配地結果者）即 BLOCKED。舊波次（W-C〜W-F）之界線已不適用，同歸戶合併、公設地併入等為現行調配規格之工作；a 之來源以現碼與 K-6 典為準。
 - **設定值**：退縮、最小寬等為案/塊級參數，**不得**靜默 fallback 代換；防 `or 3.5` 把合法的 0 值吃掉。
 
 ## 回報格式
 逐項給**嚴重度 + 檔名:行號 + 你實際跑的證據（grep / 算術結果）**：
-- **BLOCKED**：會算錯、破守恆、違反 CLAUDE.md/plan 鐵則，或**宣稱改了但 grep 證明沒改**。
+- **BLOCKED**：會算錯、破守恆、違反裁定正典／CLAUDE.md／當前施工單之鐵則，或**宣稱改了但 grep 證明沒改**。
 - **WARNING**：高風險、邊界條件可疑、未驗證的假設。
 - **NOTE**：可改善、不擋。
 
@@ -51,6 +51,6 @@ model: opus
 ## 你做不到的（誠實邊界，交回人類 + claude.ai，勿假裝有定論）
 你與實作者是**同一模型、共享同一套盲區**。下列**判斷層**問題標 WARNING、交回人類裁示，不要自己拍板：
 - 「這是 bug 還是預期的中間態？」
-- 「這個調配/補償該在哪個波次做？」
+- 「這個調配/補償是否在本單射程內？」
 - 法規本意、附件二公式選擇、跨波架構取捨。
 這些靠法規條文 + 領域專家（KL）+ claude.ai，不是同模型的 reviewer 能獨力定的。
````

## 附錄卯　塊 `AM`（`git apply` 於 `AGENTS.md`（`git apply --numstat` ＝ `3`／`3`））

````diff
diff --git a/AGENTS.md b/AGENTS.md
index 35e7b6a..b391792 100644
--- a/AGENTS.md
+++ b/AGENTS.md
@@ -8,7 +8,7 @@
 
 | 序 | 檔案 | 內容 |
 |---|---|---|
-| 1 | **`docs/rulings/K-6_街角地分配程序與可分配判準.md`** | **裁定正典**（K-6／~~K-7~~／K-8 §一〜§五-2／**K-9 §一〜§五**）。⚠️ **K-7 已於 2026-08-01 整條撤銷·由 K-9 取代**（原文存查於該檔考古段） |
+| 1 | **`docs/rulings/K-6_街角地分配程序與可分配判準.md`** | **裁定正典**（K-6／~~K-7~~／K-8 §一〜§五-2／**K-9 各則**）。⚠️ **K-7 已於 2026-08-01 整條撤銷·由 K-9 取代**（原文存查於該檔考古段） |
 | 2 | **`CLAUDE.md`** | 專案總則、工作紀律、核心鐵律、目前進度 |
 | 3 | `.claude/skills/` | 常駐技能規則（驗證流程／失敗考古／停機條件／禁靜默兜底 等） |
 | 4 | `docs/配地計算總規格_v3.md` | 完整規格（部分章節已由裁定正典取代，見其檔頭註記） |
@@ -36,8 +36,8 @@
 - **🔒 行號是易腐資產**：引用他處一律用**符號名 ＋ 可自癒 grep 指令**；
   非用行號不可者，同列記下該行號成立之 commit。
 - **🔒 禁靜默兜底**：缺值一律 loud raise 或警示，不得以案件值（如 `or 3.5`）編造。
-- **🔒 只有真觸及域邊界**（法規解釋、土地分配後果、面積歸屬）**才停機上呈**；
-  純技術項一路 plan → reviewer → 實作 → 量測 → push 做完，不要回問。
+- **🔒 停機與自解**：CC 遇疑義時依 `CLAUDE.md`「作業常規之追加五」——五項全滿足方得自解；黑名單五項恆停機上呈
+  （動任一宗地之 G／面積／街角歸屬／抵費地／配地幾何、動生產碼一字含註解、二讀法之土地後果相異、須新訂準據或廢止／放寬既有之閘、涉 KL 已裁之款而二讀法相斥）。
 - **🔒 倉內報告＝唯一本體**：報告本體寫 `docs/reports/W-*.md` 並 commit；聊天僅為 ping。
 
 ## 三方分工
````

## 附錄辰　塊 `P19`（附於 `CLAUDE.md` 之末（工項二））

````markdown

## 🔧 指令檔之載入改制（`W-G.9-365`·KL `2026-10-04` 令·⛔ 上文一字不刪·純末端追加）

1. **緣由**（KL `2026-10-04 06:08` 逐字：「因現在我會常駐Opus 5.5 模型，所以參考prompt-audit 第 1、2 項指出：`CLAUDE.md `約 87% 是舊紀錄，行號錨已失效...協助修改相關檔案以匹配最新 Opus5.5 模型」）：本檔約 `3,500` 列、`334` KB，每個 CC 工作階段皆全文載入；CC 之施工樹在主 checkout 之下（例：`W-G.9-364R` 所載之 `.claude/worktrees/…`）時，主 checkout 之本檔亦作為上層目錄之檔一併載入。其中多數為已被後節取代之紀錄，新舊條文並陳而互相牴觸。
2. **改制**：本檔與 `AGENTS.md` 自本批起不再自動載入（`.claude/settings.json` 之 `claudeMdExcludes`：`**/CLAUDE.md`、`**/AGENTS.md`）。此二樣式比對絕對路徑，故於本專案之工作階段，使用者層級之 `~/.claude/CLAUDE.md`（若日後建立）亦不載入。本檔仍為規則之全文與紀錄簿，照舊只作末端追加；其現行規則之索引在 `.claude/rules/常設規則索引.md`（自動載入），配地碼之領域指引在 `.claude/rules/配地碼之領域指引.md`（讀寫 `app.py`、`verify/` 之 Python 檔時載入）。
3. **索引之維護**：索引之更動須經施工單；凡施工單新增或取代常設規則者，同單須一併更新索引之對應條，否則新規則不會進入 CC 開工時之 context。索引之每個〔字樣〕須恰命中本檔一列；其檢查器與失敗考古之目錄之重生成器見 `docs/orders/W-G.9-365_輕量單.md` 之附錄午（塊 `CK`）與附錄巳（塊 `GF`），日後之單於本檔末端追加後須重跑之。
4. **技能**：`failure-archaeology`（因其長）、`stop-conditions` 與 `wave-discipline`（因其過時）不自動叫用（`skillOverrides`·`user-invocable-only`），需要時以 `/` 選單手動叫用；新增 `failure-archaeology-index`（失敗考古之目錄）；七技能檔與 `README.md` 之失準處見各檔末之「失準之更正」「現況之補記」或「本技能已停止自動叫用」節；審查代理 `.claude/agents/redistribution-reviewer.md` 與 `AGENTS.md` 之過時處已逐處更正（二檔不在 `常規一 ②` 補款③ (2) 之正典檔之列）。
5. **驗收**：KL 於新開之 CC 工作階段以 `/context` 核對其記憶檔之列：不含本檔與 `AGENTS.md`，而含 `.claude/rules/常設規則索引.md`。若本檔仍在其列（例：`claudeMdExcludes` 之樣式於該平台未命中），則本改制未生效，以施工單另處，不得自行改設定。
````

## 附錄巳　塊 `GF`（倉外 `<O>\gen_fa_index.py`（⛔ 入倉·塊 `FX` 之重生成器））

````python
#!/usr/bin/env python3
"""自 .claude/skills/failure-archaeology/SKILL.md 機械生成其目錄技能（W-G.9-365 塊 FX）。
用法：python gen_fa_index.py <repo> <輸出檔>
生成式：圍欄外之 `## N. 標題` 依序逐列為 `- N. 標題`；圍欄外之 `## 🔧 …` 依序逐列為 `- 🔧 …`。"""
import re, sys
repo, out = sys.argv[1], sys.argv[2]
src = open(f"{repo}/.claude/skills/failure-archaeology/SKILL.md", encoding="utf-8").read()
fm = re.match(r"---\n(.*?)\n---\n", src, re.S).group(1)
desc = re.search(r"^description: (.*)$", fm, re.M).group(1)
entries, addenda, fence = [], [], False
for line in src.split("\n"):
    if line.startswith("```"):
        fence = not fence
        continue
    if fence:
        continue
    m = re.match(r"^## (\d+)\. (.*)$", line)
    if m:
        entries.append((int(m.group(1)), m.group(2).rstrip()))
    elif line.startswith("## 🔧 "):
        addenda.append(line[3:].rstrip())
nums = [n for n, _ in entries]
assert nums == list(range(1, len(nums) + 1)), "則號非自 1 起連續"
body = [
    "---",
    "name: failure-archaeology-index",
    f"description: {desc}（本技能為失敗考古之目錄；依標題擇則，再只讀該則之全文）",
    "---",
    "",
    "# 失敗考古之目錄",
    "",
    f"`failure-archaeology/SKILL.md` 共 {len(entries)} 則，全文約 4,800 行，自 `W-G.9-365` 起不自動叫用，以免一次載入全文。用法：",
    "",
    "1. 依下列標題找出與眼前症狀相關之則（可多則）。",
    "2. 讀該則：`grep -n \"^## <則號>\\. \" .claude/skills/failure-archaeology/SKILL.md` 取其起列，以 Read 自該列讀至下一個 `## ` 標題為止。",
    "3. 某則另有加註節（下列「加註節」）者，讀該則時以 `grep -n \"節 <則號> 之\"` 一併取之。",
    "4. 該檔所載之 `檔名:行號` 錨多成文於 2026-08-22 以前，多已漂移，只作史料；現況以符號名與現碼為準。",
    "5. 該檔自 2026-08-22 起未再增補；其後之失誤與教訓見 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 與 `docs/reports/W-G.4_泛用阻塞項登記表.md`。",
    "",
    "## 目錄",
    "",
]
body += [f"- {n}. {t}" for n, t in entries]
body += ["", "## 加註節", ""]
body += [f"- {a}" for a in addenda]
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(body) + "\n")
print(f"則 {len(entries)}；加註節 {len(addenda)}；列 {len(body)}")
````

## 附錄午　塊 `CK`（倉外 `<O>\checkidx.py`（⛔ 入倉·索引之定位字樣檢））

````python
#!/usr/bin/env python3
"""常設規則索引之定位字樣檢：每個〔字樣〕須恰命中 CLAUDE.md 一列；「外：檔「字樣」」須其檔存在且字樣恰命中該檔一列以上。
用法：python checkidx.py <repo> <索引檔>"""
import os, re, sys
repo, idx = sys.argv[1], sys.argv[2]
src = open(os.path.join(repo, "CLAUDE.md"), encoding="utf-8").read().splitlines()
lines = open(idx, encoding="utf-8").read().splitlines()
bad = n_in = n_ext = 0
for n, l in enumerate(lines, 1):
    for key in re.findall(r"〔([^〕]+)〕", l):
        if key.startswith("外："):
            n_ext += 1
            m = re.match(r"外：(\S+?\.md)(.*)", key)
            if not m:
                bad += 1; print(f"L{n} 外之形不明: {key!r}"); continue
            path = m.group(1)
            if not os.path.exists(os.path.join(repo, path)):
                bad += 1; print(f"L{n} 外檔不存在: {path}")
                continue
            body = open(os.path.join(repo, path), encoding="utf-8").read().splitlines()
            for q in re.findall(r"「([^」]+)」", m.group(2)):
                c = sum(1 for x in body if q in x)
                if c < 1:
                    bad += 1; print(f"L{n} 外檔字樣無命中: {path} {q!r}")
            continue
        n_in += 1
        c = sum(1 for x in src if key in x)
        if c != 1:
            bad += 1; print(f"L{n} 命中列數={c}: {key!r}")
print(f"索引列數 {len(lines)}；內部字樣 {n_in}；外部指標 {n_ext}；不合 {bad}")
sys.exit(1 if bad else 0)
````

SELF_SHA256: 824fc8852ccad28ea460f5eb2b0e6bfe571b63eb6ff8f95f5d9bb2e308810ffc
