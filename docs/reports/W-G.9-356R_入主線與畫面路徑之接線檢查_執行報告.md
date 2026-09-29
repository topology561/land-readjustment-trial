# `W-G.9-356R`　入主線與畫面路徑之接線檢查：執行報告

> **單** ＝ `docs/orders/W-G.9-356_輕量單.md`。**受單** ＝ CC。**級** ＝ 輕（本批⛔ 跑 `run_all` 及 `run` 類之量·依單）。
> **分支** ＝ 主線 `wip/s1-endpart`：`0b05925374f2de46c2493f5f56ef64667a2fed1d` →（工項零′ 快轉）`1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f` → 工項零〜三之零生產碼 `commit`。側支 `verify/W-G.9-353-endmerge` 留於 `1ef3bb5…`（⛔ 再推）。
> **量測環境** ＝ Windows 11·Python 3.13.11·Git Bash；殼⛔ 設 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6`（出艙 `[None, None, None]`）。
> **收工閘**（`§四`）之實測值與**工項四**（主 checkout 之同步）之出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 異動（`git show --numstat`） |
|---|---|---|
| 零′　主線快轉 | **無 `commit`**；遠端 ref `refs/heads/wip/s1-endpart`：`0b05925374f2de46c2493f5f56ef64667a2fed1d` → `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`（`git push origin 1ef3bb5…:refs/heads/wip/s1-endpart`·快轉·⛔ `--force`） | 所納 `15` 筆（見 ③-1） |
| 零　本單原封入倉 | `475414d0e55377509abb9bff883cf6c81b1feca7` | `docs/orders/W-G.9-356_輕量單.md` 增 `885`／刪 `0`（新檔） |
| 一　量測器 `F15` | `1cf82a980493275c3a8d76301f169201d9b35c90` | `verify/probes/probe_WG9356_screenmerge_wiring.py` 增 `605`／刪 `0`（新檔） |
| 二　塊 `P10` | `4aa6b507f7b5308254a6ea7cb5bb354897db2c09` | `CLAUDE.md` 增 `20`／刪 `0` |
| 三　本報告 | （本檔所在之 `commit`·自指 ⇒ 見對話） | 本檔（新檔） |

## ② 停機款 `1`〜`13` 之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `0b05925`、側支 ＝ `1ef3bb5`、施工樹追蹤檔無變動、heads ＝ `31` | 主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`；`git status --porcelain --untracked-files=no` 空；heads `31` ⇒ ⛔ 觸 |
| `2` | 本單 bytes／`sha256` ＝ `§五-1`；來源存在；入倉 blob 與來源逐位同 | 來源取於第二處（KL 主 checkout 之根·施工樹之根無）；`68511` B·`sha256` `3785118b5463743026b1fdb7df83814460be0ccc45eec6575b19e206bd092184`·`CR` `0`；`SELF_SHA256`（`P-5` 原口徑·受詞 `68433` B）單載 ＝ 實算 ＝ `3460118bc977366c7c339ce4d98c67a59f963b4fb11ae34577e04bf92899181d`；入倉 blob 與來源 `==` ⇒ ⛔ 觸 |
| `3` | 工項零′ 前置 `1`〜`3` 皆 ＝ 期 | 見 ③-1 ⇒ ⛔ 觸 |
| `4` | 快轉之 `push` 不被拒、⛔ 須 `--force` | `0b05925..1ef3bb5  1ef3bb5… -> wip/s1-endpart`·`rc 0` ⇒ ⛔ 觸 |
| `5` | 快轉後之出艙 ①〜④ 皆 ＝ 期 | 見 ③-2 ⇒ ⛔ 觸 |
| `6` | 塊 `F15`／`P10` 之 bytes／`sha256` ＝ `§五-1` | 見 ⑤ ⇒ ⛔ 觸 |
| `7` | 工項一之必過 `rc 0`／必破 `rc 1`（末列 ＝ `§一` 項 `6`）；二態全文 ＝ 塊 `T1`／`T2` | 必過 `rc 0`；必破 `rc 1`·末列逐字相同；二態與 `T1`／`T2` 逐列相同（去 CR 及列尾空白）⇒ ⛔ 觸 |
| `8` | `CLAUDE.md` 刪除欄 `0`、嚴格前綴 | 刪除欄 `0`；`295353` → `299948`·嚴格前綴 `True` ⇒ ⛔ 觸 |
| `9` | `§四` 收工閘皆 ＝ 期 | 於本檔之 `commit` 推後量——出艙於對話 |
| `10` | 工項四之諸款 | 於收工閘之後辦——出艙於對話 |
| `11` | 工項零〜三之 `push` 目標恆 ＝ `wip/s1-endpart`；⛔ 推側支 | `475414d`／`1cf82a9`／`4aa6b50` 皆 `HEAD:wip/s1-endpart` 快轉；側支⛔ 推 ⇒ ⛔ 觸 |
| `12` | ⛔ 作「孰為正典」之判；⛔ 改塊、器、命令一字 | 未作；塊與器皆逐位原封；命令逐字（`<repo>` 以反斜線之絕對路徑傳入） |
| `13` | 新檔⛔ 為 `git check-ignore` 所命中 | `docs/orders/W-G.9-356_輕量單.md` `rc 1`；`verify/probes/probe_WG9356_screenmerge_wiring.py` `rc 1`；本檔 `rc 1`（入倉前驗）⇒ ⛔ 觸 |

