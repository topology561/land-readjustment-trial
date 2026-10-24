# `W-G.9-394` 規格單　執行端之回報（**停機上呈**·停機款 `12`）

- 執行端（雲端·`effort=high`）·接單 `2026-10-24T05:34+08:00`（`ops/queue` `9bb33d1`）〜停機 `2026-10-24T08:4x+08:00`。
- 單：`orders/W-G.9-394_規格單.md`，bytes `128277`、`sha256` `d5f25291933534156a055e325d819947da3cd81db597ddc69997f506f0073539` ＝ `STATE.json`；`SELF_SHA256`（`P-5` 原口徑·受詞 `128199` B）實算 `0a8e4622d1c4333442e834b40dad2d562dfb4feb0027c9933043a1491e82eadb` ＝ 單載；pre-flight 🔴 `0`／🟡 `2`（`:221`、`:420`·＝ 單 `§五-1` 項 `9` 之具名豁免之二處）。
- `<O>` ＝ `/tmp/o394`（倉外）。

## 〇、停機之由（要）

工項二之唯讀獨立審查（驗 `V-1`〜`V-9` 皆合期之後、推前）報 **WARNING 二項·皆「涉域上判斷／規格之漏載」** ⇒ 停機款 `12`（⛔ 自裁）。執行端已自倉核其所指之碼之處（見 ⑥ 之末），其形確在：

1. **W-2（規格之歧義）**：`K-9-50` 題一 4 之「未得之一端……否則**連同其半併入已取得之一端**」之試算（`app.py`〔`bfb8fb9`〕`15333`：`if _noaff(state, _t2, {W['blk'], _lb}, {Lo['c']}):`）經 `_noaff`。`R-2` 依單改 `_noaff`（併入後之中止由新登記致 ⇒ 不過）⇒ 此處之 `GB-205` 之中止由「停機」變為「不過」（其後入 `W-G.9-357` 之 `K-9-48` 七項 4／3／5 與 `K-9-51` 之處置）。然單 `§三` 之用語云「🔒 段三 `K-9-50` 題一 4 之試算與末端塊之評選之試算（`trial_winner`）雖屬候選，其中止照舊停機（`§三-1` ⛔ 及·塊 `K41` 之二之庚）」，而塊 `K41` 之二之庚唯特指「未得之一端之原位次」之試算（`15312`〜`15317`·其中止照舊停機·⛔ 經 `_noaff`）。⇒ `15333` 之試算屬「題一 4 之試算」（⇒ 須照舊停機·則 `R-2` 之字面〔改 `_noaff` 之本體〕與之衝突）抑否（⇒ 照 `R-2` 判不過），單有二讀。審查者之合成例（`ex3_t14.py`）：改前停機；改後 `A1(1)` 以 `50` 部分併入 `F1(1)`、`D(1)` 未成、第 `5` 項轉調配。
2. **W-1（域上之判·規格未載）**：`GB-205` 之中止判為不過之後，餵入 `K-9-66` 之按比例之二分（`k966_block_merge`·`app.py` `14741`·「以二分法（視檢核為單調）求……通過之最大 `n`」；其呼叫：手冊先行 `16826`、第一趟 `17422`、段三後處理 `15579`）——同一（片 → 受併宗）以較小之比例再試而部分採用。塊 `K41` 之二之丙云「該候選不過」、【工】丑云「回到收受之前、該次之組合⛔ 再施」；以較小之比例再試是否屬「該次之組合」之再施，單未載。審查者之合成例：段三後處理之道路片 `K8(1)`／`K9(1)` 以 `10.5`、`24.5` 部分併入 `K1(1)`（其 `G` 止於觸發點之下）；手冊先行 `R1(1)` 以 `40` 部分併入 `X1(2)`。

**本案之影響**：本案二退縮⛔ 觸 `GB-205` 之形（`F38 run` 之 `R1`：`k965_part_split` 之 `None` `0`·登記之增 `0`·其 spy 涵蓋全程之試算）；`V-4`〜`V-6` ⇒ 本案之配地⛔ 變。上二項唯及他案（泛用化）之土地後果。

