# `W-G.9-392` 補令一　執行端回報（停機上呈·停機款 `4″`）

- 受單：`orders/W-G.9-392_補令一.md`（`95051` B·`sha256` `1d9a2eae95e9f09ef473f2df89c31a7342893059a88ad806c71ebd4793eca3cb`·與 `STATE.json` 合；`SELF_SHA256` 依 `P-5` 原口徑自驗 ＝ `6f75b64a0243fa24ff628fda763d79f62875f0e2f4005b0b7b5a986d5aff9db6`·合）。
- 結果：**停機上呈**（停機款 `4″`·工項二″ 之前置″ 項 `4` 之期不符）。**生產碼⛔ 動**（`R-0″` 未施、`R-7″` 未撰）；**本案配地⛔ 變**。
- 停機之內容⛔ 涉土地後果（純屬單內之期之書法·與 `自誤 629`〔`W-G.9-388` 補令一前置″ 項 `3`〕、`自誤 632`〔`W-G.9-390` 補令一前置″ 項 `4`〕同形）。
- 時程：接單 `2026-10-22T17:01:00+08:00`（推送一度被拒〔發單端之門鈴之記錄 `d1d5c8a` 同時入〕·重取後依新態〔仍 `pending`·單之 `sha256` 不變〕重放而成 `7cf862e`）→ 停機 `17:05`（Asia/Taipei）；`effort=high`。
- `<O>` ＝ `/tmp/O392p1`（倉外）；施工樹 ＝ `/tmp/w`（雲端完整複本）。

## 一、停機款之三值

| 款 | 期（本補令之文·逐字） | 實 |
|---|---|---|
| `4″`（工項二″ 之前置″ 項 `4`） | 「`git diff --stat c4666ab HEAD` 之出艙唯塊 `Fy48` 之 `9` 檔（入報告）」 | 出艙 **`10` 檔**（見下）：`docs/orders/W-G.9-392_補令一.md`（`A`·`622` 列之增·＝ 工項零″ 依本補令所入之本補令自身）與塊 `Fy48` 之 `9` 器（`M`） |

`git diff --stat c4666ab HEAD`（`HEAD` ＝ 工項一″ 之端 `f12824f57b5576bc54260ee5e61965e149511937`）之出艙逐字：

```
 ....9-392_\350\243\234\344\273\244\344\270\200.md" | 622 +++++++++++++++++++++
 verify/probes/probe_WG9363_k953.py                 |   1 +
 verify/probes/probe_WG9367_adj4.py                 |   1 +
 verify/probes/probe_WG9370_adj4mut.py              |   1 +
 verify/probes/probe_WG9385_k974.py                 |   1 +
 verify/probes/probe_WG9387_k961h.py                |   1 +
 verify/probes/probe_WG9388_k961s3.py               |   1 +
 verify/probes/probe_WG9389_trialstop.py            |   1 +
 verify/probes/probe_WG9390_k961r.py                |   1 +
 verify/probes/probe_WG9392_k980g.py                |  65 ++-
 10 files changed, 694 insertions(+), 1 deletion(-)
```

`git -c core.quotepath=false diff --name-status c4666ab HEAD`：