## ③ 工項零′ 之出艙

### ③-1　前置 `1`〜`3`（含逐筆判之空輸出）

```text
== 前置 1
is-ancestor rc=0
count 0b05925374f2de46c2493f5f56ef64667a2fed1d..1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f = 15
count 1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f..0b05925374f2de46c2493f5f56ef64667a2fed1d = 0
== 前置 2
app.py
verify/selection_pipeline.py
verify/stepg_pipeline.py
(列數 3)
判別力：無 :(glob) 之形 ⇒ 7 列
1ef3bb5:app.py = e11232a6569bf33c7b2b7f15da989873a06ff28c
== 前置 3（逐筆·含空輸出）
-- 655c6e34d23bd66078fb7c48637ee752ef90b979 命中 0 列 :: W-G.9-353 工項零：本單原封入倉（側支）⛔ 零生產碼
-- 576708c1013836f8ff6f3bf2a6b8c78bf13fe549 命中 0 列 :: W-G.9-353 工項一：量測器 F12（末端塊之合併再試與強制抵費地）入倉（側支）⛔ 零生產碼
-- c970ae60d092e8e803a3d156db2434c4f617c204 命中 3 列 :: W-G.9-353 工項二：末端塊之合併再試與強制抵費地（K-9-49 ②·K-9-36 ③）之 harness 路徑 🔴 生產碼（側支）
     app.py
     verify/selection_pipeline.py
     verify/stepg_pipeline.py
-- 83d34209a224b168b66e63137cadea4cdd1aacd4 命中 0 列 :: W-G.9-353 工項三：K-9-49 ②·K-9-36 ③ 之落地狀態 ＋ 待落地清單之更新（側支）⛔ 零生產碼
-- 928d2920702bc128cc973ddfb3b234d83a4b05bc 命中 0 列 :: W-G.9-353 工項四：執行報告入倉（側支）⛔ 零生產碼
-- cd3c29f1f2b555b8325077f6f48aff8eb2e58ef2 命中 0 列 :: W-G.9-354 工項零：本單原封入倉（側支）⛔ 零生產碼
-- 758cfbacc99c456247293a9a0ef9b1325e5661e1 命中 0 列 :: W-G.9-354 工項一：量測器 F13（數末端塊之競合·K-9-50）入倉 ＋ F12 之更新（側支）⛔ 零生產碼
-- a44a3868342bf32e1c6f409ace79e61b82e83896 命中 1 列 :: W-G.9-354 工項二：數末端塊之合併再試相互競合（K-9-50）之 harness 路徑 ＋ 後處理之承前 🔴 生產碼（側支）
     app.py
-- 9e744db0664903f1bcd14b4faa6cba09bbec27ee 命中 0 列 :: W-G.9-354 工項三：K-9-50 之入典 ＋ 攢批登記（自誤 546／547·GB-194）＋ 待落地清單之更新（側支）⛔ 零生產碼
-- f55935cb95b5e6c058231ee89d5dd19e3a291456 命中 0 列 :: W-G.9-354 工項四：執行報告入倉（側支）⛔ 零生產碼
-- 31f03d3d01902462409a20058f95d78a8fe7604e 命中 0 列 :: W-G.9-355 工項零：本單原封入倉（側支）⛔ 零生產碼
-- 167e475d480c657fa3d0ff27189b16ee278dbb2d 命中 0 列 :: W-G.9-355 工項一：量測器 F14（末端塊合併再試之畫面路徑）入倉 ＋ F4 之更新（側支）⛔ 零生產碼
-- f173a4e2a54d1ae036e14ecc35e88d0a9befdf31 命中 1 列 :: W-G.9-355 工項二：末端塊之合併再試（含 K-9-50）之畫面路徑 🔴 生產碼（側支）
     app.py
-- b1d3d3b7977d455f0239bc4768975137f30ce2e0 命中 0 列 :: W-G.9-355 工項三：攢批登記（自誤 548）＋ 待落地清單之更新 ＋ 恆常附款 n③ 之試行期變通（側支）⛔ 零生產碼
-- 1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f 命中 0 列 :: W-G.9-355 工項四：執行報告入倉（側支）⛔ 零生產碼
```

