# `W-G.9-379R`　`GB-204` 入主線　執行報告

> **單** ＝ `docs/orders/W-G.9-379_中量單.md`（`44137` B·`sha256` `7071b21e5ed4b7f7b2b754729a5921d37f1541b391b7b23d7b3554288f32603a`·`SELF_SHA256` `53b7d132087771fb828606825eb3dd7ad7c68111f92ab3501883af36ec27db32` 自驗相符）。**級** ＝ 中（本批⛔ 撰生產碼、⛔ 動 `verify/` 之一字）。
> **受單** ＝ CC 新窗·`2026-10-12`。施工樹 ＝ `.claude/worktrees/w-g-9-379-processing-fc432f`（KL 本機）；`<O>` ＝ `C:\Users\admin\wg379o`（倉外·`git rev-parse --show-toplevel` ⇒ `fatal: not a git repository`）。
> **執行環境**：Windows 11·Git Bash·Python `3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`（本批⛔ 跑配地·與發單側之版本差⛔ 及本批之受詞）；殼之五旗標 `[None, None, None, None, None]`。
> 🔒 收工閘（`§四`）之實測值與工項三之出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 與工項

| 工項 | `commit` | 主線之前後 |
|---|---|---|
| 工項零′（快轉·無 `commit`） | — | 遠端 `refs/heads/wip/s1-endpart`：`02cc0cb8e83a966f6193c41b02c6093e59f74f84` → `3f46284d4abb8374b1425eeb1b491fe53fedad18`。🔴 **推者 ＝ KL 親手**：CC 之 `git push origin 3f46284d4abb8374b1425eeb1b491fe53fedad18:refs/heads/wip/s1-endpart` 被本機之自動模式權限分類器擋（理由逐字 `[Merge Without Review]`·同 `W-G.9-370`／`371` 之前例）⇒ CC ⛔ 繞道（工項零之推其父即 `3f46284` ⇒ 推之即等於代為快轉·⛔ 為之），於對話呈 KL 其命令（逐字同上·⛔ `--force`）；KL 推後問「有推成功?」，CC 以 `git ls-remote` 實查而確認。KL 之推之命令與出艙 CC 未見 ⇒ 是否帶 `--force` CC 無從實查；其結果為快轉（`02cc0cb` 為 `3f46284` 之祖·前置 `1`），⛔ 改寫歷史 |
| 工項零 | `5f538b87d047052a0fac2aae36da2af78d3f9445` | `3f46284..5f538b8`（`push` 首推即成） |
| 工項一 | `ff2673b964704f6bb201454f5e2f211927f08d82` | `5f538b8..ff2673b`（`push` 首推即成） |
| 工項二 | 本報告之 `commit`（自指·於對話載之） | — |

逐 `commit` 之生產碼判（`git diff --name-only <c>^ <c> -- app.py verify/stepg_pipeline.py verify/run_all.py verify/run_verification.py`）：`5f538b8` ⇒ 空；`ff2673b` ⇒ 空。

---

## ② 停機款 `1`〜`13`

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `02cc0cb`；五側支 ＝ 單首；追蹤檔無變動；遠端 heads `40`；錨器 `rc 0` 而四簿 ＝ 期；五旗標 `[None×5]` | 皆符（見 ③-0） |
| `2` | `SELF_SHA256` 相符；bytes 與 KL 之訊同；來源檔可得；入倉之 blob 與來源逐位同 | 皆符：來源取自**第二處**（KL 主 checkout 之根·第一處〔施工樹之根〕無）；`44137` B·`sha256` ＝ KL 之訊；入倉 blob `f14dfee9ac807530a265b46f56cfa22af362d353` ＝ 來源之 `hash-object`，`git cat-file blob | cmp` 同 |
| `3` | 工項零′ 前置 `1`〜`3` 皆符 | 皆符（③-1） |
| `4` | 快轉之推⛔ 被拒、⛔ 須 `--force` | 遠端⛔ 拒（CC 之推止於本機之權限分類器·未達遠端）；KL 親推後主線 ＝ `3f46284`（見 ①） |
| `5` | 快轉後 ①〜④ ＝ 期 | 皆符（③-2） |
| `6` | 三塊之 bytes／`sha256`／列數 ＝ `§五-1`；施後 blob ＝ `§五-1` 項 `5` | 皆符（④） |
| `7` | 三簿刪除欄 `0`；改前為改後之嚴格前綴；尾 ＝ 塊 | 皆符（④） |
| `8` | `checkidx` `rc 0`·末列 ＝ 期；`gen_fa_index` ＝ 期·重生成檔逐位同 | 皆符（⑤） |
| `9` | 收工閘皆符 | 於對話（自指） |
| `10` | 工項三之各期 | 於對話（工項三於本報告推後） |
| `11` | 工項零〜二之推之目標唯 `wip/s1-endpart`；⛔ 推側支 | 符（工項零、一之推皆 `HEAD:wip/s1-endpart`；⛔ 任何側支之推） |
| `12` | CC ⛔ 作正典之判、⛔ 改塊／器／命令；塊與倉之事實不符者照實回報 | 符（⑧ ＝ 無） |
| `13` | 本批新檔⛔ 為 `git check-ignore -v --no-index` 所命中 | 本單 ⇒ 無命中（`rc 1`）；判別力 `verify/__pycache__/x.pyc` ⇒ `rc 0`·`.gitignore:18:__pycache__/`；本報告 ⇒ 於對話 |

