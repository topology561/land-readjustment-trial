# `W-G.9-392R`　試算至穩定與取得之宗之自我檢查　執行報告（原單 ＋ 補令一 ＋ 補令二）

- 受單：`docs/orders/W-G.9-392_規格單.md`（原單）、`docs/orders/W-G.9-392_補令一.md`（補令一）、`docs/orders/W-G.9-392_補令二.md`（補令二·`26525` B·`sha256` `d442bc4f66fac771997990b0e3e656bff3fc6c1132eb131c9e73fd09c91205a0`·`SELF_SHA256`〔`P-5`〕`83eab58b8d50a348bc63c2ba816e5f8694ab5f4b7cd0aadc9fdf393076eeae8e`·皆合 `ops/queue` 之 `STATE.json`）。
- 執行端（雲端之排程「市地重劃·執行端」）；施工樹 ＝ `/tmp/w`（雲端完整複本）；`<O>` ＝ `/tmp/O392p2`（倉外）；`<repo>` ＝ `/tmp/w`；`nproc` ＝ `4`；並行 `2`；Python `3.11.17`；`effort=high`。
- 前趟之停機：原單 ⇒ 停機款 `12`（`ops/queue` 之 `reports/W-G.9-392_規格單_回報.md`）；補令一 ⇒ 停機款 `4″`（`ops/queue` 之 `reports/W-G.9-392_補令一_回報.md`·前置″ 項 `4` 之期漏計補令一之入倉·`自誤 636`）。本趟依補令二續自 `f12824f`。
- 🔒 主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（⛔ 動）；本批改本案之配地 ⇒ 側支保留、入主線待 KL 核。主 checkout 之同步由 KL 自行為之（README 第六節第 6 款）。

## ① 逐 `commit` 之 hash 與工項（側支 `verify/W-G.9-392-k980g`·皆快轉）

| 工項 | `commit` | 內容 |
|---|---|---|
| 原單工項零 | `c066161` | 原單入倉（前趟） |
| 原單工項一 | `c4666ab4c747058fbaad143009c3a4138b7396dc` | 塊 `Fy47` 之 `12` 器（前趟） |
| 補令一工項零″ | `31208b076709800329a63eaea0d47138c1a71680` | 補令一入倉（前趟） |
| 補令一工項一″ | `f12824f57b5576bc54260ee5e61965e149511937` | 塊 `Fy48` 之 `9` 器（前趟） |
| **補令二工項零‴** | `c0ec2a5d1eff117495d9b952e013a6d75f88df3f` | 補令二入倉（`git cat-file blob` 與來源 `cmp` 逐位同·`git status --porcelain --untracked-files=no` 唯此 `1` 檔） |
| **工項二″** | `d3d8f46e9a067ecb45e93374ec8bd0ce4cb68458` | `R-0″`（原趟之碼之重施）＋ `R-7″`：`app.py` `+79`／`−11`、`verify/stepg_pipeline.py` `+33`／`−0`（對 `c0ec2a5`）；施後 blob `app.py` ＝ `b4cee75a8d5bfc0564ef7c855eb1dc4463f56458`、`verify/stepg_pipeline.py` ＝ `0cd22fc9ad8a45dcde435c1af016b26a95e0bc6b` |
| **工項三″** | `43ea230cb9b9363af7e0f4500b53aac887de74f5` | 塊 `K38`＋`K39`、`P49`＋`P50`、`G16`、`E37`＋`E38` 之純末端追加 |
| **工項四″** | （本 `commit`） | 本報告與 `.diff` |

## ② 停機款之三值

### 補令二（`1‴`〜`4‴`）

| 款 | 期 | 實 |
|---|---|---|
| `1‴` | 主線 `56c77fd`、側支 `f12824f`、heads `52`、追蹤檔⛔ 變、`issuer_anchor 634 629` `rc 0` 與四簿之值、旗標 `[None×5]`、六模組可匯入 | 皆合：`56c77fd10f8c…`、`f12824f57b55…`、`52`（存 `<O>/heads_before_392p2.txt`）、空、`rc 0`（自誤 `619`／`634`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`）、`[None, None, None, None, None]`、安裝後 `rc 0` |
| `2‴` | 補令二之 `SELF_SHA256`、bytes／`sha256`；補令一 `95051` B／`1d9a2eae…`／`SELF_SHA256` `6f75b64a…`；入倉 blob ＝ 來源 | 皆合 |
| `3‴` | 塊 `E38` `2359` B·`0420c8ef…`·`13` 列；`<O>/rep392.diff` `15801` B·`72b1892b…`·`205` 列；塊 `Fy48`／`K39`／`E37`／`P50` ＝ 補令一 `§五″` 項 `2`／`4` | 皆合：`E38` `2359`／`0420c8ef5f916b5aee93a4c1884ba1581fff875486f747238308ddddffbe3c27`／`13`；`rep392.diff` `15801`／`72b1892b4829af83e6ef13e408b66c626bbeccb095047b5969b8c501b0409207`／`205`；`Fy48` `13929`／`111e365c…`／`200`；`K39` `8422`／`d7500302…`／`44`；`E37` `2731`／`36aa95b1…`／`13`；`P50` `2590`／`d1e27cc2…`／`17` |
| `4‴` | 補令一之 `3″`〜`13″`（代換後）皆⛔ 成就 | 皆⛔ 成就（下表） |

### 補令一（`1″`〜`13″`·`1″`／`2″` 由 `1‴`／`2‴` 代之）

| 款 | 實 |
|---|---|
| `3″` | 合：`R-0″` 之 `git apply --check` 過；施後 `f12af112e5bf3c80248bc8821624ae1e02b5fed1`／`0cd22fc9ad8a45dcde435c1af016b26a95e0bc6b` |
| `4″` | 合：前置″ (甲) `34`／(乙) `6` 呼叫皆合期；(丙) 沿用基準；`D-3` 之（甲）九列、（乙）一列與四字樣皆合（第 ③ 節） |
| `5″` | ⛔ 成就（規格無歧義；⛔ 改禁改） |
| `6″` | ⛔ 成就：`V-1″`〜`V-9″` 皆合；本案配地之改變 ＝ 原單 `§一` 項 `5` |
| `7″` | ⛔ 成就：推送之目標唯 `verify/W-G.9-392-k980g`（快轉）與 `ops/queue`；⛔ `--force`；主線⛔ 動 |
| `8″` | ⛔ 成就：四檔之改前皆為改後之嚴格前綴、刪除欄 `0`、其尾 ＝ 塊、blob ＝ 期；`checkidx`／`gen_fa_index` ＝ 期 |
| `9″` | 收工閘於回報（`ops/queue`）載之（自指⛔ 寫入本檔） |
| `10″` | ⛔ 成就（⛔ 改單、塊、器、命令一字） |
| `11″` | ⛔ 成就：補令二入倉檔之 `git check-ignore -v --no-index` ⇒ `rc 1` |
| `12″` | ⛔ 成就：唯讀獨立審查 (A) `0`（第 ⑥ 節） |
| `13″` | ⛔ 成就 |

### 原單（`1`〜`13`）

原單之款由補令一之款代之（補令一單首「原單之條依補令一之所定」）；前趟原單於停機款 `12` 停（其回報之路徑如上）、補令一於 `4″` 停。本趟其餘之款皆⛔ 成就。

## ③ 前置與驗之出艙

### 開場（`§零-0‴`）

- `pip`：初匯入 `rc 1`（`No module named 'shapely'`）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`<O>/pip_install_req.txt`·`rc 0`）⇒ 補令一 `§零-0″` 項 `5` 之釘回五列（`<O>/pip_pin.txt`·`rc 0`）、去 `tzdata`（`<O>/pip_uninstall_tzdata.txt`·`rc 0`）⇒ 六模組匯入 `rc 0`；`pip check` ⇒ `No broken requirements found.`
- 版本之比對：`Python 3.11.17` ＝ 基準；`pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ＝ 基準；主線之端 ＝ `56c77fd…` ＝ 基準之 sha ⇒ 前置″ (丙) **沿用** `基準/56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81.md` 之值（`40` 呼叫·⛔ 重跑）。
- pre-flight：補令二 ⇒ `rc 0`·🔴 `0`／🟡 `0`／ℹ️ `2`（`P-5` ✅ 受詞 `26447` B；`P-3` `def main` ＝ `23691`-`31434`）＝ `§五‴` 項 `5`；補令一（唯記錄）⇒ `rc 0`·🔴 `0`／🟡 `3`（`[P-4] :183`、`:298`、`:539` ＝ 具名豁免之三處）／ℹ️ `2`。

### 前置″ 項 `4`（`D-3`·於工項零‴ 之端 `c0ec2a5`）

