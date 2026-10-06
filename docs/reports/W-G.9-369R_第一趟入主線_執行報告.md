# `W-G.9-369R`　第一趟入主線　執行報告 ⛔ 零生產碼（本批唯快轉納入已放行之生產碼 `70db4f0`）

> 受單 ＝ CC（工作樹 `.claude/worktrees/land-readjustment-trial-c317bf`·開場時 `d7a5ea4` 乾淨·依 `§零-0` 項 `2` detached 於側支之端，快轉後 detached 於主線）·`2026-10-07`。
> 單 ＝ `docs/orders/W-G.9-369_中量單.md`（`51729` B·`sha256` `7e3e14ae9c35b32c03930696d35508d4bbe4a3f65399f77a6cc58cbc86d4381f`·`348` 個 `\n`·CR `0`·`SELF_SHA256` 自驗相符）。來源 ＝ 第二處（KL 主 checkout 之根·未追蹤）；第一處（CC 施工樹之根）無此檔。KL 之訊唯以路徑引本單、⛔ 載 bytes／`sha256` ⇒ 依 `§零-0` 項 `4` 照實具名而以 `SELF_SHA256` 為據。
> 級 ＝ 中（⛔ 跑 `run_verification.py`／`run_all`）。
> 本檔載開場、工項零′〜二；收工閘 `1`〜`9` 之實測值與工項三之出艙，依單 `§三` 工項二於對話補報（⛔ 寫入本檔·自指）。
> 殼：Git Bash（Windows 11）·`python` ＝ Python `3.13.11`·`numpy` `2.4.4`（`< 2.5`·`GB-198` ⛔ 觸）·`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；`core.autocrlf`：system `true`／local `false`。

## ① 逐 `commit`

| 工項 | `commit` | 異動 | 生產碼四檔（`app.py`、`verify/stepg_pipeline.py`、`verify/run_all.py`、`verify/run_verification.py`）之 `git diff --name-only` |
|---|---|---|---|
| 零′ | **無 `commit`**；遠端 `refs/heads/wip/s1-endpart`：前 `d7a5ea4a36477d3867de181a9ca59ad714eeaeda` → 後 `e7855ecf75ca4ed692baa982f5f25ec672847e79`（`git push origin e7855ecf75ca4ed692baa982f5f25ec672847e79:refs/heads/wip/s1-endpart` ⇒ `d7a5ea4..e7855ec`·`rc 0`·⛔ `--force`） | 快轉 `8` 筆（其中生產碼 `1` 筆 ＝ `70db4f068ca3888ffa4b4fce565e4effaa037f31`） | （快轉·見 ③） |
| 零 | `cec55bf197f63cf2c7ff3771881c69a08595e1b0` | `A docs/orders/W-G.9-369_中量單.md`（blob `a80c161cc7d442fb94edf067ada904fbd4aa6c30` ＝ 來源之 `git hash-object --no-filters`；`git cat-file blob` 與來源 `cmp` 無差） | 空 |
| 一 | `5f530be13a2000a9f7d7761fc625e38d8a49423a` | `M` 四簿（numstat `CLAUDE.md` `31`／`0`；`GB` 簿 `21`／`0`；自誤簿 `36`／`0`；`K-6` 典 `11`／`0`） | 空 |
| 二 | 本檔之 `commit`（自指·其 hash 於對話補報） | `A docs/reports/W-G.9-369R_第一趟入主線_執行報告.md` | 空（於對話補報其出艙） |

`commit` 訊息：首段一律逐字依單；其後另附 `Co-Authored-By` 尾列一列（同倉內 `W-G.9-366` 諸 `commit` 之例·見 ⑨ 自捕 `3`）。三筆皆 `git commit -F`。

## ② 停機款之三值

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `d7a5ea4`；側支 `e7855ec`；施工樹追蹤檔無變動；heads `36`；`§零-0` 項 `3` `rc 0` 且四簿 ＝ 期；旗標 `[None×5]` | `git rev-parse origin/wip/s1-endpart` ＝ `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`；`origin/verify/W-G.9-367-adj4` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`；`git ls-remote --heads origin` ＝ `36` 列（`verify/` `31`·`wip/` `3`·`claude/` `1`·`main` `1`）；detach 後 `git status --porcelain --untracked-files=no` ＝ 空（全 `status --porcelain` 亦空）；`probe_WG9321_issuer_anchor.py … 579 577` `rc 0`·stderr `0` B·項4′：自誤 `564`／`579`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `194`／`201`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `60`／`63`／`[44, 47]`；旗標 `[None, None, None, None, None]` ⇒ ⛔ 成就 |
| `2` | `SELF_SHA256` 相符；來源存；入倉 blob ＝ 來源 | 實算 ＝ 單載 ＝ `2700e88408593e60efa443a5b6e01fc68b7febecaca5cfe1539100ae85118bb0`（受詞 `51651` B）；KL 之訊⛔ 載 bytes ⇒ ⛔ 比；入倉 blob 與來源逐位同 ⇒ ⛔ 成就 |
| `3` | 前置 `1`〜`3` 皆符 | 見 ③ ⇒ ⛔ 成就 |
| `4` | `push` 成而⛔ `--force` | `d7a5ea4..e7855ec`·`rc 0` ⇒ ⛔ 成就 |
| `5` | 快轉後 ①〜④ ＝ 期 | 見 ③ ⇒ ⛔ 成就 |
| `6` | 四塊與 `§五-1` 同；施後 blob ＝ `§五-1` 項 `6` | 見 ④ ⇒ ⛔ 成就 |
| `7` | 刪除欄 `0`；嚴格前綴；尾 ＝ 塊 | 見 ④ ⇒ ⛔ 成就 |
| `8` | `checkidx` `rc 0`·末列 ＝ 期；`gen_fa_index` ＝ 期且逐位同 | 見 ⑤ ⇒ ⛔ 成就 |
| `9` | 收工閘皆符 | 於對話補報（自指） |
| `10` | 工項三之各期 | 於對話補報（工項三於收工閘之後） |
| `11` | 工項零〜二之 `push` 皆至 `wip/s1-endpart`；⛔ 推側支 | 工項零′、零、一之 `push` 目標皆 `wip/s1-endpart`；側支⛔ 推（工項二之 `push` 於對話補報） |
| `12` | ⛔ 作「孰為正典」之判；⛔ 改塊、器、命令 | ⛔ 作；塊、器、命令一字未改（`<repo>` 以反斜線之絕對路徑傳入）；塊與倉之事實之不符：見 ⑧（無） |
| `13` | 新檔⛔ 為 `git check-ignore` 所命中 | 本單：`git check-ignore -v` `rc 1`（無命中）；本檔：見 ⑦ 之末 |

