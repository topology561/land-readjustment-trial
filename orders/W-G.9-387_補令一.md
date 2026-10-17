# `W-G.9-387` 補令一：原單工項四（執行報告入倉）之補 ＋ 主線快轉（`34736ab` → 本補令工項一″ 之 `commit`·`W-G.9-387`〔`K-9-61` ⑧ 之落地〕入主線）

> **本補令建議等級 ＝ `medium`**（⛔ 撰生產碼、⛔ 動 `verify/` 之一字；受詞 ＝ 本補令與報告二新檔之入側支、主線之快轉）。
> **發單** ＝ 發單端（發單側·自動輪）·`2026-10-17`。**受單** ＝ 執行端（雲端之排程「市地重劃·執行端」·其施工樹 ＝ 雲端之完整複本）。
> **所補** ＝ `docs/orders/W-G.9-387_規格單.md`（「原單」）之工項四（執行報告入倉·原趟未做）與 `§四-2`（入主線之短單）。原單留倉、⛔ 改一字。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`；側支 `verify/W-G.9-387-k961h` ＝ `6dae569e97b3f58ba4a6128783c9eaaf26a38bba`（原單工項三·KL 本機之 Claude Code 代行）；遠端 heads **`47`**。
> **級** ＝ **中**（⛔ 跑 `run_all`——快轉後主線之生產碼 `34` 檔 ≡ 側支之 `d2c4f65`；發單端已於拋棄式 worktree 自倉重跑原單之 `V-1`〜`V-9` 之 `64` 呼叫與收工閘〔`§一″` 項 `2`〕；本補令之收工閘唯跑量測器之 `selftest`／`wiring`）。
> 🔑 **通則** ＝ 原單之通則照舊（`ops/queue` 之 README 第六節·雲端 Linux：直譯器 `python3`；`<repo>` 及一切路徑引數為正斜線之絕對路徑；`<O>` ＝ 執行端自定之倉外輸出目錄；`commit` 訊息一律 `git commit -F`；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；Bash 命令⛔ 含 heredoc；量測之殼⛔ 設五旗標〔原單單首 🔑〕；並行 ≤ `2`）。
> 🔑 **`commit` 訊息之書法**（`自誤 604`）：各工項所令之訊息為**首列**，逐字；其後空一列，附受單側之環境所附之尾列；⛔ 他列。
> 🔑 **來源檔** ＝ `ops/queue` 之 `orders/W-G.9-387_補令一.md`；其 bytes／`sha256` ＝ 同分支之 `STATE.json` 之 `order_bytes`／`order_sha256`。執行端一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **撇號**：「″」＝ U+2033。本補令之款號、工項號、閘號唯指本補令之條。
> 🔒 **⛔ 寫 `CLAUDE.md`**（KL `2026-10-17 22:42` 同意·無人值守之輪之寫入為雲端之分類器所拒）：本補令⛔ 令寫 `CLAUDE.md`、`K-6` 典或任何帳本。
> 🛑 **本補令⛔ 及於**：生產碼、`verify/` 之一字、任何錨；`GB` 簿、`VR` 簿、`K-6` 典、自誤簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 之一字；側支 `verify/W-G.9-387-k961h` 之刪除或改寫（保留為歷史）；任何他側支；`ops/queue` 除 `執行端.md` 所許外之一字。
> 🔴 **本補令⛔ 令執行端作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零″`　開場（**先於工項零″**·⛔ 跳序）

