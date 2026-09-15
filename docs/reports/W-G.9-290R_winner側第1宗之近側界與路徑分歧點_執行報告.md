# `W-G.9-290R`　執行報告（**現查·零生產碼**）：winner 側之第 1 宗如何取得其**近側界** ／ 二態之路徑分歧點

> **單** ＝ `docs/orders/W-G.9-290_施工單_winner側第1宗之近側界與路徑分歧點.md`（工項零已原封入倉）
> **基座** ＝ `39ab6e3252a735940918f2a1c284f2dac34e67c6`（`ls-remote` 實查·全 `40` 碼）
> **分級** ＝ **中**（純現查與量測·**零生產碼**·⛔ 改碼一字·⛔ 替身·⛔ 反事實·**⛔ 鑄任何號**）
> 🛑 **出艙即止**：本報告**⛔ 判** `forced` 側應否走同一路、**⛔ 擬**任何實作形、**⛔ 判**孰誤、
> **⛔ 解除／收窄** `GB-170`、**⛔ 提**修法主張、**⛔ 呈** KL。

---

## `§零`　開工閘（九項·逐項當場重跑·⛔ 採單所載之數·**同格載其產生指令**）

| # | 受詞（**產生指令逐字**） | 實測 | 判 |
|---|---|---|---|
| `1` | `git ls-remote origin refs/heads/wip/s1-endpart` | `39ab6e3252a735940918f2a1c284f2dac34e67c6`（全 `40` 碼） | ✅ |
| `2` | `git rev-parse HEAD:app.py` | `4379108a4856714078c410ff4e6291ecfdf6d2c1` | ✅ |
| `3` | `git merge-base --is-ancestor 05a11bd665f6c2790ff821c9e3a1606651e345d4 HEAD`（🆕 **新附款 `(c)`**：`rc` **緊接該指令**·⛔ 經管線） | `rc = 1` ⇒ **非祖先**；判別力[必為祖先] ＝ `c76525ec` ⇒ `rc = 0` | ✅ |
| `4` | `python verify/probes/probe_order_preflight.py <本單>` | `SELF_SHA256` 實算 ＝ 單載 ＝ `3f8ea148da416230c10d12f2d8e75639e38ca7deaa4baa4041230ecb8e2e1f44`（`P-5` 受詞 `13692` B）；判別力二造（**先自證 bytes 相異**）：造甲 全檔 `13770` B（`Δ +78`）`0d88b18a…`／造乙 去末尾 `\n` `13691` B（`Δ −1`）`a408b019…` ⇒ **皆相異** | ✅ |
| `4'` | 受詞自證（坑 `bf`·受詞 ＝ **所量之檔名**） | 檔名 ＝ `W-G.9-290_施工單_winner側第1宗之近側界與路徑分歧點.md`；[必真] 含 `W-G.9-290` ＝ `True`／[必偽] 含 `W-G.9-289` ＝ `False`（併報本文命中 `4`／`12`） | ✅ |
| `5` | 同 `4` ＋ `--selftest` | `rc = 0`（🔴 停機款 `0`／🟡 提示 `0`）·`P-3` `def main` ＝ `14975`-`24579`；`--selftest` `rc = 0` | ✅ |
| `5'` | `python verify/tools/wg9223_acceptance_audit.py --selftest` | `rc = 0` | ✅ |
| `6` | `python verify/probes/probe_WG9267_issuer_measurers.py registry` | 自誤 `383`／`393`｜`GB` `168`／`170`｜`VR` `80`／`95`｜`K-9` `28`／`29` | ✅ |
| `6'` | `python verify/probes/probe_WG9269_pit_index.py` | **`87`／`87`**·🔴 命中 `0`·末標籤 `bi` ⇒ **下一標籤 `bj`**；造甲 坑 `n` 定義處 `6` ≥ `1`／造乙 人造坑 `0`／`0` ⇒ **器非紅**（母體 ＝ `HEAD` 之追蹤 `.md` **`778`** 檔·落檔 `verify/out/WG9290R_pitindex_pre.log`·`stderr` `0` B） | ✅ |
| `7` | `git ls-files \| grep -E '^verify/[^/]+\.py$'` ＋ `app.py` | `33` ＋ `1` ＝ **正面列舉 `34` 檔**；判別力[必不命中] ＝ pathspec `verify/*.py` 多咬之子層檔數 ＝ **`304`**（判準「須 `> 0`」·⛔ 定值） | ✅ |
| `8` | `git ls-tree -r HEAD verify/baselines \| sha256sum`（`core.quotePath` **預設**·⛔ `ls-files`） | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·檔數 **`298`** | ✅ |

### `§零-2`　號占用之預查

**三軸**：`(1)` `blob@39ab6e3252a735940918f2a1c284f2dac34e67c6`／`(2)` 全 `docs/` **`756`** 檔（讀不到 `0`）／
`(3)` **檔框 ＋ 列框**（宣告框·`D3` 嚴格式·`列框 = |D2 ∪ D3|`）。

| 號 | `D1` 檔 | `D2` 列 | `D3` 列 | **列框** | **檔框** | 鬆框 | 角色 |
|---|---|---|---|---|---|---|---|
| **`W-G.9-290`** | `0` | `0` | `0` | **`0`** | **`0`** | `0`／`0` | 受詢 ⇒ **未占用·可用** ✅ |
| `W-G.9-289` | `2` | `2` | `2` | `4` | `2` | `25` 列／`2` 檔 | 對照組 甲[必占用] ✅ |
| （執行期組出之人造號·字面⛔ 出艙·`GB-147`） | `0` | `0` | `0` | `0` | `0` | `0` | 對照組 乙[必為零] ✅ |