## ③ 工項零′ 之前置與快轉後之出艙（`<O>\ff_pre.txt`、`<O>\ff_post.txt` 原樣）

前置（`commit` 前·與快轉分開之呼叫）：

```
## 前置1
is-ancestor rc=0
count d7a5ea4..e7855ec = 8
count e7855ec..d7a5ea4 = 0
merges: []
## 前置2
app.py
verify/selection_pipeline.py
[lines=2]
control without :(glob) lines=8
app.py@e7855ec = af2b8f397c71a0adee156c4fdb90696ef7dadf43
selection_pipeline@e7855ec = 9e189d50a9c685589bef8df0389f0af597f2cc43
## 前置3
e7855ecf75ca4ed692baa982f5f25ec672847e79 hits=0 []  W-G.9-368 工項二：執行報告入倉（側支）⛔ 零生產碼
37555ef781c03d9e70f05d2cca1586c4223331fb hits=0 []  W-G.9-368 工項一：K-9-57〜K-9-63 之立（同街廓同地主分不到之宗·停機條款丁類 34 項之定案）入 K-6 典（純末端追加·側支）⛔ 零生產碼
1c53963ef0e4c317f945f92b289a83550c100832 hits=0 []  W-G.9-368 工項零：本單原封入倉（側支）⛔ 零生產碼
7c4ecc26a60eebea287f318c89a4c5e4254ca19a hits=0 []  W-G.9-367 工項四：執行報告入倉（新側支）⛔ 零生產碼
7f1cde4ad8d6bd94eddc557388733b260ac1e39c hits=0 []  W-G.9-367 工項三：K-9-56 之立 ＋ GB-199／GB-201 之進度 ＋ 自誤 578／579 ＋ 常設規則索引之一列 ＋ 待落地清單之更新（新側支）⛔ 零生產碼
70db4f068ca3888ffa4b4fce565e4effaa037f31 hits=2 [app.py verify/selection_pipeline.py]  W-G.9-367 工項二：規格步 4 乙之第一趟（K-9-53 ②·K-9-56）＋ 手冊先行之 GB-201 之防護 🔴 生產碼（新側支）
b8639c08814f4101c81a3045b64e0b7d3603d386 hits=0 []  W-G.9-367 工項一：量測器 F24（規格步 4 乙·第一趟）入倉 ＋ F4／F9／F10／F14／F23 之錨之更新（新側支）⛔ 零生產碼
85a0d61462150c1b54a3471a55aa7d3113e0cdc1 hits=0 []  W-G.9-367 工項零：本單原封入倉（新側支）⛔ 零生產碼
```

