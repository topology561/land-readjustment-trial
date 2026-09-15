# `W-G.9-303R6`　補令六（新窗首則·起手單）執行報告

> **受詞** ＝ `docs/orders/W-G.9-303_補令六_新窗首則與起手單.md`（本窗自倉讀單）。
> **分級** ＝ **重**（現查 ＋ `run_verification` 全量·**零生產碼**·⛔ 開分支·⛔ 修批）。
> **本批⛔ 鑄任何號**（自誤／`GB`／`VR`／`K-9`／坑 皆⛔）——自捕照實併記，鑄號**候 `W-G.9-304`**。
> **⛔ 出艙本窗 context 之百分比**（`補令六 §零-5`）；本批未遭遇任何資源硬限之可觀測事件。

---

## `§二`　工項零：本補令原封入倉（**先於開工閘**）

**取檔路** ＝ **甲**（主檢出工作區之**未追蹤**檔）。

### 一　入倉前之釘死 —— 🛑 **loud 拒測**（⛔ 判綠·⛔ 判「不符」）

| 項 | 產生指令 | 值 |
|---|---|---|
| 源之 bytes | `wc -c < <源>` | **`18715`** |
| 源之 `CR`／`LF` | `python -c "b=open(p,'rb').read(); b.count(b'\r')"` | `CR` **`0`**／`LF` `221` |
| 源之內容 `sha256` | `sha256sum <源>` | `e9176721c492628bb0b4ef78a1905eb85b67bfa61093df68c2cee7208afb248f` |
| **期值（KL 交付時之回報）** | —— | 🛑 **⛔ 載**（KL 之訊息僅含檔路徑） |

🛑 **⇒ 該款之判定組為空 ⇒ `loud` 拒測**：「**無從回測**」⛔ 等同「回測不過」
（`CLAUDE.md`「`序 11` 之一般化」款 `三`）。⛔ 以「未觸」充綠。

🔒 **傳輸保真改由 `SELF_SHA256`（`P-5`·**發單側所出之單載值**）承擔**，並附**否證對照**：

| 造 | 受詞 | 實得 | 期 | 判 |
|---|---|---|---|---|
| **[必綠]** | 原封交付檔 | `SELF_SHA256` ✅ 相符（受詞 `18637` B·實算 `841760a6e1bc93e9…`／單載 `841760a6e1bc93e9…`） | 相符 | ✅ |
| **[必紅]** | **受詞區間內**竄改 `1` 位元組 | 🔴 不符（實算 `39fbe40d7364e165…`／單載 `841760a6e1bc93e9…`） | 不符 | ✅ |

⇒ 該檢**非恆綠**；`18715` B 中之 `18637` B 由發單側所出之值背書，其餘 `78` B **即該 `SELF_SHA256:` 列本身**（`13 + 64 + 1`），其值已與實算逐位相符。
🔒 **射程之照實**：此仍**⛔ 證**「發單側送出之原文 → 落檔」之保真——`CLAUDE.md`「作業常規之追加四」之**射程界限**已逐字預告該缺口（「來源係聊天訊息、無獨立 `sha256` 可比…欲使該閘及於全鏈，**發單側須於單內同格載其送出時之 `sha256`**」）。

### 二　落檔與入倉後之出艙

| 項 | 產生指令 | 值 | 判 |
|---|---|---|---|
| 落檔逐位 ＝ 源 | `shutil.copyfile` 後 `bytes` 比對 | `True`（`18715` B） | ✅ |
| **blob `sha1`** | `git rev-parse HEAD:<路徑>` | `44a0ddaff4fd8c92bc9fda3efc1cc7731b8fa5b8` | —— |
| **blob 內容 `sha256`** | `git cat-file blob HEAD:<路徑>` ⇒ `sha256` | `e9176721c492628bb0b4ef78a1905eb85b67bfa61093df68c2cee7208afb248f` | ✅ **二框並報** |
| blob ＝ 磁碟 ＝ 源 | 三者逐位 | `True` | ✅ |
| `CR`（**讀 blob 取 bytes**） | `git cat-file blob` ⇒ `count(b'\r')` | **`0`** | ✅ |
| 判別力[必非零] | `git cat-file blob HEAD:data/V6.dxf` ⇒ `CR` | **`12308`**（全長 `88341` B） | ✅ |
| `deletions` | `git diff --numstat <base> <head>` | `+221 / -0` ⇒ 合計 **`0`** | ✅ |
| 受詞自證（坑 `bf`） | 落點字串 | 含 `補令六` ＝ `True`[必真]／含 `補令五` ＝ `False`[必偽] | ✅ |
| 檔數 ＝ `1` | `git diff --name-only -z <base> <head>` | `['docs/orders/W-G.9-303_補令六_新窗首則與起手單.md']` ⇒ `1` | ✅ |
| 造甲[必≥1] | `git cat-file -e HEAD:docs/orders/W-G.9-303_補令五_舊窗收工批與自誤410.md` | `rc = 0` ⇒ 存在 | ✅ |
| 造乙[必為0] | `git cat-file -e HEAD:<執行期組出之人造名>`（字面⛔ 出艙） | `rc = 128` ⇒ 不存在 | ✅ |
| 生產碼判法 | `git diff --name-only <base>..<head> \| grep -xE 'app\.py\|verify/stepg_pipeline\.py\|verify/run_all\.py\|verify/run_verification\.py'` | **`0`** 行（`rc = 1`） | ✅ |
| 對照組[必非零] | 同 pattern 掃 `git ls-tree -r --name-only HEAD` | **`4`** 行 ⇒ `['app.py','verify/run_all.py','verify/run_verification.py','verify/stepg_pipeline.py']` | ✅ |

⇒ **零生產碼 commit** ⇒ `常規一` 補款：**逕行 `push`**。
`git push origin HEAD:refs/heads/wip/s1-endpart` ⇒ `dbc5b1d..b688ad1` ⇒ `rc = 0`。

🛑 **`W-G.9-303` `§二` 工項零⛔ 重辦**——已由 `補令二 §二` 代行，其 `commit` 全 `40` 碼 ＝
**`bb742f8d13f90269ecd805ad9eb79ce4c35b6767`**；本窗當場自倉復現其二框：
blob `sha1` ＝ `8c85fc1ccdf781ce08c10ba397038bfe97c50238`（`22313` B）／
blob 內容 `sha256` ＝ `460779b22a491bc8132f424525ebab1df308eca1944e5a81483391244d568142`
——**與 `補令六 §零-4` 所載逐位相符**。

