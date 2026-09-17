# `W-G.9-308_補令一`　施工單（**輕**）：`K-9-38`／`K-9-39` 之鑄 ／ 裁定 B5 之末端註記 ／ `自誤 420`・`421` 之鑄 ／ 宣告框補款 `⑨` ／ `W-G.9-308` 款 `4` 之靜態結案 ／ `308R` 未入倉落檔之處置

> **態**｜開工 ＝ `bc15a55f78f3fb9f1a7201fb719fb119c0942487` **或其後裔**（發單側自倉 `ls-remote` 實查·🛑 CC 須自行重跑·**全 `40` 碼**）。
> **單** ＝ `docs/orders/W-G.9-308_補令一_K-9-38與K-9-39之鑄及自誤420至421與款4之靜態結案.md`（工項零 ＝ 本單原封入倉）。
> **分級** ＝ **輕**（登記 ＋ 靜態探針一支·**零生產碼**·**⛔ `run_verification`**·**⛔ 開分支**·**⛔ 修批**）。
> 🛑 **本批鑄號 ＝ `K-9-38` ＋ `K-9-39` ＋ `自誤 420` ＋ `自誤 421`**（**四號**·逐字由本單供）；宣告框補款 `⑨` 係補款（`戒 36`）⛔ 鑄號；`GB`／`VR`／坑 **⛔ 鑄**。
> 🔑 **補令之射程**：本單辦 `W-G.9-308` 之未竟（`308R` `§六-4` 器紅）及其後之登記；**⛔ 改 `W-G.9-308` 單一字**。與該單相牴者**僅一點**：該單款 `4` 之完整全量**⛔ 再跑 `run_verification`**，改以本單工項四之**靜態全證**結案（`§零-2` 裁 `2`）。
> 🔴 **修批之號仍為 `W-G.9-309`**（`K-6` 之 `K-9-32` 落地狀態欄、`K-9-37` 末句、`GB` 簿 `GB308` 節所載·逐字見倉）；**本單⛔ 占其號**、⛔ 辦修批、⛔ 自續 `W-G.9-309`。
> 🔑 **序**：**① `§二` 工項零**（單獨 `commit`·單獨 `push`）⇒ **② `§一` 開工閘** ⇒ **③ `§三` 工項一** ⇒ **④ `§四` 工項二** ⇒ **⑤ `§五` 工項三** ⇒ **⑥ `§六` 工項四**（靜態）⇒ **⑦ `§七` 工項五** ⇒ **⑧ `§八` 收工閘**。
> 🛑 **辦畢 ⇒ 出報告 ⇒ 停**。⛔ 呈 KL。
> 🗑 **本單為第二版**，取代同名之第一版（其 `SELF_SHA256` ＝ `5dfecd21c620d6b4273719f84c9599c930d3cd89d8c36206aeb91e607c8808b2`·全檔 `sha256` `45b679882f09fa185e4c2748e4dda611943b6795b930999b0df95b8f237ff5e5`·`50169` B·**⛔ 入倉**）；二版之差僅在 `K-9-39` 與裁定 B5 之末端註記（KL `2026-09-17` 就他形調配池之答）及其連帶之 `§零-2` 裁 `5`、`§二` 入倉前閘、`【驗收】`。**第一版已入倉者 ⇒ 本版⛔ 辦、停、上呈。**

---

## `§零`　發單側之核可・裁（**⛔ CC 自裁·⛔ CC 重辦**）

### `§零-1`　`W-G.9-308R` 之復驗（發單側自倉獨立·沙盒 `Python 3.12.3`·態 `bc15a55`）