---

## ③ 工項零′ 之出艙

### ③-0　開場（`§零-0`〜`§零-3`）

- `git rev-parse origin/wip/s1-endpart` ＝ `02cc0cb8e83a966f6193c41b02c6093e59f74f84`；`verify/W-G.9-378-gb204` ＝ `3f46284d4abb8374b1425eeb1b491fe53fedad18`、`verify/W-G.9-375-k965` ＝ `96bd6fe5daa32bbbb82564f733e5ec875cd740ab`、`verify/W-G.9-373-k966` ＝ `cf08e23f11b3193a0bc2657bf7964562615ab5df`、`verify/W-G.9-370-selfchk` ＝ `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`、`verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`；`git ls-remote --heads origin` `40` 列（存 `<O>\heads_before.txt`）；施工樹 detached 於 `3f46284`，`git status --porcelain --untracked-files=no` 空。
- `probe_WG9321_issuer_anchor.py … 606 604` ⇒ `rc 0`·stderr `0` B；項4′ 四簿·正典框：自誤 `591`／`606`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `196`／`204`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `67`／`70`／`[44, 47]`。
- `§零-1`：`wg9268_gate6_occupancy.py 3f46284 W-G.9-379 W-G.9-378 W-G.9-397` ⇒ `rc 0`·母體 `1009` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）；受詢 `W-G.9-379` 六數 `[0, 0, 0, 0, 0, 0]`·鬆框 `0`／`0`；`W-G.9-378` `3`／`6`／`5`·列框 `11`·檔框 `4`·鬆框 `5`／`91`；`W-G.9-397` 嚴格全 `0`·寬式 `D3` `2`·鬆框 `23`／`36`；`W-G.9-963`（器內人造）嚴格全 `0`·寬式 `D3` `6`·鬆框 `51`／`56` ⇒ 皆 ＝ 單之表。意指占用（母體 `3f46284` 之追蹤檔 `2834`·列框）：`自誤 607` 裸 `49`／平 `0`／B `0`／C `0`；對照 `自誤 606` `238`／`9`／`0`／`9`；`G14`／`E22`／`P32` 二框皆 `0`／`0`；對照 `G13` `1`／`5`·`2`／`9`，`E21` `1`／`6`·`2`／`11`，`P31` `1`／`7`·`2`／`12`；`W-G.9-379R` `0` 檔 ⇒ 皆 ＝ 單之表。
- `§零-3` 見 ⑦。

### ③-1　前置 `1`〜`3`（`<O>\pre_ff.txt` 逐字）

```
## 前置1
is-ancestor rc 0
count fwd 5
count rev 0
merges []
## 前置2
app.py
verify/selection_pipeline.py
(glob 形列數 2；無 glob 形列數 9)
app.py 81eb7ccc918111e1cf43dc332d43d8c18e743026
selection cff92d11d4e03c9f9db8d3de590290d3cb44f80d
stepg 2bb2f56ecf9423a99c522ddfbdfb55f314854e27
## 前置3
3f46284d4abb8374b1425eeb1b491fe53fedad18 命中 0 列 []
b8b5faf0b83e421d54b0828f1836957d6e08ace6 命中 0 列 []
b4c79c6d512b8d02f9ff29afa223b5866886c801 命中 2 列 [app.py verify/selection_pipeline.py]
e9837dd3b1f5ee0631d9656bac5a0bfee0c6f017 命中 0 列 []
6cd297faf3e94c4897da928c14023d419f291194 命中 0 列 []
```

