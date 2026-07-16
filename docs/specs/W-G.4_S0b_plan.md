# W-G.4 S0b**＋S0c** 施工 plan（幾何漏歸零·修漏 T1/T2/T3＋**第四源同源修**＋補償碼拆＋三閘＋乙匯出＋甲-2）

> 依據：`docs/specs/W-G.4_規格_v3.md` §N3-0／**§N3-0c**／**§N3-0d**（唯一施工依據）＋ `W-G.4_CC交辦_v3.md`（丙時序第 1 步）。
> 基準 HEAD：`4168319`（規格/交辦 v3＋補丁一＋兩份停機報告已入倉·**病灶原封未動**·已 grep 覆核）。
> **⚠️ 範圍改變（KL 2026-07-16 晚裁·補丁二）**：原「僅 S0b」→ **S0b＋S0c 併段、單次重烤**（S0c 提前插於 §9 原中斷點之前）。
> **代價**：S0b 不單獨收官。**理由**：錨只重定一次（F.1／§N4／§N5 之錨否則須重定兩遍）。
> **仍不動** §N1 buffer 幾何化、§N2 街角、§N3 targeting、§N5 下游——彼等為 S1~S5，本 plan 一律不觸。
> 前置採認：(甲) 全庫全掃已於 `46feb2f`（`docs/reports/W-G.4_S0b_甲全庫全掃盤點.md`）完成；本 plan 逐處 grep 現 HEAD 覆核（禁採信舊報告·N0-17-c）。
> N0-16：harness 引擎與 app.py **同源**（`_block_strip = ns["_block_strip"]` 實證·見 §T2-#3/#4）；T2 正確性靠**②不變量閘＋③預測差量閘**，不靠 UI 錨（④）。

---

## 0. 現 HEAD grep 覆核（禁採信舊報告·逐處坐實）

四 pattern 於 `100cfa3` 之病灶點確認未動：

| # | 檔:行 | 現況 code（覆核） | 判定 |
|---|---|---|---|
| T2-1 | `verify/stepg_pipeline.py:707-719` | `_uunion_d(allocated_polys).buffer(0.001)`→`blk_poly.difference()`→`g.area >= 1.0` | 病灶·改 |
| T2-2 | `app.py:15247-15263` | 同構（`# 補充 2：buffer(0.001) 消除浮點碎邊`） | 病灶·改（N0-16 同源同碼·須與 T2-1 逐字一致） |
| T2-3 | `verify/wf_f1.py:323-328` | `unary_union(list(new_polys.values())).buffer(0.001)`→`.difference()`→`area >= 1.0` | 病灶·改 |
| T2-4 | `verify/wf_f4.py:715-721` | `unary_union(list(npolys.values())).buffer(0.001)`→`.difference()`→`area >= 1.0`（E3 段·僅供 S=0 診斷·見 §T2-#4） | 病灶·改 |
| 補償-1 | `verify/wf_f1.py:239-243` | `_fuse`：`u.buffer(0.0011).buffer(-0.0011)` | 拆·改 loud-assert |
| 補償-2 | `verify/wf_f4.py:1143-1147` | `_fuse`（`_reshape_block` 內）：同上 | 拆·改 loud-assert |
| 補償-3 | `app.py:15509` | `_uu_off([_poly_l, _poly_s]).buffer(0.001).buffer(-0.001)`（Phase 8 抵費地<5㎡碎片合併·防護二） | 拆（見 §補償-3·WATCH） |

**無關·不動（甲全掃已列·本波不觸）**：`.difference()` 9 處（`app.py:4107/4175/6224/7108/15913/15916/15917` 等·屬 W-A.2 殘料/道路/截角/offland 診斷）＋`area>=1.0` 4 處（`app.py:3251/6237/12876/16713`·非池片）。

---

## 1. T2 池片建構主修法（四處·核心）

### 1.0 機制（統一表述）

業主宗沿 **d_hat 軸**（＝FRONT_LINE 方向·s 軸）以 `_block_strip` 逐帶切出，切線 ⊥ allocation_dir（∥地界線）。**兩端往中間排**：左組自 `corner_pt`(p1) 沿 `d_hat` 推進、右組自 `end_pt`(p2) 沿 `d_hat_rev`(=−d_hat) 推進，中央殘餘＝調配池。

**T2 定義**：池片改為在**業主宗未占之 s-互補區間**上、以**同一 `_block_strip`／同切線**直接切出，**廢 boolean difference、廢 buffer 膨脹、廢 `area>=1.0` 過濾**。

街廓 s 值域 ＝ `[s_min, s_max]`（街廓頂點在 d_hat 上投影之**完整**值域·§N3-0「鋪滿之 s 域須涵蓋街廓在 ALLOC_LINE 投影之完整值域」）。分割為：

```
街廓 = [p1 楔形: s∈[s_min, 首業主宗s起]]        ← 池
     + [左組業主宗帶…]                          ← 宗
     + [左 forced 帶 (若有): s∈[0, left_buffer_S]] ← 池（見註）
     + [中央池帶: s∈[left_cum_S, s_max_biz_R]]   ← 池
     + [右組業主宗帶…]                          ← 宗
     + [右 forced 帶 (若有)]                     ← 池
     + [p2 楔形: s∈[末業主宗s迄, s_max]]         ← 池
```

- 每片 ＝ `_block_strip(block_poly, d_hat, corner_pt + s_a·d_hat, s_b − s_a, allocation_dir)`。相鄰片共用**同一條** s=s_a 切線（同 n_hat=rot90(allocation_dir)）→ **精確鋪滿·無縫·無重疊·無 boolean**。
- **s-區間之取得（優先·最精確）**：用**已存累積 S 座標**——左組 `[left_buffer_S, left_cum_S]`、右組自 `end_pt` 內推 `right_cum_S`、forced 帶 `[0,left_buffer_S]`/`[s_max−right_buffer_S, s_max]`、中央 `[left_cum_S, actual_max_proj−right_cum_S]`——**非** 對 cut_coords 做浮點投影（投影僅作交叉驗證）。理由：累積 S 即業主宗 `_block_strip` 之真實切線位置，用之則切線逐位一致。
- **末筆楔形**：`_block_strip(last_cut → 街廓端)`；其非矩形係 ALLOC_LINE 與 BLOCK/BASELINE 不平行之真實幾何（非毛刺），一律計入池（§T1）。
- **piece 身分**：T2 產出之池片＝{p1楔形?, 左forced?, 中央, 右forced?, p2楔形?}——與現 baseline（`difference` 後 `area>=1.0` 濾）之**真實池片一一對映**，僅各自 `+= net_leak`（預測差量閘③）；T1 或會新留原被丟棄之末筆楔形（預測差量閘⑤·可歸因）。

