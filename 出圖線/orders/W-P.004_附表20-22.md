# W-P.004　附表 20、22（附表 23 同式·一張）（照手冊表樣）

- **題**：依 KL 2026-10-27 23:15、23:20 之答（`出圖線/KL答覆/2026-10-27_2315.md`、`2026-10-27_2320.md`），產製附表 20 公共設施用地負擔面積統計表、附表 22 計算負擔總計表（附表 23 為其範例 2，格式相同 ⇒ 一張）。各照手冊之表樣（KL 10/24 02:14、14:55 之通式）。
- **範圍**：唯新增 `plots/burden_tables.py`、`verify/plots/check_W-P004.py`、`verify/plots/mutate_W-P004.py`、`verify/plots/preview_W-P004.py`、`docs/出圖/W-P.004_附表20-22.md`；⛔ 改任何既有之檔（含本線既有之 `plots/prelim_maps.py`、`plots/appx_tables.py` 等·唯 `import` 之）；⛔ 改 `requirements.txt`；⛔ 新套件。
- **授權（逐字）**：
  - KL 2026-10-23 17:31「1. 是　2. 以手冊（拾參）所附的圖例為主」；17:48「…還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」（README 第一節）。
  - KL 2026-10-24 02:14「2. 是，表格改照手冊表樣（乙）」；14:55「是」；2026-10-26 23:14「是，1 甲、2 同意、3 同意」。
  - KL 2026-10-27 23:15「一甲、二甲（請發單端出單時加一條：附表 20 各列「乘（1−C）後再取位」）、三 B（其實實務上正式辦理重劃時，若真的重劃範圍內有未登記土地也會先行辦理登記為中華民國，所以重劃區基本是只會有總登記面積、DXF圖面計算面積，所以屬"係登記與實測之差"）、四甲、五乙（在意「地主依清冊可驗算」，所以選乙，並請發單端在表下加註「一般負擔係數所用之重劃前地價，係以各宗地之圖面面積計」，說明兩數為何不同。）、六乙。」
  - KL 2026-10-27 23:20「1. 甲」（第十項上漲率以表上第五項之重劃前平均地價算）。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`（自 `d4928d4` 前進）；`wip/plots` ＝ `16705506114aa13d67a346eb20173694dd7a23bf`（未含 `20e03bf` ⇒ 工項 1 之合併必做；發單端試併無衝突）。
- **側支**：`verify/W-P.004-burden-tables`（自 `wip/plots` 出）。單號 `W-P.004` 經 `git grep -F` 證未占用為單或分支（主倉 `1670550`、佇列；唯見「移 W-P.004」之預告文字）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具）。

## §一　所據

1. **手冊**（`參考/市地重劃作業手冊.txt`）：
   - 附表 20：第 3077〜3084 列（臨街地特別負擔與一般負擔之兩部分）、第 3085〜3113 列（道路、溝渠在前；備註欄之說明）、第 3292〜3304 列（表樣·編號／名稱／合計面積／臨街地特別負擔面積／一般負擔面積／備註·小計·「製表日期: 年 月 日 承辦: 股長: 科長:」）。
   - 附表 22、23：第 3128〜3214 列（各欄之填法與四式）、第 3336〜3450 列（表樣二範例·左「重劃前情形」一〜五、「各項負擔情形」六、七；右「重劃後情形」八、九、「計算負擔」十〜十三、備註·「承辦 股長 科長 局(處)長 製表日期」）。
2. **資料**（唯讀）：
   - `data/V6.dxf`（cp950）：`BLOCK` 圖層之閉合區塊與其註記「編號-名稱」（G1 公園 7464.6824、RD1〜RD4 道路 1082.2651／1035.9400／959.6692／1604.0013；含四道路註記之聯集區塊 4681.8753 ＝ 四者之和·不列）；`FRONT_LINE` 6 條、`SIDE_LINE` 8 條。
   - `verify/case_params_UC9898.json`：`blocks.*.{正面,左側,右側}.{期望長度_m,期望負擔面積_m2}`（負擔非 0 者 12 邊·和 1053.80）；`財務接線_v3` 之 `重劃區總面積_m2_精確`（34949.888）、`抵充地_m2`／`已徵收公設_m2`（0）、`重劃前平均地價_元每m2`（38498.678…·圖面面積計）、`重劃後平均地價_元每m2`、`中繼錨`（費用總額 150053099 ＝ 工程費＋重劃費＋貸款利息）、`後街廓_面積單價`（Σ 各二位 ＝ 1643176255.06）、`重劃前區段_面積單價`、`原地號_區段`；錨：`斷言錨`（B 0.171043、C 0.091319、總負擔率 0.40712387）、`_斷言錨_身分`（公設 12146.56、特別 957.58、一般 11188.98）。
   - `data/地籍資料來源_匿名版.xlsx` 之 `U_LAND`：面積、「公私別」（第 38 欄·所有權部）、「所有權統一編號」（53 宗·私 31341.00／公 3365.00·無混合；統一編號私 61、公 2）。
3. **既有之函式**（唯讀·`import`）：`plots/prelim_maps.py` 之 `load_cadastre`、`load_price_zones`、`owner_rows`、`_grid`、`_page`、`_blank`、`SourceError`、`C_UID`；`plots/appx_tables.py` 之 `_book`、`_title`、`_sign`、`_center`、`block_key`、`CASE_PARAMS`。
4. **內容之判斷**（皆依手冊、資料或 KL 之答；⛔ 新定）：
   - 附表 20（問一甲）：每一公設區塊一列（編號、名稱取圖上之註記·⛔ 寫死本案之名）；公設區塊 ＝ 編號非「R<數字>」之單一註記區塊；序：名稱含「道路」者在前、餘次之，各依編號（手冊第 3085 列之序）。
   - 臨街地特別負擔之歸屬：每一負擔非 0 之街廓邊，以長度（三位）對 `期望長度_m` 取其線（恰一條），兩側法向外移 0.5 m 取樣 400 點；一側須為該街廓，他側 ≥ 90％ 落於同一公設區塊者歸之（不合即停機）。本案：RD1 ＝ R2 正面＋R1 左側；RD2 ＝ R3、R5 正面＋R1 右側＋R4 左側；RD3 ＝ R6 正面＋R4 右側；RD4 ＝ R2 左、R3 右、R5 左、R6 右。
   - 特別負擔欄（問二甲＋加條）：各列 ＝（Σ 未乘之負擔）×（1−C）**後再取位**（二位）；C ＝ 費用總額 ÷ Σ（街廓面積 × 單價）。本案 212.00／398.87／186.09／160.62／0.00，小計 957.58（先加總再取位則為 957.57 ⇒ 錯）。一般負擔 ＝ 合計（圖面面積二位）− 特別。小計 12146.56／957.58／11188.98 ＝ 錨。
   - 附表 22 第一項（問三 B）：實測 34949.89；私 31341.00、公 3365.00；第 3、4 目 0；備註「3.實測面積較登記面積多 243.89 平方公尺，係登記與實測之差，非未登記地。」（差額由資料算；實測小於登記者停機）。第二項 0（其二目 0）。
   - 第三項（問四甲）：統一編號不重複計：63（私 61、公 2）。第四項與第七項之補助金額：留空。
   - 第五項（問五乙）：Σ（登記面積 × 區段單價〔個位〕）＝ 1,336,204,754 元；÷ 登記面積 34706.00 ＝ 38,500.68。**表下加註**：「註：一般負擔係數所用之重劃前地價，係以各宗地之圖面面積計（總地價 1,344,405,805 元，每平方公尺 38,498.68 元），第五項係依重劃前土地清冊以登記面積計，故二數不同。」（引號內之前句為 KL 逐字；括號內之二數由 `重劃前區段_面積單價` 算出）。
   - 第六項：抄附表 20 之小計（手冊第 3148〜3161 列）。第七項：費用總額 150,053,099。
   - 第八項：總地價 1,643,176,255（至元）、每平方公尺 72,058.61。第九項：34949.888 − 12146.56 ＝ 22,803.33。
   - 第十項（KL 23:20 甲）：表上第八項 ÷ 表上第五項 ＝ 72,058.61 ÷ 38,500.68 ＝ 1.871619。
   - 第十一項：核心線之式與值（一般負擔 × 重劃前平均地價〔圖面面積計〕÷〔重劃後平均地價 ×（實測 − 抵充 − 原位置原面積）〕）＝ 0.171043；第十二項：費用總額 ÷ Σ 街廓總價 ＝ 0.091319（核心線 `C分母形式` 加總形）；各項之下一列列其計算式（照手冊範例）。
   - 第十三項：公設比（公設圖面實值 12146.5579 ÷ 實測精確）34.75％＋費用比 5.96％ ＝ 40.71％；備註 1、2 列二比率之計算式（手冊第 3212 列）。
   - 位數（問六乙）：面積二位、總地價至元、平均地價二位、上漲率與係數六位、比率 0.01％（存值已取位·格式 `#,##0.00`、`#,##0`、`0.000000`、`0.00%`）。
   - 對土地之影響：無（分配結果與兩係數不變）。

## §二　規格

