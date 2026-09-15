# `W-G.9-300R`　執行報告：路丙之**接觸面之現查** ／ 🛑 **停二成就 ⇒ 工項二⛔ 辦**

> **單** ＝ `docs/orders/W-G.9-300_開場文_接觸面之現查與修批.md`（工項零已入倉·`5b39171c`）
> **態**｜開工 ＝ `1500686adeef9e01bcf1dd928638963c79bad52b`（`ls-remote` 實查·全 `40` 碼）
> **分級** ＝ **重**（現查 ＋ `run_verification` 全量·🔴 **修批未辦**——`§三` 三-2 **停二成就**）
> 🛑 **本批⛔ 鑄任何號**（自誤／`GB`／`VR`／`K-9`／坑 皆⛔）——自捕**照實併記**（`§六`），鑄號**候發單側**。
> 🛑 **本報告⛔ 呈 KL。** ⛔ 判 `GB-170` 可否解除、⛔ 判「改幾處算只改該處」、⛔ 提修法主張。

---

## `§零`　開工閘（十一項·**每列同格載其產生指令**·`自誤 392`）

| # | 受詞（**指令逐字**） | 期值／判準 | 實測 | 判 |
|---|---|---|---|---|
| `1` | `git ls-remote origin refs/heads/wip/s1-endpart` | `1500686a…` 或其後裔 | `1500686adeef9e01bcf1dd928638963c79bad52b	refs/heads/wip/s1-endpart`（全 `40` 碼） | ✅ |
| `1′` | `git merge-base --is-ancestor 1500686a… FETCH_HEAD`；`rc` **緊接指令** | `rc = 0` | `rc = 0` | ✅ |
| `2` | `git rev-parse HEAD:app.py` | `4379108a4856714078c410ff4e6291ecfdf6d2c1` | `4379108a4856714078c410ff4e6291ecfdf6d2c1`（blob `1464014` B） | ✅ |
| `3` | `git merge-base --is-ancestor 05a11bd665f6c2790ff821c9e3a1606651e345d4 HEAD`；`rc` 緊接指令 | 須**非**祖先（`rc = 1`） | `rc = 1` | ✅ |
| `4` | `python verify/probes/probe_order_preflight.py <本單>` | `P-5` 之 `SELF_SHA256` 逐位相符·`P-3` 不紅·🟡 逐項處置 | `P-5` **`SELF_SHA256` ✅ 相符**（取檔內**最末**一個·受詞 `24984` B·實算 `e113cca6295c8003…`／單載 `e113cca6295c8003…`）·`P-3` **不紅**（`app.py` 之 `def main` ＝ `14975`-`24579`）·🔴 `0` 項·🟡 **`0`** 項 | ✅ |
| `4′` | 受詞自證（坑 `bf`·受詞 ＝ **器所印之檔名列**） | 含 `W-G.9-300` ＝ `True`／含 `W-G.9-299` ＝ `False` | 器印 `【order pre-flight】W-G.9-300_開場文_接觸面之現查與修批.md（25062 B／208 列）` ⇒ `True`／`False` | ✅ |
| `5` | 同 `4` ＋ `--selftest`；`python verify/tools/wg9223_acceptance_audit.py --selftest` | 二器 `rc = 0`·preflight 四靶逐項成立 | `rc = 0`／`rc = 0`；靶① `P-3` 紅 ✅／靶② `P-4` 提示 ✅／靶③ `P-6` 提示 ✅／**反靶** `-190R` 之 `P-3` 不紅 ✅ | ✅ |
| `6` | `python verify/probes/probe_WG9267_issuer_measurers.py registry` | 四簿之數 | 自誤 相異 `393`／MAX `403`／缺 `[106, 355, 356, 357]`｜`GB` `168`／`170`／缺 `[12, 87]`｜`VR` `80`／`95`／缺 `[73, 75]`｜`K-9` `28`／`29`／缺 `[]` | ✅ |
| `6′` | `python verify/probes/probe_WG9269_pit_index.py`（🛑 **等待綁行程結束**·⛔ `\| tail -N`） | `87`／`87`·末 `bi` ⇒ 下一 `bj` | **`87` 標籤／`87` 可解析**（數字系 `26` ＋ 字母系 `61`·末 `bi`）·母體 ＝ 追蹤 `.md` **`799`** 檔；造甲 坑 `n` 定義處 `6 ≥ 1` ✅／造乙 人造坑 `0`／`0` ✅ | ✅ |
| `7` | `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`（**正面列舉**·⛔ pathspec） | `34` 檔；判別力[必不命中] 子層 `^verify/.+/.+\.py$` 須 `> 0` | **`34`**（`1 + 33`·逐檔列舉見 `verify/out/WG9300R_static.log:9-43`）；子層 ＝ **`313`** `> 0` ✅（**逐批漂移**·⛔ 定值） | ✅ |
| `8` | `git ls-tree -r HEAD verify/baselines \| sha256sum`（`core.quotePath` **未設 ⇒ 預設**·⛔ `ls-files`） | `a898f4e1bba8…`·檔數 `298` | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·**`298`** 檔（`git config --get core.quotePath` ⇒ `rc = 1` ⇒ 未設） | ✅ |
| `9` | `git ls-remote origin 'refs/heads/verify/*'` | `…-299-gb170` ＝ `0`；判別力[必存在] `…-269-p3a` ＝ `1` | 該族共 **`20`**；`verify/W-G.9-299-gb170` ＝ **`0`**；`verify/W-G.9-269-p3a` ＝ **`1`**（`05a11bd6…`·與閘 `3` 同一物件） | ✅ |
| `10` | **四物證落檔**（**先 `git cat-file -e <rev>:<path>` 驗存在**·**三態分列**） | 四者逐位未動 | 四者皆 **態1:存在**；blob ＝ `1a35dc168655…`／`f93eb2fcb7e6…`／`16742f3805e0…`／`5cef4c8dfe7a…` ⇒ **逐位未動**；[必存在] `app.py` ＝ 態1／[必為零] 執行期組出之人造路徑 ＝ 態2／人造 `rev` ＝ 態3 | ✅ |

