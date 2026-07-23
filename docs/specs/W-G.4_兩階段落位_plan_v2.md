# W-G.4 兩階段落位 plan v2（KL 域裁 2026-07-23 落地計畫）

> canonical 域裁＝`docs/specs/W-G.4_KL域裁_兩階段落位_部分面積拆分_Rw側選.md`（裁定A＋B1–B5）。
> 坐實證據＝`docs/reports/W-G.4_§4_兩階段落位_坐實.md`（R1@3.5m 推進序列 dump）。
> **可復現探針**＝`verify/probes/probe_stage_order.py`（env 開關·預設不影響 `run_all`）：
> ```
> WV_PROBE=1 python verify/probes/probe_stage_order.py --setback 3.5 --block R1 --lot "628-37(1)"
> ```
> 行號基準＝HEAD `951e347`（v1 行號已驗訖，v2 未動碼故不變）。
>
> **v1→v2 差異**：claude.ai 複驗（2026-07-23）放行 §二/§三 架構；**D-3／D-4 已裁結案**（§四·§六）；
> 新增 **§七 修復驗收靶**、**§八 波後 backlog**；必辦①探針入倉、必辦②交叉引用更正。
>
> **施工閘**：D-1／D-2 仍待 KL；**其餘部分可即刻進行**。若 KL 答覆不改動 §二/§三 架構 →
> CC 逕進 P1–P5（plan→reviewer→施工→push），施工後由 claude.ai 複驗實作；
> 若答覆改動架構 → 停機出 plan v3。**plan v2 前仍：勿改引擎、勿烤、勿收綠、G006 錨不動。**

---

## 一、現況機制（root cause 對應碼）

**單一序列混排**：`run_step_g` 把街廓內全部宗（原地主＋wf_f4 遞補合成宗 `add_syn`）一起送
`_spatial_order_parcels_v2` 依**投影位次**排序（單一序列），再以 k* 切左右兩組、兩端往中間推進，池＝殘餘：

| 環節 | 引擎（verify/） | app live 複本（#20 四處同改） |
|---|---|---|
| 投影排序 `_spatial_order_parcels_v2` | stepg_pipeline.py:382 | app.py:5956（def）／15460（call）|
| k* 選槽 `_select_pool_slot` | stepg_pipeline.py:714（orchestration 682–756）| app.py:5889（def）／15815（call）|
| 左右分組＋兩端推進 `_advance_block_with_split` | stepg_pipeline.py:486（def·分組 488–496）/525（左迴圈）/596（右迴圈）| app.py:15575 |
| `S_remain = actual_max_proj − left_cum − right_cum` | 左 :547／右 :618 | app 同構 |
| 右端 `_oblique_s_max` | stepg_pipeline.py:585 | app.py:6921（def）|
| 池片（殘餘）`_pool_strips_for_block` | stepg_pipeline.py:767 | app.py:7046（def）|
| 遞補合成宗生成 `add_syn` | wf_f4.py:178（def）；E1:442/582、E2:915/1001/1053 | —（引擎專屬）|
| E3 整形消費 `推進側別`＋`累積S(m)` 排序 | wf_f4.py:1156 | — |

**破鏈**（坐實報告）：`add_syn` 合成宗 anchor＝池片質心 → 投影落在原地主宗之間 → 單一序列**插隊**
→ 原地主末宗（3.5m 之 628-37(1)）被推至 `S_remain=8.57 <` 需 8.81 → |G−幾何|=7.9。

---

## 二、目標架構（裁定B 兩階段）

### 階段1（B1·原位次定案）
- 輸入＝**重劃前土地**（原地主宗；含 F.0 同歸戶合併之「原位次原地變寬」宗與 F.2 搬 a′ 之受宗——
  皆屬既有宗面積變動、位相不變原則既涵蓋）。
