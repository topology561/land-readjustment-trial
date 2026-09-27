# `W-G.9-353R`　末端塊之合併再試與強制抵費地（`K-9-49 ②`·`K-9-36 ③`）之 harness 路徑（側支）：執行報告

> **受單** ＝ CC 新窗（施工樹 ＝ `.claude/worktrees/weight-unit-w-g-9-353-dcbf3a`·Windows 11）。**單** ＝ `docs/orders/W-G.9-353_重量單.md`。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；**側支** ＝ `verify/W-G.9-353-endmerge`（本批新建）。**主線⛔ 動。**
> 殼之旗標：`[None, None, None]`（`WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6`·開工時與二次 `run_all` 前各出艙一次）。
> 收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。

---

## ①　逐 `commit` 之 hash 與工項

| 工項 | `commit` | 訊息首列 | 動之檔（增／刪） |
|---|---|---|---|
| 零 | `655c6e34d23bd66078fb7c48637ee752ef90b979` | `W-G.9-353 工項零：本單原封入倉（側支）⛔ 零生產碼` | `docs/orders/W-G.9-353_重量單.md`（新檔·`1530`／`0`） |
| 一 | `576708c1013836f8ff6f3bf2a6b8c78bf13fe549` | `W-G.9-353 工項一：量測器 F12（末端塊之合併再試與強制抵費地）入倉（側支）⛔ 零生產碼` | `verify/probes/probe_WG9353_endmerge.py`（新檔·`769`／`0`） |
| 二 | `c970ae60d092e8e803a3d156db2434c4f617c204` | `W-G.9-353 工項二：末端塊之合併再試與強制抵費地（K-9-49 ②·K-9-36 ③）之 harness 路徑 🔴 生產碼（側支）` | `app.py` `161`／`11`；`verify/stepg_pipeline.py` `4`／`0`；`verify/selection_pipeline.py` `103`／`34` |
| 三 | `83d34209a224b168b66e63137cadea4cdd1aacd4` | `W-G.9-353 工項三：K-9-49 ②·K-9-36 ③ 之落地狀態 ＋ 待落地清單之更新（側支）⛔ 零生產碼` | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `20`／`0`；`CLAUDE.md` `23`／`0` |
| 四 | （本檔之 `commit`·自指·出艙於對話） | `W-G.9-353 工項四：執行報告入倉（側支）⛔ 零生產碼` | 本檔（新檔） |

各 `commit` 訊息之首列逐字同單；其後附本倉慣例之 `Co-Authored-By` 列（見 ⑥ 自解 `3`）。

---

## ②　停機款 `1`〜`11`（款·期·實）

