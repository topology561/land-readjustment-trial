# 🔬 `W-G.9-161R`　`BASE` 三源 ＋ 十二點三類不變式之**落地**（🔴 首張生產碼批）

**單**：`W-G.9-161`（`SELF_SHA256 = 052c6883ece57282df19e6094d0705d75f9f2a7853578e86940afb14296da9de`·CC 覆核**逐位相符**·扣末列）
**基座**：`77ebc492415726272a164bb6f5b9dfd96dec268a`
**`app.py` blob 期初**：`b4cc30835feaad03dfc37f394a669bbb45988b8b`
🔴 **`app.py` blob 期末**：**`8daca97f7b9f520cd1c8fdcfa4823a45f4199395`**（絕對值出艙·`R-12` 符）
**量測時點**：`2026-08-28`　🔒 **母體之態**（`VR-058 三`）＝ **`blob@77ebc49` ＝ 本批基座**

## 🛑 結論先行

| # | 事 | 判 |
|---|---|---|
| `1` | **零行為變更已證**——`Z-2′` 期初／期末逐閘 `diff` **`rc=0`**（逐字相同）；`Z-3′` 正規化後**相異列數 `0`** | ✅ |
| `2` | **判別力已證**——`D-1`〜`D-5` **`5／5` 三項齊備**（正向對照不紅／擾動紅／訊息含受詞） | ✅ |
| `3` | 🔴 **`R-5`／`R-8` 不符**——`baseline` 閘與 `run_all` 於**基座即紅**（**准紅碼**·`CLAUDE.md` 明載本分支驗收改為「與凍存之期望 FAIL 名單逐項相同」·**⛔ 非全綠**） | 🛑 **停機回報** |
| `4` | 🔴 **`R-9` 不符**——`run_all` 一趟中 `14` 個 tag 有 **`7` 個執行次數 ＝ `0`**（成因二類·逐點具名） | ⚠️ 單已標⛔ 非停機 |
| `5` | **`deletions` 逐列 ＝ `0`**——本批之生產碼變更**全為純附加**（單原預期 `> 0`） | ℹ️ |

🔒 **⛔ 未為使 `Z-1′`〜`Z-4′` 轉綠而修改濾式、放寬容差、或關閉斷言**（單 `§八` 逐字）。

### 異動清單（`git diff --numstat 77ebc49 -- .`）

```text
219	0	app.py
21	0	docs/reports/W-G.9波_claude.ai側自誤登記.md
28	0	docs/驗證裁定登記表.md
3	0	verify/selection_pipeline.py
6	0	verify/stepg_pipeline.py
3	0	verify/wf_f0.py
2	0	verify/wf_f1.py
3	0	verify/wf_f2.py
3	0	verify/wf_f3.py
11	0	verify/wf_f4.py
```

---

## §一　取號現查（🛑 CC 自跑·裸框與錨定框二數並報·態 ＝ 本批基座）

🔒 **母體** ＝ `docs/**/*.md` ＋ `CLAUDE.md` ⇒ **`389` 檔**（態 ＝ `blob@77ebc49`）

| 待鑄 | 定義列式 | 該式 MAX | 裸框 列／次 | 錨定框 列／次 | 對照組 | 判 |
|---|---|---|---|---|---|---|
| `W-G.9-161` | `^docs/reports/W-G\.9-(\d{1,4})` | `160` | `1`／`1` | `1`／`1` | `W-G.9-160` ⇒ `8`／`8` | ✅ 未占用（唯一命中 ＝ `160R:184` 之**前瞻引用**·其意指正為本單） |
| 自誤 `195` | `^#+ 自誤 \`?([0-9]{1,4})\`?` | **`194`** | `0`／`0` | `0`／`0` | `自誤 \`194\`` ⇒ `3`／`3` | ✅ 未占用 |
| `VR` | `^##\s*\`VR-([0-9]{1,4})\`` | `76` | — | — | — | 🔒 **本批⛔ 不鑄新 `VR`**（以就地加註更正） |