| # | 項 | 發單側實得（產生方式） | 判 |
|---|---|---|---|
| `1` | 主線 | `bc15a55f78f3fb9f1a7201fb719fb119c0942487`；`git rev-list --count aa1394c..bc15a55` ＝ `11`；`git log --numstat --format= aa1394c..bc15a55` 之 `14` 列中刪除欄非 `0` 者 ＝ `0` | ✅ |
| `2` | 生產碼 `34` 檔 | 母體 ＝ `git ls-tree --name-only HEAD verify/` ⋂ `*.py`（`33`）＋ `app.py`；`git diff --numstat f24e1d7a bc15a55 -- <34 檔>` ＝ `0` 檔；第二態 ＝ 逐檔 blob `sha1` 對照相異 `0`；`app.py` ＝ `4379108a4856714078c410ff4e6291ecfdf6d2c1` | ✅ |
| `3` | 四簿 | `probe_WG9267_issuer_measurers.py registry` ⇒ 自誤 `409`／`419`（缺 `[106, 355, 356, 357]`）；`GB` `168`／`170`（缺 `[12, 87]`）；`VR` `80`／`95`（缺 `[73, 75]`）；`K-9` `36`／`37`（缺 `[]`） | ✅ |
| `4` | 坑 | `probe_WG9269_pit_index.py HEAD` ⇒ 以程式自其資料列計數 `94`／`94` 可解析·末 `bp`；第二態 ＝ 標籤序列與「`1`〜`26`、`a`〜`z`、`aa`〜`az`、`ba`〜`bp`」之期望序列逐項相等（母體 ＝ HEAD 之追蹤 `.md` `830` 檔） | ✅ |
| `5` | `baselines`／refs | `git ls-tree -r HEAD verify/baselines \| sha256sum` ＝ `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·`298` 列；`git ls-remote origin 'refs/heads/verify/*'` ＝ `20` 列·`gb170` `0`·`p3a` `1`；`p3a` `is-ancestor` `rc = 1` | ✅ |
| `6` | `308R` 報告 | `93171` B；列數 ＝ `1108`（`wc -l` ＝ `splitlines` ＝ `LF` 數） | ✅ |
| `7` | `§六-7` 分類表 | 自 `verify/out/WG9308R_lots.log` 之 `§六-7` 逐宗全量表之資料列（`88` 列）以程式重分類；`S_raw` 取 hex 欄自解、`W` 取同街廓 `驗_A_W` 之值集，自算 `S_raw − W` 與該表帶號欄相異 `0` ⇒ 八格之列數、`< W` 數、`驗_A幾何` 分布**逐格相符**；`38` ＝ `18` ＋ `20` | ✅ |

### `§零-2`　裁（**`8` 項**）

1. **`308R` 之受領**：工項零、開工閘 `14`／`14`、工項一（自誤 `417`〜`419`）、工項二（`K-9-31`〜`K-9-37` ＋ 二則末端註記 ＋ `GB` 簿追加）、工項三款 `1`〜`8`、工項四款 `1`／`2`／`3`／`5`／`6`／`7` ⇒ **受領**。款 `4` 之器紅（列數 `3` ≠ 強制呼叫總數 `21`）之歸因 ＝ **量測器紅**（其母體僅取主幹二進入）⇒ **受領**；CC 依單⛔ 重跑 ⇒ **處置正確**。

2. **款 `4` 之結案：改以靜態全證，⛔ 再跑 `run_verification`**。依據（發單側自倉·態 `bc15a55`·AST 實查）：
   - 受詞之呼叫端 ＝ `verify/stepg_pipeline.py` 之 `_run_step_g_impl` 內之 `for blk_label, parcels_in_blk in parcels_by_block.items():`（AST 區間 `526`–`1634`）；`_corner_buffer_S` 之呼叫於 `659`／`670`；
   - 名集 N7（`_side_lines_blk`／`_sl_left`／`_sl_right`／`_side_mid_left`／`_side_mid_right`／`_has_left_corner`／`_has_right_corner`）於該迴圈體內之首次賦值於 `679`〜`685`；**首次賦值前之讀取 ＝ `0`**；
   - 該二呼叫之引數逐字（去其換行）＝ `blk_poly, d_hat, corner_pt, allocation_dir_block, float(_l_min), 'left', _label=blk_label`（右側同形）⇒ **⛔ 含 N7 之任一名**。
   - ⇒ 強制呼叫時框內之 N7 **構造上即為前一輪次之綁定**（首輪則未存在），且**⛔ 為該呼叫所用** ⇒ `308R` `§六-4` 之九筆「存在而相異」係此靜態次序之**必然**，**⛔ 構成現行配地之缺陷**；其為**修批之陷阱**（`W-G.9-308` `§零-2` 裁 `7` 所具名）。
   - ⇒ 以工項四之探針對**生產碼 `34` 檔之全部呼叫**全證之，並立為恆常附款（`§一-1` 款 `c`）。
   - 🔒 **併記**：`308R` `§六-7` 之「該側有無側街」取自進入時之登記表參照（`verify/probes/probe_WG9308R_lots.py` 之 `REG_SNAP`·該檔 `784`〜`798` 列逐字）、**⛔ 取框內值** ⇒ 其分類**⛔ 受** `§六-4` 之影響。
   - 🔑 發單側以工項四之探針（本單 `§六` 所載之位元組）於 `bc15a55` 實跑：呼叫 `7`（`Name` 形 `4`／`Subscript` 形 `3`）；通則命中 `0`；引數含後綁之名 `0`；N7 首次賦值前之讀取 `0`；判別力二造綠。

3. **`自誤 420`（發單側之責）**：`308R` 自捕 `3`（`W-G.9-308` `§六-2` 款 `2` 之欄載「未捨入」而其取法所名之二鍵皆為捨入值）⇒ 鑄（逐字見 `§三`）。發單側已自 blob 實查：`app.py`（blob `4379108a…`）`solve_G_binary` 之 `return` 逐字 `'G': round(G_conv, 2)`／`'area_geom': round(area_conv, 2)`；`_solve_G_one` 之 fallback 路徑逐字 `_r['area_geom'] = round(_r.get('S', 0) * avg_depth, 2)`。

4. **`自誤 421`（發單側之責）**：交接文九（`claude.ai` 側換手·九·`2026-09-17`·⛔ 在倉）載「`K-9-39` 可鑄」，未就調配池之落位次序全倉查既有正典；新窗鑄前全倉查得 `5` 列 `4` 檔（框 ＝ 正則 `(裁定\s*B\s*5|裁定B[^\n]{0,6}B5|跨占大之一側|跨占大的一側|起始側)` 之逐列子字串框；母體 ＝ HEAD 之追蹤 `.md`／`.py` `1197` 檔·態 `bc15a55`；二數並報：子字串框 `5` 列 `4` 檔／列首錨框 `^\s*` ＋ 同式 `0` 列），其中 `docs/specs/W-G.4_KL域裁_兩階段落位_部分面積拆分_Rw側選.md` 之 B5 與之同受詞相牴 ⇒ 呈 KL ⇒ KL `2026-09-17` 裁「取代」 ⇒ 鑄（逐字見 `§三`）。

5. **`K-9-38`／`K-9-39` 之鑄 ＋ 裁定 B5 之末端註記**（逐字見 `§四`）。KL 之語已由發單側以原對話之 KL 訊息逐字對照（過往對話之檢索）。`K-9-39` 併載 KL `2026-09-17` 就他形調配池（一端為末端塊或無街角者）之答：亦採「最左,最右,左,右...」，臨末端塊之端⛔ 設藍影、仍驗內接矩形 ⇒ **`K-9-39` 之射程及於任一形之調配池**。

6. **宣告框補款 `⑨`（發單側之裁·前例 ＝ 補款 `⑧`）**：`308R` 自捕 `4`（`D2` 對「他批對本單之前瞻引用」無排除款）⇒ 比照補款 `⑤` 立之（逐字見 `§五`）。**首次施行之實測**（發單側·母體 ＝ 各態之全 `docs/`·判法 ＝ 補款 `①` 之三形帶數字邊界）：
   - `W-G.9-308` @ `aa1394c`（母體 `806` 檔）：`D1` `0`／`D2` `2`／`D3` `0`；`D2` 二列所在檔之檔名所載單號皆 ＝ `W-G.9-307` ⇒ 依 `⑨` 之 `D2` ＝ **`0`**（與 `308R` `§零` 自解 `1` 之讀法乙同結論）；
   - 判別力[必非零] `W-G.9-307` @ `bc15a55`（母體 `808` 檔）：`D1` `5`（⛔ 受 `⑨` 影響）⇒ **仍占用**。

7. **`308R` 未入倉之落檔（`§七-5` 所具名之六檔）⇒ 入倉**。前例：`git ls-tree --name-only HEAD verify/out/` 之名（小寫化）含 `pit` 者 ＝ `64`（態 `bc15a55`·例 `verify/out/WG9301R_pit_post.log`）。**逐檔 `git add`**；不存在者 loud 具名、**⛔ 重生**（母體 ＝ `W-G.9-308R` `§七-5` 所列六名）。

8. **`308R` 自捕 `1`／`2`／`5`／`6`／`7`**：照實併記已足，**⛔ 鑄號**。

---

## `§一`　開工閘（**`13` 項**·**每列同格載其產生指令**·🛑 **跑於 `§二` 之後**）

| # | 受詞（指令逐字） | **期值／判準** |
|---|---|---|
| `0` | `python -c "import sys; print(sys.version)"` | 出艙逐字；期 `3.13.11` 起首——不符 ⇒ **loud 具名、停** |
| `1` | `git ls-remote origin refs/heads/wip/s1-endpart` | `bc15a55f78f3fb9f1a7201fb719fb119c0942487` 或其後裔（後裔以 `merge-base --is-ancestor` 證·`rc` 緊接指令） |
| `2` | `git rev-parse HEAD:app.py`（框 ＝ blob `sha1`） | `4379108a4856714078c410ff4e6291ecfdf6d2c1` |
| `3` | `python verify/probes/probe_order_preflight.py <本單>` | `P-5` `SELF_SHA256` 逐位相符；🔴 `0`；🟡 **逐項具名處置**（發單側出單前實跑之數見 `§十`·CC 須自行重跑） |
| `3'` | 受詞自證（以器所印之檔名列） | [必真] 含 `補令一` ＝ `True`／[必偽] 含 `補令二` ＝ `False` |
| `4` | `python verify/probes/probe_WG9267_issuer_measurers.py registry`（器之輸出為正典） | 自誤 `409`／`419`（缺 `[106, 355, 356, 357]`）｜`GB` `168`／`170`（缺 `[12, 87]`）｜`VR` `80`／`95`（缺 `[73, 75]`）｜`K-9` `36`／`37`（缺 `[]`） |
| `5` | `python verify/probes/probe_WG9269_pit_index.py <rev 釘死>`（全量落檔·`open(p,'wb')`） | `94`／`94`·末 `bp`；器自印判別力二造綠 |
| `6` | `git ls-tree HEAD --name-only -z verify/` ⋂ `*.py` ＋ `app.py`（正面列舉） | `34` 檔；判別力[必不命中] 子層 `*.py` 須 `> 0`（⛔ 定值·發單側於 `bc15a55` 得 `329`） |
| `7` | `git ls-tree -r HEAD verify/baselines \| sha256sum`（`core.quotePath` 預設） | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·`298` 列 |
| `8` | `git ls-remote origin 'refs/heads/verify/*'` | `20` 列；`verify/W-G.9-299-gb170` 命中 `0`；`verify/W-G.9-269-p3a` 命中 `1` |
| `9` | 四受改檔之期初（`git rev-parse HEAD:<路徑>` 前先 `git cat-file -e`·取 bytes） | 自誤簿 `4d9308611f436e861c38f50c16b208bb0b0bbf13`·`886273` B／`K-6` `d3986761eeae8a3faa9cd6711c3c2850ebf1cc8d`·`330691` B／`CLAUDE.md` `579d8df329d3e22861d08062b15b284cabcb834a`·`236365` B／`W-G.4` 域裁檔 `5b2fd952425b168507cc194c73fdd7c0d3b2ffd7`·`9013` B（態 `bc15a55`；主線有後裔者以實得為準並具名差異之 `commit`）；期初 bytes 存錄於記憶體 |
| `10` | 本批新物之未占（`git ls-tree -r --name-only -z HEAD`·取 bytes） | 路徑含 `WG9308S1` 者 ＝ `0`；檔名含 `W-G.9-308_補令一` 者 ＝ **`1`**（＝ 工項零所入之本單·**跑於 `§二` 之後**）|
| `11` | 未入倉落檔之存否（`git status --porcelain -z -- verify/out/`·取 bytes） | 逐檔出艙六名之態：`verify/out/WG9308R_pit_pre.log`／`.err`、`WG9308R_pit_s3.log`／`.err`、`WG9308R_pit_post.log`／`.err`（⛔ 預設其存在） |

