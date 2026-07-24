# W-G.4 裁定 M — 施工 plan v1

> 基準／BEFORE 錨＝**`df9834c`**。canonical＝`W-G.4_KL域裁M_原位次小往大_街角winner更正.md`
> （含 Q1/Q2/Q3 裁決）。盤點＝`docs/reports/W-G.4_裁定M_盤點表.md`。
> 依 CLAUDE.md：plan 一寫完**立即送 reviewer**、不停等 KL。

## 〇、規模與風險（先講·誠實）

本 plan **同時含兩類改動**，耦合但性質不同：

| 類 | 內容 | 風險 |
|---|---|---|
| **口徑修正**（Q1） | 街角 G-gate 由粗估 → **真 G** | **高**：動全部街角 winner 判定 ⇒ 錨大量連動；且 `run_corner_pk` 需新輸入（B/C/尺度/price），**6 個呼叫端**同改 |
| **機制新增**（M-1/2(c)/3） | 合併自救＋小往大部分拆分 | 中：全新路徑、無既有可回歸 |

**耦合點**：M-2(c) 自救後「合併後是否 ≥ 街角規定面積」之判定**用的就是真 G** ⇒ 兩者不可拆序
（先做 (c) 而 G 仍粗估 ⇒ 自救門檻用錯口徑；先做 Q1 而無 (c) ⇒ 純動錨無收益）。
⇒ **同單元、但分步 commit**（P-A…P-F），每步 `py_compile` ＋ 關鍵 grep。

---

## 一、P-A：`_corner_first_lot_G`（真 G·單一真相源）

**新增** app.py module 級函式，入 `_WF_NS_NAMES`：

```python
def _corner_first_lot_G(*, a_m2, A_ratio, B, C, l_front, l_side, F,
                        block_poly, d_hat, corner_pt, s_max_blk, side,
                        allocation_dir, side_mid, avg_depth, _label=''):
    """M-2 Q1：**假設第 1 宗**之真 G。與實配第 1 宗**同一條 solve 路徑**。"""
```

- **內部一律呼叫 `solve_G_binary`**（**禁另寫平行式**·Q1 鐵律）。
- 「假設第 1 宗」之參數語意（與實配首宗逐項對映）：
  | 參數 | 值 | 依據 |
  |---|---|---|
  | `baseline_pt` | 左＝`corner_pt`；右＝`corner_pt + s_max_blk·d̂` | 實配首宗 `left_cum_S` 初值＝`_left_buffer_S`＝**forced band**；而「假設有地主宗入選」⇒ **無 forced** ⇒ `buf=0` |
  | `d_hat` | 左＝`+d̂`；右＝`−d̂` | 同 stepg 左右組 |
  | `is_corner` | `True` | 第 1 宗街角地 |
  | `W_prev` | `0.0` | 首宗 |
  | `S_max_limit` | `s_max_blk`（`_oblique_s_max`·退 `S_block_max`） | 首宗可用全幅 |
- **失敗＝loud raise**（禁回 None／禁 fallback·Q1 鐵律）。
- **stepg／app 兩路徑共用同一函式**（#20 四處同改之單一真相源）。

⚠️ **不動 `solve_G_binary` 本身**（凍結·僅新增呼叫端）。

## 二、P-B：`run_corner_pk` 輸入補（純加性·6 呼叫端）

真 G 需 `B`／`C`／`l_front`／`l_side`／`F`／`A`——**全源自 snapshot**
（`B_value`:stepg:153、`C_for_calc`:106、`sb 尺度`:130-131、price:財務接線_v3），
現行 `run_corner_pk(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels, setback)` **無 snapshot**。

**改**：增 `snapshot`（keyword-only、**無預設**⇒漏傳即 TypeError·非靜默）。

**抽出** `_finance_ctx_for_pk(ns, snapshot, cb)` → `{B, C, sb_rows_by_label, pre_price, post_price}`，
**與 `run_step_g` 之算式同源**（B/C 之推導**移為共用 helper 或逐字對映＋同值斷言**——
見 §六 reviewer 待決 R1）。

**6 呼叫端同改**：`run_verification:423`／`wd3_fragment_geom:93`／`wd4_tier_list:187`／
`wg_g1_smoke:56`／`wg_g2_smoke:35`／`wg_g3:81`。

## 三、P-C：G 來源換真 G＋**消滅 or-鏈**（Q1 鐵律）

- `selection_pipeline.run_corner_pk`：`_G_est = estG(...)` → `_G_true = ns["_corner_first_lot_G"](...)`。
- `_candidates` 之 `'G_value'`／`'G_estimated'` → **單一鍵 `'G_true'`**。
- `_pk_one_side_v12`（app:8474-8477）現行：
  ```python
  cand_G = (g_values_map.get(...) or cand.get('G_value') or cand.get('G_estimated', 0))
  ```
  → **改為單一來源＋缺即 raise**：
  ```python
  if 暫編 not in g_values_map: raise RuntimeError("🔴 M-2/Q1：取不到真 G …禁 fallback")
  ```
  （`or`-鏈之 falsy 陷阱亦一併消滅——`G=0.0` 現行會被 `or` 跳過。）
- **`_estimate_G_for_qualification` 之處置**：其**唯一消費端**為 PK；換源後成孤兒 →
  依 `expand-contract` **contract 段整段刪**（先 grep 證零殘留）。
  ⚠️ 若他處仍消費 → 保留並註明（reviewer 查核項 R2）。

