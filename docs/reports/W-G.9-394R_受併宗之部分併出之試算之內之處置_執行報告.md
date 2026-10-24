# `W-G.9-394R` 受併宗之部分併出之試算之內之處置——執行報告（補令二之續做·新側支 `verify/W-G.9-394-k9615`）

- 單：原單 `docs/orders/W-G.9-394_規格單.md`（`866f2d5` 入倉）＋ 補令一 `docs/orders/W-G.9-394_補令一.md`（`bf363f4` 入倉）＋ 補令二 `docs/orders/W-G.9-394_補令二.md`（`04d0757` 入倉）。
- 執行端 ＝ 雲端之排程「市地重劃·執行端」；施工樹 `/tmp/w`（完整複本）；`<O>` ＝ `/tmp/O`（倉外）；雲端 Linux `4` 核（`nproc` ＝ `4`）；Python `3.11.17`；`pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`；殼無 `WV_`；並行 `2`；effort ＝ `high`。
- 結果：工項零‴、二″、三″、四″ 皆成；**本案之配地⛔ 變**（`V-4″`〜`V-6″`）；主線 `wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`（⛔ 動）。
- 前趟之停機：原單之趟 ⇒ 停機款 `12`（`ops/queue` 之 `reports/W-G.9-394_規格單_回報.md`）；補令一之趟 ⇒ 停機款 `4″`（前置″ 項 `4` 之期與工項零″ 之入倉相牴·`ops/queue` 之 `reports/W-G.9-394_補令一_回報.md`·`自誤 640`）——補令二 `§三‴` 之代換 `D-3` 正之，本趟依之續做。

## ① 逐 `commit` 之 hash 與工項（`5d2a283..` 新側支·八筆·`--merges` 空）

| 工項 | `commit` | 首列 | 推送 |
|---|---|---|---|
| 原單工項零 | `866f2d5` | （原單之趟·⛔ 變） | 前趟 |
| 原單工項一 | `9e25177` | （原單之趟·⛔ 變） | 前趟 |
| 補令一工項零″ | `bf363f4` | （補令一之趟·⛔ 變） | 前趟 |
| 補令一工項一″ | `9a952c9` | （補令一之趟·⛔ 變） | 前趟 |
| 補令二工項零‴ | `04d075754add7bc88a9a3b6a34aa222e36bd1eb6` | `W-G.9-394 工項零‴：補令二原封入倉（新側支）⛔ 零生產碼` | `9a952c9..04d0757` |
| 工項二″ | `3f36450aa2c3330bffa7f13e9662dfdeee9307a0` | `W-G.9-394 工項二″：候選之試算中受併宗須部分併出（GB-205）⇒ 該候選不過（K-9-61 ⑤）·採用之配地照舊停機（原趟之碼之重施）🔴 生產碼（新側支）` | `04d0757..3f36450`（驗與審查皆符後） |
| 工項三″ | `94b1280` | `W-G.9-394 工項三″：K-9-61 ⑤ 與 GB-205 之試算之內之處置·候選之不過之後之 K-9-66 之讀法入典·自誤 638〜640·GB-205 之縮·待落地清單之更新（新側支）⛔ 零生產碼` | `3f36450..94b1280` |
| 工項四″ | （本檔所在之 `commit`） | `W-G.9-394 工項四″：執行報告入倉（新側支）⛔ 零生產碼` | — |

## ② 停機款之三值（款·期·實）

### 補令二 `§零-2‴`