---

## `§一`　工項零：本單原封入倉

| 受詞（**產生指令**） | 實測 |
|---|---|
| 所指之檔數（`git -c core.quotePath=false ls-files -z -- docs/orders/` ＋ 錨定框施於**檔名**） | **`1`**（母體 ＝ 追蹤之 `docs/orders/` **`156`** 檔）；造甲 `W-G.9-289` ＝ `1` 檔（須 ≥ `1`）✅／造乙 執行期組出之人造名 ＝ `0` 檔 ✅ |
| 行尾（`git cat-file blob <sha1> \| tr -cd '\r' \| wc -c`·**⛔ `od`**） | `CR` ＝ **`0`** ✅／`LF` ＝ `157`／bytes ＝ `13770`；判別力[必非零] ＝ `verify/out/KL_UI_3.5m_2e08a41_stdout.log` 之 blob `CR` ＝ **`2987`** |
| 三方逐位相同 | blob `sha1` ＝ `f994a20cd865d52c4791e625117d4d0c7f071efb`；**blob 內容 `sha256` ＝ 磁碟 ＝ 源** ＝ `0d88b18a47e5698414225e57beacdc4caf7c688f3190040f5ad96a23a4ee077a`（`13770` B ＝ `13770` B） |
| `numstat` | `157	0`（**`deletions` ＝ `0`**） |

---

## `§二`　工項一（**主檢·現查**）

🔒 **器** ＝ `verify/probes/probe_WG9290_neardir.py`（底本 ＝ `probe_WG9287_landeffect.py` 之 `drive`·⛔ 另寫第二份驅動）·
`rc = 0`·`stderr` **`0`** B·全量落檔 `verify/out/WG9290R_neardir.log`。
🔒 **通道** ＝ harness（`stepg_pipeline.run_step_g`）·**態甲**（`WV_K6_STEP0` 未設）·`SB ∈ {0.0, 3.5}`·`run_step_g` 之終局 ＝ **（未拋）**。
🔒 **包裹點**（自碼面現查·⛔ 推定）＝ `ns["_solve_G_one"]`——`_alloc_dir_used` 係於該函式內設於其回傳上
（`app.py:14014`／`:14029`），而 `solve_G_binary` 之回傳**尚無**該欄。

### `§二-0`　四重自我驗證閘

| 閘 | 受詞 | `0m` | `3.5m` | 判 |
|---|---|---|---|---|
| `(i)` | `_build_corner_range_v3` 之閉式回代 `\|S1_par·sinθ − S1_perp\|` ≤ `1e-9` | 逐格 **`0.0`** | 逐格 **`0.0`** | ✅ |
| `(ii)` | `is_corner=True` 之筆，其 `_alloc_dir_used` 須**逐位等於**同格 `_first_corner_alloc_dir` 之回傳 | **`13`／`13`**·不符 `0` | **`11`／`11`**·不符 `0` | ✅ |
| `(iii)` | **鏈側之歸屬**：每筆須恰屬 `left_group`／`right_group` 之一、總數 ＝ 該段筆數 | **`97`／`97`**·皆非 `0` | **`97`／`97`**·皆非 `0` | ✅ |
| `(iv)` | 🔑 **線向之槽**：`rot90(_alloc_dir_used)` 須與該宗 `cut_coords` 之**實邊** `\|cos\| ≥ 1 − 1e-6` | **`8`／`8`** 逐筆 `\|cos\|` ＝ `1.0`（二情境合計） | | ✅ |

### `§二-1`　款 `1`：`is_second_after_corner` 之賦值鏈

**母體（正面列舉）** ＝ `app.py` ＋ `verify/` 全部 `.py`（**含子層**）＝ **`338`** 檔；框無 `^` 錨 ⇒ **檔 `3` ／ 列 `13`**；
對照組[必為零]（執行期組出·字面⛔ 出艙）＝ **`0`**。

| 角色 | `檔:行` | **函式** | 逐字 |
|---|---|---|---|
| **定義處** | `app.py:12435` | `_lot_gate`（參數·預設 `False`） | `is_second_after_corner=False, chain_side='', _label=''):` |
| **消費處①** | `app.py:12528` | `_lot_gate` | `if is_second_after_corner and bool((_ctx.get('has_side') or {}).get(_side)):` ⇒ **藍影閘（`_k923_gate1`）之守衛** |
| **消費處②** | `app.py:12610` | `_lot_gate` | `else ('第2宗' if is_second_after_corner else '其後')),` |
| **實參①②** | `app.py:22176`／`:22313` | `main` | `is_second_after_corner=(_lg_idx_left == 1),`／`(_lg_idx_right == 1),` |
| **實參③④** | `verify/stepg_pipeline.py:836`／`:955` | `_run_step_g_impl` | 同上逐字 |
| （餘 `4` 列） | `app.py:12479`／`verify/probes/probe_WG9287_landeffect.py` ×`5` | — | docstring 與**探針**（⛔ 生產碼） |

### `§二-2`　款 `4`：二態之逐宗分項表（⛔ 只報合取）

🩸 **本批自捕 `1`**（見 `§五`）：鏈側之歸屬**⛔ 得取** `_solve_G_one` 之 `side` 參數
（`verify/stepg_pipeline.py:804` `side = entry.get('side', '無')`·其為**街角側別**）；
本表之鏈側係以 `left_group`／`right_group` 之**成員** `is` 比對所得（閘 `(iii)` 證其無漏無重）。