**請發單端裁處**：上二項之讀法（W-2：`15333` 之試算之中止為停機抑不過；W-1：`GB-205` 之不過是否入 `K-9-66` 之按比例再試）——其屬既裁之讀法者出補令，屬新域問者依 README 第二節請示 KL。

## 一、`commit` 與推送

| 工項 | `commit` | 推送 |
|---|---|---|
| 零 | `866f2d502bf7056935b38ca429a54639d8d1c5d7`（`docs/orders/W-G.9-394_規格單.md`·`1046`／`0`·blob 與來源 `cmp` 逐位同） | `git push origin HEAD:refs/heads/verify/W-G.9-394-k9615` ⇒ `* [new branch]`；推後 heads（濾後）`54`、主線 `5d2a283…` |
| 一 | `9e2517717d8b67587813760ef5ada6b3ef350a3e`（`4`／`2`、`5`／`0`、`3`／`1`、`475`／`0`·唯此 `4` 檔） | `866f2d5..9e25177`（快轉） |
| 二 | `bfb8fb90b429c81ecc0e7ee2a2216a66116dbd92`（`app.py` `+18`／`−4`·施後 blob `b39dfc4598f48d4fa829df2b92ed023707bcd285`·`1881442` B） | **⛔ 推**（停機款 `12`·唯在執行端之倉外施工樹·其全文差異見 ⑧） |
| 三、四 | ⛔ 為 | — |

- 新側支 `verify/W-G.9-394-k9615` ＝ `9e25177`（工項一之端）；已推之 `commit` ⛔ 撤（單 `§零-2` 末）。主線 `wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`（⛔ 動）。主 checkout 之同步由 KL 自行為之（README 第六節第 `6` 款）。
- heads：開工 濾後 `53`（未濾 `56`·其差 ＝ `refs/heads/wip/plots`、`refs/heads/verify/W-P.001-prelim`、`refs/heads/verify/W-P.001-tables`·單載未濾 `55`，出圖線之分支多一·濾後之母體 ＝ 期）；工項零之後 濾後 `54`。

## 二、開場（`§零-0`）

1. context 之餘量充足（約 `14.9` M tokens）；`nproc` ＝ `4`。
2. `origin/wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7` ✅；heads 濾後 `53` ✅（`<O>/heads_before_394.txt`）·⛔ 含新側支 ✅；`checkout --detach` 後 `status --porcelain --untracked-files=no` 空 ✅；追蹤檔 `2923`；`app.py` ＝ `d91f6ee8…` ✅。
3. `probe_WG9321_issuer_anchor.py /tmp/w <O>/anchor_before.txt 637 636` ⇒ `rc 0`·`stderr` `0` B；項4′：自誤 `622`／`637`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]` ✅。
4. bytes／`sha256`／`SELF_SHA256` ✅（見首）。
5. 環境：初驗 `rc 1`（`No module named 'shapely'`）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ 依單釘回六包、去 `tzdata`（皆 `rc 0`）⇒ 再驗 `rc 0` ✅。旗標 `[None, None, None, None, None]` ✅。
6. `Python 3.11.17`；`pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ＝ 基準；主線 ＝ 基準之 sha ⇒ **前置 (丙) `73` 呼叫沿用** `基準/5d2a2836617bc2aea57f0c7513e67d9b2313f7f7.md`（⛔ 重跑）。
7. 取號現查（`§零-1`）：`自誤 638`、塊 `Fy50`／`K41`／`P52`／`E40`／`G18`、`W-G.9-394R`、`W-G.9-394-k9615`、`W-G.9-394_規格單`、`probe_WG9394` 皆 `0`／`0`；對照甲 `Fy49` `2`、`K40` `3`、`P51` `1`、`E39` `1`、`G17` `1` 檔 ✅。
8. 塊之實得（抽取式 ＝ 單 `§五-1` 末）：`Fy50` `29876` B·`1533282c…`·`548` 列；`K41` `13280` B·`2440cfd5…`·`62` 列；`P52` `3164` B·`f7103308…`·`18` 列；`E40` `1381` B·`ce34b2b8…`·`12` 列；`G18` `1436` B·`817a345b…`·`9` 列（皆 ＝ `§五-1` 項 `2`／`4`）。`CK` `1539` B·`00cd3949…`·`31` 列；`GF` `2445` B·`b11edb77…`·`47` 列（＝ 項 `7`）。工項一之 `4` 器之施前 blob ＝ 項 `2`、施後 ＝ 項 `5`；`git apply --check` 過。工項三之四檔（倉外預算·以塊附於末）：`962803`／`5c5eafdc…`、`36799`／`d2e96792…`、`1234811`／`11127efb…`、`1068693`／`2d1a44b0…`（皆 ＝ 項 `5`·⛔ 寫入倉）。