1. **新增 `plots/burden_tables.py`**：逐位元組 ＝ 附錄丁。命令列 `python plots/burden_tables.py --out <倉外之目錄>`，輸出二檔（各一工作表·A4·寬一頁）：
   | 檔 | 表樣之要（行列以 1 起） |
   |---|---|
   | `附表20_公共設施用地負擔面積統計表.xlsx` | 列 1 題（A1:F1）；列 2 六欄之表頭；列 3〜7 RD1〜RD4、G1；列 8「小　計」；列 9 簽欄 |
   | `附表22_計算負擔總計表.xlsx` | 列 1 題（A1:J1）；列 2〜21 二欄組（A〜E 左：大類／項次／項目／值／單位·一〜七；F〜J 右：八〜十三、計算式、備註）；列 22 簽欄；列 23 表下之註 |
2. **新增 `verify/plots/check_W-P004.py`**：逐位元組 ＝ 附錄甲（量測 S0〜S7·獨立於 `plots/`·特別負擔之歸屬以異法〔邊之 1 m 緩衝扣除該街廓後與公設區塊之交集面積最大者〕求之）。
3. **新增 `verify/plots/mutate_W-P004.py`**：逐位元組 ＝ 附錄乙（故意錯誤 Ⓐ〜Ⓕ）。
4. **新增 `verify/plots/preview_W-P004.py`**：逐位元組 ＝ 附錄丙。
5. **新增 `docs/出圖/W-P.004_附表20-22.md`**：逐位元組 ＝ 附錄戊。
6. 發單端之原型（暫存·⛔ 入倉·於 `1670550` 試併 `20e03bf` 之上）已依附錄實作：出表印「附表20 小計 12146.56／957.58／11188.98」「附表22 前 1336204754·38500.68；後 1643176255·72058.61；上漲率 1.871619；B 0.171043；C 0.091319；比率 0.4071（0.3475＋0.0596）；人數 63」；附錄甲 8/8 綠；附錄乙之成果綠、6 種皆紅（Ⓐ S2＋S3、Ⓑ S3＋S5＋S6、Ⓒ S3、Ⓓ S4＋S6、Ⓔ S6、Ⓕ S7）；出表約 20 秒、量測約 21 秒、故意錯誤約 63 秒。預覽見 `出圖線/待KL/W-P.004_第二版原型預覽.png`。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.004-burden-tables`；`git merge --no-edit origin/wip/s1-endpart`（本單出時主線 `20e03bf`·必有合併之 commit）；有衝突即停機。
2. **程式**：§二 1〜5。附錄甲〜戊之取用法：自本單擷取該附錄之開欄（甲〜丁為三個反引號加 `python`；戊為四個反引號加 `markdown`）與其閉欄（同數之反引號）間之文字，末尾一換行；bytes 與 sha256 須合：
   - 甲 `verify/plots/check_W-P004.py`：19684 bytes·`bffd0abda9d7c57e1429dbd77d0088edcca240abb51821fc0e5df7bcc0b5a443`
   - 乙 `verify/plots/mutate_W-P004.py`：4160 bytes·`fdc8af656a9c116e8a1741f6df490790babbdab778b6c1340cbfdea9a444aacb`
   - 丙 `verify/plots/preview_W-P004.py`：2814 bytes·`e04c7ee9d95a23116db5f1d381c48d715c7ef4108b694d2c45aef8587dfc2001`
   - 丁 `plots/burden_tables.py`：23181 bytes·`44991167fb223e54378a7affd44cc17a9363fb63f3ed3c59ef72f4fcbfdf8bf3`
   - 戊 `docs/出圖/W-P.004_附表20-22.md`：4161 bytes·`bcf40008345881cada1b7bbad3d98e2b45eeddebc34e2b3c805b10920f3164b5`
   不合即停機上呈；⛔ 改一字。`python -m py_compile` 四 `.py` 皆過。
3. **量測**：`python plots/burden_tables.py --out <out>`（印 12 列「特別負擔 …」、附表 20 之五列與小計、附表 22 之要值，如 §二 6）；`python verify/plots/check_W-P004.py <out>` ⇒ S0〜S7 共 8 項皆 PASS、結束碼 0。另照舊：`plots/appx_tables.py --out <out3>` ＋ `check_W-P003.py <out3>`（8/8）、`plots/fetch_moedict.py`、`plots/prelim_maps.py --out <out2> --moedict <json>`、`check_W-P001.py`（12/12）、`check_W-P002.py`（8/8·第三參數以 `synth_W-P002a.py` 產之）——證既有之輸出未受擾（主線合併後亦然）。
4. **故意錯誤之測**：`python verify/plots/mutate_W-P004.py <out> <拋棄式之工作目錄>` ⇒ 成果綠；Ⓐ〜Ⓕ 皆紅（所紅之項記之）；結束碼 0。
5. **差異閘**（README 第四節）：`git diff --name-status <實際併入之主線之 sha（應為 20e03bf…）> <側支之端>` 每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status 1670550 <側支之端> -- plots verify/plots docs/出圖` 唯 §二 之五新檔（皆 `A`）；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：`python verify/plots/preview_W-P004.py <out> <PNG 目錄>`，其輸出 `W-P.004_附表20-22.png` 入佇列之 `出圖線/成果/`。
7. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
8. **回報**：`出圖線/reports/W-P.004_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、差異閘與對照組、合併之 sha、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲〜戊之 bytes 或 sha256 不合；或 S0〜S7 於成果不過而非程式之誤。
3. `plots/burden_tables.py` 報 `SourceError`（如某邊之取樣未集中、抵充非 0、實測小於登記、公私別非唯一）——⛔ 自擬填法。
4. 須改任何既有之檔、或須新套件。
5. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P004.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.004：附表 20、22（23 同式）之量測。
獨立於 plots/：⛔ import 之；期望取自倉內原始資料（data/V6.dxf、data/地籍資料來源_匿名版.xlsx、
verify/case_params_UC9898.json）、手冊（參考/市地重劃作業手冊.txt 第 3077〜3200、3292〜3304、3336〜3450 列）、
KL 之錨（case_params 之 斷言錨 與 _斷言錨_身分）與 KL 2026-10-27 23:15、23:20 之答。

命令列：python verify/plots/check_W-P004.py <成果目錄>
  成果目錄 ＝ plots/burden_tables.py --out 之目錄。
任一不過 ⇒ 結束碼 1。
S0 二檔皆在、可讀；S1 附表 20 之表樣；S2 附表 20 之列（區塊、合計面積、合計＝特別＋一般）；
S3 附表 20 之臨街地特別負擔（歸屬、各列乘 1−C 後取位、小計＝錨）；S4 附表 22 第一〜五項；
S5 附表 22 第六〜九項；S6 附表 22 第十〜十三項；S7 附表 22 之備註、簽欄與表下之註。
"""
import io
import json
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DXF = os.path.join(REPO, "data", "V6.dxf")
XLSX_SRC = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
CASE = os.path.join(REPO, "verify", "case_params_UC9898.json")
SECTION_NAME = "0013德安段"
FILES = {20: "附表20_公共設施用地負擔面積統計表.xlsx", 22: "附表22_計算負擔總計表.xlsx"}

# KL 之錨（case_params 之 _斷言錨_身分：KL Tab7 C 值明細／Step H 截圖；斷言錨）
ANCHOR_A20 = (Decimal("12146.56"), Decimal("957.58"), Decimal("11188.98"))
ANCHOR_B, ANCHOR_C, ANCHOR_RATE = Decimal("0.171043"), Decimal("0.091319"), Decimal("0.40712387")
# KL 2026-10-27 23:15 問五乙（監看窗之讀第 5 點）、23:20 甲；問四甲（私有 61、公有 2）
ANCHOR_PRE = (Decimal("1336204754"), Decimal("38500.68"))
ANCHOR_RISE = Decimal("1.871619")
ANCHOR_OWNERS = (61, 2)
ANCHOR_MAP_PRE = (Decimal("1344405805"), Decimal("38498.68"))   # 圖面面積計之重劃前總地價與平均地價

A20_TITLE = "○○縣(市)第○○期○○○○市地重劃區公共設施用地負擔面積統計表"
A20_HEAD = ["編號", "名稱", "合計面積（平方公尺）", "臨街地特別負擔面積（平方公尺）", "一般負擔面積（平方公尺）", "備註"]
A20_SIGN = ["製表日期:　年　月　日", "承辦:", "股長:", "科長:"]
A22_TITLE = "○○縣(市)第○期○○○○市地重劃區計算負擔總計表"
A22_SIGN = ["承辦", "股長", "科長", "局(處)長", "製表日期:　年　月　日"]
NOTE_KL = "一般負擔係數所用之重劃前地價，係以各宗地之圖面面積計"
FACES = ("正面", "左側", "右側")


def _blank(v):
    return v is None or (isinstance(v, str) and v.strip() in ("", "null"))


def D(x):
    return Decimal(repr(x)) if isinstance(x, float) else Decimal(str(x))


def rhu(x, nd):
    return D(x).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


def _ws(out, n):
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(out, FILES[n]))
    if len(wb.worksheets) != 1:
        raise AssertionError(f"附表 {n} 之工作表數 {len(wb.worksheets)}≠1")
    return wb.worksheets[0]


def _last(ws):
    last = 0
    for row in ws.iter_rows():
        for c in row:
            if not _blank(c.value):
                last = max(last, c.row)
    return last


def _nonblank(ws, r):
    return [ws.cell(r, c).value for c in range(1, ws.max_column + 1) if not _blank(ws.cell(r, c).value)]


# ---------------------------------------------------------------- 獨立之讀
def src_dxf():
    """⇒ 公設區塊 {編號: (名稱, Polygon)}、街廓 {編號: Polygon}、{圖層: [LineString]}。"""
    import ezdxf
    from shapely.geometry import LineString, Point, Polygon
    with open(DXF, "rb") as f:
        msp = ezdxf.read(io.TextIOWrapper(f, encoding="cp950", newline=None)).modelspace()
    polys = [Polygon([(v.dxf.location.x, v.dxf.location.y) for v in e.vertices])
             for e in msp.query('POLYLINE[layer=="BLOCK"]')]
    polys += [Polygon(list(e.get_points("xy"))) for e in msp.query('LWPOLYLINE[layer=="BLOCK"]')]
    texts = [(e.dxf.text.strip(), Point(e.dxf.insert.x, e.dxf.insert.y)) for e in msp.query('TEXT[layer=="BLOCK"]')]
    pub, lot = {}, {}
    for p in polys:
        labs = [t for t, pt in texts if p.contains(pt)]
        if len(labs) != 1:
            continue
        no, name = labs[0].split("-", 1)
        if re.match(r"^R\d+$", no):
            lot[no] = p
        else:
            pub[no] = (name, p)
    lines = {lay: [LineString([(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)])
                   for e in msp.query(f'LINE[layer=="{lay}"]')] for lay in ("FRONT_LINE", "SIDE_LINE")}
    return pub, lot, lines


def src_case():
    d = json.load(open(CASE, encoding="utf-8"))
    return d["blocks"], d["財務接線_v3"]


def src_ledger():
    """⇒ {地號: (面積, 公私別, {統一編號})}（U_LAND·德安段·「重劃區地籍」之 53 宗）。"""
    import openpyxl
    wb = openpyxl.load_workbook(XLSX_SRC, read_only=True)
    rows = list(wb["重劃區地籍"].iter_rows(values_only=True))
    il = rows[0].index("地號")
    lots = {str(r[il]).strip() for r in rows[1:] if not _blank(r[il])}
    out, head = {}, None
    for r in wb["U_LAND"].iter_rows(values_only=True):
        if head is None:
            head = list(r)
            ia, ipp, iu = head.index("面積"), head.index("公私別"), head.index("所有權統一編號")
            continue
        if r[0] != SECTION_NAME or _blank(r[1]):
            continue
        m, s = divmod(int(r[1]), 10000)
        ln = f"{m}" if s == 0 else f"{m}-{s}"
        if ln not in lots:
            continue
        a, pp, u = out.get(ln, (D(r[ia]), r[ipp], set()))
        if a != D(r[ia]) or pp != r[ipp]:
            raise AssertionError(f"{ln} 之面積或公私別不一")
        u.add(str(r[iu]).strip())
        out[ln] = (a, pp, u)
    if set(out) != lots:
        raise AssertionError(f"U_LAND 缺宗：{sorted(lots - set(out))}")
    return out


def _post_total(v):
    return sum(rhu(D(x["面積_m2"]) * D(x["單價_元每m2"]), 2) for x in v["後街廓_面積單價"].values())


def _cost(v):
    m = v["中繼錨"]
    return Decimal(int(m["工程費_元"]) + int(m["重劃費_元"]) + int(v["貸款利息_元"]))


def expect_a20(pub, lot, lines, blocks, v):
    """⇒ [(編號, 名稱, 合計, 特別, 一般)]（期望之序：道路在前、各依編號）、{編號: 未乘之特別負擔}、公設圖面面積之和。
    特別負擔之歸屬（與 plots/ 異法）：街廓邊之 1 m 緩衝區扣除該街廓後，與各公設區塊之交集面積最大者。"""
    raw = {k: Decimal(0) for k in pub}
    for b in blocks:
        for face in FACES:
            f = blocks[b][face]
            if D(f["期望負擔面積_m2"]) == 0:
                continue
            lay = "FRONT_LINE" if face == "正面" else "SIDE_LINE"
            hit = [ln for ln in lines[lay] if abs(ln.length - f["期望長度_m"]) < 5e-4]
            if len(hit) != 1:
                raise AssertionError(f"{b}.{face} 之線 {len(hit)} 條")
            zone = hit[0].buffer(1.0).difference(lot[b])
            road = max(pub, key=lambda k: zone.intersection(pub[k][1]).area)
            raw[road] += D(f["期望負擔面積_m2"])
    omc = 1 - _cost(v) / _post_total(v)

    def order(k):
        m = re.match(r"^(\D*)(\d*)$", k)
        return (0 if "道路" in pub[k][0] else 1, m.group(1), int(m.group(2) or 0))
    rows = []
    for k in sorted(pub, key=order):
        t = rhu(pub[k][1].area, 2)
        sp = rhu(raw[k] * omc, 2)
        rows.append((k, pub[k][0], t, sp, t - sp))
    return rows, raw, sum(D(pub[k][1].area) for k in pub)


# ---------------------------------------------------------------- 量測
def s0(out):
    import openpyxl
    for f in FILES.values():
        p = os.path.join(out, f)
        if not os.path.isfile(p) or os.path.getsize(p) == 0:
            return False, f"缺或空：{f}"
        if _last(openpyxl.load_workbook(p).worksheets[0]) == 0:
            return False, f"無內容：{f}"
    return True, "二檔皆在、可讀、非空"


def _a20_body(ws):
    r, rows = 3, []
    while ws.cell(r, 2).value != "小　計":
        if r > 200:
            raise AssertionError("無小計之列")
        rows.append([ws.cell(r, c).value for c in range(1, 7)])
        r += 1
    return rows, r


def s1(out):
    ws = _ws(out, 20)
    if ws.cell(1, 1).value != A20_TITLE or "A1:F1" not in {str(m) for m in ws.merged_cells.ranges}:
        return False, f"題：{ws.cell(1, 1).value!r}"
    if [ws.cell(2, c).value for c in range(1, 7)] != A20_HEAD:
        return False, f"表頭：{[ws.cell(2, c).value for c in range(1, 7)]}"
    rows, rs = _a20_body(ws)
    if _nonblank(ws, rs + 1) != A20_SIGN or _last(ws) != rs + 1:
        return False, f"簽欄（列 {rs + 1}）：{_nonblank(ws, rs + 1)}"
    for r in range(3, rs + 1):
        for c in (3, 4, 5):
            if ws.cell(r, c).number_format != "#,##0.00":
                return False, f"列 {r} 欄 {c} 之格式 {ws.cell(r, c).number_format}"
    return True, f"題、表頭 6 欄、{len(rows)} 列、小計列 {rs}、簽欄、面積二位"


def s2(out, exp):
    ws = _ws(out, 20)
    rows, _ = _a20_body(ws)
    got = [(r[0], r[1], rhu(r[2], 2)) for r in rows]
    want = [(e[0], e[1], e[2]) for e in exp]
    if got != want:
        return False, f"列：{got} ≠ {want}"
    for r in rows:
        if rhu(r[2], 2) != rhu(r[3], 2) + rhu(r[4], 2) or not _blank(r[5]):
            return False, f"{r[0]}：合計≠特別＋一般 或備註有值 {r}"
    return True, f"{len(rows)} 列＝圖上之公設區塊（{'、'.join(g[0] for g in got)}）、合計面積＝圖面面積二位、合計＝特別＋一般"


def s3(out, exp, raw):
    ws = _ws(out, 20)
    rows, rs = _a20_body(ws)
    got = [rhu(r[3], 2) for r in rows]
    want = [e[3] for e in exp]
    if got != want:
        return False, f"特別負擔：{got} ≠ {want}（未乘 {[raw[e[0]] for e in exp]}）"
    sub = tuple(rhu(ws.cell(rs, c).value, 2) for c in (3, 4, 5))
    if sub != ANCHOR_A20 or sub != tuple(sum(rhu(r[c], 2) for r in rows) for c in (2, 3, 4)):
        return False, f"小計 {sub} ≠ 錨 {ANCHOR_A20} 或 ≠ 各列之和"
    if sum(raw.values()) != Decimal("1053.80"):
        return False, f"未乘之和 {sum(raw.values())}"
    return True, f"特別負擔 {'、'.join(str(x) for x in got)}（未乘之和 1053.80）；小計 {sub[0]}／{sub[1]}／{sub[2]}＝錨"


def _find(ws, lab, col):
    rs = [r for r in range(1, ws.max_row + 1) if ws.cell(r, col).value == lab]
    if len(rs) != 1:
        raise AssertionError(f"「{lab}」於欄 {col} 之列數 {len(rs)}")
    return rs[0]


def _val(ws, lab, col, nf=None):
    r = _find(ws, lab, col)
    c = ws.cell(r, col + 1)
    if nf is not None and c.number_format != nf:
        raise AssertionError(f"「{lab}」之格式 {c.number_format}≠{nf}")
    return c.value


def s4(out, ledger, v):
    ws = _ws(out, 22)
    if ws.cell(1, 1).value != A22_TITLE:
        return False, f"題：{ws.cell(1, 1).value!r}"
    priv = sum(a for a, pp, _ in ledger.values() if pp == "私")
    pub = sum(a for a, pp, _ in ledger.values() if pp == "公")
    exact = D(v["重劃區總面積_m2_精確"])
    A = "#,##0.00"
    want = [("重劃區實測面積", rhu(exact, 2)), ("1.私有土地面積", rhu(priv, 2)), ("2.公有土地面積", rhu(pub, 2)),
            ("3.未登記土地面積", Decimal(0)), ("4.實測誤差面積", Decimal(0)),
            ("原公有道路溝渠河川及未登記等土地抵充面積", Decimal(0))]
    for lab, w in want:
        g = _val(ws, lab, 3, A)
        if rhu(g, 2) != w:
            return False, f"「{lab}」{g} ≠ {w}"
    r = _find(ws, "原公有道路溝渠河川及未登記等土地抵充面積", 3)
    if [rhu(ws.cell(r + i, 4).value, 2) for i in (1, 2)] != [0, 0]:
        return False, "抵充之二目非 0"
    up = {u for _, pp, us in ledger.values() if pp == "私" for u in us}
    uq = {u for _, pp, us in ledger.values() if pp == "公" for u in us}
    n = (len(up), len(uq))
    if n != ANCHOR_OWNERS or up & uq:
        return False, f"人數 {n} ≠ 錨 {ANCHOR_OWNERS}"
    if [_val(ws, "重劃區土地所有權人數", 3), _val(ws, "1.私有：", 3), _val(ws, "2.公有：", 3)] != [sum(n), n[0], n[1]]:
        return False, "人數之格"
    r4 = _find(ws, "私有土地所有權人申請（同意）辦理重劃情形　人數：", 3)
    if not _blank(ws.cell(r4, 4).value) or not _blank(ws.cell(r4 + 1, 4).value):
        return False, "第四項有值（資料所無·須留空）"
    zone = v["原地號_區段"]
    price = {z: rhu(d["單價_元每m2"], 0) for z, d in v["重劃前區段_面積單價"].items()}
    tot = sum(a * price[zone[ln]] for ln, (a, _, _) in ledger.items())
    avg = rhu(tot / (priv + pub), 2)
    g_tot = _val(ws, "評定之重劃前平均地價及總地價　總地價：", 3, "#,##0")
    g_avg = _val(ws, "每平方公尺地價：", 3, "#,##0.00")
    if (rhu(tot, 0), avg) != ANCHOR_PRE or (rhu(g_tot, 0), rhu(g_avg, 2)) != ANCHOR_PRE:
        return False, f"第五項 {g_tot}／{g_avg}；期 {rhu(tot, 0)}／{avg}；錨 {ANCHOR_PRE}"
    return True, (f"實測 {rhu(exact, 2)}、私 {rhu(priv, 2)}、公 {rhu(pub, 2)}、未登記與誤差 0、抵充 0；"
                  f"人數 {sum(n)}（{n[0]}＋{n[1]}）；第四項空；第五項 {ANCHOR_PRE[0]}／{ANCHOR_PRE[1]}")


def s5(out, exp, v):
    ws = _ws(out, 22)
    sub = tuple(sum(e[i] for e in exp) for i in (2, 3, 4))
    A = "#,##0.00"
    got = (rhu(_val(ws, "公共設施用地扣除原公有道路溝渠河川及未登記土地等抵充土地後共同負擔總面積", 3, A), 2),
           rhu(_val(ws, "1.臨街地特別負擔×(1-C)", 3, A), 2), rhu(_val(ws, "2.一般負擔", 3, A), 2))
    if got != sub or got != ANCHOR_A20:
        return False, f"第六項 {got} ≠ 附表 20 之小計 {sub}／錨"
    cost = _cost(v)
    if D(_val(ws, "費用負擔總額：1.費用總額", 3, "#,##0")) != cost or cost != Decimal(150053099):
        return False, f"費用 {cost}"
    if not _blank(ws.cell(_find(ws, "2.補助金額", 3), 4).value):
        return False, "補助金額有值（資料所無·須留空）"
    pt = _post_total(v)
    g = (rhu(_val(ws, "評定之重劃後平均地價及總地價　總地價：", 8, "#,##0"), 0), rhu(_val(ws, "每平方公尺地價：", 8, A), 2))
    if g != (rhu(pt, 0), rhu(v["重劃後平均地價_元每m2"], 2)) or pt != Decimal("1643176255.06"):
        return False, f"第八項 {g}（Σ {pt}）"
    alloc = rhu(D(v["重劃區總面積_m2_精確"]) - sub[0], 2)
    if rhu(_val(ws, "重劃後可分配土地面積", 8, A), 2) != alloc or alloc != Decimal("22803.33"):
        return False, f"第九項 ≠ {alloc}"
    return True, f"第六項＝附表 20 小計＝錨；費用 {cost}、補助空；第八項 {g[0]}／{g[1]}；第九項 {alloc}"


def s6(out, v, exp, pub_dxf):
    ws = _ws(out, 22)
    K = "0.000000"
    pre = rhu(_val(ws, "每平方公尺地價：", 3), 2)
    post = rhu(_val(ws, "每平方公尺地價：", 8), 2)
    rise = rhu(_val(ws, "重劃前後每平方公尺平均地價上漲率：", 8, K), 6)
    if rise != rhu(post / pre, 6) or rise != ANCHOR_RISE:
        return False, f"上漲率 {rise}（期 {rhu(post / pre, 6)}·錨 {ANCHOR_RISE}）"
    exact = D(v["重劃區總面積_m2_精確"])
    gen = sum(e[4] for e in exp)
    post_full = D(v["重劃後平均地價_元每m2"])
    b = rhu(gen * D(v["重劃前平均地價_元每m2"]) / (post_full * exact), 6)
    c = rhu(_cost(v) / _post_total(v), 6)
    gb = rhu(_val(ws, "公共設施用地一般負擔係數：", 8, K), 6)
    gc = rhu(_val(ws, "費用負擔係數：", 8, K), 6)
    if (gb, gc) != (b, c) or (b, c) != (ANCHOR_B, ANCHOR_C):
        return False, f"B／C {gb}／{gc}（期 {b}／{c}·錨 {ANCHOR_B}／{ANCHOR_C}）"
    r1, r2 = pub_dxf / exact, _cost(v) / (post_full * exact)
    want = (rhu(ANCHOR_RATE, 4), rhu(r1, 4), rhu(r2, 4))
    P = "0.00%"
    got = (rhu(_val(ws, "平均負擔比率：", 8, P), 4), rhu(_val(ws, "1.公共設施用地負擔比率：", 8, P), 4),
           rhu(_val(ws, "2.費用負擔比率：", 8, P), 4))
    if got != want or rhu(r1 + r2, 8) != ANCHOR_RATE:
        return False, f"比率 {got} ≠ {want}（r1+r2 {rhu(r1 + r2, 8)}）"
    return True, f"上漲率 {rise}＝{post}÷{pre}；B {gb}、C {gc}＝錨；比率 {got[0]}＝{got[1]}＋{got[2]}；格式六位與 0.00%"


def s7(out, v, ledger):
    ws = _ws(out, 22)
    texts = [str(ws.cell(r, c).value) for r in range(1, ws.max_row + 1) for c in range(1, ws.max_column + 1)
             if not _blank(ws.cell(r, c).value)]
    diff = rhu(D(v["重劃區總面積_m2_精確"]) - sum(a for a, _, _ in ledger.values()), 2)
    need = [f"實測面積較登記面積多 {diff:,.2f} 平方公尺，係登記與實測之差，非未登記地",
            "1.公共設施用地負擔比率", "2.費用負擔比率", "備註"]
    miss = [t for t in need if not any(t in x for x in texts)]
    if miss or diff != Decimal("243.89"):
        return False, f"備註缺：{miss}（差 {diff}）"
    last = _last(ws)
    note = ws.cell(last, 1).value or ""
    if not note.startswith("註：" + NOTE_KL) or f"{ANCHOR_MAP_PRE[0]:,}" not in note or f"{ANCHOR_MAP_PRE[1]:,}" not in note:
        return False, f"表下之註：{note!r}"
    if _nonblank(ws, last - 1) != A22_SIGN:
        return False, f"簽欄：{_nonblank(ws, last - 1)}"
    zt = sum(D(z["面積_m2"]) * D(z["單價_元每m2"]) for z in v["重劃前區段_面積單價"].values())
    za = sum(D(z["面積_m2"]) for z in v["重劃前區段_面積單價"].values())
    if (rhu(zt, 0), rhu(zt / za, 2)) != ANCHOR_MAP_PRE:
        return False, f"圖面之重劃前地價 {rhu(zt, 0)}／{rhu(zt / za, 2)}"
    return True, f"備註（二比率之式、差額 {diff}）、簽欄、表下之註（KL 逐字·{ANCHOR_MAP_PRE[0]:,}／{ANCHOR_MAP_PRE[1]:,}）"


def run(out, src=None, quiet=False):
    """⇒ 不過之項名之列。src ＝ load_src() 之值（省略者即讀之）。"""
    exp, raw, pub_dxf, ledger, v = load_src() if src is None else src
    tests = [
        ("S0", lambda: s0(out)),
        ("S1", lambda: s1(out)),
        ("S2", lambda: s2(out, exp)),
        ("S3", lambda: s3(out, exp, raw)),
        ("S4", lambda: s4(out, ledger, v)),
        ("S5", lambda: s5(out, exp, v)),
        ("S6", lambda: s6(out, v, exp, pub_dxf)),
        ("S7", lambda: s7(out, v, ledger)),
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


def load_src():
    pub, lot, lines = src_dxf()
    blocks, v = src_case()
    exp, raw, pub_dxf = expect_a20(pub, lot, lines, blocks, v)
    return exp, raw, pub_dxf, src_ledger(), v


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

## 附錄乙　`verify/plots/mutate_W-P004.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.004 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓕ 共 6 種變異體須各紅（量測 ＝ check_W-P004.py 之 8 項）。

