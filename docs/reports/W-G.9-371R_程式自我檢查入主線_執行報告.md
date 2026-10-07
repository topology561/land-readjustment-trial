# `W-G.9-371R`　程式自我檢查入主線（`K-9-57` ⑧·`W-G.9-370` 入主線）＋ `K-6` 典之註 ＋ 自誤 `588`〜`589` ＋ 待落地清單之更新：執行報告

> **單** ＝ `docs/orders/W-G.9-371_中量單.md`（`46078` B·`sha256` `717c223475bef52978bb102fe2aae8019dd8401fda300e72e77fcfbcbc8f56f8`·`SELF_SHA256` 相符）。**受單** ＝ CC 新窗（`2026-10-07`·Windows 11·施工樹 ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-371-construction-cd029f`）。**級** ＝ 中（本批⛔ 撰生產碼、⛔ 動 `verify/`）。
> `<O>` ＝ `C:\Users\admin\AppData\Local\Temp\claude\C--Users-admin-Desktop-land-readjustment-trial--claude-worktrees-wg9-371-construction-cd029f\b3ce3bc7-4dda-48ea-8da1-6aa3c7aefb51\scratchpad\O`（倉外·`git -C <O> rev-parse --is-inside-work-tree` ⇒ `fatal: not a git repository`）。
> 🔴 **偏離之照實記**：工項零′ 之快轉由 **KL 親手推送**（CC 之 `git push` 為本工作階段之權限分類器所拒·見 ③、⑨）。收工閘之實測值與工項三之出艙於對話（⛔ 寫入本檔·自指）。

---

## ①　逐 `commit` 之 hash 與工項

| 工項 | `commit` | 遠端 `wip/s1-endpart` 之前 → 後 |
|---|---|---|
| 工項零′（主線快轉·**KL 執行**） | 無 `commit` | `3b35daad5fbf1749b7b596b0013575ec4388202d` → `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583` |
| 工項零（本單原封入倉） | `61286800fa47711d71a691d27fc9e25ea6acb6f3` | `fe1fe3b` → `6128680`（`git push` 首推即成） |
| 工項一（`K-6` 典之註·自誤 `588`〜`589`·待落地清單） | `f29be7c319ac1933ebea90d5fc0693866ec832e4` | `6128680` → `f29be7c`（首推即成） |
| 工項二（本報告） | 本檔所在之 `commit`（自指·其 hash 見對話） | `f29be7c` → 本 `commit` |

逐 `commit` 之生產碼判（`git diff --name-only <c>^ <c> -- app.py verify/stepg_pipeline.py verify/run_all.py verify/run_verification.py`）：工項零 ＝ 空輸出；工項一 ＝ 空輸出。

## ②　停機款 `1`〜`13`

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `3b35daa`·側支 `fe1fe3b`／`e7855ec`·施工樹追蹤檔無變動·heads `37`·器 `rc 0` 且四簿 ＝ 期·旗標 `[None×5]` | 全符：`3b35daad…`／`fe1fe3bf…`／`e7855ecf…`；`status --porcelain --untracked-files=no` ＝ 空；heads `37`；`probe_WG9321_issuer_anchor.py … 587 583` `rc 0`·自誤 `572`／`587`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `195`／`202`／`[12, 87, 179, 181, 183, 184, 185]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `60`／`63`／`[44, 47]`·stderr `0` B；旗標 `[None, None, None, None, None]` |
| `2` | `SELF_SHA256` 相符·bytes ＝ KL 之訊·來源檔可得·入倉 blob ＝ 來源 | 全符：`SELF_SHA256` `c00517036c722243cf1379ccf02fa579227bc2f87051ce273996b17d1c7e608c` 實算相符；`46078` B·`sha256` ＝ KL 之訊；來源取自**第二處**（KL 主 checkout 之根·施工樹之根無之）；入倉 blob `8f978e3aae8542e3b1f7dfefd4138cb194922888`·`git cat-file blob` 與來源 `cmp` 相同·`sha256` ＝ `717c2234…` |
| `3` | 工項零′ 前置 ＝ 期 | 全符（③） |
| `4` | 快轉之 `push` 不被拒、⛔ `--force` | 遠端未拒；CC 之 `push` 為本工作階段之權限分類器所拒（⛔ 屬遠端之拒）⇒ KL 親手推送（非強推·①） |
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
- `1`：`git merge-base --is-ancestor 3b35daa… fe1fe3b…` ⇒ `rc 0`；`git rev-list --count 3b35daa..fe1fe3b` ＝ `5`；反向 ＝ `0`；`git rev-list --merges 3b35daa..fe1fe3b` ＝ 空。
- `2`：`git diff --name-only 3b35daa fe1fe3b -- app.py ":(glob)verify/*.py"` ⇒ `app.py`、`verify/selection_pipeline.py`（`2` 列）；判別力：去 `:(glob)` ⇒ `5` 列（另 `verify/probes/probe_WG9363_k953.py`、`verify/probes/probe_WG9367_adj4.py`、`verify/probes/probe_WG9370_adj4mut.py`）；`fe1fe3b:app.py` ＝ `da3c67a0f409273918246fd3d12218afa8f23a9c`；`fe1fe3b:verify/selection_pipeline.py` ＝ `a1d46f7d9a41a5d99808a7fdfe2bc27d8dfb86fb`。
- `3`：逐筆（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）：

