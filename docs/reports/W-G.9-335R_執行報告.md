# `W-G.9-335R`　執行報告：主線快轉至 `be5108d` ＋ `GB-168` 之解除 ＋ `自誤 510`／`512`／`513`／`514` ＋ 待落地清單之更新

> **受單** ＝ CC 新窗·`2026-09-24`。**單** ＝ `docs/orders/W-G.9-335_輕量單.md`。**級** ＝ 輕。
> **施工處** ＝ worktree `.claude/worktrees/wg9-287-construction-window-c202df`（分支 `claude/land-readjustment-w-g-9-335-0d818d`·以 `HEAD:refs/heads/wip/s1-endpart` 推主線）。
> 本檔⛔ 載收工閘之實測值（自指）；其出艙於對話。

---

## ①　逐 `commit` 之 hash 與工項之對應

| 工項 | `commit`（全 `40` 碼） | 說明 |
|---|---|---|
| 零′ | ⛔ 無 `commit` | 遠端 `refs/heads/wip/s1-endpart`：前 `32db2c8d1835516f6f81bf87b8e00eceb3cd0d64` → 後 `be5108d0067e63e23a397fdcbe43358800381470`（`git push origin be5108d…:refs/heads/wip/s1-endpart`·快轉·⛔ `--force`） |
| 零 | `4cf99804fc84818cb7b96ff35714152a1266328c` | 本單原封入倉（新檔 `1`·`326`／`0`） |
| 一 | `3520728f9832a1951ab04a8536e6e1d2e41cebad` | 三塊之末端追加（`CLAUDE.md` `13`／`0`·`GB` 簿 `17`／`0`·自誤簿 `34`／`0`） |
| 二 | 本檔所在之 `commit`（其 hash 出艙於對話） | 本報告（新檔 `1`） |
| 三 | ⛔ 無 `commit` | 主 checkout 之同步；於本檔入倉後辦，結果出艙於對話 |

🔒 逐 `commit` 之生產碼判法（`常規一` 補款 `🔧 二`·四檔清單之 `grep -xE`）：工項零、工項一之命中皆 `0` 行（`rc 1`）⇒ 逕行 `push`。

## ②　停機款 `1`〜`8` 之三值

| # | 款 | 值 | 據 |
|---|---|---|---|
| `1` | 開工態 | 🟢 未觸發 | `origin/wip/s1-endpart` ＝ `32db2c8…`、`origin/verify/W-G.9-333-gb168` ＝ `be5108d…`；施工樹 `git status --porcelain` ＝ `0` 列 |
| `2` | 快轉 `push` | 🟢 未觸發 | 首推即成（`32db2c8..be5108d`）·⛔ `--force` |
| `3` | 快轉後出艙 | 🟢 未觸發 | 見 `③` 四項皆符 |
| `4` | 塊 bytes／`sha256` | 🟢 未觸發 | 見 `④` 三塊皆符 |
| `5` | `check-ignore` | 🟢 未觸發 | 本單 `rc 1`；本報告 `rc 1` |
| `6` | 收工閘 | 🔵 本檔⛔ 載（自指·於對話出艙） | — |
| `7` | 主 checkout | 🔵 本檔入倉後辦（於對話出艙）；入倉前預查：分支 `wip/s1-endpart`、追蹤檔變動 `0`、`app.py`／`verify/stepg_pipeline.py`／`CLAUDE.md` 之 `hash-object` ＝ 其 `HEAD` blob（⛔ 只信 `git status`） | — |
| `8` | 自判正典／改單 | 🟢 未觸發 | 本批⛔ 改單之塊與命令一字 |

## ③　工項零′ 快轉後之出艙