（逐筆判之形 ＝ `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`；`hits=0 []` 即空輸出。命中者恰 `1` 筆 ＝ `§二` 逐筆放行清單之 `70db4f068ca3888ffa4b4fce565e4effaa037f31`，其訊息首段與清單逐字同。）

快轉之前另單獨量遠端：`wip/s1-endpart` ＝ `d7a5ea4…`、`verify/W-G.9-367-adj4` ＝ `e7855ec…`、heads `36`、`git branch -r --contains 70db4f0…` ＝ 唯 `origin/verify/W-G.9-367-adj4`。

快轉後（`git fetch origin` 之後）：

```
① e7855ecf75ca4ed692baa982f5f25ec672847e79	refs/heads/wip/s1-endpart
② heads=36
   prod files=34
③ vs e7855ec diff=0
③ control vs d7a5ea4 diff=2 [app.py verify/selection_pipeline.py ]
④
  origin/verify/W-G.9-367-adj4
  origin/wip/s1-endpart
```

（③ 之生產碼 `34` 檔 ＝ `app.py` ＋ `git ls-tree --name-only origin/wip/s1-endpart verify/` 之頂層 `*.py` `33`。）其後 `git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `e7855ecf75ca4ed692baa982f5f25ec672847e79`。

## ④ 四塊之實得與四簿之改前改後

抽取式 ＝ `§五-1` 末（附錄標題列之後之第一個圍欄開列〔四反引號 ＋ `markdown`〕之次列至閉列〔恰四反引號〕之前一列·`\n` 相接末附 `\n`·UTF-8·二進位寫出）；`<O>\extract.py`。

| 塊 | 圍欄（開／閉之列·`1` 起） | bytes | `sha256` | `\n` 數 | 首列空 | 期（`§五-1`） |
|---|---|---|---|---|---|---|
| `K12` | `231`／`243` | `2812` | `44fc8b40530941aa445511680509d243d959d00b23a1a98be5bd63ccfe0fccca` | `11` | 是 | 同 |
| `G10` | `247`／`269` | `3578` | `0ef04ef5227149815a23da1ea4c57642d884d838a77b92e99bc7fcc65492dc1a` | `21` | 是 | 同 |
| `E12` | `273`／`310` | `5895` | `0b00e3f586c7e994c27b2c672a1b69c3e2b7ad4e266f65541b294021b9b5b60e` | `36` | 是 | 同 |
| `P22` | `314`／`346` | `5474` | `076516d5b3413a2a7ac7cb58dbe449b108f6600e1c81529c40b5f40201414fa1` | `31` | 是 | 同 |
| `CK`（`W-G.9-365_輕量單.md` 附錄午） | `807`／`839` | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | 否 | 同 |
| `GF`（同單附錄巳） | `755`／`803` | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | 否 | 同 |

四塊之 CR 皆 `0`。塊 `P22` 之 `⬜`：子字串框 `15`·列框 `13`（＝ 塊之自載）。

四簿（改前 ＝ `e7855ec` 之 blob；改後 ＝ 工項一 `5f530be` 之 blob；`<O>\append.py` 以 `ab` 附之並驗）：

| 簿 | 改前 bytes／blob | 改後 bytes／blob | 嚴格前綴 | 尾 ＝ 塊 | numstat |
|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `546901`／`6b85ddf8a53c476f9f2e20b8370daeb54f91baab` | `549713`／`bc3ebbb1dcfe3a5c652a4d6796baf0567dbd33c5` | 真 | 真 | `11`／`0` |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1044434`／`469b445059b37d0014badf86797421f86876e431` | `1048012`／`24ac5bf6d0c2f1bc34656e7abb4580f110a712b2` | 真 | 真 | `21`／`0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1121735`／`aca7f565fa03722254278215fa360285dbc11f88` | `1127630`／`5b5f049122e832cd97503bd16d4839122b4e2f33` | 真 | 真 | `36`／`0` |
| `CLAUDE.md` | `342956`／`f3557822bcfe0c4bb40485261290f31744c7c745` | `348430`／`58e78852447032f1f17d1ae151b8517fb28661b6` | 真 | 真 | `31`／`0` |

