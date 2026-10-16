# `W-G.9-385R`　補令一　工項二″　停機上呈（停機款 `12″`·唯讀獨立審查之發現 #1：`R-13` 之「比例 ＜ `0`」⛔ 設容差——道路 `BLOCK` 恰為一筆全公有之抵充地（真比例 `0`）者，於實座標之尺度下浮點之誤差（約 `−1e-16`）使之誤報「宗地之片重疊」而停止計算·規格之漏載）

> **受單** ＝ CC 窗（`2026-10-16`·續原單之窗）。**來源檔** ＝ KL 主 checkout 之根（第二處·二進位複製·入倉後 `git cat-file blob` 與來源 `cmp` 同）；KL 之訊⛔ 載 bytes／`sha256`（唯貼檔之路徑）⇒ 以 `SELF_SHA256` 為據（`d71faf55…d8804ea010` 相符·`probe_order_preflight` 之 `P-5` 亦相符）。
> **本檔 ＝ 停機上呈**（原單 `§五-2` 之 1·本補令 `§零-2″` 款 `12″`）：工項二″ 之碼**⛔ 推新側支**、存本地 `hold/W-G.9-385p1-c2`；工項三″、四″ ⛔ 辦。⛔ 自改、⛔ 自裁。
> context 餘量（開場自報）：約 `14.98M` tokens。

---

## 一、態

| 項 | 值 |
|---|---|
| 主線 `wip/s1-endpart` | `158f7fe959697571d8179988cd4c192c0016ead9`（⛔ 動） |
| 新側支 `verify/W-G.9-385-k974` | `32bb289`（原單之停機上呈）→ 工項零″ `b248f350f2467a591b7d1056d84c6b9a6802c528` → 工項一″ `01ad480b221fe80bcfc4edd04c997d5569d3eba1` → 本停機上呈之 `commit`（零生產碼） |
| 工項二″ 之碼 | 本地 `hold/W-G.9-385p1-c2` ＝ `28046f2f03a86b3786c873e84e5afe678bcb048f`（**⛔ push**）；`app.py` ＝ `797082a61374214280aa1d11f4b9578eb2795f44`（`1841263` B·對工項一″ 之端 `+381`／`-3`·對 `hold/W-G.9-385-c2` `+31`／`-7`）；全文差異（對工項一″ 之端）＝ 同目錄 `W-G.9-385R_補令一_工項二_app差異.diff`（`27119` B·CR `0`） |
| 前之 `hold` | 本地 `hold/W-G.9-385-c2` ＝ `fb63735`（留之·⛔ push） |
| 遠端 heads | `45`（⛔ 增） |
| `<O>` | `C:\Users\admin\w385o`（同原單）；前置於倉外之 worktree `C:\Users\admin\w385P`（`01ad480`·跑後 `git status --porcelain` 空） |

## 二、停機款（款·期·實）