（甲）`git -c core.quotepath=false diff --name-status 31208b0 f12824f`（`rc 0`·九列）：

```
M	verify/probes/probe_WG9363_k953.py
M	verify/probes/probe_WG9367_adj4.py
M	verify/probes/probe_WG9370_adj4mut.py
M	verify/probes/probe_WG9385_k974.py
M	verify/probes/probe_WG9387_k961h.py
M	verify/probes/probe_WG9388_k961s3.py
M	verify/probes/probe_WG9389_trialstop.py
M	verify/probes/probe_WG9390_k961r.py
M	verify/probes/probe_WG9392_k980g.py
```

（乙）`git -c core.quotepath=false diff --name-status f12824f HEAD`（`rc 0`·一列）：

```
A	docs/orders/W-G.9-392_補令二.md
```

四字樣 `git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py`：「GB-206」「k980_acq_check」「end_block_trial_G」「K980_G_TOL」⇒ 各無出艙、`rc 1`。

### 前置″ (甲)(乙)·驗 `V-1″`〜`V-2″` 與 `V-4″`〜`V-6″` 之 `80` 呼叫

全表見附錄一（前態實跑 `40`：(甲) `34` ＋ (乙) `6`·其餘 `40` ＝ 沿用基準；施後 `80` 實跑）。前態 `40` 呼叫之 `rc`／`stderr`／末列皆 ＝ 補令一 `§五″` 項 `8` 之「工項一″ 之端」之列（`#16`、`#17`、`#18`、`#46`、`#78`、`#79`、`#80` 之紅如期）；`f8_pre_35.json`／`f8_pre_00.json` ＝ `8be0160bc14dd92a5331f86eecc995cae0507376`／`6fb86647807f9744594071be25c522b6b506c230`。施後 `80` 呼叫皆 `rc 0`、末列皆 ＝ 「施後」之列、`stderr` 合計 `0` B。重跑 `0`（無逾時、無 `rc` ≠ 期）。

- `V-1″`：`F36 selftest` `G1`〜`G4`、`H1`〜`H5`、`E1`〜`E5`、`J1`〜`J3` ✅、`P0 判式自驗 17／17`；`F36 wiring` `W1`〜`W8` ✅（`W8` `_corner_first_lot_G 之 _solve_G_one 以 is_corner=True、w0_start=0.0（呼叫 1）`）；`F36 run` `R1@3.5`（自我檢查 `423` 次·異 `[]`）、`R2@3.5`、`R1@0.0`（`324` 次）、`R2@0.0` ✅。其 `34` 呼叫之 `stdout` 全文見附錄二。
- `V-2″`：`40` 呼叫皆 `rc 0`；`F23 selftest`（`#4`）之 `P0 逐項擾動恰該項紅 75／75`。
- `V-3″`：`Fy47` 之器中 `Fy48` 所⛔ 改之三（`probe_WG9361_k954.py` `b39c2b0e…`、`probe_WG9375_k965.py` `4d74ea35…`、`probe_WG9391_k980x.py` `d99f637c…`）＝ 原單 `§五-1` 項 `5`；`Fy48` 之 `9` 器 ＝ 補令一 `§五″` 項 `5`；`git diff --name-status f12824f HEAD -- verify/probes` ⇒ `0` 列。
- `V-4″`：`F36 diff`（`rc 0`·`stderr` `0` B）：

```
3.5 m：
  宗 R5·628-18(2)·left G(㎡) 268.33 → 268.34
  抵費地 R1-抵費地-1 面積 851.68 → 851.69
  抵費地 R3-抵費地 面積 1651.41 → 1651.4
  抵費地 R4-抵費地 面積 697.4 → 697.39
  抵費地 R5-抵費地 面積 1221.44 → 1221.45
  抵費地 R6-抵費地 面積 980.59 → 980.58
全比相異 6 項
0 m：
  抵費地 R1-抵費地-1 面積 851.67 → 851.69
  抵費地 R3-抵費地 面積 1651.41 → 1651.4
  抵費地 R4-抵費地 面積 697.4 → 697.39
  抵費地 R5-抵費地 面積 1221.47 → 1221.46
  抵費地 R6-抵費地 面積 980.59 → 980.58
全比相異 5 項
```

  ＝ 原單 `§一` 項 `5` 之逐字；對照組 `k6s3_pre_35` 對 `k6s3_pre_00` ⇒ `全比相異 45 項`。`k6s3 cmp` 二退縮皆 `rc 1`、末列 `相異 1 項 ⇒ 🔴 異`（其項 `R1-抵費地-1`：3.5 m `851.68` ≠ `851.69`；0 m `851.67` ≠ `851.69`）——**本案之配地之改變 ＝ 原單 `§一` 項 `5`**。
- `V-5″`：`parity` 二退縮皆 `rc 0`、末列 `⇒ rc 0（不符 0 項）`；以 `<HEAD>` 代二態之 `HEAD`（前態 `c0ec2a5…`、施後 `d3d8f46…`）之全值後，落檔（`8683`／`284` B）與 `stdout`（`1586`／`1584` B）前後皆 `cmp` 逐位同；對照（⛔ 代）⇒ 四者皆 `cmp rc 1`（唯落檔之 `"head"` 欄與 `stdout` 首列之「態」異）。
- `V-6″`：`F8 run` 二退縮 `rc 0`、`⇒ 紅 []；rc 0`；`git hash-object`：3.5 m `8be0160bc14dd92a5331f86eecc995cae0507376` → `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、0 m `6fb86647807f9744594071be25c522b6b506c230` → `884e91714a79288406faa4def6518847de36de39`；JSON 之逐欄比（`python3` 讀二檔、遞迴比其鍵與值·倉外之 `jdiff.py`）：3.5 m `/dropped/R2/left[0]/G(㎡)` `3.81` → `3.82`、`/rows[16]/G(㎡)` `268.33` → `268.34`（`相異之欄 2`）；0 m `/dropped/R2/left[0]/G(㎡)` `3.81` → `3.82`（`相異之欄 1`）。
- `V-7″`：生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對 `f12824f` 相異恰 `2`（`app.py`、`verify/stepg_pipeline.py`）；`verify/` 之一切檔相異唯 `verify/stepg_pipeline.py`；AST：`app.py` 增 `['K980_G_MAX_ITER', 'K980_G_TOL', 'end_block_trial_G', 'k980_acq_check']`、減 `[]`、相異之節點 `['_WF_NS_NAMES', '_corner_first_lot_G', '_solve_G_one', 'end_block_host', 'f3_screen_stepg_run']`；`verify/stepg_pipeline.py` 相異 `['_run_step_g_impl']`（增減 `[]`）；`git diff --no-index <O>/app_R0.py <repo>/app.py` ⇒ `rc 1`（全文見下）；`git diff --no-index <O>/stepg_R0.py <repo>/verify/stepg_pipeline.py` ⇒ `rc 0`。

```
diff --git a/tmp/O392p2/app_R0.py b/tmp/w/app.py
index f12af11..b4cee75 100644
--- a/tmp/O392p2/app_R0.py
+++ b/tmp/w/app.py
@@ -19874,7 +19874,8 @@ def _corner_first_lot_G(*, a_m2, A_ratio, B, C, l_front, l_side, F,
         blk_poly=block_poly, d_hat=_dh_use, baseline_pt=_bp,
         S_max=max(0.1, _s_max), is_corner=True, side=_side_cn, avg_depth=avg_depth,
         B=B, C=C, tab6_burden=tab6_burden,
-        allocation_dir=allocation_dir, side_mid=side_mid, W_prev=0.0)
+        allocation_dir=allocation_dir, side_mid=side_mid, W_prev=0.0,
+        w0_start=0.0)  # W-G.9-392 補令一（R-7″·K-9-41 ①）：評選之式之起算點 ＝ 0
     return float(_res.get('G', 0.0) or 0.0)
 
 
