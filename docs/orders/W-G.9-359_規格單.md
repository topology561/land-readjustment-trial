# `W-G.9-359`　規格單：調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）＋ 正面道路只限「道路」類 ＋ 驗證路徑之區外道路名稱（新側支 `verify/W-G.9-359-cand`）＋ `K-9-52` 之入典 ＋ 待落地清單之更新

> **本單建議等級 ＝ `xhigh`**（本單令 CC 依規格撰寫生產碼·規格單流程之常態首張）。
> **發單** ＝ 發單側窗五十六·`2026-09-29`。**受單** ＝ CC 新窗（工項零〜四於 **CC 之施工樹**·**一切 `commit` 推至新側支 `verify/W-G.9-359-cand`**，其起點 ＝ 主線之端 `1841914`）。
> **流程 ＝ 規格單**（常態·`docs/reports/W-G.9波_恆常附款登記表.md`「恆常附款 `n③` 之試行期變通之期滿與續行（`W-G.9-358`）」節 ③·附則甲〜丙施行·`§二`）：**生產碼由 CC 依 `§三` 撰寫**；發單側給規格（`§三`）、量測器（塊 `F18`·CC ⛔ 改一字）、資料檔（塊 `J1`）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py`／`verify/run_verification.py` 之 blob（由 CC 回報、發單側復驗時自倉重算）。
> **級** ＝ **重**（生產碼 `2` 檔：`app.py`、`verify/run_verification.py`；新資料檔 `1`：`verify/case_front_road_names_UC9898.json`；土地後果：**本案⛔**——正面道路之推導不變〔候選皆「道路」類·`§一` 項 `6`〕，候選街廓名單**僅顯示**、⛔ 消費端；**他案有**——正面線沿公園、廣場等非道路之公共設施街廓者，由「以之為正面道路」改為區外待填〔`K-9-52` ①〕；名單之消費候規格步 `4`〜`6`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`（`W-G.9-358` 工項三）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-359-cand`（工項零立之·其後皆快轉）；主線⛔ 動**。
> 🔑 本單之一切呼叫形，其直譯器名一律寫 `python`（`自誤 466`）。塊 `F18`／`J1`／`K5`／`P13`／`V1` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）；`commit` 訊息一律 `git commit -F`（`恆常附款 h`）。含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8。**Windows 下 `<repo>` 及一切路徑引數一律以反斜線之絕對路徑傳入**（`W-G.9-333R` ⑦-1·`自誤 479`）。
> 🔑 **來源檔**（檔名逐字 `W-G.9-359_規格單.md`·本單）：取之序 ＝ CC 施工樹之根 → KL 主 checkout 之根 → KL 主 checkout 之 `docs/orders/`（未追蹤者）；三處皆無 ⇒ 停機款 `2`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`（先以 `python -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6')])"` 出艙 `[None, None, None]`）。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 與 `verify/run_verification.py` 以外之生產碼一字（生產碼 `34` 檔之其餘 `32` 檔）；`§三-3` 之禁改；W-F（`verify/wf_f0.py`〜`wf_f4.py`）與 W-D.4 之任何錨；`verify/case_params_UC9898.json`；`verify/baselines`；`verify/out/` 之二凍存名單；`VR` 簿、`GB` 簿、自誤簿、恆常附款登記表之一字；`K-6` 典、`CLAUDE.md`、`docs/配地計算總規格_v3.md` 除塊 `K5`／`P13`／`V1` 之純末端追加外之一字；既有量測器之一字；任何既有側支之推送、刪除或改寫；KL 主 checkout。
> 🔴 **本單⛔ 令 CC 作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`；`git ls-remote --heads origin` 之列數 ＝ `32`，且⛔ 含 `refs/heads/verify/W-G.9-359-cand`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 550 549` ⇒ `rc 0`。
4. 本單之 bytes／`sha256` 對拍 `§五-1`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。

### `§零-1`　取號現查（宣告框）

器 ＝ `verify/probes/wg9268_gate6_occupancy.py`；母體 ＝ 開工態之 `docs/` 全檔（**`922`** 檔·器之出艙「讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`」）。發單側窗五十六實跑（皆 `rc 0`）：

| 受詞 | 嚴格 `D1`／`D2`／`D3` | 寬式 `D1`／`D2`／`D3` | 列框 | 檔框 | 鬆框 檔／列 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-359`（本單之號）｜`python verify/probes/wg9268_gate6_occupancy.py 1841914 W-G.9-359 W-G.9-358 W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `2`／`4` | 🟢 可取（鬆框 `4` 列 ＝ `docs/orders/W-G.9-358_輕量單.md:104`／`:893`／`:942` 與 `docs/reports/W-G.9波_恆常附款登記表.md:624` 之「自 `W-G.9-359` 起」——規格單流程常態之始點之**前引**·⛔ 占用） |
| 對照甲［必非零］`W-G.9-358` | `2`／`6`／`5` | `2`／`6`／`5` | `11` | `3` | `4`／`33` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`W-G.9-396` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `6`／`9` | 🟢 宣告框 `0`、鬆框非零（漏框偵察有咬） |
| `K-9-52`（本批所鑄之裁號）｜`python verify/probes/wg9268_gate6_occupancy.py 1841914 K-9-52 K-9-51 K-9-93` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `0`／`0` | 🟢 可取 |
| 對照甲［必非零］`K-9-51` | `1`／`11`／`0` | `1`／`11`／`2` | `11`（寬式 `13`） | `5` | `9`／`75` | 🟢 框非恆空 |
| 對照甲′［鬆框之漏框偵察］`K-9-93` | `0`／`0`／`0` | `0`／`0`／`0` | `0` | `0` | `1`／`2` | 🟢 宣告框 `0`、鬆框非零 |
| 對照乙［器內人造·須全 `0`］`W-G.9-963` | `0`／`0`／`0` | `0`／`0`／`2` | `0`（寬式 `2`） | `0`（寬式 `1`） | `20`／`23` | 🟡 寬式 `D3` ＝ `2`：同 `docs/orders/W-G.9-357_規格單.md` `§零-1` 所載之具名豁免（報告內嵌本器之出艙）·受詢之判⛔ 受影響 |

本批⛔ 鑄自誤／`GB`／`VR`；`K-9` `MAX` ＝ `51` ⇒ 取 `K-9-52`（塊 `K5`）。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `1841914`，或遠端 heads ≠ `32`，或遠端已有 `verify/W-G.9-359-cand`，或施工樹之追蹤檔有變動 |
| `2` | 本單之 bytes／`sha256` 與 `§五-1` 不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `F18`／`J1`／`K5`／`P13`／`V1` 任一之 bytes／`sha256` 與 `§五-1` 不符；或寫出後之 blob ≠ `§五-1` 項 `7` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或 CC 須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-7` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變**（`V-2`〜`V-5` 任一相異） |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-359-cand`；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之三檔任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | CC 作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過 |
| `11` | 本批任一新檔為 `git check-ignore` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer（附則丙）之發現涉域上判斷或規格之漏載 |

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單側實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單側窗五十六自倉實跑·本機 Linux·倉外工作樹·殼無 `WV_`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／側支／refs | 主線 `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`；側支 `verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f`、`verify/W-G.9-343-k929b` ＝ `14e022265bd1c190d7d6f9c1a0c6900bcec120db`、`verify/W-G.9-341-gb182` ＝ `d0add71ff85e62c2afb1f2f5d327c4488624c4a1`、`verify/W-G.9-338-origin` ＝ `2ec1eb2bf43616ce662d95dc633b4c71f366eb15`、`verify/W-G.9-333-gb168` ＝ `be5108d0067e63e23a397fdcbe43358800381470`；凍存 `verify/W-G.9-299-gb170` ＝ `488c4858da63ebe370ed950788947aa742eb44ad`；遠端 heads **`32`**（`verify/` `27`·`wip/` `3`·`claude/` `1`·`main` `1`）；`verify/W-G.9-359-cand` ⛔ 存 |
| `2` | 生產碼與三簿（開工態 blob） | `app.py` `d8938792ab09e71636dc6916b61432c522c847e5`（`1617196` B）；`verify/run_verification.py` `4d83d2c5a32c364021f26679a58172e1f1554dab`（`101887` B）；`verify/selection_pipeline.py` `8d38e55013bec51ab81978336fe04e928f5baf98`；`verify/stepg_pipeline.py` `ca56b5c4cfc5b7fb8a0838061e775c6ac54f8dac`；`K-6` 典 `435812` B；`CLAUDE.md` `308508` B；`docs/配地計算總規格_v3.md` `65433` B（皆以換行結尾·CR `0`） |
| `3` | `W-G.9-358` 之復驗（發單側窗五十六·依交接文五十五 `§四-1`·全數自倉重跑） | 四 `commit`（`0afa6a8`／`a36f766`／`9fca83c`／`1841914`）線性、各訊息首段逐字 ＝ 單所令；主線之祖含 `4716f20`；單 ＝ `b0770965…`（`90856` B·`SELF_SHA256` 經 `P-5` 自驗相符·pre-flight 🔴 `0`／🟡 `4` 同單 `§五-1` 項 `9`）；六塊之 bytes／`sha256` 逐格相符；`F17` blob ＝ `75563128…`；三簿 `1080872`／`308508`／`65928` 皆嚴格前綴、所增 ＝ 塊 `E6`／`P12`／`H2` 逐位；工項一二態之出艙與塊 `T1`／`T2` **逐位同**；收工閘 `1`〜`9` 自倉重跑皆符（閘 `7` 四簿 ＝ 自誤 `535`／`550`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `48`／`51`／`[44, 47]`）；報告 ⑥ 載 KL 貼單之訊息逐字（檔路徑一列 ＋「是」）——**全數相符** |
| `4` | 本批之受詞 | `docs/specs/調配階段_泛用規格_v1.md` 步 `3`（候選街廓名單）；`docs/配地計算總規格_v3.md` 五級③（八鍵詞典序·KL `2026-09-05`）；`K-9-1` ⑨（最小建築面積之級）；`K-9-46`（原街廓·增配之比較⛔ 設容差）；`K-9-52`（本批入典·`§二`）；`CLAUDE.md` 諸「待落地清單之更新」節之規格步 `3` 與其三前置（`W-G.9-350` 節序 `3`／`4`·`W-G.9-351` 節序 `3`） |
| `5` | 現碼之行為（開工態） | ① 正面道路之推導之候選 ＝ 一切非可建築土地之街廓（`parse_cad_precision_layers` 之 `r3_front_road_derive` 之第二引數·⛔ 分類別）；② 候選街廓名單⛔ 存（`adj_*` 唯 `adj_intake`／`adj_intake_rows`）；③ harness 無區外道路名稱之來源（`R1`／`R4` 之識別符 ＝ `None`）——皆由塊 `F18` 之三子命令證之（`§一` 項 `7`） |
| `6` | 本案（harness·開工態） | 可建築街廓 `6`（`R1`〜`R6`·皆住宅區）、非可建築 `5`（`RD1`〜`RD4` 道路、`G1` 鄰里公園）；正面道路之推導：`R2` ＝ `RD1`、`R3`／`R5` ＝ `RD2`、`R6` ＝ `RD3`、`R1`／`R4` ＝ 區外（`W-G.9-350 §一` 項 `5` 之表）——其候選皆「道路」類（`G1` 與任一正面線之重疊皆 `0`）⇒ `K-9-52` ① ⛔ 變之；正面路寬 `R1`／`R4` ＝ `12 m`、餘 ＝ `8 m`（二種）；深度（N-19′）`R1` `33.15`、`R2` `44.47`、`R3` `44.34`、`R4` `33.11`、`R5` `45.71`、`R6` `45.51`；合併單位：退縮 `3.5` ⇒ `23`（建地軌 `15`·公設軌 `8`）、`0.0` ⇒ `24`（`16`·`8`） |
| `7` | 量測器於工項一之端（`1841914` ＋ 塊 `F18`·發單側實跑） | `F18 selftest` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`F18 wiring` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']；rc 1`；`F18 run` ⇒ **`rc 1`**，末列逐字 `⇒ 紅 ['受詞缺']；rc 1` |
| `8` | 發單側之原型（**⛔ 交付**·僅為量測器之必過之實例） | 發單側於倉外拋棄式工作樹依 `§三` 撰一原型（`app.py` 與 `verify/run_verification.py`·⛔ 入倉·其 blob ⛔ 為本單之期），於其上：`F18 selftest` ⇒ `rc 0`（`C1`〜`C18`〔`22` 例〕皆 ✅·`P0` `22／22`）、`F18 wiring` ⇒ `rc 0`（`W1`〜`W6` 皆 ✅）、`F18 run` ⇒ `rc 0`（二退縮 `R0`〜`R5` 皆 ✅）；另以程式字樣為錨施十三突變（同深改嚴格小於／較寬者⛔ 排最後／最小建築面積之級反向／原街廓⛔ 居首／正面道路⛔ 比／較深與較淺同組／錨點取最小／迄點取最小之抵費地／偶數捨入／往大者⛔ 標第二趟排除／廣場得為正面道路／公設軌依街廓名／深度差⛔ 取二位），各使 `selftest` 之所指之例轉紅（⛔ 入 `F18`·`§四-2`）；`§四-3` 閘 `8`〜`24` 之諸器皆 ＝ 其期 （`k6s3 cmp` 二退縮相異 `0` 項；`F8 run` 二退縮與 `F9 run` 之出艙對開工態 `diff` 皆空；`parity` `3.5` ⇒ 配地列 `35`／`34`、`0.0` ⇒ `36`／`35`·不符格 `0`·`Z` ＝ `[('harness', 'R1-抵費地-2')]`；`run_all` 同一倉外路徑之出艙對開工態**逐位同**〔`235960` B·相異項 `0`〕；`F9`〜`F17` 之 `selftest`／`wiring`／`run`、`wfns_ast` `48`／`48`／`47`、`main_synth`「app 側宿主 ＝ f3_screen_stepg_run」皆 `rc 0`）。🔒 原型首版將 `R-10` 之二名置於 `SNAPSHOT` 之後 ⇒ `run_all` 相異項 `5`（`#59`〜`#62`、`#64`·皆其 traceback 所載 `run_verification.py` 之行號 `+17`）；改置 `def main` 之後即逐位同——`R-10` 之位置之由。**CC 之碼⛔ 須同原型**；唯須滿足 `§三` 與 `§四` |
| `9` | `F8 run`／`run_all`（開工態） | `F8 run`、`k6s3 run`（`n` ＝ `35`／`36`）二退縮與 `F9 run` 皆 `rc 0`；`run_all` 於倉外路徑 ⇒ `64` 項·PASS `28`／FAIL `36`·末端夾具／golden 列 `21`·對帳段 `22／36`·`235960` B（其 bytes 平台與路徑相依·⛔ 入判） |