| 款 | 期 | 實 |
|---|---|---|
| `1‴` | 主線 `5d2a283`、新側支 `9a952c9`、heads（濾後）`54`、樹淨、`anchor 637 636` `rc 0` 且四簿 ＝ 期、旗標 `[None×5]`、環境可匯入 | 皆合（四簿：自誤 `622`／`637`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`）⇒ ⛔ 成就 |
| `2‴` | 補令二 `SELF_SHA256` ＝ `c5f69236…`、bytes／`sha256` ＝ `STATE.json`（`28330`／`3efbbf13…`）、補令一 ＝ `91807`／`4daafece…`／`SELF` `7cce1d0f…`、入倉後之 blob 逐位同 | 皆合 ⇒ ⛔ 成就 |
| `3‴` | 塊 `E42` ＝ `2471` B／`6d167acd…`／`13` 列；`rep394.diff` 與八塊 ＝ 補令一 `§五″` 項 `2`〜`4` | 皆合（見 ④）⇒ ⛔ 成就 |
| `4‴` | 補令一之 `3″`〜`13″` 任一成就 | 皆⛔ 成就（下表） |

### 補令一 `§零-2″`（`1″`／`2″` 由 `1‴`／`2‴` 代之）

| 款 | 期 | 實 |
|---|---|---|
| `3″` | 塊與 `rep394.diff` 之 bytes／`sha256`／列數合；`git apply --check` 過；施後 blob ＝ `b39dfc45…`、`F38` ＝ `1a6f2b7c…`、四檔 ＝ `§五″` 項 `5`（自誤簿依 `D-8` ＝ `f7a54a01…`） | 皆合 ⇒ ⛔ 成就 |
| `4″` | 前置″（依 `D-3`）之任一期不符 | 皆合（③）⇒ ⛔ 成就 |
| `5″` | 規格有歧義而涉域上判斷 | 未見 ⇒ ⛔ 成就 |
| `6″` | `V-1″`〜`V-9″` 任一 ≠ 期；改器；配地改變 | 皆合；⛔ 改器；配地⛔ 變 ⇒ ⛔ 成就 |
| `7″` | 推送目標非新側支／`ops/queue`、被拒、須 `--force`、主線推進 | 皆快轉成功；主線 `5d2a283` ⛔ 動 ⇒ ⛔ 成就 |
| `8″` | 四檔之改前非嚴格前綴、尾 ≠ 塊（自誤簿 ＝ `E40`＋`E41`＋`E42`）、刪除欄 ≠ `0`、blob ≠ 期；`checkidx`／`gen_fa_index` ≠ 期 | 皆合 ⇒ ⛔ 成就 |
| `9″` | 收工閘任一 ≠ 期 | 收工閘於工項四″ 推後量之（實測值見 `ops/queue` 之回報·⛔ 自指） |
| `10″` | 執行端之「孰為正典」之判、改器／塊／命令 | 無 ⇒ ⛔ 成就 |
| `11″` | 新檔為 `check-ignore` 所命中 | 無（`rc 1`）⇒ ⛔ 成就 |
| `12″` | 審查之發現涉域上判斷或規格之漏載 | 無（⑥）⇒ ⛔ 成就 |
| `13″` | 存取被拒、寫入為分類器所拒 | 無 ⇒ ⛔ 成就 |

### 原單 `§零-2`（`1`〜`13`·依補令一之所定讀之）

| 款 | 期 | 實 |
|---|---|---|
| `1` | 開工態（原單之趟） | 前趟已過（原單之回報）；本趟之開工態由 `1‴` 代之 ⇒ 合 |
| `2` | 原單之 `SELF_SHA256` 與入倉之 blob | 倉內 `docs/orders/W-G.9-394_規格單.md` ＝ `ops/queue` 之 `orders/W-G.9-394_規格單.md`（`cmp` 同） |
| `3` | 塊 `Fy50`／`K41`／`P52`／`E40`／`G18` 之 bytes／`sha256`／列數 | `K41` `13280`／`2440cfd5…`／`62`；`P52` `3164`／`f7103308…`／`18`；`E40` `1381`／`ce34b2b8…`／`12`；`G18` `1436`／`817a345b…`／`9`（合）；`Fy50` 之 `3` 器之 blob ＝ 原單 `§五-1` 項 `5`（`V-3″`） |
| `4` | 前置之期 | 由 `4″`（`D-3`）代之 ⇒ 合 |
| `5` | 域上之歧義 | 未見 |
| `6` | `V-1`〜`V-9` | 由 `V-1″`〜`V-9″` 代之 ⇒ 合 |
| `7` | 推送 | 合（同 `7″`） |
| `8` | 工項三之四檔 | 由 `8″` 代之 ⇒ 合 |
| `9` | 收工閘 | 由 `9″` 代之 |
| `10` | 自裁、改塊器命令 | 無 |
| `11` | `check-ignore` | 無命中 |
| `12` | 審查之 WARNING | 原單之趟成就（W-1、W-2）⇒ 補令一塊 `K42` 定之；本趟之審查 ⇒ 無 |
| `13` | 存取 | 無 |

## ③ 前置″ 與驗之出艙

### 開場（`§零-0‴`）

- `git rev-parse origin/wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`；`origin/verify/W-G.9-394-k9615` ＝ `9a952c949c931286512b65e6539539cc1c245857`；heads（濾後）＝ `54`（全列存 `<O>/heads_before_394p2.txt`）；`git checkout --detach origin/verify/W-G.9-394-k9615` 後樹淨；`app.py` ＝ `d91f6ee81f25eed01551e60774f26105c3186c45` ＝ `git rev-parse 5d2a283:app.py`；旗標 ＝ `[None, None, None, None, None]`。
- 環境：初無 `shapely` ⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ 原單 `§零-0` 項 `5` 之釘回之命令逐字（`rc 0`）與 `pip uninstall -y tzdata`（`rc 0`）⇒ 匯入 `rc 0`。
- 版本之比對（前置″ (丙) 之前提）：主線之端 `5d2a283…` ＝ 基準之 sha；`Python 3.11.17` ＝ 基準；`pip freeze` 之 `sha256` `ae1438da…` ＝ 基準 ⇒ (丙) **沿用** `基準/5d2a2836617bc2aea57f0c7513e67d9b2313f7f7.md` 之 `73` 呼叫之值（⑨ 之表標「沿用基準」）。
- pre-flight（補令二）：🔴 `0`／🟡 `0`／ℹ️ `2`（`P-5` ✅ 相符·受詞 `28252` B；`P-3` `def main` ＝ `23812`-`31555`）＝ 補令二 `§五‴` 項 `5`。

### 前置″ 項 `4`（`D-3`·於工項零‴ 之端 `04d0757`）

（甲）`git -c core.quotepath=false diff --name-status 9e25177 9a952c9`（恰二列）：

```text
A	docs/orders/W-G.9-394_補令一.md
M	verify/probes/probe_WG9394_k9615.py
```

（乙）`git -c core.quotepath=false diff --name-status 9a952c9 HEAD`（恰一列）：

```text
A	docs/orders/W-G.9-394_補令二.md
```

二字樣：`git grep -c -F "W-G.9-394" -- app.py` ⇒ 無出艙·`rc 1`；`git grep -c -F "K-9-61 ⑤" -- app.py` ⇒ `app.py:5`·`rc 0`。皆合 `§五‴` 項 `4`。

### 前置″ (甲)(乙)（`14` 呼叫·於 `04d0757`·`<O>/pre/`）

皆合補令一 `§五″` 項 `8` 之「工項一″ 之端」之欄（`#85`／`#86` `rc 1` 如期·餘 `rc 0`·`stderr` 皆 `0` B·機械對拍 `14`／`14`）；`f8_pre_35.json` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、`f8_pre_00.json` ＝ `884e91714a79288406faa4def6518847de36de39`。逐列見 ⑨。

