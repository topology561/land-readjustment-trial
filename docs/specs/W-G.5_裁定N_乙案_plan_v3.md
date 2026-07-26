# W-G.5 裁定 N · **乙案** — 施工 plan **v3**（delta over v2）

> **取代 plan v2**。v2 之未變更節次**仍有效**，本檔只寫 **delta**（v2 四 BLOCKED ＋ 六 WARNING 之修）。
> **基準倉態**：`origin/wip/s1-endpart = effc29d`。**引擎仍零改動**。
> **⛔ 施工仍未解封**——見 §一（**U7 為硬前置·非技術題·KL 未裁不得開工**）。
> 審查鏈：v1（3 BLOCKED）→ v2（4 BLOCKED）→ **v3**。

---

## 一、🔴🔴 **U7：baseline 重烤授權 —— 本波之硬前置**（v2 未插旗·reviewer 二審 BLOCKED-1）

### 1.1 矛盾之形狀

| 事實 | 出處 |
|---|---|
| 0m 之驗證閘係對 `verify/baselines/v3/*.csv` 之**逐格 diff** | `grep -n "diff_rows(" verify/run_verification.py`（診斷／G 值／滑池槽／J 表） |
| 該批 0m 閘**現全 PASS** | `verify/out/N_runall.log`：`v3·診斷0m`／`指配0m`／`v3·G值0m`／`v3·滑池槽0m`／`v3·J表0m`／`k* 六塊經驗錨0m` |
| P-2 落地**必改分配幾何** | R6 左組前三宗退出、`628-4(1)` G 692.05→≈606；**R1 首宗 G ＋5.3255**（W-2） |
| ⇒ 上列 0m 閘**必翻 FAIL**、且為**新 FAIL 名目** | — |
| 而 v2 §13.1 定「FAIL 名目出現新項 ⇒ 停機」、V5 定「逐字比對」 | v2 §十二／§十三 |
| 重烤（`WV_BAKE`）屬 **P-H**，而 **P-H 由 KL 凍結** | 交辦文「P-H 維持凍結」 |

⇒ **改引擎、禁重烤、卻要求 FAIL 名目逐字不變——三者不可同時成立。**
這**不是技術題**，是排程／授權題。**CC 不得自決**。

### 1.2 上呈 KL 之三個選項（**請擇一裁示**）

| 選項 | 內容 | 代價 |
|---|---|---|
| **(甲)** P-H **局部解凍**：僅授權重烤 0m／3.5m 之 v3 baseline 六檔 | 可正常施工·V5 恢復意義 | 重烤即把乙案結果定為新基準，需 KL 先目視認可 |
| **(乙)** 維持全凍結，V5 改為「**僅比對未預測之新 FAIL**」＋本 plan 附**預測翻閘清單** | 不動 baseline | 預測清單本身無獨立驗證（＝自己說自己對·舉證力弱） |
| **(丙)** 本波只做**不改幾何**之項（P-1／P-5／P-7／P-9／P-10 ＋ P-3 之量測函式與夾具），**P-2／P-4／P-6 延後至解凍** | 零風險·可立即開工 | 乙案核心（P-2）不落地 |

**CC 建議 (丙) 先行**——理由：(丙) 之項目**全部與 baseline 無關**（純文件／UI／夾具／死碼清除），
可立即產出且零回歸風險；待 KL 裁 U7 後再以 (甲) 或 (乙) 續做 P-2。
**但此為建議、不自決**：三選項之取捨繫於 KL 對「何時可把乙案結果定為基準」之判斷。

### 1.3 預測翻閘清單（選項(乙) 之必要附件·**先備**）

| 閘 | 現況 | 預測 | 理由 |
|---|---|---|---|
| `v3·G值0m` | PASS | FAIL | R6 三宗退出＋`628-4(1)` G 變；R1 首宗 ＋5.3255 |
| `v3·診斷0m` | PASS | FAIL | 同上（G 欄入診斷表） |
| `指配0m` | PASS | FAIL | 承接／退出改指配 |
| `抵費地0m(應空)` | PASS | **待驗** | 楔形由池片轉宗地 ⇒ 抵費地列可能變 |
| `v3·滑池槽0m`／`v3·J表0m` | PASS | FAIL | k* 連動（W-3） |
| `k* 六塊經驗錨0m` | PASS | FAIL | 退出宗使 `widths` 出現 0 ⇒ k*(R6) 幾必變（W-3） |
| `結構不變量永久閘0m` | PASS | **應維持 PASS** | 守恆／結構不變量不應因本波破——**若翻即真 bug** |

