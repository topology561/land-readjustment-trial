# `W-G.9-382` 補令二：主線快轉（至 `32f70d6`·`W-G.9-382`〔`K-9-73` 之落地·補令一〕入主線）＋ 主 checkout 之同步

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字；受詞 ＝ 主線之快轉、本補令與報告二新檔、主 checkout 之同步）。
> **發單** ＝ 發單側窗八十四·`2026-10-14`。**受單** ＝ CC（工項零′〜一於 **CC 之施工樹**；工項二於 **KL 之主 checkout**）。
> **所補** ＝ `docs/orders/W-G.9-382_規格單.md`（「原單」·blob `30dda4af23c2b257465d2ba250bc0f2e4c3c7f66`）之 `§四-2`（入主線之請示·另單）；`docs/orders/W-G.9-382_補令一.md`（「補令一」·`14464` B·`sha256` `a2e477fba65451e39eaa22fcf29b715e6cf406c4f63272d575dbf3432869e838`）。二者皆留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `0587ea487d3ad0f6eeff3c3687997650d819f3b3`；側支 `verify/W-G.9-382-k973` ＝ `32f70d69ba23add4e46776c3629a0a301ae19af6`（原單工項四）；遠端 heads **`42`**；KL 之主 checkout 停於 `32f70d6…`（detached·KL 之畫面核對之步驟·`§一` 項 `3`）。
> **級** ＝ **中**（⛔ 跑 `run_verification.py`／`run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之端；發單側窗八十四已自倉重跑原單之 `V-1`〜`V-9` 與收工閘〔`§一` 項 `2`〕；KL 之畫面核對已符〔`§二`〕；收工閘唯跑量測器之 `selftest`／`wiring`）。
> 🔑 原單之一切通則照舊（直譯器名 `python`；`git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Windows 下路徑引數一律反斜線之絕對路徑；Bash 之輸出路徑一律單引號之絕對路徑；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標；`<O>` 同原單）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-382_補令二.md`·本補令）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2″`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項二之撞檔前置必觸發，依其處置（`自誤 542`）。
> 🔑 **撇號**：「″」＝ U+2033。本補令之款號（`1″` 等）與閘號（`1″` 等）唯指本補令之條。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/` 之一字（待落地清單之「`W-G.9-382` 已入主線」之更新、`自誤 616`〔補令一 `§一` 裁三〕、補令一裁二之 C-1 ⇒ 皆併 `W-G.9-383`·`§一` 項 `4`）；側支之刪除或改寫；本地 `hold/W-G.9-382-c2`（⛔ 推·⛔ 動）。
> 🔴 **本補令⛔ 令 CC 作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `0587ea487d3ad0f6eeff3c3687997650d819f3b3`；`git rev-parse origin/verify/W-G.9-382-k973` ＝ `32f70d69ba23add4e46776c3629a0a301ae19af6`；`git ls-remote --heads origin` 之列數 ＝ **`42`**（全列存 `<O>\heads_before_382p2.txt`·收工閘 `5″` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-382-k973` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 615 612` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `600`／`MAX` `615`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `71`／`74`／`[44, 47]`（＝ 原單收工閘 `7` 之期·發單側窗八十四於 `32f70d6` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 KL 所貼之訊；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。KL 之訊未載或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。
5. `python verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單側實跑之出艙見 `§五` 項 `3`）。

### `§零-1`　停機款

