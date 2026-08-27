# 🔧 `W-G.9-147R`　`GB-105` 前置：`_projection_order` 呼叫點之**完整盤點與母體具名**

**基座** ＝ `e9ad89806d632144c5b3a9756ed22f0218283fcf`　**`app.py` blob** ＝ `b4cc30835feaad03dfc37f394a669bbb45988b8b`
**性質**：🔒 **只讀**·⛔ **零生產碼**·⛔ 未改任何既有檔一字·純新增三檔
**量測時點**：`2026-08-27`·情境 `0m`／`WV_K6_STEP0=on`·**harness 態**（⛔ 非 app live 態）

> 🔴 **一句話結論**：`GB-105` 所載之「**`4` 處**」**嚴重不足**——生產鏈實為 **`12` 處**（漏掉**整個 `wf_f0`〜`f4` 引擎**共 `7` 處 ＋ `selection_pipeline.py` `1` 處）。且四類母體**受詞互異**，⛔ **不可能**以單一「暫編地號集合逐位相同」之不變式串起全部呼叫點。

---

## §零　`V-0`　取號現查（三事齊·常規四-五／-六）

| 形（框逐字） | 命中 |
|---|---|
| `^###.*W-G\.9-147` | **`0`** |
| `` `W-G.9-147` ``（反引號式） | **`0`** |
| `W-G_9-147`（檔名式·內容） | **`0`** |
| 檔名含 `147`（`git ls-tree -r --name-only HEAD`） | **`0`** |
| 裸 `W-G\.9-147` | **`0`** |
| **對照組** `W-G\.9-145` | **`6` 檔**（⇒ 量測器非紅） |

⇒ 🔒 **`W-G.9-147` 實體命中 ＝ `0`** ⇒ 取號安全（**`P-1` 符**）。

### 🩸 `V-0` 之一項不符：**對照組 `W-G.9-146` 實得 `0`**

單 `§零` 稱「建議 `W-G.9-146`，**其於摘錄檔入倉後必 `≥1`**」。
🔒 **現查**：`grep -rn "W-G\.9-146" .` ⇒ **`0`**（全倉）。
⇒ 🔴 **`W-G.9-146-PRE` 正典摘錄檔⛔ 不在倉內**（`docs/reports` 之 `W-G.9-NNN` 現行 max ＝ **`145`**）。
🔒 **⛔ 不影響取號**：`146` 依**常規四-二**（單號一經發出即占用）已占用，`147` 仍為下一個未占用號。
⇒ 已改以 `W-G.9-145`（`6` 檔）為對照組，量測器非紅。

---

## §一　`V-1`　七形盤點（母體 ＝ `app.py` ＋ `verify/**/*.py`·`204` 個 `.py`·⛔ 不含 `docs/`／log）

🔒 本 clone **無** `.claude/worktrees/`（`ls` ⇒ `No such file or directory`）⇒ ⛔ 無 `GB-35` 之巢狀污染。

| 形 | 框（逐字） | 命中 |
|---|---|---|
| `a` | `_projection_order` | **`61`** |
| `b` | `_projection_order(` | **`8`** |
| `c` | `ns\["_projection_order"\]` | **`14`** |
| `c′` | `ns\['_projection_order'\]` | **`1`**（`probe_WG996_yi_invariants.py:391`·**字串內**·⛔ 非呼叫） |
| `d` | `\["_projection_order"\]`（**⛔ 不假定容器為 `ns`**） | **`16`**（＝ `c` 之 `14` ＋ **`2`**） |
| `d′` | `\['_projection_order'\]` | **`1`**（同 `c′`） |
| `e` | `getattr\(.*_projection_order` | **`0`**（對照組 `getattr\(` ＝ **`56`** ⇒ 量測器非紅） |
| `e′` | `globals\(\)\[` | **`1`**（`stepg_pipeline.py:269`·受詞為 `_V3_FINANCE`·**與本符號無關**） |
| `e″` | `locals\(\)\[` | **`0`**（對照組同 `e`） |
| `f` | `= *_projection_order *$` ／ `= *_projection_order *[,)]` | **`0`**／**`0`** |
| `g` | `def _projection_order` | **`4`**（**對照組·必 `≥1`** ⇒ 量測器非紅；其中**真定義僅 `1`** ＝ `app.py:7593`，餘 `3` 係探針內之字串） |