**T3 遵守**：池仍為**幾何**（`_block_strip` 切出多邊形），**非帳目式**（§N3-0 T3 否決帳目式·§N1 forced=range 為幾何量）。

### 1.1 §T2-#1 `verify/stepg_pipeline.py:689-763`（harness 引擎）

- **可用變數（reviewer 覆核·分兩類）**：
  - **✅ 在 pool-build 點(689) scope**：`blk_poly`、`blk_area`、`d_hat`(338)、`corner_pt`(331)、`allocation_dir_block`(342)、`_left_buffer_S`/`_right_buffer_S`(496·673-675)、`left_cum_S`/`right_cum_S`（`_adv_final[...]`·655）、`left_results`/`right_results`（各 `_res['cut_coords']`）。
  - **🔴 reviewer 抓錯·NOT in scope**：`actual_max_proj`/`end_pt`/`d_hat_rev`（定義於 `_advance_block_with_split` **閉包內** 569-577·閉包 return dict(652-659) **不含**·pool-build 點在閉包外·直取＝NameError）。**改法**：不倚賴此三者——`s_domain=(s_min,s_max)` 由 **helper 內部**自 `block_poly` 頂點對 d_hat 投影（相對 corner_pt）現算（見 §1.5）；如需 `actual_max_proj` 則於呼叫點以 561-572 原式重算（`max(投影)`）。**app 側同構**（閉包 14951-15164·同缺·同補）。
- **改法**：以 `_uunion_d = ns/_SP_d` 現有 shapely helper，**移除** 707-708 之 `.buffer(0.001)`+`difference`、移除 713-721 之 `area>=1.0` 過濾；改呼叫**新 helper `_pool_strips_for_block(...)`**（見 §1.5）產生 `offset_geoms`（list[Polygon]），其餘（`_pool_total_blk`、g_rows 抵費地列 733-761、`_min_block` 收斂旗標）**不動**。
- **鋪滿自檢**：新 helper 內建 `|Σ(業主宗帶 + 池帶) − blk_area| ≤ 0.01`（§閘②-鋪滿），破則 loud raise。

### 1.2 §T2-#2 `app.py:15229-15320`（app 引擎·N0-16 同源同碼）

- 與 §T2-#1 **逐字同構**（same helper、same 變數名·app 側 `left_cum_S=_adv_final['left_cum_S']` 15216-15217）。改動須與 stepg **byte 級對映**（G.3 三重確立之基礎）。
- 15267-15274 之「碎裂孤島」`st.warning`：保留（>1 池片仍可能·forced+中央）；但語意由「夾擠 bug」轉為正常（多 forced 帶）——文案微調或保留，**不影響引擎**。

### 1.3 §T2-#3 `verify/wf_f1.py:322-338`（F.1 R1 整形段）

- **關鍵**：wf_f1 **已 harvest `_block_strip = ns["_block_strip"]`**（142）＋自有 `strip_at(cum_S,S)` 閉包（168·wrap `_block_strip`）；業主宗（`new_polys`）本就以真 `_block_strip` 切出。**僅 322-328 池重算是抄寫病灶。**
- **可用變數**：`block_poly`、`d_hat`(153)、`corner_pt`(154)、`alloc_dir`(155)、`left_buffer_S`(163-166)、`cos_dn`(158)、`strip_at`(168)、`new_polys`、`cum`（301 後＝左組末端 s）、`right`（右側未動·`_poly_of(r)`）、`wedge`(195)。
- **改法**：移除 323-328；改用 `strip_at` 於互補 s-區間切池帶。R1 雙情境 `left_buffer_S=0`（163 註·不寫死·依 forced_map）。左組占 `[0, cum]`（含吞楔形之標的）、右組占其投影區間、中央池＝`strip_at(cum, 右組起−cum)`；末筆楔形依 s 值域。`pool_rows`（330-337·臨正街長診斷）沿用新 `pieces`。
- **鋪滿自檢**：同 §閘②（`|Σ − block_poly.area| ≤ 0.01`）。

### 1.4 §T2-#4 `verify/wf_f4.py:701-729`（E3 整形段）

- **現況辨析（重要·免誤改）**：wf_f4 之池**總量**已由**守恆**得之（`pool_final[blk] = poolE[blk]`·711·comment 701-704 自承 buffer-free）；715-721 之 `difference(buffer(0.001))`→`pieces` **僅供 724-729 之「S=0 池片殘留」診斷**（`_front_len_of(g)<0.5`），**不供總量**、**且現不進 g_tab**（S0a：E3 不進終態·`g_tab=build_step_g_tables(sgE)`）。
- **為何仍須改（#20 修一次到位）**：§N5（S5）令 reshape 回寫 g_tab 後，E3 幾何進終態、此漏原路返回。故 S0b 先修乾淨。
- **改法**：`_reshape_block`（1074）已有 `strip_at`(1109)/`d_hat`(1086)/`corner`(1097/1104)/`alloc_dir`(1087)/`buf`(1099/1106) 在 scope，且持 `grp`(反整側)＋`other`(另側)＋`block_poly`。→ **`_reshape_block` 回傳增加 `pool_polys`**（以 `strip_at` 於互補 s-區間切出之池帶 list），`compute()` 收入 `pool_polys_by_blk`；E3 之 715-721 改用 `pool_polys_by_blk[blk]`（無則對未整形塊仍走互補切·見下），**S=0 診斷 724-729 照舊跑於新 pieces**。
- **未整形塊**（`new_polys_by_blk` 僅含被 `_reshape_block` 動過之塊）：其 `npolys` 來自 E 世代原 cut_coords；此類塊之池帶亦以「互補 s-區間 `_block_strip`」切出（需 d_hat/corner/alloc·由 `fl`(722)＋`cad` 重建，同 `_reshape_block:1083-1093 之式`）。**helper 化**（§1.5）使 #1~#4 共用同一切帶邏輯。
- **鋪滿自檢**：同 §閘②。

### 1.5 共用 helper（DRY·四處同源）

新增**模組級純函式**（建議置於 app.py `_block_strip` 鄰近·由 `ns` harvest·verify 端 `ns["_pool_strips_for_block"]` 取用；與 N0-16 同源原則一致）：

