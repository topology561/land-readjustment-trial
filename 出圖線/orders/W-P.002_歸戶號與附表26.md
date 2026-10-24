# W-P.002　歸戶號（重劃前歸戶圖之註記）與附表 26 土地所有權人索引表

- **題**：依 KL 所定之序編「歸戶號」，註於 DXF 之「重劃前歸戶圖」圖層之每宗，並入「顏色對照表」；產製手冊附表 26「土地所有權人索引表」。DXF 之他圖元、附表 2、3 ⛔ 變（KL 已定版）。
- **範圍**：唯 `plots/`、`verify/plots/`、`docs/出圖/` 之下（含改本線所建之 `plots/prelim_maps.py`）；⛔ 改任何既有之檔；⛔ 改 `requirements.txt`。
- **授權（逐字）**：
  - KL 2026-10-23 17:31「1. 是　2. 以手冊（拾參）所附的圖例為主」；17:48「…還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」（README 第一節）。
  - KL 2026-10-23 21:18「問一：甲，單獨在前；問二：甲」（歸戶圖每宗註歸戶號；單獨所有者在前、共有者在後·`出圖線/KL答覆/2026-10-23_2118.md`）。
  - KL 2026-10-24 11:43「甲」（筆劃 ＝ 教育部標準字體·`出圖線/KL答覆/2026-10-24_0245.md` 末）。
  - KL 2026-10-24 14:55「是」（附表 2、3 之手冊表樣定版，為其後附表之通式·`出圖線/KL答覆/2026-10-24_1455.md`）。
  - KL 2026-10-25 02:30「一甲　二乙　三甲　四可·甲」；02:33「共有戶裡同時有自然人和公司（或公有土地）時，以自然人為主」（`出圖線/KL答覆/2026-10-25_0230.md`）。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `d4928d4845513a42fb1ac826a63167a38c78d4fb`（W-P.001 時為 `5d2a283`，已前進；發單端以 `git merge-tree` 試併 `wip/plots` 無衝突）；`wip/plots` ＝ `7827368fda88058f8e978e27956640d2e0f56abc`。
- **側支**：`verify/W-P.002-owner-index`（自 `wip/plots` 出）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具）。

## §一　所據

1. 手冊（`參考/市地重劃作業手冊.txt`·ops/queue 之根）：
   - 第 2719〜2724 列：「單獨所有土地…將所有權人姓名及國民身分證統一編號相同者歸為一戶，歸戶號得以姓名筆劃多寡為順序編列」；「共有土地…將各共有人相同者歸為一戶，歸戶號得以共有人數之多寡作排列順序編列」。
   - 第 3829〜3832 列：「編製土地所有權人索引表(附表 26)…(1) 依照土地所有權人姓氏筆劃順序排列。(2) 註明各該姓氏於土地分配清冊之冊數及頁數。(3)…應單獨裝訂成冊」。
   - 第 4080〜4094 列附表 26 之表樣：題「土地所有權人索引表」；欄「所有權人姓名｜分配清冊（第 冊、第 頁）｜附註」左右二組；表末「承辦: 股長: 科長: 製表日期: 年 月 日」。
2. KL 之答（引言之逐字）之讀，定為下列規則（監看窗之讀·見答覆檔）：
   - **筆劃之比**（一甲）：逐字比較；每字先比筆劃（教育部），筆劃同而字不同者依部首序，使同姓相鄰；姓同再比第二字、第三字。
   - **分群**（二乙）：自然人在前，公司與團體次之，公有最後；各群之內依上法。歸戶號之單獨所有之戶與索引表皆適用（KL 所答之題名即「歸戶號與土地所有權人索引表之排序」）。
   - **共有戶**（三甲·02:33）：人數少者在前；同人數者依「首列登記人」之姓名（＝ 該戶自然人中依上法最前者），再同者依該戶最小之地號。共有人中有任一自然人者屬自然人之群。
   - **索引表**（四可·甲）：每一所有權人皆列，共有者每人一列；同一人分屬數戶者每戶一列、同名相鄰；「冊」「頁」留空，「附註」填歸戶號。
   - 單獨所有者在前、共有者在後（21:18）。
