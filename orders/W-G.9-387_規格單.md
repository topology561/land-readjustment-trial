# `W-G.9-387`　規格單：`K-9-61` ⑧ 之落地（合併單位之原街廓之擇：各街廓之分不到之土地之應分配面積之加總較大者 → 相同〔`0.01 ㎡`〕⇒ 重劃前面積之合計較大者 → 再同 ⇒ 最小之暫編地號較小者·⛔ 停機·KL 補裁 `2026-10-17 14:55` 第 `1` 點、`15:23`「甲」）＋ 段三後處理 (a)（所鄰之已配得街廓恰一者）之受詞（不論地號·採現行·⛔ 改碼）之入典 ＋ `ops/queue` 之規則檔之登記 ＋ 待落地清單之更新（新側支 `verify/W-G.9-387-k961h`）

> **本單建議等級 ＝ `high`**（生產碼 `1` 檔：`app.py` 之 `adj_intake` 一函式之內之改·頂層之新名 `0`·`§三-2`；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-17`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本·工項零〜四之一切 `commit` 推至**新側支 `verify/W-G.9-387-k961h`**，其起點 ＝ 主線之端 `34736ab`）。
> **流程 ＝ 規格單**（常態）：**生產碼由執行端依 `§三` 撰寫**；發單端給規格（`§三`）、量測器（塊 `Fy38`·執行端⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py` 之 blob（由執行端回報、發單端復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `1` 檔之一函式；**本案之配地⛔ 變**〔`§一` 項 `5`〕）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）；遠端 heads **`46`**（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-387-k961h`（工項零立之·其後皆快轉）；主線⛔ 動**（入主線另以短單·`§四-2`）。
> 🔑 **通則** ＝ `ops/queue` 之 `README_自動化運作規則.md` 第六節（雲端·Linux）：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之**絕對路徑**；`<O>` ＝ 執行端自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）；`commit` 訊息一律 `git commit -F`；含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8；Bash 命令⛔ 含 heredoc。塊 `Fy38`／`K29`／`P40` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ 遠端分支 `ops/queue` 之 `orders/W-G.9-387_規格單.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python3 -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限** ＝ README 第六節第 `3` 款：各驗之命令之同時並行數 ≤ **`2`**；逾時或 `rc` ≠ 期者，於⛔ 他負載之下**重跑一次**，二趟之出艙皆照實入報告（重跑之趟 ＝ 期 ⇒ 該呼叫以重跑之趟為準·報告具名之）。
> 🔑 **撰碼中之自跑**：執行端撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之 `adj_intake` 以外之一字（含其餘一切頂層節點、`k967_rank`、`k967_pre_area`、`adj_q2`、`adj_intake_rows`、`adj_candidate_lists`）；`adj_intake` 內 `§三-1` 所列以外之一字；生產碼 `34` 檔之其餘 `33` 檔（`verify/` 頂層之 `*.py`）；`§三-3` 之禁改；既有量測器除塊 `Fy38` 所改之 `4` 檔外之一字；`data/` 之一切檔、`verify/case_params_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、`GB` 簿、自誤簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`K-6` 典、`CLAUDE.md` 除塊 `K29`／`P40` 之純末端追加外之一字；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；任何他側支之推送、刪除或改寫；`K-9-61` ①〜⑥、`GB-205`、`K-9-59`、`K-9-60`、`K-9-62` 之指配、`K-9-63`——另單。
> 🔴 **本單⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本單未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量與本機之核數（`nproc`）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`；`git ls-remote --heads origin` 之列數 ＝ **`46`**（全列存 `<O>/heads_before_387.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-387-k961h`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 623 622` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `608`／`MAX` `623`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（發單端於 `34736ab` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝之出艙存 `<O>`）；量測之殼之旗標之出艙 ＝ 單首 🔑 之期。

### `§零-1`　取號現查（宣告框）

**本批⛔ 鑄號**（`自誤`、`GB`、`VR`、`K-9` 皆⛔ 鑄；`K-6` 典之本節之二、三 ＝ 既有之 `K-9-61` 之 KL 補裁·其號⛔ 變）。

**塊名、新名**（母體 ＝ 開工態 `34736ab` 之追蹤檔 **`2880`** 檔·`git grep -l`／`git grep -h … | wc -l` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fy38`、`P40`（逐名） | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取 |
| `K29` | `0`／`0` | `5`／`5` | 🟢 可取（諸列皆量測器之項名〔`F23` 之 `K29` 等〕·⛔ 塊名） |
| 對照甲［必非零］`Fy37` | `2`／`11` | — | 🟢 框非恆空 |
| 對照甲［必非零］`K28` | `1`／`12` | — | 🟢 框非恆空 |
| 對照甲［必非零］`P39` | `1`／`3` | — | 🟢 框非恆空 |
| 報告名 `W-G.9-387R`、新側支之名 `W-G.9-387-k961h`、本單名 `W-G.9-387_規格單`、新器 `probe_WG9387_k961h`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |

量測器之新檔名 `F31`（`verify/probes/probe_WG9387_k961h.py`）。收工閘 `6`／`7` 以之驗（自誤 `MAX` ＝ `623`·⛔ 變）。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `34736ab`，或遠端 heads ≠ `46`、或已含 `refs/heads/verify/W-G.9-387-k961h`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期，或 `§零-0` 項 `5` 之環境於安裝後仍不能匯入 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本單不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy38`／`K29`／`P40` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy38` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或執行端須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-387-k961h`（工項零〜四）或 `ops/queue`（回報）；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之二簿（`K-6` 典、`CLAUDE.md`）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | 執行端作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或執行端認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 |
| `13` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能 |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁：停機上呈之全文寫入 `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`（`result` ＝ `停機上呈`）；已推至新側支之 `commit` ⛔ 撤。

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python3 verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單端實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單端自倉實跑·雲端 Linux·倉外工作樹·殼無 `WV_`·Python `3.11.17`·`shapely 2.2.0`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）；遠端 heads **`46`**；追蹤檔 `2880`（`git ls-tree -r 34736ab \| wc -l`）；`app.py` ＝ `cfd66e889f23a502792bec3ddf0fb9c875ec7524`；`K-6` 典 ＝ `6f502cd8cca1f617beb5b9345325aef22a75b251`（`829153` B）；`CLAUDE.md` ＝ `0b36e0d292941ea380d1b5dc40718081680ec6d5`（`415049` B）；自誤簿 ＝ `c78a429da9822c0d4dfaae47b62b74d31d1ef9b8`（`1203451` B·本批⛔ 動）；`probe_WG9270_closegate.py 623 622 .` ⇒ `rc 0`（對照 `624 623` ⇒ `rc 7`）；`probe_WG9321_issuer_anchor.py … 623 622` ⇒ `rc 0`（`§零-0` 項 `3` 之值）；本批所改之 `4` 器之施前 blob ＝ `§五-1` 項 `2` |
| `2` | 受詞（`34736ab`·`app.py` 之 `adj_intake`） | 合併單位（`K-9-45`（一））之中有建築街廓內不能分配之土地（類 `ADJ_DISP_POOL`·`_pool`）者，其原街廓：`_basis` ＝ `{所屬街廓: Σ 應分配面積}`（`所屬單元` 相同之列唯計一次·其街廓 ＝ 首見之列之 `所屬街廓`）；`_top ＝ max(_basis.values())`；`_cands` ＝ 與 `_top` 之差 ≤ `_EPS`（`1e-9`）之街廓；`len(_cands) != 1` ⇒ `RuntimeError`「【未裁】歸戶 … 之原街廓：應分配面積並列 … ⇒ 停機（⛔ 自裁）」；否則 `_home ＝ _cands[0]`。`原街廓之據` ＝ `_basis`。`git grep -c -F` 於 `app.py`（列框）：「之原街廓：應分配面積並列」`1`、「k967_rank(」`9`、「float(_r['原有面積'])」`1` |
| `3` | 工項一之端（`34736ab` ＋ 塊 `Fy38`·倉外實跑） | `§四-1` 之 `58` 呼叫（`V-1`〜`V-2`）與前置 `3` 之六呼叫於工項一之端：`58` 呼叫中 `55` 呼叫 `rc 0`（末列 ＝ `§五-1` 之「項 `8` 之表」之工項一之端）、`3` 呼叫 `rc 1` ＝ 前置 `1`（`F31 selftest`／`F31 wiring`／`F10 selftest`·末列逐字見該處）；`F31 run` 於工項一之端 `rc 0`（本案⛔ 遇並列 ⇒ 舊碼與新式同值·`§一` 項 `5`）；前置 `3` 之六呼叫皆 `rc 0`；諸呼叫之 `stderr` 合計 `0` B |
| `4` | 原型（發單端·倉外·`34736ab` ＋ 塊 `Fy38` ＋ `§三` 之一實作·⛔ 為執行端之期） | 原型之 `app.py` ＝ `afa7e5a760a3723bb9514ba0106bda8b378310b1`（`1842706` B·對開工態 `+10`／`-7`·唯 `adj_intake` 之內）——⛔ 為期；頂層節點之相異（AST）＝ `{adj_intake}`；頂層之名之集⛔ 變。`64` 呼叫（`V-1`〜`V-2` 之 `58` 與 `V-4`〜`V-6` 之 `run`／`parity` 之六·同 `§四-1` 之命令）於原型皆 `rc 0`，其末列 ＝ `§五-1` 之「項 `8` 之表」之施後之列；諸器之 `stderr` 合計 `0` B。`F31 selftest` 之 `K1`〜`K18` 之期值皆發單端依 `§三-1` `R-1` 手算（各例之註）、原型實得與之逐值同。🔒 撰原型中 `F23 wiring` 之 `W8`／`F24 wiring` 之 `W7` 紅一次：原型之初稿以字面 `float(_r['原有面積'])` 累加重劃前面積——該字面為 `F10` 之突變 `M1` 之換入之字樣（`verify/probes/` 之字串常數·於基準恰一見〔`adj_candidate_lists` 之錨點〕）⇒ 二見 ⇒ 紅；改書之後綠（`§三-3` 之 `2`）。`F10 selftest`／`wiring`、`F18 wiring` 於原型之初（未改器）紅（`adj_intake` 呼 `k967_rank`，二器之抽出⛔ 含之 ⇒ `NameError`）⇒ 塊 `Fy38` 增其抽出之名 |
| `5` | 本案之量（主線之端與原型·二退縮） | **主線之端**（`probe_WG9351_intake.py run`·`34736ab`）：合併單位 `17`（建地軌 `9`·公設軌 `8`）；建地軌之原街廓之據跨二街廓者三——`G011`（`3.5 m` `R2 3.81`／`R3 92.46`；`0 m` `R2 3.81`／`R3 88.63`）⇒ `R3`；`G025`（`R5 0.99`／`R6 0.26`·二退縮）⇒ `R5`；`G030`（`3.5 m` `R2 27.55`／`R3 28.34` ⇒ `R3`；`0 m` `R2 27.55`／`R3 24.88` ⇒ `R2`）；其差皆 ≫ `0.01 ㎡` ⇒ 新式之 ① 即定之 ⇒ **原街廓⛔ 變**（`F31 run` 之 `R3` 之外部錨 ＝ 此諸值·`17` 單位全列）。**二態之對拍**（前態 ＝ 工項一之端、後態 ＝ 原型·二退縮）：`k6s3 cmp` 二退縮皆 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 之落檔與 `stdout` 前後逐位同（發單端之二樹之 `HEAD` 皆 `34736ab`·⛔ 須正規化）、末列皆 `⇒ rc 0（不符 0 項）`——配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`；`F31 run` 之 `R2`／`R3` 二退縮皆 ✅（`G011` ⇒ `R3`、`G025` ⇒ `R5`、`G030` ⇒ `R3`〔`3.5 m`〕／`R2`〔`0 m`〕）；十二呼叫之 `stderr` 合計 `0` B ⇒ **配地⛔ 變**（`V-4`〜`V-6`） |
| `6` | 判別力（發單端·倉外·原型之上逐一施一突變） | （一）`F31 selftest`（新碼之突變·錨 ＝ 原型之字樣·⛔ 入器〔受單側之碼異〕）十五種皆捕：M1 逐位比（⛔ 以 `0.01 ㎡`）⇒ `K3`／`K17`；M2 逐筆之最大（請示之乙）⇒ `K6`／`K12`；M3 重劃前面積以分攤登記面積 ⇒ `K9`／`K18`；M4 代表取重劃前面積最大之一筆（請示之一之乙）⇒ `K5`；M5 取最大之暫編地號 ⇒ `K5`／`K15`；M6 並列 ⇒ 停機（舊）⇒ `K2`／`K5`／`K8`／`K9`／`K10`／`K11`／`K13`／`K15`〜`K18`；M7 差 ≤ `0.01` 即同 ⇒ `K4`／`K17`；M8 合併單元之 `G` 逐片計 ⇒ `K7`；M9 重劃前面積唯計單元之自身之片 ⇒ `K8`；M10 街廓內以數值取最小之暫編地號 ⇒ `K15`；M11 重劃前面積先於 `G` ⇒ `K1`／`K4`／`K7`／`K10`；M12 街廓間以數值比暫編地號 ⇒ `K13`；M13 重劃前面積逐筆先捨後加 ⇒ `K16`；M14 重劃前面積逐位比（`G` 仍以 `0.01 ㎡`）⇒ `K17`；M15 重劃前面積⛔ 扣入池閘之帳 ⇒ `K18`。🔒 `K16`〜`K18` 與 M13〜M15 係定稿前另一唯讀審查者（發單端所派·⛔ 參與撰寫）之所揭（其二突變於初稿之 `K1`〜`K15` 全綠）而補；同審所揭之他項——`R-1` 之「⛔ 增 `raise`」之明文、`§三-3` 之 `3` 之巢狀之許、`F10` 之外部錨於入池閘之帳之片亦扣段三部分併出、塊 `K29` 之三之射程之限（KL 問二唯答所鄰恰一之情形）與四之【工】之歸類——皆已入本單（二）`F31 wiring`：開工態（舊碼）⇒ `X1`／`X2` 紅（`X3`〜`X5` 綠）；`X3` 之判別力：頂層增一輔助函式之原型之變體 ⇒ 紅（`⇒ 紅 ['X3']；rc 1`）；`X5`：改 `verify/selection_pipeline.py` 一字之變體 ⇒ 紅（`⇒ 紅 ['X5']；rc 1`）。（三）`F31 run`：其 `R2` 之外部錨（本器另寫之三鍵）與 `R3`（主線之端之值）於工項一之端（舊碼）與原型皆綠——本案⛔ 遇並列，舊新之碼於本案同值（項 `5`）；其判別力：令 `EXPECT_RUN` 之 `G030`@`0.0` 為 `R3` 之變體 ⇒ `R3@0.0` 紅（`⇒ 紅 ['R3@0.0']；rc 1`·`R2` 仍 ✅）。（四）`F10`：塊 `Fy38` 之後之 `selftest` 於工項一之端（舊碼）⇒ `S6` 紅（舊碼之並列停機）、原型 ⇒ 綠 |
| `7` | `run_all` | ⛔ 跑（單首之「級」·`§四-1` 工項二之「⛔ 跑之由」） |

