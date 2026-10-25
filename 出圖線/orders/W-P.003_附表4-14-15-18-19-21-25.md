# W-P.003　附表 4、14、15、18、19、21、25（照手冊表樣）

- **題**：依 KL 2026-10-25 15:10 之下一步（`出圖線/KL答覆/2026-10-25_1510.md`），產製 A 類之附表之一批：附表 4 抵充土地清冊、14 他項權利清冊、15 限制登記清冊、18 重劃前地價評議表、19 重劃後地價評議表、21 重劃後可分配土地街廓面積地價計算表、25 街角地側面道路負擔百分率累積表。各照手冊之表樣（KL 10/24 02:14、14:55：表頭、簽欄、列印標題之通式）。
- **發單端之改分**（記於 `出圖線/交接.md`）：附表 20、22、23（公共設施用地負擔面積統計表、計算負擔總計表二式）移 `W-P.004`——其逐項之公設、臨街地特別負擔之分項與範例 1／2 之擇，手冊與資料未定，須先調查並請示。
- **範圍**：唯新增 `plots/appx_tables.py`、`verify/plots/check_W-P003.py`、`verify/plots/mutate_W-P003.py`、`verify/plots/preview_W-P003.py`、`docs/出圖/W-P.003_附表4-14-15-18-19-21-25.md`；⛔ 改任何既有之檔（含本線既有之 `plots/prelim_maps.py`、`plots/owner_index.py`）；⛔ 改 `requirements.txt`；⛔ 新套件。
- **授權（逐字）**：
  - KL 2026-10-23 17:31「1. 是　2. 以手冊（拾參）所附的圖例為主」；17:48「…還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」（README 第一節）。
  - KL 2026-10-24 02:14「1 .是　2. 是，表格改照手冊表樣（乙）」；14:55「是」（附表之表樣之通式）；2026-10-25 15:10「是」（W-P.002 全部定版·下一步 W-P.003）。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `d4928d4845513a42fb1ac826a63167a38c78d4fb`；`wip/plots` ＝ `cb55e0b396f15179b48f24170bc37683383d4c75`（已含 `d4928d4`）。
- **側支**：`verify/W-P.003-tables-a`（自 `wip/plots` 出）。單號 `W-P.003` 經 `git grep -F` 證未占用（主倉 `cb55e0b`、佇列）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具）。

## §一　所據

1. **手冊**（`參考/市地重劃作業手冊.txt`）：
   - 附表 4：第 731〜741 列（抵充土地之二類）、第 879〜899 列（表樣·表末三合計與「日期：編造：校對：承辦人：科長：」）。
   - 附表 14、15：第 2735〜2747 列（「重劃後轉載情形欄暫不填寫」）、第 2771、2773 列（表樣·附註「本表未列事項詳原土地登記簿記載」·簽欄「日期：承辦：股長：科長：局(處)長：」）。
   - 附表 18、19：第 2803〜2826 列（重劃前為宗地地價，計算至個位數、四捨五入；重劃後劃設區段價之範圍）、第 2851、2853 列（表樣·「評議日期」）。
   - 附表 21：第 3117〜3123 列、第 3312〜3330 列（表樣）。
   - 附表 25：第 4048〜4078 列（1〜18 公尺 × 十分位之 Rw 百分率、「公分以下用內插法」、表註）。
2. **資料**（唯讀）：
   - `verify/case_params_UC9898.json` 之 `財務接線_v3`：`抵充地_m2` ＝ 0（「KL 確認皆為 0」）；`原地號_區段`、`重劃前區段_面積單價`（a 43909.23…、b 37322.85…·W-P.001 已以個位四捨五入用於重劃前地價圖·KL 10/24 02:14 定版）；`後街廓_面積單價`（R1〜R6 之面積與單價·全精度；其 Σ(面積×單價) ＝ 1643176255.06 為 KL 之錨〔`C分母形式`〕、Σ面積 ＝ 22803.33〔`_重劃後平均地價_來源`〕）；`global.分區` ＝ 住宅區。
   - `data/地籍資料來源_匿名版.xlsx`：「重劃區地籍」（53 宗·花蓮市·德安段·小段空）；`U_LAND` 之「權利種類」（現存之他項權利）於本區 95 列皆空；限制登記之欄匯入資料無（「重劃區地籍」之「有無限制登記」皆空）。
3. **既有之函式**（唯讀·`import`）：`plots/prelim_maps.py` 之 `load_cadastre`、`load_price_zones`、`round_half_up`、`landno_key`、`_grid`、`_page`、`_blank`、`SourceError`（W-P.001／002 之物·⛔ 改）。
4. **內容之判斷**（手冊或資料已定者·本單照之；⛔ 新定）：
   - 附表 4：KL 確認抵充地 0 ⇒ 無列、三合計皆 0。
   - 附表 14、15：現存他項權利 0、限制登記無資料 ⇒ 無列（表樣照出）。遇有列者停機（§四 3）。
   - 附表 18：每宗一列（表之「土地坐落」欄至地號），依區段、地號排；區段與單價之格縱向合併；單價 ＝ W-P.001 之宗地地價（個位）。評議之三欄留空。
   - 附表 19：每街廓一列（重劃後區段價係依街廓·`_後街廓_來源`）；「起訖點或範圍」填「街廓 R1」等；「街路或地段名稱」資料所無 ⇒ 留空；單價存全精度（核心線之 KL 裁定「全精度參與乘除，禁先 round」）、顯示二位小數。
   - 附表 21：每街廓一列；「編號」「計算式」（規劃測量人員之面積計算）資料所無 ⇒ 留空；面積 ＝ 後街廓之面積；「單價 × 面積」以文字示之；總價 ＝ 面積 × 單價（二位四捨五入·六街廓之和 ＝ 錨 1643176255.06）。
   - 附表 25：照錄手冊之值（法定之表）。**⛔ 用 `app.py` 之 `rw_from_width`**：其表為整數公尺之一位小數、線性內插，與手冊之表差至 0.05（如 5.3 公尺：手冊 45.85、程式 45.8）——此差已記於 `出圖線/交接.md`「交監看窗」，屬核心線之事，本單⛔ 涉。

## §二　規格

1. **新增 `plots/appx_tables.py`**：逐位元組 ＝ 附錄丁。命令列 `python plots/appx_tables.py --out <倉外之目錄>`，輸出七檔（各一工作表·A4 列印·寬一頁·列印標題）：
   | 檔 | 表樣之要（行列以 1 起） |
   |---|---|
   | `附表04_抵充土地清冊.xlsx` | 列 1 題（A1:J1）；列 2 十欄之表頭；列 3〜5 三合計（A 欄文字、E 欄 0、F 欄「平方公尺」）；列 7 簽欄 |
   | `附表14_他項權利清冊.xlsx` | 列 1 題；列 2 所有權人欄（姓名、住址、統編、分配清冊第冊第頁號·值空）；列 3〜5 三層表頭 21 欄；列 7 附註；列 8 簽欄 |
   | `附表15_限制登記清冊.xlsx` | 同上之式·23 欄 |
   | `附表18_重劃前地價評議表.xlsx` | 列 1 題；列 2 評議日期；列 3〜4 表頭 9 欄；列 5〜57 每宗一列 |
   | `附表19_重劃後地價評議表.xlsx` | 列 1 題；列 2 評議日期；列 3 表頭 7 欄；列 4〜9 R1〜R6 |
   | `附表21_重劃後可分配土地街廓面積地價計算表.xlsx` | 列 1〜2 題；列 3「第○可分配土地街廓面積地價圖」；列 4〜5 表頭 7 欄；列 6〜11 R1〜R6；列 13 簽欄 |
   | `附表25_街角地側面道路負擔百分率累積表.xlsx` | 列 1 題；列 2〜3 表頭（公寸 0.0、1〜9·備註）；列 4〜21 為 1〜18 公尺；列 22 表註 |
