# `W-G.9-389R`　試算內之程式之停機之上拋　執行報告（執行端·雲端）

> 單：`docs/orders/W-G.9-389_規格單.md`（`134281` B·`sha256` `8ba8c7bc90a61cc871d95fdad038e8206e0ca05d7acf6164db9a552447490ef0`·`SELF_SHA256` `0d30f02fc7df4183ce26a5cf25762555c09ae1c0f8af26efaf7f845fdf846fa9` 自驗相符）。
> 本批唯推新側支 `verify/W-G.9-389-trialstop`（工項零新立·其後皆快轉）；主線 `wip/s1-endpart` ＝ `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`（⛔ 動）。
> 施工樹 ＝ `/tmp/w`（雲端之完整複本·`<repo>`）；撰碼之樹 ＝ `/tmp/wc`（`/tmp/w` 之本地複本·撰碼與自跑用·⛔ 推）；`<O>` ＝ `/tmp/claude-0/-home-user-land-readjustment-trial/86967310-f1b6-5e2d-9a8e-c84a41251721/scratchpad/O`（倉外·⛔ 在任何 git 工作樹內·`git rev-parse --show-toplevel` ⇒ `fatal: not a git repository`）。
> 殼無 `WV_`（`[None, None, None, None, None]`）；`Python 3.11.17`；`shapely 2.2.0`；`nproc` ＝ `4`；並行 ≤ `2`；開工時之 context 餘量約 `14.9 M` tokens。
> 收工閘之實測值載於 `ops/queue` 之 `reports/W-G.9-389_規格單_回報.md`（⛔ 寫入本檔·自指）。主 checkout 之同步由 KL 自行為之（README 第六節第 6 款）。
> 單之複本（`/tmp/w/W-G.9-389_規格單.md`·`執行端.md` 丙 3）記於本地之 `.git/info/exclude`（倉外·⛔ 入任何 `commit`）。

## ① `commit` 與工項

| 工項 | `commit` | 內容 |
|---|---|---|
| 工項零 | `4d21a04373f1e2228fa7ae35f568c60c20c99401` | 本單原封入倉（`docs/orders/W-G.9-389_規格單.md`·新立側支） |
| 工項一 | `1689af8ebbe96d2cac3f366b5f27f83a968851d5` | 量測器（塊 `Fy41`·`7` 改 `1` 新） |
| 工項二 | `a298a4f3e364705a780447294dc9459e096ed4fd` | 生產碼（`app.py`、`verify/selection_pipeline.py`） |
| 工項三 | `b117fb3d3235347f7626de85cecec2e31e94eed1` | 塊 `K32` 入 `K-6` 典、塊 `P43` 入 `docs/待落地清單.md` |
| 工項四 | （本檔所在之 `commit`·見回報） | 本報告與差異檔 |

## ② 停機款之三值（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `929ea20`、heads `48`、⛔ 含新側支、追蹤檔⛔ 變動、`§零-0` 項 `3` 之 `rc 0` 與四簿、旗標 `[None×5]`、環境可匯入 | 主線 `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb`；heads `48`（存 `<O>/heads_before_389.txt`）；新側支之列 `0`；`git status --porcelain --untracked-files=no` 空；issuer_anchor `rc 0`·四簿：自誤 `614`／`629`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `76`／`79`／`[44, 47]`；旗標 `[None, None, None, None, None]`；匯入：初 `rc 1`（`ModuleNotFoundError: shapely`）⇒ 依 README 第六節第 2 款 `python3 -m pip install -r requirements.txt --break-system-packages`（出艙 `<O>/pip_install.txt`）⇒ `rc 0` ⇒ **不成就** |
| `2` | `SELF_SHA256`、bytes／`sha256`、入倉之 blob 相符 | `134281` B·`8ba8c7bc…` ＝ `STATE.json`；`SELF_SHA256` 實算 `0d30f02f…` ＝ 單載；`git cat-file blob HEAD:docs/orders/W-G.9-389_規格單.md` 與來源 `cmp` 同 ⇒ **不成就** |
| `3` | 三塊之 bytes／`sha256`／列數；`git apply --check`；寫出後之 blob | 見 ④；皆相符；`--check` `rc 0` ⇒ **不成就** |
| `4` | 前置之期 | 見 ③；`28` 呼叫皆合期、前置 `4` 之六字樣皆無出艙 `rc 1` ⇒ **不成就** |
| `5` | 規格之歧義涉域上判斷；須改 `§三-3` | 無（`§三-4` 之四項皆查·見 ⑥）⇒ **不成就** |
| `6` | `V-1`〜`V-9` 皆期；⛔ 改器；本案配地⛔ 變 | 皆期（見 ③）；`8` 器之 blob ＝ `§五-1` 項 `5`；`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔同、`parity` 正規化後同 ⇒ **不成就** |
| `7` | `push` 之目標唯新側支（工項）／`ops/queue`（回報）；⛔ 被拒、⛔ `--force`；主線⛔ 推進 | 工項零〜三之四推皆至 `verify/W-G.9-389-trialstop`、皆受；主線仍 `929ea20` ⇒ **不成就**（`ops/queue` 之推一次被拒〔發單端之門鈴之 `commit` 先至〕⇒ 依 README 第五節重取後 `rebase`·⛔ `--force`·見 ⑥） |
| `8` | 工項三之二檔：刪除欄 `0`、嚴格前綴、尾 ＝ 塊、blob；`checkidx`、`gen_fa_index` | 見 ④、⑨；皆相符 ⇒ **不成就** |
| `9` | 收工閘 | 量於工項四之推後·載回報 |
| `10` | ⛔ 作正典之判、⛔ 改塊器命令 | ⛔ 為之；`<repo>` ＝ `/tmp/w`（絕對路徑）⇒ **不成就** |
| `11` | 新檔⛔ 為 `check-ignore` 所命中 | 量於收工閘 `2`·載回報 |
| `12` | 審查之發現涉域上判斷或規格之漏載 | 審查無 (A)／(B)；其三項 (C)（審查者自判「記錄·不阻」）之處置見 ⑥ ⇒ 判**不成就**（其由逐條載 ⑥·供發單端復驗） |
| `13` | 存取被拒、寫入被分類器所拒 | 無 ⇒ **不成就** |

## ③ 前置與驗之出艙

### 前置（於工項一之端 `1689af8`·`/tmp/w`·`2026-10-19T02:49:28Z`〜`03:18:53Z`·並行 `2`）

- **(甲)(乙)** `28` 呼叫（`#1`, `#2`, `#3`, `#4`, `#5`, `#17`, `#6`, `#13`, `#18`, `#7`, `#19`, `#31`, `#32`, `#33`, `#62`〜`#66`, `#69`〜`#71` ＋ `#56`〜`#61`）：皆合期——`#69` `rc 1`·`⇒ 紅 ['受詞缺']；rc 1`；`#70` `rc 1`·`⇒ 紅 ['X1', 'X2', 'X3', 'X4']；rc 1`；`#71` `rc 1`·`⇒ 紅 ['受詞缺']；rc 1`；餘 `25` 呼叫 `rc 0`·末列 ＝ 表；`stderr` 合計 `0` B；耗時之和 `3527` s（逐呼叫見附錄甲）。`F8` 之前態落檔：`f8_pre_35.json` ＝ `8be0160bc14dd92a5331f86eecc995cae0507376`、`f8_pre_00.json` ＝ `6fb86647807f9744594071be25c522b6b506c230`（＝ `§一` 項 `5`）。
- **(丙) 版本之比對**：主線之端 `929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb` ＝ 基準之 sha；`python3 --version` ＝ `Python 3.11.17` ＝ 基準；`python3 -m pip freeze` 之 `sha256`：**裝前** `1280ab514f0c15f8f27e4b0eaf8a483bd9a4ec3d2aa1606aba8e2ca7e7b251b1`（雲端之新容器·`shapely` 等未裝）⇒ 依 README 第六節第 2 款裝之 ⇒ **裝後** `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ＝ 基準 ⇒ 三者皆同 ⇒ **沿用** `基準/929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb.md` 之值（`43` 呼叫·⛔ 重跑）。
- **前置 `4`**（`<O>/pre4_grep.txt`）：六字樣皆無出艙、`rc 1`。
- **pre-flight**（`§零-3`·`python3 verify/probes/probe_order_preflight.py /tmp/w/W-G.9-389_規格單.md`）：`rc 0`·`stderr` `0` B；🔴 `0`／🟡 `3`（`P-4` `:238`、`P-4` `:545`、`P-6` `:1321`）／ℹ️ `2`（`P-5` 相符·`P-3` `def main` ＝ `23421`-`31163`）＝ `§五-1` 項 `9` ⇒ 🟡 三項依單**具名豁免**。

### 驗（工項二 `a298a4f`·⛔ 推前·`/tmp/w`·`2026-10-19T03:23:12Z`〜`04:45:11Z`·並行 `2`·一律從頭整套照跑）

| # | 實 |
|---|---|
| `V-1` | `22` 呼叫皆 `rc 0`、末列 ＝ 表之施後之列；`F33 selftest` `K1`〜`K16` ✅、`P0 判式自驗 16／16` ✅；`F33 wiring` `X1`〜`X5` ✅（`X1` 帶號 `10`〔基準 `10`〕；`X2` app `5`〔基準 `5`〕／selection_pipeline `3`〔基準 `3`〕未合 `[]`；`X4` 換 `0`／增 `6`）；`F33 run` `R1@3.5`（登記 `0`·G 值列 `35`）、`R1@0.0`（登記 `0`·G 值列 `36`）、`R2@3.5`（上拋：「🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成）」）✅（全文見附錄乙） |
| `V-2` | 其餘 `43` 呼叫（`#56`〜`#61` 除外）皆 `rc 0`、末列 ＝ 表之施後之列；`F23 selftest`（`#4`）之 `✅ P0 逐項擾動恰該項紅 75／75` |
| `V-3` | `8` 器之 blob ＝ `§五-1` 項 `5`（`43da36a7…`、`468eb1fa…`、`0e10ba31…`、`7aa267a8…`、`b44cd02b…`、`4081e384…`、`d731fd35…`、`da1bd8c5…`） |
| `V-4` | `run` 二退縮 `rc 0`；`cmp`：`3.5` `rc 0`·`相異 0 項 ⇒ ✅ 同`·`stderr` `0` B；`0.0` `rc 0`·`相異 0 項 ⇒ ✅ 同`·`stderr` `0` B（`k6s3 cmp` 之全文即此一列） |
| `V-5` | `parity` 二退縮 `rc 0`·末列 `⇒ rc 0（不符 0 項）`；正規化之比（`HEAD` 之全值以 `<HEAD>` 代之·前 `1689af8ebbe96d2cac3f366b5f27f83a968851d5`、後 `a298a4f3e364705a780447294dc9459e096ed4fd`）見下 |
| `V-6` | `run` 二退縮 `rc 0`·末列 `⇒ 紅 []；rc 0`；`git hash-object`：`3.5` 二列皆 `8be0160bc14dd92a5331f86eecc995cae0507376`；`0.0` 二列皆 `6fb86647807f9744594071be25c522b6b506c230` |
| `V-7` | 生產碼 `34` 檔對工項一之端相異恰 `2`：`app.py` `55`／`10`·blob `80d00d86155eddb843b3e3e2efa8e2e47c0db142`（bytes 見 ④）、`verify/selection_pipeline.py` `6`／`0`·blob `fec1d5c0f80584ab008612eec92ab540dfe44fdd`；`verify/` 之他檔相異 `0`（`git diff --name-status` 唯 `M verify/selection_pipeline.py`）；頂層之名之增 ＝ 五名、去 `[]`；相異之既有節點 ＝ `§三-2` 之 `11` 函式（恰其集） |
| `V-8` | `app.py`：`raise k6_program_stop(` ⇒ `app.py:10`；`k6_trial_raise_since(_m389,` ⇒ `app.py:5`；`_m389 = k6_trial_mark()` ⇒ `app.py:5`；`K6_PROGRAM_STOPS = []` ⇒ `app.py:1`；`verify/selection_pipeline.py`：`ns["k6_trial_raise_since"](_m389,` ⇒ `:3`；`_m389 = ns["k6_trial_mark"]()` ⇒ `:3` |
| `V-9` | `71` 呼叫之 `stderr` 合計 `0` B；`k6s3 cmp` 二呼叫 `0` B |

