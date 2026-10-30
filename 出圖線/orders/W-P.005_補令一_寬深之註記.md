# W-P.005_補令一　公告分配地籍線之「寬」改顯示 S、街角第 1 宗之「深」納道路截角

- **題**：依 KL 2026-10-30 08:00 之答（`出圖線/KL答覆/2026-10-30_0800.md`·W-P.005 第一版之確認第 2 點），改公告分配地籍線之分配地之註記：「寬」改顯示 S（G 值計算之臨正面道路寬度）；「深」維持 面積 ÷ W；**街角第 1 宗**之深改為（面積 ＋ 道路截角面積）÷ W。其餘（宗之形與面積、地號與 S 型、對照表、歸戶圖、地價圖、顏色對照表、重劃前三圖層）⛔ 變。
- **範圍**：唯本線所建之 `plots/alloc_state.py`、`plots/post_maps.py`、`verify/plots/check_W-P005.py`、`verify/plots/mutate_W-P005.py`（全文換為附錄），新增 `verify/plots/preview_W-P005a.py`、`docs/出圖/W-P.005_補令一_寬深之註記.md`；⛔ 改任何既有之檔（本線以外者）；⛔ 改 `requirements.txt`；⛔ 新套件。
- **授權（逐字）**：
  - KL 2026-10-23 17:31「1. 是　2. 以手冊（拾參）所附的圖例為主」；17:48「圖就出DXF或DWG(圖層含重劃前地籍線、公告分配地籍線、重劃前歸化圖、分配後歸戶圖、地價圖)即可，所有的標題及排版由使用者編輯。…」（README 第一節）。
  - KL 2026-10-29 23:33「1. 問1：是。」「2. 實量深是要取哪一段?寬可否顯示G值計算的S(臨正面道路寬度)」「3. 其餘是」（`出圖線/KL答覆/2026-10-29_2333.md`）。
  - KL 2026-10-30 08:00「1. 深度維持現行，但特例是街角地，可否僅在計算街角地深度時，其街角地面積把截角面積暫時納入，再以面積(含道路截角)/寬」「2. 計算深度用的（面積 ÷ 寬）寬用W會比較準，但圖面顯示時用S，民眾比較直觀」（`出圖線/KL答覆/2026-10-30_0800.md`）。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `9fd34275770b7fc53103b9eb42ba21925f823f9a`（自 `bd7da4d` 前進·含 `W-G.9-399` 之生產碼）；`wip/plots` ＝ `verify/W-P.005-post-maps` ＝ `9deaad28ca37bd24c4c02ddc86d65da3b7a9d574`（未含 `9fd3427` ⇒ 工項 1 之合併必做；發單端試併無衝突）。
- **側支**：`verify/W-P.005a-width-depth`（自 `wip/plots` 出）。單名與側支名經 `git grep -F`（主倉 `9fd3427`＋`9deaad2`）與 `git ls-remote` 證未占用（佇列唯見本單之上鎖之記）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具）。

## §一　所據

1. **KL 之答**：見引言。監看窗之讀（`2026-10-30_0800.md`）：深 ＝ 面積 ÷ W（W ＝ 判畸零地之宗地寬度）；街角第 1 宗之深 ＝（該宗面積 ＋ 該宗所臨之道路截角面積）÷ W；道路截角面積 ＝ 正面臨路線與側面道路線之延長交點（未截角之理論角）與截角線所圍之三角形之面積，由圖資幾何算出、⛔ 寫死，唯為計算深度而暫時納入（⛔ 改面積之註記、⛔ 改配地面積）；圖面之寬顯示 S；抵費地與道路、公園仍只註地號、面積。
2. **街角第 1 宗之 W 是否為截角前之寬（監看窗令查明·K-9-5-15 五：角地之寬度與深度一律以截角前形狀量測）**——發單端實查（主線 `9fd3427` 併 `9deaad2` 之上，跑既有之管線）：
   - 引擎之宗地寬度 ＝ `S × |正面臨路線之方向 · 垂直於宗地分配線之方向|`（`verify/stepg_pipeline.py` 之 `_mark_zaling`：`_pw = S × _cos_dn`）；而 S 自正面臨路線之端點量起，正面臨路線畫至**未截角之理論角**（`FRONT_LINE` 之 p1／p2 ＝ 與 `SIDE_LINE` 之交點，本案八角皆重合至 0）。⇒ **現行之 W 於街角第 1 宗即為截角前之寬，⛔ 改。**
   - 本案各街角第 1 宗之二值（截角後之寬 ＝ 自正面臨路線上之截角點起量）：

     | 退縮 | 街角第 1 宗 | 街廓·側 | S | W（現行·截角前） | 截角後之寬 | 道路截角面積 |
     |---|---|---|---|---|---|---|
     | 3.5 m | 628-36(1) | R1 左 | 19.46 | 19.40 | 15.74 | 6.71 |
     | 3.5 m | 628(5) | R1 右 | 11.53 | 11.49 | 8.12 | 5.77 |
     | 3.5 m | 628(1) | R4 左 | 54.22 | 54.16 | 50.45 | 6.86 |
     | 3.5 m | 628-1(1) | R4 右 | 21.99 | 21.97 | 18.43 | 6.28 |
     | 3.5 m | 628-18(1) | R6 右 | 7.22 | 7.20 | 3.81 | 5.77 |
     | 3.5 m | 628-45(1) | R5 左 | 12.13 | 12.08 | 8.63 | 6.14 |
     | 3.5 m | 628-41(1) | R2 左 | 7.12 | 7.10 | 3.57 | 6.28 |
     | 3.5 m | 628-45(2) | R3 右 | 20.30 | 20.21 | 16.66 | 6.20 |
     | 0 m | 628-37(1) | R1 左 | 8.43 | 8.40 | 4.75 | 6.71 |
     | 0 m | 628-18(2) | R5 左 | 6.07 | 6.04 | 2.60 | 6.14 |
     | 0 m | 628-45(2) | R3 右 | 7.80 | 7.77 | 4.21 | 6.20 |
     | 0 m | 其餘五宗 | 同 3.5 m（628(5)、628(1)、628-1(1)、628-18(1)、628-41(1)） | | | | |

     截角皆為一直線（二頂點）、落於道路、⛔ 與任一宗重疊。
3. **配地結果**：同 W-P.005（階段一之終·段三後）。主線前進至 `9fd3427`（`W-G.9-399` 改末端塊之先後）後，發單端以 `plots/alloc_state.py`（W-P.005 版）於 `9deaad2` 與試併 `9fd3427` 之上各跑二退縮，**`配地結果_退縮0m.json`、`_3.5m.json` 逐位元組同** ⇒ 配地未變。
4. **新增之輸入**（皆取自既有之管線·唯讀）：`g_rows` 之「S(m)」「第1筆街角」「街角側別」；CAD 之 `side_lines_by_side`（側面道路線之 p1、p2）。
5. **內容之判斷**（依 KL 之答與資料）：
   - 「街角地」取 `g_rows` 之「第1筆街角」＝是者（本案與「街角地」＝是者同集）；每一側面道路線恰一宗（V8 驗之）。
   - 道路截角之形：理論角 C ＝ 正面臨路線與該側之側面道路線（皆延長）之交點；A ＝ 該宗之頂點中落於正面臨路線（容差 0.02 m）而最近 C 者；B ＝ 落於側面道路線而最近 C 者；截角 ＝ C 與該宗之邊界自 A 至 B 之較短之一段所圍（弧形之截角亦適用）。A ＝ B ⇒ 面積 0。
   - 位數：面積（二位）＋ 截角面積（二位四捨五入）⇒ ÷ W（二位）⇒ 深取二位四捨五入（同 W-P.005 之深之取位）。
   - 對土地之影響：無（唯圖面之呈現）。
6. **告知事項**（監看窗令列·⛔ 裁）：分配線與正面臨路線斜交 ⇒ 圖上之「寬（S）× 深」⛔ 等於面積；本案 S − W：3.5 m 為 0.02〜0.09 m、0 m 為 0.02〜0.07 m（一般宗之「S × 深 − 面積」0.74〜3.13 ㎡；街角第 1 宗另含截角，6.65〜10.17 ㎡）。全表見附錄庚。

## §二　規格