---

## `§一`　開工閘（**跑於 `§二` 之後**·每列同格載其產生指令）

🩸 **偏離之照實併記**：`0-a`／`0-b`／`0-c` 於 `§二` 落地**前**曾以**偵察**身分預跑一次；
本節之值係 `§二` 落地**後**如式重跑所得。⛔ 頂替、⛔ 以預跑之值出艙。

### 一-1　倉內 `303` 單 `§零` 之十一項（期值依 `補令六 §零-3` 取代）

| # | 產生指令（逐字） | 實得 | 期 | 判 |
|---|---|---|---|---|
| `1` | `git ls-remote origin refs/heads/wip/s1-endpart` | `b688ad10e56054274c501b0d244b3c6cb196161a` | `4bc9c773…` **或其後裔** | ✅ |
| `1`附 | `git merge-base --is-ancestor 4bc9c77347416ff474f778d24dcc7dc23132f9a0 HEAD` | `rc = 0` | `rc = 0` | ✅ |
| `2` | `git rev-parse HEAD:app.py`（框 ＝ blob `sha1`） | `4379108a4856714078c410ff4e6291ecfdf6d2c1` | 同左 | ✅ |
| `3` | `git merge-base --is-ancestor 05a11bd665f6c2790ff821c9e3a1606651e345d4 HEAD` | `rc = 1` | **非**祖先（`rc = 1`） | ✅ |
| `4` | `python verify/probes/probe_order_preflight.py <倉內 303 單之倉外暫存檔>` | 🔴 機械款 **`0`** 項；`P-5` ✅ 相符（受詞 `22235` B）；`P-3` 不紅 | 同左 | ✅ |
| `4'` | 受詞自證（坑 `bf`）：器所印之檔名 ＝ `W-G.9-303_單.md` | 含 `W-G.9-303` ＝ `True`[必真]／含 `W-G.9-302` ＝ `False`[必偽] | 同左 | ✅ |
| `5` | `… probe_order_preflight.py --selftest`；`python verify/tools/wg9223_acceptance_audit.py --selftest` | 二器 `rc = 0`；preflight **四靶逐項成立** | 同左 | ✅ |
| `6` | `python verify/probes/probe_WG9267_issuer_measurers.py registry` | 自誤 相異 **`400`**／MAX **`410`**（缺 `[106,355,356,357]`）｜`GB` `168`／`170`（缺 `[12,87]`）｜`VR` `80`／`95`（缺 `[73,75]`）｜`K-9` `28`／`29`（缺 `[]`） | `§零-3` `A1` | ✅ |
| `6'` | `python verify/probes/probe_WG9269_pit_index.py` | **`90`／`90`**·末標籤 **`bl`** ⇒ 下一 **`bm`**；器自印判別力二造 ✅ | `§零-3` `A2` | ✅ |
| `7` | `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py` | **`34`** 檔（`33 + 1`）；判別力[必不命中] 子層 `*.py` ＝ **`316`** > `0` | `34` | ✅ |
| `8` | `git ls-tree -r HEAD verify/baselines \| sha256sum`；`… --name-only \| wc -l` | `a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9`·檔數 **`298`** | 同左 | ✅ |
| `9` | `git ls-remote origin 'refs/heads/verify/*'` | `verify/W-G.9-299-gb170` 命中 **`0`**；[必存在] `verify/W-G.9-269-p3a` 命中 **`1`**（`05a11bd665f6c2790ff821c9e3a1606651e345d4`） | 同左 | ✅ |
| `10` | 物證落檔（清單**自 `交接註_舊窗收工二` 項 `10` 機械抽出**·⛔ 轉錄）：逐檔 `git cat-file -e HEAD:<p>` ⇒ `git rev-parse HEAD:<p>` | **三態分列：態1 `13` ／ 態2 `0` ／ 態3 `0`**；**逐位未動 `True`**（期初 `4bc9c773…` ＝ 期末） | 逐位未動 | ✅ |

🔒 **閘 `10` 之逐檔全量**（`|六物證| = 6`／`|本波新增| = 9`／**聯集 `13`**·重疊 `2`；三數與交接註 `10` 逐位相符）：
`WG9295R_joint_v1_selfpolluted.log` `1a35dc16865576f9`／`WG9296R_w0rec_v1_blknone.log` `f93eb2fcb7e693f8`／
`WG9297R_w0caliber_v1_blkabsent.log` `16742f3805e00161`／`WG9298R_gate3_v1_firstcall.log` `5cef4c8dfe7a6ea6`／
`WG9300R_dynamic.log` `c0233110de1d7dfc`／`WG9300R_dynamic_v1_wrongframe.log` `b3ab88b73dda0cc3`／
`WG9300R_gate6p_pit.log` `bcda31316777789e`／`WG9300R_static.log` `da701732f21a2bc3`／
`WG9300R_static_v1_popcollapse.log` `476aac14eda53ccb`／`WG9301R_pit_post.log` `60c68b15b4291841`／
`WG9301R_selfderive.log` `6860cc92f8d7b902`／`WG9302R_pit_pre.log` `0af63667705be31b`／
`WG9302R_sidesrc.log` `000f046e80546dc6`。
判別力[必為零] ＝ 一**執行期組出**之人造落檔名 ⇒ `git cat-file -e` `rc = 128` ⇒ ✅。

### 一-2　`補令六` 另加之三項

| # | 產生指令 | 實得 | 判 |
|---|---|---|---|
| `0-a` | `python verify/probes/probe_order_preflight.py <本補令之磁碟檔>` | 🔴 機械款 **`0`**；`P-5` ✅ 相符（受詞 `18637` B·實算 `841760a6e1bc93e9…`／單載 同）；`P-3` 不紅；🟡 **`2`** 項（逐項處置見 `一-3`） | ✅ |
| `0-b` | `python verify/probes/probe_order_preflight.py <倉內 303 單之倉外暫存檔>` | `P-5` 實算 **全 `64` 碼** ＝ `37c6c848bc9dd757f69cf3178a02b5ce55d52b4aa2bdd1b60bc4dc074dad4d19`（受詞 **`22235`** B）⇒ 與期值逐位相符；受詞自證 ✅（見閘 `4'`）；暫存檔**⛔ 入倉** | ✅ |
| `0-c` | 七錨之復現：`grep -c -F '<錨逐字>' <倉內 303 單之暫存檔>`（**逐錨各跑一次**·⛔ alternation·錨**自 `補令四` 之 blob 逐字取**·⛔ 經 shell 引號) | 見下表 | ✅ |

