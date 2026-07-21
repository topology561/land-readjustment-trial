# W-G.4 S1 §4 D-右側 上呈：補丁七 §一.1 構造 ≠ 實際碎片（右側 R3 差 2.46）＋側別自偵不可純幾何

> reviewer 獨立複現駁斥·屬設計／意思裁定層（非同模型 reviewer 能拍板）·上呈 KL＋claude.ai

> ✅ **KL 2026-07-21 裁定·本上呈已回覆·勿據原文行動（掛錯波次）**：
> ① R3 末端邊(D→E) **∥ALLOCLINE（實測 0.00°）→ R3 無未臨正街**；R3-右 78.24 係**街角(§3)碎片**（production 已正確處理）→ **D-右側 從 §4 剔除**（不補右端鏡像·作廢 probe R3 右段·不改街角碼）。
> ② 是非題1 ＝ **乙**：未臨正街「面積實體」＝實際碎片 `frag["poly"]`（半平面僅判別語意）。③ 是非題2 ＝ **`frag["s"]` 確認可**（資料驅動·非 hardcode）。是非題3 moot（R3 非末端案）。
> canonical spec → `docs/specs/W-G.4_規格v3補丁十_N0-20末端塊fallback定案.md`。

- 日期：2026-07-21；branch `wip/s1-endpart`（HEAD `e343139`）
- 觸發：純技術批 plan（`W-G.4_S1_§4_純技術批_plan.md`）送 redistribution-reviewer → reviewer 依 **plan 自身 §1.2 公式**獨立複現·**駁斥 §1（D-右側）兩主張**。
- 性質：**新域邊界**（撞到才上呈·白話是非題）；與兩 PENDING fallback 裁（approach §8-1／§8-2）**相連**。

---

## 一、現況（reviewer 獨立坐實·CC 讀碼複核）

D-右側 本意 ＝ 補 R_end 構造之**右側鏡像式**並複現 R3（防失敗考古 #25「只驗左側」）。reviewer 依 plan §1.2 公式寫鏡像式，**左端值 R1 5.3255／R6 85.7064／R3 0.0001 與現行 probe 逐位同**（證鏡像忠實）→ 右端實算：

| 塊 | 補丁七 §一.1 構造（末端 ALLOCLINE 外側半平面） | 實際碎片 `frag`（`_poly_of` trunk-B 抵費地列） | 差 |
|---|---|---|---|
| R6（左） | 85.7064 | 85.66 | **0.05**（資料源級）|
| R1（左） | 5.3255 | 5.30／5.33 | ~0.03 |
| **R3（右）** | **75.78** | **78.24**（凍存 78.19）| **2.46** |

**根因（CC 讀碼坐實）**：`frag["poly"] = _poly_of(trunk-B 抵費地列)`（`wf_f1:115／133`）＝**上游管線之實際剩餘碎地**（真 DXF 幾何·非重建）；構造 ＝ 補丁七 §一.1 之**半平面切割**。**二者係不同幾何**：左側偶合（R6 0.05）·右側**顯著分岔**（R3 2.46·約 50 倍）。**approach §1 前提「構造 ≈ 碎片（差 ＝ pipeline vs CAD 資料源噪聲）」於右側不成立。**

## 二、影響

- **production 無恙**：`_reshape_block` 右側用 `wedge = frag["poly"]`（真碎片 78.24·wf_f4:1153）＋既有右側鏡像（`corner = p1+_oblique_s_max·d̂`·:1130）→ **正確**。缺陷限 **approach §1 構造式／未來 `_end_region_R`／報告表**（報告把 R3 R_end 算在左端 0.0001／153.77）·**未入 production**。
- **§4 R_end 準確度**：若未來 `_end_region_R` 之「未臨正街」取**構造**（75.78）→ 右側塊 `area(R_end)` 偏 2.46 → winner 乙門檻（`G≥area(R_end)`）／無-winner fallback（末筆抵費地嚴格＝`area(R_end)`）**於右側用錯 R_end**。UC9898 winner G≫R_end **不觸發**（latent·無夾具）·但為**未來／edge 正確性 ＋ A(a)／B-2 調和 ＋ §8-1 fallback 守恆**之前提。
- **A(a) 調和變難（reviewer §5 NOTE）**：approach §4 A(a) 擬「施工時斷言 `|frag − 構造| < tol` 釘安全向」——R3 差 **2.46**（非 R6 之 0.05）→ tol 若取 ~0.05 級·**R3 必誤觸 raise**。fallback 施工前須先解此落差。