命令列：python verify/plots/mutate_W-P004.py <成果目錄> <拋棄式之工作目錄>
  成果目錄 ＝ plots/burden_tables.py --out 之目錄（⛔ 改之；變異體皆寫於工作目錄）。
  Ⓑ、Ⓓ 掛換 plots/ 之函式後重出（於本行程之記憶體中·⛔ 改檔）；他者改成果之複本。
結束碼：成果綠且 6 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P004", os.path.join(HERE, "check_W-P004.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)


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
    import burden_tables
    return burden_tables


def _regen(d, obj, attr, val):
    orig = getattr(obj, attr)
    setattr(obj, attr, val)
    try:
        if os.path.exists(d):
            shutil.rmtree(d)
        _plots().main(["--out", d])
    finally:
        setattr(obj, attr, orig)


def mA_drop_block(d):
    p, wb = _book(d, 20)
    ws = wb.worksheets[0]
    r = chk._find(ws, "G1", 1)
    ws.delete_rows(r)
    wb.save(p)


def mB_no_one_minus_c(d):
    bt = _plots()
    orig = bt.a20_rows

    def rows(pub, raw, one_minus_c):
        return orig(pub, raw, 1)
    _regen(d, bt, "a20_rows", rows)


def mC_round_after_sum(d):
    """小計之特別負擔改為「未乘之和 ×（1−C）再取位」（957.57），一般負擔隨之（11188.99）。"""
    p, wb = _book(d, 20)
    ws = wb.worksheets[0]
    r = chk._find(ws, "小　計", 2)
    ws.cell(r, 4, 957.57)
    ws.cell(r, 5, 11188.99)
    wb.save(p)


