# `W-G.9-390` 補令三　執行端回報（**完成**）

- 受單：`orders/W-G.9-390_補令三.md`（`144572` B·`sha256` `9b74273c61b4597351f29dff5243712400274a75ed36881b6df62b529e7304cf`·與 `STATE.json` 合；`SELF_SHA256` 依 `P-5` 原口徑自驗 ＝ `81832dc7d2e6736898ca9da2dcce32766e11e9edf086737c6ace0ccb96b4ca26`·合）。
- 結果：**完成**（停機款 `1⁗`〜`13⁗` 皆⛔ 成就）。五筆皆推新側支 `verify/W-G.9-390-k961r`（快轉）：`6d1e994` → `e456b93`（工項零⁗）→ `3cf4685`（工項一⁗）→ `a41022d`（工項二⁗·🔴 生產碼）→ `5bbe795`（工項三⁗）→ **`ca3ea9eb674ae5c411a4969f68398baf74be9745`**（工項四⁗）。主線 `wip/s1-endpart` ＝ `2aa63021da38632704519e05d53ced9f56e22659`（⛔ 動）；heads `50`。主 checkout 之同步由 KL 自行為之。
- **本案之配地⛔ 變**：`k6s3 cmp` 二退縮相異 `0`（對照組 `18`）；`F8` 之落檔前後逐位同（`8be0160b…`／`6fb86647…`）；`parity` 二退縮以同一字樣代 `HEAD` 後逐位同（⛔ 代者相異）。`F34 run`：`3.5 m` 之段三之成者 `3` 皆保留 ⇒ ⛔ 停機；`0 m` 之段三之成者 `0`。
- `app.py`：`80d00d86155eddb843b3e3e2efa8e2e47c0db142` → `82855efb31049c2d21146c2c6fc903182615f912`（`1856077` B·`+57`／`−15`·唯 `k6b_stage3_run`）：`R-1⁗`（取得即鎖定之宗之查·未保留或試算中止 ⇒ 停機·⛔ 還原）、`R-4⁗`（`W-G.9-388` `R-5` 去之）、`R-9‴`（題一 3 之序·`_rk390` 經頂層 `k967_rank`／`k967_pre_area`）、`R-5⁗`（docstring）。
- 倉內之執行報告：`docs/reports/W-G.9-390R_取得街角之宗之回原狀_執行報告.md`（`ca3ea9e`·①〜⑩、停機款四單之三值、`74` 呼叫之表、差異之全文）＋ `W-G.9-390R_取得街角之宗之回原狀_差異.diff`。
- `effort=high`；`<O>` ＝ `/tmp/O`；施工樹 ＝ `/tmp/w`；撰碼用之拋棄式 worktree ＝ `/tmp/dev`（⛔ 推）；審查者之腳本 ＝ `/tmp/rv/`（倉外）。

## 一、時程（Asia/Taipei·`2026-10-21`）

接單 `01:16:35`（`3e86505`）→ 開場畢、工項零⁗ `e456b93`／一⁗ `3cf4685` 推 `01:20:51` → 前置⁗ (甲)(乙) `20` 呼叫 `01:21:23`〜`02:31:37`（並行 `2`）→ 工項二⁗ `commit` `02:33:37`（⛔ 即推）→ 施後 `74` 呼叫 `02:34:05`〜`05:23:52`（並行 `2`·其耗時之和 `20375` s·本機較發單端約慢 `1.6` 倍）→ `V-3⁗`〜`V-8⁗` `05:25` → 唯讀獨立審查 `05:25`〜`05:38` → 工項二⁗ 推 `05:38` → 工項三⁗ `5bbe795` 推 `05:38` → 工項四⁗ `ca3ea9e` 推 → 收工閘 → 本回報。進度列五（`log.md`）。

## 二、`§零⁗` 之實值