| 格 | idx | 暫編地號 | `forced` | `marker` | **`is_corner`** | `is_chain_head` | `near_dir`（入·**槽**） | `_alloc_dir_used`（出·**槽**） |
|---|---|---|---|---|---|---|---|---|
| `R2/left@0m` | `0` | `628-41(1)` | **`False`** | `True` | **`True`** | `True` | `None` | `(-0.6721303204856223, -0.7404328681817782)` |
| `R2/left@0m` | `1` | `628-42(1)` | `False` | `False` | `False` | `False` | `(-0.6721303204856223, -0.7404328681817782)` | `(0.7260188428756796, 0.6876748067142342)` |
| `R2/left@3.5m` | `0` | `628-42(1)` | **`True`** | **`False`** | **`False`** | `True` | `None` | `(0.7260188428756796, 0.6876748067142342)` |
| `R2/left@3.5m` | `1` | `628-41(1)` | `True` | `False` | `False` | `False` | `(0.7260188428756796, 0.6876748067142342)` | `(0.7260188428756796, 0.6876748067142342)` |
| `R4/left@0m` | `0` | `628(1)+` | **`True`** | **`True`** | **`True`** | `True` | `None` | `(-0.7517327519688664, 0.6594678685253096)` |
| `R4/left@3.5m` | `0` | `628(1)+` | **`True`** | **`True`** | **`True`** | `True` | `None` | 同上 |

🔑 **⇒ `forced` 與 `is_corner` ⛔ 一一對應**：`R4/left` **既 `forced` 又 `is_corner=True`**；
`R2/left@3.5m` **`forced` 而 `is_corner=False`**。**決定「遠側界是否 ∥SIDELINE」者 ＝ `is_first_corner_marker`**（⛔ `forced`）。

**🔑 二態自同一入口起之<u>第一個取值相異之分支</u>（逐字）**——其**有二處**，逐處具名：

| # | 分支之逐字 | `檔:行`（函式） | 其條件之**各分項真值** |
|---|---|---|---|
| `甲` | `if _fo_left:` ⇒ `_left_buffer_S = _corner_buffer_S(…)`；否則留 `_left_buffer_S = 0.0`（`:650`）⇒ `left_cum_S = float(_left_buffer_S)`（`:776`） | `verify/stepg_pipeline.py:657`（`_run_step_g_impl`） | `R2/left@0m` `_fo_left` ＝ **`False`** ⇒ `cum_S`（入）＝ **`0.0`**；`R4/left@0m` ＝ **`True`** ⇒ `cum_S`（入）＝ **`4.49975224003872`**（＝ `buf`）；`R4/left@3.5m` ⇒ **`7.8185635189090075`**；`R2/left@3.5m` ⇒ **`8.696079893776137`** |
| `乙` | `if is_corner: allocation_dir = _first_corner_alloc_dir(side_mid)` | `app.py:13990`（`_solve_G_one`；`def` 於 `:13929`） | 其條件 ← `is_first_corner_l = bool(entry.get('is_first_corner_marker', False)) and not first_corner_used_left`（`verify/stepg_pipeline.py:805`–`:808`）⇒ `R2/left@0m` idx `0` `marker` ＝ **`True`**／`R2/left@3.5m` idx `0` ＝ **`False`**／`R4/left` idx `0` ＝ **`True`** |

### `§二-3`　款 `2`：winner 側之第 1 宗之**近側界**係取自何物

🩸 **本批自捕 `3`**（見 `§五`）：`near_dir`／`allocation_dir` 係 **`allocation_dir` 槽**之向量，
其**線向 ＝ `rot90(·)`**（碼面逐字：`_block_strip` 之「切割帶兩側方向 `n_hat = rot90(allocation_dir)`」；
`_first_corner_alloc_dir` docstring：「其切帶之 `allocation_dir` 改為 `rot90_cw(SIDE 方向)`
（`_block_strip` 之 `n_hat = rot90(allocation_dir)` ⇒ **界線 ∥SIDELINE**）」）。本節之線向**皆已取 `rot90`**，
並由閘 `(iv)` 以該宗 `cut_coords` 之**實邊**逐筆坐實（`|cos|` ＝ `1.0`）。

**🔑 賦值鏈（逐字·逐處具名）**

```
verify/stepg_pipeline.py:791   _near_dir_left = None                      ← 鏈頭恆 None
verify/stepg_pipeline.py:828   _near_dir=_near_dir_left,                  ← 傳入 _solve_one
verify/stepg_pipeline.py:513   def _solve_one(…, _near_dir=None, …):
verify/stepg_pipeline.py:522       near_dir=_near_dir,   ← 薄殼直通·⛔ 推導
app.py:13969                   def _solve_G_one(…, near_dir=None, …):
app.py:13990                       if is_corner: allocation_dir = _first_corner_alloc_dir(side_mid)
app.py:13996                       _alloc_dir_used = (None if allocation_dir is None
                                                      else tuple(float(_c) for _c in allocation_dir))
app.py:14012                       near_dir=near_dir,    ← 傳入 solve_G_binary
app.py:14014 / :14029              _r['_alloc_dir_used'] = _alloc_dir_used
verify/stepg_pipeline.py:855   _near_dir_left = res.get('_alloc_dir_used')   ← **前一宗**之值交遞
```

**⇒ 該物 ＝ 前一宗（街角第 0 宗）之 `_alloc_dir_used`；其產生者 ＝ `app.py:13990` 之換值
（`_first_corner_alloc_dir(side_mid)`·`def` 於 `app.py:13929`·回 `rot90_cw(SIDE 方向)`·
🔒 「以 `side_mid` 幾何反查 SIDE_LINE——⛔ 不靠任何字串標籤」）。**

