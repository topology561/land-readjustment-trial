# `W-G.9-348R`　驗證器二處之更正與攢批登記：執行報告

> **受單** ＝ CC（Windows·施工樹 `.claude/worktrees/wg9-284-construction-window-667198`）。**開工態** ＝ `57c4623c8d28525565ef0665cffc53e9371b10e6`。
> 本報告之數皆於本窗當場實跑；出艙檔存倉外之目錄 `<O>`（本窗 scratchpad 之 `O\`）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 訊息首列 | numstat（增／刪） |
|---|---|---|---|
| 零 | `7a56a8e30ab3d5c57ac54870d3a5713e141bbe7b` | `W-G.9-348 工項零：本單原封入倉 ⛔ 零生產碼` | `docs/orders/W-G.9-348_重量單.md` `586／0` |
| 一 | `f8a8c53e1590049e47c48fd0065b85593c89cebc` | `W-G.9-348 工項一：量測器 F7（harvest 快取鍵）入倉 ⛔ 零生產碼` | `verify/probes/probe_WG9348_harvest_key.py` `97／0` |
| 二 | `2bec5870e422c57f59ec1edfb65be5d0a1125566` | `W-G.9-348 工項二：app_harvest 快取鍵之正規化（自誤 479）＋ k* 經驗錨 3.5m 之重錨（段三·逐塊歸因）🔴 生產碼` | `verify/app_harvest.py` `9／3`；`verify/run_verification.py` `6／1` |
| 三 | `84195d7fe663e032a1236c7a9eadc721a7a9fe16` | `W-G.9-348 工項三：攢批登記（自誤 524〜537·GB-190／GB-191·GB-186／GB-153 之進度）＋ 待落地清單之更新 ⛔ 零生產碼` | `CLAUDE.md` `17／0`；自誤登記 `142／0`；`GB` 登記表 `39／0` |
| 四 | （本檔之 `commit`·見對話） | `W-G.9-348 工項四：執行報告入倉 ⛔ 零生產碼` | 本檔（新檔） |

`push`：工項零 `57c4623..7a56a8e`；工項一 `7a56a8e..f8a8c53`；工項二 `f8a8c53..2bec587`（驗畢後·與驗為分開之呼叫）；工項三 `2bec587..84195d7`。皆快轉、皆首推即成、⛔ `--force`。

---

## ② 停機款 `1`〜`12` 之三值（款／實測／判）

| # | 款（要旨） | 實測 | 判 |
|---|---|---|---|
| `1` | 開工主線 ＝ `57c4623`；追蹤檔無變動 | `git rev-parse origin/wip/s1-endpart` ＝ `57c4623c8d28525565ef0665cffc53e9371b10e6`；`checkout --detach` 後 `status --porcelain --untracked-files=no` ＝ `0` 列 | 🟢 未觸 |
| `2` | 本單 bytes／`sha256`；入倉 blob 逐位相同 | 本單 `60148` B·`sha256` `797aaf43abd0bf44cd0a98afff618250856c7f2be8987061da974c86ea97bc9c`·`CR` `0`；`SELF_SHA256`（`P-5` 原口徑·受詞 `60070` B）實算 ＝ 單載 `fef0e7bd…b4ed`；入倉 blob 之 `sha256` ＝ 來源 | 🟢 未觸 |
| `3` | 五塊 bytes／`sha256` | 見 ④ 表·五塊皆逐位相符 | 🟢 未觸 |
| `4` | 工項二前置之期 | `F7` 改前 `rc 1`；`parity N1`／`N2` 改前皆 `rc 3`（訊息含 `K-9-5-4②`）；`runall_pre` 跑畢 | 🟢 未觸 |
| `5` | `D1` 之 `apply --check` 與施後 blob | `--check` `rc 0`；施後 `app_harvest.py` `00ebac621c17eb08ebe77daf37ebc8aeff7353cc`、`run_verification.py` `ed488baef2e2dab99a6c054ad0a9110675b9afdf`、`app.py` `f4c47af6b864de683b99985597310d36b1f43d23` | 🟢 未觸 |
| `6` | 驗 `V-1`〜`V-3` | 見 ③：皆如期；✅→🔴 `0` | 🟢 未觸 |
| `7` | 工項二之 `push` 須有 `§二` 放行；無被拒／無 force | 放行見 ⑤；四次 `push` 皆快轉首推即成 | 🟢 未觸 |
| `8` | 三檔刪除欄 `0`；嚴格前綴 | 三檔 numstat 刪除欄皆 `0`；改後 ＝ 改前 ＋ 塊（逐位）⇒ 嚴格前綴 | 🟢 未觸 |
| `9` | `§四` 收工閘 | 於本檔推後量·出艙於對話（⛔ 寫入本檔·自指） | ⏳ 見對話 |
| `10` | 工項五（主 checkout） | 於本檔推後辦·出艙於對話 | ⏳ 見對話 |
| `11` | CC 作「孰為正典」之判或改塊／器／命令求過 | 無（塊、器、命令一字未改） | 🟢 未觸 |
| `12` | 新檔為 `git check-ignore` 所命中 | `docs/orders/W-G.9-348_重量單.md`、`verify/probes/probe_WG9348_harvest_key.py` 皆 `rc 1`（未命中）；本檔見對話 | 🟢 未觸（本檔見對話） |

---

## ③ 工項二之前置與驗之全部出艙

**`§零` 開場**：context 餘量充足（約 `14.7M` tokens）；`probe_WG9321_issuer_anchor.py <repo> <檔> 523 522` ⇒ `rc 0`；`python -c` 出艙 `None None`（殼⛔ 設 `WV_`）；遠端 heads `30`；pre-flight 🔴 `0`／🟡 `5`（`P-1` `:70`／`:473`、`P-4` `:136`／`:170`／`:249`·與 `§五-1` 項 `9` 逐項同 ⇒ 依單之具名豁免）／ℹ️ `P-5` 相符、`P-3` `def main` ＝ `18054`-`25633`。

**`§零-1` 取號**：`wg9268_gate6_occupancy.py 57c4623 W-G.9-348 W-G.9-347 W-G.9-397` ⇒ `rc 0`，母體 `897` 檔（讀不到 `20`）；四列之數與單之表逐格同。意指占用（母體 ＝ 開工態追蹤檔 `2695`·可讀 `2671`·讀不到 `24`·錨定框·列框）：`自誤 524`〜`537` 裸／B／C 皆 `0/0`；對照甲 `自誤 523` 裸 `3/11`·B `0/0`·C `3/10`；`GB-190`／`GB-191` 皆 `0/0`；對照甲 `GB-189` `4/21`；對照乙（人造）各形 `0/0`。

### `F7`（`V-1`）二態全文

改前（`f8a8c53`）⇒ `rc 1`：
```
  W0 正規形：C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-284-construction-window-667198\app.py ⇒ 鍵數 1
  🔴 W1 含 . 段：C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-284-construction-window-667198\.\app.py ⇒ 同一物件 False·streamlit 未被換 False·鍵數 2
  🔴 W2 含 .. 段：C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-284-construction-window-667198\verify\..\app.py ⇒ 同一物件 False·streamlit 未被換 False·鍵數 3
  🔴 W3 分隔符互換：C:/Users/admin/Desktop/land-readjustment-trial/.claude/worktrees/wg9-284-construction-window-667198/app.py ⇒ 同一物件 False·streamlit 未被換 False·鍵數 4
  🔴 鍵數 ＝ 4（期 1）
  ✅ 對照（複本 C:\Users\admin\AppData\Local\Temp\wg9348_5rlngsl1\app.py）⇒ 非同一物件 True·鍵數 5（期 5）