| # | 期 | 實 | 判 |
|---|---|---|---|
| `1` | 主線 ＝ `0b05925`；追蹤檔無變動；遠端無 `verify/W-G.9-353-endmerge`；heads ＝ `30` | `git rev-parse origin/wip/s1-endpart` ＝ `0b05925374f2de46c2493f5f56ef64667a2fed1d`；`--detach` 後 `git status --porcelain --untracked-files=no` 列數 `0`；該側支命中 `0`；heads `30` | 🟢 未成就 |
| `2` | 本單 bytes／`sha256` 符 `§五-1`；來源檔可得；入倉 blob 與來源逐位同 | 來源檔取自**第二處**（KL 主 checkout 之根·施工樹之根無）；`111925` B·`sha256` `33b69bd8b14248338cdfedbda11feb1605f5e43da7605e649fec73e3fe698760`·`CR` `0`；`SELF_SHA256`（`P-5` 原口徑·受詞 `111847` B）載 `99cef36e…42a79` ＝ 實算 `99cef36e…42a79`；入倉後 `git cat-file blob HEAD:docs/orders/W-G.9-353_重量單.md \| sha256sum` ＝ `33b69bd8…98760` | 🟢 |
| `3` | 四塊之 bytes／`sha256` 符 `§五-1` | 見 ④：四塊皆逐位相符 | 🟢 |
| `4` | 工項二前置之期 | `F12` 三子命令皆 `rc 1`（末列見 ③-1）；`F8 run` 二退縮皆 `rc 0`；`run_all` 跑畢（`rc 1` ＝ 准紅碼之 `W-V run_all: FAIL`·其判由 `V-5` 之對拍承擔） | 🟢 |
| `5` | `git apply --check` 過；施後三 blob ＝ `§五-1` 項 `6` | `--check` `rc 0`（`--numstat` ＝ `161 11 app.py`／`103 34 verify/selection_pipeline.py`／`4 0 verify/stepg_pipeline.py`）；施後 `app.py` `0c7739fde995fc77b75d2deccc3a7b78f575c91b`（`1566816` B）、`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`（`121566` B）、`verify/selection_pipeline.py` `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`（`47216` B）；`py_compile` 三檔 `rc 0` | 🟢 |
| `6` | `V-1`〜`V-5` 皆符 | 見 ③-2〜③-6：皆符 | 🟢 |
| `7` | 一切 `push` 之目標 ＝ 該側支、⛔ 被拒、⛔ `--force`；主線⛔ 推進 | 工項零〜三之 `push` 四次皆首推即成、皆為快轉（`[new branch]` → `655c6e3..576708c` → `576708c..c970ae6` → `c970ae6..83d3420`）；主線始終 `0b05925…` | 🟢 |
| `8` | 工項三二檔刪除欄 `0`、改前全檔為改後之嚴格前綴 | `numstat` `20`／`0`、`23`／`0`；`K-6` `410740 → 412870`、`CLAUDE.md` `282537 → 286590`，二者嚴格前綴皆 `True`；附加段之 `sha256` 各 ＝ `K2`／`P7` 之值 | 🟢 |
| `9` | `§四` 收工閘皆符 | 收工閘於工項四推後量·出艙於對話（自指·⛔ 入本檔） | —（本檔外） |
| `10` | CC ⛔ 作「孰為正典／應改為」之判、⛔ 改塊器命令 | 塊、器、命令一字未改；未作任何正典之判（`⑥` 所列皆為照實具名之事實） | 🟢 |
| `11` | 新檔⛔ 為 `git check-ignore` 所命中 | 本單、`F12` 皆 `git check-ignore -v` 無輸出（`rc 1`）；本報告同（見工項四之前檢·出艙於對話） | 🟢 |

---

## ③　工項二之前置與驗之出艙

### ③-1　前置（工項一之端 `576708c`）

**`F12 selftest`**（`rc 1`）：

````text
  🔴 受詞缺：['end_block_forced_buf', 'end_block_forced_bands', 'end_block_merge_run', 'SS_END_BLOCK_MODE', 'SS_END_BLOCK_MERGE']
⇒ 紅 ['受詞缺']；rc 1
````

**`F12 wiring`**（`rc 1`）：

````text
── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py ＋ verify/selection_pipeline.py）──
  🔴 W1 模組層之二常數與三函式、函式內⛔ 案件字面（案件字面 []）
  🔴 W2 二宿主：強制帶之 s 長入鏈之起點（左鏈之前）、強制帶入池（`_pool_strips_for_block` 之前）
  🔴 W3 宿主之准否：讀 `SS_END_BLOCK_MODE`／`SS_END_BLOCK_MERGE`／退縮，傳 `allow_forced=_allow`
  🔴 W4 harness：`alloc_state`／`alloc_eval` 於配地前設 `'trial'`；`run_corner_pk_k6b` 於段三之 if／else 之後（頂層）恰一次呼叫 `run_end_block_merge`，段三亦用同一組回呼（頂層呼叫 []）
  🔴 W5 `run_end_block_merge`：隔離（finally 復原 session 與 `K917_DROPPED`）後寫紀錄、帶退縮
  🔴 W6 `_WF_NS_NAMES` 含 `end_block_forced_buf`／`end_block_forced_bands`
  🔴 W7 `end_block_merge_run`：交 `k6b_stage3_run`（單一真相源）、除外三類、競合以合併群查
── 判別力（每一突變須使至少一項由綠轉紅）──
  🔴 N1 harness 左鏈⛔ 讓出強制帶：突變錨不存在（0）
  🔴 N2 harness 配地試算⛔ 設 trial：突變錨不存在（0）
  🔴 N3 宿主⛔ 傳准否：突變錨不存在（0）
  🔴 N4 畫面⛔ 入池強制帶：突變錨不存在（0）
⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'N1', 'N2', 'N3', 'N4']；rc 1
````

**`F12 run`**（`rc 1`）：

````text
  🔴 受詞缺：end_block_merge_run 等
⇒ 紅 ['受詞缺']；rc 1
````

**`F8 run`**：`3.5` ⇒ `rc 0`·末列 `⇒ 紅 []；rc 0`；`0.0` ⇒ `rc 0`·末列 `⇒ 紅 []；rc 0`。二次之後施工樹 `git status --porcelain` 空。

**`run_all`**（`<P>` ＝ `C:\Users\admin\AppData\Local\Temp\w353P`·`git worktree add --detach <P> HEAD`·`HEAD` ＝ `576708c`）：`rc 1`（末列 `W-V run_all: FAIL`）；`238127` B；跑畢 `git worktree remove --force <P>`。

**附（⛔ 單之前置所列·為 `V-4` 之比較而加跑）**：`F10 run`、`F11 run` 於工項一之端各 `rc 0`·末列 `⇒ 紅 []；rc 0`。

### ③-2　`V-1`（工項二之 `commit` `c970ae6`·⛔ `push` 前）

**`F12 selftest`**（`rc 0`）：

````text
── 合成對照（harvest 之 end_block_*／end_block_merge_run〔其內 k6b_stage3_run 為真〕）──
  ✅ S1 皆未達而准 ⇒ 無當選·列全留：得 (None, ['未達', '未達'])　期 (None, ['未達', '未達'])
  ✅ S1b 皆未達而不准 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S2 強制 ⇒ ⛔ 落位·紀錄當選 None·強制抵費地·buf 3.5·R_end 150：得 (['A(1)', 'B(1)'], None, True, 3.5, 150.0, None, True, False, None)　期 (['A(1)', 'B(1)'], None, True, 3.5, 150.0, None, True, False, None)
  ✅ S3 首趟強制而本趟不准 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S4 首趟強制而本趟准 ⇒ 沿用（⛔ 重評）：得 (True, 0, ['A(1)', 'B(1)'])　期 (True, 0, ['A(1)', 'B(1)'])
  ✅ S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）：得 (3.5, 0.0, 3.5, 0.0, 0.0)　期 (3.5, 0.0, 3.5, 0.0, 0.0)
  ✅ S6 強制帶 ＝ R_end（非強制⛔ 入）：得 (1, 150.0, 0, 0)　期 (1, 150.0, 0, 0)
  ✅ S7 定案趟：強制側有末端塊之宗 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S7b 定案趟：強制側無末端塊之宗 ⇒ 過：得 '過'　期 '過'
  ✅ S8 顯示：強制抵費地之列：得 ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）']　期 ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）']
  ✅ S9a 宿主：試算 ⇒ 准：得 (True, None)　期 (True, None)
  ✅ S9b 宿主：定案而無紀錄 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S9c 宿主：定案而紀錄（同退縮）載該端 ⇒ 准：得 (True, None)　期 (True, None)
  ✅ S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S9e 宿主：定案而紀錄只載他街廓 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S10a 無標的（C1(1) 單獨即達）⇒ 逕回（同一物件）：得 (True, [], [], 0)　期 (True, [], [], 0)
  ✅ S10b ① 同街廓成（⛔ 驗不影響原位次）：得 ([('C1(1)', '①', '成', '免'), ('C2(1)', '—', '略·已定案', '—')], {}, 0, ['C1(1)', 'C2(1)', 'D(1)'])　期 ([('C1(1)', '①', '成', '免'), ('C2(1)', '—', '略·已定案', '—')], {}, 0, ['C1(1)', 'C2(1)', 'D(1)'])
  ✅ S10c ② 道路成且驗不影響原位次：得 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '成', '通過')], {}, 2)　期 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '成', '通過')], {}, 2)
  ✅ S10d ② 之驗不過 ⇒ 未成 ⇒ 皆未達：得 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '未成', '不過')], {'BX': ['left']})　期 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '未成', '不過')], {'BX': ['left']})
  ✅ S10e 除外：上鎖者⛔ 併入：得 ('C1(1)', '—', '未成', '—')　期 ('C1(1)', '—', '未成', '—')
  ✅ S10f 除外：街角第 1 宗⛔ 併入：得 ('C1(1)', '—', '未成', '—')　期 ('C1(1)', '—', '未成', '—')
  ✅ S10g 除外：段三已併出者⛔ 併入：得 ('C1(1)', '—', '未成', '—')　期 ('C1(1)', '—', '未成', '—')
  ✅ S10h 競合：同一合併群之候選分屬二末端塊 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S10i 試算中止 ⇒ 逕回並記其由：得 (True, None, True)　期 (True, None, True)
