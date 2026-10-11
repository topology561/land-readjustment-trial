# `W-G.9-377R`　接線與突變之判別力之補寫　執行報告

> **單** ＝ `docs/orders/W-G.9-377_中量單.md`（`76232` B·`sha256` `206dbf34ab1534ae8eae67225ec5f995c57c7e2ce5c1c841d3d18cba9cbc6322`·`SELF_SHA256` 自驗相符）。**受單** ＝ CC 新窗·`2026-10-11`·施工樹 ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\w-g-9-377-processing-9d2950`（detached）。
> **`<O>`**（倉外輸出目錄）＝ `C:\Users\admin\AppData\Local\Temp\claude\C--Users-admin-Desktop-land-readjustment-trial--claude-worktrees-w-g-9-377-processing-9d2950\61284ca3-4b09-49eb-bc09-72235027f0bf\scratchpad\O377`（`git rev-parse --is-inside-work-tree` ⇒ `fatal: not a git repository`）。
> **環境** ＝ Windows 11·Git Bash·Python `3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`（發單側 ＝ Linux·`3.13.16`／`2.4.6`／`2.2.0`；本批之量測值與單載之期逐字同）；量測之殼之旗標 `[None, None, None, None, None]`；`core.autocrlf` ＝ system `true`／local `false`。
> 本檔⛔ 載收工閘之實測值與工項四之出艙（自指·單 `§三` 工項三），二者於對話出艙。

## ①　逐 `commit`

| 工項 | `commit` | 首列（逐字·其後空一列附 `Co-Authored-By` 尾列·`自誤 604` 之書法） |
|---|---|---|
| 零 | `2aa9c030ca1a76063b48cae5f53e82c5290662f2` | `W-G.9-377 工項零：本單原封入倉 ⛔ 零生產碼` |
| 一 | `2167167098a46b47242de9f414a7e4075a4e6eea` | `W-G.9-377 工項一：F27 之 mutate（N01〜N57）／wiring Y7／selftest T5 ＋ F28 之 L4〜L6 ＋ F29 之 K50 ⛔ 零生產碼` |
| 二 | `cce606769fd11161e7cb1102b1a42bdd95309fc7` | `W-G.9-377 工項二：自誤 604 ＋ 待落地清單之更新（接線與突變之補寫·補令二之⛔ 量之二項·F29 之增例）⛔ 零生產碼` |
| 三 | 本檔之 `commit`（自指·於對話出艙） | `W-G.9-377 工項三：執行報告入倉 ⛔ 零生產碼` |

各 `commit` 之生產碼判（`git diff --name-only HEAD~1 HEAD`·逐 commit 出艙）：零 ＝ `docs/orders/W-G.9-377_中量單.md`；一 ＝ `verify/probes/probe_WG9373_k966.py`、`verify/probes/probe_WG9373p1_partrem.py`、`verify/probes/probe_WG9375_k965.py`；二 ＝ `CLAUDE.md`、`docs/reports/W-G.9波_claude.ai側自誤登記.md`——四生產碼檔（`app.py`、`verify/stepg_pipeline.py`、`verify/run_all.py`、`verify/run_verification.py`）命中 `0`。`push` 皆 `HEAD:wip/s1-endpart`·快轉·首推即成·⛔ `--force`·⛔ 推側支。

## ②　停機款 `1`〜`12`

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `a3925f1`；四側支 ＝ 單首；追蹤檔無變動；heads `39`；開場之器 `rc 0` 且四簿 ＝ 期；旗標 `[None×5]` | 主線 `a3925f1037f96277c690940303f0332df782e3d7`；`96bd6fe5…`／`cf08e23f…`／`fe1fe3bf…`／`e7855ecf…` ＝ 單首；`git status --porcelain --untracked-files=no` 空（`0` B）；heads `39`（存 `<O>\heads_before.txt`）；`probe_WG9321_issuer_anchor.py … 603 599` `rc 0`·自誤 `588`／`603`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`·`GB` `196`／`204`／`[12, 87, 179, 181, 183, 184, 185, 203]`·`VR` `80`／`95`／`[73, 75]`·`K-9` `67`／`70`／`[44, 47]`·stderr `0` B；旗標 `[None, None, None, None, None]` ⇒ ⛔ 成就 |
| `2` | `SELF_SHA256` 相符；KL 之訊之 bytes ＝ 本單；來源檔可得；入倉 blob ＝ 來源 | KL 之訊載 `76232` bytes／`sha256` `206dbf34…6322`（全 `64` 碼）＝ 實測；`SELF_SHA256` 單載 ＝ 實算 `388516fa69a199c27e85c59fff3fccae0d6774c189adce36024e23bb76ff1374`；來源取自第二處（KL 主 checkout 之根·施工樹之根無之）；`git cat-file blob HEAD:docs/orders/W-G.9-377_中量單.md` 與來源 `cmp` 同 ⇒ ⛔ 成就 |
| `3` | 五塊 ＝ `§五-1`；`git apply --check` 過；施後 blob ＝ `§五-1` | 見 ③ ⇒ ⛔ 成就 |
| `4` | 三器、二簿之刪除欄 `0`；二簿嚴格前綴、尾 ＝ 塊 | 見 ③ ⇒ ⛔ 成就 |
| `5` | 工項一項 `4` ＝ 期 | 見 ④ ⇒ ⛔ 成就 |
| `6` | `checkidx` `rc 0`·末列 ＝ 期；`gen_fa_index` ＝ 期·逐位同 | 見 ⑤ ⇒ ⛔ 成就 |
| `7` | `§四` 收工閘 ＝ 期 | 於對話出艙（自指） |
| `8` | 工項四之諸項 ＝ 期 | 於對話出艙（工項四於本檔之 `commit` 之後） |
| `9` | `push` 之目標 ＝ `wip/s1-endpart`·⛔ `--force`·⛔ 側支 | 工項零〜二之三推皆 `HEAD -> wip/s1-endpart` 之快轉（`a3925f1..2aa9c03`、`2aa9c03..2167167`、`2167167..cce6067`） ⇒ ⛔ 成就 |
| `10` | `mutate` 之子程序⛔ 逾時；基準 `N00` 全綠 | `✅ N00 —·基準（⛔ 突變）：錨 1 見；所指 []；紅 []`；逾時 `0` ⇒ ⛔ 成就 |
| `11` | 新檔⛔ 為 `git check-ignore -v --no-index` 所命中 | 本單：`rc 1`·無命中（工項零前實跑）；報告：於收工閘 `2` 量（對話） ⇒ 本單側⛔ 成就 |
| `12` | CC ⛔ 作正典之判、⛔ 改塊／器／命令 | ⛔ 改一字；塊之文字與倉之事實之不符 ＝ 無（見 ⑧） ⇒ ⛔ 成就 |

