# W-G.4 裁定 M — 施工 plan **v2**（Q1＋M 同波·全做）

> canonical＝`docs/specs/W-G.4_KL域裁M_原位次小往大_街角winner更正.md`（M-1~M-4）。
> **BEFORE 錨＝`df9834c`**（Q-M3 裁定）。基準 commit＝`b5f1a86`。
> 前置：plan v1 → reviewer **BLOCKED×6＋WARNING×8** → 四題上呈 → KL/claude.ai 裁 →
> T1 真 G 探針（`docs/reports/W-G.4_裁定M_T1_真G探針結果.md`）測得 **winner 零翻盤**
> ⇒ 依裁決分支 **plan v2 全做**。
> 依 CLAUDE.md：plan 一寫完**立即送 reviewer**、不停等 KL。

---

## 〇、既裁不重議（本 plan 之不動前提）

| 題 | 裁決 | 本 plan 之落實處 |
|---|---|---|
| **Q-M1** | (b) 先量後裁 → T1 量畢**零翻盤** ⇒ **全做**（Q1＋M 同波） | 全 plan |
| **Q-M2** | **樂觀**口徑（兩端皆不預設 forced·不扣對端 buffer）＋**落地後一致性硬閘**（winner 實配 G < 街角規定面積 ⇒ **loud 停機**） | §四 P-C-3、§五 P-D-6 |
| **Q-M3** | **合法重定錨程序**：BEFORE 釘 `df9834c`／逐格歸因／**單獨 commit** 重烤／**禁改 `skip_cols`** | §八 P-H |
| **Q-M4** | 真 G 走**同一 `_solve_one` 整條含 fallback**；**loud raise 限「輸入缺值」**（solver 失敗不 raise·走既有 `iterate_G_S` 退路） | §二 P-0b、§三 P-A |

> ⚠️ **引表必連裁決段**（`failure-archaeology #27`）：本 plan 引 T1 探針之 M-2(c) 靶
> （R2左 8.65／R5左 52.56／R3右 103.66）時，其前提為 **Q-M2 樂觀口徑＋假設第 1 宗**；
> 該三數**不可**與 reviewer 之「實配 G」數列互代（二者量的不是同一件事·T1 §二已定）。

---

## 〇.5、**BEFORE 實測狀態**（施工前必先釘死·`b5f1a86`＝功能上等同 `df9834c`）

**實測**（`python verify/run_all.py` → `verify/out/M_before_runall.log`）：
**42 PASS ／ 22 FAIL**（`RESULT: FAIL`）。
`git diff --stat df9834c b5f1a86` ＝ **10 檔全為 docs／skill／探針**（`app.py`／`verify/*.py` 治理碼零異動）
⇒ **BEFORE 錨 `df9834c` 與現況同態**，本表即 Q-M3 之「前」。

**BEFORE FAIL 集合（22 項·逐字）**：

| # | 閘 | 成因（倉內既載） |
|---|---|---|
| 1-6 | `v3·G值{0m,3.5m}`／`v3·滑池槽{…}`／`v3·J表{…}` | **v3 baseline 過期·待波末重烤**（S1 波 defer） |
| 7 | `k* 六塊經驗錨3.5m` | 同上（k* 為經驗非機制不變量） |
| 8-9 | `W-D.3 碎片幾何/三分類(v3)`／`碎片逐邊CAD(v3)` | 同上 |
| 10-15 | `W-D.4 四梯清單{0m,3.5m}`／`碎片遞補{…}`／`跨占分配線{…}` | 同上 |
| 16 | `F.0 釋池對象＝梯3 二群 [('G025',1.79),('G030',55.09)]` | 同上 |
| **17** | **`W-F F.0`** | **`🔴 六格錨破：G007 G(Σa)=359.43 ≠ 錨 362.08（0m）`**（`wf_f0.py:198`） |
| 18-21 | `W-F F.1`／`F.2`／`F.3`／`F.4` | **級聯**：F.0 raise → 存在性守衛全跳過 |
| 22 | `W-G G.2 世代幾何曝出契約` | 級聯（`_f0["0m"]` 為 None） |

### 🔴 對本 plan 之**結構性後果**（新發現·plan v1 未察）

**錨之落點（實查）**：`verify/wf_f0.py:55-56` `GSA_EXPECT`（硬寫字面·`"0m": {"G006":365.84,
"G007":362.08, "G009":153.19, …}`），判於 `:192-199`。
⚠️ **關鍵旁支**：`:194-196` 對 `WV_BAKE` 環境變數**降級為 warning**
（`⚠️ [WV_BAKE] 六格錨異…`）、**不 raise**。

⇒ 二條結論（**第一條修正我先前之過度推論**）：

1. **P-E 並非「完全不可驗」**——以 `WV_BAKE=<tmp>` 跑即可穿過 F.0 抵達 `wf_f2`
   （既有 `probe_capacity_decomp` 家族正是走此路）。故 **E-1 之 expand 同值斷言、
   M-1/M-3 三段測項，皆可在 P-0c 之前先驗**。
2. **但 `run_all` 生產閘仍紅**（無 `WV_BAKE` 即 raise）⇒ 本波**收不了官**。
   故「**F.0 六格錨重烤**」仍須自 P-H 前移為 **P-0c**——只是它是
   **「收官之前置」而非「P-E 之前置」**。此即倉內既已認列之「波末重烤」
   （`wg4-s1-endpart-fallback` 記「CC 次動作＝波末重烤」、S1 波以 `准紅碼` 放行），本波為其到期日。

- **P-0c 之性質＝重定錨**（改 `GSA_EXPECT` 字面·屬**錨家族**）⇒ 依 canonical §五.3 ＋ Q-M3：
  **獨立 commit**、報告獨立節載前後值、附逐格歸因。
- **歸因來源**：六格錨過期係 **S0b/S0c/N1／兩階段落位 P2** 之既有連動（本波之前），
  **非本波引入** ⇒ 歸因表須**明載其 commit 出處**，禁以「本波所致」混算
  （否則 Q-M3 之「逐格歸因」失去鑑別力）。
