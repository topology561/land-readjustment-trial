# `W-G.9-383` 補令一：工項二停機之裁（唯讀審查之 #13〜#15）——再試成者之標記於入池閘之合併單元之取代時併入單元（`R-12`·新立）＋ 量測器 `F23` 之 `K60`（工項一′）＋ 工項二之碼以倉內之差異檔與塊 `Fy33` 施之（工項二′）＋ 續辦工項三、四（新側支 `verify/W-G.9-383-k975`）

> **本補令建議等級 ＝ `heavy`**（生產碼之改·`V-1`〜`V-9` 全數重跑·`52` 呼叫 ≈ `100`〜`130` 分）。**⛔ 撰新碼**：工項一′、工項二′ 之一切改動 ＝ 本補令之塊與倉內之差異檔之原樣之施。
> **發單** ＝ 發單側窗八十六·`2026-10-15`。**受單** ＝ CC（續辦·同一新側支 `verify/W-G.9-383-k975`·一切 `commit` 推至該側支·快轉·主線⛔ 動）。
> **所補** ＝ `docs/orders/W-G.9-383_規格單.md`（`150341` B·`sha256` `ed57adfab62e1de2cdebdac4db3d7fee17751339a89903072ae41c726b53d4a4`·blob `4df3a5dae75dfa8cacb25bcfc6a80f15d893174e`·「原單」）。二者皆留倉、⛔ 改一字；**相牴之點以本補令為準，本補令未及者依原單**。
> **所應** ＝ CC 之停機報告 `docs/reports/W-G.9-383R_工項二停機上呈_唯讀審查之發現.md`（`13490` B·`sha256` `270105471bf4e02c5a233bbc709d6b6cfbb52b76159dd0fa83a6fcd4e87f9c4c`·blob `fa0a992c1acb7766d7dd7d1c7287760d1f07a853`·「停機報告」）之四、五（#13〜#15）、八。
> **開工態** ＝ 新側支 `verify/W-G.9-383-k975` ＝ `51ca5d8c0db7832be5b9e4a6f6d429fe854f74cb`（其前 ＝ 工項零 `3f1574a1be15f12c0e8d9fc55b5590bc9625ba19`、工項一 `a9131fb766ecbbcadab23b9c3dc263b58aa5f8e8`）；主線 `wip/s1-endpart` ＝ `2663f559272a3a87af8821e54d20e689d3aebd5b`；遠端 heads **`43`**；CC 本地 `hold/W-G.9-383-c2` ＝ `eac8847149b102d4e90ff60d5aaeaa0634fba7d3`（**⛔ 推**——其父為 `a9131fb`，推之於 `51ca5d8` 之上須 `--force`·停機款 `7`）；工項二之碼 ＝ 倉內 `docs/reports/W-G.9-383R_工項二_app差異.diff`（`33180` B·`sha256` `8044eb29719197d3ee488fc04f2ee84bfeb4407edf0f4ea8e9f14b0e76713514`·blob `e7fa2c8ccdd4ff08bca1cee5c5960734f5752580`·以下稱「**工項二之碼**」·施後 `app.py` ＝ `3eb87c969fbd82aefb7c09504f4db01490c68159`〔`1808515` B〕、`verify/selection_pipeline.py` ＝ `cf1d8e41d81ad9e17f1bc3817df58302d8207176`〔`59291` B〕）。
> 🔑 原單之一切通則照舊（直譯器名、塊之抽取式〔`§五-1` 末〕、`git commit -F`、`PYTHONIOENCODING`／`PYTHONUTF8`、路徑引數之形、Bash 之禁、量測之殼⛔ 設五旗標、並行之限〔重型同時 ≤ `2`〕、`<O>` 同原單）。本補令之塊（附錄甲′、乙′）之抽取式同原單，以 `## 附錄甲′`／`## 附錄乙′` 起首之列之後之第一個圍欄開列為準。
> 🔑 **來源檔**（檔名逐字 `W-G.9-383_補令一.md`·本補令）：取之序同原單；三處皆無 ⇒ 停機款 `2′`。CC 一律**二進位複製**、⛔ 讀入改寫。
> 🔑 **撇號**：「′」＝ U+2032。本補令之款號（`1′` 等）、工項號（`零′`、`一′`、`二′`）、閘號（`1′` 等）唯指本補令之條。
> 🛑 **本補令⛔ 及於**：原單之一切禁；`app.py` 除「工項二之碼」與塊 `Fy33` 原樣之施外之一字；`verify/selection_pipeline.py` 除「工項二之碼」原樣之施外之一字；量測器除塊 `Fy32` 原樣之施外之一字；新側支之既有四 `commit` 之改寫（⛔ `--force`、⛔ `rebase`、⛔ `amend`）；塊 `K23`／`E26`／`P36`（照原單·⛔ 改一字·`§一` 裁七）；自誤簿之新號（`§一` 裁五·候鑄）。
> 🔴 **本補令⛔ 令 CC 作任何「孰為正典」「應改為」之判**；遇本補令未及之情形 ⇒ **停機上呈、⛔ 自裁**。