## 三、前置（工項一之端 `9e25177`·倉外 worktree `/tmp/wt1`·並行 `2`）

- (甲) `8` 呼叫、(乙) `6` 呼叫 ⇒ `14`／`14` 合期（`#85`、`#86` `rc 1` 如期之紅）·`stderr` `0` B·耗時之和 `2170` s；`f8_pre_35.json`／`f8_pre_00.json` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`／`884e91714a79288406faa4def6518847de36de39`。
- (丙) 沿用基準（二之 6）。
- 前置 `4`：「W-G.9-394」⇒ 無出艙·`rc 1`；「K-9-61 ⑤」⇒ `app.py:5`·`rc 0` ✅。

## 四、驗（工項二之 `commit` `bfb8fb9`·倉外 worktree `/tmp/wt2`·殼無 `WV_`·從頭整套·並行 `2`·⛔ 沿用）

| # | 實 | 判 |
|---|---|---|
| `V-1` | `8` 呼叫皆 `rc 0`·末列 ＝ 施後之列；`F38 selftest` ✅ `18`／`18`（`T1`〜`T11`）、`wiring` ✅ `8`（`W1`〜`W8`）、`run` ✅ `R1@3.5`、`R2@3.5`（受併宗 `25`）、`R1@0.0`、`R2@0.0`（受併宗 `26`） | ✅ |
| `V-2` | 其餘皆 `rc 0`·末列 ＝ 施後之列；`F23 selftest` `✅ P0 逐項擾動恰該項紅 75／75` | ✅ |
| `V-3` | `4` 器之 blob ＝ `§五-1` 項 `5` | ✅ |
| `V-4` | `F36 diff` 3.5 m／0 m 皆 `rc 0`·全文唯一列 `全比相異 0 項`；`cmp` 皆 `rc 0`·`相異 0 項 ⇒ ✅ 同`；對照 `k6s3_pre_35` 對 `k6s3_pre_00` ⇒ `全比相異 44 項` | ✅ |
| `V-5` | `parity` 二退縮皆 `⇒ rc 0（不符 0 項）`；落檔與 `stdout` 各以 `<HEAD>` 代二態之 `HEAD`（各 `1` 處）後逐位同（四對皆 `True`）；⛔ 代 ⇒ 皆異 | ✅ |
| `V-6` | `#58`／`#59` `⇒ 紅 []；rc 0`；`hash-object`：3.5 m 二列 `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、0 m 二列 `884e91714a79288406faa4def6518847de36de39` | ✅ |
| `V-7` | 生產碼 `34` 檔對 `9e25177` 相異唯 `app.py`（`18`／`4`）；`verify/` 相異 `0`；頂層之名⛔ 增減、相異之節點 ＝ `{end_block_merge_run, k6_trial_raise_since, k6b_stage3_run, k953_manual_run}`（`F38 W1`·審查者之 AST 亦同） | ✅ |
| `V-8` | 「W-G.9-394」`6`；「K-9-61 ⑤」`7`（＞ 前置之 `5`） | ✅ |
| `V-9` | `stderr` 合計 `0` B | ✅ |

全跑：`87` 呼叫·耗時之和 `16781` s·壁鐘 `22:03`〜`00:23`（UTC）；⛔ 有逾時、重跑。