1. **`plots/alloc_state.py`**：全文換為附錄丁。增：分配地之「S」（`S(m)`·二位）、「街角第1宗側別」（「第1筆街角」＝是者·左／右；「第1筆街角」非是／否、側別不明、該側無側面道路線 ⇒ `SourceError`）；可分配之街廓之「側面道路線」（{左／右: [p1, p2]}）。他欄⛔ 變。
2. **`plots/post_maps.py`**：全文換為附錄戊。增 `_line_cross`、`corner_cut`（§一 5 之形·頂點不臨二線或所圍者與該宗重疊 ⇒ `SourceError`）、常數 `ON_LINE_TOL = 0.02`；`cad_lines(e, no, blocks)`：分配地 ⇒ `[地號, 面積, "寬"+S, "深"+深]`；`write_dxf` 加參數 `blocks`。他處⛔ 變。
3. **`verify/plots/check_W-P005.py`**：全文換為附錄甲（V3 改驗寬 ＝ S、深之新式；新增 V8；二退縮共 18 項）。
4. **`verify/plots/mutate_W-P005.py`**：全文換為附錄乙（新增 Ⓕ〜Ⓘ；共 9 種）。
5. **新增 `verify/plots/preview_W-P005a.py`**：附錄丙（街角第 1 宗之放大圖）。
6. **新增 `docs/出圖/W-P.005_補令一_寬深之註記.md`**：附錄己。
7. 發單端之原型（暫存·⛔ 入倉·於 `9deaad2` 試併 `9fd3427` 之上）已依附錄實作，實得：
   - `alloc_state`：退縮 0 m 宗 35（分配地 29、抵費地 6）、3.5 m 宗 34（28、6）；略皆 `['R1-抵費地-2']`（同 W-P.005）。
   - `post_maps` 印之地號之序與 W-P.005 §二 7 逐號同（3.5 m 1〜39、0 m 1〜40）。
   - `check_W-P005` 18/18；`mutate_W-P005` 成果綠，Ⓐ 紅（V2〜V7）、Ⓑ（V3、V4）、Ⓒ（V4）、Ⓓ（V5）、Ⓔ（V6）、Ⓕ（V3）、Ⓖ（V3）、Ⓗ（V3）、Ⓘ（V8）；約 2 分鐘。
   - 對照組：以 `9deaad2` 之 `plots/post_maps.py` 於新配地結果出圖，附錄甲 ⇒ V3 紅（例「628-36(1) 之註記 ['5', '638.61', '寬19.40', '深32.92'] ≠ ['5', '638.61', '寬19.46', '深33.26']」）、餘 8 項綠。
   - 註記之例（3.5 m）：地號 5（628-36(1)·R1 左街角）「寬19.46」「深33.26」＝（638.61 ＋ 6.71）÷ 19.40；地號 4（628-35(2)）「寬22.22」「深33.50」＝ 741.92 ÷ 22.15。
   - 環境同 W-P.005 §二 7（venv＋`numpy<2.3`）。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.005a-width-depth`；`git merge --no-edit origin/wip/s1-endpart`（本單出時主線 `9fd3427`·必有合併之 commit）；有衝突即停機。
2. **程式**：§二 1〜6。附錄之取用法：自本單擷取該附錄之開欄（甲〜戊為三個反引號加 `python`；己為四個反引號加 `markdown`）與其閉欄（同數之反引號）間之文字，末尾一換行；bytes 與 sha256 須合：
   - 甲 `verify/plots/check_W-P005.py`：25303 bytes·`bc02ed3836bfa2ad6d8cdaa0e8cc3623db8239dcc81d52009d2ac9ad21090404`
   - 乙 `verify/plots/mutate_W-P005.py`：7620 bytes·`d18e4f40579c8311d619eb56d5a979645dc4b70671314d33b062f41ad90590b8`
   - 丙 `verify/plots/preview_W-P005a.py`：4160 bytes·`ccc1f1792df9339489271ce3069511f283c55917b03a8d4a8d0e1b15e6138c8e`
   - 丁 `plots/alloc_state.py`：8433 bytes·`a1212c6af787947ce86e34c46159405100d28cfbb76e94d3fa3fa8c28f18dbf7`
   - 戊 `plots/post_maps.py`：20692 bytes·`0bd89669259390269d5c8cc3c88d0c2ee21337fe013bc95d17a566c18311b00d`
   - 己 `docs/出圖/W-P.005_補令一_寬深之註記.md`：2287 bytes·`9bff9e1108e263c68677a5c4fd0ed5bbac489450c59d4ef1d45cfe02fa3ef83e`
   不合即停機上呈；⛔ 改一字。`python -m py_compile` 五 `.py` 皆過。
3. **量測**（`<py>` ＝ W-P.005 §二 7 之 venv 之直譯器）：
   - `<py> plots/fetch_moedict.py <M>`；`<py> plots/prelim_maps.py --out <P> --moedict <M>/dict-revised.json`；
   - `<py> plots/alloc_state.py --out <O> --setback 0 --setback 3.5`（印如 §二 7）；
   - 二退縮各 `<py> plots/post_maps.py --state <O>/配地結果_退縮<t>m.json --pre-dxf <P>/重劃前圖.dxf --moedict <M>/dict-revised.json --out <O>`（印之地號之序須 ＝ W-P.005 §二 7）；
   - `<py> verify/plots/check_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json 0 3.5` ⇒ 18 項皆 PASS、結束碼 0；
   - 註記之抽驗：3.5 m 之地號 5 之四列 ＝ `5`、`638.61`、`寬19.46`、`深33.26`；地號 4 ＝ `4`、`741.92`、`寬22.22`、`深33.50`（§二 7）。
   - 另照舊：`check_W-P001.py`（12/12）、`check_W-P002.py`（8/8）、`check_W-P003.py`（8/8）、`check_W-P004.py`（8/8）。
4. **故意錯誤之測**：`<py> verify/plots/mutate_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json <拋棄式之工作目錄>` ⇒ 成果綠；Ⓐ〜Ⓘ 皆紅（所紅之項記之·期如 §二 7）；結束碼 0。
5. **對照組與其餘輸出⛔ 變**：於拋棄式之目錄 `<C>`，複製 `<O>` 之二配地結果，以 `9deaad2` 之 `plots/post_maps.py`（`git worktree` 或 `git show 9deaad2:plots/post_maps.py`·與 `9deaad2` 之 `plots/` 同目錄跑）出圖 ⇒ (a) 附錄甲於 `<C>` ⇒ 唯 V3 紅（二退縮）；(b) 附錄辛（倉外之暫存·⛔ 入倉）`<py> 附錄辛 <C> <O> <t>` 二退縮皆印「非寬深之圖元 … 同」「寬深之文字」二數相等、地號對照表與顏色對照表皆「同」（原型：3.5 m 576 圖元、文字 56／56；0 m 583、58／58）。
6. **差異閘**（README 第四節）：`git diff --name-status <實際併入之主線之 sha（應為 9fd3427…）> <側支之端>` 每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status 9deaad2 <側支之端> -- plots verify/plots docs/出圖` 唯 `M plots/alloc_state.py`、`M plots/post_maps.py`、`M verify/plots/check_W-P005.py`、`M verify/plots/mutate_W-P005.py`、`A verify/plots/preview_W-P005a.py`、`A docs/出圖/W-P.005_補令一_寬深之註記.md`；對照組（拋棄式複本改 `app.py` 一字）必紅。
7. **預覽 PNG**：`<py> verify/plots/preview_W-P005.py <O> <PNG> 0 3.5` 與 `<py> verify/plots/preview_W-P005a.py <O> <PNG> 0 3.5`，其四輸出（`W-P.005_重劃後三圖層_退縮<t>m.png` 覆舊、`W-P.005_補令一_街角宗之寬深_退縮<t>m.png`）入佇列之 `出圖線/成果/`。
8. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
9. **回報**：`出圖線/reports/W-P.005_補令一_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、對照組、差異閘、合併之 sha、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲〜己之 bytes 或 sha256 不合；或 V0〜V8 於成果不過而非程式之誤；或地號之序與 W-P.005 §二 7 不合、或 §二 7 之註記之例不合（主線前進致配地變者亦停·記其差）。
3. `plots/alloc_state.py` 或 `plots/post_maps.py` 報 `SourceError`（含街角第 1 宗之側別不明、截角之形不合）或配地流程之 `RuntimeError`——⛔ 自擬填法、⛔ 設 `WV_BAKE`。
4. 須改本線以外之既有之檔、或須新套件（numpy 之版本唯限於倉外之 venv）。
5. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P005.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005：重劃後三圖層與地號對照表之量測。
獨立於 plots/：⛔ import 之（V7 唯以子行程呼叫 plots/post_maps.py 之命令列）；期望取自 配地結果_退縮*.json
（plots/alloc_state.py 之輸出·即配地流程之 g_rows）、重劃前圖.dxf（W-P.001／002 定版之三圖層）、
verify/case_params_UC9898.json、KL 2026-10-28 23:31、23:37 之答。

命令列：python verify/plots/check_W-P005.py <成果目錄> <重劃前圖.dxf> <dict-revised.json> <退縮…>
  成果目錄 ＝ plots/alloc_state.py 與 plots/post_maps.py 之 --out（同一目錄）。
任一不過 ⇒ 結束碼 1。
V0 各檔皆在、可讀；V1 圖層（恰六＋系統二）、重劃前三圖層之圖元與重劃前圖逐一同；
V2 公告分配地籍線之宗（數、形、面積、各街廓密接而無重疊、略之列皆 0）；
V3 地號與註記（每宗恰一地號、無重號、＝ 對照表之正式地號；面積、寬、深之值）；
V4 S 型之預設編定（異法重導：形心·區·街廓之序·交替·公設續編於後；1〜N 連號）；
V5 分配後歸戶圖（原地主之地 ＝ 其重劃前之歸戶色與歸戶號；抵費地一色並註「抵費地」；公設不填色、只畫界線）；
V6 重劃後地價圖（街廓之價·二位；一價一色；公設不填色）；
V7 對照表之用（改號即帶入圖；重號、空白 ⇒ 停止而無輸出）與顏色對照表；
V8 街角第 1 宗（W-P.005_補令一·KL 2026-10-30 08:00）：每一側面道路線恰一宗；其 W 為截角前之寬（異法重導）；
   道路截角（異法：該宗與理論角之凸包減該宗、取含理論角之一塊）面積 > 0、落於道路、⛔ 與任一宗重疊。
V3 之寬 ＝ S（G 值計算之臨正面道路寬度）、深 ＝ 面積 ÷ W，街角第 1 宗之深 ＝（面積 ＋ 道路截角面積）÷ W
   （截角以 V8 之異法算之）。
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
POST_MAPS = os.path.join(REPO, "plots", "post_maps.py")
PRE_LAYERS = ("重劃前地籍線", "重劃前歸戶圖", "重劃前地價圖")
L_CAD, L_OWN, L_PRICE = "公告分配地籍線", "分配後歸戶圖", "重劃後地價圖"
SYS_LAYERS = {"0", "Defpoints"}
OFFSET_WORD = "抵費地"
MAP_SHEET = "地號對照表"
MAP_HEAD = ("暫編", "街廓", "類別", "配地之暫編地號", "預設地號（S 型）", "正式地號", "面積（㎡）")
NO_RE = re.compile(r"^\d+(-\d+)?$")
TOL_SHAPE = 1e-4      # 多邊形之對稱差（㎡）
TOL_TILE = 0.05       # 一街廓之宗之和與街廓面積（㎡）
FMT = {"dxf": "公告圖_退縮{}m.dxf", "map": "地號對照表_退縮{}m.xlsx",
       "color": "顏色對照表_重劃後_退縮{}m.xlsx", "state": "配地結果_退縮{}m.json"}


def rhu(x, nd=2):
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


def s2(x):
    return f"{rhu(x):.2f}"


def nkey(s):
    a = str(s).split("-")
    return (int(a[0]), int(a[1]) if len(a) > 1 else 0)


class Ctx:
    pass


def load(out, pre_dxf, tag):
    import ezdxf
    import openpyxl
    from shapely.geometry import Polygon
    c = Ctx()
    c.tag = tag
    c.p = {k: os.path.join(out, v.format(tag)) for k, v in FMT.items()}
    c.state = json.load(open(c.p["state"], encoding="utf-8"))
    c.doc = ezdxf.readfile(c.p["dxf"])
    c.pre = ezdxf.readfile(pre_dxf)
    ws = openpyxl.load_workbook(c.p["map"], data_only=True)[MAP_SHEET]
    rows = list(ws.iter_rows(values_only=True))
    c.map_head = tuple(rows[0][:len(MAP_HEAD)])
    c.map = [r for r in rows[1:] if r and r[0] is not None and r[1] is not None]
    c.color = openpyxl.load_workbook(c.p["color"], data_only=True)
    c.msp = c.doc.modelspace()

    def polys(msp, layer):
        return [(Polygon([(p[0], p[1]) for p in e.get_points("xy")]), e)
                for e in msp.query(f'LWPOLYLINE[layer=="{layer}"]')]

    def texts(msp, layer):
        from shapely.geometry import Point
        return [(Point(e.dxf.align_point[0], e.dxf.align_point[1]), e.dxf.text)
                for e in msp.query(f'TEXT[layer=="{layer}"]')]

    def hatches(msp, layer):
        out_ = []
        for e in msp.query(f'HATCH[layer=="{layer}"]'):
            if len(e.paths) != 1:
                raise AssertionError("HATCH 之邊界非一")
            out_.append((Polygon([(v[0], v[1]) for v in e.paths[0].vertices]), tuple(e.rgb)))
        return out_
    c.polys, c.texts, c.hatches = polys, texts, hatches
    blocks = c.state["街廓"]
    c.alloc = {k for k, v in blocks.items() if "宗地分配線方向" in v}
    c.public = sorted(k for k in blocks if k not in c.alloc)
    c.lots = c.state["宗"]
    c.post_price = {b: d["單價_元每m2"] for b, d in
                    json.load(open(CASE, encoding="utf-8"))["財務接線_v3"]["後街廓_面積單價"].items()}
    return c


def _sig(e):
    t = e.dxftype()
    if t == "LWPOLYLINE":
        return (t, e.dxf.layer, tuple((round(p[0], 6), round(p[1], 6)) for p in e.get_points("xy")))
    if t == "TEXT":
        return (t, e.dxf.layer, e.dxf.text, round(e.dxf.align_point[0], 6), round(e.dxf.align_point[1], 6))
    if t == "HATCH":
        return (t, e.dxf.layer, tuple(e.rgb),
                tuple((round(v[0], 6), round(v[1], 6)) for v in e.paths[0].vertices))
    return (t, e.dxf.layer)


def _match(c):
    """配地結果之每宗（與公設之區塊）⇒ 公告分配地籍線之多邊形（對稱差 ≤ TOL_SHAPE）。"""
    from shapely.geometry import Polygon
    ps = c.polys(c.msp, L_CAD)
    want = [(x["配地暫編"], x, Polygon(x["多邊形"])) for x in c.lots]
    want += [(b, None, Polygon(c.state["街廓"][b]["多邊形"])) for b in c.public]
    got = {}
    used = set()
    for key, x, wp in want:
        hit = [i for i, (p, _) in enumerate(ps) if p.symmetric_difference(wp).area <= TOL_SHAPE]
        if len(hit) != 1 or hit[0] in used:
            return None, f"{key} 於 {L_CAD} 之多邊形 {len(hit)} 個"
        used.add(hit[0])
        got[key] = (x, ps[hit[0]][0])
    if len(used) != len(ps):
        return None, f"{L_CAD} 有多出之多邊形 {len(ps) - len(used)} 個"
    return got, None


def v0(c):
    return []


def v1(c):
    bad = []
    names = {ly.dxf.name for ly in c.doc.layers}
    want = SYS_LAYERS | set(PRE_LAYERS) | {L_CAD, L_OWN, L_PRICE}
    if names != want:
        bad.append(f"圖層 {sorted(names ^ want)}")
    for ly in PRE_LAYERS:
        a = sorted(_sig(e) for e in c.msp if e.dxf.layer == ly)
        b = sorted(_sig(e) for e in c.pre.modelspace() if e.dxf.layer == ly)
        if a != b or not a:
            bad.append(f"{ly} 之圖元與重劃前圖不同（{len(a)}／{len(b)}）")
    for e in c.msp:
        if e.dxf.layer in SYS_LAYERS:
            bad.append(f"系統圖層 {e.dxf.layer} 上有圖元")
            break
    return bad


def v2(c):
    from shapely.ops import unary_union
    from shapely.geometry import Polygon
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    n = len(c.polys(c.msp, L_CAD))
    if n != len(c.lots) + len(c.public):
        bad.append(f"宗數 {n} ≠ {len(c.lots)}＋{len(c.public)}")
    for x in c.lots:
        if s2(Polygon(x["多邊形"]).area) != s2(x["面積"]):
            bad.append(f"{x['配地暫編']} 之面積 {x['面積']} ≠ 圖 {Polygon(x['多邊形']).area:.4f}")
    for b in sorted(c.alloc):
        ps = [got[x["配地暫編"]][1] for x in c.lots if x["街廓"] == b]
        bp = Polygon(c.state["街廓"][b]["多邊形"])
        s = sum(p.area for p in ps)
        u = unary_union(ps)
        if abs(s - bp.area) > TOL_TILE or u.symmetric_difference(bp).area > TOL_TILE:
            bad.append(f"{b}：宗之和 {s:.3f}、聯集之差 {u.symmetric_difference(bp).area:.4f}、街廓 {bp.area:.3f}")
    for d in c.state["略"]:
        if s2(d["幾何面積"]) != "0.00":
            bad.append(f"略之列 {d['配地暫編']} 之面積非 0")
    return bad


def _map_rows(c):
    if c.map_head != MAP_HEAD:
        raise AssertionError(f"對照表之表頭 {c.map_head}")
    return {r[3] if r[3] is not None else r[0]: r for r in c.map}


def v3(c):
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    try:
        mr = _map_rows(c)
    except AssertionError as ex:
        return [str(ex)]
    if len(mr) != len(got):
        bad.append(f"對照表 {len(mr)} 列 ≠ {len(got)} 宗")
    tx = c.texts(c.msp, L_CAD)
    seen = {}
    for key, (x, poly) in got.items():
        inside = [s for pt, s in tx if poly.contains(pt)]
        nos = [s for s in inside if NO_RE.match(s)]
        if len(nos) != 1:
            bad.append(f"{key} 之地號之註記 {nos}")
            continue
        no = nos[0]
        if no in seen:
            bad.append(f"地號 {no} 重號：{seen[no]}、{key}")
        seen[no] = key
        r = mr.get(key)
        if r is None or str(r[5]) != no:
            bad.append(f"{key} 之地號 {no} ≠ 對照表 {None if r is None else r[5]}")
        area = x["面積"] if x else rhu(poly.area)
        want = [no, s2(area)]
        if x and x["類別"] == "分配地":
            w = rhu(x["宗地寬度"])
            a = Decimal(repr(float(x["面積"])))
            if "街角第1宗側別" in x:
                a += rhu(_cut_alt(c, x).area)
            d = (a / w).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            want += [f"寬{rhu(x['S']):.2f}", f"深{d:.2f}"]
        if sorted(inside) != sorted(want):
            bad.append(f"{key} 之註記 {inside} ≠ {want}")
    if len(tx) != sum(4 if (x and x["類別"] == "分配地") else 2 for x, _ in got.values()):
        bad.append(f"{L_CAD} 之文字數不合（{len(tx)}）")
    return bad


def _theory_corner(c, x):
    """異法：以向量之叉積解正面臨路線與側面道路線（皆延長）之交點。"""
    b = c.state["街廓"][x["街廓"]]
    (ax, ay), (bx, by) = b["正面臨路線"]
    (px, py), (qx, qy) = b["側面道路線"][x["街角第1宗側別"]]
    rx, ry, sx, sy = bx - ax, by - ay, qx - px, qy - py
    den = rx * sy - ry * sx
    t = ((px - ax) * sy - (py - ay) * sx) / den
    return ax + t * rx, ay + t * ry


def _cut_alt(c, x):
    """異法之道路截角：（該宗 ∪ 理論角）之凸包 − 該宗，取與理論角相接之一塊。"""
    from shapely.geometry import MultiPoint, Point, Polygon
    lot = Polygon(x["多邊形"])
    cp = Point(_theory_corner(c, x))
    rest = MultiPoint(list(lot.exterior.coords) + [cp.coords[0]]).convex_hull.difference(lot)
    parts = [g for g in getattr(rest, "geoms", [rest]) if g.area > 1e-9 and g.distance(cp) < 1e-6]
    if len(parts) != 1:
        raise AssertionError(f"{x['配地暫編']} 之道路截角 {len(parts)} 塊")
    return parts[0]


def v8(c):
    import math
    from shapely.geometry import LineString, Point, Polygon
    from shapely.ops import unary_union
    bad = []
    blocks = c.state["街廓"]
    lots = [x for x in c.lots if x["類別"] == "分配地"]
    roads = unary_union([Polygon(blocks[b]["多邊形"]) for b in c.public if blocks[b]["分類"] != "公園"]
                        or [Polygon()])
    every = unary_union([Polygon(x["多邊形"]) for x in c.lots])
    n_c = 0
    for b in sorted(c.alloc):
        for side in sorted(blocks[b].get("側面道路線", {})):
            hit = [x for x in lots if x["街廓"] == b and x.get("街角第1宗側別") == side]
            sl = LineString(blocks[b]["側面道路線"][side])
            touch = [x for x in lots if x["街廓"] == b and Polygon(x["多邊形"]).intersection(sl.buffer(0.02)).area > 0.01]
            if len(hit) != 1:
                bad.append(f"{b} {side}側 之街角第 1 宗 {len(hit)} 宗")
                continue
            x = hit[0]
            if [y["配地暫編"] for y in touch] != [x["配地暫編"]]:
                bad.append(f"{b} {side}側 臨側面道路線之宗 {[y['配地暫編'] for y in touch]} ≠ {x['配地暫編']}")
            n_c += 1
            (ax, ay), (bx, by) = blocks[b]["正面臨路線"]
            L = math.hypot(bx - ax, by - ay)
            ux, uy = (bx - ax) / L, (by - ay) / L
            dx, dy = blocks[b]["宗地分配線方向"]
            dl = math.hypot(dx, dy)
            cosv = abs(ux * dx / dl + uy * dy / dl)
            sinv = math.sqrt(max(0.0, 1 - cosv * cosv))   # 正面臨路線與「垂直於宗地分配線」之夾角之餘弦
            cx, cy = _theory_corner(c, x)
            fl = LineString(blocks[b]["正面臨路線"])
            ts = [abs((px - cx) * ux + (py - cy) * uy) for px, py in Polygon(x["多邊形"]).exterior.coords
                  if fl.distance(Point(px, py)) <= 0.02]
            w_pre, w_post = max(ts) * sinv, (max(ts) - min(ts)) * sinv
            if abs(rhu(w_pre) - rhu(x["宗地寬度"])) > Decimal("0.01"):
                bad.append(f"{x['配地暫編']} 之 W {x['宗地寬度']} ≠ 截角前之寬 {w_pre:.3f}（截角後 {w_post:.3f}）")
            if not w_post < w_pre - 1:
                bad.append(f"{x['配地暫編']} 之截角前後之寬不分（{w_pre:.3f}／{w_post:.3f}）")
            try:
                cut = _cut_alt(c, x)
            except AssertionError as ex:
                bad.append(str(ex))
                continue
            if cut.area <= 0.01:
                bad.append(f"{x['配地暫編']} 之道路截角之面積 {cut.area:.4f}")
            if cut.intersection(roads).area < 0.99 * cut.area:
                bad.append(f"{x['配地暫編']} 之道路截角不在道路（{cut.intersection(roads).area:.4f}／{cut.area:.4f}）")
            if cut.intersection(every).area > 1e-4:
                bad.append(f"{x['配地暫編']} 之道路截角與宗重疊")
    if n_c == 0:
        bad.append("無街角第 1 宗")
    if any("街角第1宗側別" in x and x.get("街角第1宗側別") not in blocks[x["街廓"]].get("側面道路線", {})
           for x in lots):
        bad.append("街角第 1 宗之側別無側面道路線")
    return bad


def _expected_order(c):
    """異法：形心；街廓之序 ＝ 形心之 y 降、x 降；第奇個街廓自東而西（形心 x 降）、第偶個自西而東；公設續後。"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    blocks = c.state["街廓"]
    P = {k: Polygon(v["多邊形"]) for k, v in blocks.items()}
    u = unary_union([p.buffer(0.01) for p in P.values()])
    regs = list(getattr(u, "geoms", [u]))
    regs.sort(key=lambda g: (-g.centroid.y, -g.centroid.x))
    seq, pubs = [], []
    for g in regs:
        mem = [k for k in P if g.contains(P[k].centroid) or g.contains(P[k].representative_point())]
        al = sorted([k for k in mem if k in c.alloc], key=lambda k: (-P[k].centroid.y, -P[k].centroid.x))
        for i, k in enumerate(al):
            lots = [x for x in c.lots if x["街廓"] == k]
            lots.sort(key=lambda x: Polygon(x["多邊形"]).centroid.x, reverse=(i % 2 == 0))
            seq += [x["配地暫編"] for x in lots]
        pubs += sorted([k for k in mem if k not in c.alloc], key=lambda k: (-P[k].centroid.y, -P[k].centroid.x))
    return seq + pubs


def v4(c):
    bad = []
    try:
        mr = _map_rows(c)
    except AssertionError as ex:
        return [str(ex)]
    exp = _expected_order(c)
    dflt = {k: r[4] for k, r in mr.items()}
    want = {k: str(i) for i, k in enumerate(exp, start=1)}
    if {k: str(v) for k, v in dflt.items()} != want:
        diff = [(k, dflt.get(k), want.get(k)) for k in exp if str(dflt.get(k)) != want[k]][:6]
        bad.append(f"預設地號 ≠ S 型之序：{diff}")
    got, err = _match(c)
    if err:
        return bad + [err]
    tx = c.texts(c.msp, L_CAD)
    on_map = {}
    for key, (_x, poly) in got.items():
        nos = [s for pt, s in tx if poly.contains(pt) and NO_RE.match(s)]
        on_map[key] = nos[0] if len(nos) == 1 else None
    if c.with_default and on_map != want:
        bad.append("圖上之地號 ≠ S 型之預設（未給對照表者）")
    return bad


def v5(c):
    from shapely.geometry import Polygon
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    pre = c.pre.modelspace()
    pre_poly = {}
    for p, _e in c.polys(pre, PRE_LAYERS[0]):
        labs = [s for pt, s in c.texts(pre, PRE_LAYERS[0]) if p.contains(pt)]
        if len(labs) == 1:
            pre_poly[labs[0]] = p
    pre_h = c.hatches(pre, PRE_LAYERS[1])
    pre_t = c.texts(pre, PRE_LAYERS[1])
    hh = c.hatches(c.msp, L_OWN)
    ht = c.texts(c.msp, L_OWN)
    outl = c.polys(c.msp, L_OWN)
    owner_colors = set()
    offs = set()
    n_h = 0
    for key, (x, poly) in got.items():
        mine = [col for hp, col in hh if hp.symmetric_difference(poly).area <= TOL_SHAPE]
        labs = [s for pt, s in ht if poly.contains(pt)]
        if x is None:
            if mine or labs:
                bad.append(f"公設 {key} 有填色或註記")
            if len([1 for p, _ in outl if p.symmetric_difference(poly).area <= TOL_SHAPE]) != 1:
                bad.append(f"公設 {key} 於 {L_OWN} 無界線")
            continue
        n_h += 1
        if len(mine) != 1 or len(labs) != 1:
            bad.append(f"{key} 之填色 {len(mine)}、註記 {labs}")
            continue
        if x["類別"] == "抵費地":
            offs.add(mine[0])
            if labs[0] != OFFSET_WORD:
                bad.append(f"{key} 之註記 {labs[0]}")
            continue
        pp = pre_poly.get(x["原地號"])
        if pp is None:
            bad.append(f"{key} 之原地號 {x['原地號']} 不在重劃前圖")
            continue
        pc = [col for hp, col in pre_h if hp.symmetric_difference(pp).area <= TOL_SHAPE]
        pl = [s for pt, s in pre_t if pp.contains(pt)]
        if pc != [mine[0]] or pl != [labs[0]]:
            bad.append(f"{key}（原 {x['原地號']}）：色 {mine[0]}／歸戶號 {labs[0]} ≠ 重劃前 {pc}／{pl}")
        owner_colors.add(mine[0])
    if len(offs) > 1:
        bad.append(f"抵費地之色不一：{offs}")
    if offs & owner_colors or offs & {col for _, col in pre_h}:
        bad.append("抵費地之色與某戶之色同")
    if len(hh) != n_h or len(ht) != n_h:
        bad.append(f"{L_OWN} 之填色 {len(hh)}、註記 {len(ht)} ≠ {n_h}")
    # 相鄰之不同戶異色
    lots = [(x, poly) for x, poly in got.values() if x and x["類別"] == "分配地"]
    for i, (a, pa) in enumerate(lots):
        for b, pb in lots[i + 1:]:
            if a["歸戶"] != b["歸戶"] and pa.buffer(0.05).intersects(pb):
                ca = [col for hp, col in hh if hp.symmetric_difference(pa).area <= TOL_SHAPE]
                cb = [col for hp, col in hh if hp.symmetric_difference(pb).area <= TOL_SHAPE]
                if ca == cb:
                    bad.append(f"相鄰之異戶 {a['配地暫編']}、{b['配地暫編']} 同色")
    return bad


def v6(c):
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    hh = c.hatches(c.msp, L_PRICE)
    ht = c.texts(c.msp, L_PRICE)
    col_of = {}
    n = 0
    for key, (x, poly) in got.items():
        mine = [col for hp, col in hh if hp.symmetric_difference(poly).area <= TOL_SHAPE]
        labs = [s for pt, s in ht if poly.contains(pt)]
        if x is None:
            if mine or labs:
                bad.append(f"公設 {key} 有填色或註記")
            continue
        n += 1
        want = s2(c.post_price[x["街廓"]])
        if len(mine) != 1 or labs != [want]:
            bad.append(f"{key} 之填色 {len(mine)}、註記 {labs} ≠ {want}")
            continue
        col_of.setdefault(want, set()).add(mine[0])
    if any(len(v) != 1 for v in col_of.values()):
        bad.append(f"同價異色：{col_of}")
    cols = [next(iter(v)) for v in col_of.values()]
    if len(set(cols)) != len(cols):
        bad.append("異價同色")
    if len(hh) != n or len(ht) != n:
        bad.append(f"{L_PRICE} 之填色 {len(hh)}、註記 {len(ht)} ≠ {n}")
    return bad


def v7(c):
    bad = []
    # 顏色對照表 ＝ 圖
    ws = c.color[L_OWN]
    rows = list(ws.iter_rows(values_only=True))[1:]
    got, err = _match(c)
    if err:
        return [err]
    hh = c.hatches(c.msp, L_OWN)
    ht = c.texts(c.msp, L_OWN)
    tx = c.texts(c.msp, L_CAD)
    tab = {}
    for _ly, no, col, nos in rows:
        for s in str(nos).split("、"):
            tab[s] = (str(no), col)
    for key, (x, poly) in got.items():
        if x is None:
            continue
        no = [s for pt, s in tx if poly.contains(pt) and NO_RE.match(s)][0]
        col = [cc for hp, cc in hh if hp.symmetric_difference(poly).area <= TOL_SHAPE][0]
        lab = [s for pt, s in ht if poly.contains(pt)][0]
        if tab.get(no) != (lab, "{},{},{}".format(*col)):
            bad.append(f"顏色對照表之 {no} {tab.get(no)} ≠ 圖 {lab}／{col}")
    if c.run_map:
        bad += _map_runs(c)
    return bad


def _map_runs(c):
    """以子行程跑 plots/post_maps.py：①二宗之正式地號互換 ⇒ 圖隨之；②重號、③空白 ⇒ 結束碼非 0 且無輸出。"""
    import openpyxl
    bad = []
    tmp = tempfile.mkdtemp(prefix="wp005_map_")
    try:
        base = [sys.executable, POST_MAPS, "--state", c.p["state"], "--pre-dxf", c.pre_path,
                "--moedict", c.moedict]
        lots = [r for r in c.map if r[2] == "分配地"]
        a, b = lots[0], lots[-1]

        def edited(name, fn):
            wb = openpyxl.load_workbook(c.p["map"])
            ws = wb[MAP_SHEET]
            for row in ws.iter_rows(min_row=2):
                fn(row)
            p = os.path.join(tmp, name)
            wb.save(p)
            return p

        def swap(row):
            if row[0].value == a[0]:
                row[5].value = b[5]
            elif row[0].value == b[0]:
                row[5].value = a[5]

        def dup(row):
            if row[0].value == a[0]:
                row[5].value = b[5]

        def blank(row):
            if row[0].value == a[0]:
                row[5].value = None
        for name, fn, ok_expected in (("swap.xlsx", swap, True), ("dup.xlsx", dup, False),
                                      ("blank.xlsx", blank, False)):
            o = os.path.join(tmp, name + ".out")
            r = subprocess.run(base + ["--out", o, "--map", edited(name, fn)], capture_output=True, text=True)
            made = os.path.exists(os.path.join(o, FMT["dxf"].format(c.tag)))
            if ok_expected:
                if r.returncode != 0 or not made:
                    bad.append(f"改號之對照表未能產出（{r.returncode}）：{r.stderr[-300:]}")
                    continue
                import ezdxf
                from shapely.geometry import Polygon
                d2 = ezdxf.readfile(os.path.join(o, FMT["dxf"].format(c.tag)))
                m2 = d2.modelspace()
                tx = c.texts(m2, L_CAD)
                for row, want in ((a, b[5]), (b, a[5])):
                    x = next(x for x in c.lots if x["配地暫編"] == row[3])
                    poly = Polygon(x["多邊形"])
                    nos = [s for pt, s in tx if poly.contains(pt) and NO_RE.match(s)]
                    if nos != [str(want)]:
                        bad.append(f"改號後 {row[0]} 之地號 {nos} ≠ {want}")
            elif r.returncode == 0 or made:
                bad.append(f"{name} 未停止（結束碼 {r.returncode}、輸出 {made}）")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return bad


CHECKS = [("V0", v0), ("V1", v1), ("V2", v2), ("V3", v3), ("V4", v4), ("V5", v5), ("V6", v6), ("V7", v7), ("V8", v8)]


def run(out, pre_dxf, moedict, tags, quiet=False, run_map=True, with_default=True):
    fails = []
    for tag in tags:
        try:
            c = load(out, pre_dxf, tag)
        except Exception as ex:   # noqa: BLE001  （V0：缺檔、不可讀）
            if not quiet:
                print(f"FAIL V0 退縮{tag}m：{ex}")
            fails.append(f"V0@{tag}")
            continue
        c.pre_path, c.moedict = pre_dxf, moedict
        c.run_map, c.with_default = run_map, with_default
        for name, fn in CHECKS:
            try:
                bad = fn(c)
            except Exception as ex:   # noqa: BLE001
                bad = [f"{type(ex).__name__}: {ex}"]
            if not quiet:
                print(f"{'PASS' if not bad else 'FAIL'} {name} 退縮{tag}m" + ("" if not bad else "：" + "；".join(bad[:5])))
            if bad:
                fails.append(f"{name}@{tag}")
    return fails


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) < 4:
        print(__doc__)
        return 2
    out, pre_dxf, moedict, *tags = argv
    fails = run(out, pre_dxf, moedict, tags)
    print(f"{'全過' if not fails else '不過 ' + str(fails)}（{len(CHECKS) * len(tags) - len(fails)}/{len(CHECKS) * len(tags)}）")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄乙　`verify/plots/mutate_W-P005.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓘ 共 9 種變異體須各紅（量測 ＝ check_W-P005.py 之 V0〜V8）。
  Ⓕ〜Ⓘ：W-P.005_補令一（KL 2026-10-30 08:00·寬顯示 S、深 ＝ 面積 ÷ W、街角第 1 宗之深含道路截角）。

