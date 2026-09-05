# W-G.9-241R　排序準據 seam 之**偵察** ＋ 交接文 `§七` 該列之更正 ＋ 自誤 `292`　執行報告

> **零生產碼**。`app.py`／`verify/**.py` **一字未動**（閘 `P` 逐位給證·§六）。
> **⛔ 抽 seam**（抽 seam 為 `W-G.9-242`）；**⛔ 於本報告提出修法建議**——偵察歸偵察。
> 🔒 一切數字**當場現查於倉**，⛔ 採單所載之值；與單相異者逐項具名。

---

## §零　態錨與工作副本

| 項 | 值（現查於 `2026-09-06`）|
|---|---|
| 開工態 `origin/wip/s1-endpart` | `09d1deda3b41e64272a9b0ca24df3d53d116a100`（`ls-remote` 現查）|
| 施工副本 | 短路徑拋棄式 clone `C:/Users/admin/AppData/Local/Temp/w240`（`core.autocrlf=false`）|
| 本報告產出時之 clone `HEAD` | `b4ca330`（＝ `09d1ded` ＋ 工項零）|
| `app.py` blob | `02cc6d7313789149ba852f997d2d8051a6cefaa0`（與 `-239` 交接文 `§一` 逐位相符）|
| 🔴 本 session 之 project dir | **舊態 worktree**（`6cb77b7`·`left-right` `1 614`）⇒ 一切規則依據以 `git show <rev>:<path>` 取得，⛔ 讀工作區 |

---

## §一　開工閘

### `S-0`（單之完整性）✅ **綠**

| 項 | 值 |
|---|---|
| `SELF_SHA256` 列命中 | **1**（取最末一個）|
| payload | **9221** B（全檔 **9299** B・**187** LF・**CR 0**）|
| 宣告 ＝ 實算 | `7fb2848757369ca6652dbe5992e519cf4d6c37f22bac7f7e01e20d076ed71b10` ⇒ **逐位相符** |

### `S-1`（號占用·宣告框）✅ **三列逐位復現單所載值**

🔒 **三軸**：來源 `blob@09d1deda3b41e64272a9b0ca24df3d53d116a100`／
母體 **全 `docs/` 556 檔**（其中 **19** 檔為 `.png`／`.jpg` 二進位而讀不到，檔名皆⛔ 含單號）／
粒度框 **檔框 ＋ 列框**。母體取法 ＝ `git ls-tree -r -z --name-only`（**⛔ `ls-files --with-tree`**）；
逐檔以 `git cat-file --batch` 取**倉側 blob**（`GB-139 ②`）。

| 號 | 宣告框 檔／列 | 鬆框 檔／列 | 單所載 | 判 |
|---|---|---|---|---|
| **`W-G.9-241`** | **0**／**0** | **0**／**0** | `0/0`・`0/0` | ✅ **未占用**·相符 |
| `W-G.9-240` | **4**／**7** | **4**／**20** | `4/7`・`4/20` | ✅ 對照組 甲（`≥ 1`）·相符 |
| `W-G.9-242` | **0**／**0** | **0**／**0** | `0/0`・`0/0` | ✅ 對照組 乙（次號）·相符 |
| 人造號（**代稱**·字樣⛔ 入倉·`GB-147`）| **0**／**0** | **0**／**0** | —— | ✅ 器須紅之造 |

### `S-2`（append-only）✅

既有二檔皆**純末端追加**，上文一字未改 ⇒ `deletions` 全 **`0`**（§六）。

---

## §二　工項零：本單原封入倉 ✅

| 檔 | B | LF | CR | 落檔 `sha256` | 入倉 blob | 判 |
|---|---|---|---|---|---|---|
| `docs/orders/W-G.9-241_排序準據seam偵察與交接文更正.md` | 9299 | 187 | 0 | `3a2df78fa7dcfb93…` | `204e0c52…`／內容 `sha256` 同左 | ✅ 逐位相同 |

🛑 該 `sha256` 閘只證「落檔→入倉」，**⛔ 證「聊天原文→落檔」**。

---

## §三　工項一：seam 偵察

### `a`　單 `§二 a` 之復現 ✅ **四列計數與四錨逐字全數相符**

🔒 **三軸**：來源 `blob@b4ca330`（`verify/**.py`／`app.py` 與 `09d1ded` 逐位相同·閘 `P` 給證）／
母體 各該單檔／粒度框 **列框**（`grep -c` 語意＝含該字面之列數）。

| 字樣 | `wf_f0` | `wf_f2` | `wf_f4` | 單所載 | 判 | （併載 `app.py`）|
|---|---|---|---|---|---|---|
| `級1` | **1** | **3** | **13** | `1`／`3`／`13` | ✅ | **0** |
| `相鄰` | **1** | **4** | **4** | `1`／`4`／`4` | ✅ | **71** |
| `鄰近` | **0** | **3** | **2** | `0`／`3`／`2` | ✅ | **3** |
| `sorted(` | **11** | **6** | **39** | `11`／`6`／`39` | ✅ | **58** |

**四錨逐字復現**（`git cat-file blob` 側）

| 落點 | 逐字 | 判 |
|---|---|---|
| `verify/wf_f2.py:99` | `"""§2 相鄰：共享 BLOCK 邊(<0.5m) 或 隔單一 RD 相望。回傳 set of frozenset({a,b})。"""` | ✅ 相符 |
| `verify/wf_f2.py:161`／`:163`／`:165` | `lvl = "級1相鄰"`／`lvl = "級2鄰近"`／`lvl = "級3非鄰近"` | ✅ 相符 |
| `verify/wf_f4.py:487` | `LV = {0: "級1相鄰", 1: "級2鄰近", 2: "級3非鄰近"}` | ✅ 相符 |
| `verify/wf_f4.py:798` | `"級別": LV[_level(gid, blk)],` | ✅ 相符 |

### `b`　逐點偵察表

🔒 **母體**：`verify/wf_f0.py` ∪ `verify/wf_f2.py` ∪ `verify/wf_f4.py` ∪ `app.py`；
樣式 ＝ `sorted(` ／ `.sort(` ／ 級字面（`級1`／`級2`／`級3`）。
🔒 **可行性**：逐點總量 **168**（含同列重複計）⇒ **相異列 165** ⇒ **逐點可行**
（**⛔ 抽樣、⛔ 停機、⛔ 縮母體**）。
🔒 **完備性機檢**：各 (檔, 樣式) 之表列數 ＝ 獨立計得之列數（機器斷言 **GREEN**）；
且分類器斷言 **無漏判、無多判**（165/165）。

**角色分布**：`A` **12**／`B` **69**／`C` **72**／`D` **12**。
🔒 `D` 之中，凡**係選擇準據但受詞非「選塊」**者，其角色格逐字載明其受詞（⛔ 以裸 `D` 掩之）。

#### `A` 列之**輸入／鍵／消費端**（單所令之另載·12 列全載）