🔒 **本表之資料列 ＝ `13`**（`0`／`1`／`2`／`3`／`3'`／`4`／`5`／`6`／`7`／`8`／`9`／`10`／`11`·發單側以程式自本單計得）。

### `§一-1`　恆常附款（**逐項適用·⛔ 省**）

🛑 **`W-G.9-308` `§一-1` 之恆常附款全數逐項適用**（逐字見該單·⛔ 省）。
🆕 **本單所增**：
（`a`）**凡單內鑄一攔法者，出單前以該攔法逐款回掃本單全文並出艙回掃之結果**；**重擬之版次對前版未改之款重跑攔法**（`自誤 420`）；
（`b`）**凡擬鑄之裁，以其受詞之關鍵語及其同義詞全倉查既有之裁，查得者同格具名其與新裁之關係（取代／併存／例外）**（`自誤 421`）；
（`c`）**凡於 `_corner_buffer_S` 之呼叫所在之迴圈體內新增讀取 N7 之任一名者，讀取點須位於該迴圈體內之綁定語句之後**；其閘 ＝ `verify/probes/probe_WG9308S1_bindorder.py` 之「通則命中」與「N7 首次賦值前之讀取」皆 ＝ `0`（`§零-2` 裁 `2`）。

---

## `§二`　工項零：**本單原封入倉**（主線·🔑 **先於開工閘**）

落點 ＝ `docs/orders/W-G.9-308_補令一_K-9-38與K-9-39之鑄及自誤420至421與款4之靜態結案.md`；**⛔ 改一字**。
🛑 **入倉前閘**：`git ls-tree -r --name-only -z HEAD docs/orders/` 之名（取 bytes）含 `W-G.9-308_補令一` 者須 ＝ `0`；`≠ 0`（第一版已入倉）⇒ **停、⛔ 辦本版、上呈**。
🔒 整全性之判準 ＝ `SELF_SHA256`（`P-5`）；判別力二造（必綠 ＝ 原檔／必紅 ＝ 改一位元組之副本·**該副本⛔ 入倉**）須出艙。
入倉後出艙：blob `sha1` ＋ blob 內容 `sha256` ＝ 磁碟 ＝ 源；`CR` ＝ `0`（讀 blob 取 bytes；判別力[必非零] ＝ `data/V6.dxf`）；`deletions` ＝ `0`。
🛑 **落地後即 `push`**（生產碼 `0` 行），**其後方跑 `§一`**。

---

## `§三`　工項一：**`自誤 420` ＋ `自誤 421` 之鑄**（主線·**二段分列 `commit`**）

🔑 界：`<!-- ZW420-BEGIN -->`／`<!-- ZW420-END -->`；`<!-- ZW421-BEGIN -->`／`<!-- ZW421-END -->`。
落點皆 ＝ `docs/reports/W-G.9波_claude.ai側自誤登記.md` **檔末追加**（`420`、`421` 依序）。
🛑 唯一性之框 ＝ **整列逐位相等**·母體 ＝ 本單單檔·各哨兵須命中 `1`；併報子字串框之數（**二數並報**）。
🛑 「payload」＝ 界內之列去其首尾之空列；⛔ 剝層、⛔ 加 `> `、⛔ 改一字；落檔 `open(p,'wb')`；追加之式 ＝ `old + b'\n' + payload + b'\n'`。

<!-- ZW420-BEGIN -->

### 🩸 `自誤 420`　**施工單所鑄之攔法於同一單內即未施行：`W-G.9-308` `§六-2` 款 `2` 之欄載「未捨入之 `G` 與 `area_geom`」，而其取法所名之二鍵皆為捨入值**

**形**：`W-G.9-308` `§六-2` 款 `2` 之 `jsonl` 欄逐字「**未捨入之 `G` 與 `area_geom` 之 `float.hex`**」，同節之取法逐字令取 `res['G']`／`res['area_geom']`；
而 `app.py`（blob `4379108a4856714078c410ff4e6291ecfdf6d2c1`）`solve_G_binary` 之 `return` 逐字 `'G': round(G_conv, 2)`、`'area_geom': round(area_conv, 2)`，`_solve_G_one` 之 fallback 路徑逐字 `_r['area_geom'] = round(_r.get('S', 0) * avg_depth, 2)`——未捨入者僅 `S_raw`／`W_far_raw`／`Rw_raw`／`W_rw_start_raw` 四鍵。
該款係該單第二版起所擬；第三、四版重擬時沿用、未查。**同一單之工項一即鑄 `自誤 418`，其攔法 ① 逐字「施工單凡指名一物件之欄或屬性，出單前自 blob 實查其建構式（型別、是否持未捨入值、是否持幾何物件）」**。

**徵候**：CC 於 `W-G.9-308R` `§六-2` 依 `常規二` 取保守項、將欄名改記為 `G_回傳時_float_hex`／`area_geom_回傳時_float_hex` 並逐字回報（該報告 `§十一` 自捕 `3`）。

**根因**：立戒與施戒同批——出單前之自檢以新鑄之攔法為「今後之受詞」，**未以之回掃立戒之文件自身**；且重擬之版次以「前版已查」充該款之查。

**後果**：修批改後對拍之改前側，其面積仍僅有二位捨入之值（幾何以座標串指紋 `float.hex` 保全、`S` 以 `S_raw` 保全）；`W-G.9-308` 單所期「未捨入面積之基線」⛔ 成就。未致錯裁、未動土地。

**攔法（三款）**：
① 凡單內鑄一攔法者，出單前以該攔法逐款回掃本單全文，並於單內出艙回掃之結果（逐款具名受詞與判）；
② 單所載之欄名或受詞含「未捨入」「全精度」「原值」等性質詞者，同格逐字引其建構式之 `return` 列並載該檔之 blob；
③ 重擬之版次，對前版未改之款一律重跑全部攔法，⛔ 以「前版已查」充之。

<!-- ZW420-END -->

<!-- ZW421-BEGIN -->

### 🩸 `自誤 421`　**交接文載「`K-9-39` 可鑄」，未以受詞（調配池之落位次序）全倉查既有正典，致與 KL `2026-07-23` 裁定 B5 之牴觸未具名**

**形**：發單側交接文（`claude.ai` 側換手·九·`2026-09-17`·⛔ 在倉）第四節載「`K-9-39` 可鑄」（第 `1` 筆最左、第 `2` 筆最右，其後左、右交替），第五節列鑄 `K-9-38`、`K-9-39`；
而 `docs/specs/W-G.4_KL域裁_兩階段落位_部分面積拆分_Rw側選.md` 之裁定 B5 逐字（去其換行而引·引文內之 `→` 係原文之符號、⛔ 方向性轉引）「起始側：比較池範圍與兩側 **18m Rw 範圍**之**跨占寬度**，先從跨占大之一側配第1筆；**每配一筆後池縮小、重算兩側跨占**，下一筆從當時跨占大之一側；兩側皆無跨占 → 任一側往內。」與之**同受詞相牴**；
`app.py` `_place_pool_parcels` 之 docstring 載 B5 之實作；且 `K-9-35` 射程 ④ 逐字「裁定B、D、K ⛔ 變」、`K-9-37` 射程 ③ 逐字（去其粗體標記）「⛔ 及於調配池之面積、其調配之次序與拆分」。

**徵候**：新窗依交接文之開場序列復驗後、擬單前，全倉查得 `5` 列 `4` 檔（框 ＝ 正則 `(裁定\s*B\s*5|裁定B[^\n]{0,6}B5|跨占大之一側|跨占大的一側|起始側)` 之逐列子字串框；母體 ＝ HEAD 之追蹤 `.md`／`.py` `1197` 檔·態 `bc15a55`；二數並報：子字串框 `5` 列 `4` 檔／列首錨框 `^\s*` ＋ 同式 `0` 列）而現；呈 KL 後，KL `2026-09-17` 裁以「最左、最右、左、右…」取代 B5（`K-9-39`）。

