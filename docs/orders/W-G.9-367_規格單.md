# `W-G.9-367`　規格單：規格步 `4` 乙——第一趟（`K-9-53` ②·`K-9-56`：合併單位之地主另有已配得之宗者，沿其候選街廓名單併入第一個有其已配得之宗之街廓；整體不過者逐片、可拆分）（新側支 `verify/W-G.9-367-adj4`）＋ 手冊先行之 `GB-201` 之防護 ＋ `K-9-56` 之立 ＋ `GB-199`／`GB-201` 之進度 ＋ 自誤 `578`／`579` ＋ 常設規則索引之一列 ＋ 待落地清單之更新

> **本單建議等級 ＝ `xhigh`**（生產碼 `2` 檔·`app.py` 之新名十一〔純函式七·畫面之入口一〕與 harness 之入口一·既有函式三之插入·規格與量測器皆全·有土地後果）。
> **發單** ＝ 發單側窗六十八·`2026-10-04`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-367-adj4`**，其起點 ＝ 主線之端 `d7a5ea4`）。
> **流程 ＝ 規格單**（常態·`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通之期滿與續行（`W-G.9-358`）」節 ③·附則甲〜丙施行·`§二`）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `F24`·CC ⛔ 改一字）、既有量測器之錨之更新（塊 `F9p`／`F10p`／`F14p`／`F23p`／`F4p`）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py`／`verify/selection_pipeline.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **重**（生產碼 `2` 檔：`app.py`、`verify/selection_pipeline.py`；🔴 **有土地後果**——二退縮之配地：歸戶 `G001` 之道路片 `628-3(1)`（`13.15 ㎡`·兩側皆無已配地）整筆併入其 `R3` 之 `628-34(2)`，其應分配面積 `250.24 → 257.91 ㎡`、`R3` 之抵費地減 `7.65`／`7.64 ㎡`、合併單位 `18 → 17`〔`§一` 項 `6`〕；其所據 ＝ `K-9-53` ②〔KL `2026-09-30`〕與 `K-9-56`〔KL `2026-10-04`〕；**入主線前另呈 KL**〔`§四-2`〕）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`（`W-G.9-366` 工項三）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-367-adj4`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F24`／`F9p`／`F10p`／`F14p`／`F23p`／`F4p`／`K10`／`G9`／`E11`／`P21`／`IX2` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-367_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。旗標 off 之量一律由量測器於其行程內自設（`F24 offsnap`／`run`·`F23 offsnap`／`run`·塊 `F14p` 所改之器）；殼⛔ 設之。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py`、`verify/selection_pipeline.py` 以外之生產碼一字（生產碼 `34` 檔之其餘 `32` 檔）；`§三-3` 之禁改；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4 之任何錨；`verify/case_params_UC9898.json`；`verify/case_front_road_names_UC9898.json`；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿、恆常附款登記表、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md` 除塊 `K10`／`G9`／`E11`／`P21` 之純末端追加外之一字；常設規則索引除塊 `IX2` 所改之一列外之一字；既有量測器除塊 `F9p`／`F10p`／`F14p`／`F23p`／`F4p` 所改之外之一字；任何既有側支之推送、刪除或改寫；KL 主 checkout。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`；`git ls-remote --heads origin` 之列數 ＝ `35`，且⛔ 含 `refs/heads/verify/W-G.9-367-adj4`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 577 566` ⇒ `rc 0`（其「項4′ 四簿·正典框」＝ 自誤 `562`／`577`、`GB` `194`／`201`、`VR` `80`／`95`、`K-9` `52`／`55`／`[44, 47]`）。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態 `d7a5ea4` 之 `docs/` 全檔 **`968`** 檔（器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗六十八實跑 `python verify/probes/wg9268_gate6_occupancy.py d7a5ea4 W-G.9-367 W-G.9-366 W-G.9-396`（`rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-367`（本單之號） | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`W-G.9-366` | `2`／`4`／`3` | `2`／`4`／`3` | `7` | `2` | `2`／`25` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `20`／`31` | 🟢 宣告框 `0`、鬆框非零（器之標籤「甲（須 ≥1）」依本表之角色讀之·同 `W-G.9-365R` ⑥ 自解 `1`） |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `31`／`34` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-358_輕量單.md` `§零-1` 所載之具名豁免·受詢之判⛔ 受影響 |

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `d7a5ea4` 之追蹤檔 **`2787`** 檔·列框；發單側窗六十八以 `git grep -c -P "(?<![0-9\-])<號>(?![0-9])" d7a5ea4` 實算）：

| 號 | 錨定框之列 | 判 |
|---|---|---|
| `K-9-56` | `2` | 🟢 可取——二列 ＝ `docs/orders/W-G.9-342_輕量單.md:30`（「對照乙［必為零］`W-G.9-396`／`自誤 596`／`GB-196`／`K-9-56`」）與 `docs/orders/W-G.9-361_補令一.md:32`（引前者之鬆框）·其時之未取號·⛔ 占用 |
| `自誤 578` | `0`（C 形 `` `自誤 578` `` 含於其中） | 🟢 可取 |
| `自誤 579` | `0`（同上） | 🟢 可取 |
| 對照甲［必非零］`K-9-55` | `202` | 🟢 框非恆空 |
| 對照甲［必非零］`自誤 577` | `4` | 🟢 框非恆空 |

`K-9` `MAX` ＝ `55`、自誤 `MAX` ＝ `577`（`§零-0` 項 `3` 之器）⇒ 本批取 `K-9-56`（塊 `K10`）、`自誤 578`／`579`（塊 `E11`）；⛔ 鑄 `GB`／`VR`。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `d7a5ea4`，或遠端 heads ≠ `35`，或遠端已有 `verify/W-G.9-367-adj4`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `F24`／`F9p`／`F10p`／`F14p`／`F23p`／`F4p`／`K10`／`G9`／`E11`／`P21`／`IX2` 任一之 bytes／`sha256` 與 `§五-1` 不符；或寫出後之 blob ≠ `§五-1` 項 `14`；或塊 `F9p`／`F10p`／`F14p`／`F23p`／`F4p`／`IX2` 任一之 `git apply --check` 不過 |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-8` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有 `§一` 項 `6` 所列以外之任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-367-adj4`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之四檔（`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md`）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴；或常設規則索引之增刪 ≠ `1`／`1`；或工項三之 `checkidx` 之必紅／必綠不如期 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer（附則丙）之發現涉域上判斷或規格之漏載 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `16`。

---