1. 自報 context 餘量與 `nproc`。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`；`git rev-parse origin/verify/W-G.9-387-k961h` ＝ `6dae569e97b3f58ba4a6128783c9eaaf26a38bba`；`git ls-remote --heads origin` 之列數 ＝ **`47`**（全列存 `<O>/heads_before_387p1.txt`·收工閘 `5″` 用）；施工樹 `git checkout --detach origin/verify/W-G.9-387-k961h` 後 `git status --porcelain --untracked-files=no` ＝ 空；量測之殼之旗標之出艙 ＝ `[None, None, None, None, None]`（原單單首 🔑 之命令）。
3. 於施工樹：`python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑（檔·非目錄）> 623 622` ⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 相異 `608`／`MAX` `623`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（發單端於 `6dae569` 實跑同）。
4. 本補令之 bytes／`sha256` 對拍 `STATE.json` 之 `order_bytes`／`order_sha256`；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）。
5. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` ⇒ `rc 0`（不然者依 README 第六節第 2 款裝之後再驗）。
6. `python3 verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單端實跑之出艙見 `§五″` 項 `3`）。

### `§零-1″`　停機款

| # | 款 |
|---|---|
| `1″` | 開工時主線 ≠ `34736ab`，或側支 ≠ `6dae569`，或遠端 heads ≠ `47`，或施工樹之追蹤檔有變動，或 `§零″` 項 `3` 之 `rc` 或四簿之值 ≠ 期，或旗標之出艙 ≠ 期，或項 `5` 之環境於安裝後仍不能匯入 |
| `2″` | 本補令之 `SELF_SHA256` 自驗不符；或 `STATE.json` 所載之 bytes／`sha256` 與本補令不符；或入倉後 `git cat-file blob` 與來源不逐位相同 |
| `3″` | 工項一″ 之重量（項 `3`）任一 ≠ 期；或差異檔之 blob ≠ `§五″` 項 `4` |
| `4″` | 工項二″ 前置之任一期不符 |
| `5″` | 工項二″ 之 `push` 被拒，或須 `--force`／`--force-with-lease` 方能成（⛔ 改目標、⛔ `--force`） |
| `6″` | 工項二″ 快轉後之出艙 ①〜④ 任一 ≠ 期 |
| `7″` | 工項零″、一″ 之任一 `push` 之目標非 `verify/W-G.9-387-k961h`；工項二″ 之 `push` 之目標非 `wip/s1-endpart` 或其值非工項一″ 之 `commit`；或推至他支 |
| `8″` | `§三-1″` 收工閘任一 ≠ 期 |
| `9″` | 執行端作任何「孰為正典」「應改為」之判，或改器、命令一字以求其過；或本批任一新檔為 `git check-ignore -v --no-index` 所命中 |
| `10″` | 存取倉庫被拒而依 README 第八節第 4 款附掛後仍不能；或任一寫入為環境之分類器所拒（⛔ 繞道·照實回報） |

停機 ⇒ 依 `執行端.md` 丙之第 5 步與丁；已推之 `commit` ⛔ 撤；工項二″ 未成者主線⛔ 動。

---

## `§一″`　所據

1. **原單之施作之實況**（發單端自倉讀·⛔ 採執行端之自報）：側支 `verify/W-G.9-387-k961h` 對主線 `34736ab` 唯四筆 `commit`（`git rev-list --count 34736ab..6dae569` ＝ `4`、反向 ＝ `0`、`--merges` 空）：`789cccb49e9a771add83b33dc91534f27875bbdd`（工項零·`979`／`0`）、`160c3f48608cdc2cd782dfeecdab0c370658ebd8`（工項一·五器 ＝ 原單 `§五-1` 項 `5`）、`d2c4f65da03f04130e1d125f1beee317a2d4c3fa`（工項二·`app.py` `12`／`7`·其 blob `efae3a5a4a918353b6db3e7d0dc61219a8741a82`·`1842945` B）、`6dae569e97b3f58ba4a6128783c9eaaf26a38bba`（工項三·`K-6` 典 `64`／`0`·`CLAUDE.md` `27`／`0`·二 blob ＝ 原單 `§五-1` 項 `5`·作者欄 `diag <diag@local>`——KL 本機之 Claude Code 代行·KL `2026-10-17 22:42` 同意·見 `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`）。四筆之首列 ＝ 原單所令逐字。逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判，命中者恰 `d2c4f65`（`app.py`）。**工項四未做**：原趟之執行端於工項三停機上呈（`CLAUDE.md` 之寫入為分類器所拒），其 `V-1`〜`V-9` 之出艙以倉外之附件交 KL、⛔ 入倉。
2. **發單端之獨立復驗**（`2026-10-17`·雲端 Linux `4` 核·倉外之拋棄式 worktree·殼無 `WV_`·Python `3.11.17`·`shapely 2.2.0`·⛔ 採執行端之自報）：
   - **差異之逐行讀**（`git diff 160c3f4 d2c4f65 -- app.py`·`+12`／`-7`·唯 `adj_intake`）對原單 `§三`：`R-1` 之四句（`_top`、`_cands`、並列之 `raise`、`_home = _cands[0]`）去之，代以 `_pre387`（每一池列之 `原有面積` 之和·⛔ 去重）、`_pid387`（池列之 `暫編地號` 之最小者·字串之比·其值皆由 `adj_intake` 以 `str(...)` 立）、`_home ＝ min((k967_rank(_v, _pre387[_b], _pid387[_b]), _b) for _b, _v in _basis.items())[1]`——`k967_rank` 直呼、`_basis` 之建（`_seen` 之去重）⛔ 動、`原街廓之據` 仍 ＝ `_basis`、⛔ 增 `raise`；`R-2` docstring 之「停機」去並列之款、增 `🔧 W-G.9-387` 之註；`R-3` 他處⛔ 動。頂層節點之名之集 ＝ 工項一之端（AST）、相異之節點 ＝ `{adj_intake}`；生產碼 `34` 檔對 `160c3f4` 相異恰 `app.py`；`verify/` 對 `160c3f4` 相異 `0`。`V-8` 之字樣：「之原街廓：應分配面積並列」施後 `rc 1`（施前 `app.py:1`）、「float(_r['原有面積'])」「float(_r['應分配面積'])」「if _pool or (_cm and not _al):」「if '段三併出' in t:」施後各 `app.py:1`。
   - **`64` 呼叫之重跑**（原單 `§五-1`「項 `8` 之表」之命令·於 `d2c4f65`）：後態（`d2c4f65`）之 `64` 呼叫 ＋ 前態（`160c3f4`·工項一之端）之 `9` 呼叫（`#31`、`#56`〜`#63`）＝ `73` 呼叫·並行 `2`·耗時之和 `10306` s：皆 `rc` ＝ 原單「項 `8` 之表」之同態之期、末列逐字同（`#56`／`#57` 之末列為 JSON 之摘要·⛔ 比）、`stderr` 合計 `0` B；後態之 `F31 selftest` `K1`〜`K18`、`F31 wiring` `X1`〜`X5`、`F31 run` `R1`〜`R3`（二退縮）皆 ✅（`G011` ⇒ `R3`、`G030` ⇒ `R3`〔`3.5 m`〕／`R2`〔`0 m`〕·合併單位 `17` 之原街廓 ＝ 外部錨）；前態之 `F31 selftest`／`F31 wiring`／`F10 selftest` 紅 ＝ 期（對照組·末列逐字 ＝ 原單 `§四-1` 工項二前置 `1`）；`P0` ＝ `75／75`（`F23`）、`74／74`（`F29`）、`35／35`（`F16`）、`31／31`（`F27`）、`29／29`（`F28`）。
   - **本案配地⛔ 變**：`k6s3 cmp`（前態 `160c3f4` 對後態 `d2c4f65`）二退縮皆 `rc 0`、末列 `相異 0 項 ⇒ ✅ 同`；`F8 run` 之落檔前後逐位同（`3.5 m` `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` `6fb86647807f9744594071be25c522b6b506c230`）；`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`，其落檔與 `stdout` 以同一字樣代 `HEAD` 之全值後前後逐位同（對照：⛔ 代之則異）。
   - **收工閘**（原單 `§四-3`·於 `6dae569`·工項四之報告二檔未入 ⇒ 閘 `1`／`3`／`5` 以其餘之受詞量之）：閘 `1` 之四筆之增刪 ＝ 期；閘 `2` 生產碼相異 `1`（`app.py`）、`verify/` 相異 `5`（`M` `4`·`A` `1`）、新檔之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`·`.gitignore:18:__pycache__/`）；閘 `3` 九檔之 blob `CR` 合計 `0`（`data/V6.dxf` `12308`）；閘 `4` `K-6` 典 `829153` → `837880`、`CLAUDE.md` `415049` → `419752`·改前皆改後之嚴格前綴·其尾 ＝ 塊 `K29`／`P40`（`8727` B `5ef03ee9…`／`4703` B `fecb444b…`）·`.claude/`、`docs/reports/` 對 `34736ab` 相異 `0`；閘 `6` `closegate 623 622 .` ⇒ `rc 0`（`✅ 二閘皆過`·判別力 `624 623` ⇒ `rc 7`）；閘 `7` `rc 0`·四簿之值 ＝ `§零″` 項 `3`；閘 `8` `checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`，`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·重生成之檔與倉內逐位同（塊 `CK` `1539` B `00cd3949…`、`GF` `2445` B `b11edb77…`）。
