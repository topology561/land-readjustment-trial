# W-G.9-32：∥SIDELINE 落地前之受詞校正現查

**基座**：`wg925-handoff` @ `6e88094`（＝`origin/wip/s1-endpart`·開場時二者同值）
**批號現查**：`W-G.9-32` ⇒ **0 檔·0 報告檔** ⇒ 未占用（判別力自檢：`W-G.9-31` ⇒ **4 檔**）
**性質**：⛔ 零生產碼 · ⛔ 零 baseline 更新（`VR-012`）
**結論**：🔴 **`Q1`／`Q2`／`Q3` 三項預測全部成立** ⇒ **本單之疑慮成立**——設計 `W-G.9-30` 之 §3 與 §5 `P1` **⛔ 非同一界面**。

⚠️ **行號綁 commit**：本報告所載之一切行號，皆成立於 **`6e88094`**（`CLAUDE.md` 行號衛生第 2 款）。

---

## 現查 A：破量之受詞

**母體**：`verify/probes/probe_D2b17_dual.py`

| 標籤 | 產生行 | **決定其枚舉之行** | **所枚舉之容器** |
|---|---|---|---|
| `池{i}×池{j}`（`:9047`） | `:349`／`:376` | `:344-345` `for i in range(len(pieces))` | `pieces` |
| `池{pi}×宗{bi}`（`:9050`） | `:356`／`:383` | `:351-352` `for pi, pg in enumerate(pieces)` ／ `for bi, bg in enumerate(biz)` | `pieces` × `biz` |
| 🔴 `宗{i}×宗{j}`（**`:9062`** ＝ `②-宗 圍堵閘`） | `:363`／`:390` | **`:358-359`** `for i in range(len(biz))` ／ `for j in range(i + 1, len(biz))` | **`biz` × `biz`**·⛔ **不含 `pieces`** |

**`biz` 之溯源**（逐段）：
`:340 def measure_A(pieces, biz)` ← `:618` `aP, aB, aZ, adet = measure_A(pieces, biz)` ← `:614` `pieces, biz = c["pieces"], c["biz"]`
← `:540-542` `pieces, biz = replicate_pieces(ns, block_poly, d_hat, corner_pt, allocation_dir, biz_polys)`
← `:535` spy 攔截 `_pool_strips_for_block` 之第 5 參數 `biz_polys`
← `app.py:20019-20021` 之生產呼叫：`_pool_strips_for_block(blk_poly, d_hat, corner_pt, allocation_dir_block, **allocated_polys**, …)`
🔒 `:406` `_biz = [p for p in (biz_polys or []) if p is not None and not p.is_empty]`（僅濾空·⛔ 不改集合語意）

⇒ **`②-宗 圍堵閘` 所量者 ＝ 業主宗 × 業主宗**（`allocated_polys` 兩兩配對）；`pieces`（池片）**⛔ 不在該式之內**。
⇒ **哪一行決定了它 ＝ `:358-359`**。

---

## 現查 B：改 `_corner_buffer_S` 之回傳能否影響現查 A 所得之受詞

### 式一 `_corner_buffer_S` 內部之切帶呼叫

`app.py:8954`　`_g, _ar = _block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)`
⇒ **⛔ 未傳 `n_hat_far`**。
🔒 其 docstring 逐字自陳（`:8898`）：`⚠️ **D-2b-11【a-1】交叉引用**：\`_block_strip\` 已加雙線形式 \`n_hat_far\`；本函式**未傳**該參數`

### 式二 `_pool_strips_for_block` 內之切帶呼叫

`app.py:9068`　`g, _ = _block_strip(block_poly, d_hat, bp, b - a, allocation_dir=allocation_dir)`
⇒ **⛔ 未傳 `n_hat_far`**。

### 式三 `buf` 之全部消費點（兩路徑 × 兩側·⛔ 正面列舉）

