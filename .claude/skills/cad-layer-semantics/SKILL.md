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

## 🔒 BASELINE 配對＝**1:N**（KL 裁定 2026-07-26·正典·失敗考古 #38）
- **屁股對屁股共用 BASELINE 是合法繪法**：兩街廓背靠背時共畫一條。UC9898 實證
  **4 條 BASELINE 服務 6 街廓**（`R2_R3-baseline` 由 R2/R3 共用、`R5_R6-baseline` 由 R5/R6 共用）。
- **不變式**：**每街廓恰有一條有效 BASELINE；一條 BASELINE 得服務 1~N 個街廓。**
  配不到者 **loud raise**，禁靜默略過。
- **配對依據禁用「最近距離」與「共端點」**。改結構性三條件（**全部成立**才配）：
  (a) 近平行 `|Δθ(BASELINE, 該街廓 FRONTLINE)| ≤ 10°`；
  (b) 位於該街廓 FRONTLINE 之**屁股側**（沿 FRONT 法向指向街廓內為正）；
  (c) 垂距落在合理深度域 `[1.0m, 街廓對角線]`——排除「0」與「發散」。
  多條同時滿足 ⇒ 取**垂距最小**者。落點：`parse_cad_precision_layers`
  （`grep -n "def parse_cad_precision_layers" app.py`·比照既有「ALLOC ⊥ FRONT」閘）。
  ⚠️ **`_extract_cad_lines` 是過期名**——僅存於 `verify/app_harvest.py` 之 `__main__` 自測清單，
  app.py 全檔無此符號；引用時勿沿用。
- **一條 BASELINE 可能被畫成數段共線線段**：UC9898 之 R1/R4 屁股線即為同一無限直線上之
  兩段（方位差 0.0005°、街廓邊到兩者垂距皆 0.0000）⇒ **配到哪一段幾何等價**、量測值不變。
  ⇒ 對拍時**禁以「配到哪一條線段」為判準**，須比**線**（角度＋垂距）或直接比量測值。
- `baselines_matched_count` **不得作為配對正確性之證據**（舊語意只計「有候選之線條數」；
  UC9898 曾 4/4 全中卻 3 對 1 錯）。現語意＝「配到 BASELINE 之街廓數」。

## 幾何容差
- 「同一直邊」可能由方位差僅十幾角秒的多段組成、直弦離邊界 ~2mm → **線上判定容差 ≥1cm**（`perp_tol=0.05` 實用），1e-6 會漏量。
- 未來案例 FRONT/SIDE/BASELINE 可能是**聚合線（折線）**——一切配對/量測不可寫死單一直線段。

## 其他鎖定語意
- **畸零地最小寬/深＝二維查表：使用分區 × 面臨道路寬度**（花蓮縣畸零地使用規則附表；正面路寬為使用者輸入）。本案住宅區×12m 與 ×8m 恰同檔 3.5m——**巧合非常數**；禁止任何「分區為主鍵」或「路寬為唯一鍵」的單鍵句（KL v2 定案 2026-07-05）。
- BLOCK 線三種語意型；ㄇ形 RD↔RD 道路切割線**不是**分割邊界。R=街廓、RD=道路、G=公設；§1 街角評選僅 R 街廓。
- 公同共有：持分和 >1（每人全額）；分別共有：持分和 ≈1。
- 實座標基準：`docs/案例空間基準_UC9898.md/.json`（53 地號＋11 面＋四線層全驗、R1 角分析 ground truth）。

## 🔒 FRONT_LINE／SIDE_LINE 綁定＝共線＋投影重疊最長（KL 裁 2026-07-26·C-6）
- **域裁**：`FRONTLINE`／`SIDELINE` 之**對側必為道路(RD)**；一條 FRONT/SIDE 線
  **只屬於一個可建築街廓**、**不存在 R-R 共用**（`BASELINE` 相反·共用合法）。
  ⇒ **候選池只含可建築街廓**（排除 RD／公設）。
- **判準＝共用原語 `_line_block_overlap`**（與 `_anchor_chamfers_topology` 同判準·
  `ang_tol=2°`／`perp_tol=1m`）：方位 mod180 差 ≤ tol ∧ 兩端垂距 ≤ tol ∧ 投影落 span 內，
  取**真實 1-D 重疊長最大**者。**廢 first-hit break**、全掃取最大。**禁自創第三種判準。**
- **側別（左/右）唯一來源＝該街廓 FRONTLINE 之 p1（左）／p2（右）**。
  🔒 **禁寫入圖層名**：同一條側街線對相鄰兩塊為**不同側別**，命名結構上不可行，
  且會產生**第二真值來源**。
- **UC9898 實測勝差**（供對拍）：FRONT 最小 80.26m（R1）、SIDE 29.56–41.42m，**次者皆 0.00**。
  8 條 SIDE 中 4 條端點同時吻合兩塊之 FRONTLINE 端點（街角處端點聚集）⇒ 端點重合法有實風險。
- **順序不變性為硬性質**：`verify/fixture_cad_binding_order.py`（置換 DXF 實體順序 3 種·逐位元組相等）。

## 🔒 幾何推論四件套（KL 裁 2026-07-26·C-12·**通則**）
凡幾何推論（線層歸屬、截角、街角規定範圍、分配線方向…）一律須配齊：
**① 自動判定 → ② 可視化列表 → ③ 使用者確認 → ④ 持久化**。
**只有 raise 而無 UI 承接者，視為未完工。**
- **案由**：泛用化目標＝供**不同案件之公務員／廠商跨案使用**。以 `RuntimeError` 或
  「請改圖層名」要求使用者自救**不是產品**。
- **分層**：引擎層偵測歧義 → raise **結構化例外**（帶各候選之量值與 entity handle）·
  維持 no-silent-fallback、**禁靜默選**；UI 層攔截 → 渲染確認頁
  （無歧義預填、按確認即過；有歧義標紅＋下拉＋並列量值），結果**持久化至專案設定**。
- **圖層命名制度全案取消**（含 `BASELINE-R1` 型逃生門）——**UI 即逃生門**，
  使用者不需學任何命名規則、既有 DXF 不需修改。
