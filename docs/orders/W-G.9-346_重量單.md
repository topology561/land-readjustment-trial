# `W-G.9-346`　重量單：段三畫面入口之「中斷即停機」——`W-G.9-345` reviewer 之 W-A／W-B 之修 ＋ 量測器 `F6` 入倉

> **發單** ＝ 發單側窗四十二·`2026-09-26`。**受單** ＝ CC 新窗（於 **CC 之施工樹**施工·⛔ 於 KL 之主 checkout）。
> **級** ＝ **重**（生產碼：`app.py` 模組層之 `f3_screen_k6b_stage3` 與其上二常數·⛔ 動 `def main()` 一字）。
> **開工態** ＝ 側支 `verify/W-G.9-343-k929b` ＝ `4a633d0fae4960109b6a892691ab14b5f3738a09`；主線 `wip/s1-endpart` ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`（**本單⛔ 動主線**）。
> **KL 放行** ＝ 見 `§二`。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`。塊 `D1`／`P1` 以**檔案管線**、依**圍欄之逐列索引**機械抽取（`§五-1` 之抽取式）並以二進位寫出（`newline='\n'`）；`commit` 訊息一律 `git commit -F`。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`。
> 🔑 **二來源檔**（KL 置於 **CC 之施工樹之根**·檔名逐字）：`W-G.9-346_重量單.md`（本單）／`probe_WG9346_failclosed.py`（檔 `F6`）。CC 一律**二進位複製**、⛔ 讀入改寫。施工樹之根無之 ⇒ 取 KL 主 checkout 之根（承 `W-G.9-345R` 自解 `1`）。
> 🔑 **`run_all` 一律於倉外之拋棄式 worktree 跑，且改前、改後用<u>同一倉外路徑</u>**（`git worktree add --detach <P> <commit>`；跑畢 `git worktree remove --force <P>`；再以同一 `<P>` 建下一態）。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0` 與 `WV_K6B_STAGE3`（先以 `python -c "import os;print(os.environ.get('WV_K6_STEP0'),os.environ.get('WV_K6B_STAGE3'))"` 出艙 `None None`）；器 `F4`／`F6` 於行程內自設旗標。
> 🛑 **本單⛔ 及於**：`def main()`；`k6b_stage3_run`、`k6b_stage3_selected`、`k6b_stage3_fingerprint`、`k6b_screen_build_for_g`、`_build_wf_ctx`；`verify/**`（工項一之 `F6` 除外）；`K-6` 典／`GB` 簿／自誤簿／`VR` 簿；任何錨；主線。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/verify/W-G.9-343-k929b` ＝ `4a633d0fae4960109b6a892691ab14b5f3738a09`、`git rev-parse origin/wip/s1-endpart` ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`；施工樹 `git checkout --detach origin/verify/W-G.9-343-k929b` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 523 522` ⇒ `rc 0`。
4. 二來源檔之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態（`4a633d0`）之 `docs/` 全檔 **`893`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗四十二實跑 `python verify/probes/wg9268_gate6_occupancy.py 4a633d0 W-G.9-346 W-G.9-345 W-G.9-396`：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-346`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-345` | `2`／`3`／`4` | `2`／`3`／`4` | `7` | `2` | `2`／`23` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`1` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`2` | 🟢 |

本單⛔ 鑄任何號。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時側支 ≠ `4a633d0` 或主線 ≠ `6090a7f`，或追蹤檔有變動 |
| `2` | 本單或 `F6` 之 bytes／`sha256` 與 `§五-1` 不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`P1` 之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二之任一期不符（尤：`F6` 之紅集 ≠ `{C1, C2, C3, C4, C6}`） |
| `5` | 工項三之 `commit` 改動 `app.py` 以外之檔，或期末 `app.py` 之 blob ≠ `§五-1` 項 `6` |
| `6` | 工項四之任一閘不符 |
| `7` | `run_all` 二態對拍之 ✅→🔴 ≠ `0` 或相異項 ≠ `0`——⛔ 自判其當否，逐項出艙後停機 |
| `8` | CC 作任何「孰為正典」「應改為」之判，或改 `F4`／`F6`、塊、命令一字以求其過 |
| `9` | 任一 `commit` 推至**主線**；或工項一之父 ≠ 工項零之 `commit`；或工項三之父 ≠ 工項一之 `commit` |
| `10` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py docs/orders/W-G.9-346_重量單.md` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `7`。