⇒ 命中 ≥ `1` 列者恰 `3` 筆（`c970ae60d092e8e803a3d156db2434c4f617c204`／`a44a3868342bf32e1c6f409ace79e61b82e83896`／`f173a4e2a54d1ae036e14ecc35e88d0a9befdf31`）＝ `§二` 逐筆放行清單。

### ③-2　快轉後之出艙 ①〜④

```text
① 1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f	refs/heads/wip/s1-endpart
② heads 31
   vs 0b05925 相異：app.py
   vs 0b05925 相異：verify/selection_pipeline.py
   vs 0b05925 相異：verify/stepg_pipeline.py
③ 受檢 34 檔；vs 1ef3bb5 相異 0；判別力 vs 0b05925 相異 3
④   origin/verify/W-G.9-353-endmerge   origin/wip/s1-endpart 
```

其後施工樹 `git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`。

### ③-3　開場之取號現查（`§零-1`）與 pre-flight（`§零-3`）

`python verify/probes/wg9268_gate6_occupancy.py 1ef3bb5 W-G.9-356 W-G.9-355 W-G.9-399`（`rc 0`·母體 ＝ 全 `docs/` `913` 檔·讀不到 `20`）：

```text
三軸 (1) 來源 ＝ 1ef3bb5
三軸 (2) 母體 ＝ 全 docs/ 913 檔（讀不到 20 ＝ git失敗 0 ＋ 解碼失敗 20）
三軸 (3) 粒度框 ＝ 檔框 ＋ 列框（宣告框·D1/D2/D3 三數分列）

── 受詢之號 ──
  W-G.9-356      嚴格    D1 檔=0    D2 列=0    D3 列=0    雙屬=0   列框(∪)=0    檔框=0    ｜ 鬆框 檔=0    列=0    ｜ 受詢 ⇒ 須全 0
  W-G.9-356      寬式    D1 檔=0    D2 列=0    D3 列=0    雙屬=0   列框(∪)=0    檔框=0    ｜ 鬆框 檔=0    列=0    ｜ 受詢 ⇒ 須全 0

── 對照組 甲（已知占用·須 ≥1）──
  W-G.9-355      嚴格    D1 檔=2    D2 列=7    D3 列=8    雙屬=0   列框(∪)=15   檔框=3    ｜ 鬆框 檔=6    列=62   ｜ 甲（須 ≥1）
  W-G.9-355      寬式    D1 檔=2    D2 列=7    D3 列=8    雙屬=0   列框(∪)=15   檔框=3    ｜ 鬆框 檔=6    列=62   ｜ 甲（須 ≥1）
  W-G.9-399      嚴格    D1 檔=0    D2 列=0    D3 列=0    雙屬=0   列框(∪)=0    檔框=0    ｜ 鬆框 檔=2    列=3    ｜ 甲（須 ≥1）
  W-G.9-399      寬式    D1 檔=0    D2 列=0    D3 列=0    雙屬=0   列框(∪)=0    檔框=0    ｜ 鬆框 檔=2    列=3    ｜ 甲（須 ≥1）

── 對照組 乙（人造·執行期組出·代稱 ⟨NEG⟩·須 =0）──
  W-G.9-963      嚴格    D1 檔=0    D2 列=0    D3 列=0    雙屬=0   列框(∪)=0    檔框=0    ｜ 鬆框 檔=16   列=17   ｜ 乙（須 =0）
  W-G.9-963      寬式    D1 檔=0    D2 列=0    D3 列=0    雙屬=0   列框(∪)=0    檔框=0    ｜ 鬆框 檔=16   列=17   ｜ 乙（須 =0）
   ⟨NEG⟩ 之六數 = [0, 0, 0, 0, 0, 0] ／鬆框列 = 17

🔒 判：受詢之六數（嚴格 D1/D2/D3 ＋ 寬式 D1/D2/D3）= [0, 0, 0, 0, 0, 0]
   鬆框亦 0 ⇒ ⛔ 漏框之虞
```

