# `W-G.9-349`　重量單：不能建築之宗之入池（閘二 `K-9-12`／`K-9-13` ＋ 臨正街寬 `K-9-33` 之接線）＋ `K-9-29 六` 入池閘（同歸戶相鄰合併試算）＋ `k*` 經驗錨之重錨 ＋ 攢批登記 ＋ 待落地清單之更新

> **發單** ＝ 發單側窗四十五·`2026-09-26`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**；工項五於 **KL 之主 checkout**）。
> **級** ＝ **重**（生產碼 `3` 檔：`app.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py`；🔴 **有土地後果**——KL 於 `2026-09-26` 之請示〔附圖〕答「是」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `88dc179e730e829b8b3ec828bb2df40841d0b900`。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D1`／`F8`／`E2`／`G2`／`R1`／`P3` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）。
> 🔑 **來源檔一**（KL 置於 **CC 之施工樹之根**·檔名逐字）：`W-G.9-349_重量單.md`（本單）。CC 一律**二進位複製**、⛔ 讀入改寫；施工樹之根無之 ⇒ 取 KL 主 checkout 之根（承 `W-G.9-348R` 自解 `1`）。本批之新檔（`F8`）與改動（`D1`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）；唯本單明令設 `WV_K929_6=off` 之呼叫，於**該呼叫之環境**設之（⛔ 設於殼）。
> 🛑 **本單⛔ 及於**：塊 `D1` 以外之生產碼一字；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單（`K6A2_期望FAIL名單_WG97_名目加原因.txt`、`WG99_端到端複本_終止點凍存_投影.txt`）；`K-6` 典／`VR` 簿；任何側支之刪除或改寫。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `88dc179e730e829b8b3ec828bb2df40841d0b900`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 537 523` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔 **`899`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗四十五實跑 `python verify/probes/wg9268_gate6_occupancy.py 88dc179 W-G.9-349 W-G.9-348 W-G.9-398`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-349`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-348` | `2`／`6`／`4` | `2`／`6`／`4` | `10` | `3` | `4`／`44` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-398` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`1` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `7`／`7` | 🟢 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態之追蹤檔 `2698` 檔〔可讀 `2674`〕·錨定框 `(?<![0-9\-])<號>(?![0-9])`·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取）：

| 號 | 裸（錨定）檔／列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 538`〜`541`（`4` 號·逐號） | 皆 `0`／`0` | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`自誤 537` | `3`／`4` | `0`／`0` | `3`／`4` | 🟢 C 形非空（B 形於本倉為量測器紅·`GB-158`） |
| `GB-192`／`GB-193` | 皆 `0`／`0` | — | — | 🟢 可取 |
| 對照甲［必非零］`GB-191` | `4`／`16` | — | — | 🟢 |

自誤 `MAX` ＝ `537`、`GB` `MAX` ＝ `191`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 538`〜`541`、`GB-192`／`GB-193`；⛔ 鑄 `VR`／`K-9`。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `88dc179`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`F8`／`E2`／`G2`／`R1`／`P3` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二前置之任一期不符（尤：`F8 selftest`／`F8 wiring` 之改前 `rc ≠ 1`） |
| `5` | 塊 `D1` 之 `git apply --check` 不過；或施後之 blob ≠ `§五-1` 項 `8` |
| `6` | 工項二之驗 `V-1`〜`V-5` 任一 ≠ 期（尤：`V-5` 之相異項或 ✅→🔴 逾 `§三` 工項二所列） |
| `7` | 工項二之 `push` 無 `§二` 之放行；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項三之四檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項五：主 checkout 之追蹤檔有變動、或切至 `wip/s1-endpart` 被拒、或 `--ff-only` 被拒 |
| `11` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `12` | 本批任一新檔為 `git check-ignore` 所命中 |
| `13` | 任一呼叫出艙 `K-9-29 六` 之停機（`【未裁】`：合併組含街角第 `1` 宗／跨左右推進／一達一未達之反例；或「逾輪未收斂」）——本案實測⛔ 觸發（`§一` 項 `7`） |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `10`。

---

## `§一`　態錨（發單側窗四十五自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `88dc179e730e829b8b3ec828bb2df40841d0b900`；側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`30`**（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼（開工態 blob） | `app.py` `f4c47af6b864de683b99985597310d36b1f43d23`（`1489745` B）；`verify/stepg_pipeline.py` `eb557b4bb3caeaf7ef2459dadc7919f3334a432e`（`116528` B）；`verify/run_verification.py` `ed488baef2e2dab99a6c054ad0a9110675b9afdf`（`101222` B） |
| `3` | `run_all`（開工態·倉外路徑） | `64` 項：PASS `31`／FAIL `33`；對帳段「名目：凍存 `22`／現況 `33`」 |
| `4` | 現況之不能建築而仍配於原位者（塊 `F8` 之 `run` 之 `R1` 量·`WV_K929_6=off` ＝ 開工態之行為） | 退縮 `3.5 m` ⇒ `25` 宗（皆內接矩形不合格 ＋ 臨正街寬 `<` `3.50`）；另 `3` 宗已因閘一（藍影）不配地；`0 m` ⇒ `27` 宗 ＋ 閘一 `4` 宗。閘二（`K-9-12` 矩形容納）自 `2026-08-17` 裁定後迄未接線（本檔「🔧 進度表之現況更正：`K-9-17` 遞補迴圈已落地」節） |
| `5` | 改後之配地（harness·塊 `D1` 施後·殼無 `WV_`） | 見下表；三停機款（`§零-2` 項 `13`）皆⛔ 觸發；合併皆一輪即收斂（第二輪無新合併） |
| `6` | 二實作之對拍 | 發單側之倉外原型（`proto_k929_6.py`：以 `k917_should_drop` 之替身與外迴圈為之）與塊 `D1` 之生產實作，二退縮之配地逐宗 `G` 相符（`±0.011 ㎡`）；唯合併單元之名相異（原型以佔位者名、`D1` 以標的名·`K-9-29 四`） |
| `7` | 段三與街角選定 | 塊 `D1` 施後，段三（街角合併重試）之紀錄（`3.5 m` `18` 列／`0 m` `0` 列）、街角 winners、段三後之宗地，皆與開工態逐位同（段三之試算亦經入池閘） |
| `8` | 畫面對 harness（`verify/probes/probe_WG9345_screen.py parity <R> <退縮> on`） | 施後·殼無 `WV_`：`3.5` ⇒ `rc 0`（配地列 harness `36`／畫面 `35`·不符格 `0`）；`0.0` ⇒ `rc 0`（`37`／`36`·`0`）；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（`GB-186`·同開工態） |
| `9` | 合併單元佔位之讀法（`GB-193` 丁·`自誤 541`） | 將塊 `D1` 之「推進序在先者」改為相反之端（左 ⇔ 右）實跑：二退縮之配地宗集與不配地宗集皆同；`R3`（唯一右側推進之合併組 `G014`）之配地逐宗同；相異者僅左側推進之合併組所在之 `R5`／`R6`（`3.5 m`：`628-21(1)` `433.99 → 433.74` 等 `6` 列；`0 m` `12` 列）——左側推進者「投影序在前」與「推進序在先」同義，其相反之端非本單之讀法 |
| `10` | `run_all`（`WV_K929_6=off`·施 `D1` 之前一版〔無 `k*` 重錨〕·同一倉外路徑） | 與開工態之 `run_all` 全檔**逐位相同**（`cmp`） |
| `11` | `run_all`（施後·殼無 `WV_`·同一倉外路徑） | `64` 項：PASS `28`／FAIL `36`；對開工態之相異見 `§三` 工項二 `V-5`（發單側以同一倉外路徑二態實跑）；本單 `k*` 重錨之效另以施 `D1` 前一版（無重錨）隔離之：相異恰 `#17`／`#27`（FAIL → PASS）與 `#59`〜`#62`、`#64`（traceback 行號 `+4`） |

**`§一` 項 `5` 之表**（harness·配地宗數·`ΣG`〔㎡〕·街廓 − `ΣG`〔㎡〕）：

| 街廓 | `3.5 m` 改前 | `3.5 m` 改後 | `0 m` 改前 | `0 m` 改後 |
|---|---|---|---|---|
| `R1` | `5`·`1718.44`·`1175.11` | `4`·`1628.38`·`1265.17` | `5`·`1718.06`·`1175.49` | `4`·`1628.00`·`1265.55` |
| `R2` | `12`·`2588.22`·`1780.38` | `6`·`2098.23`·`2270.37` | `13`·`2533.52`·`1835.08` | `6`·`1953.75`·`2414.85` |
| `R3` | `13`·`2739.53`·`1467.27` | `5`·`2372.12`·`1834.68` | `14`·`2417.60`·`1789.20` | `6`·`2050.16`·`2156.64` |
| `R4` | `2`·`1978.78`·`1229.09` | `2`·`1978.78`·`1229.09` | `2`·`1978.78`·`1229.09` | `2`·`1978.78`·`1229.09` |
| `R5` | `9`·`2618.03`·`1532.18` | `6`·`2455.61`·`1694.60` | `10`·`2328.41`·`1821.80` | `6`·`2220.81`·`1929.40` |
| `R6` | `11`·`2347.57`·`1628.73` | `5`·`2071.22`·`1905.08` | `11`·`2347.57`·`1628.73` | `5`·`2071.22`·`1905.08` |
| 計 | `52` | `28` | `55` | `29` |

合併紀錄（`3.5 m`；`0 m` 另加 `R5` 之 `G007`〔`628-20(2)`＋`628-30(1)`＋`628-45(1)`·留置 `351.63`〕）：`R2` `G010`〔`628-40(1)`＋`628-43(1)`·留置 `292.95`〕；`R6` `G017`〔`628-21(1)`＋`628-22(1)`＋`628-23(1)`·留置 `433.99`〕；`R3` `G006`〔`628-47(1)`＋`628-48(1)`＋`628-49(2)`·留置 `365.82`〕；`R6` `G009`〔`628(2)`＋`628-1(2)`·入池〕；`R3` `G014`〔`628-28(1)`＋`628-29(1)`·入池〕。入池 `22` 宗（`3.5 m`·`15` 歸戶·重劃前面積 `2363.40 ㎡`）／`23` 宗（`0 m`·`16` 歸戶·`2513.70 ㎡`）。

---

## `§二`　KL 之語與射程

🔒 **KL 之裁（`2026-09-26 21:29`·發單側窗四十五·逐字）**：「是」——所答之【要你判斷】逐字：「同意依上述方式擬單落地嗎？落地後，新調配程式完成前，畫面將呈現這 22 宗暫不配地、面積留在調配池。（是／否）」；其【要改成】逐字：「1. 不能建築之宗，先與同街廓、同歸戶、地籍相鄰之土地合併試算。2. 合併後可建築者，留在原位。3. 仍不能建築者，不配地，由下一宗遞補；其面積留在調配池，待新調配程式調配。」
🔒 **該請示所附之事實之更正**（`自誤 540`／`541`）：其「各街廓之未配地面積增加 `90`〜`580 ㎡`」於 `3.5 m` 實為 `90.06`〜`489.99 ㎡`（`R4` `0`）；其附帶通知「本案成組者皆在左側推進」為偽（`R3` `G014` 係右側推進），惟「此讀法不生差異」於本案成立（`§一` 項 `9`）。二者⛔ 動 KL 所答之方式。
🔒 **本單之讀法**（已以通知呈 KL·`GB-193`）：「不能建築」＝ 內接矩形（`K-9-12`）、最小建築面積（`v3` ⑨⑩·使用者有輸入時）任一不合格，或臨正街寬 `S` `<` 畸零地寬（`K-9-33`·`S ＝` 畸零地寬合格）；街角第 `1` 宗免（`K-9-12-e`／`K-9-33`）；街廓一側之末位不能建築者亦不配地（其位空出即入池·`K-9-13`）；「相鄰」＝ 地籍共邊，可經同歸戶之宗連成一組（同前置合併之判·`k6_merge_groups`）；合併後之單元以標的宗（個別 `G` 最大）為名、佔推進序在先者之位。

🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項二之生產碼 `commit` 推入主線之放行，CC 將其逐字載入報告；**無之 ⇒ 工項二之驗畢後停於推送前，於對話請示 KL**。所答之【要你判斷】逐字：「同意將『不能建築之宗先與同街廓同歸戶相鄰土地合併試算、仍不能建築者不配地而留在調配池』之程式（畫面與驗證二路徑）推入主線嗎？（是／否）」

🔒 **逐筆放行清單**：本批動生產碼者恰 **`1`** 筆（工項二）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `app.py`（`k917_should_drop` 二處·`k917_note_drop`·新函式 `k929_6_enabled`／`k929_6_unbuildable`／`k929_6_fixpoint`／`_k929_6_screen_gate`·`f3_screen_stepg_run` 之首與末·`K6B_SCREEN_TRIAL_KEYS`·`_WF_NS_NAMES`·成果區之合併紀錄）；`verify/stepg_pipeline.py`（`run_step_g` 之入池閘）；`verify/run_verification.py`（`K_STAR_EXPECT` 之二情境 ＋ 註解 `4` 列） | 塊 `D1` | 🔴 有（`§一` 項 `5` 之表） |

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至主線；`(b)` 工項二之 `push` 以 `§二` 之放行為條件；`(c)` 工項五於 KL 本機之主 checkout·⛔ `commit`；`(d)` ⛔ 及其他任何生產碼、任何他錨。
🔒 **旗標**：`WV_K929_6`（未設／`on` ⇒ 本批之行為；`off` ⇒ 逐位回到本批前之行為·`§一` 項 `10`）。KL 本機之介面⛔ 設之。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-349_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-349 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F8` 入倉（主線·零生產碼）

塊 `F8` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9349_k9296.py`（**新檔**）。`commit` 訊息逐字 `W-G.9-349 工項一：量測器 F8（入池閘）入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項二　塊 `D1`：閘二與臨正街寬之接線 ＋ `K-9-29 六` 入池閘 ＋ `k*` 經驗錨之重錨（🔴 生產碼·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9349_k9296.py selftest <repo>` ⇒ **`rc 1`**（末列含 `受詞缺`）。
2. `python verify/probes/probe_WG9349_k9296.py wiring <repo>` ⇒ **`rc 1`**（`W1`〜`W8` 皆紅）。
3. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D1` 依圍欄之逐列索引抽出為 `<O>\D1.diff`、對拍 `§五-1` 後，`git apply --check <O>\D1.diff` ⇒ 過；`git apply <O>\D1.diff`；`git hash-object app.py` ＝ `8672b00d9b76f77c0cb3b9ca1487a42486d53653`、`git hash-object verify/stepg_pipeline.py` ＝ `21b9cb341a17b17f05c4ce487c26b40ccdc32747`、`git hash-object verify/run_verification.py` ＝ `4d83d2c5a32c364021f26679a58172e1f1554dab`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-349 工項二：閘二與臨正街寬之接線（K-9-12／K-9-13／K-9-33）＋ K-9-29 六 入池閘（同歸戶相鄰合併試算）＋ k* 經驗錨之重錨（入池閘·逐塊歸因）🔴 生產碼`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9349_k9296.py selftest <repo>`；`… wiring <repo>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`wiring` 之 `M1`〜`M4` 皆「轉紅」 |
| `V-2` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5`；`… run <repo> 0.0`；另於**該呼叫之環境**設 `WV_K929_6=off` 跑 `… run <repo> 3.5` | 前二者 **`rc 0`**、`R1` 之數 ＝ `0`、合併紀錄 `3.5 m` `5` 列／`0 m` `6` 列（結果：留置 `3`／`4`、入池 `2`／`2`）、逐街廓之宗數與 `ΣG` ＝ `§一` 項 `5` 之表之改後欄；第三者 **`rc 0`**、`R1` 之數 ＝ **`25`**、`R3`「無」 |
| `V-3` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35.json`；同 `0.0` | 皆 **`rc 0`**、配地列不符格 `0`；配地列 harness／畫面 ＝ `36／35`（`3.5`）、`37／36`（`0.0`）；`Z` ＝ `[('harness', 'R1-抵費地-2')]` |
| `V-4` | `python verify/probes/probe_WG9348_harvest_key.py <repo>`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9330_wfns_ast.py <repo>` | 前二者 **`rc 0`**（末列 `⇒ 紅 []；rc 0`）；第三者 **`rc 0`**·`43`／`43`／`42` |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log` | 項數同（`64`）；PASS `31 → 28`、FAIL `33 → 36`；**相異項恰 `28`**：`#14`／`#15`／`#16`／`#24`／`#25`／`#26`（v3 之 G 值·滑池槽·J 表）、`#39`／`#40`（W-D.3）、`#41`〜`#46`、`#48`（W-D.4）、`#53`（F.0 釋池對象·名目改）、`#58`（W-F F.0·其停由錨值不符改為錨鍵「未被評估」）——以上狀態 FAIL → FAIL；`#17`／`#27`（`k*` 經驗錨·名目改為本單之錨·PASS → PASS）；`#32`（v3 A 逐宗全查·名目之列數 `107` → `57`·PASS → PASS）；`#59`〜`#62`、`#64`（FAIL → FAIL·本體之異**恰為** `verify/run_verification.py` 之 traceback 行號 `+4`·CC 逐項以 `diff` 出艙其異列）；**✅→🔴 恰 `3`** ＝ `#49`（F.0-pre 雙軌錨）、`#50`（F.0-pre 公設軌 8 群）、`#55`（W-D.4 遞補錨 R6）——皆 W-F／W-D.4 之凍存錨（`W-G.9-348 §二` 之射程之裁：⛔ 重錨）；🔴→✅ `0`；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／33 → 22／36` |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（`§二` 之放行成立後·與驗為分開之呼叫）：`git push origin HEAD:wip/s1-endpart`。

### 工項三　攢批登記 ＋ 更正附註 ＋ 待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `E2`／`G2`／`R1`／`P3` 各依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位**附於**：
- `E2` ⇒ `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；
- `G2` ⇒ `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；
- `R1` ⇒ `docs/reports/W-G.9-348R_驗證器二處更正與攢批登記_執行報告.md` 之末；
- `P3` ⇒ `CLAUDE.md` 之末。

四檔之刪除欄皆 `0`、改前全檔為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-349 工項三：攢批登記（自誤 538〜541·GB-192／GB-193）＋ W-G.9-348R 之更正附註 ＋ 待落地清單之更新 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項四　執行報告入倉（主線·新檔 `docs/reports/W-G.9-349R_入池閘與閘二接線_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`13` 之三值；③ 工項二之前置與驗之全部出艙（`F8` 三子命令之全文、`parity` 二份之 `rc` 與末三列、`runall` 對拍之全文、相異項之本體異列）；④ 六塊之實得（bytes／`sha256`）與四檔之改前改後 bytes；⑤ `§二` 之放行（KL 之逐字或請示之經過）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-349 工項四：執行報告入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項五　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（根之來源檔為未追蹤檔·⛔ 計）。
2. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
3. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項四 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `8672b00d9b76f77c0cb3b9ca1487a42486d53653`。
任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項四之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項零／一／三／四 逐檔 **`0`**；工項二 ＝ `app.py` **`3`**、`verify/stepg_pipeline.py` **`1`**、`verify/run_verification.py` **`2`**（＝ 塊 `D1`） |
| `2` | 生產碼 `34` 檔對 `88dc179` | 相異恰 **`3`**（`app.py` ＝ `8672b00d…`、`verify/stepg_pipeline.py` ＝ `21b9cb34…`、`verify/run_verification.py` ＝ `4d83d2c5…`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4` | 四檔之 bytes | `docs/reports/W-G.9波_claude.ai側自誤登記.md` `1058035 → 1064143`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1009475 → 1013686`；`docs/reports/W-G.9-348R_驗證器二處更正與攢批登記_執行報告.md` `13543 → 14638`；`CLAUDE.md` `266266 → 268881`；四者改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`30`**；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 541 537 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 541 537` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `526`／`MAX` `541`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `186`／`193`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `45`／`48`／`[44, 47]`（缺號集皆 ＝ 開工態） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·`43`／`43`／`42` |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9349_k9296.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之替身 ＋ 塊 `F8` ＋ 塊 `D1` ＋ 四塊 ＋ 報告之替身·五 `commit`）並實跑閘 `1`、`2`、`3`、`4`、`6`〜`13` ⇒ 見 `§五-1` 項 `11`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D1` | `26709` B·`sha256` `7671a7cc5400328796fa5fd70577ccefa6a5123591c7b70498fd759079cf406b`·`451` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F8` | `20615` B·`sha256` `bc0dd808c02609f413634c01124f4bafabd82586f02b8a693be122209f04be0c`·`403` 列（圍欄內全文·末附換行） |
| `4` | 塊 `E2` | `6108` B·`sha256` `8af97b3e95c45cf49817aee5fa281ecfd27fceb9a0d89ab2b8723a944362b333`·`42` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1058035` B）之末後，期末 ＝ `1064143` B |
| `5` | 塊 `G2` | `4211` B·`sha256` `3056bec5945a32812b7d1336a412c1724d9d2b16ea8f422068e0c14aee4cf0d2`·`28` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1009475` B）之末後，期末 ＝ `1013686` B |
| `6` | 塊 `R1` | `1095` B·`sha256` `def690276ad01d2294587e63bce32db0a5071b148ae723f1328f08ec2865fe79`·`9` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9-348R_驗證器二處更正與攢批登記_執行報告.md`（`13543` B）之末後，期末 ＝ `14638` B |
| `7` | 塊 `P3` | `2615` B·`sha256` `2dfa9f71fc7c9447c5408a87e0b579b16273b1125e53b1d776fe5838db111d52`·`17` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`266266` B）之末後，期末 ＝ `268881` B |
| `8` | 施 `D1` 後之 blob | `app.py` `8672b00d9b76f77c0cb3b9ca1487a42486d53653`（`1506634` B）；`verify/stepg_pipeline.py` `21b9cb341a17b17f05c4ce487c26b40ccdc32747`（`118225` B）；`verify/run_verification.py` `4d83d2c5a32c364021f26679a58172e1f1554dab`（`101887` B）（開工態 `f4c47af6…`／`eb557b4b…`／`ed488bae…`） |
| `9` | `F8` 之二態 | 開工態 `selftest`／`wiring` 皆 `rc 1`；施 `D1` 後皆 `rc 0` |
| `10` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十五實跑：🔴 機械 `0` 項／🟡 提示 `9` 項——`P-2` `:1102`（塊 `E2` 之 `自誤 538`「形」段·所引係被登記之 `W-G.9-325` 之逐字、⛔ 本單之出艙計數 ⇒ **具名豁免**）、`P-4` `:47`／`:71`／`:143`／`:180`（`§零-2` 停機款、`§一` 態錨、工項二之驗、`§四` 收工閘之表頭·其箭頭之座標系皆為「改前〔`88dc179`〕→ 改後〔工項二之 `commit`〕」，表內自載 ⇒ **具名豁免**）、`P-4` `:596`（塊 `D1` 之碼註·其 `⇒` 為合併試算之處理序，註內自載 ⇒ **具名豁免**）、`P-4` `:690`（塊 `F8` 之 docstring·其 `⇒` 為「旗標 on／off ⇒ 期值」，同段自載 ⇒ **具名豁免**）、`P-4` `:1132`（塊 `E2` 之 `自誤 541`·其「左側／右側」係推進側〔`FRONT_LINE` 之 `p1`／`p2`〕，同則之標題具名 ⇒ **具名豁免**）、`P-4` `:1151`（塊 `G2` 之 `GB-192`·其序為同一工作階段「先 `0 m`、後 `3.5 m`」之操作時序，同則之標題具名 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `18054`–`25633`）⇒ `rc 0` |
| `11` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`88dc179` ＋ 五 `commit`）：閘 `1` 工項二 `297／3`、`32／1`、`6／2`（`app.py`／`verify/stepg_pipeline.py`／`verify/run_verification.py`·增／刪），餘逐檔刪 `0`；閘 `2` 相異恰 `3`；閘 `3` `CR` 合計 `0`（`10` 檔·判別力 `12308`）；閘 `4` 四檔如 `§四`（嚴格前綴）；閘 `6`〜`13` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `43`／`43`／`42`；`F5`「app 側宿主 ＝ f3_screen_stepg_run」；`F6`、`F7`、`F8` 二子命令之末列 `⇒ 紅 []；rc 0`）；跑畢追蹤檔之變動 `0` |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零、一、三、四 ⇒ 逕行 `push` 主線；工項二 ⇒ 依 `§二` 之放行、驗皆符後推主線；工項五 ⇒ KL 本機之主 checkout。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D1`（`git apply` 之差異·三檔）

````diff
diff --git a/app.py b/app.py
index f4c47af..8672b00 100644
--- a/app.py
+++ b/app.py
@@ -9388,6 +9388,12 @@ def k917_should_drop(res, is_corner_first, has_successor, chain_side, blk_label,
     """
     _v = str(((res or {}).get("_lg_cols") or {}).get("驗_B藍影", "") or "").strip()
     if _v != "不合格":
+        # 🆕 `W-G.9-349`（`K-9-13`：不得建築者不配地·由下一宗遞補）：閘二（`K-9-12` 內接矩形）、
+        #   最小建築面積（`v3` ⑨⑩）與臨正街寬（`K-9-33`）之接線。街角第 `1` 宗免（`K-9-12-e`／`K-9-33`）。
+        #   🔒 末位（無後繼）亦不配地——其位空出即入池（`K-9-13`）；閘一之末位⛔ 受本款影響（仍 loud）。
+        #   🔒 旗標 `WV_K929_6=off` ⇒ 本款⛔ 執行（逐位同本批前）。
+        if (not is_corner_first) and k929_6_enabled() and k929_6_unbuildable(res):
+            return True, "不合格"
         return False, _v
     if is_corner_first:
         raise RuntimeError(
@@ -9395,6 +9401,10 @@ def k917_should_drop(res, is_corner_first, has_successor, chain_side, blk_label,
             f"竟為閘一『不合格』——其分配範圍係 winner 之 `G` 所單獨決定、⛔ 受遞補影響"
             f"（構造保證）⇒ 此情狀⛔ 得發生（`GB-104` 之 loud 斷言）。")
     if not has_successor:
+        # 🆕 `W-G.9-349`：閘二接線後，前宗之不配地得使末位遞補為受藍影檢之宗（連鎖）⇒ 末位之閘一不合格
+        #   依 `K-9-13` 不配地（其位空出即入池）；旗標 off ⇒ 仍 loud（本批前之斷言）。
+        if k929_6_enabled():
+            return True, _v
         raise RuntimeError(
             f"🔴 `K-9-9 六`：街廓 {blk_label} {chain_side} 側之末位 {pid!r} 遭閘一剔除而"
             f"**⛔ 後繼可遞補** ⇒ 候選耗盡。正典逐字「必然產生配餘地……⛔ 會發生『塞不下』」"
@@ -9409,13 +9419,216 @@ def k917_note_drop(blk_label, chain_side, pid, res, tp=None):
        該宗既不進 `g_rows`，其幾何即歸池 ⇒ **⛔ 另設「入池」之碼**（⛔ 第二份定義）。
     🔒 **⛔ 超配**（`K-9-11 三`）：本函式⛔ 動任何宗之 `G`。
     """
-    K917_DROPPED.setdefault((str(blk_label), str(chain_side)), []).append({
+    _rec = {
         "暫編地號": pid,
         "G(㎡)": round(float((res or {}).get("G", 0.0) or 0.0), 4),
         "宗地寬度(m)": round(float((res or {}).get("_宗地寬度", 0.0) or 0.0), 4),
         "驗_B藍影": str(((res or {}).get("_lg_cols") or {}).get("驗_B藍影", "")),
         "歸戶": (tp or {}).get("歸戶鍵Gxxx", (tp or {}).get("歸戶", "")),
-    })
+    }
+    # 🆕 `W-G.9-349`：不配地之由（旗標 on 始記·off ⇒ 紀錄逐位同本批前）
+    if k929_6_enabled():
+        _why = (["藍影"] if _rec["驗_B藍影"].strip() == "不合格" else []) + k929_6_unbuildable(res)
+        _rec["不配地由"] = "、".join(_why) if _why else "—"
+    K917_DROPPED.setdefault((str(blk_label), str(chain_side)), []).append(_rec)
+
+
+# ══════════ 🆕 `W-G.9-349`：`K-9-29 六`（五級之入池閘）＋ 閘二之接線（`K-9-12`／`K-9-13`／`K-9-33`）══════════
+#   KL 放行 `2026-09-26`（發單側窗四十五·附圖）。正典：`K-9-29 四／五／六`、`K-9-13`、`K-9-33`；
+#   規格 ＝ `docs/specs/調配階段_泛用規格_v1.md` 步 `1`（「G < MinA」讀為不能分配·`2026-09-23` 通知三）。
+#   🔒 模組層·⛔ 讀 `st`／session；一切外部量由參數注入（harness ＝ `verify/stepg_pipeline.py` 之 `run_step_g`；
+#      畫面 ＝ `f3_screen_stepg_run`）。旗標 `WV_K929_6`：未設／`on` ⇒ 啟用；`off` ⇒ 逐位回到本批前之行為。
+K929_6_ENV = "WV_K929_6"
+
+
+def k929_6_enabled():
+    """入池閘之旗標：未設或空 ⇒ `True`；`on` ⇒ `True`；`off` ⇒ `False`；其他值 ⇒ `RuntimeError`（⛔ 靜默退回）。"""
+    import os as _os_k9296
+    _v = _os_k9296.environ.get(K929_6_ENV)
+    _s = '' if _v is None else str(_v).strip().lower()
+    if _s in ('', 'on'):
+        return True
+    if _s == 'off':
+        return False
+    raise RuntimeError(
+        f"🔴 [K-9-29 六] 環境變數 {K929_6_ENV} ＝ {_v!r}：只接受 on／off（或未設）——⛔ 靜默退回預設")
+
+
+def k929_6_unbuildable(res):
+    """回該宗之不能建築項（`list`·空 ⇒ 無）：`內接矩形`（`K-9-12`·`驗_A幾何`）、`最小建築面積`（`v3` ⑨⑩·`驗_C面積`）、
+    `臨正街寬`（`K-9-33`：`S < 畸零地寬`；`S ＝ 畸零地寬` 合格·題三）。
+    🔒 只讀 `_lot_gate` 之落欄與 `res` 之 `S_raw`；「不適用」「無從判定」⛔ 當不合格；`W`／`S` 取不到 ⇒ 臨正街寬⛔ 判。"""
+    _lg = (res or {}).get("_lg_cols") or {}
+    _out = []
+    if str(_lg.get("驗_A幾何", "") or "").strip() == "不合格":
+        _out.append("內接矩形")
+    if str(_lg.get("驗_C面積", "") or "").strip() == "不合格":
+        _out.append("最小建築面積")
+    try:
+        _W = float(_lg.get("驗_A_W"))
+        _S = float((res or {}).get("S_raw", (res or {}).get("S")))
+    except (TypeError, ValueError):
+        _W = _S = None
+    if _W is not None and _S is not None and _S + 1e-9 < _W:
+        _out.append("臨正街寬")
+    return _out
+
+
+def k929_6_fixpoint(build_parcels, trial, own_map, pre_price_by_zone, front_lines, *, max_rounds=None):
+    """`K-9-29 六`（入池閘）之不動點——`W-G.9-349`。
+
+    參數
+      build_parcels      原位次之輸入宗地（⛔ 改寫；合併以深拷貝之新 dict 取代）。
+      trial              `trial(build) -> (rows, dropped, payload)`：以所給之 build 跑配地（入池閘⛔ 再入）；
+                         `rows` ＝ G 值列；`dropped` ＝ 本趟之 `{(街廓, 側): [不配地紀錄]}`；`payload` 原樣回傳。
+      own_map            `{原地號: gid}`（`t8_ownership_map`）。
+      pre_price_by_zone  `{重劃前地價區段: 單價}`（`a′` 之 `p`）。
+      front_lines        `{街廓: {"p1": (x, y), "p2": (x, y)}}`（投影序之軸）。
+    回傳 `(build_final, (rows, dropped, payload) 之末趟, log)`；末趟即以 `build_final` 所跑者。
+
+    規則（`K-9-29 四／五／六`）：
+      ① 不配地之宗 `u`，取其同街廓、同歸戶、地籍共邊相鄰（可經同歸戶之宗連成）之宗之連通分量 `C`（含原位可配者）；
+      ② `|C| ≥ 2` 且 `C`（以原宗計）未試過 ⇒ 合併：標的宗 ＝ 個別 `G` 最大者（並列取暫編字典序最小）；
+         其餘各以 `a′ ＝ a × p(自身) ÷ p(標的)` 併入（`K-9-29 三`）；合併後之單元佔推進序在先者之位
+         （左側推進 ＝ 投影序最小者；右側推進 ＝ 投影序最大者）；
+      ③ 重跑；合併後可配 ⇒ 留置；仍不配地 ⇒ 全部入池（其地即池）；
+      ④ 反覆至無新合併。
+    停機（`RuntimeError`·⛔ 靜默略過）：合併組含街角第 `1` 宗；合併組跨左右推進；投影軸、地價取不到；
+      含原位可配者之合併單元終不配地（`K-9-29 六`「一達一未達者於閘內併入（不進池）」之反例·【未裁】）；
+      逾 `max_rounds`（預設 ＝ 宗數 ＋ `1`）未收斂。
+    """
+    import copy as _cp_k9296
+    from shapely.geometry import Polygon as _Pg_k9296
+    from shapely.ops import unary_union as _uu_k9296
+
+    def _pid(t):
+        return str(t.get('暫編地號'))
+
+    def _gid(t):
+        return str((own_map or {}).get(str(t.get('原地號', '')), '') or '')
+
+    def _a(t):
+        if '分攤登記面積_m2' in t:
+            return float(t.get('分攤登記面積_m2', 0) or 0) + float(t.get('面積_m2', 0) or 0)
+        return float(t.get('面積_m2', 0) or 0)
+
+    def _p(t):
+        _z = t.get('重劃前地價區段')
+        if not _z or _z not in (pre_price_by_zone or {}):
+            raise RuntimeError(
+                f"🔴 [K-9-29 六 a′] {_pid(t)!r} 之重劃前地價區段 {_z!r} 不在重劃前地價表 ⇒ 停機；⛔ 退 a′ ＝ a")
+        _v = float(pre_price_by_zone[_z] or 0)
+        if _v <= 0:
+            raise RuntimeError(f"🔴 [K-9-29 六 a′] 區段 {_z!r} 之單價 {_v!r} ≤ 0 ⇒ 停機")
+        return _v
+
+    build = list(build_parcels or [])
+    geom = {_pid(t): _Pg_k9296(t['polygon_coords']).buffer(0) for t in build}
+    members = {_pid(t): [_pid(t)] for t in build}
+    tried = set()
+    log = []
+    cap = int(max_rounds) if max_rounds else (len(build) + 1)
+    for _rnd in range(1, cap + 1):
+        out = trial(build)
+        rows, dropped = out[0], out[1]
+        by = {_pid(t): t for t in build}
+        side_of, g_of, corner_first, drops = {}, {}, set(), []
+        for _r in rows or []:
+            _k = str(_r.get('暫編地號'))
+            side_of[_k] = _r.get('推進側別')
+            g_of[_k] = float(_r.get('G(㎡)') or 0)
+            if str(_r.get('驗_宗序', '')) == '街角第1宗':
+                corner_first.add(_k)
+        for (_blk_d, _side_d), _lst in sorted((dropped or {}).items()):
+            for _e in _lst:
+                _k = str(_e.get('暫編地號'))
+                side_of[_k] = _side_d
+                g_of[_k] = float(_e.get('G(㎡)') or 0)
+                drops.append((str(_blk_d), _k))
+        drop_ids = {k for _, k in drops}
+        plans, used = [], set()
+        for _blk_u, u in sorted(set(drops)):
+            if u not in by or u in used:
+                continue
+            _g = _gid(by[u])
+            if not _g:
+                continue
+            _bl = by[u].get('所屬街廓')
+            comp, _stk = {u}, [u]
+            while _stk:
+                _x = _stk.pop()
+                for _y in sorted(by):
+                    if _y in comp or by[_y].get('所屬街廓') != _bl or _gid(by[_y]) != _g:
+                        continue
+                    if k6_shares_segment(geom[_x], geom[_y])[0]:
+                        comp.add(_y)
+                        _stk.append(_y)
+            if len(comp) < 2:
+                continue
+            _orig = frozenset(_m for _c in comp for _m in members[_c])
+            if _orig in tried:
+                continue
+            if comp & corner_first:
+                raise RuntimeError(
+                    f"🔴 [K-9-29 六]【未裁】街廓 {_bl} 之合併組 {sorted(_orig)} 含街角第 1 宗 "
+                    f"{sorted(comp & corner_first)} ⇒ 停機（⛔ 自裁併入街角地與否）")
+            _sides = {side_of.get(_c) for _c in comp}
+            if len(_sides) != 1 or None in _sides:
+                raise RuntimeError(
+                    f"🔴 [K-9-29 六]【未裁】街廓 {_bl} 之合併組 {sorted(_orig)} 之推進側 {sorted(map(str, _sides))} "
+                    "非單一 ⇒ 停機（⛔ 自裁「投影序在前者」）")
+            _side = next(iter(_sides))
+            _fl = (front_lines or {}).get(_bl) or {}
+            if _fl.get('p1') is None or _fl.get('p2') is None:
+                raise RuntimeError(f"🔴 [K-9-29 六] 街廓 {_bl} 之 FRONTLINE 取不到 ⇒ 停機（投影序無從定）")
+            _ord = [_pid(t) for t in _projection_order([by[_c] for _c in comp], _fl['p1'], _fl['p2'])]
+            _first = _ord[0] if _side == 'left' else _ord[-1]
+            _tgt = min(comp, key=lambda _c: (-g_of.get(_c, 0.0), _c))
+            _q = {_c: _a(by[_c]) * (_p(by[_c]) / _p(by[_tgt])) for _c in sorted(comp) if _c != _tgt}
+            plans.append(dict(comp=comp, orig=_orig, bl=_bl, side=_side, gid=_g, first=_first, tgt=_tgt,
+                              q=_q, keep=bool(comp - drop_ids)))
+            used |= comp
+        if not plans:
+            _fin = {str(_r.get('暫編地號')) for _r in rows or []}
+            for _row in log:
+                _u = _row['標的']
+                _row['結果'] = '留置' if _u in _fin else ('入池' if _u in drop_ids else '續併')
+                if _row['結果'] == '入池' and _row['含原位可配']:
+                    raise RuntimeError(
+                        f"🔴 [K-9-29 六]【未裁】合併組 {_row['成員']}（含原位可配之宗）合併後仍不配地 ⇒ 停機"
+                        "（「一達一未達者於閘內併入（不進池）」之反例·⛔ 自裁）")
+            return build, out, log
+        for _pl in plans:
+            _t = by[_pl['tgt']]
+            _unit = _cp_k9296.deepcopy(_t)
+            _unit['面積_m2'] = float(_unit.get('面積_m2', 0) or 0) + sum(_pl['q'].values())
+            if _pl['first'] != _pl['tgt']:
+                _f = by[_pl['first']]
+                for _k in ('polygon_coords', 'centroid_x', 'centroid_y'):
+                    if _k in _f:
+                        _unit[_k] = _cp_k9296.deepcopy(_f[_k])
+            _unit['入池閘併入'] = sorted(_pl['orig'])
+            _nb = []
+            for t in build:
+                _k = _pid(t)
+                if _k == _pl['first']:
+                    _nb.append(_unit)
+                elif _k not in _pl['comp']:
+                    _nb.append(t)
+            build = _nb
+            by = {_pid(t): t for t in build}
+            geom[_pl['tgt']] = _uu_k9296([geom[_c] for _c in _pl['comp']]).buffer(0)
+            members[_pl['tgt']] = sorted(_pl['orig'])
+            for _c in _pl['comp']:
+                if _c != _pl['tgt']:
+                    geom.pop(_c, None)
+                    members.pop(_c, None)
+            tried.add(_pl['orig'])
+            log.append({'輪': _rnd, '街廓': _pl['bl'], '推進側': _pl['side'], '歸戶': _pl['gid'],
+                        '成員': sorted(_pl['orig']), '標的': _pl['tgt'], '佔位': _pl['first'],
+                        '併入量(a′)': round(sum(_pl['q'].values()), 4), 'a 合計': round(_a(_unit), 4),
+                        '含原位可配': _pl['keep'], '結果': '—'})
+    raise RuntimeError(f"🔴 [K-9-29 六] 逾 {cap} 輪未收斂 ⇒ 停機（⛔ 截斷）")
 
 
 def _corner_band_geom(block_poly, d_hat, front_p1, allocation_dir, buf, side,
@@ -15075,6 +15288,8 @@ _WF_NS_NAMES = [
     # 🆕 `W-G.9-269` `c1`：`K-9-17` 遞補迴圈之三名（引擎 `verify/stepg_pipeline.py` 經 `ns` 消費）。
     #   🛑 漏列即 **app 生產路徑 KeyError**（`fixture_wf_ns_wiring` 之受詞）。
     "k917_should_drop", "k917_note_drop",
+    # 🆕 `W-G.9-349`：`K-9-29 六` 入池閘之三名（引擎 `verify/stepg_pipeline.py` 之 `run_step_g` 經 `ns` 消費）。
+    "k929_6_enabled", "k929_6_fixpoint", "K917_DROPPED",
     # 🆕 B-5（plan v3 §四·D-3 寬度制）：平移切帶範圍多邊形**即算即用**之單一真相源。
     #   ⚠️ 走 ns 函式、**不**存 session 新鍵——session 資料走 `_WFSessionShim`，
     #      且 harness（run_verification）從不算負擔範圍，存鍵在 harness 路徑必缺。
@@ -16204,8 +16419,19 @@ def f3_screen_stepg_run(st, *,
         classified_blocks,
         post_price_by_block,
         pre_price_by_zone,
-        sb_rows_by_label):
+        sb_rows_by_label,
+        _k929_6_inner=False):
     """畫面「🧮 執行 G 值迭代計算」配地區（_btn_clicked or _auto_recalc）之本體（W-G.9-345 工項三·自 main() 原封抽出·零行為變更）。"""
+    # 🆕 `W-G.9-349`（`K-9-29 六` 入池閘·KL 放行 `2026-09-26`）：旗標 on 且非試算趟 ⇒ 先以試算趟（代理 st）求末態之
+    #   build，再以之跑本體（真 st）；合併紀錄於本體末與 `f3_G_values` 同寫（`f3_k929_6_log`）。旗標 off ⇒ 本段⛔ 執行。
+    _k929_6_log = None
+    if (not _k929_6_inner) and k929_6_enabled():
+        build_parcels, _k929_6_log = _k929_6_screen_gate(st, dict(
+            B_value=B_value, C_for_calc=C_for_calc, _auto_recalc=_auto_recalc, _btn_clicked=_btn_clicked,
+            _new_params=_new_params, _param_key=_param_key, _tab6_burden=_tab6_burden,
+            block_meta_by_label=block_meta_by_label, build_parcels=build_parcels,
+            classified_blocks=classified_blocks, post_price_by_block=post_price_by_block,
+            pre_price_by_zone=pre_price_by_zone, sb_rows_by_label=sb_rows_by_label))
     if _auto_recalc and not _btn_clicked:
         st.info("🔄 偵測到街角地變動，自動重算 G 值…")
     g_rows = []
@@ -16234,6 +16460,7 @@ def f3_screen_stepg_run(st, *,
     #   狀態機閉合：成功時末端寫回二產物並清 `f3_g_needs_rerun`。
     st.session_state.pop('f3_G_values', None)
     st.session_state.pop('f3_G_trace', None)
+    st.session_state.pop('f3_k929_6_log', None)   # 🆕 `W-G.9-349`：同二產物之生命週期
     st.session_state['f3_g_needs_rerun'] = True
     _params_for_g = dict(st.session_state.get(_param_key, _new_params))
 
@@ -17654,6 +17881,9 @@ def f3_screen_stepg_run(st, *,
 
     st.session_state['f3_G_values'] = g_rows
     st.session_state['f3_G_trace'] = detail_trace
+    # 🆕 `W-G.9-349`：入池閘之合併紀錄（旗標 off 或試算趟 ⇒ ⛔ 寫）
+    if _k929_6_log is not None:
+        st.session_state['f3_k929_6_log'] = _k929_6_log
     # 🚨 Phase 9.12 Issue 4：清除 rerun flag（G 值已重新計算完成）
     st.session_state.pop('f3_g_needs_rerun', None)
     _n_offset = sum(1 for r in g_rows if r.get('推進側別') == '抵費地')
@@ -17767,6 +17997,8 @@ K6B_SCREEN_TRIAL_KEYS = (
     'f3_k94_baseline_touch', 'f3_offset_fragments_merged', 'f3_stage2_placed', 'f3_wd2_pool_diag',
     # 本批所增（1）
     'f3_corner_cand_diag',
+    # 🆕 `W-G.9-349`：入池閘之合併紀錄（配地本體所寫）
+    'f3_k929_6_log',
 )
 K6B_SCREEN_STAGE3_KEYS = ('f3_k6b_stage3_temp', 'f3_k6b_stage3_build', 'f3_k6b_stage3_fp')
 # 🆕 `W-G.9-346`：段三於街角選位（首趟／試算趟）後自 session 讀回之鍵（⊂ K6B_SCREEN_TRIAL_KEYS）；
@@ -18050,6 +18282,56 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
     return {'temp': temp2, 'build': build2, 'log': log, 'order': order, 'ran': True}
 
 
+def _k929_6_screen_gate(st, g_kwargs):
+    """🆕 `W-G.9-349`：入池閘之畫面入口（`f3_screen_stepg_run` 之首·旗標 on 且非試算趟時）。
+    試算趟 ＝ `f3_screen_stepg_run(代理 st, …, _k929_6_inner=True)`（吃畫面即時之地價·⛔ 借用 harness）；
+    隔離 ＝ 試算前存 `K6B_SCREEN_TRIAL_KEYS` 與 `K917_DROPPED`、試算後復。回 `(build_final, log)`。
+    試算中止或 `k929_6_fixpoint` 停機 ⇒ `st.error` ＋ `st.stop()`（loud·⛔ 退回未閘之 build）。"""
+    import copy as _cp_k9296s
+    import contextlib as _cl_k9296s
+    import io as _io_k9296s
+    _ss = st.session_state
+    _saved = {k: _cp_k9296s.deepcopy(_ss[k]) for k in K6B_SCREEN_TRIAL_KEYS if k in _ss}
+    _k917_saved = _cp_k9296s.deepcopy(K917_DROPPED)
+
+    def _trial(_b):
+        K917_DROPPED.clear()
+        _px = _K6BTrialSt(st)
+        try:
+            with _cl_k9296s.redirect_stdout(_io_k9296s.StringIO()):
+                f3_screen_stepg_run(_px, **dict(g_kwargs, _auto_recalc=False, _btn_clicked=True,
+                                                build_parcels=_b, _k929_6_inner=True))
+        except _K6BTrialDone:
+            pass
+        except _K6BTrialStop as _e_t:
+            raise RuntimeError(
+                f"🔴 [K-9-29 六·畫面] 試算（配地）中止：{_px.msgs[-1:]}（⛔ 退回未閘之配地）") from _e_t
+        if 'f3_G_values' not in _ss:
+            raise RuntimeError("🔴 [K-9-29 六·畫面] 試算（配地）未產出 G 值表（⛔ 退回未閘之配地）")
+        return list(_ss.get('f3_G_values') or []), _cp_k9296s.deepcopy(dict(K917_DROPPED)), None
+
+    _err = None
+    try:
+        _bf, _last, _log = k929_6_fixpoint(
+            g_kwargs['build_parcels'], _trial, _ss.get('t8_ownership_map', {}) or {},
+            g_kwargs['pre_price_by_zone'], _ss.get('f3_cad_front_lines', {}) or {})
+    except RuntimeError as _e_g:
+        _err = str(_e_g).split("\n")[0][:500]
+    finally:
+        for _k in K6B_SCREEN_TRIAL_KEYS:
+            if _k in _saved:
+                _ss[_k] = _saved[_k]
+            else:
+                _ss.pop(_k, None)
+        K917_DROPPED.clear()
+        K917_DROPPED.update(_k917_saved)
+    if _err is not None:
+        st.error(_err)
+        st.stop()
+        raise RuntimeError(_err)
+    return _bf, _log
+
+
 # ============ 主程式 ============
 def main():
     st.title("🏗️ 市地重劃地價估算系統")
@@ -24064,6 +24346,18 @@ def main():
                         use_container_width=True, hide_index=True,
                     )
 
+                    # 🆕 `W-G.9-349`：入池閘（`K-9-29 六`）之合併紀錄——同歸戶相鄰合併試算之成否（留置／入池）
+                    _k929_6_log_v = st.session_state.get('f3_k929_6_log')
+                    if _k929_6_log_v is not None:
+                        with st.expander(f"🔗 K-9-29 六：不能建築之宗之同歸戶相鄰合併試算（{len(_k929_6_log_v)} 列）",
+                                         expanded=bool(_k929_6_log_v)):
+                            if _k929_6_log_v:
+                                st.dataframe(_pd.DataFrame([{k: str(v) for k, v in _r.items()}
+                                                            for _r in _k929_6_log_v]),
+                                             use_container_width=True, hide_index=True)
+                            else:
+                                st.caption("（本次無合併試算）")
+
                     # 🆕 W-G Y 波診斷專用（KL 2026-07-14 交辦·非產品功能）：
                     # live g_rows JSON dump 供 sub-cent 定位。
                     # 純加·輸出 st.session_state['f3_G_values'] 原始物件（全精度、未捨入、
diff --git a/verify/run_verification.py b/verify/run_verification.py
index ed488ba..4d83d2c 100644
--- a/verify/run_verification.py
+++ b/verify/run_verification.py
@@ -59,9 +59,13 @@ F4DIR = os.path.join(HERE, "baselines", "wf", "f4")  # 🆕 W-F F.4 收斂波 ba
 #   於 `3.5m` 使 `R2` 左、`R5` 左之街角由強制抵費地改為合併後之街角第 1 宗（`628-41(1)`／`628-45(1)`）；
 #   二態實測：`WV_K6B_STAGE3=off` ⇒ 前值逐塊相符、未設 ⇒ 本值（`W-G.9-344` 補令二裁二以 `oracle`
 #   ⛔ 呼叫段三碼算得同值）。`0m` 段三⛔ 執行（段二序 `0` 列）⇒ 未改。
+#   🆕 `W-G.9-349`（重錨·逐塊歸因）：`0m` 之 `R2 8→7`、`R3 7→5`、`R5 7→4`、`R6 6→3`；`3.5m` 之 `R2 7→5`、
+#   `R3 7→5`、`R6 6→3`；前值 ＝ `{"R1": 2, "R2": 8, "R3": 7, "R4": 1, "R5": 7, "R6": 6}`（`0m`）／本檔上一版之 `3.5m`。
+#   歸因 ＝ 入池閘（`K-9-29 六` ＋ 閘二 `K-9-12`／`K-9-13` ＋ `K-9-33`）使不能建築之宗入池、同歸戶相鄰者合併；
+#   所變之街廓恰為有宗入池或合併者（`R1` 有而未變·`R4` 無）；二態實測：`WV_K929_6=off` ⇒ 前值逐塊相符、未設 ⇒ 本值。
 K_STAR_EXPECT = {
-    "0m":   {"R1": 2, "R2": 8, "R3": 7, "R4": 1, "R5": 7, "R6": 6},
-    "3.5m": {"R1": 1, "R2": 7, "R3": 7, "R4": 1, "R5": 4, "R6": 6},  # R1 2→1：S0d 改 S→最優切點移；R2 8→7／R5 7→4：段三（W-G.9-348）
+    "0m":   {"R1": 2, "R2": 7, "R3": 5, "R4": 1, "R5": 4, "R6": 3},  # W-G.9-349：入池閘
+    "3.5m": {"R1": 1, "R2": 5, "R3": 5, "R4": 1, "R5": 4, "R6": 3},  # R1 2→1：S0d 改 S→最優切點移；R2 8→7／R5 7→4：段三（W-G.9-348）；R2 7→5／R3 7→5／R6 6→3：入池閘（W-G.9-349）
 }
 OUTDIR = os.path.join(HERE, "out")
 CORNER_BLOCKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
diff --git a/verify/stepg_pipeline.py b/verify/stepg_pipeline.py
index eb557b4..21b9cb3 100644
--- a/verify/stepg_pipeline.py
+++ b/verify/stepg_pipeline.py
@@ -236,7 +236,7 @@ def assert_depth_same_source(depth_from_snapshot):
 
 
 def run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
-               winners_state, forced_map, setback, eff_min_build_by_blk=None):
+               winners_state, forced_map, setback, eff_min_build_by_blk=None, _k929_6_inner=False):
     """一情境 Step G（**薄殼**·`W-G.9-247` 工項一）——**只包、不吞**。
 
     🔒 **本殼之唯一職責** ＝ 於 `RuntimeError` 上掛 `e.partial` 後**原樣 `raise`**
@@ -254,6 +254,37 @@ def run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, build_parcels,
     🔒 `_pcap` ＝ partial capture。其 `g_rows` 掛的是 `_run_step_g_impl` 內
     `g_rows = []` 之**同一 list 物件**（掛引用·⛔ 複製）⇒ 中止時已 `extend` 之列全在。
     """
+    # 🆕 `W-G.9-349`（`K-9-29 六` 入池閘·KL 放行 `2026-09-26`）：旗標 on 且非試算趟 ⇒ 以 app 之
+    #   `k929_6_fixpoint` 求末態之 build（試算趟 ＝ 本函式 `_k929_6_inner=True`）；回末趟之結果（即以末態 build
+    #   所跑者·⛔ 重跑）並掛 `k929_6`（`build`／`log`）。`K917_DROPPED` ＝ 呼叫前之內容 ＋ 末趟所記（同單趟之累加）。
+    #   🔒 旗標 off ⇒ 本段⛔ 執行（逐位同本批前）。
+    if not _k929_6_inner and ns["k929_6_enabled"]():
+        import copy as _cp_k9296
+        _k917 = ns["K917_DROPPED"]
+        _saved = _cp_k9296.deepcopy(_k917)
+        _pre = _compute_v3_finance(ns, snapshot, cb, cad)["pre_price_by_zone"]
+        _ss9 = fake_st.session_state
+
+        def _trial(_b):
+            _k917.clear()
+            _sg9 = run_step_g(ns, fake_st, cb, cad, snapshot, param_rows, _b,
+                              winners_state, forced_map, setback,
+                              eff_min_build_by_blk=eff_min_build_by_blk, _k929_6_inner=True)
+            return _sg9["g_rows"], _cp_k9296.deepcopy(dict(_k917)), _sg9
+
+        try:
+            _bf, _last, _log9 = ns["k929_6_fixpoint"](
+                build_parcels, _trial, _ss9.get("t8_ownership_map", {}) or {}, _pre,
+                _ss9.get("f3_cad_front_lines", {}) or {})
+        finally:
+            _fin_drops = _cp_k9296.deepcopy(dict(_k917))
+            _k917.clear()
+            _k917.update(_saved)
+            for _kk, _vv in _fin_drops.items():
+                _k917.setdefault(_kk, []).extend(_vv)
+        _sg_out = _last[2]
+        _sg_out["k929_6"] = {"build": _bf, "log": _log9}
+        return _sg_out
     _pcap = {'g_rows': [], 'aborted_blk': None}
     try:
         return _run_step_g_impl(
````

## 附錄乙　塊 `F8`（新檔 `verify/probes/probe_WG9349_k9296.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-349 量測器（發單側窗四十五擬·檔 F8·⛔ 由受單側改一字）：`K-9-29 六`（入池閘）＋ 閘二之接線（`K-9-12`／`K-9-13`／`K-9-33`）。

