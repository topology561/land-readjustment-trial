# W-P.001 補令一　附表 2、3 改照手冊表樣

- **題**：`W-P.001` 之附表 2（重劃前土地地號摘錄簿）、附表 3（重劃前土地清冊）之**版式**改照手冊之表樣；內容（地號、所有權人、面積、持分等）⛔ 變。DXF 與顏色對照表⛔ 動（KL 02:14 已定版）。
- **範圍**：唯 `plots/`、`verify/plots/`、`docs/出圖/` 之下（含改 `W-P.001` 本線所建之檔）；⛔ 改任何既有之檔。
- **授權（逐字）**：KL 2026-10-24 02:14（`出圖線/KL答覆/2026-10-24_0214.md`）「1 .是　2. 是，表格改照手冊表樣（乙）」；監看窗之讀：表頭一次之鄉鎮市區／段／小段、附表 2 一列四組「地號／備註」、附表 3 依手冊之欄序、表末簽欄、跨頁每頁重出表頭（列印標題）；「其後之附表一律照手冊之表樣」。KL 2026-10-23 17:48「所有的標題及排版由使用者編輯」——故本單唯照手冊表樣之**結構**，⛔ 做字型、框線之精修以外之排版。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`；`wip/plots` ＝ `f00dabae89c3f84263f35dbf35c1bcdd6668f134`。
- **側支**：`verify/W-P.001-tables`（自 `wip/plots` 出）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具）。

## §一　所據

1. 手冊（`參考/市地重劃作業手冊.txt`·ops/queue 之根）：
   - 第 771〜795 列附表 2 之表樣：「○○縣(市)第○○期○○ 鄉鎮 市區 段 市地重劃區地號摘錄簿 小段」；「地號 備註 地號 備註 地號 備註 地號 備註」；「編造： 校對： 承辦人： 科長： 日期：」。
   - 第 797〜864 列附表 3 之表樣：「○○縣(市)第○○期○○市地重劃區」「重劃前土地清冊」；鄉鎮市區／段／小段；欄「土地標示（地號、面積（㎡））」「持分面積（持分、面積（㎡））」「所有權人（姓名、國民身分證統一編號、住所）」「當期公告現值（元/㎡）」「當期申報地價（元/㎡）」「原規定地價或前次移轉現值（元/㎡）」「管理人（代表人）」「他項權利」「建物」「限制登記」「備註」；「編造： 校對： 承辦人： 科長： 日期：」。
   - 第 710〜712 列：「按重劃區內鄉鎮市區、段別、小段別，依地號順序摘錄」⇒ 每一（鄉鎮市區, 段, 小段）一工作表。
2. 填入之值：同 `W-P.001` §一 4、§二 5〜6（⛔ 變；KL 21:18 問二 ＝ 甲，他項權利之打勾同前）。
3. 匯入資料無縣市名、期別、重劃區名 ⇒ 題中之「○○」**照手冊原樣保留**，由使用者填（⛔ 杜撰）。小段：匿名版無值 ⇒ 留空。

## §二　規格（改 `plots/prelim_maps.py` 之 `write_appx2`、`write_appx3`；輸出檔名⛔ 變）

0. 分組：依（鄉鎮市區, 段, 小段）分組，每組一工作表，名 ＝ 段＋小段（至多 31 字）；鄉鎮市區或段為空者 `SourceError` 停（⛔ 補值）。本資料恰一組（花蓮市／德安段）。
1. **附表 2**（每工作表）：
   - 列 1：A1 ＝ `○○縣(市)第○○期○○市地重劃區地號摘錄簿`，合併 A1:H1、置中。
   - 列 2：A2 `鄉鎮市區`、B2 值、C2 `段`、D2 值、E2 `小段`、F2 值（空則空）。
   - 列 3：A3〜H3 ＝ `地號、備註、地號、備註、地號、備註、地號、備註`。
   - 列 4 起：地號依（母號, 子號）之數值升冪，**由左而右、再由上而下**每列四組（地號置 A、C、E、G；備註 B、D、F、H 留空）；末列可不滿。資料列⛔ 重出鄉鎮市區／段。
   - 資料之後空一列，次列為簽欄：`編造：`、`校對：`、`承辦人：`、`科長：`、`日期：` 各一格，由左而右（欄距 ＝ ⌊欄數÷5⌋，至少 1）；此列為工作表之末一非空列。
   - 列印標題 ＝ 列 1〜3；A4 直式；寬度縮為一頁。欄數恰 8。
2. **附表 3**（每工作表）：
   - 列 1：A1 ＝ `○○縣(市)第○○期○○市地重劃區`，合併 A1:O1；列 2：A2 ＝ `重劃前土地清冊`，合併 A2:O2；皆置中。
   - 列 3：A3 `鄉鎮市區`、B3 值、C3 `段`、D3 值、E3 `小段`、F3 值。
   - 列 4〜5（二層表頭）：A4:B4 合併 `土地標示`、C4:D4 合併 `持分面積`、E4:G4 合併 `所有權人`；列 5 之 A〜G ＝ `地號、面積（㎡）、持分、面積（㎡）、姓名、國民身分證統一編號、住所`；H〜O 各縱併列 4〜5，依序 `當期公告現值（元/㎡）、當期申報地價（元/㎡）、原規定地價或前次移轉現值（元/㎡）、管理人（代表人）、他項權利、建物、限制登記、備註`。合併格恰此 15 處（A1:O1、A2:O2、A4:B4、C4:D4、E4:G4、H4:H5〜O4:O5）。
   - 列 6 起：每宗每所有權人一列（共有者分行·95 列），欄 A〜O 之值依序 ＝ 地號、面積、持分（`分子/分母`）、持分面積、姓名、統編、住所、公告現值、申報地價、（空）、管理人「ˇ」、他項權利「ˇ」、（空）、（空）、（空）——值之算法同 `W-P.001` §二 6；地號、面積於共有者之每列皆填（⛔ 合併）。資料列⛔ 重出鄉鎮市區／段。
   - 資料之後空一列，次列為簽欄（同附表 2 之式·欄距 ⌊15÷5⌋＝3）。
   - 列印標題 ＝ 列 1〜5；A4 橫式；寬度縮為一頁。欄數恰 15。
3. 框線、欄寬、字型：得加（⛔ 量測·由使用者再編）。手冊附表 3 之「說明」二款係編造者之注意事項，⛔ 入表。
4. 發單端之原型（暫存·⛔ 入倉）已依上式實作並通過 §三 3；其預覽見 `出圖線/待KL/W-P.001_補令一_原型預覽.png`。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.001-tables`；`git merge --no-edit origin/wip/s1-endpart`；有衝突即停機。
2. **程式**：改 `plots/prelim_maps.py` 之附表 2、3 之寫法；新增 `verify/plots/check_W-P001_tables.py`，其內容**逐位元組**＝ 本單附錄甲（`sha256` ＝ `997cde00e304dc2f4d31db16374308c8ed666899aaf044ce776cb0753844fdba`·7498 bytes·⛔ 改一字；不合即停機上呈）。
3. **量測**：
   - `python verify/plots/check_W-P001_tables.py <out>/附表02_重劃前土地地號摘錄簿.xlsx <out>/附表03_重劃前土地清冊.xlsx` ⇒ T1〜T6 皆 PASS、結束碼 0。
   - `verify/plots/check_W-P001.py` 之 M7 改為呼叫 `check_W-P001_tables.run` 而以其 6 項皆過為過（期望值仍唯由附錄甲取之·⛔ 另寫）；M0〜M6 ⛔ 動；全 12 項 PASS。
