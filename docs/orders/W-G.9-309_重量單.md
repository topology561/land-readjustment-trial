# `W-G.9-309`　重量單：`GB-170` 之修（強制抵費地之遠側界線、其後 `1` 宗之近側界線、強制抵費地之物化形）＋ 強制側藍影受檢宗之宗序（`K-9-31 ④`／`K-9-32 ②④`）＋ `自誤 469`〜`475` ＋ `GB-172`／`GB-173`

> **發單** ＝ 發單側窗二十一·`2026-09-22`。**受單** ＝ CC 窗 B（KL 告 context `32%`·已辦主 checkout 更新四令）。
> **級** ＝ **重**（生產碼 `2` 檔·落凍存分支）。**開工態** ＝ `2f46579c6c9c91d9f1b88431a7e6ae9d998ce311`（`wip/s1-endpart`）。
> **KL 放行** ＝ `2026-09-22` 逐字「是，放行，出 `W-G.9-309`（重量批）」（呈文與射程見 `§二`）。
> 🛑 **主線之生產碼 ⛔ 動一字**；生產碼只落凍存分支 `verify/W-G.9-299-gb170`（`GB` 簿 `:7824`／`:8132` 所釘之名）。

---

## `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報窗 B 之 context 餘量；**預估不足以辦畢工項零〜六者，停**（停機款 `11`），先出交接文、⛔ 開工。
2. 以 `git rev-parse HEAD` 核開工態 ＝ `2f46579c6c9c91d9f1b88431a7e6ae9d998ce311`，`git status --porcelain` 之追蹤檔變動 ＝ `0`（停機款 `1`）。
3. 以 `python verify/probes/probe_WG9321_issuer_anchor.py . <倉外落檔> 468 464` 重跑態錨器，逐格對 `§一`（停機款 `1`）。
4. 本單以**檔案**收之（⛔ 經剪貼簿）；工項一之抽取器對本單全文驗 `CR`（含即停·停機款 `2`）。

---

## `§零`　取號・級・停機款

### `§零-1`　取號現查（`恆常附款 e`＋`e②`＋`e③`·`z`）

| 號 | 檔名側 | 內文側（框·母體 ＝ 開工態全倉 `2620` 檔） | `e③` 之判 | 取用 |
|---|---|---|---|---|
| `W-G.9-309` | `0`（`docs/orders/W-G.9-309*`） | `git grep -l 'W-G\.9-309'` ＝ `51`（`*.md` `45`·`verify/out/` `5`·`verify/probes/` `1`） | 皆為本工項之預留引述（`307`〜`325` 諸單與報告）⇒ `(b)` | **取** |
| `自誤 469` | — | `git grep -n '自誤 469'` ＝ `2` 列（`docs/orders/W-G.9-325_輕量單.md:25`、`docs/reports/W-G.9-325R_CC交接文.md:58`） | 二列皆為「對照乙［必為零］」之判別力哨兵 ⇒ `(c)`（器之自指·扣除） | **取** |
| `自誤 470`〜`475` | — | `git grep -nE '自誤 47[0-9]'` ＝ `0` | — | **取** |
| `GB-172`／`GB-173` | — | `git grep -nE 'GB-17[2-9]'` ＝ `0` | — | **取** |
| 分支 `verify/W-G.9-299-gb170` | 遠端 `0`（`git ls-remote --heads origin`） | — | `GB` 簿所釘之名（`:7824`／`:8132`） | **立** |

🔒 受單側於開工時以上列之式**當場重算**並二值並列（`恆常附款 f`）；任一相異 ⇒ 停機款 `1`。
🔒 `自誤 469` 前經交接文十九擬予「交接文十八 `§四 乙`（以字樣命中斷言器之可執行性質）」；該則之全文⛔ 在倉、發單側本窗⛔ 得 ⇒ 本單**⛔ 鑄該則**，其號候全文到時另取。

### `§零-2`　停機款（`恆常附款 n`：一律三值·🟢 已執行且通過／🛑 未執行／🔴 已執行且破）

| # | 停機款 |
|---|---|
| `1` | 開工態、態錨、取號之任一格與本單相異 |
| `2` | 本單含 `CR`；或抽取器（附件 `X-0`）之任一附件 `sha256` 不符、或新檔目標既存（`rc ≠ 0`） |
| `3` | 工項二（釘紅）之出艙與 `§三 工項二` 所載之期值相異 |
| `4` | `git apply` 失敗；或施作後 `git hash-object app.py` ≠ `5ceddfce896d106c8bc3c5a66ce7e236ab0a104d`、`git hash-object verify/stepg_pipeline.py` ≠ `e4bd912b4f9e8cfe7cc49aef66f41ed566020937` |
| `5` | 工項三之閘器 `rc ≠ 0`，或其任一閘非 🟢，或土地影響表與附件 `B-1` 相異 |
| `6` | 工項三之靜態器（`probe_WG9308S1_bindorder.py`／`probe_WG91_static_checks.py`／`probe_WG918_downcast.py`）任一 `rc ≠ 0` |
| `7` | 收工閘（`§四`）任一非 🟢 |
| `8` | 主線 `wip/s1-endpart` 上出現生產碼四檔（`app.py`／`verify/stepg_pipeline.py`／`verify/run_all.py`／`verify/run_verification.py`）之任何變動 |
| `9` | 凍存分支之 `push` 先於停機款 `2`〜`6` 全 🟢；或任何併入主線之動作（`merge`／`cherry-pick`／`rebase` 至主線） |
| `10` | 工項五之任一末端追加破嚴格前綴（`恆常附款 x` 三值之 🔴） |
| `11` | 窗 B 之 context 不足以辦畢本單 |

🛑 停機即停；以三值出艙已辦各款，⛔ 自行變通。

### `§零-3`　pre-flight 機檢之逐項處置

受單側以 `python verify/probes/probe_order_preflight.py docs/orders/W-G.9-309_重量單.md` 跑之；`P-3`／`P-5` 為停機款，其餘 🟡 逐項具名採納或豁免（⛔ 靜默略過）。發單側出單前之實跑結果與處置見附錄 `P`。

---

## `§一`　態錨（開工態 `2f46579`·發單側窗二十一自倉實跑·`2026-09-22`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線 | `2f46579`（`e7b80c5..` `1` 筆·`git diff --name-status` 僅 `A` 一列） |
| `2` | 生產碼 | `verify/` 頂層 `*.py` `33` ＋ `app.py` ＝ `34`；`app.py` blob `8466f7493082bf84aa4f02d6c1c6e55ff746fc4a`（`1465843` B） |
| `3` | 子層 `*.py` | `375`（交叉檢 `408` ＝ `408`） |
| `4` | 四簿（正典框） | 自誤 `458`／`468`／缺 `[106,355,356,357]`；`GB` `169`／`171`／`[12,87]`；`VR` `80`／`95`／`[73,75]`；`K-9` `42`／`43`／`[]` |
| `5` | `baselines` | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·`298` 列 |
| `6` | refs | `25` |
| `8` | 母體 | 全倉 `2620`／`.md` `901`／`docs/` `861`／`verify/out/` `1024` |
| `9` | 恆常附款 | 相異款號 `28`·表列式 `37` |
| `11` | 收工閘 | `probe_WG9270_closegate.py 468 464 .` ⇒ `rc 0` |
| `12` | dprime | 先移出落檔再跑 ⇒ `rc 0`·重生 `11cf47bb…` 與倉內逐位相同 |

---

## `§二`　KL 之放行（逐字）與射程

**發單側所呈（窗二十一·`2026-09-22`·附平面圖·【要你判斷】為逐字，餘為摘錄）**
- 【現況】R2 街廓左端，強制抵費地 308.17 ㎡，其上緣沿分配方向斜出。緊鄰的 628-42(1) 分得 4.77 ㎡，是一條寬約 0.1 m、深約 45 m 的狹長條。628-41(1) 分得 183.23 ㎡。
- 【要改成】① 強制抵費地實際分出來的土地，形狀一併照 9/15 之界線切出，即上緣與側街平行；面積仍為 308.17 ㎡。② 依 9/17 裁二，緊鄰強制抵費地的那一宗要受藍影檢查（藍影 76.11 ㎡）。③ 628-42(1) 在新界線下只能分得 2.55 ㎡，未達藍影，兩側境界線會交叉 ⇒ 不配地，面積入調配池。④ 由 628-41(1) 遞補到緊鄰位置，並同樣受檢；檢查結果合格。
- 【對土地的影響】628-42(1) 不配地（原有土地 8.34 ㎡）；628-41(1) 183.23 → 176.60 ㎡、負擔比率 42.62% → 44.69%；628-40(1)+ 299.51 → 299.07 ㎡；R4 街廓左端強制抵費地面積不變、形狀改，628(1)+ 減少 1.50 ㎡（退縮 0 m）、1.28 ㎡（退縮 3.5 m）；其他街廓不變。
- 【要你判斷】是否放行：將上述兩項修改寫入測試版本並逐宗核對，仍不併入正式版本（併入時另行請您放行）？（是／否）

**KL 逐字所答** ＝「是，放行，出 `W-G.9-309`（重量批）」。

🩸 呈文之用語有誤（`自誤 475`）：「上緣」實指**遠側界線**；「沿分配方向」實指**與宗地分配線平行**（`K-9-43`（五）：分配方向垂直於宗地分配線）。放行之受詞以平面圖與逐宗數為準，⛔ 繫於該二詞。

🛑 **射程（發單側釘死·⛔ CC 擴之）**——`(a)` 附件 `B` 寫入凍存分支並 `push`；`(b)` 該分支之逐宗核對與畫面核對之準備；`(c)` 🔴 ⛔ 入主線（另一次放行）；`(d)` ⛔ 及於 `GB-167`／`168`／`169`／`171` 之修、`K-9-29` 之任何子項、`K-9-33 ⑤` 所增二條件之接線、`GB-172`／`GB-173` 之修。逐字入 `GB` 簿見附件 `C-1`。

🔒 **逐筆放行清單**（`恆常附款 y`·母體 ＝ 本批將落入**主線**之全部 `commit`）：`c1`（工項零＋一）、`c3`（工項五＋六）——二者皆**⛔ 改動**生產碼四檔 ⇒ 生產碼 `commit` 於主線 ＝ `0`；`常規一` 四項齊備者逕 `push`。凍存分支之 `c2` 係本放行 `(a)` 之受詞。

---

## `§三`　工項

**依賴序**：工項零＋一（`c1`·主線）→ 工項二（釘紅·零 commit）→ 工項三（`c2`·凍存分支）→ 工項四（畫面核對之備·零 commit）→ 工項五＋六（`c3`·主線）→ `§四` 收工閘。

### 工項零　本單原封入倉（主線·⛔ 零生產碼）

路徑 ＝ `docs/orders/W-G.9-309_重量單.md`（`常規三`：沿 `W-G.9-324_中量單.md`／`W-G.9-325_輕量單.md` 之形）。**檢**：`bytes`／`CR` 之有無／`sha256` 逐位出艙；`SELF_SHA256` 之自驗依 `P-5` 原口徑（取檔內最末一個 `SELF_SHA256` 列以前之全部 bytes）。

### 工項一　附件之抽取與器入倉（主線·⛔ 零生產碼·與工項零同一 `commit` `c1`）

1. 以 CC 之檔案工具，將附件 `X-0` 之內容逐字寫為倉外之 `extract_wg9309.py`（LF·UTF-8·⛔ 經命令列·`恆常附款 h`），核其 `sha256` ＝ 附件 `X-0` 標題所載。
2. `python <倉外>/extract_wg9309.py docs/orders/W-G.9-309_重量單.md . <倉外暫存目錄>`（無 `--append`）⇒ `rc 0`；出艙其逐附件之列（期：附件數 `17`·`新檔` `10`·`倉外` `2`·`末端追加` `4`·`X-0` 自身 `1`）。
3. 新檔 `10` 支（`verify/probes/probe_WG9309_gates.py` ＋ `verify/probes/wg9309/` 下 `9` 支）入 `c1`；`倉外` 之 `B` 與 `B-1` ⛔ 入倉（`B` 已嵌於本單）。
4. `c1` 為純新增 ⇒ `常規一 ②` 以 `git diff --numstat` 之刪除欄全 `0` 證之；逕 `push` 主線。

🔒 `verify/probes/wg9309/` 內 `drv.py`／`chk_band.py`／`cmp.py`（交接文十九附錄 B）、`drv_p2b.py`／`ovl2.py`／`r2_geom.py`／`synth_attr.py`（交接文二十附錄 B）、`chk_p3.py`（窗二十一）係**發單側沙盒之量測器逐字**（Linux·`python3`），隨單入倉以免「發單側量測器未入倉」；受單側須跑者僅 `probe_WG9309_gates.py` 所驅之 `chk_wg9309.py` 與 `synth_attr.py`。

### 工項二　釘紅（⛔ 零 commit·`GB-170` 放行 `(b)` 之「① 先釘紅」）

1. 於倉外立拋棄式 worktree：`git worktree add --detach <倉外>/wt_base 2f46579`。
2. `python verify/probes/probe_WG9309_gates.py <倉外>/wt_base <倉外>/wt_base <倉外>/out_pinred`（**二參皆為基座**）。
3. **期值**（發單側沙盒實測·基座 `2f46579`）：`rc` ＝ `7`；閘 `1`／`2`／`5`／`6`／`8`／`10` ＝ 🔴、閘 `9` ＝ 🛑（基座無 `_corner_band_geom`）、閘 `3`／`4`／`7` ＝ 🟢；閘 `1` 之受驗值 ＝ `A_0` `R4` `13.055881`、`A_35` `R2` `38.068189`、`A_35` `R4` `13.05519`、`B_35` `R2` `38.068189`；閘 `2` 之 `R2` ＝ `19.031794`（`A_35`／`B_35`）。
4. 出艙 `out_pinred/WG9309_gates.md` 之全文；該檔於 `c3` 入倉為 `verify/out/WG9309_pinred.md`。判準：逐閘之三值與上列相同，所列數值之差 `≤ 1e-4`（容各機之浮點差）；否則停機款 `3`。

### 工項三　生產碼（凍存分支·`c2`·🔴 生產碼）

1. 自 `c1` 後之主線 `HEAD` 立分支 `verify/W-G.9-299-gb170`，切換之。
2. `git apply --check <倉外暫存目錄>/W-G.9-309_P4.diff` ⇒ `git apply` 同檔；核 `git hash-object app.py` ＝ `5ceddfce896d106c8bc3c5a66ce7e236ab0a104d`、`git hash-object verify/stepg_pipeline.py` ＝ `e4bd912b4f9e8cfe7cc49aef66f41ed566020937`（停機款 `4`）；`git diff --stat` ＝ `2 files changed, 94 insertions(+), 23 deletions(-)`。
3. 閘器：`python verify/probes/probe_WG9309_gates.py <倉外>/wt_base . <倉外>/out_gates` ⇒ **期** `rc 0`、十閘皆 🟢；其「土地影響」節與附件 `B-1` 逐列相同（停機款 `5`）。
4. 靜態器：`python verify/probes/probe_WG9308S1_bindorder.py`、`python verify/probes/probe_WG91_static_checks.py`、`python verify/probes/probe_WG918_downcast.py` ⇒ 皆 `rc 0`（發單側於附件 `B` 施作後之沙盒樹實跑皆 `rc 0`·停機款 `6`）。
5. **觀測**（三值·⛔ 停機款·`恆常附款 d`：**未能於出單前實查**）：`python verify/run_verification.py` 於本分支之 `rc`、歷時與其末 `40` 列；另於基座 worktree 同跑一次並二值並列。
6. `commit`（訊息自擬·須含 `W-G.9-309`、`🔴 生產碼`、`凍存分支`），於停機款 `2`〜`6` 全 🟢 後 `push` 本分支（放行 `(a)`）；**⛔ 併入主線**（停機款 `9`）。

**附件 `B` 之內容**（`GB-170` 之 `(i)(ii)(iii)` ＋ 受檢宗序·相對 `2f46579`）：
- `app.py`：`_corner_band_geom`（新函式·強制帶幾何之單一真相源）；`_corner_buffer_S` 增選用參數 `far_line_dir`（預設 `None` ⇒ 逐位不變）並委派之；`_pool_strips_for_block` 增選用參數 `forced_bands`（預設 `None` ⇒ 逐位不變）；畫面路徑（`def main` 內）三處鏡射 stepg：遠側線向之求取與 `far_line_dir` 之傳入、界面單線鏈之初值、池片之 `forced_bands`；受檢宗序之判別式（左右鏈）；`_lot_gate` docstring 射程一行之增補。
- `verify/stepg_pipeline.py`：同上之 stepg 側（遠側線向、`far_line_dir`、界面單線鏈初值、`forced_bands`、受檢宗序）。
- 🔒 受檢宗序之判別式（二檔四處同字）：`is_second_after_corner=((_lg_idx_側 == (0 if _fo_側 else 1)) and not bool(is_first_corner_側))`。
- 🔒 `verify/wf_f1.py`／`verify/wf_f4.py` **⛔ 改**（`GB-173`）。

