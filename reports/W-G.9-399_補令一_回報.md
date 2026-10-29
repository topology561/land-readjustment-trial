# `W-G.9-399_補令一` 執行端回報：**停機上呈**（停機款 `12″`）

> 執行端（CC·雲端）·`2026-10-29`·effort=high。單 ＝ `ops/queue` 之 `orders/W-G.9-399_補令一.md`（`89175` B·`b086c2042f9e…` ＝ `STATE.json`·`SELF_SHA256` `d39adf8c…` 依 `P-5` 自驗合）。
> **結論**：工項零″、一″ 已推新側支；工項二″ 已撰、`commit`（`7f7ad7c`·**⛔ 推**），其驗 `V-1″`〜`V-9″` 皆合期（`97` 呼叫皆合「施後」之列·**本案配地⛔ 變**）；唯讀獨立審查之總判 PASS（隨機測 `2000`＋`1000` 例新碼不合 `0`），**唯其 WARNING-1 為規格之漏載**（下之 ⑥：宗 ∩ `R_end` 為「多邊形 ＋ 線段」之集合時，該線段是否計入臨端線——`R-1″` 之字面計之、原單塊 `K48` 之三之乙「交集**多邊形**之外框」不計；二讀之土地後果（互相等待之先後之量）相異，且字面之讀之值隨座標系而變；**執行端已自重現**）；其形⛔ 在 `§三-4″` 之已知之形 ①〜⑥ 之內 ⇒ **停機款 `12″`**（⛔ 自裁）。依 `§零-2″` 末：已推之 `commit` ⛔ 撤；工項二″ ⛔ 推（其差異之全文 ＝ 同目錄之 `W-G.9-399_補令一_回報_app.diff`）；工項三″、四″ ⛔ 為。主線 `bd7da4d` ⛔ 動。

## ① `commit` 與推送

| 工項 | `commit` | 推送 |
|---|---|---|
| 零″ | `31887d94b981e162842b2547de3b9b2e050059ab`（`docs/orders/W-G.9-399_補令一.md` 新·`552`／`0`·blob 之 `sha256` ＝ `b086c204…`） | `git push origin HEAD:verify/W-G.9-399-k960x`：`23f3fc8..31887d9`（快轉）；推後 heads（濾後）`57`、主線 `bd7da4d…` |
| 一″ | `1612750ff6291af48a98f46a44667e414af06968`（`verify/probes/probe_WG9399_k960x.py` `85`／`6`·blob `a9a3466725cecc5017151061c131c613617e1312`·`48222` B） | `31887d9..1612750`（快轉） |
| 二″ | `7f7ad7ccb3e285a9c2d027664defd10be1797504`（`app.py` 唯一·對 `1612750` `359`／`14`·施後 blob **`1158f83e060600a71bd9ff28c66d7ebdb9d6aa16`**·`1927970` B；對 `<O>/app_R0.py`〔`95047cb9…`〕`78`／`7`） | **⛔ 推**（停機款 `12″`）。全文差異 ＝ 同目錄之 `W-G.9-399_補令一_回報_app.diff`（`40810` B·`sha256` `16c561ff47fb7962ca8060c18f5d74631adecf6acd4ff165553e26fb80203a9c`·`509` 列 ＝ `git diff 1612750 7f7ad7c -- app.py`；施於 `1612750`（＝ `23f3fc8`）之 `app.py` 即得 blob `1158f83e…`·執行端實施驗之） |
| 三″、四″ | ⛔ 為 | — |

遠端（本回報時）：`verify/W-G.9-399-k960x` ＝ `1612750`；主線 `wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`（⛔ 動）；heads（`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`）`57`；除 `ops/queue` 與新側支外之 `55` 列逐列 ＝ `<O>/heads_before_399p1.txt`。

## ② 停機款之三值（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1″` | 主線 `bd7da4d`、新側支 `23f3fc8`、heads `57`；追蹤檔無變動；`§零-0″` 項 `3` `rc 0` 與四簿；旗標 `[None×5]`；環境可匯入 | 皆合：`bd7da4d…`、`23f3fc84…`、`57`（`<O>/heads_before_399p1.txt`）；`status` 空；`app.py` `ca9f917e…`、`F42` `2325d3fc…`；`rc 0`·自誤 `629`／`644`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；`[None, None, None, None, None]`；裝後匯入 `rc 0` |
| `2″` | `SELF_SHA256`、bytes／`sha256`、入倉之 blob | 皆合（`d39adf8c…`；`89175`／`b086c204…`；`git cat-file blob HEAD:docs/orders/W-G.9-399_補令一.md` 之 `sha256` ＝ `b086c204…`） |
| `3″` | 四塊與原單二塊與 `rep399.diff` 之 bytes／`sha256`／列數；`apply --check`；施後 blob | 皆合：`Fy58` `13709`／`1f6b8bb5…`／`180`；`K49` `9098`／`1e9a151f…`／`45`；`P60` `2930`／`d5bdb8fe…`／`15`；`E46` `3386`／`591ec9a0…`／`13`；`K48` `15358`／`1a1f8a17…`／`72`；`P59` `2902`／`c533677d…`／`16`；`rep399.diff` `34949`／`7f3b769f…`／`434`（原趟之回報 `46671`／`a2167cae…`）；`Fy58`、`rep399.diff` 之 `--check` 皆過；`F42` ＝ `a9a34667…`、`R-0″` 施後 ＝ `95047cb9…`（`1922322` B） |
| `4″` | 前置″ 之期 | 皆合（下之 ③） |
| `5″` | 規格無歧義而涉域；⛔ 須改禁改 | 撰碼中未遇 |
| `6″` | `V-1″`〜`V-9″` 皆合；本案配地⛔ 變 | 皆合（下之 ③）；本案配地⛔ 變 |
| `7″` | 推之目標唯新側支／`ops/queue`；⛔ 被拒；主線⛔ 推進 | 合（二推皆至新側支·快轉；`ops/queue` 之推皆快轉） |
| `8″` | 工項三″ 之三檔 | **未及**（⛔ 為）；其預算（倉外·`<O>/pv/`）：`K-6` 典 `1025082` → `1049538`·blob `008685ca…`、`待落地清單.md` `49281` → `55113`·blob `ad10dbf5…`、自誤簿 `1249001` → `1252387`·blob `209a7e46…`（皆 ＝ `§五″` 項 `5`·嚴格前綴·尾 ＝ 塊）；塊 `CK` `1539`／`00cd3949…`／`31`、`GF` `2445`／`b11edb77…`／`47`（＝ 項 `7`） |
| `9″` | 收工閘 | **未及** |
| `10″` | ⛔ 自判正典、⛔ 改塊／器／命令 | 合 |
| `11″` | 新檔⛔ 為 `check-ignore` 所命中 | 合（本補令 `rc 1`） |
| **`12″`** | **唯讀獨立審查之發現⛔ 涉域上判斷或規格之漏載（`§三-4″` 之已知之形除外）** | **成就**：WARNING-1（⑥）。執行端已自重現（⑥ 之末） |
| `13″` | 存取⛔ 被拒；寫入⛔ 為分類器所拒 | 合 |