3. 筆劃之資料：npm `@leonsilicon/moedict-data@0.202603.0`（MIT；資料源 g0v/moedict-data ＝ 教育部《重編國語辭典修訂本》）之 tarball `https://registry.npmjs.org/@leonsilicon/moedict-data/-/moedict-data-0.202603.0.tgz`（20,509,261 bytes·sha256 `daf8e17ecd728bbdf4fe72ca9aa9912a01c05b34ca306a6b1cf2a6a07dcefe6d`）內之 `package/dict-revised.json`（63,298,941 bytes·sha256 `f68fc3df140a64d8de6eb905ff6576bfd9d260eed0bbf5cc9c41aba5a131a7ad`）。取 `title` 為單字者之 `stroke_count` 與 `radical`（11,327 字·無一字二值）。辭典內容之授權為 CC BY-ND 3.0 TW ⇒ **⛔ 入倉**（JSON 與其衍生之字表皆⛔）；唯讀其 JSON、⛔ 執行套件之程式碼。⛔ 用 Unihan `kTotalStrokes`（混大陸值：蓮 13、邱 7、阮 6）。
4. 所有權人之群：`U_LAND` 第 37 欄「類別」、第 38 欄「公私別」（0 起算）：「公私別」＝「公」⇒ 公有；「私」且「類別」＝ 1 ⇒ 自然人；「私」且「類別」＝ 7 ⇒ 公司與團體；其餘之組合 ⇒ `SourceError` 停（⛔ 自定；示範之 53 宗唯此三種：(1,私) 89 列、(3,公) 3 列、(5,公) 2 列、(7,私) 1 列）。**附記**：發單端 16:35 之請示稱公有土地一戶，實為二戶——628-3、628-34（「類別」5）與 713、718、719（「沈辰思宗」·「類別」3·「公私別」公·有管理者）；本單依資料之欄。
5. 歸戶之鍵：同 `W-P.001`（`plots/prelim_maps.py` 之 `households`：該宗全體所有權人之（統編, 姓名）之集合）⇒ 33 戶（單獨 21、共有 12）。

## §二　規格

0. **取筆劃之資料**：新增 `plots/fetch_moedict.py`：`python plots/fetch_moedict.py <目錄>` ⇒ 以標準庫下載 §一 3 之 tarball、驗其 sha256、以 `tarfile` **唯取** `package/dict-revised.json` 一員寫至 `<目錄>/dict-revised.json`、驗其 sha256；任一不合即報錯停。⛔ `npm install`、⛔ 執行套件內之任何程式。輸出之目錄⛔ 在倉內（量測與出圖皆以參數指其路徑）。
1. **新增 `plots/owner_index.py`**（介面名照此，§三 4 之故意錯誤之測以之掛換）：
   - `load_strokes(path) -> dict[str, tuple[int, int]]`：驗 JSON 之 sha256（不合即 `SourceError`）；回傳 字 →（筆劃, 部首號）。部首號 ＝ 康熙 214 部之序（`unicodedata.normalize("NFKC", chr(0x2F00 + i))` → `i + 1`；資料之部首「青」以「靑」〔174〕對之）；部首不在 214 部者 `SourceError`。
   - 字之鍵：漢字（`unicodedata.name` 以 `CJK UNIFIED IDEOGRAPH` 或 `CJK COMPATIBILITY IDEOGRAPH` 起者）＝ `(0, 筆劃, 部首號, ord(字))`；漢字而無筆劃之資料者 `SourceError`（⛔ 補值）；非漢字（數字、英文字母、括號等）＝ `(1, ord(字), 0, 0)`，排於漢字之後（示範資料之「測試團體182」係匿名化所致）。姓名之鍵 ＝ 逐字之鍵之序列。**筆劃與部首皆同而字不同者依 `ord`**（＝ Unicode 之康熙部首＋餘筆之字典序；唯定其先後，同姓相鄰不受影響——此點於第一版之確認時告 KL）。
   - `group_of(row) -> int`：自然人 0、公司與團體 1、公有 2（§一 4）。
   - `number_households(...)`：單獨所有之戶依（群, 姓名之鍵, 最小地號）；共有戶依（人數, 首列登記人〔該戶自然人中姓名之鍵最小者〕之姓名之鍵, 最小地號）；共有戶無自然人者 `SourceError`（其群與人數孰先未定·停而上呈）。單獨在前、共有在後，自 1 連號。
   - `index_rows(...)`：每（所有權人, 戶）一列，依（群, 姓名之鍵, 歸戶號）排序 ⇒ [(姓名, 歸戶號)]。
   - `write_appx26(path, rows)`。