---

## `§零`　開場（**先於工項零′**·⛔ 跳序）

1. 自報 context 餘量。
2. `git fetch origin`；`git rev-parse origin/wip/s1-endpart` ＝ `2663f559272a3a87af8821e54d20e689d3aebd5b`；`git rev-parse origin/verify/W-G.9-383-k975` ＝ `51ca5d8c0db7832be5b9e4a6f6d429fe854f74cb`；`git ls-remote --heads origin` 之列數 ＝ **`43`**（全列存 `<O>\heads_before_383p1.txt`；其中除 `verify/W-G.9-383-k975` 之列外之 `42` 列 ＝ 原單之 `<O>\heads_before.txt`）；施工樹 `git checkout --detach origin/verify/W-G.9-383-k975` 後 `git status --porcelain --untracked-files=no` ＝ 空；本地 `hold/W-G.9-383-c2` 之存否與其值出艙（不存⛔ 礙——工項二′ 一律以倉內之差異檔為之）。
3. 本補令之 bytes／`sha256` 對拍 KL 所貼之訊；本補令之 `SELF_SHA256` 依 `P-5` 原口徑自驗（受詞 ＝ 自檔首至檔內**最末**一個 `SELF_SHA256:` 列之前一個 `\n`〔含〕之全部位元組）；KL 之訊未載或為縮寫者，照實具名而以 `SELF_SHA256` 為據（⛔ 停機）。
4. 原單、停機報告、工項二之碼之差異檔之 bytes／`sha256`／blob ＝ 單首之值（`git cat-file -s`／`git cat-file -p <blob> | sha256sum`）；塊 `Fy32`／`Fy33` 之抽取 ＝ `§五` 項 `2`。
5. `python verify/probes/probe_order_preflight.py <本補令之路徑>` 並逐項再處置（發單側實跑之出艙見 `§五` 項 `7`）。

### `§零-1`　停機款（原單之款照舊；下列四款**代**原單之同號之款）

| # | 款 |
|---|---|
| `1′` | 開工時主線 ≠ `2663f55`，或新側支 ≠ `51ca5d8`，或遠端 heads ≠ `43`，或其除新側支外之 `42` 列 ≠ 原單之 `<O>\heads_before.txt`，或施工樹之追蹤檔有變動，或量測之殼之旗標之出艙 ≠ `[None, None, None, None, None]` |
| `2′` | 本補令之 `SELF_SHA256` 自驗不符；或 KL 之訊所載之 bytes／`sha256` 與本補令不符；或來源檔於三處皆無；或入倉後 `git cat-file blob` 與來源不逐位相同；或 `§零` 項 `4` 之值 ≠ 期 |
| `3′` | 塊 `Fy32`／`Fy33`／工項二之碼之 `git apply --check` 任一不過；或施後之 blob ≠ `§二` 之期；或工項二′ 之前置′ `1`、`2` 任一 ≠ 期 |
| `6′` | 原單之款 `6` 照舊（其期依 `§二` 之代）；另：`V-1`〜`V-9` 任一 ≠ 期 ⇒ **⛔ 改量測器、⛔ 改塊、⛔ 改碼**以求其過 |

---

## `§一`　裁（發單側·非域上之判·本案零土地後果）