**逐格之對拍**（`corner_range_polys[side]` 之遠側境界線：錨 `_Tp`／線向 `su`）

| 格 | 受檢之宗 | 近側界之**線向** ＝ `rot90(near_dir)` | 遠側境界線之線向 | **`\|cos\|`** | `\|cos\| − 1` | 垂距（近側界之錨 → 遠側境界線） |
|---|---|---|---|---|---|---|
| 🔑 **`R2/left@0m`**（**真 winner**·`forced`＝`False`） | idx `1` `628-42(1)` | `(0.7404328681817783, -0.6721303204856224)` | `(0.7404328681817783, -0.6721303204856224)` | **`1.0000000000000002`** | **`2.220446049250313e-16`**（＝ 一個 ULP） | `3.904440490887934` |
| 🔴 `R2/left@3.5m`（單稱「winner」·實測 `forced`＝**`True`**） | idx `1` `628-41(1)` | `(-0.6876748067142342, 0.7260188428756796)` | `(0.7404328681817783, -0.6721303204856224)` | **`0.9971563070524017`** | `-0.002843692947598342` | `1.802240394085697` |
| 🔴 同上 | idx `2` `628-27(1)` | 同上 | 同上 | **`0.9971563070524017`** | 同上 | `5.884534149251879` |
| `R4/left@0m`（`forced`） | idx `0`（**唯一之宗**） | `near_dir` ＝ **`None`** ⇒ 單線路徑 ⇒ **近側界 ∥ALLOCLINE** | — | — | — | — |
| `R4/left@3.5m`（`forced`） | idx `0`（**唯一之宗**） | 同上 | — | — | — | — |

🔒 **⇒ 該機制（近側界 ∥SIDELINE）<u>存在且運作</u>——其於<u>真 winner 格</u> `R2/left@0m` 逐位成立**
（`|cos| − 1` ＝ 一個 ULP）。
🔴 **⇒ 單 `§三-1` 所舉之格 `R2/left@3.5m` 實為 `forced` 態**，其 idx `0` 之 `marker` ＝ `False`
⇒ **⛔ 有該交遞** ⇒ 其 idx `1` 之近側界 `|cos|` ＝ `0.9972`（**⛔ ∥**）。
🛑 **⇒ 單 `§三-1` 之<u>結論</u>（「該機制存在且運作」）成立，而其<u>所舉之例</u>經實測為誤。⛔ 判孰誤。**

### `§二-4`　款 `3`：`cum_S`／`W_0` 之當場值與其產生式逐字

| 格 | idx | `cum_S`（入） | `W_prev` | `W_near`（回傳·＝ `W_0`） | `G` | `S` | 解法 | **起算是否亦走 s-帶** |
|---|---|---|---|---|---|---|---|---|
| `R2/left@0m`（**真 winner**） | `0` | **`0.0`** | `0.0` | **`0.0`** | `175.95` | `4.06` | 幾何二分法 | 🔑 **否**——`_fo_left` ＝ `False` ⇒ `_left_buffer_S` 留初值 `0.0`（`stepg:650`） |
| `R2/left@0m` | `1` | `7.448704378836619` | `4.06` | `5.74` | `0.23` | `0.18` | 幾何二分法 | — |
| `R2/left@3.5m` | `0` | **`8.696079893776137`** | `0.0` | `6.98` | `4.77` | `0.11` | 幾何二分法 | 🔑 **是**——＝ `buf`（`_corner_buffer_S` 之 bisect 反解） |
| `R2/left@3.5m` | `1` | `8.802342306944828` | `7.09` | `7.09` | `183.23` | `4.08` | 幾何二分法 | — |
| `R4/left@0m` | `0` | **`4.49975224003872`** | `0.0` | **`4.48`** | `2017.54` | `60.92` | 幾何二分法 | 🔑 **是**——＝ `buf` |
| `R4/left@3.5m` | `0` | **`7.8185635189090075`** | `0.0` | **`7.79`** | `2023.33` | `61.1` | 幾何二分法 | 🔑 **是**——＝ `buf` |

**產生式逐字**（`verify/stepg_pipeline.py`）：

```
:650   _left_buffer_S = 0.0
:657   if _fo_left:
:659       _left_buffer_S = _corner_buffer_S(
:660           blk_poly, d_hat, corner_pt, allocation_dir_block,
:661           float(_l_min), 'left', _label=blk_label)
:776   left_cum_S = float(_left_buffer_S)
:819   baseline_pt = (corner_pt + left_cum_S * d_hat …)      ← 🔑 **起算點**
```

### `§二-5`　款 `5`：街角地本身（第 0 宗）之**遠側界**於二態之產生者（🛑 **⛔ 判二者應否同一**）

| 態 | 物 | **產生式逐字** | 其**線向** |
|---|---|---|---|
| **真 winner**（`R2/left@0m`） | 鏈之第 0 宗 `628-41(1)` | `app.py:13990` `if is_corner: allocation_dir = _first_corner_alloc_dir(side_mid)` ⇒ `app.py:14000` `solve_G_binary(…)` 以其 `G` 二分解出 `S`／`cut_coords` | `rot90(_alloc_dir_used)` ＝ **∥SIDELINE**（閘 `(iv)` `\|cos\|` ＝ `1.0`） |
| **`forced`**（`R4/left`·二情境） | 鏈之第 0 宗 `628(1)+` | **同上逐字**（其 `is_corner` 亦 ＝ `True`） | **同為 ∥SIDELINE** |
| **`forced`**（`R4/left`·二情境） | **強制抵費地片**（其 `推進側別` 欄 ＝ `'抵費地'`·`W-G.9-287` 已量得其幾何面積逐位 ＝ `range_area`） | `app.py:9332` `_corner_buffer_S(…)` 之 **bisect 反解**（「解 `buf` 使**真實池帶面積 ＝ `range_area`**」·`\|Δ\| ≤ tol`）⇒ `_block_strip(block_poly, d_hat, bp, w, allocation_dir=allocation_dir)` | `rot90(allocation_dir)` ＝ **∥ALLOCLINE** |