## ③ 前置″ 與驗之出艙（`<O>` ＝ `/tmp/claude-0/-home-user-land-readjustment-trial/f483ad25-63bf-5f66-8e5e-3a22e6bb5950/scratchpad/o399p1`·倉外·容器暫存）

- **`§零-0″`**：`nproc` ＝ `4`；context 餘量充足（約 `14.9` M tokens）。環境：初無 `shapely`（匯入 `rc 1`）⇒ 依 `requirements.txt` 裝（`rc 0`）⇒ `pip freeze` `9ad34edc…`（異於基準）⇒ 依原單 `§零-0` 項 `5` 之命令逐字釘回（`rc 0`）＋ `pip uninstall -y tzdata --break-system-packages`（`rc 0`）⇒ **`ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`**（＝ 基準）；`Python 3.11.17`；匯入 `rc 0`。pre-flight（`23f3fc8` 之器·`rc 0`）：🔴 `0`；🟡 `4`（`P-4` `:102`、`:115`、`:139`、`:196`·皆 `§五″` 項 `9` 所具名豁免者）；ℹ️ `P-5` ✅（受詞 `89097` B）、`P-3` ＝ `24044`–`31788`（器所量者為施工樹之 `app.py`〔＝ `bd7da4d`〕·單所記之 `24384`–`32128` 為原型之值·照實記之）。`§零-0″` 項 `8`：`rep399.diff` ＝ 項 `3`。
- **前置″ (甲)(乙)**（工項一″ 之端 `1612750`·施工樹 `/tmp/w`·`12:47:26`→`13:57:42`·耗時之和 `6163` s）：`51` 呼叫之 `rc`／`stderr`／末列 ＝ 期（「項 `8` 之表」之工項一″ 之端之列·`#95` 依本補令之表），**不符 `0`**（`#95`／`#96`／`#97` ＝ `rc 1`·末列逐字同表）；`stderr` 合計 `0` B；`f8_pre_35.json` ＝ `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、`f8_pre_00.json` ＝ `186b090b68836f0ece2c0d23dad5573941995bf5`。並行：起 `2`；撰碼中之自跑時降為 `1`（自跑亦 `1`·合計 ≤ `2`），自跑畢復 `2`。
- **前置″ (丙)**：主線之端 ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434` ＝ 基準之 sha；`Python 3.11.17` ＝；`pip freeze` `ae1438da…` ＝ ⇒ **沿用** `基準/bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434.md` 之 `46` 呼叫之值（⛔ 重跑）。
- **前置″ 項 `4`**：`git diff --name-status 23f3fc8 1612750` ＝ 恰 `2` 列（`A	"docs/orders/W-G.9-399_\350\243\234\344\273\244\344\270\200.md"`〔＝ `docs/orders/W-G.9-399_補令一.md`·工項零″ 之一筆〕、`M	verify/probes/probe_WG9399_k960x.py`）；「k960_idx_first」「END_BLOCK_IDX_W_AREA」「end_block_end_geom」皆無出艙、`rc 1`。
- **驗**（`7f7ad7c`·`push` 前·殼無 `WV_`·並行 `2`·從頭整套照跑 `97` 呼叫·`13:59:13`→`15:58:39`·耗時之和 `14331` s·⛔ 容器重啟·⛔ 重跑）：
  - `V-1″`／`V-2″`：`97` 呼叫之 `rc`／`stderr`／末列 ＝ 「施後」之列，**不符 `0`**；`F42 selftest` `P0 判式自驗 73／73`、`F42 wiring` `W1`〜`W6` ✅、`F42 run` `R1`〜`R3`（二退縮）✅；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`。
  - `V-3″`：`16` 器之 blob ＝ 原單 `§五-1` 項 `5`（`F42` ＝ `a9a34667…`）；`verify/probes/` 對 `1612750` 相異 `0`。
  - `V-4″`：`F36 diff` 3.5 m／0 m 皆 `rc 0`·`全比相異 0 項`；`cmp` 皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`（`stderr` 皆 `0` B）。
  - `V-5″`：`parity` 皆 `rc 0`·`⇒ rc 0（不符 0 項）`；落檔與 `stdout`（`#60`／`#61`）對前置″：以 `<HEAD>` 代 `HEAD` 之全值（前 `1612750ff629…`、後 `7f7ad7ccb3e2…`·各恰一見）後**逐位同**（`parity35` `8648` B、`parity00` `250` B、`#60` `1552` B、`#61` `1550` B）；對照：⛔ 代之則四者皆異（唯 `"head"` 列／首列之態）。
  - `V-6″`：`run` 皆 `⇒ 紅 []；rc 0`；`hash-object` 3.5 m 二列皆 `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、0 m 二列皆 `186b090b68836f0ece2c0d23dad5573941995bf5`。
  - `V-7″`：生產碼對 `1612750` 相異唯 `M app.py`（`359`／`14`·blob `1158f83e…`）；`verify/` 相異 `0`；`git diff --no-index <O>/app_R0.py app.py` 之 hunk 七（下表·皆在 `R-1″`〜`R-5″` 之處·各附 `R-6″` 之註）；`ast` 頂層節點：對 `app_R0.py` 增減 `0`、相異 ＝ `{end_block_apply, end_block_end_line, end_block_eval_rows, end_block_merge_run, end_block_pick}`；對 `bd7da4d` 增恰九（`END_BLOCK_IDX_W_AREA`、`END_BLOCK_IDX_W_LINE`、`END_BLOCK_LINE_TOL`、`end_block_end_geom`、`end_block_end_line`、`end_block_end_segs`、`k960_idx_first`、`k960_idx_key`、`k960_idx_rank`）、減 `0`、相異之既有節點恰六（`end_block_apply`、`end_block_eval_rows`、`end_block_host`、`end_block_merge_run`、`end_block_pick`、`k6b_stage3_run`）＝ 十五。
  - `V-8″`：「k960_idx_first」`6`、「END_BLOCK_IDX_W_AREA」`2`、「end_block_end_geom」`7`；`` `W-G.9-399` 補令一 ″ `` ⇒ `5`（判別力：`<O>/app_R0.py` ⇒ `0`）。
  - `V-9″`：諸器之 `stderr` 合計 `0` B。

| hunk（`app_R0.py` → `app.py`） | 所屬函式 | 條 |
|---|---|---|
| `@@ -11727,6 +11727,23 @@` | `end_block_end_line` | `R-2″`（沿 BASELINE 而行之邊之二端為觸點） |
| `@@ -11802,6 +11819,44 @@` | `end_block_pick` | `R-1″` ①（評選之迴圈前之分配） |
| `@@ -11819,10 +11874,9 @@` | `end_block_pick` | `R-1″` ②（列之臨端線 ＝ 所得之小段之和） |
| `@@ -11907,9 +11961,14 @@` | `end_block_apply` | `R-3″`（`RuntimeError` 之攔·`end_err`） |
| `@@ -11977,6 +12036,8 @@` | `end_block_apply` | `R-3″`（紀錄之 `端線之誤`） |
| `@@ -12108,7 +12169,9 @@` | `end_block_eval_rows` | `R-4″` |
| `@@ -12275,6 +12338,14 @@` | `end_block_merge_run` | `R-5″` |

`97` 呼叫之逐列之表見附錄甲。

## ④ 塊之實得

見 ② 之 `3″`。工項三″ 之三檔未寫入倉（⛔ 為）。

## ⑤ 推送之目標與 heads

見 ①。

## ⑥ 唯讀獨立審查之發現（停機之由）與執行端之自捕

**審查**（`redistribution-reviewer`·唯讀·受詞 ＝ 施工樹 `7f7ad7c`、`<O>/app_R0.py`、`<O>/post/v7_noindex.diff`、本補令 `§三″`／塊 `K49`、原單 `§三`／塊 `K48`）之總判：**PASS**，附 WARNING-1（其請發單端裁其是否構成停機款 `12″`）。逐條：
1. `V-7″` 之 hunk 七唯在 `R-1″`〜`R-6″` 之處（審查者自重產之 `--no-index` 與 `<O>` 之檔逐行同）；`ast` 相異恰五、對 `bd7da4d` 增九、相異十五；差異中無新 `def`／`lambda`（無巢狀之撞名）。
2. `R-1″` 合塊 `K49` 之二之甲：跨占之判同評選之迴圈；迭代全部 `entries`（⛔ 限於至當選為止）；右端以反序（原位次以該端為起）；切點 ＝ `R_end` 與諸 cut 之頂點之投影（`0 ＜ t ＜ 1`·並 `0`、`1`）；`R_end` 之外框逾半者方得歸、歸首一逾半之宗即 `break`（一小段至多一宗）；列值取 `2` 位、指數之分子用未取位。證之核：小段之內無頂點之投影 ⇒ 每一合格之邊於一小段非全蓋即不蓋 ⇒ Σ得 ≤ Σ`boundary(R_end)` ＝ `end_len`。
3. `R-2″` 合塊 `K49` 之二之乙（`sin 2°`、異側 ⇒ `0`、否則二端之垂距之較小者、≤ `0.05`；外框之頂點之序；二端入候選；`2.0` 以字面書而附註；⛔ 新頂層名）。
4. `R-3″`〜`R-5″` 之鍵之流合塊 `K49` 之二之丙（審查者自撰之 `keyflow.py`：右端 FRONT 端點外移 `0.08 m` ⇒ 右端 `端線(m)` `None`、`端線之誤` ＝ 直呼之訊息之首列、列之指數 `None`、⛔ 停機；左端無此鍵、`30.0`；顯示三形皆合；互相等待而誤在第二端 `BF` ⇒ 停機、訊息含「端線無從定」與「BF 左端之端線無從定：…」；無互相等待 ⇒ 照配·同 `M5`）。
5. **隨機測**（TWD97 之尺度·平移 `3e5±5e4`、`2.6e6±5e4`·旋轉 `0`〜`360°`·鏡射 `50%`）：
   - （甲）`rt_a.py`（seed `20261029`）`2000` 例（生成中剔除不健全之分割 `194` 例）·`4000` 端·`8282` 列；街廓 `W 25`〜`60`、`D 15`〜`40`，二端各取直／斜（±`6 m`）／二折；條片 ＝ `街廓 ∩ 端線.buffer(w)`（`w` 對數均勻 `3 mm`〜`20 cm`·`40%` 唯沿端線之一段）；`1607` 例含 ≤ `1 ㎡` 之宗；`20%` 條片與鄰宗之序互換；`30%` 之條帶再橫切為二；每例驗分割健全。直呼 `end_block_apply`（`trial` 恆未達、恆准強制）；未取位之量以 `ns` 內之 `round` 改恆等再跑取之。

     | 判式 | 新碼 不合／最大超出 | 原趟之碼 不合／最大超出 |
     |---|---|---|
     | Σ臨端線 ≤ `end_len ＋ n × 0.005` | `0`／`−4.5e−6` | `344`／`+90.99 m` |
     | Σ指數 ≤ `1 ＋ n × 5e−7` | `0`／`−5.0e−7` | `344`／`+0.976` |
     | 未取位 Σ ≤ `end_len ＋ 1e−6` | `0`／`−1.0e−6` | `344`／`+90.997` |
     | 未取位 Σ指數 ≤ `1 ＋ 1e−6` | `0` | `344`／`+0.976` |
     | 與取樣之參照（`2 mm`）之差 ＞ `2 cm` | `8` 例（WARNING-1）；參照亦計線段者 ⇒ `0` 例（最大 `2.85 mm`） | `357` |

   - （乙）`rt_b.py`（seed `7`）`1000` 例·`2000` 端：BASELINE 過屁股線上之隨機一點、偏 U(`−1.9°`, `1.9°`)；參照 ＝ 同形 `θ ＝ 0` 之 `end_len`。新碼：不合 `0`（最大超出 `−1.0e−6`）、端線含屁股線之段 `0` 端、不可定 `0` 端；原趟之碼：不合 `755`（最大 `+9.43 m`）、含屁股線之段 `823` 端。
   - `F42 selftest`（倉外之複本）：新碼 `73／73`；原趟之碼 `61／73`，紅 `['E11', 'E11′', 'E11′', 'E12', 'E13', 'P6', 'P7', 'P9', 'P10', 'P11', 'P12', 'M10']`（＝ `§一″` 項 `3`）。
6. **WARNING-1（停機之由·規格之漏載）**：宗之多邊形（GEOS 判 `valid`）之環沿端線有零寬之折返者，`R_end ∩ 該宗` 得為 `GeometryCollection(Polygon, LineString)`；`_boundary_len_on_line` 遞迴計入其 `LineString` ⇒ 該宗得「非其多邊形所臨」之端線之段。例 `485`：該宗之多邊形實臨 `6.20 m`，卻得 `11.24 m`（其段原屬一 ≤ `1 ㎡` 而⛔ 入列之條片）；例 `1683`：原位次先之鄰宗以其刺奪條片之 `13.9 m`；`8` 例皆 cut 含 `LineString`。Σ ≤ `end_len` 照成立。**二讀**：`R-1″` 之字面（`_boundary_len_on_line(該宗 ∩ R_end, p, q)`·碼完全照之）計其線段；原單塊 `K48` 之三之乙（「分子 ＝ 該宗 ∩ `R_end` 之**交集多邊形**之外框落於端線之長」）之嚴讀則⛔ 計。**土地之果**：唯於此形之地籍輸入，改互相等待之先後之量（評選指數）。審查者所示之最小之改之向（待裁·執行端⛔ 採）：cut 唯取其多邊形之部。此形⛔ 在 `§三-4″` ①〜⑥ 之字面之內（⑥ 之「手造之異常輸入」唯及 `TypeError`／`AttributeError`）；原趟之碼亦有之（非本補令所引入）。
   - **執行端之自重現**（`<O>/rv_chk485.py`·全文見附錄乙；以審查者之 `rt_a.py` 之生成重得例 `485`）：TWD97 旋轉之座標下，`end_block_apply` 之左端之列 `[('Q1(1)', 18.57, 11.24, 0.970754)]`、端線 `11.51`；該宗 `valid True`、`R_end ∩ 該宗` ＝ `GeometryCollection ['Polygon', 'LineString']`、全 cut 之臨端線 `11.2361`、唯多邊形之部 `6.2036`；條片（宗 `0`）跨占 `0.6264 ㎡`⛔ 入列。**另見**：同一宗地以**未變換之本地座標**量之，cut 為純 `Polygon`、臨端線 `6.2036`——即字面之讀之值**隨座標系（浮點）而變**（本補令 `F42` 之 `E11′`、`P7` 等以「旋轉鏡射 ⇒ 同」為期之同族之性質於此形不成立）。
   - **NOTE**（⛔ 擋·⛔ 修）：NOTE-2 `端線之誤` 以 `_g.get('end_err')` 之真假判之（首列為空字串則失其鍵·現之訊息皆以「🔴」起首·不可達）；NOTE-3 `R-3″` 之 `except RuntimeError` 亦攔 `end_block_end_geom` 之「缺幾何」「side 非法」二停機而記入 `端線之誤`（合 `R-3″` 之字面；前之 `end_block_side_geom` 已先攔·不可達）；NOTE-4 舊註（`end_block_pick` 內「臨端線之長 ＝ 該宗 ∩ R_end 之外框落於端線之長」）與 `end_block_end_line`、`end_block_apply` 之 docstring 未改，唯其後追加新註（合「`R-1″`〜`R-6″` 以外⛔ 動」·讀者易混）；NOTE-5 `V-8″` 之字樣 新碼 `5`、短字樣 `8`（原型 `3`／`11`·⛔ 擋）；已知之形之重現：原位次 vs 距端線最近（⑤ `158`）、「歸他端」之列保留原臨端線（⑤ `161`）。
   - 審查者之自首：曾誤於 `/home/user/land-readjustment-trial/`（本對話之初始目錄·非施工樹）生 `a_R0.out`、`a_R0.time` 二暫存檔，即刪；施工樹 `/tmp/w` 之 `git status --porcelain` 空、`HEAD` `7f7ad7c`、`find /tmp/w -newer` 去 `.git` 後 `0` 檔。其臨時檔皆在 `/tmp/rv399p1/`（容器暫存）。

**執行端之自捕與自解**：
1. **heredoc**：單首 🔑 令「Bash 命令⛔ 含 heredoc」；執行端於接單之初以 heredoc 改 `STATE.json` 一次（其出之格式異於原檔 ⇒ 即 `git checkout` 還原、⛔ `commit`；其後改以倉外之檔 `st.py`／`lg.py` 為之），撰碼中另有一次空之 heredoc（無作用·`grep` 之查）。皆⛔ 及量測之命令、⛔ 及倉內之檔。照實記之。
2. **`<O>/app_R0.py`**：初自撰碼之複本（`/tmp/wdev`·`1612750` ＋ `rep399.diff`）取之；`R-0″` 於施工樹施後（blob `95047cb9…`）即以施工樹之檔覆之（同 blob）。
3. **`R-1″` 之列之對應**：初以 `enumerate` 改評選之迴圈之首列，嗣為免動既有之句（突變之錨之險）改以 `id(entry)` 對應、迴圈之句照舊。
4. **並行**：撰碼中之自跑（`F42 selftest`、`#1`〜`#97` 中之 `42` 呼叫〔selftest／wiring〕與 `#19`、`#22`、`#47`、`#97`·於 `/tmp/wdev`·皆綠）期間，前置″ 之跑降為並行 `1`、自跑 `1`（合計 ≤ `2`）。驗之 `97` 呼叫期間⛔ 他負載；審查之期間唯審查者之程序（≤ `2`）。
5. **pre-flight 之 `P-3`**：見 ③。