⚠️ **此表為預測、非實測**（舉證力弱·`CLAUDE.md` #21）。落地後以實跑覆核；
**預測外之新 FAIL ⇒ 停機**。

---

## 二、P-2 修正（reviewer 二審 BLOCKED-2／-3 ＋ W-1／W-2／W-3／W-4／W-5）

### 2.1 🔴 union 與 raise **必須移出既有 `try`**（BLOCKED-2·已自驗）

自驗（`sed -n '7798,7812p' app.py`）：

```python
        if final_cut is not None and not final_cut.is_empty:
            if hasattr(final_cut, 'geoms'):        # MultiPolygon → 取面積最大者
                _biggest = max(list(final_cut.geoms), key=lambda g: g.area)
                ...  cut_coords = [...]            # ← **只取最大片**
    except Exception:
        cut_coords = []                            # ← **吞掉一切 raise**
```

**兩個獨立致命點**（皆已復現）：
1. v2 §2.2 之 `raise ...非單一 Polygon` 若寫在此 `try` 內 ⇒ 被吞 ⇒ `cut_coords = []`
   ⇒ 該宗無幾何 ⇒ `allocated_polys` 缺它（`grep -n "allocated_polys.append" verify/stepg_pipeline.py`）
   ⇒ `_missing_owner` **只 print 不 raise** ⇒ **池雙計該宗全部面積**（守恆破更大）。
2. 即使不 raise：MultiPolygon 分支**靜默取最大片**當 `cut_coords`，而 `area_conv` 取**全 multi**
   ⇒ **B-1 原病以另一條路徑無聲復發**。

**修法**：
- union ＋ 形狀檢查 ＋ `area_conv` 賦值**全部移到 `try` 之外**（`try` 只保留 `cut_coords` 生成）。
- `unfront_poly is not None` 時，MultiPolygon 分支**改為 raise**（禁沿用「取最大片」）。

### 2.2 🔴 `_corner_first_lot_G` **側別 gate ＋ 起點斷言**（BLOCKED-3）

- `_corner_block_true_G` 對每候選**逐側**呼叫（`grep -n "gp\['p1'\] = round(_corner_first_lot_G" app.py`）；
  右側時 `_bp = _cp + s_max_right·d̂`、`_dh_use = −d̂`。把**左**楔形餵進右側 ⇒ union 必不相連
  ⇒ raise ⇒ 被 `_solve_G_one` 之 `except Exception: pass` **靜默吞** ⇒ 落 `iterate_G_S`
  ⇒ **PK winner 無聲翻盤**（正是 §13.1 要停機者，卻以偵測不到的方式發生）。
- **修法**：(a) `unfront_poly` **依側別 gate**（左楔形只給 `side='左'`，右側傳 `None`）；
  (b) 承接前置加 **loud 斷言 `left_cum_S == 0`**（≡「首宗 baseline_pt ≡ p1」）——
  左端若為 forced（`_left_buffer_S > 0`）則首宗 strip 起於 `p1 + buf·d̂`、與楔形隔著街角抵費地帶
  ⇒ **必不相連** ⇒ **不得承接**、須 loud 診斷；
  (c) §2.4 之 guard 須**涵蓋 `_corner_first_lot_G` 這條路徑**（v2 只寫了兩處、漏此）。

⚠️ UC9898 現**尚未觸發**（R1 首宗起於 s=0＝`_left_buffer_S=0`；R6 左無 SIDELINE ⇒ buf=0），
**但 latent ≠ 安全**——`_left_buffer_S` 取決於 PK winner 落哪側，而 §2.6 正是要改 PK 的 G
⇒ **本波可親手製造失效條件**。故 (b) 之斷言為必需，非防禦性冗餘。

### 2.3 `_pending_unfront_poly` 之 scope（W-1）

`_advance_block_with_split` **每塊被呼叫 3 次**（`_k_star` 退化趟／`_k_naive` 基準趟／`_k_star` 正式趟；
app 與 stepg **各 3 處**＝共 6 個呼叫點）。
⇒ **必須於函式體頂端重新計算／重設**，每次呼叫獨立。
若置街廓層 ⇒ 基準趟消耗、正式趟見 `None` ⇒ **兩趟不同源** ⇒ `widths` 與實配脫鉤。
**驗收清單＝該 6 個呼叫點**（`grep -n "_advance_block_with_split(" app.py verify/stepg_pipeline.py`）。

