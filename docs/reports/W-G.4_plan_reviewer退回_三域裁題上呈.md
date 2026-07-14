# W-G.4 plan reviewer 退回重寫 · 三域裁題上呈（停機）

- 日期：2026-07-15；plan HEAD＝`b8899c8`；規格＝v1.1（`docs/specs/終態幾何消解波_規格.md`）
- reviewer（redistribution-reviewer·獨立跑 grep/REPL·不採信 CC 說詞）判定：**退回重寫**（4 BLOCKED + 9 WARNING）
- **CC 已自驗確認** B1/B2/B3（下附 CC 自跑 REPL 輸出·對稱紀律：不採信 reviewer 說詞）
- **狀態：停機**——D1/D2/D3 為**規格未涵蓋之真實違規／規格層空白**，屬域裁層，**未裁不施工**（CLAUDE.md：必答題未裁先施工＝停機）

---

## 一、reviewer PASS 項（plan 已驗正確者）

| 項 | 內容 | reviewer 自證 |
|---|---|---|
| P1 | §B.2 `front_len_fn=None` 純加性 | `solve_G_binary` 真呼叫端僅 2 處（`app.py:14657`、`stepg_pipeline.py:292`）皆用 kwargs → default None 保 byte 不變 ✅ |
| P2 | X3（code `l_front`＝正典 l₂ 正街） | `app.py:6774` `- Rw*F*l_side - S_guess*l_front`；baseline 欄名 `l₂ 正面尺度`/`l₁ 側面尺度` 對應 ✅ |
| P3 | forced buffer＝矩形近似（非面積保留） | `stepg_pipeline.py:412-426` `_left_buffer_S = _l_min / avg_depth_default`＝**S 方向推進偏移** ✅ |
| P4 | §A 靶數逐位命中 | R2 233.79/8.7157/1.6758、R5 300.52/212.84、Z R1=109.44 R6=166.03、MinA 全組 ✅；**plan 正確抓到偵察報告漏列之 R5 forced** |
| P5 | E2 不受 E3 回饋 | `wf_f4.py:652` E2 → `:682` E3，E2 之後不再被讀 ✅ |
| P6 | 現況守恆 | baseline F.4 3.5m 殘差 R1−0.19…R6−0.17，皆 <1㎡ ✅ |

---

## 二、三域裁題（**上呈 KL／claude.ai·未裁不施工**）

### D1（reviewer B1）：R5 街角補足必破池三則 — §1.2 順位鏈第 2~4 階未設計

**CC 自驗 REPL**（scratchpad/wg4_verify_blocked.py）：
```
R5 池片 = [212.79, 163.75]  Σ=376.54
角池 212.79 → 範圍 300.52（補 87.73）；中央池 163.75 − 87.73 = 76.02
MinA_R5 = 157.64  →  76.02 ∈ (0, MinA)? True  ← 池三則破 🔴
⚠️ R5 最大池片 = 212.79（正是角池本身，非中央池）
```

**問題**：
1. 規格 §1.2「同 Ri **最大**調配池片，調至該片降至 MinA 為止」——R5 之最大池片**正是被補的角池**（212.79 > 163.75）。「最大池片」與「中央主體池」在 R5 **不是同一片**，規格文字對此情形無定義。
2. 中央池 163.75 可釋出上限僅 `163.75 − 157.64 = 6.11`（降至 MinA 為止），**遠不足 87.73**。→ §1.2 順位鏈第 2 階（同 Ri 次大池片）**已無池可調**（R5 僅 2 片）。
3. 進入第 3 階「同實體街廓其他 Ri」：**規格僅例示 R1/R2/R3 同屬一實體街廓**，未定義 R5 屬哪個實體街廓群組。
4. **更根本（reviewer 指出·CC 認同）**：跨 Ri／跨街廓「調池」在**幾何層無意義**——R5 之殘餘 76.02 是 R5 街廓內的**實體多邊形**，帳目上從 R6 撥面積**不會讓它消失**。→ 帳目級守恆與幾何級守恆**分岔**（違硬閘 1「帳目級＋幾何級」）。

**上呈選項（KL 裁）**：
- (a) 76.02 併入相鄰宗地（等 G？增配？）使 R5 中央池**歸零**（池三則允許 0）；
- (b) 縮小補足量（R5 角池補至「中央池恰為 0 或 ≥MinA」之最大可行值，接受角池 < 範圍）；
- (c) §1.2 之「跨 Ri／跨街廓調池」定義**幾何實現方式**（如何讓 R5 的實體多邊形消失）；
- (d) 其他 KL 裁示。

---

### D2（reviewer B2）：R6 右街角第1宗（**私有宗**）現存違規 — 規格無私有宗補足機制

