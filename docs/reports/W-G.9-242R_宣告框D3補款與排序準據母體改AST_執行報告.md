# W-G.9-242R　宣告框 `D3` 補款 ＋ 排序準據母體改 **AST** ＋ 五級依賴序入典 ＋ 自誤 `293`／`294`　執行報告

> **零生產碼**。`app.py`／`verify/**.py` **一字未動、亦⛔ 新增任何檔**（閘 `P` 前後各報一次·§七）。
> **⛔ 抽 seam**（順延為次一單·生產碼·須 KL 逐 commit 放行）。
> **⛔ 執行 `verify/run_all.py`／`run_verification.py`**（本單⛔ 需其輸出·實測本批未跑）。
> 掃描器係**拋棄式**、置於**倉外**、**⛔ 入倉**；入倉者只有其輸出表。
> 🔒 一切數字**當場現查於倉**，⛔ 採單所載之值；與單相異者逐項具名。

---

## §零　態錨

| 項 | 值（現查於 `2026-09-06`）|
|---|---|
| 開工態 `origin/wip/s1-endpart` | `cb4b82f27f33e1182daaf413a1417035f4e333e6`（`ls-remote` 現查）|
| 施工副本 | 短路徑拋棄式 clone `C:/Users/admin/AppData/Local/Temp/w240`（`core.autocrlf=false`）|
| 本報告產出時之 clone `HEAD` | `5f5cdcb`（＝ `cb4b82f` ＋ 工項零）|
| 掃描器所在 | `C:/Users/admin/AppData/Local/Temp/w240t/`（**倉外**·⛔ 入倉·⛔ 置於 `verify/` 或 `app.py` 側）|

---

## §一　開工閘

### `S-0`（單之完整性）✅ **綠**

payload **16837** B（全檔 **16915** B・**292** LF・**CR 0**）；`SELF_SHA256` 列命中 **1**；
宣告 ＝ 實算 ＝ `b1181a93b258a7261bc25ca944233a85aaae354781da0e444e9716b8eb78e88e`。

### `S-1`（號占用·宣告框）

🔒 **三軸**：來源 `blob@cb4b82f27f33e1182daaf413a1417035f4e333e6`／
母體 **全 `docs/` 558 檔**（其中 **19** 檔為 `.png`／`.jpg` 二進位而讀不到·可解碼 **539**·檔名皆⛔ 含單號）／
粒度框 **檔框 ＋ 列框**。母體取法 ＝ `git ls-tree -r -z --name-only`；逐檔取**倉側 blob**（`GB-139 ②`）。

| 號 | 宣告框 檔／列 | 鬆框 檔／列 | 單所載 | 判 |
|---|---|---|---|---|
| **`W-G.9-242`** | **1**／**1** | **2**／**8** | `1/1`・`2/8` | ✅ 相符（其處置見 `S-1′`）|
| `W-G.9-241` | **3**／**4** | **3**／**10** | `3/10`・`3/10` | 🔴 **宣告框列數不符**（見下）|
| `W-G.9-243` | **0**／**0** | **0**／**0** | `0/0`・`0/0` | ✅ 對照組 乙（次號）·相符 |
| 人造號（**代稱**·字樣⛔ 入倉·`GB-147`）| **0**／**0** | **0**／**0** | —— | ✅ 器須紅之造 |

🔴 **對照組 甲 `W-G.9-241` 之宣告框列數與單所載相異**：單載 `3／10`，實測 **`3／4`**。
其**鬆框** `3／10` 與單**相符** ⇒ 疑係抄錄時把鬆框列數填入宣告框欄。
🔒 **其角色判準（須 `≥ 1`）仍成立** ⇒ **⛔ 觸發本單所定之停機條件**（該條件之受詞係 `S-1′` 之落點·見單 `§零`）。
**`241` 宣告框之拆解（逐筆）**：`D1` 檔名 **2**（`-241` 單／`-241R` 報告）
＋ `D2` 標題 **4**（`-241:1`、`-241:113`、`交接文_W-G.9-240:177`、`-241R:1`）⇒ **檔 3／列 4**。

### `S-1′`（本單特則·**逐筆比對**·⛔ 憑命中數）✅ **綠**

`W-G.9-242` 之宣告框**唯一落點恰為**：

