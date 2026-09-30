# `W-G.9-359R`　調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）＋ 正面道路只限「道路」類 ＋ 驗證路徑之區外道路名稱——執行報告（原單 ＋ 補令一 ＋ 補令二）

> **單** ＝ `docs/orders/W-G.9-359_規格單.md`（原單）＋ `docs/orders/W-G.9-359_補令一.md` ＋ `docs/orders/W-G.9-359_補令二.md`（相牴以後者為準）。
> **側支** `verify/W-G.9-359-cand`（主線 `wip/s1-endpart` ＝ `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`·⛔ 動）。
> **生產碼之終態**（工項二 ＝ `e1b5b04ac2957e1e732854f58f50f99d37bb8ea5`）：`app.py` `cae25232047add2dc6703d9b2d1cee50d1601472`（`1639619` B·對 `1841914` 增 `343`／刪 `3`）、`verify/run_verification.py` `3bd2b378368df204f0c0fca1734d597851e1252b`（`103178` B·增 `21`／刪 `0`）；資料檔 `verify/case_front_road_names_UC9898.json` `449d375530d8d2207f39aec9f9ac3ba7b524b1c7`。
> 🔒 **本案之配地、街角、抵費地皆⛔ 變**（`V-2`〜`V-5` 逐位同開工態）；名單**僅顯示**、⛔ 消費端。
> 🛑 收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。

---

## ①　逐 `commit` 之 hash 與工項（本側支之全部十一筆·依序）

| # | `commit` | 工項 | 生產碼判法（逐 `commit`） |
|---|---|---|---|
| `1` | `ecef7f3051af75ff3352a15ef02143e3dda85259` | 工項零：原單原封入倉 | `0` 行 |
| `2` | `14a026bf6e982505304747f1a0f6cb57d3b515a8` | 工項一：量測器 `F18` 入倉 | `0` 行 |
| `3` | `b63ad7fca595075d32ca2fb51d9fc835241299b9` | 停機報告一（停機款 `12`·`F-1`） | `0` 行 |
| `4` | `f82b43bf968a7ce33c79121d9e06dd7fb605af39` | 補令一 工項零′：補令一原封入倉 | `0` 行 |
| `5` | `2432ae2d3616a64254578d6a3b8365e0fb969f0b` | 補令一 工項一′：`F18` 之增項（`C19`〜`C22`） | `0` 行 |
| `6` | `03910d8d1727b6877f4ad925137c98031829426e` | 停機報告二（停機款 `12`·`B-1`／`B-2`） | `0` 行 |
| `7` | `47180afe1e1cfdfa476eb30e048f0a3d8bdbbde5` | 補令二 工項零″：補令二原封入倉 | `0` 行 |
| `8` | `51f082dbcf7255b071ff069410ebb7e63d4274f2` | 補令二 工項一″：`F18` 之增項（`C23`〜`C26`） | `0` 行 |
| `9` | `e1b5b04ac2957e1e732854f58f50f99d37bb8ea5` | 工項二：生產碼 ＋ 資料檔（原單 ＋ 補令一、二） | `app.py`、`verify/run_verification.py`（`2` 行） |
| `10` | `e00f7754e015002601af55e1334381af4995d39b` | 工項三：`K-9-52` 之入典（塊 `K5″`）＋ `P13` ＋ `V1` | `0` 行 |
| `11` | 本報告之 `commit` | 工項四：執行報告入倉 | `0` 行 |

🔒 未推之本地 ref（⛔ 推）：`hold/W-G.9-359-c2` ＝ `78c1c6f`（首輪之工項二）、`hold/W-G.9-359-c2b` ＝ `3edca01`（補令一之工項二）、`hold/W-G.9-359-c2c-draft` ＝ `d2070ff`（補令二之工項二初稿·依第三輪審查發現 1 修後以 `e1b5b04` 代之·`⑥`）。

## ②　停機款之三值（終態之制：補令二 `§零-1` 之 `1″`〜`4″` 代原單同號；`5`〜`12` 照原單）

| 款 | 期 | 實 |
|---|---|---|
| `1″` | 主線 `1841914`、側支 `03910d8`、heads `33`、施工樹淨 | 皆符（未成就） |
| `2″` | 補令二 bytes／`sha256` ＝ `§五`；來源三處之一；入倉逐位 | `49043` B·`sha256` `b632d698f858ccfd599e186afc60481b93a1da03a0c7d1f765e8908a272e616c`·`SELF_SHA256` 經 `P-5` 自驗相符；來源 ＝ KL 主 checkout 之根；入倉 blob 逐位同（未成就） |
| `3″` | 塊 `F18q`／`K5″` ＝ `§五`；`git apply --check` 過；施後 blob ＝ `4fb5085b…` | `F18q` `7322` B／`103` 列、`K5″` `10130` B／`96` 列 `sha256` 皆符；施後 `verify/probes/probe_WG9359_cand.py` ＝ `4fb5085ba8ab3581b79359e260586d810047c3f6`（`47743` B·增 `61`／刪 `3`）；`J1`／`P13`／`V1` ＝ 原單 `§五-1`（未成就） |
| `4″` | 前置皆 ＝ 期 | 皆符（未成就·`③-1`） |
| `5` | 規格有歧義而涉域上判斷 | 首輪（`F-1`）與補令一之輪（`B-1`）曾成就 ⇒ 停機報告一、二；本輪未成就 |
| `6` | `V-1″`〜`V-8′` 皆 ＝ 期 | 皆符（未成就·`③-2`） |
| `7` | `push` 之目標唯本側支；⛔ 被拒、⛔ `--force` | 十筆皆快轉（`⑤`）；主線⛔ 推進（未成就） |
| `8` | 工項三之三檔之刪除欄 `0`、嚴格前綴 | `K-6` 典 `435812 → 445942`、`CLAUDE.md` `308508 → 312493`、`v3` `65433 → 67089`；刪除欄皆 `0`；皆嚴格前綴（未成就） |
| `9` | 收工閘 | 出艙於對話 |
| `10` | CC 作「孰為正典」「應改為」之判 | ⛔ 作（未成就） |
| `11` | 新檔為 `git check-ignore` 所命中 | 原單、二補令、`F18`、`J1`、二停機報告、三差異檔、本報告皆無命中（未成就） |
| `12` | 唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 | 首輪（`F-1`）與補令一之輪（`B-1`／`B-2`）成就 ⇒ 停機報告一、二；**本輪（第三輪）無 (b) 項**（`⑥-2`）⇒ 未成就 |

## ③　工項二之前置與驗之全部出艙

