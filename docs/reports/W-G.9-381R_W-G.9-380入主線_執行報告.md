# `W-G.9-381R`　`W-G.9-380` 入主線（主線快轉至 `37f30e1`）＋ 補令一之裁之讀法入典 ＋ `自誤 610`〜`612` ＋ 單號之順延 ＋ 待落地清單之更新　執行報告

> **單** ＝ `docs/orders/W-G.9-381_中量單.md`（`52982` B·`sha256` `ba23ba285c5d1fb3befc1ab288c5475b3345a7f446367fd110337fbb834f5031`·`SELF_SHA256` `ce094822cf0161d40c1aa4107012a93ac21324d47df59ab4cbbf8112f7cabd56` 自驗相符）。
> **受單** ＝ CC 窗（施工樹 `.claude/worktrees/w-g-9-381-processing-883a54`·Windows 11·Git Bash·Python `3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`）·`2026-10-13`。
> **級** ＝ 中（本批⛔ 撰生產碼、⛔ 動 `verify/` 之一字；⛔ 跑 `run_verification.py`／`run_all`）。
> **`<O>`** ＝ `C:\Users\admin\wg381o`（倉外·`git rev-parse --show-toplevel` 於該目錄 ⇒ `fatal: not a git repository`·`rc 128`）。一切出艙檔存於此。
> 收工閘之實測值與工項三之出艙載於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 首列 | 遠端 `wip/s1-endpart` 之前 → 後 |
|---|---|---|---|
| 零′（主線快轉） | 無 `commit` | — | `63a86bb2f9ee7d1277dbbc93b129a2bc345db5f0` → `37f30e196d40d3ce528214b72b2df12ca333394f` |
| 零 | `ba8a67ee1715fefe38d137edf1e560dbfe084435` | `W-G.9-381 工項零：本單原封入倉 ⛔ 零生產碼` | `37f30e1` → `ba8a67e` |
| 一 | `74c8a7eba6de7b1f46d392091d7eb7239276f7b0` | `W-G.9-381 工項一：W-G.9-380 入主線 ＋ 補令一之裁之讀法 ＋ 自誤 610〜612 ＋ 單號之順延 ＋ 待落地清單之更新 ⛔ 零生產碼` | `ba8a67e` → `74c8a7e` |
| 二 | 本檔之 `commit`（其 hash 見對話之完工回報） | `W-G.9-381 工項二：執行報告入倉 ⛔ 零生產碼` | `74c8a7e` → 本檔之 `commit` |

🔴 **工項零′ 之推者照實記**：CC 之 `git push origin 37f30e196d40d3ce528214b72b2df12ca333394f:refs/heads/wip/s1-endpart` 被 Claude Code 之權限分類器擋下（訊息 `[Blind Apply]`·git 無出艙·遠端未動）⇒ 依停機款 `4` 之括注（前例 `W-G.9-379`）停下並出艙其訊息。KL 親推：KL 於**本施工樹**（`…\.claude\worktrees\w-g-9-381-processing-883a54`）之終端機逐字執行同一命令，git 出艙 `63a86bb..37f30e1  37f30e196d40d3ce528214b72b2df12ca333394f -> wip/s1-endpart`；KL 其後於主 checkout 再推同一命令 ⇒ `Everything up-to-date`（空操作）。⛔ `--force`；目標值逐字。工項零、一由 CC 推，皆首推即成（`rc 0`）。

各 `commit` 之生產碼判（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）：工項零 ＝ 空輸出（`0` 列）；工項一 ＝ 空輸出（`0` 列）。

---

