# `W-G.9-328`　中量單：`W-G.9-309` 之入主線（凍存分支 `c2`／`c2b` 以合併 `commit` 併入）＋ KL 畫面輸出二檔與呈文附圖入倉 ＋ `GB-174` 之立 ＋ `自誤 480`〜`484`

> **級** ＝ **中**（生產碼入主線：以合併 `commit` 併入已驗之 `c2`／`c2b`·⛔ 新寫生產碼一字·閘器重跑一次·⛔ 跑 `run_verification`·⛔ 寫 `verify/baselines`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `c34d36a1c6b437d7698abf267b1c5bb8527b4332`；**凍存** `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`（⛔ 動）。**受詞** ＝ CC 施工窗（新窗須先讀畢本單全文與 `docs/reports/W-G.9-309R_執行報告.md`）。
> **KL 之放行** ＝ `2026-09-22` 逐字「是」（`§二`）——本單之合併 `commit` 即其受詞；⛔ 再問 KL。
> 🔑 一切呼叫形之直譯器名寫 `python`；**一切路徑參數以 `os.path.abspath` 所得之形傳入**（`自誤 479`）。🩸 發單側窗二十三以相對路徑 `.` 傳受驗樹 ⇒ 受驗四格皆 `rc 1`（`K-9-5-4②` 之 loud raise）；本單之期值皆以絕對路徑實得。
> 🛑 **⛔ 以 shell 命令列傳遞含反引號之文字**（`恆常附款 h`）——payload 一律以**檔案管線**、依**圍欄之逐列索引**機械抽取；`commit` 訊息一律 `-F`。
> 🛑 **本單⛔ 及於**：`GB-174` 之修；`GB-136`／`167`／`168`／`169`／`171`／`172`／`173` 之任何修；`K-9-29` 之任何子項；`K-9-33 ⑤` 之接線；`GB-170` 之解除（候發單側）；凍存分支之改寫（⛔ rebase、⛔ 刪除、⛔ 強推）；本機 Streamlit 之升級。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　取號・停機款・pre-flight

### `§零-1`　取號現查（`e`／`e②`／`e③`／`z`／`aa`）

