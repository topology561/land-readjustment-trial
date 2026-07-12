# W-G G.2 收官報告：GIS 終態顯示（純呈現層，零重算）

- 波次：W-G 子波 G.2；日期：2026-07-12；基準 HEAD 前＝`34b48f3`（G.2 偵察上呈）
- 鐵律：**純呈現層——數據只讀 wf 引擎回傳終態物件、禁重算（座標→plotly 變換＝明許例外）**。
- 交辦四點增補全落：①世代切換語意標籤 ②E 層以暫編去重防殘影 ③PNG 產物入倉 `docs/reports/g2_png/` ④kaleido 主路（裝成功，未用備援）。

## 一、停機上呈與 KL 裁定（本波內）

**停機事實（偵察報告 §五② 更正）**：`build_step_g_tables` **剝除 cut_coords**（stepg:857）→ f2/E 分配形原始列、
f1/f4 整形新形座標**皆未曝出**，禁重算下 f1/f2/E 三代地圖畫不出。

**KL 裁定（2026-07-12）**：准**引擎側純加性補曝＝純加性曝值第四例**（承 sgB_rows/sgD_rows/f0_parcels 先例），加三圍欄：
①曝出鍵深拷貝/tuple 凍結（防 UI 反灌引擎狀態）②靜態「只寫不讀」斷言（grep 級，每檔恰 1 寫點、他檔零越界）
③reviewer 聚焦四行落點（該代計算完成後曝、不在內迴圈）。裁定已入 `verify/baselines/wf/PROVENANCE_F5.md` §六。

**補曝清單**（全部深拷貝/tuple 凍結、該代計算完成後、每 tag 一次）：
| 檔 | 新曝鍵 | 內容 |
|---|---|---|
| wf_f2 | `sgC_rows` | trunk C 原始列（含 cut_coords）|
| wf_f4 | `sgE_rows`＋`reshape_polys` | trunk E 原始列＋E3 整形新形座標 |
| wf_f1 | `reshape_polys`＋`wedge_coords` | R1 整形新形＋楔形本體座標 |

## 二、驗收

| 閘 | 結果 |
|---|---|
| 引擎補曝零 diff | ✅ run_all **ALL GREEN**（全代 baseline 逐格 PASS＝補曝零擾動機證）|
| run_all 終態 | ✅ **155 `✅ PASS`／0 FAIL／ALL GREEN**（154＋1＝G.2 閘）|
| +1 閘 | `W-G G.2 世代幾何曝出契約＋只寫不讀（v3/f0/f1/f2/f3/E 逐宗座標·靜態越界=0）` |
| PNG smoke | ✅ **10/10**（6 世代＋4 專題）→ `docs/reports/g2_png/`（各 ~80KB） |
| localhost | `.claude/launch.json`（streamlit-app @8501）供 KL 驗視 |

**smoke 日誌（verbatim 尾段）**：
```
… 引擎全鏈跑通，開始出圖（純呈現：只讀曝出幾何）
  ✅ v3.png ✅ f0.png ✅ f1.png ✅ f2.png ✅ f3.png ✅ E.png
  ✅ theme_pool_flow.png ✅ theme_exit.png ✅ theme_reshape.png ✅ theme_ledger.png
✅ SMOKE PASS：10/10 PNG → docs/reports/g2_png
```
截圖目檢：E 終態（綠＝私人分配/黃＝池抵費地/橙＝整形新形，R1-R6 輪廓正確）、33 群 gid 著色（同色跨街廓＝同歸戶）成圖。

## 三、實作

1. **引擎補曝**（§一，+12/−2 行、dict 尾行擴充、零行為變更）。
2. **app 視覺層（module 級 builder 群，純呈現）**：
   - `_wg_gen_figure(rows, cb_by, reshape_polys, wedge_coords, compare_mode)`——世代地圖；
     **交辦②去重**：整形宗以新形取代原形（`rp.pop(pid)`＋`drawn` set，防殘影）；
     `compare_mode=True`（f1／整形專題）時原形改畫虛線外框＝前後對照。
   - `_wg_theme_pool_flow`（各塊 池_D→池_E3 差額標注＋conv_rows 源塊→目標塊藍箭頭）、
     `_wg_theme_exit`（出口三色：橙=增配§31-1-2🚩／綠=≥½配地／紅=<½現金補償🚩，**旗標語氣非自動裁**）、
     `_wg_theme_ledger`（gid palette 著色沿 Tab1 慣例、hover=應走/實走鏈/歸因）。
   - 著色慣例沿用：私人分配綠/抵費地黃（DXF NEW_PARCEL/OFFSET_LAND）、`F3_CATEGORY_COLORS`、gid palette。
3. **交辦①世代切換語意標籤**：`v3 配地基準｜f0 同街廓合併＋梯3釋池｜f1 R1楔形整形｜f2 跨街廓a′｜f3 公設調配｜E 終態（7-5最佳化＋終態整形）`。
4. **交辦③五表與圖聯動**：7-4↔池流向、7-5↔雙出口、池↔池終態圖、整形↔前後對照、總決算↔33群圖（各 tab 圖上表下）。
5. **+1 閘（154→155）**：(a) 曝出契約——五代原始列逐宗 cut_coords＋f1/f4 新形座標非空；(b) 圍欄②靜態「只寫不讀」——新曝鍵每引擎檔恰 1 寫點、wf_f0/f3/stepg/selection 零越界。
6. **PNG smoke** `verify/wg_g2_smoke.py`：headless `_build_wf_ctx`→f0→f4→harvested builder 出 10 圖（kaleido）。
7. omap 方向證實（`原地號→gid`，wf_f0:78 同式）＝gid 著色/雙出口歸戶對映正確。

## 四、上呈事項
1. **`data/地籍資料來源_匿名版.xlsx` 本機異動**（非本波所為；開波即有 `.~lock`＝LibreOffice 開啟中）。
   **未入本波 commit**、未代裁。ownership 靶全綠＝歸戶指紋未受影響。請 KL 確認是否本人操作。
2. f4 `reshape_polys` 含整形塊之全宗新形（標的＋前移＋未動；引擎輸出如此）→ E 圖橙色面較廣，
   hover 有角色區分；如需「僅變動宗著橙」屬呈現層過濾，可 G.3 後微調。
3. 33 gid > 10 色 palette 循環（同色歧義由 hover 消解）；沿用 Tab1 慣例不另造色系。

## 五、G.3 預告
雙路同源終驗（app live 終態 vs wf/f4 baseline 逐格 byte 級對拍）＝W-G 收官王牌，本波未搶。
