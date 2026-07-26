# W-G.5 裁定 N · **乙案** — 施工 plan **v2**（P-1～P-10）

> **取代 plan v1**（`docs/specs/W-G.5_裁定N_乙案_plan_v1.md`·**未施工即被駁**）。
> **canonical**：KL 2026-07-26 二輪定案（N-2′／N-8／N-9／N-10／N-11／N-12）。
> **基準倉態**：`origin/wip/s1-endpart = effc29d`。**引擎零改動**（`git diff HEAD -- app.py verify/` 空）。
> **v1 → v2 之由**：reviewer 三 BLOCKED ＋ 七 WARNING（審查紀錄見 §〇.1）。
> **⛔ P-H 維持凍結。plan 未過 reviewer 不得動引擎。**
> **行號紀律**：全文**符號名＋可自癒 grep**（`CLAUDE.md` 🔒 行號衛生）。

---

## 〇.1　v1 被駁之三處（**逐項已自行 grep 復現·非採信 reviewer 說詞**）

| # | v1 之錯 | 我的復現證據 | v2 處置 |
|---|---|---|---|
| **B-1** | v1 §2.2 稱「唯一算式改動＝`diff` 加常數」。**錯**：`solve_G_binary` 收斂後之 `final_cut`／`area_conv`／`cut_coords` **全部**來自 `_block_strip`（strip-only），常數項只進 G 不進幾何 ⇒ 帳-幾何脫鉤 | `sed -n '7783,7795p' app.py` → `final_cut, _final_area = _block_strip(...)`；`area_conv = float(_final_area or 0.0)`。守恆閘 `_resid_wd2 = round(_sum_G_blk + _pool_total_blk − blk_area, 2)`，`_tol_blk = n_lots × 0.015`（`grep -n "_resid_wd2 = round" verify/stepg_pipeline.py`）⇒ R6 13 宗 tol 僅 0.195㎡、殘差將達 **+85.7064**（逾 440 倍） | **§二重寫**：改傳**多邊形**、收斂後 union 進 `final_cut`（見 §2.2） |
| **B-2** | v1 §六 只列 2 個末端族消費者 | `grep -rn "_end_band\|_end_region_R" --include=*.py .` → 另有**生產碼** `_place_pool_parcels` 內 `_band = _end_band(...)`（`grep -n "_band = _end_band" app.py`）、`verify/fixture_end_reserve.py`（`:60` assert／`:143` 呼叫）、`_WF_NS_NAMES` 之 `"_end_region_R"`（`grep -n '"_strip_axis", "_end_region_R"' app.py`）、`verify/run_verification.py` 引用 | **§六重寫**＋新增 §6.2 範圍待裁 |
| **B-3** | v1 §8.1 由「三源皆落 47.4–47.7、甲式 44.59 離群」推論深度＝FRONT 法向縱深 | ①我自己的 `_front_normal_depth` 取 `max(xs)`，而 N-12 明寫**最小值** ⇒ **實作與定義相反**；②KL 之 166.57 ＝ `_end_band(p1, 3.5)` 之輸出（**ALLOC 軸**）⇒ 非獨立源；③FRONT/ALLOC 夾角 4.6°（cos 0.9968）⇒ 兩軸差 ≈0.15m **小於**各源散布 0.27m ⇒ **原理上無鑑別力** | **§八重寫**：撤回該推論、四讀併陳、深度口徑**上呈 KL**；探針已修（`max`→`min`＋兩讀併印） |

**另**：v1 唯一自標「BLOCKED 級待驗」之 §2.2 定點斷言，reviewer 逐行驗證**成立**
（每輪重算 ✅／無跨輪 state ✅／clamp 後單調性 ✅）⇒ v1 §十二第一條停機條款**不觸發**。
**教訓記帳**：我把旗插在對的地方，真正的 BLOCKED 卻在沒插旗處——
「自評風險點 ≠ 真風險點」，此即 reviewer **獨立復現**之價值（`CLAUDE.md` 🔒 自評 gate 綠不可替代）。

---

## 〇.2　乙案要旨（不變）

起算點**不動**（`corner_pt = p1`·S 恆自 FRONTLINE 端點 p1 起量、恆非負），改為**迭代式加常數項**：

```
未臨正街真幾何面積 + 臨街帶面積(S) = 該宗應分配面積(G)
```

