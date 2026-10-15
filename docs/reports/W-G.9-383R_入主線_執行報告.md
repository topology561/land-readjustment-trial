# `W-G.9-383R`　入主線：執行報告（補令二·主線快轉至 `fa31382` ＋ 主 checkout 之同步）

> 受單 ＝ CC（新窗·`2026-10-15`）。施工樹 ＝ `.claude/worktrees/land-readjustment-trial-doc-27afb2`（倉之 worktree·detached）。倉外出艙 `<O>` ＝ `C:\Users\admin\AppData\Local\Temp\claude\C--Users-admin-Desktop-land-readjustment-trial--claude-worktrees-land-readjustment-trial-doc-27afb2\0c83f24f-1477-42e9-8c1f-63c10e948a32\scratchpad\O`（⛔ 在任何 git 工作樹之內：`git -C <O> rev-parse --show-toplevel` ⇒ `fatal: not a git repository`）。
> 所據 ＝ `docs/orders/W-G.9-383_補令二.md`（本補令）；所補 ＝ 原單 `§四-2`、補令一。
> **結果**：主線 `wip/s1-endpart` 由 `2663f55` 快轉至 `fa31382`（`W-G.9-383`〔`K-9-73` ④ 與 `K-9-75`〜`K-9-77` 之落地·補令一〕入主線）——**CC 之推首推即成**（未被權限分類器所擋）；其後工項零、一由 CC 推至主線。本案之配地⛔ 變。

## ①　逐 `commit`

| 序 | `commit` | 工項 | 生產碼判法 |
|---|---|---|---|
| — | **無 `commit`**：遠端 `refs/heads/wip/s1-endpart` `2663f559272a3a87af8821e54d20e689d3aebd5b` → `fa31382fab2ca953d3cce5e8d478e8166cb937b7`（快轉·納入八筆：`3f1574a`、`a9131fb`、`51ca5d8`、`a555254`、`be64c2f`、`ee60f28`、`1d50a70`、`fa31382`） | 工項零′ | 八筆中命中者唯 `ee60f28`（`app.py`、`verify/selection_pipeline.py`·`§二` 之放行清單） |
| 1 | `8966ed32cc375ad7dc63d94ccce04906deb97734` | 工項零（本補令原封入倉） | 空（唯 `docs/orders/W-G.9-383_補令二.md`·`146`／`0`） |
| 2 | 本報告之 `commit` | 工項一 | 空 |

## ②　停機款之三值

| 款 | 期 | 實 |
|---|---|---|
| `1″` | 主線 `2663f55`、側支 `fa31382`、heads `43`、追蹤檔無變動、`§零` 項 `3`、旗標 | 皆符：`git rev-parse` ＝ `2663f559…`／`fa31382f…`；heads `43`（存 `<O>\heads_before_383p2.txt`）；`git checkout --detach origin/verify/W-G.9-383-k975` 後 `git status --porcelain --untracked-files=no` 空；`probe_WG9321_issuer_anchor.py … 619 615` ⇒ `rc 0`（`stderr` `0` B）·「項4′ 四簿·正典框」＝ 自誤 `604`／`619`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `74`／`77`／`[44, 47]`；旗標 `[None, None, None, None, None]` |
| `2″` | `SELF_SHA256`；KL 之訊；來源檔；入倉 blob | 來源 ＝ KL 主 checkout 之根（第二處·施工樹之根無之）；`22090` B·`sha256` `d067def98ac83f59d6ae94a790952cfcddbe69069200046870f59d26fa7d8707`（＝ KL 之訊所載 `22090 B·sha256 d067def9…d8707`）·CR `0`·`146` 列；`SELF_SHA256` 實算 ＝ 單載 `b39ab533d04a633d937abe05f79354a56a350eab09c18270af5b69a1d1d645e1`（受詞 `22012` B）✅；二進位複製後 `cmp` 同；入倉 `git cat-file blob :docs/orders/W-G.9-383_補令二.md \| sha256sum` ＝ 來源 ✅ |
| `3″` | 工項零′ 前置 | 皆符（`③`） |
| `4″` | 工項零′ 之 `push` 被拒或須 `--force` | 未觸：`git push origin fa31382fab2ca953d3cce5e8d478e8166cb937b7:refs/heads/wip/s1-endpart` ⇒ `rc 0`·`2663f55..fa31382  fa31382fab2ca953d3cce5e8d478e8166cb937b7 -> wip/s1-endpart`（快轉·⛔ `--force`） |
| `5″` | 快轉後之出艙 ①〜④ | 皆符（`③`） |
| `6″` | 工項零、一之 `push` 之目標 | 皆 `wip/s1-endpart`（`HEAD:wip/s1-endpart`·快轉）；⛔ 推側支 |
| `7″` | 收工閘 | 實測值出艙於對話（⛔ 寫入本檔·自指） |
| `8″` | 工項二 | 於收工閘之後·出艙於對話 |
| `9″` | ⛔ 改器、命令；新檔之 `git check-ignore -v --no-index` | 未改；本補令 ⇒ `rc 1`（無命中）；本報告見收工閘 `2″` |

## ③　工項零′ 之出艙

