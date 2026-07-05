# W-A.3 細部 plan：CAD 圖層重構

> 給 Claude Code。依 CLAUDE.md 與 docs/配地計算總規格_v3.md（v3.1）概念 5、6。
> **開新對話、模型用高階模型**（動底層暫編生成 + BASELINE 語意，跨模組影響大）。
> 套用前先完成「§0 盤點」回報 KL、確認後分步動工。每步 py_compile + 異動清單。
> 行號基於 app__20260612_.py（W-A.2 後版）。

## W-A.3 目標

把 CAD 圖層語意按 v3.1 概念 5 重構，為 W-B 街角構造打乾淨地基：
1. BLOCK 語意收窄為「使用分區界」；同分區內分配分隔線移交 BASELINE。
2. BASELINE 改為「屁股線」（不平移 0.5m），兼任分配線。
3. 暫編標記「逕割性質 / 分配性質」。
4. 無 SIDE_LINE 街廓分支（無街角、不算街角評點與 Rw）。

⚠️ **本波不改 G 計算、不改面積分配邏輯**，只動「圖層語意 + 暫編標記 + 街廓外框」。
守恆式與四欄面積（W-A 成果）不得破壞——每步驗收回歸確認 R5 12 塊幾何面積=DXF真值。

---

## §0 盤點（動工前全部回報 KL，這是高風險波、務必先盤點）

### 0-1. BASELINE 儲存結構落差（最關鍵）

現況：`result['baselines'][blk] = {'point':(x,y), 'angle_deg':float, ...}`（line ~1176/1322）
——存的是「一個點 + 角度」，**不是線段兩端點**。
但 v3.1 要 BASELINE 當「屁股線」（一條線），街角構造要「垂直於 BASELINE」。
- 回報：point+angle 是否足以定義一條線（理論上點+角度可定一條無限長線）？
- 街角構造「垂直於 BASELINE」只需要 BASELINE 的「方向」（angle_deg 已有）+ 一個
  通過點（point 已有）——**若如此，現有 point+angle 結構可能已足夠**，
  不需改存兩端點。請 Claude Code 評估並回報：沿用 point+angle 即可，
  還是需補存線段兩端點？

### 0-2. 0.5m 平移現況

grep 解析階段找不到 baseline + 0.5m 平移。回報：
- 那 0.5m 平移到底在程式哪裡（UI 互動設定階段？還是根本沒實作）？
- 若根本沒實作 → 「取消 0.5m」無需動程式，僅繪圖規範敘明 BASELINE 畫在屁股線上即可。
- 若有實作 → 指出位置，評估移除影響。

### 0-3. BASELINE 的 G 計算依賴

回報 `baselines` / `baseline_pt` / `angle_deg` 被哪些下游讀取
（`_block_strip`、`solve_G`、推進方向 d_hat 等），確認「改屁股線語意」
不破壞這些依賴。特別是推進方向：v3.1 概念 6 改用 FRONT_LINE 定推進，
BASELINE 不再負責推進方向——回報現況推進方向是否依賴 baseline，若是，
W-A.3 是否要改接 FRONT_LINE（或留待 W-D）。

### 0-4. classified_blocks 建構與 BLOCK/分配線分流

`classified_blocks` 由 polygonize（line ~3217/3243）BLOCK 線重建。回報：
- 目前 polygonize 的輸入線是哪些圖層（只有 BLOCK？還是含其他）？
- 「同分區內分配分隔線」（如 R1/R2/R3 間那條）目前在哪個圖層、
  是否參與 polygonize 切出 R1/R2/R3？
- 若目前這條線在 BLOCK 圖層、參與 polygonize → W-A.3 要把它改認到 BASELINE，
  但 polygonize 仍需它來圍出 R1/R2/R3 外框（見 §3）。

---

## §1 BLOCK 語意收窄 + BASELINE 兼任分配線

### 概念

- BLOCK 圖層 = 只有使用分區界（R↔RD、R↔G、RD↔G）。
- 同分區內分配分隔線（R↔R）= BASELINE 圖層（使用者改畫在 BASELINE）。
- 街廓外框（如 R1）由「BLOCK 線 + BASELINE 線」共同圍成（§3）。

### 實作（依 §0-4 盤點結果定案）

繪圖規範改變（使用者端）：原本畫在 BLOCK 的「同分區分隔線」改畫 BASELINE。
程式端：polygonize 圍街廓外框時，輸入線 = BLOCK 線 ∪ BASELINE 線
（這樣 R1/R2/R3 仍能被 BASELINE 切開、各自圍成獨立街廓外框）。
但「跨線土地是否逕為分割」的判定要分圖層（§2）。

> 若 §0-4 顯示現況分隔線在 BLOCK、且改 BASELINE 會牽動太多，
> 回報替代方案（如：BLOCK 內部再分「分區界 BLOCK」與「分配 BLOCK」子標記）。

---

