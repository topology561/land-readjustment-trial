# `W-G.9-385R`　工項二　停機上呈（停機款 `12`·唯讀獨立審查之發現 #1、#2：`R-2` ③ 之公有持分於「權利範圍分子／分母」缺值時無定〔`NaN` ⇒ ⛔ 錯誤、尺度靜默成 `5.0`〕；地籍資料來源之讀取之例外〔分母 `0`、缺欄、檔之讀取失敗〕於步驟 H 無定〔未捕 ⇒ 畫面中止〕——規格之漏載）

> **受單** ＝ CC 窗（`2026-10-16`）。**來源檔** ＝ KL 主 checkout 之根（第二處·二進位複製·入倉後 `git cat-file blob` 與來源 `cmp` 同）；KL 之訊⛔ 載 bytes／`sha256`（唯貼檔之路徑）⇒ 以 `SELF_SHA256` 為據（`a6541193…41f20d2` 相符·`probe_order_preflight` 之 `P-5` 亦相符）。
> **本檔 ＝ 停機上呈**（`§五-2` 之 1）：工項二之碼**⛔ 推新側支**、存本地 `hold/W-G.9-385-c2`；工項三、四⛔ 辦。⛔ 自改、⛔ 自裁。
> context 餘量（開場自報）：約 `14.86M` tokens。

---

## 一、態

| 項 | 值 |
|---|---|
| 主線 `wip/s1-endpart` | `158f7fe959697571d8179988cd4c192c0016ead9`（⛔ 動） |
| 新側支 `verify/W-G.9-385-k974` | 工項零 `0fc214fe6ed847604ac04ec4ba7e87f6382281c6` → 工項一 `e6a22894d5197a4fe16dcbc2dfe5163468130908` → 本停機上呈之 `commit`（零生產碼） |
| 工項二之碼 | 本地 `hold/W-G.9-385-c2` ＝ `fb637350b8aa333519dc101091de58c57b2a4aca`（**⛔ push**）；`app.py` ＝ `e89fbe6215c2cab7285741d1235c77f531f19131`（`1839197` B·對工項一之端 `+357`／`-3`）；全文差異 ＝ 同目錄 `W-G.9-385R_工項二_app差異.diff`（`git diff e6a2289 fb63735 -- app.py`·`25029` B·CR `0`） |
| 遠端 heads | `45`（開工 `44` ＋ 新側支） |
| `<O>` | `C:\Users\admin\w385o`（倉外·非任何 git 工作樹·諸器之出艙皆存之）；前置於倉外之 worktree `C:\Users\admin\w385P`（`git worktree add --detach … e6a2289`·跑後 `git status --porcelain` 空） |
| 本機 | Windows 11·Python `3.13.11`·`20` 核 |