**裁一（#13）：採停機報告四之第二形——入池閘之合併單元之取代時，自 build 去之成員之標記併入單元（`R-12`·新立）。** 手冊先行之「入池閘之合併單元之取代」之段（`k953_manual_run`·工項二之碼施後之 `app.py` 之 `:15675`〜`:15686`），於 `_oth953` 定之後、`_nb953` 之前：`_oth953` 之成員中，於 `state["by"]` 而帶標記之鍵（`'第31條第3款併入'`）且其值非空者，其值之聯集非空 ⇒ `_nt953` 中之單元（暫編地號 ＝ 宿主者）之同鍵 ＝ `sorted(其既有之值 ∪ 該聯集)`；聯集為空 ⇒ ⛔ 增鍵（單元之 dict 與工項二之碼逐位同）。其後（`_cand_st`、`_same953`、紀錄、取代與否）⛔ 變；取代未成 ⇒ `state` ⛔ 變（受併之片仍在 build·帶其標記）。字面 ＝ 塊 `Fy33` 之第二段。
- **由一（⛔ 新之域上之擇）**：原單塊 `K23` 四之戊（「再試成者之標記於其後之試算存續」）係發單側之【工】之讀法、已以交付之通知告 KL（⛔ 駁即視為同意）；標記存於何處屬其落地之形。受併之片為單元之宿主者，單元 ＝ 其 dict 之深拷貝 ⇒ 標記本即存續（停機報告四）；為成員者亦應存續——同一事唯因孰之應分配面積大而異其果，係程式之漏，⛔ 新之處理原則。
- **由二（第一形〔成員之片取自片之表 `_tab965`〕⛔ 採）**：畫面之入池閘（`_k929_6_screen_gate`·工項二之碼施後之 `app.py:22834`〜`:22837`）所傳之 `temp_parcels` ＝ `session_state['f3_temp_parcels']`（套疊之切片·段三之前·同 `:26230`），手冊先行之試算與 G 值迭代之入池閘皆經之 ⇒ 其片之表之受併之片⛔ 帶標記 ⇒ 第一形於畫面仍失之（且為靜默）。發單側讀碼實核。
- **由三（第三形〔維持 `R-3` 之字面而記為已知之界〕⛔ 採）**：KL `2026-10-05` 之泛用之令（他案可能遇之形須即解·「遇之即停」⛔ 為解）；且屬「失之而⛔ 示」之族。
- **射程**：生產碼中以單元取代宿主而自 build 去其成員者唯此一處（`git grep -n -F "['units'][" -- app.py ':(glob)verify/*.py'` ⇒ 恰一列·工項二之碼施後 `app.py:15677`、塊 `Fy33` 施後 `:15679`；同命令以 `'["units"]['` ⇒ 無出艙）。單元其後於他次之入池閘中為他單元之成員者，該次之判以其輸入之 build 之宿主之 dict 讀之（`_inb965`·⛔ 改）。
- **本案**：再試三筆二退縮皆未成 ⇒ 無片帶標記 ⇒ 聯集恆空 ⇒ `R-12` ⛔ 觸（`V-4`〜`V-6`·`§五` 項 `5`、`6`）。**他案**：再試成而受併之片為同地主他宗之單元之成員者，其後同街廓同地主配不到之他宗唯得依第 `3` 步併入該單元（⛔ 依第 `1` 步捲入）——與受併之片為宿主者同（原單 `F29` `K72`）。

**裁二（#14）：採現碼之讀。** 原單 `R-5` ⑦ 之 `'結果': '成'／'未成', '檢核': '通過'／'不過'` 依其列之序相配（成 ⇒ 通過、未成 ⇒ 不過）——發單側擬單之意，與既有之手冊之列之配對（`_verdict953`）同；「不影響原位次」之檢核本身之不過見於 `不過之由`。⛔ 改碼。

**裁三（#15）：** ① `k953_manual_run` 之 docstring 之 🔧 `W-G.9-383` 款之停機之述改合其碼（「再試之受詞存在而試算之 `kept` 非 dict」⇒「逐分量判之時當下之試算之 `kept` 非 dict」）——字面 ＝ 塊 `Fy33` 之第一段（碼 ＝ 規格·⛔ 改碼）。②〜④ 照實載於報告 ⑥·⛔ 處置：② 單元之成員出自同一 build 之 `入池閘併入`，一片屬二以上之宗者入池閘之輸出已不合，⛔ 實生；③ 缺 `暫編地號` 之列唯增一鍵 `'None'`，片之所屬單元之查（不在 ⇒ 停機）不受之；④ 型不合 ⇒ `AttributeError`（loud·⛔ 靜默）。

**裁四（撰碼中之自捕 `'kept'`）：** 照實載於報告 ⑥·⛔ 處置（量測器⛔ 改·合原單 `§三-3` 之 `2`）。

**裁五（自誤）：** `R-3` 定「帶標記」之受詞為輸入之 build 之片，而未及手冊先行之單元之取代（自 build 去成員）——規格之漏 ⇒ 發單側之自誤（擬 `620`）**候鑄·併次單**（⛔ 入本批之塊 `E26`·其 blob 與閘 `4`／`6`／`7` 之期照原單）。

**裁六（審查）：** 工項二′ 之碼 ＝ 工項二之碼 ＋ 塊 `Fy33`（發單側所擬·逐字）⇒ 附則丙之唯讀審查**重派**，其受詞唯：塊 `Fy33` 之二段（`R-12` 之置處、其受詞〔`_oth953` 之成員·`state["by"]` 之值〕、聯集為空者⛔ 增鍵、取代未成者 `state` ⛔ 變；docstring 二處）與塊 `Fy32`（`K60` 之期合 `R-12`；`units_if` 缺 ⇒ 玩具之行為與工項一之端逐位同·⛔ 及既有之例）。發現涉域上判斷或規格之漏載 ⇒ 停機款 `12`（⛔ 自裁）；純實作之瑕 ⇒ **停機上呈**（⛔ 改塊）。停機報告五之 #1〜#12、#16、#17 之結論沿用。

