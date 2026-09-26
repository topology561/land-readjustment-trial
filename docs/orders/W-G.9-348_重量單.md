# `W-G.9-348`　重量單：驗證器二處之更正（`app_harvest` 快取鍵之正規化·`k*` 經驗錨 `3.5m` 之重錨）＋ 錨重量之射程收窄（W-F／W-D.4 凍存·⛔ 重錨）＋ 攢批登記 ＋ 待落地清單之更新

> **發單** ＝ 發單側窗四十四·`2026-09-26`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**；工項五於 **KL 之主 checkout**）。
> **級** ＝ **重**（生產碼 `2` 檔各一處：`verify/app_harvest.py`、`verify/run_verification.py`；皆⛔ 土地後果；`app.py` ⛔ 動一字）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `57c4623c8d28525565ef0665cffc53e9371b10e6`。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `D1`／`F7`／`E1`／`G1`／`P2` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`／`533`）——唯工項二之「非正規形」二造（`§三` 工項二）刻意以他形傳入，係該工項之受測物，⛔ 違本款。
> 🔑 **來源檔一**（KL 置於 **CC 之施工樹之根**·檔名逐字）：`W-G.9-348_重量單.md`（本單）。CC 一律**二進位複製**、⛔ 讀入改寫；施工樹之根無之 ⇒ 取 KL 主 checkout 之根（承 `W-G.9-345R`／`W-G.9-346R` 自解 `1`）。本批之新檔（`F7`）與改動（`D1`）皆自本單之塊抽出，⛔ 另有來源檔。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0` 與 `WV_K6B_STAGE3`（先以 `python -c "import os;print(os.environ.get('WV_K6_STEP0'),os.environ.get('WV_K6B_STAGE3'))"` 出艙 `None None`）。
> 🛑 **本單⛔ 及於**：`app.py` 之任何修改；`verify/` 頂層 `*.py` 除塊 `D1` 所改之二處外之任何修改；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4（`verify/wd4_tier_list.py`）之任何錨；`verify/baselines`；`verify/out/` 之二凍存名單（`K6A2_期望FAIL名單_WG97_名目加原因.txt`、`WG99_端到端複本_終止點凍存_投影.txt`）；`K-6` 典／`VR` 簿；任何側支之刪除或改寫。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**——出艙即止。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `57c4623c8d28525565ef0665cffc53e9371b10e6`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 523 522` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔 **`897`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗四十四實跑 `python verify/probes/wg9268_gate6_occupancy.py 57c4623 W-G.9-348 W-G.9-347 W-G.9-397`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-348`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-347` | `2`／`4`／`4` | `2`／`4`／`4` | `8` | `2` | `2`／`16` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-397` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `4`／`5` | 🟢 宣告框 `0` |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `6`／`6` | 🟢 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態之追蹤檔 `2695` 檔〔可讀 `2671`〕·錨定框 `(?<![0-9\-])<號>(?![0-9])`·列框·`常規四（七）補款二` 之更正：B 形 ⋀ C 形並取）：

| 號 | 裸（錨定）檔／列 | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|
| `自誤 524`〜`537`（`14` 號·逐號） | 皆 `0`／`0` | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`自誤 523` | `3`／`11` | `0`／`0` | `3`／`10` | 🟢 C 形非空（B 形於本倉為量測器紅·`GB-158`） |
| `GB-190`／`GB-191` | 皆 `0`／`0` | — | — | 🟢 可取 |
| 對照甲［必非零］`GB-189` | `4`／`21` | — | — | 🟢 |

對照乙（人造·執行期組出·代稱 ⟨NEG⟩·其字樣⛔ 入倉·`GB-147`）⇒ 各形皆 `0`。自誤 `MAX` ＝ `523`、`GB` `MAX` ＝ `189`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 524`〜`537`、`GB-190`／`GB-191`；⛔ 鑄 `VR`／`K-9`。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `57c4623`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `D1`／`F7`／`E1`／`G1`／`P2` 任一之 bytes／`sha256` 與 `§五-1` 不符 |
| `4` | 工項二前置之任一期不符（尤：`F7` 之改前 `rc ≠ 1`；`F4 parity` 非正規形之改前 `rc ≠ 3`） |
| `5` | 塊 `D1` 之 `git apply --check` 不過；或施後之 blob ≠ `§五-1` 項 `7` |
| `6` | 工項二之驗 `V-1`〜`V-3` 任一 ≠ 期（尤：✅→🔴 ≠ `0`；或相異項逾 `§三` 工項二 `V-3` 所列） |
| `7` | 工項二之 `push` 無 `§二` 之放行；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成 |
| `8` | 工項三之三檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四` 收工閘任一 ≠ 期 |
| `10` | 工項五：主 checkout 之追蹤檔有變動、或切至 `wip/s1-endpart` 被拒、或 `--ff-only` 被拒 |
| `11` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `12` | 本批任一新檔為 `git check-ignore` 所命中 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗四十四自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `57c4623c8d28525565ef0665cffc53e9371b10e6`；側支 `verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`30`**（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`） |
| `2` | 生產碼（開工態 blob） | `app.py` `f4c47af6b864de683b99985597310d36b1f43d23`；`verify/app_harvest.py` `fa1f213900dd33999fecafc1bccbbc3d8661d4cc`；`verify/run_verification.py` `bbea91fe7982123f83033b46557fb7d3af4fdc14` |
| `3` | `run_all`（開工態·倉外路徑·`797` 秒） | `64` 項：PASS `30`／FAIL `34`；對帳段「名目：凍存 `22`／現況 `34`」；`#27 k* 六塊經驗錨3.5m` 🔴（錨 `{R1 1, R2 8, R3 7, R4 1, R5 7, R6 6}`、實得 `{R1 1, R2 7, R3 7, R4 1, R5 4, R6 6}`）；`#58`〜`#62` `W-F F.0`〜`F.4` 🔴（`F.0` 停於 `GSA` 錨檢·`F.1`〜`F.4` 跳過） |
| `4` | 錨之分解（行程內中性化 `wf_f0.GSA_EXPECT` ＝ 空表·跑 `run_verification.main()`·三態·倉外器） | 態 `M` ＝ `WV_K6_STEP0=on`＋`WV_K6B_STAGE3=off`（其配地逐宗 ≡ 原主線 `6090a7f`·`W-G.9-347` 之 `F2 cmp`）／`K` ＝ `WV_K6B_STAGE3=off`／`T` ＝ 皆未設（生產態）。見下表 |
| `5` | 改後之模擬（倉外·`57c4623` ＋ 塊 `F7` ＋ 塊 `D1`·`789` 秒） | `run_all` `64` 項：PASS `30 → 31`；以 `verify/probes/probe_WG9343_step0_flag.py runall` 逐項對拍 ⇒ 相異項恰 `7`：`#27`（名目改為 `k* 六塊經驗錨3.5m {'R1': 1, 'R2': 7, 'R3': 7, 'R4': 1, 'R5': 4, 'R6': 6}`·FAIL → PASS）；`#58`〜`#62`、`#64`（狀態 FAIL → FAIL·違規數同·本體之異恰為 `verify/run_verification.py` 之 traceback 行號 `+5`〔塊 `D1` 於 `K_STAR_EXPECT` 之上增註解 `5` 列〕）；其餘 `57` 項逐項同；末端夾具／golden 列 `21／21` 相異 `0`（含 `fixture_yi_construction.py`）；對帳段 `22／34 → 22／33`；✅→🔴 `0` |
| `6` | `F7`（塊 `F7`·`verify/probes/probe_WG9348_harvest_key.py`） | 開工態 ⇒ `rc 1`（`W1 含 . 段`／`W2 含 .. 段` 各成一鍵·鍵數 `3`·`streamlit` 被換）；施 `D1` 後 ⇒ `rc 0`（鍵數 `1`·對照〔位元相同之複本〕⇒ 非同一物件·鍵數 `2`） |
| `7` | `F4 parity`（`verify/probes/probe_WG9345_screen.py parity <R> 3.5 off`）之 `<R>` 取非正規形 `<repo>/.` | 開工態 ⇒ `rc 3`（`K-9-5-4②：side_mid=(310506.137745, 2651928.673455) 於 f3_cad_side_lines_by_side 查無對應側界`）；施 `D1` 後 ⇒ `rc 0`（配地列 `harness 68／畫面 67`·不符格 `0`） |
| `8` | 畫面「執行七級調配」（`GB-191`） | 以 harvest 之 `_build_wf_ctx` 組 ctx（session 以 harness 之產物鋪之·同 `F4 wfctx` 之法）餵 `wf_f0.compute`：`0 m`／`3.5 m` 皆停於 `run_step_g` 之 `` `cad['baselines']` 為空 ``；補 `baselines` 後改停於 `GSA` 錨檢（`0 m` 值不符 `3` 項；`3.5 m` 值不符 `2` 項 ＋ `G007` 未被評估）。三支端到端複本（`verify/wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py`）皆停於前者（各 `rc 1`） |
| `9` | `R1-抵費地-2`（`GB-186`） | harness 之 `cut_coords` 重算：`0.004575 ㎡`（`0 m`）／`0.004600 ㎡`（`3.5 m`）·長邊 `29.5788 m`；`F4 parity` 之 `Z` 於 `3.5 off`／`3.5 on`／`0.0 on` 皆 ＝ `[('harness', 'R1-抵費地-2')]` |