### 🔴 形 `d` 較形 `c` 多出之 `2` 處（＝**單所預見之「容器名非 `ns`」**）

- `verify/probes/probe_WG916_isolate.py:72`：`out = orig["_projection_order"](parcels, p1, p2)`
- `verify/probes/probe_WG999_yi_chain.py:292`：`SOP2, PO = ns2["_spatial_order_parcels_v2"], ns2["_projection_order"]`

### 🔴 形 `f` 之判：**嚴格式 `0`，惟別名確實存在**（經 `ns[...]` 路徑）

嚴格式（`= _projection_order` 之裸綁定）命中 **`0`** ⇒ **`P-3` 字面符**。
🔒 **惟推廣式現查**：別名 **`PO`** 由 `PO = ns["_projection_order"]` 綁定於 `4` 支探針，其後以 `PO(...)` 呼叫；別名 **`orig`** 為 dict、以 `orig["_projection_order"](...)` 呼叫。
⇒ 🔒 **形 `f` 之「`0`」⛔ 不等於「無別名」**——本符號之別名走的是**形 `c`／`d` 之路徑**，已被涵蓋。
🔴 **另有一處<u>覆寫</u>**（⛔ 非別名）：`probe_WG916_isolate.py:87` `ns["_projection_order"] = w_proj` ⇒ **生產符號被探針就地換掉**。

### 🔴 去重後之呼叫點清單

#### （甲）**生產鏈**（`app.py` ＋ `verify/` 非 `probes`）＝ **`12` 處**

| # | `檔:行` | 該行逐字（截） | 第一實參 |
|---|---|---|---|
| `1` | `app.py:7731` | `pre_seq = _projection_order(parcels_in_block, front_line_p1, front_line_p2)` | `parcels_in_block` |
| `2` | `app.py:11396` | `_ordered = _projection_order(_mem, _p1, _p2)` | `_mem` |
| `3` | `app.py:18913` | `_projection_order(_all_in_blk, _fl_p1_lstep, _fl_p2_lstep))` | `_all_in_blk` |
| `4` | `verify/selection_pipeline.py:339` | `ns["_projection_order"](_all_in_blk, _fl_p1_lstep, _fl_p2_lstep)` | `_all_in_blk` |
| `5` | `verify/stepg_pipeline.py:499` | `ns["_projection_order"](_stage1_parcels, _cad_fl_blk.get('p1'), …)` | `_stage1_parcels` |
| `6` | `verify/wf_f0.py:256` | `return [tp["暫編地號"] for tp in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]` | `pib` |
| `7` | `verify/wf_f1.py:376` | `return [tp["暫編地號"] for tp in ns["_projection_order"](pseudo, fl["p1"], fl["p2"])]` | `pseudo` |
| `8` | `verify/wf_f2.py:95` | `return [x["暫編地號"] for x in ns["_projection_order"](pib, …)]` | `pib` |
| `9` | `verify/wf_f3.py:78` | `return [x["暫編地號"] for x in ns["_projection_order"](pib, …)]` | `pib` |
| `10` | `verify/wf_f4.py:1043` | `return [x["暫編地號"] for x in ns["_projection_order"](pib, …)]` | `pib` |
| `11` | `verify/wf_f4.py:1433` | `return [t["暫編地號"] for t in ns["_projection_order"](pseudo, …)]` | `pseudo` |
| `12` | `verify/wf_f4.py:1503` | `return [t["暫編地號"] for t in ns["_projection_order"](pseudo, …)]` | `pseudo` |

🔒 **`wf_f0`〜`f4` 屬<u>生產</u>、⛔ 非測試**——依 `CLAUDE.md §7` 逐字「**單一真相源＝`verify/wf_f0~f4`（此即「引擎」之定義）**；app 接線＝……**禁 fork**」。
⇒ 🔴 **`GB-105` 之「`4` 處」漏列 `8` 處**（`wf_*` `7` ＋ `selection_pipeline` `1`）。

#### （乙）**探針**（`verify/probes/`·診斷·⛔ 非生產）