2. **新增 `verify/plots/check_W-P003.py`**：逐位元組 ＝ 附錄甲（量測 P0〜P7·獨立於 `plots/`）。
3. **新增 `verify/plots/mutate_W-P003.py`**：逐位元組 ＝ 附錄乙（故意錯誤 Ⓐ〜Ⓖ）。
4. **新增 `verify/plots/preview_W-P003.py`**：逐位元組 ＝ 附錄丙。
5. **新增 `docs/出圖/W-P.003_附表4-14-15-18-19-21-25.md`**：本單之授權之逐字、§一 4 之各判斷與其所據、附表 20、22、23 移 `W-P.004` 之由、附表 25 與程式現行之 Rw 之差（唯記·⛔ 改）、量測與故意錯誤之表。
6. 發單端之原型（暫存·⛔ 入倉）已依附錄丁實作：附錄甲 8/8 綠；附錄乙之成果綠、7 種皆紅（Ⓐ P4、Ⓑ P4、Ⓒ P6、Ⓓ P7、Ⓔ P5、Ⓕ P2、Ⓖ P0＋P1）；出表約 15 秒、量測約 15 秒、故意錯誤約 50 秒。預覽見 `出圖線/待KL/W-P.003_原型預覽.png`。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.003-tables-a`；`git merge --no-edit origin/wip/s1-endpart`（主線未前進者即無事）；有衝突即停機。
2. **程式**：§二 1〜5。附錄甲〜丁之取用法：自本單擷取該附錄之 ```` ```python ```` 與 ```` ``` ```` 間之文字，末尾一換行；bytes 與 sha256 須合：
   - 甲 `verify/plots/check_W-P003.py`：18454 bytes·`73e6220125ad07f99d0e2a7ae746fc94abc243c9cedf24104d1501d1cf9685ef`
   - 乙 `verify/plots/mutate_W-P003.py`：4339 bytes·`0e0b4b4a05a908bed246bf0a67f98d0e6bba93f3263f15e1589fe1a4dc2304bd`
   - 丙 `verify/plots/preview_W-P003.py`：3126 bytes·`39693f9d8fc4d1a5d0f5858c839738f91c95668da415cfef996c2992cc4a5381`
   - 丁 `plots/appx_tables.py`：16978 bytes·`cc5c59f8870ad3be712a5c8df3a105b125b438d46efb24bc4566256eac1961c6`
   不合即停機上呈；⛔ 改一字。
3. **量測**：`python plots/appx_tables.py --out <out>`（印「附表18 53 列」「Σ面積 22803.33·Σ總價 1643176255.06」「附表25 171 格」）；`python verify/plots/check_W-P003.py <out>` ⇒ P0〜P7 共 8 項皆 PASS、結束碼 0。另照舊：`plots/fetch_moedict.py`、`plots/prelim_maps.py --out <out2> --moedict <json>`、`check_W-P001.py`（12/12）、`check_W-P002.py`（8/8·第三參數以 `synth_W-P002a.py` 產之）——證既有之輸出未受擾。
4. **故意錯誤之測**：`python verify/plots/mutate_W-P003.py <out> <拋棄式之工作目錄>` ⇒ 成果綠；Ⓐ〜Ⓖ 皆紅（所紅之項記之）。
5. **差異閘**（README 第四節）：`git diff --name-status d4928d4845513a42fb1ac826a63167a38c78d4fb <側支之端>`（主線若前進，以實際併入之主線之 sha 代之）每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status cb55e0b <側支之端>` 唯 §二 之五新檔（皆 `A`·主線前進所帶入者除外）；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：`python verify/plots/preview_W-P003.py <out> <PNG 目錄>`，其輸出 `W-P.003_附表4-14-15-18-19-21-25.png` 入佇列之 `出圖線/成果/`。
7. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
8. **回報**：`出圖線/reports/W-P.003_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、差異閘與對照組、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲〜丁之 bytes 或 sha256 不合；或 P0〜P7 於成果不過而非程式之誤。
3. `plots/appx_tables.py` 報 `SourceError`（如抵充地非 0、有現存之他項權利）——⛔ 自擬填法。
4. 須改任何既有之檔、或須新套件。
5. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P003.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.003：附表 4、14、15、18、19、21、25 之量測。
獨立於 plots/：⛔ import 之；期望取自倉內原始資料（data/地籍資料來源_匿名版.xlsx、verify/case_params_UC9898.json）、
手冊（參考/市地重劃作業手冊.txt 第 879〜899、2771〜2773、2851〜2853、3312〜3330、4048〜4078 列）與 KL 之錨。

命令列：python verify/plots/check_W-P003.py <成果目錄>
  成果目錄 ＝ plots/appx_tables.py --out 之目錄。
任一不過 ⇒ 結束碼 1。
P0 七檔皆在、可讀；P1 附表 4；P2 附表 14；P3 附表 15；P4 附表 18；P5 附表 19；P6 附表 21；P7 附表 25。
"""
import hashlib
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
XLSX_SRC = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
CASE = os.path.join(REPO, "verify", "case_params_UC9898.json")
SECTION_NAME = "0013德安段"
FILES = {
    4: "附表04_抵充土地清冊.xlsx",
    14: "附表14_他項權利清冊.xlsx",
    15: "附表15_限制登記清冊.xlsx",
    18: "附表18_重劃前地價評議表.xlsx",
    19: "附表19_重劃後地價評議表.xlsx",
    21: "附表21_重劃後可分配土地街廓面積地價計算表.xlsx",
    25: "附表25_街角地側面道路負擔百分率累積表.xlsx",
}
# KL 之錨（verify/case_params_UC9898.json 之 財務接線_v3：C分母形式 Σ(後街廓面積×單價) ＝ 1643176255.06；
#   重劃後平均地價之來源注 Σ可建築面積 22803.33）
ANCHOR_SUM_TOTAL = Decimal("1643176255.06")
ANCHOR_SUM_AREA = Decimal("22803.33")
ANCHOR_ZONE = {"a": (43909, 5), "b": (37323, 48)}     # W-P.001 之區段地價（個位）與宗數
# 手冊附表 25 之 171 格（「W.十分位:值」以「;」接）之 sha256（發單端自手冊第 4053〜4076 列解析）
RW_SHA = "3ddefae4f4ab41a16eaedb7c057050aa921580027950d3a0efbf7e34abf4d8fa"
RW_SPOT = {(1, 0): 17.36, (1, 1): 18.08, (5, 3): 45.85, (12, 0): 80.00, (17, 9): 99.75, (18, 0): 100.00}

A4_HEAD = ["鄉鎮市區", "段", "小段", "地號", "登記面積（㎡）", "抵充面積（㎡）", "權屬", "管理機關", "代管機關", "備註"]
A4_FOOT = ["合計道路、溝渠、河川等土地抵充面積：", "未登記土地面積：", "總計抵充土地面積："]
A4_SIGN = ["日期：", "編造：", "校對：", "承辦人：", "科長："]
A14_SIGN = ["日期：", "承辦：", "股長：", "科長：", "局(處)長："]
A14_NOTE = "附註：本表未列事項詳原土地登記簿記載"
A14_CELLS = {
    (1, 1): "○○縣(市)第○○期○○○○市地重劃區他項權利清冊",
    (3, 1): "重劃前原載情形", (3, 15): "重劃後變更情形", (3, 21): "備註",
    (4, 1): "土地標示", (4, 7): "權利人", (4, 9): "主登記次序", (4, 10): "權利種類", (4, 11): "權利範圍",
    (4, 12): "權利價值", (4, 13): "存續期間", (4, 14): "其他登記事項", (4, 15): "土地標示", (4, 20): "協議內容",
    (5, 1): "鄉鎮市區", (5, 2): "段", (5, 3): "小段", (5, 4): "地號", (5, 5): "面積（㎡）", (5, 6): "持分比率",
    (5, 7): "姓名", (5, 8): "住址", (5, 15): "段", (5, 16): "小段", (5, 17): "地號", (5, 18): "面積（㎡）",
    (5, 19): "持分比率",
}
A14_MERGES = {"A1:U1", "A3:N3", "O3:T3", "U3:U5", "A4:F4", "G4:H4", "I4:I5", "J4:J5", "K4:K5", "L4:L5",
              "M4:M5", "N4:N5", "O4:S4", "T4:T5"}
A15_CELLS = {
    (1, 1): "○○縣(市)第○○期○○○○市地重劃區限制登記清冊",
    (3, 1): "重劃前原載情形", (3, 13): "重劃後轉載情形", (3, 23): "備註",
    (4, 1): "土地標示", (4, 7): "權利人", (4, 9): "登記種類", (4, 10): "權利範圍", (4, 11): "內容",
    (4, 12): "限制登記文號及囑託機關", (4, 13): "土地標示", (4, 18): "權利人", (4, 20): "登記種類",
    (4, 21): "權利範圍", (4, 22): "協議內容",
    (5, 1): "鄉鎮市區", (5, 2): "段", (5, 3): "小段", (5, 4): "地號", (5, 5): "面積（㎡）", (5, 6): "持分比率",
    (5, 7): "姓名", (5, 8): "國民身分證統一編號", (5, 13): "段", (5, 14): "小段", (5, 15): "地號",
    (5, 16): "面積（㎡）", (5, 17): "持分比率", (5, 18): "姓名", (5, 19): "國民身分證統一編號",
}
A15_MERGES = {"A1:W1", "A3:L3", "M3:V3", "W3:W5", "A4:F4", "G4:H4", "I4:I5", "J4:J5", "K4:K5", "L4:L5",
              "M4:Q4", "R4:S4", "T4:T5", "U4:U5", "V4:V5"}
OWNER_BLOCK = ["土地所有權人姓名", "住址", "國民身分證統一編號", "分配清冊　第　冊　第　頁　號"]
A18_HEAD3 = {1: "區段編號", 2: "查估之重劃前每平方公尺單價", 3: "土地坐落",
             7: "地價及標準地價評議委員會修正意見、具體事實及理由", 8: "評議結果（元/平方公尺）", 9: "備註"}
A18_HEAD4 = {3: "鄉鎮市區", 4: "段", 5: "小段", 6: "地號"}
A19_HEAD = ["區段編號", "街路或地段名稱", "起訖點或範圍", "查估之路線價或區段價（元/平方公尺）",
            "地價及標準地價評議委員會修正意見、具體事實及理由", "評議結果（元/平方公尺）", "備註"]
A21_HEAD4 = {1: "街廓編號", 2: "都市計畫使用分區", 3: "規劃測量人員計算之面積", 6: "單價 × 面積", 7: "總價"}
A21_HEAD5 = {3: "編號", 4: "計算式", 5: "平方公尺"}
A21_SIGN = ["製表日期:　年　月　日", "承辦:", "股長:", "科長:"]
A25_COLHEAD = ["0.0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
REVIEW_DATE = "評議日期：　　年　　月　　日"


def _blank(v):
    return v is None or (isinstance(v, str) and v.strip() in ("", "null"))


def rhu(x, nd):
    q = Decimal(1).scaleb(-nd)
    return Decimal(repr(float(x))).quantize(q, rounding=ROUND_HALF_UP)


def landno_key(s):
    p = str(s).split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0)


def _ws(out, n):
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(out, FILES[n]))
    if len(wb.worksheets) != 1:
        raise AssertionError(f"附表 {n} 之工作表數 {len(wb.worksheets)}≠1")
    return wb.worksheets[0]


def _merges(ws):
    return {str(m) for m in ws.merged_cells.ranges}


def _last(ws):
    last = 0
    for row in ws.iter_rows():
        for c in row:
            if not _blank(c.value):
                last = max(last, c.row)
    return last


def _row_vals(ws, r, ncol):
    return [ws.cell(r, c).value for c in range(1, ncol + 1)]


def _nonblank(ws, r):
    return [v for v in _row_vals(ws, r, ws.max_column) if not _blank(v)]


def _cells(ws, want):
    bad = [(rc, ws.cell(*rc).value, v) for rc, v in want.items() if ws.cell(*rc).value != v]
    return bad


# ---------------------------------------------------------------- 獨立之讀
def src_lots():
    import openpyxl
    wb = openpyxl.load_workbook(XLSX_SRC, read_only=True)
    rows = list(wb["重劃區地籍"].iter_rows(values_only=True))
    h = rows[0]
    it, isec, il = h.index("鄉鎮市"), h.index("地段"), h.index("地號")
    lots = {str(r[il]).strip(): (r[it], r[isec]) for r in rows[1:] if not _blank(r[il])}
    head = None
    rights = 0
    for r in wb["U_LAND"].iter_rows(values_only=True):
        if head is None:
            head = r
            ik = [i for i, x in enumerate(head) if x == "權利種類"]
            if len(ik) != 1:
                raise AssertionError(f"U_LAND 之「權利種類」欄 {len(ik)} 個")
            ik = ik[0]
            continue
        if r[0] != SECTION_NAME or _blank(r[1]):
            continue
        m, s = divmod(int(r[1]), 10000)
        ln = f"{m}" if s == 0 else f"{m}-{s}"
        if ln in lots and not _blank(r[ik]):
            rights += 1
    return lots, rights


def src_case():
    d = json.load(open(CASE, encoding="utf-8"))
    return d["財務接線_v3"], d["global"]["分區"]


# ---------------------------------------------------------------- 量測
def p0(out):
    import openpyxl
    for n, f in FILES.items():
        p = os.path.join(out, f)
        if not os.path.isfile(p) or os.path.getsize(p) == 0:
            return False, f"缺或空：{f}"
        wb = openpyxl.load_workbook(p)
        if _last(wb.worksheets[0]) == 0:
            return False, f"無內容：{f}"
    return True, "七檔皆在、可讀、非空"


def p1(out, v):
    ws = _ws(out, 4)
    if ws.cell(1, 1).value != "○○縣(市)第○○期○○市地重劃區抵充土地清冊" or "A1:J1" not in _merges(ws):
        return False, f"題：{ws.cell(1, 1).value!r}"
    if _row_vals(ws, 2, 10) != A4_HEAD:
        return False, f"表頭：{_row_vals(ws, 2, 10)}"
    want_area = v["抵充地_m2"]
    if want_area != 0:
        return False, f"case_params 之抵充地_m2＝{want_area}（本單唯 0）"
    for i, lab in enumerate(A4_FOOT):
        got = _nonblank(ws, 3 + i)
        if got != [lab, 0, "平方公尺"]:
            return False, f"列 {3 + i}：{got}"
    sign = _last(ws)
    if _nonblank(ws, sign) != A4_SIGN or sign != 7 or any(_nonblank(ws, r) for r in (6,)):
        return False, f"簽欄（列 {sign}）：{_nonblank(ws, sign)}"
    return True, "表頭 10 欄、無列、三合計 0 ㎡（case_params 抵充地_m2＝0）、簽欄列 7"


def _rights_form(ws, n, cells, merges, ncol):
    bad = _cells(ws, cells)
    if bad:
        return f"表頭格：{bad[:3]}"
    miss = merges - _merges(ws)
    if miss:
        return f"合併格缺：{sorted(miss)}"
    if _nonblank(ws, 2) != OWNER_BLOCK:
        return f"所有權人欄：{_nonblank(ws, 2)}"
    if any(_nonblank(ws, 6)):
        return f"列 6 有值：{_nonblank(ws, 6)}"
    if _nonblank(ws, 7) != [A14_NOTE] or _nonblank(ws, 8) != A14_SIGN or _last(ws) != 8:
        return f"附註／簽欄：{_nonblank(ws, 7)} {_nonblank(ws, 8)} 末列 {_last(ws)}"
    if ws.max_column < ncol or _blank(ws.cell(3, ncol).value):
        return f"欄數不足 {ncol}"
    return None


def p2(out, rights):
    if rights != 0:
        return False, f"示範資料之現存他項權利 {rights} 列（本單唯 0 列之式）"
    ws = _ws(out, 14)
    e = _rights_form(ws, 14, A14_CELLS, A14_MERGES, 21)
    return (False, e) if e else (True, "表頭三層 21 欄合手冊、無列（現存他項權利 0）、附註與簽欄")


def p3(out):
    ws = _ws(out, 15)
    e = _rights_form(ws, 15, A15_CELLS, A15_MERGES, 23)
    return (False, e) if e else (True, "表頭三層 23 欄合手冊、無列（匯入資料無限制登記之欄）、附註與簽欄")


def p4(out, lots, v):
    ws = _ws(out, 18)
    if ws.cell(1, 1).value != "○○縣（市）第○○期○○○○市地重劃區重劃前地價評議表" or ws.cell(2, 1).value != REVIEW_DATE:
        return False, f"題／評議日期：{ws.cell(1, 1).value!r} {ws.cell(2, 1).value!r}"
    if _cells(ws, {(3, c): t for c, t in A18_HEAD3.items()}) or _cells(ws, {(4, c): t for c, t in A18_HEAD4.items()}):
        return False, "表頭"
    zone_of = v["原地號_區段"]
    unit = {z: d["單價_元每m2"] for z, d in v["重劃前區段_面積單價"].items()}
    price = {z: int(rhu(u, 0)) for z, u in unit.items()}
    for z, (pp, cnt) in ANCHOR_ZONE.items():
        if price.get(z) != pp or sum(1 for ln in lots if zone_of.get(ln) == z) != cnt:
            return False, f"錨：區段 {z} 之地價 {price.get(z)}／宗數"
    want = []
    for z in sorted(set(zone_of[ln] for ln in lots)):
        for ln in sorted([x for x in lots if zone_of[x] == z], key=landno_key):
            want.append((z, price[z], lots[ln][0], lots[ln][1], None, ln))
    merged = {}
    for m in ws.merged_cells.ranges:
        for r in range(m.min_row, m.max_row + 1):
            for c in range(m.min_col, m.max_col + 1):
                merged[(r, c)] = ws.cell(m.min_row, m.min_col).value
    got = []
    for r in range(5, _last(ws) + 1):
        vals = [merged.get((r, c), ws.cell(r, c).value) for c in range(1, 10)]
        if any(not _blank(x) for x in vals[6:]):
            return False, f"列 {r} 之評議欄有值：{vals[6:]}"
        got.append(tuple(None if _blank(x) else x for x in vals[:6]))
    if got != want:
        diff = [(i, g, w) for i, (g, w) in enumerate(zip(got, want)) if g != w][:2]
        return False, f"列數 {len(got)}／{len(want)}；差 {diff}"
    for z in ANCHOR_ZONE:
        rs = [5 + i for i, w in enumerate(want) if w[0] == z]
        rng = f"A{rs[0]}:A{rs[-1]}"
        if len(rs) > 1 and rng not in _merges(ws):
            return False, f"區段 {z} 之格未合併（{rng}）"
    return True, f"{len(got)} 列＝{len(lots)} 宗、序（區段→地號）、區段地價 a 43909×5、b 37323×48、評議欄空"


def _post(v):
    b = v["後街廓_面積單價"]
    keys = sorted(b, key=lambda k: (int(k[1:]), k))
    return [(k, Decimal(repr(float(b[k]["面積_m2"]))), float(b[k]["單價_元每m2"])) for k in keys]


def p5(out, v):
    ws = _ws(out, 19)
    if ws.cell(1, 1).value != "○○縣（市）第○○期○○○○市地重劃區重劃後地價評議表" or ws.cell(2, 1).value != REVIEW_DATE:
        return False, "題／評議日期"
    if _row_vals(ws, 3, 7) != A19_HEAD:
        return False, f"表頭：{_row_vals(ws, 3, 7)}"
    post = _post(v)
    if _last(ws) != 3 + len(post):
        return False, f"末列 {_last(ws)}≠{3 + len(post)}"
    for i, (k, a, u) in enumerate(post):
        r = 4 + i
        row = _row_vals(ws, r, 7)
        if row[0] != k or not _blank(row[1]) or row[2] != f"街廓 {k}" or any(not _blank(x) for x in row[4:]):
            return False, f"列 {r}：{row}"
        if not isinstance(row[3], (int, float)) or abs(row[3] - u) > 1e-6:
            return False, f"列 {r} 單價 {row[3]}≠{u}"
        if ws.cell(r, 4).number_format != "#,##0.00":
            return False, f"列 {r} 單價之格式 {ws.cell(r, 4).number_format}"
    return True, f"{len(post)} 列 R1〜R{len(post)}、單價全精度（|差|≤1e-6）、顯示二位"


def p6(out, v, zoning):
    ws = _ws(out, 21)
    if ws.cell(1, 1).value != "○○縣(市)第○○期○○市地重劃區" or ws.cell(2, 1).value != "重劃後可分配土地街廓面積地價計算表":
        return False, "題"
    if ws.cell(3, 5).value != "第○可分配土地街廓面積地價圖":
        return False, f"圖號格：{ws.cell(3, 5).value!r}"
    if _cells(ws, {(4, c): t for c, t in A21_HEAD4.items()}) or _cells(ws, {(5, c): t for c, t in A21_HEAD5.items()}):
        return False, "表頭"
    post = _post(v)
    sa, st = Decimal(0), Decimal(0)
    for i, (k, a, u) in enumerate(post):
        r = 6 + i
        row = _row_vals(ws, r, 7)
        tot = rhu(float(a) * u, 2)
        want = [k, zoning, None, None, float(a), f"{u:,.2f} × {float(a):,.2f}", float(tot)]
        if row[:4] != want[:4] or row[5] != want[5] or abs(row[4] - want[4]) > 1e-9 or abs(row[6] - want[6]) > 1e-6:
            return False, f"列 {r}：{row} ≠ {want}"
        sa += Decimal(repr(row[4]))
        st += rhu(row[6], 2)
    if sa != ANCHOR_SUM_AREA or st != ANCHOR_SUM_TOTAL:
        return False, f"Σ面積 {sa}／Σ總價 {st} ≠ 錨 {ANCHOR_SUM_AREA}／{ANCHOR_SUM_TOTAL}"
    sign = 6 + len(post) + 1
    if _nonblank(ws, sign) != A21_SIGN or _last(ws) != sign:
        return False, f"簽欄（列 {sign}）：{_nonblank(ws, sign)}"
    return True, f"{len(post)} 列；Σ面積 {sa}、Σ總價 {st}（＝KL 之錨）；簽欄列 {sign}"


def p7(out):
    ws = _ws(out, 25)
    if ws.cell(1, 1).value != "街角地側面道路負擔百分率累積表":
        return False, "題"
    if [ws.cell(3, c).value for c in range(2, 12)] != A25_COLHEAD or ws.cell(2, 2).value != "公寸" \
            or ws.cell(3, 1).value != "RW" or ws.cell(2, 12).value != "備註" or ws.cell(4, 12).value != "公分以下用內插法。":
        return False, "表頭"
    vals = {}
    for r in range(4, 22):
        w = ws.cell(r, 1).value
        if w != r - 3:
            return False, f"列 {r} 之公尺 {w}"
        for j in range(10):
            x = ws.cell(r, 2 + j).value
            if w == 18 and j > 0:
                if not _blank(x):
                    return False, f"18 公尺列之第 {j} 格有值 {x}"
                continue
            if not isinstance(x, (int, float)):
                return False, f"({w},{j}) 非數：{x!r}"
            vals[(w, j)] = float(x)
    s = ";".join(f"{w}.{j}:{vals[(w, j)]:.2f}" for w, j in sorted(vals))
    if len(vals) != 171 or hashlib.sha256(s.encode()).hexdigest() != RW_SHA:
        bad = [(k, vals.get(k), x) for k, x in RW_SPOT.items() if vals.get(k) != x]
        return False, f"171 格之 sha256 不合手冊（格數 {len(vals)}；錨差 {bad}）"
    seq = [vals[k] for k in sorted(vals)]
    if any(b <= a for a, b in zip(seq, seq[1:])):
        return False, "非嚴格遞增"
    if ws.cell(22, 1).value != "註：本表係由前面負擔百分率簡表推演而來。" or _last(ws) != 22:
        return False, f"註／末列 {_last(ws)}"
    return True, "171 格合手冊（sha256 " + RW_SHA[:8] + "…）、嚴格遞增、表頭與註"


def run(out, src=None, quiet=False):
    """⇒ 不過之項名之列。src ＝ (lots, rights, v, zoning)（省略者即讀之）。"""
    if src is None:
        lots, rights = src_lots()
        v, zoning = src_case()
    else:
        lots, rights, v, zoning = src
    tests = [
        ("P0", lambda: p0(out)),
        ("P1", lambda: p1(out, v)),
        ("P2", lambda: p2(out, rights)),
        ("P3", lambda: p3(out)),
        ("P4", lambda: p4(out, lots, v)),
        ("P5", lambda: p5(out, v)),
        ("P6", lambda: p6(out, v, zoning)),
        ("P7", lambda: p7(out)),
    ]
    fails = []
    for name, fn in tests:
        try:
            ok, msg = fn()
        except Exception as e:  # noqa: BLE001  量測之例外即不過
            ok, msg = False, f"{type(e).__name__}: {e}"
        if not quiet:
            print(f"{'PASS' if ok else 'FAIL'} {name} {msg}")
        if not ok:
            fails.append(name)
    if not quiet:
        print(f"{len(tests) - len(fails)}/{len(tests)}" + (f"；不過：{fails}" if fails else ""))
    return fails


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    return 1 if run(argv[0]) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄乙　`verify/plots/mutate_W-P003.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.003 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓖ 共 7 種變異體須各紅（量測 ＝ check_W-P003.py 之 8 項）。