**`V-5` 之正規化之比**（`<O>/v5_cmp.txt`）：

```
parity35_pre.json ↔ parity35_post.json：HEAD 之現 1／1；代之後逐位同 True（sha256 25810ad8b1fb8866／25810ad8b1fb8866）；對照·⛔ 代之 ⇒ 逐位同 False
parity00_pre.json ↔ parity00_post.json：HEAD 之現 1／1；代之後逐位同 True（sha256 58a3d9e85d265d15／58a3d9e85d265d15）；對照·⛔ 代之 ⇒ 逐位同 False
call_pre_60.out ↔ call_post_60.out：HEAD 之現 1／1；代之後逐位同 True（sha256 73ba729fc44a775e／73ba729fc44a775e）；對照·⛔ 代之 ⇒ 逐位同 False
call_pre_61.out ↔ call_post_61.out：HEAD 之現 1／1；代之後逐位同 True（sha256 b2f8709d925ec913／b2f8709d925ec913）；對照·⛔ 代之 ⇒ 逐位同 False
```

**`parity` 之末十五列**（施後·`3.5`）：

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（19 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（13 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 3.5, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（37 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（45／45）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
```

（施後·`0.0`）：

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（0 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（0 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 0.0, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（46 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（46／46）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
```

施後 `71` 呼叫之耗時之和 `9831` s·`stderr` 合計 `0` B（逐呼叫見附錄甲）。重跑：無呼叫逾時或 `rc` ≠ 期（⛔ 有重跑之趟·唯 ⑥ 自捕 1 之中斷之趟）。

## ④ 塊之實得與二檔之 bytes

| 塊 | bytes | `sha256` | 列 | 圍欄（單之列） |
|---|---|---|---|---|
| `Fy41` | `50521` | `3465cb3454435641b1e498dc0c24fc6819e2bb4631feac817610c23e6a6d29b6` | `880` | `360`〜`1241` |
| `K32` | `8438` | `91350d1a24ad058ec428843e4d784709fb6ea151ad764c1072b9ca3857c4c729` | `53` | `1245`〜`1299` |
| `P43` | `3463` | `fa89ba2932bfe6622e4a9f9e481180501863c90da45118f44f79d32fc41e0dfb` | `20` | `1303`〜`1324` |
| `CK`（`W-G.9-365` 附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | `807`〜`839` |
| `GF`（`W-G.9-365` 附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | `755`〜`803` |

- 塊 `Fy41`：施前 `7` 器之 blob ＝ `§五-1` 項 `2`（`probe_WG9389_trialstop.py` 施前⛔ 存）；`git apply --check` `rc 0`；施後 `8` 器之 blob ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `8` 檔；`git show --numstat`：`8`／`4`、`5`／`0`、`4`／`0`、`5`／`0`、`7`／`0`、`10`／`0`、`12`／`1`、`662`／`0`。
- `K-6` 典：`859830` → `868268` B（`a3f9d47a…` → `107182948b85fa9ada222ed1e418acc14989e5d6`）；`docs/待落地清單.md`：`7351` → `10814` B（`76bc7135…` → `69c1bf339ad17e3195ee280da8bcc8d799251a1a`）；二檔：改前全檔為改後之嚴格前綴、尾 ＝ 塊、`numstat` `53`／`0`、`20`／`0`。
- 工項二之施後：`app.py` ＝ `80d00d86155eddb843b3e3e2efa8e2e47c0db142`（`1851822` B）、`verify/selection_pipeline.py` ＝ `fec1d5c0f80584ab008612eec92ab540dfe44fdd`（`60609` B）。

## ⑤ 推送

| 工項 | 命令 | 結果 |
|---|---|---|
| 零 | `git push origin HEAD:refs/heads/verify/W-G.9-389-trialstop` | `* [new branch]`·`4d21a04`；推後 heads `49`、主線 `929ea20…` |
| 一 | `git push origin HEAD:verify/W-G.9-389-trialstop` | `4d21a04..1689af8` |
| 二 | 同 | `1689af8..a298a4f`（驗與審查皆符後） |
| 三 | 同 | `a298a4f..b117fb3` |
| 四 | 同 | 見回報（推後之 `git ls-remote --heads origin` 亦載回報） |

## ⑥ 自捕與自解；唯讀獨立審查

### 自捕與自解

1. **`V-8` 之初量 `raise k6_program_stop(` ⇒ `app.py:11`（期 `10`）**：`R-1` 之塊首之註寫「帶號之停機一律 `` `raise k6_program_stop(…)` ``」，其字樣為 `git grep -F` 所計。發現於驗之首趟起跑後（`03:21:39Z` 起·約 `1` 分即中止·其出艙移至 `<O>/aborted_post1/`·⛔ 用）。自解：該註改為「帶號之停機一律經 `` `k6_program_stop` `` 立之」（唯此一列·`app.py:9778`）；工項二之 `commit` 於**未推**之時以 `--amend` 更之（`136b255` → `a298a4f`·⛔ 推過·⛔ 涉遠端之歷史）；其後 `V-1`〜`V-9` **從頭整套重跑**（上表皆此趟）。
2. **`ops/queue` 之接單之推被拒一次**：發單端之門鈴之 `commit`（`7ec1cd2`）先至 ⇒ 重新 `fetch`、`STATE.json` 仍 `pending` ⇒ `rebase`（`log.md` 之末列衝突·二列皆留）⇒ 推（`541545b`）·⛔ `--force`。
3. **進度列**：驗之起跑時於 `ops/queue` 之 `log.md` 增一列（`ca01d55`·防逾時之誤判）。
4. **環境**：雲端之新容器初無 `shapely` 等 ⇒ 依 README 第六節第 2 款裝之（見 ③ (丙)）。
5. **`§三-4` 之自查**（撰碼前·`929ea20`）：
   - 帶號之 `raise`（AST·字串常數）於 `app.py` 恰 `10`（＝ `R-2` 之列）；`verify/selection_pipeline.py` `0`。`raise` 以外帶號之字串常數唯 `app.py:10851` 之 `print`（`GB-182`·非停機）；⛔ 有由變數組之帶號之訊息。`verify/` 之他檔唯 `verify/wv_reconcile.py:166`（`assert_list_integrity`·`GB-86`）——其屬驗證之對帳器（`run_all`／`fixture_e2e_termination` 用之）、⛔ 在試算之路徑；`R-2` 之受詞 ＝ `app.py`（單 `§三-1`）⇒ ⛔ 動·記之。
   - 吞之處：以名之呼叫圖查「捕 `RuntimeError`／`Exception`／裸／`_K6BTrialStop` 而⛔ 再拋、且其本體可達十處之函式」之 `try`：`app.py` 唯 `end_block_merge_run`、`_k929_6_screen_gate`（轉 `st.error` ＋ `st.stop` ＋ `raise`·⛔ 吞·單 `§三-1` 之「⛔ 及之處」）、三畫面之試算、`main` 之二處（調配之輸入之盤點·塊 `K32` 之六之 `10`「照舊」）；`_try965` 以回呼 `trial` 呼之（名之圖⛔ 及·人工確認）；`verify/selection_pipeline.py` 之吞者唯三 harness 之試算；`verify/stepg_pipeline.py` 之 `except Exception` 五處之本體皆幾何之算·⛔ 達十處 ⇒ 八處之外⛔ 有。
   - 本案之試算之外即觸之帶號之停機：`F33 run` `R1` 登記 `0` ⇒ 無。
6. **撰碼中之自跑**（`/tmp/wc`·⛔ 改器）：`F33 selftest`（`rc 0`）、`F33 wiring 929ea20`（`rc 0`）、`F23 wiring 7d8e954`（`rc 0`）、`F24 wiring d7a5ea4`（`rc 0`）。其中 `F33 selftest` 一呼叫（`~2` s）於前置之二呼叫並行之中跑之（第 `3` 個程序·⛔ 驗之受詞·記之）。

### 唯讀獨立審查（`redistribution-reviewer`·⛔ 改檔·⛔ `commit`·暫存唯於 `/tmp/rv389`·`04:46Z`〜`05:12Z`）

審查之結論：**(A) 改配地或違裁示 ⇒ 無；(B) 純實作之瑕 ⇒ 無**。逐條：

| 條 | 所見 | 判 |
|---|---|---|
| `R-1` | 五名之位（`app.py:9779`〜`9801`·`K917_DROPPED = {}` 之後、`def k917_should_drop`〔`9811`〕之前）與序合；式實測：`xGB-1`、`W-GB-2`、`1GB-3`、`GB-`、`GB-x`、`gb-7`、`未裁` ⇒ 停機（⛔ 登記·訊息含 `W-G.9-389` 與 repr）；`（GB-4）`、`【未裁】` ⇒ 登記；③ 之字串常數⛔ 配號式（AST `0`）；⑤ 取首一新登記者（連登 `GB-11`、`【未裁】b` ⇒ 拋 `GB-11` 者）；登記之用唯 `append`／`len`／索引 | 合 |
| `R-2` | 自寫之 AST 掃描：基準帶號之 `raise` 恰 `10`（列號 ＝ 單之表）、`HEAD` 皆 `k6_program_stop`；逐列比對 `−10`／`+55`，`10` 列 `−` 唯一換後 ＝ 對應之 `+`；十處於執行期必配號 | 合 |
| `R-3` | `<where>` 八句逐字、依序全等；八處之位皆合；`end_block_merge_run` 之二句仍相接 | 合 |
| 吞之處⛔ 漏 | 以名建可達 `k6_program_stop` 之集（`50` 名）而掃：八處之外唯 `_k929_6_screen_gate`（停機）、`main` 二處（照舊）；`stepg_pipeline` 之 `except Exception` 之本體皆⛔ 達十處 | 合（限：以名建圖） |
| `§三-3` | 錨：可解析之器之字串常數 `26525`，基準恰一見者 `902` 於 `HEAD` 仍恰一（破 `0`）；新列⛔ 有「四空白以上繼以中文」；函式名恰一者仍恰一；`F23`／`F24 wiring` 自跑 `rc 0`；頂層之增恰五、異恰 `11`；三函式⛔ 案件字面；十處之訊息⛔ 改 | 合 |
| `R-4` | `git diff --stat` 唯二檔；`selection_pipeline` `+6`／`−0` 皆含 `k6_trial_` | 合 |
| 配地 | `F33 run` 自跑：`R1@3.5` 登記 `0`·G 值列 `35`；`R1@0.0` 登記 `0`·`36`；`R2@3.5` 上拋 | 合 |

**二例（審查者自寫·⛔ 用 `F29`／`F33` 之玩具·街廓 `Q1`·p1(0,0)→p2(48,0)·P1 甲 `250`〔街角第 1 宗〕、P2 甲 `50`、P3 乙 `500`、P4 丙 `300`、P5 乙 `40`·G ＝ a × `0.55` − `8`〔首一非街角宗〕·最小分配 `90`·帶號之停機以真呼 `k917_should_drop(…, True, …)` 立之〔真之 `GB-104`〕）**：

