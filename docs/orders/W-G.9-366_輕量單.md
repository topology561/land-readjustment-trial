# `W-G.9-366`　輕量單：開工自動對齊（桌面版新建之工作區落後主線時，開工即自動快轉並提示重讀常設規則索引）＋ 主 checkout 之同步 ＋ KL 本機使用者設定之掛載 ⛔ 零生產碼

> **本單建議等級 ＝ `medium`**（本單⛔ 令 CC 撰碼；受詞 ＝ 新器 `verify/tools/wg9366_session_sync.py`、常設規則索引之一列、`CLAUDE.md` 之末端追加、主 checkout 之同步、KL 本機使用者設定之一項）。
> **發單** ＝ 發單側窗六十八·`2026-10-04`。**受單** ＝ CC 新窗（工項零〜三於 **CC 之施工樹**；工項四於 **KL 之主 checkout**；工項五於 **KL 本機之使用者設定**與一個自建自刪之探針工作區）。
> **級** ＝ **輕**（零生產碼；⛔ 動生產碼 `34` 檔與任何宗地之配地；⛔ 跑 `run_verification.py`／`run_all`。`verify/` 之動唯新增 `verify/tools/wg9366_session_sync.py`〔⛔ 屬生產碼 `34` 檔〕；其驗為器之自驗與機械之逐位對拍。KL 之放行見 `§二`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `3c0c59c078e13e12a06df31576741f537c5dc8a6`（`W-G.9-365` 工項三）；遠端 heads `35`；KL 之主 checkout 於 `wip/s1-endpart` ＝ `3c0c59c…`（`W-G.9-365` 工項四）。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`。塊 `SS`／`IX`／`P20`／`US` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（抽取式見 `§五-1` 末）；塊 `CK`／`GF` 以同一抽取式自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳取出（`CLAUDE.md`「指令檔之載入改制」節項 `3`）。`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**。`<O>` ＝ CC 自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-366_輕量單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。本批之一切改動皆自本單之塊抽出。
> 🛑 **本單⛔ 及於**：生產碼 `34` 檔之一字；`verify/` 除新檔 `verify/tools/wg9366_session_sync.py` 外之一字；`docs/` 下除本單與報告二新檔外之一字；`CLAUDE.md` 除塊 `P20` 之純末端追加外之一字；`.claude/` 除常設規則索引之一列（塊 `IX`）外之一字（`.claude/settings.json` ⛔ 動）；KL 本機之使用者設定除 `hooks.SessionStart` 之一項外之一字；任何側支之推送、刪除或改寫；任何既有之工作區與分支（工項五自建自刪之探針工作區與其分支除外）。
> 🔴 **本單⛔ 令 CC 判「孰為正典」**；塊之文字 CC ⛔ 改一字——CC 認為塊之文字有誤者，照實回報（停機款 `9`）。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量（於對話出艙）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `3c0c59c078e13e12a06df31576741f537c5dc8a6`；`git ls-remote --heads origin` 之列數 ＝ `35`（全 `35` 列存 `<O>\heads_before.txt`·收工閘 `6` 用）；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 577 566` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `562`／`MAX` `577`、`GB` `194`／`201`、`VR` `80`／`95`、`K-9` `52`／`55`（＝ `W-G.9-365` 收工閘 `7`）。
4. 本單之 bytes／`sha256` 對拍 KL 所貼之訊；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載 bytes／`sha256` 或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。
5. **放行**：KL 貼本單之同一訊息須逐字答問一「是」（`§二`）；未答或答「否」⇒ 停機款 `11`。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態 `3c0c59c` 之 `docs/` 全檔 **`966`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗六十八實跑 `python verify/probes/wg9268_gate6_occupancy.py 3c0c59c W-G.9-366 W-G.9-365 W-G.9-396`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-366`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-365` | `2`／`12`／`6` | `2`／`12`／`6` | `18` | `2` | `2`／`34` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `18`／`28` | 🟢 宣告框 `0`、鬆框非零（器之標籤「甲（須 ≥1）」依本表之角色讀之·同 `W-G.9-365R` ⑥ 自解 `1`） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `29`／`32` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

本批⛔ 鑄自誤／`GB`／`VR`／`K-9` 之號；收工閘 `7` 以四簿之值不變驗之。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `3c0c59c`，或施工樹之追蹤檔有變動，或遠端 heads ≠ `35`，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes 與本單不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 任一塊之 bytes／`sha256`／列數與 `§五-1` 不符；或 `git apply --check` 不過；或施後之 blob ≠ `§五-1` 項 `8` |
| `4` | `CLAUDE.md` 之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 塊 `P20`；常設規則索引之 `git apply --numstat` ≠ `1`／`0` |
| `5` | 工項一、二之驗任一 ≠ 期（器之 `--selftest`／`--selftest-mutant`／`--cwd`；`checkidx` 之必紅與必綠；`gen_fa_index` 之重生成） |
| `6` | `§四` 收工閘任一 ≠ 期 |
| `7` | 任一 `push` 之目標非 `wip/s1-endpart`，或被拒，或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項四：主 checkout 之追蹤檔有變動；其 `HEAD` ≠ `3c0c59c…` 或其分支 ≠ `wip/s1-endpart`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過；或 CC 認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `10` | 本批任一新檔為 `git check-ignore` 所命中 |
| `11` | KL 貼本單之同一訊息未逐字答問一「是」 |
| `12` | 工項五：主 checkout 之路徑 ≠ 期；使用者家目錄 ≠ 期，或環境變數 `CLAUDE_CONFIG_DIR` 已設；塊 `US` 之器 `rc` ≠ `0`、其所增之項或自驗二／三 ≠ 期，或使用者設定之寫入被拒（照實回報其訊息·⛔ 改他法寫入）；探針之任一出艙 ≠ 期；探針工作區或其分支之移除失敗（⛔ `--force`·照實回報） |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `10`。

---

## `§一`　態錨（發單側窗六十八自倉實取·本機 Linux·倉外工作樹）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `wip/s1-endpart` ＝ `3c0c59c078e13e12a06df31576741f537c5dc8a6`；遠端 heads **`35`**（`verify/` `30`·`wip/` `3`·`claude/` `1`·`main` `1`）；`main` ＝ `6cb77b7`（遠端之預設分支） |
| `2` | `W-G.9-365` 之復驗（發單側窗六十八） | 四 `commit`（`9727c37`／`2b210b1`／`e1cc2cb`／`3c0c59c`）之訊息首列 ＝ 該單所令逐字；該單 `§五-1` 項 `19` 之 `15` 檔之 blob 逐檔相符；生產碼 `34` 檔與 `verify/` 對 `0e0edb3` 相異 `0`；`docs/` 相異恰 `2`（`A`：該單、其報告）；heads `35`——**全數相符**。KL 於新開之工作階段以 `/context` 核對：記憶檔 ＝ `.claude/rules/常設規則索引.md`（約 `11k`）＋ `MEMORY.md`（約 `7.7k`），不含 `CLAUDE.md` 與 `AGENTS.md` ⇒ 該單之改制生效 |
| `3` | 事證（KL 所貼·`2026-10-04`） | ① 工作階段 `claude/context-799757`：`git log -1` ＝ `0e0edb3`、無 `.claude\rules` 目錄；以 `git merge --ff-only origin/wip/s1-endpart`（`0e0edb3..3c0c59c`）快轉並 `/clear` 後，記憶檔含常設規則索引。② KL 依發單側之議於桌面版選分支 `wip/s1-endpart`（勾 worktree）另開：工作區 `claude/context-770073` 之 `HEAD` ＝ `0e0edb3`，而本機與遠端之 `wip/s1-endpart` 皆 ＝ `3c0c59c`；`git worktree list` 之首列 ＝ 主 checkout `C:/Users/admin/Desktop/land-readjustment-trial` 於 `3c0c59c [wip/s1-endpart]`。③ 二次建於 `0e0edb3` 之工作階段，KL 以 `/context` 所見之記憶檔皆唯 `MEMORY.md`（約 `7.7k`）——舊版之 `CLAUDE.md` 未載入，所缺者唯常設規則索引；快轉並 `/clear` 後 ＝ 常設規則索引（約 `11k`）＋ `MEMORY.md`（舊版工作區之專案設定無 `claudeMdExcludes` 而 `CLAUDE.md` 仍未載入，其故【未證】）。⇒ 桌面版建工作區所據之版本，既非主 checkout 之 `HEAD`、亦非遠端主線之端、亦非遠端之預設分支（`6cb77b7`）——本倉之檔與 git 之設定皆無從左右（發單側推測為桌面版自身所記之舊版本·【未證】） |
| `4` | 機制（Claude Code 之文件·發單側窗六十八查） | SessionStart hook 於工作階段開始時執行，其 matcher 依來源分 `startup`／`resume`／`clear`／`compact`（另有 `fork`），以豎線列舉；hook 之 stdin 為 JSON，含 `cwd`（工作階段之目錄）與 `source`；`exit 0` 時 stdout 之文字加入 Claude 之 context；非零之結束碼⛔ 擋開工；`timeout` 之單位為秒；Windows 下 command 以 Git Bash 執行（無則 PowerShell）；使用者設定（`~/.claude/settings.json`）施於一切專案之一切工作階段，其修改通常由檔案監看即時生效；context 壓縮（compact）後，專案根之 `CLAUDE.md` 與無 `paths` 之 rules 自磁碟重新注入，以 Read 讀入之內容則隨對話摘要；專案之 `.claude/settings.json` 自工作階段之目錄讀取 ⇒ 建於舊版本之工作區讀到的是舊版之專案設定（本批若改專案設定，正是需要它的那些工作區讀不到） |
| `5` | 本批之受詞之開工態（`git rev-parse 3c0c59c:<檔>`·bytes） | `.claude/rules/常設規則索引.md` `ee0685a144f62ffcc9e0c8ab0eafb3ef946f4b5a`（`24624` B）；`CLAUDE.md` `b85cd9c20801be24faa3e1a9a88e3be9b9bb50ea`（`336749` B）；`.claude/settings.json` `4e33f016f12c07eb56dc93d49daab0445a33899b`（`503` B·本批⛔ 動）；`verify/tools/wg9366_session_sync.py` ＝ 無；`app.py` `176f90c96f6c13ede5c0c4e2425bebbbe827bf51`；皆以換行結尾·CR `0` |
| `6` | 器之設計（塊 `SS`） | **開工**（`startup`／`clear`）時，工作區合於下列**全部**者，以 `git merge --ff-only` 快轉至 `origin/wip/s1-endpart`（先 `git fetch origin wip/s1-endpart`·限時 `20` 秒·其輸出⛔ 經管線·連不上則以本機之遠端追蹤 ref 為準；自開始逾 `40` 秒則⛔ 快轉），並出通知（含「請先以 Read 讀常設規則索引」）：遠端 `origin` 之網址以 `land-readjustment-trial`（或其 `.git`）結尾；為 linked worktree（主 checkout 之 `.git` 為目錄 ⇒ 不動）；分支名以 `claude/` 起首（detached、他分支 ⇒ 不動）；追蹤檔無變動；`HEAD` 為主線之端之祖先而不等於之；主線所新增之檔於工作區皆不存在、其上層路徑亦非檔（git 快轉時會逕行覆蓋或移除被忽略之檔 ⇒ 先擋）。本器之 git 呼叫皆關閉自動 gc（`gc.auto=0`、`maintenance.auto=false`）。落後而不合後三者，只出通知、不動；不落後者（含只超前者）無聲。快轉而常設規則索引於開工時係舊版或缺者，於該工作區之 git 管理目錄（`.git/worktrees/<名>/`）記狀態檔 `wg9366_state` ＝ `stale`；**壓縮**（`compact`）時見 `stale` 則再提醒（「若 context 中未見索引之全文，請再以 Read 讀之」）；其後之 `startup`／`clear` 改記 `fresh`（規則已自磁碟重新載入）。壓縮之提醒與 `fresh` 之改記只依前二條件（工作區於開工快轉後轉為 detached〔各單之開場即如此〕者仍適用）；狀態係逐工作區、⛔ 逐工作階段。`resume`、`fork` ⇒ 不動。⛔ push、⛔ 動他分支、⛔ 刪檔；一切例外皆 `rc 0`（照實出艙其訊息）。自驗 `T1`〜`T14`（含 `T10a`）於系統暫存目錄自建 git 倉為之（⛔ 觸及本倉·⛔ 連網） |

---

## `§二`　KL 之語與射程

KL `2026-10-04`（逐字）：「桌面版新開的工作區可能停在舊版本,要如何徹底解決這件事，不然每次都要 快轉到 `origin/wip/s1-endpart`，再 `/clear`...對程式新手不友善」；「所以以後我CC開新窗，我的main 要選哪一個?」；「剛開新CC窗 wip/s1-endpart 反而memory.file 無法展開」；「擬366單」。

- 發單側先後所議之二法皆不足：① 設定 `worktree.baseRef`（Claude Code 新建工作區之基準：`fresh` ＝ 遠端之預設分支、`head` ＝ 本機之 `HEAD`）——本案之舊版本二者皆非（`§一` 項 `3`）⇒ 撤回；② 開窗時選分支 `wip/s1-endpart`——實測仍建於 `0e0edb3`（`§一` 項 `3` ②）。⇒ ⛔ 倚賴桌面版之建法，改於**開工之時**對齊。
- hook 掛於**使用者設定**而⛔ 掛於專案設定之由 ＝ `§一` 項 `4` 末句；其所指之器以**絕對路徑**指向主 checkout，故主 checkout 須恆為最新（各單收尾之同步·本單工項四）。
- 快轉只施於「桌面版新建、無任何變動、無自己之 `commit`」之工作區 ⇒ ⛔ 覆蓋任何人之工作；其餘只出通知。
- 快轉後之規則以 Read 讀入（開工時未能載入）；context 壓縮後 Read 之內容隨摘要而淡出 ⇒ 本器於 `compact` 再提醒一次，⛔ 須 KL 另行 `/clear`。
- 對土地無影響：⛔ 動任何配地之程式與數字。

**問一**（KL 於貼本單之同一訊息答之）：

> 【現況】您在桌面版開新的 CC 視窗時，CC 的工作區有時建在舊版本：今天上午程式已更新到 365 完成後的版本，新視窗的工作區卻還停在 364 完成時的版本，CC 因此讀不到 365 新立的「常設規則索引」，要您手動更新再重開（`/clear`）。開窗時改選 `wip/s1-endpart` 也一樣；這是桌面版自己的行為，本專案的檔案改不到它。
> 【要改成】在您電腦上 Claude 的個人設定檔（`C:\Users\admin\.claude\settings.json`）加一項「開工自動對齊」：每次開新視窗或 `/clear` 時自動檢查工作區——若是桌面版新建、沒有任何修改、只是版本落後，就自動更新到最新版，並提醒 CC 先讀常設規則索引（CC 工作途中若整理記憶，會再提醒一次）；若工作區已有修改或成果，只提醒、不動。您不必再手動更新或 `/clear`。要知道的四件事：①這一項會讓您本機每次開 CC 新視窗（任何專案）時先執行一支小程式；本專案的視窗會先向 GitHub 確認最新版，通常一兩秒，網路不通時最多約 20 秒後放棄、照常開工；其他專案的視窗，程式一確認不是本專案就結束。②若日後搬移或改名本專案的程式資料夾，每個新視窗會多一行錯誤訊息（不影響使用），屆時刪去此項或請 CC 改路徑即可。③改設定檔之前先備份原檔；改寫後內容不變，但排版可能變成標準格式。④日後要停用，刪去設定檔裡這一項即可（可請 CC 代辦）。完成後同步您本機的程式資料夾，並用一個暫時的測試工作區實際演練一次再刪除。
> 【對土地的影響】無。不改任何配地程式、配地結果、驗證用的數字。
> 【要你判斷】是否同意在您的個人設定檔加入此項，並依本單同步您本機的程式資料夾？（是／否）

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

本單（二進位複製）入 `docs/orders/W-G.9-366_輕量單.md`；入倉之 blob ＝ 來源逐位（停機款 `2`）。`commit` 訊息逐字 `W-G.9-366 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　開工自動對齊之器（主線·零生產碼·一 `commit`）

