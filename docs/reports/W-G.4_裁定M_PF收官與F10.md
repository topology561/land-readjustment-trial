# W-G.4 裁定 M — **P-F 收官（F-2/F-5/F-6）＋ F-10 三項 ＋ 行號衛生**

> 基準 `ebe24fe`。依 KL 裁復（2026-07-25）：F-1 證據效力「有效·P-F 不拆」＋F-2「准·三附帶」
> ＋行號衛生一併做完＋F-10 三項補做＋BK-4 裁定入倉。
> 紀律：凡「已修／已驗／已咬合」之宣稱，**均附實際輸出行**。**新閘必附咬合反例之紅字**。

---

## 〇、一句話

P-F 之 F-2／F-5／F-6 全部落地並實測；F-10 三項全部補做且**三個都造出紅字證其會咬**；
行號衛生掃完 **22 處活碼引用**並把 doctrine 寫入 `CLAUDE.md`。
另補一個既有**覆蓋率洞**：三個末端夾具原本**不在任何自動流程內**，本次納入 `run_all`。

**行為零變更之證明**：全部異動後 `run_all` 非 BAKE ＝ **56 PASS／14 FAIL**，
**FAIL 名目逐字與 `ebe24fe` 前態相同**（3.5m baseline 7 列＋`k*3.5m`＋`F.0~F.4` 五列＋`G.2`）。
碼面異動之 diff：行號衛生段 **24 insert／23 delete·全屬註解/docstring**；
F-10 三閘為**加性**（新增 `_pop_viol` 與 `_pz_of`·既有判準未動）。

---

## 一、F-2：末端 gate 斷言改靶（KL 准·三附帶全數落實）

### 1.1 (a) 斷言改對 `_unfront_area` ＋末端 winner 前後集合

新檔 `verify/fixture_end_winner.py`。**核心命題**（`_cond1` 單獨無從產生者）：

> **cond1 為真而 cond2 為假時，gate 必須不觸發。**

`_cond1 = not fo["{side}_has_side"]` 係直接讀旗標、by construction 近恆真；
上述命題**唯有** `_unfront_area` 被真的計算並比較時才成立。

**實測**（`verify/out/M_0725_F2_end_winner.log`·exit=0）：

```
[3.5m·left]  驗0 _unfront_area：有伸出 40.0000(手算 40.0000)／無伸出 0.0000(手算 0.0000)  ✅
[3.5m·left]  驗1 cond1真+cond2假 ⇒ 同 gate 關：C=('raise','整形寬') vs B2=('raise','整形寬')  ✅
[3.5m·left]  驗2 cond2真 ⇒ 標的換人：A=('raise','不相鄰') vs B=('raise','整形寬')  ✅
[3.5m·left]  驗3 首宗達 area(R_end) ⇒ gate 開關同標的：A3=('ok','TEST-1') B3=('ok','TEST-1')  ✅
[3.5m·right] 驗2 cond2真 ⇒ 標的換人：A=('raise','不相鄰') vs B=('ok','TEST-1')  ✅
RESULT: PASS
```

### 1.2 (b) 咬合反例（**必附紅字**）

把 `ns["_end_region_R"]` 之回傳面積壓成 `0.0`（模擬 gate 失去判別力：`G ≥ area(R_end)` 恆真）：

```
【咬合反例】把 `_end_region_R` 面積壓成 0（模擬 gate 失去判別力）⇒ 本夾具應轉紅：
   [0m·left]   驗2 cond2真 ⇒ 標的換人：A=('raise','整形寬') vs B=('raise','整形寬')  🔴
   [0m·right]  驗2 cond2真 ⇒ 標的換人：A=('ok','TEST-1') vs B=('ok','TEST-1')        🔴
   [3.5m·left] 驗2 cond2真 ⇒ 標的換人：A=('raise','整形寬') vs B=('raise','整形寬')  🔴
   [3.5m·right]驗2 cond2真 ⇒ 標的換人：A=('ok','TEST-1') vs B=('ok','TEST-1')        🔴
   反例結果：🔴 FAIL（正確——閘咬得到）
```

反例**內建於夾具**（`run(patch_rend=True)`）⇒ **可重跑複驗**，非一次性手改。

### 1.3 (c) side/tag-agnostic