🔒 **⇒ 二態之「鏈之第 0 宗」之遠側界產生式<u>逐字相同</u>**；相異者為 **`forced` 態多一個在其之前的物**
（強制抵費地片），且該片之遠側界（＝ `buf` 線）**同時**是鏈之第 0 宗之**起算點**。

### `§二-6`　款 `6`：`corner_range_polys` 之鋪設處與消費處

**母體（正面列舉）** ＝ 生產碼 **`34`** 檔；框無 `^` 錨 ⇒ **檔 `2` ／ 列 `15`**；對照組[必為零] ＝ `0`。

| 角色 | `檔:行` | **函式** | 逐字（節略） |
|---|---|---|---|
| **鋪設** | `verify/stepg_pipeline.py:413` | `_run_step_g_impl` | `ctx = {'corner_range_polys': {}, 'corner_range_errors': {}}` |
| **鋪設** | `verify/stepg_pipeline.py:429` | `_run_step_g_impl` | `ctx['corner_range_polys'][(_crp_lbl, _crp_wh)] = ns['_build_corner_range_v3'](` |
| 診斷 | `verify/stepg_pipeline.py:449`／`:452` | `_run_step_g_impl` | 診斷字串之組成 |
| **消費** | `verify/stepg_pipeline.py:696` | `_run_step_g_impl` | `_lg_crp_sg = {_w_sg: ctx['corner_range_polys'].get((blk_label, _w_sg))` |
| **消費** | `verify/stepg_pipeline.py:705` | `_run_step_g_impl` | `'corner_range_polys': _lg_crp_sg,`（入 `_lg_blk_ctx`） |
| 回傳 | `verify/stepg_pipeline.py:1642` | `_run_step_g_impl` | `'corner_range_polys': ctx['corner_range_polys'],` |
| **消費（唯一之判定用）** | `app.py:12529` | `_lot_gate` | `_cp = (_ctx.get('corner_range_polys') or {}).get(_side)` |
| docstring | `app.py:12483` | `_lot_gate` | 鍵之說明 |
| （app 路徑·`main`） | `app.py:13166`／`:21959`／`:21981`／`:23219`／`:23324` | `select_corner_lots_both_sides_v12`／`main` ×`4` | `session_state` 之 `f3_corner_range_polys` 與 UI 文案 |

**🔑 其於 `forced` 側是否被消費**（`W-G.9-287` 已量得·本批⛔ 重量）：
`app.py:12529` 之消費**受 `is_second_after_corner ∧ has_side[_side]` 守衛** ⇒
`R4/left`（`forced`·**僅 `1` 宗**·無 idx `1`）**⛔ 被消費**（`_k923_gate1` `0` 次）；
`R2/left@3.5m`（`forced`·有 idx `1`）**被消費**（`_k923_gate1` `2` 次·`ok=True`）。
🔒 **⇒ `corner_range_polys` 之生產消費端唯一者為 `_lot_gate` 之藍影閘（`app.py:12529`·觀測模式）**；
`:1642` 為回傳、`:449`／`:452` 為診斷 ⇒ **⛔ 參與配地幾何**。

---

## `§三`　工項二：一則末端追加

| 受詞 | 實測 |
|---|---|
| 落點 | `docs/reports/W-G.4_泛用阻塞項登記表.md` **檔末**（⛔ 鑄號·⛔ 改任何原節一字） |
| payload | 單之列 `97`–`106`（**`10`** 列／**`1085`** B／`sha256` `af3e13962e71fc00911983cc69c5dd21c80ed110c1c6ff233d9d0f1505822a55`·由檔案管線直接抽出·`常規七 一`） |
| **落地形之判準**（`自誤 393` 逐字） | payload 內含 `#` 標題列 ＝ **`False`** ⇒ **原樣保留 `> `**（⛔ 剝層） |
| **落地形之機驗**（⛔ 鑄號之證） | 本節之題**⛔ 可**被 `GB` 之標題錨定框 `^#{2,4} \`?GB-N\`?` 命中 ⇒ **`False`**（期 `False`）；對照組[必命中] ＝ 倉內既有之 `### \`GB-169\` 🆕　…` 形 ⇒ **`True`** |
| 期初／期末 bytes | `889380` → `890962`（**`+1582`**／**刪除 `0`**）·追加段 `CR` ＝ `0`／`LF` ＝ `19` |
| 嚴格前綴之二造 | 造甲[必真] **`True`**／造乙[必偽] `(old + b'X').startswith(new)` ＝ **`False`** |
| 簡繁機檢 | 受詞 ＝ 本批**自撰**之題與前言（⛔ 含單之 payload）⇒ 簡體命中 `{}`·**`rc` ＝ `0`**；[必命中]對照 `GB-170` ＝ `1` |
| `常規七 三` 覆核 | 重抽 == 首抽 ⇒ **`True`**；簿內含該 payload ⇒ **`True`** |
| `wg942_append_audit.py` | `rc = 0` |
| **四簿（落地後）** | 自誤 `383`／`393`·`GB` `168`／`170`·`VR` `80`／`95`·`K-9` `28`／`29` ⇒ **逐位未動**（**坐實⛔ 鑄號**） |

