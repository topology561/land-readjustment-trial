# `W-G.9-365R`　指令檔之載入改制　執行報告（⛔ 零生產碼）

> 受單 ＝ CC（施工樹 ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-365-lightweight-form-694f6a`·Windows）。單 ＝ `docs/orders/W-G.9-365_輕量單.md`。級 ＝ 輕。
> 本報告⛔ 記收工閘之實測值與工項四之出艙（自指）——二者於對話出艙。

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 訊息首列（逐字·另附 `Co-Authored-By` 尾列·同 `W-G.9-364` 各 `commit` 之體例） | 生產碼判法（`git diff --name-only <前>..<本> \| grep -xE '…四檔…'`）之出艙 |
|---|---|---|---|
| 零 | `9727c371a7cbb564ab29c1b08463ca5928b7278a` | `W-G.9-365 工項零：本單原封入倉 ⛔ 零生產碼` | 空（`rc 1`·命中 `0` 列） |
| 一 | `2b210b13353ac583f9e4634aa72993ae98a3485e` | `W-G.9-365 工項一：.claude/ 之載入改制（claudeMdExcludes·常設規則索引·技能之載入設定與失準之更正·審查代理之更正）⛔ 零生產碼` | 空（`rc 1`·命中 `0` 列） |
| 二 | `e1cc2cbb855b76b076c80b410ebac0a7af435db4` | `W-G.9-365 工項二：AGENTS.md 之更正 ＋ CLAUDE.md 之載入改制之記（末端追加）⛔ 零生產碼` | 空（`rc 1`·命中 `0` 列） |
| 三 | （本報告之 `commit`·自指 ⇒ 於對話出艙） | `W-G.9-365 工項三：執行報告入倉 ⛔ 零生產碼` | （同上） |

三筆皆 `git push origin HEAD:wip/s1-endpart` 首推即成（快轉：`0e0edb3..9727c37`、`9727c37..2b210b1`、`2b210b1..e1cc2cb`），⛔ `--force`。

`git show --numstat`：工項零 ＝ `docs/orders/W-G.9-365_輕量單.md` `841`／`0`；工項一 ＝ `.claude/agents/redistribution-reviewer.md` `9`／`9`、`.claude/rules/常設規則索引.md` `123`／`0`、`.claude/rules/配地碼之領域指引.md` `18`／`0`、`.claude/settings.json` `9`／`0`、`.claude/skills/README.md` `9`／`0`、`.claude/skills/cad-layer-semantics/SKILL.md` `11`／`0`、`.claude/skills/corner-selection-rules/SKILL.md` `13`／`0`、`.claude/skills/failure-archaeology-index/SKILL.md` `158`／`0`、`.claude/skills/fixture-provenance/SKILL.md` `6`／`0`、`.claude/skills/g-formula-rules/SKILL.md` `11`／`0`、`.claude/skills/stop-conditions/SKILL.md` `12`／`0`、`.claude/skills/validation-runbook/SKILL.md` `11`／`0`、`.claude/skills/wave-discipline/SKILL.md` `13`／`0`（`13` 檔）；工項二 ＝ `AGENTS.md` `3`／`3`、`CLAUDE.md` `8`／`0`。

## ② 停機款 `1`〜`11` 之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `0e0edb3`；追蹤檔無變動；heads ＝ `35`；`§零-0` 項 `3` 之 `rc 0` 且四簿 ＝ `562`／`577`、`194`／`201`、`80`／`95`、`52`／`55` | `git fetch` 後 `origin/wip/s1-endpart` ＝ `0e0edb3a40e68efd6748c08c198eaa51851b603c`；`ls-remote --heads` `35` 列；`checkout --detach` 後 `status --porcelain --untracked-files=no` 空；`probe_WG9321_issuer_anchor.py` `rc 0`·stderr `0` B·「項4′ 四簿·正典框」：自誤 `562`／`577`、`GB` `194`／`201`、`VR` `80`／`95`、`K-9` `52`／`55` ⇒ 未觸 |
| `2` | `SELF_SHA256` 自驗相符；KL 之訊所載 bytes 與本單相符；來源檔可得；入倉 blob ＝ 來源 | `SELF_SHA256` 單載 ＝ 實算 ＝ `824fc8852ccad28ea460f5eb2b0e6bfe571b63eb6ff8f95f5d9bb2e308810ffc`（受詞 `101887` B）；來源 `101965` B·`sha256` `4f641f3270742afd6b8c50c92503ab5cd8f98302025340a2aea850c9c95c640e` ＝ KL 之訊所載；來源取自第二處（KL 主 checkout 之根·第一處 CC 施工樹之根無）；入倉 blob `8a450e3e370a3055c4cc6490df01048ca7da5b2f` ＝ 來源之 `hash-object`，`git cat-file blob` 之 `sha256` ＝ 來源 ⇒ 未觸 |
| `3` | 十七塊之 bytes／`sha256` ＝ `§五-1`；`git apply --check` 過；施後 blob ＝ `§五-1` 項 `19` | 見 ③：十七塊逐塊相符；`AG`／`AM` 之 `--check` 皆 `rc 0`（`--numstat` `9`／`9`、`3`／`3`）；施後 `15` 檔逐檔相符 ⇒ 未觸 |
| `4` | 九檔之刪除欄 `0`、改前為改後之嚴格前綴、尾 ＝ 塊 | 見 ③：九檔皆 `True` ⇒ 未觸 |
| `5` | `GF` 重生成 ＝ `FX`；`CK` 之 `rc`（工項二後）＝ `0`；`settings.json` 可解且 `hooks` ＝ 開工態 | 見 ④ ⇒ 未觸 |
| `6` | `§四` 收工閘皆符 | 收工閘於本報告推後量（自指）⇒ 於對話出艙 |
| `7` | `push` 目標 ＝ `wip/s1-endpart`、未被拒、⛔ `--force` | 三推皆快轉首推即成 ⇒ 未觸（第四推見對話） |
| `8` | 工項四之前提與出艙 | 工項四於收工閘後辦（自指）⇒ 於對話出艙 |
| `9` | CC ⛔ 判正典、⛔ 改塊／器／命令 | 塊、器、命令皆未改一字；CC 未發現塊文與倉之事實不符者 ⇒ 未觸 |
| `10` | 新檔皆⛔ 為 `check-ignore` 所命中 | `docs/orders/W-G.9-365_輕量單.md`、`.claude/rules/常設規則索引.md`、`.claude/rules/配地碼之領域指引.md`、`.claude/skills/failure-archaeology-index/SKILL.md` 皆 `rc 1`（無命中）；本報告見對話 ⇒ 未觸 |
| `11` | KL 於同一訊息逐字答問一「是」 | 見 ⑤ ⇒ 未觸 |

## ③ 塊之實得與九個末端追加之受詞

抽取：以 `§五-1` 末之抽取式（圍欄開列之次列至閉列之前一列，逐列 `\n` 相接並末附 `\n`，UTF-8）自來源檔逐塊二進位寫出。

| 塊 | 圍欄（開／閉列） | bytes | `sha256` | 列 | 首位元組 |
|---|---|---|---|---|---|
| `S` | `183`／`208` | `503` | `0fc742bddfed9d161e48c028f982f951ba2268b191e4bcf7208f74cf9970b248` | `24` | `{` |
| `R1` | `212`／`336` | `24624` | `b8d436b50ad5e1bda0a2978390cd17e5489b96fdf84a33dd62a43619a6f9eeb9` | `123` | `#` |
| `R2` | `340`／`359` | `1365` | `256e1249497dfa5c78706dd6177023085755b4a14d0aebdb619efa47e473b086` | `18` | `-` |
| `FX` | `363`／`522` | `21080` | `df14158df94ff8d94ee12cfd802c5d7fc1f4b213fd53ee891087a8490b666b1c` | `158` | `-` |
| `C1` | `526`／`538` | `1292` | `42cceb7b4e62e70d364bed753949c9a9650ac482fa6a1100f88355346c745084` | `11` | `\n` |
| `C2` | `542`／`556` | `2081` | `ea084f79db2a7047485b765ef128fdb10d9cdbd06c229eb9e79b6188e7777997` | `13` | `\n` |
| `C3` | `560`／`572` | `1047` | `960d3e7b4752f192168207bb0b7469b38f35878b974aa126e92769c830ff5ecc` | `11` | `\n` |
| `C4` | `576`／`588` | `1080` | `b2c5281ccd435807610c9859e262b6e44ed3e7d625b007c100c1cd09514c1ead` | `11` | `\n` |
| `C5` | `592`／`599` | `351` | `7defdb1f5720e62a0d743bad3a7ea229163742f48dabb915a2133e06226a6e04` | `6` | `\n` |
| `C6` | `603`／`613` | `750` | `5bc151571c9a8a7ec9fa86bb60c050d038bc8cbfd685fe1580028ffe9ee168b3` | `9` | `\n` |
| `C7` | `617`／`630` | `1182` | `d39951237e9d41bc4e3ed1c3984b64b1d71e29e1f34b4502526ce29d6d20a226` | `12` | `\n` |
| `C8` | `634`／`648` | `997` | `421246f2f2441eb7d75fa05c62929d491831376846657ff05ac07fd51a49a810` | `13` | `\n` |
| `AG` | `652`／`709` | `5592` | `db2aef49c0ac2af60c9d7bbbe67a832fd40bb8e6787f555cb3291c030df8f149` | `56` | `d` |
| `AM` | `713`／`738` | `2025` | `faff54de82aeccae369f9bd1749461b9641bb485b10561e33058b2709f9123c4` | `24` | `d` |
| `P19` | `742`／`751` | `2640` | `3a1b8c5bd76d41fd75d76ba23111f599a60d87517d6dc85d0b68f8509b5bf380` | `8` | `\n` |
| `GF` | `755`／`803` | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | `#` |
| `CK` | `807`／`839` | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | `#` |

十七塊之 bytes／`sha256`／列逐塊 ＝ `§五-1` 項 `2`〜`18`。`GF`／`CK` 置倉外（scratchpad），⛔ 入倉。

開工態之受詞（`git rev-parse 0e0edb3:<檔>` ＝ 工作區 `hash-object`）逐檔 ＝ `§一` 項 `3`（`12` 檔）；`git ls-tree 0e0edb3 .claude/rules/ .claude/skills/failure-archaeology-index/` ＝ `0` 列；受詞皆以 `0x0A` 結尾（`tail -c1`）、CR `0`。

九個末端追加之受詞（改前全檔為改後之嚴格前綴，且改後之尾 ＝ 塊·逐位）：

| 塊 | 受詞 | 改前 bytes | 改後 bytes | 嚴格前綴且尾 ＝ 塊 |
|---|---|---|---|---|
| `C1` | `.claude/skills/g-formula-rules/SKILL.md` | `3440` | `4732` | `True` |
| `C2` | `.claude/skills/corner-selection-rules/SKILL.md` | `7915` | `9996` | `True` |
| `C3` | `.claude/skills/cad-layer-semantics/SKILL.md` | `17201` | `18248` | `True` |
| `C4` | `.claude/skills/validation-runbook/SKILL.md` | `8292` | `9372` | `True` |
| `C5` | `.claude/skills/fixture-provenance/SKILL.md` | `5852` | `6203` | `True` |
| `C6` | `.claude/skills/README.md` | `2386` | `3136` | `True` |
| `C7` | `.claude/skills/stop-conditions/SKILL.md` | `2651` | `3833` | `True` |
| `C8` | `.claude/skills/wave-discipline/SKILL.md` | `2960` | `3957` | `True` |
| `P19` | `CLAUDE.md` | `334109` | `336749` | `True` |

施後之 blob（`git hash-object --no-filters`）：`§五-1` 項 `19` 之 `15` 檔逐檔相符（bytes 亦符），CR 皆 `0`。

## ④ 工項一之驗之出艙

- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`·出艙逐字 `則 124；加註節 14；列 158`；`cmp` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同。
- `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md`：
  - **工項一之態（必紅）** ⇒ `rc 1`；出艙逐字二列：`L88 命中列數=0: '指令檔之載入改制'`／`索引列數 123；內部字樣 120；外部指標 9；不合 1`。
  - **工項二之後（必綠）** ⇒ `rc 0`；出艙逐字一列：`索引列數 123；內部字樣 120；外部指標 9；不合 0`。
- `.claude/settings.json`：`json.load` 可解，`sorted(d)` ＝ `['claudeMdExcludes', 'hooks', 'skillOverrides']`；其 `hooks` 與 `git show 0e0edb3:.claude/settings.json` 之 `hooks` 相等（`True`；開工態之鍵唯 `['hooks']`）。
- 工項一施後 `git status --porcelain --untracked-files=all`：`M` `10` 列（`.claude/settings.json`、`.claude/agents/redistribution-reviewer.md`、八受詞）、`??` `3` 列（二 `.claude/rules/` 新檔、`failure-archaeology-index/SKILL.md`）；別無他列。工項二施後：`M AGENTS.md`、`M CLAUDE.md` 二列。

## ⑤ `§二` 之放行

KL 貼本單之同一訊息逐字：「請依 W-G.9-365_輕量單.md（101965 B·sha256 4f641f3270742afd6b8c50c92503ab5cd8f98302025340a2aea850c9c95c640e）辦理。問一之答：是。」⇒ 問一 ＝ 「是」。

## ⑥ CC 之自捕與自解

**自捕**

1. **量測器紅（`常規五`·自身工具）**：工項一前之快照器以 f-string 寫 `b.endswith(b'\\n')`，其字面為「反斜線＋`n`」二字元 ⇒ 十二受詞皆印 `ends_nl=False`，與 `§一` 項 `3`「皆以換行結尾」相牴觸。未據以判任何事；改以 `tail -c1 | od` 重量 ⇒ 十五檔末位元組皆 `0a`。該欄僅屬顯示，快照之 bytes 本身未受影響（其後之嚴格前綴驗即以之為據）。
2. **heredoc 之守衛**：一次以 bash herestring（`<<<`）餵檔清單之命令為 PreToolUse hook `verify/tools/wg9237_heredoc_guard.py` 所阻（H1）——係 CC 誤用；改以 `Write` 落檔之腳本以路徑執行。附帶證此 hook 於本施工樹生效。

**自解清單**（`作業常規之追加五`）

1. 對照甲′ `W-G.9-396`：器之出艙將其標為「甲（須 ≥1）」而宣告框六數皆 `0`；本單 `§零-1` 明定其角色為「鬆框之漏框偵察」（期：宣告框 `0`、鬆框非零）。實測宣告框 `0`、鬆框 `16`／`25` ＝ 單之表 ⇒ 依單之角色讀之。讀法二（器之標籤）與讀法一之後果皆不動土地；機械證據 ＝ 與 `§零-1` 表逐格相同（類 `8`·裝飾性標籤）。
2. pre-flight 之 🟡 四項（`P-1` `:807`、`P-4` `:642`／`:669`／`:720`）：與 `§五-1` 項 `21` 逐項同列、同提示；依單之具名豁免處之（非 CC 所自創之豁免）。
3. `commit` 訊息：首列逐字依單；另附 `Co-Authored-By` 尾列，與 `W-G.9-364` 五 `commit` 之既有體例相同（類 `3`·格式）。

## ⑦ 各段耗時（本機時鐘）

| 段 | 起 | 迄 |
|---|---|---|
| `§零`（開場·取號·pre-flight·抽塊） | `11:14:27` | `11:15:50` 前後 |
| 工項零（入倉·推） | `11:15:56` | `11:16` 前後 |
| 工項一（施·驗·推） | `11:16` 前後 | `11:17` 前後 |
| 工項二（施·驗·推） | `11:17` 前後 | `11:18:00` |
| 工項三（本報告） | `11:18` | 見對話 |