🩸 **閘 `10` 之自捕（出艙前攔下·⛔ 頂替·⛔ 鑄號）**
首算以**內容 `sha256`** 為框 ⇒ 四者**全不符**（`956bf39f…`／`000ae17f…`／`46b4e9e9…`／`11fb216c…`）。
**⛔ 逕判受詞紅**，先依「位元組數／校驗碼須聲明量測框」查框：單所載之十二碼係 **blob `sha1`**
（`git rev-parse HEAD:<path>`）⇒ 改以該框重算，四者**逐位相符**。
🔒 **其為量測框之誤、⛔ 受詞之誤**；🔒 `sha256` 與 `sha1` 二數**並列於上表與本節**，⛔ 只報其一。

### `§零-1`　`P-4`／`P-1` 之逐項處置

本窗實跑 preflight：🔴 **`0`** 項／🟡 **`0`** 項／ℹ️ `2` 項（`P-5` 相符、`P-3` 之 `def main` ＝ `14975`-`24579`）。
⇒ 🔒 **🟡 之判定組為<u>空</u>** ⇒ 依單 `§零-1` 之逐項處置義務**無受詞可處置**——
🛑 **本項照實具名為「判定組為空」**，⛔ 以「全數受豁免」出艙（`序 11 之一般化` 款 `二`：**空集之「全數命中」恆真**）。

---

## `§零′`　前批之核可　🔒 **⛔ 重辦**（單明定「發單側已辦」）

五 `commit`（`f608d50e`／`d2866022`／`80d59188`／`e0215256`／`1500686a`）之核可係**發單側之行為**，本窗⛔ 重辦、⛔ 覆核。

---

## `§一`　新窗之態（**首則·已重建·⛔ 略**）

**首讀四檔**（皆自 `git show HEAD:<path>`·⛔ 讀工作區·⛔ 憑記憶）：
① `docs/orders/W-G.9-299_施工單_鑄號形之更正與路丙之受領與修批.md`（`343` 列·其 `§五`／`§六` 全文）
② `docs/orders/W-G.9-299_補令一_舊窗收工批.md`
③ `docs/reports/W-G.9-299_交接註_舊窗收工.md`（`279` 列·**十二項**）
④ `docs/reports/W-G.9-298R_A′受詞之重釘與閘iii造之重設_執行報告.md`

🔒 **工作區之態（開窗第一動作·`harness-worktree` 之陷阱查）**：
`git rev-parse --abbrev-ref HEAD` ＝ `claude/land-readjustment-orders-7a4635`；
`git rev-list --left-right --count HEAD...1500686a…` ＝ **`0	0`** ⇒ **工作區即波線態**（⛔ `main` 態）；
`core.autocrlf` 三層分列 ＝ system `true`／global **未設**（`rc = 1`）／**local `false`** ⇒ 有效值 **`false`**；
`CLAUDE.md` 工作區 `236365` B ＝ 其 blob `236365` B（**⛔ CRLF 膨脹**）；
`.claude/settings.json` 與 `verify/tools/wg9237_heredoc_guard.py` **二者皆在** ⇒ heredoc 硬閘**於本 session 生效**
（🔒 本窗實測其**確曾攔下**一次 ⇒ ⛔ 恆綠·見 `§六` 自捕 `3`）。

| # | 事 | 本窗之遵行 |
|---|---|---|
| `3` | 路丙之地位 ＝ **`GB-170` 之修之實作形**·射程 ＝ **取線之設計** | ✅ 本批只量**接觸面**（施行之可行性），⛔ 觸取線之設計 |
| `4` | KL 放行之射程 `(a)(b)`；`(c)` ⛔ 及於入倉主線 | ✅ **本批⛔ 動用放行**（工項二未辦）·⛔ 開任何分支 |
| `5` | `GB-170` 失效條件 `(2)(3)` 候工項二 | ✅ **⛔ 解除、⛔ 收窄、⛔ 提修法主張** |
| `6` | 未解之餘量 `6.157e-6 ㎡`（比值 `0.987897178336173`） | ✅ **⛔ 以此充「其成因已閉合」**·本批⛔ 判其成因 |
| `7` | 次號 自誤 `404`／`GB` `171`／`VR` `96`／`K-9` `30`／坑 `bj` | ✅ **本批零鑄號**（`§六` 收工閘 `4`／`5` 證之） |

---

## `§二`　工項零：**本單原封入倉**（主線·`commit 5b39171c`）