## ② 停機款 `1`〜`13` 之三值

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `63a86bb`；六側支 ＝ 單首；施工樹追蹤檔⛔ 變；heads `41`；開場之器 `rc 0` 與四簿之值 ＝ 期；旗標 `[None×5]` | 主線 `63a86bb2f9ee7d1277dbbc93b129a2bc345db5f0`；六側支：`verify/W-G.9-380-k375s` `37f30e196d40d3ce528214b72b2df12ca333394f`、`verify/W-G.9-378-gb204` `3f46284d4abb8374b1425eeb1b491fe53fedad18`、`verify/W-G.9-375-k965` `96bd6fe5daa32bbbb82564f733e5ec875cd740ab`、`verify/W-G.9-373-k966` `cf08e23f11b3193a0bc2657bf7964562615ab5df`、`verify/W-G.9-370-selfchk` `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`、`verify/W-G.9-367-adj4` `e7855ecf75ca4ed692baa982f5f25ec672847e79`（皆 ＝ 單首）；`git checkout --detach origin/verify/W-G.9-380-k375s` 後 `status --porcelain --untracked-files=no` ＝ 空；heads `41`（存 `<O>\heads_before.txt`）；`probe_WG9321_issuer_anchor.py … 609 607` ⇒ `rc 0`·stderr `0` B·項4′：自誤 `594`／`609`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `69`／`72`／`[44, 47]`；旗標 `[None, None, None, None, None]` ⇒ **未觸** |
| `2` | `SELF_SHA256` 相符；KL 之訊之 bytes ＝ 本單；來源檔存；入倉 blob ＝ 來源 | 來源取自 KL 主 checkout 之根（施工樹之根無之·序之第二處）；`52982` B·`sha256` ＝ KL 之訊；`SELF_SHA256` 實算 ＝ 單載（受詞 `52904` B）；`git cat-file blob HEAD:docs/orders/W-G.9-381_中量單.md` 與來源 `cmp` 逐位同（blob `7f0ac23567f0466b7d61e727214e078004fd52f8`）⇒ **未觸** |
| `3` | 工項零′ 前置皆符 | 見 ③ ⇒ **未觸** |
| `4` | 快轉之 `push` 不被拒、⛔ 須 `--force` | CC 之 `push` 為權限分類器所擋（⛔ git 之拒）⇒ **觸其括注之情形**：停下出艙其訊息，KL 親推後續之（見 ①）；⛔ 改目標、⛔ `--force` |
| `5` | 快轉後 ①〜④ ＝ 期 | 見 ③ ⇒ **未觸** |
| `6` | 三塊之 bytes／`sha256`／列數 ＝ `§五-1`；施後 blob ＝ `§五-1` 項 `5` | 見 ④ ⇒ **未觸** |
| `7` | 三簿刪除欄 `0`；改前為改後之嚴格前綴；尾 ＝ 塊 | 見 ④ ⇒ **未觸** |
| `8` | `checkidx` `rc 0`·末列 ＝ 期；`gen_fa_index` 出艙 ＝ 期·逐位同 | 見 ⑤ ⇒ **未觸** |
| `9` | `§四` 收工閘皆符 | 收工閘於本檔之 `commit` 推後量（自指）·其值見對話 |
| `10` | 工項三之各期 | 工項三於收工閘之後·其出艙見對話 |
| `11` | 工項零〜二之 `push` 之目標皆 `wip/s1-endpart`、⛔ 推側支 | 工項零、一之 `push` 皆 `HEAD:wip/s1-endpart`；側支⛔ 推 ⇒ **未觸** |
| `12` | CC ⛔ 作正典之判、⛔ 改塊／器／命令；塊與倉之事實不符者回報 | ⛔ 作；塊、器、命令皆逐字；見 ⑧ ⇒ **未觸** |
| `13` | 新檔⛔ 為 `check-ignore -v --no-index` 所命中 | 本單：`rc 1`（無命中）；本報告：見對話之閘 `2` ⇒ 本單 **未觸** |

---

## ③ 工項零′ 前置之全部出艙與快轉後之出艙

**前置 `1`**：`git merge-base --is-ancestor 63a86bb… 37f30e1…` ⇒ `rc 0`；`git rev-list --count 63a86bb..37f30e1` ＝ `8`；反向 ＝ `0`；`git rev-list --merges 63a86bb..37f30e1` ＝ 空。

**前置 `2`**：`git diff --name-only 63a86bb 37f30e1 -- app.py ":(glob)verify/*.py"` ⇒ `1` 列 `app.py`（對照：無 `:(glob)` 之形 ⇒ `5` 列）；`37f30e1:app.py` ＝ `ca97584efdd9f2744715d2c4649003f7262ce356`；`37f30e1:verify/selection_pipeline.py` ＝ `cff92d11d4e03c9f9db8d3de590290d3cb44f80d`；`37f30e1:verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`。