🔒 **`0-a` 之單內互斥（`常規二`·⛔ 上呈 KL·發單側當場裁·逐字回報）**：
`0-a` 之期值欄逐字載「其值由 KL 交付時之回報取之·**本補令⛔ 自載·結構上遞迴**」，
而本補令**其實自載** `SELF_SHA256`（其 `:221`），且該值係**前綴雜湊**（受詞 ＝ 檔首至該列前一個 `\n` 含）
⇒ **結構上⛔ 遞迴**。**取保守項續辦** ＝ 逕以該自載值實測 `P-5`，結果**相符**。
🔒 該括號於 `§二` 之「**內容 `sha256`**」為**真**（全檔雜湊自載方為遞迴），於 `SELF_SHA256` 為**偽**——二者異物。

#### `0-c` 七錨（**逐錨分列**·錨 bytes 併報）

| 錨 | 錨 bytes | 命中 | `rc` | 期 | 判 |
|---|---|---|---|---|---|
| `A1` | `57` | `1` | `0` | `1` | ✅ |
| `A2` | `88` | `1` | `0` | `1` | ✅ |
| `A3` | `61` | `1` | `0` | `1` | ✅ |
| `A4` | `63` | `1` | `0` | `1` | ✅ |
| `A5` | `71` | `1` | `0` | `1` | ✅ |
| `A6` | `36` | `1` | `0` | `1` | ✅ |
| `A7` | `87` | `1` | `0` | `1` | ✅ |

判別力[必為零] ＝ 一**執行期組出**之人造錨（字面⛔ 出艙）⇒ 命中 **`0`**（`rc = 1`）✅。
判別力[必非零] ＝ 字樣 `自誤` 於同一受詞 ⇒ **列框 `13`**／**字元框 `14`**（**二數並報**·二數**相異** ⇒ ⛔ 定值）✅。

🔒 **取錨之保真**：錨自 `docs/orders/W-G.9-303_補令四_閘9之重立與工項零之序.md`
（blob `sha1` `d709a39879e52d0e86a6001f9ed1a85cd9240626`·`28644` B）之表列**機械抽出**
（框 ＝ `^\| \`A([1-7])\` \| (.*) \| \*\*\`1\`\*\* \|$`·各剝**一個**反引號），
並以 `subprocess` 之 `argv` 直呼 `grep`、**⛔ 經 shell** ⇒ `|` 與反引號**零失真通道**。
⚠️ 該檔另有一組同前綴之表列（`§零-3` 之**四欄**期值表）⇒ 框以**末欄 `**\`1\`**`** 區辨；
二表合計命中 `14` 列，抽出者恰 `7`。

### 一-3　`P-4` 之逐項處置（⛔ 靜默略過·**⛔ 目視**）

🔒 **先查該器之觸發式**（`verify/probes/probe_order_preflight.py` 之 `P-4` 實作逐字）：
> `if ("→" in p) and re.search(r"逐字|轉引|引", p):` ⇒ 若 `not re.search(r"座標系|方向|注入方向|來源.*[:：]|自.*抽出", p)` 則提示。

| 來源 | 起列 | 段內 `→` 次數 | `逐字\|轉引\|引` 之全部命中 | **真受詞** | 歸類 | 處置 |
|---|---|---|---|---|---|---|
| `0-a`（本補令） | `:27` | `3` | `['逐字','轉引','引']` | ① `→` 之**字面**（被引之觸發式本身）② `工項零 → 開工閘 → 其餘工項`（節序） | **(甲)** 流程節序（含**引述**他處之此類串接者） | **具名豁免** |
| `0-a`（本補令） | `:197` | `6` | `['逐字','逐字']` | `§二 → §一 → §三 → §四 → 收工閘 → 自檢 → 逐 commit`（**報告之節序**） | **(甲)** | **具名豁免** |
| `0-b`（倉內 `303` 單） | `:167` | `8` | `['逐字']` | `§零 開工閘 → §零′ → 逐工項 → … → 逐 commit`（**報告之節序**） | **(甲)** | **具名豁免** |

🛑 三項**皆⛔ 幾何向量之方向性轉引** ⇒ **無座標系可具名**；⛔ 有任一項落於三類之外。
🛑 本批**⛔ 出艙任何幾何向量之夾角** ⇒ 「釘槽並以實邊機驗」之附款**無受詞**（⛔ 以「未觸」充綠·此為**判定組為空**之照實具名）。

---

## `§三`　工項一：街廓識別於 `_corner_buffer_S` 內之可信取得

**落檔（全量·⛔ `| tail -N`）** ＝ `verify/out/WG9303R6_static.log`（`236` 列）
＋ `verify/out/WG9303R6_static2.log`（`124` 列·**框補正**）。
**母體之產生指令** ＝ `git ls-tree HEAD --name-only verify/` ⋂ `*.py` ＋ `app.py` ⇒ **`34`** 檔（外部錨 ＝ 閘 `7`）。

### 三-1　款 `1`　`f3_cad_side_lines_by_side` 之寫入端與層① 鍵之源頭

**四形分列**（⛔ 沿用 `W-G.9-302R` 已具名其對 `ast.Dict` 鍵字面有盲區之三形框）：

| 形 | 處數 | 全量逐處 |
|---|---|---|
| `Subscript`（Store） | **`2`** | `app.py :: main` ⇒ `st.session_state['f3_cad_side_lines_by_side'] = (`／`verify/run_verification.py :: build_pipeline` ⇒ `ss["f3_cad_side_lines_by_side"] = slm` |
| `Assign`（裸名） | **`0`** | 🛑 **loud**：該形於母體內無命中（母體 `34` 檔） |
| `.get` | **`23`** | 逐處見落檔（含 `app.py :: _first_corner_alloc_dir`／`select_corner_lots_both_sides_v12`／`_build_wf_ctx`／`_annotate_temp_parcel_cut_type`、`verify/stepg_pipeline.py :: _run_step_g_impl` 等） |
| `Dict`／`DictComp` | **`6`** | `app.py :: parse_cad_precision_layers`（`result = {`）／`app.py :: _build_wf_ctx`／`verify/run_verification.py :: main`／`wg_g1_smoke`／`wg_g2_smoke`／`wg_g3` |

