# W-P.007　附表 13 之版面照手冊範本（KL 2026-10-31 08:32·17:14）

- **題**：依 KL 2026-10-31 08:32（`出圖線/KL答覆/2026-10-31_0832.md`·各附表之版面一律照手冊範本）、17:14（`出圖線/KL答覆/2026-10-31_1714.md`·附表 13、24 內容定版 ⇒ 次辦版面），將**附表 13 重劃前後土地分配清冊**之版面照手冊 PDF 第 88 頁（`參考/手冊附表頁/附表13_重劃前後土地分配清冊_手冊PDF第88頁.png`）於 Excel 重畫。**附表 24 ⛔ 本單**（KL 之 Excel 範本去識別未盡·`出圖線/交接.md` 第六節 18:24·俟監看窗換檔後另單）。
- **範圍**：**改** `plots/post_tables.py`（唯附表 13 之版面）、`verify/plots/check_W-P006.py`（唯附表 13 之讀取之位置）；**新增** `verify/plots/check_W-P007.py`、`verify/plots/mutate_W-P007.py`、`verify/plots/preview_W-P007.py`、`docs/出圖/W-P.007_附表13版面.md`；⛔ 改他檔（含 `plots/alloc_state.py`、`plots/post_maps.py`、`plots/prelim_maps.py`、`verify/plots/mutate_W-P006.py`、`verify/plots/preview_W-P006*.py`·唯 `import` 或呼叫）；⛔ 改 `requirements.txt`；⛔ 新套件。
- **對土地的影響**：無。表之內容（值、欄名、表之分法、附表 24）與 `W-P.006_補令一` 定版者逐值同（量測 L0、L1 證之）。
- **授權（逐字）**：
  - KL 2026-10-23 17:48「圖就出DXF或DWG(…)即可，所有的標題及排版由使用者編輯。還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」（README 第一節）。
  - KL 2026-10-31 08:14「…但是格式問題（不限於附表24），有辦法做到與手冊範本附表格是一致?」；08:32「我只有部分我之前同是做的附表excel檔，其餘附表沒有excel檔的就參考上傳手冊pdf檔，但pdf檔應該都有在市地重劃專案資料夾內了」；17:14「一 是、二 乙、三 是、四 是、五 是」。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `9fd34275770b7fc53103b9eb42ba21925f823f9a`；`wip/plots` ＝ `15935e2d608def08db9bf3dc69fe0b1a75e5981e`（已含 `9fd3427` ⇒ 工項 1 之合併應為「Already up to date」；主線若前進則必有合併之 commit）。
- **側支**：`verify/W-P.007-table13-layout`（自 `wip/plots` 出）。單名與側支名經 `git grep -F` 證未占用（佇列唯本線之記事提及、`15935e2` 無、遠端分支無）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具·核心線 `order` ＝ `W-G.9-396_規格單`）。

## §一　所據

1. **手冊**：PDF 第 88 頁（印刷頁 78）之附表 13 表樣（監看窗 08:32 自 KL 所附之 PDF 取出·200 dpi）；文字版 `參考/市地重劃作業手冊.txt` 第 2769 列（欄名之序·同 W-P.006 定版之欄名）。
2. **KL 之答之讀**（監看窗 08:32 之讀第 1、3 點·入典以 KL 逐字為準）：版面照手冊範本（格線、欄位之編排、合併、直書、橫式紙張與頁首頁尾）；欄名仍依手冊；無 Excel 範本者以手冊之原頁重畫；驗之法須含「與範本逐格對照」（格線、合併範圍、欄名）。
3. **發單端自範本量得**（2000 像素寬之圖）：
   - 縱線 25 條之 x：135、198、262、325、388、451、515、588、662、730、830、943、997、1051、1105、1159、1213、1335、1408、1482、1566、1650、1708、1767、1865 ⇒ 24 欄（同 W-P.006 之 24 欄·欄之序不變）；欄寬取像素 ÷ 7。
   - 框外：左上「附表 13 重劃前後土地分配清冊」、右上「共＿冊第＿冊第＿頁」；框內第一列為題。
   - 所有權人區（四列）：左之標籤二格（「土地所有權人（首列登記人）姓名／國民身分證統一編號」二行合一格；「管理人姓名／國民身分證統一編號」二行合一格），其右之值格各分二列（姓名、統編），至「評定單價」欄止（588〜830 ＝ 第 8〜10 欄）；「住址」直書一格跨四列（第 11 欄）；住址之值格跨第 12〜24 欄、分上（所有權人）下（管理人）二格。
   - 表頭三列：同 W-P.006（「重劃前土地情形」1〜10 欄、「扣除各項負擔後應分配面積」第 11 欄跨三列、「重劃後土地情形」12〜23 欄、「備註」第 24 欄跨三列）；直書者：鄉鎮市區、小段、地號、登記面積、取配面積、持分比率、使用分區、小段、地號、面積、持分比率、建號、二「姓名」、備註、住址。
   - 資料列 5 列；附註緊接框下；簽欄（日期、承辦、股長、科長、局(處)長）於 x ≈ 150、463、805、1120、1430 ⇒ 第 1、6、10、14、19 欄。
   - 外框之線粗於內線。
4. **既有之函式**（唯讀·`import`）：同 `W-P.006_補令一`（`plots/prelim_maps.py`、`plots/owner_index.py`、`plots/post_maps.py`）。
5. **環境之實測**：openpyxl 讀回 xlsx 時，以合併之首格之框線重設該合併範圍之他格 ⇒ 合併範圍內之框線⛔ 以 openpyxl 量之；`check_W-P007` L5 逕讀 xlsx 之 XML（`xl/styles.xml` 之 `borders`／`cellXfs` 與各表之 `<c s=…>`）。

## §二　規格

1. **改 `plots/post_tables.py`**：逐位元組 ＝ 附錄丁。所改唯附表 13 之版面：
   - 列 1 表名（框外·粗體）、列 2 冊頁（S2:X2·靠右）、列 3 題（A3:X3·框內）；
   - 列 4〜7：標籤 A4:G5、A6:G7（二行·分散對齊）；值 H4:J4（首列登記人姓名）、H5:J5（統編）、L4:X5（住址）、H6:J6（管理人姓名）、H7:J7（統編）、L6:X7（管理人之住址·資料所無·留空）；「住址」K4:K7（直書）；
   - 列 8〜10 表頭（欄名與合併同 W-P.006·下移三列；直書之格見 `A13_VERT`；「重劃前土地情形」「重劃後土地情形」分散對齊）；
   - 列 11 起資料：每表 max(列數, 5) 列（不足者留空格·有框線）；備註之字多者其列加高；
   - 框（第 3 列至資料末列）：每格細線、外框粗線；附註於框下一列、簽欄於其次列（A、F、J、N、S 欄）；
   - 欄寬（`A13_WIDTH`）、列高（`A13_HEIGHT`、資料列 38 點）；A4 橫式、寬一頁、每頁重出第 1〜10 列。
   - 表之內容（各格之值與數字格式、欄名、表之分法、首列登記人、縣有之表）與附表 24：**⛔ 變**（發單端以舊版〔`15935e2`〕之輸出比對：二退縮皆同·印出之摘要逐字同）。
2. **改 `verify/plots/check_W-P006.py`**：逐位元組 ＝ 附錄戊。唯附表 13 之讀取之位置（題第 3 列、表頭第 8〜10 列、資料第 11 列起、首列登記人之格、附註於 `11 ＋ max(列數, 5)`、簽欄於其次列之 A、F、J、N、S 欄）；V0〜V6 所量之內容⛔ 變。
3. **新增 `verify/plots/check_W-P007.py`**：逐位元組 ＝ 附錄甲。L0 附表 24 與舊版逐格同；L1 附表 13 之表名、首列登記人、資料列（值與格式）與舊版同；L2 合併 ＝ 範本；L3 字（表名、冊頁、題、各標籤、附註、簽欄、列數）＝ 範本；L4 直書 ＝ 範本；L5 格線（XML）；L6 欄寬之比（差 ≤ 0.004）與紙張。範本之值寫於該檔（`SPEC_*`·⛔ 自 `plots/` 取）。
4. **新增 `verify/plots/mutate_W-P007.py`**：逐位元組 ＝ 附錄乙（Ⓐ 住址未跨四列、Ⓑ 欄名改用他名、Ⓒ 鄉鎮市區漏直書、Ⓓ 外框未加粗、Ⓔ 首列登記人之姓名與統編錯格）。
5. **新增 `verify/plots/preview_W-P007.py`**：逐位元組 ＝ 附錄丙（依 Excel 之欄寬、列高、合併、直書、框線繪二表·`preview_W-P006.py`、`check_W-P007.py` 唯 `import`）。
6. **新增 `docs/出圖/W-P.007_附表13版面.md`**：逐位元組 ＝ 附錄己。
7. 發單端之原型（暫存·⛔ 入倉·於 `15935e2` 之上·venv＋`numpy<2.3`〔2.2.6〕·openpyxl 3.1.5·matplotlib 3.11.2）實得：
   - `alloc_state`、`post_maps`：同 `W-P.006_補令一`。
   - `post_tables`：0 m「附表 13 戶 33（有分配地 16、取配面積可填 14、現金補償 0）＋縣有 11；附表 24 張 29（Σa 可填 14）」；3.5 m「…附表 24 張 28（Σa 可填 14）」——與舊版之印出（除「輸出」列）逐字同。
   - `check_W-P007`（新版 vs 舊版之輸出）14/14；**對照組**（舊版之輸出當新版量之）：二退縮 L1〜L6 皆紅、L0 綠。
   - `check_W-P006` 14/14（約 2 分）；**對照組**（舊版之輸出以新 `check_W-P006` 量之）：V1、V2、V3 紅。
   - `mutate_W-P007`（約 1 分半）：成果綠；Ⓐ 紅 L2、Ⓑ 紅 L3、Ⓒ 紅 L4、Ⓓ 紅 L5、Ⓔ 紅 L1。
   - `mutate_W-P006`（約 7 分）：成果綠；Ⓐ〜Ⓙ 皆紅（所紅之項同 `W-P.006_補令一` §二 6）。
   - 預覽 `W-P.007_附表13版面_退縮0m.png` sha256 `eaa2985be2afbe1405f219dd5896738b48e4c4ae8ee1fc709307ae39ad1493c2`、`_退縮3.5m.png` `a9b5f15ff69b2c1eafc06c004f6c25027455e32eb1076a80a063785ffcf102a6`（二表皆「歸戶號29」「縣有（抵費地）」；他環境之字形或致 sha256 異·記之、⛔ 停）。
   - 另以試算表軟體（LibreOffice）開啟、轉 PDF 目視：直書、合併、分散對齊、框線皆如範本（發單端之對照圖 `出圖線/待KL/W-P.007_原型預覽_附表13版面對照.png`）。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.007-table13-layout`；`git merge --no-edit origin/wip/s1-endpart`（記其結果；有衝突即停機）。
2. **程式**：§二 1〜6。附錄之取用法：自本單擷取該附錄之開欄（甲〜戊為三個反引號加 `python`；己為四個反引號加 `markdown`）與其閉欄（同數之反引號）間之文字，末尾一換行；bytes 與 sha256 須合：
   - 甲 `verify/plots/check_W-P007.py`：13437 bytes·`b9ac2f5cad4c077ffd79e12178a876ee979c45df5c0e9bd45d91affa43b0fc64`
   - 乙 `verify/plots/mutate_W-P007.py`：4034 bytes·`c856e6963228226757f60ee80805f1f8a8d94bf8794bd9d4c79970cfbb7ee57d`
   - 丙 `verify/plots/preview_W-P007.py`：6732 bytes·`298dcceaad1c963a5ded959c8673b8a7adc3c5639d40372bc58b9bebb3dc95f7`
   - 丁 `plots/post_tables.py`：31432 bytes·`60c01cf0043c299544f508bec3ebe3bde7f25c499ac7e504a7e59ebd01100d67`
   - 戊 `verify/plots/check_W-P006.py`：29461 bytes·`a9a9e535da58ad57679b06a001e6d74a12096304ab8c273a72a412a9d0ad9dfe`
   - 己 `docs/出圖/W-P.007_附表13版面.md`：2838 bytes·`9da8bf40e6c1d68a54b19548224778fff7e232fd3e3a2f6ba9bdc1edcd1368d2`
   不合即停機上呈；⛔ 改一字。`python -m py_compile` 五 `.py` 皆過。
3. **量測**（`<py>` ＝ venv 之直譯器）：
   - `<py> plots/fetch_moedict.py <M>`；`<py> plots/prelim_maps.py --out <P> --moedict <M>/dict-revised.json`；
   - `<py> plots/alloc_state.py --out <O> --setback 0 --setback 3.5`；二退縮各 `<py> plots/post_maps.py --state <O>/配地結果_退縮<t>m.json --pre-dxf <P>/重劃前圖.dxf --moedict <M>/dict-revised.json --out <O>`；
   - **舊版之輸出**：`git worktree add <W> 15935e2`，複 `<O>` 之全部至 `<OLD>`，二退縮各 `cd <W> && <py> plots/post_tables.py --state <O>/配地結果_退縮<t>m.json --moedict <M>/dict-revised.json --out <OLD>`；
   - 二退縮各 `<py> plots/post_tables.py --state <O>/配地結果_退縮<t>m.json --moedict <M>/dict-revised.json --out <O>`（印如 §二 7·與舊版之印出除「輸出」列逐字同）；
   - `<py> verify/plots/check_W-P007.py <O> <OLD> 0 3.5` ⇒ 14 項皆 PASS、結束碼 0；
   - `<py> verify/plots/check_W-P006.py <O> <P> <M>/dict-revised.json 0 3.5` ⇒ 14 項皆 PASS；
   - **對照組**：`check_W-P007.py <OLD> <OLD> 0 3.5` 須紅（L1〜L6）；`<OLD>` 之副本以新 `check_W-P006` 量之須紅（記所紅之項）；
   - 另照舊：`check_W-P005`（18/18）、`check_W-P001`（12/12）、`check_W-P002`（8/8）、`check_W-P003`（8/8）、`check_W-P004`（8/8）。
4. **故意錯誤之測**：`<py> verify/plots/mutate_W-P007.py <O> <OLD> <M>/dict-revised.json <拋棄式之工作目錄>` ⇒ 成果綠、Ⓐ〜Ⓔ 皆紅、結束碼 0；`<py> verify/plots/mutate_W-P006.py <O> <P> <M>/dict-revised.json <另一拋棄式目錄>` ⇒ 成果綠、Ⓐ〜Ⓙ 皆紅（Bash 逾時放寬）。
5. **差異閘**（README 第四節）：`git diff --name-status <實際併入之主線之 sha（應為 9fd3427…）> <側支之端>` 每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status 15935e2 <側支之端>` 唯 `M plots/post_tables.py`、`M verify/plots/check_W-P006.py`、`A verify/plots/check_W-P007.py`、`A verify/plots/mutate_W-P007.py`、`A verify/plots/preview_W-P007.py`、`A docs/出圖/W-P.007_附表13版面.md`；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：`<py> verify/plots/preview_W-P007.py <O> <PNG 目錄> 0 3.5`，其二輸出入佇列之 `出圖線/成果/`（sha256 與 §二 7 不同者記之、⛔ 停）。
7. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
8. **回報**：`出圖線/reports/W-P.007_回報.md`（各工項之實測、量測之全輸出、對照組、故意錯誤之表、差異閘、合併之結果、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲〜己之 bytes 或 sha256 不合；或 L0〜L6、V0〜V6 於成果不過而非程式之誤；或 §二 7 之實得不合（主線前進致配地變者亦停·記其差）。
3. `plots/alloc_state.py`、`plots/post_maps.py` 或 `plots/post_tables.py` 報 `SourceError` 或配地流程之 `RuntimeError`——⛔ 自擬填法、⛔ 設 `WV_BAKE`。
4. 須改任何他檔、或須新套件（numpy 之版本唯限於倉外之 venv）。
5. 任一版面或內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P007.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.007 之量測（單 §三 3）：附表 13 重劃前後土地分配清冊之版面照手冊範本（KL 2026-10-31 08:32）。
獨立於 plots/：⛔ import 之；版面之期望（合併、字、直書、格線、欄寬之比）由發單端依
參考/手冊附表頁/附表13_重劃前後土地分配清冊_手冊PDF第88頁.png 量得、逐格寫於本檔（SPEC_*）；
內容之期望 ＝ 舊版（W-P.006_補令一·KL 2026-10-31 17:14 定版）之輸出——表之內容逐值⛔ 變。