⇒ 紅 ['W1 含 . 段', 'W2 含 .. 段', 'W3 分隔符互換', '鍵數']；rc 1
```
改後（`2bec587`）⇒ `rc 0`：
```
  W0 正規形：C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-284-construction-window-667198\app.py ⇒ 鍵數 1
  ✅ W1 含 . 段：C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-284-construction-window-667198\.\app.py ⇒ 同一物件 True·streamlit 未被換 True·鍵數 1
  ✅ W2 含 .. 段：C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg9-284-construction-window-667198\verify\..\app.py ⇒ 同一物件 True·streamlit 未被換 True·鍵數 1
  ✅ W3 分隔符互換：C:/Users/admin/Desktop/land-readjustment-trial/.claude/worktrees/wg9-284-construction-window-667198/app.py ⇒ 同一物件 True·streamlit 未被換 True·鍵數 1
  ✅ 鍵數 ＝ 1（期 1）
  ✅ 對照（複本 C:\Users\admin\AppData\Local\Temp\wg9348_csoirzmr\app.py）⇒ 非同一物件 True·鍵數 2（期 2）
⇒ 紅 []；rc 0
```

### `parity` 五份（`3.5 off`·`V-2` 與前置 `2`）

`N1` ＝ `<repo 反斜線>\.`；`N2` ＝ 同路徑之正斜線形；`R` ＝ 正規形（反斜線絕對路徑）。

| 份 | `rc` | 末三列（全檔僅 `2` 列者錄全檔） |
|---|---|---|
| `N1` 改前 | `3` | `【F4 parity】態 f8a8c53e1590049e47c48fd0065b85593c89cebc·退縮 3.5·WV_K6B_STAGE3=off·擾動 False`／`🔴 harness 執行中止：RuntimeError: 🔴 K-9-5-4②：`side_mid`=(310506.137745, 2651928.673455) 於 `f3_cad_side_lines_by_side` 查無對應側界 ⇒ 停（no-silent-fallback） ⇒ 無從判定` |
| `N2` 改前 | `3` | 同上（逐字） |
| `N1` 改後 | `0` | `✅ 配地列（harness 68／畫面 67；不符格 0）`／`ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]`／`⇒ rc 0（不符 0 項）` |
| `N2` 改後 | `0` | 同上（逐字） |
| `R` 改後 | `0` | 同上（逐字） |

### `runall` 對拍（`V-3`·前置 `3`）

`<P>` ＝ `C:\Users\admin\AppData\Local\Temp\w348P`（前置與驗同一路徑·每次跑畢 `worktree remove --force`）。`runall_pre`（`f8a8c53`·`10m10s`·`rc 1`）；`runall_post`（`2bec587`·`9m11s`·`rc 1`）。`probe_WG9343_step0_flag.py runall` ⇒ `rc 0`，全文：
```
【runall】項 64／64·PASS 30 → 31·FAIL 34 → 33
  #27 k* 六塊經驗錨3.5m {'R1': 1, 'R2': 8, 'R3': 7, 'R4': 1, 'R5': 7, 'R6': 6} ⇒ 名目改為 k* 六塊經驗錨3.5m {'R1': 1, 'R2': 7, 'R3': 7, 'R4': 1, 'R5': 4, 'R6': 6} ｜狀態 FAIL → PASS｜違規數 0 → 0｜本體 異
  #58 W-F F.0 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #59 W-F F.1 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #60 W-F F.2 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #61 W-F F.3 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #62 W-F F.4 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #64 W-G G.2 世代幾何曝出契約 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  相異項 7；其餘 57 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／34 → 22／33；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
