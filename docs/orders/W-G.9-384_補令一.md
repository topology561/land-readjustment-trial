# `W-G.9-384` 補令一：主線快轉（至 `663a457`·`W-G.9-384`〔`K-9-71` 之落地〕入主線）＋ 主 checkout 之同步

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字；受詞 ＝ 主線之快轉、本補令與報告二新檔、主 checkout 之同步）。
> **發單** ＝ 發單側窗八十七·`2026-10-16`。**受單** ＝ CC（工項零′〜一於 **CC 之施工樹**；工項二於 **KL 之主 checkout**）。
> **所補** ＝ `docs/orders/W-G.9-384_規格單.md`（「原單」·`126432` B·`sha256` `42668484a2f3cde92816021a46f8cf2364d4c39620b5aeb85cb38d881f356082`）之 `§四-2`（入主線之請示·另單）。原單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`；側支 `verify/W-G.9-384-k971` ＝ `663a457bb111a27e694038b2cdd22cb5c1dc8807`（原單工項四）；遠端 heads **`44`**；KL 之主 checkout 停於 `663a457…`（detached·KL 之畫面核對之步驟·`§一` 項 `3`）。
> **級** ＝ **中**（⛔ 跑 `run_verification.py`／`run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之端；發單側窗八十七已自倉重跑原單 `V-1`〜`V-9` 與收工閘〔`§一` 項 `2`〕；KL 之畫面核對已符〔`§二`〕；收工閘唯跑量測器之 `selftest`／`wiring`）。
> 🔑 原單之一切通則照舊（直譯器名 `python`；`git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Windows 下路徑引數一律反斜線之絕對路徑；Bash 之輸出路徑一律單引號之絕對路徑；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標；`<O>` 同原單）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-384_補令一.md`·本補令）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2″`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項二之撞檔前置必觸發，依其處置（`自誤 542`）。
> 🔑 **撇號**：「″」＝ U+2033。本補令之款號（`1″` 等）與閘號（`1″` 等）唯指本補令之條。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/` 之一字（待落地清單之「`W-G.9-384` 已入主線」之更新、原單之唯讀審查之 (丙) 二〔手冊先行之道路之片之再排無判別力〕之例 ⇒ 皆併 `W-G.9-385`·`§一` 項 `4`）；側支之刪除或改寫。
> 🔴 **本補令⛔ 令 CC 作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`；`git rev-parse origin/verify/W-G.9-384-k971` ＝ `663a457bb111a27e694038b2cdd22cb5c1dc8807`；`git ls-remote --heads origin` 之列數 ＝ **`44`**（全列存 `<O>\heads_before_384p1.txt`·收工閘 `5″` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-384-k971` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 620 619` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `605`／`MAX` `620`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `75`／`78`／`[44, 47]`。
4. 本補令之 bytes／`sha256` 對拍 KL 所貼之訊；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。
5. `python verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單側實跑之出艙見 `§五` 項 `3`）。

### `§零-1`　停機款