命令列：python verify/plots/check_W-P007.py <成果目錄> <舊版成果目錄> <退縮…>
  <成果目錄>     ＝ 新版 plots/post_tables.py 之輸出（附表13_…、附表24_…_退縮<t>m.xlsx）。
  <舊版成果目錄> ＝ 舊版（wip/plots 15935e2）之 plots/post_tables.py 以同一配地結果之輸出。
各退縮印 L0〜L6 之 PASS／FAIL；全 PASS 者結束碼 0。
"""
import os
import sys

FMT = {"a13": "附表13_重劃前後土地分配清冊_退縮{}m.xlsx", "a24": "附表24_土地分配計算表_退縮{}m.xlsx"}
NCOL = 24
FIRST = 11
MIN_ROWS = 5
OLD_FIRST = 8                 # 舊版之資料首列
OLD_OWNER = ((3, 4), (3, 9), (3, 13), (4, 4), (4, 9))   # 舊版之首列登記人 姓名、統編、住址、管理人姓名、統編
OLD_NOTE_GAP, OLD_SIGN_GAP = 2, 4
OLD_SIGN_COL = (1, 5, 9, 13, 17)

# ---- 手冊第 88 頁之範本（發單端量得）
SPEC_CAPTION = ((1, 1), "附表 13 重劃前後土地分配清冊")
SPEC_BOOK = ((2, 19, 2, 24), "共　　冊　第　　冊　第　　頁")
SPEC_TITLE = ((3, 1, 3, 24), "○○縣(市)第○○期○○○○市地重劃區重劃前後土地分配清冊")
SPEC_LABEL = (
    ((4, 1, 5, 7), "土地所有權人（首列登記人）姓名\n國民身分證統一編號"),
    ((6, 1, 7, 7), "管理人姓名\n國民身分證統一編號"),
    ((4, 11, 7, 11), "住址"),
    ((8, 1, 8, 10), "重劃前土地情形"), ((8, 11, 10, 11), "扣除各項負擔後應分配面積(㎡)"),
    ((8, 12, 8, 23), "重劃後土地情形"), ((8, 24, 10, 24), "備註"),
    ((9, 1, 10, 1), "鄉鎮市區"), ((9, 2, 10, 2), "段"), ((9, 3, 10, 3), "小段"), ((9, 4, 10, 4), "地號"),
    ((9, 5, 10, 5), "登記面積(㎡)"), ((9, 6, 10, 6), "取配面積(㎡)"), ((9, 7, 9, 8), "所有權人"),
    ((10, 7, 10, 7), "姓名"), ((10, 8, 10, 8), "國民身分證統一編號"), ((9, 9, 10, 9), "持分比率"),
    ((9, 10, 10, 10), "評定單價(元／㎡)"),
    ((9, 12, 10, 12), "使用分區"), ((9, 13, 10, 13), "段"), ((9, 14, 10, 14), "小段"), ((9, 15, 10, 15), "地號"),
    ((9, 16, 10, 16), "面積(㎡)"), ((9, 17, 10, 17), "評定單價(元／㎡)"), ((9, 18, 9, 19), "預計繳領差額地價"),
    ((10, 18, 10, 18), "繳（元）"), ((10, 19, 10, 19), "領（元）"), ((9, 20, 9, 21), "所有權人"),
    ((10, 20, 10, 20), "姓名"), ((10, 21, 10, 21), "國民身分證統一編號"), ((9, 22, 10, 22), "持分比率"),
    ((9, 23, 10, 23), "建號"),
)
SPEC_VALUE = ((4, 8, 4, 10), (5, 8, 5, 10), (4, 12, 5, 24), (6, 8, 6, 10), (7, 8, 7, 10), (6, 12, 7, 24))
SPEC_VERT = {(4, 11), (8, 24), (9, 1), (9, 3), (9, 4), (9, 5), (9, 6), (9, 9), (9, 12), (9, 14), (9, 15),
             (9, 16), (9, 22), (9, 23), (10, 7), (10, 20)}
# 手冊第 88 頁（2000 像素寬之圖）之 25 條縱線之 x
SPEC_X = (135, 198, 262, 325, 388, 451, 515, 588, 662, 730, 830, 943, 997, 1051, 1105, 1159, 1213, 1335, 1408,
          1482, 1566, 1650, 1708, 1767, 1865)
TOL_W = 0.004                 # 各欄寬占全寬之比之容差
NOTE = "附註：重劃後分配面積與實地指界交接土地面積如有不符，應以地政機關實際登記面積為準。"
SIGN = ("日期：", "承辦：", "股長：", "科長：", "局(處)長：")
SIGN_COL = (1, 6, 10, 14, 19)


def load(out, old, tag):
    import openpyxl
    p = {k: os.path.join(out, v.format(tag)) for k, v in FMT.items()}
    q = {k: os.path.join(old, v.format(tag)) for k, v in FMT.items()}
    new = {k: openpyxl.load_workbook(v) for k, v in p.items()}
    new["raw13"] = raw_borders(p["a13"])
    return new, {k: openpyxl.load_workbook(v) for k, v in q.items()}


def data_rows(ws, first, stop=None):
    """first 列起之資料列（值與格式）：舊版至首一全空之列止；新版至框末列（stop）止、去其末之全空列。"""
    out, r = [], first
    while (r <= stop) if stop else any(ws.cell(r, c).value is not None for c in range(1, NCOL + 1)):
        out.append(tuple((ws.cell(r, c).value, ws.cell(r, c).number_format) for c in range(1, NCOL + 1)))
        r += 1
    while out and all(v is None for v, _ in out[-1]):
        out.pop()
    return out


def last_row(ws):
    """框之末列 ＝ 附註之上一列。"""
    hit = [r for r in range(FIRST, ws.max_row + 1) if ws.cell(r, 1).value == NOTE]
    if len(hit) != 1:
        raise ValueError(f"{ws.title} 之附註 {len(hit)} 處")
    return hit[0] - 1


def raw_borders(path):
    """⇒ {表名: {(列, 欄): (左, 右, 上, 下)}}：逕讀 xlsx 之 XML（openpyxl 讀回時以合併之首格重設其餘格之框線，
    故⛔ 用之量合併範圍內之線）。"""
    import re
    import zipfile
    from xml.etree import ElementTree as ET
    from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
          "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    z = zipfile.ZipFile(path)
    st = ET.fromstring(z.read("xl/styles.xml"))
    borders = []
    for b in st.find("m:borders", ns):
        borders.append(tuple((b.find(f"m:{k}", ns).get("style") if b.find(f"m:{k}", ns) is not None else None)
                             for k in ("left", "right", "top", "bottom")))
    xf = [int(x.get("borderId", 0)) for x in st.find("m:cellXfs", ns)]
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    out = {}
    for sh in ET.fromstring(z.read("xl/workbook.xml")).find("m:sheets", ns):
        tgt = rels[sh.get(f"{{{ns['r']}}}id")]
        tgt = re.sub(r"^/?(xl/)?", "xl/", tgt)
        cells = {}
        for c in ET.fromstring(z.read(tgt)).iter(f"{{{ns['m']}}}c"):
            col, row = coordinate_from_string(c.get("r"))
            cells[(row, column_index_from_string(col))] = borders[xf[int(c.get("s", 0))]]
        out[sh.get("name")] = cells
    return out


def merges(ws):
    return {(m.min_row, m.min_col, m.max_row, m.max_col) for m in ws.merged_cells.ranges}


# ---------------------------------------------------------------- 量測
def l0(new, old):
    """附表 24：與舊版逐格同（表名、值、格式、合併）。"""
    bad = []
    a, b = new["a24"], old["a24"]
    if a.sheetnames != b.sheetnames:
        return [f"附表 24 之表名 {len(a.sheetnames)}／{len(b.sheetnames)}"]
    for x, y in zip(a, b):
        if merges(x) != merges(y) or (x.max_row, x.max_column) != (y.max_row, y.max_column):
            bad.append(f"附表 24 {x.title} 之合併或範圍")
            continue
        for r in range(1, x.max_row + 1):
            for c in range(1, x.max_column + 1):
                u, v = x.cell(r, c), y.cell(r, c)
                if (u.value, u.number_format) != (v.value, v.number_format):
                    bad.append(f"附表 24 {x.title} {u.coordinate}")
    return bad


def l1(new, old):
    """附表 13：表名、首列登記人五值、資料列（24 欄之值與格式）、資料列外之格皆與舊版同（唯位置依範本）。"""
    bad = []
    a, b = new["a13"], old["a13"]
    if a.sheetnames != b.sheetnames:
        return [f"附表 13 之表名 {a.sheetnames[:3]}…／{b.sheetnames[:3]}…"]
    for x, y in zip(a, b):
        got = tuple(x.cell(r, c).value for r, c, _, _ in SPEC_VALUE[:5])
        want = tuple(y.cell(r, c).value for r, c in OLD_OWNER)
        if got != want or x.cell(SPEC_VALUE[5][0], SPEC_VALUE[5][1]).value is not None:
            bad.append(f"{x.title} 之首列登記人 {got}／{want}")
        dn, do = data_rows(x, FIRST, last_row(x)), data_rows(y, OLD_FIRST)
        if dn != do:
            bad.append(f"{x.title} 之資料列（{len(dn)}／{len(do)}）")
        if y.cell(OLD_FIRST + len(do) + OLD_NOTE_GAP - 1, 1).value != NOTE or \
                tuple(y.cell(OLD_FIRST + len(do) + OLD_SIGN_GAP - 1, c).value for c in OLD_SIGN_COL) != SIGN:
            bad.append(f"{y.title} 之舊版之附註或簽欄不在其位（舊版之讀法不合）")
    return bad


def l2(new, old):
    """合併範圍 ＝ 範本（冊頁、題、標籤、所有權人之值格；資料列無合併）。"""
    bad = []
    want = {m for m in {SPEC_BOOK[0], SPEC_TITLE[0]} | {m for m, _ in SPEC_LABEL} | set(SPEC_VALUE)
            if m[:2] != m[2:]}
    for ws in new["a13"]:
        got = merges(ws)
        if got != want:
            bad.append(f"{ws.title} 之合併 多 {sorted(got - want)[:3]} 少 {sorted(want - got)[:3]}")
    return bad


def l3(new, old):
    """字：表名、冊頁、題、各標籤、附註（緊接框下）、簽欄（附註之下一列·五處）；資料列數 ＝ max(列數, 5)。"""
    bad = []
    for ws in new["a13"]:
        (r, c), t = SPEC_CAPTION
        if ws.cell(r, c).value != t:
            bad.append(f"{ws.title} 之表名")
        for (r1, c1, _, _), t in (SPEC_BOOK, SPEC_TITLE) + SPEC_LABEL:
            if ws.cell(r1, c1).value != t:
                bad.append(f"{ws.title} {ws.cell(r1, c1).coordinate} {ws.cell(r1, c1).value!r}≠{t!r}")
        try:
            last = last_row(ws)
        except ValueError as ex:
            bad.append(str(ex))
            continue
        n = len(data_rows(ws, FIRST, last))
        if last != FIRST + max(n, MIN_ROWS) - 1:
            bad.append(f"{ws.title} 之框末列 {last}（資料 {n} 列）")
        if tuple(ws.cell(last + 2, c).value for c in SIGN_COL) != SIGN:
            bad.append(f"{ws.title} 之簽欄")
        for r in range(FIRST + n, last + 1):
            if any(ws.cell(r, c).value is not None for c in range(1, NCOL + 1)):
                bad.append(f"{ws.title} 列 {r} 非空")
    return bad


def l4(new, old):
    """直書之格 ＝ 範本（text_rotation 255）；他格皆非直書。"""
    bad = []
    for ws in new["a13"]:
        got = {(cell.row, cell.column) for row in ws.iter_rows() for cell in row
               if cell.alignment is not None and cell.alignment.text_rotation == 255}
        if got != SPEC_VERT:
            bad.append(f"{ws.title} 之直書 多 {sorted(got - SPEC_VERT)[:3]} 少 {sorted(SPEC_VERT - got)[:3]}")
    return bad


def l5(new, old):
    """格線（逕讀 XML）：框內（第 3 列至框末列·1〜24 欄）每格四邊有線、外框粗線；框外（第 1、2 列、附註與簽欄）無線。"""
    bad = []
    for ws in new["a13"]:
        raw = new["raw13"][ws.title]
        last = last_row(ws)
        miss, outer = 0, 0
        for r in range(3, last + 1):
            for c in range(1, NCOL + 1):
                lt, rt, tp, bt = raw.get((r, c), (None,) * 4)
                if None in (lt, rt, tp, bt):
                    miss += 1
                if (c == 1 and lt != "medium") or (c == NCOL and rt != "medium") or \
                        (r == 3 and tp != "medium") or (r == last and bt != "medium"):
                    outer += 1
        for r in (1, 2, last + 1, last + 2):
            for c in range(1, NCOL + 1):
                if any(x is not None for x in raw.get((r, c), (None,) * 4)):
                    miss += 1
        if miss or outer:
            bad.append(f"{ws.title} 之格線 缺／多 {miss}、外框 {outer}")
    return bad


def l6(new, old):
    """欄寬之比 ＝ 範本（各欄占全寬之比差 ≤ 0.004）；A4 橫式、每頁重出 1〜10 列、寬一頁。"""
    from openpyxl.utils import get_column_letter
    bad = []
    px = [b - a for a, b in zip(SPEC_X, SPEC_X[1:])]
    for ws in new["a13"]:
        w = [ws.column_dimensions[get_column_letter(c)].width for c in range(1, NCOL + 1)]
        if any(x is None or x <= 0 for x in w):
            bad.append(f"{ws.title} 之欄寬未設")
            continue
        d = max(abs(x / sum(w) - y / sum(px)) for x, y in zip(w, px))
        if d > TOL_W:
            bad.append(f"{ws.title} 之欄寬之比差 {d:.4f}")
        ps = ws.page_setup
        if (ps.orientation, str(ps.paperSize), str(ws.print_title_rows).replace("$", ""), ps.fitToWidth) != \
                ("landscape", "9", "1:10", 1):
            bad.append(f"{ws.title} 之紙張 {ps.orientation} {ps.paperSize} {ws.print_title_rows} {ps.fitToWidth}")
    return bad


def run(fn, *a):
    try:
        return fn(*a)
    except Exception as ex:  # noqa: BLE001
        return [f"量測中止：{type(ex).__name__}: {ex}"]


def main(argv):
    out, old, tags = argv[0], argv[1], argv[2:]
    ok = True
    for tag in tags:
        tag = f"{float(tag):g}"
        new, ref = load(out, old, tag)
        for name, fn in (("L0", l0), ("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4), ("L5", l5), ("L6", l6)):
            bad = run(fn, new, ref)
            ok &= not bad
            print(f"退縮 {tag} m {name} {'PASS' if not bad else 'FAIL'}" + ("" if not bad else "：" + "；".join(bad[:4])))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄乙　`verify/plots/mutate_W-P007.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.007 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓔ 共 5 種變異體須各紅（量測 ＝ check_W-P007.py 之 L0〜L6）。

命令列：python verify/plots/mutate_W-P007.py <成果目錄> <舊版成果目錄> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py、plots/post_maps.py、plots/post_tables.py 之 --out（⛔ 改之）。
  唯驗退縮 3.5 m。各變異體 ＝ plots/ 之複本（於工作目錄）之 post_tables.py 改一處之字（MUTANTS）後，以子行程重出
  附表 13、24 於工作目錄，再以 check_W-P007 對舊版成果量之。
結束碼：成果綠且 5 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P007", os.path.join(HERE, "check_W-P007.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"
STATE, MAP = "配地結果_退縮{}m.json", "地號對照表_退縮{}m.xlsx"

MUTANTS = [   # (名, 說明, 原字, 改字)
    ("Ⓐ", "住址之標籤未跨四列", '(4, 11, 7, 11, "住址")', '(4, 11, 5, 11, "住址")'),
    ("Ⓑ", "欄名改用他名（取配面積→分配面積）", '(9, 6, 10, 6, "取配面積(㎡)")', '(9, 6, 10, 6, "分配面積(㎡)")'),
    ("Ⓒ", "鄉鎮市區漏直書", "A13_VERT = ((4, 11), (8, 24), (9, 1), (9, 3),", "A13_VERT = ((4, 11), (8, 24), (9, 3),"),
    ("Ⓓ", "外框未加粗", "Border(left=thick if c == 1 else thin", "Border(left=thin if c == 1 else thin"),
    ("Ⓔ", "首列登記人之姓名與統編錯格", "    (4, 8, 4, 10), (5, 8, 5, 10), (4, 12, 5, 24),",
     "    (5, 8, 5, 10), (4, 8, 4, 10), (4, 12, 5, 24),"),
]
CHECKS = (("L0", chk.l0), ("L1", chk.l1), ("L2", chk.l2), ("L3", chk.l3), ("L4", chk.l4), ("L5", chk.l5),
          ("L6", chk.l6))


def _measure(out, old):
    new, ref = chk.load(out, old, TAG)
    return [name for name, fn in CHECKS if chk.run(fn, new, ref)]


def main(argv):
    out, old, moe, work = argv
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(work)
    ok = True
    base = _measure(out, old)
    print(f"成果：{'綠' if not base else '紅 ' + '、'.join(base)}")
    ok &= not base
    src = open(os.path.join(REPO, "plots", "post_tables.py"), encoding="utf-8").read()
    for name, desc, a, b in MUTANTS:
        if src.count(a) != 1:
            print(f"{name}（{desc}）：原字不唯一或不在（{src.count(a)}）")
            ok = False
            continue
        d = os.path.join(work, name)
        pdir = os.path.join(d, "plots")
        shutil.copytree(os.path.join(REPO, "plots"), pdir, ignore=shutil.ignore_patterns("__pycache__"))
        with open(os.path.join(pdir, "post_tables.py"), "w", encoding="utf-8") as f:
            f.write(src.replace(a, b))
        o = os.path.join(d, "out")
        os.makedirs(o)
        for k in (STATE, MAP):
            shutil.copy(os.path.join(out, k.format(TAG)), o)
        # 複本之 plots/ 不在倉內 ⇒ prelim_maps 之 REPO 指向複本之上層；以符號連結補 data／verify（唯讀）
        for sub in ("data", "verify"):
            os.symlink(os.path.join(REPO, sub), os.path.join(d, sub))
        r = subprocess.run([sys.executable, os.path.join(pdir, "post_tables.py"), "--state",
                            os.path.join(o, STATE.format(TAG)), "--moedict", moe, "--out", o],
                           capture_output=True, text=True, encoding="utf-8")
        red = ["出表即停"] if r.returncode != 0 else _measure(o, old)
        print(f"{name}（{desc}）：{'紅 ' + '、'.join(red) if red else '綠（未捕）'}")
        ok &= bool(red)
    print("結論：" + ("成果綠、變異體皆紅" if ok else "不合"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄丙　`verify/plots/preview_W-P007.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.007 之預覽 PNG（單 §三 6）：附表 13 之二表依 Excel 之版面（欄寬、列高、合併、直書、分散對齊、粗細框線）繪之，
供 KL 與手冊第 88 頁對看。

命令列：python verify/plots/preview_W-P007.py <成果目錄> <PNG 之輸出目錄> <退縮…>
輸出：W-P.007_附表13版面_退縮<t>m.png（每一退縮一檔）。
所取：有重劃後之列之戶中，資料列最多而 ≤ 8 者（同者歸戶號小者）之一表，及「縣有（抵費地）」之表。
預覽之上方之小標唯供 KL 一眼辨表，⛔ 屬附表之內容；字形為 Noto Sans CJK（Excel 中以使用者之字形為準）。
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("preview_W_P006", os.path.join(HERE, "preview_W-P006.py"))
pv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pv)
_spec = importlib.util.spec_from_file_location("check_W_P007", os.path.join(HERE, "check_W-P007.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
plt = pv.plt
OUT = "W-P.007_附表13版面_退縮{}m.png"
OFFSET_SHEET = "縣有（抵費地）"
PX_PER_W, PX_PER_PT = 7.0, 4.0 / 3.0
LW = {"thin": 0.6, "medium": 1.8}


def _pick(wb):
    best = None
    for ws in wb:
        if not ws.title.startswith("歸戶號"):
            continue
        last = chk.last_row(ws)
        rows = chk.data_rows(ws, chk.FIRST, last)
        if not any(r[14][0] is not None for r in rows) or len(rows) > 8:
            continue
        key = (-len(rows), int(ws.title[3:]))
        if best is None or key < best[0]:
            best = (key, ws.title)
    if best is None:
        raise ValueError("無可取之戶")
    return best[1]


def _draw(ax, ws, raw, x0, y0):
    """自 (x0, y0)（像素·y 向下）繪 ws 之第 1 列至簽欄；⇒ 底之 y。"""
    from openpyxl.utils import get_column_letter
    ncol = chk.NCOL
    last = chk.last_row(ws) + 2
    xs = [x0]
    for c in range(1, ncol + 1):
        xs.append(xs[-1] + ws.column_dimensions[get_column_letter(c)].width * PX_PER_W)
    ys = [y0]
    for r in range(1, last + 1):
        ys.append(ys[-1] + (ws.row_dimensions[r].height or 15) * PX_PER_PT)
    span = {}
    inner = set()
    box = {}
    for m in ws.merged_cells.ranges:
        span[(m.min_row, m.min_col)] = (m.max_row, m.max_col)
        for r in range(m.min_row, m.max_row + 1):
            for c in range(m.min_col, m.max_col + 1):
                inner.add((r, c))
                box[(r, c)] = (m.min_row, m.min_col, m.max_row, m.max_col)
        inner.discard((m.min_row, m.min_col))
    for (r, c), (lt, rt, tp, bt) in raw.items():
        if r > last or c > ncol:
            continue
        if (r, c) in box:   # 合併之格之內部之線不繪（Excel 亦不顯示）
            r1, c1, r2, c2 = box[(r, c)]
            lt, rt, tp, bt = (lt if c == c1 else None, rt if c == c2 else None, tp if r == r1 else None,
                              bt if r == r2 else None)
        for st, (xa, ya, xb, yb) in ((lt, (xs[c - 1], ys[r - 1], xs[c - 1], ys[r])), (rt, (xs[c], ys[r - 1], xs[c], ys[r])),
                                     (tp, (xs[c - 1], ys[r - 1], xs[c], ys[r - 1])), (bt, (xs[c - 1], ys[r], xs[c], ys[r]))):
            if st:
                ax.plot([xa, xb], [ya, yb], color="black", lw=LW.get(st, 0.6), solid_capstyle="butt")
    for r in range(1, last + 1):
        for c in range(1, ncol + 1):
            if (r, c) in inner:
                continue
            cell = ws.cell(r, c)
            txt = pv._fmt(cell)
            if not txt:
                continue
            r2, c2 = span.get((r, c), (r, c))
            xa, xb, ya, yb = xs[c - 1], xs[c2], ys[r - 1], ys[r2]
            al = cell.alignment
            fs = 13 if r == 3 else 11 if r == 1 else 6.5
            if al is not None and al.text_rotation == 255:
                n = len(txt)
                step = min((yb - ya - 6) / max(n, 1), 12)
                for i, ch in enumerate(txt):
                    ax.text((xa + xb) / 2, (ya + yb) / 2 + (i - (n - 1) / 2) * step, ch, ha="center", va="center",
                            fontsize=6.5)
            elif al is not None and al.horizontal == "distributed":
                lines = txt.split("\n")
                for j, line in enumerate(lines):
                    yy = (ya + yb) / 2 + (j - (len(lines) - 1) / 2) * 13
                    n = len(line)
                    for i, ch in enumerate(line):
                        xx = xa + 12 + (xb - xa - 24) * (i / max(n - 1, 1))
                        ax.text(xx, yy, ch, ha="center", va="center", fontsize=7)
            else:
                ha = "left" if (al is None or al.horizontal in (None, "general", "left")) and r > 3 and c == 1 \
                    and (r, c) not in span else ("right" if al is not None and al.horizontal == "right" else "center")
                x = xa + 2 if ha == "left" else xb - 2 if ha == "right" else (xa + xb) / 2
                if r == 1:
                    ha, x = "left", xa
                if r > 3:   # 格內之字依格寬折行（Excel 之自動換行）
                    per = max(int((xb - xa - 4) / (fs * 1.45)), 1)
                    txt = "\n".join(txt[i:i + per] for i in range(0, len(txt), per)) if r <= 10 or c == chk.NCOL \
                        else txt
                ax.text(x, (ya + yb) / 2, txt, ha=ha, va="center", fontsize=fs, wrap=False, linespacing=1.15,
                        fontweight="bold" if r == 1 else "normal")
    return ys[-1], xs[-1]


def main(argv):
    import openpyxl
    out, png, tags = argv[0], argv[1], argv[2:]
    os.makedirs(png, exist_ok=True)
    for tag in tags:
        t = f"{float(tag):g}"
        path = os.path.join(out, chk.FMT["a13"].format(t))
        wb = openpyxl.load_workbook(path)
        raw = chk.raw_borders(path)
        names = [_pick(wb), OFFSET_SHEET]
        fig, ax = plt.subplots(figsize=(17, 24))
        y, right = 10, 0
        for nm in names:
            ax.text(0, y + 10, f"【預覽】附表 13　{nm}（退縮 {t} m）", fontsize=10, color="#555555", va="center")
            y, x = _draw(ax, wb[nm], raw[nm], 20, y + 30)
            right = max(right, x)
            y += 40
        ax.set_xlim(0, right + 20)
        ax.set_ylim(y, 0)
        ax.set_aspect("equal")
        ax.axis("off")
        p = os.path.join(png, OUT.format(t))
        fig.savefig(p, dpi=110, bbox_inches="tight")
        plt.close(fig)
        print(f"輸出 {p}（{'、'.join(names)}）")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄丁　`plots/post_tables.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.006　附表 13 重劃前後土地分配清冊、附表 24 土地分配計算表（照手冊表樣·先做格式與可填之欄）。

命令列：python plots/post_tables.py --state <配地結果_退縮*.json> --moedict <dict-revised.json> --out <目錄>
          [--map <地號對照表.xlsx>]
  --state ＝ plots/alloc_state.py 之輸出（W-P.006 版：含「財務」「歸戶表」「現金補償」及分配地之 G 式各項）。
  --map   ＝ 承辦人改過之地號對照表（plots/post_maps.py 之輸出）；無 ⇒ S 型之預設（同 post_maps）。
輸出（皆寫至 --out，⛔ 入倉）：OUT_FMT 之二檔。

所據：出圖線/orders/W-P.006_附表13-24.md（§一、§二）。
  手冊（參考/市地重劃作業手冊.txt）第 2702〜2733 列（附表 13 之編造與歸戶）、第 2769 列（附表 13 之表樣）、
  第 3755〜3800 列（附表 24 之編造）、第 3813〜3828 列（附表 13 之重劃後部分·抵費地與共同負擔公共設施）、
  第 3990〜4045 列（附表 24 之範例：①＝G×C÷(1−C)、②＝Σ(a＋a')−G−①、③＝平均公告現值）。
  KL 2026-10-28 23:31 問二 甲（未受分配而發給現金補償之戶照列·重劃後各欄留空·備註「未達最小分配面積標準
  二分之一，發給現金補償 ○○ 元」）；問三 甲（平均公告現值以匯入之公告現值暫填·表下加註）；
  23:37（正式地號依對照表帶入）；10/26 23:14 第 1 點 甲（重劃前單價取個位、重劃後單價全精度計算、顯示二位）；
  10/30 19:28（W-P.005 全定版·下一批附表 13、24）。
  本版之配地 ＝ 階段一之終（調配之前）：未分配之戶之重劃後各欄留空；各宗之 a 之併入（a'）之逐筆來源
  管線未出 ⇒ 附表 24 之重劃前唯列原位次之地號，附表 13 之「取配面積」留空（俟調配之終態）。
W-P.007（KL 2026-10-31 08:32「各附表之版面一律照手冊範本」·17:14）：附表 13 之版面照手冊 PDF 第 88 頁重畫——
  表名與冊頁在框外、題在框內；所有權人與管理人四列（標籤二行合一格、住址直書跨四列、住址之格分所有權人與管理人）；
  表頭三列（直書之格依手冊）；欄寬依手冊之比；每表至少 5 列；附註與簽欄緊接框下；橫式 A4、每頁重出 1〜10 列。
  表之內容（值、欄名、表之分法）⛔ 變；附表 24 ⛔ 變。
W-P.006_補令一（KL 2026-10-31 08:14·出圖線/KL答覆/2026-10-31_0814.md 之 1〜8）：
  一 縣有之表依管理機關分表（「縣有（抵費地）」管理人＝花蓮縣政府〔手冊第 4501 列「縣（市）主管機關」·
     平均地權條例第 3 條〕；「縣有（道路）」等公共設施各一表，管理人〔手冊第 4498 列「各該公共設施主管機關」〕
     資料所無 ⇒ 留空）；
  三 取配面積：一戶之分配地之 a 之和 ＝ 該戶重劃前各宗登記面積之和（差 ≤ 0.01×宗數）⇒ 各宗皆整筆參加分配，
     附表 13 之取配面積 ＝ 登記面積；否則留空。附表 24：其戶唯一筆重劃前土地且如上 ⇒ 分配面積 ＝ Σa ＝ 本宗之 a、
     Σa' ＝ 0（手冊第 3762 列「Σa：原位次分配土地…逕以重劃前面積加總」）；他者分配面積、Σa、Σa' 留空並加註；
  四 附表 24 之重劃前單價唯列配地計算所用之值（區段地價·未取整·顯示二位）並加註其義；
  五 表下加註計算式之取位；七 ③ 之暫值之註；八 欄名依手冊（附表 24 範例·手冊第 3990〜4045 列）。
缺值一律報錯停止（⛔ 靜默補值）；匯入資料所無之欄留空（⛔ 杜撰）。
"""
import argparse
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （地籍、歸戶、表樣之共用·W-P.001／002）
import owner_index  # noqa: E402
import post_maps as PMAP  # noqa: E402  （暫編、S 型之預設、對照表·W-P.005）