```

- `V-8″`（`git grep -c -F`）：「GB-206」`app.py:3`；「k980_acq_check」`app.py:6`、`verify/stepg_pipeline.py:4`；「end_block_trial_G」`app.py:7`、`verify/stepg_pipeline.py:2`；「K980_G_TOL」`app.py:3`（皆 ≥ 期）。
- `V-9″`：`V-1″`〜`V-6″` 之諸器之 `stderr` 合計 `0` B。

## ④ 塊之實得與四檔之改前改後

| 塊 | bytes | `sha256` | 列 |
|---|---|---|---|
| `K38`（原單·自倉內之原單抽之） | `10377` | `4221620f982d1cea9421d17fd0da27321b008b0c533172ca15681445da5a15df` | `61` |
| `P49`（同） | `2911` | `85d8def1d73db3c126ccb80d1aae4deeefb8a3f2b2db1961a6513f858abeb8e3` | `21` |
| `G16`（同） | `2019` | `f94b797c518d99da29d346b9236c3185e9399acb4fc92eba21e4d8a5371ac0c1` | `12` |
| `K39`（補令一） | `8422` | `d7500302458aa5d5249a0a58c2775c1fe3bbea1ac22a54228f38ca0838f90549` | `44` |
| `E37`（補令一） | `2731` | `36aa95b1e81c72ff49b9679a30f2aefc63bae590200517b48c4b746a6a97c25f` | `13` |
| `P50`（補令一） | `2590` | `d1e27cc218abb9863b24e0ddef23f02911d28a9afdfe53e8f3544838bff2bb79` | `17` |
| `E38`（補令二） | `2359` | `0420c8ef5f916b5aee93a4c1884ba1581fff875486f747238308ddddffbe3c27` | `13` |
| `CK`（`W-G.9-365` 附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` |
| `GF`（同附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` |

| 檔 | 改前 B | 改後 B | 改後 blob | `numstat` |
|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md`（＋`K38`＋`K39`） | `919452` | `938251` | `bb1f801424c698e392cfa5c289a14d509ac772d7` | `105`／`0` |
| `docs/待落地清單.md`（＋`P49`＋`P50`） | `23233` | `28734` | `0f71f2a4691bf2e7434a064f9d104cd58cdb6162` | `38`／`0` |
| `docs/reports/W-G.4_泛用阻塞項登記表.md`（＋`G16`） | `1063208` | `1065227` | `240317a7c1bac742607302bb987a031ca597d4a6` | `12`／`0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md`（＋`E37`＋`E38`） | `1225486` | `1230576` | `043851e0ea12bb1956d32836aff0edae306802bc` | `26`／`0` |

改前皆為改後之嚴格前綴（`head -c <改前 B>` 與改前 `cmp` 同）。

## ⑤ 推送之目標與推後之 heads

- 推送：`verify/W-G.9-392-k980g`：`f12824f` → `c0ec2a5`（工項零‴）→ `d3d8f46`（工項二″·驗與審查皆符後）→ `43ea230`（工項三″）→ 本 `commit`（工項四″）；皆快轉、⛔ `--force`。
- 工項零‴ 推後 `git ls-remote --heads origin` ＝ `52` 列；主線 ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`。工項四″ 推後之 heads 之全比載於 `ops/queue` 之回報（收工閘 `5″`）。

## ⑥ 自捕與自解；唯讀獨立審查

### 自捕與自解

1. `ops/queue` 之接單之推送一度被拒（發單端之門鈴之記錄 `f906eee` 同時入）⇒ 重取：`status` 仍 `pending`、單之 `sha256` 不變 ⇒ 以遠端為底重放（⛔ `--force`）。
2. **通則「Bash 命令⛔ 含 heredoc」之違（一次）**：接單時改 `STATE.json` 之助手腳本（倉外之暫存目錄·唯改 `ops/queue` 之 `STATE.json`）以 heredoc 寫之；其後之一切腳本與訊息檔皆以檔案寫入之工具為之；量測之命令皆⛔ 用 heredoc。
3. 補令二之複本置施工樹之根（`執行端.md` 丙 3）而以 `.git/info/exclude` 排除之（⛔ 入倉）。
4. 撰碼於另一複本（`/tmp/w2`·自 `/tmp/w` 本地 `clone`）以免擾前置之跑；前置畢後於施工樹 `git apply <O>/rep392.diff`（blob 合 `R-0″`）再以 `cp` 移入 `R-7″` 之 `app.py`（blob 同 `b4cee75a…`）、`py_compile`、`commit`。撰碼中之自查唯靜態（AST、字樣之錨之計數）·⛔ 跑量測器 ⇒ 並行恆 ≤ `2`。
5. 等待用之迴圈之 `pgrep -f` 之式自匹配其殼而⛔ 終（唯致逾時之通知·⛔ 涉量測）⇒ 改以 `[r]unner.py` 之式。
6. `V-5″` 之代換：初以 `f12824f` 為前態之 `HEAD` 代之而不合；前態之實 `HEAD` ＝ 工項零‴ 之端 `c0ec2a5`（前置″ 於其上跑）⇒ 以之代後逐位同（第 ③ 節）。

### 唯讀獨立審查（另派之唯讀 reviewer·⛔ 改檔·⛔ `commit`；前後 `git status --porcelain` 空、`HEAD` 皆 `d3d8f46`）

結論：**(A) `0`、(B) `0`、(C) `5`**。

- ① `git diff --no-index <O>/app_R0.py app.py` 唯一 hunk（`R-7″`）；`stepg` 與 `stepg_R0` 逐位同；`git diff c0ec2a5 d3d8f46` 之全文合 `R-1`〜`R-6`；審查者於倉外重施 `rep392.diff` 得 `f12af112…`／`0cd22fc9…`。
- ② 呼叫者：Step L `app.py:20958`（`_corner_block_true_G`）、harness `verify/selection_pipeline.py:441`（`run_corner_pk`）·二者經 `app.py:19905`／`19913`；自我檢查 `app.py:22137`／`22300`、`verify/stepg_pipeline.py:936`／`1085`。與實配之鏈首（`app.py:22098`／`22240`／`22260`、`verify/stepg_pipeline.py:902`／`1030`／`1049`）逐參數：`w0_start` 改後同（`0.0`）；`is_chain_head` 為無效之差（`solve_G_binary` 唯於 `is_corner or is_chain_head` 讀之·`is_corner=True` 兩邊皆真）；`near_dir`、`side_mid`、`allocation_dir`、`W_prev`、`l_side`／`F`、`s_back` 同；`baseline_pt`（右）與 `d_hat` 唯浮點末位；`S_max` 唯上界。
- ③ 獨立之合成之例（以 `verify/app_harvest.harvest` 分載改前、改後之真函式·依 `f3_screen_stepg_run` 之鏈首之引數逐行重建迷你之鏈）：例一 矩形 `48×23`、`δ ∈ {0, 0.001, 0.05, 0.3, −0.05}`·左右；例二 斜交 `78°`（旋轉 `33°`·TWD97 之量級）`δ` 同上、斜交 `97°`（旋轉 `−121°`）`δ ∈ {0, 0.05, 0.3}`——`13` 組皆幾何二分。**改後**：評選 ＝ 自我檢查之重算 ＝ 實配（取 2 位）皆同、`k980_acq_check` 皆過；**改前**：`δ ＞ 0` 之 `15` 側評選高於實配而皆觸 `GB-206`（例：矩形 `δ ＝ 0.001` 左 `168.92` 對 `168.91`；`δ ＝ 0.3` 右 `205.37` 對 `203.33`）；`δ ＝ 0`、`−0.05` 改前改後同；實配之值改前改後逐位同。
- ④ `k980_acq_check` → `k6_program_stop` 之上拋之路仍在（實測·改前改後皆然）；`k6_trial_mark`／`k6_trial_raise_since` 之 `8` 處⛔ 動；`§三-3` 六款皆合（字樣之錨：器之字串 `26715` 中於改前恰一而改後⛔ 恰一者 `0`；`main` AST 同；頂層之相異 ＝ `§三-3″`；新案件字面 `0`；簽名之變 `0`）。
- (A) 中遇之已知之形（唯記·⛔ 構成停機款 `12″`）：② 評選之式之幾何求解失敗 ⇒ `app.py:19770`〜`19773` 之 `K-9-41 ①` 停機（Step L 以 `st.error`＋`st.stop` 接之）；③ `δ ＜ 0` 同值；⑥／原單塊 `K38` 之 `65`（右鏈首宗之 `_adj` 之重解 ⇒ 自我檢查停機）；原單塊 `K38` 之甲（不動點恰在半分 `±1e-6` 內）。
- (C)：1. `_corner_first_lot_G` 之 docstring（`app.py:19823`）「solver 失敗走 `_solve_G_one` fallback（不 raise）」於改後不實（`R-7″` 禁改他處·已列待落地序 `26`）；`_solve_G_one` 之 docstring（`19722`〜`19723`）同類之舊述。2. `verify/test_corner_first_lot_G.py` 之 A-4 於改前（`app_R0`）改後皆 `rc 1`（`_first_corner_alloc_dir` 拋·`K-9-5-4` ② 以來之舊壞·⛔ 為本改所致·宜登記待查）。3. `is_chain_head` 之差為無效之差（規格之「⛔ 增 `is_chain_head`」成立）。4. `probe_WG971_wrap.py`、`probe_ruling_K4_s_origin.py`、`probe_WG921_b_slot_divergence.py` 三檔於 Python 3.11 ⛔ 能 `ast.parse`（f-string）⇒ 審查者之字樣之錨之自查未涵其常數（`R-7″` 唯增一列）。5. 缺 FRONT 時 `_sl392` 為 `None` ⇒ `_corner_first_lot_G` 之無號之 `RuntimeError`（原趟已記之 (C)·已知之形 ⑤）。
- 處置：(A)(B) 無 ⇒ ⛔ 修；(C) 唯記（⛔ 改·🛑）。

## ⑦ 設計說明（原單 `§三-5`·補令一 `§三-5″`）

- `R-0″`：`<O>/rep392.diff`（原趟之回報之附錄二）施於 `c0ec2a5`：`git apply --check` 過、施後 `app.py` ＝ `f12af112e5bf3c80248bc8821624ae1e02b5fed1`、`verify/stepg_pipeline.py` ＝ `0cd22fc9ad8a45dcde435c1af016b26a95e0bc6b`（＝ 補令一 `§五″` 項 `3`）；二進位複製為 `<O>/app_R0.py`、`<O>/stepg_R0.py`。
- `R-1`〜`R-6`（原趟之撰·照原趟之回報五；列號為改後）：`R-1` `app.py:13159`〜`13160`（`K980_G_TOL = 1e-6`、`K980_G_MAX_ITER = 200`）、`_solve_G_one` 之 `solve_G_binary(…)`（`app.py:19745` 附近）改傳 `tol=K980_G_TOL, max_iter=K980_G_MAX_ITER`；`R-2` `k980_acq_check`（`app.py:11688`）；`R-3` `end_block_trial_G`（`app.py:11701`）·`end_block_host` 之 `_trial` 委派之（`app.py:11757`）；`R-4` 四處 `app.py:22137`／`22144`（左）、`22300`／`22307`（右）、`verify/stepg_pipeline.py:936`／`943`（左）、`1085`／`1092`（右）·上界 `_sl392`／`_smr392` 每街廓算一次（`app.py:21945`、`verify/stepg_pipeline.py:821`·經 `ns["_oblique_s_max"]`）；`R-5` `_WF_NS_NAMES`（`app.py:20295`）增 `"k980_acq_check", "end_block_trial_G"`；`R-6` 新區域名皆帶 `392`、`R-3` 之側別之停機⛔ 帶號。評選之式之引數之源：Step L `app.py:20958`、`run_corner_pk` `verify/selection_pipeline.py:441`、`end_block_host` 之 `_trial`。
- `R-7″`：`app.py:19872`〜`19878` 之 `_corner_first_lot_G` 內唯一之 `_solve_G_one(…)` 之呼叫，其末之引數 `W_prev=0.0` 之後增 `w0_start=0.0`（字面之浮點常數·新之一列）並附行尾之註 `# W-G.9-392 補令一（R-7″·K-9-41 ①）：評選之式之起算點 ＝ 0`；他之引數一字⛔ 動（`is_corner=True`、`W_prev=0.0` 照舊·⛔ 增 `is_chain_head`）；`verify/stepg_pipeline.py` ⛔ 改（harness 經 `ns['_corner_first_lot_G']` 自隨）。對 `R-0″` 之碼 `+2`／`−1`。
- 呼叫處之全列（改後）：`_solve_G_one(` ＝ `app.py:19872`（`_corner_first_lot_G` 內）、`app.py:21550`（畫面之 `_solve_one` 之薄殼）、`verify/stepg_pipeline.py:556`（`ns["_solve_G_one"]`）；`_corner_first_lot_G(` ＝ `app.py:19905`、`19913`（`_corner_block_true_G` 內）、`app.py:22137`、`22300`、`verify/stepg_pipeline.py:936`、`1085`；其上游 ＝ `_corner_block_true_G`：`app.py:20958`（Step L）、`verify/selection_pipeline.py:441`（`run_corner_pk`）；`end_block_trial_G(` ＝ `app.py:11757`、`22144`、`22307`、`verify/stepg_pipeline.py:943`、`1092`。
- `§三-3″` 之自查：第 `1`／`2` 款——撰碼中以倉外之腳本計 `verify/probes/*.py` 之字串常數（長 ≥ `4`·`26715` 個）於 `<O>/app_R0.py` 與改後之 `app.py` 之計數：有變者 `8`（`'    '` 等空白之串、`'  # '`、`'W-G.9-'` `570` → `571`、`'w0_start'` `19` → `20`），其改前之計數皆 ≫ `1` ⇒ 「恰一」之錨⛔ 觸；`F23 wiring`（`#5`）、`F24 wiring`（`#6`）於施後之驗皆 `rc 0`；第 `3` 款 `main` ⛔ 動；第 `4` 款見 `V-7″`；第 `5` 款 `F36 wiring` `W7` ✅；第 `6` 款簽名⛔ 變。

