# W-G.4 S1 §4 純技術批 plan（裁前可自理·不觸 fallback 守恆·送 reviewer）

- 日期：2026-07-21；branch `wip/s1-endpart`；承 `e343139`（＝origin·已 push）
- 依據：approach `W-G.4_S1_§4_N0-20_approach.md` §0.6（reviewer 二審 CC 自理技術修）＋新 session 交接 §三；補丁七（N0-20 幾何正典·§一.1／§二.2）
- 紀律：泛用四約束（禁本案常數·禁 hardcode 塊名／側別）；plan→reviewer→施工→push
- 狀態：**reviewer 二審已回**（下 §0.1）——§2／§3／範圍圍欄 **PASS→施工**；**§1 D-右側 REFUTED→BLOCKED**（上呈 KL·見 `W-G.4_S1_§4_D右側_構造vs碎片落差_上呈.md`）。

---

## 0.1 🔴 reviewer 二審 verdict（獨立複現·CC 接受）

| # | 項 | verdict | 據 |
|---|---|---|---|
| §2 | probe過期名 | **PASS** | `recon.md:22` 確 `probe_rend3.py`·`git ls-files` 無此檔 |
| §3 | rebake 註解 | **PASS**（零行為·非 golden 捕捉） | 實算 `n×0.005` ≠ 訊息自述 `n×(0.005×深度＋0.005)`·僅閘失敗才出現·run_all 綠路徑不觸 |
| §0/§4 | 範圍圍欄 | **PASS** | fallback raise `wf_f4:1162` 原封·`_end_region_R`／winner 門檻 grep 空（未建）·A(a)/B-2 僅 doc |
| **§1** | **D-右側** | **🔴 REFUTED** | reviewer 依 §1.2 公式複現右端 R3 ＝ **75.78**·非 §1.3 宣稱 78.19（Δ≈2.4·非 <0.05）；側別自偵 R1 兩端皆有（純幾何不可定側） |

**§1 兩宣稱經 reviewer 自身算術駁斥**（詳 §1 修正）：構造(半平面)75.78 ≠ 實際碎片 frag 78.24（右側差 2.46·根因＝二不同幾何）；側別須用 `frag["s"]`。→ **屬設計/意思域裁·上呈 KL/claude.ai·裁前不施工 §1**。§2/§3 與此無關·續施工。

---

## 0. 範圍（**EXCLUDES** fallback 核心）

**排除（BLOCKED·兩域裁未回·裁前不施工＝停機）**：無-winner fallback 守恆模型（§8-1 甲池吸收／乙建地前移）＋乙搜尋語意（§8-2 首筆嚴格／續搜）。本 plan **一律不碰** `wf_f4:1162 raise → fallback` 之改、不碰任何 G／池／bisect 路徑。

**納入（純技術·與 fallback 守恆無關·approach §0.6）**：

| # | 項 | 性質 | 碼位 |
|---|---|---|---|
| 1 | **D-右側** probe 右側鏡像＋複現 R3 | 施工（probe）＋設計（approach §1 鏡像式） | `probe_§4_R_end.py` ＋ approach doc |
| 2 | probe過期名 | doc 更正 | `recon.md:22` |
| 3 | rebake WATCH | 註解／訊息順修（零行為） | `wf_f4:712／719-720` |
| 4 | A(a)／B-2 先備 | 設計（approach doc·待 fallback 施工消費） | approach doc |

**零 production 影響（證）**：production `_reshape_block` 右側**已正確**——`corner = p1 + _oblique_s_max·d̂`（wf_f4:1130）＋`wedge = frag["poly"]`（:1153·＝R3 78.19 DXF 實體）。D-右側 缺陷限於 **probe ＋ 設計式 ＋ 報告表**（把 R3 R_end 算在**左端** 0.0001／153.77）·**未入 production**。本波不改 production 行為。

---

## 1. D-右側（substantive·#25「只驗左側」風險核心）