## 五、停機款 `1`〜`13` 之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `5d2a283`、heads 濾後 `53`·⛔ 含新側支、追蹤檔無變、四簿 ＝ 期、旗標 ＝ 期、環境可匯入 | 皆合（⛔ 成就） |
| `2` | `SELF_SHA256`、bytes／`sha256` 合；入倉之 blob 與來源逐位同 | 皆合（⛔ 成就） |
| `3` | 五塊 ＝ `§五-1`；`git apply --check` 過；blob ＝ 項 `5` | 皆合（⛔ 成就） |
| `4` | 前置之期皆合 | `14`／`14`＋前置 `4` 皆合（⛔ 成就） |
| `5` | 撰碼中無域上之歧義、⛔ 須改禁改 | 撰碼中未見（⛔ 成就）；然見款 `12` |
| `6` | `V-1`〜`V-9` 皆 ＝ 期、本案配地⛔ 變 | 皆合（⛔ 成就） |
| `7` | 推送之目標唯新側支／`ops/queue`、⛔ 被拒、⛔ `--force`、主線⛔ 動 | 合（`ops/queue` 之一次非快轉被拒 ⇒ `pull --rebase` 後推·單之款係就新側支與主線言·照實記之） |
| `8` | 工項三之四檔 | ⛔ 至（倉外預算之 blob 皆 ＝ 項 `5`） |
| `9` | 收工閘 | ⛔ 至 |
| `10` | ⛔ 作正典之判、⛔ 改塊器命令 | 合（⛔ 成就） |
| `11` | 新檔⛔ 為 `check-ignore` 所命中 | 本單之入倉之檔、`probe_WG9394_k9615.py` 皆 `rc 1`（⛔ 成就） |
| `12` | 審查之發現⛔ 涉域上判斷或規格之漏載 | **成就**：WARNING `W-1`、`W-2`（〇） |
| `13` | 存取⛔ 被拒 | 合（⛔ 成就） |

## 六、唯讀獨立審查（一輪·`redistribution-reviewer`·⛔ 改檔）之回報（要錄·其腳本與出艙在執行端之暫存 `/tmp/rv394/`·不入倉）