命令列：python verify/plots/mutate_W-P003.py <成果目錄> <拋棄式之工作目錄>
  成果目錄 ＝ plots/appx_tables.py --out 之目錄（⛔ 改之；變異體皆寫於工作目錄）。
  Ⓑ、Ⓓ 掛換 plots/ 之函式或常數後重出（於本行程之記憶體中·⛔ 改檔）；他者改成果之複本。
結束碼：成果綠且 7 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P003", os.path.join(HERE, "check_W-P003.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)

# 程式現行之 Rw（app.py rw_from_width：整數公尺之一位小數·線性內插）——與手冊之表差 ≤ 0.05
APP_RW = [0.0, 17.4, 24.4, 31.3, 37.8, 44.0, 50.0, 55.7, 61.1, 66.3,
          71.1, 75.7, 80.0, 84.0, 87.8, 91.3, 94.4, 97.4, 100.0]


def _copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def _book(d, n):
    import openpyxl
    p = os.path.join(d, chk.FILES[n])
    return p, openpyxl.load_workbook(p)


def _plots():
    sys.path.insert(0, os.path.join(REPO, "plots"))
    import appx_tables
    return appx_tables


def _regen(d, obj, attr, val):
    orig = getattr(obj, attr)
    setattr(obj, attr, val)
    try:
        if os.path.exists(d):
            shutil.rmtree(d)
        _plots().main(["--out", d])
    finally:
        setattr(obj, attr, orig)