| # | 款 |
|---|---|
| `1″` | 開工時主線 ≠ `fffa397`，或側支 ≠ `663a457`，或遠端 heads ≠ `44`，或施工樹之追蹤檔有變動，或 `§零` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ `[None, None, None, None, None]` |
| `2″` | 本補令之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本補令不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3″` | 工項零′ 前置之任一期不符 |
| `4″` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（權限設定所擋者 ⇒ 停下出艙其訊息，KL 親推後續之·⛔ 改目標、⛔ `--force`） |
| `5″` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6″` | 工項零、一之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `7″` | `§三-1` 收工閘任一 ≠ 期 |
| `8″` | 工項二：主 checkout 之追蹤檔有變動；開工時其 `HEAD` ≠ `663a457…`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9″` | CC 作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本批任一新檔為 `git check-ignore -v --no-index` 所命中 |

---

## `§一`　所據

1. **快轉之受詞**（發單側窗八十七·拋棄式 clone 實算）：`git merge-base --is-ancestor fffa397 663a457` 真；`git rev-list --count fffa397..663a457` ＝ `5`、反向 ＝ `0`；`git rev-list --merges fffa397..663a457` ＝ 空；`git diff --name-only fffa397 663a457 -- app.py ":(glob)verify/*.py"` ＝ 恰 `app.py`、`verify/selection_pipeline.py`；五筆逐筆以同式判，命中者恰 `8ce1a1828ee8b0a9991d05c91ef3b48c06fee401`（原單工項二·命中 `2` 列）；`663a457` 之追蹤檔 `2864`（框 ＝ `git ls-tree -r 663a457` 之列數）；其 `app.py` ＝ `261c5ac99f2b3b6e19152a689156378242d4c3a7`、`verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`、`verify/probes/probe_WG9363_k953.py` ＝ `abe2f7fabe818bda5b71ef41a8b59aa3335be85b`、`verify/probes/probe_WG9357_k948.py` ＝ `e5a867a2eede82090e5889842d450a026481e139`、`CLAUDE.md` ＝ `d1b1a1f2a6ee56fcdb7c9f65fd288be38b73e86c`。
2. **側支之碼之驗**（發單側窗八十七·`2026-10-16`·倉外·⛔ 採 CC 之自報）：側支之端之生產碼係 CC 依原單 `§三` 所撰（與發單側之原型異·屬規格單之流程），發單側逐條對 `R-1`〜`R-10` 讀之（`k971_key5` 之 `r2`／`r5` 之分支與 `adj_candidate_lists` 代數同式；再排之置處、三支之鍵、惰取之條件〔相異街廓數〕、二停機、二回呼之六引數之源、六入口皆合）；於拋棄式 worktree（`663a457`）重跑原單 `V-1`〜`V-2` 之 `52` 呼叫：皆 `rc 0`、末列皆 ＝ 原單 `§五-1` 項 `8` 之施後之列（與發單側之原型逐列同；`F23` `P0 74／74`、`W1`〜`W9` ✅；`F16` `P0 35／35`；`F29` `P0 74／74`；`F27 mutate` `無從判定 []`）；`stderr` 合計 `0` B；`k6s3 cmp`（前態 ＝ `fffa397` ＋ 塊 `Fy34`〔≡ 原單工項一之端 `b47efbc`〕對 `663a457`）二退縮 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔二退縮前後逐位同；`parity` 二退縮 `⇒ rc 0（不符 0 項）`、其落檔與 `stdout` 以同一字樣代 `HEAD` 後逐位同（⛔ 代之則異）·配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·手冊先行 session 鍵 `f3_k953_log` `37`／`46` 列；倉外之小器於 `663a457` 二退縮：段三後處理之第 `5` 項之列 `0`、末端塊合併再試之紀錄 `0` 列、手冊先行之 `K-9-51` 之列 `0`、五級之屬性之回呼之呼數 `0`；收工閘 `1`〜`4`、`6`〜`8` 發單側於 `663a457` 自跑皆符（閘 `6` 判別力 `621 620` ⇒ `rc 7`；`15` 檔之 `CR` `0`；三簿改前皆為改後之嚴格前綴）；五筆之首列 ＝ 原單所令逐字。
3. **KL 主 checkout**（倉外之物）：KL 依發單側窗八十七所示之步驟（`git fetch`；`git checkout --detach origin/verify/W-G.9-384-k971`）切至 `663a457` 而核對畫面（`§二`）；其根或有未追蹤之 `W-G.9-384_規格單.md`（CC 之原單之來源·倉內之對應檔在 `docs/orders/`·路徑異 ⇒ ⛔ 撞）、`W-G.9-383_*.md` 之舊單與本補令之來源檔。
4. **快轉之淨效**（主線 → `663a457`·本案）：配地⛔ 變（項 `2`·`§二`）；畫面⛔ 變（`K-9-71` 於本案⛔ 觸）；`K-9-71` 之落地（段三後處理之第 `5` 項之輪與手冊先行之 `K-9-51` 之輪：建地之片之候選依本街廓 → 五級與深度 → 距離；五級之屬性 ＝ 調配之名單之同一處·`blk5` 與六入口）；量測器七器之期之更新；三簿之 `K-9-78` 之立、`K-9-71` 之落地之讀法、`自誤 620`、待落地清單之更新（原單工項三）。🔒 **待落地清單於本批⛔ 更新**——其「`W-G.9-384` 已入主線」之註、原單之唯讀審查之 (丙) 二之例，皆併 `W-G.9-385`（KL 之效率之令·純登記⛔ 單出）。

---

## `§二`　放行（KL 之逐字）

**入主線之請示**（發單側窗八十七於對話所呈·`2026-10-16`）：附發單側自倉復驗之結果與畫面核對之步驟（全新視窗·先退縮 `3.5 m`、再以另一全新視窗 `0 m`·依序按「執行第 1 宗街角地優先權選位」、「🧮 執行 G 值迭代計算」·應見 ＝ 主線之端·配地、抵費地與各段紀錄⛔ 變·手冊先行之紀錄 `37`／`46` 列），並明載逐字「核對無誤的話，請回覆准入主線。我收到後再出補令，把主線快轉到這個版本，並同步你的主 checkout。」

**KL 之語**（`2026-10-16 11:19`·`Asia/Taipei`·逐字）：「核對無誤」

🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一`）：KL 之語係答上開之請示——其請示以「核對無誤」為放行之條件、並明載本批之生產碼與其土地後果（本案配地⛔ 變）⇒ 發單側讀為 **工項零′（主線快轉）與工項二（主 checkout 之同步）之放行**（`W-G.9-381` 之前例：KL `2026-10-13 16:04`「是，畫面核對無誤(16:04)，續擬W-G.9-381」）；本補令由 KL 貼予 CC 即其確認。CC 將本節之 KL 之逐字載入報告。