🔒 殼⛔ 設 `WV_`（`[None, None, None]`）；`<repo>` ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\w-g-9-350-weight-unit-b1014d`；`<O>` ＝ `C:\Users\admin\AppData\Local\Temp\wgO359`（首輪之驗移存 `<O>\r1\`、補令一之驗移存 `<O>\r2\`、補令二初稿 `d2070ff` 之不完整之驗移存 `<O>\r3a\`）；`<P>` ＝ `C:\Users\admin\AppData\Local\Temp\wgP359`（前置與驗之 `run_all` 同一路徑·各自 `git worktree add --detach` 後跑、跑畢 `git worktree remove --force`）。

### ③-1　前置

- **原單之前置 `2`〜`5`**（於 `14a026b`·首輪所跑·補令一、二准沿用）：`k6s3 run` 二退縮 `rc 0`（`n` ＝ `35`／`36`·`stage3_log_rows` ＝ `18`／`0`）；`F8 run` 二退縮 `rc 0`（`2988`／`3318` B）；`F9 run` `rc 0`（`2358` B）；`run_all` `rc 1`（准紅碼·`238132` B·`stderr` `0` B·項 `64`·PASS `28`·末端夾具／golden `21`·對帳段 `22／36`）。
- **補令二 工項二前置 `1`**（於 `51f082d`）：`F18 selftest`／`wiring`／`run` 皆 `rc 1`，末列逐字 `⇒ 紅 ['受詞缺']；rc 1`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']；rc 1`／`⇒ 紅 ['受詞缺']；rc 1`。
- **前置 `2`**：`git diff --quiet 14a026b 51f082d -- app.py ":(glob)verify/*.py"` ⇒ `rc 0`（`34` 檔）；`<O>` 之六出艙猶在 ⇒ 沿用。
- **前置 `3`（判別力之復現）**：倉外拋棄式 worktree（`51f082d` ＋ `hold/W-G.9-359-c2b` 之三檔·`app.py` ＝ `6e6d7e33…`）：`F18 selftest` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['C23', 'C24', 'C25', 'C26']；rc 1`·`P0` `30／30`。

### ③-2　驗（於 `e1b5b04`）

| # | 受詞 | 實得 | 判 |
|---|---|---|---|
| `V-1″` | `F18 selftest`／`wiring`／`run`（全文見下）；`cmp <O>\r2\f18_run_post.log <O>\f18_run_post.log` | 皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；`C1`〜`C26`（`30` 例）皆 ✅、`P0` `30／30`；`W1`〜`W6` 皆 ✅；`R0`〜`R5` 二退縮皆 ✅；**`run` 之出艙與補令一之輪逐位同**（`cmp` 相同）；本機 `8015` B ＝ `7953` B ＋ `62` 個 `CR`（Windows 文字模式之 `CRLF`；去 `CR` 後恰 ＝ 補令二所載之 `7953` B） | ✅ |
| `V-2` | `k6s3 run` 二退縮 ＋ `cmp` 二份（全文見下） | `run` 皆 `rc 0`；`cmp` 皆 `rc 0` | ✅ |
| `V-3` | `F8 run` 二退縮、`F9 run` ＋ 對前置之 `diff` | 皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；**三份 `diff` 皆 `0` B** | ✅ |
| `V-4` | `parity` 二退縮（末十列見下） | 皆 `rc 0`（`不符 0 項`）；配地列 `35`／`34`、`36`／`35`；`Z` ＝ `[('harness', 'R1-抵費地-2')]` | ✅ |
| `V-5` | `<P>` 於 `e1b5b04`：`run_all`；`probe_WG9343_step0_flag.py runall`（全文見下）；`diff` | `run_all` `rc 1`（同前置）；對拍器 `rc 0`；**`diff` 之全文 ＝ 空**（`rc 0`·`0` B；二份皆 `238132` B·`stderr` `0` B） | ✅ |
| `V-6` | 生產碼 `34` 檔對 `51f082d` | 相異恰 `2`：`app.py` `d8938792… → cae25232…`（增 `343`／刪 `3`）、`verify/run_verification.py` `4d83d2c5… → 3bd2b378…`（增 `21`／刪 `0`）；`verify/`：`A verify/case_front_road_names_UC9898.json`（`449d3755…`）、`M verify/run_verification.py`，餘 `0` | ✅ |
| `V-7` | 閘 `8″`〜`24`（三流並行·`38` 命令） | **`38` 命令皆 `rc 0`**（逐命令見下） | ✅ |
| `V-8′` | `git diff 3edca01 e1b5b04 -- app.py verify/run_verification.py` | 三 `@@`：`-11775`（`adj_pool_anchor`·自其 `def` 列起·docstring ＋ `R-6″`）、`-11823`（`adj_candidate_lists` 之 docstring、import 與巢狀之坐標之檢）、`-11847`（錨點之坐標之檢）——**皆於二函式之內**；`verify/run_verification.py` 無差；全文 ＝ `⑩` | ✅ |

#### `V-1″`　`F18 selftest` 之全文

````text
── 合成對照（harvest 之 app.py·⛔ 本案資料）──
  ✅ C1 使用分區相同者先（縱其他鍵較差、距離較遠）
  ✅ C2 最小建築面積：同級 → 往小（次一級先）→ 往大；往大者第二趟排除
  ✅ C3 正面道路相同者先
  ✅ C4 正面路寬相同者先
  ✅ C5 次一級路寬：本區實有路寬逐級往窄，較寬者排最後（問二附圖）
  ✅ C6 深度：相差 0.10 以內同深（再依距離）→ 較淺（差小者先）→ 較深（差小者先）
  ✅ C7 深度：以 tol ＝ 0.5 重算 ⇒ 0.50 以內皆同深（依距離）
  ✅ C8 距離近者先；無抵費地之街廓（距離 —）排於同鍵者之後
  ✅ C9 八鍵前七皆同 ⇒ 街廓名之字典序
  ✅ C10 公設軌：全部可建築街廓依距離（其他鍵⛔ 用）
  ✅ C11 錨點 ＝ 原有面積最大之一筆（並列取暫編地號小者）；距離自其質心起算
  ✅ C12 建地軌：原街廓居首（⛔ 排序·僅一次）
  ✅ C13a 正面道路無名者一次列出全部 ⇒ 停機
  ✅ C13b 正面路寬為 0 ⇒ 停機
  ✅ C13c 深度缺 ⇒ 停機
  ✅ C13d 原街廓非可建築街廓 ⇒ 停機
  ✅ C13e 錨點無幾何 ⇒ 停機
  ✅ C14 迄點 ＝ 各街廓之抵費地列中面積最大者之質心（並列取暫編地號小者；非抵費地、無幾何者⛔ 計）
  ✅ C15 類別表之鍵 ＝ F3_BLOCK_CATEGORIES；得為正面道路者唯「道路」
  ✅ C16 顯示列：各欄皆字串；序列標原街廓與第二趟排除；逐候選一列；總句載容差
  ✅ C17 adj_q2 ＝ 四捨五入至 0.01（ROUND_HALF_UP）
  ✅ C18 深度差以二位小數計：−0.13 ⇒ 較淺；＋0.10 ⇒ 同深
  ✅ C19 退化（buffer(0) 後為空）之池列⛔ 計；某街廓之池列皆退化 ⇒ 視同無抵費地（距離 —·排於同鍵者之後）
  ✅ C20 錨點之多邊形退化（buffer(0) 後為空）⇒ 停機
  ✅ C21 錨點之多邊形無效（自交）⇒ 以 buffer(0) 之質心起算（同抵費地之迄點）
  ✅ C22 最小建築面積非數、非有限或負 ⇒ 停機
  ✅ C23 池片之面積以 adj_q2 計為 0 者⛔ 計（0.0046 ㎡ 之細縫⛔ 計、恰 0.005 ㎡ 者計）；某街廓之池片皆如此 ⇒ 視同無抵費地
  ✅ C24 池片之坐標含非數值（NaN〔餘形非空／為空〕、無窮大、字串、None、轉之溢位）⇒ 停機（同街廓另有正常之片亦然）
  ✅ C25 池片之坐標含非數值者一次列出全部（街廓與暫編地號）；未滿 3 點之列⛔ 取、⛔ 列
  ✅ C26 錨點之坐標含非數值（NaN〔餘形非空〕、無窮大、字串）⇒ 停機，訊息含歸戶與暫編地號
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 30／30
⇒ 紅 []；rc 0
````

#### `V-1″`　`F18 wiring` 之全文

````text
── 接線（AST·app.py ＋ verify/run_verification.py）──
  ✅ W1 具名常數 ADJ_DEPTH_TIE_TOL_M ＝ 0.1、二函式之預設引用之、新函式內⛔ 字面 0.1／0.5（字面之列 []）
  ✅ W2 類別表 F3_CATEGORY_FRONT_ROAD 之鍵 ＝ F3_BLOCK_CATEGORIES、唯「道路」為真
  ✅ W3 正面道路推導之候選 ＝ 非可建築（_buildable_blocks 之補集）∩ 類別表為真者
  ✅ W4 新函式俱在、⛔ 案件字面、⛔ 讀 session、⛔ 含既有閘所禁之消費字樣（缺 []；案件字面 []；字樣 []）
  ✅ W5 main() 之候選街廓區塊以假 st 實際執行（四變體：深度取 f3_alloc_depth_by_label、路寬取 f3_sb_rows、最小建築面積取 K91_SS_MBA_EFFECTIVE、名稱以 id 取）（不符 []）
  ✅ W6 verify/run_verification.py 之 FRONT_ROAD_NAMES ＝ …/case_front_road_names_UC9898.json、load_front_road_names 在
⇒ 紅 []；rc 0
````

#### `V-1″`　`F18 run` 之全文

````text
══ 退縮 3.5 ══
  ✅ R0 區外道路名稱檔：列 ['R1', 'R4'] ＝ 推導無值者 ['R1', 'R4']；同一條（相異名稱 1）
  ✅ R1 正面道路之候選皆「道路」類（8 對·非道路 []）；推導 ＝ W-G.9-350 §一 項 5 之表：True
     G001｜建地軌｜原街廓 R1｜錨點 628-34(3)｜R1(31.23) → R4(97.09) → R3(46.93) → R2(67.32) → R6(115.55) → R5(78.63)
     G003｜公設軌｜原街廓 None｜錨點 628-17(1)｜R5(64.18) → R6(73.56) → R3(94.81) → R2(124.82) → R4(129.79) → R1(163.17)
     G004｜建地軌｜原街廓 R2｜錨點 628-52(2)｜R2(36.28) → R3(72.97) → R6(171.20) → R5(126.43) → R1(60.31) → R4(167.94)
     G006｜建地軌｜原街廓 R2｜錨點 628-49(1)｜R2(34.57) → R3(34.11) → R6(127.84) → R5(84.38) → R1(40.82) → R4(123.31)
     G009｜建地軌｜原街廓 R6｜錨點 628(6)｜R6(97.10) → R2(93.21) → R3(61.07) → R5(69.62) → R1(55.47) → R4(68.47)
     G011｜建地軌｜原街廓 R3｜錨點 628-42(4)｜R3(59.49) → R5(88.77) → R2(53.48) → R6(129.81) → R1(118.56) → R4(159.35)
     G012｜公設軌｜原街廓 None｜錨點 628-5(1)｜R4(53.45) → R6(57.29) → R5(96.35) → R3(144.58) → R1(174.34) → R2(189.34)
     G013｜公設軌｜原街廓 None｜錨點 628-6(1)｜R4(66.86) → R6(69.29) → R5(110.24) → R3(159.17) → R1(188.82) → R2(203.96)
     G014｜建地軌｜原街廓 R3｜錨點 628-28(1)｜R3(42.55) → R5(72.51) → R2(47.51) → R6(115.12) → R1(105.65) → R4(141.89)
     G015｜公設軌｜原街廓 None｜錨點 628-15(1)｜R6(65.83) → R5(95.68) → R4(125.54) → R3(145.05) → R2(183.44) → R1(204.90)
     G016｜公設軌｜原街廓 None｜錨點 719(1)｜R6(75.82) → R5(89.87) → R3(131.75) → R4(138.06) → R2(165.31) → R1(197.17)
     G018｜建地軌｜原街廓 R2｜錨點 628-51(1)｜R2(27.61) → R3(55.26) → R6(152.62) → R5(108.22) → R1(48.04) → R4(148.94)
     G020｜建地軌｜原街廓 R2｜錨點 628-50(1)｜R2(29.05) → R3(42.19) → R6(138.06) → R5(94.11) → R1(42.21) → R4(133.98)
     G021｜建地軌｜原街廓 R2｜錨點 628-35(3)｜R2(62.51) → R3(86.59) → R6(178.77) → R5(136.60) → R1(42.56) → R4(164.06)
     G024｜公設軌｜原街廓 None｜錨點 628-26(1)｜R3(67.48) → R2(71.43) → R5(83.95) → R6(120.85) → R1(132.34) → R4(157.45)
     G025｜建地軌｜原街廓 R5｜錨點 628-24(1)｜R5(80.07) → R3(81.24) → R6(108.81) → R2(95.23) → R1(150.07) → R4(154.25)
     G026｜建地軌｜原街廓 R5｜錨點 628-32(5)｜R5(124.08) → R3(70.66) → R6(169.52) → R2(27.73) → R1(73.08) → R4(172.15)
     G027｜建地軌｜原街廓 R5｜錨點 628-31(5)｜R5(123.80) → R3(71.93) → R6(169.36) → R2(27.21) → R1(86.77) → R4(177.64)
     G028｜公設軌｜原街廓 None｜錨點 628-2(1)｜R4(39.91) → R6(77.37) → R5(105.95) → R3(146.39) → R1(162.66) → R2(189.79)
     G030｜建地軌｜原街廓 R3｜錨點 628-27(1)｜R3(49.98) → R5(85.11) → R2(42.26) → R6(128.04) → R1(106.96) → R4(153.26)
     G031｜公設軌｜原街廓 None｜錨點 628-25(1)｜R3(76.06) → R2(82.89) → R5(85.78) → R6(119.38) → R1(142.52) → R4(160.05)
     G032｜建地軌｜原街廓 R6｜錨點 628-38(3)｜R6(46.56) → R2(148.34) → R3(110.34) → R5(63.12) → R1(172.18) → R4(108.58)
     G033｜建地軌｜原街廓 R3｜錨點 628-46(1)｜R3(31.54) → R5(48.82) → R2(70.26) → R6(87.36) → R1(60.64) → R4(80.72)
  ✅ R2 名單（23 單位）與外部錨逐單位逐序相同：相異 []
  ✅ R3 畫面區塊於本案資料之二表 ＝ harness 之顯示列（error []；表 2）
  ✅ R4 原街廓 R6 之建地軌 2 單位：0.1 ⇒ [('R6', 'R2', 'R3', 'R5', 'R1', 'R4')]；0.5 ⇒ [('R6', 'R5', 'R2', 'R3', 'R1', 'R4')]
  ✅ R5 公設軌 8 單位：名單 ＝ 全部可建築街廓、距離不減
══ 退縮 0.0 ══
  ✅ R0 區外道路名稱檔：列 ['R1', 'R4'] ＝ 推導無值者 ['R1', 'R4']；同一條（相異名稱 1）
  ✅ R1 正面道路之候選皆「道路」類（8 對·非道路 []）；推導 ＝ W-G.9-350 §一 項 5 之表：True
     G001｜建地軌｜原街廓 R1｜錨點 628-34(3)｜R1(25.22) → R4(97.09) → R3(50.55) → R2(61.80) → R6(115.55) → R5(80.45)
     G003｜公設軌｜原街廓 None｜錨點 628-17(1)｜R5(61.61) → R6(73.56) → R3(92.07) → R2(128.72) → R4(129.79) → R1(158.91)
     G004｜建地軌｜原街廓 R2｜錨點 628-52(2)｜R2(31.73) → R3(74.02) → R6(171.20) → R5(126.99) → R1(64.90) → R4(167.94)
     G006｜建地軌｜原街廓 R2｜錨點 628-49(1)｜R2(28.81) → R3(36.64) → R6(127.84) → R5(85.35) → R1(40.19) → R4(123.31)
     G007｜建地軌｜原街廓 R2｜錨點 628-45(3)｜R2(90.92) → R3(63.36) → R6(96.89) → R5(62.80) → R1(133.48) → R4(139.40)
     G009｜建地軌｜原街廓 R6｜錨點 628(6)｜R6(97.10) → R2(88.60) → R3(64.38) → R5(72.01) → R1(48.48) → R4(68.47)
     G011｜建地軌｜原街廓 R3｜錨點 628-42(4)｜R3(56.16) → R5(87.41) → R2(60.10) → R6(129.81) → R1(117.82) → R4(159.35)
     G012｜公設軌｜原街廓 None｜錨點 628-5(1)｜R4(53.45) → R6(57.29) → R5(97.43) → R3(145.34) → R1(167.38) → R2(188.09)
     G013｜公設軌｜原街廓 None｜錨點 628-6(1)｜R4(66.86) → R6(69.29) → R5(111.19) → R3(159.87) → R1(181.85) → R2(202.79)
     G014｜建地軌｜原街廓 R3｜錨點 628-28(1)｜R3(39.09) → R5(71.36) → R2(52.96) → R6(115.12) → R1(104.18) → R4(141.89)
     G015｜公設軌｜原街廓 None｜錨點 628-15(1)｜R6(65.83) → R5(94.14) → R4(125.54) → R3(143.40) → R2(185.91) → R1(199.20)
     G016｜公設軌｜原街廓 None｜錨點 719(1)｜R6(75.82) → R5(87.71) → R3(129.45) → R4(138.06) → R2(168.79) → R1(192.18)
     G018｜建地軌｜原街廓 R2｜錨點 628-51(1)｜R2(20.74) → R3(56.73) → R6(152.62) → R5(108.91) → R1(51.15) → R4(148.94)
     G020｜建地軌｜原街廓 R2｜錨點 628-50(1)｜R2(22.24) → R3(44.18) → R6(138.06) → R5(94.95) → R1(43.36) → R4(133.98)
     G021｜建地軌｜原街廓 R2｜錨點 628-35(3)｜R2(56.06) → R3(88.78) → R6(178.77) → R5(137.73) → R1(49.15) → R4(164.06)
     G024｜公設軌｜原街廓 None｜錨點 628-26(1)｜R3(63.88) → R2(77.63) → R5(82.14) → R6(120.85) → R1(130.81) → R4(157.45)
     G025｜建地軌｜原街廓 R5｜錨點 628-24(1)｜R5(77.75) → R3(77.69) → R6(108.81) → R2(100.85) → R1(147.57) → R4(154.25)
     G026｜建地軌｜原街廓 R5｜錨點 628-32(5)｜R5(124.32) → R3(70.92) → R6(169.52) → R2(26.29) → R1(76.81) → R4(172.15)
     G027｜建地軌｜原街廓 R5｜錨點 628-31(5)｜R5(123.70) → R3(71.39) → R6(169.36) → R2(29.85) → R1(89.85) → R4(177.64)
     G028｜公設軌｜原街廓 None｜錨點 628-2(1)｜R4(39.91) → R6(77.37) → R5(107.69) → R3(147.91) → R1(155.66) → R2(187.35)
     G030｜建地軌｜原街廓 R2｜錨點 628-27(1)｜R2(48.70) → R3(46.87) → R6(128.04) → R5(84.05) → R1(106.33) → R4(153.26)
     G031｜公設軌｜原街廓 None｜錨點 628-25(1)｜R3(72.44) → R5(83.72) → R2(89.01) → R6(119.38) → R1(140.69) → R4(160.05)
     G032｜建地軌｜原街廓 R6｜錨點 628-38(3)｜R6(46.56) → R2(150.82) → R3(108.56) → R5(61.26) → R1(166.79) → R4(108.58)
     G033｜建地軌｜原街廓 R3｜錨點 628-46(1)｜R3(34.55) → R5(50.66) → R2(67.27) → R6(87.36) → R1(54.96) → R4(80.72)
  ✅ R2 名單（24 單位）與外部錨逐單位逐序相同：相異 []
  ✅ R3 畫面區塊於本案資料之二表 ＝ harness 之顯示列（error []；表 2）
  ✅ R4 原街廓 R6 之建地軌 2 單位：0.1 ⇒ [('R6', 'R2', 'R3', 'R5', 'R1', 'R4')]；0.5 ⇒ [('R6', 'R5', 'R2', 'R3', 'R1', 'R4')]
  ✅ R5 公設軌 8 單位：名單 ＝ 全部可建築街廓、距離不減
⇒ 紅 []；rc 0
````

#### `V-2`　`k6s3 cmp` 二份

````text
── 3.5 ──
相異 0 項 ⇒ ✅ 同
── 0.0 ──
相異 0 項 ⇒ ✅ 同
````

#### `V-4`　`parity` 二份之末十列

````text
── 3.5 ──
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（57／57）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
── 0.0 ──
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（61／61）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

#### `V-5`　`runall` 對拍之全文

````text
【runall】項 64／64·PASS 28 → 28·FAIL 36 → 36
  相異項 0；其餘 64 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／36 → 22／36；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
````

`diff <O>\runall_pre.log <O>\runall_post.log` ⇒ `rc 0`·輸出 `0` B（全文 ＝ 空）。

#### `V-7`　逐命令（`<O>\gatesV7\gates_V7_{A,B,C}_summary.txt`·逐字）

````text
閘 8｜f18_selftest｜rc 0｜4s｜末列：⇒ 紅 []；rc 0
閘 8｜f18_wiring｜rc 0｜25s｜末列：⇒ 紅 []；rc 0
閘 8｜f18_run｜rc 0｜153s｜末列：⇒ 紅 []；rc 0
閘 9｜wfns_ast｜rc 0｜2s｜末列：引擎經 ns 取用之相異名 ＝ 47
閘 10｜main_synth｜rc 0｜28s｜末列：紅項 [] 器紅 0
閘 11｜synth9341｜rc 0｜3s｜末列：ε ＝ 0.0002｜rc 0
閘 12｜failclosed｜rc 0｜226s｜末列：⇒ 紅 []；rc 0
閘 13｜harvest_key｜rc 0｜6s｜末列：⇒ 紅 []；rc 0
閘 13｜k9296_selftest｜rc 0｜3s｜末列：⇒ 紅 []；rc 0
閘 13｜k9296_wiring｜rc 0｜12s｜末列：⇒ 紅 []；rc 0
閘 14｜fr_selftest｜rc 0｜22s｜末列：⇒ 紅 []；rc 0
閘 14｜fr_wiring｜rc 0｜40s｜末列：⇒ 紅 []；rc 0
閘 14｜fr_run｜rc 0｜3s｜末列：⇒ 紅 []；rc 0
閘 15｜in_selftest｜rc 0｜16s｜末列：⇒ 紅 []；rc 0
閘 15｜in_wiring｜rc 0｜38s｜末列：⇒ 紅 []；rc 0
閘 15｜in_run｜rc 0｜142s｜末列：⇒ 紅 []；rc 0
閘 16｜eb_selftest｜rc 0｜25s｜末列：⇒ 紅 []；rc 0
閘 16｜eb_wiring｜rc 0｜90s｜末列：⇒ 紅 []；rc 0
閘 16｜eb_run｜rc 0｜141s｜末列：⇒ 紅 []；rc 0
閘 17｜em_selftest｜rc 0｜22s｜末列：⇒ 紅 []；rc 0
閘 17｜em_wiring｜rc 0｜61s｜末列：⇒ 紅 []；rc 0
閘 17｜em_run｜rc 0｜621s｜末列：⇒ 紅 []；rc 0
閘 18｜ec_selftest｜rc 0｜34s｜末列：⇒ 紅 []；rc 0
閘 18｜ec_wiring｜rc 0｜31s｜末列：⇒ 紅 []；rc 0
閘 18｜ec_run｜rc 0｜553s｜末列：⇒ 紅 []；rc 0
閘 19｜sm_selftest｜rc 0｜3s｜末列：⇒ 紅 []；rc 0
閘 19｜sm_run｜rc 0｜975s｜末列：⇒ 紅 []；rc 0
閘 20｜smw_wiring｜rc 0｜44s｜末列：⇒ 紅 []；rc 0
閘 21｜parity35｜rc 0｜175s｜末列：⇒ rc 0（不符 0 項）
閘 21｜parity00｜rc 0｜62s｜末列：⇒ rc 0（不符 0 項）
閘 21｜f4_wiring｜rc 0｜27s｜末列：⇒ rc 0（不符 0·器紅 0）
閘 21｜f4_selftest｜rc 0｜0s｜末列：selftest 10/10 ⇒ ✅
閘 22｜pooltemp_run｜rc 0｜72s｜末列：⇒ rc 0
閘 22｜pooltemp_self｜rc 0｜0s｜末列：selftest 13/13 ⇒ ✅
閘 22｜k6s3_selftest｜rc 0｜0s｜末列：selftest 9/9 ⇒ ✅
閘 23｜k948_selftest｜rc 0｜3s｜末列：⇒ 紅 []；rc 0
閘 23｜k948_run｜rc 0｜139s｜末列：⇒ 紅 []；rc 0
閘 24｜k948w_wiring｜rc 0｜98s｜末列：⇒ 紅 []；rc 0
````

## ④　諸塊之實得與三檔之 bytes

| 塊 | 來源 | bytes | 列 | `sha256` | 去處 |
|---|---|---|---|---|---|
| `F18` | 原單附錄甲 | `40667` | `697` | `52acefc447431ef03af5e658b43c1736b086e58c291f639639a275354fda2456` | `verify/probes/probe_WG9359_cand.py`（blob `fa3d63be…`） |
| `J1` | 原單附錄乙 | `527` | `12` | `13cf56d7b64decb87e9697efb36803e62fb88b948a1ed58ce893f63cea2d0c5e` | `verify/case_front_road_names_UC9898.json`（blob `449d3755…`） |
| `K5` | 原單附錄丙 | `8777` | `95` | `de4f52eafe2ee09119306312fe8c70b7285ac86587db23a7c4cc42e61dacd14a` | ⛔ 附（由 `K5′`、再由 `K5″` 代之） |
| `P13` | 原單附錄丁 | `3985` | `22` | `c1ea196484f1bb72fd82e6bc583c6d93293eaf0a3c313233d1ca895a873cbaa7` | `CLAUDE.md` 之末 |
| `V1` | 原單附錄戊 | `1656` | `11` | `3088af182c12efd23bc53ce510227cbf40c383227d4e73c2706d239986645ced` | `docs/配地計算總規格_v3.md` 之末 |
| `F18p` | 補令一附錄甲 | `4812` | `67` | `f2033bf3730e0c275f416f393d7fddf6f6448f0d878253937156a911b3135fb0` | `git apply` ⇒ blob `507def0d…`（增 `36`／刪 `1`） |
| `K5′` | 補令一附錄乙 | `9754` | `96` | `ec1e0ecc935412bdb5d57afe973c84a1357806a2a82375a53f788237b7bfa123` | ⛔ 附（由 `K5″` 代之） |
| `F18q` | 補令二附錄甲 | `7322` | `103` | `64de4ee7b4c65e01edcad09ad228c4ffe54a2937379ae85bb66bb47ce954dd36` | `git apply` ⇒ blob `4fb5085b…`（增 `61`／刪 `3`） |
| `K5″` | 補令二附錄乙 | `10130` | `96` | `84153125001c17371ee6f1e3e92f9d8e38bbe8a17c0411de0dba1a94a228bf82` | `K-6` 典之末 |

三檔（工項三·皆嚴格前綴·刪除欄 `0`）：`docs/rulings/K-6_街角地分配程序與可分配判準.md` `435812 → 445942`（增 `96` 列）；`CLAUDE.md` `308508 → 312493`（增 `22` 列）；`docs/配地計算總規格_v3.md` `65433 → 67089`（增 `11` 列）。三單：原單 `105532` B（`8b3a0216…`）、補令一 `42197` B（`4d3a9325…`）、補令二 `49043` B（`b632d698…`）——`SELF_SHA256` 皆經 `P-5` 自驗相符。

## ⑤　推送之目標與推後之 heads

一律 `git push origin HEAD:verify/W-G.9-359-cand`（首推 `refs/heads/…`·`[new branch]`）：`ecef7f3`（新立）→ `14a026b` → `b63ad7f` → `f82b43b` → `2432ae2` → `03910d8` → `47180af` → `51f082d` → `e1b5b04` → `e00f775`——**皆快轉**、⛔ `--force`、⛔ 被拒。工項三推後：`git ls-remote --heads origin` 之列數 ＝ `33`；`verify/W-G.9-359-cand` ＝ `e00f775…`；`wip/s1-endpart` ＝ `1841914…`（⛔ 變）。本報告之推後之值出艙於對話。

## ⑥　CC 之自捕與自解、唯讀獨立審查之發現與處置

### ⑥-1　自捕與自解

1. 🩸 **前置 `run_all` 首跑誤併二流**（首輪）：以 `2>&1` 起 ⇒ 停之、清殘程、重建 `<P>`、以單令之形（`stderr` 另存）重跑；首跑之出艙⛔ 入任何判。
2. 🩸 **復現器之寫死判語**（補令一之輪·`repro_b12.py`）：B-2 列之括號判語係寫死之字面、與實得相反 ⇒ 出艙前改為依實得印出並增「形二」。
3. 🩸 **補令二之初稿 `d2070ff`**：第三輪審查發現 1（`(a)`）——池片之坐標之檢與多邊形之建置同在一迴圈，後列若使 `Polygon()` 拋非 `RuntimeError`（例：混維之環）即搶在「一次列出全部壞損之列」之前穿出，與 `R-6″` ①「閱畢全部所取之列後」之字面不全合 ⇒ 改為**兩段**（先閱畢全部所取之列而一次列出壞損，再建多邊形）；未推之 `d2070ff` 存本地 `hold/W-G.9-359-c2c-draft`、其不完整之驗移存 `<O>\r3a\`；修後重作工項二（`e1b5b04`·父仍 `51f082d`）並**全數重驗**。修前修後之復現（倉外工具 `chk_twopass.py`）：

````text
── 修前（d2070ff）──
非 RuntimeError 穿出：ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (4,) + inhomogeneous part.
── 對照：唯混維之列（無壞損）──
非 RuntimeError 穿出：ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detecte
── 修後（e1b5b04）──
RuntimeError：🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值（非數、無窮大或缺·資料之瑕·位置無從定）：QA／壞一、QB／壞二 ⇒ 停機
── 對照：唯混維之列（無壞損）──
非 RuntimeError 穿出：ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detecte
````

4. 自解（白名單 `8`·裝飾性之數）：`F18 run` 本機 `8015` B vs 補令二載 `7953` B——差恰 ＝ 其 `62` 個 `CR`（本機 Python 於 Windows 以文字模式寫出 `CRLF`）⇒ 去 `CR` 後逐數相符；`run_all` 本機 `238132` B（`CR` `1828` ⇒ 去之為 `236304` B）vs 原單載 `235960` B——餘差 `344` B 係路徑相依（原單明載其 bytes 平台與路徑相依、⛔ 入判）。逐位之比皆於同一平台之二份為之（`cmp`／`diff` 皆同）。🔒 本報告所嵌之諸出艙，嵌入時一律 `\r\n → \n`（逐檔 `CR` 數 ＝ `\r\n` 數·無孤立 `CR`·建構器驗之）；二差異檔原即 `LF`。

### ⑥-2　唯讀獨立審查（附則丙·三輪 ＋ 覆核）

| 輪 | 受審 | 發現 | 分類 | 處置 |
|---|---|---|---|---|
| 首輪 | `78c1c6f` | `F-1` 退化多邊形經 `buffer(0)` 為空，規格未定 | (b) | 🛑 停機報告一 ⇒ 補令一 裁一、裁二 |
| 首輪 | 同 | `F-2` 錨點之 `buffer(0)` 未載於規格文字 | (b) 極輕 | 補令一 裁三（`R-7′` ①） |
| 首輪 | 同 | `F-3` `R-5` ① 之訊息遇無正面線者誤述 | (a) | 補令一 `R-5′` ①（已施） |
| 首輪 | 同 | `F-4` 最小建築面積未檢 | (a) | 補令一 `R-5′` ②（已施） |
| 首輪 | 同 | `N-1`〜`N-6`（`N-4` 陳舊之二註解、`N-6` 第（五）項之射程） | 備註 | `N-4` ⇒ 補令一 `X-3′`（已施）；`N-6` ⇒ 補令一 裁四（`K5′`／`K5″` 讀法 `6`）；餘記之 |
| 補令一之輪 | `3edca01` | `B-1` 非空之細縫 vs 空片之排法 | (b) | 🛑 停機報告二 ⇒ 補令二 裁一（`R-6″` ②） |
| 補令一之輪 | 同 | `B-2` 坐標壞損之池片被靜默略去 | (b) | 🛑 停機報告二 ⇒ 補令二 裁二（`R-6″` ①、`R-7″` ①） |
| 補令一之輪 | 同 | `N-1`〜`N-4` | 備註 | 補令二 裁四：記之（`N-4` 之坐標一形由裁二收之） |
| 補令二之輪（第三輪） | `d2070ff` | 發現 1：壞損之檢與多邊形之建置同迴圈 ⇒ 非 `RuntimeError` 可搶先穿出 | (a) | **修**（兩段·`⑥-1` 之 `3`）⇒ `e1b5b04`；覆核四點皆合 |
| 同 | 同 | 發現 2：`adj_q2` 對 `|x| ≥ 1e26` 拋 `decimal.InvalidOperation`（`decimal` 預設精度 `28`）⇒ 有限而 `≥ 1e26 ㎡` 之池片面積今經 `R-6″` ② 穿出 `R-9`；補令二首之射程所載之「`|坐標| ≳ 1e154`·面積溢出為非有限」之門檻**實為面積 `1e26 ㎡`**（地表約 `5.1e14 ㎡` ⇒ 物理上不可達） | 記之 | 記之（⛔ 改·補令二之射程外） |
| 同 | 同 | 發現 3：異型之頂點（`dict`、字串 `"11"`、`bytes`）依「首二元」之檢與 `shapely` 之讀法不一——碼合公式之字面；流水線⛔ 產之 | 記之 | 記之 |
| 同 | 同 | 發現 4：同街廓二池列之暫編地號與面積皆同 ⇒ 並列規則窮盡、依列序（原單 `R-6` 既有）；暫編地號唯一 ⇒ 不可達 | 記之 | 記之 |

🔒 第三輪之總判：**無 (b) 項**；其自跑：`F18 selftest`／`wiring` `rc 0`（`P0` `30／30`）；以四突變（面積之判改 `is_empty`／遇首個壞損即停／去錨點之檢／池片之檢不攔 `OverflowError`）施於 CC 之碼之複本，各使 `['C23']`／`['C25']`／`['C26']`／`['C24']` 轉紅（＝ 補令二 `§二` 末所載）；模組層之名 `364`（對 `3edca01` 差集 `∅`·`X-8`）；二巢狀 `_coords_bad` 之 AST 同一。覆核（`e1b5b04`）：修改唯在 `adj_pool_anchor`、行為除次序之修外逐例同 `d2070ff`；`R-6″`、`X-8`、`F18` 皆合。暫存唯寫倉外 `C:\Users\admin\AppData\Local\Temp\wgR359\`、`…\wgR359b\`、`…\wgR359c\`。

## ⑦　設計說明（原單 `§三-5`·依 `e1b5b04`·以字樣錨定位·⛔ 以行號為錨）

### ⑦-1　原單 `R-1`〜`R-13`

| # | 落點（字樣錨） | 要點 |
|---|---|---|
| `R-1` | `grep -n "^F3_CATEGORY_FRONT_ROAD = {" app.py` | 字面 dict（`F18 W2` 以 `literal_eval` 讀之）；鍵 ＝ `F3_BLOCK_CATEGORIES` 之 `16` 項同序；唯 `"道路"` 為 `True`；緊接 `F3_CATEGORY_BURDEN` 之後 |
| `R-2` | `grep -n "if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)" app.py` | dict 推導式另立一 `if` 子句（⛔ 以 `and` 併入·`F18 W3` 逐子句查）；既有 `if _lr not in _buildable_blocks` 存；新列帶行尾註解 |
| `R-3` | `grep -n "^ADJ_DEPTH_TIE_TOL_M = 0.1" app.py` | 新段之首（`adj_intake_rows` 之後、`wg9248_stringify_mixed_cols` 之前）；段首之模組層註解含 `adj_intake`（五函式之外·`X-2` 依字面合） |
| `R-4` | `grep -n "^def adj_q2" app.py` | 式逐字；`Decimal`／`ROUND_HALF_UP` 於函式內 import（`F18` 以 AST 抽出於隔離之命名空間執行） |
| `R-5`（＋ 補令一 `R-5′`） | `grep -n "^def adj_block_ctx" app.py` | ① 識別符空者一次列出全部、分述二補法（`grep -n "填名無從補之" app.py`）；② 分區空 → 路寬 → 深度 → 最小建築面積（`grep -n "def _nonneg_q2" app.py`）；路寬、深度之「`≤ 0`」與最小建築面積之「`＜ 0`／非有限」皆以 `adj_q2` 之值判（附則乙）；非數 ⇒ `RuntimeError` |
| `R-6`（→ `R-6′` → `R-6″`） | `grep -n "^def adj_pool_anchor" app.py` | 見 `⑦-3` |
| `R-7`（＋ `R-7′` ①、`R-7″` ①） | `grep -n "^def adj_candidate_lists" app.py` | 錨點 `min((-原有面積, str(暫編地號)))`；點數 `＜ 3` → 坐標之檢 → `Polygon` → 無效者 `buffer(0)` → 為空 ⇒ 停機（訊息皆含歸戶與暫編地號）；距離 ＝ `adj_q2(math.hypot(迄點 − 質心))`（與 `F18` 之 `_independent` 同式同序）；八鍵逐項如原單；`r6` 之「同深／較淺／較深」於同一分支定之 |
| `R-8` | `grep -n "^def adj_candidate_rows" app.py` | 各值 `str`；`None` ⇒ `'—'`；`lines` 之句逐碼位同原單 |
| `R-9` | `grep -n "_adj359_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)" app.py` | `main()` 🧩 區塊之後、`# 🆕 W-G Y 波診斷專用` 之前；恰 `2` 句 ＋ 其上 `1` 行註解（`§三-4` 所許·AST 不變）；二 `st.markdown` 之標題句由 CC 定 |
| `R-10` | `grep -n "^def load_front_road_names" verify/run_verification.py` | `def main` 之後、`if __name__` 之前（`main` 以前之行號⛔ 移·`V-5` 證之）；值須非空白字串；`{}` 空真值過 |
| `R-11` | `verify/case_front_road_names_UC9898.json` | 塊 `J1` 二進位寫出 |
| `R-12` | — | `V-2`〜`V-5` 皆逐位同 |
| `R-13` | — | 新名唯見於定義處、`R-2`、`R-9` 與 `F18` |