| 檔:列 | 輸入（何者被排）| 鍵（依何排）| 消費端（誰讀其結果）|
|---|---|---|---|
| `wf_f0.py:218` | `qual`＝同 `(gid,blk)` 格內**達標且非畸零**之宗 | `_key(r) = (-float(G), 暫編地號)`（:209–:210）| `decisions[].target` → `_transform` → **級0 集中合併**。🔒 受詞係**同街廓級0**，**五級⛔ 適用** |
| `wf_f0.py:222` | `lots`＝該格**全部**宗（無人達標時）| 同 `_key` | `decisions[].target` → **級0' 弱弱聯合**。🔒 **五級⛔ 適用** |
| `wf_f2.py:85` | `qual`＝該歸戶名下**有達標宗**之街廓 → 該街廓 `ΣG` | `max(sorted(qual), key=qual.get)`＝`ΣG` 最大；並列取**字典序**（碼內註解逐字「並列取字典序（決定性）」）| `_decide` 回傳 `tgt_blk` → `raw` → `inject`／`conv_rows`／`transfers` → F.2 變換 |
| `wf_f2.py:86` | `blks[tgt_blk]`＝目標街廓內該歸戶之全部宗 | `(-float(G(㎡)), 暫編地號)` | `tgt_row` → `inject[tgt_row[暫編地號]] += m1` → trunk C |
| `wf_f4.py:376` | `qual`＝E0 階段該歸戶之達標街廓 → `ΣG` | `max(sorted(qual), key=qual.get)` | `tb` → `tr` → `e0_pairs` → E0 併入 |
| `wf_f4.py:377` | `byg[gid][tb]`＝目標塊內該歸戶之宗 | `(-float(G(㎡)), 暫編地號)`（**鍵在續行** `:379`）| `tr` → `e0_pairs` → `conv_rows`／實際併入 |
| 🔴 **`wf_f4.py:488`** | `mina`＝**全部**可配街廓（其鍵集）| `(_level(gid,b), dists[(gid,b)], b)`；`_level`（`:483`–`:486`）＝`0` 若 `b` 與該歸戶錨點所在公設塊相鄰／否則 `1` 若 `dists ≤ med`／否則 `2` | `border[gid]` → `:674` `for blk in border[gid]` → 首個 `_usable` 者即 `pick` → `requests[pick]` → **實際配地**。🔒 **此即「級序 → 選塊」之唯一路徑** |
| `wf_f4.py:512` | `mina`＝全部可配街廓 | `(dists[(gid,b)], b)`——**⛔ 含 `_level`** | `near_any[gid]` → `:515` `_trial(...)` → `half_r0` → `comp_groups` → **½ 線判定（配地 vs 現金補償）** |
| 🔴 **`wf_f4.py:662`** | `alloc - spset`＝本輪尚有 `a_rem` 之歸戶 | `(min(dists[(g,b)] for b in mina), g)`＝**至最近可達塊之距**，tie 取 `gid` 字典序（**鍵在續行** `:663`；碼內註解逐字「純距離優先」）| `act` → `:672` `for gid in act` → 逐歸戶選塊 → `requests` |
| 🔴 **`wf_f4.py:689`** | `requests[blk]`＝本輪請求該塊之歸戶 | `(dists[(g,blk)], g)`（行末註解逐字「裁定K：距離優先」）| `gs` → `demG`／`shares` 同級比例分攤 → `:703` `gs.remove(max(small, key=(dists,g)))` 剔除**最遠者** |
| `wf_f4.py:1170` | `feas`＝通過容量約束之**全部**指派組合 | tuple 自然序 `(總增配金額 round2, Σ增配面積 round3, Σ質心起迄距 round2, combo)` | `canon_best = feas[0][0]` → 階段二 band 之下界 |
| `wf_f4.py:1228` | `actual`＝band 內以引擎實際 `G` 重評後之候選 | 同上 tuple 自然序 | `best = actual[0]` → `combo` → `assign` → **§7-5 第2梯之最終塊指派**。🔒 **五級⛔ 適用 §7-5**（`-240` 入典之 `⑤`）|

#### 🔒 二則**碼面事實**（逐字給證·⛔ 推論）

1. **`wf_f2` 之級係<u>事後標記</u>、⛔ 選擇準據。**
   `_decide`（`:76`–`:88`）**先**選定 `tgt_blk`／`tgt_row`；`lvl`（`:160`–`:165`）**其後**才算，
   且其唯一去處為 `conv_rows["級別"]`（`:173`）——`inject`／`remove2`／`transfers` **皆⛔ 讀 `lvl`**。
2. **`wf_f4` 之級<u>確為</u>選擇準據，惟其唯一注入點為 `:488` 之排序鍵。**
   `LV`（`:487`）僅係**顯示字面表**，唯一消費點 `:798` 為輸出欄；
   真正之準據係 `_level`（`:483`–`:486`），而 `_level` 進入決策之路徑**只有一條** ＝ `:488` 之 `key` 首鍵。

### `c`　🔴🔴 判別力之前置量測——**現態下級之命中筆數 ⛔ 可測**

🔒 **實測方式**：於**拋棄式 clone 內**跑 `python verify/run_verification.py`（⛔ 主 checkout）；
該支逐情境（退縮 `0m`／`3.5m`）呼叫 `wf_f0`→`wf_f2`→`wf_f3`→`wf_f4` 並傾印 `verify/out/got_F.2_*`／`got_F.4_*`。
🔒 **⛔ 引用 `wf_f2.py:20` docstring 之數**（單之明令）——下列全係**本批當場實跑**之結果。

**結果：`RESULT: FAIL`（`PASS` 10 ／ `FAIL` 24）；二情境皆於街廓 `R2` 中止，且<u>中止點相異</u>。**

| 情境 | 中止之閘 | 逐字（實跑訊息）|
|---|---|---|
| 退縮 `0m` | **`②-宗 圍堵閘` ＝ `GB-67`** | `[StepG0m] 街廓 R2 抵費地計算失敗：🔴 ②-宗 圍堵閘破[R2]：宗-宗重疊 = 45.9766 > 上界 2.8906（(宗數14−1)×0.005×深度44.47）——**超出捨入量子可解釋範圍＝另有病**，停` |
| 退縮 `3.5m` | **telescoping 結構閘** | `[StepG3.5m] 🔴 結構閘 telescoping 破：街廓 R2 left 側 ΣRw_實跑=100.02 ≠ R(W_final=34.39)−R(W₀=6.98)=44.41（Δ=55.606 >0.1）` |

**其連鎖（逐字）**：`[F.0] stepg_ctx[0m] 缺（trunk A 未成功？）` →
`[F.1] F.0 未成功，F.1 跳過（W5 守衛）` → `[F.2] F.0 未成功，F.2 跳過（存在性守衛）` →
`[F.3] F.2 未成功，F.3 跳過` → `[F.4] F.3 未成功，F.4 跳過` →
`[G.2] 上游世代未產出：['trunkA(_ctx)', 'F.0', 'F.1', 'F.2', 'F.3', 'F.4']（0m）`。
⇒ `verify/out/` 之 `got_F.2_*`／`got_F.4_*` **一檔未生成**（實測 `ls` 命中 **0**）。

🔒 **⇒ 單所問二題之答**

1. **「現行 UC9898 之各級實際命中筆數（`級1`／`級2`／`級3`），分退縮 `0` 與 `3.5` 二情境」
   ＝ 現態下<u>不可測</u>**——`wf_f2` 與 `wf_f4` **於二情境皆未執行**。
   🛑 **⛔ 讀為「命中 ＝ `0`」**：`0` 是「量到而為零」，本案是「**量不到**」，二者⛔ 同義
   （同 `W-G.9-14` 修法 `②`：「無從判定」⛔ 與「判定為可」共用出艙碼）。
