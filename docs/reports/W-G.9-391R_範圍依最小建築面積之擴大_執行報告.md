# `W-G.9-391R`　執行報告：街角規定範圍與末端塊範圍依最小建築面積之擴大·短街廓之警示停止（`K-9-80` ④⑤⑥·`K-9-34`）

> **受單** ＝ 執行端（雲端排程「市地重劃·執行端」·Linux `4` 核·Python `3.11.17`）·`2026-10-21`。**單** ＝ `docs/orders/W-G.9-391_規格單.md`（`151956` B·`sha256` `22ef8a8c84f52b1d9ed0443705c87e685fefacafbd3134ec6aa82fb86f386c53`·`SELF_SHA256` `afb401e32d1b386414d6d862788a9462f06a42838310a02e1dd5378961df4347`·三者皆合）。
> **結果** ＝ 完成（停機款皆⛔ 成就）。**本案之配地⛔ 變**（`V-4`〜`V-6`）。主線 `wip/s1-endpart` ＝ `a8657c4`（⛔ 動）。
> `<O>` ＝ `/tmp/o391`（倉外）；施工樹 ＝ `/tmp/w`（完整複本）；前置之樹 ＝ `/tmp/w_pre`（`a749c78` 之 worktree）；驗之樹 ＝ `/tmp/w_post`（工項二之 `commit` 之 worktree）。
> 主 checkout 之同步由 KL 自行為之（README 第六節第 `6` 款）。

## ① 逐 `commit`（皆推新側支 `verify/W-G.9-391-k980x`）

| 工項 | `commit` | 首列（逐字·其後空一列附環境之尾列） |
|---|---|---|
| 零 | `65b1f254e2507fb7dcef262d9e540335bdc30571` | `W-G.9-391 工項零：本單原封入倉（新側支）⛔ 零生產碼` |
| 一 | `a749c78f0a9e908dc0a3668b79bc164c90fe8c1d` | `W-G.9-391 工項一：量測器（F35 之新器·既有之器十一之增許）（新側支）⛔ 零生產碼` |
| 二 | `a65e3c78bdc2ab06328ce442358245ddb236f831` | `W-G.9-391 工項二：街角規定範圍與末端塊範圍依最小建築面積之擴大·短街廓之警示停止（K-9-80 ④⑤⑥·K-9-34）🔴 生產碼（新側支）` |
| 三 | `54812a48960e2669d014973c7deaca0befc12f16` | `W-G.9-391 工項三：範圍依最小建築面積之擴大之讀法入典·待落地清單之更新（新側支）⛔ 零生產碼` |
| 四 | （本檔之 `commit`·見 `ops/queue` 之回報） | `W-G.9-391 工項四：執行報告入倉（新側支）⛔ 零生產碼` |

🔎 工項二之 `commit` 初為 `d565c5b1f8437fd92504a6718b6f81298ff1e58a`（⛔ 推）；唯讀審查之 (B) 一（`R-9` 之區域名）修之後以 `--amend`（未推之本地）改為 `a65e3c7`，`V-1`〜`V-9` 從頭重跑（第二趟）皆符後始推（⑥）。

三檔之施後 blob（`a65e3c7`）：`app.py` ＝ `b591d7605b932b42c9dc205bb8589ef04505045b`（`+201`／`−17`）、`verify/stepg_pipeline.py` ＝ `b2f6622351d1bcdcdf7b603c7412a8f902aa2edc`（`+9`／`−0`）、`verify/run_verification.py` ＝ `ef043da43e69f236550d0f420f6684f2edd271e4`（`+1`／`−0`）。

## ② 停機款 `1`〜`13`（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `a8657c4`；heads `50` 且無新側支；施工樹淨；`§零-0` 項 `3` `rc 0`·四簿 ＝ 期；旗標 `[None ×5]`；環境可匯入 | 主線 `a8657c4012d961eccebd77cd812c0ab6aeab030f`；heads `50`（無 `verify/W-G.9-391-k980x`）；`git status --porcelain --untracked-files=no` 空；`probe_WG9321_issuer_anchor.py … 634 629` `rc 0`·四簿 自誤 `619`／`634`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；旗標 `[None, None, None, None, None]`；匯入於裝後 `rc 0` ⇒ ⛔ 成就 |
| `2` | `SELF_SHA256`、bytes／`sha256` 合；入倉之 blob ＝ 來源 | 皆合；`git cat-file blob HEAD:docs/orders/W-G.9-391_規格單.md` 與來源 `cmp` 同 ⇒ ⛔ 成就 |
| `3` | 塊 `Fy46`／`K37`／`P48` 之 bytes／`sha256`／列數 ＝ `§五-1`；`git apply --check` 過；寫出後之 blob ＝ 項 `5` | `Fy46` `56670`／`44884335…`／`861`；`K37` `9488`／`0b26ce6f…`／`57`；`P48` `3045`／`1a358015…`／`21`；`--check` 過；`12` 器之 blob ＝ 項 `5`（④）⇒ ⛔ 成就 |
| `4` | 前置之期皆符 | (甲) `33`、(乙) `6` 呼叫皆合期；(丙) 沿用（比對皆同）；前置 `4` 四字樣皆無出艙 `rc 1` ⇒ ⛔ 成就 |
| `5` | ⛔ 歧義涉域；⛔ 須改禁改 | ⛔ 見（`§三-4` 之諸形：本案配地⛔ 變；二退縮⛔ 觸 `R-8`／`R-3`／`R-4` 之停機；範圍之他之建構唯 `wf_f4._reshape_block`〔`R-9` 明除〕；`F35 R2` 之諸街廓 ＝ 輸入值）⇒ ⛔ 成就 |
| `6` | `V-1`〜`V-9` 皆期；⛔ 改器；配地⛔ 變 | 二趟皆期（③）；器⛔ 改（`V-3`）；`k6s3 cmp` 相異 `0`、`F8` 同、`parity` 同 ⇒ ⛔ 成就 |
| `7` | `push` 之目標唯新側支／`ops/queue`；⛔ 被拒；主線⛔ 推進 | 工項零〜三皆推 `verify/W-G.9-391-k980x`（零 ＝ 新立·其後快轉）、回報推 `ops/queue`；⛔ 被拒（`ops/queue` 之接單之初推因發單端同時推門鈴之列而非快轉 ⇒ 依 README 第五節重取再判〔仍 `pending`〕後重推·非本批之側支）；主線 ＝ `a8657c4` ⇒ ⛔ 成就 |
| `8` | 二檔之刪除欄 `0`、嚴格前綴、尾 ＝ 塊、blob ＝ 項 `5`；`checkidx`／`gen_fa_index` 合 | `K-6` 典 `57`／`0`·`909964` → `919452`·blob `0fad1dafd3c6236b571969b1538170f8662d9ee6`；`docs/待落地清單.md` `21`／`0`·`20188` → `23233`·blob `48b50c3da80dff7143b82fc9eeba00673750a158`；前綴真·尾 ＝ 塊；`checkidx` `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` `則 124；加註節 14；列 158`·重生成與倉內逐位同 ⇒ ⛔ 成就 |
| `9` | 收工閘皆期 | 見 `ops/queue` 之回報（自指·⛔ 寫入本檔） |
| `10` | ⛔ 自判正典；⛔ 改塊、器、命令 | ⛔ 為；`<repo>` 以絕對路徑傳入（`/tmp/w_pre`、`/tmp/w_post`、`/tmp/w`） ⇒ ⛔ 成就 |
| `11` | 新檔⛔ 為 `check-ignore` 所命中 | 本單、`F35` 皆 `rc 1`（無命中）；報告二檔見收工閘 ⇒ ⛔ 成就 |
| `12` | 審查之發現⛔ 涉域上判斷或規格之漏載 | 二 WARN 皆塊 `K37` 之二之己之逐字、且在發單端之「記而⛔ 改」（單 `§一` 項 `7`）⇒ 非新；(B) 一 ＝ 純實作（已修）⇒ ⛔ 成就（⑥） |
| `13` | 存取⛔ 被拒；寫入⛔ 為分類器所拒 | ⛔ 見 ⇒ ⛔ 成就 |

## ③ 前置與驗之出艙

### 環境與前置 (丙) 之比對

- `python3 -c "import shapely,…"` 初 `rc 1`（`shapely` 缺）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`·出艙 `<O>/pip_install.txt`）⇒ 裝後 `certifi==2026.10.19`、`pillow==10.2.0`、`websockets==17.3`（異於基準）⇒ `python3 -m pip install certifi==2026.10.18 pillow==12.3.0 websockets==17.2 --break-system-packages`（`rc 0`·`Successfully installed certifi-2026.10.18 pillow-12.3.0 websockets-17.2`）⇒ 匯入 `rc 0`。
- 比對：主線之端 `a8657c4012d961eccebd77cd812c0ab6aeab030f` ＝ 基準之 sha；`python3 --version` ＝ `Python 3.11.17` ＝ 基準；`python3 -m pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ＝ 基準 ⇒ **皆同 ⇒ 前置 (丙) 之 `38` 呼叫沿用** `ops/queue` 之 `基準/a8657c4012d961eccebd77cd812c0ab6aeab030f.md` 之值（⛔ 重跑·下表標「基準·沿用」）。
- pre-flight（`§零-3`·`python3 verify/probes/probe_order_preflight.py <本單>`·`rc 0`）：🔴 機械 `0`；🟡 `3`（`P-4` 於 `:155`、`:232`、`:1296`）＝ `§五-1` 項 `9` 之三處 ⇒ 依單之**具名豁免**；ℹ️ `P-5` ✅ 相符（受詞 `151878` B）、`P-3` `def main` ＝ `23508`-`31250`。

### 前置 `4`（判別力）

`git grep -c -F "<字樣>" -- app.py verify/stepg_pipeline.py verify/run_verification.py` 於工項一之端：「K-9-80 ⑥」「k980_mba」「k980_range_touch_check」「end_block_band_width」⇒ 皆無出艙、`rc 1`。

### `77` 呼叫之表（前置 ＝ 工項一之端〔(甲)(乙) 實跑於 `/tmp/w_pre`·(丙) 沿用〕；施後 ＝ 第二趟〔`a65e3c7`·`/tmp/w_post`〕；格 ＝ `rc`／`stderr` B／末列（耗時 s））


| # | 命令 | 工項一之端（實跑或沿用） | 施後（`d565c5b`·實跑） | 合期 |
|---|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（141） | `0`／`0`／`⇒ 紅 []；rc 0`（132） | ✅ |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（429） | `0`／`0`／`⇒ 紅 []；rc 0`（412） | ✅ |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（34） | `0`／`0`／`⇒ 紅 []；rc 0`（33） | ✅ |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（33） | `0`／`0`／`⇒ 紅 []；rc 0`（34） | ✅ |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） | ✅ |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·36） | `0`／`0`／`⇒ 紅 []；rc 0`（37） | ✅ |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·14） | `0`／`0`／`⇒ 紅 []；rc 0`（14） | ✅ |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·232） | `0`／`0`／`⇒ 紅 []；rc 0`（245） | ✅ |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·70） | `0`／`0`／`⇒ 紅 []；rc 0`（75） | ✅ |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（509） | `0`／`0`／`⇒ 紅 []；rc 0`（502） | ✅ |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（713） | `0`／`0`／`⇒ 紅 []；rc 0`（700） | ✅ |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） | ✅ |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） | ✅ |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） | ✅ |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（基準·沿用·67） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（68） | ✅ |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·389） | `0`／`0`／`⇒ 紅 []；rc 0`（412） | ✅ |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1940） | `0`／`0`／`⇒ 紅 []；rc 0`（1937） | ✅ |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·33） | `0`／`0`／`⇒ 紅 []；rc 0`（33） | ✅ |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） | ✅ |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（基準·沿用·21） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（23） | ✅ |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·21） | `0`／`0`／`⇒ 紅 []；rc 0`（21） | ✅ |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·243） | `0`／`0`／`⇒ 紅 []；rc 0`（264） | ✅ |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·325） | `0`／`0`／`⇒ 紅 []；rc 0`（369） | ✅ |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·35） | `0`／`0`／`⇒ 紅 []；rc 0`（37） | ✅ |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·31） | `0`／`0`／`⇒ 紅 []；rc 0`（31） | ✅ |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（8） | `0`／`0`／`⇒ 紅 []；rc 0`（7） | ✅ |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（23） | `0`／`0`／`⇒ 紅 []；rc 0`（22） | ✅ |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（16） | `0`／`0`／`⇒ 紅 []；rc 0`（17） | ✅ |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（13） | `0`／`0`／`⇒ 紅 []；rc 0`（11） | ✅ |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·181） | `0`／`0`／`⇒ 紅 []；rc 0`（197） | ✅ |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·48） | `0`／`0`／`⇒ 紅 []；rc 0`（53） | ✅ |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·799） | `0`／`0`／`⇒ 紅 []；rc 0`（900） | ✅ |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） | ✅ |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·148） | `0`／`0`／`⇒ 紅 []；rc 0`（161） | ✅ |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·99） | `0`／`0`／`⇒ 紅 []；rc 0`（109） | ✅ |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） | ✅ |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·325） | `0`／`0`／`⇒ 紅 []；rc 0`（369） | ✅ |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（基準·沿用·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） | ✅ |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（基準·沿用·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） | ✅ |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（基準·沿用·1） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） | ✅ |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（基準·沿用·9） | `0`／`0`／`紅項 [] 器紅 0`（10） | ✅ |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（基準·沿用·331） | `0`／`0`／`⇒ 紅 []；rc 0`（373） | ✅ |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（215） | `0`／`0`／`（JSON 之摘要列·略）`（204） | ✅ |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（159） | `0`／`0`／`（JSON 之摘要列·略）`（150） | ✅ |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（219） | `0`／`0`／`⇒ 紅 []；rc 0`（204） | ✅ |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（154） | `0`／`0`／`⇒ 紅 []；rc 0`（150） | ✅ |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（468） | `0`／`0`／`⇒ rc 0（不符 0 項）`（450） | ✅ |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（332） | `0`／`0`／`⇒ rc 0（不符 0 項）`（324） | ✅ |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（4） | ✅ |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） | ✅ |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（366） | `0`／`0`／`⇒ 紅 []；rc 0`（361） | ✅ |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1380） | `0`／`0`／`⇒ 紅 []；rc 0`（1357） | ✅ |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1345） | `0`／`0`／`⇒ 紅 []；rc 0`（1365） | ✅ |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（146） | `0`／`0`／`⇒ 紅 []；rc 0`（142） | ✅ |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（488） | `0`／`0`／`⇒ 紅 []；rc 0`（467） | ✅ |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） | ✅ |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（367） | `0`／`0`／`⇒ 紅 []；rc 0`（368） | ✅ |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） | ✅ |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W8', 'W9']；rc 1`（7） | `0`／`0`／`⇒ 紅 []；rc 0`（23） | ✅ |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `1`／`0`／`⇒ 紅 ['受詞缺']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（149） | ✅ |

施後合期 77／77；工項一之端之實跑 39 呼叫（其餘 38 沿用基準）


### 第一趟（`d565c5b`·`V-1`〜`V-6` 之 `77` 呼叫·其後唯讀審查之 (B) 一修之 ⇒ 第二趟從頭重跑）