## ⑦ 設計說明（`§三-5″`·工項二″ `7f7ad7c`）

- **原單 `§三-5` 之各項**：照原趟（`reports/W-G.9-399_規格單_回報.md` 之 ⑦·`R-1`〜`R-13`·碼 ＝ `rep399.diff`·⛔ 改）；其上唯 `R-1″`〜`R-6″`。
- **`R-0″` 之 blob 之對證**：`git apply --check` 過 ⇒ 施後 `95047cb9ae9cacb10f28ef7294fcf2f94c6dfe20`（`1922322` B）＝ 期；即複製為 `<O>/app_R0.py`。
- **`R-1″`**（`end_block_pick`·評選之迴圈之前）：`geom['end_segs']` 真者，逐 `entries`（全部·⛔ 限至當選）求跨占之宗（頂點 ≥ `3`·無效者 `buffer(0)`·`∩ R_end` 之面積 ＞ `END_BLOCK_CROSS_MIN_AREA`）之 `cut ＝ R_end ∩ 宗`（以 `id(entry)` 為鍵·依 `entries` 之序）；頂點之集 ＝ `shapely.get_coordinates(R_end)` ∪ 各 cut 之頂點；每一直段 `(a, b)` 以諸頂點之投影之參數（`0 ＜ t ＜ 1`·並 `0`、`1`·去重排序）切為小段 `(p, q)`；`_boundary_len_on_line(R_end, p, q) ＞ 小段之長之半` 者，歸首一「`_boundary_len_on_line(cut, p, q) ＞ 半`」之宗（`break`）；列之 `臨端線(m)` ＝ `round(所得之和, 2)`、`評選指數` 之分子用未取位之和（式、分母照原單 `R-6`）。**「和 ≤ `end_len`」之證**：每一小段至多歸一宗，且唯 `R_end` 之外框落於其上者得歸；小段之內無任何頂點之投影 ⇒ `R_end` 之合格之邊於一小段非全蓋即不蓋 ⇒ 得歸之小段之長之和 ≤ Σ`_boundary_len_on_line(R_end, 各直段)` ＝ `end_len`（逐邊之和 ≥ 其聯集之長）。
- **`R-2″`**（`end_block_end_line`·觸點之候選之後、「無觸點」之停之前）：逐 `block_poly.exterior.coords` 之相鄰二點（長 ＞ `0`）：`|cross(邊, û)| ÷ 邊長 ≤ sin(radians(2.0))`（`2.0` 以字面·註其所據 ＝ `_boundary_len_on_line` 之 `ang_tol_deg` 之預設）、且距（二端之有號垂距異號 ⇒ `0`；否則二端之垂距之較小者）≤ `END_BLOCK_LINE_TOL` ⇒ 二端入觸點之候選；⛔ 新頂層名、⛔ 新巢狀函式。
- **`R-3″`〜`R-5″` 之鍵之流**：`end_block_apply` 中 `end_block_end_geom` 之 `RuntimeError` ⇒ `{'end_segs': None, 'end_len': None, 'end_err': 首列}` 併入該端之幾何 ⇒ 首趟之紀錄 `'端線(m)'` `None` ＋ **`'端線之誤'`**（唯 `end_err` 真者）⇒ `end_block_eval_rows`：有 `端線之誤` ⇒「端線 — m（無從定：<端線之誤>）；」、有 `端線(m)` 而無誤 ⇒ 照原趟、無 `端線(m)` ⇒ ⛔ 列 ⇒ `end_block_merge_run`：每一競合之 `評選` 之求之前，其 `列` 之任一端之 `_ev[街廓][端]` 有 `端線之誤` ⇒ `評選` ＝ `None`、`評選之誤` ＝「`<街廓> <端>`端之端線無從定：`<端線之誤>`」（`continue`·⛔ 呼 `k960_idx_rank`）⇒ 互相等待時 `k960_idx_first`／三位以上之支以 `評選之誤` 停機；無互相等待 ⇒ ⛔ 用。
- **`R-6″`**：`R-1″`〜`R-5″` 之處各附註（所據 ＝ 塊 `K49` 之二之甲〜丙·W-1〜W-3）；`R-1″`、`R-2″`、`R-3″` 之註載逐字 `` `W-G.9-399` 補令一 ″ ``（計 `5` 見）。
- **本案之量**（`F42 run`·二退縮同·`<O>/post/run/97.out`）：`R2` 右 端線 `44.12`·`628-34(1)` `10.42`／`0.372619`；`R3` 左 `43.91`·`628-34(2)` `34.94`／`0.799606`；`R5` 右 `47.95`·`628-23(2)` `0.0`／`0.023134`；`R6` 左 `47.71`·`628-23(1)` `0.0`／`0.114893`、`628-4(1)` `0.0`／`0.056826`（＝ 原單塊 `K48` 之四）；當選 ＝ 主線；合併再試之標的 `[]`、競合 無。

