# GIS 點選跳位 bug 修（步驟 D 重劃前區段標註）

- 日期：2026-07-13；基準 HEAD 前＝`79a4a81`
- 觸發：KL localhost 活抓——步驟 D 點 628-35(2) 卻標到 628-37（ghost 歸屬主體）。
- 性質：**純 app.py 顯示/事件層**；引擎/baseline/快照零觸、run_all 不受影響。驗收＝localhost 手動（KL）。

## 一、根因鏈（雙因）
1. **z 序脆弱（KL 主診斷）**：ghost hover **marker** trace（`_ghost_hover_unified` app.py:3120／`_ghost_hover` 2353）於「點擊靶 trace」後 add_trace → **z-top＋可點**。plotly_events 咬到它 → 回傳**該 marker 之點**（curveNumber＝ghost trace、`ev.x/y`＝ghost 質心 near 628-37）→ 消費端 else 分支用該 x/y 做 shapely → 解到 628-37。
2. **index 錯位（更深，步驟 D）**：步驟 D 消費端 `valid_parcels`（12879）只濾 `len<3`（**含 ghost**），圖面點擊靶（2237-2245）卻**排 ghost** → `curveNumber − click_offset` 之 index 與圖面**錯位**（ghost 前置即跳位），即使命中正確靶亦錯。

## 二、修法（KL 裁 option A 精神：點選判定與渲染 z 序解耦；實裝＝當前有效機制）
**⚠️ reviewer 逐 JS 追證之關鍵**：KL 建議之「customdata 白名單」在本環境**為死碼**——
`streamlit-plotly-events==0.0.6`（`_RELEASE=True`）前端只轉發 5 鍵（x/y/curveNumber/pointNumber/pointIndex）、**不含 customdata** → `ev.get('customdata')` 恆 None。
故 option A 之 customdata **無法逕行生效**；本波以**當前有效之等效根治**修好症狀，customdata 保留為**前瞻鉤（inert）**。

**兩消費端（步驟 D 12886+／§2 12445+）當前有效解析（依序）：**
1. **curveNumber 範圍命中**（`click_offset ≤ cn < +N_parcels`）→ `valid_parcels[cn−offset]`。
2. 🚧 customdata 白名單分支（`__clk__<暫編地號>`）＝**inert**（見上；待升級套件方生效）。
3. **cn=None 才** x/y shapely 後援。
4. cn 指向非點擊靶 trace（ghost marker／填色 z-top）→ **丟棄**（`_matched=None`、提示重點）——**禁用其 `ev.x/y`**（是 trace 之點非點擊位置）＝**真正修好症狀之機制**。

**index 對齊修（步驟 D 深層 bug 之實際修法）**：步驟 D `valid_parcels` 加 `not _is_ghost_sliver` → 與圖面點擊靶集**同源同準**（§2 `_clk_parcels`＝unified 圖 `valid_clk_parcels`，本已排 ghost、且用 `len(fig.data)` exact offset、更穩健）。

**customdata kwargs**（`_render_f3_overlay` 2246、unified 3082 之 `__clk__`；ghost 2356/3120 之 `__ghost__`）：已寫但**現無人讀（inert）**、標註為前瞻鉤。

## 三、與 answer-1（GIS 預設濾 ghost）之關係
預設濾 ghost 後預設視圖無此 marker、bug 隱形消失；但 **curveNumber-by-z 脆弱性仍在**（任何後加頂層 trace 重演）→ customdata 白名單為**根治非繞過**（KL 明令落 A）。

## 四、驗收
| 項 | 結果 |
|---|---|
| py_compile app.py | ✅ |
| run_all | ✅ **155 ALL GREEN**（事件層改不觸 harness）|
| diff 範圍 | app.py（~40/9）＋failure-archaeology #18；引擎/baseline/快照/stepg/selection/tests **零觸** |
| localhost 手動（KL）| 顯示/濾 ghost 兩模式點 628-35(2) 標 b 命中該筆（非跳 628-37）；步驟 D 全宗逐筆正確 |

## 五、failure-archaeology #18（詳 §七；已據 reviewer 誠實化）
根治＝「非靶 cn 丟棄＋渲染/判定集同源＋cn=None 才後援」；customdata 白名單為理想根治但**現為死碼**（0.0.6 不轉發 customdata）→ 血的教訓＝制度記憶只准記已驗證生效者為根治。

## 六、上呈 KL（reviewer 逐 JS 追證，非阻擋當前修）
1. **customdata 白名單（option A）現 inert**：`streamlit-plotly-events==0.0.6` 前端不轉發 customdata（reviewer 讀 build JS 實證：只轉發 5 鍵）。症狀已由「非靶 cn 丟棄＋渲染/判定集同源」等效根治修好。**是否升級/patch 該套件使 customdata 真生效**（option A 完整落地、白名單成真正 z 序解耦安全網）＝KL 相依決策；升級前 customdata 保留為前瞻鉤（inert、已標註）。
2. **步驟 D 手動 offset 之脆弱（WARNING-1）**：步驟 D `click_offset` 為手動推算（目前計數正確、reviewer 逐 trace 核對吻合），但因 customdata 安全網 inert，若日後於點擊靶前新增 trace 未同步更新此式 → 靜默錯位。§2 用 `len(fig.data)` exact offset 免疫。建議日後步驟 D 對齊 §2（或 customdata 生效後置首位）。
3. **cn=None 後援兩處不一致（NOTE，pre-existing）**：§2 `_resolve_clicked_parcel` 用 temp_parcels（含 ghost）取面積最大；步驟 D 用 valid_parcels（排 ghost）取面積最小。均僅 cn=None 罕觸、影響小，可日後統一。

## 七、失敗考古 #18（已據 reviewer 更正為誠實）
根治＝「非靶 cn 丟棄＋渲染/判定集同源＋cn=None 才後援」；**新增血的教訓**：customdata 白名單為理想根治但**依賴未實證能力（事件 payload 帶 customdata）→ 實為死碼**；制度記憶只准記「已驗證生效」者為根治，跨庫事件轉發須**逐鍵驗證 payload**。