⛔ 原 N-1／A 族／A′ 族／B1 **整條作廢**（v1 §〇 之對照表仍有效，沿用）。

---

## 一、P-1　規格定稿（純文件·零碼）

同 v1 §一，**增補**：
6. 明文寫入「**N-2′ 取代補丁十『乙』**」——`_end_region_R` docstring 現載
   「未臨正街『面積實體』＝ `frag_poly`；**半平面僅判別、不供面積**」（KL 補丁十裁·
   `grep -n "半平面僅判別" app.py`）。乙案改採**半平面供面積**（`block∩{s<0}`）
   ⇒ **與該既有裁定直接衝突，不得默默切換**。
   **理由**（供 KL 覆核）：`frag` 係**分配後**才存在之產物，原位次階段取不到；
   而 `block∩{s<0}` 於分配前即可由純幾何算出——乙案之常數項須在**迭代時**就位。
7. **「未臨正街面積」兩值並存之釐清**（reviewer W-9）：

| 值 | 出處 | 語意 |
|---|---|---|
| **85.7064** | `block∩{s<0}`（本波採用）；`verify/wf_f1.py` 註之 R6 池 `parts=[776.9034, 85.7064]` | 半平面真幾何面積 |
| **85.66** | `verify/wd3_fragment_geom.py`／`run_verification` 之遞補錨 | **碎片**（frag）面積 |

R1 同型：`WEDGE_AREA_ANCHOR = 5.30` vs `block∩{s<0}` = 5.3255。
⇒ 規格須明記二者**非同物**，並指定各閘用哪一個。

---

## 二、P-2　乙案迭代器（**v2 重寫·B-1／W-5／W-6／W-7**）

### 2.1 需改之符號（**7 處·v1 只列 1 處＝W-6**）

| # | 符號 | 自癒 grep | 改法 |
|---|---|---|---|
| 1 | `solve_G_binary` | `grep -n "def solve_G_binary" app.py` | 加參數＋`diff` 加常數＋**收斂後 union 幾何** |
| 2 | `_solve_G_one` | `grep -n "def _solve_G_one" app.py` | 薄殼轉手＋**loud guard 置於 try 之外**（W-5） |
| 3 | `app._solve_one`（`main()` 閉包） | `grep -n "def _solve_one" app.py` | 轉手 |
| 4 | `stepg._solve_one` | `grep -n "def _solve_one" verify/stepg_pipeline.py` | 轉手 |
| 5 | `iterate_G_S` | `grep -n "def iterate_G_S" app.py` | 常數>0 ⇒ **loud raise**（§2.4） |
| 6 | `app._advance_block_with_split` 左組迴圈 | `grep -n "def _advance_block_with_split" app.py` | 控制流（§2.5） |
| 7 | `stepg._advance_block_with_split` 左組迴圈 | `grep -n "def _advance_block_with_split" verify/stepg_pipeline.py` | 同上 |

（`_corner_first_lot_G` 見 §2.6，另計。）

### 2.2 `solve_G_binary` 改動（**B-1 修正·核心**）

**參數**：`unfront_poly=None`（shapely Polygon·**非 float**）。
面積由函式內部自 `unfront_poly.area` 取，**禁另傳 float**（避免帳／幾何兩個真相源）。
預設 `None` ⇒ 常數 0 ⇒ **既有呼叫零行為變更**（V1 驗收）。

```python
_U_area = float(unfront_poly.area) if unfront_poly is not None else 0.0
...
# 迴圈內（唯一算式改動·area_geom 維持 strip-only）
diff = (area_geom + _U_area) - G_target
...
# 🆕 收斂後（B-1）：把常數項之**幾何**併入回傳物，使 G 與幾何同一物
final_cut, _final_area = _block_strip(block_poly, d_hat, baseline_pt, _S_cut, ...)
if unfront_poly is not None:
    final_cut = unary_union([g for g in (final_cut, unfront_poly)
                             if g is not None and not g.is_empty])
    if final_cut.geom_type != 'Polygon':
        raise RuntimeError(f"🔴 solve_G_binary[{...}]：承接後幾何非單一 Polygon "
                           f"（{final_cut.geom_type}）——禁跳著掛（N-2′）")
    area_conv = float(final_cut.area)
else:
    area_conv = float(_final_area or 0.0)
```