2. **改 `plots/prelim_maps.py`**：
   - 命令列加 `--moedict <dict-revised.json>`（必填）。
   - DXF：於「重劃前歸戶圖」圖層之每宗加一 TEXT ＝ 該宗之歸戶號（阿拉伯數字之字串，如 `1`），置點、字高、字型與該宗之地號之註記同（`representative_point`·`MIDDLE_CENTER`）。DXF 之他圖元（地籍線、地號、填色、地價）⛔ 變；各戶之顏色⛔ 變（色盤仍依原之戶序指派）。
   - 顏色對照表之「重劃前歸戶圖」工作表：表頭改 `圖層、歸戶號、顏色 R,G,B、所有權人、地號`；列依歸戶號升冪（1〜33）。「重劃前地價圖」工作表⛔ 變。
   - 新輸出 `附表26_土地所有權人索引表.xlsx`；附表 2、3 ⛔ 變。
3. **附表 26 之表樣**（照手冊；一工作表）：
   - 列 1：A1 ＝ `土地所有權人索引表`，合併 A1:H1、置中。
   - 列 2〜3（二層表頭·左右二組）：A2 `所有權人姓名`（A2:A3 縱併）、B2 `分配清冊`（B2:C2 橫併）、D2 `附註`（D2:D3 縱併）；E〜H 同之（E2:E3、F2:G2、H2:H3）；B3、F3 ＝ `第 冊`，C3、G3 ＝ `第 頁`（字與半形空白照手冊）。合併格恰此 7 處。
   - 列 4 起：依 §二 1 之 `index_rows` 之序，**由左而右、再由上而下**每列二組（同附表 2 之通式·KL 14:55）；姓名置 A／E，「冊」「頁」（B、C／F、G）留空，附註（D／H）＝ 歸戶號（整數）。末列可不滿。示範資料 67 組 ⇒ 列 4〜37。
   - 資料之後空一列，次列為簽欄：`承辦:`、`股長:`、`科長:`、`製表日期: 年 月 日`（照手冊·半形冒號），置 A、C、E、G；此列為工作表之末一非空列。
   - 列印標題 ＝ 列 1〜3；A4 直式；寬度縮為一頁。欄數恰 8。框線、欄寬、字型得加（⛔ 量測）。
