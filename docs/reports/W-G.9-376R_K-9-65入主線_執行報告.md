# `W-G.9-376R`　執行報告：主線快轉至 `96bd6fe`（`K-9-65`／`K-9-58` ①②③／`K-9-70` 入主線）＋ 四簿之末端追加 ⛔ 零生產碼

> **單** ＝ `docs/orders/W-G.9-376_中量單.md`（`81939` B·`sha256` `5208739628f056d8a408840028b19ff1d5306ebb24a18ae9b3b39fc7f7561880`·`SELF_SHA256` 自驗相符）。**受單** ＝ CC 新窗（施工樹 ＝ `.claude/worktrees/w-g-9-376-processing-e12ab2`·Windows 11·Python 經 `python`）。**級** ＝ 中（⛔ 撰生產碼、⛔ 動 `verify/`、⛔ 跑 `run_verification`／`run_all`）。
> `<O>` ＝ `C:\Users\admin\wg9376_O`（倉外·⛔ 在任何 git 工作樹之內）。量測之殼之旗標出艙 `[None, None, None, None, None]`。
> 本檔⛔ 載收工閘之實測值與工項三之出艙（自指）——二者於對話出艙。

---

## ①　逐 `commit` 之 hash 與工項

| 工項 | `commit` | 說明 |
|---|---|---|
| 零′ | ⛔ `commit` | 遠端 `refs/heads/wip/s1-endpart`：前 `981f14308d51ac2cb5c4cb74792e13da459749a9` → 後 `96bd6fe5daa32bbbb82564f733e5ec875cd740ab`（`git push origin 96bd6fe5daa32bbbb82564f733e5ec875cd740ab:refs/heads/wip/s1-endpart`·出艙 `981f143..96bd6fe`·首推即成·⛔ `--force`） |
| 零 | `598e1bac57d3528ab4c94be6be58907ff9fbc122` | 本單原封入倉（`docs/orders/W-G.9-376_中量單.md`·`554`／`0`）；`git cat-file blob` 之 `sha256` ＝ 來源；推 `96bd6fe..598e1ba` |
| 一 | `ade68917a9e75c42f63d011397a1907bc49c9d52` | 四簿之末端追加（塊 `K19`／`G12`／`E19`／`P29`）；推 `598e1ba..ade6891` |
| 二 | 本檔所在之 `commit`（自指·其 hash 於對話出艙） | 本報告 |

逐 `commit` 之生產碼判（`git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`）：工項零 ＝ 空輸出（`0` 列）；工項一 ＝ 空輸出（`0` 列）；工項二 ＝ 於對話出艙。