- 流程＝現行：街角第1宗（PK winner）＋其餘依 `_spatial_order_parcels_v2` 原位次、k* 選槽、兩端推進。
- 產出＝原地主宗 G/幾何**定案**＋兩側**確定後 ALLOCLINE**（左組末切線＋右組末切線）。

### 池範圍（B4）
- ＝左右確定後 ALLOCLINE ＋ FRONTLINE ＋ BASELINE 所圍。
- **操作化＝現成 `_pool_strips_for_block`**（app.py:7046；stepg:767 已消費）：街廓多邊形 ∩ 池 s-區間
  之帶——街廓閉合多邊形（方案B 直讀）自帶 FRONT/BASELINE 邊、帶之兩端切線＝確定後 ALLOCLINE
  （斜交 `_strip_axis` 同軸）。**零新幾何元件**。
- B4 門檻：池面積 ≥ 最小畸零地規範才進階段2；不足 → 該塊不再收池內調配（溢往下一塊，走既有
  E1 spill／E2 佇列 wf_f4.py:485/536/644）。

### 階段2（B2/B3/B5·池內調配）
- 佇列序（B2）：同歸戶合併入池者 → 同歸戶公設地調配（RD 先）→ 其餘公設/遞補。
  對映現行 E 序：E0（模式一·標的＝既有宗→屬階段1 面積變動）→ E1（7-4 公設距離法）→ E2（7-5 批次）。
  🟡 **D-1（已上呈 KL·未回覆不得施工此段）**：E1/E2 內部次序與 B2「同歸戶合併→同歸戶公設(RD先)」
  之對映是否需重排（現行 E1 佇列序＝距離法非歸戶類別序）；併含「同歸戶合併**就地加寬**是否屬階段1」。
- 每筆落位（B5）：
  1. 量池範圍與**左右兩側 18m Rw 範圍**之**跨占寬度**（**寬度制**·斜切軸 s-區間長·§四 D-3 結案式）；
  2. 從跨占大之一側、自池邊界**往內**切帶落位（帶軸＝`_strip_axis` 同軸；面積→G 由既有
     `solve_G_binary` 幾何 bisect，S 預算＝**池 s-區間**、非全街廓）；
  3. 落位後池縮小 → **重算兩側跨占** → 下一筆；兩側皆無跨占 → 任一側往內（決定性 tiebreak：
     取池 s-區間較長之側；再同→左，記入 spec）。
- 部分拆分（裁定A·**D-4 已裁＝各自**）：候選筆所需帶寬 > 池剩餘 s-寬 → 以面積拆分：
  池內裝滿一段、餘額回佇列溢往下一塊（既有 spill 機制）。
  **D-4 結案（claude.ai 2026-07-23·勿再上呈 KL）**：裁定A 字面「所有土地（**含剩餘調配池**）」
  ⇒ **拆出段與留池餘額「各自」**須 ≥ 可建築下限（寬/深/面積·`get_min_lot_size` 查表·禁字面常數）；
  **任一不過 → 該筆不拆、整筆溢往下一塊**，禁靜默 clamp、禁留半合法段或半合法殘池。
- 池終態＝既有池三則（0 或 ≥MinA·run_verification.py:1027-1028）不變。

---

## 三、改動計畫（檔:行·介面）

### P1 合成宗階段旗標（資料驅動·禁名稱判別）
- `wf_f4.py:178 add_syn`：parcel dict 增 `'配地階段': '池內'`；`build_parcels` 原生宗不帶此鍵（預設階段1）。
- 判別一律讀旗標；**禁**以 `74·` 名稱前綴或塊名/側別判別（泛用紀律）。