---

## `§二`　KL 之語與射程

🔒 **所據之裁**：
- **`K-9-52`**（KL `2026-09-29 22:38`／`22:49`·逐字「1. 問一：是 2. 問二：是 … 4. 深度比較改成以 0.1 m 之容差」「補問一則：是」·本批入典·塊 `K5`）：① 正面道路只限「道路」類之街廓；② 「次一級路寬」以本區各街廓正面路寬之相異值由寬而窄逐級往下，較原街廓寬者排在全部較窄者之後、兩趟皆不排除；③ 深度相差 `0.1 m` 以內（含）視為同深（以原街廓為準）；④ ③ 只用於候選街廓之先後，增配資格仍⛔ 設容差；⑤ 通知二、三（驗證路徑之區外道路名稱另立一檔、快照⛔ 動；正面道路未填名者停機並列出）KL 未駁。問一、問二、通知三則、補問之全文與 KL 之答 ＝ 塊 `K5` 逐字。
- `v3` 五級③（KL `2026-09-05`·八鍵詞典序；`r3`〜`r5` 為排名條件、⛔ 淘汰條件；`r2` 往大者第一趟允許、第二趟排除）；`K-9-1` ⑨（最小建築面積之有效值與級）；`K-9-46`（合併單位之原街廓；增配之比較⛔ 設容差）。
🔒 **流程之令**：規格單流程自本單起為常態（KL `2026-09-29 20:20` 逐字「兩題問題：均"是"」·`docs/orders/W-G.9-358_輕量單.md` `§二`）；附則甲〜丙（恆常附款登記表「`n③` 之試行期變通之期滿與續行」節 ③ 之 `2`）：甲 本單⛔ 令任何片「維持原狀」（本批⛔ 動任何宗地）；乙 同一量之判、寫、讀出自同一式（`§三-1` `R-4`／`R-7`：深度、路寬、最小建築面積、距離皆以 `adj_q2` 之值判之、寫之、比之）；丙 CC 之唯讀獨立 reviewer 列為工項二之常設步（驗後、推前·停機款 `12`）。
🔒 **側支之推送**：KL `2026-09-02` 逐字「CC 把生產碼 commit 推到一個側分支（例如 `verify/W-G.9-198R-c1`），主分支 `wip/s1-endpart` 原地不動：OK」（`CLAUDE.md`「`W-G.9-206` 補款」之一）⇒ 本批之五筆 `commit` 推至新側支⛔ 須放行；**主線之推進另單·候 KL 逐字放行**。
🛑 **射程**：`(a)` 工項零〜四之 `push` 一律至新側支 `verify/W-G.9-359-cand`；`(b)` 主線⛔ 動、KL 主 checkout⛔ 動；`(c)` ⛔ 及 `app.py`／`verify/run_verification.py` 以外之生產碼、`§三-3` 之禁改、任何他錨；`(d)` ⛔ 建名單之消費端（規格步 `4`〜`8`·任何配地、`G` 式、判定⛔ 讀名單）、⛔ 及增配之資格與選塊、畫面所填名稱之持久化（畫面批）、`GB-194`——另單。

---

## `§三`　規格（CC 依之撰寫生產碼·⛔ 以程式行表述）

🔒 **受詞之總述**：調配之輸入盤點（`adj_intake`·`W-G.9-351`）之每一合併單位，出一**候選街廓名單**（規格步 `3`）：建地軌 ＝ 自原街廓起、其餘可建築街廓依五級八鍵升序；公設軌 ＝ 全部可建築街廓依距離升序。名單以五個新純函式求之、於畫面成果區顯示之（harness 由量測器 `F18` 以同一函式求之）；本批⛔ 消費之。另依 `K-9-52` ① 改正面道路之推導之候選，並立驗證路徑之區外道路名稱之來源。

**用語**（本節專用）：「**可建築街廓**」＝ 負擔屬性（`F3_CATEGORY_BURDEN` 之值）＝ `ADJ_BURDEN_BUILD` 之街廓；「**原街廓 `S`**」＝ 合併單位之 `原街廓`；「**候選 `T`**」＝ 可建築街廓；「**`q(x)`**」＝ `adj_q2(x)`（四捨五入至 `0.01`·`R-4`）。

### `§三-1`　行為要求（逐條·「給定何種情形、須得何種結果」）

| # | 給定 | 須得 |
|---|---|---|
| `R-1` | 類別表（`K-9-52` ①） | module 層之新 dict **`F3_CATEGORY_FRONT_ROAD`**，置於 `F3_CATEGORY_BURDEN` 之定義之後：其鍵 ＝ `F3_BLOCK_CATEGORIES` 之全部 `16` 項（同序），值皆 `bool`，**唯 `"道路"` 為 `True`** |
| `R-2` | `parse_cad_precision_layers` 中 `result['front_road_derive'] = r3_front_road_derive(_front_pts_chosen, {…})` 之第二引數（dict 推導式） | 保留其既有之條件 `if _lr not in _buildable_blocks`，**另加一條件**：該街廓之 `category`（`_br.get('category', '')`）於 `F3_CATEGORY_FRONT_ROAD` 為真（`F3_CATEGORY_FRONT_ROAD.get(…, False)`）者方入。`r3_front_road_derive` 等五函式與該函式之其餘一字⛔ 動。**本案之推導逐位同開工態**（`V-3` 之 `F9 run`） |
| `R-3` | 深度之容差（`K-9-52` ③） | module 層之具名常數 **`ADJ_DEPTH_TIE_TOL_M = 0.1`**（置於新段之首·新段位於 `adj_intake_rows` 之後、`wg9248_stringify_mixed_cols` 之前） |
| `R-4` | **`adj_q2(x)`** | 回 `Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)`（例：`0.125 ⇒ 0.13`、`2.675 ⇒ 2.68`、`1.005 ⇒ 1.01`、`-0.125 ⇒ -0.13`）。凡本批之深度、深度差、路寬、最小建築面積、距離，其判、寫、比皆以 `q` 之值（附則乙） |
| `R-5` | **`adj_block_ctx(labels, category_by, eff_min_build_by, ident_by, width_by, depth_by)`**（皆 `{label: 值}`·`labels` 為可建築街廓之 label） | ① `labels` 中 `ident_by` 之值為空（`None` 或空字串）者**一次列出全部**（依 `labels` 之序）⇒ `RuntimeError`，其訊息含字樣 **`正面道路`** 與該等 label，並告以於步驟 E 之「正面道路名稱／識別符」欄填名（`K-9-52` ⑤·通知三）；② 其後逐 label：`category_by` 之值為空、`width_by` 之值缺或 `≤ 0`、`depth_by` 之值缺或 `≤ 0` ⇒ `RuntimeError`；③ 回 `{label: {'使用分區': str(category), '最小建築面積': q(eff_min_build_by.get(label, 0) or 0), '正面道路': str(ident), '正面路寬': q(width), '深度': q(depth)}}` |
| `R-6` | **`adj_pool_anchor(g_rows)`** | 逐 `所屬街廓`，於 `推進側別` ＝ `ADJ_POOL_SIDE` 且 `cut_coords` 至少 `3` 點之列中，取多邊形（無效者 `buffer(0)`）面積最大者（並列 ⇒ `str(暫編地號)` 字典序小者）；回 `{街廓: (質心 x, 質心 y)}`（`float`）；無此種列之街廓⛔ 入 |
| `R-7` | **`adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPTH_TIE_TOL_M)`**（`intake` ＝ `adj_intake` 之回傳；`blk_ctx` ＝ `R-5` 之回傳·其鍵 ＝ 全部可建築街廓；`pool_anchor` ＝ `R-6` 之回傳；`slice_coords` ＝ `{暫編地號: polygon_coords}`） | 依 `intake['units']` 之序，逐單位出 `{'歸戶', '軌', '原街廓', '錨點', '名單'}`：<br>① **錨點** ＝ 該單位之 `建築街廓內不能分配` ＋ `共同負擔用地` 之列中 `原有面積` 最大者（並列 ⇒ `str(暫編地號)` 字典序小者）之 `str(暫編地號)`；單位無列、或錨點於 `slice_coords` 無至少 `3` 點 ⇒ `RuntimeError`。<br>② **距離** `d(T)` ＝ `q(錨點之多邊形之質心至 pool_anchor[T] 之直線距離)`；`T ∉ pool_anchor` ⇒ `None`；`r7(T)` ＝ `(0, d(T))`，`d(T)` 為 `None` 者 ＝ `(1, Decimal('0'))`。<br>③ **建地軌**（`軌` ＝ `ADJ_TRACK_BUILD`）：`S ∉ blk_ctx` ⇒ `RuntimeError`；`名單[0]` ＝ `S`（`'原街廓': True`、`'鍵': None`、描述欄皆 `'—'`、`'深度差': None`、`'距離': d(S)`、`'第二趟排除': False`·⛔ 排序）；其餘 `T ≠ S` 依 `鍵` ＝ `(r1, r2, r3, r4, r5, r6, r7, T)` **升序**：`r1` ＝ `0`（`使用分區` 同）／`1`；`r2`：級 ＝ 全部可建築街廓之 `最小建築面積` 之相異值**升序**，`i` ＝ `S` 之位、`j` ＝ `T` 之位，`j ≤ i` ⇒ `(0, i − j)`、否則 `(1, j − i)`；`r3` ＝ `0`（`正面道路` 同）／`1`；`r4` ＝ `0`（`正面路寬` 同）／`1`；`r5`：級 ＝ 全部可建築街廓之 `正面路寬` 之相異值**降序**（由寬而窄），`j ≥ i` ⇒ `(0, j − i)`、否則 `(1, i − j)`（`K-9-52` ②）；`r6`：`Δ ＝ 深度(T) − 深度(S)`（二者皆 `q` 之值），`|Δ| ≤ Decimal(repr(float(tol)))` ⇒ `(0, Decimal('0'))`（同深）、`Δ < 0` ⇒ `(0, −Δ)`（較淺）、`Δ > 0` ⇒ `(1, Δ)`（較深）（`K-9-52` ③）。<br>④ **公設軌**（其餘）：`名單` ＝ 全部可建築街廓依 `鍵` ＝ `(r7, T)` 升序（描述欄皆 `'—'`、`'深度差': None`、`'第二趟排除': False`）。<br>⑤ `名單` 之每項 ＝ `{'序', '街廓', '原街廓', '鍵', '使用分區', '最小建築面積', '正面道路', '正面路寬', '路寬級距', '深度差', '深度', '距離', '第二趟排除'}`：`'序'` ＝ `1` 起之整數；建地軌之 `T`：`'使用分區'`／`'正面道路'`／`'正面路寬'` ＝ `'同'`／`'異'`；`'最小建築面積'` ＝ `'同級'`（`r2 ＝ (0, 0)`）／`'往小 n 級'`／`'往大 n 級'`；`'路寬級距'` ＝ `'同級'`／`'往窄 n 級'`／`'往寬 n 級'`（`n` ＝ 級數·半形空白分隔）；`'深度'` ＝ `'同深'`／`'較淺'`／`'較深'`；`'深度差'` ＝ `Δ`（`Decimal`）；`'距離'` ＝ `d(T)`（`Decimal` 或 `None`）；`'第二趟排除'` ＝ `r2` 之首項為 `1`（`v3` 五級③ `r2`：往大者第二趟排除）。**⛔ 讀 session** |
| `R-8` | **`adj_candidate_rows(cand, tol=ADJ_DEPTH_TIE_TOL_M)`**（`cand` ＝ `R-7` 之回傳） | 回 `{'lines', 'units', 'detail'}`，其列之各值皆 `str`：`units` ＝ 逐單位一列 `{'歸戶', '軌', '原街廓'（`None` ⇒ `'—'`）, '錨點（重劃前面積最大之一筆）', '候選街廓（依序）'}`，末欄 ＝ 各項之 `街廓` 依序以 `' → '` 相接，`原街廓` 真者後綴 `'（原街廓）'`、`第二趟排除` 真者後綴 `'（第二趟排除）'`（例：`S（原街廓） → d → a → b → c（第二趟排除）`）；`detail` ＝ 逐單位逐項一列 `{'歸戶', '序', '街廓', '使用分區', '最小建築面積', '正面道路', '正面路寬', '路寬級距', '深度', '深度差(m)', '距離(m)'}`，後二欄 ＝ `None` ⇒ `'—'`、否則 `f"{float(v):.2f}"`；`lines` ＝ 恰一句 `f"合併單位 {N}（{ADJ_TRACK_BUILD} {nb}·{ADJ_TRACK_PUBLIC} {N − nb}）；深度相差 {float(tol):.2f} m 以內視為同深（以原街廓為準）"` |
| `R-9` | `main()` 之成果區 | 於「🧩 調配階段之輸入」之區塊（自 `_adj351_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)` 起連續 `2` 句）**之後**、`# 🆕 W-G Y 波診斷專用` 之註解之前，同縮排，增恰 `2` 句：`_adj359_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)`；`if _adj359_bf is not None:`，其內 `with st.expander("🧭 調配之候選街廓名單（五級八鍵·僅排序·尚未調配）", expanded=False):` 內：<br>① `try`：`temp` ＝ `k6b_stage3_selected(st.session_state, build_parcels, st.session_state.get('f3L_setback_default'))` 為 `None` ⇒ `temp_parcels`、否則其 `[0]`；`intake` ＝ `adj_intake(temp, _adj359_bf, st.session_state.get('f3_G_values') or [], st.session_state.get(SS_ADJ_DROPPED) or {}, st.session_state.get('t8_ownership_map', {}) or {}, {b['label']: F3_CATEGORY_BURDEN.get(b.get('category', ''), '') for b in classified_blocks})`（**與 🧩 區塊同參**）；可建築街廓 ＝ `classified_blocks` 中 `F3_CATEGORY_BURDEN.get(b.get('category', ''), '') == ADJ_BURDEN_BUILD` 者（依其序）；識別符 ＝ `r3_front_road_identifier(labels, st.session_state.get(SS_FRONT_ROAD_DERIVE, {}) or {}, {b['label']: (st.session_state.get(SS_FRONT_ROAD_NAME, {}) or {}).get(b['id'], '')})`（**名稱以 `b['id']` 取**·同步驟 E）；`blk_ctx` ＝ `adj_block_ctx(labels, {label: category}, st.session_state.get(K91_SS_MBA_EFFECTIVE, {}) or {}, {label: 識別符之 'id'}, {label: st.session_state.get('f3_sb_rows') 之列（以 '街廓' 為鍵）之 '正面路寬(m)'}, st.session_state.get('f3_alloc_depth_by_label', {}) or {})`；`cand` ＝ `adj_candidate_lists(intake, blk_ctx, adj_pool_anchor(st.session_state.get('f3_G_values') or []), {str(t['暫編地號']): (t.get('polygon_coords') or []) for t in temp})`；`view` ＝ `adj_candidate_rows(cand)`。② `except RuntimeError as e`：`st.error(str(e))`、`view` ＝ `None`。③ `view` 非 `None` ⇒ 逐 `view['lines']` 以 `st.caption`；`st.markdown`（標題一句）；`st.dataframe(_pd.DataFrame(view['units']), use_container_width=True, hide_index=True)`；`st.markdown`（標題一句）；`st.dataframe(_pd.DataFrame(view['detail']), use_container_width=True, hide_index=True)`。本區塊之 `st.dataframe` 恰 `2`、`st.caption` ＝ `lines` 之數、⛔ 他種輸出 |
| `R-10` | `verify/run_verification.py` | module 層增 `FRONT_ROAD_NAMES = os.path.join(HERE, "case_front_road_names_UC9898.json")` 與函式 **`load_front_road_names()`**，**二者皆置於 `def main` 之後、`if __name__ == "__main__":` 之前**（🔒 `main` 以前之行號⛔ 移：`run_all` 之出艙含本檔之 traceback 行號，前移即使 `V-5` 之相異項非 `0`·發單側之原型首版即以此紅）：以 UTF-8 讀之，回 `dict(該檔之 'names')`；`names` 非 `{str: 非空 str}` ⇒ `RuntimeError`（⛔ 靜默回空）。他處⛔ 呼叫之（本批之消費者唯量測器 `F18`） |
| `R-11` | 資料檔（`K-9-52` ⑤） | 新檔 `verify/case_front_road_names_UC9898.json` ＝ 塊 `J1`（依圍欄抽出·二進位寫出） |
| `R-12` | 本案（harness·退縮 `3.5`／`0.0`） | 段三、宗地、配地、末端塊之合併再試、調配之輸入、`run_all` ——**逐位同開工態**（`V-2`〜`V-5`）；名單二退縮皆⛔ 停機，其值 ＝ `F18 run` 之外部錨（`V-1`） |
| `R-13` | 消費 | 名單與 `R-1`〜`R-11` 之任一新名⛔ 為任何配地、`G` 式、判定所讀；`def main` 除 `R-9` 之 `2` 句外一字⛔ 動 |