## `§一`　態錨（發單側窗六十八自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`·`numpy 2.4.6`〔`GB-198`〕）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`；側支 `verify/W-G.9-363-k953` ＝ `cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce`、`verify/W-G.9-361-k954` ＝ `924d91634b1b36ea1d5fbbffd4a6791693ad3311`、`verify/W-G.9-359-cand` ＝ `bd072eb8924d7139d1c1bb6e39129f8b8be93f8b`、`verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`35`**（`verify/` `30`·`wip/` `3`·`claude/` `1`·`main` `1`）；`verify/W-G.9-367-adj4` ⛔ 存 |
| `2` | 生產碼、量測器與五檔（開工態 blob） | `app.py` `176f90c96f6c13ede5c0c4e2425bebbbe827bf51`（`1689501` B）；`verify/selection_pipeline.py` `c5e9fb05e222a6d43a1aa115494b0034435a0cd8`（`52125` B）；`verify/run_verification.py` `f5b896e5a702c5d958e3ba27091d27832385efc4`；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；（塊所改之五器）`verify/probes/probe_WG9345_screen.py` `e3c4b84b0b23170477f856b7ae0b18be8704bce1`；`verify/probes/probe_WG9350_frontroad.py` `4b11230f96d200f3eab304c31ae5600472e6c125`；`verify/probes/probe_WG9351_intake.py` `d0ab343ad60f4a80b04ca97d002ee759124fe07c`；`verify/probes/probe_WG9355_screenmerge.py` `a78216399a6a5c708cff4d0b9f8bf14fa462f841`；`verify/probes/probe_WG9363_k953.py` `de0a7e0629e81db3bee6d22918e169ba29cddd39`；`K-6` 典 `478272` B；`GB` 簿 `1042324` B；自誤簿 `1119307` B；`CLAUDE.md` `339034` B；常設規則索引 `dacddda92826e066813c3379fa305710adfa81bd`（`25053` B）（皆以換行結尾·CR `0`）；追蹤檔 `2787`、`verify/probes/` `397` 檔 |
| `3` | 開場之查（發單側窗六十八） | `W-G.9-366` 之落地：主線之四 `commit`（`2ce8af2`／`04a8187`／`902cd11`／`d7a5ea4`）、三檔之 blob（`verify/tools/wg9366_session_sync.py` `b30f983f…`、常設規則索引 `dacddda9…`、`CLAUDE.md` `f8e4eff0…`）＝ 該單 `§五-1` 項 `8`——自倉現查相符；`W-G.9-363` 之碼（`aab15b1`）入主線後（`W-G.9-364`），主線之 `app.py`／`verify/selection_pipeline.py` 至 `d7a5ea4` ⛔ 再變 |
| `4` | 本批之受詞 | `K-9-53` ②（KL `2026-09-30`）與 `K-9-56`（KL `2026-10-04`·本批之立）；`app.py` 之新名十一（`I-1`〜`I-8`）與 `k953_manual_run`（`GB-201` 之防護）、`f3_screen_k6b_stage3`（`I-10`）；`verify/selection_pipeline.py` 之 `run_adj4`（`I-9`）與 `run_corner_pk_k6b`（`I-10`）；`GB-199`／`GB-201`（本批之進度） |
| `5` | 現碼之行為（開工態） | 規格步 `4` 乙未落地：手冊先行之後即配地；調配之輸入（`adj_intake`）之合併單位二退縮皆 `18`（建地軌 `9`·公設軌 `9`）。其中地主另有已配得之宗者（`同歸戶原位次配地之街廓` 非空）唯 **`G001`**（公設軌·原有面積合計 `13.15 ㎡`·其片唯道路片 `628-3(1)`〔兩側皆無已配地·手冊先行⛔ 併·`段三餘量` `13.15`〕；`G001` 之已配得之宗 ＝ `R2` 之 `628-34(1)`、`R3` 之 `628-34(2)`）；餘 `17` 單位之地主皆無已配得之宗（其調配 ＝ 規格步 `5`·另單）。手冊先行之紀錄 `34`／`43` 列（`W-G.9-364` 之態） |
| `6` | 本案之土地後果（原型·harness·旗標 on） | **二退縮皆**：段三之紀錄、末端塊之合併再試、手冊先行之紀錄、街角得標與強制旗標⛔ 變（`F24 run` 之 `R2`：街角第 `1` 宗 ＝ 旗標 off 之實跑）。第一趟之紀錄（`f3_adj4_log`）恰 `1` 列：`序` `整體`·`歸戶` `G001`·`軌` `公設軌`·`街廓` `R3`·`片` `1 片`·`受併宗` `628-34(2)`·`併入量` `{628-34(2): 13.15}`·`結果` `成`（名單之首個有其已配得之宗之街廓 ＝ `R3`·「不影響原位次」之檢核通過）。配地：`R3` 之 `628-34(2)` `250.24 → 257.91`（左·`+7.67`）；他宗之應分配面積之變唯二分法之收斂之差（`≤ 0.01`）：`628-32(3)` `500.43 → 500.44`（二退縮）、`628-31(3)` `464.95 → 464.94`（`3.5 m`）；**`3.5 m`** ⇒ ΣΔG `+7.67`（Σ\|ΔG\| `7.69`）；抵費地 `R3` `1659.06 → 1651.41`（ΣΔ `−7.65`）、六街廓之和 `7233.47 → 7225.82`；**`0 m`** ⇒ ΣΔG `+7.68`（Σ\|ΔG\| `7.68`）；`R3` `1659.05 → 1651.41`（`−7.64`）、和 `7233.48 → 7225.84`；他街廓之抵費地⛔ 變。調配之輸入（二退縮同）：原位次配地 `73` 片 `26311.71 ㎡ → 74` 片 `26324.86 ㎡`；共同負擔用地·入合併單位 `32` 片 `7116.89 ㎡ → 31` 片 `7103.74 ㎡`；建築街廓內不能分配 `13` 片 `1432.13 ㎡`、無地號之殘料 `8` 片 `0`（⛔ 變）；合併單位 `18 → 17`（去者 ＝ `G001`）。`628-3(1)` 之鍵：`段三餘量` `13.15` → `段三併出` `['628-34(2)']`（去 `段三餘量`）。**由塊 `F24` 之 `run` 之 `R1`〜`R5` 逐列證之**；畫面與 harness 同（`parity`·`V-5`） |
| `7` | 量測器於工項一之端（`d7a5ea4` ＋ 塊 `F24`／`F9p`／`F10p`／`F14p`／`F23p`／`F4p`·發單側實跑） | `F24 selftest` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`F24 wiring … d7a5ea4` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['W1', 'W2', 'W3', 'W6']；rc 1`（`W4`／`W5`／`W7` 皆 ✅·`W7` 之錨 `648`／`185`、恰一之函式名 `446`／`20`）；`F24 run` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`F24 offsnap`、`F23 offsnap` ⇒ `rc 0`。前置 `3` 之諸器皆 **`rc 0`**：`parity` `3.5`／`0.0`（配地列 `35`／`34`、`36`／`35`·不符格 `0`·`Z` ＝ `[('harness', 'R1-抵費地-2')]`·「手冊先行 session 鍵 f3_k953_log」✅（`34`／`43` 列）·「第一趟 session 鍵 f3_adj4_log（0 列）」✅·末列逐字 `⇒ rc 0（不符 0 項）`）；`failclosed run … 3.5`、`F9 wiring`／`run`、`F10 wiring`／`run`、`F14 selftest`／`run`、`F23 selftest`／`wiring … 7d8e954`／`run`、`F21 run`、`F16 run`（末列逐字 `⇒ 紅 []；rc 0`）；`F3 run … 3.5 on`（末列逐字 `⇒ rc 0`）；前置 `4` 之四器皆 `rc 0` |
| `8` | 發單側之原型（**⛔ 交付**·僅為量測器之必過之實例） | 發單側於倉外拋棄式工作樹依 `§三` 撰一原型（`app.py` ＋ `verify/selection_pipeline.py`·⛔ 入倉·其 blob ⛔ 為本單之期），於其上 ＋ 塊 `F24`／`F9p`／`F10p`／`F14p`／`F23p`／`F4p`：`F24` 三子命令皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`（`selftest` `K1`〜`K22`〔含 `K4b`〕皆 ✅·`P0` `23／23`；`wiring` `W1`〜`W7` 皆 ✅·`W5` 之相異 ＝ `app.py` `['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'f3_screen_adj4', 'f3_screen_k6b_stage3', 'k953_manual_run']`、`verify/selection_pipeline.py` `['run_adj4', 'run_corner_pk_k6b']`·`W6` 之增段 `3`／`1`／`2`（`k953_manual_run`／`f3_screen_k6b_stage3`／`run_corner_pk_k6b`）·`W7` 之錨 `648`／`185`、恰一之函式名 `446`／`20`；`run` 二退縮之 `R1`〜`R5` 皆 ✅）；二 `offcmp`（工項一之端之 `offsnap` 對原型之 `offsnap`）⇒ `rc 0`（二退縮逐項 ✅）；前置 `3` 之諸器（`V-2`）皆 `rc 0`；`k6s3 cmp` 與 `F8 run` 之 `diff` ＝ `V-4`；`parity` ＝ `V-5`；`run_all` ＝ 項 `9`；`§四-3` 閘 `1`〜`29` 皆 ＝ 其期（`§五-1` 項 `17`）。🔒 **原型之初版之教訓**（⛔ 為期·CC 撰碼之鑑）：① 畫面之正面路寬初取 `f3_sb_rows` ⇒ 畫面之試算之組裝（`F4`／`F6` 之 `_screen_inputs`）無之 ⇒ `F6 failclosed` 之 `C0` 停機（「正面路寬缺」）——改取 `pk_kwargs['_corner_rows_init']`（同試算之摘要·harness 之 `param_rows` 之對應·`R-18`）；② 初版⛔ 先篩 ⇒ `F6` 之 `C3`（歸戶表空·段三未執行）之試算中止而停機——立 `adj4_possible`（`R-2`）；③ 受詞與名單之求初置於二入口 ⇒ 抽為 `adj4_plan`（純函式·共用），其讀正面道路與調配之輸入 ⇒ `F9`／`F10` 之 `W4` 之許另含之（塊 `F9p`／`F10p`）；④ 初版於 harness 直讀 session 之 `f3_alloc_depth_by_label`、並含 `'kept'`／`' 不在 temp_parcels'`／`'   else:'`／`'_ctx'`／`'first'`／`'x = '` 之字樣 ⇒ `F23 wiring` 之 `W8` 之錨命中逾 `1`（`X-3`）——改以 `adj4_depth_of` 一處讀之、改措辭；⑤ `F14` 之樁世界（G 值列無推進側別）⛔ 合調配之輸入 ⇒ 其 `_rigged` 內 `WV_ADJ4=off`（塊 `F14p`）；`F23 run` 量手冊先行之果 ⇒ 行程內 `WV_ADJ4=off`（塊 `F23p`）；`F4 parity` 之「session 之回復」以 `f3_adj4_log` 為新鍵 ⇒ 增其與 harness 逐列同之驗（塊 `F4p`）。**CC 之碼⛔ 須同原型**；唯須滿足 `§三` 與 `§四` |
| `9` | `run_all` | `python verify/run_all.py`（倉外拋棄式 worktree·殼無 `WV_`）於工項一之端：項 `64`·PASS `28`／FAIL `36`（末列 `W-V run_all: FAIL`·開工態之常態）；末端夾具／golden 列 `21／21`；對帳段 名目 凍存／現況 `22／36`。原型之 `run_all`（同一形之另一拋棄式 worktree）對之（`python verify/probes/probe_WG9343_step0_flag.py runall`·`rc 0`）：項 `64／64`·PASS `28 → 28`·FAIL `36 → 36`；**相異項恰 `6`**：`#14 v3·G值0m`（`FAIL → FAIL`·違規數 `311 → 315`）、`#15 v3·滑池槽0m`（`64 → 63`）、`#24 v3·G值3.5m`（`320 → 323`）、`#25 v3·滑池槽3.5m`（`79 → 78`）、`#41`／`#44 W-D.4 四梯清單0m／3.5m（v3 半實算）`（`171 → 171`·本體異）——皆配地之變之所生（`R3` 之池帶·`§一` 項 `6`）；`k* 六塊經驗錨` 與「結構不變量永久閘」二退縮仍 `PASS`（⛔ 在相異之列）；其餘 `58` 項之名目、狀態、違規數與本體逐項同；golden `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之 `<`／`>` 列 `82`（皆 `R3` 之池帶與其下游之列·其 bytes 平台相依·⛔ 入判） |

---

## `§二`　KL 之語與射程

🔒 **所據之裁**：
- **`K-9-53` ②**（KL `2026-09-30 18:40`·逐字「是」·`K-6` 典「`K-9-53`／`K-9-54` 之立」節）：手冊先行（①）併不進去者，與該地主其他分不到之土地合併（`K-9-45`），沿五級名單調配（規格步 `4` 第一趟）。① 已落地（`W-G.9-363`／`364`）；**本單 ＝ ② 之第一趟**（規格步 `4` 乙）。
- **`K-9-56`**（KL `2026-10-04`·本批之立·塊 `K10`）——發單側窗六十八所呈二問與【通知】三則，KL 之答（逐字·⛔ 增刪一字）：

> 1. 問1：甲 2. 問2：甲，一起併，改10/3裁的意思，兩側都沒有已配地的道路片，可以併到該地主在別的街廓已配到的土地(可拆分，以因應調配池需合格的機制)

  二問之要旨（發單側之呈文之逐字⛔ 存於倉內外可稽之檔·`自誤 579`·⛔ 充逐字）：**問1**——合併單位之土地整體併入名單上第一個有其已配得之宗之街廓之宗，「不影響原位次」之檢核不過（例：剩下之調配池不合格）時，**甲** 拆分（逐片：建地整筆、道路與公設地上之土地取最大面積；剩下者續沿名單）／**乙** ⛔ 拆分（整體改試名單之下一街廓）。**問2**——同一合併單位中之道路片，**甲** 與該單位之他片一起併入同一受併宗／**乙** 另依手冊之道路之則。同訊之【通知】三則（要旨·KL 未駁）：① 受併宗 ＝ 該街廓中其已配得之宗之一，依「同原地號 → 距錨點近 → 應分配面積大 → 暫編地號」之序（KL `2026-07-11` 之四層瀑布之推及）；② 每次併入皆受「不影響原位次」之檢核（`K-9-48` 其三）；③ 非位於受併宗之街廓之土地先折算 `a′` 再計 `G`（`K-9-45`（二））。
  **KL 之答之讀法**（⛔ 充裁）：問1 ＝ 甲（可拆分）；問2 ＝ 甲（一起併）；「改10/3裁的意思」＝ `K-9-55` 同訊之【通知】一（KL `2026-10-03 04:46` 答「OK」）所定之「兩側都沒有已配地之道路片⛔ 併到該地主在別的街廓已配到的土地」**改為「可以併」**——其片於手冊先行仍⛔ 併（手冊之道路之則無其側），而於第一趟隨其合併單位沿名單併入該地主於他街廓之已配得之宗，**可拆分**（「以因應調配池需合格的機制」＝ 問1 之甲）。
- `K-9-45`（合併單位·`G(a1＋a2′＋…)`·可拆分）；`K-9-46`（兼有者屬建地軌·原街廓）；`K-9-52`（候選街廓名單·規格步 `3`）；`K-9-48` 其三（不影響原位次之檢核）與七項 `3`（最大面積）；`v3` §8（位相不變）；`K-9-49`（街角選位之時點）。

🔒 **工程讀法**（【工】·⛔ 充裁·入典為 `K-6` 典之註〔塊 `K10`〕·其要旨以【通知】呈 KL）：
- **甲 受詞**：調配之輸入（`adj_intake`·以第一趟之前之試算求之）之合併單位中，`同歸戶原位次配地之街廓` 非空者（地主另有已配得之宗）；其片 ＝ 該單位之「建築街廓內不能分配」與「共同負擔用地」（道路、公設地上之土地）。道路片、公設片帶 `段三餘量` 者，其可併之量 ＝ 其餘量；否則全量。地主無任何已配得之宗者⛔ 在本單之射程（規格步 `5`）。
- **乙 名單**：規格步 `3` 之候選街廓名單（`K-9-52`·建地軌依五級八鍵、公設軌依距離）；以第一趟之前之試算**求一次**（⛔ 隨併入而重算）。唯公設軌之受詞者⛔ 須正面道路之名（其缺以佔位代之）。
- **丙 受詞之序**：建地軌先 → 原有面積合計大者先 → 歸戶。
- **丁 街廓之取**：沿名單，**至第一個有其已配得之宗（當下之試算）之街廓**；無者略過。
- **戊 受併宗**：該街廓中其已配得之宗之一，依（同原地號 ? `0` : `1`, 錨點〔名單之錨點〕至該宗之成員之原形之聯集之質心之距〔`0.01 m`〕, −應分配面積, 暫編地號）之最小者（【通知】①）。
- **己 整體**：全部之片（剩下 `> 0` 者）之可併之量各折算 `a′`（【通知】③）後一次併入受併宗；建地片自可建築宗地（build）去之；檢核（【通知】②·`T` ＝ 該街廓 ∪ 建地片之所屬街廓、`R` ＝ 建地片）過 ⇒ 成、該受詞止。
- **庚 逐片**（問1 甲）：整體不過 ⇒ 於同一受併宗逐片（建地 → 道路 → 公設地，同類剩下大者先）：建地片整筆（`T` ＝ 該街廓 ∪ 其所屬街廓、`R` ＝ 該片）；道路片、公設片取最大面積（`0.01 ㎡` 之來源面積之格·`T` ＝ 該街廓、`R` ＝ ∅·視為單調而二分）；其後剩下者續沿名單之下一個有其已配得之宗之街廓（其處再自整體始）。
- **辛 都不行**：名單盡而有剩下 ⇒ 留於合併單位（規格步 `5`）；記「剩下」一列。
- **壬 幾何之來源**（`GB-199`）：錨點與受併宗之成員之形 ＝ **重劃前之切片之原形**（段三之前之宗地）——⛔ 讀段三後之宗地之形（入池閘之單元帶佔位成員之形）。
- **癸 三鍵**：沿用段三之三鍵（`段三併出`／`段三部分併出`／`段三餘量`）；既有之鍵與第一趟之併入合之；下游（調配之輸入、公設地調配之 temp、步驟 M）一字不改。
- **子 街角定案**：第一趟之試算與其後之配地，皆沿用末端塊合併再試之後之街角選位之結果（⛔ 重跑·同手冊先行）。
- **丑 停機**：建地片於當下之試算已為已配得之宗或其成員（「分不到」之前提不立）；現態或前態之配地中止；受詞之片之原形缺、或非 temp 之片、或為殘料；名單缺或重複；面積或折算無從定之。⛔ 以靜默略過代之。
- **寅 旗標**：`WV_ADJ4`（未設／`on` ⇒ 啟用；`off` ⇒ 逐位回到本批前之行為，唯 session 多一鍵 `f3_adj4_log` ＝ `[]`）；手冊先行之旗標 `WV_K953` 或入池閘之旗標 `WV_K929_6` 為 `off` ⇒ 第一趟亦不辦（第一趟立於手冊先行之上）；三旗標皆判（非法之值 ⇒ 停機）。先篩：無「為 build 之某宗之歸戶、且 temp 中其片 `≥ 2`」之歸戶 ⇒ ⛔ 試算、逕回（受詞之必要條件）。
- **卯 `GB-201` 之防護**（手冊先行·`k953_manual_run`）：計畫之受併宗於當下之試算未保留 ⇒ 停機（逐片之整筆之主併入、與可拆分之片之最大面積之試之前）；⛔ 改手冊先行之他一字。

🔒 **流程之令**：規格單流程之常態（KL `2026-09-29 20:20`·`docs/orders/W-G.9-358_輕量單.md` `§二`）；附則甲〜丙（恆常附款登記表「`n③` 之試行期變通之期滿與續行」節 ③ 之 `2`）：甲 本單⛔ 令任何片「維持原狀」（本批之土地後果全由 `K-9-53` ②／`K-9-56` 之施所生，`§一` 項 `6` 已逐宗列之）；乙 同一量之判、寫、讀出自同一式（`R-9`／`R-10` 之併入量與 `R-14` 之紀錄之 `併入量` 取同一 `a′` 之比；`R-12` 之檢核同手冊先行之 `χ`）；丙 CC 之唯讀獨立 reviewer 列為工項二之常設步（驗後、推前·停機款 `12`）。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 逐字放行**。
🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至新側支 `verify/W-G.9-367-adj4`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及 `app.py`／`verify/selection_pipeline.py` 以外之生產碼、`§三-3` 之禁改、任何他錨；`(d)` ⛔ 及規格步 `5`（地主無已配得之宗之合併單位之調配·末端塊與中間調配池之進入與落位）與其後；`(e)` `K-9-55` 之理之推及（同街廓、⛔ 相鄰而未碰他街廓之分不到之建地）與 `W-G.9-363` 補令四全掃 ⑦（隔道路之建地片依道路片之計畫先併往另一側，而道路片其後未全併者）——本案皆無其形；其於第一趟之去處由名單之序與檢核定之（`§二` 丁〜庚），⛔ 另立停機款。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **受詞之總述**：規格步 `4` 乙之第一趟（`K-9-53` ②·`K-9-56`）——手冊先行之後（街角已定案），凡合併單位之地主另有已配得之宗者，沿其候選街廓名單，至第一個有其已配得之宗之街廓，將合併單位之土地（`a′` 折算）**整體**併入其已配得之宗之一；整體不過 ⇒ 於同一宗**逐片**（建地整筆、道路與公設地上之土地取最大面積），剩下者續沿名單；都不行者留於合併單位。以一純函式 `adj4_pass1_run`（`app.py`）為**單一真相源**，其受詞與名單由純函式 `adj4_plan` 求之；harness（`run_adj4`）與畫面（`f3_screen_adj4`）皆呼二者；併入之結果以**段三之三鍵**標於宗地。另於手冊先行（`k953_manual_run`）增 `GB-201` 之防護。旗標 `WV_ADJ4`。

**用語**（本節專用）：「**片**」＝ `temp_parcels` 之元素；`a(x)` ＝ `分攤登記面積_m2` ＋ `面積_m2`；「**歸戶**」`g(x)` ＝ `own_map[str(原地號)]`（缺或空 ⇒ 空字串）；「**片之類**」：`街廓分類` ＝ `道路` ⇒ **道路**；`F3_CATEGORY_BURDEN[街廓分類]` ＝ `共同負擔`（且非道路）⇒ **公設地**；＝ `可建築土地` ⇒ **建地**；餘 ⇒ 停機。「**原形**」`O(p)` ＝ `Polygon(slice_geom[p]).buffer(0)`（`slice_geom[p]` 缺或頂點 `< 3` ⇒ 停機）。「**試算**」`S(temp, build)` ＝ 注入之 `alloc_state(temp, build)` 之回傳 `{kept: {街廓: 宗之集}, bad_pools: {街廓: int}, err: str|None, G: {宗: float}, members: {宗: [成員]}, units: {…}}`（同手冊先行之 `R-14`）；同一態之物件只試算一次。「**已配得之宗**」＝ 當下之試算之 `kept` 之宗；宗 `h` 之成員 `M(h)` ＝ `members.get(h) or [h]`。`q(v)` ＝ `float(adj_q2(v))`。`a′(x→r)` ＝ 注入之 `a_prime(x, r)`（`K-9-29 三`）；**折算之比** `κ(x→r)` ＝ `a′(x→r) ÷ a(x)`（以輸入之 temp 中之 `x` 與當下之態之 `r` 為引數）。

### `§三-1`　行為要求（逐條·「給定何種情形、須得何種結果」）

| # | 給定 | 須得 |
|---|---|---|
| `R-1` | 旗標 | module 層 **`ADJ4_ENV = "WV_ADJ4"`**（全檔恰一處賦值）與 **`adj4_enabled()`**：環境變數未設、或去空白後為空、或（不分大小寫）`on` ⇒ `True`；`off` ⇒ `False`；他值 ⇒ `RuntimeError`（訊息含 `ADJ4_ENV` 之值〔`WV_ADJ4`〕與環境變數之值·⛔ 靜默退回）。另 module 層 **`ADJ4_IDENT_UNUSED`**（全檔恰一處賦值之非空字串·公設軌之名單之正面道路之佔位） |
| `R-2` | **`adj4_possible(temp_parcels, build_parcels, own_map)`**、**`adj4_subject_units(intake)`**（純函式） | 前者（先篩·⛔ 試算）：`own_map or {}` 下，「歸戶非空、為 `build_parcels` 之某片之歸戶、且 `temp_parcels` 中（`_is_ghost_sliver` 除外）其片 `≥ 2`」之歸戶存在 ⇒ `True`；否則 `False`（受詞之地主須有已配得之宗與其他一片·皆在 temp ⇒ 其必要條件）。後者回 `intake['units']` 中 `同歸戶原位次配地之街廓` 非空者（原序）；`intake` 為 `None` 或無 `units` ⇒ `[]` |
| `R-3` | **`adj4_subjects(intake, cand_lists)`**（純函式） | 回 `list` of `{'歸戶', '軌', '錨點', '名單', '片', '原有面積合計'}`：逐 `adj4_subject_units(intake)` 之單位 `u`，其名單 ＝ `cand_lists` 中 `歸戶` 同者之 `名單` 之 `街廓`（依序·`str`）、`錨點` ＝ 其 `錨點`（`str`）；`片` ＝ `u['建築街廓內不能分配']` 繼以 `u['共同負擔用地']` 之 `暫編地號`（`str`·相異·原序）；`原有面積合計` ＝ `float(u['原有面積合計'])`（`adj_intake` 之單位恆有之；原型以 `or 0` 取之·二者於其輸出等價）。序 ＝ `(軌 ＝ ADJ_TRACK_BUILD ? 0 : 1, −原有面積合計, 歸戶)`。停機：`cand_lists` 中同一歸戶二見（訊息含該歸戶與「名單重複」）；受詞之單位之歸戶無名單（訊息含該歸戶與「無候選街廓名單」） |
| `R-4` | **`adj4_depth_of(session)`**、**`adj4_trial_state(summary, err, build_used)`**（純函式·畫面與 harness 共用） | 前者回 `dict((session or {}).get('f3_alloc_depth_by_label', {}) or {})`（新 `dict`）；後者回 `dict(summary, err=err, members=…, units=…)`，其 `members`／`units` ＝ `k953_units_of(build_used)` |
| `R-5` | **`adj4_plan(intake, temp_parcels, g_rows, classified_blocks, eff_min_build_by, front_derive_by, front_name_by, width_by, depth_by)`**（純函式） | `adj4_subject_units(intake)` 空 ⇒ 回 `[]`、**⛔ 呼叫他函式**（他引數得為 `None`）。否則：可建築街廓 ＝ `classified_blocks` 中 `F3_CATEGORY_BURDEN[category]` ＝ `ADJ_BURDEN_BUILD` 者之 `label`（原序）；正面道路 ＝ `r3_front_road_identifier(可建築街廓, front_derive_by or {}, front_name_by or {})` 之 `id`——受詞之單位⛔ 含建地軌者，其 `id` 為 `None` 之街廓以 `ADJ4_IDENT_UNUSED` 代之；街廓屬性 ＝ `adj_block_ctx(可建築街廓, {label: category}, eff_min_build_by or {}, {label: 正面道路}, {label: width_by.get(label)}, depth_by or {})`；名單 ＝ `adj_candidate_lists(dict(intake, units=受詞之單位), 街廓屬性, adj_pool_anchor(g_rows), {暫編地號: polygon_coords 之 temp_parcels})`；回 `adj4_subjects(intake, 名單)`。所呼之函式之停機照拋（例：建地軌而正面道路無識別符 ⇒ `adj_block_ctx` 之停機） |
| `R-6` | **`adj4_pass1_run(temp_parcels, build_parcels, own_map, subjects, slice_geom, a_prime, alloc_state, *, log_print=print)`** 之入口 | 回 `(temp_out, build_out, log)`。① `build_parcels` 之元素須皆為 `temp_parcels` 中同 `暫編地號` 者 ⇒ 否則停機（訊息含「非 temp_parcels 之片」·**先於** ②）；② `subjects` 空 ⇒ 回 `(temp_parcels, build_parcels, [])`（**同一物件**）且**⛔ 呼叫 `alloc_state`**；③ 輸入⛔ 改寫（以深拷貝為之）；④ 對（拷貝之）輸入試算一次：`err` 非空 ⇒ 停機（訊息含「現態之配地中止」）；`G` 或 `members` 非 `dict` ⇒ 停機 |
| `R-7` | 受詞之片（逐 `subjects` 之元素·依其序） | 逐 `片` 之 `x`：非 `temp_parcels` 之片、或 `_is_ghost_sliver`、或類為建地而⛔ 在當下之 build ⇒ 停機；`a(x) ≤ 0` ⇒ 停機；`O(x)` 須可得（否則停機·訊息含 `x` 與「原形缺」）。**剩下** `L(x)` 之初值 ＝ 道路或公設地而帶 `段三餘量` ⇒ `float(段三餘量)`；否則 `a(x)`。`O(錨點)` 亦須可得 |
| `R-8` | 沿名單（逐 `名單` 之街廓 `b`·依序） | 諸片之 `L` 皆 `round(·, 4) ≤ 0` ⇒ 止。以當下之態試算 `S`（`err` 非空 ⇒ 停機）；建地片而 `L > 0` 者為 `S` 之任一已配得之宗之成員（`M(h)` 之聯集）⇒ 停機（訊息含該片與「分不到之前提不成立」）。**受併宗之候選** ＝ `S['kept'][b]` 之宗 `h` 而其為當下之 temp 之片、`g(h)` ＝ 該受詞之歸戶者；空 ⇒ 次街廓。候選之任一無 `S['G']` ⇒ 停機。**受併宗** `r` ＝ 依鍵 `(M(h) 中有片〔輸入之 temp 之片〕之原地號 ∈ 受詞之片之原地號之集 ? 0 : 1, q(O(錨點) 之質心至 ∪{O(m) : m ∈ M(h)} 之質心之距), −S['G'][h], h)` 之最小者 |
| `R-9` | 整體（每街廓 `b` 之首） | `live` ＝ `L > 0` 之片；於當下之態之拷貝：`r` 之 `面積_m2` 增 `Σ κ(x→r)·L(x)`（`x ∈ live`）；`live` 中之建地片自 build 去之；檢核 `χ(當下, 拷貝, T ＝ {b} ∪ {建地片之所屬街廓}, R ＝ live 中之建地片)`。過 ⇒ 採拷貝；`live` 之各片記併入 `r`（來源量 ＝ `L(x)`）、`L(x) ← 0`；該受詞**止**（⛔ 續名單）。不過 ⇒ ⛔ 採，進 `R-10` |
| `R-10` | 逐片（整體不過·同一 `b`、同一 `r`） | 依 `(類：建地 0／道路 1／公設地 2, −L(x), x)` 之序逐 `x ∈ live`：`κ ＝ κ(x→r)`（`≤ 0` ⇒ 停機）、`s ＝ L(x)`。**建地** ⇒ 整筆：拷貝之 `r` 之 `面積_m2` 增 `κ·s`、自 build 去 `x`；`χ(當下, 拷貝, {b, x 之所屬街廓}, {x})` 過 ⇒ 採、記併入（`s`）、`L(x) ← 0`；不過 ⇒ ⛔ 採。**道路、公設地** ⇒ 最大面積 `v` ＝ `{s} ∪ {n/100 : n 為非負整數、n/100 < s}` 中使「拷貝之 `r` 之 `面積_m2` 增 `κ·v`」之 `χ(當下, 拷貝, {b}, ∅)` 過之最大者（先試 `s`；不過 ⇒ 於 `n` 二分·視為單調）；`v > 0` ⇒ 採其態、記併入（`v`）、`L(x) ← s − v`。其後續名單之次街廓（`R-8`） |
| `R-11` | 名單盡 | 仍有 `L(x)` 之 `round(·, 4) > 0` 之片 ⇒ 記「剩下」一列（`R-14`）；其片留於合併單位（規格步 `5`） |
| `R-12` | 「不影響原位次」之檢核 `χ(前, 後, T, R)`（`K-9-48` 其三·同手冊先行之 `R-8`） | `S前` ＝ 試算（前）（`err` 非空、或 `G`／`members` 非 `dict` ⇒ 停機）；`S後` ＝ 試算（後）；`S後['err']` 非空 ⇒ **不過**（其由 ＝ `併入後配地中止：` ＋ 訊息之首 `120` 字·⛔ 停機）；逐 `t ∈ T`（字典序）：`(S前['kept'][t] − R) − S後['kept'][t]` 非空 ⇒ 不過（由 `{t} 原保留之宗 [...] 不保留`·`[...]` ＝ 其字典序之 `list` 之 `str`）；`S後['bad_pools'][t] > S前['bad_pools'][t]` ⇒ 不過（由 `{t} 配餘地不合格`）；諸由以 `；` 相接 |
| `R-13` | 輸出 | `temp_out`／`build_out` ＝ 末態（深拷貝·`build_out` 之元素與 `temp_out` 中同 `暫編地號` 者為同一物件）；受併宗之 `面積_m2` 已增其量；整筆併出之建地片已自 build 去之。**鍵**（沿用段三之三鍵）：本函式有正之併入之片 `x` ⇒ `段三併出` ＝ （既有之 `段三併出` ∪ 本函式之受併宗）之字典序 `list`；末之 `L(x)` 之 `round(·, 4) > 0` ⇒ `段三部分併出` ＝ 既有者與本函式所併之來源量（逐受併宗相加·`round(·, 4)`）之合（正者·字典序之鍵）、`段三餘量` ＝ `round(L(x), 4)`；否則去此二鍵。無正之併入之片⛔ 動其鍵 |
| `R-14` | 紀錄 `log`（`list` of `dict`） | 每列含鍵 `序`、`歸戶`、`軌`、`街廓`、`片`、`類`、`受併宗`、`併入量`、`結果`、`檢核`（未適用者 ＝ `—`；`併入量` 未適用者 ＝ `{}`）；得另有 `不過之由`、`餘量`。**整體列** ＝ `序` `整體`·`街廓` `b`·`片` `f"{len(live)} 片"`·`類` `—`·`受併宗` `r`·`併入量` ＝ 過 ⇒ `{r: round(Σ κ·L, 4)}`、否則 `{}`·`結果` `成`／`未成`·`檢核` `通過`／`不過`·不過 ⇒ `不過之由` ＝ `R-12` 之由。**逐片列** ＝ `序` `逐片`·`片` `x`·`類` `建地`／`道路`／`公設地`·`受併宗` `r`·`併入量` ＝ `{r: round(κ·所併之來源量, 4)}`（所併 `> 0`）或 `{}`·`結果` ＝ 建地 ⇒ `成`／`未成`；道路、公設地 ⇒ `成`（`round(s − v, 4)` 為 `0`）／`部分成`（`v > 0`）／`未成`·`檢核` ＝ `通過`／`部分通過`／`不過`（建地之不過另記 `不過之由`）。**剩下列** ＝ `序` `剩下`·`片` ＝ 剩下之片之字典序以 `、` 相接·`結果` `留於合併單位（規格步 5）`·`餘量` ＝ `{x: round(L(x), 4)}`。`歸戶`／`軌` ＝ 該受詞之值（三種列皆然） |
| `R-15` | 停機（`RuntimeError`·訊息首 `🔴 [K-9-53 ② 第一趟]`） | `R-3`／`R-6`／`R-7`／`R-8`／`R-10`／`R-12` 所列。**⛔ 以靜默略過代之** |
| `R-16` | 手冊先行之 `GB-201` 之防護（`k953_manual_run`·唯增列） | 逐片之**整筆之主併入**（`W-G.9-363` 補令四 `R-9⁗` ③ 之查之後）與**可拆分之片之最大面積之試**（來源量 `> 0` 時·含其 `K-9-51` 之可拆分者）之前：以當下之態試算（同一態只試算一次）——`err` 非空 ⇒ 停機；計畫之受併宗 `r` ⛔ 在其 `kept` 之任一街廓 ⇒ 停機（訊息含 `GB-201`、`r` 與該片）。訊息首 ＝ 手冊先行之既有首（`🔴 [K-9-53 手冊先行]`）。其餘一字不動 |
| `R-17` | harness（`verify/selection_pipeline.py`） | 新 **`run_adj4(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback, *, snapshot, callbacks, winners, forced, slices)`** ⇒ `(temp_out, build_out)`：**先**呼 `ns["adj4_enabled"]()`、`ns["k953_enabled"]()`、`ns["k929_6_enabled"]()`（三者皆呼·非法 ⇒ 上拋）；其一偽，或 `ns["adj4_possible"](temp_parcels, build_parcels, ss['t8_ownership_map'])` 偽 ⇒ `ss['f3_adj4_log'] ＝ []`、回輸入之同一物件（⛔ 試算、⛔ 讀 `cb` 等）。否則以**街角定案之試算**（深拷貝宗地；`ns["K917_DROPPED"].clear()`；`ss[ns["SS_END_BLOCK_MODE"]] ＝ 'trial'`；`run_step_g(…, build, winners, forced, setback, eff_min_build_by_blk={})`·**⛔ 呼叫 `run_corner_pk`**；`RuntimeError` ⇒ `err` ＝ 其首列之首 `300` 字；回 ＝ `ns["adj4_trial_state"](ns["k953_alloc_summary"](g_rows, {label: category}, {街廓: param_row}), err, 入池閘之末態 build〔無則試算之 build〕)`；另存其 `g_rows`、末態 build、temp 之拷貝、`err`、`K917_DROPPED` 之深拷貝、`ns["adj4_depth_of"](ss)`）：對輸入試算一次（`err` ⇒ 停機）⇒ `ns["adj_intake"](該 temp, 入池閘之末態 build〔⛔ 以試算之 build 代之〕, g_rows, 該 dropped, own_map, {label: 負擔屬性})` ⇒ `ns["adj4_subject_units"]` 非空者始呼 `ns["adj4_plan"](…, cb, {}, cad['front_road_derive'] or {}, run_verification.load_front_road_names(), {label: param_row 之 '正面路寬(m)'}, 該 depth)`（空 ⇒ 受詞 `[]`）⇒ `ns["adj4_pass1_run"](temp_parcels, build_parcels, own_map, 受詞, {暫編地號: polygon_coords 之 slices}, callbacks['a_prime'], 試算)`；`own_map` ＝ `ss['t8_ownership_map']`；隔離 ＝ 深拷貝 `session_state` 與 `ns["K917_DROPPED"]`、`finally` 原地回復；其後 `ss['f3_adj4_log']` ＝ 紀錄。**`run_corner_pk_k6b`**（唯增列）：`run_k953` 之呼叫之後恰一處 `temp3, build3 = run_adj4(…, temp3, build3, setback, snapshot=snapshot, callbacks=_cbk, winners=res[3], forced=res[4], slices=temp_parcels)`（`slices` ＝ 本函式之輸入 `temp_parcels`·重劃前之切片）；其回傳之末二值即之；其後⛔ 重跑街角選位 |
| `R-18` | 畫面（`app.py`） | 新 **`f3_screen_adj4(st, *, pk_kwargs, g_kwargs, slices)`** ⇒ `{'temp', 'build', 'log'}`：先去 `session_state['f3_adj4_log']`；呼 `adj4_enabled()`、`k953_enabled()`、`k929_6_enabled()`（三者皆呼）——非法 ⇒ 停機之路（下開）；其一偽，或 `adj4_possible(輸入之 temp, 輸入之 build, session_state['t8_ownership_map'])` 偽 ⇒ 其 ＝ `[]`、回輸入之同一物件（`pk_kwargs['temp_parcels']`／`['build_parcels']`）、⛔ 試算、**⛔ 呼叫 `st` 之任何方法**、⛔ 讀 `g_kwargs`。否則以**街角定案之試算**（同 `f3_screen_k953`：深拷貝宗地；`K917_DROPPED.clear()`；先去 `SS_ADJ_BUILD_FINAL`；代理 st `_K6BTrialSt`；`SS_END_BLOCK_MODE` ＝ `'trial'`；`f3_screen_stepg_run(代理, **dict(g_kwargs, _auto_recalc=False, _btn_clicked=True, build_parcels=…, _new_params=…))`·**⛔ 呼叫 `f3_screen_corner_pk_run`**；`_K6BTrialDone` ⇒ 略；`_K6BTrialStop`／`RuntimeError` ⇒ `err`；回 ＝ `adj4_trial_state(k953_alloc_summary(f3_G_values, …, {街廓: pk_kwargs['_corner_rows_init'] 之列}), err, SS_ADJ_BUILD_FINAL 之值〔無則試算之 build〕)`；另存 `f3_G_values`、`SS_ADJ_BUILD_FINAL`、temp 之拷貝、`err`、`K917_DROPPED` 之深拷貝、`adj4_depth_of(session_state)`）：對輸入試算一次（`err` ⇒ 停機）⇒ `adj_intake(…, session_state['t8_ownership_map'], {label: 負擔屬性})` ⇒ `adj4_plan(…, g_kwargs['classified_blocks'], session_state[K91_SS_MBA_EFFECTIVE], session_state[SS_FRONT_ROAD_DERIVE], {label: session_state[SS_FRONT_ROAD_NAME] 之以街廓 id 所存者}, {label: pk_kwargs['_corner_rows_init'] 之該街廓之列之 '正面路寬(m)'}（同試算之摘要之街角之列·⛔ 讀 `f3_sb_rows`）, 該 depth)` ⇒ `adj4_pass1_run(輸入, …, {暫編地號: polygon_coords 之 slices}, k6b_screen_callbacks(…)['a_prime'], 試算)`；隔離 ＝ 試算前存 `K6B_SCREEN_TRIAL_KEYS` 與 `K917_DROPPED`、`finally` 復之。**停機之路**：`RuntimeError` ⇒ `f3_k6b_stage3_error` ＝ `'（第一趟）'` ＋ 訊息之首列（`500` 字內）、`st.error` ＋ `st.stop()`、其後上拋；⛔ 寫 `f3_adj4_log`。其後 `session_state['f3_adj4_log']` ＝ 紀錄，並以 `st.expander`（`expanded=False`）示其表（`st.dataframe`；無列 ⇒ `st.caption`）。**`f3_screen_k6b_stage3`**（唯增列）之 `_end_merge` 內：`f3_screen_k953` 之後恰一處呼叫 `f3_screen_adj4(st, pk_kwargs=dict(pk_kwargs, temp_parcels=<手冊先行之出之 temp>, build_parcels=<其 build>), g_kwargs=g_kwargs, slices=temp0)`（`temp0` ＝ 既有之 `pk_kwargs['temp_parcels']`），其回之 `temp`／`build` 代手冊先行者；餘一字不動 |
| `R-19` | 旗標 off（`WV_ADJ4`、`WV_K953`、`WV_K929_6` 任一） | harness 與畫面之一切輸出**逐位同開工態**之同旗標之態；唯 session 多一鍵 `f3_adj4_log` ＝ `[]`（`V-3`） |
| `R-20` | 本案（harness·退縮 `3.5`／`0.0`·旗標 on） | 唯 `§一` 項 `6` 所列之改變（`V-1` 之 `F24 run`）；此外⛔ 任何改變 |

### `§三-2`　介面（名與簽名·量測器 `F24` 以之為受詞）

| # | 名 | 簽名／回傳 | 呼叫端 |
|---|---|---|---|
| `I-1` | 新 `ADJ4_ENV`（`"WV_ADJ4"`）、`ADJ4_IDENT_UNUSED`（非空字串）、`adj4_enabled` | `R-1`：`()` → `bool` | `run_adj4`、`f3_screen_adj4` |
| `I-2` | 新 `adj4_possible`、`adj4_subject_units` | `(temp_parcels, build_parcels, own_map)` → `bool`；`(intake)` → `list` | `run_adj4`（經 `ns`）、`f3_screen_adj4`；`adj4_subjects`、`adj4_plan`、`run_adj4` |
| `I-3` | 新 `adj4_subjects` | `(intake, cand_lists)` → `list` | `adj4_plan` |
| `I-4` | 新 `adj4_depth_of` | `(session)` → `dict` | `run_adj4`（經 `ns`）、`f3_screen_adj4` |
| `I-5` | 新 `adj4_trial_state` | `(summary, err, build_used)` → `dict` | 同上 |
| `I-6` | 新 `adj4_plan` | `(intake, temp_parcels, g_rows, classified_blocks, eff_min_build_by, front_derive_by, front_name_by, width_by, depth_by)` → `list` | 同上 |
| `I-7` | 新 `adj4_pass1_run` | `(temp_parcels, build_parcels, own_map, subjects, slice_geom, a_prime, alloc_state, *, log_print=print)` → `(list, list, list)` | 同上 |
| `I-8` | 新 `f3_screen_adj4` | `(st, *, pk_kwargs, g_kwargs, slices)` → `{'temp', 'build', 'log'}` | `f3_screen_k6b_stage3` 之 `_end_merge` |
| `I-9` | 新 `run_adj4`（`verify/selection_pipeline.py`） | `(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback, *, snapshot, callbacks, winners, forced, slices)` → `(list, list)` | `run_corner_pk_k6b` |
| `I-10` | 改（唯增列）`k953_manual_run`（`R-16`）、`f3_screen_k6b_stage3`（`R-18`）、`run_corner_pk_k6b`（`R-17`） | 簽名⛔ 變 | — |

🔒 本批之模組層新名**唯** `I-1`〜`I-9` 所列（其內之巢狀函式之名由 CC 定·受 `X-3`）。

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

| # | 禁 | 所護之閘 |
|---|---|---|
| `X-1` | `app.py` 之頂層節點對開工態相異者 ⊆ {`ADJ4_ENV`、`ADJ4_IDENT_UNUSED`、`adj4_enabled`、`adj4_possible`、`adj4_subject_units`、`adj4_subjects`、`adj4_depth_of`、`adj4_trial_state`、`adj4_plan`、`adj4_pass1_run`、`f3_screen_adj4`、`k953_manual_run`、`f3_screen_k6b_stage3`}；`verify/selection_pipeline.py` 者 ⊆ {`run_adj4`、`run_corner_pk_k6b`}（AST·⛔ 計註解與空列） | `F24 wiring` 之 `W5`；`F23 wiring` 之 `W7`（塊 `F23p`） |
| `X-2` | `k953_manual_run`、`f3_screen_k6b_stage3`、`run_corner_pk_k6b` 對開工態**唯增列**（⛔ 改、⛔ 刪既有一列·`difflib` 逐列） | `F24 wiring` 之 `W6`；`F23`／`F17`／`F21`／`F22` 之錨 |
| `X-3` | **既有量測器之錨**——`verify/probes/` 之既有之器（`F24` 除外）之字串常數（長 `≥ 4`）於開工態之 `app.py`（或 `verify/selection_pipeline.py`）恰一見者，於改後仍恰一見：新碼⛔ 複製之、⛔ 去之（發單側之原型初版所撞者例：`'kept'`、`' 不在 temp_parcels'`、`f3_alloc_depth_by_label`〔⇒ 以 `adj4_depth_of` 一處讀之〕、`'   else:'`、`'_ctx'`、`'first'`、`'x = '`）。另：開工態中**恰一處定義之函式名（含巢狀）**，改後仍恰一——新碼之巢狀函式⛔ 沿用手冊先行與段三等之名（例：`_sim953`、`_chk953`、`_dup953`、`_k951`、`_noaff`、`_apply`、`_clone`、`_row`） | `F24 wiring` 之 `W7`；`F23 wiring` 之 `W8`；諸器之突變之錨（命中須恰 `1`） |
| `X-4` | `_WF_NS_NAMES` 一字不動 | `wfns_ast` `48`／`48`／`47` |
| `X-5` | `verify/` 之一切檔一字不動，唯 `selection_pipeline.py`（`R-17`）、`probes/probe_WG9367_adj4.py`（工項一·新檔）之增與塊 `F9p`／`F10p`／`F14p`／`F23p`／`F4p` 所改之 `5` 檔（工項一） | `F8`〜`F23`、`main_synth`、`parity`、`run_all` |
| `X-6` | 新碼⛔ 含案件字面（街廓名、側別、地號、分區名之字串常數·`CASE_LIT_RE` 之形） | 泛化之鐵則；`F24 wiring` `W4` |
| `X-7` | 新碼⛔ 寫段三、末端塊合併再試、手冊先行、入池閘之 session 鍵以外之新鍵，唯 `f3_adj4_log`（`R-17`／`R-18`）；其讀唯另及 `R-18` 所列之既有鍵（`t8_ownership_map`、`K91_SS_MBA_EFFECTIVE`、`SS_FRONT_ROAD_DERIVE`、`SS_FRONT_ROAD_NAME`、`f3_alloc_depth_by_label`〔經 `adj4_depth_of`〕·唯讀）；`K6B_SCREEN_TRIAL_KEYS`、`K6B_SCREEN_STAGE3_KEYS`、`K6B_SCREEN_READBACK_KEYS` 一字不動 | `F4 parity` 之「session 之回復」 |
| `X-8` | 二回呼（harness `_k6b_callbacks`、畫面 `k6b_screen_callbacks`）、`adj_intake`、`adj_candidate_lists`、`adj_block_ctx`、`adj_pool_anchor`、`r3_front_road_identifier`、`k953_alloc_summary`、`k953_units_of`、`run_k953`、`f3_screen_k953`、`main` 一字不動（`X-1` 之推論·特記之） | `F10`／`F18`／`F23`／`main_synth` |

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`D-1`：本規格之任一條，其二讀法之後果**在土地上相異**（任一片之去處、任一宗之應分配面積、任一街廓之抵費地）。
`D-2`：某受詞之片、名單或受併宗無從依本規格定之。
`D-3`：須動 `§三-3` 之任一字始能滿足 `§三-1`。
`D-4`：本案之實跑（旗標 on）觸 `R-15`／`R-16` 之任一停機。
🔒 非域上之實作細節（巢狀函式之名與切分、區域名、註解、`RuntimeError` 之措辭〔`R-15`／`R-16` 所令之首段與 `R-3`／`R-6`／`R-7`／`R-8`／`R-16` 所令之字樣除外〕、`st.expander` 之標題句、拷貝之時機、試算之結果之快取〔「同一態只試算一次」須守〕）由 CC 定之，並於報告 ⑦ 逐項具名其選擇與其由。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐 `R-1`〜`R-20`：落於何函式、何處；`§三-4` 末之實作細節之選擇及其由；對 `§三-3` 各款之自查（逐款具名「未觸」及其據；`X-3` 附 `F24 wiring` 之 `W7` 之出艙）；附則乙之自查（折算之比〔`R-9`／`R-10` 之併入量與 `R-14` 之 `併入量`〕、檢核〔`R-12`〕之式各一）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/selection_pipeline.py` 之**全文**（報告同目錄之 `.diff` 檔·⛔ 摘要）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-367_規格單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-367 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-367-adj4`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`36`**、主線仍 ＝ `d7a5ea4…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-367-adj4`（快轉）。

**工項一　量測器入倉與既有量測器之錨之更新**（**先於生產碼**·新側支·零生產碼）：塊 `F24` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9367_adj4.py`（**新檔**）；塊 `F9p`／`F10p`／`F14p`／`F23p`／`F4p` 各抽為 `<O>\<塊名>.diff`、對拍後各 `git apply --check` ⇒ 過；各 `git apply`；`6` 檔之 `git hash-object` ＝ `§五-1` 項 `14`（停機款 `3`）。`commit` 訊息逐字 `W-G.9-367 工項一：量測器 F24（規格步 4 乙·第一趟）入倉 ＋ F4／F9／F10／F14／F23 之錨之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-367-adj4`。