4. **故意錯誤之測**（擴 `verify/plots/mutate_W-P001.py`；於拋棄式之複本）：原 ①〜⑦ 照舊皆紅；⑧ 改為 ⑧′（附表 3 於列 6 起之資料中刪一共有人之列）；新增：
   - ⓪ 舊版式：以 `wip/plots`＝`f00daba` 之 `plots/prelim_maps.py` 所出之附表 2、3 代之 ⇒ 紅；
   - ⑨ 附表 2 一列三組（清列 3 起之 G、H 欄）⇒ 紅（T1、T2）；
   - ⑩ 簽欄缺「科長：」⇒ 紅（T3）；
   - ⑪ 附表 3 拆 E4:G4 之合併 ⇒ 紅（T4）；
   - ⑫ 附表 3 失列印標題（`ws._print_rows = None`；**注意**：`ws.print_title_rows = None` 於 openpyxl 無效，發單端之原型曾誤為綠）⇒ 紅（T4）；
   - ⑬ 附表 3 之列 6 之 O 欄填「德安段」⇒ 紅（T5）。
   成果綠、①〜⑦、⑧′、⓪、⑨〜⑬ 皆紅（發單端之原型實測：⓪⑧′⑨⑩⑪⑫⑬ 皆紅、成果綠）。