**根因**：確認題之擬製只對照 KL 同段之語之**內部一致**（答 `2` 之「第2筆土地（從調配池最左側）」與「最左,最右,左,右」互斥），**未以受詞為鍵全倉查既有之裁**——以 KL 之語之內部自洽充正典之完備；且未讀既有射程款中「⛔ 變」之列。

**後果**：未致錯鑄（新窗於鑄前攔下並呈 KL）；若照交接文鑄入，`K-6` 與 `W-G.4` 域裁檔將並存二則相牴之落位次序，且 `app.py` 之自註將與正典不一致而無具名。

**攔法（三款）**：
① 凡擬鑄 `K-9` 之裁，出單前以其受詞之關鍵語（次序／起始側／跨占／拆分／門檻等）及其同義詞全倉查 `docs/` 與生產碼之既有裁定與自註，查得者同格具名其與新裁之關係（取代／併存／例外）；
② 交接文或單所載之「可鑄」，須併載該查之產生指令、母體與命中數；
③ 既有裁之射程款載「⛔ 變」某裁者，新裁若牴觸該裁，一律呈 KL 取代與否，⛔ 逕鑄。

<!-- ZW421-END -->

**落地後之機驗**：以器本身量 ⇒ 自誤 相異 **`411`**／MAX **`421`**（缺號 `[106, 355, 356, 357]`）；`420`／`421` 各命中 `1`（C 形）；`GB`／`VR`／`K-9` 一字未動；哨兵 `ZW420`／`ZW421` 入簿命中 `0`；append-only：期末 bytes 之前綴 ＝ 期初 bytes。

---

## `§四`　工項二：**`K-9-38`／`K-9-39` 之鑄 ＋ 裁定 B5 之末端註記**（主線·⛔ 上文一字不刪·🛑 **`§三` 入倉後方得辦**·**二段分列 `commit`**）

### 四-1　段甲：`docs/rulings/K-6_街角地分配程序與可分配判準.md` 檔末追加（界 ＝ `<!-- K9917B-BEGIN -->`／`<!-- K9917B-END -->`）

🔒 `K-9` 框之受詞（器取 `^#{2,4} ` 起首之列內之 `K-9-N`）：本 payload 內以 `#` 起首之列 ＝ **`2`**，各含且僅含 `K-9-38`／`K-9-39` 之一。
🛑 KL 之語**逐字**（含全形半形、引號、標點、空白）；⛔ 改一字。payload 之定義與追加之式同 `§三`。

<!-- K9917B-BEGIN -->

---

### 🔒 `K-9-38`　**末端塊之強制抵費地作調配池時：需調配之土地以同歸戶合計為單位、得拆分進入，自最大者開始；拆分後剩餘之面積得再進入調配池、再配 `1` 筆合格之土地**（KL 裁 `2026-09-17`·`W-G.9-308_補令一`）

**緣由**：`K-9-36` 射程 ③ 載「調配進入 `R_end` 範圍之土地，其面積與 `area(R_end)` 不等時之處理 ⛔ 獲逐字」；發單側於 `W-G.9-308` 第四版交付時列為暫不呈之項。KL 於 `W-G.9-308` 施工窗回復時逕答（同一訊息之第 `1` 點；第 `2` 點見 `K-9-39`）。
**KL 之語（逐字·第 `1` 點）**：「1. "調配進入 R_end 之土地面積與 R_end 不等時，如何處理"，所以需調配的土地（以同歸戶合計），可以拆分進入調配，這種末端塊R_end的調配，就先從需調配的土地最大者開始(以同歸戶合計為單位)，這樣拆分以後剩餘的土地面積還有機會可以進入調配池再配到1筆合格的土地。」

**裁之內容**：
① 需調配之土地進入末端塊之強制抵費地（`R_end` 範圍·其作調配池見 `K-9-36 ④`）時，**以同歸戶合計為單位**；
② **自需調配之土地（同歸戶合計）最大者開始**；
③ 需調配之土地**得拆分**進入——拆分者為**進入之土地**；`R_end` 本身**⛔ 拆分**（`K-9-36 ⑤` 全效）；
④ 拆分後**剩餘之面積**，得再進入調配池、再配 `1` 筆合格之土地。

**與既有正典之關係**：`K-9-36` 射程 ③ 所列二情形中，「大於者之超出部分」自本裁起獲答（③④）；「小於者之去處」（最大者仍未達 `area(R_end)`）**⛔ 獲逐字**。
③ 與 KL `2026-07-23` 裁定A「可拆分」同旨；④ 所稱「合格」之判準依既有之裁（`K-9-33`、`K-9-35`）——發單側之讀法（⛔ 充裁）。

**射程**：① 及於**任一案件**；
② 最大者仍未達 `area(R_end)` 時之處理 **⛔ 獲逐字** ⇒ **⛔ 據本裁推**，候調配之實作前附圖另呈；
③ ② 之「自最大者開始」與裁定 D（類別優先、同類別內距離優先）、裁定 K（距離優先）之先後 **⛔ 獲逐字** ⇒ **⛔ 據本裁推**，候另呈；
④ `K-9-35 ④`（任一不能容納內接矩形者⛔ 拆、整筆改往下一街廓）之於本裁之拆分 **⛔ 獲逐字** ⇒ **⛔ 據本裁推**。

**落地狀態**：⬜ **未實作**；七級調配於現行驗證程式內未被執行（`verify/run_verification.py` 之自註「`wf/f0~f4` 之 gate 因 F.0 raise 而**從未執行**」）。

🛑 **⛔ 據本裁推**：⛔ 推調配之實作形、⛔ 推任何末端塊或調配池之面積。

### 🔒 `K-9-39`　**調配池之落位次序 ＝ 最左、最右、左、右…，取代 KL `2026-07-23` 裁定 B5；臨街角第 `1` 宗之端之首筆須符合藍影機制與臨正街寬度 `≥` 畸零地寬，臨末端塊之端者⛔ 設藍影、仍驗內接矩形**（KL 裁 `2026-09-17`·`W-G.9-308_補令一`）