| `commit` | 命中列數 | 出艙 |
|---|---|---|
| `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583` | `0` | （空） |
| `7063caa3e8068bb74d9a65c2b28ecb6d62af2eaa` | `0` | （空） |
| `a5e9b0bdc87f05a3eb1145e0cd83277fa1fa2b29` | `2` | `app.py`、`verify/selection_pipeline.py` |
| `b0dae3be938fd80458f0fd94b45e04d5a8037b6e` | `0` | （空） |
| `82ee12cac33623f114c99318869ffdbad1feaab2` | `0` | （空） |

⇒ 命中者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `a5e9b0b…`。

**④ 之前值**（快轉前·`<O>\contains_before.txt`）：`git branch -r --contains a5e9b0b…` ＝ `origin/verify/W-G.9-370-selfchk`（唯一）。

**快轉**：🔴 **快轉由 KL 執行**。CC 於前置皆符後以分開之呼叫發 `git push origin fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583:refs/heads/wip/s1-endpart`，為本工作階段之自動權限分類器所拒（理由 `Merge Without Review`·⛔ 達遠端）；CC ⛔ 繞道而停機回報；KL 親手推送 `fe1fe3b → wip/s1-endpart`，並示「此為執行者之更易，單之受詞與期⛔ 變」。

**快轉後即出艙**（`<O>\post0.txt`·`<O>\post0_pop.txt`）：
- ①：`git ls-remote origin refs/heads/wip/s1-endpart` ＝ `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`。
- ②：遠端 heads ＝ `37`；除 `wip/s1-endpart` 外之 `36` 列與 `<O>\heads_before.txt` 逐列同（`diff rc 0`）。
- ③：生產碼 `34` 檔（母體：`app.py` `1` ＋ `verify/` 頂層 `*.py` `33`·以 `git ls-tree` 正面過濾）於新主線 vs `fe1fe3b` 相異 ＝ `0`（空輸出）；判別力 vs `3b35daa` ＝ `2`（`app.py`、`verify/selection_pipeline.py`）。
- ④：`git branch -r --contains a5e9b0b…` ＝ `origin/verify/W-G.9-370-selfchk`、`origin/wip/s1-endpart`。

其後 `git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`。

## ④　三塊之實得與三簿之改前改後

抽取式依 `§五-1` 末（附錄標題列後之第一個 ```` 開列至恰四反引號之閉列·逐列 `\n` 相接末附 `\n`·UTF-8）；`<O>\extract.txt`、`<O>\append.txt`。

| 塊 | bytes | `sha256` | 列 | 首列空 |
|---|---|---|---|---|
| `K14` | `2942` | `94578049d9e4b55c37e5944ce378b2f8c26b498924df121057c440c5755d7484` | `10` | 是 |
| `E14` | `3581` | `cb4d338d77f2e368c40c85009c8029582fe097a4a344191d77eb561ef6607a48` | `20` | 是 |
| `P24` | `3311` | `17a0e122689c01b882f9967f39c45f013116d86fadb857ef19fa2f9162f1d713` | `22` | 是（`⬜` 子字串框 `5`·列框 `3`） |

| 簿 | 改前 bytes／blob | 改後 bytes／blob | 嚴格前綴 | 尾 ＝ 塊 | `numstat` | CR |
|---|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `551947`／`c8ad07d49292e380551cea55bb5f75563b0bc317` | `554889`／`d21ded917960e6dd98215ebdae9a54e38b98a343` | 真 | 真 | `10`／`0` | `0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1134714`／`638b105b09a1d54274ecd82b1ee1bc4f4cc1c50e` | `1138295`／`2a49470e2a79e32c9153621e3d0d7086b7cd0ccc` | 真 | 真 | `20`／`0` | `0` |
| `CLAUDE.md` | `351013`／`10861d8050acfa7a819336f457294baad56a7511` | `354324`／`35b4d04996ce770e5e92ca7a42e3271b050b3bd7` | 真 | 真 | `22`／`0` | `0` |