## ③　五塊、三器、二簿

**五塊之實得**（`§五-1` 末之抽取式·`<O>\Fv27.diff` 等·抽取器 ＝ CC 自寫之倉外腳本）：

| 塊 | 圍欄（單之列） | bytes | `sha256` | 列 | 對 `§五-1` |
|---|---|---|---|---|---|
| `Fv27` | `204`–`570` | `25827` | `2be2129177828b3129ad4ce89f82b2ed59e3dd42c309f0e07cb08c066d168950` | `365` | 同 |
| `Fv28` | `574`–`697` | `8617` | `27d95e356f48efa5fa7cf5c2e4eda86fd429773783bb6e098e4c782c71a94eed` | `122` | 同 |
| `Fv29` | `701`–`735` | `2875` | `401bf8ba5a316a141d95ff9860faaafb3e5c6cf8bf5b79ffa35104bd15a50396` | `33` | 同 |
| `E20` | `739`–`752` | `1897` | `29f69167063309b0333a07484167fa00a32400cf5579a1c2c7bcb7deb6141eb8` | `12` | 同 |
| `P30` | `756`–`781` | `3897` | `a60ed730899c4e81e5ae3f664dd87f64f83e5c93d3942f9388d58f39ac09f836` | `24` | 同 |

**三器**（`git apply --check` `rc 0`；`git apply` `rc 0`）：

| 器 | 施前 blob／B | 施後 blob／B | numstat |
|---|---|---|---|
| `verify/probes/probe_WG9373_k966.py`（`F27`） | `64559114764758645af0f3ce1fa24643b855fb82`／`44338` | `2e5c2203a6ac9eb185c12fc8aa1eeda6e5fe4770`／`67226` | `316`／`0` |
| `verify/probes/probe_WG9373p1_partrem.py`（`F28`） | `1daec0ce619789b626e57c317658afe7f4e59f8d`／`26213` | `cafa6ecb2b99a21c78db002b52df82b6a256244a`／`33337` | `97`／`0` |
| `verify/probes/probe_WG9375_k965.py`（`F29`） | `1ea99b72e891a2c4d642b5fcdf9248e0c15e3e66`／`68252` | `684fd5797e799b8b3932bc03d61a4a87717d8d84`／`69977` | `15`／`0` |

**二簿**（二進位附加·改前全檔為改後之嚴格前綴、改後之尾 ＝ 塊：皆 `True`；改前改後 `CR` 皆 `0`）：

