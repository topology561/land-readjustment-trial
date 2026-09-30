# `W-G.9-361`　規格單：地籍相連之判之座標容差（`K-9-54`·`GB-195`）（新側支 `verify/W-G.9-361-k954`）＋ `K-9-53`／`K-9-54` 之入典 ＋ `GB-195` 之立 ＋ `自誤 558`〜`561` ＋ 待落地清單之更新

> **本單建議等級 ＝ `high`**（生產碼之改動唯一函式·規格與量測器皆全）。
> **發單** ＝ 發單側窗六十·`2026-09-30`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-361-k954`**，其起點 ＝ 主線之端 `caede20`）。
> **流程 ＝ 規格單**（常態·`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通之期滿與續行（`W-G.9-358`）」節 ③·附則甲〜丙施行·`§二`）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `F21`·CC ⛔ 改一字）、既有量測器之錨之更新（塊 `F16p`／`F12p`／`F13p`／`F3p`）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **重**（生產碼 `1` 檔：`app.py`；🔴 **有土地後果**——退縮 `3.5 m`：段三後處理之地主甲〔`G007`〕之公設地上之土地由二街廓平分改為三街廓平分〔`§一` 項 `6`〕；退縮 `0 m`⛔ 變；**KL 已於 `2026-09-30 20:34` 裁「是」接受之**〔`K-9-54`·`§二`〕）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `caede209cb769fbea2986ffe712e835ff052549b`（`W-G.9-360` 工項三）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-361-k954`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F21`／`F16p`／`F12p`／`F13p`／`F3p`／`K6`／`G5`／`E8`／`P15` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-361_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 以外之生產碼一字（生產碼 `34` 檔之其餘 `33` 檔）；`app.py` 之 `k6_shares_segment` 與其新增之輔助函式、常數 `K6_SHARE_COORD_TOL` 以外之一字（`§三-3`）；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4 之任何錨；`verify/case_params_UC9898.json`；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿、恆常附款登記表之一字；`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md` 除塊 `K6`／`G5`／`E8`／`P15` 之純末端追加外之一字；既有量測器除塊 `F16p`／`F12p`／`F13p`／`F3p` 所改之外之一字；任何既有側支之推送、刪除或改寫；KL 主 checkout。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `caede209cb769fbea2986ffe712e835ff052549b`；`git ls-remote --heads origin` 之列數 ＝ `33`，且⛔ 含 `refs/heads/verify/W-G.9-361-k954`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 557 550` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`933`** 檔·器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗六十實跑（皆 `rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-361`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py caede20 W-G.9-361 W-G.9-360 W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-360` | `2`／`4`／`3` | `2`／`4`／`3` | `7` | `2` | `3`／`35` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `9`／`14` | 🟢 宣告框 `0`、鬆框非零（漏框偵察有咬） |
| `K-9-53`｜`python verify/probes/wg9268_gate6_occupancy.py caede20 K-9-53 K-9-52 K-9-93` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| `K-9-54`｜`python verify/probes/wg9268_gate6_occupancy.py caede20 K-9-54 K-9-52 K-9-94` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`K-9-52` | `0`／`14`／`0` | `0`／`14`／`4` | `14`（寬式 `18`） | `7`（寬式 `8`） | `11`／`95` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`K-9-93`／`K-9-94` | `0`／`0`／`0`｜`0`／`2`／`0` | `0`／`0`／`0`｜`0`／`2`／`0` | `0`｜`2` | `0`｜`2` | `2`／`4`｜`5`／`9` | 🟢 鬆框非零（`K-9-94` 之列框 `2` ＝ `自誤 546` 之標題之引〔`docs/orders/W-G.9-354_重量單.md` 與自誤簿〕·⛔ 占用·⛔ 受詢） |
| `GB-195`｜`python verify/probes/wg9268_gate6_occupancy.py caede20 GB-195 GB-194 GB-395` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`1` | 🟢 可取（鬆框 `1` 列 ＝ `docs/orders/W-G.9-343_重量單.md:33`「對照乙［必為零］`W-G.9-395`／`自誤 595`／`GB-195`／`K-9-55`」·其時之未取號·⛔ 占用） |
| 對照甲［必非零］`GB-194` | 寬式 `0`／`5`／`0` | ← | `5` | `2` | `11`／`31` | 🟢 框非恆空 |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `23`／`26` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免（報告內嵌本器之出艙）·受詢之判⛔ 受影響 |

**本批所鑄之自誤之號**（母體 ＝ 開工態之追蹤檔 **`2745`** 檔·列框·`常規四（七）補款二` 之 B 形 ⋀ C 形並取；發單側窗六十以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``〕於 `caede20` 實算）：

| 號 | 裸列 | 平形 `自誤 N` | B 形 `` 自誤 `N` `` | C 形 `` `自誤 N` `` | 判 |
|---|---|---|---|---|---|
| `自誤 558` | `40` | `0` | `0` | `0` | 🟢 可取（裸列皆數字之偶合·⛔ 為自誤之引用） |
| `自誤 559` | `599` | `0` | `0` | `0` | 🟢 可取（同上） |
| `自誤 560` | `47` | `0` | `0` | `0` | 🟢 可取（同上） |
| `自誤 561` | `100` | `0` | `0` | `0` | 🟢 可取（同上） |

本批鑄 `自誤 558`〜`561`（塊 `E8`）、`GB-195`（塊 `G5`）、`K-9-53`／`K-9-54`（塊 `K6`）；⛔ 鑄 `VR`。開工態之四簿（`probe_WG9321_issuer_anchor.py` 之「項4′ 四簿·正典框」·`557 550`）：自誤 相異 `542`／`MAX` `557`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `49`／`52`／`[44, 47]`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `caede20`，或遠端 heads ≠ `33`，或遠端已有 `verify/W-G.9-361-k954`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `F21`／`F16p`／`F12p`／`F13p`／`F3p`／`K6`／`G5`／`E8`／`P15` 任一之 bytes／`sha256` 與 `§五-1` 不符；或寫出後之 blob ≠ `§五-1` 項 `11`；或塊 `F16p`／`F12p`／`F13p`／`F3p` 任一之 `git apply --check` 不過 |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-8` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有 `§一` 項 `6` 所列以外之任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-361-k954`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之四檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer（附則丙）之發現涉域上判斷或規格之漏載 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `13`。

---

## `§一`　態錨（發單側窗六十自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `caede209cb769fbea2986ffe712e835ff052549b`；側支 `verify/W-G.9-359-cand` ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`、`verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`33`**（`verify/` `28`·`wip/` `3`·`claude/` `1`·`main` `1`）；`verify/W-G.9-361-k954` ⛔ 存 |
| `2` | 生產碼、量測器與四檔（開工態 blob） | `app.py` `cae25232047add2dc6703d9b2d1cee50d1601472`（`1639619` B）；`verify/run_verification.py` `3bd2b378368df204f0c0fca1734d597851e1252b`；`verify/selection_pipeline.py` `8d38e55013bec51ab81978336fe04e928f5baf98`；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；`verify/probes/probe_WG9357_k948.py` `c7515d3ecc2f8413899fb18affdee6b3cdec1228`；`verify/probes/probe_WG9353_endmerge.py` `c12d3f85f394662630e7edd8abc7ca90f98af086`；`verify/probes/probe_WG9354_endcontest.py` `2f81f739211589dab965504f252c883ad8a1a7e9`；`verify/probes/probe_WG9344p1_pooltemp.py` `9a5459fe8d11c42f886a8c7c4427f46e5748a940`；`verify/probes/probe_WG9355_screenmerge.py` `a78216399a6a5c708cff4d0b9f8bf14fa462f841`（⛔ 改）；`K-6` 典 `445942` B；`GB` 簿 `1022244` B；自誤簿 `1089994` B；`CLAUDE.md` `317190` B（皆以換行結尾·CR `0`） |
| `3` | 開場之查（發單側窗六十） | 主線之端、遠端 heads 與八側支 ＝ 交接文五十九之錨（`W-G.9-360` 已由發單側窗五十九復驗·交接文五十九 `§一-2`·全數相符）；交接文五十九（`15950` B·`sha256` `40da8c94…`）與 `F20` 原型之 zip（三檔之 bytes／`sha256` ＝ 交接文所載）皆收；`F20` 原型於 `caede20` 重跑，規格步 `4` 之受詞 ＝ 交接文 `§一-3` |
| `4` | 本批之受詞 | `K-9-54`（KL `2026-09-30 20:34`·本批入典）；`K-6 §一`（合併群述詞）；`app.py` 之 `k6_shares_segment`；`GB-195`（本批之立）；`K-9-53`（本批唯入典）；`自誤 558`〜`561` |
| `5` | 現碼之行為（開工態） | `k6_shares_segment` 以二片邊界之精確交集之線長判相連；本案段三之輸入之切片 `126` 片中，界線於圖上重合而座標有微米級之差（頂點至他片界線之距之最大者 `1.000e-05 m`）者 `19` 對判為不相連；合併群因而斷裂之歸戶 ＝ `G005`／`G007`／`G012`／`G017`／`G022`——由塊 `F21` 之 `run` 之 `R0`〜`R2` 證之（`§一` 項 `7`） |
| `6` | 本案之土地後果（原型·harness） | **退縮 `0.0`**：段三紀錄 `0` 列；`verify/probes/probe_WG9344_k6s3.py cmp` 對開工態相異 **`0`** 項；`F8 run`（`verify/probes/probe_WG9349_k9296.py run`）之出艙對開工態**逐位同**；調配之候選街廓名單（`F18 run`·`verify/probes/probe_WG9359_cand.py run`）之退縮 `0.0` 段逐位同；畫面與 harness 之 `parity` `0.0` ⇒ 配地列 `36`／`35`、不符格 `0`（同開工態）。**退縮 `3.5`**：段三紀錄 `18 → 19` 列——後處理 `628-20(3)`（`(b)`·受併宗 `628-20(1)`·`42.15`）新增；`628-45(3)`（`(c)`）受併宗 `628-45(1)`／`628-45(2)` 各 `136.545` → `628-20(1)`／`628-45(1)`／`628-45(2)` 各 `91.03`；`628-45(4)`（`(c)`）`112.3` → 三者各 `74.8667`；其餘 `16` 列逐位同。`k6s3 cmp` 相異 **`11`** 項（容差 `0.01`）：`628-45(2)` `a` `1697.67 → 1614.72`、`G` `950.91 → 902.52`；`628-45(1)` `a` `1037.03 → 954.08`、`G` `572.05 → 525.28`；`628-20(1)` `a` `570.15 → 778.20`、`G` `336.56 → 461.06`；`628-18(2)` `G` `213.51 → 212.98`；`628-7(2)` `G` `254.64 → 253.56`；抵費地 `R3` `1834.68 → 1883.03`、`R5` `1694.57 → 1742.99`、`R6` `1901.82 → 1777.33`（街角得標、強制旗標⛔ 變）。`F8 run` 之出艙唯「逐街廓（配地宗數·ΣG）」一列相異：`R3` `5·2372.12 → 5·2323.74`、`R5` `6·2455.61 → 6·2407.24`、`R6` `5·2074.46 → 5·2198.96`（餘街廓同）。調配之輸入（`F10 run`）：待同歸戶併入之歸戶 `9 → 8`（`G007` 之 `628-20(3)` 改為原位次配地〔段三所併〕）、原位次配地 `43 片·21412.68 ㎡ → 44 片·21454.83 ㎡`、共同負擔用地·待同歸戶併入 `13 片·2680.00 → 12 片·2637.85`；合併單位 `23`（建地軌 `15`·公設軌 `8`）⛔ 變。候選街廓名單（`F18 run`）：各單位之名單之先後⛔ 變，`R3`／`R5`／`R6` 之距離隨其抵費地之形而變（`rc 0`）。末端塊之合併再試（`F11 run`·`verify/probes/probe_WG9352_endblock.py run`）二退縮之出艙對開工態逐位同；畫面與 harness 之 `parity` `3.5` ⇒ 配地列 `35`／`34`、不符格 `0`（畫面與 harness 同受 `K-9-54`）；`run_all` 對開工態唯 `#24 v3·G值3.5m` 一項相異（`FAIL → FAIL`·違規數 `295 → 299`·`§一` 項 `9`） |
| `7` | 量測器於工項一之端（`caede20` ＋ 塊 `F21` ＋ 塊 `F16p`／`F12p`／`F13p`／`F3p`·發單側實跑） | `F21 selftest` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['受詞缺', 'A4', 'A8', 'A10', 'A12']；rc 1`（常數 `K6_SHARE_COORD_TOL` 缺 ⇒ 續跑；`P0` `14／14` ✅）；`F21 wiring … caede20` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['W1', 'W2', 'W3']；rc 1`（`W4`／`W5` ✅）；`F21 run` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['受詞缺', 'R1', 'R2', 'R3@3.5', 'R4']；rc 1`（`R0` ✅：新判為相連之對 `19`〔同歸戶 `15`〕；`R3@0.0` ✅：段三紀錄 `0` 列）；`F16 run`（`verify/probes/probe_WG9357_k948.py run`）⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['R2@3.5']；rc 1`；`F12 run`（`verify/probes/probe_WG9353_endmerge.py run`）⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['X1@甲']；rc 1`（合成案甲之後處理 (a) 之停機訊息：開工態「所鄰之 B 內街廓 ＝ []」）；`F13 run`（`verify/probes/probe_WG9354_endcontest.py run`）⇒ **`rc 0`**，末列逐字 `⇒ 紅 []；rc 0`（塊 `F13p` 之上鎖三宗於開工態亦過·其出艙對未施 `F13p` 者唯合成案甲之表頭一列相異〔上鎖 `0 → 3`·咬到 `merge` `0 → 1`〕）；`F14 run`（`verify/probes/probe_WG9355_screenmerge.py run`·其 `SCEN` 取自 `F13`）⇒ **`rc 0`**，末列逐字 `⇒ 紅 []；rc 0`；`F3 run`（`verify/probes/probe_WG9344p1_pooltemp.py run … 3.5 on`）⇒ **`rc 1`**，末列逐字 `⇒ rc 1`（🔴 恰 `3` 項：`628-20(3)` 期 `['628-20(1)']`／實 `None`；`628-45(3)`、`628-45(4)` 期 `['628-20(1)', '628-45(1)', '628-45(2)']`／實 `['628-45(1)', '628-45(2)']`） |
| `8` | 發單側之原型（**⛔ 交付**·僅為量測器之必過之實例） | 發單側於倉外拋棄式工作樹依 `§三` 撰一原型（`app.py` 唯改 `k6_shares_segment` ＋ 新增常數與一輔助函式·⛔ 入倉·其 blob ⛔ 為本單之期），於其上 ＋ 塊 `F21`／`F16p`／`F12p`／`F13p`／`F3p`：`F21` 三子命令皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`（`selftest` `A1`〜`A13`〔`14` 例〕皆 ✅·`P0` `14／14`；`wiring` `W1`〜`W5` 皆 ✅·`W5` 之相異 ＝ `['K6_SHARE_COORD_TOL', '_k954_lin_len', 'k6_shares_segment']`；`run` 之 `R0`〜`R2`、`R3@3.5`、`R4`、`R3@0.0` 皆 ✅）；`F16`／`F12`／`F13`／`F14`／`F3` 之 `run` 皆 **`rc 0`**（`F16`／`F12`／`F13`／`F14` 之末列逐字 `⇒ 紅 []；rc 0`；`F3` 之末列逐字 `⇒ rc 0`）；`F12`／`F13`／`F14`／`F16` 之 `selftest`、`F12`／`F13` 之 `wiring`、`F3 selftest` 皆 `rc 0`；`§四-3` 閘 `8`〜`26` 之諸器皆 ＝ 其期（`k6s3 cmp` `0.0` 相異 `0` 項、`3.5` 相異恰 `11` 項 ＝ 項 `6`；`F8 run` `0.0` 之出艙對開工態逐位同、`3.5` 唯一列相異；`F10 run` 之 `diff` 恰項 `6` 所列之四處；`parity` `3.5` ⇒ `35`／`34`、`0.0` ⇒ `36`／`35`·不符格 `0`·`Z` ＝ `[('harness', 'R1-抵費地-2')]`；`wfns_ast` `48`／`48`／`47`；`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」；`F19 mut` `rc 0`·本部 `Z0`〜`Z2` 與四十一突變 `M1`〜`M41` 皆 ✅）。**CC 之碼⛔ 須同原型**；唯須滿足 `§三` 與 `§四` |
| `9` | `run_all`（開工態） | `python verify/run_all.py`（倉外拋棄式 worktree·殼無 `WV_`）：項 `64`·PASS `28`／FAIL `36`（末列 `W-V run_all: FAIL`·開工態之常態）；末端夾具／golden 列 `21／21`；對帳段 名目 凍存／現況 `22／36`。原型之 `run_all` 對之（`python verify/probes/probe_WG9343_step0_flag.py runall`）：相異項恰 `1`（`#24 v3·G值3.5m`·`FAIL → FAIL`·違規數 `295 → 299`·本體異）；其餘 `63` 項之名目、狀態、違規數與本體逐項同；golden `21／21`·相異 `0`；對帳段 `22／36 → 22／36` |