```
✅→🔴 ＝ `0`（狀態有變者唯 `#27`，FAIL → PASS）。

**本體之異列**（以同器之 `_ra_parse` 解析·逐項 `diff`）：

| 項 | 改前 | 改後 | Δ |
|---|---|---|---|
| `#27` | 本體 `1` 列：`        實得 {'R1': 1, 'R2': 7, 'R4': 1, 'R6': 6, 'R5': 4, 'R3': 7}` | 本體 `0` 列（PASS） | — |
| `#58` | `        le "C:\Users\admin\AppData\Local\Temp\w348P\verify\run_verification.py", line 1009, in main` | `… line 1014, in main` | `+5` |
| `#59` | `  File "<R>/verify/run_verification.py", line 1078, in main` | `… line 1083, in main` | `+5` |
| `#60` | `… line 1129, in main` | `… line 1134, in main` | `+5` |
| `#61` | `… line 1195, in main` | `… line 1200, in main` | `+5` |
| `#62` | `… line 1262, in main` | `… line 1267, in main` | `+5` |
| `#64` | `… line 1461, in main` | `… line 1466, in main` | `+5` |

`#58`〜`#62`、`#64` 各恰 `1` 異列，皆僅 `verify/run_verification.py` 之 traceback 行號 `+5`；本體列數各同（`9`／`6`／`6`／`6`／`6`／`13`）。

---

## ④ 五塊之實得與三檔之改前改後

| 塊 | 圍欄列（本單） | bytes | `sha256` | 列 | 判 |
|---|---|---|---|---|---|
| `D1` | `218`–`269` | `3121` | `ccfab0bc8f3c2dfaeca3d3d8efe1d2dca33f99bbc08facdf855cccb5c62774f8` | `50` | ✅ |
| `F7` | `273`–`371` | `4440` | `43a1fb447d49e18512efb20530af338d7fe51dfd2a161f97b50fdd4a3ac54b2d` | `97` | ✅ |
| `E1` | `375`–`518` | `16406` | `06613923020544c0c2274e314fab5a7af033b4034206a26123421851787d53f2` | `142` | ✅ |
| `G1` | `522`–`562` | `7677` | `7050d004f136c042e0d46e445b3e225101917ec8e739cd83c855f4b84ae38226` | `39` | ✅ |
| `P2` | `566`–`584` | `2663` | `df8df0440ec7f843861d583ac38047579d8e7ca67d10f65c13f393b4b7456eb3` | `17` | ✅ |