**`§一` 項 `4` 之表**（`0 m` 之 `k*` 三態：`M` `{R1 2, R2 7, R3 5, R4 1, R5 6, R6 3}`、`K`／`T` 皆 ＝ 錨 `{R1 2, R2 8, R3 7, R4 1, R5 7, R6 6}`）：

| 受詞 | 錨 | 態 `M` | 態 `K` | 態 `T` | 判 |
|---|---|---|---|---|---|
| `K_STAR_EXPECT["3.5m"]` | `{R1 1, R2 8, R3 7, R4 1, R5 7, R6 6}` | `{R1 1, R2 7, R3 5, R4 1, R5 6, R6 3}` | ＝ 錨 | `{R1 1, R2 7, R3 7, R4 1, R5 4, R6 6}` | `K → T` 之差恰 `R2 8→7`、`R5 7→4`，其間只差段三之旗標 ⇒ **歸因 ＝ 段三**（同 `W-G.9-344` 補令二裁二之 `oracle`）⇒ **本批重錨** |
| `ok_f`（`FLAGGED_EXPECT`·`0 m`） | `31` | `18` | `27` | `27` | 🗄️ ⛔ 重錨（W-D.4·`§二` 射程；差 `4` 未歸因） |
| `GSA_EXPECT["0m"]`（值不符之三格） | `G007 359.43`／`G010 283.87`／`G014 128.63` | `gsa` 為空（六鍵皆未被評估） | `306.14`／`290.88`／`127.10` | 同 `K` | 🗄️ ⛔ 重錨（W-F） |
| `GSA_EXPECT["3.5m"]`（同三格） | `370.01`／`301.17`／`129.74` | 同上 | `369.25`／`298.43`／`129.24` | 未被評估／`292.95`／`132.98` | 🗄️ ⛔ 重錨（W-F） |
| `F.3 零遺漏`（`n_pub`·`3.5 m`） | `59` | `59` | `59` | `53` | 🗄️ ⛔ 重錨（W-F） |
| W-F 之連鎖（態 `T`·中性化後） | — | — | — | `F.1` 停於 `R1 楔形面積 0.00 ≠ 錨 5.3±0.05`；`F.4` 停於 `E0` 具名錨；`F.0`／`F.2`／`F.3` 之 baseline 對拍 `24` 項紅 | 🗄️（`自誤 535`） |

---

## `§二`　KL 之語與射程

🔒 **射程之裁（發單側·`常規三`·⛔ 土地後果）**：`W-G.9-347` 塊 `P1` 序 `5` 所列之四錨，唯 `K_STAR_EXPECT["3.5m"]` 屬現行配地之驗證（原位次階段之調配池落點）；`GSA_EXPECT`、`F.3 零遺漏` 屬 W-F，`ok_f` 屬 W-D.4（其四梯以 `ΣG_戶` 對 `MinA_區` 分梯、梯 `3` 為 W-F F.0 之釋池對象）——W-F 已凍存為史料（`CLAUDE.md` 之「🔧 待落地清單之補登：調配階段之諸裁」節；`docs/specs/調配階段_泛用規格_v1.md` `§五`），其錨⛔ 重錨（`§一` 項 `4` 之表：重錨須連鎖至凍存引擎之多錨）。KL 之效率指示「錨屬量測框架，⛔ 喧賓奪主」同旨。

🔒 **生產碼入主線之放行**（`CLAUDE.md` 之 `常規一` 補款）：**KL 貼本單之同一訊息內**逐字答「是」者，視為工項二之生產碼 `commit` 推入主線之放行，CC 將其逐字載入報告；**無之 ⇒ 工項二之驗畢後停於推送前，於對話請示 KL**。所答之【要你判斷】逐字：「同意將驗證程式之二處更正（R2、R5 二街廓之比對值更新；工具重複載入之修正；皆不改任何配地結果）推入主線嗎？（是／否）」

🔒 **逐筆放行清單**：本批動生產碼者恰 **`1`** 筆（工項二）：

| `commit` | 所動之生產碼 | 要旨 | 土地後果 |
|---|---|---|---|
| 工項二 | `verify/app_harvest.py`（`harvest` 之快取鍵）；`verify/run_verification.py`（`K_STAR_EXPECT["3.5m"]` 之二值 ＋ 註解 `5` 列） | 塊 `D1` | ⛔（`app.py` blob 不變） |

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由 CC 逕行 `push` 至主線；`(b)` 工項二之 `push` 以 `§二` 之放行為條件；`(c)` 工項五於 KL 本機之主 checkout·⛔ `commit`；`(d)` ⛔ 及其他任何生產碼、任何他錨。

---

## `§三`　工項（依序）

### 工項零　本單原封入倉（主線·零生產碼）

`docs/orders/W-G.9-348_重量單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-348 工項零：本單原封入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項一　量測器 `F7` 入倉（主線·零生產碼）

塊 `F7` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9348_harvest_key.py`（**新檔**）。`commit` 訊息逐字 `W-G.9-348 工項一：量測器 F7（harvest 快取鍵）入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項二　塊 `D1`：`app_harvest` 快取鍵之正規化 ＋ `k*` 經驗錨 `3.5m` 之重錨（🔴 生產碼·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9348_harvest_key.py <repo>` ⇒ **`rc 1`**（判別力·改前）；末列之紅含 `W1 含 . 段`、`W2 含 .. 段`（Windows 另含 `W3 分隔符互換`）及 `鍵數`。
2. 非正規形二造（判別力·改前·各 ⇒ **`rc 3`**，訊息含 `K-9-5-4②`）：
   - `N1` ＝ `<repo 之反斜線絕對路徑>\.`：`python verify/probes/probe_WG9345_screen.py parity <N1> 3.5 off <O>\parity_N1_pre.json`
   - `N2` ＝ 同一路徑之正斜線形（如 `C:/…/<施工樹>`）：`python verify/probes/probe_WG9345_screen.py parity <N2> 3.5 off <O>\parity_N2_pre.json`
3. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：塊 `D1` 依圍欄之逐列索引抽出為 `<O>\D1.diff`、對拍 `§五-1` 後，`git apply --check <O>\D1.diff` ⇒ 過；`git apply <O>\D1.diff`；`git hash-object verify/app_harvest.py` ＝ `00ebac621c17eb08ebe77daf37ebc8aeff7353cc`、`git hash-object verify/run_verification.py` ＝ `ed488baef2e2dab99a6c054ad0a9110675b9afdf`、`git hash-object app.py` ＝ `f4c47af6b864de683b99985597310d36b1f43d23`（停機款 `5`）。`commit` 訊息逐字 `W-G.9-348 工項二：app_harvest 快取鍵之正規化（自誤 479）＋ k* 經驗錨 3.5m 之重錨（段三·逐塊歸因）🔴 生產碼`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9348_harvest_key.py <repo>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `V-2` | `parity <N1> 3.5 off`、`parity <N2> 3.5 off`、`parity <repo> 3.5 off`（正規形） | 三者皆 **`rc 0`**、配地列不符格 `0` |
| `V-3` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log` | 項數同；PASS 數 ＝ 改前 ＋ `1`；**相異項恰為**：`#27`（名目改為 `k* 六塊經驗錨3.5m {'R1': 1, 'R2': 7, 'R3': 7, 'R4': 1, 'R5': 4, 'R6': 6}`、狀態 FAIL → PASS）；與「狀態 FAIL → FAIL·違規數同·本體異」之項（`#58`〜`#62`、`#64`），其本體之異**恰為** `verify/run_verification.py` 之 traceback 行號 `+5`（CC 逐項以 `diff` 出艙其異列）；末端夾具／golden 列相異 `0`；✅→🔴 **`0`** |