| 款 | 期 | 實 |
|---|---|---|
| `1″` | 主線 `158f7fe`·新側支 `32bb289`·heads `45`·`hold/W-G.9-385-c2` ＝ `fb63735`、其 `app.py` ＝ `e89fbe62…`·追蹤檔⛔ 變·`§零` 項 `3` 之值·旗標 | 皆符（追蹤檔 `2870`；自誤 `605`／`620`、`GB` `197`／`205`、`VR` `80`／`95`、`K-9` `75`／`78`·缺號同原單；旗標 `[None×5]`） |
| `2″` | `SELF_SHA256`·入倉之 blob ＝ 來源 | 皆符（本補令 `36994` B·全檔 `sha256` `5ada8b41…6c913a90`·`275` 列·CR `0`；`P-5` 之受詞 `36916` B ⇒ `d71faf55…`） |
| `3″` | 塊之對拍·`git apply --check`·施後之 blob | 皆符（`Fy36` `5067`／`4e298e68…`／`76`；`K26` `4630`／`a301667e…`／`24`；`E29` `2543`／`5596263d…`／`13`；原單之 `K25`／`E28`／`P38`／`CK`／`GF` ＝ 原單 `§五-1`；`F30` 施前 `c21b6676…` → 施後 `be9eba12…`·`38190` B） |
| `4″` | 工項二″ 前置 `1`、`2` | 皆符（下開三） |
| `5″` | ⛔ 歧義而涉域上判斷 | 撰碼中⛔ 見 |
| `6″` | 驗 | **皆符**（下開三） |
| `7″` | 推之目標唯新側支·⛔ 被拒·主線⛔ 推進 | 皆符（工項零″、一″ 快轉·首推即成） |
| `8″`〜`9″` | 工項三″·收工閘 | ⛔ 辦（停機）；工項三″ 之三簿之施後 blob 已於 `<O>` 預算（倉外·⛔ 寫入倉）：`K-6` 典 `801055` → `820560` ＝ `0b02b2c8…`、自誤簿 `1196778` → `1201371` ＝ `2863ae12…`、`CLAUDE.md` `408690` → `413291` ＝ `6a2ff2ce…`（皆 ＝ `§五″` 項 `5`·嚴格前綴·CR `0`） |
| `10″` | CC ⛔ 自判 | ⛔ 自判（#1 呈之） |
| `11″` | 新檔⛔ 為 ignore 所命中 | 本補令、本檔二新檔之 `git check-ignore -v --no-index` 皆無命中 |
| `12″` | 唯讀審查之發現涉域上判斷或規格之漏載 | **成就**——#1（下開四） |

## 三、前置與驗之結果（全出艙存 `<O>\p1pre\`、`<O>\p1post\`）