## ⑧ 二檔之全文差異

同目錄之 `W-G.9-392R_試算至穩定與取得之宗之自我檢查_差異.diff`（`git diff 56c77fd d3d8f46 -- app.py verify/stepg_pipeline.py`·`215` 列·`16378` B）。

## ⑨ 工項三″ 之 `checkidx`、`gen_fa_index`

- `python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md` ⇒ `rc 0`；出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` `cmp` 逐位同。

## ⑩ 各段耗時（Asia/Taipei·並行 `2`）

| 段 | 時 | 耗時 |
|---|---|---|
| 接單、開場（環境之裝與釘回、四簿、塊之抽取、pre-flight）、工項零‴ | `17:22`〜`17:27` | ≈ `5` 分 |
| 前置″ (甲)(乙) `40` 呼叫（與撰碼並行·撰碼唯靜態之自查） | `17:27`〜`18:28` | ≈ `61` 分（耗時之和 `6317` s） |
| 施後之驗 `80` 呼叫 | `18:28`〜`21:01` | ≈ `153` 分（耗時之和 `18264` s） |
| `V-3″`〜`V-8″` 之比對 | `21:01`〜`21:03` | ≈ `2` 分 |
| 唯讀獨立審查 | `21:03`〜`21:14` | ≈ `11` 分 |
| 工項二″ 之推、工項三″、工項四″ | `21:14`〜 | — |

## 附錄一　`80` 呼叫之二態（`rc`／`stderr` B／末列·耗時 s；`<repo>` ＝ `/tmp/w`、`<O>` ＝ `/tmp/O392p2`；前態之「沿用基準」＝ 前置″ (丙)·其格 ＝ 補令一 `§五″` 項 `8` 之「工項一″ 之端」之列）

| # | 命令 | 前態（工項零‴ 之端） | 施後（`d3d8f46`） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（164） | `0`／`0`／`⇒ 紅 []；rc 0`（171） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（471） | `0`／`0`／`⇒ 紅 []；rc 0`（467） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（34） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（34） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·45） | `0`／`0`／`⇒ 紅 []；rc 0`（50） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·18） | `0`／`0`／`⇒ 紅 []；rc 0`（18） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·286） | `0`／`0`／`⇒ 紅 []；rc 0`（329） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `1`／`0`／`⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1`（87） | `0`／`0`／`⇒ 紅 []；rc 0`（99） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `1`／`0`／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（604） | `0`／`0`／`⇒ 紅 []；rc 0`（674） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `1`／`0`／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（831） | `0`／`0`／`⇒ 紅 []；rc 0`（950） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（10） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（10） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | 沿用基準：`0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（基準·80） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（87） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·483） | `0`／`0`／`⇒ 紅 []；rc 0`（598） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2221） | `0`／`0`／`⇒ 紅 []；rc 0`（2580） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·39） | `0`／`0`／`⇒ 紅 []；rc 0`（43） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·6） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（基準·25） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（26） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·25） | `0`／`0`／`⇒ 紅 []；rc 0`（26） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·298） | `0`／`0`／`⇒ 紅 []；rc 0`（352） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·424） | `0`／`0`／`⇒ 紅 []；rc 0`（485） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·42） | `0`／`0`／`⇒ 紅 []；rc 0`（48） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·42） | `0`／`0`／`⇒ 紅 []；rc 0`（46） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·8） | `0`／`0`／`⇒ 紅 []；rc 0`（9） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·27） | `0`／`0`／`⇒ 紅 []；rc 0`（28） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·19） | `0`／`0`／`⇒ 紅 []；rc 0`（20） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·13） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·231） | `0`／`0`／`⇒ 紅 []；rc 0`（274） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·59） | `0`／`0`／`⇒ 紅 []；rc 0`（71） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·1131） | `0`／`0`／`⇒ 紅 []；rc 0`（1044） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `1`／`0`／`⇒ 紅 ['R4']；rc 1`（200） | `0`／`0`／`⇒ 紅 []；rc 0`（215） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·136） | `0`／`0`／`⇒ 紅 []；rc 0`（147） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·499） | `0`／`0`／`⇒ 紅 []；rc 0`（488） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | 沿用基準：`0`／`0`／`selftest 9/9 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | 沿用基準：`0`／`0`／`selftest 13/13 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | 沿用基準：`0`／`0`／`ε ＝ 0.0002｜rc 0`（基準·2） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | 沿用基準：`0`／`0`／`紅項 [] 器紅 0`（基準·12） | `0`／`0`／`紅項 [] 器紅 0`（12） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·497） | `0`／`0`／`⇒ 紅 []；rc 0`（498） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／（JSON 之摘要列·略）（277） | `0`／`0`／（JSON 之摘要列·略）（288） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／（JSON 之摘要列·略）（204） | `0`／`0`／（JSON 之摘要列·略）（209） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（274） | `0`／`0`／`⇒ 紅 []；rc 0`（292） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（202） | `0`／`0`／`⇒ 紅 []；rc 0`（202） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（579） | `0`／`0`／`⇒ rc 0（不符 0 項）`（657） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（422） | `0`／`0`／`⇒ rc 0（不符 0 項）`（451） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（428） | `0`／`0`／`⇒ 紅 []；rc 0`（500） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·1584） | `0`／`0`／`⇒ 紅 []；rc 0`（1779） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·1549） | `0`／`0`／`⇒ 紅 []；rc 0`（1765） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（156） | `0`／`0`／`⇒ 紅 []；rc 0`（176） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（594） | `0`／`0`／`⇒ 紅 []；rc 0`（696） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（452） | `0`／`0`／`⇒ 紅 []；rc 0`（496） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／`⇒ 紅 []；rc 0`（31） | `0`／`0`／`⇒ 紅 []；rc 0`（40） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（183） | `0`／`0`／`⇒ 紅 []；rc 0`（194） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（10） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W8']；rc 1`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（32） | `0`／`0`／`⇒ 紅 []；rc 0`（491） |

