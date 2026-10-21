# `W-G.9-391`　規格單：`K-9-80` ④⑤⑥ 與 `K-9-34` 之落地——有最小建築面積之輸入者，街角規定範圍（遠側界線 ∥ SIDELINE）與末端塊範圍（內側界線沿宗地分配線內移）擴至其面積；跨占之名單與門檻皆以擴大後之範圍；一街廓之二範圍相接或重疊、或擴至他端仍未達 ⇒ 警示停止 ＋ 序 `22` 之再分（③ ⇒ `W-G.9-392`）＋ 待落地清單之更新（新側支 `verify/W-G.9-391-k980x`）

> **本單建議等級 ＝ `high`**（生產碼 `3` 檔：`app.py` 之頂層節點九之改與六新名、`verify/stepg_pipeline.py` 之 `_run_step_g_impl`、`verify/run_verification.py` 之 `build_param_table`〔`§三-1`〕；規格與量測器皆全；本案之配地⛔ 變）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-21`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本·工項零〜四之一切 `commit` 推至**新側支 `verify/W-G.9-391-k980x`**，其起點 ＝ 主線之端 `a8657c4`）。
> **流程 ＝ 規格單**（常態）：**生產碼由執行端依 `§三` 撰寫**；發單端給規格（`§三`）、量測器（塊 `Fy46`·執行端⛔ 改一字）與驗收（`§四`）；本單⛔ 含生產碼之塊、⛔ 預載施後之生產碼之 blob（由執行端回報、發單端復驗時自倉重算）。
> **級** ＝ **中**（生產碼 `3` 檔；**本案之配地⛔ 變**〔`§一` 項 `5`〕）。KL 令：以配地結果之正確為先、⛔ 全套驗證儀式 ⇒ 本批⛔ 跑 `run_all`（`§四-1` 工項二之「⛔ 跑之由」）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`（`W-G.9-390` 入主線·補令四工項零⁗′）；遠端 heads **`50`**（皆⛔ 動）。🔒 **本批之五筆 `commit` 一律推至新側支 `verify/W-G.9-391-k980x`（工項零立之·其後皆快轉）；主線⛔ 動**（入主線另以短單·`§四-2`）。
> 🔑 **通則** ＝ `ops/queue` 之 `README_自動化運作規則.md` 第六節（雲端·Linux）：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之**絕對路徑**；`<O>` ＝ 執行端自定之倉外輸出目錄（須在任何 git 工作樹之外·其路徑載於報告）；`commit` 訊息一律 `git commit -F`；含 emoji 之器先設 `PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；一切以重導所存之出艙檔一律為 UTF-8；Bash 命令⛔ 含 heredoc。塊 `Fy46`／`K37`／`P48` 以**檔案管線**、依**圍欄之逐列索引**機械抽取並以二進位寫出（`newline='\n'`·抽取式見 `§五-1` 末）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ 遠端分支 `ops/queue` 之 `orders/W-G.9-391_規格單.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **旗標之環境**：量測之殼**⛔ 設** `WV_K6_STEP0`、`WV_K6B_STAGE3`、`WV_K929_6`、`WV_K953`、`WV_ADJ4`（先以 `python3 -c "import os;print([os.environ.get(k) for k in ('WV_K6_STEP0','WV_K6B_STAGE3','WV_K929_6','WV_K953','WV_ADJ4')])"` 出艙 `[None, None, None, None, None]`）。
> 🔑 **並行之限** ＝ README 第六節第 `3` 款：各驗之命令之同時並行數 ≤ **`2`**；逾時或 `rc` ≠ 期者，於⛔ 他負載之下**重跑一次**，二趟之出艙皆照實入報告（重跑之趟 ＝ 期 ⇒ 該呼叫以重跑之趟為準·報告具名之）。
> 🔑 **前置驗算之沿用**（`發單端.md` 丙 3之一·`執行端.md` 丙 4之一·KL `2026-10-18 19:57`）：前置之 (甲)(乙)(丙) 見 `§四-1` 工項二之前置；(丙) 之沿用以 `ops/queue` 之 `基準/a8657c4012d961eccebd77cd812c0ab6aeab030f.md` 為準，其前提之比對（主線之端、`python3 --version`、`pip freeze` 之 `sha256`）之結果入回報。
> 🔑 **撰碼中之自跑**：執行端撰碼中得自跑 `§四-1` 之諸器以自查其碼（⛔ 改器一字）；工項二之 `commit` 後之驗（`V-1`〜`V-9`）任一 ≠ 期 ⇒ 停機款 `6`。
> 🔑 **⛔ 寫 `CLAUDE.md`**（雲端之分類器拒之·KL `2026-10-17 22:42` 同意）：待落地清單之更新寫於 `docs/待落地清單.md`（塊 `P48`·純末端追加）。本單⛔ 須 `CLAUDE.md` 之改。
> 🛑 **本單⛔ 及於**：主線之任何推進；`§三-1` 所列以外之生產碼之一字與行為；生產碼 `34` 檔之中 `app.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py` 以外之 `31` 檔（含 `verify/selection_pipeline.py`、`verify/fixture_*.py`、`verify/wf_*.py`）；`§三-3` 之禁改；既有量測器除塊 `Fy46` 所改之 `11` 檔外之一字；`data/` 之一切檔、`verify/case_params_UC9898.json`、`verify/baselines`、`verify/out/`；`VR` 簿、`GB` 簿、自誤簿、恆常附款登記表、常設規則索引、`.claude/`、`docs/配地計算總規格_v3.md`、`docs/specs/`、`CLAUDE.md` 之一字；`K-6` 典、`docs/待落地清單.md` 除塊 `K37`／`P48` 之純末端追加外之一字；`ops/queue` 除 `執行端.md` 所許（`STATE.json`、`reports/`、`log.md`）外之一字；任何他側支之推送、刪除或改寫；`K-9-80` ③（微差之吸收·`W-G.9-392`）、⑦（街角之強制抵費地⛔ 作調配·調配模組）、`K-9-61` ⑤ 與 `GB-205`（`W-G.9-393`）、`K-9-60`、`K-9-59`、`K-9-63`、`K-9-62` 之指配、最小建築面積之畫面與 harness 之源之統一（待落地清單序 `6`·`GB-202`）——另單。
> 🔴 **本單⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本單未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場・取號・停機款・pre-flight

### `§零-0`　受單側之開場（**先於工項零**·⛔ 跳序）

1. 自報 context 餘量與本機之核數（`nproc`）。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`；`git ls-remote --heads origin` 之列數 ＝ **`50`**（全列存 `<O>/heads_before_391.txt`·收工閘 `5` 用），且⛔ 含 `refs/heads/verify/W-G.9-391-k980x`；施工樹 `git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 634 629` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `619`／`MAX` `634`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`（發單端於 `a8657c4` 實跑同）。
4. 本單之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本單之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗；裝之出艙存 `<O>`）；量測之殼之旗標之出艙 ＝ 單首 🔑 之期。🔎 依 `requirements.txt` 裝後，`pip freeze` 之 `certifi`、`pillow`、`websockets` 三列或異於基準（發單端 `2026-10-21` 實見）⇒ 以 `python3 -m pip install certifi==2026.10.18 pillow==12.3.0 websockets==17.2 --break-system-packages` 釘回基準之版（其出艙存 `<O>`·入回報）。
6. 版本之比對（前置 (丙) 之前提）：`python3 --version` 與 `python3 -m pip freeze` 之全文之 `sha256`，對 `ops/queue` 之 `基準/a8657c4012d961eccebd77cd812c0ab6aeab030f.md` 之「一、環境之指紋」（`Python 3.11.17`、`ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`·發單端擬單之機亦同）；其結果入回報（相異 ⇒ 前置 (丙) 整份照跑·⛔ 停機）。

### `§零-1`　取號現查（宣告框）

**本批⛔ 鑄號**（`自誤`、`GB`、`VR`、`K-9` 皆⛔ 鑄·塊 `K37` 之二 ＝ 發單端之【工】之讀法·⛔ 充裁）。

**塊名、新名**（母體 ＝ 開工態 `a8657c4` 之追蹤檔 **`2906`** 檔·`git grep -l`／`git grep -h … | wc -l` ＋ `-F`·**二框各載**·`自誤 588`）：

| 受詞 | `` 塊 `<名>` `` 之框 檔／列 | `` `<名>` `` 之框 檔／列 | 判 |
|---|---|---|---|
| `Fy46`、`K37`、`P48`（逐名） | 皆 `0`／`0` | `Fy46` `0`／`0`；`K37` `9`／`27`；`P48` `0`／`0` | 🟢 可取（`K37` 之諸列皆量測器之項名或他物〔⛔ 塊名〕） |
| 對照甲［必非零］`Fy45` | `3`／`15` | — | 🟢 框非恆空 |
| 對照甲［必非零］`K36` | `1`／`10` | — | 🟢 框非恆空 |
| 對照甲［必非零］`P47` | `1`／`4` | — | 🟢 框非恆空 |
| 報告名 `W-G.9-391R`、新側支之名 `W-G.9-391-k980x`、本單名 `W-G.9-391_規格單`、新器 `probe_WG9391`（`-F`·逐名） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名（`git ls-remote --heads origin` 亦無其列） |
| 新頂層之名 `k980_mba`、`k980_range_touch_check`、`end_block_band_width`、`K980_`（前綴）；原型之區域之名 `_piece391`、`_mba391`、`_best391`、`_w391`、`_unf_poly_e`（`-F`·逐名·後者⛔ 為期·執行端之名異者另自查其⛔ 撞） | — | 皆 `0` 檔 | 🟢 ⛔ 撞名 |

量測器之新檔名 `F35`（`verify/probes/probe_WG9391_k980x.py`）。收工閘 `6`／`7` 以 `634 629` 驗之（本批⛔ 鑄自誤）。

### `§零-2`　停機款

| # | 款 |
|---|---|
| `1` | 開工時主線 ≠ `a8657c4`，或遠端 heads ≠ `50`、或已含 `refs/heads/verify/W-G.9-391-k980x`，或施工樹之追蹤檔有變動，或 `§零-0` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或量測之殼之旗標之出艙 ≠ 期，或 `§零-0` 項 `5` 之環境於安裝後仍不能匯入 |
| `2` | 本單之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本單不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3` | 塊 `Fy46`／`K37`／`P48` 任一之 bytes／`sha256`／列數與 `§五-1` 不符；或 `Fy46` 之 `git apply --check` 不過；或寫出後之 blob ≠ `§五-1` 項 `5` |
| `4` | 工項二前置之任一期不符 |
| `5` | **規格有歧義而涉域上判斷**（`§三-4`）；或執行端須改 `§三-3` 之禁改始能滿足 `§三-1` |
| `6` | 工項二之驗 `V-1`〜`V-9` 任一 ≠ 期；**量測器紅而須改量測器始能過**（⛔ 改器）；**本案配地有任一改變** |
| `7` | 任一 `push` 之目標非 `verify/W-G.9-391-k980x`（工項零〜四）或 `ops/queue`（回報）；或任一 `push` 被拒、或須 `--force`／`--force-with-lease` 方能成；或主線於本批中有任何推進 |
| `8` | 工項三之二檔（`K-6` 典、`docs/待落地清單.md`）：任一之刪除欄 ≠ `0`，或改前全檔非改後之嚴格前綴，或改後之尾 ≠ 其塊，或寫出後之 blob ≠ `§五-1` 項 `5`；或 `checkidx` 之 `rc` ≠ `0` 或末列 ≠ 期；或 `gen_fa_index` 之出艙 ≠ 期、或其重生成之檔與倉內不逐位相同 |
| `9` | `§四-3` 收工閘任一 ≠ 期 |
| `10` | 執行端作任何「孰為正典」「應改為」之判，或改塊、器、命令一字以求其過（`<repo>` 依單首 🔑 之形傳入者、閘 `6` 之 `.`〔倉根〕⛔ 屬之）；或執行端認為塊之文字與倉之事實不符（照實回報其處與證據·⛔ 自改） |
| `11` | 本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `12` | 工項二之唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 |
| `13` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁：停機上呈之全文寫入 `ops/queue` 之 `reports/W-G.9-391_規格單_回報.md`（`result` ＝ `停機上呈`）；已推至新側支之 `commit` ⛔ 撤。

### `§零-3`　pre-flight

受單側收單時自倉重跑 `python3 verify/probes/probe_order_preflight.py <本單之路徑>` 並逐項再處置（`P-3`／`P-5` 為停機款；`P-1`／`P-2`／`P-4`／`P-6` 逐項具名）；發單端實跑之出艙見 `§五-1` 項 `9`。

---

## `§一`　態錨（發單端自倉實跑·雲端 Linux `4` 核·倉外工作樹·殼無 `WV_`·Python `3.11.17`·`pip freeze` `ae1438da…`）

| # | 項 | 值 |
|---|---|---|
| `1` | 主線／refs | 主線 `a8657c4012d961eccebd77cd812c0ab6aeab030f`（`W-G.9-390` 補令四工項零⁗′·快轉自 `2aa6302`）；遠端 heads **`50`**；追蹤檔 `2906`；`app.py` ＝ `82855efb31049c2d21146c2c6fc903182615f912`（`1856077` B）；`verify/stepg_pipeline.py` ＝ `2bb2f56ecf9423a99c522ddfbdfb55f314854e27`；`verify/run_verification.py` ＝ `f5b896e5a702c5d958e3ba27091d27832385efc4`；`verify/selection_pipeline.py` ＝ `fec1d5c0f80584ab008612eec92ab540dfe44fdd`（本批⛔ 動）；`K-6` 典 ＝ `8ae87d473218de9ff2efd19ef5890502da8fbfa6`（`909964` B）；自誤簿 ＝ `c5406d05c024dae897beb3c1175934ece7c0819b`（本批⛔ 動）；`docs/待落地清單.md` ＝ `adf906d43045f365cec15fc345666c9c874faed5`（`20188` B）；`CLAUDE.md` ＝ `00e627af607baecde4f0138c1f706c851d320350`（本批⛔ 動）；`probe_WG9270_closegate.py 634 629 .` ⇒ `rc 0`（對照 `635 634` ⇒ `rc 7`）；`probe_WG9321_issuer_anchor.py … 634 629` ⇒ `rc 0`（`§零-0` 項 `3` 之值）；基準 ＝ `ops/queue` 之 `基準/a8657c4012d961eccebd77cd812c0ab6aeab030f.md`（`74` 呼叫皆合期）；本批所改之 `11` 器之施前 blob ＝ `§五-1` 項 `2` |
| `2` | 受詞（`a8657c4`） | 街角規定範圍之構造 `_build_corner_range_v3`（其呼叫四處：`select_corner_lots_both_sides_v12`〔跨占、三指數〕、`main` 之參數表〔`【左】／【右】街角最小面積(㎡)` ＝ 街角選位之門檻 `min_area_to_apply` 與強制抵費地之帶之面積 `_corner_buffer_S` 之源〕、`verify/run_verification.py` 之 `build_param_table`〔harness 之參數表〕、`verify/stepg_pipeline.py` 之 ctx〔`corner_range_polys`〕）；末端塊範圍之構造 `_end_region_R`（← `end_block_side_geom` ← `end_block_apply` ← `end_block_host`〔畫面與 harness 二宿主〕）與末端保留 `_place_pool_parcels`（其帶 ＝ `_end_band(…, min_width)`·另算）；最小建築面積之有效值 `k91_effective_min_build_area`（`K-9-1` ⑨）——**以上皆⛔ 讀最小建築面積**（`K-9-34` ⬜·`K-9-80` ④⑤⑥ ⬜）；一街廓之二範圍之相接或重疊⛔ 查 |
| `3` | 工項一之端（`a8657c4` ＋ 塊 `Fy46`·倉外實跑） | 前置 (甲) 之 `33` 呼叫之 `rc`／末列 ＝ `§五-1` 項 `8` 之工項一之端之列（`F35` 之三呼叫紅如期·前態之對照組；所改之 `11` 器之 `30` 呼叫 ＝ 基準之值）；(乙) 之 `6` 呼叫 ＝ 基準之值（其器與其受詞之檔皆⛔ 為塊 `Fy46` 所動）；諸呼叫之 `stderr` 合計 `0` B；(丙) ＝ 基準之值 |
| `4` | 施後（原型 ＋ 塊 `Fy46`·倉外實跑·⛔ 入倉） | 原型之三檔 ＝ `app.py` `f911b42b282ef66b2142b40c1f48bf6760c429c7`（`+168`／`−18`）、`verify/stepg_pipeline.py` `b27e8ec5e3dcf0ed85a5830e08ba802018c5b6ad`（`+9`／`−0`）、`verify/run_verification.py` `ccd6158aced39ab937311038860ae03096e2a4bb`（`+1`／`−0`）——**⛔ 為期**（執行端之碼異則異·唯其行為以 `V-*` 量之）；`§五-1` 項 `8` 之 `77` 呼叫：皆 `rc 0`、末列皆 ＝ 該表之施後之列（`#56`／`#57` 除外·JSON）、`stderr` 合計 `0` B·耗時之和 `13185` s·並行 `2`；`F35 selftest` `C1`〜`C9`、`E1`〜`E6`、`T1`〜`T6`、`K1` 與 `P0 22／22`、`F35 wiring` `W1`〜`W9`、`F35 run` `R1@3.5`／`R2@3.5`／`R1@0.0`／`R2@0.0` 皆 ✅ |
| `5` | 本案之配地（前態 ＝ 工項一之端〔＝ 基準〕·後態 ＝ 原型） | `k6s3 cmp`（前態 `k6s3_base_*` 對施後 `k6s3_post_*`）二退縮皆 `rc 0`·末列 `相異 0 項 ⇒ ✅ 同`·`stderr` `0` B（對照組：`k6s3_base_35` 對 `k6s3_post_00` ⇒ `相異 18 項 ⇒ 🔴 異`）；`F8` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`·＝ 基準）；`parity` 二退縮之落檔與 `stdout` 前後逐位同（發單端之二態同在 `a8657c4` 之 `HEAD`·執行端之二態之 `HEAD` 異 ⇒ 依 `V-5` 代之）；`F35 run` 之 `R1`：二退縮之參數表、街角選位、Step-G 之 ctx 之街角規定範圍之面積皆同（`8` 範圍）、末端塊之 `R_end` ＝ `252.28 ㎡`（`R6` 左·＝ 改前） ⇒ **本案之配地⛔ 變**。`R2`（以 session 之街廓覆寫輸入「各街廓之未輸入時之最大範圍之面積 ＋ `10 ㎡`」）：`3.5 m` 之輸入 ``{'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}``、`0 m` 之輸入 ``{'R1': 124.94, 'R2': 162.99, 'R3': 163.8, 'R4': 126.08, 'R5': 156.5, 'R6': 262.28}`` ⇒ 諸源之範圍之面積皆 ＝ 輸入值（`±0.01 ㎡`）、⛔ 停機 |
| `6` | 量測器之判別力（原型之上之突變·發單端實跑·`F35 selftest`／`wiring`） | 見下之「突變之表」：`16` 突變（擬單之十一 ＋ 審查所揭之五）皆紅；未突變之原型皆綠；基準（`a8657c4`）之 `F35 selftest`／`wiring`／`run` 皆紅（`§五-1` 項 `8` 之 `#75`〜`#77` 之工項一之端之列） |
| `7` | 唯讀獨立審查（一輪·⛔ 參與撰題） | (A)「改配地或違裁示」一：`_WF_NS_NAMES`（app 之七級調配之路注入引擎之名）漏列 `k980_mba`、`k980_range_touch_check` ⇒ 該路之 `run_step_g` 必 `KeyError`（審查以全套閘 `run_all` 二態比：`fixture_wf_ns_wiring` 由 `rc 0` 轉 `rc 1`、G.1 之同源之閘轉紅）⇒ 入原型（`R-6` 之末）與器（`F35 W9`·突變 `M16`）。所揭而入（純實作與器）：末端帶之倍增無上界（浮點之邊得誤訊）⇒ `R-4` 增上界；器之缺口——`W2`／`W3` 唯量形（改傳 `None` 仍綠）、畫面之短街廓之查之受詞、`k980_mba` 之分區之字面、`R2` 之停機可空過 ⇒ `W8`、`W5`、`W4`、`R2` 改之（突變 `M12`〜`M15` 皆紅）；三器（`probe_WG9353`／`9354`／`9355`）之 `run` 之替身 ⇒ 照傳（發單端之長跑自捕）。記而⛔ 改（留次單·塊 `K37` 之六 `53`〜`56`、`P48` 序 `26`）：舊七級調配引擎（`verify/wf_f4.py`·UC9898 凍結）之 `R_end` 未擴大；畫面於選位後改最小建築面積之失效；一側之範圍擴至近他端之餘地之處置（⛔ 裁 ⇒ 呈 KL）；非凸之多片；harness 之 `_lot_gate` 之源（序 `6`）；短街廓之查於選位時之提前；`K-9-80 ⑥` 之停機⛔ 入 `K6_PROGRAM_STOPS`（範圍⛔ 因合併而變·選位之首次即停）；未輸入者亦查相接（KL `22:55` 第 `5` 點之文·塊 `K37` 之二之己）；③ 之歸屬（二之辛）；`P0` 之判式自驗之式與既有之器同（⛔ 改）。審查另證：除 A-1 之二項外，全套閘之二態逐列同（本案配地⛔ 變之佐）；擴大之方向（街角 ∥ SIDE_LINE、末端塊沿宗地分配線）、未輸入之逐位⛔ 變、跨占與門檻之諸源（`v12`、參數表、`_corner_buffer_S`、`_lot_gate`、`end_block_pick`、`end_block_forced_bands`、`wd3_fragment_geom.py`、`K-9-32` 之藍線）皆合。 |

