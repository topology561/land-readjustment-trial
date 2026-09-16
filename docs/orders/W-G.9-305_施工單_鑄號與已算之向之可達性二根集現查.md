# `W-G.9-305`　施工單（**中**）：`自誤 413`・`414` ＋ 坑 `bn`・`bo` 之鑄 ／ `GB-170` 末端追加 ／ **已算之向於強制呼叫點之可達性現查（二根集）**

> **態**｜開工 ＝ `96a8204ef143231d643af395dc4ed151f820af07` **或其後裔**（發單側自倉 `ls-remote` 實查·🛑 CC 須自行重跑·**全 `40` 碼**·坑 `bh`）。
> **單** ＝ `docs/orders/W-G.9-305_施工單_鑄號與已算之向之可達性二根集現查.md`（工項零 ＝ 本單原封入倉）。
> **分級** ＝ **中**（登記 ＋ 靜態器原封入倉 ＋ 現查 ＋ **`run_verification` 全量一次**·**零生產碼**·**⛔ 開分支**·**⛔ 修批**）。
> 🛑 **本批鑄號 ＝ `自誤 413`・`414` ＋ 坑 `bn`・`bo`**（**四號**·逐字由本單供）；`GB`／`VR`／`K-9` **⛔ 鑄**。
> 🔑 **`ALPHA_LABELS` 之擴至 `bo` 於本批<u>明文授權</u>**（射程逐字見 `§四`·⛔ 逾之）。
> 🔴 **KL 之放行於本批<u>仍不動用</u>**；⛔ 改生產碼 `34` 檔一字。
> 🔑 **序**（`補令四 §零-3` 之標準附款）：**① `§二` 工項零**（單獨 `commit`·**單獨 `push`**）⇒ **② `§一` 開工閘** ⇒ **③ `§三` 工項一**（靜態器·**其實得與期值逐項相符後方得進 ④**）⇒ **④ 其餘工項**。
> 🛑 **辦畢 ⇒ 出報告 ⇒ 停**。⛔ 呈 KL。

---

## `§零`　發單側之核可與裁（**⛔ CC 自裁·⛔ CC 重辦**）

### `§零-1`　`W-G.9-304` 全批之核可（發單側自倉獨立復驗）

- `c9cc3854…`..`96a8204e…` ＝ **`9`** 個 `commit`（`git rev-list --count`）；`git show --numstat` 之刪除欄合計 **`0`**。
- 生產碼 `34` 檔（`git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`）於 `f24e1d7a10dac4da352469f91a2d5a833d6922ab`（`W-G.9-281` 工項零）與 `HEAD` 之間 `git diff --name-only` ＝ **`0`** 行。
- `probe_WG9267_issuer_measurers.py registry` ⇒ 自誤 `402`／`412`·`GB` `168`／`170`·`VR` `80`／`95`·`K-9` `29`／`30`；`probe_WG9269_pit_index.py` ⇒ **`91`／`91`**·末 `bm`。
- `verify/out/WG9304R_static.log` ＝ `17147` B／`LF` `216`／`CR` `0`；`WG9304R_dynamic.log` ＝ `169888` B／`LF` `1157`／`CR` `0`（皆取 blob bytes）。
- `W-G.9-304R §六-1` 之出現 `17`／形 `9` 經發單側**另器重得**（見 `§三` 期值 `A1`）。
- 物證落檔 **`19`** 檔（`§一` 項 `11` 之產生方式）皆態1。
⇒ **✅ 全批核可**。🔑 受單側之自捕 `1`〜`6` 皆於出艙前攔下，**處置正確**。

### `§零-2`　裁（六項）

| # | 事 | **裁** |
|---|---|---|
| `1` | 停七之判 | ✅ **受領其數**：該值確經 `_r['_alloc_dir_used']`（回傳值·鍵為字串常數·⛔ 含街廓識別）出艙。🛑 **「經回傳值出艙」⛔ 等同「於強制呼叫點可取」**——其消費端之所屬作用域見 `§三` 期值 `B` |
| `2` | 🔴 **停八之射程** | 其數受領；惟其受詞 ＝ **全程首次呼叫序號**之先後，混入不同呼叫端（不同管線階段）與不同輪次之呼叫 ⇒ **代理量**。`W-G.9-304R §六-4` 之 `('R4','L')` `_solve_G_one` 首次序號 `1` **早於任何**強制呼叫（首次 `91`）即其直證 ⇒ **停八之「不成就」⛔ 及於「強制呼叫點當下同一 (街廓,側) 之值是否已可取」** ⇒ 鑄 `自誤 414`（`§四`） |
| `3` | 🔴 **`自誤 413` 之形** | `W-G.9-304 §六-2` 款 `1` 之「十三形」⛔ 窮舉（`304R` 實測其外 `5` 形）。🔑 **併須具名**：`304R` 所採之「`(父節點型別, 欄位, ctx)` 三元組」構造上窮舉者**只及父節點**；其「出現」仍以 `Name`／`arg` 二節點型別界定 ⇒ **仍為清單**。發單側器（`§三` 節 A）實測：舊定義出現 `17`／形 `9`；**構造上之定義**（每一節點之每一欄位值逐字相等）出現 **`20`**／形 **`11`**；多出之 `3` ＝ `Constant.value`（父 `Subscript.slice`）×`2` ＋ `keyword.arg`（父 `Call.keywords`）×`1`——**前者正是停七所依之容器鍵 `'_alloc_dir_used'` 本身** |
| `4` | `GB-170` 登記表內之**自相矛盾** | 其 `W-G.9-299` 節（末端追加）載「**KL 之放行於 `W-G.9-299` 首次動用**」；而 `W-G.9-299_補令一` 逐字「其動用移至新窗（`W-G.9-300`）」、`W-G.9-300R` 逐字「KL 之放行**仍未動用**」、其後各節皆載「仍未動用」⇒ **放行迄今未動用**。該句⛔ 追改（append-only），以 `§五` 之末端追加為準。其形屬 `W-G.9-280_補令一 §八` 第 `7` 則之禁（「於任何入倉文件宣稱一件尚未發生之事」）⇒ **⛔ 鑄號** |
| `5` | 🔑 **次一受詞** | **已算之向，自其產生處至 `_corner_buffer_S` 強制呼叫點之可達性**——以**二根集分列**、**逐次**、**值空間法**現查（`§六`）。二根集 ＝ **(體)** 函式體內可及者（形參 ∪ 其 `__globals__`）／**(端)** 呼叫端框可及者（`f_locals` ∪ `f_globals`）。🛑 **⛔ 判落點、⛔ 判可施** |
| `6` | 發單側出單前之自捕（**⛔ 入倉之窗間文件**·⛔ 鑄號） | ① 窗間文件擬以「`_run_step_g_impl` 之 `f_locals`」為容器之母體——而 `res`／`_n` 之 `Store` 全屬其**巢狀函式**（`§三` 期值 `B`）⇒ **結構上排除受詞所在之層**（`自誤 411` ② 之重踩·停機款將依構造成就）；已改為 `§六` 之二根集。② 窗間文件之「本波九單」其列舉實為八（坑 `bo` 之形）。③ 本單之靜態器初稿節 B 有**二欄**標籤與運算式不符（坑 `bo` 之形·已修·見 `§四` 坑 `bo` 例 ③） |

---

## `§一`　開工閘（十二項·**每列同格載其產生指令**·`自誤 392`·🛑 **跑於 `§二` 之後**）