🔴 **二寫入處皆為<u>整表</u>賦值** ⇒ 層① 鍵**⛔ 生於該二處**，須再上溯。

🩸 **自捕（框缺陷·⛔ 頂替）**：單所令之**四形⛔ 涵蓋 `.setdefault`**，而層① 鍵之**真寫入形正是 `.setdefault`**
⇒ v1 器之「源頭」節**零命中**。已以 v2 器加**第五形**補之。

**第五形 `.setdefault`** ⇒ **`1`** 處：

```
app.py :: parse_cad_precision_layers
    逐字     = _by_side_wb = result['side_lines_by_side'].setdefault(_hit_blk, {})
    receiver = result['side_lines_by_side']
    🔑 層① 鍵 = _hit_blk   （AST = Name）
```

**逐層溯至源頭之名**：

```
_hit_blk  ← [Store] _hit_blk, _ov_sl, _rk_sl = _best_block(
                        [(float(p[0]), float(p[1])) for p in _spts], 'SIDE_LINE', sl.get('handle',''))
          🔑 源頭之名 = `_best_block`（Call·其**第 1 位序回傳**）
             定義 :: parse_cad_precision_layers   形參 = ['_pts_l','_layer_nm','_handle']
             層級 = 🔴 **內層閉包**（⛔ 在 `ns` 內）
             Return 逐字 = `_rk[0]['block'], _rk[0]['overlap_m'], _rk` ／ `None, 0.0, _rk`
```

🔒 ⇒ **層① 鍵之源頭 ＝ `_best_block` 之第 1 回傳值**（＝ 以共線重疊最大者判定之街廓名）。

### 三-2　款 `2`　`_corner_buffer_S` 體內可解之名中語義為「街廓識別」者（**全量**）

**母體之產生指令** ＝ `ast.parse(<app.py 之 HEAD blob>).body` 之頂層定義名（`ns` 鍵）∪ `_corner_buffer_S` 之八形參。
`ns` 鍵基數 ＝ **`286`**；形參 ＝ `['block_poly','d_hat','front_p1','allocation_dir','range_area','side','tol','_label']`（**`8`** 個）；
款 `2` 母體基數 ＝ **`294`**。

| 字樣 | 命中 | **全量逐名**（⛔ 只報基數） |
|---|---|---|
| `blk` | **`1`** | `k91_min_alloc_contrib_by_blk`［頂層 `def`：`def k91_min_alloc_contrib_by_blk(min_alloc_area_by_blk, eff_min_build_by_blk):`］ |
| `label` | **`3`** | `_label`［**`_corner_buffer_S` 之第 `8` 形參**］／`bl_pts_by_label`［頂層 `def`］／`n19p_depth_info_by_label`［頂層 `def`］ |
| `lbl` | **`0`** | 🛑 **loud**：無命中；母體基數 `294` |
| `block_id` | **`0`** | 🛑 **loud**：無命中；母體基數 `294` |

🔒 **判別力**：[必為零] 一**執行期組出**之人造字樣（字面⛔ 出艙）⇒ 命中 **`0`** ✅；[必非零] `ns` 鍵基數 `286` ≥ `1` ✅。
🔒 ⇒ 該四命中中，**唯一為「值」者 ＝ `_label`（形參）**；其餘三者皆為**頂層函式名**（⛔ 街廓識別之值）。

### 三-3　款 `3`　`_label` 七處實參之逐處溯源（**⛔ 以名同判物同**）

呼叫點總數（`Name` ∪ `Attribute` ∪ `ns[<字面>]` **三形並取**）＝ **`7`**
——**獨立復現** `W-G.9-301R` 五-5 之四個實參式。

| # | 呼叫端 `檔 :: 函式` | `_label` 實參逐字 | 所含之名 | 該名於**其所在函式內**之賦值來源（產生式逐字） |
|---|---|---|---|---|
| `1` | `app.py :: main` | `blk_label` | `['blk_label']` | `3` 處：`blk_label = tp['所屬街廓']`／`for blk_label, parcels_in_blk in parcels_by_block.items():`／`blk_label = matched.get('所屬街廓', '')` |
| `2` | `app.py :: main` | `blk_label` | `['blk_label']` | 同上 `3` 處 |
| `3` | `verify/stepg_pipeline.py :: _run_step_g_impl` | `blk_label` | `['blk_label']` | `1` 處：`for blk_label, parcels_in_blk in parcels_by_block.items():` |
| `4` | `verify/stepg_pipeline.py :: _run_step_g_impl` | `blk_label` | `['blk_label']` | 同上 `1` 處 |
| `5` | `verify/wf_f1.py :: compute` | `f"{lbl}·F.1"` | `['lbl']` | `1` 處：`lbl = "R1"`（🔴 **字面常數**） |
| `6` | `verify/wf_f4.py :: _reshape_block` | `f"{blk}·E3"` | `['blk']` | `1` 處：**形參**（`def _reshape_block(ns, snap, cb_by, cad, forced, rows_E, blk, frag, tag, mina):`） |
| `7` | `verify/wf_f4.py :: _reshape_block` | `f"{blk}·E3"` | `['blk']` | 同上（形參） |

**與款 `1` 之源頭比對（⛔ 判「是」或「否」以外之事）**：