### ⑦-2　補令一 `§二` 五款

| 款 | 落點（字樣錨） | 要點 |
|---|---|---|
| `R-6′` | （由 `R-6″` 代之） | 「`buffer(0)` 後為空者⛔ 計」→ 今為「面積以 `adj_q2` 計為 `0` 者⛔ 計」（涵空片） |
| `R-7′` ① | `adj_candidate_lists` 之 docstring：`grep -n "同抵費地之迄點·補令一 裁三" app.py` | 碼首輪已然；docstring 補其據 |
| `R-5′` ① | `grep -n "填名無從補之" app.py` | 見 `⑦-1` `R-5` |
| `R-5′` ② | `grep -n "def _nonneg_q2" app.py` | 見 `⑦-1` `R-5` |
| `X-3′` | ① `grep -n "中類別為「道路」者（" app.py`；② `grep -n "候選（非可建築土地之街廓中類別為「道路」者" app.py` | 二處皆唯註解／docstring；二函式之碼（AST 去 docstring）⛔ 動 |

### ⑦-3　補令二 `§二` 二款（＋ `X-8`）

| 款 | 落點（字樣錨） | 要點 |
|---|---|---|
| `R-6″` ① | `grep -n "先閱畢全部所取之列" app.py`；巢狀 `_coords_bad`：`grep -n "補令二 \`R-6″\` ①（與" app.py` | 所取之列 ＝ `推進側別 == ADJ_POOL_SIDE` 且 `cut_coords` 至少 `3` 點；**先**對全部所取之列施坐標之檢（首二元以 `float()` 轉之拋 `TypeError`／`ValueError`／`OverflowError`、或 `IndexError`／`KeyError`、或非有限）⇒ 有之則一次列出「街廓／暫編地號」（依列序）而停機；⛔ 建任何多邊形於其前 |
| `R-6″` ②③ | `grep -n "if adj_q2(_p.area) == 0:" app.py` | 其餘取多邊形（無效者 `buffer(0)`）；面積以 `adj_q2` 計為 `0` 者⛔ 計；面積最大者（全精度·並列取暫編地號小者）之質心；無餘者之街廓⛔ 入 |
| `R-7″` ① | 巢狀 `_coords_bad`：`grep -n "補令二 \`R-7″\` ①（與" app.py` | 錨點：點數 `＜ 3` 之後、`Polygon` 之前施同一式之檢 ⇒ 停機（訊息含歸戶與暫編地號） |
| `X-8` | — | 二檢唯於二函式之內（巢狀函式·二者 AST 同一）；模組層之名⛔ 增（`364`·差集 `∅`） |