**裁七（工項三之塊）：** 塊 `K23`／`E26`／`P36` 照原單（⛔ 改一字）——其「落地狀態 🔶（新側支）」之述於本補令之後仍確；本補令之裁之紀錄 ＝ 本補令（入倉）與報告 ⑥。

---

## `§二`　工項（依序·各一 `commit`·皆推新側支·快轉）

**工項零′　本補令原封入倉**（零生產碼）：`docs/orders/W-G.9-383_補令一.md`（**新檔**·二進位複製）。`commit` 訊息之首列逐字 `W-G.9-383 工項零′：補令一原封入倉（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-383-k975`。

**工項一′　量測器**（零生產碼·**先於生產碼**）：塊 `Fy32` 抽為 `<O>\Fy32.diff`，對拍 `§五` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`git hash-object verify/probes/probe_WG9363_k953.py` ＝ `083e8a0b2ecf275a7fad2992ddd60769fbedcef1`（`108036` B·施前 ＝ `9ca5656a1220c0c9120a03892f6ec2bb687f2771`）；`git diff --numstat` 恰一列 `27	4	verify/probes/probe_WG9363_k953.py`。`commit` 訊息之首列逐字 `W-G.9-383 工項一′：量測器 F23 之 K60（再試成者之標記於單元之取代之後之存續·玩具之 units_if）（新側支）⛔ 零生產碼` ⇒ `git push origin HEAD:verify/W-G.9-383-k975`。

**工項二′　生產碼**（🔴 `app.py`、`verify/selection_pipeline.py`·一 `commit`·⛔ 撰）

**前置′**（於工項一′ 之端·⛔ `commit`·出艙存 `<O>\p1_*`）：
1. `python verify/probes/probe_WG9363_k953.py selftest <repo>` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K18', 'K49', 'K50', 'K51', 'K52', 'K53', 'K54', 'K55', 'K56', 'K58', 'K59', 'K60']；rc 1`（`app.py` ＝ 開工態）。
2. `git apply --check docs/reports/W-G.9-383R_工項二_app差異.diff` ⇒ 過、`git apply` 之；`git hash-object app.py verify/selection_pipeline.py` ＝ `3eb87c969fbd82aefb7c09504f4db01490c68159`、`cf1d8e41d81ad9e17f1bc3817df58302d8207176`；同 `selftest` ⇒ `rc 1`·末列逐字 `⇒ 紅 ['K60']；rc 1`（**#13 之形於工項二之碼重現**·`R-12` 之判別力）。

**施**（接前置′ `2` 之工作樹）：塊 `Fy33` 抽為 `<O>\Fy33.diff`，對拍 `§五` 項 `2` 後 `git apply --check` ⇒ 過、`git apply`；`git hash-object app.py` ＝ `f4cb5910b9ebaf52e1030a686a28c162a592ea3f`（`1809341` B）；`python -m py_compile app.py verify/selection_pipeline.py`；`git diff --numstat` 恰二列 `224	48	app.py`、`5	2	verify/selection_pipeline.py`；`commit` 訊息之首列逐字 ＝ 原單 `§四-1` 工項二之首列（`W-G.9-383 工項二：K-9-73 ④·K-9-75〜K-9-77 之落地（手冊先行之兩側皆配不到者之再試與同號之連通·入池閘之合併之標的與回原狀之帳之序與再試之片之標記及其先判·試算之回傳增 dropped）＋ 唯註之二處 🔴 生產碼（新側支）`）。**⛔ 即 `push`。**

**驗**（於工項二′ 之 `commit`·⛔ `push` 前·殼無 `WV_`·出艙一律存 `<O>\*_post2.*`）：原單 `§四-1` 之 `V-1`〜`V-9` **全數重跑**（同命令），其期照原單，唯下列之代：

| # | 代 |
|---|---|
| `V-1` | `F23 selftest` 之 `P0 逐項擾動恰該項紅 60／60`（原單 `59／59`）；餘照原單 |
| `V-4`〜`V-6` | 前置之出艙（`<O>\k6s3_pre_*.json`、`<O>\f8_pre_*.json`、`<O>\parity*_pre.json`）沿用原單之前置 `3`（其受詞 ＝ 工項一之端·⛔ 重跑——工項一′ 唯改 `F23`，此三器⛔ 載之）；期照原單 |
| `V-7` | 對照 ＝ **工項一′ 之端**；生產碼相異恰 `2`、`app.py` `224`／`48`、`verify/selection_pipeline.py` `5`／`2`、blob ＝ `f4cb5910…`／`cf1d8e41…`；`verify/` 之他檔相異 `0`；`app.py` 之頂層之名之集 ＝ 工項一′ 之端之集 |
| `V-8` | 「'第31條第3款併入'」⇒ `app.py:4`（原單之期 ≥ `2`·此其實）；餘照原單 |