| # | 是否即層① 之鍵之**同一物** | 依據（**產生式逐字**·⛔ 以名同判） |
|---|---|---|
| `1`／`2` | 🛑 **⛔ 可判** | 其三個 `Store` 中，二者之產生式為 `tp['所屬街廓']`／`matched.get('所屬街廓','')`（**宗地紀錄之欄**），一者為 `parcels_by_block` 之 `For` target；**皆⛔ 為 `_best_block` 之回傳**。二者是否恆等，須另證 `所屬街廓` 之寫入端與 `_best_block` 同源——**本批未受詞**。 |
| `3`／`4` | 🛑 **⛔ 可判** | 產生式 ＝ `parcels_by_block.items()` 之 `For` target；`parcels_by_block` 之建構端**不在本款之受詞內**。 |
| `5` | 🔴 **否** | 產生式 ＝ **字面常數** `lbl = "R1"` ⇒ **⛔ 自任何幾何導出**。 |
| `6`／`7` | 🛑 **⛔ 可判** | 產生式 ＝ **形參**（其實參在 `_reshape_block` 之呼叫端·**不在本款之受詞內**）。 |

🔒 ⇒ **七處中，`6` 處⛔ 可判、`1` 處（`wf_f1`）確證為字面常數**；⛔ 判為「是」。

### 三-4　款 `4`　既有之「幾何 → 街廓識別」映射（**全量**·⛔ 自寫第二套幾何）

**單所令之框**（母體 ＝ `ns` 全部鍵·框 ＝ 形參含 `block_poly`／`poly`／`geom` 類 ⋀ `Return` 值含款 `2` 之字樣）
⇒ 命中 **`1`**：`app.py :: _hash_polys_for_overlay`（形參 `['parcel_polys','classified_blocks']`·
`Return` ＝ `[(b.get('id'), b.get('label',''), b.get('category',''), …`）。

🔴 **惟本案唯一之「幾何 → 街廓識別」<u>實質</u>映射 ＝ `_best_block`（款 `1` 所溯之源頭），
其⛔ 在該框之命中內**——**二獨立結構性成因**（**皆機械可判**）：

| 成因 | 逐字 |
|---|---|
| ① | 其為 `parse_cad_precision_layers` 之**內層閉包** ⇒ ⛔ 在 `t.body` 頂層名（`ns` 鍵）之母體內。**實測**：頂層 `FunctionDef` ＝ `429`／內層 `FunctionDef` ＝ `208`（母體 `34` 檔） |
| ② | 其形參 `['_pts_l','_layer_nm','_handle']` **⛔ 含** `['block_poly','poly','geom']` 任一字樣 ⇒ **縱置於頂層，該框亦⛔ 命中** |

🔒 **母體二層分列之實測**：頂層層（＝ 單所令之母體）命中 **`1`**；內層閉包層命中 **`2`**
（`app.py :: _solve_one`／`verify/stepg_pipeline.py :: _solve_one`·二者形參皆含 `_blk_poly`）。
🛑 本款**⛔ 自寫第二套幾何**——只現查既有者；上開二成因係**框之自限**之照實具名，**⛔ 逕改該框**。

### 三-5　款 `5`　判別力四造

| 造 | 實得 | 判 |
|---|---|---|
| [必為 `34`] 生產碼母體之外部錨（坑 `bj`） | `34` | ✅ |
| [必非零] `ns` 鍵基數 | `286`（≥ `1`） | ✅ |
| [必為零] **執行期組出**之人造字樣於款 `2` 之框下 | `0` | ✅ |
| [必真] `st` 在 `ns` 之鍵 | `True`（**獨立復現** `W-G.9-302R` 款 `5`） | ✅ |

🛑 **本工項⛔ 判「可信」或「不可信」、⛔ 擬任何改法或 diff、⛔ 改生產碼一字、⛔ 開分支。**

---

## `§四`　工項二：二守衛母體之關係

**落檔** ＝ `verify/out/WG9303R6_dynamic.log`（`1086` 列·**v1·器紅·保全⛔ 覆寫**）
＋ `verify/out/WG9303R6_dynamic2.log`（`1091` 列·**v2·器綠**）。

### 四-1　款 `1`　`is_corner` 之定義與求值來源

**母體** ＝ 生產碼 **`34`** 檔（正面列舉·外部錨）。**五形分列**（v1 之二形⛔ 涵蓋字面鍵·見自捕）：

| 形 | 處數 | 全量逐處（`檔 :: 函式` ＋ 賦值產生式逐字） |
|---|---|---|
| `Name`-Store | **`0`** | 🛑 **loud**：無命中 |
| `arg`（形參） | **`3`** | `app.py` ×`3`：`is_corner: bool = False,` ×`2`／`S_max, is_corner, side, avg_depth, B, C, tab6_burden,` |
| `Subscript`-Store（**字面鍵**） | **`7`** | `app.py :: main::_f3_corner_picker_fragment` ⇒ `curr['is_corner'] = new_is`；`app.py :: main` ⇒ `_existing['is_corner'] = False`／`= True` ×`2`；`app.py :: main::_f3_unified_map_fragment` ⇒ `curr['is_corner'] = True`／`= False`／`= True` |
| `Dict` 鍵字面 | **`0`** | 🛑 **loud**：無命中 |
| `Load`（讀） | **`4`** | `app.py :: _solve_G_one` ×`3`／`app.py :: solve_G_binary` ×`1` |

**文字層列框**（以資對照）＝ **`90`** 列；逐檔 ＝ `{'app.py': 73, 'verify/fixture_end_reserve.py': 1, 'verify/stepg_pipeline.py': 15, 'verify/test_corner_first_lot_G.py': 1}`。
🛑 **二數相異之成因（loud 具名）**：AST 以**節點**計（一列可含多個、且 `'is_corner'` 之字串字面於 `.get('is_corner')`／
表格文案／註解中亦占列），文字層以**列**計 ⇒ **口徑不同**，⛔ 應相等。
[必相異]造：AST 合計（`Store 3` ＋ `Load 23`，v1 之二形口徑）＝ `26` vs 文字層 `90` ⇒ **相異 `True`** ✅。

#### 🔑 **明確回答：其受詞係<u>逐宗</u>，⛔ 逐街廓**

**依據 ＝ 其賦值式所消費之名之逐字**（⛔ 以讀來像是判）：

```
app.py :: main
    for tp in build_parcels:
        if tp.get('所屬街廓', '') in _affected_blocks:
            k_tp     = tp.get('暫編地號', '')
            _existing = dict(_params_for_g.get(k_tp, {}))
            _existing['is_corner'] = False
```