- **🔒 隔離鐵律（防兩批變動混烤）**：P-0c 必須在 **P-C／P-D／P-E 之前**落地
  （即：**先**把「本波前之既有連動」烤進錨、**再**做本波之口徑與機制改動），
  如此 P-H 之歸因表所見之差異**純屬本波**。**禁**把 P-0c 與 P-H 併為一次重烤。
- **若 F.0 重烤後 F.1~F.4 仍紅** ⇒ 該紅為**既有**（`W-F F.4` 3.5m E2 結構性不可行·
  上界 7 < 需求 9·倉內已認列待域裁）⇒ 誠實定位、**不得**與本波混算。

### BEFORE 之 M-4 二 fixture（實跑·§七 之「前」）

| fixture | 實跑結果 | log |
|---|---|---|
| `verify/fixture_end_reserve.py` | **RESULT: PASS**（末端保留路徑活著·窗寬縮減 7.5000 ＝ F+MW） | `verify/out/M_before_end_reserve.log` |
| `verify/fixture_end_fallback.py` | **RESULT: ALL GREEN ✅（左右雙向）**（驗0/①/②/③/④ 全綠·左右各 5 項） | `verify/out/M_before_end_fallback.log` |

---

## 一、總覽：七步 commit 序（每步獨立可驗）

| 步 | 名 | 性質 | 綠判準 |
|---|---|---|---|
| **P-0a** | `_compute_v3_finance` 抽出（B/C/尺度/地價·單一真相源） | **純位移·零行為** | 三張 v3 baseline **byte 級零 diff** |
| **P-0b** | `_solve_G_one` 抽出（`_solve_one` 整條含 fallback·module 級） | **純位移·零行為** | 全 baseline **byte 級零 diff**＋`run_all` FAIL 集合逐字不變 |
| **P-0c** | **F.0 六格錨重烤**（`wf_f0.py:55-56 GSA_EXPECT`·§〇.5） | **重定錨**（既有連動·非本波） | `W-F F.0` 轉綠、`F.1~F.4` 得以執行；歸因表明載成因 commit。**必須先於 P-C**（隔離鐵律） |
| **P-A** | `_corner_first_lot_G`（假設第 1 宗真 G·樂觀口徑） | 新增·未接線 | ns 雙向閘綠＋新 fixture 綠；**baseline 零 diff**（未接線） |
| **P-B** | `run_corner_pk(..., snapshot=)`＋9 呼叫端＋`_pk_one_side_v12(require_g_map=)` | 純加性 | 兩顆 golden 綠；**baseline 零 diff**（真 G 尚未驅動達標） |
| **P-C** | 達標改吃真 G＋`真G(㎡)` 欄＋or-鏈消滅＋**app 鏡射同 commit**＋欄集結構閘 | **行為改**（口徑） | T1 預測：winner 零翻盤 ⇒ **指配/抵費地 baseline 零 diff**；診斷表新增欄（重定錨） |
| **P-D** | **M-2(c) 合併自救**＋consumed registry＋街角-vs-街角全域序＋兩趟定點＋落地一致性硬閘 | **行為改**（主體） | 3.5m 三 forced 端逐端報「缺口是否補足／由哪些源宗補」 |
| **P-E** | **M-1／M-3 三段**（`F2_GROUPS` 現算分流·expand-contract） | **行為改** | 三段各≥1 測；`F2_GROUPS` 同值斷言證等後方刪 |
| **P-F** | **M-4 末端塊交互驗證**（實測·非宣稱） | 驗證 | 二 fixture 續綠＋末端保留讀數歸因 |
| **P-G** | 容量拆解重跑＋報告 | 驗證 | 「9 戶差 2 戶」是否消失（**附 W-7 誠實註**） |
| **P-H** | **baseline 重烤**（**獨立 commit**·逐格歸因） | 重定錨 | 歸因表逐格；**禁改 `skip_cols`** |

**耦合鐵律**：P-C 與 P-D 不可拆序（自救門檻用的就是真 G）；但 P-0a/P-0b/P-A/P-B **純加性**，
先行落地可把「口徑改動」與「機械位移」之錯因分離（#20 四處同改教訓）。

---

## 二、P-0：兩項純位移抽出（**零行為變更·各自單獨 commit·先行**）

### P-0a — `stepg_pipeline._compute_v3_finance`（reviewer **R1** 裁：抽共用 helper）

**現況**：B／C／`sb_rows_by_label`／`post_price_by_block`／`pre_price_by_zone` 全在
`run_step_g` 函式體內算（`verify/stepg_pipeline.py:90-192`）。PK 階段要真 G 就要同一組值
⇒ 若在 PK 端**複刻**即第三份抄寫（`#20` 已付學費）。

**作法**：把 `:90-192` **原封不動**移入 module 級

```python
def _compute_v3_finance(ns, ss, cb, cad, snapshot):
    """B／C／特別負擔尺度／地價（v3 單一真相源）。**純位移自 run_step_g**：
    算式、求值順序、兩處斷言（條件① 尺度、C 兩形等價 1e-8）逐字不動。"""
    ...
    return {"B": B_value, "C": C_for_calc, "sb": sb, "sb_rows_by_label": ...,
            "post_price_by_block": ..., "pre_price_by_zone": ...,
            "_V3_FINANCE": {...}}   # 外拋 dict 原樣
```

`run_step_g` 改為呼叫之並解包。**不移動** `_tab6_burden` 之取值與 raise（`:170-177`）——
其屬 session 前置檢查、非財務算式，且 PK 階段**尚未鋪底**該鍵（移入會使 PK 誤 raise）。

**零行為證明**（唯一可採信之證據）：
1. `git stash` 前後各跑 `run_all` → **FAIL 集合逐字不變**；
2. 三張 v3 baseline（`G 值計算結果`／`滑池槽診斷`／`J 表` × 雙情境）**byte 級零 diff**
   （`fc /b` 或 `git diff --stat` 於 `verify/out/` 產物）；
3. `globals()["_V3_FINANCE"]` 外拋內容**逐鍵逐值**相等（新增臨時斷言，證畢即刪）。

