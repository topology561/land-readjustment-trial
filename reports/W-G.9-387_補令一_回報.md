# `W-G.9-387` 補令一 回報（執行端·完成）

**結果** ＝ 完成（停機款 `1″`〜`10″` 皆未觸）。
**主線** `wip/s1-endpart`：`34736ab959e3d6915abf94bda3977063bf2711e5` → **`fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753`**（快轉·⛔ `--force`）。
**側支** `verify/W-G.9-387-k961h`：`6dae569e97b3f58ba4a6128783c9eaaf26a38bba` → `405cb7499ae5c18cc195c3c1754793d1a1c7f1c6` → `fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753`（皆快轉·保留）。
**執行報告**（倉內）＝ `docs/reports/W-G.9-387R_K-9-61之八之落地_執行報告.md`（＋ 同目錄之 `W-G.9-387R_K-9-61之八之落地_app差異.diff`）。
**主 checkout 之同步** 由 KL 自行為之（README 第六節第 `6` 款）。
**`<O>`** ＝ `/tmp/o387p1`（倉外）；施工樹 ＝ `/tmp/w`。effort ＝ `high`。

## 一、`commit` 與推送

| 工項 | `commit` | 首列（逐字） | 推送 |
|---|---|---|---|
| 零″ | `405cb7499ae5c18cc195c3c1754793d1a1c7f1c6` | `W-G.9-387 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼` | `6dae569..405cb74  HEAD -> verify/W-G.9-387-k961h` |
| 一″ | `fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753` | `W-G.9-387 補令一 工項一″：執行報告入倉（原單工項四之補·側支）⛔ 零生產碼` | `405cb74..fd9ef0f  HEAD -> verify/W-G.9-387-k961h` |
| 二″ | （⛔ `commit`） | — | `34736ab..fd9ef0f  fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753 -> wip/s1-endpart` |

`commit` 訊息 ＝ 首列 ＋ 空一列 ＋ 環境所附之尾列（`Co-Authored-By`、`Claude-Session`）。

## 二、`§零″`（摘·全文見執行報告 ③）

主線 `34736ab…`、側支 `6dae569…`、heads `47`、施工樹追蹤檔無變動、旗標 `[None, None, None, None, None]`；issuer_anchor `rc 0`·四簿 ＝ 期（自誤 `608`／`623`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `76`／`79`·缺號集皆 ＝ 期）；補令 `25221` B／`f87b02d1…` ＝ `STATE`、`SELF_SHA256` `b503caee…` 相符；環境初缺 `shapely` ⇒ `python3 -m pip install -r requirements.txt --break-system-packages` 後 `rc 0`；pre-flight 🔴 `0`／🟡 `1`（`P-4` `:48` ＝ `§五″` 項 `3` 之具名豁免）／ℹ️ `2`。

## 三、工項一″（摘·全文見執行報告 ④）

- 差異檔 `4082` B·`44` 列·blob `a1d0e389268dcf6612272d208c63e048bc6a993f`（＝ `§五″` 項 `4`）。
- 檢索之重跑：塊 `CK` `1539` B `00cd3949…`、`GF` `2445` B `b11edb77…`；`checkidx` `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` `則 124；加註節 14；列 158`·重生成之檔與倉內逐位同。
- 重量甲（三呼叫）皆 `rc 0`·末列 `⇒ 紅 []；rc 0`·`stderr` `0` B；乙（`160c3f4` 之拋棄式 worktree `/tmp/s387`·已 `remove`）三呼叫皆 `rc 1`·末列逐字 ＝ 期；丙 ＝ `§一″` 項 `2` 之值（施後「之原街廓：應分配面積並列」`rc 1` 無出艙、其餘四字樣各 `app.py:1`）。

## 四、工項二″

**前置**（`<C>` ＝ `fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753`）：

| # | 期 | 實 |
|---|---|---|
| `1` | 側支 ＝ `<C>`；主線 ＝ `34736ab…` | `fd9ef0f…`；`34736ab959e3d6915abf94bda3977063bf2711e5` |
| `2` | `is-ancestor` `rc 0`；`count` `6`／反 `0`；`--merges` 空 | `rc 0`；`6`／`0`；空 |
| `3` | 命中者恰 `d2c4f65`（`app.py`） | `fd9ef0f` `0`、`405cb74` `0`、`6dae569` `0`、`d2c4f65` `1`（`app.py`）、`160c3f4` `0`、`789cccb` `0`（逐筆存 `<O>/pre3_<c>.txt`） |
| `4` | `<C>:app.py` ＝ `efae3a5a…`；對 `d2c4f65` 之 diff 空 | `efae3a5a4a918353b6db3e7d0dc61219a8741a82`；`0` 列 |