| # | rc | stderr B | 末列 | s |
|---|---|---|---|---|
| `1` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `2` | `0` | `0` | `⇒ 紅 []；rc 0` | 132 |
| `3` | `0` | `0` | `⇒ 紅 []；rc 0` | 412 |
| `4` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `5` | `0` | `0` | `⇒ 紅 []；rc 0` | 33 |
| `6` | `0` | `0` | `⇒ 紅 []；rc 0` | 34 |
| `7` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `8` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `9` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `10` | `0` | `0` | `⇒ 紅 []；rc 0` | 37 |
| `11` | `0` | `0` | `⇒ 紅 []；rc 0` | 14 |
| `12` | `0` | `0` | `⇒ 紅 []；rc 0` | 245 |
| `13` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `14` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `15` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `16` | `0` | `0` | `⇒ 紅 []；rc 0` | 75 |
| `17` | `0` | `0` | `⇒ 紅 []；rc 0` | 502 |
| `18` | `0` | `0` | `⇒ 紅 []；rc 0` | 700 |
| `19` | `0` | `0` | `⇒ 突變 8（另基準一）；紅 []；rc 0` | 8 |
| `20` | `0` | `0` | `⇒ 紅 []；rc 0` | 1 |
| `21` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `22` | `0` | `0` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` | 68 |
| `23` | `0` | `0` | `⇒ 紅 []；rc 0` | 412 |
| `24` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `25` | `0` | `0` | `⇒ 紅 []；rc 0` | 1937 |
| `26` | `0` | `0` | `⇒ 紅 []；rc 0` | 33 |
| `27` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `28` | `0` | `0` | `⇒ 紅 []；rc 0` | 5 |
| `29` | `0` | `0` | `⇒ rc 0（不符 0·器紅 0）` | 23 |
| `30` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `31` | `0` | `0` | `⇒ 紅 []；rc 0` | 21 |
| `32` | `0` | `0` | `⇒ 紅 []；rc 0` | 264 |
| `33` | `0` | `0` | `⇒ 紅 []；rc 0` | 369 |
| `34` | `0` | `0` | `⇒ 紅 []；rc 0` | 37 |
| `35` | `0` | `0` | `⇒ 紅 []；rc 0` | 31 |
| `36` | `0` | `0` | `⇒ 紅 []；rc 0` | 7 |
| `37` | `0` | `0` | `⇒ 紅 []；rc 0` | 22 |
| `38` | `0` | `0` | `⇒ 紅 []；rc 0` | 17 |
| `39` | `0` | `0` | `⇒ 紅 []；rc 0` | 11 |
| `40` | `0` | `0` | `⇒ 紅 []；rc 0` | 197 |
| `41` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `42` | `0` | `0` | `⇒ 紅 []；rc 0` | 53 |
| `43` | `0` | `0` | `⇒ 紅 []；rc 0` | 900 |
| `44` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `45` | `0` | `0` | `⇒ 紅 []；rc 0` | 1 |
| `46` | `0` | `0` | `⇒ 紅 []；rc 0` | 161 |
| `47` | `0` | `0` | `⇒ 紅 []；rc 0` | 109 |
| `48` | `0` | `0` | `⇒ 紅 []；rc 0` | 1 |
| `49` | `0` | `0` | `⇒ 紅 []；rc 0` | 369 |
| `50` | `0` | `0` | `selftest 9/9 ⇒ ✅` | 0 |
| `51` | `0` | `0` | `selftest 13/13 ⇒ ✅` | 0 |
| `52` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `53` | `0` | `0` | `ε ＝ 0.0002｜rc 0` | 1 |
| `54` | `0` | `0` | `紅項 [] 器紅 0` | 10 |
| `55` | `0` | `0` | `⇒ 紅 []；rc 0` | 373 |
| `56` | `0` | `0` | `（JSON 之摘要列·略）` | 204 |
| `57` | `0` | `0` | `（JSON 之摘要列·略）` | 150 |
| `58` | `0` | `0` | `⇒ 紅 []；rc 0` | 204 |
| `59` | `0` | `0` | `⇒ 紅 []；rc 0` | 150 |
| `60` | `0` | `0` | `⇒ rc 0（不符 0 項）` | 450 |
| `61` | `0` | `0` | `⇒ rc 0（不符 0 項）` | 324 |
| `62` | `0` | `0` | `⇒ 紅 []；rc 0` | 4 |
| `63` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `64` | `0` | `0` | `⇒ 紅 []；rc 0` | 361 |
| `65` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `66` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `67` | `0` | `0` | `⇒ 紅 []；rc 0` | 1357 |
| `68` | `0` | `0` | `⇒ 紅 []；rc 0` | 1365 |
| `69` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `70` | `0` | `0` | `⇒ 紅 []；rc 0` | 142 |
| `71` | `0` | `0` | `⇒ 紅 []；rc 0` | 467 |
| `72` | `0` | `0` | `⇒ 紅 []；rc 0` | 1 |
| `73` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `74` | `0` | `0` | `⇒ 紅 []；rc 0` | 368 |
| `75` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `76` | `0` | `0` | `⇒ 紅 []；rc 0` | 23 |
| `77` | `0` | `0` | `⇒ 紅 []；rc 0` | 149 |

第一趟：`calls 77 NG 0 sum_s 13389`（並行 `2`·牆鐘 `6697` s）；`cmp` 二退縮 `相異 0 項 ⇒ ✅ 同`／`相異 0 項 ⇒ ✅ 同`；`F8` 之 `hash-object` `8be0160bc14dd92a5331f86eecc995cae0507376` `8be0160bc14dd92a5331f86eecc995cae0507376` `6fb86647807f9744594071be25c522b6b506c230` `6fb86647807f9744594071be25c522b6b506c230`；`parity`：

```
parity35_pre.json vs parity35_post.json: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
parity00_pre.json vs parity00_post.json: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
pre/60.out vs post/60.out: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
pre/61.out vs post/61.out: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
```

第二趟（本表之施後之欄）：`calls 77 NG 0 sum_s 13522`（並行 `2`·牆鐘 `6760` s）；`F23 selftest`（`#4`）之 `✅ P0 逐項擾動恰該項紅 75／75`；`F35 selftest` 之 `C1`〜`C9`、`E1`〜`E6`、`T1`〜`T6`、`K1` 與 `P0 22／22`、`F35 wiring` 之 `W1`〜`W9`、`F35 run` 之 `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0` 皆 ✅（全文見附錄）。

### `V-3`　器之載入

`a65e3c7` 之 `12` 器之 blob（`git rev-parse a65e3c7:verify/probes/<器>`）＝ `§五-1` 項 `5`：

```
24bb035ffceecb346914e700764ac40b153a6a1d
10df59760e80b96a7f41f97f6bcca668186682e1
4c450cf963cb7ffe39dcd528726a0482e1c216eb
2ce4dd5bb5f330c084e4667c44b13ddcd36f7825
67af34857e44ed3b186091e096f28ef18c6ffb70
1f1118b7457feb7aaa4c06d0abb3f361320075fa
c5cf831b8b872c21987a370984e4eba985fca44a
cf1d143df2ca188070a6787903753fe56e0798e5
a24ddf7e29c20ed6547e1fa847457881e76774e6
72ff303cb761bdc12a4402f70b7d8beb133512d0
40b4b1b73f6aefd24bf8080c8da054fb8b3588d5
80f6326ef5dea32b769e2423da0338cd86553fea
```

### `V-4`　`k6s3 cmp`（全文）

```
$ python3 verify/probes/probe_WG9344_k6s3.py cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json   # rc 0·stderr 0 B
相異 0 項 ⇒ ✅ 同
$ python3 verify/probes/probe_WG9344_k6s3.py cmp <O>/k6s3_pre_00.json <O>/k6s3_post_00.json   # rc 0·stderr 0 B
相異 0 項 ⇒ ✅ 同
```

`run` 二呼叫（`#56`／`#57`）皆 `rc 0`·`stderr` `0` B。

### `V-5`　`parity` 之正規化之比與其對照

以同一字樣 `<HEAD>` 代前態 `a749c78f0a9e908dc0a3668b79bc164c90fe8c1d`、後態 `a65e3c78bdc2ab06328ce442358245ddb236f831` 之全值後逐位比（`<O>/v5.py`）：

```
parity35_pre.json vs parity35_post.json: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
parity00_pre.json vs parity00_post.json: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
pre/60.out vs post/60.out: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
pre/61.out vs post/61.out: 代之 ⇒ 逐位同（代之數 1／1）；⛔ 代之（對照）⇒ 相異
```

末十五列（`3.5 m`·施後）：

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（19 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（13 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 3.5, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（37 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（45／45）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
```

末十五列（`0 m`·施後）：

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（0 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（0 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 0.0, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（46 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（46／46）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
```

### `V-6`　`F8` 之 `git hash-object`（`pre_35`、`post_35`、`pre_00`、`post_00`）

```
8be0160bc14dd92a5331f86eecc995cae0507376
8be0160bc14dd92a5331f86eecc995cae0507376
6fb86647807f9744594071be25c522b6b506c230
6fb86647807f9744594071be25c522b6b506c230
```

二對各逐位同（`3.5 m` `8be0160b…`、`0 m` `6fb86647…` ＝ 基準）。

### `V-7`　生產碼之相異（`a749c78` → `a65e3c7`·`<O>/v7.py`·AST）

```
生產碼之數 34 34
生產碼相異 3 ['app.py', 'verify/run_verification.py', 'verify/stepg_pipeline.py']
verify/ 相異 2 ['M\tverify/run_verification.py', 'M\tverify/stepg_pipeline.py']
app.py 增 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check'] 減 [] 改 ['_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_host', 'end_block_side_geom', 'f3_screen_stepg_run', 'main', 'select_corner_lots_both_sides_v12'] 相異之節點 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_side_geom', 'f3_screen_stepg_run', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']
  blob b591d7605b932b42c9dc205bb8589ef04505045b 增刪 201	17	app.py
verify/stepg_pipeline.py 增 [] 減 [] 改 ['_run_step_g_impl'] 相異之節點 ['_run_step_g_impl']
  blob b2f6622351d1bcdcdf7b603c7412a8f902aa2edc 增刪 9	0	verify/stepg_pipeline.py
verify/run_verification.py 增 [] 減 [] 改 ['build_param_table'] 相異之節點 ['build_param_table']
  blob ef043da43e69f236550d0f420f6684f2edd271e4 增刪 1	0	verify/run_verification.py
```

### `V-8`　字樣（`git grep -c -F … a65e3c7 -- 三檔`）

```
[K-9-80 ⑥]
a65e3c7:app.py:4
[k980_mba]
a65e3c7:app.py:6
a65e3c7:verify/run_verification.py:1
a65e3c7:verify/stepg_pipeline.py:3
[k980_range_touch_check]
a65e3c7:app.py:4
a65e3c7:verify/stepg_pipeline.py:1
[end_block_band_width]
a65e3c7:app.py:7
```

皆 ≥ 期（「K-9-80 ⑥」`app.py` `4` ≥ `3`；「k980_mba」三檔 `6`／`1`／`3`；「k980_range_touch_check」`app.py` `4` ≥ `3`、stepg `1`；「end_block_band_width」`app.py` `7` ≥ `2`）；判別力 ＝ 前置 `4`。

### `V-9`　`stderr`

第二趟之 `77` 呼叫與 `cmp` 二呼叫之 `stderr` 合計 `0` B（第一趟亦 `0` B；前置之 `39` 呼叫亦 `0` B）。

## ④ 塊之實得與二檔之改前改後

| 塊 | bytes | `sha256` | 列 | 期（`§五-1`） |
|---|---|---|---|---|
| `Fy46` | `56670` | `44884335729bc8b1cf79c144a3cdb959b13ce4949b2c9c5233b83424c6698cf5` | `861` | 同 |
| `K37` | `9488` | `0b26ce6fcfcefc753f2969343b8398c48b1f3641657095d9cb659e9d03df1afb` | `57` | 同 |
| `P48` | `3045` | `1a3580158b9588e82d151d05eba573dcb1bbb344264e7b965b1448ddd7cd3ed1` | `21` | 同 |
| `CK`（自 `docs/orders/W-G.9-365_輕量單.md` 之附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | 同 |
| `GF`（同·附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | 同 |

`Fy46` 之施前 blob（`12` 器之 `11`）皆 ＝ `§五-1` 項 `2`（`probe_WG9391_k980x.py` 施前⛔ 存）；施後之 `12` 器之 blob ＝ 項 `5`（`24bb035f`、`10df5976`、`4c450cf9`、`2ce4dd5b`、`67af3485`、`1f1118b7`、`c5cf831b`、`cf1d143d`、`a24ddf7e`、`72ff303c`、`40b4b1b7`、`80f6326e`）；`git status --porcelain` 唯此 `12` 檔；工項一之增刪 ＝ 收工閘 `1` 之列（`4`／`2` ×3、`7`／`0` ×3、`8`／`1`、`8`／`0`、`10`／`1`、`9`／`0`、`9`／`1`、`559`／`0`）。

| 檔 | 改前 bytes／blob | 改後 bytes／blob | 增／刪 |
|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `909964`／`8ae87d473218de9ff2efd19ef5890502da8fbfa6` | `919452`／`0fad1dafd3c6236b571969b1538170f8662d9ee6` | `57`／`0` |
| `docs/待落地清單.md` | `20188`／`adf906d43045f365cec15fc345666c9c874faed5` | `23233`／`48b50c3da80dff7143b82fc9eeba00673750a158` | `21`／`0` |

二檔：改前全檔為改後之嚴格前綴（真）、改後之尾 ＝ 其塊（真）。

## ⑤ 推送之目標與推後之 heads

| 工項 | 命令 | 結果 |
|---|---|---|
| 零 | `git push origin HEAD:refs/heads/verify/W-G.9-391-k980x` | `* [new branch] HEAD -> verify/W-G.9-391-k980x`；推後 heads `51`、主線 `a8657c4` |
| 一 | `git push origin HEAD:verify/W-G.9-391-k980x` | `65b1f25..a749c78` |
| 二 | 同 | `a749c78..a65e3c7`（驗二趟與審查皆符後·與驗為分開之呼叫） |
| 三 | 同 | `a65e3c7..54812a4` |
| 四 | 同 | 見 `ops/queue` 之回報 |

本檔撰時（工項三推後）之 `git ls-remote --heads origin`：`51` 列；`refs/heads/verify/W-G.9-391-k980x` ＝ `54812a48960e2669d014973c7deaca0befc12f16`；`refs/heads/wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`；除 `ops/queue` 與新側支外之 `49` 列逐列 ＝ `<O>/heads_before_391.txt`（`diff` 空）。

## ⑥ 自捕與自解·唯讀獨立審查

### 執行端之自捕與自解

| # | 事 | 處置 |
|---|---|---|
| 自捕 1 | 前置 (甲)(乙) 之 runner 首次啟動之呼叫之列含 `#64` 重複（`40` 列） | 啟動數秒內察覺 ⇒ 止之（含已起之二子行程 `#25`／`#67`）、清其出艙、以正確之 `39` 列重啟；最終出艙唯重啟之趟（各呼叫恰一筆） |
| 自捕 2 | `V-*` 第一趟之 runner 首次啟動之列含 `#43` 重複（`78` 列） | 同上：止之（含已起之 `#25`／`#68`）、清其出艙；改以程式自項 `8` 之表生成去重之列（斷言 `77` 相異）後重啟 |
| 自捕 3 | 撰碼中自查（`/tmp/o391/anchorcheck.py`·非量測器）：`k980_range_touch_check` 之訊息之 `m ≤ ` 使量測器之一字串常數（`probe_ruling_K8_sideline_pairing.py` 之 f 字串之 `m ≤ `）於 `app.py` 由恰一見變二見（`§三-3` 第 `1` 款） | 改訊息為「距 … m·相接之距 … m」；複查 ⇒ 恰一見之違 `0` |
| 自捕 4 | 撰碼中自查：新 docstring 之折行有「四個以上之空白繼以中文起首」之列（`§三-3` 第 `1` 款） | 改為以 `-`／反引號起首；審查另以 AST 複驗新增之列 ⇒ 無 |
| 自捕 5 | 撰碼中自查並行：前置 (甲)(乙) 跑時（並行 `2`），撰碼之自跑（`F35 selftest`／`wiring`／`run`、`F23 wiring`、`F24 wiring`）逐一另起（同時至多 `3` 行程·`nproc` `4`）| 照實記之；前置之 `39` 呼叫皆合期（其結果不依時）；`V-*` 之二趟則嚴守並行 `2`（其間⛔ 他負載·唯讀審查於第一趟畢後始派） |

| 自捕 6 | 單首 🔑「Bash 命令⛔ 含 heredoc」：接單時（讀單之前）於 `/tmp/q` 改 `STATE.json` 之一命令用 heredoc；報告之組裝時一命令誤含空之 heredoc（`python3 - <<'EOF'` 而無本文·無作用） | 照實記之；二者皆⛔ 涉施工樹與單之命令（`STATE.json` 之改已依 `執行端.md` 乙 2 推之·其 `diff` 唯 `status`／`status_since`／`history` 一筆）；其餘之命令皆以腳本檔為之 |

### 唯讀獨立審查（一輪·`redistribution-reviewer`·⛔ 改檔、⛔ `commit`·受詞 `d565c5b`）

審查自跑之證：差異逐字 ＝ `item2.diff`；`py_compile` 三檔過；`F35 selftest`／`wiring … a8657c4`／`run` 皆 `rc 0`；`§三-3` 六款以其自寫之 AST 腳本重驗皆成立（量測器之字串常數於基準 `app.py` 恰一見者 `714`、工作樹⛔ 恰一者 `0`；三指定錨恰一；新巢狀名唯 `_area_at391`、`_piece391`；新增之列無「四空白＋中文」起首；頂層之增恰六、改恰十；六既有函式之簽名唯末增 `min_build_area=None`；`main` 唯增一列；新增之列無 `GB-`／【未裁】／案件字面）。

**R-6／R-7 之窮查**：範圍之建構唯四處（v12、`main`、`build_param_table`、stepg 之 ctx）皆傳；下游之門檻與名單（`f3_corner_range_areas`／`polys` ⇒ `_lot_gate`、K-4 之 `_cr_areas_jw`、末端評選之排除；參數表之街角最小面積 ⇒ `_corner_buffer_S`〔畫面／stepg／wf_f1〕、`selection_pipeline`、`wd3_fragment_geom`；`R_end` ⇒ `end_block_pick` 之門檻、`end_block_forced_buf`／`bands`）皆讀擴大後者；唯 `wf_f4._reshape_block` 讀未擴大者（`R-9` 明除）⇒ 「名單或門檻用未擴大之範圍」⛔ 見。

