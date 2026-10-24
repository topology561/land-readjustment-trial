# W-P.002　歸戶號（重劃前歸戶圖之註記）與附表 26 土地所有權人索引表（出圖線之紀錄）

- 單：`ops/queue` 之 `出圖線/orders/W-P.002_歸戶號與附表26.md`（24928 bytes·sha256 `dc88715a…e18e8`）。
- 回報：`ops/queue` 之 `出圖線/reports/W-P.002_回報.md`。

## 檔

| 檔 | 用 |
|---|---|
| `plots/fetch_moedict.py` | 取筆劃之資料：`python3 plots/fetch_moedict.py <倉外之目錄>` ⇒ `<目錄>/dict-revised.json`（驗 tarball 與 JSON 之 sha256；唯取一員；⛔ 執行套件之程式） |
| `plots/owner_index.py` | 筆劃之讀取、字與姓名之鍵、分群、歸戶號之編定、附表 26 之輸出 |
| `plots/prelim_maps.py` | 加 `--moedict`（必填）；DXF「重劃前歸戶圖」每宗加歸戶號之 TEXT；顏色對照表加「歸戶號」欄；新出 `附表26_土地所有權人索引表.xlsx` |
| `verify/plots/check_W-P002.py` | 量測 Q0、Q1、Q1b、Q2〜Q5（7 項·內容逐位元組＝單之附錄甲·sha256 `4d430476…c4f3`）：`python3 verify/plots/check_W-P002.py <成果目錄> <dict-revised.json>` |
| `verify/plots/mutate_W-P002.py` | 故意錯誤之測 Ⓐ〜Ⓔ：`python3 verify/plots/mutate_W-P002.py <成果目錄> <拋棄式之工作目錄> <dict-revised.json>` |
| `verify/plots/preview_W-P002.py` | 預覽 PNG：左歸戶圖（自 DXF 讀回）、右附表 26 全表 |

出圖之命令：`python3 plots/prelim_maps.py --out <目錄> --moedict <dict-revised.json>`。

## 排序之規則（單 §一 2·KL 之答）

| 項 | 規則 | 出處 |
|---|---|---|
| 筆劃之標準 | 教育部標準字體 | KL 2026-10-24 11:43「甲」（`出圖線/KL答覆/2026-10-24_0245.md` 末） |
| 姓名之比 | 逐字比較；每字先比筆劃，次部首（康熙 214 部之序），再 Unicode 碼位（筆劃與部首皆同之異字，例：汪、沈皆水部 7 劃 ⇒ 汪在沈前）；非漢字排於漢字之後 | KL 2026-10-25 02:30「一甲」 |
| 分群 | 自然人 → 公司與團體 → 公有（`U_LAND`「類別」「公私別」：公 ⇒ 公有；私＋1 ⇒ 自然人；私＋7 ⇒ 公司與團體；他者停） | 02:30「二乙」 |
| 單獨與共有 | 單獨所有之戶在前、共有之戶在後 | KL 2026-10-23 21:18「問一：甲，單獨在前」 |
| 單獨所有之戶 | 依（群, 姓名, 最小地號） | 02:30 |
| 共有之戶 | 依（人數〔少者在前〕, 首列登記人〔該戶自然人中姓名最前者〕, 最小地號）；共有戶無自然人者停 | 02:30「三甲」、02:33 |
| 索引表 | 每（所有權人, 戶）一列，依（群, 姓名, 歸戶號）；「冊」「頁」留空；「附註」＝ 歸戶號 | 02:30「四可·甲」 |

附表 26 之表樣照手冊（`參考/市地重劃作業手冊.txt` 第 4080〜4094 列）：題合併 A1:H1；二層表頭左右二組（合併 7 處）；列 4 起每列二組，由左而右、再由上而下；空一列後簽欄「承辦:　股長:　科長:　製表日期: 年 月 日」（A、C、E、G）；列印標題 1〜3、A4 直式、寬一頁。

## 筆劃之資料

- 名：教育部《重編國語辭典修訂本》（g0v/moedict-data 之整理），npm 套件 `@leonsilicon/moedict-data`，版本 `0.202603.0`（套件 MIT）。
- 網址：`https://registry.npmjs.org/@leonsilicon/moedict-data/-/moedict-data-0.202603.0.tgz`
  - tarball：20,509,261 bytes·sha256 `daf8e17ecd728bbdf4fe72ca9aa9912a01c05b34ca306a6b1cf2a6a07dcefe6d`
  - 取其 `package/dict-revised.json`：63,298,941 bytes·sha256 `f68fc3df140a64d8de6eb905ff6576bfd9d260eed0bbf5cc9c41aba5a131a7ad`
- 取 `title` 為單字者之 `stroke_count` 與 `radical`；部首以康熙部首（U+2F00〜）之 NFKC 對之，「青」對「靑」（174）。
- 授權：辭典之內容為 CC BY-ND 3.0 TW ⇒ **⛔ 入倉**（JSON 與其衍生之字表皆⛔）；每次出圖前以 `plots/fetch_moedict.py` 取至倉外。
- ⛔ 用 Unihan `kTotalStrokes`（混大陸之值：蓮 13、邱 7、阮 6）、⛔ 用 PyPI `strokes`（大陸之值）。
- 新依賴：唯標準庫（`urllib`、`tarfile`、`hashlib`）；⛔ 改 `requirements.txt`（入主線時由核心線併之）。

## 量測

| 項 | 內容 |
|---|---|
| Q0 | 筆劃之資料之 sha256 與錨（草 10、蓮 15、葉 13、蔡 15、鄭 15、邱 8、阮 7…） |
| Q1 | 歸戶圖每宗恰一歸戶號、合獨立重算之值；歸戶號恰 1〜33 |
| Q1b | 發單端手排之錨（628-26→1、628→2、628-2→3、628-51→19、713→20、628-3→21、628-35→22、628-39→23、628-40→24、628-15→33） |
| Q2 | 附表 26 之題、合併格、二層表頭、列印標題、欄數 8 |
| Q3 | 67 組之序與歸戶號、冊頁空、空位唯末 |
| Q4 | 簽欄為末列 |
| Q5 | 顏色對照表之表頭、歸戶號 1〜33、地號、色與 DXF 合 |

另：`check_W-P001.py` 12/12 照舊。

## 故意錯誤之表

| 變異 | 應紅之量測 |
|---|---|
| Ⓐ 大陸筆劃（掛換 `owner_index.load_strokes`：草 9、蓮 13、葉 12、邱 7、阮 6）後重出 | Q1、Q3、Q5 |
| Ⓑ 歸戶圖 628-26 之歸戶號 `1`→`2` | Q1 |
| Ⓒ 附表 26 漏沈昌穎之第二戶（其後遞補） | Q3 |
| Ⓓ 不分群（掛換 `owner_index.group_of` 恆回 0）後重出 | Q1、Q3、Q5 |
| Ⓔ 附表 26 之簽欄缺 `股長:` | Q4 |

另：`mutate_W-P001.py` 照舊成果綠、14 種皆紅。