**緣由**：同 `K-9-38`（同一訊息之第 `2` 點）；其後發單側呈確認題一則並述第 `3` 筆起之形；新窗查得與裁定 B5 相牴而再呈一題（`自誤 421`），並將他形之調配池列為候呈之題，KL 逕答。
**KL 之語（逐字·第 `2` 點）**：「2. "兩側界線不平行之調配池（如 R4 ），調配後剩餘之土地是否另驗臨正街寬度"，這裡延伸一個問題，R4街廓這種僅有左右2側街角地的街廓，若進入調配階段，此時進來調配池的第1個土地，因其近側境界線為平行SIDELINE方向，而調配土地遠側境界線為ALLOCLINE方向，所以為了地籍線不交叉，第1 筆進來調配的土地(例如從調配池最左側開始)，需要藍影機制+S>=畸零地寬 驗收機制。若調配進來的第2筆土地（從調配池最左側），因也會有2側境界線交叉問題，所以也要有 藍影機制+S>=畸零地寬 驗收機制。調配池的分配方式為"最左,最右,左,右,左,右..."的方式辦理調配。」
**發單側所呈之確認題一（逐字·附平面圖）**：【要你判斷】「第 2 筆調配進入之土地是從調配池最右側進入？（是／否）」（去其粗體標記而引）
**KL 之答（逐字）**：「域裁：是，從調配池最右側，但前提是第1筆調配進入調配池的是從最左側，意思就是，調配進調配池的前2筆土地都要先把調配池最左、最右側會有第及交叉問題的位置，調配後的土地要能符合 藍影+畸零地寬的資格」
**發單側之述（逐字·節錄）**：「第 3 筆起兩側界線皆沿分配方向，應不再有交叉問題。」
**KL 之答（逐字）**：「第 3 筆起兩側界線皆沿分配方向，應不再有交叉問題。確認」
**發單側所呈之題（逐字·附平面圖·新窗）**：【要你判斷】「左右兩端皆為街角第 1 宗之街廓，其調配池之落位次序，以 9/17 所答「最左、最右、左、右…」取代 7/23 裁定 B5（兩側 18 公尺範圍跨占寬度大者先配）？（是／否）」（去其粗體標記而引）；同訊之通知（逐字）：「通知（非題）：一端為末端塊或無街角之調配池，本題不及之，仍依 B5。此係發單側之讀法，不充裁。」
**KL 之答（逐字）**：「1. 域裁：是，以今天9/17日裁示的 「最左、最右、左、右…」取代 7/23 裁定 B5。原理如下，之後入調配池的土地若是在W=18m範圍內，依據G值公式該調配進來的土地仍要作臨側街負擔Rw計算。所以由最左,最右,左,右的程序同理也是吃到Rw負擔的最佳解，因為這樣的調配順序，會讓不計算負擔的"配餘地"(或稱"抵費地",或稱"剩餘的調配池")，能盡量在街廓中間不在街廓左右側18M的範圍內。」
**發單側之候呈題（逐字·未附圖）**：「他形調配池：一端為末端塊或無街角之調配池，是否也改依「最左、最右、左、右…」？」（去其粗體標記而引）
**KL 之答（逐字）**：「有關"一端為末端塊，或無街角者"的他行調配池部分，因為也是採"最左,最右,左,右..."的調配順序方式，只是值得提醒一下，末端塊的遠側境界線（定義：所謂的"遠側"境界線是指街廓左右側各自往街廓中間分配方向而與夏禕宗分配土地的相鄰(共用)的地界線，例如街廓最左側往街廓中間分配，該宗土地本身遠側境界線指的就是本宗土地右側的那條境界線，與下1宗土地相鄰共用的地界線；最右側也是一樣的邏輯），因末端塊的遠側境界線係平行ALLOCLINE方向，所以末端塊後1宗需調配的土地，不會有地籍交叉問題，就無需要藍影機制，但是仍要有內接矩形驗收。」
（「夏禕宗」依同句下文「與下1宗土地相鄰共用的地界線」讀為「下1宗」；「他行」讀為「他形」·⛔ 改原文一字。）

**裁之內容**：
① **適用**：任一調配池——左右二端皆為街角第 `1` 宗者（`K-9-37`）、一端為街角第 `1` 宗而他端為末端塊者、二端皆為末端塊者（`K-9-31`：無側街之端稱末端塊）；
② **落位次序**：調配進入之第 `1` 筆落於調配池**最左**、第 `2` 筆落於**最右**，其後依**左、右、左、右…**交替；
③ **遠側境界線之義**（KL 逐字定義）：街廓左右側各自往街廓中間分配時，本宗土地與下 `1` 宗土地相鄰（共用）之地界線——自最左側往中間分配者為本宗之右側界線，自最右側者同理；
④ **臨街角第 `1` 宗之端**：該端之首筆調配進入之土地，其近側界線平行該側 SIDELINE、遠側界線沿 ALLOCLINE 方向，二界不平行 ⇒ 須符合**藍影機制**與**臨正街寬度 `S ≥` 畸零地寬**之資格；二端皆為街角第 `1` 宗者，即第 `1`、`2` 筆；
⑤ **臨末端塊之端**：末端塊之遠側境界線平行 ALLOCLINE 方向 ⇒ 末端塊後 `1` 宗需調配之土地無地籍交叉 ⇒ **⛔ 設藍影機制**，**仍驗內接矩形**；
⑥ **其餘各筆**（兩側界線皆沿分配方向）：**⛔ 設藍影機制**（依 KL 之確認「第 3 筆起兩側界線皆沿分配方向，應不再有交叉問題。確認」與答 `2` 所載藍影之設置理由「為了地籍線不交叉」；發單側已以此告 KL）；其內接矩形與 `S` 之驗依 `K-9-33`／`K-9-35`；
⑦ **取代裁定 B5**：B5 之「起始側」與「下一筆從當時跨占大之一側」自本裁起於任一調配池**⛔ 適用**；
⑧ **KL 之理由**：調配進入之土地落於側街 `18 m`（`W = 18 m`）範圍內者仍依 G 值公式計臨側街負擔 `Rw`；此序使**不計負擔之配餘地**（剩餘之調配池）儘量居街廓中間、不在左右側 `18 m` 範圍內。

**發單側之讀法（⛔ 充裁）**：一端為街角第 `1` 宗而他端為末端塊者，其臨街角第 `1` 宗之端依 ④——KL 本答以「只是值得提醒一下」僅就末端塊之端另載 ⑤，⛔ 另及街角之端。

**與既有正典之關係**：裁定 F（池內負擔：有跨占者依 G 公式以 Rw 比率計算）**⛔ 變**，且為理由 ⑧ 之前提；裁定 A、B1〜B4 **⛔ 變**。
⑤ 與 `K-9-37 ②`（臨末端塊之側沿 ALLOCLINE 方向）一致；③ 之義與倉內既有「遠側境界線」之用法同旨（例：`docs/orders/W-G.9-189_施工單_幾何本體批第二批.md` 逐字「遞補宗之遠側境界線 ＝ 自**前一宗（第 `0` 宗或前一已定宗）之遠側境界線**起」）。
`app.py` `_place_pool_parcels` 之 docstring 逐字（去其粗體標記·引文內之 `→` 係原文之符號、⛔ 方向性轉引）「跨占大之側先配；相等或兩側皆 0 → tie-break：池 s-區間較長之側；再同→左」係 B5 之實作（生產碼·⛔ 改一字·見落地狀態）。

**射程**：① 及於**任一案件**之**任一形**調配池；
② 首筆資格不合格時之處理（遞補、改往下一街廓或其他）**⛔ 獲逐字** ⇒ **⛔ 據本裁推**；
③ 調配後剩餘之土地是否另驗 `S`（`K-9-35` 射程 ⑤）**仍⛔ 獲逐字**——KL 答 `2` 係延伸至進入之土地，未逐字答原問；
④ 末端塊之強制抵費地作調配池者（`K-9-36 ④`、`K-9-38`），其 `R_end` 範圍與本裁之落位次序之關係 **⛔ 獲逐字** ⇒ **⛔ 據本裁推**。

**落地狀態**：⬜ **未實作**——`app.py` `_place_pool_parcels` 現依 B5（碼面自註·未經實跑）；七級調配於現行驗證程式內未被執行。

🛑 **⛔ 據本裁推**：⛔ 推調配之實作形、⛔ 推任何調配池之面積、⛔ 推首筆不合格之處理、⛔ 推 `K-9-29` 之碼側落地與 `W-G.9-309` 之先後。

<!-- K9917B-END -->

**段甲落地後之機驗**：器 ⇒ `K-9` 相異 **`38`**／MAX **`39`**／缺號 `[]`；反向機驗：`K-6` 內 `^#{2,4} ` 起首且含 `K-9-38` 之列 ＝ `1`、含 `K-9-39` 之列 ＝ `1`（整列框與子字串框二數並報）；哨兵 `K9917B` 入簿命中 `0`；append-only：期末 bytes 之前綴 ＝ 期初 bytes。

### 四-2　段乙：`docs/specs/W-G.4_KL域裁_兩階段落位_部分面積拆分_Rw側選.md` 檔末追加（界 ＝ `<!-- B5N-BEGIN -->`／`<!-- B5N-END -->`）

🛑 payload 內**⛔ 任何以 `#` 起首之列**；payload 之定義與追加之式同 `§三`。

<!-- B5N-BEGIN -->

---

**🔧 裁定 B5 之末端註記**（`W-G.9-308_補令一`·⛔ 改本檔上文一字）

> 調配池之落位次序，自 KL `2026-09-17` 之裁起依 `docs/rulings/K-6_街角地分配程序與可分配判準.md` 所載 `K-9-39`（最左、最右、左、右…；臨街角第 `1` 宗之端之首筆須符合藍影機制與臨正街寬度 `≥` 畸零地寬；臨末端塊之端者⛔ 設藍影、仍驗內接矩形）——**B5 於任一形之調配池⛔ 適用**。
> KL 之答逐字（節錄·全文見 `K-9-39`）：「1. 域裁：是，以今天9/17日裁示的 「最左、最右、左、右…」取代 7/23 裁定 B5。」「有關"一端為末端塊，或無街角者"的他行調配池部分，因為也是採"最左,最右,左,右..."的調配順序方式」
> 裁定 A、B1〜B4、C〜J ⛔ 變。