前態實跑 40 呼叫·耗時之和 6317 s；施後 80 呼叫·耗時之和 18264 s·stderr 合計 0 B

## 附錄二　`V-1″` 之 `34` 呼叫之 `stdout` 全文（施後·`d3d8f46`·依前置″ (甲) 之序）

### `#1`　`python3 verify/probes/probe_WG9385_k974.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
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

### `#2`　`python3 verify/probes/probe_WG9385_k974.py wiring /tmp/w 158f7fe`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 頂層之新名與⛔ 案件字面：[True, True, True, True]／K974_PARAMS True／字面 []
  ✅ W2 main() 恰一處呼之：['k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)']
  ✅ W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）：
  ✅ W4 JUNCTION 存 session：
  ✅ W5 步驟 H 之段以假 st 實跑：[{'label': 'B1', 'front_width': 15.0, 'front_length': 0.0, 'front_new': False, 'left_side_width': 0.0, 'left_side_length': 0.0, 'left_side_new': False, 'right_side_width': 0.0, 'right_side_length': 0.0, 'right_side_new': False, 'front_scale': 2.25, 'left_side_scale': 0.5}]／[('warning', '⚠️ 警示甲')]／[('error', '⛔ 錯甲'), ('error', '⛔ 錯乙')]／停 False/True
  ✅ W6 verify/ 之生產碼⛔ 呼之：[]
  ✅ W7 main／calc 唯增列（具名之換列三）·頂層之相異：相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k967_pool_less', 'k967_pool_out', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']／刪列 3
⇒ 紅 []；rc 0
````

### `#3`　`python3 verify/probes/probe_WG9385_k974.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  各面之尺度：R4 front 0.0／left 1.0／right 1.0；R6 front 2.0／left None／right 1.0；R5 front 2.0／left 1.0／right None；R2 front 2.0／left 1.0／right None；R3 front 2.0／left None／right 1.0；R1 front 0.0／left 1.0／right 1.0
  ✅ R1 尺度 ＝ 快照之負擔尺度_輸入：不符 []／警示 []／錯誤 []
  ✅ R2 calc 之列給尺度與否逐值同：741.76／741.76
  ✅ R3 抵充地之模擬（628-34·RD1）：RD1 1082.2651／628-34 之片 131.6000／比例 0.878403／負擔路寬 7.0272／期 1.513613、0.756806／得 1.513616、0.756808
  ✅ R4 私有地填「是」⇒ 填列錯誤：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']
  ✅ R6 二欄之結果之存與換檔：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']／[]
  ✅ R5 JUNCTION 之模擬（RD1 之一端）：框內 89.6652／比例 0.867420／期 1.469679／得 1.469679
⇒ 紅 []；rc 0
````

### `#4`　`python3 verify/probes/probe_WG9363_k953.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
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

### `#5`　`python3 verify/probes/probe_WG9363_k953.py wiring /tmp/w 7d8e954`（`rc 0`·`stderr` `0` B）

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

### `#17`　`python3 verify/probes/probe_WG9363_k953.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.51／ΣG 之變 2934.51（和 ≤ 0.1）True
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.87／ΣG 之變 3663.87（和 ≤ 0.1）True
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

### `#6`　`python3 verify/probes/probe_WG9367_adj4.py wiring /tmp/w d7a5ea4`（`rc 0`·`stderr` `0` B）

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

### `#13`　`python3 verify/probes/probe_WG9367_adj4.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
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

### `#18`　`python3 verify/probes/probe_WG9367_adj4.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@3.5：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@3.5：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6600（和 +0.0200·≤ 0.1）
  ✅ R4@3.5：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@3.5：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
  ✅ R1@0.0：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@0.0：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@0.0：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6600（和 +0.0200·≤ 0.1）
  ✅ R4@0.0：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@0.0：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
⇒ 紅 []；rc 0
````

### `#7`　`python3 verify/probes/probe_WG9370_adj4mut.py wiring /tmp/w 3b35daa`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
````

### `#19`　`python3 verify/probes/probe_WG9370_adj4mut.py mutate /tmp/w`（`rc 0`·`stderr` `0` B）

````text
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

