# W-P.006　附表 13 重劃前後土地分配清冊、附表 24 土地分配計算表（先做格式與可填之欄）

- **題**：依 KL 2026-10-30 19:28（`出圖線/KL答覆/2026-10-30_1928.md`·W-P.005 全定版、下一批附表 13、24），以 W-P.005 之「暫編 → 正式地號對照表」之正式地號為據，出附表 13、24；KL 2026-10-28 23:31 問二甲（現金補償之戶照列）、問三甲（平均公告現值暫以匯入之公告現值）納之。配地仍為階段一之終（調配之新模組未成）⇒ 先做格式與可填之欄（KL 10/28 10:48 之讀第 2 點）。
- **範圍**：新增 `plots/post_tables.py`、`verify/plots/check_W-P006.py`、`verify/plots/mutate_W-P006.py`、`verify/plots/preview_W-P006.py`、`docs/出圖/W-P.006_附表13-24.md`；**改** `plots/alloc_state.py`（本線之檔·唯增欄·既有之欄逐值不變）；⛔ 改任何他檔（含本線其餘之 `plots/*.py`·唯 `import`）；⛔ 改 `requirements.txt`；⛔ 新套件。
- **授權（逐字）**：
  - KL 2026-10-23 17:48「圖就出DXF或DWG(…)即可，所有的標題及排版由使用者編輯。還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」（README 第一節）。
  - KL 2026-10-28 23:31「2. 問2：甲」「3. 問3：土地公告現值，是要過1年才有可能會調，但是在公告時1個月內通常部會跨年度，所以採甲：以匯入之公告現值暫填。「重劃前各宗依面積加權平均」這個算法，是否是=Σ(重劃前登記面積*公告土地現值)/Σ重劃前登記面積，請參考上傳的"宜蘭縣分配計算表"」。
  - KL 2026-10-28 23:37「保留「暫編 → 正式地號對照表」」。
  - KL 2026-10-30 19:28「W-P.005：是」。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `9fd34275770b7fc53103b9eb42ba21925f823f9a`；`wip/plots` ＝ `351e8548b88bf58993966f59bda6b821ae573d6b`（已含 `9fd3427` ⇒ 工項 1 之合併應為「Already up to date」；主線若前進則必有合併之 commit）。
- **側支**：`verify/W-P.006-tables-13-24`（自 `wip/plots` 出）。單號 `W-P.006` 經 `git grep -F` 證未占用（主倉 `351e854` 無；遠端分支無；佇列唯見交接與答覆之文字）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具·核心線 `order` ＝ `W-G.9-399_補令三`）。

## §一　所據