**突變之表**（每種之所據：(a) 泛用化之目標／(b) 既裁之樣態或自誤之錯／(c) 出錯而變空而照樣亮綠；三法 ①「KL 所否之選項」：KL `22:55` 之問4（警示停止·所否 ＝ 照常續行）⇒ `M5`；問5（兩者都用擴大後之範圍·所否 ＝ 唯其一）⇒ `M6`（門檻用原範圍）、`M11`（名單用原範圍）；② 換名、鏡射、旋轉 ＝ `F35 selftest` 之 `C8`、`E5`；③ 邊界 ＝ 恰等（`C4`、`E2`）、零（`C1`、`C2`、`E6`）、門檻之兩側（`T1`、`T2`、`T3`）、一範圍與三範圍（`T5`、`T6`））：

| 突變 | 所據 | 所改（原型之上） | 紅 |
|---|---|---|---|
| `M1` | (b) `K-9-34` ②「是 ⇒ 同 ①」 | 面積已達者亦「擴」（縮至最小建築面積） | selftest `rc 1`·['C3']；wiring `rc 0`·[] |
| `M2` | (b) `K-9-80` ④「末端塊無須退縮」 | 擴大後之末端帶另加退縮（`+0.5 m`） | selftest `rc 1`·['E3']；wiring `rc 0`·[] |
| `M3` | (c) | 相接之判之受詞恆為空 | selftest `rc 1`·['T2', 'T3', 'T4', 'T6']；wiring `rc 0`·[] |
| `M4` | 三法 ③ | 相接之判用嚴格 `＜` | selftest `rc 1`·['T2']；wiring `rc 0`·[] |
| `M5` | 三法 ①（問4） | 相接或重疊唯記之而⛔ 停 | selftest `rc 1`·['T2', 'T3', 'T4', 'T6']；wiring `rc 0`·[] |
| `M6` | 三法 ①（問5） | harness 之參數表（門檻之源）⛔ 傳最小建築面積 | selftest `rc 0`·[]；wiring `rc 1`·['W1', 'W4'] |
| `M7` | (b) 二源 | 末端保留之帶回用畸零地寬（`_end_band` 之直呼） | selftest `rc 0`·[]；wiring `rc 1`·['W3', 'W8'] |
| `M8` | (b) `K-9-34`「平行SIDELINE」 | 擴大之切線改 ∥ 宗地分配線 | selftest `rc 1`·['C9']；wiring `rc 0`·[] |
| `M9` | (a) 寫死側別 | 唯左端之末端塊依最小建築面積擴大 | selftest `rc 1`·['E5']；wiring `rc 1`·['W8'] |
| `M10` | (b) `K-9-1` ⑨ 裁丙 | 有效值⛔ 讀街廓覆寫 | selftest `rc 1`·['K1']；wiring `rc 0`·[] |
| `M11` | 三法 ①（問5） | 街角選位之範圍⛔ 傳最小建築面積 | selftest `rc 0`·[]；wiring `rc 1`·['W1', 'W4'] |
| `M12` | 審查所揭（(c) 之族） | 末端保留之帶⛔ 擴大（`_place_pool_parcels` 內改傳 `None`） | selftest `rc 0`·[]；wiring `rc 1`·['W8'] |
| `M13` | 審查所揭 | `end_block_apply` 改傳 `None` 於 `end_block_side_geom` | selftest `rc 0`·[]；wiring `rc 1`·['W8'] |
| `M14` | 審查所揭 | 畫面之短街廓之查去二末端塊範圍 | selftest `rc 0`·[]；wiring `rc 1`·['W5'] |
| `M15` | 審查所揭 | 參數表之 `k980_mba` 之分區傳空字面 | selftest `rc 0`·[]；wiring `rc 1`·['W4'] |
| `M16` | 審查所揭（A-1） | `_WF_NS_NAMES` 漏列二新名 | selftest `rc 0`·[]；wiring `rc 1`·['W9'] |

---

## `§二`　所據之語與射程

🔒 **所據**：`docs/待落地清單.md` 之「……`W-G.9-390` 補令三（`K-9-80`·取得即鎖定·KL `2026-10-20 22:30`／`22:55`）；序 `7`、`8` 之改；序之單號之順延」節之序 `22`（「`K-9-80` ③（微差之吸收）、④〜⑥ 與 `K-9-34`」·落地之單 `W-G.9-391`）。`K-6` 典 `K-9-80`（`W-G.9-390` 補令三之節·KL 之語逐字見該節）之：

> ④ **範圍依最小建築面積之擴大**：街角規定範圍 ＝ `K-9-34`（遠側界線 ∥ SIDE_LINE 平移 `退縮 ＋ 畸零地寬`；面積 ＜ 最小建築面積〔有輸入者〕⇒ 續平移至面積 ＝ 最小建築面積）之重申；**末端塊範圍**（新）：`R_end` 之面積 ＜ 最小建築面積（有輸入者）⇒ 其往街廓內部之界線沿宗地分配線（地界線）之方向平行內移，至面積 ＝ 最小建築面積；末端塊無退縮。未輸入者 ⇒ 範圍⛔ 變。
> ⑤ **跨占之名單與門檻**（問5）：皆以擴大後之範圍定之（跨占者 ＝ 位置與擴大後之範圍重疊之重劃前土地；門檻 ＝ 擴大後之範圍之面積）。
> ⑥ **短街廓**（問4）：一街廓之二範圍（末端塊與末端塊、街角與末端塊、街角與街角）擴大後相接或重疊 ⇒ 比照前置地基檢查，警示並停止（⛔ 自動處理）。

KL 之語（`2026-10-20 22:30`·逐字）：「……其中最小建築面積若有輸入的話，則街角地除了程式用SIDELINE平行移動 退縮+畸零地寬，還要檢視這寬度=退縮+畸零地寬 所圍成的街角地規定範圍面積是否有>=該街廓的最小建築面積，若無，則SIDELINE再繼續平行移動直至=最小建築面積。／末端塊範圍也是(只是末端塊無須退縮)，檢視R_end>=最小建築面積，若無，則R_end往街廓內部(中間)的地界線ALLOC_LINE平行移動直至=最小建築面積。」（`22:55`·逐字）：「5. 問4：比照前置地基檢查，短街廓範圍相接或重疊時警示停止／6. 問5：兩者都用擴大後的範圍」。`K-9-34`（KL `2026-09-17`·逐字）：「頂多當該街廓有最小建築面積之輸入時，就需要檢查街角最小規定範圍的遠側境界線=退縮+畸零地寬 時，該面積是否>=最小建築面積，若無則就要依據"最小建築面積"去決定街角規定範圍的遠側界線(平行SIDELINE)，若該街廓沒輸入"最小建築面積"，遠側界線就是=退縮+畸零地寬)」。

🔒 **請示前之三關之甲**（既裁之窮查·`發單端.md` 丁 0）：以「最小建築面積／最小建築基地」「擴大／續平移／內移」「相接／重疊／短街廓」「跨占／門檻」四組之詞全文搜 `K-6` 典（`K-9-1` ⑨、`K-9-32`〜`K-9-36`、`K-9-49`、`K-9-80`）與 `參考/市地重劃作業手冊.txt`（手冊⛔ 及範圍之擴大）：`K-9-80` ④⑤⑥ 與 `K-9-34` 之文已定受詞（有輸入者之二範圍）、方向（街角 ∥ SIDELINE、末端塊沿宗地分配線內移）、量（＝ 最小建築面積）、跨占與門檻之源（擴大後）、短街廓之處置（警示停止）；其未逐字者——「＝」之容差、最小建築面積之源（有效值）、相接之距、查之時點、擴至他端仍未達之形——皆以既裁之同族之讀法定之（塊 `K37` 之二之甲〜己），其土地之果⛔ 異於 ④⑤⑥ 之文 ⇒ **⛔ 新域問**（【工】·以交付之通知告 KL）。③ 之微差之吸收——其受詞之源未明（本案之一例 `0.01 ㎡`），二讀之土地後果須先量 ⇒ 再分為 `W-G.9-392`（塊 `K37` 之二之辛、四）。

🔒 **授權**（自動化之委任·`K-6` 典 `W-G.9-386` 之節之一之 KL 逐字）：KL `2026-10-17 07:23` 第 `3` 點「除了只是修正施作疏漏的補令，新的規格單和入主線也可以不用我過目，畢竟討論到現在我覺得已經大多配地的幾何情況、分配成果檢驗機制(R_END,街角地檢驗,內接矩形,若有最小建築面積之檢核,配地要臨FRONTLINE及BASELINE等)及市地重劃扣除負擔之分配精神，已經大致都有說明與你討論過了，所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」；`07:58`「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」。本單 ＝ 待落地清單上已有 KL 裁示之項目（`K-9-80` ④⑤⑥、`K-9-34`）。**`expects_allocation_change` ＝ `false`**（`§一` 項 `5`）——執行端之量得本案配地有任一改變 ⇒ 停機款 `6`。

🔒 **【工】之讀法**（塊 `K37` 之二·以交付之通知告 KL）：甲 最小建築面積之源（有效值·畫面與 harness 同一二鍵·`k980_mba`）；乙「＝」之量（`[最小建築面積, ＋0.01 ㎡]`·浮點餘裕 `1e-6 ㎡`）；丙 街角之擴大（∥ SIDELINE·扣截角）；丁 末端塊之擴大（帶寬自畸零地寬增之·末端保留同源）；戊 跨占之名單與門檻（街角選位之範圍、參數表之街角最小面積、末端塊之 `R_end` 皆擴大後）；己 短街廓（距 ≤ `0.01 m` ⇒ 停機·查之時點）；庚 `K-9-80` ① 之保證；辛 ③ 之再分。

🔒 **單之再分**（工程裁·唯序·⛔ 涉土地後果·塊 `K37` 之四）：待落地清單之序 `22` 再分——本單（④⑤⑥ 與 `K-9-34`）與 `W-G.9-392`（③·先查其源）；原定之 `W-G.9-392`（`K-9-61` ⑤、`GB-205`）、`W-G.9-393`（`K-9-60`）、`W-G.9-394`（`K-9-59`／`K-9-63`）各順延一號。

🛑 **射程**：`(a)` 工項零、一、三、四（零生產碼）由執行端逕行 `push` 至新側支；`(b)` 工項二（🔴）於其驗與審查皆符後 `push` 至新側支；`(c)` ⛔ 及主線（入主線另以短單·`§四-2`）、他側支、`data/` 之資料檔、`K-9-80` ③⑦、`K-9-61` ⑤、`GB-205`、`K-9-59`、`K-9-60`、`K-9-62` 之指配、`K-9-63`、`GB-196`〜`GB-198`、`GB-202`、規格步 `5`——另單；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）。

---

## `§三`　規格（執行端依之撰寫生產碼·⛔ 以程式行表述）

🔒 **用語**（`a8657c4`）：
- 「**最小建築面積之有效值**」＝ `k91_effective_min_build_area(label, category, by_label, by_category)`（`K-9-1` ⑨ 裁丙）；`0` ＝ 未輸入。「**二鍵**」＝ session 之 `K91_SS_MBA_BY_LABEL`（街廓覆寫）、`K91_SS_MBA_BY_CATEGORY`（分區底）。
- 「**街角規定範圍**」＝ `_build_corner_range_v3` 之回傳；「**末端塊範圍**」＝ `_end_region_R` 之 `R_end`（未臨正街 ∪ 末端帶）。
- 「**擴大**」＝ 有效值 ＞ `0` 而範圍之面積 ＜ 有效值 `− K980_AREA_EPS` 時，範圍之內側（遠側）界線續往街廓內平移至 `0 ≤ 面積 − 有效值 ≤ K980_AREA_TOL`。

### `§三-1`　行為要求（逐條）

| 條 | 處 | 要求 |
|---|---|---|
| `R-1` | 常數 | `app.py` 之頂層增三常數：`K980_AREA_TOL = 0.01`（㎡）、`K980_AREA_EPS = 1e-6`（㎡）、`K980_TOUCH_TOL = 0.01`（m）；各附註其義（擴大後之面積之上餘、「已達」之浮點餘裕、相接之距）。 |
| `R-2` | 有效值之單一入口 | 頂層新函式 `k980_mba(session, label, category)`：回 `k91_effective_min_build_area(label, category, <session 之街廓覆寫鍵之值或 {}>, <session 之分區底鍵之值或 {}>)`；`session` 為 `None` ⇒ 視同空之 dict；二鍵缺 ⇒ 未輸入（⛔ 停機·鍵缺即使用者未輸入）。 |
| `R-3` | 街角規定範圍之擴大 | `_build_corner_range_v3` 增關鍵字參數 `min_build_area=None`（簽名之末）。`None` 或 `0` ⇒ 回傳之範圍與改前逐位同；`< 0` ⇒ 停機（經其 `_stop`）；有效值 ＞ `0` 而面積 ≥ 有效值 `− K980_AREA_EPS` ⇒ 逐位同；否則**擴大**：平移後之 SIDELINE（`_Tp` 之線·方向 `(sux, suy)`）續沿 `sigma·d̂` 平移（路平行距 ＞ `S1_par`），範圍 ＝ 街廓之多邊形為該線所切之片之中距 `_anchor` 最近者扣截角三角形（與既有之構造同法）；平移至該線⛔ 再切到街廓仍未達 ⇒ `raise RuntimeError(…)`（訊息含「K-9-80 ⑥」「短街廓」與有效值）；求解⛔ 收斂 ⇒ 停機（經 `_stop`）。🔒 既有之列一字⛔ 動（`§三-3` 第 `1` 款之錨），擴大之碼唯插於函式末之 `return rng` 之前（其內之 `return` 之句⛔ 含子字串 `return rng`）。 |
| `R-4` | 末端塊範圍之擴大 | 頂層新函式 `end_block_band_width(block_poly, cad_alloc, end_pt, min_width, frag_poly, min_build_area, _label='')`：`min_width` 缺或 ≤ `0` ⇒ 停機；`min_build_area` ⛔ ＞ `0` ⇒ 停機（未輸入者⛔ 入本函式）；`area(frag_poly ∪ _end_band(…, min_width))` ≥ 有效值 `− K980_AREA_EPS` ⇒ 回 `min_width`；街廓之面積 ＜ 有效值 ⇒ `raise RuntimeError(…)`（含「K-9-80 ⑥」「短街廓」）；否則回帶寬 `w`（`_end_band` 之寬之引數·⊥ALLOC 之垂距）使 `0 ≤ area(frag_poly ∪ _end_band(…, w)) − 有效值 ≤ K980_AREA_TOL`；帶寬之倍增逾街廓之外接矩形之對角線而仍未達（浮點之邊）⇒ 同上之「K-9-80 ⑥」之停機；⛔ 收斂 ⇒ 停機。`_end_region_R` 增關鍵字參數 `min_build_area=None`：`None` 或 `0` ⇒ 帶寬 ＝ `min_width`（逐位同）；否則帶寬 ＝ `end_block_band_width(…)`。`end_block_side_geom`、`end_block_apply`、`end_block_host` 各增關鍵字參數 `min_build_area=None` 並逐層傳之（`end_block_host` ⇒ `end_block_apply` ⇒ `end_block_side_geom` ⇒ `_end_region_R`）。 |
| `R-5` | 末端保留之同源 | `_place_pool_parcels` 增關鍵字參數 `min_build_area=None`；其末端保留之帶 ＝ `_end_region_R(blk_poly, alloc_dir_cad, <該端之 end_pt>, float(min_width), <該端之未臨正街之多邊形>, …, min_build_area=min_build_area)` 之第一個回傳（帶）——未臨正街之多邊形 ＝ 同處既有之 `_block_strip(…)` 之第一個回傳（⛔ 另算）；該函式內⛔ 直接呼叫 `_end_band`。 |
| `R-6` | 二宿主之傳與短街廓之查（末端塊） | 畫面 `f3_screen_stepg_run` 與 harness `verify/stepg_pipeline.py` 之 `_run_step_g_impl`：其 `end_block_host(…)` 與 `_place_pool_parcels(…)` 之呼叫各傳 `min_build_area=k980_mba(<session>, blk_label, blk_meta.get('category', ''))`（畫面之 session ＝ `st.session_state`；harness ＝ `ss`·經 `ns['k980_mba']`）；`end_block_host` 之呼叫之後（同一區塊之內）呼叫 `k980_range_touch_check(blk_label, {'左側街角規定範圍': <該街廓左之街角規定範圍>, '右側街角規定範圍': <右>, '左端末端塊範圍': <其回傳之 info 之左之 r_end>, '右端末端塊範圍': <右>})`（街角規定範圍之源 ＝ 各宿主傳予 `end_block_host` 之 `corner_range_polys` 之同物）。`app.py` 之 `_WF_NS_NAMES`（app 之七級調配之路注入引擎之名）增 `"k980_mba", "k980_range_touch_check"`（引擎經 `ns[…]` 取之·漏列即 `KeyError`）。 |
| `R-7` | 街角規定範圍之四處（跨占之名單與門檻之源） | 下列四處之 `_build_corner_range_v3(…)` 之呼叫皆傳 `min_build_area=`：① `select_corner_lots_both_sides_v12`（跨占、三指數之範圍）＝ `_mba_pk`，其值於取 `_blk_meta_wb` 之 `try` 之內以 `k980_mba(<該處之 session>, _this_blk_B4, (_blk_meta_wb or {}).get('category', ''))` 立之、其 `except` 之支立為 `None`（該支⛔ 構造範圍）；二範圍建畢（`_corner_range_left`／`_right`）即呼叫 `k980_range_touch_check(_this_blk_B4, {'左側街角規定範圍': …, '右側街角規定範圍': …})`；② `main` 之參數表（街角最小面積 ＝ 門檻與強制抵費地之面積之源）＝ `k980_mba(st.session_state, _lbl, b.get('category', ''))`；③ `verify/run_verification.py` 之 `build_param_table`（harness 之參數表）＝ `ns["k980_mba"](fake_st.session_state, lbl, b.get("category", ""))`；④ `verify/stepg_pipeline.py` 之 ctx（`corner_range_polys`）＝ `ns['k980_mba'](ss, _crp_lbl, _crp_b.get('category', ''))`。🔒 `main` 之改**唯增列**（`§三-3` 第 `3` 款）。 |
| `R-8` | 短街廓之判 | 頂層新函式 `k980_range_touch_check(blk_label, ranges)`：`ranges` ＝ {名: 多邊形或 `None`}；`None`／空者不計；任二者之距（`distance`）≤ `K980_TOUCH_TOL` ⇒ `raise RuntimeError(…)`（訊息含「K-9-80 ⑥」「短街廓」、街廓名、二範圍之名、其距與交之面積）；他 ⇒ 回 `None`。 |
| `R-9` | 訊息與他 | `R-3`／`R-4`／`R-8` 之停機訊息⛔ 帶 `GB-` 之號或【未裁】；新增之 docstring 載 `W-G.9-391` 與所據之條；`R-1`〜`R-9` 以外之一字⛔ 動（含 `verify/wf_f4.py` 之 `_reshape_block` 之 `_end_region_R` 之呼叫——UC9898 凍結之舊七級調配引擎·⛔ 傳·塊 `K37` 之六 `53`·另單）；新增之區域名皆帶 `391`（⛔ 撞所在函式與全檔之既有之名；`_place_pool_parcels` 之未臨正街之多邊形之名得異）。 |