### 施（`R-0″`）

`git apply --check <O>/rep394.diff` ⇒ 過；`git apply`；`git hash-object app.py` ＝ `b39dfc4598f48d4fa829df2b92ed023707bcd285`（`1881442` B）；`python3 -m py_compile app.py` ⇒ 過；二進位複製為 `<O>/app_R0.py`。

### 驗（於 `3f36450`·⛔ 推前·`<O>/post/`·從頭整套·⛔ 沿用）

| # | 期 | 實 |
|---|---|---|
| `V-1″` | `8` 呼叫皆 `rc 0`、末列 ＝ 施後之列；`F38` 之 `T1`〜`T14`、`W1`〜`W8`、`R1@3.5`／`R2@3.5`／`R1@0.0`／`R2@0.0` 皆 ✅ | 合（全文見本檔末之附） |
| `V-2″` | 其餘 `73` 呼叫皆 `rc 0`、末列 ＝ 施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` | 合（機械對拍 `87`／`87` 不符 `0`；`#4` 之出艙含 `✅ P0 逐項擾動恰該項紅 75／75`） |
| `V-3″` | `Fy50` 之 `3` 器之 blob ＝ 原單 `§五-1` 項 `5`；`F38` ＝ `1a6f2b7c…`；`verify/probes/` 對 `9a952c9` 相異 `0` | `628c72a3…`、`be268e40…`、`c14e3e41…`、`1a6f2b7cefa32ac6476bc1d041ec29b3dd314647`；相異 `0` ⇒ 合 |
| `V-4″` | `F36 diff` 皆 `全比相異 0 項`（其前無項之列）；`cmp` 皆 `相異 0 項 ⇒ ✅ 同`；對照 `全比相異 44 項` | 3.5 m／0 m：`F36 diff` `rc 0`·出艙唯一列 `全比相異 0 項`；`cmp` `rc 0`·`相異 0 項 ⇒ ✅ 同`；對照 `rc 0`·`全比相異 44 項` ⇒ **本案之配地⛔ 變** |
| `V-5″` | `parity` 皆 `rc 0`·`⇒ rc 0（不符 0 項）`；以同一字樣代 `HEAD` 後逐位同；⛔ 代之對照 ⇒ 異 | 落檔二、`stdout` 二：代後同 `True`、⛔ 代同 `False`（各代 `1` 處：`04d0757…` ↔ `3f36450…`）⇒ 合 |
| `V-6″` | `F8` 之落檔前後逐位同 | 3.5 m `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`（二列同）、0 m `884e91714a79288406faa4def6518847de36de39`（二列同）⇒ 合 |
| `V-7″` | 生產碼 `34` 檔對 `9a952c9` 相異恰 `1`（`app.py` `+18`／`−4`）；`git diff --no-index <O>/app_R0.py <repo>/app.py` ⇒ `rc 0`；`verify/` 相異 `0`；頂層之名⛔ 增減、相異之節點恰四 | `18	4	app.py`（唯此）；`--no-index` 無出艙·`rc 0`；`verify/` 相異 `0`；AST：頂層節點 `417`／`417`、名之增 `[]`、減 `[]`、相異 `['end_block_merge_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run']` ⇒ 合 |
| `V-8″` | 「W-G.9-394」⇒ `6`；「K-9-61 ⑤」⇒ `7` | `app.py:6`、`app.py:7` ⇒ 合 |
| `V-9″` | `stderr` 合計 `0` B | `<O>/post/*.err` 合計 `0` B（`V-4″` 之五呼叫之 `stderr` 亦 `0` B）⇒ 合 |