```
_strip_axis(d_hat, allocation_dir) -> (m_hat, denom)
_strip_s_range(geom, d_hat, corner_pt, allocation_dir) -> (s_min, s_max)
_pool_strips_for_block(block_poly, d_hat, corner_pt, allocation_dir,
                       biz_polys, _label='') -> list[Polygon]
  # biz_polys: 業主宗**實際幾何** list[Polygon]（cut_coords 所建·同源）
  #   → s 區間由 helper 自 biz_polys 之切線座標取得（非由呼叫端給累積 S）
  #   → 免依賴各呼叫端相異之 buffer／cum_S 慣例；forced 帶／末筆楔形自然落入互補區間
  # s_domain 由 helper 內部自 block_poly 頂點於同一 s 軸現算
  #   → 免倚賴閉包內之 actual_max_proj（reviewer WARNING B）
  # 回傳互補區間之 _block_strip 帶（p1楔形/forced/中央/p2楔形）
  # 內建：鋪滿閘（以**實際宗幾何**校驗）＋不重疊閘（池-池／池-宗）＋T1 退化網（雙路 loud）
```
- **⚠️ 實測校正（2026-07-16·取代本節原「對 d_hat 投影」之述）**：`_block_strip` 之切帶係以
  **n_hat＝rot90(allocation_dir)** 為邊界方向之**平行四邊形**；ALLOC 僅在**繪圖公差內** ⊥ FRONT
  （UC9898 實測 2.6°–5.3°，`stepg:344-349` 之 ⊥ 閘容差 0.15）→ 切線**斜交**。故**禁以正交投影
  `(p−corner)·d_hat` 量 s**（量不到切線位置：實測 R1 `Σ[(街廓∩slab)−宗]＝346.89㎡`、鋪滿殘差
  **93.21㎡**）。**正確式＝斜交切線座標**：點 p＝bp＋t·d̂＋u·n̂，取 m̂＝rot90(n̂)（∴n̂·m̂＝0）得
  **`t ＝ ((p−bp)·m̂)/(d̂·m̂)`**（`_strip_axis`／`_strip_s_range`；n_hat 取法逐字對映 `_block_strip`，
  含 allocation_dir 缺值退 rot90(d_hat) 之正交近似）。改用後 slab 差額 **346.89→0.0000**、
  殘差 **93.21→0.1547**（餘量＝第四源·見 `docs/reports/W-G.4_S0b_第四源_宗S捨入_停機上呈.md`）。
  **教訓**：首版合成測用 `alloc ∥ d_hat`（正交）全綠＝**失敗考古 #7**（fixture 自造只測自己的想像）；
  **斜交是本案常態（CLAUDE.md §8 明載），正交才是特例** → 合成 fixture 必含斜交 2.6°/5.3°/12°。
- **入參皆在各呼叫點 scope**：`block_poly`/`d_hat`/`corner_pt`/`allocation_dir`（=allocation_dir_block）四者於 stepg:689／app（池建構點）／wf_f1:322／wf_f4（`_reshape_block`/E3 由 `fl`+`cad` 重建·同 wf_f1:150-158 式）皆可取；`biz_polys` 即 `allocated_polys`／`new_polys.values()`／`npolys.values()`。**不需** 閉包內之 `actual_max_proj/end_pt/d_hat_rev`。

- **同源保證**：#1(stepg)/#2(app) 直接呼叫；#3(wf_f1)/#4(wf_f4) 亦呼叫同一 harvested helper（`strip_at` 之等價·因 helper 內用 `_block_strip`＋同 corner/d_hat/alloc）。→ 四處**單一真相源**、根絕「抄寫複本各自漂移」（#20 根因）。
- **⚠️ 設計裁決（送 reviewer）**：helper 置於 app.py 抑或獨立 `verify/` 模組——若置 app.py，wf_f1/wf_f4 經 `ns` 取（已有先例 `ns["_block_strip"]`）；若獨立模組，app.py `import`。**傾向前者**（同源、harvest 既有機制）。reviewer 核可置放點。

---

## 2. T1 防護網（`area>=1.0` → 寬度退化判定）

- **廢** 四處之 `g.area >= 1.0` sliver 過濾（§N3-0 T1·面積是二維投影·不得判一維退化）。
- **改** `g.buffer(-1e-4).is_empty` 退化判定：退化＝boolean 毛刺（消除）；非退化＝**真碎片·一律計入池**。
- **T1 為 T2 之殘餘防護網**：T2 精確鋪滿後**不產生** boolean 毛刺 → **T1 應永不觸發**。**觸發即 loud warn 入報告**（no-silent-fallback·代表 T2 未做乾淨·回歸訊號）。
- `ε=1e-4` 依據＝**數值極限**（min_width 3.5m 之 ~1/35000·退化界·甲-2 ✅有依據）。
- 註：T2 helper 內若已精確鋪滿，池帶本不含毛刺；T1 僅在「helper 回傳片再過濾」之防線位置設一次（不散置）。

---

## 3. T3 否決帳目式（**無 code 改動·僅記錄**）

§N3-0 T3：否決「池改帳目式（街廓−Σ配地真面積·不做 boolean）」。本 plan 之 T2 **維持池為幾何**（`_block_strip` 多邊形），符合 T3。**wf_f4 之 `pool_final[blk]=poolE[blk]`（帳目總量）保留**（其為守恆總量記帳·非池片幾何來源）；池**片幾何**改由 §T2-#4 之 `strip_at` 切出——帳（總量）與幾何（片）於 §閘③「池帳−池幾何≤0.01」對齊，**不分岔**。

---

## 4. 補償碼連根拆（三處）

### 4.1 `verify/wf_f1.py:239-243` `_fuse`

- 現：`u = unary_union([a,b]); if u.geom_type!="Polygon": u = u.buffer(0.0011).buffer(-0.0011)`。
- 註 235-238 自承：楔形已被 stepg `buffer(0.001)` 侵蝕 1mm → 縫 → 閉運算彌合。
- **T2 消滅侵蝕後**：楔形＝未侵蝕之真實池楔、與 strip 連續 → `unary_union` **本就單一 Polygon**。
- **改**：拆 buffer 閉運算 → `u = unary_union([a,b]); if u.geom_type != "Polygon": raise RuntimeError("🔴 T2 後 _fuse 仍非單一 Polygon（strip/楔形有真縫＝T2 未做乾淨），停")`（loud·no-silent-fallback）。

### 4.2 `verify/wf_f4.py:1143-1147` `_fuse`（`_reshape_block` 內）

- 同 4.1（F.4 類比）。同改。

### 4.3 `app.py:15509` Phase 8 抵費地<5㎡碎片合併（防護二）