| 檔 | 改前 B | 改後 B | 改後 ＝ 改前 ＋ 塊 | 改後之 `CR` |
|---|---|---|---|---|
| `CLAUDE.md` | `263603` | `266266` | ✅ | `0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1041629` | `1058035` | ✅ | `5`（全在改前之前綴；塊 `E1` 之 `CR` ＝ `0`） |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1001798` | `1009475` | ✅ | `5`（同上；塊 `G1` 之 `CR` ＝ `0`） |

`F7` 入倉 blob 之 `sha256` ＝ 塊 `F7`（逐位）。

---

## ⑤ `§二` 之放行

KL 於貼本單之同一訊息內逐字答：「**是**」（該訊息 ＝ 本單之附檔 ＋ 「是」）。依 `§二`，視為工項二之生產碼 `commit` 推入主線之放行；工項二於 `V-1`〜`V-3` 皆如期後，以分開之呼叫 `push`。

---

## ⑥ 自捕與自解

**本批之自解清單**（`CLAUDE.md` 作業常規之追加五）：

| # | 疑義（逐字要旨） | 讀法 | 所取 | 機械證據 | 所棄之由 |
|---|---|---|---|---|---|
| `1` | 來源檔一「KL 置於 CC 之施工樹之根」，而施工樹之根無之 | (a) 停機；(b) 取 KL 主 checkout 之根（單首已明載此退路） | (b) | 取得檔之 `sha256` 與 `P-5` 自驗皆相符（②） | (a) 單已授此退路 |
| `2` | `commit` 訊息「逐字」，而本倉慣例於首列後附 `Co-Authored-By` 列 | (a) 僅首列；(b) 首列逐字 ＋ 慣例之附列 | (b) | `57c4623` 等前批 `commit` 皆為此形（`git log -3 --format=%B`） | 首列逐字不變；附列與前批同形（白名單 `3`） |
| `3` | 收工閘 `3`「本批文字檔之 `CR` 合計 `0`」，而二登記檔改後各含 `CR` `5` | (a) 以全檔計；(b) 以本批所增之內容計 | 二數並報 | 改後 ＝ 改前 ＋ 塊（逐位），五塊之 `CR` 皆 `0` ⇒ 該 `5` 全在改前之前綴 | 本批⛔ 改既有文字；出艙二數（白名單 `8`） |

**自捕**：
1. 工項三之首試以 heredoc 內聯 Python，為 `wg9237_heredoc_guard` 之 PreToolUse 閘所擋（`GB-143`）；該命令整條未執行（含其中之 `worktree remove`），改以 scratchpad 之腳本檔呼叫；其後另行 `worktree remove`。量測器層（白名單 `5`）。
2. 本體 `diff` 之輔助腳本首跑印 `ALL … False`：其「本體列數不同」之判未豁免 `#27`（FAIL → PASS 之本體必由 `1` 列變 `0` 列）。逐項出艙後，`#58`〜`#62`、`#64` 皆「僅行號 `+5`」、其他 `0`；量測器紅、⛔ 受詞紅（白名單 `5`）。
3. 出艙 `parity` 末列之首試，於 bash 雙引號內以 `"$O\\$f"` 串路徑，`\$` 被讀為跳脫而檔名不展開（`No such file`）；改以正斜線路徑重取。量測器層。

---

## 🔧 更正（`W-G.9-349` 工項三·⛔ 上文一字不刪·純末端追加）

🩸 **被更正之對象**：本檔 ④ 之第二表二列（`docs/reports/W-G.9波_claude.ai側自誤登記.md`／`docs/reports/W-G.4_泛用阻塞項登記表.md`）之「改後之 `CR`」欄逐字 `` `5`（全在改前之前綴；塊 `E1` 之 `CR` ＝ `0`） ``／`` `5`（同上；塊 `G1` 之 `CR` ＝ `0`） ``，與 ⑥ 自解清單 `3` 之「而二登記檔改後各含 `CR` `5`」及其所取「二數並報」。
🔒 **實為**：二檔之換行符 `CR`（位元組 `0x0D`）於改前（`2bec587`）與改後（`84195d7`）皆 **`0`**；所計之 `5` 係字面二字元（反斜線 ＋ 小寫 `r`）之出現數（二檔改前改後各 `5`·皆在改前之前綴）。器之判別力：`data/V6.dxf` 之 `CR` ＝ `12308`。
🔒 **出處**：CC 於推送工項四後自捕（`W-G.9-348` 之回報·對話）；發單側窗四十五自倉復算（態 `88dc179`）。
🔒 收工閘 `3`（本批文字檔之 `CR` 合計 `0`）⛔ 受影響——其當場所量者為真 `CR`。零土地後果。