`python verify/probes/probe_order_preflight.py <本單>` ⇒ `rc 0`：🔴 `0`／🟡 `5`（`P-4` `:63`／`:157`／`:330`／`:835`、`P-6` `:63`）／ℹ️ `2`（`P-5` 相符、`P-3` 區間 `19744`–`27416`）——與單 `§五-1` 項 `4` 逐項同；🟡 五項採單之具名豁免。
`python verify/probes/probe_WG9321_issuer_anchor.py <repo> <O>\anchor_pre.log 548 547` ⇒ `rc 0`（四簿：自誤 `533`／`548`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `47`／`50`·缺號集同單 `§四` 閘 `7`）。

## ④ 工項一之二態之全文

**內嵌之 log**：由落檔以程式直接嵌入（⛔ 手抄）；Windows 下 Python 之 stdout 重導為文字模式 ⇒ 落檔之行尾為 `CRLF`（孤 `CR` ＝ `0`），嵌入時正規化為 `LF`。

`python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <施工樹>`（`app.py` ＝ `e11232a6569bf33c7b2b7f15da989873a06ff28c`）⇒ **`rc 0`**（`39` s）：

```text
── 接線與合成案（AST·工作樹之 app.py）──
  ✅ W0 受詞在模組層（缺 []）
  ✅ W1 R-1 三出口（三出口皆經 _end_merge → f3_screen_end_block_merge(st, …)）
  ✅ W2 R-1 單一真相源（end_block_merge_run：呼叫 1（期 1）·在合併再試之入口 1·非呼叫之引用列 []；f3_screen_end_block_merge 之呼叫 1（期 1）·在段三之畫面入口 1）
  ✅ W3 R-5 四注入物之單一真相源（巢狀 ['a_prime', 'alloc_eval', 'alloc_state', 'trial_winner']；回四鍵 True；他處同名 []；段三：['a_prime', 'trial_winner', 'alloc_state']；合併再試：['a_prime', 'alloc_eval', 'alloc_state']）
  ✅ W4 R-3／R-4 試算 'trial'（{'alloc_state': True, 'alloc_eval': True}）
  ✅ W5 R-6 隔離（SS_END_BLOCK_MODE＝'f3_end_block_mode' ∈ 鍵 True；try 前存 True；finally 復 True；K917 ['K917_DROPPED.clear', 'K917_DROPPED.update']）
  ✅ W6 R-7 紀錄（try 後寫 rec True／log True；try 內或其前寫 False；段三之畫面入口之首去 rec True／log True）
  ✅ W7 R-12 失效之二鍵（去 SS_END_BLOCK_MERGE True；去 f3_end_block_merge_log True）
  ✅ W8 R-12 顯示之接線（if 之式 True；end_block_merge_rows(X, …get('f3_end_block_merge_log')) True；位置 True）
  ✅ S1 自誤517 顯示區塊之合成案（三情形皆符）
  ✅ S2 自誤517 失效函式之合成案（未去 []；他鍵留 True；f3_g_needs_rerun True）
── 判別力（每一突變須使其所指之項轉紅）──
  ✅ M1 出口①⛔ 辦合併再試：轉紅 ['W1']（須含 W1）
  ✅ M2 出口③以段三前之宗地辦合併再試：轉紅 ['W1']（須含 W1）
  ✅ M3 以別名呼叫單一真相源：轉紅 ['W2', 'W3', 'W5', 'W6']（須含 W2）
  ✅ M4 合併再試另寫 alloc_eval：轉紅 ['W3']（須含 W3）
  ✅ M5 合併再試之注入物錯位：轉紅 ['W3']（須含 W3）
  ✅ M6 段三之試算配地⛔ 設 'trial'：轉紅 ['W4']（須含 W4）
  ✅ M7 合併再試之試算配地⛔ 設 'trial'：轉紅 ['W4']（須含 W4）
  ✅ M8 試算旗標⛔ 入隔離之鍵：轉紅 ['W5']（須含 W5）
  ✅ M9 合併再試之 finally ⛔ 復原：轉紅 ['W5']（須含 W5）
  ✅ M10 逐列紀錄⛔ 寫：轉紅 ['W6']（須含 W6）
  ✅ M11 段三之畫面入口之首⛔ 去前次之紀錄：轉紅 ['W6']（須含 W6）
  ✅ M12 失效函式⛔ 去紀錄：轉紅 ['W7', 'S2']（須含 S2）
  ✅ M13 顯示⛔ 傳逐列：轉紅 ['W8', 'S1']（須含 S1）
  ✅ M14 顯示⛔ 出逐列表：轉紅 ['S1']（須含 S1）
⇒ 紅 []；rc 0
```