### `#14`　`python3 verify/probes/probe_WG9375_k965.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ K1 弱弱聯合·大者在前 ⇒ X2 併入 X、於 X 之位；乙照原位
  ✅ K2 弱弱聯合·大者在後 ⇒ X 併入 X2；乙遞補而不配地
  ✅ K3 同街廓先（弱弱聯合）·他街廓之己宗（他地號）⛔ 依手冊併入（K-9-73·改 K-9-64）
  ✅ K4 他街廓之己宗相連（他地號）⇒ 入池閘⛔ 處（K-9-73）
  ✅ K5 合併後反不能配 ⇒ 回原狀、併入原可配之宗之原位（K-9-58 ③）
  ✅ K6 街角第 1 宗⛔ 合併、依手冊併入（K-9-58 ①）
  ✅ K7 跨左右推進 ⇒ 併向應分配面積較大之一側（K-9-58 ②）
  ✅ K8 第 3 步：併入同街廓不相連之已配得之宗（其位）
  ✅ K9 N0-9 之片亦先判同街廓（K-9-73·改 K-9-64 ③）
  ✅ K10 重排後遞補者從第 1 步起處理
  ✅ K11 弱弱聯合之宗其後配不到 ⇒ ⛔ 再弱弱聯合
  ✅ K12 第 3 步併入後反不配地 ⇒ 回原狀
  ✅ K13 經同地主之道路片相連 ⇒ 入池閘⛔ 處（交手冊先行·K-9-73）
  ✅ K14 輸入之單元之成員之形與成員之列（NOTE 5）
  ✅ K15 單元之成員之切片取不到 ⇒ 停機
  ✅ K16 入池閘⛔ 判經道路片之相連 ⇒ 切片未給亦⛔ 停機（K-9-73）
  ✅ K17 檢核之輸入未給 ⇒ 停機
  ✅ K18 調配之輸入：宿主在他街廓 ⇒ 配地街廓 ＝ 宿主之街廓
  ✅ K19 調配之輸入：入池閘之帳之部分併出
  ✅ K20 重劃前面積取輸入之 build 之帳（K-9-67·補令一 R-16′）
  ✅ K21 重劃前面積減入池閘之部分併出（入池閘部分併出·輸入之帳）
  ✅ K22 K-9-58 ③ 二次皆不配地 ⇒ 收斂（⛔ 空轉·⛔ 往他街廓）
  ✅ K23 部分併出之帳隨剩下入單元（調配之輸入⛔ 重計）
  ✅ K24 第 1 步之相連以其自身之地（他街廓併入之片⛔ 計）
  ✅ K25 受併宗最後不配地 ⇒ 已併入者回原狀（K-9-61 ⑤）
  ✅ K26 調配之輸入：受併宗為他單元之成員
  ✅ K27 經同地主之連續道路片相連 ⇒ 入池閘⛔ 處（交手冊先行·K-9-73）
  ✅ K28 部分併入後之剩下⛔ 再試他街廓（續第 3 步起）
  ✅ K29 地主於本街廓已有配得之宗 ⇒ ⛔ 弱弱聯合（K-9-57 ④）
  ✅ K30 N0-9 之片亦依手冊併入街角第 1 宗（K-9-73·K-9-58 ①）
  ✅ K31 第 3 步：街角第 1 宗依手冊併入
  ✅ K32 回原狀後各併入原可配之宗中應分配面積最大者（K-9-76 ②·⛔ 相鄰者先）
  ✅ K33 單元之部分併入 ⇒ 各成員乘同一百分比（巳 ①·K-9-66）
  ✅ K34 合併之宗終不配地 ⇒ 回原狀（K-9-58 ③·收斂時）
  ✅ K35 已試之帳以成員為準
  ✅ K36 調配之輸入：配地街廓含宿主之街廓
  ✅ K37 合併之列其後同一標的再受同街廓之併入 ⇒ 前列「續併」、末列「留置」
  ✅ K38 受併宗之相連⛔ 藉他街廓併入之片
  ✅ K39 回溯由最近之一次施起
  ✅ K40 不相連而併入之片⛔ 為相連
  ✅ K41 他街廓之併入之回溯由最近之一次起（K-9-61 ⑤）
  ✅ K42 回原狀之組合⛔ 再施（跨回溯）
  ✅ K43 回原狀後之併入⛔ 取已試之組合
  ✅ K44 回原狀後之併入逐宗（其一不配地⛔ 連帶其他）
  ✅ K45 回原狀之帳跨回溯而存
  ✅ K46 調配之輸入：段三之受併宗未配地 ⇒ 停機
  ✅ K47 N0-9 之片之回原狀後之併入
  ✅ K48 回原狀之帳之序定於回原狀之時（依其時之應分配面積·K-9-76 ②）
  ✅ K49 回原狀之帳之分不到之宗 ①′ 先於 ①
  ✅ K50 回原狀之帳之序以該次合併時之應分配面積定
  ✅ K51 成員之地價區段相異 ⇒ 各以其來源量計
  ✅ K52 合併之單元之部分併入之調配之輸入
  ✅ K53 成員之剩下之合與宗之面積不符（含非成員之土地）⇒ 停機
  ✅ K54 k965_part_split 之純函式
  ✅ K55 含非成員之土地而部分併入皆不過檢核 ⇒ ⛔ 停機·記未成（停機待檢核過後）
  ✅ K56 單片含非其成員之土地（面積_m2 淨 ≤ 0）而部分併入過檢核 ⇒ 停機（GB-205）
  ✅ K57 單片之帳相合 ⇒ 部分併入照常（其帳為全量）
  ✅ K58 單片含非其成員之土地而部分併入皆不過檢核 ⇒ ⛔ 停機·記未成
  ✅ K59 街角第 1 宗之應分配面積小於他宗 ⇒ 併入應分配面積大者（K-9-73 ①）
  ✅ K60 N0-9 之片亦入弱弱聯合（K-9-73 ②）
  ✅ K61 街角第 1 宗之依手冊之併入部分成／未成 ⇒ 其餘續依第 3 步併入次大之已配得之宗（K-9-73 ①）
  ✅ K62 同街廓相連之合併含可配得之宗 ⇒ 標的 ＝ 可配得之最大一塊（其側其位·K-9-76 ①）
  ✅ K63 回原狀之帳之序 ＝ 可配得之宗之應分配面積大者先（⛔ 相連者先·K-9-76 ②）
  ✅ K64 宗之成員帶「第31條第3款併入」⇒ ⛔ 併入同街廓之已配得之宗；弱弱聯合不以已配得之宗之有無為限（K-9-75 ①）
  ✅ K65 他宗之分量⛔ 含帶標記之宗（K-9-75 ①）
  ✅ K66 帶標記之宗之分量⛔ 含已配得之宗 ⇒ 與相連之配不到者依第 4 步合併（K-9-75 ①）
  ✅ K67 帶標記之宗之相連之合併不配地 ⇒ 續與不相連之配不到之宗弱弱聯合（全部·K-9-77）
  ✅ K68 同歸戶之他宗在推進序之前 ⇒ 帶標記之宗與其相連之宗先合併（K-9-77）
  ✅ K69 他街廓之帶標記之宗⛔ 先之（K-9-77）
  ✅ K70 他歸戶之帶標記之宗⛔ 先之（K-9-77）
  ✅ K71 帶標記之宗二 ⇒ 依 k967_rank 之序先之（K-9-77）
  ✅ K72 帶標記之宗已配得 ⇒ 相連之配不到之宗依第 3 步併入之（K-9-77）
  ✅ K73 帶標記之宗二·推進序之首⛔ 帶標記 ⇒ 依 k967_rank 之序（K-9-77）
  ✅ K74 推進序之首為帶標記而序次之宗 ⇒ 序首之帶標記之宗先之（K-9-77）
  ✅ P0 判式自驗 74／74
⇒ 紅 []；rc 0
````

### `#15`　`python3 verify/probes/probe_WG9375_k965.py wiring /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ Y1 簽名：五位置參數 ＋ 關鍵字 max_rounds／temp_parcels／cat_of／front_rows（預設 None）
  ✅ Y2 harness 之 run_step_g：入池閘之呼叫恰一、注入三參數、切片取 session 之 f3_k965_temp
  ✅ Y3 畫面之 _k929_6_screen_gate：注入三參數（f3_temp_parcels·classified_blocks·sb_rows_by_label）
  ✅ Y4 harness 之 build_build_parcels 寫 session 之 f3_k965_temp
  ✅ Y5 k929_6_fixpoint 內：k966_block_merge 恰一（得 1）·k953_alloc_summary／k967_rank／_projection_order 皆呼
  ✅ Y6 adj_intake 讀「入池閘部分併出」與「入池閘成員部分併出」
  ✅ Y7 k929_6_fixpoint 之字串常數⛔ 含案件字面（命中 []）
  ✅ Y8 三【未裁】之停機已去（K-9-58 ①②③）·未收斂之停機仍在
  ✅ Y9 畫面對拍器之畫面之 session 寫 f3_temp_parcels（同 main()）
  ✅ Y10 k965_part_split 之簽名·k929_6_fixpoint 內呼之恰一（得 1）·_pre965 呼 _src965·巳 ① 之停機已去
  ✅ Y11 GB-205 之停機⛔ 在 k965_part_split（得 0）·在 _try965 之 _chk965 之後（_chk965 [10415]·停機 [10420]）
⇒ 紅 []；rc 0
````

### `#16`　`python3 verify/probes/probe_WG9375_k965.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：build 51 宗·單元 7 ＝ 本器所載 True
  ✅ R2@3.5：配地 28 宗·不配地 21 宗 ＝ 本器所載 True
  ✅ R3@3.5：入池閘之紀錄 7 列 ＝ 本器所載 True
  ✅ R1@0.0：build 52 宗·單元 6 ＝ 本器所載 True
  ✅ R2@0.0：配地 29 宗·不配地 21 宗 ＝ 本器所載 True
  ✅ R3@0.0：入池閘之紀錄 6 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