**獨立之合成之例**（`F35` 之外·審查之 `/tmp/rev391/syn*.py`）：
- (a) 左 ＝ SIDE_LINE 之街角（截角 `3×3`）、右 ＝ 無側街之末端塊（未臨正街三角形 `80 ㎡`）、深 `20`、最小建築面積 `200`：寬 `16.2` ⇒ 擴大前⛔ 相接；擴大後街角 `200.0045 ㎡`（遠界 `x ＝ 10.2252`）、`R_end` `200.0049 ㎡`（帶寬 `6.0002`）、距 `0`、交 `0.51 ㎡` ⇒ `k980_range_touch_check` 以「K-9-80 ⑥ 短街廓·左側街角規定範圍與右端末端塊範圍」停；寬 `16.5`（距 `0.2745`）、`17`（距 `0.7744`）⇒ ⛔ 停；三寬於 `None`／`0` 之 `wkb` 與基準逐位同。
- (b) 斜交 SIDE_LINE `(0,0)→(8,20)`（原範圍 `71.2142 ㎡`）：最小建築面積 `250`、`333.33` ⇒ `250.0055`、`333.3338 ㎡`（皆 ∈ `[值, 值＋0.01]`）；遠界於 `y＝0` 與 `y＝20` 之 `x` 差 `8.000000`（∥ SIDE_LINE）·含原範圍；右側鏡射 ⇒ `−8.000000`；`2000` ⇒ ⑥ 停；`−1` ⇒ `_stop`；`None`／`0`／`面積 − 1e-7` ⇒ `wkb` 與基準同。
- (c) ALLOC 斜向 `(0.3,1)` 之末端塊：`None`／`0` ⇒ `wkb` 與基準同；`500` ⇒ `R_end` `500.0007`、帶之內側界之向 ∥ ALLOC。

**發現與處置**：

| # | 審查之類 | 處 | 要旨 | 執行端之處置 |
|---|---|---|---|---|
| 1 | WARN（判斷層） | 二宿主之 `k980_range_touch_check`（`end_block_host` 之後） | 定案趟之 `end_block_pick`「皆未達」之停機可先於 ⑥ 之停機發出 ⇒ 短街廓仍停，惟其訊息或非「K-9-80 ⑥」 | ⛔ 停機款 `12`：查之時點 ＝ 塊 `K37` 之二之己之逐字（「末端塊與他範圍 ＝ 末端塊之評選（`end_block_host`）之後」）；「短街廓之查於選位時之提前」已在發單端之審查之「記而⛔ 改」（單 `§一` 項 `7`·塊 `K37` 之六／`P48` 序 `26`）⇒ 非新漏載·照實記 |
| 2 | WARN（判斷層） | 塊 `K37` 之二之己 | 未輸入而二範圍本即相接亦停 ⇒ 他案之新停機點，宜於交付之通知明列 | ⛔ 停機款 `12`：該讀法為塊 `K37` 之二之己之逐字、單 `§一` 項 `7` 之「記而⛔ 改」亦載；本案 `F35 R1` 未觸；交發單端之通知 |
| 3 | B（純實作） | `end_block_band_width` | 新增之區域名 `unary_union`（import）、推導式之 `g` ⛔ 帶 `391`（`R-9`）；執行端複查另得巢狀函式之引數 `_w` | **修之**：`unary_union as _uu391`、`_g391`、`_w391`（`+4`／`−4`）⇒ 工項二之 `commit` 由 `d565c5b` 改為 `a65e3c7`（⛔ 推過·`--amend` 於未推之本地）；AST 複查新增之區域名之⛔ 帶 `391` 者唯簽名之 `min_build_area`（單所令）與 `_mba_pk`（單所令）；`V-1`〜`V-9` 從頭重跑（第二趟·見 ③） |
| 4 | C | `_build_corner_range_v3` | 規格外之「擴大後須含擴大前」之停機 | 照留（`K-6` 典 `W-G.9-391` 之節之六 `56` 之「其二分之單調之設失之者停機（⛔ 靜默）」之實作）·記之 |
| 5 | C | `R-3` 之非凸／`有效值 ≈ 全街廓` | 非凸之缺口（審查之 U 形例 `420`）⇒「二分⛔ 收斂」之 `_stop`（訊息無「短街廓」） | 照留（loud·他案之形 `56`）·記之 |
| 6 | C | `_place_pool_parcels` 之末端保留帶 | 與 `end_block_side_geom` 之 `R_end` 之帶同式而非同物：右端之 `end_pt` 二式（`_cp + S_block_max·d̂` 與 `p1 + dot(p2−p1, d̂)·d̂`）至多差 ulp ⇒ 有輸入者之二分或於邊界異路 | 照留：未臨正街之多邊形依 `R-5` 取同處既有之 `_block_strip`；`end_pt` 之二式為既有（改前 `_end_band` 之直呼亦然）·記之 |
| 7 | C | stepg 之 ctx 之 `except` | `R-3` 之停機於 ctx 處被既有之 `except` 收（入 `corner_range_errors`） | 照留：同一輸入先於 `build_param_table`（無 `try`）停機·記之 |
| 8 | C | `k980_range_touch_check` | 非 shapely 之物被略 | 照留：諸呼叫端皆傳 shapely 或 `None`·記之 |
| 9 | C（程序） | 審查之自跑 | 其 `py_compile` 寫 `/tmp/w_post/__pycache__/*.pyc`（`.gitignore` 內·`git status` 淨） | 第二趟另建新工作樹（`/tmp/w_post` 移除後重建於 `a65e3c7`） |

## ⑦ 設計說明（`§三-5`）

### 逐條（`R-1`〜`R-9`）

| 條 | 落於何處 | 字樣 |
|---|---|---|
| `R-1` | `app.py` 頂層·`k91_effective_min_build_area` 之後 | `K980_AREA_TOL = 0.01`（㎡·擴大後之面積之上餘）、`K980_AREA_EPS = 1e-6`（㎡·「已達」之浮點餘裕）、`K980_TOUCH_TOL = 0.01`（m·相接之距）；各附註其義 |
| `R-2` | `app.py` 頂層新函式 `k980_mba(session, label, category)`（緊接三常數） | `session` 為 `None` ⇒ `{}`；回 `k91_effective_min_build_area(label, category, session.get(K91_SS_MBA_BY_LABEL) or {}, session.get(K91_SS_MBA_BY_CATEGORY) or {})`；鍵缺 ⇒ 未輸入（`0.0`·⛔ 停機） |
| `R-3` | `_build_corner_range_v3`：簽名之末增 `min_build_area=None`；擴大之碼唯插於函式末之 `return rng` 之前（既有之列一字⛔ 動） | `None` ⇒ 跳過；`< 0` ⇒ `_stop`；`> 0` 且 `rng.area < 有效值 − K980_AREA_EPS` ⇒ 擴大（見下之求解）；否則逐位同 |
| `R-4` | 頂層新函式 `end_block_band_width(block_poly, cad_alloc, end_pt, min_width, frag_poly, min_build_area, _label='')`（置於 `_end_band` 與 `_end_region_R` 之間）；`_end_region_R` 增 `min_build_area=None`（`None`／`0` ⇒ 帶寬 ＝ `min_width`；否則以 `end_block_band_width` 之回傳重賦 `min_width` 後經既有之 `band = _end_band(…, min_width, …)` 之句構帶·該句一字⛔ 動）；`end_block_side_geom`、`end_block_apply`、`end_block_host` 各增 `min_build_area=None`（簽名之末）並逐層照傳 | `end_block_host` 之照傳以**新增之一列** `min_build_area=min_build_area,` 插於 `trial=_trial, cache=_cache, allow_forced=_allow)` 之前一列（`§三-3` 第 `1` 款） |
| `R-5` | `_place_pool_parcels`：簽名之末增 `min_build_area=None`；末端保留之帶 ＝ `_end_region_R(blk_poly, alloc_dir_cad, <end_pt>, float(min_width), _unf_strip391[0], _label=…, min_build_area=min_build_area)[0]` | 未臨正街之多邊形 ＝ 同處既有之 `_block_strip(…)` 之回傳（改為留其二元組 `_unf_strip391`·`_unfront` 取其 `[1]`·⛔ 另算）；`_end_band` 之直呼刪 |
| `R-6` | 畫面 `f3_screen_stepg_run`、harness `_run_step_g_impl` | `end_block_host(…)` 與 `_place_pool_parcels(…)` 之呼叫各增一列 `min_build_area=k980_mba(<session>, blk_label, blk_meta.get('category', ''))`（harness 經 `ns['k980_mba'](ss, …)`）；`end_block_host` 之呼叫之後（同一 `if` 區塊之內）呼叫 `k980_range_touch_check(blk_label, {'左側街角規定範圍': …, '右側街角規定範圍': …, '左端末端塊範圍': (_eb_info['left'] or {}).get('r_end'), '右端末端塊範圍': …})`——街角規定範圍之源：畫面 ＝ 傳予 `end_block_host` 之 `_eb_crp`（同物）；harness ＝ `ctx['corner_range_polys'].get((blk_label, side))`（與傳予 `end_block_host` 之 dict 之值同物）；`_WF_NS_NAMES` 增 `"k980_mba", "k980_range_touch_check"`（附註列） |
| `R-7` | 四處之 `_build_corner_range_v3(…)` | ① v12：`_mba_pk = k980_mba(_st_wb5.session_state, _this_blk_B4, (_blk_meta_wb or {}).get('category', ''))` 立於取 `_blk_meta_wb` 之 `try` 之末、其 `except` 之支立 `_mba_pk = None`（該支 `_alloc_wb = None` ⇒ ⛔ 構造範圍）；呼叫增一列 `min_build_area=_mba_pk,`；二範圍建畢（`for` 之後·`if _alloc_wb …` 之外）呼叫 `k980_range_touch_check(_this_blk_B4, {'左側街角規定範圍': _corner_range_left, '右側街角規定範圍': _corner_range_right})`；② `main` 之參數表：**唯增一列** `min_build_area=k980_mba(st.session_state, _lbl, b.get('category', '')),`（插於 `_make_chamfer_tri_wb(b, _wh_cr),` 與 `dxf_quantum=_q_cr, …` 之間）；③ `build_param_table`：增一列 `min_build_area=ns["k980_mba"](fake_st.session_state, lbl, b.get("category", "")),`；④ stepg 之 ctx：增一列 `min_build_area=ns['k980_mba'](ss, _crp_lbl, _crp_b.get('category', '')),` |
| `R-8` | 頂層新函式 `k980_range_touch_check(blk_label, ranges)`（緊接 `k980_mba`） | `None`／空者不計；任二者 `distance ≤ K980_TOUCH_TOL` ⇒ `raise RuntimeError`（訊息含「K-9-80 ⑥」「短街廓」、街廓名、二範圍之名、距、交之面積）；他 ⇒ `None` |
| `R-9` | 訊息 | 三處之停機訊息⛔ 帶 `GB-` 號或【未裁】；新 docstring／附註載 `W-G.9-391` 與所據之條；`verify/wf_f4.py` 一字⛔ 動；新增之區域名皆帶 `391`（`_mba_pk` 為單所指名之例外） |

### `R-3`／`R-4` 之求解

- **`R-3`（街角）**：線之參數 ＝ 自截角前側界 `S1` 沿 `sigma·d̂` 之路平行距 `p`（`p ＝ S1_par` 即既有之平移後側界）；`_piece391(p)` ＝ 過 `S1 + sigma·p·d̂`、方向 `(sux, suy)`、半長 `_ext`（既有之值）之線切 `blk`，取片中距既有之 `_anchor` 最近者扣截角三角形（`buffer(0)` 之修同既有）；片數 ＜ `2` ⇒ `None`。
  - **全街廓之先判**：`blk.difference(chamfer_tri).area < 有效值` ⇒ `raise RuntimeError`（「K-9-80 ⑥ 短街廓」·含有效值）——即「平移至該線⛔ 再切到街廓仍未達」（範圍之極限 ＝ 全街廓扣截角）。
  - **上界（代倍增之上界）**：該線過街廓之最遠頂點之 `p`（`max_v ((v − S1)·n̂_S) / (sigma·(d̂·n̂_S))`·`n̂_S` ＝ 側界之法向）——逾之即⛔ 切到街廓；`d̂·n̂_S ≠ 0` 由既有之 `den_s` 之停機保證。
  - **二分**：`[S1_par, 上界]`，至多 `200` 次；`mid` 之片為 `None`／空 ⇒ `hi ＝ mid`；面積 ＜ 有效值 ⇒ `lo ＝ mid`；`0 ≤ 面積 − 有效值 ≤ K980_AREA_TOL` ⇒ 取之、止；他 ⇒ `hi ＝ mid`。
  - **⛔ 收斂** ⇒ `_stop`；**單調之設之查**：取之片須含擴大前之範圍（`buffer(eps)`·`eps` ＝ 既有之 `_corner_range_eps(dxf_quantum)`），不然 ⇒ `_stop`（非凸之多片等·`K-6` 典 `W-G.9-391` 之節之六 `56`）。
  - **浮點**：二分之序唯依 `S1_par` 與上界（換名、鏡射、旋轉之下同值至浮點）⇒ 取之 `p` 同至浮點（`F35 C8` 差 ≤ `1e-6 ㎡`）；`K980_AREA_EPS` 吸收「恰等」之浮點（`C4`）。
- **`R-4`（末端塊）**：`_area_at391(w) ＝ unary_union([frag_poly, _end_band(…, w)]).area`（與 `_end_region_R` 同式·同一 `_end_band`）。
  - `a(min_width) ≥ 有效值 − K980_AREA_EPS` ⇒ 回 `min_width`（原物·逐位同）；街廓之面積 ＜ 有效值 ⇒ 「K-9-80 ⑥ 短街廓」。
  - **倍增**：`hi ＝ 2·hi` 至 `a(hi) ≥ 有效值`；`hi` 逾街廓之外接矩形之對角線而仍未達（浮點之邊）⇒ 「K-9-80 ⑥ 短街廓」。
  - `a(hi) − 有效值 ≤ K980_AREA_TOL` ⇒ 回 `hi`；否則 **二分** `[lo, hi]` 至多 `200` 次（同上之三支）；**⛔ 收斂** ⇒ `RuntimeError`。
  - **浮點**：回傳之 `w` 由 `_end_region_R` 以同一 `_end_band` 重構 ⇒ 其面積與求解時逐位同。

### 呼叫處之全列（生產碼 `34` 檔·AST·`<O>/callsites.py`）

| 處 | 受呼 | 所在函式 | `min_build_area` |
|---|---|---|---|
| `app.py:11161` | `_end_region_R` | `_place_pool_parcels` | 傳 `min_build_area` |
| `app.py:11407` | `_end_band` | `end_block_band_width._area_at391` | ⛔ 傳 |
| `app.py:11468` | `end_block_band_width` | `_end_region_R` | ⛔ 傳 |
| `app.py:11470` | `_end_band` | `_end_region_R` | ⛔ 傳 |
| `app.py:11540` | `_end_region_R` | `end_block_side_geom` | 傳 `min_build_area` |
| `app.py:11634` | `end_block_side_geom` | `end_block_apply` | 傳 `min_build_area` |
| `app.py:18843` | `_build_corner_range_v3` | `select_corner_lots_both_sides_v12` | 傳 `_mba_pk` |
| `app.py:29199` | `_build_corner_range_v3` | `main` | 傳 `k980_mba(st.session_state, _lbl, b.get('category', ''))` |
| `verify/fixture_corner_range_k8.py:263` | `_build_corner_range_v3` | `main._build` | ⛔ 傳 |
| `verify/fixture_end_fallback.py:82` | `_end_region_R` | `run_case` | ⛔ 傳 |
| `verify/fixture_end_reserve.py:143` | `_end_band` | `main` | ⛔ 傳 |
| `verify/run_verification.py:259` | `_build_corner_range_v3` | `build_param_table.rng` | 傳 `ns['k980_mba'](fake_st.session_state, lbl, b.get('category', ''))` |
| `verify/stepg_pipeline.py:467` | `_build_corner_range_v3` | `_run_step_g_impl` | 傳 `ns['k980_mba'](ss, _crp_lbl, _crp_b.get('category', ''))` |
| `verify/wf_f4.py:1404` | `_end_region_R` | `_reshape_block` | ⛔ 傳 |
| `verify/wf_f4.py:1422` | `_end_region_R` | `_reshape_block` | ⛔ 傳 |

由：`end_block_band_width` 內與 `_end_region_R` 內之 `_end_band` 為帶之構造本身（帶寬已定）；`_end_region_R` 內之 `end_block_band_width` 以位置引數傳之（簽名之第六引數）；`verify/fixture_*.py` 三處為既有之夾具（未輸入之形之構造之斷言·⛔ 屬生產之配地路徑·單 `§三-1` ⛔ 及）；`verify/wf_f4.py` 二處 ＝ `R-9` 明除（塊 `K37` 之六 `53`·序 `26`）。

### 對 `§三-3` 各款之自查