子命令（一律 python verify/probes/probe_WG9349_k9296.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·只 harvest `app.py`）：`k929_6_enabled` 之解析、`k929_6_unbuildable` 之四項、
           `k917_should_drop` 之旗標二態、`k929_6_fixpoint` 之九例（合併·標的·佔位·a′·入池·三停機·不收斂·判別力）。
  run      <repo> <退縮> [<out.json>]
           harness 生產入口（`run_corner_pk_k6b` → `run_step_g`）跑一情境；旗標取自環境（`WV_K929_6`）。出艙：
           合併紀錄、不配地（含其由）、逐街廓之配地宗數與 ΣG；並驗：
             R1 旗標 on ⇒ 配地列中非街角第 1 宗者，⛔ 有內接矩形／最小建築面積不合格、⛔ 有 S(m) < 畸零地寬 − 0.006；
                旗標 off ⇒ 同一量出艙其數（判別力：須 > 0 方證 R1 非恆綠·本案 3.5 m 為 25）；
             R2 旗標 on ⇒ 不配地紀錄皆含「不配地由」且非「—」；off ⇒ 皆⛔ 含該鍵；
             R3 旗標 on ⇒ 回傳含 `k929_6`；合併紀錄之「結果」∈ {留置, 入池, 續併}；留置者之標的在配地列、其 a 面積 ＝ 「a 合計」（±0.01）；
                off ⇒ 回傳⛔ 含 `k929_6`。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import contextlib, copy, io, json, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _rect(x0, x1, y0=0.0, y1=30.0):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]