- **例一**（入池閘依手冊併入 P1{P1, P2} 後之試算觸 `GB-104`）：基底（無停機）二態同 `alloc {'P1': 165.0, 'P3': 297.0, 'P4': 165.0}`；**改前**：續辦、`alloc {'P1': 164.9945, …}`（`GB-104` 被吞為不過 ⇒ 轉按比例部分併入 `49.99`·試算 `17` 次）；**改後**：上拋「🔴 [試算內之程式之停機·入池閘·併入後之試算] 🔴 `K-9-17` 遞補：街廓 Q1 left 側之**街角第 1 宗** 'P1' 竟為閘一『不合格』…（`GB-104` 之 loud 斷言）。」·登記 `1`。
- **例二甲**（同一入池閘之內二試算相繼：先整筆併入 ⇒ 無號之中止、後按比例部分併入 ⇒ `GB-104`）：**改前**：試算 `['ok','plain','gb104'×12,'ok','ok']`、P1 之記「未成」·併入量 `0.0`（`12` 次 `GB-104` 皆被吞）；**改後**：試算 `['ok','plain','gb104']`、上拋（無號者照舊為不過而續辦·帶號者上拋）·登記 `1`。
- **例二乙**（巢狀：外 ＝ `end_block_merge_run` 之試算、內 ＝ `k929_6_fixpoint`／`_try965`）：改前四形皆續辦（`'標的': None`·記試算中止）；改後：乙1 內無號＋外無號 ⇒ 續辦（照舊）；乙2 內帶號 `GB-104` ⇒ 上拋「🔴 [試算內之程式之停機·末端塊合併再試·試算] 🔴 `K-9-17` …」；乙3 試算之前先存 `GB-777` 之登記＋內無號 ⇒ 續辦（以長度分之·⛔ 波及）；乙4 內 `GB-104` 被吞、其後 `GB-204`（真呼 `k967_pool_less({}, [1])`）亦被吞 ⇒ 上拋首一之 `GB-104` 全文。

**審查者列為 (C)「規格未明載」之三項與 (D) 之記錄**（審查者自判：皆記錄、⛔ 阻工項二之推）：

- `C-1` 號式之 `\d` 依 Unicode（全形數字 `GB-５` 為號）、前一字之界唯 ASCII（`ＡGB-6` 為號）。**執行端之處置**：⛔ 自裁其讀法；本碼之式與單之量測器 `F33` 之 `TAG_RE`（`(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】`）逐字同（即單之用語之機械形）；`app.py` 之十處皆 ASCII ⇒ 本案與一切既有之停機⛔ 受影響 ⇒ 判非停機款 `12` 之「規格之漏載」（⛔ 涉土地後果）；呈發單端復驗時定之。
- `C-2` 未經 `k6_program_stop` 而訊息帶號之 `RuntimeError`（例：`verify/` 之他檔將來新立者）仍為不過。**處置**：其即塊 `K32` 之二之乙（以登記判之）與戊（新立之帶號之停機一律經 `k6_program_stop`·`X1` 守 `app.py`）所定之射程 ⇒ 規格已載·記之。
- `C-3` ③ 之自我停機（⛔ 帶號之訊息）本身無號、⛔ 登記，若於試算之內觸之則依庚為不過。**處置**：其形為 `R-1` ③ 所令（「其字串常數⛔ 配 ②」）；十處於執行期必配號 ⇒ 不可達 ⇒ 規格已載·記之。
- `D-1` `R-3` `1`、`2` 之上拋唯在 `except` 之支（依 `R-3` 之表）；試算成功而其內部吞過一筆登記者，此二處⛔ 見之、外殼或其後之試算見之；名之掃描⛔ 見此類內部之吞。`D-2` 試算之外之截字（`_k929_6_screen_gate` `[:500]`、`main` 之 `st.error`）照舊。`D-3` ①② 之前之註為 `#: 🔒 …`，其上之塊註首列載「🆕 `W-G.9-389`」（「形如」之寬讀）。`D-4` `probe_WG971_wrap.py`、`probe_ruling_K4_s_origin.py`、`probe_WG921_b_slot_divergence.py` 於 `py3.11` 解析失敗（早於本單）·錨之自掃⛔ 含之。`D-5` 登記於同一程序中唯增（設計使然）。

⇒ 發現⛔ 涉域上判斷（三項 (C) 皆⛔ 涉配地之果·其讀法⛔ 由執行端定）、純實作之瑕無 ⇒ 工項二推之。

## ⑦ 設計說明（`§三-5`）

- **`R-1`**：落於 `app.py:9776`〜`9808`（`K917_DROPPED = {}`〔`:9773`〕之後、`def k917_should_drop`〔`:9811`〕之前）：塊註（`# ── 🆕 \`W-G.9-389\`：…──` 與其下四列）；`K6_PROGRAM_STOPS = []`（其前 `#: 🔒` 之註）；`K6_PROGRAM_STOP_RE = re.compile(r"(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】")`（既有之 `import re`·`app.py:13`）；`k6_program_stop(msg)`：`_s = str(msg)`；⛔ 配 ⇒ `raise RuntimeError(f"🔴 \`W-G.9-389\`：\`k6_program_stop\` 之訊息⛔ 帶程式之停機之號 ⇒ 停機（⛔ 登記）：{_s[:200]!r}")`；配 ⇒ `K6_PROGRAM_STOPS.append(_s)`、`return RuntimeError(_s)`；`k6_trial_mark()` ⇒ `len(K6_PROGRAM_STOPS)`；`k6_trial_raise_since(mark, where)` ⇒ 長度 ＞ `int(mark)` 時 `raise RuntimeError(f"🔴 [試算內之程式之停機·{where}] {K6_PROGRAM_STOPS[int(mark)]}")`，否則 `return None`。三函式各一列之 docstring（⛔ 折行）。
- **`R-2`**：十處之 `raise RuntimeError(` → `raise k6_program_stop(`（引數與折列⛔ 動）：`app.py:7496`（`evaluate_parcel_width_n14`·`GB-13`）、`:9835`（`k917_should_drop`·`GB-104`）、`:10420`（`_try965`·`GB-205`）、`:12491`、`:12594`（`adj_intake`·【未裁】）、`:14646`、`:14649`（`k967_pool_out`·`GB-204`）、`:14661`、`:14664`（`k967_pool_less`·`GB-204`）、`:16476`（`_gb201_953`·`GB-201`）（`HEAD` 之列號）。
- **`R-3`**：八處各增二列（mark 與上拋）；尾註⛔ 附（`§三-3` 之 1 之錨之險之避）。改後之前後三列見附錄丙。
- **`R-4`**：他字⛔ 動；`verify/selection_pipeline.py` 唯增 `6` 列。新區域名 `_m389`（基準中 `0` 見）。
- **`§三-3` 之自查**：`1` 字樣之錨 ⇒ `F23 wiring`（`W8`）、`F24 wiring`（`W7`）自跑與驗皆 `rc 0`；新之註與 docstring 之列⛔ 有「四空白以上繼以中文」起首者（註皆於第 `0` 欄、其續列為 `#` ＋ 三空白）；`_m389` 與五名⛔ 撞名。`2` 突變之錨 ⇒ `V-1`／`V-2` 之突變器（`#19`、`#22`、`#43`、`#47` 等）皆綠。`3` 頂層之名 ⇒ `V-7`／`X3`。`4` 案件字面 ⇒ `X5`。`5` 十處之訊息⛔ 改 ⇒ `X3` 之 `_diff_ok`（差唯換列與增列）。
- 全文差異：同目錄之 `W-G.9-389R_試算內之程式之停機之上拋_差異.diff`（`git diff 1689af8 a298a4f -- app.py verify/selection_pipeline.py`·`15741` B）。

## ⑧ `app.py` 與 `verify/selection_pipeline.py` 之全文差異

見同目錄之 `W-G.9-389R_試算內之程式之停機之上拋_差異.diff`。

## ⑨ 工項三之 `checkidx`、`gen_fa_index`

- `python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`·末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md` ⇒ `rc 0`·`則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` `cmp` 同。

## ⑩ 各段耗時（UTC·並行 `2`）

| 段 | 時 |
|---|---|
| 接單（`ops/queue`） | `02:44`〜`02:45` |
| 開場（`§零-0`·裝依賴·pre-flight） | `02:45`〜`02:47` |
| 工項零、一 | `02:47`〜`02:49` |
| 前置 (甲)(乙) `28` 呼叫 | `02:49:28`〜`03:18:53`（`29` 分·耗時之和 `3527` s） |
| 撰碼與自跑（與前置並行·`/tmp/wc`） | `02:50`〜`03:21` |
| 驗之首趟（中斷·⑥ 自捕 1） | `03:21:39`〜`03:22` |
| 驗 `V-1`〜`V-9`（`71` 呼叫） | `03:23:12`〜`04:45:11`（`82` 分·耗時之和 `9831` s） |
| 唯讀獨立審查 | `04:46`〜`05:12` |
| 工項二之推、工項三 | `05:13`〜`05:15` |
| 工項四 | `05:15`〜 |

---

## 附錄甲　前置與施後之 `71` 呼叫（`rc`／`stderr` B／末列逐字·耗時 s；`<repo>` ＝ `/tmp/w`；`<態>` ＝ `pre`／`post`；「沿用基準」＝ 前置 (丙)）

| # | 命令 | 工項一之端（rc／stderr B／末列·s） | 施後（rc／stderr B／末列·s） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（102）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（104） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（359）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（347） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（33）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（34）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（34） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（27） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（11） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（194） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（55） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（389）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（384） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（532）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（529） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8）·照跑·(甲) | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（7） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（61） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（319） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1447） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（26） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（21） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（14）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（17） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（202）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（204） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（283）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（273） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（28） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（20） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（12） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（9） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（152） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（41） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（707） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（124） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（95） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（278） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`紅項 [] 器紅 0`（9） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（278） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（163）·照跑·(乙) | `0`／`0`／`（JSON 之摘要列·略）`（165） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（119）·照跑·(乙) | `0`／`0`／`（JSON 之摘要列·略）`（117） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（164）·照跑·(乙) | `0`／`0`／`⇒ 紅 []；rc 0`（162） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（118）·照跑·(乙) | `0`／`0`／`⇒ 紅 []；rc 0`（118） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（349）·照跑·(乙) | `0`／`0`／`⇒ rc 0（不符 0 項）`（339） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（252）·照跑·(乙) | `0`／`0`／`⇒ rc 0（不符 0 項）`（245） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（3）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（281）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（279） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（2）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1012） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | 沿用基準（(丙)·⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1001） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（1）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `1`／`0`／`⇒ 紅 ['X1', 'X2', 'X3', 'X4']；rc 1`（104）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（105） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（1）·照跑·(甲) | `0`／`0`／`⇒ 紅 []；rc 0`（363） |

前置 28 呼叫·耗時之和 3527 s·stderr 合計 0 B；施後 71 呼叫·耗時之和 9831 s·stderr 合計 0 B·並行 2

## 附錄乙　`V-1` 之 `22` 呼叫之全文（施後·`a298a4f`）

### `#1` `python3 verify/probes/probe_WG9385_k974.py selftest <repo>`（`rc 0`·`stderr` `0` B·`2` s）