## 四、P-D：M-2(c) 合併自救（**主體**）

於 `_pk_one_side_v12` **第一關淘汰前**插入自救：

```
for cand in group:
    G_true = g_values_map[暫編]                    # P-C 後單一來源
    if G_true >= min_area_to_apply: → qualified
    else:
        缺口 = min_area_to_apply − G_true
        救援池 = 同歸戶於【其他可建築街廓】之【未達該塊 MinA】地   ← M-2 原文
        if 救援池 可補足 缺口(依 Q3 只取所需):
            cand['_m2_rescue'] = {...}             # 帳面量·**不改真交集幾何**（Q2）
            → qualified（合併後 ≥ 規定面積）
        else: → eliminated（照舊）
```

**Q2 硬約束**：`E-1.7 空間濾網（真交集 > 1.0㎡）`**照舊先行**——
自救**僅解 G 門檻**，**不得**成為無跨占者之候選後門。**測項**：構造「真交集 0.5㎡ ＋ 合併後 G 充足」
之 synthetic，斷言**仍 eliminated**。

## 五、P-E：M-1 ＋ M-3 三段（跨街廓小往大·部分拆分）

**落點＝`wf_f2._decide`**（跨街廓決策·現 `if not qual: return None` 即棄→F.4）。

```
新增分支：qual 為空（＝M-1 要件「多街廓均未達」）
  → 小往大部分拆分（目標＝保住原位次分配處數最大化）
     M-3(i)① 補足量：併入以補足【目標塊 MinA】為度（Q3「只取所需」）
     M-3(i)② 餘額他併：餘額先依 M-1 往同歸戶其他較大地
     M-3(i)③ 餘額回流街角：餘額合併後任一街廓仍未達 MinA ⇒ 併入同歸戶街角地
     量不足救全部 → 取【保住處數最大之子集】；同處數 tie-break＝優先救較大者（Q3-tb 補注）
  → 部分拆分不可行 → 整筆連同乙′併入最大之丙（M-1 退路）
```

**M-3(ii) 補注**（遠地同時可救街角與 M-1 → 街角優先）：以**優先序旗標**實作·可單點關閉（KL 否決即改）。

**泛用四約束**：處數/缺口/子集選擇一律由 `mina[blk]`／`gid`／`G` 現算驅動——
**禁塊名（R1…）／側別字面／案例常數**。

## 六、P-F：M-4 交互驗證（**不得被 Q1 錨連動排擠**）

| 驗證項 | 基準（本波前一單元實測） | 判準 |
|---|---|---|
| 末端保留觸發集 | 3.5m **唯 R6 左端**·未臨正街 **85.706㎡**·末端帶 `s∈[0, 3.5114]` | M-1/M-2 後**不得無故消失或位移**；若變動須歸因於 winner 更正之合法連動並載明 |
| `_end_gate` `_cond1` 上游 | `forced[blk]['{side}_has_side']` | M-2 改 `forced_offset` 而**非** `has_side` ⇒ `_cond1` 應**不變**·斷言之 |
| E3 `_reshape_block` fallback | 全案 latent（未觸發） | 落地後仍 latent，或觸發須誠實報 |
| `fixture_end_reserve.py` | 10 斷言 Δ=0 | **必須續綠** |

## 七、驗收

1. `py_compile` ＋ **ns 雙向閘**（新增 `_corner_first_lot_G` 須入 `_WF_NS_NAMES`）。
2. **全閘重跑·BEFORE 釘 `df9834c`**；FAIL 集合**不得新增名目**
   （`W-F F.4` 之死因若遷移 → 誠實定位既有/新引入）。
3. **首要讀數**：重跑 `probe_capacity_decomp` 家族 → 3.5m
   **「合併後仍需調配群數 vs 可容上界」**·**「9 戶差 2 戶」是否消失**。
   附帶：三端「⚠️強制抵費地」是否轉為地主宗（＝forced 鎖定 918.50㎡ 是否釋回）。
4. **錨連動獨立節**（spec §五.3）：`F1_REVERIFY`／UC9898 R1左3.5m winner／
   `第 1 宗街角地指配結果_退縮*.csv`／街角三指數 golden — **逐項載前後值**。
   ⚠️ **golden 圖 8（0.6685/0.3315）為手冊語意錨·若變動＝實作 bug、非合法重定錨**。
5. V2/V3/V8/V9 維持**未驗·待波末重烤**。

## 八、⛔ reviewer 待決／潛在停機

| # | 題 | 性質 |
|---|---|---|
| **R1** | B/C 於 PK 與 `run_step_g` **兩處計算**——抽共用 helper（動 stepg·風險）vs 逐字對映＋同值斷言（`expand` 段做法）？ | 技術·reviewer 定 |
| **R2** | `_estimate_G_for_qualification` 是否真為孤兒（grep 全倉消費端） | 技術 |
| **R3** | 真 G 需 `a`＝`分攤登記面積+面積_m2`（實配口徑）；PK 現用 `幾何面積_m2` ⇒ **口徑二次分岔**·須一併對齊 | 技術·**易漏** |
| **R4** | M-2 自救之「其他可建築街廓未達地」與 M-1 之救援池**重疊** ⇒ 同一宗可能被雙重消費 ⇒ 須單一結算帳（M-3(ii) 街角優先即此序） | 技術·**守恆風險** |
| **R5** | 若 reviewer 認定 Q2 空間濾網須放寬方可行 → **停機上呈**（spec §五.5） | 域 |