`probe_WG916_isolate.py:72`（＋ `:87` **覆寫**）／`probe_WG996_yi_invariants.py:407`／`:408`／`:453`／`probe_WG998_gate_paths.py:108`／`:181`／`:182`／`:258`／`:327`／`:362`／`probe_WG998b_control_dprime.py:101`　⇒ **`12` 處**（另 `probe_WG999_yi_chain.py:292` 為綁定）。

---

## §二　`V-2`　逐呼叫點之**母體具名**（🔴 本單核心）

| # | `檔:行` | ② 第一實參 | ③ 賦值處（逐字） | ④ 母體之受詞 | ⑤ 回傳去向 |
|---|---|---|---|---|---|
| `1` | `app.py:7731` | `parcels_in_block` | **函式參數**（`_spatial_order_parcels_v2` `def@7689`）；呼叫端 `app.py:20037` 逐字 `parcels_in_block=_stage1_parcels,   # P2-a：僅階段1宗`；另一呼叫端 `verify/stepg_pipeline.py:479` | **該街廓之階段 1 宗**（⛔ 排除已配地階段之宗） | `pre_seq` → `pre_seq_meta[*]['pre_position']` |
| `2` | `app.py:11396` | `_mem` | `app.py:11382` 逐字 `_mem = [_pk[_j] for _j in _g]` | 🔴 **單一合併群之成員**（`n = 2`〜`3`）·⛔ **非街廓全體** | `_ordered[0]` → 合併宗**命名**（`+`）與 `_rep_i` |
| `3` | `app.py:18913` | `_all_in_blk` | `app.py:18897` 逐字 `_all_in_blk = by_blk.get(_lbl, [])`；`by_blk` 建於 `:18851-18853`（`for r in _g_rows: by_blk.setdefault(r['所屬街廓'], []).append(r)`） | **該街廓之 `_g_rows` 全體**（Step-G 產出列·**含 ghost**） | `_rank_by_tpid` → PK tiebreaker |
| `4` | `verify/selection_pipeline.py:339` | `_all_in_blk` | `:333` 逐字 `_all_in_blk = by_blk.get(_lbl, [])`；`by_blk` 建於 `:306-308`（同式） | 同 `3`（**`3` 之 harness 鏡射**·碼註逐字「鏡射 app tiebreaker 換源」） | 同 `3` |
| `5` | `verify/stepg_pipeline.py:499` | `_stage1_parcels` | `:416` 逐字 `_stage1_parcels = [tp for tp in parcels_in_blk if '配地階段' not in tp]` | **該街廓之階段 1 宗** | `_proj_rank` → **結構閘** `_pos_bad` |
| `6` | `verify/wf_f0.py:256` | `pib` | `:254-255` 逐字 `pib = [tp for tp in parcels if tp["所屬街廓"] == blk and not tp.get("_is_ghost_sliver")]` | 🔴 **該街廓·⛔ 排除 ghost**（判準與 `5` **不同**） | `_proj_order` 回傳暫編地號序 |
| `8`／`9`／`10` | `wf_f2.py:95`／`wf_f3.py:78`／`wf_f4.py:1043` | `pib` | 三處**逐字相同**：`pib = [{"暫編地號": tp["暫編地號"], "polygon_coords": tp.get("polygon_coords")} for tp in parcels if tp["所屬街廓"] == blk and not tp.get("_is_ghost_sliver")]` | 同 `6`，惟**僅投影出二鍵** | 同 `6` |
| `7`／`11`／`12` | `wf_f1.py:376`／`wf_f4.py:1433`／`wf_f4.py:1503` | `pseudo` | 皆為 `pseudo = [{"暫編地號": k, "polygon_coords": list(v.exterior.coords)} for k, v in <polys>.items()]` | 🔴 **reshape 前／後之多邊形字典**（`polys_by_id`／`fb_polys`／`new_polys`）·⛔ **非街廓宗地清單** | 「**位次序不變**」之**成對**對拍（`oB` vs `oN`／`_oE` vs `_oN`／`oE` vs `oN`） |

### 🔒 ⇒ 母體**至少四類·受詞互異**