⚠️ **不改 `run_step_g` 簽章**（`stepg_pipeline` 為 8 處消費之熱點）。

### P-0b — `app._solve_G_one`（**Q-M4 裁：同一 `_solve_one` 整條含 fallback**）

**現況兩份**：`app.py:15662`（`main()` 內嵌 def）／`verify/stepg_pipeline.py:298-328`（`run_step_g` 內嵌）。
二者皆閉包吃 `B_value`／`C_for_calc`／`_tab6_burden`／`solve_G_binary`／`iterate_G_S`。

**作法**：於 **app.py module 級**新增

```python
def _solve_G_one(*, a_m2, A, l_front, l_side, F, blk_poly, d_hat, baseline_pt,
                 S_max, is_corner, side, avg_depth, B, C, tab6_burden,
                 allocation_dir=None, side_mid=None, W_prev=0.0):
    """G 解算單一真相源：幾何二分法 → **失敗退 `iterate_G_S`（原 fallback 整條保留）**。
    回 `(res, solver_label)`。**Q-M4**：假設第 1 宗與實配第 1 宗共用本函式。"""
```

body ＝ 現行 `_solve_one` **逐字**（含 `try/except Exception: pass` → `iterate_G_S`
→ `area_geom = S×avg_depth`／`cut_coords = []`）。**不加 raise**（Q-M4：loud raise 限輸入缺值·見 P-A）。

兩處內嵌 `_solve_one` 改為**薄殼**（保留原簽章與呼叫端零改）：

```python
def _solve_one(_a_m2, _A, ..., _W_prev=0.0):
    return _solve_G_one(a_m2=_a_m2, A=_A, ..., B=B_value, C=C_for_calc,
                        tab6_burden=_tab6_burden, ...)
```

`_solve_G_one` 入 `_WF_NS_NAMES`；`stepg_pipeline` 以 `ns["_solve_G_one"]` 取（同
`solve_G_binary`／`_oblique_s_max` 既有慣例）。

**零行為證明**：同 P-0a 三項＋`run_all` 全 baseline 零 diff。

> **為何 P-0b 不可省**：Q-M4 裁「同一 `_solve_one` 整條含 fallback」。若 `_corner_first_lot_G`
> 直呼 `solve_G_binary`（如 T1 探針），則**閘之 solver 覆蓋 ⊊ 實配之 solver 覆蓋**——
> 幾何二分法失敗時實配仍配得出（走代數迭代），閘卻判 G=0 ⇒ 淘汰 ⇒ 閘比實配嚴、
> 正是 Q1 鐵律三「口徑一致」所禁。**T1 探針之 `_true_G` 於此點與本 plan 不同源，
> 其絕對值待 P-A 後複量**（結構結論「零翻盤」不受影響：二分法本案全收斂）。

---

## 三、P-A：`_corner_first_lot_G`（假設第 1 宗真 G·**樂觀口徑**）

**落點**：app.py module 級（緊接 `_estimate_G_for_qualification` 之後），入 `_WF_NS_NAMES`。

```python
def _corner_first_lot_G(*, a_m2, A_ratio, B, C, l_front, l_side, F,
                        block_poly, d_hat, corner_pt, s_max_left, s_max_right,
                        side, allocation_dir, side_mid, avg_depth,
                        tab6_burden, _label=''):
    """M-2 Q1：**假設第 1 宗**之真 G。**與實配第 1 宗同一條 solve 路徑**（`_solve_G_one`）。"""
```

### 3.1 參數口徑（**Q-M2 樂觀**·reviewer B-6/W-5/R3 已修正）

| 參數 | 值 | 依據（含 reviewer 更正） |
|---|---|---|
| `baseline_pt` | 左＝`corner_pt`；右＝`corner_pt + s_max_right·d̂` | 兩端皆不預設 forced ⇒ `buf=0`（Q-M2 樂觀） |
| `d_hat` | 左＝`+d̂`；右＝`−d̂` | `stepg:576/647` 左右組 |
| `S_max_limit` | 左＝**`S_block_max`**；右＝**`_oblique_s_max`** | **reviewer B-6 更正**（plan v1 誤寫兩端同 `_oblique_s_max`；`app:6925-6927` 自述 R3 差 **3.4571m**） |
| | **不扣對端 buffer**（`_right_buffer_S`／`left_cum_S`） | 「樂觀」之定義；**已知偏寬**、故配 §五 P-D-6 落地硬閘（Q-M2） |
| `is_corner`／`W_prev` | `True`／`0.0` | 第 1 宗 |
| `a` | `round(分攤登記面積_m2 + 面積_m2, 2)`·源 **`temp_parcels`** | **reviewer R3**（PK 現用 `幾何面積_m2` ⇒ 口徑二次分岔；實測 Δa ∈ [−2.53, +0.72]）。取值走防 KeyError 慣例 `tp.get('分攤登記面積_m2', tp.get('面積_m2', 0))` |
| `avg_depth`／`min_width` | **顯式自 snapshot** `街廓分配深度_m`／`get_min_lot_size(category, 正面路寬)` | **reviewer W-5**：PK 時段 `f3_alloc_depth_by_label`／`f3_min_width_by_label` **尚未鋪底**（`stepg:196-202` 才寫）；fallback 差額 R6 **6.05㎡**、R3 4.89㎡ |
| `B`／`C`／`price` | `_compute_v3_finance`（P-0a·單一真相源） | 避第三份抄寫（`#20`） |

### 3.2 loud raise 之**邊界**（Q-M4 裁）

- **raise**：`a`／`A`／`B`／`C`／`block_poly`／`d_hat`／`corner_pt`／`avg_depth`／`min_width`／
  `snapshot` 該塊節點 —— **任一缺值或 ≤0（面積/深度/寬度類）即 loud**。
- **不 raise**：`_solve_G_one` 之幾何二分法失敗 → 照走 `iterate_G_S`（Q-M4：與實配同側）。
- **不 raise**：`side_mid` 為 None（該側無 SIDE_LINE）→ 該側本無街角、PK 不會問到；
  若仍被問到＝上游 bug ⇒ **raise**（此為輸入缺值）。