| # | 款 |
|---|---|
| `1″` | 開工時主線 ≠ `0587ea4`，或側支 ≠ `32f70d6`，或遠端 heads ≠ `42`，或施工樹之追蹤檔有變動，或 `§零` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ `[None, None, None, None, None]` |
| `2″` | 本補令之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本補令不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3″` | 工項零′ 前置之任一期不符 |
| `4″` | 工項零′ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（權限設定所擋者 ⇒ 停下出艙其訊息，KL 親推後續之·⛔ 改目標、⛔ `--force`） |
| `5″` | 工項零′ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6″` | 工項零、一之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `7″` | `§三` 收工閘任一 ≠ 期 |
| `8″` | 工項二：主 checkout 之追蹤檔有變動；開工時其 `HEAD` ≠ `32f70d6…`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；切至 `wip/s1-endpart` 被拒；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9″` | CC 作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本批任一新檔為 `git check-ignore -v --no-index` 所命中 |

---

## `§一`　所據

1. **快轉之受詞**（發單側窗八十四·拋棄式 clone 實算）：`git merge-base --is-ancestor 0587ea4 32f70d6` 真；`git rev-list --count 0587ea4..32f70d6` ＝ `7`、反向 ＝ `0`；`git rev-list --merges 0587ea4..32f70d6` ＝ 空；`git diff --name-only 0587ea4 32f70d6 -- app.py ":(glob)verify/*.py"` ＝ 恰 `app.py`；七筆逐筆以同式判，命中者恰 `7ec63f9eced8f0e436a83d149ad7c22487455a50`（原單工項二′·補令一）；`32f70d6` 之追蹤檔 `2851`；其 `app.py` ＝ `48bb05ae97c4b20c8447716313e1b6c74fef3a7a`、`verify/selection_pipeline.py` ＝ `cff92d11d4e03c9f9db8d3de590290d3cb44f80d`、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`、`verify/probes/probe_WG9375_k965.py` ＝ `10abeb049580ef607103e33266d7f9fa57ff3638`、`CLAUDE.md` ＝ `76d57b26123173ec7c5775daab1615d197a664eb`。
2. **側支之碼之驗**（發單側窗八十四·`2026-10-14`·倉外·⛔ 採 CC 之自報）：於 `32f70d6` 之拋棄式工作樹重跑原單 `V-1`〜`V-3` 之 `52` 呼叫——皆 `rc 0`、末列皆 ＝ 原單 `§五-1` 項 `10` 之施後之列（`F29` `P0 61／61`、`Y1`〜`Y11` ✅；`F23` `P0 48／48`；`F23 run` 之 `R5@3.5`／`R5@0.0` ✅）；`stderr` 合計 `0` B；`k6s3 cmp`（前態 `0587ea4`〔其 `app.py` 與 `k6s3`／`F8`／`parity` 三器 ≡ 工項一之端〕對 `32f70d6`）二退縮 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔二退縮逐位同；`parity` 二退縮 `⇒ rc 0（不符 0 項）`、其落檔與 `stdout` 以同一字樣代 `HEAD` 與工作樹之路徑後逐位同（⛔ 代之則異）·配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`；`V-7` 唯 `app.py`、`V-8` ＝ 前八者無出艙·「（第31條第3款）」`app.py:1`；收工閘 `1′`〜`3′`、`4`、`6`〜`8` 皆符；`app.py` 之差異逐條對原單 `R-1`〜`R-6` 審之皆合。
3. **KL 主 checkout**（倉外之物）：KL 依發單側窗八十四所示之步驟（`git fetch origin`；`git checkout --detach origin/verify/W-G.9-382-k973`）切至 `32f70d6` 而核對畫面（`§二`）；其根有未追蹤之 `W-G.9-382_規格單.md`、`W-G.9-382_補令一.md`（倉內之對應檔在 `docs/orders/`·路徑異 ⇒ ⛔ 撞）與本補令之來源檔。
4. **快轉之淨效**（主線 → `32f70d6`·本案）：配地⛔ 變（項 `2`·`§二`）；畫面唯手冊先行之紀錄之「依據」欄之字面變（`3.5 m` `7` 列、`0 m` `8` 列·原單 `§一` 項 `5`）；`K-9-73` 之落地（入池閘唯處同街廓；手冊先行之計畫之序 ＝ 第 31 條第 3 款〔唯同一原地號〕→ 道路用地分配原則 → 同街廓相鄰者）、唯註之二處；量測器五器之期之更新；三簿之 `K-9-73`／`K-9-74` 之立、`K-9-72` 之逐款對照之結果、`自誤 613`〜`615`、待落地清單之更新（原單工項三）。🔒 **待落地清單於本批⛔ 更新**——其「`W-G.9-382` 已入主線」之註、`自誤 616`、C-1 之 docstring 二處，皆併 `W-G.9-383` 之工項一（KL 之效率之令·純登記⛔ 單出）。

---

## `§二`　放行（KL 之逐字）

**入主線之請示**（發單側窗八十四於對話所呈·`2026-10-14`）之【要你判斷】逐字：「核對相符，是否同意 `W-G.9-382` 入主線？請回覆「同意 W-G.9-382 入主線」。」；同訊明載：放行後以本補令「主線快轉至 `32f70d6`，並同步主 checkout」。

**KL 之語**（`2026-10-14 10:38`·`Asia/Taipei`·逐字）：「核對相符，同意 W-G.9-382 入主線」

🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一`）：所答之問已明載生產碼之 `commit`（`7ec63f9`·唯一）與其土地後果（本案配地⛔ 變·唯「依據」欄之字面）⇒ **為工項零′（主線快轉）與工項二（主 checkout 之同步）之放行**；CC 將本節之 KL 之逐字載入報告。