| 受詞 | 實測 |
|---|---|
| 落點 | `docs/orders/W-G.9-300_開場文_接觸面之現查與修批.md`（新檔·`numstat` ＝ **`208` 增／`0` 刪**） |
| **三方逐位對拍**（blob ＝ 磁碟 ＝ 源） | `True`——blob `25062` B·內容 `sha256` `7547a131b9d7e812a98ba9df114cb1766556901d866c244553be473409dff016`·blob `sha1` `e78cb6d8705c369a82cdd7007103b4f254dc483a` |
| `CR`（框 ＝ `bytes.count(b'\r')`·**讀 blob 取 bytes**） | **`0`**；判別力[必非零] ＝ 倉內 blob `data/V6.dxf` `CR` **`12308`**（全長 `88341` B） |
| **受詞自證**（坑 `bf`） | 器所印之檔名含 `W-G.9-300` ＝ `True`[必真]／含 `W-G.9-299` ＝ `False`[必偽] |
| 檔數自證（框 ＝ `os.path.isfile`·母體 ＝ 工作區） | 受詞 ＝ `1`；造甲[必≥1] `W-G.9-299_補令一…` ＝ `True`／造乙[必為0] **執行期組出**之人造名 ＝ `False`（字面⛔ 出艙） |
| 生產碼判法（母體**正面列舉 `34` 檔**·框 ＝ `git diff --name-only 1500686a..HEAD` ⋂ 四檔清單） | **`0`** 行 ⇒ **零生產碼 commit** ⇒ 依 `常規一` 補款 `🔧 一` **逕行 `push`**；對照組[必非零] `17fd981^..17fd981` ＝ **`2`** ⇒ 器非紅 |

🔒 **閘之量測與其所守護之動作係<u>分開之呼叫</u>**（`W-G.9-199` 常規補款 `一`）——
生產碼判法之量測、三方對拍、`push`、`push` 後之 `ls-remote` 各為**獨立之呼叫**，⛔ 置於同一命令塊。

---

## `§三`　工項一：**路丙之接觸面之現查**（主線·**零生產碼**）

🔑 **本工項所用之二項手段，皆在單 `§三` 首段之明文授權內**：
① **執行 `run_verification` 全量**（款 `2` 乙形之動態量測）——🛑 **⛔ 改生產碼一字**；
② **於 `verify/probes/` 新增量測器** ＝ `verify/probes/probe_WG9300_contact_surface.py`（**新檔**）——
🛑 **⛔ 動既有探針一字**（`§六` 收工閘 `6` 之 `34` 檔 blob 相異 `0` 證之；`verify/probes/**` 既有檔亦零異動）。

🔒 **本器對生產態之唯一介入**＝ 換 `run_verification.harvest` 之**模組屬性**，使其於 `harvest()` 回傳後
包裹 `ns["_corner_buffer_S"]`（此即 `W-G.9-299 §五` 款 `2` 所**明定**之取法），
其包裹**只讀不改**（`return fn(*a, **k)`）。**⛔ 改 `app.py`／`verify/` 任一檔之 bytes。**

### 三-1　款 `1`：`S` ＝ `_corner_buffer_S` 之全部呼叫端（**AST**·二形並取）

**母體**（**正面列舉**·⛔ pathspec `verify/*.py`）＝ **`34`** 檔｜**框** ＝ `ast.Call`，其 `func` 為
`Name('_corner_buffer_S')`（**形甲**）**或** `Subscript(Name('ns'), Constant('_corner_buffer_S'))`（**形乙**）。
**檔／處二數並報**：檔 ＝ **`4`**／處 ＝ **`7`**　【倉】`verify/out/WG9300R_static.log:8`

| # | 檔 | 所在函式名 | 形 | **字樣錨**（⛔ 行號為錨） | 錨之唯一性 | `allocation_dir` 位之實參逐字 | 落 `def main` 內 |
|---|---|---|---|---|---|---|---|
| `S1` | `app.py` | `main` | 形甲 | `` `_left_buffer_S = _corner_buffer_S(` `` | `1` | `` `allocation_dir_block` ``（位置#4） | 🔴 **True** |
| `S2` | `app.py` | `main` | 形甲 | `` `_right_buffer_S = _corner_buffer_S(` `` | `1` | `` `allocation_dir_block` `` | 🔴 **True** |
| `S3` | `verify/stepg_pipeline.py` | `_run_step_g_impl` | 形甲 | `` `_left_buffer_S = _corner_buffer_S(` `` | `1` | `` `allocation_dir_block` `` | False |
| `S4` | `verify/stepg_pipeline.py` | `_run_step_g_impl` | 形甲 | `` `_right_buffer_S = _corner_buffer_S(` `` | `1` | `` `allocation_dir_block` `` | False |
| `S5` | `verify/wf_f1.py` | `compute` | **形乙** | `` `left_buffer_S = ns["_corner_buffer_S"](` `` | `1` | `` `alloc_dir` `` | False |
| `S6` | `verify/wf_f4.py` | `_reshape_block` | **形乙** | `` `buf = (ns["_corner_buffer_S"](block_poly, d_hat, p1, alloc_dir,` `` | 🔴 **`2`** | `` `alloc_dir` `` | False |
| `S7` | `verify/wf_f4.py` | `_reshape_block` | **形乙** | （**同上·`S6`／`S7` 共用一字樣**） | 🔴 **`2`** | `` `alloc_dir` `` | False |

🛑 **loud 具名一（錨之唯一性不足）**：`S6`／`S7` 之字樣錨於 `wf_f4.py` **命中 `2`** ⇒ **⛔ 唯一**
——二者係 `side == 'left'` 之 `IfExp` 二支（`left`／`right`），其賦值列逐字相同。
⇒ 引用該二處者**須併載其 `side` 實參**（`'left'`／`'right'`）方足以定位。