### 工項四　畫面核對之備（⛔ 零 commit·放行 `(b)`）

1. 於 KL 本機之**主 checkout 以外**立 worktree：`git worktree add C:\Users\admin\Desktop\lrt-309 verify/W-G.9-299-gb170`（路徑名依 `常規三` 可另提）；核該處 `git hash-object app.py` ＝ `5ceddfce896d106c8bc3c5a66ce7e236ab0a104d`。**主 checkout ⛔ 動**。
2. 列出主 checkout 內畫面啟動所需、而不在倉內之物（`.gitignore` 所排除者如 `.streamlit/`、真地籍資料檔等）；**⛔ 自行複製**——其複製與否請示 KL。
3. 於報告寫明 KL 之核對事項（地籍語）：自該資料夾以 `streamlit run app.py` 啟動，依平常之操作跑至分配結果，於 R2 街廓左端（退縮 3.5 m）看三事——① 強制抵費地 308.17 ㎡；② 628-42(1) 不出現於分配結果；③ 628-41(1) 為 176.60 ㎡。並記主控台有無錯誤。
4. KL 之核對**⛔ 為本單之閘**（候 KL 擇時辦）；其結果於入主線之呈文時引之。

### 工項五　登記（主線·⛔ 零生產碼·純末端追加·與工項六同一 `commit` `c3`）

1. 切回主線。`python <倉外>/extract_wg9309.py docs/orders/W-G.9-309_重量單.md . <倉外暫存目錄> --append` ⇒ 四則末端追加之列皆「已附（嚴格前綴 ✅）」、`rc 0`（停機款 `10`）。
   - `C-1` → `docs/reports/W-G.4_泛用阻塞項登記表.md`（KL 放行之逐字與射程、`GB-170` 失效條件之現況、`GB-171` 修屬之更正、`GB-172`／`GB-173` 之立）
   - `C-2` → `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`自誤 469`〜`475`）
   - `C-3` → `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`K-9-31 ④`／`K-9-32 ②③④` 之落地狀態）
   - `C-4` → `CLAUDE.md`（進度表 `:590`／`:1099`／`:1457` 之現況更正）
2. 🔒 抽取器之嚴格前綴檢外，另以 `verify/tools/wg942_append_audit.py`（嚴格前綴 ＝ `True`）對四檔各驗一次，三值出艙（`恆常附款 x`）。
3. ⚠️ 重跑須防重附：`--append` 僅跑一次；重跑前以 `git diff --stat` 核四檔未附。

### 工項六　執行報告入倉（主線·新檔·`c3`）

1. `docs/reports/W-G.9-309R_執行報告.md`（新檔）：`§零-0`〜`§四` 之逐款三值、工項二與工項三之閘器全文、工項三之觀測、工項四之準備結果與 KL 核對事項、`c1`／`c2`／`c3` 之 `commit` 與 `push` 之出艙。
2. `verify/out/WG9309_pinred.md`（工項二之 `WG9309_gates.md`）、`verify/out/WG9309_gates.md`（工項三之同檔）——新檔 `2` 支；閘器之逐格 JSON **⛔ 入倉**（倉外保留）。
3. `c3` 逕 `push` 主線（`常規一`：零生產碼·純新增 ＋ 純末端追加）。

---

## `§四`　收工閘（**重**·`c3` 入倉後於主線量·`恆常附款 n` 三值／`r` 同格載基線態）

| # | 閘 | 期值（基線態 ＝ `§一`） |
|---|---|---|
| `1` | `python verify/probes/probe_WG9270_closegate.py 475 468 .` | `rc 0`（基線：`468 464` ⇒ `rc 0`） |
| `2` | `python verify/probes/probe_WG9321_issuer_anchor.py . <倉外落檔> 475 468` | `rc 0` |
| `3` | 主線之生產碼四檔 | `app.py` blob ＝ `8466f7493082bf84aa4f02d6c1c6e55ff746fc4a`（**絕對值**·⛔ 變）；其餘三檔之 blob 與 `2f46579` 同 |
| `4` | 凍存分支 | 遠端存在；其 `app.py` blob ＝ `5ceddfce896d106c8bc3c5a66ce7e236ab0a104d`、`verify/stepg_pipeline.py` ＝ `e4bd912b4f9e8cfe7cc49aef66f41ed566020937`；與主線之分歧 ＝ `c2` 一筆 |
| `5` | 四簿期末（算式見 `§四-1`） | 見 `§四-1` |
| `6` | 母體（算式見 `§四-2`） | 見 `§四-2` |

### `§四-1`　四簿期末之算式（`恆常附款 w①`·⛔ 直接寫一個數）

- 自誤（正典框）：相異 ＝ `458 ＋ 7`（新鑄 `469`／`470`／`471`／`472`／`473`／`474`／`475`）＝ `465`；`MAX` ＝ `475`；缺號 ＝ `[106, 355, 356, 357]`（⛔ 增）。自擬框：`454 ＋ 7 ＝ 461`。
- `GB`：相異 ＝ `169 ＋ 2`（新鑄 `172`／`173`）＝ `171`；`MAX` ＝ `173`；缺號 ＝ `[12, 87]`。
- `VR`：`80`／`95`／`[73, 75]`（⛔ 變）。`K-9`：`42`／`43`／`[]`（⛔ 變·本單⛔ 鑄裁）。
- 恆常附款：相異款號 `28`·表列式 `37`（⛔ 變·本單⛔ 立款）。

### `§四-2`　母體之算式（`恆常附款 e`／`e②`·含受單側為執行本單所必生之物）

除本單自身之產物外 ＝ 全倉 `2620`／`.md` `901`／`docs/` `861`／`verify/out/` `1024`／子層 `*.py` `375`／refs `25`。
本單之產物（逐筆）：`docs/orders/W-G.9-309_重量單.md`、`docs/reports/W-G.9-309R_執行報告.md`、`verify/out/WG9309_pinred.md`、`verify/out/WG9309_gates.md`、`verify/probes/probe_WG9309_gates.py`、`verify/probes/wg9309/` 下 `9` 支（`chk_wg9309.py`／`chk_p3.py`／`synth_attr.py`／`drv.py`／`chk_band.py`／`cmp.py`／`drv_p2b.py`／`ovl2.py`／`r2_geom.py`）；遠端分支 `verify/W-G.9-299-gb170`。
⇒ 全倉 `2620 ＋ 14`；`.md` `901 ＋ 4`；`docs/` `861 ＋ 2`；`verify/out/` `1024 ＋ 2`；子層 `*.py` `375 ＋ 10`；頂層 `*.py` `33`（⛔ 變）；refs `25 ＋ 1`。受單側另生之物（報告以外之落檔、`commit` 訊息所引之檔）須逐筆具名並扣算。

---

## `§五`　`恆常附款` 逐款回掃（`28` 款·`a`／`ab①` 之施行·⛔ 靜默略過）

| 款 | 對本單之施行 |
|---|---|
| `a` | 本單所鑄七則自誤之攔法皆為既有款之施行（`r`／`l`／`m`／`p`／`w`／`q②`）、⛔ 新立 ⇒ 回掃之受詞 ＝ 本表 |
| `b` | 本單⛔ 鑄裁。所鑄 `GB` 二則以受詞之關鍵語（`s_min`／`p1 楔形`／`N0-20`；`wf_f1`／`wf_f4`／側界線登記表）查既有：`GB-172` 與 `N0-20`（`S1_plan:71`／`:84`）**併存**；`GB-173` 為 `W-G.9-308R §五-3` 之**擴充** |
| `c` | 附件 `B` 於 `_corner_buffer_S` 呼叫所在之迴圈體內新讀 `_fo_*`／側界線登記表，讀取點皆在其綁定之後；`probe_WG9308S1_bindorder.py` 於基座與附件 `B` 施作後之沙盒樹皆 `rc 0` |
| `d` | 期值及於倉外之物：工項三-`5`（`run_verification`）**未能於出單前實查** ⇒ 列為觀測、⛔ 期值；工項四之畫面核對⛔ 為本單之閘 |
| `e`／`e②` | `§四-2` 已依其形寫出，並含受單側必生之物 |
| `e③` | `§零-1` 逐號三分 |
| `f` | 本單自載之基數（附件 `17` ＝ `X-0` `1` ＋ 新檔 `10` ＋ 倉外 `2` ＋ 末端追加 `4`；閘 `10`；變動街廓 `A_0` `1`／`A_35` `2`／`B_0` `0`／`B_35` `1`；其餘街廓 `51`／`38`／`29`／`15` 宗；閘十之受詞 `14` 宗）發單側以程式重算（附錄 `P`）；受單側收單時當場重算 |
| `g` | 新檔 `14` 支之路徑以 `git check-ignore -v` 查 ⇒ 命中 `0`（沙盒·態 `2f46579`） |
| `h` | 含反引號之文字一律經檔案管線（附件抽取器）；`X-0` 由 CC 之檔案工具逐字寫出 |
| `i` | 量測之受詞以關鍵語查 `GB` 簿：`GB-170`（本修·擴充其失效條件之現況）、`GB-171`（修屬另單·附件 `C-1 (3)`）、`GB-168`／`169`（⛔ 及於）、`GB-104`（`k917_should_drop` 之 loud 斷言·本修觸及其消費端·閘 `6`／`8` 證其未觸發）；`K-9-23` `§五`（`W-G.9-142` 舊態之 `R2` 左藍影 `76.2056`·本單之 `76.1084` 為現態之值）——皆讀其末端追加 |
| `j` | 本單⛔ 以哨兵之落地後命中為期值 |
| `k` | 「倉內無」之宣稱：`GB-172`〜`179` 全倉 `0`、`自誤 470`〜`479` 全倉 `0`、`CLAUDE.md` 內 `W-G.9-269` `0`——各以 `git grep` 全倉／單檔二框查之；判別力 ＝ 同式之 `GB-171`／`自誤 468`／`W-G.9-268`（`CLAUDE.md`）須命中 |
| `l` | 各閘之框與母體載於閘器之出艙列；附件之 bytes ＝ 區塊內文 ＋ 末一 `LF` |
| `m` | 本單⛔ 設替身。受詞之全部消費者：`_corner_buffer_S` `7` 處（`app.py` `2`·stepg `2`·`wf_f1` `1`·`wf_f4` `2`）、`_pool_strips_for_block` `4` 處（`app.py` `1`·stepg `1`·`wf_f1` `1`·`wf_f4` `1`）、`is_second_after_corner=` 之實參 `4` 處（`app.py` `2`·stepg `2`）；`wf_f*` 之 `5` 處⛔ 改（`GB-173`） |
| `n`／`n④` | 閘一律三值；閘器以 list 形 `subprocess`、呼叫形寫 `python`；每閘備判別力：閘 `1`／`2`（基座須破）、閘 `3`／`4`（擾動副本須被攔）、閘 `5`／`6`／`8`／`10`（工項二之基座對基座須破） |
| `o` | 二樹之差逐（態·情境）比之，母體 ＝ 同一（態·情境）之全部列 ⇒ 可比；態甲與態乙⛔ 互比 |
| `p` | `§零-0` ⛔ 跳序 |
| `q`／`q②` | 本單⛔ 呈 KL；前呈之用語之誤鑄為 `自誤 475`；工項四之 KL 核對事項以地籍語寫之 |
| `r` | 工項二即各閘之基線態（三值） |
| `s` | 閘十之帶（頂點位移 `≤ 0.001` m）有回授（左鏈之變經右鏈求解之上限傳入）⇒ 帶取自**修後**之實測（最大 `0.0005` m）之二倍，⛔ 取改前之值 |
| `t` | 本單⛔ 令以既有文字為錨之純插入（生產碼以 `git apply`、登記以末端追加） |
| `u` | 新接之量 ＝ 側界線中點經 `_first_corner_alloc_dir` 所得之遠側線向；其產生式與 `GB-170`（本項）同、與 `GB-171`（量測軸）⛔ 同 ⇒ 同格具名 `GB-171` 之殘差屬另單（附件 `C-1 (3)`） |
| `v` | 新鑄條目之標題形複刻 `自誤 468`／`GB-171`；以收工閘 `1`／`2` 自驗（發單側已於沙盒乾跑·附錄 `P`） |
| `w` | `§四-1` 之算式；`blob` 錨同格載其態（主線／凍存分支） |
| `x` | 工項五-`2` 三值 |
| `y` | `§二` 之逐筆放行清單 |
| `z` | 本單⛔ 以人造哨兵充［必為零］ |
| `aa` | 全稱否定（`k` 列）之判別力取同形族已知成員 |
| `ab` | ① 本單⛔ 立、⛔ 修款；② 本單⛔ 取正典索引可得之物 |

---

## `§五-1`　驗收與上呈

1. 受單側收單時當場重算 `§零-1` 與 `恆常附款 f` 之基數；出艙 `§零-2` 十一款之三值。
2. 報告入倉後，發單側以拋棄式 clone 獨立復驗：凍存分支之二 blob、閘器之重跑、四簿與母體；⛔ 採信報告之自述。
3. **入主線**須 KL 另一次放行：發單側於復驗畢、KL 畫面核對畢後擬呈文（逐態並列·附平面圖·以地籍語）；⛔ CC 自呈。
4. 上呈之意思決定（`§三` 任一停機後之取捨）⛔ CC 自裁。

---

## 附錄 `P`　發單側出單前之自驗（沙盒·`2026-09-22`）

🔒 本附錄之數皆發單側沙盒實跑（Linux·shapely `2.1.2`／GEOS `3.13.1`·基座 `2f46579`）；受單側之機器所得若於 `1e-4` 以內相異，依各款之判準處置。

**P-1　pre-flight**（`probe_order_preflight.py` 對本單之乾跑版）：`rc 0`；🔴 `0` 項；🟡 `3` 項，逐項處置如下（列號以出單版為準，受單側重跑得之）：
- `[P-1]` 命中附件 `X-0` 之碼行 `sys.stdout.reconfigure(encoding="utf-8")` ⇒ **豁免**：碼文之字樣，⛔ 為全稱否定之宣稱。
- `[P-4]` 命中工項五-`1`「切回主線」⇒ **豁免**：指 `git` 分支之切換，⛔ 為幾何方向之轉引。
- `[P-4]` 命中附件 `B` 之碼行 `def _band_area(buf):` 一帶 ⇒ **豁免**：diff 之碼文；其方向語之座標系由碼內之參數（`d_hat`／`allocation_dir`／`far_line_dir`）定之。
- `[P-5]` 相符；`[P-3]` `def main` 區間已實查，本單⛔ 以 `app.py:N` 為閘之受詞（受檢之閘皆經 stepg 之 harness 路徑）。

**P-2　乾跑**（倉外 worktree 自 `2f46579`·`commit` ⛔ `push`）：抽取器 `rc 0`（附件 `17`）；`c1` 新檔 `11`（本單 ＋ 器 `10`）·刪除 `0`；附件 `B` 施作後 blob ＝ `5ceddfce…`／`e4bd912b…`、`2 files changed, 94 insertions(+), 23 deletions(-)`；四則末端追加皆嚴格前綴 ✅（`945020 → 949934`／`989176 → 996655`／`370539 → 371944`／`238340 → 239352` B）；`c3` 後收工閘 `475 468` ⇒ `rc 0`、態錨器 `475 468` ⇒ `rc 0`：自誤 `465`／`475`／`[106,355,356,357]`（自擬 `461`）、`GB` `171`／`173`／`[12,87]`、`VR` `80`／`95`、`K-9` `42`／`43`；全倉 `2634`／`.md` `905`／`docs/` `863`／`verify/out/` `1026`／子層 `*.py` `385`（交叉檢 `418`）。

**P-3　閘器之自證**：受驗樹 ＝ 附件 `B` 施作後 ⇒ `rc 0`·十閘 🟢；基座對基座 ⇒ `rc 7`（閘 `1`／`2`／`5`／`6`／`8`／`10` 🔴·閘 `9` 🛑·閘 `3`／`4`／`7` 🟢）；閘 `3`／`4` 之擾動副本（`A_35`·`R2` 左二宗疊合）皆被攔。受單側之呼叫形（list 形 `subprocess` 與 `PYTHONIOENCODING`）以單格實跑一次證其可行。