## 二、停機款（款·期·實）

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `158f7fe`·heads `44`·⛔ 含新側支·追蹤檔⛔ 變·開場之器 `rc 0` 與四簿之值·旗標 `[None×5]` | 皆符（追蹤檔 `2866`；自誤 `605`／`620`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`·`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`·`VR` `80`／`95`／`[73, 75]`·`K-9` `75`／`78`／`[44, 47]`；`<O>\heads_before.txt` `44` 列） |
| `2` | `SELF_SHA256`·入倉之 blob ＝ 來源 | 皆符（本單 `131051` B·全檔 `sha256` `886648e9…ceb45f9e1`·`1095` 列·CR `0`；`P-5` 口徑之受詞 `130973` B ⇒ `a6541193…41f20d2`） |
| `3` | 塊之 bytes／`sha256`／列數·`git apply --check`·四器之施後 blob | 皆符（`Fy35` `42206`／`971c7f3a…`／`657`；`K25` `14875`／`c59cedd2…`／`120`；`E28` `2050`／`a10594d9…`／`13`；`P38` `4601`／`4ab9a278…`／`27`；`CK` `1539`／`00cd3949…`／`31`；`GF` `2445`／`b11edb77…`／`47`；四器 ＝ `ccdb11f3…`／`d76cf9fe…`／`b1ad31f5…`／`c21b6676…`·`17`／`0`、`5`／`0`、`5`／`0`、`563`／`0`） |
| `4` | 工項二前置 `1`〜`4` | 皆符（下開三） |
| `5` | ⛔ 歧義而涉域上判斷 | 撰碼中⛔ 見 |
| `6` | `V-1`〜`V-9` | **皆符**（下開三） |
| `7` | 推之目標唯新側支·⛔ 被拒·主線⛔ 推進 | 皆符（工項零 `[new branch]`、工項一快轉，皆首推即成；主線仍 `158f7fe`） |
| `8`〜`9` | 工項三·收工閘 | 工項三、四⛔ 辦（停機） |
| `10` | CC ⛔ 自判 | ⛔ 自判（#1、#2 呈之） |
| `11` | 新檔⛔ 為 ignore 所命中 | 本單、新器、本檔二新檔之 `git check-ignore -v --no-index` 皆無命中 |
| `12` | 唯讀審查之發現涉域上判斷或規格之漏載 | **成就**——#1、#2（下開四） |

## 三、前置與驗之結果（全出艙存 `<O>\pre\`、`<O>\post\`·`NN.out`／`NN.err` ＝ 下表之 `#`）