| `commit`（全 `40` 碼） | 首列 | 生產碼 | 所據 | 土地後果 |
|---|---|---|---|---|
| `7ec63f9eced8f0e436a83d149ad7c22487455a50` | `W-G.9-382 工項二：K-9-73 之落地（入池閘唯處同街廓·同街廓之已配得之宗依應分配面積大者先·N0-9 之片亦判之；手冊先行之計畫之序 ＝ 第 31 條第 3 款〔唯同一原地號〕→ 道路用地分配原則 → 同街廓相鄰者）＋ 唯註之二處 🔴 生產碼（新側支）` | `app.py` | 原單 `§三`；補令一 `§一` 裁一、`§二` | 本案配地⛔ 變（`§一` 項 `2`） |

🛑 **射程**：`(a)` 主線快轉至 `32f70d69ba23add4e46776c3629a0a301ae19af6`（工項零′·**以前置皆符為條件**）；`(b)` 工項零、一（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項二於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` ⛔ 及生產碼、`verify/`、任何錨、四簿、`CLAUDE.md`、`.claude/`。

---

## `§三`　工項（依序）

### 工項零′　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：
1. `git merge-base --is-ancestor 0587ea487d3ad0f6eeff3c3687997650d819f3b3 32f70d69ba23add4e46776c3629a0a301ae19af6` ⇒ `rc 0`；`git rev-list --count 0587ea4..32f70d6` ＝ `7`；`git rev-list --count 32f70d6..0587ea4` ＝ `0`；`git rev-list --merges 0587ea4..32f70d6` ＝ 空。
2. `git diff --name-only 0587ea4 32f70d6 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `1` 列：`app.py`（🔒 `:(glob)` ⛔ 省——無之則 `*` 跨 `/`、兼中 `verify/probes/` 之檔）；`git rev-parse 32f70d6:app.py` ＝ `48bb05ae97c4b20c8447716313e1b6c74fef3a7a`；`git rev-parse 32f70d6:verify/selection_pipeline.py` ＝ `cff92d11d4e03c9f9db8d3de590290d3cb44f80d`；`git rev-parse 32f70d6:verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`。
3. `git rev-list 0587ea4..32f70d6` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `commit`（`7ec63f9…`·命中 `1` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3″`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：

```
git push origin 32f70d69ba23add4e46776c3629a0a301ae19af6:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4″`）；⛔ 改目標值（逐字 `32f70d69ba23add4e46776c3629a0a301ae19af6`·⛔ 用任何分支名之當下值）；⛔ 刪側支 `verify/W-G.9-382-k973`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5″`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `32f70d69ba23add4e46776c3629a0a301ae19af6`；
② 遠端 heads ＝ **`42`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `32f70d6` 之相異 ＝ **`0`**；判別力［必非零］：vs `0587ea4` 之相異 ＝ **`1`**（`app.py`）；
④ `git branch -r --contains 7ec63f9eced8f0e436a83d149ad7c22487455a50` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-382-k973`）。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `32f70d6…` 方續工項零。

### 工項零　本補令原封入倉（主線·零生產碼）

`docs/orders/W-G.9-382_補令二.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-382 補令二 工項零：本補令原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一　執行報告入倉（主線·新檔 `docs/reports/W-G.9-382R_入主線_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1″`〜`9″` 之三值（款·期·實）；③ 工項零′ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ `§二` 之放行（KL 之逐字）；⑤ pre-flight 之出艙與逐項之處置；⑥ CC 之自捕與自解；⑦ 各段耗時。收工閘之實測值與工項二之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-382 補令二 工項一：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> rev-parse HEAD` ＝ `32f70d69ba23add4e46776c3629a0a301ae19af6`（`§一` 項 `3`）；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次將新入之路徑集 `A`（期 ＝ 本補令、報告）；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8″`）；不等 ⇒ 停機款 `8″`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項一 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `48bb05ae97c4b20c8447716313e1b6c74fef3a7a`；`… hash-object verify/selection_pipeline.py` ＝ `cff92d11d4e03c9f9db8d3de590290d3cb44f80d`；`… hash-object verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`；`… hash-object verify/probes/probe_WG9375_k965.py` ＝ `10abeb049580ef607103e33266d7f9fa57ff3638`；`… hash-object CLAUDE.md` ＝ `76d57b26123173ec7c5775daab1615d197a664eb`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。

任一不符 ⇒ 停機款 `8″`·⛔ 動、回報實值。主 checkout 之根之未追蹤之單（原單、補令一、本補令之來源檔）由 KL 自行移除（CC ⛔ 刪之）。