### `§三-2`　介面（名與形·量測器以之為受詞）

- `F35`（`verify/probes/probe_WG9391_k980x.py`·新）：`selftest <repo>` 之 `C1`〜`C9`、`E1`〜`E6`、`T1`〜`T6`、`K1` 與 `P0`；`wiring <repo> a8657c4` 之 `W1`〜`W9`；`run <repo>` 之 `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0`。其所量之名與形：`R-1` 之三常數與 `R-2`／`R-4`／`R-8` 之三新函式之名與簽名（以 harvest 呼之）；`_build_corner_range_v3`、`end_block_side_geom`、`_end_region_R` 之 `min_build_area` 之關鍵字；`W1` 四處之呼叫皆傳 `min_build_area`；`W2` `end_block_side_geom`／`end_block_host`／`_place_pool_parcels` 之呼叫皆傳之；`W3` `_place_pool_parcels` 呼叫 `_end_region_R` 恰一、⛔ 呼叫 `_end_band`，`_end_region_R` 呼叫 `end_block_band_width` 恰一（全檔亦恰一）；`W4` 其值皆為 `k980_mba(…)`（或 `_mba_pk`·其賦值恰一為之·他者唯 `None`）、`k91_effective_min_build_area` 於 `k980_mba` 外之呼叫之數對基準⛔ 增；`W5` `k980_range_touch_check` 之呼叫於 `select_corner_lots_both_sides_v12`、`f3_screen_stepg_run`、`_run_step_g_impl` 各恰一（`app.py` 全檔恰二）；`W6` 頂層之名之增恰六；`W7` ⛔ 案件字面；`W8` `min_build_area` 之逐層照傳（`end_block_host`→`end_block_apply`→`end_block_side_geom`→`_end_region_R`、`_place_pool_parcels`→`_end_region_R` 皆傳 `min_build_area=min_build_area`）；`W9` 引擎經 `ns[…]` 取之新名皆在 `_WF_NS_NAMES`；另 `W4` 之 `k980_mba` 之分區之引數⛔ 為字面、`W5` 之範圍之名齊全。
- 塊 `Fy46` 所改之既有之器（`11` 檔·皆唯增許或照傳·其判式⛔ 變）：`probe_WG9385_k974.py`（`W7`）、`probe_WG9363_k953.py`（`W6`／`W7`）、`probe_WG9367_adj4.py`（`W5`）、`probe_WG9370_adj4mut.py`（`X1`／`X2`）、`probe_WG9387_k961h.py`（`X3`／`X5`）、`probe_WG9388_k961s3.py`（`X3`／`X5`）、`probe_WG9389_trialstop.py`（`X3`／`X4`）、`probe_WG9390_k961r.py`（`X2`／`X4`）——各增 `NEW391`（六新名）、`W391`（六新名 ＋ `app.py` 之九函式與 `_WF_NS_NAMES`）、`F391`（harness 二檔）之許；`probe_WG9353_endmerge.py`、`probe_WG9354_endcontest.py`、`probe_WG9355_screenmerge.py`——其 `run` 所注入之 `end_block_side_geom` 之替身（`geo`）增關鍵字參數 `min_build_area=None` 並照傳之（`R-4` 之新參數·⛔ 增之則其 `run` 中止）；細目見 `§五-1` 項 `2`。

### `§三-3`　禁改（既有閘之錨·執行端撰碼須避之；觸之即既有閘轉紅 ⇒ 停機款 `6`）

1. **量測器之字樣之錨**（`F23 wiring` 之 `W8`〔基準 `7d8e954`〕、`F24 wiring` 之 `W7`〔基準 `d7a5ea4`〕）：`verify/probes/` 之一切 `.py` 之字串常數（長 ≥ `4`）於基準之 `app.py`／`verify/selection_pipeline.py` 中恰一見者，於工作樹仍須恰一見（以**子字串**計·含註解與 docstring）。🔒 本單之受詞之例（發單端以原型實測）：`    return rng`、`cut = _LS3([(_Tp[0] - sux * _ext`（`_build_corner_range_v3`）、`trial=_trial, cache=_cache, allow_forced=_allow)`（`end_block_host`）於 `app.py` **恰一見**——擴大之碼⛔ 照抄此三句（其切線之變數之名須異）、`end_block_host` 之 `min_build_area=` 須增於該句之**前一列**（⛔ 改該句）；新之註解、docstring 之折行⛔ 令一列以四個以上之空白繼以中文起首（錨含「縮排之空白 ＋ 中文」之子字串）；基準中恰一之函式名（含巢狀）於工作樹仍恰一 ⇒ 新之巢狀名⛔ 撞既有之名。執行端撰碼中自跑 `F23 wiring`／`F24 wiring` 以查之。
2. **突變之錨**（`F13`／`F16`／`F17`／`F23`／`F27`／`F28`／`F29` 之突變）：其錨須仍於其函式內**恰一見**——新碼⛔ 照抄既有之句（以子字串計）。
3. **`main` 唯增列**（`F30 wiring` 之 `W7`：`main`、`calc_special_burden_total` 對基準之刪列唯 `W-G.9-385` 之三列）：參數表之 `_build_corner_range_v3(…)` 之呼叫之 `min_build_area=` 以**新增之一列**為之（插於 `_make_chamfer_tri_wb(b, _wh_cr),` 之列與 `dxf_quantum=_q_cr, …` 之列之間·⛔ 改既有之列）。
4. **頂層**：`app.py` 之頂層之名之增恰 `{K980_AREA_TOL, K980_AREA_EPS, K980_TOUCH_TOL, k980_mba, k980_range_touch_check, end_block_band_width}`、無減；頂層節點之相異 ＝ 此六 ∪ `{_WF_NS_NAMES, _build_corner_range_v3, _end_region_R, _place_pool_parcels, end_block_apply, end_block_host, end_block_side_geom, f3_screen_stepg_run, main, select_corner_lots_both_sides_v12}`；`verify/stepg_pipeline.py` 之頂層節點之相異 ＝ `{_run_step_g_impl}`、`verify/run_verification.py` ＝ `{build_param_table}`（二檔之頂層之名⛔ 變·簽名⛔ 變）；`verify/selection_pipeline.py` 一字⛔ 動。
5. **⛔ 案件字面**（`F35 wiring` 之 `W7`）：新增或改之頂層節點內⛔ 新增合 `^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$` 之字串常數。
6. 既有之函式之簽名之既有參數、回傳之形⛔ 改（新參數皆為簽名之末之關鍵字參數·預設 `None`）。

### `§三-4`　域上之未定 ⇒ 停機上呈（⛔ 自裁）

本單之行為 ＝ 塊 `K37` 之二之【工】之讀法（以交付之通知告 KL·⛔ 涉域上之新判）。撰碼中若見下列任一 ⇒ 停機上呈：本案之配地或任一紀錄有任一改變；本案之二退縮之任一街廓觸 `R-8` 之停機或 `R-3`／`R-4` 之「短街廓」之停機；街角規定範圍或末端塊範圍另有被建構、或其面積另有被計算而 `R-3`〜`R-7` 未及之處（`_build_corner_range_v3`、`_end_band`、`_end_region_R` 之他之呼叫；其傳與否涉配地者·`verify/wf_f4.py` 之 `_reshape_block` 除外〔`R-9`〕）；`F35 run` 之 `R2` 之某一街廓之範圍之面積 ≠ 其輸入值（`±0.01 ㎡`）。

### `§三-5`　執行端之設計說明（報告 ⑦ 須載）

逐條（`R-1`〜`R-9`）：落於何處、其字樣；`R-3`／`R-4` 之求解之法（倍增之上界、二分之止、⛔ 收斂之判）與其浮點之處；`_build_corner_range_v3`、`_end_band`、`_end_region_R`、`end_block_side_geom` 之一切呼叫處之全列（逐一名之·附其傳 `min_build_area` 與否及其由）；對 `§三-3` 各款之自查。另附 `git diff <工項一之端> <工項二之 commit> -- app.py verify/stepg_pipeline.py verify/run_verification.py` 之全文（報告同目錄之 `.diff`）。

---

## `§四`　驗收

### `§四-1`　工項（依序·各一 `commit`·皆推新側支 `verify/W-G.9-391-k980x`）

**工項零　本單原封入倉**（新側支·零生產碼）：`docs/orders/W-G.9-391_規格單.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-391 工項零：本單原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:refs/heads/verify/W-G.9-391-k980x`（**新立**·⛔ `--force`）；推後 `git ls-remote --heads origin` 之列數 ＝ **`51`**、主線仍 ＝ `a8657c4…`。其後之工項一律 `git push origin HEAD:verify/W-G.9-391-k980x`（快轉）。

**工項一　量測器**（**先於生產碼**·零生產碼）：塊 `Fy46` 抽為 `<O>/Fy46.diff`，對拍 `§五-1` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`12` 檔（`11` 改·`1` 新）之 `git hash-object` ＝ `§五-1` 項 `5`；`git status --porcelain` 唯此 `12` 檔（停機款 `3`）。`commit` 訊息之首列逐字 `W-G.9-391 工項一：量測器（F35 之新器·既有之器十一之增許）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-391-k980x`。

**工項二　生產碼**（🔴 `app.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py`·執行端依 `§三` 撰寫·一 `commit`）

**前置**（於工項一之端·⛔ `commit`·出艙一律存 `<O>`·`發單端.md` 丙 3之一之三份）：
1. **(甲) 本單新增或修改之量測器之呼叫**（照跑·末列逐字 ＝ `§五-1` 項 `8` 之工項一之端之列）：`§五-1` 項 `8` 之表之 `#1`, `#2`, `#3`, `#4`, `#5`, `#17`, `#6`, `#13`, `#18`, `#7`, `#19`, `#62`, `#63`, `#64`, `#65`, `#66`, `#69`, `#70`, `#71`, `#72`, `#73`, `#74`, `#75`, `#76`, `#77`, `#9`, `#25`, `#36`, `#37`, `#67`, `#38`, `#39`, `#68`（`33` 呼叫·其命令逐字見該表）：`#75` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；`#76` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W8', 'W9']；rc 1`；`#77` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['受詞缺']；rc 1`；其餘 `30` 呼叫 ⇒ `rc 0`·末列 ＝ 該表之同列；諸呼叫之 `stderr` 皆 `0` B。
2. **(乙) 本案配地之前後比對之前態**（照跑）：`python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_pre_35.json`；同 `0.0` ⇒ `<O>/k6s3_pre_00.json`；`python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_pre_35.json`；同 `0.0` ⇒ `<O>/f8_pre_00.json`；`python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_pre.json`；同 `0.0` ⇒ `<O>/parity00_pre.json`（皆 `rc 0`·末列 ＝ `§五-1` 項 `8` 之 `#56`〜`#61` 之工項一之端之列）。
3. **(丙) 本單未動之量測器之呼叫**（`§五-1` 項 `8` 之表之 `#1`〜`#74` 中 (甲)(乙) 以外之 `38` 呼叫）：`§零-0` 項 `6` 之比對皆同（主線之端 ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f` ＝ 基準之 sha、`python3 --version`、`pip freeze` 之 `sha256` ＝ 基準所載）⇒ **沿用** `基準/a8657c4012d961eccebd77cd812c0ab6aeab030f.md` 之值、⛔ 重跑；任一不同 ⇒ 整份照跑（其期 ＝ 該表之工項一之端之列·皆 `rc 0`）。回報記其比對與所為。
4. `git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py verify/run_verification.py`（逐一）：「K-9-80 ⑥」「k980_mba」「k980_range_touch_check」「end_block_band_width」⇒ 各**無出艙**、`rc 1`（`V-8` 之判別力）。

任一 ≠ 期 ⇒ 停機款 `4`。

**施**：執行端依 `§三` 撰寫三檔之改動；`python3 -m py_compile app.py verify/stepg_pipeline.py verify/run_verification.py`；`commit` 訊息之首列逐字 `W-G.9-391 工項二：街角規定範圍與末端塊範圍依最小建築面積之擴大·短街廓之警示停止（K-9-80 ④⑤⑥·K-9-34）🔴 生產碼（新側支）`。**⛔ 即 `push`。**

**驗**（於工項二之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>/*_post.*`·🔒 一律從頭整套照跑·⛔ 沿用基準）：

| # | 受詞 | 期 |
|---|---|---|
| `V-1` | 塊 `Fy46` 所改、所增之器之呼叫（`33` 呼叫·`§五-1` 項 `8` 之表之 `#1`, `#2`, `#3`, `#4`, `#5`, `#17`, `#6`, `#13`, `#18`, `#7`, `#19`, `#62`, `#63`, `#64`, `#65`, `#66`, `#69`, `#70`, `#71`, `#72`, `#73`, `#74`, `#75`, `#76`, `#77`, `#9`, `#25`, `#36`, `#37`, `#67`, `#38`, `#39`, `#68`） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F35 selftest` 之 `C1`〜`C9`、`E1`〜`E6`、`T1`〜`T6`、`K1` 與 `P0 22／22`、`F35 wiring` 之 `W1`〜`W9`、`F35 run` 之 `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0` 皆 ✅ |
| `V-2` | 其餘之呼叫（`§五-1` 之「項 `8` 之表」之 `#1`〜`#74` 中 `V-1` 與 `#56`〜`#61` 以外者·其命令逐字見該表） | 皆 **`rc 0`**；末列 ＝ `§五-1` 項 `8` 之施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` |
| `V-3` | `V-1`〜`V-2` 之器之載入 | 本批所改、所增之器 `12` 檔之 blob ＝ `§五-1` 項 `5`（⛔ 改器） |
| `V-4` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_post_35.json`；同 `0.0`；`… cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json`；同 `0.0` | `run` 皆 `rc 0`；`cmp` 皆 **`rc 0`**、末列逐字 `相異 0 項 ⇒ ✅ 同`（**本案之配地⛔ 變**） |
| `V-5` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_post.json`；同 `0.0` ⇒ `<O>/parity00_post.json` | `parity` 皆 **`rc 0`**；末列逐字 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置 `2` 之同呼叫：**唯落檔之 `"head"` 欄與 `stdout` 首列之 `HEAD` 異（二態之 `commit` 必異·`自誤 607`），以外逐位同**（以「以同一字樣代 `HEAD` 之全值後逐位比」量之，並另載一對照：⛔ 代之則相異） |
| `V-6` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_post_35.json`；同 `0.0` ⇒ `<O>/f8_post_00.json`；`git hash-object <O>/f8_pre_35.json <O>/f8_post_35.json`；同 `00` | `run` 皆 **`rc 0`**、末列逐字 `⇒ 紅 []；rc 0`；二 `hash-object` 之出艙各二列相等（落檔逐位同） |
| `V-7` | 生產碼 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py`）對工項一之端 | 相異恰 **`3`**（`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）；其增／刪之數與其 blob 出艙（發單端復驗時自倉重算·⛔ 預載）；`verify/` 之一切檔對工項一之端相異唯此二；三檔之頂層之名與相異之節點 ＝ `§三-3` 第 `4` 款（AST） |
| `V-8` | `R-1`〜`R-8` 之字樣（`git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py verify/run_verification.py`·逐一） | 「K-9-80 ⑥」⇒ `app.py` ≥ `3`；「k980_mba」⇒ 三檔各 ≥ `1`；「k980_range_touch_check」⇒ `app.py` ≥ `3`、`verify/stepg_pipeline.py` ≥ `1`；「end_block_band_width」⇒ `app.py` ≥ `2`（其數出艙·判別力 ＝ 前置 `4`） |
| `V-9` | `V-1`〜`V-6` 之諸器之 `stderr` | 合計 **`0`** B |

任一 ≠ 期 ⇒ 停機款 `6`（**⛔ 改量測器、⛔ 改 `§三-3` 之禁改以求其過**；逾時之重跑依單首 🔑）。🔒 **`run_all` ⛔ 跑之由**（KL 令·單首之「級」）：本批之受詞（有輸入者之範圍之擴大）本案⛔ 觸（harness ⛔ 輸入·`§一` 項 `5`），其「⛔ 變」由 `V-4`〜`V-6` 直接量之；擴大之接線由 `F35 run` 之 `R2`（以 session 之街廓覆寫輸入）實跑量之。

**唯讀獨立審查**（驗皆符後、推前）：執行端另派一唯讀之 reviewer（⛔ 改檔、⛔ `commit`），以 `§三` 對照工項二之全文差異逐條審之，並專審：`R-3`／`R-4` 之求解（倍增之上界、二分之止、未切到街廓之處、浮點）；`R-5` 之未臨正街之多邊形與 `end_block_side_geom` 者之同一；`R-6`／`R-7` 之一切呼叫處（窮查 `_build_corner_range_v3`、`_end_band`、`_end_region_R`、`end_block_side_geom`、`街角最小面積`、`r_end` 之讀處·有範圍或其面積另算而未傳者即「名單或門檻用未擴大之範圍」）；`R-8` 之受詞（街角與街角、街角與末端塊、末端塊與末端塊）之齊全；`§三-3` 之六款；以獨立之合成之例（`F35` 之外·至少二例：其一 ＝ 一街廓有一側街與一末端塊而擴大後相接；其二 ＝ 側街斜交而擴大後之範圍之遠側界線之方向）比改前、改後之行為；其發現逐條載入報告 ⑥。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ 執行端修之、重驗 `V-1`〜`V-9`、於報告具名。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-391-k980x`。

