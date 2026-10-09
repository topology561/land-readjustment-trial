# `W-G.9-374R`　主線快轉（至 `cf08e23`·`W-G.9-373` 入主線）＋ `K-6` 典之 `K-9-69` 之立與入主線之註 ＋ 自誤 `592`〜`598` ＋ 待落地清單之更新：執行報告

> **單** ＝ `docs/orders/W-G.9-374_中量單.md`（`80875` B·`sha256` `b7f740285765e2ffcd5585d499c4792807b4904620da94efb21b160e92073a23`·`SELF_SHA256` `a4ccabd7403d64e004f7a83a8eefc7ed076d8754e89fe6bc1bf5ba3e3bcf501f` 實算相符）。**受單** ＝ CC 新窗（`2026-10-09`·Windows 11·施工樹 ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\land-readjustment-trial-5a2fe0`·開窗時在分支 `claude/land-readjustment-trial-5a2fe0` 之 `104e4aa`；`§零-0` 項 `2` 依單 `git checkout --detach origin/verify/W-G.9-373-k966`）。**級** ＝ 中（本批⛔ 撰生產碼、⛔ 動 `verify/`）。
> `<O>` ＝ `C:\Users\admin\o374`（倉外·`git -C <O> rev-parse --is-inside-work-tree` ⇒ `fatal: not a git repository`·`rc 128`）。本機 Python `3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`（發單側為 `3.13.16`／`2.4.6`／`2.2.0`·照實載·本批⛔ 跑配地之器）。量測之殼之 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6`／`WV_K953`／`WV_ADJ4` 皆未設（出艙 `[None, None, None, None, None]`）。
> 工項零′ 之快轉由 **CC 推送**、首推即成（⛔ 被拒·⛔ `--force`）。收工閘之實測值與工項三之出艙於對話（⛔ 寫入本檔·自指）。

---

## ①　逐 `commit` 之 hash 與工項

| 工項 | `commit` | 遠端 `wip/s1-endpart` 之前 → 後 |
|---|---|---|
| 工項零′（主線快轉） | 無 `commit` | `104e4aaf211959c38b4030c55372bb5ef513c7fa` → `cf08e23f11b3193a0bc2657bf7964562615ab5df`（`git push origin cf08e23f11b3193a0bc2657bf7964562615ab5df:refs/heads/wip/s1-endpart`·出艙 `104e4aa..cf08e23  cf08e23f11b3193a0bc2657bf7964562615ab5df -> wip/s1-endpart`·首推即成） |
| 工項零（本單原封入倉） | `b7f99a15fcb7a7a3232db3172a7a77e53ab64c70` | `cf08e23` → `b7f99a1`（`git push origin HEAD:wip/s1-endpart`·首推即成） |
| 工項一（`K-9-69` 之立與入主線之註·自誤 `592`〜`598`·待落地清單） | `52d2513ed78992704530b42a3e25aae07c737920` | `b7f99a1` → `52d2513`（首推即成） |
| 工項二（本報告） | 本檔所在之 `commit`（自指·其 hash 見對話） | `52d2513` → 本 `commit` |

逐 `commit` 之生產碼判（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）：工項零 ＝ 空輸出；工項一 ＝ 空輸出。

