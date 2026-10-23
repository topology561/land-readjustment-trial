# W-P.001　重劃前三圖層＋顏色對照表＋附表 2、3（出圖線之紀錄）

- 單：`ops/queue` 之 `出圖線/orders/W-P.001_重劃前三圖層與附表2-3.md`（10716 bytes·sha256 `636b393d…c7d1`）。
- 回報：`ops/queue` 之 `出圖線/reports/W-P.001_回報.md`。

## 檔

| 檔 | 用 |
|---|---|
| `plots/prelim_maps.py` | 出圖與報表：`python3 plots/prelim_maps.py --out <目錄>` ⇒ `重劃前圖.dxf`、`顏色對照表_重劃前.xlsx`、`附表02_重劃前土地地號摘錄簿.xlsx`、`附表03_重劃前土地清冊.xlsx` |
| `verify/plots/check_W-P001.py` | 量測 M0〜M7（12 項）：`python3 verify/plots/check_W-P001.py <dxf> <附表3>`；期望值自 `data/` 與 `verify/case_params_UC9898.json` 獨立取之（⛔ import 出圖程式） |
| `verify/plots/mutate_W-P001.py` | 故意錯誤之測 8 種：`python3 verify/plots/mutate_W-P001.py <成果目錄> <拋棄式之工作目錄>` |
| `verify/plots/preview_W-P001.py` | 預覽 PNG：自輸出之 DXF 與附表讀回而繪 |

## 所據與資料之來源

- 宗地幾何：`data/V6_1.dxf` 經 `app.py` 之 `parse_ua_cadastral_dxf` → `reconstruct_parcel_polygons` → `validate_parcel_assignments_by_area`（經 `verify/app_harvest.harvest()`·⛔ 改 `app.py`）；面積校正恰二次交換：`628-3↔628-1`、`628-44↔628-41`（不符即停）。
- 地號：`data/地籍資料來源_匿名版.xlsx` 之「重劃區地籍」（53 宗）；所有權：同檔 `U_LAND` 之「0013德安段」（以所有權登記次序去重·95 列·33 戶）。
- 重劃前宗地地價：`verify/case_params_UC9898.json` 之 `財務接線_v3`（區段單價四捨五入至個位：a `43909`、b `37323`）。

## 量測之讀法（執行端之記）

- M6：DXF 之系統圖層「0」（規格強制）與「Defpoints」（`ezdxf` 存檔時必補，刪之亦補回）不計，其上無任何圖元；其餘圖層恰為三層。