1. context 充足；`nproc` ＝ `4`。
2. `origin/wip/s1-endpart` ＝ `2aa63021…`；`origin/verify/W-G.9-390-k961r` ＝ `6d1e9948…`；heads `50`（`<O>/heads_before_390p3.txt`）；`checkout --detach` 後 `status` 空；`app.py` ＝ `80d00d86…`；旗標 `[None, None, None, None, None]`。
3. `issuer_anchor … 629 623` ⇒ `rc 0`；正典框：自誤 `614`／`629`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（皆合）。
4. bytes／`sha256`／`SELF_SHA256` 皆合。
5. 初 `import shapely…` ⇒ `ModuleNotFoundError`；`python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）後 `rc 0`。
6. `Python 3.11.17`；裝後 `pip freeze` ＝ `80716bfb…`（`certifi`、`pillow`、`websockets` 三列異）⇒ 依 🔎 釘之（`rc 0`）⇒ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（`1114` B·`64` 列）＝ 基準 ⇒ 前置⁗ (丙) 沿用。
7. pre-flight：🔴 `0`／🟡 `3`（`P-4` `:119`、`:163`、`:198`·＝ `§五⁗` 項 `9` 之具名豁免）／ℹ️ `2`。
8. `§零-1⁗`：`K-9-80`、`自誤 634`、塊名四、新區域名 `15` 於 `6d1e994`（追蹤檔 `2902`）皆 `0` 見；對照 `` 塊 `Fy44` ``、`` 塊 `E35` `` 各 `1` 檔。`ops/queue` 之 `*.md`（本補令除外）之 `K-9-80` 有命中：`log.md`、`交接.md`、`進度表.md`——皆發單端出單之時與其後（`ae58e6b`、`b5cff50`）之同一用之記（⛔ 他用）⇒ 照實記之、⛔ 停（宣告框·⛔ 停機款）。
9. 諸塊：`Fy45` `55496`／`453da9f4…`／`597`；`K36` `14660`／`94be75cd…`／`76`；`E36` `2491`／`57bd12a3…`／`13`；`P47` `3107`／`76e91a75…`／`20`；倉內之 `K33`、`P44`、`K34`、`E34`、`P45`、`K35`、`E35`、`P46`、`CK`、`GF` 皆 ＝ `§五⁗` 項 `4`／原單 `§五-1` 項 `7`。

## 三、前置⁗ 與驗

- 前置⁗ (甲)(乙)：`20` 呼叫皆合期（`stderr` `0` B）；(丙) ⇒ `54` 呼叫沿用 `基準/2aa63021da38632704519e05d53ced9f56e22659.md`。項 `4`／`5` 逐字合（倉內報告 ③-甲）。
- `V-1⁗`／`V-2⁗`：施後 `74` 呼叫一律從頭照跑，皆 `rc 0`、末列 ＝ `§五⁗` 項 `8` 之施後之列、`stderr` 合計 `0` B；`F34 selftest` `L1`〜`L14` ✅·`P0 14／14`；`F34 wiring` `X1`〜`X4` ✅；`F34 run` `R1@3.5`、`R1@0.0`、`R0` ✅；`F32 selftest` `K13` ✅；`F13 selftest` 全例與 `M0`〜`M16` ✅；`F23 selftest` `P0 75／75`。
- `V-3⁗`：二器 ＝ `eb3ad6af…`／`8cc7d3a0…`；他器 ＝ `6d1e994` 之值；`verify/` 對工項一⁗ 之端相異 `0`。
- `V-4⁗`：`cmp` 二退縮 `rc 0`·`相異 0 項 ⇒ ✅ 同`。`V-5⁗`：`parity` 二退縮 `rc 0`；代 `HEAD`（`3cf4685…`／`a41022d…`）後落檔與 `stdout` 皆逐位同；⛔ 代 ⇒ 相異。`V-6⁗`：`8be0160bc14dd92a5331f86eecc995cae0507376`（二）、`6fb86647807f9744594071be25c522b6b506c230`（二）。
- `V-7⁗`：生產碼 `34` 檔唯 `app.py` 異（`57`／`15`）；頂層之名之集同；相異之節點 `['k6b_stage3_run']`；題二之二行各 `1`。`V-8⁗`：「取得即鎖定之宗之查」`app.py:6`、「於試算⛔ 保留」`app.py:1`、「於現態未保留」「還原後仍出現」各 `rc 1`。`V-9⁗`：`0` B。

## 四、唯讀獨立審查（另派·唯讀·倉外 `/tmp/rv/`）

- (A) 改配地或違規格、違裁示：**無**。(D) 涉域上判斷或規格之漏載之新形：**無**（所遇皆 `§三-4⁗` ①②④）⇒ 停機款 `12⁗` ⛔ 成就。
- 合成之例（`F34`、`F32` 之外·自手算）：例一 a（① 取得之宗未保留·該群無待後處理之土地）改前靜默、改後停機（＝ 手算）；例一 a′（試算中止）改後停機；例一 b（三成者其二未保留、非成者亦未保留）訊息唯具未保留之二成者；例二（皆保留·同一地主之道路片併入取得之宗·`P1` `194`）改前改後逐位同 ＝ 手算（另 b、c 二變形亦同）；例三（`R-9‴`）改後依題一 3 之序 ＝ 手算；例零（無成者）試算 `0`。
- (B) 純實作之瑕：無能改配地者（記：`_ct_pick` 首註解之改述；步驟 10 之 `err` 之判不可達而留之）⇒ ⛔ 改、⛔ 重驗。
- (C) 記而⛔ 改：有成者而無待後處理之群者多呼一次試算（規格所要·`L8`）；保留之查以紀錄之「街廓」取之（舊 `R-5` 以 `_blk_of`·本案同）；補令二之 C-1〜C-3（`§三-4⁗` ⑦·留次單）；三舊器 Python `3.11.17` 不能解析而未入審查者自寫之錨掃描（`F23 W8`／`F24 W7` 涵蓋全集·皆綠）。
- 全文要旨見倉內報告 ⑥。

## 五、收工閘（於 `ca3ea9e` 量）

| 閘 | 實 |
|---|---|
| `1⁗` | 十一筆 `2aa6302..HEAD` 之 `numstat`：`7c171db` `1160`／`0`；`591b9c3` 五器（`4`/`2`、`5`/`3`、`10`/`5`、`4`/`1`、`561`/`0`）；`640a652` `642`／`0`；`ddddfb8` `149`／`5`；`320f967` `725`／`0`；`6d1e994` `38`/`5`、`81`/`19`（⛔ 變）；`e456b93` `1070`／`0`；`3cf4685` `5`/`3`、`105`/`372`；`a41022d` `app.py` `57`／`15`；`5bbe795` 自誤簿 `57`／`0`、`K-6` 典 `239`／`0`、`docs/待落地清單.md` `69`／`0`；`ca3ea9e` 報告 `400`／`0`、差異 `120`／`0`。五筆之首列 ＝ 所令逐字 ✅ |
| `2⁗` | 生產碼相異恰 `['app.py']`；`verify/` 相異恰 `5`（`M` `4`·`A` `1`）；新檔三之 `git check-ignore -v --no-index` 皆 `rc 1`；對照 `verify/__pycache__/x.pyc` ⇒ `rc 0`·`.gitignore:18:__pycache__/` ✅ |
| `3⁗` | `15` 檔之 blob 之 `CR` 合計 `0`；判別力 `data/V6.dxf` ＝ `12308` ✅ |
| `4⁗` | `K-6` 典 `868268` → `909964`、自誤簿 `1215603` → `1225486`、待落地清單 `10814` → `20188`；改前皆為改後之嚴格前綴；其尾之 `sha256` ＝ 諸塊之接（`K33`〜`K36`、`E34`〜`E36`、`P44`〜`P47`）；`CLAUDE.md`、`GB` 簿、`VR` 簿（依 `issuer_anchor` 器所讀之檔·`docs/reports/W-G.4_泛用阻塞項登記表.md`、`docs/驗證裁定登記表.md`）、`.claude/`、`verify/selection_pipeline.py` 對 `2aa6302` 相異 `0` ✅ |
| `5⁗` | heads `50`；主線 ＝ `2aa63021…`；`verify/W-G.9-390-k961r` ＝ `ca3ea9e…`（其祖含 `6d1e994`）；其餘 `48` 列（`ops/queue` 與本側支除外）逐列 ＝ `<O>/heads_before_390p3.txt` ✅（全列見附錄） |
| `6⁗` | `closegate 634 629 .` ⇒ `rc 0`·`✅ 二閘皆過`；判別力 `635 634 .` ⇒ `rc 7` ✅ |
| `7⁗` | `issuer_anchor … 634 629` ⇒ `rc 0`；正典框：自誤 `619`／`634`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`；`VR` `80`／`95`；**`K-9` `77`／`80`**／`[44, 47]` ✅ |
| `8⁗` | `checkidx` ⇒ `rc 0`·`索引列數 124；內部字樣 122；外部指標 9；不合 0`；`gen_fa_index` ⇒ `則 124；加註節 14；列 158`·與 `SKILL.md` 逐位同 ✅ |