def mD_map_area_pre_price(d):
    """第五項改用圖面面積計之總地價與平均地價（問五 甲）。"""
    bt = _plots()
    orig = bt.a22_values

    def vals(v, reg_area, n_owner, pre_total, sub20):
        x = orig(v, reg_area, n_owner, pre_total, sub20)
        x["前總"], x["前均"] = x["_前總圖面"], x["_前均圖面"]
        return x
    _regen(d, bt, "a22_values", vals)


def mE_core_rise(d):
    """上漲率改用核心線之重劃前平均地價（÷ 38,498.68 ＝ 1.871716·KL 23:20 之乙）。"""
    p, wb = _book(d, 22)
    ws = wb.worksheets[0]
    r = chk._find(ws, "重劃前後每平方公尺平均地價上漲率：", 8)
    ws.cell(r, 9, 1.871716)
    wb.save(p)


def mF_drop_note(d):
    p, wb = _book(d, 22)
    ws = wb.worksheets[0]
    ws.cell(chk._last(ws), 1).value = None
    wb.save(p)


MUTANTS = [
    ("Ⓐ 附表 20 漏一區塊", mA_drop_block, True),
    ("Ⓑ 臨街地特別負擔未乘（1−C）", mB_no_one_minus_c, False),
    ("Ⓒ 特別負擔先加總後取位", mC_round_after_sum, True),
    ("Ⓓ 第五項用圖面面積之總地價", mD_map_area_pre_price, False),
    ("Ⓔ 上漲率用核心線之重劃前平均地價", mE_core_rise, True),
    ("Ⓕ 漏表下之註", mF_drop_note, True),
]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print(__doc__)
        return 2
    out, work = argv
    src = chk.load_src()
    base = chk.run(out, src, quiet=True)
    print(f"成果：{'綠' if not base else '紅 ' + str(base)}")
    ok = not base
    for i, (name, fn, from_copy) in enumerate(MUTANTS):
        d = os.path.join(work, f"m{i}")
        if from_copy:
            _copy(out, d)
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