**前置 `3`**（逐筆·出艙檔 `<O>\pre3_<c>.txt`）：

| `commit` | 命中列數 | 出艙 |
|---|---|---|
| `37f30e196d40d3ce528214b72b2df12ca333394f` | `0` | （空） |
| `6584c293e8911a55317d7c2abdf9dbdd45b5ec5d` | `0` | （空） |
| `177dcf68b33e1756908afbef17fc6bfb46af0869` | `1` | `app.py` |
| `e0adbfeea4f838a585b0311853712f91a1c27706` | `0` | （空） |
| `12f5d3e82d60afc5f048db024923f212f7b90ff2` | `0` | （空） |
| `e745255f367a8d04011c778b86b31e21e92a4136` | `0` | （空） |
| `64071b620f8caf18aba2b2893aab75670adbacb2` | `0` | （空） |
| `0cde290e3de2cf30f6a991709096b17c9d30cd38` | `0` | （空） |

命中者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `177dcf68b33e1756908afbef17fc6bfb46af0869`。

**快轉後**（出艙檔 `<O>\post_ff.txt`）：
① `git ls-remote origin refs/heads/wip/s1-endpart` ＝ `37f30e196d40d3ce528214b72b2df12ca333394f`；
② 遠端 heads ＝ `41`；除 `wip/s1-endpart` 外之 `40` 列與 `heads_before.txt` 逐列同；
③ 生產碼 `34` 檔於新主線 vs `37f30e1` 相異 `0`；判別力：vs `63a86bb` 相異 `1`（`app.py`）；
④ `git branch -r --contains 177dcf68b33e1756908afbef17fc6bfb46af0869` ＝ `origin/verify/W-G.9-380-k375s`、`origin/wip/s1-endpart`。

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `37f30e196d40d3ce528214b72b2df12ca333394f`。

---

## ④ 三塊之實得與三簿之改前改後

塊之抽取（依 `§五-1` 末之抽取式·以 `## 附錄甲`／`乙`／`丙` 之後之第一個圍欄開列為準·二進位寫出）：

| 塊 | bytes | `sha256` | 列數 | 期 |
|---|---|---|---|---|
| `K21` | `5080` | `ccf8cf90a5d0448f63416473b40f6a4aefe65578e350b6a03292b57c46e850dd` | `23` | ＝ |
| `E24` | `5007` | `975a7848f7d997dfceba1ad7db9cae61b5c1fdedf3f465b729dfeeb50f554714` | `31` | ＝ |
| `P34` | `4156` | `a7406197a995a2704ef48c618b33887b4c4854215bce28839086fb565b99d338` | `26` | ＝ |

三簿（改前全檔 ＝ `HEAD` 之 blob〔逐位核〕；附後核「改後以改前為嚴格前綴且其尾 ＝ 塊」皆真）：

| 簿 | 改前 bytes → 改後 bytes | 施後 blob | `numstat` | `CR` |
|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `723139` → `728219` | `22797fa6563b46fc9fa80bdde2c6daf87cdc40d7` | `23`／`0` | `0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1175875` → `1180882` | `b76e3e659448c1bc45ed6966595435964906c5ef` | `31`／`0` | `0` |
| `CLAUDE.md` | `390979` → `395135` | `62a21b12234d4e9b5073e7a95959e1c0892155c7` | `26`／`0` | `0` |

施後 blob 皆 ＝ `§五-1` 項 `5`。`core.autocrlf` 分層現查：system ＝ `true`（`C:/Program Files/Git/etc/gitconfig`）、local ＝ `false`（倉之 `.git/config`·施工樹繼承之）；寫入一律二進位，工作樹之檔 `CR` ＝ `0`。

---

## ⑤ 工項一之 `checkidx`、`gen_fa_index`

塊 `CK`／`GF` 自 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳抽出：`CK` `1539` B·`00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；`GF` `2445` B·`b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（皆 ＝ `§五-1` 項 `6`）；寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。

