# `W-G.9-398` 補令一　執行端回報（停機上呈·停機款 `4″`）

- 受單：`orders/W-G.9-398_補令一.md`（`146863` B·`sha256` `3c1e6621ccbd4721c613ebda5311214e0ce16a88e3462a03aefce57259391f89`·與 `STATE.json` 合；`SELF_SHA256` 依 `P-5` 原口徑自驗 ＝ `7c0d3516ed6e8ac97b358c29ca8ec61e4535a73f2fc18ade853c7be5cf739037`·合）。
- 結果：**停機上呈**（停機款 `4″`·工項二″ 之前置″ 項 `4` 之期不符）。**生產碼⛔ 動**（`R-1″`〜`R-7″` 未撰）；**本案配地⛔ 變**。
- 停機之內容⛔ 涉土地後果（純屬單內之期之計數之書法·與 `W-G.9-392` 補令一之停機〔前置″ 項 `4`〕、`自誤 629`、`自誤 632` 同形）。
- 時程：接單 `2026-10-28T15:28:04+08:00`（`ops/queue` `ed97a81`）→ 停機 `15:31`（Asia/Taipei）；`effort=high`。
- `<O>` ＝ `/tmp/O`（倉外）；施工樹 ＝ `/tmp/w`（雲端完整複本）。

## 一、停機款之三值

| 款 | 期（本補令之文·逐字） | 實 |
|---|---|---|
| `4″`（工項二″ 之前置″ 項 `4`） | 「`git diff --name-status f748370 <工項一″ 之 commit>` 之出艙 ＝ `A docs/orders/W-G.9-398_補令一.md` 與塊 `Fy56` 之 `18` 檔（皆 `M`）——恰 `18` 列（以工項一″ 之 `commit` 之全 sha 為端點·⛔ 以 `HEAD`）」 | 出艙 **`19` 列**：`A` 本補令 `1` 列 ＋ 塊 `Fy56` 之 `18` 檔（`M`）`18` 列——其列之內容與期之列舉逐一相合，唯列數 `19` ≠ 期之「恰 `18` 列」 |

`git -c core.quotepath=false diff --name-status f748370 8bc2add56c7f7201219db0064e3cdfedc30681fe`（工項一″ 之 `commit` 之全 sha 為端點）之出艙逐字（`<O>/pre/name_status_qpf.txt`·`19` 列；⛔ `quotepath=false` 之同命令之出艙存 `<O>/pre/name_status.txt`·亦 `19` 列）：

```
A	docs/orders/W-G.9-398_補令一.md
M	tests/test_pool_slot.py
M	verify/probes/probe_WG9352_endblock.py
M	verify/probes/probe_WG9363_k953.py
M	verify/probes/probe_WG9367_adj4.py
M	verify/probes/probe_WG9370_adj4mut.py
M	verify/probes/probe_WG9373_k966.py
M	verify/probes/probe_WG9375_k965.py
M	verify/probes/probe_WG9385_k974.py
M	verify/probes/probe_WG9387_k961h.py
M	verify/probes/probe_WG9388_k961s3.py
M	verify/probes/probe_WG9389_trialstop.py
M	verify/probes/probe_WG9390_k961r.py
M	verify/probes/probe_WG9391_k980x.py
M	verify/probes/probe_WG9392_k980g.py
M	verify/probes/probe_WG9393_endall.py
M	verify/probes/probe_WG9394_k9615.py
M	verify/probes/probe_WG9395_k960.py
M	verify/probes/probe_WG9398_rw25.py
```

（供參·⛔ 為期之代：以工項零″ 之 `commit` `ce6912dc8d044db3d5bb5449420a3c1708357ca1` 為前端之 `name-status` ⇒ `18` 列·唯塊 `Fy56` 之 `18` 檔。）

前置″ 項 `4` 之後半（同項·供參）：`git grep -c -F "<字樣>" -- app.py` 之「rw_width_mm」「rw_pct_2dp」「jump398」⇒ 各**無出艙**、`rc 1`（＝ 期·`<O>/pre/grep3.txt`）。