## 附錄丙　`verify/plots/preview_W-P004.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.004 之預覽 PNG（單 §三 6）：附表 20、22 之截取。

命令列：python verify/plots/preview_W-P004.py <成果目錄> <PNG 之輸出目錄>
輸出：W-P.004_附表20-22.png
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

OUT_NAME = "W-P.004_附表20-22.png"
PANELS = [
    ("附表20_公共設施用地負擔面積統計表.xlsx", "附表 20　公共設施用地負擔面積統計表"),
    ("附表22_計算負擔總計表.xlsx", "附表 22（附表 23 同式）　計算負擔總計表"),
]


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
        if nf == "0.000000":
            return f"{v:.6f}"
        if nf == "0.00%":
            return f"{v * 100:.2f}%"
    return str(v)


def draw(ax, path, title, widths, note=False):
    import openpyxl
    ws = openpyxl.load_workbook(path).worksheets[0]
    last = ws.max_row - 1 if note else ws.max_row
    cells = [[_fmt(ws.cell(r, c)) for c in range(1, ws.max_column + 1)] for r in range(2, last + 1)]
    ax.axis("off")
    ax.set_title(f"{title}　｜　{ws['A1'].value}", fontsize=13, loc="left")
    t = ax.table(cellText=cells, loc="upper left", cellLoc="left", colWidths=widths)
    t.auto_set_font_size(False)
    t.set_fontsize(8)
    t.scale(1, 1.4)
    if note:
        ax.text(0, 0.02, str(ws.cell(ws.max_row, 1).value), fontsize=10, transform=ax.transAxes)


def main(argv):
    src, out = argv
    os.makedirs(out, exist_ok=True)
    p = os.path.join(out, OUT_NAME)
    fig = plt.figure(figsize=(26, 18))
    gs = fig.add_gridspec(2, 1, height_ratios=[0.45, 1.3])
    draw(fig.add_subplot(gs[0]), os.path.join(src, PANELS[0][0]), PANELS[0][1], [0.08, 0.08, 0.16, 0.2, 0.16, 0.12])
    draw(fig.add_subplot(gs[1]), os.path.join(src, PANELS[1][0]), PANELS[1][1],
         [0.05, 0.03, 0.27, 0.07, 0.07, 0.04, 0.03, 0.3, 0.07, 0.04], note=True)
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

## 附錄丁　`plots/burden_tables.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.004　附表 20 公共設施用地負擔面積統計表、附表 22 計算負擔總計表（附表 23 為其範例 2·同式·一張）。
照手冊表樣（KL 2026-10-24 02:14／14:55）；填法依 KL 2026-10-27 23:15、23:20。

命令列：python plots/burden_tables.py --out <目錄>
輸出（皆寫至 --out，⛔ 入倉）：見 OUT_NAMES。
所據：出圖線/orders/W-P.004_附表20-22.md（§一、§二）。
  附表 20：使用者圖（data/V6.dxf）之 BLOCK 圖層，每一公共設施區塊一列（編號、名稱取其註記「編號-名稱」；
    道路在前、餘次之，各依編號）；合計面積 ＝ 區塊之圖面面積；臨街地特別負擔 ＝ 臨接該區塊之街廓邊之負擔面積
    （verify/case_params_UC9898.json 之 blocks.*.{正面,左側,右側}.期望負擔面積_m2）之和 ×（1−C），各列乘後再取位
    （KL 23:15 問二）；一般負擔 ＝ 合計 − 特別。
  附表 22：一 實測面積（財務接線_v3.重劃區總面積_m2_精確）、私有與公有之登記面積（U_LAND「公私別」）、
    未登記與實測誤差填 0（KL 23:15 問三 B·差額記於備註）；二 抵充 0；三 所有權人數（同一統一編號計一人·問四）；
    四 留空；五 Σ（登記面積 × 區段單價〔個位〕）÷ 登記面積和（問五 乙）；六 抄附表 20 之小計；七 費用總額；
    八 Σ（街廓面積 × 單價）、平均地價；九 實測面積 − 公設合計；十 第八項 ÷ 第五項（表上之數·KL 23:20）；
    十一 一般負擔係數（核心線之式·重劃前平均地價以圖面面積計）；十二 費用負擔係數（加總形）；十三 平均負擔比率。
    位數（問六 乙）：面積二位、總地價至元、平均地價二位、上漲率與係數六位、比率 0.01％。