任一 ≠ 期 ⇒ 停機款 `6`。

**推**（`§二` 之放行成立後·與驗為分開之呼叫）：`git push origin HEAD:wip/s1-endpart`。

### 工項三　攢批登記 ＋ 待落地清單之更新（主線·零生產碼·一 `commit`）

塊 `E1`／`G1`／`P2` 各依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位**附於**：
- `E1` ⇒ `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；
- `G1` ⇒ `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；
- `P2` ⇒ `CLAUDE.md` 之末。

三檔之刪除欄皆 `0`、改前全檔為改後之嚴格前綴（停機款 `8`）。`commit` 訊息逐字 `W-G.9-348 工項三：攢批登記（自誤 524〜537·GB-190／GB-191·GB-186／GB-153 之進度）＋ 待落地清單之更新 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項四　執行報告入倉（主線·新檔 `docs/reports/W-G.9-348R_驗證器二處更正與攢批登記_執行報告.md`·零生產碼·一 `commit`）

須載：① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值；③ 工項二之前置與驗之全部出艙（`F7` 二態全文、`parity` 五份之 `rc` 與末三列、`runall` 對拍之全文、`#58`〜`#62`／`#64` 之 `diff` 異列）；④ 五塊之實得（bytes／`sha256`）與三檔之改前改後 bytes；⑤ `§二` 之放行（KL 之逐字或請示之經過）；⑥ CC 之自捕與自解。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-348 工項四：執行報告入倉 ⛔ 零生產碼` ⇒ `push origin HEAD:wip/s1-endpart`。

### 工項五　主 checkout 之同步（KL 本機·⛔ `commit`·⛔ `push`）

1. `git -C <主 checkout> fetch origin`；`git -C <主 checkout> status --porcelain --untracked-files=no` ＝ 空（根之來源檔為未追蹤檔·⛔ 計）。
2. `git -C <主 checkout> checkout wip/s1-endpart`；`git -C <主 checkout> merge --ff-only origin/wip/s1-endpart`。
3. 出艙：`git -C <主 checkout> branch --show-current` ＝ `wip/s1-endpart`；`git -C <主 checkout> rev-parse HEAD` ＝ 工項四 `commit` 之全 `40` 碼；`git -C <主 checkout> hash-object app.py` ＝ `f4c47af6b864de683b99985597310d36b1f43d23`。
任一不符 ⇒ 停機款 `10`·⛔ 動、回報實值。

---

## `§四`　收工閘（工項四之 `commit` 推後·於主線之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項零／一／三／四 逐檔 **`0`**；工項二 ＝ `verify/app_harvest.py` **`3`**、`verify/run_verification.py` **`1`**（＝ 塊 `D1`） |
| `2` | 生產碼 `34` 檔對 `57c4623` | 相異恰 **`2`**（`verify/app_harvest.py` ＝ `00ebac62…`、`verify/run_verification.py` ＝ `ed488bae…`）；`app.py` ＝ `f4c47af6…` |
| `3` | 本批文字檔之 `CR` | 合計 **`0`** |
| `4` | 三檔之 bytes | `CLAUDE.md` `263603 → 266266`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `1041629 → 1058035`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1001798 → 1009475`；三者改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`30`**；`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 537 523 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 537 523` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `522`／`MAX` `537`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `184`／`191`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `45`／`48`／`[44, 47]`（缺號集皆 ＝ 開工態） |
| `8` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·`40`／`40`／`39` |
| `9` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `10` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `11` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四（本單之替身 ＋ 塊 `F7` ＋ 塊 `D1` ＋ 三塊 ＋ 報告之替身·五 `commit`）並實跑閘 `1`、`4`、`6`〜`12` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `D1` | `3121` B·`sha256` `ccfab0bc8f3c2dfaeca3d3d8efe1d2dca33f99bbc08facdf855cccb5c62774f8`·`50` 列（圍欄內全文·末附換行） |
| `3` | 塊 `F7` | `4440` B·`sha256` `43a1fb447d49e18512efb20530af338d7fe51dfd2a161f97b50fdd4a3ac54b2d`·`97` 列（圍欄內全文·末附換行） |
| `4` | 塊 `E1` | `16406` B·`sha256` `06613923020544c0c2274e314fab5a7af033b4034206a26123421851787d53f2`·`142` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1041629` B）之末後，期末 ＝ `1058035` B |
| `5` | 塊 `G1` | `7677` B·`sha256` `7050d004f136c042e0d46e445b3e225101917ec8e739cd83c855f4b84ae38226`·`39` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1001798` B）之末後，期末 ＝ `1009475` B |
| `6` | 塊 `P2` | `2663` B·`sha256` `df8df0440ec7f843861d583ac38047579d8e7ca67d10f65c13f393b4b7456eb3`·`17` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`263603` B）之末後，期末 ＝ `266266` B |
| `7` | 施 `D1` 後之 blob | `verify/app_harvest.py` `00ebac621c17eb08ebe77daf37ebc8aeff7353cc`；`verify/run_verification.py` `ed488baef2e2dab99a6c054ad0a9110675b9afdf`（開工態 `fa1f2139…`／`bbea91fe…`） |
| `8` | `F7` 之二態 | 開工態 `rc 1`；施 `D1` 後 `rc 0`（`§一` 項 `6`） |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗四十四實跑：🔴 機械 `0` 項／🟡 提示 `5` 項——`P-1` `:70`（`§一` 之表頭·其各列之否定〔如「未被評估」〕皆於列內具名其態與器 ⇒ **具名豁免**）、`P-1` `:473`（`自誤 533` 之形·其框〔單首之首個 `---` 之前〕與母體〔`W-G.9-341`〜`347` 七單〕同段具名 ⇒ **具名豁免**）、`P-4` `:136`／`:170`（工項二之驗與收工閘之表頭·其箭頭皆為「改前 → 改後」，表內自載 ⇒ **具名豁免**）、`P-4` `:249`（塊 `D1` 之註解「`R2 8→7`、`R5 7→4`」·同註自載「前值 → 本值」⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `18054`–`25633`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux） | 拋棄式 worktree（`57c4623` ＋ 五 `commit`）：閘 `1` 工項二 `9／3`、`6／1`（增／刪），餘逐檔刪 `0`；閘 `4` 三檔 `263603 → 266266`／`1041629 → 1058035`／`1001798 → 1009475`（嚴格前綴）；閘 `6`〜`12` 皆 `rc 0`（閘 `7` 之四簿如 `§四`；`wfns_ast` `40`／`40`／`39`；`F5`「app 側宿主 ＝ f3_screen_stepg_run」；`F6`、`F7` 末列 `⇒ 紅 []；rc 0`） |

抽取式 ＝ 圍欄開列（`` ````diff ``、`` ````python `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零、一、三、四 ⇒ 逕行 `push` 主線；工項二 ⇒ 依 `§二` 之放行、驗皆符後推主線；工項五 ⇒ KL 本機之主 checkout。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `D1`（`git apply` 之差異·二檔）

````diff
diff --git a/verify/app_harvest.py b/verify/app_harvest.py
index fa1f213..00ebac6 100644
--- a/verify/app_harvest.py
+++ b/verify/app_harvest.py
@@ -127,8 +127,14 @@ _CACHE = {}
 
 def harvest(app_py=APP_PY):
     """回傳 (ns, fake_st)：ns 為真函式活命名空間，fake_st 供 driver 填 session_state。"""
-    if app_py in _CACHE:
-        return _CACHE[app_py]
+    # 🆕 `W-G.9-348`（`自誤 479` 之攔法「器內正規化」）：快取鍵改為 `os.path.abspath` 之正規形。
+    #   由：同一檔之二寫法（反斜線對正斜線、含 `.` 段）原各成一鍵 ⇒ 二次 harvest ⇒ 後者之 fake
+    #   `streamlit` 取代 `sys.modules['streamlit']`，先 harvest 者之 session 即與 `import streamlit`
+    #   所得者脫鉤（`W-G.9-346R` ⑧-2）。⛔ 用 `os.path.normcase`：`fixture_yi_construction` 以
+    #   `_CACHE[APP_PY]` 就地灌注複本，Windows 下 `normcase` 改大小寫即不命中其鍵。
+    _key = os.path.abspath(app_py)
+    if _key in _CACHE:
+        return _CACHE[_key]
     with open(app_py, "r", encoding="utf-8") as f:
         src = f.read()
     fake = _install_fake_streamlit()