### P2 引擎 run_step_g 兩階段化（stepg_pipeline.py）
- :382 `_spatial_order_parcels_v2` 呼叫：輸入過濾＝僅階段1宗（`'配地階段' not in tp`）。
- :486 `_advance_block_with_split`：階段1 照舊（k*/兩端推進·僅原地主）。
- 新增 module 級 `_place_pool_parcels(pool_strips, stage2_parcels, side_ctx, ns, …)`：實作 §二·階段2
  （B5 側選＋池內切帶＋拆分）；於 :727（`_adv_final` 定案）之後、:767 池片結算之前呼叫；產出 rows 併入
  `g_rows`（欄位同構·`推進側別`＝落位側·`累積S(m)`＝該側池內累積，E3 排序語意相容 wf_f4.py:1156）。
- 池片結算 :767：改於階段2 落位後計（池＝階段1殘餘 − 階段2已落位）。
- W/Rw thread：階段2 落位宗續用該側 W 鏈（`_W_prev` 自階段1末值續）——
  🟡 **D-2（已上呈 KL·未回覆不得施工此段）**：池內調配宗是否計 Rw 側街負擔（於 18m 範圍內落位者）；
  telescoping 閘（:848-863）之 W_final 隨之定義。

### P3 app live 複本同改（#20 四處同改鐵律）
- app.py:15460（ordered_v2 過濾）/15575（_advance 階段1）/15815 後（呼叫同一 `_place_pool_parcels`
  ——**單一真相源**：函式放 app.py module 級、入 `_WF_NS_NAMES` harvest、stepg 經 ns 取用，同
  `_oblique_s_max`/`_corner_buffer_S` 先例；**禁 fork**）。
- ⚠️ app live 迴圈實際只跑原地主宗（合成宗僅存在於 wf_f4 引擎路徑）→ app 端改動＝過濾語意
  no-op ＋ ns 曝出；G.3 雙路同源不破。

### P4 閘與 harness（run_verification.py／stepg_pipeline.py）
- 位次=投影序閘 stepg:398-409：作用域改「階段1宗」（合成宗不再在 ordered_v2·閘語意自然收斂）。
- §N3-0 逐宗主閘 :818-832／守恆-帳幾何級 :915-959：**不動**（兩階段後池內切帶 by-construction
  |G−幾何|≤tol；此即修復驗證靶）。
- `K_STAR_EXPECT`（run_verification.py:502-505）/`GSA_EXPECT`/F.0–F.4 baseline：**行為變更→波末重烤**
  （本 plan 施工波之收官條件；本階段不烤）。
- fixture：新增池內落位單測（左右雙向＋兩側無跨占＋池<畸零＋拆分邊界），仿 `fixture_end_fallback.py`
  真檢（非 tautology）。

### P5 wf_f4 消費端
- `_Eng.rows()`（wf_f4.py:143-145）：合成宗 rows 由階段2 產出（推進側別∈{left,right} 保持）→ 介面不變。
- E1 `_reach`/E2 `_e2_optimal`（:502/:873）：改讀階段2 後之真池剩餘；E2 成本帶 `POS_SLACK_AREA`
  假設（位置相依 G 誤差上界）於池內落位下重驗——band-sufficiency 閘（既有）破則 loud。
- E3 `_reshape_block`（:1156 起）：排序鍵 `累積S(m)` 語意相容（P2 保證）；末端塊 fallback（補丁十）不動。

---

## 四、B5「跨占寬度」＝**寬度制（D-3 已裁結案·claude.ai 2026-07-23）**

> **裁定＝(a) 寬度制**。理由：KL 原話「占 Rw 18m 範圍有 **2m 寬／4m 寬**」為**公尺寬度**、非面積。
> 量測軸＝引擎既有**斜切軸** `_strip_axis`（app.py:6851），與 S 維同軸（純技術決定）。
> **勿再上呈 KL。**

**落地式**：
```
跨占寬度(側) = len_s( 池範圍 ∩ 該側18m負擔範圍多邊形 )      # s＝_strip_axis 斜切軸座標
             = s_max(交集) − s_min(交集)                    # 與 S_remain 同維、可逐筆遞減
```
- 18m 負擔範圍多邊形＝`_build_corner_range_v2(side_mid, verts, centroid, alloc, 18.0, None)`
  （app.py:14332 左／14337 右·W-C §2·v3.1 §5·不扣截角）。