## ⑧ `app.py` 之全文差異

同目錄之 `W-G.9-399_補令一_回報_app.diff`（見 ①）。

## ⑨ 工項三″ 之出艙

未及（⛔ 為·其預算見 ② `8″`）。

## ⑩ 各段耗時（Asia/Taipei）

接單 `12:42`；`§零-0″`〜工項一″ `12:42`〜`12:47`；前置″ `12:47:26`〜`13:57:42`（並行 `2`／撰碼自跑時 `1`）；撰碼與自跑 `12:50`〜`13:40`；工項二″ 之 `commit` `13:58`；驗 `13:59:13`〜`15:58:39`（並行 `2`）；審查 `16:00`〜`16:13`；自重現 `16:13`〜`16:16`；回報 `16:2x`。

## 附錄甲　`97` 呼叫之表（前置″·驗）

格 ＝ `rc`／`stderr` B／末列（耗時 s）。(甲)(乙) ＝ 本輪實跑於 `1612750`；(丙) ＝ 沿用基準。驗 ＝ 本輪實跑於 `7f7ad7c`。`<O>/<態>/` ＝ `<O>/pre/`／`<O>/post/`。

| # | 命令 | 工項一″ 之端（前置″） | 施後（驗） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（118） | `0`／`0`／`⇒ 紅 []；rc 0`（140） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（364） | `0`／`0`／`⇒ 紅 []；rc 0`（378） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（30） | `0`／`0`／`⇒ 紅 []；rc 0`（34） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（32） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（14） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（258） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（76） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（388） | `0`／`0`／`⇒ 紅 []；rc 0`（438） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（542） | `0`／`0`／`⇒ 紅 []；rc 0`（576） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | (甲)(乙) `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（10） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（70） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（370） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1624） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（24） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（24） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（262） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（306） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（36） | `0`／`0`／`⇒ 紅 []；rc 0`（46） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（28） | `0`／`0`／`⇒ 紅 []；rc 0`（34） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（22） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（12） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（178） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（58） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（768） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（162） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（112） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（314） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`selftest 9/9 ⇒ ✅`（2） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`selftest 13/13 ⇒ ✅`（2） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`紅項 [] 器紅 0`（10） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（340） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/<態>/k6s3_<態>_35.json` | (甲)(乙) `0`／`0`／（JSON 之摘要列·略）（172） | `0`／`0`／（JSON 之摘要列·略）（198） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/<態>/k6s3_<態>_00.json` | (甲)(乙) `0`／`0`／（JSON 之摘要列·略）（124） | `0`／`0`／（JSON 之摘要列·略）（136） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/<態>/f8_<態>_35.json` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（164） | `0`／`0`／`⇒ 紅 []；rc 0`（186） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/<態>/f8_<態>_00.json` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（120） | `0`／`0`／`⇒ 紅 []；rc 0`（136） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/<態>/parity35_<態>.json` | (甲)(乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（360） | `0`／`0`／`⇒ rc 0（不符 0 項）`（388） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/<態>/parity00_<態>.json` | (甲)(乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（256） | `0`／`0`／`⇒ rc 0（不符 0 項）`（282） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（282） | `0`／`0`／`⇒ 紅 []；rc 0`（312） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1132） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1066） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（116） | `0`／`0`／`⇒ 紅 []；rc 0`（152） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（364） | `0`／`0`／`⇒ 紅 []；rc 0`（436） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（280） | `0`／`0`／`⇒ 紅 []；rc 0`（344） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（34） | `0`／`0`／`⇒ 紅 []；rc 0`（60） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（556） | `0`／`0`／`⇒ 紅 []；rc 0`（606） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（280） | `0`／`0`／`⇒ 紅 []；rc 0`（336） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（278） | `0`／`0`／`⇒ 紅 []；rc 0`（320） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（280） | `0`／`0`／`⇒ 紅 []；rc 0`（320） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（282） | `0`／`0`／`⇒ 紅 []；rc 0`（338） |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（8） | `0`／`0`／`⇒ 紅 []；rc 0`（10） |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（290） | `0`／`0`／`⇒ 紅 []；rc 0`（318） |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（4） |
| `92` | `python3 verify/probes/probe_WG9398_rw25.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `93` | `python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `94` | `python3 tests/test_pool_slot.py` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`（2） |
| `95` | `python3 verify/probes/probe_WG9399_k960x.py selftest <repo>` | (甲)(乙) `1`／`0`／`⇒ 紅 ['E1', 'E1′', 'E1″', 'E2', 'E3', 'E4', 'E5', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E7', 'E8', 'E8′', 'E9', 'E10', 'E11', 'E11', 'E11′', 'E11′', 'E11′', 'E11′', 'E12', 'E12', 'E13', 'E13′', 'E14', 'E15', 'E15', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', '丙·例外', '丁·例外', 'M1', 'M2', 'M4', 'M6', 'M8', 'M10']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `96` | `python3 verify/probes/probe_WG9399_k960x.py wiring <repo> bd7da4d` | (甲)(乙) `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4']；rc 1`（14） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `97` | `python3 verify/probes/probe_WG9399_k960x.py run <repo>` | (甲)(乙) `1`／`0`／`⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`（292） | `0`／`0`／`⇒ 紅 []；rc 0`（324） |

