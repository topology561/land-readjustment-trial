# `W-G.9-392` 規格單　執行端回報：**停機上呈**（停機款 `12`；兼 `§三-4` 之「應分配面積另有不經 `_solve_G_one` 之求解」）

> 執行端（CC·雲端排程「市地重劃·執行端」）·`2026-10-22`。結果 ＝ **停機上呈**。⛔ 自裁、⛔ 改單／器／塊一字。
> 主線 `wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（⛔ 動）。新側支 `verify/W-G.9-392-k980g` ＝ `c4666ab4c747058fbaad143009c3a4138b7396dc`（工項零、一·⛔ 撤）。遠端 heads `52`。
> **工項二之 `commit` `3c304b8f94298590fc19ad446c1290246da662bf` ⛔ 推**（單 `§四-1`：驗與審查皆符後方推；審查不符）——其二檔之全文差異附於本檔之末（附錄二），以保全之（雲端容器為暫存）。工項三、四⛔ 施。

## 一、停機款之三值（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `56c77fd`、heads `51`、無新側支、樹淨、`§零-0` 項 `3` 四簿之值、旗標 `[None×5]`、環境可匯入 | 皆合（主線 `56c77fd…`；heads `51`；新側支之列 `0`；`status` 空；四簿：自誤 `619`／`634`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；旗標 `[None, None, None, None, None]`；依 `requirements.txt` 裝後匯入 `rc 0`） |
| `2` | `SELF_SHA256`、bytes／`sha256` 相符；入倉 blob 逐位同 | 合（`144622` B·`5ff3ea900591…`；`SELF_SHA256` 自驗 `124adb779367…`；`git cat-file blob` 與來源 `cmp` 同） |
| `3` | 塊 `Fy47`／`K38`／`P49`／`G16` 之 bytes／`sha256`／列數；`git apply --check`；寫出後 blob | 合（`Fy47` `49006` B·`4afe0b6e…`·`839` 列；`K38` `10377` B·`4221620f…`·`61`；`P49` `2911` B·`85d8def1…`·`21`；`G16` `2019` B·`f94b797c…`·`12`；`apply --check` 過；`12` 器之施前、施後 blob 皆 ＝ `§五-1` 項 `2`／`5`） |
| `4` | 前置 (甲)(乙)(丙)、前置 `4` | 合（`80` 呼叫皆合期·`stderr` 合計 `0` B；`f8_pre` ＝ `8be0160b…`／`6fb86647…`；前置 `4` 之四字樣皆無出艙·`rc 1`） |
| `5` | 規格無涉域之歧義；⛔ 須改 `§三-3` 之禁改 | **見款 `12`**（審查之 (A-2) 即 `§三-4` 之「應分配面積另有不經 `_solve_G_one` 之求解」之形） |
| `6` | `V-1`〜`V-9` 皆 ＝ 期；配地之改變 ＝ `§一` 項 `5` | 皆合（下第三節） |
| `7` | 推送之目標唯新側支／`ops/queue`；⛔ `--force` | 合（工項零 新立、工項一 快轉；主線⛔ 動） |
| `8` | 工項三之三檔 | **未施**（停機於工項二之審查） |
| `9` | 收工閘 | **未及**（停機） |
| `10` | ⛔ 自判正典、⛔ 改塊／器／命令 | 合（⛔ 改；`<repo>` ＝ `/tmp/w`） |
| `11` | 新檔⛔ 為 `.gitignore` 所命中 | 合（本單、新器 `git check-ignore -v --no-index` 皆 `rc 1`） |
| **`12`** | **唯讀獨立 reviewer 之發現⛔ 涉域上判斷或規格之漏載** | **🔴 成就：(A-1)、(A-2) 二條（第四節）** |
| `13` | 存取與寫入⛔ 被拒 | 合 |

## 二、`commit` 與推送

| 工項 | `commit` | 首列（逐字） | 推送 |
|---|---|---|---|
| 零 | `c06616193db8b69adc52f01e82b550fc1b24c868` | `W-G.9-392 工項零：本單原封入倉（新側支）⛔ 零生產碼` | `HEAD:refs/heads/verify/W-G.9-392-k980g`（新立）·推後 heads `52`·主線 `56c77fd…` |
| 一 | `c4666ab4c747058fbaad143009c3a4138b7396dc` | `W-G.9-392 工項一：量測器（F36 之新器·既有之器十一之增許與更錨）（新側支）⛔ 零生產碼` | 快轉 `c066161..c4666ab`；`numstat` ＝ 閘 `1` 之工項一之列逐項同（`3/0`、`9/0`、`9/0`、`4/0`、`9/0`、`5/1`、`5/0`、`6/0`、`13/2`、`6/0`、`2/0`、`567/0`） |
| 二 | `3c304b8f94298590fc19ad446c1290246da662bf`（**本機·⛔ 推**） | `W-G.9-392 工項二：每宗之應分配面積試算至穩定·取得之宗之自我檢查（K-9-80 ③·KL 05:22 甲）🔴 生產碼（新側支）` | ⛔（審查不符） |

工項二之二檔：`app.py` `+77`／`−10` ⇒ blob `f12af112e5bf3c80248bc8821624ae1e02b5fed1`；`verify/stepg_pipeline.py` `+33`／`−0` ⇒ blob `0cd22fc9ad8a45dcde435c1af016b26a95e0bc6b`。

## 三、前置與驗之出艙（摘要·全表見附錄一）

- **版本之比對**（`§零-0` 項 `6`）：`Python 3.11.17` 同；`pip freeze` 之 `sha256` ＝ `a1042e4ce42466f9…`（基準 `ae1438da…`）——依單釘四列之後仍異二列：`python-dateutil==3.0.0`（基準 `2.9.0.post0`）、多 `tzdata==2026.5`（`requirements.txt` 之解之新版·單未令釘之）⇒ **前置 (丙) 整份照跑**（⛔ 沿用基準·⛔ 停機）。
- **前置**（工項一之端 `c4666ab`·`80` 呼叫·並行 `2`）：`80／80` 合「工項一之端」之列；`stderr` 合計 `0` B；耗時之和 `14830` s。`#16`／`#17`／`#18`／`#46` ⇒ `rc 1` 如期；`#78` `⇒ 紅 ['受詞缺']；rc 1`、`#79` `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']；rc 1`、`#80` `⇒ 紅 ['受詞缺']；rc 1`。`f8_pre_35.json` ＝ `8be0160bc14dd92a5331f86eecc995cae0507376`、`f8_pre_00.json` ＝ `6fb86647807f9744594071be25c522b6b506c230`。
- **`V-1`／`V-2`／`V-9`**（工項二之 `commit`·從頭整套·並行 `2`）：`80／80` 合「施後」之列（皆 `rc 0`）；`stderr` 合計 `0` B；耗時之和 `15615` s。`F36 selftest` `G1`〜`G4`、`H1`〜`H5`、`E1`〜`E5` 皆 ✅、`P0 判式自驗 14／14`（`G1 量 290·略 10；G2 量 288·略 12`）；`F36 wiring` `W1`〜`W7` 皆 ✅；`F36 run`：`R1@3.5 自我檢查 423 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8`、`R2@3.5 不合 []`、`R1@0.0 自我檢查 324 次`、`R2@0.0 不合 []`。`#4`（`probe_WG9363_k953.py selftest`）載 `✅ P0 逐項擾動恰該項紅 75／75`。
  - 🩸 **容器之重啟**：施後之驗之中途（`11` 呼叫已畢）雲端容器重啟、背景之跑停；環境（`pip freeze` `a1042e4c…`、`HEAD` `3c304b8`、樹淨）重核同後，其餘 `69` 呼叫自頭重跑（中斷之趟之出艙棄之）。⛔ 逾時、⛔ `rc` 異，故無「重跑一次」之二趟可載。