3. **快轉之受詞**：工項零″、一″ 推後之側支之端（工項一″ 之 `commit`）；其祖含 `34736ab` 與 `6dae569`；`34736ab..<工項一″>` 之 `commit` 數 ＝ `6`、`--merges` 空；生產碼之命中唯 `d2c4f65`（項 `1`）。

---

## `§二″`　授權與射程

🔒 **授權**（`ops/queue` 之 README 第一節·KL 逐字）：`2026-10-17 07:23` 第 `3` 點「……新的規格單和入主線也可以不用我過目……所以接下來除了域領域需通知我外，是否可以自動化處理本專案既有流程?」；`07:58`「1. 修正施作疏漏的補令，若是預期中的改變就不需要通知我 2. 除了上面1. 說明，其他上面的界線表均同意 3. 放雲端，並同意讓你取得 `land-readjustment-trial` 的推送權限」。本補令 ＝ 修正施作疏漏之補令（原單工項四之未做）＋ 入主線之短單（原單 `§四-2`）；原單之生產碼於本案之配地⛔ 變（`§一″` 項 `2`）⇒ README 第二節之自動處理第 `1`、`2` 款。**`expects_allocation_change` ＝ `false`**。

🔒 **KL `2026-10-17 22:42` 之同意**（發單側窗八十七所轉·見 `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md` 之三）：原單工項三由 KL 本機之 Claude Code 代行；往後無人值守之輪⛔ 寫 `CLAUDE.md`。