四組（`{0m,3.5m}` × `{left,right}`）走**同一套判準**；幾何由 `side` 參數化鏡像產生，
碼中無塊名、無側別分歧常數。期望值全部獨立手算（見夾具 docstring 之二表）。

### 1.4 📌 實測附帶發現（**非預測·是輸出**）

`area(R_end)` 之門檻與下游「整形後寬 ≥ mw」閘在本合成幾何下**同值**：
`S_new` 滿足 `strip(0,S_new)+frag = G`、而 `strip(0,mw) = 末端帶` ⇒
`S_new ≥ mw ⟺ G ≥ frag+末端帶 ＝ area(R_end)`。
⇒ **gate 之作用即把下游 raise 前移為「往後找」**。

惟「往後找」跨過中間宗後，`_reshape_block` 之楔形相鄰守衛（`grep -n "楔形與標的" verify/wf_f4.py`）
必然 raise「不相鄰」——**兩側皆然**（見 1.1 之 A 欄）。
⇒ **E3 之「往後找成功取得末端 winner」分支，在合成幾何下無法不 raise 地走完。**
本案未觸及（見 §二 F-5），故不影響現狀；**列 backlog·非本波處置**。

---

## 二、F-5：E3 fallback **latent 確認**（實測）

| 問 | 答 | 證據 |
|---|---|---|
| 無勝者 fallback（`抵費地末`）是否觸發？ | **否·0 次** | 69 個 bake 檔全掃 `抵費地末` 命中 **0** |
| E3 實際跑在哪些塊？ | 3.5m＝**R1／R6**，皆有 winner | `bake_pf/wf/f4/F.4_整形_退縮3.5m.csv` |

```
3.5m,R1,628-36(1),標的(吞楔形·left),639.46,...
3.5m,R6,628-4(1), 標的(吞楔形·left),776.72,...
```

⇒ 碼註「UC9898 winner G≫area(R_end)→不觸發」**成立**（R6 winner G=776.72）。
fallback 之唯一活證據仍為 `fixture_end_fallback.py`（左右各 5 項綠）。

---

## 三、F-6：被消費源宗與末端帶之交集（**具體化·左右各驗**）

M-5 於 3.5m 消費移除三宗：`628-30(1)@R5`／`628-45(1)@R5`／`628-30(2)@R2`
（`M-5 結算閘3.5m` 名目之 `A0∖P1`）。

**末端帶（`_end_band`）窗只存在於 R6 左**——六塊全被 `_place_pool_parcels` 走過：

```
844x R1   846x R2   850x R3   469x R4   844x R5   21x R6
```

R6 之 21 次呼叫 **21/21 觸發**；**R1~R5 共 3853 次呼叫零觸發**（`M_0725_PF_bake_diag.log`）。

⇒ **被消費之三宗所在塊（R2／R5）根本沒有末端帶窗** ⇒ 本案**無交集**、無「末宗被消費致窗重列」情形。
左右皆同（R2/R5 兩側均零觸發）。

> **結構註（非本案實測·標明之）**：即使他案發生該情形，`_end_band` 窗係**趟1 重跑時現算**
> （`run_step_g` 吃 `parcels₁` 後重新進 `_place_pool_parcels`·無快取），故窗會自動重列；
> 風險不在「窗沒重算」，而在**窗重算後其內候選集是否仍滿足 §4 之保留語意**——此點本案無母體可測，**列 backlog**。

---

## 四、F-10 三項（全部補做·**三個都咬得到**）

### 4.1 F-10-1 結算閘兩側母體同集機檢

`_val0` 母體＝`_A0`（`g_rows` 濾 `推進側別∈{left,right}`）、`_val1` 母體＝`_bp_by_tag[tag]`（未濾）。
新增**對稱差**機檢，合法差類**逐類舉證**（碼註）：

| 類 | 內容 | 舉證條件 |
|---|---|---|
| (A) | `_A0 ∖ parcels₁`：M-5 全額消費之源宗 | `reg.remaining(pid) <= 1e-6` |
| (B) | `parcels₁ ∖ _A0`：趟0 `g_rows` 中**完全不存在**該 pid | `pid ∉ _A0_all` |
| — | **反面**：pid 在 `_A0_all` 卻被側別濾掉 ⇒ 趟0 未計、趟1 計入 ⇒ **口徑不一·紅** | — |