```
docs/orders/W-G.9-241_排序準據seam偵察與交接文更正.md:4
> ⛔ 動 `app.py`／`verify/**.py` 任何一字。**本單⛔ 抽 seam**——抽 seam 為 `W-G.9-242`，
```

被咬之款 ＝ **`D3`-「本單」同列**（**⛔** `D1`、**⛔** `D2`、**⛔** `D3`-列首）。
⇒ **非多一列、非少一列、落點與單所載逐字相同** ⇒ **⛔ 觸發停機**。

### `S-2`（append-only）✅

三張既有檔（`CLAUDE.md`／`GB` 簿／自誤簿）皆**純末端追加**，上文一字未改 ⇒ `deletions` 全 **`0`**（§七）。

---

## §二　工項零：本單原封入倉 ✅

`docs/orders/W-G.9-242_宣告框D3補款與排序準據母體改AST與依賴序入典.md`
**16915** B／**292** LF／**CR 0**／落檔 `sha256 cceb2709919622e6…`；
入倉 blob `90c2b9d9…`，其內容 `sha256` **與落檔逐位相同** ✅。
🛑 該閘只證「落檔→入倉」，**⛔ 證「聊天原文→落檔」**。

---

## §三　工項一：宣告框 `D3` 之邊界補款（`CLAUDE.md`）✅

| 項 | 值 |
|---|---|
| 追加形 | **純末端追加**（`\n---\n\n` ＋ payload ＋ `\n`）·上文一字未改 |
| payload 來源 | 本單**第 `71`–`97` 列**（四反引號圍欄在 `70`／`98`·邊界已逐列印出坐實）|
| 追加量 | **2026** B／**30** LF／**CR 0** |
| 改前 | 184114 B・2229 LF・`sha256 b1c1c38fca7f04278997c25393673059c9500ee76f64ad2e7761e9670925abfb` |
| 改後 | 186140 B・2259 LF・`sha256 a9f40e68f59980bbc2c435d77c6db4e7292e036798da987824eb92a4af20379d` |
| `numstat` | **`30 / 0`** ⇒ `deletions ＝ 0` ✅ |

**字樣錨（二形同格併載·改前／改後）**
🔒 三軸：改前 `blob@cb4b82f`／改後 本批工作區；母體 `CLAUDE.md` 單檔；粒度框 **列框**。

| 字樣 | 改前 | 改後 | 判 |
|---|---|---|---|
| `號占用閘之框`（受詞錨）| **1** | **2** | ✅ 改前唯一 |
| `宣告框`（判別力自檢·寬字樣）| **7** | **11** | ✅ **`> ` 受詞錨**（改前 `7 > 1`·改後 `11 > 2`）⇒ 該檢**非恆為 `1`** |

🔒 **入典之要旨**（逐字見該節）：`D3` 之「同列含「本單」＋該號」款，**僅於該號 ＝ 該檔檔名所載之單號時成立**；
`D3` 之另一款（列首即該號）與 `D1`／`D2`／`②`／`③`／`④` **一字未動**；⛔ 追改任何既出之取號結論。

---

## §四　工項二：排序準據母體改 **AST 為主 ＋ 列框為對照組**

### `a`　案由三洞之復現（⛔ 採單所載）✅ 全數復現

| 洞 | 單所載 | 本批復現 |
|---|---|---|
| `max/min(…, key=)` 未入列框 | 真漏 **2** | ✅ `verify/wf_f4.py:433`（`max(lots, key=(a, pid))`）／`:703`（`max(small, key=(dists,g))`）|
| 鍵在**續行** | **3** 處 | ✅ `:377`–`379`／`:662`–`663`／`:1346`–`1347`（AST 之 `lineno`–`end_lineno` 天然涵蓋）|
| 單自身錨表落在自身母體外 | **2**／`4` | ✅ `verify/wf_f2.py:99`（無級字面亦無 `sorted(`）／`verify/wf_f4.py:798`（「級別」⛔ 等於 `級1/2/3` 字面）|

### `b`　主框：AST（⛔ 列框）

🔒 **母體**：`verify/wf_f0.py` ∪ `verify/wf_f2.py` ∪ `verify/wf_f4.py` ∪ `app.py`。
🔒 **節點四款**（單 `§三 b` 逐字）：① `Call` 且 `func` 為 `Name(sorted|min|max)`；
② `Call` 且 `func` 為 `Attribute(attr='sort')`；③ `heapq.nsmallest|nlargest` 或 `Name(nsmallest|nlargest)`；
④ 上列節點 `keywords` 中 `arg == 'key'` 者之**實參完整原文**（`ast.get_source_segment`）。
🔒 **粒度框 ＝ 節點**（記 `lineno`–`end_lineno`），**⛔ 列**。
🔒 **三軸**：來源 `blob@cb4b82f`（`verify/**.py`／`app.py`；閘 `P` 給證其與 `-241R` 逐位相同）／母體 上開四檔／粒度框 **節點**。
🔒 **掃描器之兩造對照組**（同一 code path）：人造樣本之四款節點 **4/4** 命中、`plain_call(1)` **未被咬** ⇒ **GREEN**。

| 檔 | AST 站點 | 其中帶 `key=` | 列框命中列數（對照組）|
|---|---|---|---|
| `verify/wf_f0.py` | **12** | 2 | 12 |
| `verify/wf_f2.py` | **7** | 2 | 11 |
| `verify/wf_f4.py` | **71** | 10 | 54 |
| `app.py` | **277** | 50 | 88 |
| **合計** | **367** | **64** | **165**（相異列）|

**三集（同格併載·⛔ 只報其一）**

| 集 | 數 | 說明 |
|---|---|---|
| `AST ∖ 列框`（**新捕**之站點）| **215** | 其列範圍內⛔ 有任何列框命中列 |
| `AST ∩ 列框`（站點）| **152** | —— |
| `列框 ∖ AST`（**列**）| **21** | 單載「若非空即紅」⇒ **逐列具名於 `f`** |

🔒 **AST 之增益（構造上的）**：其**拆解巢狀呼叫**——例 `verify/wf_f2.py:85` 之
`max(sorted(qual), key=qual.get)` 於 AST 為**二站**（內層 `sorted(qual)`＋外層 `max(…, key=)`），
列框則只得**一列**；`verify/wf_f4.py:376` 同形。

### `c`　五點必中（單 `§三 b`·任一未捕 ⇒ 停機）✅ **GREEN**

| 必中之點 | 捕獲之站點 | 判 |
|---|---|---|
| `verify/wf_f4.py:433` | `433–433` `1·Name(max)` | ✅ |
| `verify/wf_f4.py:703` | `703–703` `1·Name(max)` | ✅ |
| `verify/wf_f4.py:379`（`:377` 之鍵所在列）| `377–379` `1·Name(sorted)` | ✅ |
| `verify/wf_f4.py:663`（`:662` 之鍵所在列）| `662–663` `1·Name(sorted)` | ✅ |
| `verify/wf_f4.py:1347`（`:1346` 之鍵所在列）| `1346–1347` `1·Name(sorted)` | ✅ |

🔒 三處續行係**由呼叫節點之 `lineno`–`end_lineno` 範圍涵蓋**，⛔ 另設規則。

### `d`　對照組：列框（沿用 `-241` 之框·⛔ 改其定義·⛔ 判準）

沿用 `sorted(` ∪ `.sort(` ∪ 級字面（`級1`／`級2`／`級3`），**列框**。
🔒 **判別力自證**：對照組之數 **165**（相異列）——**非零** ✅，且 **≠ AST 之 367** ✅
⇒ 二框**可分**，該量測器**非恆綠**。

### `e`　`app.py` 之界：三數同格對照 ＋ AST 何以能排除 widget 參數

🔒 **三軸**：來源 `blob@cb4b82f`／母體 `app.py` 單檔／粒度框 **逐欄載明**。

| 量 | 值 | 粒度框 |
|---|---|---|
| AST 下 `app.py` 之命中 | **277** | **節點**（四款）|
| ┗ 其中帶 `key=` 者 | **50** | **節點** |
| `key=` 之列框命中 | **216** | **列** |
| `key=lambda` 之列框命中 | **48** | **列** |

🛑 **⛔ 以 `216` 為「排序準據數」出艙**——其含大量非比較子。

🔒 **AST 何以能排除 widget 參數（構造 ＋ 實測）**
其只自**上開四款節點**之 `keywords` 取 `key`；Streamlit 之 `st.number_input(..., key="x")`
係 `func` 為 `Attribute(attr='number_input')` 之 `Call`，**⛔ 落於四款** ⇒ 構造上被排除。
**實測坐實**（`app.py` 全樹）：帶 `key=` 關鍵字之 `Call` 節點共 **208**，
其中落於四款者 **50**、**⛔ 落於四款者 158**；後者之 `func` 名分布（前 14）：

| func | 數 | func | 數 | func | 數 |
|---|---|---|---|---|---|
| `_ni` | 40 | `.selectbox` | 8 | `.download_button` | 5 |
| `.button` | 23 | `_cb` | 8 | `.text_input` | 5 |
| `.number_input` | 18 | `.radio` | 5 | `_di` | 4 |
| `.checkbox` | 14 | `_sb` | 5 | `.file_uploader` | 4 |
| `_sl` | 11 | | | `.data_editor` | 4 |

⇒ **被排除之 158 者全數為 Streamlit widget 或其包裝函式**（`_ni`／`_sl`／`_cb`／`_sb`／`_di` 係其本地包裝）。
🔒 **併記一差**：列框 `key=` **216 列** vs AST 全 `Call` 帶 `key` **208 節點**——
差之來源為**粒度不同**（列 vs 節點）＋ 列框亦咬**註解／字串內**之 `key=` 字面。**二數⛔ 互代**。

### `f`　`列框 ∖ AST` 之 **21** 列：逐列具名與成因（單載「非空即紅」）

🔒 **成因分二類，皆為「該列⛔ 為呼叫節點」** ⇒ AST 依其四款判準**本就不取**：

**類一　級字面（`19` 列）**——註解／docstring／字串常量／`dict` 欄值

| 檔:列 | 逐字（節錄）| 形 |
|---|---|---|
| `verify/wf_f0.py:135` | `ROUTE_OUT = {"G009": "轉F.2(同歸戶R4有達標宗·級1相鄰街廓)",` | dict 欄值 |
| `verify/wf_f2.py:3` | `W-F F.2 — 級1/2/3 跨街廓同歸戶合併（a′ 首次登場；…）` | docstring |
| `verify/wf_f2.py:20` | `UC9898 七轉出全級1（相鄰）；級2/3 不現。` | docstring |
| `verify/wf_f2.py:161`／`:163`／`:165` | `lvl = "級1相鄰"`／`"級2鄰近"`／`"級3非鄰近"` | 字串常量 |
| `verify/wf_f4.py:5` | `母體＝trunk D（F.3 終態）…E0(7-1 級1 殘餘) → E1(7-4) → E2(7-5)` | docstring |
| `verify/wf_f4.py:362` | `# ══ E0：殘餘同歸戶級1 sweep（§7-1 級1＋裁示2；…） ══` | 註解 |
| `verify/wf_f4.py:403`／`:404`／`:406`／`:410` | `f"E0級1殘餘併入 …"`／`"段": "E0級1"`／`"級別": "級1(同歸戶)"`／`"處置": "併入(§7-1級1)"` | 字串常量／dict 欄值 |
| `verify/wf_f4.py:487` | `LV = {0: "級1相鄰", 1: "級2鄰近", 2: "級3非鄰近"}` | dict 欄值（**顯示字面表**）|
| `verify/wf_f4.py:1526`／`:1541`／`:1543`／`:1563` | `("E0級1", "E0級1")` 等段名對照與鏈文案 | 字串常量 |
| `verify/wf_f4.py:1535`／`:1537` | `#   梯0：…／殘旗標宗 E0 級1／…`／`#   梯2：…E0 級1(G011)…` | 註解 |

**類二　註解／docstring 內**引述**舊寫法（`2` 列）**

| 檔:列 | 逐字（節錄）|
|---|---|
| `app.py:9371` | `（\`sorted(offset_land.geoms, key=area, reverse=True)\`），使 g_rows 抵費地列之` |
| `app.py:9555` | `# 回傳序＝**面積遞減**（逐字沿用舊 boolean 式慣例 \`sorted(..., key=area, reverse=True)\`）` |

🔒 **判**：`21` 列**逐列皆為非可執行之文字**（級字面 `19` ＋ 註解內引述 `2`）
⇒ 該差集**⛔ 證 AST 漏抓**；其反面意義為 **AST 之框排除了非碼面之字面命中**。
🛑 **⛔ 以「差集非空」逕判 AST 紅**——單所令者係「逐列具名並判其成因」，本節已逐列為之。
🔒 **`verify/wf_f4.py:798`（`"級別": LV[_level(gid, blk)]`）⛔ 在此 21 列內**
——其既⛔ 在列框（無級字面）、亦⛔ 在 AST（非四款節點），故**二框皆不取**；
其角色（輸出欄）已於 `-241R §三 b` 逐字處置，本批**⛔ 追改**。

### `g`　角色判（**367** 站·逐點·⛔ 抽樣）

🔒 **口徑沿用 `-241R`**：`A` 選塊準據（seam 之受詞）／`B` 輸出排版／`C` 內部決定性／`D` 其他；
凡 `D` 而**係選擇準據但受詞非「選塊」**者，其角色格**逐字載明其受詞**。
🔒 **完備性機檢**：各 (檔, 樣式) 之表列數 ＝ 獨立計得之數 ⇒ **GREEN**；
分類器另設二自檢並**當場咬中二瑕**（皆已修·見下）。

**角色分布**：`A` **19**／`B` **66**／`C` **85**／`D` **197**。

**判之工法（逐字·⛔ 抽樣）**
- **`151` 站**係**逐站覆寫**（含全部 `64` 個帶 `key=` 之真比較子）。
- **`216` 站**由**具名之機械判準**判定，其判準逐字為：

| 桶 | 判準（機械·可稽核）| 站數 | 角色 |
|---|---|---|---|
| `S` | `min`／`max` 且**位置引數 `≥ 2`** 且⛔ `key=` ⇒ **純量夾擠／邊界裁切**，受詞為**一個數值之上下界**、⛔ 一組候選之序 | **132** | `D` |
| `E` | `min`／`max` 之**單一可迭代引數**且⛔ `key=` ⇒ **聚合取極值**，產出**一個量**（範圍／門檻／殘差上界）| **53** | `D` |
| `N` | `sorted(x)` ⛔ `key=` ⇒ 集合／字典之**決定性列舉**，各元素處理獨立 | **24** | `C` |
| `T` | `xs.sort()` ⛔ `key=` ⇒ 原地自然序，供其後比較或串接 | **7** | `C` |

🛑 **此⛔ 抽樣**：每一站點皆列於下表並各帶其角色與理由；桶判準者其理由即該判準之逐字。

🩸 **分類器自檢當場咬中之二瑕（已修·⛔ 隱去）**
1. **`K` 桶漏判 `1` 站**（`app.py:5373` `_rows.sort(key=str(block))`）——由「`K` 桶不得落入預設」之自檢捕得，已補判 `B`。
2. **同列多站共用覆寫**——`app.py:9022` 同列有**二站**（外層 `max(_compl, key=…)` 與內層 `max(c['both'], abs(c['gap']))`），
   原以 (檔, 列) 為鍵之覆寫使**內層純量 `max` 被連帶改判**；已改以 (檔, 列, 桶) 精確覆寫。
   🔒 **診斷**：同列多站者共 **36** 列，其中**角色相異**者僅此 **1** 處。

#### 逐點表（**367** 列·全表）

| 檔:列 | 節點類 | 逐字（AST 原文）| 角色 | 判之依據 |
|---|---|---|---|---|
| `verify/wf_f0.py:204` | `N·sorted` | `sorted(cell.items())` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `verify/wf_f0.py:218` | `K·sorted` | `sorted(qual, key=_key)` | **A** | 級0 標的宗選定；輸入 `qual`（達標且非畸零之宗）／鍵 `_key=(-G, 暫編地號)`／消費端 `decisions[].target` → `_transform`。🔒 受詞係**同街廓級0**，**五級⛔ 適用** |
| `verify/wf_f0.py:222` | `K·sorted` | `sorted(lots, key=_key)` | **A** | 級0' 標的宗選定；輸入 `lots`（全部宗）／鍵同 `_key`／消費端同上。🔒 **五級⛔ 適用** |
| `verify/wf_f0.py:228` | `N·sorted` | `sorted(zones)` | **B** | 寫入 `decisions` 之輸出欄 |
| `verify/wf_f0.py:284` | `N·sorted` | `sorted(all_merged & win_set)` | **C** | 斷言用集合之決定性列舉，其值只進 `raise`／比對 |
| `verify/wf_f0.py:319` | `N·sorted` | `sorted(set(GSA_EXPECT[tag]) - set(gsa))` | **C** | 斷言用集合之決定性列舉，其值只進 `raise`／比對 |
| `verify/wf_f0.py:338` | `N·sorted` | `sorted(gsa)` | **B** | `raise` 訊息內之 f-string |
| `verify/wf_f0.py:386` | `N·sorted` | `sorted(fa \| fb)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `verify/wf_f0.py:403` | `N·sorted` | `sorted({r["所屬街廓"] for r in A.values()})` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `verify/wf_f0.py:407` | `S·max` | `max(0, k-1)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f0.py:433` | `N·sorted` | `sorted(poolB)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `verify/wf_f0.py:443` | `N·sorted` | `sorted(removed)` | **B** | 寫入 `decisions` 之輸出欄 |
| `verify/wf_f2.py:85` | `N·sorted` | `sorted(qual)` | **A** | 🔒 **同列二站**：內層 `sorted(qual)` 係外層之輸入正規化（`A-附屬`）；外層 `max(sorted(qual), key=qual.get)` ＝ **F.2 目標街廓選定**（ΣG 最大·並列取字典序·碼內註解逐字）／消費端 `_decide` → `raw` → `inject`／`transfers` |
| `verify/wf_f2.py:85` | `K·max` | `max(sorted(qual), key=qual.get)` | **A** | 🔒 **同列二站**：內層 `sorted(qual)` 係外層之輸入正規化（`A-附屬`）；外層 `max(sorted(qual), key=qual.get)` ＝ **F.2 目標街廓選定**（ΣG 最大·並列取字典序·碼內註解逐字）／消費端 `_decide` → `raw` → `inject`／`transfers` |
| `verify/wf_f2.py:86` | `K·sorted` | `sorted(blks[tgt_blk], key=lambda r: (-float(r["G(㎡)"]), r["暫編地號"]))` | **A** | F.2 目標**宗**選定；輸入 目標街廓內該歸戶之宗／鍵 `(-G, 暫編地號)`／消費端 `inject[tgt] += m1` → trunk C |
| `verify/wf_f2.py:87` | `N·sorted` | `sorted(blks.items())` | **C** | `src_rows` 之列舉序：非達標塊之**全部**列皆取（⛔ 選擇），序只定 `raw`／`conv_rows` 之列序 |
| `verify/wf_f2.py:200` | `N·sorted` | `sorted(poolC)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `verify/wf_f2.py:250` | `N·sorted` | `sorted({r["所屬街廓"] for r in B.values()})` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `verify/wf_f2.py:261` | `N·sorted` | `sorted(remove2)` | **B** | `"removed": sorted(remove2)` 輸出欄 |
| `verify/wf_f4.py:256` | `S·max` | `max(mina, gw)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:270` | `S·max` | `max(a, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:340` | `E·min` | `min(mina.values())` | **D** | `min(mina.values())` ＝ **`MinA_區`（門檻值）**；受詞為一個量，⛔ 候選之序 |
| `verify/wf_f4.py:368` | `K·sorted` | `sorted(flagged, key=lambda x: x["暫編地號"])` | **C** | E0 sweep 之處理序（按暫編地號）；各 `r` 之併入互不相依，其結果於 `:396` 另行排序後消費 |
| `verify/wf_f4.py:376` | `N·sorted` | `sorted(qual)` | **A** | 🔒 **同列二站**：內層 `sorted(qual)` 為輸入正規化（`A-附屬`）；外層 `max(…, key=qual.get)` ＝ **E0 目標街廓選定** |
| `verify/wf_f4.py:376` | `K·max` | `max(sorted(qual), key=qual.get)` | **A** | 🔒 **同列二站**：內層 `sorted(qual)` 為輸入正規化（`A-附屬`）；外層 `max(…, key=qual.get)` ＝ **E0 目標街廓選定** |
| `verify/wf_f4.py:377–379` | `K·sorted` | `sorted([x for x in byg[gid][tb] if float(x["G(㎡)"]) >= mina[tb] and not x["畸零地旗標"].strip()], key=lambda x: (-float(x["` | **A** | E0 目標**宗**選定；鍵 `(-G, 暫編地號)`（**跨列 377–379**·AST 已天然涵蓋）／消費端 `e0_pairs` → E0 併入 |
| `verify/wf_f4.py:388` | `N·sorted` | `sorted(x[1]["暫編地號"] for x in e2_class)` | **C** | 二 `sorted` 之**相等比對**（第2梯類源宗 vs 具名錨），係斷言 |
| `verify/wf_f4.py:388` | `N·sorted` | `sorted(E2_NAMED.values())` | **C** | 二 `sorted` 之**相等比對**（第2梯類源宗 vs 具名錨），係斷言 |
| `verify/wf_f4.py:390` | `N·sorted` | `sorted(x[1]['暫編地號'] for x in e2_class)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:392` | `N·sorted` | `sorted(x[1]['暫編地號'] for x in e2_class)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:395` | `N·sorted` | `sorted(_rm0 & win_set)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:396` | `N·sorted` | `sorted(e0_pairs.items())` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:433` | `K·max` | `max(lots, key=lambda x: (x["a"], x["pid"]))` | **A** | 🔴 **歸戶錨點宗之選定**（`max(lots, key=(a, pid))`）⇒ `ginfo[gid]["anchor"]` ⇒ `dists` ⇒ **`:488`／`:512`／`:662`／`:689` 全部距離準據之<u>起算點</u>**。🔴 **此站⛔ 在 `-241` 之列框母體內**——改 AST 後方入框 |
| `verify/wf_f4.py:441` | `N·sorted` | `sorted({x["類"] for x in lots if x["類"]})` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:452–453` | `N·sorted` | `sorted(g for g, gi in ginfo.items() if "RD" in gi["類集"] and g in _bld_gids)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:488` | `K·sorted` | `sorted(mina, key=lambda b: (_level(gid, b), dists[(gid, b)], b))` | **A** | 🔴 **seam 主站**；輸入 `mina`（全部可配街廓）／鍵 `(_level(gid,b), dists[(gid,b)], b)`（`_level` 定義於 `:483`–`:486`）／消費端 `border[gid]` → `:674` 首個 `_usable` 即 `pick` → `requests` → **實際配地**。🔒 **「級序 → 選塊」之唯一路徑** |
| `verify/wf_f4.py:499` | `S·max` | `max(eng.pool(blk) - unreach.get(blk, 0.0) - 1.0, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:500` | `S·min` | `min(a2, max(1.0, eatable - 5.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:500` | `S·max` | `max(1.0, eatable - 5.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:512` | `K·sorted` | `sorted(mina, key=lambda b: (dists[(gid, b)], b))` | **A** | ½ 輪0 之**最近塊**選定；鍵 `(dists, b)`——**⛔ 含 `_level`**／消費端 `_trial` → `half_r0` → `comp_groups` → **½ 線判定（配地 vs 現金補償）** |
| `verify/wf_f4.py:514` | `N·sorted` | `sorted(ginfo)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:523` | `N·sorted` | `sorted(comp_groups)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:523` | `N·sorted` | `sorted(COMP_EXPECT)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:525` | `N·sorted` | `sorted(comp_groups)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:526` | `N·sorted` | `sorted(COMP_EXPECT)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:546` | `N·sorted` | `sorted(post_price)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:549` | `N·sorted` | `sorted(comp_groups)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:576` | `S·max` | `max(a_rem[g], 50.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:577` | `S·max` | `max(G / a2p, 0.05)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:648` | `S·min` | `min(a_rem[_g2] + _back, ginfo[_g2]["a"])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:662–663` | `K·sorted` | `sorted(alloc - spset, key=lambda g: (min(dists[(g, b)] for b in mina), g))` | **A** | 🔴 **E1 歸戶處理序**（全域佇列）；鍵 `(min(dists…), g)`（**跨列 662–663**）／消費端 `:672` 逐歸戶選塊 → `requests` |
| `verify/wf_f4.py:663` | `E·min` | `min(dists[(g, b)] for b in mina)` | **A** | `A-附屬`：`:662` 之**鍵內式** `min(dists[(g,b)] for b in mina)`＝至最近可達塊之距。🔴 AST 將其**另立為站**，列框則⛔ 及之 |
| `verify/wf_f4.py:688` | `N·sorted` | `sorted(requests)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:689` | `K·sorted` | `sorted(requests[blk], key=lambda g: (dists[(g, blk)], g))` | **A** | 🔴 **同塊內歸戶之分攤序**；鍵 `(dists[(g,blk)], g)`（行末註解逐字「裁定K：距離優先」）／消費端 `demG`／`shares` → `:703` 剔除 |
| `verify/wf_f4.py:703` | `K·max` | `max(small, key=lambda g: (dists[(g, blk)], g))` | **A** | 🔴 **同級比例分攤之剔除準據**（剔最遠者）；`:689` 之對偶。🔴 **此站⛔ 在 `-241` 之列框母體內** |
| `verify/wf_f4.py:705` | `S·min` | `min(shares[g], demG[g])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:708` | `S·min` | `min(shG / (_conv(g, blk) * _ratio(g, blk)), a_rem[g])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:718` | `S·max` | `max(0.0, a_rem[g] - need)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:749` | `S·max` | `max(a_rem[last_g] + d_a, 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:776` | `N·sorted` | `sorted(v)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:790` | `N·sorted` | `sorted(placed.items())` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:811` | `N·sorted` | `sorted(x[1]["暫編地號"] for x in e2_class)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:813` | `N·sorted` | `sorted(set(rm2) & win_set)` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:857` | `N·sorted` | `sorted(alloc)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:862` | `N·sorted` | `sorted(syn_ids.items())` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:873` | `N·sorted` | `sorted(per_blk)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:967` | `E·max` | `max(p[0] * ax + p[1] * ay for p in cs)` | **D** | 幾何投影之極值（`max/min(p·a for p in cs)`）⇒ 產出一個範圍量 |
| `verify/wf_f4.py:968` | `E·min` | `min(p[0] * ax + p[1] * ay for p in cs)` | **D** | 幾何投影之極值（`max/min(p·a for p in cs)`）⇒ 產出一個範圍量 |
| `verify/wf_f4.py:977` | `N·sorted` | `sorted(mina)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:1012` | `N·sorted` | `sorted(pool_final)` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1014` | `N·sorted` | `sorted(comp_groups)` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1017` | `N·sorted` | `sorted(comp_groups)` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1020` | `N·sorted` | `sorted({s[0] for s in spill_75})` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1021` | `N·sorted` | `sorted(pool_final.items())` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1079` | `N·sorted` | `sorted(mina)` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:1081` | `S·max` | `max(eng.pool(b) - unreach.get(b, 0.0), 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1111` | `S·min` | `min(a_full, max(3.0, reachable[b] * 0.5))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1111` | `S·max` | `max(3.0, reachable[b] * 0.5)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1132` | `S·max` | `max(0.0, gt - G)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1133` | `S·max` | `max(G, gt)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1169` | `N·sorted` | `sorted(cost.items())` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1170` | `T·sort` | `feas.sort()` | **A** | **§7-5 第2梯最佳化·canonical 最優**：`feas.sort()` → `feas[0][0]`；鍵＝ tuple 自然序 `(總增配金額, Σ增配面積, Σ質心起迄距, combo)`。🔒 **五級⛔ 適用 §7-5** |
| `verify/wf_f4.py:1175` | `E·max` | `max(post_price.values())` | **D** | `SLACK`／`max_err` 之聚合取極值 ⇒ 產出一個量（band 充分性斷言之輸入） |
| `verify/wf_f4.py:1205` | `S·max` | `max(0.0, gt - G)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1209` | `S·max` | `max(G, gt)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `verify/wf_f4.py:1224` | `E·max` | `max(abs(canon_by_combo[r[3]] - r[0]) for r in actual)` | **D** | `SLACK`／`max_err` 之聚合取極值 ⇒ 產出一個量（band 充分性斷言之輸入） |
| `verify/wf_f4.py:1228` | `T·sort` | `actual.sort()` | **A** | **§7-5 第2梯最佳化·終局指派**：`actual.sort()` → `best = actual[0]` → `assign`。🔒 **五級⛔ 適用 §7-5** |
| `verify/wf_f4.py:1232` | `N·sorted` | `sorted({r[0] for r in actual})` | **C** | 群／塊／指派／斷言集之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:1290` | `N·sorted` | `sorted(cost.items())` | **B** | 回傳 dict 之輸出欄 |
| `verify/wf_f4.py:1346–1347` | `K·sorted` | `sorted([r for r in lots if r["推進側別"] == side], key=lambda x: float(x.get("累積S(m)", 0) or 0))` | **D（選序·受詞＝同側宗之整形序）** | E3 楔形遞補整形：同側宗按 `累積S(m)` 升序（**跨列 1346–1347**）。受詞為宗之整形序、**⛔ 選塊** |
| `app.py:86` | `K·sort` | `result['data'].sort(key=lambda x: x['ym'])` | **B** | 報表／UI 之顯示序（時序、缺口率、最終序位、群組、地號） |
| `app.py:279` | `S·max` | `max(0, round((trans_date - comp).days / 365.25, 1))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:302` | `S·min` | `min(10, len(case_df))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:315` | `S·min` | `min(10, len(land_df))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:401` | `S·min` | `min(10, len(df))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:514` | `S·max` | `max(gf * 0.10, 5.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:518` | `S·max` | `max(gf * 0.125, 25.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:782` | `N·sorted` | `sorted(set(rp['layer'] for rp in raw_polys))` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:819` | `K·max` | `max(union_geom.geoms, key=lambda g: g.area)` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:825` | `K·max` | `max(compound, key=lambda p: p['area_m2'])` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:884` | `K·sort` | `_parsed.sort(key=lambda x: -x[0])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:925` | `N·sorted` | `sorted(set(rp['layer'] for rp in raw_polys))` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:1441` | `K·sort` | `_rk.sort(key=lambda x: (-x['overlap_m'], x['block']))` | **C** | `_best_block` 之候選決定性排序（`-overlap_m, block`）——受詞＝**線↔街廓綁定**，⛔ 分配選塊 |
| `app.py:1504` | `E·min` | `min(_sl_dist2(_se, _p1) for _se in _s_ends)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:1505` | `E·min` | `min(_sl_dist2(_se, _p2) for _se in _s_ends)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:1506` | `S·min` | `min(_d1, _d2)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:1527–1529` | `S·max` | `max( _legacy_bs.get('left', 0.0), _legacy_bs.get('right', 0.0) )` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:1678` | `K·sort` | `_cands.sort(key=lambda c: (c['perp_m'], str(c['br'].get('handle', ''))))` | **C** | BASELINE 候選／等價 handle 之決定性擇一，受詞＝圖層配對 |
| `app.py:1713` | `S·max` | `max(_lo_r, _Ldist / _len_seg)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:1719` | `S·max` | `max(_EPS_LEGAL, min(_raw_q, _EPS_LEGAL_CEIL))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:1719` | `S·min` | `min(_raw_q, _EPS_LEGAL_CEIL)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:1726` | `N·sorted` | `sorted(str(c['br'].get('handle', '')) for c in _cands)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:1727` | `K·min` | `min(_cands, key=lambda c: str(c['br'].get('handle', '')))` | **C** | BASELINE 候選／等價 handle 之決定性擇一，受詞＝圖層配對 |
| `app.py:1798` | `N·sorted` | `sorted(_layers_found)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:2051` | `E·min` | `min(_ts)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:2051` | `E·max` | `max(_ts)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:2150` | `N·sorted` | `sorted(_per_group.items())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:2156` | `N·sorted` | `sorted(set(agg['parcels']))` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:2599` | `N·sorted` | `sorted({v for v in zones_map.values() if v})` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:2740` | `E·min` | `min(xs_only)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:2740` | `E·max` | `max(xs_only)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:2741` | `E·min` | `min(ys_only)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:2741` | `E·max` | `max(ys_only)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:2742` | `S·max` | `max((maxx - minx) * 1.5, 10.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:2743` | `S·max` | `max((maxy - miny) * 1.5, 10.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:3104` | `N·sorted` | `sorted({v for v in zones_map.values() if v})` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:3310` | `K·sort` | `rows_with_geom.sort(key=lambda x: x[0])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:3787` | `K·sort` | `candidates.sort(key=lambda x: (x[0], x[1]))` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:4016` | `T·sort` | `edges.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:4036` | `T·sort` | `edges.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:4065` | `K·max` | `max(inter_poly.geoms, key=lambda g: g.area)` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:4082` | `E·max` | `max(cut_dists)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:4140` | `K·sort` | `integrity_warnings.sort(key=lambda x: -x['缺口率_%'])` | **B** | 報表／UI 之顯示序（時序、缺口率、最終序位、群組、地號） |
| `app.py:4745` | `S·max` | `max(_np.linalg.norm(p1 - ip), _np.linalg.norm(p2 - ip))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:4746` | `S·max` | `max(_np.linalg.norm(p3 - ip), _np.linalg.norm(p4 - ip))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:4792` | `S·max` | `max(pair_A, pair_B)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:4793` | `S·min` | `min(pair_A, pair_B)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:4855` | `S·max` | `max(0.0, 1.0 - float(C_value or 0.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:4946` | `K·max` | `max(range(len(edges)), key=lambda i: edges[i]['length'])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:4951` | `K·sort` | `remaining.sort(key=lambda x: -x[1])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:5014` | `S·max` | `max(original_area, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5042` | `T·sort` | `mbr_edge_lens.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:5130` | `K·sort` | `side_lengths.sort(key=lambda t: (t[0]['p1'][0] + t[0]['p2'][0]) / 2.0)` | **C** | 側邊按中點 x 排序，供**左右判定**之決定性 |
| `app.py:5300` | `S·min` | `min(_d, 180.0 - _d)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5307` | `S·max` | `max(0.0, min(_hi, _Lseg) - max(_lo, 0.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5307` | `S·min` | `min(_hi, _Lseg)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5307` | `S·max` | `max(_lo, 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5373` | `K·sort` | `_rows.sort(key=lambda r: str(r['block']))` | **B** | `_rows.sort(key=str(block))` ＝ 診斷表之顯示序 |
| `app.py:5487` | `S·min` | `min(_da, 180.0 - _da)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5527` | `K·max` | `max(_fm, key=lambda x: x[1])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:5655` | `S·min` | `min(_da, 180.0 - _da)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5661` | `S·max` | `max(min(_ta, _tb), 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5661` | `S·min` | `min(max(_ta, _tb), 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5661` | `S·min` | `min(_ta, _tb)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5661` | `S·max` | `max(_ta, _tb)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5760` | `S·max` | `max(0.0, (rw_from_width(W_cur) - rw_from_width(W_prev)) / 100.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5918` | `E·max` | `max(proj_n)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5918` | `E·min` | `min(proj_n)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5930` | `K·sorted` | `sorted(seg, key=lambda q: q[0])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:5941` | `S·max` | `max(min(p[0] for p in fw), min(p[0] for p in bw))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5941` | `E·min` | `min(p[0] for p in fw)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5941` | `E·min` | `min(p[0] for p in bw)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5942` | `S·min` | `min(max(p[0] for p in fw), max(p[0] for p in bw))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5942` | `E·max` | `max(p[0] for p in fw)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5942` | `E·max` | `max(p[0] for p in bw)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5950` | `E·min` | `min(depths)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5950` | `E·max` | `max(depths)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5956` | `S·min` | `min(d1, d2)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5956` | `S·max` | `max(d1, d2)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5961` | `S·max` | `max(D_avg, 1e-6)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5969` | `S·min` | `min(d1, d2)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:5993` | `E·max` | `max(_xs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5993` | `E·min` | `min(_xs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5993` | `E·max` | `max(_ys)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:5993` | `E·min` | `min(_ys)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6213` | `E·min` | `min(_offs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6213` | `E·max` | `max(_offs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6215` | `E·min` | `min(_abs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6215` | `E·max` | `max(_abs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6443` | `S·max` | `max(0.0, min(0.9, tb))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6443` | `S·min` | `min(0.9, tb)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6465` | `S·max` | `max(0.0, G_raw)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6504` | `S·max` | `max(float(np.linalg.norm(d)), 1e-9)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6511` | `K·sort` | `edges.sort(key=lambda e: -e[2])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:6513` | `S·max` | `max(float(np.linalg.norm(dv)), 1e-9)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6603` | `S·max` | `max(0.0, max(max(_tvr[_i], _tvr[_i + 1]) for _i in _fe))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6603` | `S·max` | `max(_tvr[_i], _tvr[_i + 1])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6603` | `E·max` | `max(max(_tvr[_i], _tvr[_i + 1]) for _i in _fe)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6616` | `S·max` | `max(0.0, 1.0 - _g * _g)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6634` | `E·min` | `min(abs(_x) for _x in _dep)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6639` | `N·sorted` | `sorted(_re)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:6642` | `N·sorted` | `sorted(set(_re) \| {(_i + 1) % _n_e for _i in _re})` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:6643–6644` | `K·sorted` | `sorted(((_ring[_i][1], _dep[_i], _ring[_i][0]) for _i in _ridx), key=lambda _r: _r[0])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:6838` | `E·min` | `min(_tv)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6841` | `E·min` | `min(_tv)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6859` | `E·max` | `max(_tv)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6861` | `E·max` | `max(_tv)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6913` | `N·sorted` | `sorted(_fe_idx)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:6915` | `S·max` | `max(0.0, max(max(_tv[_i], _tv[_i + 1]) for _i in _fe_idx))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6915` | `S·max` | `max(_tv[_i], _tv[_i + 1])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:6915` | `E·max` | `max(max(_tv[_i], _tv[_i + 1]) for _i in _fe_idx)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6960` | `E·max` | `max(_xs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6960` | `E·min` | `min(_xs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:6969` | `N·sorted` | `sorted(_ts)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:7227` | `S·max` | `max(0.1, max(projs))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:7227` | `E·max` | `max(projs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:7299` | `K·sort` | `candidates.sort(key=lambda x: -x[1])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:7359` | `K·sort` | `candidates.sort(key=lambda x: -x[1])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:7457` | `S·max` | `max(edge_len * 2.0, 100.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:7473` | `K·max` | `max(clipped.geoms, key=lambda ls: ls.length)` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:7619` | `K·sorted` | `sorted(parcels, key=_proj_of)` | **D（選序·受詞＝原位次投影序）** | `_projection_order` 本體 `sorted(parcels, key=_proj_of)`——**位次序不變量之單一真相源**，⛔ 選塊準據 |
| `app.py:7813` | `N·sorted` | `sorted(set(_got) ^ set(_exp))` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7844` | `N·sorted` | `sorted(_val)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7847` | `N·sorted` | `sorted(x for x in _val if not x.startswith(_pfx))` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7859` | `N·sorted` | `sorted(_got_rm)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7859` | `N·sorted` | `sorted(_rm)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7859` | `N·sorted` | `sorted(_got_rm ^ _rm)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7860` | `N·sorted` | `sorted(_got_ad)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7860` | `N·sorted` | `sorted(_ad)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7860` | `N·sorted` | `sorted(_got_ad ^ _ad)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7883` | `N·sorted` | `sorted(_got - _bs)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:7947` | `E·max` | `max(t['J'] for t in table)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:7950` | `K·min` | `min(cand, key=lambda t: (t['dev'], t['k']))` | **D（選序·受詞＝滑池槽 k\*）** | `min(cand, key=(dev,k))`——`J` 最大之 ε 帶內取最靠中央、再取小 `k`（碼內註解逐字 STEP 3） |
| `app.py:8287` | `S·min` | `min(4, len(mbr_coords) - 1)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:8290` | `T·sort` | `mbr_edges.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:8294` | `S·max` | `max(mbr_short * 0.25, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:8295` | `E·min` | `min(rxs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:8295` | `E·max` | `max(rxs)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:8296` | `E·min` | `min(rys)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:8296` | `E·max` | `max(rys)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:8321` | `K·sort` | `arms.sort(key=lambda a: -a.area)` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:8379` | `K·sort` | `edges.sort(key=lambda e: -e['L'])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:8667` | `K·sort` | `candidates.sort(key=lambda x: x[0])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:8828` | `S·max` | `max(bnd[2] - bnd[0], bnd[3] - bnd[1])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:8956` | `S·max` | `max(_b[2] - _b[0], _b[3] - _b[1])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:8999` | `E·max` | `max((c['resid'] for c in _chain), default=0.0)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:9000` | `E·max` | `max((c['both'] for c in _compl), default=0.0)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:9001` | `E·max` | `max((abs(c['gap']) for c in _compl), default=0.0)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:9015` | `K·max` | `max(_chain, key=lambda c: c['resid'])` | **B** | 診斷表之取最大（`resid`／`both`|`gap`），供訊息與列示 |
| `app.py:9022` | `K·max` | `max(_compl, key=lambda c: max(c['both'], abs(c['gap'])))` | **B** | 診斷表之取最大（`resid`／`both`|`gap`），供訊息與列示 |
| `app.py:9022` | `S·max` | `max(c['both'], abs(c['gap']))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出）（`:9022` 之**內層** `max(c['both'], abs(c['gap']))`；同列外層之 `max(_compl, key=…)` 另判 `B`） |
| `app.py:9223` | `E·min` | `min(ts)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:9223` | `E·max` | `max(ts)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:9244` | `E·max` | `max(s_vals)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:9310` | `S·max` | `max(s_min, 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9408` | `T·sort` | `biz_iv.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:9414` | `S·max` | `max(merged[-1][1], b)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9423` | `S·min` | `min(a, s_max)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9424` | `S·max` | `max(cur, b)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9522` | `S·max` | `max(0, n_biz - 1)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9558` | `K·sorted` | `sorted(pieces, key=lambda g: g.area, reverse=True)` | **C** | 抵費地片之回傳序（面積遞減）——只定 `{blk}-抵費地-{i}` 之**編號**（碼內註解逐字「與回傳序無關」之內部 s 序另有其物） |
| `app.py:9770` | `S·max` | `max(_pool_lo, _reserve['lo'])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9772` | `S·min` | `min(_pool_hi, _reserve['hi'])` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:9830` | `S·max` | `max(0.1, _pool_S)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:10041` | `S·max` | `max(0.1, float(S_max_limit or 0.1))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:10145–10147` | `S·max` | `max(0.0, (a * (1.0 - A * B) - Rw * F * l_side - S_guess * l_front) * (1.0 - C))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:10221` | `K·max` | `max(list(final_cut.geoms), key=lambda g: g.area)` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:10443` | `K·max` | `max(cand_ok, key=lambda x: float(x.get('a 面積(㎡)', 0.0) or 0.0))` | **A** | **同歸戶合併之標的宗選定**（碼內註解逐字「多筆：找主要暫編地號（面積最大者，優先 G ≥ 最小分配面積）」）；輸入 `cand_ok`／`rows`／鍵 `a 面積(㎡)` 最大／消費端 `primary` ← 其餘宗併入。🔒 受詞係**標的宗**、⛔ 選塊 ⇒ 與 `wf_f0:218/:222` 同族，**五級⛔ 適用** |
| `app.py:10446` | `K·max` | `max(rows, key=lambda x: float(x.get('a 面積(㎡)', 0.0) or 0.0))` | **A** | **同歸戶合併之標的宗選定**（碼內註解逐字「多筆：找主要暫編地號（面積最大者，優先 G ≥ 最小分配面積）」）；輸入 `cand_ok`／`rows`／鍵 `a 面積(㎡)` 最大／消費端 `primary` ← 其餘宗併入。🔒 受詞係**標的宗**、⛔ 選塊 ⇒ 與 `wf_f0:218/:222` 同族，**五級⛔ 適用** |
| `app.py:10550` | `S·max` | `max(_CR_EPS_LEGAL, min(_CR_EPS_K * float(dxf_quantum), _CR_EPS_LEGAL_CEIL))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:10550` | `S·min` | `min(_CR_EPS_K * float(dxf_quantum), _CR_EPS_LEGAL_CEIL)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:10618–10619` | `K·min` | `min(pieces.geoms, key=lambda g: g.centroid.distance(_Pv2(side_mid)))` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:10756` | `K·max` | `max(_cands, key=_dep)` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:10784` | `S·min` | `min(_dep(P_block), _dep(Q))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11036` | `S·max` | `max(0.0, m * t_star)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11037` | `S·min` | `min(_W(0.0, t_star), _W(_D_at, t_star))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11244` | `S·min` | `min(_dPb, _dQq)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11254` | `N·sorted` | `sorted(r['t'] for r in _l2_ok)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11267` | `S·min` | `min(_W(_l2['d_top'], t_star), _W(_l2['d_bot'], t_star))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11275` | `N·sorted` | `sorted({round(_v, 12) for _tag, _j, _v in _l2_sw})` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11300` | `S·min` | `min(_W(0.0, 0.0), _W(_Db, 0.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11435` | `N·sorted` | `sorted(_by_gid.keys())` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11436` | `N·sorted` | `sorted(_by_gid[_gid])` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11455` | `N·sorted` | `sorted(_adj[_u])` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11459` | `N·sorted` | `sorted(_comp)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11460` | `K·sort` | `_out.sort(key=lambda c: c[0])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:11630` | `N·sorted` | `sorted(_idx_by_blk)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11675` | `N·sorted` | `sorted(str(_m.get("暫編地號", "")) for _m in _mem)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11701` | `E·min` | `min(_m["_k6_src_index"] for _m in _mem)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:11715` | `N·sorted` | `sorted(str(_m.get("暫編地號", "")) for _m in _mem)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:11851` | `S·max` | `max(1e-12, q.area * 1e-12)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:11929–11931` | `N·sorted` | `sorted({round(_a % 180.0, 9) for _a in _rect_fit_edge_angles_deg(poly)} \| {round(_i * _st % 180.0, 9) for _i in range` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:12037` | `S·min` | `min(_hi, _t)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:12039` | `S·max` | `max(_lo, _t)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:12404` | `K·sort` | `_cv.sort(key=_d_front)` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:12443` | `S·max` | `max(_seg_P0Ps * _sin_t, T)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:12519` | `K·min` | `min(pieces, key=lambda g: g.distance(_anchor))` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:13039` | `S·max` | `max(float(cand.get('_corner_cut_den', 0) or 0), 1e-9)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13041` | `S·max` | `max(float(cand.get('_side_line_den', 0) or 0), 1e-9)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13043` | `S·max` | `max(float(cand.get('_corner_range_area', 0) or 0), 1e-9)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13045` | `S·min` | `min(_cc_len / _cc_den, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13046` | `S·min` | `min(_sl_len / _sl_den, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13047` | `S·min` | `min(_tj_inter / _tj_range, 1.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13063–13066` | `K·sorted` | `sorted( group, key=lambda c: (-round(float(c.get('priority_index', 0)), 4), float(c.get('_pre_position_rank', float('i` | **D（選序·受詞＝街角 PK 名次）** | `指數名次` 之賦予；鍵 `(-指數 4dp, _pre_position_rank)`（碼內註解逐字「平手鍵與下方 `qualified.sort` 同源」） |
| `app.py:13079–13082` | `K·sort` | `qualified.sort(key=lambda c: ( -round(float(c.get('priority_index', 0)), 4), # 1: 手冊優先權指數（4dp 判平手） float(c.get('_pre_p` | **D（選序·受詞＝街角 winner）** | 🔴 街角 PK **winner 之決定**（同鍵）——**有土地後果**，惟受詞係街角優先權、⛔ 調配選塊 |
| `app.py:13153` | `K·sort` | `_rows.sort(key=lambda r: (r['名次'], -r['街角試算G(㎡)'], -r['指數數值'], r['暫編地號']))` | **B** | 報表／UI 之顯示序（時序、缺口率、最終序位、群組、地號） |
| `app.py:13271` | `N·sorted` | `sorted(set(_by[_P1]) & set(_by[_P2]))` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:13549` | `K·min` | `min(candidates, key=lambda c: c['d_to_vc'])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:13747` | `S·max` | `max(0.1, _s_max)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13815` | `S·max` | `max(0.0, min(0.95, burden))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13815` | `S·min` | `min(0.95, burden)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13888` | `S·max` | `max(road_area_m2, 1e-6)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13896` | `S·max` | `max(float(s.get('left', 0.0) or 0.0), 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:13897` | `S·max` | `max(float(s.get('right', 0.0) or 0.0), 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14032` | `S·max` | `max(0.0, float(public_owned_supply_m2 or 0.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14033` | `S·max` | `max(0.0, float(offset_land_supply_m2 or 0.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14034` | `S·max` | `max(0.0, float(public_land_area_m2 or 0.0))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14037` | `S·min` | `min(needed, public_supply)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14040` | `S·min` | `min(needed, offset_supply)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14545` | `N·sorted` | `sorted(led)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:14812` | `S·max` | `max(0, atp - lv)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:14813` | `S·min` | `min(age, el)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:15869` | `S·max` | `max(1.0, total_area_t5 * 0.02)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16042` | `S·max` | `max(0, int(total_years) - 1)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16059` | `S·min` | `min(required_land_area * 1.05, float(total_buildable_fin))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16088` | `S·max` | `max(1, int(n))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16097` | `S·max` | `max(0.0, 1.0 - ((i - mid) / max(mid, 1)) ** 2)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16097` | `S·max` | `max(mid, 1)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16106` | `E·max` | `max(raw)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:16112` | `S·max` | `max(1, int(n))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:16236` | `S·min` | `min(0, beginning_balance)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:17119` | `T·sort` | `own_fp_parts.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:17136` | `T·sort` | `mort_fp_parts.sort()` | **C** | 原地自然序 `xs.sort()`，供其後之比較或串接 |
| `app.py:17309` | `K·sorted` | `sorted(fp_to_group.items(), key=lambda x: x[1])` | **B** | 報表／UI 之顯示序（時序、缺口率、最終序位、群組、地號） |
| `app.py:17374` | `N·sorted` | `sorted(_all_codes)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:17417` | `N·sorted` | `sorted(edited_df7["歸戶群組"].unique())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:17431` | `N·sorted` | `sorted(_blk_area.items())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:18098` | `K·sort` | `_hits.sort(key=lambda x: -x[1])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:18345–18348` | `N·sorted` | `sorted( {str(tp.get('暫編地號', '') or '') for tp in temp_parcels if tp.get('暫編地號')} )` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:19077–19078` | `N·sorted` | `sorted({tp['原地號'] for tp in temp_parcels if not tp.get('_is_ghost_sliver', False)})` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:19545` | `S·max` | `max(public_common_total - offset_area - sb['special_total'], 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:19784` | `E·min` | `min(_valid_mins)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:19792–19794` | `K·min` | `min(((k, v) for k, v in _min_alloc_area_by_blk.items() if v is not None and v > 0), key=lambda kv: kv[1])` | **C** | `min(..., key=kv[1])`＝取 `MinA_區` 之來源塊，供顯示與診斷 |
| `app.py:19851–19853` | `N·sorted` | `sorted({int(tc['cutoff_idx']) for tc in (_gr_a.get('theoretical_corners') or []) if tc.get('cutoff_idx') is not None})` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:19859–19860` | `N·sorted` | `sorted({ci for _s in ('left', 'right') for ci in ((_topo_a['sides'].get(_s) or {}).get('chamfer_idxs') or [])})` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:20009` | `K·min` | `min(_k92_rows, key=lambda r: r['margin'])` | **C** | 內部候選之決定性排序或取極；受詞皆⛔ 為街廓分配 |
| `app.py:20153` | `E·max` | `max((c['臨正街長度_m'] for c in _candidates), default=1.0)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:20154` | `E·max` | `max((c['臨側街長度_m'] for c in _candidates), default=1.0)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:20155` | `E·max` | `max((c['跨占街角面積_m2'] for c in _candidates), default=1.0)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:20285` | `N·sorted` | `sorted(_k6b_lk_set)` | **C** | 集合／字典之**決定性列舉**（自然序），各元素之處理彼此獨立 |
| `app.py:20320` | `S·max` | `max(float(_dc.get('_corner_range_area', 0) or 0), 1e-9)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:20561` | `N·sorted` | `sorted(_cr_areas_ui.keys())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:21245` | `S·max` | `max(-1.0, min(1.0, _cosaf))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:21245` | `S·min` | `min(1.0, _cosaf)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:21299` | `K·sort` | `ordered_v2.sort(key=lambda e: (not e['is_corner_winner'],))` | **D（選序·受詞＝原位次重排）** | 🔴 `ordered_v2.sort(key=(not is_corner_winner,))`＝街角 winner 置前之**原位次重排**——**有土地後果**，惟⛔ 選塊 |
| `app.py:21577` | `S·max` | `max(0.1, S_block_max - left_cum_S - right_cum_S)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:21659` | `S·max` | `max(0.1, actual_max_proj - left_cum_S - right_cum_S)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:21676` | `S·max` | `max(0.1, S_remain - _adj)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:21930` | `S·min` | `min(50.0, blk_area * 0.05)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:22065` | `S·max` | `max(0.0, min(0.95, _burden_for_orphan))` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:22065` | `S·min` | `min(0.95, _burden_for_orphan)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:22157–22158` | `K·max` | `max(_offs, key=lambda r: float(r.get('幾何面積(㎡)', 0) or 0))` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:22202–22204` | `K·max` | `max( _merged.geoms, key=lambda g: g.area )` | **C** | 幾何多片取一（面積／長度／距離最極者）——受詞＝**幾何片**，⛔ 街廓分配 |
| `app.py:22357` | `N·sorted` | `sorted(_diag.items())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22427` | `N·sorted` | `sorted(_wd2_diag)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22435` | `N·sorted` | `sorted(_wd2_diag)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22473` | `N·sorted` | `sorted(_br)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22492` | `N·sorted` | `sorted(_sides)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22496` | `E·max` | `max(float(x.get('W(m)', 0) or 0) for x in lst)` | **D** | **聚合取極值**：`min`／`max` 之單一可迭代引數且⛔ `key=` ⇒ 產出**一個量**（範圍／門檻／殘差上界），**⛔ 候選之排序** |
| `app.py:22537` | `N·sorted` | `sorted(_dep)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22567` | `N·sorted` | `sorted(_fo_on.items())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22622` | `N·sorted` | `sorted(_blk_poly_dg.items())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22664` | `N·sorted` | `sorted(_fo_dg.items())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:22997` | `S·max` | `max(_info['min_width'] * _alloc_depth_w1 - _cutoff_w1, 0.0)` | **D** | **純量夾擠／邊界裁切**：`min`／`max` 且**位置引數 ≥ 2** 且⛔ `key=` ⇒ 其受詞為**一個數值之上下界**、**⛔ 一組候選之序**（機械判準·逐站列出） |
| `app.py:23391` | `N·sorted` | `sorted(_own_groups.keys())` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |
| `app.py:23521` | `K·sort` | `_gid_lands.sort(key=lambda x: x[1])` | **B** | 報表／UI 之顯示序（時序、缺口率、最終序位、群組、地號） |
| `app.py:23652` | `N·sorted` | `sorted(_gid_parcel_set)` | **B** | 圖層名／Excel／UI 下拉／診斷表／結構閘訊息之列舉與顯示序 |

---

## §五　工項三：五級實作依賴序之入典（`GB` 簿）✅

| 項 | 值 |
|---|---|
| 受詞 | `docs/reports/W-G.4_泛用阻塞項登記表.md`（**純末端追加**·上文一字未改）|
| payload 來源 | 本單**第 `179`–`213` 列**（四反引號圍欄在 `178`／`214`）|
| 追加量 | **2356** B／**38** LF／**CR 0** |
| 改前 | 656210 B・4693 LF・`sha256 0ae6e5fd3365798ea924f2a7e63990c8d04e5ffa4988f0c9af213d7a7e229aec` |
| 改後 | 658566 B・4731 LF・`sha256 3c6e734e42fcd31b33472ebf1e6606d5314cd8c8973bd8fa5001ed0793ac5258` |
| `numstat` | **`38 / 0`** ⇒ `deletions ＝ 0` ✅ |

**字樣錨（改前／改後）**——🛑 **單 `§四 c` 未指名該錨**，本報告取新節之二個唯一字樣代之並具名此事：

| 字樣 | 改前 | 改後 | 判 |
|---|---|---|---|
| `五級實作之依賴序`（節題）| **0** | **1** | ✅ 恰增 1 |
| `得以替代證據放行`（KL 裁之關鍵句）| **0** | **1** | ✅ 恰增 1 |

🔒 **`GB` 號零污染**（新節逐字自載「⛔ 鑄 `GB` 號」）：
標題錨定框 `` ^#{2,4} `?GB-N`? `` ⇒ `MAX` **150 → 150**、命中 **67 → 67**；
寬框 `` ^#+ .*?GB-N `` ⇒ `MAX` **150 → 150**、命中 **149 → 149** ⇒ **二框皆不動** ✅。
🛑 **`GB` 之相異／缺號集⛔ 出艙**（`CLAUDE.md` 字樣錨「在其釘定前，⛔ 得出艙」）。

🔒 **入典之要旨**（逐字見該節）：KL 所裁之序 `1 K-9-1 → 2 區外道路清單 → 3 seam 抽出 → 4 五級實作 → 5 GB-67／telescoping → 6 事後協調重算`；
`1`／`2` 在前之技術事實 ＝ `r2`／`r3` 係詞典序第 `2`／`3` 鍵、**支配 `r4`–`r8`**；
`5` 得後推之新款 ＝ **五級實作得以替代證據放行**，其代價逐字載明（⛔ 得用 `R4`／`R5`／`R6` 逐值迴歸）。

---

## §六　工項四：自誤 `293`／`294` ✅

### `a`　末號之獨立復算（⛔ 採單所載）

🔒 框 ＝ `VR-091` 補款二 `①` 之正字定義框 `A` **＋ 範圍框**（範圍框之二端**已展開**併入相異集）。
🔒 三軸：來源 改前 `blob@cb4b82f`／改後 本批工作區；母體 自誤簿**單檔**；粒度框 **列框**。

| 量 | 改前（自算）| 單所載 | 改後（自算）|
|---|---|---|---|
| 一 定義框列命中 | **286** | —— | **288** |
| 二 重咬列 | **3**（`:3338`／`:3373`／`:3403`）| —— | **3** |
| 三 純單筆列命中 | **283** | —— | **285** |
| 範圍框條數 | **8** | —— | **8** |
| 相異 | **285** | **285** ✅ | **287** |
| `MIN` | **7** | **7** ✅ | **7** |
| `MAX` | **292** | **292** ✅ | **294** |
| 缺號清單 | **`[106]`** | **`[106]`** ✅ | **`[106]`** |
| 恆等式 `MAX−MIN+1−缺號數 == 相異` | **True** | **True** ✅ | **True** |

⇒ **`N` ＝ `293`、`N+1` ＝ `294`**（與單相符）。

### `b`　鑄號之形（依 `常規四（九）四`·⛔ 自創形）

既有最末一則之標題形 ＝ `## 自誤 \`292\`　**…**` ⇒ 本批二則採同形：

```
## 自誤 `293`　**以鬆框之數出艙為號占用之判準**
## 自誤 `294`　**斷言正典「不存在」而未窮查**
```

🔒 與單 `§五` 之 `### \`自誤 N\`｜…` 之三處差（`###`→`##`／號入反引號之位置／`｜`→全形空白）
**皆係 `常規四（九）四` 所令之範本化**，⛔ 裁量。
🔒 **內文逐字未改**（機驗：`自誤 N` 佔位符於二則內文之出現數 **皆 ＝ 0**·assert 通過）。

### `c`　鑄號收工閘（單 `§五` 所定三項）

| 項 | 判準 | 實測 | 判 |
|---|---|---|---|
| ① | `MAX` 自 `292` → `294` | `292` → **`294`** | ✅ |
| ② | 缺號恆 `[106]` | `[106]` → **`[106]`** | ✅ |
| ③-1 | 盲區（`> MAX` 之落號）`= 0` | **0**（改前改後皆然）| ✅ |
| ③-2 | 併報 `GB` 簿零污染 | `GB` `MAX` **150 → 150**、二框命中皆不動 | ✅ |

🛑 **③-2 之逐字更正（事實·⛔ 條文）**：單 `§五` 收工閘 `③` 作「併報 `GB` 簿本批**未動**（零污染）」，
惟本單 `§四`（工項三）**明令追加於 `GB` 簿末端** ⇒ **該簿本批確有異動**（`38 / 0`）。
本報告依其**可成立之受詞**行之：所報者為 **`GB` 之號（`MAX` 與二框命中）零污染**，
**⛔ 該簿未被異動**。二者⛔ 互代。

🔒 **另二機檢**：定義框 `A` 之**盲區探針**（`#+` 與「自誤」間之前綴文字非空者）改前改後**皆 `0`**
⇒ `VR-091` 補款二 `④` 之**復審條件未觸發**；`293`／`294` 於改後命中集**皆 present** ✅。

### `d`　落地量

改前 575553 B・6618 LF ／ `293` 追加 **1450** B・**23** LF ／ `294` 追加 **1447** B・**23** LF ／
改後 **578450** B・**6664** LF・**CR 0**・`sha256 677d73cb87bf0fa9b999c56bc998e3554294fc15fb8122ffd6995f67d8fe5be3`；
`numstat` **`46 / 0`** ⇒ `deletions ＝ 0` ✅。

---

## §七　閘之總表

| 閘 | 判準 | 實測 | 判 |
|---|---|---|---|
| `S-0` | 最末 `SELF_SHA256` 逐位相符 | 宣告 ＝ 實算 `b1181a93…` | ✅ |
| `S-1` | 宣告框 ＋ 兩造對照組 | `242` `1/1`・`2/8`／`243` `0/0`／人造號 `0/0`；🔴 甲 `241` 宣告框列數與單相異（`3/4` vs 單載 `3/10`）| ✅（其角色判準仍成立）|
| `S-1′` | 落點**恰為**該一列 | `docs/orders/W-G.9-241_…:4`·款 `D3`-本單同列 | ✅ |
| `S-2` | append-only | 三既有檔 `deletions` 全 `0` | ✅ |
| **閘 `P`** | 生產碼五檔 `sha256` **前後各報一次** | 前後皆與單所載前 16 位逐一相符（見下）| ✅ |
| ⛔ 新增生產碼檔 | `app.py`／`verify/**` 之 diff 須空 | `git diff --numstat -- app.py verify/` **空** | ✅ |
| `deletions` | append-only ＝ `0` | `30/0`・`38/0`・`46/0`；新檔二張（本單、本報告）亦 `0` | ✅ |
| 五點必中 | 單 `§三 b` 之五點 | **5/5** 全捕 | ✅ |
| 掃描器對照組 | 兩造（四款節點命中／`plain_call` 未咬）| **GREEN** | ✅ |
| 對照組判別力 | 列框之數非零且 `≠` AST | `165` ≠ `367`，且 `165 > 0` | ✅ |
| 完備性檢查 | 各 (檔,樣式) 表列數 ＝ 獨立計數 | **GREEN**（`367/367` 皆得角色與理由）| ✅ |
| 鑄號收工閘 | 單 `§五` ①②③ | 四格全綠（③ 之受詞已更正）| ✅ |
| ⛔ 執行 harness | 本批⛔ 跑 `run_all`／`run_verification` | **未跑**（`verify/out/` 未新增任何檔·倉態僅三處文件追加）| ✅ |
| 掃描器⛔ 入倉 | 置於倉外 | `C:/Users/admin/AppData/Local/Temp/w240t/`（`git status` 無其蹤）| ✅ |

**閘 `P` 之五值（前後相同·與單所載前 16 位逐一相符）**

| 檔 | B | `sha256` | 單所載前 16 位 |
|---|---|---|---|
| `app.py` | 1417946 | `e3e464ea2493d0461b629941280c55238633cc57573d0837363d60eb3c85b7ca` | `e3e464ea2493d046` ✅ |
| `verify/selection_pipeline.py` | 35367 | `6c6783420dbc635c4c6b6eee1f1cab7054cc281a9733fd10e35dae41c8f25cbc` | `6c6783420dbc635c` ✅ |
| `verify/run_verification.py` | 96923 | `e48f24c84079f3652606bdf8fb7333964bca8cceee976533afd511964dffbebd` | `e48f24c84079f365` ✅ |
| `verify/stepg_pipeline.py` | 96261 | `0260273350021311c7ba81821fc4bc66aace6ba84d31166f3645ceb4ec6601a5` | `0260273350021311` ✅ |
| `verify/run_all.py` | 24681 | `4ba89fef909794910e5705af3880e0e9ca87208f663ad4c56f16e558936ebfcf` | `4ba89fef90979491` ✅ |

---

## §八　🔴 上呈（**⛔ 由 CC 自裁**）

1. **`S-1` 對照組甲之數不符**（單載 `W-G.9-241` 宣告框 `3／10`，實測 `3／4`；其鬆框 `3／10` 相符）
   ——疑係抄錄時把鬆框列數填入宣告框欄。**其角色判準仍成立、⛔ 觸停機**，惟該表係下游取號之引錨。
2. **單 `§五` 收工閘 `③` 之受詞不能成立**：其令「併報 `GB` 簿本批**未動**」，
   而同單 `§四` 明令追加於 `GB` 簿 ⇒ 二者相斥。本報告改報**`GB` 之號零污染**並具名此更正。
3. **`列框 ∖ AST` ＝ `21` 非空**（單載「若非空即紅」）：本報告已**逐列具名並判其成因**
   ——`19` 列級字面（註解／docstring／字串常量／dict 欄值）＋ `2` 列註解內引述舊寫法，
   **皆⛔ 為呼叫節點**。**是否據此把「級字面」自對照組之定義中剔除 ＝ 意思決定。**
4. **`verify/wf_f4.py:798` 二框皆不取**（既⛔ 在列框、亦⛔ 在 AST）
   ——其為 `_level` 之**輸出欄**消費點。**是否於 AST 框外另設「級之消費點」之框 ＝ 意思決定。**
5. **AST 之界（`§三 f` 已標旗·本批復現）**：AST 只抓**靜態**表達。
   本批之 `A` 列中，`verify/wf_f0.py:218`／`:222` 之鍵係 `key=_key`（**具名函式**，其定義在 `:209`–`:210`），
   AST 取得之 `key` 實參原文為 `_key` **三字**、⛔ 其比較內容 ⇒ **仍賴人判**。
   **是否擴及「具名 key 函式之定義展開」＝ 意思決定。**
6. **角色 `A` 之 `19` 站中，五級之射程仍只及三站**（`wf_f4.py:488` ＋ 連帶之 `:662`／`:689`）：
   `wf_f0:218/:222`、`app.py:10443/:10446` 屬**標的宗選定**（同街廓合併）；
   `wf_f4:1170/:1228` 屬 **§7-5 第2梯**；`wf_f2:85/:86`、`wf_f4:376/:377` 屬 F.2／E0 之目標塊宗選定；
   `wf_f4:433`／`:512`／`:663`／`:703` 為距離鏈之起算點、½ 線與分攤剔除。
   此係**事實對照**、⛔ 修法建議（單 `§三` ⛔ 令本批提修法）。

---

## §九　⛔ 未辦（單之明文）

- **⛔ 抽 seam**（順延為次一單·生產碼·須 KL 逐 commit 放行）——本批 `app.py`／`verify/**.py` **一字未動、亦⛔ 新增任何檔**。
- **⛔ 執行 `verify/run_all.py`／`run_verification.py`**——本批未跑（`verify/out/` 無新增）。
- **⛔ 將掃描器入倉**——其置於倉外，入倉者只有本報告之輸出表。
- **⛔ 於本單實作依賴序之任一項**（`K-9-1` UI 欄／區外道路清單／seam／五級／`GB-67`·telescoping／事後協調重算）。
- **⛔ 回改** `入倉前之號占用閘`／`號占用閘之母體`／`號占用閘之框改宣告框` 三節任一字（`D1`／`D2`／`②`／`③`／`④` 一字未動）。