- **結論**：BLOCKED 無；`R-1`〜`R-6` 皆落地、字樣合；`R-4` 守；`§三-3` 六款逐款查過皆合（頂層節點 `417`／`417`·名⛔ 增減·相異恰四；新增之列無「四空白 ＋ 中文」起首者；基準中恰一之函式名仍恰一；八處之殼之既有句⛔ 動；`verify/` 零改；`main` ⛔ 動；子字串之錨唯 `'(?![0-9])'` 由 `1` 變 `2`，其於 `F23`／`F24` 之基準 `0` 見 ⇒ ⛔ 為錨）。審查者自跑 `#85`、`#86`、`#69`、`#70`、`#72`、`#73`、`#82`、`#5`、`#6`、`#14`、`#15` 皆 `rc 0`。
- **呼叫端之窮查**：入池閘·併入後之試算（`10418`·其內之 `trial` ⛔ 再入入池閘 ⇒ `GB-205` ⛔ 達·行為⛔ 變·`§三` 之用語之二清單皆未列·NOTE-A）；末端塊合併再試（`11926`／`11927`·現態 ⇒ 停機）；段三／手冊先行／第一趟之畫面與 harness 之殼（`23319`／`748`、`23504`／`871`、`23605`／`938`·兩用 ⇒ 回 `err`、由消費端判）；`R-6`（`16503`·停機）。
- **`err` 之讀處之窮查**：判停機者（採用）：段三 `15090`、`15314`、`15630`、`15778`、`15834`；手冊先行 `16285`、`16294`、`16426`、`16725`、`16748`、`16883`；第一趟 `17199`、`17248`、`17285`、`17372`；畫面 `23617`；harness `949`；`R-5` 之取代 ⇒ `R-6` 停機。判不過者（候選）：`16297`（`_chk953` 之 `_sa`）、`16404`（`_B4`·與 `_sa` 同一 memo 之物）、`17252`（`_chk_a4` 之 `_sa`）、`15088`（`R-2`）。`trial_winner`：段三者唯跑街角選位（⛔ 經入池閘）；末端塊之 `_trial`（`11992`）經 `alloc_eval`、無殼 ⇒ `GB-205` 直接上拋停機（照舊）。「採用之配地之試算之中止由 `GB-205` 致而今被靜默判為不過／續辦」之處：**無**。
- **`R-2` 之 mark 之位與判式**：合。NOTE-C（記而⛔ 改）：判式為「其間有任何新登記」（⛔ 特判 `GB-205`）·依「每一 `alloc_state` 皆有殼」之不變式（`F33 X2` 守之）；無殼之 `alloc_state` 吞 `GB-104` 之合成例（`ex2b.py`）：改前停機、改後判不過——單之 `R-2` 之字面與塊 `K41` 之二之庚已載之。
- **獨立之合成之例**（⛔ 照抄 `F38`·替身之 `alloc_state` 於殼內呼叫真之 `k929_6_fixpoint`〔`F29` 之 `ToyLate`·換名、換數〕，由真之入池閘 `10425` 立 `GB-205`；其與真實之差：`GB-205` 生於另一玩具街廓、非該候選之受併宗本身，`kept`／`G` 由玩具給）：
  - 例一 手冊先行（`ex1_k953.py`·`F27` 之 `_wk` 之世界·受併宗 `X1(2)` 受併即觸）：改前停機（「試算內之程式之停機…GB-205」）；改後該批不過（`X1(1)`、`R1(1)`、`P1(1)` 併入 `X1(2)` 皆未成；改併 `C1(1)` 成；`K-9-51` 成）；不觸者二樹逐列同。
  - 例二 段三後處理之道路片（`ex2_s3post.py`·`K1(1)` 以 ① 取得〔＋`K2(1)`〕後擬併同一地主之道路片 `K9(1)`／`K8(1)`·觸發 ＝ `K1` 之 `G` ＞ `180`）：改前停機；改後後處理 (b) 二片皆未成（不過）、第 `5` 項轉調配、`K1` 之 `G` `180`；不觸者二樹同。
  - 補例四 `R-6`（`ex4_r6.py`）：取代之試算以 `GB-205` 中止 ⇒ 改前、改後皆停機（後者之訊息含「R-5 之取代之試算·W-G.9-394」）；去 `R-6` 之列之突變 ⇒ 記「未取代」而續辦（判別力）；`C0` 即中止 ⇒ 二樹皆停機。`F38` 對 `R-6` 唯靜態之 `W8`（記而⛔ 改）。
- **WARNING**（涉域上判斷／規格之漏載）：**W-1**、**W-2**（見〇）。
- **他之 NOTE**（⛔ 擋）：守恆與本案配地審查者未實跑（靜態之論：無 `GB-205` 之新登記者四處皆 no-op；執行端之 `V-4`〜`V-6` 實量之）；NOTE-B：採用之配地中 `GB-205` 之停機之訊息之形變（如「現態之配地中止（無從判定）：'…GB-205…'」·`err` 取前 `300` 字、`GB-205` 之訊約 `140` 字 ⇒ 號仍在）；`k6_trial_raise_since` 之 docstring 首列與 `end_block_merge_run` 之 docstring ① 未更（`R-1`〜`R-6` 以外之字⛔ 動）；`R-6` 之 `where` 含 `_hdr953` ⇒ 訊息之括號巢狀（外觀）；候選之試算之 `GB-205` 之登記留於 `K6_PROGRAM_STOPS`（例一增 `15` 筆·唯 mark 之窗內用之·無以其總長判事之處）。審查者於 `/tmp/w` 跑 `py_compile` 一次 ⇒ 改寫 `__pycache__/app.cpython-311.pyc`（gitignore 內·二樹 `status --porcelain` 皆空）。
- **執行端之自核**（⛔ 判正典）：W-2 之 `15333` 確為 `K-9-50` 題一 4 之 `else` 支（`_noaff(state, _t2, {W['blk'], _lb}, {Lo['c']})`·其前之「未得之一端之原位次」之試算 `15312`〜`15317` 照舊停機·⛔ 經 `_noaff`）；W-1 之 `k966_block_merge`（`14741`·docstring「以二分法（視檢核為單調）」）之呼叫 `15579`、`16826`、`17422`（另入池閘 `10456`）確在。