缺值或與單之所據不符一律報錯停止（⛔ 靜默補值）；匯入資料所無之欄留空（⛔ 杜撰）。
"""
import argparse
import io
import json
import math
import os
import re
import sys
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （讀取與表樣之共用函式·W-P.001／002）
import appx_tables as AT  # noqa: E402  （表樣之共用函式·W-P.003）

DXF_BLOCK = os.path.join(REPO, "data", "V6.dxf")
DXF_ENCODING = "cp950"
LAYER_BLOCK, LAYER_FRONT, LAYER_SIDE = "BLOCK", "FRONT_LINE", "SIDE_LINE"
FACE_LAYER = {"正面": LAYER_FRONT, "左側": LAYER_SIDE, "右側": LAYER_SIDE}
LOT_RE = re.compile(r"^R\d+$")      # 可分配之街廓（app parse_block_dxf 之慣例「R<數字>」）
ROAD_WORD = "道路"                  # 手冊第 3085 列：道路、溝渠在前
OFFSET_M = 0.5                      # 街廓邊向外取樣之距
SAMPLES = 400
MIN_SHARE = Decimal("0.9")          # 一邊之取樣落於同一公設區塊之最低比例
UNION_TOL = 0.01                    # 聯集區塊之面積 ＝ 其成員之和之容差（㎡）
C_PUBPRIV = 38                      # U_LAND「公私別」（所有權部）
TITLE_A20 = "○○縣(市)第○○期○○○○市地重劃區公共設施用地負擔面積統計表"
TITLE_A22 = "○○縣(市)第○期○○○○市地重劃區計算負擔總計表"
A20_HEAD = ("編號", "名稱", "合計面積（平方公尺）", "臨街地特別負擔面積（平方公尺）", "一般負擔面積（平方公尺）", "備註")
SIGN_A20 = ("製表日期:　年　月　日", "承辦:", "股長:", "科長:")
SIGN_A22 = ("承辦", "股長", "科長", "局(處)長", "製表日期:　年　月　日")
NOTE_PRE_PRICE = "一般負擔係數所用之重劃前地價，係以各宗地之圖面面積計"   # KL 23:15 問五（逐字）

OUT_NAMES = {
    "a20": "附表20_公共設施用地負擔面積統計表.xlsx",
    "a22": "附表22_計算負擔總計表.xlsx",
}


def dec(x):
    if isinstance(x, Decimal):
        return x
    if isinstance(x, float):
        return Decimal(repr(x))
    return Decimal(str(x))


def q(x, nd):
    return dec(x).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------- 讀取
def load_dxf(path=DXF_BLOCK):
    import ezdxf
    with open(path, "rb") as f:
        doc = ezdxf.read(io.TextIOWrapper(f, encoding=DXF_ENCODING, newline=None))
    return doc.modelspace()


def _ring(e):
    if e.dxftype() == "LWPOLYLINE":
        return [(p[0], p[1]) for p in e.get_points("xy")], e.closed
    return [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices], e.is_closed


def load_blocks(msp):
    """⇒ {編號: (名稱, Polygon)}（唯單一註記之區塊）。聯集之區塊（含二以上之註記）須 ＝ 其成員之和。"""
    from shapely.geometry import Point, Polygon
    polys = []
    for e in msp.query(f'LWPOLYLINE POLYLINE[layer=="{LAYER_BLOCK}"]'):
        pts, closed = _ring(e)
        if not closed:
            raise PM.SourceError(f"{LAYER_BLOCK} 有未閉合之線（{len(pts)} 點）")
        polys.append(Polygon(pts))
    texts = []
    for e in msp.query(f'TEXT MTEXT[layer=="{LAYER_BLOCK}"]'):
        t = e.plain_text() if e.dxftype() == "MTEXT" else e.dxf.text
        texts.append((t.strip(), Point(e.dxf.insert.x, e.dxf.insert.y)))
    single, unions = {}, []
    for p in polys:
        labs = [t for t, pt in texts if p.contains(pt)]
        if not labs:
            raise PM.SourceError(f"{LAYER_BLOCK} 有無註記之區塊（面積 {p.area:.4f}）")
        if len(labs) > 1:
            unions.append((labs, p))
            continue
        if "-" not in labs[0]:
            raise PM.SourceError(f"區塊之註記非「編號-名稱」：{labs[0]!r}")
        no, name = labs[0].split("-", 1)
        if no in single:
            raise PM.SourceError(f"區塊之編號重複：{no}")
        single[no] = (name, p)
    for labs, p in unions:
        nos = [t.split("-", 1)[0] for t in labs]
        if any(n not in single for n in nos):
            raise PM.SourceError(f"聯集區塊之成員無單獨之區塊：{labs}")
        s = sum(single[n][1].area for n in nos)
        if abs(s - p.area) > UNION_TOL:
            raise PM.SourceError(f"聯集區塊 {nos} 之面積 {p.area:.4f} ≠ 成員之和 {s:.4f}")
    return single


def public_blocks(blocks):
    pub = {k: v for k, v in blocks.items() if not LOT_RE.match(k)}
    if not pub:
        raise PM.SourceError("圖上無公共設施之區塊")
    return pub


def block_order(no, name):
    m = re.match(r"^(\D*)(\d*)$", no)
    pre, num = (m.group(1), int(m.group(2)) if m.group(2) else 0) if m else (no, 0)
    return (0 if ROAD_WORD in name else 1, pre, num, no)


def load_case(path=AT.CASE_PARAMS):
    d = json.load(open(path, encoding="utf-8"))
    v = d["財務接線_v3"]
    for k in ("重劃區總面積_m2_精確", "抵充地_m2", "已徵收公設_m2", "重劃前平均地價_元每m2", "重劃後平均地價_元每m2",
              "貸款利息_元", "中繼錨", "後街廓_面積單價", "重劃前區段_面積單價"):
        if k not in v:
            raise PM.SourceError(f"case_params 之 財務接線_v3 缺 {k}")
    return d["blocks"], v


def cost_total(v):
    m = v["中繼錨"]
    s = int(m["工程費_元"]) + int(m["重劃費_元"]) + int(v["貸款利息_元"])
    if s != int(m["費用總額_元"]):
        raise PM.SourceError(f"費用總額 {m['費用總額_元']} ≠ 工程費＋重劃費＋利息 {s}")
    return s


def post_total(v):
    """Σ（街廓面積 × 單價·各二位四捨五入）＝ 附表 21 之總價之和（W-P.003）。"""
    t = Decimal(0)
    for b, x in v["後街廓_面積單價"].items():
        if PM._blank(x.get("面積_m2")) or PM._blank(x.get("單價_元每m2")):
            raise PM.SourceError(f"後街廓 {b} 之面積或單價為空")
        t += q(dec(x["面積_m2"]) * dec(x["單價_元每m2"]), 2)
    return t


# ---------------------------------------------------------------- 臨街地特別負擔之歸屬
def _locate(blocks, x, y):
    from shapely.geometry import Point
    pt = Point(x, y)
    for no, (_, p) in blocks.items():
        if p.contains(pt):
            return no
    return None


def face_road(blocks, pub, lot, line):
    """街廓 lot 之一邊（LINE）沿兩側法向各外移 OFFSET_M 取樣；一側須落於 lot，他側之多數 ⇒ 所臨之公設區塊。"""
    (x1, y1), (x2, y2) = line
    L = math.hypot(x2 - x1, y2 - y1)
    nx, ny = -(y2 - y1) / L, (x2 - x1) / L
    side = {1: Counter(), -1: Counter()}
    for i in range(SAMPLES):
        t = (i + 0.5) / SAMPLES
        px, py = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
        for s in (1, -1):
            side[s][_locate(blocks, px + s * OFFSET_M * nx, py + s * OFFSET_M * ny)] += 1
    inner = [s for s in (1, -1) if side[s].most_common(1)[0][0] == lot]
    if len(inner) != 1:
        raise PM.SourceError(f"街廓 {lot} 之邊 {line} 兩側皆非／皆是該街廓")
    out = side[-inner[0]]
    road, n = max(((k, c) for k, c in out.items() if k is not None), key=lambda kc: kc[1], default=(None, 0))
    if road not in pub or Decimal(n) / SAMPLES < MIN_SHARE:
        raise PM.SourceError(f"街廓 {lot} 之邊外側之取樣未集中於一公設區塊：{dict(out)}")
    return road


def face_lines(msp):
    out = {LAYER_FRONT: [], LAYER_SIDE: []}
    for lay in out:
        for e in msp.query(f'LINE[layer=="{lay}"]'):
            out[lay].append(((e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)))
    return out


def special_by_road(msp, blocks, pub, case_blocks):
    """⇒ {公設編號: Σ 期望負擔面積（未乘 1−C）}、[(街廓, 面, 負擔, 公設)]。"""
    lines = face_lines(msp)
    raw = {k: Decimal(0) for k in pub}
    faces = []
    for lot in sorted(case_blocks, key=AT.block_key):
        if lot not in blocks:
            raise PM.SourceError(f"case_params 之街廓 {lot} 不在圖上")
        for face, lay in FACE_LAYER.items():
            f = case_blocks[lot].get(face)
            if f is None:
                raise PM.SourceError(f"case_params 之 {lot}.{face} 缺")
            burden = dec(f["期望負擔面積_m2"])
            if burden == 0:
                continue
            want = q(f["期望長度_m"], 3)
            hit = [ln for ln in lines[lay] if q(math.hypot(ln[1][0] - ln[0][0], ln[1][1] - ln[0][1]), 3) == want]
            if len(hit) != 1:
                raise PM.SourceError(f"{lot}.{face}：{lay} 中長 {want} 之線 {len(hit)} 條（須恰一條）")
            road = face_road(blocks, pub, lot, hit[0])
            raw[road] += burden
            faces.append((lot, face, burden, road))
    return raw, faces


# ---------------------------------------------------------------- 附表 20
def a20_rows(pub, raw, one_minus_c):
    rows = []
    for no in sorted(pub, key=lambda k: block_order(k, pub[k][0])):
        name, p = pub[no]
        total = q(p.area, 2)
        sp = q(raw[no] * one_minus_c, 2)          # 各列乘（1−C）後再取位（KL 23:15 問二）
        rows.append((no, name, total, sp, total - sp))
    sub = tuple(sum(r[i] for r in rows) for i in (2, 3, 4))
    return rows, sub


def write_a20(path, rows, sub):
    wb, ws = AT._book()
    ws.title = "公設負擔面積統計表"
    n = len(A20_HEAD)
    AT._title(ws, 1, TITLE_A20, n)
    for c, lab in enumerate(A20_HEAD, start=1):
        ws.cell(2, c, lab).alignment = AT._center()
    r = 2
    for no, name, total, sp, gen in rows:
        r += 1
        for c, v in enumerate((no, name, float(total), float(sp), float(gen)), start=1):
            ws.cell(r, c, v)
        for c in (3, 4, 5):
            ws.cell(r, c).number_format = "#,##0.00"
    r += 1
    ws.cell(r, 2, "小　計").alignment = AT._center()
    for c, v in zip((3, 4, 5), sub):
        ws.cell(r, c, float(v)).number_format = "#,##0.00"
    PM._grid(ws, 2, r, n)
    AT._sign(ws, r + 1, SIGN_A20, n)
    PM._page(ws, "1:2", landscape=False)
    wb.save(path)


# ---------------------------------------------------------------- 附表 22
def registry(lots, owners, area, zone_of, price):
    """⇒ 私／公之登記面積、所有權人數（統一編號不重複）、Σ（登記面積 × 區段單價〔個位〕）。"""
    a = {"私": Decimal(0), "公": Decimal(0)}
    uid = {"私": set(), "公": set()}
    pre_total = Decimal(0)
    for x in lots:
        ln = x["地號"]
        kinds = {r[C_PUBPRIV] for seq in owners[ln].values() for r in seq}
        if len(kinds) != 1 or not kinds <= set(a):
            raise PM.SourceError(f"{ln} 之公私別 {kinds}（須唯「私」或「公」）")
        k = kinds.pop()
        a[k] += dec(area[ln])
        for r in PM.owner_rows(owners, ln):
            if PM._blank(r[PM.C_UID]):
                raise PM.SourceError(f"{ln} 有統一編號為空之所有權人")
            uid[k].add(str(r[PM.C_UID]).strip())
        pre_total += dec(area[ln]) * dec(price[zone_of[ln]])
    if uid["私"] & uid["公"]:
        raise PM.SourceError(f"同一統一編號兼為私有與公有：{sorted(uid['私'] & uid['公'])}")
    return a, {k: len(s) for k, s in uid.items()}, pre_total


def a22_values(v, reg_area, n_owner, pre_total, sub20):
    exact = dec(v["重劃區總面積_m2_精確"])
    offset, kept = dec(v["抵充地_m2"]), dec(v["已徵收公設_m2"])
    if offset != 0 or kept != 0:
        raise PM.SourceError(f"抵充地 {offset}／原位置原面積分配 {kept} 非 0：本單未定其填法")
    reg = reg_area["私"] + reg_area["公"]
    diff = exact - reg
    if diff < 0:
        raise PM.SourceError(f"實測面積小於登記面積（{diff}）：本單未定其填法（KL 23:15 問三唯定「多」者）")
    denom = exact - offset - kept
    pre_avg = q(pre_total / reg, 2)
    post_t = post_total(v)
    post_avg_full = dec(v["重劃後平均地價_元每m2"])
    post_avg = q(post_avg_full, 2)
    cost = cost_total(v)
    total20, sp20, gen20 = sub20
    pub_raw = dec(v["_pub_raw"])
    r1 = pub_raw / denom
    r2 = Decimal(cost) / (post_avg_full * denom)
    pre_avg_map = dec(v["重劃前平均地價_元每m2"])
    return {
        "實測": q(exact, 2), "私有": q(reg_area["私"], 2), "公有": q(reg_area["公"], 2),
        "未登記": Decimal(0), "實測誤差": Decimal(0), "差額": q(diff, 2),
        "抵充": q(offset, 2), "抵充已登記": Decimal(0), "抵充未登記": Decimal(0),
        "人數": n_owner["私"] + n_owner["公"], "人數私": n_owner["私"], "人數公": n_owner["公"],
        "前總": q(pre_total, 0), "前均": pre_avg,
        "共同負擔": total20 - offset - kept, "特別": sp20, "一般": gen20,
        "費用": cost,
        "後總": q(post_t, 0), "後均": post_avg,
        "可分配": q(exact - total20, 2),
        "上漲率": q(post_avg / pre_avg, 6),                       # 表上第八項 ÷ 第五項（KL 23:20）
        "B": q(gen20 * pre_avg_map / (post_avg_full * denom), 6),
        "C": q(Decimal(cost) / post_t, 6),
        "比率": q(r1 + r2, 4), "公設比": q(r1, 4), "費用比": q(r2, 4),
        "_前均圖面": q(pre_avg_map, 2), "_前總圖面": q(v["_pre_total_map"], 0), "_denom": q(denom, 2), "_kept": q(kept, 2),
    }


def _fmt(x, nd):
    return f"{dec(x):,.{nd}f}"


A22_NCOL = 10
NF = {"area": "#,##0.00", "yuan": "#,##0", "avg": "#,##0.00", "k6": "0.000000", "pct": "0.00%", "int": "0"}


def write_a22(path, x):
    wb, ws = AT._book()
    ws.title = "計算負擔總計表"
    AT._title(ws, 1, TITLE_A22, A22_NCOL)
    left = [  # (列, 大類, 項次, 項目, 值, 格式, 單位)
        (2, "重劃前情形", "一", "重劃區實測面積", x["實測"], "area", "平方公尺"),
        (3, None, None, "1.私有土地面積", x["私有"], "area", "平方公尺"),
        (4, None, None, "2.公有土地面積", x["公有"], "area", "平方公尺"),
        (5, None, None, "3.未登記土地面積", x["未登記"], "area", "平方公尺"),
        (6, None, None, "4.實測誤差面積", x["實測誤差"], "area", "平方公尺"),
        (7, None, "二", "原公有道路溝渠河川及未登記等土地抵充面積", x["抵充"], "area", "平方公尺"),
        (8, None, None, "1.已登記土地面積", x["抵充已登記"], "area", "平方公尺"),
        (9, None, None, "2.未登記土地面積", x["抵充未登記"], "area", "平方公尺"),
        (10, None, "三", "重劃區土地所有權人數", x["人數"], "int", "人"),
        (11, None, None, "1.私有：", x["人數私"], "int", "人"),
        (12, None, None, "2.公有：", x["人數公"], "int", "人"),
        (13, None, "四", "私有土地所有權人申請（同意）辦理重劃情形　人數：", None, None, "人，占　　％"),
        (14, None, None, "面積：", None, None, "平方公尺，占　　％"),
        (15, None, "五", "評定之重劃前平均地價及總地價　總地價：", x["前總"], "yuan", "元"),
        (16, None, None, "每平方公尺地價：", x["前均"], "avg", "元"),
        (17, "各項負擔情形", "六", "公共設施用地扣除原公有道路溝渠河川及未登記土地等抵充土地後共同負擔總面積",
         x["共同負擔"], "area", "平方公尺"),
        (18, None, None, "1.臨街地特別負擔×(1-C)", x["特別"], "area", "平方公尺"),
        (19, None, None, "2.一般負擔", x["一般"], "area", "平方公尺"),
        (20, None, "七", "費用負擔總額：1.費用總額", x["費用"], "yuan", "元"),
        (21, None, None, "2.補助金額", None, None, "元"),
    ]
    right = [
        (2, "重劃後情形", "八", "評定之重劃後平均地價及總地價　總地價：", x["後總"], "yuan", "元"),
        (3, None, None, "每平方公尺地價：", x["後均"], "avg", "元"),
        (4, None, "九", "重劃後可分配土地面積", x["可分配"], "area", "平方公尺"),
        (5, "計算負擔", "十", "重劃前後每平方公尺平均地價上漲率：", x["上漲率"], "k6", None),
        (6, None, None, f"{_fmt(x['後均'], 2)} ÷ {_fmt(x['前均'], 2)}", None, None, None),
        (7, None, "十一", "公共設施用地一般負擔係數：", x["B"], "k6", None),
        (8, None, None, f"{_fmt(x['一般'], 2)} × {_fmt(x['_前均圖面'], 2)} ÷ [{_fmt(x['後均'], 2)} × "
                        f"({_fmt(x['實測'], 2)} － {_fmt(x['抵充'], 2)} － {_fmt(x['_kept'], 2)})]", None, None, None),
        (9, None, "十二", "費用負擔係數：", x["C"], "k6", None),
        (10, None, None, f"{_fmt(x['費用'], 0)} ÷ {_fmt(x['後總'], 0)}", None, None, None),
        (11, None, "十三", "平均負擔比率：", x["比率"], "pct", None),
        (12, None, None, "1.公共設施用地負擔比率：", x["公設比"], "pct", None),
        (13, None, None, "2.費用負擔比率：", x["費用比"], "pct", None),
        (14, "備註", None, "1.公共設施用地負擔比率", None, None, None),
        (15, None, None, f"{_fmt(x['共同負擔'], 2)} ÷ ({_fmt(x['實測'], 2)} － {_fmt(x['抵充'], 2)} － {_fmt(x['_kept'], 2)}) ＝ "
                         f"{x['公設比'] * 100:.2f}％", None, None, None),
        (16, None, None, "2.費用負擔比率", None, None, None),
        (17, None, None, f"{_fmt(x['費用'], 0)} ÷ [{_fmt(x['後均'], 2)} × ({_fmt(x['實測'], 2)} － "
                         f"{_fmt(x['抵充'], 2)} － {_fmt(x['_kept'], 2)})] ＝ {x['費用比'] * 100:.2f}％", None, None, None),
    ]
    if x["差額"] > 0:
        right.append((18, None, None, f"3.實測面積較登記面積多 {_fmt(x['差額'], 2)} 平方公尺，係登記與實測之差，非未登記地。",
                      None, None, None))
    for base, rows in ((0, left), (5, right)):
        for r, grp, no, lab, val, nf, unit in rows:
            if grp:
                ws.cell(r, base + 1, grp).alignment = AT._center()
            if no:
                ws.cell(r, base + 2, no).alignment = AT._center()
            ws.cell(r, base + 3, lab)
            if val is not None:
                c = ws.cell(r, base + 4, float(val) if nf != "int" else int(val))
                c.number_format = NF[nf]
            if unit:
                ws.cell(r, base + 5, unit)
    last = 21
    for c1, (r1, r2) in ((1, (2, 16)), (1, (17, 21)), (6, (2, 4)), (6, (5, 13)), (6, (14, last))):
        ws.merge_cells(start_row=r1, start_column=c1, end_row=r2, end_column=c1)
    PM._grid(ws, 2, last, A22_NCOL)
    AT._sign(ws, last + 1, SIGN_A22, A22_NCOL)
    ws.cell(last + 2, 1, f"註：{NOTE_PRE_PRICE}（總地價 {_fmt(x['_前總圖面'], 0)} 元，每平方公尺 "
                         f"{_fmt(x['_前均圖面'], 2)} 元），第五項係依重劃前土地清冊以登記面積計，故二數不同。")
    PM._page(ws, "1:1", landscape=True)
    wb.save(path)


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.004 附表 20、22（23 同式）")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)

    case_blocks, v = load_case()
    msp = load_dxf()
    blocks = load_blocks(msp)
    pub = public_blocks(blocks)
    raw, faces = special_by_road(msp, blocks, pub, case_blocks)
    cost = cost_total(v)
    one_minus_c = 1 - Decimal(cost) / post_total(v)
    rows, sub = a20_rows(pub, raw, one_minus_c)

    lots, owners, area = PM.load_cadastre()
    zone_of, unit, price = PM.load_price_zones()
    miss = {x["地號"] for x in lots} - set(zone_of)
    if miss:
        raise PM.SourceError(f"case_params 之原地號_區段 缺：{sorted(miss)}")
    reg_area, n_owner, pre_total = registry(lots, owners, area, zone_of, price)
    zones = v["重劃前區段_面積單價"]
    za = sum(dec(z["面積_m2"]) for z in zones.values())
    zt = sum(dec(z["面積_m2"]) * dec(z["單價_元每m2"]) for z in zones.values())
    if abs(zt / za - dec(v["重劃前平均地價_元每m2"])) > Decimal("0.01"):
        raise PM.SourceError(f"區段之 Σ面積×單價÷Σ面積 {zt / za} ≠ 重劃前平均地價 {v['重劃前平均地價_元每m2']}")
    v = dict(v, _pub_raw=sum(dec(p.area) for _, p in pub.values()), _pre_total_map=zt)
    x = a22_values(v, reg_area, n_owner, pre_total, sub)

    p = {k: os.path.join(a.out, n) for k, n in OUT_NAMES.items()}
    write_a20(p["a20"], rows, sub)
    write_a22(p["a22"], x)
    for lot, face, b, road in faces:
        print(f"特別負擔 {lot}.{face} {b} → {road}")
    print("附表20 " + "；".join(f"{r[0]} {r[2]}／{r[3]}／{r[4]}" for r in rows))
    print(f"附表20 小計 {sub[0]}／{sub[1]}／{sub[2]}")
    print(f"附表22 前 {x['前總']}·{x['前均']}；後 {x['後總']}·{x['後均']}；上漲率 {x['上漲率']}；"
          f"B {x['B']}；C {x['C']}；比率 {x['比率']}（{x['公設比']}＋{x['費用比']}）；人數 {x['人數']}")
    for k, f in p.items():
        print(f"輸出 {f}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄戊　`docs/出圖/W-P.004_附表20-22.md`（逐位元組照錄）

````markdown
# W-P.004　附表 20、22（23 同式）

> 出圖線·單 `出圖線/orders/W-P.004_附表20-22.md`（`ops/queue`）。本檔記其授權、內容之判斷與驗證之表。

## 一、授權（逐字）

- KL 2026-10-23 17:48：「…還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」。
- KL 2026-10-24 02:14「2. 是，表格改照手冊表樣（乙）」；14:55「是」（附表之表樣之通式）。
- KL 2026-10-26 23:14「是，1 甲、2 同意、3 同意」（W-P.003 定版·下一步 W-P.004）。
- KL 2026-10-27 23:15：「一甲、二甲（請發單端出單時加一條：附表 20 各列「乘（1−C）後再取位」）、三 B（其實實務上正式辦理重劃時，若真的重劃範圍內有未登記土地也會先行辦理登記為中華民國，所以重劃區基本是只會有總登記面積、DXF圖面計算面積，所以屬"係登記與實測之差"）、四甲、五乙（在意「地主依清冊可驗算」，所以選乙，並請發單端在表下加註「一般負擔係數所用之重劃前地價，係以各宗地之圖面面積計」，說明兩數為何不同。）、六乙。」
- KL 2026-10-27 23:20：「1. 甲」（上漲率以表上第五項之重劃前平均地價算）。

## 二、內容之判斷與所據

| 項 | 填法 | 所據 |
|---|---|---|
| 附表 20 之列 | 圖（`data/V6.dxf`）之 `BLOCK` 圖層之每一公共設施區塊一列；編號、名稱取其註記「編號-名稱」；道路在前、餘次之，各依編號 | KL 問一甲；手冊第 3085 列 |
| 公設區塊之辨 | 註記之編號非「R<數字>」者（可分配之街廓之慣例）；含二以上註記之聯集區塊不列，唯驗其面積 ＝ 成員之和 | app `parse_block_dxf` 之慣例 |
| 合計面積 | 區塊之圖面面積，二位 | 手冊第 3082〜3084 列 |
| 臨街地特別負擔 | 街廓邊（`FRONT_LINE`／`SIDE_LINE`，以長度對 `blocks.*.期望長度_m`）兩側外移 0.5 m 取樣 400 點，外側 ≥ 90％ 落於同一公設區塊者歸之；各公設區塊之 Σ 期望負擔面積 ×（1−C），**各列乘後再取位** | KL 問二甲 ＋ 加條 |
| 一般負擔 | 合計 − 特別（各列） | 手冊第 3084 列 |
| 附表 22 第一項 | 實測 ＝ `重劃區總面積_m2_精確`；私、公 ＝ U_LAND「公私別」之登記面積；第 3、4 目 0；差額記於備註 | KL 問三 B |
| 第二項 | 0（`抵充地_m2` ＝ 0） | KL 確認 |
| 第三項 | 統一編號不重複計；私、公分列 | KL 問四甲 |
| 第四項、第七項之補助 | 留空 | 資料所無 |
| 第五項 | Σ（登記面積 × 區段單價〔個位〕）÷ 登記面積和；表下加註 | KL 問五乙 |
| 第六項 | 抄附表 20 之小計 | 手冊第 3148〜3161 列 |
| 第八項 | Σ（街廓面積 × 單價·各二位）＝ 附表 21 之和；平均地價 ＝ 核心線之值 | 手冊第 3176〜3177 列；W-P.003 |
| 第九項 | 實測 − 公設合計 | 手冊第 3178〜3180 列 |
| 第十項 | 表上第八項 ÷ 第五項 | 手冊第 3182 列；KL 23:20 甲 |
| 第十一項 | 一般負擔 × 重劃前平均地價（圖面面積計·核心線）÷〔重劃後平均地價 ×（實測 − 抵充 − 原位置原面積）〕 | 手冊第 3184〜3193 列；KL 問五（係數照核心線） |
| 第十二項 | 費用總額 ÷ Σ（街廓面積 × 單價） | 核心線 `C分母形式`（加總形） |
| 第十三項 | 公設比（圖面實值 ÷ 分母）＋ 費用比 | 手冊第 3197〜3209 列；核心線 |
| 位數 | 面積二位、總地價至元、平均地價二位、上漲率與係數六位、比率 0.01％ | KL 問六乙 |

## 三、量測與故意錯誤

- 量測 `verify/plots/check_W-P004.py`：S0〜S7（獨立之讀；特別負擔之歸屬以「邊之 1 m 緩衝扣除街廓後與公設區塊交集面積最大者」異法求之）。
- 故意錯誤 `verify/plots/mutate_W-P004.py`：Ⓐ 漏一區塊、Ⓑ 未乘（1−C）、Ⓒ 先加總後取位、Ⓓ 第五項用圖面面積、Ⓔ 上漲率用核心線之值、Ⓕ 漏表下之註——皆須紅。
- 新套件：無（`ezdxf`、`shapely`、`openpyxl`、`matplotlib` 皆既有）。
````