- **前置 `1`**（工項一之端·`e6a2289`）：`F30 selftest` `rc 1`·末列 `⇒ 紅 ['K0']；rc 1`；`F30 wiring … 158f7fe` `rc 1`·`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W7']；rc 1`；`F30 run` `rc 1`·`⇒ 紅 ['R0']；rc 1`；三呼叫 `stderr` `0` B。`F23 selftest` `rc 0`·`P0 逐項擾動恰該項紅 75／75`。
- **前置 `2`**：其餘 `52` 呼叫皆 `rc 0`、末列 ＝ `§五-1` 項 `8`（`44` 呼叫 `⇒ 紅 []；rc 0`；`F27 mutate` `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`F25 mutate` `⇒ 突變 8（另基準一）；紅 []；rc 0`；`screen wiring` `⇒ rc 0（不符 0·器紅 0）`；`k6s3 selftest` `selftest 9/9 ⇒ ✅`；`pooltemp selftest` `selftest 13/13 ⇒ ✅`；`synth` `ε ＝ 0.0002｜rc 0`；`main_synth` `紅項 [] 器紅 0`）。
- **前置 `3`**：`k6s3 run`／`F8 run`／`parity` 二退縮六呼叫皆 `rc 0`（`parity` 末列 `⇒ rc 0（不符 0 項）`）·`stderr` `0` B。
- **前置 `4`**：「def k974_burden_scales」無出艙 `rc 1`；「僅新闢道路計入臨街地特別負擔」`app.py:1`；「k974_read_junctions(_doc_cad_p7)」無出艙 `rc 1`。
- **`V-1`**（於 `fb63735`）：七呼叫皆 **`rc 0`**·`⇒ 紅 []；rc 0`；`F30 selftest` `K1`〜`K16` ✅；`F30 wiring` `W1`〜`W7` ✅（`W7`：相異 `['K974_PARAMS', 'calc_special_burden_total', 'k962_land_marks', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'main']`／刪列 `3`）；`F30 run` `R1`〜`R6` ✅（`R1` 各面之尺度 ＝ 快照·警示 `0`·錯誤 `0`；`R2` `741.76`／`741.76`；`R3` `RD1 1082.2651`／`628-34 之片 131.6000`／比例 `0.878403`／負擔路寬 `7.0272`／期 `1.513613`、`0.756806`／得 `1.513616`、`0.756808`；`R5` 框內 `89.6652`／比例 `0.867420`／期 `1.469679`／得 `1.469679`）；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`。
- **`V-2`**：`48` 呼叫皆 **`rc 0`**、末列 ＝ `§五-1` 項 `8` 之施後之列（同前置 `2` 之諸末列）。
- **`V-3`**：四器之 blob ＝ `§五-1` 項 `5`（`ccdb11f3…`／`d76cf9fe…`／`b1ad31f5…`／`c21b6676…`）。
- **`V-4`**：`k6s3 cmp` 二退縮皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`·`stderr` `0` B。
- **`V-5`**：`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`。以同一字樣（`<HEAD>`）代 `HEAD` 之全值（二態各恰一見）後：二落檔、二 `stdout` 皆逐位同；對照（⛔ 代之）：四者皆相異。
- **`V-6`**：`git hash-object`：`f8_pre_35`／`f8_post_35` ＝ `6b0d558fc16e581a92c8a6fc6db95561bfa70b53`（二列相等）；`f8_pre_00`／`f8_post_00` ＝ `8daf7e0e4d71dd7863e0ab45ec5820930863e8aa`（二列相等）。🔒 其值與 `§一` 項 `5` 之發單側（Linux）之值（`8be0160b…`／`6fb86647…`）異——`V-6` 之期唯前後相等（照實載·本機 Windows）。
- **`V-7`**：生產碼 `34` 檔（`app.py` ＋ `verify/*.py` `33`）對工項一之端相異恰 `1`（`app.py`·`+357`／`-3`）；`verify/` 之一切檔相異 `0`；AST：頂層之新名 ＝ `{K974_PARAMS, k962_land_marks, k974_burden_scales, k974_read_junctions, k974_screen_scales}`、去者 `0`；相異之節點 ＝ 此五 ∪ `{calc_special_burden_total, main}`。
- **`V-8`**：「def k962_land_marks」「def k974_read_junctions」「def k974_burden_scales」「def k974_screen_scales」「K974_PARAMS = {」「_k974 = k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)」「k974_read_junctions(_doc_cad_p7)」「sb = calc_special_burden_total(road_data, C_for_calc)」各 `app.py:1`；「僅新闢道路計入臨街地特別負擔」無出艙 `rc 1`。
- **`V-9`**：`V-1`〜`V-6` 之諸器之 `stderr` 合計 `0` B。

🔒 **撰碼中之自跑**（單首 🔑）：於施工樹先跑 `F30` 之三、`F23 wiring`／`F24 wiring`／`F25 wiring`、`F23 selftest` 與十六器（諸 `wiring`、`harvest_key`、`synth`、`main_synth`）皆符，始 `commit`；其間 `F23 wiring` 之 `W8`／`F24 wiring` 之 `W7` 紅一次（錨 `重劃區外` 於基準恰一見·初稿之步驟 E 之說明書「道路在重劃區外者不計」致 `2`）⇒ 改書「道路在區外者不計」（`R-7` ⑤ 之字樣）·其後皆綠（自捕·⛔ 改器）。

## 四、停機之由：唯讀獨立審查之發現 #1、#2（規格之漏載）

審查者 ＝ 另派之唯讀 reviewer（⛔ 改檔·⛔ `commit`·其草稿存 `<O>\review_scratch\`）。其 BLOCKED `0`、純實作之瑕（b）`0`；涉規格之漏載（a）`12` 則，其中二則審查者建議呈 KL：

**#1　公有持分之缺值（`NaN`）⇒ ⛔ 錯誤、尺度靜默成最大值 `5.0`**（`fb63735` 之 `app.py:4993-4994`、`:5002`、`:5168`；既有之 `calc_frontage_burden_scale` `:4744-4750`）
- **形**：註記之地號之 U_LAND 之列中，「公私別」＝「公」者之「權利範圍分子」或「分母」為空 ⇒ `share` ＝ `NaN`；`share <= 0` 為偽 ⇒ ⛔ 入錯誤；`min(NaN, 1.0)` ＝ `NaN` 入 `抵充地`。下游 `if sh:` 以 `NaN` 為真 ⇒ `B` ＝ `NaN` ⇒ 比例 ＝ `NaN` ⇒ `calc_frontage_burden_scale(NaN)` 之諸比較皆偽 ⇒ 回 `5.0`（最大之尺度）。
- **證**（審查者實跑·CC 復讀其碼同）：例 N1 ⇒ `{'抵充地': {'10-1': nan}, 'errors': []}`；合成之例 E6（`NaN` 之持分）⇒ 正面 `2.975`（期 `2.15`·`RB` 之段之尺度成 `5.0`）。
- **規格**：`R-2` ③ 唯定「公有持分 ＝ Σ（公私別 ＝「公」之所有權人之「權利範圍分子」÷「權利範圍分母」）；其 ≤ `0` ⇒ 錯誤」——分子／分母之缺值⛔ 載。tab1 之同讀以 `pd.notna` 守之（`app.py` 之歸戶指紋）。

**#2　地籍資料來源之讀取之例外 ⇒ 步驟 H 中止（未捕）**（`fb63735` 之 `app.py:4993`、`:4958`、`:5205`）
- **形**：分母 `0` ⇒ `ZeroDivisionError`（例 N2）；U_LAND 缺「段小段」之欄 ⇒ `KeyError`（例 N12）；`k974_screen_scales` 之 `pd.ExcelFile`／`read_excel` 之任一失敗亦上拋——皆⛔ 捕 ⇒ `main` 之步驟 H 以例外中止（施前之步驟 H ⛔ 讀 Excel）。tab1 之同讀以 `try`／`st.error` 承之。
- **規格**：`R-2`／`R-5` ⛔ 載例外之處置；`R-4` 末「⛔ 停機（錯誤唯入回傳）」唯及 `k974_burden_scales`。

**後果之界**：本案⛔ 觸（本案之「重劃區地籍」無二欄 ⇒ `U_LAND` ⛔ 讀、`k962_land_marks` 回三空；`V-4`〜`V-6` 配地⛔ 變）；`F30` 之合成之例與模擬⛔ 及之（其持分皆有值）。他案之 U_LAND 若有公有之列之持分空白或分母 `0`、或其表之欄名異 ⇒ 前者靜默以最大之尺度計、後者畫面中止。

**CC 之判**：二者之處置須定（例：持分缺值 ⇒ 填列錯誤〔其字樣〕／該所有權人略之／以 `0` 計；讀取之例外 ⇒ 填列錯誤而停止計算〔其字樣〕／上拋）——屬規格之定 ⇒ **停機款 `12`·⛔ 自裁**。諸例僅列其形，CC ⛔ 擇。

## 五、唯讀獨立審查之其餘發現與處置

| # | 級 | 要旨 | 處置 |
|---|---|---|---|
| `1` | (a)·呈 | 公有持分之缺值 ⇒ 尺度靜默成 `5.0`（上開四） | **停機款 `12`** |
| `2` | (a)·呈 | 讀取之例外 ⇒ 步驟 H 中止（上開四） | **停機款 `12`** |
| `3` | (a) | 中心線之長 `0` 之節：碼略之（`:5136-5137`）；諸點皆重合者報「未繪 CENTERLINE」（例 E3）——`|cross| ÷ 節長` 於此無定 | 照實呈（CC 之實作之擇·規格⛔ 載） |
| `4` | (a) | 面之線落於中心線上（`cross` ＝ `0`）⇒ `d` ＝ `0`·帶空 ⇒ 區界 ⇒ 基寬 `0`·尺度 `0` ＋ 路寬之警示（例 E4）——「側 ＝ 叉積之號」於 `0` 無定 | 照實呈 |
| `5` | (a) | `§三-4` 所列之二形（線之中點之二向之偏移點皆落於街廓內；最近之節有二而其側相異）於執行時⛔ 偵（`:5097` 唯反向一次；`:5139-5140` 取先） | 照實呈（`§三-4` 定為撰碼中之停機之形·執行時之偵否⛔ 載） |
| `6` | (a) | 道路 BLOCK 內之宗地之片重疊而 `B` ＞ `A` ⇒ 比例 ＜ `0`（例 E5 ⇒ `−0.4`）⇒ 負擔路寬 ＜ `0` ⇒ 尺度靜默為 `0`、明細載負比例 | 照實呈 |
| `7` | (a) | 可建築街廓之頂點為 `None` 或二點 ⇒ 函式拋例外（例 E7／E10）；`R-5` 之式唯道路 BLOCK 以 `vertices` 篩之 | 照實呈 |
| `8` | (a) | `k962_land_marks` 之角落：地段空白算一相異之地段（例 N5：「地號 10-1 於 甲段、 皆有」）；浮點之地號 `10.0` ⇒「U_LAND 無對應資料」（同 tab1）；`NaN` 之地段／地號印為空字串；統編與姓名皆空者去重而併（同 `build_ownership`）；一格至多一錯誤、③ 先於 ④（例 N7） | 照實呈 |
| `9` | (a) | 面之一部⛔ 臨道路 BLOCK 者，其部以 `0` 計而明細無其列（臨接比之和 ＜ `1`）；勾新闢而部分未臨者⛔ 警示（`K-9-79` ② 唯及皆⛔ 臨者） | 合規格·照實呈（畫面⛔ 見） |
| `10` | (a) | 路寬之警示之字樣無道路 BLOCK 之名 ⇒ 一面臨二段者之二則無從分辨（字樣依 `R-4`） | 合規格·照實呈 |
| `11` | (a) | 錯誤 ⇒ `st.stop()` ⇒ `f3_sb_rows`（`:28376`）留前一輪之值（`:19968` 讀之）；置處依 `R-7` ② | 合規格·照實呈 |
| `12` | (a) | `f3_cad_junctions` 唯精準圖層之讀取成功時更新 ⇒ 換 DXF 而其讀取失敗時留前檔之框（同既有之 `f3_cad_*` 之諸鍵） | 合規格·照實呈 |
| `13` | (c) | `R-1`〜`R-5` 逐條合（取樣、法向、容差〔同距依 label 之序〕、垂距與側、帶之號、無宗地之一則警示、`JUNCTION` 之去、新闢 ⇒ 比例 `1`〔⛔ 求 `A`／`B`〕、權 ＝ 段數之比·每一道路恰加一次、明細之十鍵與「（無）」之列、線長 `0` 之面略之、`buffer(0)`、⛔ 讀 session；七則訊息之字樣；`R-5` 之存〔缺表亦存〕、`U_LAND` 唯二欄有值時讀、左側之補、錯誤之序） | — |
| `14` | (c) | `R-6`〜`R-9`：`calc_special_burden_total` 唯增列；`main` 恰三易列（`:28055-28057`、`:28411-28413`）；`JUNCTION` 之讀於 `dxf_quantum` 之列之後（隔一註列）；`_k974` 之列逐字·⛔ 附行末之註；警示、錯誤與 `st.stop()` 在 `road_data = []` 之前；尺度之鍵唯有其面者增；明細之展開在表之後；caption 載 `R-7` ⑤ 之四點；`K974_PARAMS` 以 🆕 之註代 docstring（`dict` 無 docstring） | — |

**審查者之獨立之合成之例**（`F30` 之外·harvest 實跑）：街廓 B1 ＝ `(0,0)`–`(100,30)`；正面 `(0,0)→(100,0)` 臨 `RA`（`x` `0`–`30`）、`RB`（`30`–`60`·其內宗地 `2` ＝ `x` `30`–`42`·`180 ㎡`·抵充地持分 `1`）、`x` `60`–`80` 無道路 BLOCK、`RC`（`80`–`100`·其另一側唯 `_GHOST_x` 之片 ⇒ 區界）；左側臨 `RW`（勾新闢·`8 m`）；正面輸入 `15 m`·未勾。手算：段數 `120`／`120`／`80`（無）／`80` ⇒ `RA` `3.75`、`RB` 比例 `0.6` ⇒ `9 m` ⇒ `2.25`、`RC` 區界 ⇒ `7.5` ⇒ `1.75` ⇒ 正面 ＝ `0.3·3.75 ＋ 0.3·2.25 ＋ 0.2·0 ＋ 0.2·1.75` ＝ **`2.15`**、左側 **`1.0`**；`RB` 之 `x` `50`–`60` 加 `JUNCTION` ⇒ `A` `300` ⇒ 比例 `0.4` ⇒ `6 m` ⇒ `1.0` ⇒ 正面 **`1.775`**。實得 `{'front': 2.15, 'left': 1.0}`、`{'front': 1.7750000000000001, 'left': 1.0}`·警示、錯誤皆 `0`·明細合手算。對照：`_GHOST` 之片改為實地號 ⇒ `RC` 非區界 ⇒ 正面 `2.55`（合期）；中心線反向 ⇒ 區界仍真；另一側加地籍 ⇒ 區界偽。審查者另實跑 `F30`（三）、`F23`／`F24`／`F25 wiring` 皆 `rc 0`·`stderr` `0` B；`git status --porcelain` 恆空。
🔒 審查者自陳：其 `F23` 之出艙初誤寫於 `<O>\review_scratch_f23w.txt`（許可之目錄之外·仍在倉外），後移入 `<O>\review_scratch\f23w.txt`；⛔ 觸任何 git 工作樹。

## 六、設計說明（`§三-5`·摘要·全文差異見同目錄之 `.diff`）

- **`R-1`**：`K974_PARAMS`（`app.py:4908-4915`·`calc_special_burden_total` 之後）恰六鍵；其上一列之註以 ``🆕 `W-G.9-385`（`R-1`…`` 起首（`dict` 無 docstring）。
- **`R-2`** `k962_land_marks`（`:4918-5003`）：二欄以欄名取之（序恆「第33條排除」→「抵充地」）；格之值以巢狀 `_k974_cell_text` 去空白（`None`／`NaN` ⇒ 空）；地號之整數依 tab1 之 `重劃地號轉ULAND整數` 之式（例外 ⇒ 無之）；去重之鍵同 tab1 之歸戶指紋；④ 之地段之序 ＝ 全表首見之序；一格至多一錯誤（③ 先於 ④）。
- **`R-3`** `k974_read_junctions`（`:5006-5029`）。
- **`R-4`** `k974_burden_scales`（`:5032-5184`）：道路 BLOCK 以 `shapely.prepared.prep` 判 `contains`（等價·省時）；容差之最近者以嚴格 `<` 取 ⇒ 同距取 label 之序之先；垂距之最近之節以 `LineString.distance` 之嚴格 `<` ⇒ 同者取先；長 `0` 之節略之（#3）；帶之號：`cross` ＜ `0`（點在中心線之右）⇒ `+d`（左側）、否則 `−d`；地籍之聯集於首次須判區界時始求（巢狀 `_k974_cad_union`）；權 ＝ `(len(ts) / n) * sc` 逐道路一加。
- **`R-5`** `k974_screen_scales`（`:5187-5228`）：`import hashlib` 於函式內（⛔ 增頂層之節點）。
- **`R-6`**：`calc_special_burden_total` 增六列（三 `if`）與 docstring 之 🔧 一款。
- **`R-7`**：三易列（步驟 E 之 caption 一列 ⇒ 三列·前句「路寬長度計算至……不計道路截角。」原樣留之；公式說明二列 ⇒ 三列）；增列五處（`JUNCTION`、`_k974` 與警示錯誤、尺度之鍵、明細之展開）。
- **`§三-3` 之自查**：`F23 wiring`（`W7`／`W8`）、`F24 wiring`（`W5`／`W7`）、`F25 wiring`（`X2`）、`F30 wiring`（`W1`／`W7`）、`F27 mutate`、`F25 mutate`、`F19 mut`、`F22 mut`、`F17`／`F10`／`F27`／`F29`／`F14`／`F15`／`F9`／`F4` 之接線皆綠（`V-1`／`V-2`）；巢狀之名皆以 `_k974_` 起首（基準無之）；四新函式⛔ 案件字面（`W1`）。

## 七、⛔ 辦之項

- 工項二之 `push`、工項三（塊 `K25`／`E28`／`P38` 之入典·`checkidx`／`gen_fa_index`）、工項四（執行報告）、收工閘——皆⛔ 辦（停機）。塊 `K25`／`E28`／`P38`、`CK`／`GF` 之抽取已存 `<O>`（對拍皆符）·⛔ 寫入倉。
- 次之處置候發單側之裁（#1、#2 之處置之定）；`hold/W-G.9-385-c2` 之碼可為其基。

## 八、`61` 呼叫（`V-1`〜`V-2` 之 `55` ＋ 前置 `3`／`V-4`〜`V-6` 之六）之 `rc`／`stderr`／耗時／末列

並行：前置 `5`（`<O>\runner.py`）；驗 `4` ＋ `1`（`screenmerge run` 先起）；撰碼中之自跑另 `1`——同時 ≤ `6`。末列 ＝ `stdout` 之末一非空列（去行尾之 `\r`）。逾時或 `rc` ≠ 期者 `0` ⇒ 無重跑之趟。

| # | 呼叫 | 前置（`e6a2289`）rc／stderr B／s | 前置之末列 | 驗（`fb63735`）rc／stderr B／s | 驗之末列 |
|---|---|---|---|---|---|
| `1` | `python verify/probes/probe_WG9385_k974.py selftest <repo>` | `1`／`0`／`4.3` | `⇒ 紅 ['K0']；rc 1` | `0`／`0`／`4.7` | `⇒ 紅 []；rc 0` |
| `2` | `python verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `1`／`0`／`15.4` | `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W7']；rc 1` | `0`／`0`／`16.8` | `⇒ 紅 []；rc 0` |
| `3` | `python verify/probes/probe_WG9385_k974.py run <repo>` | `1`／`0`／`5.3` | `⇒ 紅 ['R0']；rc 1` | `0`／`0`／`343.3` | `⇒ 紅 []；rc 0` |
| `4` | `python verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` |
| `5` | `python verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`37.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`33.5` | `⇒ 紅 []；rc 0` |
| `6` | `python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`33.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`34.7` | `⇒ 紅 []；rc 0` |
| `7` | `python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`12.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`12.9` | `⇒ 紅 []；rc 0` |
| `8` | `python verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.2` | `⇒ 紅 []；rc 0` |
| `10` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`57.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`62.3` | `⇒ 紅 []；rc 0` |
| `11` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`26.3` | `⇒ 紅 []；rc 0` | `0`／`0`／`26.7` | `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`46.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`52.3` | `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `15` | `python verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`3.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`3.1` | `⇒ 紅 []；rc 0` |
| `16` | `python verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`74.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`86.0` | `⇒ 紅 []；rc 0` |
| `17` | `python verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`565.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`614.4` | `⇒ 紅 []；rc 0` |
| `18` | `python verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`811.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`864.5` | `⇒ 紅 []；rc 0` |
| `19` | `python verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`24.2` | `⇒ 突變 8（另基準一）；紅 []；rc 0` | `0`／`0`／`23.1` | `⇒ 突變 8（另基準一）；紅 []；rc 0` |
| `20` | `python verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.3` | `⇒ 紅 []；rc 0` |
| `21` | `python verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`10.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`11.0` | `⇒ 紅 []；rc 0` |
| `22` | `python verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`171.2` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` | `0`／`0`／`160.7` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` |
| `23` | `python verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`493.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`534.9` | `⇒ 紅 []；rc 0` |
| `24` | `python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `25` | `python verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`2085.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`2216.5` | `⇒ 紅 []；rc 0` |
| `26` | `python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`69.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`78.2` | `⇒ 紅 []；rc 0` |
| `27` | `python verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`4.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `28` | `python verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`16.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`18.7` | `⇒ 紅 []；rc 0` |
| `29` | `python verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`42.4` | `⇒ rc 0（不符 0·器紅 0）` | `0`／`0`／`47.3` | `⇒ rc 0（不符 0·器紅 0）` |
| `30` | `python verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`5.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`5.0` | `⇒ 紅 []；rc 0` |
| `31` | `python verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`20.3` | `⇒ 紅 []；rc 0` | `0`／`0`／`21.8` | `⇒ 紅 []；rc 0` |
| `32` | `python verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`49.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`56.5` | `⇒ 紅 []；rc 0` |
| `33` | `python verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`420.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`455.5` | `⇒ 紅 []；rc 0` |
| `34` | `python verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`31.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`34.0` | `⇒ 紅 []；rc 0` |
| `35` | `python verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`112.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`123.4` | `⇒ 紅 []；rc 0` |
| `36` | `python verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`27.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`29.0` | `⇒ 紅 []；rc 0` |
| `37` | `python verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`73.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`80.2` | `⇒ 紅 []；rc 0` |
| `38` | `python verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`52.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`55.4` | `⇒ 紅 []；rc 0` |
| `39` | `python verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`45.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`50.5` | `⇒ 紅 []；rc 0` |
| `40` | `python verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`235.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`227.6` | `⇒ 紅 []；rc 0` |
| `41` | `python verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.3` | `⇒ 紅 []；rc 0` |
| `42` | `python verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`31.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`33.5` | `⇒ 紅 []；rc 0` |
| `43` | `python verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`598.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`635.6` | `⇒ 紅 []；rc 0` |
| `44` | `python verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.3` | `⇒ 紅 []；rc 0` |
| `45` | `python verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`3.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`3.3` | `⇒ 紅 []；rc 0` |
| `46` | `python verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`193.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`185.5` | `⇒ 紅 []；rc 0` |
| `47` | `python verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`427.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`448.2` | `⇒ 紅 []；rc 0` |
| `48` | `python verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`4.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `49` | `python verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`427.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`444.3` | `⇒ 紅 []；rc 0` |
| `50` | `python verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`0.1` | `selftest 9/9 ⇒ ✅` | `0`／`0`／`0.1` | `selftest 9/9 ⇒ ✅` |
| `51` | `python verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`0.1` | `selftest 13/13 ⇒ ✅` | `0`／`0`／`0.1` | `selftest 13/13 ⇒ ✅` |
| `52` | `python verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`8.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`8.0` | `⇒ 紅 []；rc 0` |
| `53` | `python verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`4.6` | `ε ＝ 0.0002｜rc 0` | `0`／`0`／`4.3` | `ε ＝ 0.0002｜rc 0` |
| `54` | `python verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`33.8` | `紅項 [] 器紅 0` | `0`／`0`／`34.0` | `紅項 [] 器紅 0` |
| `55` | `python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`433.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`458.3` | `⇒ 紅 []；rc 0` |
| `56` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json` | `0`／`0`／`270.2` | `{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4…` | `0`／`0`／`240.2` | `{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4…` |
| `57` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>\k6s3_post_00.json` | `0`／`0`／`195.6` | `{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4…` | `0`／`0`／`173.4` | `{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4…` |
| `58` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_post_35.json` | `0`／`0`／`246.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`213.7` | `⇒ 紅 []；rc 0` |
| `59` | `python verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>\f8_post_00.json` | `0`／`0`／`181.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`154.0` | `⇒ 紅 []；rc 0` |
| `60` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json` | `0`／`0`／`543.6` | `⇒ rc 0（不符 0 項）` | `0`／`0`／`587.6` | `⇒ rc 0（不符 0 項）` |
| `61` | `python verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>\parity00_post.json` | `0`／`0`／`375.4` | `⇒ rc 0（不符 0 項）` | `0`／`0`／`407.5` | `⇒ rc 0（不符 0 項）` |

耗時之和：前置 `61` 呼叫 `9704.1` s（其中 `55` 呼叫 `7891.4` s）；驗 `61` 呼叫 `10464.5` s（其中 `55` 呼叫 `8688.1` s）。stderr 合計：前置 `0` B；驗 `0` B。