## 七、設計說明（`§三-5`）

- **`R-1`**（`k6_trial_raise_since`·`9805`〜`9813`）：簽名 `(mark, where, *, adopted=False)`；`for _s394 in K6_PROGRAM_STOPS[int(mark):]`：`adopted` 或 ⛔ 合 `(?<![0-9A-Za-z\-])GB-205(?![0-9])` ⇒ `raise RuntimeError(f"🔴 [試算內之程式之停機·{where}] {_s394}")`；否則 `return None`。docstring 首列照舊、增二列（`W-G.9-394`、`K-9-61` ⑤、`adopted` 之義）。式於函式內書之（⛔ 新頂層之名）。
- **`R-2`**（`_noaff`·`15082`〜`15094`）：`_sb` 之後取 `_m394 = k6_trial_mark()`；`_sa` 之後 `_eb394, _ea394 = _sb.get("err"), _sa.get("err")`；`if (not _eb394) and _ea394 and len(K6_PROGRAM_STOPS) > _m394: return False`；其後之「無從判定」之停機與 `_lost`／`bad_pools` 照舊（⛔ 照抄既有之句·以新名書之）。
- **`R-3`**（`end_block_merge_run`·`11927`）：既有之 `k6_trial_raise_since(_m389, '末端塊合併再試·試算')` 之次增 `k6_trial_raise_since(_m389, '末端塊合併再試·現態之試算·W-G.9-394', adopted=True)`（行末之註同列·含 `k6_trial_`）。
- **`R-4`**：`k929_6_fixpoint` ⛔ 動。
- **`R-5`**：`W-G.9-389` 之註之段之末增一列（`9781`）。新區域名 `_s394`、`_m394`、`_eb394`、`_ea394`、`_mk394`（改前全檔 `0` 見）。
- **`R-6`**（`k953_manual_run`·`16501`〜`16503`）：`_ok953 = _same953(_sim953(_cand_st))` 之前 `_mk394 = k6_trial_mark()`、之後 `k6_trial_raise_since(_mk394, f"{_hdr953} R-5 之取代之試算·W-G.9-394", adopted=True)`（行末之註同列）。
- **`k6_trial_raise_since` 之一切呼叫處**（施後）：`app.py` `10418` 入池閘·併入後（其 `trial` ⛔ 再入入池閘 ⇒ `GB-205` ⛔ 達）；`11926` 末端塊合併再試（現態·`adopted` 偽）、`11927`（同·`adopted=True`）；`16503` 手冊先行 R-5 之取代（`adopted=True`）；`23319` 段三·畫面、`23504` 手冊先行·畫面、`23605` 第一趟·畫面（殼·兩用：併入前／現態之消費端判停機、併入後之消費端判不過）；`verify/selection_pipeline.py` `748`、`871`、`938`（harness 之殼·同·⛔ 動）。
- **`err` 之讀處**：見 ⑥ 之窮查（執行端自 `grep -n "get(['\"]err['\"])\|\[['\"]err['\"]\]" app.py` 得 `41` 列〔施後·含同一判之多列〕·與審查者之表合）。
- **`§三-3` 之自查**：撰碼中自跑 `#4`、`#5`、`#6`、`#63`、`#66`、`#69`、`#70`、`#72`、`#73`、`#81`、`#82`、`#85`、`#86`（施工樹·`13`／`13` ＝ 施後之期）；docstring 之初稿有「四空白 ＋ 中文」起首之折行二列 ⇒ 撰碼中即改。

## 八、`app.py` 之全文差異（`git diff 9e25177 bfb8fb9 -- app.py`）