**唯讀獨立審查**（`§一` 裁六·驗皆符後、推前）。

**推**（驗與審查皆符後·與驗為分開之呼叫）：`git push origin HEAD:verify/W-G.9-383-k975`。

**工項三**：照原單 `§四-1` 工項三（⛔ 改一字·其期照原單）。

**工項四**：照原單 `§四-1` 工項四，另載：① 逐 `commit` 之 hash 含停機上呈之 `commit`（`51ca5d8`）、工項零′、工項一′、工項二′（並載 `eac8847` 未推及其處）；② 停機款之三值含本補令之 `1′`〜`3′`、`6′`；③ 前置′ 之出艙；⑥ 停機報告五之發現、本補令之審查之發現，與其處置 ＝ 本補令 `§一` 裁一〜裁七（逐字引裁一、裁二之首句）；⑧ `W-G.9-383R_K-9-75之落地_app差異.diff` ＝ `git diff a9131fb <工項二′> -- app.py verify/selection_pipeline.py` 之全文（其 `numstat` ＝ `224`／`48`、`5`／`2`；其 `index` 列之縮寫之長依本地之物件數·⛔ 預載其 `sha256`）。

---

## `§三`　收工閘之代（原單 `§四-3` 之閘 `1`〜`3` 代以下開；閘 `4`〜`8` 照原單）

| 閘 | 受詞 | 期 |
|---|---|---|
| `1′` | 本批八筆 `commit`（`git log --reverse --format=%s 2663f55..HEAD` 之序·`git show --numstat`） | 工項零 ＝ 原單之增（`982`／`0`）；工項一 ＝ 原單閘 `1` 之二器之數；停機上呈（`51ca5d8`）＝ 二檔之增（`85`／`0`、`443`／`0`）；工項零′ ＝ 本補令之增（刪 `0`）；工項一′ ＝ `verify/probes/probe_WG9363_k953.py` `27`／`4`（唯此一檔）；工項二′ ＝ `app.py` `224`／`48`、`verify/selection_pipeline.py` `5`／`2`（唯此二檔）；工項三 ＝ 原單閘 `1` 之三簿之數；工項四 ＝ 報告二檔之增（刪 `0`）；首列：工項零、一、二′、三、四 ＝ 原單 `§四-1` 所令逐字，工項零′、一′ ＝ `§二` 所令逐字 |
| `2′` | 生產碼 `34` 檔與 `verify/` 對 `2663f55` | 同原單閘 `2`（生產碼相異恰 `2`·`verify/` 相異恰 `3`·皆 `M`）；本批之新檔**六**（原單、本補令、停機報告、停機報告之差異檔、執行報告二檔）之 `git check-ignore -v --no-index` 皆無命中（判別力同原單） |
| `3′` | 本批文字檔之 `CR`（受詞與判別力同原單閘 `3`） | 合計 **`0`**（**`13`** 檔：原單閘 `3` 之 `10` 檔 ＋ 本補令、停機報告、停機報告之差異檔） |

---

## `§四`　土地後果

**本案 ＝ 原單 `§一` 項 `5`、⛔ 增減**（再試三筆二退縮皆未成 ⇒ `R-12` ⛔ 觸·`§五` 項 `5`、`6` 之實跑）。**他案**：`§一` 裁一之射程。

---

## `§五`　驗收之基數（發單側窗八十六以程式重算·拋棄式 clone）