- 現：`_merged = _uu_off([_poly_l, _poly_s]).buffer(0.001).buffer(-0.001)`（雙向 buffer 消縫·15497 註「防護二」）。
- **改**：拆 buffer → `_merged = _uu_off([_poly_l, _poly_s])`。
- **⚠️ WATCH（送 reviewer·可能牽 §N5）**：Phase 8「<5㎡ 碎片自動合併」本身之 `<5㎡` 為**殘餘定閘候選**（甲-2·§N5 重審）。T2 後池片為精確帶，同塊之兩池片（如 forced 帶＋中央帶）**s-不相鄰** → `unary_union` 成 MultiPolygon → 現碼 15515-15521 取最大 geom（**丟小片幾何·保其面積入帳**）＝**帳/幾何分岔**（正是 T2 欲消者）。
  - **S0b 最小改**：拆 buffer（如上）；並將「取最大 geom」路徑加 loud warn（`若 _merged 非單一 Polygon → warn「Phase 8 合併產生 MultiPolygon·§N5 重審」`），**由新 §閘③（池帳−池幾何）把關**——若因此紅，即為真訊號、上呈（不靜默 take-largest）。
  - **替代（若 reviewer 認為 S0b 不宜留半殘）**：S0b 暫**停用** Phase 8 <5㎡ 合併（池片保原樣·由 §N5 統一處理碎片消解）。**此為設計裁決·標旗送 reviewer**（傾向：拆 buffer＋loud warn＋靠閘③把關·不停用·保最小侵入）。

---

## 5. 必立三閘（皆 0.01·依據＝幾何精度上限）

### 5.1 白縫閘（散文閘→碼閘·`app.py:15904-15932`）

- 現：offland/白縫量算於 `st.expander`(15856) 內、`_uncov`(15916)＝`_offland.difference(_off_u).area`、寫入 `'池區未成抵費地(白縫㎡)'`(15929)·**僅 UI 診斷·無閘**（run_verification/run_all/tests 命中 0·N0-17-b 教科書散文閘）。
- **立**：每街廓加碼閘 `if _uncov is not None and abs(_uncov) > 0.01: st.error(...白縫破·具名街廓＋白縫㎡·停機③族·上呈)`。
- **🔴 reviewer WARNING E（必守）**：`_uncov`(15916) 位於 `try`(15912)…`except Exception: pass`(15920) 內——閘**須置於 15921 之後（try 外）**，否則 `st.error`/`raise` 之前若走 assert 會被 15920 靜默吞成非閘（教科書套套邏輯）。落點：try 區塊結束後、`_rows_gap.append` 之外層迴圈末端逐街廓判。
- **並須新立於 harness**（現僅 app.py UI·N0-17-b 須指碼位置）：於 `verify/run_verification.py` 或 stepg 池片建構後加**同義白縫閘**（池區未成抵費地＝0·±0.01），使 run_all 覆蓋。**⚠️ 設計裁決·送 reviewer**：白縫之定義（offland − 已畫抵費地）於 harness 側之等價量測點——傾向於 T2 helper 之鋪滿自檢即涵蓋（Σ池帶＝offland 全體→無「未成抵費地」殘餘）；若如此，白縫閘＝鋪滿閘之推論、UI 側 assert 為顯性化。reviewer 核。
- 依據＝**幾何精度上限**（shapely double·~100m 街廓下 1e-2 保守界·甲-2 ✅）。

### 5.2 覆蓋閘＋不重疊兩級（**KL 2026-07-16 裁改·原 Σ 式已廢**）

⚠️ 原「`|Σ全片幾何 − 街廓面積| ≤ 0.01`」**廢**——既存第四源（宗 S 2dp 捨入·N0-18 推論一）致 Σ 式與不重疊閘**聯立不可滿足**，且 Σ 式紅之成因是**重疊（重複計算）非漏**。改為：

- **①' 覆蓋閘**：`|union(全片幾何) − 街廓面積| ≤ 0.01`（依據＝幾何精度上限）。**S0b 必綠**（實測 **0.0000**）。
- **②-池**：池-池／池-宗交集 ≤ **1e-6**（依據＝數值極限）。**S0b 必綠**（實測 **0**）。
- **②-宗（圍堵閘·本波即立真碼閘）**：`宗-宗重疊 ≤ (宗數−1) × 0.005 × 分配深度`（逐街廓）。依據＝**2dp 捨入半量子 × 深度**之機制推導上界。**超出即另有病、立紅停機**；**S0c 後收 ≤1e-6**。實測 R1：0m 0.1547／3.5m 0.2597 vs 上界 (5−1)×0.005×32.97＝**0.6594** ✅。
  **停機② 已全域實證**（`4168319`·R1–R6 × 雙情境全綠·餘裕 2.5×–4.5×）→ **N0-18／圍堵閘之推導經實測成立**；S0c 併入後此閘即收 1e-6。
- **③ 池帳−池幾何 ≤ 0.01**（保留）。
- **⚠️ 間隙側圍堵閘「不立」（KL 2026-07-16 晚裁·停機② 選項 (a) 駁回）**：S0c 後相鄰宗共用同一條捨入切線，**縫與疊 by construction 同時歸零**——為即將消滅之現象立閘＝**死碼**。
- **Σ 式降為診斷輸出**（印殘差＋宗-宗重疊＋**縫量**）。**S0c 後縫與疊應歸 0**；**不歸 0 即另有病、停機**——此即 Σ 診斷之保留理由（S0c 收斂之量測證據）。
- 落點：T2 helper 內建自檢＋`verify/run_verification.py`（F.2/F.3/F.4 各段 `results.append`）。

### 5.3 守恆閘收緊（真閘·6.0/1.0 → 0.01）

**⚠️ KL 2026-07-16 裁改：原「6.0/1.0 → 0.01」廢**（依據錯配·N0-17-a／N0-18 推論三——現行式為**帳-幾何混合閘**，誤差源含每宗 G 捨入 ±0.005＋第四源重疊，與 0.01「幾何精度上限」不同類，照收必紅）。改**拆兩級**：

**🔴 KL 2026-07-16 三度裁改（補丁三 §二）：帳對幾何閘＝兩級化。⚠️ 前版「`宗數×0.005 ＋ 圍堵界`／S0c 後收 `宗數×0.005`」因 claude.ai 之維度錯已廢**（以 G 之**面積**量子冒充 S 之**長度**量子×深度·≈45 倍 → 停機③ `b68e7c1` 四閘同破）。

- **守恆-幾何級**：`|union(宗+池) − 街廓| ≤ 0.01` ＝ **①' 覆蓋閘同一條**（勿重複立閘）。**0.01 志向不變。**
- **🆕 逐宗主閘（新增·緊閘·志向所在）**：`|G_i − 幾何_i| ≤ 0.005×分配深度 ＋ tol(0.01) ＋ 0.005`（逐宗）。
  依據＝S 長度捨入半量子×d(面積)/dS ＋ bisect 容差 ＋ G 面積捨入半量子（**皆已 ruled·無新常數**）。
  **作用**＝任何非捨入成因之病灶於逐宗層立紅、**不被街廓 Σ 之正負相消淹沒**。斜交因子 ≤1.004 由 tol 吸收。
- **守恆-帳幾何級（逐街廓 Σ）**：`|ΣG ＋ 池幾何 − 街廓| ≤ 宗數×(0.005×深度 ＋ tol ＋ 0.005)`（＝逐宗上界之和·三角不等式）：
  `verify/stepg_pipeline.py:807`（→`841` raise 停機③）＋`app.py:15341`（→st.error）。