def mA_drop_lot(d):
    p, wb = _book(d, 18)
    ws = wb.worksheets[0]
    ws.delete_rows(chk._last(ws))
    wb.save(p)


def mB_unrounded_price(d):
    at = _plots()
    pm = at.PM
    orig = pm.load_price_zones

    def load(path=pm.CASE_PARAMS):
        z, u, _ = orig(path)
        return z, u, dict(u)
    _regen(d, pm, "load_price_zones", load)


def mC_rounded_unit_total(d):
    p, wb = _book(d, 21)
    ws = wb.worksheets[0]
    for r in range(6, 12):
        a = ws.cell(r, 5).value
        u = float(ws.cell(r, 6).value.split(" × ")[0].replace(",", ""))
        ws.cell(r, 7, float(chk.rhu(round(u) * a, 2)))
    wb.save(p)


def mD_app_rw(d):
    at = _plots()
    tab = {w: tuple(round(APP_RW[w] + (APP_RW[w + 1] - APP_RW[w]) * j / 10, 2) for j in range(10))
           for w in range(1, 18)}
    tab[18] = (100.0,)
    _regen(d, at, "RW_TABLE", tab)


def mE_swap_post(d):
    p, wb = _book(d, 19)
    ws = wb.worksheets[0]
    a, b = ws.cell(5, 4).value, ws.cell(6, 4).value
    ws.cell(5, 4, b)
    ws.cell(6, 4, a)
    wb.save(p)