---

## `§一`　態錨（錨於 `4a633d0`·發單側窗四十二自倉實跑）

| # | 項 | 值 |
|---|---|---|
| `1` | 側支／主線 | 側支 `verify/W-G.9-343-k929b` ＝ `4a633d0fae4960109b6a892691ab14b5f3738a09`（其下 `b0c9edc` ＝ `W-G.9-345` 工項五之生產碼）；主線 ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`；遠端 heads **`30`**（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`·`git ls-remote --heads origin` 實數） |
| `2` | `app.py` 之 blob | `550ba546f2ef172f9029c284e1323e426438f0bc`（＝ `b0c9edc:app.py`） |
| `3` | `CLAUDE.md` | `259916` B（以換行結尾·CR `0`） |
| `4` | `W-G.9-345` 之復驗（發單側窗四十二·於本機〔Linux〕自跑） | `F4 ast`（`877cbed`·基 `0ec1e42`）`rc 0`·`12` 列全 ✅；`parity` 於端 `3.5 on`／`0.0 on`／`3.5 s3off`／`3.5 off`／`0.0 off` 皆 `rc 0`（配地列 `60／59`、`63／62`、`68／67`、`68／67`、`63／62`·不符格 `0`·`Z` ＝ `[('harness','R1-抵費地-2')]`）；`--perturb` `rc 1`；`wiring`／`f4ctx`／`wfctx 3.5`／`wfctx 0.0` 皆 `rc 0`；`VA-5` 五器於三態皆 `rc 0`；`run_all` 同一倉外路徑 `0ec1e42` 對 `b0c9edc`：`64／64`·`30→30`·`34→34`·相異 `1` 項（`#64 W-G G.2` 之 `run_verification.py` 行號 `1460 → 1461`） |
| `5` | 畫面路徑之段三紀錄（`F4 parity 3.5 on` 之 `json`） | `18` 列，逐列與 `W-G.9-344` 附錄乙同（候選、層級、成否、整筆併入、試算 G、門檻、後處理之受併量） |

---

## `§二`　KL 之語與射程

🔒 **由**：本單係 `W-G.9-345` 之 reviewer 所提 W-A／W-B（`docs/reports/W-G.9-345R_段三畫面路徑_執行報告.md` 之 `⑧`）之修；其性質屬 KL 已裁之範圍——`W-G.9-345 §二` 之通知逐字「仍停機者限於規則未定或無從判定之情形」——段三執行中斷即「無從判定」，本單使其一律 loud，⛔ 新立任何配地規則。
🔒 **生產碼之放行**（`CLAUDE.md` 之 `常規一` 補款：生產碼 `commit` 之 `push` 前請示）：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項三之 `push`（**只及側支**）之放行，CC 將其逐字載入報告；**無之 ⇒ 工項三、四畢後停於 `push` 前，於對話請示 KL**。
🛑 **射程**：`(a)` 工項三之生產碼 `commit` 只推**側支** `verify/W-G.9-343-k929b`；`(b)` 工項零、一、五同落該側支；`(c)` **主線之快轉⛔ 在本放行內**（與 `K-9-29 二`、段三同批，另呈 KL 放行）；`(d)` 本案之配地結果**⛔ 變**（`VC-3`／`VC-7` 證之）。

---

## `§三`　規格

### `§三-0`　缺口之所在（發單側窗四十二實測·⛔ 為 CC 之判）