**P-4　其餘**：
- 原型 `P3`（受檢宗序之判別式）與附件 `B`（`P3` ＋ 畫面路徑之鏡射 ＋ docstring）於 harness 四格之逐宗列與閘值**逐位相同**（畫面路徑不經 harness）。
- 附件 `B` 之畫面路徑三處，以 AST 查其所讀之名皆於同一逐街廓迴圈內先綁後讀；界面單線鏈之初值位於巢狀函式 `_advance_block_with_split` 內，以閉包讀之，與既有之 `_fo_*` 同法。
- 靜態器 `probe_WG9308S1_bindorder.py`／`probe_WG91_static_checks.py`／`probe_WG918_downcast.py` 於基座與附件 `B` 施作後皆 `rc 0`。
- 閘十之歸因試驗（二拋棄式副本令右鏈求解之上限不含左鏈累積量）：`R2` 右鏈 `7`／`7` 宗由相異轉為逐位相同 ⇒ 右鏈之次毫米位移係既存之耦合，⛔ 為附件 `B` 之邏輯所致。
- 基座之既有遞補剔除（`K917_DROPPED`）：甲 `0m` `R2` 左 `628-27(1)`／`628-42(1)`、`R5` 左 `628-53(2)`；甲 `3.5m` `R5` 左 `628-53(2)`；乙 `0m` `R2` 左 `628-27(1)`／`628-42(1)`；乙 `3.5m` 無 ⇒ 附件 `B` 新增者僅 `3.5m` 二態之 `R2` 左 `628-42(1)`（閘 `6`）。

---

## 附件（`X-0` 之抽取器依標題列之形讀之·⛔ 改標題列一字）

| 附件 | 方式 | 路徑 | bytes | sha256 |
|---|---|---|---|---|
| `X-0` | 倉外 | `extract_wg9309.py` | `3238` | `e42376c06e5fdc8d…` |
| `A-1` | 新檔 | `verify/probes/probe_WG9309_gates.py` | `10845` | `8c2e9f095374d817…` |
| `A-2` | 新檔 | `verify/probes/wg9309/chk_wg9309.py` | `7004` | `8a9515ffbf467315…` |
| `A-3` | 新檔 | `verify/probes/wg9309/synth_attr.py` | `2800` | `50d6df21f1c58230…` |
| `A-4` | 新檔 | `verify/probes/wg9309/chk_p3.py` | `6845` | `55a79d4be63951f2…` |
| `A-5` | 新檔 | `verify/probes/wg9309/drv.py` | `2776` | `714cd40e7f7e960f…` |
| `A-6` | 新檔 | `verify/probes/wg9309/chk_band.py` | `3951` | `48eebccbffe685dd…` |
| `A-7` | 新檔 | `verify/probes/wg9309/cmp.py` | `1224` | `5cf1f503c441a5a3…` |
| `A-8` | 新檔 | `verify/probes/wg9309/drv_p2b.py` | `3552` | `b9d01966d71063a6…` |
| `A-9` | 新檔 | `verify/probes/wg9309/ovl2.py` | `2169` | `5e0fc328cf52771e…` |
| `A-10` | 新檔 | `verify/probes/wg9309/r2_geom.py` | `698` | `2aa10f9f5143c074…` |
| `B` | 倉外 | `W-G.9-309_P4.diff` | `20176` | `5356801be3c09ccf…` |
| `B-1` | 倉外 | `W-G.9-309_B1_土地影響.md` | `4626` | `264a41347c171a2f…` |
| `C-1` | 末端追加 | `docs/reports/W-G.4_泛用阻塞項登記表.md` | `4914` | `33cfde2ac43530c1…` |
| `C-2` | 末端追加 | `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `7479` | `406ec0010088569e…` |
| `C-3` | 末端追加 | `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `1405` | `d12b394a6e6b6c15…` |
| `C-4` | 末端追加 | `CLAUDE.md` | `1012` | `16b95b767c03e2e5…` |

#### 附件 X-0　倉外　`extract_wg9309.py`　sha256 `e42376c06e5fdc8de6532c68fde7e31795c70b0184d055ae0c2869cb63fc712b`

````python
# -*- coding: utf-8 -*-
# W-G.9-309 附件抽取器（附件 X-0·受單側以檔案管線造之·⛔ 命令列貼上）
# 用法：python extract_wg9309.py <本單之路徑> <倉之根> <倉外暫存目錄> [--append]
#   新檔     ⇒ 寫入 <倉之根>/<路徑>（既存即停）
#   倉外     ⇒ 寫入 <倉外暫存目錄>/<路徑>
#   末端追加 ⇒ 無 --append 時只驗其 sha256 並寫副本至 <倉外暫存目錄>/<檔名>.append；
#              有 --append 時於驗畢後逕附於 <倉之根>/<路徑> 之末（目標須存在且以 LF 結尾）
# rc ＝ 問題數；一切寫檔皆 LF、UTF-8、⛔ 轉換行尾。
import hashlib
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ORDER, REPO, OUTSIDE = sys.argv[1], sys.argv[2], sys.argv[3]
APPEND = "--append" in sys.argv[4:]
raw = open(ORDER, "rb").read()
if b"\r" in raw:
    print("🔴 本單含 CR ⇒ 行尾已被轉換 ⇒ 停"); sys.exit(1)
t = raw.decode("utf-8")
pat = re.compile(r"^#### 附件 (\S+)\u3000(新檔|倉外|末端追加)\u3000`([^`]+)`\u3000sha256 `([0-9a-f]{64})`\n\n````[a-z]*\n(.*?)\n````$",
                 re.M | re.S)
items = pat.findall(t)
bad = 0
seen = set()
print("附件數 ＝ %d" % len(items))
for aid, mode, path, want, body in items:
    if aid in seen:
        print("🔴 %s 重出" % aid); bad += 1; continue
    seen.add(aid)
    data = (body + "\n").encode("utf-8")
    got = hashlib.sha256(data).hexdigest()
    ok = got == want
    msg = "%s %s %s %d B sha256 %s" % (aid, mode, path, len(data), "✅" if ok else "🔴 實 %s" % got)
    if not ok:
        bad += 1; print(msg); continue
    if aid == "X-0":
        print(msg + "（自身·⛔ 寫出）"); continue
    if APPEND and mode != "末端追加":
        print(msg + "（--append 期·略）"); continue
    if mode == "新檔":
        dst = os.path.join(REPO, *path.split("/"))
        if os.path.exists(dst):
            print(msg + " 🔴 目標既存"); bad += 1; continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "wb").write(data); print(msg + " → 寫出")
    elif mode == "倉外":
        dst = os.path.join(OUTSIDE, *path.split("/"))
        os.makedirs(os.path.dirname(dst) or OUTSIDE, exist_ok=True)
        open(dst, "wb").write(data); print(msg + " → 倉外")
    else:
        dst = os.path.join(REPO, *path.split("/"))
        if not os.path.exists(dst):
            print(msg + " 🔴 目標不存在"); bad += 1; continue
        cur = open(dst, "rb").read()
        if not cur.endswith(b"\n") or b"\r" in cur:
            print(msg + " 🔴 目標非 LF 結尾或含 CR"); bad += 1; continue
        os.makedirs(OUTSIDE, exist_ok=True)
        open(os.path.join(OUTSIDE, os.path.basename(path) + ".append"), "wb").write(data)
        if APPEND:
            open(dst, "ab").write(data)
            new = open(dst, "rb").read()
            pref = new[:len(cur)] == cur and new[len(cur):] == data
            print(msg + (" → 已附（嚴格前綴 ✅·%d → %d B）" % (len(cur), len(new)) if pref else " 🔴 附後嚴格前綴破"))
            bad += 0 if pref else 1
        else:
            print(msg + " → 已驗（未附）")
print("rc ＝ %d" % bad)
sys.exit(bad)
````

#### 附件 A-1　新檔　`verify/probes/probe_WG9309_gates.py`　sha256 `8c2e9f095374d8179002d12897e77a6d123069e84b133c3c432a83c526430567`

````python
# -*- coding: utf-8 -*-
r"""`W-G.9-309` 之閘器（發單側擬·隨單入倉·⛔ 零生產碼）

用法：python verify/probes/probe_WG9309_gates.py <基座樹> <受驗樹> <出艙目錄>
  基座樹 ＝ `2f46579` 之拋棄式 worktree；受驗樹 ＝ 施作後之 worktree（或凍存分支之 checkout）。
  逐（態·情境）以 `verify/probes/wg9309/chk_wg9309.py` 驅動二樹（list 形 `subprocess`·`n④`），
  另以 `verify/probes/wg9309/synth_attr.py` 驅動受驗樹。
出艙 ＝ `<出艙目錄>/WG9309_gates.md` ＋ 逐格 JSON；`rc` ＝ 🔴 閘數（🛑 未執行者亦計入）。

🔒 閘一律三值（🟢 已執行且通過／🛑 未執行／🔴 已執行且破·`恆常附款 n`）。
🔒 閘一、閘二之判別力 ＝ 基座樹之同量須為 🔴（**[必命中]**）；基座樹竟為 🟢 ⇒ 該閘不可證偽 ⇒ 🔴。
"""
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "wg9309")
BASE, NEW, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
ENV = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")   # 🔒 Windows 之管線編碼（受單側主 checkout）
CELLS = [("A_0", "甲", "0.0"), ("A_35", "甲", "3.5"), ("B_0", "乙", "0.0"), ("B_35", "乙", "3.5")]
# 🔒 期值（發單側於沙盒實測·窗二十一·`2026-09-22`·基座 `2f46579`）
EXPECT_CHANGED = {"A_0": ["R4"], "A_35": ["R2", "R4"], "B_0": [], "B_35": ["R2"]}
EXPECT_NEWDROP = {"A_0": {}, "A_35": {"R2/left": ["628-42(1)"]}, "B_0": {}, "B_35": {"R2/left": ["628-42(1)"]}}
EXPECT_SYNTH = "{('left', 'bad', 's_min<0'): 12, ('left', 'ok', 's_min>=0'): 12, ('right', 'ok', 's_min>=0'): 24}"
TOL_G1, TOL_G2, TOL_G4, TOL_SHIFT = 0.005, 1e-6, 1e-3, 1e-3

log = []
def say(s=""):
    print(s); log.append(s)

def run(tree, tag, mode, sb):
    out = os.path.join(OUT, "WG9309_%s_%s.json" % (tag, mode + "_" + sb))
    cp = subprocess.run([sys.executable, os.path.join(TOOLS, "chk_wg9309.py"), tree, mode, sb, out],
                        capture_output=True, env=ENV)
    if cp.returncode != 0 or not os.path.exists(out):
        return None, cp.returncode
    return json.load(open(out, encoding="utf-8")), 0

def key(r):
    return (r["所屬街廓"], r["推進側別"], r["暫編地號"])

def drops(d):
    return {k: sorted(set(x["暫編地號"] for x in v)) for k, v in (d["gates"]["dropped"] or {}).items()}

def maxshift(a, b):
    from shapely.geometry import Polygon
    pa, pb = Polygon(a), Polygon(b)
    return max(min(((x - u) ** 2 + (y - v) ** 2) ** 0.5 for u, v in pb.exterior.coords) for x, y in pa.exterior.coords)

G = {}
def gate(name, ok, detail):
    v = "🛑 未執行" if ok is None else ("🟢 已執行且通過" if ok else "🔴 已執行且破")
    G[name] = v; say("| %s | %s | %s |" % (name, v, detail))

say("# `W-G.9-309` 閘器出艙")
say("基座樹 ＝ `%s`；受驗樹 ＝ `%s`" % (BASE, NEW))
R = {}
for c, m, sb in CELLS:
    b, rb = run(BASE, "base", m, sb)
    n, rn = run(NEW, "new", m, sb)
    R[c] = (b, n)
    say("- 格 `%s`：基座 %s／受驗 %s" % (c, "rc 0" if b else "🔴 rc %s" % rb, "rc 0" if n else "🔴 rc %s" % rn))
say()
say("| 閘 | 三值 | 細 |")
say("|---|---|---|")
ok_run = all(b is not None and n is not None for b, n in R.values())
if not ok_run:
    for nm in ("閘1", "閘2", "閘3", "閘4", "閘5", "閘6", "閘7", "閘8", "閘10"):
        gate(nm, None, "驅動失敗 ⇒ 未執行")
else:
    # 閘1／閘2（受驗樹 ＋ 基座判別力）
    g1n, g1b, g2n, g2b, nb = [], [], [], [], 0
    for c, (b, n) in R.items():
        for tag, d, g1, g2 in (("new", n, g1n, g2n), ("base", b, g1b, g2b)):
            for blk, bg in d["gates"]["blocks"].items():
                for x in bg["bands"]:
                    if tag == "new": nb += 1
                    g1.append((c, blk, x["side"], x["g1_symdiff_mat_range"]))
                    g2.append((c, blk, x["side"], sum(v for _, v in x["g2_range_owner"])))
    g1_new_ok = nb > 0 and all(v is not None and v <= TOL_G1 for *_, v in g1n)
    g1_base_red = len(g1b) > 0 and all(v is None or v > TOL_G1 for *_, v in g1b)
    gate("閘1", g1_new_ok and g1_base_red, "強制抵費地物化形 vs 規定範圍（界 `%s`）：受驗 %s｜基座[必命中]須全破 %s（強制側數 `%d`）" % (TOL_G1, g1n, g1b, nb))
    g2_new_ok = nb > 0 and all(v <= TOL_G2 for *_, v in g2n)
    g2_base_red = any(v > TOL_G2 for *_, v in g2b)
    gate("閘2", g2_new_ok and g2_base_red, "規定範圍 ∩ 業主宗：受驗 %s｜基座[必命中]須至少一破 %s" % (g2n, g2b))
    # 閘3／閘4（自列重算·⛔ 採信量測器之欄）＋ 判別力造（擾動副本須被攔）
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    def g34(rows, blocks):
        b3, b4 = [], []
        for blk, bg in blocks.items():
            R_ = [r for r in rows if r["所屬街廓"] == blk and isinstance(r.get("cut_coords"), list) and len(r["cut_coords"]) >= 3]
            own = [(r["暫編地號"], Polygon(r["cut_coords"])) for r in R_ if r["推進側別"] in ("left", "right")]
            allp = [Polygon(r["cut_coords"]) for r in R_]
            inv = [k for k, q in own if not q.is_valid]
            ov = [(own[i][0], own[j][0]) for i in range(len(own)) for j in range(i + 1, len(own)) if own[i][1].intersection(own[j][1]).area > 1e-6]
            if inv or ov: b3.append((blk, inv, ov))
            ua = unary_union(allp).area if allp else 0.0
            if abs(sum(q.area for q in allp) - bg["block_area"]) > TOL_G4 or abs(ua - bg["block_area"]) > TOL_G4: b4.append((blk, round(sum(q.area for q in allp) - bg["block_area"], 6)))
        return b3, b4
    bad3, bad4, nblk = [], [], 0
    for c, (b, n) in R.items():
        x3, x4 = g34(n["rows"], n["gates"]["blocks"]); nblk += len(n["gates"]["blocks"])
        bad3 += [(c,) + t for t in x3]; bad4 += [(c,) + t for t in x4]
    _c0 = R["A_35"][1]; _rows = [dict(r) for r in _c0["rows"]]
    _own = [r for r in _rows if r["所屬街廓"] == "R2" and r["推進側別"] == "left"]
    _own[1]["cut_coords"] = [list(t) for t in _own[0]["cut_coords"]]            # 擾動：二宗疊合
    p3, p4 = g34(_rows, {"R2": _c0["gates"]["blocks"]["R2"]})
    say("  - 閘3／閘4 判別力造（`A_35`·`R2` 左二宗疊合之擾動副本）：閘3 攔 `%s`·閘4 攔 `%s`" % (bool(p3), bool(p4)))
    gate("閘3", nblk > 0 and not bad3 and bool(p3), "業主宗有效且兩兩不重疊（受驗·街廓格數 `%d`）：破 %s" % (nblk, bad3))
    gate("閘4", nblk > 0 and not bad4 and bool(p4), "街廓面積守恆（Σ ≡ 聯集 ≡ 街廓面積·界 `%s`）：破 %s" % (TOL_G4, bad4))
    # 閘5／閘6／閘7／閘8／閘10
    bad5, bad6, bad7, bad8, bad10, n10 = [], [], [], [], [], 0
    for c, (b, n) in R.items():
        ra = {key(r): r for r in b["rows"]}; rn = {key(r): r for r in n["rows"]}
        ch = sorted(set(k[0] for k in set(ra) | set(rn) if ra.get(k) != rn.get(k)))
        oth = [k for k in set(ra) | set(rn) if k[0] not in ch]
        same = sum(1 for k in oth if ra.get(k) == rn.get(k))
        if ch != EXPECT_CHANGED[c] or same != len(oth) or not oth: bad5.append((c, ch, same, len(oth)))
        say("  - `%s` 變動街廓 %s（期 %s）·其餘逐位 `%d／%d`" % (c, ch, EXPECT_CHANGED[c], same, len(oth)))
        da, dn = drops(b), drops(n)
        newd = {k: sorted(set(dn.get(k, [])) - set(da.get(k, []))) for k in dn if set(dn.get(k, [])) - set(da.get(k, []))}
        gone = {k: sorted(set(da.get(k, [])) - set(dn.get(k, []))) for k in da if set(da.get(k, [])) - set(dn.get(k, []))}
        if newd != EXPECT_NEWDROP[c] or gone: bad6.append((c, newd, gone))
        if b["err"] != n["err"] or (c.startswith("B_") and not b["err"]): bad7.append((c, (b["err"] or "")[:60], (n["err"] or "")[:60]))
        if EXPECT_NEWDROP[c]:
            chain = [r for r in n["rows"] if r["所屬街廓"] == "R2" and r["推進側別"] == "left"]
            h = chain[0] if chain else {}
            if h.get("暫編地號") != "628-41(1)" or h.get("驗_宗序") != "第2宗" or h.get("驗_B藍影") != "合格":
                bad8.append((c, h.get("暫編地號"), h.get("驗_宗序"), h.get("驗_B藍影")))
        for k in set(ra) & set(rn):
            if k[0] in ch and k[1] in ("left", "right"):
                side_forced = bool((n.get("forced") or {}).get(k[0], {}).get(k[1] + "_forced_offset", False))
                if not side_forced:
                    n10 += 1
                    s = maxshift(ra[k]["cut_coords"], rn[k]["cut_coords"])
                    if ra[k]["G(㎡)"] != rn[k]["G(㎡)"] or s > TOL_SHIFT: bad10.append((c, k, ra[k]["G(㎡)"], rn[k]["G(㎡)"], round(s, 6)))
    gate("閘5", not bad5, "變動街廓之集 ＝ 期值且其餘街廓逐宗逐位相同：破 %s" % bad5)
    gate("閘6", not bad6, "遞補剔除之差（受驗 − 基座）＝ 期值且無消失：破 %s" % bad6)
    gate("閘7", not bad7, "停機訊息二樹同一·態乙之基座須非空（既存之 `R4` 右結構閘）：破 %s" % bad7)
    gate("閘8", sum(1 for c in EXPECT_NEWDROP if EXPECT_NEWDROP[c]) > 0 and not bad8, "強制側鏈首（緊鄰強制抵費地）＝ `628-41(1)`·`第2宗`·藍影合格：破 %s" % bad8)
    gate("閘10", n10 > 0 and not bad10, "變動街廓之非強制鏈：`G` 同一且頂點位移 ≤ `%s` m（受詞宗數 `%d`）：破 %s" % (TOL_SHIFT, n10, bad10))