## ②　停機款 `1`〜`13`（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `981f143`、四側支之值、施工樹追蹤檔無變動、heads `39`、`§零-0` 項 `3` `rc 0` 且四簿 ＝ 期、旗標 ＝ `[None×5]` | 主線 `981f14308d51…`；`verify/W-G.9-375-k965` `96bd6fe5daa3…`；`verify/W-G.9-373-k966` `cf08e23f11b3…`；`verify/W-G.9-370-selfchk` `fe1fe3bf59eb…`；`verify/W-G.9-367-adj4` `e7855ecf75ca…`；heads `39`；`git checkout --detach origin/verify/W-G.9-375-k965` 後 `status --porcelain --untracked-files=no` ＝ 空（`0` B）；器 `rc 0`·自誤 `584`／`599`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `195`／`202`／`[12, 87, 179, 181, 183, 184, 185]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `67`／`70`／`[44, 47]`；旗標 `[None, None, None, None, None]` ⇒ 未成就 |
| `2` | `SELF_SHA256` 相符；bytes ＝ KL 之訊；來源檔可得；入倉 blob ＝ 來源 | KL 之訊 `81939` B／`5208739628f0…`＝ 實算；`SELF_SHA256` 單載 ＝ 實算 `a443bad28ea8e71e455461b7be1da295807695abf56294dab89cb76da75a341c`；來源 ＝ 第二處（KL 主 checkout 之根·施工樹之根無之）；`git cat-file blob HEAD:docs/orders/W-G.9-376_中量單.md` 之 `sha256` ＝ `5208739628f0…`、blob `917e1ec4a09f613e522ea18d6f2995d8f1a39582` ＝ 來源之 `hash-object` ⇒ 未成就 |
| `3` | 工項零′ 前置 `1`〜`3` ＝ 期 | 皆 ＝ 期（見 ③）⇒ 未成就 |
| `4` | `push` 首推即成·⛔ `--force` | 首推即成 ⇒ 未成就 |
| `5` | 快轉後 ①〜④ ＝ 期 | 皆 ＝ 期（見 ③）⇒ 未成就 |
| `6` | 四塊 bytes／`sha256`／列數 ＝ `§五-1`；施後 blob ＝ `§五-1` 項 `6` | 皆 ＝ 期（見 ④）⇒ 未成就 |
| `7` | 刪除欄 `0`；改前為改後之嚴格前綴；尾 ＝ 塊 | `220`／`0`、`15`／`0`、`36`／`0`、`27`／`0`；四簿皆嚴格前綴、尾 ＝ 塊（以 `ade6891^`／`ade6891` 之 blob 驗）⇒ 未成就 |
| `8` | `checkidx` `rc 0`·末列 ＝ 期；`gen_fa_index` 出艙 ＝ 期·與倉內逐位同 | 見 ⑤ ⇒ 未成就 |
| `9` | 收工閘皆 ＝ 期 | 自指 ⇒ 於對話出艙 |
| `10` | 工項三之諸期 | 工項三後於本檔 ⇒ 於對話出艙 |
| `11` | 工項零〜二之 `push` 之目標皆 `wip/s1-endpart`；⛔ 推側支 | 工項零、一之目標皆 `HEAD:wip/s1-endpart`；側支⛔ 推 ⇒ 未成就（工項二同·於對話出艙） |
| `12` | CC ⛔ 判正典、⛔ 改塊／器／命令；塊與倉之事實不符者回報 | ⛔ 改一字；不符 ＝ 無（見 ⑧）⇒ 未成就 |
| `13` | 新檔⛔ 為 `git check-ignore` 所命中 | 本單 `git check-ignore -v` ⇒ `rc 1`（無命中）；本報告於對話出艙 ⇒ 未成就 |

## ③　工項零′ 之前置與快轉後之出艙（全部·存 `<O>\pre0_out.txt`、`<O>\ff_after.txt`）

**前置**：

```
1a is-ancestor rc 0
1b count A..B 8
1c count B..A 0
1d merges ''
2a :(glob) 形 列數 3 ['app.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']
2a′ 判別力［無 :(glob）］列數 10
2b app.py d6218273e0ba3cdf45598a37968eac6d907ebb58
2b verify/stepg_pipeline.py 2bb2f56ecf9423a99c522ddfbdfb55f314854e27
2b verify/selection_pipeline.py 96cbf3ffbdd36bbf4d02bf10e9635bbf69b5926c
3 母體筆數 8
3 96bd6fe5daa32bbbb82564f733e5ec875cd740ab 命中列 0 （空輸出）
3 a298c4c3b2f5472a5cc9d3957731b6c450cd6ac5 命中列 0 （空輸出）
3 9fc8e5b4a389a8f121150be7a219b790eb3f349d 命中列 3 ['app.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']
3 c19606c2ca808d8778f7fe2c6f9c8db7e7339906 命中列 0 （空輸出）
3 429151b7efb780b2ecb5823a40d08ce5185b91f0 命中列 0 （空輸出）
3 fd8a148a92524dde4d2f04a7d0ba88decf4186d7 命中列 0 （空輸出）
3 1cc8f5d48d530bb3da2d02e373972574ff18b55b 命中列 0 （空輸出）
3 3a48853f1fa30e8fabb925bd20b035238a0d43c0 命中列 0 （空輸出）
3 命中者 [('9fc8e5b4a389a8f121150be7a219b790eb3f349d', 3)]
```

（`A` ＝ `981f143…`、`B` ＝ `96bd6fe…`；命中者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `9fc8e5b4a389a8f121150be7a219b790eb3f349d`。）

**快轉後**：

```
① 96bd6fe5daa32bbbb82564f733e5ec875cd740ab	refs/heads/wip/s1-endpart
② heads 39
③ vs96bd6fe: 0
③ vs981f143: app.py verify/selection_pipeline.py verify/stepg_pipeline.py
④
  origin/verify/W-G.9-375-k965
  origin/wip/s1-endpart
```

