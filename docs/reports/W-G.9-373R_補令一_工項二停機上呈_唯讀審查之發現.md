# `W-G.9-373R`　補令一 工項二停機上呈：唯讀獨立審查之發現——同一趟之內，`K-9-67` 之重劃前面積之表看不到本趟已部分併出之量（規格之漏載·停機款 `12`）

> 受單 ＝ CC 新窗·`2026-10-09`（受 `docs/orders/W-G.9-373_補令一.md`·續辦原單 `docs/orders/W-G.9-373_規格單.md` 之工項二〜四）。施工樹 ＝ `.claude/worktrees/land-readjustment-trial-doc-ce8910`（倉之 worktree·detached）。倉外出艙 `<O>` ＝ `C:\Users\admin\o373p1`（⛔ 在任何 git 工作樹之內）。本機 Windows 11·Python `3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`（發單側為 `numpy 2.4.6`／`shapely 2.2.0`·照實載）。量測之殼之 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6`／`WV_K953`／`WV_ADJ4` 皆未設（出艙 `[None, None, None, None, None]`）。
> 🛑 **停機款 `12`**（原單之款照舊·補令 `§零-2` 末：「工項二之唯讀獨立 reviewer 之發現涉域上判斷或規格之漏載 ⇒ 停機」）成就 ⇒ **停機上呈·⛔ 自裁**。工項二之生產碼**⛔ 推**（存本地 ref `hold/W-G.9-373p1-c2`）；工項三（入典與登記）、工項四（執行報告）**⛔ 辦**（候裁）。本檔 ＝ 停機報告（零生產碼），與工項二之二檔之全文差異（同目錄 `W-G.9-373R_補令一_工項二_二檔差異.diff`）同一 `commit` 推至側支 `verify/W-G.9-373-k966`（快轉）。
> 驗 `V-1′`〜`V-9′` **皆符**（`§二`）；審查之 (B) 純實作之瑕 ＝ **`0`**；(C) NOTE ＝ `6`（`§三`）。

## `§零`　態

| 項 | 值 |
|---|---|
| 主線 `wip/s1-endpart` | `104e4aaf211959c38b4030c55372bb5ef513c7fa`（⛔ 動） |
| 側支 `verify/W-G.9-370-selfchk`／`verify/W-G.9-367-adj4` | `fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583`／`e7855ecf75ca4ed692baa982f5f25ec672847e79`（皆⛔ 動） |
| 側支 `verify/W-G.9-373-k966` | 開工 `fcef5a3e3d1f073747ae81b4a998c6cdbfb26a2d` → 工項零′ `dce634a5c465c5e9d9a6890c5815aa3c805e5be9` → 工項一′ `b73fbd42d053110006e847a6e3dd69774bf03b41` → 本停機報告之 `commit`（零生產碼·快轉） |
| 工項二之碼 | `6e7272ae314e4acc4cbc343014e5b0be2f36049e`（父 ＝ `b73fbd4`）——**⛔ 推**，存本地 ref **`hold/W-G.9-373p1-c2`**（KL 主 checkout 與此 worktree 共用之 `.git`）；`app.py` blob `5ea2beb33e9dbd1b682afb8b2191c5007b064ff4`、`verify/selection_pipeline.py` blob `2d7def55f37e15b22698ce9ec217b00f18d4b92d`（＝ 原碼）；`git show --numstat`：`app.py` `738`／`449`、`verify/selection_pipeline.py` `13`／`3`；對原碼（`54e142c`·本地 `hold/W-G.9-373-c2`）之差：`app.py` `+85`／`−20`（`diff` 列框）；其全文差異（對工項一′ 之端）＝ 同目錄 `W-G.9-373R_補令一_工項二_二檔差異.diff`（`git diff b73fbd4 6e7272a -- app.py verify/selection_pipeline.py`·`104903` B·`1570` 列·真 `0x0D` `0`）；對原碼之差異之全文 ＝ 本檔附錄四 |
| 前窗之碼 | `hold/W-G.9-373-c2` ＝ `54e142c91d69c7469a8f6a2d0ad6b314771560bb`（存否 ＝ 存·⛔ 動） |
| 遠端 heads | 開工 `38` → 工項零′／一′ 之推後 `38`；其餘 `37` 列 ＝ `<O>\heads_before_p1.txt` |

逐 `commit` 之生產碼判法（`git diff --name-only <父> <commit> -- app.py verify/stepg_pipeline.py verify/run_all.py verify/run_verification.py`）：工項零′ ＝ 空；工項一′ ＝ 空；工項二 ＝ `app.py`（未推）；本停機報告 ＝ 空（推前另驗）。

## `§一`　開工閘、前置′ 與工項零′／一′（皆 ＝ 期）

| 款 | 期 | 實 |
|---|---|---|
| `1′` | 主線 `104e4aa`、側支 `fcef5a3`、二舊側支、heads `38`、追蹤檔無變動、`§零-0` 項 `3`、旗標 | 皆符：`git rev-parse` 四值逐位 ＝ 期；heads `38`（全列存 `<O>\heads_before_p1.txt`）；`git checkout --detach origin/verify/W-G.9-373-k966` 後 `git status --porcelain --untracked-files=no` 空；`issuer_anchor 590 589` `rc 0`、「項4′」自誤 `575`／`590`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、GB `195`／`202`／`[12, 87, 179, 181, 183, 184, 185]`、VR `80`／`95`／`[73, 75]`、K-9 `64`／`67`／`[44, 47]`；旗標 `[None]*5`；本地 `hold/W-G.9-373-c2` ＝ 存（`54e142c`） |
| `2′` | 本補令 bytes／`sha256`／`SELF_SHA256`；來源檔；入倉 blob ＝ 來源；二檔 | 來源 ＝ **KL 主 checkout 之根**（第二處；施工樹之根無之）；`75289` B·`sha256` `4d02f4d1bdf429f818fdd2eb11454d9f2e624ce31c090284af8ce66ddc2331b3` ＝ KL 所貼；`SELF_SHA256` 自驗（受詞 `75211` B）＝ `fe4ad58c…18fd62` ＝ 檔載；入倉 blob 之 `sha256` ＝ 來源；CR `0`；`docs/reports/W-G.9-373R_工項二_二檔差異.diff` `91107` B／`4c995c8a…bf415`、停機報告 `73838` B／`26aab8ea…c84faa`（皆 ＝ 期） |
| `3′` | 塊 `F28`／`Fn3`；`git apply --check`；三器之施前、四器之施後之 blob；原碼之施後 | `F28` `21683` B·`68f9e42f…ca224`·`336` 列；`Fn3` `2582` B·`3afbb8a3…0ccdb`·`39` 列（皆 ＝ `§五` 項 `2`／`3`）；三器施前 blob ＝ `45ceb3ac…`／`ba39d356…`／`6278d18d…`；`Fn3` 之 `--check`／`apply` 皆 `rc 0`；施後四器 ＝ `dfae7e7c…`／`52f32e65…`／`884a1d56…`／`922ad406…`（逐位 ＝ `§五` 項 `4`）；原碼之差異檔之 `--check`／`apply` 皆 `rc 0`·施後 `app.py` ＝ `6ea0b01e…`（`1745326` B）、`verify/selection_pipeline.py` ＝ `2d7def55…`、`numstat` `661`／`437`、`13`／`3`（＝ `§五` 項 `5`） |
| `4′` | 前置′ | 項 `1`：`F28 selftest` `rc 1`·末列逐字 `⇒ 紅 ['E1', 'E3', 'E5', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'I1', 'I2', 'I3', 'M1', 'Q1', 'Q2']；rc 1`·`P0` `20／20`；項 `2`：`F23 wiring 7d8e954`／`F24 wiring d7a5ea4` `rc 0`·`⇒ 紅 []；rc 0`，`F25 wiring 3b35daa` `rc 1`·`⇒ 紅 ['X3', 'X5']；rc 1`，`F25 mutate` `rc 1`·`⇒ 突變 8（另基準一）；紅 ['M00']；rc 1`；項 `3`：`git diff --name-only e4e98a5 HEAD -- app.py verify/` ＝ 唯 `verify/probes/` 之四檔 ⇒ 前窗 `C:\Users\admin\o373` 之 `k6s3_pre_35.json`／`k6s3_pre_00.json`／`f8_pre_35.json`／`f8_pre_00.json` **沿用**（二進位複製至 `<O>`·`sha256` 二處同：`1623511f…71d81`／`5d22a05a…486a1`／`3c074e75…bb910`／`3b86505c…222270`） |
| `5` | 規格歧義而涉域上判斷 | 撰碼中 CC ⛔ 遇；**成就於審查之發現**（`§三` A1·歸停機款 `12`） |
| `6′` | `V-1′`〜`V-9′` | **皆符**（`§二`） |
| `7′` | push 之目標 | 工項零′、工項一′、本報告：皆 `verify/W-G.9-373-k966`（快轉·⛔ `--force`）；主線與二舊側支⛔ 動 |
| `8` | 三簿 | 工項三⛔ 辦（倉外模擬之 blob ＝ 原單 `§五-1` 項 `13`·`§五`） |
| `9′` | 收工閘′ | ⛔ 及（工項三／四候裁） |
| `10` | ⛔ 改塊、器、命令 | 未改 |
| `11` | 新檔之 `git check-ignore` | 本補令、`probe_WG9373p1_partrem.py` 皆無命中（`rc 1`）；本報告與差異檔推前另驗 |
| `12` | 唯讀審查之發現涉域上判斷或規格之漏載 | **成就**（`§三` A1） |

工項零′：`docs/orders/W-G.9-373_補令一.md`（`git show --numstat` ＝ `635`／`0`）·`dce634a`；推後 heads `38`。工項一′：`b73fbd4`·`numstat` ＝ `2`／`0`、`2`／`0`、`2`／`0`、`336`／`0`（逐位 ＝ 收工閘 `1′` 之期）。pre-flight：🔴 `0`／🟡 `1`（`P-1` `:225`·依補令 `§五` 項 `10` 具名豁免）；`P-5` ✅（受詞 `75211` B）；ℹ️ `P-3` `def main` ＝ `21799`-`29519`。原碼之上 `F28 selftest` ⇒ `rc 1`·紅 `['E1', 'E3', 'E5', 'S1', 'S3', 'S4', 'I1', 'I3', 'M1', 'Q1']`（＝ `§五` 項 `8` 之原碼之期·撰碼前之自跑）。

## `§二`　工項二之驗 `V-1′`〜`V-9′`：全數相符（審查前·於 `6e7272a`）

撰碼中先自跑 `selftest`／`wiring` 二十器（`dev_*`·皆 `rc 0`），後 `commit`，於 `commit` 全套正式跑（`*_post*`·`53` 器·三道·重器並行 ≤ `2`·`rc` 皆 `0`·stderr 合計 `0` B）。

| 驗 | 實 |
|---|---|
| `V-1′` | `F27 selftest`／`wiring`／`run` 皆 `rc 0`·`⇒ 紅 []；rc 0`；`run` 二退縮 `R1`〜`R3` 皆 ✅（`R2`：`R3` 之 `628-28(1)`／`628-29(1)` 並列 `69.2`／`65.75`·重劃前面積 `114.0` ⇒ `628-28(1)`；`R6` ⇒ `628-21(1)`；`R3`：members `51`／`52` 宗） |
| `V-2′` | `F23 selftest`／`wiring 7d8e954`／`run`、`F24 selftest`／`wiring d7a5ea4`／`run`（二退縮 `R1`〜`R5` ✅·`3.5` ΣΔG `+7.6700`／ΣΔ抵費地 `-7.6500`、`0.0` `+7.6800`／`-7.6400`）、`F16 selftest`／`run`、`F17 wiring`、`F14 selftest`／`run`、`F10 selftest`／`wiring`／`run`、`F25 wiring 3b35daa`／`mutate`（末列 `⇒ 突變 8（另基準一）；紅 []；rc 0`）：皆 `rc 0`·末列 ＝ 期 |
| `V-3′` | `F9 selftest`／`wiring`、`F26 selftest`、`F22 mut`、`F15 wiring`、`F19 mut`、`F18 selftest`／`wiring`、`probe_WG9352`〜`9354` 之 `selftest`／`wiring`、`probe_WG9344_k6s3.py selftest`（`selftest 9/9 ⇒ ✅`）、`probe_WG9344p1_pooltemp.py selftest`（`13/13`）、`probe_WG9345_screen.py wiring`（`⇒ rc 0（不符 0·器紅 0）`）、`probe_WG9349_k9296.py selftest`、`probe_WG9348_harvest_key.py`、`probe_WG9341_synth.py`（`ε ＝ 0.0002｜rc 0`）、`probe_WG9340_main_synth.py`（`紅項 [] 器紅 0`）：皆 `rc 0`·末列 ＝ 原單 `§五-1` 項 `15`（`F20` 依補令裁四去之） |
| `V-4′` | `k6s3 run` 二退縮 `rc 0`；`cmp`（對前置）二者皆 `rc 0`·末列逐字 `相異 0 項 ⇒ ✅ 同` |
| `V-5′` | `parity` 二退縮皆 `rc 0`·末列 `⇒ rc 0（不符 0 項）`；配地列 `35`／`34`、`36`／`35`·不符格 `0`；`Z` ＝ `[('harness', 'R1-抵費地-2')]`；`f3_k953_log` `34`／`43` 列、`f3_adj4_log` `1`／`1` 列、`f3_k6b_stage3_log` `19`／`0` 列、段三後 build `45`／`46`、`f3_end_block_merge` ＝ `{'退縮': …, '標的': [], '皆未達': {}}`（皆 ✅） |
| `V-6′` | `probe_WG9349_k9296.py run` 二退縮、`F21 run`、`probe_WG9346_failclosed.py run <repo> 3.5`、`F26 run`、`F9 run` 皆 `rc 0`·`⇒ 紅 []；rc 0`；`f8_post_35.json`／`f8_post_00.json` 與前置之 `f8_pre_*.json` 皆 `cmp` 逐位同 |
| `V-7′` | 生產碼 `34` 檔（`app.py` ＋ `git ls-tree b73fbd4 verify/` 之頂層 `*.py`·列數 `34`）對工項一′ 之端相異恰 `2`（`app.py`、`verify/selection_pipeline.py`）；`verify/` 之差唯 `M verify/selection_pipeline.py`；全倉之差唯此二檔 |
| `V-8′` | `*_post*` 之 `53` 器之 stderr 合計 `0` B |
| `V-9′` | `F28 selftest` `rc 0`·`E1`〜`E7`、`S1`〜`S6`、`I1`〜`I3`、`M1`〜`M2`、`Q1`〜`Q2` 皆 ✅·`P0` `20／20`·末列 `⇒ 紅 []；rc 0`（全文見附錄二） |

本案之配地⛔ 變：`V-1′ run`、`V-4′`〜`V-6′` 皆 ＝ 開工態。長跑之後施工樹 `git status --porcelain` ＝ 空（器⛔ 遺物於倉）。

## `§三`　唯讀獨立審查之發現（附則丙·`redistribution-reviewer`·⛔ 改檔·⛔ 跑長跑之器·約 `22` 分）

審查之總判（要旨）：補令 `§二` 之 `R-13′`／`R-14′`／`R-15′`／`R-16′`／`R-9′`／`R-11′` 逐條照規格落地；`F12` 之 `M6`／`M8` 之錨各恰一見；`_L` 之既有賦值⛔ 改；`ρ0` 之落點、受詞、分母合規格，`_a357`／`_aprime` 乘之、`_k357` 取未乘之值（k6b 內之 `a′` 皆經 `_aprime`·直呼 `a_prime(` 者唯 `_k357` 之分子）；前帳於 `state` 建立之前取副本（`_apply` 之呼叫全在 `_clone` 之上 ⇒ `_by0` 於取鍵之前⛔ 被改寫）；帳之合之趟於取鍵之環之後、`return` 之前，以 `.update`／`del` 為之（`_tp['段三部分併出'] = ` 全檔之數三態皆 `1`）；取鍵之環與三支⛔ 改；`R-15′` 之候選篩、`段三併出` 之聯集；`R-16′` 四表字面同一式、片之序與距離⛔ 改；`R-9′` 之剩下唯以帳、守恆（`A·ρ ＋ A·(1−ρ) − A` 實算 `0.0`）；NOTE `5` 三處皆改；頂層節點對 `104e4aa` 之相異恰所許之 `12` 名、新模組名恰原單之五、巢狀 def 增減皆 `0`（`_a357` 增一關鍵字參數 `_raw`·⛔ 違「新巢狀 def ⛔ 增」）；`.discard(` 之數三態皆 `1`；本案逐位⛔ 變（`x*1.0`、`x − sum([])` 實測逐位同·段三首呼 `ρ0` 皆 `1`、`_pre373` 空·末端塊合併再試於標的為空時逕回）。審查者另於倉外之拋棄式抽取（`git archive b73fbd4` ＋ 原碼之二檔）重跑 `F28 selftest` ⇒ 紅 `['E1', 'E3', 'E5', 'S1', 'S3', 'S4', 'I1', 'I3', 'M1', 'Q1']`（＝ `§五` 項 `8`）。**(B) 純實作之瑕 `0` 項；(C) NOTE `6` 項；(A) 域／規格 `1` 項（A1·本案不觸）。**

### A1　同一趟之內，`K-9-67` 之重劃前面積之表看不到本趟已部分併出之量——規格未定

- **受詞**：補令 `§二` `R-16′`「四處之重劃前面積之表……之每一片之值 ＝ 其分攤登記面積 − 其 `段三部分併出` 之值之和（無該鍵 ⇒ `0`·**各處之輸入之態**）」；其所據 ＝ 補令 `§一` 裁六 ①「部分併出之剩下所含者唯其剩下」。
- **事實**：帳（`段三部分併出`）唯於各處（段三 `k6b_stage3_run`、手冊先行 `k953_manual_run`、第一趟 `adj4_pass1_run`）之**末**始寫入（`R-5` (d)、`R-14′` ②）；而同一趟之內，建地片一經部分併出（`R-5` (a) 之試施·`面積_m2` 減其量、仍留 build），**其後之試算**（`alloc_state`·harness `verify/selection_pipeline.py` 之 `run_step_g`，含入池閘 `k929_6_fixpoint`）所受之 build 中，該片之 `面積_m2` 已減而其帳未寫 ⇒
  - 入池閘之 `_pre_k967`（取其輸入之 build·`R-16′` 之式）於該片得 `分攤 − 前帳`（多計本趟已併出之 `v`）；
  - 段三第 `5` 項之 `_pa`（取 `_by0`）、手冊先行之 `_pre953`（取 `_tin953`）、第一趟之 `_pre_a4`（取 `_tin_a4`）——皆取該處之輸入之態（趟首之帳）——於「受併宗之成員（趟中之試算之 `members`）含本趟已部分併出之片」者同。
- **CC 之復現**（`<O>\repro_A1.py`·倉外·唯讀·於 `6e7272a`·全文與出艙見附錄三）：
  - (1) 段三（`F16` 之 `_world4`·`F28` 之 `S2` 之形·`Y1(1)` 分攤 `90`）：包 `alloc_state` 記每次試算所見之 `Y1(1)`——題一 `4` 已部分併出 `X1(1)` `20` 之後之試算，`Y1(1)` 之 `面積_m2` ＝ `-20.0`（及試施中之 `-70.0` 等）而 `段三部分併出` **未帶** ⇒ `R-16′` 之式之值恆 `90.0`；趟畢始為 `面積_m2` `-70.0`、`段三部分併出` `{'X1(1)': 20.0, 'Z1(1)': 50.0}`、其值 `20.0`。
  - (2) 入池閘之代表宗（`F28` 之 `Q` 之玩具·Y1 分攤 `130`·已部分併出 `40`·前受併入 `10` ⇒ `a` `100`·與 Y2〔`a` `100`〕之 `G` 並列 `60`）：帳已寫 ⇒ `['Y2']`；**帳未寫（＝ 趟中之試算之輸入之形）⇒ `['Y1']`**（剩下 `90` ＜ `100` ⇒ 性質之期 `Y2`）。
- **土地後果**：本案⛔ 觸（三處皆一次全部試併即過、無部分併出之片；`V-1′`／`V-4′`〜`V-6′`）。他案——唯於趟中之試算有 `K-9-67` 之並列（`G` 於 `0.01 ㎡` 同），且其並列之宗或其成員含本趟已部分併出之片時，始可翻轉入池閘之代表宗或受併宗之擇；試算之結果（`kept`／`bad_pools`）又入「不影響原位次」之檢核 ⇒ 得及併入之成否。原碼（取全額之分攤登記面積）之差更大；本補令之 `R-16′` 唯補其跨趟之部分。
- **CC 之判**：規格之字面（「各處之輸入之態」）無歧義、CC 照之；然其所據之性質（裁六 ①）於趟中⛔ 成立——與補令自誤乙（「閘繫於代理量而非性質」）同族，而補令未及趟中之態 ⇒ **規格之漏載**。補之須於三處之試施（`R-5` (a)）中寫趟中之帳（或令重劃前面積之表改讀他物），涉 `R-5` 之設計 ⇒ ⛔ CC 自定（停機款 `12`）。
- **待裁之讀法**（⛔ CC 自擇）：甲 照現碼（`R-16′` 之字面·趟中之試算以趟首之帳計；他案之並列時得與性質不合）；乙 三處之試施於建地之部分併出時即於拷貝中寫其帳（`段三部分併出` 加 `v`·`段三併出` 加受併宗），令趟中之試算所見之帳即其性質（趟末之帳之合須隨之改，免重加）；丙 他式（例：入池閘等四表改以「分攤登記面積 −（輸入之 `面積_m2` 之減量）」之類定之——然 `面積_m2` 兼載受併入之量，補令裁二已斥之）。各讀法之土地後果於他案相異（唯並列時）。

### (B) 純實作之瑕

無。

### (C) NOTE 級（審查者列·不擋·⛔ 改·候復工時一併處置）

1. `_a357` 之關鍵字參數 `_raw` 遮蔽 `k6b_stage3_run` 外層之多邊形之表 `_raw`（`_a357` 本體⛔ 用之 ⇒ 無行為之影響）。改名須重跑 `F17`／`F23`／`F24 wiring`。
2. `R-13′` 之推導式於每元素重算 `set(locked or ())`／`set(corner_lots or ())`（唯效率）；建地之判、`段三餘量` 之判⛔ 再查類別——於既有之不變量（建地片⛔ 帶 `段三餘量`、道路片⛔ 在 build）之下與規格等價。
3. 前帳若唯 `段三部分併出` 而無 `段三併出`（依各寫者之規則不可達），帳之合將建 `段三併出 ＝ []`，`adj_intake` 遇之停機（loud·⛔ 靜默）。
4. 段三之「整筆併入」之旗（`_rnd373` 之 `_one`）唯看本趟之 `_part`：前趟已部分併出之建地於本趟以單一要求全數併出者記 `[x]`（甲案之下 ＝ 與一分未併者同；唯及紀錄，倉內無程式讀此欄）。
5. 舊述仍存而已為其後之 `W-G.9-373` 段所代：`k6b_stage3_run` 之 docstring 之 `W-G.9-357` 段（「可拆分者逐受併宗以最大面積……」）、`_t14_357` 之首註（「七項 4」「最大面積」）、`adj4_pass1_run` 之 docstring 首段（「於同一宗逐片……取最大面積」）、取鍵之環前之註（「全無併入 ⇒ 唯 段三餘量 ＝ a(x)」·今之值 ＝ `a·ρ0`）——皆⛔ 在 NOTE `5` 所列三處之內。
6. 段三之帳之合以已四捨五入之本趟之量相加，手冊先行／第一趟則以原值相加後四捨五入（差 ≤ `0.00005`）。

## `§四`　設計說明（補令 `§二` 末·工項二之碼·⛔ 推）

對原碼（`54e142c` 之二檔）之改動唯 `app.py`（`verify/selection_pipeline.py` ＝ 原碼）；其全文見附錄四。逐條：

| 條 | 落點（`6e7272a` 之 `app.py`） | 字樣（可 grep） | 要 |
|---|---|---|---|
| `R-13′` | `end_block_merge_run`·`_L` 之既有賦值之後 | `_bin_ebm = {b['暫編地號'] for b in (build_parcels or [])}`、`_L = _L - {t['暫編地號'] for t in temp_parcels` | 自 `_L` 去 `temp_parcels` 中「`段三併出` 非空 ∧（在本函式之輸入之 `build_parcels` ∨ `round(段三餘量, 4) > 0`）∧ ⛔ 在 `locked` ∧ ⛔ 在 `corner_lots`」者；`_L` 之既有賦值（`F12` `M6`）、`M8`、候選之收集⛔ 改；⛔ `.discard(`；docstring ③ 改述為「已全數併出者（部分併出之剩下⛔ 除外·KL 裁 `2026-10-08`）」 |
| `R-14′` ① | `k6b_stage3_run`·`_by0`／`_bids0` 之環之後、`state = _mk_state(_temp0, _bids0)` 之前 | `_rho0_373, _pre373 = {}, {}`、`_den373`、`return _v if _raw else _v * _rho0_373[x]`、`* _rho0_373[src]`、`/ _a357(x, _raw=True)` | 非建地之片（`街廓分類 ＝ 道路` 或 負擔屬性 ≠ `可建築土地`·＝ `_kind` 之非 `bld`）而 `段三併出` 非空且帶 `段三餘量` 者 `ρ0 ＝ 段三餘量 ÷ (分攤 ＋ 面積_m2)`（分母 ≤ `0` ⇒ `RuntimeError`）；他片 `1.0`。`_a357(x)` 回 `a·ρ0`（其 `_raw=True` 回 `a`·唯 `_k357` 用之 ⇒ 折算比 ＝ `a′ ÷ a`、二者皆未乘）；`_aprime` 乘 `src` 之 `ρ0`。前帳（`段三併出` 之集、`段三部分併出` 之副本）於同處存 `_pre373`（`_by0` 之物件與初始 `state` 同一 ⇒ 前帳⛔ 於末讀 `_by0`） |
| `R-14′` ② | `k6b_stage3_run`·取鍵之環（與其三支·⛔ 改）之後、`return` 之前 | `_bnow373`、`for _pid in sorted(set(_pre373) & (set(_left) \| set(marks) \| merged_out)):`、`_acc373` | 受詞 ＝ 前帳非空 ∩ 本趟所觸；`段三併出` ＝ 前帳之集 ∪ 現之集（`.update`）；帶 `段三餘量` 或（建地 ∧ 仍在 build）⇒ `段三部分併出` ＝ 前帳 ⊕ 現之帳（逐受併宗相加·`round(·, 4) > 0`·`.update`）；否則有之 ⇒ `del`。未觸者⛔ 動。⛔ 字樣 `_tp['段三部分併出'] = `；`for` 之 iter 之寫法避 `set(marks) \| set(_left)` 之子字串（`F17` `W11` 之「取鍵之環恰一」） |
| `R-15′` | `k953_manual_run`·候選篩；輸出之鍵之環 | `if (('段三併出' in _tq) or ('段三餘量' in _tq)) and not (_so953 == 'bld' and _pk953 in _bin953):`、`_d.update({'段三併出': sorted(set(_d.get('段三併出') or ()) \| _marks953[_x])})` | `_so953` 之取移至篩之前（純函式）；建地片而在 build 者受理；他片帶鍵者略；`段三併出` 之直寫改為聯集；建地之部分併出之 `段三部分併出` 之合既有者照原碼 |
| `R-16′` | `k929_6_fixpoint` 之 `_pre_k967`；`k6b_stage3_run` 之 `_p5_373` 之 `_pa`；`k953_manual_run` 之 `_pre953`；`adj4_pass1_run` 之 `_pre_a4` | `- sum(float(_v) for _v in (… .get('段三部分併出') or {}).values())` | 四表之每一片 ＝ `float(t.get('分攤登記面積_m2', 0) or 0) − Σ段三部分併出`（無鍵 ⇒ `0`·各處之輸入之態）；片之序（`_ga`、`_order953`）與距離⛔ 改。**A1（`§三`）即此條於趟中之態之漏載** |
| `R-9′` | `adj_intake`·建地之部分併出之支 | `_mg_b = sum(…)` 移於前、`_now_b = _a(t) - _mg_b` | 剩下以帳定之、⛔ 讀 `面積_m2`；停機之條件與訊息⛔ 變；原有面積／段三併出面積仍以原單之 ρ 形（`_a × ρ`、`_a × (1 − ρ)`·`ρ ＝ now ÷ (now ＋ merged)`·二式等價·擇一） |
| `R-11′` | docstring 與註 | `🔧 補令一（R-…）` 之段 | `end_block_merge_run` ③；`k6b_stage3_run`（`R-14′`／`R-16′` 之段）；`k953_manual_run`（`R-15′`／`R-16′` 之段；停機列之「可拆分之片之最大面積之試」改為「每一受併之街廓之 `k966_block_merge` 之前……之每一要求」）；`adj_intake`（`R-9′`）；`k929_6_fixpoint`、`adj4_pass1_run`（`R-16′`）；`adj4` 之模組頭註（`K-9-66`／`K-9-68` 之述代「逐片……取最大面積」）；`k6b_stage3_run` 內一行註之已去之名（改為「其舊之巢狀皆已去之」）。⛔ 及行為 |

🔒 **自查**：新模組名 `0`、新巢狀 def `0`（`_a357` 增關鍵字參數）；`F12 wiring`（`M6`／`M8`／`W7`）、`F13 wiring`、`F17 wiring`（`W0`〜`W12` 與十五突變）、`F23 wiring 7d8e954`（`W6`〜`W8`）、`F24 wiring d7a5ea4`（`W5`〜`W7`）、`F25 wiring 3b35daa`（`X1`〜`X5`）／`mutate`（八突變）、`F10 wiring`（`W4`）於撰碼中（`dev_*`）與 `commit` 後（`*_post*`）皆綠；`.discard(` 之數 `1 → 1`；新增之列逾 `120` 字者 `0`；`app.py` 之真 `0x0D` `0`。

## `§五`　工項三之備（⛔ 辦·候裁）

- 塊 `K16`（`13711` B·`fbd6dab3…d59d42`·`86` 列）、`E16`（`2044` B·`105e46e7…bb811`·`12` 列）、`P26`（`4341` B·`e17010e7…5c611`·`22` 列）自原單依圍欄之逐列索引抽出 ＝ 原單 `§五-1` 項 `10`〜`12`。
- 倉外模擬（`cat <簿> <塊> | git hash-object --stdin`·⛔ 寫倉）：`K-6` 典 ⇒ `47b15cfe2f4446ecc03fc810bd42e3e2bd764f66`、自誤簿 ⇒ `58c4b6311d5a54f6d38e697c1cb2f8e31692c89c`、`CLAUDE.md` ⇒ `2aaa54c5ccf8c85288bfe9de7339c3b5fe5bc593`——皆 ＝ 原單 `§五-1` 項 `13`；三簿之施前 bytes `604411`／`1141491`／`357698`、blob `2a458e30…`／`1c921b32…`／`132d8ec8…`（＝ 原單 `§一` 項 `1`）。
- 塊 `CK`（`1539` B·`00cd3949…22e554d`·`31` 列）、`GF`（`2445` B·`b11edb77…ce10cc`·`47` 列）自 `docs/orders/W-G.9-365_輕量單.md` 之附錄午／巳抽出 ＝ 原單 `§五-1` 項 `14`（存 `<O>\checkidx.py`、`<O>\gen_fa_index.py`·⛔ 入倉）。
- 塊 `K16` 之「落地狀態」（「🔶 側支 `verify/W-G.9-373-k966`（`W-G.9-373` 工項二）」）：補令裁五令⛔ 改；然工項二之碼今再⛔ 推 ⇒ 若依原式入典，其文與倉態不符（同前窗停機報告 `§六` 末項）——候裁後隨復工之單定之。

## `§六`　CC 之自捕與自解

**自捕**：
1. 工項三之塊之初抽（倉外·⛔ 及倉）：Bash 之迴圈以雙引號寫輸出路徑 `"C:\\Users\\admin\\o373p1\\$b.md"`，其 `\\$` 致變數未展開 ⇒ 三塊皆寫入同一雜檔 `C:\Users\admin\o373p1$b.md`（`<O>` 之外·`4341` B·末寫者 ＝ `P26`），而三簿之模擬因讀不到 `<O>\K16.md` 等而得施前之 blob；即察、刪其雜檔（CC 自生之檔），改以單引號之絕對路徑逐塊重抽（`bytes`／`sha256` ＝ 期）、重模擬（＝ 期）。倉與受測物⛔ 涉。
2. `R-14′` 之撰碼中自察：`_by0` 之物件與初始 `state` 之物件同一，取鍵之環得寫之 ⇒ 前帳若於帳之合之時讀 `_by0` 則或讀到本趟所寫者；故前帳於 `state` 建立之前另存副本（`_pre373`）。
3. `R-14′` 之撰碼中自察：取鍵之環之第二支（`_tp['段三餘量'] = round(_a357(_pid), 4)`）為 `F17` 之錨（`probe_WG9358_k948_wiring.py` 之 `W11` 之逐字之比）⛔ 得改 ⇒ `段三餘量` 之剩下（`a·ρ0`）須由 `_a357` 自身乘 `ρ0`；而折算比須未乘 ⇒ `_a357` 增關鍵字參數 `_raw`（⛔ 增巢狀 def）。

**自解清單**（五項全滿足者·⛔ 及土地）：
1. 本停機報告與差異檔之檔名（`W-G.9-373R_補令一_工項二停機上呈_唯讀審查之發現.md`、`W-G.9-373R_補令一_工項二_二檔差異.diff`）——零土地後果（檔名）；零生產碼；可機驗（`git grep -l -F "W-G.9-373R_補令一"` 於 `b73fbd4` ＝ `0` 檔·對照 `W-G.9-373R_工項二停機上呈` ＝ `1` 檔〔非恆空〕；工項四之預定名 `W-G.9-373R_K-9-66至68之落地_*`、`W-G.9-373R_工項二_補令一改動` 皆⛔ 用）；可逆（新檔）；記於此。依前窗之停機報告之例（`W-G.9-373R_工項二停機上呈_…`）。
2. 本地 ref 之名 `hold/W-G.9-373p1-c2`（工項二之碼之存處·⛔ 推）——零土地後果；零生產碼；可機驗（`git for-each-ref` 之開工態唯 `hold/W-G.9-373-c2` 一名含 `W-G.9-373`；遠端無之）；可逆（ref 可刪）；記於此。

## `§七`　耗時（本機·約數·自 `<O>` 之檔時與 `commit` 之時）

| 段 | 起訖 | 約 |
|---|---|---|
| 開場（`§零-0`）·工項零′／一′ | `04:47`〜`04:51` | `4` 分 |
| 前置′（五器） | `04:51`〜`04:52` | `1` 分 |
| 原碼之施·撰碼（含 `dev_*` 之二十器之自跑） | `04:52`〜`05:05` | `13` 分 |
| `commit` 後之驗（`*_post*`·三道·`53` 器） | `05:05`〜`05:42` | `37` 分（`F14 run` `2140` s 為最） |
| 唯讀獨立審查 | `05:43`〜`06:05` | `22` 分 |
| A1 之復現與本報告 | `06:06`〜 | — |

## `§八`　候裁之題（發單側／KL）

1. **A1**（`§三`）：同一趟之內（段三、手冊先行、第一趟之各一呼之中），建地之部分併出既施而其帳未寫之時，`K-9-67` 之重劃前面積（入池閘之代表宗之表 `_pre_k967` 與三處之受併宗之表）於該片取何值——甲 照現碼（趟首之帳）／乙 試施即寫趟中之帳／丙 他式。
2. NOTE `1`〜`6`（`§三` (C)）之處置（皆不擋）。
3. 復工之單：工項二之碼（`hold/W-G.9-373p1-c2` ＝ `6e7272a`）之續改（A1 之裁之落地與 NOTE 之處置）、其驗之重跑、審查之重辦；工項三之塊 `K16` 之「落地狀態」之文；工項四。

## 附錄　出艙（逐字）

### 附錄一　一覽（`<O>\*.rc`·逐字·`[標籤] rc stderr 秒 末列`；標籤 `pre_*` ＝ 前置′、`orig_*` ＝ 原碼之上之撰碼前自跑、`dev_*` ＝ 撰碼中之自跑、`*_post*` ＝ 工項二之 commit 之驗；長列截於 `300` 字）

```
[F10_run_post] rc=0 stderr=0B t=320.7s last=⇒ 紅 []；rc 0
[F10_selftest_post] rc=0 stderr=0B t=21.9s last=⇒ 紅 []；rc 0
[F10_wiring_post] rc=0 stderr=0B t=60.9s last=⇒ 紅 []；rc 0
[F14_run_post] rc=0 stderr=0B t=2139.8s last=⇒ 紅 []；rc 0
[F14_selftest_post] rc=0 stderr=0B t=4.0s last=⇒ 紅 []；rc 0
[F15_wiring_post] rc=0 stderr=0B t=76.8s last=⇒ 紅 []；rc 0
[F16_run_post] rc=0 stderr=0B t=232.6s last=⇒ 紅 []；rc 0
[F16_selftest_post] rc=0 stderr=0B t=4.2s last=⇒ 紅 []；rc 0
[F17_wiring_post] rc=0 stderr=0B t=78.2s last=⇒ 紅 []；rc 0
[F18_selftest_post] rc=0 stderr=0B t=4.2s last=⇒ 紅 []；rc 0
[F18_wiring_post] rc=0 stderr=0B t=39.1s last=⇒ 紅 []；rc 0
[F19_mut_post] rc=0 stderr=0B t=754.6s last=⇒ 紅 []；rc 0
[F21_run_post] rc=0 stderr=0B t=174.3s last=⇒ 紅 []；rc 0
[F22_mut_post] rc=0 stderr=0B t=506.8s last=⇒ 紅 []；rc 0
[F23_run_post] rc=0 stderr=0B t=500.7s last=⇒ 紅 []；rc 0
[F23_selftest_post] rc=0 stderr=0B t=4.3s last=⇒ 紅 []；rc 0
[F23_wiring_post] rc=0 stderr=0B t=39.2s last=⇒ 紅 []；rc 0
[F24_run_post] rc=0 stderr=0B t=812.3s last=⇒ 紅 []；rc 0
[F24_selftest_post] rc=0 stderr=0B t=4.0s last=⇒ 紅 []；rc 0
[F24_wiring_post] rc=0 stderr=0B t=38.5s last=⇒ 紅 []；rc 0
[F25_mutate_post] rc=0 stderr=0B t=24.2s last=⇒ 突變 8（另基準一）；紅 []；rc 0
[F25_wiring_post] rc=0 stderr=0B t=16.8s last=⇒ 紅 []；rc 0
[F26_run_post] rc=0 stderr=0B t=306.8s last=⇒ 紅 []；rc 0
[F26_selftest_post] rc=0 stderr=0B t=4.1s last=⇒ 紅 []；rc 0
[F27_run_post] rc=0 stderr=0B t=431.1s last=⇒ 紅 []；rc 0
[F27_selftest_post] rc=0 stderr=0B t=4.0s last=⇒ 紅 []；rc 0
[F27_wiring_post] rc=0 stderr=0B t=3.0s last=⇒ 紅 []；rc 0
[F28_selftest_post] rc=0 stderr=0B t=4.4s last=⇒ 紅 []；rc 0
[F9_run_post] rc=0 stderr=0B t=4.5s last=⇒ 紅 []；rc 0
[F9_selftest_post] rc=0 stderr=0B t=34.4s last=⇒ 紅 []；rc 0
[F9_wiring_post] rc=0 stderr=0B t=61.9s last=⇒ 紅 []；rc 0
[dev_F10_selftest] rc=0 stderr=0B t=21.6s last=⇒ 紅 []；rc 0
[dev_F10_wiring] rc=0 stderr=0B t=50.9s last=⇒ 紅 []；rc 0
[dev_F11_selftest] rc=0 stderr=0B t=38.7s last=⇒ 紅 []；rc 0
[dev_F11_wiring] rc=0 stderr=0B t=121.7s last=⇒ 紅 []；rc 0
[dev_F12_selftest] rc=0 stderr=0B t=35.9s last=⇒ 紅 []；rc 0
[dev_F12_wiring] rc=0 stderr=0B t=93.0s last=⇒ 紅 []；rc 0
[dev_F13_selftest] rc=0 stderr=0B t=69.0s last=⇒ 紅 []；rc 0
[dev_F13_wiring] rc=0 stderr=0B t=59.4s last=⇒ 紅 []；rc 0
[dev_F14_selftest] rc=0 stderr=0B t=4.6s last=⇒ 紅 []；rc 0
[dev_F16_selftest] rc=0 stderr=0B t=4.6s last=⇒ 紅 []；rc 0
[dev_F17_wiring] rc=0 stderr=0B t=90.1s last=⇒ 紅 []；rc 0
[dev_F23_selftest] rc=0 stderr=0B t=4.8s last=⇒ 紅 []；rc 0
[dev_F23_wiring] rc=0 stderr=0B t=44.4s last=⇒ 紅 []；rc 0
[dev_F24_selftest] rc=0 stderr=0B t=4.5s last=⇒ 紅 []；rc 0
[dev_F24_wiring] rc=0 stderr=0B t=45.5s last=⇒ 紅 []；rc 0
[dev_F25_mutate] rc=0 stderr=0B t=25.2s last=⇒ 突變 8（另基準一）；紅 []；rc 0
[dev_F25_wiring] rc=0 stderr=0B t=17.7s last=⇒ 紅 []；rc 0
[dev_F27_selftest] rc=0 stderr=0B t=4.5s last=⇒ 紅 []；rc 0
[dev_F27_wiring] rc=0 stderr=0B t=3.6s last=⇒ 紅 []；rc 0
[dev_F28_selftest] rc=0 stderr=0B t=4.7s last=⇒ 紅 []；rc 0
[e9352_selftest_post] rc=0 stderr=0B t=36.6s last=⇒ 紅 []；rc 0
[e9352_wiring_post] rc=0 stderr=0B t=136.5s last=⇒ 紅 []；rc 0
[e9353_selftest_post] rc=0 stderr=0B t=31.2s last=⇒ 紅 []；rc 0
[e9353_wiring_post] rc=0 stderr=0B t=92.9s last=⇒ 紅 []；rc 0
[e9354_selftest_post] rc=0 stderr=0B t=65.0s last=⇒ 紅 []；rc 0
[e9354_wiring_post] rc=0 stderr=0B t=57.7s last=⇒ 紅 []；rc 0
[f8_post_00] rc=0 stderr=0B t=135.3s last=⇒ 紅 []；rc 0
[f8_post_35] rc=0 stderr=0B t=198.0s last=⇒ 紅 []；rc 0
[failclosed_post] rc=0 stderr=0B t=416.0s last=⇒ 紅 []；rc 0
[harvest_key_post] rc=0 stderr=0B t=8.5s last=⇒ 紅 []；rc 0
[k6s3_post_00] rc=0 stderr=0B t=186.9s last={"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)"}, "R5": {"p1_end": "628-18(2)", "p2_end": null}, "R2": {"p1_end": "628-41(1)", "p2_end": null}, "R3": {"…
[k6s3_post_35] rc=0 stderr=0B t=265.2s last={"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)"}, "R5": {"p1_end": "628-45(1)", "p2_end": null}, "R2": {"p1_end": "628-41(1)", "p2_end": null}, "R3": {"…
[k6s3_selftest_post] rc=0 stderr=0B t=0.1s last=selftest 9/9 ⇒ ✅
[k6s3cmp_post_00] rc=0 stderr=0B t=0.1s last=相異 0 項 ⇒ ✅ 同
[k6s3cmp_post_35] rc=0 stderr=0B t=0.1s last=相異 0 項 ⇒ ✅ 同
[k9296_selftest_post] rc=0 stderr=0B t=4.2s last=⇒ 紅 []；rc 0
[orig_F28_selftest] rc=1 stderr=0B t=4.1s last=⇒ 紅 ['E1', 'E3', 'E5', 'S1', 'S3', 'S4', 'I1', 'I3', 'M1', 'Q1']；rc 1
[parity00_post] rc=0 stderr=0B t=388.0s last=⇒ rc 0（不符 0 項）
[parity35_post] rc=0 stderr=0B t=618.3s last=⇒ rc 0（不符 0 項）
[pooltemp_selftest_post] rc=0 stderr=0B t=0.1s last=selftest 13/13 ⇒ ✅
[pre_F23_wiring] rc=0 stderr=0B t=39.5s last=⇒ 紅 []；rc 0
[pre_F24_wiring] rc=0 stderr=0B t=40.0s last=⇒ 紅 []；rc 0
[pre_F25_mutate] rc=1 stderr=0B t=21.9s last=⇒ 突變 8（另基準一）；紅 ['M00']；rc 1
[pre_F25_wiring] rc=1 stderr=0B t=15.5s last=⇒ 紅 ['X3', 'X5']；rc 1
[pre_F28_selftest] rc=1 stderr=0B t=5.5s last=⇒ 紅 ['E1', 'E3', 'E5', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'I1', 'I2', 'I3', 'M1', 'Q1', 'Q2']；rc 1
[screen_wiring_post] rc=0 stderr=0B t=52.0s last=⇒ rc 0（不符 0·器紅 0）
[synth9340_post] rc=0 stderr=0B t=40.7s last=紅項 [] 器紅 0
[synth9341_post] rc=0 stderr=0B t=4.1s last=ε ＝ 0.0002｜rc 0
```

### 附錄二　`F28 selftest`（`V-9′`·`<O>\F28_selftest_post.out`·全文）

```
── 部分併入他處後剩下之土地於其後各段（甲案）──
  ✅ E1 末端塊合併再試：同地主相鄰之 C1(2) 為部分併出之剩下（50）⇒ 得併入（⛔ 除外）：100 ＋ 50 ＝ 150 ⇒ ① 成；C1(2) 全數併出 ⇒ 段三併出 取聯集、去 段三部分併出
  ✅ E2 對照：C1(2) 一分未併而 a ＝ 50 ⇒ 同 E1 之配地
  ✅ E3 末端塊合併再試：同地主之道路片 R2(1) 為部分併出之剩下（30）⇒ 得併入、其量 ＝ 30：90 ＋ 30 ＝ 120 ⇒ ② 成；R2 全數併出 ⇒ 段三併出 取聯集、去 段三部分併出／段三餘量
  ✅ E4 對照：R2(1) 一分未併而 a ＝ 30 ⇒ 同 E3 之配地
  ✅ E5 本趟未觸之片之帳⛔ 動：同 E1，另道路片 R2(1)（他地主·帶前帳·本趟未觸）⇒ 其三鍵照舊
  ✅ E6 部分併出之剩下 C1(2) 已分配予街角（corner_lots）⇒ 照舊除外：C1(1) 未成；C2(1) 以 ② 道路成；C1(2) 之帳⛔ 動
  ✅ E7 對照：C1(2) 一分未併而 a ＝ 50、已分配予街角 ⇒ 同 E6 之配地
  ✅ S1 段三：Y1(1) 帶前帳（Q9(1) 5·面積_m2 −5）而本趟再部分併出（X1(1) 20、Z1(1) 50）⇒ 段三併出 聯集、段三部分併出 相加、面積_m2 −75、仍在 build
  ✅ S2 對照：Y1(1) ⛔ 帶前帳 ⇒ 本趟之帳唯 X1(1) 20、Z1(1) 50、面積_m2 −70
  ✅ S3 段三：道路片 X3(1)（分攤 80）帶前帳（已併出 40·段三餘量 40）⇒ 其可併之量 ＝ 40：半 20 ⇒ 100 ＋ 20 ＜ 130 不成，整片 40 ⇒ 140 ⇒ ② 成；X3 全數併出 ⇒ 段三併出 聯集（Q8(1)、X1(1)）、去他二鍵
  ✅ S4 段三：X3(1) 帶前帳（已併出 20·段三餘量 60）⇒ 半 30 ⇒ 100 ＋ 30 ＝ 130 ⇒ ②半 成；其另半於題一 4 之全量 30（折算比 ＝ 1·⛔ 受 ρ0 之影響）未成（BX 已滿）、第 5 項 Z1(1) 亦滿 ⇒ 段三部分併出 Q8(1) 20 ＋ X1(1) 30、段三餘量 30；Y1(1) 題一 4 併 X1(1) 30、第 5 項併 Z1(1) 50 ⇒ 面積_m2 −80
  ✅ S5 對照：X3(1) 一分未併而 a ＝ 40 ⇒ 同 S3 之配地
  ✅ S6 對照：X3(1) 一分未併而 a ＝ 60 ⇒ 同 S4 之配地
  ✅ I1 調配之輸入：部分併出之建地（其單元不配地·分攤 50·已併出 20）其後受併入 30 ⇒ 原有面積 30、段三併出面積 20
  ✅ I2 對照：⛔ 受併入 ⇒ 原有面積 30、段三併出面積 20
  ✅ I3 其單元配地而其後受併入 30 ⇒ 原位次配地·原有面積 30、段三併出面積 20
  ✅ M1 手冊先行：X1(1) 為部分併出之剩下（分攤 60·已併出 10·仍在 build）⇒ 受理：跨分配線整筆併入 X1(2) 50；段三併出 聯集、去 段三部分併出
  ✅ M2 對照：X1(1) 一分未併而 a ＝ 50 ⇒ 同 M1 之併入
  ✅ Q1 入池閘之代表宗：Y1 為部分併出之剩下（分攤 130·已併出 40·其後受併入 10 ⇒ a 100）與 Y2（a 100）G 並列 60 ⇒ 重劃前面積 Y1 ＝ 130 − 40 ＝ 90 ＜ 100 ⇒ Y2
  ✅ Q2 對照：Y1 一分未併而分攤 90、其後受併入 10 ⇒ 同 Q1
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 20／20
⇒ 紅 []；rc 0
```

### `k6s3cmp_post_35`（全文）

```
相異 0 項 ⇒ ✅ 同
```

### `k6s3cmp_post_00`（全文）

```
相異 0 項 ⇒ ✅ 同
```

### `parity35_post`（末十五列）

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（19 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（13 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 3.5, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（34 列）
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

### `parity00_post`（末十五列）

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（0 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（0 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 0.0, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（43 列）
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

### 附錄三　A1 之復現（`<O>\repro_A1.py`·倉外·⛔ 入倉；呼叫：`python repro_A1.py <repo>`·於 `6e7272a`）

出艙（逐字）：

```
(1) Y1(1) 之分攤登記面積 90.0
(1) 本趟之試算所見之 Y1(1)（面積_m2, 帶段三部分併出, R-16′ 式之值）之相異者： [(-72.5, False, 90.0), (-70.31, False, 90.0), (-70.03, False, 90.0), (-70.01, False, 90.0), (-70.0, False, 90.0), (-69.99, False, 90.0), (-69.96, False, 90.0), (-69.89, False, 90.0), (-69.76, False, 90.0), (-69.21, False, 90.0), (-68.12, False, 90.0), (-63.75, False, 90.0), (-55.0, False, 90.0), (-45.0, False, 90.0), (-22.5, False, 90.0), (-21.09, False, 90.0), (-20.38, False, 90.0), (-20.03, False, 90.0), (-20.01, False, 90.0), (-20.0, False, 90.0), (-19.98, False, 90.0), (-19.94, False, 90.0), (-19.85, False, 90.0), (-19.68, False, 90.0), (-16.87, False, 90.0), (-11.25, False, 90.0), (0.0, False, 90.0), (40.0, False, 90.0)]
(1) 本趟畢之 Y1(1)：面積_m2 -70.0 段三部分併出 {'X1(1)': 20.0, 'Z1(1)': 50.0} R-16′ 式之值 20.0
(2) 入池閘之代表宗：帳已寫 ⇒ ['Y2'] ｜帳未寫（趟中之試算之輸入）⇒ ['Y1'] （Y1 之剩下 90 ＜ Y2 之 100 ⇒ 性質之期 Y2）
```

原文：

```python
"""W-G.9-373 補令一 工項二 停機上呈之復現（倉外·唯讀·玩具）：A1——同一趟之內，K-9-67 之重劃前面積之表看不到本趟已部分
併出之量（帳於各處之末始寫）。
 (1) 段三（F16 之 _world4·F28 之 S2 之形）：包 alloc_state，記每次試算所見之 Y1(1)——本趟題一 4 已部分併出 X1(1) 20 之後之
     試算，Y1(1) 之 面積_m2 已減，而其 段三部分併出 未寫 ⇒ 依 R-16′ 之式（分攤 − 段三部分併出之和）之值 ＝ 全額。
 (2) 入池閘之代表宗（F28 之 Q 之玩具）：Y1 之 面積_m2 已減其所併出 40（且前受併入 10），帳已寫 ⇒ Y2；帳未寫（＝ 趟中之試算之輸入）⇒ Y1。
呼叫：python repro_A1.py <repo>"""
import contextlib, importlib.util, io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
REPO = sys.argv[1]
sys.path.insert(0, os.path.join(REPO, 'verify'))
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns, _st = harvest(os.path.join(REPO, 'app.py'))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO, rel))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


f16 = load('verify/probes/probe_WG9357_k948.py', 'f16a1')
f27 = load('verify/probes/probe_WG9373_k966.py', 'f27a1')
f28 = load('verify/probes/probe_WG9373p1_partrem.py', 'f28a1')


def pre_tab(t):
    # R-16′ 之式（四處同一式）
    return float(t.get('分攤登記面積_m2', 0) or 0) - sum(float(v) for v in (t.get('段三部分併出') or {}).values())


# ── (1) 段三之趟中之試算所見 ──
temp, own, blocks, cl = f16._world4()
build = [t for t in temp if t['街廓分類'] == f16.H]
ap, _tw, st = f16._cbs({'BX': 60.0, 'BY': 1000.0, 'B7': 50.0}, None, ('Y1(1)',))
seen = []


def st_rec(temp_, build_):
    y = next((b for b in build_ if b['暫編地號'] == 'Y1(1)'), None)
    if y is not None:
        seen.append((round(float(y.get('面積_m2', 0) or 0), 4), '段三部分併出' in y, round(pre_tab(y), 4)))
    return st(temp_, build_)


thr = {('BX', '左'): 130.0, ('BY', '左'): 200.0}


def tw(temp_, build_, blk, end, cand):
    b_ = {b['暫編地號']: b for b in build_}
    g = f16._g(b_[cand]) if cand in b_ else 0.0
    return (cand if g >= thr[(blk, end)] else None), round(g, 2), thr[(blk, end)]


order = [{'最終序位': 1, '街廓': 'BX', '端': '左', '暫編地號': 'X1(1)'},
         {'最終序位': 2, '街廓': 'BY', '端': '左', '暫編地號': 'Y1(1)'}]
ct = [{'形': '一', '列': [('BX', '左', 'X1(1)', 10.0), ('BY', '左', 'Y1(1)', 10.0)]}]
t2, b2, log = ns['k6b_stage3_run'](order, set(), own, temp, build, blocks, cl, ap, tw, st_rec,
                                   log_print=lambda *x: None, contests=ct)
y_in = next(t for t in temp if t['暫編地號'] == 'Y1(1)')
y_out = next(t for t in t2 if t['暫編地號'] == 'Y1(1)')
print('(1) Y1(1) 之分攤登記面積', y_in['分攤登記面積_m2'])
print('(1) 本趟之試算所見之 Y1(1)（面積_m2, 帶段三部分併出, R-16′ 式之值）之相異者：', sorted(set(seen)))
print('(1) 本趟畢之 Y1(1)：面積_m2', round(float(y_out['面積_m2']), 4), '段三部分併出', y_out.get('段三部分併出'),
      'R-16′ 式之值', round(pre_tab(y_out), 4))

# ── (2) 入池閘之代表宗：帳已寫 vs 帳未寫（趟中） ──
r_led = f28._q(ns, f27, {'分攤登記面積_m2': 130.0, '面積_m2': -30.0, '段三併出': ['Q(1)'], '段三部分併出': {'Q(1)': 40.0}})
r_mid = f28._q(ns, f27, {'分攤登記面積_m2': 130.0, '面積_m2': -30.0})
print('(2) 入池閘之代表宗：帳已寫 ⇒', r_led, '｜帳未寫（趟中之試算之輸入）⇒', r_mid, '（Y1 之剩下 90 ＜ Y2 之 100 ⇒ 性質之期 Y2）')
```

### 附錄四　原碼（`54e142c`）→ 工項二（`6e7272a`）之差異（`git diff 54e142c 6e7272a -- app.py verify/selection_pipeline.py`·全文）

（`verify/selection_pipeline.py` ＝ 原碼 ⇒ 唯 `app.py`）

````diff
diff --git a/app.py b/app.py
index 6ea0b01..5ea2beb 100644
--- a/app.py
+++ b/app.py
@@ -9534,6 +9534,7 @@ def k929_6_fixpoint(build_parcels, trial, own_map, pre_price_by_zone, front_line
       逾 `max_rounds`（預設 ＝ 宗數 ＋ `1`）未收斂。
     🆕 `W-G.9-373`（`K-9-67` ① 之 1·KL 裁 `2026-10-08`）：② 之標的宗改為——諸宗之 `G` 以 `0.01 ㎡`（`adj_q2`）比，取其
       最大者；並列 ⇒ 重劃前面積（成員之分攤登記面積之和·輸入之 build）大者；再並列 ⇒ 暫編地號小者（`k967_rank`）。
+      🔧 補令一（R-16′）：各宗之重劃前面積 ＝ 分攤登記面積 − `段三部分併出` 之和（部分併出之剩下所含者唯其剩下）。
     """
     import copy as _cp_k9296
     from shapely.geometry import Polygon as _Pg_k9296
@@ -9564,7 +9565,9 @@ def k929_6_fixpoint(build_parcels, trial, own_map, pre_price_by_zone, front_line
     geom = {_pid(t): _Pg_k9296(t['polygon_coords']).buffer(0) for t in build}
     members = {_pid(t): [_pid(t)] for t in build}
     # 🆕 `W-G.9-373`（`K-9-67` ① 之 1）：重劃前面積之表 ＝ 輸入之 build 之各宗之分攤登記面積（取之一次）
-    _pre_k967 = {_pid(t): float(t.get('分攤登記面積_m2', 0) or 0) for t in build}
+    # 🔧 `W-G.9-373` 補令一（R-16′）：減其 段三部分併出之和（部分併出之剩下所含者唯其剩下）
+    _pre_k967 = {_pid(t): float(t.get('分攤登記面積_m2', 0) or 0)
+                 - sum(float(_v) for _v in (t.get('段三部分併出') or {}).values()) for t in build}
     tried = set()
     log = []
     cap = int(max_rounds) if max_rounds else (len(build) + 1)
@@ -10864,8 +10867,8 @@ def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lot
          `K-9-50` 處之；分屬三個以上之末端塊、一端屬二以上之競合、同一候選同時跨占二末端塊之 `R_end`
          ⇒ 🔴 停機（逐案呈核·⛔ 推）。
       ③ 各標的之未達候選依原投影序為列，交 `k6b_stage3_run`（① 同街廓相鄰 → ② 道路及公設地上相鄰·整筆；
-         ② 驗「不影響原位次」；後處理同段三）；併入之除外 ＝ `locked` ∪ `corner_lots` ∪ 段三已併出者
-         （`K-9-49 ③`：已上鎖、已併入或已分配予街角之土地⛔ 再併入末端塊）。
+         ② 驗「不影響原位次」；後處理同段三）；併入之除外 ＝ `locked` ∪ `corner_lots` ∪ 已全數併出者
+         （部分併出之剩下⛔ 除外·KL 裁 `2026-10-08`）（`K-9-49 ③`：已上鎖、已併入或已分配予街角之土地⛔ 再併入末端塊）。
       ④ 未成之標的 ⇒ 記「皆未達」（定案之配地據以強制抵費地·`K-9-36 ③`）。
     回 `(temp_out, build_out, log, rec)`；`rec` ＝ `{'退縮': setback, '標的': [[街廓, 端]…],
     '皆未達': {街廓: [端…]}}`（試算中止 ⇒ `'標的'` ＝ `None`、另載 `'試算中止'`；有競合 ⇒ 另載 `'競合'`）。"""
@@ -10930,6 +10933,12 @@ def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lot
         _rec['競合'] = [{'形': c['形'], '列': [list(e) for e in c['列']]} for c in _ct]
     _L = (set(locked or ()) | set(corner_lots or ())
           | {t['暫編地號'] for t in temp_parcels if t.get('段三併出')})
+    # 🔧 `W-G.9-373` 補令一（R-13′·KL 裁 `2026-10-08 20:18` 甲案）：段三之除外唯取已全數併出者——部分併出之剩下（建地片仍在
+    #   build；非建地之片帶 段三餘量 而其四位小數 ＞ 0）自 _L 去之，唯其⛔ 在 locked、⛔ 在 corner_lots 者（照舊除外）
+    _bin_ebm = {b['暫編地號'] for b in (build_parcels or [])}
+    _L = _L - {t['暫編地號'] for t in temp_parcels
+               if t.get('段三併出') and (t['暫編地號'] in _bin_ebm or round(float(t.get('段三餘量') or 0), 4) > 0)
+               and t['暫編地號'] not in set(locked or ()) and t['暫編地號'] not in set(corner_lots or ())}
 
     def _trial(temp, build, blk, end, cand):
         _e = ((alloc_eval(temp, build) or {}).get(blk) or {}).get(_SIDE[end]) or {}
@@ -11488,6 +11497,8 @@ def adj_intake(temp_parcels, build_final, g_rows, dropped, own_map, burden_by_bl
     🔒 殘料（`_is_ghost_sliver`）⛔ 入任何合併單位（無地號·無地主）；其於 build／G 值列者略之。
     🆕 `W-G.9-373`（`K-9-66` 通知 `3`）：建地之部分併出（可建築土地上之切片帶 `段三部分併出` 且 `段三併出` 非空·仍在 build）
       ⇒ 其剩下仍為原街廓之該宗：原有面積 ＝ 分攤登記面積 × ρ（ρ ＝ 剩下 ÷（剩下 ＋ 已併出））、已併出之量計入原位次配地；
+      🔧 補令一（R-9′·KL 裁 `2026-10-08 20:18` 甲案）：已併出 ＝ `段三部分併出` 之和（其帳逐趟累計）、剩下 ＝ 分攤登記面積 −
+      已併出（以帳定之·⛔ 讀 `面積_m2`——其兼載其後受併入之量）；
       其單元配地 ⇒ 原位次配地（配地街廓含受併宗之街廓）；不配地 ⇒ 建築街廓內不能分配（應分配面積 ＝ 該趟之 `G`）。
       停機：受併宗未配地；剩下或已併出 ≤ 0；不在 build；不配地紀錄之街廓非本街廓。
     """
@@ -11578,8 +11589,10 @@ def adj_intake(temp_parcels, build_final, g_rows, dropped, own_map, burden_by_bl
             _rcv_b = [str(_x) for _x in (t.get('段三併出') or [])]
             if any(_x not in _alloc for _x in _rcv_b):
                 raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 段三所併出之 {_k!r} 之受併宗 {_rcv_b} 未配地 ⇒ 停機")
-            _now_b = _a(t) + float(t.get('面積_m2', 0) or 0)
+            # 🔧 `W-G.9-373` 補令一（R-9′）：剩下以帳定之 ＝ 分攤登記面積 − 段三部分併出之和（所併出之來源量·其帳逐趟累計）；
+            #   ⛔ 讀 面積_m2（其兼載其後受併入之量·KL 甲案之下部分併出之剩下得為受併宗）
             _mg_b = sum(float(_v) for _v in (t.get('段三部分併出') or {}).values())
+            _now_b = _a(t) - _mg_b
             if not _now_b > 0 or not _mg_b > 0:
                 raise RuntimeError(f"🔴 [W-G.9-373 調配之輸入] 建地之部分併出之 {_k!r}：剩下 {_now_b!r}／已併出 {_mg_b!r} "
                                    "不皆 > 0 ⇒ 停機")
@@ -13654,6 +13667,11 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
       〔部分併出者留 build、`面積_m2` 減其量、帶 `段三部分併出`·⛔ `段三餘量`〕）；剩下依第 `5` 項逐輪（候選之序以一次之
       試算定之：距離 → `k967_rank`；同一輪轉到同一街廓者一起·先到者⛔ 重分），諸輪畢仍有剩下者轉調配。同一街廓有二位以上
       地主之土地而一次全部試併不過者，於其諸列之首記層級 `K-9-66` 之列。`alloc_state` 之回傳另含 `members`（`K-9-67`）。
+    🔧 補令一（R-14′／R-16′·KL 裁 `2026-10-08 20:18` 甲案）：部分併入他處後剩下之土地與一分未併者同樣處理——輸入之片帶
+      前帳（`段三併出`／`段三部分併出`）者：非建地之片而帶 `段三餘量` 者，其可併之量 ＝ `段三餘量`（片之來源量與 `a′` 皆乘
+      ρ0 ＝ `段三餘量` ÷ a；折算比⛔ 受其影響）；本趟所觸之片而前帳非空者，`段三併出` 取前帳之集之聯集，仍有剩下者
+      `段三部分併出` ＝ 前帳 ⊕ 本趟之帳（逐受併宗相加），已全數併出者去之；本趟未觸者⛔ 動。第 `5` 項之重劃前面積之表之
+      各片 ＝ 分攤登記面積 − `段三部分併出` 之和。已併入他處之部分⛔ 動、⛔ 重分。
     """
     import copy as _cp
     from shapely.geometry import Polygon as _Pg, LineString as _Ls
@@ -13678,6 +13696,22 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         if _b.get('暫編地號') not in _by0:
             raise RuntimeError(f"🔴 [K-6-B 段三] build 片 {_b.get('暫編地號')!r} 不在 temp_parcels")
         _bids0.append(_b['暫編地號'])
+    # 🔧 `W-G.9-373` 補令一（R-14′ ①·KL 裁 `2026-10-08 20:18` 甲案）：前帳之剩下之量——非建地之片而帶非空之 段三併出 與
+    #   段三餘量 者 ρ0 ＝ 段三餘量 ÷ (分攤登記面積 ＋ 面積_m2)；他片 ρ0 ＝ 1（建地片之 面積_m2 已減其所併出）。片之來源量
+    #   （_a357）與片之 a′（_aprime）皆乘 ρ0，折算比（_k357）⛔ 受其影響。前帳（輸入之 段三併出／段三部分併出）存 _pre373
+    #   （R-14′ ②·⛔ 讀 _by0——其物件於末之取鍵或被寫）
+    _rho0_373, _pre373 = {}, {}
+    for _pid, _t in _by0.items():
+        _rho0_373[_pid] = 1.0
+        _cat373 = str(_t.get('街廓分類', '') or '')
+        if (_cat373 == '道路' or F3_CATEGORY_BURDEN.get(_cat373, '') != '可建築土地') and _t.get('段三併出') \
+                and '段三餘量' in _t:
+            _den373 = float(_t.get('分攤登記面積_m2', 0) or 0) + float(_t.get('面積_m2', 0) or 0)
+            if not _den373 > 0:
+                raise RuntimeError(f"🔴 [K-6-B 段三] {_pid} 帶前帳而其面積 {_den373!r} ≤ 0——剩下之比無從定之（停機款 9）")
+            _rho0_373[_pid] = float(_t['段三餘量']) / _den373
+        if _t.get('段三併出') or _t.get('段三部分併出'):
+            _pre373[_pid] = (set(_t.get('段三併出') or ()), dict(_t.get('段三部分併出') or {}))
     state = _mk_state(_temp0, _bids0)
 
     # 幾何（僅供判定·⛔ 改宗地之幾何）：合併群與共邊判用原多邊形；切分與面積比用 buffer(0)
@@ -13776,7 +13810,8 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                 st["build"] = [b for b in st["build"] if b['暫編地號'] != _src]
 
     def _aprime(st, src, dst):
-        return float(a_prime(st["by"][src], st["by"][dst]))
+        # 🔧 `W-G.9-373` 補令一（R-14′ ①）：乘 src 之 ρ0（前帳之剩下）
+        return float(a_prime(st["by"][src], st["by"][dst])) * _rho0_373[src]
 
     def _noaff(before, after, blks, removed):
         _sb = alloc_state(before["temp"], before["build"])
@@ -14164,15 +14199,17 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         # 補令一 `R-15`：有剩下(r) ⇔ round(r, 4) ＞ 0（與寫出之四位小數同一式；判、寫、讀皆依之）
         return round(float(r), 4) > 0
 
-    def _a357(x):
+    def _a357(x, _raw=False):
+        # 🔧 `W-G.9-373` 補令一（R-14′ ①）：片之來源量乘 ρ0（前帳之剩下）；_raw ⇒ 未乘（唯折算比 _k357 用之）
         _v = float(_by0[x].get('分攤登記面積_m2', 0) or 0) + float(_by0[x].get('面積_m2', 0) or 0)
         if not _v > 0:
             raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {x} 之面積 {_v!r} ≤ 0——來源面積之折算無從定之（停機款 9）")
-        return _v
+        return _v if _raw else _v * _rho0_373[x]
 
     def _k357(x, recv):
         # 🔧 `W-G.9-373`（R-5）：a′ 之分子取 x 之輸入之態（_by0·建地之部分併出後其當下之面積已減）
-        _k = float(a_prime(_by0[x], state["by"][recv])) / _a357(x)
+        # 🔧 `W-G.9-373` 補令一（R-14′ ①）：折算比 ＝ a′ ÷ a（二者皆未乘 ρ0）
+        _k = float(a_prime(_by0[x], state["by"][recv])) / _a357(x, _raw=True)
         if not _k > 0:
             raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {x} → {recv} 之 a′ 折算 {_k!r} ≤ 0（停機款 9）")
         return _k
@@ -14209,7 +14246,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         return float(_Dec357(repr(_d)).quantize(_Dec357('0.01'), rounding=_HU357))
 
     # ── 🆕 `W-G.9-373`（`K-9-66`／`K-9-68`）：試施（R-5 (a)）、輪（R-5 (b)）、第 5 項之輪（R-7 ④）──
-    #   代 `K-9-48` 七項 3／4／7 之逐片（最大面積·整筆）與 `K-9-51` 之逐片（`_max357`／`_k951`／`_split357` 去之）。
+    #   代 `K-9-48` 七項 3／4／7 之逐片（最大面積·整筆）與 `K-9-51` 之逐片（其舊之巢狀皆已去之）。
     _cls373 = {'bld': '建地', 'road': '道路', 'pub': '公設地'}
 
     def _try373(st, pairs):
@@ -14289,7 +14326,9 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] 現態配地中止：{_cur['err']!r}（停機款 9）")
         _own = own_map or {}
         _cm = _cur.get("members") if isinstance(_cur.get("members"), dict) else {}
-        _pa = {p: float(t.get('分攤登記面積_m2', 0) or 0) for p, t in _by0.items()}
+        # 🔧 `W-G.9-373` 補令一（R-16′）：重劃前面積 ＝ 分攤登記面積 − 段三部分併出之和（部分併出之剩下所含者唯其剩下）
+        _pa = {p: float(t.get('分攤登記面積_m2', 0) or 0) - sum(float(_v) for _v in (t.get('段三部分併出') or {}).values())
+               for p, t in _by0.items()}
         _seq = {}
         for x in xs:
             _gx = str(_own.get(str(_by0[x].get('原地號', '') or ''), '') or '')
@@ -14612,6 +14651,21 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         else:
             _tp.pop('段三部分併出', None)
             _tp.pop('段三餘量', None)
+    # 🔧 `W-G.9-373` 補令一（R-14′ ②·KL 裁 `2026-10-08 20:18` 甲案）：帳之合——本趟所觸之片（在 marks、_left 或 merged_out）
+    #   而其前帳非空者：段三併出 ＝ 前帳之集 ∪ 現之集；仍有剩下（帶 段三餘量，或建地片而仍在 build）⇒ 段三部分併出 ＝ 前帳 ⊕
+    #   現之帳（逐受併宗相加·四位·＞ 0）；否則（已全數併出）⇒ 去 段三部分併出。本趟未觸者⛔ 動（其帳⛔ 再加）
+    _bnow373 = {b['暫編地號'] for b in state["build"]}
+    for _pid in sorted(set(_pre373) & (set(_left) | set(marks) | merged_out)):
+        _tp = state["by"][_pid]
+        _ps373, _pp373 = _pre373[_pid]
+        _tp.update({'段三併出': sorted(_ps373 | set(_tp.get('段三併出') or ()))})
+        if '段三餘量' in _tp or (_kind(_pid) == 'bld' and _pid in _bnow373):
+            _acc373 = dict(_pp373)
+            for _r, _v in (_tp.get('段三部分併出') or {}).items():
+                _acc373[_r] = _acc373.get(_r, 0.0) + float(_v)
+            _tp.update({'段三部分併出': {_r: round(_v, 4) for _r, _v in sorted(_acc373.items()) if round(_v, 4) > 0}})
+        elif '段三部分併出' in _tp:
+            del _tp['段三部分併出']
     return state["temp"], state["build"], log
 
 
@@ -14705,8 +14759,8 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
       配地中止；`members` 非 dict；該片已自為已配得之宗或為其成員（`K-9-53` ① 之前提「分不到」與 `K-9-51` 之前提
       「剩餘土地」皆不成立）；同一地主於本街廓之已配得之宗之成員與之相連（入池閘之射程·`R-6` (a) 之同街廓之例·
       `K-9-55` 之前提「不相鄰」不成立）（補令二 裁二·補令三 裁一〜三·補令四 裁一）。
-      🆕 `W-G.9-367`（`GB-201` 之防護）：逐片之整筆之主併入、與可拆分之片之最大面積之試（來源量 ＞ 0·含 `K-9-51` 之可拆分者）
-      之前，計畫之受併宗於當下之試算未保留（或當下之配地中止）⇒ 停機。
+      🆕 `W-G.9-367`（`GB-201` 之防護）：每一受併之街廓之 `k966_block_merge` 之前（`W-G.9-373`·第 `1` 輪與 `K-9-51` 之諸輪
+      之每一要求），計畫之受併宗於當下之試算未保留（或當下之配地中止）⇒ 停機。
       （本街廓之候選之檢核不過 ⇒ 記未成、續試他宗·⛔ 停機——補令二 裁一·`K-9-55` 之二·代補令一之停機。）
       ⛔ 以靜默略過代之。
     🆕 `W-G.9-373`（`K-9-66`／`K-9-67`／`K-9-68`·KL 裁 `2026-10-07`／`2026-10-08`）：整批不過 ⇒ 第 `1` 輪 ＝ 各片之計畫之
@@ -14715,6 +14769,9 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
       （候選之序以一次之試算定之：距離 → 本街廓者先 → `k967_rank`；同一輪轉到同一街廓者一起·先到者⛔ 重分），
       諸輪畢仍有剩下者入合併單位。受併宗之擇與道路片之落點之末鍵改依 `K-9-67`（應分配面積大 → 重劃前面積大 → 暫編地號小
       ·⛔ 停機）。同一街廓有二位以上地主之土地而一次全部試併不過者，於其街廓之諸列之首記 `K-9-66` 之列。
+    🔧 補令一（R-15′／R-16′·KL 裁 `2026-10-08 20:18` 甲案）：候選——仍在 build 之建地片縱帶段三之鍵（部分併入他處後剩下之
+      土地）亦受理（其量 ＝ 該片之 a·已減其所併出），與一分未併者同；他片帶 `段三併出` 或 `段三餘量` 者略（照舊）。輸出之
+      `段三併出` ＝ 該片之既有之集 ∪ 本趟之受併宗。重劃前面積之表之各片 ＝ 分攤登記面積 − `段三部分併出` 之和。
     """
     import copy as _cp953
     from shapely.geometry import Polygon as _Pg953, LineString as _Ln953
@@ -14766,9 +14823,11 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
         _pk953 = str(_tq['暫編地號'])
         if _tq.get('_is_ghost_sliver') or _raw953.get(_pk953) is None:
             continue
-        if ('段三併出' in _tq) or ('段三餘量' in _tq):
-            continue
         _so953 = _sort953(_tq)
+        # 🔧 `W-G.9-373` 補令一（R-15′ ①·KL 裁 `2026-10-08 20:18` 甲案）：建地片而在 build 者受理（縱帶段三之鍵·其量 ＝ 該片之
+        #   a·已減其所併出）；他片帶 段三併出 或 段三餘量 者略（照舊）
+        if (('段三併出' in _tq) or ('段三餘量' in _tq)) and not (_so953 == 'bld' and _pk953 in _bin953):
+            continue
         if _so953 in ('road', 'pub') or (_so953 == 'bld' and _pk953 in _bin953):
             _cands953.append(_pk953)
     _bown953 = {_gown953(_bq953) for _bq953 in (build_parcels or [])} - {''}
@@ -14813,7 +14872,9 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
         return [str(_m) for _m in (C0['members'].get(_h) or [_h]) if str(_m) in _tin953]
 
     # 🆕 `W-G.9-373`（`K-9-67`）：重劃前面積之表 ＝ 輸入之 temp 之各片之分攤登記面積（未經地價折算）
-    _pre953 = {_pk953: float(_tq.get('分攤登記面積_m2', 0) or 0) for _pk953, _tq in _tin953.items()}
+    # 🔧 `W-G.9-373` 補令一（R-16′）：減其 段三部分併出之和（部分併出之剩下所含者唯其剩下）
+    _pre953 = {_pk953: float(_tq.get('分攤登記面積_m2', 0) or 0)
+               - sum(float(_v) for _v in (_tq.get('段三部分併出') or {}).values()) for _pk953, _tq in _tin953.items()}
 
     _lots_of953 = {}                    # 歸戶 → 其已配得之宗（字典序）
     for _h953 in sorted(_home953):
@@ -15323,7 +15384,8 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
     for _x in sorted(set(_marks953) | set(_rest953)):
         _d = state["by"][_x]
         if _x in _marks953:
-            _d['段三併出'] = sorted(_marks953[_x])
+            # 🔧 `W-G.9-373` 補令一（R-15′ ②）：該片之既有之集 ∪ 本趟之受併宗
+            _d.update({'段三併出': sorted(set(_d.get('段三併出') or ()) | _marks953[_x])})
         if _x in _bnow953 and _sort953(_tin953[_x]) == 'bld':
             # 🆕 `W-G.9-373`（`K-9-66`·R-5 (d)）：建地之部分併出（仍留 build）⇒ 段三部分併出（既有者合之）·⛔ 段三餘量
             _pp953 = dict((str(_k), float(_v)) for _k, _v in (_d.get('段三部分併出') or {}).items())
@@ -15349,8 +15411,8 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
 # ══════════ 🆕 `W-G.9-367`：規格步 4 乙——第一趟（`K-9-53` ②·KL 裁 `2026-09-30`；`K-9-56`·KL 裁 `2026-10-04`）══════════
 #   正典：`grep -n "K-9-56" docs/rulings/K-6_街角地分配程序與可分配判準.md`；工程讀法 ＝ 同典「`K-9-56`」節之註。
 #   手冊先行之後（街角已定案），凡合併單位之地主另有已配得之宗者，沿其候選街廓名單，至第一個有其已配得之宗之街廓，
-#   將合併單位之土地（`a′` 折算）整體併入其已配得之宗之一；整體不過 ⇒ 於同一宗逐片（建地整筆、道路與公設地上之土地
-#   取最大面積），剩下者續沿名單；都不行者留於合併單位（規格步 5·另單）。
+#   將合併單位之土地（`a′` 折算）整體併入其已配得之宗之一；整體不過 ⇒ 依 `K-9-66`（`k966_block_merge`·`W-G.9-373`：
+#   建地 → 道路 → 公設地逐類全併，不過之類按比例），剩下者續沿名單（`K-9-68` 之輪）；都不行者留於合併單位（規格步 5·另單）。
 #   🔒 單一真相源 ＝ `adj4_pass1_run`（純函式·⛔ 讀 `st`／session）；受詞與名單 ＝ `adj4_plan`（純函式）；
 #      harness ＝ `run_adj4`（selection 之 harness 檔）；畫面 ＝ `f3_screen_adj4`。併入之結果沿用段三之三鍵標於宗地。
 #   🔒 旗標 `WV_ADJ4`：未設／`on` ⇒ 啟用；`off` ⇒ 逐位回到本批前之行為（唯 session 多一鍵 `f3_adj4_log` ＝ `[]`）；
@@ -15497,6 +15559,7 @@ def adj4_pass1_run(temp_parcels, build_parcels, own_map, subjects, slice_geom, a
       要求，依受併之街廓分組，逐街廓以 `k966_block_merge` 處置（一次全部〔整體〕→ 建地 → 道路 → 公設地逐類全併，不過之類
       按比例·建地可拆分〔部分併出者留 build、`面積_m2` 減其量、帶 `段三部分併出`〕；同一輪到達同一街廓者一起·先到者⛔ 重分）；
       受併宗之序之末鍵改依 `k967_rank`。同一街廓有二位以上地主之土地而整體不過者，於其諸列之首記 `K-9-66` 之列。
+      🔧 補令一（R-16′）：`k967_rank` 之重劃前面積之表之各片 ＝ 分攤登記面積 − `段三部分併出` 之和。
     """
     import copy as _cp_a4
     from shapely.geometry import Polygon as _Pg_a4
@@ -15661,7 +15724,9 @@ def adj4_pass1_run(temp_parcels, build_parcels, own_map, subjects, slice_geom, a
 
     _rank_a4 = {'建地': 0, '道路': 1, '公設地': 2}
     # 🆕 `W-G.9-373`（`K-9-67`）：重劃前面積之表 ＝ 輸入之 temp 之各片之分攤登記面積（未經地價折算）
-    _pre_a4 = {_p: float(_t.get('分攤登記面積_m2', 0) or 0) for _p, _t in _tin_a4.items()}
+    # 🔧 `W-G.9-373` 補令一（R-16′）：減其 段三部分併出之和（部分併出之剩下所含者唯其剩下）
+    _pre_a4 = {_p: float(_t.get('分攤登記面積_m2', 0) or 0)
+               - sum(float(_v) for _v in (_t.get('段三部分併出') or {}).values()) for _p, _t in _tin_a4.items()}
     # 🔧 `W-G.9-373`（`K-9-68`）：諸受詞先備（R-7·其序 ＝ 受詞之序），其後逐輪辦之（R-8）
     _SJ_a4 = []
     for _sj in subjects:
@@ -15729,7 +15794,7 @@ def adj4_pass1_run(temp_parcels, build_parcels, own_map, subjects, slice_geom, a
                     raise RuntimeError(f"{_hd_a4} 街廓 {_bk} 之候選之宗 {_noG} 無 G——受併宗之序無從定之 ⇒ 停機")
 
                 # 🔧 `W-G.9-373`（`K-9-67`）：同距離者之序改為 `k967_rank`（G 大 → 重劃前面積〔成員之輸入之分攤登記面積〕
-                #   大 → 暫編地號小）
+                #   大 → 暫編地號小）；補令一（R-16′）：各片之重劃前面積 ＝ 分攤登記面積 − 段三部分併出之和
                 def _rkey_a4(_h):
                     _ms = _mof_a4(_h)
                     _same = any(_m in _tin_a4 and str(_tin_a4[_m].get('原地號', '') or '') in _lots_set for _m in _ms)
````