| 類 | 呼叫點 | 受詞 |
|---|---|---|
| **甲**（階段 1 宗） | `1`／`5` | `'配地階段' not in tp` |
| **乙**（排除 ghost·僅二鍵） | `6`／`8`／`9`／`10` | `not _is_ghost_sliver` |
| **丙**（合併群成員） | `2` | 單一群之 `n = 2`〜`3` |
| **丁**（reshape 多邊形字典·成對） | `7`／`11`／`12` | 前／後兩態 |
| **戊**（`_g_rows` 全體·含 ghost） | `3`／`4` | `by_blk[_lbl]` |

---

## §三　`V-3`　執行期母體實測（探針 `verify/probes/probe_WG9147_projorder.py`）

🔒 **量測器自檢**（⛔ 二皆綠方採信）：
① `ns is _projection_order.__globals__` ＝ **`True`** ⇒ 覆寫 `ns[...]` **亦攔得到 `app.py` 內部之直接呼叫**（⇒ `1`／`2`／`3` 皆可觀測）。
② 人造呼叫後 REC 增量 ＝ **`1`**（須 `1`）。
🔒 `rc = 0`／`stderr` ＝ **`0` B**。log ＝ `verify/out/probe_WG9147_projorder_e9ad898.log`。

### `V-3-a`　觀測到之呼叫點

| 呼叫點 | 次數 |
|---|---|
| `app.py:11396` | `8` |
| `app.py:7731` | `2` |
| `verify/selection_pipeline.py:339` | `6` |
| `verify/stepg_pipeline.py:499` | `2` |

🛑 **未被觀測者（⛔ 非「不存在」）**：
- `app.py:18913` —— 落在 **`main()` 內**（`def main` `@13444..22609`）⇒ 依 `CLAUDE.md` 逐字「**`main()` 內之敘述從不被 `run_all` 執行**」。
- `wf_f0`〜`f4` 之 `7` 處 —— 管線於 **`R2` 中止**（逐字：`街廓 R2 抵費地計算失敗：🔴 ②-宗 圍堵閘破[R2]：宗-宗重疊 = 45.9766 > 上界 2.8906`）⇒ 未進 `wf_*` 階段。

### `V-3-b`　🔴 **逐街廓**對拍（⭐ 可分辨「真母體差」與「覆蓋差」）

| 街廓 | 對拍 | 判 | 對稱差 |
|---|---|---|---|
| **`R1`** | `:339` vs `:7731` | 🔴 **集合相異** | 只在 `:339`：**`['_GHOST_(R1)']`**；只在 `:7731`：`[]` |
| `R1` | `:339` vs `:499` | 🔴 **集合相異** | 同上 |
| `R1` | `:7731` vs `:499` | ✅ **逐位相同** | — |
| **`R2`** | `:339` vs `:7731` vs `:499` **三者** | ✅ **逐位相同**（`n=14`） | — |
| `R2` | `:11396`(`n=2`) vs 其餘 | 🔴 **集合相異** | 只在 `:11396`：`['628-40(1)','628-43(1)']` |
| `R3` | `:11396`(`n=2,3,2`) vs `:339`(`n=10`) | 🔴 **集合相異** | 只在 `:11396`：`['628-30(3)','628-45(2)']` |
| `R4` | 僅 `:339`(`n=3`·含 `_GHOST_(R4)`) | — | 其餘未達 |
| `R5` | `:11396`(`n=3,3`) vs `:339`(`n=8`) | 🔴 **集合相異** | 只在 `:11396`：`['628-21(2)','628-22(2)','628-23(2)']` |
| `R6` | `:11396`(`n=2,3`) vs `:339`(`n=8`) | 🔴 **集合相異** | 只在 `:11396`：`['628(2)','628-1(2)']` |

🔒 **三項決定性讀法**：
1. **`R1` 之唯一差 ＝ `_GHOST_(R1)`** ⇒ 係**真母體差**（⛔ 非管線中止所致之覆蓋差）——坐實 `甲` 類（階段 1 宗）與 `戊` 類（`_g_rows` 全體）**對 ghost 之處置不同**。
2. **`R2` 三者逐位相同**（該街廓**無 ghost**）⇒ 🔴 **「同不同」<u>隨街廓而異</u>** ⇒ ⛔ **不得寫成一條全域「逐位相同」之不變式**。
3. **`:11396` 於 `R2`／`R3`／`R5`／`R6` 皆集合相異**，其母體恆為 `n = 2`〜`3` 之**群成員** ⇒ 與其餘呼叫點**結構上不可能同集合**。

---