### 2.4 承接宗之寬度（W-4）

`_mark_zaling` 之寬度由 **S** 導出、不看幾何
（`grep -n "_pw = float(_res.get('S'" verify/stepg_pipeline.py`）。
承接後該宗實跨 `s ∈ [s_min, S]` ⇒ 寬度應為 `(S − s_min)·cos_dn`；R6 低報 `3.6068·cos_dn ≈ 3.59m`。
連動 `_畸零旗標`／`_widths_local`（→k*）／P-3 之 N-11(2)。
⇒ **`_mark_zaling` 須納入改點清單**（v2 漏）。

### 2.5 退出宗之表達（W-3 ＋ reviewer 未答之題）

退出宗維持 `_widths_local` 之 `0.0`（`grep -n "_widths_local = \[0.0\]" verify/stepg_pipeline.py`）
⇒ `_adv_base['widths']` 改 ⇒ `_select_pool_slot` 之 k* 改 ⇒ `k* 六塊經驗錨0m` 翻（已列 §1.3）。

🔴 **v3 須明定**（v2 只寫「入 M-5 U₀」）：退出宗在 `g_rows` 中**以 `G=0` 之列存在**（非不出列）——
理由：不出列會使 `_sum_G_blk` 之母體與宗數不一致、且下游「宗數」型診斷失準；
出列且 `G=0` 則守恆帳自然成立（該宗面積留在池）。**此為技術決定、記帳於此**。

### 2.6 N-9 分支（W-5）

承接後該宗一側界線＝**街廓左封邊**（實測與 `n_front` 夾 0.287°，與 ALLOC 之 4.61° 不同）
⇒ **非 ALLOC 平行線** ⇒ 兩界線不平行 ⇒ 依 N-9 **須走取-min 分支**。
⇒ **承接宗不得當中間宗處理**（v2 §3.2 之「中間宗 寬度 ≡ S」對它不適用）。
⇒ 與 v2 §3.4 之「合成末端宗主錨」**明文連起**：該合成夾具即承接宗之抽象模型。

---

## 三、P-3／P-8 深度（reviewer 二審 BLOCKED-4 ＋ W-6）

### 3.1 🔴 **乙1 亦作廢**——與乙2 同為取樣產物（已自驗）

v2 §8.2 標乙1「40.2775·穩定·兩獨立量測一致」**錯**。自驗（`scratchpad/chk.py`·R6·全 FRONT）：

| 取樣 step | `min(chord > 1e-9)` | **`min(chord, s ≥ 0.5)`** |
|---|---|---|
| 0.21464 | 40.2776 | **40.2776** |
| 0.01000 | **1.9943** | **40.2776** |
| 0.00100 | **0.1994** | **40.2776** |

⇒ **無排除帶之 min 隨取樣→0**（乙1、乙2 同病）；
⇒ **有排除帶（`s ≥ 0.5`）則跨三個數量級之取樣完全穩定於 40.2776**。

**此即 U9 之答案形狀**：N-12 之 min **必須附排除帶定義**才可實作。
排除多寬、依據為何 ⇒ **KL 裁**（CC 之實測顯示 `0.5m` 已足以穩定，但該值**須有法源或工程依據、
不得由 CC 挑一個好看的數**）。

⚠️ 併記：排除退化帶後真正的 min **落在 `s = 85.850`＝p2 端** ⇒ 用它當「**p1 端**深度」在語意上
是拿街廓**另一端**的幾何定門檻 ⇒ **語意問題仍在**、與取樣無關。

### 3.2 🔴 撤回 v2 §8.2.1 之「恆退化為 0」通則（W-6·理由過強）

v2 稱「該值**恆**退化為 0」——**不成立**。reviewer 查 R6 p1 附近頂點：
`v[0]=(0,0)`（p1 本身即街廓頂點）、`v[4]=(0.2392, 47.7050)`
⇒ p1 處內角錐張 `atan(47.705/0.2392) = 89.713°`，`n_front` 在 90° ⇒ **差 0.287° 落在錐外**。
若左封邊向 `−d̂` 傾，`chord(p1)` 立刻是滿值 47.7，而**楔形仍存在**
（楔形之充要條件＝「封邊傾角 < ALLOC 傾角 4.61°」，**與傾向無關**）。