── 判別力（突變之函式以其原始碼改一處後重綁於 ns·每一突變須使至少一例轉紅·畢即復原）──
  ✅ M1 皆未達⛔ 理准否（恆停機）：轉紅 ['S1 皆未達而准 ⇒ 無當選·列全留', 'S2 強制 ⇒ ⛔ 落位·紀錄當選 None·強制抵費地·buf 3.5·R_end 150', 'S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）', 'S6 強制帶 ＝ R_end（非強制⛔ 入）', 'S9a 宿主：試算 ⇒ 准', 'S9c 宿主：定案而紀錄（同退縮）載該端 ⇒ 准']
  ✅ M2 宿主恆准：轉紅 ['S9b 宿主：定案而無紀錄 ⇒ 停機', 'S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機', 'S9e 宿主：定案而紀錄只載他街廓 ⇒ 停機']
  ✅ M3 宿主⛔ 對退縮：轉紅 ['S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機']
  ✅ M4 強制帶之 s 長恆 0：轉紅 ['S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）']
  ✅ M5 強制⛔ 入池：轉紅 ['S6 強制帶 ＝ R_end（非強制⛔ 入）']
  ✅ M6 段三已併出者⛔ 除外：轉紅 ['S10g 除外：段三已併出者⛔ 併入']
  ✅ M7 ⛔ 查競合：轉紅 ['S10h 競合：同一合併群之候選分屬二末端塊 ⇒ 停機']
  ✅ M8 試算中止⛔ 攔：轉紅 ['S10i 試算中止 ⇒ 逕回並記其由']
  ✅ M0 復原後：紅 []
⇒ 紅 []；rc 0
````

**`F12 wiring`**（`rc 0`）：

````text
── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py ＋ verify/selection_pipeline.py）──
  ✅ W1 模組層之二常數與三函式、函式內⛔ 案件字面（案件字面 []）
  ✅ W2 二宿主：強制帶之 s 長入鏈之起點（左鏈之前）、強制帶入池（`_pool_strips_for_block` 之前）
  ✅ W3 宿主之准否：讀 `SS_END_BLOCK_MODE`／`SS_END_BLOCK_MERGE`／退縮，傳 `allow_forced=_allow`
  ✅ W4 harness：`alloc_state`／`alloc_eval` 於配地前設 `'trial'`；`run_corner_pk_k6b` 於段三之 if／else 之後（頂層）恰一次呼叫 `run_end_block_merge`，段三亦用同一組回呼（頂層呼叫 ['Assign']）
  ✅ W5 `run_end_block_merge`：隔離（finally 復原 session 與 `K917_DROPPED`）後寫紀錄、帶退縮
  ✅ W6 `_WF_NS_NAMES` 含 `end_block_forced_buf`／`end_block_forced_bands`
  ✅ W7 `end_block_merge_run`：交 `k6b_stage3_run`（單一真相源）、除外三類、競合以合併群查
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 harness 左鏈⛔ 讓出強制帶：轉紅 ['W2']
  ✅ N2 harness 配地試算⛔ 設 trial：轉紅 ['W4']
  ✅ N3 宿主⛔ 傳准否：轉紅 ['W3']
  ✅ N4 畫面⛔ 入池強制帶：轉紅 ['W2']
⇒ 紅 []；rc 0
````

### ③-3　`V-2`（`F8 run` 二退縮）

`3.5` ⇒ `rc 0`·末列 `⇒ 紅 []；rc 0`；`0.0` ⇒ `rc 0`·末列 `⇒ 紅 []；rc 0`。**改前改後二份 `cmp` 皆逐位同 ⇒ `diff` 皆空**（`§一` 項 `9` 符）。