🛑 **射程**：`(a)` 工項零″、一″（零生產碼）推至側支 `verify/W-G.9-387-k961h`（快轉）；`(b)` 工項二″ 主線快轉至工項一″ 之 `commit`（**以前置皆符為條件**·⛔ `--force`）；`(c)` 回報依 `執行端.md` 丁推至 `ops/queue`，並於 `log.md` 之該列記「主線 `34736ab959e3d6915abf94bda3977063bf2711e5` → `<工項一″ 之全 40 碼>`」（README 第二節「入主線之安全」）；`(d)` 主 checkout 之同步省之（README 第六節第 6 款·KL 自為之）；`(e)` ⛔ 及生產碼、`verify/`、任何錨、帳本、`CLAUDE.md`、`.claude/`。

---

## `§三″`　工項（依序）

### 工項零″　本補令原封入倉（側支·零生產碼）

`docs/orders/W-G.9-387_補令一.md`（**新檔**·自來源二進位複製）。`git cat-file blob HEAD:docs/orders/W-G.9-387_補令一.md` 與來源逐位同（停機款 `2″`）。`commit` 訊息之首列逐字 `W-G.9-387 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`（快轉）。

### 工項一″　執行報告入倉（原單工項四之補·側支·零生產碼·一 `commit`）

1. **差異檔**：`git diff --no-color --no-ext-diff 160c3f48608cdc2cd782dfeecdab0c370658ebd8 d2c4f65da03f04130e1d125f1beee317a2d4c3fa -- app.py` 之 `stdout` 以二進位寫為 `docs/reports/W-G.9-387R_K-9-61之八之落地_app差異.diff`（新檔）；其 `git hash-object` ＝ `§五″` 項 `4`（停機款 `3″`）。
2. **檢索之重跑**：依原單工項三之 `2`〜`4`（塊 `CK`／`GF` 自 `docs/orders/W-G.9-365_輕量單.md` 抽出·對拍原單 `§五-1` 項 `7`）於側支之端重跑 `checkidx`、`gen_fa_index` ⇒ 期 ＝ 原單之同項（`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`則 124；加註節 14；列 158`·重生成之檔與倉內逐位同）。
3. **重量**（出艙存 `<O>`·⛔ `commit`）：
   - 甲、於施工樹（側支之端）：`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`、`… wiring <repo> 34736ab`、`python3 verify/probes/probe_WG9351_intake.py selftest <repo>` ⇒ 皆 `rc 0`、末列逐字 `⇒ 紅 []；rc 0`、`stderr` `0` B。
   - 乙、判別力［必紅］：`git worktree add --detach <S> 160c3f48608cdc2cd782dfeecdab0c370658ebd8`（拋棄式·`<S>` 在任何 git 工作樹之外）；於 `<S>` 以 `<repo>` ＝ `<S>` 重跑甲之三呼叫 ⇒ 皆 `rc 1`、末列逐字 ＝ 原單 `§四-1` 工項二前置 `1` 之三列（`⇒ 紅 ['K2', 'K3', 'K5', 'K8', 'K9', 'K10', 'K11', 'K13', 'K15', 'K16', 'K17', 'K18']；rc 1`；`⇒ 紅 ['X1', 'X2']；rc 1`；`⇒ 紅 ['S6 應分配面積並列 ⇒ 重劃前面積較大者']；rc 1`）；其後 `git worktree remove --force <S>`。
   - 丙、`git grep -c -F "<字樣>" d2c4f65da03f04130e1d125f1beee317a2d4c3fa -- app.py` 與同式於 `160c3f48608cdc2cd782dfeecdab0c370658ebd8`，逐一於原單 `V-8` 之五字樣 ⇒ ＝ `§一″` 項 `2` 之值。
4. **報告**（新檔 `docs/reports/W-G.9-387R_K-9-61之八之落地_執行報告.md`）須載：① 原單之工項零〜三之 `commit`（全 `40` 碼·首列·作者欄）與本補令之工項零″ 之 `commit`；② 原單之停機之事由與工項三之代行（引 `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`·載其於本輪取得時之 `git hash-object`）——原趟之 `V-1`〜`V-9` 之出艙在倉外之附件、⛔ 入倉，本報告⛔ 重述其數；發單端之獨立重跑見本補令 `§一″` 項 `2`（隨工項零″ 入倉）；③ 本補令 `§零″` 之出艙與停機款 `1″`〜`10″` 之三值（款·期·實·唯工項一″ 之 `commit` 前可量者）；④ 上開 `2`、`3` 之全部出艙；⑤ 原單 `§三-5` 之設計說明——依差異檔逐條（`R-1`〜`R-3`）載其落處與字樣，並註「撰碼者 ＝ 原趟之執行端」；⑥ 二簿（`K-6` 典、`CLAUDE.md`）之改前改後之 bytes／blob（`34736ab`／`6dae569`）；⑦ pre-flight 之出艙與逐項之處置；⑧ 執行端之自捕與自解；⑨ 各段耗時（並行之數）。工項二″ 之出艙與收工閘之實值於回報（⛔ 寫入本檔·自指）。
5. `commit`（二新檔·唯此二檔）訊息之首列逐字 `W-G.9-387 補令一 工項一″：執行報告入倉（原單工項四之補·側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-387-k961h`（快轉）。

### 工項二″　主線快轉（🛑 ⛔ `--force`·⛔ `commit`）

**前置**（⛔ `commit`·出艙一律存 `<O>`）：令 `<C>` ＝ 工項一″ 之 `commit` 之全 `40` 碼（`git rev-parse HEAD`）。
1. `git fetch origin`；`git rev-parse origin/verify/W-G.9-387-k961h` ＝ `<C>`；`git rev-parse origin/wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`。
2. `git merge-base --is-ancestor 34736ab959e3d6915abf94bda3977063bf2711e5 <C>` ⇒ `rc 0`；`git rev-list --count 34736ab..<C>` ＝ `6`；`git rev-list --count <C>..34736ab` ＝ `0`；`git rev-list --merges 34736ab..<C>` ＝ 空。
3. `git rev-list 34736ab..<C>` 逐筆以 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"` 判（🔒 `:(glob)` ⛔ 省）：命中 ≥ `1` 列者恰 `1` 筆 ＝ `d2c4f65da03f04130e1d125f1beee317a2d4c3fa`（命中 `1` 列 `app.py`）；逐筆之出艙（含空輸出）存 `<O>`。
4. `git rev-parse <C>:app.py` ＝ `efae3a5a4a918353b6db3e7d0dc61219a8741a82`；`git diff --name-only d2c4f65da03f04130e1d125f1beee317a2d4c3fa <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。

任一 ≠ 期 ⇒ 停機款 `4″`·⛔ 快轉。

**快轉**（前置皆符後·與前置為分開之呼叫）：`git push origin <C>:refs/heads/wip/s1-endpart`（`<C>` 以全 `40` 碼書之）。🛑 ⛔ `--force`／`--force-with-lease`（被拒 ⇒ 停機款 `5″`）；⛔ 刪側支 `verify/W-G.9-387-k961h`（保留為歷史）。

🔒 **快轉後即出艙**（停機款 `6″`）：① `git ls-remote origin refs/heads/wip/s1-endpart` 全 `40` 碼 ＝ `<C>`；② 遠端 heads ＝ **`47`**（⛔ 增減）；③ 生產碼 `34` 檔於新主線 vs `d2c4f65` 之相異 ＝ **`0`**；判別力［必非零］：vs `34736ab` 之相異 ＝ **`1`**（`app.py`）；④ `git branch -r --contains d2c4f65da03f04130e1d125f1beee317a2d4c3fa` 含 `origin/wip/s1-endpart`（快轉前唯 `origin/verify/W-G.9-387-k961h`）。

---

## `§三-1″`　收工閘（工項二″ 之後·於主線之端〔＝ `<C>`〕量）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1″` | 本批二筆 `commit`（工項零″、一″）之增刪（`git show --numstat`） | 工項零″ ＝ 本補令之增（`132`）／`0`；工項一″ ＝ 報告二檔之增（差異檔 `44`／`0`）·唯此二檔；二筆之首列 ＝ `§三″` 所令逐字 |
| `2″` | `git diff --name-status 6dae569 HEAD`；生產碼 `34` 檔與 `verify/` | 恰 **`3`** 列：`A` 本補令、`A` 報告、`A` 差異檔；生產碼與 `verify/` 之一切檔對 `6dae569` 相異 **`0`**；判別力［必非零］：生產碼對 `34736ab` 相異 **`1`**（`app.py`）；三新檔之 `git check-ignore -v --no-index` 皆無命中（判別力［必非零］：同命令對 `verify/__pycache__/x.pyc` ⇒ `rc 0`·命中 `.gitignore:18:__pycache__/`） |
| `3″` | 三新檔之 `CR`（主線之端之 blob·Python 計位元組·判別力：`data/V6.dxf` ＝ `12308`） | 合計 **`0`** |
| `4″` | 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` | 對 `6dae569` 相異 **`0`**（`git rev-parse HEAD:CLAUDE.md` ＝ `66e9c07af114da5cbe3eaff30c78008540c2836f`；`K-6` 典 ＝ `a880ba93f826ad3ce3bf79c4dfe910fd16c43b0c`） |
| `5″` | 自限 | 遠端 heads **`47`**；主線 ＝ `<C>`；側支 `verify/W-G.9-387-k961h` ＝ `<C>`；其餘 `45` 列中除 `ops/queue`（回報後可變）外之 `44` 列逐列 ＝ `<O>/heads_before_387p1.txt` 之同列 |
| `6″` | `python3 verify/probes/probe_WG9270_closegate.py 623 622 .` | **`rc 0`**（末列 `✅ 二閘皆過`）；判別力：`… 624 623 .` ⇒ `rc 7` |
| `7″` | `python3 verify/probes/probe_WG9321_issuer_anchor.py <repo 絕對路徑> <輸出檔之絕對路徑> 623 622` | **`rc 0`**；其「項4′ 四簿·正典框」＝ `§零″` 項 `3` 之值（⛔ 變） |
| `8″` | 量測器（於主線之端·`13` 呼叫）：`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`；`… wiring <repo> 158f7fe`；`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`；`… wiring <repo> 7d8e954`；`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`；`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`；`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`；`python3 verify/probes/probe_WG9357_k948.py selftest <repo>`；`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`；`python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>`；`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`；`… wiring <repo> 34736ab`；`python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | 皆 **`rc 0`**；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0` ＝ `75／75`（`F23`）、`35／35`（`F16`）、`74／74`（`F29`）、`31／31`（`F27`）、`29／29`（`F28`）；`F31 selftest` `K1`〜`K18`、`F31 wiring` `X1`〜`X5` 皆 ✅ |

---

## `§四″`　土地後果

**本案**：配地⛔ 變（`§一″` 項 `2`·`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔逐位同、`parity` 不符 `0`）；本案之合併單位無原街廓之並列者（`G011` ⇒ `R3`、`G025` ⇒ `R5`、`G030` ⇒ `R3`〔`3.5 m`〕／`R2`〔`0 m`〕·差皆 ≫ `0.01 ㎡`）。**他案**：主線自此遇「同一歸戶之分不到之土地分在二以上之街廓、而其應分配面積之加總相同」者⛔ 停機，依 KL `2026-10-17 14:55` 第 `1` 點、`15:23`「甲」之序擇原街廓：應分配面積之加總（`0.01 ㎡`）較大者 → 重劃前面積之合計較大者 → 最小之暫編地號較小者。