**執行端之所見（⛔ 裁）**：工項零″ 依本補令將本補令入倉於 `f748370` 與工項一″ 之端之間，故 `f748370..<工項一″>` 必含之（期之文亦列之）；期之列舉（`A` 一 ＋ `M` 十八）與其「恰 `18` 列」於字面相牴（`§五″` 項 `10` 之模擬之述亦載「`18` 列」）。孰為所指（例：期改為 `19` 列；或「`18`」唯指塊 `Fy56` 之列；或前端改為工項零″ 之端），執行端⛔ 判——依單首 🔴、停機款 `4″` 與 `10″` 停下（`W-G.9-392` 補令一之前例同）。

## 二、已做之工項（皆依單·逐字之首列·快轉推側支）

| 工項 | `commit` | 推送 | 內容 |
|---|---|---|---|
| 零″ | `ce6912dc8d044db3d5bb5449420a3c1708357ca1` | `verify/W-G.9-398-rw25`：`f748370` → `ce6912d`（快轉） | `docs/orders/W-G.9-398_補令一.md`（新檔·二進位複製·`git cat-file blob HEAD:…` 與來源 `cmp` 逐位同；`git check-ignore -v --no-index` 無命中 `rc 1`）·`git show --numstat` ＝ `1121`／`0`；推後 heads（濾後之母體）＝ `56`、主線 ＝ `20e03bf…` |
| 一″ | `8bc2add56c7f7201219db0064e3cdfedc30681fe` | `verify/W-G.9-398-rw25`：`ce6912d` → `8bc2add`（快轉） | 塊 `Fy56`（`<O>/Fy56.diff`·`49904` B·`89d49c8b…`·`695` 列 ＝ `§五″` 項 `2`）：`git apply --check` 過（`rc 0`）→ `git apply`（`rc 0`）→ `18` 檔之 blob 與 bytes ＝ `§五″` 項 `5`（`18／18`·`<O>/fy56_blobs.txt`）；`git status --porcelain` 唯此 `18` 檔；`git show --numstat` ＝ 閘 `1″` 之工項一″ 之列（`3`／`1`、`3`／`1`、`14`／`0`、`7`／`0`、`3`／`0`、`3`／`0`、`8`／`0`、`8`／`0`、`5`／`0`、`6`／`0`、`5`／`0`、`6`／`0`、`3`／`0`、`6`／`0`、`6`／`2`、`6`／`2`、`6`／`2`、`162`／`13`） |

- 二 `commit` 之訊息 ＝ 所令之首列逐字 ＋ 空列 ＋ 環境之尾列二列；`git commit -F`。
- 前置″ (甲)(乙)(丙)：**⛔ 跑**（停機在先·`W-G.9-392` 補令一之前例同）。工項二″〜四″：**⛔ 做**。已推之二 `commit` ⛔ 撤（`§零-2″` 末）。
- 停機時：遠端 heads（濾後之母體）＝ **`56`**；與 `<O>/heads_before_398p1.txt` 之差唯 `verify/W-G.9-398-rw25` 一列（`f748370` → `8bc2add`·其祖含 `f748370`）；主線 `wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`（⛔ 變）。
- 施工樹之 `app.py`、`verify/stepg_pipeline.py` 仍 ＝ `87e784a3…`／`0cd22fc9…`（未施）。

## 三、`§零″` 之實值