- **`V-3`**：`git diff --quiet c4666ab 3c304b8 -- verify/probes` ⇒ 同（`12` 器之 blob ＝ `§五-1` 項 `5`）。
- **`V-4`**：`F36 diff`（3.5 m）`rc 0`，逐字：`宗 R5·628-18(2)·left G(㎡) 268.33 → 268.34`／`抵費地 R1-抵費地-1 面積 851.68 → 851.69`／`抵費地 R3-抵費地 面積 1651.41 → 1651.4`／`抵費地 R4-抵費地 面積 697.4 → 697.39`／`抵費地 R5-抵費地 面積 1221.44 → 1221.45`／`抵費地 R6-抵費地 面積 980.59 → 980.58`／`全比相異 6 項`；（0 m）`rc 0`：`抵費地 R1-抵費地-1 面積 851.67 → 851.69`／`抵費地 R3-抵費地 面積 1651.41 → 1651.4`／`抵費地 R4-抵費地 面積 697.4 → 697.39`／`抵費地 R5-抵費地 面積 1221.47 → 1221.46`／`抵費地 R6-抵費地 面積 980.59 → 980.58`／`全比相異 5 項`。`k6s3 cmp` 二退縮皆 `rc 1`·末列 `相異 1 項 ⇒ 🔴 異`（其項 `R1-抵費地-1`）。⇒ **本案配地之改變 ＝ `§一` 項 `5`**（逐字同）。
- **`V-5`**：`parity` 二退縮皆 `rc 0`·`⇒ rc 0（不符 0 項）`。以 `<HEAD>` 代二態之 `HEAD` 全值（前 `c4666ab…`·後 `3c304b8…`·各見 `1` 次）後：`parity35` 落檔（`8683` B）、`parity00` 落檔（`284` B）、二 `stdout`（`1586`／`1584` B）皆**逐位同**；對照（⛔ 代）皆相異。
- **`V-6`**：`run` 二退縮皆 `⇒ 紅 []；rc 0`；`hash-object`：3.5 m `8be0160b…` → `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、0 m `6fb86647…` → `884e91714a79288406faa4def6518847de36de39`（＝ 期）。JSON 逐欄遞迴比：3.5 m `/dropped/R2/left[0]/G(㎡) 3.81 → 3.82`、`/rows[16]/G(㎡) 268.33 → 268.34`（`相異 2 欄`·`rows[16]` ＝ `628-18(2)`）；0 m `/dropped/R2/left[0]/G(㎡) 3.81 → 3.82`（`相異 1 欄`）。
- **`V-7`**：生產碼 `34` 檔對 `c4666ab` 相異唯 `app.py`、`verify/stepg_pipeline.py`；`verify/` 相異唯 `verify/stepg_pipeline.py`。AST：`app.py` 頂層之名之增 `['K980_G_MAX_ITER', 'K980_G_TOL', 'end_block_trial_G', 'k980_acq_check']`·減 `[]`·相異之節點 `['K980_G_MAX_ITER', 'K980_G_TOL', '_WF_NS_NAMES', '_solve_G_one', 'end_block_host', 'end_block_trial_G', 'f3_screen_stepg_run', 'k980_acq_check']`；`verify/stepg_pipeline.py` 增減 `[]`·相異之節點 `['_run_step_g_impl']`（＝ `§三-3` 第 `4` 款）。
- **`V-8`**：「GB-206」`app.py:3`；「k980_acq_check」`app.py:6`、`verify/stepg_pipeline.py:4`；「end_block_trial_G」`app.py:7`、`verify/stepg_pipeline.py:2`；「K980_G_TOL」`app.py:3`（判別力 ＝ 前置 `4` 之 `rc 1`）。

## 四、唯讀獨立審查（停機款 `12` 之所據）

另派之唯讀 reviewer（⛔ 改檔·⛔ `commit`；前後 `git status --porcelain` 空、`HEAD` 不變）之結論：**(A) 二條、(B) 無**。執行端已自行重跑其例三而坐實 (A-1)，並查碼坐實 (A-2)。

### (A-1) 評選之式與實配之輸入有結構性之差：`w0_start`（否證塊 `K38` 二之丁之「與評選處之輸入之差至多為浮點之末位」）

- 實配之街角第 1 宗傳 `_w0_start=0.0`（`app.py:22106`、`:22248`、`:22268`；`verify/stepg_pipeline.py` 同構）⇒ `solve_G_binary` 之 `W_near ＝ 0`（`K-9-41` ①）。
- 評選之式 `_corner_first_lot_G`（`app.py:19872` 之 `_solve_G_one(…)`）**⛔ 傳 `w0_start`**（＝ `None`）⇒ `W_near` 取幾何之量（街角點對 SIDE_LINE 中點之投影）。
- 二者唯於 FRONT 之端點恰落於 SIDE_LINE 之無限直線上時相等——本案合之（`app.py:19803` 所引之探針 §1 ＝ `0.000000000`），故本案二退縮之自我檢查 `423`／`324` 次皆過。
- **他案**：合成之街廓（矩形 `60×20`·右側街角第 1 宗·`a` ＝ `300`），SIDE_LINE 偏 `δ`（執行端重跑·改後之碼）：`δ ＝ 0` ⇒ 評選 `96.53`、實配 `96.53`·過；**`δ ＝ 0.001 m` ⇒ `96.53` ≠ `96.52` ⇒ `GB-206` 停機**；`δ ＝ 0.05 m` ⇒ `96.77` ≠ `96.40` ⇒ 停機（改前之碼同形 ＝ `96.76` 對 `96.40`：此 `0.36 ㎡` 之不一致早已存在而未見）。SIDE_LINE 端點對 FRONT 端點之吻合之容差為 `0.5 m`（超過才警示·`app.py:27341`〜`27347`）⇒ 他案之圖差 `1 mm` 即觸 `GB-206`，而訊息歸因為「取至 2 位不同」。塊 `K38` 之四之他案之形 `57`〜`66` 未載此形。
- **待裁（⛔ 自裁）**：評選之式是否亦依 `K-9-41` ①（／`K-9-5-12`（五）1）帶 `w0_start=0.0`；或另立「FRONT 端點須落於 SIDE_LINE 上」之閘；或此形依 `GB-206` 停機即為所欲。其土地後果：前者於本案⛔ 變（本案 `δ ＝ 0`）、於他案改街角之評選之值（可翻門檻邊緣之得標）。

### (A-2) `R-1` 之受詞之外另有一路應分配面積之計算（`§三-4` 所列之停機之形）

- `app.py:26648`（`main()` 內「🏘️ 土地歸戶」分頁之「📐 歸戶後應分配面積計算」）：閉式 `G ＝ (a(1−A·B) − RW·F·L1 − S·L2)(1−C)`，取至 `4` 位，寫入 session 鍵 `alloc_results_df`（`:26687`）並供匯出（`:26764`）。
- 其不經 `_solve_G_one`；`§三-4` 明令「應分配面積另有不經 `_solve_G_one` 之求解（全倉之生產碼 `34` 檔）」⇒ 停機上呈；塊 `K38` 二之乙之「⛔ 及」之列未載之。
- 其為閉式（無收斂之問題·容差之改無涉），⛔ 屬評選或實配；惟取 `4` 位與 KL 甲之「取至小數 2 位」之字面⛔ 一。**待裁**：是否在 KL `05:22` 甲之射程內（或列為「⛔ 及」）。

### WARNING-1（未證·供參）

harness 之 `run_corner_pk`（`verify/selection_pipeline.py:440`）取 `A` 之區段之源為快照之 `原地號_區段`，鏈上取 `tp` 之 `重劃前地價區段`；自我檢查以實配之輸入重算評選之式，故⛔ 能偵測評選當時之輸入之源之分岔。本案 `parity` 綠，⛔ 為結構之保證；與 (A-1) 同屬「末位之差」之前提之射程。

### (B) 純實作之瑕：無。（C）無礙之記

1. `_BISECT_TOL = 0.01`（`app.py:9496`、`:9504`）之註仍稱「`solve_G_binary` 之 tol」，生產之路已為 `1e-6`（帳對幾何閘寬 `0.015` 今偏寬而仍保守；`R-6` 禁改·宜登記）。2. `verify/stepg_pipeline.py:416`〜`417` 之 `solve_G_binary`／`iterate_G_S` 之區域別名全檔⛔ 呼叫（死別名）。3. `_smr392` 每街廓算一次；`_strip_axis` 之退化於 Step L 先觸，⛔ 新之失敗之形。4. 缺 FRONT 時 `_corner_first_lot_G` 拋無號之 `RuntimeError`，惟 Step L 對缺 FRONT 之街廓不產勝者，此路⛔ 可達。5. 實作 `+77`／`−10`（原型 `+75`／`−10`·⛔ 為期）。
- 審查之他項（皆合）：`R-1`〜`R-6` 之落點與 AST 之數；`solve_G_binary(` 之呼叫全倉唯 `app.py:19745`；`R-4` 四處之引數與 Step L（`app.py:20957`）、`run_corner_pk`（`verify/selection_pipeline.py:441`）、`end_block_host` 之 `_trial` 逐一對照（除上開 `w0_start` 與 WARNING-1 外唯浮點末位之差：`d_hat` 之算法）；自我檢查之停機於段三、入池閘、末端塊合併再試之試算內確上拋（`k6_trial_mark`／`k6_trial_raise_since` 之諸處·實測吞 `RuntimeError` 後仍上拋）；右鏈之自我檢查在 `_adj` 之重試之後（`#65` 之形）；`§三-3` 六款皆合（錨之比對：器之字串 `26708` 中於基準恰一而今⛔ 恰一者 `0`；突變之器皆 `rc 0`；`main` ⛔ 動）；合成之例一（右側街角第 1 宗·`400` 個 `a`）：改前評選與實配取 2 位異 `61／400`、改後 `0／400`；例二（末端塊·左右各 `300`）：改前各 `32／300`、改後 `0`；改前改後之 `_trial` 於 `480` 組輸入之輸出逐位同、`solve_one` 所受之引數 `480` 對 `480` 同。

## 五、執行端之設計說明（`§三-5`·供復驗與次單）

- `R-1`：`app.py:13158`〜`13160` 新增 `K980_G_TOL = 1e-6`、`K980_G_MAX_ITER = 200`（附註所據）；`_solve_G_one`（`app.py:19754`）之 `solve_G_binary(…)` 改傳 `tol=K980_G_TOL, max_iter=K980_G_MAX_ITER`，他引數⛔ 動。
- `R-2`：`k980_acq_check`（`app.py:11688`）——`round(float(·), 2)` 二值異 ⇒ `raise k6_program_stop("🔴 [GB-206·K-9-80 ③] 街廓 …·<側>·<kind> <pid>：評選之所算 x.xx ㎡ ≠ 實配之所算 y.yy ㎡（…）")`；同 ⇒ `None`。
- `R-3`：`end_block_trial_G`（`app.py:11701`）——側別⛔ left／right ⇒ 無號之 `RuntimeError`；其解之式與舊之巢狀 `_trial` 逐位同（區域名 `_d392`／`_c392`／`_dd392`／`_bp392`／`_r392`）；`end_block_host` 之 `_trial`（`app.py:11757`）改 `return end_block_trial_G(solve_one, _a, _A, l_front, blk_poly, _d, _cp, S_block_max, avg_depth, allocation_dir, side, s_back)`（`_d`／`_cp` ＝ 既有之 `np.asarray(d_hat)`／`np.asarray(corner_pt)`·⛔ 刪）。
- `R-4`：二上界 `_sl392`（`‖front_p2 − corner_pt‖`·與 `_corner_first_lot_G` 之前提之斷言同式）、`_smr392`（`(_oblique_s_max(blk_meta['vertices'], d_hat, corner_pt, allocation_dir_block) or _sl392) if allocation_dir_block is not None else _sl392`）每街廓算一次：`app.py:21944`〜`21948`、`verify/stepg_pipeline.py:821`〜`825`（經 `ns["_oblique_s_max"]`）。四處：`app.py:22135`〜`22146`（左）、`:22298`〜`22309`（右）；`verify/stepg_pipeline.py:935`〜`946`（左）、`:1084`〜`1095`（右）——皆在 `k917_should_drop` 之 `continue` 之後、`_lg_idx_*` 之推進之前；`if _commit and is_first_corner_*:` ⇒ `_corner_first_lot_G(…)`；`elif _commit and _lg_idx_* == 0 and entry.get('is_end_block') and _eb_info['<側>'] is not None:` ⇒ `end_block_trial_G(…)[0]`；harness 經 `ns['k980_acq_check']`、`ns['_corner_first_lot_G']`、`ns['end_block_trial_G']`。
- `R-5`：`_WF_NS_NAMES`（`app.py:20294`）增 `"k980_acq_check", "end_block_trial_G"`。
- `R-6`：新區域名皆帶 `392`；`R-3` 之側別之停機⛔ 帶號。
- 呼叫處之全列（改後）：`_solve_G_one(` ＝ `app.py:19872`（`_corner_first_lot_G` 內）、`app.py:21549`（畫面之 `_solve_one` 薄殼）、`verify/stepg_pipeline.py:556`（`ns["_solve_G_one"]`·harness 之薄殼）；`_corner_first_lot_G(` ＝ `app.py:19904`、`:19912`（`_corner_block_true_G` 內）、`app.py:22136`、`:22299`、`verify/stepg_pipeline.py:936`、`:1085`；`end_block_trial_G(` ＝ `app.py:11757`、`:22143`、`:22306`、`verify/stepg_pipeline.py:943`、`:1092`。
- `§三-3` 之自查：第 `1` 款——撰碼中自跑 `probe_WG9363_k953.py wiring … 7d8e954`／`probe_WG9367_adj4.py wiring … d7a5ea4`，首趟紅 `W8`／`W7`（錨之異 `[('·容差 ', 2)]`·新常數之註含「·容差 1e-6」）⇒ 改註之措辭（「舊 80；`K980_G_TOL` 之下…」）後皆 `rc 0`（未 `commit` 前之自捕）；第 `2`〜`6` 款見第三節 `V-7` 與第四節。

## 六、自捕與自解

1. `pip freeze` 與基準異二列（`python-dateutil`、`tzdata`）⇒ 依單 (丙) 整份照跑（⛔ 自釘單外之版）。
2. 撰碼中之自跑之器（F23／F24 wiring 等）與前置之 `2` 並行之跑同時，致並行之數短暫為 `3`（⛔ 屬單之「驗」之命令；施後之驗則嚴守 `2`）。
3. 本單之複本置施工樹之根（`執行端.md` 丙 3）而以 `.git/info/exclude` 排除之（⛔ 入倉·使 `git status --porcelain` 唯受詞之檔）。
4. 容器之重啟（第三節）。
5. 撰碼之於另一複本（`/tmp/w2`）以免擾前置之跑，前置畢後以 `cp` 移入施工樹後 `py_compile`、`commit`。

## 七、各段耗時（並行 `2`）

開工與工項零、一 ≈ `10` 分；撰碼與自跑 ≈ `25` 分（與前置並行）；前置 `80` 呼叫 ≈ `124` 分（耗時之和 `14830` s）；施後之驗 ≈ `11` 呼叫 `60` 分 ＋ 重啟後 `69` 呼叫 `51` 分（耗時之和 `15615` s）；`V-4`〜`V-8` ≈ `3` 分；唯讀審查 ≈ `26` 分。

## 八、留待

- 發單端／KL：(A-1)、(A-2) 之裁；裁後之補令（或改單）再施工項二〜四。工項二之 `3c304b8` 之碼（附錄二）可原樣再用或依裁改之。
- 主 checkout 之同步由 KL 自行為之（README 第六節第 6 款）。

## 附錄一　`80` 呼叫之二態（`rc`／`stderr` B／末列·耗時 s·合期否）

| # | 前置之組 | 命令 | 工項一之端（前置·實跑） | 施後（工項二·實跑） |
|---|---|---|---|---|
| `1` | 甲 | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `2` | 甲 | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（145）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（143）✅ |
| `3` | 甲 | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（431）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（425）✅ |
| `4` | 甲 | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `5` | 甲 | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（29）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（29）✅ |
| `6` | 甲 | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（30）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（30）✅ |
| `7` | 甲 | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ |
| `8` | 丙 | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `9` | 丙 | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `10` | 丙 | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（40）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（39）✅ |
| `11` | 丙 | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（16）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（15）✅ |
| `12` | 丙 | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（275）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（268）✅ |
| `13` | 甲 | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `14` | 甲 | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `15` | 甲 | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `16` | 甲 | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `1`／`0`／`⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1`（81）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（80）✅ |
| `17` | 甲 | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `1`／`0`／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（568）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（584）✅ |
| `18` | 甲 | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `1`／`0`／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（787）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（810）✅ |
| `19` | 甲 | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9）✅ | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8）✅ |
| `20` | 丙 | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `21` | 丙 | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ |
| `22` | 丙 | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（71）✅ | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（66）✅ |
| `23` | 丙 | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（489）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（471）✅ |
| `24` | 丙 | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `25` | 丙 | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2089）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2254）✅ |
| `26` | 丙 | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（35）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（33）✅ |
| `27` | 丙 | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `28` | 丙 | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（6）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（6）✅ |
| `29` | 丙 | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（24）✅ | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（23）✅ |
| `30` | 丙 | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `31` | 丙 | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（25）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（24）✅ |
| `32` | 丙 | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（295）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（282）✅ |
| `33` | 丙 | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（426）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（402）✅ |
| `34` | 丙 | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（39）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（39）✅ |
| `35` | 丙 | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（35）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（35）✅ |
| `36` | 丙 | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（8）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（7）✅ |
| `37` | 丙 | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（24）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（23）✅ |
| `38` | 丙 | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（17）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（16）✅ |
| `39` | 丙 | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（12）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（11）✅ |
| `40` | 丙 | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（224）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（227）✅ |
| `41` | 丙 | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `42` | 丙 | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（57）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（54）✅ |
| `43` | 丙 | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（952）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（958）✅ |
| `44` | 甲 | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（1）✅ |
| `45` | 甲 | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（1）✅ |
| `46` | 甲 | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `1`／`0`／`⇒ 紅 ['R4']；rc 1`（185）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（185）✅ |
| `47` | 丙 | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（124）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（113）✅ |
| `48` | 丙 | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（1）✅ |
| `49` | 丙 | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（413）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（445）✅ |
| `50` | 丙 | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（0）✅ | `0`／`0`／`selftest 9/9 ⇒ ✅`（0）✅ |
| `51` | 丙 | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（0）✅ | `0`／`0`／`selftest 13/13 ⇒ ✅`（0）✅ |
| `52` | 丙 | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ |
| `53` | 丙 | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2）✅ | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1）✅ |
| `54` | 丙 | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（10）✅ | `0`／`0`／`紅項 [] 器紅 0`（10）✅ |
| `55` | 丙 | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（409）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（445）✅ |
| `56` | 乙 | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_pre_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（245）✅ | `0`／`0`／`（JSON 之摘要列·略）`（241）✅ |
| `57` | 乙 | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_pre_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（172）✅ | `0`／`0`／`（JSON 之摘要列·略）`（173）✅ |
| `58` | 乙 | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_pre_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（240）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（242）✅ |
| `59` | 乙 | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_pre_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（173）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（171）✅ |
| `60` | 乙 | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_pre.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（510）✅ | `0`／`0`／`⇒ rc 0（不符 0 項）`（561）✅ |
| `61` | 乙 | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_pre.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（378）✅ | `0`／`0`／`⇒ rc 0（不符 0 項）`（360）✅ |
| `62` | 甲 | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（4）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（5）✅ |
| `63` | 甲 | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（3）✅ |
| `64` | 甲 | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（416）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（409）✅ |
| `65` | 甲 | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `66` | 甲 | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `67` | 丙 | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1474）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（1572）✅ |
| `68` | 丙 | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1453）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（1563）✅ |
| `69` | 甲 | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `70` | 甲 | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（152）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（146）✅ |
| `71` | 甲 | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（543）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（534）✅ |
| `72` | 甲 | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `73` | 甲 | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `74` | 甲 | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（412）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（411）✅ |
| `75` | 甲 | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（2）✅ |
| `76` | 甲 | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／`⇒ 紅 []；rc 0`（26）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（31）✅ |
| `77` | 甲 | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（163）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（156）✅ |
| `78` | 甲 | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（2）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（8）✅ |
| `79` | 甲 | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']；rc 1`（5）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（5）✅ |
| `80` | 甲 | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（26）✅ | `0`／`0`／`⇒ 紅 []；rc 0`（415）✅ |

前置：合期 80／80·stderr 合計 0 B·耗時之和 14830 s
施後：合期 80／80·stderr 合計 0 B·耗時之和 15615 s

## 附錄二　工項二（`3c304b8`·⛔ 推）之二檔之全文差異（`git diff c4666ab 3c304b8 -- app.py verify/stepg_pipeline.py`）

````diff
diff --git a/app.py b/app.py
index b591d76..f12af11 100644
--- a/app.py
+++ b/app.py
@@ -11685,6 +11685,40 @@ def end_block_forced_bands(eb_info):
     return _out
 
 
+def k980_acq_check(kind, blk_label, side, pid, g_eval, g_actual):
+    """🆕 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「甲」之「自我檢查」）：取得之宗（街角第 1 宗、末端塊之當選者）之二次所算之比。
+    `g_eval` ＝ 評選之式依實配之輸入重算之值、`g_actual` ＝ 實配之值；各取至 2 位（`round(·, 2)`）不同 ⇒ 立程式之停機
+    `GB-206`（經 `k6_program_stop` 登記·試算之內亦上拋·⛔ 靜默取其一）；同 ⇒ 回 `None`（⛔ 登記）。"""
+    _ge392 = round(float(g_eval), 2)
+    _ga392 = round(float(g_actual), 2)
+    if _ge392 != _ga392:
+        raise k6_program_stop(
+            f"🔴 [GB-206·K-9-80 ③] 街廓 {blk_label}·{side}·{kind} {pid}：評選之所算 {_ge392:.2f} ㎡ ≠ "
+            f"實配之所算 {_ga392:.2f} ㎡（取得之宗之二次所算取至 2 位不同 ⇒ 停機·⛔ 靜默取其一）")
+    return None
+
+
+def end_block_trial_G(solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max, avg_depth,
+                      allocation_dir, side, s_back):
+    """🆕 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「甲」）：末端塊之評選之試算之單一真相源（#20）。
+    `end_block_host` 之評選與二宿主之取得之宗之自我檢查皆經本函式；左 ⇒ 方向 d̂、起點 `corner_pt`；
+    `右 ⇒ 方向 −d̂、起點 corner_pt ＋ S_block_max·d̂`；上界 `max(0.1, S_block_max)`。回 `(G, S_raw)`。"""
+    if side not in ('left', 'right'):
+        raise RuntimeError(
+            f"🔴 `W-G.9-392`：end_block_trial_G 之側別 {side!r} 非 left／right ⇒ 停（no-silent-fallback）")
+    _d392 = np.asarray(d_hat, dtype=float)
+    _c392 = np.asarray(corner_pt, dtype=float)
+    if side == 'left':
+        _dd392, _bp392 = _d392, _c392
+    else:
+        _dd392, _bp392 = -_d392, _c392 + float(S_block_max) * _d392
+    _r392, _ = solve_one(a_m2, A_ratio, l_front, 0.0, 0.0, blk_poly, _dd392, _bp392,
+                         max(0.1, float(S_block_max)), False, '無', avg_depth, _allocation_dir=allocation_dir,
+                         _side_mid=None, _W_prev=0.0, _w0_start=0.0, _near_dir=None,
+                         _is_chain_head=True, _s_back=s_back)
+    return float(_r392.get('G', 0.0)), float(_r392.get('S_raw', _r392.get('S', 0.0)))
+
+
 def end_block_host(ordered, *, blk_label, blk_poly, d_hat, corner_pt, front_p2, alloc_dir_cad,
                    allocation_dir, session, corner_range_polys, solve_one, l_front, avg_depth,
                    S_block_max, post_price, pre_price_by_zone, min_build_area=None):
@@ -11719,15 +11753,9 @@ def end_block_host(ordered, *, blk_label, blk_poly, d_hat, corner_pt, front_p2,
         _pre = float(pre_price_by_zone.get(tp.get('重劃前地價區段', ''), 0.0) or 0.0)
         _post = float(post_price or 0.0)
         _A = (_post / _pre) if (_pre > 0 and _post > 0) else 1.0
-        if side == 'left':
-            _dd, _bp = _d, _cp
-        else:
-            _dd, _bp = -_d, _cp + float(S_block_max) * _d
-        _res, _ = solve_one(_a, _A, l_front, 0.0, 0.0, blk_poly, _dd, _bp, max(0.1, float(S_block_max)),
-                            False, '無', avg_depth,
-                            _allocation_dir=allocation_dir, _side_mid=None, _W_prev=0.0,
-                            _w0_start=0.0, _near_dir=None, _is_chain_head=True, _s_back=s_back)
-        return float(_res.get('G', 0.0)), float(_res.get('S_raw', _res.get('S', 0.0)))
+        # 🆕 `W-G.9-392`：評選之試算委派單一真相源 `end_block_trial_G`（二宿主之取得之宗之自我檢查同之）
+        return end_block_trial_G(solve_one, _a, _A, l_front, blk_poly, _d, _cp, S_block_max, avg_depth,
+                                 allocation_dir, side, s_back)
 
     return end_block_apply(ordered, blk_label=blk_label, block_poly=blk_poly, d_hat=d_hat,
                            corner_pt=corner_pt, front_p2=front_p2, cad_alloc=alloc_dir_cad,
@@ -13127,6 +13155,10 @@ K980_AREA_TOL = 0.01        # ㎡·擴大後之範圍之面積之上餘：`0 ≤
 K980_AREA_EPS = 1e-6        # ㎡·「範圍之面積已 ≥ 最小建築面積」之判之浮點餘裕（⛔ 法定之量）
 K980_TOUCH_TOL = 0.01       # m·一街廓之二範圍之距 ≤ 本值 ⇒ 相接或重疊（法定粒度）
 
+# 🆕 `W-G.9-392`（`K-9-80` ③·KL `2026-10-22 05:22`「是」·甲）：每宗之應分配面積試算至穩定後取至小數 2 位（評選與實配同值）。
+K980_G_TOL = 1e-6           # ㎡·應分配面積（G）之二分之收斂之容差（`_solve_G_one` → `solve_G_binary`·舊 0.01）
+K980_G_MAX_ITER = 200       # 次·其二分之次數之上限（舊 80；`K980_G_TOL` 之下之所需遠小於此）
+
 
 def k980_mba(session, label, category):
     """`W-G.9-391`（`K-9-80` ④⑤·`K-9-1` ⑨ 裁丙）：某街廓之最小建築面積之有效值之單一入口（畫面與 harness 同一二鍵）。
@@ -19719,7 +19751,7 @@ def _solve_G_one(*, a_m2, A, l_front, l_side, F, blk_poly, d_hat, baseline_pt,
                 is_corner=is_corner,
                 is_chain_head=is_chain_head,             # 🆕 W-G.9-261：鏈頭旗標（薄殼直通·⛔ 在此推導）
                 side_label=side if side in ('左側', '右側') else '左側',
-                tol=0.01, max_iter=80,
+                tol=K980_G_TOL, max_iter=K980_G_MAX_ITER,   # 🆕 W-G.9-392：試算至穩定（K-9-80 ③·KL 05:22 甲）
                 allocation_dir=allocation_dir,
                 side_mid=side_mid, W_prev=W_prev,
                 near_dir=near_dir,                       # 🆕 D-2b-23【甲】：界面單線（⛔ 不在此推導）
@@ -20258,6 +20290,8 @@ _WF_NS_NAMES = [
     #      （逐字「實拋 KeyError @ stepg_pipeline.py:699｜'k91_effective_min_build_area'」）
     #      ⇒ app 生產路徑之 `_wf_ns()` 必崩（`自誤 302` 之形·CC 自犯）。
     "k91_effective_min_build_area",
+    # 🆕 `W-G.9-392`（`K-9-80` ③）：取得之宗之自我檢查與末端塊之評選之試算之二名（引擎 `verify/stepg_pipeline.py` 經 `ns` 消費·漏列即 app 路徑 KeyError）。
+    "k980_acq_check", "end_block_trial_G",
 ]
 
 
@@ -21906,6 +21940,13 @@ def f3_screen_stepg_run(st, *,
                                  if (_mw_blk > 0 and _pw < _mw_blk) else '')
             return _res
 
+        # 🆕 `W-G.9-392`（`K-9-80` ③·`R-4`）：取得之宗之自我檢查之評選之式之二上界（＝ Step L 之評選之同式·每街廓算一次）。
+        _sl392 = (float(_np_d.linalg.norm(_np_d.asarray(_front_p2_blk, dtype=float)[:2]
+                                          - _np_d.asarray(corner_pt, dtype=float)[:2]))
+                  if (_front_p2_blk is not None and corner_pt is not None) else None)
+        _smr392 = ((_oblique_s_max(blk_meta.get('vertices'), d_hat, corner_pt, allocation_dir_block) or _sl392)
+                   if allocation_dir_block is not None else _sl392)
+
         # ── 🆕 W-D.2 §3（D-1 bootstrap 載體）：單塊可重入推進 ──
         def _advance_block_with_split(_k_split, _commit):
             """依池槽 _k_split 切分後執行雙向推進（Task D-2 左右迴圈整段內移）。
@@ -22090,6 +22131,19 @@ def f3_screen_stepg_run(st, *,
                     if _commit:   # 🆕 `W-G.9-333` `c3`：試推進⛔ 記（去重）
                         k917_note_drop(blk_label, 'left', k, res, tp)
                     continue
+                # 🆕 `W-G.9-392`（`K-9-80` ③·KL 05:22 甲）：取得之宗之自我檢查（末趟·鏈首·評選之式依實配之輸入重算·取至 2 位異 ⇒ GB-206）
+                if _commit and is_first_corner_l:
+                    k980_acq_check('街角第1宗', blk_label, 'left', k, _corner_first_lot_G(
+                        a_m2=a_m2, A_ratio=A_ratio, B=B_value, C=C_for_calc, l_front=l_front, l_side=l_side_use,
+                        F=F_use, block_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt, s_max_left=_sl392,
+                        s_max_right=_smr392, side='左', allocation_dir=allocation_dir_block, side_mid=_side_mid_left,
+                        avg_depth=avg_depth_default, tab6_burden=_tab6_burden, front_p2=_front_p2_blk,
+                        _label=f'{blk_label}·{k}·左·W-G.9-392'), res.get('G', 0.0))
+                elif _commit and _lg_idx_left == 0 and entry.get('is_end_block') and _eb_info['left'] is not None:
+                    k980_acq_check('末端塊', blk_label, 'left', k, end_block_trial_G(
+                        _solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max,
+                        avg_depth_default, allocation_dir_block, 'left', float(_eb_info['left']['s_back']))[0],
+                        res.get('G', 0.0))
                 _lg_idx_left += 1
                 if _has_left_corner:   # thread 累積 W_前 給下一筆
                     _W_prev_left = float(res.get('W_far', _W_prev_left))
@@ -22240,6 +22294,19 @@ def f3_screen_stepg_run(st, *,
                     if _commit:   # 🆕 `W-G.9-333` `c3`：試推進⛔ 記（去重）
                         k917_note_drop(blk_label, 'right', k, res, tp)
                     continue
+                # 🆕 `W-G.9-392`（`K-9-80` ③·KL 05:22 甲）：取得之宗之自我檢查（右鏈·於 `_adj` 之重試之後之定案之 `res`）
+                if _commit and is_first_corner_r:
+                    k980_acq_check('街角第1宗', blk_label, 'right', k, _corner_first_lot_G(
+                        a_m2=a_m2, A_ratio=A_ratio, B=B_value, C=C_for_calc, l_front=l_front, l_side=l_side_use,
+                        F=F_use, block_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt, s_max_left=_sl392,
+                        s_max_right=_smr392, side='右', allocation_dir=allocation_dir_block, side_mid=_side_mid_right,
+                        avg_depth=avg_depth_default, tab6_burden=_tab6_burden, front_p2=_front_p2_blk,
+                        _label=f'{blk_label}·{k}·右·W-G.9-392'), res.get('G', 0.0))
+                elif _commit and _lg_idx_right == 0 and entry.get('is_end_block') and _eb_info['right'] is not None:
+                    k980_acq_check('末端塊', blk_label, 'right', k, end_block_trial_G(
+                        _solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max,
+                        avg_depth_default, allocation_dir_block, 'right', float(_eb_info['right']['s_back']))[0],
+                        res.get('G', 0.0))
                 _lg_idx_right += 1
                 if _has_right_corner:   # thread 累積 W_前 給下一筆
                     _W_prev_right = float(res.get('W_far', _W_prev_right))
diff --git a/verify/stepg_pipeline.py b/verify/stepg_pipeline.py
index b2f6622..0cd22fc 100644
--- a/verify/stepg_pipeline.py
+++ b/verify/stepg_pipeline.py
@@ -817,6 +817,13 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     f"條件③ J 非零看守破：街廓 {blk_label} {_side_nm_w2}側有 SIDE_LINE 但 "
                     f"F×l₁={_F_w2:.2f}×{_l1_w2:.2f}=0（快照 負擔尺度_輸入 未正確消費？）")
 
+        # 🆕 `W-G.9-392`（`K-9-80` ③·`R-4`）：取得之宗之自我檢查之評選之式之二上界（＝ `run_corner_pk` 之評選之同式·每街廓算一次·app 同構）。
+        _sl392 = (float(_np_d.linalg.norm(_np_d.asarray(_front_p2_blk, dtype=float)[:2]
+                                          - _np_d.asarray(corner_pt, dtype=float)[:2]))
+                  if (_front_p2_blk is not None and corner_pt is not None) else None)
+        _smr392 = ((ns["_oblique_s_max"](blk_meta.get('vertices'), d_hat, corner_pt, allocation_dir_block) or _sl392)
+                   if allocation_dir_block is not None else _sl392)
+
         # ── 可重入推進（app _advance_block_with_split 逐行複刻；headless 無 st 訊息） ──
         def _advance_block_with_split(_k_split, _commit):
             _N_f = len(ordered_v2)
@@ -924,6 +931,19 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     if _commit:   # 🆕 `W-G.9-333` `c3`：試推進⛔ 記（去重·app 同構）
                         ns['k917_note_drop'](blk_label, 'left', k, res, tp)
                     continue
+                # 🆕 `W-G.9-392`（`K-9-80` ③·KL 05:22 甲）：取得之宗之自我檢查（app 同構·三名經 ns）
+                if _commit and is_first_corner_l:
+                    ns['k980_acq_check']('街角第1宗', blk_label, 'left', k, ns['_corner_first_lot_G'](
+                        a_m2=a_m2, A_ratio=A_ratio, B=B_value, C=C_for_calc, l_front=l_front, l_side=l_side_use,
+                        F=F_use, block_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt, s_max_left=_sl392,
+                        s_max_right=_smr392, side='左', allocation_dir=allocation_dir_block, side_mid=_side_mid_left,
+                        avg_depth=avg_depth_default, tab6_burden=_tab6_burden, front_p2=_front_p2_blk,
+                        _label=f'{blk_label}·{k}·左·W-G.9-392'), res.get('G', 0.0))
+                elif _commit and _lg_idx_left == 0 and entry.get('is_end_block') and _eb_info['left'] is not None:
+                    ns['k980_acq_check']('末端塊', blk_label, 'left', k, ns['end_block_trial_G'](
+                        _solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max,
+                        avg_depth_default, allocation_dir_block, 'left', float(_eb_info['left']['s_back']))[0],
+                        res.get('G', 0.0))
                 _lg_idx_left += 1
                 if _has_left_corner:
                     if not _W0_left_set:
@@ -1060,6 +1080,19 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     if _commit:   # 🆕 `W-G.9-333` `c3`：試推進⛔ 記（去重·app 同構）
                         ns['k917_note_drop'](blk_label, 'right', k, res, tp)
                     continue
+                # 🆕 `W-G.9-392`（`K-9-80` ③·KL 05:22 甲）：取得之宗之自我檢查（右鏈·於 `_adj` 之重試之後之定案之 `res`·app 同構）
+                if _commit and is_first_corner_r:
+                    ns['k980_acq_check']('街角第1宗', blk_label, 'right', k, ns['_corner_first_lot_G'](
+                        a_m2=a_m2, A_ratio=A_ratio, B=B_value, C=C_for_calc, l_front=l_front, l_side=l_side_use,
+                        F=F_use, block_poly=blk_poly, d_hat=d_hat, corner_pt=corner_pt, s_max_left=_sl392,
+                        s_max_right=_smr392, side='右', allocation_dir=allocation_dir_block, side_mid=_side_mid_right,
+                        avg_depth=avg_depth_default, tab6_burden=_tab6_burden, front_p2=_front_p2_blk,
+                        _label=f'{blk_label}·{k}·右·W-G.9-392'), res.get('G', 0.0))
+                elif _commit and _lg_idx_right == 0 and entry.get('is_end_block') and _eb_info['right'] is not None:
+                    ns['k980_acq_check']('末端塊', blk_label, 'right', k, ns['end_block_trial_G'](
+                        _solve_one, a_m2, A_ratio, l_front, blk_poly, d_hat, corner_pt, S_block_max,
+                        avg_depth_default, allocation_dir_block, 'right', float(_eb_info['right']['s_back']))[0],
+                        res.get('G', 0.0))
                 _lg_idx_right += 1
                 if _has_right_corner:
                     if not _W0_right_set:
````