5. **差異閘**（README 第四節）：`git diff --name-status 5d2a283 <側支之端>`（主線若已前進，以併入之主線之 sha 代之）每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：附表 2 全頁、附表 3 首頁（含二層表頭）之列印預覽一 PNG（法不拘，如 LibreOffice 轉 PDF 後轉 PNG），入佇列之 `出圖線/成果/W-P.001_補令一_附表2-3.png`。
7. **docs**：`docs/出圖/W-P.001_重劃前三圖層.md` 補一節記本補令（版式之改、量測、故意錯誤之表）。
8. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
9. **回報**：`出圖線/reports/W-P.001_補令一_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、差異閘、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲之 sha256 不合；或 T1〜T6 於成果不過而非程式之誤（例：資料之鄉鎮市區／段不只一組）。
3. 須改任何既有之檔、或須裝 `requirements.txt` 以外之套件（LibreOffice 等出預覽之工具不在此限，唯⛔ 入倉）。
4. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P001_tables.py`（逐位元組照錄·取用法：自本單擷取 ```` ```python ```` 與 ```` ``` ```` 間之文字，末尾一換行）

```python
# -*- coding: utf-8 -*-
"""
W-P.001 補令一：附表 2、3 之手冊表樣之量測（獨立於 plots/prelim_maps.py：⛔ import 之；期望取自倉內原始資料與手冊）。

命令列：python verify/plots/check_W-P001_tables.py <附表02.xlsx> <附表03.xlsx>
任一不過 ⇒ 結束碼 1。T1〜T3 附表 2；T4〜T6 附表 3。
"""
import functools
import os
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
XLSX_SRC = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
SIGN = ["編造：", "校對：", "承辦人：", "科長：", "日期："]
H2_ROW3 = ["地號", "備註"] * 4
H3_ROW5 = ["地號", "面積（㎡）", "持分", "面積（㎡）", "姓名", "國民身分證統一編號", "住所"]
H3_ROW4 = {1: "土地標示", 3: "持分面積", 5: "所有權人", 8: "當期公告現值（元/㎡）", 9: "當期申報地價（元/㎡）",
           10: "原規定地價或前次移轉現值（元/㎡）", 11: "管理人（代表人）", 12: "他項權利", 13: "建物",
           14: "限制登記", 15: "備註"}
H3_MERGES = {"A1:O1", "A2:O2", "A4:B4", "C4:D4", "E4:G4"} | {f"{c}4:{c}5" for c in "HIJKLMNO"}


def _blank(v):
    return v is None or (isinstance(v, str) and v.strip() == "")


def lkey(s):
    p = str(s).split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0)


@functools.lru_cache(maxsize=None)
def truth():
    import openpyxl
    wb = openpyxl.load_workbook(XLSX_SRC, read_only=True)
    rows = list(wb["重劃區地籍"].iter_rows(values_only=True))
    h = rows[0]
    it, isec, ilot = h.index("鄉鎮市"), h.index("地段"), h.index("地號")
    body = [r for r in rows[1:] if not _blank(r[ilot])]
    place = sorted({(r[it], r[isec]) for r in body})
    lots = sorted((str(r[ilot]).strip() for r in body), key=lkey)
    ls = set(lots)
    own = defaultdict(dict)
    area = {}
    for r in wb["U_LAND"].iter_rows(values_only=True):
        if r[0] != "0013德安段" or _blank(r[1]):
            continue
        m, s = divmod(int(r[1]), 10000)
        ln = f"{m}" if s == 0 else f"{m}-{s}"
        if ln in ls:
            own[ln].setdefault(r[23], (str(r[33]), str(r[32])))
            area[ln] = float(r[6])
    return place, lots, dict(own), area


def _sign_ok(ws):
    last = max(r for r in range(1, ws.max_row + 1)
               if any(not _blank(ws.cell(r, c).value) for c in range(1, ws.max_column + 1)))
    vals = [ws.cell(last, c).value for c in range(1, ws.max_column + 1) if not _blank(ws.cell(last, c).value)]
    return vals == SIGN, last, vals


def run(a2, a3):
    import openpyxl
    res = []

    def rec(n, ok, msg=""):
        res.append((n, bool(ok), msg))
        print(f"{'PASS' if ok else 'FAIL'} {n} {msg}")

    place, lots, own, area = truth()
    places = {p for pl in place for p in pl if p}
    if len(place) != 1:
        rec("T0", False, f"本資料應恰一組鄉鎮市區／段：{place}")
        return res
    town, sec = place[0]

    # 附表 2
    try:
        wb = openpyxl.load_workbook(a2)
        ws = wb.worksheets[0]
        if len(wb.worksheets) != 1:
            raise ValueError(f"工作表數 {len(wb.worksheets)}≠1")
        merges = {str(m) for m in ws.merged_cells.ranges}
        row2 = [ws.cell(2, c).value for c in range(1, 7)]
        row3 = [ws.cell(3, c).value for c in range(1, 9)]
        t1 = ("地號摘錄簿" in str(ws["A1"].value) and str(ws["A1"].value).startswith("○○縣(市)")
              and "A1:H1" in merges and row2 == ["鄉鎮市區", town, "段", sec, "小段", None]
              and row3 == H2_ROW3 and str(ws.print_title_rows).replace("$", "") == "1:3" and ws.max_column == 8)
        rec("T1", t1, f"題 {ws['A1'].value!r}；列2 {row2}；列3 {row3}；列印標題 {ws.print_title_rows}；欄數 {ws.max_column}")
        sok, last, sv = _sign_ok(ws)
        seq, notes, stray = [], [], []
        for r in range(4, last):
            for j in range(4):
                v, n = ws.cell(r, 1 + 2 * j).value, ws.cell(r, 2 + 2 * j).value
                if not _blank(v):
                    seq.append(str(v))
                if not _blank(n):
                    notes.append((r, n))
                if v in places or n in places:
                    stray.append(r)
        # 由左而右、再由上而下；除末列外每列滿四組
        full = all(sum(not _blank(ws.cell(r, 1 + 2 * j).value) for j in range(4)) == 4
                   for r in range(4, 4 + len(lots) // 4))
        rec("T2", seq == lots and not notes and not stray and full,
            f"地號 {len(seq)}（期望 {len(lots)}）序 {'合' if seq == lots else '不合'}；備註非空 {notes[:3]}；資料列重出鄉鎮市區／段 {stray[:3]}；每列四組 {full}")
        rec("T3", sok, f"末列 {sv}")
    except Exception as e:  # noqa: BLE001
        rec("T1", False, f"附表2 讀取失敗 {type(e).__name__}: {e}")

    # 附表 3
    try:
        wb = openpyxl.load_workbook(a3)
        ws = wb.worksheets[0]
        if len(wb.worksheets) != 1:
            raise ValueError(f"工作表數 {len(wb.worksheets)}≠1")
        merges = {str(m) for m in ws.merged_cells.ranges}
        row3 = [ws.cell(3, c).value for c in range(1, 7)]
        r4 = {c: ws.cell(4, c).value for c in H3_ROW4}
        r5 = [ws.cell(5, c).value for c in range(1, 8)]
        t4 = (str(ws["A1"].value) == "○○縣(市)第○○期○○市地重劃區" and ws["A2"].value == "重劃前土地清冊"
              and row3 == ["鄉鎮市區", town, "段", sec, "小段", None] and r4 == H3_ROW4 and r5 == H3_ROW5
              and merges == H3_MERGES and str(ws.print_title_rows).replace("$", "") == "1:5" and ws.max_column == 15)
        rec("T4", t4, f"併格差 {sorted(merges ^ H3_MERGES)}；列3 {row3}；列5 {r5}；列印標題 {ws.print_title_rows}；欄數 {ws.max_column}")
        sok, last, sv = _sign_ok(ws)
        body = [[ws.cell(r, c).value for c in range(1, 16)] for r in range(6, last)
                if any(not _blank(ws.cell(r, c).value) for c in range(1, 16))]
        per = defaultdict(list)
        for b in body:
            per[str(b[0])].append(b)
        bad = []
        for ln in lots:
            got = sorted((str(b[4]), str(b[5])) for b in per.get(ln, []))
            exp = sorted(own[ln].values())
            if got != exp:
                bad.append((ln, "人"))
                continue
            s = sum(float(b[3]) for b in per[ln])
            if abs(s - area[ln]) > 0.005 * len(per[ln]) + 1e-9 or any(abs(float(b[1]) - area[ln]) > 1e-9 for b in per[ln]):
                bad.append((ln, f"面積 Σ{s:.2f}≠{area[ln]}"))
        stray = [i for i, b in enumerate(body) if any(v in places for v in b)]
        exp_n = sum(len(v) for v in own.values())
        order_ok = [str(b[0]) for b in body] == sorted([str(b[0]) for b in body], key=lkey)
        rec("T5", len(body) == exp_n == 95 and set(per) == set(lots) and not bad and not stray and order_ok,
            f"列 {len(body)}（期望 {exp_n}）；不符 {bad[:4]}；資料列重出鄉鎮市區／段 {stray[:3]}；地號序 {order_ok}")
        rec("T6", sok, f"末列 {sv}")
    except Exception as e:  # noqa: BLE001
        rec("T4", False, f"附表3 讀取失敗 {type(e).__name__}: {e}")
    return res


N_T = 6

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    r = run(*sys.argv[1:3])
    sys.exit(0 if len(r) == N_T and all(x[1] for x in r) else 1)
```