- **全區**（`cons_resid`）＝**逐街廓加總**：`verify/run_verification.py:889`（F.2·現 `6.0`）、`951`（F.3·現 `6`·AND `verdict_all_green`）、`1009`（F.4·現 `6`·AND `verdict_all_green`）。**含 fail-detail 重複條件同步改**；label 文案同步。
- 6.0／1.0 之「殘餘定閘」定性不變；替代值**非 0.01**，而是上列原理式。
- **窮盡性（N0-17-c·已 grep 坐實·清單）**：搜 `cons_resid`／`_resid`／`守恆`／`conserv`。全庫 `cons_resid` gate 僅上列（run_verification 三處＋fail-detail·wf_f2/f3/f4 之 `cons_resid` 皆 assignment 入 anchors dict·非 gate）；逐街廓 gate 僅 stepg:813＋app.py:15341。`conserv` 命中 0（claude.ai 前誤因·regex 盲）。`app.py:7752-7904 _resid` 為 `ownership_residential_holdings` 假陽性（substring）。**無其他守恆 gate。**
- 依據＝幾何精度上限（T2 後幾何級守恆本應 ≤浮點·0.01 為 6 數量級寬鬆）。**理由（改必立）**：T2 驗收不靠守恆閘（靠預測差量閘③④），但**永久回歸保護靠它**——不收緊則明日任一波重引 0.5 皆全綠（白縫活四波之機制）。
- **⚠️ 順序**：守恆閘收緊須**在 T2 修畢、全譜系重烤綠之後**方 commit（否則現值 0.03~0.77 立紅）。本 plan 施工序（§9）已排。

---

## 6. (乙) UI 匯出升級 7 項（純 UI·不碰引擎·與 T1/T2 同一 push）

標的：`app.py:export_legal_excel`(1635)＋Sheet-1 對照清冊(1660-1699)＋Phase 7 UI(16135-16194)。現況：headers1(1666)＝`['原地號','原面積(㎡)','所屬街廓','暫編地號','應分配G(㎡)','幾何分配(㎡)','增減(㎡)','街角地']`；全 `round(...,2)`；抵費地列(1684-1695) 名 key＝`暫編地號`寫入原地號欄、幾何塞原面積欄、G 空。

| # | 缺 | 改法 |
|---|---|---|
| 1 | 街廓面積欄 | headers1 增 `'街廓面積(㎡)'`；業主宗/抵費地列皆填 `r.get('街廓面積(㎡)')`（g_row 已有·stepg:739/app 同） |
| 2 | 小數 2→≥4 位 | 對照清冊數值欄改 `round(x,4)`（或匯出未捨入值）——628(5) 應配 223.44/幾何 223.45 差 0.01＝**整個閘寬**·2 位吃閘 |
| 3 | 情境標記 0m/3.5m | `export_legal_excel` 增參數 `scenario_tag`；Sheet-1 增 `'情境'` 欄（或檔名/分頁標）·兩情境不撞名 |
| 4 | 階段標記 trunk A/B/E | 增 `'階段'` 欄（trunk A=F.0／E=終態）·避免誤判（claude.ai 曾差點誤判此檔為終態） |
| 5 | 終態 trunk E 匯出 | 現僅吐 F.0（g_rows＝Step G）；增終態 g_tab（F.4/sgE）之匯出路徑——**F.0 與 E 兩錨都要**（§N1 forced=range/池三則/鋪滿閘全在終態） |
| 6 | 池片穩定 key | 抵費地列 key 改 **s_rel 起訖**（如 `R5-抵費地@s[a,b]`）·非序號——UI `R5-抵費地-2`＝F.4 `R5-抵費地-1`＝同片·**對拍禁以名稱為 key** |
| 7 | 池片幾何另立欄 | 抵費地列現塞原面積欄/G 空 → 池片幾何入 `'幾何分配(㎡)'` 欄·原地號/應分配G 標「—」明確 |

- **N0-16**：乙屬**④接線對拍**·目的＝T2 動 app.py 後之接線保證＋匯出泛化基建·**非** T2 正確性來源。
- **不碰引擎**：僅改 `export_legal_excel` 與 Phase 7 UI 之欄位/格式/新增終態匯出呼叫；g_rows/g_tab 資料來源不動。

---

## 7. (甲-2) 閾值回溯盤點（12 項·三分類＋依據）

| # | 閾值 | 位置（檔:行） | 分類 | 依據／處置 |
|---|---|---|---|---|
| 1 | 白縫 `<1㎡` | `W-D.2_plan:83`／`W-D.1.3:201`（**散文·無碼**） | **散文閘** | 🔴 N0-17-b·**本波立碼閘 ≤0.01**（§5.1·幾何精度上限） |
| 2 | `area >= 1.0` | 四病灶處 | 濾網常數 | 🔴 殘餘定閘（與守恆 1.0 自洽盲區）·**T1 廢**→`buffer(-1e-4).is_empty` |
| 3 | `buffer(0.001)` | 四病灶處 | 濾網常數 | 🔴 病灶·**T2 廢** |
| 4 | `buffer(0.0011)` | wf_f1:242／wf_f4:1146／app.py:15509 | 補償常數 | 🔴 補償碼·**T2 後拆**（§4） |
| 5 | 鋪滿 `≤0.01` | S0b 新硬閘（§5.2） | **真閘（新）** | ✅ 幾何精度上限 |
| 6 | 交集 `≤1e-6` | S0b 新硬閘（§5.2） | **真閘（新）** | ✅ 數值極限 |
| 7 | 守恆·全區 `<6.0` | **`run_verification:889/951/1009`（真碼閘）** | **真閘** | 🔴 殘餘定閘·**必立·收 6.0→0.01**（§5.3·43萬元/次） |
| 8 | 守恆·逐街廓 `<1.0` | **`stepg:813`／`app.py:15341`（真碼閘）** | **真閘** | 🔴 殘餘定閘·**必立·收 1.0→0.01**（72,059元/街廓） |
| 9 | T1 `ε=1e-4` | S0b T1（§2） | 真閘（新） | ✅ 數值極限（min_width 1/35000） |
| 10 | 抵費地碎片 `<5㎡` | `app.py:15489`（Phase 8） | 濾網常數 | ⚠️ 殘餘定閘·待歸因（§N5 重審·**S0b 不改閾值**·僅拆其 buffer 補償） |
| 11 | E3 整形 `0.1` | `wf_f4:709`（`abs(new_area−old_area)>0.1` 整形守恆） | 真閘 | ✅ **已歸因（KL 2026-07-16 裁·補丁三 §三-1·由「待歸因」升格）**：其破因＝**量子項**（停機③ 坐實 R1 0.16 ≈ `0.005×32.97=0.165`）→ 閘寬改 **`整形涉及宗數 × (0.005×深度 ＋ 0.005)`**（同帳對幾何式·**範圍限整形集合**；R1 一宗＝**0.170**）。註：整形係「重切既有宗」故無 bisect tol 項。 |
| 12 | bisect `tol 0.01` | `solve_G_binary:6712`／`_bisect_area` | 真閘 | ✅ 幾何精度上限（2dp 顯示層一致） |
| +補 | `UNCOVERED_TOL 0.05` | `app.py:4033/4112/4121/**4182/4191**`（**5 處**·reviewer 補全·W-A.2 殘料·**非白縫**·辨析陷阱） | 真閘 | ⚠️ 待歸因（暫標·W-A.2 域·非 S0b 標的） |
| +補2 | `WEDGE_AREA_ANCHOR=5.30 ±0.05` | `verify/wf_f1.py:31/196`（R1 楔形量測錨·`量測為準`）／`wf_f4:58 F1_REVERIFY`（僅**身分**錨·不變） | 真閘 | 🔴 **T2 直接衝擊·且已由停機② 實測坐實遠大於預期**：不僅 net_leak（+0.19/+0.17 > ±0.05 tol），**更因 N0-19 之 s-帶分解使「片」之身分本身改變**——實測 R1 0m 之 p1 帶＝**0.07㎡**（非 5.30；舊 5.30 連通碎片於 s-帶分解下已併入其所屬帶）。**依 §N3-0d：單次重烤後重量測、中心值重定；5.30↔0.07 之對映由實測給出，不做讀碼考古。** `±0.05` tol（量測 wiggle·無原理依據）標 `⚠️ 殘餘定閘·待歸因`。身分錨 `TARGET_ANCHOR`/`F1_REVERIFY` **不變**。**🔴 預授權停機點**：若重烤後「待吞之 R1 楔形片」前提不成立 → 停機上呈 KL。 |