## 附錄乙　審查之 WARNING-1 之重現之腳本（倉外·容器暫存）

### `rv_chk485.py`（執行端之自重現·以審查者之 `rt_a.py` 之 `gen`／`xf` 生例 `485`）

````python
"""執行端之自重現（審查 WARNING-1·例 485）：經 end_block_pick 之同一路徑（無效者 buffer(0)）求宗 ∩ R_end 之型與臨端線。"""
import runpy
import random
import sys

import numpy as np
from shapely.geometry import Polygon

sys.argv = ['x', '/tmp/rv399p1/app_head.py', '0', '1', '/dev/null']
g = runpy.run_path('/tmp/rv399p1/rt_a.py')
rng = random.Random(20261029)
gen, ns = g['gen'], g['ns']
c = 0
while c < 485:
    r = gen(rng)
    if r is None:
        continue
    blk0, parts0, W, kinds = r
    ang = rng.uniform(0, 360); mir = rng.random() < 0.5
    f, v = g['xf'](ang, mir, 3.0e5 + rng.uniform(-5e4, 5e4), 2.6e6 + rng.uniform(-5e4, 5e4))
    c += 1
D = blk0.bounds[3]
blk = Polygon([f(p) for p in blk0.exterior.coords])
cad = v((0.0, 1.0))
geo = ns['end_block_side_geom'](blk, v((1.0, 0.0)), np.array(f((0, 0))), np.array(f((W, 0))), cad,
                                ns['alloc_normal_axis'](cad), 3.5, 'left', _label='BX')