⇒ receiver `_existing` ＝ `_params_for_g[**暫編地號**]` ⇒ **鍵係宗地**（`暫編地號`），⛔ 街廓。
`_f3_corner_picker_fragment`／`_f3_unified_map_fragment` 之 `curr = dict(_params_now.get(k, {}))` 同形。
其**消費端**為 `_solve_G_one(*, …, is_corner, side, …)` 之**關鍵字形參**——其唯一決定點逐字：

```
app.py :: _solve_G_one
    if is_corner:
        allocation_dir = _first_corner_alloc_dir(side_mid)
```

（`app.py:13929` `def _first_corner_alloc_dir(side_mid):`·其**唯一呼叫端守衛係 `is_corner`**
——**獨立復現** `W-G.9-303` `§零′` ⑤ 之併記。）

🔴 **併記（照實）**：`Subscript`-Store 之 **`7` 處全數落於 `app.py` 之 `def main` 內**
（`main` 區間 ＝ `14975`-`24579`·AST 實查·`P-3` 之輸出）⇒ **`run_all`／`run_step_g` 從不執行之**
（`CLAUDE.md`「`main()` 內之敘述，`run_all` 不得單獨作為驗收依據」之同族）。
harness 路徑之 `is_corner` 另由 `verify/stepg_pipeline.py` 之 `_pm.get('is_corner', False)` 取得
（`'is_corner_winner': bool(_pm.get('is_corner', False))`）。

判別力：[必為零] 人造名（執行期組出）於 AST 命中 **`0`** ✅；[必非零] `Store` 處數 `3`（五形合計 `14`）≥ `1` ✅。

### 四-2　款 `2`　「街角第 `1` 宗」判準於碼面之載體（**全量**·字樣由框生成）

| 字樣 | `FunctionDef` | 頂層 `Assign` | **全量逐名** |
|---|---|---|---|
| `corner` | **`14`** | **`1`** | `app.py`：`_annotate_block_corner_flags`／`_rebuild_corners_topology`／`_find_block_corner`／`_auto_detect_corner_side`／`_corner_buffer_S`／`_corner_range_eps`／`_build_corner_range_v3`／`select_corner_lots_both_sides_v12`／`_extract_corner_cut_line`／`_first_corner_alloc_dir`／`_corner_first_lot_G`／`_corner_block_true_G`／`assign_corner_side_by_projection`；`verify/selection_pipeline.py :: run_corner_pk`；頂層 `Assign` ＝ `verify/fixture_end_fallback.py :: corner_abate = 0.0` |
| `first` | **`2`** | **`0`** | `app.py :: _first_corner_alloc_dir`／`app.py :: _corner_first_lot_G` |
| `_fc` | **`0`** | **`0`** | 🛑 **loud**：無命中（母體 `34` 檔） |

### 四-3　款 `3`　二母體之關係（**動態·本案**·`run_verification` 全量）

`run_verification.main()` 之 `rc` ＝ **`1`**（🔒 **既存之准紅碼**·`CLAUDE.md` 分支狀態宣告·⛔ 本批所致）。

#### 量測器之自證（🛑 **母體⛔ 含其自身輸出**）

| 受詞 | 生產錄 | **器自身（須 `0`）** | 判 |
|---|---|---|---|
| `_corner_buffer_S` | **`21`** | **`0`** | ✅ |
| `_solve_G_one` | **`2065`** | **`0`** | ✅ |

🔑 **該欄非恆為 `0`**：v1（**同一受詞·未冪等**）之器自身欄為 **`21`**／**`2065`** ⇒ 其歸零係**修**之效。
冪等自證：`RV.harvest` 被呼叫 **`2`** 次／`wrap()` 進入 **`2`** 次／**因已包裝而跳過 `1` 次**。
呼叫端一律以 `(co_filename, co_name, co_firstlineno)` 序辨（🛑 **`id(·)` ⛔ 作錨**）。

#### 🔴 二受詞之 `side` **詞彙不同**（碼面事實·⛔ 量測器所造）

| 受詞 | `side` 之相異**原值** |
|---|---|
| `_corner_buffer_S` | `['left']` |
| `_solve_G_one` | `['右側', '左側', '無']` |

⇒ 集合比較**必須先正規化**（`left`→`L`／`左側`→`L`／`right`／`右側`→`R`）；**原值與正規值並報**。

#### (甲)　`_corner_buffer_S` 實走之呼叫端 × 街廓 × 側（**全量**）

| 呼叫端檔 | 呼叫端函式 | 街廓 | 側(原值) | 側(正規) | 次數 |
|---|---|---|---|---|---|
| `verify/stepg_pipeline.py` | `_run_step_g_impl` | `R2` | `left` | `L` | `6` |
| `verify/stepg_pipeline.py` | `_run_step_g_impl` | `R4` | `left` | `L` | `15` |

**(甲) ＝ `[('R2','L'), ('R4','L')]`（基數 `2`）**
——🔑 **本批獨立重得**，與 `W-G.9-300R` 之 `side = ['left']`·`_label = ['R2','R4']` 相符。
`f_locals` 自證：命中街廓 **`21`**／未命中 **`0`**；命中之鍵 ＝ `['blk_label']`（**多鍵並取**·同框其他命中鍵 ＝ `[]`）。

#### (乙)　`is_corner` 為**真**之街廓 × 側（**全量**）

`is_corner` 分布：真 **`807`**／偽 **`1258`**／`None` **`0`**。

| 街廓 | 側(原值) | 側(正規) | 次數 |
|---|---|---|---|
| `R1` | `右側` | `R` | `90` |
| `R1` | `左側` | `L` | `90` |
| `R2` | `左側` | `L` | `186` |
| `R3` | `右側` | `R` | `150` |
| `R4` | `右側` | `R` | `12` |
| `R4` | `左側` | `L` | `27` |
| `R5` | `左側` | `L` | `126` |
| `R6` | `右側` | `R` | `126` |

**(乙) ＝ `[('R1','L'),('R1','R'),('R2','L'),('R3','R'),('R4','L'),('R4','R'),('R5','L'),('R6','R')]`（基數 `8`）**
🛑 **街廓⛔ 可得之 `is_corner` 為真者 ＝ `0` 次** ⇒ 本次**無**不可得之分項（⛔ 判為零、⛔ 判為空之附款**無受詞**）。

#### (丙)　差集**逐項列舉**（正規化後）

