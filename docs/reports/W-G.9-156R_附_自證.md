# 🔒 `W-G.9-156R` 附件　收工閘 `10` 之**機械自證**

**受檢**：`verify/probes/probe_WG9156_pred_inputs.py`　**態**：`blob@5f06a659` 之工作區　**量測時點**：`2026-08-28`

---

## 甲　⛔ 無寫死絕對路徑（`verify/run_all.py` 之永久機檢）

🔒 **樣式逐字**（同 `run_all.py` 之 `_ABS_PAT`·**以片段串接構成**，否則本檢會咬到自己）：

```python
_ABS_PAT = ["C:" + "/", "C:" + chr(92), "/" + "Users" + "/",
            "Desktop" + "/land", "Desktop" + chr(92) + "land"]
```

| 受檢 | 命中列數 |
|---|---|
| `verify/probes/probe_WG9156_pred_inputs.py` | **`0`** |

🔒 **對照組（⛔ 命中 `0` 之斷言必附·常規四-六）**——同一支比對器餵二列人造字串：

| 對照列（人造·⛔ 不入倉） | 期望 | 實得 |
|---|---|---|
| 含樣式者（`REPO = r'…'` 之絕對路徑形） | 命中 | **命中 ✅** |
| 不含樣式者（`REPO = os.path.dirname(VERIFY)`） | 未命中 | **未命中 ✅** |

⇒ 🔒 **比對器對二造皆如預期** ⇒ 其 `0` 係**真 `0`**、⛔ 非量測器紅。
🔒 本檔之 `REPO` 由 `__file__` 推導：`REPO = os.path.dirname(VERIFY)`。

---

## 乙　⛔ 未 import `app.py`／`verify/wf_*` 之任何幾何函式

🔒 **框 ＝ `ast` 之 `Import`／`ImportFrom` 全走訪**（⛔ 非 `grep`——`grep` 會漏縮排於函式內之 import）。

| 行 | 模組 | 名 | 類 |
|---|---|---|---|
| `32` | `contextlib` | `—` | 標準庫 |
| `33` | `io` | `—` | 標準庫 |
| `34` | `math` | `—` | 標準庫 |
| `35` | `os` | `—` | 標準庫 |
| `36` | `subprocess` | `—` | 標準庫 |
| `37` | `sys` | `—` | 標準庫 |
| `39` | `numpy` | `—` | 第三方 |
| `40` | `shapely.affinity` | `rotate` | 第三方 |
| `40` | `shapely.affinity` | `translate` | 第三方 |
| `41` | `shapely.geometry` | `LineString` | 第三方 |
| `41` | `shapely.geometry` | `Polygon` | 第三方 |
| `41` | `shapely.geometry` | `box` | 第三方 |
| `222` | `app_harvest` | `harvest` | 🔧 **管線驅動**（取母體） |
| `223` | `run_verification` | `—` | 🔧 **管線驅動**（取母體） |
| `224` | `selection_pipeline` | `run_corner_pk` | 🔧 **管線驅動**（`run_corner_pk` ⇒ winner） |
| `225` | `stepg_pipeline` | `run_step_g` | 🔧 **管線驅動**（`run_step_g` ⇒ `G`／`②-宗` 輸出） |
| `226` | `probe_WG981_scope` | `—` | 🔬 **他探針之捕捉器**（`spy_solve`／`spy_pool`·⛔ 非幾何判準） |

🔒 **`app` 之命中 ＝ `0`**：全檔⛔ 無 `import app`／`from app import`／`exec(app`；
`app_harvest.harvest()` 係 **headless harness 之既有入口**（`CLAUDE.md §7` 逐字：專供 headless harness），
其回傳之 `ns` **本探針僅用以取母體與 `G`**、⛔ 未自其中取任何幾何函式。

🔒 **`wf_*` 之命中 ＝ `0`**（框 ＝ `wf_f0`／`wf_f1`／`wf_f2`／`wf_f3`／`wf_f4`）：

| 框 | 命中列數 | 對照組 |
|---|---|---|
| `wf_f0`〜`wf_f4`（全檔） | **`0`** | `run_step_g` ⇒ `6` 列 ⇒ 量測器非紅 |

### 🔒 `ns[...]` 之取用清單（**逐列具名**——證只取了二個 spy 之受包裝對象）

| 行 | 逐字 |
| `230` | `o_solve, o_pool = ns["_solve_G_one"], ns["_pool_strips_for_block"]` |
| `249` | `ns["_solve_G_one"] = w81.spy_solve(o_solve)` |
| `250` | `ns["_pool_strips_for_block"] = w81.spy_pool(o_pool)` |
| `267` | `ns["_solve_G_one"], ns["_pool_strips_for_block"] = o_solve, o_pool` |
| `477` | `"  ns['_solve_G_one']        = w81.spy_solve(o_solve)",` |
| `478` | `"  ns['_pool_strips_for_block'] = w81.spy_pool(o_pool)",` |

⇒ 🔒 僅 `_solve_G_one`／`_pool_strips_for_block` 二符號，且**只作 spy 之<u>包裝與還原</u>**
（`w81.spy_solve` / `w81.spy_pool` 於呼叫時**原樣轉呼原函式**並側錄其引數）
⇒ **⛔ 未以其為判準**；藍影／矩形容納／遞補迴圈**三判準全由本檔自寫**
（`cell_raw`／`pick_blue`／`gate1`／`gate2`／`rect_fit`／`touch_len`）。

---

## 丙　`P ⊖ R` 之方法界限（🔒 **⛔ 不得讀成「已證全角度不可容納」**）

| 判 | 健全性 |
|---|---|
| `False` ①款（**面積證書** `area(P) < W·D`） | 🔒 **解析證書·與角度無關** ⇒ **健全** |
| `False` ②款（全掃描角之 `P ⊖ R` 皆空） | 🔒 四角交集法對非凸 `P` 係真侵蝕之**超集** ⇒ 超集空 ⇒ 真侵蝕必空（**該角健全**）；⚠️ 惟角度係**有限掃描**（步長 `0.5°` ＋ 全部邊向）⇒ **⛔ 非全角度之數學證明** |
| `True` | 🔒 以 `P.contains(rect)` **實證** ⇒ **健全** |
| `None` | 侵蝕非空而無一候選實證 ⇒ **⛔ 不得逕判**（本批**未出現**此態） |

🔒 **本批之全部 `閘二 = False` 皆另附量化**（`D` 固定下之最大寬）：
`R1右 2.6162`／`R3右 第1宗 2.6420`／`R3右 628-29(1)+ 2.9217`／`R6右 628-38(1) 2.6307` m，門檻 `3.50 m`
⇒ 距門檻 `0.58`〜`0.88 m`，**⛔ 非刀鋒**（併看 `GB-102` 之法定值刀鋒案）。