---

## `§二`　KL 之語與射程

🔒 **所據之裁**：
- **`K-9-54`**（KL `2026-09-30 20:34`·逐字「是」·本批入典·塊 `K6`）：地籍界線之座標相差在 `0.1 mm` 以內者，視為共用同一段界線（`K-6 §一` 之相連）；由此所生之退縮 `3.5 m` 段三後處理之變動（地主甲之公設地上之土地改由三街廓平分）KL 接受。所呈之全文與 KL 之答 ＝ 塊 `K6` 逐字（含所呈二處失準之 `🔧` 註·`自誤 560`／`561`）。
- **`K-9-53`**（KL `2026-09-30 18:40`·逐字「是」·本批入典·⛔ 本批落地·塊 `K6`）：地主已有配得土地者，手冊先行、併不進去者始入合併單位沿名單調配——其碼屬規格步 `4` 之單；本批唯入典。
- `K-6 §一`（合併群述詞·「共用線段（兩端完全共點；單點相接不算）」）；`K6_SHARE_MIN_LEN` 之原註（逐字「兩端完全共點於浮點下不可判」）；`K-9-25`（有面積之縫隙⛔ 密合·⛔ 牴觸）；`K-9-48` 其三·讀法 `5`（公設地上之土地於合併群所跨之已配得之街廓平分·段三後處理之既有之碼·⛔ 動）。
🔒 **流程之令**：規格單流程之常態（KL `2026-09-29 20:20`·`docs/orders/W-G.9-358_輕量單.md` `§二`）；附則甲〜丙（恆常附款登記表「`n③` 之試行期變通之期滿與續行」節 ③ 之 `2`）：甲 本單⛔ 令任何片「維持原狀」（本批之土地後果全由既有之段三後處理依新之相連之判所生，`§一` 項 `6` 已逐宗列之）；乙 同一量之判、寫、讀出自同一式（`§三-1` `R-2`：相連之判與所回之長出自同一式·`R-3`）；丙 CC 之唯讀獨立 reviewer 列為工項二之常設步（驗後、推前·停機款 `12`）。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 逐字放行**。
🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至新側支 `verify/W-G.9-361-k954`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及 `app.py` 之 `k6_shares_segment`（及其新增之輔助函式、常數）以外之生產碼、`§三-3` 之禁改、任何他錨；`(d)` ⛔ 及規格步 `4`（`K-9-53` 之碼·`adj_intake` 之分類之改·`F20` 之入倉）——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **受詞之總述**：`app.py` 模組層 `k6_shares_segment(poly_a, poly_b, min_len=None)`（`K-6 §一` 之「共用線段」之唯一判準·其呼叫者 ＝ `k6_merge_groups`、`k929_6_fixpoint`、`k6b_stage3_run` 之 `_adj`／`_nbr_blocks`、`k6_step0_merge`、`k6_merge_selftest`；`end_block_merge_run` 經 `k6_merge_groups`）：現以二片邊界之精確交集之線性部分之總長判之。**本批於「精確之長未達門檻」之後補上座標容差之重判**（`K-9-54`）；精確之長已達門檻者，一切（布林與所回之長）逐位同現碼。harness 與畫面二路徑皆呼叫同一函式 ⇒ 二路徑同受之；諸呼叫者之碼⛔ 動。

**用語**（本節專用）：「**精確之長** `E`」＝ 現碼所算之 `_tot`（`poly_a.boundary.intersection(poly_b.boundary)` 之線性部分之總長）；「**門檻** `m`」＝ `min_len`（`None` ⇒ `K6_SHARE_MIN_LEN`）；「**容差** `ε`」＝ `K6_SHARE_COORD_TOL`；「**線長** `λ(g)`」＝ 幾何 `g` 之 `LineString`／`LinearRing` 之長之和（`Multi*`／`GeometryCollection` 逐元素下探；`Point`／`MultiPoint` 計 `0`）。

### `§三-1`　行為要求（逐條·「給定何種情形、須得何種結果」）

| # | 給定 | 須得 |
|---|---|---|
| `R-1` | 常數（`K-9-54`） | module 層之新具名常數 **`K6_SHARE_COORD_TOL = 0.0001`**（單位 m），置於 `K6_SHARE_MIN_LEN` 之定義（含其後之三列註）之後、`def k6_shares_segment` 之前；全檔恰一處賦值。`K6_SHARE_MIN_LEN` 之定義與其註一字不動 |
| `R-2` | `k6_shares_segment(poly_a, poly_b, min_len=None)` | 簽名⛔ 變。① `poly_a` 或 `poly_b` 為 `None` ⇒ `(False, 0.0)`（同現碼）；② 精確之長 `E` 之算法（含其 `try`／`except` ⇒ `(False, 0.0)`）一字不動；③ `E ≥ m` ⇒ **`(True, E)`**（布林與長皆逐位同現碼）；④ `E < m` ⇒ 重判：`poly_a.distance(poly_b) > ε` ⇒ `(False, E)`；否則 `L₁ ＝ λ(poly_a.boundary ∩ poly_b.boundary.buffer(ε))`、`L₂ ＝ λ(poly_b.boundary ∩ poly_a.boundary.buffer(ε))`、`L ＝ min(L₁, L₂)`：`L ≥ m` ⇒ **`(True, L)`**；否則 ⇒ **`(False, E)`**；⑤ ④ 之任一幾何運算拋例外 ⇒ `(False, E)`（⛔ 靜默改判相連） |
| `R-3` | 判與長之同式（附則乙） | 同一 `(poly_a, poly_b, min_len)` 之布林與所回之長出自 `R-2` 之同一分支（③ 之 `E` 或 ④ 之 `L`）；`(a, b)` 與 `(b, a)` 同判、同長（`L` 取二向之小者） |
| `R-4` | `min_len ＝ 0.0` 之呼叫（`k6_merge_selftest` 之 `S-5` 族·`自誤` 所記之退化） | `E ≥ 0` 恆真 ⇒ ③（同現碼·⛔ 進 ④） |
| `R-5` | 既有之自檢 `k6_merge_selftest()`（`S-1`〜`S-7`） | 一字不動而仍過（`S-1` 之長 `1.0`、`S-2` 之 `(False, 0.0)`、`S-5` 之 `(False, 0.005)` 皆逐位同） |
| `R-6` | 本案（harness·退縮 `3.5`／`0.0`） | **退縮 `0.0`**：段三、宗地、配地、末端塊之合併再試、調配之輸入 ——**逐位同開工態**（`V-2`〜`V-5`）；**退縮 `3.5`**：唯 `§一` 項 `6` 所列之改變（段三紀錄 `18 → 19` 列：後處理之 `628-20(3)`〔`(b)`·受併宗 `628-20(1)`·`42.15`〕新增、`628-45(3)`／`628-45(4)`〔`(c)`〕之受併宗 `628-45(1)`／`628-45(2)` → `628-20(1)`／`628-45(1)`／`628-45(2)` 各 `91.03`／`74.8667`；其配地、抵費地、調配之輸入之變 ＝ `§一` 項 `6`）；此外⛔ 任何改變 |
| `R-7` | 呼叫者 | `k6_merge_groups`、`k929_6_fixpoint`、`k6b_stage3_run`、`end_block_merge_run`、`k6_step0_merge`、`k6_merge_selftest` 及畫面之諸函式一字⛔ 動（其行為之變全由 `R-2` 所生） |

### `§三-2`　介面（名與簽名·量測器 `F21` 以之為受詞）

| # | 名 | 簽名／回傳 | 呼叫端 |
|---|---|---|---|
| `I-1` | 新 `K6_SHARE_COORD_TOL`（`0.0001`） | `R-1` | `k6_shares_segment`（`R-2` ④）；他處⛔ 引之（`F21 wiring` `W3`） |
| `I-2` | 改 `k6_shares_segment` | `(poly_a, poly_b, min_len=None)` → `(bool, float)`（`R-2`） | 同現碼（`R-7`） |
| `I-3` | 新之模組層輔助函式（得有·名由 CC 定） | 唯為 `k6_shares_segment` 所呼叫（`λ` 之類） | `k6_shares_segment` |

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

| # | 禁 | 所護之閘 |
|---|---|---|
| `X-1` | `app.py` 之頂層節點對開工態相異者 ⊆ {`k6_shares_segment`、`K6_SHARE_COORD_TOL`、新增而唯為 `k6_shares_segment` 所呼叫之函式}（AST·⛔ 計註解與空列） | `F21 wiring caede20` 之 `W5` |
| `X-2` | `k6_shares_segment` 內之既有字樣 `_it = _ba.intersection(_bb)` 須存（精確之長先算·`R-2` ②） | `F21 wiring` 之 `W2` |
| `X-3` | `K6_SHARE_MIN_LEN` 之值與其註一字不動；`k6_merge_selftest` 一字不動 | `F21 selftest` 之 `A12`／`A13`；`R-5` |
| `X-4` | `_WF_NS_NAMES` 一字不動 | `wfns_ast` `48`／`48`／`47` |
| `X-5` | `verify/` 之一切檔一字不動，唯 `probes/probe_WG9361_k954.py`（工項一·新檔）之增與 `probes/probe_WG9357_k948.py`／`probes/probe_WG9353_endmerge.py`／`probes/probe_WG9354_endcontest.py`／`probes/probe_WG9344p1_pooltemp.py`（塊 `F16p`／`F12p`／`F13p`／`F3p`·工項一）之改 | `F9`〜`F19`、`main_synth`、`parity`、`run_all` |
| `X-6` | 新碼⛔ 含案件字面（街廓名、側別、地號、分區名之字串常數·`CASE_LIT_RE` 之形）；`k6_shares_segment` 內⛔ 字面 `0.0001`／`1e-4`（以 `K6_SHARE_COORD_TOL` 為之） | 泛化之鐵則；`F21 wiring` `W4` |
| `X-7` | `def main` 一字不動 | `main_synth`、`F4 wiring`、`F9 wiring`、`F10 wiring`、`F15 wiring` |

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`D-1`：本規格之任一條，其二讀法之後果**在土地上相異**（任一合併群、段三之任一列、任一宗之面積）。
`D-2`：`R-2` ④ 於某情形無從依本規格定之（例：二片之邊界含非有限之坐標）。
`D-3`：須動 `§三-3` 之任一字始能滿足 `§三-1`。
🔒 非域上之實作細節（輔助函式之名與切分、註解、`buffer` 之解析度參數〔⛔ 設則用 `shapely` 之預設〕）由 CC 定之，並於報告 ⑦ 逐項具名其選擇與其由。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐 `R-1`〜`R-7`：落於何函式、何處；`§三-4` 末之實作細節之選擇及其由；對 `§三-3` 各款之自查（逐款具名「未觸」及其據）；附則乙之自查（`R-3`：判與長之同式）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py` 之**全文**（報告內嵌或報告同目錄之 `.diff` 檔·⛔ 摘要）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-361_規格單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-361 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-361-k954`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`34`**、主線仍 ＝ `caede20…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-361-k954`（快轉）。