---

## `§三-1`　收工閘（工項一之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1″` | 本批二筆 `commit`（工項零、一）之增刪（`git show --numstat`） | 工項零 ＝ 本補令之增／`0`；工項一 ＝ 報告之增／`0`；二筆之首列 ＝ `§三` 所令逐字 |
| `2″` | `git diff --name-status 32f70d6 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`2`** 列：`A` 本補令、`A` 報告；生產碼與 `verify/` 之一切檔對 `32f70d6` 相異 **`0`**；判別力［必非零］：生產碼對 `0587ea4` 相異 **`1`**（`app.py`）；二新檔之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3″` | 二新檔之 `CR`（真 `0x0D`·受詞 ＝ 主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`** |
| `4″` | 四簿、`CLAUDE.md`、`.claude/` | 對 `32f70d6` 相異 **`0`**（閘 `2″` 之二列以外無他檔即證之；另 `git rev-parse HEAD:CLAUDE.md` ＝ `76d57b26123173ec7c5775daab1615d197a664eb`） |
| `5″` | 自限 | 遠端 heads **`42`**；主線 ＝ 工項一之 `commit`，其祖含 `32f70d6`；側支 `verify/W-G.9-382-k973` ＝ `32f70d6…`（⛔ 變）；其餘 `40` 列（除 `wip/s1-endpart` 與該側支）逐列 ＝ `<O>\heads_before_382p2.txt` |
| `6″` | `python verify/probes/probe_WG9270_closegate.py 615 612 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 616 615 .` ⇒ `rc 7` |
| `7″` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 615 612` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零` 項 `3` 之值（⛔ 變） |
| `8″` | 量測器（於主線之端）：`python verify/probes/probe_WG9375_k965.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`python verify/probes/probe_WG9373_k966.py selftest <repo>`；`… wiring <repo>`；`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>`；`python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`；`python verify/probes/probe_WG9367_adj4.py selftest <repo>` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`P0` ＝ `61／61`（`F29`）、`48／48`（`F23`）、`31／31`（`F27`）、`29／29`（`F28`）、`86／86`（`F14`）、`28／28`（`F24`）；`F29 wiring` `Y1`〜`Y11` ✅、`F27 wiring` `Y1`〜`Y9` ✅；`stderr` 合計 `0` B |

---

## `§四`　土地後果

**本案**：配地⛔ 變；主線之畫面唯手冊先行之紀錄之「依據」欄之字面變（`3.5 m` `7` 列、`0 m` `8` 列·原單 `§一` 項 `5`）。**他案**：主線自此依 `K-9-73`（同街廓同地主先·第 31 條第 3 款唯同一原地號·道路用地分配原則次之）。

---

## `§五`　驗收之基數（發單側窗八十四以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 快轉之受詞 | `§一` 項 `1`；新名之占用（母體 ＝ `32f70d6` 之追蹤檔 `2851` 檔·`git grep -l -F`）：`W-G.9-382_補令二` ＝ `0`、`W-G.9-382R_入主線` ＝ `0` ⇒ 可取 |
| `3` | pre-flight | `python verify/probes/probe_order_preflight.py <本補令>`·發單側窗八十四實跑（態 `32f70d6`·定稿）：🔴 機械 `0` 項；🟡 提示與 ℹ️ 記錄見 KL 所貼之訊之附記（皆逐項具名處置） |
| `4` | 模擬（拋棄式 worktree `32f70d6`·⛔ push·工項零′ 須遠端⛔ 模擬） | 工項零 ＋ 工項一（報告之替身）二 `commit`：閘 `1″` 首列逐字·增刪 ＝ 本補令之增／`0`、替身 `1`／`0`；閘 `2″` 恰二 `A`·生產碼對 `32f70d6` 相異 `0`、對 `0587ea4` 恰 `app.py`·二新檔 `git check-ignore -v --no-index` 無命中（`rc 1`）·對照 `rc 0`；閘 `4″` `CLAUDE.md` ＝ `76d57b26…`；閘 `6″` `✅ 二閘皆過`；閘 `7″` `rc 0`·四簿之值 ＝ `§零` 項 `3`；閘 `8″` 之 `P0` 之期 ＝ 發單側於 `32f70d6` 之實跑（`§一` 項 `2`）：`61／61`、`48／48`、`31／31`、`29／29`、`86／86`、`28／28`·`F27 wiring` `Y1`〜`Y9` ✅ |

SELF_SHA256: b18b95d00877e8096e1e128db76d52e4a2c4e440adeb640a87a9ed244b7976fc