> 🔴 **BLOCKED（reviewer REFUTED·上呈 KL）**：下 §1.2/§1.3 之「純幾何側別自偵」與「右端構造複現 R3 78.19」**經 reviewer 獨立算術駁斥**——
> ① 右端構造（補丁七 §一.1 半平面）＝ **75.78** ≠ 實際碎片 frag **78.24**（Δ2.46·根因＝二不同幾何·非資料源噪聲）；
> ② 側別純幾何不可定（R1 左 5.33 真 frag／右 6.60 幻影·兩端皆有）→ 須用 `frag["s"]`（＝production 源）。
> 二者屬**設計/意思域裁**（`W-G.4_S1_§4_D右側_構造vs碎片落差_上呈.md`·連 §8-1）·**裁前不施工 §1**。下文 §1.2/§1.3 保留為「被駁之原擬」·裁後 revise。

### 1.1 現況（repo 坐實）
- probe（`probe_§4_R_end.py:22-29`）三塊**同用左端式**：未臨正街 ＝ `block∩{s<0}`（`smin<0` 才有）·末端帶錨於 `p1`。
- R1／R6 ＝左側案（未臨正街端 ＝ p1·s<0）→ 85.7064／5.3255 對錨 ✓。
- **R3 ＝右側案**（repo 錨：`W-D.4_碎片遞補對照:4` ＝ `right,628-45(2)`·`PROVENANCE_v3.md:145` R3-抵費地-2 ＝ **78.19**·`wd3_fragment_edges.csv:10` 臨路）→ 左端式得 **0.0001**（R3 左端無未臨正街）·**未臨正街端實為 p2**。
- ⇒ 報告表（approach:102·recon:27）R3「0.0001／153.7720／153.7721」**係錯端計算**（153.77 ＝ p1 錨 band∩R3·**非** R3 真末端帶）。

### 1.2 改（側別**自偵**·禁 hardcode「R3=右」）
補丁七 §一.1：未臨正街 ＝ `block∩{末端 ALLOCLINE 外側半平面}`·末端 ALLOCLINE ＝ 過**未臨正街端點**且 ∥`cad_alloc` 之線。§二.2：末端帶 ＝ 該線向街廓內平移 mw（**垂距**）。左右鏡像 ＝ **未臨正街端點 p1 ↔ p2 對調**。

probe 泛化（每塊自偵未臨正街端·**非寫死側別**）：
1. `m̂,denom = _strip_axis(d̂, ad)`；`smin,smax = _strip_s_range(poly,d̂,p1,ad)`；`s_p2 = ((p2−p1)·m̂)/denom`（p2 之 s 座標·**同軸**·恆等 `s(p1)=0`）。
2. **左端未臨正街** ＝ `block∩{s<0}`：`smin < −ε` → 有（端點 p1）。
3. **右端未臨正街** ＝ `block∩{s>s_p2}`：`smax > s_p2 + ε` → 有（端點 `pmax = p1 + s_p2·d̂` ≈ p2）。
4. 末端帶錨於該端未臨正街之端點 `e`（左 ＝ p1／右 ＝ pmax）：`band = Polygon([e−B·ca, e+B·ca, e+B·ca+mw·n̂, e−B·ca+mw·n̂]) ∩ poly`·`n̂ = rot90(ca)` 定號使 `(centroid−e)·n̂>0`·**`B` 由 block bounds 導**（對角線長·禁硬編 500）。
5. `R_end = 未臨正街 ∪ 末端帶`（該端·共界不疊）。

> **同源（防 #20）**：右端終點與 s 軸取 `_strip_s_range`／`_strip_axis`（＝ production `_reshape_block:1130` 右側 `corner`／`_oblique_s_max` 之同一軸）·**禁**另立正交式量 s（斜交下 R3 差 3.4571m·補丁五 BLOCKED-1）。

### 1.3 驗收
- **R3**：右端未臨正街 ≈ **78.19**（baseline·現行倉態 ~78.24·差 ＝ block polygon 資料源〔pipeline vs 原始 CAD〕·approach:105 已述·非構造）·Δ<0.05；右端末端帶 ＋ R_end 逐位可重現（純 CAD 座標·KL／claude.ai 逐塊坐實）。
- **R1／R6 不變**（左側·端點 p1）：85.7064／5.3255 **逐位同現**。
- probe 印出「偵得未臨正街端（左／右）」·三塊端別 ＝ R1 左／R6 左／R3 右。