| # | 項 | 期 | 實 |
|---|---|---|---|
| ① | `git ls-remote origin refs/heads/wip/s1-endpart` | `be5108d0067e63e23a397fdcbe43358800381470` | `be5108d0067e63e23a397fdcbe43358800381470` ✅ |
| ② | 遠端 heads | `27` | `27` ✅ |
| ③ | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`）vs `be5108d` ／ vs `32db2c8` | `0` ／ `2` | `0` ／ `2`（`app.py`、`verify/stepg_pipeline.py`）✅ |
| ④ | `git branch -r --contains 181b5e8…` 含 `origin/wip/s1-endpart` | 含 | `origin/verify/W-G.9-333-gb168`、`origin/wip/s1-endpart` ✅ |

先驗：`git merge-base --is-ancestor 32db2c8… be5108d…` ⇒ `rc 0`。

## ④　塊 `P1`〜`P3` 之實得

抽取 ＝ 自倉內之單（`docs/orders/W-G.9-335_輕量單.md`·與來源逐位相同）依圍欄之逐列索引取圍欄內全文·末附換行；並驗其前後列確為圍欄。

| 塊 | 列 | bytes | `sha256` | 受檔 | 改前 → 改後 bytes | 嚴格前綴 ／ 檔尾 ＝ 塊 |
|---|---|---|---|---|---|---|
| `P1` | `:145`–`:161` | `2677` | `e239f453b1a0713ea02f7d38b5cbbb5a09b473c8dd304d3cfb7e7ab0c2595b8b` | `docs/reports/W-G.4_泛用阻塞項登記表.md` | `970290` → `972967` | ✅ ／ ✅ |
| `P2` | `:167`–`:200` | `3453` | `a82fd24c03a9b7327cd071f761159801dbabe1d49041be244e822436393e5fac` | `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1027019` → `1030472` | ✅ ／ ✅ |
| `P3` | `:206`–`:218` | `1116` | `63af48be51236478e15200c731796d568474e93e4a836fcbb8f87d4f96bb0b7d` | `CLAUDE.md` | `243249` → `244365` | ✅ ／ ✅ |

三塊之 `CR` ＝ `0`；三受檔改前皆以換行結尾。

## ⑤　`§五-1` 基數之重算

| # | 基數 | 單載 | 重算 |
|---|---|---|---|
| `1` | 工項數 | `5` | `5`（`§三` 之 `### 工項` 標題：零′、零、一、二、三）✅ |
| `2` | `§六` 款數 | `28` | `28`（`§六` 表之資料列 `28`；`probe_WG9321_issuer_anchor.py` 項 `9` 相異款號 `28`）✅ |
| `3` | 所鑄之號 | 裁 `0`／`GB` `0`／自誤 `4`；解除 `1` | 同（塊 `P2` 之 `### 🩸 \`自誤 N\`` 標題 `4`；塊 `P1` 解除 `GB-168` `1`）✅ |
| `4` | 停機款數 | `8` | `8` ✅ |
| `5` | 塊 | 見 `§五-1` 項 `5` | 見本檔 `④` ✅ |
| `6` | 逐筆放行清單 | 母體 `2`／動生產碼 `1` | `git rev-list 32db2c8..be5108d` ＝ `2`；動生產碼者 ＝ `181b5e8`（`app.py`、`verify/stepg_pipeline.py`）✅ |
| `7` | pre-flight | 紅 `0`／提示 `0` | 自倉重跑 `rc 0`：紅 `0`／提示 `0`；`P-5` 相符（受詞 `27258` B）；`P-3` 記錄 `def main` ＝ `15083`-`24735` ✅ |

`§零-1` 取號現查（母體 ＝ `be5108d` 全倉 `2660`／`*.md`＋`*.py` `1350`·框式逐字取單）：`W-G.9-335`、`自誤 510`／`512`／`513`／`514` 四欄皆 `0`；`W-G.9-334` ＝ `0`／`2`／`2`／`2`、`自誤 511` ＝ `0`／`1`／`1`／`1`（落點與單逐字相同）；對照甲 `W-G.9-330` ＝ `2`／`9`／`45`／`48`；對照乙四號皆 `0`；定義域 `127` 個·`MAX` `333`·⛔ 含 `399`。全與單相符。

`§一` 態錨：`probe_WG9321_issuer_anchor.py <repo> <outfile> 509 496` 於開工態主線 `rc 0`，項 `1`〜`8` 逐格與單相符（`probe_WG9330_wfns_ast.py` 主線 `rc 3`·`37`／`37`·缺 `_wg9268p_anchor_advance`）。

## ⑥　CC 之自捕

1. **量測器紅（`常規五`）**：`probe_WG9321_issuer_anchor.py` 首跑 `rc 1`，traceback 尾 ＝ `UnicodeEncodeError: 'cp950' codec can't encode character '⛔'`（於 `print`）⇒ 屬量測器紅、⛔ 受詞紅；設 `PYTHONIOENCODING=utf-8` 重跑 `rc 0`。白名單類 `5`。
2. **heredoc 被 hook 擋**：以 heredoc 寫取號現查器之命令被 `verify/tools/wg9237_heredoc_guard.py` 攔下 ⇒ 改以 `Write` 落倉外檔後以路徑呼叫；⛔ 繞過該閘。
3. 施工樹之分支於工項零′ 後以 `git reset --hard origin/wip/s1-endpart` 對齊至 `be5108d`（施工樹開工時 ＝ `32db2c8`、追蹤檔變動 `0` ⇒ 無物可失）。

## ⑦　下一 CC 窗須知

1. 主線之端 ＝ 本檔之 `commit`（其後若有工項三，⛔ 產生 `commit`）。側支 `verify/W-G.9-333-gb168` 保留（tip ＝ `be5108d…`·⛔ 刪）。
2. 本機 `probe_*` 器凡含 emoji 輸出者，一律先設 `PYTHONIOENCODING=utf-8`（`常規五`）。
3. 待落地之依賴序見 `CLAUDE.md` 檔尾「待落地清單之更新：`GB-168` 之修已入主線」節：次為 `K-9-29 二` 碼側落地（廢前置合併·生產碼·逐 `commit` 放行）。
4. 主 checkout 之根之來源檔 `W-G.9-335_輕量單.md` 由 KL 自行移除（CC⛔ 刪）。