KIND_LOT, KIND_OFFSET = PMAP.KIND_LOT, PMAP.KIND_OFFSET
COUNTY = "花蓮縣"   # 抵費地與共同負擔公共設施用地之所有權人（手冊第 3819〜3821 列·登記為縣有）
NOTE_PUBLIC = "依平均地權條例第 60 條規定，由土地所有權人共同負擔取得土地"
NOTE_OFFSET = "依平均地權條例第 60 條規定，由土地所有權人以未建築土地折價抵付之土地"
NOTE_CASH = "未達最小分配面積標準二分之一，發給現金補償 {:,} 元"
NOTE_A13 = "附註：重劃後分配面積與實地指界交接土地面積如有不符，應以地政機關實際登記面積為準。"
NOTE_A24 = ("③暫以匯入之地籍資料所載之公告土地現值計（暫值）；依手冊，以重劃土地分配結果公告期滿時之"
            "當期公告土地現值為準")
NOTE_ROUND = "計算式各數為取位後之顯示值，與重劃後應分配權利面積之差係取位所致"
NOTE_PRE = ("評定之重劃前單價、原位置重劃前地價：配地計算所用之重劃前地價區段之區段地價（未取整、顯示至小數二位）；"
            "附表 18 之評定單價為其取至元之值")
NOTE_SPLIT = ("本宗之 a 含同戶他筆土地或本筆土地分屬他宗之部分，其逐筆之來源待配地程式提供，"
              "分配面積、Σa、Σa'暫空")