| # | 受詞（指令逐字） | **期值／判準** |
|---|---|---|
| `1` | `git ls-remote origin refs/heads/wip/s1-endpart` | `96a8204ef143231d643af395dc4ed151f820af07` **或其後裔**（全 `40` 碼） |
| `2` | `git rev-parse HEAD:app.py`（🔒 **框 ＝ blob `sha1`**·`自誤 405`） | `4379108a4856714078c410ff4e6291ecfdf6d2c1` |
| `3` | `git merge-base --is-ancestor 05a11bd665f6c2790ff821c9e3a1606651e345d4 HEAD` | 須**非**祖先（`rc = 1`·`rc` **緊接該指令**·先 `git cat-file -t` 證該物存在） |
| `4` | `python verify/probes/probe_order_preflight.py <本單>` | `P-5` `SELF_SHA256` 逐位相符（🔒 **整全性之判準即此·⛔ 另設帶外釘死**·`自誤 412`）；`P-3` 不紅；🟡 **逐項具名處置**（見 `§一-1`） |
| `4'` | 受詞自證（坑 `bf`） | [必真] 含 `W-G.9-305` ＝ `True`／[必偽] 含 `補令六` ＝ `False` |
| `5` | 同 `4` ＋ `--selftest`；`python verify/tools/wg9223_acceptance_audit.py --selftest` | 二器 `rc = 0` |
| `6` | `python verify/probes/probe_WG9267_issuer_measurers.py registry`（🔒 **器之輸出為正典**） | 自誤 **`402`**／**`412`**（缺 `[106,355,356,357]`）｜`GB` `168`／`170`（缺 `[12,87]`）｜`VR` `80`／`95`（缺 `[73,75]`）｜`K-9` `29`／`30`（缺 `[]`） |
| `6'` | `python verify/probes/probe_WG9269_pit_index.py` | **`91`／`91`**·末標籤 **`bm`** ⇒ 下一 **`bn`**（🛑 **等待綁行程結束**·⛔ `\| tail -N`） |
| `7` | `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py`（**正面列舉**·坑 `be`） | **`34`** 檔；判別力[必不命中] 子層 **須 `> 0`**（⛔ 定值）；🔑 **本數即本批一切母體之外部錨**（坑 `bj`） |
| `8` | `git ls-tree -r HEAD verify/baselines \| sha256sum`（`core.quotePath` **預設**） | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·檔數 `298` |
| `9` | `git ls-remote origin 'refs/heads/verify/*'` | 該族 `20` 支；`verify/W-G.9-299-gb170` 命中 **`0`**（**⛔ 開**）；判別力[必存在] `verify/W-G.9-269-p3a` 命中 **`1`** |
| `10` | **本波九單之在倉性**（`自誤 407` 攔法 ③·**三態分列**·`rc` 緊接指令） | `W-G.9-303` 施工單／補令一〜六（`7`）＋ `W-G.9-304` 施工單（`1`）＋ 本單（`1`）＝ **`9`** **皆態1**；🛑 其列舉之產生指令 ＝ `git ls-tree -r --name-only -z HEAD docs/orders/` ⋂ 檔名前綴 `W-G.9-303_`／`W-G.9-304_`／`W-G.9-305_`（**取 bytes**·坑 `bk`）⇒ 計數**由該指令得**；判別力[必為零] ＝ 一**執行期組出**之人造路徑須 `rc ≠ 0`（字面⛔ 出艙） |
| `11` | **物證落檔**（🔒 **框 ＝ blob `sha1`**·**先 `cat-file -e` 驗存在**·三態分列·取 bytes） | 集合甲 ＝ `docs/reports/W-G.9-303_交接註_舊窗收工二.md` 之節 `10` 表內之 `.log` 名（**⛔ 轉錄**·自 blob 取）⇒ `13`；集合乙 ＝ `git ls-tree -r --name-only HEAD verify/out/` ⋂ 名前綴 `WG9303R6_`／`WG9304R_` ⋂ `*.log` ⇒ `6`；（集合甲取**相異**名）聯集 **`19`** ⇒ **皆態1·逐位未動**（🔒 `WG9303R6_*.log` 四份之 `CR` **非 `0`** 係已具名之自捕·**⛔ 修**·⛔ 判紅） |

### `§一-1`　`P-4`／`P-1`／`P-2` 之逐項處置（**⛔ 靜默略過**·**⛔ 目視**）

🛑 **歸類⛔ 目視**——須**先查該器之觸發式**再據以定位其真受詞（`W-G.9-303R6 §一-3` 之體例）。
🟡 之受詞若屬**三類**⇒ **受具名豁免**：**(甲)** `→`／`⇒` 係**賦值鏈／消費鏈／查表鏈／流程節序**之串接（含**引述**他處之此類串接者）；
**(乙)** 方向性之詞係**序之詞而非幾何**（`前綴`／`後裔`／`首`／`末`／`前`／`後`／`先`／`晚`／`早`／`首次`／`裡側`）；
**(丙)** `⇒` 係**推論之連詞**，⛔ 空間之指向。
🛑 三類皆⛔ 幾何向量之方向性轉引 ⇒ **無座標系可具名**。**凡不在此三類內者，⛔ 受本豁免，須停、照實具名、⛔ 續**。
🛑 本批出艙之向量變換（`§六` 款 `3` 之四變換）一律**以座標分量之逐字式**具名（`(x,y)`／`(−x,−y)`／`(−y,x)`／`(y,−x)`），⛔ 以「左轉／右轉」代之。

🛑 **恆常附款逐項適用·⛔ 省**（坑 `bh`／`bi`／`bj`／`bk`／`bl`／`bc`／`bd`／`be`／`bf`／`bg`／`g`／`3`、
`GB-158` **三形分列**（🔒 自誤之標題形為 **C 形** `` `自誤 N` ``·⛔ B 形）、簡繁誤字機檢、`rev` 釘死、**先跑再寫**、
[必為零]之造須**先自證可滿足**且**判定組為空時 loud 拒測**、payload 之落地形機驗**繫於性質**、
函式名**二形並取**、頂層全域取 `t.body`、`rc` **緊接指令**、**逐閘出艙執行次數**、**等待綁行程結束**、
**`id(·)` ⛔ 作錨**、**⛔ `\| tail -N`**、**讀 blob 取 bytes**、**量測器之母體⛔ 含其自身輸出**、
**帶號與絕對值並列**、**物證落檔保全⛔ 覆寫**、`f_locals` 鍵須**自證存在**並**增第二鍵**、
`git rev-parse <rev>:<路徑>` 未加 `--` 之**回退** ⇒ 先 `cat-file -e`·**三態分列**、
**簿之數一律取器之輸出**、**母體之基數須綁外部錨**、**含 CJK 路徑之 `git` 輸出取 bytes**、
**摘要值一律逐字具名其產生指令**、**母體一律以產生指令界定**、
**⛔ `git ls-files --with-tree=<rev>`**（坑 `bl`）、**`grep` 含 alternation 者逐支分列**·**字面之框自 blob 逐字取**（`自誤 409`）、
**落檔一律 `open(p,'wb')`**·**⛔ shell 重導向 Python `stdout`**（`W-G.9-303R6` 自捕 `5`）、
**凡長跑在跑，任何修復動作須先確認無在途之量測**、
🆕 **框之語法形須窮舉**·**母體以頂層名界定者須同格出艙其非頂層之基數**（`自誤 411`）、
🆕 **機械順序**：⛔ 預書 之款一律「佔位符 → 跑 → 填」·**逐款回掃**同文件之警告（坑 `bm`）、
自捕為零者須併具「**⛔ 讀為『本批無誤』**」）。
🆕 **本單新增之恆常附款**：**「出現」一律以「每一節點之每一欄位值逐字相等」構造上界定**（`自誤 413`）、
**時序閘須先具名其比較之執行脈絡**·全程序號⛔ 作判準（`自誤 414`）、
**以 `stdout` 落檔之器一律 `reconfigure(encoding="utf-8", newline="\n")`**（坑 `bn`）、
**欄之標籤逐字須與其運算式逐項對照後方得出艙**（坑 `bo`）。

---

## `§二`　工項零：**本單原封入倉**（主線·🔑 **先於開工閘**）

落點 ＝ `docs/orders/W-G.9-305_施工單_鑄號與已算之向之可達性二根集現查.md`；**⛔ 改一字**。
🔒 **整全性之判準 ＝ `SELF_SHA256`（`P-5`）**——**⛔ 另設任何帶外之釘死**（`自誤 412` 攔法 ①）；
其判別力二造（必綠 ＝ 原檔／必紅 ＝ 改一位元組之副本·**該副本⛔ 入倉**）須**出艙**。
**入倉後之出艙**：**blob `sha1` ＋ blob 內容 `sha256` ＝ 磁碟 ＝ 源**（🔒 **二框並報**）；
`CR` ＝ `0`（**讀 blob 取 bytes**；判別力[必非零] ＝ `data/V6.dxf`）；`deletions` ＝ **`0`**；
**受詞自證**（坑 `bf`·[必真] 含 `W-G.9-305`／[必偽] 含 `補令六`）；
檔數 ＝ `1` 之自證（造甲[必≥1] ＝ `docs/orders/W-G.9-304_施工單_K-9-30之落地與已算之向之可得性.md`／造乙[必為0] ＝ **執行期組出**之人造名·字面⛔ 出艙）。
🛑 **落地後即 `push`**（生產碼判法 `0` 行 ⇒ `常規一` 補款：逕行 `push`），**其後方跑 `§一`**。

---

## `§三`　工項一：**發單側靜態器之原封入倉 ＋ 重跑**（主線·**零生產碼**·🔑 **先於 `§四`**）

🔑 **明文授權**：於 `verify/probes/` **新增一檔** `probe_WG9305_issuer_static.py`（**⛔ 動既有探針一字**）＋ 其落檔 `verify/out/WG9305_issuer_static.log`。
🔒 地位 ＝ **發單側自擬框·⛔ 正典**（`自誤 331` 之體例）；入倉之唯一目的 ＝ 使本單 `§零-2` 所引之數**可逐字重跑**（`自誤 409`）。