- **純加性曝出**：現行僅存面積（session `f3_burden_range_18m`·app.py:14341/14356）→ 需另存
  **多邊形**於 session（新鍵，如 `f3_burden_range_18m_poly`）並入 `_WF_NS_NAMES` 供引擎 ns 取用；
  **勿改既有面積鍵**（既有消費者 app.py:16409 不受影響）。
- 邊界：該側無 SIDE_LINE ⇒ 無 18m 範圍 ⇒ 跨占＝0（B5「兩側皆無跨占→任一側往內」涵蓋）。
- **決定性 tiebreak**（泛用·禁擲硬幣）：兩側跨占相等或皆 0 → 取池 s-區間較長之側；再同 → 左。

**gap 佐證（保留備查·claude.ai 窮舉搜尋複驗屬實）**——倉內既有、且**皆非**本量法：
- 18m 負擔範圍多邊形雖可由 `_build_corner_range_v2(…,18.0,None)` 生（app.py:14332/14337），
  惟 session `f3_burden_range_18m`（app.py:14341/14356）**只存面積**、多邊形未保留、引擎 ns 未曝。
- 「跨占」既有語意＝街角 PK **跨占面積**（app.py:14497·宗∩街角範圍·面積制）與 W-D.4 跨占分配線
  （wd4_tier_list.py:297）——**皆非**「池×Rw範圍 跨占寬度」。
- 倉內**唯一**池交集碼＝app.py:7164 之池-宗**不得重疊**閘（斷言性質），非量法。
- ⇒ 本量法確為新增；已由 D-3 裁定 (a) 寬度制定案（上式），**非自創**。

---

## 五、影響面、風險、回退

- **行為變更**：合成宗 G/位置全數重定（F.3/F.4 六表、G值表、池片、E3 整形、33 群總決算）→
  F.0–F.2 理論零動（僅原地主；閘驗證）、F.3/F.4 baseline 波末重烤。UI（app）零動（P3 no-op）。
- **風險**：
  1. E2 窮舉最優性假設（位置相依成本帶）與池內落位交互——band-sufficiency 閘看守，破即停機上呈；
  2. 拆分產生之段須合法基地——每步查表驗證，不過即整筆溢（禁半合法段）；
  3. Rw/telescoping 語意（D-2）未裁前 W 鏈續用之暫行——閘若破即停機；
  4. 池 s-區間非單片（如 R1 雙片 0.32/35.28）——階段2 只在 ≥最小畸零之片內落位、小片留池（既有
     池三則語意）；
  5. 邊界：N=0 階段2 佇列／池恰＝MinA／兩側皆無跨占——fixture 全覆蓋。
- **回退**：兩階段為**單一碼路**（舊單序列路徑**整刪**·no-silent-fallback·禁雙路徑並存）；
  回退＝git revert 施工 commit（原子波·一 commit 一機制）。

## 六、域確認題狀態

| # | 題 | 狀態 |
|---|---|---|
| **D-1** | 階段2 佇列序與 E0/E1/E2 對映（含「同歸戶合併就地加寬是否屬階段1」）| 🟡 **已上呈 KL·未回覆前不得施工**（影響 §二階段2 佇列與 P5）|
| **D-2** | 池內調配宗計否 Rw 側街負擔 | 🟡 **已上呈 KL·未回覆前不得施工**（影響 P2 W/Rw thread 與 telescoping 閘 :848-863）|
| **D-3** | 跨占量法 | ✅ **結案＝(a) 寬度制**（claude.ai 2026-07-23·§四）·勿再上呈 |
| **D-4** | 拆分段最小合法性 | ✅ **結案＝各自**（拆出段與留池餘額皆須合法·§二）·勿再上呈 |