| 差集 | 逐項 | 基數 |
|---|---|---|
| **(甲) ∖ (乙)** | `[]` | **`0`** |
| **(乙) ∖ (甲)** | `[('R1','L'),('R1','R'),('R3','R'),('R4','R'),('R5','L'),('R6','R')]` | **`6`** |

### 四-4　款 `4`　**三態分列**之判（🛑 ⛔ 判其後果）

| 態 | 判 | 依據 |
|---|---|---|
| ① **(甲) ⊆ (乙)** | ✅ **成立** | `(甲) ∖ (乙) = []` |
| ② **(甲) ⊄ (乙)** | ❌ 不成立 | **逐格列舉 ＝ `[]`**（無格） |
| ③ **(乙) 不可得** | ❌ 不成立 | `_solve_G_one` 生產錄 `2065` 次；街廓不可得者 `0` 次 |

🛑 **⛔ 判其對土地之後果、⛔ 擬任何 fallback、⛔ 呈 KL、⛔ 判孰是孰誤、⛔ 提修法主張。**

### 四-5　款 `5`　判別力四造

| 造 | 實得 | 判 |
|---|---|---|
| [必為 `34`] 外部錨（坑 `bj`） | `34` | ✅ |
| [必非零] 款 `1` 之 `Store` 處數 | `3`（五形合計 `14`）≥ `1` | ✅ |
| [必為零] **執行期組出**之人造名於款 `1` 之框下 | `0` | ✅ |
| [必相異] AST 數與文字層數**各自出艙** | AST `26`（二形口徑）／文字層列框 `90` ⇒ 相異 | ✅ |

---

## 🩸 本批之**自捕**（⛔ 頂替·**⛔ 鑄號**·鑄號候 `W-G.9-304`）

🛑 **⛔ 讀為「本批無誤」** ——本批自捕 **`4`** 則，**全為 CC 自身量測器之缺陷**，皆於出艙前攔下。

| # | 形 | 徵候 | 成因 | 處置 |
|---|---|---|---|---|
| `1` | 🔴 **動態量測器之「器自身」欄 ＝ 生產錄**（`21/21`・`2065/2065`·**恰各半**） | v1 落檔 `WG9303R6_dynamic.log` | `RV.harvest` 被呼叫 **`2`** 次（`main()` 與 `n19p_depth_by_block()`），而 `wrap()` **非冪等** ⇒ 每次呼叫被錄**兩次**，內層之呼叫端即本器（`MISS` 內之 `呼叫端 'sgo2'` ×`624` 為直證） | 以屬性旗標令包裝冪等（v2）；**v1 落檔保全⛔ 覆寫**，並以之為 v2「器自身 ＝ `0`」之**判別力反造** |
| `2` | 🔴 **二受詞之 `side` 口徑不同而逕行集合比較** | v1 之 `(乙)` 側別欄印出 `"('右側')"`；`(甲)∖(乙)` ＝ 全量、款 `4` 判為 ② | `_corner_buffer_S` 用 `left/right`、`_solve_G_one` 用 `左側/右側` ⇒ **交集恆空** ⇒ `(甲) ⊆ (乙)` **恆偽** | v2 正規化並**原值與正規值並報**；🔴 **v1 之款 `4` 判「② (甲) ⊄ (乙)」係假象·⛔ 出艙為結論** |
| `3` | 🔴 **靜態器之四形框漏 `.setdefault`** | v1 之「層① 鍵之源頭」節**零命中** | 單所令之四形（`Subscript`／`Assign`／`.get`／`Dict`-`DictComp`）⛔ 涵蓋 `.setdefault`，而真寫入形正是之 | v2 加**第五形**；源頭鏈完整溯得 `_best_block` |
| `4` | 🔴 **靜態器之 `is_corner` `Store` 框漏字面鍵** | v1 報 `Store = 3`（皆形參），漏 `X['is_corner'] = …` **`7`** 處 | 🩸 **即同單 `§三` 款 `1` 附款所警告之 `ast.Dict`／字面鍵盲區，於次一款即重踩**（`CLAUDE.md`「立戒者在下一批最容易違反自己的戒」之實例·且係**同一張單內**之重踩） | v2 改**五形分列** |

---

## 🔑 本批之**自解清單**（`作業常規之追加五` 一-5·逐項五欄）

### 自解 `1`　v1 動態器紅 ⇒ **修工具、重跑**（白名單 `5`）

| 欄 | 內容 |
|---|---|
| ① 疑義逐字 | 單 `§四` 首段：「執行 `run_verification` 全量**一次**」——而 v1 之器紅使該次量測⛔ 得出艙 |
| ② 二個以上之讀法 | (a) 授權已用罄 ⇒ **停機上呈**；(b) `作業常規之追加五` **白名單 `5`**：「**量測器紅**（CC 自身工具之缺陷）⇒ **修工具、重跑、記為自捕**」 |
| ③ 所取者 | **(b)** ——白名單 `5` **逐字命中**本情形 |
| ④ 機械證據 | 五項全備：①零土地後果（`run_verification` 對**受追蹤檔零異動**·`git status --porcelain --untracked-files=no` 輸出**空**）②零生產碼（新增者皆在 `verify/probes/`·**⛔ 在 `34` 檔母體內**·生產碼判法 `0` 行／對照組 `4` 行）③可機驗（器自身欄：v2 ＝ `0`[必綠]／v1 ＝ `21`·`2065`[必紅]·**二造皆實跑**）④可逆（**新建檔**·v1 之器與落檔一字未動）⑤具名（本清單 ＋ 自捕表） |
| ⑤ 所棄者之由 | (a) 將使「一次」之字面凌駕於「量測器紅⛔ 出艙」之上位戒——而 `CLAUDE.md` 逐字：「該閘不過，⛔ 據以下任何結論」 |

### 自解 `2`　`§二` 入倉前釘死之**期值不可得**