命令列：python verify/plots/mutate_W-P005.py <成果目錄> <重劃前圖.dxf> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py 與 plots/post_maps.py 之 --out（⛔ 改之；變異體皆寫於工作目錄）。
  唯驗退縮 3.5 m（量測之 V7 之子行程略之·以省時；V7 之判別力另以 Ⓔ 之外之成果之量測證之）。
  Ⓒ〜Ⓗ 掛換 plots/post_maps.py 之函式後重出（於本行程之記憶體中·⛔ 改檔）；Ⓐ、Ⓑ 改成果之複本；
  Ⓘ 改配地結果之複本（街角第 1 宗之 W 改為截角後之寬）後重出。
結束碼：成果綠且 9 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P005", os.path.join(HERE, "check_W-P005.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"


def _copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def _plots():
    sys.path.insert(0, os.path.join(REPO, "plots"))
    import post_maps
    return post_maps


def _dxf(d):
    import ezdxf
    p = os.path.join(d, chk.FMT["dxf"].format(TAG))
    return p, ezdxf.readfile(p)


def mA_drop_lot(d, env):
    """公告分配地籍線漏一宗（刪其界線）。"""
    p, doc = _dxf(d)
    msp = doc.modelspace()
    e = next(iter(msp.query(f'LWPOLYLINE[layer=="{chk.L_CAD}"]')))
    msp.delete_entity(e)
    doc.saveas(p)