**工項二　生產碼**（🔴 `app.py` ＋ `verify/selection_pipeline.py`·CC 依 `§三` 撰寫·一 `commit`·推新側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9367_adj4.py selftest <repo>`；`… wiring <repo> d7a5ea4`；`… run <repo>` ⇒ 皆 **`rc 1`**（末列逐字 ＝ `§一` 項 `7`）。
2. `python verify/probes/probe_WG9367_adj4.py offsnap <repo> <O>\a4off_pre.json`；`python verify/probes/probe_WG9363_k953.py offsnap <repo> <O>\k953off_pre.json`（皆 `rc 0`）。
3. `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_pre.json`；同 `0.0` ⇒ `<O>\parity00_pre.json`；`python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5`；`python verify/probes/probe_WG9350_frontroad.py wiring <repo>`；`… run <repo>`；`python verify/probes/probe_WG9351_intake.py wiring <repo>`；`… run <repo>`；`python verify/probes/probe_WG9355_screenmerge.py selftest <repo>`；`… run <repo>`；`python verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`… run <repo>`；`python verify/probes/probe_WG9361_k954.py run <repo>`；`python verify/probes/probe_WG9344p1_pooltemp.py run <repo> 3.5 on`；`python verify/probes/probe_WG9357_k948.py run <repo>` ⇒ 皆 **`rc 0`**（末列逐字 ＝ `§一` 項 `7`）。
4. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`（皆 `rc 0`）；`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫二檔之改動；`python -m py_compile app.py verify/selection_pipeline.py`；`commit` 訊息逐字 `W-G.9-367 工項二：規格步 4 乙之第一趟（K-9-53 ②·K-9-56）＋ 手冊先行之 GB-201 之防護 🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9367_adj4.py selftest <repo> > <O>\f24_self_post.log`；`… wiring <repo> d7a5ea4 > <O>\f24_wir_post.log`；`… run <repo> > <O>\f24_run_post.log` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `K1`〜`K22`（含 `K4b`）皆 ✅、`P0` `23／23`；`wiring` 之 `W1`〜`W7` 皆 ✅；`run` 之二退縮 `R1`〜`R5` 皆 ✅（`§一` 項 `6`） |
| `V-2` | 前置 `3` 之諸器（`parity` 除外·同命令·出艙存 `<O>\*_post.log`） | 皆 **`rc 0`**；末列逐字 ＝ 前置之同器（`F3` 之末列逐字 `⇒ rc 0`） |
| `V-3` | `python verify/probes/probe_WG9367_adj4.py offsnap <repo> <O>\a4off_post.json`；`python verify/probes/probe_WG9367_adj4.py offcmp <O>\a4off_pre.json <O>\a4off_post.json`；`python verify/probes/probe_WG9363_k953.py offsnap <repo> <O>\k953off_post.json`；`python verify/probes/probe_WG9363_k953.py offcmp <O>\k953off_pre.json <O>\k953off_post.json` | 皆 **`rc 0`**；二 `offcmp` 之二退縮逐項 ✅（旗標 off ⇒ 逐位同開工態·`R-19`）；`F24 offcmp` 之「第一趟之紀錄」之出艙 ＝ `<缺> → 0`（二退縮·`ℹ️` 列）；`F23 offcmp` 之「手冊先行之紀錄」＝ `0 → 0` |
| `V-4` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`python verify/probes/probe_WG9344_k6s3.py cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0`；`python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `4` 之一份 `diff` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 1`**：二退縮相異各恰 **`3`** 項——`R3` 之 `628-34(2)` 之 `a 面積` `429.35 → 442.5`、`G` `250.24 → 257.91`；`R3-抵費地` 之面積 `1659.06 → 1651.41`（`3.5`）／`1659.05 → 1651.41`（`0.0`）·容納內接矩形皆 `True`；末列逐字 `相異 3 項 ⇒ 🔴 異`（**街角得標、強制旗標、他街廓⛔ 在相異之列**）；`F8 run` 皆 `rc 0`（末列逐字 `⇒ 紅 []；rc 0`），其 `diff`：二退縮各恰 `2` 列（`<`／`>` 列·「逐街廓（配地宗數·ΣG）」之 `R3` `2547.73 → 2555.40`〔`3.5`〕／`2547.72 → 2555.40`〔`0.0`〕） |
| `V-5` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | 皆 **`rc 0`**；配地列 `3.5` ⇒ harness `35`／畫面 `34`、`0.0` ⇒ `36`／`35`，不符格 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]`；「手冊先行 session 鍵 f3_k953_log」✅（`34`／`43` 列）；「第一趟 session 鍵 f3_adj4_log」✅（`1`／`1` 列）；「段三後 build 之暫編地號依序」`45`／`46`；「session 之回復」✅；末列逐字 `⇒ rc 0（不符 0 項）` |
| `V-6` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`、FAIL `36 → 36`；**相異項恰 `6`**：`#14`（違規數 `311 → 315`）、`#15`（`64 → 63`）、`#24`（`320 → 323`）、`#25`（`79 → 78`）、`#41`／`#44`（`171 → 171`·本體異）——皆 `FAIL → FAIL`·配地之變之所生（`§一` 項 `9`）；`k* 六塊經驗錨` 與「結構不變量永久閘」二退縮仍 `PASS`；其餘 `58` 項逐項同；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py`）；二者之 blob 與增／刪之數出艙（發單側復驗時自倉重算）；`verify/` 之其餘一切檔對工項一之端相異 `0` |
| `V-8` | `§四-3` 閘 `8`〜`29` 之諸器（於工項二之 `commit`） | 皆 ＝ 其期 |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-8`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-367-adj4`。

**工項三　入典與登記**（新側支·零生產碼·一 `commit`）：
1. 塊 `K10` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `G9` 附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末；塊 `E11` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末（皆二進位·嚴格前綴·停機款 `8`）。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `13`，寫為 `<O>\checkidx.py`、`<O>\gen_fa_index.py`（⛔ 入倉）。
3. 塊 `IX2` 寫為 `<O>\IX2.diff`：`git apply --check <O>\IX2.diff` ⇒ 過；`git apply --numstat <O>\IX2.diff` ⇒ `1`／`1`；`git apply <O>\IX2.diff`。
4. **必紅**（判別力·塊 `P21` 未入前）：`python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md` ⇒ `rc 1`；不合恰一列 `` L116 命中列數=0: 'W-G.9-367`·' ``；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 1`。
5. 塊 `P21` 以二進位附於 `CLAUDE.md` 之末（停機款 `8`）。
6. **必綠**：同 `4` 之命令 ⇒ `rc 0`；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
7. `python <O>\gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>\FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（本批⛔ 動失敗考古·依 `CLAUDE.md`「指令檔之載入改制」節項 `3` 重跑）。
8. `commit` 訊息逐字 `W-G.9-367 工項三：K-9-56 之立 ＋ GB-199／GB-201 之進度 ＋ 自誤 578／579 ＋ 常設規則索引之一列 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-367-adj4`。

**工項四　執行報告入倉**（新側支·新檔 `docs/reports/W-G.9-367R_規格步4乙第一趟_執行報告.md`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F24` 三子命令之全文、二 `offcmp` 之全文、塊所改之器之 `run`／`wiring`／`selftest` 之全文（`V-2`）、`k6s3 cmp` 二份之全文、`F8 run` 二份之 `diff` 之全文、`parity` 二份之末十五列、`runall` 對拍之全文與 `diff` 之結果）；④ 塊之實得（bytes／`sha256`）與五檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **二檔之全文差異**（`§三-5`）；⑨ 工項三之 `checkidx` 之必紅與必綠、`gen_fa_index` 之出艙；⑩ **各段耗時**（讀單／撰碼／前置／驗／審查／登記／報告）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-367 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-367-adj4`。

### `§四-2`　復驗時補寫者（規格單流程·⛔ 本單之期）

發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以 CC 之碼之字樣為錨之接線檢查（`R-8` 之受併宗之鍵、`R-9` 之整體與其止、`R-10` 之逐片之序與最大面積之格、`R-12` 之二判、`R-13` 之三鍵之合、`R-16` 之二施點）及其突變之判別力；**併入主線之請示**（有土地後果·`K-9-56` 已裁·附 KL 於畫面之核對：側支之 `app.py` 於退縮 `3.5 m`／`0 m` 按「🧮 執行 G 值迭代計算」，`R3` 之抵費地 ＝ `§一` 項 `6` 之值〔以驗證之案件固定數據·畫面之地價異者其差見 `K-6` 典「`K-9-53` ① 之入主線；KL 之畫面核對」節〕、「🧭 規格步 4 乙（第一趟）」之紀錄 ＝ `1` 列）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9367_adj4.py` `1131`／`0`、`verify/probes/probe_WG9350_frontroad.py` `15`／`1`、`verify/probes/probe_WG9351_intake.py` `15`／`1`、`verify/probes/probe_WG9355_screenmerge.py` `8`／`0`、`verify/probes/probe_WG9363_k953.py` `7`／`0`、`verify/probes/probe_WG9345_screen.py` `8`／`0`（增／刪·即塊之 `@@` 所載）；工項二 ＝ `app.py`、`verify/selection_pipeline.py`（增／刪 ＝ 工項二之 `V-7` 所出艙）；工項三 ＝ `docs/rulings/K-6_街角地分配程序與可分配判準.md` `51`／`0`、`docs/reports/W-G.4_泛用阻塞項登記表.md` `16`／`0`、`docs/reports/W-G.9波_claude.ai側自誤登記.md` `22`／`0`、`CLAUDE.md` `21`／`0`、`.claude/rules/常設規則索引.md` `1`／`1`；工項四 ＝ 報告之增（刪 `0`） |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `d7a5ea4` | 生產碼相異恰 **`2`**（`app.py`、`verify/selection_pipeline.py` ＝ 工項二之 `V-7` 所出艙之 blob）；`verify/` 之一切檔相異恰 **`7`**（`A` `1`：新檔 `verify/probes/probe_WG9367_adj4.py`；`M` `6`：`verify/selection_pipeline.py` ＋ 塊 `F9p`／`F10p`／`F14p`／`F23p`／`F4p` 所改之五檔·blob 皆 ＝ `§五-1` 項 `14`）；本批之新檔（本單、`F24`、報告）之 `git check-ignore` 皆無命中 |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`15` 檔：本單、`F24`、塊所改之五器、`app.py`、`verify/selection_pipeline.py`、`K-6` 典、`GB` 簿、自誤簿、`CLAUDE.md`、常設規則索引、報告） |
| `4` | 五檔之 bytes | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `478272` → `485972`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `1042324` → `1044434`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `1119307` → `1121735`；`CLAUDE.md` `339034` → `342956`；`.claude/rules/常設規則索引.md` `25053` → `25091`（改一列）；前四者改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`36`**；主線 ＝ `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`（⛔ 變）；`verify/W-G.9-367-adj4` ＝ 工項四之 `commit`，其祖含 `d7a5ea4`；`verify/W-G.9-363-k953` ＝ `cb5490a…`、`verify/W-G.9-361-k954` ＝ `924d916…`、`verify/W-G.9-359-cand` ＝ `bd072eb…`、`verify/W-G.9-357-k948` ＝ `4716f20…`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 579 577 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 579 577` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`564`**／`MAX` **`579`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `194`／`201`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；**`K-9` `53`／`56`**／`[44, 47]`（`GB`／`VR` 皆 ＝ 開工態） |
| `8` | `python verify/probes/probe_WG9367_adj4.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑> d7a5ea4`；`… run <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9363_k953.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑> 7d8e954`；`… run <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `10` | `python verify/probes/probe_WG9330_wfns_ast.py <repo 絕對路徑>` | **`rc 0`**·**`48`／`48`／`47`** |
| `11` | `python verify/probes/probe_WG9340_main_synth.py <repo 絕對路徑>` | **`rc 0`**·「app 側宿主 ＝ f3_screen_stepg_run」 |
| `12` | `python verify/probes/probe_WG9341_synth.py <repo 絕對路徑>` | **`rc 0`** |
| `13` | `python verify/probes/probe_WG9346_failclosed.py run <repo 絕對路徑> 3.5` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9348_harvest_key.py <repo 絕對路徑>`；`python verify/probes/probe_WG9349_k9296.py selftest …`；`… wiring …`；`… run … 3.5`；`… run … 0.0` | 皆 **`rc 0`** |
| `15` | `python verify/probes/probe_WG9350_frontroad.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `16` | `python verify/probes/probe_WG9351_intake.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `17` | `python verify/probes/probe_WG9352_endblock.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `18` | `python verify/probes/probe_WG9353_endmerge.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `19` | `python verify/probes/probe_WG9354_endcontest.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`** |
| `20` | `python verify/probes/probe_WG9355_screenmerge.py selftest …`；`… run …` | 皆 **`rc 0`** |
| `21` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring …` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `22` | `python verify/probes/probe_WG9345_screen.py parity … 3.5 on <json>`；同 `0.0`；`… wiring …`；`python verify/probes/probe_WG9345_screen.py selftest` | 皆 **`rc 0`**（`parity` 之數 ＝ `V-5`） |
| `23` | `python verify/probes/probe_WG9344p1_pooltemp.py run <repo 絕對路徑> 3.5 on`；`… selftest`；`python verify/probes/probe_WG9344_k6s3.py selftest` | 皆 **`rc 0`** |
| `24` | `python verify/probes/probe_WG9357_k948.py selftest …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `25` | `python verify/probes/probe_WG9358_k948_wiring.py wiring …` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`（本部 `W0`〜`W12` 皆 ✅·二十九突變皆 ✅） |
| `26` | `python verify/probes/probe_WG9359_cand.py selftest …`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `27` | `python verify/probes/probe_WG9360_cand_mut.py mut <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `28` | `python verify/probes/probe_WG9361_k954.py selftest <repo 絕對路徑>`；`… wiring <repo 絕對路徑>`（⛔ 基準 rev·`W-G.9-363 §四-3` 閘 `27` 之註）；`… run <repo 絕對路徑>` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
| `29` | `python verify/probes/probe_WG9362_k954_mut.py mut <repo 絕對路徑>` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

🔒 **閘 `9` 之註**：`F23 wiring` 之 `W7`（頂層之相異 ⊆ 其許）之許自塊 `F23p` 起含本批之新名十一（`X-1`）；本批之頂層之限另由 `F24 wiring` 之 `W5` 量之。
🔒 **必過之實例**：發單側已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`29` ⇒ 見 `§五-1` 項 `17`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `F24` | `60474` B·`sha256` `b957dd4185b3d38ca1ba92eb48ded20e99f4ad76985193b061c7942045a1730e`·`1131` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9367_adj4.py` |
| `3` | 塊 `F9p` | `2856` B·`sha256` `adc703dcaaffac1ec256ff5f0542dd8ae4984b02e76b762db67fc10346e45db3`·`43` 列（圍欄內全文·末附換行）；抽為 `<O>\F9p.diff`，`git apply` 於 `verify/probes/probe_WG9350_frontroad.py`（施前 blob `4b11230f96d200f3eab304c31ae5600472e6c125`） |
| `4` | 塊 `F10p` | `3177` B·`sha256` `5be578bef1c0a4667777e4c3b936adbf75dc44f1150330160477ffc442376ad1`·`44` 列（圍欄內全文·末附換行）；抽為 `<O>\F10p.diff`，`git apply` 於 `verify/probes/probe_WG9351_intake.py`（施前 blob `d0ab343ad60f4a80b04ca97d002ee759124fe07c`） |
| `5` | 塊 `F14p` | `1202` B·`sha256` `cb000761c71076036f25f529180ab78b43252e9fe6d5625448cb434607d467d1`·`26` 列（圍欄內全文·末附換行）；抽為 `<O>\F14p.diff`，`git apply` 於 `verify/probes/probe_WG9355_screenmerge.py`（施前 blob `a78216399a6a5c708cff4d0b9f8bf14fa462f841`） |
| `6` | 塊 `F23p` | `2329` B·`sha256` `4b5209eeef491eb50877182c1112e1f6d7ae2d37b6a4dfbee6d61dc83fde7780`·`32` 列（圍欄內全文·末附換行）；抽為 `<O>\F23p.diff`，`git apply` 於 `verify/probes/probe_WG9363_k953.py`（施前 blob `de0a7e0629e81db3bee6d22918e169ba29cddd39`） |
| `7` | 塊 `F4p` | `2112` B·`sha256` `27181cee9f3ffe95ff0b440facb52cd5f025f2b85c8cffa5c29774a122dfafe8`·`26` 列（圍欄內全文·末附換行）；抽為 `<O>\F4p.diff`，`git apply` 於 `verify/probes/probe_WG9345_screen.py`（施前 blob `e3c4b84b0b23170477f856b7ae0b18be8704bce1`） |
| `8` | 塊 `K10` | `7700` B·`sha256` `4690b0e7598198cf24e57f8f9adc06cda7d24d474e16c213be92024d912b1399`·`51` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`478272` B）之末後，期末 ＝ `485972` B |
| `9` | 塊 `G9` | `2110` B·`sha256` `f95191c25a5e49ed1fac6c03b8f4b7189555546018bc6d10a58083cc0b0b9ef3`·`16` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.4_泛用阻塞項登記表.md`（`1042324` B）之末後，期末 ＝ `1044434` B |
| `10` | 塊 `E11` | `2428` B·`sha256` `2f776a0bcafc25a878a08326322356e9589ca29ba4efb9377088f1fd2f8a4546`·`22` 列（圍欄內全文·末附換行）；附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md`（`1119307` B）之末後，期末 ＝ `1121735` B |
| `11` | 塊 `P21` | `3922` B·`sha256` `8d7b8b135b9c777d9ed219ae41274b5e1e0aefd6f36cea28a858aad7b2862631`·`21` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`339034` B）之末後，期末 ＝ `342956` B |
| `12` | 塊 `IX2` | `2469` B·`sha256` `72ab3f82f43668e2e44a2408abcce16268eb0fde487b49005ce98e2c1a11aad6`·`13` 列（圍欄內全文·末附換行）；抽為 `<O>\IX2.diff`，`git apply` 於 `.claude/rules/常設規則索引.md`（施前 blob `dacddda92826e066813c3379fa305710adfa81bd`） |
| `13` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳·同一抽取式） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列 |
| `14` | 寫出後之 blob | `verify/probes/probe_WG9367_adj4.py` `1a984542a9e67799be6a2d7baa207776e1aa7d10`；`verify/probes/probe_WG9350_frontroad.py` `20580605bcbde90316bc7780f5e2575a2b2015d9`；`verify/probes/probe_WG9351_intake.py` `2030566ad1da1f28387df18ee7d8b5f5a2354895`；`verify/probes/probe_WG9355_screenmerge.py` `b96e2331f25a956ea3d0c600d8266f0199c72205`；`verify/probes/probe_WG9363_k953.py` `c0bc21aaa76d35b4b975cd1cf99b11b24f498b46`；`verify/probes/probe_WG9345_screen.py` `ce56266d9b698653b4e99cd145223f8434f65879`（以上工項一）；`docs/rulings/K-6_街角地分配程序與可分配判準.md` `90193df88ff64ac6a542ab1c43d2fad402d62f41`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `469b445059b37d0014badf86797421f86876e431`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `aca7f565fa03722254278215fa360285dbc11f88`；`CLAUDE.md` `f3557822bcfe0c4bb40485261290f31744c7c745`；`.claude/rules/常設規則索引.md` `a18e96d6b4d7640c84260469bb09f67b7bc41aab`（以上工項三）。🔒 `app.py`／`verify/selection_pipeline.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `15` | 量測器之二態 | 工項一之端（`d7a5ea4` ＋ 塊 `F24`／`F9p`／`F10p`／`F14p`／`F23p`／`F4p`）＝ `§一` 項 `7`；工項二施後 ＝ `§一` 項 `8`（原型為其必過之實例） |
| `16` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗六十八實跑（態 `d7a5ea4`）：🔴 機械 `0` 項／🟡 提示 `9` 項——`P-1` `:99`（`§二` 工程讀法之首列·所觸之否定字樣係「⛔ 充裁」之標、⛔ 為量之全稱 ⇒ **具名豁免**）、`P-1` `:1689`（塊 `K10` 之射程·「⛔ 及於」係射程之界、⛔ 為量之全稱 ⇒ **具名豁免**）、`P-4` `:73`（`§一` 之表頭·其箭頭之座標系 ＝ 開工態 `d7a5ea4`〔工項一之端〕至原型，表內自載 ⇒ **具名豁免**）、`P-4` `:95`／`:1670`（`K-9-56` 之問之要旨·其箭頭係受併宗之序之先後、⛔ 為方向之轉引 ⇒ **具名豁免**）、`P-4` `:125`（`§三` 之用語·其箭頭係 `a′` 之折算之自來源至受併宗，同列自定 ⇒ **具名豁免**）、`P-4` `:219`（`§四-1` 驗之表頭·其箭頭之座標系 ＝ 工項一之端〔前置〕至工項二之 `commit`〔驗〕，表內自載 ⇒ **具名豁免**）、`P-4` `:254`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `d7a5ea4` 至工項三／四之端，表內自載 ⇒ **具名豁免**）、`P-6` `:1780`（塊 `P21` 之「前節之更新」列·所觸之數係待落地表之序號、⛔ 為實測之數 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `21232`–`28952`）⇒ `rc 0` |
| `17` | 收工閘之模擬（發單側·本機 Linux·⛔ `push`） | `git worktree add --detach <S> d7a5ea4`（拋棄式·⛔ `push`）＋ 本單之前稿（塊與本單逐位同）＋ 自前稿依圍欄抽出之塊 `F24`／`F9p`／`F10p`／`F14p`／`F23p`／`F4p`（各 `git apply --check` 過）＋ 原型之二檔 ＋ 塊 `K10`／`G9`／`E11`／`P21`／`IX2` ＋ 報告之替身·五 `commit`（訊息 ＝ `§四-1` 所令逐字）：工項一之六檔之 blob ＝ 項 `14`；前置 `1`〜`5` 之出艙 ＝ `§一` 項 `7`／`9`；`V-1`〜`V-7` 皆 ＝ 其期（`V-3` 之二 `offcmp` `rc 0`、`V-4` 之 `cmp` 各 `3` 項與 `F8` 之 `diff` 各 `2` 列、`V-5`、`V-6` 之相異 `6` 項）；工項三之 `checkidx` 之必紅（不合 `1`）與必綠（不合 `0`）、`gen_fa_index` 之重生成與倉內逐位同、塊 `CK`／`GF` ＝ 項 `13`、施後之 blob ＝ 項 `14`；閘 `1` 之增刪 ＝ 其期（工項二 ＝ `app.py` `526`／`0`、`verify/selection_pipeline.py` `81`／`0`〔原型之數·⛔ 為期〕；工項四 ＝ 替身）；閘 `2` 生產碼相異 `2`、`verify/` 相異 `7`（`A` `1`·`M` `6`）、新檔三之 `git check-ignore` 皆無命中；閘 `3` CR `0`（`15` 檔·`V6.dxf` `12308`）；閘 `4` 前四檔皆嚴格前綴、其末 ＝ 項 `8`〜`11`、常設規則索引 `25091` B；閘 `6` `rc 0`（`MAX` `579`）；閘 `7` `rc 0`·四簿 ＝ 自誤 `564`／`579`、`GB` `194`／`201`、`VR` `80`／`95`、`K-9` `53`／`56`／`[44, 47]`；另 `python verify/tools/wg942_append_audit.py d7a5ea4` ⇒ `rc 0`·`結論：✅ 全部成立`（受檢 `77`·參考）；閘 `8`〜`29` 之諸器（`51` 命令·於同一樹〔`HEAD^{tree}` ＝ `b939b9b6545c56445a4ea32d41c1293ed7a6d2c3`〕之另一拋棄式 worktree 並行實跑）皆 ＝ 其期，其出艙與 `§一` 項 `8` 同；`stderr` 合計 `0` B |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·語言名不拘：本單用 `python`、`diff`、`markdown`；他單另有 `json` 等）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準，⛔ 以全檔之圍欄之序數數之（他單之圍欄之語言名⛔ 限於本單所列·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-367-adj4`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F24`（新檔 `verify/probes/probe_WG9367_adj4.py`（工項一））

````python
# -*- coding: utf-8 -*-
"""W-G.9-367 量測器（發單側窗六十八擬·檔 F24·⛔ 由受單側改一字）：規格步 4 乙（`K-9-53` ②·第一趟·`K-9-56`）——
合併單位之地主另有已配得之宗者，沿其候選街廓名單，至第一個有其已配得之宗之街廓，將合併單位之土地（`a′` 折算）併入其
已配得之宗（`app.py` 之 `adj4_pass1_run`）；並量手冊先行之 `GB-201` 之防護（`k953_manual_run`）。

子命令（一律 python verify/probes/probe_WG9367_adj4.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取受詞；`verify/selection_pipeline.py` 取 `run_adj4`）。玩具之回呼：
           `alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內之 `面積_m2` 之和 `>` 該街廓之容量 ⇒ 該街廓之配餘地
           不合格一處；`err_cap` 逾者 ⇒ 配地中止；`lose` ＝ `{宗: (門檻, 失者)}`（該宗之 `面積_m2` `>` 門檻 ⇒ 失者不保留）；
           `G` ＝ 分攤登記面積 ＋ 面積（`gmap` 覆寫）；`a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓）。
           K1〜K22 ＝ 各支（期值出自規格單 `§三`·⛔ 呼叫受測碼求期）；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
  wiring   <repo> <基準 commit>
           接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_adj4`）與 `run_corner_pk_k6b`
           之序；W3 畫面之入口（`f3_screen_adj4`）與 `f3_screen_k6b_stage3` 之序；W4 新碼⛔ 案件字面；W5 既有函式對基準
           一字未動（本單所改之三函式除外）·頂層節點之相異 ⊆ 本單之許；W6 本單所改之三函式對基準唯增列（⛔ 改既有一列）；
           W7 既有量測器之錨（其字串常數〔長 ≥ 4〕於基準之 app.py／selection_pipeline.py 恰一見者）於工作樹仍恰一見；
           基準中恰一之函式名（含巢狀）於工作樹仍恰一。（以 CC 之碼之字樣為錨之接線與突變之判別力 ＝ 復驗時補寫·另單。）
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：同一行程先設 `WV_ADJ4=off`、再去之，各跑一次：R1 第一趟之紀錄逐列 ＝
           本器所載；R2 街角第 1 宗 ＝ off 之實跑；R3 配地之變（G 之差 ＞ 容差 `0.01` 之宗、各街廓之抵費地之差）＝ 本器所載，
           且 Σ抵費地之減 ＝ ΣG 之增（容差 `0.1`）；R4 調配之輸入之類（切片數·原有面積）與合併單位數 ＝ 本器所載；
           R5 受詞之片之段三之三鍵 ＝ 本器所載。
  offsnap  <repo> <out.json> [<退縮> …]
           於行程內設 `WV_ADJ4=off`，harness 實跑本案，以 sha256 摘要其街角、宗地（暫編地號·段三之三鍵·面積二欄）、build、
           段三紀錄、末端塊紀錄、手冊先行之紀錄、配地列、入池閘紀錄、不配地紀錄、調配之輸入，寫 out。
  offcmp   <a.json> <b.json>
           二 offsnap 之摘要逐項同（第一趟之紀錄唯出艙·⛔ 入判）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, difflib, io, os, re, subprocess, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01