| 款 | 自查 |
|---|---|
| `1` 字樣之錨 | `<O>/anchorcheck.py`（自寫·⛔ 量測器）：`verify/probes/*.py` 之字串常數（長 ≥ `4`）於基準 `app.py` 恰一見者，工作樹⛔ 恰一者 `0`（自捕 `3` 修後）；三指定錨 `    return rng`、`cut = _LS3([(_Tp[0] - sux * _ext`、`trial=_trial, cache=_cache, allow_forced=_allow)` 皆恰一（擴大之碼之切線改名 `_ln391`、`_tp391`；`end_block_host` 之 `min_build_area=` 以新增之一列插於該句之前一列）；新之 docstring 之折行⛔ 以「四空白＋中文」起首；基準中恰一之函式名仍恰一、新巢狀名 `_area_at391`、`_piece391` 皆⛔ 撞；`F23 wiring`（`#5`）、`F24 wiring`（`#6`）二趟皆 `rc 0` |
| `2` 突變之錨 | 新碼⛔ 照抄既有之句（`_piece391` 之 `min(…, key=lambda _g391: …)`、`_uu391([_g391 for _g391 in …])` 皆改名）；突變之器（`#19`、`#22`、`#43`、`#47` 等）二趟皆 `rc 0` |
| `3` `main` 唯增列 | `main` 之差異唯 `+1`（`min_build_area=k980_mba(st.session_state, _lbl, b.get('category', '')),`·插於 `_make_chamfer_tri_wb(b, _wh_cr),` 與 `dxf_quantum=_q_cr, …` 之間）；既有之器（含諸 `wiring`）二趟皆 `rc 0` |
| `4` 頂層 | `V-7`：`app.py` 增恰六、減 `0`、改恰十（`_WF_NS_NAMES`、`_build_corner_range_v3`、`_end_region_R`、`_place_pool_parcels`、`end_block_apply`、`end_block_host`、`end_block_side_geom`、`f3_screen_stepg_run`、`main`、`select_corner_lots_both_sides_v12`）；stepg ＝ `{_run_step_g_impl}`、`run_verification` ＝ `{build_param_table}`；`verify/selection_pipeline.py` ⛔ 動 |
| `5` ⛔ 案件字面 | `F35 wiring W7` ✅（新增或改之頂層節點 `16`·新增之案件字面 `[]`） |
| `6` 簽名 | 六既有函式皆唯於簽名之末增 `min_build_area=None`；既有參數、預設值、回傳之形⛔ 改 |


## ⑧ 三檔之全文差異

`git diff a749c78 a65e3c7 -- app.py verify/stepg_pipeline.py verify/run_verification.py` 之全文 ＝ 同目錄之 `W-G.9-391R_範圍依最小建築面積之擴大_差異.diff`（`423` 列）。

## ⑨ 工項三之 `checkidx`、`gen_fa_index`

```
$ python3 <O>/checkidx.py <repo> <repo>/.claude/rules/常設規則索引.md      # rc 0
索引列數 124；內部字樣 122；外部指標 9；不合 0
$ python3 <O>/gen_fa_index.py <repo> <O>/FX_regen.md                     # rc 0
則 124；加註節 14；列 158
$ cmp <O>/FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md   # 逐位同
```

## ⑩ 各段耗時（UTC·`2026-10-21`）

| 段 | 起訖 | 耗時 | 並行 |
|---|---|---|---|
| 接單、`§零-0`（依賴之裝與釘）、工項零、工項一 | `07:13`–`07:16` | 約 `3` min | — |
| 前置 (甲)(乙) `39` 呼叫（`/tmp/w_pre`） | `07:17`–`08:36` | 牆鐘 `4772` s（耗時之和 `9547` s） | `2`（其間撰碼之自跑另起·自捕 `5`） |
| 撰碼（工項二）與自跑（`F35`、`F23`／`F24 wiring`、`V-7`／`V-8`） | `07:20`–`07:50` | 約 `30` min | — |
| `V-*` 第一趟 `77` 呼叫（`d565c5b`） | `08:37`–`10:29` | 牆鐘 `6697` s（和 `13389` s） | `2` |
| 唯讀獨立審查一輪 | `10:30`–`10:41` | 約 `11` min | — |
| (B) 一之修、`V-*` 第二趟 `77` 呼叫（`a65e3c7`） | `10:42`–`12:35` | 牆鐘 `6760` s（和 `13522` s） | `2` |
| 工項二之推、工項三、工項四 | `12:35`– | — | — |


## 附錄　`V-1` 之諸呼叫之全文（第二趟·`a65e3c7`·`<repo>` ＝ `/tmp/w_post`）

#### `#1`　`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
  ✅ K1：{'front': 3.75, 'left': 1.0}／[]／[]
  ✅ K2：{'B1': {'front': 2.25}}／{'B1': {'front': 3.75}}
  ✅ K3：{'B1': {'front': 3.0}}
  ✅ K4：{'B1': {'front': 1.75}}／{'B1': {'front': 1.75}}／[]
  ✅ K5：{'B1': {'front': 1.75}}
  ✅ K6：{'B1': {'front': 3.75}}
  ✅ K7：{'B1': {'front': 3.15}}／[('RE', 0.4), ('RW', 0.6)]
  ✅ K8：{'B1': {'front': 0.0}}／['B1 正面道路勾選新闢，但未偵測到道路 BLOCK']／[]
  ✅ K9：{'B1': {'front': 3.75}}／['B1 正面：中心線垂距 × 2 ＝ 12.00 m，與輸入路寬 15.00 m 相差逾 0.5 m，請確認']
  ✅ K10：{'B1': {'front': 3.0882352941176467}}／{'B1': {'front': 2.625}}
  ✅ K11：['道路 BLOCK RA 未繪 CENTERLINE（B1 正面臨之），請補畫']
  ✅ K12：{'抵充地': {'100-1': 1.0, '100-3': 0.5, '100-4': 0.5}, '第33條排除': {}, 'errors': []}／['填列錯誤：甲段 100-2「第33條排除」欄填「是」，但該地號非公有地（U_LAND 公私別）', '填列錯誤：甲段 100-2「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）', '填列錯誤：甲段 100-1「第33條排除」欄填「Y」，僅得填「是」或空白', '填列錯誤：甲段 100-9「抵充地」欄填「是」，但 U_LAND 無對應資料']／['填列錯誤：地號 100-1 於 甲段、乙段 皆有，「抵充地」無從對應宗地']／{'抵充地': {}, '第33條排除': {}, 'errors': []}
  ✅ K13：[[(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]]
  ✅ K14：2.25／0.0／0.0
  ✅ K15：{'B1': {'front': 3.75}}
  ✅ K16：{'B1': {'front': 3.75}}／['尚無宗地資料（地籍），中心線是否為重劃區界⛔ 判（以輸入之路寬計）']
  ✅ K17：{'抵充地': {'100-3': 0.5}, '第33條排除': {}, 'errors': ['填列錯誤：甲段 100-1「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數', '填列錯誤：甲段 100-2「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數']}
  ✅ K18：{'B1': {'front': 0.0}}／['道路 BLOCK RA 內抵充地之面積大於扣除路口後之面積（宗地之片重疊），請檢查地籍（B1 正面臨之）']
  ✅ K19：[('壞檔', True, ['地籍資料來源讀取失敗（BadZipFile）：File is not a zip file']), ('缺欄', True, ["地籍資料來源讀取失敗（KeyError）：'段小段'"])]
  ✅ K20：前提（浮點之負）6／60；不符 []（0）
  ✅ K21：[True, True]
  ✅ K22：[True, True]
⇒ 紅 []；rc 0
`````

#### `#2`　`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`（rc `0`·stderr `0` B·139 s）

`````
  ✅ W1 頂層之新名與⛔ 案件字面：[True, True, True, True]／K974_PARAMS True／字面 []
  ✅ W2 main() 恰一處呼之：['k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)']
  ✅ W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）：
  ✅ W4 JUNCTION 存 session：
  ✅ W5 步驟 H 之段以假 st 實跑：[{'label': 'B1', 'front_width': 15.0, 'front_length': 0.0, 'front_new': False, 'left_side_width': 0.0, 'left_side_length': 0.0, 'left_side_new': False, 'right_side_width': 0.0, 'right_side_length': 0.0, 'right_side_new': False, 'front_scale': 2.25, 'left_side_scale': 0.5}]／[('warning', '⚠️ 警示甲')]／[('error', '⛔ 錯甲'), ('error', '⛔ 錯乙')]／停 False/True
  ✅ W6 verify/ 之生產碼⛔ 呼之：[]
  ✅ W7 main／calc 唯增列（具名之換列三）·頂層之相異：相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k967_pool_less', 'k967_pool_out', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']／刪列 3
⇒ 紅 []；rc 0
`````

#### `#3`　`python3 verify/probes/probe_WG9385_k974.py run <repo>`（rc `0`·stderr `0` B·431 s）

`````
  各面之尺度：R4 front 0.0／left 1.0／right 1.0；R6 front 2.0／left None／right 1.0；R5 front 2.0／left 1.0／right None；R2 front 2.0／left 1.0／right None；R3 front 2.0／left None／right 1.0；R1 front 0.0／left 1.0／right 1.0
  ✅ R1 尺度 ＝ 快照之負擔尺度_輸入：不符 []／警示 []／錯誤 []
  ✅ R2 calc 之列給尺度與否逐值同：741.76／741.76
  ✅ R3 抵充地之模擬（628-34·RD1）：RD1 1082.2651／628-34 之片 131.6000／比例 0.878403／負擔路寬 7.0272／期 1.513613、0.756806／得 1.513616、0.756808
  ✅ R4 私有地填「是」⇒ 填列錯誤：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']
  ✅ R6 二欄之結果之存與換檔：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']／[]
  ✅ R5 JUNCTION 之模擬（RD1 之一端）：框內 89.6652／比例 0.867420／期 1.469679／得 1.469679
⇒ 紅 []；rc 0
`````

#### `#4`　`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
── 手冊先行（K-9-53 ①）之各支 ──
  ✅ K1 跨分配線（所鄰之已配得之宗恰一）⇒ 整筆併入、出 build、帶 段三併出
  ✅ K2 跨分配線（所鄰之已配得之宗分處二街廓）⇒ 併入應分配面積（G）較大者
  ✅ K3 （K-9-67）二者之 G 並列 ⇒ 重劃前面積同（300）⇒ 暫編地號小者 E1(1)；E1 之重劃前面積 250 ⇒ X1(2)
  ✅ K4 建地片與同街廓之已配得之宗相鄰 ⇒ 依手冊整筆併入之（K-9-58 ③·W-G.9-380）
  ✅ K5 道路·兩側皆有 ⇒ 依中心線切分、各半併入該側之宗（a′ × 半之面積比）
  ✅ K6 道路·唯一側有 ⇒ 整筆往該側（所鄰之街廓依中心線分側）
  ✅ K7 道路·兩側皆無 ⇒ 未併、帶 段三餘量 ＝ a（視同無同歸戶）
  ✅ K8 道路片全在無已配得之側（⛔ 鄰有之側之街廓）⇒ 仍整筆往有之側
  ✅ K9 隔道路之分不到之建地 ⇒ 隨道路片往另一側之宗
  ✅ K10 公設地 ⇒ 平分於其合併群所及之已配得之街廓（群外之已配得之宗⛔ 與）
  ✅ K11 公設地不相連於任何已配得之宗 ⇒ 未併、帶 段三餘量 ＝ a
  ✅ K12 路口之道路片（鄰三街廓以上、含公設地）⇒ 比照公設地平分
  ✅ K13 落點四層瀑布：① 同原地號者先於較近者；② 皆非同原地號 ⇒ 質心距近者；③ 等距 ⇒ G 大者；④ 皆同 ⇒ 暫編地號
  ✅ K14 （K-9-66）整批不過 ⇒ 建地整筆不過 ⇒ 按比例部分併入 10；剩下 50 依 K-9-51（他街廓之已配得之宗·距離近者先）
  ✅ K15 可拆分之片之最大面積（0.01 ㎡ 之格）；其餘 ⇒ K-9-51 皆無 ⇒ 入合併單位、帶 段三部分併出／段三餘量
  ✅ K16 併入後配地中止 ⇒ 不過（記其由·⛔ 停機）
  ✅ K17 帶段三之鍵之片⛔ 受理
  ✅ K18 無任何配得土地之地主：同號之連通分量之再試未成 ⇒ 回輸入之同一物件、紀錄唯再試之列（K-9-73 ④）
  ✅ K19 入池閘之合併單元：取代後之配地全同 ⇒ 取代；相異 ⇒ ⛔ 取代（記之）
  ✅ K20 調配之輸入（⛔ 改·沿用段三之鍵）：併出 ⇒ 原位次配地（所屬單元『段三併入 …』）；餘量 ⇒ 入合併單位；待同歸戶併入 ＝ 空
  ✅ K21 公設地調配之 temp（⛔ 改·沿用段三之鍵）：併出而無餘量 ⇒ 去之；部分併出 ⇒ 依餘量之比縮之
  ✅ K22 a′ 之折算（街廓之地價比）
  ✅ K23 （K-9-66）整批不過時：建地先（全入）、道路次（按比例）、公設地未試；剩下之列於諸輪之後
  ✅ K24 旗標 WV_K953：未設／on ⇒ 真；off ⇒ 偽；他值 ⇒ 停機
  ✅ K25 可為受詞之片之歸戶於 build 皆無片（例：歸戶表為空）⇒ ⛔ 試算配地、回輸入之同一物件、紀錄 ＝ []
  ✅ K26 試算之摘要：抵費地之形放不下最小建築面積之矩形 ⇒ 配餘地不合格一處；保留 ⇒ 保留宗與其 G；餘⛔ 計
  ✅ K27 入池閘之單元：成員（缺 ⇒ 自身）；成員 ≥ 2 者為單元（深拷貝）
  ✅ K28 K-9-51 之候選含 x 之本街廓之已配得之宗（與 x ⛔ 相連·距離 0）⇒ 先試併之、過 ⇒ 併入、出 build（K-9-55）；其檢核不過 ⇒ 記未成、續試他宗；皆不行 ⇒ 入合併單位（補令二·乙案）
  ✅ K29 入池閘之旗標 off（WV_K929_6）⇒ 手冊先行不辦（harness 與畫面皆回輸入之同一物件、紀錄 []、畫面⛔ 呼叫 st）；二旗標皆判（WV_K953 off 而 WV_K929_6 非法 ⇒ 停機）
  ✅ K30 畫面：旗標值非法（WV_K953 或 WV_K929_6）⇒ f3_k6b_stage3_error ＝ （手冊先行）…、st.error ＋ st.stop、⛔ 寫紀錄
  ✅ K31 入池閘之單元之取代後：build ⊂ temp（同物件）、temp 中之標的 ＝ 單元（帶入池閘併入）、他成員仍在 temp 而⛔ 在 build
  ✅ K32 K-9-51 之候選同距離（0）：本街廓之宗居先於他街廓之宗（G 較大者亦然·K-9-55 之二）；本街廓無之、或其檢核不過 ⇒ 他街廓之宗
  ✅ K33 K-9-51 之本街廓之候選與 x 相連（C0 之後始為已配得）、⛔ 相連 ⇒ 皆本街廓之宗居先、併入之（W-G.9-380）
  ✅ K34 K-9-51 之本街廓之候選之成員取當下之試算：其單元於 C0 之後始含與 x 相接之片、該片⛔ 與 x 相接 ⇒ 皆併入之（W-G.9-380）；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K35 本街廓之候選：G 較小者（H2(1)）與 x 相接 ⇒ 相接者（距離 0）先、併入之（K-9-51·W-G.9-380）；後者⛔ 與 x 相接 ⇒ 併入 G 較大者
  ✅ K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入
  ✅ K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入其計畫之受併宗
  ✅ K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片——⛔ 停機、依計畫併入（W-G.9-380）；⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（程式自我檢查·K-9-57 ⑧）
  ✅ K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）
  ✅ K41 跨二街廓之小片 S(1) 唯與已配得之宗 R(1) 之成員 Q(1)（⛔ R(1) 之自身之形）相連 ⇒ 手冊先行連同成員看之、依手冊整筆併入 R(1)（巳 ③）
  ✅ K42 計畫之同街廓相鄰之已配得之宗（Q1(1)·X1(2) 為他地號 ⇒ ⛔ 第 31 條第 3 款）之併入之檢核不過（BA 之容量 0）⇒ 記未成、依 K-9-51 併入他街廓之宗（X1(2)）
  ✅ K43 同街廓相鄰（Q1(1)）與他街廓之同一原地號（X1(2)）並存 ⇒ 第 31 條第 3 款先（K-9-73）：X1(2) 之 G 400 ⇒ X1(2)；Q1(1) 之 G 400 ⇒ 仍 X1(2)
  ✅ K44 同街廓相鄰之已配得之宗二（A1(1) G 300、A2(1) G 200）⇒ 應分配面積大者 A1(1)（K-9-61 ①⑦·K-9-67）
  ✅ K45 （K-9-73 ⑤）與他街廓之已配得之宗（X1(2)·他地號）相連而無同一原地號者 ⇒ ⛔ 依手冊併入（計畫無受併宗·未併）
  ✅ K46 （K-9-73 ③⑤⑦）分不到之 C1(1) 與他街廓之同一原地號 C1(2) 及他地號 G1(1)（G 較大）皆相連、且隔自己之道路片 R1(1) ⇒ 第 31 條第 3 款（唯同一原地號）先 ⇒ C1(2)
  ✅ K47 （K-9-73 ⑥·手冊道路用地分配原則 1）分不到之 C1(1) 隔自己之道路片 R1(1)（另一側 X1(2)），而同街廓有已配得之C9(1) 與之相連 ⇒ 道路兩側皆有己地（道路片依中心線切分·⛔ 隨道路往另一側）⇒ 併入同街廓相鄰之 C9(1)
  ✅ K48 （K-9-73 ⑤）分不到之 X1(1) 與同街廓之 Q1(1) 及他街廓之他地號 X1(2)（G 400·較大）皆相連 ⇒ 他地號之相連⛔ 入比較 ⇒ 併入同街廓相鄰之 Q1(1)
  ✅ K49 （K-9-73 ④）X1(1)（BA 60）與 X1(2)（BB 300）皆不配地 ⇒ X1(1) 整筆併入 G 大之 X1(2)；併後 X1(2)（360）配地 ⇒ 成：X1(1) 出 build、帶 段三併出 ['X1(2)']；X1(2) 之 面積_m2 60、帶 第31條第3款併入 ['X1(1)']
  ✅ K50 （K-9-75）受併之片依應分配面積（不配地紀錄之 G）：X1(1) 之 G 500 ＞ X1(2) 之 300 ⇒ X1(2) 併入 X1(1)（⛔ 依面積）
  ✅ K51 （K-9-75·K-9-67）G 並列（皆 100）⇒ 重劃前面積大者（X1(2) 300 ＞ X1(1) 60）受併（⛔ 暫編地號之序）
  ✅ K52 （K-9-29）再試之併入量依 a′（BA 之地價 2 倍）⇒ 120
  ✅ K53 （K-9-75 ②）同一原地號跨三街廓（X1(1)·BA ─ X1(2)·BB ─ Z1(1)·BD·X1(1) 與 Z1(1) ⛔ 直接相接）皆不配地 ⇒ 餘二片皆併入 G 最大之 Z1(1)（400）；併後 760 配地 ⇒ 成
  ✅ K54 （K-9-75 ②）三街廓之同號之連通分量而 Z1(1) 已配得 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1)（⛔ 與 Z1(1) 直接相接）亦併入 Z1(1)
  ✅ K55 （K-9-73 ⑥）同一原地號而隔道路之 C1(1)（BC）⛔ 入同號之連通分量 ⇒ 再試唯 X1(1) → X1(2)
  ✅ K56 再試之受詞存在而試算未回 dropped ⇒ 停機（⛔ 以空代之）
  ✅ K57 同號之片 X1(2) 為已配得之宗 Y1(1) 之成員 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1) 併入 Y1(1)
  ✅ K58 （K-9-75）同一原地號之公設地之片（P1(1)·PK·與 X1(2) 相接）⛔ 入同號之連通分量 ⇒ 再試照行（X1(1) → X1(2)）
  ✅ K59 （K-9-73 ⑨）受併之片配地而「不影響原位次」之檢核不過（BB 之配餘地不合格）⇒ 未成（⛔ 施）
  ✅ K60 再試成而受併之片 X1(2) 為同地主之 Y1(1)（宿主）之單元之成員 ⇒ 單元之取代（X1(2) 出 build）之後，Y1(1) 之單元帶 第31條第3款併入 ['X1(1)']（⛔ 失）
  ✅ K61 （K-9-71）BC 之使用分區（商業區）異於片之所屬街廓 BA ⇒ 五級排後：剩下 50 併入 BD 之 Z1(1)（⛔ 距離近之 C1(1)）
  ✅ K62 （K-9-71）五級皆同而 BC 較深（40）⇒ 排後 ⇒ Z1(1)；BC 深 30.1（同深之容差 0.1 m 內）⇒ 依距離 ⇒ C1(1)
  ✅ K63 （K-9-71）BD 之最小建築面積往大（100）⇒ 排後而⛔ 淘汰：C1(1)（BC 容 0）不過 ⇒ 續試 Z1(1) 成
  ✅ K64 他街廓之候選二以上（BC、BD）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）
  ✅ K65 他街廓之候選唯一（BB·C1 去之）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（K42 之形）
  ✅ K66 五級之屬性缺片之所屬街廓（BA）⇒ 停機
  ✅ K67 五級之屬性之回呼唯於須比時呼之、且一次（K61 之形 ⇒ 1；Z1 非 g1 ⇒ 他街廓唯一 ⇒ 0）
  ✅ K68 k971_key5 ＝ adj_candidate_lists 之建地軌之八鍵之前六（合成之屬性三組·七街廓·逐對 126）
  ✅ K69 再試成而受併之片 X1(2) 為 Y1(1) 之單元之成員；取代後之配地相異（未取代）⇒ 當下之態⛔ 變：X1(2) 仍在 build 且帶標記、宿主 Y1(1)⛔ 帶鍵
  ✅ K70 他街廓唯一（BC）而其候選二宗（C1(1)、C9(1)·皆 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行 ⇒ C1(1)
  ✅ K71 五級與深度皆同之他街廓 BC（距 10）、BD（距 20）、BZ（距 1·名序最後）⇒ 依距離 ⇒ BZ 之 Z9(1)（⛔ 依街廓名）
  ✅ K72 （K-9-71）正面路寬：BA 8、BC 15（往寬）、BD 6（往窄）⇒ 二者皆異、級距 BD 先（往窄先於往寬）⇒ Z1(1)
  ✅ K73 （K-9-71）正面道路：BC 臨他路（RX）⇒ 排後 ⇒ Z1(1)
  ✅ K74 五級之屬性之回呼回非 dict ⇒ 停機
  ✅ K75 （K-9-71）道路之片 R1(1)（RD）之北半部分併入 X1(2)（BB 容 33.333）後，剩下 16.67 之他街廓之候選 ＝ C1(1)（BC·距 0·使用分區 商業區）、Z1(1)（BD·距 10）⇒ 道路之片照距離 ⇒ C1(1)（⛔ 依五級排 Z1(1) 先）
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 75／75
⇒ 紅 []；rc 0
`````

#### `#5`　`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`（rc `0`·stderr `0` B·32 s）