改前四簿皆以 `\n` 結尾、CR `0`（判別力：`git cat-file blob e7855ec:data/V6.dxf` 之 CR ＝ `12308`）。施後之 blob 於快轉之前先以「改前 blob ＋ 塊」預算一次（與上表同），附後再算一次、`commit` 後以 `git rev-parse HEAD:<path>` 三算——皆 ＝ `§五-1` 項 `6`。

## ⑤ 工項一之 `checkidx`、`gen_fa_index`

- `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md`（塊 `P22` 附後）⇒ `rc 0`·stderr `0` B·末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。（索引本批⛔ 動：blob `a18e96d6b4d7640c84260469bb09f67b7bc41aab`·`25091` B。）
- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`·stderr `0` B·出艙 `則 124；加註節 14；列 158`；`cmp <O>\FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md` 無差（二者 `sha256` 皆 `df14158df94ff8d94ee12cfd802c5d7fc1f4b213fd53ee891087a8490b666b1c`）。

## ⑥ `§二` 之放行（KL 之逐字·依單 `§二` 錄）

KL 之畫面核對（`2026-10-06 22:30`·逐字）：

> 核對畫面無誤，上傳相關報表

發單側窗七十呈 KL 之「三、入主線之內容」與【要你判斷】（`2026-10-06 22:33`·逐字）：

> - **主線**：`d7a5ea4` → `e7855ec`，快轉，共 8 筆 commit。
> - **生產碼**：只有 `70db4f0` 一筆，改 `app.py` 與 `verify/selection_pipeline.py`，即 W-G.9-367 之第一趟。
> - **零生產碼**：其餘 7 筆，含 K-9-56 至 K-9-63 之正典。
> - **對土地之影響**（二退縮同）：
>   - 歸戶 G001 之道路片 628-3(1)（13.15 ㎡，兩側皆無已配地）併入其於 R3 之 628-34(2)，應分配面積由 250.24 增為 257.91 ㎡；
>   - R3 抵費地由 1659.06（0 m 為 1659.05）減為 1651.41 ㎡；
>   - 合併單位由 18 減為 17；
>   - 其他街廓不變。
>
> 【要你判斷】主線是否快轉至側支之端 `e7855ec`，並改依上表先出 W-G.9-369、再出 W-G.9-370？（是／否）
>
> 您答「是」後，此答將逐字載入 W-G.9-369，作為入主線之放行依據。

KL 之答（`2026-10-06 22:34`·逐字）：

> 是

⇒ 工項零′（主線快轉）與工項三（主 checkout 之同步）之放行（`常規一`）。逐筆放行清單（`恆常附款 y`）之唯一生產碼 `commit` ＝ `70db4f068ca3888ffa4b4fce565e4effaa037f31`，與 ③ 前置 `3` 之逐筆判之命中者同。

## ⑦ pre-flight（`python verify/probes/probe_order_preflight.py <來源檔之絕對路徑>`·態 `e7855ec`）

`rc 0`·stderr `0` B；出艙（原樣）：

```
【order pre-flight】W-G.9-369_中量單.md（51729 B／348 列）
── 🔴 機械·停機款：0 項 ──
── 🟡 提示·須逐項處置：5 項 ──
  [P-2] :96   🟡 出艙計數而同段⛔ 未載其框：> - **主線**：`d7a5ea4` → `e7855ec`，快轉，共 8 筆 commit。
  [P-4] :72   🟡 方向性轉引而同段⛔ 未具名座標系：| # | 項 | 值 |
  [P-4] :96   🟡 方向性轉引而同段⛔ 未具名座標系：> - **主線**：`d7a5ea4` → `e7855ec`，快轉，共 8 筆 commit。
  [P-4] :187  🟡 方向性轉引而同段⛔ 未具名座標系：| 閘 | 受詞 | 期 |
  [P-4] :279  🟡 方向性轉引而同段⛔ 未具名座標系：### 🩸 `自誤 580`　**交接文六十九→七十（倉外·⛔ 入倉）`§二-2` 之標題逐字「弱弱聯合三問（KL 2026-10-05 14:49）」——KL 答三問之時刻實為 