**工項三　入典與登記**（零生產碼·一 `commit`）：
1. 塊 `K37` 附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末；塊 `P48` 附於 `docs/待落地清單.md` 之末（皆依圍欄之逐列索引抽出、對拍 `§五-1` 後以二進位附之·刪除欄 `0`·改前全檔為改後之嚴格前綴·停機款 `3`／`8`）；二檔之 blob ＝ `§五-1` 項 `5`。
2. 自倉內 `docs/orders/W-G.9-365_輕量單.md` 以 `§五-1` 末之抽取式取出塊 `CK`（附錄午）、`GF`（附錄巳），對拍 `§五-1` 項 `7`，寫為 `<O>/checkidx.py`、`<O>/gen_fa_index.py`（⛔ 入倉）。
3. 二塊寫後：`python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列逐字 `索引列數 124；內部字樣 122；外部指標 9；不合 0`（本批⛔ 動索引）。
4. `python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md` ⇒ 出艙 `則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（停機款 `8`）。
5. `commit` 訊息之首列逐字 `W-G.9-391 工項三：範圍依最小建築面積之擴大之讀法入典·待落地清單之更新（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-391-k980x`。

**工項四　執行報告入倉**（新檔 `docs/reports/W-G.9-391R_範圍依最小建築面積之擴大_執行報告.md` ＋ 同目錄之 `W-G.9-391R_範圍依最小建築面積之擴大_差異.diff`·零生產碼·一 `commit`）：須載 ① 逐 `commit` 之 hash 與工項；② 停機款 `1`〜`13` 之三值（款·期·實）；③ 前置與驗之全部出艙（`V-1` 之諸呼叫之全文、`V-5` 之正規化之比與其對照、`V-6` 之 `hash-object` 之出艙、`k6s3 cmp` 之全文、`parity` 之末十五列、前置 (丙) 之版本之比對與所為、`77` 呼叫之 `rc`／`stderr`／耗時／末列之表〔前置與驗二態·沿用者具名·重跑者二趟並載〕）；④ 塊之實得（bytes／`sha256`）與二檔之改前改後 bytes；⑤ 推送之目標與推後之 `git ls-remote --heads origin`；⑥ 執行端之自捕與自解、**唯讀獨立審查之發現與處置**；⑦ **設計說明**（`§三-5`）；⑧ **三檔之全文差異**（同目錄）；⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙；⑩ **各段耗時**（並行之數）。收工閘之實測值出艙於回報（⛔ 寫入本檔·自指）。`commit` 訊息之首列逐字 `W-G.9-391 工項四：執行報告入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-391-k980x`。其後依 `執行端.md` 丁回報於 `ops/queue`。

### `§四-2`　次單（⛔ 本單之期）

發單端復驗本批（自倉從頭重跑 `V-1`〜`V-9` 與收工閘·⛔ 沿用）⇒ 皆符且本案配地⛔ 變 ⇒ **入主線之短單**（快轉 `a8657c4` → 新側支之端·⛔ `--force`·自動化之委任之二之甲·快轉前於 `ops/queue` 之 `log.md` 與 `STATE.json` 之 `history` 記前後值）＋ 立 `基準/<新主線之全 sha>.md`；其後 `W-G.9-392`（`K-9-80` ③·先查其源）。

### `§四-3`　收工閘（工項四之 `commit` 推後·於新側支之端量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1` | 本批五筆 `commit` 之增刪欄（`git show --numstat`） | 工項零 ＝ 本單之增（刪 `0`）；工項一 ＝ `probe_WG9353_endmerge.py` `4`／`2`、`probe_WG9354_endcontest.py` `4`／`2`、`probe_WG9355_screenmerge.py` `4`／`2`、`probe_WG9363_k953.py` `7`／`0`、`probe_WG9367_adj4.py` `7`／`0`、`probe_WG9370_adj4mut.py` `7`／`0`、`probe_WG9385_k974.py` `8`／`1`、`probe_WG9387_k961h.py` `8`／`0`、`probe_WG9388_k961s3.py` `10`／`1`、`probe_WG9389_trialstop.py` `9`／`0`、`probe_WG9390_k961r.py` `9`／`1`、`probe_WG9391_k980x.py` `559`／`0`（唯此 `12` 檔）（增／刪）；工項二 ＝ `app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`（唯此三檔·其數出艙）；工項三 ＝ `K-6` 典 `57`／`0`、`docs/待落地清單.md` `21`／`0`（唯此二檔）；工項四 ＝ 報告二檔之增（刪 `0`）；五筆之首列 ＝ `§四-1` 所令逐字 |
| `2` | 生產碼 `34` 檔與 `verify/` 對 `a8657c4` | 生產碼相異恰 **`3`**（`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）；`verify/` 之一切檔相異恰 **`14`**（`M` `13`：`run_verification.py`、`stepg_pipeline.py`、`probes/probe_WG9353_endmerge.py`、`probes/probe_WG9354_endcontest.py`、`probes/probe_WG9355_screenmerge.py`、`probes/probe_WG9363_k953.py`、`probes/probe_WG9367_adj4.py`、`probes/probe_WG9370_adj4mut.py`、`probes/probe_WG9385_k974.py`、`probes/probe_WG9387_k961h.py`、`probes/probe_WG9388_k961s3.py`、`probes/probe_WG9389_trialstop.py`、`probes/probe_WG9390_k961r.py`；`A` `1`：`probes/probe_WG9391_k980x.py`）；本批之新檔（本單、新器、報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3` | 本批文字檔之 `CR`（真 `0x0D`·受詞 ＝ 新側支之端之 blob〔`git cat-file -p HEAD:<路徑>`〕·Python 計位元組·判別力：`data/V6.dxf` 之 blob ＝ `12308`） | 合計 **`0`**（`20` 檔：本單、`12` 器、生產碼三檔、`K-6` 典、`docs/待落地清單.md`、報告二檔） |
| `4` | 二檔之 bytes | `K-6` 典 `909964` → **`919452`**；`docs/待落地清單.md` `20188` → **`23233`**；改前皆為改後之嚴格前綴；其尾 ＝ 塊；`CLAUDE.md`、自誤簿、`GB` 簿、`VR` 簿、`.claude/`、`verify/selection_pipeline.py` 對 `a8657c4` 相異 `0` |
| `5` | 自限 | 遠端 heads **`51`**；主線 ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`（⛔ 變）；`verify/W-G.9-391-k980x` ＝ 工項四之 `commit`，其祖含 `a8657c4`；其餘 `50` 列中除 `ops/queue`（回報後可變）外之 `49` 列（含主線）逐列 ＝ `<O>/heads_before_391.txt` 之同列 |
| `6` | `python3 verify/probes/probe_WG9270_closegate.py 634 629 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 635 634 .` ⇒ `rc 7` |
| `7` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 634 629` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零-0` 項 `3` 之值（⛔ 變） |
| `8` | 工項三之項 `3`／`4` 於新側支之端重跑 | 同其期 |

🔒 **必過之實例**：發單端已於拋棄式 worktree 模擬工項零〜四並實跑閘 `1`〜`4`、`6`〜`8` ⇒ 見 `§五-1` 項 `10`。

---

## `§五`　驗收之基數

### `§五-1`　受單側收單時須當場重算之基數

| # | 受詞 | 值（發單端擬本單時以程式重算） |
|---|---|---|
| `1` | 本單 | 見本單末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 塊 `Fy46` | `56670` B·`sha256` `44884335729bc8b1cf79c144a3cdb959b13ce4949b2c9c5233b83424c6698cf5`·`861` 列（圍欄內全文·末附換行）；抽為 `<O>/Fy46.diff`，`git apply` 於 `verify/probes/` 之 `12` 檔（`11` 改·`1` 新），其施前 blob（B）：`probe_WG9353_endmerge.py` `8a9d11c2dd7ee42220022eab1549a5d808b4e769`（`44265`）、`probe_WG9354_endcontest.py` `066261c86675fdb2d7b49c8715fd6015b63617ca`（`55924`）、`probe_WG9355_screenmerge.py` `776cddce3b0ec99468ce1a6c33cc71deb5241d57`（`38127`）、`probe_WG9363_k953.py` `468eb1faad6b2ec373829be90e56727898555104`（`127760`）、`probe_WG9367_adj4.py` `0e10ba31053f1368304817ffb764a0f039bab06f`（`73566`）、`probe_WG9370_adj4mut.py` `7aa267a87c9a7828d11f6c71b13573ab51655157`（`21032`）、`probe_WG9385_k974.py` `b44cd02b459b3a254cf8539a254170e9aa6d26f9`（`43431`）、`probe_WG9387_k961h.py` `4081e384dfa238d287d0604bd0a91e4864bd0ca3`（`23549`）、`probe_WG9388_k961s3.py` `8cc7d3a065243e496dc41ac1fa6a2b742e966101`（`41613`）、`probe_WG9389_trialstop.py` `0decb9551f484c7ff74e52eceb3623e2efa057f2`（`33432`）、`probe_WG9390_k961r.py` `eb3ad6afb0f4589f9f9d466f1d8b3b246b28b8d5`（`28810`）；`probe_WG9391_k980x.py` 施前⛔ 存 |
| `3` | — | （⛔ 用） |
| `4` | 塊 `K37`／`P48` | 塊 `K37` `9488` B·`sha256` `0b26ce6fcfcefc753f2969343b8398c48b1f3641657095d9cb659e9d03df1afb`·`57` 列；塊 `P48` `3045` B·`sha256` `1a3580158b9588e82d151d05eba573dcb1bbb344264e7b965b1448ddd7cd3ed1`·`21` 列（二者皆圍欄內全文·末附換行·首列為空列）；`K37` 附於 `K-6` 典（`909964` B）之末 ⇒ `919452` B；`P48` 附於 `docs/待落地清單.md`（`20188` B）之末 ⇒ `23233` B |
| `5` | 寫出後之 blob | 工項一之 `12` 器（`verify/probes/`·B）：`probe_WG9353_endmerge.py` ＝ `24bb035ffceecb346914e700764ac40b153a6a1d`（`44523`）、`probe_WG9354_endcontest.py` ＝ `10df59760e80b96a7f41f97f6bcca668186682e1`（`56182`）、`probe_WG9355_screenmerge.py` ＝ `4c450cf963cb7ffe39dcd528726a0482e1c216eb`（`38389`）、`probe_WG9363_k953.py` ＝ `2ce4dd5bb5f330c084e4667c44b13ddcd36f7825`（`128437`）、`probe_WG9367_adj4.py` ＝ `67af34857e44ed3b186091e096f28ef18c6ffb70`（`74366`）、`probe_WG9370_adj4mut.py` ＝ `1f1118b7457feb7aaa4c06d0abb3f361320075fa`（`21675`）、`probe_WG9385_k974.py` ＝ `c5cf831b8b872c21987a370984e4eba985fca44a`（`44341`）、`probe_WG9387_k961h.py` ＝ `cf1d143df2ca188070a6787903753fe56e0798e5`（`24486`）、`probe_WG9388_k961s3.py` ＝ `a24ddf7e29c20ed6547e1fa847457881e76774e6`（`42532`）、`probe_WG9389_trialstop.py` ＝ `72ff303cb761bdc12a4402f70b7d8beb133512d0`（`34486`）、`probe_WG9390_k961r.py` ＝ `40b4b1b73f6aefd24bf8080c8da054fb8b3588d5`（`29744`）、`probe_WG9391_k980x.py` ＝ `80f6326ef5dea32b769e2423da0338cd86553fea`（`33297`·新）；工項三之二檔：`K-6` 典 ＝ `0fad1dafd3c6236b571969b1538170f8662d9ee6`（`919452` B）、`docs/待落地清單.md` ＝ `48b50c3da80dff7143b82fc9eeba00673750a158`（`23233` B）。🔒 生產碼三檔之施後 blob **⛔ 預載**（規格單·由執行端回報） |
| `6` | — | （⛔ 用） |
| `7` | 塊 `CK`／`GF`（自倉內 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳） | 塊 `CK` `1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；塊 `GF` `2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列（＝ `W-G.9-390` 規格單 `§五-1` 項 `7`） |
| `8` | 量測器之二態（發單端實跑·倉外·雲端 Linux `4` 核） | 見本節末之「項 `8` 之表」（`77` 呼叫·二態之 `rc`／`stderr`／末列） |
| `9` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本單>`·發單端實跑（態 `a8657c4`·定稿之前一版·其後唯本列與項 `10` 之文字之填）：🔴 機械 `0` 項／🟡 提示 `3` 項——`P-4` 於 `§三-2` 之 `F35` 之列（其箭頭為逐層照傳之呼叫之鏈）、`§四-3` 之表之首列（其箭頭為改前至改後之 bytes〔閘 `4`〕）、附錄丙之表之首列（塊 `P48` 之內之試算 `G` 之前後〔`307.79` 至 `307.78 ㎡`〕）⇒ **具名豁免**（皆非方向之轉引）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23508`–`31250`·本單⛔ 用） |
| `10` | 收工閘之模擬（發單端·⛔ `push`） | `git worktree add --detach <S> a8657c4`（拋棄式·雲端 Linux）＋ 本單（定稿之前一版·其三塊與定稿逐位同）＋ 原型之三檔（代工項二）＋ 報告之替身·五 `commit`：塊之抽取 ＝ 項 `2`／`4`、塊 `CK`／`GF` ＝ 項 `7`；`git apply --check` 過；`12` 器之施後 blob ＝ 項 `5`、`git status --porcelain` 唯此 `12` 檔；前置 `4` 之四字樣皆 `rc 1`；工項二 ＝ `app.py` `168`／`18`、`verify/run_verification.py` `1`／`0`、`verify/stepg_pipeline.py` `9`／`0`（原型）·`V-8` 之四字樣 ＝ 期（`app.py` 「K-9-80 ⑥」`4`、「k980_mba」`7`、「k980_range_touch_check」`4`、「end_block_band_width」`8`；`verify/run_verification.py` 「k980_mba」`1`；`verify/stepg_pipeline.py` 「k980_mba」`3`、「k980_range_touch_check」`1`）；二檔之施後 blob、bytes ＝ 項 `5`、閘 `4`；`checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·逐位同；閘 `1` 之五筆之增刪 ＝ 該閘之期（工項一 ＝ 項 `5` 之 `12` 器之列·工項三 ＝ `K-6` 典 `57`／`0`、`docs/待落地清單.md` `21`／`0`·工項四〔替身〕二檔各 `1`／`0`）·首列 ＝ 所令逐字；閘 `2` ＝ 生產碼相異 `3`、`verify/` 相異 `14`（`M` `13`·`A` `1`）·新檔四之 `git check-ignore -v --no-index` 皆 `rc 1`（對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` `20` 檔之 blob `CR` `0`（`data/V6.dxf` `12308`）；閘 `4` 前綴皆真·`CLAUDE.md` 等相異 `0`；閘 `6` `rc 0`（判別力 `635 634` ⇒ `rc 7`）；閘 `7` `rc 0`（四簿 ＝ `§零-0` 項 `3`）；閘 `8` ＝ 期；閘 `5` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空。`V-1`〜`V-6` 之器⛔ 於模擬重跑：其受詞之檔與 `§一` 項 `3`〜`5` 之實跑逐位同（`12` 器 ＝ 項 `5`、生產碼三檔 ＝ 原型） |

**項 `8` 之表**（`#1`〜`#74` ＝ `基準/a8657c4012d961eccebd77cd812c0ab6aeab030f.md` 之呼叫〔其序與命令同之〕；`#75`〜`#77` ＝ `F35 selftest`／`F35 wiring`／`F35 run`；`#56`〜`#61` 之落檔之名：工項一之端 ⇒ `_pre`、施後 ⇒ `_post`；格 ＝ `rc`／`stderr` B／末列逐字；耗時（s）見括號·⛔ 為期。「工項一之端」之欄：前置 (甲) 之 `33` 呼叫 ＝ 發單端於 `a8657c4` ＋ 塊 `Fy46` 之實跑；其餘 `44` 呼叫 ＝ 基準之值〔前置 (乙)(丙)·其樹與工項一之端唯塊 `Fy46` 之 `12` 器異、其 `12` 器之呼叫皆入 (甲)〕。「施後」＝ 原型 ＋ 塊 `Fy46`·發單端實跑·並行 `2`）：

| # | 命令 | 工項一之端 | 施後（原型） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（127） | `0`／`0`／`⇒ 紅 []；rc 0`（152） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（395） | `0`／`0`／`⇒ 紅 []；rc 0`（395） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（32） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（31） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·36） | `0`／`0`／`⇒ 紅 []；rc 0`（42） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·14） | `0`／`0`／`⇒ 紅 []；rc 0`（15） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·232） | `0`／`0`／`⇒ 紅 []；rc 0`（272） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·70） | `0`／`0`／`⇒ 紅 []；rc 0`（89） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（438） | `0`／`0`／`⇒ 紅 []；rc 0`（498） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（617） | `0`／`0`／`⇒ 紅 []；rc 0`（694） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（10） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（10） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（基準·67） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（81） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·389） | `0`／`0`／`⇒ 紅 []；rc 0`（412） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1733） | `0`／`0`／`⇒ 紅 []；rc 0`（1776） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·33） | `0`／`0`／`⇒ 紅 []；rc 0`（40） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·5） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（基準·21） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（24） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·21） | `0`／`0`／`⇒ 紅 []；rc 0`（24） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·243） | `0`／`0`／`⇒ 紅 []；rc 0`（273） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·325） | `0`／`0`／`⇒ 紅 []；rc 0`（360） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·35） | `0`／`0`／`⇒ 紅 []；rc 0`（41） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·31） | `0`／`0`／`⇒ 紅 []；rc 0`（37） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（7） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（18） | `0`／`0`／`⇒ 紅 []；rc 0`（23） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（15） | `0`／`0`／`⇒ 紅 []；rc 0`（17） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（10） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·181） | `0`／`0`／`⇒ 紅 []；rc 0`（211） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·48） | `0`／`0`／`⇒ 紅 []；rc 0`（61） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·799） | `0`／`0`／`⇒ 紅 []；rc 0`（867） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·148） | `0`／`0`／`⇒ 紅 []；rc 0`（178） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·99） | `0`／`0`／`⇒ 紅 []；rc 0`（133） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·325） | `0`／`0`／`⇒ 紅 []；rc 0`（356） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（基準·1） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（基準·9） | `0`／`0`／`紅項 [] 器紅 0`（11） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·331） | `0`／`0`／`⇒ 紅 []；rc 0`（372） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（基準·187） | `0`／`0`／`（JSON 之摘要列·略）`（223） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（基準·136） | `0`／`0`／`（JSON 之摘要列·略）`（153） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·189） | `0`／`0`／`⇒ 紅 []；rc 0`（218） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·138） | `0`／`0`／`⇒ 紅 []；rc 0`（158） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（基準·412） | `0`／`0`／`⇒ rc 0（不符 0 項）`（458） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（基準·294） | `0`／`0`／`⇒ rc 0（不符 0 項）`（310） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（331） | `0`／`0`／`⇒ 紅 []；rc 0`（369） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1236） | `0`／`0`／`⇒ 紅 []；rc 0`（1240） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1234） | `0`／`0`／`⇒ 紅 []；rc 0`（1254） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（128） | `0`／`0`／`⇒ 紅 []；rc 0`（156） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（436） | `0`／`0`／`⇒ 紅 []；rc 0`（486） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（321） | `0`／`0`／`⇒ 紅 []；rc 0`（360） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W8', 'W9']；rc 1`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（26） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（153） |