````
  ✅ K1：{'front': 3.75, 'left': 1.0}／[]／[]
  ✅ K2：{'B1': {'front': 2.25}}／{'B1': {'front': 3.75}}
  ✅ K3：{'B1': {'front': 3.0}}
  ✅ K4：{'B1': {'front': 1.75}}／{'B1': {'front': 1.75}}／[]
  ✅ K5：{'B1': {'front': 1.75}}
  ✅ K6：{'B1': {'front': 3.75}}
  ✅ K7：{'B1': {'front': 3.15}}／[('RE', 0.4), ('RW', 0.6)]
  ✅ K8：{'B1': {'front': 0.0}}／['B1 正面道路勾選新闢，但未偵測到道路 BLOCK']／[]
  ✅ K9：{'B1': {'front': 3.75}}／['B1 正面：中心線垂距 × 2 ＝ 12.00 m，與輸入路寬 15.00 m 相差逾 0.5 m，請確認']
  ✅ K10：{'B1': {'front': 3.0882352941176467}}／{'B1': {'front': 2.625}}
  ✅ K11：['道路 BLOCK RA 未繪 CENTERLINE（B1 正面臨之），請補畫']
  ✅ K12：{'抵充地': {'100-1': 1.0, '100-3': 0.5, '100-4': 0.5}, '第33條排除': {}, 'errors': []}／['填列錯誤：甲段 100-2「第33條排除」欄填「是」，但該地號非公有地（U_LAND 公私別）', '填列錯誤：甲段 100-2「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）', '填列錯誤：甲段 100-1「第33條排除」欄填「Y」，僅得填「是」或空白', '填列錯誤：甲段 100-9「抵充地」欄填「是」，但 U_LAND 無對應資料']／['填列錯誤：地號 100-1 於 甲段、乙段 皆有，「抵充地」無從對應宗地']／{'抵充地': {}, '第33條排除': {}, 'errors': []}
  ✅ K13：[[(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]]
  ✅ K14：2.25／0.0／0.0
  ✅ K15：{'B1': {'front': 3.75}}
  ✅ K16：{'B1': {'front': 3.75}}／['尚無宗地資料（地籍），中心線是否為重劃區界⛔ 判（以輸入之路寬計）']
  ✅ K17：{'抵充地': {'100-3': 0.5}, '第33條排除': {}, 'errors': ['填列錯誤：甲段 100-1「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數', '填列錯誤：甲段 100-2「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數']}
  ✅ K18：{'B1': {'front': 0.0}}／['道路 BLOCK RA 內抵充地之面積大於扣除路口後之面積（宗地之片重疊），請檢查地籍（B1 正面臨之）']
  ✅ K19：[('壞檔', True, ['地籍資料來源讀取失敗（BadZipFile）：File is not a zip file']), ('缺欄', True, ["地籍資料來源讀取失敗（KeyError）：'段小段'"])]
  ✅ K20：前提（浮點之負）6／60；不符 []（0）
  ✅ K21：[True, True]
  ✅ K22：[True, True]
⇒ 紅 []；rc 0
````

### `#2` `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`（`rc 0`·`stderr` `0` B·`104` s）

````
  ✅ W1 頂層之新名與⛔ 案件字面：[True, True, True, True]／K974_PARAMS True／字面 []
  ✅ W2 main() 恰一處呼之：['k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)']
  ✅ W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）：
  ✅ W4 JUNCTION 存 session：
  ✅ W5 步驟 H 之段以假 st 實跑：[{'label': 'B1', 'front_width': 15.0, 'front_length': 0.0, 'front_new': False, 'left_side_width': 0.0, 'left_side_length': 0.0, 'left_side_new': False, 'right_side_width': 0.0, 'right_side_length': 0.0, 'right_side_new': False, 'front_scale': 2.25, 'left_side_scale': 0.5}]／[('warning', '⚠️ 警示甲')]／[('error', '⛔ 錯甲'), ('error', '⛔ 錯乙')]／停 False/True
  ✅ W6 verify/ 之生產碼⛔ 呼之：[]
  ✅ W7 main／calc 唯增列（具名之換列三）·頂層之相異：相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K974_PARAMS', 'adj_intake', 'calc_special_burden_total', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k967_pool_less', 'k967_pool_out', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'main']／刪列 3
⇒ 紅 []；rc 0
````

### `#3` `python3 verify/probes/probe_WG9385_k974.py run <repo>`（`rc 0`·`stderr` `0` B·`347` s）

````
  各面之尺度：R4 front 0.0／left 1.0／right 1.0；R6 front 2.0／left None／right 1.0；R5 front 2.0／left 1.0／right None；R2 front 2.0／left 1.0／right None；R3 front 2.0／left None／right 1.0；R1 front 0.0／left 1.0／right 1.0
  ✅ R1 尺度 ＝ 快照之負擔尺度_輸入：不符 []／警示 []／錯誤 []
  ✅ R2 calc 之列給尺度與否逐值同：741.76／741.76
  ✅ R3 抵充地之模擬（628-34·RD1）：RD1 1082.2651／628-34 之片 131.6000／比例 0.878403／負擔路寬 7.0272／期 1.513613、0.756806／得 1.513616、0.756808
  ✅ R4 私有地填「是」⇒ 填列錯誤：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']
  ✅ R6 二欄之結果之存與換檔：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']／[]
  ✅ R5 JUNCTION 之模擬（RD1 之一端）：框內 89.6652／比例 0.867420／期 1.469679／得 1.469679
⇒ 紅 []；rc 0
````

### `#4` `python3 verify/probes/probe_WG9363_k953.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1` s）

````
── 手冊先行（K-9-53 ①）之各支 ──
  ✅ K1 跨分配線（所鄰之已配得之宗恰一）⇒ 整筆併入、出 build、帶 段三併出
  ✅ K2 跨分配線（所鄰之已配得之宗分處二街廓）⇒ 併入應分配面積（G）較大者
  ✅ K3 （K-9-67）二者之 G 並列 ⇒ 重劃前面積同（300）⇒ 暫編地號小者 E1(1)；E1 之重劃前面積 250 ⇒ X1(2)
  ✅ K4 建地片與同街廓之已配得之宗相鄰 ⇒ 依手冊整筆併入之（K-9-58 ③·W-G.9-380）
  ✅ K5 道路·兩側皆有 ⇒ 依中心線切分、各半併入該側之宗（a′ × 半之面積比）
  ✅ K6 道路·唯一側有 ⇒ 整筆往該側（所鄰之街廓依中心線分側）
  ✅ K7 道路·兩側皆無 ⇒ 未併、帶 段三餘量 ＝ a（視同無同歸戶）
  ✅ K8 道路片全在無已配得之側（⛔ 鄰有之側之街廓）⇒ 仍整筆往有之側
  ✅ K9 隔道路之分不到之建地 ⇒ 隨道路片往另一側之宗
  ✅ K10 公設地 ⇒ 平分於其合併群所及之已配得之街廓（群外之已配得之宗⛔ 與）
  ✅ K11 公設地不相連於任何已配得之宗 ⇒ 未併、帶 段三餘量 ＝ a
  ✅ K12 路口之道路片（鄰三街廓以上、含公設地）⇒ 比照公設地平分
  ✅ K13 落點四層瀑布：① 同原地號者先於較近者；② 皆非同原地號 ⇒ 質心距近者；③ 等距 ⇒ G 大者；④ 皆同 ⇒ 暫編地號
  ✅ K14 （K-9-66）整批不過 ⇒ 建地整筆不過 ⇒ 按比例部分併入 10；剩下 50 依 K-9-51（他街廓之已配得之宗·距離近者先）
  ✅ K15 可拆分之片之最大面積（0.01 ㎡ 之格）；其餘 ⇒ K-9-51 皆無 ⇒ 入合併單位、帶 段三部分併出／段三餘量
  ✅ K16 併入後配地中止 ⇒ 不過（記其由·⛔ 停機）
  ✅ K17 帶段三之鍵之片⛔ 受理
  ✅ K18 無任何配得土地之地主：同號之連通分量之再試未成 ⇒ 回輸入之同一物件、紀錄唯再試之列（K-9-73 ④）
  ✅ K19 入池閘之合併單元：取代後之配地全同 ⇒ 取代；相異 ⇒ ⛔ 取代（記之）
  ✅ K20 調配之輸入（⛔ 改·沿用段三之鍵）：併出 ⇒ 原位次配地（所屬單元『段三併入 …』）；餘量 ⇒ 入合併單位；待同歸戶併入 ＝ 空
  ✅ K21 公設地調配之 temp（⛔ 改·沿用段三之鍵）：併出而無餘量 ⇒ 去之；部分併出 ⇒ 依餘量之比縮之
  ✅ K22 a′ 之折算（街廓之地價比）
  ✅ K23 （K-9-66）整批不過時：建地先（全入）、道路次（按比例）、公設地未試；剩下之列於諸輪之後
  ✅ K24 旗標 WV_K953：未設／on ⇒ 真；off ⇒ 偽；他值 ⇒ 停機
  ✅ K25 可為受詞之片之歸戶於 build 皆無片（例：歸戶表為空）⇒ ⛔ 試算配地、回輸入之同一物件、紀錄 ＝ []
  ✅ K26 試算之摘要：抵費地之形放不下最小建築面積之矩形 ⇒ 配餘地不合格一處；保留 ⇒ 保留宗與其 G；餘⛔ 計
  ✅ K27 入池閘之單元：成員（缺 ⇒ 自身）；成員 ≥ 2 者為單元（深拷貝）
  ✅ K28 K-9-51 之候選含 x 之本街廓之已配得之宗（與 x ⛔ 相連·距離 0）⇒ 先試併之、過 ⇒ 併入、出 build（K-9-55）；其檢核不過 ⇒ 記未成、續試他宗；皆不行 ⇒ 入合併單位（補令二·乙案）
  ✅ K29 入池閘之旗標 off（WV_K929_6）⇒ 手冊先行不辦（harness 與畫面皆回輸入之同一物件、紀錄 []、畫面⛔ 呼叫 st）；二旗標皆判（WV_K953 off 而 WV_K929_6 非法 ⇒ 停機）
  ✅ K30 畫面：旗標值非法（WV_K953 或 WV_K929_6）⇒ f3_k6b_stage3_error ＝ （手冊先行）…、st.error ＋ st.stop、⛔ 寫紀錄
  ✅ K31 入池閘之單元之取代後：build ⊂ temp（同物件）、temp 中之標的 ＝ 單元（帶入池閘併入）、他成員仍在 temp 而⛔ 在 build
  ✅ K32 K-9-51 之候選同距離（0）：本街廓之宗居先於他街廓之宗（G 較大者亦然·K-9-55 之二）；本街廓無之、或其檢核不過 ⇒ 他街廓之宗
  ✅ K33 K-9-51 之本街廓之候選與 x 相連（C0 之後始為已配得）、⛔ 相連 ⇒ 皆本街廓之宗居先、併入之（W-G.9-380）
  ✅ K34 K-9-51 之本街廓之候選之成員取當下之試算：其單元於 C0 之後始含與 x 相接之片、該片⛔ 與 x 相接 ⇒ 皆併入之（W-G.9-380）；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K35 本街廓之候選：G 較小者（H2(1)）與 x 相接 ⇒ 相接者（距離 0）先、併入之（K-9-51·W-G.9-380）；後者⛔ 與 x 相接 ⇒ 併入 G 較大者
  ✅ K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入
  ✅ K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入其計畫之受併宗
  ✅ K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片——⛔ 停機、依計畫併入（W-G.9-380）；⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（程式自我檢查·K-9-57 ⑧）
  ✅ K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）
  ✅ K41 跨二街廓之小片 S(1) 唯與已配得之宗 R(1) 之成員 Q(1)（⛔ R(1) 之自身之形）相連 ⇒ 手冊先行連同成員看之、依手冊整筆併入 R(1)（巳 ③）
  ✅ K42 計畫之同街廓相鄰之已配得之宗（Q1(1)·X1(2) 為他地號 ⇒ ⛔ 第 31 條第 3 款）之併入之檢核不過（BA 之容量 0）⇒ 記未成、依 K-9-51 併入他街廓之宗（X1(2)）
  ✅ K43 同街廓相鄰（Q1(1)）與他街廓之同一原地號（X1(2)）並存 ⇒ 第 31 條第 3 款先（K-9-73）：X1(2) 之 G 400 ⇒ X1(2)；Q1(1) 之 G 400 ⇒ 仍 X1(2)
  ✅ K44 同街廓相鄰之已配得之宗二（A1(1) G 300、A2(1) G 200）⇒ 應分配面積大者 A1(1)（K-9-61 ①⑦·K-9-67）
  ✅ K45 （K-9-73 ⑤）與他街廓之已配得之宗（X1(2)·他地號）相連而無同一原地號者 ⇒ ⛔ 依手冊併入（計畫無受併宗·未併）
  ✅ K46 （K-9-73 ③⑤⑦）分不到之 C1(1) 與他街廓之同一原地號 C1(2) 及他地號 G1(1)（G 較大）皆相連、且隔自己之道路片 R1(1) ⇒ 第 31 條第 3 款（唯同一原地號）先 ⇒ C1(2)
  ✅ K47 （K-9-73 ⑥·手冊道路用地分配原則 1）分不到之 C1(1) 隔自己之道路片 R1(1)（另一側 X1(2)），而同街廓有已配得之C9(1) 與之相連 ⇒ 道路兩側皆有己地（道路片依中心線切分·⛔ 隨道路往另一側）⇒ 併入同街廓相鄰之 C9(1)
  ✅ K48 （K-9-73 ⑤）分不到之 X1(1) 與同街廓之 Q1(1) 及他街廓之他地號 X1(2)（G 400·較大）皆相連 ⇒ 他地號之相連⛔ 入比較 ⇒ 併入同街廓相鄰之 Q1(1)
  ✅ K49 （K-9-73 ④）X1(1)（BA 60）與 X1(2)（BB 300）皆不配地 ⇒ X1(1) 整筆併入 G 大之 X1(2)；併後 X1(2)（360）配地 ⇒ 成：X1(1) 出 build、帶 段三併出 ['X1(2)']；X1(2) 之 面積_m2 60、帶 第31條第3款併入 ['X1(1)']
  ✅ K50 （K-9-75）受併之片依應分配面積（不配地紀錄之 G）：X1(1) 之 G 500 ＞ X1(2) 之 300 ⇒ X1(2) 併入 X1(1)（⛔ 依面積）
  ✅ K51 （K-9-75·K-9-67）G 並列（皆 100）⇒ 重劃前面積大者（X1(2) 300 ＞ X1(1) 60）受併（⛔ 暫編地號之序）
  ✅ K52 （K-9-29）再試之併入量依 a′（BA 之地價 2 倍）⇒ 120
  ✅ K53 （K-9-75 ②）同一原地號跨三街廓（X1(1)·BA ─ X1(2)·BB ─ Z1(1)·BD·X1(1) 與 Z1(1) ⛔ 直接相接）皆不配地 ⇒ 餘二片皆併入 G 最大之 Z1(1)（400）；併後 760 配地 ⇒ 成
  ✅ K54 （K-9-75 ②）三街廓之同號之連通分量而 Z1(1) 已配得 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1)（⛔ 與 Z1(1) 直接相接）亦併入 Z1(1)
  ✅ K55 （K-9-73 ⑥）同一原地號而隔道路之 C1(1)（BC）⛔ 入同號之連通分量 ⇒ 再試唯 X1(1) → X1(2)
  ✅ K56 再試之受詞存在而試算未回 dropped ⇒ 停機（⛔ 以空代之）
  ✅ K57 同號之片 X1(2) 為已配得之宗 Y1(1) 之成員 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1) 併入 Y1(1)
  ✅ K58 （K-9-75）同一原地號之公設地之片（P1(1)·PK·與 X1(2) 相接）⛔ 入同號之連通分量 ⇒ 再試照行（X1(1) → X1(2)）
  ✅ K59 （K-9-73 ⑨）受併之片配地而「不影響原位次」之檢核不過（BB 之配餘地不合格）⇒ 未成（⛔ 施）
  ✅ K60 再試成而受併之片 X1(2) 為同地主之 Y1(1)（宿主）之單元之成員 ⇒ 單元之取代（X1(2) 出 build）之後，Y1(1) 之單元帶 第31條第3款併入 ['X1(1)']（⛔ 失）
  ✅ K61 （K-9-71）BC 之使用分區（商業區）異於片之所屬街廓 BA ⇒ 五級排後：剩下 50 併入 BD 之 Z1(1)（⛔ 距離近之 C1(1)）
  ✅ K62 （K-9-71）五級皆同而 BC 較深（40）⇒ 排後 ⇒ Z1(1)；BC 深 30.1（同深之容差 0.1 m 內）⇒ 依距離 ⇒ C1(1)
  ✅ K63 （K-9-71）BD 之最小建築面積往大（100）⇒ 排後而⛔ 淘汰：C1(1)（BC 容 0）不過 ⇒ 續試 Z1(1) 成
  ✅ K64 他街廓之候選二以上（BC、BD）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）
  ✅ K65 他街廓之候選唯一（BB·C1 去之）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（K42 之形）
  ✅ K66 五級之屬性缺片之所屬街廓（BA）⇒ 停機
  ✅ K67 五級之屬性之回呼唯於須比時呼之、且一次（K61 之形 ⇒ 1；Z1 非 g1 ⇒ 他街廓唯一 ⇒ 0）
  ✅ K68 k971_key5 ＝ adj_candidate_lists 之建地軌之八鍵之前六（合成之屬性三組·七街廓·逐對 126）
  ✅ K69 再試成而受併之片 X1(2) 為 Y1(1) 之單元之成員；取代後之配地相異（未取代）⇒ 當下之態⛔ 變：X1(2) 仍在 build 且帶標記、宿主 Y1(1)⛔ 帶鍵
  ✅ K70 他街廓唯一（BC）而其候選二宗（C1(1)、C9(1)·皆 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行 ⇒ C1(1)
  ✅ K71 五級與深度皆同之他街廓 BC（距 10）、BD（距 20）、BZ（距 1·名序最後）⇒ 依距離 ⇒ BZ 之 Z9(1)（⛔ 依街廓名）
  ✅ K72 （K-9-71）正面路寬：BA 8、BC 15（往寬）、BD 6（往窄）⇒ 二者皆異、級距 BD 先（往窄先於往寬）⇒ Z1(1)
  ✅ K73 （K-9-71）正面道路：BC 臨他路（RX）⇒ 排後 ⇒ Z1(1)
  ✅ K74 五級之屬性之回呼回非 dict ⇒ 停機
  ✅ K75 （K-9-71）道路之片 R1(1)（RD）之北半部分併入 X1(2)（BB 容 33.333）後，剩下 16.67 之他街廓之候選 ＝ C1(1)（BC·距 0·使用分區 商業區）、Z1(1)（BD·距 10）⇒ 道路之片照距離 ⇒ C1(1)（⛔ 依五級排 Z1(1) 先）
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 75／75
⇒ 紅 []；rc 0
````