def mF_drop_header(d):
    p, wb = _book(d, 14)
    ws = wb.worksheets[0]
    ws.cell(4, 12).value = None
    wb.save(p)


def mG_empty_file(d):
    open(os.path.join(d, chk.FILES[4]), "wb").close()


MUTANTS = [
    ("Ⓐ 附表 18 漏一宗", mA_drop_lot, True),
    ("Ⓑ 區段地價未取個位", mB_unrounded_price, False),
    ("Ⓒ 附表 21 總價以取整之單價計", mC_rounded_unit_total, True),
    ("Ⓓ 附表 25 用程式現行之 Rw", mD_app_rw, False),
    ("Ⓔ 附表 19 R2、R3 單價互換", mE_swap_post, True),
    ("Ⓕ 附表 14 漏「權利價值」", mF_drop_header, True),
    ("Ⓖ 附表 4 為空檔", mG_empty_file, True),
]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print(__doc__)
        return 2
    out, work = argv
    lots, rights = chk.src_lots()
    v, zoning = chk.src_case()
    src = (lots, rights, v, zoning)
    base = chk.run(out, src, quiet=True)
    print(f"成果：{'綠' if not base else '紅 ' + str(base)}")
    ok = not base
    for i, (name, fn, from_copy) in enumerate(MUTANTS):
        d = os.path.join(work, f"m{i}")
        if from_copy:
            _copy(out, d)
            fn(d)
        else:
            fn(d)
        fails = chk.run(d, src, quiet=True)
        print(f"{name}：{'紅 ' + str(fails) if fails else '綠（未捕）'}")
        ok = ok and bool(fails)
    print("合" if ok else "不合")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄丙　`verify/plots/preview_W-P003.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.003 之預覽 PNG（單 §三 7）：附表 4、14、15、18（前 24 列）、19、21、25 之截取。

命令列：python verify/plots/preview_W-P003.py <成果目錄> <PNG 之輸出目錄>
輸出：W-P.003_附表4-14-15-18-19-21-25.png
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

OUT_NAME = "W-P.003_附表4-14-15-18-19-21-25.png"
PANELS = [
    ("附表04_抵充土地清冊.xlsx", "附表 4　抵充土地清冊", None),
    ("附表19_重劃後地價評議表.xlsx", "附表 19　重劃後地價評議表", None),
    ("附表14_他項權利清冊.xlsx", "附表 14　他項權利清冊", None),
    ("附表21_重劃後可分配土地街廓面積地價計算表.xlsx", "附表 21　重劃後可分配土地街廓面積地價計算表", None),
    ("附表15_限制登記清冊.xlsx", "附表 15　限制登記清冊", None),
    ("附表25_街角地側面道路負擔百分率累積表.xlsx", "附表 25　街角地側面道路負擔百分率累積表", None),
    ("附表18_重劃前地價評議表.xlsx", "附表 18　重劃前地價評議表（前 24 列）", 28),
]


def _fmt(cell):
    v = cell.value
    if v is None:
        return ""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        nf = cell.number_format
        if nf == "#,##0.00":
            return f"{v:,.2f}"
        if nf == "0.00":
            return f"{v:.2f}"
        if nf == "#,##0":
            return f"{v:,.0f}"
    return str(v)


def draw(ax, path, title, max_row):
    import openpyxl
    ws = openpyxl.load_workbook(path).worksheets[0]
    last = ws.max_row if max_row is None else min(ws.max_row, max_row)
    cells = [[_fmt(ws.cell(r, c)) for c in range(1, ws.max_column + 1)] for r in range(2, last + 1)]
    ax.axis("off")
    ax.set_title(f"{title}　｜　{ws['A1'].value}", fontsize=13, loc="left")
    t = ax.table(cellText=cells, loc="upper left", cellLoc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(6.5)
    t.scale(1, 1.15)


def main(argv):
    src, out = argv
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, OUT_NAME)
    fig = plt.figure(figsize=(30, 30))
    gs = fig.add_gridspec(4, 2, height_ratios=[0.6, 0.7, 0.9, 1.6])
    for i, (f, title, mr) in enumerate(PANELS):
        ax = fig.add_subplot(gs[3, :]) if i == 6 else fig.add_subplot(gs[i // 2, i % 2])
        draw(ax, os.path.join(src, f), title, mr)
    fig.tight_layout()
    fig.savefig(p, dpi=80)
    plt.close(fig)
    sz = os.path.getsize(p)
    print(f"{p}\t{sz} bytes")
    return 0 if sz > 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄丁　`plots/appx_tables.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.003　附表 4、14、15、18、19、21、25（照手冊表樣·KL 2026-10-24 02:14／14:55）。

