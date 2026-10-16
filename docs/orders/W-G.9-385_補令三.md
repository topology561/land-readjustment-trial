# `W-G.9-385` 補令三：主線快轉（至 `8d0a990`·`W-G.9-385`〔`K-9-74`、`K-9-62` 二欄、`K-9-79` 之落地〕入主線）＋ 主 checkout 之同步 ＋ 二本地暫存支之刪除

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字；受詞 ＝ 主線之快轉、本補令與報告二新檔、主 checkout 之同步、CC 之本地二支之刪除）。
> **發單** ＝ 發單側窗八十七·`2026-10-17`。**受單** ＝ CC（工項零⁗〜一⁗、三⁗ 於 **CC 之施工樹**；工項二⁗ 於 **KL 之主 checkout**）。
> **所補** ＝ `docs/orders/W-G.9-385_規格單.md`（「原單」）之 `§四-2`（入主線之請示·另單）。原單、補令一、補令二留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`；側支 `verify/W-G.9-385-k974` ＝ `8d0a99091b848bd33637f94ed8323c276ce81f74`（補令二 工項四‴）；遠端 heads **`45`**；KL 之主 checkout 停於 `wip/s1-endpart` ＝ `158f7fe…`（`W-G.9-384` 補令一 工項二之同步）；CC 之本地 `hold/W-G.9-385-c2` ＝ `fb637350b8aa333519dc101091de58c57b2a4aca`、`hold/W-G.9-385p1-c2` ＝ `28046f2f03a86b3786c873e84e5afe678bcb048f`。
> **級** ＝ **中**（⛔ 跑 `run_verification.py`／`run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之端；發單側窗八十七已自倉重跑原單之 `V-1`〜`V-9` 與收工閘〔`§一⁗` 項 `2`〕；收工閘唯跑量測器之 `selftest`／`wiring`）。
> 🔑 原單之一切通則照舊（直譯器名 `python`；`git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Windows 下路徑引數一律反斜線之絕對路徑；Bash 之輸出路徑一律單引號之絕對路徑；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標；`<O>` 同原單；並行 ≤ `6`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔**（檔名逐字 `W-G.9-385_補令三.md`·本補令）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2⁗`。CC 一律**二進位複製**、⛔ 讀入改寫；取自第三處者，工項二⁗ 之撞檔前置必觸發，依其處置（`自誤 542`）。
> 🔑 **撇號**：「⁗」＝ U+2057。本補令之款號、工項號、閘號唯指本補令之條。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/` 之一字；遠端之側支之刪除或改寫（`verify/W-G.9-385-k974` 保留為歷史）；`hold/*` 以外之本地支。
> 🔴 **本補令⛔ 令 CC 作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場（**先於工項零′⁗**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`；`git rev-parse origin/verify/W-G.9-385-k974` ＝ `8d0a99091b848bd33637f94ed8323c276ce81f74`；`git ls-remote --heads origin` 之列數 ＝ **`45`**（全列存 `<O>\heads_before_385p3.txt`·收工閘 `5⁗` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-385-k974` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 623 622` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `608`／`MAX` `623`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`。
4. 本補令之 bytes／`sha256` 對拍 KL 所貼之訊；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗。
5. `python verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單側實跑之出艙見 `§五⁗` 項 `3`）。

### `§零-1⁗`　停機款

| # | 款 |
|---|---|
| `1⁗` | 開工時主線 ≠ `158f7fe`，或側支 ≠ `8d0a990`，或遠端 heads ≠ `45`，或施工樹之追蹤檔有變動，或 `§零` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期 |
| `2⁗` | 本補令之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本補令不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3⁗` | 工項零′⁗ 前置之任一期不符 |
| `4⁗` | 工項零′⁗ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（權限設定所擋者 ⇒ 停下出艙其訊息，KL 親推後續之·⛔ 改目標、⛔ `--force`） |
| `5⁗` | 工項零′⁗ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `6⁗` | 工項零⁗、一⁗ 之任一 `push` 之目標非 `wip/s1-endpart`；或任一 `push` 至側支 |
| `7⁗` | `§三-1⁗` 收工閘任一 ≠ 期 |
| `8⁗` | 工項二⁗：主 checkout 之追蹤檔有變動；開工時其 `HEAD` ≠ `158f7fe…` 或其支 ≠ `wip/s1-endpart`；撞檔前置之任一檔與入倉之 blob 相異、或主 checkout 之根已有同名檔；`--ff-only` 被拒；出艙任一 ≠ 期 |
| `9⁗` | 工項三⁗ 之前置之任一 ≠ 期 |
| `10⁗` | CC 作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本批任一新檔為 `git check-ignore -v --no-index` 所命中 |

---

## `§一⁗`　所據

1. **快轉之受詞**（發單側窗八十七·倉外實算）：`git merge-base --is-ancestor 158f7fe 8d0a990` 真；`git rev-list --count 158f7fe..8d0a990` ＝ `11`、反向 ＝ `0`；`git rev-list --merges 158f7fe..8d0a990` ＝ 空；`git diff --name-only 158f7fe 8d0a990 -- app.py ":(glob)verify/*.py"` ＝ 恰 `app.py`；十一筆逐筆以同式判，命中者恰 `1a5ed5710eb248a96d895ba2cfd285abd6fdb074`（補令二 工項二‴·命中 `1` 列）；`8d0a990` 之追蹤檔 `2876`（`git ls-tree -r 8d0a990` 之列數）；其 `app.py` ＝ `cfd66e889f23a502792bec3ddf0fb9c875ec7524`、`verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`、`verify/probes/probe_WG9385_k974.py` ＝ `87c8a3883355cd6093efa4e281b47e473c01a769`、`verify/probes/probe_WG9363_k953.py` ＝ `ccdb11f3a0573c23c91a84e8b35b9735716058cc`、`CLAUDE.md` ＝ `6a2ff2ce9d296903f8e19ba8d194c642556f6639`。
2. **側支之碼之驗**（發單側窗八十七·`2026-10-17`·倉外·⛔ 採 CC 之自報）：側支之端之生產碼係 CC 依原單 `§三`、補令一 `§三″`、補令二 `§三‴` 所撰；發單側逐條讀其全文差異（`git diff 158f7fe 8d0a990 -- app.py`·`+390`／`-3`）對 `R-1`〜`R-19`：`K974_PARAMS` 七鍵、`k962_land_marks` 之五形與 `R-11` 之序、`k974_read_junctions`、`k974_burden_scales` 之取樣／容差／垂距／區界之帶／比例之母體／`R-13` 與 `R-16` 之容差（`−r × A` ＞ `overlap_tol_m2`）／權 ＝ 段數之比、`k974_screen_scales` 之存與 `R-12`／`R-17`、`calc_special_burden_total` 之唯增列、`main` 之三易列與增列——皆合。於拋棄式 worktree（`8d0a990`）重跑原單 `V-1`〜`V-2` 之 `55` 呼叫：皆 `rc 0`、末列皆 ＝ 發單側之原型之同呼叫之末列（逐列同）；`F30 selftest` `K1`〜`K22` ✅（`K20` 前提 `6`／`60`·不符 `0`）、`F30 wiring` `W1`〜`W7` ✅、`F30 run` `R1`〜`R6` ✅、`F23 selftest` `P0 75／75`；`stderr` 合計 `0` B；耗時之和 ≈ `9001` s。`k6s3 cmp`（前態 ＝ `158f7fe` ＋ 原單之塊 `Fy35`〔≡ 原單工項一之端〕對 `8d0a990`）二退縮 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔二退縮前後逐位同（本機 Linux·`8be0160b…`／`6fb86647…`）；`parity` 二退縮 `⇒ rc 0（不符 0 項）`、其落檔與 `stdout` 以同一字樣代 `HEAD` 後逐位同（⛔ 代之則異）；三簿之 blob ＝ 補令二 `§五‴` 項 `5`（`K-6` 典 `e8639d46…`·`824230` B、自誤簿 `c78a429d…`·`1203451` B、`CLAUDE.md` `6a2ff2ce…`·`413291` B）；`probe_WG9270_closegate.py 623 622 .` ⇒ `rc 0`（判別力 `624 623` ⇒ `rc 7`）；`probe_WG9321_issuer_anchor.py … 623 622` ⇒ `rc 0`（`§零` 項 `3` 之值）。
3. **KL 主 checkout**（倉外之物）：`wip/s1-endpart` ＝ `158f7fe`（`W-G.9-384` 補令一 工項二）；其根或有未追蹤之 `W-G.9-385_規格單.md`、`W-G.9-385_補令一.md`、`W-G.9-385_補令二.md`（CC 之來源·倉內之對應檔在 `docs/orders/`·路徑異 ⇒ ⛔ 撞）與本補令之來源檔。
4. **快轉之淨效**（主線 → `8d0a990`·本案）：配地⛔ 變（項 `2`）；畫面：步驟 E 之說明之新文、步驟 H 之「K-9-74」之明細之展開（各面之尺度、B 值 ＝ 主線之端）；`K-9-74`、`K-9-62`（二欄之讀取與檢核）、`K-9-79` 之落地；量測器四器（`F30` 新；`F23`、`F24`、`F25` 之許與 `K75`）；三簿之 `W-G.9-384` 之入主線、`K-9-79` 之立、諸讀法與補令一、二之處置、`自誤 621`〜`623`、待落地清單之更新（`CLAUDE.md` 之塊 `P38`·其序 `2` 之「🔶」於本補令之後實為 ✅·其更新併次單）。

---

## `§二⁗`　放行（KL 之逐字）

**發單側之訊**（發單側窗八十七·`2026-10-16`·對話·逐字·節錄）：「執行端已完成 W-G.9-385，結果放在側支（`verify/W-G.9-385-k974`，最新提交 `8d0a990`），主線仍停在 `158f7fe`，沒有變動。我還在做自己的獨立復驗，還不能請您核對畫面。……復驗都符合後，我會送上入主線的請示，附上畫面核對步驟。……請您決定：執行端保留了兩個本地暫存支（`hold/W-G.9-385-c2`、`hold/W-G.9-385p1-c2`），內容都已併入側支。入主線後可以刪除，下一張補令可以順手處理。」

**KL 之語**（`2026-10-16 23:59`·`Asia/Taipei`·逐字）：

> 執行端保留了兩個本地暫存支（`hold/W-G.9-385-c2`、`hold/W-G.9-385p1-c2`），內容都已併入側支。入主線後可以刪除，下一張補令可以順手處理。
> 確認入主線

🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一`）：KL 之「確認入主線」係答上開之訊（其訊明載本批之生產碼、其土地後果〔本案配地⛔ 變〕與發單側之復驗之待畢），並引二本地支之刪除之議而許之 ⇒ 發單側讀為 **工項零′⁗（主線快轉）、工項二⁗（主 checkout 之同步）與工項三⁗（二本地支之刪除）之放行**，以發單側之復驗皆符為條件（`§一⁗` 項 `2`·已符）。KL 未先於畫面核對（原單 `§四-2`）——發單側之訊已告之「同步完成後，若您方便，可開畫面看二處」；本補令由 KL 貼予 CC 即其確認。CC 將本節之 KL 之逐字載入報告。

| `commit`（全 `40` 碼） | 首列 | 生產碼 | 所據 | 土地後果 |
|---|---|---|---|---|
| `1a5ed5710eb248a96d895ba2cfd285abd6fdb074` | `W-G.9-385 補令二 工項二‴：K-9-74 之落地與 K-9-62 二欄之讀取與檢核（補令一之碼〔hold/W-G.9-385p1-c2〕＋ R-16 重疊之容差 0.01 ㎡·R-17 缺表之錯誤）🔴 生產碼（新側支）` | `app.py` | 原單 `§三`、補令一 `§三″`、補令二 `§三‴` | 本案配地⛔ 變（`§一⁗` 項 `2`） |

🛑 **射程**：`(a)` 主線快轉至 `8d0a99091b848bd33637f94ed8323c276ce81f74`（工項零′⁗·**以前置皆符為條件**）；`(b)` 工項零⁗、一⁗（零生產碼）由 CC 逕行 `push` 至主線；`(c)` 工項二⁗ 於 KL 本機之主 checkout·⛔ `commit`·⛔ `push`；`(d)` 工項三⁗ 唯 CC 之本地二支（⛔ 遠端）；`(e)` ⛔ 及生產碼、`verify/`、任何錨、四簿、`CLAUDE.md`、`.claude/`。

---

## `§三⁗`　工項（依序）

### 工項零′⁗　主線快轉（**第一動**·🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：
1. `git merge-base --is-ancestor 158f7fe959697571d8179988cd4c192c0016ead9 8d0a99091b848bd33637f94ed8323c276ce81f74` ⇒ `rc 0`；`git rev-list --count 158f7fe..8d0a990` ＝ `11`；`git rev-list --count 8d0a990..158f7fe` ＝ `0`；`git rev-list --merges 158f7fe..8d0a990` ＝ 空。
2. `git diff --name-only 158f7fe 8d0a990 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `1` 列：`app.py`（🔒 `:(glob)` ⛔ 省）；`git rev-parse 8d0a990:app.py` ＝ `cfd66e889f23a502792bec3ddf0fb9c875ec7524`；`git rev-parse 8d0a990:verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`；`git rev-parse 8d0a990:verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`。
3. `git rev-list 158f7fe..8d0a990` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判：命中 ≥ `1` 列者恰 `1` 筆 ＝ `§二⁗` 逐筆放行清單之 `commit`（`1a5ed57…`·命中 `1` 列）；逐筆之出艙（含空輸出）存 `<O>`。

任一 ≠ 期 ⇒ 停機款 `3⁗`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：

```
git push origin 8d0a99091b848bd33637f94ed8323c276ce81f74:refs/heads/wip/s1-endpart
```

🛑 **三禁**：⛔ `--force`／`--force-with-lease`（被拒即主線已被他動 ⇒ 停機款 `4⁗`）；⛔ 改目標值（逐字 `8d0a99091b848bd33637f94ed8323c276ce81f74`）；⛔ 刪側支 `verify/W-G.9-385-k974`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `5⁗`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `8d0a99091b848bd33637f94ed8323c276ce81f74`；
② 遠端 heads ＝ **`45`**（⛔ 增減）；
③ 生產碼 `34` 檔於新主線 vs `8d0a990` 之相異 ＝ **`0`**；判別力［必非零］：vs `158f7fe` 之相異 ＝ **`1`**（`app.py`）；
④ `git branch -r --contains 1a5ed5710eb248a96d895ba2cfd285abd6fdb074` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-385-k974`）。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart`，`HEAD` ＝ `8d0a990…` 方續工項零⁗。

### 工項零⁗　本補令原封入倉（主線·零生產碼）

`docs/orders/W-G.9-385_補令三.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-385 補令三 工項零⁗：本補令原封入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項一⁗　執行報告入倉（主線·新檔 `docs/reports/W-G.9-385R_入主線_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項（含工項零′⁗ 之「無 `commit`·遠端 ref 之前後值」）；② 停機款 `1⁗`〜`10⁗` 之三值；③ 工項零′⁗ 前置之全部出艙（含逐筆判之空輸出）與快轉後之出艙 ①〜④；④ `§二⁗` 之放行（KL 之逐字）；⑤ pre-flight 之出艙與逐項之處置；⑥ CC 之自捕與自解；⑦ 各段耗時。收工閘之實測值與工項二⁗、三⁗ 之出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-385 補令三 工項一⁗：執行報告入倉 ⛔ 零生產碼` ⇒ `git push origin HEAD:wip/s1-endpart`。

### 工項二⁗　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`·於收工閘皆符之後）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ `158f7fe959697571d8179988cd4c192c0016ead9`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（未追蹤之來源檔⛔ 計）。
2. **撞檔前置**（`自誤 542`）：
   - 甲、`git -C <主 checkout> diff --name-only --diff-filter=A -z HEAD origin/wip/s1-endpart` ⇒ 本次將新入之路徑集 `A`（期 ＝ 原單、補令一、補令二、本補令、`F30`、二停機上呈之四檔、執行報告二檔、本補令之報告）；
   - 乙、`git -C <主 checkout> ls-files --others --exclude-standard -z` ⇒ 未追蹤之路徑集 `U`；
   - 丙、`A ∩ U` 逐檔：`git -C <主 checkout> hash-object <該檔>` 對 `git -C <主 checkout> rev-parse origin/wip/s1-endpart:<該檔>`——相等 ⇒ 將該檔**移**至主 checkout 之根（檔名不變·⛔ 刪·⛔ 覆寫；根已有同名檔 ⇒ 停機款 `8⁗`）；不等 ⇒ 停機款 `8⁗`·⛔ 動；
   - 丁、甲乙丙之出艙（含 `A ∩ U` 為空者）存 `<O>`。
3. `git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
4. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項一⁗ 之 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `cfd66e889f23a502792bec3ddf0fb9c875ec7524`；`… hash-object verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`；`… hash-object verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`；`… hash-object verify/probes/probe_WG9385_k974.py` ＝ `87c8a3883355cd6093efa4e281b47e473c01a769`；`… hash-object verify/probes/probe_WG9363_k953.py` ＝ `ccdb11f3a0573c23c91a84e8b35b9735716058cc`；`… hash-object CLAUDE.md` ＝ `6a2ff2ce9d296903f8e19ba8d194c642556f6639`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空。

任一不符 ⇒ 停機款 `8⁗`·⛔ 動、回報實值。主 checkout 之根之未追蹤之單（原單、補令一、補令二、本補令之來源檔與先前之舊單）由 KL 自行移除（CC ⛔ 刪之）。

### 工項三⁗　二本地暫存支之刪除（CC 之施工之倉·⛔ 遠端·於工項二⁗ 之後）

**前置**（出艙存 `<O>`）：
1. `git rev-parse hold/W-G.9-385-c2` ＝ `fb637350b8aa333519dc101091de58c57b2a4aca`；`git rev-parse hold/W-G.9-385p1-c2` ＝ `28046f2f03a86b3786c873e84e5afe678bcb048f`；`git ls-remote --heads origin` 無 `hold/` 之列。
2. `git rev-parse hold/W-G.9-385-c2:app.py` ＝ `e89fbe6215c2cab7285741d1235c77f531f19131`、`git rev-parse hold/W-G.9-385p1-c2:app.py` ＝ `797082a61374214280aa1d11f4b9578eb2795f44`（＝ 二停機上呈所報之 blob·其全文差異已入主線〔`docs/reports/W-G.9-385R_工項二_app差異.diff`、`docs/reports/W-G.9-385R_補令一_工項二_app差異.diff`〕；其後之碼 `1a5ed57` 已入主線〔工項零′⁗ ④〕）。
3. `git diff --name-only e6a2289 hold/W-G.9-385-c2`、`git diff --name-only 01ad480 hold/W-G.9-385p1-c2` 各唯 `app.py`。

任一 ≠ 期 ⇒ 停機款 `9⁗`·⛔ 刪。

**刪**：`git branch -D hold/W-G.9-385-c2 hold/W-G.9-385p1-c2`；出艙：`git branch --list "hold/*"` 無此二列；`git reflog` 之條目⛔ 動（`gc` ⛔ 跑）。

---

## `§三-1⁗`　收工閘（工項一⁗ 之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1⁗` | 本批二筆 `commit`（工項零⁗、一⁗）之增刪（`git show --numstat`） | 工項零⁗ ＝ 本補令之增／`0`；工項一⁗ ＝ 報告之增／`0`；二筆之首列 ＝ `§三⁗` 所令逐字 |
| `2⁗` | `git diff --name-status 8d0a990 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`2`** 列：`A` 本補令、`A` 報告；生產碼與 `verify/` 之一切檔對 `8d0a990` 相異 **`0`**；判別力［必非零］：生產碼對 `158f7fe` 相異 **`1`**（`app.py`）；二新檔之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3⁗` | 二新檔之 `CR`（主線之端之 blob·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4⁗` | 四簿、`CLAUDE.md`、`.claude/` | 對 `8d0a990` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `6a2ff2ce9d296903f8e19ba8d194c642556f6639`） |
| `5⁗` | 自限 | 遠端 heads **`45`**；主線 ＝ 工項一⁗ 之 `commit`，其祖含 `8d0a990`；側支 `verify/W-G.9-385-k974` ＝ `8d0a990…`（⛔ 變）；其餘 `43` 列（除 `wip/s1-endpart` 與該側支）逐列 ＝ `<O>\heads_before_385p3.txt` |
| `6⁗` | `python verify/probes/probe_WG9270_closegate.py 623 622 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 624 623 .` ⇒ `rc 7` |
| `7⁗` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 623 622` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零` 項 `3` 之值（⛔ 變） |
| `8⁗` | 量測器（於主線之端）：`python verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python verify/probes/probe_WG9375_k965.py selftest <repo>`；`python verify/probes/probe_WG9357_k948.py selftest <repo>`；`python verify/probes/probe_WG9373_k966.py selftest <repo>`；`python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`F30 selftest` `K1`〜`K22` ✅；`F30 wiring` `W1`〜`W7` ✅（`W7` 之基準 `158f7fe`·相異之節點 ＝ 原單之七）；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）；`stderr` 合計 `0` B |

---

## `§四⁗`　土地後果

**本案**：配地⛔ 變；各面之負擔尺度與 B 值 ＝ 主線之端（本案之「重劃區地籍」無二欄、道路皆勾新闢、`R1`／`R4` 之正面在區外）；畫面增步驟 E 之說明之新文與步驟 H 之明細。**他案**：主線自此依 `K-9-74`／`K-9-79` 求臨街地特別負擔之尺度（未勾新闢之區內道路依扣除抵充地之比例計·區界在中心線者以垂距·一面臨二段以上者加權·勾新闢而無道路 `BLOCK` 者 `0` 並警示），並讀「重劃區地籍」之「第33條排除」「抵充地」二欄（填錯、持分缺漏、讀取失敗、缺表、宗地之片重疊者皆列錯誤而停止計算）。

---

## `§五⁗`　驗收之基數（發單側窗八十七以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 快轉之受詞 | `§一⁗` 項 `1`；新名之占用（母體 ＝ `8d0a990` 之追蹤檔 `2876` 檔·`git grep -l -F`）：`W-G.9-385_補令三` ＝ `0`、`W-G.9-385R_入主線` ＝ `0` ⇒ 可取 |
| `3` | pre-flight | `python verify/probes/probe_order_preflight.py <本補令>`·發單側窗八十七實跑（態 `8d0a990`·定稿）：🔴 機械 `0` 項／🟡 提示 `1` 項——`P-2` `:44`（`§一⁗` 項 `1`·其計數皆為 git 之物件之計數〔`rev-list --count`、`diff --name-only`、`ls-tree -r`〕，非號之占用之框；號之占用唯本表項 `2`〔完整之名·`git grep -l -F`〕⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕·本補令⛔ 用） |
| `4` | 模擬（拋棄式 worktree `8d0a990`·⛔ push·工項零′⁗、二⁗、三⁗ 與閘 `5⁗` 須遠端或他機⛔ 模擬） | 工項零⁗ ＋ 工項一⁗（報告之替身）二 `commit`：工項零⁗ 之 blob ＝ 來源；閘 `1⁗` 首列逐字·增刪 ＝ 本補令之增（`161`）／`0`、替身 `1`／`0`；閘 `2⁗` 恰二 `A`·生產碼與 `verify/` 對 `8d0a990` 相異 `0`、生產碼對 `158f7fe` 恰 `app.py`·二新檔之 `git check-ignore -v --no-index` 無命中（`rc 1`）；閘 `3⁗` `CR` `0`；閘 `4⁗` `CLAUDE.md` ＝ `6a2ff2ce…`；閘 `6⁗` `✅ 二閘皆過`·判別力 `624 623` ⇒ `rc 7`；閘 `7⁗` `rc 0`·四簿之值 ＝ `§零` 項 `3`；閘 `8⁗` 十呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`P0` `75／75`（`F23`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）·`stderr` `0` B；結束時 `git status --porcelain` 空 |

SELF_SHA256: d6d8dd0d5143289c3fd86f29ad97df31c516afde9ae7eb14a82cb0e4bb23934e