## §2 三種暫編標記（逕割性質 / 分配性質）

暫編 temp_parcel 新增欄位 `cut_type`：
```
'逕割' : 被 BLOCK 線（使用分區界）切出 → 未來逕為分割成真實子地號
'分配' : 被 BASELINE（屁股線/分配線）或宗地分配線切出 → 試分配用，不逕割
```
判定：暫編產生時，看「切出此暫編的邊」來自哪個圖層。
- 落在 BLOCK 線兩側 → 逕割
- 落在 BASELINE 兩側（同分區）→ 分配

用途：
- 四欄面積（W-A）：逕割暫編未來各有真實登記面積；分配暫編用分攤登記面積。
  W-A.3 階段兩者都先用分攤登記面積（試分配），但標記區分供未來實際作業用。
- 未來實際作業：只有 `cut_type='逕割'` 的線要送地政逕為分割。

> 本波只加標記，不改四欄面積計算邏輯。

---

## §3 街廓外框拼接（BLOCK + BASELINE 共同圍成）

每個可建築街廓的封閉外框，由其周圍的 BLOCK 線 + BASELINE 線共同圍成。
- 有分配線的街廓（R1/R2/R3）：外框 = 部分 BLOCK 線（臨道路/公設那幾邊）
  + BASELINE 線（與隔壁分配街廓的分隔邊）。
- 無分配線的小街廓：外框純 BLOCK 線。

實作：polygonize 輸入 = BLOCK ∪ BASELINE（§1），切出的每個多邊形即一個街廓外框。
街廓的「屁股線」= 該外框中，屬於 BASELINE 的那條邊（街角構造 W-B 用）。
- 若街廓屁股恰是 BLOCK 線（如三面公設地的例子，屁股是南側 BLOCK）→
  該處使用者會在 BLOCK 上重疊畫一條 BASELINE（概念 5），程式讀 BASELINE 即可。

---

## §4 無 SIDE_LINE 街廓分支

判定：街廓的 FRONT_LINE 端點（p1/p2）無任何 SIDE_LINE 相接 → 該端非街角；
兩端皆無 → 無街角街廓。
無街角街廓的處理：
- 跳過街角評點指數（W-D）、跳過街角規定範圍構造（W-B）。
- 跳過 Rw 側街負擔（W-C）：G 公式的 Rw·F·l₁ 項 = 0。
- 土地仍兩端依 FRONT_LINE 投影位次往中間排、調配池居中（概念 6）。

本波（W-A.3）只需**標記**街廓是否有街角（`has_corner: bool`、`corner_sides: ['left'/'right']`），
供 W-B/W-C/W-D 讀取。實際的街角計算分支在那些波次實作。

---

## §5 BASELINE 規範正名（依 §0-1、§0-2 結果）

- 若 §0-1 結論「point+angle 已足夠」→ BASELINE 解析不改結構，僅文件/註解
  正名為「屁股線」、語意說明更新。
- 若 §0-2 結論「0.5m 未實作」→ 無需動程式，繪圖 SOP 敘明畫在屁股線上。
- 推進方向：依 §0-3，若現況依賴 baseline，標記「W-D 改接 FRONT_LINE」、
  本波不動（避免牽動 G 計算）；若已不依賴，確認即可。

---

## 驗收（冷啟動：停 app → 重啟 → 新分頁 → Tab1 匯入 → Tab4 重跑步驟C）

| 驗收點 | 預期 |
|---|---|
| py_compile | 通過 |
| 迴歸：R5 12 塊幾何面積 | 仍 = DXF 真值（W-A 成果未破壞）|
| 迴歸：_UNC | 仍歸零、118 筆暫編對應 53 地號 |
| 街廓外框 | R1/R2/R3 各自圍出獨立外框（BASELINE 切開）；無分配線街廓純 BLOCK 圍 |
| 暫編 cut_type | 每筆有標記（逕割/分配）；跨 RD 道路的 628-7 各塊=逕割，同分區切的=分配 |
| 無街角街廓標記 | 三面公設地型街廓 has_corner=False；有 SIDE_LINE 街廓 corner_sides 正確 |
| BASELINE 屁股線 | 每可建築街廓能取到屁股線（point+angle 或線段）|
| 守恆式 | 各街廓 ΣG + 調配池 = 街廓 DXF 面積（本波未改 G，應自然成立）|

驗收通過後進 W-B（街角規定範圍構造，用本波建好的 BASELINE 屁股線 + 街廓外框）。

## 紀律
- 本波只動圖層語意/暫編標記/街廓外框，**不動 G 計算與四欄面積**。
- §0 五項盤點全部先回報 KL 再動工——尤其 0-1 BASELINE 結構、0-4 分隔線圖層，
  這兩個決定動的範圍大小。
- BASELINE 改語意若觸及 G 計算依賴（§0-3），該部分留待 W-D、本波不動。
- commit + push 到 claude/fix-cad-topology-mismatch-QfyPU。