🔒 字樣錨之唯一性（於 `e1b5b04`）：`先閱畢全部所取之列` `1`、`補令二 \`R-6″\` ①（與` `1`、`補令二 \`R-7″\` ①（與` `1`、`if adj_q2(_p.area) == 0:` `1`；寬字樣 `_coords_bad` ＝ `4`、`之坐標含非數值` ＝ `3` ⇒ 判別力非恆 `1`；對照（人造字樣）＝ `0`。

### ⑦-4　`§三-3`（`X-1`〜`X-7`）與 `X-8` 之自查、附則乙之自查

`X-1`（🧩 區塊一字未動）／`X-2`（五函式之全文含 docstring 對八字樣 `0` 命中·`F18 W4`）／`X-3`（`r3_*` 五函式、`R3_*`、`_line_block_overlap`、`_best_block` 之碼未動·唯 `X-3′` 之二處註解）／`X-4`（`wfns_ast` `48`／`48`／`47`）／`X-5`（`verify/` 唯 `run_verification.py` 純附加與新 json）／`X-6`（無案件字面；五函式內無 `0.1`／`0.5`）／`X-7`（`main` 唯 `R-9` 之 `2` 句）／`X-8`（無新模組層名）——**皆未觸**（第三輪 reviewer 逐項證之）。
附則乙：深度、路寬、最小建築面積、距離、池片之面積——其判、寫、比皆以 `adj_q2` 之值；錨點與池片之坐標之檢同一式（二巢狀函式 AST 同一）。