| # | 受詞 | 值 |
|---|---|---|
| `1` | 本補令 | 見本補令末列之 `SELF_SHA256`（`P-5` 原口徑）；bytes／`sha256` 見 KL 所貼之訊 |
| `2` | 塊 `Fy32`／`Fy33` | 塊 `Fy32` `5503` B·`sha256` `62a9caae47d4231f32660844499a762018978082eac246766a633348b25e9c92`·`79` 列（施於 `verify/probes/probe_WG9363_k953.py`·施前 blob `9ca5656a…`）；塊 `Fy33` `2811` B·`sha256` `890daa886fec5fbcaa85cbae47d67ca799820cb4b1a329553bda81932f4ce32d`·`31` 列（施於工項二之碼施後之 `app.py`·blob `3eb87c96…`）（皆圍欄內全文·末附換行·抽取式同原單） |
| `3` | 原單／停機報告／工項二之碼 | 單首之值（`git cat-file` 於 `51ca5d8` 實算）；工項二之碼於 `a9131fb` 之上 `git apply` ⇒ `app.py` ＝ `3eb87c96…`、`verify/selection_pipeline.py` ＝ `cf1d8e41…`（＝ 停機報告一之值·CC 之 `eac8847` 之二檔逐位同） |
| `4` | 工項一′〜二′ 之模擬（拋棄式 worktree `51ca5d8`·⛔ push） | 塊 `Fy32` `git apply --check` `rc 0`·施後 blob `083e8a0b…`（`108036` B）·`numstat` `27	4`；前置′ `1` ⇒ `rc 1`·末列 ＝ 期（紅 `12` 例·`stderr` `0` B）；工項二之碼 `git apply --check` `rc 0`·施後 blob ＝ 期；前置′ `2` ⇒ `rc 1`·末列 `⇒ 紅 ['K60']；rc 1`（其 `K60` 之得 ＝ `_mark4` 之 temp 唯 `{'X1(2)': ['X1(1)']}`、期 ＝ 另含 `'Y1(1)': ['X1(1)']`；再試之列〔成〕、單元之列〔`Y1(1)` 取代〕、輸出之 build 之集皆同——**#13 之形**：取代成而標記失）；塊 `Fy33` `git apply --check` `rc 0`·施後 `app.py` ＝ `f4cb5910…`（`1809341` B）·`py_compile` 過；對 `51ca5d8` 之 `numstat` ＝ `224	48	app.py`、`27	4	verify/probes/probe_WG9363_k953.py`、`5	2	verify/selection_pipeline.py`；`V-8` 之字樣 ＝ 期（「'第31條第3款併入'」`app.py:4`）；`app.py` 之頂層 `def`／`class` 之名之序 ＝ `a9131fb`（`281`·同序）；`§一` 裁一之射程之 `git grep` ＝ 所載 |
| `5` | `V-1`〜`V-3`（發單側之原型 ＝ 項 `4` 之施後之樹·本機 Linux·Python `3.13.16`·`numpy 2.4.6`·`shapely 2.2.0`·殼無 `WV_`·重型同時 `2`） | `52` 呼叫皆 **`rc 0`**·`stderr` 合計 `0` B·末列 ＝ 原單 `§五-1` 項 `8` 之施後之列；`P0`：`F29` `74／74`、**`F23` `60／60`**、`F27` `31／31`、`F28` `29／29`、`F24` `28／28`、`F14` `86／86`；`F27 mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`F23 run` 之 `R6@3.5`／`R6@0.0` ✅（各 `3` 列）；諸器之耗時之和 `5113` s |
| `6` | `V-4`〜`V-6`（前 ＝ `a9131fb`·後 ＝ 項 `5` 之樹） | 前後 `12` 呼叫（`k6s3 run`／`F8 run`／`parity`·二退縮）皆 `rc 0`·`stderr` `0` B；`V-4` `k6s3 cmp` 二退縮皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`；`V-5` `parity` 皆 `⇒ rc 0（不符 0 項）`，以同一字樣代 `HEAD` 之全值後落檔逐位同（⛔ 代之 ⇒ 相異）、`stdout` 唯一列異：`f3_k953_log（34 列）` → `（37 列）`（`3.5 m`）、`（43 列）` → `（46 列）`（`0 m`）；`V-6` `F8` 落檔前後逐位同：`8be0160bc14dd92a5331f86eecc995cae0507376`（`3.5 m`）、`6fb86647807f9744594071be25c522b6b506c230`（`0 m`）（＝ 停機報告三之 `V-6`）——**本案之配地⛔ 變** |
| `7` | pre-flight | `python verify/probes/probe_order_preflight.py <本補令>`·發單側窗八十六實跑（態 `51ca5d8`·定稿）：🔴 機械 `0` 項／🟡 提示 `0` 項／ℹ️ 記錄 `2` 項（`P-5` 相符；`P-3` 之 `app.py` `def main` 區間〔AST〕＝ `22694`–`30414`·本補令⛔ 用） |

---

## 附錄甲′　塊 `Fy32`（`git apply` 之差異·`verify/probes/probe_WG9363_k953.py`·工項一′）

````diff
diff --git a/verify/probes/probe_WG9363_k953.py b/verify/probes/probe_WG9363_k953.py
index 9ca5656..083e8a0 100644
--- a/verify/probes/probe_WG9363_k953.py
+++ b/verify/probes/probe_WG9363_k953.py
@@ -61,6 +61,11 @@
            隔道路⛔ 入連通·`dropped` 未回 ⇒ 停機·片為已配得之宗之成員 ⇒ ⛔ 再試·公設地之片⛔ 入連通·受併之片配地而檢核
            不過 ⇒ 未成）。期值出自本器之玩具之手算（發單側窗八十五）。
            P0 隨之 59 項。