**二態之對拍**（發單端·上表之落檔）：`k6s3 cmp` 二退縮皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`·`stderr` `0` B（對照組 `相異 18 項 ⇒ 🔴 異`）；`F8` 之落檔 `git hash-object` 前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮之落檔與 `stdout` 前後逐位同（發單端之二態同在 `a8657c4` 之 `HEAD`·執行端之二態之 `HEAD` 異 ⇒ 依 `V-5` 代之） ⇒ **本案配地⛔ 變**。

抽取式 ＝ 圍欄開列（四個反引號 `` ```` `` 繼以語言名之列·本單用 `diff` 與 `markdown`）之次列至閉列（恰四個反引號之列）之前一列，逐列以 `\n` 相接並末附 `\n`，UTF-8 編碼；本單之塊以其附錄之標題列（以 `## 附錄甲`〜`## 附錄丙` 起首之列）之後之第一個圍欄開列為準。🔒 **自他單取塊**（塊 `CK`／`GF`）：以該單之附錄之標題列（以 `## 附錄午`／`## 附錄巳` 起首之列）之後之第一個圍欄開列為準（該單之圍欄之語言名不拘·`自誤 578`）。

### `§五-2`　上呈

1. 任一停機款成就 ⇒ **停機上呈**·⛔ 自改。
2. 工項零〜四 ⇒ 逕行 `push` 新側支 `verify/W-G.9-391-k980x`（工項二於驗與審查皆符後）；主線⛔ 動。
3. 回報 ⇒ `ops/queue` 之 `reports/W-G.9-391_規格單_回報.md`（`執行端.md` 丁）。

---

## 附錄甲　塊 `Fy46`（`git apply` 之差異·`verify/probes/` 之 `12` 器·工項一）

````diff
diff --git a/verify/probes/probe_WG9353_endmerge.py b/verify/probes/probe_WG9353_endmerge.py
index 8a9d11c..24bb035 100644
--- a/verify/probes/probe_WG9353_endmerge.py
+++ b/verify/probes/probe_WG9353_endmerge.py
@@ -553,12 +553,14 @@ def _pipeline(ns, fake_st, rv, sb, scen=None):
             hits["merge"] += 1
         return saved["end_block_merge_run"](temp, build, own, set(locked) | set(cfg["lock"]), corner, *a, **k)
 
-    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
+    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label='',
+            min_build_area=None):  # 🔧 `W-G.9-391`：`end_block_side_geom` 增 `min_build_area`（照傳·未傳者⛔ 傳·F35 量之）
         if cfg["mw"] is not None and _label == "R6":
             hits["geo"] += 1
             min_width = cfg["mw"]
         return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
-                                            min_width, side, _label=_label)
+                                            min_width, side, _label=_label,
+                                            **({} if min_build_area is None else {"min_build_area": min_build_area}))
     ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
     try:
         with contextlib.redirect_stdout(io.StringIO()):
diff --git a/verify/probes/probe_WG9354_endcontest.py b/verify/probes/probe_WG9354_endcontest.py
index 066261c..10df597 100644
--- a/verify/probes/probe_WG9354_endcontest.py
+++ b/verify/probes/probe_WG9354_endcontest.py
@@ -650,12 +650,14 @@ def _pipeline(ns, fake_st, rv, sb, scen=None):
     cfg = SCEN.get(scen) or dict(wid={}, lock=[], excl=[])
     hits = {"host": 0, "merge": 0, "geo": 0}
 
-    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
+    def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label='',
+            min_build_area=None):  # 🔧 `W-G.9-391`：`end_block_side_geom` 增 `min_build_area`（照傳·未傳者⛔ 傳·F35 量之）
         # 注入：所給之端 ⇒ 末端塊（⛔ 未臨正街），R_end ＝ 以所給之寬構之末端帶（經宿主之 `_end_band`）
         w = cfg["wid"].get((_label, side))
         if w is None:
             return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
-                                                min_width, side, _label=_label)
+                                                min_width, side, _label=_label,
+                                            **({} if min_build_area is None else {"min_build_area": min_build_area}))
         hits["geo"] += 1
         p1 = np.asarray(corner_pt, float)[:2]
         dd = np.asarray(d_hat, float)[:2]
diff --git a/verify/probes/probe_WG9355_screenmerge.py b/verify/probes/probe_WG9355_screenmerge.py
index 776cddc..4c450cf 100644
--- a/verify/probes/probe_WG9355_screenmerge.py
+++ b/verify/probes/probe_WG9355_screenmerge.py
@@ -622,11 +622,13 @@ def _screen_pipeline_factory(f13, f4, extra):
         hits = {"host": 0, "merge": 0, "geo": 0}
         msig = inspect.signature(saved["end_block_merge_run"])
 
-        def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
+        def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label='',
+                min_build_area=None):  # 🔧 `W-G.9-391`：`end_block_side_geom` 增 `min_build_area`（照傳·未傳者⛔ 傳·F35 量之）
             w = cfg["wid"].get((_label, side))
             if w is None:
                 return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
-                                                    min_width, side, _label=_label)
+                                                    min_width, side, _label=_label,
+                                            **({} if min_build_area is None else {"min_build_area": min_build_area}))
             hits["geo"] += 1
             p1 = np.asarray(corner_pt, float)[:2]
             dd = np.asarray(d_hat, float)[:2]
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index 468eb1f..2ce4dd5 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -1519,6 +1519,13 @@ SP_ALLOW |= set(CHG384_SP)
 CHG385_APP = ("main", "calc_special_burden_total")
 KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG385_APP)
 APP_ALLOW |= {"K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales"} | set(CHG385_APP)
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+KEEP_APP = tuple(x for x in KEEP_APP if x not in W391)
+APP_ALLOW |= set(W391)
 
 
 def _top_dump(tree):
diff --git a/verify/probes/probe_WG9367_adj4.py b/verify/probes/probe_WG9367_adj4.py
index 0e10ba3..67af348 100644
--- a/verify/probes/probe_WG9367_adj4.py
+++ b/verify/probes/probe_WG9367_adj4.py
@@ -44,6 +44,7 @@
   🔧 `W-G.9-385`（`K-9-74`／`K-9-79`·⛔ 上列一字不刪）：wiring 之 W5 之許增 `K974_PARAMS`、`k962_land_marks`、
            `k974_read_junctions`、`k974_burden_scales`、`k974_screen_scales`、`calc_special_burden_total`、`main`（其接線與
            二函式之唯增列由 F30 之 wiring 量之）。