**工項一　量測器入倉與既有量測器之錨之更新**（**先於生產碼**·新側支·零生產碼）：塊 `F21` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9361_k954.py`（**新檔**）；塊 `F16p`／`F12p`／`F13p`／`F3p` 各抽為 `<O>\F16p.diff`／`<O>\F12p.diff`／`<O>\F13p.diff`／`<O>\F3p.diff`、對拍後各 `git apply --check` ⇒ 過；各 `git apply`；五檔之 `git hash-object` ＝ `§五-1` 項 `11`（停機款 `3`）。`commit` 訊息逐字 `W-G.9-361 工項一：量測器 F21（地籍相連之判之座標容差）入倉 ＋ F3／F12／F13／F16 之錨之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-361-k954`。

**工項二　生產碼**（🔴 `app.py`·CC 依 `§三` 撰寫·一 `commit`·推新側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9361_k954.py selftest <repo>`；`… wiring <repo> caede20`；`… run <repo>` ⇒ 皆 **`rc 1`**（末列逐字 ＝ `§一` 項 `7`）。
2. `python verify/probes/probe_WG9357_k948.py run <repo>`；`python verify/probes/probe_WG9353_endmerge.py run <repo>`；`python verify/probes/probe_WG9354_endcontest.py run <repo>`；`python verify/probes/probe_WG9355_screenmerge.py run <repo>`；`python verify/probes/probe_WG9344p1_pooltemp.py run <repo> 3.5 on` ⇒ 其 `rc` 與末列逐字 ＝ `§一` 項 `7`。
3. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`（皆 `rc 0`）。
4. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）；`python verify/probes/probe_WG9351_intake.py run <repo> > <O>\f10_pre.log`（`rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫 `app.py` 之改動；`python -m py_compile app.py`；`commit` 訊息逐字 `W-G.9-361 工項二：地籍相連之判之座標容差（K-9-54·GB-195）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9361_k954.py selftest <repo> > <O>\f21_self_post.log`；`… wiring <repo> caede20 > <O>\f21_wir_post.log`；`… run <repo> > <O>\f21_run_post.log` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `A1`〜`A13`（`14` 例）皆 ✅、`P0` `14／14`；`wiring` 之 `W1`〜`W5` 皆 ✅（`W5` 之相異 ⊆ {`k6_shares_segment`、`K6_SHARE_COORD_TOL`、新增之輔助函式}）；`run` 之 `R0`〜`R2`、`R3@3.5`、`R4`、`R3@0.0` 皆 ✅（新判為相連之對 `19`〔同歸戶 `15`〕；合併群相異之歸戶 ＝ `G005`／`G007`／`G012`／`G017`／`G022`） |
| `V-2` | `python verify/probes/probe_WG9357_k948.py run <repo> > <O>\f16_run_post.log`；`python verify/probes/probe_WG9353_endmerge.py run <repo> > <O>\f12_run_post.log`；`python verify/probes/probe_WG9354_endcontest.py run <repo> > <O>\f13_run_post.log`；`python verify/probes/probe_WG9355_screenmerge.py run <repo> > <O>\f14_run_post.log`；`python verify/probes/probe_WG9344p1_pooltemp.py run <repo> 3.5 on > <O>\f3_run_post.log` | 皆 **`rc 0`**；其末列逐字 ＝ `§一` 項 `8` |
| `V-3` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`python verify/probes/probe_WG9344_k6s3.py cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`（段三紀錄 `3.5` ⇒ `19` 列、`0.0` ⇒ `0` 列）；`cmp` 之 `0.0` ⇒ **`rc 0`**（相異 `0` 項）；`cmp` 之 `3.5` ⇒ **`rc 1`**，相異恰 **`11`** 項 ＝ `§一` 項 `6` 所列（宗 `628-45(2)` 之 `a`／`G`、`628-45(1)` 之 `a`／`G`、`628-20(1)` 之 `a`／`G`、`628-18(2)` 之 `G`、`628-7(2)` 之 `G`、抵費地 `R3`／`R5`／`R6`；其值於 `0.01` 內 ＝ 該項所載）；街角得標、強制旗標⛔ 在相異之列 |
| `V-4` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `diff`；`python verify/probes/probe_WG9351_intake.py run <repo> > <O>\f10_post.log` 與前置 `4` 之 `diff` | 皆 **`rc 0`**；`0.0` 之 `diff` **空**；`3.5` 之 `diff` 恰一列之改（「逐街廓（配地宗數·ΣG）」之列·`§一` 項 `6`）；`F10 run` 之 `diff` 恰 ＝ `§一` 項 `6` 所列之四處（待同歸戶併入之歸戶 `9 → 8`、原位次配地 `43 片·21412.68 ㎡ → 44 片·21454.83 ㎡`、共同負擔用地·待同歸戶併入 `13 片·2680.00 ㎡ → 12 片·2637.85 ㎡`、`G007` 之 `628-20(3)` 之待併列之去） |
| `V-5` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | 皆 **`rc 0`**；配地列 `3.5` ⇒ harness `35`／畫面 `34`、`0.0` ⇒ `36`／`35`，不符格 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`（畫面與 harness 同受 `K-9-54`） |
| `V-6` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`、FAIL `36 → 36`；**相異項恰 `1`**：`#24 v3·G值3.5m`（`FAIL → FAIL`·違規數 `295 → 299`·本體異）；其餘 `63` 項之名目、狀態、違規數與本體逐項同；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`1`**（`app.py`）；其 blob 與增／刪之數出艙（發單側復驗時自倉重算）；`verify/` 之一切檔對工項一之端相異 `0` |
| `V-8` | `§四-3` 閘 `8`〜`26` 之諸器（於工項二之 `commit`） | 皆 ＝ 其期 |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-8`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-361-k954`。

**工項三　入典與登記**（新側支·零生產碼·一 `commit`）：塊 `K6` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `G5` 附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；塊 `E8` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P15` 附於 `CLAUDE.md` 之末（皆二進位·嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-361 工項三：K-9-53／K-9-54 之入典 ＋ GB-195 之立 ＋ 自誤 558〜561 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-361-k954`。

**工項四　執行報告入倉**（新側支·新檔 `docs/reports/W-G.9-361R_地籍相連之判之座標容差_執行報告.md`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F21` 三子命令之全文、`F16`／`F12`／`F13` 之 `run` 之全文、`k6s3 cmp` 二份之全文、`F8 run` 二份與 `F10 run` 之 `diff` 之全文、`parity` 二份之末十列、`runall` 對拍之全文與 `diff` 之結果）；④ 七塊之實得（bytes／`sha256`）與四檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **`app.py` 之全文差異**（`§三-5`）；⑨ **各段耗時**（讀單／撰碼／前置／驗／審查／登記／報告）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-361 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-361-k954`。

### `§四-2`　復驗時補寫者（規格單流程·⛔ 本單之期）