## 六、設計說明（`§三-5⁗`·要旨·全文見倉內報告 ⑦）

- `R-1⁗`：步驟 `1`〜`8` 之環（本體⛔ 動）之後、步驟 10 之前；成者 ＝ 紀錄中 `序` ≠ 後處理、`結果` ＝ 成之列之 (街廓, 端, 候選)；以 (街廓, 候選) 之排序之多重集對 `successes`、另判重複 ⇒ 不合即停機；成者 ≥ `1` ⇒ `alloc_state` 一次；`err` ⇒ 停機（「取得即鎖定之宗之查：試算中止 …」）；未保留 ⇒ 停機（「取得即鎖定之宗之查：成者 <街廓> <端>端 <暫編地號>、… 於試算⛔ 保留——程式錯誤 ⇒ 停機」·唯具未保留者）；步驟 10 之首次 `_cur` ＝ 此試算（⛔ 另呼·其下之 `err` 之判不可達而留之）。
- `R-4⁗`：`W-G.9-388` `R-5` 之註解與 `_recv_out` 之查整段刪之（「於現態未保留」`1` → `0`）。
- `R-9‴`：區域函式 `_rk390`（內呼頂層 `k967_rank`／`k967_pre_area`·表 ＝ 現態之分攤登記面積 − Σ段三部分併出·成員 ＝ 候選 ∪ 整筆併入之片）；`_ct_cross` 之整片各試而二端皆成 ⇒ `_ct_pick(A, B, '一', _two390)`；`_ct_pick` 增 `rk390=None`；題二之二行與 `_ct_pick(A, B, '二')` 各恰一見、⛔ 動。
- `§三-3⁗` 之自查：`F23 wiring`、`F24 wiring` 撰碼中自跑皆綠；新增之列無「四空白＋中文」起首者；新區域名皆帶 `390`。