| 路徑 | 行 | 逐字 | **位置／方向** |
|---|---|---|---|
| A | `:19624`／`:19625` | `left_cum_S = float(_left_buffer_S)`／`right_cum_S = …` | **位置**（沿 `s` 之累積起點） |
| A | `:19627`／`:19628` | `_W_prev_left = (_left_buffer_S * _cos_dn) if _has_left_corner else 0.0` | **位置**（W 鏈之種子值） |
| A | `:19656`／`:19669` | `k956_W_from_mp(_gs_l + float(_left_buffer_S) * _du_diag, …)`／`_gs_r - float(_right_buffer_S) * _du_diag,` | **位置**（起點沿 `_du_diag` 平移） |
| A | `:19902`／`:19904` | `'b': _left_buffer_S * _cos_dn`／`'b': _right_buffer_S * _cos_dn` | **位置**（選槽起算值） |
| B | `:611`／`:612` | `left_cum_S = float(_left_buffer_S)`／`right_cum_S = …` | **位置** |
| B | `:829`／`:830` | `_b_L0 = _mp_base_W0(corner_pt, _left_buffer_S, …) if _fo_left else 0.0` | **位置**（其內 `_bp0 = _gs + _buf * _du` ⇒ 平移起點） |

### 🔒 一句結論（⛔ 二選一·不得含混）

> **`buf` 之八個消費點<u>全部</u>改變帶之【起點位置】；⛔ 無一改變帶之【界線方向】。**

---

## 現查 C：近側界方向之表達力

### C-1 `_block_strip` docstring 對「近側方向」之逐字

- `:8419-8420`　`切割帶兩側方向 n_hat = rot90(allocation_dir)。allocation_dir 應為 rot90(f3_cad_alloc_dir)（§0.5-B）…`
- `:8425`　`` `n_hat_far`：**遠側**切邊之方向。`None` ⇒ **沿用近側 `n_hat`** ＝ **現行行為·逐位不變**。 ``
- 🔴 **`:8426`　`近側方向仍**只**由既有 `allocation_dir` 決定 ——⛔ **未新增近側參數**`**
- `:8430`　`造帶，兩條切邊**共用同一個 `n̂`** ⇒ **僅能表達平行四邊形**。`
- `:8434`　`**幾何（雙線分支）**：近側線過 `bp`、方向 `n̂`；遠側線過 `bp + S·d̂`、方向 `n̂_far`。`

### C-2 `n_hat_far` 逐檔命中（⛔ 正面列舉五檔·⛔ 未用「全倉 grep 再排除」）

| 檔 | `n_hat_far` | 判別力自檢 `_block_strip` | 該格是否可採 |
|---|---:|---:|---|
| `app.py` | **13** | **40** | ✅ 可採 |
| `verify/stepg_pipeline.py` | **0** | **1** | ✅ 可採（**對照非 0 ⇒ 證該式非恆 0**） |
| `verify/run_verification.py` | 0 | **0** | ⚠️ **作廢**（`S-2`） |
| `verify/run_all.py` | 0 | **0** | ⚠️ **作廢**（`S-2`） |
| `verify/selection_pipeline.py` | 0 | **0** | ⚠️ **作廢**（`S-2`） |

🩸 **`S-2` 之逐項處置（⛔ 不掩蓋）**：後三檔之**對照組回 0** ⇒ 依 `S-2`「先疑量測器、後疑命題」，
**該三格之量測作廢**、具名為 **⚠️ 無鑑別力**（該三檔根本不提 `_block_strip` ⇒ 其 `n_hat_far` 為 0 屬**必然**、⛔ 非資訊）。
⇒ 本節之結論**僅依** `C-1` 之禁止逐字 ＋ 前兩檔之可採實測，⛔ **未依賴**該三格。

### 🔒 出艙碼（三碼擇一）

> **`不可`**（附禁止之逐字）

**逐字**：`app.py:8426`　`近側方向仍**只**由既有 \`allocation_dir\` 決定 ——⛔ **未新增近側參數**`
⇒ 而 `allocation_dir` 為**整條帶共用**之單一方向（`:8419` `n_hat = rot90(allocation_dir)`）
⇒ **⛔ 無法只令「第 2 宗之近側界」改向**而不動其餘。

⚠️ 本碼 ⛔ **非** `無從判定`——**禁止之逐字已明載於碼面**，⛔ 非「查不到」。

---

## `Q1`〜`Q3` 逐項判