### `§三-2`　介面（名與簽名·量測器 `F18` 以之為受詞）

| # | 名 | 簽名／回傳 | 呼叫端 |
|---|---|---|---|
| `I-1` | 新 `F3_CATEGORY_FRONT_ROAD`（dict）、`ADJ_DEPTH_TIE_TOL_M`（`0.1`） | `R-1`／`R-3` | `parse_cad_precision_layers`（`R-2`）；`adj_candidate_lists`／`adj_candidate_rows` 之 `tol` 之預設 |
| `I-2` | 新 `adj_q2` | `(x)` → `Decimal` | `adj_block_ctx`、`adj_candidate_lists` |
| `I-3` | 新 `adj_block_ctx` | `(labels, category_by, eff_min_build_by, ident_by, width_by, depth_by)` → `dict` | `main()`（`R-9`）；`F18` |
| `I-4` | 新 `adj_pool_anchor` | `(g_rows)` → `dict` | 同上 |
| `I-5` | 新 `adj_candidate_lists` | `(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPTH_TIE_TOL_M)` → `list` | 同上 |
| `I-6` | 新 `adj_candidate_rows` | `(cand, tol=ADJ_DEPTH_TIE_TOL_M)` → `{'lines', 'units', 'detail'}` | 同上 |
| `I-7` | 新 `load_front_road_names`、`FRONT_ROAD_NAMES`（`verify/run_verification.py`） | `()` → `dict` | `F18` |

### `§三-3`　禁改（既有閘之錨·CC 撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

| # | 禁 | 所護之閘 |
|---|---|---|
| `X-1` | 「🧩 調配階段之輸入」之區塊（自 `_adj351_bf = …` 起連續 `2` 句）一字不動（`R-9` 之新區塊須另立於其後·⛔ 併入其內） | `F10 wiring` `W5`（抽該 `2` 句以假 st 執行·期「三表」「總句 1」）與其突變 `N4` |
| `X-2` | 五個新函式（`adj_q2`／`adj_block_ctx`／`adj_pool_anchor`／`adj_candidate_lists`／`adj_candidate_rows`）之全文（含 docstring 與註解）⛔ 含字樣：`adj_intake`、`SS_ADJ_BUILD_FINAL`、`SS_ADJ_DROPPED`、`f3_k929_6`、`r3_front_road`、`SS_FRONT_ROAD`、`front_road_derive`、`session_state` | `F9 wiring`／`F10 wiring` 之消費端之閘（該等字樣唯許於所列之函式與 `main`）；`F18 wiring` `W4` |
| `X-3` | `r3_front_road_derive`／`r3_normalize_road_name`／`r3_front_road_identifier`／`r3_front_road_caption`／`r3_front_road_rows`、`R3_*` 常數、`_line_block_overlap`、`_best_block` 一字不動；`parse_cad_precision_layers` 唯 `R-2` 之一條件得增（既有之 `if _lr not in _buildable_blocks` 須存） | `F9` 之 `selftest`（`M0`〜`M3`）／`wiring`（`W1`〜`W3c`·`W2d`）／`run` |
| `X-4` | `_WF_NS_NAMES` 一字不動 | `wfns_ast` `48`／`48`／`47` |
| `X-5` | `adj_intake`、`adj_intake_rows`、`k6b_*`、`end_block_*`、`k6_merge_groups`、`solve_G_binary`、`_solve_G_one`、`k929_6_*`、`f3_screen_*`、`k6b_stage3_selected`、`n19p_depth_info_by_label`、`k91_*`、`F3_BLOCK_CATEGORIES`、`F3_CATEGORY_BURDEN` 一字不動；`verify/` 唯 `run_verification.py` 得改（唯增 `R-10` 之二名·既有一字不動）、唯 `case_front_road_names_UC9898.json`（`R-11`）與 `probes/probe_WG9359_cand.py`（工項一）得增，餘（含 `selection_pipeline.py`、`stepg_pipeline.py`、`case_params_UC9898.json`）一字不動 | `F9`〜`F17`、`main_synth`、`parity`、`run_all` |
| `X-6` | 新碼⛔ 含案件字面（街廓名、側別、地號、分區名之字串常數·`CASE_LIT_RE` 之形）；五個新函式內⛔ 字面 `0.1`／`0.5`（以 `ADJ_DEPTH_TIE_TOL_M` 為之） | 泛化之鐵則；`F18 wiring` `W1`／`W4` |
| `X-7` | `def main` 除 `R-9` 之 `2` 句外一字不動 | `main_synth`、`F4 wiring`、`F9 wiring` `W3a`〜`W3c`、`F10 wiring` `W5`、`F15 wiring` |

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`D-1`：本規格之任一條，其二讀法之後果**在土地上相異**（任一單位之名單之先後、第二趟排除之標）。
`D-2`：`R-5`〜`R-7` 之輸入於某情形無從依本規格定之（例：某可建築街廓無正面路寬、深度之資料來源不止一而其值相異）。
`D-3`：須動 `§三-3` 之任一字始能滿足 `§三-1`。
🔒 非域上之實作細節（函式內之切分、區域名〔`R-9` 之 `_adj359_bf` 除外〕、註解、`RuntimeError` 之措辭〔`R-5` 所令之字樣除外〕、`st.markdown` 之標題句）由 CC 定之，並於報告 ⑦ 逐項具名其選擇與其由。

### `§三-5`　CC 之設計說明（報告 ⑦ 須載）

逐 `R-1`〜`R-13`：落於何函式、何處；`§三-4` 末之實作細節之選擇及其由；對 `§三-3` 各款之自查（逐款具名「未觸」及其據）；附則乙之自查（深度、路寬、最小建築面積、距離之判、寫、比之式各一）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/run_verification.py` 之**全文**（報告內嵌或報告同目錄之 `.diff` 檔·⛔ 摘要）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-359_規格單.md`（**新檔**·二進位複製）。`commit` 訊息逐字 `W-G.9-359 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-359-cand`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`33`**、主線仍 ＝ `1841914…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-359-cand`（快轉）。

**工項一　量測器入倉**（**先於生產碼**·新側支·零生產碼）：塊 `F18` 依圍欄之逐列索引抽出、對拍 `§五-1` 後，以二進位寫為 `verify/probes/probe_WG9359_cand.py`（**新檔**·blob ＝ `§五-1` 項 `7`）。`commit` 訊息逐字 `W-G.9-359 工項一：量測器 F18（調配之候選街廓名單）入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-359-cand`。

**工項二　生產碼 ＋ 資料檔**（🔴 `app.py` ＋ `verify/run_verification.py`·CC 依 `§三` 撰寫；塊 `J1` 寫為 `verify/case_front_road_names_UC9898.json`·一 `commit`·推新側支）

**前置**（於工項一之端·⛔ `commit`·出艙一律存倉外之目錄 `<O>`；`<P>` ＝ 倉外之拋棄式 worktree 之絕對路徑，前置與驗之 `run_all` **同一路徑**）：
1. `python verify/probes/probe_WG9359_cand.py selftest <repo>`；`… wiring <repo>`；`… run <repo>` ⇒ 皆 **`rc 1`**（末列逐字 ＝ `§一` 項 `7`）。
2. `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_pre_35.json`；同 `0.0` ⇒ `<O>\k6s3_pre_00.json`（皆 `rc 0`）。
3. `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_pre_35.log`；同 `0.0` ⇒ `<O>\f8_pre_00.log`（皆 `rc 0`）。
4. `python verify/probes/probe_WG9350_frontroad.py run <repo> > <O>\f9_pre.log`（`rc 0`）。
5. `git worktree add --detach <P> HEAD`；於 `<P>`：`python verify/run_all.py > <O>\runall_pre.log`（跑畢 `git worktree remove --force <P>`）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：CC 依 `§三` 撰寫二檔之改動；塊 `J1` 依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位寫為 `verify/case_front_road_names_UC9898.json`（blob ＝ `§五-1` 項 `7`）；`python -m py_compile app.py verify/run_verification.py`；`commit` 訊息逐字 `W-G.9-359 工項二：調配之候選街廓名單（規格步 3·五級八鍵·K-9-52）＋ 正面道路只限道路類 ＋ 驗證路徑之區外道路名稱 🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | `python verify/probes/probe_WG9359_cand.py selftest <repo> > <O>\f18_self_post.log`；`… wiring <repo> > <O>\f18_wir_post.log`；`… run <repo> > <O>\f18_run_post.log` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`；`selftest` 之 `C1`〜`C18`（`22` 例）皆 ✅、`P0` `22／22`；`wiring` 之 `W1`〜`W6` 皆 ✅；`run` 之二退縮 `R0`〜`R5` 皆 ✅（合併單位 `3.5` ⇒ `23`、`0.0` ⇒ `24`；`R4` 之二單位） |
| `V-2` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json`；同 `0.0`；`python verify/probes/probe_WG9344_k6s3.py cmp <O>\k6s3_pre_35.json <O>\k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；二 `cmp` 皆 **`rc 0`**（逐宗、抵費地、街角得標、強制旗標皆同） |
| `V-3` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 > <O>\f8_post_35.log`；同 `0.0`；二者各與前置 `3` 之一份 `diff`；`python verify/probes/probe_WG9350_frontroad.py run <repo> > <O>\f9_post.log` 與前置 `4` `diff` | 皆 **`rc 0`**；**三份之 `diff` 皆空**（正面道路之推導逐位同·`R-2`） |
| `V-4` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json`；同 `0.0` ⇒ `<O>\parity00_post.json` | 皆 **`rc 0`**；配地列 `3.5` ⇒ harness `35`／畫面 `34`、`0.0` ⇒ `36`／`35`，不符格 `0`；`Z` 皆 ＝ `[('harness', 'R1-抵費地-2')]` |
| `V-5` | 另立 `<P>`（同前置之路徑）於工項二之 `commit` 跑 `python verify/run_all.py > <O>\runall_post.log`；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`；另 `diff <O>\runall_pre.log <O>\runall_post.log` | 項數 `64`；PASS `28 → 28`；**相異項 `0`**；末端夾具／golden 列 `21／21`·相異 `0`；對帳段 `22／36 → 22／36`；`diff` 之全文出艙於報告（其 bytes 平台相依·⛔ 入判） |
| `V-6` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`2`**（`app.py`、`verify/run_verification.py`）；二者之 blob 與增／刪之數出艙（發單側復驗時自倉重算）；`verify/` 之其餘一切檔對工項一之端唯增 `case_front_road_names_UC9898.json`（blob ＝ `§五-1` 項 `7`），餘相異 `0` |
| `V-7` | `§四-3` 閘 `8`〜`24` 之諸器（於工項二之 `commit`） | 皆 ＝ 其期 |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**）。

**唯讀獨立審查**（附則丙·驗皆符後、推前）：CC 另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ CC 修之、重驗 `V-1`〜`V-7`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-359-cand`。