`V-4″` 之全文：`F36 diff 35`／`00` ＝ `全比相異 0 項`（各一列）；`cmp 35`／`00` ＝ `相異 0 項 ⇒ ✅ 同`（各一列）。

## ④ 塊之實得與四檔之改前改後

| 塊 | B | `sha256` | 列 |
|---|---|---|---|
| `E42`（補令二） | `2471` | `6d167acdc927f472514cda8fd3a5a6a55d4fd4682753faf879fe0c944931b07b` | `13` |
| `Fy51` | `12081` | `8aba075f67d2760a13d166da546af0bc8c6c0e6334a52f6c3cc430f98ab83946` | `189` |
| `K42` | `10773` | `e67c21bd13d377d3ecb2f39f15c544655a8d31fa73751f2db1e7a875e6ab0373` | `41` |
| `P53` | `1965` | `ce5abdda50c70588741999e17ce488b3d353b9932b34ec8260311f039f87796e` | `15` |
| `E41` | `2361` | `4870fc7ae3f705a943b62915b55059e7dcec865ac36fb38298ec7cad0ff78bce` | `12` |
| `K41` | `13280` | `2440cfd55da323e684455a911feed56bfb4588d9fe6d8a58d150063f36ca2946` | `62` |
| `P52` | `3164` | `f710330890f8c552fe5201647e77cf3642302a3a6b5aee1eaa4fd6d3f38c6612` | `18` |
| `E40` | `1381` | `ce34b2b84d655acfaf152de538b6dbcd7c9812f9cb31faa12684b0f791199f83` | `12` |
| `G18` | `1436` | `817a345b238ce2171822659ac6738028f17b6b527ed85b661cb095ce38799508` | `9` |
| `CK` | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` |
| `GF` | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` |
| 回報之 ⑧ 之差異（`rep394.diff`） | `4614` | `82b505e634c6defbe7f87bbf4bdeeac1ff139d98f539005e9d1447870163e0d7` | `63` |

（回報 `reports/W-G.9-394_規格單_回報.md` ＝ `38607` B·`df29afec516b0b4229b5228a09c1feab5e9231b584154e7c8388e90e0cd0c0aa`。）

| 檔 | 改前 B | 改後 B | 所附（依序） | 改後 blob |
|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `949523` | `973576` | `K41`＋`K42` | `8aaf0433ebade3a3fa65a2fdb48457829771a3f3` |
| `docs/待落地清單.md` | `33635` | `38764` | `P52`＋`P53` | `87205e000bbcf573313689798f0755e8bba0615d` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1233430` | `1239643` | `E40`＋`E41`＋`E42` | `f7a54a014b7b986fdffa26e83dd2641fbf28617d` |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1067257` | `1068693` | `G18` | `2d1a44b0de499d0c7d6ada72510882deb8660272` |

四檔皆二進位末端追加（改前為改後之嚴格前綴·以程式斷言）；`numstat` ＝ `103`／`0`、`33`／`0`、`37`／`0`、`9`／`0`。

## ⑤ 推送之目標與推後之遠端分支之列

- 母體之式：`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`。
- 一切推送 ＝ `git push origin HEAD:verify/W-G.9-394-k9615`（快轉·⛔ `--force`）：`9a952c9..04d0757`（工項零‴·推後列數 `54`、主線 `5d2a283`）、`04d0757..3f36450`（工項二″）、`3f36450..94b1280`（工項三″）、工項四″（本檔）。推後之列數與逐列之比見收工閘 `5″`（`ops/queue` 之回報）。

## ⑥ 自捕與自解、唯讀獨立審查

### 自捕與自解

- 抽塊之腳本初稿之 f-string 含反斜線（Python 3.11 之語法錯）⇒ 改後重跑；無檔被寫（首趟於語法錯即止）。
- 量測之對拍腳本初稿之表之讀取越過「項 `8` 之表」之末而讀入他表 ⇒ 限於表內後重跑（`87`／`87`、`14`／`14` 不符 `0`）。
- 雲端之一程序之背景時限：長驗以 `setsid nohup` 起之、逐呼叫落檔（未遇中斷）。

### 唯讀獨立審查（一輪·`redistribution-reviewer`·⛔ 改檔·於拋棄式 worktree `/tmp/rv`〔`3f36450`〕與 `/tmp/rv0`〔`04d0757`〕·⛔ 觸施工樹）