### 3.3 P-A 之測（未接線階段即可跑）

| 測 | 內容 | 期望 |
|---|---|---|
| A-1 | `_corner_first_lot_G` vs `_solve_G_one` 直呼（同參數） | **逐位全等**（證同一路徑·非平行式） |
| A-2 | 左右端 `S_max_limit` **不同源** | 對同塊左右各解一次，斷言取用之 `S_max` 分別 == `S_block_max` / `_oblique_s_max`（B-6 反例守衛） |
| A-3 | 缺值 loud | `a=None`／`depth=0`／`min_width=0` 各觸 `RuntimeError`（no-silent-fallback） |
| A-4 | fallback 覆蓋 | 餵不可解幾何（`block_poly` 退化）→ **不 raise**、`solver_label == '代數迭代(fallback)'`（Q-M4） |

---

## 四、P-B／P-C：接線（真 G 驅動達標）＋**app 鏡射同 commit**

### P-B（純加性·baseline 零 diff）

1. **`run_corner_pk` 增 `snapshot`**（keyword-only、**無預設** ⇒ 漏傳即 `TypeError`·非靜默）。
   **9 個呼叫端同改**（reviewer 更正 plan v1 之「6」）：

   | # | 檔:行 |
   |---|---|
   | 1 | `verify/run_verification.py:423` |
   | 2 | `verify/wd3_fragment_geom.py:93` |
   | 3 | `verify/wd4_tier_list.py:187` |
   | 4 | `verify/wg_g1_smoke.py:56` |
   | 5 | `verify/wg_g2_smoke.py:35` |
   | 6 | `verify/wg_g3.py:81` |
   | 7 | **`verify/tools/y_dump_diff.py:59`**（plan v1 漏） |
   | 8 | `verify/probes/probe_corner_trueG.py:93`（T1 探針·同步改，使其與生產同源） |
   | 9 | **`app.py:14927` 自有 PK**（＝第 9 條路徑·**非** `run_corner_pk`·見下 B-3） |

   靜態閘：新增 `run_all` 檢核「全倉 `run_corner_pk(` 呼叫端數 == 8 且**全部**帶 `snapshot=`」
   （AST `Call` 掃描·防日後漏改）。

2. **`_pk_one_side_v12` 增 `require_g_map: bool = False`**（reviewer **B-1** 修法：
   raise **不得**無條件加在 `_pk_one_side_v12`，否則直接炸掉圖 8 golden＝`run_all` 第一道閘）。

   同時**消滅 or-鏈之 falsy 陷阱**（`G=0.0` 現行被 `or` 跳過）：

   ```python
   pid = cand.get('暫編地號', '')
   if require_g_map:
       if pid not in g_values_map:
           raise RuntimeError(f"🔴 M-2/Q1：{pid} 取不到真 G（禁 fallback）")
       cand_G = float(g_values_map[pid])
   elif pid in g_values_map:      cand_G = float(g_values_map[pid])
   elif 'G_value' in cand:        cand_G = float(cand['G_value'])
   elif 'G_estimated' in cand:    cand_G = float(cand['G_estimated'])
   else:
       raise RuntimeError(f"🔴 {pid} 無任何 G 來源（禁靜默視為 0）")
   ```

   **零行為證明**：生產路徑 `g_values_map` 恆含全候選且值 ≥0.5（`estG` 之 `+0.5`）⇒ 從不落 falsy；
   golden 之 `g_values_map={}` ⇒ 落 `G_value=1e9` ⇒ **與現行同**。**禁改兩顆 golden fixture**
   （`tests/test_corner_priority_golden.py:63,69,79`／`verify/app_harvest.py:174`＝手冊語意錨）。

### P-C（行為改：達標改吃真 G）

1. `run_corner_pk` 內：對每候選另算 `_G_true = ns["_corner_first_lot_G"](...)`；
   `g_values_map` 改餵 **`_G_true`**，並以 `require_g_map=True` 呼叫 v12。
2. **`G_estimated`／`G_value` 保留**（reviewer **B-2**：`_estimate_G_for_qualification`
   有 **3 真消費端**——`app.py:14870`(**live Streamlit UI**)／`selection_pipeline.py:290`／
   `app_harvest.py:150`——**不刪**）。診斷表**新增 `真G(㎡)` 欄**、`G估(㎡)` 欄**語意與值皆不動**。
   ⇒ 副效果：`run_verification.py:451-456`「G估 欄變動 N 格（期 0）」**續綠**（Q-M3 之紅只剩欄集）。
3. **落地一致性硬閘（Q-M2 裁·本 plan 之對價）**：見 §五 P-D-6。

### B-3｜**`app.py:14860-14939` 必須同 commit**（reviewer 判**致命**）

`app.py:14927` 有**自有** `select_corner_lots_both_sides_v12` 呼叫，
`:15050` 寫 `f3_corner_winners`、`:15081` 寫 `f3L_forced_offset`——**正是 §7 引擎 ctx 之來源**
（`app.py:9106-9107`）。只改 harness ⇒ **harness 綠、真 app 之 R5左/R2左/R3右 仍是強制抵費地、
918.50㎡ 仍鎖住** ⇒ 本波首要驗收讀數**在 KL 的 UI 上不會成立**。

⇒ `app.py:14860-14939` 與 `selection_pipeline.py:316-370` **逐項同改、同 commit**。

**欄集結構閘（新增·`run_all`）**：
```
app `_candidates` 之鍵集  ==  selection_pipeline `_candidates` 之鍵集
```
以 **AST 取兩處 dict literal 之 key 字面**比對（非執行期比對——app 段在 `main()` 內、
headless 不執行）。破 ⇒ FAIL 並列出差集。**理由**：B-3 之根因即「兩份鏡射碼無機器看守」。

---

## 五、P-D：**M-2(c) 合併自救**（主體）

### D-1 循環相依之解：**兩趟定點**（技術決·CC 自理）

「同歸戶於其他可建築街廓之**未達分配面積地**」之判準需 **G**，而 G 由 Step G 產、
Step G 又吃 PK 之 winner ⇒ 循環。canonical M-1 已定時點為「**投影序算 G 後、剔除前**」
⇒ 自救之**判料**取自 trunk A，**結果**回饋 PK。故：