| 簿 | 改前 B／blob | 改後 B／blob | numstat |
|---|---|---|---|
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1165190`／`5cf217beea6566f9d411eb7a408df9bcf7bc477d` | `1167087`／`4b8e995b6d1cd45f4f17da5479427e00d10d974c` | `12`／`0` |
| `CLAUDE.md` | `377034`／`bb2a928103a571ec4ebf24b28b329c6c8fa944b4` | `380931`／`ccb5269d17bf8527edb529bebb29efb87919c8ab` | `24`／`0` |

## ④　工項一項 `4` 之出艙（`<repo>` ＝ 施工樹之絕對路徑·出艙存 `<O>\c1_*.out`）

| 呼叫 | `rc` | 末列（逐字） | 其餘 |
|---|---|---|---|
| `probe_WG9373_k966.py selftest` | `0` | `⇒ 紅 []；rc 0` | `✅ P0 逐項擾動恰該項紅 28／28`；`✅ T5 手冊先行·第 1 輪之來源量 ＝ 計畫之量 ÷ κ（BB 之 κ ＝ 2）⇒ 比例 0.433333：A1 52／B1 43.33／C1 34.67；甲之剩下 34 全入 A2；帳以來源量計（Y 21.67／Z 17.33）` |
| `probe_WG9373_k966.py wiring` | `0` | `⇒ 紅 []；rc 0` | `Y1`〜`Y7` 皆 ✅（`Y7`：`{'k953_manual_run': [True], 'k6b_stage3_run': [True], 'adj4_pass1_run': [True]}`） |
| `probe_WG9373_k966.py mutate` | `0` | `⇒ 突變 57（另基準一）；紅 []；rc 0` | ✅ 列 `58`（`N00` ＋ `N01`〜`N57`）·🔴 `0`；耗時 `10:32:37`→`10:34:49` |
| `probe_WG9373p1_partrem.py selftest` | `0` | `⇒ 紅 []；rc 0` | `✅ P0 逐項擾動恰該項紅 26／26`；`L4`／`L5`／`L6` ✅ |
| `probe_WG9375_k965.py selftest` | `0` | `⇒ 紅 []；rc 0` | `✅ P0 判式自驗 50／50`；`✅ K50 回原狀之帳之序以該次合併時之應分配面積定` |

stderr 合計 `0` B（五檔皆 `0`）。`mutate` 後施工樹之 `git status --porcelain --ignored --untracked-files=all` 唯三器之 ` M`（倉內無遺留）。

## ⑤　工項二之 `checkidx`、`gen_fa_index`

- 塊 `CK`（`docs/orders/W-G.9-365_輕量單.md` 附錄午·圍欄 `807`–`839`）`1539` B·`00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF`（附錄巳·`755`–`803`）`2445` B·`b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（皆 ＝ `§五-1` 項 `7`）。
- `python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 0`·stderr `0` B·末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`·stderr `0` B·出艙 `則 124；加註節 14；列 158`；`cmp <O>\FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md` 同。

## ⑥　`§二` 之 KL 之逐字

> C:\Users\admin\Desktop\land-readjustment-trial>   git -C C:\Users\admin\Desktop\land-readjustment-trial log -1 --oneline
> a3925f1 (HEAD -> wip/s1-endpart, origin/wip/s1-endpart) W-G.9-376 工項二：執行報告入倉 ⛔ 零生產碼

（`2026-10-11 07:43`·轉引自單 `§二`。）本窗 KL 之訊（逐字）：「依根目錄 W-G.9-377_中量單.md 辦 W-G.9-377（76232 bytes／sha256 206dbf34ab1534ae8eae67225ec5f995c57c7e2ce5c1c841d3d18cba9cbc6322）。」

## ⑦　pre-flight

`python verify/probes/probe_order_preflight.py <本單>` ⇒ `rc 0`·stderr `0` B：🔴 機械 `0` 項／🟡 提示 `2` 項／ℹ️ 記錄 `2` 項（＝ `§五-1` 項 `8`）。

| 項 | 出艙 | 處置 |
|---|---|---|
| `P-4` `:158` | 方向性轉引而同段⛔ 未具名座標系（`§四` 之表頭） | 具名豁免（單 `§五-1` 項 `8`：閘 `4` 之箭頭 ＝ 改前至改後·表內自載） |
| `P-6` `:775` | 停機款所繫之數⛔ 未具名實測出處（塊 `P30` 之「前節之更新」） | 具名豁免（單 `§五-1` 項 `8`：其數皆序號之對應·⛔ 為實測數） |
| `P-5` `:783` | `SELF_SHA256` ✅ 相符（受詞 `76154` B） | — |
| `P-3` | `app.py` `def main` 區間 `22630`–`30350` | 本單⛔ 用 |

§零-1 取號之復算（`a3925f1`）：`wg9268_gate6_occupancy.py a3925f1 W-G.9-377 W-G.9-376 W-G.9-397` `rc 0`·母體 `1004` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）；`W-G.9-377` 嚴格／寬式皆全 `0`·鬆框 `0`／`0`；`W-G.9-376` `2`／`8`／`6`·列框 `14`·檔框 `4`·鬆框 `5`／`48`；`W-G.9-397` 嚴格 `0`·寬式 `D3` `2`·鬆框 `20`／`31`；`W-G.9-963` 嚴格 `0`·寬式 `D3` `6`·鬆框 `48`／`53`——皆 ＝ 單之表。意指占用（追蹤檔 `2829`·`git grep -c`）：`604` 裸 `32`／平 `0`／B `0`／C `0`；`603` `143`／`6`／`0`／`6`；塊名 `Fv27`／`Fv28`／`Fv29`／`E20`／`P30` 二框皆 `0`／`0`；`E19` `1`／`4`·`2`／`11`；`P29` `2`／`11`·`2`／`18`；`W-G.9-377R` `0`／`0`——皆 ＝ 單之表。

## ⑧　塊之文字與倉之事實之不符

無。另核塊 `E20` 所載之倉側數（於 `a3925f1`）：`W-G.9-` 起首之 `commit` `1107`、含 `Co-Authored-By:` 尾列 `1096`、最近 `150` 筆中「首列 ＋ 空列 ＋ 唯尾列」`146`、`docs/reports/` 提及該尾列 `18` 檔（`W-G.9-345R`〜`W-G.9-376R`）、`docs/orders/` 含「`commit` 訊息逐字」之令 `48` 檔——皆同。

## ⑨　CC 之自捕與自解

**自捕**
1. 塊之抽取之首趟，Bash 之輸出路徑寫為 `"$O\\${p##*:}.blk"`，`\$` 被讀為字面 `$` ⇒ 五呼叫皆 `OSError: [Errno 22]`（⛔ 寫出任何檔）；改為逐一具名之路徑重跑，皆 ＝ 期。塊 `CK`／`GF` 同一呼叫之輸出路徑無此形，首趟即 ＝ 期。
2. 唯讀 reviewer 自報：其以 `python -m py_compile` 驗三器，於 `verify/probes/__pycache__/` 生 `.pyc` 三檔（`.gitignore:18` 命中·未追蹤），已由其自刪並移除該目錄；CC 於 `commit` 前以 `git status --porcelain --ignored --untracked-files=all` 復核：唯三器之 ` M`。

**reviewer**（唯讀·驗後推前之常設步）總判「可推」：範圍、錨恰一見（`57`／`57`·另以 AST 自算）、`mutate` 只寫倉外之暫存（`tempfile.mkdtemp`·`finally` 中 `rmtree`·子程序 `PYTHONDONTWRITEBYTECODE=1`）、基準一之判式 ＝ 全綠、`T5`／`Y7`／`L4`〜`L6`／`K50` 之所量與說明文一致（手算復核），皆 ✅。其 ⚠️ 一項**呈發單側**（CC ⛔ 判·⛔ 改）：
- `F27 mutate` 之出艙碼——逾時、子程序例外、錨數 `n ≠ 1` 三種「無從判定」與「突變未被捕」皆歸 `rc 1`（`verify/probes/probe_WG9373_k966.py` 之 `mutate` 末之 `return 1 if bad else 0`）；該器 docstring 自定 `3 無從判定`，`CLAUDE.md` 有「算不出與判為偽不得共用同一出艙碼」之戒。逐列之出艙可分辨（「逾時」「例外」「錨 n 見」），此混用唯致假紅、⛔ 致假綠；本批之實跑無此三態。
- 其 NOTE 二：`L5` 以 `sorted(set(rec))` 比表，⛔ 斷言「第 1 輪 55、第 2 輪 25」之輪序；暫存目錄之 `rmtree(ignore_errors=True)` 清理失敗時無聲（皆在倉外）。

**本批之自解清單**：
1. `commit` 訊息：依單首 🔑（`自誤 604`）＝ 首列逐字 ＋ 空列 ＋ `Co-Authored-By` 尾列——⛔ 自解（單已明令）。
2. 上列 reviewer 之 ⚠️：不停機而呈發單側。五項：零土地後果（量測器之出艙碼·不動任何宗地）；零生產碼；可機驗（本批 `mutate` 之實跑 ✅ `58`／🔴 `0`·逾時 `0`）；可逆（⛔ 改任何檔·唯記載）；載於本清單。

## ⑩　各段耗時（本機時刻·`2026-10-11`）

| 段 | 時刻 |
|---|---|
| 開場（§零-0〜§零-3） | `10:29:56`（heads 存檔）〜 `10:31` |
| 工項零 | `10:31:36` `commit`·隨即 `push` |
| 工項一（抽塊·施·selftest／wiring `10:32:13`〜`10:32:28`·`mutate` `10:32:37`〜`10:34:49`·reviewer 約 `8.7` 分） | `10:41:49` `commit`·隨即 `push` |
| 工項二 | `10:42:09` `commit`·隨即 `push` |
| 工項三 | 本檔 |