## ⑧　二檔之全文差異（`git diff 14a026b e1b5b04 -- app.py verify/run_verification.py`·`14a026b` 至 `51f082d` 之間生產碼⛔ 變 ⇒ 同 `51f082d..e1b5b04`·`27367` B·`421` 列·`sha256` `4c6c20046b790aaf0ba79613ba84bc6064994ce07afcf5881d503d6ae8a5f0d0`）

````diff
diff --git a/app.py b/app.py
index d893879..cae2523 100644
--- a/app.py
+++ b/app.py
@@ -1475,13 +1475,14 @@ def parse_cad_precision_layers(doc, classified_blocks: list, dxf_bytes) -> dict:
     result['front_lines_matched_count'] = len(result['front_lines'])
 
     # ── 🆕 `W-G.9-350`：正面道路之幾何推導（五級八鍵之 `r3`·KL 裁 `2026-09-05`）──────
-    #   候選 ＝ 非「可建築土地」之街廓（與上方 `_buildable_blocks` 同一判準之補集·⛔ 分區名字面）；
+    #   候選 ＝ 非「可建築土地」之街廓（與上方 `_buildable_blocks` 同一判準之補集·⛔ 分區名字面）中類別為「道路」者（`K-9-52` ①·`F3_CATEGORY_FRONT_ROAD`）；
     #   量測原語與容差 ＝ `_best_block` 所用之 `_line_block_overlap`（`W-G.9-235` 工項一之裁）。
     result['front_road_derive'] = r3_front_road_derive(
         _front_pts_chosen,
         {_lr: (_br.get('category', ''), _pr)
          for _lr, (_br, _pr, _cr, _fr_dir) in blk_polys.items()
-         if _lr not in _buildable_blocks})
+         if _lr not in _buildable_blocks
+         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})   # 🆕 `W-G.9-359`（`K-9-52` ①）：唯「道路」類
 
     # ── 🆕 W-G.5 C-6：SIDE_LINE 同判準綁定（街廓由重疊定·**側別仍由 FRONT p1→p2 導出**）──
     #
@@ -2461,6 +2462,27 @@ F3_CATEGORY_BURDEN = {
     "機關用地": "非共同負擔",
     "其他非共同負擔之公共設施用地": "非共同負擔",
 }