FN = "adj4_pass1_run"
SELF_NAME = "probe_WG9367_adj4.py"
REMAIN = "留於合併單位（規格步 5）"


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__, str(ex)[:160])
    out.append((name, got, exp))


# ── 玩具（⛔ 本案資料）──
H, RDC, PKC = "住宅區", "道路", "鄰里公園"
TB, TP = "建地軌", "公設軌"


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a, lot=None):
    return {"暫編地號": pid, "原地號": lot or pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


def _a(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, lose=None, calls=None):
    """玩具之回呼（`calls` ＝ list ⇒ 每次試算附一筆）。"""
    cap, price, gmap, err_cap, lose = cap or {}, price or {}, gmap or {}, err_cap or {}, lose or {}

    def a_prime(src, dst):
        return _a(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)

    def alloc_state(temp, build):
        if calls is not None:
            calls.append(1)
        acc = {}
        for b in build:
            acc[b["所屬街廓"]] = acc.get(b["所屬街廓"], 0.0) + float(b.get("面積_m2", 0) or 0)
        for blk, v in acc.items():
            if v > err_cap.get(blk, 1e18) + 1e-9:
                return {"kept": {}, "bad_pools": {}, "err": f"玩具之配地中止（{blk}）", "G": {}, "members": {},
                        "units": {}}
        gone = set(drop)
        by = {b["暫編地號"]: b for b in build}
        for h, (thr, lost) in lose.items():
            if h in by and float(by[h].get("面積_m2", 0) or 0) > thr + 1e-9:
                gone.add(lost)
        kept, bad, G, mem = {}, {}, {}, {}
        for b in build:
            p = b["暫編地號"]
            if p in gone:
                continue
            kept.setdefault(b["所屬街廓"], set()).add(p)
            G[p] = gmap.get(p, _a(b))
            mem[p] = [p]
        for blk, v in acc.items():
            if v > cap.get(blk, 1e18) + 1e-9:
                bad[blk] = 1
        return {"kept": kept, "bad_pools": bad, "err": None, "G": G, "members": mem, "units": {}}
    return a_prime, alloc_state


def _w():
    """世界：BA x∈[0,20]、BB x∈[20,40]、BD x∈[40,60]（y∈[0,30]·住宅區）；道路 RD（y∈[-10,0]）；公園 PK（y∈[30,50]·
    x∈[0,20]）。歸戶 g1：X1(1)（BA·分不到之建地）、X1(2)／W1(1)（BB·已配得）、Z1(1)（BD·已配得）、R1(1)（道路片）、
    P1(1)（公設片）。"""
    t = [_tp("Q1(1)", "BA", H, _R(0, 10, 0, 30), 300), _tp("X1(1)", "BA", H, _R(10, 20, 0, 30), 60),
         _tp("X1(2)", "BB", H, _R(20, 30, 0, 30), 300), _tp("W1(1)", "BB", H, _R(30, 40, 0, 30), 200),
         _tp("Z1(1)", "BD", H, _R(40, 50, 0, 30), 400), _tp("Q2(1)", "BD", H, _R(50, 60, 0, 30), 300),
         _tp("R9(1)", "RD", RDC, _R(0, 20, -10, 0), 200), _tp("R1(1)", "RD", RDC, _R(20, 30, -10, 0), 100),
         _tp("R8(1)", "RD", RDC, _R(30, 60, -10, 0), 300),
         _tp("P1(1)", "PK", PKC, _R(0, 10, 30, 50), 200), _tp("P9(1)", "PK", PKC, _R(10, 20, 30, 50), 200)]
    own = {"Q1": "gQ", "X1": "g1", "W1": "g1", "Z1": "g1", "Q2": "gQ2", "R9": "gR", "R1": "g1", "R8": "gR8",
           "P1": "g1", "P9": "gP", "V1": "g1"}
    return t, own


SJ = {"歸戶": "g1", "軌": TB, "錨點": "P1(1)", "名單": ["BA", "BB", "BD"], "片": ["X1(1)", "R1(1)", "P1(1)"],
      "原有面積合計": 360.0}
_NS = {}


def _go(*, sj=None, cap=None, price=None, drop=("X1(1)",), gmap=None, err_cap=None, lose=None, own_upd=None,
        pre=None, lot_upd=None, temp_geom=None, geom_extra=None, geom_rm=(), calls=None, raw=False):
    t, own = _w()
    own = dict(own, **(own_upd or {}))
    by = {x["暫編地號"]: x for x in t}
    geom = {x["暫編地號"]: [list(c) for c in x["polygon_coords"]] for x in t}
    for pid, poly in (geom_extra or {}).items():
        geom[pid] = [list(c) for c in poly]
    for pid in geom_rm:
        geom.pop(pid, None)
    for pid, lot in (lot_upd or {}).items():
        by[pid]["原地號"] = lot
    for pid, poly in (temp_geom or {}).items():
        by[pid]["polygon_coords"] = [list(c) for c in poly]
    for pid, kv in (pre or {}).items():
        by[pid].update(copy.deepcopy(kv))
    build = [x for x in t if x["街廓分類"] == H]
    ap, st = _cbs(cap, price, drop, gmap, err_cap, lose, calls)
    subj = [dict(SJ, **(sj or {}))] if sj is not False else []
    res = _NS["fn"](t, build, own, subj, geom, ap, st, log_print=lambda *x: None)
    return (res, t, build) if raw else res


def _rows(res):
    out = []
    for r in res[2]:
        q = tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))
        if r.get("序") == "剩下":
            out.append(("剩下", r.get("歸戶"), r.get("片"), r.get("結果"),
                        tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("餘量") or {}).items()))))
        else:
            out.append((r.get("序"), r.get("歸戶"), r.get("街廓"), r.get("片"), r.get("類"), r.get("受併宗"), q,
                        r.get("結果")))
    return out