# 閘9 合成例（受驗樹）
cp = subprocess.run([sys.executable, os.path.join(TOOLS, "synth_attr.py"), NEW], capture_output=True, env=ENV)
got = cp.stdout.decode("utf-8", "replace").strip().split("\n")[-1] if cp.returncode == 0 else ""
gate("閘9", (got == EXPECT_SYNTH) if cp.returncode == 0 else None, "合成例計數 ＝ `%s`（期 `%s`）" % (got, EXPECT_SYNTH))
# 土地影響表（變動街廓·基座 → 受驗）
say()
say("## 土地影響（變動街廓·基座 → 受驗）")
for c, (b, n) in R.items():
    if not (b and n): continue
    ra = {key(r): r for r in b["rows"]}; rn = {key(r): r for r in n["rows"]}
    for k in sorted(set(ra) | set(rn)):
        if k[0] in EXPECT_CHANGED[c] and ra.get(k) != rn.get(k):
            f = lambda r, x: "—" if r is None else r.get(x)
            say("- `%s` %s｜G %s → %s｜幾何 %s → %s｜負擔比率 %s → %s" % (c, "/".join(k), f(ra.get(k), "G(㎡)"), f(rn.get(k), "G(㎡)"),
                f(ra.get(k), "幾何面積(㎡)"), f(rn.get(k), "幾何面積(㎡)"), f(ra.get(k), "負擔比率"), f(rn.get(k), "負擔比率")))
red = sum(1 for v in G.values() if not v.startswith("🟢"))
say()
say("rc ＝ 非 🟢 閘數 ＝ `%d`（閘數 `%d`）" % (red, len(G)))
open(os.path.join(OUT, "WG9309_gates.md"), "w", encoding="utf-8", newline="\n").write("\n".join(log) + "\n")
sys.exit(red)
````

#### 附件 A-2　新檔　`verify/probes/wg9309/chk_wg9309.py`　sha256 `8a9515ffbf46731586361c2071d34fc95d83558e50520c8525d593fb96e7849f`

````python
# `W-G.9-309` 之四閘量測器（發單側擬·隨單入倉）：綁土地性質·⛔ 綁中間量·任一樹皆可驅動
#  ① 強制抵費地之物化形 ≡ 規定範圍多邊形（對稱差 ≤ 0.005 ㎡）——物化形 ＝ 與規定範圍交集最大之池片
#  ② 規定範圍多邊形 ∩ 全部業主宗 ≤ 1e-6 ㎡（強制側·以規定範圍為受詞·⛔ 以帶為受詞）
#  ③ 業主宗兩兩不重疊（≤ 1e-6）且皆為有效多邊形；強制側緊鄰宗之藍影判與臨接長
#  ④ 街廓面積守恆（全部列之聯集 ≡ 街廓·Σ 面積 ≡ 街廓面積）
# 用法：python chk_wg9309.py <repo> <甲|乙> <0.0|3.5> <out.json>
import contextlib, io, os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3]); OUT = sys.argv[4]
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from shapely.geometry import Polygon
from shapely.ops import unary_union
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
cap = {}; crp = {}
_o_ps = ns["_pool_strips_for_block"]
def _ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    cap[_label] = dict(block=block_poly)
    _kw = {} if forced_bands is None else {"forced_bands": forced_bands}
    return _o_ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, **_kw)
ns["_pool_strips_for_block"] = _ps
_olg = ns["_lot_gate"]
def _lg(res, tp, ctx, *a, **k):
    cp = (ctx.get("corner_range_polys") or {}).get(k.get("chain_side"))
    if cp is not None: crp[(k.get("_label"), k.get("chain_side"))] = cp
    return _olg(res, tp, ctx, *a, **k)
ns["_lot_gate"] = _lg
ns["K917_DROPPED"].clear()
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
err = None
with contextlib.redirect_stdout(io.StringIO()):
    try:
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
        g_rows = sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:300]; g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
dropped = {f"{k[0]}/{k[1]}": v for k, v in ns["K917_DROPPED"].items()}
rows = []
for r in g_rows:
    d = {}
    for k, v in r.items():
        if k == "cut_coords":
            try: d[k] = [[float(a), float(b)] for a, b in v] if v and not isinstance(v, str) else v
            except Exception: d[k] = str(v)
        else:
            try: json.dumps(v); d[k] = v
            except Exception: d[k] = str(v)
    rows.append(d)
def poly(r):
    c = r.get("cut_coords")
    return Polygon(c) if isinstance(c, list) and len(c) >= 3 else None
G = {"err": err, "dropped": dropped, "blocks": {}}
for blk, c in cap.items():
    R = [r for r in rows if r["所屬街廓"] == blk]
    own = [(r["暫編地號"], poly(r)) for r in R if r["推進側別"] in ("left", "right")]
    pools = [(r["暫編地號"], poly(r)) for r in R if r["推進側別"] == "抵費地"]
    allp = [p for _, p in own + pools if p is not None]
    bg = {}
    bg["n_own"] = len(own); bg["n_pool"] = len(pools)
    bg["own_invalid"] = [k for k, p in own if p is None or not p.is_valid]
    ov = []
    for i in range(len(own)):
        for j in range(i + 1, len(own)):
            a, b = own[i][1], own[j][1]
            if a is not None and b is not None:
                x = a.intersection(b).area
                if x > 1e-6: ov.append((own[i][0], own[j][0], round(x, 6)))
    bg["own_own_overlap"] = ov
    bl = c["block"]
    bg["block_area"] = round(bl.area, 6); bg["sum_rows"] = round(sum(p.area for p in allp), 6)
    bg["union_symdiff_block"] = round(unary_union(allp).symmetric_difference(bl).area, 6) if allp else None
    bands = []
    fo = forced.get(blk, {}) if isinstance(forced, dict) else {}
    for side in ("left", "right"):
        if not fo.get(side + "_forced_offset", False):
            continue
        rng = crp.get((blk, side))
        cand = [(k, p) for k, p in pools if p is not None and rng is not None and p.intersection(rng).area > 1e-6]
        mat = max(cand, key=lambda kp: kp[1].intersection(rng).area) if cand else None
        bands.append(dict(side=side, range_area=(None if rng is None else round(rng.area, 6)),
                          mat_piece=(None if mat is None else mat[0]), mat_area=(None if mat is None else round(mat[1].area, 6)),
                          g1_symdiff_mat_range=(None if (mat is None or rng is None) else round(mat[1].symmetric_difference(rng).area, 6)),
                          g2_range_owner=([] if rng is None else [(k, round(p.intersection(rng).area, 6)) for k, p in own if p is not None and p.intersection(rng).area > 1e-6])))
    bg["bands"] = bands
    adj = [dict(k=r["暫編地號"], side=r["推進側別"], G=r["G(㎡)"], 序=r.get("驗_宗序"), B=r.get("驗_B藍影"),
                藍影=r.get("驗_B_藍影面積"), 正街=r.get("驗_B_臨正街"), 屁股=r.get("驗_B_臨屁股"),
                nv=(None if poly(r) is None else len(poly(r).exterior.coords) - 1))
           for r in R if r.get("驗_宗序") in ("第2宗", "街角第1宗")]
    bg["checked_lots"] = adj
    G["blocks"][blk] = bg
json.dump({"mode": MODE, "sb": SB, "err": err, "forced": forced, "rows": rows, "gates": G}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, default=str)
print(json.dumps({"mode": MODE, "sb": SB, "err": (err or "")[:120], "n_rows": len(rows), "dropped": dropped}, ensure_ascii=False, default=str))
for blk, bg in G["blocks"].items():
    flag = []
    if bg["own_invalid"]: flag.append("invalid")
    if bg["own_own_overlap"]: flag.append("own-ov")
    if bg["union_symdiff_block"] is not None and bg["union_symdiff_block"] > 1e-3: flag.append("union≠block")
    for b in bg["bands"]:
        if b["g1_symdiff_mat_range"] is None or b["g1_symdiff_mat_range"] > 0.005: flag.append("g1")
        if b["g2_range_owner"]: flag.append("g2")
    print(blk, "OK" if not flag else flag, "blk", bg["block_area"], "Σ", bg["sum_rows"], "∪Δ", bg["union_symdiff_block"],
          "bands", [(b["side"], b["mat_piece"], b["mat_area"], b["range_area"], b["g1_symdiff_mat_range"], b["g2_range_owner"]) for b in bg["bands"]])
    for a in bg["checked_lots"]:
        print("   ", a)
````

#### 附件 A-3　新檔　`verify/probes/wg9309/synth_attr.py`　sha256 `50d6df21f1c58230dde42b4555d0571fe51f6d96b5c5c8e20225632913de35e8`

````python
# 發單側原型檢核（scratch）：右側分支之合成例（甲-3）——強制帶 vs 解析之規定範圍（SIDELINE 內移 D）
import os, sys, io, contextlib, math
import numpy as np
from shapely.geometry import Polygon, LineString
from shapely import affinity
REPO=sys.argv[1]
sys.path.insert(0, os.path.join(REPO,"verify"))
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns,_ = harvest(os.path.join(REPO,"app.py"))
def unit(v): v=np.asarray(v,float); return v/np.linalg.norm(v)
def case(side, side_tilt_deg, alloc_tilt_deg, D, fd_sign):
    # FRONT 沿 x 軸 (0,0)→(60,0)；深 30；SIDELINE 在 side 端，傾 side_tilt
    t=math.radians(side_tilt_deg)
    if side=='right':
        s0=np.array([60.0,0.0]); s1=s0+30*np.array([math.tan(t),1.0])
        blk=Polygon([(0,0),tuple(s0),tuple(s1),(0,30)])
    else:
        s0=np.array([0.0,0.0]); s1=s0+30*np.array([math.tan(t),1.0])
        blk=Polygon([tuple(s0),(60,0),(60,30),tuple(s1)])
    sv=unit(s1-s0)                                   # SIDE 線向
    nrm=np.array([sv[1],-sv[0]]) if side=='left' else np.array([-sv[1],sv[0]])  # 指向街廓內
    nrm = nrm if np.dot(nrm, np.array(blk.centroid.coords[0])-s0)>0 else -nrm
    # 解析之規定範圍：街廓 ∩ {距 SIDELINE ≤ D}
    big=1e4
    p=s0+D*nrm
    hp=Polygon([tuple(s0-big*sv),tuple(s0+big*sv),tuple(p+big*sv),tuple(p-big*sv)])
    rng=blk.intersection(hp)
    a=math.radians(alloc_tilt_deg); allocation_dir=np.array([math.cos(a),math.sin(a)])   # ⊥ ALLOC 線
    d_hat=np.array([1.0,0.0]); front_p1=np.array([0.0,0.0])
    fd=fd_sign*np.array([sv[1],-sv[0]])              # ⊥ SIDE（±）
    with contextlib.redirect_stdout(io.StringIO()):
        buf=ns["_corner_buffer_S"](blk,d_hat,front_p1,allocation_dir,float(rng.area),side,_label='synth',far_line_dir=fd)
        g,ar=ns["_corner_band_geom"](blk,d_hat,front_p1,allocation_dir,buf,side,far_line_dir=fd)
    sd=g.symmetric_difference(rng).area
    dom=ns['_strip_s_range'](blk,d_hat,front_p1,allocation_dir)
    return dict(s_min=float(dom[0]),s_max=float(dom[1]),side=side,side_tilt=side_tilt_deg,alloc_tilt=alloc_tilt_deg,D=D,fd_sign=fd_sign,range=round(rng.area,6),band=round(ar,6),buf=round(buf,6),symdiff=sd)

from collections import Counter
cnt=Counter()
for side in ('left','right'):
    for st in (-6.0,-2.7,2.7,6.0):
        for at in (0.0,3.0,-4.0):
            for sg in (1,-1):
                r=case(side,st,at,7.0,sg)
                bad=r['symdiff']>1e-3
                neg=(r['s_min']<-1e-9) if side=='left' else (r['s_max']>60+1e-9)
                cnt[(side,'bad' if bad else 'ok','s_min<0' if (side=='left' and r['s_min']<-1e-9) else 's_min>=0')]+=1
                mx=max(cnt.get('mx',0), r['symdiff'] if not bad else 0)
print(dict(cnt))
````

#### 附件 A-4　新檔　`verify/probes/wg9309/chk_p3.py`　sha256 `55a79d4be63951f28a5594d4e2e9e4480133516feb62dc4b70a5475d6c02e50a`

````python
# 發單側原型檢核（scratch·不入倉）：P3 之四閘（綁土地性質·⛔ 綁中間量）
#  ① 強制抵費地之物化形 ≡ 規定範圍多邊形（對稱差 ≤ 0.005 ㎡）
#  ② 強制帶 ∩ 全部業主宗 ≤ 1e-6 ㎡
#  ③ 業主宗兩兩不重疊（≤ 1e-6）且皆為有效多邊形；強制側緊鄰宗之藍影判與臨接長
#  ④ 街廓面積守恆（全部列之聯集 ≡ 街廓·Σ 面積 ≡ 街廓面積）
# 用法：python3 chk_p3.py <repo> <甲|乙> <0.0|3.5> <out.json>
import contextlib, io, os, sys, json
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3]); OUT = sys.argv[4]
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from shapely.geometry import Polygon
from shapely.ops import unary_union
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
cap = {}; crp = {}
_o_ps = ns["_pool_strips_for_block"]
def _ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    cap[_label] = dict(block=block_poly, bands=list(forced_bands or []))
    _kw = {} if forced_bands is None else {"forced_bands": forced_bands}
    return _o_ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, **_kw)
ns["_pool_strips_for_block"] = _ps
_olg = ns["_lot_gate"]
def _lg(res, tp, ctx, *a, **k):
    cp = (ctx.get("corner_range_polys") or {}).get(k.get("chain_side"))
    if cp is not None: crp[(k.get("_label"), k.get("chain_side"))] = cp
    return _olg(res, tp, ctx, *a, **k)