**施工放行**：D-1/D-2 之外的部分可即刻進行。KL 回覆後若**不改動 §二/§三 架構** →
逕進 P1–P5（plan→reviewer→施工→push），施工後由 claude.ai 複驗實作；**若改動架構 → 停機出 plan v3**。

---

## 七、修復驗收靶（施工後複驗·明列）

| # | 靶 | 判準 | 量法／出處 |
|---|---|---|---|
| V1 | **主症解除** | 628-37(1)@3.5m `|G−幾何| ≤ _acct_geom_tol_per_lot`（post-S0d 0.015）**且** 其 `S_remain` 足額（≥ 所需帶寬，非踩 0.1 下限） | 探針 `probe_stage_order.py --setback 3.5`；§N3-0 逐宗主閘 stepg:818-832 |
| V2 | **階段1 零動** | F.0／F.1／F.2 六表逐格 **zero diff**（僅原地主宗參與階段1，遞補移出序列不得回頭改動原位次結果）| `run_verification.py` F.0/F.2 diff_rows |
| V3 | **守恆全綠** | §N3-0 逐宗主閘（:818-832）＋守恆-帳幾何級（:915-959）＋①' 覆蓋閘 全綠、無 raise | run_all |
| V4 | **池三則不變** | 各塊池終態 `0 或 ≥MinA`（無中間態）| `run_verification.py:1027-1028` |
| V5 | **位次序不變** | 階段1 宗之 `pre_position ≡ _projection_order`；F.0 位次序/毗鄰閘綠 | stepg:398-409、F.0 `pos_viol`/`adj_viol` |
| V6 | **telescoping** | ΣRw_側 == R(W_final) − R(W₀) 逐側綠（D-2 裁定後定 W_final 語意）| stepg:848-863 |
| V7 | **邊界 fixture 真檢** | 新 fixture 覆蓋：① 兩側皆無跨占 ② 池 < 最小畸零（不進階段2）③ 拆分邊界（拆出段/殘池各自合法·D-4）④ 池 s-區間**非單片**（如 R1 之 0.32/35.28）⑤ 左右雙向對稱。**須真檢**（構造已知答案手算對拍），**非 tautology**（前車：`fixture_end_fallback.py` 舊「4項恆等式」因 end_abate 相消而空轉·reviewer 揭）| 仿 `verify/fixture_end_fallback.py` |
| V8 | **E2 最優性未破** | band-sufficiency 閘綠、`_e2_optimal` 可行數 >0 且 opt ≤ 次優 | `run_verification.py:1029-1035` |
| V9 | **雙路同源** | G.3 app-path == 重烤 baseline（P3 為 no-op ＋ ns 曝出，須實證未破）| wg_g3 |
| V10 | **重烤後全綠** | F.3/F.4 baseline 重烤後 `run_all` ALL GREEN（收官條件·**須 push 進 origin 方得報收官**）| `run_all.py` |

> ⚠️ V1–V9 為**施工波**驗收；V10 之重烤**本階段不做**（勿烤 baseline）。

---

## 八、波後 backlog（本波不處理·僅登錄）

- **泛用化 watch（claude.ai 必辦④）**：`app.py:17649` 之 §7 引擎 UI 文案自陳
  「**67 項案例錨定斷言**（六格 G(Σa)、SNAP_WAVG、楔形面積錨）」凍結於 UC9898、
  非 UC9898 資料即 `_is_uc9898` 圍欄擋跑——與本專案「**泛用化為本**」紀律有張力。
  現況為 KL 既有裁定（「引擎不得為 UI 妥協」·列泛化波 backlog），本波**不動**；
  惟兩階段落位新碼**須自始 side-agnostic／資料驅動、零新增案例錨**，勿加深此債。
- 探針常設化：`verify/probes/` 往後凡作為裁定依據之實證，探針一律入倉附重跑指令
  （claude.ai 必辦①確立之驗證紀律）。
