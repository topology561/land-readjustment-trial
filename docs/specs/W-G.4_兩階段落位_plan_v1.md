# W-G.4 兩階段落位 plan v1（KL 域裁 2026-07-23 落地計畫·**勿施工**·待 claude.ai 複驗）

> canonical 域裁＝`docs/specs/W-G.4_KL域裁_兩階段落位_部分面積拆分_Rw側選.md`（裁定A＋B1–B5）。
> 坐實證據＝`docs/reports/W-G.4_§4_兩階段落位_坐實.md`（R1@3.5m 推進序列 dump）。
> 本檔＝純計畫；**本階段勿改引擎、勿烤、勿收綠**。行號基準＝HEAD `1880dd1`。

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
  ⚠️ **域確認題 D-1**：E1/E2 內部次序與 B2「同歸戶合併→同歸戶公設(RD先)」之對映是否需重排
  （現行 E1 佇列序＝距離法非歸戶類別序）——上呈 KL 確認，plan 不擅裁。
- 每筆落位（B5）：
  1. 量池範圍與**左右兩側 18m Rw 範圍**之**跨占寬度**（§四 spec gap 提案）；
  2. 從跨占大之一側、自池邊界**往內**切帶落位（帶軸＝`_strip_axis` 同軸；面積→G 由既有
     `solve_G_binary` 幾何 bisect，S 預算＝**池 s-區間**、非全街廓）；
  3. 落位後池縮小 → **重算兩側跨占** → 下一筆；兩側皆無跨占 → 任一側往內（決定性 tiebreak：
     取池 s-區間較長之側；再同→左，記入 spec）。
- 部分拆分（裁定A）：候選筆所需帶寬 > 池剩餘 s-寬 → 以面積拆分：池內裝滿一段（該段經 G 計算
  且成品須為合法基地），餘額回佇列溢往下一塊（既有 spill 機制）；**每步後池剩餘與所有宗皆須
  通過可建築規定**（寬/深/面積·`get_min_lot_size` 查表·禁字面常數），不過 → 該筆不落此塊（整筆溢），
  禁靜默 clamp。
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
  ⚠️ **域確認題 D-2**：池內調配宗是否計 Rw 側街負擔（於 18m 範圍內落位者）；telescoping 閘
  （:848-863）之 W_final 隨之定義。上呈 KL，plan 不擅裁。

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

## 四、B5「跨占寬度」＝**spec gap**（倉內無現成量法·提案待裁）

**倉內既有**（grep 坐實）：
- 18m Rw 負擔範圍**多邊形**：`_build_corner_range_v2(side_mid, verts, centroid, alloc, shift=18.0, None)`
  ——app.py:14332（左）/14337（右）（W-C §2·v3.1 §5·不扣截角）；惟 session `f3_burden_range_18m`
  （app.py:14341/14356）**只存面積**、多邊形未保留；引擎 ns 未曝。
- 「跨占」既有語意＝街角 PK **跨占面積**（app.py:14497·宗∩街角範圍·面積制）與 W-D.4 跨占分配線
  （wd4_tier_list.py:297）——**皆非**「池×Rw範圍 跨占寬度」。
- ⇒ **「池範圍與 18m Rw 範圍之跨占寬度」無現成量法＝spec gap**·勿逕自定義。

**提案（供 KL／claude.ai 裁·二擇一或另裁）**：
- (a) **寬度制（建議）**：跨占寬度＝(池範圍 ∩ 該側18m負擔範圍多邊形) 於**斜交切線軸**
  （`_strip_axis`·app.py:6851）之 s-區間長——與引擎 S 維度同軸、B5「每配一筆重算」自然遞減；
  需把 `_build_corner_range_v2(…,18.0,None)` 多邊形入 session/ns（純加性曝出）。
- (b) 面積制：跨占＝交集面積（同 PK 慣例）；惟「寬度」字義較遠。
- 邊界：無 SIDE_LINE 側＝無 Rw 範圍＝跨占 0（B5「兩側皆無跨占→任一側往內」涵蓋）。

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

## 六、域確認題彙總（上呈 KL·不 block plan 複驗）

- **D-1** B2 佇列序與 E0/E1/E2 對映（E1 距離法內部序 vs 歸戶類別序）。
- **D-2** 池內調配宗之 Rw 側街負擔計否（影響 telescoping 閘 W_final 定義）。
- **D-3** 跨占量法 (a) 寬度制 vs (b) 面積制（§四）。
- **D-4** 拆分段之最小合法性：拆出段與留池餘額**各自**須≥可建築下限，抑或僅拆出段？（裁定A 字面
  「所有土地（含剩餘調配池）」→ 傾向各自；確認之）。