def _keys(res):
    out = {}
    for x in res[0]:
        d = {}
        for k in ("段三併出", "段三部分併出", "段三餘量"):
            if k in x:
                v = x[k]
                d[k] = (tuple(v) if isinstance(v, list) else
                        tuple(sorted((a, round(float(b), 2)) for a, b in v.items())) if isinstance(v, dict)
                        else round(float(v), 2))
        if d:
            out[x["暫編地號"]] = d
    return out


def _acc(res):
    return {x["暫編地號"]: round(float(x.get("面積_m2", 0) or 0), 2) for x in res[0]
            if float(x.get("面積_m2", 0) or 0)}


def _bids(res):
    return [b["暫編地號"] for b in res[1]]


def _halt(fn, phrases):
    try:
        fn()
    except RuntimeError as e:
        return ("停機", all(p in str(e) for p in phrases))
    return ("無停機",)


class _FakeSt:
    """畫面之假 st：`session_state` ＝ dict；方法之呼叫依序記其名。"""

    def __init__(self):
        self.session_state = {}
        self.calls = []

    def error(self, *a, **k):
        self.calls.append("error")

    def stop(self):
        self.calls.append("stop")

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)

        def _f(*a, **k):
            self.calls.append(name)
            return contextlib.nullcontext()
        return _f


ENVS = ("WV_ADJ4", "WV_K953", "WV_K929_6")


def _setenv(vals):
    for k, v in zip(ENVS, vals):
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


# 手冊先行之世界（同 F23 之世界一·⛔ 讀 F23）——GB-201 之例
def _wk():
    t = [_tp("X1(1)", "BA", H, _R(10, 20, 0, 30), 60), _tp("X1(2)", "BB", H, _R(20, 30, 0, 30), 300),
         _tp("Y1(1)", "BB", H, _R(30, 40, 0, 30), 200), _tp("Z1(1)", "BD", H, _R(40, 50, 0, 30), 400),
         _tp("Q1(1)", "BA", H, _R(0, 10, 0, 30), 300), _tp("Q2(1)", "BD", H, _R(50, 60, 0, 30), 300),
         _tp("R1(1)", "RD", RDC, _R(20, 30, -10, 0), 100), _tp("R9(1)", "RD", RDC, _R(0, 20, -10, 0), 200),
         _tp("R8(1)", "RD", RDC, _R(30, 60, -10, 0), 300),
         _tp("C1(1)", "BC", H, _R(20, 30, -40, -10), 300), _tp("C9(1)", "BC", H, _R(0, 20, -40, -10), 300),
         _tp("C8(1)", "BC", H, _R(30, 60, -40, -10), 300),
         _tp("P1(1)", "PK", PKC, _R(20, 30, 30, 50), 200), _tp("P9(1)", "PK", PKC, _R(30, 40, 30, 50), 200)]
    own = {"X1": "g1", "Y1": "gY", "Z1": "gZ", "Q1": "gQ", "Q2": "gQ2", "R1": "g1", "R9": "gR", "R8": "gR8",
           "C1": "g1", "C9": "gC", "C8": "gC8", "P1": "g1", "P9": "gP"}
    blocks = {"BA": {"category": H}, "BB": {"category": H}, "BD": {"category": H}, "RD": {"category": RDC},
              "BC": {"category": H}, "PK": {"category": PKC}}
    return t, own, blocks, {"RD": [(-10.0, -5.0), (70.0, -5.0)]}


def _k15(ns):
    """GB-201：手冊先行中，X1(1) 之整筆併入 X1(2)（其檢核之街廓唯 BA／BB）使他街廓之某宗不保留；其後以該宗為計畫之
    受併宗之併入 ⇒ 停機（⛔ 以已失保留之宗為受併宗而靜默併入）。甲 ＝ 可拆分之片（道路片 R1(1) 之計畫含 C1(1)）；
    乙 ＝ 整筆之建地片（BE 之 X1(3) 之計畫 ＝ BD 之 Q2(1)〔同歸戶〕）。"""
    def go(lost, extra, own_upd, blk_upd, drop):
        t, own, blocks, cl = _wk()
        t += extra
        own = dict(own, **own_upd)
        blocks = dict(blocks, **blk_upd)
        build = [x for x in t if x["街廓分類"] == H]
        ap, st0 = _cbs(None, None, drop)

        def st(temp, b):
            r = st0(temp, b)
            x2 = next((x for x in temp if x["暫編地號"] == "X1(2)"), None)
            if x2 is not None and float(x2.get("面積_m2", 0) or 0) > 0:
                r["kept"] = {k: set(v) - {lost} for k, v in r["kept"].items()}
            return r
        return ns["k953_manual_run"](t, build, own, blocks, cl, ap, st, log_print=lambda *x: None)
    a = _halt(lambda: go("C1(1)", [], {}, {}, ("X1(1)",)), ["GB-201", "C1(1)", "R1(1)"])
    b = _halt(lambda: go("Q2(1)", [_tp("X1(3)", "BE", H, _R(60, 70, 0, 30), 50)], {"Q2": "g1"}, {"BE": {"category": H}},
                         ("X1(1)", "X1(3)")), ["GB-201", "Q2(1)", "X1(3)"])
    return a, b


def _k11(ns):
    def u(g, track, area, blks, inb, com):
        return {"歸戶": g, "軌": track, "原有面積合計": area, "同歸戶原位次配地之街廓": blks,
                "建築街廓內不能分配": [{"暫編地號": x} for x in inb], "共同負擔用地": [{"暫編地號": x} for x in com]}
    units = [u("gA", TP, 500.0, ["B1"], [], ["a(1)", "a(2)"]), u("gB", TB, 100.0, ["B2"], ["b(1)"], ["b(2)", "b(1)"]),
             u("gC", TB, 300.0, [], ["c(1)"], []), u("gD", TB, 100.0, ["B3"], ["d(1)"], [])]
    lists = [{"歸戶": g, "錨點": f"{g[1].lower()}(1)", "名單": [{"街廓": "B2"}, {"街廓": "B1"}]} for g in ("gA", "gB", "gC", "gD")]
    it = {"units": units}
    su = [x["歸戶"] for x in ns["adj4_subject_units"](it)]
    sj = ns["adj4_subjects"](it, lists)
    view = [(s["歸戶"], s["軌"], s["錨點"], tuple(s["名單"]), tuple(s["片"]), s["原有面積合計"]) for s in sj]
    miss = _halt(lambda: ns["adj4_subjects"](it, [x for x in lists if x["歸戶"] != "gD"]), ["gD", "無候選街廓名單"])
    dup = _halt(lambda: ns["adj4_subjects"](it, lists + [lists[0]]), ["gA", "名單重複"])
    return su, view, miss, dup


def _k18(ns):
    """adj4_plan：無受詞 ⇒ []（⛔ 求名單）；公設軌之受詞而無正面道路 ⇒ 以佔位代之、名單依距離；建地軌 ⇒ 停機。"""
    sq = lambda x0, y0: [[x0, y0], [x0 + 10, y0], [x0 + 10, y0 + 10], [x0, y0 + 10]]  # noqa: E731
    cb = [{"label": "B1", "category": H, "id": "i1"}, {"label": "B2", "category": H, "id": "i2"},
          {"label": "RD", "category": RDC, "id": "i3"}]
    g_rows = [{"所屬街廓": "B1", "推進側別": "抵費地", "暫編地號": "p1", "cut_coords": sq(0, 0)},
              {"所屬街廓": "B2", "推進側別": "抵費地", "暫編地號": "p2", "cut_coords": sq(100, 0)}]
    temp = [{"暫編地號": "r(1)", "polygon_coords": sq(80, 0)}]

    def it(track, home):
        return {"units": [{"歸戶": "g1", "軌": track, "原街廓": home, "原有面積合計": 100.0, "同歸戶原位次配地之街廓": ["B1"],
                           "建築街廓內不能分配": [], "共同負擔用地": [{"暫編地號": "r(1)", "原有面積": 100.0}]}]}
    empty = ns["adj4_plan"]({"units": [dict(it(TP, None)["units"][0], 同歸戶原位次配地之街廓=[])]},
                            None, None, None, None, None, None, None, None)
    args = (temp, g_rows, cb, {}, {}, {}, {"B1": 8.0, "B2": 8.0}, {"B1": 20.0, "B2": 20.0})
    pub = ns["adj4_plan"](it(TP, None), *args)
    pubv = [(s["歸戶"], s["軌"], s["錨點"], tuple(s["名單"]), tuple(s["片"])) for s in pub]
    bld = _halt(lambda: ns["adj4_plan"](it(TB, "B1"), *args), ["正面道路無識別符"])
    return empty, pubv, bld


def _k16(ns, sp):
    """三旗標之任一 off ⇒ harness 與畫面皆回輸入之同一物件、紀錄 []、⛔ 呼叫 st。"""
    keep = tuple(os.environ.get(k) for k in ENVS)
    t, _own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    out = []
    try:
        for vals in (("off", None, None), (None, "off", None), (None, None, "off")):
            _setenv(vals)
            fst = _FakeSt()
            fst.session_state["f3_adj4_log"] = ["舊"]
            r = sp.run_adj4(ns, fst, None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                            forced=None, slices=None)
            st = _FakeSt()
            st.session_state["f3_adj4_log"] = ["舊"]
            rr = ns["f3_screen_adj4"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={}, slices=None)
            out.append((r[0] is t, r[1] is b, fst.session_state.get("f3_adj4_log"),
                        rr["temp"] is t, rr["build"] is b, rr["log"], st.session_state.get("f3_adj4_log"), st.calls))
    finally:
        _setenv(keep)
    return tuple(out)


def _k17(ns, sp):
    """三旗標之任一其值非法 ⇒ harness 上拋；畫面走停機之路（`f3_k6b_stage3_error`·`st.error`·`st.stop`）。"""
    keep = tuple(os.environ.get(k) for k in ENVS)
    t, _own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    out = []
    try:
        for vals in (("maybe", None, None), (None, "maybe", None), (None, None, "maybe")):
            _setenv(vals)
            try:
                sp.run_adj4(ns, _FakeSt(), None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                            forced=None, slices=None)
                h1 = "無停機"
            except RuntimeError:
                h1 = "停機"
            st = _FakeSt()
            st.session_state["f3_k6b_stage3_error"] = "前之標記"
            try:
                ns["f3_screen_adj4"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={}, slices=None)
                h2 = "無停機"
            except RuntimeError:
                h2 = "停機"
            except Exception as e:  # noqa: BLE001
                h2 = type(e).__name__
            out.append((h1, h2, st.calls, str(st.session_state.get("f3_k6b_stage3_error", "")).startswith("（第一趟）"),
                        "f3_adj4_log" in st.session_state))
    finally:
        _setenv(keep)
    return tuple(out)


def _k21(ns):
    """adj4_possible（先篩·純函式）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True。"""
    t, own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    f = ns["adj4_possible"]
    tg = copy.deepcopy(t)
    for x in tg:
        if x["暫編地號"] == "R9(1)":
            x["_is_ghost_sliver"] = True
    bg = [x for x in tg if x["街廓分類"] == H]
    return (f(t, b, own), f(t, b, {}), f(t, b, None), f(t, b, {"Q1": "gQ"}), f(t, b, {"Q1": "gQ", "R9": "gQ"}),
            f(tg, bg, {"Q1": "gQ", "R9": "gQ"}), f(t, b, {"R9": "gR", "P9": "gR"}))


def _k22(ns, sp):
    """三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st。"""
    keep = tuple(os.environ.get(k) for k in ENVS)
    t, _own = _w()
    b = [x for x in t if x["街廓分類"] == H]
    try:
        _setenv((None, None, None))
        fst = _FakeSt()
        fst.session_state.update({"f3_adj4_log": ["舊"], "t8_ownership_map": {}})
        r = sp.run_adj4(ns, fst, None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                        forced=None, slices=None)
        st = _FakeSt()
        st.session_state.update({"f3_adj4_log": ["舊"], "t8_ownership_map": {}})
        rr = ns["f3_screen_adj4"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={}, slices=None)
        return (r[0] is t, r[1] is b, fst.session_state.get("f3_adj4_log"), rr["temp"] is t, rr["build"] is b,
                rr["log"], st.session_state.get("f3_adj4_log"), st.calls)
    finally:
        _setenv(keep)


def _k1(ns):
    keep = os.environ.get("WV_ADJ4")
    out = []
    try:
        for v in (None, "", " On ", "off", "OFF", "maybe"):
            if v is None:
                os.environ.pop("WV_ADJ4", None)
            else:
                os.environ["WV_ADJ4"] = v
            try:
                out.append(ns["adj4_enabled"]())
            except RuntimeError:
                out.append("停機")
    finally:
        if keep is None:
            os.environ.pop("WV_ADJ4", None)
        else:
            os.environ["WV_ADJ4"] = keep
    return tuple(out)


def _k2():
    calls = []
    res, t, b = _go(sj=False, calls=calls, raw=True)
    t2, b2 = copy.deepcopy(t), [x for x in t if x["街廓分類"] == H]
    bad = _halt(lambda: _NS["fn"](t2[:-1], b2 + [t2[-1]], {}, [], {}, None, None), ["非 temp_parcels 之片"])
    return (res[0] is t, res[1] is b, res[2], len(calls), bad)


def _k3():
    res, t, b = _go(raw=True)
    t2, b2 = res[0], res[1]
    ids = {id(x) for x in t2}
    untouched = all(float(x.get("面積_m2", 0) or 0) == 0 and "段三併出" not in x for x in t)
    return (_rows(res), _keys(res), _acc(res), _bids(res), all(id(x) in ids for x in b2), untouched, len(b))


B_ALL = ["Q1(1)", "X1(1)", "X1(2)", "W1(1)", "Z1(1)", "Q2(1)"]
B_NOX = ["Q1(1)", "X1(2)", "W1(1)", "Z1(1)", "Q2(1)"]


def _first_recv(**kw):
    return _rows(_go(sj={"名單": ["BB"], **kw.pop("sj", {})}, **kw))[0][5]


def _cases(ns, sp):
    out = []
    _NS["fn"] = ns[FN]
    _run(out, "K1 旗標：未設／空／' On ' ⇒ True；off／OFF ⇒ False；他值 ⇒ 停機", lambda: _k1(ns),
         (True, True, True, False, False, "停機"))
    _run(out, "K2 無受詞 ⇒ 回輸入之同一物件、紀錄 []、⛔ 試算；build 片不在 temp ⇒ 停機（受詞為空亦然）", _k2,
         (True, True, [], 0, ("停機", True)))
    _run(out, "K3 整體成：名單首 BA 無其已配得之宗 ⇒ 略過；BB 之受併宗 X1(2)（同原地號）；三片皆併、建地片自 build 去、"
              "輸入⛔ 改、build ⊆ temp（同物件）", _k3,
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (("X1(2)", 360.0),), "成")],
          {"P1(1)": {"段三併出": ("X1(2)",)}, "R1(1)": {"段三併出": ("X1(2)",)}, "X1(1)": {"段三併出": ("X1(2)",)}},
          {"X1(2)": 360.0}, B_NOX, True, True, 6))
    r4 = lambda: _go(cap={"BB": 150.0})  # noqa: E731
    _run(out, "K4 整體不過（BB 之容量 150）⇒ 逐片：建地整筆成、道路片取最大面積（0.01 之格）、公設片未成；剩下續往名單之"
              "下一街廓 BD（整體成·受併宗 Z1(1)）", lambda: (_rows(r4()), _keys(r4()), _acc(r4()), _bids(r4())),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 60.0),), "成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 90.0),), "部分成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (), "未成"),
           ("整體", "g1", "BD", "2 片", "—", "Z1(1)", (("Z1(1)", 210.0),), "成")],
          {"P1(1)": {"段三併出": ("Z1(1)",)}, "R1(1)": {"段三併出": ("X1(2)", "Z1(1)")},
           "X1(1)": {"段三併出": ("X1(2)",)}},
          {"X1(2)": 150.0, "Z1(1)": 210.0}, B_NOX))
    _run(out, "K4b 整體不過之列記其由（配餘地不合格）", lambda: r4()[2][0].get("不過之由"), "BB 配餘地不合格")
    r5 = lambda: _go(cap={"BB": 150.0}, sj={"名單": ["BA", "BB"]})  # noqa: E731
    _run(out, "K5 名單盡而有剩下 ⇒ 剩下之列（留於合併單位）；部分併出者之三鍵（段三部分併出·段三餘量）",
         lambda: (_rows(r5())[-1], _keys(r5())),
         (("剩下", "g1", "P1(1)、R1(1)", REMAIN, (("P1(1)", 200.0), ("R1(1)", 10.0))),
          {"R1(1)": {"段三併出": ("X1(2)",), "段三部分併出": (("X1(2)", 90.0),), "段三餘量": 10.0},
           "X1(1)": {"段三併出": ("X1(2)",)}}))
    r6 = lambda: _go(cap={"BB": 0.0, "BD": 0.0})  # noqa: E731
    _run(out, "K6 全不容 ⇒ 每街廓整體＋三逐片皆未成、剩下 ＝ 全部；⛔ 改宗地（建地片仍在 build·無鍵·無增）",
         lambda: (len(_rows(r6())), [r[-1] for r in _rows(r6())[:-1]], _rows(r6())[-1], _keys(r6()), _acc(r6()),
                  _bids(r6())),
         (9, ["未成"] * 8, ("剩下", "g1", "P1(1)、R1(1)、X1(1)", REMAIN,
                            (("P1(1)", 200.0), ("R1(1)", 100.0), ("X1(1)", 60.0))), {}, {}, B_ALL))
    sq = {"A0(1)": _R(25, 35, 40, 50)}
    _run(out, "K7 受併宗之序（同街廓有二宗）：① 同原地號居先（距離較遠亦然）② 距離近 ③ 同距離 ⇒ G 大 ④ 同 G ⇒ 暫編地號小",
         lambda: (_first_recv(sj={"錨點": "Q2(1)"}),
                  _first_recv(sj={"錨點": "Q2(1)"}, lot_upd={"X1(2)": "V1"}),
                  _first_recv(sj={"錨點": "A0(1)"}, lot_upd={"X1(2)": "V1"}, geom_extra=sq),
                  _first_recv(sj={"錨點": "A0(1)"}, lot_upd={"X1(2)": "V1"}, geom_extra=sq,
                              gmap={"X1(2)": 250.0, "W1(1)": 250.0})),
         ("X1(2)", "W1(1)", "X1(2)", "W1(1)"))
    sr = {"軌": TP, "錨點": "R1(1)", "名單": ["BB"], "片": ["R1(1)"], "原有面積合計": 100.0}
    pre = {"R1(1)": {"段三併出": ["Q9(1)"], "段三部分併出": {"Q9(1)": 40.0}, "段三餘量": 60.0}}
    _run(out, "K8 前已有段三之三鍵之片：其剩下 ＝ 段三餘量；全併 ⇒ 段三併出合之、去部分二鍵；部分 ⇒ 段三部分併出合之、"
              "段三餘量 ＝ 新剩下",
         lambda: (_rows(_go(sj=sr, pre=pre)), _keys(_go(sj=sr, pre=pre)), _rows(_go(sj=sr, pre=pre, cap={"BB": 50.0})),
                  _keys(_go(sj=sr, pre=pre, cap={"BB": 50.0}))),
         ([("整體", "g1", "BB", "1 片", "—", "X1(2)", (("X1(2)", 60.0),), "成")],
          {"R1(1)": {"段三併出": ("Q9(1)", "X1(2)")}},
          [("整體", "g1", "BB", "1 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 50.0),), "部分成"),
           ("剩下", "g1", "R1(1)", REMAIN, (("R1(1)", 10.0),))],
          {"R1(1)": {"段三併出": ("Q9(1)", "X1(2)"), "段三部分併出": (("Q9(1)", 40.0), ("X1(2)", 50.0)),
                     "段三餘量": 10.0}}))
    _run(out, "K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（其分不到之前提不成立）", lambda: _halt(lambda: _go(drop=()),
                                                                          ["X1(1)", "分不到之前提不成立"]), ("停機", True))
    _run(out, "K10 現態之配地中止 ⇒ 停機", lambda: _halt(lambda: _go(err_cap={"BB": -1.0}), ["現態之配地中止"]),
         ("停機", True))
    _run(out, "K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ "
              "共同負擔用地（相異）；無名單 ⇒ 停機；名單重複 ⇒ 停機", lambda: _k11(ns),
         (["gA", "gB", "gD"],
          [("gB", TB, "b(1)", ("B2", "B1"), ("b(1)", "b(2)"), 100.0), ("gD", TB, "d(1)", ("B2", "B1"), ("d(1)",), 100.0),
           ("gA", TP, "a(1)", ("B2", "B1"), ("a(1)", "a(2)"), 500.0)],
          ("停機", True), ("停機", True)))
    far = {"W1(1)": _R(1000, 1010, 0, 30)}
    _run(out, "K12 GB-199：受併宗之序之距離取 slice_geom 之原形（temp 之形縱異亦然）；片之原形缺 ⇒ 停機",
         lambda: (_first_recv(sj={"錨點": "Q2(1)"}, lot_upd={"X1(2)": "V1"}, temp_geom=far),
                  _halt(lambda: _go(geom_rm=("R1(1)",)), ["R1(1)", "原形缺"])),
         ("W1(1)", ("停機", True)))
    pr = {"BB": 2.0}
    r13 = lambda: _go(price=pr, cap={"BB": 100.0}, sj={"名單": ["BA", "BB"]})  # noqa: E731
    _run(out, "K13 a′ 折算（K-9-45 二）：併入量 ＝ 來源面積 × p(來源) ÷ p(受併宗)；最大面積之格取來源面積；三鍵之部分併出記"
              "來源面積",
         lambda: (_rows(_go(price=pr, sj={"名單": ["BB"]})), _acc(_go(price=pr, sj={"名單": ["BB"]})), _rows(r13()),
                  _keys(r13())),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (("X1(2)", 180.0),), "成")], {"X1(2)": 180.0},
          [("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (("X1(2)", 30.0),), "成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 50.0),), "成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (("X1(2)", 20.0),), "部分成"),
           ("剩下", "g1", "P1(1)", REMAIN, (("P1(1)", 160.0),))],
          {"P1(1)": {"段三併出": ("X1(2)",), "段三部分併出": (("X1(2)", 40.0),), "段三餘量": 160.0},
           "R1(1)": {"段三併出": ("X1(2)",)}, "X1(1)": {"段三併出": ("X1(2)",)}}))
    r14 = lambda: _go(lose={"X1(2)": (50.0, "W1(1)")}, sj={"名單": ["BA", "BB"]})  # noqa: E731
    _run(out, "K14 「不影響原位次」：併入使同街廓原保留之宗不保留 ⇒ 不過（整體與逐片皆然）",
         lambda: (_rows(r14()), r14()[2][0].get("不過之由")),
         ([("整體", "g1", "BB", "3 片", "—", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "X1(1)", "建地", "X1(2)", (), "未成"),
           ("逐片", "g1", "BB", "R1(1)", "道路", "X1(2)", (("X1(2)", 50.0),), "部分成"),
           ("逐片", "g1", "BB", "P1(1)", "公設地", "X1(2)", (), "未成"),
           ("剩下", "g1", "P1(1)、R1(1)、X1(1)", REMAIN, (("P1(1)", 200.0), ("R1(1)", 50.0), ("X1(1)", 60.0)))],
          "BB 原保留之宗 ['W1(1)'] 不保留"))
    _run(out, "K15 GB-201（手冊先行）：計畫之受併宗於當下之試算未保留 ⇒ 停機（可拆分之片／整筆之建地片）", lambda: _k15(ns),
         (("停機", True), ("停機", True)))
    no_call = ((True, True, [], True, True, [], [], []),) * 3
    _run(out, "K16 三旗標（WV_ADJ4／WV_K953／WV_K929_6）之任一 off ⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 呼叫 st",
         lambda: _k16(ns, sp), no_call)
    _run(out, "K17 三旗標之任一其值非法 ⇒ harness 停機；畫面 ⇒ f3_k6b_stage3_error ＝ （第一趟）…、st.error、st.stop、"
              "⛔ 寫紀錄", lambda: _k17(ns, sp), (("停機", "停機", ["error", "stop"], True, False),) * 3)
    _run(out, "K18 adj4_plan：無受詞 ⇒ []；唯公設軌 ⇒ 正面道路之缺以佔位代之、名單依距離；建地軌 ⇒ 停機（正面道路無識別符）",
         lambda: _k18(ns), ([], [("g1", TP, "r(1)", ("B2", "B1"), ("r(1)",))], ("停機", True)))
    _run(out, "K19 adj4_depth_of：取 f3_alloc_depth_by_label（缺 ⇒ {}）；回新 dict",
         lambda: (ns["adj4_depth_of"]({"f3_alloc_depth_by_label": {"B1": 20.0}}), ns["adj4_depth_of"]({}),
                  ns["adj4_depth_of"](None)), ({"B1": 20.0}, {}, {}))
    bu = [{"暫編地號": "u(1)", "入池閘併入": ["u(1)", "u(2)"]}, {"暫編地號": "v(1)"}]
    _run(out, "K20 adj4_trial_state：摘要 ＋ err ＋ 成員與單元（成員 ≥ 2 者為單元·深拷貝）",
         lambda: (lambda r: (sorted(r), r["kept"], r["err"], r["members"], sorted(r["units"]),
                             r["units"]["u(1)"] is not bu[0]))(
             ns["adj4_trial_state"]({"kept": {"B1": {"u(1)"}}, "bad_pools": {}, "G": {"u(1)": 1.0}}, None, bu)),
         (["G", "bad_pools", "err", "kept", "members", "units"], {"B1": {"u(1)"}}, None,
          {"u(1)": ["u(1)", "u(2)"], "v(1)": ["v(1)"]}, ["u(1)"], True))
    _run(out, "K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True",
         lambda: _k21(ns), (True, False, False, False, True, False, False))
    _run(out, "K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st",
         lambda: _k22(ns, sp), (True, True, [], True, True, [], [], []))
    return out