1. **手冊**（`參考/市地重劃作業手冊.txt`）：
   - 第 2702〜2733 列：附表 13「重劃前部分依重劃前土地清冊填載」「共有土地者，應分別填載各共有人資料」「按歸戶後所有各筆土地之段、小段、地號順序，將重劃前土地資料依序填載於土地分配清冊」。
   - 第 2769 列（附表 13 之表樣）：重劃前土地情形〔鄉鎮市區、段、小段、地號、登記面積、取配面積、所有權人（姓名、國民身分證統一編號）、持分比率、評定單價〕、扣除各項負擔後應分配面積、重劃後土地情形〔使用分區、段、小段、地號、面積、評定單價、預計繳領差額地價（繳、領）、所有權人（姓名、國民身分證統一編號）、持分比率、建號〕、備註；表首「土地所有權人（首列登記人）姓名、國民身分證統一編號、住址、管理人姓名、國民身分證統一編號」「共　冊第　冊第　頁」；表末「附註：重劃後分配面積與實地指界交接土地面積如有不符，應以地政機關實際登記面積為準。」與簽欄「日期：承辦：股長：科長：局(處)長：」。
   - 第 3755〜3800 列：附表 24「以重劃後地號為準，1 筆土地填載 1 張」；Σa（原位次）、Σa'（非原位次）；l1、l2、F、S、W、Rw；「計算應繳(領)差額地價：係指實際分配面積與應分配面積之差值與重劃後評定地價之乘積」；「公共設施用地負擔：土地所有權人實際負擔之土地按當期公告土地現值計算」。
   - 第 3813〜3828 列：附表 13 之重劃後部分；「抵費地及共同負擔公共設施用地亦應編造…土地所有權人，登記為各直轄市、縣(市)有…重劃前土地欄免填寫…備註欄加註」二式（逐字見 §二 3 之常數）。
   - 第 3990〜4045 列（附表 24 之範例）：202.83＝〔340.64(1−2.32758621×0.13579793)−0×0×0−6.50×2.00〕×(1−0.07790626)；① 17.14 × 162,000 ＝ 2,776,680；② 120.67 × 69,600 ＝ 8,398,632；合計 11,175,312 ⇒ ①＝G×C÷(1−C)、②＝Σ(a＋a')−G−①（`check_W-P006` 之 V0 以此自證）。
2. **KL 之答**：見引言；另 10/26 23:14 第 1 點 甲（重劃前單價取個位；重劃後單價全精度計算、顯示二位）。問三之式：監看窗之驗算（宜蘭縣表）定權數為「計入 G 之面積」；本程式唯原位次之一宗時即該宗之現值。
3. **配地結果之來源**（同 W-P.005 §一 3）：階段一之終（段三後·`run_step_g` 之 `g_rows`）。發單端實查：
   - 二退縮皆 **33 戶中 17 戶於本階段無分配地**（其地或在道路、公園，或俟調配），16 戶有。⇒ 該 17 戶於附表 13 唯填重劃前、重劃後留空、備註留空（是否現金補償俟調配之新模組）。
   - 各宗之 a（`g_rows` 之「a 面積」）＝ 該宗之分攤登記面積（原位次）＋ 併入之面積（段三等之同戶合併·`build_parcels` 之「面積_m2」）。**併入之面積之逐筆來源（哪一原地號之哪一塊）管線未出**（`f3_k6b_stage3_log` 唯一部分）⇒ 附表 24 之重劃前唯列原位次之地號，Σa'以總數填；附表 13 之「取配面積」留空。
   - 引擎之 G 為幾何二分之解；以表上之值（S、F 二位，A、B、C 全精度）重算之差最大 0.012 ㎡（二退縮 57 宗）⇒ 計算式之「G」照引擎之值，量測容差 0.02。
   - 本示範資料：一戶之各宗之共有人與持分皆同（12 共有戶）、各宗之公告現值皆 33,321 ⇒ 重劃後之持分按原共有狀態、平均公告現值皆可定；不同者程式即停或留空（見 §二 3）。
4. **既有之函式**（唯讀·`import`）：`plots/prelim_maps.py`（`load_cadastre`、`households`、`household_members`、`owner_rows`、`load_price_zones`、`landno_key`、`_grid`、`_page`、`C_*`、`CASE_PARAMS`、`SourceError`）；`plots/owner_index.py`（`load_strokes`、`number_households`）；`plots/post_maps.py`（`load_state`、`tag_of`、`entries_of`、`s_order`、`default_numbers`、`read_map`、`KIND_*`）；`verify/stepg_pipeline._compute_v3_finance`（B、C、單價·`alloc_state` 呼叫之）。
5. **內容之判斷**（依手冊、KL 之答或資料；未經 KL 逐項確認者於第一版併呈）：
   - 附表 13：一戶一表（表名「歸戶號 N」），另一表「縣有」；首列登記人 ＝ 該戶地號最小之宗之登記次序最先者。重劃後之列唯該戶之分配地（正式地號序），應分配面積 ＝ G。抵費地與公設之所有權人「花蓮縣」、持分「1/1」、使用分區（抵費地 ＝ 案之分區；道路、公園 ＝ 其區塊之分類）。
   - 附表 24：唯分配地（抵費地與公設無 G 之計算）；代表人 ＝「首列登記人」或「○○○等 N 人」；Σa 與 Σa' 見 §一 3；**「評定之重劃前單價」取個位（同附表 18），「原位置重劃前地價」為計算 A 所用之全精度、顯示二位**（引擎之 A 用全精度·核心線之裁定）——二者並列，第一版併呈；W ＝ 引擎之「W(m)」（查 Rw 之寬），Rw 以小數四位示之。
   - 差額地價 ＝（面積 − G）× 重劃後單價（元·四捨五入）；本階段面積 ＝ G ⇒ 皆 0。
   - 「共　冊第　冊第　頁」、建號、法定空地面積、共有人申請單獨分配、預配位置之單價、重劃後之段與小段：資料所無或本階段無 ⇒ 留空。

## §二　規格

1. **改 `plots/alloc_state.py`**：逐位元組 ＝ 附錄丁。所增：分配地之「a」「a原位次」「併入面積」「重劃前區段」「F」「W」「Rw」「l側」「l正」；檔之「財務」「歸戶表」「現金補償」（＝ `[]`）「現金補償之來源」。既有之鍵逐值不變（發單端以舊版之輸出比對：刪新鍵後二退縮逐值同）。
2. **新增 `plots/post_tables.py`**：逐位元組 ＝ 附錄戊。`python plots/post_tables.py --state <O>/配地結果_退縮<t>m.json --moedict <json> --out <O> [--map <xlsx>]`（約 15 秒）⇒ `附表13_重劃前後土地分配清冊_退縮<t>m.xlsx`、`附表24_土地分配計算表_退縮<t>m.xlsx`。
3. 要式（皆在附錄戊）：配地結果缺「財務」「歸戶表」「現金補償」或分配地缺 G 式之項 ⇒ 停；歸戶表與重劃前之戶非一一對應 ⇒ 停；現金補償之歸戶不明、金額非正整數、重複、或該戶已有分配地 ⇒ 停；一戶之各宗之（姓名、統編、持分）不同 ⇒ 停；平均公告現值於有併入而該戶各宗現值不一時留空（俟併入之逐筆來源）。備註之字：抵費地「依平均地權條例第 60 條規定，由土地所有權人以未建築土地折價抵付之土地」、公設「依平均地權條例第 60 條規定，由土地所有權人共同負擔取得土地」、現金補償「未達最小分配面積標準二分之一，發給現金補償 {金額:,} 元」；附表 24 表下「①＝G×C÷(1−C)；②＝(Σa＋Σa')−G−①；③＝平均公告現值」「暫以匯入時之公告現值計，公告期滿後應以當期公告現值更正」。
4. **新增 `verify/plots/check_W-P006.py`**：逐位元組 ＝ 附錄甲（V0〜V6·獨立於 `plots/`·U_LAND 自讀·歸戶號與區段單價取重劃前顏色對照表、重劃後之歸戶號取重劃後顏色對照表）。
5. **新增 `verify/plots/mutate_W-P006.py`**：逐位元組 ＝ 附錄乙（Ⓐ〜Ⓔ）。
6. **新增 `verify/plots/preview_W-P006.py`**：逐位元組 ＝ 附錄丙。
7. **新增 `docs/出圖/W-P.006_附表13-24.md`**：逐位元組 ＝ 附錄己。
8. 發單端之原型（暫存·⛔ 入倉·於 `351e854` 之上）已依附錄實作，實得：
   - `alloc_state`：同 W-P.005（0 m 宗 35〔分配地 29、抵費地 6〕、3.5 m 34〔28、6〕；略皆 `['R1-抵費地-2']`）；B ＝ 0.17104255833716267、C ＝ 0.0913189310870504；重劃前單價 a 43909.2308486259、b 37322.846221332016。
   - `post_maps`：地號之序同 W-P.005 §二 7（3.5 m 1〜39、0 m 1〜40）；`check_W-P005` 18/18（新版之配地結果）。
   - `post_tables`：二退縮皆「附表 13 戶 33（有分配地 16、現金補償 0）＋縣有 11」；附表 24 0 m 29 張、3.5 m 28 張。例（3.5 m 地號 5·628-36·歸戶號 32·5 人共有）：G 638.61、Σ 1047.00（947.97＋99.03）、① 64.18、② 344.21、③ 33,321、負擔額 4,893,467＋11,469,421＝16,362,888、差額 0；計算式「638.61=〔1047.00×(1−1.73644529×0.17104256)−33.25×1.00×1.0000−19.46×0.00〕×(1−0.09131893)」。
   - `check_W-P006` 14/14（二退縮各 V0〜V6）；`mutate_W-P006`：成果綠、Ⓐ 紅 V5、Ⓑ 紅 V4、V5、Ⓒ 紅 V4、Ⓓ 紅 V3、Ⓔ 紅 V6。
   - 預覽 `W-P.006_附表13-24_退縮0m.png` sha256 `72c0af1e224ef89bb27cdc41e36b7ef8ea7b22424123ec92371343ff95702307`、`_退縮3.5m.png` `438ccaaac316b494d46873063e7123962a89811ceb0a9ade60bdcdb00616e69d`（重出逐位元組同）。
   - 環境：同 W-P.005 §二 7（venv＋`numpy<2.3`）。費時：`alloc_state` 約 5 分鐘、`post_tables` 每退縮約 15 秒、`check_W-P006` 二退縮約 2 分鐘、`mutate_W-P006` 約 5 分鐘。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.006-tables-13-24`；`git merge --no-edit origin/wip/s1-endpart`（記其結果；有衝突即停機）。
2. **程式**：§二 1、2、4〜7。附錄之取用法：自本單擷取該附錄之開欄（甲〜戊為三個反引號加 `python`；己為四個反引號加 `markdown`）與其閉欄（同數之反引號）間之文字，末尾一換行；bytes 與 sha256 須合：
   - 甲 `verify/plots/check_W-P006.py`：26177 bytes·`04cd3db20113d9a05fda06d35e90dffcc3789a4c3f03f2547700c60c13ab1958`
   - 乙 `verify/plots/mutate_W-P006.py`：4266 bytes·`25854029016d81d07e7ceee721bc0fcef9272667404a35aa5a8a9190ba2c5858`
   - 丙 `verify/plots/preview_W-P006.py`：4054 bytes·`8f6a8573a2bb0ff8e9926e9bd9f59cf3c1a14f4e3f8081b298f3624f97ecf2cb`
   - 丁 `plots/alloc_state.py`：11655 bytes·`6ab75de56ceb1bb0d63c1749aed26b9ee410b60b48161a11b9c462785c1f9260`
   - 戊 `plots/post_tables.py`：24041 bytes·`3ce914e82c7b7f324aec952b6350984a019cb4baa777fbbab0124332e8e3dd8d`
   - 己 `docs/出圖/W-P.006_附表13-24.md`：3826 bytes·`9683f80f55eeb382d5bb5a5daae1ee24ae4be89016a3a1d6fd73966d7d0f01bf`
   不合即停機上呈；⛔ 改一字。`python -m py_compile` 五 `.py` 皆過。
3. **量測**（`<py>` ＝ §二 8 之 venv 之直譯器）：
   - `<py> plots/fetch_moedict.py <M>`；`<py> plots/prelim_maps.py --out <P> --moedict <M>/dict-revised.json`；
   - `<py> plots/alloc_state.py --out <O> --setback 0 --setback 3.5`（印如 §二 8）；
   - 二退縮各 `<py> plots/post_maps.py --state <O>/配地結果_退縮<t>m.json --pre-dxf <P>/重劃前圖.dxf --moedict <M>/dict-revised.json --out <O>`（地號之序 ＝ W-P.005 §二 7）；
   - 二退縮各 `<py> plots/post_tables.py --state <O>/配地結果_退縮<t>m.json --moedict <M>/dict-revised.json --out <O>`（印如 §二 8）；
   - `<py> verify/plots/check_W-P006.py <O> <P> <M>/dict-revised.json 0 3.5` ⇒ 14 項皆 PASS、結束碼 0；
   - 另照舊：`check_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json 0 3.5`（18/18）、`check_W-P001.py`（12/12）、`check_W-P002.py`（8/8）、`check_W-P003.py`（8/8）、`check_W-P004.py`（8/8）。
4. **故意錯誤之測**：`<py> verify/plots/mutate_W-P006.py <O> <P> <M>/dict-revised.json <拋棄式之工作目錄>` ⇒ 成果綠；Ⓐ〜Ⓔ 皆紅（所紅之項記之）；結束碼 0。
5. **差異閘**（README 第四節）：`git diff --name-status <實際併入之主線之 sha（應為 9fd3427…）> <側支之端>` 每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status 351e854 <側支之端>` 唯 `M plots/alloc_state.py` 與 §二 之五新檔（`A`）；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：`<py> verify/plots/preview_W-P006.py <O> <PNG 目錄> 0 3.5`，其二輸出入佇列之 `出圖線/成果/`（sha256 應 ＝ §二 8；不同者記之、⛔ 停）。
7. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
8. **回報**：`出圖線/reports/W-P.006_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、差異閘與對照組、合併之結果、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲〜己之 bytes 或 sha256 不合；或 V0〜V6 於成果不過而非程式之誤；或 §二 8 之實得不合（主線前進致配地變者亦停·記其差）。
3. `plots/alloc_state.py`、`plots/post_maps.py` 或 `plots/post_tables.py` 報 `SourceError` 或配地流程之 `RuntimeError`——⛔ 自擬填法、⛔ 設 `WV_BAKE`。
4. 須改任何他檔、或須新套件（numpy 之版本唯限於倉外之 venv）。
5. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P006.py`（逐位元組照錄）

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
N_A24 = "暫以匯入時之公告現值計，公告期滿後應以當期公告現值更正"
L_A24 = "①＝G×C÷(1−C)；②＝(Σa＋Σa')−G−①；③＝平均公告現值"
H6 = ("鄉鎮市區", "段", "小段", "地號", "登記面積(㎡)", "取配面積(㎡)", "所有權人", None, "持分比率", "評定單價(元／㎡)",
      None, "使用分區", "段", "小段", "地號", "面積(㎡)", "評定單價(元／㎡)", "預計繳領差額地價", None, "所有權人", None,
      "持分比率", "建號", None)
H5 = ("重劃前土地情形",) + (None,) * 9 + ("扣除各項負擔後應分配面積(㎡)", "重劃後土地情形") + (None,) * 11 + ("備註",)
H7 = (None,) * 6 + ("姓名", "國民身分證統一編號") + (None,) * 9 + ("繳（元）", "領（元）", "姓名", "國民身分證統一編號") + (None,) * 3
FIRST = 8
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
    return c


def rows_of(ws, first=FIRST):
    out = []
    r = first
    while any(ws.cell(r, k).value is not None for k in range(1, 25)):
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
    want = [f"歸戶號{n}" for n in hh] + ["縣有"]
    if c.a13.sheetnames != want:
        return [f"附表 13 之表 {c.a13.sheetnames}"]
    for ws in c.a13:
        if ws.cell(1, 1).value != T_A13:
            bad.append(f"{ws.title} 之題")
        for rr, h in ((5, H5), (6, H6), (7, H7)):
            if tuple(ws.cell(rr, k).value for k in range(1, 25)) != h:
                bad.append(f"{ws.title} 列 {rr} 之表頭")
        rows, r = rows_of(ws)
        if ws.cell(r + 1, 1).value != N_A13 or [ws.cell(r + 3, k).value for k in (1, 5, 9, 13, 17)] != \
                ["日期：", "承辦：", "股長：", "科長：", "局(處)長："]:
            bad.append(f"{ws.title} 之附註或簽欄")
        if ws.title == "縣有":
            if ws.cell(3, 4).value != COUNTY:
                bad.append("縣有之所有權人")
            continue
        n = int(ws.title[3:])
        lns = sorted((ln for ln, h in c.hh_of.items() if h == n), key=nkey)
        f = c.own[lns[0]][0]
        got = (ws.cell(3, 4).value, ws.cell(3, 9).value, ws.cell(3, 13).value, ws.cell(4, 4).value, ws.cell(4, 9).value)
        if got != (f[0], f[1], f[3], f[4], f[5]):
            bad.append(f"{ws.title} 之首列登記人 {got}")
    return bad


def v2(c):
    """附表 13 之重劃前：每戶之各宗 × 各所有權人一列（地號序·登記次序）；取配面積留空。"""
    bad = []
    for n in sorted(set(c.hh_of.values())):
        ws = c.a13[f"歸戶號{n}"]
        rows, _ = rows_of(ws)
        got = [r[:10] for r in rows if r[3] is not None]
        want = []
        for ln in sorted((ln for ln, h in c.hh_of.items() if h == n), key=nkey):
            for nm, uid, sh, *_ in c.own[ln]:
                want.append((c.place[ln][0], c.place[ln][1], None, ln, c.area[ln], None, nm, uid, sh, c.price_of[ln]))
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
    ws = c.a13["縣有"]
    rows, _ = rows_of(ws)
    want = []
    for x in c.others:
        want.append((c.no[x["配地暫編"]], c.zoning, c.fin["重劃後單價"][x["街廓"]], N_OFF, float(dq(x["面積"]))))
    for b in c.public:
        from shapely.geometry import Polygon
        want.append((c.no[b], c.state["街廓"][b]["分類"], None, N_PUB, float(dq(Polygon(c.state["街廓"][b]["多邊形"]).area))))
    want.sort(key=lambda t: nkey(t[0]))
    got = [(r[14], r[11], r[16], r[23], r[15]) for r in rows]
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
        if ws.title != "縣有" and any(r[23] is not None for r in rows_of(ws)[0]):
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
        a0, tot = dq(x["a原位次"]), dq(x["a"])
        P, K = "重劃前", "計算分配有關資料"
        exp = {
            ("", "歸戶號"): [c.hh_of[ln], "所有權(代表)人姓名", rep], (P, "段"): [c.place[ln][1], None, None],
            (P, "小段"): [None, None, None], (P, "地號"): [ln, None, None],
            (P, "登記面積(㎡)"): [c.area[ln], None, None], (P, "分配面積(㎡)"): [float(a0), None, None],
            (P, "共有人申請單獨分配持分比例"): [None, None, None], (P, "持分面積(㎡)"): [None, None, None],
            (P, "法定空地面積(㎡)"): [None, None, None],
            (P, "當期公告現值(元/㎡)"): [float(next(iter(c.cur[ln]))), None, None],
            (P, "評定之重劃前單價(元/㎡)"): [c.price_of[ln], None, None],
            "Σa（原位次）(㎡)": [float(a0), None, None], "Σa'（併入）(㎡)": [float(tot - a0), None, None],
            "Σ(a＋a')(㎡)": [float(tot), None, None], "原位置重劃前地價(元/㎡)": [float(pre), None, None],
            "預配位置重劃前原地平均單價(元/㎡)": [None, None, None], "重劃後宗地地價(元/㎡)": [float(post), None, None],
            "A＝重劃後宗地地價÷重劃前地價": [float(A), None, None], "B": [float(B), None, None],
            "C": [float(C), None, None], "1−C": [float(1 - C), None, None], "S(m)": [float(dq(x["S"])), None, None],
            "W(m)": [float(dq(x["W"])), None, None], "F(m)": [float(dq(x["F"])), None, None],
            "l1": [float(dq(x["l側"])), None, None], "l2": [float(dq(x["l正"])), None, None],
            "Rw": [float(dq(x["Rw"] / 100, 4)), None, None],
        }
        exp = {(k if isinstance(k, tuple) else (K, k)): e for k, e in exp.items()}
        for k, e in exp.items():
            if not same(v.get(k), e):
                bad.append(f"{ws.title} 之「{k}」{v.get(k)} ≠ {e}")
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
        exp = {
            "段": [None, None, None], "小段": [None, None, None], "地號": [no, None, None],
            "評定之重劃後單價(元/㎡)": [float(post), None, None], "重劃後應分配權利面積 G(㎡)": [float(G), None, None],
            "實配面積(㎡)": [float(area), None, None], "分配率＝G／Σ(a＋a')": [float(G / tot), None, None],
            "面積(㎡)": [float(area), None, None], "土地使用分區": [c.zoning, None, None],
            "預計繳納（領取）差額地價總額": [box, None, None],
            "抵費地負擔 ①": [float(b1), float(post), float(y1)],
            "公共設施用地共同負擔 ②（單價 ③）": [float(b2), None if cur is None else float(cur),
                                         None if y2 is None else float(y2)],
            "合計（重劃費用負擔總額）": [None, None, None if y2 is None else float(y1 + y2)],
            "預計應繳納差額地價": [None, None, float(d) if d > 0 else 0.0],
            "預計應領取差額地價": [None, None, float(-d) if d < 0 else 0.0],
            "重劃費用負擔": ["面積(㎡)", "單價(元/㎡)", "負擔額(元)"],
        }
        exp = {(R, k): e for k, e in exp.items()}
        for k, e in exp.items():
            if not same(v.get(k), e):
                bad.append(f"地號{no} 之「{k}」{v.get(k)} ≠ {e}")
        if (R, L_A24) not in v or (R, N_A24) not in v:
            bad.append(f"地號{no} 之圖例或加註")
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
            gk = ("重劃後", "重劃後應分配權利面積 G(㎡)")
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

## 附錄乙　`verify/plots/mutate_W-P006.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.006 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓔ 共 5 種變異體須各紅（量測 ＝ check_W-P006.py 之 V0〜V6）。

命令列：python verify/plots/mutate_W-P006.py <成果目錄> <重劃前成果目錄> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py、plots/post_maps.py、plots/post_tables.py 之 --out（⛔ 改之）。
  唯驗退縮 3.5 m。各變異體 ＝ plots/ 之複本（於工作目錄）之 post_tables.py 改一處之字（MUTANTS）後，以子行程重出
  附表 13、24 於工作目錄，再以 check_W-P006 量之（V6 之子行程亦用該變異體）；V6 費時，唯成果與 Ⓔ 量之。
結束碼：成果綠且 5 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P006", os.path.join(HERE, "check_W-P006.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"

MUTANTS = [   # (名, 說明, 原字, 改字, 跑 V6 否)
    ("Ⓐ", "抵費地負擔面積漏 ÷(1−C)", "b1 = q(G * C / (1 - C), 2)", "b1 = q(G * C, 2)", False),
    ("Ⓑ", "附表 24 漏一宗", "    for e in es:\n        no, ln = numbers", "    for e in es[1:]:\n        no, ln = numbers",
     False),
    ("Ⓒ", "地價比 A 以個位之重劃前單價計", "    A = post / pre\n", "    A = post / q(pre, 0)\n", False),
    ("Ⓓ", "抵費地與公設之備註互換", "NOTE_OFFSET if e[\"類別\"] == KIND_OFFSET else NOTE_PUBLIC",
     "NOTE_PUBLIC if e[\"類別\"] == KIND_OFFSET else NOTE_OFFSET", False),
    ("Ⓔ", "現金補償之備註漏寫", "note = NOTE_CASH.format(cash[k]) if k in cash else None", "note = None", True),
]


def _measure(out, pre, moe, prog, with_v6):
    c = chk.load(out, pre, TAG)
    red = []
    for name, fn in (("V0", chk.v0), ("V1", chk.v1), ("V2", chk.v2), ("V3", chk.v3), ("V4", chk.v4), ("V5", chk.v5)):
        if chk.run(fn, c):
            red.append(name)
    if with_v6 and chk.run(chk.v6, c, moe, prog):
        red.append("V6")
    return red


def main(argv):
    out, pre, moe, work = argv
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(work)
    ok = True
    base = _measure(out, pre, moe, chk.PROG, True)
    print(f"成果：{'綠' if not base else '紅 ' + '、'.join(base)}")
    ok &= not base
    src = open(os.path.join(REPO, "plots", "post_tables.py"), encoding="utf-8").read()
    for name, desc, a, b, v6 in MUTANTS:
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
        for k in ("state", "map", "color"):
            shutil.copy(os.path.join(out, chk.FMT[k].format(TAG)), o)
        prog = os.path.join(pdir, "post_tables.py")
        # 複本之 plots/ 不在倉內 ⇒ prelim_maps 之 REPO 指向複本之上層；以符號連結補 data／verify（唯讀）
        for sub in ("data", "verify"):
            os.symlink(os.path.join(REPO, sub), os.path.join(d, sub))
        r = subprocess.run([sys.executable, prog, "--state", os.path.join(o, chk.FMT["state"].format(TAG)),
                            "--moedict", moe, "--out", o], capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            red = ["出表即停"]
        else:
            red = _measure(o, pre, moe, prog, v6)
        print(f"{name}（{desc}）：{'紅 ' + '、'.join(red) if red else '綠（未捕）'}")
        ok &= bool(red)
    print("結論：" + ("成果綠、變異體皆紅" if ok else "不合"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄丙　`verify/plots/preview_W-P006.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.006 之預覽 PNG（單 §三 6）：附表 13（一戶）與附表 24（一張）之截取。

命令列：python verify/plots/preview_W-P006.py <成果目錄> <PNG 之輸出目錄> <退縮…>
輸出：W-P.006_附表13-24_退縮<t>m.png（每一退縮一檔）。
所取：附表 24 中所有權人最多之宗（同者取地號小者）之一張，及附表 13 中該宗所屬之戶之一表。
預覽之標題唯供 KL 一眼辨表，⛔ 屬附表之內容；格之合併與框線以 Excel 開啟為準。
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

for _f in ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",):
    if os.path.exists(_f):
        font_manager.fontManager.addfont(_f)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=_f).get_name()

A13 = "附表13_重劃前後土地分配清冊_退縮{}m.xlsx"
A24 = "附表24_土地分配計算表_退縮{}m.xlsx"
OUT = "W-P.006_附表13-24_退縮{}m.png"


def _fmt(cell):
    v = cell.value
    if v is None:
        return ""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        nf = cell.number_format
        if nf in ("#,##0.00",):
            return f"{v:,.2f}"
        if nf == "#,##0":
            return f"{v:,.0f}"
        if nf == "0.00000000":
            return f"{v:.8f}"
        if nf == "0.0000":
            return f"{v:.4f}"
        if nf == "0.00":
            return f"{v:.2f}"
        if nf == "0.00%":
            return f"{v * 100:.2f}%"
    return str(v)


def pick(wb24):
    """⇒ (表名, 地號)：所有權人最多（代表人「等N人」之 N）者，同者地號小者。"""
    best = None
    for ws in wb24:
        rep = str(ws.cell(2, 4).value or "")
        n = int(rep.rsplit("等", 1)[1][:-1]) if "等" in rep else 1
        no = ws.title[2:]
        key = (-n, tuple(int(p) for p in no.split("-")))
        if best is None or key < best[0]:
            best = (key, ws.title, no)
    return best[1], best[2]


def main(argv):
    import openpyxl
    out, png, tags = argv[0], argv[1], argv[2:]
    os.makedirs(png, exist_ok=True)
    for t in tags:
        t = f"{float(t):g}"
        wb24 = openpyxl.load_workbook(os.path.join(out, A24.format(t)))
        wb13 = openpyxl.load_workbook(os.path.join(out, A13.format(t)))
        name24, no = pick(wb24)
        ws24 = wb24[name24]
        ws13 = next(ws for ws in wb13 if any(ws.cell(r, 15).value == no for r in range(8, ws.max_row + 1)))
        fig = plt.figure(figsize=(26, 20))
        ax1 = fig.add_axes([0.01, 0.52, 0.98, 0.45])
        ax2 = fig.add_axes([0.01, 0.01, 0.6, 0.48])
        last = max(r for r in range(1, ws13.max_row + 1) if any(ws13.cell(r, c).value is not None for c in range(1, 25)))
        cells = [[_fmt(ws13.cell(r, c)) for c in range(1, 25)] for r in range(3, last + 1)]
        ax1.axis("off")
        ax1.set_title(f"附表 13　{ws13.title}（退縮 {t} m）｜　{ws13['A1'].value}", fontsize=14, loc="left")
        tb = ax1.table(cellText=cells, loc="upper left", cellLoc="center")
        tb.auto_set_font_size(False)
        tb.set_fontsize(6.5)
        tb.scale(1, 1.5)
        cells = [[_fmt(ws24.cell(r, c)) for c in range(1, 5)] for r in range(2, ws24.max_row + 1)
                 if any(ws24.cell(r, c).value is not None for c in range(1, 5))]
        ax2.axis("off")
        ax2.set_title(f"附表 24　{name24}（退縮 {t} m）｜　{ws24['A1'].value}", fontsize=14, loc="left")
        tb = ax2.table(cellText=cells, loc="upper left", cellLoc="left", colWidths=[0.28, 0.62, 0.05, 0.05])
        tb.auto_set_font_size(False)
        tb.set_fontsize(8)
        tb.scale(1, 1.25)
        p = os.path.join(png, OUT.format(t))
        fig.savefig(p, dpi=80)
        plt.close(fig)
        print(f"輸出 {p}（{ws13.title}、{name24}）")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄丁　`plots/alloc_state.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005　配地結果之取出（重劃後三圖層與地號對照表之輸入）。

命令列：python plots/alloc_state.py --out <目錄> --setback <退縮公尺> [--setback …]
輸出（皆寫至 --out，⛔ 入倉）：配地結果_退縮<退縮>m.json（每一退縮一檔）。

所據：出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md（§一 3、§二 1）。
  來源 ＝ 既有之無畫面之配地流程（verify/ 之管線·唯呼叫·⛔ 改），依 verify/run_verification.py 之 main
  之序：load_snapshot → harvest → build_pipeline → build_param_table → build_ownership →
  build_build_parcels → run_corner_pk_k6b → run_step_g（eff_min_build_by_blk＝{}）。
  所取者 ＝ 階段一之終（段三後·調配〔核心線階段二〕之前）之 g_rows；調配之新模組入主線後，唯改本檔之來源。
  「推進側別」＝「抵費地」之列 ⇒ 類別「抵費地」（同 app.py export_allocated_dxf）；他列 ⇒「分配地」。
  面積二位四捨五入為 0.00 之列不成宗，列於「略」（印之·⛔ 靜默）。
  W-P.005_補令一（KL 2026-10-30 08:00）：分配地加「S」（G 值計算之臨正面道路寬度·g_rows 之 S(m)）與
  「街角第1宗側別」（g_rows 之「第1筆街角」＝是者之「街角側別」：左／右）；街廓加「側面道路線」（CAD 之
  side_lines_by_side·左／右·各 [p1, p2]）——供公告分配地籍線之「寬」（顯示 S）與街角宗之「深」（含道路截角）。
  W-P.006（附表 13、24·KL 2026-10-30 19:28）：分配地加 G 式之各項（「a」＝g_rows 之 a 面積、「a原位次」＝該宗之
  分攤登記面積〔build_parcels·二位〕、「併入面積」＝ a − a原位次、「重劃前區段」、「F」、「W」〔g_rows 之 W(m)·Rw 所查〕、
  「Rw」〔%〕、「l側」、「l正」）；檔加「財務」（stepg_pipeline._compute_v3_finance 之 B、C、重劃後單價〔街廓〕、
  重劃前單價〔區段〕·全精度·同 run_step_g 所用）、「歸戶表」（地號 → 歸戶之代號·t8_ownership_map）、
  「現金補償」（階段一未判 ⇒ []；調配之新模組入主線後由本檔填之·每項 {"歸戶", "金額"}）。
缺值一律報錯停止（⛔ 靜默補值）。
"""
import argparse
import contextlib
import io
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "verify"))

SOURCE_NOTE = "階段一之終（段三後·未經調配）：verify/stepg_pipeline.run_step_g 之 g_rows"
CASH_NOTE = "階段一未判現金補償（調配之新模組未成）"
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_SIDE = "抵費地"
OUT_FMT = "配地結果_退縮{}m.json"
SIDE_NAME = {"left": "左", "right": "右"}
CORNER_SIDE = {"左側": "左", "右側": "右"}


class SourceError(RuntimeError):
    """資料與單之所據不符 ⇒ 停機上呈。"""


def q2(x):
    return float(Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def tag_of(setback):
    s = f"{setback:g}"
    return s


def run_pipeline(setbacks):
    """⇒ (cb_by, cad, omap, {退縮: g_rows}, {退縮: build_parcels}, 財務)。管線之印出一律收於記憶體（⛔ 擾本程式之輸出）。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk_k6b
    from stepg_pipeline import run_step_g, _compute_v3_finance
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        snapshot = rv.load_snapshot()
        ns, fake_st = harvest()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        fin = _compute_v3_finance(ns, snapshot, list(cb_by.values()), cad)
        rows, bps = {}, {}
        for sb in setbacks:
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            _d, _s, _o, win, forced, _tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snapshot)
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3,
                            win, forced, sb, eff_min_build_by_blk={})
            rows[sb] = sg["g_rows"]
            bps[sb] = bp3
        omap = dict(fake_st.session_state["t8_ownership_map"])
    return cb_by, cad, omap, rows, bps, fin


def finance_of(fin):
    out = {"B": float(fin["B"]), "C": float(fin["C"]),
           "重劃後單價": {k: float(v) for k, v in sorted(fin["post_price_by_block"].items())},
           "重劃前單價": {k: float(v) for k, v in sorted(fin["pre_price_by_zone"].items())}}
    if not (0 < out["B"] < 1 and 0 < out["C"] < 1) or not out["重劃後單價"] or not out["重劃前單價"]:
        raise SourceError(f"財務之值不合：B {out['B']}、C {out['C']}")
    return out


def blocks_of(cb_by, cad):
    alloc = cad.get("alloc_dir_by_block") or {}
    front = cad.get("front_lines") or {}
    sides = cad.get("side_lines_by_side") or {}
    out = {}
    for lbl in sorted(cb_by):
        b = cb_by[lbl]
        vs = b.get("vertices") or []
        if len(vs) < 3:
            raise SourceError(f"街廓 {lbl} 之頂點不足")
        cat = b.get("category")
        if not cat:
            raise SourceError(f"街廓 {lbl} 無分類")
        d = {"分類": cat, "面積": float(b["area_m2"]), "多邊形": [[float(x), float(y)] for x, y in vs]}
        if lbl in alloc:
            if lbl not in front:
                raise SourceError(f"街廓 {lbl} 有宗地分配線而無正面臨路線")
            d["宗地分配線方向"] = [float(v) for v in alloc[lbl]]
            d["正面臨路線"] = [[float(v) for v in front[lbl]["p1"]], [float(v) for v in front[lbl]["p2"]]]
            sl = {}
            for side, nm in SIDE_NAME.items():
                if side in sides.get(lbl, {}):
                    s = sides[lbl][side]
                    sl[nm] = [[float(v) for v in s["p1"]], [float(v) for v in s["p2"]]]
            d["側面道路線"] = sl
        out[lbl] = d
    return out


def own_area_of(build):
    """build_parcels ⇒ {暫編地號: 分攤登記面積_m2}（缺 ⇒ 不入；用時缺即停）。"""
    out = {}
    for b in build:
        k = b.get("暫編地號")
        if k in out:
            raise SourceError(f"build_parcels 之暫編地號 {k} 重複")
        if k and b.get("分攤登記面積_m2") is not None:
            out[k] = float(b["分攤登記面積_m2"])
    return out


def lots_of(g_rows, blocks, omap, own_area):
    lots, dropped = [], []
    seen = set()
    for r in g_rows:
        pid = r.get("暫編地號")
        if not pid or pid in seen:
            raise SourceError(f"配地之列之暫編地號缺或重複：{pid!r}")
        seen.add(pid)
        blk = r.get("所屬街廓")
        if blk not in blocks or "宗地分配線方向" not in blocks[blk]:
            raise SourceError(f"{pid} 之街廓 {blk!r} 非可分配之街廓")
        cs = r.get("cut_coords") or []
        if len(cs) < 3:
            raise SourceError(f"{pid} 無多邊形")
        area = q2(r["幾何面積(㎡)"])
        kind = KIND_OFFSET if r.get("推進側別") == OFFSET_SIDE else KIND_LOT
        if area == 0:
            dropped.append({"配地暫編": pid, "街廓": blk, "類別": kind, "幾何面積": float(r["幾何面積(㎡)"])})
            continue
        d = {"配地暫編": pid, "街廓": blk, "類別": kind, "面積": area,
             "多邊形": [[float(x), float(y)] for x, y in cs]}
        if kind == KIND_LOT:
            ln = r.get("原地號")
            if not ln or ln not in omap:
                raise SourceError(f"{pid} 之原地號 {ln!r} 不在歸戶表")
            w = r.get("宗地寬度(m)")
            if w is None or float(w) <= 0:
                raise SourceError(f"{pid} 之宗地寬度缺")
            s = r.get("S(m)")
            if s is None or float(s) <= 0:
                raise SourceError(f"{pid} 之 S 缺")
            d.update({"原地號": ln, "歸戶": omap[ln], "G": q2(r["G(㎡)"]), "宗地寬度": q2(w), "S": q2(s)})
            if pid not in own_area:
                raise SourceError(f"{pid} 無分攤登記面積（build_parcels）")
            a = Decimal(repr(float(r["a 面積(㎡)"]))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            a0 = Decimal(repr(own_area[pid])).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            if a <= 0 or a0 <= 0 or a0 > a:
                raise SourceError(f"{pid} 之 a {a}、分攤登記面積 {a0} 不合")
            zone = r.get("重劃前區段")
            if not zone:
                raise SourceError(f"{pid} 之重劃前區段缺")
            for k in ("F(m)", "W(m)", "Rw(%)", "l₁ 側面尺度", "l₂ 正面尺度"):
                if r.get(k) is None or float(r[k]) < 0:
                    raise SourceError(f"{pid} 之 {k} 缺或負")
            d.update({"a": float(a), "a原位次": float(a0), "併入面積": float(a - a0), "重劃前區段": zone,
                      "F": float(r["F(m)"]), "W": float(r["W(m)"]), "Rw": float(r["Rw(%)"]),
                      "l側": float(r["l₁ 側面尺度"]), "l正": float(r["l₂ 正面尺度"])})
            first = r.get("第1筆街角")
            if first == "是":
                side = CORNER_SIDE.get(r.get("街角側別"))
                if side is None:
                    raise SourceError(f"{pid} 為街角第 1 宗而街角側別 {r.get('街角側別')!r} 不明")
                if side not in blocks[blk]["側面道路線"]:
                    raise SourceError(f"{pid} 為{side}側街角第 1 宗而街廓 {blk} 無該側之側面道路線")
                d["街角第1宗側別"] = side
            elif first != "否":
                raise SourceError(f"{pid} 之「第1筆街角」{first!r} 非是／否")
        lots.append(d)
    return lots, dropped


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 配地結果之取出")
    ap.add_argument("--out", required=True)
    ap.add_argument("--setback", type=float, action="append", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    cb_by, cad, omap, rows, bps, fin = run_pipeline(a.setback)
    blocks = blocks_of(cb_by, cad)
    finance = finance_of(fin)
    for sb in a.setback:
        lots, dropped = lots_of(rows[sb], blocks, omap, own_area_of(bps[sb]))
        doc = {"退縮_m": sb, "來源": SOURCE_NOTE, "街廓": blocks, "宗": lots, "略": dropped,
               "財務": finance, "歸戶表": {k: omap[k] for k in sorted(omap)},
               "現金補償": [], "現金補償之來源": CASH_NOTE}
        p = os.path.join(a.out, OUT_FMT.format(tag_of(sb)))
        with open(p, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        n_off = sum(1 for x in lots if x["類別"] == KIND_OFFSET)
        print(f"退縮 {tag_of(sb)} m：宗 {len(lots)}（分配地 {len(lots) - n_off}、抵費地 {n_off}）；"
              f"略 {[x['配地暫編'] for x in dropped]}")
        print(f"輸出 {p}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄戊　`plots/post_tables.py`（逐位元組照錄）

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
NOTE_A24 = "暫以匯入時之公告現值計，公告期滿後應以當期公告現值更正"
LEGEND_A24 = "①＝G×C÷(1−C)；②＝(Σa＋Σa')−G−①；③＝平均公告現值"
SIGN_A13 = ("日期：", "承辦：", "股長：", "科長：", "局(處)長：")
SIGN_A24 = ("製表日期：", "承辦：", "股長：", "科長：", "局（處）長：")
TITLE_A13 = "○○縣(市)第○○期○○○○市地重劃區重劃前後土地分配清冊"
TITLE_A24 = "○○縣（市）第○○期○○○○市地重劃區土地分配計算表"
BOOK_A13 = "共　　冊　第　　冊　第　　頁"
SHEET_COUNTY = "縣有"
A13_NCOL = 24
A13_FIRST = 8                       # 資料之首列
A24_NCOL = 6
OUT_FMT = {"a13": "附表13_重劃前後土地分配清冊_退縮{}m.xlsx", "a24": "附表24_土地分配計算表_退縮{}m.xlsx"}
NF = {"area": "#,##0.00", "yuan": "#,##0", "p2": "#,##0.00", "k8": "0.00000000", "k4": "0.0000",
      "m2": "0.00", "pct": "0.00%"}

# 附表 13 之表頭（列, 欄起, 列迄, 欄迄, 字）
A13_HEAD = (
    (5, 1, 5, 10, "重劃前土地情形"), (5, 11, 7, 11, "扣除各項負擔後應分配面積(㎡)"),
    (5, 12, 5, 23, "重劃後土地情形"), (5, 24, 7, 24, "備註"),
    (6, 1, 7, 1, "鄉鎮市區"), (6, 2, 7, 2, "段"), (6, 3, 7, 3, "小段"), (6, 4, 7, 4, "地號"),
    (6, 5, 7, 5, "登記面積(㎡)"), (6, 6, 7, 6, "取配面積(㎡)"), (6, 7, 6, 8, "所有權人"),
    (6, 9, 7, 9, "持分比率"), (6, 10, 7, 10, "評定單價(元／㎡)"),
    (7, 7, 7, 7, "姓名"), (7, 8, 7, 8, "國民身分證統一編號"),
    (6, 12, 7, 12, "使用分區"), (6, 13, 7, 13, "段"), (6, 14, 7, 14, "小段"), (6, 15, 7, 15, "地號"),
    (6, 16, 7, 16, "面積(㎡)"), (6, 17, 7, 17, "評定單價(元／㎡)"), (6, 18, 6, 19, "預計繳領差額地價"),
    (7, 18, 7, 18, "繳（元）"), (7, 19, 7, 19, "領（元）"), (6, 20, 6, 21, "所有權人"),
    (7, 20, 7, 20, "姓名"), (7, 21, 7, 21, "國民身分證統一編號"), (6, 22, 7, 22, "持分比率"), (6, 23, 7, 23, "建號"),
)
A13_OWNER = (   # 列 3、4：所有權人與管理人（標籤之欄起迄, 值之欄起迄）
    (3, (1, 3, "土地所有權人（首列登記人）姓名"), (4, 6)), (3, (7, 8, "國民身分證統一編號"), (9, 10)),
    (3, (11, 12, "住址"), (13, 18)),
    (4, (1, 3, "管理人姓名"), (4, 6)), (4, (7, 8, "國民身分證統一編號"), (9, 10)),
)
A24_PRE = ("段", "小段", "地號", "登記面積(㎡)", "分配面積(㎡)", "共有人申請單獨分配持分比例",
           "持分面積(㎡)", "法定空地面積(㎡)", "當期公告現值(元/㎡)", "評定之重劃前單價(元/㎡)")
A24_CALC = ("Σa（原位次）(㎡)", "Σa'（併入）(㎡)", "Σ(a＋a')(㎡)", "原位置重劃前地價(元/㎡)",
            "預配位置重劃前原地平均單價(元/㎡)", "重劃後宗地地價(元/㎡)", "A＝重劃後宗地地價÷重劃前地價",
            "B", "C", "1−C", "S(m)", "W(m)", "F(m)", "l1", "l2", "Rw")
A24_POST = ("評定之重劃後單價(元/㎡)", "重劃後應分配權利面積 G(㎡)", "實配面積(㎡)", "分配率＝G／Σ(a＋a')",
            "段", "小段", "地號", "面積(㎡)", "土地使用分區", "預計繳納（領取）差額地價總額")
A24_BURDEN_HEAD = ("重劃費用負擔", "面積(㎡)", "單價(元/㎡)", "負擔額(元)")
A24_BURDEN = ("抵費地負擔 ①", "公共設施用地共同負擔 ②（單價 ③）", "合計（重劃費用負擔總額）",
              "預計應繳納差額地價", "預計應領取差額地價")


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


# ---------------------------------------------------------------- 計算（附表 24）
def calc(e, fin, pre_unit_int, owners, hh_lns):
    post = D(fin["重劃後單價"][e["街廓"]])
    pre = D(fin["重劃前單價"][e["重劃前區段"]])
    B, C = D(fin["B"]), D(fin["C"])
    G, area = q(D(e["G"]), 2), q(D(e["面積"]), 2)
    a0, a1 = q(D(e["a原位次"]), 2), q(D(e["併入面積"]), 2)
    tot = a0 + a1
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
    return {"post": post, "pre": pre, "pre_int": pre_unit_int, "B": B, "C": C, "A": A, "G": G, "area": area,
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
def a13_sheet(wb, name, head_owner, pre_rows, post_rows, note_first):
    ws = wb.create_sheet(name)
    _put(ws, 1, 1, TITLE_A13, c2=A13_NCOL)
    _put(ws, 2, 19, BOOK_A13, c2=A13_NCOL)
    vals = list(head_owner)
    for (r, (c1, c2, lab), (v1, v2)), v in zip(A13_OWNER, vals):
        _put(ws, r, c1, lab, c2=c2)
        _put(ws, r, v1, v, c2=v2)
    for r1, c1, r2, c2, lab in A13_HEAD:
        _put(ws, r1, c1, lab, r2=r2, c2=c2)
    n = max(len(pre_rows), len(post_rows), 1)
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
    last = A13_FIRST + n - 1
    PM._grid(ws, 3, last, A13_NCOL)
    ws.cell(last + 2, 1, NOTE_A13)
    step = A13_NCOL // len(SIGN_A13)
    for i, lab in enumerate(SIGN_A13):
        ws.cell(last + 4, 1 + i * step, lab)
    PM._page(ws, "1:7", landscape=True)
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


def write_a13(path, doc, ents, numbers, sch, cash, zoning, pre_price):
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
                                 (ln, None), (area[ln], "area"), (None, "area"), (nm, None), (uid, None),
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
    rows = []
    for e in sorted((e for e in ents if e["類別"] != KIND_LOT), key=lambda e: PM.landno_key(numbers[e["暫編"]])):
        off = e["類別"] == KIND_OFFSET
        price = (float(D(fin["重劃後單價"][e["街廓"]])), "p2") if off else (None, None)
        rows.append([(None, "area"), (zoning if off else e["類別"], None), (None, None), (None, None),
                     (numbers[e["暫編"]], None), (float(q(D(e["面積"]), 2)), "area"), price,
                     (None, "yuan"), (None, "yuan"), (COUNTY, None), (None, None), ("1/1", None), (None, None)])
    ws = a13_sheet(wb, SHEET_COUNTY, (COUNTY, None, None, None, None), [], rows, None)
    for i, e in enumerate(sorted((e for e in ents if e["類別"] != KIND_LOT),
                                 key=lambda e: PM.landno_key(numbers[e["暫編"]]))):
        _put(ws, A13_FIRST + i, 24, NOTE_OFFSET if e["類別"] == KIND_OFFSET else NOTE_PUBLIC)
    wb.save(path)
    return out


# ---------------------------------------------------------------- 附表 24
def write_a24(path, doc, ents, numbers, sch, zoning, pre_price):
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
        x = calc(e, fin, pre_price[ln], owners, lns)
        own = shares(owners, ln)
        ws = wb.create_sheet(f"地號{no}")
        _put(ws, 1, 1, TITLE_A24, c2=A24_NCOL)
        _put(ws, 2, 1, "歸戶號")
        _put(ws, 2, 2, hh_no[k])
        _put(ws, 2, 3, "所有權(代表)人姓名")
        _put(ws, 2, 4, own[0][0] if len(own) == 1 else f"{own[0][0]}等{len(own)}人", c2=A24_NCOL)
        r = 3
        _put(ws, r, 1, "重劃前", c2=A24_NCOL)
        pre = (loc[ln]["段"], loc[ln].get("小段"), ln, (area[ln], "area"), (float(x["a0"]), "area"), None, None, None,
               (float(curval(owners, ln)), "yuan"), (pre_price[ln], "yuan"))
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
        post_v = ((x["post"], "p2"), (x["G"], "area"), (x["area"], "area"), (x["G"] / x["tot"], "pct"),
                  (None, None), (None, None), (no, None), (x["area"], "area"), (zoning, None), (box, None))
        for lab, (v, nf) in zip(A24_POST, post_v):
            r += 1
            _put(ws, r, 1, lab)
            _put(ws, r, 2, v if isinstance(v, str) or v is None else float(v), nf)
        r += 1
        for c, lab in enumerate(A24_BURDEN_HEAD, start=1):
            _put(ws, r, c, lab)
        burden = ((x["b1"], x["post"], x["y1"]), (x["b2"], x["c3"], x["y2"]), (None, None, x["sum"]),
                  (None, None, d if d > 0 else 0), (None, None, -d if d < 0 else 0))
        for lab, (a_, p_, y_) in zip(A24_BURDEN, burden):
            r += 1
            _put(ws, r, 1, lab)
            _put(ws, r, 2, _num(a_), "area")
            _put(ws, r, 3, _num(p_), "p2")
            _put(ws, r, 4, _num(y_), "yuan")
        PM._grid(ws, 2, r, A24_NCOL)
        ws.cell(r + 1, 1, LEGEND_A24)
        ws.cell(r + 2, 1, NOTE_A24)
        for i, lab in enumerate(SIGN_A24):
            ws.cell(r + 4, 1 + i, lab)
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
    r13 = write_a13(p["a13"], doc, ents, numbers, sch, cash, zoning, pre_price)
    r24 = write_a24(p["a24"], doc, ents, numbers, sch, zoning, pre_price)
    n_lot = sum(1 for e in ents if e["類別"] == KIND_LOT)
    print(f"退縮 {tag} m：附表 13 戶 {len(r13)}（有分配地 {sum(1 for x in r13 if x[2])}、現金補償 {len(cash)}）＋縣有 "
          f"{len(ents) - n_lot}；附表 24 張 {len(r24)}")
    for no, hh, x in r24:
        print(f"  地號 {no}（歸戶號 {hh}）：G {x['G']}、Σ {x['tot']}（{x['a0']}＋{x['a1']}）、① {x['b1']}、② {x['b2']}、"
              f"③ {x['c3']}、負擔額 {x['y1']}＋{x['y2']}＝{x['sum']}、差額 {x['diff']}")
    for k, v in p.items():
        print(f"輸出 {v}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄己　`docs/出圖/W-P.006_附表13-24.md`（逐位元組照錄）

````markdown
# W-P.006　附表 13 重劃前後土地分配清冊、附表 24 土地分配計算表

> 單：`ops/queue` 之 `出圖線/orders/W-P.006_附表13-24.md`。本檔記產出之法、依據與量測；版面（欄寬、字級、分頁）由使用者編輯（KL 2026-10-23 17:48）。

## 產出之法

1. `python plots/alloc_state.py --out <O> --setback 0 --setback 3.5`（W-P.006 版：分配地另含 G 式之各項；檔另含「財務」「歸戶表」「現金補償」）。
2. `python plots/post_maps.py --state <O>/配地結果_退縮<t>m.json --pre-dxf <P>/重劃前圖.dxf --moedict <json> --out <O>`（地號對照表·W-P.005）。
3. `python plots/post_tables.py --state <O>/配地結果_退縮<t>m.json --moedict <json> --out <O> [--map <承辦人改過之地號對照表>]` ⇒ `附表13_重劃前後土地分配清冊_退縮<t>m.xlsx`、`附表24_土地分配計算表_退縮<t>m.xlsx`。

## 依據（KL）

- 2026-10-28 23:31 問二 甲：未受分配而發給現金補償之戶照列於附表 13；重劃前各欄照填、重劃後各欄留空；備註「未達最小分配面積標準二分之一，發給現金補償 ○○ 元」（金額由配地結果之「現金補償」帶入）。
- 同 問三 甲：附表 24 之平均公告現值以匯入之公告現值暫填；平均 ＝ Σ(計入 G 之面積 × 現值) ÷ Σ 計入 G 之面積（個位）；表下加註「暫以匯入時之公告現值計，公告期滿後應以當期公告現值更正」。
- 2026-10-28 23:37：正式地號依「暫編 → 正式地號對照表」帶入（重號或缺號即停）。
- 2026-10-26 23:14 第 1 點 甲：重劃前單價取至個位；重劃後單價以全精度計算、顯示二位。
- 2026-10-30 19:28：W-P.005 全定版；下一批附表 13、24（先做格式與可填之欄）。

## 規則之要

- 附表 13：一戶一表（表名「歸戶號 N」·歸戶號同 W-P.002），另一表「縣有」列抵費地與道路、公園（所有權人花蓮縣、持分 1/1、重劃前欄免填、備註照手冊第 3824〜3828 列）。重劃前：該戶各宗 × 各所有權人一列（地號序·登記次序），單價取個位（同附表 18）；「取配面積」留空（俟調配終態）。重劃後：該戶之各分配地（正式地號序）× 各所有權人一列（持分按原共有狀態·一戶之各宗之持分不同即停）；應分配面積 ＝ G；差額地價 ＝（面積 − G）× 重劃後單價（元·四捨五入），正者入「繳」、負者入「領」。
- 附表 24：一分配地一張（表名「地號 N」）。重劃前列原位次之地號；Σa ＝ 該宗之分攤登記面積、Σa' ＝ 併入之面積（a − 分攤登記面積）。A ＝ 重劃後宗地地價 ÷ 原位置重劃前地價（全精度·同引擎）。計算式 ＝「G＝〔Σ×(1−A×B)−F×l1×Rw−S×l2〕×(1−C)」，以表上之值重算與 G 之差 ≤ 0.02 ㎡（G 為引擎之解）。①＝G×C÷(1−C)（二位）、②＝Σ−G−①、③＝平均公告現值；負擔額 ＝ 面積 × 單價（元·四捨五入）。
- 本版之配地 ＝ 階段一之終（調配之前）：未分配之戶之重劃後各欄留空；併入之逐筆來源管線未出（交監看窗）。

## 量測與故意錯誤

- `verify/plots/check_W-P006.py`：V0（手冊範例之式自證）、V1（表之集合、表頭、首列登記人）、V2（重劃前之列）、V3（重劃後之列、縣有、正式地號恰一次、面積之和）、V4（附表 24 之重劃前與計算分配有關資料、計算式）、V5（負擔與差額）、V6（現金補償、改號帶入、缺鍵即停·子行程）。
- `verify/plots/mutate_W-P006.py`：Ⓐ〜Ⓔ（① 漏 ÷(1−C)、附表 24 漏一宗、A 以個位單價計、抵費地與公設之備註互換、現金補償之備註漏寫）皆紅。
````