```
趟0：run_corner_pk(rescue=None)                     ← Q1 真 G 閘·無自救
   → run_step_g(winners₀, forced₀, build_parcels)   ← trunk A₀
   → U₀ = { 宗 : G(A₀) < MinA[所屬街廓] }            ← 與 wf_f0._decide 同一述詞
趟1：run_corner_pk(rescue_ctx={U₀, gid_map, mina, zone_price})
   → winners₁／forced₁／consumed registry
   → parcels₁ = build_parcels ⊖ consumed(全額者) ⊕ a′注入(winner) ⊖ 部分消費者之殘 a
   → run_step_g(winners₁, forced₁, parcels₁)        ← trunk A₁
定點檢查：U₁ = {G(A₁) < MinA} → 若「由 U₁ 導出之自救決策」≠「由 U₀ 導出者」→ 再迭一趟
         上限 3 趟；仍不收斂 ⇒ **loud raise**（禁靜默取末趟）
```

- **封裝**：趟0/趟1 全在 `selection_pipeline.run_corner_pk` 之**外**（`run_verification` 層），
  但以新 module `verify/m_rescue.py` 承載決策邏輯，使 8 個 `run_corner_pk` 呼叫端
  **除加 `snapshot=` 外零改**（未傳 `rescue_ctx` ⇒ 走趟0 語意＝Q1-only）。
- **`app.py` 對應**：app 之 Step G 在 PK 之後，本即天然兩趟結構；
  app 端接 `_m_rescue_plan`（由 §7 引擎 ctx 回灌），**不在 app 重寫決策**（CLAUDE.md §7 禁 fork）。
- **成本**：每情境多 1 次 `run_step_g`（趟0），實測列 P-G。

### D-2 自救母體（M-2 原文·逐字對映）

對每個「真 G < 街角規定面積」之跨占候選 `cand`（gid＝`g`、所在塊＝`b`）：

```
救援池(cand) = { s ∈ build_parcels :
                 gid(s) == g                      # 同歸戶
                 ∧ blk(s) != b                    # 「其他」可建築街廓
                 ∧ 可建築(blk(s))                  # 「可建築街廓」
                 ∧ s ∈ U                          # 「未達分配面積地」
                 ∧ s ∉ consumed }                 # B-5 單一結算帳
```

**Q2 硬約束（裁定 §2.2·canonical 原句）**：`E-1.7 真交集 > 1.0㎡` **絕對地板照舊**——
自救**僅解 G 門檻這一關**。E-1.7 落在 `app.py:8402-8403`（`select_corner_lots_both_sides_v12`
之 Step 1 分流）、**先於** `_pk_one_side_v12` ⇒ 依 reviewer **W-6**，Q2 測項**落點上移**至
`select_corner_lots_both_sides_v12`（原 plan v1 落在 `_pk_one_side_v12` ⇒ **套套邏輯**）。

### D-3 注入量：**只取所需**（Q3）＋**重跑迭代**（reviewer **W-2**）

**禁** `缺口 ÷ 固定比率`——G 對 a **次線性**（reviewer 實測 `G/a ∈ 0.5594–0.5828`）。

```
def _min_a_prime_for_corner(cand, threshold, supply):
    """二分搜尋最小 a′ 使 _corner_first_lot_G(a + a′) ≥ threshold。
       每次評估**重呼 `_corner_first_lot_G`**（＝與閘/實配同一 solver·單一真相源）。"""
    lo, hi = 0.0, supply
    if G(a + supply) < threshold: return None, G(a+supply)   # 供給不足·全額仍不夠
    for _ in range(40):                       # tol 0.01㎡
        mid = (lo + hi) / 2
        if G(a + mid) >= threshold: hi = mid
        else:                       lo = mid
        if hi - lo < 0.01: break
    return round(hi, 2), G(a + hi)
```

- **單調性**：`G` 對 `a` 嚴格遞增（G 公式 ＋ `solve_G_binary` 幾何驅動）⇒ 二分合法。
  **加驗**：迭代前先斷言 `G(a) < threshold ≤ G(a+supply)`（區間有解），破即 loud。
- **a′ 換算**：`a′ = a_源 × p(源zone) / p(目標zone)`＝`wf_f2.a_prime_mode1`（**模式一**·
  同歸戶跨街廓必有目標地）。**供給** ＝ Σ 救援池之 `a_源`（依 D-4 序逐宗取用）。
- **部分消費**：某源宗只被取用 `x < a_源` ⇒ registry 記 `(pid, x)`，該宗之
  `分攤登記面積_m2 + 面積_m2` 相應扣減 `x`（**非**整宗移除）。餘額走 M-3(i)②/③（§六）。

### D-4 **街角 vs 街角**之全域決定性序（reviewer **B-5**·M-3(ii) 解不了）

reviewer 真資料：`G011` 之 `628-42(1)@R2左` ↔ `628-42(2)@R3右` **對稱互救** ⇒ 幻影 **+161.80㎡**；
`G030` 同構 ⇒ **+98.00㎡**。M-3(ii) 定的是「街角 vs M-1」序、**非**「街角 vs 街角」。

**決定性序（技術補注·KL 可否決）**：
1. 蒐集全案**所有**待救街角端 `(blk, side)`，計其 `缺口 = 街角規定面積 − 真G(最強候選)`；
2. **排序鍵**＝`(缺口 ↑, blk 字典序 ↑, side ∈ {'左'<'右'})`——**缺口小者先取**；
3. 依序貪婪配給；每源宗之 a 由 registry 扣減，**至多消費一次**（partial 亦記帳）；
4. 街角端內部之源宗取用序＝`(a_源 ↓, 暫編地號 ↑)`（大者先·減少被拆宗數）。

**理據**：上位精神「街角強制抵費地為**最後手段**」之操作化＝**forced 端數最小化**；
供給受限時「缺口小者先」即該目標之貪婪最優。**全案零塊名／零側別字面／零案例常數**（泛用四約束）。