### 三-1　落檔之形（**⛔ 改一字**）

界 ＝ `<!-- P305S-BEGIN -->` 與 `<!-- P305S-END -->` 之間；其內**首個**逐字為 ```` ```python ```` 之列與**其後首個**逐字為 ```` ``` ```` 之列**之間**之全部列（**⛔ 含二 fence 列**），
以 `b'\n'` 連接並加尾 `b'\n'`，**`open(p,'wb')`** 落檔。
🔒 **落檔後之機驗**（本單內載·其傳遞由 `SELF_SHA256` 保之·⛔ 帶外）：內容 `sha256` ＝ `dc5ef64f55f2de26d7c5298d99dc5253cc94751cb730f5d5cb2b57159300ecb2`／`11289` B／`204` 列／`CR` ＝ `0`；
不符 ⇒ **停、照實具名、⛔ 逕修**。界之唯一性 ＝ **整列逐位相等**·母體 ＝ 本單單檔·各須 **`1`**（併報子字串框之數·**二數並報**）。

### 三-2　執行（**於倉根目錄**·落檔 `open(p,'wb')`·⛔ shell 重導向 Python `stdout`）

`python verify/probes/probe_WG9305_issuer_static.py HEAD` ⇒ `rc = 0`；落檔 `CR` ＝ `0`。

### 三-3　🔑 **期值**（發單側於 `96a8204e…` 以本器逐字原樣實跑所得·**逐項對拍**·🛑 **任一不符 ⇒ 停、照實具名、⛔ 進 `§四`**）

| 代號 | 器之輸出欄（**標籤逐字**） | 期值 |
|---|---|---|
| `錨` | `[錨] git ls-tree HEAD --name-only verify/ ⋂ *.py ＋ app.py` | `34` 檔 |
| `A1` | `A1（Name∪arg 節點）：出現`／`相異形` | `17`／`9` |
| `A2` | `A2（每一欄位值·構造上）：出現`／`相異形` | `20`／`11` |
| `A2∖A1` | `A2 ∖ A1（A1 之定義結構上⛔ 及者）` | 出現 `3`／形 `2` ⇒ `('Constant.value', 'Subscript', 'slice', '-')` ×`2`；`('keyword.arg', 'Call', 'keywords', '-')` ×`1` |
| `自洽` | `自洽：A2 之 Name/arg 部分 ＝ A1 ？` | `True` |
| `造` | `判別力[必為零] 人造名於 A2`／`判別力[必非零] A2 出現` | `0`／`20` |
| `A層` | `非頂層基數（自誤 411 攔法 ②）` | `0` |
| `B0` | `巢狀作用域（Function/Async/Lambda/ClassDef ＋ 四種 comprehension）＝`／`其中具名者 ＝` | `52` ⇒ `DictComp 9`／`FunctionDef 13`／`GeneratorExp 14`／`Lambda 1`／`ListComp 14`／`SetComp 1`；具名 `13` |
| `B-res` | `res` 之 `Store/形參 所屬作用域`／`Load`／`其餘 str 欄位` | `{'_advance_block_with_split': 3}`／`{'_advance_block_with_split': 43}`／`{('_chain','Constant.value'): 1, ('_iface_deltas','Constant.value'): 4}` |
| `B-_n` | `_n` 之 `Store/形參`／comprehension 內 `Store` | `{'_iface_deltas': 1, '_guard_auth_scope': 1}`／`1`（🛑 **本器之自限**·其所屬作用域係併入外層具名函式者·**loud**） |
| `B-dir` | `_near_dir_left`／`_near_dir_right` 之 `Store` | 各 `{'_advance_block_with_split': 2}` |
| `B-key` | `_alloc_dir_used` 之 `其餘 str 欄位` | `{('_advance_block_with_split','Constant.value'): 2, ('_iface_deltas','Constant.value'): 1}` |
| `B-For` | 逐街廓 `For` 處數／其所屬作用域／`_corner_buffer_S` 之 `Name` 形呼叫 | `1`／`_run_step_g_impl`／`2` 處（所屬 `_run_step_g_impl`） |
| `B-ord` | `上開 34 處呼叫之位序先於最末一處強制呼叫者`／`於本 For 內定義之 11 個中，其定義位序先於首處強制呼叫者` | `0`／`0` |

🛑 **本工項⛔ 由上表判「可得」或「不可得」**——靜態之位序⛔ 等同執行之先後（迴圈、跨輪、跨呼叫端皆可使二者相異·`自誤 414`）；其判由 `§六` 之動態款承擔。

<!-- P305S-BEGIN -->

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probe_WG9305_issuer_static.py — 發單側（claude.ai）出 `W-G.9-305` 前之自擬靜態現查器·原封入倉（自誤 331 之體例）

🔒 地位：發單側自擬框·**⛔ 正典**。入倉之唯一目的 ＝ 使受單側可逐字重跑發單側於單內所引之數（自誤 409）。
🔒 唯讀：只以 `git cat-file blob <rev>:<path>` 取 bytes（坑 bk）；⛔ 寫任何 tracked 檔；⛔ import 生產路徑。
用法：python verify/probes/probe_WG9305_issuer_static.py [<rev>]      （預設 HEAD）

節 A：`app.py :: _solve_G_one` 之受詞出現普查——二種「出現」之定義並報
  A1 ＝ `W-G.9-304R §六-1` 之定義（僅 `ast.Name` 節點 ＋ `ast.arg` 節點）之 (父節點型別, 欄位, ctx)
  A2 ＝ **構造上之定義**：AST 內**每一節點之每一欄位值**，凡為 `str` 且逐字等於受詞者皆為一「出現」
        （含 `Constant.value`／`keyword.arg`／`Attribute.attr`／`alias.name`／`Global.names` 等·⛔ 以型別清單界定）
節 B：`verify/stepg_pipeline.py :: _run_step_g_impl` 之巢狀作用域與七名之所屬作用域

🔒 本器之自限（loud）：
  ① 「出現」＝ 逐字相等（⛔ 子字串）；執行期組出之字串、變數鍵之 `getattr`、`exec` 靜態不可見 ⇒ 由動態款承擔。
  ② 節 B 之「所屬作用域」以具名函式／lambda 計；comprehension 作用域併入其外層具名函式——其受影響之數逐名出艙。
  ③ 位序（行號）只供比較先後，⛔ 為錨。