2. 單之款 `2`（「**若**級2／級3 之命中確為 `0` ⇒ 逐字載明無鑑別力」）之**前提未成就**
   ——本批⛔ 確認其為 `0`，故**不作該逐字載明**。

🔒 **對 `W-G.9-242` 之意涵（事實陳述·⛔ 修法建議）**
> 單 `§二 c` 所慮者為「以 UC9898 輸出逐值不變為驗收 ⇒ 該綠**無鑑別力**」。
> **本測所得之情況較該慮更前一步**：現態下 UC9898 於 `F.2`／`F.4` **⛔ 有任何輸出**
> ⇒ 「輸出逐值不變」此一驗收**⛔ 可執行**（非「可執行但無鑑別力」）。
> 🔒 其可行性因此**繫於**二結構閘（`0m` 之 `GB-67`／`3.5m` 之 telescoping）之處置，
> **而該二者係二事、各有其解除條件**（見 §四）。

🔒 **本測之判別力自證**：同一次實跑中 `PASS` **10** 列（含 `v3 財務錨 B == 0.171043`、
`C == 0.091319`、`C 兩形等價 |Δ|=2.92e-10`、`F.0-pre 15.73㎡ 歸因` 等）
⇒ 該 harness **非恆紅**、其 `FAIL` 有受詞。
🔒 **本測⛔ 動任何生產碼**：實跑前後閘 `P` 五檔 `sha256` 逐位相同（§六）；
`run_verification.py` 亦**未改寫任何已追蹤檔**（實跑後 `git status` 僅本批二處文件追加）。

### `d`　🔴 掃描母體之**三個洞**（事實登記·⛔ 條文·⛔ 由 CC 自裁）

單所定之掃描母體 ＝ `sorted(` ∪ `.sort(` ∪ 級字面。當場機檢，其**漏抓**三類：

**洞一　以 `max(…, key=)`／`min(…, key=)` 表達之排序準據**

| 檔:列 | 逐字 | 何以要害 |
|---|---|---|
| 🔴 `verify/wf_f4.py:433` | `anchor = max(lots, key=lambda x: (x["a"], x["pid"]))` | **歸戶錨點宗之選定** ⇒ `ginfo[gid]["anchor"]` ⇒ `dists` ⇒ **`:488`／`:512`／`:662`／`:689` 全部距離準據之<u>起算點</u>** |
| 🔴 `verify/wf_f4.py:703` | `gs.remove(max(small, key=lambda g: (dists[(g, blk)], g)))` | 同級比例分攤之**剔除準據**（剔最遠者）——`:689` 之對偶 |

🔒 **量之界**：`verify/` 三檔之 `EXTRA∖BASE` 且含 `key=` 者 ＝ **5** 列，
其中 **3** 列係續行（見洞二），**真漏 ＝ 2**（即上表）。
🛑 **`app.py` 之對應數⛔ 出艙為「排序準據」**：其 `key=` 命中 **216** 列而 `key=lambda` 僅 **48** 列
——`app.py` 之 `key=` 多為 **Streamlit widget 參數**，與比較子無關。
（三軸：來源 `blob@b4ca330`／母體 各該單檔／粒度框 列框。）

**洞二　多列呼叫之<u>鍵在續行</u>，列框會把「站點」與「其準據」拆開**

| 站點（在母體內）| 其鍵所在之列（⛔ 在母體內）|
|---|---|
| `verify/wf_f4.py:377` | `:379` `key=lambda x: (-float(x["G(㎡)"]), x["暫編地號"]))[0]` |
| `verify/wf_f4.py:662` | `:663` `key=lambda g: (min(dists[(g, b)] for b in mina), g))` |
| `verify/wf_f4.py:1346` | `:1347` `key=lambda x: float(x.get("累積S(m)", 0) or 0))` |

⇒ **逐點表之「逐字」欄若只截該列，讀者看不到鍵**；本報告已於各該列之判之依據欄具名其續行。

**洞三　🔴 本單 `§二 a` 之錨表，其 `4` 個錨中有 `2` 個⛔ 在本單自身所定之掃描母體內**

| 錨 | 在母體內？| 何以不在 |
|---|---|---|
| `verify/wf_f2.py:99` | 🔴 **否** | 該列含「相鄰」而**⛔ 含** `級1`／`級2`／`級3` 之字面，亦⛔ 含 `sorted(`／`.sort(` |
| `verify/wf_f2.py:161`（及 `:163`／`:165`）| ✅ 是 | —— |
| `verify/wf_f4.py:487` | ✅ 是 | —— |
| `verify/wf_f4.py:798` | 🔴 **否** | 該列作 `"級別": LV[_level(gid, blk)],`——「級別」二字**⛔ 等於**級字面 `級1/2/3` |

🛑 ⇒ **單之錨表與單之母體不自洽**；本報告**⛔ 把該二列塞進逐點表**（否則即偽稱母體完備），
改列本節，並於 `§三 b` 之二則碼面事實中逐字處置 `:798` 之角色（輸出欄）。
🛑 **母體是否應擴及 `max/min(key=)`、是否改以 AST（而非列框）為粒度 ＝ 意思決定 ⇒ 候發單側／KL。**

### `e`　逐點偵察表（**165** 列·全表）

