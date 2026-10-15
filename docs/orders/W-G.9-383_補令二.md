# `W-G.9-383` 補令二：主線快轉（至 `fa31382`·`W-G.9-383`〔`K-9-73` ④ 與 `K-9-75`〜`K-9-77` 之落地·補令一〕入主線）＋ 主 checkout 之同步

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字；受詞 ＝ 主線之快轉、本補令與報告二新檔、主 checkout 之同步）。
> **發單** ＝ 發單側窗八十六·`2026-10-15`。**受單** ＝ CC（工項零′〜一於 **CC 之施工樹**；工項二於 **KL 之主 checkout**）。
> **所補** ＝ `docs/orders/W-G.9-383_規格單.md`（「原單」·blob `4df3a5dae75dfa8cacb25bcfc6a80f15d893174e`）之 `§四-2`（入主線之請示·另單）；`docs/orders/W-G.9-383_補令一.md`（「補令一」·`30060` B·`sha256` `7a85b9bb9dd7975bce1576ecfbbea916550a1a314a2b6bca551a3b52166e625a`）。二者皆留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `2663f559272a3a87af8821e54d20e689d3aebd5b`；側支 `verify/W-G.9-383-k975` ＝ `fa31382fab2ca953d3cce5e8d478e8166cb937b7`（原單工項四）；遠端 heads **`43`**；KL 之主 checkout 停於 `fa31382…`（detached·KL 之畫面核對之步驟·`§一` 項 `3`）。
> **級** ＝ **中**（⛔ 跑 `run_verification.py`／`run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之端；發單側窗八十六已自倉重跑原單 `V-1`〜`V-9` 與收工閘〔`§一` 項 `2`〕；KL 之畫面核對已符〔`§二`〕；收工閘唯跑量測器之 `selftest`／`wiring`）。
> 🔑 原單之一切通則照舊（直譯器名 `python`；`git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Windows 下路徑引數一律反斜線之絕對路徑；Bash 之輸出路徑一律單引號之絕對路徑；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標；`<O>` 同原單）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-383_補令二.md`·本補令）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2″`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項二之撞檔前置必觸發，依其處置（`自誤 542`）。
> 🔑 **撇號**：「″」＝ U+2033。本補令之款號（`1″` 等）與閘號（`1″` 等）唯指本補令之條。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/` 之一字（待落地清單之「`W-G.9-383` 已入主線」之更新、`自誤 620`〔補令一 `§一` 裁五〕、補令一之審查之 #9〔「聯集非空而取代未成」之支之例〕⇒ 皆併 `W-G.9-384`·`§一` 項 `4`）；側支之刪除或改寫；本地 `hold/W-G.9-383-c2`（⛔ 推·⛔ 刪）。
> 🔴 **本補令⛔ 令 CC 作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `2663f559272a3a87af8821e54d20e689d3aebd5b`；`git rev-parse origin/verify/W-G.9-383-k975` ＝ `fa31382fab2ca953d3cce5e8d478e8166cb937b7`；`git ls-remote --heads origin` 之列數 ＝ **`43`**（全列存 `<O>\heads_before_383p2.txt`·收工閘 `5″` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-383-k975` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 619 615` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `604`／`MAX` `619`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `74`／`77`／`[44, 47]`。
4. 本補令之 bytes／`sha256` 對拍 KL 所貼之訊；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。
5. `python verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單側實跑之出艙見 `§五` 項 `3`）。

### `§零-1`　停機款