🛑 **loud 具名二（文字層與 AST 二數相異）**：文字層（`_corner_buffer_S(` 之**列框**）＝ **`5`** 列
（`app.py` `3`／`verify/stepg_pipeline.py` `2`）；AST 之處 ＝ **`7`** ⇒ **差 `-2`**　【倉】`:78`
**成因逐項**（⛔ 一句帶過）：
> `(a)` 文字層**多計** `1`：`app.py` 之 `` `def _corner_buffer_S(block_poly, d_hat, front_p1, allocation_dir, range_area, side,` ``
> 係**定義列**、⛔ `Call` 節點。
> `(b)` 文字層**漏計** `3`：`S5`／`S6`／`S7` 之寫法為 `` ns["_corner_buffer_S"](`` ⇒ **字樣 `_corner_buffer_S(` 於該二檔命中 `0`**。
> 🔑 ⇒ **「二形並取」⛔ 是形式要求**——單取形甲（或單取文字層）將**整組漏掉 `wf_f1`／`wf_f4` 之三處**，
> 而該三處**全為 `forced` 路徑**（款 `4′`）⇒ 漏之則 `停二` 之受詞被削去一半。

### 三-2　款 `2`：`F` ＝ 生產期實走之呼叫端（**二形並取·⛔ 擇一**）

#### （甲）**靜態**：`verify/run_verification.py` 之遞移 `import` 閉包（母體 ＝ `34` 檔）

**全量列舉**（基數 ＝ **`11`**）　【倉】`verify/out/WG9300R_static.log:107-118`：
`run_verification.py`／`app_harvest.py`／`selection_pipeline.py`／`stepg_pipeline.py`／`wf_f0.py`／
`wd3_fragment_geom.py`／`wd4_tier_list.py`／`wf_f1.py`／`wf_f2.py`／`wf_f3.py`／`wf_f4.py`

| `S` 之檔 | 在閉包內 |
|---|---|
| `app.py` | 🔴 **否** |
| `verify/stepg_pipeline.py` | ✅ 是 |
| `verify/wf_f1.py` | ✅ 是 |
| `verify/wf_f4.py` | ✅ 是 |

🛑 **本形之界限（照實·⛔ 頂替）**：`app.py` 之「⛔ 在閉包內」**⛔ 等同「其碼未被載入」**
——`app.py` 係由 `app_harvest.harvest()` **`exec`** 入 `ns`（`co_filename` ＝ `'<app.py:harvest>'`），
**⛔ 經 `import`** ⇒ **`import` 圖結構上看不見它**。⇒ 甲形對 `app.py` **無鑑別力**，其判由**乙形**承擔。

#### （乙）**動態**：包裹 `ns["_corner_buffer_S"]` ＋ **呼叫鏈之 `co_name`／`co_filename` 序**（**⛔ `id(·)`**）

🔒 **取法之具名**：單 `§三` 款 `2` 乙形逐字許「`sys.settrace` **或等價**」。
本器取**等價之包裹形**（＝ `W-G.9-299 §五` 款 `2` 所明定者），其由有二：
① `settrace` 之全域攔截於本案之長跑（`235.7 s`）代價過鉅；
② 受詞之辨識所需者為**呼叫鏈之 `co_name`／`co_filename` 序**，包裹形可由 `sys._getframe` 直取，
**與 `settrace` 同值**且⛔ 觸及生產碼。

**驅動**＝ `run_verification.main()`（**全量一次**·**等待綁行程結束**·⛔ `| tail -N`）
`rc` ＝ **`1`**（＝ **准紅碼**之常態·⛔ 本批所致）·耗時 **`235.7 s`**·例外 **無**　【倉】`verify/out/WG9300R_dynamic.log:1044`
包裹實際生效次數 ＝ **`1`**（`harvest` 有快取 ⇒ `1` 即足）

**逐閘出艙執行次數**：**生產錄 ＝ `21`**　**器自身 ＝ `0`**　【倉】`:1046`
🔒 **量測器之母體⛔ 含其自身輸出**——二欄**分列**，後者須 `0` 且實得 `0`。

**外圍函式之執行計數**（🔑 **區辨「外圍未執行」與「外圍執行而 `forced` 為偽」**）　【倉】`:1048-1053`

| 受詞 | 次數 |
|---|---|
| `run_verification.run_step_g`（**已綁之名**） | **`4`** |
| `stepg_pipeline.run_step_g`（**模組屬性**） | **`10`** |
| `wf_f1.compute` | **`0`** |
| `wf_f4._reshape_block` | **`0`** |
| `wf_f4.compute` | **`0`** |

🛑 **二處並換之由（⛔ 只換其一）**：`run_verification` 係 `from stepg_pipeline import (…)`
⇒ 其名**於 `import` 時已綁** ⇒ 單換 `_SP` 之模組屬性對該 driver **無效**，所得之 `0` 將係
**綁定之別**、⛔ 受詞之真。⇒ **二處並換並二數分列**（`4`／`10`·二者皆非零 ⇒ 器非紅）。

**`F` 之逐 site 歸屬**（鍵 ＝ **呼叫端自身之框**）　【倉】`:1056`
> 檔 `stepg_pipeline.py` :: 函式 `_run_step_g_impl` ⇒ 對位之 AST 處 ＝ **`S3`**
> 執行次數 ＝ **`21`**　`side` 之分布 ＝ `['left']`　`_label` 之分布 ＝ `['R2', 'R4']`
> 呼叫鏈（`co_name`@`co_filename`）＝ `_run_step_g_impl`@`stepg_pipeline.py` → `run_step_g`@`stepg_pipeline.py`
> → `main`@`run_verification.py` → `run_dynamic`@`probe_WG9300_contact_surface.py`

🔒 **`|F| = 1`**（＝ `{S3}`）·**`|S∖F| = 6`**　【倉】`:1100`

**`S∖F` 逐處之「未執行」之<u>分項成因</u>**（⛔ 以「未執行」充「非接觸面」·一律 **loud 具名為「本案未走·射程未定」**）：

| # | 執行次數 | **分項成因**（⛔ 一句帶過） | 射程 |
|---|---|---|---|
| `S1`／`S2` | `0` | 🔴 **落於 `app.py` 之 `def main` 內**（AST 實查 ＝ `14975`-`24579`）——`harvest` 保留 `main` 而**從不呼叫**（走 `stepg`）⇒ **`run_verification` 結構上⛔ 驅動之** | **UI 路徑**·本批**結構上不可驗** |
| `S4` | `0` | 外圍 `_run_step_g_impl` **確曾執行**（`run_step_g` `4`／`10` 次·且同函式之 `S3` 錄得 `21` 次）⇒ 其未執行係 **`_fo_right` 為偽**（本案三 `forced` 格**皆左側**） | 本案未走·**射程未定** |
| `S5` | `0` | 🔴 外圍 `wf_f1.compute` **執行 `0` 次** ⇒ **整段從未進入**（⛔ 「進入而分支為偽」） | 本案未走·**射程未定** |
| `S6`／`S7` | `0` | 🔴 外圍 `wf_f4.compute` 與 `wf_f4._reshape_block` **皆執行 `0` 次** ⇒ **整段從未進入** | 本案未走·**射程未定** |

🔒 **二形之結果分列並報**：甲形（`import` 閉包）判 `wf_f1`／`wf_f4` **在**閉包內，
乙形（動態）判其**執行 `0` 次** ⇒ **二形相異**。
🛑 **loud 具名其相異之成因**：甲形量「**可否被載入**」、乙形量「**本案是否走到**」——
**二者⛔ 同一述詞**；`wf_f1`／`wf_f4` 係「可載入而本案未走」。⇒ 🔒 **以乙形為 `F` 之判準**，
甲形之用僅在**證 `app.py` 之特殊性**（既⛔ 在 `import` 圖內、亦⛔ 在執行錄內）。

### 三-3　款 `3`：`_first_corner_alloc_dir` 之可達性 ＋ `side_mid` 之在域性

**注入通道之窮舉**（`自誤 399` 族·⛔ 以「其一可達」充「皆可達」）＝ **模組 `__globals__`／`ns`／參數／閉包** 四者。

| 通道 | `S3`（＝ `F`·**動態實測**·`f_locals`／`f_globals`） |
|---|---|
| 模組 `__globals__` | `_first_corner_alloc_dir` 在 `f_globals` ＝ **`False`** |
| `ns` | 鍵 `ns` 在 `f_locals` ＝ **`True`**；`ns` 含 `_first_corner_alloc_dir` ＝ **`True`** |
| 參數 | `ns` 係 `_run_step_g_impl` 之在域名（同上） |
| 閉包 | `co_freevars` ＝ **`()`** |

⇒ 🔒 **`S3` 之三態判 ＝「`ns` 注入」**（⛔ 模組全域直呼·⛔ 不可達）。
**靜態半**（`t.body` 頂層·全 `7` 處）：`_first_corner_alloc_dir` 於**頂層**僅見於 `app.py`（`True`）；
於 `stepg_pipeline.py`／`wf_f1.py`／`wf_f4.py` 皆 **`False`**，且三檔之 `ns["_first_corner_alloc_dir"]` **列框 ＝ `0`**
⇒ 該符號於此三檔**現行⛔ 被消費**。

**`side_mid` 之在域性（二鍵並報·鍵先自證存在·⛔ 只報其一）**

| 量測 | 靜態（AST·該函式內·**呼叫列之前**是否已賦值） | 動態（`f_locals`·**呼叫當下**） |
|---|---|---|
| `side_mid` | 七處**皆空** | `S3`：**`False`** |
| `_side_mid_left` | 七處**皆於呼叫列之<u>後</u>方賦值**（`app`／`stepg`）或**全無**（`wf_f1`／`wf_f4`） | `S3`：**`True`** |
| `_side_mid_right` | 同上 | `S3`：**`True`** |
| `_side_lines_blk` | — | `S3`：**`True`** |

🔴 **二量測相異 ⇒ 必須具名其成因（⛔ 取其一而略其一）**：
`S3` 與 `_side_mid_left`／`_side_mid_right` 之賦值**同處一個逐街廓 `for` 迴圈之內**
（`for (blk_label, parcels_in_blk)`），而**賦值在呼叫之後** ⇒
> **首次**迭代時該二名**未綁**（靜態判「⛔ 可取」為真）；
> **其後**之迭代，該二名**綁的是<u>前一街廓</u>之值**（動態判 `True` 之由）。

🛑 ⇒ **`f_locals` 之 `True` ⛔ 等同「可取」**——於 `S3` 取 `_side_mid_left` 將**靜默取得前一街廓之側界中點**。
🔒 實測坐實其可發生：本案 `_label` 分布 ＝ `['R2', 'R4']`，而 `R2` 之前尚有 `R1` 迭代
（`R1` 兩側皆非 `forced` ⇒ 其 `S3` 未觸發而 `_side_mid_*` 仍被賦值）。
⇒ 🔒 **就單 `§四` 款 `1` 之附款「`side_mid` 之取式須自該處在域之名取」而言，`S3` 之在域性<u>不足</u>**
——在域之名存在，惟其**值屬他街廓**；取之即**靜默錯值**（⛔ 型別可擋）。
🛑 **本報告⛔ 就此提任何改法**（⛔ 新增參數、⛔ 改簽章、⛔ 自行擴改）——照實出艙，候發單側。

### 三-4　款 `4`：**判準載體**之現查（頂層 `*_EXPECT` 之 **AST** 賦值 ＋ `baselines` 列框）

**框** ＝ `t.body` 之 `Assign`／`AnnAssign`，目標 `Name` 且 `endswith('_EXPECT')`（**⛔ 字樣掃**）。
全母體合計 ＝ **`11`** 個／分布 **`4`** 檔　【倉】`verify/out/WG9300R_static.log:100`
⇒ 🔒 **與發單側之預查（`11` 個·`run_verification.py`／`wd4_tier_list.py`／`wf_f0.py`／`wf_f4.py`）相符**
（🛑 其為**外部錨**·本器**自行重得**·⛔ 以預查充結論）。

| 檔 | 頂層 `*_EXPECT` | 逐名 | `baselines` 列框 |
|---|---|---|---|
| `verify/run_verification.py` | `1` | `K_STAR_EXPECT` | `16` |
| `verify/wd4_tier_list.py` | `7` | `MINA_QU_EXPECT`／`HALF_EXPECT`／`FLAGGED_EXPECT`／`TRACK_EXPECT`／`TIER_EXPECT`／`PUB_PARCELS_EXPECT`／`PUB_HOLDER_GROUPS_EXPECT` | `1` |
| `verify/wf_f0.py` | `1` | `GSA_EXPECT` | `5` |
| 🔴 **`verify/wf_f4.py`** | **`2`** | `COMP_EXPECT`／`E0_EXPECT` | `1` |
| `app.py` | `0` | — | `22` |
| `verify/stepg_pipeline.py` | **`0`** | — | `4` |

**`S ∪ F` 之檔別判**：`app.py` `0`／`verify/stepg_pipeline.py` **`0`**／`verify/wf_f1.py` `0`／🔴 `verify/wf_f4.py` **`2`**。

### 三-5　款 `4′`：各處**是否為 `forced` 之路徑**（`停二` 之受詞·**AST 實查**·⛔ 憑閱讀）

**其判之產生指令（逐字）**：對每一 `Call` 節點取其於該檔 AST 之**全部外圍** `ast.If`／`ast.IfExp`
（判準 ＝ `n.lineno <= call.lineno <= n.end_lineno`），將其 `test` 以 `ast.unparse` 出艙；
**旗字樣集（逐字）** ＝ `('_fo_left', '_fo_right', 'forced_offset', 'forced')`；任一外圍 `test` 命中即判為 `forced` 路徑。

| # | **命中之外圍 `test`（逐字）** | 判 |
|---|---|---|
| `S1` | `If` `` `_fo_left` `` | **是** |
| `S2` | `If` `` `_fo_right` `` | **是** |
| `S3` | `If` `` `_fo_left` `` | **是** |
| `S4` | `If` `` `_fo_right` `` | **是** |
| `S5` | `If` `` `fo.get('left_forced_offset')` `` | **是** |
| `S6` | `IfExp` `` `fo.get('left_forced_offset')` `` | **是** |
| `S7` | `IfExp` `` `fo.get('right_forced_offset')` `` | **是** |

🔒 **判別力[必為否]**：以**同一支求值器**餵一**已知非 `forced`** 之受詞 ＝ `_corner_buffer_S` 之**定義列**
（`def _corner_buffer_S`）⇒ 其外圍 `If`／`IfExp` ＝ **`0`** 個 ⇒ 判 **否** ✅
⇒ 🔒 **該判準非恆真**（⛔ 「凡受詞皆判是」）。　【倉】`verify/out/WG9300R_static.log:255`

### 三-6　款 `5`：判別力**五**造

| 造 | 期 | 實測 | 判 |
|---|---|---|---|
| [必非零] `\|S\| ≥ 1` | `≥ 1` | `7` | ✅ |
| [必相異] 文字層之數與 AST 之數**各自出艙** | 二數並報 | `5` 與 `7` | ✅ |
| [必為零] 一**執行期組出**之人造函式名（字面⛔ 出艙） | `0` | `0` | ✅ |
| [必命中] `verify/run_verification.py` 在甲形閉包內（自反） | `True` | `True` | ✅ |
| 🆕 [必為 `34`] **母體基數之外部錨**（＝ `§零` 閘 `7`） | `34` | `34` | ✅ |

🩸 **第五造係本窗自捕後所增**（見 `§六` 自捕 `1`）——**原四造對母體塌陷全盲**。

---

## `§四`　🛑 **三停機款之逐款判**

| # | 停機款（單 `§三` 三-2 逐字） | 實測 | **判** |
|---|---|---|---|
| **停一** | `\|F\| = 0` | `\|F\| = **1**`（＝ `{S3}`·執行 `21` 次） | 🟢 **未成就** |
| **停二** | `S∖F` 中有任一處**經判為 `forced` 之路徑**而未在 `F` 內 | `S∖F` ＝ `{S1, S2, S4, S5, S6, S7}`（`6` 處）·**`6` 處<u>全數</u>經判為 `forced` 路徑**（款 `4′`·判別力[必為否] 成立） | 🔴 **成就** |
| **停三** | `F` 中有任一檔其**頂層 `*_EXPECT` 賦值數 `> 0`** | `F` 之檔 ＝ `verify/stepg_pipeline.py` ⇒ 頂層 `*_EXPECT` ＝ **`0`** | 🟢 **未成就** |

### `§四-1`　`停二` 之 **loud 具名**（單所明令）

> 🔴 **`S∖F` 含 `app.py` 之二處（`S1`／`S2`）——該二處係 <u>UI 路徑</u>、`run_verification` ⛔ 驅動**
> （`harvest` 保留 `main()` 而**從不呼叫**）⇒ **其改於本批結構上不可驗**：
> 改之則工項二款 `2`（其餘逐位不變）與款 `3`（逐宗面積差）**必全綠**，
> 而該綠**得其所非**——綠之來源係「該碼從未被執行」，⛔ 「改動無害」。（六問第 `4` 問）

### `§四-2`　`停三` 之**併記**（⛔ 讀為「已排除」）

`停三` 於**現態**未成就，惟其**唯一之由**係 `F` 恰為 `{S3}` 而 `stepg_pipeline.py` 之 `*_EXPECT` ＝ `0`。
🔴 **`S∖F` 之 `S6`／`S7` 落於 `verify/wf_f4.py`，該檔頂層 `*_EXPECT` ＝ `2`（`COMP_EXPECT`／`E0_EXPECT`）**
⇒ **若發單側裁該二處為射程 `(b)` 之「該處」而納入受改之集，`停三` 即當場成就**（`GB-48` 族之自我指涉）。
🛑 **本報告⛔ 就此作成任何裁**——照實併記，候發單側。

### `§四-3`　🛑 **本批之處置**

**`停二` 成就 ⇒ 依單 `§三` 三-2 之明文「判器紅、停、上呈·⛔ 續辦工項二」**：

- ⛔ **未辦工項二**（`§四` 修批）之**任一款**；
- ⛔ **未動用 KL 之放行**（其射程 `(a)(b)` 於本批**仍未動用**·`(c)` 之第二次放行更未涉及）；
- ⛔ **未改生產碼一字**；⛔ **未開 `verify/W-G.9-299-gb170` 或任何分支**；
- ⛔ **未判**「改幾處算只改該處」——**孰為 KL 射程 `(b)` 之「該處」由發單側裁**（單 `§三` 逐字）。

🔒 **工項二款 `5` 之受詞（藍影／`K-9-23` 閘一之求值次數·`_lot_gate` 之筆數與 `is_second_after_corner` 之值）
＝ <u>未辦</u>**——其屬工項二，受停機款拘束。🛑 **⛔ 以「未辦」充「已量為零」**；
`GB-170` 原節所載之「該二格 `_lot_gate` 各 `1` 筆·`is_second_after_corner` 恆 `False` ⇒ 藍影求值 `0` 次」
係**前批之實測**，本批**⛔ 復現、⛔ 引為本批之數**（其「應否求值」逐字**未判**·本批亦⛔ 判）。

---

## `§五`　一句話推導

> `_corner_buffer_S` 之呼叫端**實為 `7` 處**（二形並取方見·單取文字層只見 `4` 處而漏掉 `wf_f1`／`wf_f4` 之三處），
> 其中生產期**實走者僅 `1` 處**（`stepg_pipeline._run_step_g_impl` 之左支·`21` 次·`R2`／`R4`），
> 而**其餘 `6` 處<u>全數</u>是 `forced` 路徑**——含 `app.py` 之二處（UI 路徑·`run_verification` 結構上⛔ 驅動）
> ⇒ **「改 `F` 即足」不成立**、接觸面**逾** KL 射程 `(b)` 之「只改該處」⇒ **停二成就 ⇒ 工項二⛔ 辦**。

---

## `§六`　本批之自捕（**逐則**·形／徵候／根因／攔法·**皆於出艙前攔下**·⛔ 頂替·🛑 **⛔ 鑄號**·鑄號候發單側）

| # | 形 | 徵候 | 根因 | 攔法 |
|---|---|---|---|---|
| `1` | 新器之母體由 `34` 檔**靜默塌為 `1` 檔**，而**判別力四造全綠** | 輸出載「基數 ＝ `1`（`1 + 0`）」而 `§零` 閘 `7` 同態獨立得 `34` ⇒ **二數互斥** | 器居 `verify/probes/` 而 `REPO` 取**二層** `dirname` ⇒ 解為 `…/verify` ⇒ `git ls-tree HEAD -- verify/` 於該 cwd 解為 `verify/verify/` ⇒ **靜默得空**；`app.py` 因 `HEAD:app.py` 與 cwd 無關而**倖存**，遂使 `[必非零] \|S\|≥1` 與自反之 `[必命中]` **二造照樣全綠** | **母體基數須綁<u>外部錨</u>**（`常規八 二 ③` 界限檢查）⇒ 增 `[必為 34]` 第五造；🔒 **`N/N` 之自證只證一致·⛔ 證正確** |
| `2` | `F` 之逐處歸屬**七處全塌為一桶**，且所印之「位」係**上一層**之位 | 印出「呼叫端 ＝ `run_step_g` :: 位 `:259`」，而 `:259` 落於 `run_step_g` 之內、⛔ 任一 `Call` 之位 | `_chain()` 自 `sys._getframe(2)` 起 ⇒ `chain[0]` **即呼叫端自身**，而聚合鍵誤取 `chain[1]` | 聚合鍵改取 `chain[0]`，並**將每筆錄與 AST 之 `S#` 逐筆對位**（對不上即 loud）；已重跑全量（`235.7 s`）復現 |
| `3` | 以 `python - <<'PYEOF'` 就地補綴器碼之呼叫被**阻斷** | `PreToolUse` 回 `exit 2` ＋ 逐字理由（`H1 heredoc/herestring 引入符`·偏移 `162`） | **⛔ 誤攔**——係 `GB-143` 補款二之**真攔截點**確實生效 | 依其 `MISFIRE_POLICY` **處置一**：改以落檔／路徑呼叫（本批改用逐處 `Edit`）；🔒 **⛔ 停用本器、⛔ 改其 `PATTERNS`**。**併記其為本器之活體生效實證**（`§一`） |
| `4` | 閘 `10` 四物證**全判不符** | 四者**同時**不符 ⇒ 「全錯」比「部分錯」更像**框之誤** | 單所載之十二碼係 **blob `sha1`**，而首算以**內容 `sha256`** 為框 | **位元組數／校驗碼須聲明量測框**；二框**並列出艙**（`§零` 閘 `10` 與其自捕節），⛔ 只報其一 |
| `5` | 器之 `forced` 判準之首版**印不出**（`rc = 1`） | `TypeError: not all arguments converted during string formatting` | `%` 格式化之右運算元為 `tuple`（`FORCED_TOKENS`）⇒ 被展開為多引數 | **以 `rc` ＋ traceback 為判**（⛔ 以「有落檔」充「已跑完」）；改 `% (FORCED_TOKENS,)` 後重跑 |

🔒 **五則皆<u>於出艙前</u>攔下**；`1`／`2` 二則**已致一次全量重跑**（`235.7 s`），其 v1 落檔**保全⛔ 覆寫**：
`verify/out/WG9300R_static_v1_popcollapse.log`（`7475` B）／`verify/out/WG9300R_dynamic_v1_wrongframe.log`（`164551` B）。

---

## `§七`　⛔ **為之事**之逐項自檢（單 `§五`·**逐項**·⛔ 略）

| 受詞 | 自檢 |
|---|---|
| ⛔ 併線（含 `p3a`／本批之新支） | ✅ **未為**——本批⛔ 開任何分支；`p3a` 對 `HEAD` 之 `merge-base --is-ancestor` 仍 `rc = 1` |
| ⛔ push 任何生產碼異動至 `wip/s1-endpart` | ✅ **未為**——生產碼判法逐 `commit` 皆 **`0`** 行 |
| ⛔ 第二次放行前⛔ 推主線之生產碼 | ✅ **未為** |
| ⛔ 覆寫 `verify/baselines` 任一檔或**四物證落檔**任一 | ✅ **未為**——`baselines` `298` 檔·`a898f4e1…` 期初＝期末；四物證 blob 逐位未動 |
| ⛔ `WV_BAKE` | ✅ **未設**（shell ＝ `<未設>`／`os.environ.get('WV_BAKE')` ＝ `None`） |
| ⛔ 引任何自 baseline 取得之數 | ✅ **未為**——本報告之數皆出自 AST 現查與活體執行錄 |
| ⛔ 改任何函式簽章／⛔ 改任何 `*_EXPECT` 一字／⛔ 新增任何 `import` 於生產碼 | ✅ **未為**（`34` 檔 blob 期初＝期末·相異 `0`） |
| ⛔ 改 `_corner_buffer_S`／`_build_corner_range_v3`／`_first_corner_alloc_dir`／`k956_W_from_mp`／`_mp_base_W0` 之**函式體**一字 | ✅ **未為** |
| ⛔ 動 `ALPHA_LABELS` 一字 | ✅ **未為**——其唯一載體 `verify/probes/probe_WG9269_pit_index.py` 之 `git diff --numstat` 輸出**空** |
| ⛔ 動 `probe_WG9292_pathC.py`／`probe_WG9295_joint.py`／`probe_WG9298_gate3.py`／任何**既有**探針一字 | ✅ **未為**——本批於 `verify/probes/` **只新增一檔** |
| ⛔ 鑄自誤／`GB`／`VR`／`K-9`／坑之**任何號** | ✅ **零鑄號**（收工閘 `4`／`5` 證之）·自捕五則**照實併記於 `§六`**、鑄號候發單側 |
| ⛔ 解除或收窄任何 `GB`（含 `GB-170`） | ✅ **未為** |
| ⛔ 落地 `K-9-5-*`／`K-9-12`／`K-9-29` 之任何子項 | ✅ **未為** |
| ⛔ 追改 `W-G.9-299`／補令一／交接註或任何已入倉文件一字 | ✅ **未為**——本批 `deletions` 全 `0`（逐 `commit` 見 `§八`） |
| ⛔ 刪任何 ref | ✅ **未為**——`refs/heads/verify/*` 期初＝期末 **`20`** 個 |
| ⛔ 擴 KL 放行之射程／⛔ 呈 KL／⛔ 擬第二次放行之呈文 | ✅ **未為** |
| ⛔ 判 `GB-170` 可否解除／⛔ 判「改幾處算只改該處」／⛔ 判孰是／⛔ 判孰誤／⛔ 提修法主張 | ✅ **未為**——`§三`／`§四` 只出艙 `S`／`F`／逐處之判**與其產生指令** |
| ⛔ 驗 `(甲)`／`(乙)` 逐位相同之機制 | ✅ **未為** |
| ⛔ 於任何入倉文件宣稱一件尚未發生之事 | ✅ **未為**——`push` 後之 `ls-remote` 實查值**出艙於回報**（收工閘 `7`）·⛔ 入倉 |

---

## `§八`　逐 `commit`（**全 `40` 碼**·**主線與分支分列**）

**分支** ＝ **無**（本批⛔ 開任何分支·`verify/W-G.9-299-gb170` 期末仍 **`0`**）。

**主線**：

| # | `commit`（全 `40` 碼） | 題 |
|---|---|---|
| `1` | `5b39171cf3be193c52a78b52edeb1ccfbbfd630b` | `W-G.9-300 工項零：本單原封入倉（三方逐位對拍·受詞自證）⛔ 零生產碼` |
| `2` | （本報告 ＋ 新器 ＋ 五物證落檔·其 `sha` 見回報） | `W-G.9-300 工項一：接觸面之現查 ＋ 停二成就（⛔ 辦工項二）⛔ 零生產碼` |

---

## `§九`　收工閘（**報告入倉後量**·嚴格末端追加）

（本節於報告入倉後以**純末端追加**補之。）