| # | 預測 | 判 | 依據 |
|---|---|---|---|
| **Q1** | 現查 A 之枚舉容器 ＝ 業主宗集合 | ✅ **成立** | `biz` ← `biz_polys` ← `app.py:20021` 之 `allocated_polys` |
| **Q2** | 現查 B 三式之結論 ＝「位置」 | ✅ **成立** | 八個消費點全為位置；且式一／式二**皆未傳 `n_hat_far`** |
| **Q3** | 現查 C 出艙碼 ＝「不可」 | ✅ **成立** | `:8426` 之禁止逐字 |

🔴 **⇒ 本單之疑慮成立**：設計 `W-G.9-30` §3 之改動（於 `_corner_buffer_S` 加 `n_hat_far`）作用於**帶之起點位置**這一界面；
而 §5 之 `P1` 所指之閘（`②-宗 圍堵閘`）量的是**業主宗兩兩重疊**，其形狀由 `_block_strip` 之 `n̂`／`n̂_far` 決定
——而 `_corner_buffer_S` 與 `_pool_strips_for_block` **兩處皆未傳 `n_hat_far`**。
⇒ **§3 之改動⛔ 不會使 `P1` 成立** ⇒ 設計 §3／§5 **須重定**。

---

## 停機條件之逐條判

| 碼 | 判 | 依據 |
|---|---|---|
| **S-1**（生產檔 diff） | ⛔ 未觸發 | 本批 `git diff` 僅及 `docs/`；`app.py`／`verify/` 零觸 |
| **S-2**（對照組回 0） | 🛑 **觸發 3 格·已處置** | 現查 C-2 後三檔 ⇒ 該三格量測**作廢**、⛔ 未用於結論 |
| **S-3**（需動被量之物） | ⛔ 未觸發 | 三項現查全為**靜態讀取**，⛔ 未跑任何探針、⛔ 未改任何被量之檔 |

---

## 入倉四項

| # | 落點 | 前 → 後 | 驗 |
|---|---|---|---|
| ① | 本報告（新建） | — | — |
| ② | `docs/驗證裁定登記表.md` ＋ **`VR-013`** | 261 → **275** | 定義式 ⇒ **1**；編號現查：`VR-013` 全倉 **0 檔**·定義式 **0**（最大為 `VR-012`） |
| ③ | `docs/reports/W-G.4_泛用阻塞項登記表.md` ＋ **`GB-64`** | `^\| ` 117 → **118** | `^\| \*\*GB-64\*\*` ⇒ **1**；刪除行 **0** |
| ④ | `docs/design/W-G.9-30_∥SIDELINE界線之接線設計.md` **檔末就地加註** | 218 → **238** | 加註命中 ⇒ **1**；刪除行 **0** ⇒ **⛔ 原句一字未刪** |

🔒 **`GB-64` 之編號現查（考古 82·逐筆看落點）**：字樣全倉 **1 檔命中**，落點為
`docs/reports/W-G.9-29_R2破量歸因與授權入倉.md` 之一句**現查記錄**（「`GB-63`／`GB-64` 皆 0 命中」）
⇒ **⛔ 非占用**；實體判準 `^\| \*\*GB-64\*\*` ⇒ **0** ⇒ **未占用**、⛔ 未改號。

---

## ⛔ 本批未涵蓋之事

1. ⛔ **未重定設計 §3／§5**——本批只現查並具名，重定屬另案（`VR-013` 已載其後果）。
2. ⛔ **未提出「新增近側參數」或「另闢構造」之方案**——`GB-64` 已標「🛑 需 KL 域裁」。
3. ⛔ **未跑任何探針、未跑 `run_all`**——三項現查全為靜態；⇒ **⛔ 未實測**「若真傳了 `n_hat_far` 會如何」。
4. ⛔ **未查** `_block_strip` 之**雙線分支本身**是否正確（其唯一生產呼叫端 `app.py:9720` 之行為未驗）。
5. ⛔ **未動** `verify/baselines/`、⛔ 未動任何凍存物與名單、⛔ 未動 `app.py`／`verify/` 下任何檔。
6. ⛔ **後三檔之 `n_hat_far` 命中數不作為證據**（`S-2` 作廢·已具名）。
7. ⛔ **未推翻** `K-9-5-4` 釋示補之授權、⛔ 未推翻 `W-G.9-29` 之楔形歸因——二者之受詞與本批不同。