## 七、自捕與自解

1. 施後 `74` 呼叫之總時長逾背景工作之 `2` h 上限 ⇒ 初起之背景工作（未有任一呼叫之結果寫出）即止之、清其出艙，以脫離之程序從頭重起；其後 `74` 呼叫皆一趟而畢（⛔ 重跑之例）。
2. 清理殘程序之 `pkill -f` 之字樣命中其自身之殼（`rc 144`）；其後以 `ps` 判之、無殘程序。
3. 撰碼中之 `py_compile` 生 `/tmp/dev/__pycache__/` ⇒ 即刪之；施工樹之 `py_compile` 所生之 `/tmp/w/__pycache__/` 亦即刪之（皆 `.gitignore` 所忽·⛔ 入 `commit`）。
4. 接單之 `ops/queue` 之推送初被拒（發單端同時推 `b5cff50`·門鈴與交接之更新）⇒ 重新取之、`STATE` 仍 `pending`、單檔⛔ 變 ⇒ `rebase` 後推（`3e86505`）。

## 八、待發單端

- 復驗本批（`§四-2⁗`：自倉從頭重跑 `V-1⁗`〜`V-9⁗` 與收工閘）⇒ 入主線之短單（快轉 `2aa6302` → `ca3ea9eb674ae5c411a4969f68398baf74be9745`）＋ `基準/<新主線之全 sha>.md`。
- 本機之耗時約為發單端之 `1.6` 倍（`#25` `2912` s、`#67` `2088` s、`#68` `2028` s）——次單之時程或宜計之。

## 附錄　收工閘 `5⁗` 之 `git ls-remote --heads origin`（推後·`50` 列）