- `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`；stderr `0` B。
- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`；出艙 `則 124；加註節 14；列 158`；stderr `0` B；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` `cmp` 逐位同。

---

## ⑥ `§二` 之放行（KL 之逐字）

> `2026-10-13 12:41`：如何 切到側分支端點，確認顯示的是 `37f30e1`?
>
> `2026-10-13 16:04`：是，畫面核對無誤(16:04)，續擬W-G.9-381

其「是」所答之問（入主線之請示之【要你判斷】）已明載生產碼之 `commit` `177dcf6` 與其土地後果（本案無）⇒ 為工項零′（主線快轉）與工項三（主 checkout 之同步）之放行（單 `§二`）。

---

## ⑦ pre-flight 之出艙與逐項之處置

`python verify/probes/probe_order_preflight.py <本單>` ⇒ `rc 0`·stderr `0` B（`52982 B／336 列`）：

- 🔴 機械 `0` 項。
- 🟡 `P-6` `:329`（塊 `P34` 之「前節之更新」列）⇒ **具名豁免**（單 `§五-1` 項 `7`：其「⇒」係前節之序與本表之序之對應·⛔ 停機款所繫之數·逐字之塊）。
- ℹ️ `P-5` `:336` 相符（受詞 `52904` B）；`P-3` `app.py` `def main` 區間（AST）＝ `22747`–`30467`（本單⛔ 用）。

＝ 發單側之實跑（`§五-1` 項 `7`）。

---

## ⑧ CC 讀塊時認為與倉之事實不符之處

無。

---

## ⑨ CC 之自捕與自解

**本批之自解清單**：無（本批未行自解款）。

自捕（皆⛔ 土地後果·⛔ 影響任何出艙之判）：
1. 以 `grep -n '^## 附錄[午巳]'` 偵察塊 `CK`／`GF` 之位置時，多位元組字元類於 Git Bash 之 `grep` 下多命中他附錄（`己`、`庚`、`壬`、`子`、`寅`、`卯`）——唯偵察之顯示；塊之抽取以 Python 之「列首前綴」為之（⛔ 用字元類），其 bytes／`sha256`／列數皆 ＝ 期。
2. `§零-1` 之意指占用與塊名之框，CC 以 `git grep -c`（`-P` 錨定框／`-F` 三形）於 `37f30e1` 重算：追蹤檔 `2843`；`610` 裸 `9889`／平 `0`／B `1`／C `0`；`611` `99`／`0`／`0`／`0`；`612` `89`／`0`／`0`／`0`；`609` `82`／`7`／`0`／`7`；塊名 `K21` 塊框 `0`／`0`·名框 `3`／`3`；`E24`、`P34` 皆 `0`；對照 `K20` `4`／`22`·`9`／`38`，`E23` `1`／`4`·`4`／`16`，`P33` `1`／`5`·`4`／`18`；`W-G.9-381R` `0` 檔。宣告框器 `wg9268_gate6_occupancy.py 37f30e1 W-G.9-381 W-G.9-380 W-G.9-397` ⇒ `rc 0`·母體 `1018` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）·四列 ＝ 單之表。皆 ＝ 單。

---

## ⑩ 各段耗時（本機時刻·`<O>` 出艙檔之 mtime 與 `commit` 時刻）

| 段 | 時刻 | 約耗 |
|---|---|---|
| 開場（fetch／refs／heads） | `16:23:40` | — |
| 開場之器（四簿） | `16:23:49` | `< 1` 分 |
| pre-flight | `16:24:27` | `< 1` 分 |
| 取號重算（宣告框器、意指占用） | `16:25:01`〜`16:25:19` | `1` 分 |
| 工項零′ 前置 `1`〜`3` | `16:25:33` | `< 1` 分 |
| 快轉之 `push` 被擋 → KL 親推 → 快轉後之出艙 | `16:30:12` | 約 `5` 分（候 KL） |
| 工項零 `commit`／`push` | `16:30:37` | `< 1` 分 |
| 工項一（附塊·`checkidx`·`gen_fa_index`·`commit`／`push`） | `16:31:03`〜`16:31:17` | `< 1` 分 |
| 工項二（本檔） | 其後 | — |