def _perturb(v):
    if isinstance(v, bool):
        return not v
    if isinstance(v, (int, float)):
        return v + 1
    if isinstance(v, str):
        return v + "′"
    if isinstance(v, tuple):
        return (v + ("′",)) if not v else (_perturb(v[0]),) + v[1:]
    if isinstance(v, list):
        return v + ["′"]
    if isinstance(v, dict):
        return dict(v, **{"′": 0})
    return ("′", v)


def _need(ns, sp):
    names = (FN, "adj4_enabled", "adj4_possible", "adj4_subject_units", "adj4_subjects", "adj4_plan", "adj4_depth_of",
             "adj4_trial_state",
             "f3_screen_adj4",
             "k953_manual_run", "k953_enabled", "k929_6_enabled")
    return [n for n in names if n not in ns] + ([] if hasattr(sp, "run_adj4") else ["run_adj4"])


def selftest(repo):
    ns, _ = _harvest(repo)
    import selection_pipeline as sp
    need = _need(ns, sp)
    if need:
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    cases = _cases(ns, sp)
    print("── 規格步 4 乙（K-9-53 ②·第一趟）之各支 ──")
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    hits = 0
    for i in range(len(cases)):
        pert = [(n, g, (_perturb(e) if j == i else e)) for j, (n, g, e) in enumerate(cases)]
        r = _report(pert, verbose=False)
        base = set(red)
        code = cases[i][0].split()[0]
        if (set(r) - base) == {code} or (code in base and set(r) == base):
            hits += 1
    ok0 = hits == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {hits}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0




# ── wiring ──
CASE_LIT_RE = re.compile(r"^(R\d+|RD\d+|G\d+|G0\d\d|\d{3}(-\d+)?(\(\d+\))?|left|right|左|右|住宅區|商業區)$")
SIG = ["temp_parcels", "build_parcels", "own_map", "subjects", "slice_geom", "a_prime", "alloc_state"]
NEW_APP = {"adj4_enabled": [], "adj4_possible": ["temp_parcels", "build_parcels", "own_map"],
           "adj4_subject_units": ["intake"], "adj4_subjects": ["intake", "cand_lists"],
           "adj4_depth_of": ["session"], "adj4_trial_state": ["summary", "err", "build_used"],
           "adj4_plan": ["intake", "temp_parcels", "g_rows", "classified_blocks", "eff_min_build_by",
                         "front_derive_by", "front_name_by", "width_by", "depth_by"],
           FN: SIG, "f3_screen_adj4": ["st"]}
NEW_CONST = ("ADJ4_ENV", "ADJ4_IDENT_UNUSED")
CHG_APP = ("k953_manual_run", "f3_screen_k6b_stage3")
RA_SIG = ["ns", "fake_st", "cb", "cad", "param_rows", "temp_parcels", "build_parcels", "setback"]
RA_KW = ["snapshot", "callbacks", "winners", "forced", "slices"]
CHG_SP = ("run_corner_pk_k6b",)


def _git_show(repo, rev, rel):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{rel}"], capture_output=True,
                          check=True).stdout.decode("utf-8")


def _defs(src):
    tree = ast.parse(src)
    return {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}, tree


def _calls(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            nm = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)
            if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant):
                nm = str(f.slice.value)
            out.append((nm, n.lineno, n.col_offset, n))
    return sorted(out, key=lambda x: (x[1], x[2]))


def _top_dump(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            k = n.name
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            k = n.targets[0].id
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            k = n.target.id
        else:
            k = f"<{type(n).__name__}>"
        out.setdefault(k, []).append(ast.dump(n))
    return out


def _fn_names(src):
    out = {}
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[n.name] = out.get(n.name, 0) + 1
    return out


def _kw(call, name):
    for k in call.keywords:
        if k.arg == name:
            return k.value
    return None


def _insert_only(old, new):
    """old → new 之差唯增列（⛔ 改、⛔ 刪既有一列）且增段 ≥ 1。回 (ok, 增段數, 說明)。"""
    a, b = old.splitlines(), new.splitlines()
    ops = difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes()
    bad = [(t, i1 + 1, i2) for t, i1, i2, _j1, _j2 in ops if t not in ("equal", "insert")]
    ins = [j2 - j1 for t, _i1, _i2, j1, j2 in ops if t == "insert"]
    return (not bad and len(ins) > 0), len(ins), f"非增之段（基準之列）{bad[:3]}"


def _wiring_checks(repo, base, app=None, spp=None):
    chk = []
    if app is None:
        app = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    if spp is None:
        spp = open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read()
    ad, atree = _defs(app)
    sd, stree = _defs(spp)
    # W1 新名與簽名
    consts = {}
    for n in atree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
                and isinstance(n.value, ast.Constant):
            consts.setdefault(n.targets[0].id, []).append(n.value.value)
    fsig = {nm: ([a.arg for a in ad[nm].args.args] if nm in ad else None) for nm in NEW_APP}
    okk = (ad.get(FN) is not None and [a.arg for a in ad[FN].args.kwonlyargs] == ["log_print"]
           and ad.get("f3_screen_adj4") is not None
           and [a.arg for a in ad["f3_screen_adj4"].args.kwonlyargs] == ["pk_kwargs", "g_kwargs", "slices"])
    okc = (consts.get("ADJ4_ENV") == ["WV_ADJ4"] and len(consts.get("ADJ4_IDENT_UNUSED") or []) == 1
           and isinstance(consts["ADJ4_IDENT_UNUSED"][0], str) and consts["ADJ4_IDENT_UNUSED"][0].strip() != "")
    ra = sd.get("run_adj4")
    oks = (ra is not None and [a.arg for a in ra.args.args] == RA_SIG and [a.arg for a in ra.args.kwonlyargs] == RA_KW)
    chk.append(("W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）",
                fsig == NEW_APP and okk and okc and oks, f"簽名 {fsig == NEW_APP}／kw {okk}／常數 {okc}／harness {oks}"))
    # W2 harness 之入口與序
    cra = _calls(ra) if ra is not None else []
    need_ra = ("adj4_enabled", "k953_enabled", "k929_6_enabled", "adj4_possible", "adj_intake", "adj4_plan",
               "k953_alloc_summary", "adj4_trial_state", "adj4_depth_of", "run_step_g")
    okr = (ra is not None and sum(1 for c in cra if c[0] == FN) == 1 and sum(1 for c in cra if c[0] == "adj4_plan") == 1
           and all(any(c[0] == nm for c in cra) for nm in need_ra)
           and not any(c[0] in ("run_corner_pk", "run_corner_pk_k6b", "run_k953") for c in cra))
    pk = sd.get("run_corner_pk_k6b")
    cs = _calls(pk) if pk is not None else []
    i_k = [c for c in cs if c[0] == "run_k953"]
    i_a = [c for c in cs if c[0] == "run_adj4"]
    i_pk_after = [c for c in cs if c[0] == "run_corner_pk" and i_a and c[1] > i_a[0][1]]
    sl = _kw(i_a[0][3], "slices") if i_a else None
    okw = (len(i_k) == 1 and len(i_a) == 1 and i_a[0][1] > i_k[0][1] and not i_pk_after
           and {k.arg for k in i_a[0][3].keywords} >= {"winners", "forced", "callbacks", "snapshot", "slices"}
           and isinstance(sl, ast.Name) and sl.id == "temp_parcels")
    asg_ok = False
    ret_ok = False
    if pk is not None and i_a:
        for n in ast.walk(pk):
            if isinstance(n, ast.Assign) and n.value is i_a[0][3]:
                tg = n.targets[0]
                asg_ok = isinstance(tg, ast.Tuple) and [getattr(e, "id", None) for e in tg.elts] == ["temp3", "build3"]
        last = pk.body[-1]
        ret_ok = (isinstance(last, ast.Return) and isinstance(last.value, ast.Tuple)
                  and [getattr(e, "id", None) for e in last.value.elts[-2:]] == ["temp3", "build3"])
    chk.append(("W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫"
                "街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ "
                "回傳之末二值、其後⛔ 再呼叫 run_corner_pk", okr and okw and asg_ok and ret_ok,
                f"入口 {okr}／序 {okw}／承接 {asg_ok}／回傳 {ret_ok}"))
    # W3 畫面之入口與序
    fs = ad.get("f3_screen_adj4")
    cfs = _calls(fs) if fs is not None else []
    need_fs = ("adj4_enabled", "k953_enabled", "k929_6_enabled", "adj4_possible", "adj_intake", "adj4_plan",
               "f3_screen_stepg_run",
               "k6b_screen_callbacks", "k953_alloc_summary", "adj4_trial_state", "adj4_depth_of")
    ok3 = (fs is not None and sum(1 for c in cfs if c[0] == FN) == 1 and sum(1 for c in cfs if c[0] == "adj4_plan") == 1
           and all(any(c[0] == nm for c in cfs) for nm in need_fs)
           and not any(c[0] in ("f3_screen_corner_pk_run", "f3_screen_k6b_stage3", "f3_screen_k953") for c in cfs))
    s3 = ad.get("f3_screen_k6b_stage3")
    c5 = _calls(s3) if s3 is not None else []
    i5k = [c for c in c5 if c[0] == "f3_screen_k953"]
    i5a = [c for c in c5 if c[0] == "f3_screen_adj4"]
    sl5 = _kw(i5a[0][3], "slices") if i5a else None
    t0 = False
    for n in (s3.body if s3 is not None else []):
        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple) \
                and [getattr(e, "id", None) for e in n.targets[0].elts] == ["temp0", "build0"]:
            t0 = ast.unparse(n.value) == "(pk_kwargs['temp_parcels'], pk_kwargs['build_parcels'])"
    ok4 = (len(i5k) == 1 and len(i5a) == 1 and i5a[0][1] > i5k[0][1] and isinstance(sl5, ast.Name)
           and sl5.id == "temp0" and t0)
    chk.append(("W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、"
                "⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0"
                "（＝ pk_kwargs['temp_parcels']）", ok3 and ok4, f"入口 {ok3}／序 {ok4}"))
    # W4 新碼⛔ 案件字面
    lits = []
    for nm, node in [(k, ad.get(k)) for k in NEW_APP] + [("run_adj4", ra)]:
        for x in (ast.walk(node) if node is not None else []):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
                lits.append((nm, x.value))
    chk.append(("W4 新碼⛔ 案件字面", not lits, str(lits)))
    try:
        bapp = _git_show(repo, base, "app.py")
        bsp = _git_show(repo, base, "verify/selection_pipeline.py")
    except Exception as e:  # noqa: BLE001
        chk.append(("W5 頂層之相異 ⊆ 本單之許", False, f"基準讀不到：{type(e).__name__}"))
        return chk
    # W5 頂層之相異 ⊆ 本單之許
    allow_app = set(NEW_APP) | set(NEW_CONST) | set(CHG_APP)
    allow_sp = {"run_adj4"} | set(CHG_SP)
    for nm_, cur_, old_, allow_ in (("app.py", atree, ast.parse(bapp), allow_app),
                                    ("verify/selection_pipeline.py", stree, ast.parse(bsp), allow_sp)):
        a_, b_ = _top_dump(cur_), _top_dump(old_)
        diff = sorted(k for k in set(a_) | set(b_) if a_.get(k) != b_.get(k))
        chk.append((f"W5 {nm_} 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）", set(diff) <= allow_,
                    f"相異 {diff}；逾 {sorted(set(diff) - allow_)}"))
    # W6 本單所改之三函式：唯增列、增列皆屬本單
    bd, _ = _defs(bapp)
    bsd, _ = _defs(bsp)
    w6 = []
    for nm, cur, old, src_c, src_o in [(n, ad.get(n), bd.get(n), app, bapp) for n in CHG_APP] + \
                                      [(n, sd.get(n), bsd.get(n), spp, bsp) for n in CHG_SP]:
        if cur is None or old is None:
            w6.append((nm, False, 0, "缺"))
            continue
        ok_, k_, note_ = _insert_only(ast.get_source_segment(src_o, old), ast.get_source_segment(src_c, cur))
        w6.append((nm, ok_, k_, note_))
    chk.append(("W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列"
                "（⛔ 改、⛔ 刪既有一列）", all(x[1] for x in w6), "；".join(f"{a} {b}·增段 {c}" + ("" if b else f"（{d}）")
                                                       for a, b, c, d in w6)))
    # W7 既有量測器之錨仍恰一見；基準中恰一之函式名仍恰一
    lits8 = set()
    pdir = os.path.join(repo, "verify", "probes")
    for p8 in sorted(os.listdir(pdir)):
        if not p8.endswith(".py") or p8 == SELF_NAME:
            continue
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                t8 = ast.parse(open(os.path.join(pdir, p8), encoding="utf-8").read())
        except Exception:  # noqa: BLE001
            continue
        for x in ast.walk(t8):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and len(x.value) >= 4:
                lits8.add(x.value)
    for nm_, cur_s, old_s in (("app.py", app, bapp), ("verify/selection_pipeline.py", spp, bsp)):
        anc = [x for x in lits8 if old_s.count(x) == 1]
        moved = sorted((x[:60], cur_s.count(x)) for x in anc if cur_s.count(x) != 1)
        fb, fc = _fn_names(old_s), _fn_names(cur_s)
        dup = sorted((k, fc.get(k, 0)) for k, v in fb.items() if v == 1 and fc.get(k, 0) != 1)
        chk.append((f"W7 {nm_}：既有量測器之錨（{len(anc)}）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·"
                    f"{sum(1 for v in fb.values() if v == 1)}）仍恰一", not moved and not dup,
                    f"錨之異 {moved[:6]}；函式名之異 {dup[:8]}"))
    return chk


def wiring(repo, base):
    chk = _wiring_checks(repo, base)
    red = []
    for name, ok, note in chk:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本案（harness）──
# 第一趟之紀錄之 (序, 歸戶, 街廓, 片, 類, 受併宗, ((受併宗, 併入量 2 位)…), 結果)／剩下 ⇒ (剩下, 歸戶, 片, 結果, 餘量)
R1_EXPECT = {
    3.5: [("整體", "G001", "R3", "1 片", "—", "628-34(2)", (("628-34(2)", 13.15),), "成")],
    0.0: [("整體", "G001", "R3", "1 片", "—", "628-34(2)", (("628-34(2)", 13.15),), "成")],
}
# 配地之變（off → on）：{暫編地號: (G_off 2 位, G_on 2 位)}（|ΔG| ＞ 容差者）；{街廓: (抵費地_off, 抵費地_on)}
R3_EXPECT = {
    3.5: ({"628-34(2)": (250.24, 257.91)}, {"R3": (1659.06, 1651.41)}),
    0.0: ({"628-34(2)": (250.24, 257.91)}, {"R3": (1659.05, 1651.41)}),
}
# 調配之輸入之類（切片數, 原有面積合計 ㎡）與合併單位數；off → on 之去者（歸戶）
_R4_TOT = {"共同負擔用地·入合併單位": (31, 7103.74), "原位次配地": (74, 26324.86),
           "建築街廓內不能分配": (13, 1432.13), "無地號之殘料": (8, 0.0)}
R4_EXPECT = {3.5: (_R4_TOT, 17, ["G001"]), 0.0: (_R4_TOT, 17, ["G001"])}
# 受詞之片之段三之三鍵
R5_EXPECT = {3.5: {"628-3(1)": {"段三併出": ("628-34(2)",)}}, 0.0: {"628-3(1)": {"段三併出": ("628-34(2)",)}}}


def _pipeline(ns, fst, rv, sp, sb):
    from stepg_pipeline import run_step_g
    with contextlib.redirect_stdout(io.StringIO()):
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fst, snap)
        rv.build_ownership(ns, fst, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
        params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
        res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
        log = copy.deepcopy(fst.session_state.get("f3_adj4_log"))
        ns["K917_DROPPED"].clear()
        sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                        eff_min_build_by_blk={})
    drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
    own = dict(fst.session_state.get("t8_ownership_map") or {})
    bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
    it = ns["adj_intake"](res[5], sg["k929_6"]["build"], sg["g_rows"], drops, own, bur)
    return log, sg["g_rows"], it, res[5]


def _norm(log):
    out = []
    for r in log or []:
        q = tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))
        if r.get("序") == "剩下":
            out.append(("剩下", r.get("歸戶"), r.get("片"), r.get("結果"),
                        tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("餘量") or {}).items()))))
        else:
            out.append((r.get("序"), r.get("歸戶"), r.get("街廓"), r.get("片"), r.get("類"), r.get("受併宗"), q,
                        r.get("結果")))
    return out


def _gpool(rows):
    g = {str(r["暫編地號"]): (r["所屬街廓"], r["推進側別"], float(r["G(㎡)"])) for r in rows
         if r.get("推進側別") in ("left", "right")}
    p = {}
    for r in rows:
        if r.get("推進側別") == "抵費地":
            p[r["所屬街廓"]] = p.get(r["所屬街廓"], 0.0) + float(r.get("幾何面積(㎡)") or 0)
    return g, p