```text
diff --git a/app.py b/app.py
index d91f6ee..b39dfc4 100644
--- a/app.py
+++ b/app.py
@@ -9778,6 +9778,7 @@ K917_DROPPED = {}
 #   🔒 帶號之停機一律經 `k6_program_stop` 立之（登記其全文）；吞試算之中止之處，試算之前取 `k6_trial_mark()`，
 #   其後 `k6_trial_raise_since(…)` 見有新登記者即上拋其首者之全文——⛔ 判為「不過」「未成」「試算中止」而續辦。
 #   🛑 他之試算中止（無號·配地上不可）照舊為「不過」（`K-9-53` ① 之工程讀法之庚）。
+#   🔧 `W-G.9-394`（`K-9-61` ⑤·`K-9-48` 其三·`K-6` 典 `W-G.9-394` 之節之二）：`GB-205`（受併宗含非其成員之受併之土地而須依手冊部分併出）之新登記，於試算之殼（`adopted` 為偽）⛔ 上拋——候選之試算之中止由呼叫端判為不過（回到收受之前）；採用之配地之試算之後（`adopted=True`）照舊上拋。
 
 #: 🔒 程式之停機之登記（全文·⛔ 截）；⛔ 清、⛔ 刪其項——巢狀之試算以長度分之。
 K6_PROGRAM_STOPS = []
@@ -9801,10 +9802,14 @@ def k6_trial_mark():
     return len(K6_PROGRAM_STOPS)
 
 
-def k6_trial_raise_since(mark, where):
-    """🆕 `W-G.9-389`：登記之長度 ＞ `mark` ⇒ 上拋其首一新登記者之全文（⛔ 截）；否則回 `None`。"""
-    if len(K6_PROGRAM_STOPS) > int(mark):
-        raise RuntimeError(f"🔴 [試算內之程式之停機·{where}] {K6_PROGRAM_STOPS[int(mark)]}")
+def k6_trial_raise_since(mark, where, *, adopted=False):
+    """🆕 `W-G.9-389`：登記之長度 ＞ `mark` ⇒ 上拋其首一新登記者之全文（⛔ 截）；否則回 `None`。
+    🔧 `W-G.9-394`（`K-9-61` ⑤·`K-9-48` 其三）：新登記依其序逐一——
+    `adopted` 為偽（試算之殼·候選之試算之中止由呼叫端判為不過）⇒ 上拋其首一非帶 `GB-205` 之號者（帶之者⛔ 上拋）；
+    `adopted` 為真（採用之配地之試算之後）⇒ 上拋其首一者。所免之號唯 `GB-205`。"""
+    for _s394 in K6_PROGRAM_STOPS[int(mark):]:
+        if adopted or not re.search(r"(?<![0-9A-Za-z\-])GB-205(?![0-9])", _s394):
+            raise RuntimeError(f"🔴 [試算內之程式之停機·{where}] {_s394}")
     return None
 
 
@@ -11919,6 +11924,7 @@ def end_block_merge_run(temp_parcels, build_parcels, own_map, locked, corner_lot
     except RuntimeError as _e:
         _rec['標的'] = None
         k6_trial_raise_since(_m389, '末端塊合併再試·試算')
+        k6_trial_raise_since(_m389, '末端塊合併再試·現態之試算·W-G.9-394', adopted=True)   # 🔧 K-9-61 ⑤：現態 ⇒ 停機（⛔ 記試算中止）
         _rec['試算中止'] = str(_e).split("\n")[0][:300]
         return temp_parcels, build_parcels, [], _rec
     _tg = []
@@ -15074,7 +15080,13 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
 
     def _noaff(before, after, blks, removed):
         _sb = alloc_state(before["temp"], before["build"])
+        # 🔧 `W-G.9-394`（`K-9-61` ⑤·`K-9-48` 其三）：併入前無中止、併入後之試算之中止由其間之新登記（`GB-205`·受併宗須依
+        #   手冊部分併出）致 ⇒ 該候選不過（回到收受之前）；其餘之中止照舊停機（「無從判定」）
+        _m394 = k6_trial_mark()
         _sa = alloc_state(after["temp"], after["build"])
+        _eb394, _ea394 = _sb.get("err"), _sa.get("err")
+        if (not _eb394) and _ea394 and len(K6_PROGRAM_STOPS) > _m394:
+            return False
         if _sb.get("err") or _sa.get("err"):
             raise RuntimeError(
                 f"🔴 [K-6-B 段三] 「不影響原位次」無從判定（配地中止）：併入前 {_sb.get('err')!r}｜"
@@ -16486,7 +16498,9 @@ def k953_manual_run(temp_parcels, build_parcels, own_map, blocks, centerlines, a
         _nb953 = [str(_bq953['暫編地號']) for _bq953 in state["build"]
                   if str(_bq953['暫編地號']) not in _oth953]
         _cand_st = _mk953(_nt953, _nb953)
+        _mk394 = k6_trial_mark()   # 🔧 `W-G.9-394`（K-9-61 ⑤）：取代之試算屬採用之配地之查（非候選）
         _ok953 = _same953(_sim953(_cand_st))
+        k6_trial_raise_since(_mk394, f"{_hdr953} R-5 之取代之試算·W-G.9-394", adopted=True)   # GB-205 ⇒ 停機（⛔ 記未取代）
         _put_row953(序='單元', 歸戶=_gown953(state["by"][_h953]), 街廓=_home953[_h953], 片=_h953,
                     結果=('取代' if _ok953 else '未取代（取代後之配地相異）'))
         if _ok953:
```