命令列：python plots/appx_tables.py --out <目錄>
輸出（皆寫至 --out，⛔ 入倉）：見 OUT_NAMES。
所據：出圖線/orders/W-P.003_附表4-14-15-18-19-21-25.md（§一、§二）。
  附表 4　抵充土地清冊：verify/case_params_UC9898.json 之 財務接線_v3.抵充地_m2（KL 確認 0）⇒ 無列、合計 0。
  附表 14　他項權利清冊：U_LAND 之「權利種類」（現存之他項權利）；示範資料無 ⇒ 無列。
  附表 15　限制登記清冊：匯入之地籍無限制登記之欄（「重劃區地籍」之「有無限制登記」皆空）⇒ 無列。
  附表 18　重劃前地價評議表：每宗一列；區段與宗地地價同 W-P.001（財務接線_v3·個位四捨五入·手冊第 2804〜2806 列）。
  附表 19　重劃後地價評議表：每街廓一列（財務接線_v3.後街廓_面積單價·全精度存值·顯示二位小數）。
  附表 21　重劃後可分配土地街廓面積地價計算表：每街廓一列；總價 ＝ 面積 × 單價（二位四捨五入）。
  附表 25　街角地側面道路負擔百分率累積表：手冊第 4048〜4078 列之值（法定之表·照錄）。
