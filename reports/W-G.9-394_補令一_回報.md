# `W-G.9-394_補令一` 執行端回報（停機上呈·停機款 `4″`）

- 單：`ops/queue` 之 `orders/W-G.9-394_補令一.md`（`91807` B·`sha256` `4daafece1c62bf6feb1715a6cdd6cc86b11559d330593b76b90a5f92ee0349d4` ＝ `STATE.json`；`SELF_SHA256` 依 `P-5` 口徑自驗 ＝ `7cce1d0facedb0f33a1a778e41a8eb9c27398e8505274d357d383d09d3efe694`·相符）
- 結果：**停機上呈**（停機款 `4″`：前置″ 項 `4` 之期不符）。工項二″（生產碼）**未施、未 `commit`、未推**；工項三″、四″ 未做。
- 土地後果：**無**（生產碼一字未動；本停機屬單之文字與倉態之不一，非域上判斷）。
- 施工樹：`/tmp/w`（雲端完整複本）；`<O>` ＝ `/tmp/O`（倉外）。effort ＝ `high`。

## 一、停機款之三值

| 款 | 期（單之原文） | 實 |
|---|---|---|
| `4″`（前置″ 項 `4`） | 「`git diff --stat 9e25177 HEAD` 之出艙唯塊 `Fy51` 之 `1` 檔（入報告）」 | 出艙 **`2` 檔**：`docs/orders/W-G.9-394_補令一.md`（`620` 增·工項零″ 依單入倉之本補令）、`verify/probes/probe_WG9394_k9615.py`（`157` 增）；`2 files changed, 777 insertions(+)` |

出艙之全文（`/tmp/O/pre/diffstat_9e25177_HEAD.txt`）：

```text
 ....9-394_\350\243\234\344\273\244\344\270\200.md" | 620 +++++++++++++++++++++
 verify/probes/probe_WG9394_k9615.py                | 157 ++++++
 2 files changed, 777 insertions(+)
```

`git log --oneline 9e25177..HEAD`：`9a952c9`（工項一″）、`bf363f4`（工項零″）。`git diff --name-status 9e25177 HEAD`：`A docs/orders/W-G.9-394_補令一.md`、`M verify/probes/probe_WG9394_k9615.py`。

**證據**：前置″ 之「工項一″ 之端」依單必含工項零″ 之 `commit`（本補令原封入倉·單 `§四-1″` 工項零″·收工閘 `1″` 亦載「工項零″ ＝ 本補令之增」），故 `9e25177..HEAD` 必含本補令之新檔。單之期「唯塊 `Fy51` 之 `1` 檔」與此不合。執行端⛔ 判何者為正（單之筆誤抑另有所指），依停機款 `4″`（「工項二″ 之前置″ 之任一期不符」）停下。

## 二、已做之事與其實值

### `§零-0″` 開場（皆合期）

1. context 餘量充足（約 `14.8M` tokens）；`nproc` ＝ `4`。
2. `origin/wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`；`origin/verify/W-G.9-394-k9615` ＝ `9e2517717d8b67587813760ef5ada6b3ef350a3e`；heads（濾後之母體）＝ `54`（全列存 `/tmp/O/heads_before_394p1.txt`）；`git checkout --detach origin/verify/W-G.9-394-k9615` 後 `git status --porcelain --untracked-files=no` ＝ 空；`app.py` 之 `git hash-object` ＝ `d91f6ee81f25eed01551e60774f26105c3186c45` ＝ `git rev-parse 5d2a283:app.py`；旗標之出艙 ＝ `[None, None, None, None, None]`。
3. `probe_WG9321_issuer_anchor.py /tmp/w /tmp/O/anchor_open.txt 637 636` ⇒ `rc 0`；項4′ 四簿：自誤 `622`／`637`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（皆合）。
4. bytes／`sha256`／`SELF_SHA256` 皆合（見首）。
5. 環境：初無 `shapely` ⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`·`/tmp/O/pip_install.txt`）；異於基準之七處同原單所載（`certifi 2026.10.23`、`pandas 3.1.0`、`python-dateutil 3.0.0`、`streamlit 1.66.1`、`tzdata 2026.5`、`websockets 17.3` 等）⇒ 依原單 `§零-0` 項 `5` 之命令逐字釘回（`rc 0`·`/tmp/O/pip_pin.txt`）與 `pip uninstall -y tzdata`（`rc 0`·`/tmp/O/pip_untz.txt`）；其後 `import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas` ⇒ `rc 0`。
6. 版本之比對：`python3 --version` ＝ `Python 3.11.17`；`pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ＝ `基準/5d2a2836617bc2aea57f0c7513e67d9b2313f7f7.md` 所載；主線之端 ＝ 基準之 sha ⇒ 前置″ (丙) 之沿用之前提成立（因停機，(丙) 未及用）。
7. pre-flight：🔴 機械 `0`／🟡 提示 `1`（`[P-4] :185` 收工閘之表之首 ＝ `§五″` 項 `9` 之具名豁免）；`P-5` ✅；`P-3` `def main` ＝ `23812`-`31555`。
8. `reports/W-G.9-394_規格單_回報.md` ＝ `38607` B·`df29afec…`；抽出之 `/tmp/O/rep394.diff` ＝ `4614` B·`82b505e634c6defbe7f87bbf4bdeeac1ff139d98f539005e9d1447870163e0d7`·`63` 列（合 `§五″` 項 `3`）。

### 塊之實得（皆合 `§五″` 項 `2`／`4`、原單 `§五-1` 項 `4`）