其後施工樹 `git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `96bd6fe5daa32bbbb82564f733e5ec875cd740ab`。

## ④　四塊之實得與四簿之改前改後

抽取式 ＝ `§五-1` 末（附錄標題列後之第一個圍欄開列之次列至閉列之前一列·`\n` 相接末附 `\n`·二進位寫出）：

| 塊 | bytes | `sha256` | 列 | 首列空 | 判 |
|---|---|---|---|---|---|
| `K19` | `26278` | `d491f264c370998c2376e9ee90f6f26c53f5ca4803d86c3b39f15b4348119b6f` | `220` | 是 | ＝ 期 |
| `G12` | `3245` | `6c6e017111fa3d3b849f7f34ca24300c9cb401001334948d66e872b83800f6dc` | `15` | 是 | ＝ 期 |
| `E19` | `7187` | `18b922e9cfe2be060acb677dd78b562b23cdef70580757def3ecdf6bc852b832` | `36` | 是 | ＝ 期 |
| `P29` | `4481` | `de81243a469537682a1e3d4ebf1cad55eaaf66bcee961c1ee08d307dc11bbe8a` | `27` | 是 | ＝ 期（payload 內 `⬜` 子字串 `11`·列 `9` ＝ 塊之自載） |
| `CK`（`W-G.9-365` 附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | — | ＝ 期 |
| `GF`（`W-G.9-365` 附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | — | ＝ 期 |

| 簿 | 改前 bytes／blob | 改後 bytes／blob | `numstat` |
|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `658568`／`64f708d141a75835b75f6f8aacb05c05f5f7436f` | `684846`／`5fab239a68b58ef042d38d7a731eb8b5eade5f03` | `220`／`0` |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1050787`／`3461cdd803b48b85ec5c84a8f2e15f57f1ac2b78` | `1054032`／`7d56b5328c2c3968b9425992544848d92f70a503` | `15`／`0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1158003`／`7e63046b580d2c1057fcdf9cf93528dd1e779be0` | `1165190`／`5cf217beea6566f9d411eb7a408df9bcf7bc477d` | `36`／`0` |
| `CLAUDE.md` | `372553`／`fec6405ec301054ce9d9707e6794222efddd50d8` | `377034`／`bb2a928103a571ec4ebf24b28b329c6c8fa944b4` | `27`／`0` |

改前四簿皆以換行結尾、`CR` `0`；改後之 blob 皆 ＝ `§五-1` 項 `6`。

## ⑤　工項一之 `checkidx`、`gen_fa_index`

