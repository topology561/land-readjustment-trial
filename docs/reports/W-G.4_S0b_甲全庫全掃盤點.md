# W-G.4 S0b (甲) 全庫全掃盤點（禁靠印象·grep 四 pattern 逐處判定）

- 日期：2026-07-15；規格＝`W-G.4_規格_v3.md` §N3-0 (甲)（afb97ab 後續）
- 交辦：CC 前版 S0b 僅點名 2 處·claude.ai 補得 4 處·再指「app.py buffer(0.001) 實有 5 處」——**失敗考古 #20 墨未乾即再犯**。本表 grep 全庫四 pattern·逐處判定「本病灶／補償碼／相關／無關」·禁再以印象定位。
- 方法：`grep -n` 全 `.py`（app.py + verify/*.py）之 `buffer(0.001)`／`buffer(0.0011)`／`area >= 1.0`／`.difference(`。

---

## 一、本病灶：池片建構（T2 主修法標的·四處）

**判準**：`block.difference(allocated_union.buffer(0.001))` + `area >= 1.0` sliver 過濾——即「配地聯集膨脹 1mm → 差集出池 → 面積過濾」之池片建構慣用法。

| # | 檔:行 | code | 階段 |
|---|---|---|---|
| 1 | `stepg_pipeline.py:707/708/716/719` | `_uunion_d(allocated_polys).buffer(0.001)` → `blk_poly.difference()` → `g.area >= 1.0` | Step G 抵費地（harness 引擎） |
| 2 | `app.py:15247/15248/15258/15261` | `_uunion_d(allocated_polys).buffer(0.001)` → `blk_poly.difference()` → `g.area >= 1.0`（同構·N0-16：同源同碼） | Step G 抵費地（app 引擎） |
| 3 | `wf_f1.py:323/324/327/328` | `unary_union(new_polys).buffer(0.001)` → `block_poly.difference()` → `g.area >= 1.0` | F.1 R1 池重算（**CC 前漏**） |
| 4 | `wf_f4.py:715/716/719/721` | `unary_union(npolys).buffer(0.001)` → `bpoly.difference()` → `g.area >= 1.0` | E3 整形段池重算（**CC 前漏**） |

→ **T2 四處全改**為 `_block_strip` 同切線精確鋪滿（§N3-0 T2）。#1/#2 為同源同碼（N0-16）·須逐字一致；#3/#4 為抄寫複本（bug 一併抄入·#20）。

## 二、補償碼：形態學閉運算（T2 後須連根拆·兩處）

**判準**：`u.buffer(0.0011).buffer(-0.0011)`——對池片建構之 1mm 侵蝕之膨脹再侵蝕補償。

| # | 檔:行 | code | 說明 |
|---|---|---|---|
| 1 | `wf_f1.py:242` | `u = u.buffer(0.0011).buffer(-0.0011)`（`_fuse` 內） | 彌合 stepg buffer(0.001) 侵蝕縫（L235 註解自承「已被 stepg allocated_union.buffer(0.001) 侵蝕 1mm·已知而繞過」） |
| 2 | `wf_f4.py:1146` | `u = u.buffer(0.0011).buffer(-0.0011)`（`_reshape_block._fuse` 內） | 同 |

→ T2 消滅侵蝕後·補償成**過度校正**·**連根拆**（§N3-0）·`_fuse` 改為 `unary_union` 後直接斷言單一 Polygon（無縫則本就單一·有縫＝T2 未做乾淨·loud raise）。

## 三、相關·§N5 時檢視（碎片合併·非池片建構·一處）

| 檔:行 | code | 判定 |
|---|---|---|
| `app.py:15509` | `_uu_off([_poly_l, _poly_s]).buffer(0.001).buffer(-0.001)`（碎片合併·雙向 buffer 消縫） | **非池片建構病灶**——屬 §N5 碎片消解（把兩 cut_coords 合併）之 UI 側。惟其用 buffer 消縫·T2/§N5 改碎片幾何後須一致檢視（列 §N5 backlog·非 S0b T2 直接標的） |

## 四、無關·列表證清白（非池片建構·grep 命中但用途不同）

### `.difference()` 無關處

| 檔:行 | 用途 |
|---|---|
| `app.py:4107` | W-A.2 §2 無主殘料（`blk_poly.difference(covered)`·歸屬比對） |
| `app.py:4175` | 殘料迭代（`residue.difference(pp_poly)`） |
| `app.py:6224` | 道路分支切割（`poly.difference(junction_box)`） |
| `app.py:7108` | 街角截角（`target.difference(chamfer_tri)`） |
| `app.py:15913/15916/15917` | **offland 診斷表**（白縫量對照）——L15941 註解明書「offset_land 重算**未套** buffer(0.001)·故為真實幾何」＝**本病之漏偵測器·正確保留·不動** |

### `area >= 1.0` 無關處

| 檔:行 | 用途 |
|---|---|
| `app.py:3251` | 一般 polygon 面積過濾（非池片） |
| `app.py:6237` | 道路 arms 過濾 |
| `app.py:12876` | `_result.geoms` 過濾（非池片） |
| `app.py:16713` | `pc.area` 過濾（非池片） |

→ 上列 9 處 `.difference()` + 4 處 `area>=1.0` 皆**非池片建構**·T2 不動。其中 `app.py:15913-15917` offland 診斷為**漏偵測器·刻意保留真實幾何**。

## 五、KL「app.py 5 處」之核對

- `buffer(0.001)` 於 app.py **grep 命中 5 行**：`15246`（註解）/`15247`（**病灶 code**）/`15470`（註解）/`15509`（碎片合併 code）/`15941`（註解）。
- **實 code 2 處**：15247（病灶·T2 改）+ 15509（碎片合併·§N5 檢視）；**病灶僅 15247**。
- 註解 3 處（15246/15470/15941）——15941 為 offland 診斷之說明（漏偵測器）。
- KL「5 處」＝grep 命中行數（含註解）；CC 前「點名 2 處」＝指池片建構病灶（app.py 15247 + stepg 707）。**本表逐處判定·差異釐清**。

## 六、S0b T2 施工標的總表（送 reviewer 前定稿）

| 類 | 處數 | 位置 |
|---|---|---|
| **T2 改（池片建構）** | 4 | stepg:707-719 / app.py:15247-15261 / wf_f1:323-328 / wf_f4:715-721 |
| **補償碼拆** | 2 | wf_f1:242 / wf_f4:1146 |
| **§N5 檢視（碎片合併）** | 1 | app.py:15509 |
| **無關·不動** | 13 | 9× `.difference()` + 4× `area>=1.0`（含 offland 診斷漏偵測器 15913-15917 保留） |

→ **(甲) 全掃完成·逐處判定入表**。S0b plan 據此展開 T2 四處 diff + 補償碼拆 + 乙匯出升級 + 丙時序 → reviewer 審。
