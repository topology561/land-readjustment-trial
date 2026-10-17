# `W-G.9-387`　規格單：`K-9-61` ⑧ 之 KL 補裁之落地（合併單位之原街廓：各街廓之分不到土地之應分配面積之和 → 重劃前面積之和 → 最小之暫編地號·`k967_rank`；並列之停機去之）＋ 段三後處理 (a) 之讀法之入典（不論地號·碼⛔ 改）＋ 射程之重分 ＋ `ops/queue` 規則檔之修訂之登記 ＋ 自誤 `624`、`625` ＋ 待落地清單之更新（新側支 `verify/W-G.9-387-k961h`）

> **本單建議等級 ＝ `high`**（生產碼 `1` 檔：`app.py` 之 `adj_intake` 一函式·`§三-2`；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單端（自動輪）·`2026-10-17`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本·工項零〜四·**一切 `commit` 推至新側支 `verify/W-G.9-387-k961h`**，其起點 ＝ 主線之端 `34736ab`）。
> **流程 ＝ 規格單**（常態）：**生產碼由執行端依 `§三` 撰寫**；發單端給規格（`§三`）、量測器（塊 `Fy38`·執行端⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之 `app.py` 之 blob（由執行端回報、發單端復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `1` 檔·一函式；**本案之配地⛔ 變**〔`§一` 項 `5`〕）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）；遠端 heads **`46`**（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-387-k961h`（工項零立之·其後皆快轉）；主線⛔ 動**（入主線另以短單·`§四-2`）。
> 🔑 **通則** ＝ `ops/queue` 之 `README_自動化運作規則.md` 第六節（雲端·Linux）：直譯器 `python3`；`<repo>` 及一切路徑引數皆正斜線之絕對路徑；`git commit -F`；含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8；Bash 命令⛔ 含 heredoc；`<O>` ＝ 執行端自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）。塊 `Fy38`／`K29`／`E31`／`P40` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ 遠端分支 `ops/queue` 之 `orders/W-G.9-387_規格單.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python3 -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限**（README 第六節第 `3` 款）：驗之命令之同時並行數 ≤ **`2`**；逾時或 `rc` ≠ 期者，於⛔ 他負載之下**重跑一次**，二趟之出艙皆照實入報告（重跑之趟 ＝ 期 ⇒ 該呼叫以重跑之趟為準·報告具名之）。
> 🔑 **撰碼中之自跑**：執行端撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🛑 **本單⛔ 及於**：主線之任何推進；`app.py` 之頂層節點除 `adj_intake` 外之一字（**頂層之新名⛔ 增**）；`adj_intake` 內除 `§三-1` 所令之二處（原街廓之擇定之段、docstring）外之一字；生產碼 `34` 檔之其餘 `33` 檔（含 `verify/selection_pipeline.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py`）；`k967_rank`、`adj_q2`、`k967_pre_area`、`adj_intake_rows` 之一字；`§三-3` 之禁改；既有量測器除塊 `Fy38` 所改之 `4` 檔外之一字；`data/`、`verify/case_params_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、`GB` 簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/` 之一字；`K-6` 典、自誤簿、`CLAUDE.md` 除塊 `K29`／`E31`／`P40` 之純末端追加外之一字；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；任何他側支之推送、刪除或改寫；`K-9-61` ①〜⑥（段三後處理之五停機、`GB-205`·`W-G.9-388`／`389`）、`K-9-60`、`K-9-59`、`K-9-63`、`K-9-62` 之指配、`K-9-78`、規格步 `5`〜`8`、`GB-196`〜`198`／`202`。
> 🔴 **本單⛔ 令執行端作任何「孰為正典」「應改為」之判**；**域上之未定 ⇒ 停機上呈、⛔ 自裁**（`§三-4`）。**量測器紅而須改量測器始能過 ⇒ 停機、⛔ 改器**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量與本機之核數（`nproc`）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`；`git ls-remote --heads origin` 之列數 ＝ **`46`**（全列存 `<O>/heads_before_387.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-387-k961h`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 623 622` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `608`／`MAX` `623`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（發單端於 `34736ab` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝之出艙存 `<O>`）。

### `§零-1`　取號現查（宣告框）

**本批所鑄之號**（意指占用·母體 ＝ 開工態 `34736ab` 之追蹤檔 **`2880`** 檔·列框；發單端以 `git grep -c`〔`-P "(?<![0-9\-])<號>(?![0-9])"`／`-F "自誤 <號>"`／`` -F "自誤 `<號>`" ``／`` -F "`自誤 <號>`" ``〕於 `34736ab` 實算）：

| 號 | 裸（錨定）列 | 平形 | B 形 | C 形 | 判 |
|---|---|---|---|---|---|
| `自誤 624` | `54` | `0` | `0` | `0` | 🟢 可取（裸列皆數字之偶合——`sha256`／blob 之子字串、行號、量測之值等） |
| `自誤 625` | `34` | `0` | `0` | `0` | 🟢 可取（同上） |
| 對照甲［必非零］`自誤 623` | — | `7` | — | `7` | 🟢 框非恆空 |