4. 發單端之原型（暫存·⛔ 入倉）已依上式實作；其輸出通過 §三 3 全部，`W-P.001` 之量測 12/12 與故意錯誤 14 種皆紅亦照舊；預覽見 `出圖線/待KL/W-P.002_原型預覽.png`。原型之歸戶號：單獨之自然人 1〜18（余思宛 1、阮宛哲 2、林廷弘 3…鄭昌靜 18）、公司 19（628-51）、公有 20〜21（713 等、628-3 等）、共有 22〜33（2 人 5 戶、3 人 2 戶、4 人 3 戶、5 人 1 戶、13 人 1 戶）。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.002-owner-index`；`git merge --no-edit origin/wip/s1-endpart`；有衝突即停機。
2. **程式**：§二 0〜3；新增 `verify/plots/check_W-P002.py`，其內容**逐位元組** ＝ 本單附錄甲（`sha256` ＝ `4d430476496dc4dc85d61a9a95888f39ea0acfe77347419ced5667ffd7bdc4f3`·11490 bytes·⛔ 改一字；不合即停機上呈）。
3. **量測**：
   - 以 `plots/fetch_moedict.py` 取得 JSON（倉外）；`python plots/prelim_maps.py --out <out> --moedict <json>`。
   - `python verify/plots/check_W-P002.py <out> <json>` ⇒ Q0、Q1、Q1b、Q2〜Q5 共 7 項皆 PASS、結束碼 0。
   - `python verify/plots/check_W-P001.py <out>/重劃前圖.dxf <out>/附表03_重劃前土地清冊.xlsx` ⇒ 12/12（⛔ 改該檔）。
4. **故意錯誤之測**：新增 `verify/plots/mutate_W-P002.py <成果目錄> <拋棄式之工作目錄> <json>`；成果須綠，下列 5 種各紅（發單端之原型實測之不過項附於括號）：
   - Ⓐ 大陸筆劃：掛換 `owner_index.load_strokes` 使其回傳之草 9、蓮 13、葉 12、邱 7、阮 6 後重出 ⇒ 紅（Q1、Q3、Q5）；
   - Ⓑ 歸戶圖 628-26 之歸戶號 `1` 改 `2` ⇒ 紅（Q1）；
   - Ⓒ 附表 26 漏一列（沈昌穎之第二戶，其後遞補）⇒ 紅（Q3）；
   - Ⓓ 不分群：掛換 `owner_index.group_of` 恆回 0 後重出 ⇒ 紅（Q1、Q3、Q5）；
   - Ⓔ 附表 26 之簽欄缺 `股長:` ⇒ 紅（Q4）。
   另：`verify/plots/mutate_W-P001.py <out> <工作目錄>` 照舊成果綠、14 種皆紅（⛔ 改該檔·每跑約 3 分鐘）。
5. **差異閘**（README 第四節）：`git diff --name-status d4928d4845513a42fb1ac826a63167a38c78d4fb <側支之端>`（主線若再前進，以實際併入之主線之 sha 代之）每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：左「重劃前歸戶圖」（自輸出之 DXF 讀回而繪：填色＋歸戶號）、右附表 26 全表，一 PNG，入佇列之 `出圖線/成果/W-P.002_歸戶號與附表26.png`（得擴 `verify/plots/` 之預覽程式或新增之）。
7. **docs**：新增 `docs/出圖/W-P.002_歸戶號與附表26.md`：排序之規則（§一 2）與 KL 之答之出處、筆劃之資料之名、版本、網址、兩 sha256、授權（⛔ 入倉之故）、取得之命令；新依賴⛔ 改 `requirements.txt`（入主線時由核心線併之）；量測與故意錯誤之表。
8. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
9. **回報**：`出圖線/reports/W-P.002_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、差異閘、`wip/plots` 前後值、33 戶之歸戶號之表）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲之 sha256 不合；tarball 或 JSON 之 sha256 不合；或 Q0〜Q5 於成果不過而非程式之誤。
3. 任一所有權人之「類別／公私別」不在 §一 4 之三種；任一共有戶無自然人；任一姓名之漢字無筆劃之資料。
4. 須改任何既有之檔、或須裝 `requirements.txt` 以外之 Python 套件（出預覽之工具不在此限，唯⛔ 入倉）。
5. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P002.py`（逐位元組照錄·取用法：自本單擷取 ```` ```python ```` 與 ```` ``` ```` 間之文字，末尾一換行）

```python
# -*- coding: utf-8 -*-
"""
W-P.002：歸戶號（重劃前歸戶圖之註記）、顏色對照表之歸戶號、附表 26 土地所有權人索引表之量測。
獨立於 plots/：⛔ import 之；期望取自倉內原始資料、教育部筆劃之資料（dict-revised.json）、手冊與 KL 之答。

命令列：python verify/plots/check_W-P002.py <成果目錄> <dict-revised.json>
  成果目錄 ＝ plots/prelim_maps.py --out 之目錄（讀 重劃前圖.dxf、顏色對照表_重劃前.xlsx、附表26_土地所有權人索引表.xlsx）。
任一不過 ⇒ 結束碼 1。Q0 筆劃之資料；Q1/Q1b 歸戶圖之歸戶號；Q2〜Q4 附表 26；Q5 顏色對照表。
排序之所據：KL 2026-10-23 21:18（單獨在前）、2026-10-25 02:30（一甲 二乙 三甲 四可·甲）、02:33（共有戶以自然人為主）。
"""
import functools
import hashlib
import json
import os
import sys
import unicodedata
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
XLSX_SRC = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
MOE_SHA = "f68fc3df140a64d8de6eb905ff6576bfd9d260eed0bbf5cc9c41aba5a131a7ad"
# 教育部標準字體之筆劃（KL 2026-10-24 11:43「甲」；大陸之值：草 9、蓮 13、葉 12、蔡 14、鄭 14、邱 7、阮 6）
STROKE_ANCHORS = {"草": 10, "花": 8, "蓮": 15, "連": 11, "進": 12, "葉": 13, "蔡": 15, "鄭": 15,
                  "邱": 8, "郭": 11, "阮": 7, "余": 7, "沈": 7}