**本案實際對稱差**（名目已載·非「已檢查」四字）：

```
母體對稱差 A0∖P1=['628-30(1)', '628-30(2)', '628-45(1)']（全額消費源）
／P1∖A0=2 宗（未產 G 列）·gid空桶=['_GHOST_(R1)', '_GHOST_(R4)']
```

### 4.2 F-10-2 除守恆閘內之靜默歸零（BK-1 提前結案）

`_pre_price_m5.get(zone, 0.0) or 0.0` → `_pz_of(pid)`：`gid` 非空而 zone 單價查無／≤0 ⇒ **記紅**（含 pid/gid/zone）。
**白名單明列**：僅 `gid == ""` 豁免；且其前提（落該桶者必為 gid/zone **雙落空** ghost）
由 (C) 類硬檢守——gid 空卻**有** zone ⇒ 紅。本案 `gid空桶` 恰為兩 ghost（見 4.1），**前提係量到的、非假設**。

> ⚠️ **機制偏離之誠實聲明**：KL 原文為「loud **raise**」，本實作採 **loud 紅列**。
> 理由＝倉內 **W-2 已裁**：`main()` 頂層迴圈無 enclosing try，裸 raise 會使整個 harness 當場死、
> 其餘閘一列不報，且 stderr 未 reconfigure（cp950）致訊息亂碼。
> 兩者皆「不可靜默通過」（`_ok_bal` 吃 `_pop_viol`）；若 KL 仍要 raise，一行可改。

### 4.3 F-10-3 M-5 三列改為可證偽

判準（**0m／3.5m 同一套**）：

```
award==0  ⟺  ( forced 端數==0  ∨  每一 forced 端皆有明列之不可救理由 )
```

「明列理由」＝ `m_rescue.build_plan` 之 log 對該端輸出「維持強制抵費地」
（`grep -n "維持強制抵費地" verify/m_rescue.py`）。
⇒ 涵蓋「`_ctx_m5` 為空致 `build_plan` 根本沒跑」之漏跑情形（舊版該情形照樣三列全綠）。

### 4.4 咬合實證（`WV_BITE=1`·**未設＝inert·同 `WV_BAKE` 契約**）

注入兩型真缺陷＋一個偽 forced 端。`verify/out/M_0725_F10_bite.log`：

```
⚠️ [WV_BITE·0m]   已注入：F-10-3 偽 forced 端 _BITE_left
⚠️ [WV_BITE·3.5m] 已注入：(B) ['_GHOST_(R1)']／(D) 摘除區段 ['a']

🔴 (B) _GHOST_(R1)：同時在 parcels₁ 與趟0 g_rows，卻因 推進側別∉{left,right}（實為 '池內'）
       被濾出 `_A0` ⇒ 趟0 未計、趟1 計入·兩側口徑不一                                   ×1
🔴 (D) 628-36(1)（gid=G029）之重劃前地價區段 'a' 查無單價或 ≤0（得 0.0）——守恆式禁以
       0 元靜默帶過；可用區段＝['b']                                                     ×11
🔴 forced 端 _BITE_left 於 M-5 log 查無「維持強制抵費地」之明列理由——「救不動」與「漏跑」
   不可區分，禁靜默綠                                                                     ×3

🔴 FAIL  M-5 定點閘0m／無新生閘0m／結算閘0m（本情境 forced 端 1 個／award 0（1 端理由缺漏））
🔴 FAIL  M-5 結算閘3.5m（…）
```

讀數 **52 PASS／18 FAIL**（乾淨為 56／14）＝恰 **+4 紅**，與注入點一一對應。

---

## 五、行號衛生（KL 裁·**一併做完**）

### 5.1 doctrine 入 `CLAUDE.md`（工作紀律）

三條：① 引**符號名 ＋ 可自癒 grep**；② 非用行號不可者**同列記下其成立之 commit**；
③ **禁「某檔無某行」之否定性存在主張**（N0-17-c 變體）。

### 5.2 活碼掃除（**22 處·全部改為符號名＋grep**）