⇒ `G ≡ area_conv` ⇒ `Σ(G−幾何) = 0` ⇒ **守恆閘不破**（B-1 解）。
⇒ V2「R6 池帶 2→1」成立（該片被 union 進宗地幾何、不再是池片）。

**已復現之前提（reviewer 逐行驗·我覆核同意）**：
bisect **每輪重算** `G_target`（含 `−S_guess·l₂` 與 `Rw(S_guess)`）＝**已是定點求解**；
`_W_near` 只依 `baseline_pt`／`side_mid`（迴圈不變）＝無跨輪 state；
`rw_from_width` 單調非減 ⇒ `G_target` 非增 ⇒ `diff` 非減 ⇒ clamp 造出之平段位於根**右**側、
二分不會停錯。⇒ **不需另建定點迴圈**（KL「禁一階近似」之要求由現行結構已滿足）。

### 2.3 承接資格判定（**W-5 前置化 ＋ W-7 口徑釘死**）

🔴 **必須在進 bisect 迴圈前顯式判定**（W-5）：若根落在 bracket 外
（`_U_area > G_target(0)`），bisect 會於 `abs(S_max−S_min) < tol/1000` 靜默 break、
`converged=False`、`S_conv≈0`、`G_conv=last_G_target`——而 **`converged` 全庫只作顯示、無人 raise**
（`grep -rn "converged" --include=*.py .` → 僅 `'✅' if ... else '⚠️'` 兩處）
⇒ 靠 bisect 結果反推資格會讀到垃圾值。

**單一判定函式**（裁後單點可改）：

```python
def _carry_eligible(*, G_target_at_0, unfront_area, min_width, depth):
    """回 (ok, why)。**兩讀並存·KL 未裁**（§8.2）：
       弱（N-2′ 字面「吃不下」）：unfront_area ≤ G_target_at_0
       強（N-10 承接門檻）      ：G ≥ unfront_area + min_width×depth
                                 ⟺ area_geom ≥ min_width×depth  （∵ G = area_geom + unfront_area）
       強蘊含弱（min_width×depth > 0）——已驗兩分支。"""
```

⚠️ **v1 自裁「採強者」，v2 撤回**：N-2′ 字面只說「吃不下」＝弱條件；改用強條件**會改變承接者**
⇒ **意思決定·上呈 KL**（§十二）。v2 之**預設實作採弱條件**（忠於 N-2′ 字面），
`_carry_eligible` 之強條件分支同時寫好、以參數切換，裁後改一行。

**口徑釘死**（W-7）：強條件實作**以 `area_geom ≥ min_width × depth` 表述**
（等價但不經 G，避免實作者誤取 `G_target(0)` 或代數 fallback 之 G）。

### 2.4 `iterate_G_S` 代數 fallback（**W-5 之 guard 置放**）

該路徑無幾何 ⇒ `unfront` > 0 時**loud raise**。
🔴 **guard 不得放在 `solve_G_binary` 內**——`_solve_G_one` 之
`try: solve_G_binary(...) except Exception: pass`（`grep -n "except Exception" app.py` 於
`_solve_G_one` 段）會**靜默吞掉**、落到 `iterate_G_S`，85.71㎡ 無聲蒸發。
⇒ guard 置於 **`iterate_G_S` 內**（其呼叫在 try 之外）**或** `_solve_G_one` 之 try **之前**。
本 plan 採**兩處都放**（前者為真守衛、後者為早停）。

### 2.5 呼叫端控制流（**W-4 措辭修正**）

```
_pending_unfront_poly = block∩{s<0} 之多邊形（該塊·左側·資料驅動·N-5 禁寫死）
for entry in left_group:
    ok, why = _carry_eligible(...)
    if not ok:
        → 該宗退出原位次分配（loud 診斷·入 M-5 U₀·P-4）
        → _pending_unfront_poly 不變、continue        # 下一順位遞補到 p1 位置
    res = _solve_one(..., _unfront_poly=_pending_unfront_poly)
    _pending_unfront_poly = None                      # 已承接·後續宗恆 None
```