MGR_OFFSET = "花蓮縣政府"    # 抵費地之管理機關（手冊第 4501 列「縣（市）主管機關」·平均地權條例第 3 條）
LEGEND_A24 = "①＝G×C÷(1−C)；②＝(Σa＋Σa')−G−①；③＝平均公告現值"
SIGN_A13 = ("日期：", "承辦：", "股長：", "科長：", "局(處)長：")
SIGN_A24 = ("製表日期：", "承辦：", "股長：", "科長：", "局（處）長：")
TITLE_A13 = "○○縣(市)第○○期○○○○市地重劃區重劃前後土地分配清冊"
TITLE_A24 = "○○縣（市）第○○期○○○○市地重劃區土地分配計算表"
BOOK_A13 = "共　　冊　第　　冊　第　　頁"
SHEET_COUNTY = "縣有（{}）"
A13_NCOL = 24
A13_FIRST = 11                      # 資料之首列
A24_NCOL = 6
OUT_FMT = {"a13": "附表13_重劃前後土地分配清冊_退縮{}m.xlsx", "a24": "附表24_土地分配計算表_退縮{}m.xlsx"}
NF = {"area": "#,##0.00", "yuan": "#,##0", "p2": "#,##0.00", "k8": "0.00000000", "k4": "0.0000",
      "m2": "0.00", "pct": "0.00%"}

# 附表 13 之版面（W-P.007·照手冊 PDF 第 88 頁〔參考/手冊附表頁/附表13_重劃前後土地分配清冊_手冊PDF第88頁.png〕）
# 列 1 表名、列 2 冊頁、列 3 題（框內）、列 4〜7 所有權人與管理人、列 8〜10 表頭、列 11 起資料。
CAPTION_A13 = "附表 13 重劃前後土地分配清冊"
A13_HEAD = (    # （列, 欄起, 列迄, 欄迄, 字）
    (8, 1, 8, 10, "重劃前土地情形"), (8, 11, 10, 11, "扣除各項負擔後應分配面積(㎡)"),
    (8, 12, 8, 23, "重劃後土地情形"), (8, 24, 10, 24, "備註"),
    (9, 1, 10, 1, "鄉鎮市區"), (9, 2, 10, 2, "段"), (9, 3, 10, 3, "小段"), (9, 4, 10, 4, "地號"),
    (9, 5, 10, 5, "登記面積(㎡)"), (9, 6, 10, 6, "取配面積(㎡)"), (9, 7, 9, 8, "所有權人"),
    (9, 9, 10, 9, "持分比率"), (9, 10, 10, 10, "評定單價(元／㎡)"),
    (10, 7, 10, 7, "姓名"), (10, 8, 10, 8, "國民身分證統一編號"),
    (9, 12, 10, 12, "使用分區"), (9, 13, 10, 13, "段"), (9, 14, 10, 14, "小段"), (9, 15, 10, 15, "地號"),
    (9, 16, 10, 16, "面積(㎡)"), (9, 17, 10, 17, "評定單價(元／㎡)"), (9, 18, 9, 19, "預計繳領差額地價"),
    (10, 18, 10, 18, "繳（元）"), (10, 19, 10, 19, "領（元）"), (9, 20, 9, 21, "所有權人"),
    (10, 20, 10, 20, "姓名"), (10, 21, 10, 21, "國民身分證統一編號"), (9, 22, 10, 22, "持分比率"),
    (9, 23, 10, 23, "建號"),
)
A13_OWNER_LABEL = (   # 所有權人與管理人之標籤（列, 欄起, 列迄, 欄迄, 字）
    (4, 1, 5, 7, "土地所有權人（首列登記人）姓名\n國民身分證統一編號"),
    (6, 1, 7, 7, "管理人姓名\n國民身分證統一編號"),
    (4, 11, 7, 11, "住址"),
)
A13_OWNER_VALUE = (   # 首列登記人之 姓名、統編、住址、管理人姓名、管理人統編、管理人住址 之格（列, 欄起, 列迄, 欄迄）
    (4, 8, 4, 10), (5, 8, 5, 10), (4, 12, 5, 24), (6, 8, 6, 10), (7, 8, 7, 10), (6, 12, 7, 24),
)
A13_VERT = ((4, 11), (8, 24), (9, 1), (9, 3), (9, 4), (9, 5), (9, 6), (9, 9), (9, 12), (9, 14), (9, 15),
            (9, 16), (9, 22), (9, 23), (10, 7), (10, 20))    # 直書之格（手冊第 88 頁之直排字）
A13_DIST = ((4, 1), (6, 1), (8, 1), (8, 12))                  # 分散對齊之格（手冊之字距展開）
A13_WIDTH = (9.0, 9.1, 9.0, 9.0, 9.0, 9.1, 10.4, 10.6, 9.7, 14.3, 16.1, 7.7,
             7.7, 7.7, 7.7, 7.7, 17.4, 10.4, 10.6, 12.0, 12.0, 8.3, 8.4, 14.0)   # 手冊之欄寬（像素）÷ 7
A13_HEIGHT = {1: 24, 2: 20, 3: 28, 4: 20, 5: 20, 6: 18, 7: 18, 8: 20, 9: 34, 10: 84}
A13_ROW_H = 38          # 資料列之高
A13_NOTE_CHARS, A13_LINE_H = 7, 14   # 備註欄每行約 7 字、每行 14 點：備註之字多者，其列加高（自動換行而⛔ 截字）
A13_MIN_ROWS = 5        # 每表至少之資料列（手冊之表樣 5 列）
A13_SIGN_COL = (1, 6, 10, 14, 19)
A13_BOOK = (2, 19, 2, 24)
A24_PRE = ("段", "小段", "地號", "登記面積(㎡)", "分配面積(㎡)", "共有人申請單獨分配持分比例",
           "持分面積(㎡)", "法定空地面積(㎡)", "當期公告現值(元/㎡)", "評定之重劃前單價(元/㎡)")
A24_CALC = ("Σa(㎡)", "Σa'(㎡)", "Σ(a＋a')(㎡)", "原位置重劃前地價(元/㎡)",
            "預配位置重劃前原地平均單價(元/㎡)", "重劃後宗地地價(元/㎡)", "A＝重劃後宗地地價／預配位置重劃前地價",
            "B", "C", "1−C", "S(m)", "W(m)", "F(m)", "l1", "l2", "Rw")
A24_POST = ("評定之重劃後單價(元/㎡)", "重劃費用負擔總額(元)", "重劃後應分配權利面積(㎡)", "實配面積(㎡)",
            "分配率＝G／a", "段", "小段", "地號", "面積(㎡)", "土地使用分區", "預計繳納(領取)差額地價總額")
A24_BURDEN_HEAD = (("抵費地負擔", "①面積(㎡)", "重劃後單價(元/㎡)", "負擔額(元)"),
                   ("公共設施用地共同負擔", "②面積(㎡)", "③平均公告現值(元/㎡)", "負擔額(元)"))
A24_BURDEN = ("合計(元)", "預計應繳納差額地價(元)", "預計應領取差額地價(元)")


def D(x):
    return Decimal(repr(float(x)))


def q(x, nd):
    return x.quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- 讀取與核對
def load_case_zoning():
    d = json.load(open(PM.CASE_PARAMS, encoding="utf-8"))
    z = d["global"].get("分區")
    if PM._blank(z):
        raise PM.SourceError("case_params 之 global.分區 為空")
    return z


def check_state(doc):
    for k in ("財務", "歸戶表", "現金補償"):
        if k not in doc:
            raise PM.SourceError(f"配地結果缺 {k}（須 W-P.006 版之 plots/alloc_state.py）")
    f = doc["財務"]
    for k in ("B", "C", "重劃後單價", "重劃前單價"):
        if k not in f:
            raise PM.SourceError(f"配地結果之財務缺 {k}")
    for x in doc["宗"]:
        if x["類別"] != KIND_LOT:
            continue
        for k in ("a", "a原位次", "併入面積", "重劃前區段", "F", "W", "Rw", "l側", "l正"):
            if k not in x:
                raise PM.SourceError(f"{x['配地暫編']} 缺 {k}")
        if x["街廓"] not in f["重劃後單價"] or x["重劃前區段"] not in f["重劃前單價"]:
            raise PM.SourceError(f"{x['配地暫編']} 之街廓或區段無單價")
        if q(D(x["a原位次"]) + D(x["併入面積"]), 2) != q(D(x["a"]), 2):
            raise PM.SourceError(f"{x['配地暫編']} 之 a ≠ 原位次＋併入")


def scheme(moedict, doc, ents):
    """⇒ (lots, owners, area, key_of, hh_no, hh_lots, code_key)：重劃前之地籍與歸戶（W-P.001／002 之法）
    及配地之歸戶代號 → 重劃前之戶（一一對應·不一即停）。"""
    strokes = owner_index.load_strokes(moedict)
    lots, owners, area = PM.load_cadastre()
    key_of, _order = PM.households(lots, owners)
    hh_lots, members = PM.household_members(owners, key_of)
    hh_no = owner_index.number_households(hh_lots, members, strokes, PM.landno_key)
    table = doc["歸戶表"]
    code_key = {}
    for ln, k in key_of.items():
        if ln not in table:
            raise PM.SourceError(f"歸戶表無 {ln}")
        if code_key.setdefault(table[ln], k) != k:
            raise PM.SourceError(f"歸戶代號 {table[ln]} 對應重劃前之數戶")
    if len(set(code_key.values())) != len(code_key):
        raise PM.SourceError("重劃前之一戶對應數歸戶代號")
    extra = sorted(set(table) - set(key_of), key=PM.landno_key)
    for ln in extra:
        if table[ln] not in code_key:
            raise PM.SourceError(f"歸戶表之 {ln} 之代號 {table[ln]} 無重劃前之戶")
    if extra:
        print(f"歸戶表另有重劃前地籍所無之號（不用）：{extra}")
    for e in ents:
        if e["類別"] == KIND_LOT and code_key.get(e["歸戶"]) != key_of.get(e["原地號"]):
            raise PM.SourceError(f"{e['暫編']} 之歸戶 {e['歸戶']} 與其原地號之戶不一")
    return lots, owners, area, key_of, hh_no, hh_lots, code_key