def mB_dup_number(d, env):
    """二宗同號（改一宗之地號之註記為他宗之號）。"""
    p, doc = _dxf(d)
    msp = doc.modelspace()
    nos = [t for t in msp.query(f'TEXT[layer=="{chk.L_CAD}"]') if chk.NO_RE.match(t.dxf.text)]
    nos[0].dxf.text = nos[1].dxf.text
    doc.saveas(p)


def _regen(d, env, attr, val, edit_state=None):
    import json
    pm = _plots()
    orig = getattr(pm, attr) if attr else None
    if attr:
        setattr(pm, attr, val)
    try:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)
        st = os.path.join(env["out"], chk.FMT["state"].format(TAG))
        shutil.copy(st, d)
        if edit_state:
            st = os.path.join(d, chk.FMT["state"].format(TAG))
            doc = json.load(open(st, encoding="utf-8"))
            edit_state(doc)
            with open(st, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=1)
        pm.main(["--state", st, "--pre-dxf", env["pre"], "--moedict", env["moe"], "--out", d])
    finally:
        if attr:
            setattr(pm, attr, orig)


def mC_no_alternation(d, env):
    """S 型不交替（每一街廓皆自東而西）。"""
    pm = _plots()
    orig = pm.s_order

    def s_order(doc, ents):
        from shapely.geometry import Polygon
        o = orig(doc, ents)
        pos = {t: i for i, t in enumerate(o)}
        by = {}
        for e in ents:
            by.setdefault(e["街廓"], []).append(e)
        blocks = [b for b in dict.fromkeys(e["街廓"] for e in sorted(ents, key=lambda e: pos[e["暫編"]]))
                  if "宗地分配線方向" in doc["街廓"][b]]
        out = []
        for b in blocks:
            out += [e["暫編"] for e in sorted(by[b], key=lambda e: -Polygon(e["多邊形"]).centroid.x)]
        return out + [t for t in o if t not in set(out)]
    _regen(d, env, "s_order", s_order)