---

## `§四`　判別力二造之判（`§三` 款 `7`）

| 造 | 受詞 | 實測 | 判 |
|---|---|---|---|
| `(1)` [必命中] | `is_second_after_corner` 為真之筆（＝ 碼側 idx `1`）≥ `1` | **`59`** | ✅ |
| `(2)` [必為零] | 一**執行期組出**之人造名（字面⛔ 出艙·`GB-147`·**已先驗其於現母體命中為 `0`**） | **`0`** | ✅ |

---

## `§五`　本批之自捕（**`3` 則**·皆於出艙前攔下·⛔ 頂替）

| # | 形 | 徵候 | 攔法 |
|---|---|---|---|
| `1` | **鏈側之重建取錯欄** ＝ 我以 `_solve_G_one` 之 `side` 參數推鏈側，而該參數實為該宗之**街角側別**（`verify/stepg_pipeline.py:804` `side = entry.get('side', '無')`）；`'無'` 落入 `else` 分支 ⇒ **一切非街角宗被誤標為 `right`** | 🔴 **⛔ 報錯**，且表面完全合理（每格皆有 `left`／`right`、數目亦像）——係以 `W-G.9-287`【倉】之 `628-41(1)`（實為 `R2/left` 之宗）對拍方顯其偽 | 改以**鏈之群**判定（`left_group`／`right_group` 之成員 `is` 比對·`:796`／`:897`；`_lot_gate` 於 `:843`／`:961` 傳字面 `'left'`／`'right'`）＋ **新增閘 `(iii)`**（`97`／`97` 無漏無重） |
| `2` | **單所舉之格與其標籤不符** ＝ 單 `§三-1` 稱 `R2/left@3.5m` 為「winner 側」，當場重量得其 `forced` ＝ **`True`** | 若逕依單所舉之格量之，得 `\|cos\|` ＝ `0.9972`（⛔ ∥）⇒ **會把「機制不存在」寫成結論** | 依 `常規二` **取保守項**：**併量**單所指之格**與**一格**真正之 winner**（`R2/left@0m`·`forced`＝`False`），**二者並報**·⛔ 擇一·**⛔ 改單一字** |
| `3` | 🔴 **線向取錯槽** ＝ `near_dir`／`allocation_dir` 係 **`allocation_dir` 槽**之向量，其**線向 ＝ `rot90(·)`**（碼面逐字 `n_hat = rot90(allocation_dir)`）；我逕以槽向量為線向 ⇒ `\|cos\|` 讀成 **`0.0`**（⊥）而真值為 **`1.0`**（∥） | 🔴 該誤**朝「⛔ 平行」之方向**失準 ⇒ **會把「機制存在」誤讀為「不存在」** | 改取 `rot90`；**新增閘 `(iv)`**：`rot90(_alloc_dir_used)` 須與該宗 `cut_coords` 之**實邊** `\|cos\| ≥ 1 − 1e-6`（實測 `8`／`8` 皆 `1.0`） |

### `§五-1`　🛑 **併呈（照實·⛔ 判孰誤·⛔ 追改任何既有文件）**

自捕 `3` 之受詞及於**前批之既出數**。以【倉】`verify/out/WG9287R_landeffect.log` 之多邊形**逐點**機驗
（`R4/left@0.0m`·⛔ 重算·直引落檔）：

| 量 | 值 |
|---|---|
| 遠側境界線之**實邊**方向（甲`[2]`→甲`[3]`） | `(-0.6594678685224185, -0.7517327519714024)` |
| `W-G.9-286`／`-287` 所報之 `su` | `(-0.6594678685253096, -0.7517327519688664)` ⇒ **與實邊 `\|cos\|` ＝ `1.0`** ✅（`su` **確為線向**） |
| `buf` 帶之**實切邊**方向（乙`[4]`→乙`[5]`） | `(-0.6943193337697838, -0.7196670499289818)` |
| `rot90(allocation_dir)` | `(0.694319333763684, 0.7196670499348666)` ⇒ **與實切邊 `\|cos\|` ＝ `1.0`** ✅ |
| 🔑 **二線之真 `\|cos\|`**（實邊 vs 實切邊） | **`0.9988785830613192`**（⇒ 夾角 ≈ `2.71°`） |
| `W-G.9-286`／`-287` 所出艙之 `\|cos\|` | **`0.04734528804692001`** ＝ **`su · allocation_dir`**（**二個不同槽**之向量之內積） |

🔒 **其<u>結論方向仍成立</u>**（`0.99888 ≠ 1` ⇒ 二線⛔ 為同一條、⛔ 平行）；
受影響者為**該數之語意**——`0.0473` 讀來似「近乎垂直」，而真值為「**夾角 `2.71°`**」。
🛑 本報告**⛔ 判孰誤**、**⛔ 追改**任何既有文件一字；其處置**候發單側**。

---

## `§六`　一句話推導

> winner 側之第 1 宗（碼側 idx `1`）之**近側界**係**由鏈交遞取得**——`near_dir` ← **前一宗**（街角第 0 宗）之
> `res['_alloc_dir_used']`（`stepg:855`），而後者因 `is_corner=True` 而由 `app.py:13990`
> `allocation_dir = _first_corner_alloc_dir(side_mid)` 換為 `rot90_cw(SIDE)` ⇒ 其**線向 ∥SIDELINE**
> （真 winner 格 `R2/left@0m` 實測 `|cos| − 1` ＝ 一個 ULP）；而 `R4/left`（`forced`）之唯一宗**其 `is_corner` 亦 ＝ `True`**
> ⇒ **其遠側界已 ∥SIDELINE**，二態之第一個取值相異之分支實為
> **`stepg:657` `if _fo_left:`**（`cum_S`＝`0.0` vs ＝`buf`）與 **`app.py:13990` `if is_corner:`**（`marker` 之別）**二處**。