`````
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（608）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
`````

#### `#17`　`python3 verify/probes/probe_WG9363_k953.py run <repo>`（rc `0`·stderr `0` B·501 s）

`````
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.47／ΣG 之變 2934.53（和 ≤ 0.1）True
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.83／ΣG 之變 3663.88（和 ≤ 0.1）True
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
`````

#### `#6`　`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`（rc `0`·stderr `0` B·32 s）

`````
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（610）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
`````

#### `#13`　`python3 verify/probes/probe_WG9367_adj4.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
── 規格步 4 乙（K-9-53 ②·第一趟）之各支 ──
  ✅ K1 旗標：未設／空／' On ' ⇒ True；off／OFF ⇒ False；他值 ⇒ 停機
  ✅ K2 無受詞 ⇒ 回輸入之同一物件、紀錄 []、⛔ 試算；build 片不在 temp ⇒ 停機（受詞為空亦然）
  ✅ K3 整體成：名單首 BA 無其已配得之宗 ⇒ 略過；BB 之受併宗 X1(2)（同原地號）；三片皆併、建地片自 build 去、輸入⛔ 改、build ⊆ temp（同物件）
  ✅ K4 整體不過（BB 之容量 150）⇒ 逐片：建地整筆成、道路片取最大面積（0.01 之格）、公設片未成；剩下續往名單之下一街廓 BD（整體成·受併宗 Z1(1)）
  ✅ K4b 整體不過之列記其由（配餘地不合格）
  ✅ K5 名單盡而有剩下 ⇒ 剩下之列（留於合併單位）；部分併出者之三鍵（段三部分併出·段三餘量）
  ✅ K6 全不容 ⇒ 每街廓整體＋三逐片皆未成、剩下 ＝ 全部；⛔ 改宗地（建地片仍在 build·無鍵·無增）
  ✅ K7 受併宗之序（同街廓有二宗）：① 同原地號居先（距離較遠亦然）② 距離近 ③ 同距離 ⇒ G 大 ④ 同 G ⇒ 重劃前面積大（K-9-67）⑤ 再同 ⇒ 暫編地號小
  ✅ K8 前已有段三之三鍵之片：其剩下 ＝ 段三餘量；全併 ⇒ 段三併出合之、去部分二鍵；部分 ⇒ 段三部分併出合之、段三餘量 ＝ 新剩下
  ✅ K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（程式自我檢查·K-9-57 ⑧·`W-G.9-370` 之訊息）
  ✅ K10 現態之配地中止 ⇒ 停機
  ✅ K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ 共同負擔用地（相異）；無名單 ⇒ 停機；名單重複 ⇒ 停機
  ✅ K12 GB-199：受併宗之序之距離取 slice_geom 之原形（temp 之形縱異亦然）；片之原形缺 ⇒ 停機
  ✅ K13 a′ 折算（K-9-45 二）：併入量 ＝ 來源面積 × p(來源) ÷ p(受併宗)；最大面積之格取來源面積；三鍵之部分併出記來源面積
  ✅ K14 「不影響原位次」：併入使同街廓原保留之宗不保留 ⇒ 不過（整體與逐片皆然）
  ✅ K15 GB-201（手冊先行）：計畫之受併宗於當下之試算未保留 ⇒ 停機（可拆分之片／整筆之建地片）
  ✅ K16 三旗標（WV_ADJ4／WV_K953／WV_K929_6）之任一 off ⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 呼叫 st
  ✅ K17 三旗標之任一其值非法 ⇒ harness 停機；畫面 ⇒ f3_k6b_stage3_error ＝ （第一趟）…、st.error、st.stop、⛔ 寫紀錄
  ✅ K18 adj4_plan：無受詞 ⇒ []；唯公設軌 ⇒ 正面道路之缺以佔位代之、名單依距離；建地軌 ⇒ 停機（正面道路無識別符）
  ✅ K19 adj4_depth_of：取 f3_alloc_depth_by_label（缺 ⇒ {}）；回新 dict
  ✅ K20 adj4_trial_state：摘要 ＋ err ＋ 成員與單元（成員 ≥ 2 者為單元·深拷貝）
  ✅ K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True
  ✅ K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st
  ✅ K23 R-8 之止：整體不過（他街廓之原保留之宗失·非單調之玩具）而逐片皆成 ⇒ 諸片皆無剩下 ⇒ 止於本街廓（⛔ 往名單之次街廓 BD）
  ✅ K24 （K-9-66）T 含建地片之所屬街廓：全數併出使 BA 之 Q1 失 ⇒ 整體與建地之全併皆不過；按比例 59.99（留 build）⇒ 過；道路、公設地未試
  ✅ K25 （K-9-66）同類按比例：建地全入後道路容 190 ⇒ R9 126.67、R1 63.33（各乘 190／300）；列依剩下大者先
  ✅ K26 R-12：併入後之配地中止 ⇒ 不過（記其由）；整體不過 ⇒ 逐片（公設片取最大面積）
  ✅ K27 R-10′（K-9-57 ⑧·程式自我檢查）：同一輪中併入某街廓之前，以當下之試算查其所受之建地片——前一街廓之併入使之已為已配得之宗（依既定機制不會發生·玩具以非單調之回呼造之）⇒ 停機（⛔ 靜默併出）；對照 ⇒ 二街廓皆整體成
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 28／28
⇒ 紅 []；rc 0
`````

#### `#18`　`python3 verify/probes/probe_WG9367_adj4.py run <repo>`（rc `0`·stderr `0` B·695 s）

`````
  ✅ R1@3.5：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@3.5：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@3.5：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6700（Σ|ΔG| 7.6900）／ΣΔ抵費地 -7.6500（和 +0.0200·≤ 0.1）
  ✅ R4@3.5：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@3.5：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
  ✅ R1@0.0：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@0.0：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@0.0：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6400（和 +0.0400·≤ 0.1）
  ✅ R4@0.0：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@0.0：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
⇒ 紅 []；rc 0
`````

#### `#7`　`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`（rc `0`·stderr `0` B·3 s）

`````
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
`````

#### `#19`　`python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>`（rc `0`·stderr `0` B·9 s）

`````
  ✅ M00 —·基準（⛔ 突變）：錨 1 見；紅 []；所指 []
  ✅ M20 R-12·原保留之宗之判去之：錨 1 見；紅 ['K14', 'K23', 'K24']；所指 ['K14']
  ✅ M21 R-12·配餘地不合格之判去之：錨 1 見；紅 ['K4', 'K4b', 'K5', 'K6', 'K8', 'K13', 'K25']；所指 ['K4b']
  ✅ M23 R-12·併入後之配地中止改為過：錨 1 見；紅 ['K26']；所指 ['K26']
  ✅ M24 R-13·段三併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M25 R-13·段三部分併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M26 R-13·全併⛔ 去部分二鍵：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M27 R-13·段三餘量之值誤：錨 1 見；紅 ['K5', 'K8', 'K13']；所指 ['K8']
  ✅ M30 R-16·GB-201 之判恆過：錨 1 見；紅 ['K15']；所指 ['K15']
⇒ 突變 8（另基準一）；紅 []；rc 0
`````

#### `#62`　`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`（rc `0`·stderr `0` B·4 s）

`````
── 合成對照（AST 抽出之 adj_intake 等）──
  ✅ K1 G 之加總較大者：得 'B2'　期 'B2'
  ✅ K2 G 相同 ⇒ 重劃前面積之合計較大者：得 'B1'　期 'B1'
  ✅ K3 G 以 0.01 ㎡ 為單位相同 ⇒ 重劃前面積：得 'B2'　期 'B2'
  ✅ K4 G 以 0.01 ㎡ 為單位相異 ⇒ G：得 'B1'　期 'B1'
  ✅ K5 G、重劃前面積皆同 ⇒ 最小之暫編地號較小者：得 'B1'　期 'B1'
  ✅ K6 G 逐街廓加總（⛔ 逐筆）：得 'B1'　期 'B1'
  ✅ K7 合併單元之 G 只計一次：得 'B2'　期 'B2'
  ✅ K8 合併單元之重劃前面積計其諸成員：得 'B1'　期 'B1'
  ✅ K9 重劃前面積 ＝ 原有面積（部分併出之剩下·⛔ 分攤登記面積）：得 'B2'　期 'B2'
  ✅ K10 三街廓：二者並列 ⇒ 其後之鍵：得 'B3'　期 'B3'
  ✅ K11 皆同 ⇒ ⛔ 停機：得 True　期 True
  ✅ K12 原街廓之據 ＝ 各街廓之 G 之加總：得 {'B1': 35.0, 'B2': 30.0}　期 {'B1': 35.0, 'B2': 30.0}
  ✅ K13 暫編地號以字典序比：得 'B1'　期 'B1'
  ✅ K14 單一街廓：得 'B2'　期 'B2'
  ✅ K15 街廓內之最小之暫編地號亦以字典序：得 'B1'　期 'B1'
  ✅ K16 重劃前面積先加後捨：得 'B1'　期 'B1'
  ✅ K17 重劃前面積以 0.01 ㎡ 為單位相同 ⇒ 暫編地號：得 'B2'　期 'B2'
  ✅ K18 重劃前面積 ＝ 原有面積（入池閘之帳之剩下）：得 'B2'　期 'B2'
⇒ 紅 []；rc 0
`````

#### `#63`　`python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`（rc `0`·stderr `0` B·3 s）

`````
  ✅ X1 adj_intake 呼叫 k967_rank（呼叫 1）
  ✅ X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise（[]）
  ✅ X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']）
  ✅ X4 adj_intake 內⛔ 案件字面（[]）
  ✅ X5 生產碼 app.py 以外之 33 檔對基準相異 0（相異 []）
⇒ 紅 []；rc 0
`````

#### `#64`　`python3 verify/probes/probe_WG9387_k961h.py run <repo>`（rc `0`·stderr `0` B·375 s）

`````
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.81、R3 92.46｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R3｜據 R2 27.55、R3 28.34｜外部錨 R3
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.81、R3 88.63｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R2｜據 R2 27.55、R3 24.88｜外部錨 R2
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
⇒ 紅 []；rc 0
`````