```
a18bb57064a308c8eddaa8b6d2a354681a67b844	refs/heads/claude/wg9-95z-v3-resume-hgpzfs
6cb77b7f0c08e2edf62f8e9cd239efa774a98d95	refs/heads/main
bbdd19968d342cb2136f0d685d847061e6146436	refs/heads/ops/queue
b772f8aa09820f01312081588fd8c8d718c8ac86	refs/heads/verify/W-G.9-198R-c1
a1107a17825c37430f69349afaceef4d09c6f5f8	refs/heads/verify/W-G.9-198R-c2
6e677223e4ab2823f1a2d276bc5635472b4d51a7	refs/heads/verify/W-G.9-198R-c3
8b0534c451a45a8d066e7bbc98a6ee7d67323432	refs/heads/verify/W-G.9-219R2-c1
20b04ac8caa137108b24ecc0d27253076f43adcb	refs/heads/verify/W-G.9-229-c1
845d08db3cb63fa6562ebdf6459c56629de5f6b4	refs/heads/verify/W-G.9-243-c1
6b5fe718a0d53d07b86a460d520037affa555a1b	refs/heads/verify/W-G.9-244-c1
1a6a357aa797e06cfd8f60db9fa6a6a032a221f8	refs/heads/verify/W-G.9-244-c2
29ebc141aab5e1fa49d1712dbb8322c54109497e	refs/heads/verify/W-G.9-246-c1
910d5e785a301c0e6564bab30c9b376b8bda5143	refs/heads/verify/W-G.9-247-c1
2709504b2aad9f4924d4182ef37e3d47d861767e	refs/heads/verify/W-G.9-248-c1
3242e962f52aa1f170cb69c6b2db28a666c2994f	refs/heads/verify/W-G.9-255-c1
e9d1b9c3e6e46580da28392e1ed7495d5b34638f	refs/heads/verify/W-G.9-261-c1
36385ef061591b5366b3295061efaa15f3a18b21	refs/heads/verify/W-G.9-268p-c1
95a530c187ca8f6b15581a1250e2a72dcfe7eb6d	refs/heads/verify/W-G.9-268p-c2
363602b874992e30aaea72576e536cf1cedba657	refs/heads/verify/W-G.9-268p-c3
2f1292748d1326f1590ae20d5d18dd8f5364af5b	refs/heads/verify/W-G.9-269-c1
dc373d018fa04a2a2538d04b6b194a1dfb4dcd3d	refs/heads/verify/W-G.9-269-c2
ce06622f2caa8e0f3bac03c347c7e041e84b73b4	refs/heads/verify/W-G.9-269-c3
05a11bd665f6c2790ff821c9e3a1606651e345d4	refs/heads/verify/W-G.9-269-p3a
488c4858da63ebe370ed950788947aa742eb44ad	refs/heads/verify/W-G.9-299-gb170
be5108d0067e63e23a397fdcbe43358800381470	refs/heads/verify/W-G.9-333-gb168
2ec1eb2bf43616ce662d95dc633b4c71f366eb15	refs/heads/verify/W-G.9-338-origin
d0add71ff85e62c2afb1f2f5d327c4488624c4a1	refs/heads/verify/W-G.9-341-gb182
14e022265bd1c190d7d6f9c1a0c6900bcec120db	refs/heads/verify/W-G.9-343-k929b
1ef3bb5678473f4df2ab780ba1bdfa22cb09b05f	refs/heads/verify/W-G.9-353-endmerge
4716f202bfd9368d960b942025b2bb8da34c6dd6	refs/heads/verify/W-G.9-357-k948
bd072eb8924d7139d1c1bb6e39129f8b8be93f8b	refs/heads/verify/W-G.9-359-cand
924d91634b1b36ea1d5fbbffd4a6791693ad3311	refs/heads/verify/W-G.9-361-k954
cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce	refs/heads/verify/W-G.9-363-k953
e7855ecf75ca4ed692baa982f5f25ec672847e79	refs/heads/verify/W-G.9-367-adj4
fe1fe3bf59eb778f3ec99b4c6cf8e1658eaa2583	refs/heads/verify/W-G.9-370-selfchk
cf08e23f11b3193a0bc2657bf7964562615ab5df	refs/heads/verify/W-G.9-373-k966
96bd6fe5daa32bbbb82564f733e5ec875cd740ab	refs/heads/verify/W-G.9-375-k965
3f46284d4abb8374b1425eeb1b491fe53fedad18	refs/heads/verify/W-G.9-378-gb204
37f30e196d40d3ce528214b72b2df12ca333394f	refs/heads/verify/W-G.9-380-k375s
32f70d69ba23add4e46776c3629a0a301ae19af6	refs/heads/verify/W-G.9-382-k973
fa31382fab2ca953d3cce5e8d478e8166cb937b7	refs/heads/verify/W-G.9-383-k975
663a457bb111a27e694038b2cdd22cb5c1dc8807	refs/heads/verify/W-G.9-384-k971
8d0a99091b848bd33637f94ed8323c276ce81f74	refs/heads/verify/W-G.9-385-k974
fd9ef0fa136bcc0f2ab0d1e88c7632b539cbf753	refs/heads/verify/W-G.9-387-k961h
929ea20434fe0d1b06e6c94a7cdc85ef145ae7fb	refs/heads/verify/W-G.9-388-k961s3
2aa63021da38632704519e05d53ced9f56e22659	refs/heads/verify/W-G.9-389-trialstop
ca3ea9eb674ae5c411a4969f68398baf74be9745	refs/heads/verify/W-G.9-390-k961r
886645475b60f790c06d52333501e917596c28be	refs/heads/wip/W-G.4-S0b-S0c
c286a79cc6a699c57c7763306c4beae9ef7b60a3	refs/heads/wip/W-G.9-318-preserve
2aa63021da38632704519e05d53ced9f56e22659	refs/heads/wip/s1-endpart
```