+  🔧 `W-G.9-391`（`K-9-34`·`K-9-80` ④⑥·⛔ 上列一字不刪）：wiring 之 W5 之許增範圍之擴大之六新名與九函式（其行為與接線由 F35 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, copy, difflib, io, os, re, subprocess, sys, warnings
@@ -772,6 +773,12 @@ ALLOW375_APP += ("K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_
 ALLOW375_APP += ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
                 "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
                 "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+ALLOW375_APP += W391
 
 
 def _git_show(repo, rev, rel):
diff --git a/verify/probes/probe_WG9370_adj4mut.py b/verify/probes/probe_WG9370_adj4mut.py
index 7aa267a..1f1118b 100644
--- a/verify/probes/probe_WG9370_adj4mut.py
+++ b/verify/probes/probe_WG9370_adj4mut.py
@@ -112,6 +112,13 @@ ALLOW373_APP += ("K974_PARAMS", "k962_land_marks", "k974_read_junctions", "k974_
 ALLOW373_APP += ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
                 "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
                 "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
+ALLOW373_APP += W391
+ALLOW375_FILES += F391
 
 
 def _strip_fns(src, names):
diff --git a/verify/probes/probe_WG9385_k974.py b/verify/probes/probe_WG9385_k974.py
index b44cd02..c5cf831 100644
--- a/verify/probes/probe_WG9385_k974.py
+++ b/verify/probes/probe_WG9385_k974.py
@@ -42,6 +42,7 @@
            （同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）。
 🔧 `W-G.9-388`（⛔ 上列一字不刪）：W7 之頂層之相異之許增 `k6b_stage3_run`（`K-9-61` ①②③⑥·其行為由 F32 量之）。
 🔧 `W-G.9-389`（⛔ 上列一字不刪）：W7 之頂層之相異之許增試算內之程式之停機之上拋之五新名與十一函式（其行為與接線由 F33 量之）。
+🔧 `W-G.9-391`（`K-9-34`·`K-9-80` ④⑥·⛔ 上列一字不刪）：W7 之頂層之相異之許增範圍之擴大之六新名與九函式（`main` 之唯增列照舊·其行為與接線由 F35 量之）。
 rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
 """
 import ast, contextlib, io, os, sys
@@ -57,6 +58,11 @@ NEW_NAMES = ["K974_PARAMS"] + NEW_FUNCS
 W389_APP = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
                 "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
                 "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 TOL = 1e-9
 
 
@@ -498,8 +504,9 @@ def wiring(repo, base):
         # 🔧 `W-G.9-387`：其後之單所改之頂層節點亦許（`adj_intake`·`K-9-61` ⑧·其行為由 F31 量之）
         # 🔧 `W-G.9-388`：同（`k6b_stage3_run`·`K-9-61` ①②③⑥·其行為由 F32 量之）
         # 🔧 `W-G.9-389`：同（試算內之程式之停機之上拋·F33 量之）
+        # 🔧 `W-G.9-391`：同（範圍依最小建築面積之擴大·F35 量之）
         ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
-               | set(W389_APP)
+               | set(W389_APP) | set(W391)
                and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
         res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
     except Exception as e:
diff --git a/verify/probes/probe_WG9387_k961h.py b/verify/probes/probe_WG9387_k961h.py
index 4081e38..cf1d143 100644
--- a/verify/probes/probe_WG9387_k961h.py
+++ b/verify/probes/probe_WG9387_k961h.py
@@ -40,6 +40,11 @@ NEW389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial
 W389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
             "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
             "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
 # 外部錨（R3）：主線 `34736ab` 之 `probe_WG9351_intake.py run <repo>` 之「單位」列之原街廓（發單端 2026-10-17 實跑）
 EXPECT_RUN = {
@@ -271,6 +276,8 @@ def wiring(repo, base):
         ok3 = set(bt) == set(ct) and set(dif) <= {FN_AI} | {"k6b_stage3_run"}    # 🔧 `W-G.9-388`：其後之單所改者亦許（F32 量之）
         ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) and set(bt) <= set(ct)
                       and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389))   # 🔧 `W-G.9-389`：同（F33 量之）
+        ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) | set(NEW391) and set(bt) <= set(ct)
+                      and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389) | set(W391))   # 🔧 `W-G.9-391`：同（F35 量之）
         res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", ok3,
                     f"增 {sorted(set(ct) - set(bt))}／去 {sorted(set(bt) - set(ct))}／相異 {dif}"))
         ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
@@ -287,6 +294,7 @@ def wiring(repo, base):
             if b != c:
                 chg.append(p)
         chg = [p for p in chg if p != "verify/selection_pipeline.py"]   # 🔧 `W-G.9-389`：其增列（F33 之 X4 量之）
+        chg = [p for p in chg if p not in F391]   # 🔧 `W-G.9-391`：harness 二檔之增列（F35 量之）
         res.append((f"X5 生產碼 app.py 以外之 {len(prod)} 檔對基準相異 0", not chg and len(prod) >= 1, f"相異 {chg}"))
     except Exception as e:  # noqa: BLE001
         res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", False, f"基準讀不到：{type(e).__name__}"))
diff --git a/verify/probes/probe_WG9388_k961s3.py b/verify/probes/probe_WG9388_k961s3.py
index 8cc7d3a..a24ddf7 100644
--- a/verify/probes/probe_WG9388_k961s3.py
+++ b/verify/probes/probe_WG9388_k961s3.py
@@ -47,6 +47,11 @@ NEW389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial
 W389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
             "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
             "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 
 try:
     sys.stdout.reconfigure(encoding="utf-8")
@@ -532,6 +537,9 @@ def wiring(repo, base):
     # 🔧 `W-G.9-389`：其後之單之新名（名之集唯增之）與所改之頂層節點亦許（F33 量之）
     ok3 = ok3 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW389) and set(tb) <= set(ta)
                   and set(diff) <= {"k6b_stage3_run"} | set(W389))
+    # 🔧 `W-G.9-391`：同（F35 量之）
+    ok3 = ok3 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW389) | set(NEW391) and set(tb) <= set(ta)
+                  and set(diff) <= {"k6b_stage3_run"} | set(W389) | set(W391))
     print(("  ✅" if ok3 else "  🔴") + f" X3 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
     if not ok3:
         red.append("X3")
@@ -541,7 +549,8 @@ def wiring(repo, base):
     if lits:
         red.append("X4")
     ch = [l for l in _git(repo, "diff", "--name-only", base, "--", "verify/").splitlines()
-          if l.count("/") == 1 and l.endswith(".py") and l != "verify/selection_pipeline.py"]   # 🔧 `W-G.9-389`：其增列（F33 量之）
+          if l.count("/") == 1 and l.endswith(".py") and l != "verify/selection_pipeline.py"
+          and l not in F391]   # 🔧 `W-G.9-389`：其增列（F33 量之）·🔧 `W-G.9-391`：harness 二檔（F35 量之）
     print(("  ✅" if not ch else "  🔴") + f" X5 verify/ 頂層之 *.py 對基準逐位同（異 {ch}）")
     if ch:
         red.append("X5")
diff --git a/verify/probes/probe_WG9389_trialstop.py b/verify/probes/probe_WG9389_trialstop.py
index 0decb95..72ff303 100644
--- a/verify/probes/probe_WG9389_trialstop.py
+++ b/verify/probes/probe_WG9389_trialstop.py
@@ -42,6 +42,11 @@ ALLOW = {"evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "en
          "f3_screen_adj4"}
 # 🔧 `W-G.9-390`：其後之單所改之頂層節點（⛔ 限於二形·F34 量之）
 ALLOW390 = {"k6b_stage3_run"}
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 TAG_RE = re.compile(r"(?<![0-9A-Za-z\-])GB-\d+(?![0-9])|【未裁】")
 TRIAL_CALLS = {"f3_screen_stepg_run", "run_step_g", "trial", "alloc_eval"}
 CATCH = {"RuntimeError", "_K6BTrialStop", "Exception"}
@@ -535,6 +540,8 @@ def wiring(repo, base):
             if not ok_:
                 why.append(f"{k}：{w_}")
     ok3 = add == NEW_TOP and not gone and set(dif) <= ALLOW | ALLOW390 and not why
+    # 🔧 `W-G.9-391`：其新名與所改之頂層節點亦許（⛔ 及 ALLOW 之二形之查·F35 量之）
+    ok3 = ok3 or (add == NEW_TOP | set(NEW391) and not gone and set(dif) <= ALLOW | ALLOW390 | set(W391) and not why)
     res.append(("X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形", ok3,
                 f"增 {sorted(add)}／去 {sorted(gone)}／相異 {dif}／不合 {why}"))
     # X4
@@ -545,6 +552,8 @@ def wiring(repo, base):
         diffs = [p for p in tops if _git_show(repo, base, p) != _read(repo, p)]
         ok4a, w4 = _diff_ok(sbsrc, ssrc)
         ok4 = diffs == ["verify/selection_pipeline.py"] and ok4a and "換 0" in w4
+        # 🔧 `W-G.9-391`：harness 二檔之增列亦許（selection_pipeline 之查照舊·F35 量之）
+        ok4 = ok4 or (sorted(set(diffs) - set(F391)) == ["verify/selection_pipeline.py"] and ok4a and "換 0" in w4)
         res.append(("X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列", ok4, f"異 {diffs}／{w4}"))
     except Exception as e:  # noqa: BLE001
         res.append(("X4 verify/ 頂層唯 selection_pipeline.py 異", False, f"中止 {type(e).__name__}：{e}"))
diff --git a/verify/probes/probe_WG9390_k961r.py b/verify/probes/probe_WG9390_k961r.py
index eb3ad6a..40b4b1b 100644
--- a/verify/probes/probe_WG9390_k961r.py
+++ b/verify/probes/probe_WG9390_k961r.py
@@ -45,6 +45,11 @@ LOCK = "取得即鎖定之宗之查"
 KEPT = "於試算⛔ 保留"
 BLOCKS = {"BA": {"category": H}, "BB": {"category": H}, "RD": {"category": RDC}}
 CL = {"RD": [(-40.0, -5.0), (90.0, -5.0)]}
+# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
+NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
+W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
+                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
+F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
 
 
 def _harvest(repo):
@@ -401,6 +406,9 @@ def wiring(repo, base):
     ta, tb = _top(app), _top(old)
     diff = sorted(k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k))
     ok2 = diff == ["k6b_stage3_run"] and set(ta) == set(tb)
+    # 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點亦許（F35 量之）
+    ok2 = ok2 or ("k6b_stage3_run" in diff and set(ta) - set(tb) == set(NEW391) and set(tb) <= set(ta)
+                  and set(diff) <= {"k6b_stage3_run"} | set(W391))
     print(("  ✅" if ok2 else "  🔴") + f" X2 頂層之相異 {diff}（期 ['k6b_stage3_run']）、名之集同 {set(ta) == set(tb)}")
     if not ok2:
         red.append("X2")
@@ -410,7 +418,7 @@ def wiring(repo, base):
     if lits:
         red.append("X3")
     ch = [l for l in _git(repo, "diff", "--name-only", base, "--", "verify/").splitlines()
-          if l.count("/") == 1 and l.endswith(".py")]
+          if l.count("/") == 1 and l.endswith(".py") and l not in F391]   # 🔧 `W-G.9-391`：harness 二檔（F35 量之）
     print(("  ✅" if not ch else "  🔴") + f" X4 verify/ 頂層之 *.py 對基準逐位同（異 {ch}）")
     if ch:
         red.append("X4")
diff --git a/verify/probes/probe_WG9391_k980x.py b/verify/probes/probe_WG9391_k980x.py
new file mode 100644
index 0000000..80f6326
--- /dev/null
+++ b/verify/probes/probe_WG9391_k980x.py
@@ -0,0 +1,559 @@
+# -*- coding: utf-8 -*-
+"""W-G.9-391 量測器（發單端擬·檔 F35·⛔ 由受單側改一字）：街角規定範圍與末端塊範圍依最小建築面積之擴大（`K-9-34`·
+`K-9-80` ④⑤）與短街廓之二範圍相接或重疊之警示停止（`K-9-80` ⑥）。
+
+所量之性質：街廓有最小建築面積之輸入（有效值 ＞ 0）而範圍之面積 ＜ 之 ⇒ 街角規定範圍之遠側界線續沿 SIDE_LINE 之法向平移
+（∥SIDE_LINE）、末端塊範圍之內側界線續沿 ALLOC 平行內移（末端塊無退縮），至 `0 ≤ 面積 − 最小建築面積 ≤ 0.01 ㎡`；未輸入
+（`None`、`0`）或面積已 ≥ 之 ⇒ 範圍⛔ 變（逐位同）；跨占之名單與門檻皆以擴大後之範圍定之（單一真相源）；一街廓之二範圍
+（街角與街角、街角與末端塊、末端塊與末端塊）擴大後相接（距 ≤ 0.01 m）或重疊、或擴至街廓之他端仍未達 ⇒ 停機（警示停止）。
+
+子命令（一律 python3 verify/probes/probe_WG9391_k980x.py <子命令> …）：
+  selftest <repo>
+           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取諸函式）。玩具街廓 BA：x∈[0,60]、y∈[0,30]，正面 y ＝ 0（p1 ＝ (0,0)·
+           p2 ＝ (60,0)），屁股線 y ＝ 30，左側街 x ＝ 0（截角三角形 (0,0)(3,0)(0,3)），宗地分配線 ∥ y 軸；退縮 0、畸零地寬 3.5、
+           分配深度 30。期值皆手算（各例之註）：
+           C1 未輸入（`None`）⇒ 面積 100.5（＝ 3.5×30 − 4.5）；C2 輸入 0 ⇒ 與 C1 逐位同；C3 輸入 100（＜ 100.5）⇒ 同 C1；
+           C4 輸入恰 100.5 ⇒ 同 C1（門檻上）；C5 輸入 150 ⇒ 面積 ∈ [150, 150.01]、遠側界線 x ＝ 5.15（±0.001）∥ SIDE_LINE、
+           含 C1 之範圍；C6 輸入 2000（＞ 街廓 1795.5）⇒ 停機（訊息含「K-9-80 ⑥」）；C7 輸入 −1 ⇒ 停機；C8 C5 之旋轉 37°、
+           鏡射並移至 TWD97 之尺度 ⇒ 面積同 C5（±1e-6）；C9 側街斜交（SIDE_LINE (0,0)→(6,30)·宗地分配線 ∥ y 軸·截角
+           (0,0)(3,0)(0.6,3)）輸入 200 ⇒ 面積 ∈ [200, 200.01]、遠側界線 ∥ SIDE_LINE（其於 y＝0 與 y＝30 之 x 差 ＝ 6）。末端塊之玩具 BE：多邊形 (10,0)(70,0)(70,30)(0,30)，正面 p1 ＝ (10,0)、
+           p2 ＝ (70,0)，左端之未臨正街 ＝ 三角形 150 ㎡：E1 未輸入 ⇒ R_end 255（＝ 150 ＋ 3.5×30）、內側界 x ＝ 13.5；E2 輸入 255
+           （門檻上）⇒ 同 E1；E3 輸入 300 ⇒ R_end ∈ [300, 300.01]、內側界 x ＝ 15（±0.001·∥ ALLOC）；E4 輸入 2000 ⇒ 停機
+           （「K-9-80 ⑥」）；E5 E3 之旋轉、鏡射、TWD97 ⇒ 同 E3；E6 `_end_region_R` 之未輸入與 0 ⇒ R_end 逐位同（255）、
+           `end_block_band_width` 之 0 ⇒ 停機（⛔ 入本函式）。
+           相接之判 T1 二矩形之距 0.02 ⇒ ⛔ 停；T2 距恰 0.01 ⇒ 停（≤）；T3 距 0.005 ⇒ 停；T4 重疊 ⇒ 停（訊息含二範圍之名）；
+           T5 唯一範圍或含 `None` ⇒ ⛔ 停；T6 三範圍而唯其中二者相接 ⇒ 停。K1 `k980_mba` 之有效值之序（`K-9-1` ⑨ 裁丙：街廓覆寫
+           → 分區底 → 0；session 無鍵或 `None` ⇒ 0）。P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
+  wiring   <repo> <基準 commit>
+           W1 `_build_corner_range_v3(` 之生產呼叫（`app.py`、`verify/stepg_pipeline.py`、`verify/run_verification.py`·AST）
+           皆以關鍵字傳 `min_build_area`；W2 `end_block_side_geom(`、`end_block_host(`、`_place_pool_parcels(` 之呼叫（同上
+           三檔·含 `ns["…"](` 之形）皆傳 `min_build_area`；W3 末端帶之單一真相源：`_place_pool_parcels` 呼叫 `_end_region_R`
+           恰一、⛔ 呼叫 `_end_band`，`_end_region_R` 呼叫 `end_block_band_width` 恰一（全檔亦恰一）；W4 上開生產呼叫之 `min_build_area=` 之值皆為 `k980_mba(…)`
+           （`select_corner_lots_both_sides_v12` 之 `_mba_pk` 之賦值恰一為之·其餘唯 `None`）、`k91_effective_min_build_area` 於
+           `k980_mba` 外之呼叫之數對基準⛔ 增；W5 `k980_range_touch_check(` 之呼叫：`select_corner_lots_both_sides_v12` 內、
+           `f3_screen_stepg_run` 內、`verify/stepg_pipeline.py` 之 `_run_step_g_impl` 內各恰一（`app.py` 全檔恰二）；W6 `app.py`
+           之頂層之名之增恰 `{K980_AREA_TOL, K980_AREA_EPS, K980_TOUCH_TOL, end_block_band_width, k980_range_touch_check,
+           k980_mba}`、無減；W7 新增或改之頂層節點內⛔ 案件字面；
+           W8 `min_build_area` 之逐層照傳（`end_block_host`→`end_block_apply`→`end_block_side_geom`→`_end_region_R`、
+           `_place_pool_parcels`→`_end_region_R` 之呼叫皆恰一而傳 `min_build_area=min_build_area`）；W9 `verify/stepg_pipeline.py`
+           經 `ns["…"]` 取之新名皆在 `app.py` 之 `_WF_NS_NAMES`（app 之七級調配之路·漏列即 KeyError）。另 W4 之 `k980_mba`
+           之分區之引數⛔ 為字面、W5 之範圍之名齊全（v12 二·二宿主四）。
+  run      <repo> [<退縮> …]
+           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 未輸入（harness 之現狀）⇒ 參數表之街角最小面積、街角選位之範圍面積、
+           Step-G 之 ctx 之範圍面積三者同、末端塊之紀錄之 `R_end` ＝ 改前之式（未臨正街 ＋ 末端帶）；R2 以 session 之 `K91_SS_MBA_BY_LABEL`（畫面之同一鍵）輸入「各街廓之最小建築面積 ＝ 其未輸入時之最大範圍之面積
+           ＋ 10 ㎡」⇒ 上開三源之街角最小面積皆 ＝ 輸入值（±0.01）、末端塊之 `R_end` ＝ 輸入值（±0.01）、⛔ 停機。
+rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
+"""
+import ast, contextlib, io, math, os, re, subprocess, sys
+
+try:
+    sys.stdout.reconfigure(encoding="utf-8")
+except Exception:  # noqa: BLE001
+    pass
+
+CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
+K6 = "K-9-80 ⑥"
+NEW_TOP = {"K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check",
+           "k980_mba"}
+
+
+def _harvest(repo):
+    sys.path.insert(0, os.path.join(repo, "verify"))
+    from app_harvest import harvest
+    with contextlib.redirect_stdout(io.StringIO()):
+        ns, fake_st = harvest(os.path.join(repo, "app.py"))
+    return ns, fake_st
+
+
+# ───────────────────────── selftest ─────────────────────────
+
+def _xf(ang_deg, mirror, tx, ty):
+    c, s = math.cos(math.radians(ang_deg)), math.sin(math.radians(ang_deg))
+
+    def f(p):
+        x, y = float(p[0]), float(p[1])
+        if mirror:
+            x = -x
+        return (c * x - s * y + tx, s * x + c * y + ty)
+
+    def v(d):
+        x, y = float(d[0]), float(d[1])
+        if mirror:
+            x = -x
+        return (c * x - s * y, s * x + c * y)
+    return f, v
+
+
+def _corner(ns, mba, xf=None, mirror=False):
+    from shapely.geometry import Polygon
+    f, v = xf if xf else ((lambda p: (float(p[0]), float(p[1]))), (lambda d: (float(d[0]), float(d[1]))))
+    blk = [f(p) for p in [(3, 0), (60, 0), (60, 30), (0, 30), (0, 3)]]
+    front = [f((0, 0)), f((60, 0))]
+    if mirror:                                  # 鏡射 ⇒ 左右互換：p1 須仍為「左」（FRONT 之方向約定）
+        front = [front[1], front[0]]
+    cen = Polygon(blk).centroid.coords[0]
+    return ns["_build_corner_range_v3"](
+        blk, cen, front, [f((0, 30)), f((60, 30))], [f((0, 0)), f((0, 30))], v((0, 1)), 30.0, 0.0, 3.5,
+        Polygon([f((0, 0)), f((3, 0)), f((0, 3))]), dxf_quantum=0.0001, _label="BA",
+        _side=("right" if mirror else "left"), min_build_area=mba)
+
+
+def _end(ns, mba, xf=None, mirror=False):
+    import numpy as np
+    from shapely.geometry import Polygon
+    f, v = xf if xf else ((lambda p: (float(p[0]), float(p[1]))), (lambda d: (float(d[0]), float(d[1]))))
+    poly = Polygon([f(p) for p in [(10, 0), (70, 0), (70, 30), (0, 30)]])
+    A = np.asarray
+    p1, p2 = A(f((10, 0))), A(f((70, 0)))
+    d = A(v((1, 0)))
+    ca = A(v((0, 1)))
+    ad = A((-ca[1], ca[0]))
+    if mirror:                                  # 鏡射之後左端在 p2 側 ⇒ 以右端量之（p1／p2 互換、d̂ 反向）
+        g = ns["end_block_side_geom"](poly, -d, p2, p1, ca, -ad, 3.5, "right", _label="BE", min_build_area=mba)
+    else:
+        g = ns["end_block_side_geom"](poly, d, p1, p2, ca, ad, 3.5, "left", _label="BE", min_build_area=mba)
+    return g
+
+
+def _inner_x(geom, xf_inv=None):
+    xs = [p[0] for p in geom.exterior.coords]
+    return xs
+
+
+def selftest(repo):
+    ns, _ = _harvest(repo)
+    need = ["_build_corner_range_v3", "end_block_side_geom", "end_block_band_width", "k980_range_touch_check",
+            "_end_band", "K980_AREA_TOL", "K980_TOUCH_TOL", "k980_mba"]
+    miss = [n for n in need if n not in ns]
+    if miss:
+        print(f"  🔴 受詞缺 {miss}")
+        print("⇒ 紅 ['受詞缺']；rc 1")
+        return 1
+    from shapely.geometry import Polygon, box
+    C = []
+
+    def run(fn):
+        try:
+            return ("ok", fn())
+        except RuntimeError as e:
+            return ("停", str(e))
+        except Exception as e:  # noqa: BLE001
+            return ("例外", f"{type(e).__name__}: {e}")
+
+    def area(r):
+        return round(float(r[1].area), 6) if r[0] == "ok" else r
+
+    def stopped(r, key=K6):
+        return r[0] == "停" and key in r[1]
+
+    c1 = run(lambda: _corner(ns, None))
+    base_wkb = c1[1].wkb if c1[0] == "ok" else None
+    C.append(("C1 未輸入 ⇒ 100.5", area(c1), 100.5))
+    for nm, m in (("C2 輸入 0 ⇒ 逐位同 C1", 0), ("C3 輸入 100 ⇒ 逐位同 C1", 100.0), ("C4 輸入恰 100.5 ⇒ 逐位同 C1", 100.5)):
+        r = run(lambda m=m: _corner(ns, m))
+        C.append((nm, (r[0] == "ok" and r[1].wkb == base_wkb), True))
+    c5 = run(lambda: _corner(ns, 150.0))
+    if c5[0] == "ok":
+        a5 = float(c5[1].area)
+        xs = sorted({round(p[0], 3) for p in c5[1].exterior.coords})
+        xm = max(p[0] for p in c5[1].exterior.coords)
+        par = {(round(p[0], 9), round(p[1], 6)) for p in c5[1].exterior.coords if abs(p[0] - xm) < 1e-3}
+        g5 = (150.0 <= a5 <= 150.01, abs(xm - 5.15) <= 0.001,
+              len(par) >= 2 and max(q[0] for q in par) - min(q[0] for q in par) < 1e-9,
+              bool(c1[0] == "ok" and c5[1].buffer(1e-9).contains(c1[1])))
+    else:
+        g5 = c5
+    C.append(("C5 輸入 150 ⇒ 面積∈[150,150.01]·遠側 x＝5.15·∥SIDE_LINE·含 C1", g5, (True, True, True, True)))
+    C.append(("C6 輸入 2000 ⇒ 停機（K-9-80 ⑥）", stopped(run(lambda: _corner(ns, 2000.0))), True))
+    C.append(("C7 輸入 −1 ⇒ 停機", run(lambda: _corner(ns, -1.0))[0], "停"))
+    xf = _xf(37.0, True, 301234.5, 2650987.25)
+    c8 = run(lambda: _corner(ns, 150.0, xf=xf, mirror=True))
+    C.append(("C8 C5 之旋轉 37°·鏡射·TWD97 ⇒ 面積同 C5", (c8[0] == "ok" and c5[0] == "ok"
+                                                    and abs(float(c8[1].area) - float(c5[1].area)) <= 1e-6), True))
+    def _obl(mba):
+        blk = [(3, 0), (60, 0), (60, 30), (6, 30), (0.6, 3)]
+        return ns["_build_corner_range_v3"](
+            blk, Polygon(blk).centroid.coords[0], [(0, 0), (60, 0)], [(6, 30), (60, 30)], [(0, 0), (6, 30)], (0, 1),
+            30.0, 0.0, 3.5, Polygon([(0, 0), (3, 0), (0.6, 3)]), dxf_quantum=0.0001, _label="BO", _side="left",
+            min_build_area=mba)
+    c9 = run(lambda: _obl(200.0))
+    if c9[0] == "ok":
+        _pts = list(c9[1].exterior.coords)
+        _xa = max(p[0] for p in _pts if abs(p[1]) < 1e-6)
+        _xb = max(p[0] for p in _pts if abs(p[1] - 30.0) < 1e-6)
+        g9 = (200.0 <= float(c9[1].area) <= 200.01, abs((_xb - _xa) - 6.0) <= 1e-6)
+    else:
+        g9 = c9
+    C.append(("C9 側街斜交（∦ 宗地分配線）輸入 200 ⇒ 面積∈[200,200.01]·遠側界線 ∥ SIDE_LINE（Δx＝6）", g9, (True, True)))
+    e1 = run(lambda: _end(ns, None))
+    if e1[0] == "ok":
+        g1 = (round(float(e1[1]["r_end_area"]), 6), round(float(e1[1]["buf"]), 6))
+    else:
+        g1 = e1
+    C.append(("E1 未輸入 ⇒ R_end 255·內側界 13.5（buf 3.5）", g1, (255.0, 3.5)))
+    e2 = run(lambda: _end(ns, 255.0))
+    C.append(("E2 輸入恰 255 ⇒ 逐位同 E1", (e2[0] == "ok" and e1[0] == "ok" and e2[1]["r_end"].wkb == e1[1]["r_end"].wkb), True))
+    e3 = run(lambda: _end(ns, 300.0))
+    if e3[0] == "ok":
+        a3 = float(e3[1]["r_end_area"])
+        g3 = (300.0 <= a3 <= 300.01, abs(float(e3[1]["buf"]) - 5.0) <= 0.001)
+    else:
+        g3 = e3
+    C.append(("E3 輸入 300 ⇒ R_end∈[300,300.01]·內側界 x＝15", g3, (True, True)))
+    C.append(("E4 輸入 2000 ⇒ 停機（K-9-80 ⑥）", stopped(run(lambda: _end(ns, 2000.0))), True))
+    e5 = run(lambda: _end(ns, 300.0, xf=xf, mirror=True))
+    C.append(("E5 E3 之旋轉·鏡射·TWD97 ⇒ R_end 同 E3", (e5[0] == "ok" and e3[0] == "ok"
+                                                and abs(float(e5[1]["r_end_area"]) - float(e3[1]["r_end_area"])) <= 1e-6), True))
+    bp = Polygon([(10, 0), (70, 0), (70, 30), (0, 30)])
+    frag = Polygon([(10, 0), (10, 30), (0, 30)])
+    import numpy as np
+    e6 = [run(lambda m=m: ns["_end_region_R"](bp, np.asarray((0.0, 1.0)), np.asarray((10.0, 0.0)), 3.5, frag,
+                                             _label="BE", min_build_area=m)) for m in (None, 0)]
+    e6b = run(lambda: ns["end_block_band_width"](bp, np.asarray((0.0, 1.0)), np.asarray((10.0, 0.0)), 3.5, frag, 0,
+                                                 _label="BE"))
+    C.append(("E6 _end_region_R 之未輸入與 0 ⇒ R_end 逐位同（255）；end_block_band_width 之 0 ⇒ 停機",
+              (all(x[0] == "ok" for x in e6) and e6[0][1][1].wkb == e6[1][1][1].wkb and round(e6[0][1][2], 6),
+               e6b[0]), (255.0, "停")))
+    chk = ns["k980_range_touch_check"]
+    a = box(0, 0, 10, 30)
+    C.append(("T1 距 0.02 ⇒ ⛔ 停", run(lambda: chk("BA", {"甲": a, "乙": box(10.02, 0, 20, 30)}))[0], "ok"))
+    # 距恰為 K980_TOUCH_TOL 之浮點值（0.01 − 0 ＝ 0.01·⛔ 以 10.01 − 10 之捨入）
+    C.append(("T2 距恰 0.01 ⇒ 停", stopped(run(lambda: chk("BA", {"甲": box(-10, 0, 0, 30), "乙": box(0.01, 0, 10, 30)}))),
+              True))
+    C.append(("T3 距 0.005 ⇒ 停", stopped(run(lambda: chk("BA", {"甲": a, "乙": box(10.005, 0, 20, 30)}))), True))
+    t4 = run(lambda: chk("BA", {"左側街角規定範圍": a, "右端末端塊範圍": box(9, 0, 20, 30)}))
+    C.append(("T4 重疊 ⇒ 停（訊息具二範圍之名）", (stopped(t4) and "左側街角規定範圍" in t4[1] and "右端末端塊範圍" in t4[1]), True))
+    C.append(("T5 唯一範圍或含 None ⇒ ⛔ 停", [run(lambda: chk("BA", {"甲": a}))[0],
+                                          run(lambda: chk("BA", {"甲": a, "乙": None}))[0]], ["ok", "ok"]))
+    C.append(("T6 三範圍而唯其中二者相接 ⇒ 停", stopped(run(lambda: chk("BA", {"甲": a, "乙": box(30, 0, 40, 30),
+                                                                    "丙": box(40.0, 0, 50, 30)}))), True))
+    mb = ns["k980_mba"]
+    L_, C_ = ns["K91_SS_MBA_BY_LABEL"], ns["K91_SS_MBA_BY_CATEGORY"]
+    C.append(("K1 有效值之序（K-9-1 ⑨）：街廓覆寫 → 分區底 → 0；session 無鍵或 None ⇒ 0",
+              [mb({L_: {"BA": 180.0}, C_: {"住宅區": 120.0}}, "BA", "住宅區"),
+               mb({L_: {"BB": 180.0}, C_: {"住宅區": 120.0}}, "BA", "住宅區"),
+               mb({L_: {"BA": 0}, C_: {"商業區": 120.0}}, "BA", "住宅區"), mb({}, "BA", "住宅區"), mb(None, "BA", "住宅區")],
+              [180.0, 120.0, 0.0, 0.0, 0.0]))
+    red = []
+    for name, got, exp in C:
+        ok = got == exp
+        print(("  ✅ " if ok else "  🔴 ") + name)
+        if not ok:
+            print(f"       得 {got!r}"[:700])
+            print(f"       期 {exp!r}"[:700])
+            red.append(name.split()[0])
+    base = {j for j, (_, g2, e2) in enumerate(C) if g2 != e2}
+    p0 = 0
+    for i in range(len(C)):
+        bad = {j for j, (_, g2, e2) in enumerate(C) if g2 != (("擾動", e2) if j == i else e2)}
+        if bad == base | {i}:
+            p0 += 1
+    ok0 = p0 == len(C)
+    print(("  ✅ " if ok0 else "  🔴 ") + f"P0 判式自驗 {p0}／{len(C)}")
+    if not ok0:
+        red.append("P0")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+# ───────────────────────── wiring ─────────────────────────
+
+def _git(repo, *a):
+    r = subprocess.run(["git", "-C", repo, *a], capture_output=True)
+    return r.stdout.decode("utf-8") if r.returncode == 0 else ""
+
+
+def _callee(n):
+    f = n.func
+    if isinstance(f, ast.Name):
+        return f.id
+    if isinstance(f, ast.Attribute):
+        return f.attr
+    if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant) and isinstance(f.slice.value, str):
+        return f.slice.value
+    return None
+
+
+def _calls(tree, name):
+    return [n for n in ast.walk(tree) if isinstance(n, ast.Call) and _callee(n) == name]
+
+
+def _kw(n, k):
+    return any(kw.arg == k for kw in n.keywords)
+
+
+def _fn_node(tree, name):
+    for n in tree.body:
+        if isinstance(n, ast.FunctionDef) and n.name == name:
+            return n
+    return None
+
+
+def _top(src):
+    out = {}
+    for n in ast.parse(src).body:
+        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
+            out[n.name] = ast.dump(n)
+        elif isinstance(n, ast.Assign):
+            for t in n.targets:
+                if isinstance(t, ast.Name):
+                    out[t.id] = ast.dump(n)
+    return out
+
+
+def wiring(repo, base):
+    print(f"── 接線（工作樹對基準 {base}）──")
+    red = []
+    srcs = {}
+    for p in ("app.py", "verify/stepg_pipeline.py", "verify/run_verification.py", "verify/selection_pipeline.py"):
+        try:
+            srcs[p] = open(os.path.join(repo, p), encoding="utf-8").read()
+        except Exception as e:  # noqa: BLE001
+            print(f"  ⚠️ {p} 讀不到：{type(e).__name__}")
+            print("⇒ rc 3（無從判定）")
+            return 3
+    old = _git(repo, "show", f"{base}:app.py")
+    if not old:
+        print("  ⚠️ 基準之 app.py 取不到")
+        print("⇒ rc 3（無從判定）")
+        return 3
+    trees = {p: ast.parse(s) for p, s in srcs.items()}
+    three = ("app.py", "verify/stepg_pipeline.py", "verify/run_verification.py")
+    w1 = [(p, n.lineno, _kw(n, "min_build_area")) for p in three for n in _calls(trees[p], "_build_corner_range_v3")]
+    ok1 = len(w1) >= 4 and all(x[2] for x in w1)
+    print(("  ✅" if ok1 else "  🔴") + f" W1 _build_corner_range_v3 之呼叫 {len(w1)}（期 ≥ 4）皆傳 min_build_area："
+          f"{[x[:2] for x in w1 if not x[2]] or '皆傳'}")
+    if not ok1:
+        red.append("W1")
+    w2 = {nm: [(p, n.lineno, _kw(n, "min_build_area")) for p in three for n in _calls(trees[p], nm)]
+          for nm in ("end_block_side_geom", "end_block_host", "_place_pool_parcels")}
+    ok2 = (len(w2["end_block_side_geom"]) >= 1 and len(w2["end_block_host"]) >= 2 and len(w2["_place_pool_parcels"]) >= 2
+           and all(x[2] for v in w2.values() for x in v))
+    print(("  ✅" if ok2 else "  🔴") + f" W2 諸呼叫之數 {[(k, len(v)) for k, v in w2.items()]}（期 ≥ 1、≥ 2、≥ 2）皆傳 "
+          f"min_build_area：{[(k, x[:2]) for k, v in w2.items() for x in v if not x[2]] or '皆傳'}")
+    if not ok2:
+        red.append("W2")
+    ta = trees["app.py"]
+    ppp, erR = _fn_node(ta, "_place_pool_parcels"), _fn_node(ta, "_end_region_R")
+    w3 = {"_place_pool_parcels→_end_region_R": len(_calls(ppp, "_end_region_R")) if ppp else -1,
+          "_place_pool_parcels→_end_band": len(_calls(ppp, "_end_band")) if ppp else -1,
+          "_end_region_R→end_block_band_width": len(_calls(erR, "end_block_band_width")) if erR else -1,
+          "end_block_band_width 之呼叫（全檔）": len(_calls(ta, "end_block_band_width"))}
+    ok3 = (w3["_place_pool_parcels→_end_region_R"] == 1 and w3["_place_pool_parcels→_end_band"] == 0
+           and w3["_end_region_R→end_block_band_width"] == 1 and w3["end_block_band_width 之呼叫（全檔）"] == 1)
+    print(("  ✅" if ok3 else "  🔴") + f" W3 末端帶之單一真相源 {w3}（期 1、0、1、1）")
+    if not ok3:
+        red.append("W3")
+    # W4 最小建築面積之源：生產呼叫之 `min_build_area=` 之值皆為 `k980_mba(…)`（或 v12 之 `_mba_pk`·其賦值為之）
+    vals, bad4 = [], []
+    for p in three:
+        for nm in ("_build_corner_range_v3", "end_block_host", "_place_pool_parcels"):
+            for n in _calls(trees[p], nm):
+                v = next((k.value for k in n.keywords if k.arg == "min_build_area"), None)
+                ok_ = (isinstance(v, ast.Call) and _callee(v) == "k980_mba") or (isinstance(v, ast.Name) and v.id == "_mba_pk")
+                vals.append((p, nm, n.lineno))
+                if not ok_:
+                    bad4.append((p, nm, n.lineno))
+    v12 = _fn_node(ta, "select_corner_lots_both_sides_v12")
+    asg = [n for n in ast.walk(v12) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_mba_pk"
+                                                                        for t in n.targets)] if v12 else []
+    asg_ok = sum(1 for n in asg if isinstance(n.value, ast.Call) and _callee(n.value) == "k980_mba") == 1 and \
+        all((isinstance(n.value, ast.Call) and _callee(n.value) == "k980_mba") or
+            (isinstance(n.value, ast.Constant) and n.value.value is None) for n in asg)
+    k91 = [(p, n.lineno) for p in three for n in _calls(trees[p], "k91_effective_min_build_area")
+           if _fn_node(trees[p], "k980_mba") is None or not (_fn_node(trees[p], "k980_mba").lineno <= n.lineno
+                                                              <= _fn_node(trees[p], "k980_mba").end_lineno)]
+    k91b = [(p, n.lineno) for p in three for n in _calls(ast.parse(_git(repo, "show", f"{base}:{p}") or "pass"),
+                                                          "k91_effective_min_build_area")]
+    lit_cat = [(p, n.lineno) for p in three for n in _calls(trees[p], "k980_mba")
+               if len(n.args) >= 3 and isinstance(n.args[2], ast.Constant)]
+    ok4 = len(vals) >= 8 and not bad4 and asg_ok and len(k91) == len(k91b) and not lit_cat
+    print(("  ✅" if ok4 else "  🔴") + f" W4 min_build_area 之值皆為 k980_mba（呼叫 {len(vals)}·期 ≥ 8·不合 {bad4}）、v12 之 _mba_pk "
+          f"之賦值 {asg_ok}、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（{len(k91)}／基準 {len(k91b)}）、"
+          f"k980_mba 之分區之引數為字面者 {lit_cat}（期無）")
+    if not ok4:
+        red.append("W4")
+    w5 = []
+    for fname in ("select_corner_lots_both_sides_v12", "f3_screen_stepg_run"):
+        fn = _fn_node(ta, fname)
+        w5.append((fname, len(_calls(fn, "k980_range_touch_check")) if fn else -1))
+    tot5 = len(_calls(ta, "k980_range_touch_check"))
+    sgh = _fn_node(trees["verify/stepg_pipeline.py"], "_run_step_g_impl")
+    w5.append(("stepg:_run_step_g_impl", len(_calls(sgh, "k980_range_touch_check")) if sgh else -1))
+    K4 = {"左側街角規定範圍", "右側街角規定範圍", "左端末端塊範圍", "右端末端塊範圍"}
+    keys5 = []
+    for fn, need in ((_fn_node(ta, "select_corner_lots_both_sides_v12"), K4 - {"左端末端塊範圍", "右端末端塊範圍"}),
+                     (_fn_node(ta, "f3_screen_stepg_run"), K4), (sgh, K4)):
+        for n in (_calls(fn, "k980_range_touch_check") if fn else []):
+            d = n.args[1] if len(n.args) >= 2 else None
+            got = {k.value for k in d.keys if isinstance(k, ast.Constant)} if isinstance(d, ast.Dict) else set()
+            keys5.append(got == need)
+    ok5 = all(c == 1 for _, c in w5) and tot5 == 2 and len(keys5) == 3 and all(keys5)
+    print(("  ✅" if ok5 else "  🔴") + f" W5 k980_range_touch_check 之呼叫 {w5}·app.py 全檔 {tot5}（期各 1·app.py 全 2）、"
+          f"其範圍之名齊全 {keys5}（期三真）")
+    if not ok5:
+        red.append("W5")
+    tn, tb = _top(srcs["app.py"]), _top(old)
+    add, rem = set(tn) - set(tb), set(tb) - set(tn)
+    ok6 = add == NEW_TOP and not rem
+    print(("  ✅" if ok6 else "  🔴") + f" W6 頂層之名之增 {sorted(add)}（期 {sorted(NEW_TOP)}）、減 {sorted(rem)}")
+    if not ok6:
+        red.append("W6")
+    chg = sorted(k for k in tn if tn.get(k) != tb.get(k))
+    lits = []
+    for n in ta.body:
+        nm = getattr(n, "name", None) or (n.targets[0].id if isinstance(n, ast.Assign)
+                                          and isinstance(n.targets[0], ast.Name) else None)
+        if nm in chg:
+            seg = ast.get_source_segment(srcs["app.py"], n) or ""
+            segb = ""
+            ob = _fn_node(ast.parse(old), nm)
+            if ob is not None:
+                segb = ast.get_source_segment(old, ob) or ""
+            newc = {c.value for c in ast.walk(n) if isinstance(c, ast.Constant) and isinstance(c.value, str)
+                    and CASE_LIT_RE.match(c.value)}
+            oldc = {c.value for c in ast.walk(ob) if isinstance(c, ast.Constant) and isinstance(c.value, str)
+                    and CASE_LIT_RE.match(c.value)} if ob is not None else set()
+            lits += sorted((nm, x) for x in newc - oldc)
+    ok7 = not lits
+    print(("  ✅" if ok7 else "  🔴") + f" W7 新增或改之頂層節點（{len(chg)}）內新增之案件字面 {lits}")
+    if not ok7:
+        red.append("W7")
+    # W8 逐層照傳（`min_build_area=min_build_area`·⛔ 改傳 None 或他值）
+    w8 = []
+    for outer, inner in (("end_block_host", "end_block_apply"), ("end_block_apply", "end_block_side_geom"),
+                         ("end_block_side_geom", "_end_region_R"), ("_place_pool_parcels", "_end_region_R")):
+        fo = _fn_node(ta, outer)
+        cs = _calls(fo, inner) if fo else []
+        ok_ = len(cs) == 1 and any(k.arg == "min_build_area" and isinstance(k.value, ast.Name)
+                                   and k.value.id == "min_build_area" for k in cs[0].keywords)
+        w8.append((outer, inner, ok_))
+    ok8 = all(x[2] for x in w8)
+    print(("  ✅" if ok8 else "  🔴") + f" W8 逐層照傳 min_build_area {[(a, b) for a, b, o in w8 if not o] or '皆照傳'}")
+    if not ok8:
+        red.append("W8")
+    # W9 引擎經 ns 取之新名皆在 `_WF_NS_NAMES`（app 之七級調配之路·漏列即 KeyError）
+    wf = next((n.value for n in ta.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
+               and t.id == "_WF_NS_NAMES" for t in n.targets)), None)
+    wfn = {e.value for e in getattr(wf, "elts", []) if isinstance(e, ast.Constant)}
+    used = {n.slice.value for n in ast.walk(trees["verify/stepg_pipeline.py"]) if isinstance(n, ast.Subscript)
+            and isinstance(n.value, ast.Name) and n.value.id == "ns" and isinstance(n.slice, ast.Constant)
+            and n.slice.value in NEW_TOP}
+    ok9 = bool(used) and used <= wfn
+    print(("  ✅" if ok9 else "  🔴") + f" W9 引擎經 ns 取之新名 {sorted(used)} ⊆ _WF_NS_NAMES（漏 {sorted(used - wfn)}）")
+    if not ok9:
+        red.append("W9")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+# ───────────────────────── run ─────────────────────────
+
+def _one(ns, fst, sb, mba_by):
+    import run_verification as rv
+    import selection_pipeline as sp
+    from stepg_pipeline import run_step_g
+    import stepg_pipeline
+    out = {"err": None}
+    try:
+        with contextlib.redirect_stdout(io.StringIO()):
+            snap = rv.load_snapshot()
+            cb_by, cad = rv.build_pipeline(ns, fst, snap)
+            # 最小建築面積之輸入 ＝ session 之 `K91_SS_MBA_BY_LABEL`（畫面之同一鍵）；`None` ⇒ 去之（未輸入）
+            fst.session_state.pop(ns["K91_SS_MBA_BY_CATEGORY"], None)
+            if mba_by is None:
+                fst.session_state.pop(ns["K91_SS_MBA_BY_LABEL"], None)
+            else:
+                fst.session_state[ns["K91_SS_MBA_BY_LABEL"]] = dict(mba_by)
+            rv.build_ownership(ns, fst, rv.ANON_XLSX)
+            v6 = open(rv.V6DXF, "rb").read()
+            tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
+            params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
+            out["param"] = {(r["街廓"], s): r.get(f"【{c}】街角最小面積(㎡)") for r in params
+                            for s, c in (("left", "左"), ("right", "右")) if r.get(f"【{c}】街角最小面積(㎡)") is not None}
+            try:
+                res = sp.run_corner_pk(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
+                ra = fst.session_state.get("f3_corner_range_areas", {}) or {}
+                out["pk"] = {(b, s): v.get(s) for b, v in ra.items() for s in ("left", "right") if v.get(s) is not None}
+                ns["K917_DROPPED"].clear()
+                fst.session_state.pop(ns["SS_END_BLOCK_EVAL"], None)
+                sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, bp, res[3], res[4], sb,
+                                eff_min_build_by_blk={})
+                out["ctx"] = {k: round(float(v.area), 2) for k, v in (sg.get("corner_range_polys") or {}).items()
+                              if v is not None}
+                ev = fst.session_state.get(ns["SS_END_BLOCK_EVAL"]) or {}
+                out["rend"] = {(b, s): v.get("R_end(㎡)") for b, e in ev.items() for s, v in e.items() if v.get("觸發")}
+            except RuntimeError as e:
+                out["err"] = str(e).splitlines()[0][:300]
+    finally:
+        fst.session_state.pop(ns["K91_SS_MBA_BY_LABEL"], None)
+    return out
+
+
+def run(repo, sbs):
+    ns, fst = _harvest(repo)
+    if "end_block_band_width" not in ns:
+        print("  🔴 受詞缺")
+        print("⇒ 紅 ['受詞缺']；rc 1")
+        return 1
+    red = []
+    for sb in sbs:
+        try:
+            r0 = _one(ns, fst, sb, None)
+            ok1 = (r0["err"] is None and r0["param"] and all(abs(float(r0["param"][k]) - float(r0["pk"].get(k, -1))) <= 0.01
+                                                             for k in r0["param"])
+                   and all(abs(float(r0["param"][k]) - float(r0["ctx"].get(k, -1))) <= 0.01 for k in r0["param"]))
+            det1 = f"街角 {len(r0.get('param') or {})}·末端塊 {r0.get('rend')}·err {r0['err']}"
+        except Exception as e:  # noqa: BLE001
+            ok1, det1, r0 = False, f"例外 {type(e).__name__}：{str(e)[:200]}", None
+        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb} 未輸入：三源之街角範圍面積同（{det1}）")
+        if not ok1:
+            red.append(f"R1@{sb}")
+            continue
+        mx = {}
+        for (b, s), v in list(r0["param"].items()) + list((r0.get("rend") or {}).items()):
+            mx[b] = max(mx.get(b, 0.0), float(v))
+        mba = {b: round(v + 10.0, 2) for b, v in mx.items()}
+        try:
+            r2 = _one(ns, fst, sb, mba)
+            if r2["err"] is not None:
+                ok2 = False    # 輸入值 ＝ 最大範圍 ＋ 10 ㎡ ⇒ 本案⛔ 短街廓·任何停機皆不合
+                det2 = f"停機 {r2['err'][:160]}"
+            else:
+                bad = [(k, v, mba[k[0]]) for src in ("param", "pk", "ctx", "rend") for k, v in (r2.get(src) or {}).items()
+                       if not (mba[k[0]] - 1e-9 <= float(v) + 0.005 and float(v) <= mba[k[0]] + 0.01 + 0.005)]
+                ok2 = (not bad and set(r2["param"]) == set(r0["param"]) and set(r2["pk"]) == set(r0["param"])
+                       and set(r2["ctx"]) == set(r0["param"]) and set(r2.get("rend") or {}) == set(r0.get("rend") or {}))
+                det2 = f"輸入 {mba}·不合 {bad[:4]}"
+        except Exception as e:  # noqa: BLE001
+            ok2, det2 = False, f"例外 {type(e).__name__}：{str(e)[:200]}"
+        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb} 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（{det2}）")
+        if not ok2:
+            red.append(f"R2@{sb}")
+    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
+    return 1 if red else 0
+
+
+def main(argv):
+    if len(argv) < 3:
+        print(__doc__)
+        return 2
+    cmd, repo = argv[1], os.path.abspath(argv[2])
+    if cmd == "selftest":
+        return selftest(repo)
+    if cmd == "wiring":
+        if len(argv) != 4:
+            print("用法：wiring <repo> <基準 commit>")
+            return 2
+        return wiring(repo, argv[3])
+    if cmd == "run":
+        sys.path.insert(0, os.path.join(repo, "verify"))
+        os.chdir(repo)
+        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
+        return run(repo, sbs)
+    print(__doc__)
+    return 2
+
+
+if __name__ == "__main__":
+    sys.exit(main(sys.argv))
````

## 附錄乙　塊 `K37`（附於 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 之末·工項三）

````markdown

---

## 🔧 `W-G.9-391`：`K-9-80` ④⑤⑥ 與 `K-9-34` 之落地（有最小建築面積之輸入者，街角規定範圍與末端塊範圍擴至其面積；跨占之名單與門檻皆以擴大後之範圍；短街廓之二範圍相接或重疊 ⇒ 警示停止）；`K-9-80` ③ 之微差之吸收之再分（⛔ 上文一字不刪·純末端追加）

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`（`W-G.9-390` 入主線）之後；本節由 `W-G.9-391` 規格單（新側支 `verify/W-G.9-391-k980x`）入典，緊接上節（`W-G.9-390` 補令三之節）之後。**授權** ＝ `W-G.9-386` 之節之一之 KL 之逐字（自動化之委任）。本節⛔ 鑄 `K-9` 之號（`K-9-80`、`K-9-34` 之落地之讀法之登記）。

### 一、所據

`K-9-80` ④（「街角規定範圍 ＝ `K-9-34` …之重申；**末端塊範圍**（新）：`R_end` 之面積 ＜ 最小建築面積（有輸入者）⇒ 其往街廓內部之界線沿宗地分配線（地界線）之方向平行內移，至面積 ＝ 最小建築面積；末端塊無退縮。未輸入者 ⇒ 範圍⛔ 變」）、⑤（「跨占之名單與門檻皆以擴大後之範圍定之」）、⑥（「一街廓之二範圍（末端塊與末端塊、街角與末端塊、街角與街角）擴大後相接或重疊 ⇒ 比照前置地基檢查，警示並停止（⛔ 自動處理）」）；`K-9-34` ②（「否 ⇒ 依最小建築面積決定遠側界線（∥SIDELINE）…取範圍面積恰 ＝ 最小建築面積之位置」）。KL 之語見上節（`2026-10-20 22:30`／`22:55`）與 `K-9-34` 之節（`2026-09-17`）。

### 二、【工】之讀法（`W-G.9-391`·發單端·⛔ 充裁）

- **甲 最小建築面積之源**：某街廓之最小建築面積 ＝ 其有效值（`K-9-1` ⑨ 裁丙：街廓覆寫 → 分區底 → `0`；`0` ＝ 未輸入）；畫面與驗證程式（harness）皆取 session 之同一二鍵（街廓覆寫、分區底）——頂層之單一入口 `k980_mba`。harness 之二情境⛔ 輸入（待落地清單之序 `6`·`GB-202`）⇒ 本案之驗證之配地⛔ 變；畫面有輸入者，其範圍依本節擴之。harness 之逐宗驗證站（`_lot_gate`）之最小建築面積仍取 `run_step_g` 之參數（`eff_min_build_by_blk`·二情境為空）——二源於本案同為未輸入，其統一屬序 `6`。
- **乙 「＝ 最小建築面積」之量**：擴大後之範圍之面積 ∈ `[最小建築面積, 最小建築面積 ＋ 0.01 ㎡]`（同街角強制抵費地之帶之 `_corner_buffer_S` 之 `tol`；寧大勿小，使取得之宗之面積 ≥ 最小建築面積）；「面積已 ≥ 最小建築面積」之判容浮點之餘裕 `1e-6 ㎡`（⛔ 法定之量）。
- **丙 街角規定範圍之擴大**：平移後之 SIDELINE（`K-9-5-14` 之乙式之遠側界線）續沿前緣線之方向往街廓內平移（⇒ 仍 ∥ SIDELINE·`K-9-34` ②），範圍 ＝ 街廓之多邊形為其所切之街角側之片扣道路截角（同 `K-8` §五 之構造）；未輸入或面積已達 ⇒ 範圍逐位⛔ 變。
- **丁 末端塊範圍之擴大**：`R_end` ＝ 未臨正街 ∪ 末端帶；末端帶之內側界（∥ 宗地分配線）續往街廓內平移（帶寬自畸零地寬增之·末端塊無退縮）；未輸入或面積已達 ⇒ 帶寬 ＝ 畸零地寬（逐位⛔ 變）。末端保留（`_place_pool_parcels`）之帶與末端塊之評選之 `R_end` 同源。
- **戊 跨占之名單與門檻**（⑤）：街角 ＝ 街角選位之範圍（跨占、三指數之真交集之受詞）與參數表之街角最小面積（門檻、強制抵費地之面積之源·`K-9-32` ①）皆以擴大後之範圍；末端塊 ＝ 其評選之跨占與門檻（`G ≥ area(R_end)`）、強制抵費地（末）之範圍皆以擴大後之 `R_end`。
- **己 短街廓**（⑥）：一街廓之二範圍（擴大後）之距 ≤ `0.01 m`（法定粒度）⇒ 相接或重疊 ⇒ 停機（訊息含「K-9-80 ⑥」與二範圍之名）；範圍擴至街廓之他端（或全街廓）仍未達最小建築面積者亦同（其範圍必與他端相接）；未輸入（範圍⛔ 擴大）而二範圍本即相接或重疊者亦同（KL `22:55` 第 `5` 點「短街廓範圍相接或重疊時警示停止」之文⛔ 以擴大為限）。查之時點：街角與街角 ＝ 街角選位之二範圍建畢；末端塊與他範圍 ＝ 末端塊之評選（`end_block_host`）之後（畫面與 harness 同構）。⛔ 自動調整範圍、⛔ 擇一而續。
- **庚 `K-9-80` ① 之保證**：本節落地之後，有輸入者之街角與末端塊之「取得」（`G ≥` 擴大後之範圍之面積）即保證其面積 ≥ 最小建築面積（`K-9-1`「街角第 `1` 宗⛔ 豁免最小建築面積」⛔ 變·其豁免之實由範圍之構造代之）。
- **辛 `K-9-80` ③ 之微差之吸收之再分**（工程裁·唯序）：③ 之「其餘之重算之微差」之受詞須先查其源（本案之量：退縮 `3.5 m` 與 `0 m` 之 `R6` 右之街角之宗，取得時之試算 `G` `307.79 ㎡`、終態 `307.78 ㎡`；他之取得之宗之終態之 `G` 之異皆含同一地主之併入）——其源與二讀（取得時之面積鎖定而以調配池吸收、或終態依法定公式重算）之土地後果之異，於其單擬時列明，有二讀而土地後果相異者呈 KL；⛔ 入本節之落地。

### 三、本案之量

harness 之二情境⛔ 輸入最小建築面積 ⇒ 範圍逐位⛔ 變；短街廓之查⛔ 觸；`k6s3 cmp` 二退縮相異 `0`、`F8` 之落檔、`parity` 前後逐位同 ⇒ **本案之配地⛔ 變**（`W-G.9-391` 規格單 `§一` 項 `5`）。另以 session 之街廓覆寫輸入「各街廓之最小建築面積 ＝ 其未輸入時之最大範圍之面積 ＋ `10 ㎡`」實跑本案（`F35 run` 之 `R2`）：參數表、街角選位、Step-G 之三處之街角規定範圍之面積與末端塊之 `R_end` 皆 ＝ 其輸入值（`±0.01 ㎡`），⛔ 停機。

### 四、單之再分（工程裁·唯序·⛔ 涉土地後果）

`K-9-80` ③ 之微差之吸收 ⇒ `W-G.9-392`（先查其源·二之辛）；上節之四之諸單各順延一號：`K-9-61` ⑤ 與 `GB-205` ⇒ `W-G.9-393`；`K-9-60` ⇒ `W-G.9-394`；`K-9-59`、`K-9-63` ⇒ `W-G.9-395`。

### 五、`ops/queue` 之規則檔之登記

本節定稿時之值與上節之五逐位同（`README_自動化運作規則.md` `d775035e…`、`發單端.md` `69a1e952…`、`執行端.md` `ce550ab5…`、`每日摘要.md` `a24cd157…`、`ring.sh` `fef64a34…`、`本機模式.md` `ea16425b…`）——⛔ 變。

### 六、他案之形（泛用化）

| # | 形 | 處置 |
|---|---|---|
| `42` | 未輸入最小建築面積（有效值 `0`） | 範圍逐位⛔ 變（`F35` 之 `C1`、`C2`、`E1`、`E6`） |
| `43` | 有輸入而範圍之面積已 ≥ 之（含恰等） | 範圍逐位⛔ 變（`C3`、`C4`、`E2`） |
| `44` | 有輸入而範圍之面積 ＜ 之 | 擴至 `[最小建築面積, ＋0.01 ㎡]`（`C5`、`E3`） |
| `45` | 側街與宗地分配線斜交 | 街角之遠側界線仍 ∥ SIDELINE（`C9`） |
| `46` | 擴至街廓之他端（或全街廓）仍未達 | 停機（`K-9-80 ⑥`·`C6`、`E4`） |
| `47` | 一街廓之二範圍（街角與街角、街角與末端塊、末端塊與末端塊）擴大後相接或重疊 | 停機（`K-9-80 ⑥`·`T2`〜`T4`、`T6`）；距恰 `0.01 m` ⇒ 相接（`T2`）；距 ＞ `0.01 m` ⇒ 續（`T1`） |
| `48` | 換名、鏡射、旋轉、實座標之尺度 | 範圍之面積同（`C8`、`E5`） |
| `49` | 街廓覆寫與分區底並存、唯其一、皆無 | 依 `K-9-1` ⑨ 裁丙之序（`K1`） |
| `50` | 街角為強制抵費地 | 其面積與遠側地界線隨擴大後之範圍（`K-9-32` ①·參數表之街角最小面積） |
| `51` | 末端塊為強制抵費地 | 其範圍 ＝ 擴大後之 `R_end`（`K-9-36` ③⑤） |
| `52` | 畫面有輸入而 harness ⛔ 輸入 | 二者之範圍可異（待落地清單之序 `6`·`GB-202`）；本節⛔ 及其源之統一 |
| `53` | 舊七級調配引擎（`verify/wf_f4.py` 之 `_reshape_block`·UC9898 凍結）之末端之門檻與強制抵費地（末） | 仍讀未擴大之 `R_end`（本節⛔ 及·有輸入者與 Step-G 不一）——新調配模組（規格步 `5`〜`8`）以擴大後之範圍為受詞；舊引擎之處置留查（待落地清單序 `26`） |
| `54` | 畫面於街角選位之後改最小建築面積 | 跨占之名單（選位時）與門檻、末端塊範圍（當下）之輸入可異（⑤ 之受詞之一致）——其失效之機制留查（序 `26`·`main` 之最小建築面積之欄現⛔ 掛失效之鉤，其前提「本值不入 G 式」於本節之後已不成立） |
| `55` | 一側之範圍擴大而他端既非街角、亦非末端塊 | 範圍可擴至近街廓之他端（⛔ 二範圍 ⇒ ⑥ ⛔ 觸）；其餘地之處置（照配或停）⛔ 裁 ⇒ 留 `W-G.9-392` 擬單時列二讀、土地後果相異者呈 KL（序 `26`） |
| `56` | 街廓非凸而擴大後之範圍為多片 | 畫面之存（`f3_corner_range_polys` 唯存單片之外框）與 harness 之 ctx 不對稱（既有之形）；其二分之單調之設失之者停機（⛔ 靜默） |

### 七、落地狀態

`K-9-80` ④⑤⑥、`K-9-34` 🔶（新側支 `verify/W-G.9-391-k980x`·`W-G.9-391` 規格單·候入主線之短單）。`K-9-80` ③ 之微差之吸收 ⬜（`W-G.9-392`）；⑦ ⬜（調配模組）。`K-9-61` ⑤ ⬜（`W-G.9-393`）。
````

## 附錄丙　塊 `P48`（附於 `docs/待落地清單.md` 之末·工項三）

````markdown

---

## 🔧 待落地清單之更新：`W-G.9-390` 入主線；`K-9-80` ④⑤⑥ 與 `K-9-34` 之落地（新側支）；序 `22` 之再分（③ ⇒ `W-G.9-392`）；序之單號之順延

🔒 **態** ＝ 主線 `wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`（`W-G.9-390` 與其補令一〜四入主線）之後；本批之碼在新側支 `verify/W-G.9-391-k980x`。

| 序 | 裁／項 | 要旨 | 態 | 出處 |
|---|---|---|---|---|
| `7` | `K-9-80` ②（同上節） | 同上節 | ✅（主線 `a8657c4`） | `K-6` 典 `W-G.9-390` 補令三之節 |
| `21` | `K-9-50` 題一第 3 點之 KL 改裁（同上節） | 同上節 | ✅（主線 `a8657c4`） | `K-6` 典 `W-G.9-390` 補令二之節之三 |
| `22` | `K-9-80` ④⑤⑥ 與 `K-9-34`（上節之序 `22` 之一） | 有最小建築面積之輸入者，街角規定範圍（∥ SIDELINE）與末端塊範圍（沿宗地分配線內移）擴至其面積；跨占之名單與門檻皆以擴大後之範圍；一街廓之二範圍相接或重疊、或擴至他端仍未達 ⇒ 警示停止 | 🔶（新側支·候入主線之短單） | `K-6` 典 `W-G.9-391` 之節 |
| `25` | `K-9-80` ③（上節之序 `22` 之二） | 鎖定之宗之重算之微差之吸收：先查其源（本案 `R6` 右之街角之宗 `307.79` → `307.78 ㎡`），二讀而土地後果相異者呈 KL | ⬜ | 落地之單 `W-G.9-392`（`K-6` 典 `W-G.9-391` 之節之二之辛） |
| `19` | `K-9-61` ⑤、`GB-205`（同上節） | 同上節 | ⬜ | 落地之單 `W-G.9-393` |
| `8` | `K-9-60`（同上節） | 同上節 | ⬜ | 落地之單 `W-G.9-394` |
| `9` | `K-9-59`、`K-9-63`（同上節） | 同上節 | ⬜ | 落地之單 `W-G.9-395` |
| `26` | `W-G.9-391` 之唯讀審查之記而⛔ 改（`K-6` 典 `W-G.9-391` 之節之六 `53`〜`55`） | 舊七級調配引擎（`verify/wf_f4.py`）之 `R_end` 未擴大；畫面於選位後改最小建築面積之失效；一側之範圍擴至近他端之餘地之處置（⛔ 裁 ⇒ 列二讀呈 KL） | ⬜（候查·`55` 與序 `25` 同單呈 KL） | `K-6` 典 `W-G.9-391` 之節之六 |

🔒 **前節之更新**（上節·⛔ 追改其一字）：其序 `7`、`21` ⇒ 本表序 `7`、`21`（✅·`W-G.9-390` 入主線）；其序 `22` ⇒ 本表序 `22`（④⑤⑥ 與 `K-9-34`·`W-G.9-391`）與序 `25`（③·`W-G.9-392`）；其序 `19`、`8`、`9` 之單號各順延一；其餘各序（含 `20`、`23`、`24`）之態、出處⛔ 變。本表序 `25`、`26` 為新。
🔒 **本案之量**：本批⛔ 變配地（harness ⛔ 輸入最小建築面積·`W-G.9-391` 規格單 `§一` 項 `5`）。
🔒 **依賴序**：序 `22`（入主線之短單）→ 序 `25`（`W-G.9-392`）→ 序 `19`（`W-G.9-393`）→ 序 `8`（`W-G.9-394`）→ 序 `9`（`W-G.9-395`）→ 序 `3` → 規格步 `5`〜`8`（含序 `20`、`23`）；序 `26` 之 `55` 併序 `25`（`W-G.9-392`）呈 KL；序 `24`、`26` 之餘與序 `4`、`6`、`10`〜`15`、`17`、`18` 另單（⛔ 急）。先後之定 ＝ 發單端（KL `2026-10-17 12:40`）。
````

## 附錄丁　示範街廓（改前、改後並列·`F35 selftest` 之玩具·非本案）

> 供監看窗與 KL 一眼看出土地之變。範圍之面積 ＝ `F35 selftest` 之實算（原型）；各宗之試算 `G` 為示意之給定值（其當選與否依既有之規則：街角 ＝ 達門檻者之中依三指數擇之；末端塊 ＝ 依原投影序第一個 `G ≥ area(R_end)` 者）。本案⛔ 輸入最小建築面積 ⇒ 本案之配地⛔ 變。

**一、街角（玩具 `BA`：寬 `60 m`、深 `30 m`、左側街、截角 `4.5 ㎡`、畸零地寬 `3.5 m`、退縮 `0`）**

| 項 | 改前（或未輸入最小建築面積） | 改後（最小建築面積 ＝ `150 ㎡`） |
|---|---|---|
| 街角規定範圍 | 遠側界線距側街 `3.5 m`；面積 `100.50 ㎡` | 遠側界線續 ∥ 側街平移至距側街 `5.15 m`；面積 `150.00`〜`150.01 ㎡` |
| 跨占之名單 | 重劃前位置與 `100.50 ㎡` 之範圍重疊者 | 與擴大後之範圍重疊者（名單或增） |
| 門檻（候選之 `G` 須 ≥） | `100.50 ㎡` | `150.00 ㎡`（取其擴大後之實面積） |
| 候選 甲（`G` `130 ㎡`·三指數最高） | 達 ⇒ **當選**（街角地 `130 ㎡`） | ⛔ 達（`130 ＜ 150`）⇒ 依原投影序續排 |
| 候選 乙（`G` `160 ㎡`） | 達而未當選 ⇒ 依原投影序續排 | 達 ⇒ **當選**（街角地 `160 ㎡`） |
| 皆⛔ 達之時 | 強制抵費地 `100.50 ㎡` | 強制抵費地 `150.00 ㎡`（其遠側地界線 ＝ 擴大後之範圍之遠側界線·`K-9-32` ①） |

**二、末端塊（玩具 `BE`：正面 `60 m`、左端之未臨正街之三角形 `150 ㎡`、深 `30 m`、畸零地寬 `3.5 m`）**

| 項 | 改前（或未輸入） | 改後（最小建築面積 ＝ `300 ㎡`） |
|---|---|---|
| 末端塊範圍 `R_end` | 未臨正街 `150` ＋ 末端帶（寬 `3.5 m`）`105` ＝ `255.00 ㎡` | 末端帶之內側界沿宗地分配線內移至寬 `5.0 m`：`300.00`〜`300.01 ㎡`（末端塊無退縮） |
| 候選 丙（原投影序第 `1`·`G` `280 ㎡`） | 達（`280 ≥ 255`）⇒ **當選**（末端塊 `280 ㎡`） | ⛔ 達（`280 ＜ 300`）⇒ 自末端塊之後一宗起依原投影序排 |
| 候選 丁（原投影序第 `2`·`G` `320 ㎡`） | 依原投影序排於丙之後 | 達 ⇒ **當選**（末端塊 `320 ㎡`） |
| 皆⛔ 達之時 | 強制抵費地（末）`255 ㎡`（得作調配池） | 強制抵費地（末）`300 ㎡`（得作調配池·進入者之 `G` 須 ≥ `300`） |

**三、短街廓（`K-9-80` ⑥）**

| 形 | 改前（未輸入） | 改後（有輸入·擴大後） |
|---|---|---|
| 二範圍之距 `0.02 m` | 照常配地 | 照常配地（`T1`） |
| 二範圍之距恰 `0.01 m`、`0.005 m`、或重疊 | 舊碼⛔ 查（續配·其果未定） | **警示停止**（未輸入而範圍本即相接或重疊者亦同）：「K-9-80 ⑥ 短街廓……相接或重疊……請重新檢視街廓之劃設或最小建築面積之輸入」（`T2`〜`T4`、`T6`） |
| 範圍擴至街廓之他端仍未達（玩具 `BA` 輸入 `2000 ㎡`、`BE` 輸入 `2000 ㎡`） | — | **警示停止**（`C6`、`E4`） |

**四、換名、鏡射、旋轉**：`BA`／`BE` 旋轉 `37°`、左右鏡射並移至 TWD97 之尺度（約 `301234`, `2650987`）⇒ 擴大後之面積同上（差 ≤ `1e-6 ㎡`·`C8`、`E5`）。側街與宗地分配線斜交（側街 `(0,0)→(6,30)`）⇒ 擴大後之遠側界線仍 ∥ 側街（`C9`）。

SELF_SHA256: afb401e32d1b386414d6d862788a9462f06a42838310a02e1dd5378961df4347
