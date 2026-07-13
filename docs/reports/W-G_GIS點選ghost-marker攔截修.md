# W-G GIS 點選真根因修：ghost hover marker 攔截（診斷驅動）

- 日期：2026-07-13；KL localhost 活抓＋活驗；**承接 fae0e4c（修錯路·沒解決）**。
- 性質：純 app.py 圖面 trace 層；引擎/baseline/run_all 零觸。KL 兩處點選已驗 OK。

## 一、fae0e4c 修錯路（誠實記錄）

fae0e4c 修 `_resolve_clicked_parcel` 加 ghost 排除——但那是 **cn=None shapely 後援路徑**，KL 的「未對到」實走 **cn≠None 之 else 丟棄** 路徑，根本沒被走到。KL 再測仍壞。**純讀碼推理的錯猜。**

## 二、診斷驅動定根因（禁假設·實據）

改**寫檔診斷**（§2 點選後 append log＋toast·印 `_fig.data[cn].name`＝plotly 實際命中之 trace 名）。KL 點擊活抓：

```
cn=134｜命中trace=_ghost_hover_unified｜in_clk_range=False
```

**真根因**：`_ghost_hover_unified`（ghost hover **marker** trace·`mode='markers'`·`hoverinfo='text'`·z-top 於點擊靶·可點）**攔截近 ghost 之 plotly click** → cn=134 落於點擊靶範圍外 → else 丟棄 → 「未對到任何地號」。
（截圖 hover tooltip 顯示點擊靶資訊曾誤導——**hover 可同時顯示多 trace·click 只歸最頂層可點 trace**。）

## 三、真修（兩圖面·掃全函式·勿留第三破口）

全 app 恰 **2 個 ghost hover marker**，皆修：

| 圖面 | 函式 | 消費端 |
|---|---|---|
| §2 統一互動地圖 | `_render_f3_unified_map`（`_ghost_hover_unified`）| `_pevents_um` 12441 |
| 步驟 D 區段標註 | `_render_f3_overlay_figure`（`_ghost_hover`）| `_pevents_d` 12887（亦用於 12088/12869）|

各圖：①**移除 ghost hover marker trace**（攔截元兇）；②點擊靶加 `hoveron='fills'`（填色內部整片可點·非僅 width-0 頂點）。
ghost 灰填色（`hoverinfo='skip'`）**保留作視覺**·且不攔截 click（skip 讓 click 穿透至下層點擊靶）。移除 marker 後之 dead vars（`_ghost_hover_pts_*`/`_ghost_text_*`）一併清除。**取捨**：失 ghost 明細 tooltip（ghost 為已合至主體之碎屑·非點選目標·灰色仍可見）。

## 四、驗收

| 項 | 結果 |
|---|---|
| py_compile app.py | ✅ |
| 殘留掃描 | ✅ 無 `_ghost_hover_unified`/`_ghost_hover` marker·無診斷殘留 |
| **KL localhost 兩處手動** | ✅ §2 指定地價區段（`cn=49 命中_clk_628-2(1) in_range=True`→已標區段a）＋步驟D 皆命中·不再「未對到」|
| run_all | 不受影響（純圖面 trace 層）|

## 五、failure-archaeology #19（真根因更正·三血教訓）

①點擊歸屬 bug 禁讀碼猜根因·加診斷印命中 trace（fae0e4c 錯猜之教訓）；②plotly click 永歸最頂層可點 trace·根治＝移除頂層攔截 trace 非「丟棄其 cn」（024915b cn-丟棄把合法點擊也丟→症狀 A 換 B）；③hover 有作用 ≠ click 命中同一 trace。#18「z 序脆弱」於此坐實。

## 六、另案（本報告不含·續查）

KL 另抓：「重劃前地籍線」圖層顯示帶 BLOCK 線段、與 DXF 地籍（628-x）不符——獨立顯示層 issue·另偵察另報。