🔴 **W-4 更正**：v1 稱 app／stepg「**逐行同構**」＝**不實**。實測既有分歧：
stepg 有 `_W0_left/_W0_right/_W0_*_set/_Wfirst_*` telescoping 捕獲，app 無；
且 app 之 `_W_prev_left` 初值為 `(_left_buffer_S * _cos_dn) if _has_left_corner else 0.0`，stepg 為 `0.0`。
⇒ **改動點兩處皆在、但禁整段覆蓋**；須逐處手改、保留各自周邊碼。
（該分歧現為**惰性**：`W_prev` 在 `solve_G_binary` 迴圈內零消費——僅見於簽章／正規化／註解。
**不在本波處理**、列 backlog。）

**禁跳著掛**之結構保證：常數只交推進序當前首宗、退出者不保留、不跨宗跳過；
再加 §2.2 之 **union 須單一 Polygon** raise ⇒ 雙重保證。

### 2.6 `_corner_first_lot_G`（PK 假設第 1 宗）

同 v1 §2.6：加參數、傳真值、**產出前後對照表**；**winner 集合翻盤即停機上呈**。

---

## 三、P-3　N-11 三閘（**W-8 重寫夾具策略**）

### 3.1／3.2／3.3　三條件、N-9 寬度、N-12 深度

同 v1（條文不變）。**深度之量測範圍未定讞** ⇒ 見 §八、§十二（上呈項）。
實作**新增** `_front_normal_axis(d_hat, block_poly)`（取號指向街廓內），
**禁**沿用 `_strip_axis`／`alloc_normal_axis`（N-12 明令·兩軸斜交 4.6°）。

### 3.4 鑑別力（**W-8：v1 之錨不可用**）

🔴 **v1 以 R6 `628-4(1)`／`628-1(2)` 為主錨＝不成立**，三重理由（我已覆核）：

1. **KL 錨之 1.84 對不上**：`85.7064/47.705 = 1.7965`、`/47.437 = 1.8067`、`/44.59 = 1.9221`。
   **1.80 對得上、1.84 不**。且一階上界 `|ΔS| < U₀/D_eff = 85.7064/(692.05/14.75) = 1.827`
   ⇒ **1.84 越界**。
2. **`628-1(2)` 之「承接後 S≈1.27」是反事實值**：讀法(一)下該宗於資格判定即**退出**、
   終態不存在該 S。而 N-11 係**終態逐宗**閘 ⇒ **實跑永遠取不到 1.27**、期望值不可復現。
   （1.27 之來源可解釋：`(145.82 − 85.7064)/47.44 = 1.2673`＝該宗**若強行承接**之 S。）
3. **無鑑別力**：該二宗皆**中間宗** ⇒ N-11(2) 退化成 `S ≥ 3.5`；而 N-10 ⟺
   `area_geom ≥ 3.5×depth` ⟺（帶狀）`S ≥ 3.5` ⇒ **兩閘同值**，夾具無法證明測到的是 N-11 而非 N-10。
   且完全未觸及 N-9 真正困難之**末端／街角側宗**分支（兩界線不平行、取 min）。

**v2 夾具策略**：
- **主錨＝合成幾何**（新 `verify/fixture_n11_three_gates.py`）：構造一個**末端／街角側宗**，
  其 SIDELINE 與 ALLOC_LINE **不平行**、使「min 寬度」與 `S` **顯著不同**（如 min=3.2 而 S=5.0）
  ⇒ 閘須擋下它、而以 `S` 為準之假閘會放行 ⇒ **鑑別力自證**（比照 `fixture_end_winner` 之咬合反例法）。
- **回歸錨＝R6 兩宗**，且**明記其為 N-10 之產物、非 N-11 之獨立證據**。
- ⚠️ `fixture-provenance`：合成幾何之期望值由**手算**給出並註記推導，
  **禁**由新碼現跑一次回填。

---

## 四、P-4　M-5 觸發集合擴充

同 v1 §四。**增補**：寬度／深度量測**單一真相源**＝P-3 之函式，禁在 `m_rescue` 複刻。

---

## 五、P-5　UI「街廓最小建築面積」欄

同 v1 §五。**增補**（reviewer NOTE-14）：命名空間已擁擠——
既有 `f3_min_alloc_area_by_label`（MinA 正典·有讀有寫）、`f3_min_width_by_label`、
`f3_min_area_by_block`（**只寫不讀之孤兒**·全庫 1 命中）。
⇒ 新鍵取**不可能誤讀**之名：`f3_urban_plan_min_build_area_by_label`；
並**順手記帳**孤兒鍵 `f3_min_area_by_block`（列 backlog·本波不動）。