### `#5` `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`（`rc 0`·`stderr` `0` B·`33` s）

````
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', '_k929_6_screen_gate', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'main']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（610）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
````

### `#17` `python3 verify/probes/probe_WG9363_k953.py run <repo>`（`rc 0`·`stderr` `0` B·`384` s）

````
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.47／ΣG 之變 2934.53（和 ≤ 0.1）True
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.83／ΣG 之變 3663.88（和 ≤ 0.1）True
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

### `#6` `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`（`rc 0`·`stderr` `0` B·`34` s）

````
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', '_k929_6_screen_gate', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'main']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（612）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
````

### `#13` `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1` s）

````
── 規格步 4 乙（K-9-53 ②·第一趟）之各支 ──
  ✅ K1 旗標：未設／空／' On ' ⇒ True；off／OFF ⇒ False；他值 ⇒ 停機
  ✅ K2 無受詞 ⇒ 回輸入之同一物件、紀錄 []、⛔ 試算；build 片不在 temp ⇒ 停機（受詞為空亦然）
  ✅ K3 整體成：名單首 BA 無其已配得之宗 ⇒ 略過；BB 之受併宗 X1(2)（同原地號）；三片皆併、建地片自 build 去、輸入⛔ 改、build ⊆ temp（同物件）
  ✅ K4 整體不過（BB 之容量 150）⇒ 逐片：建地整筆成、道路片取最大面積（0.01 之格）、公設片未成；剩下續往名單之下一街廓 BD（整體成·受併宗 Z1(1)）
  ✅ K4b 整體不過之列記其由（配餘地不合格）
  ✅ K5 名單盡而有剩下 ⇒ 剩下之列（留於合併單位）；部分併出者之三鍵（段三部分併出·段三餘量）
  ✅ K6 全不容 ⇒ 每街廓整體＋三逐片皆未成、剩下 ＝ 全部；⛔ 改宗地（建地片仍在 build·無鍵·無增）
  ✅ K7 受併宗之序（同街廓有二宗）：① 同原地號居先（距離較遠亦然）② 距離近 ③ 同距離 ⇒ G 大 ④ 同 G ⇒ 重劃前面積大（K-9-67）⑤ 再同 ⇒ 暫編地號小
  ✅ K8 前已有段三之三鍵之片：其剩下 ＝ 段三餘量；全併 ⇒ 段三併出合之、去部分二鍵；部分 ⇒ 段三部分併出合之、段三餘量 ＝ 新剩下
  ✅ K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（程式自我檢查·K-9-57 ⑧·`W-G.9-370` 之訊息）
  ✅ K10 現態之配地中止 ⇒ 停機
  ✅ K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ 共同負擔用地（相異）；無名單 ⇒ 停機；名單重複 ⇒ 停機
  ✅ K12 GB-199：受併宗之序之距離取 slice_geom 之原形（temp 之形縱異亦然）；片之原形缺 ⇒ 停機
  ✅ K13 a′ 折算（K-9-45 二）：併入量 ＝ 來源面積 × p(來源) ÷ p(受併宗)；最大面積之格取來源面積；三鍵之部分併出記來源面積
  ✅ K14 「不影響原位次」：併入使同街廓原保留之宗不保留 ⇒ 不過（整體與逐片皆然）
  ✅ K15 GB-201（手冊先行）：計畫之受併宗於當下之試算未保留 ⇒ 停機（可拆分之片／整筆之建地片）
  ✅ K16 三旗標（WV_ADJ4／WV_K953／WV_K929_6）之任一 off ⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 呼叫 st
  ✅ K17 三旗標之任一其值非法 ⇒ harness 停機；畫面 ⇒ f3_k6b_stage3_error ＝ （第一趟）…、st.error、st.stop、⛔ 寫紀錄
  ✅ K18 adj4_plan：無受詞 ⇒ []；唯公設軌 ⇒ 正面道路之缺以佔位代之、名單依距離；建地軌 ⇒ 停機（正面道路無識別符）
  ✅ K19 adj4_depth_of：取 f3_alloc_depth_by_label（缺 ⇒ {}）；回新 dict
  ✅ K20 adj4_trial_state：摘要 ＋ err ＋ 成員與單元（成員 ≥ 2 者為單元·深拷貝）
  ✅ K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True
  ✅ K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st
  ✅ K23 R-8 之止：整體不過（他街廓之原保留之宗失·非單調之玩具）而逐片皆成 ⇒ 諸片皆無剩下 ⇒ 止於本街廓（⛔ 往名單之次街廓 BD）
  ✅ K24 （K-9-66）T 含建地片之所屬街廓：全數併出使 BA 之 Q1 失 ⇒ 整體與建地之全併皆不過；按比例 59.99（留 build）⇒ 過；道路、公設地未試
  ✅ K25 （K-9-66）同類按比例：建地全入後道路容 190 ⇒ R9 126.67、R1 63.33（各乘 190／300）；列依剩下大者先
  ✅ K26 R-12：併入後之配地中止 ⇒ 不過（記其由）；整體不過 ⇒ 逐片（公設片取最大面積）
  ✅ K27 R-10′（K-9-57 ⑧·程式自我檢查）：同一輪中併入某街廓之前，以當下之試算查其所受之建地片——前一街廓之併入使之已為已配得之宗（依既定機制不會發生·玩具以非單調之回呼造之）⇒ 停機（⛔ 靜默併出）；對照 ⇒ 二街廓皆整體成
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 28／28
⇒ 紅 []；rc 0
````