### 1.4 設計式補（approach §1·右側鏡像顯式化）
approach §1 構造式全 `p1／{s<0}` 本位 → 補「**右側鏡像**：未臨正街端 ＝ p2·未臨正街 ＝ `block∩{s>s(p2)}`·末端帶自 `s(p2)` 線向內 −mw 平移」。＝ D-右側「補右側鏡像式」（不入碼·approach doc）。

---

## 2. probe過期名（純 doc）
`recon.md:22` `probe_rend3.py`（scratchpad 舊名·已不存·`git ls-files` 無）→ `docs/reports/probes/probe_§4_R_end.py`（實名·已入倉）。

---

## 3. rebake WATCH（**零行為**·僅註解／raise 訊息文字）
- 現：`wf_f4:712` 註解「閘寬 ＝ 整形涉及宗數 ×（0.005×深度 ＋ 0.005）」·`:719-720` raise 訊息同式。
- 實算：`wf_f4:715` `_acct_geom_tol_block(len(npolys), _e3_depth, False)` → `_acct_geom_tol_per_lot(depth, False)`·**S0d 後已移除 `0.005×深度` 項**（`app.py:6831` docstring 明載「`_acct_geom_tol_per_lot` 已移除 0.005×深度 項」）＝ `n × 0.005`。
- ⇒ 訊息自述式（`n×(0.005×深度＋0.005)`）與實算值（`n×0.005`）**不符**——印出的 `_e3_tol` 數字對不上其括號內自述式（S0d 後遺漏更新之文字）。
- 改：`:712` 註解 ＋ `:719-720` raise 訊息改述 post-S0d `_acct_geom_tol_per_lot`（深度項已移·`整形宗數 × 0.005`；`with_tol=False` 故無 tol 項）。**碼路徑（`_e3_tol` 計算）不動 → 零行為**（py_compile ＋ run_all 綠證）。

---

## 4. A(a)／B-2 先備（設計·**非本波施工**·耦合未建 `_end_region_R`）
記於 approach doc（待 fallback 施工消費·裁後）：
- **A(a)**：`_end_region_R` 之未臨正街構造 與 `_reshape_block:1153 wedge=frag["poly"]` 係二表示（R6 frag 85.66 vs 構造 85.7064·Δ~0.05）→ 施工時 bisect wedge 亦用構造（**或** 斷言 `|frag−構造|<tol` 釘安全向）·門檻與 bisect 取**同一物件**。
- **B-2**：winner 門檻由「`G≥area(R_end)` 面積不等式」→ **顯式幾何包含斷言** `末端帶.difference(strip).area<tol`（取代面積不等式）＋述 buf×末端帶 交互（forced buf>0／非凸街廓反例）。
- 本波僅於 approach doc 記此二**設計精修**·**不動 production**（`_end_region_R`／winner 門檻皆未建·裁前不施工）。

---

## 5. 守則
- 泛用四約束：R_end／末端帶／未臨正街 逐案幾何算·∥ALLOC 斜交（缺 cad_alloc loud·禁正投影／垂直）·側／端顯式參數化·**禁寫死** 塊名／側別／mw／B。
- 零 production 影響（§0）·守恆不觸（本波不改任何 G／池／bisect／fallback raise 路徑）。

---

## 6. 驗收命令
1. `py_compile` app.py ＋ wf_f4.py ＋ probe。
2. 跑 probe → R3 右端 78.19±0.05·R1／R6 逐位不變·端別印正確（左／左／右）。
3. `run_all` 綠（rebake 註解改零行為·probe 非 harness·doc 非碼）。
4. grep 確認：無 `probe_rend` 殘留·`wf_f4:1162` fallback raise **原封未動**。

---

## 7. 送 reviewer 之問
1. **D-右側 鏡像正確性（最重·#25）**：side 自偵（`s_p2` 雙端判別）是否穩健（涵蓋兩端皆有未臨正街／皆無之退化）？右端式是否複現 R3 78.19？「禁 hardcode 側別」達成？
2. **rebake 訊息**：確認現訊息式（`n×(0.005×深度＋0.005)`）確與 `_acct_geom_tol_per_lot`（post-S0d `n×0.005`）不符？改後零行為（碼路徑不動）？
3. **範圍圍欄**：本波確**無**觸 fallback raise（`wf_f4:1162`）／守恆／production `_reshape_block` 行為？A(a)／B-2 僅 approach doc、未入碼？