def _keys_of(temp, ids):
    out = {}
    for t in temp:
        if str(t["暫編地號"]) not in ids:
            continue
        d = {}
        for k in ("段三併出", "段三部分併出", "段三餘量"):
            if k in t:
                v = t[k]
                d[k] = (tuple(v) if isinstance(v, list) else
                        tuple(sorted((a, round(float(b), 2)) for a, b in v.items())) if isinstance(v, dict)
                        else round(float(v), 2))
        out[str(t["暫編地號"])] = d
    return out


def run(repo, sbs, show=False):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if FN not in ns or not hasattr(sp, "run_adj4"):
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    red = []
    for sb in sbs:
        env = os.environ.get("WV_ADJ4")
        try:
            os.environ["WV_ADJ4"] = "off"
            log0, rows0, it0, _t0 = _pipeline(ns, fst, rv, sp, sb)
            if env is None:
                os.environ.pop("WV_ADJ4", None)
            else:
                os.environ["WV_ADJ4"] = env
            log, rows, it, temp = _pipeline(ns, fst, rv, sp, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {sb}：執行中止 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
            print("⇒ rc 3（無從判定）")
            return 3
        finally:
            if env is None:
                os.environ.pop("WV_ADJ4", None)
            else:
                os.environ["WV_ADJ4"] = env
        got1 = _norm(log)
        ok1 = log0 == [] and got1 == R1_EXPECT.get(sb)
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：第一趟之紀錄 {len(got1)} 列 ＝ 本器所載（off 之紀錄 ＝ []：{log0 == []}）")
        if not ok1:
            red.append(f"R1@{sb}")
            print(f"      得 {got1!r}")
        c0 = sorted((r["所屬街廓"], r["推進側別"], str(r["暫編地號"])) for r in rows0 if r.get("驗_宗序") == "街角第1宗")
        c1 = sorted((r["所屬街廓"], r["推進側別"], str(r["暫編地號"])) for r in rows if r.get("驗_宗序") == "街角第1宗")
        ok2 = c0 == c1 and len(c0) > 0
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：街角第 1 宗 ＝ off 之實跑 {ok2}（{len(c1)} 宗）")
        if not ok2:
            red.append(f"R2@{sb}")
        g0, p0 = _gpool(rows0)
        g1, p1 = _gpool(rows)
        dg_ = {k: (round(g0[k][2], 2) if k in g0 else None, round(g1[k][2], 2) if k in g1 else None)
               for k in sorted(set(g0) | set(g1))
               if k not in g0 or k not in g1 or g0[k][:2] != g1[k][:2] or abs(g0[k][2] - g1[k][2]) > TOL}
        dp_ = {k: (round(p0.get(k, 0.0), 2), round(p1.get(k, 0.0), 2)) for k in sorted(set(p0) | set(p1))
               if abs(p0.get(k, 0.0) - p1.get(k, 0.0)) > TOL}
        sdg = sum(v[2] for v in g1.values()) - sum(v[2] for v in g0.values())
        sdp = sum(p1.values()) - sum(p0.values())
        sabs = sum(abs(g1[k][2] - g0[k][2]) for k in set(g0) & set(g1))
        ok3 = (dg_, dp_) == R3_EXPECT.get(sb) and abs(sdg + sdp) <= 0.1
        print(("  ✅" if ok3 else "  🔴") + f" R3@{sb}：配地之變 {len(dg_)} 宗·抵費地之變 {len(dp_)} 街廓 ＝ 本器所載；"
              f"ΣΔG {sdg:+.4f}（Σ|ΔG| {sabs:.4f}）／ΣΔ抵費地 {sdp:+.4f}（和 {sdg + sdp:+.4f}·≤ 0.1）")
        if not ok3 or show:
            print(f"      得 {(dg_, dp_)!r}")
            if not ok3:
                red.append(f"R3@{sb}")
        tot = {k: (v[0], round(v[1], 2)) for k, v in sorted(it["totals"].items())}
        e4 = (tot, len(it["units"]), sorted({u["歸戶"] for u in it0["units"]} - {u["歸戶"] for u in it["units"]}))
        ok4 = e4 == R4_EXPECT.get(sb)
        print(("  ✅" if ok4 else "  🔴") + f" R4@{sb}：調配之輸入之類·合併單位數 {e4[1]}·去者 {e4[2]} ＝ 本器所載")
        if not ok4 or show:
            print(f"      得 {e4!r}")
            if not ok4:
                red.append(f"R4@{sb}")
        k5 = _keys_of(temp, _subj_pieces(log, temp))
        ok5 = k5 == R5_EXPECT.get(sb)
        print(("  ✅" if ok5 else "  🔴") + f" R5@{sb}：受詞之片之段三之三鍵 ＝ 本器所載（{len(k5)} 片）")
        if not ok5 or show:
            print(f"      得 {k5!r}")
            if not ok5:
                red.append(f"R5@{sb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _subj_pieces(log, temp):
    """紀錄所及之片：逐片之列之片 ＋ 剩下之列之片 ＋ 整體之列之受併宗所承之片（temp 之段三併出含之者）。"""
    ids = set()
    rcv = set()
    for r in log or []:
        if r.get("序") == "逐片":
            ids.add(str(r["片"]))
        elif r.get("序") == "剩下":
            ids |= set(str(r["片"]).split("、"))
        elif r.get("序") == "整體":
            rcv.add(str(r["受併宗"]))
    for t in temp:
        if set(t.get("段三併出") or []) & rcv:
            ids.add(str(t["暫編地號"]))
    return ids


# ── offsnap／offcmp：旗標 off ⇒ 逐位同開工態 ──
def _canon(x):
    import hashlib
    import json
    b = json.dumps(x, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha256(b).hexdigest(), len(b)


def offsnap(repo, out, sbs):
    import json
    os.environ["WV_ADJ4"] = "off"           # 行程內自設（開工態無此旗標 ⇒ 無作用）
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    from stepg_pipeline import run_step_g
    snap_out = {}
    for sb in sbs:
        ns["K917_DROPPED"].clear()
        with contextlib.redirect_stdout(io.StringIO()):
            snap = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fst, snap)
            rv.build_ownership(ns, fst, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
            params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
            res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
            ss = fst.session_state
            s3log = copy.deepcopy(ss.get("f3_k6b_stage3_log"))
            eblog = copy.deepcopy(ss.get("f3_end_block_merge_log"))
            k953 = copy.deepcopy(ss.get("f3_k953_log"))
            a4 = ss.get("f3_adj4_log", "<缺>")
            ns["K917_DROPPED"].clear()
            sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                            eff_min_build_by_blk={})
        drops = {f"{k}": list(v) for k, v in ns["K917_DROPPED"].items()}
        own = dict(fst.session_state.get("t8_ownership_map") or {})
        bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
        it = ns["adj_intake"](res[5], sg["k929_6"]["build"], sg["g_rows"], ns["K917_DROPPED"], own, bur)
        part = {
            "街角": [res[3], res[4]],
            "宗地": [[t.get("暫編地號"), t.get("段三併出"), t.get("段三部分併出"), t.get("段三餘量"),
                     t.get("面積_m2"), t.get("分攤登記面積_m2")] for t in res[5]],
            "build": [b.get("暫編地號") for b in res[6]],
            "段三紀錄": s3log, "末端塊紀錄": eblog, "手冊先行之紀錄": k953,
            "配地": sg["g_rows"], "入池閘": sg["k929_6"].get("log"), "不配地": drops,
            "調配之輸入": {"totals": it["totals"], "units": it["units"], "step4": it["step4"]},
        }
        snap_out[str(sb)] = {k: _canon(v) for k, v in part.items()}
        snap_out[str(sb)]["第一趟之紀錄"] = (a4 if a4 == "<缺>" else len(a4))
        print(f"  {sb}：" + "；".join(f"{k} {v[0][:12]}" for k, v in snap_out[str(sb)].items() if isinstance(v, tuple))
              + f"；第一趟之紀錄 {snap_out[str(sb)]['第一趟之紀錄']}")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(snap_out, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print(f"⇒ 寫 {out}；rc 0")
    return 0


def offcmp(a, b):
    import json
    A, B = json.load(open(a, encoding="utf-8")), json.load(open(b, encoding="utf-8"))
    red = []
    for sb in sorted(set(A) | set(B)):
        for k in sorted(set(A.get(sb, {})) | set(B.get(sb, {}))):
            if k == "第一趟之紀錄":
                continue
            ok = A.get(sb, {}).get(k) == B.get(sb, {}).get(k)
            print(("  ✅ " if ok else "  🔴 ") + f"{sb}·{k}")
            if not ok:
                red.append(f"{sb}·{k}")
        print(f"  ℹ️ {sb}·第一趟之紀錄：{A.get(sb, {}).get('第一趟之紀錄')} → {B.get(sb, {}).get('第一趟之紀錄')}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "offcmp" and len(argv) == 4:
        return offcmp(os.path.abspath(argv[2]), os.path.abspath(argv[3]))
    repo = os.path.abspath(argv[2])
    if cmd == "selftest" and len(argv) == 3:
        return selftest(repo)
    if cmd == "wiring" and len(argv) == 4:
        return wiring(repo, argv[3])
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    if cmd == "offsnap" and len(argv) >= 4:
        return offsnap(repo, os.path.abspath(argv[3]), [float(x) for x in argv[4:]] or [3.5, 0.0])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `F9p`（`git apply` 之差異·`verify/probes/probe_WG9350_frontroad.py`）

````diff
diff --git a/verify/probes/probe_WG9350_frontroad.py b/verify/probes/probe_WG9350_frontroad.py
index 4b11230..2058060 100644
--- a/verify/probes/probe_WG9350_frontroad.py
+++ b/verify/probes/probe_WG9350_frontroad.py
@@ -10,7 +10,8 @@
   wiring   <repo>
            AST 查接線：W1 具名常數；W2 `parse_cad_precision_layers` 之初值鍵、折線頂點之留存、推導之呼叫與候選集
            （非可建築土地之補集）；W3 `main()` 之 session 寫入與二顯示函式之呼叫；W4 消費端 ＝ 生產碼 `34` 檔中
-           除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內；W5 畫面路徑之合成案（`自誤 517`：抽出 `main()`
+           除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內（🔧 `W-G.9-367`：許可另含 app.py 之 `f3_screen_adj4`／`adj4_plan`
+           與 harness 之 `run_adj4`〔規格步 4 乙之名單讀正面道路〕）；W5 畫面路徑之合成案（`自誤 517`：抽出 `main()`
            之一覽區塊與卡片說明句，以假 st 與合成資料實際執行）。另施四突變（刪推導之賦值、改 session 鍵、
            於 `verify/stepg_pipeline.py` 注入一消費者、一覽只出首列），每一突變須轉紅。
   run      <repo>
@@ -256,8 +257,11 @@ def _wiring_checks(app_src, others):
     res.append(("W3c main()：呼叫 r3_front_road_rows", rows_ok, ""))
     toks = R3_FUNCS + ["SS_FRONT_ROAD_DERIVE", "front_road_derive", "R3_FRONT_ROAD_MAJORITY"]
     tok_re = re.compile("|".join(re.escape(t) for t in toks))
+    # 🔧 `W-G.9-367`（發單側窗六十八）：harness 之 `run_adj4`（規格步 4 乙之 harness 入口）許可——除其原文而後計他檔之命中
+    others = {p: (_drop_fn367(s, "run_adj4") if p == "verify/selection_pipeline.py" else s) for p, s in others.items()}
     other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
     allowed = set(R3_FUNCS) | {"parse_cad_precision_layers", "main"}
+    allowed |= {"f3_screen_adj4", "adj4_plan"}   # 🔧 `W-G.9-367`（發單側窗六十八）：規格步 4 乙之畫面入口與受詞之純函式讀正面道路（名單之街廓屬性）
     bad = []
     for fname, node in top.items():
         if fname in allowed:
@@ -337,6 +341,16 @@ def _synth_screen(app_src, mn):
     return (not bad), f"不符 {bad}"
 
 
+def _drop_fn367(src, name):
+    """🔧 `W-G.9-367`（發單側窗六十八）：除去模組層函式 `name` 之原文（無之 ⇒ 原文不變）。"""
+    t = ast.parse(src)
+    ls = src.splitlines(keepends=True)
+    for n in t.body:
+        if isinstance(n, ast.FunctionDef) and n.name == name:
+            return "".join(ls[:n.lineno - 1] + ls[n.end_lineno:])
+    return src
+
+
 def _prod_others(repo):
     out = {}
     vd = os.path.join(repo, "verify")
````

## 附錄乙之二　塊 `F10p`（`git apply` 之差異·`verify/probes/probe_WG9351_intake.py`）

````diff
diff --git a/verify/probes/probe_WG9351_intake.py b/verify/probes/probe_WG9351_intake.py
index d0ab343..2030566 100644
--- a/verify/probes/probe_WG9351_intake.py
+++ b/verify/probes/probe_WG9351_intake.py
@@ -11,7 +11,8 @@
            AST 查接線：W1 模組層之常數與二函式、二函式內⛔ 案件字面；W2 入池閘之畫面入口於復原之後寫末趟之不配地紀錄、
            配地本體同生命週期去／寫末態 build；W3 二鍵 ∈ `K6B_SCREEN_TRIAL_KEYS` 且其末項仍為 `f3_k929_6_log`；
            W4 消費端 ＝ 生產碼 `34` 檔中除 `app.py` 外命中 `0`、`app.py` 中只在許可之函式內（🔧 `W-G.9-363`：許可之函式
-           另含 `f3_screen_k953`〔手冊先行之畫面試算讀入池閘之末態 build〕）；W5 畫面路徑之合成案
+           另含 `f3_screen_k953`〔手冊先行之畫面試算讀入池閘之末態 build〕；🔧 `W-G.9-367`：另含 app.py 之 `f3_screen_adj4`／`adj4_plan`
+           與 harness 之 `run_adj4`〔規格步 4 乙以 `adj_intake` 定其受詞〕）；W5 畫面路徑之合成案
            （`自誤 517`：抽出 `main()` 之盤點區塊，以假 st 與合成資料實際執行）。另施四突變，每一突變須轉紅。
   run      <repo> [<退縮> …]
            harness 實跑本案（預設退縮 `3.5`、`0.0` 二者）：以 `adj_intake` 盤點，並以本器**另寫之分類**（⛔ 呼叫
@@ -328,9 +329,12 @@ def _wiring_checks(app_src, others):
                 bool(keys) and all(k in keys for k in ADJ_KEYS) and keys[-1] == "f3_k929_6_log", ""))
     toks = ADJ_FUNCS + ["SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED"] + ADJ_KEYS
     tok_re = re.compile("|".join(re.escape(t) for t in toks))
+    # 🔧 `W-G.9-367`（發單側窗六十八）：harness 之 `run_adj4`（規格步 4 乙之 harness 入口）許可——除其原文而後計他檔之命中
+    others = {p: (_drop_fn367(s, "run_adj4") if p == "verify/selection_pipeline.py" else s) for p, s in others.items()}
     other_hits = {p: len(tok_re.findall(s)) for p, s in sorted(others.items()) if tok_re.search(s)}
     allowed = set(ADJ_FUNCS) | {"main", "f3_screen_stepg_run", "_k929_6_screen_gate"}
     allowed |= {"f3_screen_k953"}   # 🔧 `W-G.9-363`（發單側窗六十四）：手冊先行之畫面試算讀入池閘之末態 build（其單元）
+    allowed |= {"f3_screen_adj4", "adj4_plan"}   # 🔧 `W-G.9-367`（發單側窗六十八）：規格步 4 乙之畫面試算以 `adj_intake` 定其受詞（其受詞之純函式讀之）
     bad = []
     for fname, node in top.items():
         if fname in allowed:
@@ -345,6 +349,16 @@ def _wiring_checks(app_src, others):
     return res
 
 
+def _drop_fn367(src, name):
+    """🔧 `W-G.9-367`（發單側窗六十八）：除去模組層函式 `name` 之原文（無之 ⇒ 原文不變）。"""
+    t = ast.parse(src)
+    ls = src.splitlines(keepends=True)
+    for n in t.body:
+        if isinstance(n, ast.FunctionDef) and n.name == name:
+            return "".join(ls[:n.lineno - 1] + ls[n.end_lineno:])
+    return src
+
+
 def _prod_others(repo):
     out = {}
     vd = os.path.join(repo, "verify")
````

## 附錄乙之三　塊 `F14p`（`git apply` 之差異·`verify/probes/probe_WG9355_screenmerge.py`）

````diff
diff --git a/verify/probes/probe_WG9355_screenmerge.py b/verify/probes/probe_WG9355_screenmerge.py
index a782163..b96e233 100644
--- a/verify/probes/probe_WG9355_screenmerge.py
+++ b/verify/probes/probe_WG9355_screenmerge.py
@@ -243,6 +243,10 @@ def _rigged(ns, ss, cfg, env):
     saved = {k: ns[k] for k in STUBS}
     old_env = os.environ.get("WV_K6B_STAGE3")
     os.environ["WV_K6B_STAGE3"] = env
+    # 🔧 `W-G.9-367`（發單側窗六十八）：本器之樁世界⛔ 合調配之輸入（樁之 G 值列無推進側別）⇒ 規格步 4 乙於本器內 off
+    #   （其畫面入口之接線與停機另由 F24 量之）
+    old_a4 = os.environ.get("WV_ADJ4")
+    os.environ["WV_ADJ4"] = "off"
     ns["f3_screen_corner_pk_run"], ns["f3_screen_stepg_run"] = rig.pk, rig.g
     ns["k6b_stage3_run"], ns["end_block_merge_run"] = rig.s3, rig.merge
     try:
@@ -253,6 +257,10 @@ def _rigged(ns, ss, cfg, env):
             os.environ.pop("WV_K6B_STAGE3", None)
         else:
             os.environ["WV_K6B_STAGE3"] = old_env
+        if old_a4 is None:
+            os.environ.pop("WV_ADJ4", None)
+        else:
+            os.environ["WV_ADJ4"] = old_a4
 
 
 def _enter(ns, ss, pk, g):
````

## 附錄乙之四　塊 `F23p`（`git apply` 之差異·`verify/probes/probe_WG9363_k953.py`）

````diff
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index de0a7e0..c0bc21a 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -37,6 +37,8 @@
            harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 手冊先行之紀錄逐列 ＝ 本器所載；R2 街角第 1 宗之宗 ＝ 旗標 off 之
            實跑（街角定案·`v3` §8）；R3 配地之全部（各宗之街廓·推進側·G）與各街廓之抵費地 ＝ 本器所載（容差 `0.01`）且
            Σ抵費地之減 ＝ ΣG 之增（容差 `0.1`）；R4 調配之輸入之類（切片數·原有面積）＝ 本器所載、待同歸戶併入 ＝ 空。
+           🔧 `W-G.9-367`（⛔ 上列一字不刪）：本子命令於行程內設 `WV_ADJ4=off`（本器量手冊先行之果；規格步 4 乙之果
+           另由 F24 之 run 量之）。
   offsnap  <repo> <out.json> [<退縮> …]
            於行程內設 WV_K953=off，harness 實跑本案（預設退縮 `3.5`、`0.0`），以 sha256 摘要其街角、宗地（暫編地號·
            段三之三鍵·面積二欄）、build、段三紀錄、末端塊紀錄、配地列、入池閘紀錄、不配地紀錄、調配之輸入，寫 out。
@@ -1004,6 +1006,10 @@ KEEP_SP = ("run_end_block_merge", "run_corner_pk", "_k6b_callbacks", "k6b_stage3
 APP_ALLOW = {"K953_ENV", "k953_enabled", "k953_alloc_summary", "k953_units_of", FN, "f3_screen_k953",
              "f3_screen_k6b_stage3"}
 SP_ALLOW = {"run_k953", "run_corner_pk_k6b"}
+# 🔧 `W-G.9-367`（發單側窗六十八）：規格步 4 乙之新名亦許（本批之頂層之限另由 F24 之 W5 量之）
+APP_ALLOW |= {"ADJ4_ENV", "ADJ4_IDENT_UNUSED", "adj4_enabled", "adj4_possible", "adj4_subject_units", "adj4_subjects",
+              "adj4_depth_of", "adj4_trial_state", "adj4_plan", "adj4_pass1_run", "f3_screen_adj4"}
+SP_ALLOW |= {"run_adj4"}
 
 
 def _top_dump(tree):
@@ -1194,6 +1200,7 @@ def run(repo, sbs):
         print("  🔴 受詞缺")
         print("⇒ 紅 ['受詞缺']；rc 1")
         return 1
+    os.environ["WV_ADJ4"] = "off"   # 🔧 `W-G.9-367`（發單側窗六十八）：本器量手冊先行之果 ⇒ 規格步 4 乙於行程內 off
     red = []
     for sb in sbs:
         env = os.environ.get("WV_K953")
````

## 附錄乙之五　塊 `F4p`（`git apply` 之差異·`verify/probes/probe_WG9345_screen.py`）

````diff
diff --git a/verify/probes/probe_WG9345_screen.py b/verify/probes/probe_WG9345_screen.py
index e3c4b84..ce56266 100644
--- a/verify/probes/probe_WG9345_screen.py
+++ b/verify/probes/probe_WG9345_screen.py
@@ -26,6 +26,8 @@
            ⛔ 計入「session 之回復」之外洩；試算旗標 `SS_END_BLOCK_MODE` 仍計入（⛔ 外洩）。
            🔧 `W-G.9-363`（發單側窗六十四·⛔ 上列一字不刪）：on／s3off 另驗手冊先行之紀錄（`f3_k953_log`）與 harness
            逐列同；其鍵係畫面入口之正當輸出，⛔ 計入外洩。
+           🔧 `W-G.9-367`（發單側窗六十八·⛔ 上列一字不刪）：on／s3off 另驗規格步 4 乙之第一趟之紀錄（`f3_adj4_log`）
+           與 harness 逐列同；其鍵係畫面入口之正當輸出，⛔ 計入外洩。
            配地列以暫編地號對齊；一側獨有之列須「幾何面積 0 且 G 0」（零面積池列·逐一出艙為 Z），餘須全等；
            cut_coords 以環（去閉合點·容旋轉與反向）比對。--perturb：將畫面側之 B 值乘 1.0001（必紅造）。
   wiring   <repo>
@@ -560,6 +562,12 @@ def cmd_parity(repo, sb, mode, out=None, perturb=False):
         bad += (not ok)
         say(f"  {'✅' if ok else '🔴'} 手冊先行 session 鍵 f3_k953_log（{len(REF.get('f3_k953_log') or [])} 列）")
         EBM = EBM + ("f3_k953_log",)
+        # 🔧 `W-G.9-367`（發單側窗六十八·⛔ 上列一字不刪）：規格步 4 乙之第一趟（`K-9-53` ②）之紀錄係畫面入口之正當
+        #   輸出——與 harness 同（逐列）、⛔ 計入「session 之回復」之外洩
+        ok = _same(REF.get("f3_adj4_log", "<缺>"), ssS_pk.get("f3_adj4_log", "<缺>"))
+        bad += (not ok)
+        say(f"  {'✅' if ok else '🔴'} 第一趟 session 鍵 f3_adj4_log（{len(REF.get('f3_adj4_log') or [])} 列）")
+        EBM = EBM + ("f3_adj4_log",)
         idsH = [(t["暫編地號"], t.get("段三併出")) for t in tH]
         idsS = [(t["暫編地號"], t.get("段三併出")) for t in tS2]
         ok = idsH == idsS
````

## 附錄丙　塊 `K10`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-56` 之立；規格步 `4` 乙（第一趟）之工程讀法；入側支（`W-G.9-367`·⛔ 上文一字不刪·純末端追加）

### 🔒 `K-9-56`　**規格步 `4` 乙（第一趟·`K-9-53` ②）：合併單位之土地整體併入不過「不影響原位次」之檢核者，可拆分；同一合併單位之道路片一起併；兩側都沒有已配地之道路片，可以併到該地主在別的街廓已配到的土地（可拆分，以因應調配池需合格的機制）——改 `2026-10-03` 之裁之意思**（KL 裁 `2026-10-04`·canonical）

**編號之由**（`W-G.9-367 §零-1`）：`K-9-56` 於開工態 `d7a5ea4` 之錨定框 `2` 列（`docs/orders/W-G.9-342_輕量單.md:30` 之「對照乙［必為零］」所列之未取號，與 `docs/orders/W-G.9-361_補令一.md:32` 之引之）·⛔ 占用 ⇒ 取之；`K-9-44`／`K-9-47` 仍為缺號。
**出處**：發單側窗六十八（`2026-10-04`）擬 `W-G.9-367` 之前所呈二問與【通知】三則；其呈文之逐字⛔ 存於倉內外可稽之檔（`自誤 579`）。

**發單側所呈之要旨**（⛔ 充逐字）：
- **問1**：合併單位之土地整體併入名單上第一個有其已配得之宗之街廓之宗，而「不影響原位次」之檢核不過（例：剩下之調配池不合格）時——**甲** 拆分：逐片（建地整筆、道路與公設地上之土地取最大面積），剩下者續沿名單；**乙** ⛔ 拆分：整體改試名單之下一街廓。
- **問2**：同一合併單位中之道路片——**甲** 與該單位之他片一起併入同一受併宗；**乙** 另依手冊之道路之則（依中心線切分）。
- **【通知】三則**（KL 未駁）：① 受併宗 ＝ 該街廓中其已配得之宗之一，依「同原地號 → 距錨點近 → 應分配面積大 → 暫編地號」之序（KL `2026-07-11` 之四層瀑布之推及）；② 每次併入皆受「不影響原位次」之檢核（`K-9-48` 其三）；③ 非位於受併宗之街廓之土地先折算 `a′` 再計 `G`（`K-9-45`（二））。

**KL 之答（`2026-10-04`·逐字）**：

> 1. 問1：甲 2. 問2：甲，一起併，改10/3裁的意思，兩側都沒有已配地的道路片，可以併到該地主在別的街廓已配到的土地(可拆分，以因應調配池需合格的機制)

**裁之內容**：
① 第一趟之整體併入不過檢核者**可拆分**（問1 甲）：逐片併入同一受併宗——建地整筆、道路與公設地上之土地取最大面積；剩下者續沿名單之下一個有其已配得之宗之街廓。
② 同一合併單位之道路片與他片**一起併**（問2 甲）。
③ **兩側都沒有已配地之道路片**（`K-9-53` 同訊之【通知】①·`K-9-55` 同訊之【通知】一）：**可以併到該地主在別的街廓已配到的土地**（可拆分）——改 `2026-10-03` 之裁之意思（下開「與既有正典之關係」）。
④ 【通知】三則如上。

**與既有正典之關係**：
- 本典「`K-9-53` ① 之工程讀法；手冊先行入側支」節之乙之「二側皆無 ⇒ 視同無同歸戶（【通知】①）：其片⛔ 併入他街廓之已配得之宗（【通知】① 之「單獨」），入合併單位」與「`K-9-55` 之立」節之「同訊（逐字）：「1. 通知一：OK」」之讀法（先前所稱「單獨進調配池」＝「不併到他在別的街廓已配到的土地」）——**由 ③ 改之**：其片於手冊先行仍⛔ 併（手冊之道路之則無側可併·入合併單位），於第一趟隨其合併單位沿名單併入該地主於他街廓之已配得之宗（可拆分）。⛔ 改二節之原文。
- `K-9-53` ②（併不進去者與其他分不到之土地合併、沿名單調配）——本裁定其第一趟之作法；`K-9-45`（`G(a1＋a2′＋…)`·可拆分）、`K-9-46`、`K-9-52`（名單）、`K-9-48` 其三（檢核）與七項 `3`（最大面積）——依本裁施於第一趟。

**射程**：及於**任一案件**。⛔ 及於：地主無任何已配得之宗之合併單位（規格步 `5`）。

**本案之量**（harness·發單側窗六十八之原型·`W-G.9-367 §一` 項 `6`）：二退縮之受詞唯 `G001`（公設軌·其片唯道路片 `628-3(1)`〔`13.15 ㎡`·兩側皆無已配地〕）⇒ 整體併入其 `R3` 之 `628-34(2)`（`250.24 → 257.91`）；`R3` 之抵費地 `1659.06 → 1651.41`（`3.5 m`）／`1659.05 → 1651.41`（`0 m`）；合併單位 `18 → 17`；第一趟之紀錄 `1` 列。

**規格步 `4` 乙（第一趟）之工程讀法**（發單側窗六十八·`2026-10-04`·【工】·⛔ 充裁·其要旨以【通知】呈 KL）——其碼側落地（`W-G.9-367`·`app.py` 之 `adj4_pass1_run`〔單一真相源〕與 `adj4_plan`〔受詞與名單〕·harness `verify/selection_pipeline.py` 之 `run_adj4`·畫面 `f3_screen_adj4`·旗標 `WV_ADJ4`）所取：
- **甲 受詞**：調配之輸入（以第一趟之前之試算求之）之合併單位中，地主另有已配得之宗者（`同歸戶原位次配地之街廓` 非空）；其片 ＝ 該單位之建築街廓內不能分配與共同負擔用地；道路片、公設片帶 `段三餘量` 者，其可併之量 ＝ 其餘量。
- **乙 名單**：規格步 `3` 之候選街廓名單（`K-9-52`）；第一趟之前求一次（⛔ 隨併入重算）；唯公設軌之受詞者⛔ 須正面道路之名。
- **丙 受詞之序**：建地軌先 → 原有面積合計大者先 → 歸戶。
- **丁 街廓之取**：沿名單至第一個有其已配得之宗（當下之試算）之街廓。
- **戊 受併宗**：（同原地號 → 錨點至其成員之原形之聯集之質心之距〔`0.01 m`〕→ 應分配面積大 → 暫編地號）之首（【通知】①）。
- **己 整體**：全部之片（`a′` 折算）一次併入；檢核（`T` ＝ 該街廓 ∪ 建地片之所屬街廓、`R` ＝ 建地片）過 ⇒ 成、止。
- **庚 逐片**（①）：建地 → 道路 → 公設地（同類剩下大者先）；建地整筆、道路與公設地取最大面積（`0.01 ㎡` 之來源面積之格·視為單調而二分）；剩下續沿名單。
- **辛 都不行**：留於合併單位（規格步 `5`）。
- **壬 幾何之來源**（`GB-199`）：錨點與受併宗之成員之形 ＝ 重劃前之切片之原形（段三之前之宗地）。
- **癸 三鍵**：沿用段三之三鍵（既有之鍵與第一趟之併入合之）；下游一字不改。
- **子 街角定案**：同手冊先行（⛔ 重跑街角選位）。
- **丑 停機**：建地片於當下之試算已為已配得之宗或其成員；現態或前態之配地中止；受詞之片之原形缺、非 temp 之片、殘料；名單缺或重複；面積或折算無從定之。
- **寅 旗標與先篩**：`WV_ADJ4` ＝ `off`，或 `WV_K953`、`WV_K929_6` ＝ `off` ⇒ 第一趟不辦（三旗標皆判·非法之值 ⇒ 停機）；無「為 build 之某宗之歸戶、且 temp 中其片 `≥ 2`」之歸戶 ⇒ ⛔ 試算、逕回（受詞之必要條件·`adj4_possible`）。
- **卯 手冊先行之 `GB-201` 之防護**：計畫之受併宗於當下之試算未保留 ⇒ 停機（逐片之整筆之主併入、可拆分之片之最大面積之試之前）。
🔒 **本案無其形者**（⛔ 另立停機款·其去處由名單之序與檢核定之）：`K-9-55` 之理之推及（同街廓、⛔ 相鄰而未碰他街廓之分不到之建地）；`W-G.9-363` 補令四全掃 ⑦（隔道路之建地片先依道路片之計畫併往另一側，而道路片其後未全併者）。

**落地狀態**：🔶 側支 `verify/W-G.9-367-adj4`（工項二）；主線之推進候 KL 逐字放行（`W-G.9-367 §四-2`）。
````

## 附錄丁　塊 `G9`（附於 `docs/reports/W-G.4_泛用阻塞項登記表.md` 之末）

````markdown

---

## 🔧 `GB-199`／`GB-201` 之進度（`W-G.9-367`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-367-adj4`（起於主線 `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`）；主線⛔ 變。本節⛔ 鑄號。

### `GB-199` 之進度（`W-G.9-367`）

規格步 `4` 乙（第一趟·`K-9-53` ②·`K-9-56`）明定其所讀之幾何之來源：錨點與受併宗之成員之形 ＝ **重劃前之切片之原形**（段三之前之宗地：harness ＝ `run_corner_pk_k6b` 之輸入 `temp_parcels`；畫面 ＝ `f3_screen_k6b_stage3` 之 `temp0`；`adj4_pass1_run` 之引數 `slice_geom`），⛔ 讀段三後之 temp 之形（入池閘之單元帶佔位成員之形）。量測器 `F24` 之 `K12`：temp 之形異於原形時，受併宗之序依原形；原形缺 ⇒ 停機。本案之受詞（`G001` 之 `628-3(1)`）之受併宗之成員⛔ 含佔位 ≠ 標的之單元 ⇒ 二來源之量同。
**態**：🔶 側支（失效條件之「明定單元之幾何之來源並入主線」之前半已成）；其入主線時解除。公設地調配之瀑布（`verify/wf_f3.py`·W-F 凍存）與畫面之舊「自動計算公設分配」之讀者⛔ 在本批之射程（其登記之「與配地之關係」⛔ 變）。

### `GB-201` 之進度（`W-G.9-367`）

手冊先行（`k953_manual_run`）於逐片之整筆之主併入（`R-9⁗` ③ 之查之後）與可拆分之片之最大面積之試（來源量 `> 0` 時·含其 `K-9-51` 之可拆分者）之前，以當下之試算查計畫之受併宗仍為已配得——⛔ 者停機（訊息含 `GB-201`·`W-G.9-367` `R-16`·唯增列）。量測器 `F24` 之 `K15`：甲 可拆分之片（道路片之計畫含他街廓之宗而該宗於整筆之建地片併入後⛔ 保留）、乙 整筆之建地片（其計畫之受併宗於前一片併入後⛔ 保留）⇒ 皆停機；開工態之碼（`d7a5ea4`）於同二形皆靜默併入（發單側窗六十八實跑）。本案⛔ 觸（手冊先行之整批皆過）。
**態**：🔶 側支（失效條件之「之式落地」已成）；其入主線時解除。
````

## 附錄戊　塊 `E11`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末）

````markdown

---

**取號**（`W-G.9-367 §零-1`）：本批取 `578`〜`579`（`2` 號）——發單側窗六十八擬 `W-G.9-367` 時自察之二則。

### 🩸 `自誤 578`　**`W-G.9-366` 單 `§五-1` 末之抽取式唯列 `python`／`diff`／`markdown` 三種圍欄開列，而其工項二令自 `W-G.9-365` 單取塊 `CK`／`GF`——該單另含 `json` 之開列 ⇒ 依「圍欄之逐列索引」數之，其序數⛔ 定**

**形**：自他單取塊之令，⛔ 查他單之圍欄之形；本單之抽取式之字面⛔ 涵蓋之。CC 以「開列之列號」（`:807`／`:755`）直接指名附錄午／巳之圍欄而自解（`docs/reports/W-G.9-366R_開工自動對齊_執行報告.md` ⑥ 自解 `2`）。
**後果之界**：零（塊之 bytes／`sha256` 與單所載相符·倉外檔）。
**根因**：抽取式以本單之圍欄之形為前提，未及「自他單取塊」之情形。
**後果之框**：🟡 CC 自解一處。攔點 ＝ CC（`W-G.9-366R` ⑥ 自解 `2`）。
**攔法**：`W-G.9-367 §五-1` 末之抽取式（圍欄開列之語言名不拘；自他單取塊者以該單之附錄之標題列之後之第一個圍欄開列為準）。通則：凡令自他單取塊，抽取式須及他單之圍欄之全部形，並以附錄之標題定位、⛔ 以全檔之序數。

---

### 🩸 `自誤 579`　**發單側窗六十八呈 KL 之二問與【通知】三則（`K-9-56` 之所答）之呈文，發出時⛔ 存於倉內外可稽之檔；本窗之 context 壓縮後其逐字已不可得 ⇒ `K-9-56` 之入典唯載其要旨**

**形**：同 `K-9-53` 之「同訊之【現況】【要改成】【對土地的影響】之逐字⛔ 存」之形之再見。KL 之答之逐字存（KL 之訊），其所答之問之逐字⛔ 存 ⇒ 正典之「發單側所呈（逐字）」一欄缺。
**後果之界**：零土地後果（KL 之答之逐字與其讀法皆入典；讀法另以【通知】呈 KL）；正典之可稽性之減一則。
**根因**：呈 KL 之問於發出時未同存於倉外之檔（交接文或其附件），而入典在後。
**後果之框**：🟡 正典一則之問之逐字缺。攔點 ＝ 發單側窗六十八（擬 `W-G.9-367` 之塊 `K10` 時）。
**攔法**：`K-6` 典 `K-9-56` 之「發單側所呈之要旨（⛔ 充逐字）」。通則：呈 KL 之【要你判斷】，發出時即以其全文存於倉外之檔（附於其後之交接文），入典時逐字取之。
````

## 附錄己　塊 `P21`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：規格步 `4` 乙（第一趟·`K-9-53` ②·`K-9-56`）入側支；手冊先行之 `GB-201` 之防護（`W-G.9-367`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-367-adj4`（本批新立·起於主線 `d7a5ea4a36477d3867de181a9ca59ad714eeaeda`）；主線⛔ 動。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-53` ② ＋ `K-9-56`（規格步 `4` 乙·第一趟） | 合併單位之地主另有已配得之宗者，沿其候選街廓名單至第一個有其已配得之宗之街廓，整體併入其宗之一（`a′` 折算）；不過 ⇒ 逐片（建地整筆、道路與公設地取最大面積）、剩下續沿名單；都不行 ⇒ 留於合併單位。`adj4_pass1_run`（單一真相源）·`adj4_plan`·harness `run_adj4`·畫面 `f3_screen_adj4`·旗標 `WV_ADJ4`；量測器 `F24`（`verify/probes/probe_WG9367_adj4.py`） | 🔶（側支·harness 與畫面二路徑皆入；入主線另候 KL 放行） | `docs/orders/W-G.9-367_規格單.md` |
| `2` | `GB-201`（手冊先行之計畫之受併宗於當下之試算未保留） | `k953_manual_run` 之二施點之前查之、⛔ 者停機 | 🔶（同上） | 同上；`GB` 簿 `GB-201` 之進度 |
| `3` | `GB-199`（段三後之 temp 中入池閘之單元之形） | 第一趟之幾何之來源 ＝ 重劃前之切片之原形 | 🔶（同上） | 同上；`GB` 簿 `GB-199` 之進度 |
| `4` | 序 `1`／`2` 之以程式字樣為錨之接線與突變之判別力（復驗時補寫）＋ 入主線 ＋ 主 checkout 之同步 | — | ⬜（候 KL 放行） | 次單 |
| `5` | 規格步 `5`（地主無已配得之宗之合併單位之調配：末端塊與中間調配池之進入與落位·`K-9-38`〜`40`） | 前置：`K-9-38` 射程 ④、`K-9-40` 射程 ④ 之附圖另呈 | ⬜ | 規格步 `5` |
| `6` | 規格步 `6`（½ 之判與出口）／`7`／`8`（終態與出艙） | — | ⬜ | 規格步 `6`〜`8` |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：規格步 `4` 甲（`K-9-53` ①·手冊先行）入主線；`k*` 經驗錨之重錨；`GB-201` 之立」節序 `2`（`K-9-53` ②）、序 `7`（`GB-199`）、序 `9`（`GB-201`）⇒ 🔶（本表序 `1`〜`3`）；其序 `4`（手冊先行之接線與突變之判別力之餘）之態⛔ 變（🔶·其餘之補寫併本表序 `4` 之單）；其序 `5`（`GB-198`）、序 `8`（`GB-200`）之態⛔ 變。
🔒 **本案之量**（harness·發單側窗六十八之原型）：二退縮之受詞唯 `G001`（公設軌·道路片 `628-3(1)`·`13.15 ㎡`·兩側皆無已配地）⇒ 整體併入 `R3` 之 `628-34(2)`（`250.24 → 257.91`）；`R3` 之抵費地減 `7.65`／`7.64 ㎡`；合併單位 `18 → 17`；他街廓之配地⛔ 變。
🔒 **依賴序**：本批（側支）→ 序 `4`（次單·零生產碼之補寫 ＋ 入主線之請示）→ 規格步 `5` → `6` → `7`／`8`；`GB-196`、`GB-197`、`GB-198` 另單（⛔ 急）；`GB-194`、`GB-200` 之停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ `W-G.9-357` 節序 `7` ＋ `W-G.9-360` 節序 `5`）。
🔒 **本機介面**：主線⛔ 變 ⇒ 本機介面⛔ 變。入主線並同步後，執行介面之環境 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6`／`WV_K953`／`WV_ADJ4` 皆須**未設**（設 `off` 之 `WV_ADJ4`、`WV_K953` 或 `WV_K929_6` ⇒ 第一趟不辦）；按「街角地優先權選位」之該趟，「📒 手冊先行」之紀錄之下另示「🧭 規格步 4 乙（第一趟·K-9-53 ②）」之紀錄。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `7`（子字串框·含圖例與本列）·列 ＝ `5`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄庚　塊 `IX2`（`git apply` 之差異·`.claude/rules/常設規則索引.md`）

````diff
diff --git "a/.claude/rules/\345\270\270\350\250\255\350\246\217\345\211\207\347\264\242\345\274\225.md" "b/.claude/rules/\345\270\270\350\250\255\350\246\217\345\211\207\347\264\242\345\274\225.md"
index dacddda..a18e96d 100644
--- "a/.claude/rules/\345\270\270\350\250\255\350\246\217\345\211\207\347\264\242\345\274\225.md"
+++ "b/.claude/rules/\345\270\270\350\250\255\350\246\217\345\211\207\347\264\242\345\274\225.md"
@@ -113,7 +113,7 @@
 - core.autocrlf 不得逕引；須當場分層（system／global／local）現查。KL 本機倉 local＝false；拋棄式 clone 未設 local 會繼承 system 之 true，工作區即為 CRLF。〔`core.autocrlf` 之**記述更正**〕
 - heredoc：Bash 命令不得含 `<<`（PreToolUse hook verify/tools/wg9237_heredoc_guard.py 阻斷）；腳本一律以 Write 工具落檔再以路徑執行；hook 僅在 session 之專案目錄含 .claude/settings.json 與該腳本時生效。〔外：docs/reports/W-G.4_泛用阻塞項登記表.md「之補款：**硬閘化**」「補款之補款三」〕
 - GB-198（⬜ 未修）：numpy ≥ 2.5 之 np.cross 拒收二維向量 ⇒ harness（verify/stepg_pipeline.py）中止；requirements.txt 無上界；登記之實跑以 numpy 2.4.6 為之；失效條件＝設上界 < 2.5 或改明式二維叉積。〔W-G.9-364`·〕〔外：docs/reports/W-G.4_泛用阻塞項登記表.md「### `GB-198` 🆕」〕
-- 畫面執行環境之 WV_K6_STEP0／WV_K6B_STAGE3／WV_K929_6 須未設（設之即回舊行為）；主 checkout 同步後須重啟介面。〔W-G.9-358`·〕
+- 畫面執行環境之 WV_K6_STEP0／WV_K6B_STAGE3／WV_K929_6／WV_K953／WV_ADJ4 須未設（設之即回舊行為）；主 checkout 同步後須重啟介面。〔W-G.9-358`·〕〔W-G.9-367`·〕
 - 生產與驗證讀同一份圖資，現行為 data/V6_1.dxf；data/V6.dxf 僅供溯源，不刪不覆蓋。〔外：docs/rulings/K-6_街角地分配程序與可分配判準.md「### 🔒 K-9-20　」〕
 - 開工自動對齊：KL 本機之使用者設定掛有 SessionStart hook（主 checkout 之 verify/tools/wg9366_session_sync.py）。桌面版新建之 `claude/` 工作區若乾淨而落後主線，開工時自動快轉至 `origin/wip/s1-endpart` 並出通知；見其通知者，先以 Read 讀本索引之最新版。此器依主 checkout 為最新，故各單收尾之主 checkout 同步不可省。〔開工自動對齊〕
 ## 十二、讀起來像現行、其實已被取代（讀全文時注意）
````

SELF_SHA256: ad490fd2ee80ff3edea3d008bebcbe93bc20620247af5a311d6aadb7e83a87e7