- **本波必立三閘**：#1 白縫、#5+#6 鋪滿族、#7+#8 守恆——皆碼閘、皆 ≤0.01/1e-6、皆載依據。
- **暫標待歸因**（#10 `<5㎡`／#11 `0.1`／`UNCOVERED_TOL`）：**不得再以其全綠作為正確性陳述之根據**（N0-17）；§N5/後波歸因。

---

## 8. 驗收（②不變量閘＋③預測差量閘·屬 N0-16 之②③層·非 UI 錨）

**py_compile**：`python -m py_compile app.py verify/stepg_pipeline.py verify/wf_f1.py verify/wf_f4.py verify/run_verification.py`。

**grep 坐實異動**：四病灶 `buffer(0.001)`／`area >= 1.0` 於 stepg/wf_f1/wf_f4/app 病灶點**歸零**；`buffer(0.0011)` 於 wf_f1:242/wf_f4:1146/app:15509 **歸零**；守恆 `<6.0`/`<1.0` → `<0.01`（六 gate 點）；白縫 assert 出現於碼。

**預測差量閘（重烤·③層·逐格）**：

**⚠️ 本表依 KL 2026-07-16 晚裁改寫（S0c 提前·單次重烤）**：重烤只跑一次，故預測差量須**同時含 T2 之漏歸零與 S0c 之捨入位移**。

| # | 閘 | 判準 | S0c 影響 |
|---|---|---|---|
| ① | 業主宗 G **一字不變** | baseline 欄 `G(㎡)` 逐格 byte 相同·絕對閘·一格不符即停 | **不豁免·全程有效**（G＝財務目標值·`app.py:6792`／`6804`·定於 `6821` 實切**之前**）|
| ② | 業主宗幾何面積位移 **≤ 0.005 × 分配深度**（逐宗） | baseline 欄 `幾何面積(㎡)`（`stepg:272`） | **🔴 重錨（CC 補正）**·原 `≤0.01`（前提「cut_coords 未動·應 0」）於 S0c 下**必紅** |
| ③ | 池幾何 **逐街廓總量** `+= 已證 net_leak` | 3.5m R1+0.19/R2+0.17/R3+0.25/R4+0.02/R5+0.22/R6+0.17；0m R1+0.17/R2**+0.69**/R3+0.05/R4+0.12/R5+0.26/R6+0.17（±0.01） | **逐片對映失效**（停機② 坐實片身分/片數改變·N0-19）→ 退**逐街廓總量**（§10-4 之 fallback 已觸發） |
| ④ | 重算後 net_leak == 0 | 池帳−池幾何 ≤0.01（§閘③）全街廓×情境 | 收斂判準（③ 僅回歸預測） |
| ⑤ | T1 新留 <1㎡ 片逐片可歸因 ＋ **池片數差異逐片可歸因** | 原被 `area>=1.0` 丟棄之末筆楔形＋N0-19 s-帶分解所致之片數變動·無不可歸因新增 | S0c 後**間隙側薄帶消失**（如 R1 0m 之 0.0021 帶）→ 片數應較 S0b-only 少 |

**🔴 閘② 重錨之依據（CC 補正·補丁二 §一「重錨範圍縮小為幾何欄（閘③⑤）」漏列閘②·上呈 claude.ai 覆核）**
- **坐實**：閘② 標的欄＝`幾何面積(㎡)`＝`round(_res.get('area_geom',0.0),2)`（`verify/stepg_pipeline.py:272`）；S0c **第 2 項即直接改此欄**。
- **量級**：`|S_conv − round(S_conv,2)| ≤ 0.005` × 分配深度 → R1（32.97）**≈0.16㎡ ≫ 0.01**。
- **性質**：以 0.01（幾何精度上限）管**捨入量子**誤差＝**依據錯配**（N0-17-a），**與補丁二 §三自身為守恆閘所修正者同型**。
- **新閘寬依據**：**2dp 捨入半量子 0.005m × 深度**（＝②-宗 圍堵閘之同類依據·KL 已核可）。一句話測試：改小十倍必紅，因捨入量子即 0.005。
- **不再收緊**：此位移為 S0c 之**恆定內生量**（非收斂項），與 ②-宗 圍堵閘「S0c 後收 1e-6」性質不同（後者係縫/疊消滅）。

**不變量閘（②層·絕對）**：鋪滿（§5.2）／不重疊（1e-6）／守恆（收 0.01 後）／池三則（∈{0}∪[MinA,∞)·本波不新增·沿用）／位次不變（cut_coords 未動·投影序不變）。

**⚠️ N0-16 提醒**：UI↔harness 對拍（乙）**僅證接線④**·**非** T2 正確性；T2 正確性之證明在**②＋③**（重烤），**不在** KL 之 UI 實跑（丙第 2 步之錨定屬④·接線保證）。