發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之精確先、重判後；`R-2` ④ 之二向取小、相距之先篩；`R-2` ⑤ 之例外 ⇒ 不相連）及其突變之判別力；併入主線之請示（有土地後果·`K-9-54` 已裁接受·附畫面之核對）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9361_k954.py` `489`／`0`、`verify/probes/probe_WG9357_k948.py` `5`／`2`、`verify/probes/probe_WG9353_endmerge.py` `10`／`3`、`verify/probes/probe_WG9354_endcontest.py` `6`／`2`、`verify/probes/probe_WG9344p1_pooltemp.py` `5`／`2`（增／刪·即塊之 `@@` 所載）；工項二 ＝ `app.py`（增／刪 ＝ 工項二之 `V-7` 所出艙）；工項三四 逐檔 **`0`** |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `caede20` | 生產碼相異恰 **`1`**（`app.py` ＝ 工項二之 `V-7` 所出艙之 blob）；`verify/` 之一切檔相異恰 **`5`**（新檔 `verify/probes/probe_WG9361_k954.py` ＋ 塊 `F16p`／`F12p`／`F13p`／`F3p` 所改之四檔·blob 皆 ＝ `§五-1` 項 `11`）；本批之新檔（本單、`F21`、報告）之 `git check-ignore` 皆無命中 |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`12` 檔：本單、`F21`、塊 `F16p`／`F12p`／`F13p`／`F3p` 所改之四檔、`app.py`、`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md`、報告） |
| `4` | 四檔之 bytes | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `445942` → **`456122`**；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1022244` → **`1025554`**；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `1089994` → **`1096049`**；`CLAUDE.md` `317190` → **`320678`**；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`34`**；主線 ＝ `caede209cb769fbea2986ffe712e835ff052549b`（⛔ 變）；`verify/W-G.9-361-k954` ＝ 工項四之 `commit`，其祖含 `caede20`；`verify/W-G.9-359-cand` ＝ `bd072eb…`、`verify/W-G.9-357-k948` ＝ `4716f20…`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 561 557 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 561 557` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`546`**／`MAX` **`561`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；**`GB` `188`／`195`**／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；**`K-9` `51`／`54`**／`[44, 47]`（`VR` ＝ 開工態；自誤唯增 `558`〜`561`、`GB` 唯增 `195`、`K-9` 唯增 `53`／`54`） |
| `8` | `python verify/probes/probe_WG9361_k954.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑> caede20`；`… run <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`48`／`48`／`47`** |
| `10` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `11` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `12` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest …`；`… wiring …` | 皆 **`rc 0`** |
| `14` | `python verify/probes/probe_WG9350_frontroad.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `15` | `python verify/probes/probe_WG9351_intake.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `16` | `python verify/probes/probe_WG9352_endblock.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `17` | `python verify/probes/probe_WG9353_endmerge.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `18` | `python verify/probes/probe_WG9354_endcontest.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `19` | `python verify/probes/probe_WG9355_screenmerge.py selftest …`；`… run …` | 皆 **`rc 0`** |
| `20` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring …` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `21` | `python verify/probes/probe_WG9345_screen.py parity … 3.5 on <json>`；同 `0.0`；`… wiring …`；`python verify/probes/probe_WG9345_screen.py selftest` | 皆 **`rc 0`**（`parity` 之數 ＝ `V-5`） |
| `22` | `python verify/probes/probe_WG9344p1_pooltemp.py run <repo 絕對路徑> 3.5 on`；`… selftest`；`python verify/probes/probe_WG9344_k6s3.py selftest` | 皆 **`rc 0`** |
| `23` | `python verify/probes/probe_WG9357_k948.py selftest …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`（`selftest` 之 `P0` `25／25`） |
| `24` | `python verify/probes/probe_WG9358_k948_wiring.py wiring …` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `25` | `python verify/probes/probe_WG9359_cand.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `26` | `python verify/probes/probe_WG9360_cand_mut.py mut <repo 絕對路徑>` | **`rc 0`**；本部 `Z0`〜`Z2` 皆 ✅；四十一突變 `M1`〜`M41` 皆 ✅；末列逐字 `⇒ 紅 []；rc 0` |

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F21` | `25171` B·`sha256` `3bb511d9383ffdc8aea40b9835a955e0871fef96bb957bbba29a984a2b4d9edb`·`489` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9361_k954.py` |
| `3` | 塊 `F16p` | `1601` B·`sha256` `7e97eb959cc9cfc5f8bb5ee4a5d830e20e1362cf4c4c163e7cfaaa79391fc402`·`16` 列（圍欄內全文·末附換行）；抽為 `<O>\F16p.diff`，`git apply` 於 `verify/probes/probe_WG9357_k948.py`（施前 blob `c7515d3ecc2f8413899fb18affdee6b3cdec1228`） |
| `4` | 塊 `F12p` | `2895` B·`sha256` `2c7e542d1bd7a5ea95aac0c8cc5f1b5ab8a24d7155f41b0df40fafcce2e62cb1`·`38` 列（圍欄內全文·末附換行）；抽為 `<O>\F12p.diff`，`git apply` 於 `verify/probes/probe_WG9353_endmerge.py`（施前 blob `c12d3f85f394662630e7edd8abc7ca90f98af086`） |
| `5` | 塊 `F13p` | `2153` B·`sha256` `75f81b230730bd0f376af6c3201e362fe795def17cac64eccaf91ef84297b248`·`24` 列（圍欄內全文·末附換行）；抽為 `<O>\F13p.diff`，`git apply` 於 `verify/probes/probe_WG9354_endcontest.py`（施前 blob `2f81f739211589dab965504f252c883ad8a1a7e9`）；`verify/probes/probe_WG9355_screenmerge.py`（`F14`）⛔ 改（其 `SCEN` 取自 `F13`·隨之） |
| `6` | 塊 `F3p` | `770` B·`sha256` `a4799d8bf2e347c87efbe09bac2ed65b8caf09464d5b64b01c4265503af901cb`·`16` 列（圍欄內全文·末附換行）；抽為 `<O>\F3p.diff`，`git apply` 於 `verify/probes/probe_WG9344p1_pooltemp.py`（施前 blob `9a5459fe8d11c42f886a8c7c4427f46e5748a940`） |
| `7` | 塊 `K6` | `10180` B·`sha256` `1ab1ae5a28821714cc431e1b8ab2abff1611e994710aaadbf21601dfcc937dcf`·`84` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`445942` B）之末後，期末 ＝ `456122` B |
| `8` | 塊 `G5` | `3310` B·`sha256` `abdd5849ac36ef0bf0b6ce94b9b76360d934bcad676077a11f35c26393f2dbda`·`15` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1022244` B）之末後，期末 ＝ `1025554` B |
| `9` | 塊 `E8` | `6055` B·`sha256` `cda2b01ebc3f8ed61f91e98f96d4c825fcc13a2a79d603782e2d103854c7a41b`·`42` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1089994` B）之末後，期末 ＝ `1096049` B |
| `10` | 塊 `P15` | `3488` B·`sha256` `c0e7f716ad0c70cffca9c36f01b7e6070d24288a010d5677c3cd87accd635203`·`20` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`317190` B）之末後，期末 ＝ `320678` B |
| `11` | 寫出後之 blob | `verify/probes/probe_WG9361_k954.py` `663c31e22ea63a047c813b905ad6bd5aa4a124e9`；`verify/probes/probe_WG9357_k948.py` `cabeff97d6b14244582ec7ec19c9a58578eb0612`；`verify/probes/probe_WG9353_endmerge.py` `2fb3c92b809680fb7e46269615ab46876657b9e5`；`verify/probes/probe_WG9354_endcontest.py` `26d7c9e0227105325c5656f6e1d3d032a8f7508c`；`verify/probes/probe_WG9344p1_pooltemp.py` `48ab705ec8db4c23436cd4e7054e1b0d52f3a3e4`。🔒 `app.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `12` | 量測器之二態 | 工項一之端（`caede20` ＋ 塊 `F21`／`F16p`／`F12p`／`F13p`／`F3p`）：`F21` 三子命令皆 `rc 1`；`F16`／`F12`／`F3` 之 `run` 皆 `rc 1`；`F13`／`F14` 之 `run` 皆 `rc 0`（塊 `F13p` 之上鎖於開工態亦過）（`§一` 項 `7`）；工項二施後：皆 `rc 0`（`§一` 項 `8` 之原型為其必過之實例） |
| `13` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗六十實跑（態 `caede20`）：🔴 機械 `0` 項／🟡 提示 `10` 項——`P-1` `:905`（附錄丙塊 `K6` 之 `K-9-53` 之射程·所否定者係射程之界〔未有配得土地之地主〕、⛔ 為量之全稱 ⇒ **具名豁免**）、`P-4` `:78`（`§一` 之表頭·其箭頭之座標系 ＝ 開工態 `caede20` 至原型，項 `6` 自載 ⇒ **具名豁免**）、`P-4` `:124`（`§三-2` 之表頭·所觸之箭頭係簽名之回傳 ⇒ **具名豁免**）、`P-4` `:178`（`§四-1` 工項二之驗之表頭·其箭頭之座標系 ＝ 工項一之端〔前置〕至工項二之 `commit`〔驗〕，表內自載 ⇒ **具名豁免**）、`P-4` `:205`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `caede20` 至工項三／四之端，表內自載 ⇒ **具名豁免**）、`P-4` `:976`（附錄丁塊 `G5`·所觸之箭頭係排程之序〔側支 → 次單〕⇒ **具名豁免**）、`P-4` `:994`／`:1004`（附錄戊塊 `E8` 之 `自誤 558`／`559` 之「形」·所觸之箭頭係攔點之序與交接文五十九之逐字引文〔片之去處〕⇒ **具名豁免**）、`P-4`／`P-6` `:1049`（附錄己塊 `P15` 之「前節之更正」起之段·所觸之數 `41` 之出處 ＝ `F19` 之突變之名 `M1`〜`M41`〔`自誤 558`〕、其箭頭係依賴序 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `20306`–`28026`）⇒ `rc 0` |
| `14` | 收工閘之模擬（發單側·本機 Linux·原型之工作樹 ＋ 九塊·⛔ `push`） | `git worktree add --detach <S> caede20`（拋棄式·⛔ `push`）＋ 本單 ＋ 塊 `F21`／`F16p`／`F12p`／`F13p`／`F3p` ＋ 原型之 `app.py` ＋ 塊 `K6`／`G5`／`E8`／`P15` ＋ 報告之替身·五 `commit`：閘 `1` 之刪除欄（工項一 ＝ `0`／`2`／`3`／`2`／`2`〔`F21`／`k948`／`endmerge`／`endcontest`／`pooltemp`〕；工項二 ＝ 原型之數·⛔ 為期；餘皆 `0`）；閘 `2` 生產碼相異 `1`（`app.py`）、`verify/` 相異 `5`（`A` `1`·`M` `4`）；新檔三之 `git check-ignore` 皆無命中；閘 `3` CR `0`（`12` 檔·`V6.dxf` `12308`）；閘 `4` 四檔皆嚴格前綴、其末 ＝ 本表項 `7`〜`10`；閘 `6` `rc 0`（二閘皆過）；閘 `7` `rc 0`·四簿 ＝ 自誤 `546`／`561`、`GB` `188`／`195`、`VR` `80`／`95`、`K-9` `51`／`54`／`[44, 47]`；閘 `8` `F21` 三子命令皆 `rc 0`；閘 `9`〜`26` ＝ `§一` 項 `8`（原型之 `app.py` 與 `verify/` 之一切檔與模擬之工作樹逐位同） |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````diff `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-361-k954`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F21`（新檔 `verify/probes/probe_WG9361_k954.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-361 量測器（發單側窗六十擬·檔 F21·⛔ 由受單側改一字）：地籍相連之判之座標容差（`K-9-54`·`GB-195`）。

`K-6 §一`：合併群 ＝ 同歸戶 ∧ 幾何連通（重劃前地籍上共用線段·單點相接不算）。現碼以二片邊界之精確交集之
線長判之；二片之界線於圖上重合而其座標有微米級之差者（本案 R4／R5／R6 之分配線兩側、公園 G1 與道路 RD3 之
間），精確交集為點 ⇒ 判為不相連。`K-9-54`（KL `2026-09-30 20:34` 逐字「是」）：界線座標相差在 `0.1 mm`
以內者視為共用同一段界線（相連）。

子命令（一律 python verify/probes/probe_WG9361_k954.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k6_shares_segment`／`k6_merge_groups`／
           `k6_merge_selftest` 與 `K6_SHARE_MIN_LEN`、`K6_SHARE_COORD_TOL`）。
           A1〜A3 ＝ 精確之判之既有行為逐位同（共邊長 1 ⇒ (True, 1.0)；角點相接 ⇒ (False, 0.0)；
           共邊長 0.005 ⇒ (False, 0.005)）；A4〜A7 ＝ 重判（微米級之錯位而共線 ⇒ 相連、其長≈共線長；
           平行錯位 2e-4 m ⇒ 不相連；錯位在容差內而共線長未達門檻 ⇒ 不相連、其長 ＝ 精確之長；
           二片相距逾容差 ⇒ 不相連）；A8 ＝ 本案坐標量級（1e5〜1e6 m）之微米錯位；A9 ＝ 缺片 ⇒ (False, 0.0)；
           A10〜A11 ＝ 合併群（三片鏈之第二環為微米錯位 ⇒ 一群；錯位 2e-4 ⇒ 二群）；A12 ＝ 常數；
           A13 ＝ 既有之 `k6_merge_selftest()` 仍過；P0 ＝ 判式自驗。
  wiring   <repo> [<基準 rev>]
           AST：W1 模組層 `K6_SHARE_COORD_TOL = 0.0001` 恰一處；W2 `k6_shares_segment` 先算精確交集
           （既有之字樣 `_it = _ba.intersection(_bb)` 存）、其後引 `K6_SHARE_COORD_TOL`；W3 除
           `k6_shares_segment` 及其所呼叫之模組層函式外，⛔ 他處引 `K6_SHARE_COORD_TOL`；W4 生產碼⛔ 案件字面；
           W5（給基準 rev 時）`app.py` 之頂層節點對基準 rev 相異者 ⊆ {`k6_shares_segment`、`K6_SHARE_COORD_TOL`、
           新增而唯為 `k6_shares_segment` 所呼叫之函式}。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R0 新判為相連之對（段三之輸入之切片·精確共線長 < 0.01 而
           相距 ≤ 1e-4 且二向容差共線長之小者 ≥ 0.01）＝ `19` 對（同歸戶 `15`）、其頂點至他片界線之距之最大者
           < `2e-5 m`；R1 合併群（段三之輸入之全部重劃前切片）＝ 外部錨（本器另寫之
           判·⛔ 呼叫 `k6_shares_segment`）；R2 與精確之判相異之歸戶 ＝ `G005`／`G007`／`G012`／`G017`／`G022`，
           其群如 `GROUPS_TOL`；R3 段三之紀錄（`3.5` ⇒ `19` 列·`0.0` ⇒ `0` 列）與 `3.5` 之後處理之
           `628-20(3)`／`628-45(3)`／`628-45(4)` 三列；R4 `3.5` 之配地（三受併宗之 `G`、`R3`／`R5`／`R6` 之抵費地）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FUNCS = ["k6_shares_segment", "k6_merge_groups", "k6_merge_selftest"]
CONSTS = ["K6_SHARE_MIN_LEN", "K6_SHARE_COORD_TOL"]
TOL = 1e-4
MINLEN = 0.01
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
# `K-9-54` 之後，與精確之判相異之歸戶之合併群（本案·退縮無涉·段三之輸入之切片）
GROUPS_TOL = {
    "G005": [["628-18(1)", "628-18(2)", "628-18(3)"]],
    "G007": [["628-20(1)", "628-20(2)", "628-20(3)", "628-30(1)", "628-30(2)", "628-30(3)", "628-30(4)",
              "628-45(1)", "628-45(2)", "628-45(3)", "628-45(4)", "628-45(5)"]],
    "G012": [["628-5(1)", "628-5(2)"]],
    "G017": [["628-21(1)", "628-21(2)", "628-22(1)", "628-22(2)", "628-22(3)", "628-23(1)", "628-23(2)",
              "628-23(3)"]],
    "G022": [["628-7(1)", "628-7(2)", "628-7(3)", "628-7(4)"]],
}
# 退縮 3.5 之段三後處理（`K-9-48` 讀法 5·`K-9-51`）之 G007 三列：(候選, 層級, 受併宗集, {受併宗: 併入量})
S3_ROWS_35 = [
    ("628-20(3)", "後處理(b)", ["628-20(1)"], {"628-20(1)": 42.15}),
    ("628-45(3)", "後處理(c)", ["628-20(1)", "628-45(1)", "628-45(2)"],
     {"628-20(1)": 91.03, "628-45(1)": 91.03, "628-45(2)": 91.03}),
    ("628-45(4)", "後處理(c)", ["628-20(1)", "628-45(1)", "628-45(2)"],
     {"628-20(1)": 74.8667, "628-45(1)": 74.8667, "628-45(2)": 74.8667}),
]
NEW_PAIRS = (19, 15)   # 段三之輸入之切片中，新判為相連之對之數與其中同歸戶者之數（本案）
G_35 = {"628-45(2)": 902.52, "628-45(1)": 525.28, "628-20(1)": 461.06}
POOL_35 = {"R3": 1883.03, "R5": 1742.99, "R6": 1777.33}


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__)
    out.append((name, got, exp))


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


# ── 玩具（⛔ 本案資料）──
def _P(pts):
    from shapely.geometry import Polygon
    return Polygon(pts)