### ③-4　`V-3`（`F12 run`）

````text
  ✅ R1 退縮 3.5：合併再試紀錄 {'退縮': 3.5, '標的': [], '皆未達': {}}；逐列 0；R6 左當選 628-4(1)
  ✅ R1 退縮 0.0：合併再試紀錄 {'退縮': 0.0, '標的': [], '皆未達': {}}；逐列 0；R6 左當選 628-4(1)
══ 合成案甲（退縮 3.5·注入 {'excl': ['628-4(1)'], 'lock': [], 'mw': None}·咬到 {'host': 22, 'merge': 0, 'geo': 0}）══
  ✅ X1 甲：地主 G009 以道路併入成，其合併群之他街廓已配地而本段無受併宗 ⇒ 停機（('段三／合併再試', "🔴 [K-6-B 段三 後處理] 街廓 R1 有群 ['628(1)', '628(2)', '628(3)', '628(4)', '628(5)', '628(6)', '628-1(1)', '628-1(2)', '628-1(3)'] 之保留宗而無本段之受併宗（停機款 9）")）
══ 合成案乙（退縮 3.5·注入 {'excl': ['628-4(1)'], 'lock': ['628-1(3)'], 'mw': None}·咬到 {'host': 20, 'merge': 1, 'geo': 0}）══
  ✅ X2 乙：逐列 [('628(2)', '①', '未成', '—'), ('628-1(2)', '①', '未成', '—'), ('628-23(1)', '①', '成', '免')]；當選 628-23(1)；鏈首宗 628-23(1) G 437.18 ＝ 外部錨 437.18；聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丙（退縮 3.5·注入 {'excl': ['628-4(1)'], 'lock': ['628-1(3)', '628-21(1)', '628-22(1)'], 'mw': None}·咬到 {'host': 18, 'merge': 1, 'geo': 0}）══
  ✅ X3 丙：逐列 [('628(2)', '①', '未成', '—'), ('628-1(2)', '①', '未成', '—'), ('628-23(1)', '—', '未成', '—')]；皆未達 {'R6': ['left']}；強制抵費地 R6-抵費地-2（252.28·外部錨 R_end 252.28·紀錄 252.28）；宗地 ∩ R_end 0.000000；聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丁（退縮 3.5·注入 {'excl': [], 'lock': [], 'mw': 13.0}·咬到 {'host': 0, 'merge': 0, 'geo': 30}）══
  ✅ X4 丁：逐列 [('628(2)', '②', '未成', '—'), ('628-1(2)', '②', '未成', '—'), ('628-23(1)', '①', '未成', '—'), ('628-4(1)', '②', '成', '通過'), ('628-22(1)', '—', '略·已定案', '—')]；當選 628-4(1)（R_end 701.29）；鏈首宗 628-4(1) G 779.93 ＝ 外部錨 779.93；聯集 △ 街廓 0.0000、兩兩疊 0.0000
⇒ 紅 []；rc 0
````

`rc 0`；`R1` 二退縮、`X1`〜`X4` 皆 ✅；其數與 `§一` 項 `6`／`7` 逐項同（`437.18`、`252.28`、`701.29`、`779.93`；聯集 △ 街廓與兩兩疊皆 `0.0000`；宗地 ∩ `R_end` `0.000000`）。

### ③-5　`V-4`