**快轉後即出艙**：

| # | 期 | 實 |
|---|---|---|
| ① | `ls-remote` 主線 ＝ `<C>` | `fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753	refs/heads/wip/s1-endpart` |
| ② | heads `47` | `47` |
| ③ | 生產碼 `34` 檔 vs `d2c4f65` `0`；vs `34736ab` `1`（`app.py`） | `<C>` 之生產碼 `1 + 33` 檔；`0`；`1`（`app.py`） |
| ④ | `--contains d2c4f65` 含 `origin/wip/s1-endpart` | `origin/verify/W-G.9-387-k961h`、`origin/wip/s1-endpart` |

## 五、收工閘（於主線之端 ＝ `<C>`）

| 閘 | 期 | 實 |
|---|---|---|
| `1″` | 零″ `132`／`0`；一″ 差異檔 `44`／`0`·報告·唯此二檔；首列逐字 | 零″ `132`／`0`（唯補令）；一″ 差異檔 `44`／`0`、報告 `138`／`0`（唯此二檔）；首列逐字 |
| `2″` | `6dae569..HEAD` 恰 `3` 列 `A`；生產碼與 `verify/` 相異 `0`；生產碼對 `34736ab` `1`；三新檔 `check-ignore` 無命中（對照 `rc 0`） | `3` 列皆 `A`（補令、差異檔、報告）；`0`；`['app.py']`；三檔皆 `rc 1`；對照 `rc 0`·`.gitignore:18:__pycache__/	verify/__pycache__/x.pyc` |
| `3″` | 三新檔 `CR` 合計 `0`（`data/V6.dxf` ＝ `12308`） | `0`／`0`／`0`（`25221`／`4082`／`13676` B）；對照 `12308` |
| `4″` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 對 `6dae569` 相異 `0`；`CLAUDE.md` `66e9c07a…`；`K-6` 典 `a880ba93…` | 相異 `0`；`66e9c07af114da5cbe3eaff30c78008540c2836f`；`a880ba93f826ad3ce3bf79c4dfe910fd16c43b0c`（註：`docs/待落地清單.md` 於 `6dae569` 與 `<C>` 皆不存在·故相異 `0`） |
| `5″` | heads `47`；主線 ＝ 側支 ＝ `<C>`；其餘 `44` 列逐列 ＝ 開工時 | `47`；皆 `fd9ef0f…`；`44`／`44` 同（`ops/queue` 於量時 ＝ `ed619ea`） |
| `6″` | `closegate 623 622 .` `rc 0`·`✅ 二閘皆過`；`624 623` `rc 7` | `rc 0`·`✅ 二閘皆過`·`stderr` `0` B；`rc 7` |
| `7″` | issuer_anchor `rc 0`·四簿 ＝ `§零″` 項 `3` | `rc 0`·`stderr` `0` B；自誤 `608`／`623`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `76`／`79`·缺號集同 |
| `8″` | `13` 呼叫皆 `rc 0`·末列 `⇒ 紅 []；rc 0`·`stderr` `0` B；`P0` 五值；`K1`〜`K18`、`X1`〜`X5` ✅ | 皆合（下表）；`P0` `75／75`（`probe_WG9363_k953 selftest`）、`74／74`（`probe_WG9375_k965 selftest`）、`35／35`（`probe_WG9357_k948 selftest`）、`31／31`（`probe_WG9373_k966 selftest`）、`29／29`（`probe_WG9373p1_partrem selftest`）；`K1`〜`K18`、`X1`〜`X5` 皆 ✅ |

閘 `8″` 之 `13` 呼叫（並行 `2`·牆鐘 `184` s）：