def mD_owner_shift(d, env):
    """原地主之地之色錯一戶（歸戶之色依序錯位）。"""
    pm = _plots()
    orig = pm.owner_scheme

    def owner_scheme(moedict, ents):
        key_of, hh_color, hh_no = orig(moedict, ents)
        ks = list(hh_color)
        cols = [hh_color[k] for k in ks]
        return key_of, dict(zip(ks, cols[1:] + cols[:1])), hh_no
    _regen(d, env, "owner_scheme", owner_scheme)


def mE_pre_price(d, env):
    """重劃後地價圖改用重劃前之區段地價（b 區段 37323）。"""
    pm = _plots()

    def post_prices():
        return {f"R{i}": 37323.0 for i in range(1, 7)}
    _regen(d, env, "post_prices", post_prices)


def _cad_lines_with(d, env, change):
    pm = _plots()
    orig = pm.cad_lines

    def cad_lines(e, no, blocks):
        return orig(change(dict(e)), no, blocks)
    _regen(d, env, "cad_lines", cad_lines)


def mF_width_W(d, env):
    """圖面之寬仍註 W（宗地寬度）而非 S。"""
    def ch(e):
        if "S" in e:
            e["S"] = e["宗地寬度"]
        return e
    _cad_lines_with(d, env, ch)


def mG_no_cut(d, env):
    """街角第 1 宗之深未納道路截角面積。"""
    def ch(e):
        e.pop("街角第1宗側別", None)
        return e
    _cad_lines_with(d, env, ch)


def mH_depth_by_S(d, env):
    """深以 S 除（面積 ÷ S）而非 W。"""
    def ch(e):
        if "S" in e:
            e["宗地寬度"] = e["S"]
        return e
    _cad_lines_with(d, env, ch)


def mI_post_cut_width(d, env):
    """街角第 1 宗之 W 改為截角後之寬（配地結果之複本·宗地寬度 − 理論角至正面臨路線上最近之頂點之距）。"""
    import math
    from shapely.geometry import LineString, Point, Polygon

    def edit(doc):
        for x in doc["宗"]:
            if "街角第1宗側別" not in x:
                continue
            b = doc["街廓"][x["街廓"]]
            fl = LineString(b["正面臨路線"])
            c = Point(chk._theory_corner(chk_ctx(doc), x))
            near = min(math.dist(p, c.coords[0]) for p in Polygon(x["多邊形"]).exterior.coords
                       if fl.distance(Point(p)) <= 0.02)
            x["宗地寬度"] = round(x["宗地寬度"] - near, 2)
    _regen(d, env, None, None, edit_state=edit)


def chk_ctx(doc):
    c = chk.Ctx()
    c.state = doc
    return c


MUTANTS = [
    ("Ⓐ 公告分配地籍線漏一宗", mA_drop_lot, True),
    ("Ⓑ 二宗同號", mB_dup_number, True),
    ("Ⓒ S 型不交替", mC_no_alternation, False),
    ("Ⓓ 歸戶之色錯位", mD_owner_shift, False),
    ("Ⓔ 重劃後地價圖用重劃前地價", mE_pre_price, False),
    ("Ⓕ 寬仍註 W 而非 S", mF_width_W, False),
    ("Ⓖ 街角第 1 宗之深未納道路截角", mG_no_cut, False),
    ("Ⓗ 深以 S 除而非 W", mH_depth_by_S, False),
    ("Ⓘ 街角第 1 宗之 W 用截角後之寬", mI_post_cut_width, False),
]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 4:
        print(__doc__)
        return 2
    out, pre, moe, work = argv
    env = {"out": out, "pre": pre, "moe": moe}
    base = chk.run(out, pre, moe, [TAG], quiet=True, run_map=False)
    print(f"成果：{'綠' if not base else '紅 ' + str(base)}")
    ok = not base
    for i, (name, fn, from_copy) in enumerate(MUTANTS):
        d = os.path.join(work, f"m{i}")
        if from_copy:
            _copy(out, d)
        fn(d, env)
        fails = chk.run(d, pre, moe, [TAG], quiet=True, run_map=False)
        print(f"{name}：{'紅 ' + str(fails) if fails else '綠（未捕）'}")
        ok = ok and bool(fails)
    print("合" if ok else "不合")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄丙　`verify/plots/preview_W-P005a.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005_補令一 之預覽 PNG：街角第 1 宗之放大圖（公告分配地籍線之註記自輸出之 DXF 讀回；
道路截角〔斜線〕以 check_W-P005.py 之異法自配地結果重導，唯供 KL 一眼辨「深」所納之面積）。

命令列：python verify/plots/preview_W-P005a.py <成果目錄> <PNG 之輸出目錄> <退縮…>
輸出：每一退縮一檔 W-P.005_補令一_街角宗之寬深_退縮<t>m.png。
預覽之標題、斜線與說明唯供 KL 辨圖，⛔ 屬 DXF 之內容（DXF 無標題·KL 17:48）。
"""
import importlib.util
import json
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

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("check_W_P005", os.path.join(HERE, "check_W-P005.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
L_CAD = chk.L_CAD


def corner_png(src, tag, out_png):
    import ezdxf
    from shapely.geometry import Point, Polygon
    state = json.load(open(os.path.join(src, chk.FMT["state"].format(tag)), encoding="utf-8"))
    msp = ezdxf.readfile(os.path.join(src, chk.FMT["dxf"].format(tag))).modelspace()
    outlines = [[(p[0], p[1]) for p in e.get_points("xy")] for e in msp.query(f'LWPOLYLINE[layer=="{L_CAD}"]')]
    texts = [(e.dxf.align_point[0], e.dxf.align_point[1], e.dxf.text) for e in msp.query(f'TEXT[layer=="{L_CAD}"]')]
    c = chk.Ctx()
    c.state = state
    corners = [x for x in state["宗"] if "街角第1宗側別" in x]
    if not corners:
        raise SystemExit("無街角第 1 宗")
    n = len(corners)
    cols = 4
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(6 * cols, 6.6 * rows))
    axes = [a for r in (axes if rows > 1 else [axes]) for a in r]
    for ax, x in zip(axes, corners):
        lot = Polygon(x["多邊形"])
        cut = chk._cut_alt(c, x)
        cx, cy = chk._theory_corner(c, x)
        minx, miny, maxx, maxy = lot.union(cut).bounds
        pad = 4.0
        for pl in outlines:
            xs = [p[0] for p in pl] + [pl[0][0]]
            ys = [p[1] for p in pl] + [pl[0][1]]
            ax.plot(xs, ys, color="black", linewidth=0.8)
        xs, ys = cut.exterior.xy
        ax.fill(xs, ys, facecolor="none", edgecolor="tab:red", hatch="////", linewidth=1.0)
        ax.plot([cx], [cy], marker="o", color="tab:red", markersize=4)
        for tx, ty, s in texts:
            if lot.contains(Point(tx, ty)):
                ax.text(tx, ty, s, ha="center", va="center", fontsize=11)
        a = float(x["面積"])
        w = float(x["宗地寬度"])
        ax.set_title(f"{x['街廓']}・{'左' if x['街角第1宗側別'] == '左' else '右'}側街角第 1 宗（{x['配地暫編']}）\n"
                     f"S {x['S']:.2f}／W {w:.2f}／截角 {cut.area:.2f} ㎡\n"
                     f"深 ＝（{a:.2f} ＋ {cut.area:.2f}）÷ {w:.2f}", fontsize=11)
        ax.set_xlim(minx - pad, maxx + pad)
        ax.set_ylim(miny - pad, maxy + pad)
        ax.set_aspect("equal")
        ax.axis("off")
    for ax in axes[n:]:
        ax.axis("off")
    fig.suptitle(f"W-P.005_補令一　街角第 1 宗之寬（S）與深（含道路截角·紅斜線）（退縮 {tag} m·示範資料）",
                 fontsize=16)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(out_png, dpi=90)
    plt.close(fig)


def main(argv):
    src, out, *tags = argv
    os.makedirs(out, exist_ok=True)
    rc = 0
    for t in tags:
        p = os.path.join(out, f"W-P.005_補令一_街角宗之寬深_退縮{t}m.png")
        corner_png(src, t, p)
        sz = os.path.getsize(p)
        print(f"{p}\t{sz} bytes")
        rc |= int(sz == 0)
    return rc


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
    """⇒ (cb_by, cad, omap, {退縮: g_rows})。管線之印出一律收於記憶體（⛔ 擾本程式之輸出）。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        snapshot = rv.load_snapshot()
        ns, fake_st = harvest()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        rows = {}
        for sb in setbacks:
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            _d, _s, _o, win, forced, _tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snapshot)
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3,
                            win, forced, sb, eff_min_build_by_blk={})
            rows[sb] = sg["g_rows"]
        omap = dict(fake_st.session_state["t8_ownership_map"])
    return cb_by, cad, omap, rows


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


def lots_of(g_rows, blocks, omap):
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
    cb_by, cad, omap, rows = run_pipeline(a.setback)
    blocks = blocks_of(cb_by, cad)
    for sb in a.setback:
        lots, dropped = lots_of(rows[sb], blocks, omap)
        doc = {"退縮_m": sb, "來源": SOURCE_NOTE, "街廓": blocks, "宗": lots, "略": dropped}
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

## 附錄戊　`plots/post_maps.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005　重劃後三圖層（公告分配地籍線·分配後歸戶圖·重劃後地價圖）＋ 暫編→正式地號對照表
＋ 顏色對照表（重劃後）。