## §四　`V-4`　結構閘之現況（只讀·⛔ 不改）

🔒 **現行行段（`grep -n "結構閘" verify/stepg_pipeline.py` 現查·⛔ 不沿用 `:491-509`／`:493-508`）**：
「位次＝投影序」閘之標頭在 **`verify/stepg_pipeline.py:491`**，判定式 `:497-504`，`raise` 於 **`:506-508`**。
（同檔另有 `結構閘 ⊥`@`:439`／`telescoping`@`:1224`／`階段2 telescoping`@`:1259`／`â 定向`@`:1312`／`理論＝實跑`@`:1334` 等五族·⛔ 非本單受詞。）

**`raise` 逐字**：
```
            if _pos_bad:
                raise RuntimeError(
                    f"🔴 結構閘 位次＝投影序 破：街廓 {blk_label} {len(_pos_bad)} 筆 pre_position "
                    f"≠ _projection_order 排名（暫編, pre_position, 投影排名）={_pos_bad[:3]}")
```

**本次執行之 `_pos_bad`**：該 `raise` 之字樣於本次 log 命中 **`0`** ⇒ `R1`／`R2` 二次呼叫**皆綠**（`_pos_bad` ＝ 空）。
🛑 **射程限縮**：`R3`〜`R6` **未達**（管線於 `R2` 之**另一閘**中止）⇒ 🔒 **本項只證 `R1`／`R2`，⛔ 不證全區**。

---

## §五　`V-5`　`GB-105` 三數之現況覆核（⛔ 只報·不改）

| 受詞 | 現行行號 | 逐字 |
|---|---|---|
| `GB-105` 節題 | `docs/reports/W-G.4_泛用阻塞項登記表.md:2764` | `### \`GB-105\` 🆕` |
| `GB-105` 表列 | 同檔 `:2770` | 其「現況處置」欄逐字見下 |
| `K-9-17 三【更正】一` | `docs/rulings/K-6_街角地分配程序與可分配判準.md:3020` | 見下（對照組 `二呼叫點` ＝ **`4`** 命中 ⇒ 量測器非紅） |

**`GB-105:2770`「現況處置」欄逐字**：
> 🔒 **⛔ 本批只登記·⛔ 零生產碼**。**落地批須先**：① 現查呼叫點之**完整清單**（`grep` 須含 `ns\["_projection_order"\]` 之形）② 以**暫編地號集合逐位相同**之直接不變式串起**全部**呼叫點 ③ ⛔ **不得以「閘沒紅」作為母體同步之證據**（`K-9-17 三【更正】三`：不同步係轉紅之**必要非充分**條件）。**失效條件** ＝ 該不變式落地且四點皆納入

**`K-6:3020` 逐字**：
> **一**　`pre_position` 由 `app.py:7656-7658` 之 `_projection_order(parcels_in_block, p1, p2)` 產生；閘之 `_proj_rank` 由 `verify/stepg_pipeline.py:498-500` 之 `_projection_order(_stage1_parcels, p1, p2)` 產生；二呼叫點於 `:480` 共用同一清單（倉內註解 `:414-415` 已逐字載此耦合）。

⚠️ **該段所載之三組行號皆已失準**（`app.py:7656-7658` 現為 `:7731`；`stepg:498-500` 現為 `:499`；`:480` 現為 `:479`）——⛔ **本批不改**（`docs/` 零變更），僅具名。

---

## §六　`§三` 七項預測之逐項對拍（⛔ 未改預測）