---

## 六、P-6　N-8 廢止末端族（**v2 重寫·B-2**）

### 6.1 完整消費者清單（**v1 漏 4 處**）

| 對象 | 自癒 grep | 性質 |
|---|---|---|
| `_end_gate`／`_area_rend`／末端勝者規則 | `grep -n "_end_gate = _cond1\|_area_rend" verify/wf_f4.py` | wf_f4 E3 |
| `_end_region_R` | `grep -n "def _end_region_R" app.py` | 函式 |
| `_end_band` | `grep -n "def _end_band" app.py` | 函式 |
| `{blk}-抵費地末` | `grep -rn "抵費地末" --include=*.py .` | 帳鍵 |
| `_unfront_area` | `grep -n "_unfront_area" verify/wf_f4.py` | `_end_gate` 之唯一消費者 ⇒ 隨廢（解消上批 Q3） |
| 🔴 **`_place_pool_parcels` 內 `_end_band`** | `grep -n "_band = _end_band" app.py` | **生產碼**·刪函式即 NameError |
| 🔴 **`_WF_NS_NAMES` 之 `"_end_region_R"`** | `grep -n '"_strip_axis", "_end_region_R"' app.py` | export 清單·不同步刪則雙向閘破 |
| 🔴 **`verify/fixture_end_reserve.py`** | `grep -n "_end_band" verify/fixture_end_reserve.py` | run_all 三夾具之一 |
| `verify/fixture_end_fallback.py`／`fixture_end_winner.py` | `grep -n "fixture_end_" verify/run_all.py` | 同上 |
| `verify/run_verification.py` 之引用 | `grep -n "_end_region_R" verify/run_verification.py` | 註解／閘 |

### 6.2 🔴 **廢止範圍待裁（上呈 KL）**

`_end_band` **另有一個與末端 gate 無關之用途**：`_place_pool_parcels` 之
**§4 P2-f 末端保留窗（裁定 C）**。N-8 廢「末端族」是否含此？

- **若含** ⇒ `_end_band` 可刪，但 P2-f 末端保留機制一併消失（影響階段2 落位）。
- **若不含** ⇒ `_end_band` **不得刪**，只刪 `_end_region_R`／`_end_gate`／`R_end`／勝者規則。

**v2 預設採「不含」**（保守·只廢 gate 路徑），並上呈 KL 確認。

### 6.3 閘數（**v1 說錯·更正**）

三夾具屬 `run_all` 之 **`[1/3]` golden 段**，其註明「**不進 `run_verification.results`
⇒ 不動 PASS/FAIL 計數**」（`grep -n "不進" verify/run_all.py`）。
⇒ v1 §十一「移除夾具後閘數必變」**錯**。真實影響：夾具紅會**翻 rc**、但 56/14 不動。
⇒ V5 之比對**不需扣列**，直接逐字比 FAIL 名目即可。

---

## 七、P-7　`wf_f1` 死碼與硬編常數

同 v1 §七（`TARGET_ANCHOR`／`WEDGE_AREA_ANCHOR` 及其 5 處消費點整段刪）。
🚩 **F.1 整檔存廢之張力**維持上呈（v1 §七已述）。

---

## 八、P-8　實測（**v2 重寫·B-3**）

### 8.1 🔴 撤回 v1 之「三源交叉印證」

v1 §8.1 之推論**作廢**，三理由（§〇.1 B-3）：實作取 max 而 N-12 要 min；
KL 之 166.57 即 `_end_band` 輸出（ALLOC 軸·非獨立源）；兩軸差 0.15m < 各源散布 0.27m（無鑑別力）。

**探針已修**（`verify/probes/probe_ruling_N_p8.py`）：
`_front_normal_depth`（max·已廢）→ `_front_normal_depth_min`（沿 FRONT 逐點取法向弦長之 **min**，
量測範圍參數化）；結論行改**兩讀併印**（v1 之 log 只算讀法(二)、印出與 plan 相反之結論·reviewer NOTE-16）。

### 8.2 深度四讀併陳（**不自行擇一·上呈 KL**）

