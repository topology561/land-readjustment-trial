# W-G GIS 區段點選第二破口修（_resolve_clicked_parcel ghost 污染）

- 日期：2026-07-13；KL localhost 活抓（沿 R1/R4/R6 ghost 密集帶逐點點擊仍誤配）；**獨立於 024915b**。
- 性質：純 app.py 顯示/事件層（cn=None shapely 後援）；引擎/baseline/run_all 零觸（純顯示層）。驗收＝KL localhost 手動。

## 一、根因（第二消費端·同 024915b 之 bug 類）

GIS 有**兩個獨立 plotly_events 消費端**：§2（`_pevents_um` app.py:12441）＋步驟 D（`_pevents_d` 12883）。
024915b 修的是**步驟 D 的 `valid_parcels`（排 ghost）＋兩端 curveNumber 判定路徑**；但 **§2 的 cn=None
shapely 後援**走 `_resolve_clicked_parcel(cx,cy,temp_parcels)`（app.py:5405），其候選收集迴圈
**只排 `len<3`、未排 `_is_ghost_sliver`**，而 `temp_parcels` 含 ghost →
容差 buffer 命中 ghost（取面積最大者）→ ghost 無自身區段代碼 → **誤配/落空**。
＝與 024915b **同一 bug 類（ghost 污染點選候選集）之第二實例、藏在另一消費端**。

## 二、修法（KL 明令·一行·修函式非呼叫端）

`_resolve_clicked_parcel` 候選迴圈加 `if tp.get('_is_ghost_sliver'): continue`（與既有 `len<3` 同位置·
純幾何過濾·禁重算）。**修共用函式**＝所有 caller 一次安全（§2 之 cn=None 後援即受惠）。

## 三、全函式掃描（KL 明令「一次堵齊·勿留第三破口」）

| 消費端/函式 | 候選集 | ghost 狀態 |
|---|---|---|
| §2 `_pevents_um`(12441)→`_resolve_clicked_parcel`(5405) | temp_parcels | 🔴→✅ 本次修 |
| 步驟 D `_pevents_d`(12883·12930) | valid_parcels（排 ghost） | ✅ 024915b 已修 |
| `_resolve_clicked_block`(5451·12589/12660/12724) | classified_blocks | ✅ 無 ghost（街廓非 ghost）|
| 3315 `poly.contains(pt)` | OPAR 文字→polygon 標籤配對 | — 非點選路徑 |

**全 app 恰 2 個 plotly_events call**（§2/步驟D）；parcel-click 解析僅 `_resolve_clicked_parcel`＋步驟 D 內聯迴圈。**無第三破口。**

## 四、驗收

| 項 | 結果 |
|---|---|
| py_compile app.py | ✅ |
| headless 單測（harvest 取函式） | ✅ ①ghost+real→real（排 ghost）②ghost-only→None（不誤配）③real-only 不誤傷 ④容差 buffer 亦排 ghost |
| run_all | 不受影響（純顯示/事件層·未觸 harness）|
| diff 範圍 | app.py（`_resolve_clicked_parcel` +4/1）＋failure-archaeology #19＋CLAUDE.md 收官判準；引擎/baseline/verify 零觸 |
| **localhost 手動（KL 驗收）** | 沿 R1/R4/R6 ghost 帶（628-1(1)/628-35(2) 周邊）逐點·區段代碼命中對應宗地·無「未對到任何地號」|

## 五、failure-archaeology #19

「同類 bug（ghost 污染點選候選集）可能藏在多個獨立消費端，修一處後仍須全函式掃描（grep 全 plotly_events／
全 resolve 函式／全 temp_parcels 候選迴圈），不能假設『同類 bug 只有一個』。優先修共用函式、掃描重複內聯實作。」

## 六、連帶：W-G 收官判準修正（KL 2026-07-13·入 CLAUDE.md）

先前「G.3 三重確立即收官」過寬（G.3 只證同快照兩路同源·點選 bug 致無法實跑七級調配至終態·前提不實質成立）。
**W-G 收官＝① G.3 三重確立（已成 335f5f3）＋② GIS 點選 bug 修畢（本波）＋③ KL localhost 實跑七級調配至 E 終態成立（KL 驗收）**。三者齊備才報 W-G 收官，泛化波偵察交辦文彼時方遞。