**工項三　入典與登記**（新側支·零生產碼·一 `commit`）：塊 `K5` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `P13` 附於 `CLAUDE.md` 之末；塊 `V1` 附於 `docs/配地計算總規格_v3.md` 之末（皆二進位·嚴格前綴·停機款 `8`）。`commit` 訊息逐字 `W-G.9-359 工項三：K-9-52 之入典 ＋ 待落地清單之更新 ＋ v3 五級之補充與更正標記（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-359-cand`。

**工項四　執行報告入倉**（新側支·新檔 `docs/reports/W-G.9-359R_調配之候選街廓名單_執行報告.md`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 工項二之前置與驗之全部出艙（`F18` 三子命令之全文、`k6s3 cmp` 二份、`F8 run` 二份與 `F9 run` 之 `diff` 之結果、`parity` 二份之末十列、`runall` 對拍之全文與 `diff` 之結果）；④ 五塊之實得（bytes／`sha256`）與三檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ CC 之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **二檔之全文差異**（`§三-5`）；⑨ **各段耗時**（讀單／撰碼／前置／驗／審查／登記／報告）。收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。`commit` 訊息逐字 `W-G.9-359 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-359-cand`。

### `§四-2`　復驗時補寫者（規格單流程·⛔ 本單之期）

發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之二條件、`R-7` 之八鍵與同深之判、`R-9` 之資料來源、`X-2` 之字樣）及其突變之判別力（`§一` 項 `8` 之十三突變之形）；併入主線之請示。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之刪除欄 | 工項二 ＝ `app.py`／`verify/run_verification.py`（增／刪 ＝ 工項二之 `V-6` 所出艙）；其餘逐檔 **`0`** |
| `2` | 生產碼 `34` 檔對 `1841914` | 相異恰 **`2`**（`app.py`、`verify/run_verification.py` ＝ 工項二之 `V-6` 所出艙之 blob）；`verify/` 之一切檔相異恰 **`3`**（`verify/run_verification.py` ＋ 新檔 `verify/case_front_road_names_UC9898.json`、`verify/probes/probe_WG9359_cand.py`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`**（`9` 檔：本單、`F18`、`J1`、`app.py`、`verify/run_verification.py`、`K-6` 典、`CLAUDE.md`、`v3`、報告） |
| `4` | 三檔之 bytes | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `435812` → **`444589`**；`CLAUDE.md` `308508` → **`312493`**；`docs/配地計算總規格_v3.md` `65433` → **`67089`**；改前皆為改後之嚴格前綴 |
| `5` | 自限 | 遠端 heads **`33`**；主線 ＝ `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`（⛔ 變）；`verify/W-G.9-359-cand` ＝ 工項四之 `commit`，其祖含 `1841914`；`verify/W-G.9-357-k948` ＝ `4716f20…`、`verify/W-G.9-353-endmerge` ＝ `1ef3bb5…`、`verify/W-G.9-343-k929b` ＝ `14e0222…`、`verify/W-G.9-341-gb182` ＝ `d0add71…`、`verify/W-G.9-338-origin` ＝ `2ec1eb2…`、`verify/W-G.9-333-gb168` ＝ `be5108d…`、`verify/W-G.9-299-gb170` ＝ `488c485…`（皆⛔ 變） |
| `6` | `python verify/probes/probe_WG9270_closegate.py 550 549 .` | **`rc 0`**（二閘皆過） |
| `7` | `python verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 550 549` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 `535`／`MAX` `550`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；**`K-9` `49`／`52`**／`[44, 47]`（自誤／`GB`／`VR` 皆 ＝ 開工態；`K-9` 唯增 `52`） |
| `8` | `python verify/probes/probe_WG9359_cand.py selftest <repo 絕對路徑>`；`… wiring …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |
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
| `21` | `python verify/probes/probe_WG9345_screen.py parity … 3.5 on <json>`；同 `0.0`；`… wiring …`；`python verify/probes/probe_WG9345_screen.py selftest` | 皆 **`rc 0`**（`parity` 之數 ＝ `V-4`） |
| `22` | `python verify/probes/probe_WG9344p1_pooltemp.py run <repo 絕對路徑> 3.5 on`；`… selftest`；`python verify/probes/probe_WG9344_k6s3.py selftest` | 皆 **`rc 0`** |
| `23` | `python verify/probes/probe_WG9357_k948.py selftest …`；`… run …` | 皆 **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0`（`selftest` 之 `P0` `25／25`） |
| `24` | `python verify/probes/probe_WG9358_k948_wiring.py wiring …` | **`rc 0`**；末列逐字 `⇒ 紅 []；rc 0` |

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單側擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑） |
| `2` | 塊 `F18` | `40667` B·`sha256` `52acefc447431ef03af5e658b43c1736b086e58c291f639639a275354fda2456`·`697` 列（圍欄內全文·末附換行）；寫為新檔 `verify/probes/probe_WG9359_cand.py` |
| `3` | 塊 `J1` | `527` B·`sha256` `13cf56d7b64decb87e9697efb36803e62fb88b948a1ed58ce893f63cea2d0c5e`·`12` 列（圍欄內全文·末附換行）；寫為新檔 `verify/case_front_road_names_UC9898.json` |
| `4` | 塊 `K5` | `8777` B·`sha256` `de4f52eafe2ee09119306312fe8c70b7285ac86587db23a7c4cc42e61dacd14a`·`95` 列（圍欄內全文·末附換行）；附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md`（`435812` B）之末後，期末 ＝ `444589` B |
| `5` | 塊 `P13` | `3985` B·`sha256` `c1ea196484f1bb72fd82e6bc583c6d93293eaf0a3c313233d1ca895a873cbaa7`·`22` 列（圍欄內全文·末附換行）；附於 `CLAUDE.md`（`308508` B）之末後，期末 ＝ `312493` B |
| `6` | 塊 `V1` | `1656` B·`sha256` `3088af182c12efd23bc53ce510227cbf40c383227d4e73c2706d239986645ced`·`11` 列（圍欄內全文·末附換行）；附於 `docs/配地計算總規格_v3.md`（`65433` B）之末後，期末 ＝ `67089` B |
| `7` | 寫出後之 blob | `verify/probes/probe_WG9359_cand.py` `fa3d63bec344b67da928f4fc412ce2641bf94cbd`；`verify/case_front_road_names_UC9898.json` `449d375530d8d2207f39aec9f9ac3ba7b524b1c7`。🔒 `app.py`／`verify/run_verification.py` 之施後 blob **⛔ 預載**（規格單·由 CC 回報） |
| `8` | 量測器之二態 | 工項一之端：`F18` 三子命令皆 `rc 1`（`§一` 項 `7`）；工項二施後：皆 `rc 0`（`§一` 項 `8` 之原型為其必過之實例） |
| `9` | pre-flight | `python verify/probes/probe_order_preflight.py <本單>`·發單側窗五十六實跑（態 `1841914`）：🔴 機械 `0` 項／🟡 提示 `4` 項——`P-4` `:99`（`§三-1` 之表頭·所觸之箭頭係 `R-4` 之捨入之例〔`0.125 ⇒ 0.13` 等·輸入至輸出〕與 `R-8` 之相接字串，⛔ 為方向性之轉引 ⇒ **具名豁免**）、`P-4` `:175`（`§四-1` 工項二之驗之表頭·其箭頭之座標系 ＝ 工項一之端〔前置〕至工項二之 `commit`〔驗〕，表內自載 ⇒ **具名豁免**）、`P-4` `:201`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 開工態 `1841914` 至工項三／四之端，表內自載 ⇒ **具名豁免**）、`P-6` `:1096`（附錄丁塊 `P13` 內「前節之更新」列·所觸之數係待落地表之序號、⛔ 為實測之數 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `20014`–`27686`）⇒ `rc 0` |
| `10` | 收工閘之模擬（發單側·本機 Linux·原型之工作樹 ＋ 五塊·⛔ `push`） | `git worktree add --detach <S> 1841914`（拋棄式·⛔ `push`）＋ 本單 ＋ 塊 `F18` ＋ 原型之二檔與塊 `J1` ＋ 塊 `K5`／`P13`／`V1` ＋ 報告之替身·五 `commit`：閘 `1` 之刪除欄（工項二 ＝ 原型之數·⛔ 為期；餘皆 `0`）；閘 `2` 生產碼相異 `2`（`app.py`、`verify/run_verification.py`）、`verify/` 相異 `3`；閘 `3` CR `0`（`9` 檔·`V6.dxf` `12308`）；閘 `4` `435812 → 444589`、`308508 → 312493`、`65433 → 67089`（皆嚴格前綴）；閘 `6` `rc 0`（二閘皆過）；閘 `7` `rc 0`·四簿 ＝ 自誤 `535`／`550`、`GB` `187`／`194`、`VR` `80`／`95`、`K-9` `49`／`52`／`[44, 47]`；閘 `8` `F18` 三子命令皆 `rc 0`；新檔之 `git check-ignore` 皆無命中；閘 `9`〜`24` ＝ `§一` 項 `8`（原型之 `app.py`／`verify/run_verification.py` 之 blob 與模擬之工作樹逐位同） |