| 讀法 | 深度 | N-10 門檻 | 判 |
|---|---|---|---|
| 甲 `街廓分配深度_m` | 44.5900 | 241.771 | 穩定 |
| 乙1 FRONT 法向 min·**全 FRONT** | **40.2775** | **226.678** | 穩定·兩獨立量測一致 |
| 乙2 FRONT 法向 min·p1 端 0–min_width 段 | ~~42.8029~~ ／ 1.7449 | ~~235.516~~ ／ 91.814 | 🔴 **退化·不可用**（見 8.2.1） |
| 丙 FRONT 法向 **max**（⚠️ 與 N-12 相反·僅對照） | 47.6954 | 252.640 | 算子錯 |

### 8.2.1 🔴🔴 **p1 端深度退化（本批新發現·上呈 U3）**

reviewer 量「p1 起 0–3.5m 段 min ＝ 42.8029」，我量得 **1.7449**。
**兩量測衝突 ⇒ 依停機協定不自行調和**，改直接量弦長剖面定分曉（`scratchpad/chk.py`·R6）：

```
s= 0.0000  chord= 0.0000      s= 0.2000  chord=39.8840      s= 3.5000  chord=47.5416
s= 0.0088  chord= 1.7549      s= 0.5000  chord=47.6919      s=40.0000  chord=45.7131
s= 0.0500  chord= 9.9710      s= 1.0000  chord=47.6668      s=85.8500  chord=40.2824
```

⇒ **弦長於 p1 恰為 0**，且 0→47.7 之上升發生在 **s < 0.5m** 內。
**根由**：街廓真實起點在 `s_min = −3.6068`（**p1 之後方**）——**此正是楔形存在之由**。

**結論（三項）**：
1. reviewer 之 42.8029 **無法復現**；我原輸出之 1.7449 亦僅是**取樣解析度產物**。
   ⇒ 兩者皆不可用，**乙2 欄作廢**。
2. N-12 字面「垂直距離**最小值**」若量測範圍取「該宗沿 FRONTLINE 之臨街段」而該宗自 p1 起算，
   **該值恆退化為 0** ⇒ 門檻退化為 `unfront + 0`。
3. ⇒ **N-10 之「該端深度」在邏輯上不可能是 p1 端之局部深度**。
   真義須 KL 裁（全 FRONT min ＝ 40.2775／`街廓分配深度_m` ＝ 44.59／其他）。
   ⚠️ **此為 v2 新增之上呈理由**，比 v1「哪個範圍」更根本——是「該端深度」這個概念
   在 p1 端**是否可定義**的問題。

### 8.3 承接者（**結構性結論穩健**）

**讀法(一) solo G 下，四種深度讀法之首個承接者皆為 `628-4(1)`**——
左組 solo G 依序 7.37／145.82／71.03／**692.05**／152.21／210.48，
最大之非承接者 210.48 **< 226.678**（最寬鬆門檻）⇒ **深度爭議不影響承接者判定**。
（深度爭議**確實影響** N-11(3) 深度閘與泛用性。）

**讀法(二)（含同歸戶可併ΣG）⇒ `628(2)`**。兩讀並存·**上呈**（§十二）。
🚩 「可併ΣG」係同 gid **全域粗和**、**未**套四級合併要件 ⇒ 為**上界**、非可實現量。

### 8.4 倉內已有一條閘與讀法(一)一致（**v1 未引·補記**）

`grep -n "遞補錨 R6" verify/run_verification.py` →
`W-D.4 遞補錨 R6 85.66→628-4(1)（跳過 628(2);628-1(2);628-23(1)）` **現為 PASS**。
⇒ 倉內既有斷言即「628-4(1) 承接」。⚠️ 惟該閘用 **85.66（frag）** 而非 85.7064（半平面）
⇒ 與 §一.7 之兩值釐清連動。

---

## 九、P-9　上批未辦之更正

同 v1 §九（B-1 計數 6→**7** 已由 reviewer 獨立復現；B-4 78.24 結旗）。

---

## 十、P-10　🆕 N-6 之處置（**W-10：v1 完全漏排**）

N-6（廢止機制(B)「遞補形狀調整」）在 v1 中**無任何 P 項**，僅 §七 順帶一提。
相關 run_all 閘亦未處置：`W-D.4 遞補錨 R6 85.66→628-4(1)`／`W-D.4 碎片遞補0m`／`3.5m`（皆 PASS）。