### `#44`　`python3 verify/probes/probe_WG9361_k954.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
── 合成對照（harvest 之 app.py·⛔ 本案資料）──
  ✅ A1 精確共邊（長 1）⇒ (True, 1.0)·長度逐位
  ✅ A2 角點相接 ⇒ (False, 0.0)·長度逐位
  ✅ A3 精確共邊 0.005 ⇒ (False, 0.005)
  ✅ A4 微米級錯位而共線（精確交集為一點）⇒ 相連、其長 ≈ 1（三位小數）
  ✅ A4′ 同 A4·精確交集之線長 ＝ 0（受詞確為現碼判為不相連之形）
  ✅ A5 平行錯位 2e-4 m ⇒ (False, 0.0)
  ✅ A6 容差內而共線長 0.008 ⇒ (False, 0.0)
  ✅ A7 相距 0.01 m ⇒ (False, 0.0)
  ✅ A8 坐標 ~3e5／2.6e6 m 之微米錯位（共線長 12）⇒ 相連、其長 ≈ 12
  ✅ A9 缺片（None）⇒ (False, 0.0)
  ✅ A10 三片鏈（A–B 精確、B–C 微米錯位）⇒ 一群
  ✅ A11 三片鏈（B–C 平行錯位 2e-4）⇒ 二群
  ✅ A12 常數 K6_SHARE_COORD_TOL ＝ 1e-4、K6_SHARE_MIN_LEN ＝ 0.01
  ✅ A13 既有之 k6_merge_selftest() 仍過（S-1〜S-7）
  ✅ A14 精確共線 0.0099（容差不增其長）⇒ (False, 0.0099)
  ✅ A15 角點相接而二邊近切（斜率 0.0087）⇒ (False, 0.0)
  ✅ A16 二片重疊而邊界淺交（斜率 0.0087）⇒ (False, 0.0)
  ✅ A17 一端之界址點相差 1.5e-4、他端 5e-5（中段在容差內）⇒ (False, 0.0)
  ✅ A18 中間之界址點相差 2e-4 ⇒ (False, 0.0)
  ✅ A19 坐標含 NaN（共線之邊在容差內）⇒ 二向皆不相連
  ✅ A20 重判之長二向逐位同（A4 之形）
  ✅ A21 中間之界址點相差 5e-5（容差內）⇒ 相連、其長 ≈ 10（三位小數）
  ✅ A22 MultiPolygon 與他片微米錯位而共線（A4 之形）⇒ 二向皆相連、其長 ≈ 1
  ✅ A23 自觸之環經 buffer(0) 成 MultiPolygon（二部）、其一部與他片微米錯位而共線 ⇒ 相連、其長 ≈ 1
  ✅ A24 MultiPolygon 之他部之坐標含 NaN（共線之部在容差內）⇒ 二向皆不相連
  ✅ A25 MultiPolygon 之一部與他片平行錯位 2e-4 ⇒ (False, 0.0)
  ✅ A26 非面狀之受詞（線·沿 A1 之共邊微米錯位）二向與空片 ⇒ 皆 (False, 0.0)
  ✅ A27 以容差相連之二片之聯集（buffer(0) 後仍為 MultiPolygon）與第三片平行錯位 5e-5 ⇒ 相連、其長 ≈ 1
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 28／28
⇒ 紅 []；rc 0
````

### `#45`　`python3 verify/probes/probe_WG9361_k954.py wiring /tmp/w`（`rc 0`·`stderr` `0` B）

````text
── 接線（AST·app.py）──
  ✅ W1 模組層 K6_SHARE_COORD_TOL = 0.0001 恰一處（賦值 1 處·值 0.0001）
  ✅ W2 k6_shares_segment 先算精確交集、其後引 K6_SHARE_COORD_TOL（精確交集之字樣於 1014·容差之引於 2205）
  ✅ W3 K6_SHARE_COORD_TOL 唯 k6_shares_segment 及其所呼叫之函式引之（引之者 ['k6_shares_segment']；許 ['_k954_all_finite', '_k954_areal', '_k954_vtx_len', 'k6_shares_segment']）
  ✅ W4 k6_shares_segment 及其所呼叫之函式⛔ 案件字面（[]）
⇒ 紅 []；rc 0
````

### `#46`　`python3 verify/probes/probe_WG9361_k954.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
══ 退縮 3.5 ══
  ✅ R0 新判為相連之對 19（同歸戶 15）＝ 期 (19, 15)；頂點至他片界線之距之最大者 1.000e-05 m（< 2e-05）
     628(1)〔R4·G009〕–628(2)〔R6·G009〕
     628(1)〔R4·G009〕–628(3)〔R5·G009〕
     628(1)〔R4·G009〕–_GHOST_(R4)〔R4·—〕
     628(2)〔R6·G009〕–628(3)〔R5·G009〕
     628-1(1)〔R4·G009〕–628-1(2)〔R6·G009〕
     628-12(1)〔G1·G003〕–628-12(2)〔RD4·G003〕
     628-12(1)〔G1·G003〕–628-12(3)〔RD3·G003〕
     628-18(1)〔R6·G005〕–628-18(2)〔R5·G005〕
     628-20(1)〔R6·G007〕–628-20(2)〔R5·G007〕
     628-21(1)〔R6·G017〕–628-21(2)〔R5·G017〕
     628-22(1)〔R6·G017〕–628-22(2)〔R5·G017〕
     628-23(1)〔R6·G017〕–628-23(2)〔R5·G017〕
     628-5(1)〔G1·G012〕–628-5(2)〔RD3·G012〕
     628-53(1)〔R6·G025〕–628-53(2)〔R5·G025〕
     628-7(1)〔R6·G022〕–628-7(2)〔R5·G022〕
     628-7(3)〔G1·G022〕–628-7(4)〔RD3·G022〕
     _GHOST_(G1)〔G1·—〕–_GHOST_(RD3)〔RD3·—〕
     _GHOST_(R1)〔R1·—〕–_GHOST_(RD1)〔RD1·—〕
     _GHOST_(R4)〔R4·—〕–_GHOST_(RD2)〔RD2·—〕
  ✅ R1 合併群（126 片·33 歸戶）＝ 外部錨：相異 []
  ✅ R2 與精確之判相異之歸戶 ['G005', 'G007', 'G012', 'G017', 'G022']；其群 ＝ GROUPS_TOL：True
  ✅ R3 段三之紀錄 19 列（期 19）；628-20(3) ✅；628-45(3) ✅；628-45(4) ✅
  ✅ R4 配地：628-45(2) G 902.52（期 902.52）、628-45(1) G 525.28（期 525.28）、628-20(1) G 461.06（期 461.06）；抵費地 R3 1883.05（期 1883.05）、R5 1742.98（期 1742.98）、R6 1777.33（期 1777.33）
══ 退縮 0.0 ══
  ✅ R3 段三之紀錄 0 列（期 0）
⇒ 紅 []；rc 0
````

### `#62`　`python3 verify/probes/probe_WG9387_k961h.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
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

### `#63`　`python3 verify/probes/probe_WG9387_k961h.py wiring /tmp/w 34736ab`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 adj_intake 呼叫 k967_rank（呼叫 1）
  ✅ X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise（[]）
  ✅ X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']）
  ✅ X4 adj_intake 內⛔ 案件字面（[]）
  ✅ X5 生產碼 app.py 以外之 33 檔對基準相異 0（相異 []）
⇒ 紅 []；rc 0
````

### `#64`　`python3 verify/probes/probe_WG9387_k961h.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 92.46｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R3｜據 R2 27.55、R3 28.34｜外部錨 R3
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 88.63｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R2｜據 R2 27.55、R3 24.88｜外部錨 R2
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
⇒ 紅 []；rc 0
````

### `#65`　`python3 verify/probes/probe_WG9388_k961s3.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
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
  ✅ K13 二受併宗之一於現態未保留 ⇒ 停機（取得即鎖定·⛔ 還原）
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

### `#66`　`python3 verify/probes/probe_WG9388_k961s3.py wiring /tmp/w fd88f64`（`rc 0`·`stderr` `0` B）

````text
── 接線（工作樹之 app.py 對基準 fd88f64）──
  ✅ X1 四停機之字樣皆去（殘 []）
  ✅ X2 `_recv_of(b, y)` 之形與其 5 呼叫皆二引數
  ✅ X3 頂層之相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X4 ⛔ 案件字面（[]）
  ✅ X5 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#69`　`python3 verify/probes/probe_WG9389_trialstop.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

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

### `#70`　`python3 verify/probes/probe_WG9389_trialstop.py wiring /tmp/w 929ea20`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 11（基準之帶號 10·k980_acq_check 1）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'main', 'select_corner_lots_both_sides_v12']／不合 []）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
````

### `#71`　`python3 verify/probes/probe_WG9389_trialstop.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
````

### `#72`　`python3 verify/probes/probe_WG9390_k961r.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ L1 合併再試（①）所得之宗⛔ 保留 ⇒ 停機（⛔ 還原）
  ✅ L2 經道路片（②）所得者⛔ 保留 ⇒ 停機
  ✅ L3 二端皆⛔ 保留 ⇒ 停機（訊息具二者）
  ✅ L4 先成者保留而後成之右端者⛔ 保留 ⇒ 停機（訊息具後者、⛔ 具保留者）
  ✅ L5 競合（題二）之所取之一端⛔ 保留 ⇒ 停機
  ✅ L6 競合（題一·切半二端各配一宗）而皆⛔ 保留 ⇒ 停機
  ✅ L7 皆保留 ⇒ 同改前、鎖定之宗受併入、試算 3（步驟 10 沿用其查之試算）
  ✅ L8 有成者而該群無待後處理之土地 ⇒ 仍查（試算 1）
  ✅ L9 查之試算中止 ⇒ 停機（無從判定）
  ✅ L10 無成者 ⇒ ⛔ 查（試算 0）
  ✅ L11 L7 之換名、左右鏡射、旋轉並移至 TWD97 之尺度 ⇒ 同 L7
  ✅ L12 成者皆保留而非成者之宗⛔ 保留 ⇒ ⛔ 停機
  ✅ L13 紀錄⛔ 含回原狀之列
  ✅ L14 題一 4 之照配（後處理之成）⛔ 為鎖定之受詞 ⇒ ⛔ 停機
  ✅ P0 判式自驗 14／14