⇒ **R6 是碰巧**，非通則。**結論不變**（N-10 之「該端深度」不可能是 p1 端局部深度），
但**理由換成**：`chord` 在 `[0, 0.24]` 內由 0 竄到 47.7（斜率 **199.4**）
⇒ **任何以 min 定義之端部深度在該區間皆為超敏感階躍、不是可用之工程量**。

（探針之退化提示文字須照此改寫——**現行文字帶著不成立之通則**，不改會讓 KL 據錯前提裁示。）

---

## 四、P-6（NOTE-3 補正）

保守切法（刪 `_end_region_R`、保留 `_end_band`）**經 reviewer 全掃確認自洽**。
**補一點 v2 沒寫**：`verify/run_all.py` 之三夾具元組須移除 `fixture_end_fallback.py`
與 `fixture_end_winner.py` **兩項**（`grep -n "fixture_end_" verify/run_all.py`），
否則 subprocess 找不到檔 ⇒ `rc=1`。`fixture_end_reserve.py` 只要 `_end_band` ⇒ **保留可續綠**。

**NOTE-5 併記**：`_place_pool_parcels` 之 `_reserve['lo']` 由**原始街廓幾何**重算 `_unfront`
（承接後仍為 85.7064）⇒ 該 reserve 成為 stale；因取 `max(_cum_left, _reserve['lo'])`
而 `_cum_left` 遠大之 ⇒ **實務 inert**。若 U4 裁「不含」，須於該處加註說明為何不需同步。

---

## 五、reviewer 二審之背書（**已復現·記錄在案**）

| # | 項 | 結論 |
|---|---|---|
| N-1 | **B-1(b) 我自標之風險（union 致池-宗重疊）** | ✅ **安全**。`_pool_strips_for_block` 以 s-區間**補集**構池（`cur = s_min`）；union 後承接宗 `_strip_s_range` 變 `(s_min, S)` ⇒ `a ≤ cur` ⇒ **不產生 `[s_min,0]` 池區間** ⇒ ②-池／①' 兩閘皆不破。且 union 為**精確**：`strip[0,S] ∪ band[s_min,0] ≡ _block_strip(..., p1+s_min·d̂, S−s_min)`（同組 ALLOC 切線）——此即 V2「2 片→1 片」之機制 |
| N-2 | W／Rw 不受 union 影響 | ✅ 只依 `baseline_pt`／`side_mid`／`S_guess`；`left_cum_S += S_raw`（不含楔形）⇒ telescoping 不變 |
| N-5 | `_place_pool_parcels` 池窗語意 | ✅ `_cum_left` 為純前進量·不需改 |

🔴 **教訓（第二次·記帳）**：v1 我把旗插在 §2.2 定點斷言（**沒事**），真 BLOCKED 在別處；
v2 我把旗插在 union 對池片之衝擊（**又沒事**），真 BLOCKED 在重烤授權／`try` 邊界／PK 側別。
**連續兩輪「自標風險點 ≠ 真風險點」** ⇒ 本專案 `CLAUDE.md` 之
「🔒 自評 gate 綠不可替代獨立復現」再次被實證。

---

## 六、上呈 KL（U1–U9·**U7 為施工硬前置**）

| # | 題 | 狀態 |
|---|---|---|
| **U7** | **baseline 重烤授權**（§一·甲／乙／丙 三選一） | 🔴 **硬前置·未裁不得開工 P-2** |
| U8 | 被「吃不下」踢出之宗（R6 三宗·ΣG 224.22㎡）其權利如何在終態落地？v2 只寫「入 M-5 U₀」，但 M-5 是**救援池**、非原位次分配 | 法規本意題 |
| U9 | N-12 之 min 須附**排除帶**定義（實測 `s≥0.5` 可穩定，但該值須有法源／工程依據） | 併 U3 |
| U1–U6 | 同 v2 §13.2（兩讀／弱強條件／深度真義／N-8 範圍／N-6 時程／補丁十乙） | 不阻碼面 |

---

## 七、次步

1. **U7 未裁前**：CC 依 §1.2 建議之 **(丙)** 開工——P-1／P-5／P-7／P-9／P-10
   ＋ P-3 之量測函式與合成夾具（**皆不改分配幾何、零 baseline 風險**）。
2. U7 裁後：依 (甲) 或 (乙) 續 P-2／P-4／P-6。
3. 探針文字依 §3.2 改寫（**優先**——現行文字含不成立之通則）。