**v2 主張：N-6 本波不施作、明確延後**，理由：
- 其實作即 `verify/wf_f1.py` 全檔（F.1），而 F.1 整檔存廢已列上呈（§七）；
- 上述三閘之存廢繫於 F.1 之去留，先動閘會使 V5 逐字比對失去基準。
⇒ **列 backlog·取得 KL 同意後另波施作**。本波僅保留 `docs/W-D.4_域裁鎖定.md` 之作廢眉批
（已於 `effc29d` 置入）。

---

## 十一、泛用四約束（N-5）自查

同 v1 §十。**增補**：`_front_normal_axis` 之取號由**街廓形心**決定（幾何驅動·非塊名）；
深度量測範圍為**參數**（`s_lo`/`s_hi`），非常數。

---

## 十二、驗收預測閘

| # | 預測 | 判準 |
|---|---|---|
| V1 | `unfront_poly=None` 時**逐格零 diff** | 對 `effc29d` byte-perfect |
| V2 | R6 池帶 **2 片 → 1 片**、`85.7064` 不再單獨出現 | `[T2-DIAG]` |
| V3 | **守恆** `ΣG + 池 = 街廓` | `_resid_wd2` ≤ `n_lots×0.015`。**B-1 修正之直接驗收**：若仍破 85.71 ⇒ union 未生效 |
| V4 | N-11 **鑑別力** | 合成末端宗夾具：真閘擋下、以 `S` 為準之假閘放行 |
| V5 | `run_all` | FAIL 名目**逐字比對** `verify/out/M_0725_F10_after.log`（**不需扣列**·§6.3）；禁寫死絕對路徑閘 0 命中；三夾具 rc=0 |
| V6 | PK winner **無翻盤** | 有翻盤＝停機上呈 |
| V7 | 承接者 = `628-4(1)`（讀法一） | 與 `W-D.4 遞補錨` 既有閘一致（§8.4） |

**基準**：`effc29d` ＝ **56 PASS／14 FAIL**（`verify/out/N_runall.log`）。

---

## 十三、⛔ 停機／上呈

### 13.1 停機（真域邊界·**不得自決**）

| 觸發 | 動作 |
|---|---|
| §2.6 PK winner 集合**翻盤** | 停機上呈 |
| N-11 落地後 **ΣG／池不守恆** | 停機上呈·勿自行調和 |
| P-6 廢末端族致 FAIL 名目出現**新項** | 停機上呈 |
| 需動 `corner_pt`／`_corner_buffer_S` 上界語意 | 停機——乙案明令不動 |

### 13.2 🔴 **上呈 KL（並行·不阻碼面施工）**

| # | 題 | 本波暫採 |
|---|---|---|
| U1 | §8.2 **兩讀**（solo G vs 含同歸戶可併量） | 讀法(一)·抽為 `_carry_eligible` 單點 |
| U2 | §2.3 **弱（N-2′ 字面）vs 強（N-10）** 何者為退出判準 | 弱（忠於字面）·強分支同時寫好 |
| U3 | §8.2 **N-12 深度之量測範圍**（全 FRONT／該宗臨街段／該端 min_width 段） | 併陳·不擇一 |
| U4 | §6.2 **N-8 是否含 P2-f 末端保留窗**（`_place_pool_parcels` 之 `_end_band`） | 「不含」（保守） |
| U5 | §十 **N-6 本波是否施作**（含 `wf_f1` 整檔存廢、三閘處置） | 延後 |
| U6 | §一.6 **N-2′ 取代補丁十「乙」**（半平面由「僅判別」改「供面積」）之確認 | 依乙案 |

---

## 十四、施工序

```
P-1（規格）─ P-9（更正）─ P-10（N-6 記帳·不施作）      ← 純文件·可先行
P-2（迭代器·含 B-1 幾何 union）
  ├─ P-3（N-11 三閘＋合成夾具）─┬─ P-4（U₀ 擴充）
  │                              └─ P-5（UI 欄）
  └─ P-6（廢末端族·範圍待 U4）
P-7（wf_f1 常數）  ← 獨立
每步：py_compile → grep 驗證 → 列實際異動對照本 plan → run_all → push
```