**S0a §N5 前置重驗**：本 plan 不做 §N5；但記錄 S0a 窮盡性僅有效至 §N5 前（恆等式須於 §N5 後重驗一次·入 §N7-15 前置·非 S0b 範圍）。

---

## 9. 施工序（S0b＋S0c 併段·**單次重烤**·每段閘綠再前進）

> **⚠️ 全面改寫（KL 2026-07-16 晚裁·補丁二 §二/§五）**：S0c **提前併入**（插於原中斷點 step 4 之前）→ **錨只重定一次**。
> **⚠️ 前 session 之 step 1-3 WIP 在另一台機器、依「不綠不推」未 push、本機無（已 grep 坐實：`_pool_strips_for_block` 全庫命中 0；四病灶原封未動）→ 原「✅已完成」標記作廢，一律須依 plan 重建。**

| # | 段 | 狀態 |
|---|---|---|
| 1 | **helper `_pool_strips_for_block` 立**（§1.5·**斜交切線座標更正版**）＋內建自檢（①' 覆蓋／②-池／**②-宗圍堵**／Σ 式診斷）＋T1 雙路 loud → py_compile | 🔁 **須重建** |
| 2 | **T2-#1 stepg** 接 helper → 應復現：`union(宗+池)−街廓 = 0.0000`、逐宗 slab 差額 0.0000、池側重疊 0 | 🔁 **須重建** |
| 3 | **T2-#2 app** 同構（byte 對映 stepg） | 🔁 **須重建** |
| — | *（原 §9 中斷點：第四源停機 `ee5f844` → 停機② `4168319`）* | — |
| **3.5** | 🆕 **S0c 同源修**（§N3-0c·**提前**）：① `solve_G_binary` 實切改 `round(S_conv, 2)`；② `area_geom` 改取實切面積（**`_final_area` 現為 dead value → 係新接線**；`area_conv` 之 `6793` 收斂／`6807` 未收斂**兩路徑皆改**） | 🆕 **新增** |
| **3.6** | ✅**已完成** **三閘＋圍堵重驗**：①' 覆蓋 **0.0000**／②-池 **0**／②-宗圍堵 **0.0000**（可收 1e-6）／**Σ 診斷之縫與疊已歸 0**（內部縫 0 帶）／T2-MP 0／T1 0 觸發 → **第四源根除·裁定 §二 逐項成立** | ✅ |
| **3.7** | 🆕 **帳對幾何閘兩級化**（補丁三 §二·停機③ 裁定）：**逐宗主閘新立**＋逐街廓 Σ 閘＋全區＋**E3**（補丁三 §三-1）→ 五處落點 | 🆕 **待做** |
| 4 | **T2-#3 wf_f1**＋**補償-1 拆**（§4.1）→ F.1 R1 REPL 綠。**含 `WEDGE_AREA_ANCHOR` 重量測**（§N3-0d·5.30↔0.07 由**實測**給出·不做讀碼考古）。**🔴 預授權停機點**：若「待吞之 R1 楔形片」前提不成立 → **停機上呈 KL**（域裁「R1 整形是否仍需要」） | 待做 |
| 5 | **T2-#4 wf_f4**（`_reshape_block` 回傳 pool_polys）＋**補償-2 拆**（§4.2）→ E3 REPL 綠 | 待做 |
| 6 | **T1** 四處（§2）＋**補償-3**（app:15509·§4.3） | 待做 |
| 7 | **乙 匯出升級**（§6·純 UI·七項） | 待做 |
| 8 | **單次重烤**（f3 起·舊 baseline 依 PRE 凍存）→ **預測差量閘①②③④⑤＋鋪滿／池帳−池幾何／白縫 全綠** | 待做 |
| 9 | **守恆閘收緊**（§5.3）——**S0c 已併入 → 圍堵界即歸零** | 待做 |
| 10 | py_compile → grep 異動清單對照本 plan → **commit + push**（嚴格 `git rev-parse origin/main` 驗） | 待做 |
| 11 | 報告入倉 `docs/reports/W-G.4_S0b_修漏報告.md`·聊天僅 ping | 待做 |

**step 8 之閘（依補丁二改寫·⚠️ 原文「①~⑤」中之 ② 須重錨）**
- **① 業主宗 G 一字不變＝絕對閘·S0c 亦不豁免**（補丁二 §一 勘誤：G＝財務目標值·定於 `6792`／`6804`·在 `6821` 實切**之前**）。
- **② 業主宗幾何面積位移 → 重錨 `≤ 0.005 × 分配深度`**（**CC 補正**·§8 詳述·原 `≤0.01` 於 S0c 下必紅）。
- **③ 池幾何 → 逐街廓總量對映**（**非逐片**·停機② 已坐實池片身分/片數改變·N0-19）。
- **④ net_leak == 0**（收斂判準）。**⑤** T1 新留片＋**池片數差異**逐片可歸因。
- **前置·碼錨重定**：`WEDGE_AREA_ANCHOR`（wf_f1:31/196）中心值隨重烤重定（否則 196 硬檢先破）；`±0.05` tol 標「⚠️ 殘餘定閘·待歸因」（量測 wiggle·§7 +補2）。其餘 baseline 快照 CSV 依 PRE 凍存慣例重烤。

**step 9 之收緊值（§5.3·⚠️ 已二度改寫·現行版＝補丁三 §二）**
- **「6.0/1.0→0.01」已廢**（依據錯配·補丁二 §三）；**「`宗數×0.005`／圍堵界」亦已廢**（維度錯·補丁三 §一·停機③ 實測四閘同破）。
- **現行式**：幾何級＝①' 覆蓋閘（同一條）｜**逐宗主閘 `≤0.005×深度＋tol＋0.005`**｜逐街廓 Σ `≤宗數×(0.005×深度＋tol＋0.005)`｜全區＝逐街廓加總｜E3 `≤整形涉及宗數×(0.005×深度＋0.005)`。
- **⚠️ 順序更正**：因舊閘 `<1.0` 為 **raise 停機③**（`stepg:841`）、E3 `0.1` 亦 raise，**二者於 S0c 後立即擋住管線** → 閘改須提前至 **step 3.7**（不能等到 step 9）。step 9 遂併入 step 3.7。

**丙時序定位**：本 plan＝第 1 步（plan→reviewer→實作→push）。第 2 步（KL pull→UI 實跑錨定）**須待 push 之後**·**現不得請 KL 實跑**（病灶原封未動·grep 15247 可證）。

---

## 10. 設計裁決／WATCH（送 reviewer·非 KL 域裁）

以下為**實作設計**問題（reviewer 域·非意思決定 KL 域）；若 reviewer 認為某項升為域裁，則標旗上呈 KL、停該項施工：