── ℹ️ 記錄：2 項 ──
  [P-5] :348  SELF_SHA256 ✅ 相符（取檔內**最末**一個·受詞 51651 B）｜實算 2700e88408593e60…／單載 2700e88408593e60…
  [P-3] :-    `app.py` 之 `def main` 區間（AST 實查）＝ `21782`-`29502`
```

（上錄略去器之框線與末之 `rc` 說明列。）與 `§五-1` 項 `8` 逐項同。處置：`P-2` `:96`、`P-4` `:96` ⇒ 依單之**具名豁免**（`§二` 所引呈 KL 之文之逐字·其「8 筆」之框 ＝ ③ 前置 `1` 之 `git rev-list --count d7a5ea4..e7855ec` ＝ `8`·座標系 ＝ 主線至側支之端）；`P-4` `:72` ⇒ 具名豁免（`§一` 表內自載）；`P-4` `:187` ⇒ 具名豁免（`§四` 閘 `4` 改前至改後）；`P-4` `:279` ⇒ 具名豁免（交接文之名·⛔ 方向之轉引）；`P-5` 相符；`P-3` 本單⛔ 用。

`§零-1` 取號現查（`python verify/probes/wg9268_gate6_occupancy.py e7855ec W-G.9-369 W-G.9-368 W-G.9-396`·`rc 0`·stderr `0` B）：母體 `973` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）；`W-G.9-369` 嚴格／寬式六數 `[0, 0, 0, 0, 0, 0]`·鬆框 `0`／`0`；`W-G.9-368` `2`／`4`／`6`·列框 `10`·檔框 `3`·鬆框 `3`／`24`；`W-G.9-396` 嚴格 `0`／`0`／`0`、寬式 `D3` `2`·鬆框 `24`／`40`；`⟨NEG⟩`（`W-G.9-963`）六數 `[0, 0, 0, 0, 0, 4]`·鬆框列 `39`——與 `§零-1` 之表逐格同。次單之號 `W-G.9-370`：同器六數 `[0, 0, 0, 0, 0, 0]`、鬆框 `0`／`0`（⛔ 鑄）。意指占用（`e7855ec` 之追蹤檔 `2793` 檔·`git grep -c` 列框）：

| 號 | 裸（錨定 `-P "(?<![0-9\-])<號>(?![0-9])"`） | 平形 `-F "自誤 <號>"` | B 形 `` -F "自誤 `<號>`" `` | C 形 `` -F "`自誤 <號>`" `` |
|---|---|---|---|---|
| `580` | `51` | `0` | `0` | `0` |
| `581` | `24` | `0` | `0` | `0` |
| `582` | `40` | `0` | `0` | `0` |
| `583` | `55` | `0` | `0` | `0` |
| 對照 `579` | `174` | `11` | `0` | `11` |

本檔（新檔）之 `git check-ignore -v` 於 `git add` 之前實跑，其結果於對話補報（本檔寫成在先、量在後·自指）。

## ⑧ 讀塊時認為與倉之事實不符之處

無。附塊之前逐項讀核其所引之倉內之文（態 `e7855ec`）：`K-6` 典之「`K-9-56` 之立；規格步 `4` 乙（第一趟）之工程讀法；入側支」節（其落地狀態列逐字含「🔶 側支 `verify/W-G.9-367-adj4`（工項二）；主線之推進候 KL 逐字放行」；裁之內容 ①〜④；工程讀法甲〜卯）、「`K-9-53` ① 之入主線；KL 之畫面核對」節、「`K-9-57`〜`K-9-63` 之立」節（`K-9-57` 之落地狀態含「⑥ 之第一趟於側支 `verify/W-G.9-367-adj4`」·② ⑥ ⑦ ✅）；`GB` 簿之 `GB-201` 與 `GB-199` 立項節之失效條件（塊 `G10` 所引者與倉逐字同·`-F` 全句命中各 `1`）、`GB-199` 立項節之「與配地之關係」所列之讀者（瀑布 `verify/wf_f3.py` 之 `_cascade`／`_poly_of`、畫面之舊「自動計算公設分配」、「另一讀者」入池閘之再入）、「`GB-199`／`GB-201` 之進度（`W-G.9-367`）」節（其 `GB-199` 之態列逐字含「其入主線時解除」）；`CLAUDE.md` 之末節「待落地清單之更新：規格步 `4` 乙（第一趟·…）入側支；…」之序 `1`〜`6`（與塊 `P22` 之「前節之更新」之對應同）。以上 CC 唯讀核、⛔ 判孰為正典。

## ⑨ 自捕與自解

**本批之自解清單**：無（本批未遇須自解之疑義）。

**照實記**（皆⛔ 動任一宗地、⛔ 動生產碼）：
1. KL 之訊唯以路徑引本單（未載 bytes／`sha256`）⇒ 依 `§零-0` 項 `4` 之文以 `SELF_SHA256` 為據（⛔ 停機·單已明定）。
2. 本機 `numpy` ＝ `2.4.4`（單之態錨 ＝ 發單側 Linux 之 `2.4.6`）；二者皆 `< 2.5` ⇒ `GB-198` 之情形⛔ 觸。
3. `commit` 訊息：首段逐字依單，另附 `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` 尾列（倉內 `W-G.9-366` 之三筆 `commit` 皆同此形）；首段之外⛔ 增他字。
4. 施後之 blob 於快轉之前先預算（「改前 blob ＋ 塊」），以免快轉後始見塊不合而主線已動；預算與實得同。
5. 前置 `2` 另跑無 `:(glob)` 之對照形 ⇒ `8` 列（＝ 單之所述），證 `:(glob)` 形之 `2` 列非框過窄。

## ⑩ 各段耗時（本機時鐘·`2026-10-07`·`+0800`）

| 段 | 起 | 迄 |
|---|---|---|
| 開場（`git fetch`、態錨、取號器、`SELF_SHA256`、取號現查、pre-flight） | `07:51` | `07:53:31` |
| 塊之抽取與對拍、工項零′ 前置、施後 blob 之預算 | `07:53:46` | `07:54:13` |
| 工項零′（快轉之 `push` 與 ①〜④） | `07:54:20` | `07:55:02` |
| 工項零（入倉·`commit` `07:55:22`·`push`） | `07:55:02` | `07:55:40` |
| 工項一（讀核、附塊、`checkidx`、`gen_fa_index`、`commit` `07:56:32`、`push`） | `07:55:40` | `07:56:45` |
| 工項二（本檔） | `07:57` | 於對話補報 |

## ⑪ `<O>`

`C:\Users\admin\AppData\Local\Temp\wg9369_O`（任何 git 工作樹之外；`git -C <O> rev-parse --show-toplevel` ⇒ `fatal: not a git repository`·`rc 128`）。內含 `heads_before.txt`（`36` 列·`sha256` `2316506d3b0dbc18d476e22dbf8bac4afc5b315b1fb67003f1025ed3770e1f66`）、`anchor_open*.txt`、`occ.txt`、`preflight.txt`、`ff_pre.txt`、`ff_post.txt`、四塊（`K12.md`、`G10.md`、`E12.md`、`P22.md`）、`checkidx.py`、`gen_fa_index.py`、`FX_regen.md`、`checkidx_out.txt`、`gen_out.txt` 與 CC 自寫之小器（`selfsha.py`、`extract.py`、`predict_blob.py`、`append.py`·皆⛔ 入倉）。