| `commit`（全 `40` 碼） | 首列 | 生產碼 | 所據 | 土地後果 |
|---|---|---|---|---|
| `8ce1a1828ee8b0a9991d05c91ef3b48c06fee401` | `W-G.9-384 工項二：K-9-71 之落地（段三後處理之第 5 項之輪與手冊先行之 K-9-51 之輪：建地之片之候選依本街廓 → 五級與深度 → 距離；五級之屬性 ＝ 調配之名單之同一處·blk5 與六入口）🔴 生產碼（新側支）` | `app.py`、`verify/selection_pipeline.py` | 原單 `§三` | 本案配地⛔ 變（`§一` 項 `2`） |

🛑 **射程**：`(a)` 主線快轉至 `663a457bb111a27e694038b2cdd22cb5c1dc8807`（工項零′·**以前置皆符為條件**）；`(b)` 工項零、一（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項二於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、`verify/`、任何錨、四簿、`CLAUDE.md`、`.claude/`。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：
1. `git merge-base --is-ancestor fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c 663a457bb111a27e694038b2cdd22cb5c1dc8807` ⇒ `rc 0`；`git rev-list --count fffa397..663a457` ＝ `5`；`git rev-list --count 663a457..fffa397` ＝ `0`；`git rev-list --merges fffa397..663a457` ＝ 空。
2. `git diff --name-only fffa397 663a457 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `2` 列：`app.py`、`verify/selection_pipeline.py`（🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 之檔）；`git rev-parse 663a457:app.py` ＝ `261c5ac99f2b3b6e19152a689156378242d4c3a7`；`git rev-parse 663a457:verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`；`git rev-parse 663a457:verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`。
3. `git rev-list fffa397..663a457` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `commit`（`8ce1a18…`·命中 `2` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3″`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：

```
git push origin 663a457bb111a27e694038b2cdd22cb5c1dc8807:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4″`）；⛔ 改目標值（逐字 `663a457bb111a27e694038b2cdd22cb5c1dc8807`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-384-k971`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5″`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `663a457bb111a27e694038b2cdd22cb5c1dc8807`；
② 遠端 heads ＝ **`44`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `663a457` 之相異 ＝ **`0`**；判別力［必非零］：vs `fffa397` 之相異 ＝ **`2`**（`app.py`、`verify/selection_pipeline.py`）；
④ `git branch -r --contains 8ce1a1828ee8b0a9991d05c91ef3b48c06fee401` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-384-k971`）。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `663a457…` 方續工項零。

### 工項零　本補令原封入倉（主線·零生產碼）

`docs/orders/W-G.9-384_補令一.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-384 補令一 工項零：本補令原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　執行報告入倉（主線·新檔 `docs/reports/W-G.9-384R_入主線_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1″`〜`9″` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ `§二` 之放行（KL 之逐字）；⑤ pre-flight 之出艙與逐項之處置；⑥ CC 之自捕與自解；⑦ 各段耗時。收工閘之實測值與工項二之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-384 補令一 工項一：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> rev-parse HEAD` ＝ `663a457bb111a27e694038b2cdd22cb5c1dc8807`（`§一` 項 `3`）；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次將新入之路徑集 `A`（期 ＝ 本補令、報告）；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8″`）；不等 ⇒ 停機款 `8″`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項一 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `261c5ac99f2b3b6e19152a689156378242d4c3a7`；`… hash-object verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`；`… hash-object verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`；`… hash-object verify/probes/probe_WG9363_k953.py` ＝ `abe2f7fabe818bda5b71ef41a8b59aa3335be85b`；`… hash-object verify/probes/probe_WG9357_k948.py` ＝ `e5a867a2eede82090e5889842d450a026481e139`；`… hash-object CLAUDE.md` ＝ `d1b1a1f2a6ee56fcdb7c9f65fd288be38b73e86c`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。