命令列：python plots/post_maps.py --state <配地結果_退縮*.json> --pre-dxf <重劃前圖.dxf>
          --moedict <dict-revised.json> --out <目錄> [--map <地號對照表.xlsx>]
  --state   ＝ plots/alloc_state.py 之輸出。
  --pre-dxf ＝ plots/prelim_maps.py 之「重劃前圖.dxf」（三圖層·W-P.001／002 定版）；本程式讀之、加三圖層、另存（⛔ 改原檔）。
  --map     ＝ 承辦人改過之地號對照表（本程式前次之輸出）；無 ⇒ 依 S 型自動編定之預設。
輸出（皆寫至 --out，⛔ 入倉）：公告圖_退縮<t>m.dxf（六圖層）、地號對照表_退縮<t>m.xlsx、顏色對照表_重劃後_退縮<t>m.xlsx。

所據：出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md（§一、§二）。
  KL 2026-10-28 23:31：問一 甲（程式依 S 型自動編定；全範圍同一地段；先排區〔東北先〕、再區內 S 型）；
  問四 乙（每宗註記地號、面積、分配寬度、深度）；問五 乙（抵費地自成一色並註「抵費地」；道路、公園不填色、
  只畫界線；原地主分得之地照一般歸戶上色）。KL 23:37：保留「暫編 → 正式地號對照表」（重號或缺號即停）。
  W-P.005_補令一（KL 2026-10-30 08:00）：公告分配地籍線之「寬」顯示 S（G 值計算之臨正面道路寬度）；
  「深」＝ 面積 ÷ W（W ＝ 宗地寬度·判畸零地之寬·街角宗亦為截角前之寬）；街角第 1 宗之深 ＝
  （面積 ＋ 道路截角面積）÷ W——道路截角面積 ＝ 正面臨路線與側面道路線之交點（未截角之理論角）與該宗之截角線
  所圍之面積，由圖資幾何算出，唯供計算深度（⛔ 改面積之註記與配地面積）。
缺值一律報錯停止（⛔ 靜默補值）。
"""
import argparse
import json
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （重劃前之歸戶、顏色、歸戶號·W-P.001／002）
import owner_index  # noqa: E402

LAYER_POST_CAD = "公告分配地籍線"
LAYER_POST_OWN = "分配後歸戶圖"
LAYER_POST_PRICE = "重劃後地價圖"
POST_LAYERS = (LAYER_POST_CAD, LAYER_POST_OWN, LAYER_POST_PRICE)
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_TEXT = "抵費地"
OFFSET_COLOR = (160, 160, 160)
LINE_GAP = 1.4                       # 多列註記之行距（× 字高）
REGION_TOL = 0.01                    # 區之相接之容差（公尺）
ON_LINE_TOL = 0.02                   # 宗之頂點落於正面臨路線、側面道路線上之容差（公尺）
NO_RE = re.compile(r"^[1-9]\d{0,4}(-[1-9]\d*)?$")   # 母號（不超過五位數）或「母號-子號」（手冊第 3849〜3854 列）
MAP_SHEET = "地號對照表"
MAP_HEAD = ("暫編", "街廓", "類別", "配地之暫編地號", "預設地號（S 型）", "正式地號", "面積（㎡）")
MAP_NOTE = "「正式地號」得由承辦人改之（例：段界另有調整）；重號或空白者，本程式即停止產出（KL 2026-10-28 23:37）。"


def q2(x):
    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def f2(x):
    return f"{q2(x):.2f}"


# ---------------------------------------------------------------- 讀取
def load_state(path):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    for k in ("退縮_m", "街廓", "宗", "略"):
        if k not in doc:
            raise PM.SourceError(f"配地結果缺 {k}")
    if not doc["宗"]:
        raise PM.SourceError("配地結果無宗")
    return doc


def tag_of(doc):
    return f"{float(doc['退縮_m']):g}"


def post_prices():
    v = json.load(open(PM.CASE_PARAMS, encoding="utf-8"))["財務接線_v3"]
    if "後街廓_面積單價" not in v:
        raise PM.SourceError("case_params 之 財務接線_v3 缺 後街廓_面積單價")
    return {b: float(d["單價_元每m2"]) for b, d in v["後街廓_面積單價"].items()}


# ---------------------------------------------------------------- 宗之整理
def entries_of(doc):
    """⇒ 重劃後之各宗（分配地、抵費地、公設之區塊），各附暫編（街廓-序號；公設 ＝ 其編號）。"""
    from shapely.geometry import Polygon
    blocks = doc["街廓"]
    ents = []
    by_blk = {}
    for x in doc["宗"]:
        by_blk.setdefault(x["街廓"], []).append(x)
    for lbl in sorted(blocks):
        b = blocks[lbl]
        if "宗地分配線方向" not in b:
            continue
        lots = by_blk.get(lbl, [])
        if not lots:
            raise PM.SourceError(f"可分配之街廓 {lbl} 無宗")
        (x1, y1), (x2, y2) = b["正面臨路線"]
        L = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        ux, uy = (x2 - x1) / L, (y2 - y1) / L

        def t_of(x):
            p = Polygon(x["多邊形"]).representative_point()
            return (p.x - x1) * ux + (p.y - y1) * uy
        for i, x in enumerate(sorted(lots, key=t_of), start=1):
            e = dict(x)
            e["暫編"] = f"{lbl}-{i:02d}"
            ents.append(e)
    for lbl in sorted(blocks):
        b = blocks[lbl]
        if "宗地分配線方向" in b:
            continue
        if lbl in by_blk:
            raise PM.SourceError(f"非可分配之街廓 {lbl} 有配地之宗")
        ents.append({"暫編": lbl, "配地暫編": None, "街廓": lbl, "類別": b["分類"],
                     "面積": float(q2(Polygon(b["多邊形"]).area)), "多邊形": b["多邊形"]})
    return ents


def regions(blocks):
    """⇒ [[街廓…]]：重劃範圍之相連之各區（各街廓之多邊形外擴 REGION_TOL 後之相連者）。"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    polys = {k: Polygon(v["多邊形"]) for k, v in blocks.items()}
    u = unary_union([p.buffer(REGION_TOL) for p in polys.values()])
    parts = list(getattr(u, "geoms", [u]))
    out = []
    for part in parts:
        mem = sorted(k for k, p in polys.items() if part.contains(p.representative_point()))
        out.append((part, mem))
    if sorted(k for _, m in out for k in m) != sorted(polys):
        raise PM.SourceError("街廓之分區不全或重複")
    return out


def _ne_key(geom):
    c = geom.centroid
    return (-round(c.y, 3), -round(c.x, 3))


def s_order(doc, ents):
    """重劃後地號之預設編定（KL 23:31 問一 甲）⇒ [暫編]（依地號 1、2、3…之序）。
    區：依其形心先北後南（同者先東）；區內之可分配之街廓：依形心先北後南（同者先東），
    第 1、3、5…個街廓之宗自東而西、第 2、4、6…個自西而東（S 型）；正東西向之正面臨路線則以先北後南代東西。
    各區之宗編畢，公設之區塊（道路、公園）續編於後（依區之序，區內依形心先北後南、同者先東）。"""
    from shapely.geometry import Polygon
    blocks = doc["街廓"]
    by_blk = {}
    for e in ents:
        by_blk.setdefault(e["街廓"], []).append(e)
    regs = sorted(regions(blocks), key=lambda pm: _ne_key(pm[0]))
    order, publics = [], []
    for _part, mem in regs:
        alloc = [k for k in mem if "宗地分配線方向" in blocks[k]]
        pub = [k for k in mem if "宗地分配線方向" not in blocks[k]]
        alloc.sort(key=lambda k: _ne_key(Polygon(blocks[k]["多邊形"])))
        for i, k in enumerate(alloc):
            (x1, y1), (x2, y2) = blocks[k]["正面臨路線"]
            dx, dy = x2 - x1, y2 - y1
            L = (dx * dx + dy * dy) ** 0.5
            ux, uy = dx / L, dy / L
            west = (-ux > 1e-9) or (abs(ux) <= 1e-9 and uy < 0)
            if not west:
                ux, uy = -ux, -uy          # u 指向西（正東西向者指向南）
            if i % 2 == 1:
                ux, uy = -ux, -uy          # 第 2、4、6…個街廓：自西而東

            def t_of(e):
                p = Polygon(e["多邊形"]).representative_point()
                return p.x * ux + p.y * uy
            order.extend(e["暫編"] for e in sorted(by_blk[k], key=t_of))
        pub.sort(key=lambda k: _ne_key(Polygon(blocks[k]["多邊形"])))
        publics.extend(pub)
    order.extend(publics)
    if sorted(order) != sorted(e["暫編"] for e in ents):
        raise PM.SourceError("S 型之編定漏宗或重複")
    return order


# ---------------------------------------------------------------- 地號對照表
def default_numbers(order):
    return {t: str(i) for i, t in enumerate(order, start=1)}


def write_map(path, ents, order, numbers, default):
    import openpyxl
    from openpyxl.styles import Alignment
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = MAP_SHEET
    ws.append(list(MAP_HEAD))
    pos = {t: i for i, t in enumerate(order)}
    for e in sorted(ents, key=lambda e: pos[e["暫編"]]):
        ws.append([e["暫編"], e["街廓"], e["類別"], e.get("配地暫編"), default[e["暫編"]],
                   numbers[e["暫編"]], float(q2(e["面積"]))])
    ws.append([])
    ws.append([MAP_NOTE])
    for c in ws[1]:
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    wb.save(path)


def read_map(path, ents):
    """承辦人之對照表 ⇒ {暫編: 正式地號}。暫編之集合不符、正式地號空白、格式不合、重號 ⇒ SourceError（停止）。"""
    import openpyxl
    ws = openpyxl.load_workbook(path, data_only=True)[MAP_SHEET]
    rows = list(ws.iter_rows(values_only=True))
    if tuple(rows[0][:len(MAP_HEAD)]) != MAP_HEAD:
        raise PM.SourceError(f"對照表之表頭不符：{rows[0]}")
    want = {e["暫編"] for e in ents}
    got = {}
    for r in rows[1:]:
        t = r[0]
        if t is None or str(t).strip() == "" or str(t) == MAP_NOTE:
            continue
        t = str(t).strip()
        if t not in want:
            raise PM.SourceError(f"對照表之暫編 {t} 非本次配地之宗")
        if t in got:
            raise PM.SourceError(f"對照表之暫編 {t} 重複")
        v = r[5]
        if v is None or str(v).strip() == "":
            raise PM.SourceError(f"對照表之暫編 {t} 之正式地號空白（缺號）")
        s = str(int(v)) if isinstance(v, (int, float)) and float(v).is_integer() else str(v).strip()
        if not NO_RE.match(s):
            raise PM.SourceError(f"對照表之暫編 {t} 之正式地號 {v!r} 非整數之母號（或母號-子號）")
        got[t] = s
    miss = sorted(want - set(got))
    if miss:
        raise PM.SourceError(f"對照表缺暫編：{miss}")
    seen = {}
    for t, s in sorted(got.items()):
        if s in seen:
            raise PM.SourceError(f"正式地號 {s} 重號：{seen[s]}、{t}")
        seen[s] = t
    return got