def cash_of(doc, code_key, ents):
    """現金補償 ⇒ {戶鍵: 金額}；代號不明、金額非正整數、重複、或該戶已有分配地 ⇒ 停。"""
    have = {code_key[e["歸戶"]] for e in ents if e["類別"] == KIND_LOT}
    out = {}
    for c in doc["現金補償"]:
        k = code_key.get(c.get("歸戶"))
        amt = c.get("金額")
        if k is None:
            raise PM.SourceError(f"現金補償之歸戶 {c.get('歸戶')!r} 不明")
        if not isinstance(amt, int) or isinstance(amt, bool) or amt <= 0:
            raise PM.SourceError(f"現金補償之金額 {amt!r} 非正整數")
        if k in out:
            raise PM.SourceError(f"現金補償之歸戶 {c['歸戶']} 重複")
        if k in have:
            raise PM.SourceError(f"現金補償之歸戶 {c['歸戶']} 已有分配地")
        out[k] = amt
    return out


def shares(owners, ln):
    """⇒ [(姓名, 統編, 持分, 住址, 管理人姓名, 管理人統編)]（登記次序）。"""
    out = []
    for o in PM.owner_rows(owners, ln):
        den, num = int(o[PM.C_DEN]), int(o[PM.C_NUM])
        if den <= 0 or num <= 0:
            raise PM.SourceError(f"{ln} 之權利範圍不合：{num}/{den}")
        out.append((PM._val(o[PM.C_NAME]), PM._val(o[PM.C_UID]), f"{num}/{den}", PM._val(o[PM.C_ADDR]),
                    PM._val(o[PM.C_MGR_NAME]), PM._val(o[PM.C_MGR_UID])))
    return out


def household_shares(owners, lns):
    """一戶之各宗之（姓名, 統編, 持分）須同（重劃後按原共有狀態·一戶之分配地之持分即此）；不同 ⇒ 停。"""
    s = {ln: tuple(r[:3] for r in shares(owners, ln)) for ln in lns}
    if len(set(s.values())) != 1:
        raise PM.SourceError(f"戶 {lns} 之各宗之持分不同（須地價換算之持分·本單未定）")
    return next(iter(s.values()))


def curval(owners, ln):
    vals = {o[PM.C_CURVAL] for seq in owners[ln].values() for o in seq}
    if len(vals) != 1 or any(PM._blank(v) for v in vals):
        raise PM.SourceError(f"{ln} 之公告現值缺或不一：{vals}")
    return Decimal(str(next(iter(vals))))


def avg_curval(e, owners, hh_lns):
    """平均公告現值（KL 23:31 問三之讀：Σ(計入 G 之面積 × 現值) ÷ Σ 計入 G 之面積·個位）。
    無併入 ⇒ 原地號之現值；有併入（其逐筆來源未出）⇒ 該戶各宗之現值皆同者取之（加權平均必等於之），否則 None（留空）。"""
    if D(e["併入面積"]) == 0:
        return q(curval(owners, e["原地號"]), 0)
    vals = {curval(owners, ln) for ln in hh_lns}
    return q(next(iter(vals)), 0) if len(vals) == 1 else None


def full_households(ents, key_of, hh_lots, area):
    """⇒ {戶鍵}：該戶之分配地之 a 之和 ＝ 該戶重劃前各宗登記面積之和（差 ≤ 0.01×宗數·a 取二位所致）
    ⇒ 各宗皆整筆參加分配（取配面積 ＝ 登記面積）。"""
    tot = {}
    for e in ents:
        if e["類別"] == KIND_LOT:
            k = key_of[e["原地號"]]
            n, s = tot.get(k, (0, Decimal(0)))
            tot[k] = (n + 1, s + q(D(e["a"]), 2))
    return {k for k, (n, s) in tot.items()
            if abs(s - sum(D(area[ln]) for ln in hh_lots[k])) <= Decimal("0.01") * n}


# ---------------------------------------------------------------- 計算（附表 24）
def calc(e, fin, owners, hh_lns, single):
    post = D(fin["重劃後單價"][e["街廓"]])
    pre = D(fin["重劃前單價"][e["重劃前區段"]])
    B, C = D(fin["B"]), D(fin["C"])
    G, area = q(D(e["G"]), 2), q(D(e["面積"]), 2)
    tot = q(D(e["a原位次"]), 2) + q(D(e["併入面積"]), 2)
    a0, a1 = (tot, Decimal("0.00")) if single else (None, None)   # single：其戶唯一筆且整筆參加分配
    A = post / pre
    rw = q(D(e["Rw"]) / 100, 4)
    w = q(D(e["W"]), 2)
    b1 = q(G * C / (1 - C), 2)
    b2 = tot - G - b1
    c3 = avg_curval(e, owners, hh_lns)
    y1 = q(b1 * post, 0)
    y2 = None if c3 is None else q(b2 * c3, 0)
    diff = q((area - G) * post, 0)
    f8 = lambda x: f"{q(x, 8):.8f}"  # noqa: E731
    formula = (f"{G:.2f}=〔{tot:.2f}×(1−{f8(A)}×{f8(B)})−{q(D(e['F']), 2):.2f}×{q(D(e['l側']), 2):.2f}×{rw:.4f}"
               f"−{q(D(e['S']), 2):.2f}×{q(D(e['l正']), 2):.2f}〕×(1−{f8(C)})")
    return {"post": post, "pre": pre, "B": B, "C": C, "A": A, "G": G, "area": area,
            "a0": a0, "a1": a1, "tot": tot, "rw": rw, "w": w, "b1": b1, "b2": b2, "c3": c3, "y1": y1, "y2": y2,
            "sum": None if y2 is None else y1 + y2, "diff": diff, "formula": formula}


# ---------------------------------------------------------------- 寫表之共用
def _put(ws, r, c, v, nf=None, r2=None, c2=None):
    from openpyxl.styles import Alignment
    cell = ws.cell(r, c, v)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    if nf:
        cell.number_format = NF[nf]
    if (r2 or r, c2 or c) != (r, c):
        ws.merge_cells(start_row=r, start_column=c, end_row=r2 or r, end_column=c2 or c)
    return cell


def _num(x):
    return None if x is None else float(x)


# ---------------------------------------------------------------- 附表 13
def _frame(ws, r1, r2, ncol):
    """r1〜r2 列、1〜ncol 欄：每格四邊細線，外框粗線（手冊第 88 頁）。"""
    from openpyxl.styles import Border, Side
    thin, thick = Side(style="thin"), Side(style="medium")
    for r in range(r1, r2 + 1):
        for c in range(1, ncol + 1):
            ws.cell(r, c).border = Border(left=thick if c == 1 else thin, right=thick if c == ncol else thin,
                                          top=thick if r == r1 else thin, bottom=thick if r == r2 else thin)