---

## `§七`　`⛔ 為之事`之逐項自檢（單 `§六`）

| # | 禁令 | 自檢 |
|---|---|---|
| `1` | ⛔ 改生產碼 `34` 檔一字 | ✅ 見 `§八` 閘 `2`／閘 `6`（blob 期初＝期末·相異 `0`） |
| `2` | ⛔ 開任何分支／⛔ 動用 KL 之放行 | ✅ 本批**未開**任何分支（`§八` 閘 `6'`）；KL 之放行**未被動用**（⛔ 改碼） |
| `3` | ⛔ 擬任何第二實作形／⛔ 由多邊形反推 `S1_par` | ✅ 本報告**⛔ 載**任何實作形；`§五-1` 之多邊形量測**其受詞為線之方向**（⛔ `S1_par` 之值） |
| `4` | ⛔ 改 `_corner_buffer_S`／`_build_corner_range_v3`／任何函式簽章 | ✅ 同 `1` |
| `5` | ⛔ 動 `ALPHA_LABELS` 一字 | ✅ `git diff --numstat 39ab6e32..HEAD -- verify/probes/probe_WG9269_pit_index.py` 輸出**空** |
| `6` | ⛔ 覆寫 `verify/baselines` 任一檔／⛔ `WV_BAKE`／⛔ 併線 `p3a`／⛔ 引任何自 baseline 取得之數 | ✅ `baselines` `298` 檔·框 `sha256` 未變；`WV_BAKE` ＝ `None`；`p3a` `rc = 1`；本報告之數皆出自**本批當場**之量測、**本單所供之 payload**、或**已入倉之落檔**（`WG9287R_landeffect.log`·逐處具名） |
| `7` | **⛔ 鑄任何號** | ✅ 四簿期末**逐位未動**（自誤 `383`／`393`·`GB` `168`／`170`·`VR` `80`／`95`·`K-9` `28`／`29`）；坑 `87`／`87` 未動；工項二之落地形機驗證其題**⛔ 可**被 `GB` 標題錨定框命中 |
| `8` | ⛔ 解除或收窄任何 `GB` | ✅ 本報告與落點**皆未載**任何解除／收窄；`GB-170` 之失效條件三款**仍皆未成就** |
| `9` | ⛔ 落地 `K-9-5-*`／`K-9-12`／`K-9-29` 之任何子項／⛔ 改藍影一字 | ✅ 同 `1` |
| `10` | ⛔ 判該側是否應有第 2 宗／⛔ 判 `forced` 側應否走 winner 側之路 | ✅ `§二-3`／`§二-5` 只述**現查**；**⛔ 作成**該類判斷 |
| `11` | ⛔ 追改任何已入倉文件一字 | ✅ 見 `§八` 閘 `1`（`numstat` 刪除欄全 `0`）＋ `wg942_append_audit.py` `rc = 0`；`§五-1` **⛔ 追改** `W-G.9-286`／`-287` 一字 |
| `12` | ⛔ 判孰誤、⛔ 提修法主張、⛔ 呈 KL | ✅ `§二-3` 逐字「⛔ 判孰誤」；`§五-1` 逐字「其處置**候發單側**」 |
| `13` | ⛔ 刪任何 ref | ✅ `p3a` 與主線 ref 皆在（`§八` 閘 `7`） |
| `14` | ⛔ 於任何入倉文件宣稱一件尚未發生之事 | ✅ `§八`／`§九` 為**入倉後**之末端追加；`ls-remote` 之實查於**推送後**出艙於聊天 |

---

【驗收】本批之驗收固定項已逐 token 出艙：
`ls-remote`／`SELF_SHA256`／`preflight`／`selftest`／`acceptance_audit`／`quotePath`／`uniq`／`deletions`／
`is_second_after_corner`／`corner_range_polys`／`_k923_gate1`／`_build_corner_range_v3`／`_corner_buffer_S`／
`cum_S`／`W_0`／`S1_par`／`GB-170`／`ast`／`numstat`／`ALPHA_LABELS`／`baselines`／`sha256`／`ls-tree`／`merge-base`。


---

## `§八`　收工閘（**入倉後**之末端追加·⛔ 預寫）

🛑 **本節之一切數皆於二 `commit`（`1333898`／`e6f9b06`）入倉**後**當場量**（`先跑再寫`）。