| 受詞 | `rc` | 末列（或要點） |
|---|---|---|
| `parity 3.5 on` | `0` | 見下 |
| `parity 0.0 on` | `0` | 見下 |
| `probe_WG9348_harvest_key.py` | `0` | `⇒ 紅 []；rc 0` |
| `probe_WG9346_failclosed.py run 3.5` | `0` | `⇒ 紅 []；rc 0` |
| `probe_WG9330_wfns_ast.py` | `0` | `_WF_NS_NAMES 成員數（AST）＝ 48 ／相異 ＝ 48`；`引擎經 ns 取用之相異名 ＝ 47` ⇒ **`48`／`48`／`47`** |
| `probe_WG9340_main_synth.py` | `0` | `ℹ️ app 側宿主 ＝ f3_screen_stepg_run（`W-G.9-345`）`；末列 `紅項 [] 器紅 0` |
| `F8 selftest`／`wiring` | `0`／`0` | 皆 `⇒ 紅 []；rc 0` |
| `F9 selftest`／`wiring`／`run` | `0`／`0`／`0` | 皆 `⇒ 紅 []；rc 0` |
| `F10 selftest`／`wiring`／`run` | `0`／`0`／`0` | 皆 `⇒ 紅 []；rc 0`；**`F10 run` 與工項一之端之出艙 `cmp` 逐位同** |
| `F11 selftest`／`wiring`／`run` | `0`／`0`／`0` | 皆 `⇒ 紅 []；rc 0`；**`F11 run` 與工項一之端之出艙 `cmp` 逐位同** |

`parity 3.5` 之末三列：

````text
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

`parity 0.0` 之末三列：

````text
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

⇒ 與 `§一` 項 `11` 逐項同（`35`／`34`、`36`／`35`·不符格 `0`；`Z` 皆 `[('harness', 'R1-抵費地-2')]`）。`V-4` 跑畢施工樹 `git status --porcelain` 空。

### ③-6　`V-5`（`run_all`·同一 `<P>` 路徑·`HEAD` ＝ `c970ae6`）

`run_all` `rc 1`（末列 `W-V run_all: FAIL`）；`238127` B。`python verify/probes/probe_WG9343_step0_flag.py runall <pre> <post>`（`rc 0`）之全文：

````text
【runall】項 64／64·PASS 28 → 28·FAIL 36 → 36
  相異項 0；其餘 64 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／36 → 22／36；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
````

`diff <O>\runall_pre.log <O>\runall_post.log` ⇒ `rc 0`、**輸出 `0` 列**（二份逐位同·各 `238127` B·Windows；發單側 Linux 為 `236050` B·其 bytes 平台與路徑相依·⛔ 入判）。跑畢 `git worktree remove --force <P>`。

---

## ④　四塊之實得與二檔之改前改後

抽取式 ＝ `§五-1` 末之式（圍欄開列之次列至閉列之前一列·`\n` 相接·末附 `\n`·UTF-8）。

| 塊 | 圍欄（單之列） | bytes | `sha256` | 列 | 對拍 `§五-1` |
|---|---|---|---|---|---|
| `D1` | `199`–`699` | `32497` | `137e96ed5d3a681531c630624f4e5d800064292e896ec907764c47c588202957` | `499` | ✅ |
| `F12` | `703`–`1473` | `41852` | `033eca6e073dea622907533cb39ff1ebf18969cd62a6448353a1386a2817bf36` | `769` | ✅ |
| `K2` | `1477`–`1498` | `2130` | `29d8e7862a37b52e9ed7a3e5abcd4c3dac84b053743a1a004d3b5e1332be5626` | `20` | ✅ |
| `P7` | `1502`–`1526` | `4053` | `cc6d0a2f0ad048d687c94ac322e8aa67554389d0b27349cd84ac99a0faa5aae8` | `23` | ✅ |

`verify/probes/probe_WG9353_endmerge.py` 落檔之 `sha256` ＝ `033eca6e…17bf36`（＝ `F12`）。

| 檔 | 改前 | 改後 | 嚴格前綴 | 附加段之 `sha256` | `CR` |
|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `410740` B | `412870` B | `True` | ＝ `K2` | `0` |
| `CLAUDE.md` | `282537` B | `286590` B | `True` | ＝ `P7` | `0` |

---

## ⑤　推送之目標與推後之遠端

一切 `push` 之目標 ＝ `verify/W-G.9-353-endmerge`。工項三推後 `git ls-remote --heads origin` 之列數 ＝ **`31`**，其相關列：