| # | 款 |
|---|---|
| `1″` | 開工時主線 ≠ `2663f55`，或側支 ≠ `fa31382`，或遠端 heads ≠ `43`，或施工樹之追蹤檔有變動，或 `§零` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ `[None, None, None, None, None]` |
| `2″` | 本補令之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本補令不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3″` | 工項零′ 前置之任一期不符 |
| `4″` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（權限設定所擋者 ⇒ 停下出艙其訊息，KL 親推後續之·⛔ 改目標、⛔ `--force`） |
| `5″` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6″` | 工項零、一之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `7″` | `§三-1` 收工閘任一 ≠ 期 |
| `8″` | 工項二：主 checkout 之追蹤檔有變動；開工時其 `HEAD` ≠ `fa31382…`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9″` | CC 作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本批任一新檔為 `git check-ignore -v --no-index` 所命中 |

---

## `§一`　所據

1. **快轉之受詞**（發單側窗八十六·拋棄式 clone 實算）：`git merge-base --is-ancestor 2663f55 fa31382` 真；`git rev-list --count 2663f55..fa31382` ＝ `8`、反向 ＝ `0`；`git rev-list --merges 2663f55..fa31382` ＝ 空；`git diff --name-only 2663f55 fa31382 -- app.py ":(glob)verify/*.py"` ＝ 恰 `app.py`、`verify/selection_pipeline.py`；八筆逐筆以同式判，命中者恰 `ee60f286c42b1e17920ad14328672e69388a2876`（原單工項二·補令一之工項二′·命中 `2` 列）；`fa31382` 之追蹤檔 `2859`（框 ＝ `git ls-tree -r fa31382` 之列數）；其 `app.py` ＝ `f4cb5910b9ebaf52e1030a686a28c162a592ea3f`、`verify/selection_pipeline.py` ＝ `cf1d8e41d81ad9e17f1bc3817df58302d8207176`、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`、`verify/probes/probe_WG9363_k953.py` ＝ `083e8a0b2ecf275a7fad2992ddd60769fbedcef1`、`verify/probes/probe_WG9375_k965.py` ＝ `e68ebe10ae39bdd5a697e52315f00d8d80e995a6`、`CLAUDE.md` ＝ `98ab90dd491d4e0f40ab0f47b1208c1b7935e5f2`。
2. **側支之碼之驗**（發單側窗八十六·`2026-10-15`·倉外·⛔ 採 CC 之自報）：`fa31382` 之 `app.py` 與 `verify/` 之一切檔，與發單側之原型（補令一 `§五` 項 `4`、`5` 之樹）逐位同（`git diff` 空）⇒ 發單側於該樹之實跑即其驗：原單 `V-1`〜`V-3` 之 `52` 呼叫皆 `rc 0`、末列皆 ＝ 原單 `§五-1` 項 `8` 之施後之列（`F29` `P0 74／74`、`Y1`〜`Y11` ✅；`F23` `P0 60／60`；`F27 mutate` `無從判定 []`；`F23 run` 之 `R6@3.5`／`R6@0.0` ✅）；`stderr` 合計 `0` B；`k6s3 cmp`（前態 `a9131fb`〔其 `app.py` ≡ `2663f55`〕對其樹）二退縮 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔二退縮逐位同；`parity` 二退縮 `⇒ rc 0（不符 0 項）`、其落檔以同一字樣代 `HEAD` 後逐位同（⛔ 代之則異）·`stdout` 唯手冊先行之紀錄之列數 `34` → `37`（`3.5 m`）、`43` → `46`（`0 m`）；收工閘 `1′`〜`3′`、`4`、`6`〜`8` 發單側於 `fa31382` 自跑皆符（閘 `6` 判別力 `620 619` ⇒ `rc 7`）。
3. **KL 主 checkout**（倉外之物）：KL 依發單側窗八十六所示之步驟（`git fetch origin`；`git checkout --detach origin/verify/W-G.9-383-k975`）切至 `fa31382` 而核對畫面（`§二`）；其根或有未追蹤之 `W-G.9-383_規格單.md`、`W-G.9-383_補令一.md`（倉內之對應檔在 `docs/orders/`·路徑異 ⇒ ⛔ 撞）與本補令之來源檔。
4. **快轉之淨效**（主線 → `fa31382`·本案）：配地⛔ 變（項 `2`·`§二`）；畫面唯手冊先行之紀錄之首增再試之列三（二退縮各三·皆「未成」·原單 `§一` 項 `5`）；`K-9-73` ④ 與 `K-9-75`〜`K-9-77` 之落地（手冊先行之兩側皆配不到者之再試與同號之連通；入池閘之合併之標的〔可配得之最大一塊〕、回原狀之帳之序、再試之片之標記及其先判；再試成者之標記於單元之取代時併入單元〔補令一 `R-12`〕）、唯註之二處；量測器二器之期之更新；三簿之 `K-9-75`〜`K-9-77` 之立、`自誤 616`〜`619`、待落地清單之更新（原單工項三）。🔒 **待落地清單於本批⛔ 更新**——其「`W-G.9-383` 已入主線」之註、`自誤 620`、補令一之審查之 #9 之例，皆併 `W-G.9-384`（KL 之效率之令·純登記⛔ 單出）。

---

## `§二`　放行（KL 之逐字）

**入主線之請示**（發單側窗八十六於對話所呈·`2026-10-15`）：附畫面核對之步驟（退縮 `3.5 m`／`0 m`·手冊先行之紀錄之首增再試之列三·皆「未成」·總列數 `37`／`46`·其餘與主線之端同），並明載：核對無誤後回覆放行之原話，發單側依 `W-G.9-382` 補令二之前例發「主線快轉＋主 checkout 同步」之補令二。

**KL 之語**（`2026-10-15 14:40`·`Asia/Taipei`·逐字）：「383 畫面核對無誤，准入主線」

🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一`）：所答之請示已明載本批之生產碼與其土地後果（本案配地⛔ 變·唯手冊先行之紀錄增再試之列三）⇒ **為工項零′（主線快轉）與工項二（主 checkout 之同步）之放行**；CC 將本節之 KL 之逐字載入報告。

| `commit`（全 `40` 碼） | 首列 | 生產碼 | 所據 | 土地後果 |
|---|---|---|---|---|
| `ee60f286c42b1e17920ad14328672e69388a2876` | `W-G.9-383 工項二：K-9-73 ④·K-9-75〜K-9-77 之落地（手冊先行之兩側皆配不到者之再試與同號之連通·入池閘之合併之標的與回原狀之帳之序與再試之片之標記及其先判·試算之回傳增 dropped）＋ 唯註之二處 🔴 生產碼（新側支）` | `app.py`、`verify/selection_pipeline.py` | 原單 `§三`；補令一 `§一` 裁一〜三、`§二` | 本案配地⛔ 變（`§一` 項 `2`） |

🛑 **射程**：`(a)` 主線快轉至 `fa31382fab2ca953d3cce5e8d478e8166cb937b7`（工項零′·**以前置皆符為條件**）；`(b)` 工項零、一（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項二於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、`verify/`、任何錨、四簿、`CLAUDE.md`、`.claude/`。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：
1. `git merge-base --is-ancestor 2663f559272a3a87af8821e54d20e689d3aebd5b fa31382fab2ca953d3cce5e8d478e8166cb937b7` ⇒ `rc 0`；`git rev-list --count 2663f55..fa31382` ＝ `8`；`git rev-list --count fa31382..2663f55` ＝ `0`；`git rev-list --merges 2663f55..fa31382` ＝ 空。
2. `git diff --name-only 2663f55 fa31382 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `2` 列：`app.py`、`verify/selection_pipeline.py`（🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 之檔）；`git rev-parse fa31382:app.py` ＝ `f4cb5910b9ebaf52e1030a686a28c162a592ea3f`；`git rev-parse fa31382:verify/selection_pipeline.py` ＝ `cf1d8e41d81ad9e17f1bc3817df58302d8207176`；`git rev-parse fa31382:verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`。
3. `git rev-list 2663f55..fa31382` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `commit`（`ee60f28…`·命中 `2` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3″`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：

```
git push origin fa31382fab2ca953d3cce5e8d478e8166cb937b7:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4″`）；⛔ 改目標值（逐字 `fa31382fab2ca953d3cce5e8d478e8166cb937b7`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-383-k975`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5″`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `fa31382fab2ca953d3cce5e8d478e8166cb937b7`；
② 遠端 heads ＝ **`43`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `fa31382` 之相異 ＝ **`0`**；判別力［必非零］：vs `2663f55` 之相異 ＝ **`2`**（`app.py`、`verify/selection_pipeline.py`）；
④ `git branch -r --contains ee60f286c42b1e17920ad14328672e69388a2876` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-383-k975`）。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `fa31382…` 方續工項零。

### 工項零　本補令原封入倉（主線·零生產碼）