```
A	docs/orders/W-G.9-392_補令一.md
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

前置″ 項 `4` 之後半（同項·供參）：`git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py` 之「GB-206」「k980_acq_check」「end_block_trial_G」「K980_G_TOL」⇒ 各**無出艙**、`rc 1`（＝ 期）。

**執行端之所見（⛔ 裁）**：工項零″ 依本補令將本補令入倉於 `c4666ab` 與工項一″ 之端之間，故 `c4666ab..HEAD` 必含之；前置″ 項 `4` 之期與工項零″ 之令於字面相牴。此形與 `自誤 629`（`W-G.9-388` 補令一·補令二以 `D-3` 正之）、`自誤 632`（`W-G.9-390` 補令一）同——前二例執行端皆依停機款 `4″` 停機上呈。孰為所指（例：期改為十檔、或改比較之端點為工項零″ 之端、或改為 `--name-status` 之恰幾列），執行端⛔ 判——依單首 🔴 與停機款 `4″` 停下，待發單端之補令。

## 二、已做之工項（皆依單·逐字之首列·快轉推側支）

| 工項 | `commit` | 推送 | 內容 |
|---|---|---|---|
| 零″ | `31208b076709800329a63eaea0d47138c1a71680` | `verify/W-G.9-392-k980g`：`c4666ab` → `31208b0`（快轉） | `docs/orders/W-G.9-392_補令一.md`（新檔·二進位複製·`git cat-file blob` 與來源 `cmp` 逐位同；`git check-ignore -v --no-index` 無命中 `rc 1`）·`git show --numstat` ＝ `622`／`0` |
| 一″ | `f12824f57b5576bc54260ee5e61965e149511937` | `verify/W-G.9-392-k980g`：`31208b0` → `f12824f`（快轉） | 塊 `Fy48`（`<O>/Fy48.diff`）施於 `9` 器：施前 blob ＝ `§五″` 項 `2`（`9／9`）→ `git apply --check` 過 → 施後 blob 與 bytes ＝ `§五″` 項 `5`（`9／9`：`855c8088…`／`44905`、`0f17816b…`／`129399`、`ad77099d…`／`75528`、`e49f0ae7…`／`22152`、`294f7b67…`／`25195`、`33a91f0c…`／`43255`、`42f6cdb0…`／`35714`、`8032bda5…`／`30441`、`4285882a…`／`33197`）；`git status --porcelain` 唯此 `9` 檔；`git show --numstat` ＝ 閘 `1″` 之工項一″ 之列逐項同（`1/0` × `8`、`probe_WG9392_k980g.py` `64/1`） |

- 二 `commit` 之訊息 ＝ 首列逐字（與本補令之「首列逐字」之字樣以 `grep -F` 對拍各命中 `1`）＋ 空列 ＋ 環境之尾列二列；`git commit -F`。
- 工項二″〜四″：**⛔ 做**（停機）。已推之二 `commit` ⛔ 撤（`§零-2″` 末）。
- 推後：遠端 heads ＝ **`52`**；主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（⛔ 變）；側支 `verify/W-G.9-392-k980g` ＝ `f12824f57b5576bc54260ee5e61965e149511937`（其祖含 `c4666ab`）；其餘 `50` 列（除側支與 `ops/queue`）逐列 ＝ `<O>/heads_before_392p1.txt`。
- 施工樹之 `app.py`、`verify/stepg_pipeline.py` 仍 ＝ `b591d760…`／`b2f66223…`（工項一″ 之端·未施）；`git apply --check <O>/rep392.diff` 於工項一″ 之端 ⇒ `rc 0`（唯驗其可施·⛔ 施）。

## 三、`§零″` 之實值

| 項 | 期 | 實 |
|---|---|---|
| 0-1 context／`nproc` | 自報 | context 餘量充足（約 `14.8M` tokens）；`nproc` ＝ `4` |
| 0-2 主線 | `56c77fd…` | `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81` ✅ |
| 0-2 側支 | `c4666ab…` | `c4666ab4c747058fbaad143009c3a4138b7396dc` ✅ |
| 0-2 heads | `52` | `52` ✅（全列存 `<O>/heads_before_392p1.txt`） |
| 0-2 追蹤檔之變動（`--detach origin/verify/W-G.9-392-k980g` 後） | 空 | 空 ✅ |
| 0-2 旗標 | `[None, None, None, None, None]` | 同 ✅（殼之 `WV_` 變數 `0`） |
| 0-3 `probe_WG9321_issuer_anchor.py /tmp/w <O>/issuer_anchor_open.txt 634 629` | `rc 0`；自誤 `619`／`634`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]` | `rc 0`；「項4′ 四簿·正典框」四簿之值皆同 ✅；末 `✅ 二閘皆過` |
| 0-4 本補令之 bytes／`sha256`／`SELF_SHA256` | 見上 | 皆合 ✅ |
| 0-5 環境 | `rc 0` | 初 `rc 1`（`No module named 'shapely'`）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`<O>/pip_install_req.txt`·`rc 0`）⇒ 依項 `5` 之 🔎 釘五列（`<O>/pip_pin.txt`·`rc 0`）、去 `tzdata`（`<O>/pip_uninstall_tzdata.txt`·`rc 0`）⇒ 六模組之匯入 `rc 0` ✅；`pip check` ⇒ `No broken requirements found.` |
| 0-6 版本之比對 | `Python 3.11.17`；`pip freeze` `sha256` `ae1438da…` | `Python 3.11.17` ✅；`pip freeze`（`<O>/pip_freeze.txt`）`sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ✅ ⇒ 前置″ (丙) 可沿用基準（停機在先·⛔ 及之） |
| 0-7 pre-flight | 🔴 `0`／🟡 `3`（具名豁免）／ℹ️ `2` | `rc 0`；🔴 `0`；🟡 `3`：`[P-4] :183`（`§四-3″` 之表首列）、`[P-4] :298`（`§五″` 之二態之對拍）、`[P-4] :539`（塊 `K39` 之三）＝ 具名豁免之三處；ℹ️ `2`：`P-5` ✅ 相符（受詞 `94973` B）；`P-3` 之 `def main` 區間（AST）＝ `23691`-`31434`（＝ `§五″` 項 `9`） |
| 0-8 `<O>/rep392.diff` | `15801` B·`72b1892b…`·`205` 列 | `15801` B·`72b1892b4829af83e6ef13e408b66c626bbeccb095047b5969b8c501b0409207`·`205` 列 ✅ |
| 塊之抽取（`§五″` 項 `2`／`4`） | 見該項 | `Fy48` `13929` B·`111e365c…`·`200` 列；`K39` `8422` B·`d7500302…`·`44` 列；`E37` `2731` B·`36aa95b1…`·`13` 列；`P50` `2590` B·`d1e27cc2…`·`17` 列——皆 ✅ |

## 四、停機款之餘

| 款 | 實 |
|---|---|
| `1″` | 合（上表） |
| `2″` | 合（`SELF_SHA256`、bytes／`sha256`、入倉 blob） |
| `3″` | 合（塊與 `rep392.diff` 之實得、`Fy48` 之 `apply --check` 與施後 blob；`R-0″` 未施） |
| **`4″`** | **🔴 成就**（第一節） |
| `5″`〜`6″`、`8″`〜`9″`、`12″` | 未及（停機在先） |
| `7″` | 合（推送之目標唯 `verify/W-G.9-392-k980g`〔快轉二次〕與 `ops/queue`；⛔ `--force`；主線⛔ 動） |
| `10″` | 合（⛔ 改單／塊／器／命令一字） |
| `11″` | 合（本補令之入倉檔 `git check-ignore -v --no-index` `rc 1`） |
| `13″` | 合（存取與寫入皆⛔ 被拒） |

## 五、自捕與自解

1. `ops/queue` 之接單之推送一度被拒（非快轉·發單端之門鈴之記錄 `d1d5c8a` 同時入）⇒ 重取佇列：`status` 仍 `pending`、單之 `sha256` 不變 ⇒ `rebase` 時 `log.md` 衝突，以遠端之 `log.md` 為底、附本端之一列而解（⛔ `--force`）。
2. **通則「Bash 命令⛔ 含 heredoc」之違**：本輪之初，`STATE.json` 之改（接單）與抽取之助手腳本（`/tmp/scr/extract.py`·倉外·唯依 `§五″` 末之抽取式抽塊）之寫入以 heredoc 為之；其後察之，改以檔案寫入之工具為之。抽取之結果與 `§五″` 項 `2`〜`4` 逐位同，量測之命令皆⛔ 用 heredoc。
3. 本補令之複本置施工樹之根（`執行端.md` 丙 3）而以 `.git/info/exclude` 排除之（⛔ 入倉·使 `git status --porcelain` 唯受詞之檔）。

## 六、留待

- 發單端：前置″ 項 `4` 之期之正（如補令二）；工項二″ 起續做。側支 `f12824f` 之工項零″、一″ 可承（⛔ 撤）。
- 主 checkout 之同步由 KL 自行為之（README 第六節第 6 款）。