`GB` 簿⛔ 動。

## ⑤　工項一之 `checkidx`、`gen_fa_index`

- 塊 `CK`／`GF` 自 `fe1fe3b:docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳抽出：`CK` `1539` B·`00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；`GF` `2445` B·`b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `§五-1` 項 `6`）；寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
- `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md`：塊 `P24` 附前 `rc 0`（參照）·附後 `rc 0`；末列皆逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`·出艙 `則 124；加註節 14；列 158`；`cmp <O>\FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md` ⇒ 逐位同。

## ⑥　`§二` 之放行（KL 之逐字）

- 入主線之請示之答（KL `2026-10-07 13:24`·單 `§二` 所錄）：「請示答：是」「畫面核對無誤」。
- 本窗之 KL 之語（於對話·逐字）：「工項零′ 之快轉已由 KL 親手推送（fe1fe3b → wip/s1-endpart）；此為執行者之更易，單之受詞與期⛔ 變。請自「快轉後即出艙」①〜④ 接續，④ 之前值以你已記者為準，報告 ③ 載「快轉由 KL 執行」。工項零、一、二（零生產碼）推 wip/s1-endpart，KL 放行（依單 §二 射程 (b)）。工項三於收工閘皆符後辦。」

## ⑦　pre-flight

`python verify/probes/probe_order_preflight.py <本單>`（態 `fe1fe3b`·`rc 0`·stderr `0` B）：🔴 機械 `0` 項；🟡 提示 `3` 項——`P-4` `:77`、`P-4` `:185`、`P-4` `:259`：皆依單 `§五-1` 項 `7` 之**具名豁免**（`:77` 箭頭之座標系 ＝ 主線至側支之端·表內自載；`:185` ＝ 改前至改後·表內自載；`:259` 係交接文之名·⛔ 為方向之轉引）；ℹ️ 記錄 `2` 項：`P-5` 相符（受詞 `46000` B）、`P-3` `app.py` `def main` 區間（AST）＝ `21799`–`29519`（本單⛔ 用）。

`§零-1` 之重算（`<O>\occ.txt`、`<O>\occ_meaning.txt`）：`wg9268_gate6_occupancy.py fe1fe3b W-G.9-371 W-G.9-370 W-G.9-397` `rc 0`·母體 `978` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）·各列 ＝ 單之表；意指占用（母體 `2799` 檔·列框）：`588` 裸 `34`、`589` 裸 `42`、平形／B 形／C 形皆 `0`；對照 `587` 裸 `45`／平形 `4`／B 形 `0`／C 形 `3`；塊名 `K14`／`E14`／`P24` 二框皆 `0`／`0`，對照 `K13` 塊框 `2`／`6`、名框 `2`／`10`。

## ⑧　CC 讀塊時認為與倉之事實不符之處

無。

## ⑨　CC 之自捕與自解

- **自捕 `1`（量測器紅·非受詞紅）**：快轉後出艙 ③ 之母體計數，首次以 `git ls-tree --name-only <rev> -- app.py ':(glob)verify/*.py'` 取之 ⇒ `fatal: … pathspec magic not supported by this command: 'glob'` 而印 `母體檔數 = 0`。因「`34` 檔」之母體⛔ 可為 `0`，判為量測器紅；改以 `git ls-tree` 正面過濾（`app.py` `1`·`^verify/[^/]+\.py$` `33`）重量 ⇒ `34`。③ 之相異數（`git diff` 支援 `:(glob)`）不受影響。
- **自捕 `2`（照實記）**：快轉之 `push` 被本工作階段之權限分類器所拒 ⇒ CC 停機回報、⛔ 繞道；KL 親手推送（③）。
- **照實記**：`commit` 訊息之首段逐字依單；末附 `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` 一列，同倉內 `W-G.9-370` 各 `commit` 之體例。
- **本批之自解清單**：無。

## ⑩　各段耗時（本機時刻·`+0800`）

| 段 | 起訖 |
|---|---|
| `§零-0`〜`§零-3`、工項零′ 前置、塊之唯讀抽取 | `14:00`〜`14:05` |
| 停機（候 KL：快轉之 `push` 為權限所拒） | `14:05`〜`15:19` |
| 快轉後出艙 ①〜④ | `15:19` |
| 工項零（`commit`·`push`） | `15:20` |
| 工項一（附錄·`checkidx`·`gen_fa_index`·`commit`·`push`） | `15:20`〜`15:21` |
| 工項二（本報告） | `15:21`〜 |