def _sq(x0, y0, x1, y1):
    return _P([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def _bt(res, nd=3):
    """(bool, 長) ⇒ (bool, 長之 nd 位小數)。"""
    return (bool(res[0]), round(float(res[1]), nd))


def _cases(ns):
    sh, mg = ns["k6_shares_segment"], ns["k6_merge_groups"]
    c = []
    a = _sq(0, 0, 1, 1)
    # A1〜A3：精確之判之既有行為（長度逐位）
    _run(c, "A1 精確共邊（長 1）⇒ (True, 1.0)·長度逐位", lambda: (bool(sh(a, _sq(1, 0, 2, 1))[0]),
                                                           sh(a, _sq(1, 0, 2, 1))[1] == 1.0), (True, True))
    _run(c, "A2 角點相接 ⇒ (False, 0.0)·長度逐位", lambda: (bool(sh(a, _sq(1, 1, 2, 2))[0]),
                                                      sh(a, _sq(1, 1, 2, 2))[1] == 0.0), (False, True))
    _run(c, "A3 精確共邊 0.005 ⇒ (False, 0.005)", lambda: _bt(sh(a, _sq(1, 0.995, 2, 2)), 9), (False, 0.005))
    # A4：b 之左邊自 (1+3e-6, -0.3) 至 (1-3e-6, 1.3)·與 a 之右邊（長 1）相距 ≤ 3e-6、精確交集為一點
    b4 = _P([(1 + 3e-6, -0.3), (2, -0.3), (2, 1.3), (1 - 3e-6, 1.3)])
    _run(c, "A4 微米級錯位而共線（精確交集為一點）⇒ 相連、其長 ≈ 1（三位小數）",
         lambda: (bool(sh(a, b4)[0]), round(float(sh(a, b4)[1]), 2)), (True, 1.0))
    _run(c, "A4′ 同 A4·精確交集之線長 ＝ 0（受詞確為現碼判為不相連之形）",
         lambda: round(sum(g.length for g in getattr(a.boundary.intersection(b4.boundary), "geoms",
                                                     [a.boundary.intersection(b4.boundary)])
                           if g.geom_type == "LineString"), 9), 0.0)
    # A5：平行錯位 2e-4（逾容差）⇒ 不相連、其長 ＝ 精確之長 0
    _run(c, "A5 平行錯位 2e-4 m ⇒ (False, 0.0)", lambda: _bt(sh(a, _sq(1 + 2e-4, 0, 2, 1)), 9), (False, 0.0))
    # A6：錯位 5e-5（容差內）而共線之長 0.008 ⇒ 不相連、其長 ＝ 精確之長 0
    b6 = _sq(1 + 5e-5, 0.992, 2, 2)
    _run(c, "A6 容差內而共線長 0.008 ⇒ (False, 0.0)", lambda: _bt(sh(a, b6), 9), (False, 0.0))
    # A7：二片相距 0.01（逾容差）⇒ 不相連
    _run(c, "A7 相距 0.01 m ⇒ (False, 0.0)", lambda: _bt(sh(a, _sq(1.01, 0, 2, 1)), 9), (False, 0.0))
    # A8：本案坐標量級之微米錯位（共線長 12）
    X0, Y0 = 310500.0, 2651850.0
    a8 = _P([(X0, Y0), (X0 + 10, Y0), (X0 + 10, Y0 + 12), (X0, Y0 + 12)])
    b8 = _P([(X0 + 10 + 2e-6, Y0 - 1), (X0 + 20, Y0 - 1), (X0 + 20, Y0 + 13), (X0 + 10 - 2e-6, Y0 + 13)])
    _run(c, "A8 坐標 ~3e5／2.6e6 m 之微米錯位（共線長 12）⇒ 相連、其長 ≈ 12",
         lambda: (bool(sh(a8, b8)[0]), round(float(sh(a8, b8)[1]), 1)), (True, 12.0))
    _run(c, "A9 缺片（None）⇒ (False, 0.0)", lambda: _bt(sh(None, a), 9), (False, 0.0))
    pk = lambda poly, ono: {"polygon": poly, "原地號": ono}  # noqa: E731
    A, B = _sq(0, 0, 1, 1), _sq(1, 0, 2, 1)
    C1 = _P([(2 + 3e-6, -0.2), (3, -0.2), (3, 1.2), (2 - 3e-6, 1.2)])
    C2 = _sq(2 + 2e-4, 0, 3, 1)
    own = {"A": "G1", "B": "G1", "C": "G1"}
    _run(c, "A10 三片鏈（A–B 精確、B–C 微米錯位）⇒ 一群",
         lambda: mg([pk(A, "A"), pk(B, "B"), pk(C1, "C")], own), [[0, 1, 2]])
    _run(c, "A11 三片鏈（B–C 平行錯位 2e-4）⇒ 二群",
         lambda: mg([pk(A, "A"), pk(B, "B"), pk(C2, "C")], own), [[0, 1], [2]])
    _run(c, "A12 常數 K6_SHARE_COORD_TOL ＝ 1e-4、K6_SHARE_MIN_LEN ＝ 0.01",
         lambda: (ns["K6_SHARE_COORD_TOL"], ns["K6_SHARE_MIN_LEN"]), (TOL, MINLEN))
    _run(c, "A13 既有之 k6_merge_selftest() 仍過（S-1〜S-7）",
         lambda: len(ns["k6_merge_selftest"]()) >= 16, True)
    return c


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in FUNCS + CONSTS if n not in ns]
    if [n for n in miss if n in FUNCS]:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    if miss:
        print(f"  🔴 受詞缺（常數）：{miss}——續跑行為之例（其例以例外記）")
    print("── 合成對照（harvest 之 app.py·⛔ 本案資料）──")
    cases = _cases(ns)
    red = (["受詞缺"] if miss else []) + _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    names = [c[0].split()[0] for c in cases]
    n_ok = 0
    base_red = [r for r in red if r != "受詞缺"]
    for i, (name, got, exp) in enumerate(cases):
        pert = [(n, g, ("擾動", e) if j == i else e) for j, (n, g, e) in enumerate(cases)]
        rr = _report(pert, verbose=False)
        n_ok += int(rr == sorted(set(base_red) | {name.split()[0]}, key=names.index))
    ok0 = n_ok == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {n_ok}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
def _top(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            out.setdefault(n.name, []).append(n)
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out.setdefault(t.id, []).append(n)
    return out


def _calls(fn):
    return {n.func.id for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}


def _wiring_checks(src, base_src):
    tree = ast.parse(src)
    top = _top(tree)
    chk = []
    asg = top.get("K6_SHARE_COORD_TOL", [])
    val = None
    if len(asg) == 1 and isinstance(asg[0].value, ast.Constant):
        val = asg[0].value.value
    chk.append(("W1 模組層 K6_SHARE_COORD_TOL = 0.0001 恰一處", len(asg) == 1 and val == TOL,
                f"賦值 {len(asg)} 處·值 {val!r}"))
    fns = top.get("k6_shares_segment", [])
    ok2, note2 = False, "無 k6_shares_segment"
    helpers = set()
    if len(fns) == 1:
        seg = ast.get_source_segment(src, fns[0]) or ""
        i_ex = seg.find("_it = _ba.intersection(_bb)")
        i_tol = seg.find("K6_SHARE_COORD_TOL")
        ok2 = i_ex >= 0 and i_tol > i_ex
        note2 = f"精確交集之字樣於 {i_ex}·容差之引於 {i_tol}"
        helpers = {h for h in _calls(fns[0]) if h in top and isinstance(top[h][0], ast.FunctionDef)}
    chk.append(("W2 k6_shares_segment 先算精確交集、其後引 K6_SHARE_COORD_TOL", ok2, note2))
    users = sorted({n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)
                    and any(isinstance(x, ast.Name) and x.id == "K6_SHARE_COORD_TOL" for x in ast.walk(n))})
    allowed = {"k6_shares_segment"} | helpers
    chk.append(("W3 K6_SHARE_COORD_TOL 唯 k6_shares_segment 及其所呼叫之函式引之",
                bool(users) and set(users) <= allowed, f"引之者 {users}；許 {sorted(allowed)}"))
    lits = []
    for nm in ["k6_shares_segment"] + sorted(helpers):
        for fn in top.get(nm, []):
            for x in ast.walk(fn):
                if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
                    lits.append((nm, x.value))
    chk.append(("W4 k6_shares_segment 及其所呼叫之函式⛔ 案件字面", not lits, f"{lits}"))
    if base_src is not None:
        btop = _top(ast.parse(base_src))
        dump = lambda ns_: {k: [ast.dump(v) for v in vs] for k, vs in ns_.items()}  # noqa: E731
        a_, b_ = dump(top), dump(btop)
        diff = sorted(k for k in set(a_) | set(b_) if a_.get(k) != b_.get(k))
        new_helpers = {h for h in helpers if h not in btop}
        ok5 = set(diff) <= ({"k6_shares_segment", "K6_SHARE_COORD_TOL"} | new_helpers)
        chk.append(("W5 頂層節點對基準 rev 相異者 ⊆ {k6_shares_segment, K6_SHARE_COORD_TOL, 新增之其所呼叫者}",
                    ok5, f"相異 {diff}"))
    return chk


def wiring(repo, base=None):
    src = _read(repo, "app.py")
    base_src = None
    if base:
        try:
            base_src = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True,
                                      check=True).stdout.decode("utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"🔴 取不到基準 rev {base!r} 之 app.py：{e} ⇒ 無從判定")
            return 3
    red = []
    print("── 接線（AST·app.py）──")
    for name, ok, note in _wiring_checks(src, base_src):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run ──
def _lin(g):
    t, st = 0.0, [g]
    while st:
        x = st.pop()
        if x is None or x.is_empty:
            continue
        if x.geom_type in ("LineString", "LinearRing"):
            t += x.length
        elif hasattr(x, "geoms"):
            st.extend(x.geoms)
    return t


def _conn_ext(pa, pb, tol):
    """外部錨（⛔ 呼叫 k6_shares_segment）：精確共邊之線長 ≥ 0.01，或（tol 非 None 且）二片相距 ≤ tol 而
    二向容差共線長之小者 ≥ 0.01。"""
    if pa is None or pb is None:
        return False
    if _lin(pa.boundary.intersection(pb.boundary)) >= MINLEN:
        return True
    if tol is None or pa.distance(pb) > tol:
        return False
    return min(_lin(pa.boundary.intersection(pb.boundary.buffer(tol))),
               _lin(pb.boundary.intersection(pa.boundary.buffer(tol)))) >= MINLEN


def _new_pairs(temp):
    """精確共線長 < 0.01 而（相距 ≤ TOL 且）二向容差共線長之小者 ≥ 0.01 之對；並回諸對之頂點至他片界線之距之最大者
    （唯計距 ≤ TOL 之頂點）。對之元 ＝ (暫編地號, 原地號, 街廓)。"""
    from shapely.geometry import Polygon, Point
    ps = []
    for t in temp:
        cs = t.get("polygon_coords") or []
        if len(cs) >= 3:
            ps.append(((str(t["暫編地號"]), str(t.get("原地號", "")), str(t.get("所屬街廓", ""))), Polygon(cs)))
    ps.sort(key=lambda x: x[0][0])
    out, mx = [], 0.0
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            (ka, A), (kb, B) = ps[i], ps[j]
            if A.distance(B) > TOL or _lin(A.boundary.intersection(B.boundary)) >= MINLEN:
                continue
            if min(_lin(A.boundary.intersection(B.boundary.buffer(TOL))),
                   _lin(B.boundary.intersection(A.boundary.buffer(TOL)))) < MINLEN:
                continue
            out.append((ka, kb))
            for X, Y in ((A, B), (B, A)):
                for v in X.exterior.coords:
                    d = Y.boundary.distance(Point(v))
                    if d <= TOL:
                        mx = max(mx, d)
    return out, mx


def _groups_ext(temp, own, tol):
    from shapely.geometry import Polygon
    by = {}
    for t in temp:
        g = str(own.get(str(t.get("原地號", "")), "") or "")
        cs = t.get("polygon_coords") or []
        if g:
            by.setdefault(g, []).append((str(t["暫編地號"]), Polygon(cs) if len(cs) >= 3 else None))
    out = {}
    for g, lst in by.items():
        adj = {p: set() for p, _ in lst}
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if _conn_ext(lst[i][1], lst[j][1], tol):
                    adj[lst[i][0]].add(lst[j][0])
                    adj[lst[j][0]].add(lst[i][0])
        seen, comps = set(), []
        for s in sorted(adj):
            if s in seen:
                continue
            comp, stk = [], [s]
            seen.add(s)
            while stk:
                u = stk.pop()
                comp.append(u)
                for v in sorted(adj[u] - seen):
                    seen.add(v)
                    stk.append(v)
            comps.append(sorted(comp))
        out[g] = sorted(comps)
    return out


def _groups_code(ns, temp, own):
    from shapely.geometry import Polygon
    pk = [{"原地號": t.get("原地號", ""),
           "polygon": Polygon(t["polygon_coords"]) if len(t.get("polygon_coords") or []) >= 3 else None}
          for t in temp]
    out = {}
    for g in ns["k6_merge_groups"](pk, own):
        gid = str(own.get(str(temp[g[0]].get("原地號", "")), ""))
        out.setdefault(gid, []).append(sorted(str(temp[i]["暫編地號"]) for i in g))
    return {k: sorted(v) for k, v in out.items()}


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        miss = [n for n in FUNCS + CONSTS if n not in ns]
        if [n for n in miss if n in FUNCS]:
            print(f"  🔴 受詞缺：{miss}")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        if miss:
            print(f"  🔴 受詞缺（常數）：{miss}——續跑本案之量")
            red.append("受詞缺")
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        done_groups = False
        for sb in sbs:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            print(f"══ 退縮 {sb} ══")
            if not done_groups:
                done_groups = True
                pairs, mx = _new_pairs(temp_p)
                n_same = sum(1 for a, b in pairs if own.get(a[1]) and own.get(a[1]) == own.get(b[1]))
                ok0 = (len(pairs), n_same) == NEW_PAIRS and mx < TOL / 5
                print(("  ✅" if ok0 else "  🔴") + f" R0 新判為相連之對 {len(pairs)}（同歸戶 {n_same}）＝ 期 {NEW_PAIRS}；"
                      f"頂點至他片界線之距之最大者 {mx:.3e} m（< {TOL / 5:.0e}）")
                for a, b in pairs:
                    print(f"     {a[0]}〔{a[2]}·{own.get(a[1], '—')}〕–{b[0]}〔{b[2]}·{own.get(b[1], '—')}〕")
                if not ok0:
                    red.append("R0")
                code = _groups_code(ns, temp_p, own)
                ext_t = _groups_ext(temp_p, own, TOL)
                ext_e = _groups_ext(temp_p, own, None)
                d1 = sorted(g for g in set(code) | set(ext_t) if code.get(g) != ext_t.get(g))
                print(("  ✅" if not d1 else "  🔴") + f" R1 合併群（{len(temp_p)} 片·{len(code)} 歸戶）＝ 外部錨：相異 {d1}")
                if d1:
                    red.append("R1")
                chg = sorted(g for g in set(ext_t) | set(ext_e) if ext_t.get(g) != ext_e.get(g))
                ok2 = chg == sorted(GROUPS_TOL) and all(code.get(g) == GROUPS_TOL[g] for g in GROUPS_TOL)
                print(("  ✅" if ok2 else "  🔴") + f" R2 與精確之判相異之歸戶 {chg}；其群 ＝ GROUPS_TOL："
                      f"{all(code.get(g) == GROUPS_TOL[g] for g in GROUPS_TOL)}")
                if not ok2:
                    red.append("R2")
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
                    log = list(fake_st.session_state.get("f3_k6b_stage3_log") or [])
                    ns["K917_DROPPED"].clear()
                    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                                    eff_min_build_by_blk={})
            except RuntimeError as e:
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            n_exp = 19 if abs(sb - 3.5) < 1e-9 else (0 if abs(sb) < 1e-9 else None)
            rows = []
            ok3 = n_exp is None or len(log) == n_exp
            if abs(sb - 3.5) < 1e-9:
                for cand, lvl, recvs, qty in S3_ROWS_35:
                    r = next((x for x in log if x.get("候選") == cand and x.get("序") == "後處理"), None)
                    got = None if r is None else (r.get("層級"), sorted(r["受併宗"]) if isinstance(r.get("受併宗"), list)
                                                  else [r.get("受併宗")], r.get("結果"),
                                                  {k: round(float(v), 2) for k, v in (r.get("併入量") or {}).items()})
                    exp = (lvl, recvs, "成", {k: round(v, 2) for k, v in qty.items()})
                    rows.append((cand, got == exp, got))
                    ok3 = ok3 and got == exp
            print(("  ✅" if ok3 else "  🔴") + f" R3 段三之紀錄 {len(log)} 列（期 {n_exp}）"
                  + "".join(f"；{c} {'✅' if o else '🔴 ' + repr(g)}" for c, o, g in rows))
            if not ok3:
                red.append(f"R3@{sb}")
            if abs(sb - 3.5) < 1e-9:
                gg = {str(r.get("暫編地號")): float(r.get("G(㎡)") or 0) for r in sg["g_rows"]
                      if r.get("推進側別") in ("left", "right")}
                pools = {}
                for r in sg["g_rows"]:
                    if r.get("推進側別") == "抵費地" and r.get("cut_coords") and not isinstance(r.get("cut_coords"), str):
                        from shapely.geometry import Polygon
                        pools[r.get("所屬街廓")] = pools.get(r.get("所屬街廓"), 0.0) + Polygon(r["cut_coords"]).buffer(0).area
                okg = all(abs(gg.get(k, -1) - v) <= 0.01 for k, v in G_35.items())
                okp = all(abs(pools.get(k, -1) - v) <= 0.01 for k, v in POOL_35.items())
                print(("  ✅" if okg and okp else "  🔴") + " R4 配地：" +
                      "、".join(f"{k} G {gg.get(k, float('nan')):.2f}（期 {v:.2f}）" for k, v in G_35.items()) + "；抵費地 " +
                      "、".join(f"{k} {pools.get(k, float('nan')):.2f}（期 {v:.2f}）" for k, v in POOL_35.items()))
                if not (okg and okp):
                    red.append("R4")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("selftest", "wiring", "run"):
        print(__doc__)
        return 2
    repo = os.path.abspath(argv[2])
    if argv[1] == "selftest":
        return selftest(repo)
    if argv[1] == "wiring":
        return wiring(repo, argv[3] if len(argv) > 3 else None)
    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
    return run(repo, sbs)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `F16p`（`git apply` 之差異·`verify/probes/probe_WG9357_k948.py`）