1. **W-A**（執行中斷而不留痕）：`f3_screen_k6b_stage3` 只於 `k6b_stage3_run` 丟 `RuntimeError` 時存停機訊息；他例外（如 `KeyError`）、首趟或終趟之 `st.stop()` 皆⛔ 存停機訊息、亦無指紋 ⇒ 其後之配地經 `k6b_screen_build_for_g` 得 `None`，即以段三前之宗地配出而**無警示**。本案退縮 `3.5 m` 之後果：`R3` 右、`R5` 左回為強制抵費地（`307.79`／`299.73 ㎡`·出處 ＝ `CLAUDE.md` 之 `W-G.9-343` 待落地節「同批入主線之由」），⛔ KL `2026-09-25` 所放行之地主甲合併宗。此係 `W-G.9-345 §三-2` 步驟 `7` 之規格缺口（發單側窗四十一·待鑄自誤·攢批）。
2. **W-B**（讀到前一趟之殘值）：街角選位本體（`f3_screen_corner_pk_run`）只於「有結果」時寫 `f3_corner_winners`（其 If 之 test ＝ `_f3_corner_winners_state`）與 `f3L_corner_winners`／`f3_corner_cand_diag`／`f3_k6b_stage2_order`／`f3_k6b_stage1_locked_by_block`（其 If 之 test ＝ `_corner_select_results`）；段三之首趟與試算趟皆自 session 讀回之 ⇒ 任一趟落入「無結果」分支即讀到前一趟之值。
3. **實測**（`F6 run <repo> 3.5` 於開工態）：`C1`／`C2`／`C6` ⇒ `k6b_stage3_selected` 回 `None`；`C3` ⇒ 以殘留之段二序呼叫 `k6b_stage3_run`（`1` 次）；`C4` ⇒ 試算趟 `14` 次皆無產出，段三仍跑畢並存指紋（`k6b_stage3_selected` 回段三後之宗地）。
4. reviewer 之 **W-C** ⛔ 在本單：其前半（選位後舊配地輸出之留存）係改前即有——按「優先權選位」鈕⛔ 觸發配地之自動重算（`f3_g_needs_recalc` 之寫入點唯地圖點選街角之二處）；其後半（步驟 M 於指紋不符時停住其後之頁）係 `W-G.9-345 §三-3` 第 `5` 項之設計（loud）。

### `§三-1`　改動（工項三·只動 `app.py`·**依塊 `D1` 施之**）

塊 `D1` ＝ 對 `4a633d0:app.py` 之 unified diff（`+21`／`−0`），以 `git apply` 施之；期末 `git hash-object app.py` ＝ `§五-1` 項 `6`。其語意：

- **甲**　常數 `K6B_SCREEN_READBACK_KEYS`（`6` 鍵·⊂ `K6B_SCREEN_TRIAL_KEYS`）＝ 段三自 session 讀回之街角選位產物；常數 `K6B_STAGE3_PENDING` ＝ 「未完成」之停機訊息。
- **乙**　旗標 on 時，於首趟之前：session 存 `f3_k6b_stage3_error` ＝ `K6B_STAGE3_PENDING`，並去 `f3_k6b_stage2_order`。
- **丙**　唯二正常出口撤之：「段二序為空」之出口、步驟 `8` 之成（存指紋之後）。其餘一切離開（例外、`st.stop()`）皆留之 ⇒ 配地（`k6b_screen_build_for_g`）、七級調配（`_build_wf_ctx`）、步驟 M 皆 loud，訊息止於「請重跑「街角地優先權選位」」。步驟 `7` 之 `RuntimeError` 仍以其訊息覆寫之（同改前）。
- **丁**　`trial_winner`／`alloc_state`：每趟街角選位之前去 `K6B_SCREEN_READBACK_KEYS`；其後 session 無 `f3_corner_winners` ⇒ `RuntimeError`（停機款 `9`·`alloc_state` 收為 `err` ⇒ `k6b_stage3_run` 停機）。
- 🔒 **去此 `6` 鍵⛔ 改街角選位本身之算**：二抽出函式可達之模組層函式（`80` 個·`ast` 實查）對街角選位產物之讀唯 `f3_corner_range_areas`（其可達之 `select_corner_lots_both_sides_v12` 先寫）與 `f3_pk_alloc_depth`（本體先寫），皆⛔ 在此 `6` 鍵內；且 `6` 鍵皆在 `K6B_SCREEN_TRIAL_KEYS` ⇒ 試算後由 `finally` 復原。
- 🔒 **旗標 off 之路徑一字不變**（`C5`·`VC-3` 之 `s3off`）。