- `python C:\Users\admin\wg9376_O\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md`（塊 `P29` 附後）⇒ `rc 0`·stderr `0` B·末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python C:\Users\admin\wg9376_O\gen_fa_index.py <repo> C:\Users\admin\wg9376_O\FX_regen.md` ⇒ `rc 0`·stderr `0` B·出艙 `則 124；加註節 14；列 158`；`cmp` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同。

（`<repo>` ＝ 施工樹之反斜線絕對路徑。）

## ⑥　`§二` 之放行（KL 之逐字）

KL（`2026-10-11 01:34`）：

> 1. 是，接續擬 `W-G.9-376`
> 2. 畫面核對無誤(時間：01:30)，上傳相關報表

其「是」所答之問 ＝ 發單側窗七十九之請示文之【要你判斷】「畫面核對無誤後，主線是否快轉至 `96bd6fe` 並同步你的主 checkout？（是／否）」；所載之生產碼 `commit` ＝ `9fc8e5b4a389a8f121150be7a219b790eb3f349d`（唯此一筆）、土地後果 ＝ 本案無 ⇒ 為工項零′ 與工項三之放行（單 `§二`）。

## ⑦　pre-flight（`python verify/probes/probe_order_preflight.py <本單>`·`rc 0`·stderr `0` B）

🔴 機械 `0` 項；🟡 提示 `4` 項；ℹ️ 記錄 `2` 項——與單 `§五-1` 項 `8` 逐項同：

| 項 | 處置 |
|---|---|
| `P-2` `:333` | 採單之**具名豁免**（塊 `K19` 之三所錄之請示文之首段·逐字之引；其計數之框載於該文之後列） |
| `P-4` `:82` | 採單之**具名豁免**（`§一` 表頭·箭頭之座標系 ＝ 主線至側支之端·表內自載） |
| `P-4` `:194` | 採單之**具名豁免**（`§四` 表頭·箭頭之座標系 ＝ 改前至改後·表內自載） |
| `P-6` `:547` | 採單之**具名豁免**（塊 `P29` 之「前節之更新」·其數為序號之對應） |
| `P-5` `:554` | ℹ️ `SELF_SHA256` 相符（受詞 `81861` B） |
| `P-3` | ℹ️ `app.py` `def main` 區間（AST）＝ `22630`–`30350`·本單⛔ 用 |

**取號現查**（`§零-1`·皆 ＝ 單表）：`python verify/probes/wg9268_gate6_occupancy.py 96bd6fe W-G.9-376 W-G.9-375 W-G.9-397` ⇒ `rc 0`·母體 `docs/` `1002` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）；`W-G.9-376` 嚴格／寬式六數全 `0`·鬆框 `0`／`0`；`W-G.9-375` 嚴格 `7`／`9`／`7`、寬式 `7`／`9`／`9`、列框 `16`（寬 `18`）、檔框 `8`、鬆框 `9`／`152`；`W-G.9-397` 嚴格全 `0`、寬式 `D3` `2`、鬆框 `18`／`28`；`W-G.9-963` 嚴格全 `0`、寬式 `D3` `6`、鬆框 `46`／`51`。意指占用（`96bd6fe` 追蹤檔 `2827`·列框·`git grep -c`）：`自誤 600` 裸 `201`／平 `0`／B `1`（`docs/orders/W-G.9-375_補令一.md:208` 之預留）／C `0`；`601` `2052`／`0`／`0`／`0`；`602` `87`／`0`／`0`／`0`；`603` `124`／`0`／`0`／`0`；對照 `599` `939`／`15`／`1`／`14`；`GB-204` 錨定 `2` 檔／`2` 列（裸 `-F` 同）；對照 `GB-202` `10`／`43`；塊名 `E19`／`G12`／`P29` 二框皆 `0`／`0`；`K19` 塊框 `0`／`0`、名框 `5`／`9`；對照 `K18` `4`／`21`、`10`／`36`；`W-G.9-376R`、`heads_before_376`、`答KL_合併後反而配不到` 皆 `0` 檔。

## ⑧　CC 讀塊時認為與倉之事實不符之處

**無**。抽查之可機驗者皆合：塊 `G12` 之 `app.py`（`96bd6fe`）行錨——`:14847` 為 `_pa = {…分攤登記面積_m2… − 段三部分併出…}`、`:15398` 為 `_pre953 = …`、`:15844` 為 `_pre951 = …`、`:16302` 為 `_pre_a4 = …`、`:9652` 為 `def _pre965(t):`（其內減 `入池閘部分併出`／`入池閘成員部分併出`）、`:12027` 為 `_acct375 = {}`（其次列 `for _u in build_final or []:`）；所引 `CLAUDE.md:725` 為「裸框與錨定框得數相異者，須二數並報」之列；塊 `P29` 之 `⬜` 自載 `11`／`9` ＝ 實算。

## ⑨　CC 之自捕與自解

**本批之自解清單**（`CLAUDE.md` 自解款五項：零土地後果·零生產碼·可機驗·可逆·入本清單）：

1. **`commit` 訊息之尾**：單令「`commit` 訊息逐字 ……」；三筆之首段皆逐字依單，另於空一列後附 `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` 之 trailer——依倉內前例（`W-G.9-374` 工項零〜二之 `commit` `b7f99a1`／`52d2513`／`981f143` 皆同形）。可機驗：`git log -1 --format=%s <c>` ＝ 單之逐字；零土地後果、零生產碼；判別對照：`git log --format=%B 981f143` 含同形 trailer。
2. **`<O>` 之定**：`C:\Users\admin\wg9376_O`（`git -C` 該處非工作樹）；`heads_before.txt` 依 `§零-0` 項 `2` 之名存之（`§零-1` 之 `heads_before_376` 為撞名之受詞·⛔ 為所令之檔名）。

**自捕**：無。

## ⑩　各段耗時（本機時鐘·`2026-10-11`）

| 段 | 時 |
|---|---|
| 開場（`§零-0`〜`§零-3`） | 約 `01:53`–`01:56`（`heads_before.txt` `01:54:18`；pre-flight `01:55:45`；前置 `01:55:59`） |
| 工項零′（快轉與快轉後之出艙） | `01:56:19` 前後 |
| 工項零 | `commit` `01:56:50` |
| 工項一 | 抽塊 `01:57:25`；施 `01:57:41`；`checkidx`／`gen_fa_index` `01:57:47`；`commit` `01:57:55` |
| 工項二 | 本檔撰於其後 |