ns["_lot_gate"] = _lg
ns["K917_DROPPED"].clear()
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
err = None
with contextlib.redirect_stdout(io.StringIO()):
    try:
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
        g_rows = sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:300]; g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
dropped = {f"{k[0]}/{k[1]}": v for k, v in ns["K917_DROPPED"].items()}
rows = []
for r in g_rows:
    d = {}
    for k, v in r.items():
        if k == "cut_coords":
            try: d[k] = [[float(a), float(b)] for a, b in v] if v and not isinstance(v, str) else v
            except Exception: d[k] = str(v)
        else:
            try: json.dumps(v); d[k] = v
            except Exception: d[k] = str(v)
    rows.append(d)
def poly(r):
    c = r.get("cut_coords")
    return Polygon(c) if isinstance(c, list) and len(c) >= 3 else None
G = {"err": err, "dropped": dropped, "blocks": {}}
for blk, c in cap.items():
    R = [r for r in rows if r["所屬街廓"] == blk]
    own = [(r["暫編地號"], poly(r)) for r in R if r["推進側別"] in ("left", "right")]
    pools = [(r["暫編地號"], poly(r)) for r in R if r["推進側別"] == "抵費地"]
    allp = [p for _, p in own + pools if p is not None]
    bg = {}
    bg["n_own"] = len(own); bg["n_pool"] = len(pools)
    bg["own_invalid"] = [k for k, p in own if p is None or not p.is_valid]
    ov = []
    for i in range(len(own)):
        for j in range(i + 1, len(own)):
            a, b = own[i][1], own[j][1]
            if a is not None and b is not None:
                x = a.intersection(b).area
                if x > 1e-6: ov.append((own[i][0], own[j][0], round(x, 6)))
    bg["own_own_overlap"] = ov
    bl = c["block"]
    bg["block_area"] = round(bl.area, 6); bg["sum_rows"] = round(sum(p.area for p in allp), 6)
    bg["union_symdiff_block"] = round(unary_union(allp).symmetric_difference(bl).area, 6) if allp else None
    bands = []
    for bnd in c["bands"]:
        side = None; best = None
        for (lb, sd), cp in crp.items():
            if lb == blk:
                x = bnd.symmetric_difference(cp).area
                if best is None or x < best: best, side = x, sd
        mat = [(k, p) for k, p in pools if p is not None and p.intersection(bnd).area > 0.5 * bnd.area]
        mp = mat[0][1] if len(mat) == 1 else None
        rng = crp.get((blk, side))
        bands.append(dict(side=side, band_area=round(bnd.area, 6),
                          mat_piece=[k for k, _ in mat], mat_area=(None if mp is None else round(mp.area, 6)),
                          range_area=(None if rng is None else round(rng.area, 6)),
                          g1_symdiff_mat_range=(None if (mp is None or rng is None) else round(mp.symmetric_difference(rng).area, 6)),
                          g2_band_owner=[(k, round(p.intersection(bnd).area, 6)) for k, p in own if p is not None and p.intersection(bnd).area > 1e-6]))
    bg["bands"] = bands
    adj = [dict(k=r["暫編地號"], side=r["推進側別"], G=r["G(㎡)"], 序=r.get("驗_宗序"), B=r.get("驗_B藍影"),
                藍影=r.get("驗_B_藍影面積"), 正街=r.get("驗_B_臨正街"), 屁股=r.get("驗_B_臨屁股"),
                nv=(None if poly(r) is None else len(poly(r).exterior.coords) - 1))
           for r in R if r.get("驗_宗序") in ("第2宗", "街角第1宗")]
    bg["checked_lots"] = adj
    G["blocks"][blk] = bg
json.dump({"mode": MODE, "sb": SB, "err": err, "rows": rows, "gates": G}, open(OUT, "w"), ensure_ascii=False, default=str)
print(json.dumps({"mode": MODE, "sb": SB, "err": (err or "")[:120], "n_rows": len(rows), "dropped": dropped}, ensure_ascii=False, default=str))
for blk, bg in G["blocks"].items():
    flag = []
    if bg["own_invalid"]: flag.append("invalid")
    if bg["own_own_overlap"]: flag.append("own-ov")
    if bg["union_symdiff_block"] is not None and bg["union_symdiff_block"] > 1e-3: flag.append("union≠block")
    for b in bg["bands"]:
        if b["g1_symdiff_mat_range"] is None or b["g1_symdiff_mat_range"] > 0.005: flag.append("g1")
        if b["g2_band_owner"]: flag.append("g2")
    print(blk, "OK" if not flag else flag, "blk", bg["block_area"], "Σ", bg["sum_rows"], "∪Δ", bg["union_symdiff_block"],
          "bands", [(b["side"], b["band_area"], b["mat_piece"], b["mat_area"], b["range_area"], b["g1_symdiff_mat_range"], b["g2_band_owner"]) for b in bg["bands"]])
    for a in bg["checked_lots"]:
        print("   ", a)
````

#### 附件 A-5　新檔　`verify/probes/wg9309/drv.py`　sha256 `714cd40e7f7e960f92a8a542d4a3b764b5e1281c8acd59047ccb995701e0d232`

````python
# 發單側原型驅動器（scratch·不入倉）：一（態·情境）→ 逐宗列 + forced 資訊
import contextlib, io, os, sys, json
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3]); OUT = sys.argv[4]
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
spy = {"cbs": [], "slot": []}
_o_cbs = ns["_corner_buffer_S"]
def _cbs(*a, **k):
    r = _o_cbs(*a, **k); spy["cbs"].append({"label": k.get("_label"), "side": a[5] if len(a) > 5 else k.get("side"), "range": a[4] if len(a) > 4 else k.get("range_area"), "buf": r}); return r
ns["_corner_buffer_S"] = _cbs
_o_slot = ns["_select_pool_slot"]
def _slot(w, l, r, *a, **k):
    out = _o_slot(w, l, r, *a, **k)
    f = sys._getframe(1).f_locals
    spy["slot"].append({"blk": f.get("blk_label"), "widths": list(w), "bL": l.get("b"), "bR": r.get("b"), "k": out.get("k") if isinstance(out, dict) else None}); return out
ns["_select_pool_slot"] = _slot
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
err = None
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
    g_rows = sg["g_rows"]
except RuntimeError as e:
    err = str(e).split("\n")[0][:300]; g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
KEEP = None
rows = []
for r in g_rows:
    d = {}
    for k, v in r.items():
        if k == "cut_coords":
            try: d[k] = [[float(a), float(b)] for a, b in v] if v and not isinstance(v, str) else v
            except Exception: d[k] = str(v)
        else:
            try: json.dumps(v); d[k] = v
            except Exception: d[k] = str(v)
    rows.append(d)
json.dump({"mode": MODE, "sb": SB, "err": err, "forced": str(forced)[:2000], "off": str(_off)[:2000], "rows": rows, "cbs": spy["cbs"], "slot": spy["slot"], "log_tail": buf.getvalue()[-3000:]}, open(OUT, "w"), ensure_ascii=False, default=str)
print("OK", MODE, SB, "rows", len(rows), "err", err, "cbs", len(spy["cbs"]))
````

#### 附件 A-6　新檔　`verify/probes/wg9309/chk_band.py`　sha256 `48eebccbffe685ddc1e7990c5794ccf22190b45407d8eca9dc6de2a3dc0d465c`

````python
# 發單側原型檢核（scratch）：強制帶（改後雙線形）vs 規定範圍多邊形之對稱差；SIDELINE 至帶遠側線之垂距
import contextlib, io, os, sys, json
import numpy as np
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3])
sys.path.insert(0, os.path.join(REPO, "verify"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
rec = {"cbs": [], "crp": {}}
_o = ns["_corner_buffer_S"]
def _cbs(block_poly, d_hat, front_p1, allocation_dir, range_area, side, tol=0.01, _label='', far_line_dir=None):
    buf = (_o(block_poly, d_hat, front_p1, allocation_dir, range_area, side, tol=tol, _label=_label) if far_line_dir is None else _o(block_poly, d_hat, front_p1, allocation_dir, range_area, side, tol=tol, _label=_label, far_line_dir=far_line_dir))
    rec["cbs"].append(dict(bp=block_poly, d=np.asarray(d_hat,float), p1=np.asarray(front_p1,float), ad=np.asarray(allocation_dir,float), ra=float(range_area), side=side, lbl=_label, fd=None if far_line_dir is None else np.asarray(far_line_dir,float), buf=buf))
    return buf
ns["_corner_buffer_S"] = _cbs
_olg = ns["_lot_gate"]
def _lg(res, tp, ctx, *a, **k):
    try:
        cs = k.get("chain_side"); lb = k.get("_label")
        cp = (ctx.get("corner_range_polys") or {}).get(cs)
        if cp is not None: rec["crp"][(lb, cs)] = cp
    except Exception: pass
    return _olg(res, tp, ctx, *a, **k)
ns["_lot_gate"] = _lg
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
try:
    with contextlib.redirect_stdout(io.StringIO()):
        run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
except RuntimeError as e:
    pass
slbs = fake_st.session_state.get('f3_cad_side_lines_by_side', {})
for c in rec["cbs"]:
    dom = ns["_strip_s_range"](c["bp"], c["d"], c["p1"], c["ad"]); s_min, s_max = float(dom[0]), float(dom[1])
    lo = max(s_min, 0.0); buf = c["buf"]
    a, b = (lo, buf) if c["side"] == 'left' else (s_max - buf, s_max)
    bpt = c["p1"] + a * c["d"]
    if c["fd"] is None:
        g, ar = ns["_block_strip"](c["bp"], c["d"], bpt, b - a, allocation_dir=c["ad"])
    else:
        fl = c["fd"] / np.linalg.norm(c["fd"]); al = c["ad"] / np.linalg.norm(c["ad"])
        if c["side"] == 'left':
            g, ar = ns["_block_strip"](c["bp"], c["d"], bpt, b - a, allocation_dir=c["ad"], n_hat_far=np.array([-fl[1], fl[0]]))
        else:
            g, ar = ns["_block_strip"](c["bp"], c["d"], bpt, b - a, allocation_dir=fl, n_hat_far=np.array([-al[1], al[0]]))
    crp = rec["crp"].get((c["lbl"], c["side"]))
    sd = float(g.symmetric_difference(crp).area) if (g is not None and crp is not None) else None
    sl = (slbs.get(c["lbl"]) or {}).get(c["side"]) or {}
    p1s = np.asarray(sl["p1"], float)[:2]; p2s = np.asarray(sl["p2"], float)[:2]; v = (p2s - p1s) / np.linalg.norm(p2s - p1s); nrm = np.array([-v[1], v[0]])
    inner = c["p1"] + buf * c["d"] if c["side"] == 'left' else c["p1"] + (s_max - buf) * c["d"]
    perp = abs(float(np.dot(inner - p1s, nrm)))
    print(json.dumps(dict(mode=MODE, sb=SB, lbl=c["lbl"], side=c["side"], range_area=c["ra"], buf=buf, band_area=float(ar), range_poly_area=(None if crp is None else float(crp.area)), symdiff=sd, perp_SIDELINE_to_inner=perp, two_line=c["fd"] is not None), ensure_ascii=False))
````

#### 附件 A-7　新檔　`verify/probes/wg9309/cmp.py`　sha256 `5cf1f503c441a5a36819f61ced19e36e28c4f4bd6e998616d474a345b05c41a9`

````python
import json,sys
A,B=sys.argv[1],sys.argv[2]
def key(r): return (r["所屬街廓"],r["推進側別"],r["暫編地號"])
for n in ["A_0","A_35","B_0","B_35"]:
    a=json.load(open(f"{A}_{n}.json")); b=json.load(open(f"{B}_{n}.json"))
    ra={key(r):r for r in a["rows"]}; rb={key(r):r for r in b["rows"]}
    print(f"== {n}  rows {len(ra)}→{len(rb)}  cbs {[round(x['buf'],6) for x in a['cbs']]}→{[round(x['buf'],6) for x in b['cbs']]}  slot-b {[ (s['blk'],round(s['bL'],4)) for s in a['slot'] if s['bL']]}→{[ (s['blk'],round(s['bL'],4)) for s in b['slot'] if s['bL']]}  k {[s['k'] for s in a['slot']]}→{[s['k'] for s in b['slot']]}")
    only_a=sorted(set(ra)-set(rb)); only_b=sorted(set(rb)-set(ra))
    if only_a: print("   只在前:",only_a)
    if only_b: print("   只在後:",[(k, rb[k]["G(㎡)"]) for k in only_b])
    ch=0
    for k in sorted(set(ra)&set(rb)):
        x,y=ra[k],rb[k]
        d={f:(x[f],y[f]) for f in ["G(㎡)","S(m)","W(m)","Rw(%)","負擔比率","累積S(m)"] if str(x[f])!=str(y[f])}
        cc = x.get("cut_coords")!=y.get("cut_coords")
        if d or cc:
            ch+=1; print("   ",k,d, "幾何變" if cc else "")
    print(f"   變動宗數 {ch}／共同 {len(set(ra)&set(rb))}")
````

#### 附件 A-8　新檔　`verify/probes/wg9309/drv_p2b.py`　sha256 `b9d01966d71063a646ab357997be8664ee082b111f0a97da0318d9dc217a1673`

````python
# 發單側原型驅動器（scratch·不入倉）：一（態·情境）→ 逐宗列 + forced 資訊
import contextlib, io, os, sys, json
REPO = sys.argv[1]; MODE = sys.argv[2]; SB = float(sys.argv[3]); OUT = sys.argv[4]
sys.path.insert(0, os.path.join(REPO, "verify")); sys.path.insert(0, os.path.join(REPO, "verify", "probes"))
if MODE == "甲": os.environ.pop("WV_K6_STEP0", None)
else: os.environ["WV_K6_STEP0"] = "off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO, "app.py"))
spy = {"cbs": [], "slot": []}
_o_cbs = ns["_corner_buffer_S"]
def _cbs(*a, **k):
    r = _o_cbs(*a, **k); spy["cbs"].append({"label": k.get("_label"), "side": a[5] if len(a) > 5 else k.get("side"), "range": a[4] if len(a) > 4 else k.get("range_area"), "buf": r}); return r
ns["_corner_buffer_S"] = _cbs
_o_slot = ns["_select_pool_slot"]
def _slot(w, l, r, *a, **k):
    out = _o_slot(w, l, r, *a, **k)
    f = sys._getframe(1).f_locals
    spy["slot"].append({"blk": f.get("blk_label"), "widths": list(w), "bL": l.get("b"), "bR": r.get("b"), "k": out.get("k") if isinstance(out, dict) else None}); return out
ns["_select_pool_slot"] = _slot
_o_ps = ns["_pool_strips_for_block"]
spy["xover"] = []
def _ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    fb = list(forced_bands or [])
    bad = [round(sum(b.intersection(p).area for p in biz_polys if p is not None), 6) for b in fb]
    if any(x > 1e-6 for x in bad):
        spy["xover"].append({"blk": _label, "band_owner_overlap": bad})
        fb = [b for b, x in zip(fb, bad) if x <= 1e-6]      # 量測用：交叉之帶退回 P1 行為（loud 記錄）
    return _o_ps(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, forced_bands=fb)
ns["_pool_strips_for_block"] = _ps
snapshot = rv.load_snapshot()
cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
v6 = open(rv.V6DXF, "rb").read()
temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
_d, _s, _off, wins, forced = run_corner_pk(ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, SB, snapshot=snapshot)
err = None
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p, wins, forced, SB, eff_min_build_by_blk={})
    g_rows = sg["g_rows"]
except RuntimeError as e:
    err = str(e).split("\n")[0][:300]; g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
KEEP = None
rows = []
for r in g_rows:
    d = {}
    for k, v in r.items():
        if k == "cut_coords":
            try: d[k] = [[float(a), float(b)] for a, b in v] if v and not isinstance(v, str) else v
            except Exception: d[k] = str(v)
        else:
            try: json.dumps(v); d[k] = v
            except Exception: d[k] = str(v)
    rows.append(d)
json.dump({"mode": MODE, "sb": SB, "err": err, "forced": str(forced)[:2000], "off": str(_off)[:2000], "rows": rows, "cbs": spy["cbs"], "slot": spy["slot"], "xover": spy["xover"], "log_tail": buf.getvalue()[-3000:]}, open(OUT, "w"), ensure_ascii=False, default=str)
print("OK", MODE, SB, "rows", len(rows), "err", (err or "")[:60], "cbs", len(spy["cbs"]), "xover", spy["xover"][:2])
````

#### 附件 A-9　新檔　`verify/probes/wg9309/ovl2.py`　sha256 `5e0fc328cf52771ebd08ebb1edef556adf1db922ee93b5fe5b1bb60a352645a3`

````python
# 發單側原型檢核（scratch）：強制帶（雙線）與業主宗之重疊（逐宗）
import contextlib, io, os, sys, json
REPO=sys.argv[1]; MODE=sys.argv[2]; SB=float(sys.argv[3])
sys.path.insert(0, os.path.join(REPO,"verify"))
if MODE=="甲": os.environ.pop("WV_K6_STEP0",None)
else: os.environ["WV_K6_STEP0"]="off"
from app_harvest import harvest
import run_verification as rv
from selection_pipeline import run_corner_pk
from stepg_pipeline import run_step_g
ns, fake_st = harvest(os.path.join(REPO,"app.py"))
cap=[]
_o=ns["_pool_strips_for_block"]
def _p(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
    if forced_bands:
        cap.append((_label, [p for p in biz_polys], list(forced_bands), block_poly))
    return _o(block_poly, d_hat, corner_pt, allocation_dir, biz_polys, _label=_label, _depth=_depth, _verbose=_verbose, forced_bands=forced_bands)
ns["_pool_strips_for_block"]=_p
snapshot=rv.load_snapshot()
cb_by,cad=rv.build_pipeline(ns,fake_st,snapshot)
rv.build_ownership(ns,fake_st,rv.ANON_XLSX)
v6=open(rv.V6DXF,"rb").read()
temp_p,build_p,_=rv.build_build_parcels(ns,fake_st,v6,list(cb_by.values()),snapshot)
params=rv.build_param_table(ns,fake_st,cb_by,cad,snapshot,SB)
_d,_s,_off,wins,forced=run_corner_pk(ns,fake_st,list(cb_by.values()),cad,params,temp_p,build_p,SB,snapshot=snapshot)
try:
    with contextlib.redirect_stdout(io.StringIO()):
        run_step_g(ns,fake_st,list(cb_by.values()),cad,snapshot,params,build_p,wins,forced,SB,eff_min_build_by_blk={})
except RuntimeError as e:
    print("RuntimeError:", str(e)[:160])
seen=set()
for lbl,biz,fb,bp in cap:
    key=(lbl, round(sum(p.area for p in biz),6))
    if key in seen: continue
    seen.add(key)
    import pickle; pickle.dump((lbl,biz,fb,bp),open(f"cap_{MODE}_{SB}_{lbl}.pkl","wb"))
    for k,b in enumerate(fb):
        ov=[(i, round(p.area,4), round(b.intersection(p).area,4)) for i,p in enumerate(biz) if b.intersection(p).area>1e-6]
        print(json.dumps(dict(mode=MODE,sb=SB,blk=lbl,band_area=round(b.area,4),n_biz=len(biz),overlaps=ov,sum_ov=round(sum(x[2] for x in ov),6)),ensure_ascii=False))
````

#### 附件 A-10　新檔　`verify/probes/wg9309/r2_geom.py`　sha256 `2aa10f9f5143c07402a3d8bc891e76467c1ba779349220210c9def80027c1f51`

````python
# 發單側原型檢核（scratch）：R2 左強制帶（P2·雙線）與 P1 業主宗之逐宗重疊；首宗之頂點數
# 用法：python3 r2_geom.py cap_乙_3.5_R2.pkl p1_B_35.json
import pickle, json, sys
from shapely.geometry import Polygon
lbl, biz, fb, bp = pickle.load(open(sys.argv[1], 'rb'))
band = fb[0]
d = json.load(open(sys.argv[2]))
own = {r['暫編地號']: Polygon(r['cut_coords']) for r in d['rows'] if r['所屬街廓'] == lbl and r['推進側別'] == 'left'}
for k, p in own.items():
    print(k, round(p.area, 4), 'band∩', round(p.intersection(band).area, 4))
for k, p in own.items():
    print(k, '頂點數', len(p.exterior.coords) - 1)
print('band', round(band.area, 4))
````

#### 附件 B　倉外　`W-G.9-309_P4.diff`　sha256 `5356801be3c09ccfd708ed3f85d3fba8195e1d871ce34cf793b1a660444b8091`

````diff
diff --git a/app.py b/app.py
index 8466f74..5ceddfc 100644
--- a/app.py
+++ b/app.py
@@ -9329,8 +9329,36 @@ def k917_note_drop(blk_label, chain_side, pid, res, tp=None):
     })
 
 