#### `#65`　`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
── selftest（合成·K-9-61 ①②③⑥）──
  ✅ K1 二受併宗皆與道路片相鄰 ⇒ 應分配面積大者（D1 ⇒ A1）
  ✅ K2 道路片唯與其一相鄰 ⇒ 該宗（D2 ⇒ A2·縱 G 140 ＜ 160）
  ✅ K3 應分配面積以 0.01 ㎡ 相同 ⇒ 重劃前面積大者（D1 ⇒ A2）
  ✅ K4 再同 ⇒ 暫編地號小者（D1 ⇒ A1）
  ✅ K5 無本段受併宗之街廓之原位次配得之宗二以上 ⇒ 相鄰者先 → G（D1 ⇒ A1／S2；D3 ⇒ S3）
  ✅ K6 有受併宗之街廓內另有原位次配得之宗 ⇒ 照配、與 D2 相鄰而承受之（D1 ⇒ A1·D2 ⇒ K）
  ✅ K7 所鄰之配得街廓二 ⇒ 承受之宗之 G 大之一側（X ⇒ C1·170 ＞ 160）
  ✅ K8 二側之 G 以 0.01 ㎡ 相同 ⇒ 重劃前面積大之一側（X ⇒ C1）
  ✅ K9 所鄰二以上而其一為本街廓 ⇒ 本街廓之宗（X ⇒ X9）
  ✅ K10 所鄰為零而經同一地主之道路片臨道路另一側之配得街廓 ⇒ 併入該側之宗（Y、D1 ⇒ A1）
  ✅ K11 所鄰為零而無同一地主之道路片相鄰 ⇒ 第 5 項之輪（Y ⇒ A1）
  ✅ K12 所鄰為零而本街廓另有已配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Z）
  ✅ K13 二受併宗之一於現態未保留 ⇒ 停機（取得即鎖定·⛔ 還原）
  ✅ K14 公設片平分，每街廓之一份由擇定之一宗整份承受（P ⇒ A1／S3）
  ✅ K15 承受之宗唯一者⛔ 須 G
  ✅ K16 須擇而 alloc_state 未回 G ⇒ 停機
  ✅ K17 相鄰以宗連同其於本段整筆併入之片判之（P5 ⇒ A1）
  ✅ K18 經道路片而臨者隨該道路片之受者（Y、D1 ⇒ K；D9 ⇒ A1）
  ✅ K19 道路片之端所臨之街廓⛔ 為道路之另一側（Y ⇒ A1·⛔ E1）
  ✅ K20 本街廓有同一地主之他群之配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Q）
  ✅ K21 所鄰為零而依第 5 項者其來源量為整筆、整筆併出（A1 130·Y 出 build）
  ✅ K22 重劃前面積扣段三部分併出（D1 ⇒ A1）
  ✅ K23 重劃前面積扣同一試算之入池閘之帳（D1 ⇒ A1）
  ✅ K24 經道路片之判以該建地與道路片共邊為準（Y ⇒ 第 5 項；Y2 ⇒ A1）
  ✅ K25 已為街角之合併所併出之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ E1）
  ✅ K26 同一街廓經二道路片而其受者異 ⇒ `k967_rank`（Y ⇒ K）
  ✅ K27 經道路片而臨二側 ⇒ 各側以其經道路片之受者比（Y ⇒ F1）
  ✅ K28 穿越之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ A1；C ⇒ (c)）
  ✅ K29 近半、遠半皆臨之街廓（路衝）⛔ 為道路之另一側（Y ⇒ 第 5 項 ⇒ E1；D1 ⇒ (b) E1）
  ✅ K30 第 5 項之本街廓之同一地主之配得之宗二以上 ⇒ 應分配面積大者（Y ⇒ Q·⛔ 近之 Q2）
  ✅ K31 路衝之扣以道路片為單位（Y ⇒ 經 D5 ⇒ E2）
  ✅ P0 逐項擾動恰該項紅 31／31
⇒ 紅 []；rc 0
`````

#### `#66`　`python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`（rc `0`·stderr `0` B·2 s）

`````
── 接線（工作樹之 app.py 對基準 fd88f64）──
  ✅ X1 四停機之字樣皆去（殘 []）
  ✅ X2 `_recv_of(b, y)` 之形與其 5 呼叫皆二引數
  ✅ X3 頂層之相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X4 ⛔ 案件字面（[]）
  ✅ X5 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
`````

#### `#69`　`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
  ✅ K1 程式之停機：回 RuntimeError·登記全文（⛔ 截）
  ✅ K2 ⛔ 帶號 ⇒ 停機、⛔ 登記
  ✅ K3 號之邊界（前接英數或連字號者⛔ 號；無數字者⛔ 號）
  ✅ K4 新登記 零／一／二 ⇒ ⛔ 拋／拋其全文／拋其首者
  ✅ K5 巢狀之試算以長度分之
  ✅ K6 入池閘之併入後之試算立程式之停機 ⇒ 上拋
  ✅ K7 對照：配地中止（⛔ 帶號）⇒ 照舊為不過
  ✅ K8 基底（無停機）：X 依手冊併入街角第 1 宗 C
  ✅ K9 換名：K6／K7／K8 之果除名稱外同
  ✅ K10 鏡射：K6／K7／K8 之果除名稱外同
  ✅ K11 旋轉 37°·TWD97：K6／K7／K8 之果除名稱外同
  ✅ K12 鏡射 ＋ 旋轉 213°·TWD97·換名：K6／K7／K8 之果除名稱外同
  ✅ K13 末端塊合併再試之試算立程式之停機 ⇒ 上拋
  ✅ K14 對照：末端塊之試算之配地中止 ⇒ 照舊記試算中止
  ✅ K15 試算之前之登記⛔ 波及（K7 於 K1〜K5 之登記之後）
  ✅ K16 上拋之訊息為全文（號在 1500 字之後）
  ✅ P0 判式自驗 16／16
⇒ 紅 []；rc 0
`````

#### `#70`　`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`（rc `0`·stderr `0` B·153 s）

`````
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 10（基準之帶號 10）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'adj_intake', 'end_block_apply', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'main', 'select_corner_lots_both_sides_v12']／不合 []）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
`````

#### `#71`　`python3 verify/probes/probe_WG9389_trialstop.py run <repo>`（rc `0`·stderr `0` B·478 s）

`````
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
`````

#### `#72`　`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
  ✅ L1 合併再試（①）所得之宗⛔ 保留 ⇒ 停機（⛔ 還原）
  ✅ L2 經道路片（②）所得者⛔ 保留 ⇒ 停機
  ✅ L3 二端皆⛔ 保留 ⇒ 停機（訊息具二者）
  ✅ L4 先成者保留而後成之右端者⛔ 保留 ⇒ 停機（訊息具後者、⛔ 具保留者）
  ✅ L5 競合（題二）之所取之一端⛔ 保留 ⇒ 停機
  ✅ L6 競合（題一·切半二端各配一宗）而皆⛔ 保留 ⇒ 停機
  ✅ L7 皆保留 ⇒ 同改前、鎖定之宗受併入、試算 3（步驟 10 沿用其查之試算）
  ✅ L8 有成者而該群無待後處理之土地 ⇒ 仍查（試算 1）
  ✅ L9 查之試算中止 ⇒ 停機（無從判定）
  ✅ L10 無成者 ⇒ ⛔ 查（試算 0）
  ✅ L11 L7 之換名、左右鏡射、旋轉並移至 TWD97 之尺度 ⇒ 同 L7
  ✅ L12 成者皆保留而非成者之宗⛔ 保留 ⇒ ⛔ 停機
  ✅ L13 紀錄⛔ 含回原狀之列
  ✅ L14 題一 4 之照配（後處理之成）⛔ 為鎖定之受詞 ⇒ ⛔ 停機
  ✅ P0 判式自驗 14／14
⇒ 紅 []；rc 0
`````

#### `#73`　`python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302`（rc `0`·stderr `0` B·2 s）

`````
── 接線（工作樹之 app.py 對基準 2aa6302）──
  ✅ X1 舊停機之字樣去之（殘 0）、還原之字樣去之（{'回原狀': 0, '還原後仍出現': 0}）、鎖定之查之字樣 3（期 ≥ 1）
  ✅ X2 頂層之相異 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_side_geom', 'f3_screen_stepg_run', 'k6b_stage3_run', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X3 ⛔ 案件字面（[]）
  ✅ X4 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
`````

#### `#74`　`python3 verify/probes/probe_WG9390_k961r.py run <repo>`（rc `0`·stderr `0` B·376 s）

`````
  ✅ R1@3.5：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 1·回原狀之列 0·其檢核 0·段三之成者 3·G 值列 35）
  ✅ R1@0.0：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 0·回原狀之列 0·其檢核 0·段三之成者 0·G 值列 36）
  ✅ R0 諸退縮之段三之成者之和 3（[3, 0]·期 ≥ 1·其查已行）
⇒ 紅 []；rc 0
`````

#### `#75`　`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`（rc `0`·stderr `0` B·1 s）

`````
  ✅ C1 未輸入 ⇒ 100.5
  ✅ C2 輸入 0 ⇒ 逐位同 C1
  ✅ C3 輸入 100 ⇒ 逐位同 C1
  ✅ C4 輸入恰 100.5 ⇒ 逐位同 C1
  ✅ C5 輸入 150 ⇒ 面積∈[150,150.01]·遠側 x＝5.15·∥SIDE_LINE·含 C1
  ✅ C6 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ C7 輸入 −1 ⇒ 停機
  ✅ C8 C5 之旋轉 37°·鏡射·TWD97 ⇒ 面積同 C5
  ✅ C9 側街斜交（∦ 宗地分配線）輸入 200 ⇒ 面積∈[200,200.01]·遠側界線 ∥ SIDE_LINE（Δx＝6）
  ✅ E1 未輸入 ⇒ R_end 255·內側界 13.5（buf 3.5）
  ✅ E2 輸入恰 255 ⇒ 逐位同 E1
  ✅ E3 輸入 300 ⇒ R_end∈[300,300.01]·內側界 x＝15
  ✅ E4 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ E5 E3 之旋轉·鏡射·TWD97 ⇒ R_end 同 E3
  ✅ E6 _end_region_R 之未輸入與 0 ⇒ R_end 逐位同（255）；end_block_band_width 之 0 ⇒ 停機
  ✅ T1 距 0.02 ⇒ ⛔ 停
  ✅ T2 距恰 0.01 ⇒ 停
  ✅ T3 距 0.005 ⇒ 停
  ✅ T4 重疊 ⇒ 停（訊息具二範圍之名）
  ✅ T5 唯一範圍或含 None ⇒ ⛔ 停
  ✅ T6 三範圍而唯其中二者相接 ⇒ 停
  ✅ K1 有效值之序（K-9-1 ⑨）：街廓覆寫 → 分區底 → 0；session 無鍵或 None ⇒ 0
  ✅ P0 判式自驗 22／22
⇒ 紅 []；rc 0
`````

#### `#76`　`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`（rc `0`·stderr `0` B·25 s）

`````
── 接線（工作樹對基準 a8657c4）──
  ✅ W1 _build_corner_range_v3 之呼叫 4（期 ≥ 4）皆傳 min_build_area：皆傳
  ✅ W2 諸呼叫之數 [('end_block_side_geom', 1), ('end_block_host', 2), ('_place_pool_parcels', 2)]（期 ≥ 1、≥ 2、≥ 2）皆傳 min_build_area：皆傳
  ✅ W3 末端帶之單一真相源 {'_place_pool_parcels→_end_region_R': 1, '_place_pool_parcels→_end_band': 0, '_end_region_R→end_block_band_width': 1, 'end_block_band_width 之呼叫（全檔）': 1}（期 1、0、1、1）
  ✅ W4 min_build_area 之值皆為 k980_mba（呼叫 8·期 ≥ 8·不合 []）、v12 之 _mba_pk 之賦值 True、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（4／基準 4）、k980_mba 之分區之引數為字面者 []（期無）
  ✅ W5 k980_range_touch_check 之呼叫 [('select_corner_lots_both_sides_v12', 1), ('f3_screen_stepg_run', 1), ('stepg:_run_step_g_impl', 1)]·app.py 全檔 2（期各 1·app.py 全 2）、其範圍之名齊全 [True, True, True]（期三真）
  ✅ W6 頂層之名之增 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']（期 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']）、減 []
  ✅ W7 新增或改之頂層節點（16）內新增之案件字面 []
  ✅ W8 逐層照傳 min_build_area 皆照傳
  ✅ W9 引擎經 ns 取之新名 ['k980_mba', 'k980_range_touch_check'] ⊆ _WF_NS_NAMES（漏 []）
⇒ 紅 []；rc 0
`````

#### `#77`　`python3 verify/probes/probe_WG9391_k980x.py run <repo>`（rc `0`·stderr `0` B·157 s）

`````
  ✅ R1@3.5 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28}·err None）
  ✅ R2@3.5 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}·不合 []）
  ✅ R1@0.0 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28}·err None）
  ✅ R2@0.0 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 124.94, 'R2': 162.99, 'R3': 163.8, 'R4': 126.08, 'R5': 156.5, 'R6': 262.28}·不合 []）
⇒ 紅 []；rc 0
`````

#### `#9`　`python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>`（rc `0`·stderr `0` B·2 s）

`````
── 受詞：['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows'] ⇒ 缺 [] ──
── 合成對照（樁·期值出自規格單 §三）──
  ✅ T1a 段二序為空之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  ✅ T1b 合併再試恰一次、段三本體⛔ 呼：得 (1, 0)　期 (1, 0)
  ✅ T1c 無變 ⇒ 回傳之宗地 ＝ 輸入（同一物件）：得 (True, True)　期 (True, True)
  ✅ T1d 紀錄與逐列入 session：得 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])　期 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])
  ✅ T1e 無變 ⇒ 段三之結果⛔ 存（k6b_stage3_selected ＝ None）、無停機訊息：得 (None, None)　期 (None, None)
  ✅ T1f 無變 ⇒ 真 st 之街角選位⛔ 重跑（恰一）：得 1　期 1
  ✅ T1g 合併再試之輸入：宗地 ＝ 段三之出（此出口 ＝ 原宗地）：得 (True, True)　期 (True, True)
  ✅ T1h 合併再試之輸入：上鎖 ＝ 末一次真 st 街角選位之段一上鎖、街角第 1 宗 ＝ 其 winners、街廓／中心線／退縮／歸戶：得 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})　期 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})
  ✅ T1i alloc_eval 回試算配地之評選（深拷貝）：得 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)
  ✅ T1c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T1c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T1c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T1c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T2a 段三旗標 off 之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  ✅ T2b 合併再試恰一次、段三本體⛔ 呼：得 (1, 0)　期 (1, 0)
  ✅ T2c 有變 ⇒ 回傳之宗地 ＝ 合併再試之出（同一物件）：得 (True, True)　期 (True, True)
  ✅ T2d 紀錄與逐列入 session：得 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])　期 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])
  ✅ T2e 配地所用之宗地 ＝ 合併再試之出（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T2f 所存之結果繫於段三前之宗地與退縮（他 build 或他退縮 ⇒ loud）：得 (('raise', True), ('raise', True))　期 (('raise', True), ('raise', True))
  ✅ T2g 有變 ⇒ 真 st 之街角選位重跑一次、所用 ＝ 合併再試之出：得 (2, True)　期 (2, True)
  ✅ T2h 無停機訊息：得 None　期 None
  ✅ T2c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T2c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T2c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T2c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T3a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  ✅ T3b 段三本體與合併再試各恰一次：得 (1, 1)　期 (1, 1)
  ✅ T3c 段三之試算配地亦 'trial'：得 ['trial']　期 ['trial']
  ✅ T3d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}
  ✅ T3e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (True, True, {'C(1)'})　期 (True, True, {'C(1)'})
  ✅ T3f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T3g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T3h 紀錄入 session：得 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}　期 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}
  ✅ T3i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (2, True)　期 (2, True)
  ✅ T3j 無停機訊息：得 None　期 None
  ✅ T3c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T3c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T3c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T3c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T9a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  ✅ T9b 段三本體與合併再試各恰一次：得 (1, 1)　期 (1, 1)
  ✅ T9c 段三之試算配地亦 'trial'：得 ['trial']　期 ['trial']
  ✅ T9d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}
  ✅ T9e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (True, True, {'C(1)'})　期 (True, True, {'C(1)'})
  ✅ T9f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T9g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T9h 紀錄入 session：得 {'退縮': 3.5, '標的': [], '皆未達': {}}　期 {'退縮': 3.5, '標的': [], '皆未達': {}}
  ✅ T9i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (1, True)　期 (1, True)
  ✅ T9j 無停機訊息：得 None　期 None
  ✅ T9c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T9c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T9c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T9c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T4a 合併再試停機 ⇒ 畫面 st.error ＋ st.stop：得 ('_Stop', True)　期 ('_Stop', True)
  ✅ T4b 停機訊息入 session（含合併再試之原訊息）：得 True　期 True
  ✅ T4c 其後之配地 loud（k6b_stage3_selected raise「請重跑」；k6b_screen_build_for_g ⇒ st.stop）：得 (('raise', True), 'st.stop')　期 (('raise', True), 'st.stop')
  ✅ T4d 前次之紀錄已去、本次⛔ 寫：得 ('<缺>', '<缺>')　期 ('<缺>', '<缺>')
  ✅ T4c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T4c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T4c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T5a 合併再試中斷（KeyError）⇒ 例外上拋：得 'KeyError'　期 'KeyError'
  ✅ T5b 未完成之標記留存（其文含「末端塊合併再試」）：得 True　期 True
  ✅ T5c 其後之配地 loud（k6b_stage3_selected raise「請重跑」）：得 ('raise', True)　期 ('raise', True)
  ✅ T5d 前次之紀錄已去：得 '<缺>'　期 '<缺>'
  ✅ T5c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T5c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T5c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T8a 段三停機 ⇒ st.stop；合併再試⛔ 辦：得 ('_Stop', 0)　期 ('_Stop', 0)
  ✅ T8b 前次之紀錄已去（⛔ 殘留舊紀錄）：得 ('<缺>', '<缺>')　期 ('<缺>', '<缺>')
  ✅ T8c 停機訊息含段三之原訊息：得 True　期 True
  ✅ T8c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T8c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T8c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ TK 試算隔離之鍵含 SS_END_BLOCK_MODE 之值、末項仍 f3_k929_6_log：得 (True, True)　期 (True, True)
  ✅ T6a 注入物之名（四 ＋ blk5）：得 ['a_prime', 'alloc_eval', 'alloc_state', 'blk5', 'trial_winner']　期 ['a_prime', 'alloc_eval', 'alloc_state', 'blk5', 'trial_winner']
  ✅ T6b a′ ＝ a(src) × p(src) ÷ p(dst)（100 × 1000 ÷ 500）：得 200.0　期 200.0
  ✅ T6c 試算選位回 (winner, 真G, 門檻)：得 ('A(1)', 123.45, 100.0)　期 ('A(1)', 123.45, 100.0)
  ✅ T6d 試算配地（alloc_state）之出與其 'trial'：得 ({'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}, ['trial'])　期 ({'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}, ['trial'])
  ✅ T6e 試算配地（alloc_eval）回評選之深拷貝、其 'trial'：得 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False, ['trial'])　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False, ['trial'])
  ✅ T6f 試算配地中止（st.stop）⇒ alloc_eval 拋 RuntimeError：得 'RuntimeError'　期 'RuntimeError'
  ✅ T7a 逐列 ＝ 紀錄之列（值一律字串·None ⇒ —）：得 [{'序': '1', '街廓': 'RB', '端': '右', '候選': 'P(3)', '結果': '成', '檢核': '—'}, {'序': '後處理', '街廓': 'RB', '端': '右', '候選': 'P(4)', '結果': '成', '檢核': '通過'}]　期 [{'序': '1', '街廓': 'RB', '端': '右', '候選': 'P(3)', '結果': '成', '檢核': '—'}, {'序': '後處理', '街廓': 'RB', '端': '右', '候選': 'P(4)', '結果': '成', '檢核': '通過'}]
  ✅ T7b 行內載標的之街廓與端、競合之候選與交面積、皆未達 ⇒ 強制抵費地、退縮：得 []　期 []
  ✅ T7c 無標的 ⇒ 行含「無標的」、逐列空：得 (True, [])　期 (True, [])
  ✅ T7d 試算中止 ⇒ 行含「試算中止」與其訊息：得 (True, True)　期 (True, True)
  ✅ T7e 無紀錄 ⇒ 空：得 {'lines': [], 'rows': []}　期 {'lines': [], 'rows': []}
  ✅ TS 三介面之簽名：得 [(['st'], ['g_kwargs', 'pk_kwargs']), (['st'], ['g_kwargs', 'pk_kwargs']), (['rec', 'log'], [])]　期 [(['st'], ['g_kwargs', 'pk_kwargs']), (['st'], ['g_kwargs', 'pk_kwargs']), (['rec', 'log'], [])]
── P0 判式自驗（期值記錄須全綠；逐項擾動須恰該項紅）──
  ✅ P0 期值記錄全綠 True；逐項擾動恰該項紅 86／86
⇒ 紅 []；rc 0
`````