---

## `§二`　KL 之語與射程

🔒 **所據**：`CLAUDE.md` 待落地清單「`W-G.9-384` 入主線；……（`W-G.9-385`）」節之序 `9`（`K-9-59`〜`K-9-61`、`K-9-63`）與「……（`W-G.9-386`）」節（其序之先後由發單端定之）；`K-6` 典 `K-9-61`（`2026-10-06 01:29`·其 ⑧）、`K-9-46`（三）、`K-9-67`、`K-9-48` 讀法 `3`、`K-9-73`；`ops/queue` 之 `KL答覆/2026-10-17_1240.md`（KL「丙」·先序 `9` 與序 `8`·先後由發單端定）、`KL答覆/2026-10-17_1455.md`、`KL答覆/2026-10-17_1523.md`。

🔒 **KL 之語**（逐字·全文與所問見塊 `K29` 之一）：
- `2026-10-17 12:40`：「丙：先做序 9（K-9-59～61、63）與序 8（GB-205）的落地，先後由發單端依依賴決定；K-9-38／40 附圖與調配後半排在其後；最小建築面積統一取值暫緩。」
- `2026-10-17 14:55` 第 `1` 點（⇒ `K-9-61` ⑧ 之補裁之要旨：原街廓取應分配面積〔原投影位置之 `G`〕最大者；`G` 相同再比重劃前面積；再相同依分不到土地中暫編地號最小者）、第 `2` 點（⇒ 段三後處理 (a)〔所鄰之已配得街廓恰一者〕採現行·不論地號；所鄰二以上或零者之受詞⛔ 及·塊 `K29` 之三）。
- `2026-10-17 15:23`：「甲」（⇒ 應分配面積為各街廓之分不到之土地之**加總**·⛔ 逐筆）。

🔒 **授權**（自動化之委任·`K-6` 典 `W-G.9-386` 之節之一之 KL 逐字）：KL `2026-10-17 07:23` 第 `3` 點「……新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」；`07:58`「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」。本單 ＝ 待落地清單上已有 KL 裁示之項目（`K-6` 典 `W-G.9-386` 之節之二之甲之 ①）。**`expects_allocation_change` ＝ `false`**（`§一` 項 `5`）——執行端之量得本案配地有任一改變 ⇒ 停機款 `6`。

🔒 **【工】之讀法**（塊 `K29` 之四·以交付之通知告 KL）：甲「相同」之單位 ＝ `0.01 ㎡`（`k967_rank`）；乙 重劃前面積 ＝ 調配之輸入之 `原有面積`；丙 暫編地號以字典序；丁 「原街廓之據」之顯示⛔ 變；戊 他處之擇宗⛔ 動。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由執行端逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支；`(c)` ⛔ 及主線（入主線另以短單·`§四-2`）、他側支、`data/` 之資料檔、`K-9-61` ①〜⑥、`GB-205`、`K-9-59`、`K-9-60`、`K-9-62` 之指配、`K-9-63`、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）。

---

## `§三`　規格（執行端依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**（皆 `adj_intake` 之內·`34736ab`）：
- 「**該歸戶之池列**」＝ 該歸戶之列之中類為 `ADJ_DISP_POOL` 者（既有之 `_pool`·順序 ＝ 既有）。
- 「**候選街廓**」＝ 既有之 `_basis` 之鍵（＝ 池列之 `所屬街廓` 之集·`§一` 項 `2`）。
- 「**街廓之 `G`**」＝ 既有之 `_basis[街廓]`（其式⛔ 改）。
- 「**街廓之重劃前面積**」＝ Σ（池列之中 `所屬街廓` ＝ 該街廓者之 `原有面積`）——每一池列各計一次（同一合併單元之諸成員皆計·⛔ 依 `所屬單元` 去重）。
- 「**街廓之最小暫編地號**」＝ 池列之中 `所屬街廓` ＝ 該街廓者之 `暫編地號`（字串）之最小者（字串之比）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | `adj_intake` 之原街廓之擇（既有之 `_top`、`_cands`、`len(_cands) != 1` 之 `raise`、`_home = _cands[0]` 之四句） | 去之，代以：**原街廓 ＝ 候選街廓之中使 `k967_rank(街廓之 G, 街廓之重劃前面積, 街廓之最小暫編地號)` 最小者**（`k967_rank` ＝ 既有之頂層函式·其回 `(−adj_q2(g), −adj_q2(面積), str(暫編地號))`·⛔ 改之、⛔ 另寫其等價）。⛔ 停機（三鍵之後必唯一：諸街廓之最小暫編地號互異）；**⛔ 增任何 `raise`（含防禦式之斷言）**——`F31 wiring` 之 `X2` 判 `adj_intake` 內訊息及於「原街廓」之 `raise` 為紅。`_basis` 之建之迴圈（`_seen` 與其 `float(_r['應分配面積'])` 之累加）⛔ 改一字；`原街廓之據` 仍 ＝ `_basis`；回傳之鍵、各單位之鍵⛔ 增減。 |
| `R-2` | `adj_intake` 之 docstring | 「停機」之列舉去「原街廓之應分配面積並列（【未裁】）」；增一註（形如既有之 `🔧 \`W-G.9-3xx\`` 之註）載 `R-1` 之三鍵與「⛔ 停機」。其餘之文⛔ 改。 |
| `R-3` | 其餘 | `app.py` 之 `adj_intake` 以外之一字⛔ 動；`adj_intake` 內 `R-1`、`R-2` 以外之一字⛔ 動（`_EPS` 之定義與其他之用⛔ 動）。新增之區域名⛔ 與 `adj_intake` 內既有之名同（以 `387` 為尾之名為宜）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F31`（`verify/probes/probe_WG9387_k961h.py`·新）：`selftest` 之 `K1`〜`K18`（`R-1`）；`wiring <repo> 34736ab` 之 `X1`〜`X5`（`R-1`、`R-3`）；`run` 之 `R1`〜`R3`（本案·二退縮）。
- `F10`（`probe_WG9351_intake.py`）：抽出增 `k967_rank`、`adj_q2`（`ADJ_DEPS387`）；`S6` 之期 ⇒ 重劃前面積較大之街廓；突變 `M4`（其錨 `if len(_cands) != 1:` 已去）去之；`run` 之外部錨之原街廓依 `R-1` 之三鍵另寫。`F17`（`probe_WG9358_k948_wiring.py`）：`X4` 去第四字樣（同錨）。`F18`（`probe_WG9359_cand.py`）：`_screen_ns` 之抽出增 `k967_rank`。`F30`（`probe_WG9385_k974.py`）：`W7` 之許增 `adj_intake`。
- `app.py` 之頂層節點對 `34736ab` 相異者 ＝ `{adj_intake}`；頂層之名之集⛔ 變；`verify/` 之生產碼⛔ 改。

### `§三-3`　禁改（既有閘之錨·執行端撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **突變之錨**（`F27 mutate`、`F25 mutate`、`F19 mut`、`F22 mut`、`F10 selftest` 之 `M1`〜`M3`）：其錨所在之句⛔ 動——`adj_intake` 內之 `float(_r['應分配面積'])`、`if _pool or (_cm and not _al):`、`if '段三併出' in t:` 各仍恰一見（`F10` `M1`〜`M3`、`F17` `X4`）。
2. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（字串常數之值〔⛔ 含外層之引號〕以**子字串**計）——🔒 **新碼⛔ 含字面 `float(_r['原有面積'])`**（`F10` `M1` 之換入之字樣·於基準恰一見〔`adj_candidate_lists`〕·`§一` 項 `4`）；基準中恰一之函式名（含巢狀）於工作樹仍恰一 ⇒ 新之巢狀 `def`／`lambda` 之名⛔ 用既有之名。執行端撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
3. **頂層之名之許**（`F23 wiring` 之 `W7`、`F24 wiring` 之 `W5`、`F25 wiring` 之 `X2`、`F30 wiring` 之 `W7`、`F31 wiring` 之 `X3`）：頂層之相異唯 `adj_intake`、⛔ 新名（頂層之輔助函式⛔ 立；巢狀之 `def`／`lambda` 可·其名依 `2`；`k967_rank` 直呼之）。
4. **⛔ 案件字面**（`F31 wiring` 之 `X4`、`F10 wiring` 之 `W1`）：`adj_intake` 之字串常數⛔ 合 `^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$`。
5. **抽出之受詞**（`F10`、`F18`、`F31` 以 AST 自 `app.py` 抽 `adj_intake` 於隔離之命名空間執行·其所許之他名唯 `ADJ_*`／`SS_ADJ_*` 常數、`adj_intake_rows`、`k967_rank`、`adj_q2`〔`F18` 另有其 `FUNCS` 等〕）：`adj_intake` 之新碼⛔ 呼叫此外之模組層之名（`min`、`sorted` 等內建除外）。
6. `F17 wiring` 之 `W10` 之他項、`F10 wiring` 之 `W2`〜`W5`、`F18 wiring` 之 `W5`、`F27 wiring` 之 `Y1`〜`Y9`、`F29 wiring` 之 `Y1`〜`Y11` 之接線之項⛔ 觸。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`K-9-61` ⑧ 之補裁（KL `2026-10-17 14:55` 第 `1` 點、`15:23`「甲」）已定；其落地之讀法 ＝ 塊 `K29` 之四（【工】·以交付之通知告 KL）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地或諸紀錄有任一改變；本案之任一合併單位之原街廓 ≠ `F31 run` 之 `EXPECT_RUN`；`R-1` 之式於某形無從定之（例：池列之 `原有面積` 缺或非數）。

### `§三-5`　執行端之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-3`）：落於何處、其字樣；對 `§三-3` 各款之自查。另附 `git diff <工項一之端> <工項二之 commit> -- app.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-387-k961h`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-387_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-387 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-387-k961h`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`47`**、主線仍 ＝ `34736ab…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-387-k961h`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy38` 抽為 `<O>/Fy38.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`5` 檔（`4` 改·`1` 新）之 `git hash-object` ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `5` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-387 工項一：量測器（F31 之新器·F10、F17、F18、F30 之改）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`。