re_ = geo['r_end']
eg = ns['end_block_end_geom'](blk, v((1.0, 0.0)), np.array(f((0, 0))), np.array(f((W, 0))), 'left', re_,
                              [tuple(f((-80, D))), tuple(f((W + 80, D)))], _label='BX')
cache = {}
ents = [{"tp": {"暫編地號": f"Q{i}(1)", "原地號": f"Q{i}", "polygon_coords": [list(f(q)) for q in p.exterior.coords]},
         "pre_position": 0, "is_corner_winner": False, "side": "中段"} for i, p in enumerate(parts0)]
ns['end_block_apply'](ents, blk_label="BX", block_poly=blk, d_hat=v((1.0, 0.0)), corner_pt=np.array(f((0, 0))),
                      front_p2=np.array(f((W, 0))), cad_alloc=cad, allocation_dir=ns["alloc_normal_axis"](cad), min_width=3.5,
                      has_side_pk={"left": False, "right": False}, has_side_cad={"left": False, "right": False},
                      corner_range_polys={}, trial=lambda tp, s, w: (1.0, 5.0), cache=cache, allow_forced=lambda s: True,
                      baseline_pts=[tuple(f((-80, D))), tuple(f((W + 80, D)))])
print('app 之列（左）', [(x['暫編地號'], x['跨占R_end(㎡)'], x['臨端線(m)'], x['評選指數']) for x in cache['BX']['left']['候選']],
      '端線', cache['BX']['left']['端線(m)'])
for i, p in enumerate(parts0):
    pg = Polygon([f(q) for q in p.exterior.coords])
    v = pg.is_valid
    if not v:
        pg = pg.buffer(0)
    ov = pg.intersection(re_).area
    if ov <= 1.0:
        print('part', i, '跨占', round(ov, 4), '⛔ 入列')
        continue
    cut = re_.intersection(pg)
    subs = [x.geom_type for x in getattr(cut, 'geoms', [])]
    poly_only = [x for x in getattr(cut, 'geoms', [cut]) if x.geom_type in ('Polygon', 'MultiPolygon')]
    from shapely.ops import unary_union
    pu = unary_union(poly_only) if poly_only else None
    print('part', i, 'valid', v, '跨占', round(ov, 4), 'cut', cut.geom_type, subs,
          '全 cut 之臨端線', round(sum(ns['_boundary_len_on_line'](cut, a, b) for a, b in eg['end_segs']), 4),
          '唯多邊形之臨端線', round(sum(ns['_boundary_len_on_line'](pu, a, b) for a, b in eg['end_segs']), 4) if pu else None)
print('end_len', round(eg['end_len'], 4))
````

出艙：`app 之列（左） [('Q1(1)', 18.57, 11.24, 0.970754)] 端線 11.51`／`part 0 跨占 0.6264 ⛔ 入列`／`part 1 valid True 跨占 18.5703 cut GeometryCollection ['Polygon', 'LineString'] 全 cut 之臨端線 11.2361 唯多邊形之臨端線 6.2036`／`end_len 11.5144`。同例以未變換之本地座標量之 ⇒ `part 1 valid True 跨占 18.5703 cut Polygon [] 全 cut 之臨端線 6.2036 唯多邊形之臨端線 6.2036`。

### `rt_a.py`（審查者之隨機測（甲）·`python3 rt_a.py <app 之複本> <例數> <seed> <出 json>`）

````python
# 審查者之獨立隨機測（甲）：一端之宗之分割·直呼 end_block_apply
import sys, os, io, json, math, random, contextlib, builtins
sys.dont_write_bytecode = True
APP, N, SEED, OUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
sys.path.insert(0, '/tmp/w/verify')
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns, _ = harvest(APP)
import numpy as np
from shapely.geometry import Polygon, LineString, box
from shapely.ops import substring, unary_union

