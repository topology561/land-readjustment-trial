# W-G G.2 偵察報告：GIS 終態顯示（純呈現層，禁重算）

- 波次：W-G 子波 G.2；日期：2026-07-12；基準 HEAD 前＝`cd7ad6d`（G.1 收官）
- 鐵律：**純呈現層——只讀 wf 引擎回傳之終態物件、禁在視覺層重算任何量（座標變換除外）**。
- 本報告＝偵察（禁假設）＋施工 plan。**可行性關鍵問題（幾何可用性）＝已確認可行**。

## 一、可行性結論：**可行**（幾何全數由引擎輸出曝出、無需重算）
| 世代 | 宗地幾何來源（引擎已曝、只讀） | 出處 |
|---|---|---|
| v3（trunk A·配地前） | ctx `build`/`temp` 之 `polygon_coords` ＋ trunk A g_tab `cut_coords` | Step G g_rows |
| f0（級0/0'） | `f0_out[tag]["f0_parcels"]`（polygon_coords）＋ f0 g_tab `cut_coords` | wf_f0:272 |
| f1（R1 楔形整形） | f0_parcels ＋ `f1_out[tag]["reshape_rows"]`（楔形前後） | wf_f1:135 |
| f2（跨街廓 a′） | `f2_out[tag]["f2_parcels"]` ＋ f2 g_tab `cut_coords` | wf_f2:261 |
| f3（公設調配） | `f3_out[tag]["f3_parcels"]` ＋ `sgD_rows`(cut_coords)＋`poolD_diag` | wf_f3:212-214 |
| E（終態·f4） | **f4 `g_tab`（sgE，每列 `cut_coords`＝終態宗地幾何）** ＋ `reshape_rows`（整形疊加） | wf_f4:782,804 |

- **關鍵證據**：`build_step_g_tables`（stepg:729-760）於每列 g_row 寫 `cut_coords＝parcel.exterior.coords` → **每世代 g_tab 皆帶逐宗多邊形座標**。reshape 新形亦曝座標（wf_f4:1182 `list(v.exterior.coords)`）。
- **∴ 視覺層只需讀 g_tab.cut_coords／*_parcels.polygon_coords ＋ 座標變換→plotly**（座標變換為鐵律明許例外），零重算。

## 二、專題圖層資料來源（皆引擎回傳列、只讀）
| 專題 | 來源列（引擎已曝） |
|---|---|
| 池流向（源/目標塊差額） | `pool_rows`（池_D/E 各塊）＋ `conv_rows`（源/源塊/目標） |
| 碎片與整形（楔形消滅前後） | `reshape_rows`（f1 & f4：角色/新形面積/Δ面積）＋ new_polys 座標 |
| 7-5 雙出口（增配/補償/放棄旗標） | `exit_rows`（`出口`∈增配§31-1-2 / ≥½配地 / <½現金補償） |
| 33 群總決算（實走路徑 hover） | `ledger_rows`（應走/實走鏈；33 列） |
| 五表聯動 | conv/exit/pool/reshape/ledger（G.1 已呈，G.2 加圖聯動） |

## 三、既有 GIS 慣例（可重用）
- `_render_f3_overlay_figure(classified_blocks, temp_parcels, zones_map, visible_layers)`（app.py:2135）：plotly go.Figure、逐街廓 trace＋hover、`visible_layers` 圖層控制。
- 著色：`F3_CATEGORY_COLORS`（app.py:2048 街廓分類色）、gid 配色 palette（app.py:2194 `['#1F77B4',...]`）、DXF 慣例（宗地綠 / 抵費地黃 / 中心線紅，app.py:1508-1511）。

## 四、施工 plan
1. **世代圖層 builder** `_wg_render_generation(gen, engine_out, ctx, tag)`（新 module 級純函式）：讀該世代宗地幾何（g_tab.cut_coords/*_parcels）→ plotly，宗地/池/抵費地/整形著色沿用既有慣例。
2. **世代切換器**：UI radio `v3/f0/f1/f2/f3/E` → 呈對應圖。
3. **專題圖層**：池流向/碎片整形/雙出口/33群 各一 builder（讀 §二 列），意思決定旗標（增配>0/§53-2/合議/拆單）**明確標記非自動裁語氣**。
4. **五表圖聯動**（G.1 五表 ＋ 圖）。
5. **+1 gate（→155）「G.2 世代幾何曝出契約」**：跑 f0→f4，斷言每世代 out 曝逐宗幾何（f0/f2/f3_parcels 有 polygon_coords、g_tab 列有 cut_coords、reshape_rows 有 new_polys 座標）＝視覺層「只讀不重算」之資料契約。純結構斷言、不重算。
6. **逐代 PNG smoke** `verify/wg_g2_smoke.py`：headless 建每世代 figure → 匯出 PNG（每代 ≥1 張）入報告。
7. **localhost** 供 KL 驗視。

## 五、施工決策（採建議默認、報告揭露；非架構級裁定）
1. **PNG smoke 手段**：kaleido **未安裝**（plotly 6.7.0 有）。建議 `pip install kaleido --break-system-packages`（CLAUDE.md pip 政策），headless plotly→PNG；備援＝localhost 瀏覽器截圖。
2. **E 終態幾何**：以 f4 `g_tab.cut_coords` 為主（sgE 終態逐宗）＋ `reshape_rows`/new_polys 疊加整形宗；純只讀組裝（非重算）。smoke 目視確認保真。

## 六、鐵律遵循自評
- 禁重算：全幾何/量值只讀引擎輸出，僅座標→plotly 變換（明許）。
- 意思決定：旗標視覺化用明確標記、非自動裁。
- 純加性接線層、禁 fork（延續 G.1）；引擎/baseline 零觸；+1 gate 純結構斷言。

## 七、順落（本波 commit 一併）
CLAUDE.md 加「§7 引擎接線鐵律」節：ns=globals() 非 harvest（再入）、UC9898-凍結圍欄、β 混源＋誠實圍欄、接線層純加性零 diff。