**塊名、新名**（母體同上·檔框／列框·`git grep -l`／`git grep -c` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fy38`、`E31`、`P40`（逐名） | 皆 `0`／`0` | 皆 `0`／`0` | 🟢 可取（`Fy36`／`Fy37`、`E29`／`E30` 已為 `W-G.9-385` 之補令所占） |
| `K29` | `0`／`0` | `5`／`5` | 🟢 可取（諸列皆量測器 `F23` 之項名 `K29`·⛔ 塊名） |
| 對照甲［必非零］`Fy37` | `2`／`9` | `2`／`12` | 🟢 框非恆空 |
| 對照甲［必非零］`K28` | `1`／`12` | `13`／`32` | 🟢 框非恆空 |
| 對照甲［必非零］`E30` | `1`／`3` | `2`／`11` | 🟢 框非恆空 |
| 對照甲［必非零］`P39` | `1`／`3` | `2`／`11` | 🟢 框非恆空 |
| 單號 `W-G.9-387`、報告名 `W-G.9-387R`、新側支之名 `W-G.9-387-k961h`、新器 `probe_WG9387_k961h`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |

自誤 `MAX` ＝ `623`、`K-9` `MAX` ＝ `79`（`§零-0` 項 `3` 之器）⇒ 本批取 `自誤 624`、`625`（塊 `E31`）；**⛔ 鑄 `K-9`**（KL 之補裁附於 `K-9-61` ⑧·塊 `K29` 之四之庚）、⛔ 鑄 `GB`、`VR`；量測器之新檔名 `F31`（`verify/probes/probe_WG9387_k961h.py`）。收工閘 `6`／`7` 以之驗。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `34736ab`，或遠端 heads ≠ `46`、或已含 `refs/heads/verify/W-G.9-387-k961h`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本單不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy38`／`K29`／`E31`／`P40` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy38` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5`；或 `§零-0` 項 `5` 之環境於安裝後仍不能匯入 |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或執行端須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-387-k961h`（回報之推至 `ops/queue` 除外）；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之三簿（`K-6` 典、自誤簿、`CLAUDE.md`）任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | 執行端作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或執行端認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁：停機上呈之全文寫入 `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`（`result` ＝ `停機上呈`）；已推至新側支之 `commit` ⛔ 撤。

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python3 verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單端實跑之出艙見 `§五-1` 項 `9`。

---
## `§一`　態錨（發單端自倉實跑·雲端 Linux·倉外工作樹·殼無 `WV_`·Python `3.11.17`·`numpy 2.4.6`·`shapely 2.2.0`·`nproc` `4`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）；遠端 heads **`46`**（`git ls-remote --heads origin` 之列數·含 `ops/queue`）；追蹤檔 `2880`（`git ls-tree -r 34736ab \| wc -l`）；`app.py` ＝ `cfd66e889f23a502792bec3ddf0fb9c875ec7524`（`1842245` B）、`verify/selection_pipeline.py` ＝ `d197f222076529c700a770915248790e316ce259`（`60273` B）、`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`（`121758` B）、`verify/run_verification.py` ＝ `f5b896e5a702c5d958e3ba27091d27832385efc4`（`103754` B）；本批所改之 `4` 器之施前 blob ＝ `§五-1` 項 `2`；`K-6` 典 ＝ `6f502cd8cca1f617beb5b9345325aef22a75b251`（`829153` B）、自誤簿 ＝ `c78a429da9822c0d4dfaae47b62b74d31d1ef9b8`（`1203451` B）、`CLAUDE.md` ＝ `0b36e0d292941ea380d1b5dc40718081680ec6d5`（`415049` B）；`git grep -F 'W-G.9-387' 34736ab` ⇒ 零命中 |
| `2` | 受詞（`34736ab`） | `adj_intake`（`app.py:12329`）之合併單位之原街廓：`if _pool:` 之本體（`:12573`〜`:12585`）以 `_basis`（逐街廓之不能分配者之 `應分配面積` 之和·同一單元只計一次）之最大者為 `_home`；最大者之差 ≤ `1e-9`（`_EPS`）者二以上 ⇒ `RuntimeError`「【未裁】歸戶 … 之原街廓：應分配面積並列 … ⇒ 停機（⛔ 自裁）」（`:12582`〜`:12584`）；docstring 之停機之段之末款「原街廓之應分配面積並列（【未裁】）」（`:12347`）。`k967_rank`（`:14566`）＝ `(−adj_q2(g), −adj_q2(pre_area), str(pid))`。`git grep -c -F` 於 `app.py`（列框）：「應分配面積並列」`2`、「if len(_cands) != 1:」`1`、「float(_r['應分配面積'])」`1`、「float(_r['原有面積'])」`1`（他處·`F10` 之字面·`W8`／`W7` 之錨） |
| `3` | 工項一之端（`34736ab` ＋ 塊 `Fy38`·倉外實跑） | 快速之 `43` 呼叫（`V-1`／`V-2` 之 `selftest`／`wiring` 等·含 `F31 selftest`／`wiring`）：紅者恰三——`F31 selftest` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K2', 'K3', 'K6', 'K7', 'K8', 'K10', 'K11', 'K14', 'K15']；rc 1`（開工態於 `K3`／`K14`／`K15` 停機·於 `K2`／`K6`／`K7`／`K8`／`K10`／`K11` 取 `G` 之逐位之最大者）；`F31 wiring … 34736ab` ⇒ `rc 1`·`⇒ 紅 ['X1', 'X2']；rc 1`；`F10 selftest` ⇒ `rc 1`·`⇒ 紅 ['S6 應分配面積並列 ⇒ 重劃前面積之和大者']；rc 1`；其餘 `40` 呼叫皆 `rc 0`、末列 ＝ 開工態之同器之末列；`stderr` 合計 `0` B。長跑 `9` 呼叫（`F31 run`、`F10 run`、`F30 run`、`k6s3 run`／`F8 run`／`parity` 之二退縮）：皆 `rc 0`·`stderr` `0` B；`F31 run`／`F10 run`／`F30 run` ＝ `⇒ 紅 []；rc 0`（`F31 run` 之出艙與原型之同呼叫逐位同）；`parity` 二退縮 ＝ `⇒ rc 0（不符 0 項）` |
| `4` | 原型（發單端·倉外·`34736ab` ＋ 塊 `Fy38` ＋ `§三` 之一實作·⛔ 為執行端之期） | 原型之 `app.py` ＝ `ee7b12eb3f350b548d643514afc6f9787b37fe97`（`1842748` B·對開工態 `+12`／`-9`）——⛔ 為期；頂層節點之相異（AST）＝ `{adj_intake}`、頂層之名之集⛔ 變；`R-5` 之字樣皆合（`V-8` 之期）。`V-1`〜`V-2` 之 `58` 呼叫（同 `§四-1` 之命令）於原型皆 `rc 0`，其末列 ＝ `§五-1` 項 `8` 之施後之列；諸器之 `stderr` 合計 `0` B。`F31 selftest` 之 `K1`〜`K15` 之期值皆發單端手算（各例之註）、原型實得與之逐值同。🔒 撰器中之二形：`F31 wiring` 之初稿以 `ast.get_source_segment` 取頂層之節點之原文（`1.8 MB` 之源·逾 `80` s）⇒ 改以列之區間（含裝飾·`2` s）；`F31 selftest` 之 `K8` 之初稿（二筆面積相同）⛔ 捕「代表取最大面積之一筆」之突變 ⇒ 改為 `30`／`20` ㎡ |
| `5` | 本案之量（開工態·工項一之端與原型·二退縮） | **原街廓之據跨二街廓之建地軌單位**（`F31 run`·外部錨 ＝ 開工態之盤點）：`3.5 m` ⇒ `G011` `R2 3.81`／`R3 92.46` ⇒ `R3`；`G025` `R5 0.99`／`R6 0.26` ⇒ `R5`；`G030` `R2 27.55`／`R3 28.34` ⇒ `R3`；`0 m` ⇒ `G011` `R2 3.81`／`R3 88.63` ⇒ `R3`；`G025` 同 ⇒ `R5`；`G030` `R2 27.55`／`R3 24.88` ⇒ `R2`——皆以第一鍵分（差 ≫ `0.01 ㎡`）⇒ 原街廓開工態與原型同。**二態之對拍**（前態 ＝ 工項一之端、後態 ＝ 原型·二退縮）：`k6s3 cmp` 二退縮 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 之落檔與 `stdout` 前後逐位同（發單端之二樹之 `HEAD` 皆 `34736ab`·⛔ 須正規化）、末列皆 `⇒ rc 0（不符 0 項）`——配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`；手冊先行 session 鍵 `f3_k953_log` `37`／`46` 列；十二呼叫與二 `cmp` 之 `stderr` 合計 `0` B ⇒ **配地⛔ 變**（`V-4`〜`V-6`） |
| `6` | 判別力（發單端·倉外·原型之上逐一施一突變） | （一）`F31 selftest`（新碼之突變·錨 ＝ 原型之字樣·⛔ 入器〔執行端之碼異〕）十二種皆捕：M1 三鍵以浮點逐位比 ⇒ `K2`／`K10`；M2 逐筆之最大（乙）⇒ `K4`／`K8`；M3 重劃前面積取分攤登記面積（⛔ 扣已併出）⇒ `K6`；M4 代表之暫編地號取最大面積之一筆 ⇒ `K8`；M5 代表取最大之暫編地號 ⇒ `K8`；M6 並列（`0.01 ㎡`）仍停機 ⇒ `K2`／`K3`／`K6`／`K7`／`K8`／`K10`／`K11`／`K13`／`K14`／`K15`；M7 差 ≤ `0.01` 即同 ⇒ `K9`；M8 合併單元之 `G` 逐片計 ⇒ `K5`；M9 重劃前面積唯計單元之首片 ⇒ `K7`；M10 暫編地號以其數字比 ⇒ `K15`；M11 面積先於 `G` ⇒ `K1`／`K4`／`K5`／`K9`／`K11`；M12 開工態之式（唯 `G`·並列取先）⇒ `K2`／`K3`／`K6`／`K11`／`K14`。（二）`F31 wiring` 六種皆捕：開工態 ⇒ `X1`／`X2`；改 `k967_rank` ⇒ `X3`；頂層增一輔助函式 ⇒ `X3`；`adj_intake` 內增案件字面 ⇒ `X4`；留 `_cands` ⇒ `X1`；harness（`verify/stepg_pipeline.py`）有改 ⇒ `X5`。（三）未改器之原型（開工態之 `verify/probes/` ＋ 原型之 `app.py`）⇒ `F23 wiring` `W8`、`F24 wiring` `W7`（錨 `if len(_cands) != 1:`·`F10` `M4`／`F17` `X4` 之字面）、`F30 wiring` `W7`、`F17` `W10`、`F10 selftest`／`wiring`、`F18 wiring` `W5`（`k967_rank` 未抽出 ⇒ `NameError`）紅——即塊 `Fy38` 之四器之隨改之由 |
| `7` | `run_all` | ⛔ 跑（單首之「級」·`§四-1` 工項二之「⛔ 跑之由」） |

---

## `§二`　KL 之語與射程

🔒 **所據**：`K-6` 典 `K-9-61` 之節（`2026-10-06 01:29`·⑧ ＝ `S143`）、`K-9-46`（三）（合併單位之原街廓）、`K-9-67`（應分配面積相同者先取重劃前面積較大者、再取暫編地號較小者·`k967_rank`）、`K-9-48` 讀法 3、`K-9-73` 之「與既有正典之關係」；`CLAUDE.md` 待落地清單（`W-G.9-385` 之節之序 `8`、`9`·`W-G.9-386` 之節）；`ops/queue` 之 `KL答覆/2026-10-17_1240.md`（「丙」：先落地序 `9` 與序 `8`·先後由發單端依依賴定）、`KL答覆/2026-10-17_1455.md`、`KL答覆/2026-10-17_1523.md`；KL 之語（下開）。

🔒 **KL 之語**（逐字·全文與所呈見塊 `K29` 之一）：
- `2026-10-17 14:55` 第 `1` 點：「……所以本題應該是往原投影位置計算之應分配面積G值最大者合併，所以原街廓是指應分配面積最大者，若G值相同再比重劃前面積，若重劃前面積再相同，就依分不到土地中暫編地號最小者」；第 `2` 點：「問二：採現行……」。
- `2026-10-17 15:23`：「甲」（各街廓分不到土地的 G 加總後比；相同再比各街廓分不到土地的重劃前面積合計；再相同，比各街廓分不到土地中暫編地號最小者）。

🔒 **授權**（自動化之委任·`ops/queue` 之 `README_自動化運作規則.md` 第一節·逐字）：KL `2026-10-17 07:23` 第 `3` 點「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目，……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」；`07:58`「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」。本單之項目有 KL 之逐字裁示（上開）⇒ 屬 README 第二節「自動處理」第 `1` 款。**`expects_allocation_change` ＝ `false`**（`§一` 項 `5`）：本案配地若有任一改變 ⇒ 停機款 `6`（⛔ 入主線·發單端依 README 第二節「停下來通知 KL」第 `2` 款請示 KL）。

🔒 **【工】之讀法**（塊 `K29` 之四·發單端·⛔ 充裁·於每日摘要告 KL）：甲 重劃前面積 ＝ `原有面積`；乙 應分配面積之和 ＝ 開工態之 `原街廓之據`；丙 比較以 `k967_rank`；丁 並列之停機去之；戊 本案；己 射程之重分；庚 ⛔ 鑄新號。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由執行端逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支；`(c)` ⛔ 及主線、他側支、`data/`、`K-9-61` ①〜⑥、`GB-205`、`K-9-60`、`K-9-59`、`K-9-63`、`K-9-62` 之指配、`K-9-78`、規格步 `5`——另單（`CLAUDE.md` 塊 `P40` 之表）；`(d)` 主 checkout 之同步省之（README 第六節第 `6` 款·KL 自為之）。

---

## `§三`　規格（執行端依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**：
- 「**分不到之土地**」＝ `adj_intake` 之某歸戶之列中，類 ＝ `ADJ_DISP_POOL`（建築街廓內不能分配）者（即開工態之 `_pool`）；其「街廓」＝ 該列之 `所屬街廓`。
- 「**單元**」＝ 該列之 `所屬單元`（入池閘之末態 build 之宗·開工態之 `_unit_of` 之值）。
- 「**應分配面積之和**」＝ 開工態之 `_basis`：逐街廓，該街廓之分不到之土地之 `應分配面積`（該趟之不配地紀錄之 `G(㎡)`）之和，**同一單元只計一次**（開工態之 `_seen` 之式·⛔ 改）。
- 「**重劃前面積之和**」＝ 逐街廓，該街廓之**每一**分不到之土地之列之 `原有面積` 之和（每列皆計·⛔ 依單元去重；`原有面積` 於部分併出者 ＝ 其剩下〔開工態之式·⛔ 改〕＝ `K-9-67` 之重劃前面積）。
- 「**最小之暫編地號**」＝ 逐街廓，該街廓之分不到之土地之 `暫編地號`（字串）之最小者（字串之序）。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | `adj_intake` 之合併單位之原街廓（開工態之 `if _pool:` 之本體·`_home` 之定） | 原街廓 ＝ 各街廓（`_basis` 之鍵）之中，`k967_rank(<應分配面積之和>, <重劃前面積之和>, <最小之暫編地號>)` 最小者（**恰一處**呼 `k967_rank`·三引數皆以位置傳之）。即：應分配面積之和大者先；以 `0.01 ㎡` 為單位而相同者，重劃前面積之和大者先；再相同，最小之暫編地號小者先。⛔ 停機（暫編地號唯一 ⇒ 恆分）。`原街廓之據`（`_basis`）之值與鍵⛔ 變（顯示照舊）。 |
| `R-2` | 同上 | 開工態之「原街廓之應分配面積並列 ⇒ `RuntimeError`」去之（其訊息之字樣「應分配面積並列」於 `adj_intake` 內 ⇒ `0`；`_top`、`_cands` 之名於 `adj_intake` 內 ⇒ 去之）。合併單位之 `dict` 之鍵與其餘之值⛔ 變；建地軌以外之單位、`step4`、`totals`、`slices` 之一切⛔ 變。 |
| `R-3` | `adj_intake` 之 docstring | 「停機（`RuntimeError`·⛔ 靜默略過）：……」之段之末之「；原街廓之應分配面積並列（【未裁】）」去之（其前之「殘料之原有面積 `> 0`」之後改以「。」終）；docstring 之末（`"""` 之前）增一段，以 ``🔧 `W-G.9-387` `` 起首，述 `R-1`（三鍵、`0.01 ㎡`、`k967_rank`、同一單元之 `G` 只計一次）。他處之 docstring 與註⛔ 改。 |
| `R-4` | 註 | 原街廓之擇定之段得增一註（以 ``🔧 `W-G.9-387` `` 起首）。🔒 新書之碼、註與 docstring ⛔ 含字樣 `float(_r['原有面積'])`（`§三-3` 之 `2`）、⛔ 含 `if len(_cands)`。 |
| `R-5` | 字樣（列框·`git grep -c -F … -- app.py`） | 施前（`34736ab`）：「應分配面積並列」`2`（皆在 `adj_intake`：docstring 之停機之段之一、並列之 `raise` 之一）、「if len(_cands) != 1:」`1`。施後：此二者皆 ⇒ **`0`**；「float(_r['應分配面積'])」「if _pool or (_cm and not _al):」「if '段三併出' in t:」「float(_r['原有面積'])」「def k967_rank」各恰 `1`（同施前）。 |
| `R-6` | 本案 | 二退縮之配地、街角得標與強制旗標、段三／末端塊合併再試／手冊先行／第一趟之紀錄、入池閘之紀錄、調配之輸入（含諸合併單位之原街廓）、畫面與 harness 之對拍之結果皆⛔ 變（`§一` 項 `5`）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F31`（`verify/probes/probe_WG9387_k961h.py`·新）：`selftest` 之 `K1`〜`K15`（`R-1`·AST 抽出 `adj_intake`、`k967_rank`、`adj_q2` 與 `ADJ_*`）；`wiring <repo> 34736ab` 之 `X1`〜`X5`（`R-1`〜`R-2`、頂層之相異 ⊆ {`adj_intake`}、⛔ 案件字面、`verify/` 之生產碼⛔ 改）；`run` 之 `R1`〜`R3`（`R-6`·本案·外部錨 ＝ 開工態之盤點）。
- `F10`（`probe_WG9351_intake.py`）：抽出增 `k967_rank`、`adj_q2`（⛔ 入 `W1`／`W4` 之受詞）；`S6` 之期 ⇒ 重劃前面積之和大者；突變 `M4` 去之；`run` 之外部錨之原街廓依三鍵（本器另寫）。`F17`（`probe_WG9358_k948_wiring.py`）：`W10` 之 `X4` 去「if len(_cands) != 1:」。`F18`（`probe_WG9359_cand.py`）：`_screen_ns` 之抽出增 `k967_rank`。`F30`（`probe_WG9385_k974.py`）：`W7` 之頂層之相異之許增 `adj_intake`。
- `app.py` 之頂層節點對 `34736ab` 相異者 ＝ **`{adj_intake}`**，頂層之名之集⛔ 變；`verify/` 之生產碼⛔ 改。

### `§三-3`　禁改（既有閘之錨·執行端撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **突變之錨**（`F10 selftest` 之 `M1`〜`M3`：「float(_r['應分配面積'])」「if _pool or (_cm and not _al):」「if '段三併出' in t:」；`F17` `W10` 之 `X4` 之三字樣）：於 `app.py` 與 `adj_intake` 內各仍恰 `1`。`F27 mutate`（`MUT377` 之 `N01`〜`N57`）、`F25 mutate`、`F19 mut`、`F22 mut` 之錨所在之函式本單⛔ 動 ⇒ 自然⛔ 觸；其期 ＝ `§五-1` 項 `8`。
2. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計）；基準中恰一之函式名（含巢狀）於工作樹仍恰一 ⇒ 新碼⛔ 增巢狀之 `def`（亦⛔ 增 `lambda` 以外之巢狀函式）、⛔ 含 `float(_r['原有面積'])`（`F10` 之字面·基準恰一見·`W8`／`W7` 之錨）。執行端撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
3. **頂層之名之許**（`F23 wiring` 之 `W7`、`F24 wiring` 之 `W5`、`F25 wiring` 之 `X2`、`F30 wiring` 之 `W7`、`F31 wiring` 之 `X3`）：頂層之相異 ＝ `{adj_intake}`、⛔ 新名。
4. **⛔ 案件字面**（`F31 wiring` 之 `X4`·`F10 wiring` 之 `W1`）：`adj_intake` 之字串常數⛔ 含街廓名、地號之形（`R1`〜`R6`、`G001` 之形、`628-` 之形）。
5. `F17 wiring` 之他項、`F25 wiring` 之 `X3`／`X5`、`F10 wiring` 之 `W2`〜`W5`、`F27 wiring` 之 `Y1`〜`Y9`、`F29 wiring` 之 `Y1`〜`Y11`、`F14`／`F15`／`F9`／`F4` 之接線之項⛔ 觸。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

`K-9-61` ⑧ 與其 KL 補裁已裁（塊 `K29` 之二）；其落地之讀法 ＝ 塊 `K29` 之四（【工】·於每日摘要告 KL）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地或諸紀錄有任一改變（含任一合併單位之原街廓）；`§三-1` 之式於某形無從定之（例：某分不到之土地之 `原有面積` 非數值、某街廓於 `_basis` 而無分不到之土地之列）；`R-1` 之三鍵須讀 `adj_intake` 之列以外之量方能定之。

### `§三-5`　執行端之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-5`）：落於何處、其字樣；對 `§三-3` 各款之自查；三鍵之受詞（每列皆計之面積、單元只計一次之 `G`、字串之最小暫編地號）。另附 `git diff <工項一之端> <工項二之 commit> -- app.py` 之全文（報告同目錄之 `.diff`）。

---
## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-387-k961h`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-387_規格單.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-387_規格單.md` 與來源逐位同。`commit` 訊息之首列逐字 `W-G.9-387 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-387-k961h`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`47`**、主線仍 ＝ `34736ab…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-387-k961h`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy38` 抽為 `<O>/Fy38.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`5` 檔（`4` 改·`1` 新）之 `git hash-object` ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `5` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-387 工項一：量測器（F31 之新器·F10、F17、F18、F30 之隨改）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`。

**工項二　生產碼**（🔴 `app.py`·執行端依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`）：
1. 紅（末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K2', 'K3', 'K6', 'K7', 'K8', 'K10', 'K11', 'K14', 'K15']；rc 1`；`… wiring <repo> 34736ab` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['X1', 'X2']；rc 1`；`… run <repo>` ⇒ `rc 0`·末列逐字 `⇒ 紅 []；rc 0`（本案之原街廓於開工態與施後皆同·`R2`／`R3` 之外部錨）；三呼叫之 `stderr` 皆 `0` B。
2. 綠（**`rc 0`**·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`V-1`／`V-2` 之其餘之呼叫（同 `§四-1` 之驗之命令）——唯 `F10 selftest`（`S6` 之期已改 ⇒ 工項一之端 `rc 1`·末列逐字 `⇒ 紅 ['S6 應分配面積並列 ⇒ 重劃前面積之和大者']；rc 1`）除外。
3. `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_pre_35.json`；同 `0.0` ⇒ `<O>/k6s3_pre_00.json`；`python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_pre_35.json`；同 `0.0` ⇒ `<O>/f8_pre_00.json`；`python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_pre.json`；同 `0.0` ⇒ `<O>/parity00_pre.json`（皆 `rc 0`）。
4. `git grep -c -F "應分配面積並列" -- app.py` ⇒ 出艙恰一列 `app.py:2`；`git grep -c -F "if len(_cands) != 1:" -- app.py` ⇒ 出艙恰一列 `app.py:1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：執行端依 `§三` 撰寫 `app.py` 之改動；`python3 -m py_compile app.py`；`commit` 訊息之首列逐字 `W-G.9-387 工項二：K-9-61 ⑧ 之 KL 補裁之落地（合併單位之原街廓：應分配面積之和 → 重劃前面積之和 → 最小之暫編地號·k967_rank·並列之停機去之）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>/*_post.*`）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy38` 所改、所增之器與其接線之器（`12` 呼叫）：`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`… run <repo>`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>`；`… wiring <repo>`；`… run <repo>`；`python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>`；`python3 verify/probes/probe_WG9359_cand.py selftest <repo>`；`… wiring <repo>`；`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F31 selftest` 之 `K1`〜`K15`、`F31 wiring` 之 `X1`〜`X5`、`F31 run` 之 `R1`〜`R3`（二退縮）皆 ✅ |
| `V-2` | `W-G.9-385` 規格單 `§四-1` 之 `V-1`〜`V-2` 之 `55` 呼叫中上列者以外之呼叫（命令同之·`F30 selftest`／`run` 在內）：`F30`（`probe_WG9385_k974.py selftest`／`run`）、`F23`（`probe_WG9363_k953.py selftest`／`run`）、`probe_WG9370_adj4mut.py wiring <repo> 3b35daa`、`F16`（`probe_WG9357_k948.py selftest`／`run`）、`probe_WG9355_screenmerge.py selftest`／`run`、`probe_WG9356_screenmerge_wiring.py wiring`、`probe_WG9350_frontroad.py selftest`／`wiring`／`run`、`F24`（`probe_WG9367_adj4.py selftest`／`run`）、`F29`（`probe_WG9375_k965.py selftest`／`wiring`／`run`）、`F25 mutate`（`probe_WG9370_adj4mut.py mutate`）、`F27`（`probe_WG9373_k966.py selftest`／`wiring`／`mutate`／`run`）、`F28`（`probe_WG9373p1_partrem.py selftest`）、`F8`（`probe_WG9349_k9296.py selftest`／`wiring`）、`probe_WG9345_screen.py wiring`、`probe_WG9352_endblock.py`／`probe_WG9353_endmerge.py`／`probe_WG9354_endcontest.py` 之 `selftest`／`wiring`、`F19 mut`（`probe_WG9360_cand_mut.py mut`）、`probe_WG9361_k954.py selftest`／`wiring`／`run`、`probe_WG9362_k954_mut.py mut`、`probe_WG9372_ww.py selftest`／`run`、`probe_WG9344_k6s3.py selftest`、`probe_WG9344p1_pooltemp.py selftest`、`probe_WG9348_harvest_key.py <repo>`、`probe_WG9341_synth.py <repo>`、`probe_WG9340_main_synth.py <repo>`、`probe_WG9346_failclosed.py run <repo> 3.5`（共 `46` 呼叫） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列 |
| `V-3` | `V-1`〜`V-2` 之 `58` 呼叫之器之載入 | 本批所改、所增之器 `5` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_post_35.json`；同 `0.0`；`… cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**·`R-6`） |
| `V-5` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_post.json`；同 `0.0` ⇒ `<O>/parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置 `3` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（執行端以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異）；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0` |
| `V-6` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_post_35.json`；同 `0.0` ⇒ `<O>/f8_post_00.json`；`git hash-object <O>/f8_pre_35.json <O>/f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`1`**（`app.py`）；其增／刪之數與其 blob 出艙（發單端復驗時自倉重算·⛔ 預載）；`verify/` 之一切檔對工項一之端相異 `0`；`app.py` 之頂層節點之名之集 ＝ 工項一之端之集（AST）；其相異之節點 ＝ `{adj_intake}` |
| `V-8` | `R-5` 之字樣（`git grep -c -F "<字樣>" -- app.py`·逐一） | 「float(_r['應分配面積'])」「if _pool or (_cm and not _al):」「if '段三併出' in t:」「float(_r['原有面積'])」「def k967_rank」⇒ 各 `app.py:1`；「應分配面積並列」「if len(_cands) != 1:」⇒ 皆**無出艙**、`rc 1`（判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**；逾時之重跑依單首 🔑）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞於本案之配地⛔ 觸（`§一` 項 `5`），其「⛔ 變」由 `V-4`〜`V-6` 與 `F31 run`、`F10 run`、`F23 run`／`F24 run`／`F27 run`／`F29 run`／`F16 run` 直接量之。

**唯讀獨立審查**（驗皆符後、推前）：執行端另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：三鍵之受詞（`G` 之和同一單元只計一次；重劃前面積之和每列皆計、取 `原有面積`；最小暫編地號以字串之序）、`k967_rank` 之恰一呼與其三引數之序、並列之停機與其 docstring 之款之去、`原街廓之據` 之⛔ 變、`§三-3` 之字樣之錨（`float(_r['原有面積'])` ⛔ 新增）；以獨立之合成之例（`F31` 之外·至少一例：三街廓、其一含入池閘之合併單元、G 之和以 `0.01 ㎡` 為單位而同二者）比 `adj_intake` 之原街廓與手算；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ 執行端修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-387-k961h`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K29` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `E31` 附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末；塊 `P40` 附於 `CLAUDE.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；三檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>/checkidx.py`、`<O>/gen_fa_index.py`（⛔ 入倉）。
3. 塊 `P40` 附後：`python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-387 工項三：K-9-61 ⑧ 之 KL 補裁·段三後處理 (a) 之讀法入典 ＋ 自誤 624、625 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-387R_原街廓之擇定_執行報告.md` ＋ 同目錄之 `W-G.9-387R_原街廓之擇定_app差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`12` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之十二呼叫之全文、`V-2` 之 `F27 mutate`／`F25 mutate` 之全文、`V-5` 之正規化之比與其對照、`V-6` 之 `hash-object` 之出艙、`F23 run`／`F16 run`／`F29 run` 之末十四列、`k6s3 cmp` 之全文、`parity` 之末十五列、`58` 呼叫之 `rc`／`stderr`／耗時／末列之表〔重跑者二趟並載〕）；④ 塊之實得（bytes／`sha256`）與三簿之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ 執行端之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **`app.py` 之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**（並行之數）；⑪ 雲端之執行之所見。收工閘之實測值出艙於 `ops/queue` 之回報（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-387 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`。其後依 `執行端.md` 丁回報於 `ops/queue`。

### `§四-2`　次單（⛔ 本單之期）

發單端復驗本批之碼（自倉重跑 `V-1`〜`V-9` 之要者·`k6s3 cmp`／`parity`／`F8`）後：本案配地⛔ 變而諸閘皆符 ⇒ **入主線之短單**（快轉·⛔ `--force`·README 第二節「自動處理」第 `1` 款·前後值入 `log.md`）；配地有變 ⇒ `await_kl`（側支保留）。其後 `W-G.9-388`（`CLAUDE.md` 塊 `P40` 之表序 `3`）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `verify/probes/probe_WG9351_intake.py` `37`／`4`、`probe_WG9358_k948_wiring.py` `3`／`1`、`probe_WG9359_cand.py` `3`／`1`、`probe_WG9385_k974.py` `3`／`1`、`probe_WG9387_k961h.py` `352`／`0`（唯此 `5` 檔）（增／刪）；工項二 ＝ `app.py`（唯此一檔·其數出艙）；工項三 ＝ `K-6` 典 `64`／`0`、自誤簿 `22`／`0`、`CLAUDE.md` `27`／`0`（唯此三檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `34736ab` | 生產碼相異恰 **`1`**（`app.py`）；`verify/` 之一切檔相異恰 **`5`**（`M` `4`：`probe_WG9351_intake.py`、`probe_WG9358_k948_wiring.py`、`probe_WG9359_cand.py`、`probe_WG9385_k974.py`；`A` `1`：`probe_WG9387_k961h.py`）；本批之新檔（本單、新器、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`12` 檔：本單、`5` 器、`app.py`、`K-6` 典、自誤簿、`CLAUDE.md`、報告二檔） |
| `4` | 三簿之 bytes | `K-6` 典 `829153` → **`837563`**；自誤簿 `1203451` → **`1206901`**；`CLAUDE.md` `415049` → **`419535`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊 |
| `5` | 自限 | 遠端 heads **`47`**；主線 ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（⛔ 變）；`verify/W-G.9-387-k961h` ＝ 工項四之 `commit`，其祖含 `34736ab`；其餘 `46` 列中，除 `ops/queue`（回報後可變）外之 `45` 列逐列 ＝ `<O>/heads_before_387.txt` |
| `6` | `python3 verify/probes/probe_WG9270_closegate.py 625 623 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 626 625 .` ⇒ `rc 7` |
| `7` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 625 623` | **`rc 0`**；其「項4′ 四簿·正典框」：自誤 相異 **`610`**／`MAX` **`625`**／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（自誤唯增 `624`、`625`；餘 ＝ 開工態） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單端已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---
## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單端擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 塊 `Fy38` | `32077` B·`sha256` `7bdd6c7749eecb39ef9e38bd442d1c4e5bf9b031ad7341ce1e5470f667456068`·`525` 列（圍欄內全文·末附換行）；抽為 `<O>/Fy38.diff`，`git apply` 於 `verify/probes/` 之 `5` 檔（`4` 改·`1` 新），其施前 blob（B）：`probe_WG9351_intake.py` `26669af87da4efa34150c5c927c77134286c242b`（`32524`）、`probe_WG9358_k948_wiring.py` `6bdc07df94523e29401f935dbef142c6812126b2`（`28996`）、`probe_WG9359_cand.py` `4fb5085ba8ab3581b79359e260586d810047c3f6`（`47743`）、`probe_WG9385_k974.py` `87c8a3883355cd6093efa4e281b47e473c01a769`（`42206`）；`probe_WG9387_k961h.py` 施前⛔ 存 |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K29`／`E31`／`P40` | 塊 `K29` `8410` B·`sha256` `047a3a833c2d82c1296cf2d4aa854ba6b367f72d228854938643f18cda333e78`·`64` 列；塊 `E31` `3450` B·`sha256` `2babfa7ca053ce42632aeb6b8f4e01ff47115078ef0e07ef9f1db6ce1770d5f0`·`22` 列；塊 `P40` `4486` B·`sha256` `33bf92f9f9985c9abcb27463126de0f393bf696659c44c2e9409977652898bf3`·`27` 列（皆圍欄內全文·末附換行·首列為空列；`P40` 之 payload 內 `⬜` 之子字串框 `14`·列框 `12`〔塊之自載〕）；附於 `K-6` 典（`829153` B）、自誤簿（`1203451` B）、`CLAUDE.md`（`415049` B）之末，期末 ＝ `837563`／`1206901`／`419535` B |
| `5` | 寫出後之 blob | 工項一之 `5` 器（`verify/probes/`·B）：`probe_WG9351_intake.py` ＝ `f43d746b369109171f6d137033d0f55a078ae225`（`34677`）、`probe_WG9358_k948_wiring.py` ＝ `05fc962d43468f5d23a626571759c9dfb20c56cb`（`29211`）、`probe_WG9359_cand.py` ＝ `c3fa6591c7c9c33e17139a75a64184da91c371e7`（`47878`）、`probe_WG9385_k974.py` ＝ `0e9e3fd29bc31e7c92de8e4a3f8363331e60bdc4`（`42477`）、`probe_WG9387_k961h.py` ＝ `ac0b93eee16221a347dd6f333bbab56d807522ff`（`20900`·新）；工項三之三簿：`K-6` 典 ＝ `014caeca8e80e18a2cc7f9cbc22c7f089fd9b716`（`837563` B）、自誤簿 ＝ `2ba9fc5a8f7cfe1ae1235707087bc9152bfcc4a8`（`1206901` B）、`CLAUDE.md` ＝ `816555f1b8fae459c0df022ab09f36e9cb781fd9`（`419535` B）。🔒 `app.py` 之施後 blob **⛔ 預載**（規格單·由執行端回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-386` 規格單 `§五` 項 `7`） |
| `8` | 量測器之二態（發單端實跑·倉外） | **工項一之端**（`34736ab` ＋ 塊 `Fy38`）：見 `§一` 項 `3`（其三紅呼叫之末列 ＝ 前置 `1`／`2`；`F31 run` ＝ `⇒ 紅 []；rc 0`；他呼叫 ＝ 開工態之末列）。**施後**（原型）：`58` 呼叫皆 `rc 0`，末列逐字皆 `⇒ 紅 []；rc 0`，唯：`probe_WG9373_k966.py mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`probe_WG9370_adj4mut.py mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`；`probe_WG9345_screen.py wiring` ＝ `⇒ rc 0（不符 0·器紅 0）`；`probe_WG9344_k6s3.py selftest` ＝ `selftest 9/9 ⇒ ✅`；`probe_WG9344p1_pooltemp.py selftest` ＝ `selftest 13/13 ⇒ ✅`；`probe_WG9341_synth.py` ＝ `ε ＝ 0.0002｜rc 0`；`probe_WG9340_main_synth.py` ＝ `紅項 [] 器紅 0`。`F31 selftest` `K1`〜`K15` ✅、`F31 wiring` `X1`〜`X5` ✅、`F31 run` `R1`〜`R3`（二退縮）✅。諸呼叫（含 `k6s3 run`／`F8 run`／`parity` 之二態十二呼叫）之 `stderr` 合計 `0` B；`58` 呼叫之耗時之和 ≈ `7063` s、二態之十二呼叫 ≈ `2600` s（雲端 `4` 核·並行 `2`〜`3`）。🔒 `F31 selftest`／`wiring` 與 `F23 wiring`／`F24 wiring`（其 `W8`／`W7` 掃 `F31` 之字面）以定稿之器重跑（`F31` 之頂層之原文改以列之區間取之、`K8` 之加強之後）；他器於其間⛔ 改 |
| `9` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本單>`·發單端實跑（態 `34736ab`·定稿）：🔴 機械 `0` 項／🟡 提示 `2` 項——`P-4` `:168`（工項二之「施」之 `commit` 訊息·其箭頭係三鍵之序之述〔應分配面積之和 → 重劃前面積之和 → 最小之暫編地號〕⇒ **具名豁免**）、`:205`（`§四-3` 收工閘之表頭·其箭頭之座標系 ＝ 改前至改後〔閘 `4`〕⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23351`–`31093`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單端·雲端 Linux·⛔ `push`） | `git worktree add --detach <S> 34736ab`（拋棄式）＋ 本單之定稿（`904` 列·其四塊即附錄甲〜丁）＋ 原型之 `app.py`（代工項二）＋ 報告之替身·五 `commit`（工項零之首列 ＝ 所令逐字；工項一〜四以模擬之首列代之·其後空一列附尾列）：工項零之 blob ＝ 來源；四塊之抽取 ＝ 項 `2`／`4`；`git apply --check` `rc 0`；`5` 器之施後 blob ＝ 項 `5`；工項二 ＝ `app.py` `12`／`9`；三簿之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx`／`gen_fa_index` ＝ 期·逐位同；閘 `1` ＝ 工項零 `904`／`0`、工項一 ＝ 該閘之期、工項二 ＝ 上開、工項三 ＝ 該閘之期、工項四（替身）二檔各 `1`／`0`；閘 `2` ＝ 生產碼相異 `1`、`verify/` 相異 `5`（`M` `4`·`A` `1`）·新檔四之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `12` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `4` 三簿皆改前為改後之嚴格前綴；閘 `6` `rc 0`（判別力 `626 625` ⇒ `rc 7`）；閘 `7` `rc 0`（自誤 `610`／`625`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `76`／`79`·缺號 ＝ 該閘之期）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `4`／`5` 之實跑逐位同（`5` 器 ＝ 項 `5`、`app.py` ＝ 原型） |

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丁` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-387-k961h`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 回報 ⇒ 依 `執行端.md` 丁（`ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`）。

---

## 附錄甲　塊 `Fy38`（`git apply` 之差異·`verify/probes/` 之 `5` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9351_intake.py b/verify/probes/probe_WG9351_intake.py
index 26669af..f43d746 100644
--- a/verify/probes/probe_WG9351_intake.py
+++ b/verify/probes/probe_WG9351_intake.py
@@ -20,9 +20,13 @@
            `adj_intake`）逐切片對拍（外部錨）：R1 盤點⛔ 停機；R2 逐切片之類相同；R3 合併單位（歸戶·軌·原街廓·成員）
            相同；R4 逐類之切片數與原有面積之和 ＝ 全部切片；R5 入池閘之入池宗（不配地之 build 單元之成員）之數與
            原有面積 ＝ 類「建築街廓內不能分配」者。
+  🔧 `W-G.9-387`（`K-9-61` ⑧ 之 KL 補裁·⛔ 上列一字不刪）：原街廓之擇定改依 `k967_rank`（G 之和 → 重劃前面積之和 →
+    最小之暫編地號）、⛔ 停機 ⇒ 抽出另含 `k967_rank`、`adj_q2`（`EXTRA_FUNCS`·⛔ 入 W1／W4 之受詞）；S6 之期改為重劃前面積
+    之和大者（B1）；突變 M4（並列⛔ 停機）去之（其錨已去）；`run` 之外部錨之原街廓依同一三鍵（本器另寫·⛔ 呼 `k967_rank`）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, os, re, sys
+from decimal import Decimal, ROUND_HALF_UP
 
 try:
     sys.stdout.reconfigure(encoding="utf-8")
@@ -30,6 +34,7 @@ except Exception:
     pass
 
 ADJ_FUNCS = ["adj_intake", "adj_intake_rows"]
+EXTRA_FUNCS = ["k967_rank", "adj_q2"]   # 🔧 `W-G.9-387`：唯供抽出（`adj_intake` 之原街廓之序鍵）
 ADJ_KEYS = ["f3_k929_6_build", "f3_k929_6_dropped"]
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 
@@ -44,7 +49,7 @@ def _extract_ns(src):
     tree = ast.parse(src)
     parts = []
     for node in tree.body:
-        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS:
+        if isinstance(node, ast.FunctionDef) and node.name in ADJ_FUNCS + EXTRA_FUNCS:
             parts.append(ast.get_source_segment(src, node))
         elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                 and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
@@ -109,7 +114,8 @@ def _cases(ns):
     run("S5 原街廓 ＝ 應分配面積較大者（⛔ 原有面積）",
         lambda: I(temp2, b2, [], d2, own, BUR)["units"][0]["原街廓"], "B2")
     d2t = {("B1", "left"): [{"暫編地號": "u", "G(㎡)": 25.0}], ("B2", "right"): [{"暫編地號": "v", "G(㎡)": 25.0}]}
-    run("S6 應分配面積並列 ⇒ loud", lambda: I(temp2, b2, [], d2t, own, BUR), ("例外", "RuntimeError"))
+    # 🔧 `W-G.9-387`（`K-9-61` ⑧ 之 KL 補裁）：G 並列 ⇒ 重劃前面積之和大者（u 100 ＞ v 40）⇒ B1·⛔ 停機
+    run("S6 應分配面積並列 ⇒ 重劃前面積之和大者", lambda: I(temp2, b2, [], d2t, own, BUR)["units"][0]["原街廓"], "B1")
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
@@ -422,10 +427,22 @@ def _independent(tp3, bfin, rows, drops, own, bur):
         for m in u.get("入池閘併入") or [u["暫編地號"]]:
             mem[str(m)] = str(u["暫編地號"])
     kind, owner, s3 = {}, {}, set()
+    # 🔧 `W-G.9-387`：入池閘之帳之各片之已併出之量（原街廓之第二鍵 ＝ 不能分配者之重劃前面積）
+    acct = {}
+    for u in bfin:
+        if u.get("_is_ghost_sliver"):
+            continue
+        if u.get("入池閘部分併出"):
+            acct[str(u["暫編地號"])] = sum(float(v) for v in u["入池閘部分併出"].values())
+        for m, d in (u.get("入池閘成員部分併出") or {}).items():
+            if d:
+                acct[str(m)] = sum(float(v) for v in d.values())
+    by = {}
     for t in tp3:
         if t.get("_is_ghost_sliver"):
             continue
         k = str(t["暫編地號"])
+        by[k] = t
         owner[k] = own[str(t["原地號"])]
         # 🔧 `W-G.9-363`（發單側窗六十四·⛔ 下列一字不刪）：帶 段三餘量 而其值 ＞ 0 之片（段三或手冊先行之剩下）⇒
         #   恆入合併單位（`W-G.9-357`）——其歸戶無入池之宗而有配地者，另成公設軌之單位（`adj_intake` 之 `_s3`）
@@ -450,7 +467,18 @@ def _independent(tp3, bfin, rows, drops, own, bur):
             bl = {}
             for u in {mem[k] for k in ks if kind[k] == "池"}:
                 bl[dg[u][0]] = bl.get(dg[u][0], 0.0) + dg[u][1]
-            units[g] = ("建", max(bl, key=bl.get), sorted([k for k in ks if kind[k] == "池"] + cm))
+            # 🔧 `W-G.9-387`：原街廓 ＝ (G 之和大 → 重劃前面積之和大 → 最小之暫編地號小)（`0.01 ㎡`·本器另寫）
+            pre, pmin = {}, {}
+            for k in ks:
+                if kind[k] != "池":
+                    continue
+                b, t = by[k]["所屬街廓"], by[k]
+                a = float(t.get("分攤登記面積_m2", 0) or 0) - acct.get(k, 0.0) - \
+                    sum(float(v) for v in (t.get("段三部分併出") or {}).values())
+                pre[b] = pre.get(b, 0.0) + a
+                pmin[b] = min(pmin.get(b, k), k)
+            units[g] = ("建", sorted(bl, key=lambda b: (-_q2(bl[b]), -_q2(pre[b]), pmin[b]))[0],
+                        sorted([k for k in ks if kind[k] == "池"] + cm))
             for k in cm:
                 kind[k] = "公入"
         elif cm and not has_a:
@@ -469,6 +497,11 @@ def _independent(tp3, bfin, rows, drops, own, bur):
     return kind, units
 
 
+def _q2(x):
+    """🔧 `W-G.9-387`：四捨五入至 `0.01`（本器另寫·⛔ 呼 `adj_q2`）。"""
+    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
+
+
 def run(repo, sbs):
     sys.path.insert(0, os.path.join(repo, "verify"))
     cwd = os.getcwd()
diff --git a/verify/probes/probe_WG9358_k948_wiring.py b/verify/probes/probe_WG9358_k948_wiring.py
index 6bdc07d..05fc962 100644
--- a/verify/probes/probe_WG9358_k948_wiring.py
+++ b/verify/probes/probe_WG9358_k948_wiring.py
@@ -57,6 +57,8 @@ _k6b_callbacks 之巢狀 alloc_state。
     （其錨已去·M2 之錨之縮排隨步驟 10 之重排而異），餘 15 種。
   🔧 `W-G.9-378`（`GB-204`·⛔ 上列一字不刪）：W8 之回傳之鍵於 `'members'` 之後增 `'pool_out'`（入池閘之帳·第六鍵·其值與
     `members` 取同一 build·F27 之 Y8 量之）。
+  🔧 `W-G.9-387`（`K-9-61` ⑧ 之 KL 補裁·⛔ 上列一字不刪）：`adj_intake` 之原街廓之並列之停機去之 ⇒ W10 之 X-4 之字樣去
+    其末一（並列之判）、餘三。
 rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
 """
 import ast, contextlib, io, os, sys