> ⚠️ **標為技術補注**（同 `M-3(ii)`／`Q3-tb` 位階）：若 KL 認為序應由法定優先權指數或
> 街廓位階決定 ⇒ 單點改 `_RESCUE_ORDER_KEY` 即可（設計為單一可換之 key 函式）。

### D-5 **consumed-lot registry**（跨階段單一結算帳·PK→F.0→F.2→F.4）

```python
# verify/m_rescue.py
class ConsumedRegistry:
    """跨階段單一結算帳。key＝暫編地號；value＝已被消費之 a（㎡·可 < 原 a ＝部分消費）。"""
    def claim(self, pid, amount, *, stage, target): ...   # 超額 claim ⇒ loud raise
    def remaining(self, pid): ...                          # 原 a − 已消費
    def frozen(self): ...                                  # 供 F.0/F.2/F.4 唯讀查詢
```

- **materialisation 落點**＝**趟1 之 `parcels₁` 建構時**（PK 決策 → 立即物化）：
  - 全額消費 → 該宗自 `parcels₁` **移除**；
  - 部分消費 → 該宗 `面積_m2` 扣減殘量差（四欄面積鐵律：`分攤登記面積_m2` 為唯讀 ⇒
    扣減一律落 **`面積_m2`** 累加器欄；若扣減後 `a ≤ 0` ⇒ 視同全額、移除）；
  - winner 宗 `面積_m2 += Σa′`（模式一換算後）。
- **源宗移除時機**＝`run_step_g(trunk A₁)` **之前**（否則源塊重複配地＝守恆破）。
- **下游唯讀**：`wf_f0._decide`／`wf_f2._decide`／`wf_f4` 之候選母體一律先 `∖ registry.frozen()`；
  `registry.claim` 於 F.0/F.2/F.4 再被呼叫時 **超額即 loud raise**（雙重消費之機器看守）。
- **守恆閘（新增·`run_all`）**：
  `Σ(registry 消費量) == Σ(winner 宗 面積_m2 增量 ÷ 換算比) `（逐 gid 對帳·tol 0.01㎡），
  且 `每塊 ΣG + 池 == 街廓 DXF 面積`（既有閘·續綠）。

### D-6 **落地後一致性硬閘**（Q-M2 裁·本 plan 對「樂觀」之對價）

趟1 之 `trunk A₁` 產出後，對**每個**街角 winner：

```
if 實配 G(A₁, winner) < 該端街角規定面積:
    raise RuntimeError("🔴 M-2/Q-M2 一致性破：{blk}{side} winner {pid} "
                       "過閘(樂觀真G={g_opt}) 但實配 G={g_real} < 規定面積 {thr} —— 停機上呈")
```

**非** warning、**非** 自動降級為 forced（後者會靜默吃掉「口徑偏寬」之證據）。
此閘同時是 Q1 鐵律三「閘／實配口徑須一致」之機器證明。

> **預期**：T1 實測樂觀 vs 實配之最薄餘裕 `628(5)@R1右` 為 **+13.51**（樂觀）／**+0.84**（實配），
> 二者**同號** ⇒ 本閘預期綠。若紅 ⇒ 樂觀口徑於本案不成立 ⇒ **停機上呈 Q-M2 重裁**。

---

## 六、P-E：M-1 ＋ M-3 三段

### E-1 落點與母體（reviewer **B-4**：plan v1 之落點是死碼）

`verify/wf_f2.py:40` `F2_GROUPS` 為**硬編 5 群**、`:143-144` 只對這 5 群呼叫 `_decide`
⇒ M-1 母體（`qual` 空）**永不進入**。且 `F2_GROUPS` 係案例常數、違泛用四約束。

**expand-contract 三段式**（`expand-contract-refactor` skill）：

| 段 | 作法 | 綠判準 |
|---|---|---|
| **expand** | 新增 `_f2_groups(byg, mina)` 現算分流：`multi = {gid: ≥2 塊}`；`qual 非空 → F2 既有`／`qual 空 → M-1 新路徑`。**同時保留** `F2_GROUPS` 並斷言 `set(現算之 F2 分支) == set(F2_GROUPS)` | 斷言綠＝證等 |
| **migrate** | `:143` 迴圈改吃現算集；`:146` 之 `raise("無達標塊，不應在 F.2 名單")` 改為**分流**（`qual` 空 → M-1、不再 raise） | `run_all` FAIL 集合不新增名目 |
| **contract** | 證等後**整段刪** `F2_GROUPS` 常數（grep 證零殘留） | grep 零命中 |

⚠️ **若 expand 斷言破**（現算集 ≠ 5 群）⇒ **不自行放行**：印出差集、**loud FAIL**、
入報告🚩上呈（可能意味現行 5 群名單本身即含案例假設）。

### E-2 M-1 演算法（canonical §一·目標函數＝**保住原位次分配處數最大化**）

對每個 `qual` 空之 gid（多街廓均未達）：

```
cur[b]  = Σ G(trunk B) of gid 在塊 b            # 現況
need[b] = max(0, MinA[b] − cur[b])              # 缺口
供給者  = cur 最小之塊（「最小者優先」）；供給 = Σ a_源 於該塊
受益者候選 = 其餘塊，依 need ↑ 排序             # 貪婪最大化「處數」
tie（同處數多解）→ **優先救較大者**（Q3-tb 補注）
```

- **只取所需**（Q3＝同 M-3(i)①）：每受益塊注入量由 **E-3 之重跑迭代**定，非比率折算。
- **部分拆分不可行** ⇒ 退路：整筆（連同乙′）併入**最大之丙**（canonical §一）。
- 「不可行」之定義（顯式）：`供給 < min(need[b])`（連最省的一處都補不起）
  **或** 拆分後供給塊自身之殘 a 使其**再多失一處**（即拆分之處數增益 ≤ 0）。

### E-3 注入量之**重跑迭代**（W-2·非比率折算）

M-1 受益宗**非**街角第 1 宗 ⇒ 其 G 由整條推進序列決定、無法以單宗式求。
⇒ **批次外迭代**（單趟即算全部群，成本 O(迭代數) 而非 O(群數×迭代數)）：