+def _corner_band_geom(block_poly, d_hat, front_p1, allocation_dir, buf, side,
+                      far_line_dir=None, s_lo=None, s_max=None):
+    """強制帶之幾何（`_corner_buffer_S` 之 bisect 所量者·單一真相源）。回傳 `(geom, area)`。
+    左＝s∈[max(s_min,0), buf]／右＝s∈[s_max−buf, s_max]；`far_line_dir` 有值 ⇒ 帶之裡側界 ∥ 該向之切線（雙線）。"""
+    import numpy as np
+    _d = np.asarray(d_hat, dtype=float)
+    if s_lo is None or s_max is None:
+        _dom = _strip_s_range(block_poly, d_hat, front_p1, allocation_dir)
+        if _dom is None:
+            return None, 0.0
+        s_lo, s_max = max(float(_dom[0]), 0.0), float(_dom[1])
+    a, b = (s_lo, float(buf)) if side == 'left' else (s_max - float(buf), s_max)
+    w = b - a
+    if w <= 0:
+        return None, 0.0
+    bp = np.asarray(front_p1, dtype=float) + a * _d
+    if far_line_dir is None:
+        return _block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)
+    _ad = np.asarray(allocation_dir, dtype=float)
+    _fl = np.asarray(far_line_dir, dtype=float); _fl = _fl / float(np.linalg.norm(_fl))
+    _al = _ad / float(np.linalg.norm(_ad))
+    if side == 'left':
+        return _block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir,
+                            n_hat_far=np.array([-_fl[1], _fl[0]]))
+    return _block_strip(block_poly, d_hat, bp, w, allocation_dir=_fl,
+                        n_hat_far=np.array([-_al[1], _al[0]]))
+
+
 def _corner_buffer_S(block_poly, d_hat, front_p1, allocation_dir, range_area, side,
-                     tol=0.01, _label=''):
+                     tol=0.01, _label='', far_line_dir=None):
     """
     §3 街角 forced band（plan v3 §3·補丁九）：**bisect 解 `buf` 使「真實池帶面積 == range_area」**
     （|Δ| ≤ tol）。**全精度回傳**（N0-18a·不 round）。取代舊矩形近似 `range_area ÷ avg_depth`
@@ -9400,13 +9428,9 @@ def _corner_buffer_S(block_poly, d_hat, front_p1, allocation_dir, range_area, si
               f"（p1 楔形 {abs(s_min):.4f}m 段待 §4 N0-20 切出·補丁九 裁 2 中間態·非靜默吞差）")
 
     def _band_area(buf):
-        """真實池帶面積（∥ALLOC 斜交·與 `_pool_strips_for_block` 逐字同源之 s 區間→實帶式）。"""
-        a, b = (_lo, float(buf)) if side == 'left' else (s_max - float(buf), s_max)
-        w = b - a
-        if w <= 0:
-            return 0.0
-        bp = np.asarray(front_p1, dtype=float) + a * _d
-        _g, _ar = _block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)
+        """真實池帶面積（委派 `_corner_band_geom`·與池片之強制帶同源）。"""
+        _g, _ar = _corner_band_geom(block_poly, d_hat, front_p1, allocation_dir, buf, side,
+                                    far_line_dir=far_line_dir, s_lo=_lo, s_max=s_max)
         return float(_ar or 0.0)
 
     # bisect 區間：左＝buf 為絕對 s 上界 [lo, s_max]／右＝buf 為寬 [0, s_max−s_min]
@@ -9436,7 +9460,7 @@ def _corner_buffer_S(block_poly, d_hat, front_p1, allocation_dir, range_area, si
 
 
 def _pool_strips_for_block(block_poly, d_hat, corner_pt, allocation_dir,
-                           biz_polys, _label='', _depth=None, _verbose=True):
+                           biz_polys, _label='', _depth=None, _verbose=True, forced_bands=None):
     """
     §N3-0 T2（主修法）：**池片改用與業主宗完全相同之 `_block_strip` 機制、以同一組切線直接切出。**
 
@@ -9490,6 +9514,12 @@ def _pool_strips_for_block(block_poly, d_hat, corner_pt, allocation_dir,
         r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
         if r is not None:
             biz_iv.append(r)
+    # 🆕 P2：強制帶（雙線）為**固定片**——其 s 範圍視同已占（⛔ 以 ∥ALLOC 單線重切）
+    _fb = [p for p in (forced_bands or []) if p is not None and not p.is_empty]
+    for p in _fb:
+        r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
+        if r is not None:
+            biz_iv.append(r)
     biz_iv.sort()
 
     # ── 3. 業主宗區間之聯集（第四源致相鄰宗 s 區間可重疊 ≤0.005；union 吸收之）
@@ -9531,6 +9561,10 @@ def _pool_strips_for_block(block_poly, d_hat, corner_pt, allocation_dir,
             continue
         pieces.append(g)
         kept_iv.append((a, b))
+    for p in _fb:                                   # 🆕 P2：強制帶原形入池
+        pieces.append(p)
+        _r = _strip_s_range(p, d_hat, corner_pt, allocation_dir)
+        kept_iv.append(_r if _r is not None else (s_min, s_max))
 
     # ── 5b. 🆕 **D-2b-24：幾何餘（`K-9-5-7` 配餘）** ──────────────────────────────
     #   正典逐字（`grep -n "^### 🔒 K-9-5-7" docs/rulings/K-6_街角地分配程序與可分配判準.md`）：
@@ -12468,6 +12502,7 @@ def _lot_gate(res, tp, blk_ctx, is_corner_first=False,
 
     - **街角第 1 宗**：`A` ⇒ `不適用`（`K-9-12-e`／`K-9-5-15 二`）；`B` ⇒ `不適用`。
     - **`B` 之適用** ＝ **有 sideline 之鏈之第 2 宗**（KL 語序·碼側 index `1`）；
+      🆕 `W-G.9-309`：**強制側**之碼側 index 為 `0`（強制抵費地⛔ 在推進鏈內·`K-9-31 ④`／`K-9-32 ②④`·含遞補上來者）；
       末端塊之鏈**無 sideline ⇒ 無藍影之題**（`K-9-23 三` 漏承加註·`v3` ⑪ 逐字）⇒ `不適用`。
     - **`e ＝ 0`** ＝ 該街廓無「最小建築面積」規定 ⇒ `C` `不適用`（`v3` ⑨ 逐字「僅幾何驗，無面積驗」）。
     - 所需輸入**取不到** ⇒ `無從判定`（＝單所稱之「不可判」）並**具名缺者**；
@@ -21915,6 +21950,13 @@ def main():
                         )
                         _left_buffer_S = 0.0
                         _right_buffer_S = 0.0
+                        # 🆕 `W-G.9-309`（`GB-170` (i)·app 側鏡射 stepg）：強制側之遠側界 ∥SIDELINE（`K-9-32 ①`）
+                        _sl_blk_fo = (st.session_state.get(
+                            'f3_cad_side_lines_by_side', {}) or {}).get(blk_label, {}) or {}
+                        _fd_fo_left = (_first_corner_alloc_dir((_sl_blk_fo.get('left') or {}).get('mid'))
+                                       if _fo_left else None)
+                        _fd_fo_right = (_first_corner_alloc_dir((_sl_blk_fo.get('right') or {}).get('mid'))
+                                        if _fo_right else None)
                         if _row_for_buffer and avg_depth_default > 0:
                             # 🆕 §3（plan v3 §3·補丁九）：廢矩形近似 `range ÷ avg_depth`，改 `_corner_buffer_S`
                             #   幾何 bisect（**真實斜交池帶面積 == range**）·side 參數化（#25）。
@@ -21925,7 +21967,8 @@ def main():
                                     if _l_min is not None and _l_min != float('inf'):
                                         _left_buffer_S = _corner_buffer_S(
                                             blk_poly, d_hat, corner_pt, allocation_dir_block,
-                                            float(_l_min), 'left', _label=blk_label)
+                                            float(_l_min), 'left', _label=blk_label,
+                                            far_line_dir=_fd_fo_left)
                                 except (TypeError, ValueError) as _e_cb:
                                     # KL WATCH 2026-07-20（no-silent-fallback）：range 型別壞→靜默 0 改 loud（上游 is not None/!=inf 已擋·罕觸）
                                     print(f"🔴 街廓 {blk_label} 左街角 range={_l_min!r} 型別異常（{_e_cb}）·buffer 退 0·入報告")
@@ -21936,7 +21979,8 @@ def main():
                                     if _r_min is not None and _r_min != float('inf'):
                                         _right_buffer_S = _corner_buffer_S(
                                             blk_poly, d_hat, corner_pt, allocation_dir_block,
-                                            float(_r_min), 'right', _label=blk_label)
+                                            float(_r_min), 'right', _label=blk_label,
+                                            far_line_dir=_fd_fo_right)
                                 except (TypeError, ValueError) as _e_cb:
                                     # KL WATCH 2026-07-20（no-silent-fallback）：range 型別壞→靜默 0 改 loud（上游 is not None/!=inf 已擋·罕觸）
                                     print(f"🔴 街廓 {blk_label} 右街角 range={_r_min!r} 型別異常（{_e_cb}）·buffer 退 0·入報告")
@@ -22147,8 +22191,8 @@ def main():
                             #   值 ＝ **前一宗**之 `res['_alloc_dir_used']`（＝其遠側界方向源）；
                             #   首宗 None ⇒ 單線·逐位不變。⛔ **無條件 thread**（不看 `_has_*_corner`）
                             #   ——界面鏈之存在與該側有無街角無關；有無街角只影響「前一宗用了哪個方向」。
-                            _near_dir_left = None
-                            _near_dir_right = None
+                            _near_dir_left = (_fd_fo_left if _fo_left else None)     # 🆕 `W-G.9-309`（`GB-170` (ii)·`K-9-32 ②`）
+                            _near_dir_right = (_fd_fo_right if _fo_right else None)
                             first_corner_used_left = False
                             _lg_idx_left = 0          # 🆕 `W-G.9-246′`：本鏈之宗序（碼側·自 0）
                             left_results = []
@@ -22197,7 +22241,7 @@ def main():
                                 res['_lg_cols'] = _lot_gate(
                                     res, tp, _lg_blk_ctx,
                                     is_corner_first=bool(is_first_corner_l),
-                                    is_second_after_corner=(_lg_idx_left == 1),
+                                    is_second_after_corner=((_lg_idx_left == (0 if _fo_left else 1)) and not bool(is_first_corner_l)),   # 🆕 P3：`K-9-31 ④`／`K-9-32 ②④`（app 側鏡射）
                                     chain_side='left', _label=blk_label)
                                 # 🆕 `W-G.9-269` `c1` **站 1／4（app 左鏈）**：閘一之消費 ＋ `K-9-17` 遞補。
                                 #   🔒 `c3`：**無條件執行**（旗標已移除）。
@@ -22336,7 +22380,7 @@ def main():
                                 res['_lg_cols'] = _lot_gate(
                                     res, tp, _lg_blk_ctx,
                                     is_corner_first=bool(is_first_corner_r),
-                                    is_second_after_corner=(_lg_idx_right == 1),
+                                    is_second_after_corner=((_lg_idx_right == (0 if _fo_right else 1)) and not bool(is_first_corner_r)),   # 🆕 P3：`K-9-31 ④`／`K-9-32 ②④`（app 側鏡射）
                                     chain_side='right', _label=blk_label)
                                 # 🆕 `W-G.9-269` `c1` **站 2／4（app 右鏈）**：閘一之消費 ＋ `K-9-17` 遞補。
                                 #   🔒 `c3`：**無條件執行**（旗標已移除）。
@@ -22575,9 +22619,19 @@ def main():
                                 #   單一真相源＝`_pool_strips_for_block`；**與 stepg_pipeline 逐字同構**
                                 #   （N0-16 同源同碼·G.3 三重確立之基礎），四處共用根絕抄寫漂移（#20）。
                                 #   回傳序＝面積遞減（逐字沿用舊慣例）→ g_rows 抵費地序號不因本波改（plan §11）。