### `#18` `python3 verify/probes/probe_WG9367_adj4.py run <repo>`（`rc 0`·`stderr` `0` B·`529` s）

````
  ✅ R1@3.5：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@3.5：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@3.5：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6700（Σ|ΔG| 7.6900）／ΣΔ抵費地 -7.6500（和 +0.0200·≤ 0.1）
  ✅ R4@3.5：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@3.5：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
  ✅ R1@0.0：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@0.0：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@0.0：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6400（和 +0.0400·≤ 0.1）
  ✅ R4@0.0：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@0.0：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
⇒ 紅 []；rc 0
````

### `#7` `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`（`rc 0`·`stderr` `0` B·`3` s）

````
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', '_k929_6_screen_gate', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'main']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
````

### `#19` `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>`（`rc 0`·`stderr` `0` B·`7` s）

````
  ✅ M00 —·基準（⛔ 突變）：錨 1 見；紅 []；所指 []
  ✅ M20 R-12·原保留之宗之判去之：錨 1 見；紅 ['K14', 'K23', 'K24']；所指 ['K14']
  ✅ M21 R-12·配餘地不合格之判去之：錨 1 見；紅 ['K4', 'K4b', 'K5', 'K6', 'K8', 'K13', 'K25']；所指 ['K4b']
  ✅ M23 R-12·併入後之配地中止改為過：錨 1 見；紅 ['K26']；所指 ['K26']
  ✅ M24 R-13·段三併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M25 R-13·段三部分併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M26 R-13·全併⛔ 去部分二鍵：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M27 R-13·段三餘量之值誤：錨 1 見；紅 ['K5', 'K8', 'K13']；所指 ['K8']
  ✅ M30 R-16·GB-201 之判恆過：錨 1 見；紅 ['K15']；所指 ['K15']
⇒ 突變 8（另基準一）；紅 []；rc 0
````

### `#31` `python3 verify/probes/probe_WG9351_intake.py selftest <repo>`（`rc 0`·`stderr` `0` B·`17` s）

````
── 合成對照（AST 抽出之 adj_*）──
  ✅ S1 逐切片之類：得 {'x': '原位次配地', 'y': '建築街廓內不能分配', 'r': '共同負擔用地·入合併單位', 'p': '共同負擔用地·入合併單位', 'z': '原位次配地', 's': '共同負擔用地·待同歸戶併入'}　期 {'x': '原位次配地', 'y': '建築街廓內不能分配', 'r': '共同負擔用地·入合併單位', 'p': '共同負擔用地·入合併單位', 'z': '原位次配地', 's': '共同負擔用地·待同歸戶併入'}
  ✅ S2 合併單位（歸戶·軌·原街廓·成員）：得 [('GA', '建地軌', 'B1', ['r', 'y']), ('GB', '公設軌', None, ['p'])]　期 [('GA', '建地軌', 'B1', ['r', 'y']), ('GB', '公設軌', None, ['p'])]
  ✅ S3 待同歸戶併入（兼有配地者之共同負擔用地）：得 [('GC', ['s'], ['B2'])]　期 [('GC', ['s'], ['B2'])]
  ✅ S4 盤點之和 ＝ 全部：得 (400.0, 400.0)　期 (400.0, 400.0)
  ✅ S5 原街廓 ＝ 應分配面積較大者（⛔ 原有面積）：得 'B2'　期 'B2'
  ✅ S6 應分配面積並列 ⇒ 重劃前面積較大者：得 'B1'　期 'B1'
  ✅ S7 入池之合併單元 ⇒ 成員皆不能分配、其 G 只計一次：得 ({'m1': '建築街廓內不能分配', 'm2': '建築街廓內不能分配', 'k1': '原位次配地'}, {'B1': 40.0})　期 ({'m1': '建築街廓內不能分配', 'm2': '建築街廓內不能分配', 'k1': '原位次配地'}, {'B1': 40.0})
  ✅ S8 留置之合併單元 ⇒ 成員皆配地：得 {'m1': '原位次配地', 'm2': '原位次配地', 'k1': '原位次配地'}　期 {'m1': '原位次配地', 'm2': '原位次配地', 'k1': '原位次配地'}
  ✅ S9 段三所併出者 ⇒ 配地（配地街廓 ＝ 受併宗之街廓）：得 [('c', '原位次配地', ['B1']), ('q', '原位次配地', ['B1'])]　期 [('c', '原位次配地', ['B1']), ('q', '原位次配地', ['B1'])]
  ✅ S10 段三之受併宗未配地 ⇒ loud：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S11 殘料（可重名·a＝0）⇒ 另類、⛔ 入單位：得 ([2, 0.0], 2)　期 ([2, 0.0], 2)
  ✅ S12 殘料之原有面積 > 0 ⇒ loud：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S13 build 之宗既非配地亦非不配地 ⇒ loud：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S14 G 值列之未知推進側別 ⇒ loud：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S15 非共同負擔之街廓上之切片 ⇒ loud（【未裁】）：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S16 無歸戶之切片 ⇒ loud：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S17 不配地紀錄之街廓與切片不同 ⇒ loud：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S18 兼有配地與不能分配者 ⇒ 建地軌（其共同負擔用地入單位）：得 [('GA', '建地軌', ['B1'])]　期 [('GA', '建地軌', ['B1'])]
  ✅ R1 顯示列各欄皆字串：得 True　期 True
  ✅ R2 顯示之總句：得 ['合併單位 2（建地軌 1·公設軌 1）；待同歸戶併入之歸戶 1']　期 ['合併單位 2（建地軌 1·公設軌 1）；待同歸戶併入之歸戶 1']
── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──
  ✅ M0 未突變之抽出版：紅 []（期 []）
  ✅ M1 原街廓改以原有面積比：轉紅 ['S5 原街廓 ＝ 應分配面積較大者（⛔ 原有面積）', 'S7 入池之合併單元 ⇒ 成員皆不能分配、其 G 只計一次']
  ✅ M2 兼有配地者⛔ 成單位：轉紅 ['S1 逐切片之類', 'S2 合併單位（歸戶·軌·原街廓·成員）', 'S3 待同歸戶併入（兼有配地者之共同負擔用地）', 'S11 殘料（可重名·a＝0）⇒ 另類、⛔ 入單位', 'S18 兼有配地與不能分配者 ⇒ 建地軌（其共同負擔用地入單位）', 'R2 顯示之總句']
  ✅ M3 段三所併出者當共同負擔：轉紅 ['S9 段三所併出者 ⇒ 配地（配地街廓 ＝ 受併宗之街廓）', 'S10 段三之受併宗未配地 ⇒ loud']
⇒ 紅 []；rc 0
````

### `#32` `python3 verify/probes/probe_WG9351_intake.py wiring <repo>`（`rc 0`·`stderr` `0` B·`204` s）

````
── 接線（AST·app.py ＋ 生產碼他檔 33 檔）──
  ✅ W1 模組層之 ADJ 常數與二函式、二鍵之值、二函式內⛔ 案件字面（案件字面 []）
  ✅ W2a 入池閘之畫面入口於復原之後寫 SS_ADJ_DROPPED ＝ 末趟之不配地紀錄（_last[1]）
  ✅ W2b 配地本體於入池閘之後去 SS_ADJ_BUILD_FINAL（⛔ 去 SS_ADJ_DROPPED）
  ✅ W2c 配地本體於 _k929_6_log 非 None 時寫 SS_ADJ_BUILD_FINAL ＝ build_parcels
  ✅ W3 二鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log
  ✅ W4 消費端：生產碼他檔（33 檔）命中 0；app.py 只在許可之函式內（他檔 {}；app.py 非許可函式 []）
  ✅ W5 畫面路徑之合成案：main() 之盤點區塊以假 st 實際執行（不符 []）
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 配地本體⛔ 寫 build：轉紅 ['W2c']
  ✅ N2 入池閘之畫面入口寫空之紀錄：轉紅 ['W2a']
  ✅ N3 注入 harness 消費者：轉紅 ['W4']
  ✅ N4 單位表只出首列：轉紅 ['W5']
⇒ 紅 []；rc 0
````

### `#33` `python3 verify/probes/probe_WG9351_intake.py run <repo>`（`rc 0`·`stderr` `0` B·`273` s）