# ---------------------------------------------------------------- 歸戶（照重劃前之歸戶號與顏色）
def owner_scheme(moedict, ents):
    strokes = owner_index.load_strokes(moedict)
    lots, owners, area = PM.load_cadastre()
    key_of, hh_order = PM.households(lots, owners)
    hh_color = dict(zip(hh_order, PM.distinct_palette(len(hh_order))))
    hh_lots, members = PM.household_members(owners, key_of)
    hh_no = owner_index.number_households(hh_lots, members, strokes, PM.landno_key)
    if OFFSET_COLOR in hh_color.values():
        raise PM.SourceError("抵費地之色與某戶之色同")
    g_of = {}
    for e in ents:
        if e["類別"] != KIND_LOT:
            continue
        ln = e["原地號"]
        if ln not in key_of:
            raise PM.SourceError(f"{e['暫編']} 之原地號 {ln} 不在重劃前之地籍")
        k = key_of[ln]
        if g_of.setdefault(e["歸戶"], k) != k:
            raise PM.SourceError(f"配地之歸戶 {e['歸戶']} 與重劃前之歸戶不一（{ln}）")
    if len(set(g_of.values())) != len(g_of):
        raise PM.SourceError("重劃前之一戶對應配地之數歸戶")
    return key_of, hh_color, hh_no


# ---------------------------------------------------------------- DXF
def _texts(msp, layer, lines, p):
    from ezdxf.enums import TextEntityAlignment
    n = len(lines)
    for i, s in enumerate(lines):
        y = p.y + ((n - 1) / 2 - i) * PM.TEXT_HEIGHT * LINE_GAP
        t = msp.add_text(s, height=PM.TEXT_HEIGHT, dxfattribs={"layer": layer, "style": PM.TEXT_STYLE})
        t.set_placement((p.x, y), align=TextEntityAlignment.MIDDLE_CENTER)


def _line_cross(a1, a2, b1, b2):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a1, a2, b1, b2
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-12:
        raise PM.SourceError("正面臨路線與側面道路線平行，無交點")
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def corner_cut(e, blocks):
    """街角第 1 宗之道路截角 ⇒ shapely 多邊形：正面臨路線與該側之側面道路線（皆延長）之交點 C，
    與該宗之邊界上「正面臨路線上最近 C 之頂點 A」至「側面道路線上最近 C 之頂點 B」之一段（截角線）所圍。
    A ＝ B（無截角）⇒ 空。取不到 A、B 或所圍者與該宗重疊 ⇒ SourceError。"""
    import math
    from shapely.geometry import LineString, Point, Polygon
    b = blocks[e["街廓"]]
    side = e["街角第1宗側別"]
    f1, f2_ = b["正面臨路線"]
    s1, s2 = b["側面道路線"][side]
    c = _line_cross(f1, f2_, s1, s2)
    coords = [(float(x), float(y)) for x, y in e["多邊形"]]
    if coords[0] == coords[-1]:
        coords = coords[:-1]
    fl, sl = LineString([f1, f2_]), LineString([s1, s2])
    on_f = [i for i, p in enumerate(coords) if fl.distance(Point(p)) <= ON_LINE_TOL]
    on_s = [i for i, p in enumerate(coords) if sl.distance(Point(p)) <= ON_LINE_TOL]
    if not on_f or not on_s:
        raise PM.SourceError(f"{e['暫編']} 為街角第 1 宗而其邊界不臨正面臨路線或側面道路線")
    ia = min(on_f, key=lambda i: math.dist(coords[i], c))
    ib = min(on_s, key=lambda i: math.dist(coords[i], c))
    if ia == ib:
        return Polygon()
    n = len(coords)

    def chain(i, j):
        out = [i]
        while i != j:
            i = (i + 1) % n
            out.append(i)
        return out
    c1, c2 = chain(ia, ib), chain(ib, ia)
    cut = Polygon([c] + [coords[i] for i in (c1 if len(c1) <= len(c2) else c2)])
    if not cut.is_valid or cut.intersection(Polygon(coords)).area > 1e-6:
        raise PM.SourceError(f"{e['暫編']} 之道路截角之形不合")
    return cut


def cad_lines(e, no, blocks):
    if e["類別"] == KIND_LOT:
        s = q2(e["S"])
        w = q2(e["宗地寬度"])
        a = Decimal(repr(float(e["面積"])))
        if "街角第1宗側別" in e:
            a += q2(corner_cut(e, blocks).area)
        d = (a / w).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return [no, f2(e["面積"]), f"寬{s:.2f}", f"深{d:.2f}"]
    return [no, f2(e["面積"])]


def write_dxf(pre_path, path, ents, numbers, key_of, hh_color, hh_no, price, price_color, blocks):
    import ezdxf
    from shapely.geometry import Polygon
    doc = ezdxf.readfile(pre_path)
    for name in PM.LAYERS:
        if name not in doc.layers:
            raise PM.SourceError(f"重劃前圖缺圖層 {name}")
    for name in POST_LAYERS:
        if name in doc.layers:
            raise PM.SourceError(f"重劃前圖已有圖層 {name}")
        doc.layers.add(name)
    msp = doc.modelspace()
    for e in sorted(ents, key=lambda e: e["暫編"]):
        coords = [(float(x), float(y)) for x, y in e["多邊形"]]
        if coords[0] == coords[-1]:
            coords = coords[:-1]
        rp = Polygon(coords).representative_point()
        no = numbers[e["暫編"]]
        msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": LAYER_POST_CAD})
        _texts(msp, LAYER_POST_CAD, cad_lines(e, no, blocks), rp)
        if e["類別"] in (KIND_LOT, KIND_OFFSET):
            h = msp.add_hatch(dxfattribs={"layer": LAYER_POST_OWN})
            if e["類別"] == KIND_LOT:
                k = key_of[e["原地號"]]
                h.set_solid_fill(rgb=hh_color[k])
                lab = str(hh_no[k])
            else:
                h.set_solid_fill(rgb=OFFSET_COLOR)
                lab = OFFSET_TEXT
            h.paths.add_polyline_path(coords, is_closed=True)
            _texts(msp, LAYER_POST_OWN, [lab], rp)
            v = price[e["街廓"]]
            h2 = msp.add_hatch(dxfattribs={"layer": LAYER_POST_PRICE})
            h2.set_solid_fill(rgb=price_color[v])
            h2.paths.add_polyline_path(coords, is_closed=True)
            _texts(msp, LAYER_POST_PRICE, [f2(v)], rp)
        else:
            msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": LAYER_POST_OWN})
    doc.saveas(path)


def write_color_table(path, ents, numbers, key_of, hh_color, hh_no, price, price_color):
    import openpyxl
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    ws = wb.create_sheet(LAYER_POST_OWN)
    ws.append(["圖層", "歸戶號", "顏色 R,G,B", "正式地號"])
    by_hh = {}
    for e in ents:
        if e["類別"] == KIND_LOT:
            by_hh.setdefault(key_of[e["原地號"]], []).append(numbers[e["暫編"]])
    for k in sorted(by_hh, key=lambda kk: hh_no[kk]):
        ws.append([LAYER_POST_OWN, hh_no[k], "{},{},{}".format(*hh_color[k]),
                   "、".join(sorted(by_hh[k], key=PM.landno_key))])
    offs = sorted((numbers[e["暫編"]] for e in ents if e["類別"] == KIND_OFFSET), key=PM.landno_key)
    if offs:
        ws.append([LAYER_POST_OWN, OFFSET_TEXT, "{},{},{}".format(*OFFSET_COLOR), "、".join(offs)])
    ws2 = wb.create_sheet(LAYER_POST_PRICE)
    ws2.append(["圖層", "顏色 R,G,B", "重劃後地價（元/㎡）", "街廓", "正式地號"])
    for v in sorted(price_color):
        blks = sorted(b for b, p in price.items() if p == v)
        nos = sorted((numbers[e["暫編"]] for e in ents
                      if e["類別"] in (KIND_LOT, KIND_OFFSET) and price[e["街廓"]] == v), key=PM.landno_key)
        ws2.append([LAYER_POST_PRICE, "{},{},{}".format(*price_color[v]), f2(v), "、".join(blks), "、".join(nos)])
    wb.save(path)