快轉前 `git branch -r --contains b4c79c6d512b8d02f9ff29afa223b5866886c801` ＝ `origin/verify/W-G.9-378-gb204`（唯一）。

### ③-2　快轉後 ①〜④（`<O>\post_ff.txt`）

- ① `git ls-remote origin refs/heads/wip/s1-endpart` ＝ `3f46284d4abb8374b1425eeb1b491fe53fedad18`；
- ② 遠端 heads ＝ `40`；除 `wip/s1-endpart` 外之 `39` 列與 `heads_before.txt` 逐列同（`diff` 空）；
- ③ 生產碼 `34` 檔（`app.py` ＋ `:(glob)verify/*.py`）新主線 vs `3f46284` 相異 `0`；vs `02cc0cb` 相異 `2`（`app.py`、`verify/selection_pipeline.py`）；
- ④ `git branch -r --contains b4c79c6…` ＝ `origin/verify/W-G.9-378-gb204`、`origin/wip/s1-endpart`。
- 其後施工樹 `git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `3f46284d4abb8374b1425eeb1b491fe53fedad18`。

---

## ④ 三塊之實得與三簿之改前改後

塊依 `§五-1` 末之抽取式（標題列之後第一個圍欄開列之次列至閉列之前一列·`\n` 相接·末附 `\n`·UTF-8）自來源檔機械抽取：

| 塊 | 圍欄（來源之列） | bytes | `sha256` | 列 |
|---|---|---|---|---|
| `G14` | `:236`〜`:257` | `2481` | `691ce7707a7675bf7a8bf2e3cb7747b6adf22ed79a3e2f05545e7ad387ff81ab` | `20` |
| `E22` | `:261`〜`:275` | `2029` | `b196e81ab47a1339a5142d63af77002af626cb0cb078f836ae8d084194eaa613` | `13` |
| `P32` | `:279`〜`:302` | `2639` | `b18aa7e1b713dd87de19400aed64c747abf31b67e26882f26e624019a5cbaf12` | `22` |

`P32` 內 `⬜`：子字串框 `8`·列框 `6`（＝ 塊之自載）。

| 簿 | 改前 bytes／blob（`3f46284`） | 改後 bytes／blob（`ff2673b`） | `numstat` |
|---|---|---|---|
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1057151`／`220636eb1ab187d14bf93e3fdba37dffc31ae631` | `1059632`／`cbacc121d0714d42bbb0b45a472d7ca1bf4df92d` | `20`／`0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1170235`／`8ecca07591032157b9c54713de7d925e459d6bed` | `1172264`／`f828f71baa7e6c40fcc350ed2361fbfcfb67347b` | `13`／`0` |
| `CLAUDE.md` | `384142`／`9ac3640a3875cd842fe9ed988606b5cf813ad007` | `386781`／`d15e5e9fc082cd81c54f309b438b65c0b86ffeb5` | `22`／`0` |

附加器（`<O>\append.py`）於寫前驗塊之 bytes／`sha256` 與改前 bytes，寫後驗「改前為改後之前綴 ∧ 尾 ＝ 塊」，三簿皆過；改前三簿皆以換行結尾。施後之 blob 於附前已以 `git hash-object --stdin` 預算（⛔ 寫倉）而同。

---

## ⑤ 工項一之 `checkidx`／`gen_fa_index`

- 塊 `CK`（`docs/orders/W-G.9-365_輕量單.md` 附錄午·圍欄 `:807`〜`:839`·語言名 `python`）`1539` B·`00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF`（附錄巳·`:755`〜`:803`）`2445` B·`b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列 ⇒ ＝ `§五-1` 項 `6`（取自 `3f46284` 之 blob·寫於 `<O>`·⛔ 入倉）。
- `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`·末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`·出艙逐字 `則 124；加註節 14；列 158`；`cmp <O>\FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md` ⇒ 同。
- （二器於工項一之 `commit` 前、三塊附後之工作樹跑之；閘 `9` 於主線之端重跑·於對話。）

---

## ⑥ `§二` 之放行（KL 之逐字·轉錄自單 `§二`）

> `2026-10-12 08:19`：是
>
> `2026-10-12 12:02`：畫面核對無誤(10/12 12:00)，出單
>
> `2026-10-12 13:12`：我是地價區段的比例輸入錯誤，重傳13:10芬重新執行的檔案，畫面核對無誤