<!-- B5N-END -->

**段乙落地後之機驗**：`B5N` 哨兵入檔命中 `0`；檔內以 `#` 起首之列數期末 ＝ 期初；append-only：期末 bytes 之前綴 ＝ 期初 bytes。

---

## `§五`　工項三：**宣告框補款 `⑨`**（`CLAUDE.md` 檔末追加·界 ＝ `<!-- DECL9-BEGIN -->`／`<!-- DECL9-END -->`·單獨 `commit`）

🛑 payload 之定義與追加之式同 `§三`。

<!-- DECL9-BEGIN -->

---

## 🔧 宣告框補款 `⑨`：**`D2` 之他指引用之排除**（`W-G.9-308_補令一` 工項三·發單側之裁·⛔ 上文一字不刪·純末端追加）

🛑 **本節⛔ 鑄任何號**——其為補款（`戒 36`）。
🩸 **案由**　`W-G.9-308R` `§零` 自解 `1`：`W-G.9-308` 之 `D2` ＝ `2` 列，二列皆為**前一批（`W-G.9-307` 單與其報告）之標題列對本號之前瞻引用**；補款 `⑤` 已為 `D3` 設他指之邊界，`D2` 則無 ⇒ **被前瞻引用之號構造上過不了自己的閘**（與「號占用閘之框改宣告框」節末所具名之「作廢單」缺陷同根）。

🔒 **補款（自本節起為正字規則）**

> **⑨　`D2` 標題形之他指排除**
> `D2`（列首為 `#+` 之列含該號）**僅於該列所在檔之檔名所載之單號 ＝ 該號時成立**；
> 所在檔之檔名載他號或⛔ 載任何單號者 ⇒ 該列屬**他指**（引用／前瞻／委派）⇒ 依 `②` **⛔ 構成占用**。
> 🔒 **理由**：施工單依 `作業常規之追加四：` 以其號為檔名原封入倉、報告以其號為檔名前綴 ⇒ 真占用者**必具 `D1`**；他檔之標題列含該號者必屬他指。
> 🔒 `D1`／`D3`／`②`／`③`／`④`／`⑤`／`⑥`／`⑦`／`⑧` **一字未動**；出艙之形仍依 `⑥`（三數分列），並**同格加載「依 `⑨` 排除之 `D2` 列數」**。
> 🔒 **⛔ 追改任何既出之取號結論**（`常規四（九）五`）——本款只約束**今後**。

🔒 **首次施行之實測**（發單側·判法 ＝ `①` 之三形帶數字邊界·母體 ＝ 各態之全 `docs/`）：
`W-G.9-308` @ `aa1394c`（`806` 檔）⇒ `D1` `0`／`D2` `2`／`D3` `0`；二列所在檔之檔名之號皆 ＝ `W-G.9-307` ⇒ 依 `⑨` 排除 `2` ⇒ **未占用**（與 `W-G.9-308R` 自解 `1` 讀法乙同結論）。
判別力[必非零]：`W-G.9-307` @ `bc15a55`（`808` 檔）⇒ `D1` `5` ⇒ **占用**（`⑨` ⛔ 及於 `D1`）。

---

<!-- DECL9-END -->

**落地後之機驗**：CC 以既有之宣告框量法（`W-G.9-308R` `§零` 自解 `1` 所用者）重得上開二造之三數與依 `⑨` 排除之 `D2` 列數並出艙（態分別釘死）；不符 ⇒ loud 具名、停該款；哨兵 `DECL9` 入檔命中 `0`；append-only 同 `§三`。

---

## `§六`　工項四：**款 `4` 之靜態結案**（主線·**零生產碼**·**⛔ `run_verification`**）

🔑 **明文授權**：新增 `verify/probes/probe_WG9308S1_bindorder.py`（**逐位元組取自本節 payload**·⛔ 改一字）並跑一次；落檔 `verify/out/WG9308S1_bindorder.log`（器自寫·`open(p,'wb')`）；二檔入倉（**逐檔 `git add`**·單一 `commit`）。
🔒 **payload 之取法**：界 `<!-- PRB-BEGIN -->`／`<!-- PRB-END -->` 內之列去其首尾之空列後，**再去其首列（`` ```python ``）與末列（`` ``` ``）**；落檔 ＝ `b'\n'.join(列) + b'\n'`（取 bytes·`open(p,'wb')`）。
🔒 **整全性**：落檔之 `sha256` 須 ＝ **`0b986201ea878719e5b31680cd1da38226842a0b982b15a375ac45bd133927cf`**·`10100` B·`CR` `0`；不符 ⇒ **停**、⛔ 跑。
🛑 **取法須以 Python 讀本單檔之 bytes 為之**；⛔ 以 shell 之 `echo`／`cat <<` 轉寫（坑 `bp`）。
🛑 **跑法**：`python verify/probes/probe_WG9308S1_bindorder.py <rev>`，`rev` ＝ 跑時之 `HEAD`（＝ 工項三之 `commit`·全 `40` 碼·**跑於本節入倉之前**·落檔隨同入倉）。

<!-- PRB-BEGIN -->