## ②　停機款 `1`〜`13`

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `104e4aa`·側支 `cf08e23`／`fe1fe3b`／`e7855ec`·施工樹追蹤檔無變動·heads `38`·器 `rc 0` 且四簿 ＝ 期·旗標 `[None×5]` | 全符：`git fetch origin` 後 `104e4aaf211959c38b4030c55372bb5ef513c7fa`／`cf08e23f11b3193a0bc2657bf7964562615ab5df`／`fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`／`e7855ecf75ca4ed692baa982f5f25ec672847e79`；heads `38`（全列存 `<O>\heads_before.txt`）；`checkout --detach` 後 `status --porcelain --untracked-files=no` ＝ 空；`probe_WG9321_issuer_anchor.py <repo> <O>\anchor0.txt 591 590` `rc 0`·stderr `0` B·「項4′ 四簿·正典框」：自誤 `576`／`591`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `195`／`202`／`[12, 87, 179, 181, 183, 184, 185]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `65`／`68`／`[44, 47]`；旗標 `[None, None, None, None, None]` |
| `2` | `SELF_SHA256` 相符·bytes ＝ KL 之訊·來源檔可得·入倉 blob ＝ 來源 | 全符：`SELF_SHA256` 實算相符（受詞 `80797` B）；`80875` B·`sha256` ＝ KL 之訊；來源取自**第二處**（KL 主 checkout 之根·施工樹之根與 KL 主 checkout 之 `docs/orders/` 皆無之）·二進位複製；入倉 blob 之 `git cat-file blob` `80875` B·`sha256` ＝ `b7f74028…`·與來源 `cmp` 相同 |
| `3` | 工項零′ 前置 ＝ 期 | 全符（③） |
| `4` | 快轉之 `push` ⛔ 被拒、⛔ `--force` | 首推即成·⛔ `--force` |
| `5` | 快轉後 ①〜④ ＝ 期 | 全符（③） |
| `6` | 三塊之 bytes／`sha256`／列數 ＝ `§五-1`·施後 blob ＝ `§五-1` | 全符（④） |
| `7` | 刪除欄 `0`·嚴格前綴·尾 ＝ 塊 | 全符（④） |
| `8` | `checkidx` `rc 0` 且末列 ＝ 期·`gen_fa_index` 出艙 ＝ 期且逐位同 | 全符（⑤） |
| `9` | 收工閘皆符 | 於本 `commit` 推後量·見對話 |
| `10` | 工項三之諸期 | 於收工閘之後辦·見對話 |
| `11` | 工項零〜二之 `push` 目標皆 `wip/s1-endpart`·⛔ 推側支 | 工項零、一皆 `HEAD:wip/s1-endpart`；側支⛔ 推 |
| `12` | ⛔ 判正典、⛔ 改塊／器／命令 | ⛔ 有（⑧、⑨） |
| `13` | 新檔⛔ 為 `git check-ignore` 所命中 | 本單：`git check-ignore -v` 無輸出（`rc 1`）；本報告：於收工閘 `2` 量·見對話 |

## ③　工項零′ 前置與快轉後之出艙

**前置**（`<O>\pre0.txt`·⛔ `commit`）：
- `1`：`git merge-base --is-ancestor 104e4aaf… cf08e23f…` ⇒ `rc 0`；`git rev-list --count 104e4aa..cf08e23` ＝ `11`；反向 ＝ `0`；`git rev-list --merges 104e4aa..cf08e23` ＝ 空。
- `2`：`git diff --name-only 104e4aa cf08e23 -- app.py ":(glob)verify/*.py"` ⇒ `app.py`、`verify/selection_pipeline.py`（`2` 列）；判別力：去 `:(glob)` ⇒ `11` 列；`cf08e23:app.py` ＝ `cdfe1e7b209bdff1068350196a6f59fba9be9ff2`；`cf08e23:verify/selection_pipeline.py` ＝ `2d7def55f37e15b22698ce9ec217b00f18d4b92d`。
- `3`：逐筆（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）：

| `commit` | 命中列數 | 出艙 |
|---|---|---|
| `cf08e23f11b3193a0bc2657bf7964562615ab5df` | `0` | （空） |
| `f6b29472f6d420e151b4721e98f70c287b15b69b` | `0` | （空） |
| `9d968b5b8837cd35a50cdfccb67c6eb82180f322` | `2` | `app.py`、`verify/selection_pipeline.py` |
| `c62d09ef5b32a7450aa89408ac0bd416f5f1ddd6` | `0` | （空） |
| `da61f0f145adeaca559ce50b0002fddd343fefec` | `0` | （空） |
| `3813a1e42946df5488c7ecd87999396d321c7332` | `0` | （空） |
| `b73fbd42d053110006e847a6e3dd69774bf03b41` | `0` | （空） |
| `dce634a5c465c5e9d9a6890c5815aa3c805e5be9` | `0` | （空） |
| `fcef5a3e3d1f073747ae81b4a998c6cdbfb26a2d` | `0` | （空） |
| `e4e98a50c219ec3cf78fc1d9bc881e66103f6b0b` | `0` | （空） |
| `e7fe4b9b882ef30b169aabe421774360ca6e4bdc` | `0` | （空） |

⇒ 命中者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `9d968b5…`（`2` 列）。

**快轉**：前置皆符後，以分開之呼叫發 `git push origin cf08e23f11b3193a0bc2657bf7964562615ab5df:refs/heads/wip/s1-endpart`（`<O>\push0.txt`）⇒ `rc 0`·`104e4aa..cf08e23`。

**快轉後即出艙**（`<O>\post0.txt`）：
- ①：`git ls-remote origin refs/heads/wip/s1-endpart` ＝ `cf08e23f11b3193a0bc2657bf7964562615ab5df`。
- ②：遠端 heads ＝ `38`。
- ③：生產碼 `34` 檔（母體：`app.py` ＋ `verify/` 頂層 `*.py`·以 `git ls-tree` 正面過濾·新主線實數 `34`）於新主線 vs `cf08e23` 相異 ＝ `0`；判別力 vs `104e4aa` ＝ `2`（`app.py`、`verify/selection_pipeline.py`）。
- ④：`git branch -r --contains 9d968b5…` ＝ `origin/verify/W-G.9-373-k966`、`origin/wip/s1-endpart`。快轉前之值（單載「唯 `origin/verify/W-G.9-373-k966`」）於快轉前未另量，事後以快轉前所存之 `<O>\heads_before.txt` 之 `38` 列逐列 `git merge-base --is-ancestor 9d968b5… <sha>` 重建（`<O>\contains_before.txt`）⇒ 含者唯 `refs/heads/verify/W-G.9-373-k966`（`1`／`38`）；同法之對照（`<O>\contains_ctrl.txt`）：根 `commit` `1b290e4` ⇒ `38`［必全］、未推遠端之 `6e7272a` ⇒ `0`［必零］（⑨ 自解 `1`）。

其後 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `cf08e23f11b3193a0bc2657bf7964562615ab5df`。

## ④　三塊之實得與三簿之改前改後

抽取式依 `§五-1` 末（附錄標題列後之第一個 ```` 開列〔語言名 `markdown`〕至恰四反引號之閉列·逐列 `\n` 相接末附 `\n`·UTF-8·二進位寫出）；來源 ＝ 入倉之 `docs/orders/W-G.9-374_中量單.md`；`<O>\append.txt`。

| 塊 | 標題列／開列／閉列 | bytes | `sha256` | 列 | 首列空 |
|---|---|---|---|---|---|
| `K17` | `235`／`237`／`377` | `19574` | `efed542cd83befd3a8120358973a822c07feacfaa57e8cd95517020ce990a32a` | `139` | 是 |
| `E17` | `379`／`381`／`442` | `12146` | `4fa86514ae3f592517677eea9661079808493e06e250fdf4305d01e926170bf5` | `60` | 是 |
| `P27` | `444`／`446`／`475` | `6184` | `650db46e145c5d0b3e32ac5857383c9f87f0a620a9aeb09dae29d6414ad2d168` | `28` | 是 |

| 簿 | 改前 bytes／blob | 改後 bytes／blob | 嚴格前綴 | 尾 ＝ 塊 | `numstat` | CR |
|---|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `618122`／`47b15cfe2f4446ecc03fc810bd42e3e2bd764f66` | `637696`／`44fc9969f7d8c8bedabf10a913561a5457a51f5e` | 真 | 真 | `139`／`0` | `0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1143535`／`58c4b6311d5a54f6d38e697c1cb2f8e31692c89c` | `1155681`／`7d1ed5f08892cdced160affd65b8903e7564a1be` | 真 | 真 | `60`／`0` | `0` |
| `CLAUDE.md` | `362039`／`2aaa54c5ccf8c85288bfe9de7339c3b5fe5bc593` | `368223`／`533eff8ea991df6c26cfe0bba48dd5bbee42b337` | 真 | 真 | `28`／`0` | `0` |

改前之 blob 於工作樹與 `HEAD`（`b7f99a1`）皆實算相符；改後之 blob 於 `commit` 後以 `git rev-parse 52d2513:<簿>` 復驗 ＝ 上表。`GB` 簿⛔ 動。

## ⑤　工項一之 `checkidx`、`gen_fa_index`

- 塊 `CK`／`GF` 自入倉之 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳抽出（附錄標題列後之第一個圍欄開列·語言名不拘）：`CK` 標題列 `805`·`1539` B·`00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；`GF` 標題列 `753`·`2445` B·`b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `§五-1` 項 `6`）；寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
- 塊 `P27` 附後：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`·stderr `0` B·末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`·stderr `0` B·出艙 `則 124；加註節 14；列 158`；`cmp <O>\FX_regen.md .claude\skills\failure-archaeology-index\SKILL.md` ⇒ 逐位同。

## ⑥　`§二` 之放行（KL 之逐字）

- 入主線之請示之答（KL `2026-10-09 17:22`·單 `§二` 所錄·逐字）：「畫面無誤，看完時間詳如上傳cmd的文字訊息」「主線是否快轉至 `cf08e23` 並同步你的主 checkout？是。」——依單 `§二`「生產碼入主線之放行」，為工項零′（主線快轉）與工項三（主 checkout 之同步）之放行；生產碼之 `commit` 唯 `9d968b5b8837cd35a50cdfccb67c6eb82180f322`（土地後果：無）。
- 本窗之 KL 之訊（於對話·逐字）：「@"C:\Users\admin\Desktop\land-readjustment-trial\W-G.9-374_中量單.md" 80875 B，sha256 b7f740285765e2ffcd5585d499c4792807b4904620da94efb21b160e92073a23」。

## ⑦　pre-flight 與 `§零-1` 之重算

`python verify/probes/probe_order_preflight.py <本單>`（態 `cf08e23`·`rc 0`·stderr `0` B·`<O>\preflight.txt`）：🔴 機械 `0` 項；🟡 提示 `3` 項——`P-1` `:413`、`P-4` `:82`、`P-4` `:194`：皆依單 `§五-1` 項 `7` 之**具名豁免**（`:413` 係所引中間報告之原文之括注·⛔ 為本單之全稱否定；`:82` 箭頭之座標系 ＝ 主線至側支之端與交接之名、匯出之前後·表內自載；`:194` ＝ 改前至改後·表內自載）；ℹ️ 記錄 `2` 項：`P-5` 相符（受詞 `80797` B）、`P-3` `app.py` `def main` 區間（AST）＝ `22119`–`29839`（本單⛔ 用）。

`§零-1` 之重算：
- 宣告框（`<O>\occ.txt`）：`wg9268_gate6_occupancy.py cf08e23 W-G.9-374 W-G.9-373 W-G.9-397` `rc 0`·stderr `0` B·母體 `993` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）。受詢 `W-G.9-374`：嚴格／寬式皆 `D1` `0`·`D2` `3`·`D3` `0`·列框 `3`·檔框 `3`·鬆框 `3` 檔／`8` 列——`8` 列逐筆 ＝ 單之表所具名之前瞻（`W-G.9-373_補令一.md` `:32`／`:90`／`:197`／`:246`、`W-G.9-373_補令二.md` `:175`／`:192`、`W-G.9-373R_K-9-66至68之落地_執行報告.md` `:804`／`:993`）⇒ 依單之**具名豁免**取之。對照 `W-G.9-373` `11`／`13`／`15`·列框 `28`·檔框 `12`·鬆框 `13`／`415`；`W-G.9-397` 嚴格全 `0`、寬式 `D3` `2`、鬆框 `14`／`22`；`W-G.9-963` 嚴格全 `0`、寬式 `D3` `6`、鬆框 `43`／`48`——皆 ＝ 單之表。
- 意指占用（`<O>\occ2.txt`·母體 `cf08e23` 之追蹤檔 `2817` 檔·列框）：`K-9-69` 錨定 `8` 列（`5` 檔·逐列 ＝ 塊 `K17` 之「編號之由」）、`K-9-70` `0`、對照 `K-9-68` `195`（`21` 檔）；自誤 `592`〜`598` 裸 `76`／`54`／`89`／`21`／`143`／`54`／`50`、平形 `0`／`0`／`0`／`2`／`3`／`3`／`1`、B 形皆 `0`、C 形 ＝ 平形；平形之列逐筆 ＝ 單之表所具名之對照乙之列；對照 `591` 裸 `77`／平形 `10`／B 形 `2`／C 形 `9`。塊名：`E17`／`P27` 二框皆 `0`／`0`；`K17` 塊框 `0`／`0`、名框 `4` 檔／`4` 列（量測器之項名·逐列 ＝ 單之表）；對照 `K16` 塊框 `6`／`27`、名框 `7`／`34`——皆 ＝ 單之表。

## ⑧　CC 讀塊時認為與倉之事實不符之處

無。（抽查：塊 `E17` `自誤 594` 之「`F9`〜`F27` 中獨缺 `F20`」——`verify/probes/` 之器之檔首自載之「檔 F」號實為 `F3`、`F4`、`F6`〜`F19`、`F21`〜`F28`；塊 `K17` 所引之 `K-9-49` ③「已上鎖、已併入或已分配予街角之土地」、`K-9-66` 通知 `3`、`K-9-51` 讀法 `5`「其餘量入調配之輸入之合併單位」、「`K-9-68` 之立」節，皆在改前之 `K-6` 典；塊 `P27` 之「`W-G.9-357` 之節之序 `7`（畫面之步驟 `M`·⬜）」＝ `CLAUDE.md` 該節序 `7`〔畫面「自動計算公設分配」展開區·⬜〕，「步驟 M」之名見 `docs/orders/W-G.9-345_重量單.md`。）

## ⑨　CC 之自捕與自解

- **自捕 `1`（量測器之路徑·⛔ 及倉）**：工項一首次抽塊，`K17`／`E17`／`P27` 之輸出路徑以 Bash **雙引號**含 `\\$2` 書之（違單首 🔑「Bash 之輸出路徑一律單引號之絕對路徑」），致三塊皆寫入同一錯置檔 `C:\Users\admin\o374$2.md`（`<O>` 之外·倉外；末寫者 `P27` `6184` B）；印出之 bytes／`sha256`／列數係記憶體內之值、皆 ＝ 期。隨後之 `append.py` 讀 `<O>\K17.md` ⇒ `FileNotFoundError`、`rc 1`，**於寫任何簿之前**中止（其後 `git status --porcelain` ＝ 空）。處置：刪此自產之錯置檔；以單引號之絕對路徑重抽 ⇒ 三檔落 `<O>`，`sha256sum` 實算 ＝ `§五-1` 項 `2`〜`4`；而後附塊（④）。
- **照實記**：`commit` 訊息之首段逐字依單；末附 `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` 一列，同倉內 `W-G.9-373` 各 `commit` 之體例。
- **本批之自解清單**：
  1. **④ 之快轉前值之量法**——單之 ④ 括注「快轉前唯 `origin/verify/W-G.9-373-k966`」，CC 於快轉前未另量；改以快轉前所存之 `<O>\heads_before.txt`（`17:52:11` 存·快轉 `17:54:40`）逐列重建（③ ④）。五項：零土地後果（唯量法·⛔ 及任一宗地）；零生產碼；可機驗且當批跑必紅／必綠對照（根 `commit` ⇒ `38`／`38`［必全］、`6e7272a` ⇒ `0`［必零］）；可逆（倉外新檔）；寫入本清單。

## ⑩　各段耗時（本機時刻·`+0800`）

| 段 | 起訖 |
|---|---|
| `§零-0`〜`§零-3`（`fetch`·態錨·`heads_before`·四簿之器·`SELF_SHA256`·宣告框·意指占用·pre-flight） | `17:51`〜`17:54` |
| 工項零′ 前置 `1`〜`3` | `17:54` |
| 工項零′ 快轉（`push`）與快轉後 ①〜④ | `17:54`〜`17:55` |
| 工項零（`commit`·`push`） | `17:55` |
| 工項一（抽塊·附錄·`checkidx`·`gen_fa_index`·`commit`·`push`） | `17:55`〜`17:58` |
| 工項二（④ 之重建與對照·本報告） | `17:58`〜 |