**CC 自驗 REPL**（3.5m·全街廓街角第1宗 vs 街角規定範圍）：
```
R1 左: 628-36(1)  638.61 vs 226.18 ✅     R1 右: 628(5)    328.51 vs 226.88 ✅
R4 左: 628(1)    1979.75 vs 225.25 ✅     R4 右: 628-1(1)  576.54 vs 225.67 ✅
R2 左: （forced 抵費地）範圍 309.05        R3 右: （forced 抵費地）範圍 308.93
R5 左: （forced 抵費地）範圍 300.52
R6 右: 628-18(1)  295.60 vs 299.13 → 🔴 短 3.53 ㎡
```

**問題**：
- 規格 §1.1 明文「街角第 1 宗土地（**不論私有或抵費地**、不分 forced/中央池），面積及寬度必須 ≥ 該街角規定範圍」。
- R6 右街角第1宗＝**628-18(1)（私有宗）**，幾何 295.60 **< 299.13**（短 3.53㎡）——**現存違規**。
- R6 右**非 forced**（該側有合格街角宗、PK 有 winner）→ **buffer 位移機制無法補足**（buffer 只在 forced 時存在）。
- 私有宗要補足面積 → 須**增配 a′**（改 G，觸 §7-5 增配語意／意思決定旗標）或**重跑街角 PK 改判 forced**——**規格皆未提供機制**。
- plan §D 硬閘 3 只映射「forced 池片 ≥ rng」→ **漏掉私有宗街角第1宗**；若照規格 §3-3 如實實作硬閘 3，3.5m **必再停機一次**。

**上呈選項（KL 裁）**：
- (a) 628-18(1) 增配 3.53㎡（a′ 增·G 重算·ΔG 由 R6 池扣）→ 但這是「私有宗增配」，觸 §7-5 意思決定；
- (b) 街角規定範圍之比較基準改用「**G 值**」而非幾何面積（628-18(1) G=295.59，仍短）；
- (c) 容差放行（3.53㎡ 屬幾何切分噪音？但 §1.1 是硬約束）；
- (d) 重跑該側街角 PK（改判 forced → 抵費地充當第1宗＝範圍）；
- (e) 其他 KL 裁示。

---

### D3（reviewer W1）：buffer 變動 → W/Rw 側街負擔基準未定義（**規格層空白**）

**事實**（reviewer 查碼·CC 認同）：
- `stepg_pipeline.py:500` `_W0_left = (_left_buffer_S * _cos_dn) if _has_left_corner else 0.0`
  ＝ CLAUDE.md 正典「forced 側起始 W ＝ buffer 寬」（telescoping `ΣRw_側 = R(W_final) − R(W₀_buffer)` 之錨）。
- `stepg_pipeline.py:519-522`：該側**每一宗**都吃 `l_side`/`F`（非只第一宗）。
- plan 把 buffer 從 **R2 7.0399→8.7157**、**R5 6.6723→8.6774**，卻**凍結 G**（等 G 滑動），且 §B.1 Step 4 之 g_tab 回寫欄位清單只有 `S/G/幾何面積/宗地寬度/累積S/cut_coords`——**沒有 `W(m)`/`Rw(%)`**。

**問題**：
- 終態 g_tab 同列內 `W` 與 `累積S` 將互相矛盾（baseline 現況 R2 左第1宗 累積S=14.24、W=14.20 關係成立）。
- telescoping 差額式 `ΣRw = R(W_final) − R(W₀)` **失錨**（W₀ 隨 buffer 變、但 Rw 未重算）。
- **「G 凍結」vs「Rw 重算」是域裁層**：街角補足屬「**池際面積重分**」（則 Rw/G 皆不動、僅位置移）？還是「**改變側街負擔基準**」（則 W₀ 變 → Rw 變 → G 變）？
- 規格 §1.2 只說「一切調動為池內/池際面積重分：**總量守恆不變、位次不變**」，**未提 Rw/W 一字**。

**上呈選項（KL 裁）**：
- (a) 純池際重分：W₀/Rw/G **全凍結**（buffer 位移僅視為幾何重切基準·不改負擔）→ 需明示 g_tab 之 W 欄如何呈現（保舊值？重算？）；
- (b) 負擔隨動：W₀ 依新 buffer 重算 → Rw/G 全街廓重解（**但這違反 §1.3「一般滑動宗等 G 不變」**）；
- (c) 其他 KL 裁示。

---

## 三、CC 自修項（不需域裁·plan v2 施工前修訂）

### B3：R1 被誤當「末筆街廓」（plan 事實錯誤）