+                                _fb_p2 = []                    # 🆕 `W-G.9-309`（`GB-170` (iii)·app 側鏡射 stepg）
+                                for _sd, _bS, _fd in (('left', _left_buffer_S, _fd_fo_left),
+                                                      ('right', _right_buffer_S, _fd_fo_right)):
+                                    if _fd is not None and float(_bS or 0.0) > 0.0:
+                                        _gb, _ = _corner_band_geom(blk_poly, d_hat, corner_pt,
+                                                                   allocation_dir_block, _bS, _sd,
+                                                                   far_line_dir=_fd)
+                                        if _gb is not None and not _gb.is_empty:
+                                            _fb_p2.append(_gb)
                                 offset_geoms = _pool_strips_for_block(
                                     blk_poly, d_hat, corner_pt, allocation_dir_block,
-                                    allocated_polys, _label=blk_label, _depth=avg_depth_default)
+                                    allocated_polys, _label=blk_label, _depth=avg_depth_default,
+                                    forced_bands=_fb_p2)
 
                                 _pool_total_blk = float(sum(_g.area for _g in offset_geoms))  # 🆕 W-D.2 ledger
 
diff --git a/verify/stepg_pipeline.py b/verify/stepg_pipeline.py
index 866dd3c..e4bd912 100644
--- a/verify/stepg_pipeline.py
+++ b/verify/stepg_pipeline.py
@@ -651,6 +651,11 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
         _row_for_buffer = rows_by_lbl.get(blk_label)
         _left_buffer_S = 0.0
         _right_buffer_S = 0.0
+        _sl_blk_fo = (ss.get('f3_cad_side_lines_by_side', {}) or {}).get(blk_label, {}) or {}
+        _fd_fo_left = (ns['_first_corner_alloc_dir']((_sl_blk_fo.get('left') or {}).get('mid'))
+                       if _fo_left else None)
+        _fd_fo_right = (ns['_first_corner_alloc_dir']((_sl_blk_fo.get('right') or {}).get('mid'))
+                        if _fo_right else None)
         if _row_for_buffer and avg_depth_default > 0:
             # 🆕 §3（plan v3 §3·補丁九）：廢矩形近似 `range ÷ avg_depth` → `_corner_buffer_S`
             #   幾何 bisect（真實斜交池帶面積 == range）·side 參數化（#25）·byte 級對映 app（N0-16）。
@@ -660,7 +665,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     if _l_min is not None and _l_min != float('inf'):
                         _left_buffer_S = _corner_buffer_S(
                             blk_poly, d_hat, corner_pt, allocation_dir_block,
-                            float(_l_min), 'left', _label=blk_label)
+                            float(_l_min), 'left', _label=blk_label,
+                            far_line_dir=_fd_fo_left)
                 except (TypeError, ValueError) as _e_cb:
                     # KL WATCH 2026-07-20（no-silent-fallback）：range 型別壞→靜默 0 改 loud（上游 is not None/!=inf 已擋·罕觸）
                     print(f"🔴 街廓 {blk_label} 左街角 range={_l_min!r} 型別異常（{_e_cb}）·buffer 退 0·入報告")
@@ -671,7 +677,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                     if _r_min is not None and _r_min != float('inf'):
                         _right_buffer_S = _corner_buffer_S(
                             blk_poly, d_hat, corner_pt, allocation_dir_block,
-                            float(_r_min), 'right', _label=blk_label)
+                            float(_r_min), 'right', _label=blk_label,
+                            far_line_dir=_fd_fo_right)
                 except (TypeError, ValueError) as _e_cb:
                     # KL WATCH 2026-07-20（no-silent-fallback）：range 型別壞→靜默 0 改 loud（上游 is not None/!=inf 已擋·罕觸）
                     print(f"🔴 街廓 {blk_label} 右街角 range={_r_min!r} 型別異常（{_e_cb}）·buffer 退 0·入報告")
@@ -790,8 +797,8 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
             #   值 ＝ **前一宗**之 `res['_alloc_dir_used']`（＝其遠側界方向源）；
             #   首宗 None ⇒ 單線·逐位不變。⛔ **無條件 thread**（不看 `_has_*_corner`）。
             #   ⚠️ app 側鏡射：`grep -n "界面單線鏈" app.py`（#20 四處同改之同源要求）。
-            _near_dir_left = None
-            _near_dir_right = None
+            _near_dir_left = (_fd_fo_left if _fo_left else None)
+            _near_dir_right = (_fd_fo_right if _fo_right else None)
             first_corner_used_left = False
             _lg_idx_left = 0          # 🆕 `W-G.9-246′`：本鏈之宗序（碼側·自 0）
             left_results = []
@@ -836,7 +843,7 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                 res['_lg_cols'] = ns['_lot_gate'](
                     res, tp, _lg_blk_ctx,
                     is_corner_first=bool(is_first_corner_l),
-                    is_second_after_corner=(_lg_idx_left == 1),
+                    is_second_after_corner=((_lg_idx_left == (0 if _fo_left else 1)) and not bool(is_first_corner_l)),   # 🆕 P3：`K-9-31 ④`／`K-9-32 ②④`——強制側之受檢宗 ＝ 緊鄰強制抵費地之宗（碼側 index 0·含遞補上來者）
                     chain_side='left', _label=blk_label)
                 # 🆕 `W-G.9-269` `c1` **站 3／4（harness 左鏈）**：閘一之消費 ＋ `K-9-17` 遞補。
                 #   🔒 `c3`：**無條件執行**（旗標已移除）。
@@ -957,7 +964,7 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                 res['_lg_cols'] = ns['_lot_gate'](
                     res, tp, _lg_blk_ctx,
                     is_corner_first=bool(is_first_corner_r),
-                    is_second_after_corner=(_lg_idx_right == 1),
+                    is_second_after_corner=((_lg_idx_right == (0 if _fo_right else 1)) and not bool(is_first_corner_r)),   # 🆕 P3：`K-9-31 ④`／`K-9-32 ②④`——強制側之受檢宗 ＝ 緊鄰強制抵費地之宗（碼側 index 0·含遞補上來者）
                     chain_side='right', _label=blk_label)
                 # 🆕 `W-G.9-269` `c1` **站 4／4（harness 右鏈）**：閘一之消費 ＋ `K-9-17` 遞補。
                 #   🔒 `c3`：**無條件執行**（旗標已移除）。
@@ -1172,9 +1179,19 @@ def _run_step_g_impl(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
                 #   單一真相源＝app 之 `_pool_strips_for_block`（ns harvest·同 `_block_strip` 先例）
                 #   → stepg／app／wf_f1／wf_f4 四處同源，根絕抄寫複本各自漂移（#20 根因）。
                 #   回傳序＝面積遞減（逐字沿用舊慣例）→ g_rows 抵費地序號不因本波改（plan §11）。
+                _fb_p2 = []
+                for _sd, _bS, _fd in (('left', _left_buffer_S, _fd_fo_left),
+                                      ('right', _right_buffer_S, _fd_fo_right)):
+                    if _fd is not None and float(_bS or 0.0) > 0.0:
+                        _gb, _ = ns['_corner_band_geom'](blk_poly, d_hat, corner_pt,
+                                                         allocation_dir_block, _bS, _sd,
+                                                         far_line_dir=_fd)
+                        if _gb is not None and not _gb.is_empty:
+                            _fb_p2.append(_gb)
                 offset_geoms = _pool_strips_for_block(
                     blk_poly, d_hat, corner_pt, allocation_dir_block,
-                    allocated_polys, _label=blk_label, _depth=avg_depth_default)
+                    allocated_polys, _label=blk_label, _depth=avg_depth_default,
+                    forced_bands=_fb_p2)
                 _pool_total_blk = float(sum(_g.area for _g in offset_geoms))
                 _min_block = min(50.0, blk_area * 0.05)
                 for _i, _g in enumerate(offset_geoms):
````

#### 附件 B-1　倉外　`W-G.9-309_B1_土地影響.md`　sha256 `264a41347c171a2f1f2e63f8ab77b78df7da1f0f00533a2db0aaf2a479e4b6e0`

````md
## 土地影響（變動街廓·基座 → 受驗）
- `A_0` R4/left/628(1)+｜G 2017.54 → 2016.04｜幾何 2017.54 → 2016.03｜負擔比率 0.3668 → 0.3673
- `A_0` R4/抵費地/R4-抵費地-1｜G 0.0 → 0.0｜幾何 1022.05 → 1049.67｜負擔比率 0.0 → 0.0
- `A_0` R4/抵費地/R4-抵費地-2｜G 0.0 → 0.0｜幾何 116.08 → 116.08｜負擔比率 0.0 → 0.0
- `A_0` R4/抵費地/R4-抵費地-3｜G 0.0 → 0.0｜幾何 26.11 → 26.09｜負擔比率 0.0 → 0.0
- `A_0` R4/抵費地/R4-抵費地-4｜G 0.0 → —｜幾何 26.09 → —｜負擔比率 0.0 → —
- `A_35` R2/left/628-27(1)｜G 29.61 → 29.61｜幾何 29.62 → 29.61｜負擔比率 0.423 → 0.423
- `A_35` R2/left/628-30(2)｜G 89.97 → 89.97｜幾何 89.97 → 89.97｜負擔比率 0.4014 → 0.4014
- `A_35` R2/left/628-31(2)｜G 391.66 → 391.66｜幾何 391.67 → 391.65｜負擔比率 0.4014 → 0.4014
- `A_35` R2/left/628-39(1)｜G 236.54 → 236.54｜幾何 236.54 → 236.54｜負擔比率 0.4014 → 0.4014
- `A_35` R2/left/628-40(1)+｜G 299.51 → 299.07｜幾何 299.5 → 299.06｜負擔比率 0.4172 → 0.4181
- `A_35` R2/left/628-41(1)｜G 183.23 → 176.6｜幾何 183.22 → 176.59｜負擔比率 0.4262 → 0.4469
- `A_35` R2/left/628-42(1)｜G 4.77 → —｜幾何 4.77 → —｜負擔比率 0.4281 → —
- `A_35` R2/right/628-32(2)｜G 437.02 → 437.02｜幾何 437.02 → 437.02｜負擔比率 0.4016 → 0.4016
- `A_35` R2/right/628-34(1)｜G 432.11 → 432.11｜幾何 432.11 → 432.1｜負擔比率 0.4017 → 0.4017
- `A_35` R2/right/628-35(1)｜G 58.95 → 58.95｜幾何 58.95 → 58.94｜負擔比率 0.4018 → 0.4018
- `A_35` R2/right/628-49(1)｜G 65.45 → 65.45｜幾何 65.45 → 65.44｜負擔比率 0.4017 → 0.4017
- `A_35` R2/right/628-50(1)｜G 147.18 → 147.18｜幾何 147.18 → 147.18｜負擔比率 0.4017 → 0.4017
- `A_35` R2/right/628-51(1)｜G 146.59 → 146.59｜幾何 146.59 → 146.59｜負擔比率 0.4017 → 0.4017
- `A_35` R2/right/628-52(1)｜G 71.6 → 71.6｜幾何 71.59 → 71.6｜負擔比率 0.4016 → 0.4016
- `A_35` R2/抵費地/R2-抵費地-1｜G 0.0 → 0.0｜幾何 1466.26 → 1478.12｜負擔比率 0.0 → 0.0
- `A_35` R2/抵費地/R2-抵費地-2｜G 0.0 → 0.0｜幾何 308.17 → 308.17｜負擔比率 0.0 → 0.0
- `A_35` R4/left/628(1)+｜G 2023.33 → 2022.05｜幾何 2023.34 → 2022.04｜負擔比率 0.365 → 0.3654
- `A_35` R4/抵費地/R4-抵費地-1｜G 0.0 → 0.0｜幾何 906.32 → 933.73｜負擔比率 0.0 → 0.0
- `A_35` R4/抵費地/R4-抵費地-2｜G 0.0 → 0.0｜幾何 226.01 → 226.01｜負擔比率 0.0 → 0.0
- `A_35` R4/抵費地/R4-抵費地-3｜G 0.0 → 0.0｜幾何 26.11 → 26.08｜負擔比率 0.0 → 0.0
- `A_35` R4/抵費地/R4-抵費地-4｜G 0.0 → —｜幾何 26.08 → —｜負擔比率 0.0 → —
- `B_35` R2/left/628-27(1)｜G 29.61 → 29.61｜幾何 29.62 → 29.61｜負擔比率 0.423 → 0.423
- `B_35` R2/left/628-30(2)｜G 89.97 → 89.97｜幾何 89.97 → 89.97｜負擔比率 0.4014 → 0.4014
- `B_35` R2/left/628-31(2)｜G 391.66 → 391.66｜幾何 391.67 → 391.65｜負擔比率 0.4014 → 0.4014
- `B_35` R2/left/628-39(1)｜G 236.54 → 236.54｜幾何 236.54 → 236.54｜負擔比率 0.4014 → 0.4014
- `B_35` R2/left/628-40(1)｜G 299.24 → 298.8｜幾何 299.24 → 298.8｜負擔比率 0.4172 → 0.4181
- `B_35` R2/left/628-41(1)｜G 183.23 → 176.6｜幾何 183.22 → 176.59｜負擔比率 0.4262 → 0.4469
- `B_35` R2/left/628-42(1)｜G 4.77 → —｜幾何 4.77 → —｜負擔比率 0.4281 → —
- `B_35` R2/left/628-43(1)｜G 0.27 → 0.27｜幾何 0.27 → 0.27｜負擔比率 0.4 → 0.4
- `B_35` R2/right/628-32(2)｜G 437.02 → 437.02｜幾何 437.02 → 437.02｜負擔比率 0.4016 → 0.4016
- `B_35` R2/right/628-34(1)｜G 432.11 → 432.11｜幾何 432.11 → 432.1｜負擔比率 0.4017 → 0.4017
- `B_35` R2/right/628-35(1)｜G 58.95 → 58.95｜幾何 58.95 → 58.94｜負擔比率 0.4018 → 0.4018
- `B_35` R2/right/628-49(1)｜G 65.45 → 65.45｜幾何 65.45 → 65.44｜負擔比率 0.4017 → 0.4017
- `B_35` R2/right/628-50(1)｜G 147.18 → 147.18｜幾何 147.18 → 147.18｜負擔比率 0.4017 → 0.4017
- `B_35` R2/right/628-51(1)｜G 146.59 → 146.59｜幾何 146.59 → 146.59｜負擔比率 0.4017 → 0.4017
- `B_35` R2/right/628-52(1)｜G 71.6 → 71.6｜幾何 71.59 → 71.6｜負擔比率 0.4016 → 0.4016
- `B_35` R2/抵費地/R2-抵費地-1｜G 0.0 → 0.0｜幾何 1466.26 → 1478.11｜負擔比率 0.0 → 0.0
- `B_35` R2/抵費地/R2-抵費地-2｜G 0.0 → 0.0｜幾何 308.17 → 308.17｜負擔比率 0.0 → 0.0
````

#### 附件 C-1　末端追加　`docs/reports/W-G.4_泛用阻塞項登記表.md`　sha256 `33cfde2ac43530c1d7aaf3c8ead42db5cba1da3a61633afc82fd76cda5a7f76f`

````md

## 🔧 `GB-170` 之修批（`W-G.9-309`）／KL 第二次放行之登記／`GB-171` 修屬之更正／`GB-172`・`GB-173` 之立（`W-G.9-309`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `2f46579c6c9c91d9f1b88431a7e6ae9d998ce311`（本批開工態）。

**(1) KL 之放行（逐字·`2026-09-22`·⛔ 增刪一字、⛔ 擴其射程）**
> 發單側（窗二十一）呈 KL 之【要你判斷】欄為單一是非：「是否放行：將上述兩項修改寫入測試版本並逐宗核對，仍不併入正式版本（併入時另行請您放行）？（是／否）」。所稱「兩項」＝ 同呈文【要改成】所載：① 強制抵費地實際分出來的土地，形狀一併照 9/15 之界線切出；② 依 9/17 裁二，緊鄰強制抵費地的那一宗受藍影檢查，不合格者不配地、面積入調配池，由下一宗遞補到緊鄰位置並同樣受檢。
> **KL 逐字所答 ＝「是，放行，出 `W-G.9-309`（重量批）」。**
> 🩸 該呈文之用語有誤（`自誤 475`）：稱強制抵費地之「上緣」者，其所指為**遠側界線**（與側街相對之一側）；稱「沿分配方向」者，其所指為**與宗地分配線平行**。本放行之受詞以該呈文所附之平面圖與【對土地的影響】之逐宗數為準，二者皆⛔ 繫於該二詞。

🛑 **射程（由發單側釘死·⛔ CC 擴之）**：
`(a)` 及於 `W-G.9-309` 附件 `B`（`app.py`／`verify/stepg_pipeline.py` 二檔之修·含本項之 `(i)(ii)(iii)` 及 `K-9-31 ④`／`K-9-32 ②④` 之受檢宗序）寫入凍存分支 `verify/W-G.9-299-gb170` 並 `push`；
`(b)` 及於該分支之逐宗核對（`verify/probes/probe_WG9309_gates.py` 十閘）及畫面核對之準備；
`(c)` 🔴 **⛔ 及於入主線**——主線之入倉須**另一次**放行（呈文逐字「仍不併入正式版本（併入時另行請您放行）」）；
`(d)` ⛔ 及於 `GB-167`／`168`／`169`／`171` 之任何修、`K-9-29` 之任何子項、`K-9-33 ⑤` 所增二條件（內接矩形、臨正街寬 `≥` 畸零地寬）之接線、`GB-172`／`GB-173` 之修。