1. 抽出塊 `SS`，對拍 `§五-1`（停機款 `3`），以二進位寫為新檔 `verify/tools/wg9366_session_sync.py`。
2. **驗**（停機款 `5`·出艙存 `<O>`）：
   - `python verify\tools\wg9366_session_sync.py --selftest` ⇒ `rc 0`；出艙 `16` 列，前 `15` 列皆以 `  ✅ ` 起首，其名依序 ＝ `T1`〜`T9`、`T10a`、`T10`〜`T14`，末列 `⇒ 紅 []；rc 0`。
   - `python verify\tools\wg9366_session_sync.py --selftest-mutant` ⇒ `rc 1`；末列 `⇒ 紅 ['T3', 'T4', 'T12']；rc 1`（判別力：去「無變動、無主線所無之 `commit`、新增之檔不存在」三守 ⇒ `T3`、`T4`、`T12` 必紅）。
   - `python verify\tools\wg9366_session_sync.py --cwd <repo>` ⇒ 出艙逐字 `（無訊息·skip）`（施工樹為 detached ⇒ 不動）；其後 `git rev-parse HEAD` 仍 ＝ 工項零之 `commit`（未變）。
3. 施後之 blob ＝ `§五-1` 項 `8` 之該檔；`git status --porcelain --untracked-files=all` ＝ 唯 `?? verify/tools/wg9366_session_sync.py`（施工樹之根之來源檔若在，不計·⛔ `add`）。`commit` 訊息逐字 `W-G.9-366 工項一：開工自動對齊之器（verify/tools/wg9366_session_sync.py·SessionStart hook 用）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　常設規則索引之一列 ＋ `CLAUDE.md` 之記（主線·零生產碼·一 `commit`）

1. 抽出塊 `IX`、`P20`，對拍 `§五-1`；自倉內 `docs/orders/W-G.9-365_輕量單.md` 以同一抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `6`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
2. 塊 `IX` 寫為 `<O>\IX.diff`：`git apply --check <O>\IX.diff` ⇒ 過；`git apply --numstat <O>\IX.diff` ⇒ `1`／`0`；`git apply <O>\IX.diff`。
3. **必紅**（判別力·塊 `P20` 未入前）：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 1`；不合恰一列 `L118 命中列數=0: '開工自動對齊'`；末列 `索引列數 124；內部字樣 121；外部指標 9；不合 1`。
4. 塊 `P20` 以二進位附於 `CLAUDE.md` 之末（停機款 `4`）。
5. **必綠**：同 `3` 之命令 ⇒ `rc 0`；末列 `索引列數 124；內部字樣 121；外部指標 9；不合 0`。
6. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（本批⛔ 動失敗考古·依 `CLAUDE.md`「指令檔之載入改制」節項 `3` 重跑）。
7. 施後之 blob ＝ `§五-1` 項 `8` 之二檔；`git status --porcelain --untracked-files=all` ＝ 唯 `M` 二列（常設規則索引、`CLAUDE.md`·施工樹之根之來源檔若在，不計·⛔ `add`）。`commit` 訊息逐字 `W-G.9-366 工項二：常設規則索引之一列 ＋ CLAUDE.md 之開工自動對齊之記（末端追加）⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項三　執行報告入倉（主線·新檔 `docs/reports/W-G.9-366R_開工自動對齊_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實；`8`、`12` 之實於工項四、五之後於對話補報）；③ 塊之實得（bytes／`sha256`）與 `CLAUDE.md` 之改前改後 bytes；④ 工項一、二之驗之出艙（含 `--selftest` 之全 `16` 列、`--selftest-mutant` 之末列、`checkidx` 之必紅與必綠）；⑤ `§二` 之放行（KL 之逐字）；⑥ CC 之自捕與自解；⑦ 各段耗時；⑧ `<O>` 之路徑。收工閘之實測值與工項四、五之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-366 工項三：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項四　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ `3c0c59c078e13e12a06df31576741f537c5dc8a6`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。
2. **撞檔前置**（`自誤 542`）：甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 集 `A`；乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 集 `U`；丙、`A ∩ U` 逐檔：`hash-object` 對 `rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8`）；不等 ⇒ 停機款 `8`·⛔ 動；丁、甲乙丙之出艙存 `<O>`。
3. `git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`branch --show-current` ＝ `wip/s1-endpart`；`rev-parse HEAD` ＝ 工項三之 `commit` 之全 `40` 碼；`hash-object verify/tools/wg9366_session_sync.py`、`hash-object .claude/rules/常設規則索引.md`、`hash-object CLAUDE.md` ＝ `§五-1` 項 `8` 之值；`hash-object app.py` ＝ `176f90c96f6c13ede5c0c4e2425bebbbe827bf51`；`status --porcelain --untracked-files=no` ＝ 空。

### 工項五　KL 本機使用者設定之掛載 ＋ 實境之演練（⛔ `commit`·⛔ `push`·於工項四之後）

1. **路徑之確認**：`git -C <主 checkout> worktree list --porcelain` 之首列 ＝ `worktree C:/Users/admin/Desktop/land-readjustment-trial`（以下 `<M>` ＝ 其反斜線形 `C:\Users\admin\Desktop\land-readjustment-trial`）；`python -c "import os;print(os.path.expanduser('~'))"` ＝ `C:\Users\admin`（以下稱 `<H>`）；`python -c "import os;print(os.environ.get('CLAUDE_CONFIG_DIR'))"` ＝ `None`（停機款 `12`）。
2. **掛載**：抽出塊 `US`，對拍 `§五-1`，寫為 `<O>\merge_user_settings.py`（⛔ 入倉）。`python <O>\merge_user_settings.py <H>\.claude\settings.json <M> <O>\user_settings_before_W-G.9-366.json` ⇒ `rc 0`；出艙：首列（原檔之有無、bytes、`sha256`）、次列（備份之 bytes、`sha256`、「與原檔逐位同：是」）；「新檔之 `hooks.SessionStart`」之末項（JSON 之值）＝ `{"matcher": "startup|clear|compact", "hooks": [{"type": "command", "command": "python \"C:/Users/admin/Desktop/land-readjustment-trial/verify/tools/wg9366_session_sync.py\"", "timeout": 60}]}`；`自驗二 除所增之一項外與原內容深相等：是`；`自驗三 含本器之項：1`；末列 `⇒ 增 1 項；rc 0`。本器⛔ 印設定檔之值（唯頂層鍵名與 `hooks.SessionStart`）；CC 亦⛔ 將使用者設定之全文載於對話或報告。
3. **實境之演練**（器 ＝ `<M>\verify\tools\wg9366_session_sync.py`·即使用者設定所指者；探針工作區 `<P>` ＝ `<O>\wg9366-probe`；以下 `<SIM>` ＝ `python <M>\verify\tools\wg9366_session_sync.py --hook-sim <P>`）：
   - 甲、`git -C <M> worktree add -b claude/wg9366-probe <P> 0e0edb3a40e68efd6748c08c198eaa51851b603c` ⇒ `rc 0`；`git -C <P> rev-parse HEAD` ＝ `0e0edb3a40e68efd6748c08c198eaa51851b603c`；`git -C <P> rev-parse --verify --quiet HEAD:.claude/rules/常設規則索引.md` ⇒ 非零（重現事證：該版本無常設規則索引）；`git -C <P> rev-parse --absolute-git-dir` ⇒ `<G>`（探針之 git 管理目錄）。
   - 乙、`<SIM> resume` ⇒ 出艙恰一列 `（hook 子程序 rc 0·stdout 0 B·stderr 0 B）`；`git -C <P> rev-parse HEAD` 仍 ＝ `0e0edb3…`（續接舊工作階段 ⇒ 不動）。
   - 丙、`<SIM> startup` ⇒ 出艙二列：首列逐字 「【開工自動對齊·W-G.9-366】本工作區（分支 `claude/wg9366-probe`）建於 `0e0edb3`，落後主線 `wip/s1-endpart` 8 筆；已以 `git merge --ff-only` 快轉至 `<T7>`（工作區之檔已更新為主線之最新版；快轉前本工作區無未提交之變動、無自己之 commit）。開工時所載入之常設規則係舊版或缺：請先以 Read 讀 `.claude/rules/常設規則索引.md`；讀寫 `app.py` 或 `verify/` 之 Python 檔以前，另讀 `.claude/rules/配地碼之領域指引.md`。」（`<T7>` ＝ 工項三之 `commit` 之前 `7` 碼）；次列 `（hook 子程序 rc 0·stdout 524 B·stderr 0 B）`。其後 `git -C <P> rev-parse HEAD` ＝ 工項三之 `commit`；`git -C <P> status --porcelain --untracked-files=no` ＝ 空；`<G>\wg9366_state` 之內容 ＝ `stale`。
   - 丁、`<SIM> compact` ⇒ 出艙二列：首列逐字 「【開工自動對齊·W-G.9-366】本工作階段開工時常設規則索引係舊版或缺（其後已自動快轉）；context 已壓縮，若 context 中未見 `.claude/rules/常設規則索引.md` 之全文，請再以 Read 讀之；讀寫 `app.py` 或 `verify/` 之 Python 檔以前，另讀 `.claude/rules/配地碼之領域指引.md`。」；次列 `（hook 子程序 rc 0·stdout 345 B·stderr 0 B）`。
   - 戊、`<SIM> clear` ⇒ 出艙恰一列 `（hook 子程序 rc 0·stdout 0 B·stderr 0 B）`；`<G>\wg9366_state` ＝ `fresh`；再 `<SIM> compact` ⇒ 恰一列 `（hook 子程序 rc 0·stdout 0 B·stderr 0 B）`。
   - 己、`python <M>\verify\tools\wg9366_session_sync.py --cwd <P>` ⇒ `（無訊息·current）`；`python <M>\verify\tools\wg9366_session_sync.py --cwd <M>` ⇒ `（無訊息·skip）`，且 `git -C <M> rev-parse HEAD` 仍 ＝ 工項三之 `commit`。
   - 庚、移除：`git -C <M> worktree remove <P>` ⇒ `rc 0`（⛔ `--force`）；`git -C <M> branch -D claude/wg9366-probe` ⇒ `rc 0`；其後 `git -C <M> worktree list --porcelain` ⛔ 含 `<P>`、`<G>` 不存在、`git -C <M> branch --list claude/wg9366-probe` ＝ 空、`git -C <M> status --porcelain --untracked-files=no` ＝ 空。
4. 甲〜庚之出艙存 `<O>`，並於對話逐項報之（停機款 `12`）。

**KL 之核對**（工項五之後·於對話回報發單側）：於桌面版選分支 `wip/s1-endpart`（勾 worktree）新開 CC 工作階段，請 CC 執行 `git log -1 --oneline`——其 `commit` ＝ 工項三之 `commit`（主線之端）。若該工作區原建於舊版本，CC 開工時之 context 另含一則以 `【開工自動對齊·W-G.9-366】` 起首之通知。

---

## `§四`　收工閘（工項三之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批四筆 `commit`（工項零〜三）之增刪（`git show --numstat`） | 工項零 ＝ 本單之增／`0`；工項一 ＝ `verify/tools/wg9366_session_sync.py` `422`／`0`；工項二 ＝ `.claude/rules/常設規則索引.md` `1`／`0`、`CLAUDE.md` `8`／`0`；工項三 ＝ 報告之增／`0` |
| `2` | 本批之全部異動 | `git diff --name-status 3c0c59c HEAD` 恰 `5` 列：`A` 本單、`A` 報告、`A` `verify/tools/wg9366_session_sync.py`、`M` `.claude/rules/常設規則索引.md`、`M` `CLAUDE.md` ⇒ 生產碼 `34` 檔相異 **`0`**、`.claude/settings.json` 未動；本批三新檔之 `git check-ignore` 皆無命中 |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 閘 `2` 之 `5` 檔合計 **`0`** |
| `4` | `CLAUDE.md` | 改前（`3c0c59c`）為改後之嚴格前綴，其尾 ＝ 塊 `P20` 逐位 |
| `5` | 施後之 blob | `§五-1` 項 `8` 之 `3` 檔逐檔相符 |
| `6` | 自限 | 遠端 heads **`35`**；主線 ＝ 工項三之 `commit`，其祖含 `3c0c59c`；除 `wip/s1-endpart` 外之 `34` 列與 `<O>\heads_before.txt` 逐列同 |
| `7` | `python verify/probes/probe_WG9270_closegate.py 577 566 .`；`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔> 577 566` | 皆 **`rc 0`**；四簿之值 ＝ `§零-0` 項 `3`（本批⛔ 鑄號） |
| `8` | `python verify/tools/wg942_append_audit.py 3c0c59c` | **`rc 0`**；末列 `結論：✅ 全部成立`（受檢 `77` 筆） |
| `9` | `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md`；`python <O>\gen_fa_index.py <repo> <O>\FX_regen2.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同；`python verify\tools\wg9366_session_sync.py --selftest` | `rc 0`·末列 `索引列數 124；內部字樣 121；外部指標 9；不合 0`；逐位同；`rc 0`·末列 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 只自本單抽塊而模擬工項一、二與工項五之演練，並實跑閘 `2`〜`5`、`7`〜`9` 之器 ⇒ 見 `§五-1` 項 `9`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `SS` | `22256` B·`sha256` `f8167ea421d3500c67b0cae1c3a0ae703efefed1979bfa555198a1f2f768d980`·`422` 列（圍欄內全文·末附換行）；新檔 `verify/tools/wg9366_session_sync.py`（工項一） |
| `3` | 塊 `IX` | `1974` B·`sha256` `75ff8ca5169538b3148ac7de4773f49f5e06a279e9b1150d9a2755b203cac8d8`·`12` 列（圍欄內全文·末附換行）；`git apply` 於 `.claude/rules/常設規則索引.md`（`git apply --numstat` ＝ `1`／`0`·工項二） |
| `4` | 塊 `P20` | `2285` B·`sha256` `0b05909d641e2e5d12fb4245394b76c8d4f022daa914e70103532d048cdf0a70`·`8` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md` 之末（工項二） |
| `5` | 塊 `US` | `4886` B·`sha256` `e5967bd4ffdd8ada58a580e136ca0bc4d75b24da8da914f0c107ea21adfe7b20`·`104` 列（圍欄內全文·末附換行）；倉外 `<O>\merge_user_settings.py`（⛔ 入倉·工項五） |
| `6` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳·同一抽取式） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列 |
| `7` | 塊之首列 | 塊 `P20` 之首列為空列（其抽取之首位元組 ＝ `\n`）；其餘塊之首列非空 |
| `8` | 施後之 blob（`git hash-object`·bytes） | `.claude/rules/常設規則索引.md` `dacddda92826e066813c3379fa305710adfa81bd`（`25053` B）；`CLAUDE.md` `f8e4eff0ccb1ca530413d89051133af1564eddd6`（`339034` B）；`verify/tools/wg9366_session_sync.py` `b30f983fdfc58bee2ac2cf24c347aef40a978e6c`（`22256` B） |
| `9` | 模擬（發單側·本機 Linux·`git worktree add --detach <S> 3c0c59c`·⛔ `push`） | 本批之塊（只自本單抽出）施於 `<S>`：工項一之 `--selftest` ⇒ `rc 0`·`16` 列·末列 `⇒ 紅 []；rc 0`；`--selftest-mutant` ⇒ `rc 1`·末列 `⇒ 紅 ['T3', 'T4', 'T12']；rc 1`；`--cwd <S>` ⇒ `（無訊息·skip）`；工項二之必紅與必綠 ＝ 工項二項 `3`、`5`；`gen_fa_index` 之重生成與倉內逐位同；施後之 blob ＝ 項 `8`；依工項零〜三之訊息於 `<S>` 作四筆本地 `commit`（報告以佔位檔代之·⛔ `push`）後：`git diff --name-status 3c0c59c HEAD` ＝ 閘 `2` 之 `5` 列、閘 `1` 之工項一、二之增刪相符、閘 `3` ＝ `0`、`wg942_append_audit.py 3c0c59c` ⇒ `rc 0`·`結論：✅ 全部成立`（受檢 `77`）、`probe_WG9270_closegate.py 577 566 .` ⇒ `rc 0`、`probe_WG9321_issuer_anchor.py` ⇒ `rc 0`·四簿之值 ＝ `§零-0` 項 `3`；工項五之演練（以 `<S>` 為主 checkout、暫存之使用者設定檔〔含既有之他鍵、含值之 `env`、他 hook 與 BOM〕）：塊 `US` ⇒ `增 1 項`、自驗二「是」、自驗三 `1`·`rc 0`、出艙⛔ 含 `env` 之值，以新備份檔重跑 ⇒ `增 0 項`·`rc 0`；探針工作區建於 `0e0edb3`：`resume` ⇒ `stdout 0 B`·不動；`startup` ⇒ 通知一則（`stdout 524 B`·模擬之主線之端為 `3c0c59c` ⇒ 「落後 … 4 筆」）且 `HEAD` ＝ 主線之端、狀態 `stale`；`compact` ⇒ 提醒一則（`stdout 345 B`）；`clear` ⇒ `0 B`·狀態 `fresh`；再 `compact` ⇒ `0 B`；`--cwd` ⇒ `（無訊息·current）`；主 checkout ⇒ `（無訊息·skip）`；探針之移除 `rc 0`·其 git 管理目錄不存 |
| `10` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗六十八實跑（態 `3c0c59c`）：🔴 機械 `0` 項／🟡 提示 `10` 項——`P-1` `:62`（`§一` 表：「無 `.claude\rules` 目錄」之母體 ＝ KL 所貼之該工作區之出艙；「不存在」係器之條件之述 ⇒ **具名豁免**）、`P-1` `:77`（`§二` 首項之「二者皆非」：其母體 ＝ `§一` 項 `3` 之事證·同段已引 ⇒ **具名豁免**）、`P-1` `:100`（工項一之驗：「無變動、無主線所無之 `commit`」係器之守之名·非斷言 ⇒ **具名豁免**）、`P-1` `:130`（工項五：「⛔ 含 `<P>`」「`<G>` 不存在」係同列所具名之命令之期·其母體 ＝ 該命令之出艙 ⇒ **具名豁免**）、`P-1` `:202`／`:488` 與 `P-4` `:317`（附錄甲塊 `SS` 之器內之 docstring、自驗之註與 `align` 段·其箭頭 ＝ 快轉之前後〔版本之先後〕·塊內自載 ⇒ **具名豁免**）、`P-1` `:641`（附錄丙塊 `P20`：「即無此 hook」係條件句·其母體 ＝ 建於本批以前之版本之專案設定 ⇒ **具名豁免**）、`P-1` `:655`／`:672`（附錄丁塊 `US` 之器內之 docstring 與錯誤訊息字串·非斷言 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `21232`–`28952`）⇒ `rc 0` |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````diff `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜三 ⇒ 依 `§二` 之放行、各驗皆符後逕行 `push` 主線；工項四 ⇒ KL 本機之主 checkout（收工閘皆符之後）；工項五 ⇒ KL 本機之使用者設定與探針（工項四之後）。
3. 收工後，主 checkout 之根之來源檔（本單，及工項四所移之檔）由 KL 自行移除（CC ⛔ 刪之）；`<O>` 之備份檔（使用者設定之原檔）留存，由 KL 自行處置。