# 發單端依 KL 之答手排之錨（地號 → 歸戶號）
HH_ANCHORS = {"628-26": 1, "628": 2, "628-2": 3, "628-51": 19, "713": 20, "628-3": 21,
              "628-35": 22, "628-39": 23, "628-40": 24, "628-15": 33}
FILE_DXF = "重劃前圖.dxf"
FILE_COLOR = "顏色對照表_重劃前.xlsx"
FILE_A26 = "附表26_土地所有權人索引表.xlsx"
L_CAD, L_OWN = "重劃前地籍線", "重劃前歸戶圖"
A26_MERGES = {"A1:H1", "A2:A3", "B2:C2", "D2:D3", "E2:E3", "F2:G2", "H2:H3"}
A26_ROW2 = ["所有權人姓名", "分配清冊", None, "附註"] * 2
A26_ROW3 = [None, "第 冊", "第 頁", None] * 2
A26_SIGN = ["承辦:", "股長:", "科長:", "製表日期: 年 月 日"]
COLOR_HEAD = ["圖層", "歸戶號", "顏色 R,G,B", "所有權人", "地號"]
N_HH, N_INDEX = 33, 67


def _blank(v):
    return v is None or (isinstance(v, str) and v.strip() in ("", "null"))


def lkey(s):
    p = str(s).split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0)


@functools.lru_cache(maxsize=None)
def moe(path):
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    rad_no = {}
    for i in range(214):
        rad_no[unicodedata.normalize("NFKC", chr(0x2F00 + i))] = i + 1
    rad_no["青"] = 174
    tab = {}
    for e in json.loads(raw):
        t = e.get("title", "")
        if len(t) == 1:
            tab[t] = (int(e["stroke_count"]), rad_no[e["radical"].strip()])
    return sha, tab


def ckey(c, tab):
    if unicodedata.name(c, "").startswith(("CJK UNIFIED IDEOGRAPH", "CJK COMPATIBILITY IDEOGRAPH")):
        s, r = tab[c]          # 缺 ⇒ KeyError ⇒ 量測不過（⛔ 補值）
        return (0, s, r, ord(c))
    return (1, ord(c), 0, 0)


def nkey(name, tab):
    return tuple(ckey(c, tab) for c in name)


def grp(kind, pub):
    kind, pub = str(kind).strip(), str(pub).strip()
    if pub == "公":
        return 2
    if pub == "私":
        return {"1": 0, "7": 1}[kind]
    raise KeyError((kind, pub))