+# 🆕 `W-G.9-359`（`K-9-52` ①·KL 裁 `2026-09-29`）：得為**正面道路**（五級八鍵之 `r3`）之類別——唯「道路」。
+#   鍵 ＝ `F3_BLOCK_CATEGORIES` 之全部（同序）；正面線沿公園、廣場等非道路之公共設施街廓者，其推導為區外（或歧義），
+#   由使用者於步驟 E 之「正面道路名稱／識別符」欄填名。消費者 ＝ `parse_cad_precision_layers` 之正面道路推導之候選。
+F3_CATEGORY_FRONT_ROAD = {
+    "未分類": False,
+    "住宅區": False,
+    "商業區": False,
+    "道路": True,
+    "溝渠": False,
+    "兒童遊樂場": False,
+    "鄰里公園": False,
+    "廣場": False,
+    "綠地": False,
+    "國民小學": False,
+    "國民中學": False,
+    "停車場": False,
+    "零售市場": False,
+    "社會住宅": False,
+    "機關用地": False,
+    "其他非共同負擔之公共設施用地": False,
+}
 F3_CATEGORY_COLORS = {
     "未分類": "#BDBDBD",
     "住宅區": "#2E86C1", "商業區": "#8E44AD",
@@ -11275,7 +11297,7 @@ def r3_front_road_derive(front_pts_by_label, pool_by_label,
 
     `front_pts_by_label`  `{街廓 label: [(x, y), …]}`——各街廓所綁 FRONT_LINE 之**全部頂點**
                           （折線逐段計·⛔ 截為二端點）。
-    `pool_by_label`       `{街廓 label: (category, shapely Polygon)}`——候選（非可建築土地之街廓）。
+    `pool_by_label`       `{街廓 label: (category, shapely Polygon)}`——候選（非可建築土地之街廓中類別為「道路」者·`K-9-52` ①）。
     回傳 `{label: {'line_length_m', 'candidates', 'derived', 'status'}}`：
       `candidates` ＝ 重疊長 `> 0` 之候選，逐項 `{'block','category','overlap_m','ratio'}`，
                      依重疊長降冪、同長依 label 升冪（決定性）；
@@ -11669,6 +11691,276 @@ def adj_intake_rows(intake):
     return {'units': _u, 'step4': _s4, 'totals': _t, 'lines': _lines}
 
 
+# ── 🆕 `W-G.9-359`：調配之候選街廓名單（`docs/specs/調配階段_泛用規格_v1.md` 步 `3`·`v3` 五級③ 八鍵·`K-9-52`）──
+#   受詞 ＝ 調配之輸入盤點（`adj_intake`·`W-G.9-351`）之每一合併單位：建地軌 ＝ 自原街廓起、其餘可建築街廓依
+#   五級八鍵升序；公設軌 ＝ 全部可建築街廓依距離升序。
+#   🔒 純函式·⛔ 讀 session；一切外部量由參數注入（畫面 ＝ `main()` 成果區；harness ＝ 量測器 `F18`）。
+#   🔒 深度、深度差、路寬、最小建築面積、距離之判、寫、比，皆以 `adj_q2` 之值（四捨五入至 `0.01`）為之。
+#   🛑 本批**僅排序**：⛔ 消費端（任何配地、`G` 式、判定⛔ 讀名單·規格步 `4`〜`6` 另單）。
+#: `K-9-52` ③：深度相差此值以內（含）視為同深（以原街廓為準）；只用於候選街廓之先後，增配資格⛔ 設容差（`K-9-52` ④）。
+ADJ_DEPTH_TIE_TOL_M = 0.1
+
+
+def adj_q2(x):
+    """`W-G.9-359`：四捨五入至 `0.01`（`ROUND_HALF_UP`·以 `repr(float(x))` 之十進位字面起算）⇒ `Decimal`。
+
+    例：`0.125 ⇒ 0.13`、`2.675 ⇒ 2.68`、`1.005 ⇒ 1.01`、`-0.125 ⇒ -0.13`。
+    """
+    from decimal import Decimal, ROUND_HALF_UP
+    return Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
+
+
+def adj_block_ctx(labels, category_by, eff_min_build_by, ident_by, width_by, depth_by):
+    """`W-G.9-359`：候選街廓名單所需之街廓屬性（純函式）。參數皆 `{label: 值}`；`labels` ＝ 可建築街廓之 label。
+
+    回 `{label: {'使用分區', '最小建築面積', '正面道路', '正面路寬', '深度'}}`（後四者中之數量皆為 `adj_q2` 之值；
+    最小建築面積缺者 ＝ `0`〔無規定·`K-9-1` ⑨〕）。
+    停機（`RuntimeError`·⛔ 靜默略過）：
+      ① 正面道路之識別符為空（`None` 或空字串）者——**一次列出全部**（依 `labels` 之序），並分述二補法：圖推導為
+         區外或歧義者，於步驟 E 之「正面道路名稱／識別符」欄填名；無正面線（`FRONT_LINE`）者，須先於圖補其正面線
+         （`K-9-52` ⑤·通知三·`W-G.9-359` 補令一 `R-5′` ①）；
+      ② 其後逐街廓：使用分區為空；正面路寬缺、非數或 `≤ 0`；深度缺、非數或 `≤ 0`；最小建築面積非數、非有限或
+         `＜ 0`（缺者 ＝ `0`·補令一 `R-5′` ②）——皆以 `adj_q2` 之值判之。
+    """
+    _labels = list(labels or [])
+    _ident = ident_by or {}
+    _miss = [_l for _l in _labels if _ident.get(_l) is None or str(_ident.get(_l)) == '']
+    if _miss:
+        raise RuntimeError(
+            "🔴 [W-G.9-359 候選街廓名單] 下列街廓之正面道路無識別符：%s ⇒ 停機。"
+            "圖推導為區外或歧義者：請於步驟 E 該街廓之「正面道路名稱／識別符」欄填名（臨同一條道路者填相同名稱），"
+            "按「✅ 儲存路寬資料」後重跑；無正面線（FRONT_LINE）者：須先於圖補其正面線，填名無從補之。"
+            % '、'.join(str(_l) for _l in _miss))
+
+    def _pos_q2(_v, _what, _l):
+        if _v is None or (isinstance(_v, str) and _v.strip() == ''):
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 街廓 {_l!r} 之{_what}缺 ⇒ 停機")
+        try:
+            _q = adj_q2(_v)
+            _ok = _q.is_finite() and _q > 0
+        except (TypeError, ValueError, ArithmeticError):
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 街廓 {_l!r} 之{_what} {_v!r} 非數 ⇒ 停機")
+        if not _ok:
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 街廓 {_l!r} 之{_what} {_v!r}（{_q}）≤ 0 ⇒ 停機")
+        return _q
+
+    def _nonneg_q2(_v, _l):
+        # 補令一 `R-5′` ②：缺、`None` 或空白字串 ⇒ `0`（無規定）；非數、非有限或 `＜ 0` ⇒ 停機
+        if _v is None or (isinstance(_v, str) and _v.strip() == ''):
+            _v = 0
+        try:
+            _q = adj_q2(_v)
+            _ok = _q.is_finite() and _q >= 0
+        except (TypeError, ValueError, ArithmeticError):
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 街廓 {_l!r} 之最小建築面積 {_v!r} 非數 ⇒ 停機")
+        if not _ok:
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 街廓 {_l!r} 之最小建築面積 {_v!r}（{_q}）"
+                               "非有限或 ＜ 0 ⇒ 停機")
+        return _q
+
+    _eff = eff_min_build_by or {}
+    _out = {}
+    for _l in _labels:
+        _cat = (category_by or {}).get(_l)
+        if _cat is None or str(_cat) == '':
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 街廓 {_l!r} 無使用分區 ⇒ 停機")
+        _w = _pos_q2((width_by or {}).get(_l), '正面路寬', _l)
+        _d = _pos_q2((depth_by or {}).get(_l), '深度', _l)
+        _m = _nonneg_q2(_eff.get(_l), _l)
+        _out[_l] = {'使用分區': str(_cat), '最小建築面積': _m,
+                    '正面道路': str(_ident[_l]), '正面路寬': _w, '深度': _d}
+    return _out
+
+
+def adj_pool_anchor(g_rows):
+    """`W-G.9-359`：各街廓之距離迄點（KL 質心起迄法之迄點·純函式）。
+
+    逐 `所屬街廓`，於 `推進側別` ＝ `ADJ_POOL_SIDE` 且 `cut_coords` 至少 `3` 點之列（所取之列）中：
+      ① 坐標壞損（任一頂點之首二元以 `float()` 轉之拋 `TypeError`／`ValueError`／`OverflowError`、或缺、或非有限）
+         ⇒ 閱畢全部所取之列後停機，一次列出全部壞損之列之街廓與暫編地號（依列之序·資料之瑕·補令二 裁二）；
+      ② 其餘取多邊形（無效者 `buffer(0)`），**其面積以 `adj_q2` 計為 `0` 者⛔ 計**（池面積之定式為 `0.00 ㎡`·
+         無可容之地·含 `buffer(0)` 後為空者與非空之細縫·補令二 裁一）；
+      ③ 餘者中面積最大者（全精度·並列 ⇒ `str(暫編地號)` 字典序小者）之質心，回 `{街廓: (質心 x, 質心 y)}`（`float`）；
+         無餘者之街廓⛔ 入（視同無抵費地·⛔ 停機）。未滿 `3` 點之列⛔ 取、⛔ 檢、⛔ 列。
+    """
+    import math as _m
+    from shapely.geometry import Polygon
+
+    def _coords_bad(_cs):
+        # 補令二 `R-6″` ①（與 `adj_candidate_lists` 之錨點之坐標之檢同一式）
+        try:
+            return not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)
+        except (TypeError, ValueError, OverflowError, IndexError, KeyError):
+            return True
+
+    _taken = [_r for _r in g_rows or []
+              if _r.get('推進側別') == ADJ_POOL_SIDE and len(_r.get('cut_coords') or []) >= 3]
+    # ① 先閱畢全部所取之列（⛔ 建任何多邊形），壞損者一次列出
+    _bad = [f"{_r.get('所屬街廓')}／{_r.get('暫編地號')}" for _r in _taken if _coords_bad(_r.get('cut_coords'))]
+    if _bad:
+        raise RuntimeError("🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值（非數、無窮大或缺·資料之瑕·"
+                           "位置無從定）：%s ⇒ 停機" % '、'.join(_bad))
+    # ②③
+    _best = {}
+    for _r in _taken:
+        _p = Polygon(_r.get('cut_coords'))
+        if not _p.is_valid:
+            _p = _p.buffer(0)
+        if adj_q2(_p.area) == 0:
+            continue
+        _b = str(_r.get('所屬街廓'))
+        _k = (-float(_p.area), str(_r.get('暫編地號')))
+        if _b not in _best or _k < _best[_b][0]:
+            _best[_b] = (_k, _p)
+    _out = {}
+    for _b, (_k, _p) in _best.items():
+        _c = _p.centroid
+        _out[_b] = (float(_c.x), float(_c.y))
+    return _out
+
+
+def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPTH_TIE_TOL_M):
+    """`W-G.9-359`：調配之候選街廓名單（規格步 `3`·純函式·⛔ 讀 session）。
+
+    參數
+      intake        調配之輸入盤點（`W-G.9-351`）之回傳（取其 `units`）。
+      blk_ctx       `adj_block_ctx` 之回傳（其鍵 ＝ 全部可建築街廓）。
+      pool_anchor   `adj_pool_anchor` 之回傳。
+      slice_coords  `{暫編地號: polygon_coords}`。
+      tol           深度之同深容差（`K-9-52` ③）。
+    依 `intake['units']` 之序逐單位回 `{'歸戶', '軌', '原街廓', '錨點', '名單'}`：
+      錨點 ＝ 該單位之建築街廓內不能分配 ＋ 共同負擔用地之列中原有面積最大者（並列取暫編地號小者）；
+      距離 `d(T)` ＝ 錨點之多邊形（無效者 `buffer(0)`·同抵費地之迄點·補令一 裁三）之質心至 `pool_anchor[T]`
+      之直線距離（`adj_q2`）；無迄點者 ＝ `None`
+      （`r7` ＝ `(1, 0)`·排於同鍵者之後）。
+      建地軌：名單首 ＝ 原街廓（⛔ 排序）；其餘依八鍵 `(r1, r2, r3, r4, r5, r6, r7, 街廓)` 升序：
+        `r1` 使用分區同／異；`r2` 最小建築面積之級（相異值升序；往小 `(0, n)`、往大 `(1, n)`·往大者第二趟排除）；
+        `r3` 正面道路同／異；`r4` 正面路寬同／異；`r5` 路寬之級（相異值由寬而窄；往窄 `(0, n)`、往寬 `(1, n)`·
+        `K-9-52` ②）；`r6` 深度（`|Δ| ≤ tol` 同深 `(0, 0)`、較淺 `(0, −Δ)`、較深 `(1, Δ)`·`K-9-52` ③）；`r7` 距離。
+      公設軌：名單 ＝ 全部可建築街廓依 `(r7, 街廓)` 升序。
+    停機：單位無列；錨點無幾何（`slice_coords` 無至少 `3` 點或 `buffer(0)` 後為空·位置無從定·補令一 裁二）；
+      錨點之坐標含非數值（同 `adj_pool_anchor` 之坐標之檢·資料之瑕·補令二 裁二）；建地軌之原街廓非可建築街廓。
+    """
+    import math as _m
+    from decimal import Decimal
+    from shapely.geometry import Polygon
+
+    def _coords_bad(_cs):
+        # 補令二 `R-7″` ①（與 `adj_pool_anchor` 之池片之坐標之檢同一式）
+        try:
+            return not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)
+        except (TypeError, ValueError, OverflowError, IndexError, KeyError):
+            return True
+
+    _ctx = blk_ctx or {}
+    _pa = pool_anchor or {}
+    _sc = slice_coords or {}
+    _labels = list(_ctx)
+    _tolq = Decimal(repr(float(tol)))
+    _lad2 = sorted({_ctx[_t]['最小建築面積'] for _t in _labels})
+    _lad5 = sorted({_ctx[_t]['正面路寬'] for _t in _labels}, reverse=True)
+    _dash = '—'
+    _out = []
+    for _u in (intake or {}).get('units') or []:
+        _g, _track, _home = _u.get('歸戶'), _u.get('軌'), _u.get('原街廓')
+        _sl = list(_u.get('建築街廓內不能分配') or []) + list(_u.get('共同負擔用地') or [])
+        if not _sl:
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之合併單位無土地 ⇒ 停機")
+        _a = min(_sl, key=lambda _r: (-float(_r['原有面積']), str(_r['暫編地號'])))
+        _aid = str(_a['暫編地號'])
+        _cs = _sc.get(_aid) or []
+        if len(_cs) < 3:
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 無幾何（點數 {len(_cs)}）⇒ 停機")
+        if _coords_bad(_cs):
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之坐標含非數值"
+                               "（非數、無窮大或缺·資料之瑕·位置無從定）⇒ 停機")
+        _p = Polygon(_cs)
+        if not _p.is_valid:
+            _p = _p.buffer(0)
+        if _p.is_empty:
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之多邊形為空 ⇒ 停機")
+        _ax, _ay = float(_p.centroid.x), float(_p.centroid.y)
+        _dist = {_t: (adj_q2(_m.hypot(_pa[_t][0] - _ax, _pa[_t][1] - _ay)) if _t in _pa else None)
+                 for _t in _labels}
+        _r7 = {_t: ((0, _dist[_t]) if _dist[_t] is not None else (1, Decimal('0'))) for _t in _labels}
+        if _track == ADJ_TRACK_BUILD:
+            if _home not in _ctx:
+                raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之原街廓 {_home!r} 非可建築街廓 ⇒ 停機")
+            _s = _ctx[_home]
+            _i2 = _lad2.index(_s['最小建築面積'])
+            _i5 = _lad5.index(_s['正面路寬'])
+            _items = [{'街廓': _home, '原街廓': True, '鍵': None, '使用分區': _dash, '最小建築面積': _dash,
+                       '正面道路': _dash, '正面路寬': _dash, '路寬級距': _dash, '深度差': None, '深度': _dash,
+                       '距離': _dist[_home], '第二趟排除': False}]
+            _rest = []
+            for _t in _labels:
+                if _t == _home:
+                    continue
+                _c = _ctx[_t]
+                _r1 = 0 if _c['使用分區'] == _s['使用分區'] else 1
+                _j2 = _lad2.index(_c['最小建築面積'])
+                _r2 = (0, _i2 - _j2) if _j2 <= _i2 else (1, _j2 - _i2)
+                _r3 = 0 if _c['正面道路'] == _s['正面道路'] else 1
+                _r4 = 0 if _c['正面路寬'] == _s['正面路寬'] else 1
+                _j5 = _lad5.index(_c['正面路寬'])
+                _r5 = (0, _j5 - _i5) if _j5 >= _i5 else (1, _i5 - _j5)
+                _dd = _c['深度'] - _s['深度']
+                if abs(_dd) <= _tolq:
+                    _r6, _dlab = (0, Decimal('0')), '同深'
+                elif _dd < 0:
+                    _r6, _dlab = (0, -_dd), '較淺'
+                else:
+                    _r6, _dlab = (1, _dd), '較深'
+                _rest.append({
+                    '街廓': _t, '原街廓': False, '鍵': (_r1, _r2, _r3, _r4, _r5, _r6, _r7[_t], _t),
+                    '使用分區': '同' if _r1 == 0 else '異',
+                    '最小建築面積': ('同級' if _r2 == (0, 0)
+                                     else ('往小 %d 級' if _r2[0] == 0 else '往大 %d 級') % _r2[1]),
+                    '正面道路': '同' if _r3 == 0 else '異',
+                    '正面路寬': '同' if _r4 == 0 else '異',
+                    '路寬級距': ('同級' if _r5 == (0, 0)
+                                 else ('往窄 %d 級' if _r5[0] == 0 else '往寬 %d 級') % _r5[1]),
+                    '深度差': _dd, '深度': _dlab, '距離': _dist[_t], '第二趟排除': _r2[0] == 1})
+            _rest.sort(key=lambda _x: _x['鍵'])
+            _items += _rest
+        else:
+            _items = sorted(({'街廓': _t, '原街廓': False, '鍵': (_r7[_t], _t), '使用分區': _dash,
+                              '最小建築面積': _dash, '正面道路': _dash, '正面路寬': _dash, '路寬級距': _dash,
+                              '深度差': None, '深度': _dash, '距離': _dist[_t], '第二趟排除': False}
+                             for _t in _labels), key=lambda _x: _x['鍵'])
+        _out.append({'歸戶': _g, '軌': _track, '原街廓': _home, '錨點': _aid,
+                     '名單': [{'序': _n, **_it} for _n, _it in enumerate(_items, 1)]})
+    return _out
+
+
+def adj_candidate_rows(cand, tol=ADJ_DEPTH_TIE_TOL_M):
+    """`W-G.9-359`：候選街廓名單之顯示列（純函式·各欄皆字串·⛔ 混型欄）。回 `{'lines', 'units', 'detail'}`。"""
+    def _f2(_v):
+        return '—' if _v is None else f"{float(_v):.2f}"
+
+    _units, _detail = [], []
+    for _u in cand or []:
+        _seq = []
+        for _it in _u['名單']:
+            _seq.append(str(_it['街廓']) + ('（原街廓）' if _it['原街廓'] else '')
+                        + ('（第二趟排除）' if _it['第二趟排除'] else ''))
+        _units.append({'歸戶': str(_u['歸戶']), '軌': str(_u['軌']),
+                       '原街廓': '—' if _u['原街廓'] is None else str(_u['原街廓']),
+                       '錨點（重劃前面積最大之一筆）': str(_u['錨點']),
+                       '候選街廓（依序）': ' → '.join(_seq)})
+        for _it in _u['名單']:
+            _detail.append({'歸戶': str(_u['歸戶']), '序': str(_it['序']), '街廓': str(_it['街廓']),
+                            '使用分區': str(_it['使用分區']), '最小建築面積': str(_it['最小建築面積']),
+                            '正面道路': str(_it['正面道路']), '正面路寬': str(_it['正面路寬']),
+                            '路寬級距': str(_it['路寬級距']), '深度': str(_it['深度']),
+                            '深度差(m)': _f2(_it['深度差']), '距離(m)': _f2(_it['距離'])})
+    _n = len(cand or [])
+    _nb = sum(1 for _u in cand or [] if _u['軌'] == ADJ_TRACK_BUILD)
+    _lines = [f"合併單位 {_n}（{ADJ_TRACK_BUILD} {_nb}·{ADJ_TRACK_PUBLIC} {_n - _nb}）；"
+              f"深度相差 {float(tol):.2f} m 以內視為同深（以原街廓為準）"]
+    return {'lines': _lines, 'units': _units, 'detail': _detail}
+
+
 def wg9248_stringify_mixed_cols(df, cols):
     """把指定欄轉為 `str`，以避 `pyarrow.lib.ArrowInvalid`（混型欄之 Arrow 轉換紅）。
 
@@ -26117,6 +26409,54 @@ def main():
                                 st.dataframe(_pd.DataFrame(_adj351_view['totals']),
                                              use_container_width=True, hide_index=True)
 
+                    # 🆕 `W-G.9-359`：調配之候選街廓名單（規格步 3·五級八鍵·`K-9-52`）——僅排序·⛔ 調配、⛔ 消費端
+                    _adj359_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)
+                    if _adj359_bf is not None:
+                        with st.expander("🧭 調配之候選街廓名單（五級八鍵·僅排序·尚未調配）", expanded=False):
+                            try:
+                                _adj359_s3 = k6b_stage3_selected(st.session_state, build_parcels,
+                                                                 st.session_state.get('f3L_setback_default'))
+                                _adj359_temp = temp_parcels if _adj359_s3 is None else _adj359_s3[0]
+                                _adj359_intake = adj_intake(
+                                    _adj359_temp, _adj359_bf,
+                                    st.session_state.get('f3_G_values') or [],
+                                    st.session_state.get(SS_ADJ_DROPPED) or {},
+                                    st.session_state.get('t8_ownership_map', {}) or {},
+                                    {b['label']: F3_CATEGORY_BURDEN.get(b.get('category', ''), '')
+                                     for b in classified_blocks})
+                                _adj359_bb = [b for b in classified_blocks
+                                              if F3_CATEGORY_BURDEN.get(b.get('category', ''), '') == ADJ_BURDEN_BUILD]
+                                _adj359_lbls = [b['label'] for b in _adj359_bb]
+                                _adj359_names = st.session_state.get(SS_FRONT_ROAD_NAME, {}) or {}
+                                _adj359_ident = r3_front_road_identifier(
+                                    _adj359_lbls, st.session_state.get(SS_FRONT_ROAD_DERIVE, {}) or {},
+                                    {b['label']: _adj359_names.get(b['id'], '') for b in _adj359_bb})
+                                _adj359_sb = {str(_r.get('街廓')): _r for _r in (st.session_state.get('f3_sb_rows') or [])}
+                                _adj359_ctx = adj_block_ctx(
+                                    _adj359_lbls, {b['label']: b.get('category', '') for b in _adj359_bb},
+                                    st.session_state.get(K91_SS_MBA_EFFECTIVE, {}) or {},
+                                    {_l: _adj359_ident[_l]['id'] for _l in _adj359_lbls},
+                                    {_l: (_adj359_sb.get(_l) or {}).get('正面路寬(m)') for _l in _adj359_lbls},
+                                    st.session_state.get('f3_alloc_depth_by_label', {}) or {})
+                                _adj359_view = adj_candidate_rows(adj_candidate_lists(
+                                    _adj359_intake, _adj359_ctx,
+                                    adj_pool_anchor(st.session_state.get('f3_G_values') or []),
+                                    {str(t['暫編地號']): (t.get('polygon_coords') or []) for t in _adj359_temp}))
+                            except RuntimeError as _e_adj359:
+                                st.error(str(_e_adj359))
+                                _adj359_view = None
+                            if _adj359_view is not None:
+                                for _adj359_line in _adj359_view['lines']:
+                                    st.caption(_adj359_line)
+                                st.markdown("###### 各合併單位之候選街廓（建地軌：原街廓居首，其餘依五級八鍵；"
+                                            "公設軌：全部可建築街廓依距離）")
+                                st.dataframe(_pd.DataFrame(_adj359_view['units']),
+                                             use_container_width=True, hide_index=True)
+                                st.markdown("###### 逐候選之八鍵說明（對原街廓：使用分區／最小建築面積之級／正面道路／"
+                                            "正面路寬／路寬級距／深度；距離 ＝ 錨點至該街廓最大抵費地之質心）")
+                                st.dataframe(_pd.DataFrame(_adj359_view['detail']),
+                                             use_container_width=True, hide_index=True)
+
                     # 🆕 W-G Y 波診斷專用（KL 2026-07-14 交辦·非產品功能）：
                     # live g_rows JSON dump 供 sub-cent 定位。
                     # 純加·輸出 st.session_state['f3_G_values'] 原始物件（全精度、未捨入、
diff --git a/verify/run_verification.py b/verify/run_verification.py
index 4d83d2c..3bd2b37 100644
--- a/verify/run_verification.py
+++ b/verify/run_verification.py
@@ -1529,5 +1529,26 @@ def main():
     return 0 if allok else 1
 
 
+# 🆕 `W-G.9-359`（`K-9-52` ⑤·通知二）：驗證路徑（無畫面）之區外道路名稱——畫面由使用者於步驟 E 之
+#   「正面道路名稱／識別符」欄填之；本檔只供 harness 比對「是否同一條道路」（既有之案件參數檔⛔ 動）。
+#   🔒 置於 `def main` 之後：本檔 `main` 以前之行號⛔ 移（`run_all` 之出艙含本檔之 traceback 行號）。
+#   本批之消費者唯量測器 `F18`（`verify/probes/probe_WG9359_cand.py`）。
+FRONT_ROAD_NAMES = os.path.join(HERE, "case_front_road_names_UC9898.json")
+
+
+def load_front_road_names():
+    """讀 `FRONT_ROAD_NAMES`（UTF-8），回 `dict(該檔之 'names')`（`{街廓 label: 區外道路名稱}`）。
+
+    `names` 非 `{str: 非空 str}` ⇒ `RuntimeError`（⛔ 靜默回空）；檔缺或 JSON 壞 ⇒ 原例外照拋。
+    """
+    with open(FRONT_ROAD_NAMES, encoding="utf-8") as f:
+        data = json.load(f)
+    names = data.get("names") if isinstance(data, dict) else None
+    if not isinstance(names, dict) or not all(
+            isinstance(k, str) and isinstance(v, str) and v.strip() != "" for k, v in names.items()):
+        raise RuntimeError(f"🔴 {FRONT_ROAD_NAMES} 之 names 非 {{str: 非空 str}}：{names!r} ⇒ 停機")
+    return dict(names)
+
+
 if __name__ == "__main__":
     sys.exit(main())
````

## ⑨　各段耗時（本機時刻·`2026-09-30`）

| 段 | 首輪 | 補令一 | 補令二 |
|---|---|---|---|
| 讀單與開場 | `05:42`–`05:45`（`3` 分） | `08:40`–`08:42`（`2` 分） | `11:04`–`11:06`（`2` 分） |
| 工項零／一 | `05:45`–`05:46` | `08:42` | `11:06` |
| 前置 | `05:46`–`06:10`（`run_all` 含重跑 `18` 分·並行） | `08:42`–`08:44`（沿用） | `11:06`–`11:07`（沿用） |
| 撰碼 | `05:51`–`06:01`（`10` 分） | `08:43`–`08:45`（`3` 分） | `11:07`–`11:08`；兩段之修 `11:20`–`11:23` |
| 驗 | `06:01`–`06:42`（並行） | `08:45`–`09:13`（並行） | `11:08`–`11:19`（初稿·捨）；`11:23`–`11:53`（並行） |
| 審查 | `06:13`–`06:34` | `08:46`–`08:58` | `11:09`–`11:20`；覆核 `11:25`–`11:27` |
| 停機報告 | `06:34`–`06:50` | `08:58`–`09:18` | — |
| 登記（工項三） | — | — | `11:53` |
| 報告（工項四） | — | — | `11:54`– |

## ⑩　`V-8′` 之差異全文（`git diff 3edca01 e1b5b04 -- app.py verify/run_verification.py`·`5202` B·`85` 列·`sha256` `2d93fa01999696936276e4d69f195d1a8bd02a4d0194c3edf40cdb06a8ea525a`）

````diff
diff --git a/app.py b/app.py
index 6e6d7e3..cae2523 100644
--- a/app.py
+++ b/app.py
@@ -11775,22 +11775,38 @@ def adj_block_ctx(labels, category_by, eff_min_build_by, ident_by, width_by, dep
 def adj_pool_anchor(g_rows):
     """`W-G.9-359`：各街廓之距離迄點（KL 質心起迄法之迄點·純函式）。
 