## 三、側別自偵不可純幾何（reviewer 反例）

plan §1.2 擬「純 block 幾何自偵未臨正街端·禁 hardcode 側別」。reviewer 反例：**R1 兩端皆有**——左 5.3255（＝真 frag·left）／右 **6.5961**（**無對應 frag 之幾何幻影**）。純幾何判準（`smax > s_p2+ε` → 右端有）對 R1 右端**亦為真** → 純 block 幾何**無法**還原「該端有無抵費地碎片」。**production 用 `frag["s"]`**（碎片實位·R1 s=0.02→left 正確）故無此病。⇒ 側別須改用 `frag["s"]`／`推進側別`（資料驅動·＝production 同源·**非 hardcode 塊名**）。

## 四、是非題（請 KL／claude.ai 裁）

1. **未臨正街 權威定義（域裁·連 §8-1）**：§4 R_end 之「未臨正街」取 **(甲) 補丁七 §一.1 半平面構造**·抑或 **(乙) 實際碎片 `frag`（`_poly_of`·＝production 所用者）**？二者右側差 2.46。
   - 若 **乙**：補丁七 §一.1 半平面係「**判別語意**」·面積實體一律用 `frag`（`R_end = frag ∪ 末端帶`）；A(a)「取同一物件」＝一律取 `frag`（構造僅判別、不供面積）。
   - 若 **甲**：R_end 用構造·**接受**與實際碎片右側差 2.46（則 production `wedge=frag` 與 `_end_region_R` 構造係兩物·A(a) 斷言 tol 須容 2.46）。
2. **側別源**：`_end_region_R`／probe 側別改用 `frag["s"]`／`推進側別`（資料驅動·＝production）·棄純幾何自偵——**確認可（非違「禁 hardcode 側別」）**？
3. **右側 2.46 之性質**：係「二表示預期差」（→乙）·抑或「構造之 p2 錨點／定義須修使其重現 frag」（→需 claude.ai 修補丁七 §一.1 右側式）？

## 五、次步

- 裁 1–3 後：revise approach §1（右側鏡像式依裁·未臨正街源定案）＋ D-右側 probe（側別 `frag["s"]`·未臨正街依裁甲／乙）→ 送 reviewer → 施工。
- **純技術批之 §2（probe過期名 doc）已隨本波 push；§3（rebake 註解·零行為）續施工**（皆與本裁無關·reviewer PASS）。
- 本裁**與 §8-1 fallback 守恆相連**（R_end 準確度為 fallback 面積歸屬之前提）·宜合裁。

---

**引用（絕對倉路徑）**
- 計畫：`docs/reports/W-G.4_S1_§4_純技術批_plan.md`（§1 已依本上呈標 BLOCKED）
- approach：`docs/reports/W-G.4_S1_§4_N0-20_approach.md`（§1 前提／§4 A(a)／§8-1）
- 構造 vs 碎片：`verify/wf_f1.py:115/133`（`_poly_of`）·`verify/wf_f4.py:1130/1153`（production 右側用 frag）
- 側別/面積錨：`verify/baselines/v3/W-D.4_碎片遞補對照_退縮0m.csv`（R3 78.24／right）·凍存 `…PRE-S0b…/v3/…:4`（78.19）
- reviewer 複現：右端 R3 構造 = 75.78（獨立·忠實左端對拍）