@functools.lru_cache(maxsize=None)
def truth(moe_path):
    import openpyxl
    _, tab = moe(moe_path)
    wb = openpyxl.load_workbook(XLSX_SRC, read_only=True)
    rows = list(wb["重劃區地籍"].iter_rows(values_only=True))
    il = rows[0].index("地號")
    lots = sorted((str(r[il]).strip() for r in rows[1:] if not _blank(r[il])), key=lkey)
    ls = set(lots)
    own = defaultdict(dict)       # 地號 → 登記次序 → (統編, 姓名, 群)
    for r in wb["U_LAND"].iter_rows(values_only=True):
        if r[0] != "0013德安段" or _blank(r[1]):
            continue
        m, s = divmod(int(r[1]), 10000)
        ln = f"{m}" if s == 0 else f"{m}-{s}"
        if ln in ls:
            own[ln].setdefault(int(r[23]), (str(r[32]), str(r[33]), grp(r[37], r[38])))
    hh_lots = defaultdict(list)
    hh_mem = {}
    for ln in lots:
        k = frozenset(own[ln].values())
        hh_lots[k].append(ln)
        hh_mem[k] = sorted(k)
    singles, joints = [], []
    for k, mem in hh_mem.items():
        first = min(lkey(x) for x in hh_lots[k])
        if len(mem) == 1:
            _, nm, g = mem[0]
            singles.append(((g, nkey(nm, tab), first), k))
        else:
            heads = [nkey(nm, tab) for _, nm, g in mem if g == 0]
            if not heads:
                raise ValueError(f"共有戶無自然人 {mem}")
            joints.append(((len(mem), min(heads), first), k))
    seq = [k for _, k in sorted(singles)] + [k for _, k in sorted(joints)]
    no_of_hh = {k: i + 1 for i, k in enumerate(seq)}
    no_of_lot = {ln: no_of_hh[k] for k, v in hh_lots.items() for ln in v}
    idx = sorted(((g, nkey(nm, tab), no_of_hh[k]), nm) for k, mem in hh_mem.items() for _, nm, g in mem)
    index = [(nm, key[2]) for key, nm in idx]
    lots_of_no = {no_of_hh[k]: sorted(v, key=lkey) for k, v in hh_lots.items()}
    return lots, no_of_lot, index, lots_of_no


def _last_row(ws):
    return max(r for r in range(1, ws.max_row + 1)
               if any(not _blank(ws.cell(r, c).value) for c in range(1, ws.max_column + 1)))