- ①：`git diff --no-index <O>/app_R0.py /tmp/rv/app.py` 無出艙·`rc 0`；二樹之 `app.py` 之差之 hunk 與 `rep394.diff` 逐位同；`b39dfc45…`／`d91f6ee8…` 自算合 ⇒ 合。
- ②：`F38 selftest` 於 `/tmp/rv` `rc 0`·`24`／`24`；於 `/tmp/rv0` `rc 1`·紅之列逐字 ＝ 期（`T13b` 綠）。`T12`（題一 4 之 (ii)：`F1` `290` ＞ `200` 觸 ⇒ `_noaff` 回偽 ⇒ `_t14_357` ⇒ `k966_block_merge` 按比例 `50.00`·`F1` 之 `G` ＝ `200`）、`T12b`（`EPS12` 改 `0` ⇒ `49.99`／`199.99`·`1e-6` ⇒ `50.0`／`200.0`·其必要屬實）、`T13`（`20.00`·`G` `180`）、`T13b`（全併 `40`·`G` `200`）、`T13c`（`0`·`G` `160`）、`T14`（建地類全量 `60`、道路類按比例 `40.00`、餘 `60` 依 `K-9-51`）逐項重算皆合；所量之列之欄與 `k6b_stage3_run`／`k953_manual_run` 之紀錄之欄合。
- ③（`ast`）：`_noaff` 之呼叫端五 ＝ `15140`（`_ct_try`）、`15333`（`_ct_cross`·題一 4 之 (ii)）、`15561`（`_try373`）、`15747`（逐列之 ②）、`15971`（後處理之整批）；`k966_block_merge` 之呼叫端四 ＝ `10456`（入池閘）、`15579`（`_rnd373`）、`16826`（手冊先行）、`17422`（第一趟）——與補令一 `§一″` 項 `1` 及塊 `K42` 之二之甲乙丁合。`_chk953` 之他呼叫端 `16402`、`16858` 屬實（另見 `16806`）。
- ④ 獨立之合成之例（`K-9-50` 題二·`_ct_try` 之 ② 之併入以 `GB-205` 中止·替身之殼仿畫面之 `alloc_state`）：無觸發之對照 ⇒ 二樹逐列同；`A1` 端以 `GB-205` 中止 ⇒ 改前停機（「試算內之程式之停機…GB-205…」）、改後 `A1` 未成（檢核不過）而續行、`F1` 成；`GB-104` 之對照 ⇒ 二樹皆停機；鏡像（`F1` 端）⇒ 改前停機、改後 `F1` 不過、`A1` 成。與真實之差：`alloc_state`／`trial_winner` 為玩具、`GB-205` 以替身登記、未經 `f3_screen_*`。
- 禁改：頂層節點 `417`／`417`·名⛔ 增減·相異恰四；`main`、`k6_program_stop`、`k6_trial_mark`、`K6_PROGRAM_STOPS`、`K6_PROGRAM_STOP_RE`、`k929_6_fixpoint` ⛔ 變；`verify/` 相異 `0`；`F38 wiring /tmp/rv 5d2a283` `W1`〜`W8` ✅。
- **(A) 涉域上判斷或規格之漏載：無**（所見皆補令一 `§三-4″` 之已知之形：#1 題一 4 之 (i) 與末端塊之評選之試算照舊停機；#3 採用之配地中之 `GB-205` 照舊停機；#4之二 `F38` ⛔ 量 `_ct_try` 之 `GB-205`〔審查者之合成例補證之〕與 `15344`〜`15346` 之陳註）。**(B) 純實作之瑕：無。**
- (C) NOTE（記而⛔ 改）：C-1 審查者於二拋棄式樹生 `__pycache__`（`.gitignore` 內·樹淨）；C-2 `adopted=False` 之八處之殼略過 `GB-205` ⇒ 採用之配地之停機訊息之形變為「無從判定／現態配地中止：'<err 之前 300 字>'」（`GB-205` 之訊約 `150` 字·號仍在）；C-3 `R-2` 之判式以「任何新登記」計，依賴殼已先上拋非 `GB-205` 者；C-4 被吞之 `GB-205` 之登記留於 `K6_PROGRAM_STOPS`（`T12` 一趟後 `15` 筆），跨候選之 `adopted=True` 之 mark 之誤報目前不可達；C-5 以正規式判「帶 `GB-205`」，他號之訊內嵌其字樣者會被誤免（現有 `13` 處無此）；C-6 `T12` 之註「建地 A1(1) 全量（250）」之 `250` 為 `F1` 之 `G`（措辭易誤讀·數無誤）；C-7 合成例之題二之敗端「未成／檢核 通過」為既有之 `_ct_log` 之形。
- 處置：(A)(B) 皆無 ⇒ 停機款 `12″` ⛔ 成就；⛔ 改碼；推之。

## ⑦ 設計說明（`§三-5″`·原單 `§三-5`）