`python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <P>`（`<P>` ＝ `C:\Users\admin\AppData\Local\Temp\wgP356`·`git worktree add --detach` 於 `f55935cb95b5e6c058231ee89d5dd19e3a291456`·其 `app.py` ＝ `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`·跑畢 `git worktree remove --force`）⇒ **`rc 1`**：

```text
── 接線與合成案（AST·工作樹之 app.py）──
  🔴 W0 受詞在模組層（缺 ['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows']）
  🔴 W1 R-1 三出口（return 3（期 3）；所呼 []（期 恰 1 且為巢狀函式））
  🔴 W2 R-1 單一真相源（end_block_merge_run：呼叫 0（期 1）·在合併再試之入口 0·非呼叫之引用列 []；f3_screen_end_block_merge 之呼叫 0（期 1）·在段三之畫面入口 0）
  🔴 W3 R-5 四注入物之單一真相源（k6b_screen_callbacks 缺）
  🔴 W4 R-3／R-4 試算 'trial'（k6b_screen_callbacks 缺）
  🔴 W5 R-6 隔離（f3_screen_end_block_merge 缺）
  🔴 W6 R-7 紀錄（受詞缺）
  🔴 W7 R-12 失效之二鍵（去 SS_END_BLOCK_MERGE False；去 f3_end_block_merge_log False）
  🔴 W8 R-12 顯示之接線（`X = st.session_state.get(SS_END_BLOCK_MERGE)` ＋ if 之二句缺）
  🔴 S1 自誤517 顯示區塊之合成案（抽不到顯示區塊）
  🔴 S2 自誤517 失效函式之合成案（未去 ['f3_end_block_merge', 'f3_end_block_merge_log']；他鍵留 True；f3_g_needs_rerun True）
── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──
⇒ 紅 ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'S1', 'S2']；rc 1
```