````diff
--- a/verify/probes/probe_WG9357_k948.py
+++ b/verify/probes/probe_WG9357_k948.py
@@ -508,8 +508,11 @@
         ('後處理', 'R2', '—', '628-30(2)', '後處理(a)', '成', '628-45(2)', (('628-45(2)', 150.3),)),
         ('後處理', 'RD2', '—', '628-45(5)', '後處理(b)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 105.0325), ('628-45(2)', 101.1875))),
         ('後處理', 'RD2', '—', '628-30(4)', '後處理(b)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 48.7553), ('628-45(2)', 51.6647))),
-        ('後處理', 'G1', '—', '628-45(3)', '後處理(c)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 136.545), ('628-45(2)', 136.545))),
-        ('後處理', 'RD4', '—', '628-45(4)', '後處理(c)', '成', ('628-45(1)', '628-45(2)'), (('628-45(1)', 112.3), ('628-45(2)', 112.3))),
+        # 🔧 `W-G.9-361`（`K-9-54`·KL 裁 `2026-09-30`）：地籍相連之判之座標容差 ⇒ 地主甲之合併群含 `R6` 之 `628-20(1)`
+        #   ⇒ `628-20(3)` 新增、`628-45(3)`／`628-45(4)` 三街廓平分（原二列：R3／R5 各 136.545／112.3）
+        ('後處理', 'RD3', '—', '628-20(3)', '後處理(b)', '成', '628-20(1)', (('628-20(1)', 42.15),)),
+        ('後處理', 'G1', '—', '628-45(3)', '後處理(c)', '成', ('628-20(1)', '628-45(1)', '628-45(2)'), (('628-20(1)', 91.03), ('628-45(1)', 91.03), ('628-45(2)', 91.03))),
+        ('後處理', 'RD4', '—', '628-45(4)', '後處理(c)', '成', ('628-20(1)', '628-45(1)', '628-45(2)'), (('628-20(1)', 74.8667), ('628-45(1)', 74.8667), ('628-45(2)', 74.8667))),
     ],
     0.0: [],
 }
````

## 附錄乙之二　塊 `F12p`（`git apply` 之差異·`verify/probes/probe_WG9353_endmerge.py`）

````diff
--- a/verify/probes/probe_WG9353_endmerge.py
+++ b/verify/probes/probe_WG9353_endmerge.py
@@ -24,6 +24,9 @@
            `_end_region_R`／`solve_G_binary`）。
            🔧 `W-G.9-354`：甲之停機點由「他街廓已配地而本段無受併宗」移至後處理 (a)（他街廓依原位次配得者照配·
            `K-9-48` 其二·讀法 `1` ⑤；餘片不鄰任一配得之街廓·`K-9-48` 七項 3／5／6 之承前缺口）。
+           🔧 `W-G.9-361`（`K-9-54`·地籍相連之判之座標容差）：甲之停機之因改為餘片鄰二配得之街廓（`['R4', 'R6']`·
+           目標街廓非恰一）；乙之注入加鎖 `628-22(3)`、`628-23(3)`（`G017` 之 `RD2` 道路片·其受併宗於 `R5` 非恰一），
+           故乙 ≠ 丙之前段（丙之鎖同本批前）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, io, os, re, sys
@@ -511,7 +514,9 @@
 
 SCEN = {
     "甲": dict(excl=["628-4(1)"], lock=[], mw=None),
-    "乙": dict(excl=["628-4(1)"], lock=["628-1(3)"], mw=None),
+    # 🔧 `W-G.9-361`（`K-9-54`）：地籍相連之判之座標容差 ⇒ `G017` 之合併群含 `R5` 之三宗與 `RD2` 之二道路片；其道路片之
+    #   受併宗於 `R5` 非恰一（段三後處理之「承受之宗未定」）⇒ 乙之注入加鎖此二道路片，以存本例之受詞（① 同街廓合併之當選）
+    "乙": dict(excl=["628-4(1)"], lock=["628-1(3)", "628-22(3)", "628-23(3)"], mw=None),
     "丙": dict(excl=["628-4(1)"], lock=["628-1(3)", "628-21(1)", "628-22(1)"], mw=None),
     "丁": dict(excl=[], lock=[], mw=13.0),
 }
@@ -669,10 +674,12 @@
                 continue
             if scen == "甲":
                 e = P["err"]
+                # 🔧 `W-G.9-361`（`K-9-54`）：`628(3)`（`R5`）與 `R4` 之 `628(1)`、`R6` 之 `628(2)` 隔分配線相鄰 ⇒ 所鄰之 B 內
+                #   街廓由 `[]` 改為 `['R4', 'R6']`（目標街廓非恰一·`K-9-51` 射程 ③）；仍停機
                 ok = (e is not None and e[0] == "段三／合併再試" and "後處理 (a)" in e[1]
-                      and "所鄰之 B 內街廓 ＝ []" in e[1] and "停機款 9" in e[1])
+                      and "所鄰之 B 內街廓 ＝ ['R4', 'R6']" in e[1] and "停機款 9" in e[1])
                 print(("  ✅" if ok else "  🔴") + " X1 甲：地主 G009 以道路併入成，其合併群之他街廓依原位次配得者照配"
-                      f"（`W-G.9-354`·`K-9-48` 其二·讀法 `1` ⑤）；餘片不鄰任一配得之街廓 ⇒ 後處理 (a) 停機（{e}）")
+                      f"（`W-G.9-354`·`K-9-48` 其二·讀法 `1` ⑤）；餘片鄰二配得之街廓 ⇒ 後處理 (a) 停機（{e}）")
                 if not ok:
                     red.append("X1@甲")
                 continue
````

## 附錄乙之三　塊 `F13p`（`git apply` 之差異·`verify/probes/probe_WG9354_endcontest.py`）

````diff
--- a/verify/probes/probe_WG9354_endcontest.py
+++ b/verify/probes/probe_WG9354_endcontest.py
@@ -24,7 +24,8 @@
   run      <repo> [<退縮> …]
            harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 無標的 ⇒ 紀錄⛔ 載競合。另於退縮 `3.5` 實跑三合成案（注入於
            harness 之 `ns`·⛔ 改檔）——`R3` 左端與 `R5` 右端（隔 `RD2` 相對）以所給之寬構末端帶（⛔ 未臨正街）：
-           甲 ＝ 寬 `8`／`16`（地主 `G009` 之 `628(4)`／`628(3)` 競合·皆不成 ⇒ `R5` 右端由 `628-23(2)` 續試而成）；
+           甲 ＝ 寬 `8`／`16`（地主 `G009` 之 `628(4)`／`628(3)` 競合·皆不成 ⇒ `R5` 右端由 `628-23(2)` 續試而成；
+           🔧 `W-G.9-361`：`G017` 之 `R6` 三片上鎖〔`K-9-54` 後其合併群跨 `R5`／`R6`〕）；
            乙 ＝ 寬 `8`／`5.5`，`628-23(2)` 假設跨占街角規定範圍、`G009` 他街廓之片上鎖（整片只 `R5` 成）；
            丙 ＝ 寬 `8`／`5.0`，同乙（切半只 `R5` 成，`628(4)` 連其半併入 `628(3)`）。外部錨 ＝ 本器另寫之末端帶、
            交面積、切半之比與 G 公式（⛔ 呼叫 `end_block_*`／`_end_band`／`_end_region_R`／`solve_G_binary`）。
@@ -582,7 +583,10 @@
 
 
 SCEN = {
-    "甲": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 16.0}, lock=[], excl=[]),
+    # 🔧 `W-G.9-361`（`K-9-54`）：地籍相連之判之座標容差 ⇒ `G017` 之合併群跨 `R5`／`R6`；其 `R6` 之片 `628-22(1)` 所鄰之
+    #   已配得之街廓非恰一（`R5`／`R6`·`K-9-51` 射程 ③ ⇒ 段三後處理停機）⇒ 甲之注入加鎖 `G017` 之 `R6` 三片，以存本例之受詞
+    #   （二末端塊之競合·`R5` 右端由 `628-23(2)` 續試而成）
+    "甲": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 16.0}, lock=["628-21(1)", "628-22(1)", "628-23(1)"], excl=[]),
     "乙": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 5.5},
               lock=["628(1)", "628(2)", "628(5)", "628-1(1)", "628-1(2)", "628-1(3)"], excl=["628-23(2)"]),
     "丙": dict(wid={("R3", "left"): 8.0, ("R5", "right"): 5.0},
````

## 附錄乙之四　塊 `F3p`（`git apply` 之差異·`verify/probes/probe_WG9344p1_pooltemp.py`）

````diff
--- a/verify/probes/probe_WG9344p1_pooltemp.py
+++ b/verify/probes/probe_WG9344p1_pooltemp.py
@@ -35,8 +35,11 @@
     "628-41(3)": ["628-41(1)"],
     "628-45(5)": ["628-45(1)", "628-45(2)"],
     "628-30(4)": ["628-45(1)", "628-45(2)"],
-    "628-45(3)": ["628-45(1)", "628-45(2)"],
-    "628-45(4)": ["628-45(1)", "628-45(2)"],
+    # 🔧 `W-G.9-361`（`K-9-54`·KL 裁 `2026-09-30`）：地籍相連之判之座標容差 ⇒ 地主甲之合併群含 `R6` 之 `628-20(1)`
+    #   ⇒ `628-45(3)`／`628-45(4)` 三街廓平分、`628-20(3)` 併入 `628-20(1)`（原二列之期：`628-45(1)`、`628-45(2)`）
+    "628-45(3)": ["628-20(1)", "628-45(1)", "628-45(2)"],
+    "628-45(4)": ["628-20(1)", "628-45(1)", "628-45(2)"],
+    "628-20(3)": ["628-20(1)"],
 }
 
 