MW = 3.5
_bround = builtins.round
def _idround(x, n=None):
    return x if n is not None else _bround(x)

def xf(ang, mirror, tx, ty):
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    def f(p):
        x, y = float(p[0]), float(p[1])
        if mirror: x = -x
        return (c*x - s*y + tx, s*x + c*y + ty)
    def v(d):
        x, y = float(d[0]), float(d[1])
        if mirror: x = -x
        return np.array((c*x - s*y, s*x + c*y))
    return f, v

def polys(g):
    if g.is_empty: return []
    if g.geom_type == 'Polygon': return [g]
    return [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon']

def gen(rng):
    W = rng.uniform(25, 60); D = rng.uniform(15, 40)
    kind_l = rng.choice(['straight', 'incline', 'bent']); kind_r = rng.choice(['straight', 'incline', 'bent'])
    left = [(0.0, 0.0)]; right = [(W, 0.0)]
    if kind_l == 'straight': ltop = (0.0, D)
    elif kind_l == 'incline': ltop = (rng.uniform(-6, 6), D)
    else:
        ltop = (rng.uniform(-2, 2), D); left.append((rng.choice([-1, 1])*rng.uniform(0.5, 3.0), rng.uniform(0.3, 0.7)*D))
    if kind_r == 'straight': rtop = (W, D)
    elif kind_r == 'incline': rtop = (W + rng.uniform(-6, 6), D)
    else:
        rtop = (W + rng.uniform(-2, 2), D); right.append((W + rng.choice([-1, 1])*rng.uniform(0.5, 3.0), rng.uniform(0.3, 0.7)*D))
    # ring：p1 → p2 → 右之折 → 右上 → 左上 → 左之折 → p1
    ring = [(0.0, 0.0), (W, 0.0)] + right[1:] + [rtop, ltop] + list(reversed(left[1:]))
    blk = Polygon(ring)
    if not blk.is_valid: return None
    lline = LineString([(0.0, 0.0)] + left[1:] + [ltop])
    rline = LineString([(W, 0.0)] + right[1:] + [rtop])
    parts = []
    def strip_of(line, w, frac):
        if frac < 1.0:
            L = line.length; a = rng.uniform(0, L*(1-frac)); line = substring(line, a, a + frac*L)
        return blk.intersection(line.buffer(w, cap_style=2, join_style=2))
    used = []
    # 左端之條片
    sl = None
    if rng.random() < 0.85:
        w = math.exp(rng.uniform(math.log(0.003), math.log(0.2)))
        frac = 1.0 if rng.random() < 0.6 else rng.uniform(0.1, 1.0)
        sl = strip_of(lline, w, frac)
    sr = None
    if rng.random() < 0.85:
        w = math.exp(rng.uniform(math.log(0.003), math.log(0.2)))
        frac = 1.0 if rng.random() < 0.6 else rng.uniform(0.1, 1.0)
        sr = strip_of(rline, w, frac)
    xs = sorted(set([-50.0] + [rng.uniform(1.5, 7.0)] + [rng.uniform(7.5, W - 7.5) for _ in range(rng.randint(0, 3))]
                     + [W - rng.uniform(1.5, 7.0)] + [W + 50.0]))
    strips = []
    for x0, x1 in zip(xs[:-1], xs[1:]):
        g = blk.intersection(box(x0, -1.0, x1, D + 1.0))
        for s_ in [sl, sr]:
            if s_ is not None: g = g.difference(s_)
        if rng.random() < 0.3:
            ym = rng.uniform(0.2, 0.8)*D
            strips.append(g.intersection(box(x0 - 1, -1, x1 + 1, ym)))
            strips.append(g.intersection(box(x0 - 1, ym, x1 + 1, D + 1)))
        else:
            strips.append(g)
    seq = ([sl] if sl is not None else []) + strips + ([sr] if sr is not None else [])
    # 條片與鄰宗之序之偶換（原位次最先之判之兩向皆測）
    if sl is not None and rng.random() < 0.2:
        seq[0], seq[1] = seq[1], seq[0]
    out = []
    for g in seq:
        for p in polys(g):
            if p.area > 1e-9: out.append(p)
    if any(len(p.interiors) for p in out): return None
    # 分割之健全：各宗由外框之座標重建後皆有效、面積之和 ＝ 街廓、兩兩無重疊
    rb = [Polygon(list(p.exterior.coords)) for p in out]
    if not all(q.is_valid for q in rb): return None
    if abs(sum(q.area for q in rb) - blk.area) > 1e-6: return None
    if abs(unary_union(rb).area - blk.area) > 1e-6: return None
    return blk, out, W, (kind_l, kind_r)

def lines_of(g):
    if g.is_empty: return []
    if g.geom_type == 'LineString': return [g]
    return [x for x in getattr(g, 'geoms', []) if x.geom_type == 'LineString']

def ref_alloc(geom, r_end, cut_list, with_lines=False):
    """取樣之獨立參照：每 2 mm 之點，R_end 有合格之邊蓋之者，歸首一蓋之之宗。"""
    res = {}
    for a, b in geom['end_segs']:
        a = np.array(a, float); b = np.array(b, float); d = b - a; L = float(np.hypot(*d))
        if L <= 0: continue
        n = max(1, int(math.ceil(L/0.002))); t = (np.arange(n) + 0.5)/n
        az = math.degrees(math.atan2(d[1], d[0])) % 180.0
        def cov(g):
            m = np.zeros(n, bool)
            rings = []
            for p in polys(g):
                rings.append(np.asarray(p.exterior.coords)); rings += [np.asarray(r.coords) for r in p.interiors]
            if with_lines:
                rings += [np.asarray(l.coords) for l in lines_of(g)]
            for R in rings:
                for i in range(len(R) - 1):
                    e0, e1 = R[i], R[i+1]
                    if math.hypot(*(e1 - e0)) < 1e-9: continue
                    sa = math.degrees(math.atan2(e1[1]-e0[1], e1[0]-e0[0])) % 180.0
                    da = abs(sa - az); da = min(da, 180 - da)
                    if da > 2.0: continue
                    pa = abs(d[0]*(e0[1]-a[1]) - d[1]*(e0[0]-a[0]))/L; pb = abs(d[0]*(e1[1]-a[1]) - d[1]*(e1[0]-a[0]))/L
                    if pa > 0.05 or pb > 0.05: continue
                    ta = float(np.dot(e0 - a, d))/L/L; tb = float(np.dot(e1 - a, d))/L/L
                    lo, hi = min(ta, tb), max(ta, tb)
                    m |= (t > lo) & (t < hi)
            return m
        free = cov(r_end)
        for k, cg in cut_list:
            c = cov(cg) & free
            res[k] = res.get(k, 0.0) + float(c.sum())*L/n
            free &= ~c
    return res

rng = random.Random(SEED)
stat = dict(cases=0, gen_skip=0, apply_err={}, ends=0, ends_err=0, rows=0,
            fail_round_line=0, fail_round_idx=0, fail_unr_line=0, fail_unr_idx=0, fail_ref=0,
            max_round_line_over=-1e9, max_round_idx_over=-1e9, max_unr_line_over=-1e9, max_unr_idx_over=-1e9,
            max_ref_diff=0.0, thin_cases=0, small_strip_cases=0, bent_cases=0, examples=[])
while stat['cases'] < N:
    g = gen(rng)
    if g is None:
        stat['gen_skip'] += 1; continue
    blk0, parts0, W, kinds = g
    ang = rng.uniform(0, 360); mir = rng.random() < 0.5
    f, v = xf(ang, mir, 3.0e5 + rng.uniform(-5e4, 5e4), 2.6e6 + rng.uniform(-5e4, 5e4))
    blk = Polygon([f(p) for p in blk0.exterior.coords])
    D = blk0.bounds[3]
    ents = [{"tp": {"暫編地號": f"Q{i}(1)", "原地號": f"Q{i}", "polygon_coords": [list(f(c)) for c in p.exterior.coords]},
             "pre_position": 0, "is_corner_winner": False, "side": "中段"} for i, p in enumerate(parts0)]
    cad = v((0.0, 1.0))
    kw = dict(blk_label="BX", block_poly=blk, d_hat=v((1.0, 0.0)), corner_pt=np.array(f((0, 0))), front_p2=np.array(f((W, 0))),
              cad_alloc=cad, allocation_dir=ns["alloc_normal_axis"](cad), min_width=MW,
              has_side_pk={"left": False, "right": False}, has_side_cad={"left": False, "right": False},
              corner_range_polys={}, trial=lambda tp, s, w: (1.0, 5.0), allow_forced=lambda s: True,
              baseline_pts=[tuple(f((-80, D))), tuple(f((W + 80, D)))])
    stat['cases'] += 1
    if 'bent' in kinds: stat['bent_cases'] += 1
    if any(min(p.minimum_rotated_rectangle.exterior.length, 1e9) and p.area/ max(p.length/2, 1e-9) < 0.05 for p in parts0):
        stat['thin_cases'] += 1
    if any(p.area <= 1.0 for p in parts0): stat['small_strip_cases'] += 1
    try:
        c1 = {}; ns["end_block_apply"](list(ents), cache=c1, **kw)
        ns['round'] = _idround
        try:
            c2 = {}; ns["end_block_apply"](list(ents), cache=c2, **kw)
        finally:
            del ns['round']
    except Exception as ex:
        k = f"{type(ex).__name__}: {str(ex).splitlines()[0][:90]}"
        stat['apply_err'][k] = stat['apply_err'].get(k, 0) + 1
        continue
    # 參照之幾何：直取各端之幾何
    for sd in ('left', 'right'):
        r1, r2 = c1['BX'][sd], c2['BX'][sd]
        stat['ends'] += 1
        if r2.get('端線(m)') is None:
            stat['ends_err'] += 1; continue
        L = float(r2['端線(m)'])
        rows1, rows2 = r1['候選'], r2['候選']
        n = len(rows1); stat['rows'] += n
        sl1 = sum(float(r['臨端線(m)']) for r in rows1); si1 = sum(float(r['評選指數']) for r in rows1)
        sl2 = sum(float(r['臨端線(m)']) for r in rows2); si2 = sum(float(r['評選指數']) for r in rows2)
        o1 = sl1 - (L + n*0.005); o2 = si1 - (1 + n*5e-7); o3 = sl2 - (L + 1e-6); o4 = si2 - (1 + 1e-6)
        stat['max_round_line_over'] = max(stat['max_round_line_over'], o1); stat['max_round_idx_over'] = max(stat['max_round_idx_over'], o2)
        stat['max_unr_line_over'] = max(stat['max_unr_line_over'], o3); stat['max_unr_idx_over'] = max(stat['max_unr_idx_over'], o4)
        bad = False
        if o1 > 0: stat['fail_round_line'] += 1; bad = True
        if o2 > 0: stat['fail_round_idx'] += 1; bad = True
        if o3 > 0: stat['fail_unr_line'] += 1; bad = True
        if o4 > 0: stat['fail_unr_idx'] += 1; bad = True
        # 獨立參照（取樣）
        geo = ns['end_block_side_geom'](blk, v((1.0, 0.0)) if True else None, np.array(f((0, 0))), np.array(f((W, 0))), cad,
                                         ns["alloc_normal_axis"](cad), MW, sd, _label='BX')
        eg = ns['end_block_end_geom'](blk, v((1.0, 0.0)), np.array(f((0, 0))), np.array(f((W, 0))), sd, geo['r_end'], kw['baseline_pts'], _label='BX')
        r_end = geo['r_end']
        seq = ents if sd == 'left' else list(reversed(ents))
        cl = []
        for e in seq:
            pg = Polygon(e['tp']['polygon_coords'])
            if not pg.is_valid: pg = pg.buffer(0)
            if pg.intersection(r_end).area > 1.0:
                cl.append((e['tp']['暫編地號'], r_end.intersection(pg)))
        ref = ref_alloc(eg, r_end, cl)
        got = {r['暫編地號']: float(r['臨端線(m)']) for r in rows2}
        md = max([abs(got.get(k, 0.0) - ref.get(k, 0.0)) for k in set(got) | set(ref)] or [0.0])
        stat['max_ref_diff'] = max(stat['max_ref_diff'], md)
        if md > 0.02:
            stat['fail_ref'] += 1; bad = True
            if any(lines_of(cg) for _, cg in cl): stat['fail_ref_cut_has_lines'] = stat.get('fail_ref_cut_has_lines', 0) + 1
        ref2 = ref_alloc(eg, r_end, cl, with_lines=True)
        md2 = max([abs(got.get(k, 0.0) - ref2.get(k, 0.0)) for k in set(got) | set(ref2)] or [0.0])
        stat['max_ref2_diff'] = max(stat.get('max_ref2_diff', 0.0), md2)
        if md2 > 0.02: stat['fail_ref2'] = stat.get('fail_ref2', 0) + 1
        if bad and len(stat['examples']) < 6:
            stat['examples'].append(dict(case=stat['cases'], side=sd, kinds=kinds, L=L, n=n, sum_line_unr=sl2, sum_idx_unr=si2,
                                         got={k: _bround(x, 4) for k, x in got.items()}, ref={k: _bround(x, 4) for k, x in ref.items()}))
json.dump(stat, open(OUT, 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: stat[k] for k in stat if k != 'examples'}, ensure_ascii=False))
````