def selftest(repo):
    ns, _ = _harvest(repo)
    red = []
    _need = ["k929_6_enabled", "k929_6_unbuildable", "k929_6_fixpoint", "k917_should_drop"]
    _miss = [n for n in _need if n not in ns]
    if _miss:
        print(f"  🔴 受詞缺：{_miss}")
        print(f"⇒ 紅 ['受詞缺']；rc 1")
        return 1

    def chk(name, got, exp):
        ok = (got == exp)
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)

    def chk_raise(name, fn, frag):
        try:
            fn()
        except RuntimeError as e:
            ok = frag in str(e)
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：停機 {'含' if ok else '⛔ 含'}「{frag}」")
            if not ok:
                red.append(name)
            return
        print(f"  🔴 {name}：未停機（期含「{frag}」）")
        red.append(name)

    # ── 旗標 ──
    env0 = os.environ.get("WV_K929_6")
    for v, exp in ((None, True), ("", True), ("on", True), ("ON", True), ("off", False)):
        if v is None:
            os.environ.pop("WV_K929_6", None)
        else:
            os.environ["WV_K929_6"] = v
        chk(f"旗標 {v!r}", ns["k929_6_enabled"](), exp)
    os.environ["WV_K929_6"] = "x"
    chk_raise("旗標 'x'", ns["k929_6_enabled"], "只接受 on／off")
    os.environ.pop("WV_K929_6", None)

    # ── 不能建築項 ──
    U = ns["k929_6_unbuildable"]
    lg = lambda **k: {"_lg_cols": dict({"驗_A幾何": "合格", "驗_C面積": "不適用", "驗_A_W": 3.5}, **k)}
    chk("U1 內接矩形不合格", U(dict(lg(驗_A幾何="不合格"), S_raw=5.0)), ["內接矩形"])
    chk("U2 S 3.49 < W 3.5", U(dict(lg(), S_raw=3.49)), ["臨正街寬"])
    chk("U3 S ＝ W 合格（題三）", U(dict(lg(), S_raw=3.5)), [])
    chk("U4 W 取不到 ⇒ 臨正街寬⛔ 判", U(dict(lg(驗_A_W="—"), S_raw=1.0)), [])
    chk("U5 最小建築面積不合格", U(dict(lg(驗_C面積="不合格"), S_raw=5.0)), ["最小建築面積"])
    chk("U6 無從判定⛔ 當不合格", U(dict(lg(驗_A幾何="無從判定"), S_raw=5.0)), [])
    chk("U7 S_raw 缺 ⇒ 取 S", U(dict(lg(), S=2.0)), ["臨正街寬"])

    # ── k917_should_drop 之二態 ──
    SD = ns["k917_should_drop"]
    rA = {"_lg_cols": {"驗_B藍影": "合格", "驗_A幾何": "不合格", "驗_A_W": 3.5}, "S_raw": 5.0}
    rB = {"_lg_cols": {"驗_B藍影": "不合格", "驗_A幾何": "合格", "驗_A_W": 3.5}, "S_raw": 5.0}
    chk("D1 on·A 不合格·有後繼", SD(rA, False, True, "left", "B", "x")[0], True)
    chk("D2 on·A 不合格·末位", SD(rA, False, False, "left", "B", "x")[0], True)
    chk("D3 on·A 不合格·街角第 1 宗", SD(rA, True, True, "left", "B", "x")[0], False)
    chk("D4 on·藍影不合格·末位", SD(rB, False, False, "left", "B", "x")[0], True)
    os.environ["WV_K929_6"] = "off"
    chk("D5 off·A 不合格", SD(rA, False, True, "left", "B", "x")[0], False)
    chk_raise("D6 off·藍影不合格·末位（本批前之 loud）", lambda: SD(rB, False, False, "left", "B", "x"), "K-9-9 六")
    os.environ.pop("WV_K929_6", None)

    # ── k929_6_fixpoint ──
    FP = ns["k929_6_fixpoint"]
    FL = {"B": {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}}
    PRICE = {"z1": 1000.0, "z2": 2000.0}

    def P(pid, x0, x1, a, zone="z1", lot=None):
        return {"暫編地號": pid, "原地號": lot or pid, "所屬街廓": "B", "分攤登記面積_m2": a, "面積_m2": 0.0,
                "重劃前地價區段": zone, "polygon_coords": _rect(x0, x1)}

    def mk_trial(rule, side="left", corner=()):
        """rule(build) -> set(不配地之暫編)；G ＝ a × 0.6；其餘入配地列。"""
        def trial(b):
            dropped = rule(b)
            rows, dl = [], []
            for t in b:
                a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
                if t["暫編地號"] in dropped:
                    dl.append({"暫編地號": t["暫編地號"], "G(㎡)": round(a * 0.6, 4)})
                else:
                    rows.append({"暫編地號": t["暫編地號"], "推進側別": side, "G(㎡)": a * 0.6,
                                 "驗_宗序": "街角第1宗" if t["暫編地號"] in corner else "其後"})
            return rows, ({("B", side): dl} if dl else {}), None
        return trial

    own = {"L1": "G1", "L2": "G1", "L3": "G1", "L4": "G2", "L5": "G1"}
    small = lambda b: {t["暫編地號"] for t in b if float(t["分攤登記面積_m2"]) + float(t["面積_m2"]) < 150}

    # F1：X1(300·過)｜X2(60·不過)｜X3(40·不過) 同歸戶相鄰（左推進）⇒ 併入 X1、佔 X1 之位（投影最小）、留置
    b1 = [P("X1", 0, 10, 300, lot="L1"), P("X2", 10, 12, 60, lot="L2"), P("X3", 12, 13, 40, lot="L3")]
    bf, out, log = FP(b1, mk_trial(small), own, PRICE, FL)
    chk("F1 合併一次", len(log), 1)
    chk("F1 標的 ＝ 個別 G 最大", log[0]["標的"] if log else None, "X1")
    chk("F1 佔位（左·投影最小）", log[0]["佔位"] if log else None, "X1")
    chk("F1 a 合計", log[0]["a 合計"] if log else None, 400.0)
    chk("F1 結果", log[0]["結果"] if log else None, "留置")
    chk("F1 末態 build", sorted(t["暫編地號"] for t in bf), ["X1"])
    chk("F1 入參⛔ 改寫", [t["面積_m2"] for t in b1], [0.0, 0.0, 0.0])
    # F2：同 F1 而右推進 ⇒ 佔位 ＝ 投影最大（X3）；標的仍 X1
    bf2, _, log2 = FP(copy.deepcopy(b1), mk_trial(small, side="right"), own, PRICE, FL)
    chk("F2 佔位（右·投影最大）", log2[0]["佔位"] if log2 else None, "X3")
    chk("F2 單元之名 ＝ 標的", [t["暫編地號"] for t in bf2], ["X1"])
    chk("F2 單元之位 ＝ 佔位者之幾何", bf2[0]["polygon_coords"] if bf2 else None, _rect(12, 13))
    # F3：皆不過、合併仍不過 ⇒ 入池（無停機）
    b3 = [P("Y1", 0, 2, 60, lot="L1"), P("Y2", 2, 4, 50, lot="L2")]
    _, out3, log3 = FP(b3, mk_trial(lambda b: {t["暫編地號"] for t in b}), own, PRICE, FL)
    chk("F3 結果 ＝ 入池", log3[0]["結果"] if log3 else None, "入池")
    # F4：a′ 之折算（Y2 於 z2·標的 Y1 於 z1 ⇒ a′ ＝ 50 × 2000 ÷ 1000 ＝ 100）
    b4 = [P("Y1", 0, 2, 60, lot="L1"), P("Y2", 2, 4, 50, zone="z2", lot="L2")]
    _, _, log4 = FP(b4, mk_trial(small), own, PRICE, FL)
    chk("F4 併入量 a′", log4[0]["併入量(a′)"] if log4 else None, 100.0)
    # F5：異歸戶相鄰（L4）與同歸戶不相鄰（L5）⇒ 皆⛔ 合併
    b5 = [P("Z1", 0, 2, 60, lot="L1"), P("Z2", 2, 4, 300, lot="L4"), P("Z3", 20, 22, 300, lot="L5")]
    _, _, log5 = FP(b5, mk_trial(small), own, PRICE, FL)
    chk("F5 無合併", len(log5), 0)
    # F6：合併組含街角第 1 宗 ⇒ 停機
    chk_raise("F6 含街角第 1 宗", lambda: FP(copy.deepcopy(b1), mk_trial(small, corner=("X1",)), own, PRICE, FL),
              "含街角第 1 宗")
    # F7：跨左右推進 ⇒ 停機
    def trial7(b):
        rows, dl = [], []
        for t in b:
            a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
            if a < 150:
                dl.append({"暫編地號": t["暫編地號"], "G(㎡)": a * 0.6})
            else:
                rows.append({"暫編地號": t["暫編地號"], "推進側別": "right", "G(㎡)": a * 0.6, "驗_宗序": "其後"})
        return rows, {("B", "left"): dl}, None
    chk_raise("F7 跨左右推進", lambda: FP(copy.deepcopy(b1), trial7, own, PRICE, FL), "非單一")
    # F8：含原位可配者之合併單元終不配地 ⇒ 停機
    chk_raise("F8 一達一未達之反例",
              lambda: FP(copy.deepcopy(b1), mk_trial(lambda b: small(b) | {"X1"} if len(b) == 1 else small(b)),
                         own, PRICE, FL), "一達一未達")
    # F9：輪數上限
    chk_raise("F9 逾輪", lambda: FP(copy.deepcopy(b1), mk_trial(small), own, PRICE, FL, max_rounds=1), "未收斂")
    # 判別力：無不配地 ⇒ 無合併、build 原物件
    bf0, _, log0 = FP(b1, mk_trial(lambda b: set()), own, PRICE, FL)
    chk("判別力 無不配地 ⇒ 無合併", (len(log0), bf0 == b1), (0, True))
    if env0 is None:
        os.environ.pop("WV_K929_6", None)
    else:
        os.environ["WV_K929_6"] = env0
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def run(repo, sb, out=None):
    ns, fake_st = _harvest(repo)
    import run_verification as rv
    from selection_pipeline import run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    on = ns["k929_6_enabled"]()
    with contextlib.redirect_stdout(io.StringIO()):
        snapshot = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
            ns["K917_DROPPED"].clear()
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                            eff_min_build_by_blk={})
    except RuntimeError as e:
        print(f"🔴 執行中止：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
        return 3
    rows = sg["g_rows"]
    drops = {f"{k[0]}/{k[1]}": v for k, v in ns["K917_DROPPED"].items()}
    red = []
    print(f"【F8 run】退縮 {sb}·WV_K929_6 ＝ {os.environ.get('WV_K929_6')!r}（啟用 {on}）")
    # R1
    bad = []
    for r in rows:
        pid = str(r.get("暫編地號"))
        if "抵費地" in pid or r.get("第1筆街角") == "是" or r.get("推進側別") not in ("left", "right"):
            continue
        why = []
        if str(r.get("驗_A幾何", "")).strip() == "不合格":
            why.append("內接矩形")
        if str(r.get("驗_C面積", "")).strip() == "不合格":
            why.append("最小建築面積")
        try:
            if float(r.get("S(m)")) < float(r.get("驗_A_W")) - 0.006:
                why.append("臨正街寬")
        except (TypeError, ValueError):
            pass
        if why:
            bad.append((r.get("所屬街廓"), pid, why))
    print(f"  R1 配地列中不能建築（非街角第 1 宗）之宗數 ＝ {len(bad)}")
    for b in bad:
        print(f"     {b}")
    if on and bad:
        red.append("R1")
    if not on and not bad:
        print("  🔴 R1 判別力：off 態之數為 0 ⇒ R1 可能恆綠")
        red.append("R1 判別力")
    # R2
    recs = [e for v in drops.values() for e in v]
    has = [("不配地由" in e) for e in recs]
    if on:
        ok2 = all(has) and all(e.get("不配地由") not in (None, "—") for e in recs)
    else:
        ok2 = not any(has)
    print(("  ✅" if ok2 else "  🔴") + f" R2 不配地紀錄 {len(recs)} 筆之「不配地由」")
    for k in sorted(drops):
        for e in drops[k]:
            print(f"     {k} {e.get('暫編地號')} G {e.get('G(㎡)')} 由 {e.get('不配地由', '（無此鍵）')}")
    if not ok2:
        red.append("R2")
    # R3
    k = sg.get("k929_6")
    if on:
        ok3 = k is not None
        rowby = {str(r.get("暫編地號")): r for r in rows}
        for L in (k or {}).get("log", []):
            print(f"     合併 {L}")
            if L.get("結果") not in ("留置", "入池", "續併"):
                ok3 = False
            if L.get("結果") == "留置":
                r = rowby.get(L["標的"])
                if r is None or abs(float(r.get("a 面積(㎡)") or 0) - float(L["a 合計"])) > 0.01:
                    ok3 = False
    else:
        ok3 = k is None
    print(("  ✅" if ok3 else "  🔴") + f" R3 入池閘之回傳（{'有' if k is not None else '無'}）與合併紀錄")
    if not ok3:
        red.append("R3")
    blk = {}
    for r in rows:
        pid = str(r.get("暫編地號"))
        if "抵費地" in pid or r.get("推進側別") not in ("left", "right"):
            continue
        d = blk.setdefault(r.get("所屬街廓"), [0, 0.0])
        d[0] += 1
        d[1] += float(r.get("G(㎡)") or 0)
    print("  逐街廓（配地宗數·ΣG）：" + "；".join(f"{b} {v[0]}·{v[1]:.2f}" for b, v in sorted(blk.items())))
    if out:
        json.dump({"rows": [{kk: r.get(kk) for kk in ("暫編地號", "所屬街廓", "推進側別", "a 面積(㎡)", "G(㎡)")}
                            for r in rows], "dropped": drops, "k929_6": (k or {}).get("log")},
                  open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _wiring_checks(app_src, stepg_src):
    """回 {檢名: bool}（AST·⛔ 執行）。"""
    import ast
    out = {}
    A = ast.parse(app_src)
    fns = {n.name: n for n in A.body if isinstance(n, ast.FunctionDef)}
    out["W1 模組層四函式"] = all(k in fns for k in
                              ("k929_6_enabled", "k929_6_unbuildable", "k929_6_fixpoint", "_k929_6_screen_gate"))
    f = fns.get("f3_screen_stepg_run")
    ok2 = False
    if f is not None:
        kw = [a.arg for a in f.args.kwonlyargs]
        dft = dict(zip(kw, f.args.kw_defaults))
        has_kw = "_k929_6_inner" in dft and isinstance(dft["_k929_6_inner"], ast.Constant) \
            and dft["_k929_6_inner"].value is False
        calls = [n for n in ast.walk(f) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                 and n.func.id == "_k929_6_screen_gate"]
        ok2 = has_kw and len(calls) == 1
    out["W2 配地本體之首呼叫入池閘（_k929_6_inner 預設 False·呼叫恰一）"] = ok2
    ok3 = False
    if f is not None:
        src_f = ast.get_source_segment(app_src, f) or ""
        ok3 = ("st.session_state['f3_k929_6_log'] = _k929_6_log" in src_f
               and "st.session_state.pop('f3_k929_6_log', None)" in src_f)
    out["W3 配地本體寫／去 f3_k929_6_log"] = ok3
    keys = None
    for n in A.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "K6B_SCREEN_TRIAL_KEYS"
                                             for t in n.targets):
            keys = ast.literal_eval(n.value)
    out["W4 f3_k929_6_log ∈ K6B_SCREEN_TRIAL_KEYS"] = bool(keys) and "f3_k929_6_log" in keys
    m = fns.get("main")
    ok5 = False
    if m is not None:
        src_m = ast.get_source_segment(app_src, m) or ""
        ok5 = "st.session_state.get('f3_k929_6_log')" in src_m and "K-9-29 六" in src_m
    out["W5 main() 之成果區顯示合併紀錄"] = ok5
    names = None
    for n in A.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
            names = ast.literal_eval(n.value)
    out["W6 _WF_NS_NAMES 納三名"] = bool(names) and all(
        k in names for k in ("k929_6_enabled", "k929_6_fixpoint", "K917_DROPPED"))
    S = ast.parse(stepg_src)
    rg = next((n for n in S.body if isinstance(n, ast.FunctionDef) and n.name == "run_step_g"), None)
    ok7 = False
    if rg is not None:
        a = [x.arg for x in rg.args.args]
        src_r = ast.get_source_segment(stepg_src, rg) or ""
        ok7 = "_k929_6_inner" in a and 'ns["k929_6_fixpoint"]' in src_r and 'ns["k929_6_enabled"]()' in src_r
    out["W7 harness run_step_g 之入池閘"] = ok7
    sd = fns.get("k917_should_drop")
    ok8 = False
    if sd is not None:
        src_s = ast.get_source_segment(app_src, sd) or ""
        ok8 = "k929_6_unbuildable(res)" in src_s and src_s.count("k929_6_enabled()") == 2
    out["W8 k917_should_drop 之二處接線"] = ok8
    return out


def wiring(repo):
    app_src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    stepg_src = open(os.path.join(repo, "verify", "stepg_pipeline.py"), encoding="utf-8").read()
    res = _wiring_checks(app_src, stepg_src)
    red = [k for k, v in res.items() if not v]
    for k, v in res.items():
        print(("  ✅ " if v else "  🔴 ") + k)
    # 突變（判別力）：本部全綠時，四種突變須各使其所守之檢轉紅
    muts = [
        ("M1 去 K6B_SCREEN_TRIAL_KEYS 之 f3_k929_6_log", "app",
         "    'f3_k929_6_log',\n)", "\n)", "W4 f3_k929_6_log ∈ K6B_SCREEN_TRIAL_KEYS"),
        ("M2 配地本體之入池閘呼叫改名", "app",
         "build_parcels, _k929_6_log = _k929_6_screen_gate(st, dict(",
         "build_parcels, _k929_6_log = _k929_6_screen_gate_X(st, dict(",
         "W2 配地本體之首呼叫入池閘（_k929_6_inner 預設 False·呼叫恰一）"),
        ("M3 main() 之顯示去之", "app",
         "_k929_6_log_v = st.session_state.get('f3_k929_6_log')", "_k929_6_log_v = None",
         "W5 main() 之成果區顯示合併紀錄"),
        ("M4 harness 之入池閘去之", "stepg",
         'if not _k929_6_inner and ns["k929_6_enabled"]():', "if False:",
         "W7 harness run_step_g 之入池閘"),
    ]
    if not red:
        for name, which, old, new, target in muts:
            a2, s2 = app_src, stepg_src
            if which == "app":
                if a2.count(old) != 1:
                    print(f"  🔴 {name}：突變錨命中 {a2.count(old)}（須 1）⇒ 器紅")
                    red.append(name)
                    continue
                a2 = a2.replace(old, new)
            else:
                if s2.count(old) != 1:
                    print(f"  🔴 {name}：突變錨命中 {s2.count(old)}（須 1）⇒ 器紅")
                    red.append(name)
                    continue
                s2 = s2.replace(old, new)
            r2 = _wiring_checks(a2, s2)
            ok = (r2.get(target) is False)
            print(("  ✅ " if ok else "  🔴 ") + f"{name} ⇒ 「{target}」{'轉紅' if ok else '⛔ 轉紅'}")
            if not ok:
                red.append(name)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "selftest":
        sys.exit(selftest(a[1]))
    if len(a) >= 3 and a[0] == "run":
        sys.exit(run(a[1], float(a[2]), a[3] if len(a) > 3 else None))
    if len(a) >= 2 and a[0] == "wiring":
        sys.exit(wiring(a[1]))
    print(__doc__)
    sys.exit(2)
````

## 附錄丙　塊 `E2`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-349 §零-1`）：本批取 `538`〜`541`（`4` 號）。`538` ＝ 發單側交接文十八 `§四 乙`（原擬號 `469` 已另鑄·`docs/orders/W-G.9-309_重量單.md:32`）；`539` ＝ 交接文四十二 `§四-4(f)`（二者之原文皆於發單側窗四十四到手〔KL `2026-09-26` 上傳〕、擬於交接文四十四附錄甲）；`540`／`541` 係發單側窗四十五所自捕。

### 🩸 `自誤 538`　**`W-G.9-325` 工項五 `五` 以字樣命中斷言 `probe_WG9321_cc_recheck.py`「含 `shell=True`」「同形之器」；其二處係報告文字、作為呼叫實參之命中 `0`**

**形**：`docs/orders/W-G.9-325_輕量單.md` 工項五 `五`（發單側窗十八）逐字「`verify/probes/probe_WG9321_cc_recheck.py` 含 `shell=True`（逐處具名其列號與命令）」，並以「同形之器」稱之。CC 實測（`docs/reports/W-G.9-325R_CC交接文.md` `§四-2` 項 `3`）：字樣命中 `2` 處（`:51`／`:52`），皆為該器之報告文字（對態錨器項 `10` 之「器紅（環境）」之具名）；`shell=True` 作為呼叫實參之 AST 命中 `0`。發單側窗十八擬單時曾印出該二列而未察。
**後果之界**：其結論（⛔ 修之）不受影響——無可修者；CC 具名相異、⛔ 追改單一字。單之該句於「可執行」之義上失準。零入倉之誤（生產碼）。
**根因**：以字樣命中斷言器之可執行性質，未以 AST／呼叫實參查之。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（受單側）。
**攔法**：既有 `恆常附款 k`（斷言須三查）。⛔ 新立款。教訓：斷言器之行為前，以 AST／呼叫實參查之。

---

### 🩸 `自誤 539`　**發單側窗四十二以 harness 重現 KL 首次介面驗之段三停機之同文，即向 KL 述其成因為「KL 資料使 `R1` 右翻轉」；KL 資料下 `R1` 右實為達標**

**形**：KL 本機介面驗（主 checkout ＝ 側支 `4a633d0`）之首次（同一工作階段先 `0 m`、後 `3.5 m`）於 `3.5 m` 按選位即停機（「[K-6-B 段三 後處理] 街廓 R4 有群 … 之保留宗而無本段之受併宗（停機款 9）」·`app.py` 字樣錨 `之保留宗而無本段之受併宗`）。發單側窗四十二以 harness 證得「段二序含 `R1` 右 `628(5)`」即得逐字相同之停機（負擔 ×`1.0075` 使 `628(5)` 落至 `226.99`），遂於對話述其成因為「KL 資料使 R1 右翻轉」；而 KL 之診斷（`WV_K6B_STAGE3=off`）候選明細表之 `R1` 右 `628(5)` 真 G `227.73`／門檻 `227.13`（達標），與 harness 逐位同（出處：發單側交接文四十二 `§一-7`·倉外）。
**後果之界**：同窗於對話收回；未入單、未入倉；該停機之成因仍【未證】（`GB-192`）。
**根因**：以「擾動可重現同文之停機」代「此即其成因」——擾動只證其足以致之，⛔ 證 KL 之資料確有此擾動；出艙前未以 KL 之實料核其前提。
**後果之框**：🟢 零土地後果；🟡 呈 KL 之成因說明一度失準（已收回）。攔點 ＝ **發單側**（窗四十二·KL 之診斷檔到手後）。
**攔法**：既有（`CLAUDE.md` 之「【倉】／【單】出處標注」款 `4`：二近似相符 ≠ 相互驗證，須先證其對候選具鑑別力）。⛔ 新立款。

---

### 🩸 `自誤 540`　**發單側窗四十五呈 KL 之入池請示，其【對土地的影響】（標為退縮 `3.5 m`）載「各街廓之未配地面積增加 `90`〜`580 ㎡` 不等」；上界 `580` 係退縮 `0 m` 之 `R2`，`3.5 m` 之實為 `90.06`〜`489.99 ㎡`**

**形**：發單側窗四十五以倉外器（`proto_k929_6.py`·態 `88dc179`）試算閘二接線 ＋ 入池閘之後果，呈 KL 之請示（`2026-09-26`）【對土地的影響】之首句標「退縮 `3.5 m`」，其第五款逐字「各街廓之未配地面積增加 `90`〜`580 ㎡` 不等，見附圖標題列」。該試算之逐街廓（街廓面積 − 配地 `ΣG`）：`3.5 m` ＝ `R1` `+90.06`／`R2` `+489.99`／`R3` `+367.41`／`R4` `0`／`R5` `+162.42`／`R6` `+276.35`；`0 m` 之 `R2` ＝ `+579.77`。附圖（`3.5 m`）之標題列所載者正確。
**後果之界**：KL 以「是」放行其方式；該範圍屬描述、⛔ 入判準；`W-G.9-349` 之 `§二` 以正確之數重述。零入倉之誤。
**根因**：同一試算器出艙二情境之表，擬請示時由二表各取一端合為一句，未以所標之情境逐值核。
**後果之框**：🟢 零土地後果；🟡 呈 KL 之數一處失準。攔點 ＝ **發單側**（窗四十五·擬單時復算）。
**攔法**：既有（`CLAUDE.md` 之「數字錨引倉檔」：數字須錨引其出處、禁憑記憶出艙）。⛔ 新立款。

---

### 🩸 `自誤 541`　**同請示之附帶通知逐字「本案成組者皆在左側推進，故此讀法不生差異」；`R3` 之 `628-28(1)`＋`628-29(1)`（歸戶 `G014`）係右側推進**

**形**：同請示之附帶通知第 `3` 點，就「合併後之土地，佔推進序在先者之位」一讀法，逐字「本案成組者皆在左側推進，故此讀法不生差異」。倉外器之合併紀錄（同上）載 `R3` 之 `G014` 組 `推進側` ＝ `right`。發單側窗四十五其後實測（`W-G.9-349 §一` 項 `9`）：右側推進者之「投影序在前」（`p1 → p2` 之小者）與「推進序在先」（右側推進之大者）所指之宗相異（`628-29(1)`／`628-28(1)`），惟該組於二位皆合併仍不能建築而入池，`R3` 之配地逐宗同 ⇒ **「不生差異」之結論於本案成立，其所據之前提為偽**。
**後果之界**：零土地後果；`W-G.9-349` 之 `§二` 更正其前提。零入倉之誤。
**根因**：出艙全稱（「皆」）前未逐組核其推進側；以結論之正確掩其前提之未核。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（窗四十五·擬單時實測）。
**攔法**：既有（`常規四` 款 `六`：凡「命中 `0`」之斷言須同格報所用之框、命中數與對照組——「皆在左側」即「右側者命中 `0`」）。⛔ 新立款。
````

## 附錄丁　塊 `G2`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-192`／`GB-193` 之立（`W-G.9-349`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `88dc179e730e829b8b3ec828bb2df40841d0b900`（本批開工態）。**取號**（`W-G.9-349 §零-1`）：`GB-192`／`GB-193` 於開工態全倉皆 `0` 命中（錨定框·列框）。

### `GB-192` 🆕　**畫面：KL 首次介面驗（同一工作階段先 `0 m`、後 `3.5 m`）之段三後處理停機，重開後不重現，成因【未證】**

**受詞**：`app.py` 之段三（`k6b_stage3_run`）後處理之停機（`W-G.9-344 §三-2` 步驟 `10` 明文之停機款 `9`·字樣錨 `之保留宗而無本段之受併宗`）於畫面路徑之觸發。
**實測**（KL 本機·倉外之物·發單側交接文四十二 `§一-7` 所載）：主 checkout ＝ 側支 `4a633d0`（`app.py` blob `550ba546…`）、`WV_` 未設；首次（同一工作階段先 `0 m` 選位、後 `3.5 m` 選位）⇒ `3.5 m` 按選位即停機，訊息逐字「[K-6-B 段三 後處理] 街廓 R4 有群 ['628(1)', …, '628-1(3)'] 之保留宗而無本段之受併宗（停機款 9）」；重開後一般模式直接 `3.5 m` ⇒ 段三跑畢、紀錄 `18` 列之成否與併入與 harness 全同、配地 `52` 宗中 `51` 宗逐位同（`628-40(1)` `292.69` 對 `292.68`）。發單側窗四十二以 harness 證「段二序含 `R1` 右 `628(5)`」即得逐字同文之停機；惟 KL 資料下 `R1` 右達標（真 G `227.73`／門檻 `227.13`），且已實跑排除：地價高 `0.02%`、`C` 取 `0`、總負擔比率、同一工作階段 `0 m → 3.5 m`（含 `0 m` 配地）之殘留、逐宗人工標記。
**與配地之關係**：停機（loud）·⛔ 錯配；惟觸發於合法之操作序而成因不明。
**與既有登記之界**：`GB-190`（街角地選定結果之失效只綁退縮與深度）——或同族（殘值），【未證】；`W-G.9-346`（`6cca376`·已入主線）之「首趟前去段二序」「試算趟缺 winners 即停機」可排除殘值一類之部分路徑；`自誤 539`（對此停機之成因誤判）。
**失效條件**：`(1)` 於 `W-G.9-346` 入主線後之態，以同一操作序（同一工作階段先 `0 m`、後 `3.5 m`）重演——不重現者具名其態與操作序後結案；重現者 ⇒ 成因經量測具名；`(2)` 屬缺陷者修入生產碼 ＋ KL 放行（附畫面路徑之合成案〔`自誤 517`〕）。
🔒 **排程**：KL 選辦之介面重演（交接文四十三 `§四-6` 已列）；畫面批併辦。

### `GB-193` 🆕　**入池閘（`K-9-29 六`·`W-G.9-349`）之三停機款與一讀法：本案⛔ 觸發，他案得觸發**

**受詞**：`app.py` 模組層 `k929_6_fixpoint`（字樣錨 `def k929_6_fixpoint`）之停機（`RuntimeError`·⛔ 靜默略過）與讀法：
- 甲　**合併組含街角第 `1` 宗** ⇒ 停機【未裁】（併入街角地與否·`K-9-48` 段三已先辦街角之合併）。
- 乙　**合併組跨左右推進** ⇒ 停機【未裁】（「投影序在前者」於二側推進無單一之義）。
- 丙　**含原位可配者之合併單元終不配地** ⇒ 停機【未裁】（`K-9-29 六`「一達一未達者於閘內併入（不進池）」之反例：照字面則原可配者亦隨之入池）。
- 丁（讀法·已施行）　合併後之單元佔**推進序在先者**之位（左側推進 ＝ 投影序最小者；右側推進 ＝ 投影序最大者）；`K-9-29 五` 逐字「投影序在前者」於右側推進者與之相異。
**實測**（發單側窗四十五·態 `88dc179` ＋ 本批之生產碼·harness）：甲、乙、丙於 `0 m`／`3.5 m` 皆⛔ 觸發；丁：本案右側推進之合併組唯 `R3` 之 `G014`（`628-28(1)`＋`628-29(1)`），其於二位皆合併仍不能建築而入池 ⇒ 二讀法之配地逐宗同（`W-G.9-349 §一` 項 `9`）。
**與配地之關係**：甲、乙、丙 ⇒ 停機（loud）·⛔ 錯配；丁 ⇒ 他案之右側推進合併組可建築時，二讀法之配地相異。
**與既有登記之界**：`K-9-29`（正典）；`K-9-48`（段三）。
**失效條件**：甲、乙、丙各經 KL 裁（附圖）而修入生產碼；丁經 KL 確認或另裁。
🔒 **排程**：觸發時或新調配模組之請示併辦。
````

## 附錄戊　塊 `R1`（附於 `docs/reports/W-G.9-348R_驗證器二處更正與攢批登記_執行報告.md` 之末）

````markdown

---

## 🔧 更正（`W-G.9-349` 工項三·⛔ 上文一字不刪·純末端追加）

🩸 **被更正之對象**：本檔 ④ 之第二表二列（`docs/reports/W-G.9波_claude.ai側自誤登記.md`／`docs/reports/W-G.4_泛用阻塞項登記表.md`）之「改後之 `CR`」欄逐字 `` `5`（全在改前之前綴；塊 `E1` 之 `CR` ＝ `0`） ``／`` `5`（同上；塊 `G1` 之 `CR` ＝ `0`） ``，與 ⑥ 自解清單 `3` 之「而二登記檔改後各含 `CR` `5`」及其所取「二數並報」。
🔒 **實為**：二檔之換行符 `CR`（位元組 `0x0D`）於改前（`2bec587`）與改後（`84195d7`）皆 **`0`**；所計之 `5` 係字面二字元（反斜線 ＋ 小寫 `r`）之出現數（二檔改前改後各 `5`·皆在改前之前綴）。器之判別力：`data/V6.dxf` 之 `CR` ＝ `12308`。
🔒 **出處**：CC 於推送工項四後自捕（`W-G.9-348` 之回報·對話）；發單側窗四十五自倉復算（態 `88dc179`）。
🔒 收工閘 `3`（本批文字檔之 `CR` 合計 `0`）⛔ 受影響——其當場所量者為真 `CR`。零土地後果。
````

## 附錄己　塊 `P3`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：閘二（`K-9-12`／`K-9-13`）與臨正街寬（`K-9-33`）之接線；`K-9-29 六` 入池閘（`W-G.9-349`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `88dc179e730e829b8b3ec828bb2df40841d0b900`（本批開工態）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | 閘二之接線（`K-9-12`·後果 `K-9-13`）＋ 最小建築面積（`v3` ⑨⑩）＋ 臨正街寬（`K-9-33`） | 非街角第 `1` 宗之宗，其內接矩形、最小建築面積任一不合格或臨正街寬 `<` 畸零地寬 ⇒ 不配地、由下一宗遞補（末位亦同）；`k917_should_drop` 一處（畫面與 harness 共用）；旗標 `WV_K929_6`（預設 `on`·`off` ⇒ 逐位同本批前） | ✅ | `docs/orders/W-G.9-349_重量單.md`；KL 放行 `2026-09-26` |
| `2` | `K-9-29 六` 入池閘 | 不配地之宗與同街廓同歸戶地籍相鄰之宗（連通分量）以 `a′` 合併、佔推進序在先者之位重試；合併可建築 ⇒ 留置；仍不能 ⇒ 全部入池；反覆至不動點（`k929_6_fixpoint`；harness ＝ `run_step_g`、畫面 ＝ `f3_screen_stepg_run` 各以試算趟為之） | ✅ | 同上；三停機款與一讀法 ＝ `GB-193` |
| `3` | 本檔「🔧 進度表之現況更正：`K-9-17` 遞補迴圈已落地」節之「**閘二**（`K-9-12` 矩形容納）⬜ 仍未接線」 | 自本批起已接線（序 `1`） | ✅ | 同上 |

🔒 **本案之土地後果**（harness·態 `88dc179` ＋ 本批）：退縮 `3.5 m` ⇒ 原位配地 `52 → 28` 宗；合併留置 `3` 組；入池 `22` 宗（`15` 歸戶·重劃前面積 `2363.40 ㎡`）。退縮 `0 m` ⇒ `55 → 29` 宗；合併留置 `4` 組；入池 `23` 宗（`16` 歸戶·`2513.70 ㎡`）。入池者待新調配模組調配。
🔒 **依賴序**（改自 `W-G.9-348` 之更新·其「`K-9-29 六` 入池閘」一環已落地）：正面道路識別符（幾何推導 ∪ 區外道路清單）→ 新調配模組（「調配階段之諸裁」節之序 `1`〜`8`）。
🔒 **本機介面**：主 checkout 同步後，執行介面之環境 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6` 皆須**未設**（設 `off` 之 `WV_K929_6` ⇒ 回本批前之配地）。畫面之「🧮 執行 G 值迭代計算」每次先以試算趟求入池閘之末態，其成果區另列合併紀錄。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `1`（子字串框）·列 ＝ `1`（列框）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````
SELF_SHA256: 8881e63012b80b2b77c7e584bf599fe8eff313bef20c7cb23bf76a97b07f21cc