+           🔧 `W-G.9-383` 補令一（唯讀審查 #13·⛔ 上列一字不刪）：玩具之 `_cbs` 增 `units_if`（`{標的: ([成員…], 片, 下限)}`·試算
+           之 temp 中該片之 a 達下限 ⇒ 該單元成立、其標的⛔ 以 `drop` 計）；增 K60（再試成而受併之片為同地主之他宗〔宿主〕之
+           單元之成員 ⇒ 入池閘之合併單元之取代之後，宿主之單元帶 `第31條第3款併入`〔其值 ＝ 所併入之片〕·受併之片之 temp 之鍵
+           照舊）。期值出自本器之玩具之手算（發單側窗八十六）。
+           P0 隨之 60 項。
   wiring   <repo> <基準 commit>
            接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_k953`）與 `run_corner_pk_k6b`
            之序（末端塊合併再試之後、以 winners／forced 呼叫、其後⛔ 重跑街角選位）；W3 畫面之入口（`f3_screen_k953`·
@@ -149,17 +154,27 @@ def _a(t):
     return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)
 
 
-def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, units=None, unit_g=None, need=None, nodg=False):
+def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, units=None, unit_g=None, need=None, nodg=False,
+         units_if=None):
     """玩具之回呼。`units` ＝ `{標的: [成員…]}`（入池閘之合併單元·其成員⛔ 單列）；`unit_g` ＝ 取代後之 G（覆寫·造相異）。
     🔧 `W-G.9-383`：`need` ＝ `{片: 下限}`（`drop` 之片其 a 達下限者配地）；回 `dropped`（不配地之宗之紀錄·其 G ＝ gmap 或 a）；
-    `nodg` ⇒ ⛔ 回 `dropped`。"""
+    `nodg` ⇒ ⛔ 回 `dropped`。
+    🔧 `W-G.9-383` 補令一：`units_if` ＝ `{標的: ([成員…], 片, 下限)}`——試算之 temp 中該片之 a 達下限 ⇒ 該單元成立（同
+    `units`）且其標的⛔ 以 `drop` 計；未達 ⇒ ⛔ 成立。"""
     cap, price, gmap, err_cap, units = cap or {}, price or {}, gmap or {}, err_cap or {}, units or {}
     need = need or {}
+    units_if = units_if or {}
+    units0, drop0 = units, drop
 
     def a_prime(src, dst):
         return _a(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)
 
     def alloc_state(temp, build):
+        units, drop = dict(units0), tuple(drop0)          # 🔧 `W-G.9-383` 補令一：units_if 之成立
+        for h_if, (mm_if, pz_if, thr_if) in sorted(units_if.items()):
+            if any(t["暫編地號"] == pz_if and _a(t) >= thr_if - 1e-9 for t in temp):
+                units[h_if] = list(mm_if)
+                drop = tuple(x for x in drop if x != h_if)
         kept, bad, G, acc, mem, uu = {}, {}, {}, {}, {}, {}
         ids = {b["暫編地號"] for b in build}
         for b in build:
@@ -226,7 +241,7 @@ def _w1():
 
 def _go(world, *, own_upd=None, a_upd=None, drop=("X1(1)",), cap=None, price=None, gmap=None, err_cap=None,
         units=None, unit_g=None, pre=None, extra=None, rm=(), blk_upd=None, geom_upd=None, cl_upd=None, orig_upd=None,
-        need=None, nodg=False):
+        need=None, nodg=False, units_if=None):
     t, own, blocks, cl = world()
     for e in (extra or []):
         t.append(copy.deepcopy(e))
@@ -243,7 +258,7 @@ def _go(world, *, own_upd=None, a_upd=None, drop=("X1(1)",), cap=None, price=Non
     for pid, kv in (pre or {}).items():
         next(x for x in t if x["暫編地號"] == pid).update(kv)
     build = [x for x in t if x["街廓分類"] == H]
-    ap, st = _cbs(cap, price, drop, gmap, err_cap, units, unit_g, need, nodg)
+    ap, st = _cbs(cap, price, drop, gmap, err_cap, units, unit_g, need, nodg, units_if)
     return _NS["fn"](t, build, own, blocks, cl, ap, st, log_print=lambda *x: None), t, build
 
 
@@ -579,6 +594,14 @@ def _cases(ns, sp):
          lambda: (lambda r: (_rows4(r), _keys(r), _acc(r)))(
              _go(W, drop=("X1(1)", "X1(2)"), rm=RM4, need={"X1(2)": 360.0}, cap={"BB": 50.0})),
          ([("X1(1)", "X1(2)", (), "未成", "BB 配餘地不合格")], {}, {}))
+    # 🆕 `W-G.9-383` 補令一（唯讀審查 #13·K-6 典 W-G.9-383 節之四之戊）：受併之片為他宗之單元之成員 ⇒ 其標記隨單元存續
+    _run(out, "K60 再試成而受併之片 X1(2) 為同地主之 Y1(1)（宿主）之單元之成員 ⇒ 單元之取代（X1(2) 出 build）之後，"
+              "Y1(1) 之單元帶 第31條第3款併入 ['X1(1)']（⛔ 失）",
+         lambda: (lambda r: (_rows4(r), _unit_rows(r), _mark4(r)))(
+             _go(W, drop=("X1(1)", "X1(2)", "Y1(1)"), rm=RM4, own_upd={"Y1": "g1"},
+                 units_if={"Y1(1)": (["X1(2)", "Y1(1)"], "X1(2)", 360.0)})),
+         ([("X1(1)", "X1(2)", (("X1(2)", 60.0),), "成", None)], [("Y1(1)", "取代")],
+          ({"X1(2)": ["X1(1)"], "Y1(1)": ["X1(1)"]}, ["C8(1)", "C9(1)", "Q1(1)", "Q2(1)", "Y1(1)", "Z1(1)"])))
     return out
 
 
````

## 附錄乙′　塊 `Fy33`（`git apply` 之差異·`app.py`·工項二′·施於工項二之碼之上）

````diff
diff --git a/app.py b/app.py
index 3eb87c9..f4cb591 100644
--- a/app.py
+++ b/app.py
@@ -15384,10 +15384,12 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
       （值 ＝ 所併入之片）；「不影響原位次」之檢核過且受併之片（或其所屬單元）於試算中配地 ⇒ 成（施之·其後之分量以施後之態與
       試算判之）；否則未成（⛔ 施）。逐一餘片記一列（置於紀錄之首）。有成者 ⇒ 以施後之態重算 `C0`（重行其二查）；成者之餘片
       ⛔ 入受詞、帶 `段三併出` ＝ 其既有之集 ∪ {受併之片}。上文「無受詞 ⇒ 輸入之同一物件與 `[]`」改為：無受詞而無成者 ⇒ 輸入
-      之同一物件與再試之列；有成者 ⇒ 照常輸出。停機另增：再試之受詞存在而試算之 `kept` 非 dict、`dropped` 未回或其型不合、
+      之同一物件與再試之列；有成者 ⇒ 照常輸出。停機另增：逐分量判之時當下之試算之 `kept` 非 dict、`dropped` 未回或其型不合、
       其暫編地號重見、其 G 缺、片之所屬單元⛔ 在其中（⛔ 以 0 代之）。
       計畫 (1) 之「與片直接相接且其原地號同於該片」改以同號之連通分量為準：他街廓之已配得之宗之成員在片之同號之連通分量
       （⛔ 片自身）者。
+    🔧 `W-G.9-383` 補令一（唯讀審查 #13·`K-6` 典 `W-G.9-383` 節之四之戊）：入池閘之合併單元之取代時，自 build 去之成員之
+      標記（其值）併入單元之同鍵（聯集·字典序）——受併之片為他宗之單元之成員者，其標記隨單元存續。
     """
     import copy as _cp953
     from shapely.geometry import Polygon as _Pg953, LineString as _Ln953
@@ -15678,6 +15680,12 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
                   for _tq in _cp953.deepcopy(state["temp"])]
         _oth953 = set(_mem953(_h953)) | {str(_m) for _m in (C0['members'].get(_h953) or [])}
         _oth953.discard(_h953)
+        # 🔧 `W-G.9-383` 補令一（R-12·唯讀審查 #13）：自 build 去之成員之標記併入單元之同鍵（聯集·字典序）
+        _mv953 = {str(_v953) for _m953 in _oth953 if _m953 in state["by"]
+                  for _v953 in (state["by"][_m953].get('第31條第3款併入') or [])}
+        if _mv953:
+            _u953 = next(_tq for _tq in _nt953 if str(_tq['暫編地號']) == _h953)
+            _u953['第31條第3款併入'] = sorted(set(_u953.get('第31條第3款併入') or []) | _mv953)
         _nb953 = [str(_bq953['暫編地號']) for _bq953 in state["build"]
                   if str(_bq953['暫編地號']) not in _oth953]
         _cand_st = _mk953(_nt953, _nb953)
````

SELF_SHA256: 0d38b4f36005f7d8c41df91b67cd4c6d6ad36e19db37030a8c57913039a80776