前置（施工樹·`fa31382`·`<O>\ff_pre.txt`）與快轉後（`git fetch origin` 之後·`<O>\ff_post.txt`）之全文：附錄（出艙檔之機械抽取）。要點：
- 前置 `1`：`is-ancestor` `rc 0`；`2663f55..fa31382` `8`、反向 `0`；`--merges` 空。
- 前置 `2`：`git diff --name-only 2663f55 fa31382 -- app.py ":(glob)verify/*.py"` ⇒ 恰 `app.py`、`verify/selection_pipeline.py`；`fa31382:app.py` ＝ `f4cb5910b9ebaf52e1030a686a28c162a592ea3f`、`verify/selection_pipeline.py` ＝ `cf1d8e41d81ad9e17f1bc3817df58302d8207176`、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`。
- 前置 `3`：逐筆之判，命中者恰 `ee60f286c42b1e17920ad14328672e69388a2876`（`app.py`、`verify/selection_pipeline.py`·`2` 列）；餘七筆之出艙皆空。
- 快轉後 ①：`refs/heads/wip/s1-endpart` ＝ `fa31382fab2ca953d3cce5e8d478e8166cb937b7`；② heads `43`；③ 生產碼 `34` 檔（`app.py` `1` ＋ `verify/*.py` `33`）vs `fa31382` 相異 `0`、vs `2663f55` 恰 `app.py`、`verify/selection_pipeline.py`；④ `git branch -r --contains ee60f28…` ＝ `origin/verify/W-G.9-383-k975`、`origin/wip/s1-endpart`。

## ④　放行（KL 之逐字·本補令 `§二` 所載）

- 入主線之請示（發單側窗八十六·`2026-10-15`）：附畫面核對之步驟（退縮 `3.5 m`／`0 m`·手冊先行之紀錄之首增再試之列三·皆「未成」·總列數 `37`／`46`），並明載核對無誤後回覆放行之原話。
- **KL 之語**（`2026-10-15 14:40`·`Asia/Taipei`）：「383 畫面核對無誤，准入主線」
- 所放行之生產碼之 `commit`：`ee60f286c42b1e17920ad14328672e69388a2876`（`app.py`、`verify/selection_pipeline.py`）；土地後果：本案配地⛔ 變（唯手冊先行之紀錄之首增再試之列三）。
- KL 於本窗之訊：本補令之路徑，附「位元組數：`22090` B」「`sha256`：`d067def98ac83f59d6ae94a790952cfcddbe69069200046870f59d26fa7d8707`」。

## ⑤　pre-flight

`python verify/probes/probe_order_preflight.py <本補令>`（態 `fa31382`）⇒ `rc 0`·`stderr` `0` B：🔴 機械 `0` 項；🟡 提示 `1` 項——`[P-2] :43`（框⛔ 無 `^` 錨而同段未依 `CLAUDE.md:725` 二數並報）⇒ **處置 ＝ 本補令 `§五` 項 `3` 之具名豁免**（`§一` 項 `1` 之計數皆 git 之物件之計數，非號之占用之框；與發單側之出艙同項同列）；ℹ️ 記錄 `2` 項（`P-5` `:146` `SELF_SHA256` ✅ 相符·受詞 `22012` B；`P-3` `app.py` 之 `def main` 區間〔AST〕＝ `22870`–`30590`·本補令⛔ 用）。新名之占用（`fa31382` 之追蹤檔·`git grep -l -F`）：`W-G.9-383_補令二` `0`、`W-G.9-383R_入主線` `0`。

## ⑥　自捕與自解

- 自捕：施工樹開工時停於本窗之分支 `claude/land-readjustment-trial-doc-27afb2`（`6cb77b7`·落後主線甚多）⇒ 依 `§零` 項 `2` 一律 `git checkout --detach origin/verify/W-G.9-383-k975`、其後 `origin/wip/s1-endpart`，⛔ 用該分支之工作區。
- 自捕：`§零` 項 `3` 之器之輸出檔與其 `stdout` 非逐位同（`cmp` 相異）——`diff` 之差唯輸出檔首之表頭 `4` 列（器名·開工態 `fa31382…`）與 `stdout` 末之「[落檔] … sha256=…」等 `3` 列；其餘逐位同 ⇒ 四簿之值（「項4′」段）二者同；⛔ 礙。
- 自解：無。

## ⑦　各段耗時

| 段 | 耗時 |
|---|---|
| 開場・pre-flight | 約 `2` 分 |
| 工項零′ 前置・快轉・快轉後之出艙 | 約 `1` 分 |
| 工項零・工項一 | 約 `3` 分 |

---

## 附錄（出艙之抽取·逐位）

### 工項零′ 前置（`<O>\ff_pre.txt`）

````text
## 1
is-ancestor rc=0
count fwd=8
count rev=0
merges=[]
## 2
app.py
verify/selection_pipeline.py
app.py=f4cb5910b9ebaf52e1030a686a28c162a592ea3f
selection=cf1d8e41d81ad9e17f1bc3817df58302d8207176
stepg=2bb2f56ecf9423a99c522ddfbdfb55f314854e27
## 3
-- fa31382fab2ca953d3cce5e8d478e8166cb937b7
-- 1d50a707884d8e1df718db7fad016f938a1b419a
-- ee60f286c42b1e17920ad14328672e69388a2876
app.py
verify/selection_pipeline.py
-- be64c2f643672c4361e4451bb8f9c854613a2252
-- a5552542164a10030fbae66ebb024454b5012840
-- 51ca5d8c0db7832be5b9e4a6f6d429fe854f74cb
-- a9131fb766ecbbcadab23b9c3dc263b58aa5f8e8
-- 3f1574a1be15f12c0e8d9fc55b5590bc9625ba19
````

### 快轉後之出艙 ①〜④（`<O>\ff_post.txt`）

````text
① fa31382fab2ca953d3cce5e8d478e8166cb937b7	refs/heads/wip/s1-endpart
② heads=43
③ prod files=34 / ls-tree=1+33
③ vs fa31382:
③ vs 2663f55:
app.py
verify/selection_pipeline.py
④
  origin/verify/W-G.9-383-k975
  origin/wip/s1-endpart
````