- `R-0″` 之 blob 之對證：`rep394.diff` 施於工項零‴ 之端（`app.py` ＝ `d91f6ee8…`）⇒ `b39dfc4598f48d4fa829df2b92ed023707bcd285` ＝ 補令一 `§五″` 項 `3`；`git diff 5d2a283 3f36450 -- app.py`（同目錄之 `.diff`）與 `rep394.diff` 之本體（首二列之後）逐位同。⛔ 改一字。
- 原單 `§三-5` 之各項（照實·原趟之回報 ⑦ 所載·本趟之碼與之逐位同）：`R-1`（`k6_trial_raise_since`·簽名 `(mark, where, *, adopted=False)`·`for _s394 in K6_PROGRAM_STOPS[int(mark):]`：`adopted` 或⛔ 合 `(?<![0-9A-Za-z\-])GB-205(?![0-9])` ⇒ `raise RuntimeError(f"🔴 [試算內之程式之停機·{where}] {_s394}")`；否則 `return None`）；`R-2`（`_noaff`：`_sb` 之後 `_m394 = k6_trial_mark()`；`_sa` 之後 `if (not _eb394) and _ea394 and len(K6_PROGRAM_STOPS) > _m394: return False`；其後之「無從判定」與 `_lost`／`bad_pools` 照舊）；`R-3`（`end_block_merge_run`：既有之 `k6_trial_raise_since(_m389, '末端塊合併再試·試算')` 之次增 `k6_trial_raise_since(_m389, '末端塊合併再試·現態之試算·W-G.9-394', adopted=True)`）；`R-4`（`k929_6_fixpoint` ⛔ 動）；`R-5`（`W-G.9-389` 之註之段之末增一列；新區域名 `_s394`、`_m394`、`_eb394`、`_ea394`、`_mk394`）；`R-6`（`k953_manual_run`：`_ok953 = _same953(_sim953(_cand_st))` 之前 `_mk394 = k6_trial_mark()`、之後 `k6_trial_raise_since(_mk394, f"{_hdr953} R-5 之取代之試算·W-G.9-394", adopted=True)`）。
- `k6_trial_raise_since` 之一切呼叫處（施後·原趟之回報 ⑦）：`app.py` `10418`（入池閘·併入後）、`11926`／`11927`（末端塊合併再試·現態·`adopted` 偽／真）、`16503`（手冊先行 R-5 之取代·`adopted=True`）、`23319`／`23504`／`23605`（畫面之殼·段三／手冊先行／第一趟）；`verify/selection_pipeline.py` `748`、`871`、`938`（harness 之殼·⛔ 動）。
- `alloc_state` 之中止（`err`）之讀處：原趟之回報 ⑥ 之窮查（判停機者：段三 `15090`、`15314`、`15630`、`15778`、`15834`；手冊先行 `16285`、`16294`、`16426`、`16725`、`16748`、`16883`；第一趟 `17199`、`17248`、`17285`、`17372`；畫面 `23617`；harness `949`。判不過者：`16297`、`16404`、`17252`、`15088`）；本趟之審查者以 `ast` 窮查之結論同（現態 `15630`、`15778`、`15834`、`16286`、`16427`、`16725`、`16748`、`16884`、`17200`、`23618`；併入前 `15090`、`16295`、`17249`；`adopted=True` `11927`、`16503`·皆停機）。
- `_noaff` 之呼叫端（`ast` 之 `Call`·五處）與 `k966_block_merge` 之呼叫端（四處）：見 ⑥ 之 ③（施後之列號）。
- `§三-3` 之自查：`V-7″` 之 AST（相異恰四·名⛔ 增減）；`#5`（`F23 wiring`）、`#6`（`F24 wiring`）於施後 ⇒ `rc 0`（字樣之錨）；`F33`／`F34`／`F37` 之 `wiring`（`#70`、`#73`、`#82`）⇒ `rc 0`；`F30 wiring`（`main` ⛔ 動）含於 `V-2″`。

## ⑧ `app.py` 之全文差異

同目錄之 `W-G.9-394R_受併宗之部分併出之試算之內之處置_差異.diff`（`git diff 5d2a283 3f36450 -- app.py`·`4614` B·`+18`／`−4`）。`V-7″` 之 `git diff --no-index /tmp/O/app_R0.py /tmp/w/app.py` 之出艙：**無**（`rc 0`）。

## ⑨ 工項三″ 之 `checkidx`、`gen_fa_index` 之出艙

- `python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md` ⇒ `rc 0`；出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（`cmp`）。

### `87` 呼叫之二態之表（`rc`／`stderr` B／末列·耗時 s；`<repo>` ＝ `/tmp/w`；「沿用基準」＝ 前置″ (丙)·`基準/5d2a2836617bc2aea57f0c7513e67d9b2313f7f7.md` 之值；重跑者無）