| 項 | 期 | 實 |
|---|---|---|
| 0-1 context／`nproc` | 自報 | context 餘量充足（約 `14.8M` tokens）；`nproc` ＝ `4` |
| 0-2 主線 | `20e03bf…` | `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f` ✅ |
| 0-2 側支 | `f748370…` | `f74837098ad262b941e8aa960cddca661bf1738b` ✅ |
| 0-2 heads（濾後） | `56` | `56` ✅（全列存 `<O>/heads_before_398p1.txt`） |
| 0-2 追蹤檔之變動（`--detach origin/verify/W-G.9-398-rw25` 後） | 空 | 空 ✅ |
| 0-2 三 blob | `87e784a3…`（`1895636` B）／`0cd22fc9…`（`125864` B）／`dd5a6038…` | 皆同 ✅ |
| 0-2 旗標 | `[None, None, None, None, None]` | 同 ✅ |
| 0-3 `probe_WG9321_issuer_anchor.py /tmp/w /tmp/O/issuer_anchor_pre.txt 641 640` | `rc 0`；自誤 `626`／`641`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]` | `rc 0`；「項4′ 四簿·正典框」四簿之值皆同 ✅（落檔 `sha256` `308665da…`） |
| 0-4 本補令之 bytes／`sha256`／`SELF_SHA256` | 見上 | 皆合 ✅ |
| 0-5 環境 | 匯入 `rc 0` | 初 `No module named 'shapely'` ⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`<O>/pip_install_req.txt`）⇒ 釘原單之七處、去 `tzdata`、另增二釘 `narwhals==2.27.1 fonttools==4.67.0`（`<O>/pip_pins.txt`）⇒ 六模組之匯入 `rc 0` ✅；`pip check` ⇒ `No broken requirements found.` |
| 0-6 版本之比對 | `Python 3.11.17`；`pip freeze` `sha256` `ae1438da…` | `Python 3.11.17` ✅；`pip freeze`（`<O>/freeze_final.txt`）`sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ✅ |
| 0-7 pre-flight | 🔴 `0`／🟡 `7`（具名豁免） | `rc 0`；🔴 `0`；🟡 `7`：`[P-1] :1064`、`[P-4] :69`、`:123`、`:180`、`:211`、`:1062`、`:1064` ＝ `§五″` 項 `9` 之具名豁免之七處；ℹ️ `2`：`P-5` ✅ 相符（受詞 `146785` B）；`P-3` 之 `def main` 區間（AST）＝ `23979`-`31722`（＝ `§五″` 項 `9`） |
| 塊之抽取（`§五″` 項 `2`／`4`） | 見該項 | `Fy56` `49904` B·`89d49c8b…`·`695` 列；`K47` `15535` B·`cc11da14…`·`81` 列；`E44` `3868` B·`e46c6b16…`·`22` 列；`P58` `3018` B·`302bad90…`·`16` 列——皆 ✅ |

## 四、停機款之餘

| 款 | 實 |
|---|---|
| `1″` | 合（上表） |
| `2″` | 合（`SELF_SHA256`、bytes／`sha256`、入倉 blob） |
| `3″` | 合（四塊之實得、`Fy56` 之 `apply --check` 與施後 blob `18／18`） |
| **`4″`** | **🔴 成就**（第一節） |
| `5″`〜`6″`、`8″`〜`9″`、`12″` | 未及（停機在先） |
| `7″` | 合（推送之目標唯 `verify/W-G.9-398-rw25`〔快轉二次〕與 `ops/queue`；⛔ `--force`；主線⛔ 動） |
| `10″` | 合（⛔ 改單／塊／器／命令一字） |
| `11″` | 合（本補令之入倉檔 `git check-ignore -v --no-index` `rc 1`） |
| `13″` | 合（存取與寫入皆⛔ 被拒） |

## 五、自捕與自解

1. **通則「Bash 命令⛔ 含 heredoc」之違**：本輪之 `STATE.json` 之改（接單）、塊之抽取之助手腳本（`/tmp/O/tools/extract.py`·倉外·唯依 `§五″` 末之抽取式抽塊）之寫入、`18` 檔之 blob 之對拍之助手，以 Bash 之 heredoc 為之；其後察之，本回報以檔案寫入之工具為之。抽取之結果與 `§五″` 項 `2`、`4` 逐位同；量測之命令（`issuer_anchor`、`preflight`）皆⛔ 用 heredoc。
2. 前置″ 之次序：項 `4` 為廉之檢查而先量之（⛔ 改其期·⛔ 改命令）；其不符即停，(甲)(乙)(丙) 之長跑⛔ 起（`W-G.9-392` 補令一之前例同）。
3. 本補令之複本置施工樹之根（`執行端.md` 丙 3）而以 `.git/info/exclude`（`/W-G.9-398_補令一.md`）排除之。

## 六、留待

- 發單端：前置″ 項 `4` 之期之正（列數之書法）；工項二″ 起續做。側支 `8bc2add` 之工項零″、一″ 可承（⛔ 撤）。
- 主 checkout 之同步由 KL 自行為之（README 第六節第 6 款）。