````
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
  合併單位 17（建地軌 9·公設軌 8）；待同歸戶併入之歸戶 0
     原位次配地：74 片·26324.86 ㎡
     建築街廓內不能分配：13 片·1432.13 ㎡
     共同負擔用地·入合併單位：31 片·7103.74 ㎡
     共同負擔用地·待同歸戶併入：0 片·0.00 ㎡
     無地號之殘料：8 片·0.00 ㎡
     合計：126 片·34860.73 ㎡
     單位 G003｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-17(1)〔G1·583.00〕、717(1)〔G1·246.00〕、715(1)〔G1·114.00〕、628-16(1)〔G1·558.43〕、628-16(2)〔RD4·24.57〕、628-14(1)〔G1·52.00〕、628-13(1)〔G1·72.52〕、628-13(2)〔RD4·31.48〕、628-12(1)〔G1·144.61〕、628-12(2)〔RD4·22.19〕、628-12(3)〔RD3·33.20〕｜合 1882.00｜配 —
     單位 G004｜建地軌｜原街廓 R2｜據 R2 71.59｜建 628-52(1)〔R2·119.66〕｜公 628-52(2)〔RD1·126.34〕｜合 246.00｜配 —
     單位 G011｜建地軌｜原街廓 R3｜據 R2 3.81、R3 92.46｜建 628-42(1)〔R2·8.34〕、628-42(2)〔R3·153.46〕｜公 628-42(3)〔G1·158.31〕、628-42(4)〔RD4·449.89〕｜合 770.00｜配 —
     單位 G012｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-5(1)〔G1·191.95〕、628-5(2)〔RD3·69.05〕｜合 261.00｜配 —
     單位 G013｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-6(1)〔G1·36.00〕｜合 36.00｜配 —
     單位 G014｜建地軌｜原街廓 R3｜據 R3 135.94｜建 628-28(1)〔R3·114.00〕、628-29(1)〔R3·114.00〕｜公 —｜合 228.00｜配 —
     單位 G015｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-15(1)〔G1·203.00〕｜合 203.00｜配 —
     單位 G016｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 718(1)〔G1·842.55〕、719(1)〔G1·1200.00〕、713(1)〔G1·29.00〕｜合 2071.55｜配 —
     單位 G018｜建地軌｜原街廓 R2｜據 R2 146.58｜建 628-51(1)〔R2·245.00〕｜公 —｜合 245.00｜配 —
     單位 G020｜建地軌｜原街廓 R2｜據 R2 147.18｜建 628-50(1)〔R2·246.00〕｜公 —｜合 246.00｜配 —
     單位 G024｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-26(1)〔G1·12.32〕｜合 12.32｜配 —
     單位 G025｜建地軌｜原街廓 R5｜據 R5 0.99、R6 0.26｜建 628-53(1)〔R6·0.44〕、628-53(2)〔R5·2.78〕｜公 628-24(1)〔G1·621.00〕、628-53(3)〔G1·300.44〕、628-53(4)〔RD4·229.34〕｜合 1154.00｜配 —
     單位 G028｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-2(1)〔RD3·52.00〕｜合 52.00｜配 —
     單位 G030｜建地軌｜原街廓 R3｜據 R2 27.55、R3 28.34｜建 628-27(1)〔R2·51.32〕、628-27(2)〔R3·46.68〕｜公 —｜合 98.00｜配 —
     單位 G031｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-25(1)〔G1·207.00〕｜合 207.00｜配 —
     單位 G032｜建地軌｜原街廓 R6｜據 R6 117.74｜建 628-38(1)〔R6·205.60〕｜公 628-38(2)〔G1·41.96〕、628-38(3)〔RD4·322.23〕、628-38(4)〔RD3·8.21〕｜合 578.00｜配 —
     單位 G033｜建地軌｜原街廓 R3｜據 R3 72.78｜建 628-46(1)〔R3·124.85〕｜公 628-46(2)〔RD2·121.15〕｜合 246.00｜配 —
  ✅ R2 逐切片之類（118 片）與外部錨相同：相異 []
  ✅ R3 合併單位（17）與外部錨相同：相異 []
  ✅ R4 逐類之和 ＝ 全部：126／126 片；34860.7300／34860.7300 ㎡
  ✅ R5 入池宗（不配地單元之成員）13 宗·1432.13 ㎡ ＝ 類「建築街廓內不能分配」13 片·1432.13 ㎡
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
  合併單位 17（建地軌 9·公設軌 8）；待同歸戶併入之歸戶 0
     原位次配地：74 片·26324.86 ㎡
     建築街廓內不能分配：13 片·1432.13 ㎡
     共同負擔用地·入合併單位：31 片·7103.74 ㎡
     共同負擔用地·待同歸戶併入：0 片·0.00 ㎡
     無地號之殘料：8 片·0.00 ㎡
     合計：126 片·34860.73 ㎡
     單位 G003｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-17(1)〔G1·583.00〕、717(1)〔G1·246.00〕、715(1)〔G1·114.00〕、628-16(1)〔G1·558.43〕、628-16(2)〔RD4·24.57〕、628-14(1)〔G1·52.00〕、628-13(1)〔G1·72.52〕、628-13(2)〔RD4·31.48〕、628-12(1)〔G1·144.61〕、628-12(2)〔RD4·22.19〕、628-12(3)〔RD3·33.20〕｜合 1882.00｜配 —
     單位 G004｜建地軌｜原街廓 R2｜據 R2 71.59｜建 628-52(1)〔R2·119.66〕｜公 628-52(2)〔RD1·126.34〕｜合 246.00｜配 —
     單位 G011｜建地軌｜原街廓 R3｜據 R2 3.81、R3 88.63｜建 628-42(1)〔R2·8.34〕、628-42(2)〔R3·153.46〕｜公 628-42(3)〔G1·158.31〕、628-42(4)〔RD4·449.89〕｜合 770.00｜配 —
     單位 G012｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-5(1)〔G1·191.95〕、628-5(2)〔RD3·69.05〕｜合 261.00｜配 —
     單位 G013｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-6(1)〔G1·36.00〕｜合 36.00｜配 —
     單位 G014｜建地軌｜原街廓 R3｜據 R3 130.42｜建 628-28(1)〔R3·114.00〕、628-29(1)〔R3·114.00〕｜公 —｜合 228.00｜配 —
     單位 G015｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-15(1)〔G1·203.00〕｜合 203.00｜配 —
     單位 G016｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 718(1)〔G1·842.55〕、719(1)〔G1·1200.00〕、713(1)〔G1·29.00〕｜合 2071.55｜配 —
     單位 G018｜建地軌｜原街廓 R2｜據 R2 146.58｜建 628-51(1)〔R2·245.00〕｜公 —｜合 245.00｜配 —
     單位 G020｜建地軌｜原街廓 R2｜據 R2 147.18｜建 628-50(1)〔R2·246.00〕｜公 —｜合 246.00｜配 —
     單位 G024｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-26(1)〔G1·12.32〕｜合 12.32｜配 —
     單位 G025｜建地軌｜原街廓 R5｜據 R5 0.99、R6 0.26｜建 628-53(1)〔R6·0.44〕、628-53(2)〔R5·2.78〕｜公 628-24(1)〔G1·621.00〕、628-53(3)〔G1·300.44〕、628-53(4)〔RD4·229.34〕｜合 1154.00｜配 —
     單位 G028｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-2(1)〔RD3·52.00〕｜合 52.00｜配 —
     單位 G030｜建地軌｜原街廓 R2｜據 R2 27.55、R3 24.88｜建 628-27(1)〔R2·51.32〕、628-27(2)〔R3·46.68〕｜公 —｜合 98.00｜配 —
     單位 G031｜公設軌｜原街廓 —（無建築街廓內土地）｜據 —｜建 —｜公 628-25(1)〔G1·207.00〕｜合 207.00｜配 —
     單位 G032｜建地軌｜原街廓 R6｜據 R6 117.74｜建 628-38(1)〔R6·205.60〕｜公 628-38(2)〔G1·41.96〕、628-38(3)〔RD4·322.23〕、628-38(4)〔RD3·8.21〕｜合 578.00｜配 —
     單位 G033｜建地軌｜原街廓 R3｜據 R3 72.78｜建 628-46(1)〔R3·124.85〕｜公 628-46(2)〔RD2·121.15〕｜合 246.00｜配 —
  ✅ R2 逐切片之類（118 片）與外部錨相同：相異 []
  ✅ R3 合併單位（17）與外部錨相同：相異 []
  ✅ R4 逐類之和 ＝ 全部：126／126 片；34860.7300／34860.7300 ㎡
  ✅ R5 入池宗（不配地單元之成員）13 宗·1432.13 ㎡ ＝ 類「建築街廓內不能分配」13 片·1432.13 ㎡
⇒ 紅 []；rc 0
````

### `#62` `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`（`rc 0`·`stderr` `0` B·`3` s）

````
── 合成對照（AST 抽出之 adj_intake 等）──
  ✅ K1 G 之加總較大者：得 'B2'　期 'B2'
  ✅ K2 G 相同 ⇒ 重劃前面積之合計較大者：得 'B1'　期 'B1'
  ✅ K3 G 以 0.01 ㎡ 為單位相同 ⇒ 重劃前面積：得 'B2'　期 'B2'
  ✅ K4 G 以 0.01 ㎡ 為單位相異 ⇒ G：得 'B1'　期 'B1'
  ✅ K5 G、重劃前面積皆同 ⇒ 最小之暫編地號較小者：得 'B1'　期 'B1'
  ✅ K6 G 逐街廓加總（⛔ 逐筆）：得 'B1'　期 'B1'
  ✅ K7 合併單元之 G 只計一次：得 'B2'　期 'B2'
  ✅ K8 合併單元之重劃前面積計其諸成員：得 'B1'　期 'B1'
  ✅ K9 重劃前面積 ＝ 原有面積（部分併出之剩下·⛔ 分攤登記面積）：得 'B2'　期 'B2'
  ✅ K10 三街廓：二者並列 ⇒ 其後之鍵：得 'B3'　期 'B3'
  ✅ K11 皆同 ⇒ ⛔ 停機：得 True　期 True
  ✅ K12 原街廓之據 ＝ 各街廓之 G 之加總：得 {'B1': 35.0, 'B2': 30.0}　期 {'B1': 35.0, 'B2': 30.0}
  ✅ K13 暫編地號以字典序比：得 'B1'　期 'B1'
  ✅ K14 單一街廓：得 'B2'　期 'B2'
  ✅ K15 街廓內之最小之暫編地號亦以字典序：得 'B1'　期 'B1'
  ✅ K16 重劃前面積先加後捨：得 'B1'　期 'B1'
  ✅ K17 重劃前面積以 0.01 ㎡ 為單位相同 ⇒ 暫編地號：得 'B2'　期 'B2'
  ✅ K18 重劃前面積 ＝ 原有面積（入池閘之帳之剩下）：得 'B2'　期 'B2'
⇒ 紅 []；rc 0
````

### `#63` `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`（`rc 0`·`stderr` `0` B·`3` s）

````
  ✅ X1 adj_intake 呼叫 k967_rank（呼叫 1）
  ✅ X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise（[]）
  ✅ X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since']／去 []／相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'adj_intake', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out']）
  ✅ X4 adj_intake 內⛔ 案件字面（[]）
  ✅ X5 生產碼 app.py 以外之 33 檔對基準相異 0（相異 []）
⇒ 紅 []；rc 0
````

### `#64` `python3 verify/probes/probe_WG9387_k961h.py run <repo>`（`rc 0`·`stderr` `0` B·`279` s）

````
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.81、R3 92.46｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R3｜據 R2 27.55、R3 28.34｜外部錨 R3
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.81、R3 88.63｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R2｜據 R2 27.55、R3 24.88｜外部錨 R2
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
⇒ 紅 []；rc 0
````

### `#65` `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1` s）

````
── selftest（合成·K-9-61 ①②③⑥）──
  ✅ K1 二受併宗皆與道路片相鄰 ⇒ 應分配面積大者（D1 ⇒ A1）
  ✅ K2 道路片唯與其一相鄰 ⇒ 該宗（D2 ⇒ A2·縱 G 140 ＜ 160）
  ✅ K3 應分配面積以 0.01 ㎡ 相同 ⇒ 重劃前面積大者（D1 ⇒ A2）
  ✅ K4 再同 ⇒ 暫編地號小者（D1 ⇒ A1）
  ✅ K5 無本段受併宗之街廓之原位次配得之宗二以上 ⇒ 相鄰者先 → G（D1 ⇒ A1／S2；D3 ⇒ S3）
  ✅ K6 有受併宗之街廓內另有原位次配得之宗 ⇒ 照配、與 D2 相鄰而承受之（D1 ⇒ A1·D2 ⇒ K）
  ✅ K7 所鄰之配得街廓二 ⇒ 承受之宗之 G 大之一側（X ⇒ C1·170 ＞ 160）
  ✅ K8 二側之 G 以 0.01 ㎡ 相同 ⇒ 重劃前面積大之一側（X ⇒ C1）
  ✅ K9 所鄰二以上而其一為本街廓 ⇒ 本街廓之宗（X ⇒ X9）
  ✅ K10 所鄰為零而經同一地主之道路片臨道路另一側之配得街廓 ⇒ 併入該側之宗（Y、D1 ⇒ A1）
  ✅ K11 所鄰為零而無同一地主之道路片相鄰 ⇒ 第 5 項之輪（Y ⇒ A1）
  ✅ K12 所鄰為零而本街廓另有已配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Z）
  ✅ K13 二受併宗之一於現態未保留 ⇒ 停機（④ 另單）
  ✅ K14 公設片平分，每街廓之一份由擇定之一宗整份承受（P ⇒ A1／S3）
  ✅ K15 承受之宗唯一者⛔ 須 G
  ✅ K16 須擇而 alloc_state 未回 G ⇒ 停機
  ✅ K17 相鄰以宗連同其於本段整筆併入之片判之（P5 ⇒ A1）
  ✅ K18 經道路片而臨者隨該道路片之受者（Y、D1 ⇒ K；D9 ⇒ A1）
  ✅ K19 道路片之端所臨之街廓⛔ 為道路之另一側（Y ⇒ A1·⛔ E1）
  ✅ K20 本街廓有同一地主之他群之配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Q）
  ✅ K21 所鄰為零而依第 5 項者其來源量為整筆、整筆併出（A1 130·Y 出 build）
  ✅ K22 重劃前面積扣段三部分併出（D1 ⇒ A1）
  ✅ K23 重劃前面積扣同一試算之入池閘之帳（D1 ⇒ A1）
  ✅ K24 經道路片之判以該建地與道路片共邊為準（Y ⇒ 第 5 項；Y2 ⇒ A1）
  ✅ K25 已為街角之合併所併出之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ E1）
  ✅ K26 同一街廓經二道路片而其受者異 ⇒ `k967_rank`（Y ⇒ K）
  ✅ K27 經道路片而臨二側 ⇒ 各側以其經道路片之受者比（Y ⇒ F1）
  ✅ K28 穿越之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ A1；C ⇒ (c)）
  ✅ K29 近半、遠半皆臨之街廓（路衝）⛔ 為道路之另一側（Y ⇒ 第 5 項 ⇒ E1；D1 ⇒ (b) E1）
  ✅ K30 第 5 項之本街廓之同一地主之配得之宗二以上 ⇒ 應分配面積大者（Y ⇒ Q·⛔ 近之 Q2）
  ✅ K31 路衝之扣以道路片為單位（Y ⇒ 經 D5 ⇒ E2）
  ✅ P0 逐項擾動恰該項紅 31／31