#### `#25`　`python3 verify/probes/probe_WG9355_screenmerge.py run <repo>`（rc `0`·stderr `0` B·1863 s）

`````
── F13 之判式施於畫面路徑（R1 本案·C／F／X 合成案甲乙丙）──
  ✅ R1 退縮 3.5：合併再試紀錄 {'退縮': 3.5, '標的': [], '皆未達': {}}（⛔ 載競合）；逐列 0
  ✅ R1 退縮 0.0：合併再試紀錄 {'退縮': 0.0, '標的': [], '皆未達': {}}（⛔ 載競合）；逐列 0
══ 合成案甲（退縮 3.5·注入 末端帶寬 [8.0, 16.0]、上鎖 3、假設跨占街角 []·咬到 {'host': 0, 'merge': 1, 'geo': 196}）══
  ✅ C甲 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 237.57]]}]；外部錨之交面積 R3 左 66.49／R5 右 237.57
  ✅ F甲 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X甲：逐列 [('628(4)', '②', '未成', '—'), ('628(3)', '②', '未成', '—'), ('628-34(2)', '—', '未成', '—'), ('628-23(2)', '①', '成', '免'), ('628-22(2)', '—', '略·已定案', '—')]；後處理 [('628-23(3)', '後處理(b)', '成', '628-23(2)'), ('628-22(3)', '後處理(b)', '成', '628-23(2)')]；二片皆全在中心線之一側 True；R5 右鏈首宗 628-23(2) G 1422.89 ＝ 外部錨 1422.89；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案乙（退縮 3.5·注入 末端帶寬 [8.0, 5.5]、上鎖 6、假設跨占街角 ['628-23(2)']·咬到 {'host': 102, 'merge': 1, 'geo': 204}）══
  ✅ C乙 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 217.29]]}]；外部錨之交面積 R3 左 66.49／R5 右 217.29
  ✅ F乙 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X乙：逐列 [('628(3)', '②', '成', '通過'), ('628(4)', '②', '未成', '—'), ('628-34(2)', '—', '未成', '—')]；後處理 [('628(4)', '後處理(a)', '成', '628(3)')]；R5 右鏈首宗 628(3) G 408.48 ＝ 外部錨 408.48；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丙（退縮 3.5·注入 末端帶寬 [8.0, 5.0]、上鎖 6、假設跨占街角 ['628-23(2)']·咬到 {'host': 102, 'merge': 1, 'geo': 204}）══
  ✅ C丙 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 207.25]]}]；外部錨之交面積 R3 左 66.49／R5 右 207.25
  ✅ F丙 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X丙：逐列 [('628(3)', '②半', '成', '通過'), ('628(4)', '②半', '未成', '—'), ('628-34(2)', '—', '未成', '—')]；後處理 [('628(4)', '題一 4', '成', '628(3)')]；切半之量 {'628(6)': 170.7953}／{'628(6)': 170.9947} ＝ 外部錨 170.7953／170.9947（R5 側之比 0.4997）；R5 右鏈首宗 628(3) G 408.48 ＝ 外部錨 408.48；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
⇒ 紅 []；rc 0
── E：畫面路徑之專項 ──
  ✅ E@3.5：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@0.0：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@3.5·甲：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@3.5·乙：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@3.5·丙：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
⇒ 紅 []；rc 0
`````

#### `#36`　`python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>`（rc `0`·stderr `0` B·7 s）

`````
── 合成對照（harvest 之 end_block_*／end_block_merge_run〔其內 k6b_stage3_run 為真〕）──
  ✅ S1 皆未達而准 ⇒ 無當選·列全留：得 (None, ['未達', '未達'])　期 (None, ['未達', '未達'])
  ✅ S1b 皆未達而不准 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S2 強制 ⇒ ⛔ 落位·紀錄當選 None·強制抵費地·buf 3.5·R_end 150：得 (['A(1)', 'B(1)'], None, True, 3.5, 150.0, None, True, False, None)　期 (['A(1)', 'B(1)'], None, True, 3.5, 150.0, None, True, False, None)
  ✅ S3 首趟強制而本趟不准 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S4 首趟強制而本趟准 ⇒ 沿用（⛔ 重評）：得 (True, 0, ['A(1)', 'B(1)'])　期 (True, 0, ['A(1)', 'B(1)'])
  ✅ S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）：得 (3.5, 0.0, 3.5, 0.0, 0.0)　期 (3.5, 0.0, 3.5, 0.0, 0.0)
  ✅ S6 強制帶 ＝ R_end（非強制⛔ 入）：得 (1, 150.0, 0, 0)　期 (1, 150.0, 0, 0)
  ✅ S7 定案趟：強制側有末端塊之宗 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S7b 定案趟：強制側無末端塊之宗 ⇒ 過：得 '過'　期 '過'
  ✅ S8 顯示：強制抵費地之列：得 ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）']　期 ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；各筆單獨與合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）']
  ✅ S9a 宿主：試算 ⇒ 准：得 (True, None)　期 (True, None)
  ✅ S9b 宿主：定案而無紀錄 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S9c 宿主：定案而紀錄（同退縮）載該端 ⇒ 准：得 (True, None)　期 (True, None)
  ✅ S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S9e 宿主：定案而紀錄只載他街廓 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S10a 無標的（C1(1) 單獨即達）⇒ 逕回（同一物件）：得 (True, [], [], 0)　期 (True, [], [], 0)
  ✅ S10b ① 同街廓成（⛔ 驗不影響原位次）：得 ([('C1(1)', '①', '成', '免'), ('C2(1)', '—', '略·已定案', '—')], {}, 1, ['C1(1)', 'C2(1)', 'D(1)'])　期 ([('C1(1)', '①', '成', '免'), ('C2(1)', '—', '略·已定案', '—')], {}, 1, ['C1(1)', 'C2(1)', 'D(1)'])
  ✅ S10c ② 道路成且驗不影響原位次：得 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '成', '通過')], {}, 3)　期 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '成', '通過')], {}, 3)
  ✅ S10d ② 之驗不過 ⇒ 未成 ⇒ 皆未達：得 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '未成', '不過')], {'BX': ['left']})　期 ([('C1(1)', '①', '未成', '—'), ('C2(1)', '②', '未成', '不過')], {'BX': ['left']})
  ✅ S10e 除外：上鎖者⛔ 併入：得 ('C1(1)', '—', '未成', '—')　期 ('C1(1)', '—', '未成', '—')
  ✅ S10f 除外：街角第 1 宗⛔ 併入：得 ('C1(1)', '—', '未成', '—')　期 ('C1(1)', '—', '未成', '—')
  ✅ S10g 除外：段三已併出者⛔ 併入：得 ('C1(1)', '—', '未成', '—')　期 ('C1(1)', '—', '未成', '—')
  ✅ S10i 試算中止 ⇒ 逕回並記其由：得 (True, None, True)　期 (True, None, True)
── 判別力（突變之函式以其原始碼改一處後重綁於 ns·每一突變須使至少一例轉紅·畢即復原）──
  ✅ M1 皆未達⛔ 理准否（恆停機）：轉紅 ['S1 皆未達而准 ⇒ 無當選·列全留', 'S2 強制 ⇒ ⛔ 落位·紀錄當選 None·強制抵費地·buf 3.5·R_end 150', 'S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）', 'S6 強制帶 ＝ R_end（非強制⛔ 入）', 'S9a 宿主：試算 ⇒ 准', 'S9c 宿主：定案而紀錄（同退縮）載該端 ⇒ 准']
  ✅ M2 宿主恆准：轉紅 ['S9b 宿主：定案而無紀錄 ⇒ 停機', 'S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機', 'S9e 宿主：定案而紀錄只載他街廓 ⇒ 停機']
  ✅ M3 宿主⛔ 對退縮：轉紅 ['S9d 宿主：定案而紀錄之退縮不同 ⇒ 停機']
  ✅ M4 強制帶之 s 長恆 0：轉紅 ['S5 強制帶之 s 長（左 s_hi·右 s(p2)−s_lo·非強制 0）']
  ✅ M5 強制⛔ 入池：轉紅 ['S6 強制帶 ＝ R_end（非強制⛔ 入）']
  ✅ M6 段三已併出者⛔ 除外：轉紅 ['S10g 除外：段三已併出者⛔ 併入']
  ✅ M8 試算中止⛔ 攔：轉紅 ['S10i 試算中止 ⇒ 逕回並記其由']
  ✅ M0 復原後：紅 []
⇒ 紅 []；rc 0
`````

#### `#37`　`python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>`（rc `0`·stderr `0` B·21 s）

`````
── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py ＋ verify/selection_pipeline.py）──
  ✅ W1 模組層之二常數與三函式、函式內⛔ 案件字面（案件字面 []）
  ✅ W2 二宿主：強制帶之 s 長入鏈之起點（左鏈之前）、強制帶入池（`_pool_strips_for_block` 之前）
  ✅ W3 宿主之准否：讀 `SS_END_BLOCK_MODE`／`SS_END_BLOCK_MERGE`／退縮，傳 `allow_forced=_allow`
  ✅ W4 harness：`alloc_state`／`alloc_eval` 於配地前設 `'trial'`；`run_corner_pk_k6b` 於段三之 if／else 之後（頂層）恰一次呼叫 `run_end_block_merge`，段三亦用同一組回呼（頂層呼叫 ['Assign']）
  ✅ W5 `run_end_block_merge`：隔離（finally 復原 session 與 `K917_DROPPED`）後寫紀錄、帶退縮
  ✅ W6 `_WF_NS_NAMES` 含 `end_block_forced_buf`／`end_block_forced_bands`
  ✅ W7 `end_block_merge_run`：交 `k6b_stage3_run`（單一真相源）、除外三類、競合以合併群查
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 harness 左鏈⛔ 讓出強制帶：轉紅 ['W2']
  ✅ N2 harness 配地試算⛔ 設 trial：轉紅 ['W4']
  ✅ N3 宿主⛔ 傳准否：轉紅 ['W3']
  ✅ N4 畫面⛔ 入池強制帶：轉紅 ['W2']
⇒ 紅 []；rc 0
`````

#### `#67`　`python3 verify/probes/probe_WG9353_endmerge.py run <repo>`（rc `0`·stderr `0` B·1342 s）

`````
  ✅ R1 退縮 3.5：合併再試紀錄 {'退縮': 3.5, '標的': [], '皆未達': {}}；逐列 0；R6 左當選 628-4(1)
  ✅ R1 退縮 0.0：合併再試紀錄 {'退縮': 0.0, '標的': [], '皆未達': {}}；逐列 0；R6 左當選 628-4(1)
══ 合成案甲（退縮 3.5·注入 {'excl': ['628-4(1)'], 'lock': [], 'mw': None}·咬到 {'host': 57, 'merge': 0, 'geo': 0}）══
  ✅ X1 甲：地主 G009 以道路併入成，其合併群之他街廓依原位次配得者照配（`W-G.9-354`·`K-9-48` 其二·讀法 `1` ⑤）；餘片鄰二配得之街廓 ⇒ 併入 G 大之一側（中止 None；[('後處理(a)', '成', '628(1)')]）
══ 合成案乙（退縮 3.5·注入 {'excl': ['628-4(1)'], 'lock': ['628-1(3)', '628-22(3)', '628-23(3)'], 'mw': None}·咬到 {'host': 48, 'merge': 1, 'geo': 0}）══
  ✅ X2 乙：逐列 [('628(2)', '①', '未成', '—'), ('628-1(2)', '①', '未成', '—'), ('628-23(1)', '①', '成', '免')]；當選 628-23(1)；鏈首宗 628-23(1) G 437.18 ＝ 外部錨 437.18；聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丙（退縮 3.5·注入 {'excl': ['628-4(1)'], 'lock': ['628-1(3)', '628-21(1)', '628-22(1)'], 'mw': None}·咬到 {'host': 52, 'merge': 1, 'geo': 0}）══
  ✅ X3 丙：逐列 [('628(2)', '①', '未成', '—'), ('628-1(2)', '①', '未成', '—'), ('628-23(1)', '—', '未成', '—')]；皆未達 {'R6': ['left']}；強制抵費地 R6-抵費地-2（252.28·外部錨 R_end 252.28·紀錄 252.28）；宗地 ∩ R_end 0.000000；聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丁（退縮 3.5·注入 {'excl': [], 'lock': [], 'mw': 13.0}·咬到 {'host': 0, 'merge': 0, 'geo': 68}）══
  ✅ X4 丁：逐列 [('628(2)', '②', '未成', '—'), ('628-1(2)', '②', '未成', '—'), ('628-23(1)', '①', '未成', '—'), ('628-4(1)', '②', '成', '通過'), ('628-22(1)', '—', '略·已定案', '—')]；當選 628-4(1)（R_end 701.29）；鏈首宗 628-4(1) G 779.93 ＝ 外部錨 779.93；聯集 △ 街廓 0.0000、兩兩疊 0.0000
⇒ 紅 []；rc 0
`````

#### `#38`　`python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>`（rc `0`·stderr `0` B·15 s）