🩸 **CC 自捕之量測器紅（⛔ 未出艙）**：首版之對照組取裸框 `自誤 194`（**⛔ 無反引號**）得 **`0`**
⇒ 對照組為零 ⇒ **量測器紅**。查因：其標題形逐字為 `### 自誤 \`194\`（…）`（**帶反引號**）。
🔴 **併報一新面**：自誤號於倉內**二形並存**——`自誤 193`（無反引號）得 `4` 列／`自誤 \`193\`` 得 `6` 列
⇒ 🛑 **意指占用之搜尋須<u>二形並取</u>**，單一形必漏。

🔒 **常規四（九）① 形之自證**（⛔ 附加前）：自誤之定義列式掃 payload 命中 **`1`**；
**② MAX 之推進**：`194` → **`195`**（`docs/reports/W-G.9波_claude.ai側自誤登記.md:3674`）。
🔒 **路徑現查**（`R-2`·承 `自誤 195 肢①` 之新戒）：`docs/驗證裁定登記表.md` **存在 ＝ True**；
`docs/reports/驗證裁定登記表.md` **存在 ＝ False** ⇒ 本批附於前者。

---

## §二　`§八-6`　常規七 逐字覆抽（`§一` 七列之碼面錨 ＋ `R-4` 二端·自**基座 blob**）

```text
verify/wf_f0.py:408｜            oA = _proj_order(ns, cad, c["build"], blk)
verify/wf_f0.py:409｜            oB = _proj_order(ns, cad, f0_parcels, blk)
verify/wf_f0.py:410｜            exp = [x for x in oA if x not in removed]   # 約簡序
verify/wf_f0.py:411｜            if oB != exp:

verify/wf_f2.py:251｜            oB = _proj_order(ns, cad, f0_parcels, blk)
verify/wf_f2.py:252｜            oC = _proj_order(ns, cad, f2_parcels, blk)
verify/wf_f2.py:253｜            exp = [x for x in oB if x not in remove2]
verify/wf_f2.py:254｜            if oC != exp:
verify/wf_f2.py:255｜                pos_viol.append((blk, exp, oC))

verify/wf_f3.py:191｜            oC = _proj_order(ns, cad, f2_parcels, blk)
verify/wf_f3.py:192｜            oD = _proj_order(ns, cad, f3_parcels, blk)
verify/wf_f3.py:193｜            if oC != oD:
verify/wf_f3.py:194｜                pos_viol.append((blk, oC, oD))

verify/wf_f4.py:978｜            oD = _proj_order(ns, cad, f3_out[tag]["f3_parcels"], blk)
verify/wf_f4.py:979｜            oE = _proj_order(ns, cad, eng.parcels, blk)
verify/wf_f4.py:980｜            removed_all = _rm0 | set(rm2)
verify/wf_f4.py:981｜            exp = [x for x in oD if x not in removed_all]
verify/wf_f4.py:982｜            got = [x for x in oE if not x.startswith("74·")]
verify/wf_f4.py:983｜            if got != exp:
verify/wf_f4.py:984｜                pos_viol.append((blk, exp, got))

verify/wf_f1.py:377｜        oB = _order({r["暫編地號"]: _poly_of(r) for r in r1_lots})
verify/wf_f1.py:378｜        oN = _order(new_polys)
verify/wf_f1.py:379｜        if oB != oN:

verify/wf_f4.py:1434｜            _oE = _order_fb({r["暫編地號"]: _poly_of_row(r) for r in lots})
verify/wf_f4.py:1435｜            _oN = [k for k in _order_fb(fb_polys) if k != _abate_key]

verify/wf_f4.py:1504｜    oE = _order({r["暫編地號"]: _poly_of_row(r) for r in lots})
verify/wf_f4.py:1505｜    oN = _order(new_polys)
verify/wf_f4.py:1506｜    if oE != oN:

app.py:20037｜                                parcels_in_block=_stage1_parcels,   # P2-a：僅階段1宗
verify/stepg_pipeline.py:480｜                parcels_in_block=_stage1_parcels,   # P2-a：僅階段1宗（遞補宗改走 _place_pool_parcels）
```

🔒 **九處皆與單所載逐位相符** ⇒ `R-3`／`R-4` **符**、⛔ 不停機。

---

## §三　落地之實作（`L-1′`〜`L-6′`）