**工項二　生產碼**（🔴 `app.py`·執行端依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`）：
1. 紅（末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K2', 'K3', 'K5', 'K8', 'K9', 'K10', 'K11', 'K13', 'K15', 'K16', 'K17', 'K18']；rc 1`；`… wiring <repo> 34736ab` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['X1', 'X2']；rc 1`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['S6 應分配面積並列 ⇒ 重劃前面積較大者']；rc 1`；三呼叫之 `stderr` 皆 `0` B。
2. 綠（**`rc 0`**·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`V-1`／`V-2` 之其餘之 `55` 呼叫（同 `§四-1` 之驗之命令·`F31 run` 含之）。
3. `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_pre_35.json`；同 `0.0` ⇒ `<O>/k6s3_pre_00.json`；`python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_pre_35.json`；同 `0.0` ⇒ `<O>/f8_pre_00.json`；`python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_pre.json`；同 `0.0` ⇒ `<O>/parity00_pre.json`（皆 `rc 0`）。
4. `git grep -c -F "之原街廓：應分配面積並列" -- app.py` ⇒ 出艙恰一列 `app.py:1`；`git grep -c -F "float(_r['原有面積'])" -- app.py` ⇒ 出艙恰一列 `app.py:1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：執行端依 `§三` 撰寫 `app.py` 之改動；`python3 -m py_compile app.py`；`commit` 訊息之首列逐字 `W-G.9-387 工項二：K-9-61 ⑧ 之落地（合併單位之原街廓：應分配面積之加總 → 重劃前面積之合計 → 最小之暫編地號·k967_rank·⛔ 停機）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>/*_post.*`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy38` 所改、所增之器及載之者（`13` 呼叫）：`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`… run <repo>`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`… wiring <repo>`；`… run <repo>`；`python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`；`python3 verify/probes/probe_WG9359_cand.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>`（載 `F18`）；`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`… run <repo>` | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F31 selftest` 之 `K1`〜`K18`、`F31 wiring` 之 `X1`〜`X5`、`F31 run` 之 `R1`〜`R3`（二退縮）皆 ✅ |
| `V-2` | 其餘之 `45` 呼叫（`W-G.9-385` 規格單 `§四-1` 之 `V-1`〜`V-2` 之 `55` 呼叫中上列以外者·其命令逐字見 `§五-1` 之「項 `8` 之表」之 `#1`〜`#55`） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` |
| `V-3` | `V-1`〜`V-2` 之 `58` 呼叫之器之載入 | 本批所改、所增之器 `5` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_post_35.json`；同 `0.0`；`… cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**） |
| `V-5` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_post.json`；同 `0.0` ⇒ `<O>/parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置 `3` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異） |
| `V-6` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_post_35.json`；同 `0.0` ⇒ `<O>/f8_post_00.json`；`git hash-object <O>/f8_pre_35.json <O>/f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`1`**（`app.py`）；其增／刪之數與其 blob 出艙（發單端復驗時自倉重算·⛔ 預載）；`verify/` 之一切檔對工項一之端相異 `0`；`app.py` 之頂層節點之名之集 ＝ 工項一之端之集（AST）；其相異之節點 ＝ `{adj_intake}` |
| `V-8` | `R-1`／`§三-3` 之字樣（`git grep -c -F "<字樣>" -- app.py`·逐一） | 「之原街廓：應分配面積並列」⇒ **無出艙**、`rc 1`；「float(_r['原有面積'])」⇒ `app.py:1`；「float(_r['應分配面積'])」「if _pool or (_cm and not _al):」「if '段三併出' in t:」⇒ 各 `app.py:1`（判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**；逾時之重跑依單首 🔑）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞於本案之配地⛔ 觸（`adj_intake` 之原街廓唯供調配之輸入與候選街廓名單之顯示·本案⛔ 遇並列·`§一` 項 `5`），其「⛔ 變」由 `V-4`〜`V-6` 與 `F31 run`、`F10 run`、`F23 run`、`F24 run`、`F27 run`、`F29 run`、`F16 run` 直接量之。

**唯讀獨立審查**（驗皆符後、推前）：執行端另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：三鍵之序（`G` → 重劃前面積 → 最小暫編地號）、`k967_rank` 之直呼（⛔ 另寫）、`G` 之加總之去重（`所屬單元`）⛔ 動、重劃前面積之母體（每一池列·⛔ 去重·`原有面積`·⛔ `分攤登記面積`）、最小暫編地號之受詞（該街廓之池列·字串）、⛔ 停機、`原街廓之據` ⛔ 變、`§三-3` 之六款；以獨立之合成之例（`F31` 之外·至少一例：三街廓、其中二者之 `G` 之加總以 `0.01 ㎡` 相同而重劃前面積亦同）比 `adj_intake` 與手算；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ 執行端修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-387-k961h`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K29` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `P40` 附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；二檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>/checkidx.py`、`<O>/gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P40` 附後：`python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-387 工項三：K-9-61 ⑧ 之 KL 補裁與段三後處理 (a) 之受詞入典·⑧ 之落地之讀法·ops/queue 規則檔之登記 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-387R_K-9-61之八之落地_執行報告.md` ＋ 同目錄之 `W-G.9-387R_K-9-61之八之落地_app差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之十三呼叫之全文、`V-5` 之正規化之比與其對照、`V-6` 之 `hash-object` 之出艙、`F31 run`／`F10 run` 之全文、`k6s3 cmp` 之全文、`parity` 之末十五列、`64` 呼叫〔`V-1`〜`V-2` 之 `58` ＋ `run`／`parity` 之六〕之 `rc`／`stderr`／耗時／末列之表〔前置與驗二態·重跑者二趟並載〕）；④ 塊之實得（bytes／`sha256`）與二簿之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ 執行端之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **`app.py` 之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**（並行之數）。收工閘之實測值出艙於回報（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-387 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`。其後依 `執行端.md` 丁回報於 `ops/queue`。

### `§四-2`　次單（⛔ 本單之期）

發單端復驗本批（自倉重跑 `V-1`〜`V-9` 與收工閘）⇒ 皆符且本案配地⛔ 變 ⇒ **入主線之短單**（快轉 `34736ab` → 新側支之端·⛔ `--force`·自動化之委任之二之甲·前後值入 `ops/queue` 之 `log.md`）；其後 `W-G.9-388`（段三後處理之五停機·`K-9-61` ①〜④、⑥）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `probe_WG9351_intake.py` `35`／`4`、`probe_WG9358_k948_wiring.py` `2`／`1`、`probe_WG9359_cand.py` `3`／`1`、`probe_WG9385_k974.py` `2`／`1`、`probe_WG9387_k961h.py` `409`／`0`（唯此 `5` 檔）（增／刪）；工項二 ＝ `app.py`（唯此一檔·其數出艙）；工項三 ＝ `K-6` 典 `64`／`0`、`CLAUDE.md` `27`／`0`（唯此二檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `34736ab` | 生產碼相異恰 **`1`**（`app.py`）；`verify/` 之一切檔相異恰 **`5`**（`M` `4`：`probe_WG9351_intake.py`、`probe_WG9358_k948_wiring.py`、`probe_WG9359_cand.py`、`probe_WG9385_k974.py`；`A` `1`：`probe_WG9387_k961h.py`）；本批之新檔（本單、新器、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`11` 檔：本單、`5` 器、`app.py`、`K-6` 典、`CLAUDE.md`、報告二檔） |
| `4` | 二簿之 bytes | `K-6` 典 `829153` → **`837880`**；`CLAUDE.md` `415049` → **`419752`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊；自誤簿、`GB` 簿、`VR` 簿、`.claude/` 對 `34736ab` 相異 `0` |
| `5` | 自限 | 遠端 heads **`47`**；主線 ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（⛔ 變）；`verify/W-G.9-387-k961h` ＝ 工項四之 `commit`，其祖含 `34736ab`；其餘 `46` 列中除 `ops/queue`（回報後可變）外之 `45` 列（含主線）逐列 ＝ `<O>/heads_before_387.txt` 之同列 |
| `6` | `python3 verify/probes/probe_WG9270_closegate.py 623 622 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 624 623 .` ⇒ `rc 7` |
| `7` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 623 622` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零-0` 項 `3` 之值（⛔ 變·本批⛔ 鑄號） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單端已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單端擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 塊 `Fy38` | `32390` B·`sha256` `f7402d06f8364c4552c517f15771d63903cea0dafbbb9af1e3f8c26af2378eaa`·`562` 列（圍欄內全文·末附換行）；抽為 `<O>/Fy38.diff`，`git apply` 於 `verify/probes/` 之 `5` 檔（`4` 改·`1` 新），其施前 blob（B）：`probe_WG9351_intake.py` `26669af87da4efa34150c5c927c77134286c242b`（`32524`）、`probe_WG9358_k948_wiring.py` `6bdc07df94523e29401f935dbef142c6812126b2`（`28996`）、`probe_WG9359_cand.py` `4fb5085ba8ab3581b79359e260586d810047c3f6`（`47743`）、`probe_WG9385_k974.py` `87c8a3883355cd6093efa4e281b47e473c01a769`（`42206`）；`probe_WG9387_k961h.py` 施前⛔ 存 |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K29`／`P40` | 塊 `K29` `8727` B·`sha256` `5ef03ee9ee7b555511bfe7d7564d3cbf581e0057c8f4ab3aa19b9198eca9f83a`·`64` 列；塊 `P40` `4703` B·`sha256` `fecb444b731062bb7ca83c904998355f5aea28a8bdd4aa7f4dd9e2ec867d0381`·`27` 列（皆圍欄內全文·末附換行·首列為空列；`P40` 之 payload 內 `⬜` 之子字串框 `14`·列框 `12`〔塊之自載〕）；附於 `K-6` 典（`829153` B）、`CLAUDE.md`（`415049` B）之末，期末 ＝ `837880`／`419752` B |
| `5` | 寫出後之 blob | 工項一之 `5` 器（`verify/probes/`·B）：`probe_WG9351_intake.py` ＝ `eefa02fd805b7e08a54e64c1eae0e025a2051c38`（`34887`）、`probe_WG9358_k948_wiring.py` ＝ `eafe38c5ac72580c3650197956f6363d986b0fa8`（`29097`）、`probe_WG9359_cand.py` ＝ `37c8f8e842eaba8ae827e0c2bf609e83c11ca43e`（`47911`）、`probe_WG9385_k974.py` ＝ `bbf2fa219730e7318cd2143f76e75614a7911b19`（`42349`）、`probe_WG9387_k961h.py` ＝ `770473fbb6a35768cf799b9a7ddb67a403ffabcf`（`22158`·新）；工項三之二簿：`K-6` 典 ＝ `a880ba93f826ad3ce3bf79c4dfe910fd16c43b0c`（`837880` B）、`CLAUDE.md` ＝ `66e9c07af114da5cbe3eaff30c78008540c2836f`（`419752` B）。🔒 `app.py` 之施後 blob **⛔ 預載**（規格單·由執行端回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-386` 規格單 `§五` 項 `7`） |
| `8` | 量測器之二態（發單端實跑·倉外·雲端 Linux `4` 核） | 見本節末之「項 `8` 之表」（`64` 呼叫·二態之 `rc`／`stderr`／末列）。本表之列皆發單端於上開二態之實跑；`#5`、`#6`、`#31`〜`#33`、`#62`〜`#64` 係 `F31` 之 `K16`〜`K18` 與 `F10` 之外部錨之補（定稿前之唯讀審查之所揭·`§一` 項 `6`）之後以定稿之器重跑之趟；他器於其間⛔ 改 |
| `9` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本單>`·發單端實跑（態 `34736ab`·定稿）：🔴 機械 `0` 項／🟡 提示 `2` 項——`P-4` `:163`（工項二之「施」之 `commit` 訊息·其箭頭係三鍵之序之述 ⇒ **具名豁免**）、`:200`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 改前至改後〔閘 `4`〕⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23351`–`31093`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單端·⛔ `push`） | `git worktree add --detach <S> 34736ab`（拋棄式·雲端 Linux）＋ 本單之定稿（`979` 列·其三塊即附錄甲〜丙）＋ 原型之 `app.py`（代工項二）＋ 報告之替身·五 `commit`（工項零之首列 ＝ 所令逐字；工項一〜四以模擬之首列代之·其後空一列附尾列）：工項零之 blob ＝ 來源；三塊之抽取 ＝ 項 `2`／`4`；`git apply --check` `rc 0`；`5` 器之施後 blob ＝ 項 `5`；工項二 ＝ `app.py` `10`／`7`；二簿之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx`／`gen_fa_index` ＝ 期·逐位同；閘 `1` ＝ 工項零 `979`／`0`、工項一 ＝ 該閘之期、工項二 ＝ 上開、工項三 ＝ 該閘之期、工項四（替身）二檔各 `1`／`0`；閘 `2` ＝ 生產碼相異 `1`、`verify/` 相異 `5`（`M` `4`·`A` `1`）·新檔四之 `git check-ignore -v --no-index` 無命中（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `11` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `6` `rc 0`（判別力 `624 623` ⇒ `rc 7`）；閘 `7` `rc 0`（自誤 `608`／`623`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `76`／`79`·缺號 ＝ `§零-0` 項 `3`）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `3`〜`5` 之實跑逐位同（`5` 器 ＝ 項 `5`、`app.py` ＝ 原型） |

**項 `8` 之表**（`#1`〜`#55` ＝ `W-G.9-385` 規格單 `§四-1` 之 `V-1`〜`V-2` 之 `55` 呼叫〔其序同 `W-G.9-385R` 報告之表〕；`#56`〜`#61` ＝ 前置 `3`／`V-4`〜`V-6` 之 `run`／`parity`〔其落檔之名：工項一之端 ⇒ `_pre`、施後 ⇒ `_post`〕；`#62`〜`#64` ＝ `F31`；格 ＝ `rc`／`stderr` B／末列逐字；耗時（s）見括號·本機並行 `4`·⛔ 為期）：

| # | 命令 | 工項一之端 | 施後（原型） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（109） | `0`／`0`／`⇒ 紅 []；rc 0`（117） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（402） | `0`／`0`／`⇒ 紅 []；rc 0`（408） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（31） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（31） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（33） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（12） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（204） | `0`／`0`／`⇒ 紅 []；rc 0`（212） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（66） | `0`／`0`／`⇒ 紅 []；rc 0`（66） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（488） | `0`／`0`／`⇒ 紅 []；rc 0`（504） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（838） | `0`／`0`／`⇒ 紅 []；rc 0`（832） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（13） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（16） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（131） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（125） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（493） | `0`／`0`／`⇒ 紅 []；rc 0`（488） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1948） | `0`／`0`／`⇒ 紅 []；rc 0`（1944） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（30） | `0`／`0`／`⇒ 紅 []；rc 0`（28） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（20） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（22） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['S6 應分配面積並列 ⇒ 重劃前面積較大者']；rc 1`（16） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（230） | `0`／`0`／`⇒ 紅 []；rc 0`（227） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（319） | `0`／`0`／`⇒ 紅 []；rc 0`（316） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（32） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（30） | `0`／`0`／`⇒ 紅 []；rc 0`（29） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（20） | `0`／`0`／`⇒ 紅 []；rc 0`（18） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（14） | `0`／`0`／`⇒ 紅 []；rc 0`（12） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（10） | `0`／`0`／`⇒ 紅 []；rc 0`（9） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（232） | `0`／`0`／`⇒ 紅 []；rc 0`（231） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（46） | `0`／`0`／`⇒ 紅 []；rc 0`（43） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1011） | `0`／`0`／`⇒ 紅 []；rc 0`（1009） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（181） | `0`／`0`／`⇒ 紅 []；rc 0`（182） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（104） | `0`／`0`／`⇒ 紅 []；rc 0`（105） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（319） | `0`／`0`／`⇒ 紅 []；rc 0`（318） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（10） | `0`／`0`／`紅項 [] 器紅 0`（8） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（323） | `0`／`0`／`⇒ 紅 []；rc 0`（318） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（182） | `0`／`0`／`（JSON 之摘要列·略）`（182） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（130） | `0`／`0`／`（JSON 之摘要列·略）`（130） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（178） | `0`／`0`／`⇒ 紅 []；rc 0`（178） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（132） | `0`／`0`／`⇒ 紅 []；rc 0`（130） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（390） | `0`／`0`／`⇒ rc 0（不符 0 項）`（389） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（275） | `0`／`0`／`⇒ rc 0（不符 0 項）`（275） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['K2', 'K3', 'K5', 'K8', 'K9', 'K10', 'K11', 'K13', 'K15', 'K16', 'K17', 'K18']；rc 1`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `1`／`0`／`⇒ 紅 ['X1', 'X2']；rc 1`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（318） | `0`／`0`／`⇒ 紅 []；rc 0`（318） |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丙` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-387-k961h`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 回報 ⇒ `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`（`執行端.md` 丁）。

---

## 附錄甲　塊 `Fy38`（`git apply` 之差異·`verify/probes/` 之 `5` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9351_intake.py b/verify/probes/probe_WG9351_intake.py
index 26669af..eefa02f 100644
--- a/verify/probes/probe_WG9351_intake.py
+++ b/verify/probes/probe_WG9351_intake.py
@@ -21,6 +21,10 @@
            相同；R4 逐類之切片數與原有面積之和 ＝ 全部切片；R5 入池閘之入池宗（不配地之 build 單元之成員）之數與
            原有面積 ＝ 類「建築街廓內不能分配」者。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
+🔧 `W-G.9-387`（`K-9-61` ⑧·KL 補裁 `2026-10-17 14:55`／`15:23`「甲」·⛔ 上列一字不刪）：原街廓之應分配面積以 `0.01 ㎡` 為單位
+  相同者，取重劃前面積之合計較大者，再同取分不到之土地中最小之暫編地號較小者（`k967_rank`·⛔ 停機）——抽出另含
+  `k967_rank`、`adj_q2`（`ADJ_DEPS387`）；S6 之期改為重劃前面積較大之街廓；突變 M4（並列⛔ 停機）去之（其錨已去·新碼之判別力
+  由 F31 量之）；run 之外部錨（R3）之原街廓依上開三鍵另寫。
 """
 import ast, contextlib, io, os, re, sys
 
@@ -30,6 +34,7 @@ except Exception:
     pass
 
 ADJ_FUNCS = ["adj_intake", "adj_intake_rows"]
+ADJ_DEPS387 = ["k967_rank", "adj_q2"]   # 🔧 `W-G.9-387`：`adj_intake` 所呼之函式（抽出用·⛔ 入 ADJ_FUNCS 之他判）
 ADJ_KEYS = ["f3_k929_6_build", "f3_k929_6_dropped"]
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 
@@ -44,7 +49,7 @@ def _extract_ns(src):
     tree = ast.parse(src)
     parts = []
     for node in tree.body:
-        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS:
+        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS + ADJ_DEPS387:
             parts.append(ast.get_source_segment(src, node))
         elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                 and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
@@ -109,7 +114,8 @@ def _cases(ns):
     run("S5 原街廓 ＝ 應分配面積較大者（⛔ 原有面積）",
         lambda: I(temp2, b2, [], d2, own, BUR)["units"][0]["原街廓"], "B2")
     d2t = {("B1", "left"): [{"暫編地號": "u", "G(㎡)": 25.0}], ("B2", "right"): [{"暫編地號": "v", "G(㎡)": 25.0}]}
-    run("S6 應分配面積並列 ⇒ loud", lambda: I(temp2, b2, [], d2t, own, BUR), ("例外", "RuntimeError"))
+    # 🔧 `W-G.9-387`（`K-9-61` ⑧）：應分配面積並列（25／25）⇒ 重劃前面積之合計較大者（u 100 對 v 40）⇒ B1（⛔ 停機）
+    run("S6 應分配面積並列 ⇒ 重劃前面積較大者", lambda: I(temp2, b2, [], d2t, own, BUR)["units"][0]["原街廓"], "B1")
     # 入池閘之合併單元：入池（不配地）與留置（配地）
     temp3 = [_t("m1", "L5", "B1", 60.0), _t("m2", "L6", "B1", 30.0), _t("k1", "L7", "B2", 70.0)]
     b3 = [dict(temp3[0], 入池閘併入=["m1", "m2"]), dict(temp3[2])]
@@ -188,7 +194,6 @@ def selftest(repo):
         ("M1 原街廓改以原有面積比", "float(_r['應分配面積'])", "float(_r['原有面積'])"),
         ("M2 兼有配地者⛔ 成單位", "if _pool or (_cm and not _al):", "if (_pool and not _al) or (_cm and not _al):"),
         ("M3 段三所併出者當共同負擔", "if '段三併出' in t:", "if False:"),
-        ("M4 並列⛔ 停機", "if len(_cands) != 1:", "if len(_cands) < 1:"),
     ]
     for mname, a, b in muts:
         if src.count(a) != 1:
@@ -411,6 +416,11 @@ def wiring(repo):
     return 1 if red else 0
 
 
+def _q2_387(x):
+    from decimal import Decimal, ROUND_HALF_UP
+    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
+
+
 def _independent(tp3, bfin, rows, drops, own, bur):
     """外部錨：本器另寫之分類（⛔ 呼叫 adj_intake）。回 ({暫編: 類名}, {歸戶: (軌, 原街廓, 成員)})。"""
     alloc = {str(r["暫編地號"]) for r in rows if r.get("推進側別") in ("left", "right")}
@@ -422,11 +432,24 @@ def _independent(tp3, bfin, rows, drops, own, bur):
         for m in u.get("入池閘併入") or [u["暫編地號"]]:
             mem[str(m)] = str(u["暫編地號"])
     kind, owner, s3 = {}, {}, set()
+    # 🔧 `W-G.9-387`：重劃前面積 ＝ 分攤登記面積 − 段三部分併出之和 − 入池閘之帳（build 之宗之自身與其成員）
+    po = {}
+    for u in bfin:
+        if u.get("_is_ghost_sliver"):
+            continue
+        if u.get("入池閘部分併出"):
+            po[str(u["暫編地號"])] = po.get(str(u["暫編地號"]), 0.0) + sum(float(v) for v in u["入池閘部分併出"].values())
+        for m, d in (u.get("入池閘成員部分併出") or {}).items():
+            po[str(m)] = po.get(str(m), 0.0) + sum(float(v) for v in (d or {}).values())
+    pre = {}
     for t in tp3:
         if t.get("_is_ghost_sliver"):
             continue
         k = str(t["暫編地號"])
         owner[k] = own[str(t["原地號"])]
+        # 入池閘之帳者（W-G.9-375）恆扣段三部分併出；否則唯段三併出非空者（W-G.9-373）扣之
+        pre[k] = float(t.get("分攤登記面積_m2", 0) or 0) - po.get(k, 0.0) - (
+            sum(float(v) for v in (t.get("段三部分併出") or {}).values()) if (k in po or t.get("段三併出")) else 0.0)
         # 🔧 `W-G.9-363`（發單側窗六十四·⛔ 下列一字不刪）：帶 段三餘量 而其值 ＞ 0 之片（段三或手冊先行之剩下）⇒
         #   恆入合併單位（`W-G.9-357`）——其歸戶無入池之宗而有配地者，另成公設軌之單位（`adj_intake` 之 `_s3`）
         if float(t.get("段三餘量", 0) or 0) > 0:
@@ -450,7 +473,15 @@ def _independent(tp3, bfin, rows, drops, own, bur):
             bl = {}
             for u in {mem[k] for k in ks if kind[k] == "池"}:
                 bl[dg[u][0]] = bl.get(dg[u][0], 0.0) + dg[u][1]
-            units[g] = ("建", max(bl, key=bl.get), sorted([k for k in ks if kind[k] == "池"] + cm))
+            # 🔧 `W-G.9-387`（`K-9-61` ⑧）：G 之加總（0.01 ㎡）→ 重劃前面積之合計 → 最小之暫編地號（字典序）
+            pa, mn = {}, {}
+            for k in ks:
+                if kind[k] == "池":
+                    b_ = dg[mem[k]][0]
+                    pa[b_] = pa.get(b_, 0.0) + pre[k]
+                    mn[b_] = min(mn.get(b_, k), k)
+            units[g] = ("建", sorted(bl, key=lambda b_: (-_q2_387(bl[b_]), -_q2_387(pa[b_]), mn[b_]))[0],
+                        sorted([k for k in ks if kind[k] == "池"] + cm))
             for k in cm:
                 kind[k] = "公入"
         elif cm and not has_a:
diff --git a/verify/probes/probe_WG9358_k948_wiring.py b/verify/probes/probe_WG9358_k948_wiring.py
index 6bdc07d..eafe38c 100644
--- a/verify/probes/probe_WG9358_k948_wiring.py
+++ b/verify/probes/probe_WG9358_k948_wiring.py
@@ -72,7 +72,8 @@ FN_PT, FN_HCB = "k6b_stage3_pool_temp", "_k6b_callbacks"
 NEST = ("_has357", "_res357", "_max357", "_dist357", "_k951", "_split357", "_t14_357")
 # 🔧 `W-G.9-373`（`K-9-66`）：`_max357`／`_k951`／`_split357` 去之
 NEST = tuple(x for x in NEST if x not in ("_max357", "_k951", "_split357"))
-X4 = ("float(_r['應分配面積'])", "if _pool or (_cm and not _al):", "if '段三併出' in t:", "if len(_cands) != 1:")
+# 🔧 `W-G.9-387`（`K-9-61` ⑧·原街廓之並列⛔ 停機）：去第四字樣（其句已去·新碼由 F31 量之）
+X4 = ("float(_r['應分配面積'])", "if _pool or (_cm and not _al):", "if '段三併出' in t:")
 
 
 def _read(repo, rel):
diff --git a/verify/probes/probe_WG9359_cand.py b/verify/probes/probe_WG9359_cand.py
index 4fb5085..37c8f8e 100644
--- a/verify/probes/probe_WG9359_cand.py
+++ b/verify/probes/probe_WG9359_cand.py
@@ -382,7 +382,9 @@ def _find_main_block(mn):
 
 
 def _screen_ns(app_src):
-    return _extract_ns(app_src, funcs=FUNCS + ["adj_intake", "r3_front_road_identifier", "r3_normalize_road_name"],
+    # 🔧 `W-G.9-387`：`adj_intake` 呼 `k967_rank`（原街廓之擇·`K-9-61` ⑧）⇒ 抽出亦含之
+    return _extract_ns(app_src, funcs=FUNCS + ["adj_intake", "r3_front_road_identifier", "r3_normalize_road_name",
+                                               "k967_rank"],
                        consts=CONSTS + ["SS_FRONT_ROAD_NAME", "SS_FRONT_ROAD_DERIVE", "K91_SS_MBA_EFFECTIVE"],
                        prefixes=("ADJ_", "SS_ADJ_", "R3_STATUS_"))
 
diff --git a/verify/probes/probe_WG9385_k974.py b/verify/probes/probe_WG9385_k974.py
index 87c8a38..bbf2fa2 100644
--- a/verify/probes/probe_WG9385_k974.py
+++ b/verify/probes/probe_WG9385_k974.py
@@ -489,7 +489,8 @@ def wiring(repo, base):
             for ln in difflib.ndiff((btop.get(k) or "").split("\n"), (ctop.get(k) or "").split("\n")):
                 if ln.startswith("- "):
                     dels.append((k, hashlib.sha256(ln[2:].encode("utf-8")).hexdigest()))
-        ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"}
+        # 🔧 `W-G.9-387`：其後之單所改之頂層節點亦許（`adj_intake`·`K-9-61` ⑧·其行為由 F31 量之）
+        ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"}
                and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
         res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
     except Exception as e:
diff --git a/verify/probes/probe_WG9387_k961h.py b/verify/probes/probe_WG9387_k961h.py
new file mode 100644
index 0000000..770473f
--- /dev/null
+++ b/verify/probes/probe_WG9387_k961h.py
@@ -0,0 +1,409 @@
+# -*- coding: utf-8 -*-
+"""W-G.9-387 量測器（發單端擬·檔 F31·⛔ 由受單側改一字）：`K-9-61` ⑧ 之落地——合併單位之原街廓之擇
+（KL 補裁 `2026-10-17 14:55` 第 1 點·`15:23`「甲」）。
+
+所量之性質：同一歸戶之建築街廓內不能分配之土地分處二以上之街廓者，其原街廓 ＝
+  ① 各街廓之分不到之土地之應分配面積（原投影位置之 G·入池閘之合併單元只計一次）之加總較大者；
+  ② ① 以 `0.01 ㎡` 為單位相同者，各街廓之分不到之土地之重劃前面積（`原有面積`·部分併出者為其剩下）之合計較大者；
+  ③ 再相同者，各街廓之分不到之土地中最小之暫編地號（字典序）較小者；
+  ⛔ 停機（三鍵之後必有唯一者）。
+
+子命令（一律 python verify/probes/probe_WG9387_k961h.py <子命令> …）：
+  selftest <repo>
+           合成對照（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `ADJ_*` 常數、`adj_intake`、`adj_intake_rows`、`k967_rank`、
+           `adj_q2`）：K1〜K18（各例之期值皆依上開 ①〜③ 手算·見各例之註）。
+  wiring   <repo> <基準 commit>
+           AST 查接線：X1 `adj_intake` 呼叫 `k967_rank`（`K-9-67` 之序之單一真相源）；X2 `adj_intake` 內⛔ 有其訊息及於
+           原街廓之 `raise`；X3 `app.py` 之頂層節點之名之集對基準⛔ 變、其相異之節點 ⊆ {`adj_intake`}；X4 `adj_intake` 內⛔
+           案件字面；X5 生產碼 `34` 檔中 `app.py` 以外者（`verify/` 頂層之 `*.py`）對基準相異 `0`。
+  run      <repo> [<退縮> …]
+           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 盤點⛔ 停機；R2 每一建地軌之單位之原街廓 ＝ 本器另寫之三鍵之擇
+           （⛔ 呼叫 `k967_rank`／`adj_q2`）；R3 每一合併單位之原街廓 ＝ 外部錨 `EXPECT_RUN`（主線 `34736ab` 之
+           `probe_WG9351_intake.py run` 之出艙·發單端實跑·舊碼之值）——本案⛔ 遇並列 ⇒ 原街廓⛔ 變。
+rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
+"""
+import ast, contextlib, io, os, re, subprocess, sys
+from decimal import Decimal, ROUND_HALF_UP
+
+try:
+    sys.stdout.reconfigure(encoding="utf-8")
+except Exception:
+    pass
+
+FN_AI = "adj_intake"
+EXTRACT_FUNCS = [FN_AI, "adj_intake_rows", "k967_rank", "adj_q2"]
+CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
+# 外部錨（R3）：主線 `34736ab` 之 `probe_WG9351_intake.py run <repo>` 之「單位」列之原街廓（發單端 2026-10-17 實跑）
+EXPECT_RUN = {
+    3.5: {"G003": None, "G004": "R2", "G011": "R3", "G012": None, "G013": None, "G014": "R3", "G015": None,
+          "G016": None, "G018": "R2", "G020": "R2", "G024": None, "G025": "R5", "G028": None, "G030": "R3",
+          "G031": None, "G032": "R6", "G033": "R3"},
+    0.0: {"G003": None, "G004": "R2", "G011": "R3", "G012": None, "G013": None, "G014": "R3", "G015": None,
+          "G016": None, "G018": "R2", "G020": "R2", "G024": None, "G025": "R5", "G028": None, "G030": "R2",
+          "G031": None, "G032": "R6", "G033": "R3"},
+}
+
+
+def _read(repo, rel):
+    with open(os.path.join(repo, rel), encoding="utf-8") as f:
+        return f.read()
+
+
+def _extract_ns(src):
+    tree = ast.parse(src)
+    parts, got = [], set()
+    for node in tree.body:
+        if isinstance(node, ast.FunctionDef) and node.name in EXTRACT_FUNCS:
+            parts.append(ast.get_source_segment(src, node))
+            got.add(node.name)
+        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
+                and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
+            parts.append(ast.get_source_segment(src, node))
+    miss = [f for f in EXTRACT_FUNCS if f not in got]
+    if miss:
+        raise KeyError(f"受詞缺 {miss}")
+    ns = {}
+    exec(compile("\n\n".join(parts), "<k961h_extract>", "exec"), ns)
+    return ns
+
+
+def _t(pid, blk, a, **kw):
+    d = {"暫編地號": pid, "原地號": "L" + pid, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0,
+         "重劃前地價區段": "z"}
+    d.update(kw)
+    return d
+
+
+BUR = {"B1": "可建築土地", "B2": "可建築土地", "B3": "可建築土地", "C1": "共同負擔"}
+
+
+def _case(I, spec, merged=None, extra_temp=(), alloc=()):
+    """spec ＝ [(暫編, 街廓, 原有面積, G)]（G 為 None ⇒ 該片為合併單元之他成員·⛔ 自有不配地紀錄）；皆同一歸戶 GA。
+    merged ＝ {單元: [成員…]}；extra_temp ＝ 另加之切片（配地）；alloc ＝ 配地之 build 單元。回 adj_intake 之結果。"""
+    temp = [_t(p, b, a) for p, b, a, _g in spec] + [dict(x) for x in extra_temp]
+    own = {t["原地號"]: "GA" for t in temp}
+    mem_of = {}
+    for u, ms in (merged or {}).items():
+        for m in ms:
+            mem_of[m] = u
+    build, drops = [], {}
+    for p, b, a, g in spec:
+        if mem_of.get(p, p) != p:
+            continue
+        u = dict(_t(p, b, a))
+        if p in (merged or {}):
+            u["入池閘併入"] = list(merged[p])
+        build.append(u)
+        drops.setdefault((b, "left"), []).append({"暫編地號": p, "G(㎡)": g, "不配地由": "內接矩形"})
+    for x in extra_temp:
+        build.append(dict(x))
+    rows = [{"暫編地號": p, "推進側別": "left"} for p in alloc] + [{"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]
+    return I(temp, build, rows, drops, own, BUR)
+
+
+def _home(I, *a, **k):
+    us = [u for u in _case(I, *a, **k)["units"] if u["歸戶"] == "GA"]
+    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))
+
+
+def _cases(ns):
+    I = ns[FN_AI]
+    out = []
+
+    def run(name, fn, exp):
+        try:
+            got = fn()
+        except Exception as e:  # noqa: BLE001
+            got = ("例外", type(e).__name__)
+        out.append((name, got, exp))
+
+    # K1 ①：G 之加總 10 對 25 ⇒ B2（G 大者·⛔ 重劃前面積〔100 對 40〕）
+    run("K1 G 之加總較大者", lambda: _home(I, [("u1", "B1", 100.0, 10.0), ("v1", "B2", 40.0, 25.0)]), "B2")
+    # K2 ②：G 逐位相同（25／25）⇒ 重劃前面積 100 對 40 ⇒ B1（舊碼 ⇒ 停機）
+    run("K2 G 相同 ⇒ 重劃前面積之合計較大者", lambda: _home(I, [("u1", "B1", 100.0, 25.0), ("v1", "B2", 40.0, 25.0)]), "B1")
+    # K3 ②：G 25.004 對 24.996 ⇒ 以 0.01 ㎡ 為單位皆 25.00（相同）⇒ 重劃前面積 40 對 100 ⇒ B2（逐位比 ⇒ B1）
+    run("K3 G 以 0.01 ㎡ 為單位相同 ⇒ 重劃前面積",
+        lambda: _home(I, [("u1", "B1", 40.0, 25.004), ("v1", "B2", 100.0, 24.996)]), "B2")
+    # K4 ①：G 25.006（⇒ 25.01）對 25.004（⇒ 25.00）⇒ 以 0.01 ㎡ 為單位相異 ⇒ B1（以「差 ≤ 0.01 即同」讀之 ⇒ B2）
+    run("K4 G 以 0.01 ㎡ 為單位相異 ⇒ G", lambda: _home(I, [("u1", "B1", 40.0, 25.006), ("v1", "B2", 100.0, 25.004)]), "B1")
+    # K5 ③（請示之圖一之形）：G 皆 0；重劃前面積 B1 30＋10 ＝ 40、B2 40 ⇒ 相同；最小之暫編地號 B1 p5 對 B2 p7 ⇒ B1
+    #   （以重劃前面積最大之一筆代表〔p9 對 p7〕⇒ B2）
+    run("K5 G、重劃前面積皆同 ⇒ 最小之暫編地號較小者",
+        lambda: _home(I, [("p9", "B1", 30.0, 0.0), ("p5", "B1", 10.0, 0.0), ("p7", "B2", 40.0, 0.0)]), "B1")
+    # K6 ①（請示之圖三之形·KL 答「甲」）：B1 G 20＋15 ＝ 35、B2 G 30 ⇒ B1（逐筆之最大〔20 對 30〕⇒ B2）
+    run("K6 G 逐街廓加總（⛔ 逐筆）",
+        lambda: _home(I, [("x1", "B1", 50.0, 20.0), ("x2", "B1", 50.0, 15.0), ("y1", "B2", 50.0, 30.0)]), "B1")
+    # K7 ①：入池閘之合併單元（m1＋m2·G 40）只計一次；B2 G 50 ⇒ B2（重計 ⇒ 80 ⇒ B1）
+    run("K7 合併單元之 G 只計一次",
+        lambda: _home(I, [("m1", "B1", 60.0, 40.0), ("m2", "B1", 30.0, None), ("k1", "B2", 70.0, 50.0)],
+                      merged={"m1": ["m1", "m2"]}), "B2")
+    # K8 ②：G 皆 40；重劃前面積 B1 ＝ 合併單元之諸成員 60＋30 ＝ 90、B2 70 ⇒ B1（唯計單元之自身之片 60 ⇒ B2）
+    run("K8 合併單元之重劃前面積計其諸成員",
+        lambda: _home(I, [("m1", "B1", 60.0, 40.0), ("m2", "B1", 30.0, None), ("k1", "B2", 70.0, 40.0)],
+                      merged={"m1": ["m1", "m2"]}), "B1")
+    # K9 ②：B1 之 p 分攤登記面積 100、段三部分併出 70（受併宗 r·B3·配地）⇒ 原有面積（剩下）30；B2 之 q 50；G 皆 10
+    #   ⇒ B2（以分攤登記面積 100 比 ⇒ B1）
+    run("K9 重劃前面積 ＝ 原有面積（部分併出之剩下·⛔ 分攤登記面積）", lambda: _k9(I), "B2")
+    # K10 ③：B1 G 10；B2、B3 G 30、重劃前面積 40（相同）；最小之暫編地號 B2 q2、B3 q1 ⇒ B3
+    run("K10 三街廓：二者並列 ⇒ 其後之鍵",
+        lambda: _home(I, [("q0", "B1", 90.0, 10.0), ("q2", "B2", 40.0, 30.0), ("q1", "B3", 40.0, 30.0)]), "B3")
+    # K11 ⛔ 停機：G、重劃前面積皆同之二街廓（K5）⇒ 得一街廓（⛔ 例外）
+    run("K11 皆同 ⇒ ⛔ 停機", lambda: isinstance(_home(I, [("a1", "B1", 40.0, 0.0), ("a2", "B2", 40.0, 0.0)]), str), True)
+    # K12 原街廓之據（顯示）⛔ 變：仍為各街廓之 G 之加總
+    run("K12 原街廓之據 ＝ 各街廓之 G 之加總",
+        lambda: _case(I, [("x1", "B1", 50.0, 20.0), ("x2", "B1", 50.0, 15.0), ("y1", "B2", 50.0, 30.0)])["units"][0]["原街廓之據"],
+        {"B1": 35.0, "B2": 30.0})
+    # K13 ③：字典序（K-9-61 ⑧「暫編地號字典序小者」·`k967_rank` 之 str）：p10 對 p9 ⇒ "p10" < "p9" ⇒ B1
+    run("K13 暫編地號以字典序比", lambda: _home(I, [("p10", "B1", 40.0, 0.0), ("p9", "B2", 40.0, 0.0)]), "B1")
+    # K14 單一街廓 ⇒ 該街廓
+    run("K14 單一街廓", lambda: _home(I, [("s1", "B2", 10.0, 0.0), ("s2", "B2", 5.0, 0.0)]), "B2")
+    # K15 ③：街廓內之最小亦以字典序：B1 {p10, p2} ⇒ "p10"、B2 {p11} ⇒ "p11"；G 皆 0、重劃前面積皆 40 ⇒ B1
+    #   （街廓內以數值取最小 ⇒ B1 之代表 p2 ⇒ "p11" < "p2" ⇒ B2）
+    run("K15 街廓內之最小之暫編地號亦以字典序",
+        lambda: _home(I, [("p10", "B1", 20.0, 0.0), ("p2", "B1", 20.0, 0.0), ("p11", "B2", 40.0, 0.0)]), "B1")
+    # K16 ②（【工】甲：先加後捨）：G 皆 0；B1 之重劃前面積 10.004＋10.004 ＝ 20.008 ⇒ 20.01、B2 20.004 ⇒ 20.00 ⇒ B1
+    #   （逐筆先捨後加 ⇒ 20.00 對 20.00 ⇒ 最小暫編地號 a1 ⇒ B2）
+    run("K16 重劃前面積先加後捨",
+        lambda: _home(I, [("b1", "B1", 10.004, 0.0), ("b2", "B1", 10.004, 0.0), ("a1", "B2", 20.004, 0.0)]), "B1")
+    # K17 ②（0.01 ㎡ 為單位）：G 皆 0；重劃前面積 40.004 對 39.996 ⇒ 皆 40.00（相同）⇒ 最小暫編地號 c2 對 c1 ⇒ B2
+    #   （逐位比 ⇒ B1）
+    run("K17 重劃前面積以 0.01 ㎡ 為單位相同 ⇒ 暫編地號",
+        lambda: _home(I, [("c2", "B1", 40.004, 0.0), ("c1", "B2", 39.996, 0.0)]), "B2")
+    # K18 ②（【工】乙）：B1 之 p 分攤登記面積 100、入池閘部分併出 70（受併宗 r·B3·配地）⇒ 原有面積（剩下）30；
+    #   B2 之 q 50；G 皆 10 ⇒ B2（以分攤登記面積 100 比 ⇒ B1）
+    run("K18 重劃前面積 ＝ 原有面積（入池閘之帳之剩下）", lambda: _k18(I), "B2")
+    return out
+
+
+def _k9(I):
+    p = _t("p", "B1", 100.0, 段三部分併出={"r": 70.0}, 段三併出=["r"])
+    q = _t("q", "B2", 50.0)
+    r = _t("r", "B3", 200.0)
+    temp = [p, q, r]
+    own = {t["原地號"]: "GA" for t in temp}
+    build = [dict(p), dict(q), dict(r)]
+    drops = {("B1", "left"): [{"暫編地號": "p", "G(㎡)": 10.0, "不配地由": "內接矩形"}],
+             ("B2", "left"): [{"暫編地號": "q", "G(㎡)": 10.0, "不配地由": "內接矩形"}]}
+    rows = [{"暫編地號": "r", "推進側別": "left"}, {"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]
+    us = [u for u in I(temp, build, rows, drops, own, BUR)["units"] if u["歸戶"] == "GA"]
+    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))
+
+
+def _k18(I):
+    p = _t("p", "B1", 100.0)
+    q = _t("q", "B2", 50.0)
+    r = _t("r", "B3", 200.0)
+    temp = [p, q, r]
+    own = {t["原地號"]: "GA" for t in temp}
+    build = [dict(p, 入池閘部分併出={"r": 70.0}), dict(q), dict(r)]
+    drops = {("B1", "left"): [{"暫編地號": "p", "G(㎡)": 10.0, "不配地由": "內接矩形"}],
+             ("B2", "left"): [{"暫編地號": "q", "G(㎡)": 10.0, "不配地由": "內接矩形"}]}
+    rows = [{"暫編地號": "r", "推進側別": "left"}, {"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]
+    us = [u for u in I(temp, build, rows, drops, own, BUR)["units"] if u["歸戶"] == "GA"]
+    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))
+
+
+def _report(cases):
+    red = []
+    for name, got, exp in cases:
+        ok = got == exp
+        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
+        if not ok:
+            red.append(name.split()[0])
+    return red
+
+
+def selftest(repo):
+    try:
+        ns = _extract_ns(_read(repo, "app.py"))
+    except Exception as e:  # noqa: BLE001
+        print(f"  🔴 K0 受詞：{type(e).__name__}: {e}")
+        print("⇒ 紅 ['K0']；rc 1")
+        return 1
+    print("── 合成對照（AST 抽出之 adj_intake 等）──")
+    red = _report(_cases(ns))
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def _top(src):
+    out = {}
+    for n in ast.parse(src).body:
+        k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
+            n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
+            else None)
+        if k:
+            out[k] = ast.dump(n)
+    return out
+
+
+def wiring(repo, base):
+    res = []
+    src = _read(repo, "app.py")
+    tree = ast.parse(src)
+    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
+    ai = top.get(FN_AI)
+    if ai is None:
+        print(f"  🔴 X0 受詞缺：{FN_AI}")
+        print("⇒ 紅 ['X0']；rc 1")
+        return 1
+    calls = [n for n in ast.walk(ai) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "k967_rank"]
+    res.append(("X1 adj_intake 呼叫 k967_rank", len(calls) >= 1, f"呼叫 {len(calls)}"))
+    word = "".join(["原", "街廓"])
+    rz = [ast.unparse(n)[:80] for n in ast.walk(ai) if isinstance(n, ast.Raise) and word in ast.unparse(n)]
+    res.append(("X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise", not rz, f"{rz}"))
+    lits = sorted({n.value for n in ast.walk(ai)
+                   if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value)})
+    res.append(("X4 adj_intake 內⛔ 案件字面", not lits, f"{lits}"))
+    try:
+        bsrc = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True,
+                              check=True).stdout.decode("utf-8")
+        bt, ct = _top(bsrc), _top(src)
+        dif = sorted(k for k in set(bt) | set(ct) if bt.get(k) != ct.get(k))
+        ok3 = set(bt) == set(ct) and set(dif) <= {FN_AI}
+        res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", ok3,
+                    f"增 {sorted(set(ct) - set(bt))}／去 {sorted(set(bt) - set(ct))}／相異 {dif}"))
+        ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
+                            check=True).stdout.decode("utf-8").split()
+        prod = sorted(p for p in ls if re.match(r"^verify/[^/]+\.py$", p))
+        chg = []
+        for p in prod:
+            b = subprocess.run(["git", "-C", repo, "show", f"{base}:{p}"], capture_output=True, check=True).stdout
+            try:
+                with open(os.path.join(repo, p), "rb") as f:
+                    c = f.read()
+            except OSError:
+                c = None
+            if b != c:
+                chg.append(p)
+        res.append((f"X5 生產碼 app.py 以外之 {len(prod)} 檔對基準相異 0", not chg and len(prod) >= 1, f"相異 {chg}"))
+    except Exception as e:  # noqa: BLE001
+        res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", False, f"基準讀不到：{type(e).__name__}"))
+    red = []
+    for name, ok, note in sorted(res, key=lambda r_: r_[0].split()[0]):
+        print(("  ✅ " if ok else "  🔴 ") + f"{name}（{note}）")
+        if not ok:
+            red.append(name.split()[0])
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def _q2(x):
+    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
+
+
+def _indep_home(unit):
+    """外部錨：本器另寫之三鍵之擇（⛔ 呼叫 k967_rank／adj_q2）。"""
+    g, a, m, seen = {}, {}, {}, set()
+    for r in unit["建築街廓內不能分配"]:
+        b = r["所屬街廓"]
+        if r["所屬單元"] not in seen:
+            seen.add(r["所屬單元"])
+            g[b] = g.get(b, 0.0) + float(r["應分配面積"])
+        a[b] = a.get(b, 0.0) + float(r["原有面積"])
+        m[b] = min(m.get(b, str(r["暫編地號"])), str(r["暫編地號"]))
+    best = None
+    for b in sorted(g):
+        k = (_q2(g[b]), _q2(a[b]))
+        if best is None or k > best[0] or (k == best[0] and m[b] < best[1]):
+            best = (k, m[b], b)
+    return best[2] if best else None
+
+
+def run(repo, sbs):
+    sys.path.insert(0, os.path.join(repo, "verify"))
+    cwd = os.getcwd()
+    os.chdir(repo)
+    red = []
+    try:
+        from app_harvest import harvest
+        with contextlib.redirect_stdout(io.StringIO()):
+            ns, fake_st = harvest(os.path.join(repo, "app.py"))
+        if FN_AI not in ns:
+            print(f"  🔴 R0 受詞缺：{FN_AI}")
+            print("⇒ 紅 ['R0']；rc 1")
+            return 1
+        import run_verification as rv
+        from selection_pipeline import run_corner_pk_k6b
+        from stepg_pipeline import run_step_g
+        for sb in sbs:
+            with contextlib.redirect_stdout(io.StringIO()):
+                snapshot = rv.load_snapshot()
+                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
+                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
+                v6 = open(rv.V6DXF, "rb").read()
+                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
+                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
+            try:
+                with contextlib.redirect_stdout(io.StringIO()):
+                    _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
+                        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
+                    ns["K917_DROPPED"].clear()
+                    sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
+                                    eff_min_build_by_blk={})
+            except RuntimeError as e:
+                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
+                return 3
+            k9 = sg.get("k929_6")
+            if k9 is None:
+                print(f"🔴 退縮 {sb}：run_step_g 無 k929_6 ⇒ 無從判定")
+                return 3
+            drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
+            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
+            bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
+            print(f"══ 退縮 {sb} ══")
+            try:
+                it = ns[FN_AI](tp3, k9["build"], sg["g_rows"], drops, own, bur)
+            except RuntimeError as e:
+                print(f"  🔴 R1 盤點停機：{str(e)[:300]}")
+                red.append(f"R1@{sb}")
+                continue
+            print("  ✅ R1 盤點⛔ 停機")
+            bad2 = []
+            for u in it["units"]:
+                if not u["建築街廓內不能分配"]:
+                    continue
+                ind = _indep_home(u)
+                blks = sorted({r["所屬街廓"] for r in u["建築街廓內不能分配"]})
+                if len(blks) >= 2:
+                    print(f"     {u['歸戶']}｜原街廓 {u['原街廓']}｜據 "
+                          + "、".join(f"{b} {u['原街廓之據'].get(b, 0.0):.2f}" for b in blks) + f"｜外部錨 {ind}")
+                if ind != u["原街廓"]:
+                    bad2.append((u["歸戶"], u["原街廓"], ind))
+            print(("  ✅" if not bad2 else "  🔴") + f" R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 {bad2}")
+            if bad2:
+                red.append(f"R2@{sb}")
+            exp = EXPECT_RUN.get(sb)
+            got = {u["歸戶"]: u["原街廓"] for u in it["units"]}
+            if exp is None:
+                print(f"  🔴 R3 退縮 {sb} 無外部錨")
+                red.append(f"R3@{sb}")
+                continue
+            dif3 = sorted(g for g in set(exp) | set(got) if exp.get(g, "缺") != got.get(g, "缺"))
+            print(("  ✅" if not dif3 else "  🔴") + f" R3 合併單位（{len(got)}）之原街廓 ＝ 外部錨（{len(exp)}）：相異 {dif3}")
+            if dif3:
+                red.append(f"R3@{sb}")
+    finally:
+        os.chdir(cwd)
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def main(argv):
+    if len(argv) < 3 or argv[1] not in ("selftest", "wiring", "run"):
+        print(__doc__)
+        return 2
+    repo = os.path.abspath(argv[2])
+    if argv[1] == "selftest":
+        return selftest(repo)
+    if argv[1] == "wiring":
+        if len(argv) != 4:
+            print(__doc__)
+            return 2
+        return wiring(repo, argv[3])
+    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
+    return run(repo, sbs)
+
+
+if __name__ == "__main__":
+    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `K29`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

---

## 🔧 `W-G.9-387`：`K-9-61` ⑧ 之 KL 補裁（合併單位之原街廓之擇：應分配面積之加總 → 重劃前面積之合計 → 分不到之土地中最小之暫編地號·KL `2026-10-17 14:55` 第 `1` 點、`15:23`「甲」）；段三後處理 (a)（所鄰之已配得街廓恰一者）之受詞不論地號（KL `2026-10-17 14:55` 第 `2` 點·採現行）；⑧ 之落地之【工】之讀法；`ops/queue` 之規則檔之登記；`K-9-61` 之落地之單之分（⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）之後；本節由 `W-G.9-387`（新側支 `verify/W-G.9-387-k961h`）入典。**授權** ＝ `W-G.9-386` 之節之一之 KL 之逐字（自動化之委任·其二之甲之 ①：待落地清單上已有 KL 裁示之項目）。⛔ 鑄 `K-9` 之號（本節之二、三 ＝ 既有之 `K-9-61` 之 KL 補裁·其號⛔ 變）。

### 一、KL 之語（逐字）與所問

**發單端之請示**（`2026-10-17 14:05`·`ops/queue` 之 `待KL/2026-10-17_K-9-61之二題.md`·其「要你判斷」二則·逐字）：

> 【要你判斷】兩街廓並列時，以哪一筆的暫編地號代表該街廓來比？（甲：該街廓分不到土地中暫編地號最小者／乙：該街廓分不到土地中重劃前面積最大者）
>
> 【要你判斷】段三的這類併入，是否也照 10/13 限同一筆地號？（是：照建議／否：維持現行，不論地號）

**KL** `2026-10-17 14:55`（`Asia/Taipei`·答上開之請示·逐字）：

> 1. 問一：先問你所謂的628-9(1) 30 ㎡、628-5(2) 10 ㎡，在 R4 有 628-7(1) 40 ㎡，這些原面積是指原位次計算的G值，還是重劃前面積？本題我看你要我回答的問題，程式好像未可分配之土地其"應分配面積"就視為0，但是就算不能分配也是有原投影位置先算G值(G值就是指應分配面積)，但因為G值太小導致內接矩形等驗證不過才屬未分配到土地，所以本題應該是往原投影位置計算之應分配面積G值最大者合併，所以原街廓是指應分配面積最大者，若G值相同再比重劃前面積，若重劃前面積再相同，就依分不到土地中暫編地號最小者
> 2. 問二：採現行，原因：街角第是地主最在意的位置(價值高)，所以既然相鄰的街角地有一側已經街角地評選機制為勝者，且若另一側也是經解屌地評選後確定分配不到的情形下(但2側土地相連不論地號，如附圖2)，則採現狀將另一側相連但不能分配的土地併入評選街角地winner土地。

**發單端之續請示**（`2026-10-17 14:58`·`待KL/2026-10-17_K-9-61之二題_續.md`·其「要改成」二則·逐字）：

> **甲（現行之延續）**：各街廓分不到土地的 G 加總後比；相同再比各街廓分不到土地的重劃前面積合計；再相同，比各街廓分不到土地中暫編地號最小者。
> **乙**：逐筆比——分不到土地中 G 最大的那一筆所在之街廓；G 相同再比該筆的重劃前面積；再相同，取暫編地號最小者所在之街廓。

**KL** `2026-10-17 15:23`（`Asia/Taipei`·答上開之續請示·逐字）：

> 甲

### 二、`K-9-61` ⑧ 之 KL 補裁（⛔ 新號）

**合併單位之原街廓**（`K-9-46`（三）·同一歸戶之建築街廓內不能分配之土地分處二以上之街廓者）＝ 依序：
① 各街廓之**分不到之土地之應分配面積**（原投影位置之 `G`）之**加總**較大者；
② ① 相同者，各街廓之分不到之土地之**重劃前面積之合計**較大者；
③ 再相同者，各街廓之分不到之土地中**最小之暫編地號**較小者。
三鍵之後必得唯一之街廓 ⇒ **⛔ 停機**（原「應分配面積並列 ⇒ 停機」之【未裁】去之）。

**與既有正典之關係**：
- `K-9-61` ⑧（`2026-10-06`）之「原有面積合計」⇒ **重劃前面積之合計**（KL 第 `1` 點「若G值相同再比重劃前面積」）；其「暫編地號字典序小者」之受詞 ⇒ **該街廓之分不到之土地中最小之暫編地號**（KL 第 `1` 點「依分不到土地中暫編地號最小者」）。
- `K-9-46`（三）之「取應分配面積較大者」⇒ 逐街廓之**加總**（「甲」·⛔ 逐筆之最大）——與 `W-G.9-351` 以來之現行同。
- `K-9-67`（應分配面積相同 ⇒ 重劃前面積大者 ⇒ 暫編地號小者）——同一順序（本補裁為其於原街廓之適用）。

**射程**：及於**任一案件**。**本案**：建地軌之合併單位中原街廓之據跨二街廓者三（`G011`、`G025`、`G030`·二退縮），其應分配面積之加總之差皆 ≫ `0.01 ㎡` ⇒ 原街廓⛔ 變、配地⛔ 變（`W-G.9-387` 之 `F31 run` 之 `R3`）。

### 三、段三後處理 (a)（所鄰之已配得街廓恰一者）之受詞（KL 第 `2` 點·採現行）

段三（街角合併再試）取得街角之後，同一地主於背靠之另一街廓（⛔ 隔道路·直接相鄰）分不到之建地，其所鄰之已配得街廓**恰一**者（請示之問二之所問·「一般情形」），**不論地號**，整筆併入取得街角之宗（`K-9-48` 讀法 `3`〔`2026-09-23`〕維持；KL 之由：街角地為地主最在意之位置；一側已為評選之勝者、另一側經評選確定分配不到而兩側土地相連者，併入 winner）。**射程之限**：所鄰之已配得街廓為二以上或為零者（`K-9-61` ⑥ 之本文），其受詞——`K-9-73`（`2026-10-13`）之「與既有正典之關係」所載「`K-9-61` ⑥ 之受詞唯同一筆地號」——**本節⛔ 及**（請示之問二明載其為前提而未問；其落地於 `W-G.9-388` 定之，讀法有二而土地後果相異者另呈 KL）。本案⛔ 改碼、配地⛔ 變。

### 四、⑧ 之落地之【工】之讀法（`W-G.9-387`·發單端·⛔ 充裁·以交付之通知告 KL）

- **甲 「相同」之單位**：`0.01 ㎡`（同 `K-9-67` 之【工】）——以 `k967_rank`（`K-9-67` 之序之單一真相源·`adj_q2` 四捨五入至 `0.01` 後比）比之；① 之加總、② 之合計皆先加後捨（⛔ 逐筆捨入後加）。
- **乙 重劃前面積**：調配之輸入（`adj_intake`）之該片之 `原有面積` ＝ 分攤登記面積（段三或入池閘部分併出者 ＝ 其剩下 ＝ 分攤登記面積 − 已併出之量）——與 `K-9-67` 之重劃前面積（`k967_pre_area` 之表之式）同量；其合計及於該街廓之每一分不到之片（入池閘之合併單元之諸成員皆計）。
- **乙之二 應分配面積之加總**：入池閘之合併單元之 `G` 只計一次（其諸成員共一 `G`·`W-G.9-351` 以來之現行）——與乙之「每一片皆計」不對稱，乃因 `G` 屬單元、面積屬片。
- **丙 暫編地號之比**：字典序（字串之比·`K-9-61` ⑧ 原文「字典序」·`k967_rank` 之 `str`）；街廓內之最小與街廓間之比同之。
- **丁 顯示**：「原街廓之據」仍為各街廓之應分配面積之加總（⛔ 增欄）。
- **戊 他處⛔ 動**：候選街廓名單之錨點（重劃前面積最大之一筆·`§7-4`）、入池閘、手冊先行、段三、第一趟之擇宗⛔ 變。

### 五、`ops/queue` 之規則檔之登記（`W-G.9-386` 之節之二之戊）

`W-G.9-386` 之後之修訂（皆⛔ 放寬停止之條件·`ops/queue` 之 `log.md` 記其由）：`README_自動化運作規則.md` 第六節第 `2`、`3` 款（`python3 -m pip`；核數 `2`〜`4`）、第八節第 `3` 款（有事之輪記 `effort`）；`發單端.md` 丙之第 `1` 步（判「全無」前逐序具據·收緊）、己（一輪持續工作至完成）。本節定稿時之 `sha256`：`README_自動化運作規則.md` `9613` B·`fe5be89767192c7ba45bfc4da8c5d6c855b836de3b6c2863408bbe0e411bdf68`；`執行端.md` `3289` B·`5247541c09654988376aeeeef88ce3503412058f1cd7dca38f1b956f91655ee7`；`發單端.md` `8305` B·`de1063793de6511ae9f05379aeac1ba685486b6bf9212b50fbe2e08138ca14b2`；`每日摘要.md` `768` B·`109cc9d5e0c0af604b01191809f19ef58ae8cb272c878f4b0d5797a0ff2f78b5`。

### 六、`K-9-61` 之落地之單之分（工程裁·唯序·⛔ 涉土地後果）

`W-G.9-387` ＝ ⑧（`adj_intake`）；`W-G.9-388` ＝ 段三後處理之五停機（①②③④⑥）；`W-G.9-389` ＝ ⑤ 之還原（`GB-205`·段三、手冊先行、入池閘之受併宗事後未配得者）與試算內之「程式未支援」之停機之上拋；⑦ 已落地（`W-G.9-373`·`k967_rank`）。`K-9-61` 之「落地狀態」⇒ ⑦ ✅（主線）、⑧ 🔶（新側支 `verify/W-G.9-387-k961h`·入主線另單）、①〜⑥ ⬜。
````

## 附錄丙　塊 `P40`（附於 `CLAUDE.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`K-9-61` ⑧ 之 KL 補裁與其落地（新側支）；段三後處理 (a) 之受詞（所鄰恰一者·採現行）；`K-9-61` 之落地之單之分（`W-G.9-387`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）之後；本批之碼在新側支 `verify/W-G.9-387-k961h`。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-61` ⑧ 之 KL 補裁（`2026-10-17 14:55`／`15:23`「甲」） | 合併單位之原街廓 ＝ 各街廓之分不到之土地之應分配面積之加總較大者 → 相同 ⇒ 重劃前面積之合計較大者 → 再同 ⇒ 最小之暫編地號較小者；⛔ 停機（相同之單位 `0.01 ㎡` 等 ＝【工】） | 🔶（新側支·候入主線之短單） | `K-6` 典 `W-G.9-387` 之節之二、四；`docs/orders/W-G.9-387_規格單.md` |
| `2` | 段三後處理 (a)（所鄰之已配得街廓恰一者）之受詞（`2026-10-17 14:55` 第 `2` 點） | 段三取得街角後，背靠之另一街廓相連而分不到之建地不論地號併入 winner（`K-9-48` 讀法 `3` 維持）；⛔ 改碼；所鄰二以上或零者之受詞⛔ 及（序 `6`） | ✅ | `K-6` 典 `W-G.9-387` 之節之三 |
| `3` | `K-9-62` 之指配（前節之前節序 `3`） | 公有土地依類別序指配、抵費地、按比例 | ⬜ | 另單 |
| `4` | harness 之 `blk5` 之最小建築面積（前節之前節序 `6`） | 畫面與 harness 之源之統一 | ⬜ | 另單（⛔ 急·KL `2026-10-17 12:40` 暫緩） |
| `5` | `K-9-78`（前節之前節序 `7`） | 調配之畫面入口 | ⬜ | 新調配程式之規格單（規格步 `5`〜`8`） |
| `6` | `K-9-61` ①〜④、⑥（段三後處理之五停機·前節之前節序 `9` 之一） | 承受宗之擇定（相鄰者先 → 應分配面積 → 重劃前面積 → 暫編地號）、不相連之原位次宗⛔ 動、取得街角之宗未保留 ⇒ 還原續試、所鄰已配得街廓二以上或零 | ⬜ | 落地之單 `W-G.9-388` |
| `7` | `K-9-61` ⑤、`GB-205`（前節之前節序 `8`）；試算內之「程式未支援」之停機被吞為「不過」（⛔ 鑄號） | 已收受道路、公設地上土地之宗事後未配得 ⇒ 還原、依手冊併入同一地主他宗；試算中之未支援之停機上拋 | ⬜ | 落地之單 `W-G.9-389` |
| `8` | `K-9-60`（前節之前節序 `9` 之一） | 末端塊競合三形 | ⬜ | 落地之單 `W-G.9-390` |
| `9` | `K-9-59`、`K-9-63`（前節之前節序 `9` 之一） | 讀圖側（`CENTERLINE`、`JUNCTION`、`JOINLINE`、圓弧、L 形、判側、地籍缺漏警示） | ⬜ | 落地之單 `W-G.9-391`（視規模得再分） |
| `10` | 畫面於 step G 之後再跑段三而未再跑 step G 者之調配之輸入之顯示（前節之前節序 `10`） | 審查者之警示·可達與否未驗·⛔ 鑄號 | ⬜ | 待查（另單·⛔ 急） |
| `11` | 清冊之顯示（前節之前節序 `11`） | 清冊依原地號合併顯示，與配地時之合併不一定相同 | ⬜ | 另單（⛔ 急） |
| `12` | 試算之檢核唯及受影響之街廓（發單端之碼面推論·未實跑證·⛔ 鑄號） | 受影響之街廓外之街廓之保留之失⛔ 被查 | ⬜ | 待查（另單·⛔ 急） |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：`W-G.9-384` 入主線；……（`W-G.9-385`）」節（其序 `2` 之態依「……（`W-G.9-386`）」節為 ✅）之序 `3`、`6`、`7`、`10`、`11` ⇒ 本表序 `3`、`4`、`5`、`10`、`11`（態⛔ 變）；其序 `8` ⇒ 本表序 `7`；其序 `9` ⇒ 本表序 `1`、`2`、`6`〜`9`；其序 `1`、`2`、`4`、`5` ✅ ⇒ 本表⛔ 載。本表序 `12` 為新。
🔒 **本案之量**：本批⛔ 變配地（本案之原街廓⛔ 變·`W-G.9-387` 規格單 `§一` 項 `5`）。
🔒 **依賴序**：序 `1`（入主線之短單）→ 序 `6`（`W-G.9-388`）→ 序 `7`（`W-G.9-389`）→ 序 `8`（`W-G.9-390`）→ 序 `9`（`W-G.9-391`）→ 序 `3` → 規格步 `5` → `6` → `7`／`8`（新調配模組·其畫面入口依序 `5`）；序 `4`、`10`、`11`、`12` 與 `GB-196`、`GB-197`、`GB-198`、`GB-202` 另單（⛔ 急）。先後之定 ＝ 發單端（KL `2026-10-17 12:40`「先後由發單端依依賴決定」）。
🔒 **本機介面**：同前節（⛔ 變）。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `14`（子字串框·含圖例與本列）·列 ＝ `12`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: ffa64ff4f65d96b436d7c54947295651a898cab672f583f0cc0002827618b626