| # | 預測 | 實得 | 判 |
|---|---|---|---|
| `P-1` | `W-G.9-147` 實體命中 ＝ `0` | `0`（五形皆 `0`·對照組 `6` 檔） | ✅ **符** |
| `P-2` | 去重後呼叫點 ＝ **`4`** | 🔴 **生產鏈 `12` 處**（另探針 `12` 處） | ❌ **不符** |
| `P-3` | 形 `f`（別名再綁定）＝ `0` | 嚴格式 `0`；**惟別名 `PO`／`orig` 確實存在**（走形 `c`／`d`） | ⚠️ **字面符·實質須修正** |
| `P-4` | 形 `e`（反射式）＝ `0` | `0`（`getattr` `0`／`locals()[` `0`；`globals()[` `1` 與本符號無關） | ✅ **符** |
| `P-5` | `app.py:11396` 之母體與其餘相異 | ✅ 相異，且成因**更根本**：`_mem` ＝ **單一合併群成員**（`n=2~3`）·⛔ **非「帶 `+` 之街廓清單」** | ✅ **符（成因不同）** |
| `P-6` | 其餘三處（`:7731`／`:18913`／`:499`）母體**逐位相同** | `:7731` vs `:499` ✅ **逐位相同**；`:18913` **未觀測**（在 `main()` 內），其 harness 鏡射 `:339` 於 **`R1` 因 `_GHOST_(R1)` 相異**、於 `R2` 相同 | ❌ **不符** |
| `P-7` | 結構閘 `_pos_bad` ＝ `0`（全綠） | `R1`／`R2` 皆綠；`R3`〜`R6` **未達** | ⚠️ **符但射程限縮** |

### 🔴 對【乙】之直接後果（⛔ 由發單側落筆·CC 不自選）

`P-5` **成立** ⇒ 依單 `§三` 逐字：「`GB-105` 逐字之『以暫編地號集合逐位相同之直接不變式串起全部四處』**其受詞須修正**（四處並非同一母體，不變式須**分組**）」。
🔒 **本單另加二項【乙】須併納之事實**（⛔ 超出原預測之外）：
1. **母體須分 `5` 組**（甲／乙／丙／丁／戊·見 `§二`），⛔ 非「四處分組」。
2. 🔴 **`甲` 與 `戊` 之差係 `ghost`、且<u>逐街廓而異</u>**（`R1` 相異／`R2` 相同）⇒ 不變式若寫「集合相同」將在 `R1` 立即紅、在 `R2` 假綠 ⇒ **須先裁「ghost 是否入投影序母體」**（併看 `K-9-19` 無地主之未覆蓋殘餘⛔ 非「宗」）。

---

## §七　⚠️ 附帶現查（⛔ 非 `V-1`〜`V-5` 之受詞·⛔ 本批未修）

🔒 **`run_all.py:73` 之「禁寫死絕對路徑閘」現行有 `4` 命中**（以其逐字樣式於本 clone 複刻·⛔ 未跑 `run_all` 本體）：

| `檔:行` | 逐字（截） | 判 |
|---|---|---|
| `verify/tools/wg960_z_selfcheck.py:12` | `ROOT = r"C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\wg953-handoff-ready-d…` | 🔴 **真違例**（他機必壞·＝該閘之立閘案由本身） |
| `verify/probes/probe_WG971_wrap.py:203` | `TPL = ('  File "C:\\Users\\admin\\…'` | 🟡 樣板字串 |
| `verify/tools/nameset_diff.py:19` | docstring 內之說明文字 | 🟡 說明 |

🔒 **⛔ 非本批所致**（本批新增之 `probe_WG9147_projorder.py` 對該樣式命中 **`0`**·已自證）。⛔ 本批只讀、未修。

---

## §八　收工閘

| # | 實得 |
|---|---|
| `1` | `HEAD` ＝ `e9ad89806d632144c5b3a9756ed22f0218283fcf`；`app.py` blob ＝ **`b4cc30835feaad03dfc37f394a669bbb45988b8b`**（⛔ 零觸·**絕對值出艙**） |
| `2` | `git status --porcelain` 於跑畢僅二 `??` 新檔 ⇒ **⛔ 無任何既有檔被改寫**；刪除欄逐列 `0` |
| `3` | `V-0`〜`V-5` 逐項有數、逐項附框與逐字（見上） |
| `4` | `§三` 七項預測逐項標明 符／不符（`§六`） |
| `5` | 凡「命中 `0`」之斷言皆同格附框／命中數／對照組 |
| `6` | 態之量測時點 ＝ `2026-08-27`·情境 `0m`／`STEP0=on`·**harness 態** |

**本批新增三檔**（⛔ 未改任何既有檔）：
`docs/reports/W-G.9-147R_projection_order呼叫點盤點.md`／`verify/probes/probe_WG9147_projorder.py`／`verify/out/probe_WG9147_projorder_e9ad898.log`

🛑 **回報即停**——【乙】之不變式定式**由發單側落筆**，⛔ CC 不自選（單 `§三` 末逐字）。
