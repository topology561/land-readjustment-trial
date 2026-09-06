# W-G.9-243R（段乙）　排序準據 **seam 抽出**（射程乙·四站）　執行報告

> 🔴 **生產碼**。本 commit **⛔ 已 push**——依單 `§六 e`，須先出完整 diff ＋ `V-1`／`V-2`／`V-3` 上呈，
> **俟 KL 逐字放行**後方得 push。本報告即該上呈之倉內本體。
> 🔒 **只動 `verify/wf_f4.py` 一檔**；其餘九檔（`wf_f0`／`wf_f1`／`wf_f2`／`wf_f3` ＋ 閘 `P` 五檔）**逐位不變**（`V-3`）。
> 🔒 **⛔ 執行 `verify/run_all.py`／`run_verification.py`**（單之明令·本批未跑）。

---

## §零　態錨

| 項 | 值 |
|---|---|
| 段甲之終態（本段之父）| `90157ee`（已 push·`origin/wip/s1-endpart`）|
| `verify/wf_f4.py` 改前 `sha256` | `c40295c3f8cf8686d630e1402e42886c3a178fae7d5efb883b617d7b8856779b` |
| `verify/wf_f4.py` 改後 `sha256` | `b36aeca6c4f6b364b8551e1c074a22e284f1d1b1c9892aa16bf755be10402a83` |
| `git diff --stat` | `verify/wf_f4.py | 38 ++++----` ⇒ **34 增／4 刪**（**單檔**）|
| `py_compile` | `rc = 0` ✅ |

---

## §一　射程（單 `§六 a`·乙案四站·全在 `verify/wf_f4.py`）

| 站 | 改前逐字 | 改後逐字 |
|---|---|---|
| `:433`（改後 `:463`）| `anchor = max(lots, key=lambda x: (x["a"], x["pid"]))` | `anchor = max(lots, key=_SORT_KEYS["anchor"])` |
| `:488`（改後 `:518`）| `border = {gid: sorted(mina, key=lambda b: (_level(gid, b), dists[(gid, b)], b))` | `border = {gid: sorted(mina, key=lambda b: _SORT_KEYS["border"](b, gid, _level, dists))` |
| `:663`（改後 `:693`）| `                                     key=lambda g: (min(dists[(g, b)] for b in mina), g))` | `                                     key=lambda g: _SORT_KEYS["queue"](g, dists, mina))` |
| `:689`（改後 `:719`）| `gs = sorted(requests[blk], key=lambda g: (dists[(g, blk)], g))   # 裁定K：距離優先` | `gs = sorted(requests[blk], key=lambda g: _SORT_KEYS["share"](g, blk, dists))   # 裁定K：距離優先` |

🔒 **⛔ 及於** `-242R` `A` 桶其餘 **15** 站（標的宗選定、`§7-5` 第2梯、F.2／E0 目標塊宗選定、分攤剔除 `:703`）——**一字未動**。

---

## §二　`V-1`　靜態等價之逐行人閱（單 `§六 d`）

**新增之四 provider ＋ registry（module 級·置於 `E1_MARGIN` 之後、`_money` 之前）**

```python
def _key_anchor(x):
    """歸戶錨點宗之選定鍵（原 `:433` lambda）；x ＝ 公設宗 dict。"""
    return (x["a"], x["pid"])


def _key_border(b, gid, level_fn, dists):
    """區位順序鍵（原 `:488` lambda）：級 → 距離 → 街廓 label。"""
    return (level_fn(gid, b), dists[(gid, b)], b)


def _key_queue(g, dists, mina):
    """E1 全域佇列鍵（原 `:662`–`:663` lambda）：至最近可達塊之距 → gid。"""
    return (min(dists[(g, b)] for b in mina), g)


def _key_share(g, blk, dists):
    """同塊分攤序鍵（原 `:689` lambda）：距該塊之距 → gid。"""
    return (dists[(g, blk)], g)


_SORT_KEYS = {"anchor": _key_anchor, "border": _key_border,
              "queue": _key_queue, "share": _key_share}
```

**逐站併列與差之指認（單令：差**僅**在名字與參數傳遞）**

| 站 | 改前 lambda 之**回傳式** | 改後 provider 之**回傳式** | 差 |
|---|---|---|---|
| `anchor` | `(x["a"], x["pid"])` | `(x["a"], x["pid"])` | **逐字相同**；差僅在「由 lambda 改為具名 `def`」|
| `border` | `(_level(gid, b), dists[(gid, b)], b)` | `(level_fn(gid, b), dists[(gid, b)], b)` | 差僅 `_level` → **形參名** `level_fn`（呼叫端傳入 `_level` 本身）|
| `queue` | `(min(dists[(g, b)] for b in mina), g)` | `(min(dists[(g, b)] for b in mina), g)` | **逐字相同**；`dists`／`mina` 由自由變數改為**形參** |
| `share` | `(dists[(g, blk)], g)` | `(dists[(g, blk)], g)` | **逐字相同**；`blk`／`dists` 由自由變數改為**形參** |