抽取式 ＝ 圍欄開列（`` ````python ``、`` ````json `` 或 `` ````markdown ``）之次列至閉列（`` ```` ``）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-359-cand`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 收工後，主 checkout 之根之來源檔（本單）由 KL 自行移除（CC ⛔ 刪之）。

---

## 附錄甲　塊 `F18`（新檔 `verify/probes/probe_WG9359_cand.py`）

````python
# -*- coding: utf-8 -*-
"""W-G.9-359 量測器（發單側窗五十六擬·檔 F18·⛔ 由受單側改一字）：調配之候選街廓名單（規格步 `3`·五級八鍵·
`K-9-52`：正面道路只限「道路」類之街廓；「次一級路寬」以本區實有之路寬逐級往窄、較寬者排最後；深度相差 `0.1 m`
以內視為同深〔只用於候選街廓之先後〕）。

子命令（一律 python verify/probes/probe_WG9359_cand.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `adj_q2`／`adj_block_ctx`／`adj_pool_anchor`／
           `adj_candidate_lists`／`adj_candidate_rows` 與 `ADJ_DEPTH_TIE_TOL_M`、`F3_CATEGORY_FRONT_ROAD`）。
           C1〜C18 ＝ 八鍵各鍵之決勝（使用分區／最小建築面積〔往小、往大、第二趟排除〕／正面道路／正面路寬／
           次一級路寬〔問二附圖之例〕／深度〔0.10 同深·0.11 較淺〕／距離／街廓名）、公設軌、錨點、原街廓居首、
           停機、抵費地之迄點、類別表、顯示列、四捨五入、深度差之 2 位；P0 ＝ 判式自驗。
           🔒 以程式字樣為錨之突變（判別力）⛔ 載於本器——規格單流程由發單側讀受單側之碼後補寫（`W-G.9-359 §四-2`）。
  wiring   <repo>
           AST ＋ 畫面區塊之合成執行：W1 具名常數 ＝ `0.1`、二函式之預設引用之、新函式內⛔ 字面 `0.1`／`0.5`；
           W2 類別表之鍵 ＝ `F3_BLOCK_CATEGORIES`、唯「道路」為真；W3 正面道路推導之候選 ＝ 非可建築 ∩ 類別表為真者；
           W4 新函式⛔ 案件字面、⛔ 讀 session、⛔ 含既有閘所禁之消費字樣；W5 `main()` 之候選街廓區塊（自
           `_adj359_bf` 之賦值起連續 `2` 句）以假 st ＋ 合成資料實際執行（名稱以 `id` 取、路寬取 `f3_sb_rows`、
           深度取 `f3_alloc_depth_by_label`、最小建築面積取 `K91_SS_MBA_EFFECTIVE`·四變體各有其誘餌）；
           W6 `verify/run_verification.py` 之 `FRONT_ROAD_NAMES`／`load_front_road_names`。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R0 區外道路名稱檔；R1 正面道路推導（候選皆「道路」類·推導 ＝
           `W-G.9-350 §一` 項 `5` 之表）；R2 名單⛔ 停機且與外部錨（本器另寫之排序·⛔ 呼叫名單之函式）逐單位逐序相同；
           R3 畫面區塊以假 st 於本案資料實跑，其二表 ＝ harness 之顯示列；R4 `K-9-52` ③ 之可見效果（原街廓 R6
           之建地軌單位：`0.1` ⇒ R6、R2、R3、R5、R1、R4；以 `0.5` 重算 ⇒ R6、R5、R2、R3、R1、R4）；
           R5 公設軌之名單 ＝ 全部可建築街廓、距離不減。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, math, os, re, sys
from decimal import Decimal, ROUND_HALF_UP

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FUNCS = ["adj_q2", "adj_block_ctx", "adj_pool_anchor", "adj_candidate_lists", "adj_candidate_rows"]
CONSTS = ["ADJ_DEPTH_TIE_TOL_M", "ADJ_POOL_SIDE", "ADJ_TRACK_BUILD", "ADJ_TRACK_PUBLIC",
          "F3_BLOCK_CATEGORIES", "F3_CATEGORY_FRONT_ROAD"]
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
FORBID_TOKS = ["adj_intake", "SS_ADJ_BUILD_FINAL", "SS_ADJ_DROPPED", "f3_k929_6", "r3_front_road",
               "SS_FRONT_ROAD", "front_road_derive", "session_state"]
D = Decimal


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _extract_ns(src, funcs=FUNCS, consts=CONSTS, prefixes=()):
    """自 `app.py` 以 AST 抽出所列之常數與函式，於隔離之命名空間執行。"""
    tree = ast.parse(src)
    parts = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            parts.append(ast.get_source_segment(src, node))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id in consts or node.targets[0].id.startswith(tuple(prefixes) or ("\0",))):
            parts.append(ast.get_source_segment(src, node))
    ns = {}
    exec(compile("\n\n".join(parts), "<cand_extract>", "exec"), ns)
    return ns


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
H, CM = "住宅區", "商業區"


def _sq(cx, cy, h=1.0):
    return [[cx - h, cy - h], [cx + h, cy - h], [cx + h, cy + h], [cx - h, cy + h]]


def _ctx(ns, spec):
    """spec ＝ {label: (使用分區, 最小建築面積, 正面道路, 正面路寬, 深度)}。"""
    L = sorted(spec)
    return ns["adj_block_ctx"](L, {k: spec[k][0] for k in L}, {k: spec[k][1] for k in L},
                               {k: spec[k][2] for k in L}, {k: spec[k][3] for k in L}, {k: spec[k][4] for k in L})


def _unit(ns, g, build, home, slices):
    rows = [{"暫編地號": p, "原有面積": float(a)} for p, a in slices]
    return {"歸戶": g, "軌": ns["ADJ_TRACK_BUILD"] if build else ns["ADJ_TRACK_PUBLIC"], "原街廓": home,
            "建築街廓內不能分配": rows, "共同負擔用地": []}


def _lists(ns, spec, pools, units, coords=None, **kw):
    coords = coords if coords is not None else {"u": _sq(0.0, 0.0)}
    return ns["adj_candidate_lists"]({"units": units}, _ctx(ns, spec), pools, coords, **kw)


def _seq(res, i=0):
    return [it["街廓"] for it in res[i]["名單"]]


def _one(ns, spec, pools, home="S", **kw):
    return _lists(ns, spec, pools, [_unit(ns, "g1", True, home, [("u", 100.0)])], **kw)


def _cases(ns):
    out = []
    X = lambda d: (d, 0.0)  # noqa: E731
    # C1 使用分區
    s1 = {"S": (H, 0, "X", 8, 40), "A": (CM, 0, "X", 8, 40), "B": (H, 0, "Y", 6, 50)}
    _run(out, "C1 使用分區相同者先（縱其他鍵較差、距離較遠）",
         lambda: _seq(_one(ns, s1, {"A": X(10), "B": X(100), "S": X(1)})), ["S", "B", "A"])
    # C2 最小建築面積
    s2 = {"S": (H, 150, "X", 8, 40), "a": (H, 100, "X", 8, 40), "b": (H, 0, "X", 8, 40),
          "c": (H, 200, "X", 8, 40), "d": (H, 150, "X", 8, 40)}
    p2 = {"a": X(40), "b": X(30), "c": X(10), "d": X(50), "S": X(1)}
    _run(out, "C2 最小建築面積：同級 → 往小（次一級先）→ 往大；往大者第二趟排除",
         lambda: [(it["街廓"], it["最小建築面積"], it["第二趟排除"]) for it in _one(ns, s2, p2)[0]["名單"][1:]],
         [("d", "同級", False), ("a", "往小 1 級", False), ("b", "往小 2 級", False), ("c", "往大 1 級", True)])
    # C3 正面道路
    s3 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "Y", 8, 40), "B": (H, 0, "X", 8, 40)}
    _run(out, "C3 正面道路相同者先", lambda: _seq(_one(ns, s3, {"A": X(5), "B": X(50)})), ["S", "B", "A"])
    # C4 正面路寬
    s4 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "Y", 10, 40), "B": (H, 0, "Z", 8, 40)}
    _run(out, "C4 正面路寬相同者先", lambda: _seq(_one(ns, s4, {"A": X(5), "B": X(50)})), ["S", "B", "A"])
    # C5 次一級路寬（問二附圖之例）
    s5 = {"S": (H, 0, "A", 12, 40), "T1": (H, 0, "B", 12, 40), "T2": (H, 0, "C", 10, 40),
          "T3": (H, 0, "D", 8, 40), "T4": (H, 0, "E", 6, 40), "T5": (H, 0, "F", 15, 40), "T6": (H, 0, "G", 20, 40)}
    p5 = {"T1": X(60), "T2": X(50), "T3": X(40), "T4": X(30), "T5": X(20), "T6": X(10)}
    _run(out, "C5 次一級路寬：本區實有路寬逐級往窄，較寬者排最後（問二附圖）",
         lambda: [(it["街廓"], it["路寬級距"]) for it in _one(ns, s5, p5)[0]["名單"][1:]],
         [("T1", "同級"), ("T2", "往窄 1 級"), ("T3", "往窄 2 級"), ("T4", "往窄 3 級"),
          ("T5", "往寬 1 級"), ("T6", "往寬 2 級")])
    # C6 深度（容差 0.1）
    s6 = {"S": (H, 0, "X", 8, 40.00), "a": (H, 0, "X", 8, 40.10), "b": (H, 0, "X", 8, 39.89),
          "c": (H, 0, "X", 8, 39.50), "d": (H, 0, "X", 8, 40.11), "e": (H, 0, "X", 8, 42.00),
          "f": (H, 0, "X", 8, 39.90)}
    p6 = {"a": X(60), "f": X(50), "b": X(40), "c": X(30), "d": X(20), "e": X(10)}
    _run(out, "C6 深度：相差 0.10 以內同深（再依距離）→ 較淺（差小者先）→ 較深（差小者先）",
         lambda: [(it["街廓"], it["深度"]) for it in _one(ns, s6, p6)[0]["名單"][1:]],
         [("f", "同深"), ("a", "同深"), ("b", "較淺"), ("c", "較淺"), ("d", "較深"), ("e", "較深")])
    _run(out, "C7 深度：以 tol ＝ 0.5 重算 ⇒ 0.50 以內皆同深（依距離）",
         lambda: _seq(_one(ns, s6, p6, tol=0.5)), ["S", "d", "c", "b", "f", "a", "e"])
    # C8 距離；無抵費地者排於同鍵之末
    s8 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40), "C": (H, 0, "X", 8, 40)}
    _run(out, "C8 距離近者先；無抵費地之街廓（距離 —）排於同鍵者之後",
         lambda: [(it["街廓"], it["距離"]) for it in _one(ns, s8, {"A": X(30), "B": X(20)})[0]["名單"][1:]],
         [("B", D("20.00")), ("A", D("30.00")), ("C", None)])
    # C9 街廓名
    s9 = {"S": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40)}
    _run(out, "C9 八鍵前七皆同 ⇒ 街廓名之字典序",
         lambda: _seq(_one(ns, s9, {"A": (10.0, 0.0), "B": (-10.0, 0.0)})), ["S", "A", "B"])
    # C10 公設軌
    s10 = {"A": (H, 0, "X", 8, 40), "B": (CM, 500, "Y", 20, 10), "C": (H, 0, "X", 8, 40), "Dd": (H, 0, "X", 8, 40)}
    _run(out, "C10 公設軌：全部可建築街廓依距離（其他鍵⛔ 用）",
         lambda: (lambda r: (r[0]["原街廓"], _seq(r)))(
             _lists(ns, s10, {"A": X(30), "B": X(10), "C": X(20)}, [_unit(ns, "g2", False, None, [("u", 5.0)])])),
         (None, ["B", "C", "A", "Dd"]))
    # C11 錨點
    s11 = {"S": (H, 0, "X", 8, 40), "A": (H, 0, "X", 8, 40)}
    _run(out, "C11 錨點 ＝ 原有面積最大之一筆（並列取暫編地號小者）；距離自其質心起算",
         lambda: (lambda r: (r[0]["錨點"], r[0]["名單"][1]["距離"]))(
             _lists(ns, s11, {"A": X(10), "S": X(3)},
                    [_unit(ns, "g3", True, "S", [("p2", 50.0), ("p3", 80.0), ("p1", 80.0)])],
                    coords={"p1": _sq(0.0, 0.0), "p2": _sq(500.0, 0.0), "p3": _sq(1000.0, 0.0)})),
         ("p1", D("10.00")))
    # C12 原街廓居首
    s12 = {"S": (CM, 900, "Z", 30, 5), "A": (H, 0, "X", 8, 40), "B": (H, 0, "X", 8, 40)}
    _run(out, "C12 建地軌：原街廓居首（⛔ 排序·僅一次）",
         lambda: (lambda r: [(it["街廓"], it["原街廓"], it["鍵"] is None) for it in r[0]["名單"]])(
             _one(ns, s12, {"A": X(1), "B": X(2), "S": X(99)})),
         [("S", True, True), ("A", False, False), ("B", False, False)])
    # C13 停機
    def _stop(fn):
        try:
            fn()
            return "未停"
        except RuntimeError as ex:
            return ("停", "B" in str(ex) and "C" in str(ex)) if "正面道路" in str(ex) else ("停",)
    L3 = ["A", "B", "C"]
    _run(out, "C13a 正面道路無名者一次列出全部 ⇒ 停機",
         lambda: _stop(lambda: ns["adj_block_ctx"](L3, {k: H for k in L3}, {}, {"A": "X", "B": None, "C": ""},
                                                   {k: 8 for k in L3}, {k: 40 for k in L3})), ("停", True))
    _run(out, "C13b 正面路寬為 0 ⇒ 停機",
         lambda: _stop(lambda: ns["adj_block_ctx"](["A"], {"A": H}, {}, {"A": "X"}, {"A": 0}, {"A": 40})), ("停",))
    _run(out, "C13c 深度缺 ⇒ 停機",
         lambda: _stop(lambda: ns["adj_block_ctx"](["A"], {"A": H}, {}, {"A": "X"}, {"A": 8}, {})), ("停",))
    _run(out, "C13d 原街廓非可建築街廓 ⇒ 停機",
         lambda: _stop(lambda: _one(ns, {"A": (H, 0, "X", 8, 40)}, {}, home="Q")), ("停",))
    _run(out, "C13e 錨點無幾何 ⇒ 停機",
         lambda: _stop(lambda: _one(ns, {"S": (H, 0, "X", 8, 40)}, {}, coords={})), ("停",))
    # C14 抵費地之迄點
    rows = [{"推進側別": "抵費地", "所屬街廓": "A", "暫編地號": "A-抵費地-1", "cut_coords": _sq(0, 0, 5)},
            {"推進側別": "抵費地", "所屬街廓": "A", "暫編地號": "A-抵費地-2", "cut_coords": _sq(100, 0, 2)},
            {"推進側別": "left", "所屬街廓": "A", "暫編地號": "a1", "cut_coords": _sq(500, 0, 50)},
            {"推進側別": "抵費地", "所屬街廓": "B", "暫編地號": "B-抵費地-2", "cut_coords": _sq(0, 0, 3)},
            {"推進側別": "抵費地", "所屬街廓": "B", "暫編地號": "B-抵費地-1", "cut_coords": _sq(10, 0, 3)},
            {"推進側別": "抵費地", "所屬街廓": "C", "暫編地號": "C-抵費地", "cut_coords": [[0, 0], [1, 1]]}]
    _run(out, "C14 迄點 ＝ 各街廓之抵費地列中面積最大者之質心（並列取暫編地號小者；非抵費地、無幾何者⛔ 計）",
         lambda: {k: (round(v[0], 6), round(v[1], 6)) for k, v in ns["adj_pool_anchor"](rows).items()},
         {"A": (0.0, 0.0), "B": (10.0, 0.0)})
    # C15 類別表
    _run(out, "C15 類別表之鍵 ＝ F3_BLOCK_CATEGORIES；得為正面道路者唯「道路」",
         lambda: (sorted(ns["F3_CATEGORY_FRONT_ROAD"]) == sorted(ns["F3_BLOCK_CATEGORIES"]),
                  sorted(k for k, v in ns["F3_CATEGORY_FRONT_ROAD"].items() if v is True),
                  all(isinstance(v, bool) for v in ns["F3_CATEGORY_FRONT_ROAD"].values())),
         (True, ["道路"], True))
    # C16 顯示列
    def _rows():
        rv = ns["adj_candidate_rows"](_one(ns, s2, p2))
        allstr = all(isinstance(v, str) for r in rv["units"] + rv["detail"] for v in r.values())
        return (allstr, rv["units"][0]["候選街廓（依序）"], len(rv["detail"]), "0.10 m" in rv["lines"][0])
    _run(out, "C16 顯示列：各欄皆字串；序列標原街廓與第二趟排除；逐候選一列；總句載容差",
         _rows, (True, "S（原街廓） → d → a → b → c（第二趟排除）", 5, True))
    # C17 四捨五入
    _run(out, "C17 adj_q2 ＝ 四捨五入至 0.01（ROUND_HALF_UP）",
         lambda: (str(ns["adj_q2"](0.125)), str(ns["adj_q2"](2.675)), str(ns["adj_q2"](1.005)), str(ns["adj_q2"](-0.125))),
         ("0.13", "2.68", "1.01", "-0.13"))
    # C18 深度差以二位小數計
    s18 = {"S": (H, 0, "X", 8, 44.47), "A": (H, 0, "X", 8, 44.34), "B": (H, 0, "X", 8, 44.57)}
    _run(out, "C18 深度差以二位小數計：−0.13 ⇒ 較淺；＋0.10 ⇒ 同深",
         lambda: [(it["街廓"], it["深度差"], it["深度"]) for it in _one(ns, s18, {"A": X(9), "B": X(1)})[0]["名單"][1:]],
         [("B", D("0.10"), "同深"), ("A", D("-0.13"), "較淺")])
    return out


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in FUNCS + CONSTS if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    print("── 合成對照（harvest 之 app.py·⛔ 本案資料）──")
    cases = _cases(ns)
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    n_ok = 0
    for i, (name, got, exp) in enumerate(cases):
        pert = [(n, g, ("擾動", e) if j == i else e) for j, (n, g, e) in enumerate(cases)]
        rr = _report(pert, verbose=False)
        n_ok += int(rr == sorted(set(red) | {name.split()[0]}, key=[c[0].split()[0] for c in cases].index))
    ok0 = n_ok == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {n_ok}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.calls = []

    def __getattr__(self, name):
        def rec(*a, **k):
            self.calls.append((name, a, k))
            return _NullCM()
        return rec


class _NullCM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _find_main_block(mn):
    for n in ast.walk(mn):
        for fld in ("body", "orelse", "finalbody"):
            body = getattr(n, fld, None)
            if not isinstance(body, list):
                continue
            for i, s in enumerate(body):
                if isinstance(s, ast.Assign) and isinstance(s.targets[0], ast.Name) \
                        and s.targets[0].id == "_adj359_bf" and i + 1 < len(body) and isinstance(body[i + 1], ast.If):
                    return body[i:i + 2]
    return None


def _screen_ns(app_src):
    return _extract_ns(app_src, funcs=FUNCS + ["adj_intake", "r3_front_road_identifier", "r3_normalize_road_name"],
                       consts=CONSTS + ["SS_FRONT_ROAD_NAME", "SS_FRONT_ROAD_DERIVE", "K91_SS_MBA_EFFECTIVE"],
                       prefixes=("ADJ_", "SS_ADJ_", "R3_STATUS_"))


def _exec_block(app_src, blk, ss, g_extra):
    import pandas as pd
    rns = _screen_ns(app_src)
    fst = _FakeSt(ss)
    g = dict(rns, st=fst, _pd=pd, k6b_stage3_selected=lambda ss_, b_, s_: None)
    g.update(g_extra)
    exec(compile(ast.Module(body=blk, type_ignores=[]), "<main_cand_block>", "exec"), g)
    return fst


def _toy_screen(rns_keys, variant):
    """合成畫面（⛔ 本案資料）：可建築街廓 B1（區外·名稱以 id 'b1' 存）／B2、B3（皆臨道路 C1）；歸戶 GA 之 y 不配地
    ⇒ 建地軌、原街廓 B1。距離：B3 近於 B2。深度：`f3_alloc_depth_by_label` ＝ B1 40／B2 30／B3 45（⇒ B2 較淺、B3 較深），
    另置誘餌 `f3_block_depth_by_label` ＝ B1 10／B2 50／B3 35（取之則 B3 先於 B2）。
    variant：'a' 基本｜'b' `f3_sb_rows` 之 B2 路寬 6｜'c' `K91_SS_MBA_EFFECTIVE` ＝ B1 100／B2 200／B3 100｜
             'd' 名稱改以 label 存（⛔ 以 id）。"""
    def _t(pid, lot, blk, a, c):
        return {"暫編地號": pid, "原地號": lot, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0,
                "重劃前地價區段": "z", "polygon_coords": _sq(*c)}
    temp = [_t("x", "L1", "B1", 100.0, (0, 0)), _t("y", "L2", "B1", 50.0, (5, 0)),
            _t("q", "L4", "B2", 60.0, (100, 0)), _t("r", "L5", "B3", 60.0, (-100, 0))]
    build = [dict(t) for t in temp]
    gv = [{"暫編地號": "x", "推進側別": "left", "所屬街廓": "B1"}, {"暫編地號": "q", "推進側別": "left", "所屬街廓": "B2"},
          {"暫編地號": "r", "推進側別": "left", "所屬街廓": "B3"},
          {"暫編地號": "B1-抵費地", "推進側別": "抵費地", "所屬街廓": "B1", "cut_coords": _sq(10, 0, 2)},
          {"暫編地號": "B2-抵費地", "推進側別": "抵費地", "所屬街廓": "B2", "cut_coords": _sq(80, 0, 2)},
          {"暫編地號": "B3-抵費地", "推進側別": "抵費地", "所屬街廓": "B3", "cut_coords": _sq(-20, 0, 2)}]
    der = {"B1": {"status": rns_keys["R3_STATUS_OUTSIDE"], "derived": [], "candidates": []},
           "B2": {"status": rns_keys["R3_STATUS_DERIVED"], "derived": ["C1"], "candidates": [{"block": "C1", "ratio": 0.9}]},
           "B3": {"status": rns_keys["R3_STATUS_DERIVED"], "derived": ["C1"], "candidates": [{"block": "C1", "ratio": 0.9}]}}
    ss = {rns_keys["SS_ADJ_BUILD_FINAL"]: build,
          rns_keys["SS_ADJ_DROPPED"]: {("B1", "left"): [{"暫編地號": "y", "G(㎡)": 20.0}]},
          "f3_G_values": gv, "f3L_setback_default": 3.5,
          "t8_ownership_map": {"L1": "GA", "L2": "GA", "L4": "GB", "L5": "GC"},
          rns_keys["SS_FRONT_ROAD_DERIVE"]: der,
          rns_keys["SS_FRONT_ROAD_NAME"]: ({"B1": "外路"} if variant == "d" else {"b1": "外路"}),
          "f3_sb_rows": [{"街廓": "B1", "正面路寬(m)": 8.0}, {"街廓": "B2", "正面路寬(m)": 6.0 if variant == "b" else 8.0},
                         {"街廓": "B3", "正面路寬(m)": 8.0}],
          "f3_alloc_depth_by_label": {"B1": 40.0, "B2": 30.0, "B3": 45.0},
          "f3_block_depth_by_label": {"B1": 10.0, "B2": 50.0, "B3": 35.0},
          rns_keys["K91_SS_MBA_EFFECTIVE"]: ({"B1": 100.0, "B2": 200.0, "B3": 100.0} if variant == "c" else {})}
    extra = {"build_parcels": build, "temp_parcels": temp,
             "classified_blocks": [{"label": "B1", "id": "b1", "category": H}, {"label": "B2", "id": "b2", "category": H},
                                   {"label": "B3", "id": "b3", "category": H},
                                   {"label": "C1", "id": "c1", "category": "道路"}],
             "F3_CATEGORY_BURDEN": {H: "可建築土地", "道路": "共同負擔"}}
    return ss, extra


SCREEN_EXP = {
    "a": "B1（原街廓） → B2 → B3",
    "b": "B1（原街廓） → B3 → B2",
    "c": "B1（原街廓） → B3 → B2（第二趟排除）",
}


def _synth_screen(app_src, mn):
    """`main()` 之候選街廓區塊（自 `_adj359_bf` 之賦值起連續 `2` 句）以假 st ＋ 合成資料實際執行（四變體）。"""
    if mn is None:
        return False, "無 main()"
    blk = _find_main_block(mn)
    if blk is None:
        return False, "抽不到候選街廓區塊"
    bad = []
    for v in ("a", "b", "c", "d"):
        try:
            rns = _screen_ns(app_src)
            ss, extra = _toy_screen(rns, v)
            fst = _exec_block(app_src, blk, ss, extra)
        except Exception as e:  # noqa: BLE001
            bad.append(f"{v}：執行拋 {type(e).__name__}: {e}")
            continue
        dfs = [c[1][0] for c in fst.calls if c[0] == "dataframe"]
        errs = [str(c[1][0]) for c in fst.calls if c[0] == "error"]
        caps = [c[1][0] for c in fst.calls if c[0] == "caption"]
        if v == "d":
            if dfs or len(errs) != 1 or "B1" not in errs[0]:
                bad.append(f"d：期 st.error 一則且列 B1、⛔ 出表（得 error {errs}、表 {len(dfs)}）")
            continue
        ok = not errs and len(dfs) == 2 and len(caps) == 1 and caps[0].startswith("合併單位 1") \
            and list(dfs[0]["歸戶"]) == ["GA"] and list(dfs[0]["候選街廓（依序）"]) == [SCREEN_EXP[v]] \
            and len(dfs[1]) == 3
        if v == "a":
            ok = ok and list(dfs[1]["深度差(m)"]) == ["—", "-10.00", "5.00"] and list(dfs[1]["深度"]) == ["—", "較淺", "較深"]
        if not ok:
            bad.append(f"{v}：得 error {errs[:1]}、表 {len(dfs)}、序 {list(dfs[0]['候選街廓（依序）']) if dfs else None}")
    return (not bad), f"不符 {bad}"


def _wiring_checks(app_src, rv_src):
    res = []
    tree = ast.parse(app_src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    consts = {n.targets[0].id: n for n in tree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    c = consts.get("ADJ_DEPTH_TIE_TOL_M")
    ok1 = c is not None and isinstance(c.value, ast.Constant) and c.value.value == 0.1
    dflt = all(f in top and any(isinstance(d, ast.Name) and d.id == "ADJ_DEPTH_TIE_TOL_M" for d in top[f].args.defaults)
               for f in ("adj_candidate_lists", "adj_candidate_rows"))
    lit = [n.lineno for f in FUNCS if f in top for n in ast.walk(top[f])
           if isinstance(n, ast.Constant) and n.value in (0.1, 0.5) and not isinstance(n.value, bool)]
    res.append(("W1 具名常數 ADJ_DEPTH_TIE_TOL_M ＝ 0.1、二函式之預設引用之、新函式內⛔ 字面 0.1／0.5",
                ok1 and dflt and not lit, f"字面之列 {lit}"))
    fr = consts.get("F3_CATEGORY_FRONT_ROAD")
    bc = consts.get("F3_BLOCK_CATEGORIES")
    ok2 = False
    note2 = ""
    if fr is not None and bc is not None:
        try:
            frv, bcv = ast.literal_eval(fr.value), ast.literal_eval(bc.value)
            ok2 = sorted(frv) == sorted(bcv) and [k for k, v in frv.items() if v is True] == ["道路"] \
                and all(isinstance(v, bool) for v in frv.values())
        except Exception as ex:  # noqa: BLE001
            note2 = f"literal_eval 失敗 {type(ex).__name__}"
    res.append(("W2 類別表 F3_CATEGORY_FRONT_ROAD 之鍵 ＝ F3_BLOCK_CATEGORIES、唯「道路」為真", ok2, note2))
    pc = top.get("parse_cad_precision_layers")
    ok3 = False
    if pc is not None:
        for n in ast.walk(pc):
            if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) \
                    and isinstance(n.targets[0].slice, ast.Constant) \
                    and n.targets[0].slice.value == "front_road_derive" \
                    and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", None) == "r3_front_road_derive":
                a = n.value.args
                if len(a) >= 2 and isinstance(a[1], ast.DictComp):
                    ifs = [cond for g in a[1].generators for cond in g.ifs]
                    notin = any(isinstance(x, ast.Compare) and isinstance(x.ops[0], ast.NotIn)
                                and getattr(x.comparators[0], "id", None) == "_buildable_blocks" for x in ifs)
                    cat = any(isinstance(x, ast.Call) and isinstance(x.func, ast.Attribute) and x.func.attr == "get"
                              and getattr(x.func.value, "id", None) == "F3_CATEGORY_FRONT_ROAD" for x in ifs)
                    ok3 = notin and cat
    res.append(("W3 正面道路推導之候選 ＝ 非可建築（_buildable_blocks 之補集）∩ 類別表為真者", ok3, ""))
    lits, toks, bad_fn = [], [], [f for f in FUNCS if f not in top]
    for f in FUNCS:
        if f not in top:
            continue
        seg = ast.get_source_segment(app_src, top[f]) or ""
        lits += sorted({n.value for n in ast.walk(top[f]) if isinstance(n, ast.Constant)
                        and isinstance(n.value, str) and CASE_LIT_RE.match(n.value)})
        toks += [(f, t) for t in FORBID_TOKS if t in seg]
    res.append(("W4 新函式俱在、⛔ 案件字面、⛔ 讀 session、⛔ 含既有閘所禁之消費字樣", not (lits or toks or bad_fn),
                f"缺 {bad_fn}；案件字面 {lits}；字樣 {toks}"))
    ok5, note5 = _synth_screen(app_src, top.get("main"))
    res.append(("W5 main() 之候選街廓區塊以假 st 實際執行（四變體：深度取 f3_alloc_depth_by_label、路寬取 f3_sb_rows、"
                "最小建築面積取 K91_SS_MBA_EFFECTIVE、名稱以 id 取）",
                ok5, note5))
    rtree = ast.parse(rv_src)
    rtop = {n.name for n in rtree.body if isinstance(n, ast.FunctionDef)}
    rconst = {n.targets[0].id: ast.get_source_segment(rv_src, n) for n in rtree.body if isinstance(n, ast.Assign)
              and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)}
    ok6 = "load_front_road_names" in rtop and "case_front_road_names_UC9898.json" in (rconst.get("FRONT_ROAD_NAMES") or "")
    res.append(("W6 verify/run_verification.py 之 FRONT_ROAD_NAMES ＝ …/case_front_road_names_UC9898.json、"
                "load_front_road_names 在", ok6, ""))
    return res


def wiring(repo):
    app_src = _read(repo, "app.py")
    rv_src = _read(repo, "verify/run_verification.py")
    red = []
    print("── 接線（AST·app.py ＋ verify/run_verification.py）──")
    for name, ok, note in _wiring_checks(app_src, rv_src):
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run ──
def _q2(x):
    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _independent(units, labels, cat, mba, ident, width, depth, g_rows, coords, pool_side, track_build, tol):
    """外部錨：本器另寫之排序（⛔ 呼叫名單之函式）。回 {歸戶: (錨點, [(街廓, 距離, 第二趟排除)])}。"""
    from shapely.geometry import Polygon
    best = {}
    for r in g_rows:
        cs = r.get("cut_coords") or []
        if r.get("推進側別") != pool_side or len(cs) < 3:
            continue
        p = Polygon(cs)
        p = p if p.is_valid else p.buffer(0)
        k = (-p.area, str(r["暫編地號"]))
        b = str(r["所屬街廓"])
        if b not in best or k < best[b][0]:
            best[b] = (k, (p.centroid.x, p.centroid.y))
    pa = {b: v[1] for b, v in best.items()}
    m = {l: _q2(mba.get(l, 0) or 0) for l in labels}
    w = {l: _q2(width[l]) for l in labels}
    dp = {l: _q2(depth[l]) for l in labels}
    lad2 = sorted(set(m.values()))
    lad5 = sorted(set(w.values()), reverse=True)
    T = Decimal(repr(float(tol)))
    out = {}
    for u in units:
        sl = list(u["建築街廓內不能分配"]) + list(u["共同負擔用地"])
        a = min(sl, key=lambda r: (-float(r["原有面積"]), str(r["暫編地號"])))
        p = Polygon(coords[str(a["暫編地號"])])
        p = p if p.is_valid else p.buffer(0)
        ax, ay = p.centroid.x, p.centroid.y
        dist = {l: (_q2(math.hypot(pa[l][0] - ax, pa[l][1] - ay)) if l in pa else None) for l in labels}
        dk = {l: ((0, dist[l]) if dist[l] is not None else (1, Decimal(0))) for l in labels}
        if u["軌"] == track_build:
            s = u["原街廓"]
            keys = {}
            for t in labels:
                if t == s:
                    continue
                d2 = lad2.index(m[t]) - lad2.index(m[s])
                d5 = lad5.index(w[t]) - lad5.index(w[s])
                dd = dp[t] - dp[s]
                r6 = (0, Decimal(0)) if abs(dd) <= T else ((0, -dd) if dd < 0 else (1, dd))
                keys[t] = (int(cat[t] != cat[s]), (0, -d2) if d2 <= 0 else (1, d2), int(ident[t] != ident[s]),
                           int(w[t] != w[s]), (0, d5) if d5 >= 0 else (1, -d5), r6, dk[t], t)
            seq = [s] + sorted(keys, key=keys.get)
            out[u["歸戶"]] = (str(a["暫編地號"]), [(t, dist[t], t != s and keys[t][1][0] == 1) for t in seq])
        else:
            seq = sorted(labels, key=lambda t: (dk[t], t))
            out[u["歸戶"]] = (str(a["暫編地號"]), [(t, dist[t], False) for t in seq])
    return out


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        ns, fake_st = _harvest(repo)
        miss = [n for n in FUNCS + CONSTS if n not in ns]
        if miss:
            print(f"  🔴 受詞缺：{miss}")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        if not hasattr(rv, "load_front_road_names"):
            print("  🔴 受詞缺：run_verification.load_front_road_names")
            print("⇒ 紅 ['受詞缺']；rc 1")
            return 1
        app_src = _read(repo, "app.py")
        mn = next((n for n in ast.parse(app_src).body if isinstance(n, ast.FunctionDef) and n.name == "main"), None)
        blk = _find_main_block(mn) if mn is not None else None
        OK = ns["R3_STATUS_DERIVED"]
        for sb in sbs:
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
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            k9 = sg.get("k929_6")
            if k9 is None:
                print(f"🔴 退縮 {sb}：run_step_g 無 k929_6 ⇒ 無從判定")
                return 3
            print(f"══ 退縮 {sb} ══")
            drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            cbl = list(cb_by.values())
            bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cbl}
            bb = sorted((b for b in cbl if bur[b["label"]] == ns["ADJ_BURDEN_BUILD"]), key=lambda b: b["label"])
            labels = [b["label"] for b in bb]
            der = cad.get("front_road_derive") or {}
            # R0 區外道路名稱檔
            names = rv.load_front_road_names()
            need = sorted(l for l in labels if (der.get(l) or {}).get("status") != OK)
            ok0 = sorted(names) == need and len(set(names.values())) == 1
            print(("  ✅" if ok0 else "  🔴") + f" R0 區外道路名稱檔：列 {sorted(names)} ＝ 推導無值者 {need}；"
                  f"同一條（相異名稱 {len(set(names.values()))}）")
            if not ok0:
                red.append(f"R0@{sb}")
            # R1 正面道路推導
            cands = [(l, c["block"], c["category"]) for l in labels for c in (der.get(l) or {}).get("candidates", [])]
            badc = [x for x in cands if ns["F3_CATEGORY_FRONT_ROAD"].get(x[2]) is not True]
            st_now = {l: ((der.get(l) or {}).get("status"), tuple((der.get(l) or {}).get("derived") or [])) for l in labels}
            OUT = ns["R3_STATUS_OUTSIDE"]
            st_350 = {"R1": (OUT, ()), "R2": (OK, ("RD1",)), "R3": (OK, ("RD2",)), "R4": (OUT, ()),
                      "R5": (OK, ("RD2",)), "R6": (OK, ("RD3",))}
            ok1 = not badc and st_now == st_350
            print(("  ✅" if ok1 else "  🔴") + f" R1 正面道路之候選皆「道路」類（{len(cands)} 對·非道路 {badc}）；"
                  f"推導 ＝ W-G.9-350 §一 項 5 之表：{st_now == st_350}")
            if not ok1:
                red.append(f"R1@{sb}")
            # R2 名單 vs 外部錨
            ident = ns["r3_front_road_identifier"](labels, der, names)
            idm = {l: ident[l]["id"] for l in labels}
            prow = {r["街廓"]: r for r in params}
            width = {l: prow[l]["正面路寬(m)"] for l in labels}
            depth = dict(fake_st.session_state.get("f3_alloc_depth_by_label") or {})
            cat = {b["label"]: b.get("category", "") for b in bb}
            coords = {str(t["暫編地號"]): (t.get("polygon_coords") or []) for t in tp3}
            try:
                it = ns["adj_intake"](tp3, k9["build"], sg["g_rows"], drops, own, bur)
                ctx = ns["adj_block_ctx"](labels, cat, {}, idm, width, depth)
                lst = ns["adj_candidate_lists"](it, ctx, ns["adj_pool_anchor"](sg["g_rows"]), coords)
            except RuntimeError as e:
                print(f"  🔴 R2 名單停機：{str(e)[:300]}")
                red.append(f"R2@{sb}")
                continue
            ind = _independent(it["units"], labels, cat, {}, idm, width, depth, sg["g_rows"], coords,
                               ns["ADJ_POOL_SIDE"], ns["ADJ_TRACK_BUILD"], ns["ADJ_DEPTH_TIE_TOL_M"])
            got = {u["歸戶"]: (u["錨點"], [(i["街廓"], i["距離"], i["第二趟排除"]) for i in u["名單"]]) for u in lst}
            dif = sorted(g for g in set(ind) | set(got) if ind.get(g) != got.get(g))
            for u in lst:
                print(f"     {u['歸戶']}｜{u['軌']}｜原街廓 {u['原街廓']}｜錨點 {u['錨點']}｜"
                      + " → ".join(f"{i['街廓']}({'—' if i['距離'] is None else i['距離']})" for i in u["名單"]))
            print(("  ✅" if not dif else "  🔴") + f" R2 名單（{len(got)} 單位）與外部錨逐單位逐序相同：相異 {dif}")
            if dif:
                red.append(f"R2@{sb}")
            # R3 畫面區塊於本案資料
            if blk is None:
                print("  🔴 R3 抽不到畫面之候選街廓區塊")
                red.append(f"R3@{sb}")
            else:
                rns = _screen_ns(app_src)
                ss = {rns["SS_ADJ_BUILD_FINAL"]: k9["build"], rns["SS_ADJ_DROPPED"]: drops, "f3_G_values": sg["g_rows"],
                      "f3L_setback_default": sb, "t8_ownership_map": own, rns["SS_FRONT_ROAD_DERIVE"]: der,
                      rns["SS_FRONT_ROAD_NAME"]: {b["id"]: names[b["label"]] for b in bb if b["label"] in names},
                      "f3_sb_rows": params, "f3_alloc_depth_by_label": depth, rns["K91_SS_MBA_EFFECTIVE"]: {}}
                try:
                    fst = _exec_block(app_src, blk, ss, {"build_parcels": bp3, "temp_parcels": tp3, "classified_blocks": cbl,
                                                         "F3_CATEGORY_BURDEN": ns["F3_CATEGORY_BURDEN"]})
                    dfs = [c[1][0] for c in fst.calls if c[0] == "dataframe"]
                    errs = [str(c[1][0])[:200] for c in fst.calls if c[0] == "error"]
                    view = ns["adj_candidate_rows"](lst)
                    ok3 = not errs and len(dfs) == 2 and dfs[0].to_dict("records") == view["units"] \
                        and dfs[1].to_dict("records") == view["detail"]
                    note = f"error {errs}；表 {len(dfs)}"
                except Exception as e:  # noqa: BLE001
                    ok3, note = False, f"執行拋 {type(e).__name__}: {e}"
                print(("  ✅" if ok3 else "  🔴") + f" R3 畫面區塊於本案資料之二表 ＝ harness 之顯示列（{note}）")
                if not ok3:
                    red.append(f"R3@{sb}")
            # R4 K-9-52 ③ 之可見效果
            six = [u for u in lst if u["軌"] == ns["ADJ_TRACK_BUILD"] and u["原街廓"] == "R6"]
            l05 = ns["adj_candidate_lists"]({"units": [u0 for u0 in it["units"] if u0.get("原街廓") == "R6"]}, ctx,
                                            ns["adj_pool_anchor"](sg["g_rows"]), coords, tol=0.5)
            s01 = sorted({tuple(i["街廓"] for i in u["名單"]) for u in six})
            s05 = sorted({tuple(i["街廓"] for i in u["名單"]) for u in l05})
            ok4 = bool(six) and s01 == [("R6", "R2", "R3", "R5", "R1", "R4")] and s05 == [("R6", "R5", "R2", "R3", "R1", "R4")]
            print(("  ✅" if ok4 else "  🔴") + f" R4 原街廓 R6 之建地軌 {len(six)} 單位：0.1 ⇒ {s01}；0.5 ⇒ {s05}")
            if not ok4:
                red.append(f"R4@{sb}")
            # R5 公設軌
            pub = [u for u in lst if u["軌"] != ns["ADJ_TRACK_BUILD"]]
            ok5 = all(sorted(i["街廓"] for i in u["名單"]) == labels
                      and all(u["名單"][k]["距離"] <= u["名單"][k + 1]["距離"] for k in range(len(u["名單"]) - 1))
                      for u in pub)
            print(("  ✅" if ok5 else "  🔴") + f" R5 公設軌 {len(pub)} 單位：名單 ＝ 全部可建築街廓、距離不減")
            if not ok5:
                red.append(f"R5@{sb}")
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
        return wiring(repo)
    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
    return run(repo, sbs)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `J1`（新檔 `verify/case_front_road_names_UC9898.json`）

````json
{
 "meta": {
  "case": "UC9898",
  "usage": "驗證路徑（harness）之區外道路名稱；畫面由使用者於步驟 E 之「正面道路名稱／識別符」欄填之",
  "authority": "KL 2026-09-05（R1、R4 臨同一條區外道路·docs/orders/交接文_W-G.9-238.md）；K-9-52 ⑤（通知二·2026-09-29）",
  "note": "名稱只用於比對是否同一條道路；圖推導有值之街廓⛔ 列（推導有值時使用者所填⛔ 採）"
 },
 "names": {
  "R1": "區外道路甲",
  "R4": "區外道路甲"
 }
}
````

## 附錄丙　塊 `K5`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末）

````markdown

---

## 🔧 `K-9-52` 之立（`W-G.9-359`·⛔ 上文一字不刪·純末端追加）

### 🔒 `K-9-52`　**五級八鍵之 `r3`／`r5`／`r6`：正面道路只限「道路」類之街廓；「次一級路寬」以本區各街廓正面路寬之相異值由寬而窄逐級往下，較原街廓寬者排在全部較窄者之後、兩趟皆不排除；深度相差 `0.1 m` 以內視為同深，只用於候選街廓之先後，增配資格仍不設容差**（KL 裁 `2026-09-29`·canonical·**逐字**）

**編號之由**（`W-G.9-359 §零-1`）：`K-9-52` 於開工態 `1841914` 之宣告框與鬆框皆 `0` ⇒ 取之；`K-9-44`／`K-9-47` 仍為缺號。
**出處**：發單側窗五十六（`2026-09-29`）；問一、問二各附示意圖一張（`問一附圖_正面線沿廣場.png`、`問二附圖_次一級路寬.png`·⛔ 入倉）。

**發單側所呈（逐字·⛔ 增刪一字）**：

> **問一【域問·需您判斷】正面道路是否只限「道路」類街廓**（附圖一）
>
> 【現況】程式判定各街廓之正面道路時，凡沿其正面線過半之非建地街廓都算。道路以外，公園、廣場、綠地、學校、市場等也算。`350` 曾以技術語通知此讀法，當時未明言含公園、廣場。
>
> 【要改成】只有分類為「道路」之街廓才算正面道路。正面線沿公園、廣場等者，比照區外道路處理，由您於畫面填正面道路名稱。
>
> 【對土地的影響】
> - **本案**：配地、街角、抵費地皆不變。R2、R3、R5、R6 沿區內道路，R1、R4 沿區外道路，六街廓之正面線都沒有沿公園 G1（重疊 `0` m）。
> - **他案**：以附圖一為例，B、C 隔著廣場臨道路甲。
>   - 現行把「廣場 P」當成 B、C 之正面道路，所以 A 與 B、C 不算臨相同道路。
>   - 改後由您填「道路甲」，A、B、C 即臨相同道路，調配時互相排在前面。
>
> 【要你判斷】正面道路只限「道路」類之街廓，是否？
>
> **問二【域問·需您判斷】「次一級路寬」之排法，及路寬較寬之街廓排在哪裡**（附圖二）
>
> 【現況】第（五）項「次一級路寬」已裁為往小（`2026-09-05`），但有二事未定：
> - 「級」是指本區實有之各種路寬，還是畸零地附表之路寬級距。
> - 候選街廓之路寬比原街廓寬時，排在哪裡。
>
> 【要改成】
> - **分級**：以本區各街廓正面路寬之相異值為級，由寬而窄逐級往下排。依據為塭仔圳簡報第 `24` 頁之例（30 → 20 → 15 m）。
> - **較寬者**：排在全部較窄者之後，再依級由近而遠。路寬只定先後、不淘汰（您 `2026-09-05` 所裁），所以第一趟、第二趟都不排除。
>
> 【對土地的影響】
> - **本案**：配地、街角、抵費地皆不變。本案只有 8 m（R2、R3、R5、R6）與 12 m（R1、R4）兩種路寬，比「相同路寬」時已分出先後，用不到本項。
> - **他案**：有三種以上路寬時才有差。以附圖二為例，若改採畸零地附表之級距，10、8、15 m 與 12 m 同屬一級。此時 15 m 之 T5 可能排在 8 m 之 T3 之前。
>
> 【要你判斷】「次一級路寬」照上開二點辦理，是否？（若否，請示知是否改採畸零地附表之路寬級距，或其他排法。）
>
> **通知三則**（皆非域判斷；無異議即照辦）
>
> 1. **深度 0.5 m 之容差**：以原街廓之深度為準，相差 0.5 m 以內者視為同深，再以距離定先後。超過 0.5 m 者，較淺者在前（差愈小愈前），較深者在後。此即 `9/23` 附問所述之五級做法。
> 2. **驗證程式（無畫面）中 R1、R4 之正面道路名稱**：您已裁 R1、R4 臨同一條區外道路，所以另立一個小資料檔，代入同一名稱。此名只用來比對是否同一條道路，不出現在任何表冊；既有之案件參數檔不動。
> 3. **正面道路未填名者**（區外或判不出，而畫面未填）：程式停下，列出須填名之街廓，不自行假設。

**KL 之答（`2026-09-29 22:38`·逐字·⛔ 增刪一字）**：

> 1. 問一：是
> 2. 問二：是
> 3. 如何確認沒有設環境變數 WV_K6_STEP0、WV_K6B_STAGE3、WV_K929_6 ?
> 4. 深度比較改成以 0.1 m 之容差

（第 `3` 點為操作之詢問，非裁；發單側已於對話答之。）

**發單側之補問（逐字·同日）**：

> **補問一則【域問·需您判斷】0.1 m 是否也用於增配資格**
>
> 【現況】您 9/23 裁定：增配之比較（深度淺於原街廓者才得增配）不設容差。
> 【要改成】（不改）0.1 m 只用於調配時候選街廓之先後，增配資格仍不設容差。
> 【對土地的影響】二者只在深度差 0.1 m 以內時有別。本案只有 R1、R4 相差 0.04 m（33.15／33.11 m）：
> - 增配也設 0.1 m：原街廓為 R1 者，不能以「深度較淺」為由增配到 R4；「地價較低」一款另計。
> - 不設：可以。
> 【要你判斷】0.1 m 只用於候選街廓之先後，增配資格維持不設容差，是否？

**KL 之答（`2026-09-29 22:49`·逐字）**：

> 補問一則：是

**裁之內容**：
① **正面道路只限「道路」類之街廓**（問一「是」）：五級八鍵 `r3` 之正面道路之幾何推導，其候選 ＝ 非可建築土地之街廓中類別為「道路」者；正面線沿公園、廣場、綠地等非道路之公共設施街廓者，其推導為區外（或歧義），由使用者於步驟 E 之「正面道路名稱／識別符」欄填名（`v3` 五級③「區外道路清單只填推導之空缺」照舊）。
② **「次一級路寬」**（問二「是」）：級 ＝ 本區各可建築街廓之正面路寬之相異值，由寬而窄排列；自原街廓之路寬逐級往窄排；**較原街廓寬者排在全部較窄者之後**，再依級由近而遠；第一趟、第二趟皆**⛔ 排除**（`r3`〜`r5` 為排名條件、⛔ 淘汰條件·KL `2026-09-05`）。
③ **深度之容差 ＝ `0.1 m`**（第 `4` 點·改通知一之 `0.5 m`）：以原街廓之深度為準，相差 `0.1 m` 以內（含）者視為同深，同深者再以距離定先後；超過者，較淺者在前（差愈小愈前），較深者在後（差愈小愈前）。
④ **③ 只用於候選街廓之先後**（補問「是」）：增配資格（深度淺於原街廓 ∪ 重劃後地價低於原街廓）仍依 `K-9-46` 其二第 `2` 點**⛔ 設容差**。
⑤ 通知二、三（驗證路徑之區外道路名稱另立一檔、快照⛔ 動；正面道路未填名者停機並列出須填之街廓）KL 未駁。

**射程**：① 〜 ④ 及於**任一案件**；⛔ 及於增配之選塊（`v3` §7-5 第2梯·最佳化）、手冊道路五則、公設軌之距離優先。

**發單側之讀法**（⛔ 充裁·【工】）：
1. **深度** ＝ 與 `region_min` 同一入口之街廓分配深度（`K-9-46` 其二·`§六-6`·畫面得逐街廓覆寫）；深度與其差皆以四捨五入至 `0.01 m` 之值計（`ROUND_HALF_UP`）。
2. **路寬**、**最小建築面積**亦以四捨五入至 `0.01` 之值比較；最小建築面積之級（`K-9-1` ⑨ 裁甲）含 `0`（無規定·最小值）。
3. **距離**（`r7`）＝ 合併單位之暫定錨點（`v3` §7-4：重劃前面積最大之一筆·並列取暫編地號小者）之質心，至候選街廓之抵費地中面積最大之一片之質心（KL 質心起迄法·`verify/wf_f4.py` 之定錨）之直線距離，四捨五入至 `0.01 m`；無抵費地之街廓排在同鍵者之後。
4. 建地軌之名單自原街廓起（原街廓居首·⛔ 排序）；公設軌（無原街廓）之名單 ＝ 全部可建築街廓依距離。
5. 名單只定先後；容量之判、增配、現金補償皆屬其後各步（規格步 `4`〜`6`）。

**本案之後果**（發單側窗五十六·態 `1841914` ＋ 原型·harness·退縮 `3.5 m`／`0 m`）：
- ① 正面道路之推導⛔ 變（候選皆「道路」類；公園 `G1` 與任一正面線之重疊皆 `0`）：`R2` ＝ `RD1`；`R3`、`R5` ＝ `RD2`；`R6` ＝ `RD3`；`R1`、`R4` ＝ 區外。
- ② 本案唯 `8 m`／`12 m` 二種路寬 ⇒ ⛔ 觸。
- ③ 原街廓為 `R6` 之建地軌單位（`G009`、`G032`）之名單由 `R6、R5、R2、R3、R1、R4`（`0.5 m`：`R5` 較 `R6` 深 `0.20 m` ⇒ 同深）改為 `R6、R2、R3、R5、R1、R4`（`0.1 m` ⇒ `R5` 較深）；其餘單位之名單⛔ 變。
- 名單於本批**僅顯示**（⛔ 消費端）⇒ 配地、街角、抵費地皆⛔ 變。

**落地狀態**：① 〜 ③ 與讀法 `1`〜`5` ＝ `W-G.9-359` 工項二（側支 `verify/W-G.9-359-cand`·harness ＋ 畫面）；入主線 ⬜（另候 KL 放行）；名單之消費（規格步 `4`〜`6`）⬜。
````

## 附錄丁　塊 `P13`（附於 `CLAUDE.md` 之末）

````markdown

---

## 🔧 待落地清單之更新：調配之候選街廓名單（規格步 `3`·五級八鍵·`K-9-52`）＋ 正面道路只限「道路」類 ＋ 驗證路徑之區外道路名稱 入側支（`W-G.9-359`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 側支 `verify/W-G.9-359-cand`（本批新立·起於主線 `1841914ea4a89e8b2714100a0f5831fec5d3e3dd`）；主線⛔ 動。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-52` ①（正面道路只限「道路」類） | 類別表 `F3_CATEGORY_FRONT_ROAD`（鍵 ＝ `F3_BLOCK_CATEGORIES`·唯「道路」為真）；`parse_cad_precision_layers` 之正面道路推導之候選 ＝ 非可建築 ∩ 類別表為真者 | 🔶（側支） | `docs/orders/W-G.9-359_規格單.md` |
| `2` | 驗證路徑之區外道路名稱（`K-9-52` ⑤·通知二） | `verify/case_front_road_names_UC9898.json`（`R1`／`R4` 同一名稱）＋ `verify/run_verification.py` 之 `FRONT_ROAD_NAMES`／`load_front_road_names`；快照⛔ 動 | 🔶（側支） | 同上 |
| `3` | 規格步 `3` 候選街廓名單（五級八鍵·`K-9-52` ②③④·讀法 `1`〜`5`） | `adj_q2`／`adj_block_ctx`／`adj_pool_anchor`／`adj_candidate_lists`／`adj_candidate_rows`；畫面成果區「🧭 調配之候選街廓名單」（僅排序·⛔ 消費端）；正面道路未填名者停機並列出 | 🔶（側支） | 同上 |
| `4` | 以程式字樣為錨之接線檢查及其突變（規格單流程·復驗時補寫） | 序 `1`〜`3` 之落點 | ⬜ | 次單 |
| `5` | 入主線 ＋ 主 checkout 之同步 | — | ⬜（候 KL 放行） | 次單 |
| `6` | 名單之消費（規格步 `4` 同歸戶合併〔第一趟〕→ `5` 末端塊與中間調配池〔第二趟〕→ `6` ½ 之判） | 第二趟排除最小建築面積往大者（`v3` 五級③ `r2`） | ⬜ | 規格步 `4`〜`6` |
| `7` | 畫面所填之正面道路名稱只存於該次工作階段（重啟須再填） | — | ⬜ | 畫面批 |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：新調配模組之首環（調配之輸入盤點）＋ 新調配模組之單序（`W-G.9-351`）」節序 `3`（規格步 `3`）⇒ 🔶（本表序 `3`）；其所列三前置——harness 之區外道路名稱之來源 ⇒ 本表序 `2`；候選之類別 ⇒ `K-9-52` ①（本表序 `1`）；畫面所填名稱只存於工作階段 ⇒ 本表序 `7`。「待落地清單之更新：正面道路識別符（…）（`W-G.9-350`）」節序 `3`（harness 之區外道路名稱之來源）⇒ 🔶（本表序 `2`）、序 `4`（`r3` 之消費）⇒ 🔶（本表序 `3`·僅排序）。
🔒 **本案之量**（發單側窗五十六·態 `1841914` ＋ 原型·harness）：合併單位 退縮 `3.5 m` ＝ `23`（建地軌 `15`·公設軌 `8`）、`0 m` ＝ `24`（`16`·`8`）；正面道路之推導⛔ 變；`K-9-52` ③ 使原街廓 `R6` 之 `2` 單位之名單改為 `R6、R2、R3、R5、R1、R4`；名單僅顯示 ⇒ 配地⛔ 變（其驗 ＝ `W-G.9-359` 之 `V-2`〜`V-5`）。
🔒 **依賴序**：本批（側支）→ 序 `4`／`5`（次單·零生產碼 ＋ 入主線）→ 規格步 `4` → `5`（其前置之附圖另呈）→ `6` → `7`／`8`；`GB-194` 三停機款觸發時逐案呈核；併行：畫面批（`GB-187`〜`192` ＋ Streamlit 升級 ＋ `W-G.9-357` 節序 `7` ＋ 本表序 `7`）。
🔒 **本機介面**（入主線並同步後）：成果區於「🧩 調配階段之輸入」之下多「🧭 調配之候選街廓名單」一區；步驟 E 須先填 `R1`、`R4` 之正面道路名稱（同一名稱）並按「✅ 儲存路寬資料」，否則該區以紅字列出須填名之街廓。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `8`（子字串框·含圖例與本列）·列 ＝ `6`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