| # | 命令 | 工項零‴ 之端（前置″） | 施後（工項二″ `3f36450`·從頭實跑） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·160） | `0`／`0`／`⇒ 紅 []；rc 0`（111） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·442） | `0`／`0`／`⇒ 紅 []；rc 0`（363） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（33） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（34） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·44） | `0`／`0`／`⇒ 紅 []；rc 0`（34） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·17） | `0`／`0`／`⇒ 紅 []；rc 0`（14） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·293） | `0`／`0`／`⇒ 紅 []；rc 0`（211） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·86） | `0`／`0`／`⇒ 紅 []；rc 0`（60） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·576） | `0`／`0`／`⇒ 紅 []；rc 0`（391） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·821） | `0`／`0`／`⇒ 紅 []；rc 0`（528） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（**沿用基準**·9） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（**沿用基準**·84） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（67） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·499） | `0`／`0`／`⇒ 紅 []；rc 0`（326） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2233） | `0`／`0`／`⇒ 紅 []；rc 0`（1434） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·38） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·6） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（**沿用基準**·26） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（24） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·24） | `0`／`0`／`⇒ 紅 []；rc 0`（19） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·311） | `0`／`0`／`⇒ 紅 []；rc 0`（228） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·435） | `0`／`0`／`⇒ 紅 []；rc 0`（284） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·44） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·39） | `0`／`0`／`⇒ 紅 []；rc 0`（38） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·9） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·27） | `0`／`0`／`⇒ 紅 []；rc 0`（23） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·18） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·12） | `0`／`0`／`⇒ 紅 []；rc 0`（10） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·225） | `0`／`0`／`⇒ 紅 []；rc 0`（160） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·64） | `0`／`0`／`⇒ 紅 []；rc 0`（46） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1074） | `0`／`0`／`⇒ 紅 []；rc 0`（736） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·209） | `0`／`0`／`⇒ 紅 []；rc 0`（131） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·138） | `0`／`0`／`⇒ 紅 []；rc 0`（116） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·465） | `0`／`0`／`⇒ 紅 []；rc 0`（280） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（**沿用基準**·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（**沿用基準**·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（**沿用基準**·1） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（**沿用基準**·12） | `0`／`0`／`紅項 [] 器紅 0`（9） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·470） | `0`／`0`／`⇒ 紅 []；rc 0`（279） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（159） | `0`／`0`／`（JSON 之摘要列·略）`（165） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（113） | `0`／`0`／`（JSON 之摘要列·略）`（128） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（158） | `0`／`0`／`⇒ 紅 []；rc 0`（166） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（116） | `0`／`0`／`⇒ 紅 []；rc 0`（125） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（329） | `0`／`0`／`⇒ rc 0（不符 0 項）`（346） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（237） | `0`／`0`／`⇒ rc 0（不符 0 項）`（245） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·5） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·427） | `0`／`0`／`⇒ 紅 []；rc 0`（276） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1594） | `0`／`0`／`⇒ 紅 []；rc 0`（1000） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1570） | `0`／`0`／`⇒ 紅 []；rc 0`（967） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·168） | `0`／`0`／`⇒ 紅 []；rc 0`（116） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·574） | `0`／`0`／`⇒ 紅 []；rc 0`（373） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·433） | `0`／`0`／`⇒ 紅 []；rc 0`（283） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·36） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·833） | `0`／`0`／`⇒ 紅 []；rc 0`（571） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·9） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·423） | `0`／`0`／`⇒ 紅 []；rc 0`（275） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·419） | `0`／`0`／`⇒ 紅 []；rc 0`（278） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（**沿用基準**·429） | `0`／`0`／`⇒ 紅 []；rc 0`（280） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['T1', 'T1b', 'T1c', 'T2', 'T8', 'T9', 'T9d', 'T9e', 'T10', 'T11', 'T12', 'T12b', 'T13', 'T13c', 'T14']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W8']；rc 1`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（265） | `0`／`0`／`⇒ 紅 []；rc 0`（291） |

## ⑩ 各段耗時（UTC·並行 `2`）

| 段 | 時 | 耗 |
|---|---|---|
| 取佇列·接單·開場（環境之裝與釘回、錨、pre-flight、抽塊） | `05:05`〜`05:09` | 約 `4` 分 |
| 工項零‴（入倉·推） | `05:09` | — |
| 前置″ (甲)(乙) `14` 呼叫 | `05:10:04`〜`05:22:15` | 約 `12` 分（耗時之和 `1457` s） |
| 施 `R-0″`·`commit` | `05:22` | — |
| 驗 `87` 呼叫（從頭·⛔ 沿用） | `05:22:37`〜`07:03:23` | 約 `101` 分（耗時之和 `12088` s） |
| 唯讀獨立審查（與驗並行·另二拋棄式樹） | `05:25`〜`05:35` | 約 `9` 分 |
| `V-4″`〜`V-6″` 之對拍、推工項二″、工項三″ | `07:03`〜`07:10` | 約 `7` 分 |

## 附：`V-1″` 之 `8` 呼叫之全文（`<O>/post/<#>.out`·`stderr` 皆 `0` B）