```python
# -*- coding: utf-8 -*-
"""W-G.9-308 補令一 工項四：強制呼叫與側界名之綁定次序之靜態全證（零生產碼·零 harness）。

受詞：生產碼 34 檔（HEAD 之 verify/ 頂層 *.py 與 app.py·正面列舉）內，
      對 _corner_buffer_S 之每一呼叫（語法形二：Name 形 與 ns 下標形）。
對每一呼叫，取其最內層之迴圈（For／While·同一函式內），於該迴圈體內：
  (一) 名集 N7 之七名，各出艙其迴圈體內首次 Store 之列、及首次 Store 之前之 Load（含巢狀定義內）；
  (二) 通則：迴圈體內「首次 Store 在呼叫列之後、而於呼叫列（含）之前有 Load」之名 ⇒ 期 0；
  (三) 該呼叫之引數所含之 Name，其迴圈體內首次 Store 在呼叫列之後者 ⇒ 期 0。
判別力二造（執行期組出之來源字串·不落檔）：[必命中] 讀前於綁 ⇒ (二) >= 1；[必為零] 綁前於讀 ⇒ (二) = 0。
用法：python verify/probes/probe_WG9308S1_bindorder.py <rev>
落檔：verify/out/WG9308S1_bindorder.log（open(p,'wb')·utf-8·LF）。
"""
import ast
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out", "WG9308S1_bindorder.log")
TARGET = "_corner_buffer_S"
N7 = ("_side_lines_blk", "_sl_left", "_sl_right", "_side_mid_left",
      "_side_mid_right", "_has_left_corner", "_has_right_corner")
LINES = []


def emit(s=""):
    LINES.append(s)


def git_bytes(*args):
    r = subprocess.run(["git", "-C", REPO] + list(args), capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("git %r rc=%d %r" % (args, r.returncode, r.stderr[:200]))
    return r.stdout


def population(rev):
    raw = git_bytes("ls-tree", "--name-only", "-z", rev, "verify/")
    names = [x.decode("utf-8") for x in raw.split(b"\0") if x]
    top = sorted(n for n in names if n.endswith(".py") and n.count("/") == 1)
    raw2 = git_bytes("ls-tree", "-r", "--name-only", "-z", rev, "verify/")
    sub = [x for x in raw2.split(b"\0") if x and x.endswith(b".py") and x.count(b"/") >= 2]
    return top + ["app.py"], len(sub)


def is_target_call(node):
    if not isinstance(node, ast.Call):
        return None
    f = node.func
    if isinstance(f, ast.Name) and f.id == TARGET:
        return "Name"
    if isinstance(f, ast.Subscript):
        sl = f.slice
        if isinstance(sl, ast.Constant) and sl.value == TARGET:
            return "Subscript"
    return None


def parents_map(tree):
    par = {}
    for p in ast.walk(tree):
        for c in ast.iter_child_nodes(p):
            par[c] = p
    return par


def innermost_loop(node, par):
    cur = par.get(node)
    while cur is not None:
        if isinstance(cur, (ast.For, ast.AsyncFor, ast.While)):
            return cur
        if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            return None
        cur = par.get(cur)
    return None


def _target_names(t):
    return [m.id for m in ast.walk(t) if isinstance(m, ast.Name)]


def body_events(loop):
    """迴圈體之 Name 事件。🔒 語義：迴圈目標之名視為於迴圈列 Store；
    推導式（List/Set/Dict/GeneratorExp）之目標名屬其自身作用域 ⇒ 其 Store 與對之 Load 皆⛔ 計；
    巢狀 def／lambda／class 內之 Store 屬其自身作用域 ⇒ ⛔ 計，其 Load 保守計入。"""
    ev = []
    if isinstance(loop, (ast.For, ast.AsyncFor)):
        for nm in _target_names(loop.target):
            ev.append((loop.lineno, -1, "Store", nm))

    def visit(node, comp_bound, nested):
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
            bound = set(comp_bound)
            for g in node.generators:
                visit(g.iter, bound, nested)
                bound |= set(_target_names(g.target))
                for cond in g.ifs:
                    visit(cond, bound, nested)
            elts = [node.key, node.value] if isinstance(node, ast.DictComp) else [node.elt]
            for e in elts:
                visit(e, bound, nested)
            return
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            for c in ast.iter_child_nodes(node):
                visit(c, comp_bound, True)
            return
        if isinstance(node, ast.Name):
            if node.id in comp_bound:
                return
            k = type(node.ctx).__name__
            if k == "Store" and nested:
                return
            ev.append((node.lineno, node.col_offset, k, node.id))
            return
        for c in ast.iter_child_nodes(node):
            visit(c, comp_bound, nested)

    for stmt in loop.body + loop.orelse:
        visit(stmt, frozenset(), False)
    ev.sort()
    return ev


def analyse(src, fname):
    tree = ast.parse(src)
    par = parents_map(tree)
    rows = []
    for n in ast.walk(tree):
        form = is_target_call(n)
        if not form:
            continue
        loop = innermost_loop(n, par)
        row = {"file": fname, "line": n.lineno, "form": form,
               "loop": None, "n7": {}, "general": [], "args_stale": []}
        if loop is None:
            rows.append(row)
            continue
        row["loop"] = (type(loop).__name__, loop.lineno, loop.end_lineno)
        ev = body_events(loop)
        first_store = {}
        for ln, col, k, nm in ev:
            if k == "Store" and nm not in first_store:
                first_store[nm] = ln
        for nm in N7:
            fs = first_store.get(nm)
            early = [ln for ln, col, k, x in ev if x == nm and k == "Load" and (fs is None or ln < fs)]
            row["n7"][nm] = (fs, early)
        cl = n.lineno
        gen = set()
        for ln, col, k, nm in ev:
            fs = first_store.get(nm)
            if k == "Load" and fs is not None and fs > cl and ln <= cl:
                gen.add(nm)
        row["general"] = sorted(gen)
        argnames = set()
        for a in list(n.args) + [kw.value for kw in n.keywords]:
            for m in ast.walk(a):
                if isinstance(m, ast.Name):
                    argnames.add(m.id)
        row["args_stale"] = sorted(x for x in argnames
                                   if first_store.get(x) is not None and first_store[x] > cl)
        rows.append(row)
    return rows


def selftest():
    q = chr(39)
    hit = "\n".join([
        "def f(ns, blocks):",
        "    for b in blocks:",
        "        x = _side_mid_left",
        "        _corner_buffer_S(b, x)",
        "        _side_mid_left = ns.get(" + q + "m" + q + ")",
    ])
    zero = "\n".join([
        "def f(ns, blocks):",
        "    for b in blocks:",
        "        _side_mid_left = ns.get(" + q + "m" + q + ")",
        "        _corner_buffer_S(b, _side_mid_left)",
    ])
    zero2 = "\n".join([
        "def f(ns, blocks):",
        "    for b, c in blocks:",
        "        y = c + 1",
        "        _corner_buffer_S(b, y)",
        "        z = [c for c in range(3)]",
    ])
    rz2 = analyse(zero2, "<selftest-zero2>")
    rh = analyse(hit, "<selftest-hit>")
    rz = analyse(zero, "<selftest-zero>")
    gh = sum(len(r["general"]) for r in rh)
    gz = sum(len(r["general"]) for r in rz)
    gz += sum(len(r["general"]) for r in rz2)
    return gh, gz, len(rh), len(rz) + len(rz2)


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    full = git_bytes("rev-parse", rev).decode().strip()
    emit("=" * 100)
    emit("【W-G.9-308 補令一 工項四】強制呼叫與側界名之綁定次序（靜態·rev=%s）" % full)
    emit("=" * 100)
    gh, gz, nh, nz = selftest()
    emit("判別力二造：[必命中] 通則命中 %d（呼叫數 %d）｜[必為零] 通則命中 %d（呼叫數 %d）" % (gh, nh, gz, nz))
    ok_self = (gh >= 1 and gz == 0 and nh == 1 and nz == 2)
    emit("⇒ 器 %s" % ("非紅 ✅" if ok_self else "紅 🔴（停）"))
    files, subcount = population(full)
    emit("母體：生產碼 %d 檔（verify/ 頂層 *.py %d ＋ app.py）｜判別力[必不命中] 子層 *.py = %d"
         % (len(files), len(files) - 1, subcount))
    allrows = []
    for fn in files:
        src = git_bytes("show", "%s:%s" % (full, fn)).decode("utf-8")
        allrows.extend(analyse(src, fn))
    emit("呼叫總數 = %d（Name 形 %d／Subscript 形 %d）" % (
        len(allrows), sum(r["form"] == "Name" for r in allrows),
        sum(r["form"] == "Subscript" for r in allrows)))
    emit("")
    emit("| # | 檔:列 | 形 | 最內層迴圈 | 通則命中 | 引數含後綁之名 |")
    emit("|---|---|---|---|---|---|")
    for i, r in enumerate(allrows, 1):
        emit("| %d | %s:%d | %s | %s | %s | %s |" % (
            i, r["file"], r["line"], r["form"],
            ("%s %d-%d" % r["loop"]) if r["loop"] else "無",
            r["general"] or "[]", r["args_stale"] or "[]"))
    emit("")
    emit("名集 N7 之逐呼叫明細（首次 Store 列／首次 Store 前之 Load 列）")
    for i, r in enumerate(allrows, 1):
        if not r["loop"]:
            continue
        emit("  #%d %s:%d" % (i, r["file"], r["line"]))
        for nm in N7:
            fs, early = r["n7"][nm]
            emit("     %-20s Store@%s  前置Load=%s" % (nm, fs, early))
    gen_total = sum(len(r["general"]) for r in allrows)
    stale_total = sum(len(r["args_stale"]) for r in allrows)
    early_total = sum(len(r["n7"][nm][1]) for r in allrows if r["loop"] for nm in N7)
    emit("")
    emit("彙總：通則命中合計 = %d｜引數含後綁之名合計 = %d｜N7 首次 Store 前之 Load 合計 = %d"
         % (gen_total, stale_total, early_total))
    red = (not ok_self) or subcount <= 0 or len(allrows) == 0
    emit("器紅 = %s" % red)
    data = ("\n".join(LINES) + "\n").encode("utf-8")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as fh:
        fh.write(data)
    sys.stdout.buffer.write(data)
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
```

<!-- PRB-END -->

**期值（發單側於 `bc15a55` 實跑·CC 須自行重跑·主線有後裔者以實得為準並具名差異之 `commit`）**：