OUT_FMT = {"dxf": "公告圖_退縮{}m.dxf", "map": "地號對照表_退縮{}m.xlsx", "color": "顏色對照表_重劃後_退縮{}m.xlsx"}


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 重劃後三圖層＋地號對照表＋顏色對照表")
    ap.add_argument("--state", required=True)
    ap.add_argument("--pre-dxf", required=True)
    ap.add_argument("--moedict", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map")
    a = ap.parse_args(argv)
    doc = load_state(a.state)
    tag = tag_of(doc)
    ents = entries_of(doc)
    order = s_order(doc, ents)
    default = default_numbers(order)
    numbers = read_map(a.map, ents) if a.map else dict(default)
    key_of, hh_color, hh_no = owner_scheme(a.moedict, ents)
    price_all = post_prices()
    blks = sorted({e["街廓"] for e in ents if e["類別"] in (KIND_LOT, KIND_OFFSET)})
    miss = [b for b in blks if b not in price_all]
    if miss:
        raise PM.SourceError(f"case_params 之 後街廓_面積單價 缺：{miss}")
    price = {b: price_all[b] for b in blks}
    vals = sorted(set(price.values()))
    price_color = dict(zip(vals, PM.distinct_palette(len(vals))))
    os.makedirs(a.out, exist_ok=True)
    p = {k: os.path.join(a.out, v.format(tag)) for k, v in OUT_FMT.items()}
    write_map(p["map"], ents, order, numbers, default)
    write_dxf(a.pre_dxf, p["dxf"], ents, numbers, key_of, hh_color, hh_no, price, price_color, doc["街廓"])
    write_color_table(p["color"], ents, numbers, key_of, hh_color, hh_no, price, price_color)
    n = {k: sum(1 for e in ents if e["類別"] == k) for k in (KIND_LOT, KIND_OFFSET)}
    print(f"退縮 {tag} m：分配地 {n[KIND_LOT]}、抵費地 {n[KIND_OFFSET]}、公設 {len(ents) - sum(n.values())}；"
          f"略 {[x['配地暫編'] for x in doc['略']]}")
    print("地號：" + "、".join(f"{t}→{numbers[t]}" for t in order))
    print(f"重劃後地價 {[f2(v) for v in vals]}（街廓 {price}）")
    for k, v in p.items():
        print(f"輸出 {v}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄己　`docs/出圖/W-P.005_補令一_寬深之註記.md`（逐位元組照錄）

````markdown
# W-P.005_補令一　公告分配地籍線之「寬」「深」之註記

## 依據（KL）

- 2026-10-29 23:33（`出圖線/KL答覆/2026-10-29_2333.md`）：第 1、3〜5 點是；第 2 點反問實量深之段與寬可否顯示 S。
- 2026-10-30 08:00（`出圖線/KL答覆/2026-10-30_0800.md`）：「1. 深度維持現行，但特例是街角地，可否僅在計算街角地深度時，其街角地面積把截角面積暫時納入，再以面積(含道路截角)/寬」「2. 計算深度用的（面積 ÷ 寬）寬用W會比較準，但圖面顯示時用S，民眾比較直觀」。

## 規則之要

- 分配地之註記：地號／面積（二位）／「寬」＋ S（G 值計算之臨正面道路寬度·二位）／「深」＋ 深（二位）。
- 深 ＝ 面積 ÷ W；W ＝ 宗地寬度（垂直於宗地分配線·判畸零地所用·二位）。
- 街角第 1 宗（配地結果「第1筆街角」＝是）：深 ＝（面積 ＋ 道路截角面積）÷ W。
  - 道路截角 ＝ 正面臨路線與該側之側面道路線（皆延長）之交點（未截角之理論角）與該宗之截角線所圍之形；面積由圖資幾何算出（二位），唯供計算深度，⛔ 改面積之註記、⛔ 改配地面積。
  - 街角第 1 宗之 W 已為截角前之寬（S 自理論角起量 × 正面臨路線與「垂直於宗地分配線」之夾角之餘弦；本案八宗之截角後之寬小 3.4〜3.7 m），故⛔ 另改 W（K-9-5-15 五：角地之寬度與深度一律以截角前形狀量測）。
- 抵費地、道路、公園：唯地號／面積（不變）。
- 分配線與正面臨路線斜交 ⇒ 圖上之「寬（S）× 深」不等於面積（本案 S − W 為 0.02〜0.09 m）。

## 量測與故意錯誤

- `verify/plots/check_W-P005.py`：V3 之寬改驗 S、深改驗上式（街角之截角以異法：該宗與理論角之凸包減該宗）；新增 V8（每一側面道路線恰一街角第 1 宗、其 W 為截角前之寬、截角落於道路且⛔ 與宗重疊）。二退縮共 18 項。
- `verify/plots/mutate_W-P005.py`：新增 Ⓕ 寬仍註 W、Ⓖ 街角之深未納截角、Ⓗ 深以 S 除、Ⓘ 街角之 W 用截角後之寬。
- `verify/plots/preview_W-P005a.py`：街角第 1 宗之放大圖（截角以紅斜線示之）。
````

## 附錄庚　本案各分配地之 S、W 與深（發單端原型之實得·供 KL 知斜交之差）

### 退縮 3.5 m

| 配地之暫編地號 | 街廓 | 街角第 1 宗 | 面積 | S（圖之寬） | W | S − W | 道路截角 | 舊深（面積 ÷ W） | 新深 | S × 新深 | S × 新深 − 面積 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|628-36(1)|R1|左|638.61|19.46|19.40|0.06|6.71|32.92|33.26|647.24|8.63|
|628-35(2)|R1||741.92|22.22|22.15|0.07||33.50|33.50|744.37|2.45|
|628(5)|R1|右|376.11|11.53|11.49|0.04|5.77|32.73|33.24|383.26|7.15|
|628-37(1)|R1||285.21|8.41|8.38|0.03||34.03|34.03|286.19|0.98|
|628(1)|R4|左|1788.69|54.22|54.16|0.06|6.86|33.03|33.15|1797.39|8.70|
|628-1(1)|R4|右|721.79|21.99|21.97|0.02|6.28|32.85|33.14|728.75|6.96|
|628-4(1)|R6||779.93|14.72|14.67|0.05||53.16|53.16|782.52|2.59|
|628-21(1)|R6||433.74|9.32|9.29|0.03||46.69|46.69|435.15|1.41|
|628-20(1)|R6||466.36|10.12|10.09|0.03||46.22|46.22|467.75|1.39|
|628-18(1)|R6|右|307.78|7.22|7.20|0.02|5.77|42.75|43.55|314.43|6.65|
|628-7(1)|R6||1007.91|22.82|22.75|0.07||44.30|44.30|1010.93|3.02|
|628-45(1)|R5|左|525.27|12.13|12.08|0.05|6.14|43.48|43.99|533.60|8.33|
|628-18(2)|R5||268.34|7.74|7.71|0.03||34.80|34.80|269.35|1.01|
|628-7(2)|R5||712.26|15.94|15.87|0.07||44.88|44.88|715.39|3.13|
|628-23(2)|R5||430.68|9.06|9.02|0.04||47.75|47.75|432.62|1.94|
|628-22(2)|R5||520.82|11.07|11.02|0.05||47.26|47.26|523.17|2.35|
|628-21(2)|R5||471.39|10.12|10.08|0.04||46.76|46.76|473.21|1.82|
|628-41(1)|R2|左|313.50|7.12|7.10|0.02|6.28|44.15|45.04|320.68|7.18|
|628-40(1)|R2||359.60|9.71|9.69|0.02||37.11|37.11|360.34|0.74|
|628-39(1)|R2||289.42|6.46|6.44|0.02||44.94|44.94|290.31|0.89|
|628-31(2)|R2||465.05|10.40|10.37|0.03||44.85|44.85|466.44|1.39|
|628-34(1)|R2||601.64|13.65|13.62|0.03||44.17|44.17|602.92|1.28|
|628-32(2)|R2||516.09|11.68|11.65|0.03||44.30|44.30|517.42|1.33|
|628-34(2)|R3||257.91|5.89|5.86|0.03||44.01|44.01|259.22|1.31|
|628-47(1)|R3||429.59|9.80|9.76|0.04||44.02|44.02|431.40|1.81|
|628-32(3)|R3||500.44|11.38|11.33|0.05||44.17|44.17|502.65|2.21|
|628-45(2)|R3|右|902.52|20.30|20.21|0.09|6.20|44.66|44.96|912.69|10.17|
|628-31(3)|R3||464.94|8.74|8.70|0.04||53.44|53.44|467.07|2.13|

S − W 之最大 0.09 m。

### 退縮 0 m

| 配地之暫編地號 | 街廓 | 街角第 1 宗 | 面積 | S（圖之寬） | W | S − W | 道路截角 | 舊深（面積 ÷ W） | 新深 | S × 新深 | S × 新深 − 面積 |
|---|---|---|---|---|---|---|---|---|---|---|---|
|628-37(1)|R1|左|272.82|8.43|8.40|0.03|6.71|32.48|33.28|280.55|7.73|
|628-35(2)|R1||730.81|21.88|21.81|0.07||33.51|33.51|733.20|2.39|
|628(5)|R1|右|376.11|11.53|11.49|0.04|5.77|32.73|33.24|383.26|7.15|
|628-36(1)|R1||662.10|19.78|19.72|0.06||33.58|33.58|664.21|2.11|
|628(1)|R4|左|1788.69|54.22|54.16|0.06|6.86|33.03|33.15|1797.39|8.70|
|628-1(1)|R4|右|721.79|21.99|21.97|0.02|6.28|32.85|33.14|728.75|6.96|
|628-4(1)|R6||779.93|14.72|14.67|0.05||53.16|53.16|782.52|2.59|
|628-21(1)|R6||433.74|9.32|9.29|0.03||46.69|46.69|435.15|1.41|
|628-20(1)|R6||466.36|10.12|10.09|0.03||46.22|46.22|467.75|1.39|
|628-18(1)|R6|右|307.78|7.22|7.20|0.02|5.77|42.75|43.55|314.43|6.65|
|628-7(1)|R6||1007.91|22.82|22.75|0.07||44.30|44.30|1010.93|3.02|
|628-18(2)|R5|左|259.13|6.07|6.04|0.03|6.14|42.90|43.92|266.59|7.46|
|628-20(2)|R5||534.49|13.80|13.74|0.06||38.90|38.90|536.82|2.33|
|628-7(2)|R5||712.26|15.94|15.87|0.07||44.88|44.88|715.39|3.13|
|628-23(2)|R5||430.68|9.06|9.02|0.04||47.75|47.75|432.62|1.94|
|628-22(2)|R5||520.82|11.07|11.02|0.05||47.26|47.26|523.17|2.35|
|628-21(2)|R5||471.39|10.12|10.08|0.04||46.76|46.76|473.21|1.82|
|628-41(1)|R2|左|313.50|7.12|7.10|0.02|6.28|44.15|45.04|320.68|7.18|
|628-40(1)|R2||359.60|9.71|9.69|0.02||37.11|37.11|360.34|0.74|
|628-39(1)|R2||289.42|6.46|6.44|0.02||44.94|44.94|290.31|0.89|
|628-31(2)|R2||465.05|10.40|10.37|0.03||44.85|44.85|466.44|1.39|
|628-34(1)|R2||601.64|13.65|13.62|0.03||44.17|44.17|602.92|1.28|
|628-32(2)|R2||516.09|11.68|11.65|0.03||44.30|44.30|517.42|1.33|
|628-34(2)|R3||257.91|5.89|5.86|0.03||44.01|44.01|259.22|1.31|
|628-47(1)|R3||429.59|9.80|9.76|0.04||44.02|44.02|431.40|1.81|
|628-32(3)|R3||500.44|11.38|11.33|0.05||44.17|44.17|502.65|2.21|
|628-45(2)|R3|右|343.45|7.80|7.77|0.03|6.20|44.20|45.00|351.00|7.55|
|628-30(3)|R3||562.02|10.88|10.83|0.05||51.89|51.89|564.56|2.54|
|628-31(3)|R3||461.99|10.37|10.33|0.04||44.72|44.72|463.75|1.76|

S − W 之最大 0.07 m。

## 附錄辛　對照之比對（倉外之暫存·⛔ 入倉·工項 5(b)）

命令列：`<py> 附錄辛.py <對照組之目錄> <成果目錄> <退縮>`（附錄甲之路徑須依所在之倉改其第 2 列）。

```python
import sys,ezdxf,openpyxl,importlib.util
sp=importlib.util.spec_from_file_location('c','/tmp/r/verify/plots/check_W-P005.py');c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
a,b,t=sys.argv[1:4]
def sigs(d):
    m=ezdxf.readfile(f'{d}/公告圖_退縮{t}m.dxf').modelspace()
    keep=[];wd=[]
    for e in m:
        s=c._sig(e)
        if e.dxftype()=='TEXT' and e.dxf.layer==c.L_CAD and (e.dxf.text.startswith('寬') or e.dxf.text.startswith('深')):
            wd.append(s);continue
        keep.append(s)
    return sorted(map(repr,keep)),len(wd)
ka,na=sigs(a);kb,nb=sigs(b)
print('非寬深之圖元',len(ka),'同' if ka==kb else '異','寬深之文字',na,nb)
for f in (f'地號對照表_退縮{t}m.xlsx',f'顏色對照表_重劃後_退縮{t}m.xlsx'):
    va=[[list(r) for r in ws.iter_rows(values_only=True)] for ws in openpyxl.load_workbook(f'{a}/{f}').worksheets]
    vb=[[list(r) for r in ws.iter_rows(values_only=True)] for ws in openpyxl.load_workbook(f'{b}/{f}').worksheets]
    print(f,'同' if va==vb else '異')
```