| # | 呼叫 | `rc` | `stderr` | 耗時 | 末列 |
|---|---|---|---|---|---|
| 1 | `probe_WG9385_k974.py selftest` | `0` | `0` B | `3` s | `⇒ 紅 []；rc 0` |
| 2 | `probe_WG9385_k974.py wiring … 158f7fe` | `0` | `0` B | `107` s | `⇒ 紅 []；rc 0` |
| 3 | `probe_WG9363_k953.py selftest` | `0` | `0` B | `2` s | `⇒ 紅 []；rc 0` |
| 4 | `probe_WG9363_k953.py wiring … 7d8e954` | `0` | `0` B | `33` s | `⇒ 紅 []；rc 0` |
| 5 | `probe_WG9367_adj4.py wiring … d7a5ea4` | `0` | `0` B | `34` s | `⇒ 紅 []；rc 0` |
| 6 | `probe_WG9370_adj4mut.py wiring … 3b35daa` | `0` | `0` B | `3` s | `⇒ 紅 []；rc 0` |
| 7 | `probe_WG9375_k965.py selftest` | `0` | `0` B | `2` s | `⇒ 紅 []；rc 0` |
| 8 | `probe_WG9357_k948.py selftest` | `0` | `0` B | `2` s | `⇒ 紅 []；rc 0` |
| 9 | `probe_WG9373_k966.py selftest` | `0` | `0` B | `2` s | `⇒ 紅 []；rc 0` |
| 10 | `probe_WG9373p1_partrem.py selftest` | `0` | `0` B | `2` s | `⇒ 紅 []；rc 0` |
| 11 | `probe_WG9387_k961h.py selftest` | `0` | `0` B | `3` s | `⇒ 紅 []；rc 0` |
| 12 | `probe_WG9387_k961h.py wiring … 34736ab` | `0` | `0` B | `3` s | `⇒ 紅 []；rc 0` |
| 13 | `probe_WG9351_intake.py selftest` | `0` | `0` B | `15` s | `⇒ 紅 []；rc 0` |

## 六、停機款之三值

| 款 | 期 | 實 |
|---|---|---|
| `1″` | 開工態與四簿、旗標、環境 ＝ 期 | 符（環境於安裝後可匯入） |
| `2″` | `SELF_SHA256`／`STATE`／入倉 blob 相符 | 符 |
| `3″` | 重量 ＝ 期；差異檔 blob ＝ `a1d0e389…` | 符 |
| `4″` | 工項二″ 前置皆符 | 符 |
| `5″` | 快轉之 `push` ⛔ 被拒、⛔ 須 `--force` | 一次即成（`34736ab..fd9ef0f`） |
| `6″` | 快轉後 ①〜④ ＝ 期 | 符 |
| `7″` | 零″、一″ 推至 `verify/W-G.9-387-k961h`；二″ 推至 `wip/s1-endpart` 且值 ＝ `<C>` | 符 |
| `8″` | 收工閘 ＝ 期 | 符 |
| `9″` | ⛔ 自判、⛔ 改器／命令；新檔⛔ 為 `check-ignore` 所命中 | 未觸 |
| `10″` | 存取與寫入⛔ 被拒 | 未觸（無被拒） |

## 七、自捕與自解

1. 依賴未裝（`shapely` 缺）⇒ 依 README 第六節第 `2` 款裝之（`§零″` 項 `5` 所許）。
2. 工項一″ 丙之 `git grep -c` 以 `commit` 為受詞時之出艙帶 `<commit>:` 前綴；命令之固有形、計數值 ＝ 期；照實載入執行報告。
3. 收工閘 `2″`／`3″` 之自寫之量測腳本初以 `git diff --name-status` 之引號化之路徑名（`core.quotepath` 預設）為受詞 ⇒ `check-ignore` 之受詞與 `cat-file` 之讀皆錯（讀得 `0` B）；察覺後以 `git -c core.quotepath=false` 重量（`<O>/gates_1to5_v2.txt`），上表為重量之值（初量之檔 `<O>/gates_1to5.txt` 留存）。⛔ 改倉內之器。
4. 補令於施工樹之根之副本（`執行端.md` 丙 `3`）未追蹤、⛔ 入 `commit`；結束時 `git status --porcelain` 唯此一列 `??`。

## 八、耗時（自 `clone` 起·牆鐘）

佇列與接單約 `1` 分；`§零″`（含 `pip`）約 `2` 分；工項零″、一″（含重量並行 `2`·`24` s）約 `4` 分；工項二″ 約 `1` 分；收工閘（閘 `8″` 並行 `2`·`184` s）約 `4` 分；合計約 `12` 分。