---

## `§五″`　驗收之基數（發單端以程式重算）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 `ops/queue` 之 `STATE.json` |
| `2` | 新名之占用（母體 ＝ `6dae569` 之追蹤檔 `2882` 檔·`git grep -l -F`） | `W-G.9-387_補令一` ＝ `0` 檔 ⇒ 可取；報告之二名 `W-G.9-387R_K-9-61之八之落地_執行報告`、`W-G.9-387R_K-9-61之八之落地_app差異` 唯見於原單（`docs/orders/W-G.9-387_規格單.md`·原單工項四所令之名·其檔⛔ 存：`git ls-tree -r --name-only 6dae569 docs/reports/` 無其列）⇒ 可取 |
| `3` | pre-flight | `python3 verify/probes/probe_order_preflight.py <本補令>`·發單端實跑（態 `6dae569`·定稿）：🔴 機械 `0` 項／🟡 提示 `1` 項——`P-4` `:48`（`§一″` 項 `1`·其「反向」與「→」唯 git 之 `commit` 之範圍〔`34736ab..6dae569` 與其反〕與二簿之 bytes 之改前改後，座標系即 git 之祖孫之序 ⇒ **具名豁免**）／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `23356`–`31098`·本補令⛔ 用） |
| `4` | 差異檔 | `4082` B·`44` 列·`git hash-object` ＝ `a1d0e389268dcf6612272d208c63e048bc6a993f`·`sha256` `1db8c9bc12ad67d47674d866fc86215a1860e1031e3d9606b4c67f91560fe07c`（發單端以工項一″ 之 `1` 之命令實算） |
| `5` | 模擬 | 拋棄式 worktree `6dae569`（雲端 Linux·⛔ `push`）＋ 本補令之定稿 ＋ 差異檔（工項一″ 之 `1` 之命令）＋ 報告之替身·二 `commit`（首列 ＝ 所令逐字）：工項零″ 之 blob ＝ 來源；差異檔之 blob ＝ 項 `4`；工項一″ 之重量甲（三呼叫 `rc 0`）、乙（`160c3f4` 之拋棄式 worktree·三呼叫 `rc 1`·末列 ＝ 期）、丙 ＝ 期；閘 `1″` 增刪 ＝ 本補令 `132`／`0`、差異檔 `44`／`0`、替身 `1`／`0`；閘 `2″` 恰三 `A`·生產碼與 `verify/` 對 `6dae569` 相異 `0`、生產碼對 `34736ab` 恰 `app.py`·三新檔之 `git check-ignore -v --no-index` 無命中（`rc 1`·對照 `rc 0`）；閘 `3″` `CR` `0`（`data/V6.dxf` `12308`）；閘 `4″` 相異 `0`；閘 `6″` `✅ 二閘皆過`·`624 623` ⇒ `rc 7`；閘 `7″` `rc 0`·四簿 ＝ `§零″` 項 `3`；閘 `8″` 十三呼叫皆 `rc 0`·末列皆 `⇒ 紅 []；rc 0`·`stderr` `0` B；工項二″ 之前置 `2`〜`4`（以模擬之 `<C>`）＝ 期（`rev-list --count` `6`·`--merges` 空·命中唯 `d2c4f65`·`app.py` 之 blob ＝ `efae3a5a…`）；工項二″ 之快轉與閘 `5″` 須遠端·⛔ 模擬；結束時 `git status --porcelain` 空 |

SELF_SHA256: b503caee9b75b14420ee4399537b969d43f97028c079052beaaf53a79fc78e1c