### `L-2′` 宣告表——**一處**（`app.py` 之 `_PROJ_POP_DECL`·**14** 列）

| # | `tag` | 受詞類 | `source` | `filter` | `run_all` 一趟之執行次數 |
|---|---|---|---|---|---|
| `1` | `app:v2/pre_seq` | `POP_SYNC` | `BUILD_LAYER` | `passthrough` | **16** |
| `2` | `app:main/v2_caller` | `POP_SYNC` | `BUILD_LAYER` | `stage1` | 🔴 **`0`** |
| `3` | `stepg:v2_caller` | `POP_SYNC` | `BUILD_LAYER` | `stage1` | **16** |
| `4` | `app:main/_rank_by_tpid` | `POP_SYNC` | `BUILD_LAYER` | `identity` | 🔴 **`0`** |
| `5` | `sp:_rank_by_tpid` | `POP_SYNC` | `BUILD_LAYER` | `identity` | **102** |
| `6` | `stepg:_proj_rank` | `POP_SYNC` | `BUILD_LAYER` | `stage1` | **16** |
| `7` | `wf_f0:_proj_order` | `ORDER_INVARIANCE` | `BUILD_LAYER` | `no_ghost` | 🔴 **`0`** |
| `8` | `wf_f2:_proj_order` | `ORDER_INVARIANCE` | `BUILD_LAYER` | `no_ghost` | 🔴 **`0`** |
| `9` | `wf_f3:_proj_order` | `ORDER_INVARIANCE` | `BUILD_LAYER` | `no_ghost` | 🔴 **`0`** |
| `10` | `wf_f4:_proj_order` | `ORDER_INVARIANCE` | `BUILD_LAYER` | `no_ghost` | 🔴 **`0`** |
| `11` | `wf_f1:_order` | `ORDER_INVARIANCE` | `RESHAPE` | `pseudo_of` | 🔴 **`0`** |
| `12` | `wf_f4:_order_fb` | `ORDER_INVARIANCE` | `RESHAPE` | `pseudo_of` | **2** |
| `13` | `wf_f4:_order` | `ORDER_INVARIANCE` | `RESHAPE` | `pseudo_of` | **22** |
| `14` | `app:k6step0/_ordered` | `NAME_DERIVATION` | `TEMP_LAYER` | `group_members` | **80** |

🔒 **`14` 列 ＝ `12` 呼叫點 ＋ `2` 透傳呼叫端**（`app:v2/pre_seq` 之宣告繫於呼叫端·`L-3′`）。
🔒 **`R-11`**：`filter` 之相異值 ＝ **6** 類 ＝ `group_members`／`identity`／`no_ghost`／`passthrough`／`pseudo_of`／`stage1`
⇒ 與單所列六類（`identity`／`stage1`／`no_ghost`／`group_members`／`passthrough`／`pseudo_of`）**逐字相符** ⇒ `R-11` **符**。

### `L-3′` 三類不變式之落點（**⛔ 未動碼面既有之七處序對拍一字**）

| 受詞類 | 落點 | 式 |
|---|---|---|
| `POP_SYNC` | `app.py`（`_spatial_order_parcels_v2`／`main` ×2）／`sp`／`stepg` ×2 | 實參之暫編地號序列 ≡ `filter(source)`（**逐位相同**） |
| `ORDER_INVARIANCE` | `wf_f0`／`f1`／`f2`／`f3`／`f4` ×3 之**對拍處** | **宣告式差集**：`set(前)−set(後) ≡ removed` ∧ `set(後)−set(前) ≡ added` |
| `NAME_DERIVATION` | `app.py`（K-6 §二 步驟 0） | `_mem` ⊆ `TEMP_LAYER(該街廓)`（**非空真斷言**） |

🔒 **`NAME_DERIVATION` 之 `TEMP_LAYER` 就地重算**（⛔ 不取 `_idxs`）——否則為套套邏輯：

```python
            _proj_pop_assert_subset(
                "app:k6step0/_ordered", _mem,
                [_tp_pp for _tp_pp in temp_parcels
                 if str(_tp_pp.get("所屬街廓", "") or "") == _lbl], blk=_lbl)
```