### `§三-2`　許可集

- 工項三 ＝ `app.py` 唯一。
- 🔒 **通用化**：`git diff -U0 <工項一> <工項三> -- app.py` 之 `+` 列⛔ 含街廓名、地號、案名（框 ＝ regex `['"]R\d['"]|628-|UC9898|_is_uc9898`）。

---

## `§四`　工項（依序·全數於側支）

### 工項零　本單原封入倉（零生產碼）

`docs/orders/W-G.9-346_重量單.md`（新檔·二進位複製）。`commit` 訊息逐字 `W-G.9-346 工項零：本單原封入倉（側支）⛔ 零生產碼` ⇒ `push origin HEAD:verify/W-G.9-343-k929b`。

### 工項一　量測器入倉 ＋ 塊 `P1` 之末端追加（零生產碼·一 `commit`）

1. `verify/probes/probe_WG9346_failclosed.py`（**新檔**）＝ 檔 `F6` 之二進位複製。
2. 塊 `P1` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位附於 `CLAUDE.md` 之末；`CLAUDE.md` 之刪除欄 `0`。
3. `commit` 訊息逐字 `W-G.9-346 工項一：量測器入倉 ＋ 待落地清單之更新（側支）⛔ 零生產碼` ⇒ `push origin HEAD:verify/W-G.9-343-k929b`。

**塊 `P1`**：

````markdown

---

## 🔧 待落地清單之更新：段三畫面入口之「中斷即停機」（`W-G.9-346`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `4a633d0fae4960109b6a892691ab14b5f3738a09`（本批開工態·側支 `verify/W-G.9-343-k929b` 之端）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 段三·畫面入口之中斷即停機（`W-G.9-345` reviewer 之 W-A／W-B） | 段三啟用時先立「未完成」之停機訊息，唯「段二序為空」與「成」二出口撤之；首趟前去段二序；每趟試算前去讀回鍵、試算後缺 winners 表即停機 | ⬜（本批落側支後 🔶；入主線與段三同批·另候 KL 放行） | `docs/orders/W-G.9-346_重量單.md` |

🔒 **依賴序**（承 `W-G.9-345`）：段三 harness 路徑 → 段三畫面路徑 → 本批（同側支）→ `K-9-29 二` ＋ 段三同批入主線（另候 KL 放行）→ `K-9-29 六` 入池閘 → 五級。
🔒 **量測器**：`verify/probes/probe_WG9346_failclosed.py`（`run <repo> [<退縮>]`·七情形 `C0`〜`C6`·以注入造中斷）。
````

### 工項二　改前態之量測（⛔ `commit`·出艙存倉外）

於工項一之 `commit`（其生產碼 ＝ 開工態）之施工樹：

1. `python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` ⇒ **`rc 1`**；紅集 ＝ `{C1, C2, C3, C4, C6}`、`C0`／`C5` ✅（出艙末列逐字 `⇒ 紅 ['C1', 'C2', 'C3', 'C4', 'C6']；rc 1`）。
2. **`run_all` 改前**：倉外路徑 `<P>`（工項一之 `commit`）跑 `python verify/run_all.py > <倉外>/runall_before.log 2>&1` 一次。期：`rc 1`；名目 **`64`** 項（`✅ PASS` **`30`**／`🔴 FAIL` **`34`**·框 ＝ 列首 `^\s*✅ PASS `／`^\s*🔴 FAIL `）。跑畢移除該 worktree（**`<P>` 留作工項四之同一路徑**）。

### 工項三　改動（**一** `commit`·只動 `app.py`）

塊 `D1` 依圍欄之逐列索引抽出、對拍 `§五-1` 項 `4` 後寫為倉外之檔 `<D1>`；`git apply <D1>`；`git hash-object app.py` ＝ `§五-1` 項 `6`（不符 ⇒ 停機款 `5`）。`commit` 訊息逐字 `W-G.9-346 工項三：段三畫面入口之中斷即停機（W-A／W-B）🔴 生產碼`；**先於本機 `commit`**，待工項四之閘全過、且 `§二` 之放行成立後方 `push origin HEAD:verify/W-G.9-343-k929b`（閘之量測與 `push` 為分開之呼叫）。