**對塊 `T1`／`T2`**（去 `CR` 及列尾空白後逐列比）：`f15_pass.log` 對 `T1` 相異列 `0`；`f15_break.log` 對 `T2` 相異列 `0`；判別力（擾動一列 ⇒ 不等）`True`。

## ⑤ 二塊之實得與 `CLAUDE.md` 之改前改後

| 塊 | bytes | `sha256` | 列 | 圍欄（本單之列） | 落點 |
|---|---|---|---|---|---|
| `F15` | `30405` | `d56a954a30900009c9146b665958ec05a2c8b690eba02886a786e0c5acfef45a` | `605` | `198`–`804` | 新檔 `verify/probes/probe_WG9356_screenmerge_wiring.py`（blob `c489e887300d29b90c14791024bc215709390749`） |
| `P10` | `4595` | `1302e3b8a18d2069ddc36b5fe5ae0fb11e107c85bcd0acf2ee4d0d43363ad4cb` | `20` | `808`–`829` | `CLAUDE.md` 之末 |

併抽之附錄丙：`T1` `2576` B·`46dbc8e7946eaaa5790f199966834afb8ef8aa803f4b95af4a6188ac8986eb8d`·`28` 列；`T2` `1279` B·`9e97cae7ec7c7cfe4f2b4506415529f96efd47532e1ee27266a43c96e3b98947`·`14` 列（皆 ＝ 單 `§五-1` 項 `5`）。

`CLAUDE.md`：`295353` B → `299948` B；改前為改後之嚴格前綴 `True`；`CR` `0`。

## ⑥ `§二` 之放行

KL 貼本單之同一訊息，其全文逐字為二列：

```text
@"C:\Users\admin\Desktop\land-readjustment-trial\W-G.9-356_輕量單.md"
是
```

⇒ 依 `§二`（「KL 貼本單之同一訊息內逐字答『是』者，視為工項零′（主線快轉）與工項四（主 checkout 之同步）之放行」）**放行成立**；所答之【要你判斷】逐字（單 `§二`）：「同意將側支（末端塊之合併再試：harness 與畫面二路徑·W-G.9-353〜355）併入主線，並請 CC 將您本機的程式資料夾同步至主線嗎？（是／否）」。工項零′ 之前置皆符後，以與前置分開之呼叫推送。

## ⑦ CC 之自捕與自解

**自捕**：無。
（照實：`§零-0` 項 `1` 之 context 餘量已於工項零′ 之前於對話出艙——工具計數器 `14,815,520` tokens；`W-G.9-355R` ⑥ 自捕 `1` 所載之漏，本批未再犯。）
**自解清單**：無（本批未遇須自解之疑義）。

## ⑧ 各段耗時（規格單流程之試行評估之用）

時刻取自倉外落檔之修改時間與 `commit` 時間（`+0800`·約數）。

| 段 | 起訖 | 約 |
|---|---|---|
| 讀單・開場閘（refs、態錨器、本單與四塊之對拍、取號現查、pre-flight） | 起時未錄（塊之抽取 `10:17:43`）–`10:18:21` | 約 `3`〜`5` 分 |
| 工項零′（前置 `1`〜`3`、快轉、出艙 ①〜④） | `10:18:34`–`10:19:00` | `1` 分 |
| 工項零（入倉·推） | `10:19:07` | `< 1` 分 |
| 工項一（`F15` 入倉、必過 `39` s、必破、對塊、推） | `10:19:10`–`10:20:26` | `1` 分餘 |
| 工項二（`P10`·推） | `10:20:42` | `< 1` 分 |
| 報告 | `10:21`– | 見對話 |

🔒 **評估**：本批無撰碼、無長跑（單明令⛔ 跑 `run_all` 及 `run` 類）⇒ 全批約 `10` 分，耗時主項為開場閘與量測器之二態實跑。