````text
488c4858da63ebe370ed950788947aa742eb44ad	refs/heads/verify/W-G.9-299-gb170
be5108d0067e63e23a397fdcbe43358800381470	refs/heads/verify/W-G.9-333-gb168
2ec1eb2bf43616ce662d95dc633b4c71f366eb15	refs/heads/verify/W-G.9-338-origin
d0add71ff85e62c2afb1f2f5d327c4488624c4a1	refs/heads/verify/W-G.9-341-gb182
14e022265bd1c190d7d6f9c1a0c6900bcec120db	refs/heads/verify/W-G.9-343-k929b
83d34209a224b168b66e63137cadea4cdd1aacd4	refs/heads/verify/W-G.9-353-endmerge
0b05925374f2de46c2493f5f56ef64667a2fed1d	refs/heads/wip/s1-endpart
````

主線仍 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；他五側支皆同 `§一` 項 `1`。工項四推後之值出艙於對話（自指）。

---

## ⑥　CC 之自捕與自解

**自捕**
1. **heredoc 被倉內 hook 攔下**（`verify/tools/wg9237_heredoc_guard.py`·`GB-143`）：首次以 heredoc 寫抽取器被拒 ⇒ 改以 `Write` 工具落檔後以路徑呼叫。⛔ 繞過該 hook。
2. **`cp --preserve=none` 非法引數**：工項零之首次複製失敗 ⇒ 其後之 `git add`／`git commit` 皆未生效（「nothing to commit」·`HEAD` 仍 `0b05925`）；改以 `cp` 重辦。首次失敗⛔ 留任何 `commit`、⛔ 推送。
3. **`run_all` 之副作用限於 `<P>`**：`<P>` 內改寫已追蹤之 `verify/out/probe_ruling_*.log` `4` 檔並新生 `E系列實測快照_退縮0m.csv`／`3.5m.csv` `2` 檔（`W-G.9-342` 所載之 Windows 形）；二次皆以 `git worktree remove --force` 清除；施工樹未受波及（每步後 `git status --porcelain` 空）。

**自解**（`作業常規之追加五`·皆零土地後果、零生產碼增改、可逆）
1. **加跑 `F10 run`／`F11 run` 於工項一之端**（白名單外·五項皆滿足）：`V-4` 令「`F10 run`、`F11 run` 之出艙與前置之端（工項一之端）逐字同」，而前置 `1`〜`5` 未列其跑 ⇒ 缺比較端。讀法甲 ＝ 另跑前置端（取之）；讀法乙 ＝ 以他窗舊 log 代（棄：他態他路徑）。證據 ＝ 二份 `cmp` 逐位同。
2. **取號器之第三引數**（類 `8`·裝飾性）：`python verify/probes/wg9268_gate6_occupancy.py 0b05925 W-G.9-353 W-G.9-352 W-G.9-398` 將 `W-G.9-398` 列於「對照組 甲（已知占用·須 ≥1）」而其六數皆 `0`（鬆框 `6` 檔／`9` 列），器仍 `rc 0`；單 `§零-1` 之表未列 `398`。受詢 `W-G.9-353` 之六數 `[0,0,0,0,0,0]`、`W-G.9-352` 列框 `12`／檔框 `4`、`W-G.9-963` 皆 `0` ⇒ 與單表逐項同。二值並報、續辦；⛔ 就該器之判準作任何主張。
3. **`commit` 訊息之尾列**（類 `3`）：單令訊息「逐字」；CC 以單之逐字為**首列**，其後附本倉慣例之 `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`（同 `W-G.9-352` 各 `commit`）。首列一字未改。
4. **並行之界**（類 `5` 外·照實具名）：`V-3`／`V-4` 於施工樹、後 `run_all` 於 `<P>`，二者同時跑；二者之受測物分屬二工作樹、互不寫入（`CLAUDE.md`「長跑期間不得動受測物」之受詞係同一樹內之 `app.py` 與 `verify/`）。前 `run_all` 於 `<P>` 跑時，施工樹施 `D1`——同理，`<P>` 之檔未被動。

**照實併記**
- 來源檔一取自 KL 主 checkout 之根（第二處）；**CC ⛔ 刪之**（`§五-2` 項 `3`）。
- `git apply` 之前後，未改塊、器、命令一字。
- **本檔所嵌之出艙之行尾**：Windows 下以重導所存之器出艙為 `CRLF`（Python 文字模式之 `stdout`）；嵌入本檔時僅將 `\r\n` 正規化為 `\n`（收工閘 `3` 之受詞含本檔），**字元內容一字未動**。