⇒ 紅 []；rc 0
````

### `#66` `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`（`rc 0`·`stderr` `0` B·`2` s）

````
── 接線（工作樹之 app.py 對基準 fd88f64）──
  ✅ X1 四停機之字樣皆去（殘 []）、「於現態未保留」之停機仍在
  ✅ X2 `_recv_of(b, y)` 之形與其 5 呼叫皆二引數
  ✅ X3 頂層之相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'adj_intake', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X4 ⛔ 案件字面（[]）
  ✅ X5 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#69` `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`（`rc 0`·`stderr` `0` B·`2` s）

````
  ✅ K1 程式之停機：回 RuntimeError·登記全文（⛔ 截）
  ✅ K2 ⛔ 帶號 ⇒ 停機、⛔ 登記
  ✅ K3 號之邊界（前接英數或連字號者⛔ 號；無數字者⛔ 號）
  ✅ K4 新登記 零／一／二 ⇒ ⛔ 拋／拋其全文／拋其首者
  ✅ K5 巢狀之試算以長度分之
  ✅ K6 入池閘之併入後之試算立程式之停機 ⇒ 上拋
  ✅ K7 對照：配地中止（⛔ 帶號）⇒ 照舊為不過
  ✅ K8 基底（無停機）：X 依手冊併入街角第 1 宗 C
  ✅ K9 換名：K6／K7／K8 之果除名稱外同
  ✅ K10 鏡射：K6／K7／K8 之果除名稱外同
  ✅ K11 旋轉 37°·TWD97：K6／K7／K8 之果除名稱外同
  ✅ K12 鏡射 ＋ 旋轉 213°·TWD97·換名：K6／K7／K8 之果除名稱外同
  ✅ K13 末端塊合併再試之試算立程式之停機 ⇒ 上拋
  ✅ K14 對照：末端塊之試算之配地中止 ⇒ 照舊記試算中止
  ✅ K15 試算之前之登記⛔ 波及（K7 於 K1〜K5 之登記之後）
  ✅ K16 上拋之訊息為全文（號在 1500 字之後）
  ✅ P0 判式自驗 16／16
⇒ 紅 []；rc 0
````

### `#70` `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`（`rc 0`·`stderr` `0` B·`105` s）

````
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 10（基準之帶號 10）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since']／去 []／相異 ['adj_intake', 'end_block_merge_run', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'k6b_screen_callbacks', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out']／不合 []）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/selection_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
````

### `#71` `python3 verify/probes/probe_WG9389_trialstop.py run <repo>`（`rc 0`·`stderr` `0` B·`363` s）

````
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
````

## 附錄丙　`R-3` 之八處之改後之前後三列（`HEAD`·mark 之句與上拋之句各一段）

`app.py:10409`
```python
 10406                          _mp[_m][_q['r']] = float(_mp[_m].get(_q['r'], 0.0)) + _w
 10407                          _x['入池閘成員部分併出'] = _mp
 10408          _nb = [t for t in _nb if _pid(t) not in _R]
 10409          _m389 = k6_trial_mark()
 10410          try:
 10411              _aft = trial(_nb)
 10412          except RuntimeError as _e:
```
`app.py:10413`
```python
 10410          try:
 10411              _aft = trial(_nb)
 10412          except RuntimeError as _e:
 10413              k6_trial_raise_since(_m389, '入池閘·併入後之試算')
 10414              return None, '併入後配地中止：' + str(_e).partition('\n')[0][:200]
 10415          _why = _chk965(st['out'], _aft, _T, _R)
 10416          if _why:
```
`app.py:11763`
```python
 11760      🔧 `W-G.9-384`（`K-9-71`）：`blk5` ＝ 五級之街廓屬性之回呼（`k971_blk5`），逕傳予 `k6b_stage3_run`（其後處理之第 `5` 項之
 11761        建地之片之他街廓之候選依五級與深度再排·見其 docstring）。"""
 11762      _rec = {'退縮': setback, '標的': [], '皆未達': {}}
 11763      _m389 = k6_trial_mark()
 11764      try:
 11765          _ev = alloc_eval(temp_parcels, build_parcels) or {}
 11766      except RuntimeError as _e:
```
`app.py:11768`
```python
 11765          _ev = alloc_eval(temp_parcels, build_parcels) or {}
 11766      except RuntimeError as _e:
 11767          _rec['標的'] = None
 11768          k6_trial_raise_since(_m389, '末端塊合併再試·試算')
 11769          _rec['試算中止'] = str(_e).split("\n")[0][:300]
 11770          return temp_parcels, build_parcels, [], _rec
 11771      _tg = []
```
`app.py:22943`
```python
 22940          for _k_rb in K6B_SCREEN_READBACK_KEYS:
 22941              _ss.pop(_k_rb, None)
 22942          _ss.pop(SS_ADJ_BUILD_FINAL, None)   # 🆕 `W-G.9-373`（`K-9-67`）：入池閘之末態 build 由本次試算寫（⛔ 讀前一趟之殘值）
 22943          _m389 = k6_trial_mark()
 22944          try:
 22945              with _cl_s3.redirect_stdout(_io_s3.StringIO()):
 22946                  f3_screen_corner_pk_run(_px, **dict(pk_kwargs, temp_parcels=_t, build_parcels=_b))
```
`app.py:22959`
```python
 22956              _err = f"試算中止（st.stop）：{_px.msgs[-1:]}"
 22957          except RuntimeError as _e_as:
 22958              _err = str(_e_as).split("\n")[0][:300]
 22959          k6_trial_raise_since(_m389, '段三·畫面之試算')
 22960          _rows = [] if _err else list(_ss.get('f3_G_values') or [])
 22961          _kept, _bad, _G = {}, {}, {}
 22962          for _r in _rows:
```
`app.py:23131`
```python
 23128          _sst.pop(SS_ADJ_BUILD_FINAL, None)
 23129          _pxy = _K6BTrialSt(st)
 23130          _er = None
 23131          _m389 = k6_trial_mark()
 23132          try:
 23133              with _cl953s.redirect_stdout(_io953s.StringIO()):
 23134                  _sst[SS_END_BLOCK_MODE] = 'trial'
```
`app.py:23144`
```python
 23141              _er = f"試算中止（st.stop）：{_pxy.msgs[-1:]}"
 23142          except RuntimeError as _e953t:
 23143              _er = str(_e953t).split("\n")[0][:300]
 23144          k6_trial_raise_since(_m389, '手冊先行·畫面之試算')
 23145          _gr = [] if _er else list(_sst.get('f3_G_values') or [])
 23146          _summ = k953_alloc_summary(_gr, _cat953s, _frt953s)
 23147          _bfin = _sst.get(SS_ADJ_BUILD_FINAL)
```
`app.py:23232`
```python
 23229          _ssa.pop(SS_ADJ_BUILD_FINAL, None)
 23230          _pxy = _K6BTrialSt(st)
 23231          _er = None
 23232          _m389 = k6_trial_mark()
 23233          try:
 23234              with _cl_a4s.redirect_stdout(_io_a4s.StringIO()):
 23235                  _ssa[SS_END_BLOCK_MODE] = 'trial'
```
`app.py:23245`
```python
 23242              _er = f"試算中止（st.stop）：{_pxy.msgs[-1:]}"
 23243          except RuntimeError as _e_a4t:
 23244              _er = str(_e_a4t).split("\n")[0][:300]
 23245          k6_trial_raise_since(_m389, '第一趟·畫面之試算')
 23246          _gr = [] if _er else list(_ssa.get('f3_G_values') or [])
 23247          _bfin = _ssa.get(SS_ADJ_BUILD_FINAL)
 23248          _kp_a4s.update(g_rows=_gr, build=_bfin, temp=_tt, err=_er, dropped=_cp_a4s.deepcopy(K917_DROPPED),
```
`verify/selection_pipeline.py:735`
```python
   732          ns["K917_DROPPED"].clear()
   733          _err = None
   734          _bf373 = None   # 🆕 `W-G.9-373`（`K-9-67`）：入池閘之末態 build（保留宗之成員·run_step_g 拋出者⛔ 取）
   735          _m389 = ns["k6_trial_mark"]()
   736          with _cl.redirect_stdout(_io.StringIO()):
   737              _d, _s, _o, _w, _f = run_corner_pk(ns, fake_st, cb, cad, param_rows, _t, _b, setback,
   738                                                 snapshot=snapshot)
```
`verify/selection_pipeline.py:748`
```python
   745              except RuntimeError as _e:
   746                  _err = str(_e).split("\n")[0][:300]
   747                  _rows = (getattr(_e, "partial", None) or {}).get("g_rows") or []
   748          ns["k6_trial_raise_since"](_m389, '段三·harness 之試算')
   749          _kept, _bad, _G = {}, {}, {}
   750          for _r in _rows:
   751              _blk = _r.get("所屬街廓")
```
`verify/selection_pipeline.py:862`
```python
   859          ns["K917_DROPPED"].clear()
   860          ss[ns["SS_END_BLOCK_MODE"]] = 'trial'
   861          _errk, _rowsk, _finalk = None, [], None
   862          _m389 = ns["k6_trial_mark"]()
   863          with _clk.redirect_stdout(_iok.StringIO()):
   864              try:
   865                  _sgk = run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, _bk, winners, forced, setback,
```
`verify/selection_pipeline.py:871`
```python
   868                  _finalk = (_sgk.get("k929_6") or {}).get("build")
   869              except RuntimeError as _ek:
   870                  _errk = str(_ek).split("\n")[0][:300]
   871          ns["k6_trial_raise_since"](_m389, '手冊先行·harness 之試算')
   872          _sumk = ns["k953_alloc_summary"](_rowsk, _cat_k, _front_k)
   873          _memk, _unik = ns["k953_units_of"](_finalk if _finalk is not None else _bk)
   874          # 🔧 `W-G.9-378`（`GB-204`）：pool_out 與 members 取同一 build
```
`verify/selection_pipeline.py:929`
```python
   926          ns["K917_DROPPED"].clear()
   927          ss[ns["SS_END_BLOCK_MODE"]] = 'trial'
   928          _ea4, _rowsa4, _fina4 = None, [], None
   929          _m389 = ns["k6_trial_mark"]()
   930          with _cla4.redirect_stdout(_ioa4.StringIO()):
   931              try:
   932                  _sga4 = run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, _ba4, winners, forced, setback,
```
`verify/selection_pipeline.py:938`
```python
   935                  _fina4 = (_sga4.get("k929_6") or {}).get("build")
   936              except RuntimeError as _xa4:
   937                  _ea4 = str(_xa4).split("\n")[0][:300]
   938          ns["k6_trial_raise_since"](_m389, '第一趟·harness 之試算')
   939          _got_a4.update(g_rows=_rowsa4, build=_fina4, temp=_ta4, err=_ea4,
   940                         dropped=_cpa4.deepcopy(ns["K917_DROPPED"]), depth=ns["adj4_depth_of"](ss))
   941          return ns["adj4_trial_state"](ns["k953_alloc_summary"](_rowsa4, _cat_a4, _row_a4), _ea4,
```