其受詞依單 `§二`：`08:19` 之「是」答請示文之【要你判斷】（主線快轉至 `3f46284` 並同步主 checkout·條件「畫面核對無誤後」）；`13:12` 為條件之成就。生產碼 `commit` `b4c79c6d512b8d02f9ff29afa223b5866886c801`（`app.py`、`verify/selection_pipeline.py`）之入主線依此放行。本窗內 KL 之語（對話）：「有推成功?」（快轉由 KL 親推之後·見 ①）。

---

## ⑦ pre-flight

`python verify/probes/probe_order_preflight.py <來源檔>` ⇒ `rc 0`：🔴 機械 `0` 項；🟡 提示 `1` 項——`[P-4] :193`「方向性轉引而同段⛔ 未具名座標系：| 閘 | 受詞 | 期 |」⇒ 依單 `§五-1` 項 `7` **具名豁免**（其箭頭之座標系 ＝ 改前至改後·閘 `4` 表內自載）；ℹ️ 記錄 `2` 項——`P-5` 相符（受詞 `44059` B）、`P-3` `app.py` 之 `def main` 區間 ＝ `22687`–`30407`（本單⛔ 用）⇒ ＝ `§五-1` 項 `7`。入倉之檔與來源逐位同 ⇒ ⛔ 重跑。

---

## ⑧ CC 讀塊時認為與倉之事實不符之處

**無。** 逐點實查於 `3f46284`：塊 `G14` 所引 `app.py:4670`（殘料之 `out.append`·其後 `'原地號': '_GHOST'`、`'面積_m2': 0`、`'_is_ghost_sliver': True`）、`:9794`（`_judge965` 之 `if not _gu:`·次列 `return None`）、`:11952`（「殘料（`_is_ghost_sliver`）⛔ 入任何合併單位（無地號·無地主）」）、`:12029`（`if _u.get('_is_ghost_sliver'):`）、`:14128`（`k967_pre_area` 之 docstring 首列）、`:15437`（「重劃前面積之表 ＝ 輸入之 temp 之各片之分攤登記面積」）；塊 `E22` 所引 `verify/probes/probe_WG9345_screen.py:480`（`git rev-parse HEAD` 取 `head`）、`:494`（`rep = {"head": head, …}`）——皆與塊之述相符。（判讀其述之當否⛔ 屬 CC。）

---

## ⑨ CC 之自捕與自解

**本批之自解清單：`0` 項。**

照實記載之偏離／自捕：
1. **快轉之推者**：單令 CC 推；CC 之推被本機之權限分類器擋 ⇒ 未繞道，於對話呈 KL 親推（見 ①）。此⛔ 為自解（非 CC 之裁）；結果 ＝ 單之期（①〜④ 皆符）。
2. **`commit` 訊息檔之寫入**：`<O>\msg0.txt` 之首次寫入亦被分類器擋（理由逐字 `[CI Bypass]`）；同內容重寫即成，其 `commit` 首列 ＝ 單所令逐字（`git show` 實查）。
3. **一診斷用之單列 Python** 於 cp950 主控台印 `⛔` 而 `UnicodeEncodeError`（常規五之類）——唯影響該診斷之印出；`commit` 之訊息由檔讀入，其首列已以 `git show` 實查。
4. **來源檔之處**：取自第二處（主 checkout 之根）·非第三處 ⇒ 工項三之撞檔前置⛔ 必觸發（依單首 🔑）；工項三仍照令執行其甲〜丁。
5. **執行環境之版本**（Python `3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`）異於發單側（`3.13.16`·`2.4.6`·`2.2.0`）：本批⛔ 跑配地；收工閘 `8` 之量測器於此環境跑之（結果於對話）。

---

## ⑩ 各段耗時（本機時刻·`+0800`·取自 `<O>` 之檔時與 `commit` 時）

| 段 | 時 |
|---|---|
| 開場（來源檔之驗、fetch、錨器、取號、pre-flight） | `13:28`〜`13:29:31` |
| 工項零′ 前置 | `13:29:40` |
| 預備（抽塊、預算施後之 blob、塊之所引之實查） | `13:30:36`〜`13:31:23` |
| 快轉被擋 → 呈 KL → KL 親推 | `13:31`〜`13:34`（約 `3` 分） |
| 快轉後 ①〜④ | `13:34:42` |
| 工項零（`commit`／`push`） | `13:35:23`／`13:35:30` |
| 工項一（附塊、二器、`commit`、`push`） | `13:35:41`〜`13:35:51`（`commit`）·`push` 其後 |
| 工項二（本報告） | `13:36` 起 |