任一不符 ⇒ 停機款 `8″`·⛔ 動、回報實值。主 checkout 之根之未追蹤之單（原單、`W-G.9-383_*.md` 之舊單、本補令之來源檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## `§三-1`　收工閘（工項一之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1″` | 本批二筆 `commit`（工項零、一）之增刪（`git show --numstat`） | 工項零 ＝ 本補令之增／`0`；工項一 ＝ 報告之增／`0`；二筆之首列 ＝ `§三` 所令逐字 |
| `2″` | `git diff --name-status 663a457 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`2`** 列：`A` 本補令、`A` 報告；生產碼與 `verify/` 之一切檔對 `663a457` 相異 **`0`**；判別力［必非零］：生產碼對 `fffa397` 相異 **`2`**（`app.py`、`verify/selection_pipeline.py`）；二新檔之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3″` | 二新檔之 `CR`（真 `0x0D`·受詞 ＝ 主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`** |
| `4″` | 四簿、`CLAUDE.md`、`.claude/` | 對 `663a457` 相異 **`0`**（閘 `2″` 之二列以外無他檔即證之；另 `git rev-parse HEAD:CLAUDE.md` ＝ `d1b1a1f2a6ee56fcdb7c9f65fd288be38b73e86c`） |
| `5″` | 自限 | 遠端 heads **`44`**；主線 ＝ 工項一之 `commit`，其祖含 `663a457`；側支 `verify/W-G.9-384-k971` ＝ `663a457…`（⛔ 變）；其餘 `42` 列（除 `wip/s1-endpart` 與該側支）逐列 ＝ `<O>\heads_before_384p1.txt` |
| `6″` | `python verify/probes/probe_WG9270_closegate.py 620 619 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 621 620 .` ⇒ `rc 7` |
| `7″` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 620 619` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零` 項 `3` 之值（⛔ 變） |
| `8″` | 量測器（於主線之端）：`python verify/probes/probe_WG9375_k965.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`python verify/probes/probe_WG9357_k948.py selftest <repo>`；`python verify/probes/probe_WG9373_k966.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>`；`python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`；`python verify/probes/probe_WG9367_adj4.py selftest <repo>` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`P0` ＝ `74／74`（`F29`）、`74／74`（`F23`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）、`86／86`（`F14`）、`28／28`（`F24`）；`F29 wiring` `Y1`〜`Y11` ✅、`F27 wiring` `Y1`〜`Y9` ✅；`stderr` 合計 `0` B |

---

## `§四`　土地後果

**本案**：配地⛔ 變；畫面⛔ 變（`K-9-71` 於本案⛔ 觸·原單 `§一` 項 `5`）。**他案**：主線自此依 `K-9-71`（同一地主之剩餘土地依距離併入其他處已配得之宗時，建地：本街廓者先；他街廓者先依五級與深度、相同始依距離；道路用地、公設地上之土地仍只依距離）。

---

## `§五`　驗收之基數（發單側窗八十七以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 快轉之受詞 | `§一` 項 `1`；新名之占用（母體 ＝ `663a457` 之追蹤檔 `2864` 檔·`git grep -l -F`）：`W-G.9-384_補令一` ＝ `0`、`W-G.9-384R_入主線` ＝ `0` ⇒ 可取 |
| `3` | pre-flight | `python verify/probes/probe_order_preflight.py <本補令>`·發單側窗八十七實跑（態 `663a457`·定稿）：🔴 機械 `0` 項／🟡 提示 `2` 項——皆 `:43`（`§一` 之一段）：`P-2`（其計數皆為 git 之物件之計數〔`rev-list --count`、`diff --name-only`、`ls-tree -r`〕，非號之占用之框；`CLAUDE.md:723`〜`:726` 之錨定框與二數並報之規⛔ 及之；號之占用唯本表項 `2`〔完整之名·`git grep -l -F`〕⇒ **具名豁免**）、`P-4`（其箭頭係快轉之方向〔主線 → `663a457`〕與候選之序〔本街廓 → 五級與深度 → 距離〕之述，座標系 ＝ 自開工態至快轉後·同段自載 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕·本補令⛔ 用） |
| `4` | 模擬（拋棄式 worktree `663a457`·⛔ push·工項零′ 與閘 `5″` 須遠端⛔ 模擬） | 工項零 ＋ 工項一（報告之替身）二 `commit`：閘 `1″` 首列逐字·增刪 ＝ 本補令之增（`146`）／`0`、替身 `1`／`0`；閘 `2″` 恰二 `A`·生產碼與 `verify/` 對 `663a457` 相異 `0`、生產碼對 `fffa397` 恰 `app.py`、`verify/selection_pipeline.py`·二新檔 `git check-ignore -v --no-index` 無命中（`rc 1`）·對照 `rc 0`（`.gitignore:18:__pycache__/`）；閘 `3″` `CR` `0`（對照 `12308`）；閘 `4″` `CLAUDE.md` ＝ `d1b1a1f2…`；閘 `6″` `✅ 二閘皆過`·判別力 `621 620` ⇒ `rc 7`；閘 `7″` `rc 0`·四簿之值 ＝ `§零` 項 `3`；閘 `8″` 十呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`P0` `74／74`（`F29`）、`74／74`（`F23`）、`35／35`（`F16`）、`31／31`、`29／29`、`86／86`、`28／28`·`stderr` `0` B；結束時 `git status --porcelain` 空 |

SELF_SHA256: 5b31c50d120c6b77a2bf4395cf115ac975698fcd3ef246e09f40fa196ea63ae8
