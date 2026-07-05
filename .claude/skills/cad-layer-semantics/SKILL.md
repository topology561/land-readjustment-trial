---
name: cad-layer-semantics
description: 讀寫任何 CAD/DXF/SVMAP 幾何（FRONT_LINE/SLIDE_LINE/BASELINE/ALLOC_LINE/BLOCK）、做圖層配對、左右側判定、或街廓幾何運算之前必讀。涵蓋各圖層的域語意、為何線畫到未截角尖角、共線配對法、左右正典來源。
---

# CAD 圖層語意（域規則，KL 已鎖，不可協商）

## 六個正典圖層
FRONT_LINE（檔名 FRONTLINE）、SIDE_LINE（檔名 **SLIDE_LINE**——KL 慣用拼法，勿"修正"）、BASELINE、ALLOC_LINE、BLOCK、CENTERLINE。
- 各圖層 `.cnt` 點號**各自從 1 起編、互不相通**；跨檔對位一律靠座標值。
- 檔案 Big5 編碼；面積分析表（如 UC9898.L10）欄序＝點號、縱Y(北)、橫X(東)；幾何運算取 (X,Y)=(東,北)。

## 為何 FRONT/SIDE 線畫到「理論(未截角)尖角」（勿把線改短！）
- G 公式的 **F（街角地第1筆面臨側面道路之長度）＝ SIDE_LINE 全長**（到未截角角）。
- 臨街地特別負擔：**正面道路負擔總面積＝FRONTLINE 長×尺度、側面＝SIDE_LINE 長×尺度**（按面臨路寬查表）。
- 這些量依賴未截角全長 → 線必須畫到尖角。截角只影響「街角範圍多邊形」與「項一正街角線」。
- 推論：**BLOCK 邊停在截角**、比線短約截角腿長（本案 ~3.5m）→ 端點重合配對必敗（實測六塊全滅）。

## 配對法（唯一正確）：共線＋投影重疊
FRONT/SIDE → BLOCK 邊配對三條件：方位 mod180 差 < ~2°；BLOCK 邊兩端至線垂距 < ~1m；邊中點投影落在線段 span 內。截角＝拓樸夾在 FRONT-配對邊與 SIDE-配對邊之間的 BLOCK 邊。理論角 `tc['corner']` ＝ FRONT_LINE ∩ SIDE_LINE 交點。

## 左右側的正典來源（-c.1 血訓）
- **左右正典＝CAD `side_lines_by_side`（session key `f3_cad_side_lines_by_side`）**，並已於 `_rebuild_corners_topology` 建 tc 時以 `tc['side']` 入籍。
- **BLOCK 多邊形頂點/邊的 p1,p2 順序＝數化繞向，與語意左右零耦合**——任何「距 front 邊 p1/p2 近者定側」都是擲硬幣（-c.1：五塊翻、R5 倖存）。需要側別一律讀 `tc['side']` 或 `_side_wb[side]`，禁止從繞向幾何重猜。

## 方向權威
- **ALLOC_LINE 是街廓內一切幾何方向的唯一權威**：`allocation_dir = rot90(alloc_dir)`；深度用 `_compute_block_depth_alloc(alloc_dir=f3_cad_alloc_dir)`。
- W（含街角 W_i）**⊥ALLOC 量測**、非 ∥側街：實證 R1 之 ALLOC 與側街微斜 0.55°，改 ∥側街切會使相鄰候選交集各差 ~1㎡（虛胖陷阱）。
- 街角 side_mid ＝ SIDE 子段 [截角∩SIDE → BASELINE∩SIDE] 之**子段中點**（非全線中點）。
- BASELINE＝屁股線，無 0.5m offset。`front_idx` 為資訊性欄位（`true_S_length` 全檔零讀取），不驅動任何 live 量。

## 幾何容差
- 「同一直邊」可能由方位差僅十幾角秒的多段組成、直弦離邊界 ~2mm → **線上判定容差 ≥1cm**（`perp_tol=0.05` 實用），1e-6 會漏量。
- 未來案例 FRONT/SIDE/BASELINE 可能是**聚合線（折線）**——一切配對/量測不可寫死單一直線段。

## 其他鎖定語意
- **畸零地最小寬/深＝二維查表：使用分區 × 面臨道路寬度**（花蓮縣畸零地使用規則附表；正面路寬為使用者輸入）。本案住宅區×12m 與 ×8m 恰同檔 3.5m——**巧合非常數**；禁止任何「分區為主鍵」或「路寬為唯一鍵」的單鍵句（KL v2 定案 2026-07-05）。
- BLOCK 線三種語意型；ㄇ形 RD↔RD 道路切割線**不是**分割邊界。R=街廓、RD=道路、G=公設；§1 街角評選僅 R 街廓。
- 公同共有：持分和 >1（每人全額）；分別共有：持分和 ≈1。
- 實座標基準：`docs/案例空間基準_UC9898.md/.json`（53 地號＋11 面＋四線層全驗、R1 角分析 ground truth）。