def run(out_dir, moe_path):
    import openpyxl
    res = []

    def rec(n, ok, msg=""):
        res.append((n, bool(ok), msg))
        print(f"{'PASS' if ok else 'FAIL'} {n} {msg}")

    sha, tab = moe(moe_path)
    got = {c: tab.get(c, (None,))[0] for c in STROKE_ANCHORS}
    rec("Q0", sha == MOE_SHA and got == STROKE_ANCHORS, f"sha256 {sha[:12]}…；筆劃 {got}")
    lots, no_of_lot, index, lots_of_no = truth(moe_path)
    anc = {ln: no_of_lot.get(ln) for ln in HH_ANCHORS}

    # Q1 歸戶圖之歸戶號
    try:
        import ezdxf
        from shapely.geometry import Point, Polygon
        msp = ezdxf.readfile(os.path.join(out_dir, FILE_DXF)).modelspace()
        polys = [Polygon([(p[0], p[1]) for p in e.get_points("xy")])
                 for e in msp if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == L_CAD and e.closed]
        lot_poly = {}
        for e in msp:
            if e.dxftype() == "TEXT" and e.dxf.layer == L_CAD:
                pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
                hit = [i for i, pg in enumerate(polys) if pg.contains(pt)]
                if len(hit) == 1:
                    lot_poly[e.dxf.text] = hit[0]
        on = defaultdict(list)
        stray = []
        for e in msp:
            if e.dxftype() == "TEXT" and e.dxf.layer == L_OWN:
                pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
                hit = [ln for ln, i in lot_poly.items() if polys[i].contains(pt)]
                if len(hit) == 1:
                    on[hit[0]].append(e.dxf.text)
                else:
                    stray.append(e.dxf.text)
        wrong = [(ln, on.get(ln), no_of_lot[ln]) for ln in lots if on.get(ln) != [str(no_of_lot[ln])]]
        rec("Q1", set(lot_poly) == set(lots) and not wrong and not stray
            and sorted(set(no_of_lot.values())) == list(range(1, N_HH + 1)),
            f"註記 {sum(len(v) for v in on.values())}（期望 {len(lots)}）；不符 {wrong[:4]}；落宗外 {stray[:3]}")
    except Exception as e:  # noqa: BLE001
        rec("Q1", False, f"DXF 讀取失敗 {type(e).__name__}: {e}")
    rec("Q1b", anc == HH_ANCHORS, f"錨 {anc}")

    # Q2〜Q4 附表 26
    try:
        wb = openpyxl.load_workbook(os.path.join(out_dir, FILE_A26))
        if len(wb.worksheets) != 1:
            raise ValueError(f"工作表數 {len(wb.worksheets)}≠1")
        ws = wb.worksheets[0]
        merges = {str(m) for m in ws.merged_cells.ranges}
        r2 = [ws.cell(2, c).value for c in range(1, 9)]
        r3 = [ws.cell(3, c).value for c in range(1, 9)]
        rec("Q2", ws["A1"].value == "土地所有權人索引表" and merges == A26_MERGES and r2 == A26_ROW2
            and r3 == A26_ROW3 and str(ws.print_title_rows).replace("$", "") == "1:3" and ws.max_column == 8,
            f"題 {ws['A1'].value!r}；併格差 {sorted(merges ^ A26_MERGES)}；列2 {r2}；列3 {r3}；列印標題 {ws.print_title_rows}；欄數 {ws.max_column}")
        last = _last_row(ws)
        seq, filled_bad, holes = [], [], []
        for r in range(4, last):
            for j in range(2):
                nm, bk, pg, nt = (ws.cell(r, 1 + 4 * j + d).value for d in range(4))
                if _blank(nm):
                    if not (_blank(bk) and _blank(pg) and _blank(nt)):
                        filled_bad.append(r)
                    holes.append((r, j))
                    continue
                if not (_blank(bk) and _blank(pg)):
                    filled_bad.append(r)
                seq.append((str(nm), nt))
        body_last = 4 + (N_INDEX - 1) // 2
        holes_ok = all(r > body_last or (r == body_last and j == 1 and N_INDEX % 2 == 1) for r, j in holes)
        diff = next(((i, seq[i] if i < len(seq) else None, index[i] if i < len(index) else None)
                     for i in range(max(len(seq), len(index)))
                     if i >= len(seq) or i >= len(index) or seq[i] != index[i]), None)
        rec("Q3", seq == index and len(index) == N_INDEX and not filled_bad and holes_ok,
            f"列 {len(seq)}（期望 {len(index)}）；首差 {diff}；冊頁非空 {filled_bad[:3]}；空位 {holes[:3]}")
        vals = [ws.cell(last, c).value for c in range(1, ws.max_column + 1) if not _blank(ws.cell(last, c).value)]
        rec("Q4", vals == A26_SIGN, f"末列 {vals}")
    except Exception as e:  # noqa: BLE001
        rec("Q2", False, f"附表 26 讀取失敗 {type(e).__name__}: {e}")

    # Q5 顏色對照表之歸戶號
    try:
        import ezdxf
        from shapely.geometry import Polygon
        wb = openpyxl.load_workbook(os.path.join(out_dir, FILE_COLOR), read_only=True)
        rows = list(wb["重劃前歸戶圖"].iter_rows(values_only=True))
        head, body = list(rows[0]), [r for r in rows[1:] if any(not _blank(v) for v in r)]
        nos = [r[1] for r in body]
        lot_ok = all(sorted(str(r[4]).split("、"), key=lkey) == lots_of_no.get(r[1]) for r in body)
        hcol = {}
        for e in msp:
            if e.dxftype() == "HATCH" and e.dxf.layer == L_OWN:
                rp = Polygon([(v[0], v[1]) for v in e.paths[0].vertices]).representative_point()
                hit = [ln for ln, i in lot_poly.items() if polys[i].contains(rp)]
                if len(hit) == 1:
                    hcol[hit[0]] = "{},{},{}".format(*e.rgb)
        col_bad = [r[1] for r in body if any(hcol.get(ln) != r[2] for ln in str(r[4]).split("、"))]
        rec("Q5", head == COLOR_HEAD and nos == list(range(1, N_HH + 1)) and lot_ok and not col_bad,
            f"表頭 {head}；歸戶號 {nos[:3]}…{nos[-2:]}（{len(nos)}）；地號合 {lot_ok}；色與圖不符 {col_bad[:3]}")
    except Exception as e:  # noqa: BLE001
        rec("Q5", False, f"顏色對照表讀取失敗 {type(e).__name__}: {e}")
    return res


N_Q = 7

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    r = run(*sys.argv[1:3])
    sys.exit(0 if len(r) == N_Q and all(x[1] for x in r) else 1)
```