"""
import ast, sys, subprocess, collections

sys.stdout.reconfigure(encoding="utf-8", newline="\n")   # 坑 bn：`newline` ⛔ 可省

REV = sys.argv[1] if len(sys.argv) > 1 else "HEAD"


def blob(path):
    r = subprocess.run(["git", "cat-file", "blob", f"{REV}:{path}"], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"STOP: cat-file rc={r.returncode} for {path}")
    return r.stdout.decode("utf-8")


def fdef(tree, name):
    hits = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name]
    return hits


def parents(root):
    P = {}
    for p in ast.walk(root):
        for f, v in ast.iter_fields(p):
            for c in (v if isinstance(v, list) else [v]):
                if isinstance(c, ast.AST):
                    P[id(c)] = (p, f)
    return P


def ctxname(n):
    return type(n.ctx).__name__ if hasattr(n, "ctx") else "-"


def census_A1(fn, names):
    P = parents(fn)
    C = collections.Counter()
    for n in ast.walk(fn):
        if isinstance(n, ast.Name) and n.id in names:
            p, f = P[id(n)]; C[(type(p).__name__, f, ctxname(n))] += 1
        elif isinstance(n, ast.arg) and n.arg in names:
            p, f = P[id(n)]; C[(type(p).__name__, f, "-")] += 1
    return C


def census_A2(fn, names):
    """每一節點之每一欄位值逐一比對（構造上窮舉·⛔ 型別清單）。
    節點形出現（其欄位屬於 Name/Constant 等葉節點）⇒ 以其**父節點**之 (型別, 欄位) 為形；
    其餘（識別字為某節點之 str 欄位，如 keyword.arg／arg.arg）⇒ 以 (擁有者型別.欄位, 其父型別, 父欄位) 為形。"""
    P = parents(fn)
    C = collections.Counter()
    for owner in ast.walk(fn):
        for field, val in ast.iter_fields(owner):
            for v in (val if isinstance(val, list) else [val]):
                if not (isinstance(v, str) and v in names):
                    continue
                par, pf = P.get(id(owner), (None, "-"))
                pt = type(par).__name__ if par is not None else "(root)"
                C[(f"{type(owner).__name__}.{field}", pt, pf, ctxname(owner))] += 1
    return C


def main():
    print("=" * 100)
    print(f"【probe_WG9305_issuer_static】rev = {REV}")
    ls = subprocess.run(["git", "rev-parse", REV], capture_output=True).stdout.decode().strip()
    print(f"rev-parse = {ls}")
    print("=" * 100)

    # ── 外部錨（坑 bj）──
    tops = subprocess.run(["git", "ls-tree", REV, "--name-only", "verify/"], capture_output=True).stdout.decode("utf-8").split("\n")
    prod = sorted([t for t in tops if t.endswith(".py")] + ["app.py"])
    print(f"[錨] git ls-tree {REV} --name-only verify/ ⋂ *.py ＋ app.py ⇒ {len(prod)} 檔")

    # ── 節 A ──
    app = ast.parse(blob("app.py"))
    d = fdef(app, "_solve_G_one")
    print(f"\n── 節 A　app.py :: _solve_G_one（定義處 {len(d)}）──")
    if len(d) != 1:
        raise SystemExit("STOP: _solve_G_one 定義處 ≠ 1")
    fn = d[0]
    names = {"allocation_dir", "_alloc_dir_used", "_r"}
    print(f"受詞名集（逐字·承 W-G.9-304R §六-1）＝ {sorted(names)}")
    a1 = census_A1(fn, names); a2 = census_A2(fn, names)
    print(f"A1（Name∪arg 節點）：出現 {sum(a1.values())}／相異形 {len(a1)}")
    for k, v in sorted(a1.items(), key=lambda x: (-x[1], x[0])):
        print(f"   {v:>3}  {k}")
    print(f"A2（每一欄位值·構造上）：出現 {sum(a2.values())}／相異形 {len(a2)}")
    for k, v in sorted(a2.items(), key=lambda x: (-x[1], x[0])):
        print(f"   {v:>3}  {k}")
    a2_nodeform = collections.Counter()
    for (own, pt, pf, cx), v in a2.items():
        if own in ("Name.id",):
            a2_nodeform[(pt, pf, cx)] += v
        elif own == "arg.arg":
            a2_nodeform[(pt, pf, "-")] += v
    extra = {k: v for k, v in a2.items() if k[0] not in ("Name.id", "arg.arg")}
    print(f"A2 ∖ A1（A1 之定義結構上⛔ 及者）：出現 {sum(extra.values())}／形 {len(extra)} ⇒ {sorted(extra.items())}")
    print(f"自洽：A2 之 Name/arg 部分 ＝ A1 ？ {dict(a2_nodeform) == dict(a1)}")
    art = "".join(chr(c) for c in (95, 122, 122, 113, 57, 51, 48, 53))   # 執行期組出之人造名
    print(f"判別力[必為零] 人造名於 A2 ⇒ {sum(census_A2(fn, {art}).values())}")
    print(f"判別力[必非零] A2 出現 ⇒ {sum(a2.values())}")
    inner = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)) for n in ast.walk(fn) if n is not fn)
    print(f"非頂層基數（自誤 411 攔法 ②）：_solve_G_one 內 FunctionDef/AsyncFunctionDef/Lambda ＝ {inner}")

    # ── 節 B ──
    sp = ast.parse(blob("verify/stepg_pipeline.py"))
    d = fdef(sp, "_run_step_g_impl")
    print(f"\n── 節 B　verify/stepg_pipeline.py :: _run_step_g_impl（定義處 {len(d)}）──")
    if len(d) != 1:
        raise SystemExit("STOP: _run_step_g_impl 定義處 ≠ 1")
    g = d[0]
    scopes = [n for n in ast.walk(g) if n is not g and isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp, ast.ClassDef))]
    cnt = collections.Counter(type(n).__name__ for n in scopes)
    print(f"巢狀作用域（Function/Async/Lambda/ClassDef ＋ 四種 comprehension）＝ {len(scopes)} ⇒ {dict(sorted(cnt.items()))}")
    named = [n for n in scopes if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    print(f"其中具名者 ＝ {len(named)} ⇒ {[n.name for n in named]}")

    # 每一節點之最內層「具名或 lambda」作用域
    owner_scope = {}
    def walk(node, cur):
        for c in ast.iter_child_nodes(node):
            nxt = c.name if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else ("<lambda>" if isinstance(c, ast.Lambda) else cur)
            owner_scope[id(c)] = nxt if nxt is not cur else cur
            walk(c, nxt)
    walk(g, "_run_step_g_impl")

    comp_t = (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)
    in_comp = set()
    for c in ast.walk(g):
        if isinstance(c, comp_t):
            for x in ast.walk(c):
                if x is not c:
                    in_comp.add(id(x))
    six = ["res", "_n", "_nodes", "_prev_dir", "_near_dir_left", "_near_dir_right", "_alloc_dir_used"]
    print(f"\n名集（逐字）＝ {six}")
    for nm in six:
        store = collections.Counter(); load = collections.Counter(); strf = collections.Counter()
        for owner in ast.walk(g):
            for field, val in ast.iter_fields(owner):
                for v in (val if isinstance(val, list) else [val]):
                    if not (isinstance(v, str) and v == nm):
                        continue
                    sc = owner_scope.get(id(owner), "_run_step_g_impl")
                    if isinstance(owner, ast.Name):
                        (store if isinstance(owner.ctx, ast.Store) else load)[sc] += 1
                    elif isinstance(owner, ast.arg):
                        store[sc + "(形參)"] += 1
                    else:
                        strf[(sc, f"{type(owner).__name__}.{field}")] += 1
        print(f"  {nm:<16} Store/形參 所屬作用域 ⇒ {dict(store)}")
        print(f"  {'':<16} Load 所屬作用域      ⇒ {dict(load)}")
        print(f"  {'':<16} 其餘 str 欄位（含字串常數）⇒ {dict(strf)}")
        nc = sum(1 for o in ast.walk(g) if isinstance(o, ast.Name) and o.id == nm and isinstance(o.ctx, ast.Store) and id(o) in in_comp)
        print(f"  {'':<16} 其 Name-Store 位於 comprehension 作用域內者（本器將其併入外層具名函式·自限）⇒ {nc}")

    # 強制呼叫點與巢狀函式之呼叫點，於最外層逐街廓 For 內之先後
    fors = [n for n in ast.walk(g) if isinstance(n, ast.For) and "parcels_by_block" in ast.unparse(n.iter)]
    print(f"\n逐街廓 For（iter 含字樣 parcels_by_block）＝ {len(fors)} 處")
    for F in fors:
        calls = []
        for n in ast.walk(F):
            if isinstance(n, ast.Call):
                fnm = n.func.id if isinstance(n.func, ast.Name) else None
                if fnm:
                    calls.append((n.lineno, fnm, owner_scope.get(id(n), "?")))
        cb = [c for c in calls if c[1] == "_corner_buffer_S"]
        inner_names = {x.name for x in named}
        ic = [c for c in calls if c[1] in inner_names]
        defs_in = [(x.lineno, x.name) for x in named if F.lineno <= x.lineno <= F.end_lineno]
        print(f"  For 所屬作用域 = {owner_scope.get(id(F), '_run_step_g_impl')}")
        print(f"  _corner_buffer_S 之 Name 形呼叫 ⇒ {len(cb)} 處；所屬作用域 ⇒ {sorted({c[2] for c in cb})}")
        print(f"  於本 For 內定義之巢狀具名函式 ⇒ {len(defs_in)} 個 ⇒ {[x[1] for x in sorted(defs_in)]}")
        print(f"  全部 {len(inner_names)} 個巢狀具名函式（含本 For 外定義者）於本 For 內之 Name 形呼叫 ⇒ {len(ic)} 處 ⇒ {dict(sorted(collections.Counter(c[1] for c in ic).items()))}")
        if cb:
            last_cb = max(c[0] for c in cb)
            before = [c for c in ic if c[0] < last_cb]
            print(f"  （位序·⛔ 為錨）上開 {len(ic)} 處呼叫之位序先於最末一處強制呼叫者 ⇒ {len(before)} 處 ⇒ {before}")
            dbefore = [x for x in defs_in if x[0] < min(c[0] for c in cb)]
            print(f"  （位序·⛔ 為錨）於本 For 內定義之 {len(defs_in)} 個中，其定義位序先於首處強制呼叫者 ⇒ {len(dbefore)} 個 ⇒ {[x[1] for x in dbefore]}")
    print("\n【本器⛔ 判可施與否·⛔ 擬任何改法】")


if __name__ == "__main__":
    main()
```

<!-- P305S-END -->

---

## `§四`　工項二：`自誤 413`・`414` ＋ 坑 `bn`・`bo` 之鑄 ＋ `ALPHA_LABELS` 之擴（主線·**三段分列 `commit`**·🛑 **`§三` 全數相符後方得辦**）

🔑 **明文授權一項手段**：**擴 `ALPHA_LABELS` 至 `bo`**——射程 ＝ **僅** `verify/probes/probe_WG9269_pit_index.py` 內
**新增一列** `ALPHA_LABELS += ["bn", "bo"]`（形同其既有之 `+= ["bh", "bi"]` 列·尾註同體例），**⛔ 改該檔任何既有列一字**、**⛔ 動其任何框或判準**。

🔑 界：自誤 ＝ `<!-- ZW413-BEGIN -->`／`<!-- ZW413-END -->`；坑 ＝ `<!-- PITBN-BEGIN -->`／`<!-- PITBN-END -->`。
落點皆 ＝ `docs/reports/W-G.9波_claude.ai側自誤登記.md` **檔末追加**（**二段分列 `commit`**）。
🛑 唯一性之框 ＝ **整列逐位相等**（`^…$`）·母體 ＝ 本單單檔·各須命中 **`1`**；併報**子字串框**之數（**二數並報**）。
🛑 payload **⛔ 剝層、⛔ 加 `> `、⛔ 改一字**；**落檔 `open(p,'wb')`**；追加之式須為 `old + b'\n' + payload + b'\n'`。
🔒 **坑之定義處<u>多於一處</u>之預先受領**（本單標題列亦含其標籤）——**本單⛔ 予其期值**（`自誤 403` 攔法 ②）；CC 以器之定義框出艙其清單並照實具名，**⛔ 判紅、⛔ 逕修**。

<!-- ZW413-BEGIN -->

### 🩸 `自誤 413`　**以「窮舉」自許之普查，其「出現」之界定仍係清單——分類軸構造上窮舉，受詞集未然**

**形（二層）**：
① `W-G.9-304` `§六-2` 款 `1` 令「十三形」並附「⛔ 以此為窮舉之上限」——`W-G.9-304R` `§六-1` 實測其外 **`5`** 形：
`('Assign','value','Load')`／`('Tuple','elts','Load')`／`('Compare','left','Load')`／`('comprehension','iter','Load')`／`('Attribute','value','Load')`。
② 🔑 受單側據以改採之「對受詞之每一出現取 `(父節點型別, 欄位, ctx)` 三元組」——其構造上窮舉者**只及父節點之分類**；
其「**出現**」仍以 `ast.Name`／`ast.arg` **二節點型別**界定 ⇒ **受詞集仍為清單**。
發單側於出單前以 `verify/probes/probe_WG9305_issuer_static.py` 節 A 實測（`app.py :: _solve_G_one`·受詞名集 `['_alloc_dir_used','_r','allocation_dir']`）：
舊定義 ＝ 出現 **`17`**／形 **`9`**；**構造上之定義**（AST 內每一節點之每一欄位值逐字相等）＝ 出現 **`20`**／形 **`11`**；
二者之差 ＝ `('Constant.value','Subscript','slice')` ×**`2`** ＋ `('keyword.arg','Call','keywords')` ×**`1`**。

**徵候**：多出之 `Constant.value` 二處，**正是停七所依之跨呼叫容器鍵 `'_alloc_dir_used'` 本身**
——`W-G.9-304R` 係另以款 `2`（`Subscript`-Store 之容器全量）得之，**⛔ 由款 `1` 之「窮舉」得之**；
發單側於窗間文件擬將 ② 之三元組法**逐字受領為「正解」**，出單前方自捕。

**根因**：「構造上窮舉」須**二者皆由文法生成**——**受詞集**（何者算一個出現）與**分類軸**（該出現屬何形）。
`自誤 411` 攔法 ① 以列舉補列舉；② 以構造補了分類軸，**而受詞集之界定仍停在「我想得到的節點型別」**。
識別字於 Python AST 中不只以節點出現，亦以**擁有者節點之 `str` 欄位**（`keyword.arg`／`arg.arg`／`Attribute.attr`／`alias.name`／`Global.names` 等）
及 **`Constant` 之值**（字串鍵）出現——後者恰為「以字串為鍵之容器」之唯一靜態痕跡。

**族** ＝ `自誤 411` ①（有限列舉充窮舉）之**重踩**（第二度·移至受詞集之層）＋ `自誤 406`／`411` ③（母體內涵之窄化）。

**攔法（四款）**：
① 凡以 AST 普查一名者，「**出現**」一律界定為「**AST 內每一節點之每一欄位值（含 `list` 之元素），凡為 `str` 且逐字等於該名者**」
（`ast.walk` ∘ `ast.iter_fields`）——**⛔ 以任何節點型別之列舉界定**。
② 「**形**」＝ 其值所在之 `(擁有者型別.欄位, 擁有者之父節點型別, 父欄位, ctx)`；**⛔ 另立形之清單**。
③ 凡改換普查之定義者，**新舊二定義之差須二向並報**（`新∖舊` 與 `舊∖新`）並出艙**自洽式**（新定義限於舊之節點型別時須逐位等於舊）。
④ **靜態不可見者**（執行期組出之字串、以變數為名之 `getattr`／下標、`exec`）一律 **loud 具名為該框之自限**，並**同單**指派動態款承擔；**⛔ 以靜態零命中判「無」**。

### 🩸 `自誤 414`　**時序閘以「全程首次呼叫序號」為受詞，而其所欲保證者係「同一執行脈絡內、呼叫點當下」之可得性**

**形**：`W-G.9-304` `§六-3` 停八逐字——「款 `4` 實測於**任一**強制之 (街廓,側)，`_solve_G_one`（`is_corner` 真）之**首次**呼叫序號
**晚於** `_corner_buffer_S` 強制之**首次**呼叫序號 ⇒ 於該處取之**必得空值或他街廓之值**」，並自標「**時序·繫於性質**」。

**徵候**：
① `W-G.9-304R` `§六-4`：`('R4','L')` 之 `_solve_G_one` 首次序號 **`1`**，**早於全程任何**強制呼叫（其首次 **`91`**）
⇒ 該 `1` 號**結構上⛔ 出自**強制呼叫所在之逐街廓迴圈之同一迭代；「`1 ≤ 91`」之成立⛔ 攜帶任何關於強制呼叫點當下之資訊。
② 發單側以 `verify/probes/probe_WG9305_issuer_static.py` 節 B 靜態實測（`verify/stepg_pipeline.py :: _run_step_g_impl`）：
`res` 之 `Store` **`3`** 處全屬巢狀函式 `_advance_block_with_split`；逐街廓 `For` 內，**`13`** 個巢狀具名函式之 **`34`** 處呼叫中位序先於最末一處強制呼叫者 **`0`**
⇒ 同一迭代內，強制呼叫之時該值尚未由本迭代產出；其可得與否**只能**繫於跨迭代／跨輪／跨呼叫端之持存容器——**恰為停八之受詞所不區分者**。
③ 後果：`W-G.9-304R` 之「二停機款皆不成就」**易被讀為「可得」**；窗間文件亦將停八列為「已閉」而另立待決前提——**其數已閉，其射程未閉**。

**根因**：時序之比較**未先界定其執行脈絡**（哪一次外層呼叫之哪一迭代之哪一 (街廓,側)）；
全程序號把**不同呼叫端**（不同管線階段）與**不同輪次**之呼叫排入同一序列，其「首次」係**代理量**。
閘之自標「繫於性質」**未附反例構造**——若附「閘綠而性質不成立」之例（前一階段已算出、本迭代強制呼叫時不在任何可取之處），當場可見其不繫。

**族** ＝ `自誤 381`／`自誤 376`（受詞係代理量或僅一支所具之性質）之**重踩**；其所欲攔之形即 `W-G.9-280_補令一` 所鑄之「呼叫時點尚未賦值或已被替換」之形。

**攔法（三款）**：
① 凡時序閘，須**先具名其比較之執行脈絡鍵**（至少：外層呼叫之進入序號、迭代之識別、(街廓,側)），並以**產生指令**取得之；**全程序號只准作輔助欄、⛔ 作判準**。
② 凡閘自標「**繫於性質**」者，須於同格寫出「**閘綠而性質不成立**」之反例構造，並證其於該閘之受詞下不可能；**不能證 ⇒ 該閘標為「代理」·loud**。
③ 「可得性」之閘一律**以值之實存為受詞**（於呼叫點當下之可及物中搜該值）；**⛔ 以任何先後關係代之**。

<!-- ZW413-END -->

<!-- PITBN-BEGIN -->

### 🕳 坑 `bn`　**落檔 `CRLF` 之第二來源：子行程 `sys.stdout` 之文字層**

**形**：父行程已以 `open(p,'wb')` 落檔，而**子行程之 `sys.stdout`** 於 Windows 文字層仍將 `\n` 譯為 `\r\n`；
`sys.stdout.reconfigure(encoding=…)` **⛔ 改其 `newline`**。

**徵候**：`W-G.9-304R` 自捕 `2`——`verify/out/WG9304R_static.log` 首版全檔 `CRLF`（`CR` `216`）；
其首版 `17363` B 與修後 `17147` B 之差 **`216`**，**恰等於**修後入倉版之 `LF` 數 `216`（該版 `CR` `0`·取 blob bytes）⇒ **自洽**。

**根因**：文字層之**編碼**與**換行譯碼**係二參數；只設其一，即以為已控其輸出之位元組。「已 `wb`」只控父行程之寫入層，⛔ 控子行程之文字層。

**攔法（三款）**：
① 凡以 `stdout` 落檔之器，一律 `sys.stdout.reconfigure(encoding="utf-8", newline="\n")`（**二參數並設**）。
② 落檔後一律**以 bytes 量 `CR`** 並出艙（判別力[必非零] ＝ `data/V6.dxf`）。
③ **⛔ 以「父行程已 `open(p,'wb')`」充「落檔無 `CR`」**。

### 🕳 坑 `bo`　**欄之標籤與其實際量測之受詞不符**

**形**：出艙一欄，其**標籤**所稱之範圍或性質，與**產生該欄之運算式**實際所量者不同。

**徵候（三例·皆實測）**：
① `W-G.9-304R` 自捕 `3`：靜態器印「款 `2` 之容器鍵是否**在該函式內出現**」，其實作為 `k in SRC[f]`（**全檔**包含檢）。
② `W-G.9-304R` 自捕 `5`：收工閘 `5` 之「本批**新增**之 `.md`」以 `git diff --name-only`（＝**異動**·含修改）量得 `5`，純新增實為 `2`（`--diff-filter=A`）。
③ **發單側親犯**（`W-G.9-305` 出單前自捕）：`verify/probes/probe_WG9305_issuer_static.py` 初稿節 B，
於「於本 For 內定義之巢狀具名函式 ⇒ `11` 個」之次列印「其 Name 形呼叫 ⇒ `34` 處」——該 `34` 之受詞實為 **`13`** 個巢狀具名函式（含 `For` 外定義之二者）；
同節另一欄「巢狀具名函式之定義位序先於首處強制呼叫者」之受詞實為**該 `11` 個**。二欄皆已改標籤、數未變。

**根因**：標籤於**設計時**寫下，運算式於**實作時**寫下；二者之對應**無機械檢**，且標籤讀來合理時最不受疑。
「其」「本」「新增」「函式內」等**指代詞與範圍詞**，最易在二處之間悄悄換了受詞。

**攔法（三款）**：
① 凡出艙一欄，其**標籤之逐字**須與**產生該欄之運算式**逐項對照後方得出艙；**標籤含範圍詞**（「函式內」「新增」「本 X 內」）或**指代詞**（「其」「上開」）者，須於同格具名其指涉之集合**與其基數**。
② 同一集合於相鄰二欄以不同基數出現者（如 `11` 與 `13`），須**併列其差**並具名差之成員。
③ **⛔ 以「數對了」充「標籤對了」**——數可巧合，標籤之受詞仍錯。

<!-- PITBN-END -->

**落地後之機驗**：以**器本身**量 ⇒ 自誤 相異 **`404`**／MAX **`414`**；`413`／`414` 各命中 **`1`**；
坑 **`93`／`93`**·末標籤 **`bo`** ⇒ 下一 **`bp`**·`bn`／`bo` 可解析 `True`；
🔒 **標題形之檢須用 C 形** `` `自誤 N` ``（⛔ B 形）；`ALPHA_LABELS` 成員數 **`+2`**、尾二元 ＝ `bn`／`bo`（**先實測後填**）、
該檔 `git diff --numstat` ＝ **`1` 增／`0` 刪**；哨兵 `ZW413`／`PITBN` 入簿命中皆 **`0`**；
**三框交叉誤中**（自誤框·坑框·`K-9` 框）皆 **`0`**（分列並報）；append-only 二造 ＋ `wg942_append_audit.py` `rc = 0`。

---

## `§五`　工項三：`GB-170` 之末端追加（主線·落點 ＝ `docs/reports/W-G.4_泛用阻塞項登記表.md` **檔末追加**·⛔ 上文一字不刪·🛑 **`§四` 入倉後方得辦**）

🔑 本 payload **⛔ 鑄任何號**（`戒 36`）⇒ 其形**逐字保留 `> `**；界 ＝ `<!-- GB305-BEGIN -->`／`<!-- GB305-END -->`。
🔒 **`GB-132` 之避讓**：凡**以 `#` 起首**之列，其列內**⛔ 含任何 `GB-` 之號**。

<!-- GB305-BEGIN -->

---

## 🔧 路丙落點之**第四度現查** ＋ 停八射程之更正 ＋ 放行動用紀錄之更正（`W-G.9-304R`／`-305`·⛔ 解除、⛔ 收窄·純末端追加）

🛑 **本節⛔ 鑄任何號**（`戒 36`）；⛔ 改任何原節一字、**⛔ 解除、⛔ 收窄任何阻塞項**。

> **`W-G.9-304R` 之實測**（`run_verification` 全量一次·量測器自身欄 `0`／`0`）：`_first_corner_alloc_dir(side_mid)` 所算之向，
> 經 `_r['_alloc_dir_used']`（**回傳值**·鍵為**字串常數**·⛔ 含街廓識別）出艙，其消費端於生產碼 `34` 檔實測 **`5`** 處讀；
> 停七 ✅ 不成就；停八 ✅ 不成就（`('R2','L')` `19 ≤ 213`／`('R4','L')` `1 ≤ 91`）；
> 強制呼叫端（`verify/stepg_pipeline.py :: _run_step_g_impl`）之 `f_locals` 中，`res`／`_near_dir_left`／`_near_dir_right`／`_alloc_dir_used`
> **四名皆⛔ 出現**（`21` 次逐次皆然）；其當場唯一在域之向 ＝ `allocation_dir_block`。
> **發單側之裁（`W-G.9-305 §零-2` 裁 `2`·鑄 `自誤 414`）**：停八之受詞 ＝ **全程首次呼叫序號**，混入不同呼叫端與不同輪次
> ⇒ **代理量**；`('R4','L')` 之首次序號 `1` 早於全程任何強制呼叫即其直證 ⇒ **停八之「不成就」⛔ 及於「強制呼叫點當下同一 (街廓,側) 之值是否已可取」**。
> **次一受詞（`W-G.9-305` 工項四）**：該值自其產生處至強制呼叫點之**可達性**——以**二根集**（函式體可及者／呼叫端框可及者）**逐次**、以**值之實存**現查。
> 🔧 **放行動用紀錄之更正（⛔ 追改上文一字）**：上文 `W-G.9-299` 節所載「KL 之放行於 `W-G.9-299` 首次動用」**未發生**——
> `W-G.9-299_補令一` 逐字「其動用移至新窗（`W-G.9-300`）」；`W-G.9-300R` 逐字「KL 之放行**仍未動用**」；其後各節皆載「仍未動用」
> ⇒ **KL 之放行（`2026-09-15`）迄今未動用**；以本節為準。
> 🛑 **KL 之放行仍未動用**；`verify/W-G.9-299-gb170` **⛔ 開**；生產碼 `34` 檔**一字未改**；`K-9-30` ⬜ **未實作**；
> **失效條件 `(2)`／`(3)` 仍未成就**——⛔ 解除、⛔ 收窄、⛔ 提修法主張。

<!-- GB305-END -->

**落地後之反向機驗**（`自誤 402` 攔法 ④·**三形分列並報**·框**自器碼當場取**）：聯集 MAX **須仍 `170`**、
相異 **須仍 `168`**、缺號 **須仍 `[12, 87]`**；判別力[必命中] ＝ `GB-170` 之既有定義列於三形至少一形須 `True`／
[必為零] ＝ **執行期組出**之人造號於三形皆須 `False`；二形以上皆 `0` 須 **loud 具名**。
併驗 `GB-132` 避讓：本 payload 內 `^#` 起首且含 `GB-` 者 ＝ **`0`**（判別力[必非零] ＝ 同一偵測器掃 `GB` 簿全檔）。

---

## `§六`　工項四：**已算之向於強制呼叫點之可達性現查（二根集·值空間）**（主線·**零生產碼**·🛑 **含二停機款 ＋ 不可判款**）

🔑 **明文授權三項手段**（射程逐字·⛔ 逾之）：
① **執行 `run_verification` 全量一次**（**⛔ 改生產碼一字**·**等待綁行程結束**·⛔ `| tail -N`·🛑 **其執行期間⛔ 動受測物**）；
② **於 `verify/probes/` 新增量測器**（**⛔ 動既有探針一字**）＋ 其落檔於 `verify/out/`；
③ **於行程內包裝**（⛔ 動任何檔·**包裝冪等**·`W-G.9-304R` 之體例）：`ns` 之三鍵 `_corner_buffer_S`／`_solve_G_one`／`_first_corner_alloc_dir`，
及模組 `verify/stepg_pipeline.py` 之屬性 `_run_step_g_impl`（**僅供計其進入序號**）。**各包裝之觸發數須出艙且 `≥ 1`**（[必非零]）；任一為 `0` ⇒ **loud、判器紅、停**。

### 六-1　本項之由（**發單側具名·⛔ CC 推定**）

`§零-2` 裁 `2`：停八之「不成就」⛔ 及於呼叫點當下之可得性。`§三` 期值 `B-res`／`B-ord`：同一迭代內，強制呼叫之時本迭代尚未產出該值。
⇒ **可得與否只能繫於跨迭代／跨輪／跨呼叫端之持存物**——而其**是否存在、存於何處、以何鍵存之**，靜態不可判。
⇒ 本項**只問一事**：**於每一次強制呼叫之當下，同一 (街廓,側) 先前已算之向，是否實存於二根集之可及物中；若存，其路徑之鍵是否含該街廓與該側。**
🛑 **⛔ 判落點、⛔ 判可施或不可施、⛔ 擬任何改法或 diff、⛔ 改生產碼一字、⛔ 開分支。**

### 六-2　逐款（**母體以產生指令／執行期界定**·**⛔ 抽樣**·`自誤 413`／`414` 攔法）

| 款 | 受詞 | 附款 |
|---|---|---|
| `1` | 🔑 **產出集 `P`**（全量）：① `ns['_first_corner_alloc_dir']` 之**每一次回傳值**；② `ns['_solve_G_one']` 之每一次呼叫中 `is_corner` 為真者，其回傳之 `_alloc_dir_used`。每筆記：全程序號／**`_run_step_g_impl` 之進入序號**（無則記「外」）／街廓／側（原值·正規值）／值（逐分量 `float.hex`）／**產生脈絡**（呼叫鏈之 `(co_filename 相對路徑, co_name, co_firstlineno)` 序列，至 `verify/run_verification.py` 之框止） | ①之側與 `is_corner` 一律取**其所在之 `_solve_G_one` 呼叫之實參本身**（以包裝器之呼叫堆疊歸屬·⛔ climb `f_locals`）；街廓之取得沿 `W-G.9-304R` 之多鍵並取法，**命中鍵與第二鍵並報**；🛑 ① 之筆數、② 之筆數、①⊆② 之歸屬分布**皆出艙**（⛔ 預設其關係） |
| `2` | **逐次強制呼叫**（`ns['_corner_buffer_S']` 之**全部**呼叫·⛔ 抽樣）：全程序號／進入序號／街廓（`_label` 實參逐字 ＋ 呼叫端框之街廓鍵·**二者並報**）／`side` 實參／呼叫端框之 `(co_filename, co_name, co_firstlineno)` | 呼叫端框之 `co_name` ≠ `_run_step_g_impl` 者 **loud 具名**（⛔ 略） |
| `3` | 🔑 **二根集之走訪**（每一次強制呼叫**各走一次**）：**(體)** ＝ 八形參之實值 ∪ **原函式**之 `__globals__`（須自證其與 `harvest` 所回之 `ns` 為同一物·以 `is` 判·⛔ 出艙 `id`）；**(端)** ＝ 呼叫端框之 `f_locals` ∪ `f_globals`。**穿越規則**：穿越 `dict`（鍵與值）／`list`／`tuple`／`set`／`frozenset`／`types.SimpleNamespace`／一般物件之 `__dict__`／`numpy` 之 `object` 型陣列元素／`pandas` 之 `DataFrame`・`Series` 之元素（唯讀取值）；**⛔ 穿越** `module`／`type`／函式・方法・`code`・`frame`・`generator`（其數出艙）；**葉** ＝ `str`／`bytes`／數值／`bool`／`None`／`numpy` 非 `object` 陣列／`shapely` 幾何；🔑 **其餘一切型別 ⇒「未穿越」登記**（型別名·次數·首見路徑）——**此登記即本款之構造上窮舉**（凡未明列者必落其中） | **候選葉** ＝ 長度 `2` 之 `tuple`／`list` 且二元皆為浮點，或 `size == 2` 之浮點 `ndarray`；**比對** ＝ 與 `P` 中**全程序號早於本次**之各筆，於四變換 `(x,y)`／`(−x,−y)`／`(−y,x)`／`(y,−x)` 下**逐分量位元相等**；每一命中記：**路徑**（鍵鏈逐字）·變換·所命中之 `P` 筆（序號·進入序號·街廓·側）。🔒 `id(·)` **僅准**作單次走訪內之已訪集合（**⛔ 出艙·⛔ 作錨**）；**節點上限**由受單側於器內明文並出艙，觸限 ⇒ 該次「**截斷**」 |
| `4` | 🔑 **逐次之判定表**（`21` 列或實測之列數·**全量**） | 每列：`|P同|`（同 (街廓,側正規)·序號早於本次）分列為「同進入序號」／「前進入序號」／「外」三欄；**(體)** 同命中數／他命中數；**(端)** 同命中數／他命中數；**鍵口徑可信**之同命中數（路徑之鍵鏈中**同時**含一元素逐字等於本次之街廓、及一元素屬本次側之詞彙 `{left,right,左側,右側,L,R}` 之同側者）；截斷；未穿越之型別數 |
| `5` | **判別力五造** | [必為 `34`] 外部錨（坑 `bj`）／[必命中] **合成根**（器內自建之 `{街廓: {側: P同之一筆之複本}}`·⛔ 可經任何生產物抵達）以同一走訪器搜之 ⇒ 同命中 `≥ 1` 且鍵口徑可信 `≥ 1`／[必為零] 以 `numpy.nextafter` 擾動一分量之值充 `P` 搜同一 **(體)** ⇒ `0`／[器自身須 `0`] 命中路徑經過器所擁有之物者之數（其**判別力**：合成根內刻意置入器之記錄容器 ⇒ 該數 `≥ 1`·⛔ 以恆為 `0` 之欄充造）／[必非零] 三包裝與進入序號計數器之觸發數 |

### 六-3　🛑 **停機款與不可判款**（**逐次分列**·任一格成就即成就·⛔ 以「多數格不成就」充不成就）

> **停九（可得性·繫於值之實存）**：於任一次強制呼叫，**截斷 ＝ `0` ⋀ 未穿越 ＝ `0`**，而 **(體) ∪ (端)** 之同命中 ＝ **`0`**
> ⇒ 該次之同一 (街廓,側) 先前已算之向**⛔ 實存於任何可及物** ⇒ **停、上呈**。
> 🔒 其分項成因須分列：**(i)** `|P同| ＝ 0`（全程尚無此產出）／**(ii)** `|P同| ≥ 1` 而未被任何可及物持存。
>
> **停十（鍵之口徑·繫於性質）**：於任一次強制呼叫，同命中 `≥ 1` 而**鍵口徑可信之同命中 ＝ `0`**
> ⇒ 其值之取得只能**依位置或時序**而非依鍵 ⇒ 換一迭代即取得他街廓之值（**同一路徑於他次呼叫之他命中須併出艙以證之**）⇒ **停、上呈**。
>
> **不可判款**：於任一次強制呼叫，同命中 ＝ `0` 而**截斷 `> 0` 或 未穿越 `> 0`** ⇒ 該次**⛔ 判停九成就或不成就**；
> **loud 具名其未穿越之型別與截斷之處**、**停、上呈**（⛔ 擴穿越規則以求綠、⛔ 調高上限重跑——其授權候發單側）。

🛑 **二根集須分列並報**——任一根集之同命中 `≥ 1` 皆**⛔ 據以判落點**。
🛑 **四禁仍在**（`W-G.9-301 §六-3` 逐字）：**⛔ 新增形參、⛔ 改簽章、⛔ 新增 `import`、⛔ 自寫第二套幾何**。

---

## `§七`　收工閘（**報告入倉後量**·嚴格末端追加·🛑 **落檔 `open(p,'wb')`**）

| # | 受詞（指令） | 期／判準 |
|---|---|---|
| `1` | `git show --numstat <各 commit>` 逐檔具名 | 刪除欄（`deletions`）**全 `0`** |
| `2` | 生產碼判法·母體**正面列舉 `34` 檔** | 逐區間 **`0` 行**；對照組[必非零] `17fd981^..17fd981` ＝ `≥ 1` |
| `3` | `.md`／`.py` 之 `CR`（框 ＝ 倉內 blob·**取 bytes**） | **`0`**；判別力[必非零] ＝ `data/V6.dxf` |
| `3'` | **本批新增之 `.log` 之 `CR`** | **`0`**（坑 `bn` 攔法 ①）；🔒 `WG9303R6_*.log` 四份 **⛔ 修**·⛔ 判紅 |
| `4` | 四簿期末（**器之輸出**） | 自誤 相異 **`404`**／MAX **`414`**（＋**二**）；`K-9` `29`／`30`·`GB` `168`／`170`·`VR` `80`／`95` **一字未動** |
| `5` | 坑之期末（**器之輸出**） | **`93`／`93`**（＋**二**）·末標籤 **`bo`** ⇒ 下一 **`bp`**；母體 `.md` 檔數：期初以 `git ls-tree -r --name-only -z <開工 rev>` ⋂ `*.md` 取（**⛔ `--with-tree`**·坑 `bl`·於 `96a8204e…` 發單側實得 `819`），增量 ＝ `git diff --name-only --diff-filter=A` 之 `.md` 數（坑 `bo`） |
| `5'` | `wg9223_acceptance_audit.py <本單> <本報告>` | 命中 `0` 之字樣 ＝ `0`；🛑 判定組之基數**由該指令得**·**⛔ 預書** ⇒ **機械順序**：佔位符 ⇒ 跑 ⇒ 填；受詞係 `index` ⇒ 復跑前先 `git add` |
| `6` | 自限復驗 | `34` 檔 blob 期初＝期末**相異 `0`**（判別力[必相異] ＝ 本批確有異動之檔）；`app.py` ＝ `4379108a…`；`baselines` `298` 檔·`a898f4e1…`；`p3a` `rc = 1`；`WV_BAKE` ＝ `None`；`GB-79`／`167`／`168`／`169`／`170` **⛔ 修**；`K-9-30` 亦⬜ **未實作**；**物證落檔**（`§一` 項 `11` 之 `19` 檔 ＋ 本批新增之落檔）blob **逐位未動** |
| `6'` | `git ls-remote origin 'refs/heads/verify/*'` | `verify/W-G.9-299-gb170` 命中 **`0`**；判別力[必存在] `p3a` 命中 **`1`** |
| `6''` | **本波九單之在倉性**（`§一` 項 `10` 之產生指令） | **`9`** **皆態1**；判別力[必為零] ＝ 一人造路徑須 `rc ≠ 0` |
| `6'''` | **逐款回掃之出艙**（坑 `bm` 攔法 ②） | 本報告內**全部**「某框／某法有 X 缺陷」之警告，逐項及其對**後續各款**之回掃結果（**逐項**·⛔ 只報「已回掃」） |
| `6''''` | 🆕 **標籤對照之出艙**（坑 `bo` 攔法 ①） | 本報告**全部**含範圍詞或指代詞之欄，逐欄具名其指涉之集合與基數 |
| `7` | `git ls-remote origin refs/heads/wip/s1-endpart`（`push` **後**） | 🔒 **出艙於回報·⛔ 入倉** |

---

## `§八`　🛑 **⛔ 為之事**

🔑 **本批已明文授權者**（射程逐字見 `§三`／`§四`／`§六` 首段·⛔ 逾之）：新增 `probe_WG9305_issuer_static.py`（逐字）；擴 `ALPHA_LABELS` 至 `bo`（**僅新增一列**）；
`run_verification` 全量**一次**；`verify/probes/` **新增**量測器；行程內包裝 `§六` 所列之四物。
其餘：
⛔ 改生產碼 `34` 檔**一字**；⛔ 開任何分支；⛔ 動用 KL 之放行；⛔ 辦修批；⛔ 自續 `W-G.9-306`；
⛔ 併線（含 `p3a`）；⛔ 刪任何 ref；⛔ 覆寫 `verify/baselines` 任一檔或**任一物證落檔**；⛔ `WV_BAKE`；**⛔ 引任何自 baseline 取得之數**；
⛔ 改任何函式簽章、⛔ 新增任何形參、⛔ 新增任何 `import` 於生產碼、⛔ 改任何 `*_EXPECT` 一字；
⛔ 自寫第二套幾何或第二份 `W`／`side_mid`／側界線／街廓識別之定義（`GB-48` 族）——`§六` 之走訪**只比對既有之值**、⛔ 重算任何向；
⛔ 動 `probe_WG9269_pit_index.py` 之**任何既有列**；⛔ 動任何**其他既有**探針一字；
⛔ 鑄 `GB`／`VR`／`K-9` 之任何號（**`自誤 413`・`414` ＋ 坑 `bn`・`bo` 為本批唯一之鑄**）；
⛔ 解除或收窄任何 `GB`（含 `GB-170`）；⛔ 落地 `K-9-30`／`K-9-5-*`／`K-9-12`／`K-9-29` 之任何子項；
⛔ 修 `W-G.9-303R6` 之四份 `.log`；⛔ 追改任何已入倉文件一字（含 `GB-170` 之 `W-G.9-299` 節之該句）；
⛔ 擴 KL 放行之射程；⛔ 呈 KL；⛔ 擬第二次放行之呈文；
⛔ 判 `GB-170` 可否解除、⛔ 判路丙之落點可施與否、⛔ 判落點應在函式體或呼叫端、⛔ 擬任何 fallback 之實作形、⛔ 判孰是、⛔ 判孰誤、⛔ 提修法主張；
⛔ 於 `§六` 之不可判款成就時自擴穿越規則或自調節點上限重跑；
**⛔ 估算或出艙本窗 context 之百分比**（`自誤 410`）——惟遇**可觀測之硬限事件**（行程被截／輸出被截／配額用罄）一律 loud 照實具名該事件逐字、停、上呈；
⛔ 於任何入倉文件宣稱一件尚未發生之事（及於 `commit` 訊息與「已推送」之陳述）。

---

## `§九`　報告之格

`§二` 工項零（**先於開工閘**）⇒ `§一` 開工閘（十二項）⇒ `§三` 工項一（靜態器·**期值逐項對拍表**）⇒
`§四` 工項二（`自誤 413`・`414` ＋ 坑 `bn`・`bo` ＋ `ALPHA_LABELS`·**三框交叉誤中分列**）⇒ `§五` 工項三（`GB-170`·**反向機驗**）⇒
`§六` 工項四（逐款表以落檔**全量**出艙·⛔ `\| tail -N`·**停九／停十／不可判款逐次分列**·**二根集分列**）⇒
收工閘（**入倉後末端追加**·含 `3'`／`6''`／`6'''`／`6''''`·閘 `7` **出艙於回報·⛔ 入倉**）⇒
`⛔ 為之事` 之逐項自檢 ⇒ 逐 `commit`（**全 `40` 碼**）。
🔒 凡出艙之數，同格載其**框、母體與產生指令**，且該指令須**逐字原樣執行過**（`自誤 409`）；
**母體一律以產生指令界定**（`自誤 406`）；**「出現」以構造上之定義界定**（`自誤 413`）；**時序比較先具名執行脈絡**（`自誤 414`）；
**摘要值一律逐字具名其產生指令**（`自誤 405`）；框無 `^` 錨者**二數並報**；**母體之基數綁外部錨**（坑 `bj`）；**欄之標籤與運算式逐項對照**（坑 `bo`）。
🔒 判定組為空一律 **loud 拒測**並**照實具名**；自捕為零者須併具「**⛔ 讀為『本批無誤』**」。
🔒 凡自捕一律於出艙前攔下、照實併記（**⛔ 頂替**·**⛔ 鑄號**·鑄號候發單側）；物證落檔**保全⛔ 覆寫**。
🔒 **凡「⛔ 預書」之款一律行機械順序**（佔位符 ⇒ 跑 ⇒ 填）；**出件前逐款回掃本文件之全部警告**（坑 `bm`）。

🛑 **辦畢 ⇒ 出報告 ⇒ 停。⛔ 呈 KL。**

---

【驗收】本批之驗收固定項（**⛔ 推後·⛔ 以「未觸」充綠**）：
`ls-remote`／`SELF_SHA256`／`preflight`／`acceptance_audit`／`deletions`／`cat-file`／`merge-base`／
`append_audit`／`P305S`／`ZW413`／`PITBN`／`GB305-BEGIN`／`ALPHA_LABELS`／`ls-tree`／
`probe_WG9305_issuer_static.py`／`_solve_G_one`／`_corner_buffer_S`／`_first_corner_alloc_dir`／`_run_step_g_impl`／
`_advance_block_with_split`／`_alloc_dir_used`／`__globals__`／`f_locals`／`float.hex`／`nextafter`／
`co_firstlineno`／`run_verification`／`baselines`／`numstat`／`sha256`／`WV_BAKE`／`W-G.9-299-gb170`／`p3a`。

【單止】本單受詞 ＝ CC 施工窗。發單側 ＝ `claude.ai`。**⛔ 呈 KL。**

SELF_SHA256: 61531899d513e031dd799ae7323dad18214f2c3fa6f5a93231e4881a7ab3552d