-    逐 `所屬街廓`，於 `推進側別` ＝ `ADJ_POOL_SIDE` 且 `cut_coords` 至少 `3` 點之列中，取多邊形（無效者 `buffer(0)`），
-    **其為空者⛔ 計**（退化之片·無可容之地·補令一 裁一）；餘者中面積最大者（並列 ⇒ `str(暫編地號)` 字典序小者）之質心，
-    回 `{街廓: (質心 x, 質心 y)}`（`float`）；無餘者之街廓⛔ 入（視同無抵費地·⛔ 停機）。
+    逐 `所屬街廓`，於 `推進側別` ＝ `ADJ_POOL_SIDE` 且 `cut_coords` 至少 `3` 點之列（所取之列）中：
+      ① 坐標壞損（任一頂點之首二元以 `float()` 轉之拋 `TypeError`／`ValueError`／`OverflowError`、或缺、或非有限）
+         ⇒ 閱畢全部所取之列後停機，一次列出全部壞損之列之街廓與暫編地號（依列之序·資料之瑕·補令二 裁二）；
+      ② 其餘取多邊形（無效者 `buffer(0)`），**其面積以 `adj_q2` 計為 `0` 者⛔ 計**（池面積之定式為 `0.00 ㎡`·
+         無可容之地·含 `buffer(0)` 後為空者與非空之細縫·補令二 裁一）；
+      ③ 餘者中面積最大者（全精度·並列 ⇒ `str(暫編地號)` 字典序小者）之質心，回 `{街廓: (質心 x, 質心 y)}`（`float`）；
+         無餘者之街廓⛔ 入（視同無抵費地·⛔ 停機）。未滿 `3` 點之列⛔ 取、⛔ 檢、⛔ 列。
     """
+    import math as _m
     from shapely.geometry import Polygon
+
+    def _coords_bad(_cs):
+        # 補令二 `R-6″` ①（與 `adj_candidate_lists` 之錨點之坐標之檢同一式）
+        try:
+            return not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)
+        except (TypeError, ValueError, OverflowError, IndexError, KeyError):
+            return True
+
+    _taken = [_r for _r in g_rows or []
+              if _r.get('推進側別') == ADJ_POOL_SIDE and len(_r.get('cut_coords') or []) >= 3]
+    # ① 先閱畢全部所取之列（⛔ 建任何多邊形），壞損者一次列出
+    _bad = [f"{_r.get('所屬街廓')}／{_r.get('暫編地號')}" for _r in _taken if _coords_bad(_r.get('cut_coords'))]
+    if _bad:
+        raise RuntimeError("🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值（非數、無窮大或缺·資料之瑕·"
+                           "位置無從定）：%s ⇒ 停機" % '、'.join(_bad))
+    # ②③
     _best = {}
-    for _r in g_rows or []:
-        if _r.get('推進側別') != ADJ_POOL_SIDE:
-            continue
-        _cs = _r.get('cut_coords') or []
-        if len(_cs) < 3:
-            continue
-        _p = Polygon(_cs)
+    for _r in _taken:
+        _p = Polygon(_r.get('cut_coords'))
         if not _p.is_valid:
             _p = _p.buffer(0)
-        if _p.is_empty:
+        if adj_q2(_p.area) == 0:
             continue
         _b = str(_r.get('所屬街廓'))
         _k = (-float(_p.area), str(_r.get('暫編地號')))
@@ -11823,11 +11839,19 @@ def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPT
         `K-9-52` ②）；`r6` 深度（`|Δ| ≤ tol` 同深 `(0, 0)`、較淺 `(0, −Δ)`、較深 `(1, Δ)`·`K-9-52` ③）；`r7` 距離。
       公設軌：名單 ＝ 全部可建築街廓依 `(r7, 街廓)` 升序。
     停機：單位無列；錨點無幾何（`slice_coords` 無至少 `3` 點或 `buffer(0)` 後為空·位置無從定·補令一 裁二）；
-      建地軌之原街廓非可建築街廓。
+      錨點之坐標含非數值（同 `adj_pool_anchor` 之坐標之檢·資料之瑕·補令二 裁二）；建地軌之原街廓非可建築街廓。
     """
     import math as _m
     from decimal import Decimal
     from shapely.geometry import Polygon