`docs/orders/W-G.9-383_補令二.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-383 補令二 工項零：本補令原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　執行報告入倉（主線·新檔 `docs/reports/W-G.9-383R_入主線_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1″`〜`9″` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ `§二` 之放行（KL 之逐字）；⑤ pre-flight 之出艙與逐項之處置；⑥ CC 之自捕與自解；⑦ 各段耗時。收工閘之實測值與工項二之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-383 補令二 工項一：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> rev-parse HEAD` ＝ `fa31382fab2ca953d3cce5e8d478e8166cb937b7`（`§一` 項 `3`）；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次將新入之路徑集 `A`（期 ＝ 本補令、報告）；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8″`）；不等 ⇒ 停機款 `8″`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項一 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `f4cb5910b9ebaf52e1030a686a28c162a592ea3f`；`… hash-object verify/selection_pipeline.py` ＝ `cf1d8e41d81ad9e17f1bc3817df58302d8207176`；`… hash-object verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`；`… hash-object verify/probes/probe_WG9363_k953.py` ＝ `083e8a0b2ecf275a7fad2992ddd60769fbedcef1`；`… hash-object verify/probes/probe_WG9375_k965.py` ＝ `e68ebe10ae39bdd5a697e52315f00d8d80e995a6`；`… hash-object CLAUDE.md` ＝ `98ab90dd491d4e0f40ab0f47b1208c1b7935e5f2`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。

任一不符 ⇒ 停機款 `8″`·⛔ 動、回報實值。主 checkout 之根之未追蹤之單（原單、補令一、本補令之來源檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## `§三-1`　收工閘（工項一之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1″` | 本批二筆 `commit`（工項零、一）之增刪（`git show --numstat`） | 工項零 ＝ 本補令之增／`0`；工項一 ＝ 報告之增／`0`；二筆之首列 ＝ `§三` 所令逐字 |
| `2″` | `git diff --name-status fa31382 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`2`** 列：`A` 本補令、`A` 報告；生產碼與 `verify/` 之一切檔對 `fa31382` 相異 **`0`**；判別力［必非零］：生產碼對 `2663f55` 相異 **`2`**（`app.py`、`verify/selection_pipeline.py`）；二新檔之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3″` | 二新檔之 `CR`（真 `0x0D`·受詞 ＝ 主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`** |
| `4″` | 四簿、`CLAUDE.md`、`.claude/` | 對 `fa31382` 相異 **`0`**（閘 `2″` 之二列以外無他檔即證之；另 `git rev-parse HEAD:CLAUDE.md` ＝ `98ab90dd491d4e0f40ab0f47b1208c1b7935e5f2`） |
| `5″` | 自限 | 遠端 heads **`43`**；主線 ＝ 工項一之 `commit`，其祖含 `fa31382`；側支 `verify/W-G.9-383-k975` ＝ `fa31382…`（⛔ 變）；其餘 `41` 列（除 `wip/s1-endpart` 與該側支）逐列 ＝ `<O>\heads_before_383p2.txt` |
| `6″` | `python verify/probes/probe_WG9270_closegate.py 619 615 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 620 619 .` ⇒ `rc 7` |
| `7″` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 619 615` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零` 項 `3` 之值（⛔ 變） |
| `8″` | 量測器（於主線之端）：`python verify/probes/probe_WG9375_k965.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`python verify/probes/probe_WG9373_k966.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>`；`python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`；`python verify/probes/probe_WG9367_adj4.py selftest <repo>` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`P0` ＝ `74／74`（`F29`）、`60／60`（`F23`）、`31／31`（`F27`）、`29／29`（`F28`）、`86／86`（`F14`）、`28／28`（`F24`）；`F29 wiring` `Y1`〜`Y11` ✅、`F27 wiring` `Y1`〜`Y9` ✅；`stderr` 合計 `0` B |

---

## `§四`　土地後果

**本案**：配地⛔ 變；主線之畫面唯手冊先行之紀錄之首增再試之列三（二退縮各三·皆「未成」·原單 `§一` 項 `5`）。**他案**：主線自此依 `K-9-73` ④ 與 `K-9-75`〜`K-9-77`（同一筆跨分配線、兩側皆配不到者，餘片整筆併入應分配面積最大之一側再試；同街廓之合併之標的 ＝ 可配得之最大一塊；回原狀後依應分配面積大者先；再試之序依 `K-9-77`）。

---

## `§五`　驗收之基數（發單側窗八十六以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 快轉之受詞 | `§一` 項 `1`；新名之占用（母體 ＝ `fa31382` 之追蹤檔 `2859` 檔·`git grep -l -F`）：`W-G.9-383_補令二` ＝ `0`、`W-G.9-383R_入主線` ＝ `0` ⇒ 可取 |
| `3` | pre-flight | `python verify/probes/probe_order_preflight.py <本補令>`·發單側窗八十六實跑（態 `fa31382`·定稿）：🔴 機械 `0` 項／🟡 提示 `1` 項——`P-2` `:43`（`§一` 項 `1` 之計數皆為 git 之物件之計數〔`rev-list --count`、`diff --name-only`、`ls-tree -r`〕，非號之占用之框；`CLAUDE.md:723`〜`:726` 之錨定框與二數並報之規⛔ 及之；號之占用唯本表項 `2`〔完整之名·`git grep -l -F`〕⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕·本補令⛔ 用） |
| `4` | 模擬（拋棄式 worktree `fa31382`·⛔ push·工項零′ 與閘 `5″` 須遠端⛔ 模擬） | 工項零 ＋ 工項一（報告之替身）二 `commit`：閘 `1″` 首列逐字·增刪 ＝ 本補令之增／`0`、替身 `1`／`0`；閘 `2″` 恰二 `A`·生產碼與 `verify/` 對 `fa31382` 相異 `0`、生產碼對 `2663f55` 恰 `app.py`、`verify/selection_pipeline.py`·二新檔 `git check-ignore -v --no-index` 無命中（`rc 1`）·對照 `rc 0`（`.gitignore:18:__pycache__/`）；閘 `3″` `CR` `0`（對照 `12308`）；閘 `4″` `CLAUDE.md` ＝ `98ab90dd…`；閘 `6″` `✅ 二閘皆過`·判別力 `620 619` ⇒ `rc 7`；閘 `7″` `rc 0`·四簿之值 ＝ `§零` 項 `3`；閘 `8″` 九呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`P0` `74／74`、`60／60`、`31／31`、`29／29`、`86／86`、`28／28`·`stderr` `0` B |

SELF_SHA256: b39ab533d04a633d937abe05f79354a56a350eab09c18270af5b69a1d1d645e1