## 九、`87` 呼叫之二態之表（`rc`／`stderr` B／末列·耗時 s）

| # | 命令 | 工項一之端（前置） | 施後（工項二 `bfb8fb9`） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（146） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（416） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（30） | `0`／`0`／`⇒ 紅 []；rc 0`（29） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（31） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（40） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（273） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（80） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（537） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（738） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（73） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（456） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2187） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（23） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（24） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（290） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（391） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（40） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（37） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（24） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（17） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（12） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（211） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（59） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（957） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（177） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（119） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（397） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`紅項 [] 器紅 0`（11） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（398） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（238） | `0`／`0`／`（JSON 之摘要列·略）`（226） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（166） | `0`／`0`／`（JSON 之摘要列·略）`（166） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（236） | `0`／`0`／`⇒ 紅 []；rc 0`（226） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（168） | `0`／`0`／`⇒ 紅 []；rc 0`（166） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（517） | `0`／`0`／`⇒ rc 0（不符 0 項）`（492） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（367） | `0`／`0`／`⇒ rc 0（不符 0 項）`（346） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（395） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1552） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1427） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（151） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（518） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（392） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（39） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（774） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（393） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（390） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | 沿用 `基準/5d2a2836…md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（387） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['T1', 'T1b', 'T1c', 'T2', 'T8', 'T9', 'T9d', 'T9e', 'T10', 'T11']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W8']；rc 1`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（402） | `0`／`0`／`⇒ 紅 []；rc 0`（389） |

前置之實跑 14 呼叫·耗時之和 2170 s·stderr 之和 0 B；施後 87 呼叫·耗時之和 16781 s·stderr 之和 0 B

## 十、自捕與自解

1. 接單之段（讀單之前）以 heredoc 為之二次（`STATE.json` 之更、`SELF_SHA256` 之自驗·皆⛔ 涉主倉）——單首 🔑 令⛔ heredoc；其後一律以檔為之。
2. 接單之推送一次非快轉被拒（發單端之門鈴之記先推）⇒ `pull --rebase`（`log.md` 之末列之衝突·二列皆存）後推成（README 第五節之鎖）。
3. `R-5` 之註初分二列 ⇒ 依單「增一列」回為一列。
4. README 第六節與單之衝突：無（唯路徑 ＝ Linux 絕對路徑、`python3`）。

## 十一、耗時（UTC）

接單 `21:34` → 開場、工項零、一 `21:41` → 前置 `14` 呼叫 `21:42`〜`22:00`（之和 `2170` s·並行 `2`）＋撰碼 → 工項二之 `commit` `22:03` → 驗 `87` 呼叫 `22:03`〜`00:23`（之和 `16781` s·並行 `2`）→ 審查 約 `14` 分 → 停機上呈。