+
+    def _coords_bad(_cs):
+        # 補令二 `R-7″` ①（與 `adj_pool_anchor` 之池片之坐標之檢同一式）
+        try:
+            return not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)
+        except (TypeError, ValueError, OverflowError, IndexError, KeyError):
+            return True
+
     _ctx = blk_ctx or {}
     _pa = pool_anchor or {}
     _sc = slice_coords or {}
@@ -11847,6 +11871,9 @@ def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPT
         _cs = _sc.get(_aid) or []
         if len(_cs) < 3:
             raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 無幾何（點數 {len(_cs)}）⇒ 停機")
+        if _coords_bad(_cs):
+            raise RuntimeError(f"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之坐標含非數值"
+                               "（非數、無窮大或缺·資料之瑕·位置無從定）⇒ 停機")
         _p = Polygon(_cs)
         if not _p.is_valid:
             _p = _p.buffer(0)
````

補令一之 `V-8`（`78c1c6f..3edca01`）＝ `docs/reports/W-G.9-359R_補令一_工項二_對首輪增量.diff`。

## ⑪　停機報告一 `§十一` 三項與 `§四` `F-3`／`F-4`／`N-4` 於本批之處置（對回補令一 `§一`）

| 項 | 補令一之裁 | 本批之處置 |
|---|---|---|
| `§十一` `1`（`F-1`·`R-6`） | 裁一：讀法乙（空片⛔ 計·無餘者視同無抵費地） | 施於 `3edca01`；**其後由補令二 裁一代之**（面積以 `adj_q2` 計為 `0` 者⛔ 計·涵空片）⇒ 終態 `e1b5b04` |
| `§十一` `1`（`F-1`·`R-7`） | 裁二：讀法甲（錨點退化 ⇒ 停機） | 碼首輪已然；終態保留 |
| `§十一` `2`（`F-2`） | 裁三：錨點無效者 `buffer(0)` | 碼首輪已然；docstring 補其據 |
| `§十一` `3`（`N-6`） | 裁四：⛔ 呈 KL；`K5′` 讀法 `6` 明其射程 | `K5′` 由 `K5″` 代之（讀法 `6` 同文）⇒ 已入典（工項三） |
| `F-3` | 裁五：准改措辭（`R-5′` ①） | 已施 |
| `F-4` | 裁五：准加檢（`R-5′` ②） | 已施 |
| `N-4` | 裁五：准更二處陳舊之註解（`X-3′`） | 已施 |

## ⑫　停機報告二 `§十一` 二項與 `§四` `N-1`〜`N-4` 於本批之處置（對回補令二 `§一`）

| 項 | 補令二之裁 | 本批之處置 |
|---|---|---|
| `§十一` `1`（`B-1`） | 裁一：讀法乙·門檻 ＝ 池面積之既裁定式（`adj_q2` 為 `0` 者⛔ 計） | 施（`R-6″` ②）；`C23` ✅（`0.0046 ㎡` 之細縫⛔ 計、恰 `0.005 ㎡` 者計） |
| `§十一` `2`（`B-2`） | 裁二：讀法乙（坐標含非數值 ⇒ 停機並列出之） | 施（`R-6″` ①、`R-7″` ①）；`C24`〜`C26` ✅；依第三輪審查發現 1 改為兩段 |
| 續辦（驗之沿用） | 裁三：碼變 ⇒ 驗全數重跑；前置准沿用 | 照辦（`③`）；補令一之驗移存 `<O>\r2\` |
| `N-1`〜`N-4` | 裁四：記之、⛔ 改（`N-4` 之坐標一形由裁二收之） | 記之；第三輪審查另載：`N-4` 之「坐標格式錯之 `Polygon` 例外」一形（混維之環）⛔ 為坐標之檢所涵（`⑥-1` 之 `3` 之對照）——記之 |