---

## 附錄甲　塊 `SS`（新檔 `verify/tools/wg9366_session_sync.py`（工項一））

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`W-G.9-366`：開工自動對齊（Claude Code 之 SessionStart hook·⛔ 零生產碼）。

緣由：桌面版新開之 worktree 有時建於舊版本（例：主線已至 `3c0c59c`，新工作區仍為 `0e0edb3`），
致開工時讀不到 `.claude/rules/` 之最新規則。本器於開工（`startup`／`clear`）時檢查工作區，
合於下列全部條件者，以 `git merge --ff-only` 快轉至主線之端，並告知 Claude 重讀規則：

  1. 工作區之遠端 `origin` 之網址以 `land-readjustment-trial`（或其 `.git`）結尾（他專案一律不動）；
  2. 工作區為 linked worktree（主 checkout 一律不動）；
  3. 所在分支名以 `claude/` 起首（桌面版所建者；detached 與他分支一律不動）；
  4. 追蹤檔無變動（`git status --porcelain --untracked-files=no` 為空）；
  5. `HEAD` 為主線之端之祖先而不等於之（即無主線所無之 commit、且確實落後）；
  6. 主線之端所新增之檔，於工作區皆不存在（⛔ 覆蓋未追蹤或被忽略之檔）。

落後而不合 4〜6 者，只出通知、不動；不落後者（含只超前者）無聲。快轉而常設規則索引於開工時係舊版或缺者，
另於該工作區之 git 管理目錄記一狀態檔；其後 context 壓縮（`compact`）時再提醒重讀，`/clear` 或新開工後解除
（狀態係逐工作區、⛔ 逐工作階段：同一工作區另開之工作階段開工時亦解除之）。
⛔ push、⛔ 動他分支、⛔ 刪任何檔。一切例外皆以 `rc 0` 結束（SessionStart 不得擋開工），其訊息照實出艙。