| 檔:列 | 逐字 | 角色 | 判之依據 |
|---|---|---|---|
| `verify/wf_f0.py:135` | `ROUTE_OUT = {"G009": "轉F.2(同歸戶R4有達標宗·級1相鄰街廓)",` | **D** | `ROUTE_OUT` 之**字串字面**（轉出去向文案），⛔ 任何比較 |
| `verify/wf_f0.py:204` | `for (gid, blk), lots in sorted(cell.items()):` | **C** | `for (gid,blk),lots in sorted(cell.items())`：逐格處理，各格決策彼此獨立（`decisions.append`），序只定 `decisions` 之列序 |
| `verify/wf_f0.py:218` | `target = sorted(qual, key=_key)[0]` | **A** | 級0 標的宗選定：`sorted(qual,key=_key)[0]` |
| `verify/wf_f0.py:222` | `target = sorted(lots, key=_key)[0]` | **A** | 級0' 標的宗選定：`sorted(lots,key=_key)[0]` |
| `verify/wf_f0.py:228` | `"zones": sorted(zones),` | **B** | `"zones": sorted(zones)` 寫入 `decisions` 輸出欄 |
| `verify/wf_f0.py:284` | `_wconf = sorted(all_merged & win_set)` | **C** | 斷言用集合之決定性列舉（`_wconf`／`_uncov`），其值只進 `raise`／比對 |
| `verify/wf_f0.py:319` | `_uncov = sorted(set(GSA_EXPECT[tag]) - set(gsa))` | **C** | 斷言用集合之決定性列舉（`_wconf`／`_uncov`），其值只進 `raise`／比對 |
| `verify/wf_f0.py:338` | `f"則於 P-H 重錨（刪鍵或改值），否則係上游漏配之 bug。已評估鍵＝{sorted(gsa)}")` | **B** | `raise` 訊息內之 f-string |
| `verify/wf_f0.py:386` | `for k in sorted(fa \| fb):` | **C** | 集合／字典之決定性列舉（`fa|fb`／`所屬街廓` 集／`poolB`），各元素處理獨立 |
| `verify/wf_f0.py:403` | `blocks = sorted({r["所屬街廓"] for r in A.values()})` | **C** | 集合／字典之決定性列舉（`fa|fb`／`所屬街廓` 集／`poolB`），各元素處理獨立 |
| `verify/wf_f0.py:433` | `for lbl in sorted(poolB)]` | **C** | 集合／字典之決定性列舉（`fa|fb`／`所屬街廓` 集／`poolB`），各元素處理獨立 |
| `verify/wf_f0.py:443` | `"decisions": decisions, "removed": sorted(removed), "gsa": gsa,` | **B** | `"removed": sorted(removed)` 輸出欄 |
| `verify/wf_f2.py:3` | `W-F F.2 — 級1/2/3 跨街廓同歸戶合併（a′ 首次登場；claude.ai/KL 裁定 2026-07-11）。` | **D** | 模組 docstring |
| `verify/wf_f2.py:20` | `UC9898 七轉出全級1（相鄰）；級2/3 不現。` | **D** | 模組 docstring——**且係 §二 c 判別力測之受詞**（「UC9898 七轉出全級1；級2/3 不現」） |
| `verify/wf_f2.py:85` | `tgt_blk = max(sorted(qual), key=qual.get)               # 並列取字典序（決定性）` | **A** | F.2 目標**街廓**選定：`max(sorted(qual),key=qual.get)` |
| `verify/wf_f2.py:86` | `tgt_row = sorted(blks[tgt_blk], key=lambda r: (-float(r["G(㎡)"]), r["暫編地號"]))[0]` | **A** | F.2 目標**宗**選定：`sorted(blks[tgt_blk],key=(-G,暫編))[0]` |
| `verify/wf_f2.py:87` | `src_rows = [r for blk, rows in sorted(blks.items()) if blk not in qual for r in rows]` | **C** | `src_rows` 之列舉序：非達標塊之**全部**列皆取（⛔ 選擇），序只影響 `raw`／`conv_rows` 之列序；`inject[tgt]+=m1` 之累加為交換律（惟浮點捨入序技術上相依，實測不改 baseline） |
| `verify/wf_f2.py:161` | `lvl = "級1相鄰"` | **B** | 🔴 **級之指派係事後標記**：`_decide`（:85–:87）**已先**選定目標塊／宗，`lvl` 其後才算，且唯一去處為 `conv_rows["級別"]`（:173）——`inject`／`remove2`／`transfers` **皆⛔ 讀 `lvl`** ⇒ 於 `wf_f2` **級⛔ 為選擇準據** |
| `verify/wf_f2.py:163` | `lvl = "級2鄰近"` | **B** | 🔴 **級之指派係事後標記**：`_decide`（:85–:87）**已先**選定目標塊／宗，`lvl` 其後才算，且唯一去處為 `conv_rows["級別"]`（:173）——`inject`／`remove2`／`transfers` **皆⛔ 讀 `lvl`** ⇒ 於 `wf_f2` **級⛔ 為選擇準據** |
| `verify/wf_f2.py:165` | `lvl = "級3非鄰近"` | **B** | 🔴 **級之指派係事後標記**：`_decide`（:85–:87）**已先**選定目標塊／宗，`lvl` 其後才算，且唯一去處為 `conv_rows["級別"]`（:173）——`inject`／`remove2`／`transfers` **皆⛔ 讀 `lvl`** ⇒ 於 `wf_f2` **級⛔ 為選擇準據** |
| `verify/wf_f2.py:200` | `for l in sorted(poolC):` | **C** | `poolC`／`所屬街廓` 集之決定性列舉，各元素獨立成列 |
| `verify/wf_f2.py:250` | `for blk in sorted({r["所屬街廓"] for r in B.values()}):` | **C** | `poolC`／`所屬街廓` 集之決定性列舉，各元素獨立成列 |
| `verify/wf_f2.py:261` | `"transfers": len(conv_rows), "removed": sorted(remove2),` | **B** | `"removed": sorted(remove2)` 輸出欄 |
| `verify/wf_f4.py:5` | `母體＝trunk D（F.3 終態）。執行序**嚴守規格 §7 依賴鏈**：E0(7-1 級1 殘餘) → E1(7-4) → E2(7-5)` | **D** | 模組 docstring（執行序 E0→E1→E2 之說明） |
| `verify/wf_f4.py:362` | `# ══ E0：殘餘同歸戶級1 sweep（§7-1 級1＋裁示2；F.2 _decide 同規則） ══` | **D** | 區段註解（E0 段標） |
| `verify/wf_f4.py:368` | `for r in sorted(flagged, key=lambda x: x["暫編地號"]):` | **C** | E0 sweep 之處理序（`flagged` 按暫編地號）；各 `r` 之併入互不相依，其結果於 :396 另行排序後消費 |
| `verify/wf_f4.py:376` | `tb = max(sorted(qual), key=qual.get)` | **A** | E0 目標**街廓**選定：`max(sorted(qual),key=qual.get)` |
| `verify/wf_f4.py:377` | `tr = sorted([x for x in byg[gid][tb]` | **A** | E0 目標**宗**選定：`sorted([...])[0]`（鍵在**續行** :379） |
| `verify/wf_f4.py:388` | `if sorted(x[1]["暫編地號"] for x in e2_class) != sorted(E2_NAMED.values()):` | **C** | 二 `sorted` 之**相等比對**（第2梯類源宗 vs 具名錨），係斷言 |
| `verify/wf_f4.py:390` | `print(f"⚠️ [WV_BAKE·{tag}] 第2梯類源宗 ≠ 具名錨：{sorted(x[1]['暫編地號'] for x in e2_class)}")` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:392` | `raise RuntimeError(f"🔴 [{tag}] 第2梯類源宗 ≠ 具名錨：{sorted(x[1]['暫編地號'] for x in e2_class)}")` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:395` | `raise RuntimeError(f"🔴 [{tag}] E0 移除宗為街角 winner：{sorted(_rm0 & win_set)}")` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:396` | `for pid, (gid, r, tr) in sorted(e0_pairs.items()):` | **C** | `e0_pairs` 之決定性列舉，各對獨立成事件列 |
| `verify/wf_f4.py:403` | `events[gid].append(f"E0級1殘餘併入 {pid}→{tr['暫編地號']}")` | **B** | 事件文案／`conv_rows` 之「級別」「處置」欄（**字面**，⛔ 由 `_level` 計算） |
| `verify/wf_f4.py:404` | `conv_rows.append({"情境": tag, "段": "E0級1", "歸戶": gid, "源": pid,` | **B** | 事件文案／`conv_rows` 之「級別」「處置」欄（**字面**，⛔ 由 `_level` 計算） |
| `verify/wf_f4.py:406` | `"目標塊": tr["所屬街廓"], "級別": "級1(同歸戶)",` | **B** | 事件文案／`conv_rows` 之「級別」「處置」欄（**字面**，⛔ 由 `_level` 計算） |
| `verify/wf_f4.py:410` | `"a″引擎(㎡)": ap, "配額G(㎡)": "", "處置": "併入(§7-1級1)"})` | **B** | 事件文案／`conv_rows` 之「級別」「處置」欄（**字面**，⛔ 由 `_level` 計算） |
| `verify/wf_f4.py:441` | `"類集": sorted({x["類"] for x in lots if x["類"]})}` | **B** | `"類集": sorted(...)` 輸出欄 |
| `verify/wf_f4.py:452` | `_rd_bad = sorted(g for g, gi in ginfo.items()` | **C** | `_rd_bad` 斷言集之決定性列舉 |
| `verify/wf_f4.py:487` | `LV = {0: "級1相鄰", 1: "級2鄰近", 2: "級3非鄰近"}` | **B** | `LV` ＝ 級之**顯示字面表**；唯一消費點 :798 之輸出欄。**⛔ 準據本身**（準據為 `_level`，:483–:486） |
| `verify/wf_f4.py:488` | `border = {gid: sorted(mina, key=lambda b: (_level(gid, b), dists[(gid, b)], b))` | **A** | 🔴 **seam 主站**：每一歸戶之候選街廓**順序** |
| `verify/wf_f4.py:512` | `near_any = {gid: sorted(mina, key=lambda b: (dists[(gid, b)], b))[0] for gid in ginfo}` | **A** | ½ 輪0 之**最近塊**選定（鍵**⛔ 含級**，純距離） |
| `verify/wf_f4.py:514` | `for gid in sorted(ginfo):` | **C** | 群／塊／指派之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:523` | `print(f"⚠️ [WV_BAKE·{tag}] ½ 輪0 <½ 群 {sorted(comp_groups)} ≠ 具名錨 {sorted(COMP_EXPECT)}")` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:525` | `raise RuntimeError(f"🔴 [{tag}] ½ 輪0 <½ 群 {sorted(comp_groups)} ≠ 具名錨 "` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:526` | `f"{sorted(COMP_EXPECT)}——停查再定錨")` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:546` | `f"——既非公設用地(RD/PF/G)、其塊亦不在後街廓單價表 {sorted(post_price)}；"` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:549` | `for gid in sorted(comp_groups):` | **C** | 群／塊／指派之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:662` | `act = [g for g in sorted(alloc - spset,` | **A** | 🔴 **E1 歸戶處理序**（全域佇列）；鍵在**續行** :663 |
| `verify/wf_f4.py:688` | `for blk in sorted(requests):` | **C** | `for blk in sorted(requests)`：各塊之分攤彼此獨立（`_budget(blk)` 逐塊自算） |
| `verify/wf_f4.py:689` | `gs = sorted(requests[blk], key=lambda g: (dists[(g, blk)], g))   # 裁定K：距離優先` | **A** | 🔴 **同塊內歸戶之分攤序**（`# 裁定K：距離優先`） |
| `verify/wf_f4.py:776` | `f"{ {b: sorted(v) for b, v in _s2_left.items()} }——"` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:790` | `for (gid, blk), a2 in sorted(placed.items()):` | **C** | `placed` 之決定性列舉，供輸出列生成 |
| `verify/wf_f4.py:811` | `rm2 = sorted(x[1]["暫編地號"] for x in e2_class)` | **C** | `rm2` 斷言集 |
| `verify/wf_f4.py:813` | `raise RuntimeError(f"🔴 [{tag}] E2 移除宗為街角 winner：{sorted(set(rm2) & win_set)}")` | **B** | `print`／`raise` 訊息內之 f-string |
| `verify/wf_f4.py:857` | `for gid in sorted(alloc):` | **C** | 群／塊／指派之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:862` | `for (gid, blk), pid in sorted(syn_ids.items()):` | **C** | 群／塊／指派之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:873` | `for blk in sorted(per_blk):` | **C** | 群／塊／指派之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:977` | `for blk in sorted(mina):` | **C** | 群／塊／指派之決定性列舉，各元素獨立成列或成事件 |
| `verify/wf_f4.py:1012` | `for l in sorted(pool_final)]` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1014` | `"wavg": wavg, "comp_groups": sorted(comp_groups),` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1017` | `for g in sorted(comp_groups)},` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1020` | `"rounds": rounds, "spill_75": sorted({s[0] for s in spill_75}),` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1021` | `"pool_final": {l: round(v, 2) for l, v in sorted(pool_final.items())},` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1079` | `blocks = sorted(mina)` | **C** | `blocks = sorted(mina)` ＝ `itertools` 窮舉母體之列舉序（窮舉對序不敏感） |
| `verify/wf_f4.py:1169` | `for (g, b), v in sorted(cost.items())}}` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1170` | `feas.sort()` | **A** | §7-5 第2梯最佳化·**canonical 最優**：`feas.sort()` → `feas[0][0]` |
| `verify/wf_f4.py:1228` | `actual.sort()` | **A** | §7-5 第2梯最佳化·**終局指派**：`actual.sort()` → `best=actual[0]` → `assign` |
| `verify/wf_f4.py:1232` | `a_distinct = sorted({r[0] for r in actual})` | **C** | `a_distinct` ＝ tie 統計（`second`／`tie_ct`），供診斷 |
| `verify/wf_f4.py:1290` | `for (g, b), v in sorted(cost.items())}}` | **B** | 回傳 dict 之輸出欄（`pool_final`／`comp_groups`／`spill_75`／`cost_matrix`） |
| `verify/wf_f4.py:1346` | `grp = sorted([r for r in lots if r["推進側別"] == side],` | **D（選序·受詞＝同側宗之整形序）** | E3 楔形遞補整形：同側宗按 `累積S(m)` 升序（鍵在**續行** :1347）。**受詞為宗之整形序、⛔ 選塊** |
| `verify/wf_f4.py:1526` | `("E0級1", "E0級1"), ("E1 ½測試<½", "E1補償"), ("E1 7-4 配地", "E1配地"),` | **B** | 報表段名對照表／註解／鏈文案之**字面** |
| `verify/wf_f4.py:1535` | `#   梯0：F.0 同街廓併／F.2 跨併／逃生門(E2七五)／殘旗標宗 E0 級1／F.3 公設併入／全達標留置` | **B** | 報表段名對照表／註解／鏈文案之**字面** |
| `verify/wf_f4.py:1537` | `#   梯2：E2 增配(G004/G033)／E0 級1(G011)／F.3 併入達標(G032)` | **B** | 報表段名對照表／註解／鏈文案之**字面** |
| `verify/wf_f4.py:1541` | `("建地軌", "0"): {"F0併", "全達標", "F2跨併", "F3併入", "E0級1", "E2七五"},` | **B** | 報表段名對照表／註解／鏈文案之**字面** |
| `verify/wf_f4.py:1543` | `("建地軌", "2"): {"F3併入", "E0級1", "E2七五", "全達標"},` | **B** | 報表段名對照表／註解／鏈文案之**字面** |
| `verify/wf_f4.py:1563` | `chain[r["歸戶"]].append(f"F.2跨併級1 {r['源宗']}→{r['目標宗']}")` | **B** | 報表段名對照表／註解／鏈文案之**字面** |
| `app.py:86` | `result['data'].sort(key=lambda x: x['ym'])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:782` | `return {'polygons': [], 'outer_boundary': None, 'texts': texts, 'layer_names': sorted(set(rp['layer'] for rp in raw_po` | **B** | CAD 解析結果之 `layer_names`／`layers_found` 輸出欄 |
| `app.py:884` | `_parsed.sort(key=lambda x: -x[0])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:925` | `'layer_names': sorted(set(rp['layer'] for rp in raw_polys)),` | **B** | CAD 解析結果之 `layer_names`／`layers_found` 輸出欄 |
| `app.py:1441` | `_rk.sort(key=lambda x: (-x['overlap_m'], x['block']))   # 決定性：同分按塊名` | **C** | `_best_block` 之候選決定性排序（`-overlap_m, block`）——受詞＝**線↔街廓綁定**，⛔ 分配選塊 |
| `app.py:1678` | `_cands.sort(key=lambda c: (c['perp_m'], str(c['br'].get('handle', ''))))` | **C** | BASELINE／等價 handle 之決定性排序，受詞＝圖層配對 |
| `app.py:1726` | `_equiv_handles = sorted(str(c['br'].get('handle', '')) for c in _cands)` | **C** | BASELINE／等價 handle 之決定性排序，受詞＝圖層配對 |
| `app.py:1798` | `result['diagnostics']['layers_found'] = sorted(_layers_found)` | **B** | CAD 解析結果之 `layer_names`／`layers_found` 輸出欄 |
| `app.py:2150` | `for gid, agg in sorted(_per_group.items()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:2156` | `ws2.cell(row=row, column=2, value='、'.join(sorted(set(agg['parcels']))))` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:2599` | `uniq_zones = sorted({v for v in zones_map.values() if v})` | **B** | `uniq_zones` ＝ UI 下拉選單之顯示序 |
| `app.py:3104` | `uniq_zones = sorted({v for v in zones_map.values() if v})` | **B** | `uniq_zones` ＝ UI 下拉選單之顯示序 |
| `app.py:3310` | `rows_with_geom.sort(key=lambda x: x[0])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:3787` | `candidates.sort(key=lambda x: (x[0], x[1]))` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:4016` | `edges.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:4036` | `edges.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:4140` | `integrity_warnings.sort(key=lambda x: -x['缺口率_%'])` | **B** | `integrity_warnings` 之顯示序（按缺口率遞減） |
| `app.py:4951` | `remaining.sort(key=lambda x: -x[1])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:5042` | `mbr_edge_lens.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:5130` | `side_lengths.sort(key=lambda t: (t[0]['p1'][0] + t[0]['p2'][0]) / 2.0)` | **C** | 側邊按中點 x 排序，供左右判定之決定性 |
| `app.py:5373` | `_rows.sort(key=lambda r: str(r['block']))` | **B** | `_rows` 診斷表之顯示序 |
| `app.py:5930` | `s = sorted(seg, key=lambda q: q[0])` | **C** | 線段參數 `q[0]` 之決定性排序，幾何內部 |
| `app.py:6511` | `edges.sort(key=lambda e: -e[2])` | **C** | 邊／臂按長度或面積遞減之內部幾何選擇 |
| `app.py:6639` | `_stop(f"後緣邊於環上分裂為 **{_runs} 段**（邊索引 {sorted(_re)}／共 {_n_e} 邊）"` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:6642` | `_ridx = sorted(set(_re) \| {(_i + 1) % _n_e for _i in _re})` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:6643` | `_rear = sorted(((_ring[_i][1], _dep[_i], _ring[_i][0]) for _i in _ridx),` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:6913` | `f"（邊索引 {sorted(_fe_idx)}／共 {_n_e} 邊）。本宗於兩處分別觸及 FRONT_LINE"` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:6969` | `for _t in sorted(_ts):` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:7299` | `candidates.sort(key=lambda x: -x[1])` | **C** | 候選按值遞減之內部幾何選擇 |
| `app.py:7359` | `candidates.sort(key=lambda x: -x[1])` | **C** | 候選按值遞減之內部幾何選擇 |
| `app.py:7619` | `return sorted(parcels, key=_proj_of)` | **D（選序·受詞＝原位次投影序）** | `_projection_order` 本體：`sorted(parcels,key=_proj_of)`。係**位次序不變量之單一真相源**，⛔ 選塊準據 |
| `app.py:7813` | `sorted(set(_got) ^ set(_exp)), len(_got), _got, len(_exp), _exp))` | **B** | 結構閘之 `raise`／診斷訊息內容 |
| `app.py:7844` | `% (tag, blk, _side, sorted(_val)))` | **B** | 結構閘之 `raise`／診斷訊息內容 |
| `app.py:7847` | `_bad = sorted(x for x in _val if not x.startswith(_pfx))` | **B** | 結構閘之 `raise`／診斷訊息內容 |
| `app.py:7859` | `sorted(_got_rm), sorted(_rm), sorted(_got_rm ^ _rm),` | **B** | 結構閘之 `raise`／診斷訊息內容 |
| `app.py:7860` | `sorted(_got_ad), sorted(_ad), sorted(_got_ad ^ _ad)))` | **B** | 結構閘之 `raise`／診斷訊息內容 |
| `app.py:7883` | `sorted(_got - _bs), len(_got), _d["source"], len(_bs)))` | **B** | 結構閘之 `raise`／診斷訊息內容 |
| `app.py:8290` | `mbr_edges.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:8321` | `arms.sort(key=lambda a: -a.area)` | **C** | 邊／臂按長度或面積遞減之內部幾何選擇 |
| `app.py:8379` | `edges.sort(key=lambda e: -e['L'])` | **C** | 邊／臂按長度或面積遞減之內部幾何選擇 |
| `app.py:8667` | `candidates.sort(key=lambda x: x[0])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:9371` | `（`sorted(offset_land.geoms, key=area, reverse=True)`），使 g_rows 抵費地列之` | **D** | **註解**內引述舊寫法（`sorted(..., key=area, reverse=True)`），⛔ 可執行碼 |
| `app.py:9408` | `biz_iv.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:9555` | `# 回傳序＝**面積遞減**（逐字沿用舊 boolean 式慣例 `sorted(..., key=area, reverse=True)`）` | **D** | **註解**內引述舊寫法（`sorted(..., key=area, reverse=True)`），⛔ 可執行碼 |
| `app.py:9558` | `return sorted(pieces, key=lambda g: g.area, reverse=True)` | **C** | 抵費地片之回傳序（面積遞減）——只定 `{blk}-抵費地-{i}` 之**編號**，註解逐字載明「與回傳序無關」之內部 s 序另有其物 |
| `app.py:11254` | `_l2_ts = sorted(r['t'] for r in _l2_ok)` | **C** | 層二切換值之決定性列舉 |
| `app.py:11275` | `_switch = sorted({round(_v, 12) for _tag, _j, _v in _l2_sw})` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:11435` | `for _gid in sorted(_by_gid.keys()):` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11436` | `_idx = sorted(_by_gid[_gid])` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11455` | `for _v in sorted(_adj[_u]):` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11459` | `_out.append(sorted(_comp))` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11460` | `_out.sort(key=lambda c: c[0])` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11630` | `for _lbl in sorted(_idx_by_blk):` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11675` | `sorted(str(_m.get("暫編地號", "")) for _m in _mem)))` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11715` | `_ids = sorted(str(_m.get("暫編地號", "")) for _m in _mem)` | **C** | `k6` 連通分量／群組之決定性列舉與正規化，供比對與顯示 |
| `app.py:11929` | `_angles = sorted({round(_a % 180.0, 9) for _a in _rect_fit_edge_angles_deg(poly)}` | **C** | 環／邊索引／角度集之決定性列舉，供幾何診斷與停機訊息 |
| `app.py:12404` | `_cv.sort(key=_d_front)` | **C** | 截角三角形頂點之幾何點選（`_d_front` 升序取首），其後另有辨別性檢；受詞＝頂點 |
| `app.py:13063` | `for _rk_i, _rk_c in enumerate(sorted(` | **D（選序·受詞＝街角 PK 名次）** | `指數名次` 之賦予（`-指數4dp, _pre_position_rank`） |
| `app.py:13079` | `qualified.sort(key=lambda c: (` | **D（選序·受詞＝街角 winner）** | 🔴 街角 PK **winner 之決定**（`qualified.sort` 同鍵）——**有土地後果**，惟受詞係街角優先權、⛔ 調配選塊 |
| `app.py:13153` | `_rows.sort(key=lambda r: (r['名次'], -r['街角試算G(㎡)'], -r['指數數值'], r['暫編地號']))` | **B** | `最終序位` ＝ 報表列序（`名次, -G, -指數, 暫編地號`） |
| `app.py:13271` | `_dual = sorted(set(_by[_P1]) & set(_by[_P2]))` | **C** | 雙側交集／歸戶 id 之決定性列舉 |
| `app.py:14545` | `gids = sorted(led)` | **C** | 雙側交集／歸戶 id 之決定性列舉 |
| `app.py:17119` | `own_fp_parts.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:17136` | `mort_fp_parts.sort()` | **C** | 幾何邊長／指紋片段之裸 `sort()`，供其後比較或串接 |
| `app.py:17309` | `for fp, gid in sorted(fp_to_group.items(), key=lambda x: x[1]):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:17374` | `for _code in sorted(_all_codes):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:17417` | `for _gid in sorted(edited_df7["歸戶群組"].unique()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:17431` | `for _c3, _a3 in sorted(_blk_area.items()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:18098` | `_hits.sort(key=lambda x: -x[1])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:18345` | `_temp_no_options.extend(sorted(` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:19077` | `all_original_parcels = sorted({tp['原地號'] for tp in temp_parcels` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:19851` | `_old_ch = sorted({int(tc['cutoff_idx'])` | **C** | 截角索引集之決定性列舉，供前後比對 |
| `app.py:19859` | `_new_ch = sorted({ci for _s in ('left', 'right')` | **C** | 截角索引集之決定性列舉，供前後比對 |
| `app.py:20285` | `_k6b_locked_by_block[_lbl] = sorted(_k6b_lk_set)` | **C** | `_k6b_locked_by_block` 之決定性正規化 |
| `app.py:20561` | `for _b_ui in sorted(_cr_areas_ui.keys()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:21299` | `ordered_v2.sort(key=lambda e: (not e['is_corner_winner'],))` | **D（選序·受詞＝原位次重排）** | 🔴 `ordered_v2.sort(key=(not is_corner_winner,))` ＝ 街角 winner 置前之**原位次重排**——**有土地後果**（「下一位」之受詞係重排後之序），惟⛔ 選塊 |
| `app.py:22357` | `for blk_lbl_d, info in sorted(_diag.items()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22427` | `for _lbl_w2 in sorted(_wd2_diag):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22435` | `for _lbl_w2 in sorted(_wd2_diag):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22473` | `for _lbl in sorted(_br):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22492` | `for key in sorted(_sides):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22537` | `for _lbl in sorted(_dep):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22567` | `'右buffer(m)': v.get('right_buffer_S')} for k, v in sorted(_fo_on.items())]),` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22622` | `for _lbl, _bp in sorted(_blk_poly_dg.items()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:22664` | `for _lbl, _fo in sorted(_fo_dg.items()):` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:23391` | `_gid_options.extend(sorted(_own_groups.keys()))` | **B** | Excel／UI／診斷表之列舉與顯示序 |
| `app.py:23521` | `_gid_lands.sort(key=lambda x: x[1])` | **C** | 資料列／候選之決定性排序，供其後逐列處理或取首；受詞皆⛔ 為街廓分配 |
| `app.py:23652` | `f"（地號清單：{', '.join(sorted(_gid_parcel_set)[:5])}"` | **B** | 停機訊息內之地號清單 |

---

## §四　工項二：交接文 `§七` 該列之更正 ✅

| 項 | 值 |
|---|---|
| 受詞 | `docs/orders/交接文_W-G.9-240.md`（**純末端追加**·上文一字未改）|
| payload 來源 | 本單**第 `111`–`140` 列**（`` ```markdown `` 圍欄在 `110`／`141`·邊界已逐列印出坐實）|
| 追加量 | **1761** B／**31** LF／**CR 0** |
| 改前 | 9315 B・173 LF・`sha256 cff95c86c46dbcb5e74c4e528c5e91b7e7187b30d891cbff30cfc231e54fb190` |
| 改後 | 11076 B・204 LF・`sha256 f8763a91f1e1cca30a36820eac563c35bcae725d6984e4263c7dea88ff5b11da` |
| `numstat` | **`31 / 0`** ⇒ `deletions ＝ 0` ✅ |

**字樣錨（改前／改後二數並報）**
🔒 三軸：改前 `blob@b4ca330`／改後 本批工作區／母體 該單檔／粒度框 **列框**。

| 字樣錨 | 改前 | 改後 | 判 |
|---|---|---|---|
| `二者致` | **1** | **2** | ✅ **恰增 1**（增量係新節自身引述被更正之原句·`GB-132` 自指增長）|

🔒 **本批之實跑<u>獨立坐實</u>該更正之三處**（§三 `c`·⛔ 採單所載）：
① 射程——二情境皆於 **`R2`** 中止 ⇒ 其後 `R4`／`R5`／`R6` 一筆不產生（⛔ 僅 `R4`）；
② 二事——`0m` 之中止點係 `②-宗 圍堵閘`（`GB-67`），`3.5m` 之中止點係 telescoping 結構閘，**訊息逐字相異**；
③ 性質——二者皆令 **harness** 於 `R2` 停，其受詞為**驗收能力**（`F.0`〜`F.4` 未執行），
本批⛔ 就其是否影響 app 之配地作任何新斷言（該點依單之更正逐字：`app.py` 命中 `0` ⇒ harness 專屬）。

---

## §五　工項三：自誤 `292` ✅

### `a`　末號之獨立復算（**⛔ 採單所載之值**）

🔒 框 ＝ `VR-091` 補款二 `①` 之正字定義框 `A` ＋ 範圍框（逐字自 `docs/驗證裁定登記表.md` 取）。
🔒 三軸：來源 改前 `blob@b4ca330`／改後 本批工作區；母體 `docs/reports/W-G.9波_claude.ai側自誤登記.md` **單檔**；粒度框 **列框**。

| 量 | 改前（自算）| 單所載 | 改後（自算）| 判 |
|---|---|---|---|---|
| 一 定義框列命中 | **285** | —— | **286** | ✅ `+1` |
| 二 重咬列 | **3**（`:3338`／`:3373`／`:3403`）| —— | **3** | ✅ 不變 |
| 三 純單筆列命中 | **282** | —— | **283** | ✅ `+1` |
| 範圍框條數 | **8** | —— | **8** | ✅ 不變 |
| 相異 | **284** | **284** | **285** | ✅ 相符 |
| `MIN` | **7** | —— | **7** | ✅ |
| `MAX` | **291** | **291** | **292** | ✅ 相符 |
| 缺號清單 | **`[106]`** | **`[106]`** | **`[106]`** | ✅ 恆定期望值成立（`VR-091` 補款五）|
| 盲區探針（前綴文字非空之命中）| **0** | —— | **0** | ✅ 復審條件未觸發 |

⇒ **`N` ＝ `292`**（與單所載相符）。

### `b`　鑄號之形（依 `常規四（九）四`·⛔ 自創形）

既有最末一則之標題形 ＝ `## 自誤 \`291\`　**…**` ⇒ 本則採同形：

```
## 自誤 `292`　**沿用交接文之未證斷言，且該斷言成為下游論證之前提**
```

🔒 與單 `§四` 之形之差（逐項具名）：單作 `### \`自誤 N\`｜…`；
三處差（`###`→`##`／號入反引號之位置／`｜`→全形空白）**皆係 `常規四（九）四` 所令之範本化**，⛔ 裁量。
🔒 **內文逐字未改**（機驗：`自誤 N` 佔位符於內文出現數 ＝ **0**）。

### `c`　鑄號收工閘（`常規四（九）二`）——**三項全綠**

| 項 | 判準 | 實測 |
|---|---|---|
| ① 形之自證 | 定義列式須命中新號 | ✅ 改後命中集含 `292` |
| ② `MAX` 之推進 | `N-1` → `N`，且 `N` ⛔ 在缺號集 | ✅ `291` → `292`；`292` ⛔ 在缺號集（缺號恆 `[106]`）|
| ③ `GB-132` 零污染 | 他號類之計數⛔ 受污染 | ✅ 本批 `numstat` 僅 **2** 檔（交接文＋自誤簿）⇒ `GB` 簿／`VR` 簿／`CLAUDE.md`／`docs/rulings/**` **一字未動** ⇒ `GB`／`VR`／`戒`／`K-9` 之 `MAX` **結構上不可能變動** |

### `d`　落地量

改前 574102 B・6594 LF ／ 追加 **1451** B・**24** LF・CR 0 ／
改後 **575553** B・**6618** LF・CR 0・`sha256 eaab1bfa68cb95b631ae8035d08d1cb74102a55ada4ade808155c12ebecd1a98`；
`numstat` **`24 / 0`** ⇒ `deletions ＝ 0` ✅。

---

## §六　閘之總表

| 閘 | 判準 | 實測 | 判 |
|---|---|---|---|
| `S-0` | 最末 `SELF_SHA256` 逐位相符 | 宣告 ＝ 實算 `7fb28487…` | ✅ |
| `S-1` | 宣告框 `0/0` ＋ 兩造對照組 | `241` `0/0`／甲 `240` `4/7`／乙 `242` `0/0`／人造號 `0/0` | ✅ |
| `S-2` | append-only | 二既有檔 `deletions` 全 `0` | ✅ |
| **閘 `P`** | 生產碼五檔 `sha256` 逐位不變（**含 harness 實跑前後**）| 五檔全數相符（見下）| ✅ |
| `deletions` | append-only ＝ `0` | `31/0`・`24/0`；新檔二張（本單、本報告）亦 `0` | ✅ |
| 鑄號收工閘 | `常規四（九）二` ①②③ | 三項全綠 | ✅ |
| 缺號恆定 | 自誤缺號 ＝ `[106]` | `[106]` | ✅ |
| 逐點完備性 | 各 (檔,樣式) 表列數 ＝ 獨立計數；無漏判／多判 | `165/165` **GREEN** | ✅ |
| 倉態未受長跑污染 | 實跑後 `git status` 僅本批追加 | 僅二檔 ` M` | ✅ |

**閘 `P` 之五值**

| 檔 | B | `sha256` |
|---|---|---|
| `app.py` | 1417946 | `e3e464ea2493d0461b629941280c55238633cc57573d0837363d60eb3c85b7ca` |
| `verify/selection_pipeline.py` | 35367 | `6c6783420dbc635c4c6b6eee1f1cab7054cc281a9733fd10e35dae41c8f25cbc` |
| `verify/run_verification.py` | 96923 | `e48f24c84079f3652606bdf8fb7333964bca8cceee976533afd511964dffbebd` |
| `verify/stepg_pipeline.py` | 96261 | `0260273350021311c7ba81821fc4bc66aace6ba84d31166f3645ceb4ec6601a5` |
| `verify/run_all.py` | 24681 | `4ba89fef909794910e5705af3880e0e9ca87208f663ad4c56f16e558936ebfcf` |

---

## §七　🔴 上呈（**⛔ 由 CC 自裁**）

1. **`§二 c` 之答係「不可測」而非「`0`」** ⇒ `W-G.9-242` 之驗收設計，其前提須改以本節之事實重擬。
   本報告**⛔ 提出任何修法建議**（單之明令）。
2. **掃描母體之三個洞**（`§三 d`）：`max/min(key=)` 之真漏 **2** 列（其一 `:433` 為全部距離之起算點）／
   多列呼叫之鍵在續行 **3** 處／**單自身錨表 `2`/`4` 落在單自身母體外**。
   **母體是否擴及 `max/min(key=)`、粒度是否改 AST ＝ 意思決定。**
3. **`app.py` 之 `key=` `216` 列⛔ 得讀為排序準據**（`key=lambda` 僅 **48**；其餘多為 Streamlit widget 參數）。
   本報告已於 `§三 d` 具名此界；下游⛔ 引 `216` 為「排序準據數」。
4. **`A` 列 `12` 之中，五級之射程只及其二**（`wf_f4.py:488` ＋ 其連帶之 `:662`／`:689`）：
   `wf_f0.py:218`／`:222` 屬**同街廓級0／級0'**、`wf_f4.py:1170`／`:1228` 屬 **§7-5 第2梯**
   ——依 `-240` 入典之射程款，**五級⛔ 適用**該四者。此係**事實對照**、⛔ 修法建議。
5. **本批之 harness `FAIL 24` 列⛔ 逐列歸因**——其中多列係已登記之舊基準與已登記之結構閘；
   本報告只就 `§二 c` 所需之二中止點給證，**⛔ 就其餘 `FAIL` 作成任何新斷言**。

---

## §八　⛔ 未辦（單之明文）

- **⛔ 抽 seam**（抽 seam 為 `W-G.9-242`·生產碼·須 KL 逐 commit 放行）——本批 `app.py`／`verify/**.py` **一字未動**。
- **⛔ 於本單提出修法建議**——`§七` 各項皆為事實登記與意思決定之標旗。
- **⛔ 改交接文 `§七` 該列之上文一字**（依單以**末端追加**行之）。
- **⛔ 處置** `GB-67`／telescoping 二閘（`§二 c` 只量其中止點，未動其一字）。