````

## 附錄丙　塊 `K6`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-53`／`K-9-54` 之立（`W-G.9-361`·⛔ 上文一字不刪·純末端追加）

### 🔒 `K-9-53`　**地主已有配得土地者，其分不到之土地及道路、公設地上之土地，先依手冊（跨分配線併應分配面積較大之一側、道路依中心線併入兩側已配地之宗、公設地平分）併入其已配得之宗，併不進去的才與其他分不到之土地合併、沿名單調配**（KL 裁 `2026-09-30`·canonical·**逐字**）

**編號之由**（`W-G.9-361 §零-1`）：`K-9-53` 於開工態 `caede20` 之宣告框與鬆框皆 `0` ⇒ 取之；`K-9-44`／`K-9-47` 仍為缺號。
**出處**：發單側窗五十九（`2026-09-30`）；所呈附示意圖一張（`規格步4_前置之問_628-32示意.png`·`340541` B·⛔ 入倉）；轉錄自發單側交接文五十九 `§二`（`15950` B·`sha256` `40da8c944175210e6df199b2e89b08d35d4acab938e487f46c475f7051a86828`·該文⛔ 入倉）。

**發單側所呈之【要你判斷】（逐字·⛔ 增刪一字）**：

> 地主已有配得土地者，其分不到之土地及道路、公設地上之土地，是否先依手冊（跨分配線併應分配面積較大之一側、道路依中心線併入兩側已配地之宗、公設地平分）併入其已配得之宗，併不進去的才與其他分不到之土地合併、沿名單調配？（是／否）

🔒 同訊之【現況】【要改成】【對土地的影響】之逐字⛔ 存於倉內外可稽之檔（交接文五十九唯載其要旨）；其要旨（⛔ 充逐字）：二讀法——**甲** 先依手冊（跨分配線併應分配面積較大側〔規格步 `1`〕、道路依中心線併兩側已配地之宗、公設地平分·皆受「不影響原位次」之檢核），併不進去者始入合併單位沿名單調配；**乙**（`W-G.9-351` 之 `adj_intake` 之分類）凡有分不到之建地者，其道路、公設地上之土地一律入合併單位，全體沿五級名單併入第一個有其配地之街廓；字面相衝 ＝ `K-9-45`「連同」與 `K-9-46`「兼有者依五級」對裁定 K／手冊五則／`K-9-48` 其二其三／規格步 `1`。

**同訊之【通知】二則（要旨·KL 未駁）**：① 兩側皆無之道路片而其地主於他街廓有配地者 ⇒ 依裁定 K 視同無同歸戶、單獨進調配池；② 規格步 `1` 之「同一宗跨分配線併應分配面積較大側」（`GB-175` 解除所定）現行盤點未辦（`adj_intake` 列之為「建築街廓內不能分配」）⇒ 併入規格步 `4` 之單。

**KL 之答（`2026-09-30 18:40`·逐字）**：

> 是

**裁之內容**（KL「是」＝ 所呈【要你判斷】為「是」＝ 甲；【通知】二則 KL 未駁）：
① 地主已有配得土地（原位次配地·含段三所併）者，其分不到之土地（建築街廓內不能分配者）及其道路、公設地上之土地，**先依手冊**併入其已配得之宗：跨分配線者併向應分配面積較大之一側（規格步 `1`·`N0-9`·`GB-175`）；道路依中心線切半、併入兩側已配地之宗（一側無者往另一側·裁定 K·手冊 p.`192`–`193`）；公設地上之土地平分（`K-9-48` 其三·讀法 `5`）。每次併入皆受「不影響原位次」之檢核（`K-9-48` 其三）。
② 併不進去者，與該地主其他分不到之土地合併（`K-9-45`），沿五級名單調配（規格步 `4` 第一趟）。
③ 【通知】① ② 如上。

**射程**：及於**任一案件**。⛔ 及於：地主無任何配得土地者（其土地之去處依 `K-9-45`／`K-9-46`·公設軌依裁定 K）。

**與既有正典之關係**：`K-9-45`（一）之「連同」與 `K-9-46`（一）之「兼有者屬建地軌」——**以本裁定其先後**：手冊先行，併不進去者始成合併單位；`K-9-48` 其二其三與七項、`K-9-51`——其作法（手冊先行、不影響原位次之檢核、最大面積、剩餘土地之去處）自段三之射程推及地主已有配得土地之一切情形；規格步 `1`（跨分配線併大側）、步 `2`（合併單位之成立）、步 `4`（同歸戶合併·第一趟）——依本裁之序。

**本案之量**：候規格步 `4` 之單以程式實算（交接文五十九 `§一-3` 之推估係於地籍相連之精確之判下所得·其 `628(2)` 之歸屬與 `K-9-54` 後之地籍相連不符·`自誤 559`）。

**落地狀態**：⬜ **未實作**（規格步 `4` 之單）。

### 🔒 `K-9-54`　**地籍界線之座標相差在 `0.1 mm` 以內者，視為共用同一段界線（`K-6 §一` 之相連）；由此所生之段三後處理之變動（退縮 `3.5 m` 地主甲之公設地上之土地改由三街廓平分）KL 接受**（KL 裁 `2026-09-30`·canonical·**逐字**）

**編號之由**（`W-G.9-361 §零-1`）：`K-9-54` 於開工態 `caede20` 之宣告框與鬆框皆 `0` ⇒ 取之。
**出處**：發單側窗六十（`2026-09-30`）；呈文附示意圖一張（`界線相連之判_G007示意.png`·⛔ 入倉）。

**發單側所呈（逐字·⛔ 增刪一字）**：

> 【現況】
> 程式判斷同一地主的兩筆土地是否「相連」（K-6 §一：共用一段界線），是逐點比對圖檔座標。R4、R5、R6 三個街廓之間的分配線，以及公園 G1 與道路 RD3 之間，兩側的地籍界線在圖上是同一條線，但座標有千分之一公釐級的差距（最大 0.007 mm），程式因此判成「不相連」。例如 628-20(1)（R6）和 628-20(2)（R5）實際共用 12.53 m 的界線，程式卻判為不相連。R1、R2、R3 之間沒有這個情形。
>
> 【要改成】
> 兩筆界線座標相差在 0.1 mm 以內的，視為共用同一段界線（相連）。
>
> 【對土地的影響】（兩種退縮都已實跑，比對改前改後）
> - **退縮 0 m**：配地、街角、抵費地都不變。
> - **退縮 3.5 m**：地主甲（G007）的土地連成一群後，多納入 R6 的 628-20(1)。依 K-9-48 其三（同一合併群跨多個建築街廓時，公設地上的土地平分到各街廓），變動如下：
>
>   | 土地 | 現行 | 改後 |
>   |---|---|---|
>   | 公園地 628-45(3)（273.09 ㎡） | R3、R5 各 136.55 ㎡ | R3、R5、R6 各 91.03 ㎡ |
>   | 路口道路 628-45(4)（224.60 ㎡） | R3、R5 各 112.30 ㎡ | 三街廓各 74.87 ㎡ |
>   | 道路 628-20(3)（42.15 ㎡） | 留到後面再併入 | 現在就併入 R6 的 628-20(1)（去處相同） |
>   | 應分配面積 | R3 628-45(2) 950.91；R5 628-45(1) 572.05；R6 628-20(1) 336.56 | 902.52；525.28；461.06 |
>   | 抵費地 | R3 1,834.68；R5 1,694.57；R6 1,901.82 | 1,883.03；1,742.99；1,777.33 |
>
>   街角得標不變。R5 的 628-18(2)、628-7(2) 因為界線推移，各減 0.53、1.08 ㎡。
> - **對規格步 `4` 的影響**：
>   - G009 在 R5、R6 分不到的土地（628(3)、628-1(2)、628(2)），和 R4 的 628(1)、628-1(1) 是同一筆土地跨分配線。改了之後，可以依「併向應分配面積較大的一側」併入 R4。
>   - G022 的公園地 628-7(3)（1,568.71 ㎡）會和它在 R5、R6 的土地連成一群，可以在 R5、R6 平分。
>   - 不改的話，這些土地都找不到相連的已配地。
>
> 【要你判斷】
> 地籍界線座標相差在 0.1 mm 以內的視為相連，並接受上面列出的退縮 3.5 m 配地變動，是否？（是／否）

**KL 之答（`2026-09-30 20:34`·逐字）**：

> 是

🔧 **所呈之二處失準**（發單側窗六十自捕·⛔ 改上開逐字）：① 「最大 0.007 mm」——本案新判為相連之 `19` 對（段三之輸入之全部切片 `126` 片·二片相距 `≤ 1e-4 m` 而精確共線長 `< 0.01 m`、二向容差共線長之小者 `≥ 0.01 m`·量測器 `F21` 之 `R0`）之頂點至他片界線之距之最大者 ＝ `1.000e-05 m`（`628(2)`／`628(3)`）＝ **`0.010 mm`**；所呈之 `0.007` 係唯量四對所得（`自誤 560`）。二值皆遠小於 `0.1 mm`，裁之內容⛔ 受影響。② 「不改的話，這些土地都找不到相連的已配地」——`G022` 之公園地 `628-7(3)` 確然（現碼下為孤片）；**`G009` 之 `628(3)`、`628-1(2)`、`628(2)` 於現碼即經道路片（`628(6)`／`628-1(3)`）與 `R4` 之宗相連**，所缺者唯與 `R4` 之宗之直接相鄰（隔分配線）（`自誤 561`）。

**裁之內容**：
① `K-6 §一` 之「共用線段」：二片邊界之精確交集之線長達 `K6_SHARE_MIN_LEN`（`0.01 m`）者 ⇒ 相連（同現碼·其長⛔ 變）；未達者，以座標容差 `0.1 mm`（`1e-4 m`）重判：二片相距 `≤ 1e-4 m`，且二片之邊界各落於他片邊界 `1e-4 m` 以內之線長之小者 `≥ 0.01 m` ⇒ 相連（其長 ＝ 該小者）；否則 ⇒ 不相連（其長 ＝ 精確交集之線長·同現碼）。
② 退縮 `3.5 m`：段三後處理之地主甲（`G007`）之變動 KL 接受（上開之表）；退縮 `0 m` 之配地⛔ 變。

**射程**：及於**任一案件**、及於 `K-6 §一` 之相連之一切用途（合併群、入池閘之同街廓相鄰、段三之相鄰與街廓之鄰接、末端塊之合併再試、規格步 `4`）。
**與既有正典之關係**：`K-6 §一`（「兩端完全共點」）——**讀為座標容差 `0.1 mm` 以內之共點**（浮點之圖檔座標下「完全」不可判·`K6_SHARE_MIN_LEN` 之原註逐字「兩端完全共點於浮點下不可判」）；`K-9-25`（地籍與街廓邊界間之無地號縫隙⛔ 作密合）——**⛔ 牴觸**：`0.1 mm` 遠小於該裁之縫隙（平均寬 `0.0869 m`），⛔ 密合任何有面積之縫；`GB-178` 之進度（四）之「浮點級之縫」（共界長精確為 `0`、以 `1e-9 m` 緩衝量得 `47.6792 m`）——同一現象之先見（彼處為宗地界與池帶界）。
**讀法**（發單側·【工】·⛔ 充裁）：「二向之小者」使判準對稱（`k6_shares_segment(a, b)` 與 `(b, a)` 同判）；精確之判達門檻者其長⛔ 變（既有之自檢 `S-1`〜`S-7` 與段三紀錄之鄰接長⛔ 受影響）。

**落地狀態**：① ＝ `W-G.9-361` 工項二（側支 `verify/W-G.9-361-k954`·`app.py` 之 `k6_shares_segment`·harness 與畫面二路徑同受）；入主線 ⬜（另候 KL 放行）。
````

## 附錄丁　塊 `G5`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-195` 之立（`W-G.9-361`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ `caede209cb769fbea2986ffe712e835ff052549b`（本批開工態）。**取號**（`W-G.9-361 §零-1`）：`GB-195` 於開工態之宣告框 `0`；鬆框 `1` 列（`docs/orders/W-G.9-343_重量單.md:33`·其時「對照乙［必為零］」所列之未取號·⛔ 占用）⇒ 取之。

### `GB-195` 🆕　**地籍相連之判（`K-6 §一`）以二片邊界之精確交集為之：界線於圖上重合而座標有微米級之差者判為不相連 ⇒ 合併群斷裂（本案退縮 `3.5 m` 段三後處理之平分少一街廓）**