🔒 **`wf_f4:_order_fb` 之處置**：對拍須用**未排除抵費地末**之原序 ⇒ **另取** `_oN_raw`，
⛔ **未動** `_oN = [k for k in _order_fb(fb_polys) if k != _abate_key]` 一字。

### `L-4′`／`L-6′`

🔒 一切斷言為 `raise`；⛔ 無 warn／log-only／環境變數開關／harness-only 分支。
🔒 `L-6′` 之計數（`WV_PROJ_POP_COUNT`）**僅寫檔**，其失敗以 `pass` 吞掉——
🛑 **⛔ 不影響斷言之執行**（斷言在 `_proj_pop_note()` **之後**且不依賴其結果）。

---

## §四　`§四`　零行為變更之證明（`Z-1′`〜`Z-4′`·四項全數提出）

### `Z-2′`（**本批最強之證**）：`run_all` 期初／期末**逐閘並列**

| 項 | 期初（基座·未動碼） | 期末（本批） | 判 |
|---|---|---|---|
| `RESULT:` | `FAIL` | `FAIL` | ＝ |
| `W-V run_all:` | `FAIL`（`EXIT=1`） | `FAIL`（`EXIT=1`） | ＝ |
| `✅ PASS` 計數 | **`11`** | **`11`** | ＝ |
| `🔴 FAIL` 計數 | **`23`** | **`23`** | ＝ |
| 對帳器 `類 III` | **`13` 項** | **`13` 項** | ＝ |
| 對帳結論 | `🔴 對帳 FAIL` | `🔴 對帳 FAIL` | ＝ |
| **逐閘名目＋狀態之 `diff`** | — | — | 🔒 **`rc = 0`（`34` 閘逐字相同）** |

🔒 **取法**：`grep -n "^  ✅ PASS\|^  🔴 FAIL"` 之輸出去行號後 `diff` ⇒ **空**。

### `Z-1′`　九份 baseline 對拍

🔒 baseline 相關之閘（`v3·診斷`／`率接線`／`指配`／`抵費地`／`W-F F.0`〜`F.4`／`W-D.3`／`W-D.4`／`W-G G.1`／`G.2`）
**期初／期末逐字相同**（含於上之 `34` 閘 `diff`）。
🔴 **惟其中多數於<u>基座即為 `FAIL`</u>** ⇒ `R-5`「全綠」**不符**（詳 `§六`）。

### `Z-3′`　`probe_WG9156` 重跑

| 項 | 值 |
|---|---|
| 原 log（倉內·`blob@77ebc49`） | `421` 列·`sha16 37357cc36429232b` |
| 重跑 log（期末碼） | `421` 列·`sha16 9a3b44f06870c9f8` |
| 未正規化之相異列 | `28`（**全為 `HEAD` 一列 ＋ `app.py:<行號>` 位移**·`9981`→`10188`／`9996`→`10203`·因插入 `206` 列） |
| 🔒 **正規化後之相異列數** | **`0`**（`sha16` 二側皆 `eff82d3ffe7772e7`） |

🔒 **判別力自檢**（證正規化⛔ 非把一切抹平）：**未**正規化之二 `sha16` **相異**（`37357cc3` vs `9a3b44f0`）。
🔒 **⇒ 八格 `[a]`〜`[j]` 之原始量、藍影、`G`、遞補鏈、騰出面積<u>逐格逐欄不變</u>** ⇒ `R-7` **符**。

### `Z-4′`　`run_all` ＋ 跨 process 計數

**①** `run_all.py` 期末 ＝ `FAIL`（`EXIT=1`）——🔴 **惟基座即 `FAIL`**（見 `Z-2′`）⇒ `R-8` 不符（`§六`）。
🔒 **本批⛔ 未新增任何 FAIL**：`34` 閘之名目與狀態**逐字未變**。
**②** 逐點執行次數見 `§三` 之表（自 `L-6′` 之檔案·`254` 次／`7` 個 tag）。
**③** **次數為 `0` 之 `7` 點**及其不可達成因（逐點具名）：