| # | 受詞（**產生指令**） | 實測 | 判 |
|---|---|---|---|
| `1` | `git -c core.quotePath=false show --numstat --format= <commit>` 逐檔具名 | `1333898` `+157 −0`（單）；`e6f9b06` `+19 −0`（`GB` 登記表）／`+299 −0`（本報告）／`+0 −0`／`+218 −0`／`+1 −0`（`neardir` 三檔）／`+0 −0`／`+116 −0`／`+1 −0`（`pitindex_pre` 三檔）／`+494 −0`（器）⇒ **刪除欄非 `0` 之檔數 ＝ `0`** | ✅ |
| `2` | `git diff --name-only <a> <b> -- <34 檔正面列舉>` | `39ab6e3..1333898` **`0`** 行／`1333898..e6f9b06` **`0`** 行／`39ab6e3..HEAD` **`0`** 行；對照組[必非零] `17fd981^..17fd981` ＝ **`2`** 行 | ✅ |
| `3` | `git show HEAD:<path> \| tr -cd '\r' \| wc -c` | 本批異動 **`10`** 檔逐檔 `CR` ＝ `0`·合計 **`0`**；判別力[必非零] `verify/out/KL_UI_3.5m_2e08a41_stdout.log` 之 blob `CR` ＝ **`2987`** | ✅ |
| `4` | `python verify/probes/probe_WG9267_issuer_measurers.py registry` | 自誤 `383`／`393`｜`GB` `168`／`170`｜`VR` `80`／`95`｜`K-9` `28`／`29` ⇒ **四簿逐位未動**（期初＝期末·**坐實⛔ 鑄號**） | ✅ |
| `5` | `python verify/probes/probe_WG9269_pit_index.py` | **`87`／`87`** 全數可解析·🔴 命中 **`0`**·末標籤 `bi` ⇒ **下一標籤 `bj`**（母體 ＝ `HEAD` 之追蹤 `.md` **`780`** 檔·期初 `778` ⇒ `+2` ＝ 本批新增之單與報告·**自洽**）；造甲 坑 `n` 定義處 `6` ≥ `1`／造乙 人造坑 `0`／`0` ⇒ **器非紅**；`stderr` `0` B；`ALPHA_LABELS` 一字未動（`git diff --numstat 39ab6e32..HEAD -- verify/probes/probe_WG9269_pit_index.py` 之輸出為**空**） | ✅ |
| `5'` | `python verify/tools/wg9223_acceptance_audit.py <本單> <本報告>` | `rc = 0`·【驗收】段 ＝ `:150`–`:154`·判定組（反引號 token）**`27`** 個 ⇒ **命中 `0` 之字樣 ＝ `0`**（受詞係 `index` ⇒ 已先 `git add`） | ✅ |
| `6` | 自限復驗 | `34` 檔 blob 期初＝期末 **相異 `0`**；`baselines` **`298`** 檔·框 `sha256` ＝ `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`；`p3a` `merge-base --is-ancestor` `rc` ＝ `1` ⇒ **非祖先**；`WV_BAKE` ＝ `None`；`K-9-29` 任何子項⛔ 落地／`GB-79`／`167`／`168`／`169`／`170` **⛔ 修** ⇒ 由「`34` 檔 blob 相異 `0`」**機械蘊含** | ✅ |
| `6'` | `git ls-remote origin 'refs/heads/verify/*'` | `verify/W-G.9-289-gb170` 命中 **`0`**（⇒ **⛔ 開**·本批亦**⛔ 開**任何分支）；判別力[必存在] `p3a` 命中 **`1`**（其 `20` 個 `verify/*` ref 全列已出艙於落檔） | ✅ |
| `7` | `git ls-remote origin refs/heads/wip/s1-endpart`（`push` **後**） | 🛑 **於推送後出艙於聊天**（⛔ 預寫·⛔ 於入倉文件宣稱一件尚未發生之事） | — |

🩸 **坑 `g`（照實併記）**：本批四個落檔中二個為 `CRLF`——`WG9290R_pitindex_pre.log`（`11527` B·`CR` `116` ＝ `LF` `116`）／
`WG9290R_neardir.log`（`32616` B·`CR` `218` ＝ `LF` `218`）⇒ **入倉前以二進位歸正**至 `LF`
（`11411` B／`32398` B·`CR` 皆 `0`·`Δ` ＝ `−116`／`−218` ＝ 各自之列數·**自洽**）。
`WG9290R_pitindex_post.log` 於本節落筆後同法歸正並入 `commit 3`。
🩸 **閘之量測與其所守護之動作為<u>分開之呼叫</u>**（`W-G.9-199` 常規補款 `一`）：閘 `1`–`6'` 之量測與 `push` **⛔ 置於同一命令塊**。

---

## `§九`　逐 `commit`

| # | `commit` | 主旨 | `numstat`（`+`／`−`） |
|---|---|---|---|
| `1` | `1333898` | `W-G.9-290` 工項零：本單原封入倉（三方逐位對拍·受詞自證·同格載產生指令）⛔ 零生產碼 | `+157`／**`−0`** |
| `2` | `e6f9b06` | `W-G.9-290` 工項一／二：winner 側第 1 宗之近側界係由鏈交遞取得（逐位 ∥SIDELINE）＋ 一則末端追加 ⛔ 零生產碼·⛔ 鑄號 | `+1148`／**`−0`**（`9` 檔） |
| `3` | （本 `commit`） | `W-G.9-290` 收工：收工閘 `1`〜`7` 之實測（報告入倉後量·嚴格末端追加）⛔ 零生產碼 | 見其自身之 `numstat` |

🔒 **本批為零生產碼批**（`常規一` 補款 `🔧 一`：零生產碼 `commit` **逕行 `push`**·⛔ 請示），
其判法（`git diff --name-only <前一已 push 之 HEAD>..<本 commit> \| grep -xE 'app\\.py|verify/stepg_pipeline\\.py|verify/run_all\\.py|verify/run_verification\\.py'`）
於**逐 `commit`** 皆為**空輸出** ⇒ 見上開收工閘 `2`。
🛑 **KL 之放行仍<u>未被動用</u>**——本批⛔ 改生產碼一字、⛔ 開任何分支。
🛑 **主線之 `ls-remote` 實查**（全 `40` 碼）於**推送後**出艙於聊天——**⛔ 預寫**。