**受詞**：`app.py` 模組層 `k6_shares_segment`（字樣錨 `def k6_shares_segment`）——取二片邊界之交集之線性部分之總長，`≥ K6_SHARE_MIN_LEN`（`0.01 m`）⇒ 相連；其呼叫者 ＝ `k6_merge_groups`（合併群）、`k929_6_fixpoint`（入池閘之同街廓相鄰）、`k6b_stage3_run`（段三之相鄰與街廓之鄰接）、`end_block_merge_run`（經 `k6_merge_groups`）、`k6_step0_merge`（步驟 `0`·預設 `off`）。
**實測**（發單側窗六十·倉外·態 `caede20`·harness·段三之輸入之全部切片 `126` 片〔含殘料 `8`〕·器 ＝ 量測器 `F21`〔`verify/probes/probe_WG9361_k954.py run`〕之 `R0`〜`R2`）：精確共線長 `< 0.01 m` 而二片相距 `≤ 1e-4 m`、二向容差（`1e-4 m`）共線長之小者 `≥ 0.01 m` 者 **`19` 對**——同歸戶者 `15` 對：`R4`／`R5`／`R6` 之分配線兩側 `11` 對（`628(1)`–`628(3)` `47.95 m`、`628-1(1)`–`628-1(2)` `38.74`、`628(1)`–`628(2)` `8.97`、`628(2)`–`628(3)` `2.05`、`628-18(1)`–`628-18(2)` `12.51`、`628-20(1)`–`628-20(2)` `12.53`、`628-21(1)`–`628-21(2)` `18.82`、`628-22(1)`–`628-22(2)` `18.34`、`628-23(1)`–`628-23(2)` `12.86`、`628-7(1)`–`628-7(2)` `11.14`、`628-53(1)`–`628-53(2)` `0.97`），公園 `G1` 與道路 `RD3`／`RD4` 之間 `4` 對（`628-7(3)`–`628-7(4)` `69.71`、`628-5(1)`–`628-5(2)` `12.92`、`628-12(1)`–`628-12(2)` `3.34`、`628-12(1)`–`628-12(3)` `4.72`）；殘料相涉者 `4` 對（無歸戶·⛔ 入任何群）；諸對之頂點（距他片界線 `≤ 1e-4 m` 者）至他片界線之距之最大者 ＝ `1.000e-05 m`（`628(2)`／`628(3)`）。合併群因而相異之歸戶 ＝ `G005`／`G007`／`G012`／`G017`／`G022`（`G003`／`G009`／`G025` 經他片已連通）；同街廓同歸戶之相鄰⛔ 在其列（入池閘⛔ 變）。
**與配地之關係**：退縮 `3.5 m`：段三後處理之地主甲（`G007`）之合併群少 `R6` 之 `628-20(1)` ⇒ 公園地 `628-45(3)`、路口道路 `628-45(4)` 由 `R3`／`R5` 二街廓平分（應為三街廓）；道路 `628-20(3)` 未為段三所併，留為調配之輸入「待同歸戶併入」（規格步 `4`）。退縮 `0 m`⛔ 觸。規格步 `4`（⬜）之跨分配線之判與合併群之平分亦受之。
**與既有登記之界**：`GB-178` 之進度（四）（宗地界與池帶界之「浮點級之縫」·同一現象之先見·彼處⛔ 涉相連之判）；`K-9-25`（有面積之縫隙⛔ 密合·⛔ 牴觸）。
**失效條件**：`K-9-54`（KL 裁 `2026-09-30`）之碼側落地（`W-G.9-361` 工項二）入主線。
🔒 **排程**：`W-G.9-361`（側支）→ 次單（入主線）。
````

## 附錄戊　塊 `E8`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-361 §零-1`）：本批取 `558`〜`561`（`4` 號）。`558` 係 CC 於 `W-G.9-360R`（報告）所報、發單側窗五十九復驗時證實而候鑄者（交接文五十九 `§一-2`）；`559` 係發單側窗六十讀交接文五十九 `§一-3` 時所捕；`560`、`561` 係發單側窗六十自捕於其呈 KL 之文（`K-9-54` 之所呈·逐字見 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之 `K-9-54`）。

### 🩸 `自誤 558`　**`W-G.9-360` 塊 `P14`（入 `CLAUDE.md` 之末）序 `2` 載「四十二突變」；量測器 `F19` 實為四十一（`M1`〜`M41`）**

**形**：`CLAUDE.md` 之「待落地清單之更新：調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）入主線；候選街廓名單之突變之判別力（`W-G.9-360`）」節序 `2` 逐字「本部 `Z0`〜`Z2` ＋ 四十二突變（以 `F18` 之判式量之）」；同單他處「四十一」`4` 處（`docs/orders/W-G.9-360_輕量單.md`·子字串框）、`F19` 之 docstring「`41` 種突變」、`F19` 之突變之名 `M1`〜`M41`（相異 `41`）。
**後果之界**：零（登記之文；量測器與其期⛔ 受影響）。
**根因**：擬塊 `P14` 時以記憶寫數，未以同單之量（`F19` 之 `_muts` 之數）對之。
**後果之框**：🟢 零。攔點 ＝ CC（`W-G.9-360R`·常規二·⛔ 上呈）→ 發單側窗五十九證實。
**攔法**：`W-G.9-361` 塊 `P15` 之「前節之更正」（`CLAUDE.md` 末端追加·⛔ 追改該節一字）。通則：登記之文所載之數，一律取自同單之量測器之出艙或其源碼之計數。

---

### 🩸 `自誤 559`　**交接文五十九 `§一-3` 之「二讀法於本案之差」之甲，將 `G009` 之 `628(2)`（`R6`·`11.49 ㎡`）歸 `R1`（在 `254.17` 內）；其與 `628-1(2)` 同屬一入池閘之單元（應分配面積同為 `153.11`），且於實際之地籍與 `R4` 之 `628(1)` 隔分配線相鄰（共線 `8.97 m`）**

**形**：交接文五十九 `§一-3`（逐字）「`628`／`628-1`（`G009`·`a` 區段）甲 `826.56` → `R4`（`628(1)` `407.48`·`628-1(1)` `419.08`）、`254.17` → `R1` `628(5)`」——其拆算（發單側窗六十·`G009` 之諸片之原有面積唯此組合合其數）：`254.17` ＝ `170.99`（`628(6)` 之半）＋ `71.69`（`628(4)`）＋ `11.49`（`628(2)`）；`407.48` ＝ `170.80`（`628(6)` 之另半）＋ `236.68`（`628(3)`）；`419.08` ＝ `227.41`（`628-1(2)`）＋ `191.67`（`628-1(3)`）。調配之輸入（`F20` 原型·態 `caede20`）之 `G009` 之建築街廓內不能分配：`628(2)` 與 `628-1(2)` 之應分配面積皆 `153.11`（同一單元·`原街廓之據` 計一次）。
**後果之界**：`11.49 ㎡`（`a` 區段）之去處（`R1` 或 `R4`）於推估之數；KL 之裁（`K-9-53`·甲）⛔ 受影響（其判斷係就原則）。零入倉之生產碼。
**根因**：以程式之相連之判（精確交集·`GB-195`）為地籍之實，未核 `R4`／`R6` 之分配線兩側之共線；且拆一入池閘之單元之諸片於二去處（未以單元為不可拆分之建地·`K-9-48` 七項 `4`）。
**後果之框**：🟡 呈 KL 之推估之數一處失準（`11.49 ㎡`）。攔點 ＝ 發單側窗六十（讀交接文、實量地籍時）。
**攔法**：`K-9-53` 之「本案之量」改候規格步 `4` 之單以程式實算；`GB-195`／`K-9-54`。通則：凡以程式之判推估土地之去處者，須以實際地籍（坐標容差內之共線）核其相連，且以入池閘之單元為不可拆分之單位。

---

### 🩸 `自誤 560`　**發單側窗六十呈 KL（`K-9-54` 之所呈）之【現況】載界線座標之差「最大 0.007 mm」；本案新判為相連之 `19` 對之最大者為 `0.010 mm`**

**形**：所呈逐字「座標有千分之一公釐級的差距（最大 0.007 mm）」；實測（量測器 `F21` 之 `R0`·段三之輸入之全部切片 `126` 片·新判為相連之 `19` 對之頂點〔距他片界線 `≤ 1e-4 m` 者〕至他片界線之距）之最大者 ＝ `1.000e-05 m`（`628(2)`／`628(3)`）。所呈之 `0.007`（`6.94e-06 m`·`628(1)`／`628(3)`）係唯量四對（`628(1)`／`628(3)`、`628-7(1)`／`628-7(2)`、`628-7(3)`／`628-7(4)`、`628-20(1)`／`628-20(2)`）所得。
**後果之界**：零（二值皆遠小於所擬之容差 `0.1 mm`；KL 之裁⛔ 受影響）。
**根因**：以部分之量稱全體之極值（母體未窮舉·`P-1` 之族）。
**後果之框**：🟡 呈 KL 之數一處失準。攔點 ＝ 發單側窗六十（擬 `GB-195` 時窮舉）。
**攔法**：`K-9-54` 之 `🔧` 註；`F21` 之 `R0`。通則：凡言「最大」「全部」者，同句具名其母體與其量測器。

---

### 🩸 `自誤 561`　**發單側窗六十呈 KL（`K-9-54` 之所呈）之【對土地的影響】末句「不改的話，這些土地都找不到相連的已配地」；`G009` 之 `628(3)`、`628-1(2)`、`628(2)` 於現碼即經道路片與 `R4` 之宗相連**

**形**：現碼（精確交集）下：`628(3)`–`628(6)`（`RD2`）`7.81 m`、`628(6)`–`628(1)` `34.46 m`；`628-1(2)`–`628-1(3)`（`RD3`）`0.80 m`、`628-1(3)`–`628-1(1)` `4.91 m`；`628(2)`–`628-1(2)` `1.16 m` ⇒ 皆與 `R4` 之宗同一合併群（`F21` 之 `R2`：`G009` 之群⛔ 因 `K-9-54` 而變）。所缺者唯與 `R4` 之宗之**直接**相鄰（隔分配線·跨分配線併大側之判之受詞）。「找不到相連的已配地」唯於 `G022` 之公園地 `628-7(3)` 為真（現碼下為孤片）。
**後果之界**：零（KL 所裁之事〔容差與退縮 `3.5 m` 之變動〕⛔ 繫於此句）；規格步 `4` 之去處之推估須依跨分配線之判重述。
**根因**：將「直接相鄰（跨分配線）」與「相連（經同地主之片）」混為一語。
**後果之框**：🟡 呈 KL 之後果之述一處失準。攔點 ＝ 發單側窗六十（擬 `K-9-54` 之入典時）。
**攔法**：`K-9-54` 之 `🔧` 註。通則：呈 KL 之「不改之後果」須分列其所依之判（直接相鄰／經他片相連）。
````

## 附錄己　塊 `P15`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：地籍相連之判之座標容差（`K-9-54`·`GB-195`）入側支；`K-9-53`（規格步 `4` 之先後）之入典；前節之更正（`W-G.9-361`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-361-k954`（本批新立·起於主線 `caede209cb769fbea2986ffe712e835ff052549b`）；主線⛔ 動。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-54`（地籍界線之座標相差在 `0.1 mm` 以內者視為相連） | `k6_shares_segment`：精確交集之線長達門檻者同現碼；未達者以座標容差 `K6_SHARE_COORD_TOL`（`1e-4 m`）重判（二片相距 `≤` 容差且二向容差共線長之小者 `≥ 0.01 m`）；harness 與畫面二路徑同受 | 🔶（側支） | `docs/orders/W-G.9-361_規格單.md` |
| `2` | `GB-195`（精確交集之判使合併群斷裂） | 失效條件 ＝ 序 `1` 入主線 | 🔶（側支） | 同上 |
| `3` | `K-9-53`（地主已有配得土地者：手冊先行，併不進去者始入合併單位沿名單調配） | 入典；其碼（跨分配線併大側、道路五則、公設地平分、不影響原位次之檢核、最大面積、`K-9-51`、合併單位沿名單之第一趟；`adj_intake` 之分類隨之改；量測器 `F20`〔倉外原型〕之入倉） | ⬜ | 規格步 `4` |
| `4` | `自誤 558`〜`561` | 見自誤簿 | ✅ | 同序 `1` |
| `5` | 以程式字樣為錨之突變之判別力（規格單流程·復驗時補寫）＋ 入主線 ＋ 主 checkout 之同步 | — | ⬜（候 KL 放行） | 次單 |

🔒 **前節之更正**（⛔ 追改前節一字）：「待落地清單之更新：調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）入主線；候選街廓名單之突變之判別力（`W-G.9-360`）」節序 `2` 之「四十二突變」應為「**四十一突變**」（`M1`〜`M41`·`自誤 558`）。
🔒 **本案之量**（發單側窗六十·態 `caede20` ＋ 原型·harness·量測器 `F21`／`verify/probes/probe_WG9344_k6s3.py cmp`）：退縮 `0 m` 之配地⛔ 變；退縮 `3.5 m` 段三後處理之地主甲（`G007`）：公園地 `628-45(3)`（`273.09 ㎡`）與路口道路 `628-45(4)`（`224.60 ㎡`）由 `R3`／`R5` 二街廓平分改為 `R3`／`R5`／`R6` 三街廓平分（各 `91.03`／`74.87`），道路 `628-20(3)`（`42.15 ㎡`）併入 `R6` 之 `628-20(1)`；應分配面積 `628-45(2)` `950.91 → 902.52`、`628-45(1)` `572.05 → 525.28`、`628-20(1)` `336.56 → 461.06`；抵費地 `R3` `1834.68 → 1883.03`、`R5` `1694.57 → 1742.99`、`R6` `1901.82 → 1777.33`；街角得標⛔ 變。
🔒 **依賴序**：本批（側支）→ 次單（突變之判別力 ＋ 入主線·零生產碼）→ 規格步 `4`（`K-9-53`·本序 `3`）→ `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ `W-G.9-357` 節序 `7` ＋ `W-G.9-360` 節序 `5`）。
🔒 **本機介面**（入主線並同步後）：退縮 `3.5 m` 之「🧮 執行 G 值迭代計算」之成果，`R3`／`R5`／`R6` 三街廓依上開本案之量而變；退縮 `0 m`⛔ 變。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `6`（子字串框·含圖例與本列）·列 ＝ `4`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: c1bbdd904bbdbf5f319480b2f6977832e520ad99931f8e6aea41373b34c7a7d1