1. **helper 置放**（§1.5）：app.py（harvest·傾向）vs 獨立 verify 模組。
2. **Phase 8 <5㎡ 合併**（§4.3）：拆 buffer＋loud warn＋靠閘③把關（傾向·最小侵入）vs S0b 暫停用該合併（讓 §N5 統一）。
3. **白縫閘 harness 落點**（§5.1）：等同鋪滿閘之推論（傾向）vs 獨立量測點。
4. ~~**piece 身分穩定性**：T2 是否可能改變某街廓池片**數目**（vs 現 baseline）→ 若改變則預測差量閘③（逐片對映）須改逐**街廓總量**對映＋片數差異列可歸因清單（⑤）。REPL 先驗片數。~~
   → **✅ 已實現·已裁·本項結案**（停機② `4168319`）：**確認改變**（R1 0m 池帶 3 片／3.5m 2 片；p1 帶 0.07 取代舊 5.30 連通碎片）。
   **KL 2026-07-16 晚裁 → 新正典 N0-19**：**池片＝相鄰池 s-帶之極大聯集；原子＝s-帶；身分鍵＝s 區間出生即定；連通分量＝舊實作 artifact**。
   → 閘③ **退逐街廓總量對映**（已落 §8）；片數差異併入閘⑤ 可歸因清單；§N4／§N5／N0-6 之「片」全依 N0-19 重述（已落規格）。
5. **s_max 現算 vs 舊 `actual_max_proj`（claude.ai 複驗加驗·對 WARNING B 修法之正確性關鍵）**：二者**構造上恆等**——`actual_max_proj = max((v−corner_pt)·d_hat for v in blk_meta['vertices'])`（stepg:563-569）而 `blk_poly = Polygon(blk_meta['vertices'])`（stepg:214/217）＝同一組頂點、同一投影式。**唯一分岔點**：217 之 `is_valid` 修復路徑 `buffer(0)` 可微改頂點。→ **重烤若在曾走 `buffer(0)` 修復之街廓出現 s_max 微差，屬 helper 更正確（切線與被切體同源）、非回歸。**

**本 plan 無 KL 域裁題**：S0b 之 T1/T2/T3＋補償＋閘＋乙＋甲-2 皆 §N3-0/交辦已明定；D1/D2/D3（前版 plan 之 R5 街角補足/R6 私有宗/Rw 基準）屬 §N1/§N2＝S1/S2·**不在 S0b**。若施工中撞出未涵蓋之真實違規（如某街廓 T2 後鋪滿閘無法達 0.01 之幾何成因），**停機上呈**（§N8）。

---

## 11. 不觸及清單（scope guard）

- **⚠️ 本項依 S0c 併入而改（KL 2026-07-16 晚裁）**：原「**不動** solve_G_binary」**已不成立**——**S0c 明文改 `solve_G_binary`**：
  ① 實切 `app.py:6821` → `round(S_conv, 2)`；② `area_conv` 賦值（`6793`／`6807`）改取實切面積。
  **授權範圍嚴格限此二項**；`solve_G_binary` 之**其餘一字不動**（bisect 迴圈 `6754-6800`、`G_target` 式 `6774-6776`、
  回傳 `6835-6843` 之 `'G'`／`'S'`／`W`／`Rw_pct` 皆不動）。**G 欄/S 欄/推進 baseline 不動＝預測差量閘① 之標的**。
- **不動** `_block_strip` 之切帶邏輯（僅**新增** helper 呼叫 `_block_strip` 切池帶）。
- **不動** §N1 buffer 幾何化（buffer_S 矩形近似→bisect 為 S1·本波 forced buffer 沿用現值）。
- **不動** §N2 街角確立、§N3 F.3 targeting/比例調配、§N5 g_tab 回寫/碎片消解/末筆 G-S 二分。
- **不動** wf_f4 `pool_final[blk]=poolE[blk]` 之守恆總量記帳（保留·§3）。
- **不刪** `_reshape_block`／reshape_rows/reshape_polys/resh_targets 契約（前版 reviewer B4·6 消費端）——§T2-#4 僅**新增** pool_polys 回傳、不動既有契約。
- **不改** 抵費地碎片 `<5㎡`／E3 `0.1`／`UNCOVERED_TOL 0.05` 之**閾值**（僅暫標·§7）。

---

## 12. redistribution-reviewer 獨立審查結論（`100cfa3`·py_compile 五檔全過）

**總判：核可但附 WARNING（施工前修訂）**。無 BLOCKED、無破守恆、無違 CLAUDE.md/§N3-0 鐵律；A(病灶/補償行號)、C(T3)、D(補償拆+WEDGE 錨)、F(乙匯出)、G(甲-2)、H(scope guard)、J(域裁) 皆 reviewer 自 grep/算術坐實 PASS。

**施工前必修（已落入本 plan）**：
1. **WARNING B**（§1.1/§1.5 已改）：`actual_max_proj/end_pt/d_hat_rev` 於 pool-build 點**不在 scope**（閉包內未 return）→ helper 內部自 block_poly 投影現算 s_domain·不倚賴之。
2. **WARNING E**（§5.1 已改）：白縫閘須置於 `try…except Exception:pass`(15920) **之外**·否則被靜默吞成非閘。

**NOTE（已納）**：`UNCOVERED_TOL` 實 5 處（§7 已補 4182/4191）；net_leak③ 以**重烤實測**為準·不採信偵察數字（§10-4·④net_leak==0 才是收斂判準·③僅回歸予測）；白縫閘立閘時序與守恆閘收緊**同步於 T2 重烤綠後**（§9 step 8-9·避免 T2 未竟先破）。

**設計裁決定案（reviewer 域·已採 reviewer 傾向）**：
- helper 置放＝**app.py（`ns` harvest·同 `_block_strip` 先例）**（§1.5）。
- Phase 8 <5㎡＝**最小案：拆 buffer＋loud warn＋靠閘③把關·不停用**（§4.3·reviewer 宜採最小案）。
- 白縫 harness 落點＝**由 T2 helper 鋪滿自檢涵蓋·UI 側 assert 為顯性化**（§5.1）。
- piece 身分穩定性＝重烤 REPL 先驗片數·若變動則③退逐街廓總量對映＋片數差異可歸因(⑤)（§10-4）。

**判斷層邊界（reviewer 明示·透明呈 KL·非阻擋）**：「D1/D2/D3 是否確屬 §N1/§N2 而非 S0b」為跨波架構歸屬·reviewer 與 CC 同盲區、無法獨力定讞；惟 S0b 碼路徑（T2 僅改池幾何產生法·不做街角/targeting/buffer 幾何化）**經 reviewer 坐實未偷做後波**·故當前無需 KL 前置裁示；若施工中撞 §N1/§N2 邊界模糊·§N8 停機上呈機制已備。