| tag | 成因 |
|---|---|
| `app:main/v2_caller` | 在 `app.py` `main()` 內（`13444`–`22609`）⇒ `CLAUDE.md` 逐字「**`main()` 內之敘述從不被 `run_all` 執行**」 |
| `app:main/_rank_by_tpid` | 同上 |
| `wf_f0:_proj_order` | 在 `wf_f0.compute` 之主路徑；`run_verification` 於 trunk A 之 `②-宗 圍堵閘破[R2]` 即中止 ⇒ `wf_f0`〜`f4` 主路徑未執行 |
| `wf_f2:_proj_order` | 同上 |
| `wf_f3:_proj_order` | 同上 |
| `wf_f4:_proj_order` | 同上 |
| `wf_f1:_order` | 同上 |

🔒 **對照（證「子行程確會執行」·`VR-076 S-D` 之裁成立）**：`wf_f4:_order_fb` ＝ **`2`** 次、
`wf_f4:_order` ＝ **`22`** 次——二者皆由 `run_all.py:181` 之 **fixture subprocess** 驅動
（`fixture_end_fallback`／`fixture_end_winner`）⇒ **斷言於子行程確實執行且未觸發**。

---

## §五　`§五`　判別力對照 `D-1`〜`D-5`（**5／5 三項齊備**）

🔒 探針：`verify/probes/probe_WG9161_discrim.py`（擾動**僅於執行期**·⛔ 未留於出艙生產碼）

| # | 擾動 | 正向對照（須不紅） | 擾動（須紅） | 訊息含受詞 | 判 |
|---|---|---|---|---|---|
| `D-1` | `POP_SYNC` 實參移除 `628-42(1)` | `False` ✅ | `True` ✅ | 對稱差 ＝ `['628-42(1)']` ✅ | ✅ |
| `D-2` | 宣告 `filter` `stage1`→`identity`（⛔ 不改實參） | 還原後 `False` ✅ | `True` ✅ | 訊息含 `identity` ✅ | ✅ |
| `D-3` | `_mem` 注入 `R5` 之 `628-99(1)` | `False` ✅ | `True` ✅ | 只在實參 ＝ `['628-99(1)']` ✅ | ✅ |
| `D-4` | `wf_f4:_order_fb` 之 `added` `{_abate_key}`→`∅` | `False` ✅ | `True` ✅ | 對稱差 ＝ `['74·抵費地末']` ✅ | ✅ |
| `D-5` | `wf_f3:_proj_order`（宣告 `∅`）後呼叫注入 `628-99(9)` | `False` ✅ | `True` ✅ | 對稱差 ＝ `['628-99(9)']` ✅ | ✅ |

🔒 **三項併證**（CC 自加）：
① `⊆` 之**空真**亦 `raise`（實參為空 ⇒ 紅）——⛔ 不得以空真作為通過；
② 向宣告 `empty` 之側傳入非空 ⇒ `raise`（**型別自檢**）——⇒ `∅` 之宣告⛔ 非空轉；
③ **未宣告之 `tag` ⇒ `raise`**——⇒ 新增呼叫點必被逼入 `L-2′` 表。

🔒 **`D-4`／`D-5` 為一對**（單 `§五` 逐字）：前者證非 `∅` 之宣告被讀、後者證 `∅` 之宣告非空轉——**二者皆紅** ✅。

---

## §六　`§六` 十二項驗收預測之逐項對拍（🛑 **⛔ 未改任何預測**）