def _a13_heights(ws, n):
    """資料列之高：A13_ROW_H；備註之字多者依其行數加高。"""
    for i in range(n):
        v = ws.cell(A13_FIRST + i, A13_NCOL).value
        lines = -(-len(str(v)) // A13_NOTE_CHARS) if v else 1
        ws.row_dimensions[A13_FIRST + i].height = max(A13_ROW_H, A13_LINE_H * lines)


def a13_sheet(wb, name, head_owner, pre_rows, post_rows, note_first):
    from openpyxl.styles import Alignment, Font
    from openpyxl.utils import get_column_letter
    ws = wb.create_sheet(name)
    ws.cell(1, 1, CAPTION_A13).font = Font(bold=True, size=14)
    c = _put(ws, A13_BOOK[0], A13_BOOK[1], BOOK_A13, r2=A13_BOOK[2], c2=A13_BOOK[3])
    c.alignment = Alignment(horizontal="right", vertical="center")
    _put(ws, 3, 1, TITLE_A13, c2=A13_NCOL).font = Font(size=16)
    for r1, c1, r2, c2, lab in A13_OWNER_LABEL + A13_HEAD:
        _put(ws, r1, c1, lab, r2=r2, c2=c2)
    vals = tuple(head_owner) + (None,)
    for (r1, c1, r2, c2), v in zip(A13_OWNER_VALUE, vals):
        _put(ws, r1, c1, v, r2=r2, c2=c2)
    for r, c in A13_VERT:
        ws.cell(r, c).alignment = Alignment(horizontal="center", vertical="center", text_rotation=255)
    for r, c in A13_DIST:
        ws.cell(r, c).alignment = Alignment(horizontal="distributed", vertical="center", wrap_text=True, indent=1)
    n = max(len(pre_rows), len(post_rows), A13_MIN_ROWS)
    for i in range(n):
        r = A13_FIRST + i
        if i < len(pre_rows):
            for c, (v, nf) in enumerate(pre_rows[i], start=1):
                _put(ws, r, c, v, nf)
        if i < len(post_rows):
            for c, (v, nf) in enumerate(post_rows[i], start=11):
                _put(ws, r, c, v, nf)
    if note_first:
        _put(ws, A13_FIRST, 24, note_first)
    _a13_heights(ws, n)
    last = A13_FIRST + n - 1
    _frame(ws, 3, last, A13_NCOL)
    ws.cell(last + 1, 1, NOTE_A13)
    for col, lab in zip(A13_SIGN_COL, SIGN_A13):
        ws.cell(last + 2, col, lab)
    ws.row_dimensions[last + 1].height = ws.row_dimensions[last + 2].height = 24
    for r, h in A13_HEIGHT.items():
        ws.row_dimensions[r].height = h
    for i, w in enumerate(A13_WIDTH, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    PM._page(ws, "1:10", landscape=True)
    return ws


def lot_post_rows(e, no, zoning, own3, fin):
    post = D(fin["重劃後單價"][e["街廓"]])
    G, area = q(D(e["G"]), 2), q(D(e["面積"]), 2)
    diff = q((area - G) * post, 0)
    pay, get = (diff, None) if diff >= 0 else (None, -diff)
    rows = []
    for nm, uid, sh in own3:
        rows.append([(float(G), "area"), (zoning, None), (None, None), (None, None), (no, None),
                     (float(area), "area"), (float(post), "p2"), (_num(pay), "yuan"), (_num(get), "yuan"),
                     (nm, None), (uid, None), (sh, None), (None, None)])
    return rows


def write_a13(path, doc, ents, numbers, sch, cash, zoning, pre_price, full):
    import openpyxl
    lots, owners, area, key_of, hh_no, hh_lots, code_key = sch
    fin = doc["財務"]
    loc = {x["地號"]: x for x in lots}
    by_hh = {}
    for e in ents:
        if e["類別"] == KIND_LOT:
            by_hh.setdefault(key_of[e["原地號"]], []).append(e)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    out = []
    for k in sorted(hh_lots, key=lambda kk: hh_no[kk]):
        lns = sorted(hh_lots[k], key=PM.landno_key)
        first = shares(owners, lns[0])[0]
        head = (first[0], first[1], first[3], first[4], first[5])
        pre_rows = []
        for ln in lns:
            for nm, uid, sh, *_ in shares(owners, ln):
                pre_rows.append([(loc[ln]["鄉鎮市區"], None), (loc[ln]["段"], None), (loc[ln].get("小段"), None),
                                 (ln, None), (area[ln], "area"), (area[ln] if k in full else None, "area"),
                                 (nm, None), (uid, None),
                                 (sh, None), (pre_price[ln], "yuan")])
        post_rows = []
        es = sorted(by_hh.get(k, []), key=lambda e: PM.landno_key(numbers[e["暫編"]]))
        if es:
            own3 = household_shares(owners, lns)
            for e in es:
                post_rows += lot_post_rows(e, numbers[e["暫編"]], zoning, own3, fin)
        note = NOTE_CASH.format(cash[k]) if k in cash else None
        a13_sheet(wb, f"歸戶號{hh_no[k]}", head, pre_rows, post_rows, note)
        out.append((hh_no[k], lns, [numbers[e["暫編"]] for e in es], note))
    groups = {}   # 依管理機關分表：抵費地一表、公共設施依其分類各一表（管理機關資料所無 ⇒ 分類即其別）
    for e in sorted((e for e in ents if e["類別"] != KIND_LOT), key=lambda e: PM.landno_key(numbers[e["暫編"]])):
        groups.setdefault(e["類別"], []).append(e)
    for cat in sorted(groups, key=lambda c: (c != KIND_OFFSET, PM.landno_key(numbers[groups[c][0]["暫編"]]))):
        off = cat == KIND_OFFSET
        rows = []
        for e in groups[cat]:
            price = (float(D(fin["重劃後單價"][e["街廓"]])), "p2") if off else (None, None)
            rows.append([(None, "area"), (zoning if off else e["類別"], None), (None, None), (None, None),
                         (numbers[e["暫編"]], None), (float(q(D(e["面積"]), 2)), "area"), price,
                         (None, "yuan"), (None, "yuan"), (COUNTY, None), (None, None), ("1/1", None), (None, None)])
        ws = a13_sheet(wb, SHEET_COUNTY.format(cat), (COUNTY, None, None, MGR_OFFSET if off else None, None),
                       [], rows, None)
        for i in range(len(rows)):
            _put(ws, A13_FIRST + i, 24, NOTE_OFFSET if off else NOTE_PUBLIC)
        _a13_heights(ws, max(len(rows), A13_MIN_ROWS))
    wb.save(path)
    return out


# ---------------------------------------------------------------- 附表 24
def write_a24(path, doc, ents, numbers, sch, zoning, full):
    import openpyxl
    lots, owners, area, key_of, hh_no, hh_lots, code_key = sch
    fin = doc["財務"]
    loc = {x["地號"]: x for x in lots}
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    out = []
    es = sorted((e for e in ents if e["類別"] == KIND_LOT), key=lambda e: PM.landno_key(numbers[e["暫編"]]))
    for e in es:
        no, ln = numbers[e["暫編"]], e["原地號"]
        k = key_of[ln]
        lns = sorted(hh_lots[k], key=PM.landno_key)
        single = k in full and len(lns) == 1
        x = calc(e, fin, owners, lns, single)
        own = shares(owners, ln)
        ws = wb.create_sheet(f"地號{no}")
        _put(ws, 1, 1, TITLE_A24, c2=A24_NCOL)
        _put(ws, 2, 1, "歸戶號")
        _put(ws, 2, 2, hh_no[k])
        _put(ws, 2, 3, "所有權(代表)人姓名")
        _put(ws, 2, 4, own[0][0] if len(own) == 1 else f"{own[0][0]}等{len(own)}人", c2=A24_NCOL)
        r = 3
        _put(ws, r, 1, "重劃前", c2=A24_NCOL)
        pre = (loc[ln]["段"], loc[ln].get("小段"), ln, (area[ln], "area"), (_num(x["a0"]), "area"), None, None, None,
               (float(curval(owners, ln)), "yuan"), (float(x["pre"]), "p2"))
        for lab, v in zip(A24_PRE, pre):
            r += 1
            _put(ws, r, 1, lab)
            v, nf = v if isinstance(v, tuple) else (v, None)
            _put(ws, r, 2, v, nf)
        r += 1
        _put(ws, r, 1, "計算分配有關資料", c2=A24_NCOL)
        calc_v = ((x["a0"], "area"), (x["a1"], "area"), (x["tot"], "area"), (x["pre"], "p2"), (None, None),
                  (x["post"], "p2"), (x["A"], "k8"), (x["B"], "k8"), (x["C"], "k8"), (1 - x["C"], "k8"),
                  (q(D(e["S"]), 2), "m2"), (x["w"], "m2"), (q(D(e["F"]), 2), "m2"), (q(D(e["l側"]), 2), "m2"),
                  (q(D(e["l正"]), 2), "m2"), (x["rw"], "k4"))
        for lab, (v, nf) in zip(A24_CALC, calc_v):
            r += 1
            _put(ws, r, 1, lab)
            _put(ws, r, 2, _num(v), nf)
        r += 1
        _put(ws, r, 1, "計算式")
        _put(ws, r, 2, x["formula"], c2=A24_NCOL)
        r += 1
        _put(ws, r, 1, "重劃後", c2=A24_NCOL)
        d = x["diff"]
        box = ("■繳納□領取" if d > 0 else "□繳納■領取" if d < 0 else "□繳納□領取") + f"新臺幣 {abs(d):,} 元"
        post_v = ((x["post"], "p2"), (x["sum"], "yuan"), (x["G"], "area"), (x["area"], "area"), (x["G"] / x["tot"], "pct"),
                  (None, None), (None, None), (no, None), (x["area"], "area"), (zoning, None), (box, None))
        for lab, (v, nf) in zip(A24_POST, post_v):
            r += 1
            _put(ws, r, 1, lab)
            _put(ws, r, 2, v if isinstance(v, str) or v is None else float(v), nf)
        for head, mark, (a_, p_, y_, pnf) in zip(A24_BURDEN_HEAD, ("①", "②"),
                                                 ((x["b1"], x["post"], x["y1"], "p2"), (x["b2"], x["c3"], x["y2"], "yuan"))):
            r += 1
            for c, lab in enumerate(head, start=1):
                _put(ws, r, c, lab)
            r += 1
            _put(ws, r, 1, mark)
            _put(ws, r, 2, _num(a_), "area")
            _put(ws, r, 3, _num(p_), pnf)
            _put(ws, r, 4, _num(y_), "yuan")
        burden = ((None, None, x["sum"]), (None, None, d if d > 0 else 0), (None, None, -d if d < 0 else 0))
        for lab, (a_, p_, y_) in zip(A24_BURDEN, burden):
            r += 1
            _put(ws, r, 1, lab)
            _put(ws, r, 2, _num(a_), "area")
            _put(ws, r, 3, _num(p_), "p2")
            _put(ws, r, 4, _num(y_), "yuan")
        PM._grid(ws, 2, r, A24_NCOL)
        notes = [LEGEND_A24, NOTE_A24, NOTE_ROUND, NOTE_PRE] + ([] if single else [NOTE_SPLIT])
        for i, s in enumerate(notes, start=1):
            ws.cell(r + i, 1, s)
        for i, lab in enumerate(SIGN_A24):
            ws.cell(r + len(notes) + 2, 1 + i, lab)
        ws.column_dimensions["A"].width = 30
        ws.column_dimensions["B"].width = 16
        PM._page(ws, "1:2", landscape=False)
        out.append((no, hh_no[k], x))
    wb.save(path)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.006 附表 13、24")
    ap.add_argument("--state", required=True)
    ap.add_argument("--moedict", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map")
    a = ap.parse_args(argv)
    doc = PMAP.load_state(a.state)
    check_state(doc)
    tag = PMAP.tag_of(doc)
    ents = PMAP.entries_of(doc)
    order = PMAP.s_order(doc, ents)
    numbers = PMAP.read_map(a.map, ents) if a.map else PMAP.default_numbers(order)
    sch = scheme(a.moedict, doc, ents)
    cash = cash_of(doc, sch[6], ents)
    zoning = load_case_zoning()
    zone_of, _unit, price = PM.load_price_zones()
    pre_price = {}
    for x in sch[0]:
        ln = x["地號"]
        if ln not in zone_of or zone_of[ln] not in price:
            raise PM.SourceError(f"{ln} 無重劃前地價區段或單價")
        pre_price[ln] = price[zone_of[ln]]
    os.makedirs(a.out, exist_ok=True)
    p = {k: os.path.join(a.out, v.format(tag)) for k, v in OUT_FMT.items()}
    full = full_households(ents, sch[3], sch[5], sch[2])
    r13 = write_a13(p["a13"], doc, ents, numbers, sch, cash, zoning, pre_price, full)
    r24 = write_a24(p["a24"], doc, ents, numbers, sch, zoning, full)
    n_lot = sum(1 for e in ents if e["類別"] == KIND_LOT)
    print(f"退縮 {tag} m：附表 13 戶 {len(r13)}（有分配地 {sum(1 for x in r13 if x[2])}、取配面積可填 {len(full)}、"
          f"現金補償 {len(cash)}）＋縣有 {len(ents) - n_lot}；附表 24 張 {len(r24)}"
          f"（Σa 可填 {sum(1 for x in r24 if x[2]['a0'] is not None)}）")
    for no, hh, x in r24:
        print(f"  地號 {no}（歸戶號 {hh}）：G {x['G']}、Σ {x['tot']}（Σa {x['a0']}、Σa' {x['a1']}）、① {x['b1']}、② {x['b2']}、"
              f"③ {x['c3']}、負擔額 {x['y1']}＋{x['y2']}＝{x['sum']}、差額 {x['diff']}")
    for k, v in p.items():
        print(f"輸出 {v}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄戊　`verify/plots/check_W-P006.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.006 之量測（單 §三 3）：附表 13 重劃前後土地分配清冊、附表 24 土地分配計算表。
獨立於 plots/：⛔ import 之（V6 唯以子行程呼叫 plots/post_tables.py 之命令列）；期望取自
配地結果_退縮*.json（plots/alloc_state.py）、地號對照表與重劃後顏色對照表（W-P.005·KL 定版）、重劃前顏色對照表
（W-P.001／002·KL 定版·歸戶號與區段單價）、data/地籍資料來源_匿名版.xlsx 之 U_LAND（逐欄自讀）、
verify/case_params_UC9898.json、手冊第 3990〜4045 列之範例、KL 2026-10-28 23:31 之答。

命令列：python verify/plots/check_W-P006.py <成果目錄> <重劃前成果目錄> <dict-revised.json> <退縮…> [--prog <post_tables.py>]
  <成果目錄>     ＝ 含 配地結果_退縮<t>m.json、地號對照表_退縮<t>m.xlsx、顏色對照表_重劃後_退縮<t>m.xlsx、
                   附表13_…_退縮<t>m.xlsx、附表24_…_退縮<t>m.xlsx。
  <重劃前成果目錄> ＝ plots/prelim_maps.py 之輸出（顏色對照表_重劃前.xlsx）。
各退縮印 V0〜V6 之 PASS／FAIL；全 PASS 者結束碼 0。
W-P.006_補令一（KL 2026-10-31 08:14）：縣有依管理機關分表（抵費地之管理人 花蓮縣政府、公共設施之管理人留空）；
取配面積／分配面積／Σa／Σa' 之可填與否（戶之 a 之和 ＝ 重劃前登記面積之和）；重劃前單價唯列所用之值；
表下之加註；欄名依手冊之附表 24 範例。
W-P.007（KL 2026-10-31 08:32·附表 13 之版面照手冊第 88 頁）：附表 13 之讀取之位置隨新版面改（題在第 3 列、
首列登記人之格、表頭第 8〜10 列、資料第 11 列起、附註緊接框下、簽欄五處）；所量之內容⛔ 變。版面本身由
check_W-P007.py 量之。
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CASE = os.path.join(REPO, "verify", "case_params_UC9898.json")
XLSX = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
PROG = os.path.join(REPO, "plots", "post_tables.py")
SECTION = "0013德安段"
U = {"sec": 0, "code": 1, "area": 6, "cur": 9, "seq": 23, "den": 28, "num": 29, "uid": 32, "name": 33,
     "addr": 34, "muid": 39, "mname": 40}
FMT = {"state": "配地結果_退縮{}m.json", "map": "地號對照表_退縮{}m.xlsx", "color": "顏色對照表_重劃後_退縮{}m.xlsx",
       "a13": "附表13_重劃前後土地分配清冊_退縮{}m.xlsx", "a24": "附表24_土地分配計算表_退縮{}m.xlsx"}
PRE_COLOR = "顏色對照表_重劃前.xlsx"
COUNTY = "花蓮縣"
T_A13 = "○○縣(市)第○○期○○○○市地重劃區重劃前後土地分配清冊"
T_A24 = "○○縣（市）第○○期○○○○市地重劃區土地分配計算表"
N_PUB = "依平均地權條例第 60 條規定，由土地所有權人共同負擔取得土地"
N_OFF = "依平均地權條例第 60 條規定，由土地所有權人以未建築土地折價抵付之土地"
N_A13 = "附註：重劃後分配面積與實地指界交接土地面積如有不符，應以地政機關實際登記面積為準。"
N_A24 = ("③暫以匯入之地籍資料所載之公告土地現值計（暫值）；依手冊，以重劃土地分配結果公告期滿時之"
         "當期公告土地現值為準")
N_ROUND = "計算式各數為取位後之顯示值，與重劃後應分配權利面積之差係取位所致"
N_PRE = ("評定之重劃前單價、原位置重劃前地價：配地計算所用之重劃前地價區段之區段地價（未取整、顯示至小數二位）；"
         "附表 18 之評定單價為其取至元之值")
N_SPLIT = "本宗之 a 含同戶他筆土地或本筆土地分屬他宗之部分，其逐筆之來源待配地程式提供，分配面積、Σa、Σa'暫空"
MGR_OFF = "花蓮縣政府"
CNTY = "縣有（{}）"
L_A24 = "①＝G×C÷(1−C)；②＝(Σa＋Σa')−G−①；③＝平均公告現值"
H6 = ("鄉鎮市區", "段", "小段", "地號", "登記面積(㎡)", "取配面積(㎡)", "所有權人", None, "持分比率", "評定單價(元／㎡)",
      None, "使用分區", "段", "小段", "地號", "面積(㎡)", "評定單價(元／㎡)", "預計繳領差額地價", None, "所有權人", None,
      "持分比率", "建號", None)
H5 = ("重劃前土地情形",) + (None,) * 9 + ("扣除各項負擔後應分配面積(㎡)", "重劃後土地情形") + (None,) * 11 + ("備註",)
H7 = (None,) * 6 + ("姓名", "國民身分證統一編號") + (None,) * 9 + ("繳（元）", "領（元）", "姓名", "國民身分證統一編號") + (None,) * 3
FIRST = 11
OWNER13 = ((4, 8), (5, 8), (4, 12), (6, 8), (7, 8))   # 首列登記人 姓名、統編、住址、管理人姓名、統編
SIGN13 = (1, 6, 10, 14, 19)
MIN13 = 5
TOL_G = Decimal("0.02")        # 計算式以表上之值重算與 G 之差（G 為幾何二分之解·S 等取二位）
TOL_AREA = 0.05


def dq(x, nd=2):
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


def qd(x, nd):
    return x.quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


def nkey(s):
    p = str(s).split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0)


def landno(code):
    m, s = divmod(int(code), 10000)
    return f"{m}" if s == 0 else f"{m}-{s}"


def blank(v):
    return v is None or (isinstance(v, str) and v.strip() in ("", "null"))


# ---------------------------------------------------------------- 手冊之式（V0 以範例自證）
def burden(G, tot, C, post, cur):
    b1 = qd(G * C / (1 - C), 2)
    b2 = tot - G - b1
    y1 = qd(b1 * post, 0)
    y2 = None if cur is None else qd(b2 * cur, 0)
    return b1, b2, y1, y2


def eval_formula(s):
    """「G=〔Σ×(1−A×B)−F×l1×Rw−S×l2〕×(1−C)」⇒ (G, 右式之值)。"""
    m = re.fullmatch(r"([\d.]+)=〔([\d.]+)×\(1−([\d.]+)×([\d.]+)\)−([\d.]+)×([\d.]+)×([\d.]+)−([\d.]+)×([\d.]+)〕×\(1−([\d.]+)\)", s)
    if not m:
        return None
    g, t, a, b, f, l1, rw, s_, l2, c = (Decimal(v) for v in m.groups())
    return g, (t * (1 - a * b) - f * l1 * rw - s_ * l2) * (1 - c)


# ---------------------------------------------------------------- 讀取
class Ctx:
    pass


def read_uland():
    import openpyxl
    own, area, cur = {}, {}, {}
    for r in openpyxl.load_workbook(XLSX, read_only=True)["U_LAND"].iter_rows(values_only=True):
        if r[U["sec"]] != SECTION or blank(r[U["code"]]):
            continue
        try:
            ln = landno(r[U["code"]])
        except (TypeError, ValueError):
            continue
        area[ln] = float(r[U["area"]])
        cur.setdefault(ln, set()).add(r[U["cur"]])
        own.setdefault(ln, {}).setdefault(int(r[U["seq"]]), r)
    wb = openpyxl.load_workbook(XLSX, read_only=True)
    reg = list(wb["重劃區地籍"].iter_rows(values_only=True))
    h = reg[0]
    place = {str(r[h.index("地號")]).strip(): (r[h.index("鄉鎮市")], r[h.index("地段")]) for r in reg[1:]
             if not blank(r[h.index("地號")])}
    rows = {}
    for ln, d in own.items():
        rows[ln] = [(str(r[U["name"]]), str(r[U["uid"]]), f"{int(r[U['num']])}/{int(r[U['den']])}", r[U["addr"]],
                     None if blank(r[U["mname"]]) else r[U["mname"]], None if blank(r[U["muid"]]) else r[U["muid"]])
                    for _, r in sorted(d.items())]
    return rows, area, cur, place


def load(out, pre, tag):
    import openpyxl
    c = Ctx()
    c.tag = tag
    c.p = {k: os.path.join(out, v.format(tag)) for k, v in FMT.items()}
    c.state = json.load(open(c.p["state"], encoding="utf-8"))
    ws = openpyxl.load_workbook(c.p["map"], data_only=True)["地號對照表"]
    c.no = {}
    for r in list(ws.iter_rows(values_only=True))[1:]:
        if r and r[0] is not None and r[1] is not None:
            c.no[r[3] if r[3] is not None else r[0]] = str(r[5])
    pw = openpyxl.load_workbook(os.path.join(pre, PRE_COLOR), data_only=True)
    c.hh_of = {}
    for r in list(pw["重劃前歸戶圖"].iter_rows(values_only=True))[1:]:
        for ln in str(r[4]).split("、"):
            c.hh_of[ln] = int(r[1])
    c.price_of = {}
    for r in list(pw["重劃前地價圖"].iter_rows(values_only=True))[1:]:
        for ln in str(r[4]).split("、"):
            c.price_of[ln] = int(r[3])
    cw = openpyxl.load_workbook(c.p["color"], data_only=True)["分配後歸戶圖"]
    c.post_hh = {}
    for r in list(cw.iter_rows(values_only=True))[1:]:
        if isinstance(r[1], int):
            for no in str(r[3]).split("、"):
                c.post_hh[no] = r[1]
    c.a13 = openpyxl.load_workbook(c.p["a13"], data_only=True)
    c.a24 = openpyxl.load_workbook(c.p["a24"], data_only=True)
    c.own, c.area, c.cur, c.place = read_uland()
    cp = json.load(open(CASE, encoding="utf-8"))
    c.zoning = cp["global"]["分區"]
    c.lots = [x for x in c.state["宗"] if x["類別"] == "分配地"]
    c.others = [x for x in c.state["宗"] if x["類別"] != "分配地"]
    c.public = sorted(b for b, v in c.state["街廓"].items() if "宗地分配線方向" not in v)
    c.fin = c.state["財務"]
    tot = {}
    for x in c.lots:
        n = c.hh_of[x["原地號"]]
        k, s = tot.get(n, (0, Decimal(0)))
        tot[n] = (k + 1, s + dq(x["a"]))
    c.full = {n for n, (k, s) in tot.items()
              if abs(s - sum(dq(c.area[ln]) for ln, h in c.hh_of.items() if h == n)) <= Decimal("0.01") * k}
    c.single = {n for n in c.full if sum(1 for h in c.hh_of.values() if h == n) == 1}
    cats = {}
    for x in c.others:
        cats.setdefault("抵費地", []).append(c.no[x["配地暫編"]])
    for b in c.public:
        cats.setdefault(c.state["街廓"][b]["分類"], []).append(c.no[b])
    c.county = [CNTY.format(k) for k in sorted(cats, key=lambda k: (k != "抵費地", min(nkey(v) for v in cats[k])))]
    c.cat_of = {no: k for k, v in cats.items() for no in v}
    return c


def rows_of(ws, first=FIRST):
    out = []
    r = first
    while any(ws.cell(r, k).value is not None for k in range(1, 25)) and ws.cell(r, 1).value != N_A13:
        out.append(tuple(ws.cell(r, k).value for k in range(1, 25)))
        r += 1
    return out, r


def money(c, x):
    post = Decimal(repr(c.fin["重劃後單價"][x["街廓"]]))
    return qd((dq(x["面積"]) - dq(x["G"])) * post, 0)


# ---------------------------------------------------------------- 量測
def v0(c):
    bad = []
    b1, b2, y1, y2 = burden(Decimal("202.83"), Decimal("340.64"), Decimal("0.07790626"), Decimal(162000),
                            Decimal(69600))
    if (b1, b2, y1, y2, y1 + y2) != (Decimal("17.14"), Decimal("120.67"), 2776680, 8398632, 11175312):
        bad.append(f"手冊之範例 ①②與負擔額不合：{b1} {b2} {y1} {y2}")
    g, val = eval_formula("202.83=〔340.64×(1−2.32758621×0.13579793)−0.00×0.00×0.0000−6.50×2.00〕×(1−0.07790626)")
    if dq(val) != g:
        bad.append(f"手冊之範例 G 式 {val} ≠ 202.83")
    return bad


def v1(c):
    """附表 13：一戶一表（歸戶號 ＝ 重劃前顏色對照表）＋縣有；表頭、題、附註、簽欄、首列登記人。"""
    bad = []
    hh = sorted(set(c.hh_of.values()))
    want = [f"歸戶號{n}" for n in hh] + c.county
    if c.a13.sheetnames != want:
        return [f"附表 13 之表 {c.a13.sheetnames}"]
    for ws in c.a13:
        if ws.cell(3, 1).value != T_A13:
            bad.append(f"{ws.title} 之題")
        for rr, h in ((8, H5), (9, H6), (10, H7)):
            if tuple(ws.cell(rr, k).value for k in range(1, 25)) != h:
                bad.append(f"{ws.title} 列 {rr} 之表頭")
        rows, _ = rows_of(ws)
        r = FIRST + max(len(rows), MIN13)
        if ws.cell(r, 1).value != N_A13 or [ws.cell(r + 1, k).value for k in SIGN13] != \
                ["日期：", "承辦：", "股長：", "科長：", "局(處)長："]:
            bad.append(f"{ws.title} 之附註或簽欄")
        if ws.title.startswith("縣有"):
            mgr = MGR_OFF if ws.title == CNTY.format("抵費地") else None
            if ws.cell(*OWNER13[0]).value != COUNTY or ws.cell(*OWNER13[3]).value != mgr:
                bad.append(f"{ws.title} 之所有權人或管理人 {ws.cell(*OWNER13[0]).value}、{ws.cell(*OWNER13[3]).value}")
            continue
        n = int(ws.title[3:])
        lns = sorted((ln for ln, h in c.hh_of.items() if h == n), key=nkey)
        f = c.own[lns[0]][0]
        got = tuple(ws.cell(*rc).value for rc in OWNER13)
        if got != (f[0], f[1], f[3], f[4], f[5]):
            bad.append(f"{ws.title} 之首列登記人 {got}")
    return bad


def v2(c):
    """附表 13 之重劃前：每戶之各宗 × 各所有權人一列（地號序·登記次序）；取配面積：戶之 a 之和 ＝ 登記面積之和者
    ＝ 登記面積，否則留空。"""
    bad = []
    for n in sorted(set(c.hh_of.values())):
        ws = c.a13[f"歸戶號{n}"]
        rows, _ = rows_of(ws)
        got = [r[:10] for r in rows if r[3] is not None]
        want = []
        for ln in sorted((ln for ln, h in c.hh_of.items() if h == n), key=nkey):
            for nm, uid, sh, *_ in c.own[ln]:
                want.append((c.place[ln][0], c.place[ln][1], None, ln, c.area[ln], c.area[ln] if n in c.full else None,
                             nm, uid, sh, c.price_of[ln]))
        if got != want:
            bad.append(f"歸戶號{n} 之重劃前 {len(got)}／{len(want)} 列不合")
        if any(r[:10] != (None,) * 10 for r in rows[len(got):]):
            bad.append(f"歸戶號{n} 之重劃前有多出之列")
    return bad


def v3(c):
    """附表 13 之重劃後：各分配地入其戶（歸戶號 ＝ 重劃後顏色對照表）、各所有權人一列、G／面積／單價／差額；
    縣有之表 ＝ 抵費地與公設（備註照手冊）；每一正式地號恰一次；面積之和 ＝ 全部街廓之和。"""
    bad = []
    seen = []
    tot = 0.0
    for x in c.lots:
        no = c.no[x["配地暫編"]]
        n = c.post_hh.get(no)
        if n is None or n != c.hh_of[x["原地號"]]:
            bad.append(f"{no} 之歸戶號 {n}")
            continue
        rows, _ = rows_of(c.a13[f"歸戶號{n}"])
        got = [r[10:23] for r in rows if r[14] == no]
        d = money(c, x)
        want = [(float(dq(x["G"])), c.zoning, None, None, no, float(dq(x["面積"])),
                 c.fin["重劃後單價"][x["街廓"]], float(d) if d >= 0 else None, float(-d) if d < 0 else None,
                 nm, uid, sh, None) for nm, uid, sh, *_ in c.own[x["原地號"]]]
        if got != want:
            bad.append(f"{no} 之重劃後之列不合（{len(got)}／{len(want)}）")
        seen.append(no)
        tot += float(dq(x["面積"]))
    rows = []
    for t in c.county:
        rr = rows_of(c.a13[t])[0]
        if any(c.cat_of.get(r[14]) != t[3:-1] for r in rr):
            bad.append(f"{t} 有他類之列")
        rows += rr
    want = []
    for x in c.others:
        want.append((c.no[x["配地暫編"]], c.zoning, c.fin["重劃後單價"][x["街廓"]], N_OFF, float(dq(x["面積"]))))
    for b in c.public:
        from shapely.geometry import Polygon
        want.append((c.no[b], c.state["街廓"][b]["分類"], None, N_PUB, float(dq(Polygon(c.state["街廓"][b]["多邊形"]).area))))
    want.sort(key=lambda t: nkey(t[0]))
    got = sorted(((r[14], r[11], r[16], r[23], r[15]) for r in rows), key=lambda t: nkey(t[0]))
    if got != want:
        bad.append(f"縣有之列不合：{[g for g, w in zip(got, want) if g != w][:3]}")
    if any(r[19] != COUNTY or r[21] != "1/1" or any(r[k] is not None for k in range(0, 11)) for r in rows):
        bad.append("縣有之所有權人、持分或重劃前欄不合")
    seen += [r[14] for r in rows]
    tot += sum(r[15] for r in rows)
    allno = []
    for ws in c.a13:
        allno += sorted({r[14] for r in rows_of(ws)[0] if r[14] is not None}, key=nkey)
    if sorted(allno, key=nkey) != sorted(seen, key=nkey) or len(set(allno)) != len(allno) \
            or sorted(allno, key=nkey) != sorted(c.no.values(), key=nkey):
        bad.append("正式地號非恰一次")
    from shapely.geometry import Polygon
    blk = sum(Polygon(v["多邊形"]).area for v in c.state["街廓"].values())
    if abs(tot - blk) > TOL_AREA:
        bad.append(f"面積之和 {tot:.2f} ≠ 街廓 {blk:.2f}")
    for ws in c.a13:
        if not ws.title.startswith("縣有") and any(r[23] is not None for r in rows_of(ws)[0]):
            bad.append(f"{ws.title} 有備註（本版無現金補償）")
    return bad


SECTIONS = ("重劃前", "計算分配有關資料", "重劃後")


def a24_vals(ws):
    """⇒ {(節, 標籤): [B, C, D 之值]}；節 ＝ 其上最近之「重劃前／計算分配有關資料／重劃後」（題之前為 ""）。"""
    out, sec = {}, ""
    for r in range(1, ws.max_row + 1):
        lab = ws.cell(r, 1).value
        if lab is None:
            continue
        if lab in SECTIONS and all(ws.cell(r, k).value is None for k in range(2, 5)):
            sec = lab
            continue
        key = (sec, lab)
        if key in out:
            raise AssertionError(f"{ws.title} 之 {key} 重出")
        out[key] = [ws.cell(r, k).value for k in range(2, 5)]
    return out


def same(a, b):
    """二列之值相等（浮點以相對 1e-12 為度·Excel 之存值或少末位）。"""
    if a is None or b is None or len(a) != len(b):
        return a == b
    for x, y in zip(a, b):
        if isinstance(x, float) and isinstance(y, (int, float)) and not isinstance(y, bool):
            if abs(x - y) > 1e-12 * max(1.0, abs(y)):
                return False
        elif x != y:
            return False
    return True


def v4(c):
    """附表 24：一分配地一張（正式地號之序）；歸戶號、代表人、重劃前、計算分配有關資料、計算式（與 G 之差 ≤ 0.02）。"""
    bad = []
    lots = sorted(c.lots, key=lambda x: nkey(c.no[x["配地暫編"]]))
    want = [f"地號{c.no[x['配地暫編']]}" for x in lots]
    if c.a24.sheetnames != want:
        return [f"附表 24 之表 {c.a24.sheetnames}"]
    B, C = Decimal(repr(c.fin["B"])), Decimal(repr(c.fin["C"]))
    for x in lots:
        ws = c.a24[f"地號{c.no[x['配地暫編']]}"]
        v = a24_vals(ws)
        if ("", T_A24) not in v:
            bad.append(f"{ws.title} 之題")
        ln = x["原地號"]
        own = c.own[ln]
        rep = own[0][0] if len(own) == 1 else f"{own[0][0]}等{len(own)}人"
        post = Decimal(repr(c.fin["重劃後單價"][x["街廓"]]))
        pre = Decimal(repr(c.fin["重劃前單價"][x["重劃前區段"]]))
        A = post / pre
        tot = dq(x["a"])
        single = c.hh_of[ln] in c.single
        a0 = float(tot) if single else None
        P, K = "重劃前", "計算分配有關資料"
        exp = {
            ("", "歸戶號"): [c.hh_of[ln], "所有權(代表)人姓名", rep], (P, "段"): [c.place[ln][1], None, None],
            (P, "小段"): [None, None, None], (P, "地號"): [ln, None, None],
            (P, "登記面積(㎡)"): [c.area[ln], None, None], (P, "分配面積(㎡)"): [a0, None, None],
            (P, "共有人申請單獨分配持分比例"): [None, None, None], (P, "持分面積(㎡)"): [None, None, None],
            (P, "法定空地面積(㎡)"): [None, None, None],
            (P, "當期公告現值(元/㎡)"): [float(next(iter(c.cur[ln]))), None, None],
            (P, "評定之重劃前單價(元/㎡)"): [float(pre), None, None],
            "Σa(㎡)": [a0, None, None], "Σa'(㎡)": [0.0 if single else None, None, None],
            "Σ(a＋a')(㎡)": [float(tot), None, None], "原位置重劃前地價(元/㎡)": [float(pre), None, None],
            "預配位置重劃前原地平均單價(元/㎡)": [None, None, None], "重劃後宗地地價(元/㎡)": [float(post), None, None],
            "A＝重劃後宗地地價／預配位置重劃前地價": [float(A), None, None], "B": [float(B), None, None],
            "C": [float(C), None, None], "1−C": [float(1 - C), None, None], "S(m)": [float(dq(x["S"])), None, None],
            "W(m)": [float(dq(x["W"])), None, None], "F(m)": [float(dq(x["F"])), None, None],
            "l1": [float(dq(x["l側"])), None, None], "l2": [float(dq(x["l正"])), None, None],
            "Rw": [float(dq(x["Rw"] / 100, 4)), None, None],
        }
        exp = {(k if isinstance(k, tuple) else (K, k)): e for k, e in exp.items()}
        for k, e in exp.items():
            if not same(v.get(k), e):
                bad.append(f"{ws.title} 之「{k}」{v.get(k)} ≠ {e}")
        if c.price_of[ln] != int(qd(pre, 0)):
            bad.append(f"{ws.title} 之重劃前單價 {pre} 取整 ≠ 附表 18 之 {c.price_of[ln]}")
        f8 = lambda d: f"{qd(d, 8):.8f}"  # noqa: E731
        s = (f"{dq(x['G']):.2f}=〔{tot:.2f}×(1−{f8(A)}×{f8(B)})−{dq(x['F']):.2f}×{dq(x['l側']):.2f}×"
             f"{dq(x['Rw'] / 100, 4):.4f}−{dq(x['S']):.2f}×{dq(x['l正']):.2f}〕×(1−{f8(C)})")
        got = (v.get((K, "計算式")) or [None])[0]
        if got != s:
            bad.append(f"{ws.title} 之計算式 {got} ≠ {s}")
        else:
            g, val = eval_formula(got)
            if abs(val - g) > TOL_G:
                bad.append(f"{ws.title} 之計算式重算 {val:.4f} 與 G {g} 差逾 {TOL_G}")
    return bad


def v5(c):
    """附表 24 之重劃後與重劃費用負擔：①②③、負擔額、合計、差額、分配率、圖例與加註（KL 23:31 問三）。"""
    bad = []
    C = Decimal(repr(c.fin["C"]))
    for x in c.lots:
        no = c.no[x["配地暫編"]]
        v = a24_vals(c.a24[f"地號{no}"])
        post = Decimal(repr(c.fin["重劃後單價"][x["街廓"]]))
        G, tot, area = dq(x["G"]), dq(x["a"]), dq(x["面積"])
        cur = Decimal(str(next(iter(c.cur[x["原地號"]]))))
        hh_cur = {Decimal(str(next(iter(c.cur[ln])))) for ln, h in c.hh_of.items() if h == c.hh_of[x["原地號"]]}
        if dq(x["a"]) - dq(x["a原位次"]) > 0:
            cur = next(iter(hh_cur)) if len(hh_cur) == 1 else None
        b1, b2, y1, y2 = burden(G, tot, C, post, cur)
        d = money(c, x)
        box = ("■繳納□領取" if d > 0 else "□繳納■領取" if d < 0 else "□繳納□領取") + f"新臺幣 {abs(d):,} 元"
        R = "重劃後"
        total = None if y2 is None else float(y1 + y2)
        exp = {
            "段": [None, None, None], "小段": [None, None, None], "地號": [no, None, None],
            "評定之重劃後單價(元/㎡)": [float(post), None, None], "重劃費用負擔總額(元)": [total, None, None],
            "重劃後應分配權利面積(㎡)": [float(G), None, None],
            "實配面積(㎡)": [float(area), None, None], "分配率＝G／a": [float(G / tot), None, None],
            "面積(㎡)": [float(area), None, None], "土地使用分區": [c.zoning, None, None],
            "預計繳納(領取)差額地價總額": [box, None, None],
            "抵費地負擔": ["①面積(㎡)", "重劃後單價(元/㎡)", "負擔額(元)"],
            "①": [float(b1), float(post), float(y1)],
            "公共設施用地共同負擔": ["②面積(㎡)", "③平均公告現值(元/㎡)", "負擔額(元)"],
            "②": [float(b2), None if cur is None else float(cur), None if y2 is None else float(y2)],
            "合計(元)": [None, None, total],
            "預計應繳納差額地價(元)": [None, None, float(d) if d > 0 else 0.0],
            "預計應領取差額地價(元)": [None, None, float(-d) if d < 0 else 0.0],
        }
        exp = {(R, k): e for k, e in exp.items()}
        for k, e in exp.items():
            if not same(v.get(k), e):
                bad.append(f"地號{no} 之「{k}」{v.get(k)} ≠ {e}")
        single = c.hh_of[x["原地號"]] in c.single
        for n_ in (L_A24, N_A24, N_ROUND, N_PRE):
            if (R, n_) not in v:
                bad.append(f"地號{no} 之圖例或加註缺「{n_[:12]}」")
        if ((R, N_SPLIT) in v) == single:
            bad.append(f"地號{no} 之 Σa 暫空之註 {'多' if single else '缺'}")
        if v.get((R, "製表日期：")) != ["承辦：", "股長：", "科長："]:
            bad.append(f"地號{no} 之簽欄")
        if not (b2 > 0 and b1 > 0):
            bad.append(f"地號{no} 之 ① {b1}、② {b2} 非正")
    return bad


def _run(prog, state, mapx, moedict, out):
    cmd = [sys.executable, prog, "--state", state, "--moedict", moedict, "--out", out]
    if mapx:
        cmd += ["--map", mapx]
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")


def v6(c, moedict, prog):
    """現金補償之列（KL 23:31 問二甲）、對照表之改號帶入（KL 23:37）、缺鍵即停——以子行程試之。"""
    import openpyxl
    bad = []
    tmp = tempfile.mkdtemp(prefix="cW-P006_")
    try:
        have = {c.hh_of[x["原地號"]] for x in c.lots}
        none = sorted(set(c.hh_of.values()) - have)
        if not none:
            return ["示範資料無未分配之戶，無從試現金補償"]
        n = none[0]
        ln = sorted((ln for ln, h in c.hh_of.items() if h == n), key=nkey)[0]
        code = c.state["歸戶表"][ln]
        st = dict(c.state)
        st["現金補償"] = [{"歸戶": code, "金額": 1234567}]
        sp = os.path.join(tmp, os.path.basename(c.p["state"]))
        json.dump(st, open(sp, "w", encoding="utf-8"), ensure_ascii=False)
        r = _run(prog, sp, None, moedict, os.path.join(tmp, "a"))
        if r.returncode != 0:
            bad.append(f"現金補償之試跑失敗：{r.stderr[-300:]}")
        else:
            wb = openpyxl.load_workbook(os.path.join(tmp, "a", os.path.basename(c.p["a13"])), data_only=True)
            hit = [(ws.title, rr[23]) for ws in wb for rr in rows_of(ws)[0] if rr[23] and "現金補償" in str(rr[23])]
            ws = wb[f"歸戶號{n}"]
            post_blank = all(rr[10:23] == (None,) * 13 for rr in rows_of(ws)[0])
            if hit != [(f"歸戶號{n}", "未達最小分配面積標準二分之一，發給現金補償 1,234,567 元")] or not post_blank:
                bad.append(f"現金補償之備註 {hit}、重劃後留空 {post_blank}")
        lot_code = c.state["歸戶表"][c.lots[0]["原地號"]]
        st["現金補償"] = [{"歸戶": lot_code, "金額": 100}]
        json.dump(st, open(sp, "w", encoding="utf-8"), ensure_ascii=False)
        if _run(prog, sp, None, moedict, os.path.join(tmp, "b")).returncode == 0:
            bad.append("已有分配地之戶列現金補償而未停")
        st.pop("現金補償")
        json.dump(st, open(sp, "w", encoding="utf-8"), ensure_ascii=False)
        if _run(prog, sp, None, moedict, os.path.join(tmp, "c")).returncode == 0:
            bad.append("配地結果缺「現金補償」而未停")
        x1, x2 = sorted(c.lots, key=lambda x: nkey(c.no[x["配地暫編"]]))[:2]
        n1, n2 = c.no[x1["配地暫編"]], c.no[x2["配地暫編"]]
        wb = openpyxl.load_workbook(c.p["map"])
        ws = wb["地號對照表"]
        for rr in range(2, ws.max_row + 1):
            if ws.cell(rr, 4).value == x1["配地暫編"]:
                ws.cell(rr, 6, n2)
            elif ws.cell(rr, 4).value == x2["配地暫編"]:
                ws.cell(rr, 6, n1)
        mp = os.path.join(tmp, "map.xlsx")
        wb.save(mp)
        r = _run(prog, c.p["state"], mp, moedict, os.path.join(tmp, "d"))
        if r.returncode != 0:
            bad.append(f"改號之試跑失敗：{r.stderr[-300:]}")
        else:
            wb = openpyxl.load_workbook(os.path.join(tmp, "d", os.path.basename(c.p["a24"])), data_only=True)
            gk = ("重劃後", "重劃後應分配權利面積(㎡)")
            g1 = a24_vals(wb[f"地號{n2}"]).get(gk, [None])[0]
            g2 = a24_vals(wb[f"地號{n1}"]).get(gk, [None])[0]
            if (g1, g2) != (float(dq(x1["G"])), float(dq(x2["G"]))):
                bad.append(f"改號未帶入附表 24：{n2}→{g1}、{n1}→{g2}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return bad


def run(fn, *a):
    """量測之一項 ⇒ 不合之列；量測中之例外（例：缺表）亦為不合。"""
    try:
        return fn(*a)
    except Exception as ex:  # noqa: BLE001
        return [f"量測中止：{type(ex).__name__}: {ex}"]


def main(argv):
    args = list(argv)
    prog = PROG
    if "--prog" in args:
        i = args.index("--prog")
        prog = args[i + 1]
        del args[i:i + 2]
    out, pre, moedict, tags = args[0], args[1], args[2], args[3:]
    ok = True
    for tag in tags:
        tag = f"{float(tag):g}"
        c = load(out, pre, tag)
        for name, fn in (("V0", v0), ("V1", v1), ("V2", v2), ("V3", v3), ("V4", v4), ("V5", v5)):
            bad = run(fn, c)
            ok &= not bad
            print(f"退縮 {tag} m {name} {'PASS' if not bad else 'FAIL'}" + ("" if not bad else "：" + "；".join(bad[:4])))
        bad = run(v6, c, moedict, prog)
        ok &= not bad
        print(f"退縮 {tag} m V6 {'PASS' if not bad else 'FAIL'}" + ("" if not bad else "：" + "；".join(bad[:4])))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄己　`docs/出圖/W-P.007_附表13版面.md`（逐位元組照錄）

````markdown
# W-P.007　附表 13 重劃前後土地分配清冊之版面照手冊範本（KL 2026-10-31 08:32）

- 依 KL 2026-10-31 08:32（各附表之版面一律照手冊範本；無 KL 之 Excel 範本者，以手冊之原頁為底稿於 Excel 重畫）、17:14（附表 13、24 內容定版 ⇒ 次辦版面）。
- 底稿：《市地重劃作業手冊》PDF 第 88 頁（印刷頁 78·`ops/queue` 之 `參考/手冊附表頁/附表13_重劃前後土地分配清冊_手冊PDF第88頁.png`）。
- 附表 24 之版面俟乾淨之 KL 範本（另單）。

## 產出之法

`plots/post_tables.py`（命令列同 W-P.006）。本單唯改附表 13 之版面；表之內容（值、欄名、表之分法、附表 24）與 W-P.006_補令一 定版者逐值同。

## 版面（每一表同）

| 列 | 內容 |
|---|---|
| 1 | 表名「附表 13 重劃前後土地分配清冊」（框外·粗體） |
| 2 | 冊頁「共　　冊　第　　冊　第　　頁」（框外·S〜X 欄·靠右） |
| 3 | 題（框內·A〜X 合併） |
| 4〜5 | 標籤「土地所有權人（首列登記人）姓名／國民身分證統一編號」（A〜G 合併二列·分散對齊）；姓名 H4:J4、統編 H5:J5；「住址」K4:K7（直書）；所有權人之住址 L4:X5 |
| 6〜7 | 標籤「管理人姓名／國民身分證統一編號」（A〜G 合併二列）；姓名 H6:J6、統編 H7:J7；管理人之住址 L6:X7（資料所無·留空） |
| 8〜10 | 表頭（同 W-P.006 之欄名與合併·下移三列）；直書：鄉鎮市區、小段、地號、登記面積、取配面積、持分比率、使用分區、面積、建號、二「姓名」、備註 |
| 11 起 | 資料（每表至少 5 列·不足者留空格） |
| 框下 | 附註（緊接框下一列）、簽欄（次列·日期／承辦／股長／科長／局(處)長 於 A、F、J、N、S 欄） |

- 框線：第 3 列至資料末列，每格細線、外框粗線。
- 欄寬：依手冊第 88 頁之欄寬之比（像素 ÷ 7）；列高依手冊之比；備註之字多者其列加高（自動換行）。
- 紙張：A4 橫式、寬一頁、每頁重出第 1〜10 列。

## 驗

- `verify/plots/check_W-P007.py`（L0〜L6）：附表 24 與舊版逐格同；附表 13 之內容與舊版同；合併、字、直書、格線（逕讀 xlsx 之 XML）、欄寬之比、紙張 ＝ 範本（範本之值由發單端自手冊第 88 頁量得、逐格寫於該檔）。
- `verify/plots/check_W-P006.py`：讀取之位置隨新版面改，所量之內容不變。
- `verify/plots/mutate_W-P007.py`：Ⓐ〜Ⓔ。
- `verify/plots/preview_W-P007.py`：依 Excel 之版面繪預覽。

## 未決

- 附表 24 之版面（KL 之 Excel 範本待監看窗重去識別後另單）。
- 框外之表名「附表 13 …」、每表至少 5 列：照手冊之頁面；KL 第一版確認時併呈。
````