@@ -72,7 +74,7 @@ FN_PT, FN_HCB = "k6b_stage3_pool_temp", "_k6b_callbacks"
 NEST = ("_has357", "_res357", "_max357", "_dist357", "_k951", "_split357", "_t14_357")
 # 🔧 `W-G.9-373`（`K-9-66`）：`_max357`／`_k951`／`_split357` 去之
 NEST = tuple(x for x in NEST if x not in ("_max357", "_k951", "_split357"))
-X4 = ("float(_r['應分配面積'])", "if _pool or (_cm and not _al):", "if '段三併出' in t:", "if len(_cands) != 1:")
+X4 = ("float(_r['應分配面積'])", "if _pool or (_cm and not _al):", "if '段三併出' in t:")   # 🔧 `W-G.9-387`：去並列之判
 
 
 def _read(repo, rel):
diff --git a/verify/probes/probe_WG9359_cand.py b/verify/probes/probe_WG9359_cand.py
index 4fb5085..c3fa659 100644
--- a/verify/probes/probe_WG9359_cand.py
+++ b/verify/probes/probe_WG9359_cand.py
@@ -382,7 +382,9 @@ def _find_main_block(mn):
 
 
 def _screen_ns(app_src):
-    return _extract_ns(app_src, funcs=FUNCS + ["adj_intake", "r3_front_road_identifier", "r3_normalize_road_name"],
+    # 🔧 `W-G.9-387`：`adj_intake` 之原街廓之序鍵用 `k967_rank`
+    return _extract_ns(app_src, funcs=FUNCS + ["adj_intake", "r3_front_road_identifier", "r3_normalize_road_name",
+                                               "k967_rank"],
                        consts=CONSTS + ["SS_FRONT_ROAD_NAME", "SS_FRONT_ROAD_DERIVE", "K91_SS_MBA_EFFECTIVE"],
                        prefixes=("ADJ_", "SS_ADJ_", "R3_STATUS_"))
 
diff --git a/verify/probes/probe_WG9385_k974.py b/verify/probes/probe_WG9385_k974.py
index 87c8a38..0e9e3fd 100644
--- a/verify/probes/probe_WG9385_k974.py
+++ b/verify/probes/probe_WG9385_k974.py
@@ -40,6 +40,7 @@
            ⇒ 其尺度 ＝ 外部錨（`RD1` 之 BLOCK 面積與該宗之幾何面積之比）；R4 模擬：私有地填「是」⇒ 填列錯誤；
            R5 模擬：`JUNCTION` 框疊於 `RD1` 之一端 ⇒ 比例之母體扣除之（外部錨）；R6 二欄之結果依檔之 sha256 存 session
            （同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）。
+  🔧 `W-G.9-387`（⛔ 上列一字不刪）：W7 之頂層之相異之許增 `adj_intake`（原街廓之擇定·`K-9-61` ⑧ 之 KL 補裁）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, os, sys
@@ -489,7 +490,8 @@ def wiring(repo, base):
             for ln in difflib.ndiff((btop.get(k) or "").split("\n"), (ctop.get(k) or "").split("\n")):
                 if ln.startswith("- "):
                     dels.append((k, hashlib.sha256(ln[2:].encode("utf-8")).hexdigest()))
-        ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"}
+        # 🔧 `W-G.9-387`：`adj_intake`（原街廓之擇定·`K-9-61` ⑧ 之 KL 補裁）之相異許之
+        ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total", "adj_intake"}
                and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
         res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
     except Exception as e:
diff --git a/verify/probes/probe_WG9387_k961h.py b/verify/probes/probe_WG9387_k961h.py
new file mode 100644
index 0000000..ac0b93e
--- /dev/null
+++ b/verify/probes/probe_WG9387_k961h.py
@@ -0,0 +1,352 @@
+# -*- coding: utf-8 -*-
+"""W-G.9-387 量測器（發單端擬·檔 F31·⛔ 由受單側改一字）：合併單位之原街廓之擇定（`K-9-61` ⑧ 之 KL 補裁
+`2026-10-17 14:55` 第 1 點／`15:23`「甲」）——調配之輸入盤點（`adj_intake`）。
+
+KL 之裁（要旨）：歸戶之建築街廓內不能分配之土地分處二以上之街廓者，原街廓 ＝ 各街廓之分不到土地之應分配面積
+（原投影位置之 G·同一合併單元只計一次）之**和**較大者；以 `0.01 ㎡` 為單位而相同 ⇒ 各街廓之分不到土地之**重劃前面積
+之和**較大者；再相同 ⇒ 各街廓之分不到土地中**最小之暫編地號**較小者（`K-9-67` 之序·`k967_rank`）。⛔ 停機。
+
+子命令（一律 python verify/probes/probe_WG9387_k961h.py <子命令> …）：
+  selftest <repo>
+           合成之例（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `ADJ_*` 常數與 `adj_intake`、`k967_rank`、`adj_q2`·期值皆發單端手算）：
+             K1 應分配面積之和大者先於重劃前面積與暫編地號（B2 之 G 25 ＞ B1 之 10；B1 之面積大、暫編地號小）⇒ B2；
+             K2 G 以 0.01 ㎡ 為單位相同（25.001／25.004 ⇒ 皆 25.00）⇒ 重劃前面積之和大者（B1 80 ＞ B2 40）⇒ B1；
+             K3 G 與重劃前面積皆同 ⇒ 最小之暫編地號小者（B1 之 `q7` ＞ B2 之 `q3`）⇒ B2·⛔ 停機；
+             K4 逐街廓之和（甲）而非逐筆之最大（乙）：B1 二筆 G 20＋15 ＝ 35、B2 一筆 30 ⇒ B1；
+             K5 同一入池閘之合併單元之 G 只計一次：B1 之單元（二成員）G 40、B2 G 45 ⇒ B2（重計則 B1 80）；
+             K6 重劃前面積 ＝ 原有面積（部分併出者為剩下）：B1 之 a 分攤 100·段三部分併出 70 ⇒ 30；B2 之 b 50；G 同 ⇒ B2；
+             K7 重劃前面積之和計及合併單元之全部成員：B1 之單元（60＋30 ＝ 90）、B2 80·G 同 ⇒ B1；
+             K8 代表之暫編地號取最小者（B1 之 `p9` 30 ㎡／`p1` 20 ㎡、B2 之 `p5` 50 ㎡·G、面積之和皆同）⇒ B1；
+             K9 0.01 ㎡ 之四捨五入：G 25.004 ⇒ 25.00、25.006 ⇒ 25.01（差 ≤ 0.01 而不同）⇒ 後者之街廓；
+             K10 重劃前面積以 0.01 ㎡ 為單位相同（80.001／80.004）⇒ 暫編地號（B1 之 `r2` ＜ B2 之 `r4`）⇒ B1；
+             K11 三街廓（G 30／30／29.99·面積 50／60／99）⇒ 面積大之 B2；
+             K12 唯一街廓 ⇒ 之（⛔ 受新序之影響）；
+             K13 原街廓之據 ＝ 各街廓之 G 之和（顯示照舊·⛔ 混入面積）；
+             K14 公設地／道路上之土地⛔ 計入重劃前面積（C1 之 500 ㎡）·G 同 ⇒ 面積大之 B2；
+             K15 暫編地號之比較 ＝ 字串之序（`K-9-67`·`B1` 之 `x10` ＜ `B2` 之 `x9`）⇒ B1。
+           （新碼之突變之判別力：發單端於原型施之〔本單 `§一`〕；以受單側之碼之字樣為錨之突變另單補寫。）
+  wiring   <repo> <基準>
+           AST：X1 `adj_intake` 內⛔「應分配面積並列」之字樣、⛔ `_cands`；X2 `adj_intake` 內恰一處呼 `k967_rank`
+           （三引數）；X3 `app.py` 之頂層節點對基準之相異 ⊆ {`adj_intake`}、頂層之名之集 ＝ 基準之集（`k967_rank`、`adj_q2`
+           ⛔ 改）；X4 `adj_intake` 內⛔ 案件字面（街廓名、地號）；X5 `verify/` 之生產碼對基準⛔ 改。
+  run      <repo> [<退縮> …]
+           harness 實跑本案（預設 `3.5`、`0.0`）：R1 盤點⛔ 停機；R2 原街廓之據跨二以上街廓之建地軌單位之集與其據
+           （逐街廓之 G 之和·`0.01 ㎡`）＝ 外部錨（`W-G.9-387` 擬單時於主線 `34736ab` 之盤點〔舊碼〕所得）；R3 各建地軌單位之
+           原街廓 ＝ 本器另寫之三鍵（⛔ 呼 `k967_rank`）之首，且 R2 之單位 ＝ 外部錨。
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
+FUNCS = ["adj_intake", "k967_rank", "adj_q2"]
+CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
+BUR = {"B1": "可建築土地", "B2": "可建築土地", "B3": "可建築土地", "C1": "共同負擔"}
+#: 外部錨（R2／R3）：主線 `34736ab`（舊碼·`W-G.9-387` 開工態）之 harness 盤點之原街廓之據（跨二以上街廓之建地軌單位）
+#:   與其原街廓（舊碼取 G 之和最大者；三單位皆差 ≫ 0.01 ㎡ ⇒ 新序之首同之）。發單端以 `probe_WG9351_intake.py run` 實跑所得。
+ANCHOR = {
+    3.5: {"G011": ({"R2": "3.81", "R3": "92.46"}, "R3"), "G025": ({"R5": "0.99", "R6": "0.26"}, "R5"),
+          "G030": ({"R2": "27.55", "R3": "28.34"}, "R3")},
+    0.0: {"G011": ({"R2": "3.81", "R3": "88.63"}, "R3"), "G025": ({"R5": "0.99", "R6": "0.26"}, "R5"),
+          "G030": ({"R2": "27.55", "R3": "24.88"}, "R2")},
+}
+
+
+def _read(repo, rel):
+    with open(os.path.join(repo, rel), encoding="utf-8") as f:
+        return f.read()
+
+
+def _top_nodes(src):
+    """頂層之名 ⇒ 其原文（頂層之節點皆起於第 0 欄 ⇒ 以其列之區間〔含裝飾〕取之·同名者以最後一者）。"""
+    out, ls = {}, src.split("\n")
+    for n in ast.parse(src).body:
+        k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
+            n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1
+            and isinstance(n.targets[0], ast.Name) else None)
+        if k:
+            st = min([n.lineno] + [x.lineno for x in getattr(n, "decorator_list", [])])
+            out[k] = "\n".join(ls[st - 1:n.end_lineno])
+    return out
+
+
+def _extract_ns(src):
+    """自 `app.py` 以 AST 抽出 `ADJ_*` 常數與 `FUNCS`，於隔離之命名空間執行（缺 ⇒ `KeyError`）。"""
+    tree = ast.parse(src)
+    parts, got = [], set()
+    for node in tree.body:
+        if isinstance(node, ast.FunctionDef) and node.name in FUNCS:
+            parts.append(ast.get_source_segment(src, node))
+            got.add(node.name)
+        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
+                and node.targets[0].id.startswith("ADJ_"):
+            parts.append(ast.get_source_segment(src, node))
+    if got != set(FUNCS):
+        raise KeyError(f"受詞缺 {sorted(set(FUNCS) - got)}")
+    ns = {}
+    exec(compile("\n\n".join(parts), "<k961h_extract>", "exec"), ns)
+    return ns
+
+
+def _t(pid, lot, blk, a, **kw):
+    d = {"暫編地號": pid, "原地號": lot, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0, "重劃前地價區段": "z"}
+    d.update(kw)
+    return d
+
+
+def _home(ns, temp, build, rows, drops, own=None):
+    own = own or {t["原地號"]: "GA" for t in temp}
+    it = ns["adj_intake"](temp, build, rows, drops, own, BUR)
+    us = [u for u in it["units"] if u["歸戶"] == "GA"]
+    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))
+
+
+def _cases(ns):
+    out = []
+
+    def run(name, fn, exp):
+        try:
+            got = fn()
+        except Exception as e:  # noqa: BLE001
+            got = ("例外", type(e).__name__, str(e)[:80])
+        out.append((name, got, exp))
+
+    def two(pa, ga, pb, gb, ida="a", idb="b"):
+        temp = [_t(ida, "L1", "B1", pa), _t(idb, "L2", "B2", pb)]
+        drops = {("B1", "left"): [{"暫編地號": ida, "G(㎡)": ga}], ("B2", "right"): [{"暫編地號": idb, "G(㎡)": gb}]}
+        return temp, [dict(t) for t in temp], [], drops
+
+    run("K1 應分配面積之和先於面積與暫編地號", lambda: _home(ns, *two(500.0, 10.0, 40.0, 25.0)), "B2")
+    run("K2 G 以 0.01 ㎡ 同 ⇒ 重劃前面積之和大者", lambda: _home(ns, *two(80.0, 25.001, 40.0, 25.004)), "B1")
+    run("K3 G、面積皆同 ⇒ 最小暫編地號小者·⛔ 停機",
+        lambda: _home(ns, *two(50.0, 12.0, 50.0, 12.0, "q7", "q3")), "B2")
+    # K4：B1 二筆（20＋15）、B2 一筆 30
+    t4 = [_t("a1", "L1", "B1", 10.0), _t("a2", "L2", "B1", 10.0), _t("b1", "L3", "B2", 100.0)]
+    d4 = {("B1", "left"): [{"暫編地號": "a1", "G(㎡)": 20.0}, {"暫編地號": "a2", "G(㎡)": 15.0}],
+          ("B2", "left"): [{"暫編地號": "b1", "G(㎡)": 30.0}]}
+    run("K4 逐街廓之和（甲）", lambda: _home(ns, t4, [dict(t) for t in t4], [], d4), "B1")
+    # K5：B1 之入池閘合併單元（m1＋m2·G 40 只計一次）、B2 之 k1 G 45
+    t5 = [_t("m1", "L1", "B1", 60.0), _t("m2", "L2", "B1", 30.0), _t("k1", "L3", "B2", 10.0)]
+    b5 = [dict(t5[0], 入池閘併入=["m1", "m2"]), dict(t5[2])]
+    d5 = {("B1", "left"): [{"暫編地號": "m1", "G(㎡)": 40.0}], ("B2", "left"): [{"暫編地號": "k1", "G(㎡)": 45.0}]}
+    run("K5 合併單元之 G 只計一次", lambda: _home(ns, t5, b5, [], d5), "B2")
+    # K6：B1 之 a 部分併出（分攤 100·段三部分併出 70 ⇒ 剩下 30）予已配地之 c（B3）；B2 之 b 50；G 同 12
+    t6 = [_t("a", "L1", "B1", 100.0, 段三部分併出={"c": 70.0}, 段三併出=["c"]), _t("b", "L2", "B2", 50.0),
+          _t("c", "L3", "B3", 200.0)]
+    d6 = {("B1", "left"): [{"暫編地號": "a", "G(㎡)": 12.0}], ("B2", "left"): [{"暫編地號": "b", "G(㎡)": 12.0}]}
+    run("K6 重劃前面積 ＝ 原有面積（部分併出者為剩下）",
+        lambda: _home(ns, t6, [dict(t) for t in t6], [{"暫編地號": "c", "推進側別": "left"}], d6,
+                      own={"L1": "GA", "L2": "GA", "L3": "GZ"}), "B2")
+    # K7：B1 之單元（m1 60＋m2 30）、B2 之 k1 80；G 同 40
+    t7 = [_t("m1", "L1", "B1", 60.0), _t("m2", "L2", "B1", 30.0), _t("k1", "L3", "B2", 80.0)]
+    b7 = [dict(t7[0], 入池閘併入=["m1", "m2"]), dict(t7[2])]
+    d7 = {("B1", "left"): [{"暫編地號": "m1", "G(㎡)": 40.0}], ("B2", "left"): [{"暫編地號": "k1", "G(㎡)": 40.0}]}
+    run("K7 重劃前面積之和計及單元之全部成員", lambda: _home(ns, t7, b7, [], d7), "B1")
+    # K8：B1 之 p9（G 5、面積 30）／p1（G 5、面積 20）、B2 之 p5（G 10、面積 50）
+    t8 = [_t("p9", "L1", "B1", 30.0), _t("p1", "L2", "B1", 20.0), _t("p5", "L3", "B2", 50.0)]
+    d8 = {("B1", "left"): [{"暫編地號": "p9", "G(㎡)": 5.0}, {"暫編地號": "p1", "G(㎡)": 5.0}],
+          ("B2", "left"): [{"暫編地號": "p5", "G(㎡)": 10.0}]}
+    run("K8 代表之暫編地號取最小者", lambda: _home(ns, t8, [dict(t) for t in t8], [], d8), "B1")
+    run("K9 0.01 ㎡ 之四捨五入（25.004 ⇒ 25.00；25.006 ⇒ 25.01）",
+        lambda: _home(ns, *two(900.0, 25.004, 10.0, 25.006)), "B2")
+    run("K10 面積以 0.01 ㎡ 同 ⇒ 暫編地號",
+        lambda: _home(ns, *two(80.001, 7.0, 80.004, 7.0, "r2", "r4")), "B1")
+    t11 = [_t("a", "L1", "B1", 50.0), _t("b", "L2", "B2", 60.0), _t("c", "L3", "B3", 99.0)]
+    d11 = {("B1", "left"): [{"暫編地號": "a", "G(㎡)": 30.0}], ("B2", "left"): [{"暫編地號": "b", "G(㎡)": 30.0}],
+           ("B3", "left"): [{"暫編地號": "c", "G(㎡)": 29.99}]}
+    run("K11 三街廓", lambda: _home(ns, t11, [dict(t) for t in t11], [], d11), "B2")
+    t12 = [_t("a", "L1", "B1", 50.0), _t("x", "L2", "B2", 70.0)]
+    run("K12 唯一街廓（他街廓之宗配地）",
+        lambda: _home(ns, t12, [dict(t) for t in t12], [{"暫編地號": "x", "推進側別": "left"}],
+                      {("B1", "left"): [{"暫編地號": "a", "G(㎡)": 3.0}]}), "B1")
+
+    def k13():
+        temp, build, rows, drops = two(80.0, 25.001, 40.0, 25.004)
+        it = ns["adj_intake"](temp, build, rows, drops, {"L1": "GA", "L2": "GA"}, BUR)
+        return {b: round(v, 6) for b, v in it["units"][0]["原街廓之據"].items()}
+    run("K13 原街廓之據 ＝ 各街廓之 G 之和", k13, {"B1": 25.001, "B2": 25.004})
+    t14 = [_t("a", "L1", "B1", 40.0), _t("b", "L2", "B2", 60.0), _t("r", "L1", "C1", 500.0)]
+    d14 = {("B1", "left"): [{"暫編地號": "a", "G(㎡)": 9.0}], ("B2", "left"): [{"暫編地號": "b", "G(㎡)": 9.0}]}
+    run("K14 公設地／道路上之土地⛔ 計入", lambda: _home(ns, t14, [dict(t) for t in t14[:2]], [], d14), "B2")
+    run("K15 暫編地號之比較 ＝ 字串之序", lambda: _home(ns, *two(30.0, 6.0, 30.0, 6.0, "x10", "x9")), "B1")
+    return out
+
+
+def selftest(repo):
+    try:
+        ns = _extract_ns(_read(repo, "app.py"))
+    except Exception as e:  # noqa: BLE001
+        print(f"  🔴 K0 受詞缺：{e}")
+        print("⇒ 紅 ['K0']；rc 1")
+        return 1
+    print("── 合成之例（AST 抽出之 adj_intake／k967_rank／adj_q2）──")
+    red = []
+    for name, got, exp in _cases(ns):
+        ok = got == exp
+        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
+        if not ok:
+            red.append(name.split()[0])
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def _fn(tree, name):
+    for n in tree.body:
+        if isinstance(n, ast.FunctionDef) and n.name == name:
+            return n
+    return None
+
+
+def _wiring_checks(repo, base):
+    res = []
+    src = _read(repo, "app.py")
+    tree = ast.parse(src)
+    f = _fn(tree, "adj_intake")
+    if f is None:
+        return [("X0 adj_intake 在", False, "缺")]
+    strs = [n.value for n in ast.walk(f) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
+    jst = [n for n in ast.walk(f) if isinstance(n, ast.JoinedStr)]
+    jtxt = [v.value for j in jst for v in j.values if isinstance(v, ast.Constant) and isinstance(v.value, str)]
+    names = {n.id for n in ast.walk(f) if isinstance(n, ast.Name)}
+    bad1 = [s for s in strs + jtxt if "應分配面積並列" in s]
+    res.append(("X1 adj_intake 內⛔「應分配面積並列」、⛔ _cands", not bad1 and "_cands" not in names,
+                f"字樣 {len(bad1)}／_cands {'_cands' in names}"))
+    calls = [n for n in ast.walk(f) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "k967_rank"]
+    res.append(("X2 adj_intake 內恰一處呼 k967_rank（三引數）",
+                len(calls) == 1 and len(calls[0].args) == 3 and not calls[0].keywords, f"{len(calls)} 處"))
+    try:
+        bsrc = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True,
+                              check=True).stdout.decode("utf-8")
+        btop, ctop = _top_nodes(bsrc), _top_nodes(src)
+        dif = sorted(k for k in set(btop) | set(ctop) if btop.get(k) != ctop.get(k))
+        res.append(("X3 頂層之相異 ⊆ {adj_intake}、頂層之名之集 ＝ 基準", set(dif) <= {"adj_intake"} and set(btop) == set(ctop),
+                    f"相異 {dif}"))
+    except Exception as e:  # noqa: BLE001
+        res.append(("X3 頂層之相異 ⊆ {adj_intake}、頂層之名之集 ＝ 基準", False, f"{type(e).__name__}: {e}"))
+    lits = sorted({s for s in strs if CASE_LIT_RE.match(s)})
+    res.append(("X4 adj_intake 內⛔ 案件字面", not lits, f"{lits}"))
+    try:
+        d = subprocess.run(["git", "-C", repo, "diff", "--name-only", base, "--", "verify/*.py"], capture_output=True,
+                           check=True).stdout.decode("utf-8").split()
+        d = [p for p in d if re.match(r"^verify/[^/]+\.py$", p)]
+        res.append(("X5 verify/ 之生產碼對基準⛔ 改", d == [], f"{d}"))
+    except Exception as e:  # noqa: BLE001
+        res.append(("X5 verify/ 之生產碼對基準⛔ 改", False, f"{type(e).__name__}: {e}"))
+    return res
+
+
+def wiring(repo, base):
+    red = []
+    print(f"── 接線（AST·基準 {base}）──")
+    for name, ok, note in _wiring_checks(repo, base):
+        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
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
+    """本器另寫之三鍵（⛔ 呼 `k967_rank`）：G 之和（據）→ 不能分配者之原有面積之和 → 其最小之暫編地號。"""
+    pre, pid = {}, {}
+    for r in unit["建築街廓內不能分配"]:
+        b = r["所屬街廓"]
+        pre[b] = pre.get(b, 0.0) + float(r["原有面積"])
+        pid[b] = min(pid.get(b, str(r["暫編地號"])), str(r["暫編地號"]))
+    ks = sorted(unit["原街廓之據"], key=lambda b: (-_q2(unit["原街廓之據"][b]), -_q2(pre[b]), pid[b]))
+    return ks[0]
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
+        if "adj_intake" not in ns:
+            print("  🔴 R0 受詞缺：adj_intake")
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
+                it = ns["adj_intake"](tp3, k9["build"], sg["g_rows"], drops, own, bur)
+            except RuntimeError as e:
+                print(f"  🔴 R1 盤點停機：{str(e)[:300]}")
+                red.append(f"R1@{sb}")
+                continue
+            print("  ✅ R1 盤點⛔ 停機")
+            bu = [u for u in it["units"] if u["軌"] == ns["ADJ_TRACK_BUILD"]]
+            multi = {u["歸戶"]: ({b: str(_q2(v)) for b, v in u["原街廓之據"].items()}, u["原街廓"])
+                     for u in bu if len(u["原街廓之據"]) >= 2}
+            for g, (bs, h) in sorted(multi.items()):
+                print(f"     {g}：據 {bs} ⇒ 原街廓 {h}")
+            exp = ANCHOR.get(sb)
+            ok2 = exp is not None and {g: v[0] for g, v in multi.items()} == {g: v[0] for g, v in exp.items()}
+            print(("  ✅" if ok2 else "  🔴") + f" R2 跨二以上街廓之建地軌單位（{len(multi)}）之據 ＝ 外部錨")
+            if not ok2:
+                red.append(f"R2@{sb}")
+            bad3 = [u["歸戶"] for u in bu if u["原街廓"] != _indep_home(u)]
+            ok3 = not bad3 and exp is not None and {g: v[1] for g, v in multi.items()} == {g: v[1] for g, v in exp.items()}
+            print(("  ✅" if ok3 else "  🔴") + f" R3 建地軌單位（{len(bu)}）之原街廓 ＝ 另寫之三鍵之首、跨街廓者 ＝ 外部錨："
+                  f"不符 {bad3}")
+            if not ok3:
+                red.append(f"R3@{sb}")
+    finally:
+        os.chdir(cwd)
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def main(argv):
+    if len(argv) < 3 or argv[1] not in ("selftest", "wiring", "run") or (argv[1] == "wiring" and len(argv) < 4):
+        print(__doc__)
+        return 2
+    repo = os.path.abspath(argv[2])
+    if argv[1] == "selftest":
+        return selftest(repo)
+    if argv[1] == "wiring":
+        return wiring(repo, argv[3])
+    return run(repo, [float(x) for x in argv[3:]] or [3.5, 0.0])
+
+
+if __name__ == "__main__":
+    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `K29`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

---

## 🔧 `W-G.9-387`：`K-9-61` ⑧ 之 KL 補裁（合併單位之原街廓：各街廓之分不到土地之應分配面積之和 → 重劃前面積之和 → 最小之暫編地號）；段三後處理 (a) 之跨分配線併入不論地號（`K-9-48` 讀法 3 維持）；射程之重分；`ops/queue` 規則檔之修訂之登記（⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）之後；本節由 `W-G.9-387`（新側支 `verify/W-G.9-387-k961h`）入。**授權** ＝ 本典 `W-G.9-386` 之節之一之 KL 之逐字（自動化之委任）；本單之 `expects_allocation_change` ＝ `false`。

### 一、發單端之請示與 KL 之答（逐字）

**發單端之請示**（`ops/queue` 之 `待KL/2026-10-17_K-9-61之二題.md`·`2026-10-17 14:05`·其一、二之【要你判斷】·逐字）：

> 【要你判斷】兩街廓並列時，以哪一筆的暫編地號代表該街廓來比？（甲：該街廓分不到土地中暫編地號最小者／乙：該街廓分不到土地中重劃前面積最大者）

> 【要你判斷】段三的這類併入，是否也照 10/13 限同一筆地號？（是：照建議／否：維持現行，不論地號）

**KL** `2026-10-17 14:55`（`Asia/Taipei`·`ops/queue` 之 `KL答覆/2026-10-17_1455.md`·逐字）：

> 1. 問一：先問你所謂的628-9(1) 30 ㎡、628-5(2) 10 ㎡，在 R4 有 628-7(1) 40 ㎡，這些原面積是指原位次計算的G值，還是重劃前面積？本題我看你要我回答的問題，程式好像未可分配之土地其"應分配面積"就視為0，但是就算不能分配也是有原投影位置先算G值(G值就是指應分配面積)，但因為G值太小導致內接矩形等驗證不過才屬未分配到土地，所以本題應該是往原投影位置計算之應分配面積G值最大者合併，所以原街廓是指應分配面積最大者，若G值相同再比重劃前面積，若重劃前面積再相同，就依分不到土地中暫編地號最小者
> 2. 問二：採現行，原因：街角第是地主最在意的位置(價值高)，所以既然相鄰的街角地有一側已經街角地評選機制為勝者，且若另一側也是經解屌地評選後確定分配不到的情形下(但2側土地相連不論地號，如附圖2)，則採現狀將另一側相連但不能分配的土地併入評選街角地winner土地。

**發單端之續請示**（`待KL/2026-10-17_K-9-61之二題_續.md`·`14:58`·其【要改成】與【要你判斷】·逐字）：

> 【要改成】
> - **甲（現行之延續）**：各街廓分不到土地的 G 加總後比；相同再比各街廓分不到土地的重劃前面積合計；再相同，比各街廓分不到土地中暫編地號最小者。
> - **乙**：逐筆比——分不到土地中 G 最大的那一筆所在之街廓；G 相同再比該筆的重劃前面積；再相同，取暫編地號最小者所在之街廓。

> 【要你判斷】您所說「應分配面積最大者」是指甲（各街廓加總）還是乙（單筆最大）？

**KL** `2026-10-17 15:23`（`KL答覆/2026-10-17_1523.md`·逐字）：

> 甲

### 二、補裁之內容（附於 `K-9-61` ⑧·⛔ 新號）

**⑧ 之補**（KL `14:55` 第 `1` 點 ＋ `15:23`「甲」）：合併單位之原街廓（`K-9-46`（三））——該歸戶之建築街廓內不能分配之土地分處二以上之街廓者，各街廓依下列之序比之，取其首：
1. 該街廓之分不到之土地之**應分配面積之和**（於原投影位置計算之 `G`·即該趟之 `G`；同一合併單元〔入池閘之併入〕只計一次）較大者；
2. 相同 ⇒ 該街廓之分不到之土地之**重劃前面積之和**較大者；
3. 再相同 ⇒ 該街廓之分不到之土地中**最小之暫編地號**較小者。

⑧ 之原文之「取該街廓內原有面積合計較大者」⇒ 讀為上開 2（重劃前面積·`K-9-67`）；「再同取暫編地號字典序小者」⇒ 讀為上開 3（其受詞 ＝ 各街廓之分不到之土地中之最小者）。KL 之語「程式好像未可分配之土地其"應分配面積"就視為0」之疑：程式於分不到之土地亦於原投影位置照算 `G`（`adj_intake` 之 `應分配面積` ＝ 該趟之不配地紀錄之 `G(㎡)`），⛔ 視為 `0`——發單端 `14:58` 已答（請示之圖一之例係假設 `G` 恰為 `0`·`自誤 625`）。

### 三、段三後處理 (a) 之讀法（KL `14:55` 第 `2` 點）

- `K-9-48` 讀法 3（段三後處理 (a) 之跨分配線併入·同一地主且地籍相連即可·⛔ 限同一原地號）**維持**。
- 本典 `K-9-73` 之「與既有正典之關係」之「`K-9-61` ⑥ 之……受詞唯同一筆地號（⑤）」**於段三後處理 (a) ⛔ 適用**：段三後處理 (a) 之所鄰之可建築街廓（B 內）為二以上者依 `K-9-61` ⑥ 之「向應分配面積較大之一側併」、為零者依 `K-9-51`／`K-9-71`——皆不論地號。其落地（`k6b_stage3_run` 之停機之改）另單（`W-G.9-388`）；本單⛔ 改碼。
- `K-9-73` 於手冊先行（依手冊併入地主已配得之宗）之射程⛔ 變。

### 四、【工】之讀法（發單端·⛔ 充裁·於每日摘要告 KL）

- **甲 重劃前面積**：`adj_intake` 之逐切片之 `原有面積`（分攤登記面積；段三或排配地時之部分併出者為其剩下）——即 `K-9-67` 之重劃前面積（`k967_pre_area` 之 `area_of` 之式·`W-G.9-380`）。共同負擔用地上之土地⛔ 計（原街廓唯取建築街廓）。
- **乙 應分配面積之和**：同開工態之 `原街廓之據`（每一合併單元只計一次·計入其不配地紀錄之街廓）；顯示照舊。
- **丙 比較之單位**：三鍵之比以 `k967_rank`（`K-9-67` 之序鍵·`adj_q2` 四捨五入至 `0.01`·暫編地號以字串之序）為單一真相源。
- **丁 停機**：暫編地號唯一 ⇒ 第三鍵恆分 ⇒ 開工態之「原街廓之應分配面積並列 ⇒ 停機（【未裁】）」去之。
- **戊 本案**：建地軌之合併單位中原街廓之據跨二街廓者唯三（`3.5 m`：`G011` `R2 3.81`／`R3 92.46`、`G025` `R5 0.99`／`R6 0.26`、`G030` `R2 27.55`／`R3 28.34`；`0 m`：`G011` `R2 3.81`／`R3 88.63`、`G025` 同、`G030` `R2 27.55`／`R3 24.88`）——皆以第一鍵分（差 ≫ `0.01 ㎡`）⇒ 原街廓⛔ 變、配地⛔ 變（`W-G.9-387` 之 `F31 run`）。
- **己 射程之重分**（工程裁·唯序·⛔ 涉土地後果）：`K-9-61` 之餘款與 `GB-205` 依機制分單——`W-G.9-388` ＝ 段三後處理之五停機（`K-9-61` ①②③④⑥·含上開三之讀法）；`W-G.9-389` ＝ ⑤ 之還原（`GB-205`·段三、手冊先行所受之土地）＋ 試算內之「程式未支援」之停機之上拋；`W-G.9-390` ＝ `K-9-60`；`W-G.9-391` ＝ `K-9-59`＋`K-9-63`。`14:05` 之請示之通知 `3` 稱 `W-G.9-387` 含段三五停機——由此改（於每日摘要彙報）。
- **庚 號**：本補裁附於 `K-9-61` ⑧，⛔ 鑄新號（自動輪之發單端⛔ 鑄 `K-9` 之號）。

### 五、`K-9-61` 之落地狀態（⛔ 改上文之「①〜⑧ ⬜」·依本節讀之）

⑧（含本節之補）⇒ 🔶（新側支 `verify/W-G.9-387-k961h`·入主線另單）；⑦ ⇒ ✅（`W-G.9-373`·`k953_manual_run._gtop953` 依 `k967_rank`）；①②③④⑤⑥ ⇒ ⬜（`W-G.9-388`／`389`）。

### 六、`ops/queue` 規則檔之修訂之登記（本典 `W-G.9-386` 之節之二之戊）

`W-G.9-386` 之後之修訂（皆⛔ 放寬乙之任一款·`ops/queue` 之 `log.md` 各有其列）：`README_自動化運作規則.md` 第六節第 `2`、`3` 款（`python3 -m pip`；核數 `2`〜`4`·`09:12`）、第八節第 `3` 款（有事之輪記 `effort`·`13:41`）；`發單端.md` 丙之第 `1` 步之 🔒 款（判「全無」前逐序具據·收緊·`11:41`）、己（一輪持續工作至完成·`13:35`）。其現值（`W-G.9-387` 出單時）：`README_自動化運作規則.md` `9613` B·`sha256` `fe5be89767192c7ba45bfc4da8c5d6c855b836de3b6c2863408bbe0e411bdf68`；`執行端.md` `3289` B·`5247541c09654988376aeeeef88ce3503412058f1cd7dca38f1b956f91655ee7`（⛔ 變）；`發單端.md` `8305` B·`de1063793de6511ae9f05379aeac1ba685486b6bf9212b50fbe2e08138ca14b2`；`每日摘要.md` `768` B·`109cc9d5e0c0af604b01191809f19ef58ae8cb272c878f4b0d5797a0ff2f78b5`（⛔ 變）。
````

## 附錄丙　塊 `E31`（附於 `docs/reports/W-G.9波_claude.ai側自誤登記.md` 之末·工項三）

````markdown

---

**取號**（`W-G.9-387 §一` 項 `2`）：本批取 `624`、`625`（`2` 號）。

### 🩸 `自誤 624`　**`2026-10-17 10:30` 之請示「下一個方向」判待落地清單已無可自動處理之項目，而漏列序 `8`（`GB-205`）與序 `9`（`K-9-59`〜`K-9-61`、`K-9-63`·皆有 KL 之逐字裁示）——以「依賴未完成」概括而未逐序具其裁示之出處（發單端·自動輪）**

**形**：`ops/queue` 之 `待KL/2026-10-17_下一個方向.md` 之【現況】唯列四項（`K-9-62` 之指配、調配後半、最小建築面積之取值、待查三項），⛔ 列序 `8`、`9`；其【要你判斷】之選項亦⛔ 及之。`STATE.json` 因之設 `await_kl`（README 第二節第 `6` 款）。
**後果之界**：零土地後果（⛔ 出單、⛔ 改碼）；KL 須答一次（`12:40`「丙」·其內容即序 `8`、`9`）；自動化之流程停約二小時。
**根因**：判「全無」時以待落地清單之依賴序之文字（「序 `9`……其序另呈 KL」「序 `8` 於序 `9` 之前或併之」）為「不能自動處理」之據，未對每一序查 `K-6` 典之裁示之有無；「其序另呈 KL」於自動化下屬「純屬工序之先後」（README 第二節自動處理第 `4` 款）而誤為停止之由。
**後果之框**：🟡 發單側窗八十七之審捕之（`11:41`·`log.md`）。
**裁**：⛔ 涉 KL 之裁；本號唯登記。
**攔法**：`發單端.md` 丙之第 `1` 步之 🔒 款（`11:41` 增·收緊）：判「全無」前逐序寫明其裁示之出處、有無 KL 之逐字、不能自動處理之具體依據（引正典之段·⛔ 以「依賴未完成」概括）；請示列全部之序。

### 🩸 `自誤 625`　**`2026-10-17 14:05` 之請示「K-9-61 之二題」之問一之例（圖一）以「三筆都分不到、應分配面積皆 0」示並列，而未言明所標之 30／10／40 ㎡ 為重劃前面積、亦未言明分不到之土地之應分配面積係於原投影位置照算之 `G`——KL 因而問「這些原面積是指原位次計算的G值，還是重劃前面積？」並疑「程式好像未可分配之土地其"應分配面積"就視為0」（發單端·自動輪）**

**形**：請示之問一之【對土地的影響】與 `圖一_原街廓並列之暫編地號.png`：例之三筆僅標面積（未標其為何種面積）、並以「應分配面積皆 0」述之；問題之文字亦未述分不到之土地之 `G` 之由來。
**後果之界**：零土地後果；KL 須另答一次（`14:55` 第 `1` 點附問 ⇒ `14:58` 之續請示 ⇒ `15:23`「甲」）。若 KL 依「應分配面積視為 0」之誤解裁之，原街廓之第一鍵將被讀為恆同、改以面積比——與 KL 之本意（`G` 最大者）相反（已由附問攔之）。
**根因**：示意之例取極端之值（`G` 恰為 `0`）以呈並列，而未於例中並列「`G` 照算、本例假設其恰為 `0`」之前提；呈 KL 之例之量未逐一具名其種類（重劃前面積、應分配面積、原有面積）。
**後果之框**：🟡 KL 之附問捕之（同日·擬單之前）。
**裁**：⛔ 涉 KL 之裁（KL 之裁見 `K-6` 典 `W-G.9-387` 之節）；本號唯登記。
**攔法**：呈 KL 之例凡含面積之數者，逐數具名其種類；以極端之值（如 `G` ＝ `0`）示意者，於例中明言其為假設及其在程式中之由來；例須至少一組非極端之值（使各鍵皆可見其作用）。
````

## 附錄丁　塊 `P40`（附於 `CLAUDE.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`K-9-61` ⑧ 之 KL 補裁入新側支；段三後處理 (a) 之讀法；射程之重分（`W-G.9-388`〜`391`）；`自誤 624`、`625`（`W-G.9-387`·⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`（`W-G.9-386` 工項二）之後；本批之碼在新側支 `verify/W-G.9-387-k961h`。狀態用三態（✅ 已落地／🔶 部分落地／⬜ 未落地）。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `1` | `K-9-61` ⑧ ＋ 其 KL 補裁（`2026-10-17 14:55` 第 `1` 點、`15:23`「甲」） | 合併單位之原街廓 ＝ 各街廓之分不到土地之應分配面積之和 → 重劃前面積之和 → 最小之暫編地號（`0.01 ㎡`·`k967_rank`）；並列之停機去之 | 🔶（新側支·候復驗與入主線之短單） | `K-6` 典 `W-G.9-387` 之節之二、四；`docs/orders/W-G.9-387_規格單.md` |
| `2` | 段三後處理 (a) 之跨分配線併入（KL `14:55` 第 `2` 點） | `K-9-48` 讀法 3 維持（不論地號）；`K-9-73` 之「⑥ 之受詞唯同一筆地號」於段三⛔ 及 | ✅（讀法入典·碼⛔ 改） | `K-6` 典 `W-G.9-387` 之節之三 |
| `3` | `K-9-61` ①②③④⑥（前節序 `9` 之一） | 段三後處理之五停機改依 `K-9-61`（受併宗之擇定、未保留者還原而由下一名續試、所鄰街廓二以上或零者） | ⬜ | `W-G.9-388` |
| `4` | `K-9-61` ⑤、`GB-205`（前節序 `8`）；試算內之「程式未支援」之停機之上拋 | 段三、手冊先行所受之土地於承受之宗事後未配得者之還原；`_chk953`／`_chk_a4`／`_try965` 之試算中之停機⛔ 吞為「不過」 | ⬜ | `W-G.9-389` |
| `5` | `K-9-60`（前節序 `9` 之一） | 末端塊競合三形（依 `K-9-49`、`K-9-50` 既有步驟推延·解 `GB-194`） | ⬜ | `W-G.9-390` |
| `6` | `K-9-59`、`K-9-63`（前節序 `9` 之一） | 讀圖側（道路 `BLOCK` 之 `CENTERLINE`、`JUNCTION`、`JOINLINE`、圓弧正街、L 形、判側、地籍缺漏警示） | ⬜ | `W-G.9-391` |
| `7` | `K-9-62` 之指配（前節序 `3`） | 公有土地依類別序指配、抵費地、按比例 | ⬜ | 另單 |
| `8` | harness 之 `blk5` 之最小建築面積 ＝ `{}` vs 畫面之有效值（前節序 `6`） | 二者之源之統一 | ⬜ | 另單（⛔ 急·KL `12:40`「丙」暫緩） |
| `9` | `K-9-78`（前節序 `7`） | 調配之畫面入口 | ⬜ | 新調配程式之規格單（規格步 `5`〜`8`） |
| `10` | 畫面於 step G 之後再跑段三而未再跑 step G 者之調配之輸入之顯示（前節序 `10`） | 待查 | ⬜ | 另單（⛔ 急） |
| `11` | 清冊之顯示（前節序 `11`） | 清冊依原地號合併顯示，與配地時之合併不一定相同 | ⬜ | 另單（⛔ 急） |
| `12` | 檢核唯及受影響之街廓（`_chk953`／`_chk_a4`／`_chk965`） | 其外之街廓之保留之失⛔ 被查——唯讀審查之碼面推論、未實跑證之·⛔ 鑄號 | ⬜ | 待查（⛔ 急） |
| `13` | `自誤 624`、`625` | 見自誤簿 | ✅ | 同序 `1` |

🔒 **前節之更新**（⛔ 追改前節一字）：「待落地清單之更新：`W-G.9-384` 入主線；……（`W-G.9-385`）」節（及「`W-G.9-385` 入主線；自動化之委任（`W-G.9-386`）」節之更新）之序 `9` ⇒ 本表序 `1`、`3`、`5`、`6`；序 `8` ⇒ 本表序 `4`；序 `3`、`6`、`7`、`10`、`11` ⇒ 本表序 `7`〜`11`（態⛔ 變）；序 `1`、`2`、`4`、`5` ✅ ⇒ 本表⛔ 載。本表序 `2`、`12`、`13` 為新。
🔒 **本案之量**：本批⛔ 變配地（建地軌之合併單位中原街廓之據跨二街廓者三·皆以應分配面積之和分·`W-G.9-387` 規格單 `§一` 項 `5`）。
🔒 **依賴序**：序 `1`（`W-G.9-387`·入主線之短單）→ 序 `3`（`W-G.9-388`）→ 序 `4`（`W-G.9-389`）→ 序 `5`（`W-G.9-390`）；序 `6`（`W-G.9-391`）與之⛔ 相依（輸入側）；序 `7` → 規格步 `5` → `6` → `7`／`8`（新調配模組·畫面入口依序 `9`）；`GB-196`、`GB-197`、`GB-198`、`GB-202` 與序 `8`、`10`、`11`、`12` 另單（⛔ 急）。其先後依 `K-6` 典 `W-G.9-386` 之節之二之甲之④ 由發單端定之、於每日摘要彙報。
🔒 **`⬜` 之自指增長**：本節 payload 內含 `⬜` 字樣 ＝ `14`（子字串框·含圖例與本列）·列 ＝ `12`（列框·同）；凡以本檔 `⬜` 之全檔命中為量者，須扣本節之數。
````

SELF_SHA256: 8d34ec069aea35ad2651b036d68edf5c3a58938d6c60f80babd9e128878662d0