| 塊 | B | `sha256` | 列 |
|---|---|---|---|
| `Fy51` | `12081` | `8aba075f67d2760a13d166da546af0bc8c6c0e6334a52f6c3cc430f98ab83946` | `189` |
| `K42` | `10773` | `e67c21bd13d377d3ecb2f39f15c544655a8d31fa73751f2db1e7a875e6ab0373` | `41` |
| `P53` | `1965` | `ce5abdda50c70588741999e17ce488b3d353b9932b34ec8260311f039f87796e` | `15` |
| `E41` | `2361` | `4870fc7ae3f705a943b62915b55059e7dcec865ac36fb38298ec7cad0ff78bce` | `12` |
| `K41`（原單） | `13280` | `2440cfd5…` | `62` |
| `P52`（原單） | `3164` | `f7103308…` | `18` |
| `E40`（原單） | `1381` | `ce34b2b8…` | `12` |
| `G18`（原單） | `1436` | `817a345b…` | `9` |

### 已推之 `commit`（新側支 `verify/W-G.9-394-k9615`·快轉·⛔ 撤）

| 工項 | `commit` | 內容 | 推送 |
|---|---|---|---|
| 零″ | `bf363f4` | `docs/orders/W-G.9-394_補令一.md`（新檔·`git cat-file blob` 與來源逐位同·`check-ignore` `rc 1`） | `9e25177..bf363f4`；推後 heads（濾後）`54`、主線仍 `5d2a283` |
| 一″ | `9a952c9` | `Fy51` 施於 `probe_WG9394_k9615.py`：施前 `411b7e0f…`（`24816` B）→ 施後 `1a6f2b7cefa32ac6476bc1d041ec29b3dd314647`（`34926` B）；`git status` 唯此 `1` 檔 | `bf363f4..9a952c9` |

現態：`verify/W-G.9-394-k9615` ＝ `9a952c949c931286512b65e6539539cc1c245857`；`wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`（⛔ 動）。

### 前置″（於 `9a952c9`·`/tmp/O/pre/`·並行 `2`·殼無 `WV_`）

項 `4` 之其餘：`git grep -c -F "W-G.9-394" -- app.py` ⇒ 無出艙·`rc 1`（合）；`git grep -c -F "K-9-61 ⑤" -- app.py` ⇒ `app.py:5`·`rc 0`（合）。

(甲)(乙) 之 `14` 呼叫（雖已見項 `4` 之不合，因皆唯讀之量測，跑畢以供復驗之參考）——**皆合 `§五″` 項 `8` 之「工項一″ 之端」之列**：

| # | `rc` | `stderr` B | 末列 | s |
|---|---|---|---|---|
| `5` | 0 | 0 | `⇒ 紅 []；rc 0` | 28 |
| `6` | 0 | 0 | `⇒ 紅 []；rc 0` | 29 |
| `69` | 0 | 0 | `⇒ 紅 []；rc 0` | 2 |
| `73` | 0 | 0 | `⇒ 紅 []；rc 0` | 2 |
| `82` | 0 | 0 | `⇒ 紅 []；rc 0` | 4 |
| `85` | 1 | 0 | `⇒ 紅 ['T1', 'T1b', 'T1c', 'T2', 'T8', 'T9', 'T9d', 'T9e', 'T10', 'T11', 'T12', 'T12b', 'T13', 'T13c', 'T14']；rc 1` | 2 |
| `86` | 1 | 0 | `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W8']；rc 1` | 4 |
| `87` | 0 | 0 | `⇒ 紅 []；rc 0` | 392 |
| `56` | 0 | 0 | （JSON 之摘要列·`"SB": 3.5, "err": null, "n": 35`·`stage3_log_rows` `19`） | 233 |
| `57` | 0 | 0 | （JSON 之摘要列·`"SB": 0.0, "err": null, "n": 36`） | 164 |
| `58` | 0 | 0 | `⇒ 紅 []；rc 0` | 225 |
| `59` | 0 | 0 | `⇒ 紅 []；rc 0` | 167 |
| `60` | 0 | 0 | `⇒ rc 0（不符 0 項）` | 516 |
| `61` | 0 | 0 | `⇒ rc 0（不符 0 項）` | 377 |

`f8_pre_35.json` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、`f8_pre_00.json` ＝ `884e91714a79288406faa4def6518847de36de39`（皆合）。

另：`git apply --check /tmp/O/rep394.diff` 於 `9a952c9` ⇒ 過（唯 `--check`·未施·樹淨）。

## 三、README 第六節之平台事項

- 直譯器 `python3`、路徑 Linux 絕對路徑、並行 `2`（README 第六節第 1、3 款）；主 checkout 之同步由 KL 自行為之（第 6 款）。

## 四、自捕與自解

- 首次推 `ops/queue`（接單）被拒（非快轉：發單端之門鈴之記 `0fcea57`）⇒ 重取、`rebase` 後推成（`9aea210`·⛔ `--force`）。
- 工項二″ 之 `commit` 未生 ⇒ 無差異可附（`R-0″` 之差異 ＝ 佇列之 `reports/W-G.9-394_規格單_回報.md` 之 ⑧·原封未動）。

## 五、耗時

開場至工項一″ 約 `6` 分；前置″ (甲)(乙) `14` 呼叫（並行 `2`）`04:27:21`〜`04:47:57`（UTC）約 `21` 分。

## 六、請發單端裁示之事

前置″ 項 `4` 之期（「唯塊 `Fy51` 之 `1` 檔」）與工項零″ 必入倉之本補令之新檔如何並讀——執行端⛔ 自裁。新側支已推之 `bf363f4`、`9a952c9` 照留；續做時可自 `9a952c9` 接續（前置″ (甲)(乙) 之落檔在本容器，容器為暫存，續做之輪宜重跑）。