### 工項四　閘（⛔ `commit`·於工項三之本機 `commit` 量）

依 `§五` 之 `VC-1`〜`VC-8` 逐項實跑，逐項出艙三值（期／實得／判）。全過 ⇒ 依 `§二` 放行或請示；任一不過 ⇒ 停機款 `6`（或 `5`／`7`），⛔ `push`、回報。

### 工項五　執行報告入倉（零生產碼）

`docs/reports/W-G.9-346R_段三畫面入口中斷即停機_執行報告.md`（新檔）。須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`10` 之三值；③ 二來源檔、塊 `D1`／`P1` 之實得；④ 工項二、四之全部出艙（`F6` 二態之全文、`parity` 各態之摘要、`runall_cmp.txt` 全文、全 log `diff` 之列數）；⑤ `§二` 之放行（KL 之逐字或請示之經過）；⑥ reviewer 之出艙（若送）；⑦ 執行時間；⑧ CC 之自捕與自解清單。`commit` 訊息逐字 `W-G.9-346 工項五：執行報告入倉（側支）⛔ 零生產碼` ⇒ `push origin HEAD:verify/W-G.9-343-k929b`。

---

## `§五`　【驗收】

### 工項四（於工項三之 `commit` 量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `VC-1` | `git diff --name-only <工項一> <工項三>`；`git diff --numstat <工項一> <工項三>`；`git hash-object app.py` | 恰 `app.py`；`21`／`0`；＝ `§五-1` 項 `6` |
| `VC-2` | `F6 run <repo> 3.5` | `rc 0`；`C0`〜`C6` 七列全 ✅（出艙末列逐字 `⇒ 紅 []；rc 0`）。🔒 ⛔ 以 `0.0` 代之：本案 `0 m` 之段二序 `0` 列、段三不執行 ⇒ `F6` 出 `rc 3`（無從判定） |
| `VC-3` | `F4 parity <repo> 3.5 on`；`… 0.0 on`；`… 3.5 s3off`；`… 3.5 off`；`… 0.0 off` | 皆 `rc 0`；配地列依序 `60／59`、`63／62`、`68／67`、`68／67`、`63／62`，不符格皆 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`；`3.5 on` 之段三紀錄 `18` 列 |
| `VC-4` | `F4 parity <repo> 3.5 on --perturb` | **`rc 1`** |
| `VC-5` | `F4 wiring <repo>`；`F4 wfctx <repo> 3.5`；`F4 wfctx <repo> 0.0` | 皆 `rc 0`（`wiring` 之 `W0`〜`W8` 全 ✅、丙部四突變皆 ✅） |
| `VC-6` | `issuer_anchor … 523 522`；`closegate 523 522 .`；`wfns_ast <repo>`；`F5 <repo>`；`probe_WG9341_synth <repo>` | 皆 `rc 0`；`wfns_ast` `40`／`40`／`39`；`F5` 出艙「app 側宿主 ＝ f3_screen_stepg_run」 |
| `VC-7` | 同一倉外路徑 `<P>`（工項三之 `commit`）跑 `python verify/run_all.py > <倉外>/runall_after.log 2>&1`；`python verify/probes/probe_WG9343_step0_flag.py runall <倉外>/runall_before.log <倉外>/runall_after.log > <倉外>/runall_cmp.txt`；`diff <倉外>/runall_before.log <倉外>/runall_after.log` | `run_all` `rc 1`；`runall` `rc 0`；`64／64`·`30→30`·`34→34`；**相異項 `0`**；全 log `diff` **`0` 列**（本改動只在畫面入口·harness 從不呼叫之） |
| `VC-8` | `git diff -U0 <工項一> <工項三> -- app.py` 之 `+` 列以 `§三-2` 之 regex 篩 | 命中 `0` |

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 檔 `F6`（`probe_WG9346_failclosed.py`） | `9352` B·`sha256` `407df5ad99dad61152fbd95dd7836b9cdc5bf5c95b8ef6be5a8f33d17eb7cdab`·CR `0` |
| `3` | 塊 `P1` | 1170 B·`sha256` `6b585f6efc3532cc6ccdf5bc66afd987bb37447a60d2f371eeec062135ce6655`；附於 `CLAUDE.md`（`259916` B）之末後，期末 ＝ `261086` B |
| `4` | 塊 `D1` | 4078 B·`sha256` `456a49bb7864ab0cb61195dbc361ffdeb1c3e0d709897b12471fd889673473f7` |
| `5` | 開工態之 `app.py` | blob `550ba546f2ef172f9029c284e1323e426438f0bc` |
| `6` | 期末之 `app.py` | blob `f4c47af6b864de683b99985597310d36b1f43d23` |
| `7` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十二於開工態實跑：🔴 機械 `0` 項／🟡 提示 `1` 項（`P-4`：列 `161`〔`§五` 工項四表之表頭所轄·`VC-7` 之計數之改前改後·⛔ 方向性之轉引 ⇒ **具名豁免**〕）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `18033`–`25612`）⇒ `rc 0` |

抽取式 ＝ 圍欄開列（`` ````markdown `` 或 `` ````diff ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　發單側窗四十二之雛形實跑（倉外·⛔ 入倉·供受單側對照·⛔ 為閘）

1. **改前**（`F6 run <repo> 3.5` 於開工態 `4a633d0`）：`rc 1`；末列逐字 `⇒ 紅 ['C1', 'C2', 'C3', 'C4', 'C6']；rc 1`；`C4` 之試算趟 `14` 次皆無產出而 `k6b_stage3_selected` 回段三後之宗地。
2. **雛形**（倉外之工作樹 ＝ `4a633d0` ＋ 塊 `D1`·`git apply --check` 於開工態通過·期末 blob ＝ `§五-1` 項 `6`）：`F6 run … 3.5` `rc 0`（七列全 ✅；`C4` 之停機訊息具名 `R5／左／628-18(2)`；`C1`／`C2`／`C6` 之訊息皆止於「請重跑「街角地優先權選位」」）；`F6 run … 0.0` `rc 3`（段二序 `0` 列）；`F4 parity` `3.5 on`／`0.0 on`／`3.5 s3off`／`3.5 off`／`0.0 off` 皆 `rc 0`（配地列 `60／59`、`63／62`、`68／67`、`68／67`、`63／62`·不符格 `0`；段三紀錄 `18`／`0`／`0` 列）；`--perturb` `rc 1`（不符格 `273`）；`wiring` `rc 0`（`W0`〜`W8` `14` 列 ✅·丙部四突變皆 ✅）；`wfctx 3.5`／`0.0` 皆 `rc 0`；`+` 列以 `§三-2` 之 regex 篩 ⇒ `0`。
3. **`run_all`**（同一倉外路徑；`b0c9edc` 對「`b0c9edc` ＋ 塊 `D1`」）：二者皆 `rc 1`·`64` 項 `30`／`34`；`runall` 相異 `0` 項；全 log `diff` `0` 列。
4. **`W-G.9-345` 之復驗**（本單開工之前提）：見 `§一` 項 `4`／`5`。

---

## 附錄甲　塊 `D1`

````diff
diff --git a/app.py b/app.py
index 550ba54..f4c47af 100644
--- a/app.py
+++ b/app.py
@@ -17769,6 +17769,13 @@ K6B_SCREEN_TRIAL_KEYS = (
     'f3_corner_cand_diag',
 )
 K6B_SCREEN_STAGE3_KEYS = ('f3_k6b_stage3_temp', 'f3_k6b_stage3_build', 'f3_k6b_stage3_fp')
+# 🆕 `W-G.9-346`：段三於街角選位（首趟／試算趟）後自 session 讀回之鍵（⊂ K6B_SCREEN_TRIAL_KEYS）；
+#   街角選位本體於「無結果」分支⛔ 寫之 ⇒ 每趟前先去之，使缺漏現形、⛔ 讀到前一趟之殘值。
+K6B_SCREEN_READBACK_KEYS = (
+    'f3_corner_winners', 'f3_corner_cand_diag', 'f3L_forced_offset', 'f3_corner_range_polys',
+    'f3_k6b_stage2_order', 'f3_k6b_stage1_locked_by_block',
+)
+K6B_STAGE3_PENDING = '「街角合併重試」未完成（執行中斷）'
 
 
 class _K6BTrialStop(Exception):
@@ -17887,6 +17894,9 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
         _ss['f3_k6b_stage3_log'] = []
         _ss['f3_k6b_stage3_order_used'] = _order
         return {'temp': temp0, 'build': build0, 'log': [], 'order': _order, 'ran': False}
+    # 🆕 `W-G.9-346`：段三啟用 ⇒ 先立「未完成」（唯正常出口撤之）；任何中斷皆使其後之配地 loud
+    _ss['f3_k6b_stage3_error'] = K6B_STAGE3_PENDING
+    _ss.pop('f3_k6b_stage2_order', None)
     # 3. 首趟（代理·寫真 session）；中止 ⇒ 以真 st 再跑一次使畫面現其訊息後重拋
     _px0 = _K6BTrialSt(st)
     try:
@@ -17901,6 +17911,7 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
         f3_screen_corner_pk_run(st, **pk_kwargs)
         _ss['f3_k6b_stage3_log'] = []
         _ss['f3_k6b_stage3_order_used'] = order
+        _ss.pop('f3_k6b_stage3_error', None)
         return {'temp': temp0, 'build': build0, 'log': [], 'order': order, 'ran': False}
 
     # 5. 三注入物
@@ -17929,6 +17940,8 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
 
     def trial_winner(temp, build, blk, end, cand):
         _t, _b = _copy_pair(temp, build)
+        for _k_rb in K6B_SCREEN_READBACK_KEYS:
+            _ss.pop(_k_rb, None)
         _px = _K6BTrialSt(st)
         try:
             with _cl_s3.redirect_stdout(_io_s3.StringIO()):
@@ -17937,6 +17950,9 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
             raise RuntimeError(
                 f"🔴 [K-6-B 段三·畫面] 試算（街角選位）中止：{blk}／{end}／{cand}"
                 f"——{_px.msgs[-1:]}（停機款 9）") from _e_tw
+        if 'f3_corner_winners' not in _ss:
+            raise RuntimeError(
+                f"🔴 [K-6-B 段三·畫面] 試算（街角選位）未產出 winners 表：{blk}／{end}／{cand}（停機款 9）")
         _key = {'左': 'p1_end', '右': 'p2_end'}[end]
         _win = ((_ss.get('f3_corner_winners') or {}).get(blk) or {}).get(_key)
         _row = next((r for r in (_ss.get('f3_corner_cand_diag') or [])
@@ -17953,9 +17969,13 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
         K917_DROPPED.clear()
         _px = _K6BTrialSt(st)
         _err = None
+        for _k_rb in K6B_SCREEN_READBACK_KEYS:
+            _ss.pop(_k_rb, None)
         try:
             with _cl_s3.redirect_stdout(_io_s3.StringIO()):
                 f3_screen_corner_pk_run(_px, **dict(pk_kwargs, temp_parcels=_t, build_parcels=_b))
+                if 'f3_corner_winners' not in _ss:
+                    raise RuntimeError('試算（街角選位）未產出 winners 表（停機款 9）')
                 f3_screen_stepg_run(_px, **dict(
                     g_kwargs, _auto_recalc=False, _btn_clicked=True, build_parcels=_b,
                     _new_params=dict(_ss.get(g_kwargs['_param_key']) or {})))
@@ -18026,6 +18046,7 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
     _ss['f3_k6b_stage3_temp'] = temp2
     _ss['f3_k6b_stage3_build'] = build2
     _ss['f3_k6b_stage3_fp'] = k6b_stage3_fingerprint(build0, _ss['f3L_setback_default'])
+    _ss.pop('f3_k6b_stage3_error', None)
     return {'temp': temp2, 'build': build2, 'log': log, 'order': order, 'ran': True}
 
 
````

SELF_SHA256: d103932af690780ad86876dadc87f553c7c7b1a07d384edb3799b99a5c4fafb0