🔒 **逐項確認（單所令之「凡出現任何算式、比較子、tie 次序之改動 ⇒ 停機」）**
- **算式**：四式之運算子與呼叫**一字未增未減**（`min(...)` 之生成式亦逐字相同）。
- **比較子**：四式皆回傳 `tuple`，其**元素個數與順序**未變（`2`／`3`／`2`／`2`）。
- **tie 次序**：末元素之 tiebreak 未變（`x["pid"]`／`b`／`g`／`g`）。
- **升降序**：四站原本即無 `reverse=`／負號，改後亦無。
- ⇒ **⛔ 觸發停機**。

🔒 **`_level`／`LV`／`dists`／`med`／`mina`／`adj_pub` 之算法一字未動**——
diff 之三個 hunk（`@@ -430`／`@@ -485`／`@@ -660`／`@@ -686`）皆只改該一列之 `key=`，
`_level`（`:483`–`:486`）與 `LV`（`:487`）出現於 hunk 之**上下文列**（前綴空白）而**非變更列**。

🛑 **一處<u>與單之逐字形相異</u>，須具名並候裁**
單 `§六 b` 款 `3` 作「呼叫端改為 `key=lambda x: _key_<name>(x, …)`（或直接 `key=_key_<name>`）」，
款 `4` 則令「置一 registry 作**單一掛點**」。
**本批取 `_SORT_KEYS["<name>"]` 作呼叫端**（而非直呼 `_key_<name>`），其理由：
> 若呼叫端直呼 `_key_<name>`，則 `_SORT_KEYS` **無任何讀者** ⇒ 成為「**建置未接線**」
> ——該形係本倉已多次登記之紅（如 `_k923_gate2` 生產呼叫點 `0`、`_rect_fits_free_pose` 建置未接線），
> 且 registry 將**不成其為掛點**，款 `4` 之目的落空。

🔒 **該取捨⛔ 引入任何款 `5` 所禁之物**：registry 每鍵**只有一個實作**，
**⛔ 開關、⛔ 參數化準據、⛔ 條件分支、⛔ 預留 `if` 位**（`V-2` 已機驗其四值 `is` 各具名 provider）。
🛑 **是否改為款 `3` 之逐字形（直呼 `_key_<name>`）＝ 意思決定 ⇒ 候發單側／KL**；一行之改，隨時可回。

---

## §三　`V-2`　單元級逐位對拍（拋棄式·**⛔ 入倉**·⛔ 動 `verify/`）

🔒 **工法**：於**同一 process** 內，(1) 自 `135316e` 之 blob **逐字抄錄**原四 lambda 為 `OLD_*`；
(2) **import 真模組** `verify/wf_f4.py` 取 `_SORT_KEYS` 之四值（**⛔ 另抄一份新碼**）；
(3) 比對**鍵之 tuple 逐位相同**（含 `type` 逐元素）＋ **`sorted`／`max` 之結果序相同**。
🔒 **輸入係<u>合成</u>**（因二情境皆於 `R2` 中止，`F.2`／`F.4` 一筆未產 ⇒ 真實輸入不可得）——
其覆蓋逐項具名於下表；**⛔ 讀為真實資料之迴歸**。

| 站 | 合成輸入 | 覆蓋之型別與邊界（含 **tie**）|
|---|---|---|
| `anchor` `:433` | `5` 個公設宗 dict | `a` 相異／**`a` 同值而 `pid` 相異之 tie ×3**（`30.0` 三筆）／`a = 0.0` 之邊界 |
| `border` `:488` | `4` 個街廓 label ＋ 合成 `_level`／`dists` | 級相異（`0`／`1`／`2`）／**同級同距而 label 相異之 tie**（`R2`·`R3` 皆級 `1`、距 `25.0`）|
| `queue` `:662` | `3` 個 gid ＋ `2` 塊之 `dists` | `min` 取自多塊／**最近距同值而 gid 相異之 tie**（`G001`·`G002` 皆 `5.0`）|
| `share` `:689` | `3` 個 gid ＋ 單塊之 `dists` | 距相異／**同距而 gid 相異之 tie**（`G007`·`G002` 皆 `8.0`）|

**結果**

| 量 | 值 |
|---|---|
| 鍵之逐位對拍筆數 | **15** |
| **不符筆數** | **0**（須 `0`）✅ |
| 結果序比較次數 | **5**（四站各一 `sorted` ＋ 站1 之 `max`），**皆相同** ✅ |
| registry 身分檢 | `_SORT_KEYS` 之四值 **`is`** 各具名 provider ✅；鍵集 ＝ `['anchor','border','queue','share']`（4 鍵·每鍵一實作）|
| **判別力自證** | 以**蓄意相異之鍵**（顛倒欄序 `(x["pid"], x["a"])`）比對 ⇒ **被抓到 ＝ True** ✅（⇒ 該測**非恆綠**）|