```
guess[t] = need[t] / (G/a)(t, trunk B)            # 初值（僅初值·允許比率）
for it in range(6):
    parcels' = 注入 guess → run_step_g → 量 G_real[t]
    若 ∀t: MinA ≤ G_real[t] ≤ MinA + tol_over  → 收斂、break
    對未達者 guess[t] *= (need 修正)；對超額者以割線法回縮        # 只取所需
else: raise RuntimeError("🔴 M-1 注入量 6 趟未收斂 —— 停機（禁取末趟）")
```

- `tol_over` ＝ 0.5㎡（「只取所需·不多取」之可操作容差；**明列於報告**）。
- **既有硬閘續用**：`wf_f2.py:238-241`「目標宗灌後 G ≥ MinA」為最終看守。

### E-4 M-3(i) 三段之**顯式測項**（canonical §三 **plan 必須含**）

| 段 | 測項 | 落點 | 判準 |
|---|---|---|---|
| **① 補足量** | 街角自救之注入量 ≤ 補足街角規定面積所需之最小量＋0.01 | `verify/fixture_m_rescue.py::test_topup_minimal` | 合成 gid：源 a 遠大於缺口 ⇒ 只取缺口 |
| **② 餘額他併** | ① 後餘額**先**依 M-1 往同歸戶其他較大地 | `::test_remainder_to_m1` | 合成：餘額恰可救一塊 ⇒ 該塊達 MinA、街角**不再多吃** |
| **③ 餘額回流街角** | ② 後仍任一塊未達 MinA ⇒ 餘額**亦併入街角地** | `::test_remainder_back_to_corner` | 合成：餘額不足救任何塊 ⇒ 全數回街角、源宗全額消費 |
| **M-3(ii)** | 遠地同時可救街角與 M-1 → **街角優先** | `::test_corner_precedence` | 以優先序旗標 `_M3II_CORNER_FIRST` 實作·**單點可關**（KL 否決即改） |

**fixture 出處紀律**（`fixture-provenance`）：三段之期望值**不得**由新碼跑一次回填。
合成 fixture 之期望以**手算**列於檔頭註解（面積/單價皆為合成常數·非案例值）。

---

## 七、P-F：M-4 末端塊交互驗證（**實測·非宣稱**）

canonical §四【必辦】：末端保留／N0-20 族（`_end_band`／`_end_gate`／`_end_region_R`／
E3 `_reshape_block` fallback）**不得被 M-1／M-2 吞掉或跳過**。

| # | 驗證項 | BEFORE 實測（`df9834c`·本波前一單元） | AFTER 判準 |
|---|---|---|---|
| **F-1** | 3.5m 末端保留觸發集 | **唯 R6 左端**·未臨正街 **85.706㎡**·末端帶 `s∈[0, 3.5114]`（倉內 T2-DIAG：R6 池帶 2 片 `[3.6068, 36.4339]`／面積 `[85.7064, 1651.0218]`） | 不得**無故**消失或位移；變動須逐項歸因於 winner 更正之合法連動並載明 |
| **F-2** | `_end_gate` 之 `_cond1` | `_cond1 = not fo['{side}_has_side']`（`wf_f4:1324-1325`；`_end_gate` 在 `:1338`——**reviewer 更正** plan v1 之 `1311-1324`） | M-2 改 `forced_offset`／`corner_min_area`、**非** `has_side` ⇒ `_cond1` **逐塊逐側全等**·斷言之 |
| **F-3** | `fixture_end_reserve.py` | **12 檢核項**（左 6＋右 6·全 Δ=0）——**reviewer 更正** plan v1 之「10 斷言」 | **必續綠** |
| **F-4** | `fixture_end_fallback.py` | 左右雙向真檢（驗0 band/frag/R_end＋②帳池==幾何池＋③非疊＋④G守恆） | **必續綠** |
| **F-5** | E3 `_reshape_block` fallback | 全案 **latent**（未觸發） | 仍 latent；**若觸發 ⇒ 誠實報**（含觸發塊/側/量） |
| **F-6** | **交互**：被 M-1/M-2 消費之源宗若為某塊**末宗** | BEFORE 逐塊列末宗清單 | 消費後末宗改變 ⇒ 重列 `_end_band` 窗與 `cond2` 半平面量、**逐項歸因**（`#25`：錨未參數化之維度零舉證力 ⇒ 左右**兩側各驗**） |

---

## 八、P-G／P-H：驗收與**合法重定錨**

### P-G 首要驗收讀數

重跑 `probe_capacity_decomp` 家族，報 3.5m
**「合併後仍需調配之群數」vs「可容上界」**、**「9 戶差 2 戶」是否消失**。

#### BEFORE 實測（`WV_CAPDECOMP=1 python verify/probes/probe_capacity_decomp.py`·log＝`verify/out/M_before_capdecomp.log`）

| 情境 | 需求群 | [甲現況] 可容上界 | [乙釋forced] | [丙釋碎片] | 窮舉狀態 |
|---|---|---|---|---|---|
| **0m** | **6** | 逐塊 `R1 4／R2 3／R3 2／R4 4／R5 0／R6 0`·**和 13** | 和 13 | 和 14 | **可行**（已窮舉·出指派） |
| **3.5m** | **9** | 逐塊 `R1 0／R2 2／R3 1／R4 4／R5 0／R6 0`·**和 7** ⇒ **短 2**（＝「9 戶差 2 戶」） | **和 12** | 和 7 | **`space 559872>300000·未窮舉`** |

3.5m forced 三端逐位（與盤點表 §〇 及 T1 靶**逐位吻合**）：

```
R5 左  300.52㎡  s∈(0.269, 8.677)   s_rel=0.031  ←left_forced_offset
R2 左  309.05㎡  s∈(0.268, 8.716)   s_rel=0.034  ←left_forced_offset
R3 右  308.93㎡  s∈(88.074, 96.803) s_rel=0.96   ←right_forced_offset
                                          Σ = 918.50㎡
```