| 款 | 受詞（器之出艙列） | 期 |
|---|---|---|
| `1` | 判別力二造 | [必命中] 通則命中 `1`（呼叫數 `1`）／[必為零] 通則命中 `0`（呼叫數 `2`）⇒ 器非紅 |
| `2` | 母體 | 生產碼 `34` 檔（頂層 `33` ＋ `app.py`）；子層 `*.py` `329`（`> 0` 即可） |
| `3` | 呼叫總數 | `7`（`Name` 形 `4`／`Subscript` 形 `3`）：`verify/stepg_pipeline.py:659`／`:670`、`verify/wf_f1.py:216`、`verify/wf_f4.py:1351`／`:1362`、`app.py:21903`／`:21914` |
| `4` | 彙總 | 通則命中合計 `0`｜引數含後綁之名合計 `0`｜N7 首次 Store 前之 Load 合計 `0` |
| `5` | 器紅 | `False`（`rc = 0`） |

🛑 **停機款**：款 `1` 紅或款 `4` 任一 `≠ 0` ⇒ **停、⛔ 入倉、上呈**（照實全量出艙·⛔ 判改法）；款 `3` 與期相異而款 `4` 皆 `0` ⇒ 照實具名、續辦。
🔒 **結案之判屬發單側**（`§零-2` 裁 `2`）：本節綠 ⇒ `W-G.9-308` 款 `4` 以本節結案；**⛔ 再跑 `run_verification`**。

---

## `§七`　工項五：**`308R` 未入倉落檔之入倉**（單獨 `commit`）

受詞 ＝ `§一` 閘 `11` 所列六名中態為 `??` 者。**逐檔 `git add <路徑>`**（**⛔ `git add -A verify/out/`**·`CLAUDE.md` 逐字）；逐檔出艙 bytes／`sha256`／`CR` 數。
不存在者 ⇒ loud 具名、**⛔ 重生**（母體 ＝ `§一` 閘 `11` 之六名；其重生指令逐字已載 `W-G.9-308R` `§七-5`）。六名皆不存在 ⇒ 本工項照實具名「無受詞」、⛔ `commit`。

---

## `§八`　收工閘（**報告入倉後量**·嚴格末端追加·🛑 **落檔 `open(p,'wb')`**）

| # | 受詞（指令） | 期／判準 |
|---|---|---|
| `1` | `git show --numstat <各 commit>` 逐檔具名 | 刪除欄**全 `0`** |
| `2` | 生產碼判法·母體**正面列舉 `34` 檔** | blob 期初＝期末相異 `0`；`app.py` ＝ `4379108a…` |
| `3` | 本批異動之 `.md`／`.py`／`.log`／`.err` 之 `CR`（倉內 blob·取 bytes） | **`0`**；判別力[必非零] ＝ `data/V6.dxf` |
| `4` | 四簿期末（器之輸出） | 自誤 相異 **`411`**／MAX **`421`**（缺 `[106, 355, 356, 357]`）；`K-9` 相異 **`38`**／MAX **`39`**／缺號 `[]`；`GB` `168`／`170`·`VR` `80`／`95` 一字未動 |
| `5` | 坑之期末（器之輸出·`rev` 釘死·全量落檔） | **`94`／`94`**·末 **`bp`** |
| `6` | append-only（四受改檔） | 期末 bytes 之前綴 ＝ `§一` 閘 `9` 之期初 bytes（逐檔） |
| `7` | 自限復驗 | `baselines` `298`·`a898f4e1…`；`p3a` `rc = 1`；`refs/heads/verify/*` `20` 支·`gb170` `0`；`WV_BAKE` ＝ `None`；既有探針 `probe_WG9308R_lots.py`／`probe_WG9308R_sites2.py` 與物證落檔 `WG9308R_lots.log`／`WG9308R_lots_pre.jsonl`／`WG9308R_sites2.log` blob 期初＝期末 |
| `8` | 標籤對照（`自誤 416`） | 本報告全部計數標籤，逐欄具名其指涉之集合與基數（以程式自資料列計數） |
| `9` | `git ls-remote origin refs/heads/wip/s1-endpart`（`push` **後**） | 🔒 **出艙於回報·⛔ 入倉** |

---

## `§九`　🛑 **⛔ 為之事**

🔑 **本批已明文授權者**（射程逐字見 `§三`〜`§七` 首段·⛔ 逾之）：二則自誤之鑄；`K-9-38`／`K-9-39` 之鑄；`W-G.4` 域裁檔之 B5 末端註記；`CLAUDE.md` 之宣告框補款 `⑨`；新增 `probe_WG9308S1_bindorder.py` 及其落檔並跑一次；`308R` 未入倉之六檔之入倉。
其餘：⛔ 改生產碼 `34` 檔**一字**；⛔ `run_verification`；⛔ 開任何分支；⛔ 動用 KL 之放行；⛔ 辦修批；⛔ 自續或占用 `W-G.9-309`；⛔ 併線（含 `p3a`）；⛔ 刪任何 ref；
⛔ 覆寫 `verify/baselines` 任一檔或任一物證落檔；⛔ `WV_BAKE`；⛔ 動任何既有探針一字；⛔ 鑄 `GB`／`VR`／坑之任何號、⛔ 鑄 `K-9-38`／`K-9-39` 以外之 `K-9`；⛔ 解除或收窄任何 `GB`；⛔ 落地任何 `K-9` 子項；
⛔ 追改任何已入倉文件一字（含 `W-G.9-308` 單與 `308R` 報告）；⛔ 呈 KL；⛔ 判改法、⛔ 擬任何 diff；⛔ 於器紅或停機款成就時自擴規則、自調框或重跑；
⛔ 估算或出艙本窗 context 之百分比——惟遇可觀測之硬限事件一律 loud 照實具名、停、上呈；⛔ 以 shell 命令列傳遞含反引號之文字；
⛔ 於任何入倉文件宣稱一件尚未發生之事（及於 `commit` 訊息與「已推送」之陳述）。

---

## `§十`　報告之格

`docs/reports/W-G.9-308R2_補令一_K-9-38與K-9-39之鑄與款4之靜態結案_執行報告.md`（命名前例 ＝ `W-G.9-307R2_補令一_舊窗收工_執行報告.md`）：
`§二` 工項零 ⇒ `§一` 開工閘（逐閘出艙）⇒ `§三` 工項一（機驗）⇒ `§四` 工項二（段甲／段乙之機驗）⇒ `§五` 工項三（二造之三數）⇒ `§六` 工項四（器之出艙全文 ＋ 期值對照）⇒ `§七` 工項五 ⇒ 收工閘（入倉後末端追加·閘 `9` 出艙於回報）⇒ `⛔ 為之事` 之逐項自檢 ⇒ 逐 `commit`（全 `40` 碼）。
🔒 凡出艙之數，同格載其框、母體與產生指令，且該指令須逐字原樣執行過；計數標籤以程式自資料列計數。
🔒 自捕照實併記（⛔ 鑄號）；自捕為零者須併具「**⛔ 讀為『本批無誤』**」。
🔑 **發單側出單前之實跑**：`probe_order_preflight.py <本單>` ⇒ 🔴 `0`／🟡 `0`（`P-5` 相符）；器之 `K-9` 框於暫存副本模擬段甲落地 ⇒ `38`／`39`；自誤框模擬工項一落地 ⇒ `411`／`421`。

🛑 **辦畢 ⇒ 出報告 ⇒ 停。⛔ 呈 KL。**

---

【驗收】本批之驗收固定項（**⛔ 推後·⛔ 以「未觸」充綠**）：
`sys.version`／`ls-remote`／`SELF_SHA256`／`preflight`／`deletions`／`merge-base`／`ZW420`／`ZW421`／`K9917B-BEGIN`／`B5N-BEGIN`／`DECL9-BEGIN`／`PRB-BEGIN`／`K-9-38`／`K-9-39`／`裁定 B5`／`_place_pool_parcels`／`probe_WG9308S1_bindorder.py`／`WG9308S1_bindorder.log`／`_corner_buffer_S`／`_side_mid_left`／`solve_G_binary`／`round(G_conv, 2)`／`宣告框補款`／`WG9308R_pit_pre.log`／`遠側境界線`／`臨末端塊之端`／`bc15a55`。

【單止】本單受詞 ＝ CC 施工窗。發單側 ＝ `claude.ai`。**⛔ 呈 KL。**

SELF_SHA256: 50450afa9ad6a8a17f196e46ad90ebb861890fb2481953fa33e6798e8ecf4817