**四站之結果序（合成輸入下）**：`border` ⇒ `['R1','R2','R3','R4']`；
`queue` ⇒ `['G003','G001','G002']`；`share` ⇒ `['G005','G002','G007']`；
`anchor` 之 `max` 與 `sorted` 新舊**同一物件**。

🛑 **`V-2` 之界（逐字·⛔ 隱去）**：其所證者為**鍵函式之等價**，
**⛔ 證** 整體配地結果之等價——後者須 `F.2`／`F.4` 之真實輸出，而該輸出於現態**不可得**
（`-241R §三 c`：二情境皆於 `R2` 中止）。

---

## §四　`V-3`　檔級雜湊（前後各報一次）

| 檔 | 改前 `sha256` 前 16 位 | 改後 | 判 |
|---|---|---|---|
| `verify/wf_f0.py` | `6758ea766b001b95` | `6758ea766b001b95` | ✅ 不變 |
| `verify/wf_f1.py` | `30e19048dfd781bc` | `30e19048dfd781bc` | ✅ 不變 |
| `verify/wf_f2.py` | `f974724d7e694ad7` | `f974724d7e694ad7` | ✅ 不變 |
| `verify/wf_f3.py` | `226c7c5fa00464f3` | `226c7c5fa00464f3` | ✅ 不變 |
| **`verify/wf_f4.py`** | `c40295c3f8cf8686` | **`b36aeca6c4f6b364`** | 🔴 **唯一得變者**（單之明文）|
| `app.py` | `e3e464ea2493d046` | `e3e464ea2493d046` | ✅ 不變 |
| `verify/selection_pipeline.py` | `6c6783420dbc635c` | `6c6783420dbc635c` | ✅ 不變 |
| `verify/run_verification.py` | `e48f24c84079f365` | `e48f24c84079f365` | ✅ 不變 |
| `verify/stepg_pipeline.py` | `0260273350021311` | `0260273350021311` | ✅ 不變 |
| `verify/run_all.py` | `4ba89fef90979491` | `4ba89fef90979491` | ✅ 不變 |

⇒ **十檔中恰一檔變動**，與單之射程一致。

---

## §五　工項五 `f`：待落地登記（`GB` 簿·純末端追加）✅

| 項 | 值 |
|---|---|
| payload 來源 | 本單**第 `246`–`257` 列**（四反引號圍欄 `245`／`258`）|
| 追加量 | **830** B／**15** LF／**CR 0** |
| 改前 | 658566 B・4731 LF・`sha256 3c6e734e42fcd31b…` |
| 改後 | 659396 B・4746 LF・`sha256 bbb6ca5ef5fc2986…` |
| `numstat` | **`15 / 0`** ⇒ `deletions ＝ 0` ✅ |
| 字樣錨 | `閘 \`P\` ⛔ 涵蓋生產路徑上之` **0 → 1**；`import wf_f4 as _wf4` **0 → 1** |

🔒 其要旨：`verify/wf_f0`–`wf_f4` **在 app 之生產路徑上**（`app.py:23844` `import wf_f4 as _wf4`），
而閘 `P` 之五檔**不含** `wf_f*.py` ⇒ **該五檔無雜湊閘**；本單以 `V-3` 之逐批併報代之，登記此缺口候裁。

---

## §六　🛑 放行（**⛔ 繞道**）

- 本 commit **⛔ 已 push**（本地保全 ref ＝ `keep/W-G.9-243-c1`）。
- 上呈之三件已備：`V-1`（§二·含完整 diff 之逐行人閱）／`V-2`（§三）／`V-3`（§四）。
- 🛑 **⛔ 以「段甲已綠」「diff 很小」「純重構」為由自行 push。**
- 🛑 **一項候裁**：呼叫端採 `_SORT_KEYS["<name>"]`（而非款 `3` 之逐字 `_key_<name>`）之理由見 §二末；
  若發單側／KL 裁採逐字形，改動為**四列**，`V-2` 須重跑。
- 🛑 **一項請示**：本倉標準之生產碼流程另有「先推側分支 `verify/<單號>-c<n>` 供發單側逐位復驗」一步；
  本單 `§六 e` 只言「⛔ push、出 diff 上呈」。**是否推側分支 ＝ 意思決定**，本批**未推任何遠端**。

---

## §七　⛔ 未辦（單之明文）

- **⛔ 於本批新增任何替代準據**——registry 每鍵一實作，⛔ 開關／參數化／條件分支／預留 `if` 位。
- **⛔ 動** `_level`（`:483`–`:486`）／`LV`（`:487`）／`dists`／`med`／`mina`／`adj_pub` 之算法。
- **⛔ 動** `wf_f0`／`wf_f1`／`wf_f2`／`wf_f3`／`app.py` 與閘 `P` 五檔（`V-3` 給證）。
- **⛔ 新增任何檔**（provider 置於 `wf_f4.py` 同檔）。
- **⛔ 執行** `verify/run_all.py`／`run_verification.py`（本批未跑·`verify/out/` 無新增）。
- **⛔ 及於** `A` 桶其餘 15 站。