⇒ **成因鏈由本讀數獨立確證**：甲（現況·含 forced 鎖定）**7 < 9**；
乙（釋 forced 918.50）**12 ≥ 9**；丙（只釋碎片）仍 **7** ⇒
**缺口之唯一有效解在 forced 釋回、不在碎片**——即 M-2(c) 之靶。

⚠️ **reviewer W-7 誠實註（必載於報告·已由上表 BEFORE 實測坐實）**：
「12 ≥ 9」係**鬆弛上界**，且 log **自述** `窮舉=space 559872>300000·未窮舉`
（0m 之「可行」則係**真窮舉**並出具指派 ⇒ 二情境之證據強度不同級、禁並列引用）；
且 M-1/M-2 會改變「需求群」集合本身（9 會動）⇒ **前後不可當獨立對比**。
報告須**同時**列「需求群集合之**前後成員差**」（BEFORE 3.5m 需求群＝
`{G003, G004, G014, G015, G016, G018, G020, G025, G033}`·見 consume matrix），
**不得只報數字**。

附帶讀數：三端「⚠️強制抵費地」是否轉為地主宗（＝918.50㎡ forced 鎖定是否釋回）——
逐端報 **缺口是否補足／由哪些源宗補**（T1 靶：R2左 8.65／R5左 52.56／R3右 103.66）。

`W-F F.4` 現有殘紅（3.5m E2 結構性不可行·上界 7 < 需求 9）若遷移 ⇒ **誠實定位**
（既有 or 新引入），**禁**以「本波前即紅」帶過。

### P-H 合法重定錨（**獨立 commit**·Q-M3 裁）

1. **BEFORE 釘 `df9834c`**——所有前後值以之為「前」。
2. **禁改 `skip_cols`**（`run_verification.py:441-444`）、**禁改** `_exp_gd`、**禁退役**任何閘。
3. 先出**逐格歸因表**（每一格差異 → 歸因於 {Q1 口徑／M-2 winner 更正／M-1 搬移／連動} 之一），
   **無法歸因者 ⇒ 停機**，不得重烤。
4. 歸因表過後，**單獨 commit** 執行 `WV_BAKE` 重烤，commit message 標
   `rebake(裁定M): 域裁後果之合法重定錨`，並於報告**獨立節**載**前後值**：
   `F1_REVERIFY`（`wf_f4:61`）／UC9898 R1左 3.5m winner／
   `第 1 宗街角地指配結果_退縮*.csv`／街角三指數 golden。
5. ⚠️ **golden 圖 8（0.6685／0.3315）為手冊語意錨**——**若變動＝實作 bug、非合法重定錨**。
6. **V2/V3/V8/V9 維持「未驗·待波末重烤」**（spec §五.4）。
7. **`docs/specs/W-G.4_CC交辦_v3.md:105`「3.5m forced 擴為 5」已過期**（現況 3 端；
   628(5) 為 **+0.84**、628-18(1) 為 **+8.65** 過關）——引用前須標作廢（reviewer §二 末）。

---

## 九、泛用四約束**逐項自查**（canonical §五.1）

| 約束 | 本 plan 之新碼 | 自查 |
|---|---|---|
| **禁硬編塊名** | `_corner_first_lot_G`／`m_rescue`／M-1：全部 by `blk` 變數 | ✅；且 **P-E contract 段主動刪除既有** `F2_GROUPS` 案例常數（淨改善） |
| **禁硬編側別** | 左右差異僅二處且**參數化**：`S_max_limit`（`S_block_max` vs `_oblique_s_max`）、`d_hat` 正負 | ✅ 由 `side` 參數驅動；A-2 測守衛 |
| **禁硬編常數** | `MinA`／街角規定面積／深度／最小寬**一律現算或自 snapshot**（W-5）；`tol_over=0.5`／`E1_MARGIN` 型容差**明列於報告** | ✅ |
| **換案仍成立** | 判別走資料驅動旗標（`has_side`／`forced_offset`／`可建築` 分類／`gid`） | ✅；`_RESCUE_ORDER_KEY` 為單一可換 key 函式 |

**既有違例之處置**：`wf_f4:61 F1_REVERIFY`／`E0_EXPECT`／`E2_NAMED`／`COMP_EXPECT` 為
**錨對拍常數**（非決策常數）⇒ 本波**不動**（動之即毀對拍能力）；`F2_GROUPS` 為**決策常數** ⇒ **刪**。

---

## 十、⛔ 停機條件（真域邊界·純技術自理）

| # | 觸發 | 動作 |
|---|---|---|
| S-1 | **D-6 落地一致性閘紅**（樂觀過閘但實配 < 規定面積） | 停機上呈 **Q-M2 重裁**（含逐端 樂觀G/實配G/門檻） |
| S-2 | **M-3(ii) 被實測打破**（遠地救街角反使處數減少） | 停機上呈（canonical §五.5） |
| S-3 | **M-2 與既有街角雙條件裁定衝突**（E-1.7 須放寬方可行） | 停機上呈（canonical §五.5·Q2 前哨） |
| S-4 | **E-1 expand 斷言破**（現算 F.2 分流集 ≠ `F2_GROUPS`） | 印差集·loud FAIL·報告🚩上呈 |
| S-5 | **兩趟定點 3 趟不收斂** ／ **M-1 注入 6 趟不收斂** | loud raise·停機（禁取末趟） |
| S-6 | **P-H 有無法歸因之 baseline 差異格** | 停機·**不得重烤** |
| S-7 | **圖 8 golden 變動** | ＝實作 bug（非重定錨）·停機修碼 |

其餘（序之選擇、容差、迭代法、模組切分）＝**純技術·CC 自理**，於報告載明。

---

## 十一、次步

1. 本 plan **立即送 reviewer**（`redistribution-reviewer`·獨立復現）——**不停等 KL**。
2. reviewer 綠 → 依 §一 七步 commit 序施工。
3. 每步 `py_compile` ＋ 關鍵 grep ＋ `run_all`；**FAIL 集合不得新增名目**。
4. 報告本體寫 `docs/reports/W-G.4_裁定M_施工報告.md`；聊天＝ping。
5. **未 push 不報收官**（`git rev-parse origin/wip/s1-endpart` 須含該 commit）。