| # | 預測 | 實得 | 判 |
|---|---|---|---|
| `R-1` | 自誤 MAX ＝ `194` ⇒ 取 `195`；`VR` MAX ＝ `76`（⛔ 不鑄新 `VR`） | 自誤 MAX `194`／`195` 二框皆 `0`；`VR` MAX `76`·未鑄 | ✅ **符** |
| `R-2` | `docs/驗證裁定登記表.md` 存在；`docs/reports/…` ⛔ 不存在 | `True`／`False` | ✅ **符** |
| `R-3` | `§一` 七列之碼面錨逐位相符 | 七處逐位相符（`§二`） | ✅ **符** |
| `R-4` | `app.py:20037` 與 `stepg:480` 二端皆餵 `_stage1_parcels` | 二端逐字相符（`§二`） | ✅ **符** |
| `R-5` | 🔴 `Z-1′` 九份 baseline **全綠** | 🔴 baseline 閘於**基座即多數 `FAIL`**（准紅碼）；**期初 ≡ 期末** | 🔴 **不符**（🛑 見下） |
| `R-6` | 🔴 `Z-2′` 期初／期末逐閘**相同** | **`34` 閘 `diff rc=0`**·`11 PASS`／`23 FAIL`／對帳 `類 III 13` 皆同 | ✅ **符** |
| `R-7` | 🔴 `Z-3′` 八格逐欄**不變** | 正規化後**相異列數 `0`**（`sha16` 相同） | ✅ **符** |
| `R-8` | 🔴 `Z-4′①` `run_all.py` **全綠** | `FAIL`（`EXIT=1`）——🔴 **基座即 `FAIL`**；本批**未新增任何 FAIL** | 🔴 **不符**（🛑 見下） |
| `R-9` | `run_all` 一趟使全部 `12` 點次數 `>0` | `14` tag 中 **`7` 個為 `0`**（成因二類·逐點具名於 `§四`） | 🔴 **不符**（單已標⛔ 非停機） |
| `R-10` | `D-1`〜`D-5` 各至少一次 `raise` | **`5／5` 三項齊備** ＋ 三項併證 | ✅ **符** |
| `R-11` | `filter` 相異值 ＝ **六**類 | ``group_members`／`identity`／`no_ghost`／`passthrough`／`pseudo_of`／`stage1``（**6** 類） | ✅ **符** |
| `R-12` | `app.py` blob 期末 ≠ `b4cc3083…` | **`8daca97f7b9f520cd1c8fdcfa4823a45f4199395`** | ✅ **符** |

⇒ **符 `9`／不符 `3`（`R-5`／`R-8`／`R-9`）／不可判 `0`**。

### 🛑 `R-5`／`R-8` 不符之**具名**（依單 `§六`：任一不符 ⇒ 停機回報）

🔒 **二者之不符<u>皆非本批所致</u>**——**基座（`77ebc49`·未動一位元碼）之 `run_all` 即為 `FAIL`**：
`RESULT: FAIL`／`W-V run_all: FAIL`／`EXIT=1`／`11 PASS`／`23 FAIL`／對帳 `類 III` `13` 項。

🔒 **`CLAUDE.md` 已明載本分支之驗收基準**（逐字）：

```text
CLAUDE.md:70｜    **非 regression、非資料壞、非施工可致**；錨待**波末重烤**更新。
CLAUDE.md:71｜    ⇒ 期間之驗收改為 **「與凍存之期望 FAIL 名單逐項相同」**，⛔ **非「全綠」**。
CLAUDE.md:72｜    凍存名單：`verify/out/K6A2_期望FAIL名單_902f5d1.txt`（**逐項名目**·⛔ 非計數）。
CLAUDE.md:73｜    **案由**：在此之前，「紅但沒變壞」只靠**整檔 md5／`diff` 相同**撐著
CLAUDE.md:74｜    ——一有**合法**變更（新增一支夾具、多印一行診斷）即失效，屆時無從分辨
```

⇒ 🔒 **本分支現為「准紅碼」，其驗收為「與凍存之期望 FAIL 名單逐項相同」，⛔ 非「全綠」**
⇒ `R-5`／`R-8` 之**字面前提於基座即不成立**。
🔒 **本批就該基準之表現 ＝ 逐閘逐字未變**（`Z-2′` `diff rc=0`）⇒ **零行為變更成立**。
🛑 **CC ⛔ 未為使其轉綠而改任何濾式／容差／斷言**；`R-5`／`R-8` 之判準是否應改寫為
「期初 ≡ 期末」，**由發單側落筆**。

---

## §七　`§七` 不辦事項之逐項確認

⛔ 未落地 `VR-074`／`VR-075`；⛔ 未落地 `K-9-23` 二閘／`K-9-16`／`K-9-17`／`K-9-12`／`K-9-13`；
⛔ 未寫遞補迴圈；⛔ 未補 `GB-104` 之 loud 斷言；⛔ 未解除 `GB-105`／`GB-110`；
⛔ 未重產 baseline；⛔ 未動 `data/`；⛔ 未改任何既有 `docs/` 文字。