- **前置 `1`**（工項一″ 之端·`01ad480`）：`F30 selftest` `rc 1`·`⇒ 紅 ['K0']；rc 1`；`F30 wiring … 158f7fe` `rc 1`·`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W7']；rc 1`；`F30 run` `rc 1`·`⇒ 紅 ['R0']；rc 1`；其餘 `52` 呼叫 `rc 0`、末列 ＝ 原單 `§五-1` 項 `8`（`F23 selftest` `P0 逐項擾動恰該項紅 75／75`）；前態六呼叫（`k6s3 run`／`F8 run`／`parity`）`rc 0`；`61` 呼叫之 `stderr` 合計 `0` B。原單前置 `4`：「def k974_burden_scales」無出艙 `rc 1`；「僅新闢道路計入臨街地特別負擔」`app.py:1`；「k974_read_junctions(_doc_cad_p7)」無出艙 `rc 1`。
- **前置 `2`**：`git checkout hold/W-G.9-385-c2 -- app.py` ⇒ `git hash-object app.py` ＝ `e89fbe6215c2cab7285741d1235c77f531f19131`；`F30 selftest` ⇒ `rc 1`·`stderr` `0` B·末列 `⇒ 紅 ['K17', 'K18', 'K19']；rc 1`（`K17`：`例外 ZeroDivisionError: float division by zero`；`K18`：`{'B1': {'front': 0.0}}／[]`；`K19`：`[('壞檔', False, '拋 BadZipFile'), ('缺欄', False, '拋 KeyError')]`）。
- **施**：`R-11`（`k962_land_marks`·`28046f2` 之 `app.py:4989-5006`）、`R-12`（`k974_screen_scales`·`:5226-5235`）、`R-13`（`k974_burden_scales`·`:5186-5189`）、三函式之 docstring 之末各增 ``🔧 `W-G.9-385` 補令一`` 之一款；`py_compile` 過。
- **`V-1`**（於 `28046f2`）：七呼叫皆 **`rc 0`**·`⇒ 紅 []；rc 0`；`F30 selftest` `K1`〜`K19` ✅（`K17` `{'抵充地': {'100-3': 0.5}, …}`＋二則錯誤；`K18` `{'B1': {'front': 0.0}}`＋錯誤一則；`K19` `BadZipFile`／`KeyError` 皆入「地籍資料來源讀取失敗（」之錯誤一則）；`F30 wiring` `W1`〜`W7` ✅；`F30 run` `R1`〜`R6` ✅（`R3` `1.513616`、`0.756808`；`R5` `1.469679`）；`F23 selftest` `P0 75／75`。
- **`V-2`**：`48` 呼叫皆 **`rc 0`**、末列 ＝ 原單 `§五-1` 項 `8` 之施後之列。
- **`V-3`**：四器之 blob ＝ `ccdb11f3…`／`d76cf9fe…`／`b1ad31f5…`（原單 `§五-1` 項 `5`）、`be9eba12…`（本補令 `§五″` 項 `5`）。
- **`V-4`**：`k6s3 cmp` 二退縮皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`。
- **`V-5`**：`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`；以 `<HEAD>` 代 `HEAD` 之全值（二態各恰一見）後二落檔、二 `stdout` 皆逐位同；對照（⛔ 代之）：皆相異。
- **`V-6`**：`f8_pre_35`／`f8_post_35` ＝ `6b0d558fc16e581a92c8a6fc6db95561bfa70b53`（二列相等）；`f8_pre_00`／`f8_post_00` ＝ `8daf7e0e4d71dd7863e0ab45ec5820930863e8aa`（二列相等·同機之前後相等）。
- **`V-7`**：對工項一″ 之端相異恰 `app.py`；`verify/` 相異 `0`；頂層之新名 ＝ 五、相異之節點 ＝ 原單之七。
- **`V-8`**：原單 `R-9` 之八字樣各 `app.py:1`、「僅新闢道路計入臨街地特別負擔」無出艙 `rc 1`；`R-14`：「缺漏或分母非正數」「地籍資料來源讀取失敗（」「宗地之片重疊」各 `app.py:1`。
- **`V-9`**：`stderr` 合計 `0` B。

🔒 撰碼中之自跑：`F30`（三）、`F23 wiring`、`F24 wiring`、`F25 wiring`、`main_synth` 皆綠，始 `commit`（⛔ 紅之趟）。

## 四、停機之由：唯讀獨立審查之發現 #1（規格之漏載）

**形**：`R-13` 逐字「未勾新闢而比例 `r` ＜ `0`（`B` ＞ `A`·宗地之片重疊）⇒ 錯誤……、略之」——碼依之以嚴格之 `ratio < 0`（`28046f2` 之 `app.py:5186`）。道路 `BLOCK` 恰為一筆全公有之抵充地之片（持分 `1`·其片 ＝ 道路之多邊形）者，真比例 ＝ `0`；然 `A`（`difference` 之面積）與 `B`（片 ∩ 去後之多邊形之面積）於實座標（TWD97 之量級·旋轉之道路）之浮點之計算相差約 `1e-12 ㎡` ⇒ 比例 ≈ `−1e-16` ⇒ 誤報「道路 BLOCK … 內抵充地之面積大於扣除路口後之面積（宗地之片重疊），請檢查地籍（…）」而停止計算（步驟 H）。
**證**：
- 審查者（`<O>\review2_scratch\bad_all.py`·`out_all.txt`·`C5`）：隨機之旋轉之道路三百（座標 `1e5`〜`3e5`、`2.5e6`〜`2.8e6`）、各一片 ＝ 道路之多邊形·持分 `1.0` ⇒ 誤報 `41`／`300`（⛔ `JUNCTION`）、`37`／`300`（有 `JUNCTION`）；真比例皆 `0`。
- CC 復現（`<O>\review2_scratch\cc_r13_check.py`·獨立之造法·種子 `385`）：旋轉之道路二百 ⇒ 誤報 **`36`／`200`**；軸向（近水平）之道路二百 ⇒ `0`／`200`（浮點之誤差依方位而異）。
- 施 `R-13` 前（`hold/W-G.9-385-c2`）：同形之比例 ≈ `−1e-16` ⇒ 負擔路寬 ≈ `−1e-15` ⇒ `calc_frontage_burden_scale` ⇒ `0.0`（即真值）·⛔ 錯誤。
**後果之界**：本案⛔ 觸（本案之「重劃區地籍」無二欄 ⇒ 持分皆 `0` ⇒ `B` ＝ `0`）；`F30` 之 `K18`（整數座標·`B` ＝ `2A`）⛔ 及之。他案：既成道路全為公有土地而填「抵充地」者（常見之形）——依方位約一成餘之道路 `BLOCK` 誤報而停止計算，使用者無從改正（地籍無誤）。
**CC 之判**：`R-13` 之判須一容差（例：絕對 `r` ＜ `−ε`、或以面積 `B − A` ＞ `ε ㎡`、或相對 `A`；其值）——屬規格之定 ⇒ **停機款 `12″`·⛔ 自裁**。諸例僅列其形，CC ⛔ 擇。

## 五、唯讀獨立審查之其餘發現與處置

| # | 級 | 要旨 | 處置 |
|---|---|---|---|
| `1` | (a)·呈 | `R-13` 之 `ratio < 0` ⛔ 容差（上開四） | **停機款 `12″`** |
| `2` | (c) | `R-11`（`:4989-5006`）：`pd.to_numeric(…, errors='coerce')`；分子／分母 `NaN`、分母 ≤ `0`、分子 ＜ `0` 唯及去重後之公有者；字樣逐字；該格 `continue`（⛔ 再判非公有地與 ④）；序 無對應 → `R-11` → 非公有地 → 二地段（例 `A7`、`A7b`、`A7c`、`A2d`）；`0`／負／空白／文字／`None`／`Timestamp` 皆⛔ 拋 | — |
| `3` | (c) | `R-12`（`:5226-5235`）：`try` 涵 `pd.ExcelFile`、表名之查、二 `read_excel`、`filled`、`k962_land_marks`；字樣逐字；`(h, marks)` 各支皆存、再呼用其存（`B1b`）；`k974_burden_scales` 在 `try` 之外（其例外上拋·`B7`／`B7b`） | — |
| `4` | (c) | `R-13` 之支之形：`continue` 在比例之後、路寬之警示之前 ⇒ ⛔ 入面之尺度、⛔ 入明細、⛔ 警示（同 `A ≤ 0`）；勾新闢者比例 `1` ⇒ ⛔ 及（`C1`〜`C3`） | — |
| `5` | (c) | `R-15`：三函式之 docstring 之末各一款（`:4929-4931`、`:5060-5061`、`:5213-5214`）；對 `hold` 之他處⛔ 改（AST：唯三函式異·去 docstring 後亦然；函式名之數⛔ 變）；頂層之新名唯五；新巢狀之名三（`_k974_cell_text`、`_k974_polygon`、`_k974_cad_union`）於 `158f7fe` 皆 `0` 見 | — |
| `6` | (a)·註 | 缺表 ⇒ 三空而⛔ 錯誤（`U_LAND` 在而「重劃區地籍」缺 ⇒ `B2`；「重劃區地籍」有「是」而 `U_LAND` 缺 ⇒ `B3` 之註記靜默略之）——合原單 `R-5` ①「缺表者 ⇒ 三空」之字面，與「⛔ 靜默」之旨相左；實務上 tab1 於缺表者已列錯誤而停（`app.py:25783-25785`） | 照實呈（規格已定之形） |
| `7` | (a)·註 | `U_LAND` 缺「公私別」之欄 ⇒「該地號非公有地（U_LAND 公私別）」（碼以 `ow.get` 讀格·⛔ 例外 ⇒ ⛔ 入 `R-12`）；仍停止計算；`U_LAND` 缺「權利範圍分母」⇒ `R-11` 之錯誤 | 照實呈（原單 `R-2` ③ 之字面之果） |
| `8` | (c) | `k962_land_marks` 之直呼而 `U_LAND` 缺「段小段」⇒ `KeyError`（`A3c`）；`R-11` 之「⛔ 拋」之受詞為權利範圍；唯一之生產之呼叫者以 `R-12` 捕之（`B5`·`F30` `K19`） | — |
| `9` | (a)·註 | 角落：分子為文字 `"inf"` ⇒ 持分 `inf` ⇒ `min` 記 `1.0`；分母 `"inf"` ⇒ 非公有地；分母為布林 `TRUE` ⇒ 視為 `1`——皆合規格之字面；Excel 之數值格⛔ 存 `inf` | 照實呈 |
| `10` | (c)·註 | `hashlib.sha256` 在 `try` 之外（`:5221`）⇒ `f7_saved[1]` 非 bytes 者拋 `TypeError`（`B8`／`B9`）；⛔ 在 `R-12` 之列；tab1 恆存 `getvalue()` 之 bytes | — |

**審查者之壞之資料之實跑**（`F30` 之外·harvest `28046f2` 之 `app.py`）：(1) 公有者分子 `1`、分母空白 ⇒ `R-11` 之錯誤；(2) 分母 `−2` ⇒ 同；分母 `0`、分子 `−1`、分母 `"abc"`、分母為空字串 ⇒ 同；分子 `0` ⇒ 非公有地；`" 1 "`／`"4"` ⇒ `{200-1: 0.25}`；(3) `U_LAND` 缺「公私別」⇒ 非公有地（#7）；(4) `U_LAND` 在而「重劃區地籍」缺 ⇒ `errors []`·三空·存 `(h, 三空)`（#6）；私有者空白而公有者有效 ⇒ `{0.5}`；同一所有權人之重複列（有效者先／壞者先）⇒ 依去重之首列；壞檔 ⇒「地籍資料來源讀取失敗（BadZipFile）：File is not a zip file」；`U_LAND` 缺「段小段」⇒「地籍資料來源讀取失敗（KeyError）：'段小段'」；`k974_burden_scales` 之例外 ⇒ 上拋（⛔ 吞）；片重疊 ⇒ 錯誤·該面 `0.0`·明細空；`RA` 負、`RB` 正 ⇒ 面 `0.875`（＝ `0.5 × 1.75`）·明細唯 `RB`；整數座標之 `B ＝ A` ⇒ 比例 `0`·⛔ 錯誤；實座標之 `B ＝ A` ⇒ 上開 #1。審查者另實跑 `F30 selftest`／`wiring`、`F23 wiring`、`F24 wiring` 皆 `rc 0`·`stderr` `0` B；兩差異檔與 `git diff` 逐位同。
🔒 審查者自陳：其 `python -m py_compile app.py` 重寫已忽略之 `__pycache__/app.cpython-313.pyc`（`.gitignore:18`）；其後皆設 `PYTHONDONTWRITEBYTECODE=1`；追蹤檔恆乾淨。

## 六、設計說明（`R-11`〜`R-13`·補令一 `§三″`）

- **`R-11`**：去重之迴圈內，公有者以 `pd.to_numeric(…, errors='coerce')` 取分子、分母；`pd.isna(num) or pd.isna(den) or den <= 0 or num < 0` ⇒ 記 `bad_frac`、該所有權人⛔ 計；迴圈之後 `bad_frac` ⇒ 錯誤（字樣分二 f-string 書之·「缺漏或分母非正數」在一列）、`continue`。其位在「U_LAND 無對應資料」之後、「非公有地」之前。
- **`R-12`**：原單 `R-5` ① 之讀取與 `k962_land_marks` 之呼叫入 `try`（六列之縮排增四格·其文⛔ 改）；`except Exception as e` ⇒ 三空 ＋ 錯誤一則；`ss['f3_k962_marks_cache'] = (h, marks)` 在 `try` 之外（各支皆存）。
- **`R-13`**：比例之後（未勾新闢之支內）`if ratio < 0:` ⇒ 錯誤、`continue`。
- **`R-15`**：三函式之 docstring 之末各增 ``🔧 `W-G.9-385` 補令一（`R-1x`）`` 之一款；其文⛔ 含 `R-14` 之三字樣（保其恰 `1`）。
- **`§三-3` 之自查**：`F23 wiring`（`W7`／`W8`）、`F24 wiring`、`F25 wiring`、`F30 wiring`（`W1`／`W7`）與 `V-2` 之諸接線皆綠。

## 七、⛔ 辦之項

- 工項二″ 之 `push`、工項三″（塊 `K25`＋`K26`／`E28`＋`E29`／`P38` 之入典·`checkidx`／`gen_fa_index`）、工項四″（執行報告）、收工閘——皆⛔ 辦（停機）。諸塊之抽取與三簿之施後 blob 已於 `<O>` 對拍皆符（上開二之 `8″`）。
- 次之處置候發單側之裁（#1 之容差之定）；`hold/W-G.9-385p1-c2` 之碼可為其基（其餘皆合）。

## 八、`61` 呼叫之 `rc`／`stderr`／耗時／末列（前置 ＝ 工項一″ 之端；驗 ＝ `28046f2`）

並行：前置 `5`；驗 `4` ＋ `1`（`screenmerge run` 先起）；撰碼中之自跑另 `1`——同時 ≤ `6`。末列 ＝ `stdout` 之末一非空列。逾時或 `rc` ≠ 期者 `0` ⇒ 無重跑之趟。

| # | 呼叫 | 前置（`01ad480`）rc／stderr B／s | 前置之末列 | 驗（`28046f2`）rc／stderr B／s | 驗之末列 |
|---|---|---|---|---|---|
| `1` | `python verify/probes/probe_WG9385_k974.py selftest <repo>` | `1`／`0`／`4.3` | `⇒ 紅 ['K0']；rc 1` | `0`／`0`／`4.9` | `⇒ 紅 []；rc 0` |
| `2` | `python verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `1`／`0`／`15.7` | `⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W7']；rc 1` | `0`／`0`／`15.2` | `⇒ 紅 []；rc 0` |
| `3` | `python verify/probes/probe_WG9385_k974.py run <repo>` | `1`／`0`／`5.2` | `⇒ 紅 ['R0']；rc 1` | `0`／`0`／`320.5` | `⇒ 紅 []；rc 0` |
| `4` | `python verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` |
| `5` | `python verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`37.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`32.1` | `⇒ 紅 []；rc 0` |
| `6` | `python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`33.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`32.8` | `⇒ 紅 []；rc 0` |
| `7` | `python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`12.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`12.8` | `⇒ 紅 []；rc 0` |
| `8` | `python verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`4.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.2` | `⇒ 紅 []；rc 0` |
| `10` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`58.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`60.8` | `⇒ 紅 []；rc 0` |
| `11` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`25.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`27.5` | `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`46.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`49.1` | `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`4.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`4.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` |
| `15` | `python verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`3.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`3.2` | `⇒ 紅 []；rc 0` |
| `16` | `python verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`75.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`78.3` | `⇒ 紅 []；rc 0` |
| `17` | `python verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`581.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`559.1` | `⇒ 紅 []；rc 0` |
| `18` | `python verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`813.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`801.2` | `⇒ 紅 []；rc 0` |
| `19` | `python verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`24.1` | `⇒ 突變 8（另基準一）；紅 []；rc 0` | `0`／`0`／`22.8` | `⇒ 突變 8（另基準一）；紅 []；rc 0` |
| `20` | `python verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.3` | `⇒ 紅 []；rc 0` |
| `21` | `python verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`10.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`10.3` | `⇒ 紅 []；rc 0` |
| `22` | `python verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`169.2` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` | `0`／`0`／`158.9` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` |
| `23` | `python verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`503.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`477.9` | `⇒ 紅 []；rc 0` |
| `24` | `python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`5.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.6` | `⇒ 紅 []；rc 0` |
| `25` | `python verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`2064.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`2048.6` | `⇒ 紅 []；rc 0` |
| `26` | `python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`68.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`71.9` | `⇒ 紅 []；rc 0` |
| `27` | `python verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`4.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.6` | `⇒ 紅 []；rc 0` |
| `28` | `python verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`16.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`16.6` | `⇒ 紅 []；rc 0` |
| `29` | `python verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`42.6` | `⇒ rc 0（不符 0·器紅 0）` | `0`／`0`／`43.3` | `⇒ rc 0（不符 0·器紅 0）` |
| `30` | `python verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`5.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`5.1` | `⇒ 紅 []；rc 0` |
| `31` | `python verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`19.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`20.9` | `⇒ 紅 []；rc 0` |
| `32` | `python verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`48.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`50.8` | `⇒ 紅 []；rc 0` |
| `33` | `python verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`429.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`407.9` | `⇒ 紅 []；rc 0` |
| `34` | `python verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`30.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`30.9` | `⇒ 紅 []；rc 0` |
| `35` | `python verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`109.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`116.3` | `⇒ 紅 []；rc 0` |
| `36` | `python verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`26.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`27.5` | `⇒ 紅 []；rc 0` |
| `37` | `python verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`73.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`76.0` | `⇒ 紅 []；rc 0` |
| `38` | `python verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`52.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`54.1` | `⇒ 紅 []；rc 0` |
| `39` | `python verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`45.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`47.8` | `⇒ 紅 []；rc 0` |
| `40` | `python verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`224.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`222.6` | `⇒ 紅 []；rc 0` |
| `41` | `python verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.2` | `⇒ 紅 []；rc 0` |
| `42` | `python verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`31.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`31.8` | `⇒ 紅 []；rc 0` |
| `43` | `python verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`587.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`605.5` | `⇒ 紅 []；rc 0` |
| `44` | `python verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `45` | `python verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`3.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`3.4` | `⇒ 紅 []；rc 0` |
| `46` | `python verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`181.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`179.9` | `⇒ 紅 []；rc 0` |
| `47` | `python verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`417.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`432.8` | `⇒ 紅 []；rc 0` |
| `48` | `python verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.2` | `⇒ 紅 []；rc 0` |
| `49` | `python verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`418.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`418.7` | `⇒ 紅 []；rc 0` |
| `50` | `python verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`0.1` | `selftest 9/9 ⇒ ✅` | `0`／`0`／`0.1` | `selftest 9/9 ⇒ ✅` |
| `51` | `python verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`0.1` | `selftest 13/13 ⇒ ✅` | `0`／`0`／`0.1` | `selftest 13/13 ⇒ ✅` |
| `52` | `python verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`7.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`7.7` | `⇒ 紅 []；rc 0` |
| `53` | `python verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`4.4` | `ε ＝ 0.0002｜rc 0` | `0`／`0`／`4.2` | `ε ＝ 0.0002｜rc 0` |
| `54` | `python verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`32.2` | `紅項 [] 器紅 0` | `0`／`0`／`33.2` | `紅項 [] 器紅 0` |
| `55` | `python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`429.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`430.8` | `⇒ 紅 []；rc 0` |
| `56` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>\k6s3_post_35.json` | `0`／`0`／`247.8` | `{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4…` | `0`／`0`／`239.3` | `{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4…` |
| `57` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>\k6s3_post_00.json` | `0`／`0`／`176.3` | `{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4…` | `0`／`0`／`174.4` | `{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4…` |
| `58` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>\f8_post_35.json` | `0`／`0`／`235.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`218.8` | `⇒ 紅 []；rc 0` |
| `59` | `python verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>\f8_post_00.json` | `0`／`0`／`170.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`156.2` | `⇒ 紅 []；rc 0` |
| `60` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>\parity35_post.json` | `0`／`0`／`549.5` | `⇒ rc 0（不符 0 項）` | `0`／`0`／`542.3` | `⇒ rc 0（不符 0 項）` |
| `61` | `python verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>\parity00_post.json` | `0`／`0`／`390.5` | `⇒ rc 0（不符 0 項）` | `0`／`0`／`378.7` | `⇒ rc 0（不符 0 項）` |

耗時之和：前置 `61` 呼叫 `9611.8` s（其中 `55` 呼叫 `7841.9` s）；驗 `61` 呼叫 `9814.0` s（其中 `55` 呼叫 `8104.3` s）。stderr 合計：前置 `0` B；驗 `0` B。