`````
── 合成對照（harvest 之 end_block_merge_run〔其內 k6b_stage3_run 為真〕）──
  ✅ TA 題一 ① 二端皆以本街廓內之土地成 ⇒ 道路於後處理依中心線切分各歸：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])
  ✅ TB 題一 ① 只 A 成 ⇒ 只一端需要 ⇒ B 整片成：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '②', '成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'X1(1)': 60.0, 'Y1(1)': 130.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '②', '成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'X1(1)': 60.0, 'Y1(1)': 130.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])
  ✅ TC 題一 ① 只 A 成、B 整片未成（Y1 配得）⇒ 道路之下半併 Y1、Y2 照配：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '②', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {'BY': ['left']}, {'X1(1)': 92.0, 'Y1(1)': 48.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '②', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {'BY': ['left']}, {'X1(1)': 92.0, 'Y1(1)': 48.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TD 題一 ① 只 A 成、B 整片未成（Y1 不配得）⇒ Y1 併入 X1、道路之下半併 Y2：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '②', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('Y1(1)', '後處理(a)', '成', 'X1(1)'), ('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y2(1)'))], {'BY': ['left']}, {'X1(1)': 182.0, 'Y2(1)': 48.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y2(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '②', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('Y1(1)', '後處理(a)', '成', 'X1(1)'), ('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y2(1)'))], {'BY': ['left']}, {'X1(1)': 182.0, 'Y2(1)': 48.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y2(1)'])
  ✅ TE 題一 切半二端皆成（上 0.4／下 0.6）：得 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])
  ✅ TF 題一 切半只 A 成、Y1 連其半配得 ⇒ 其半併 Y1：得 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('Y1(1)', '題一 4', '成', 'Y1(1)')], {'BY': ['left']}, {'X1(1)': 92.0, 'Y1(1)': 48.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('Y1(1)', '題一 4', '成', 'Y1(1)')], {'BY': ['left']}, {'X1(1)': 92.0, 'Y1(1)': 48.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TG 題一 切半只 A 成、Y1 連其半不能配得 ⇒ 連同其半併入 X1：得 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('Y1(1)', '題一 4', '成', 'X1(1)')], {'BY': ['left']}, {'X1(1)': 230.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y2(1)'])　期 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [('Y1(1)', '題一 4', '成', 'X1(1)')], {'BY': ['left']}, {'X1(1)': 230.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y2(1)'])
  ✅ TH 題一 整片只 A 成：得 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '—'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TI 題一 整片二端皆成 ⇒ G 大者（A 240 ＞ B 220·交面積 B 30 ＞ A 15 ⛔ 用）：得 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TT 題一 整片二端皆成·G 相同 ⇒ 重劃前面積大者（補令二）：得 ([('Y1(1)', '②', '成', '通過'), ('X1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·競合歸他端', '—'), ('K1(1)', '①', '未成', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {'BX': ['left']}, {'X2(1)': 10.0, 'Y1(1)': 150.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'X2(1)', 'Y1(1)'])　期 ([('Y1(1)', '②', '成', '通過'), ('X1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·競合歸他端', '—'), ('K1(1)', '①', '未成', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {'BX': ['left']}, {'X2(1)': 10.0, 'Y1(1)': 150.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'X2(1)', 'Y1(1)'])
  ✅ TU 題一 整片二端皆成·G 與重劃前面積皆相同 ⇒ 暫編地號小者（補令二）：得 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TJ 題一 整片二端皆成·交面積並列 ⇒ G 大者（補令二改名·原：跨占者暫編地號小者）：得 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '②', '成', '通過'), ('Y1(1)', '②', '未成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'X1(1)': 140.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TK 題一 皆不成 ⇒ 二端皆⛔ 併；A 由他人（K1 併 K2）續試而成：得 ([('X1(1)', '②', '未成', '—'), ('Y1(1)', '②', '未成', '—'), ('K1(1)', '①', '成', '免'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'K1(1)': 200.0}, ['K1(1)', 'P(1)', 'Q(1)', 'X1(1)', 'X2(1)', 'Y1(1)', 'Y2(1)'])　期 ([('X1(1)', '②', '未成', '—'), ('Y1(1)', '②', '未成', '—'), ('K1(1)', '①', '成', '免'), ('Y2(1)', '—', '略·競合歸他端', '—')], [], {'BY': ['left']}, {'K1(1)': 200.0}, ['K1(1)', 'P(1)', 'Q(1)', 'X1(1)', 'X2(1)', 'Y1(1)', 'Y2(1)'])
  ✅ TL 題一 夥伴之端先由他人定案 ⇒ 競合消滅·逐列（B 整片成）：得 ([('K1(1)', '①', '成', '免'), ('X1(1)', '—', '略·已定案', '—'), ('Y1(1)', '②', '成', '通過'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'K1(1)': 40.0, 'Y1(1)': 130.0}, ['K1(1)', 'P(1)', 'Q(1)', 'X1(1)', 'X2(1)', 'Y1(1)'])　期 ([('K1(1)', '①', '成', '免'), ('X1(1)', '—', '略·已定案', '—'), ('Y1(1)', '②', '成', '通過'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'K1(1)': 40.0, 'Y1(1)': 130.0}, ['K1(1)', 'P(1)', 'Q(1)', 'X1(1)', 'X2(1)', 'Y1(1)'])
  ✅ TM 題一 A 擱置中 B 由他人（M1 併 M2）定案 ⇒ 釋出·A 逐列成（Y2 不配得 ⇒ 併 Y1）：得 ([('M1(1)', '①', '成', '免'), ('X1(1)', '①', '成', '免'), ('Y1(1)', '—', '略·已定案', '—')], [('Y2(1)', '後處理(a)', '成', 'Y1(1)'), ('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0, 'M1(1)': 100.0}, ['K1(1)', 'K2(1)', 'M1(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])　期 ([('M1(1)', '①', '成', '免'), ('X1(1)', '①', '成', '免'), ('Y1(1)', '—', '略·已定案', '—')], [('Y2(1)', '後處理(a)', '成', 'Y1(1)'), ('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {}, {'M1(1)': 100.0, 'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'M1(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])
  ✅ TN 題一 公設片平分（0.5／0.5）二端皆成：得 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'X1(1)': 100.0, 'Y1(1)': 90.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '②半', '成', '通過'), ('Y1(1)', '②半', '成', '通過'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [], {}, {'X1(1)': 100.0, 'Y1(1)': 90.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])
  ✅ TO 題二 ① 只左拿得下：得 ([('W1(1)', '②', '未成', '—'), ('Z1(1)', '①', '成', '免'), ('Z2(1)', '①', '未成', '—')], [('Z3(1)', '後處理(b)', '成', 'Z1(1)')], {'BZ': ['right']}, {'Z1(1)': 350.0}, ['W1(1)', 'W2(1)', 'Z1(1)'])　期 ([('W1(1)', '②', '未成', '—'), ('Z1(1)', '①', '成', '免'), ('Z2(1)', '①', '未成', '—')], [('Z3(1)', '後處理(b)', '成', 'Z1(1)')], {'BZ': ['right']}, {'Z1(1)': 350.0}, ['W1(1)', 'W2(1)', 'Z1(1)'])
  ✅ TP 題二 ① 二端皆拿得下 ⇒ 交面積大者（右 20 ＞ 左 10）：得 ([('W1(1)', '②', '未成', '—'), ('Z2(1)', '①', '成', '免'), ('Z1(1)', '①', '未成', '免')], [('Z3(1)', '後處理(b)', '成', 'Z2(1)')], {'BZ': ['left']}, {'Z2(1)': 370.0}, ['W1(1)', 'W2(1)', 'Z2(1)'])　期 ([('W1(1)', '②', '未成', '—'), ('Z2(1)', '①', '成', '免'), ('Z1(1)', '①', '未成', '免')], [('Z3(1)', '後處理(b)', '成', 'Z2(1)')], {'BZ': ['left']}, {'Z2(1)': 370.0}, ['W1(1)', 'W2(1)', 'Z2(1)'])
  ✅ TQ 題二 ① 二端皆拿得下·交面積並列 ⇒ 前緣線 p1 側（左）：得 ([('W1(1)', '②', '未成', '—'), ('Z1(1)', '①', '成', '免'), ('Z2(1)', '①', '未成', '免')], [('Z3(1)', '後處理(b)', '成', 'Z1(1)')], {'BZ': ['right']}, {'Z1(1)': 350.0}, ['W1(1)', 'W2(1)', 'Z1(1)'])　期 ([('W1(1)', '②', '未成', '—'), ('Z1(1)', '①', '成', '免'), ('Z2(1)', '①', '未成', '免')], [('Z3(1)', '後處理(b)', '成', 'Z1(1)')], {'BZ': ['right']}, {'Z1(1)': 350.0}, ['W1(1)', 'W2(1)', 'Z1(1)'])
  ✅ TR 題二 ② 只右拿得下：得 ([('W1(1)', '②', '未成', '—'), ('Z2(1)', '②', '成', '通過'), ('Z1(1)', '②', '未成', '—')], [], {'BZ': ['left']}, {'Z2(1)': 370.0}, ['W1(1)', 'W2(1)', 'Z2(1)'])　期 ([('W1(1)', '②', '未成', '—'), ('Z2(1)', '②', '成', '通過'), ('Z1(1)', '②', '未成', '—')], [], {'BZ': ['left']}, {'Z2(1)': 370.0}, ['W1(1)', 'W2(1)', 'Z2(1)'])
  ✅ TS 題二 二端皆拿不下 ⇒ 皆⛔ 併：得 ([('W1(1)', '②', '未成', '—'), ('Z1(1)', '—', '未成', '—'), ('Z2(1)', '—', '未成', '—')], [], {'BZ': ['left', 'right']}, {}, ['W1(1)', 'W2(1)', 'Z1(1)', 'Z2(1)', 'Z4(1)'])　期 ([('W1(1)', '②', '未成', '—'), ('Z1(1)', '—', '未成', '—'), ('Z2(1)', '—', '未成', '—')], [], {'BZ': ['left', 'right']}, {}, ['W1(1)', 'W2(1)', 'Z1(1)', 'Z2(1)', 'Z4(1)'])
  ✅ H1 同一合併群之候選分屬三個末端塊 ⇒ 停機：得 ('停機', True)　期 ('停機', True)
  ✅ H2 一筆土地同時跨占二末端塊 ⇒ 停機：得 ('停機', True)　期 ('停機', True)
  ✅ H3 一末端塊屬二競合 ⇒ 停機：得 ('停機', True)　期 ('停機', True)
  ✅ P1 他街廓依原位次配得之宗照配（⛔ 動·⛔ 停機）：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'W5(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)'))], {}, {'X1(1)': 92.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'W5(1)', 'X1(1)', 'Y1(1)'])
  ✅ P2 公設片平分須由 BW 承受而其配得之宗二筆 ⇒ 相鄰者先 → G → 重劃前面積 → 暫編地號（W5）：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)')), ('G5(1)', '後處理(c)', '成', ('W5(1)', 'X1(1)', 'Y1(1)'))], {}, {'X1(1)': 122.0, 'Y1(1)': 128.0, 'W5(1)': 30.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'W5(1)', 'W6(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)')), ('G5(1)', '後處理(c)', '成', ('W5(1)', 'X1(1)', 'Y1(1)'))], {}, {'W5(1)': 30.0, 'X1(1)': 122.0, 'Y1(1)': 128.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'W5(1)', 'W6(1)', 'X1(1)', 'Y1(1)'])
  ✅ P3 公設片三街廓平分，BW 由其唯一配得之宗承受：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)')), ('G5(1)', '後處理(c)', '成', ('W5(1)', 'X1(1)', 'Y1(1)'))], {}, {'X1(1)': 122.0, 'Y1(1)': 128.0, 'W5(1)': 30.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'W5(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)')), ('G5(1)', '後處理(c)', '成', ('W5(1)', 'X1(1)', 'Y1(1)'))], {}, {'W5(1)': 30.0, 'X1(1)': 122.0, 'Y1(1)': 128.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'W5(1)', 'X1(1)', 'Y1(1)'])
  ✅ S1 道路片全在中心線之一側（X5）⇒ 不切、全歸該側：得 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)')), ('X5(1)', '後處理(b)', '成', 'X1(1)')], {}, {'X1(1)': 112.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])　期 ([('X1(1)', '①', '成', '免'), ('Y1(1)', '①', '成', '免'), ('X2(1)', '—', '略·已定案', '—'), ('K1(1)', '—', '略·已定案', '—'), ('Y2(1)', '—', '略·已定案', '—')], [('X3(1)', '後處理(b)', '成', ('X1(1)', 'Y1(1)')), ('X5(1)', '後處理(b)', '成', 'X1(1)')], {}, {'X1(1)': 112.0, 'Y1(1)': 98.0}, ['K1(1)', 'K2(1)', 'P(1)', 'Q(1)', 'X1(1)', 'Y1(1)'])
── 判別力（突變之函式以其原始碼改一處後重綁於 ns·每一突變須使至少一例轉紅·畢即復原）──
  ✅ M1 ⛔ 交競合（逐列）：轉紅 ['TA', 'TB', 'TC', 'TD', 'TE', 'TF', 'TG', 'TH', 'TI', 'TT', 'TU', 'TJ', 'TK', 'TM', 'TN', 'TO', 'TP', 'TQ', 'TR', 'TS', 'P1', 'P2', 'P3', 'S1']
  ✅ M2 交面積之比較反向：轉紅 ['TP']
  ✅ M3 題一 3 之序⛔ 暫編地號（補令二·錨於 k967_rank）：轉紅 ['TU']
  ✅ M15 題一 3 之序之 G 反向（補令二）：轉紅 ['TI', 'TJ']
  ✅ M16 題一 3 之序之重劃前面積反向（補令二）：轉紅 ['TT']
  ✅ M4 並列取 p2 側：轉紅 ['TQ']
  ✅ M5 ⛔ 切半：轉紅 ['TE', 'TF', 'TG', 'TN']
  ✅ M6 未得之一端恆併入已取得之一端：轉紅 ['TF']
  ✅ M7 ⛔ 查三以上：轉紅 ['H1']
  ✅ M8 ⛔ 查一端二競合：轉紅 ['H3']
  ✅ M9 未得之一端⛔ 略同群之候選：轉紅 ['TC', 'TD', 'TF', 'TG', 'TH', 'TI', 'TT', 'TU', 'TJ', 'TK']
  ✅ M10 無受併宗街廓之配得者⛔ 照配：轉紅 ['TC', 'TD', 'TF', 'TG', 'TH', 'TI', 'TT', 'TU', 'TJ', 'TL', 'TM', 'P1', 'P2', 'P3']
  ✅ M11 未得之一端之土地⛔ 歸已取得之一端：轉紅 ['TD']
  ✅ M12 道路片須恰切二：轉紅 ['S1']
  ✅ M13 ⛔ 擱置（逐列）：轉紅 ['TA', 'TB', 'TC', 'TD', 'TE', 'TF', 'TG', 'TH', 'TI', 'TT', 'TU', 'TJ', 'TK', 'TM', 'TN', 'TO', 'TP', 'TQ', 'TR', 'TS', 'P1', 'P2', 'P3', 'S1']
  ✅ M14 夥伴之端定案⛔ 釋出：轉紅 ['TM']
  ✅ M0 復原後：紅 []
⇒ 紅 []；rc 0
`````

#### `#39`　`python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>`（rc `0`·stderr `0` B·12 s）

`````
── 接線（AST／字樣·app.py ＋ verify/selection_pipeline.py）──
  ✅ W1 `end_block_merge_run` 交競合、三以上與一端二競合停機、題一／題二依街廓之同異
  ✅ W2 `k6b_stage3_run`：`contests=None`、逐列之環經 `_k950_rows`、無競合 ⇒ 逐列依序
  ✅ W3 段三之二呼叫端（harness／畫面）⛔ 給競合
  ✅ W4 道路片之中心線切分 ＝ 單一真相源（後處理 (b) 與題一之切半）
  ✅ W5 後處理：無本段受併宗之街廓之配得者照配、承受之宗經 `_recv_of`
  ✅ W6 二函式內⛔ 案件字面（案件字面 []）
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 ⛔ 交競合：轉紅 ['W1']
  ✅ N2 逐列之環⛔ 經 `_k950_rows`：轉紅 ['W2']
  ✅ N3 後處理 (b) 另切：轉紅 ['W4']
  ✅ N4 ⛔ 照配：轉紅 ['W5']
⇒ 紅 []；rc 0
`````

#### `#68`　`python3 verify/probes/probe_WG9354_endcontest.py run <repo>`（rc `0`·stderr `0` B·1291 s）

`````
  ✅ R1 退縮 3.5：合併再試紀錄 {'退縮': 3.5, '標的': [], '皆未達': {}}（⛔ 載競合）；逐列 0
  ✅ R1 退縮 0.0：合併再試紀錄 {'退縮': 0.0, '標的': [], '皆未達': {}}（⛔ 載競合）；逐列 0
══ 合成案甲（退縮 3.5·注入 末端帶寬 [8.0, 16.0]、上鎖 3、假設跨占街角 []·咬到 {'host': 0, 'merge': 1, 'geo': 144}）══
  ✅ C甲 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 237.57]]}]；外部錨之交面積 R3 左 66.49／R5 右 237.57
  ✅ F甲 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X甲：逐列 [('628(4)', '②', '未成', '—'), ('628(3)', '②', '未成', '—'), ('628-34(2)', '—', '未成', '—'), ('628-23(2)', '①', '成', '免'), ('628-22(2)', '—', '略·已定案', '—')]；後處理 [('628-23(3)', '後處理(b)', '成', '628-23(2)'), ('628-22(3)', '後處理(b)', '成', '628-23(2)')]；二片皆全在中心線之一側 True；R5 右鏈首宗 628-23(2) G 1422.89 ＝ 外部錨 1422.89；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案乙（退縮 3.5·注入 末端帶寬 [8.0, 5.5]、上鎖 6、假設跨占街角 ['628-23(2)']·咬到 {'host': 75, 'merge': 1, 'geo': 150}）══
  ✅ C乙 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 217.29]]}]；外部錨之交面積 R3 左 66.49／R5 右 217.29
  ✅ F乙 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X乙：逐列 [('628(3)', '②', '成', '通過'), ('628(4)', '②', '未成', '—'), ('628-34(2)', '—', '未成', '—')]；後處理 [('628(4)', '後處理(a)', '成', '628(3)')]；R5 右鏈首宗 628(3) G 408.48 ＝ 外部錨 408.48；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丙（退縮 3.5·注入 末端帶寬 [8.0, 5.0]、上鎖 6、假設跨占街角 ['628-23(2)']·咬到 {'host': 75, 'merge': 1, 'geo': 150}）══
  ✅ C丙 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 207.25]]}]；外部錨之交面積 R3 左 66.49／R5 右 207.25
  ✅ F丙 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X丙：逐列 [('628(3)', '②半', '成', '通過'), ('628(4)', '②半', '未成', '—'), ('628-34(2)', '—', '未成', '—')]；後處理 [('628(4)', '題一 4', '成', '628(3)')]；切半之量 {'628(6)': 170.7953}／{'628(6)': 170.9947} ＝ 外部錨 170.7953／170.9947（R5 側之比 0.4997）；R5 右鏈首宗 628(3) G 408.48 ＝ 外部錨 408.48；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
⇒ 紅 []；rc 0
`````