🔒 **`L-5′` 之逐項確認**：⛔ 未改任何濾式之內容——`'配地階段' not in tp`／`_is_ghost_sliver`／
`by_blk` 之建法**一字未動**（新增之 `_proj_pop_filter` 係其**逐字複述**、供斷言比對，
⛔ 未取代原處）；⛔ 未統一 ghost 判準；⛔ 未動 `_projection_order` 本體／`_proj_of`；
⛔ 未合併四支引擎之 `def _proj_order`；🛑 ⛔ **未動碼面既有之七處序對拍一字**
（`oB != exp`／`oC != exp`／`oC != oD`／`got != exp`／`oB != oN`／`_oE != _oN`／`oE != oN`）。

🔒 **`data/` 零觸之證**：上方 `numstat` 之輸出**無 `data/` 之列**。

## §八　收工閘

| # | 項 | 結果 |
|---|---|---|
| `1` | `HEAD` 全 `40` 碼；**`app.py` blob 期末**；`numstat` 逐檔 | 基座 `77ebc492415726272a164bb6f5b9dfd96dec268a`；期末 **`8daca97f7b9f520cd1c8fdcfa4823a45f4199395`**；見檔頭 ✅ |
| `2` | 🛑 **push 前須請示**（⛔ 不繫於 `deletions` 之值） | 🛑 **請示中**·⛔ 未 push |
| `3` | `Z-1′`〜`Z-4′` 四項全數提出 | ✅ `§四` |
| `4` | `D-1`〜`D-5` 五組逐組報三事 | ✅ `§五`（`5／5`） |
| `5` | `§六` 十二項預測逐項對拍 | ✅ `§六`（符 `9`／不符 `3`） |
| `6` | 常規七：碼面逐字自基座 blob 重抽 | ✅ `§二`（九處逐位相符） |
| `7` | `VR-058 一`／`三`：命中數標框 ＋ 態 ＝ 本批基座 | ✅ `§一` |
| `8` | 常規八：`N/N` 型自證同格具名外部錨 | ✅ 見下 |
| `9` | 常規四（九）：形自證 ＋ MAX 推進 | ✅ `§一`（形自證命中 `1`；`194`→`195`） |
| `10` | `data/` 零觸；`docs/` 既有檔零改 | ✅ `§七` |
| `11` | 報告命名 ＝ `W-G.9-161R` | ✅ |

🔒 **常規八之施用**：本報告之 `N/N` 型自證為 `§五` 之「**`5／5`**」。外部錨三項——
① **與獨立來源對拍** ＝ `Z-2′` 之期初／期末 `run_all`（**二次獨立長跑·不同 clone**）逐閘 `diff rc=0`；
② **判別力對照** ＝ `D-1`〜`D-5` 每組皆含**正向對照**（未擾動須不紅）⇒ 證⛔ 非恆紅；
③ **界限檢查** ＝ `Z-3′` 之**未**正規化 `sha16` **相異**而正規化後**相同** ⇒ 證正規化⛔ 未把一切抹平。

---

## §九　🛑 交予發單側之三項

1. **`R-5`／`R-8` 不符**（`§六`）——其字面前提（「全綠」）於**基座即不成立**（准紅碼）。
   建議判準改為「**期初 ≡ 期末**」（本批已達成·`diff rc=0`）。⛔ CC 不自裁。
2. **`R-9` 不符**——`14` tag 中 `7` 個次數 `0`，成因二類（`main()` 內 `2` 個／trunk A 中止致 `wf_*` 主路徑 `5` 個）。
   🔒 **`S-D` 之裁經本批實證成立**：`wf_f4` 之二點確由 fixture subprocess 執行（`2`／`22` 次）。
3. **`deletions` ＝ `0`**——本批之生產碼變更**全為純附加**，與單首節之預期（`> 0`）相異；
   ⚠️ 惟 push 條件依單 `§零之零` **只此一處**（⛔ 不得逕行·須請示）⇒ **CC 未逕推**。

🩸 **CC 自捕之量測器紅**（`§一`）：對照組取無反引號之 `自誤 194` 得 `0` ⇒ 量測器紅、⛔ 未出艙；
併發現**自誤號二形並存** ⇒ 意指占用之搜尋須二形並取。