⇒ 紅 []；rc 0
````

### `#73`　`python3 verify/probes/probe_WG9390_k961r.py wiring /tmp/w 2aa6302`（`rc 0`·`stderr` `0` B）

````text
── 接線（工作樹之 app.py 對基準 2aa6302）──
  ✅ X1 舊停機之字樣去之（殘 0）、還原之字樣去之（{'回原狀': 0, '還原後仍出現': 0}）、鎖定之查之字樣 3（期 ≥ 1）
  ✅ X2 頂層之相異 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_side_geom', 'end_block_trial_G', 'f3_screen_stepg_run', 'k6b_stage3_run', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X3 ⛔ 案件字面（[]）
  ✅ X4 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#74`　`python3 verify/probes/probe_WG9390_k961r.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 1·回原狀之列 0·其檢核 0·段三之成者 3·G 值列 35）
  ✅ R1@0.0：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 0·回原狀之列 0·其檢核 0·段三之成者 0·G 值列 36）
  ✅ R0 諸退縮之段三之成者之和 3（[3, 0]·期 ≥ 1·其查已行）
⇒ 紅 []；rc 0
````

### `#75`　`python3 verify/probes/probe_WG9391_k980x.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ C1 未輸入 ⇒ 100.5
  ✅ C2 輸入 0 ⇒ 逐位同 C1
  ✅ C3 輸入 100 ⇒ 逐位同 C1
  ✅ C4 輸入恰 100.5 ⇒ 逐位同 C1
  ✅ C5 輸入 150 ⇒ 面積∈[150,150.01]·遠側 x＝5.15·∥SIDE_LINE·含 C1
  ✅ C6 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ C7 輸入 −1 ⇒ 停機
  ✅ C8 C5 之旋轉 37°·鏡射·TWD97 ⇒ 面積同 C5
  ✅ C9 側街斜交（∦ 宗地分配線）輸入 200 ⇒ 面積∈[200,200.01]·遠側界線 ∥ SIDE_LINE（Δx＝6）
  ✅ E1 未輸入 ⇒ R_end 255·內側界 13.5（buf 3.5）
  ✅ E2 輸入恰 255 ⇒ 逐位同 E1
  ✅ E3 輸入 300 ⇒ R_end∈[300,300.01]·內側界 x＝15
  ✅ E4 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ E5 E3 之旋轉·鏡射·TWD97 ⇒ R_end 同 E3
  ✅ E6 _end_region_R 之未輸入與 0 ⇒ R_end 逐位同（255）；end_block_band_width 之 0 ⇒ 停機
  ✅ T1 距 0.02 ⇒ ⛔ 停
  ✅ T2 距恰 0.01 ⇒ 停
  ✅ T3 距 0.005 ⇒ 停
  ✅ T4 重疊 ⇒ 停（訊息具二範圍之名）
  ✅ T5 唯一範圍或含 None ⇒ ⛔ 停
  ✅ T6 三範圍而唯其中二者相接 ⇒ 停
  ✅ K1 有效值之序（K-9-1 ⑨）：街廓覆寫 → 分區底 → 0；session 無鍵或 None ⇒ 0
  ✅ P0 判式自驗 22／22
⇒ 紅 []；rc 0
````

### `#76`　`python3 verify/probes/probe_WG9391_k980x.py wiring /tmp/w a8657c4`（`rc 0`·`stderr` `0` B）

````text
── 接線（工作樹對基準 a8657c4）──
  ✅ W1 _build_corner_range_v3 之呼叫 4（期 ≥ 4）皆傳 min_build_area：皆傳
  ✅ W2 諸呼叫之數 [('end_block_side_geom', 1), ('end_block_host', 2), ('_place_pool_parcels', 2)]（期 ≥ 1、≥ 2、≥ 2）皆傳 min_build_area：皆傳
  ✅ W3 末端帶之單一真相源 {'_place_pool_parcels→_end_region_R': 1, '_place_pool_parcels→_end_band': 0, '_end_region_R→end_block_band_width': 1, 'end_block_band_width 之呼叫（全檔）': 1}（期 1、0、1、1）
  ✅ W4 min_build_area 之值皆為 k980_mba（呼叫 8·期 ≥ 8·不合 []）、v12 之 _mba_pk 之賦值 True、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（4／基準 4）、k980_mba 之分區之引數為字面者 []（期無）
  ✅ W5 k980_range_touch_check 之呼叫 [('select_corner_lots_both_sides_v12', 1), ('f3_screen_stepg_run', 1), ('stepg:_run_step_g_impl', 1)]·app.py 全檔 2（期各 1·app.py 全 2）、其範圍之名齊全 [True, True, True]（期三真）
  ✅ W6 頂層之名之增 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']（期 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']）、減 []
  ✅ W7 新增或改之頂層節點（22）內新增之案件字面 []
  ✅ W8 逐層照傳 min_build_area 皆照傳
  ✅ W9 引擎經 ns 取之新名 ['k980_mba', 'k980_range_touch_check'] ⊆ _WF_NS_NAMES（漏 []）
⇒ 紅 []；rc 0
````

### `#77`　`python3 verify/probes/probe_WG9391_k980x.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28}·err None）
  ✅ R2@3.5 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}·不合 []）
  ✅ R1@0.0 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28}·err None）
  ✅ R2@0.0 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 124.94, 'R2': 162.99, 'R3': 163.8, 'R4': 126.08, 'R5': 156.5, 'R6': 262.28}·不合 []）
⇒ 紅 []；rc 0
````

### `#78`　`python3 verify/probes/probe_WG9392_k980g.py selftest /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ G1 D 15·l₂ 6：二上界 × 二座標系之 G ＝ round(G*, 2)
  ✅ G2 D 25·l₂ 2：同 G1
  ✅ G3 邊界：G* 於半分之上 2e-5 ⇒ 進、之下 2e-5 ⇒ 捨（四解皆同）
  ✅ G4 常數：K980_G_TOL ≤ 1e-6、K980_G_MAX_ITER ≥ 100
  ✅ H1 二值同 ⇒ 過（回 None·登記⛔ 增）
  ✅ H2 二值異 ⇒ 停（GB-206·K-9-80 ③·宗·二值·登記增恰一而全文同）
  ✅ H3 取至 2 位同 ⇒ 過
  ✅ H4 取至 2 位恰差 0.01 ⇒ 停
  ✅ H5 末端塊·右 ⇒ 停（訊息含末端塊、right）
  ✅ E1 左端之引數
  ✅ E2 右端：方向 −d̂、起點 p1 ＋ S·d̂
  ✅ E3 S ＝ 0.05 ⇒ 上界 0.1
  ✅ E4 側別非 left／right ⇒ 停機
  ✅ E5 回 (G, S_raw)
  ✅ J1 右側之街角第 1 宗：評選之式 ＝ 實配之鏈首（SIDE_LINE 偏 δ·二座標系·二 a）
  ✅ J2 左側之街角第 1 宗：同 J1
  ✅ J3 判別之前提：比之數 40·δ 0.3 之幾何之起算點異其 G
  ℹ️ G1 量 290·略 10；G2 量 288·略 12
  ✅ P0 判式自驗 17／17
⇒ 紅 []；rc 0
````

### `#79`　`python3 verify/probes/probe_WG9392_k980g.py wiring /tmp/w 56c77fd`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 _solve_G_one 之 solve_G_binary 以 K980_G_TOL／K980_G_MAX_ITER（呼叫 1·全檔 1）
  ✅ W2 取得之宗之自我檢查之四處（[('app.py', 4), ('verify/stepg_pipeline.py', 4)]）
  ✅ W3 end_block_host 之評選經 end_block_trial_G（1）·solve_one 之直呼 0
  ✅ W4 引擎經 ns 取之新名 ['end_block_trial_G', 'k980_acq_check'] ⊆ _WF_NS_NAMES（漏 []）
  ✅ W5 頂層之名之增 ['K980_G_MAX_ITER', 'K980_G_TOL', 'end_block_trial_G', 'k980_acq_check']·減 []
  ✅ W6 k980_acq_check 經 k6_program_stop 立 GB-206 之停機
  ✅ W7 新增或改之頂層節點（9）內新增之案件字面 []
  ✅ W8 _corner_first_lot_G 之 _solve_G_one 以 is_corner=True、w0_start=0.0（呼叫 1）
⇒ 紅 []；rc 0
````

### `#80`　`python3 verify/probes/probe_WG9392_k980g.py run /tmp/w`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 自我檢查 423 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@3.5 本案之錨（KL 05:22 所核之甲）不合 []
  ✅ R1@0.0 自我檢查 324 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@0.0 本案之錨（KL 05:22 所核之甲）不合 []
⇒ 紅 []；rc 0
````