`app.py`(6)／`verify/stepg_pipeline.py`(3)／`verify/wf_f4.py`(3)／`verify/wf_f0.py`(3)／
`verify/probes/probe_stage_order.py`(3)／`probe_capacity_decomp.py`／`probe_capacity_decomp_solve.py`／
`probe_jkstar_legitimacy.py`／`selection_pipeline.py`／`fixture_end_reserve.py`。
**逐筆斷言「舊字串在該檔恰出現 n 次」，不符即停**（禁盲改）；diff 為 **24 insert／23 delete·全屬註解/docstring**。

**實查之腐爛例**（不只那三處）：

| 引用 | 宣稱 | 實測該行 |
|---|---|---|
| `stepg_pipeline` → `wf_f4._reshape_block :1311` | gate 條件1 | `corner = p1 + _smax_f4 * d_hat` |
| `probe_stage_order` → `wf_f4.py:183` | 硬寫 0.0 | **空行**（真址＝`add_syn` 之 `a2=0.0`） |
| `probe_capacity_decomp` → `wf_f4 :284-286` | `_s0_unreachable` | `best = None`（真址 293） |
| `app.py:1667` → `stepg:276/277` | `g_rows` 2dp | `_corner_buffer_S = …` |
| `app.py:6803` → `app.py:6836` | `round(G_conv,2)` | 一句註解 |
| **同一檔內自相矛盾** | `app:1672/1702` 稱 Patch B-2 在 `16717-16732`；`app:9272` 稱在 `16177-16185` | 二者至少一錯 |

### 5.3 文件面

`plan_v4.md` §八 F-2／`CC交接文` §三·§5.4：原行號錨標記作廢並載真值與 +13 位移成因；
§5.4 之教訓改寫為 KL 指出之更利者——**否定性存在主張須綁 commit**。

---

## 六、🆕 覆蓋率洞修補：三個末端夾具納入 `run_all`

`verify/fixture_end_{reserve,fallback,winner}.py` 原本**不在任何自動流程內**——
`run_all.py` `[1/3]` 僅跑 圖8 golden／滑池槽 golden／B-3 欄集閘。
⇒ 三檔以 **subprocess** 納入 `[1/3]`（`fixture_end_fallback` 於 import 期即 `sys.exit()`，直接 import 會帶走 harness）。

⚠️ 本段**不進** `run_verification.results` ⇒ **不動 PASS/FAIL 計數**、亦**不動 P-H 之「161 名目」母體**。

---

## 七、BK-4 裁定與 P-H 前置鐵則

已入 `docs/reports/W-G.4_裁定M_重錨登記.md` **§五**（三路證據＋六條前置鐵則），
R-9／BK-4 兩列由「待裁／🚩上呈」改為「已裁·P-H 依此歸因」。**F-1 已列入 P-H 必驗項**
（P-H 後須以**非 BAKE** 重現 `85.706㎡`／`s∈[-0.0000,3.5114]`／R6 唯一觸發 21/21）。

---

## 八、backlog（有記錄之延後·非「待議」）

| # | 項 | 形狀 |
|---|---|---|
| BK-5 🆕 | E3「往後找」分支必觸楔形相鄰守衛 raise（§1.4） | 或放寬相鄰守衛至「標的與楔形間僅隔被跳過宗」，或明訂該情形即停機上呈。本案未觸及 |
| BK-6 🆕 | 末端帶窗於他案發生「末宗被消費」時，窗重算後候選集是否仍滿足 §4 保留語意（§三） | 需可觸發之母體 |
| BK-1 | ✅ **本波結案**（F-10-2） | — |
| BK-2 | ✅ **本波結案**（F-10-3） | — |
| BK-3 | 非 award gid 絕對護欄 `1e-6` → `max(1e-6, 1e-9×|v0|)` | **P-H** |

---

## 九、本次新增／異動之 log

| 檔 | 內容 |
|---|---|
| `M_0725_F2_end_winner.log` | F-2 夾具·16 項綠＋咬合反例 4 紅 |
| `M_0725_F10_after.log` | F-10 三閘上線後·56 PASS/14 FAIL（名目零增減） |
| `M_0725_F10_bite.log` | `WV_BITE=1` 咬合·52 PASS/18 FAIL（+4 紅） |
| `M_0725_F2F10_final.log` | 全部異動後之終驗（含 run_all 夾具整合） |