缺值一律報錯停止（⛔ 靜默補值）；匯入資料所無之欄留空（⛔ 杜撰）。
"""
import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （讀取與表樣之共用函式·W-P.001／002）

CASE_PARAMS = PM.CASE_PARAMS
TITLE_HEAD = "○○縣(市)第○○期○○○○市地重劃區"
TITLE_HEAD_SHORT = "○○縣(市)第○○期○○市地重劃區"
SIGN_A4 = ("日期：", "編造：", "校對：", "承辦人：", "科長：")
SIGN_A14 = ("日期：", "承辦：", "股長：", "科長：", "局(處)長：")
SIGN_A21 = ("製表日期:　年　月　日", "承辦:", "股長:", "科長:")
NOTE_A14 = "附註：本表未列事項詳原土地登記簿記載"
REVIEW_DATE = "評議日期：　　年　　月　　日"

# 附表 25（手冊第 4053〜4076 列·W 公尺 → 十分位之 Rw %）
RW_TABLE = {
    1: (17.36, 18.08, 18.80, 19.52, 20.23, 20.94, 21.64, 22.35, 23.05, 23.75),
    2: (24.44, 25.14, 25.83, 26.52, 27.20, 27.88, 28.56, 29.24, 29.91, 30.58),
    3: (31.25, 31.92, 32.58, 33.24, 33.89, 34.55, 35.20, 35.85, 36.49, 37.14),
    4: (37.78, 38.42, 39.05, 39.68, 40.31, 40.94, 41.56, 42.18, 42.80, 43.42),
    5: (44.03, 44.64, 45.24, 45.85, 46.45, 47.05, 47.64, 48.24, 48.83, 49.42),
    6: (50.00, 50.58, 51.16, 51.74, 52.31, 52.88, 53.45, 54.02, 54.58, 55.14),
    7: (55.69, 56.25, 56.80, 57.35, 57.89, 58.44, 58.98, 59.52, 60.05, 60.58),
    8: (61.11, 61.64, 62.16, 62.68, 63.20, 63.72, 64.23, 64.74, 65.24, 65.75),
    9: (66.25, 66.75, 67.24, 67.74, 68.23, 68.72, 69.20, 69.68, 70.16, 70.64),
    10: (71.11, 71.58, 72.05, 72.52, 72.98, 73.44, 73.89, 74.35, 74.80, 75.25),
    11: (75.69, 76.14, 76.58, 77.02, 77.45, 77.88, 78.31, 78.74, 79.16, 79.58),
    12: (80.00, 80.42, 80.83, 81.24, 81.64, 82.05, 82.45, 82.85, 83.24, 83.64),
    13: (84.03, 84.42, 84.80, 85.18, 85.56, 85.94, 86.31, 86.68, 87.05, 87.42),
    14: (87.78, 88.14, 88.49, 88.85, 89.20, 89.55, 89.89, 90.24, 90.58, 90.92),
    15: (91.25, 91.59, 91.91, 92.24, 92.56, 92.88, 93.20, 93.52, 93.83, 94.14),
    16: (94.44, 94.75, 95.05, 95.35, 95.64, 95.94, 96.23, 96.52, 96.80, 97.08),
    17: (97.36, 97.64, 97.91, 98.18, 98.45, 98.72, 98.98, 99.24, 99.49, 99.75),
    18: (100.00,),
}

OUT_NAMES = {
    "a4": "附表04_抵充土地清冊.xlsx",
    "a14": "附表14_他項權利清冊.xlsx",
    "a15": "附表15_限制登記清冊.xlsx",
    "a18": "附表18_重劃前地價評議表.xlsx",
    "a19": "附表19_重劃後地價評議表.xlsx",
    "a21": "附表21_重劃後可分配土地街廓面積地價計算表.xlsx",
    "a25": "附表25_街角地側面道路負擔百分率累積表.xlsx",
}


# ---------------------------------------------------------------- 共用
def _center():
    from openpyxl.styles import Alignment
    return Alignment(horizontal="center", vertical="center", wrap_text=True)


def _book():
    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    return wb, ws


def _title(ws, row, text, ncol):
    ws.cell(row, 1, text).alignment = _center()
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncol)


def _hdr(ws, r1, c1, r2, c2, text):
    ws.cell(r1, c1, text).alignment = _center()
    if (r1, c1) != (r2, c2):
        ws.merge_cells(start_row=r1, start_column=c1, end_row=r2, end_column=c2)


def _sign(ws, row, labels, ncol):
    step = max(1, ncol // len(labels))
    for i, lab in enumerate(labels):
        ws.cell(row, 1 + i * step, lab)


def load_params(path=CASE_PARAMS):
    d = json.load(open(path, encoding="utf-8"))
    v = d["財務接線_v3"]
    for k in ("抵充地_m2", "後街廓_面積單價"):
        if k not in v:
            raise PM.SourceError(f"case_params 之 財務接線_v3 缺 {k}")
    zoning = d["global"].get("分區")
    if PM._blank(zoning):
        raise PM.SourceError("case_params 之 global.分區 為空")
    return v, zoning


# ---------------------------------------------------------------- 附表 4
A4_NCOL = 10
A4_HEAD = ("鄉鎮市區", "段", "小段", "地號", "登記面積（㎡）", "抵充面積（㎡）", "權屬", "管理機關", "代管機關", "備註")


def write_a4(path, offset_area):
    if offset_area != 0:
        raise PM.SourceError(f"抵充地_m2＝{offset_area}≠0：本單唯據 KL 確認之 0（抵充之宗之清單須另單）")
    wb, ws = _book()
    ws.title = "抵充土地清冊"
    _title(ws, 1, TITLE_HEAD_SHORT + "抵充土地清冊", A4_NCOL)
    for c, lab in enumerate(A4_HEAD, start=1):
        ws.cell(2, c, lab).alignment = _center()
    PM._grid(ws, 2, 2, A4_NCOL)
    r = 3
    ws.cell(r, 1, "合計道路、溝渠、河川等土地抵充面積：")
    ws.cell(r, 5, 0)
    ws.cell(r, 6, "平方公尺")
    ws.cell(r + 1, 1, "未登記土地面積：")
    ws.cell(r + 1, 5, 0)
    ws.cell(r + 1, 6, "平方公尺")
    ws.cell(r + 2, 1, "總計抵充土地面積：")
    ws.cell(r + 2, 5, 0)
    ws.cell(r + 2, 6, "平方公尺")
    _sign(ws, r + 4, SIGN_A4, A4_NCOL)
    PM._page(ws, "1:2", landscape=True)
    wb.save(path)
    return []


# ---------------------------------------------------------------- 附表 14、15
A14_NCOL = 21
A15_NCOL = 23


def _owner_block(ws, row, ncol):
    """表頭之所有權人欄（每一所有權人一頁之式）：值留空，由使用者填。"""
    ws.cell(row, 1, "土地所有權人姓名")
    ws.cell(row, 5, "住址")
    ws.cell(row, 10, "國民身分證統一編號")
    ws.cell(row, ncol - 4, "分配清冊　第　冊　第　頁　號")


def rights_rows(owners):
    """現存之他項權利（U_LAND 之「權利種類」非空者）之列。"""
    out = []
    for ln in sorted(owners, key=PM.landno_key):
        for seq in owners[ln].values():
            for o in seq:
                if not PM._blank(o[PM.C_RIGHT_KIND]):
                    out.append((ln, o))
    return out


def write_a14(path, owners):
    rows = rights_rows(owners)
    if rows:
        raise PM.SourceError(f"有現存之他項權利 {len(rows)} 列：本單未定其填法 ⇒ 停機上呈")
    wb, ws = _book()
    ws.title = "他項權利清冊"
    _title(ws, 1, TITLE_HEAD + "他項權利清冊", A14_NCOL)
    _owner_block(ws, 2, A14_NCOL)
    _hdr(ws, 3, 1, 3, 14, "重劃前原載情形")
    _hdr(ws, 3, 15, 3, 20, "重劃後變更情形")
    _hdr(ws, 3, 21, 5, 21, "備註")
    _hdr(ws, 4, 1, 4, 6, "土地標示")
    _hdr(ws, 4, 7, 4, 8, "權利人")
    for c, lab in zip(range(9, 15), ("主登記次序", "權利種類", "權利範圍", "權利價值", "存續期間", "其他登記事項")):
        _hdr(ws, 4, c, 5, c, lab)
    _hdr(ws, 4, 15, 4, 19, "土地標示")
    _hdr(ws, 4, 20, 5, 20, "協議內容")
    for c, lab in enumerate(("鄉鎮市區", "段", "小段", "地號", "面積（㎡）", "持分比率", "姓名", "住址"), start=1):
        ws.cell(5, c, lab).alignment = _center()
    for c, lab in enumerate(("段", "小段", "地號", "面積（㎡）", "持分比率"), start=15):
        ws.cell(5, c, lab).alignment = _center()
    PM._grid(ws, 3, 5, A14_NCOL)
    ws.cell(7, 1, NOTE_A14)
    _sign(ws, 8, SIGN_A14, A14_NCOL)
    PM._page(ws, "1:5", landscape=True)
    wb.save(path)
    return rows


def write_a15(path):
    wb, ws = _book()
    ws.title = "限制登記清冊"
    _title(ws, 1, TITLE_HEAD + "限制登記清冊", A15_NCOL)
    _owner_block(ws, 2, A15_NCOL)
    _hdr(ws, 3, 1, 3, 12, "重劃前原載情形")
    _hdr(ws, 3, 13, 3, 22, "重劃後轉載情形")
    _hdr(ws, 3, 23, 5, 23, "備註")
    _hdr(ws, 4, 1, 4, 6, "土地標示")
    _hdr(ws, 4, 7, 4, 8, "權利人")
    for c, lab in zip(range(9, 13), ("登記種類", "權利範圍", "內容", "限制登記文號及囑託機關")):
        _hdr(ws, 4, c, 5, c, lab)
    _hdr(ws, 4, 13, 4, 17, "土地標示")
    _hdr(ws, 4, 18, 4, 19, "權利人")
    for c, lab in zip(range(20, 23), ("登記種類", "權利範圍", "協議內容")):
        _hdr(ws, 4, c, 5, c, lab)
    for c, lab in enumerate(("鄉鎮市區", "段", "小段", "地號", "面積（㎡）", "持分比率", "姓名", "國民身分證統一編號"),
                            start=1):
        ws.cell(5, c, lab).alignment = _center()
    for c, lab in enumerate(("段", "小段", "地號", "面積（㎡）", "持分比率", "姓名", "國民身分證統一編號"), start=13):
        ws.cell(5, c, lab).alignment = _center()
    PM._grid(ws, 3, 5, A15_NCOL)
    ws.cell(7, 1, NOTE_A14)
    _sign(ws, 8, SIGN_A14, A15_NCOL)
    PM._page(ws, "1:5", landscape=True)
    wb.save(path)
    return []


# ---------------------------------------------------------------- 附表 18
A18_NCOL = 9


def write_a18(path, lots, zone_of, price):
    wb, ws = _book()
    ws.title = "重劃前地價評議表"
    _title(ws, 1, "○○縣（市）第○○期○○○○市地重劃區重劃前地價評議表", A18_NCOL)
    ws.cell(2, 1, REVIEW_DATE)
    _hdr(ws, 3, 1, 4, 1, "區段編號")
    _hdr(ws, 3, 2, 4, 2, "查估之重劃前每平方公尺單價")
    _hdr(ws, 3, 3, 3, 6, "土地坐落")
    for c, lab in enumerate(("鄉鎮市區", "段", "小段", "地號"), start=3):
        ws.cell(4, c, lab).alignment = _center()
    _hdr(ws, 3, 7, 4, 7, "地價及標準地價評議委員會修正意見、具體事實及理由")
    _hdr(ws, 3, 8, 4, 8, "評議結果（元/平方公尺）")
    _hdr(ws, 3, 9, 4, 9, "備註")
    rows = []
    r = 4
    for z in sorted(set(zone_of[x["地號"]] for x in lots)):
        grp = sorted([x for x in lots if zone_of[x["地號"]] == z], key=lambda x: PM.landno_key(x["地號"]))
        r0 = r + 1
        for x in grp:
            r += 1
            vals = (z, price[z], x["鄉鎮市區"], x["段"], x.get("小段"), x["地號"])
            for c, v in enumerate(vals, start=1):
                if c <= 2 and r > r0:
                    continue
                ws.cell(r, c, v)
            rows.append(vals)
        for c in (1, 2):
            ws.cell(r0, c).alignment = _center()
            if r > r0:
                ws.merge_cells(start_row=r0, start_column=c, end_row=r, end_column=c)
        ws.cell(r0, 2).number_format = "#,##0"
    PM._grid(ws, 3, r, A18_NCOL)
    PM._page(ws, "1:4", landscape=True)
    wb.save(path)
    return rows


# ---------------------------------------------------------------- 附表 19
A19_NCOL = 7
A19_HEAD = ("區段編號", "街路或地段名稱", "起訖點或範圍", "查估之路線價或區段價（元/平方公尺）",
            "地價及標準地價評議委員會修正意見、具體事實及理由", "評議結果（元/平方公尺）", "備註")


def block_key(b):
    return (int(b[1:]) if b[:1] == "R" and b[1:].isdigit() else 10 ** 9, b)


def write_a19(path, post):
    wb, ws = _book()
    ws.title = "重劃後地價評議表"
    _title(ws, 1, "○○縣（市）第○○期○○○○市地重劃區重劃後地價評議表", A19_NCOL)
    ws.cell(2, 1, REVIEW_DATE)
    for c, lab in enumerate(A19_HEAD, start=1):
        ws.cell(3, c, lab).alignment = _center()
    rows = []
    r = 3
    for b in sorted(post, key=block_key):
        u = post[b]["單價_元每m2"]
        if PM._blank(u):
            raise PM.SourceError(f"後街廓 {b} 之單價為空")
        r += 1
        vals = (b, None, f"街廓 {b}", float(u))
        for c, v in enumerate(vals, start=1):
            ws.cell(r, c, v)
        ws.cell(r, 4).number_format = "#,##0.00"
        rows.append(vals)
    PM._grid(ws, 3, r, A19_NCOL)
    PM._page(ws, "1:3", landscape=True)
    wb.save(path)
    return rows


# ---------------------------------------------------------------- 附表 21
A21_NCOL = 7


def write_a21(path, post, zoning):
    wb, ws = _book()
    ws.title = "街廓面積地價計算表"
    _title(ws, 1, TITLE_HEAD_SHORT, A21_NCOL)
    _title(ws, 2, "重劃後可分配土地街廓面積地價計算表", A21_NCOL)
    ws.cell(3, A21_NCOL - 2, "第○可分配土地街廓面積地價圖")
    _hdr(ws, 4, 1, 5, 1, "街廓編號")
    _hdr(ws, 4, 2, 5, 2, "都市計畫使用分區")
    _hdr(ws, 4, 3, 4, 5, "規劃測量人員計算之面積")
    for c, lab in enumerate(("編號", "計算式", "平方公尺"), start=3):
        ws.cell(5, c, lab).alignment = _center()
    _hdr(ws, 4, 6, 5, 6, "單價 × 面積")
    _hdr(ws, 4, 7, 5, 7, "總價")
    rows = []
    r = 5
    for b in sorted(post, key=block_key):
        a, u = post[b]["面積_m2"], post[b]["單價_元每m2"]
        if PM._blank(a) or PM._blank(u):
            raise PM.SourceError(f"後街廓 {b} 之面積或單價為空")
        a, u = float(a), float(u)
        total = PM.round_half_up(a * u, 2)
        r += 1
        vals = (b, zoning, None, None, a, f"{u:,.2f} × {a:,.2f}", total)
        for c, v in enumerate(vals, start=1):
            ws.cell(r, c, v)
        ws.cell(r, 5).number_format = "#,##0.00"
        ws.cell(r, 7).number_format = "#,##0.00"
        rows.append(vals)
    PM._grid(ws, 4, r, A21_NCOL)
    _sign(ws, r + 2, SIGN_A21, A21_NCOL)
    PM._page(ws, "1:5", landscape=True)
    wb.save(path)
    return rows


# ---------------------------------------------------------------- 附表 25
A25_NCOL = 12
A25_COLHEAD = ("0.0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def write_a25(path):
    wb, ws = _book()
    ws.title = "Rw累積表"
    _title(ws, 1, "街角地側面道路負擔百分率累積表", A25_NCOL)
    ws.cell(3, 1, "RW").alignment = _center()
    _hdr(ws, 2, 2, 2, 11, "公寸")
    for c, lab in enumerate(A25_COLHEAD, start=2):
        ws.cell(3, c, lab).alignment = _center()
    _hdr(ws, 2, 12, 3, 12, "備註")
    rows = []
    r = 3
    for w in sorted(RW_TABLE):
        r += 1
        ws.cell(r, 1, w).alignment = _center()
        for j, v in enumerate(RW_TABLE[w]):
            ws.cell(r, 2 + j, v).number_format = "0.00"
            rows.append((w, j, v))
    _hdr(ws, 4, 12, r, 12, "公分以下用內插法。")
    PM._grid(ws, 2, r, A25_NCOL)
    ws.cell(r + 1, 1, "註：本表係由前面負擔百分率簡表推演而來。")
    PM._page(ws, "1:3", landscape=False)
    wb.save(path)
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.003 附表 4、14、15、18、19、21、25")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)

    lots, owners, area = PM.load_cadastre()
    zone_of, unit, price = PM.load_price_zones()
    miss = {x["地號"] for x in lots} - set(zone_of)
    if miss:
        raise PM.SourceError(f"case_params 之原地號_區段 缺：{sorted(miss)}")
    v, zoning = load_params()
    post = v["後街廓_面積單價"]

    p = {k: os.path.join(a.out, n) for k, n in OUT_NAMES.items()}
    write_a4(p["a4"], v["抵充地_m2"])
    r14 = write_a14(p["a14"], owners)
    write_a15(p["a15"])
    r18 = write_a18(p["a18"], lots, zone_of, price)
    r19 = write_a19(p["a19"], post)
    r21 = write_a21(p["a21"], post, zoning)
    r25 = write_a25(p["a25"])
    print(f"附表4 抵充 {v['抵充地_m2']} ㎡；附表14 {len(r14)} 列；附表15 0 列")
    print(f"附表18 {len(r18)} 列（區段 {sorted(set(zone_of.values()))}·{price}）")
    print(f"附表19 {len(r19)} 列；附表21 {len(r21)} 列·Σ面積 {round(sum(x[4] for x in r21), 2)}"
          f"·Σ總價 {round(sum(x[6] for x in r21), 2)}")
    print(f"附表25 {len(r25)} 格")
    for k, f in p.items():
        print(f"輸出 {f}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```