@@ -137,7 +143,7 @@ def harvest(app_py=APP_PY):
     ns = {"__name__": "app_harvested", "__file__": app_py}
     exec(code, ns)
     ns["__harvest_stats__"] = {"kept": nkept, "skipped": nskip}
-    _CACHE[app_py] = (ns, fake)
+    _CACHE[_key] = (ns, fake)
     return ns, fake
 
 
diff --git a/verify/run_verification.py b/verify/run_verification.py
index bbea91f..ed488ba 100644
--- a/verify/run_verification.py
+++ b/verify/run_verification.py
@@ -54,9 +54,14 @@ F4DIR = os.path.join(HERE, "baselines", "wf", "f4")  # 🆕 W-F F.4 收斂波 ba
 #   🆕 P-0c（裁定M·Q-S3·claude.ai 2026-07-25）：改 **per-tag**——「跨情境 k* 不變」係 **S0d 前之
 #   經驗巧合、非設計不變量**（舊註「本案恰不變」已更正）。S0d(07-20)改 S → R1 3.5m 最優切點 2→1；
 #   重驗基礎＝`J(k*)≥J(naive)` 永久閘雙情境 PASS（probe_jkstar_legitimacy.py·M_P0c_jkstar.log）。
+#   🆕 `W-G.9-348`（重錨·逐塊歸因）：`3.5m` 之 `R2 8→7`、`R5 7→4`；前值（`W-G.9-344` 前）
+#   ＝ `{"R1": 1, "R2": 8, "R3": 7, "R4": 1, "R5": 7, "R6": 6}`。歸因 ＝ 段三（`K-6 §二 段三` ＋ `K-9-48`）
+#   於 `3.5m` 使 `R2` 左、`R5` 左之街角由強制抵費地改為合併後之街角第 1 宗（`628-41(1)`／`628-45(1)`）；
+#   二態實測：`WV_K6B_STAGE3=off` ⇒ 前值逐塊相符、未設 ⇒ 本值（`W-G.9-344` 補令二裁二以 `oracle`
+#   ⛔ 呼叫段三碼算得同值）。`0m` 段三⛔ 執行（段二序 `0` 列）⇒ 未改。
 K_STAR_EXPECT = {
     "0m":   {"R1": 2, "R2": 8, "R3": 7, "R4": 1, "R5": 7, "R6": 6},
-    "3.5m": {"R1": 1, "R2": 8, "R3": 7, "R4": 1, "R5": 7, "R6": 6},  # R1 2→1：S0d 改 S→最優切點移
+    "3.5m": {"R1": 1, "R2": 7, "R3": 7, "R4": 1, "R5": 4, "R6": 6},  # R1 2→1：S0d 改 S→最優切點移；R2 8→7／R5 7→4：段三（W-G.9-348）
 }
 OUTDIR = os.path.join(HERE, "out")
 CORNER_BLOCKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
````

## 附錄乙　塊 `F7`（新檔 `verify/probes/probe_WG9348_harvest_key.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-348 量測器（發單側窗四十四擬·檔 F7·⛔ 由受單側改一字）：`verify/app_harvest.py` 之快取鍵正規化（`自誤 479`）。

受詞：`app_harvest.harvest(p)` 對「同一檔之不同寫法」是否回傳**同一物件**（⇒ 只 harvest 一次、
`sys.modules['streamlit']` 只被換一次）。
量法：於本行程以 `<repo>/verify` 載入 `app_harvest`，先清其 `_CACHE`，再以同一 `app.py` 之諸寫法逐一呼叫：
  W0 ＝ `os.path.abspath(<repo>/app.py)`（正規形）
  W1 ＝ `<repo>/./app.py`（含 `.` 段；以 `os.sep` 串接）
  W2 ＝ `<repo>/verify/../app.py`（含 `..` 段）
  W3 ＝ 分隔符互換之形（`os.sep` 與 `os.altsep` 互換；`os.altsep` 為 None 之平台〔POSIX〕⇒ 本項記「不適用」、⛔ 計入判）
判：諸寫法之回傳，其二元素（`ns`／`fake_st`）皆 `is` W0 所回者（回傳之 tuple 每次新建·⛔ 以 tuple 比）；`_CACHE` 之鍵數 ＝ `1`；`sys.modules['streamlit']` 自 W0 之後⛔ 被換。
另判（受詞之對照·⛔ 可省）：以同一 `app.py` 之**位元相同之複本**（另一目錄）呼叫 ⇒ 須**非**同一物件、鍵數 ＋1
（證本器所判者為「路徑之同一」、⛔ 為「一律回同一物件」之恆綠）。

用法：python verify/probes/probe_WG9348_harvest_key.py <repo>
  （判別力：於 `57c4623`〔改前〕跑 ⇒ 須 `rc 1`〔W1／W2 各成一鍵〕；改後 ⇒ `rc 0`。）