| 欄 | 內容 |
|---|---|
| ① 疑義逐字 | `§二`：「其值**由 KL 交付時之回報取之**…bytes ＋ 內容 `sha256` 二數須逐位相符；不符 ⇒ 停、⛔ 入倉」 |
| ② 二個以上之讀法 | (a)「不可得」＝「不符」⇒ **停、⛔ 入倉**；(b)「不可得」≠「不符」⇒ **loud 拒測該款**、續辦，傳輸保真改由 `P-5` 承擔 |
| ③ 所取者 | **(b)** |
| ④ 機械證據 | `CLAUDE.md`「`序 11` 之一般化」款 `三` 逐字：「**「無從回測」⛔ 等同「回測不過」**」；且「作業常規之追加四」之**射程界限**已逐字預告來源側無獨立 `sha256`。`P-5` 之否證對照[必綠]／[必紅]**皆實跑且如期** |
| ⑤ 所棄者之由 | (a) 將使**每一張**未附 `sha256` 之單皆⛔ 入倉 ⇒ 與倉內既行之入倉慣例（`docs/orders/` 已 `31` 號在倉）互斥 |

🔒 **二項皆⛔ 落於黑名單**：未動任何宗地之 `G`／面積／街角歸屬／抵費地／配地幾何；未動生產碼一字；
二讀法之後果在土地上**相同**（皆為零）；未新訂準據（二者皆**援引既有明文**）；未涉 KL 已裁之款。

---

## 一句話推導

層① 鍵源自 `_best_block`（幾何→街廓·**內層閉包**），而 `_corner_buffer_S` 體內可解之街廓識別**唯有形參 `_label`**（其七處實參中 `6` 處⛔ 可判源、`1` 處為字面常數）；動態上 `_corner_buffer_S` 實走之 `{(R2,L),(R4,L)}` **⊆** `is_corner` 為真之 `8` 格——**此為現查之出艙，⛔ 任何可信性之判。**

---

## 🛑 `⛔ 為之事` 之逐項自檢

| # | 受詞 | 判 | 證 |
|---|---|---|---|
| `1` | ⛔ 改生產碼 `34` 檔一字 | ✅ **未為** | 逐 `commit` 之生產碼判法皆 **`0`** 行（對照組 `4`）；收工閘 `6` 之 `34` 檔 blob 期初＝期末相異 `0` |
| `2` | ⛔ 開任何分支；⛔ 動用 KL 之放行；⛔ 辦修批；⛔ 自續 `W-G.9-304` | ✅ **未為** | `git ls-remote origin 'refs/heads/verify/*'` 之集合未變；本報告止於 `W-G.9-303R6` |
| `3` | ⛔ 併線（含 `p3a`）；⛔ 刪任何 ref；⛔ 覆寫 `verify/baselines` 任一檔或**任一物證落檔**；⛔ `WV_BAKE`；⛔ 引任何自 `baseline` 取得之數 | ✅ **未為** | `p3a` `rc = 1`；`baselines` `298`·`a898f4e1…`；`13` 物證逐位未動；`WV_BAKE` ＝ **未設**（探針以 `assert` 自證）；本報告未引任何 baseline 之數 |
| `4` | ⛔ 改任何函式簽章／新增形參／新增 `import` 於生產碼／改任何 `*_EXPECT` | ✅ **未為** | 生產碼零異動（同 `1`） |
| `5` | ⛔ 自寫第二套幾何或第二份 `W`／`side_mid`／側界線／街廓識別之定義（`GB-48` 族） | ✅ **未為** | 二靜態器只讀 AST；動態器只**包裝**既有函式、⛔ 重算任何幾何 |
| `6` | ⛔ 動 `ALPHA_LABELS` 一字；⛔ 動任何**既有**探針一字 | ✅ **未為** | `ALPHA_LABELS` 之唯一 `.py` 載體 `verify/probes/probe_WG9269_pit_index.py` 之 `git diff --numstat` 輸出**空**；本批新增之四支探針皆為**新檔** |
| `7` | **⛔ 鑄自誤／`GB`／`VR`／`K-9`／坑之任何號** | ✅ **未為** | 收工閘 `4`／`5` 之器輸出與開工閘**逐格相同** |
| `8` | ⛔ 追加任何 `GB` 之末端登記；⛔ 解除或收窄任何 `GB`（含 `GB-170`） | ✅ **未為** | `docs/reports/W-G.4_泛用阻塞項登記表.md` 本批零異動 |
| `9` | ⛔ 落地 `K-9-5-*`／`K-9-12`／`K-9-29` 之任何子項 | ✅ **未為** | 生產碼零異動 |
| `10` | ⛔ 改 `W-G.9-303` 施工單一字；⛔ 重辦其 `§二` 工項零 | ✅ **未為** | 該單 blob `sha1` `8c85fc1c…` 未變；工項零之代行 `commit` 已具名 |
| `11` | **⛔ 追改本波七單／二交接註／`W-G.9-303R`／`W-G.9-303R4` 或任何已入倉文件一字** | ✅ **未為** | 逐 `commit` 之 `deletions` 全 `0`；本批之異動**全為新檔** |
| `12` | ⛔ 擴 KL 放行之射程；⛔ 呈 KL；⛔ 擬第二次放行之呈文 | ✅ **未為** | 本報告**⛔ 呈 KL** |
| `13` | ⛔ 判 `GB-170` 可否解除／路丙落點可施與否／`停四` 為誤／「`(甲) ⊄ (乙)`」之土地後果／擬 fallback／判孰是孰誤／提修法主張 | ✅ **未為** | `§四` 款 `4` 僅出艙三態分列之判 |
| `14` | **⛔ 估算或出艙本窗 context 之百分比** | ✅ **未為** | 本報告無任何百分比；亦未遭遇資源硬限之可觀測事件 |
| `15` | ⛔ 於任何入倉文件宣稱一件尚未發生之事（及於 `commit` 訊息與「已推送」之陳述） | ✅ **未為** | 收工閘之值**皆於報告入倉後量**，以**末端追加**落地 |

---

## 逐 `commit`（**全 `40` 碼**）

| # | `commit` | 內容 | `deletions` |
|---|---|---|---|
| `1` | `b688ad10e56054274c501b0d244b3c6cb196161a` | `§二` 工項零：本補令原封入倉 | `0` |
| `2` | `094b841320b461cdc91f6ce715a492d86c55aa64` | `§三`／`§四` 之四支量測器與四份落檔 | `0` |
| `3` | （本報告之 `commit`·見末端追加段） | 執行報告入倉 | `0` |

**基座** ＝ `dbc5b1d45a664f1d4fd5676e5dcb5880d23d7bce`。