**(2) 本項失效條件之現況**：`(1)` ⇒ 凍存分支上成就；`(2)` ⇒ 凍存分支上成就（逐宗之差見 `docs/reports/W-G.9-309R_執行報告.md`）；`(3)` ⇒ 主線未入 ⇒ **未成就**。🛑 **本項⛔ 解除、⛔ 收窄。**

**(3) `GB-171` 之修屬（更正上文 `GB-171` 末節「修法之施作與行為差之量測屬 `W-G.9-309`」之讀法）**：依發單側交接文十九 `§三（二）`（`2026-09-22`·發單側裁），選槽側 `W_1` 之軸與選槽估算之寬度（`GB-168` 之殘差）**⛔ 併入** `W-G.9-309`，另單辦之、帶數請放行；其正典依據 ＝ `K-9-43`。`W-G.9-309` 修後選槽側之強制起算點隨 `buf` 變（`3.5m`·`R2`：`6.9805 → 5.2888`·選槽結果⛔ 變），其量測軸仍為街廓軸 ⇒ 與 `K-9-43` 不合之處**屬該另單**。

---

### `GB-172` 🆕　**有側街之端，左側強制帶之下界夾於 `0`：側街外傾（`s_min < 0`）時強制帶 ≠ 規定範圍**

**受詞**：`app.py` `_corner_buffer_S` 之 `_lo = max(s_min, 0.0)` 及 `_corner_band_geom` 之左側下界（`W-G.9-309` 所立）；`p1` 楔形歸 `N0-20`（`docs/specs/W-G.4_S1_plan.md:71`／`:84`）。
**實測**（`verify/probes/wg9309/synth_attr.py`·態 ＝ `W-G.9-309` 之凍存分支·合成街廓正面 `60 m`·深 `30 m` × 側街傾角 `{−6°, −2.7°, 2.7°, 6°}` × 宗地分配線傾角 `{0°, 3°, −4°}` × 遠側線向之正負號·左右各 `24` 例）：右側 `24`／`24` 成立（對稱差 `≤ 1.2e-11` ㎡）；左側 `12` 成立／`12` ⛔ 成立，⛔ 成立者恰為 `s_min < 0` 之 `12` 例（對稱差 `20.49`〜`157.53` ㎡）。本案四格⛔ 觸發（`W-G.9-309` 閘一之最大對稱差 `0.0046` ㎡）。
**失效條件**：`(1)` 左側 `s_min < 0` 時楔形之處置經 KL 裁或依 `N0-20` 落地；`(2)` 合成例左側 `24`／`24` 成立；`(3)` 本案逐位不變之證。🛑 **⛔ 解除、⛔ 收窄、⛔ 提修法主張**——三者皆未成就。

### `GB-173` 🆕　**`verify/wf_f1.py`／`verify/wf_f4.py` 之強制帶與池片仍為單線（側界線登記表⛔ 在域）**

**受詞**（態 `2f46579`·字樣 `_corner_buffer_S"](`／`_pool_strips_for_block"](` 現查）：`verify/wf_f1.py` 強制帶 `1` 處（`:216`）與池片 `1` 處（`:388`）；`verify/wf_f4.py` 強制帶 `2` 處（`:1351`／`:1362`）與池片 `1` 處（`:956`）。
**由**：側界線登記表於該二路徑⛔ 在域（`W-G.9-308R §五-3`）⇒ 無從求遠側線向；`F.1`〜`F.4` 於 `run_all` 全跳過 ⇒ 結構上不可驗。`W-G.9-309` 所增之參數皆為選用、預設 `None` ⇒ 該二路徑之行為逐位不變。
**失效條件**：`(1)` 側界線登記表接入該二路徑；`(2)` 同改並經閘驗；`(3)` 其餘逐位不變之證。🛑 **⛔ 解除、⛔ 收窄。**
````

#### 附件 C-2　末端追加　`docs/reports/W-G.9波_claude.ai側自誤登記.md`　sha256 `406ec0010088569ec2a7670856e395f592e46dbf99bebcdcf6ce5f7bca552f7b`

````md

---

### 🩸 `自誤 469`　**判原型「界線已對」而未查其後首宗之有效性：`628-42(1)` 已成三角形、`628-41(1)` 已侵入規定範圍 `50.85` ㎡，皆在原型之落檔內可見**

**形**：發單側（窗十九）於交接文十九 `§四 甲-1` 以「強制帶 vs 規定範圍之對稱差 `≤ 0.005`」判原型 `P1` 之界線已對，並將 `P1` 下業主宗之變動標為「⛔ 期值」；而 `P1` 之落檔內 `R2` 左（`3.5m`）`628-42(1)` 已為頂點數 `3` 之三角形（`2.5466` ㎡），`628-41(1)` 與規定範圍重疊 `50.8488` ㎡（窗二十以 `ovl2.py`／`r2_geom.py` 量得；窗二十一復現·`verify/probes/wg9309/`）。
**後果之界**：未出單、未入倉；窗二十以原型 `P2` 觸發既存之 `②-池` 閘而揭。🟢
**根因**：閘綁中間量（界線）而未綁土地性質（物化形與全部鄰宗不重疊）——交接文十九 `§五-1` 自身所載教訓之同族；「⛔ 期值」之標記使該批⛔ 被檢。
**後果之框**：🟡 原型判讀之誤·零入倉。攔點 ＝ **發單側（窗二十）＋ 既存之硬停閘**。
**攔法**：既有 `恆常附款 r`；`W-G.9-309` 之閘二（規定範圍 ∩ 業主宗）即其施行。⛔ 新立款。

---

### 🩸 `自誤 470`　**一句之內二數分屬二量：`−1.51`（幾何面積）與 `−1.28`（`G`）並列為同一宗之變動**

**形**：交接文十九 `§四 甲-2`「`R4` `628(1)+` `−1.51`／`−1.28` ㎡」——`0m` 之 `−1.51` 係幾何面積（`2017.54 → 2016.03`），`3.5m` 之 `−1.28` 係 `G`（`2023.33 → 2022.05`）；同口徑 ＝ `G` `−1.50`／`−1.28`、幾何面積 `−1.51`／`−1.30`（窗二十更正；窗二十一以 `drv.py` 復現）。
**後果之界**：未入倉、未呈 KL。🟢
**根因**：`恆常附款 l`（期值同格載其框）之再犯——未載量名。
**後果之框**：🟡 交接文之數失真。攔點 ＝ **發單側（窗二十）**。
**攔法**：既有 `恆常附款 l`。⛔ 新立款。

---

### 🩸 `自誤 471`　**取號現查之命中數未載母體：「內文側 `45` 檔」僅於 `*.md` 成立，全倉為 `51`**

**形**：交接文十九 `§一` 項 `10`「`W-G.9-309` 保留（內文側 `45` 檔引）」；`git grep -l 'W-G\.9-309' -- '*.md'` ＝ `45`，全倉 ＝ `51`（另 `verify/out/` `5` 檔、`verify/probes/` `1` 檔）。
**後果之界**：未據之取捨。🟢
**根因**：`恆常附款 l`／`P-2`（計數須同段載其框）之再犯。
**後果之框**：🟡。攔點 ＝ **發單側（窗二十）**。
**攔法**：既有 `恆常附款 l`。⛔ 新立款。

---

### 🩸 `自誤 472`　**病灶已具名而未就其全部消費者查其判法：主 checkout 之更新令三度以依 stat 之 git 路徑為據**

**形**：`W-G.9-325` 交接註 `5`-`1` 已具名主 checkout 之 `app.py` 差純為行尾、index 所記 size 過期；發單側（窗十九）其後所出之主 checkout 更新令，前令一-`3`（`git diff`）、補令一（`restore`·`rc 0` 而零效果）、補令二（`merge --ff-only` 被拒）三度仍以依 stat 之路徑為判；至補令三 `read-tree HEAD` ＋ `update-index --refresh` 後內容框閘始全綠（`read-cache.c` `ie_modified` 之 size 捷徑讀法經該閘證實）。
**後果之界**：主 checkout 未受損（備份夾 `C:\Users\admin\Desktop\lrt_premerge_backup_20260921`·`135` 檔）；三令之誤皆為內容框後驗所擋。🟢
**根因**：病灶具名後，未就其**全部消費者**逐一查其判法。
**後果之框**：🟡 三令之無效操作·零資料損失。攔點 ＝ **閘（內容框後驗）與受單側**。
**攔法**：既有 `恆常附款 m`（全部消費者之列出）之類推施行。⛔ 新立款。

---

### 🩸 `自誤 473`　**以過時之治理文件狀態斷言碼面：稱 `K-9-17` 遞補迴圈「部分落地·觀測模式」「未開工」，而 `W-G.9-269 c3`（`17fd981`·`2026-09-12`）已令其無條件執行**

**形**：交接文二十 `§三-2` 判 `2` 引 `CLAUDE.md:1457`「部分落地·觀測模式」及 `:590`／`:1099`「未開工」，並稱 `_lot_gate` 為觀測模式；而態 `2f46579` 之 `app.py` `k917_should_drop`／`k917_note_drop`（`:9286`／`:9316`）已消費 `驗_B藍影`，不合格者不配地、由鏈之下一宗遞補（`app.py` 與 `verify/stepg_pipeline.py` 左右鏈·四處）；`CLAUDE.md` 全檔 `W-G.9-269` 之命中 ＝ `0`。
**後果之界**：交接文二十據之擬原型 `P3` 之射程為「藍影之執行與遞補」（重量）；窗二十一於開場序 `4` 讀碼而更正——`P3` 實為強制側受檢宗序一處之改（每鏈一判別式）。未出單、未入倉。🟢
**根因**：`恆常附款 p`（以倉內已有答案收窄或定射程前須讀畢）之同族——以治理文件代碼面；「已落地而治理文件未更新」與「已裁而未落地」同為誤診之源。
**後果之框**：🟡 射程之高估·零入倉。攔點 ＝ **發單側（窗二十一·開場序 `4`）**。
**攔法**：既有 `恆常附款 p`；`CLAUDE.md` 進度表之更正（`W-G.9-309` 工項五-`4`）。⛔ 新立款。

---

### 🩸 `自誤 474`　**所引行號未標其所繫之樹：`app.py:12487`／`:22234`／`:22373`、`verify/stepg_pipeline.py:846`／`:967` 係原型 `P2` 樹之行號**

**形**：交接文二十 `§三-2` 判 `2` 所引；基座（`2f46579`）之對應行號為 `app.py:12453`／`:22200`／`:22339`、`verify/stepg_pipeline.py:839`／`:960`（窗二十一實查）。
**後果之界**：未入倉；窗二十一以字樣重錨。🟢
**根因**：`恆常附款 w`（`blob`／`sha256` 錨須同格載其所繫之態）之類推——行號亦為繫態之錨。
**後果之框**：🟡。攔點 ＝ **發單側（窗二十一）**。
**攔法**：既有 `恆常附款 w`。⛔ 新立款。

---

### 🩸 `自誤 475`　**呈 KL 之文用語有誤：稱強制抵費地之「上緣」而實指遠側界線；稱其「沿分配方向」而實指與宗地分配線平行（`q②` 再犯）**

**形**：發單側（窗二十一）於 `2026-09-22` 呈 KL 之放行請求，【現況】作「其上緣沿分配方向斜出」、【要改成】作「即上緣與側街平行」，平面圖標註同。所指之線係強制抵費地與其後一宗之交界（**遠側界線**·平面圖上與側街相對之一側）；現況該線**與宗地分配線平行**，而依 `K-9-43`（五）（`docs/rulings/K-6_街角地分配程序與可分配判準.md` 檔末），「分配方向」＝ 垂直於宗地分配線之方向 ⇒「沿分配方向」與所指相反。
**後果之界**：KL 已答「是，放行」；該答之受詞以平面圖（線形依實際座標繪製）與【對土地的影響】之逐宗數為準，二者皆⛔ 繫於該二詞 ⇒ 放行之受詞⛔ 變；已於 `W-G.9-309` 之 `GB` 簿登記與交付時一併告知 KL。🟡
**根因**：`恆常附款 q②`（程式之方向名須先以地政用語定義）之再犯；以方位字（上／下）指稱界線，而平面圖之擺置係發單側所定、⛔ 為地籍之定義。
**後果之框**：🟡 呈文用語之誤·放行受詞未變。攔點 ＝ **發單側（窗二十一·擬 `W-G.9-309` 時自捕）**。
**攔法**：既有 `恆常附款 q②`；另：呈 KL 之文稱界線者，一律以「近側界線／遠側界線／臨正面道路／臨側街／臨後側」稱之，⛔ 以圖之方位字稱之（併入 `q②` 之施行·⛔ 新立款）。
````

#### 附件 C-3　末端追加　`docs/rulings/K-6_街角地分配程序與可分配判準.md`　sha256 `d12b394a6e6b6c159e2b048dfdae7ec1936f1f29577d525cd9b4fd59b771fb20`

````md

### 🔧 `K-9-31 ④`／`K-9-32 ②③④` 之落地狀態（`W-G.9-309`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 凍存分支 `verify/W-G.9-299-gb170`（主線 `wip/s1-endpart` **⛔ 入**·KL `2026-09-22` 放行之射程 `(c)`）。
① `K-9-32 ①②`（強制抵費地之遠側地界線與側街平行；其後 `1` 宗之裡側界線 ＝ 該線）及強制抵費地之物化形 ≡ 規定範圍 ⇒ **凍存分支上落地**（`GB-170` 之 `(i)(ii)(iii)`）。
② `K-9-31 ④`／`K-9-32 ④`（藍影受檢宗 ＝ 緊鄰強制抵費地之宗·含遞補上來者）⇒ **凍存分支上落地**：強制側之受檢宗 ＝ 推進鏈之碼側 index `0`（強制抵費地⛔ 在推進鏈內）；鏈首為街角第 `1` 宗者⛔ 受檢（`_lot_gate` 之既有射程·`K-9-32 ④` 所載之形）。
③ `K-9-32 ③` 之遞補 ＝ 既有 `W-G.9-269 c3` 之 `k917_should_drop`／`k917_note_drop`（主線已落地·無條件執行）；其受詞僅 `K-9-23` 閘一（藍影）——`K-9-33 ⑤` 所增之內接矩形與「臨正街寬 `≥` 畸零地寬」**⬜ 未接線**。
④ 本案之逐宗結果（`R2` 左·退縮 `3.5 m`·態甲乙同）：`628-42(1)` 不配地；`628-41(1)` 遞補至緊鄰位置、藍影合格（`176.60` ㎡）——見 `docs/reports/W-G.9-309R_執行報告.md`。
🛑 **主線之落地狀態 ＝ ⬜ 未實作**（入主線須 KL 另一次放行）。
````

#### 附件 C-4　末端追加　`CLAUDE.md`　sha256 `16b95b767c03e2e53be06f713b2e321bc0fad6d70895f6c3e96040dbfd18a4a0`

````md

## 🔧 進度表之現況更正：`K-9-17` 遞補迴圈已落地（`W-G.9-309`·⛔ 上文一字不刪·純末端追加）

🩸 **被更正之對象**：`:590`（⬜ 未開工）、`:1099`（⬜ 未開工）、`:1457`（🔶 部分落地·「`K-9-17` 遞補迴圈……本批⛔ 不辦」）。
🔒 **現況**（態 `2f46579`·碼面實查）：`W-G.9-269 c3`（`17fd981`·`2026-09-12`）已移除旗標 `WG9269_K917_BACKFILL` ⇒ `K-9-23` 閘一（藍影）之判由 `k917_should_drop` 消費，不合格者不配地、由鏈之下一宗遞補（`app.py` 左右鏈與 `verify/stepg_pipeline.py` 左右鏈·四處）；**閘二**（`K-9-12` 矩形容納）⬜ 仍未接線；`_lot_gate` 本身仍無副作用（只回傳判定）。
🔒 **`W-G.9-309`**：`GB-170` 之修與強制側之藍影受檢宗序（`K-9-31 ④`／`K-9-32 ②④`）⇒ 凍存分支 `verify/W-G.9-299-gb170` 落地；主線 ⬜。
🛑 本節⛔ 改上文一字（append-only）；上文三列之字⛔ 改，以本節為準讀之。
````

SELF_SHA256: 1fc8976f2222a1b60d2e7c7ab4860b9e3daa665986e637f75e8b597426f4a977