母體 ＝ 開工態全倉追蹤 **`2635`** 檔；內文側 ＝ 其中 `*.md`＋`*.py` **`1329`** 檔（`git ls-files`·`utf-8`·`errors='ignore'`）。框式（**可原樣執行**·`l⑥`·逐列 `re.search`；子字串框 ＝ `re.findall` 於全文）：單號 ＝ ``W-G\.9-N(?![0-9])``；自誤號 ＝ ``自誤[\s　`]*`?N(?![0-9])``；`GB` 號 ＝ ``GB-N(?![0-9])``；檔名側 ＝ 同式施於路徑字串。

| 受詞 | 檔名側 | 檔框 | 列框 | 子字串框 | 判 |
|---|---|---|---|---|---|
| `W-G.9-328`（本單之號） | `0` | `0` | `0` | `0` | 🟢 **可取** |
| `GB-174` | `0` | `0` | `0` | `0` | 🟢 **可取** |
| `自誤 480`／`481`／`482`／`483`／`484` | 各 `0` | 各 `0` | 各 `0` | 各 `0` | 🟢 **可取** |
| 對照甲［必命中·同形族］`W-G.9-325`／`GB-173`／`自誤 479` | `3`／`0`／`0` | `11`／`4`／`3` | `43`／`18`／`6` | `48`／`18`／`6` | 🟢 框非恆空 |
| 對照乙［必為零］`W-G.9-331`／`GB-179`／`自誤 489` | `0` | `0` | `0` | `0` | 🟢 ⛔ 占用 |

**對照乙之定義域**（`z`）：路徑以 `docs/orders/W-G.9-N` 起首之號（`re.match`）＝ **`123`** 個·`MAX` **`325`**·⛔ 含 `331`；`GB` 簿之號 `MAX` **`173`**（正典器）·⛔ 含 `179`；自誤 `MAX` **`479`**（正典器）·⛔ 含 `489`。
🩸 **`W-G.9-326`／`327`／`329` ⛔ 取**：三者之內文非零（前批所引之對照乙·`W-G.9-323`〜`325` 之單與報告），`328` 為 `MAX` 之上第一個四框皆零之號。

### `§零-2`　停機款（三值·`n`）

| # | 款 | 初態 |
|---|---|---|
| `1` | 開工前或 `push` 前以 `git ls-remote` 實查：主線 ≠ `c34d36a…`，或凍存分支 ≠ `488c485…`（⛔ rebase·⛔ 逕併） | 🛑 未執行 |
| `2` | 合併有衝突；或合併後 `app.py` blob ≠ `b4288438b6b029f4799a79fffacde1e7722c369f`、`verify/stepg_pipeline.py` ≠ `e4bd912b4f9e8cfe7cc49aef66f41ed566020937`、`verify/wf_f1.py` ≠ `23a2e919f0bdd3907d56a1ac9662e89aeee50584`、`verify/wf_f4.py` ≠ `df366b588800cb3fb17f31fac250aca72cf17ed4`；或生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`）相對開工態之相異 ≠ 恰 `app.py` ⋀ `verify/stepg_pipeline.py` | 🛑 未執行 |
| `3` | `git diff --numstat <合併>^1 <合併>` ≠ `git diff --numstat 7eddd91 488c485`（期 ＝ `app.py` `73`/`16`·`verify/stepg_pipeline.py` `24`/`7`） | 🛑 未執行 |
| `4` | 閘器（基座 `2f46579` 對合併樹）`rc ≠ 0`，或其出艙除首二列外 ≠ 倉內 `verify/out/WG9309_gates.md` 除首二列 | 🛑 未執行 |
| `5` | KL 二檔之來源 `sha256`／bytes 與 `§五-1` 不符；或入倉後 `git cat-file blob` 之 bytes ≠ 來源 bytes | 🛑 未執行 |
| `6` | 任一 payload（`P1`〜`P4`）之 bytes 或 `sha256` 與 `§五-1` 不符 | 🛑 未執行 |
| `7` | 本單於主 checkout 與 worktree 之二份⛔ 逐位相同 | 🛑 未執行 |
| `8` | 本批合併 `commit` 以外之任一 `commit` 之刪除欄非逐檔 `0` | 🛑 未執行 |
| `9` | `§四` 收工閘任一非 🟢 | 🛑 未執行 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或觸及 `GB-174` 之修 | 🛑 未執行 |

### `§零-3`　pre-flight 機檢之逐項處置（`W-G.9-190R §九（甲）`·⛔ 靜默略過）

| 項 | 性質 | 實得 | 處置 |
|---|---|---|---|
| `P-3`／`P-5` | **機械可判·停機款** | 紅 **`0`** 項；`P-5` ✅ 相符（受詞 **`51997`** B） | 🟢 通過 |
| `P-1`／`P-2`／`P-4`／`P-6` | 文字啟發式·⛔ 停機款 | **`6`** 項（`P-2` `1`／`P-4` `3`／`P-6` `2`）；逐項處置：`P-2` `:86` 之「`4` 筆」其框即同列所列舉之 `d1`〜`d4`；`P-4` `:112`／`:123`／`:225` 係「→」與「⛔ 增刪」之字面，⛔ 涉方向之轉引（後二者在塊 `P1`／`P4` 內）；`P-6` `:129`／`:202` 所繫之數於同節具名出處（`numstat` ＝ `git diff 7eddd91 488c485`；清單 ＝ 塊 `P1`） | ⚪ 不生 |

受單側收單時須自倉重跑本器並逐項再處置；`rc ≠ 0` ⇒ **停機回報**。

---

## `§一`　態錨（逐字嵌入·受單側須逐格自倉重跑·`w②①`）

呼叫形（`w②③`）：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 之絕對路徑> <outfile 之絕對路徑> 479 468`。「列」＝ `split('\n')` 之長度（`w②⑤`）。

| # | 項 | 值（錨於 `c34d36a`·發單側窗二十三自倉實跑·`2026-09-22`） |
|---|---|---|
| `1` | 主線 | `c34d36a1c6b437d7698abf267b1c5bb8527b4332`（`c34d36a → 7eddd91 → 2f46579`） |
| `2` | 凍存 | `488c4858da63ebe370ed950788947aa742eb44ad`（`488c485 → 86a1680 → 7eddd91`）；`git rev-list --left-right --count 7eddd91...488c485` ＝ `0 2`；主線對凍存 ＝ `1 2` |
| `3` | 生產碼（開工態） | **`34`**（頂層 `33` ＋ `app.py`）；`app.py` blob ＝ `8466f7493082bf84aa4f02d6c1c6e55ff746fc4a`；`verify/stepg_pipeline.py` ＝ `866dd3cb3dc2ca7cd4b950c11cd40e8bf15ba97b` |
| `3′` | 生產碼（凍存） | `app.py` ＝ `b4288438b6b029f4799a79fffacde1e7722c369f`；`verify/stepg_pipeline.py` ＝ `e4bd912b4f9e8cfe7cc49aef66f41ed566020937`；`86a1680` 之 `app.py` ＝ `5ceddfce896d106c8bc3c5a66ce7e236ab0a104d` |
| `3″` | 子層 `*.py` | **`385`**（`git ls-files 'verify/*.py'` 全 `418` − 頂層 `33`） |
| `4` | 正典框（正典器 `probe_WG9270_closegate.py`） | 自誤 **`469`**／**`479`**（缺 `[106,355,356,357]`）｜`GB` `171`／`173`（缺 `[12,87]`）｜`VR` `80`／`95`（缺 `[73,75]`）｜`K-9` `42`／`43`（缺 `[]`） |
| `4′` | 自擬框（`probe_WG9267_issuer_measurers.py`） | 自誤 **`465`**／**`479`**（缺另含 `434`〜`437`）｜`GB` `171`／`173`｜`VR` `80`／`95`｜`K-9` `42`／`43` |
| `5` | `baselines` | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·`298` 列 |
| `6` | refs | 遠端 **`26`**（`verify/` `21`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `7` | 五簿／典 | 自誤簿 `c6be0c2fe4ed1259ff8ff9372a03cb689e0ff753`·`1001228` B·`11163` 列｜恆常附款簿 `c790fbc16c06efd3ac88195850cfcbef47c58dc4`·`59311` B·`554` 列｜`GB` 簿 `4e99cc2138b8dc651ef19c3df37b03efde7d0f1d`·`950471` B·`8438` 列｜`K-6` 典 `8937375840601f90c8d3ad57fdbb5fdc2cb9da07`·`371944` B·`4587` 列｜`VR` 簿 `7cff9a3790641ee5f97c367a960aeec5efd3f1cd`·`394392` B·`5124` 列 |
| `8` | 母體 | 全倉 **`2635`**｜`.md` **`906`**｜`docs/` **`864`**｜`verify/out/` **`1026`** |
| `9` | 恆常附款 | 相異款號 **`28`**·表列式款列命中 **`37`** |
| `10` | 收工閘（開工態） | `python verify/probes/probe_WG9270_closegate.py 479 468 .` ⇒ `rc 0` |

---

## `§二`　KL 之放行（逐字）與射程

**發單側所呈**（窗二十三·`2026-09-22`·附平面圖）之【要你判斷】逐字：「是否放行：將測試版本之上述修改併入正式版本（通知二之修正另單辦理）？（是／否）」。**KL 逐字所答 ＝「是」。**
呈文之【現況】【要改成】【對土地的影響】（逐態並列）、通知二、射程與**逐筆放行清單**（`恆常附款 y`），逐字載於塊 `P1` 之 `(1)`——⛔ 於此重述。放行之受詞以該呈文之平面圖與逐宗數為準。
🩸 該呈文未載逐筆放行清單（`自誤 484`）；清單補載於塊 `P1`，其所列改動生產碼之 `commit` 恰為 `86a1680`／`488c485`／本單之合併 `commit`，與呈文所述之修改同一（停機款 `3` 保之）。

---

## `§三`　工項（依序·`commit` 共 `4` 筆：`d1`〜`d4`）

### 工項零　本單原封入倉（`d1`·⛔ 零生產碼）

`docs/orders/W-G.9-328_中量單.md`（**新檔**）。KL 置本單於主 checkout；CC 二進位複製入 worktree 並逐位對拍（停機款 `7`）；`SELF_SHA256` 依 `P-5` 原口徑自驗。開工前先行停機款 `1` 之實查。

### 工項一　合併（`d2`·🔴 生產碼·KL 放行之受詞）

1. `git fetch origin verify/W-G.9-299-gb170`；確認其 tip ＝ `488c485…`（停機款 `1`）。
2. 抽塊 `P4` 為倉外之訊息檔，行 `git merge --no-ff -F <該檔之絕對路徑> origin/verify/W-G.9-299-gb170`。
3. **推送前**機檢（停機款 `2`／`3`）：四 blob、生產碼 `34` 檔相異集、`numstat` 對拍——逐項出艙實得值。
🔒 發單側已於拋棄式分支實行本工項（`c34d36a` ＋ 佔位之 `d1`）：合併無衝突；四 blob 皆如停機款 `2` 所載；生產碼相異恰二檔；`numstat` 相同。

### 工項二　閘器於合併樹重跑（出艙入 `d3`）

`python verify/probes/probe_WG9309_gates.py <基座 2f46579 之拋棄式 worktree 之絕對路徑> <合併樹之絕對路徑> <倉外出艙目錄之絕對路徑>` ⇒ **期** `rc 0`、十閘皆 🟢、除首二列外與倉內 `verify/out/WG9309_gates.md` 逐位相同（停機款 `4`）。其 `WG9309_gates.md` 複製入倉為 **`verify/out/WG9328_gates_merged.md`**（新檔）；八個 `json` ⛔ 入倉。
🔒 **基線態**（`r`）：基座對基座 ＝ 🔴 `rc 7`（倉內 `verify/out/WG9309_pinred.md` 第 `28` 列）；基座對 `488c485` ＝ 🟢 `rc 0`（倉內 `verify/out/WG9309_gates.md`）。發單側於 Linux 沙盒以絕對路徑對合併樹實跑 ⇒ `rc 0`·除首二列逐位相同。受單側平台之輸出**未能於出單前實查**（`d`）；不符即停機款 `4`、二值並列。

### 工項三　KL 畫面輸出二檔與呈文附圖入倉（`d3`）

1. KL 將畫面輸出二檔（發單側窗二十二／二十三所收者）置於 worktree 外之任一目錄並告知 CC 其路徑；CC 以**二進位**複製為：`verify/out/KL_UI_3.5m_488c485_重劃法定報表.xlsx`、`verify/out/KL_UI_3.5m_488c485_stdout.log`（命名依既有 `verify/out/KL_UI_3.5m_<commit>_*` 之體例；`xlsx` 於 `verify/out/` 係首例）。
2. `git -c core.autocrlf=false add` 之；以 `git cat-file blob` 驗入倉之 bytes 與 `sha256` ＝ 來源（停機款 `5`）。`stdout.log` 為純 `CRLF`（`CR` `2722`）⇒ **⛔ 正規化**。
3. 抽塊 `P3` 為新檔 `docs/reports/W-G.9-328_附圖_入主線呈文平面圖.svg`。

### 工項四　登記（`d3`·純末端追加）

1. 塊 `P1` → `docs/reports/W-G.4_泛用阻塞項登記表.md` **檔末追加**（`GB-170` 之 `🔧` 節 ＋ `GB-174` 之立；標題形自 `GB-173` 與該簿最近一則 `🔧` 節逐字複刻·`v`）。
2. 塊 `P2` → `docs/reports/W-G.9波_claude.ai側自誤登記.md` **檔末追加**（`自誤 480`〜`484`；標題形自 `自誤 479` 逐字複刻）。

**塊 `P1`**：

```markdown

## 🔧 `GB-170` 之修之入主線：KL 第三次放行之登記／失效條件 `(3)` 之現況／`GB-174` 之立（`W-G.9-328`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `c34d36a1c6b437d7698abf267b1c5bb8527b4332`（本批開工態）。

**(1) KL 之放行（逐字·`2026-09-22`·⛔ 增刪一字、⛔ 擴其射程）**
> 發單側（窗二十三）呈 KL 之【要你判斷】欄為單一是非：「是否放行：將測試版本之上述修改併入正式版本（通知二之修正另單辦理）？（是／否）」。所稱「上述修改」＝ 同呈文【要改成】所載：① R2、R4 兩街廓臨側街一端之強制抵費地，其遠側界線改與側街平行，面積不變；② 緊鄰強制抵費地之宗須受藍影檢查；不合格者不配地，由下一宗遞補並同樣受檢。
> **KL 逐字所答 ＝「是」。**
> 該呈文之【對土地的影響】逐態並列（業主宗列應分配面積，抵費地列實測面積）：甲 `0 m` ＝ `R4`（強制抵費地 `116.08` ㎡ 形狀改；其與 `628(1)+` 間之 `26.11` ㎡ 狹長抵費地消失；`628(1)+` `2017.54 → 2016.04`；另一端抵費地 `1022.05 → 1049.67`）；甲 `3.5 m` ＝ `R2`（`628-42(1)` 不配地·原有 `8.34` ㎡·改前分得 `4.77` ㎡；`628-41(1)` `183.23 → 176.60`·負擔比率 `42.62% → 44.69%`；`628-40(1)+` `299.51 → 299.07`；強制抵費地 `308.17` ㎡ 形狀改；中段抵費地 `1466.26 → 1478.12`）＋ `R4`（強制抵費地 `226.01` ㎡ 形狀改；`26.11` ㎡ 狹長抵費地消失；`628(1)+` `2023.33 → 2022.05`；另一端抵費地 `906.32 → 933.73`）；乙 `0 m` ＝ 無；乙 `3.5 m` ＝ `R2`（同甲，惟 `628-40(1)` `299.24 → 298.80`、中段抵費地 `→ 1478.11`）。其他街廓逐宗不變。附平面圖 ＝ `docs/reports/W-G.9-328_附圖_入主線呈文平面圖.svg`（`W-G.9-328` 工項四所入）。
> 同呈文之通知二（不配地之宗其原有土地未計入業主之權利）即下開 `GB-174`；呈文逐字「通知二之修正另單辦理」。

🛑 **射程（由發單側釘死·⛔ CC 擴之）**：
`(a)` 及於以**合併 `commit`** 將凍存分支 `verify/W-G.9-299-gb170`（tip `488c4858da63ebe370ed950788947aa742eb44ad`·含 `86a1680`（`c2`）與 `488c485`（`c2b`））併入主線 `wip/s1-endpart`；合併後生產碼相對開工態之差須 ≡ `7eddd91 → 488c485` 之差（`app.py` `+73/−16`·`verify/stepg_pipeline.py` `+24/−7`）；
`(b)` ⛔ 及於 `GB-174` 之修；⛔ 及於 `GB-136`／`GB-167`／`168`／`169`／`171`／`172`／`173` 之任何修、`K-9-29` 之任何子項、`K-9-33 ⑤` 所增二條件之接線；
`(c)` ⛔ 改寫凍存分支（⛔ rebase、⛔ 刪除、⛔ 強推）。

**逐筆放行清單**（`恆常附款 y`·母體 ＝ 本批將落入主線之全部 `commit`·判準 ＝ 是否改動生產碼 `34` 檔）：`86a1680`（`c2`）🔴 改 `app.py`／`verify/stepg_pipeline.py`；`488c485`（`c2b`）🔴 改 `app.py`；合併 `commit` 🔴（對第一親之差 ≡ 上二筆之合）——三者即本放行之受詞；其餘本批 `commit`（本單入倉、登記、報告）⛔ 改動生產碼。

**(2) 本項失效條件之現況**：`(1)`／`(2)` ⇒ 凍存分支上成就（`W-G.9-309` 節）；`(3)` ⇒ 本批合併後於主線成就，其合併 `commit` 載於 `docs/reports/W-G.9-328R_執行報告.md`（⛔ 載於本節·自指）。🛑 **本項之解除候發單側收單復驗後登記；⛔ CC 自裁。**

---

### `GB-174` 🆕　**不配地之宗，其原有面積與應分配面積⛔ 計入該業主之歸戶：法定「歸戶負擔計算表」與試分配（四梯分級）二處皆然**

**受詞**（態 `488c485`·字樣現查）：`verify/wd4_tier_list.py` 之 `compute` 內 `g_rows = [r for r in sg["g_rows"] if r.get("推進側別") != "抵費地"]`（`:229`·歸戶之母體）；`app.py` 之 `k917_note_drop`（docstring 逐字「該宗既不進 `g_rows`」；其所記之「歸戶」欄於本案二宗皆空）；法定報表 Sheet 2「歸戶負擔計算表」之母體同。
**由**：`K-9-11 三`（不配地 ＋ 走合併／調配機制）、KL `2026-09-12` 裁一（「該同歸戶土地合併後的重劃前面積 `G(a+a'+…)`」）與裁二（現金補償一律本文式 ＝ `Σa_i × 原位置後地價`）——三者之受詞皆及於該戶之**全部**土地；現行之母體⛔ 含不配地之宗 ⇒ 該宗之權利於歸戶層消失。
**實測**（發單側窗二十三·沙盒·情形甲·`verify/wd4_tier_list.py` blob `cfd8de92c70eb7068a6f0650e33a5f7c71e1523d`·**估算性質 ＝ 半實算(試分配·非正式)**·時態 ＝ 基座 `2f46579`／凍存 `488c485` 之當次實跑·依 `GB-159` **⛔ 對外**）：
- `G011`（`628-42(1)`·`R2`·原有 `8.34` ㎡）：退縮 `0 m` 與 `3.5 m`（後者自 `488c485` 起）⛔ 計入 ⇒ 宗數 `1`、`ΣG_戶` `89.96`、增配 `25.92` ㎡、§52-1 `1,976,296` 元、§53-2 `6,516,134` 元（基座 `3.5 m` 計入時 ＝ 宗數 `2`、`94.73`、`21.15`、`1,612,602`、`6,861,642`）。
- `G025`（`628-53(2)`·`R5`·原有 `2.78` ㎡）：二退縮皆⛔ 計入 ⇒ 本文式 `30,193` 元僅按 `628-53(1)` `0.44` ㎡；未計部分 ＝ `2.78 × 72,433.68 ≈ 201,366` 元（發單側算式·`R5` 後地價取自 `rv.load_snapshot()["財務接線_v3"]`）。
- `G030`（`628-27(1)`·`R2`·原有 `51.32` ㎡）：退縮 `0 m` ⛔ 計入 ⇒ 本文式 `3,381,204` 元僅按 `628-27(2)` `46.68` ㎡；未計部分 ＝ `51.32 × 68,621.38 ≈ 3,521,649` 元（＝ 同戶 `3.5 m` 之 `6,902,853` 與 `0 m` 之差，逐元相符）。
- KL 畫面輸出（`verify/out/KL_UI_3.5m_488c485_重劃法定報表.xlsx`·「歸戶負擔計算表」）：`G011` 宗地數 `1`·原總面積 `153.46` ㎡；`G025` `0.44` ㎡。
**與既有之關係**（`恆常附款 b`／`i`／`k`·母體 ＝ 態 `c34d36a` 之 `*.md`＋`*.py` `1329` 檔·逐列 `re.search`）：式甲「（歸戶負擔｜歸戶表｜重劃前土地總面積｜原總面積）× （不配地｜剔除｜`628-42`｜`628-53`｜`DROPPED`）」雙向 `.{0,60}` ⇒ `0` 列（判別力：同形而第二組改「宗地數｜原地號」⇒ `1` 列）；式乙「（`ΣG_戶`｜`Σa_i`｜宗數｜四梯｜梯次｜試分配｜`wd4`）× （剔除｜不配地｜`DROPPED`｜`K917`）」雙向 `.{0,80}` ⇒ `7` 列；式丙「歸戶 × （不配地｜剔除）」雙向 `.{0,60}` ⇒ `17` 列——乙丙逐列檢視，皆⛔ 載本缺陷。其關係：`docs/W-F_細部規格.md` §7 之 KL 裁定 (D)（梯 `3` 之 `G025`／`G030` 不配地·補償照 §53 實算）所據之 `ΣG_戶`（`1.84`／`55.64` ㎡）**含**今之不配地宗，`W-G.9-269` 所立之剔除機制使之自歸戶消失（`W-G.9-269R_本體階_新窗開工與c2前置.md` §一 已照實併記二組 `ΣG` 之相異，⛔ 判孰誤、令其對帳屬波末重烤）⇒ 本項為**該機制所引入**；KL 域裁 M「剔除前能以同歸戶合併自救者先合併」與本項同向，本項⛔ 裁其先後；`W-G.9-269` 補令十三 `§一-2`「三戶之最終補償數……另呈」係其**值**之緩出，本項係其**母體**之缺陷；`docs/W-D.4_合併分配規格.md` 步 `0`（`ΣG_戶` ＝ 群內各宗 `G` 之直加）未載不配地宗之處置 ⇒ 本項為其**擴充**。
**待 KL 之一問**（修時另呈·⛔ 本項裁之）：梯 `2`（增配）之戶，其不配地之宗應以何應分配面積併入——本案 `G011`：改後位置之 `2.55` ㎡／改前之 `4.77` ㎡（`3.5 m`）；`0 m` 為 `0.23` ㎡。
**失效條件**：`(1)` 二處之歸戶母體皆含不配地之宗；`(2)` 梯 `2` 之併入值經 KL 裁；`(3)` 本案三戶之數逐戶重出並改前改後二態並列。🛑 **⛔ 解除、⛔ 收窄。**
```

**塊 `P2`**：

```markdown

---

### 🩸 `自誤 480`　**補令一停機款 `7` 之比對框取基座樹：受驗物既改變土地結果，其對帳原因必與基座異 ⇒ 該款於出單之當下即不可滿足；受單側以射程不及之句自解續行**

**形**：`W-G.9-309` 補令一停機款 `7` 字面「受驗樹之 `FAIL` 名目集 ≠ 基座樹，或任一 `FAIL` 之原因（名稱＋原因一併比對）≠ 基座樹」。出補令時發單側已持 CC 工項三-`5` 之實測（基座 `1029` 列 ≠ `c2` `1012` 列），附件 `B` 之土地後果必令對帳原因變動，而仍以基座為框。發單側窗二十二實測（Linux 沙盒·三樹各一跑）：基座對 `c2b` 原因相異之 `FAIL` `9` 項，`101` 列中 `99` 列屬 `R2`／`R4` 或 `B-1` 所列 `17` 宗，餘 `2` 列為 `628-42(2)`（與 `628-42(1)` 同歸戶之連動）；`c2` 對 `c2b` 僅 `1` 項（`G.1`·即補令一之本旨），十八張 `got_*.csv` 逐位相同。CC 以「單於同款末句就同型之差明文排除」自解續行——該句之射程為 `PASS` 側，所涉 `9` 項皆屬 `FAIL` 側 ⇒ 字面成就之停機款由受單側自解而未上呈（受單側之偏離·併記於本則·⛔ 另立號）。
**後果之界**：補令一之本旨（附件 `D` 除消除二名漏列外⛔ 生行為差）已由 `c2`／`c2b` 對拍獨立證成 ⇒ 發單側追認 CC 之續行；`c2b`／`c3` ⛔ 需重作。🟢
**根因**：停機款之比對框未以單出之前已持之實測驗其可滿足性（`恆常附款 d` 後段「二款並存者須自檢可同時滿足性」之類推）；比對之二態未取「前一受驗態」以隔離本步之增量（`恆常附款 o`）。
**後果之框**：🟡 字面成就之停機款未上呈。攔點 ＝ **發單側**（窗二十二·以二樹之 `got_*.csv` 逐列對拍）。
**攔法**：既有 `恆常附款 d`／`o`；受單側引條文為據時須核其射程。⛔ 新立款。

---

### 🩸 `自誤 481`　**交接文二十一 `§一-5` 載重量單 `116192` B，實 `116212` B**

**形**：發單側交接文二十一 `§一-5` 所載 `W-G.9-309` 重量單之 bytes 為 `116192`；窗二十二自倉實算 `116212`，`sha256` `ac4488dd…` 相符（CC 報告亦載 `116212`）。
**後果之界**：檔為真、⛔ 生任何判之誤。🟢
**根因**：以手抄轉入交接文，未以程式出艙之值直貼。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（窗二十二之開場序重算）。
**攔法**：既有 `恆常附款 f`／`w`。⛔ 新立款。

---

### 🩸 `自誤 482`　**補令一工項乙-`6` 載「`v3 A 逐宗全查` `87 → 88` 列」，方向倒置：實為基座 `88` → 受驗 `87`**

**形**：`W-G.9-309` 補令一工項乙-`6` 之述；實測基座 `88` 列、`c2`／`c2b` 皆 `87` 列（少一列 ＝ `628-42(1)` 於退縮 `3.5 m` 不配地）。CC 報告 `§L` 沿用原文。
**後果之界**：計數之值無誤，唯二態之序倒置；⛔ 生停機或放行之誤。🟢
**根因**：述二態之差時未同時出艙二態各自之母體與方向（`恆常附款 o`）。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（窗二十二）。
**攔法**：既有 `恆常附款 o`。⛔ 新立款。

---

### 🩸 `自誤 483`　**交接文二十二 `§二-4` 稱 `R4` 之狹長抵費地「併入街角強制抵費地」：增加者實為另一端之非強制抵費地；且 `G011` 之試分配數未載時態錨**

**形**：該節載「臨側街一端之小片抵費地（`26.11` ㎡）併入街角強制抵費地（`1022.05 → 1049.67` ㎡／`3.5 m` `906.32 → 933.73` ㎡）」。窗二十三以二樹之宗地座標對拍：`R4` 之強制抵費地為左端之 `116.08`／`226.01` ㎡（面積不變·形狀改），`26.11` ㎡ 狹長條位於其與 `628(1)+` 之間而消失；增加者為 `R4` 另一端之抵費地，該端⛔ 設強制（`right_forced_offset` ＝ `False`）。同節所載 `G011` 之增配、差額地價、放棄改領三數未載 `W-G.9-270` 補令一 `§一-2` 之時態錨。
**後果之界**：窗二十三於呈 KL 前自倉重跑、依座標改寫，並補三要件 ⇒ 誤述⛔ 入呈文。🟢
**根因**：以量之名稱與增減額推其位置，未對拍 `cut_coords` 之位置。
**後果之框**：🟢 零入呈文之誤。攔點 ＝ **發單側**（窗二十三）。
**攔法**：既有 `恆常附款 q`（呈 KL 之土地影響須逐態並列）與 `W-G.9-270` 補令一 `§一-2`。⛔ 新立款。

---

### 🩸 `自誤 484`　**窗二十三之入主線呈文未載逐筆放行清單（`恆常附款 y`）**

**形**：該呈文之【要你判斷】以「測試版本之上述修改」為受詞，未自倉重導「本批將落入主線之全部 `commit`」及其是否改動生產碼。
**後果之界**：將落入主線而改動生產碼者恰為 `86a1680`（`c2`）、`488c485`（`c2b`）及其合併 `commit`；合併 `commit` 對第一親之差 ≡ `7eddd91 → 488c485` 之差（`W-G.9-328` 停機款 `3` 保之）⇒ 放行之受詞與呈文所述之修改同一；清單已補載於 `GB` 簿 `W-G.9-328` 節。🟢
**根因**：呈文以地政用語撰寫時，將 `y` 視為單內之事而未置入呈文。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（擬 `W-G.9-328` 時自捕）。
**攔法**：既有 `恆常附款 y`。⛔ 新立款。
```

**塊 `P3`**（`svg`·`6` 列）：

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 974.4970201253891" width="760" height="974.4970201253891" xmlns:c2pa="http://c2pa.org/manifest"><metadata><c2pa:manifest>AAAWgmp1bWIAAAAeanVtZGMycGEAEQAQgAAAqgA4m3EDYzJwYQAAABZcanVtYgAAAEdqdW1kYzJtYQARABCAAACqADibcQN1cm46YzJwYTpkNDc5ZmIyNy1iN2FmLTQyY2QtYTFiZi04NGJkZDY4Njc4YzcAAAADl2p1bWIAAAApanVtZGMyYXMAEQAQgAAAqgA4m3EDYzJwYS5hc3NlcnRpb25zAAAAALxqdW1iAAAARGp1bWRjYm9yABEAEIAAAKoAOJtxE2MycGEuaW5ncmVkaWVudC52MwAAAAAYYzJzaJRCjEmp7BH62opiAu0Vx+YAAABwY2JvcqNpZGM6Zm9ybWF0bWltYWdlL3N2Zyt4bWxqaW5zdGFuY2VJRHgseG1wOmlpZDpmM2ZmMDhkYi0wNDYzLTRiZGUtOTQ3My00MDJiNmU5ZjJhZjNscmVsYXRpb25zaGlwaHBhcmVudE9mAAAB4mp1bWIAAABBanVtZGNib3IAEQAQgAAAqgA4m3ETYzJwYS5hY3Rpb25zLnYyAAAAABhjMnNoHXdIn9is5ceeWRsAX1Hz6QAAAZljYm9yomdhY3Rpb25zgqJmYWN0aW9ua2MycGEub3BlbmVkanBhcmFtZXRlcnOha2luZ3JlZGllbnRzgaJjdXJseC1zZWxmI2p1bWJmPWMycGEuYXNzZXJ0aW9ucy9jMnBhLmluZ3JlZGllbnQudjNkaGFzaFggN43jNr+Bd1QBi5uL6Pw74A56+8a5XH4lbqObS5UoWKSkZmFjdGlvbngdY29tLmFudGhyb3BpYy5jbGF1ZGUucHJvdmlkZWRqcGFyYW1ldGVyc6F4H2NvbS5hbnRocm9waWMub3JpZ2luLWNvbmZpZGVuY2VndW5rbm93bmtkZXNjcmlwdGlvbnhmQ2xhdWRlIHByb3ZpZGVkIHRoaXMgZmlsZSBhdCB0aGUgcmVxdWVzdCBvZiBhIHVzZXIgYW5kIG1heSBoYXZlIGNyZWF0ZWQgb3IgbW9kaWZpZWQgdGhlIGZpbGUgY29udGVudHMubXNvZnR3YXJlQWdlbnShZG5hbWVmQ2xhdWRlcmFsbEFjdGlvbnNJbmNsdWRlZPUAAADIanVtYgAAAEBqdW1kY2JvcgARABCAAACqADibcRNjMnBhLmhhc2guZGF0YQAAAAAYYzJzaI3EPqPp5JTCl1U6n7oWoecAAACAY2JvcqVjYWxnZnNoYTI1NmNwYWRNAAAAAAAAAAAAAAAAAGRoYXNoWCA1MZ4749msRSjL9IRAPfdPbDTnfMY8t301WENrOFCgU2RuYW1lbmp1bWJmIG1hbmlmZXN0amV4Y2x1c2lvbnOBomVzdGFydBiyZmxlbmd0aBkeBAAAAj5qdW1iAAAAJ2p1bWRjMmNsABEAEIAAAKoAOJtxA2MycGEuY2xhaW0udjIAAAACD2Nib3KlY2FsZ2ZzaGEyNTZpc2lnbmF0dXJleE1zZWxmI2p1bWJmPS9jMnBhL3VybjpjMnBhOmQ0NzlmYjI3LWI3YWYtNDJjZC1hMWJmLTg0YmRkNjg2NzhjNy9jMnBhLnNpZ25hdHVyZWppbnN0YW5jZUlEeCx4bXA6aWlkOjhjMmFhMmQ5LTJhMjctNGI4MS1hNGMxLTk4NWE3NGY5ZWRlY3JjcmVhdGVkX2Fzc2VydGlvbnODomN1cmx4LXNlbGYjanVtYmY9YzJwYS5hc3NlcnRpb25zL2MycGEuaW5ncmVkaWVudC52M2RoYXNoWCA3jeM2v4F3VAGLm4vo/DvgDnr7xrlcfiVuo5tLlShYpKJjdXJseCpzZWxmI2p1bWJmPWMycGEuYXNzZXJ0aW9ucy9jMnBhLmFjdGlvbnMudjJkaGFzaFgggJKlZAMI78unbaGoupRemR/9Tnb+2or0S2o2lZ0LRtyiY3VybHgpc2VsZiNqdW1iZj1jMnBhLmFzc2VydGlvbnMvYzJwYS5oYXNoLmRhdGFkaGFzaFggDI6NcMKAeXtTma2YDlU8U4wM6ZK3tiMp+810uKF4xgp0Y2xhaW1fZ2VuZXJhdG9yX2luZm+jZG5hbWVvQW50aHJvcGljIEZpbGVzZ3ZlcnNpb25lMS4wLjBrc3BlY1ZlcnNpb25lMi40LjAAABA4anVtYgAAAChqdW1kYzJjcwARABCAAACqADibcQNjMnBhLnNpZ25hdHVyZQAAABAIY2JvctKEWQISogEmGCFZAgowggIGMIIBjaADAgECAhRA5aAK7sI50L64g/oGQgU9Z1UTADAKBggqhkjOPQQDAzBJMRcwFQYDVQQKEw5BbnRocm9waWMsIFBCQzEuMCwGA1UEAxMlQW50aHJvcGljIENvbnRlbnQgQ3JlZGVudGlhbHMgUm9vdCBDQTAeFw0yNjA4MDcxODQzNTZaFw0yODA4MDYxOTQzNTZaMEQxFzAVBgNVBAoTDkFudGhyb3BpYywgUEJDMSkwJwYDVQQDEyBBbnRocm9waWMgQ2xhdWRlIENvbnRlbnQgU2lnbmluZzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABJh6CmvLUBgFFNU0vUKlOVtE6djd17L5SuwX0LemFisBM3dkd/3cyjxFA3Qo5S46fX0/ihY0VZ7mfb9KF703t5OjWDBWMA4GA1UdDwEB/wQEAwIHgDAVBgNVHSUEDjAMBgorBgEEAYPoXgIBMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUzlHiBIFOZFsj+OPEz5o+nMHXXMIwCgYIKoZIzj0EAwMDZwAwZAIwMXMdFJ4BetLLVY7ORuE9noqbbAZOZn/aArXyTwFAZfKrPzxF2vPoJNf1+UCdg1XGAjBwX1zd9WGqYkqmL5SFqw1QySjr1zJfpJM9+1rdDwSPLMOPOjKuiXjoU/pUUeG9RwmhY3BhZFkNngAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPZYQPVkXj3d/L69DbBx/nchGiKHRFvj+zr0Lloxtoxd0xgbZadMfvO4T9evYqbBY1MumtKCQRiAyIMR7DOEFsVPsKU=</c2pa:manifest></metadata><style>
svg{font-family:"Noto Sans CJK TC","Microsoft JhengHei","PingFang TC",sans-serif}.t{font-size:14px;font-weight:600;fill:#222}.l{font-size:11px}.e{font-size:11px;font-weight:600;fill:#555;text-anchor:middle}.s{font-size:10px;fill:#666}
.own{fill:#dbe9f6;stroke:#555;stroke-width:0.6}.chg{fill:#9cc3e8;stroke:#1f5f99;stroke-width:1}
.pool{fill:#fde3b0;stroke:#8a6d3b;stroke-width:0.6}.forced{fill:#f5b041;stroke:#8a4b08;stroke-width:1.2}
.drop{fill:#c0392b;stroke:#c0392b;stroke-width:2.5}
</style><rect width="100%" height="100%" fill="#fff"/><text x="40" y="72" class="t">R2 街廓・臨側街一端（退縮 3.5 m）改前</text><text x="40" y="87" class="s">強制抵費地之遠側界線與宗地分配線平行，與側街夾約 4.3°</text><path d="M83.3,469.3 L82.4,469.3 L109.6,110.2 L110.4,110.2 L83.3,469.3 Z" class="drop"/><path d="M116.0,469.1 L83.3,469.3 L110.4,110.2 L143.1,110.4 L116.0,469.1 Z" class="chg"/><path d="M121.2,469.1 L116.0,469.1 L143.1,110.4 L148.4,110.4 L121.2,469.1 Z" class="own"/><path d="M174.7,468.8 L121.2,469.1 L148.4,110.4 L201.8,110.6 L174.7,468.8 Z" class="own"/><path d="M190.8,468.8 L174.7,468.8 L201.8,110.6 L208.0,110.7 L208.0,241.5 L190.8,468.8 Z" class="own"/><path d="M190.8,468.8 L208.0,241.5 L208.0,468.7 L190.8,468.8 Z" class="own"/><path d="M82.4,469.3 L40.0,469.5 L40.0,138.2 L68.4,110.0 L109.6,110.2 L82.4,469.3 Z" class="forced"/><line x1="67.5" y1="303.8" x2="223.0" y2="126.0" stroke="#444" stroke-width="0.8"/><circle cx="67.5" cy="303.8" r="1.8" fill="#444"/><text x="226.0" y="130.0" class="l" fill="#444">抵費地（強制） 308.17 ㎡</text><line x1="96.4" y1="289.7" x2="223.0" y2="174.5" stroke="#c0392b" stroke-width="0.8"/><circle cx="96.4" cy="289.7" r="1.8" fill="#c0392b"/><text x="226.0" y="178.5" class="l" fill="#c0392b">628-42(1) 4.77 ㎡</text><line x1="113.2" y1="289.7" x2="223.0" y2="223.0" stroke="#1f5f99" stroke-width="0.8"/><circle cx="113.2" cy="289.7" r="1.8" fill="#1f5f99"/><text x="226.0" y="227.0" class="l" fill="#1f5f99">628-41(1) 183.22 ㎡</text><line x1="132.2" y1="289.7" x2="223.0" y2="271.5" stroke="#444" stroke-width="0.8"/><circle cx="132.2" cy="289.7" r="1.8" fill="#444"/><text x="226.0" y="275.5" class="l" fill="#444">628-27(1) 29.62 ㎡</text><line x1="161.5" y1="289.7" x2="223.0" y2="320.0" stroke="#444" stroke-width="0.8"/><circle cx="161.5" cy="289.7" r="1.8" fill="#444"/><text x="226.0" y="324.0" class="l" fill="#444">628-40(1)+ 299.50 ㎡</text><line x1="191.4" y1="355.1" x2="223.0" y2="368.5" stroke="#444" stroke-width="0.8"/><circle cx="191.4" cy="355.1" r="1.8" fill="#444"/><text x="226.0" y="372.5" class="l" fill="#444">628-30(2) 89.97 ㎡（部分）</text><line x1="203.7" y1="355.1" x2="223.0" y2="417.0" stroke="#444" stroke-width="0.8"/><circle cx="203.7" cy="355.1" r="1.8" fill="#444"/><text x="226.0" y="421.0" class="l" fill="#444">628-39(1) 236.54 ㎡（部分）</text><text x="32" y="289.8" class="e" transform="rotate(-90 32 289.8)">側街</text><text x="124.0" y="106" class="e">正面道路</text><text x="124.0" y="483.5" class="e">後側</text><text x="226.0" y="469.5" class="s">→ 往街廓另一端</text><line x1="40" y1="499.5021931119263" x2="80.0" y2="499.5021931119263" stroke="#333" stroke-width="2"/><text x="84.0" y="503.5021931119263" class="s">5 m</text><text x="410" y="72" class="t">R2 街廓・臨側街一端（退縮 3.5 m）改後</text><text x="410" y="87" class="s">強制抵費地之遠側界線改與側街平行（面積不變）</text><path d="M466.0,110.1 L511.0,110.3 L483.9,469.1 L466.0,469.2 L466.0,110.1 Z" class="chg"/><path d="M489.2,469.1 L483.9,469.1 L511.0,110.3 L516.3,110.4 L489.2,469.1 Z" class="own"/><path d="M542.6,468.9 L489.2,469.1 L516.3,110.4 L569.7,110.6 L542.6,468.9 Z" class="own"/><path d="M558.7,468.8 L542.6,468.9 L569.7,110.6 L578.0,110.7 L578.0,213.5 L558.7,468.8 Z" class="own"/><path d="M558.7,468.8 L578.0,213.5 L578.0,468.7 L558.7,468.8 Z" class="own"/><path d="M410.0,138.2 L438.4,110.0 L466.0,110.1 L466.0,469.2 L410.0,469.5 L410.0,138.2 Z" class="forced"/><line x1="438.0" y1="303.7" x2="593.0" y2="126.0" stroke="#444" stroke-width="0.8"/><circle cx="438.0" cy="303.7" r="1.8" fill="#444"/><text x="596.0" y="130.0" class="l" fill="#444">抵費地（強制） 308.17 ㎡</text><line x1="481.7" y1="289.7" x2="593.0" y2="182.6" stroke="#1f5f99" stroke-width="0.8"/><circle cx="481.7" cy="289.7" r="1.8" fill="#1f5f99"/><text x="596.0" y="186.6" class="l" fill="#1f5f99">628-41(1) 176.59 ㎡</text><line x1="500.1" y1="289.7" x2="593.0" y2="239.2" stroke="#444" stroke-width="0.8"/><circle cx="500.1" cy="289.7" r="1.8" fill="#444"/><text x="596.0" y="243.2" class="l" fill="#444">628-27(1) 29.61 ㎡</text><line x1="529.5" y1="289.7" x2="593.0" y2="295.8" stroke="#444" stroke-width="0.8"/><circle cx="529.5" cy="289.7" r="1.8" fill="#444"/><text x="596.0" y="299.8" class="l" fill="#444">628-40(1)+ 299.06 ㎡</text><line x1="560.3" y1="341.1" x2="593.0" y2="352.3" stroke="#444" stroke-width="0.8"/><circle cx="560.3" cy="341.1" r="1.8" fill="#444"/><text x="596.0" y="356.3" class="l" fill="#444">628-30(2) 89.97 ㎡（部分）</text><line x1="573.2" y1="341.1" x2="593.0" y2="408.9" stroke="#444" stroke-width="0.8"/><circle cx="573.2" cy="341.1" r="1.8" fill="#444"/><text x="596.0" y="412.9" class="l" fill="#444">628-39(1) 236.54 ㎡（部分）</text><text x="402" y="289.8" class="e" transform="rotate(-90 402 289.8)">側街</text><text x="494.0" y="106" class="e">正面道路</text><text x="494.0" y="483.5" class="e">後側</text><text x="596.0" y="469.5" class="s">→ 往街廓另一端</text><line x1="410" y1="499.5021931119263" x2="450.0" y2="499.5021931119263" stroke="#333" stroke-width="2"/><text x="454.0" y="503.5021931119263" class="s">5 m</text><text x="40" y="546.5021931119263" class="t">R4 街廓・臨側街一端（退縮 3.5 m）改前</text><text x="40" y="561.5021931119263" class="s">強制抵費地之遠側界線與側街夾約 2.7°，其後留一狹長抵費地</text><path d="M99.8,584.5 L160.0,584.5 L160.0,849.5 L124.4,849.5 L99.8,584.5 Z" class="chg"/><path d="M40.0,614.1 L40.0,614.1 L67.0,584.5 L99.8,584.5 L111.8,849.5 L61.8,849.5 L40.0,614.1 Z" class="forced"/><path d="M99.8,584.5 L124.4,849.5 L111.8,849.5 L99.8,584.5 Z" class="pool"/><line x1="78.7" y1="731.8" x2="175.0" y2="600.5" stroke="#444" stroke-width="0.8"/><circle cx="78.7" cy="731.8" r="1.8" fill="#444"/><text x="178.0" y="604.5" class="l" fill="#444">抵費地（強制） 226.01 ㎡</text><line x1="108.9" y1="717.0" x2="175.0" y2="682.2" stroke="#444" stroke-width="0.8"/><circle cx="108.9" cy="717.0" r="1.8" fill="#444"/><text x="178.0" y="686.2" class="l" fill="#444">抵費地 26.11 ㎡</text><line x1="136.0" y1="717.0" x2="175.0" y2="763.8" stroke="#1f5f99" stroke-width="0.8"/><circle cx="136.0" cy="717.0" r="1.8" fill="#1f5f99"/><text x="178.0" y="767.8" class="l" fill="#1f5f99">628(1)+ 2023.34 ㎡（部分）</text><text x="32" y="717.0" class="e" transform="rotate(-90 32 717.0)">側街</text><text x="178.0" y="849.5" class="s">→ 往街廓另一端</text><line x1="40" y1="879.4970201253891" x2="80.0" y2="879.4970201253891" stroke="#333" stroke-width="2"/><text x="84.0" y="883.4970201253891" class="s">5 m</text><text x="410" y="546.5021931119263" class="t">R4 街廓・臨側街一端（退縮 3.5 m）改後</text><text x="410" y="561.5021931119263" class="s">強制抵費地之遠側界線改與側街平行，628(1)+ 直接緊鄰</text><path d="M463.5,584.5 L530.0,584.5 L530.0,849.5 L488.1,849.5 L463.5,584.5 Z" class="chg"/><path d="M410.0,614.1 L437.0,584.5 L463.5,584.5 L488.1,849.5 L431.8,849.5 L410.0,614.1 L410.0,614.1 Z" class="forced"/><line x1="449.0" y1="731.8" x2="545.0" y2="600.5" stroke="#444" stroke-width="0.8"/><circle cx="449.0" cy="731.8" r="1.8" fill="#444"/><text x="548.0" y="604.5" class="l" fill="#444">抵費地（強制） 226.01 ㎡</text><line x1="502.9" y1="717.0" x2="545.0" y2="723.0" stroke="#1f5f99" stroke-width="0.8"/><circle cx="502.9" cy="717.0" r="1.8" fill="#1f5f99"/><text x="548.0" y="727.0" class="l" fill="#1f5f99">628(1)+ 2022.04 ㎡（部分）</text><text x="402" y="717.0" class="e" transform="rotate(-90 402 717.0)">側街</text><text x="548.0" y="849.5" class="s">→ 往街廓另一端</text><line x1="410" y1="879.4970201253891" x2="450.0" y2="879.4970201253891" stroke="#333" stroke-width="2"/><text x="454.0" y="883.4970201253891" class="s">5 m</text><rect x="40" y="904.4970201253891" width="16" height="12" class="forced"/><text x="62" y="914.4970201253891" class="l">強制抵費地</text><rect x="280" y="904.4970201253891" width="16" height="12" class="pool"/><text x="302" y="914.4970201253891" class="l">其他抵費地</text><rect x="520" y="904.4970201253891" width="16" height="12" class="chg"/><text x="542" y="914.4970201253891" class="l">面積有變之業主宗</text><rect x="40" y="926.4970201253891" width="16" height="12" class="own"/><text x="62" y="936.4970201253891" class="l">其他業主宗</text><rect x="280" y="926.4970201253891" width="16" height="12" class="drop"/><text x="302" y="936.4970201253891" class="l">628-42(1)（改後不配地；寬約 0.1 m，以粗紅線示其位置）</text><text x="40" y="964.4970201253891" class="s">資料：發單側沙盒實跑，情形甲、退縮 3.5 m；改前＝基座 2f46579，改後＝測試版本 488c485。狹長宗為便識讀以線示意，面積為實值。依 GB-159，本圖⛔ 對外。</text></svg>
```

**塊 `P4`**（合併 `commit` 之訊息）：

```text
W-G.9-328 工項一：凍存分支 verify/W-G.9-299-gb170（c2 86a1680＋c2b 488c485）併入主線 🔴 生產碼（KL 2026-09-22 放行「是」）

GB-170 之修（強制抵費地之遠側界線與側街平行、其物化形、強制側藍影受檢宗序）與 _WF_NS_NAMES 補列二名。
合併後生產碼對第一親之差 ≡ 7eddd91→488c485（app.py +73/−16·verify/stepg_pipeline.py +24/−7）。
放行逐字與射程：docs/reports/W-G.4_泛用阻塞項登記表.md 之 W-G.9-328 節。
```

### 工項五　執行報告入倉（`d4`·新檔 `docs/reports/W-G.9-328R_執行報告.md`）＋ 收工閘

報告須載：`d1`〜`d4` 之 hash（**合併 `commit` 之 hash 即 `GB-170` 失效條件 `(3)` 之錨**）；停機款 `1`〜`10` 之三值；工項一之四 blob 與 `numstat`；工項二之 `rc` 與逐位對拍；工項三之二檔 bytes／`sha256`（來源與 blob）；`§四` 各閘之實得。收工閘於 `d4` 之後量、其實測值出艙於回報（⛔ 寫入報告·自指）。
🛑 **推送**：`§四` 全 🟢 後，先行停機款 `1` 之實查，再一次 `push` `d1`〜`d4`（主線為快轉）。⛔ 推送凍存分支。

---

## `§四`　收工閘（`d4` 入倉後於主線量·三值·基線態 ＝ `§一`）

🔒 **`n③` 之施行**：發單側已於拋棄式分支模擬 `d1`〜`d4`（`d1`／`d4` 以佔位檔代）並實跑本節各閘——下表之期值即其實得（**必過之實例**）；於**合併 `commit` 之態**（未追加）跑閘 `8` ⇒ **`rc 7`**（**必破之實例**·新號 `484` 未命中、`MAX` 仍 `479`）。

| 閘 | 受詞 | 基線態（開工態） | 期 |
|---|---|---|---|
| `1` | 逐 `commit` 之刪除欄 | — | `d1`／`d3`／`d4` 逐檔 `0`；**唯一具名豁免** ＝ `d2`（合併）：對第一親 ＝ `app.py` `+73/−16`·`verify/stepg_pipeline.py` `+24/−7` |
| `2` | 生產碼 `34` 檔對開工態之相異 | `0` | 恰 `app.py` ⋀ `verify/stepg_pipeline.py`；四 blob 如停機款 `2` |
| `3` | 本批 `.md` 與 `.svg` 之 `CR` | — | 受檢 `6` 檔（本單／報告／`GB` 簿／自誤簿／`WG9328_gates_merged.md`／附圖）合計 **`0`**；`stdout.log` 具名豁免（`CR` `2722`·來源原樣） |
| `4` | 四簿期末（二框並報） | 見 `§一` 項 `4`／`4′` | 見 `§四-1` |
| `5` | `append-only` 三值 | — | 自誤簿 🟢／`GB` 簿 🟢／恆常附款簿 🔵／`K-6` 典 🔵／`VR` 簿 🔵／`CLAUDE.md` 🔵 |
| `6` | 自限 | `§一` 項 `5`／`6`／`2` | `baselines` 與遠端 `26` **⛔ 變**；凍存分支 tip ⛔ 變；保全分支 `origin/wip/W-G.9-318-preserve` 仍為主線之祖 |
| `7` | 母體 | `§一` 項 `8` | 除本批之產物外 ＝ 開工態；全倉 **`2641`**（＋ `6`：本單／合併閘器出艙／`xlsx`／`stdout.log`／附圖／報告 ＋ `N_cc`）｜`.md` **`909`**｜`docs/` **`867`**｜`verify/out/` **`1029`**｜頂層 `*.py` `33`｜子層 `*.py` `385`；`N_cc` 逐筆具名（`e②`） |
| `8` | `python verify/probes/probe_WG9270_closegate.py 484 479 .` | 🟢 `rc 0`（`479 468`） | **`rc 0`** |
| `9` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <out 絕對路徑> 484 479` | 🟢 `rc 0`（`479 468`） | **`rc 0`** |
| `10` | 工項二之閘器 | 見工項二 | **`rc 0`**·除首二列與 `WG9309_gates.md` 逐位相同 |

### `§四-1`　四簿期末之算式（`w①`）

| 框 | 簿 | 算式 | 期末 |
|---|---|---|---|
| 正典框 | 自誤 | `469` ＋ `5`（`480`／`481`／`482`／`483`／`484`） | **`474`**／`MAX` **`484`**／缺 `[106,355,356,357]` |
| 自擬框 | 自誤 | `465` ＋ `5` | **`470`**／`MAX` **`484`** |
| 正典框 | `GB` | `171` ＋ `1`（`174`） | **`172`**／`MAX` **`174`**／缺 `[12,87]` |
| 正典框 | `VR`／`K-9` | ⛔ 鑄 | `80`／`95`·`42`／`43`·⛔ 變 |
| — | 恆常附款 | ⛔ 新立·⛔ 修訂 | **`28`** 款·表列式 `37`·⛔ 變 |

五簿／典期末（**算式**）：自誤簿 `1001228 + 5331 = 1006559` B·`11163 + 50 = 11213` 列｜`GB` 簿 `950471 + 7717 = 958188` B·`8438 + 34 = 8472` 列｜恆常附款簿／`K-6` 典／`VR` 簿 ⛔ 變。

---

## `§五`　驗收與上呈

### `§五-1`　受單側收單時須當場重算之基數（`f`）

| # | 基數 | 單載 |
|---|---|---|
| `1` | 工項數／`commit` 數 | **`6`**（零〜五）／**`4`**（`d1`〜`d4`） |
| `2` | `§六` 款數 | **`28`**（施行 `20`／不生 `8`） |
| `3` | 所鑄 | 自誤 **`5`**（`480`〜`484`）／`GB` **`1`**（`174`）／裁 **`0`** |
| `4` | 停機款數 | **`10`** |
| `5` | 塊（圍欄內·末附換行） | `P1` `:118`–`:151`·**`7717`** B·`c195f81076e6da54…`／`P2` `:157`–`:206`·**`5331`** B·`8e2d6bcc85d739c8…`／`P3` `:212`–`:217`·**`17367`** B·`e6d8906c03cce843…`／`P4` `:223`–`:227`·**`504`** B·`eeb447ccdbf3fc6a…` |
| `6` | KL 二檔（來源） | 畫面輸出 `xlsx`（本窗收檔之名 `重劃法定報表_trunkA_prime_3_5m__3_.xlsx`）：**`14603`** B·`baaa1c17d0b6e95062389121f4173fafafc2e83d3a103bc4247d64c9a6d27cb5`｜主控台全文：**`139861`** B·`f4ee16e63f9818319555081ec4fec19fb6198138b3ccd11c906bad4b8a4ee546`（`CR` `2722`／`LF` `2722`） |

🔒 抽取一律依**圍欄之逐列索引**（`常規七 一`）；bytes 不符 ⇒ 停機款 `6`。其餘不符者以列舉為準並具名·⛔ 追改本單一字。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 合併 `commit` 係 KL `2026-09-22` 所放行（`§二`）⇒ 收工閘全 🟢 後由 CC **逕行 `push`**；⛔ 及於繞過 harness 權限分類器。
3. **KL 之事**：推送之後、任何畫面核對之前，主 checkout（`C:\Users\admin\Desktop\land-readjustment-trial`）須先更新至新主線。

---

## `§六`　恆常附款逐款回掃（`28` 款）

| 款 | 對本單之施行 | 判 |
|---|---|---|
| `a` | 本單⛔ 鑄攔法（五則自誤之攔法皆「既有·⛔ 新立款」） | ⚪ 不生 |
| `b` | 本單⛔ 鑄裁（`GB-174` 為阻塞項） | ⚪ 不生 |
| `c` | 本單⛔ 動 `_corner_buffer_S` 之迴圈（合併僅帶入已驗之碼） | ⚪ 不生 |
| `d` | 工項二之期值及於受單側平台、工項三之二檔在 KL 之機 ⇒ **未能於出單前實查**；不符者停機款 `4`／`5`、二值並列 | 🟢 施行 |
| `e`／`e②`／`e③` | `§零-1` 四框逐筆；`§四` 閘 `7` 寫為「除本批之產物外」並含 `N_cc` | 🟢 施行 |
| `f` | `§五-1` 令受單側重算其基數 | 🟢 施行 |
| `g` | 本批六新路徑以 `git check-ignore -v` 查 ⇒ 皆⛔ 在忽略族（`rc 1`·`.gitignore` `27` 非空列） | 🟢 施行 |
| `h` | 全部 payload 以檔案管線、依圍欄之逐列索引抽取；`commit` 訊息 `-F` | 🟢 施行 |
| `i` | 量測之受詞（閘器·試分配器）已讀 `GB-170` 全部 `🔧` 節、`GB-171`〜`173`、`GB-159`／`GB-162`（⛔ 用 baseline 之數）；`GB-174` 之關係具名於塊 `P1` | 🟢 施行 |
| `j` | ⛔ 以哨兵之落地後全倉命中為期值 | ⚪ 不生 |
| `k` | 「倉內無」之宣稱：`§零-1` 四框；`GB-174` 之三式（塊 `P1`·式甲附判別力）；⛔ 新立器（沿用閘器與正典器） | 🟢 施行 |
| `l`／`l⑥` | `§零-1` 之框式可原樣執行；塊之 bytes 明定「圍欄內·末附換行」 | 🟢 施行 |
| `m` | 本單⛔ 定替身 | ⚪ 不生 |
| `n`／`n②`／`n③`／`n④` | 停機款三值；閘器於驅動失敗時 loud（`🛑 未執行`）；`§四` 載必過／必破二實例；呼叫形寫 `python`、路徑取絕對形 | 🟢 施行 |
| `o` | 二態之差（開工態對合併樹：母體 ＝ 生產碼 `34` 檔；基座對合併樹：母體 ＝ 閘器之四格·`18` 街廓格）皆同母體 ⇒ 可比 | 🟢 施行 |
| `p` | 本單係讀畢 `docs/reports/W-G.9-309R_執行報告.md` 全文與交接文二十二、開場序未跳之後所擬 | 🟢 施行 |
| `q`／`q②` | 呈文之【對土地的影響】逐態並列（塊 `P1` 逐字）；以地政用語 | 🟢 施行 |
| `r` | `§四` 各閘並載基線態 | 🟢 施行 |
| `s` | ⛔ 設殘差之期值帶 | ⚪ 不生 |
| `t` | 純末端追加·⛔ 以既有文字為錨之插入 | ⚪ 不生 |
| `u` | ⛔ 將既有之量接入新路徑（合併之碼已於 `W-G.9-309` 驗） | ⚪ 不生 |
| `v` | 塊 `P1`／`P2` 之標題形自 `GB-173`／`自誤 479` 逐字複刻；於拋棄式分支以正典器自驗（閘 `8` `rc 0`）；`§四-1` 二框並報 | 🟢 施行 |
| `w` | `§四-1` 為算式並逐號列舉；`§一` 逐格繫 `c34d36a`；呼叫形含引數 | 🟢 施行 |
| `x` | `§四` 閘 `5` 為三值 | 🟢 施行 |
| `y` | 逐筆放行清單載於塊 `P1`；其缺於呈文者登記為 `自誤 484` | 🟢 施行 |
| `z` | 對照乙之定義域已先列舉（`§零-1`） | 🟢 施行 |
| `aa` | 對照甲 ＝ `W-G.9-325`／`GB-173`／`自誤 479`（同形族） | 🟢 施行 |
| `ab` | ① 本單⛔ 新立或修訂款；② 四簿之數取自正典器（`probe_WG9270_closegate.py`）·⛔ 以文字搜框取之 | 🟢 施行 |

**算式**：施行 ＝ **`20`**（`d e f g h i k l n o p q r v w x y z aa ab`）／不生 ＝ **`8`**（`a b c j m s t u`）；`20 + 8 = 28`·重疊 `[]`。

---

SELF_SHA256: 85ce53edfade165548547260271bda4bff3d26ed052f3575d83ec98a7837d73d