### `#5`

````text
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（609）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
````

### `#6`

````text
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（611）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
````

### `#69`

````text
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

### `#73`

````text
── 接線（工作樹之 app.py 對基準 2aa6302）──
  ✅ X1 舊停機之字樣去之（殘 0）、還原之字樣去之（{'回原狀': 0, '還原後仍出現': 0}）、鎖定之查之字樣 3（期 ≥ 1）
  ✅ X2 頂層之相異 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'f3_screen_stepg_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X3 ⛔ 案件字面（[]）
  ✅ X4 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#82`

````text
  ✅ W1 end_block_side_geom 之 'gate': False 之回傳 0
  ✅ W2 _place_pool_parcels 之「_unfront 之判 ⇒ continue」0·引 END_BLOCK_UNFRONT_EPS True·寫死 1e-3 0
  ✅ W3 _end_region_R／end_block_band_width 之「frag_poly 空」之停機 []
  ✅ W4 end_block_apply 之 'gate' 之字面 0
  ✅ W5 頂層之名之增 []·減 []·相異之節點 ['_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_merge_run', 'end_block_side_geom', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run']
  ✅ W6 新增或改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
  ✅ W8 END_BLOCK_UNFRONT_EPS ＝ 0.001
  ✅ W9 end_block_apply 之 `raise k6_program_stop(…GB-207…)` 1（期 1）
⇒ 紅 []；rc 0
````

### `#85`

````text
  ✅ T1 新登記唯 GB-205 ⇒ None
  ✅ T1b 新登記唯 GB-205 而 adopted ⇒ 上拋 GB-205
  ✅ T1c adopted 而無新登記 ⇒ None
  ✅ T2 GB-205 繼以 GB-104 ⇒ 上拋 GB-104
  ✅ T3 GB-104 繼以 GB-205 ⇒ 上拋 GB-104
  ✅ T4 GB-2050 ⇒ 上拋
  ✅ T5 【未裁】⇒ 上拋
  ✅ T6 無新登記 ⇒ None
  ✅ T7 mark 之前之登記⛔ 計 ⇒ None
  ✅ T8 入池閘之 GB-205 於候選之試算之殼 ⇒ 中止之訊息含 GB-205·登記增一·殼⛔ 上拋
  ✅ T9 段三：A1(1) 之 ② 之併入後之試算以 GB-205 中止 ⇒ A1(1) 未成（不過）、B1(1) 成
  ✅ T9b 其中止為 GB-104 ⇒ 停機
  ✅ T9c 其中止無號 ⇒ 停機（無從判定·照舊）
  ✅ T9d 併入前之試算以 GB-205 中止 ⇒ 停機（無從判定）
  ✅ T9e 併入前、後之試算皆以 GB-205 中止 ⇒ 停機（無從判定·⛔ 判為不過）
  ✅ T10 末端塊合併再試之現態之試算以 GB-205 中止 ⇒ 停機
  ✅ T10b 其中止無號 ⇒ 記試算中止而回（照舊）
  ✅ T11 T9 之換名、鏡射、旋轉 37°、TWD97 ⇒ 同 T9
  ✅ T12 題一 4 之「連同其半併入已取得之一端」之試算以 GB-205 中止 ⇒ 不過 ⇒ K-9-66 按比例（⛔ 停機）
  ✅ T12b T12 之換名、鏡射、旋轉 37°、TWD97 ⇒ 同 T12
  ✅ T13 段三後處理 (b) 之道路片之併入以 GB-205 中止 ⇒ 不過 ⇒ K-9-66 按比例 20
  ✅ T13b 觸發 ＝ G ＞ 200（全併恰在門檻上）⇒ 全併 40
  ✅ T13c 觸發 ＝ G ＞ 160（任一格即觸）⇒ 未成
  ✅ T14 手冊先行之候選之併入後之試算以 GB-205 中止 ⇒ 不過 ⇒ K-9-66（＝ F27 K16 之形·⛔ 停機）
⇒ 紅 []；rc 0
````

### `#86`

````text
  ✅ W1 頂層之名之增 []·減 []·相異之節點 ['end_block_merge_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run']
  ✅ W2 k6_trial_raise_since 內之號之字面 ['GB-205']
  ✅ W3 _noaff 之二試算之間之 mark 與「新登記 ⇒ return False」（_noaff 有）
  ✅ W4 end_block_merge_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W8 k953_manual_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W5 k929_6_fixpoint 之 `raise k6_program_stop(…GB-205…)` 1（期 1）·對基準⛔ 變 True
  ✅ W6 所改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
⇒ 紅 []；rc 0
````

### `#87`

````text
  ✅ R1@3.5 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@3.5 受併宗 25·最後之配地⛔ 保留者 []
  ✅ R1@0.0 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@0.0 受併宗 26·最後之配地⛔ 保留者 []
⇒ 紅 []；rc 0
````