## 附錄戊　塊 `V1`（附於 `docs/配地計算總規格_v3.md` 之末）

````markdown

---

## 🔧 五級八鍵之 `r3`／`r5`／`r6` 之**補充與更正標記**（`K-9-52`·KL 裁 `2026-09-29`·`W-G.9-359`·⛔ 上文一字不刪·純末端追加）

🛑 **本節⛔ 鑄任何號**——其為補充與更正標記（`戒 36`）；裁之正文 ＝ `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之 `K-9-52`（逐字）。**⛔ 回改上文「🔧 §7-1 級1/2/3 與 §7-4 之區位順序改採「五級（八鍵詞典序）」」節一字**；自本節起，該節 ③ 之 `r3`／`r5`／`r6` 以下列為準：

- **`r3` 正面道路**（補充）：幾何推導之候選唯類別為「道路」之街廓；正面線沿公園、廣場、綠地等非道路之公共設施街廓者，其推導為區外（或歧義），由區外道路清單（使用者所填之名稱）補其空缺。
- **`r5` 路寬級距**（補充）：級 ＝ 本區各可建築街廓之正面路寬之相異值，由寬而窄排列；自原街廓之路寬逐級往窄；**較原街廓寬者排在全部較窄者之後**（再依級由近而遠）；兩趟皆⛔ 排除。**⛔ 以畸零地附表之路寬級距為級**。
- **`r6` 深度**（**更正**）：容差 ＝ 具名常數 **`0.1 m`**（上文「⛔ 字面 `0.5`」之 `0.5` **停止適用**）；以原街廓之深度為準，相差 `0.1 m` 以內（含）視為同深（同深者由 `r7` 定先後）；超過者，較淺者按 `|Δ深度|` 升序在前、較深者按 `|Δ深度|` 升序在後（同上文之編碼）。
- **增配**（上文 ⑤·§7-5 第2梯）之資格⛔ 受 `r6` 之容差影響：仍為嚴格比較、⛔ 設容差（`K-9-46` 其二第 `2` 點·`K-9-52` ④）。
````

SELF_SHA256: c57431273edfef313aa8a7174417fe7523766712260c1910e269b16cf8c7a8b4