用法：
  hook（stdin 為 Claude Code 之 JSON，取其 `cwd`、`source`）：python wg9366_session_sync.py
  手動：python wg9366_session_sync.py --cwd <工作區路徑>
  模擬 hook（以子程序經 stdin 餵 JSON）：python wg9366_session_sync.py --hook-sim <工作區路徑> <source>
  自驗：python wg9366_session_sync.py --selftest          ⇒ 末列 `⇒ 紅 []；rc 0`
  判別力：python wg9366_session_sync.py --selftest-mutant ⇒ 末列 `⇒ 紅 ['T3', 'T4', 'T12']；rc 1`
"""
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time

MAINLINE = "wip/s1-endpart"
REMOTE = "origin"
PROJECT_KEY = "land-readjustment-trial"
INDEX = ".claude/rules/常設規則索引.md"
DOMAIN = ".claude/rules/配地碼之領域指引.md"
TAG = "【開工自動對齊·W-G.9-366】"
STATE = "wg9366_state"          # 置於該工作區之 git 管理目錄（.git/worktrees/<名>/）·⛔ 在工作樹內
FETCH_LIMIT = 20                # 秒
MERGE_DEADLINE = 40             # 秒：自本器開始逾此即⛔ 快轉（hook 之限時為 60 秒）
_URL_RE = re.compile(r"[/\\:]" + re.escape(PROJECT_KEY) + r"(\.git)?[/\\]?$")
_ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")


_NOGC = ["-c", "gc.auto=0", "-c", "maintenance.auto=false"]   # Windows 下 gc 無法背景執行 ⇒ 關之


def _git(cwd, *args, timeout=30):
    r = subprocess.run(["git", *_NOGC, "-C", cwd, *args], capture_output=True, timeout=timeout, env=_ENV,
                       stdin=subprocess.DEVNULL)
    return r.returncode, r.stdout.decode("utf-8", "replace").strip(), r.stderr.decode("utf-8", "replace").strip()


def _fetch(cwd):
    """取主線之端；輸出一律丟棄（⛔ 管線 ⇒ 逾時之子程序不致卡住本器）。"""
    try:
        subprocess.run(["git", *_NOGC, "-c", "http.lowSpeedLimit=1000", "-c", "http.lowSpeedTime=10", "-C", cwd,
                        "fetch", "--quiet", REMOTE, MAINLINE], stdin=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=FETCH_LIMIT, env=_ENV)
    except subprocess.TimeoutExpired:
        pass                                    # 連不上則以本機之遠端追蹤 ref 為準


def _blob(cwd, rev, path):
    rc, out, _ = _git(cwd, "rev-parse", "--verify", "--quiet", f"{rev}:{path}")
    return out if rc == 0 else None


def _ours(cwd, need_branch=True):
    """合於條件 1〜3（need_branch=False 時只 1〜2）者回 (工作樹頂, 分支或空字串)，否則 None。"""
    rc, url, _ = _git(cwd, "remote", "get-url", REMOTE)
    if rc != 0 or not _URL_RE.search(url.strip()):
        return None
    rc, top, _ = _git(cwd, "rev-parse", "--show-toplevel")
    if rc != 0 or not os.path.isfile(os.path.join(top, ".git")):
        return None                             # 主 checkout（.git 為目錄）或非 git
    rc, branch, _ = _git(cwd, "symbolic-ref", "--quiet", "--short", "HEAD")
    if need_branch and (rc != 0 or not branch.startswith("claude/")):
        return None                             # detached 或非桌面版所建之分支
    return top, (branch if rc == 0 else "")


def _state_path(cwd):
    rc, gd, _ = _git(cwd, "rev-parse", "--absolute-git-dir")
    return os.path.join(gd, STATE) if rc == 0 and gd else None


def _set_state(cwd, value):
    """記狀態；寫不成者回 False（⛔ 擋開工、⛔ 吞訊息）。"""
    try:
        p = _state_path(cwd)
        if not p:
            return False
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(value + "\n")
        return True
    except OSError:
        return False


def _get_state(cwd):
    p = _state_path(cwd)
    if p and os.path.isfile(p):
        return open(p, encoding="utf-8").read().strip()
    return None


def _occupied(top, rel):
    """主線所新增之 rel，於工作區已有同名之檔，或其上層路徑已為檔（快轉將覆蓋或移除之）。"""
    parts = rel.split("/")
    for k in range(1, len(parts)):
        q = os.path.join(top, *parts[:k])
        if os.path.lexists(q) and not os.path.isdir(q):
            return True
    return os.path.lexists(os.path.join(top, *parts))


def align(cwd, mutate=False, fetch=True):
    """回 (訊息或空字串, 動作)。動作 ∈ {"skip", "current", "ff", "notice", "error"}。"""
    t0 = time.monotonic()
    ours = _ours(cwd)
    if ours is None:
        return "", "skip"
    top, branch = ours
    tip_ref = f"{REMOTE}/{MAINLINE}"
    if fetch:
        _fetch(cwd)
    rc, tip, _ = _git(cwd, "rev-parse", "--verify", "--quiet", tip_ref)
    if rc != 0:
        return f"{TAG}找不到 `{tip_ref}`，未對齊；施工前請依單之開場核對主線之端。", "error"
    _, head, _ = _git(cwd, "rev-parse", "HEAD")
    _, n_behind, _ = _git(cwd, "rev-list", "--count", f"HEAD..{tip_ref}")
    if head == tip or n_behind == "0":
        return "", "current"                    # 已在主線之端，或只超前（無可快轉）
    behind = _git(cwd, "merge-base", "--is-ancestor", "HEAD", tip_ref)[0] == 0
    _, n_ahead, _ = _git(cwd, "rev-list", "--count", f"{tip_ref}..HEAD")
    _, dirty, _ = _git(cwd, "status", "--porcelain", "--untracked-files=no")
    rc, added, _ = _git(cwd, "diff", "--name-only", "--diff-filter=AR", "-z", "HEAD", tip_ref)
    if rc != 0:
        clash = ["（無從比對主線所新增之檔）"]
    else:
        clash = [p for p in added.split("\0") if p and _occupied(top, p)]
    if not mutate and (dirty or not behind or clash):
        if dirty:
            why = "追蹤檔有未提交之變動"
        elif not behind:
            why = f"含主線所無之 commit {n_ahead} 筆（自己之成果，或建於他分支）"
        else:
            why = f"主線所新增之檔已存在於工作區（{'、'.join(clash[:3])}{' 等' if len(clash) > 3 else ''}）"
        return (f"{TAG}本工作區（分支 `{branch}`·`{head[:7]}`）落後主線 `{MAINLINE}`（`{tip[:7]}`）{n_behind} 筆，"
                f"但{why}，未自動快轉。施工前請依單之開場核對主線之端。"), "notice"
    if time.monotonic() - t0 > MERGE_DEADLINE:
        return (f"{TAG}本工作區（分支 `{branch}`·`{head[:7]}`）落後主線 `{MAINLINE}` {n_behind} 筆，"
                f"但取主線之端逾時，未自動快轉。施工前請依單之開場核對主線之端。"), "notice"
    old_idx = _blob(cwd, "HEAD", INDEX)
    rc, _, err = _git(cwd, "merge", "--ff-only", "--quiet", tip_ref)
    if rc != 0:
        return f"{TAG}快轉失敗（`{head[:7]}` → `{tip[:7]}`）：{err[:300]}。施工前請依單之開場核對主線之端。", "error"
    new_idx = _blob(cwd, "HEAD", INDEX)
    msg = (f"{TAG}本工作區（分支 `{branch}`）建於 `{head[:7]}`，落後主線 `{MAINLINE}` {n_behind} 筆；"
           f"已以 `git merge --ff-only` 快轉至 `{tip[:7]}`（工作區之檔已更新為主線之最新版；快轉前本工作區無未提交之變動、無自己之 commit）。")
    if new_idx and new_idx != old_idx:
        msg += (f"開工時所載入之常設規則係舊版或缺：請先以 Read 讀 `{INDEX}`；"
                f"讀寫 `app.py` 或 `verify/` 之 Python 檔以前，另讀 `{DOMAIN}`。")
        if not _set_state(cwd, "stale"):
            msg += "（狀態檔未能寫入：context 壓縮後之再提醒將缺。）"
    else:
        msg += "常設規則索引未變。"
    return msg, "ff"


def on_compact(cwd):
    """context 壓縮後：本工作階段若係快轉而來（狀態 ＝ stale），再提醒重讀。"""
    if _ours(cwd, need_branch=False) is None or _get_state(cwd) != "stale":
        return ""
    return (f"{TAG}本工作階段開工時常設規則索引係舊版或缺（其後已自動快轉）；context 已壓縮，"
            f"若 context 中未見 `{INDEX}` 之全文，請再以 Read 讀之；讀寫 `app.py` 或 `verify/` 之 Python 檔以前，另讀 `{DOMAIN}`。")


def dispatch(cwd, source, mutate=False, fetch=True):
    """依 SessionStart 之來源分派；回訊息（可為空）。"""
    if source == "compact":
        return on_compact(cwd)
    if source not in (None, "startup", "clear"):
        return ""                               # resume、fork 等：不動
    if _ours(cwd, need_branch=False) is not None and _get_state(cwd) == "stale":
        _set_state(cwd, "fresh")                # 新開工或 /clear ⇒ 規則自磁碟重新載入
    msg, _ = align(cwd, mutate, fetch)
    return msg


def _emit(text):
    if text:
        sys.stdout.buffer.write((text + "\n").encode("utf-8"))


def _hook():
    cwd, source = os.getcwd(), None
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8") or "{}")
        source = data.get("source")
        cwd = data.get("cwd") or cwd
    except Exception:
        pass
    try:
        msg = dispatch(cwd, source)
    except Exception as e:  # SessionStart ⛔ 擋開工
        msg = f"{TAG}本器例外（{type(e).__name__}），未對齊；施工前請依單之開場核對主線之端。"
    _emit(msg)
    return 0


def _hook_sim(cwd, source):
    """以子程序執行本器之 hook 模式（stdin ＝ JSON），照實出艙其 stdout 與 rc。"""
    payload = json.dumps({"cwd": cwd, "source": source, "hook_event_name": "SessionStart"}, ensure_ascii=False)
    r = subprocess.run([sys.executable, os.path.abspath(__file__)], input=payload.encode("utf-8"), capture_output=True)
    out = r.stdout.decode("utf-8", "replace")
    sys.stdout.write(out)
    print(f"（hook 子程序 rc {r.returncode}·stdout {len(r.stdout)} B·stderr {len(r.stderr)} B）")
    return 0


def _rm(path):
    """刪暫存目錄（Windows 下 git 之物件檔為唯讀，先去唯讀）；回是否刪盡。"""
    for root, dirs, files in os.walk(path):
        for n in dirs + files:
            try:
                os.chmod(os.path.join(root, n), stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
            except OSError:
                pass
    shutil.rmtree(path, ignore_errors=True)
    return not os.path.exists(path)


# ── 自驗（暫存目錄內建倉·⛔ 觸及本倉·⛔ 連網）──────────────────────────────────
def _selftest(mutate=False):
    tmp = tempfile.mkdtemp(prefix="wg9366_")
    cfg = ["-c", "user.name=wg9366", "-c", "user.email=wg9366@test", "-c", "core.autocrlf=false",
           "-c", "init.defaultBranch=main", "-c", "commit.gpgsign=false"]

    def run(cwd, *a):
        r = subprocess.run(["git", *cfg, "-C", cwd, *a], capture_output=True)
        if r.returncode != 0:
            raise RuntimeError(f"git {' '.join(a)}: {r.stderr.decode('utf-8', 'replace')}")
        return r.stdout.decode().strip()

    def write(path, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)

    red, lines = [], []

    def check(name, ok, detail):
        lines.append(f"  {'✅' if ok else '🔴'} {name} {detail}")
        if not ok:
            red.append(name)

    try:
        def make(proj):
            bare = os.path.join(tmp, proj + ".git")
            main = os.path.join(tmp, proj + "_main")
            subprocess.run(["git", *cfg, "init", "--bare", "-q", bare], check=True)
            subprocess.run(["git", *cfg, "clone", "-q", bare, main], check=True, capture_output=True)
            run(main, "checkout", "-q", "-b", MAINLINE)
            write(os.path.join(main, "a.txt"), "A\n")
            write(os.path.join(main, "sub", "s.txt"), "S\n")
            run(main, "add", "a.txt", "sub"); run(main, "commit", "-q", "-m", "A")
            a = run(main, "rev-parse", "HEAD")
            write(os.path.join(main, INDEX), "索引 B\n")
            run(main, "add", INDEX); run(main, "commit", "-q", "-m", "B")
            b = run(main, "rev-parse", "HEAD")
            run(main, "push", "-q", "origin", MAINLINE)
            return main, a, b

        main, a, b = make(PROJECT_KEY)

        def wt(name, base, branch=True):
            p = os.path.join(tmp, "wt_" + name)
            if branch:
                run(main, "worktree", "add", "-q", "-b", f"claude/{name}" if branch is True else branch, p, base)
            else:
                run(main, "worktree", "add", "-q", "--detach", p, base)
            return p

        def head(p):
            return run(p, "rev-parse", "HEAD")

        # T1：落後、乾淨、claude/ ⇒ 快轉，並令重讀索引（索引於 A 無、於 B 有）；記狀態 stale
        p = wt("t1", a); msg, act = align(p, mutate)
        check("T1", act == "ff" and head(p) == b and "已以 `git merge --ff-only` 快轉" in msg and "請先以 Read 讀" in msg
              and _get_state(p) == "stale", f"act={act} head={'tip' if head(p) == b else head(p)[:7]} state={_get_state(p)}")
        # T2：已在主線之端 ⇒ 無聲
        p = wt("t2", b); msg, act = align(p, mutate)
        check("T2", act == "current" and msg == "" and head(p) == b, f"act={act}")
        # T3：有自己之 commit（與主線分叉）⇒ 只通知、不動
        p = wt("t3", a); write(os.path.join(p, "own.txt"), "own\n")
        run(p, "add", "own.txt"); run(p, "commit", "-q", "-m", "own"); h0 = head(p)
        msg, act = align(p, mutate)
        check("T3", act == "notice" and head(p) == h0 and "含主線所無之 commit 1 筆" in msg, f"act={act}")
        # T4：追蹤檔有變動 ⇒ 只通知、不動
        p = wt("t4", a); write(os.path.join(p, "a.txt"), "A dirty\n"); msg, act = align(p, mutate)
        check("T4", act == "notice" and head(p) == a and "追蹤檔有未提交之變動" in msg, f"act={act}")
        # T5：主 checkout ⇒ 無聲、不動
        run(main, "checkout", "-q", "--detach", a); run(main, "checkout", "-q", "-B", "claude/t5main", a)
        msg, act = align(main, mutate)
        check("T5", act == "skip" and head(main) == a and msg == "", f"act={act}")
        # T6：非 claude/ 之分支 ⇒ 無聲、不動
        p = wt("t6", a, branch="feature/t6"); msg, act = align(p, mutate)
        check("T6", act == "skip" and head(p) == a and msg == "", f"act={act}")
        # T7：detached ⇒ 無聲、不動
        p = wt("t7", a, branch=False); msg, act = align(p, mutate)
        check("T7", act == "skip" and head(p) == a and msg == "", f"act={act}")
        # T8：他專案、名稱相近之他專案（遠端網址不以專案名結尾）⇒ 無聲、不動
        res = []
        for proj in ("other-project", PROJECT_KEY + "-archive"):
            main2, a2, _ = make(proj)
            p8 = os.path.join(tmp, "wt_t8_" + proj); run(main2, "worktree", "add", "-q", "-b", "claude/t8", p8, a2)
            msg, act = align(p8, mutate)
            res.append(act == "skip" and run(p8, "rev-parse", "HEAD") == a2 and msg == "")
        check("T8", all(res), f"res={res}")
        # T9：落後但索引未變 ⇒ 快轉，訊息載「常設規則索引未變」，⛔ 記 stale
        write(os.path.join(main, "c.txt"), "C\n")
        run(main, "checkout", "-q", MAINLINE)
        run(main, "add", "c.txt"); run(main, "commit", "-q", "-m", "C"); c = run(main, "rev-parse", "HEAD")
        run(main, "push", "-q", "origin", MAINLINE)
        p = wt("t9", b); msg, act = align(p, mutate)
        check("T9", act == "ff" and head(p) == c and "常設規則索引未變" in msg and "請先以 Read 讀" not in msg
              and _get_state(p) is None, f"act={act}")
        # T10：主線之端由他處推進（本機之遠端追蹤 ref 仍舊）⇒ 須經 fetch 方知落後
        other = os.path.join(tmp, "other_clone")
        subprocess.run(["git", *cfg, "clone", "-q", "-b", MAINLINE, os.path.join(tmp, PROJECT_KEY + ".git"), other],
                       check=True, capture_output=True)
        write(os.path.join(other, "d.txt"), "D\n")
        run(other, "add", "d.txt"); run(other, "commit", "-q", "-m", "D"); d = run(other, "rev-parse", "HEAD")
        run(other, "push", "-q", "origin", MAINLINE)
        p = wt("t10a", c); msg, act = align(p, mutate, fetch=False)
        check("T10a", act == "current" and head(p) == c, f"act={act}（⛔ fetch ⇒ 不知落後·對照）")
        p = wt("t10", c); msg, act = align(p, mutate)
        check("T10", act == "ff" and head(p) == d and "落後主線 `wip/s1-endpart` 1 筆" in msg,
              f"act={act} head={'D' if head(p) == d else head(p)[:7]}")
        # T11：只超前（有自己之 commit、⛔ 落後）⇒ 無聲、不動
        p = wt("t11", d); write(os.path.join(p, "own.txt"), "own\n")
        run(p, "add", "own.txt"); run(p, "commit", "-q", "-m", "own"); h0 = head(p)
        msg, act = align(p, mutate)
        check("T11", act == "current" and msg == "" and head(p) == h0, f"act={act}")
        # T12：主線所新增之檔已以「被忽略之檔」存在於工作區（git 於快轉時會逕行覆蓋之）⇒ 只通知、⛔ 覆蓋
        p = wt("t12", c); write(os.path.join(p, ".gitignore"), "d.txt\n"); write(os.path.join(p, "d.txt"), "local\n")
        msg, act = align(p, mutate)
        ok12a = act == "notice" and head(p) == c and "d.txt" in msg and \
            open(os.path.join(p, "d.txt"), encoding="utf-8").read() == "local\n"
        # 上層路徑已為被忽略之檔（主線新增 sub2/e.txt，工作區有被忽略之檔 sub2）
        run(main, "merge", "-q", "--ff-only", d)
        write(os.path.join(main, "sub2", "e.txt"), "E\n")
        run(main, "add", "sub2"); run(main, "commit", "-q", "-m", "E")
        run(main, "push", "-q", "origin", MAINLINE)
        q = wt("t12b", d); write(os.path.join(q, ".gitignore"), "sub2\n"); write(os.path.join(q, "sub2"), "local\n")
        msg2, act2 = align(q, mutate)
        ok12b = act2 == "notice" and head(q) == d and "sub2/e.txt" in msg2 and os.path.isfile(os.path.join(q, "sub2"))
        check("T12", ok12a and ok12b, f"act={act}/{act2}")
        # T13：hook 之分派——resume 不動；工作階段之目錄為子目錄亦快轉；壓縮後再提醒；/clear 後解除
        p = wt("t13", a)
        r1 = dispatch(p, "resume", mutate)
        ok1 = r1 == "" and head(p) == a
        r2 = dispatch(os.path.join(p, "sub"), "startup", mutate)
        ok2 = ("已以 `git merge --ff-only` 快轉" in r2 and head(p) == run(p, "rev-parse", f"{REMOTE}/{MAINLINE}")
               and _get_state(p) == "stale")
        r3 = dispatch(p, "compact", mutate)
        ok3 = "context 已壓縮" in r3 and "請再以 Read 讀之" in r3
        r4 = dispatch(p, "clear", mutate)
        ok4 = r4 == "" and _get_state(p) == "fresh"
        r5 = dispatch(p, "compact", mutate)
        ok5 = r5 == ""
        # 開工快轉後轉為 detached（各單之開場即如此）⇒ 壓縮時仍提醒、/clear 時仍解除
        q = wt("t13d", a); dispatch(q, "startup", mutate); run(q, "checkout", "-q", "--detach")
        ok6 = "context 已壓縮" in dispatch(q, "compact", mutate)
        ok7 = dispatch(q, "clear", mutate) == "" and _get_state(q) == "fresh" and dispatch(q, "compact", mutate) == ""
        check("T13", ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7,
              f"resume={ok1} startup(子目錄)={ok2} compact={ok3} clear={ok4} compact′={ok5} detached={ok6 and ok7}")
        # T14：遠端追蹤 ref 不存在 ⇒ 錯誤之通知（⛔ 擋開工）
        run(main, "update-ref", "-d", f"refs/remotes/{REMOTE}/{MAINLINE}")
        p = wt("t14", a); msg, act = align(p, mutate, fetch=False)
        check("T14", act == "error" and "找不到" in msg and head(p) == a, f"act={act}")
    except Exception as e:
        lines.append(f"  🔴 例外 {type(e).__name__}: {e}")
        red.append("EXC")
    finally:
        if not _rm(tmp):
            print(f"⚠️ 暫存目錄未能全刪（⛔ 影響判定）：{tmp}", file=sys.stderr)
    print("\n".join(lines))
    rc = 1 if red else 0
    print(f"⇒ 紅 {red}；rc {rc}")
    return rc


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    a = sys.argv[1:]
    if a[:1] == ["--selftest"]:
        return _selftest(False)
    if a[:1] == ["--selftest-mutant"]:
        return _selftest(True)
    if a[:1] == ["--cwd"] and len(a) == 2:
        msg, act = align(a[1])
        print(msg or f"（無訊息·{act}）")
        return 0
    if a[:1] == ["--hook-sim"] and len(a) == 3:
        return _hook_sim(a[1], a[2])
    return _hook()


if __name__ == "__main__":
    sys.exit(main())
````

## 附錄乙　塊 `IX`（`git apply` 於 `.claude/rules/常設規則索引.md`（`git apply --numstat` ＝ `1`／`0`·工項二））

````diff
diff --git a/.claude/rules/常設規則索引.md b/.claude/rules/常設規則索引.md
index ee0685a..dacddda 100644
--- a/.claude/rules/常設規則索引.md
+++ b/.claude/rules/常設規則索引.md
@@ -115,6 +115,7 @@
 - GB-198（⬜ 未修）：numpy ≥ 2.5 之 np.cross 拒收二維向量 ⇒ harness（verify/stepg_pipeline.py）中止；requirements.txt 無上界；登記之實跑以 numpy 2.4.6 為之；失效條件＝設上界 < 2.5 或改明式二維叉積。〔W-G.9-364`·〕〔外：docs/reports/W-G.4_泛用阻塞項登記表.md「### `GB-198` 🆕」〕
 - 畫面執行環境之 WV_K6_STEP0／WV_K6B_STAGE3／WV_K929_6 須未設（設之即回舊行為）；主 checkout 同步後須重啟介面。〔W-G.9-358`·〕
 - 生產與驗證讀同一份圖資，現行為 data/V6_1.dxf；data/V6.dxf 僅供溯源，不刪不覆蓋。〔外：docs/rulings/K-6_街角地分配程序與可分配判準.md「### 🔒 K-9-20　」〕
+- 開工自動對齊：KL 本機之使用者設定掛有 SessionStart hook（主 checkout 之 verify/tools/wg9366_session_sync.py）。桌面版新建之 `claude/` 工作區若乾淨而落後主線，開工時自動快轉至 `origin/wip/s1-endpart` 並出通知；見其通知者，先以 Read 讀本索引之最新版。此器依主 checkout 為最新，故各單收尾之主 checkout 同步不可省。〔開工自動對齊〕
 ## 十二、讀起來像現行、其實已被取代（讀全文時注意）
 - 「發單側⛔ 有倉之存取權」節之結論全部作廢〔發單側<u>有</u>倉之存取權〕；常規一四項於零生產碼側已不拘束〔「生產碼」之**機械界定**〕；B 形單獨使用不可信〔B 形於本倉為量測器紅〕。
 - 自誤寬形停用〔寬形之**廢止標記**〕；占用母體改全 docs/、列框改聯集、D3 改嚴格式〔宣告框補款 `⑦`〕〔宣告框補款 `⑧`〕；「戒之次號仍為 40」已過時（戒 40 已鑄於 W-G.9-206 單，次號須現查）。
````

## 附錄丙　塊 `P20`（附於 `CLAUDE.md` 之末（工項二））

````markdown

## 🔧 開工自動對齊（`W-G.9-366`·KL `2026-10-04` 令·⛔ 上文一字不刪·純末端追加）

1. **緣由**：`2026-10-04`，KL 於桌面版選分支 `wip/s1-endpart`（勾 worktree）新開工作階段，其工作區 `claude/context-770073` 建於 `0e0edb3`，而本機與遠端之 `wip/s1-endpart` 皆已為 `3c0c59c`（`git worktree list` 與 `git rev-parse` 之出艙·KL 所貼）⇒ 開工時讀不到 `W-G.9-365` 所立之 `.claude/rules/常設規則索引.md`。桌面版建工作區所據之版本非本倉所能左右。
2. **機制**：KL 本機之使用者設定（`~/.claude/settings.json`）掛 SessionStart hook（`startup`／`clear`／`compact`），執行主 checkout 之 `verify/tools/wg9366_session_sync.py`。開工（`startup`／`clear`）時，工作區合於下列全部條件者，以 `git merge --ff-only` 快轉至 `origin/wip/s1-endpart`，並告知 Claude 以 Read 讀常設規則索引：遠端網址以 `land-readjustment-trial` 結尾；為 linked worktree；分支名以 `claude/` 起首；追蹤檔無變動；`HEAD` 為主線之端之祖先而不等於之；主線所新增之檔於工作區皆不存在。落後而不合後三條件者只出通知、不動；不落後者無聲。快轉而索引於開工時係舊版或缺者，記狀態於該工作區之 git 管理目錄，其後 context 壓縮（`compact`）時再提醒重讀，`/clear` 或新開工後解除。主 checkout、detached、他分支、他專案一律不動；⛔ push、⛔ 刪檔；本器之例外一律不擋開工。
3. **掛於使用者設定之由**：依 Claude Code 之文件，專案之 `.claude/settings.json` 自工作階段之目錄讀取，工作區若建於本批以前之版本即無此 hook；使用者設定則每次皆讀，而其所指之器在主 checkout，各單收尾之主 checkout 同步使之恆為最新。故主 checkout 之同步不可省。
4. **開關**：KL 欲停用時，自使用者設定之 `hooks.SessionStart` 刪該項即可（其 command 含 `wg9366_session_sync.py`）；不涉本倉。重新掛載之器見 `docs/orders/W-G.9-366_輕量單.md` 之塊 `US`（冪等·寫前先備份）。
5. **驗收**：KL 於桌面版選 `wip/s1-endpart` 新開工作階段，請 CC 執行 `git log -1 --oneline`，其端 ＝ 主線之端。
````

## 附錄丁　塊 `US`（倉外 `<O>\merge_user_settings.py`（⛔ 入倉·工項五））

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""W-G.9-366 工項五：於 KL 之使用者設定掛 SessionStart hook（倉外之器·⛔ 入倉）。

用法：python merge_user_settings.py <使用者設定檔> <主 checkout 之絕對路徑> <備份檔>
- 主 checkout 之下無 verify/tools/wg9366_session_sync.py ⇒ rc 2、⛔ 寫。
- 備份檔已存在 ⇒ rc 2、⛔ 寫（⛔ 覆寫備份）。
- 設定檔存在而非合法 JSON、頂層非物件、hooks 非物件或 hooks.SessionStart 非陣列 ⇒ rc 2、⛔ 寫。
- 既有之鍵與值一律保留；只於 hooks.SessionStart 末增一項（已有同一 command 者 ⇒ 不重複增·冪等）。
- 寫前將原檔逐位元組備份至 <備份檔>（原檔不存在者，備份檔為空檔）；新檔先寫暫存檔再整檔替換。
- 寫後重讀自驗：新檔可解、除所增之一項外與原內容深相等、含本器之項恰 1。
- 出艙：原檔與備份之 bytes／sha256、新檔之頂層鍵名（⛔ 印其值·設定檔可能含金鑰等）、
  新檔之 hooks.SessionStart 全文、自驗三列、末列 `⇒ 增 N 項；rc 0`。
"""
import copy
import hashlib
import json
import os
import sys


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 4:
        print("用法：python merge_user_settings.py <使用者設定檔> <主 checkout> <備份檔>")
        return 2
    path, main_dir, backup = sys.argv[1], sys.argv[2], sys.argv[3]
    script = os.path.normpath(os.path.join(os.path.abspath(main_dir), "verify", "tools",
                                           "wg9366_session_sync.py")).replace("\\", "/")
    if not os.path.isfile(script):
        print(f"🔴 主 checkout 之下無 {script} ⇒ ⛔ 寫")
        return 2
    if os.path.exists(backup):
        print(f"🔴 備份檔已存在：{backup} ⇒ ⛔ 寫（⛔ 覆寫備份）")
        return 2
    command = f'python "{script}"'
    existed = os.path.exists(path)
    raw = open(path, "rb").read() if existed else b""
    print(f"原檔：{'存在' if existed else '不存在'}；bytes {len(raw)}；sha256 {hashlib.sha256(raw).hexdigest()}")
    try:
        data = json.loads(raw.decode("utf-8-sig")) if raw.strip() else {}
    except ValueError as e:
        print(f"🔴 既有設定檔非合法 JSON（{e}）⇒ ⛔ 寫")
        return 2
    if not isinstance(data, dict):
        print("🔴 既有設定檔之頂層非物件 ⇒ ⛔ 寫")
        return 2
    before = copy.deepcopy(data)
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        print("🔴 既有之 hooks 非物件 ⇒ ⛔ 寫")
        return 2
    ss = hooks.setdefault("SessionStart", [])
    if not isinstance(ss, list):
        print("🔴 既有之 hooks.SessionStart 非陣列 ⇒ ⛔ 寫")
        return 2

    def mine(d):
        return sum(1 for e in d.get("hooks", {}).get("SessionStart", []) if isinstance(e, dict)
                   for h in e.get("hooks", []) if isinstance(h, dict) and h.get("command") == command)

    added = 0
    if mine(data) == 0:
        ss.append({"matcher": "startup|clear|compact",
                   "hooks": [{"type": "command", "command": command, "timeout": 60}]})
        added = 1
    with open(backup, "wb") as f:
        f.write(raw)
    bk = open(backup, "rb").read()
    print(f"備份：{backup}；bytes {len(bk)}；sha256 {hashlib.sha256(bk).hexdigest()}；"
          f"與原檔逐位同：{'是' if bk == raw else '否'}")
    if bk != raw:
        print("🔴 備份與原檔不同 ⇒ ⛔ 寫")
        return 2
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    d = os.path.dirname(os.path.abspath(path))
    os.makedirs(d, exist_ok=True)
    tmp = os.path.join(d, os.path.basename(path) + ".wg9366.tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)
    new = json.loads(open(path, encoding="utf-8").read())
    print(f"新檔：bytes {len(text.encode('utf-8'))}；頂層鍵 {sorted(new)}")
    print("新檔之 hooks.SessionStart：")
    print(json.dumps(new["hooks"]["SessionStart"], ensure_ascii=False, indent=2))
    print("自驗一 新檔可解：是")
    stripped = copy.deepcopy(new)
    if added:
        stripped["hooks"]["SessionStart"].pop()
        if not stripped["hooks"]["SessionStart"] and "SessionStart" not in before.get("hooks", {}):
            del stripped["hooks"]["SessionStart"]
        if not stripped["hooks"] and "hooks" not in before:
            del stripped["hooks"]
    same = stripped == before
    print(f"自驗二 除所增之一項外與原內容深相等：{'是' if same else '否'}")
    n = mine(new)
    print(f"自驗三 含本器之項：{n}")
    ok = same and n == 1
    print(f"⇒ 增 {added} 項；rc {0 if ok else 1}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
````

SELF_SHA256: b86104257c3b5457a344a31901d70903eb59f000ec1f99cdd83c92a76ce8cbf3