rc：0 皆如期／1 有不如期者／2 用法錯／3 無從判定（受詞缺）。
"""
import importlib.util
import os
import shutil
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    repo = os.path.abspath(argv[1])
    ah_path = os.path.join(repo, "verify", "app_harvest.py")
    app0 = os.path.join(repo, "app.py")
    if not (os.path.isfile(ah_path) and os.path.isfile(app0)):
        print(f"🔴 受詞缺：{ah_path} 或 {app0} ⇒ rc 3")
        return 3
    spec = importlib.util.spec_from_file_location("app_harvest_F7", ah_path)
    ah = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ah)
    if not (hasattr(ah, "harvest") and isinstance(getattr(ah, "_CACHE", None), dict)):
        print("🔴 受詞缺：app_harvest 無 harvest 或 _CACHE ⇒ rc 3")
        return 3
    ah._CACHE.clear()

    forms = [
        ("W0 正規形", app0),
        ("W1 含 . 段", repo + os.sep + "." + os.sep + "app.py"),
        ("W2 含 .. 段", os.path.join(repo, "verify") + os.sep + ".." + os.sep + "app.py"),
    ]
    if os.altsep:
        forms.append(("W3 分隔符互換", app0.replace(os.sep, os.altsep)))
    else:
        print("  ℹ️ W3 分隔符互換：本平台 os.altsep 為 None ⇒ 不適用（⛔ 計入判）")

    bad = []
    base = ah.harvest(forms[0][1])
    st0 = sys.modules.get("streamlit")
    print(f"  W0 正規形：{forms[0][1]} ⇒ 鍵數 {len(ah._CACHE)}")
    for name, p in forms[1:]:
        got = ah.harvest(p)
        same = (got[0] is base[0]) and (got[1] is base[1])   # 回傳之 tuple 每次新建 ⇒ 逐元素比
        st_same = sys.modules.get("streamlit") is st0
        print(f"  {'✅' if (same and st_same) else '🔴'} {name}：{p} ⇒ 同一物件 {same}·"
              f"streamlit 未被換 {st_same}·鍵數 {len(ah._CACHE)}")
        if not (same and st_same):
            bad.append(name)
    n_keys = len(ah._CACHE)
    ok_keys = (n_keys == 1)
    print(f"  {'✅' if ok_keys else '🔴'} 鍵數 ＝ {n_keys}（期 1）")
    if not ok_keys:
        bad.append("鍵數")

    # 對照：位元相同之複本（另一目錄）⇒ 須非同一物件
    tmpd = tempfile.mkdtemp(prefix="wg9348_")
    try:
        cp = os.path.join(tmpd, "app.py")
        shutil.copyfile(app0, cp)
        other = ah.harvest(cp)
        _nb = other[0] is not base[0]
        diff_ok = _nb and (len(ah._CACHE) == n_keys + 1)
        print(f"  {'✅' if diff_ok else '🔴'} 對照（複本 {cp}）⇒ 非同一物件 {_nb}·"
              f"鍵數 {len(ah._CACHE)}（期 {n_keys + 1}）")
        if not diff_ok:
            bad.append("對照")
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)

    print(f"⇒ 紅 {bad}；rc {1 if bad else 0}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄丙　塊 `E1`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-348 §零-1`）：本批取 `524`〜`537`（`14` 號）。`524`〜`530` ＝ `W-G.9-344` 補令一 `§七` `1`〜`3`、補令二 `§七` `4`〜`7`（發單側交接文四十 `§四-3`）；`531` ＝ 同交接文 `§一-5`；`532` ＝ 交接文四十二 `§四-4(b)`；`533`／`534` ＝ 交接文四十三 `§四-4(g)`／`(h)`；`535`〜`537` 係發單側窗四十四所自捕（`537` 承交接文四十二 `§四-4(a)`）。

### 🩸 `自誤 524`　**`W-G.9-344` 原單 `§三-2` 以街廓多邊形判「路口片」與後處理 (b) 之所鄰，未以其自身之受測例實跑；本案街廓多邊形與地籍線不重合**

**形**：原單（發單側窗三十九）`§三-2` 之名詞「路口片 ＝ 道路片，其與所屬街廓以外之街廓多邊形相鄰者 `≥ 3` 塊」與步驟 `10` (b)「每一片以其所鄰之 `b ∈ B` 定其去處」，皆以街廓多邊形為受詞。本案 `628-30(4)` 對 `R3` 街廓多邊形共邊 `0`、對 `R3` 地籍片 `628-30(3)` 共邊 `13.2756 m`；照字面則 `628-45(4)` 改走道路片切分、`628-30(4)` 之 `R3` 側半片成「未處置」，與 KL 放行之配地（原單附錄乙）相斥。同單所附檔 `F2` 之 `oracle` 以寫死之表 `ORACLE_PUB_HALF` 與「距街廓多邊形 `< 0.05 m`」判之，⛔ 以原單之判法驗（`W-G.9-344` 補令一 `§一` 之二表）。
**後果之界**：CC 於工項三前停機（停機款 `9`／`11`），生產碼一字未寫；發單側窗四十出補令一裁一（「相鄰」⟺ 地籍片 `k6_shares_segment` 共邊）。零入倉之誤（生產碼）。
**根因**：判法之字面與受測例（附錄乙）分由二處產出（字面 ＝ 單之名詞；受測例 ＝ `oracle` 之寫死表），出單前未以字面實跑受測例。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（停機）。
**攔法**：既有（`常規八` 二之 ①：原始量須與獨立來源對拍）。⛔ 新立款。

---

### 🩸 `自誤 525`　**`W-G.9-344` 原單 `§三-4` 令「吃配地結果」之下游改用段三後之宗地，漏處 F.3／F.4 所消費之 `temp` 母體**

**形**：原單 `§三-4` 列「吃配地結果」者改用段三後之宗地，而 `verify/run_verification.py` 之 F.0 ctx 另有鍵 `"temp"`（F.3／F.4 之公設地調配所消費）未處置 ⇒ 段三所併之道路片與公設片將於公設地調配再計一次。
**後果之界**：CC 之 reviewer 捕得；補令一裁三（段三所併出之片加鍵 `段三併出`，`k6b_stage3_pool_temp` 排除之）落之（`a403842`）。零入倉之誤。
**根因**：以「吃配地結果」一語為框列消費者，未逐鍵列 ctx 之全部消費者。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（reviewer）。
**攔法**：既有 `恆常附款 m`（受詞之全部消費者）。⛔ 新立款。

---

### 🩸 `自誤 526`　**`W-G.9-344` 原單後處理 (b) 之二款互斥：「僅一側 ∈ `B` ⇒ 全入該側」與「所鄰之 `b` 不唯一 ⇒ 停機」於單側道路片相撞**

**形**：原單步驟 `10` (b) 之二款各自成立，而於「所鄰二街廓、其一 ∉ `B`」之道路片同時成立而結論相反。
**後果之界**：CC 之 reviewer 捕得；補令一裁二（半片之 `N` 三分：`1` 入該側／`≥ 2` 停機／`0` 該側 ∉ `B`·恰一側 ⇒ 全入）落之。零入倉之誤。
**根因**：多款之判準未以本案之各片逐一跑全部款。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（reviewer）。
**攔法**：既有（`常規二`：施工單內部條款互斥者由發單側當場裁）。⛔ 新立款。

---

### 🩸 `自誤 527`　**補令一所附檔 `F3` 之片數判法以集合算期、以串列比實；`temp` 含零面積 ghost 重號 ⇒ 真資料必紅**

**形**：檔 `F3`（`verify/probes/probe_WG9344p1_pooltemp.py`·發單側窗四十擬）之期望片數以集合（去重）算、實得以串列（含重號）比；段三之輸入 `temp` 為 `126` 片、相異暫編地號 `124`（零面積 ghost 重號·補令二 `§零` 項 `3`）⇒ 其判必紅；其自檢⛔ 含重號之造，出單前未以真資料跑其判法。
**後果之界**：CC 於工項四停機（停機款 `10`／`12`）；補令二以 `F3′`（逐元素依序比對·保留重號·自檢 `13/13`·以依規格之替身於真資料驗其判別力）取代。零入倉之誤（生產碼）。
**根因**：量測器之自檢造未含受詞之已知特徵（重號），出單前未以真資料跑。
**後果之框**：🟢 零後果（量測器紅）。攔點 ＝ **CC**（停機）。
**攔法**：既有（`常規八` 二之 ②；`CLAUDE.md` 之「探針還原內部幾何時，須以『碼面自身之保證』當自我驗證閘」節之第二觸發點：停機上呈之前必先自證量測器非紅）。⛔ 新立款。

---

### 🩸 `自誤 528`　**`W-G.9-344` 原單 `V-12` 之「✅→🔴 ＝ `0`」於本案結構上不可滿足**

**形**：原單 `V-12` 令改前改後之 `run_all` 無 ✅→🔴；而 `K_STAR_EXPECT["3.5m"]`（`verify/run_verification.py`）係開工態之經驗值，KL 放行之改後配地（段三）必改 `R2`／`R5` 之切點 ⇒ `#27 k* 六塊經驗錨3.5m` 必 ✅→🔴；出單時未以 `oracle` 態量 `run_all` 之錨項。
**後果之界**：CC 停機；補令二裁二以 `F2 oracle`（⛔ 呼叫段三碼）算得 `R2 7`／`R5 4`，與 CC 實得逐塊同 ⇒ 受領，`V-12` 收窄為「恰此一項、恰此值」；該錨之重量延至入主線後（`W-G.9-348` 落之）。零入倉之誤。
**根因**：「✅→🔴 ＝ `0`」之閘未先以期望態驗其可滿足性。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（停機）。
**攔法**：既有（閘須可滿足且可證偽·`自誤 245`／`251` 之戒）。⛔ 新立款。

---

### 🩸 `自誤 529`　**補令一裁三未查 `wf_f3` 之 `n_pub` 與其排除之受詞同源（同一 ctx 鍵兼餵調配之母體與零遺漏之母數）**

**形**：補令一裁三令 F.3／F.4 之 `temp` 用「排除 `段三併出`」後者；而 `wf_f3` 之 `n_pub`（`F.3 零遺漏` 之母數）亦取自同一 ctx 鍵 ⇒ 排除同時改零遺漏之母數（`3.5 m` `59 → 53`）。
**後果之界**：CC 之 reviewer 捕得；補令二裁三具名其 `6` 筆，零遺漏之錨併入入主線後之重量；W-F 凍存 ⇒ ⛔ 重錨（`W-G.9-348`）。零入倉之誤。
**根因**：出令時未查該 ctx 鍵之全部消費者。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（reviewer）。
**攔法**：既有 `恆常附款 m`。⛔ 新立款。

---

### 🩸 `自誤 530`　**`W-G.9-344` 原單 `§三-4` 之 harness 呼叫端清單漏 `verify/tools/y_dump_diff.py`**

**形**：原單 `§三-4` 所列之 `run_corner_pk` 結果之消費端（改用段三後之宗地者）未含 `verify/tools/y_dump_diff.py`。
**後果之界**：CC 之 reviewer 捕得；補令二裁四豁免之、歸畫面次單；`W-G.9-345` 工項五改接（`b0c9edc`）。零入倉之誤。
**根因**：呼叫端清單之母體未含 `verify/tools/**`。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（reviewer）。
**攔法**：既有（`CLAUDE.md` 之「證據指令一律『正面列舉』」節）。⛔ 新立款。

---

### 🩸 `自誤 531`　**`W-G.9-344` 原單 `§三-4` 令「F.4 模式二 `p_avg` 之母體照舊原始」而未設閘守之；同一 ctx 鍵兼餵「吃配地結果」與「重劃前母數」**

**形**：原單 `§三-4` 明載「F.4 模式二 `p_avg` 之母體照舊原始」；`a403842` 之 ctx `"build"` 改為段三後，而 `verify/wf_f4.py` 之 `p_avg = wf_f2._block_pre_avg(snap, c["build"], pre_price)` 讀之 ⇒ 該令未落實；CC 之處置表僅以夾具 `fixture_mode2_hand` 一列代之。發單側窗四十實算、窗四十一復現（`W-G.9-345 §一` 項 `10`·`3.5 m`）：`R3` `37435.5100 → 37461.2777`、`R5` `37699.8699 → 37756.6769` 元/㎡，餘四塊不變。
**後果之界**：F.4 於其態未執行（`W-F F.0` 先停）⇒ ⛔ 及任何出艙；發單側窗四十復驗時捕得；`W-G.9-345` 工項五以 `k6b_f4_ctx` 落之（`b0c9edc`）。
**根因**：該令只有字面、無綁性質之閘；同一 ctx 鍵兼餵二種母體（與 `529` 同形）。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（窗四十）。
**攔法**：既有（`W-G.9-199` 裁 `H` 之一般式：閘須直接綁性質）。⛔ 新立款。

---

### 🩸 `自誤 532`　**`W-G.9-345 §三-2` 之段三畫面入口，其停機訊息只於 `RuntimeError` 存之；他例外與 `st.stop()` ⛔ 留痕，且⛔ 去前次之段二序**

**形**：`W-G.9-345`（發單側窗四十一）`§三-2` 步驟 `7` 只於 `k6b_stage3_run` 丟 `RuntimeError` 時存 `f3_k6b_stage3_error`；他例外（如 `KeyError`）、首趟或終趟之 `st.stop()` 皆⛔ 存停機訊息、亦無指紋 ⇒ 其後按「配地」時 `k6b_stage3_selected` 回 `None`、`k6b_screen_build_for_g` 回段三前之宗地，配地而無警示（`W-G.9-345R` ⑧ 之 W-A）；步驟 `1` ⛔ 去 `f3_k6b_stage2_order`，街角選位於「土地歸戶為空」時⛔ 寫任何鍵 ⇒ 段三可能吃前次之段二序（同 ⑧ 之 W-B）。
**後果之界**：CC 之 reviewer 捕得；`W-G.9-346`（`6cca376`）以「中斷即停機」修之，其後同批入主線（`W-G.9-347`）。其間 KL 於主 checkout（側支 `4a633d0`）之介面實跑有無觸及該路【未證】；該路所出者為段三前之配地（⛔ 新造之錯配）。
**根因**：規格只列正常出口與一種例外型，未逐一列舉離開該函式之全部出口並定其痕跡。
**後果之框**：🟡 【未證】（見上）。攔點 ＝ **CC**（reviewer）。
**攔法**：既有（`CLAUDE.md` 之「`序 11` 之一般化」節款 `二`：受詞缺漏時須 loud）。⛔ 新立款。教訓：凡「中途失敗即停機」之規格，須逐出口（例外型、`st.stop()`、提前 `return`）列其所留之痕跡。

---

### 🩸 `自誤 533`　**`W-G.9-346` 單首漏載「Windows 下 `<repo>` 一律以反斜線傳入」；`自誤 479` 之攔法「器內正規化」迄未落地**

**形**：單首（首個 `---` 之前）含「反斜線」之列數：`W-G.9-341`〜`345`、`347` 各 `1`，`346`（發單側窗四十二）為 `0`。CC 首跑以正斜線（`pwd -W`）⇒ `F4 parity` 五態與 `--perturb` 皆 `rc 3`、`wfctx` `rc 1`（訊息 `K-9-5-4②：side_mid=(310506.137745, 2651928.673455) 於 f3_cad_side_lines_by_side 查無對應側界`）；成因 ＝ `verify/app_harvest.py` 之 `_CACHE` 以路徑字串為鍵 ⇒ 同一 `app.py` 之二寫法即二次 harvest，後者之 fake `streamlit` 取代 `sys.modules['streamlit']`（`W-G.9-346R` ⑧-2）。發單側窗四十三以非正規形 `<repo>/.` 於 Linux 重現（`W-G.9-346` 之改前態與其端之 `parity 3.5 off` 皆 `rc 3`、正規形 `rc 0`）；窗四十四於 `57c4623` 復現（`rc 3`）。
**後果之界**：CC 自捕，改以反斜線重跑；發單側窗四十三裁其⛔ 觸停機款 `8`。第三次復發（`W-G.9-309`／`333`／`346`）。
**根因**：單首之固定款以前單為範本手抄而漏一款；該款所防之病未於器內根治。
**後果之框**：🟢 零後果（量測器紅）。攔點 ＝ **CC**（自捕）。
**攔法**：`W-G.9-348` 工項二（`_CACHE` 鍵改為 `os.path.abspath` 之正規形·檔 `F7` 守之）⇒ 路徑之二寫法⛔ 再致二次 harvest；單首之款仍載（二重）。

---

### 🩸 `自誤 534`　**`W-G.9-346 §三-1` 丁之 🔒 句「二抽出函式可達之模組層函式對街角選位產物之讀唯 `f3_corner_range_areas` 與 `f3_pk_alloc_depth`」字面不成立**

**形**：該句（發單側窗四十二）之全稱「唯」，而 `f3_screen_stepg_run` 讀 `f3_corner_winners`、`f3L_forced_offset`、`f3_corner_range_polys`（`W-G.9-346R` ⑥-5）。
**後果之界**：CC 之 reviewer 捕得；其結論（去此 `6` 鍵⛔ 改街角選位本身之算）成立——試算內配地在街角選位之後、缺 winners 即停；`f3_corner_range_polys` 唯逐宗驗證站讀之（其註「其失敗不得影響分配」）。
**根因**：全稱「唯」之斷言，其母體（可達函式）與受詞（讀街角選位產物之鍵）未逐函式逐鍵列表出艙。
**後果之框**：🟢 零後果。攔點 ＝ **CC**（reviewer）。
**攔法**：既有 `恆常附款 m`；`常規四` 六（「命中 `0`」之斷言須同格報框、命中數、對照組）之類推。⛔ 新立款。

---

### 🩸 `自誤 535`　**`W-G.9-347` 塊 `P1` 序 `5` 將凍存之 W-F 之錨（`GSA_EXPECT`／`F.3 零遺漏`）與 W-D.4 之 `ok_f` 列為入主線後須重量之受詞，未讀 `CLAUDE.md` 之 `W-G.9-332` 節**

**形**：`W-G.9-347`（發單側窗四十三）塊 `P1`（已入 `CLAUDE.md`）序 `5` 列四錨為次單之受詞，交接文四十三 `§四-1` 並擬手法「行程內中性化 `wf_f0.GSA_EXPECT` 使 `F.0`〜`F.4` 跑完」。而 `CLAUDE.md` 之「🔧 待落地清單之補登：調配階段之諸裁」節（`W-G.9-332`）逐字「W-F（`verify/wf_f0.py`〜`wf_f4.py`）凍存為史料」，`docs/specs/調配階段_泛用規格_v1.md` `§五` 將「各子波之具名錨（`raise` 合計 `83`）」列為不沿用。發單側窗四十四實測（態 `57c4623`·行程內中性化 `GSA_EXPECT`）：`F.0` 過錨後，`F.1` 停於 `R1 楔形面積 0.00 ≠ 錨 5.3±0.05`、`F.4` 停於 `E0` 具名錨，`F.0`／`F.2`／`F.3` 之 baseline 對拍 `24` 項紅 ⇒ 重錨須連鎖至凍存引擎之多錨。
**後果之界**：窗四十四出單前捕得；`W-G.9-348` 收窄其射程為 `K_STAR_EXPECT["3.5m"]`，W-F 與 W-D.4 之錨⛔ 重錨（塊 `P2` 序 `3`）。入倉之清單一列失準，以 `W-G.9-348` 塊 `P2` 更正。
**根因**：列錨之受詞時未查其所屬程式之現況（凍存與否）。
**後果之框**：🟡 入倉之待落地清單一列失準（⛔ 土地後果）。攔點 ＝ **發單側**（窗四十四）。
**攔法**：既有（`CLAUDE.md` 之「🔒 動筆前先對現況」）。⛔ 新立款。

---

### 🩸 `自誤 536`　**交接文四十三 `§四-2` 擬 `_CACHE` 鍵改以 `os.path.normcase(os.path.abspath(p))`；Windows 下將使 `fixture_yi_construction` 之就地灌注不命中**

**形**：`verify/fixture_yi_construction.py` 以 `app_harvest._CACHE[app_harvest.APP_PY] = app_harvest.harvest(app_py)` 灌注變異之複本、再經 `harvest()`（預設引數 `APP_PY`）取之；`normcase` 於 Windows 轉小寫（`ntpath.normcase(r'C:\Users\admin\Desktop\land-readjustment-trial\app.py')` ⇒ `c:\users\admin\desktop\land-readjustment-trial\app.py`·發單側窗四十四於 Linux 以 `ntpath` 實跑）⇒ 取之不命中所灌之鍵、改 harvest 真 `app.py` ⇒ 該夾具之變異造不生效。
**後果之界**：窗四十四擬單時捕得；`W-G.9-348` 改取 `os.path.abspath`（⛔ `normcase`）。零入倉之誤。
**根因**：擬改快取鍵時未查 `_CACHE` 之全部直寫者。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（窗四十四）。
**攔法**：既有 `恆常附款 m`。⛔ 新立款。

---

### 🩸 `自誤 537`　**檔 `F4` 以二位小數之顯示欄判「零面積池列」；`W-G.9-345` 塊 `P1` 序 `3` 據之擬另行登記之片，實為 `GB-186` 之細縫（`0.0046 ㎡`）**

**形**：檔 `F4`（`verify/probes/probe_WG9345_screen.py`·發單側窗四十一擬）之列比對以欄 `幾何面積(㎡)`（`app.py` 之 `round(_g.area, 2)`）判「一側獨有之零面積池列」（`Z`）；`W-G.9-345` 塊 `P1`（已入 `CLAUDE.md`）序 `3` 據之載「harness 多一「幾何面積 `0`」之池列（二退縮皆 `R1-抵費地-2`）——待登記」，交接文四十二、四十三承之為「零面積池列差」之登記候選。發單側窗四十四以 harness 之 `cut_coords` 重算（態 `57c4623`）：該片面積 `0.004575`（`0 m`）／`0.004600 ㎡`（`3.5 m`），最小外接矩形長邊 `29.5788 m` ⇒ 即 `GB-186` 之細縫（`0.0046 ㎡`·長 `29.58 m`）。
**後果之界**：窗四十四捕得；⛔ 另鑄，併入 `GB-186` 之進度（`W-G.9-348`）。
**根因**：以二位小數之顯示欄代「面積為零」之性質（代理量）；擬立項前未以全精度幾何核其身分。
**後果之框**：🟢 零後果。攔點 ＝ **發單側**（窗四十四）。
**攔法**：既有（`W-G.9-199` 裁 `H` 之一般式）。⛔ 新立款。
````

## 附錄丁　塊 `G1`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-190`／`GB-191` 之立 ＋ `GB-186`／`GB-153` 之進度（`W-G.9-348`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `57c4623c8d28525565ef0665cffc53e9371b10e6`（本批開工態）。**取號**（`W-G.9-348 §零-1`）：`GB-190`／`GB-191` 於開工態全倉皆 `0` 命中（錨定框·列框）。

### `GB-190` 🆕　**畫面：街角地選定（含街角合併重試）之結果，其失效只綁退縮與分配深度二欄；失效後之配地⛔ 停機**

**受詞**（皆 `app.py` 之 `st.session_state`·開工態 `app.py` blob `f4c47af6b864de683b99985597310d36b1f43d23`）：
- 甲　`f3_corner_winners` 以字面鍵名寫入者恰一（字樣錨 `st.session_state['f3_corner_winners'] = _f3_corner_winners_state`·街角選位本體 `f3_screen_corner_pk_run`·且僅於本趟有 winner 時寫〔其上一列 `if _f3_corner_winners_state:`〕）、以字面鍵名清除者恰一（`_f3L_invalidate_g_cache`）；段三試算之鍵表（`K6B_SCREEN_TRIAL_KEYS`／`K6B_SCREEN_READBACK_KEYS`）於試算內去而復原，⛔ 失效之用；後者之掛接唯二：退縮欄之 `_f3L_setback_changed`（委派呼叫之）與逐街廓深度覆寫欄（`on_change=_f3L_invalidate_g_cache`）⇒ 街角選位之他項輸入（`f3_screen_corner_pk_run` 之引數：地價、`B`／`C`、街廓、宗地；及 session 之土地歸戶）變更後，`f3_corner_winners` 與段三之產物⛔ 失效，其後之配地讀前次之結果。
- 乙　`_f3L_invalidate_g_cache` 去 `f3_corner_winners` 與段三諸鍵（`K6B_SCREEN_STAGE3_KEYS` ＋ `f3_k6b_stage3_error`）後之配地：`k6b_stage3_selected` 回 `None`（無指紋）⇒ `k6b_screen_build_for_g` 回段三前之宗地；`f3_screen_stepg_run` 之 `_step_l_winners` 為空 ⇒ 以個別標記定街角；畫面僅見 `f3_g_needs_rerun` 之橫幅（`W-G.9-346R` ⑥-6）。
- 丙　`f3_screen_k6b_stage3` 之首趟無產出（如土地歸戶為空）時，「段二序為空」之出口撤停機訊息，而前次之 `f3_corner_winners`／`f3L_forced_offset` 可能殘留供配地（`W-G.9-346R` ⑥-7）。
**實測**（母體 ＝ 開工態 `app.py` 全檔·列框·字樣以 `grep -F`）：`['f3_corner_winners'] = ` ＝ `1`；`pop('f3_corner_winners'` ＝ `1`；`on_change=_f3L_invalidate_g_cache` ＝ `2`（其一為註解列 ⇒ 掛接 `1`）；`_f3L_invalidate_g_cache()` ＝ `2`（其一為定義列 ⇒ 呼叫 `1`·於 `_f3L_setback_changed` 內）；對照組 `f3_corner_winners` ＝ `15`（⇒ 量測器非紅）。乙、丙 ＝ reviewer 之碼面判讀（`W-G.9-346R` ⑥）；本案之實例【未證】。
**與配地之關係**：可能以過時或缺之街角選定結果照出配地而⛔ 停機；本案之實例【未證】。
**與既有登記之界**：`GB-187`（街角地選定之結果被清除後之 G 值計算，以技術語中斷）——同族（街角地選定之結果缺漏或過時）、異受詞（`GB-187` ＝ 中斷時之用語；本項 ＝ 不中斷之諸路）。
**失效條件**：`(1)` 街角地選定（含段三）之產物附其輸入之指紋，配地時指紋不符或缺 ⇒ 以地政用語停機並指示重跑街角地選定（修入生產碼 ＋ KL 放行·附畫面路徑之合成案〔`自誤 517`〕）；`(2)` 合成案之甲／乙／丙三造於改後皆 loud。
🔒 **排程**：畫面批（`GB-187`／`GB-188`／`GB-189`／Streamlit 升級）併辦。

### `GB-191` 🆕　**畫面：「執行七級調配」之 ctx（`_build_wf_ctx`）無 `baselines` ⇒ 於 `run_step_g` 以「BASELINE 圖層未解析」停機（訊息誤指圖層）**

**受詞**：`app.py` 模組層 `_build_wf_ctx`（字樣錨 `def _build_wf_ctx`）所組之 `cad` 僅六鍵（`alloc_dir_by_block`／`centerlines`／`front_lengths`／`front_lines`／`side_lengths_by_side`／`side_lines_by_side`）；`verify/wf_f0.py` 之 trunk B 以之呼叫 `run_step_g`，而 `verify/stepg_pipeline.py` 之 `run_step_g` 自 `7fa957e`（`2026-07-31`·K-8 段三 commit A）起於 `cad.get("baselines")` 為空即停（字樣錨 `` `cad['baselines']` 為空 ``）。
**實測**（發單側窗四十四·態 `57c4623`·以 harvest 之 `_build_wf_ctx` 組 ctx·session 以 harness 之產物鋪之〔同 `verify/probes/probe_WG9345_screen.py wfctx` 之法〕）：`0 m`／`3.5 m` 皆 ⇒ `` RuntimeError: 🔴 run_step_g：`cad['baselines']` 為空——BASELINE 圖層未解析或配對全失敗 ``；同 ctx 補 `baselines`（取 harness 之 `cad`）⇒ 改停於 `GSA` 錨檢（`0 m` 值不符 `3` 項；`3.5 m` 值不符 `2` 項 ＋ `G007` 未被評估）。三支端到端複本（`verify/wg_g1_smoke.py`／`wg_g2_smoke.py`／`wg_g3.py`）皆同停於此（各 `rc 1`·發單側窗四十四實跑）；`verify/fixture_e2e_termination.py` 之凍存（`verify/out/WG99_端到端複本_終止點凍存_投影.txt`·三支皆停於 `R2` 之 `②-宗` 閘）已過時，該夾具 `rc 1`。
**與配地之關係**：⛔ 動配地；畫面「執行七級調配」於本案⛔ 能產出，其訊息令操作者往 CAD 之 BASELINE 圖層找因（誤指）。
**與既有登記之界**：W-F 凍存為史料（`CLAUDE.md` 之「調配階段之諸裁」節；新調配程式落地後按鈕改接）——本項之受詞係其間之按鈕行為與訊息；`GB-153`（W-F 之逐值迴歸不可得）——異受詞。
**失效條件**：`(1)` 畫面「執行七級調配」改接新調配程式；或 `(2)` 於改接前，該按鈕以地政用語明示「七級調配（舊程式）已停用、新程式建置中」，⛔ 以圖層之訊息出（修入生產碼 ＋ KL 放行·附畫面路徑之合成案〔`自誤 517`〕）。
🔒 **排程**：畫面批併辦；或隨新調配模組。

### `GB-186` 之進度（⛔ 解除）

🔒 **本項之片之全精度**（發單側窗四十四·態 `57c4623`·以 `run_corner_pk_k6b` ＋ `run_step_g` 之 `cut_coords` 重算）：harness 配地列之 `R1-抵費地-2`，面積 `0.004575 ㎡`（`0 m`）／`0.004600 ㎡`（`3.5 m`）；最小外接矩形長邊皆 `29.5788 m`、短邊 `0.000525`／`0.000765 m`；其欄 `幾何面積(㎡)` 以二位小數顯示為 `0.0`。
🔒 **新事實**：畫面路徑（`f3_screen_stepg_run`）之配地列⛔ 含本片——`verify/probes/probe_WG9345_screen.py parity` 之 `Z` 於 `3.5 off`／`3.5 on`／`0.0 on`（發單側窗四十四實跑）皆 ＝ `[('harness', 'R1-抵費地-2')]`，同 `W-G.9-345 §五-2` 項 `2` 之記。`W-G.9-345` 塊 `P1` 序 `3` 之「幾何面積 `0` 之池列——待登記」即本片 ⇒ 自本進度起併入本項、⛔ 另鑄（`自誤 537`）。二路徑於本片相異之成因【未證】。
🛑 **⛔ 解除**（失效條件 `(1)`〜`(3)` 未成就）。

### `GB-153` 之進度（⛔ 解除）

🔒 `①`（`F.0`–`F.4` 之逐值迴歸）於入主線後之態（`57c4623`）仍不可得：`W-F F.0` 🔴（`GSA` 錨檢·`0m` 值不符 `3` 項）。發單側窗四十四以行程內中性化 `wf_f0.GSA_EXPECT` 實跑 ⇒ `F.0` 過錨後，`F.1` 停於 `R1 楔形面積 0.00 ≠ 錨 5.3±0.05`、`F.4` 停於 `E0` 具名錨，`F.0`／`F.2`／`F.3` 之 baseline 對拍 `24` 項紅。
🔒 W-F 係凍存之史料（`CLAUDE.md` 之「🔧 待落地清單之補登：調配階段之諸裁」節·`W-G.9-332`；`docs/specs/調配階段_泛用規格_v1.md` `§五` 將「各子波之具名錨」列為不沿用）⇒ `W-G.9-348` 裁：其錨⛔ 重錨；`①` 於 W-F 為受詞之期間⛔ 可得；新調配程式另立其驗收（同規格 `§四`；`§六` 序 `5`「新程式另立路徑，不依之」）。
🛑 **⛔ 解除**（`①` 未成就）；本項之受詞於新調配程式落地、畫面「執行七級調配」改接新程式時另議。
````

## 附錄戊　塊 `P2`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：錨之重量收窄（W-F／W-D.4 凍存·⛔ 重錨）；`app_harvest` 快取鍵之正規化（`W-G.9-348`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `57c4623c8d28525565ef0665cffc53e9371b10e6`（本批開工態）。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）；🗄️ ＝ 凍存·⛔ 辦。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `W-G.9-347` 塊 `P1` 序 `6`：`自誤 479` 之攔法「器內正規化」 | `verify/app_harvest.py` 之 `_CACHE` 鍵改為 `os.path.abspath` 之正規形（⛔ `normcase`：`verify/fixture_yi_construction.py` 以 `_CACHE[APP_PY]` 就地灌注·`自誤 536`）；檔 `F7`（`verify/probes/probe_WG9348_harvest_key.py`）守之 | ✅ | `docs/orders/W-G.9-348_重量單.md` |
| `2` | 同塊序 `5` 之 `K_STAR_EXPECT["3.5m"]` | `R2 8→7`、`R5 7→4`；歸因 ＝ 段三（`WV_K6B_STAGE3=off` ⇒ 前值逐塊相符；未設 ⇒ 本值） | ✅ | 同上 `§一` |
| `3` | 同塊序 `5` 之 `GSA_EXPECT`、`F.3 零遺漏`（W-F）與 `ok_f`（W-D.4） | **⛔ 重錨**：W-F 凍存為史料（本檔「🔧 待落地清單之補登：調配階段之諸裁」節；`docs/specs/調配階段_泛用規格_v1.md` `§五`）；W-D.4 之四梯清單以 `ΣG_戶` 對 `MinA_區` 分梯、其梯 `3` 為 W-F F.0 之釋池對象（同規格 `§五` 不沿用列）⇒ 同凍存。`ok_f` 之旗標（`0 m`·態 `57c4623`）：`WV_K6_STEP0=on`＋`WV_K6B_STAGE3=off` ⇒ `18`；`WV_K6B_STAGE3=off` ⇒ `27`；未設 ⇒ `27`；錨 `31`（差 `4` 未歸因） | 🗄️ | 同上 `§一`；`自誤 535` |
| `4` | 畫面「執行七級調配」之現況 | 本案按之 ⇒ 停於 `wf_f0` 內 `run_step_g` 之 BASELINE 檢（`_build_wf_ctx` 所組之 `cad` 無 `baselines`·`GB-191`）；縱補之，仍停於 `wf_f0` 之 `GSA` 錨檢（`0 m` 值不符 `3` 項；`3.5 m` 值不符 `2` 項 ＋ `G007` 未被評估）——發單側窗四十四以 `_build_wf_ctx`（harvest）實跑·畫面實跑【未證】。新調配程式落地前⛔ 以之為配地成果 | ⬜（新調配模組落地後改接·同「調配階段之諸裁」節） | 同上 `§一`；`GB-191` |

🔒 **依賴序**（改自 `W-G.9-347` 之更新·其「錨之重量」一環已收窄並落地）：`K-9-29 六` 入池閘 → 五級（新調配模組；其內之序見「調配階段之諸裁」節）。
🔒 **登記**：本批鑄 `自誤 524`〜`537`、`GB-190`／`GB-191`；`GB-186`／`GB-153` 之進度。
🔒 **本機介面**：本批之生產碼⛔ 及 `app.py`（blob 仍 `f4c47af6b864de683b99985597310d36b1f43d23`）⇒ 介面之行為⛔ 變。
````

SELF_SHA256: fef0e7bd54c36221accbb559a66b149394aa0d9d4178f2d2b5967bc4b531b4ed