**CC 自驗 REPL**（`has_side` 實查·兩情境同）：
```
R1: left_has_side=True  right_has_side=True  → 末筆端 = 無（兩端皆街角）
R2: left_has_side=True  right_has_side=False → 末筆端 = 右
R3: left_has_side=False right_has_side=True  → 末筆端 = 左
R4: left_has_side=True  right_has_side=True  → 末筆端 = 無
R5: left_has_side=True  right_has_side=False → 末筆端 = 右
R6: left_has_side=False right_has_side=True  → 末筆端 = 左
```
**碎片所在端 × 末筆端 對照**：

| 街廓 | 碎片 | 碎片端(s_rel) | 該端 has_side | 判定 |
|---|---|---|---|---|
| R1 | 5.30（兩情境） | 左 (0.018) | **True（街角端）** | **§1.3 碎片**（非末筆） |
| R3 | 78.19（0m） | 右 (0.986) | **True（街角端）** | **§1.3 碎片**（非末筆） |
| R6 | 85.66（兩情境） | 左 (0.012) | **False（末筆端）** ✅ | **§1.4/§1.5 末筆** |

→ **§1.4 末筆規則本案僅適用 R6**。plan §A 表給 R1「末筆端 p1·Z=109.44」**撤銷**；R1/R3 碎片走 §1.3 等 G 滑動（現有 `_reshape_block` 機制之收編版）。
→ 末筆端判定**必須**由 `forced[blk]["{side}_has_side"] == False` 實查決定（該鍵存在·`selection_pipeline.py:493-499`），**禁寫死**。

### B4：`_reshape_block` 整刪 → `reshape_rows`/`reshape_polys` 契約成孤兒

reviewer 列出之消費端（CC 認同·須保契約）：

| 消費端 | 內容 |
|---|---|
| `run_verification.py:997,1001` | `d4["reshape_rows"]` 直接索引（KeyError）＋對拍 `F.4_整形_退縮*.csv` |
| `run_verification.py:1160` | `isinstance(_f4["0m"].get("reshape_polys"), dict)` |
| `run_verification.py:1162-1167` | **G.2 靜態閘**：`wf_f4.py` 原始碼中 `"reshape_polys"`／`"sgE_rows"` 各須**恰 1 次** |
| `wg_g3.py:37,57` | reshape_rows 逐格對拍（G.3 同源） |
| `app.py:17039-17114` | E 世代圖 + 整形表 |
| `wg_g2_smoke.py:64-89` | PNG |
| `wf_f4.py:698-699` | `resh_targets["R1"] != F1_REVERIFY[tag]` 錨閘 |

→ plan v2：`_resolve_block_final` **仍輸出** `reshape_rows`／`reshape_polys`／`resh_targets`（保契約·最小侵入），**不刪** 6 個消費端。`_reshape_block` 之 helper 收編（§1.8-3）但**輸出契約保留**。

### 其餘 WARNING（plan v2 一併修）
- **W2**：Step 1 之 `a_cur`（strip area）≠ 硬閘 3 驗之量（實際池片面積）——R3 右 strip=311.61 vs 池片 389.80。→ 統一用**實際池片面積**。
- **W3**：「同 Ri 最大池片」對 R5 為偽（見 D1）。
- **W4**：對側組「byte 不變」不成立（bisect 路徑 ≠ solve_G_binary·必有 sub-cent 漂移）；`_resolve_block_final` 之作用街廓集須明界定（R4 無碎片/無 forced/無末筆 → 不動）。
- **W5**：末筆 ΔG 無錨（reviewer 粗估 R6 ΔG≈+2.2㎡）；**ΔG 須同步回寫 `E`（`eng.rows()`）**，否則 `wf_f4.py:781` `cons` 立破。
- **W6**：`front_len_fn(cut)` 須守衛（`_block_strip` 於 S≤0 回 None／可能 MultiPolygon）。
- **W7**：末筆位移路徑本案零觸發（R6 628-4(1) 已在末筆位）→ 位次閘須**自建對拍**（既有 `wf_f4.py:769-780` 比的是重劃前投影序·對終態重切零保護）。
- **W8**：app.py `_wg_gen_figure` E 終態圖改 g_tab（§1.8-2）須映射子波。
- **W9**：0m R3 碎片 78.19 已收斂（見上表·§1.3 碎片）。

---

## 四、結論與下一步

- **停機**：D1/D2/D3 未裁前**不施工**（規格未涵蓋之真實違規／規格層空白·屬域裁層·reviewer 不裁·CC 不自裁）。
- **CC 已備**：B3/B4/W2~W9 之修訂方向已定，俟 D1/D2/D3 裁定後一併出 **plan v2** → 重送 reviewer → 施工。
- **未 push 不得報收官**（最高紀律）：本波尚在 plan 階段，無收官宣稱。
