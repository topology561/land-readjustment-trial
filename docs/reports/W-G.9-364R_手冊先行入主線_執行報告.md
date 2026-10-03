# `W-G.9-364R`　執行報告：主線快轉（至 `cb5490a`·手冊先行入主線）＋ 量測器 `F23` 之增項（`K39`／`K40`）＋ `run_all` 之 `k*` 經驗錨之重錨 ＋ 攢批登記 ＋ `K-6` 典之註 ＋ 待落地清單之更新

> 受單 ＝ CC 新窗·`2026-10-04`。施工樹 ＝ `.claude/worktrees/w-g-9-364-processing-c6a906`（開窗時在分支 `claude/w-g-9-364-processing-c6a906` 之 `7d8e954`；`git checkout --detach origin/verify/W-G.9-363-k953` 後開工）。倉外出艙目錄 `<O>` ＝ `C:\Users\admin\AppData\Local\Temp\wgO364`；倉外工具 ＝ `…\wgT364`（抽取器 `blocks.py`、意指占用之計數器 `occ_num.py`、前置與出艙之殼 `pre0.sh`／`post0.sh`、工項一之殼 `step1.sh`、`run_all` 之殼 `runall.sh`、附加器 `append3.py`、收工閘之殼 `gates.sh`／`gates_git.py`、本報告之建構器）；拋棄式 worktree `<P>` ＝ `…\wgP364`（工項一之必破三態與工項二之 `run_all` 前後皆用此一路徑·每次跑畢即 `git worktree remove --force`）。
> 開工態：主線 `7d8e9547a00d31bd7afdef43f1ccbffdd3c673ad`；側支 `verify/W-G.9-363-k953` ＝ `cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce`；遠端 heads `35`。
> 來源檔：施工樹之根無之；取自第二處（KL 主 checkout 之根·`W-G.9-364_中量單.md`·`81543` B）；二進位複製（`cmp` 逐位同）。

## ①　逐 `commit`

| 工項 | `commit` | 內容 |
|---|---|---|
| 零′ | 無 `commit` | 遠端 `refs/heads/wip/s1-endpart`：`7d8e9547a00d31bd7afdef43f1ccbffdd3c673ad` → `cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce`（`git push origin cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce:refs/heads/wip/s1-endpart`·快轉·⛔ `--force`·首推即成） |
| 零 | `e14d2ef72032d9357d67693375450aff9211629c` | `docs/orders/W-G.9-364_中量單.md`（新檔·`550`／`0`·入倉 blob 之 `sha256` ＝ `99d6b5a842a9cf9973fe1c078ec2deb43e78e9cb46622e90fbcbf3083fcbd2f2` ＝ 來源·`cmp` 逐位同） |
| 一 | `c4820a02e517f724c4448f4a8ef6cbfdf0806097` | `verify/probes/probe_WG9363_k953.py`（`29`／`0`·blob `4943b1162789fe6e6b1cc11f4e78dd1fcc4e5d99` → `de0a7e0629e81db3bee6d22918e169ba29cddd39`·`77638` → `79351` B） |
| 二 | `aa94de3616ea6881ca1727a16b7ca7779ad91256` | 🔴 `verify/run_verification.py`（`5`／`2`·blob `3bd2b378368df204f0c0fca1734d597851e1252b` → `f5b896e5a702c5d958e3ba27091d27832385efc4`·`103178` → `103754` B）·`K_STAR_EXPECT` 之二列之值與其註 |
| 三 | `0f106cec8f9b5f0a0ccd01f870f799deee0aa9df` | `docs/rulings/K-6_街角地分配程序與可分配判準.md` `10`／`0`；`docs/reports/W-G.4_泛用阻塞項登記表.md` `20`／`0`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` `112`／`0`；`CLAUDE.md` `25`／`0` |
| 四 | （本報告） | 本檔 |

## ②　停機款 `1`〜`14`

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `7d8e954`、側支 `cb5490a`、施工樹追蹤檔無變動、heads `35`、`§零-0` 項 `3` 之 `rc` 與四簿 | `git fetch origin` 後主線 `7d8e9547…`、側支 `cb5490a9…`；`git checkout --detach origin/verify/W-G.9-363-k953` 後 `git status --porcelain --untracked-files=no` 空；heads `35`；`probe_WG9321_issuer_anchor.py <repo> <檔> 566 565` ⇒ `rc 0`·`stderr` `0` B·「項4′ 四簿·正典框」自誤 相異 `551`／`MAX` `566`、`GB` `193`／`200`、`VR` `80`／`95`、`K-9` `52`／`55`（缺號 自誤 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`·`GB` `[12, 87, 179, 181, 183, 184, 185]`·`VR` `[73, 75]`·`K-9` `[44, 47]`） ⇒ 未觸 |
| `2` | 本單之 bytes／`sha256` ＝ KL 之訊、`SELF_SHA256` 自驗相符、來源檔在、入倉逐位同 | `81543` B·`sha256` `99d6b5a842a9cf9973fe1c078ec2deb43e78e9cb46622e90fbcbf3083fcbd2f2`·CR `0`·LF `550`；KL 之訊逐字載「`81543 B·sha256 99d6b5a8…bd2f2`」——bytes 相符，`sha256` 為縮寫（首 `8` 碼・末 `5` 碼）而與實算之首末逐碼相符 ⇒ 全 `64` 碼之據依 `§零-0` 項 `4` 取 `SELF_SHA256`：`P-5` 原口徑之受詞 `81465` B·實算 ＝ 單載 `68b2a4ddb0fc50a9cc32b2e832c344a56220dad5a2e50b74587615a03608bdc0`；來源在第二處；入倉 blob ＝ 來源（`cmp`） ⇒ 未觸 |
| `3` | 工項零′ 前置皆符 | 見 ③ ⇒ 未觸 |
| `4` | `push` 不被拒、⛔ `--force` | 首推即成（`7d8e954..cb5490a`） ⇒ 未觸 |
| `5` | 快轉後 ①〜④ 皆符 | 見 ③ ⇒ 未觸 |
| `6` | 八塊逐位同 `§五-1`；`git apply --check` 過；施後之 blob | 見 ⑥；`F23t` ⇒ `de0a7e06…`、`RV1` ⇒ `f5b896e5…`、`MA` ⇒ `app.py` `293e14a0…`、`MB` ⇒ `5da75a5c…`（`--check` 皆過·`--numstat` `29`／`0`、`5`／`2`） ⇒ 未觸 |
| `7` | 工項一之四態 | 見 ④ ⇒ 未觸 |
| `8` | 四簿刪除欄 `0`、嚴格前綴 | 見 ⑥ ⇒ 未觸 |
| `9` | 收工閘 | 於對話出艙（自指·⛔ 寫入本檔） |
| `10` | 工項五 | 於對話出艙（本報告入倉之後） |
| `11` | `push` 目標皆 `wip/s1-endpart`、⛔ 推側支 | 工項零′／零／一／二／三之 `push` 目標皆 `wip/s1-endpart`；側支⛔ 推 ⇒ 未觸 |
| `12` | ⛔ 判正典、⛔ 改塊器命令 | 未改任何塊、器、命令一字（`<repo>` 依單首 🔑 之形傳入） ⇒ 未觸 |
| `13` | 新檔⛔ 為 `git check-ignore` 所命中 | 本單 `rc 1`（無命中）；本報告於 `commit` 前實查（結果於對話出艙） ⇒ 未觸 |
| `14` | 工項二之驗 ＝ `§一` 項 `8` | 見 ⑤ ⇒ 未觸 |

開場之餘項：
- 旗標之環境 `[None, None, None, None]`；`python` ＝ `3.13.11`；`core.autocrlf` 有效值 `false`；`core.longpaths` `true`。
- 取號現查（`wg9268_gate6_occupancy.py cb5490a W-G.9-364 W-G.9-363 W-G.9-396`·`rc 0`·`stderr` `0` B·母體 `docs/` `962` 檔·讀不到 `20`〔git 失敗 `0`＋解碼失敗 `20`〕）之諸數與 `§零-1` 表逐格相同：受詢之號 嚴格與寬式之 `D1`／`D2`／`D3` 全 `0`、鬆框 `0`／`0`；對照甲 嚴格與寬式皆 `19`／`37`／`3`·列框 `40`·檔框 `21`·鬆框 `18`／`302`；對照甲′ 宣告框全 `0`·鬆框 `14`／`22`；人造對照乙 嚴格全 `0`·寬式 `D3` `2`（列框 `2`·檔框 `1`）·鬆框 `27`／`30`（同 `§零-1` 之具名豁免）。🔒 本報告⛔ 內嵌該器之原樣出艙列（`W-G.9-357` 節所載之自指）。
- 意指占用（母體 ＝ `cb5490a` 之追蹤檔 `2777` 檔·列框·`git grep -c` 之列數合計）：`自誤 567`〜`577` 之裸（錨定）列逐號 `27`／`42`／`160`／`92`／`68`／`151`／`34`／`69`／`211`／`123`／`45`·平形皆 `0` 唯 `574` ＝ `8`（`git grep -o -E` 實查：`8` 筆皆 `自誤 5741`）·B 形皆 `0`·C 形皆 `0`；對照甲 `自誤 566` 裸 `98`·平 `16`·B `0`·C `15`；`GB-201` 平 `0`；對照甲 `GB-200` 平 `74` ＝ `§零-1` 表。
- pre-flight（`probe_order_preflight.py <本單>`）`rc 0`·`stderr` `0` B·🔴 `0`／🟡 `4`（`P-4` `:73`、`:198`、`:305`、`:530`·皆同 `§五-1` 項 `12` 之具名豁免·採之）／ℹ️ `2`（`P-5` 相符·受詞 `81465` B；`P-3` `def main` ＝ `21232`–`28952`）。

## ③　工項零′ 之出艙

前置（`<O>/pre0/pre0.log` 全文·前置 `3` 之逐筆含空輸出·逐筆之 `git diff --name-only` 之原出艙另存 `<O>/pre0/p3_<commit>.txt`）：

```text
== 1 ==
is-ancestor rc=0
count A..B = 17
count B..A = 0
merges A..B = []
== 2 ==
glob 形 列數 = 2
app.py
verify/selection_pipeline.py
（對照）無 :(glob) 形 列數 = 9
cb5490a:app.py = 176f90c96f6c13ede5c0c4e2425bebbbe827bf51
cb5490a:verify/selection_pipeline.py = c5e9fb05e222a6d43a1aa115494b0034435a0cd8
== 3 ==
cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce 0 列 []
6944a1197426df43f2bd68b1f5e0b15c4aa7b770 0 列 []
aab15b159bc34500e47325017482522137ff9bae 2 列 [app.py verify/selection_pipeline.py ]
03f47a2b003cd910bd0f3fdd09e578a36d92d6a0 0 列 []
81c5de687ecd3a2de599e0757f699320a8241cdd 0 列 []
6b3480d93f5172429f8ed65775b8bed36f434a36 0 列 []
d746b4b9b4e125903d48187d7fd6d4d372872f87 0 列 []
4a48bd68009218a7a3489e8aa0e6eefe51748f0c 0 列 []
db1b395a03c93b079661b5591a40f0740196f3d0 0 列 []
a0b9b12a075a70a1b207422be70aa45a55f3f590 0 列 []
2894acb571a8074a404c04f1c25b90b180efa219 0 列 []
e29cd8c78dbaeea8aac4553247795f0f0f4d3c3f 0 列 []
7c09770c4dadf36113141ff07e7cf206bfeb6823 0 列 []
a005da74e94b35e23b2422bcfcf162a5a0e4a6e3 0 列 []
b0f51bef0aac8540a799a5bd0ef775c4b69c4804 0 列 []
0a4a812becebe4949030316f48b252af8e1943da 0 列 []
0a79302d36ba218c530b2ae91b51c3da2d0bfa77 0 列 []
逐筆 17 筆·命中 ≥1 列者 1 筆
```

快轉（`<O>/ff_push.log` 全文）：

```text
To https://github.com/topology561/land-readjustment-trial.git
   7d8e954..cb5490a  cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce -> wip/s1-endpart
```

快轉後（`<O>/post0.log` 全文·③ 之生產碼 ＝ `app.py` ＋ `verify/` 頂層 `*.py`·② 之 heads 前後之差除 `wip/s1-endpart` 外為空）：

```text
① cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce	refs/heads/wip/s1-endpart
② heads = 35
   heads 前後之差（除 wip/s1-endpart）:
   （無差）
③ 生產碼 34 檔·新主線 vs cb5490a 相異 = 0；判別力 vs 7d8e954 相異 = 2 [ app.py verify/selection_pipeline.py ]
④   origin/verify/W-G.9-363-k953   origin/wip/s1-endpart 
```

其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `cb5490a9555f2c7a1a1c22cd36045b7fb2d568ce`。

## ④　工項一之四態

`F23` 一律自施工樹跑之（施塊後 blob `de0a7e06…`）；必破三態之 `<P>` 依序 `add` → `apply` → `hash-object` → `selftest` → `remove`（`<O>/step1_summary.txt` 全文）：

```text
必過 selftest｜rc 0｜4s｜stderr 0B｜末列：⇒ 紅 []；rc 0
必過 wiring 7d8e954｜rc 0｜39s｜stderr 0B｜末列：⇒ 紅 []；rc 0
B3：apply rc=0·app.py=7b6c7dc2a301391b03b4d0c12e6a39b3251586b0（期 7b6c7dc2a301391b03b4d0c12e6a39b3251586b0）
必破 B3 selftest｜rc 1｜4s｜stderr 0B｜末列：⇒ 紅 ['K37', 'K38', 'K39', 'K40']；rc 1
B3：worktree remove rc=0
MA：apply rc=0·app.py=293e14a030ed58204e9cb52a9b515a83d9f67bb7（期 293e14a030ed58204e9cb52a9b515a83d9f67bb7）
必破 MA selftest｜rc 1｜4s｜stderr 0B｜末列：⇒ 紅 ['K39']；rc 1
MA：worktree remove rc=0
MB：apply rc=0·app.py=5da75a5c7cfa1cdd63a27f3df380e59aff207035（期 5da75a5c7cfa1cdd63a27f3df380e59aff207035）
必破 MB selftest｜rc 1｜4s｜stderr 0B｜末列：⇒ 紅 ['K39', 'K40']；rc 1
MB：worktree remove rc=0
step1 done
```

必過·`selftest`（施工樹·`app.py` `176f90c9…`）·`<O>/f23_self.log` 之末十列（`K1`〜`K40` 之 ✅ 計 `40`、🔴 計 `0`）：

```text
  ✅ K34 K-9-51 之本街廓之候選之成員取當下之試算：其單元於 C0 之後始含與 x 相接之片 ⇒ 停機（入池閘之射程）；該片⛔ 與 x 相接 ⇒ 併入之；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ ⛔ 停機（⛔ 取聯集）
  ✅ K35 整筆者於候選之迴圈之前全檢本街廓之候選：G 較大而⛔ 與 x 相接之宗居先、G 較小者與 x 相接 ⇒ 停機；後者⛔ 與 x 相接 ⇒ 併入 G 較大者
  ✅ K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（K-9-51 之「剩餘土地」不立）；皆非 ⇒ 併入
  ✅ K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（K-9-53 ① 之「分不到」不立）；皆非 ⇒ 併入其計畫之受併宗
  ✅ K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連 ⇒ 停機（入池閘之射程）——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片，皆停機；⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ ⛔ 停機（⛔ 取聯集）
  ✅ K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）
  ✅ K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 40／40
⇒ 紅 []；rc 0
```

必過·`wiring … 7d8e954`·`<O>/f23_wir.log` 之末十列：

```text
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['K953_ENV', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['run_corner_pk_k6b', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（642）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（180）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
```

必破甲（`03f47a2` ＋ 倉內 `docs/reports/W-G.9-363R_補令三續辦_二檔差異.diff` ⇒ `app.py` `7b6c7dc2…`）·`<O>/f23_B3.log` 之紅項之列與末列：

```text
  🔴 K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（K-9-53 ① 之「分不到」不立）；皆非 ⇒ 併入其計畫之受併宗：得 (('無停機',), ('無停機',), [('手冊', 'X(1)', 'a', 'B1(1)', (('B1(1)', 300.0),), '成')])　期 (('停機', True), ('停機', True), [('手冊', 'X(1)', 'a', 'B1(1)', (('B1(1)', 300.0),), '成')])
  🔴 K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連 ⇒ 停機（入池閘之射程）——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片，皆停機；⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ ⛔ 停機（⛔ 取聯集）：得 (('無停機',), ('無停機',), [('手冊', 'X(1)', 'a', 'B1(1)', (('B1(1)', 300.0),), '成')], [('手冊', 'X(1)', 'a', 'B1(1)', (('B1(1)', 300.0),), '成')])　期 (('停機', True), ('停機', True), [('手冊', 'X(1)', 'a', 'B1(1)', (('B1(1)', 300.0),), '成')], [('手冊', 'X(1)', 'a', 'B1(1)', (('B1(1)', 300.0),), '成')])
  🔴 K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）：得 (('無停機',), ('無停機',))　期 (('停機', True), ('停機', True))
  🔴 K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）：得 ('無停機',)　期 ('停機', True)
  ✅ P0 逐項擾動恰該項紅 40／40
⇒ 紅 ['K37', 'K38', 'K39', 'K40']；rc 1
```

必破乙（`cb5490a` ＋ 塊 `MA` ⇒ `app.py` `293e14a0…`）·`<O>/f23_MA.log` 之紅項之列與末列：

```text
  🔴 K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）：得 (('無停機',), ('無停機',))　期 (('停機', True), ('停機', True))
  ✅ P0 逐項擾動恰該項紅 40／40
⇒ 紅 ['K39']；rc 1
```

必破丙（`cb5490a` ＋ 塊 `MB` ⇒ `app.py` `5da75a5c…`）·`<O>/f23_MB.log` 之紅項之列與末列：

```text
  🔴 K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）：得 (('停機', True), ('無停機',))　期 (('停機', True), ('停機', True))
  🔴 K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（K-9-53 ① 之「分不到」不立·K-9-51 之「剩餘土地」不立）：得 ('無停機',)　期 ('停機', True)
  ✅ P0 逐項擾動恰該項紅 40／40
⇒ 紅 ['K39', 'K40']；rc 1
```

四態之 `P0` 皆 `40／40`、`stderr` 皆 `0` B。

## ⑤　工項二之 `run_all`

二跑皆於倉外之 `<P>` ＝ `C:\Users\admin\AppData\Local\Temp\wgP364`（前後同一路徑·跑畢即 `git worktree remove --force`·殼之旗標 `[None, None, None, None]`）：

| 跑 | 受詞（`<P>` 之 `HEAD`） | `verify/run_verification.py` | `rc` | 耗時 | `stderr` | 出艙 |
|---|---|---|---|---|---|---|
| 前（工項一之端·塊 `RV1` 施前） | `c4820a02e517f724c4448f4a8ef6cbfdf0806097` | `3bd2b378368df204f0c0fca1734d597851e1252b` | `1`（`W-V run_all: FAIL`·常態） | `1708` s | `0` B | `<O>/runall_pre.log` |
| 後（工項二之 `commit`） | `aa94de3616ea6881ca1727a16b7ca7779ad91256` | `f5b896e5a702c5d958e3ba27091d27832385efc4` | `1`（同上） | `1958` s | `0` B | `<O>/runall.log` |

塊 `RV1` 之施：`git apply --check` 過；`git apply` 後 `hash-object` ＝ `f5b896e5…`（`103754` B）；`git diff --numstat` ＝ `5`／`2`（唯 `verify/run_verification.py`）；`python -m py_compile verify/run_verification.py`（殼設 `PYTHONDONTWRITEBYTECODE=1`）`rc 0`·所生之 `verify/__pycache__/`（`run_verification.cpython-313.pyc` 一檔）於 `commit` 前去之；施前後之 AST（倉外 `astcmp.py`·節點數 `14224`／`14224`）相異唯 `5` 個 `Constant`：`0m` 之 `R2` `7 → 6`、`R3` `5 → 4`，`3.5m` 之 `R1` `1 → 2`、`R2` `5 → 6`、`R3` `5 → 4`（其餘節點逐一同型同值）。

`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall.log` ⇒ `rc 0`·`stderr` `0` B（`<O>/runall_cmp.log` 全文）：

```text
【runall】項 64／64·PASS 26 → 28·FAIL 38 → 36
  #17 k* 六塊經驗錨0m {'R1': 2, 'R2': 7, 'R3': 5, 'R4': 1, 'R5': 4, 'R6': 3} ⇒ 名目改為 k* 六塊經驗錨0m {'R1': 2, 'R2': 6, 'R3': 4, 'R4': 1, 'R5': 4, 'R6': 3} ｜狀態 FAIL → PASS｜違規數 0 → 0｜本體 異
  #27 k* 六塊經驗錨3.5m {'R1': 1, 'R2': 5, 'R3': 5, 'R4': 1, 'R5': 4, 'R6': 3} ⇒ 名目改為 k* 六塊經驗錨3.5m {'R1': 2, 'R2': 6, 'R3': 4, 'R4': 1, 'R5': 4, 'R6': 3} ｜狀態 FAIL → PASS｜違規數 0 → 0｜本體 異
  #59 W-F F.1 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #60 W-F F.2 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #61 W-F F.3 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #62 W-F F.4 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  #64 W-G G.2 世代幾何曝出契約 ｜狀態 FAIL → FAIL｜違規數 1 → 1｜本體 異
  相異項 7；其餘 57 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／38 → 22／36；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
```

⇒ ＝ `§一` 項 `8` 之期：項 `64／64`·PASS `26 → 28`·FAIL `38 → 36`；**相異項恰 `7`**（`#17`、`#27`：`FAIL → PASS`·其名目之值改為 `{'R1': 2, 'R2': 6, 'R3': 4, 'R4': 1, 'R5': 4, 'R6': 3}`；`#59`〜`#62`、`#64`：`FAIL → FAIL`·違規數 `1 → 1`·本體異）；其餘 `57` 項逐項同；末端夾具／golden `21／21`·相異 `0`；對帳 `22／38 → 22／36`、含「對帳 FAIL」二態皆 `True`；末列二態皆 `W-V run_all: FAIL`。

`k*` 之二列（前·`runall_pre.log`）：`🔴 FAIL  k* 六塊經驗錨0m {'R1': 2, 'R2': 7, 'R3': 5, 'R4': 1, 'R5': 4, 'R6': 3}`（實得 `{'R1': 2, 'R4': 1, 'R6': 3, 'R5': 4, 'R2': 6, 'R3': 4}`）、`🔴 FAIL  k* 六塊經驗錨3.5m {'R1': 1, 'R2': 5, 'R3': 5, 'R4': 1, 'R5': 4, 'R6': 3}`（實得同）；（後·`runall.log`）：`✅ PASS  k* 六塊經驗錨0m {'R1': 2, 'R2': 6, 'R3': 4, 'R4': 1, 'R5': 4, 'R6': 3}`、`✅ PASS  k* 六塊經驗錨3.5m {'R1': 2, 'R2': 6, 'R3': 4, 'R4': 1, 'R5': 4, 'R6': 3}`。「結構不變量永久閘」二退縮於後仍 `✅ PASS`（⛔ 在相異之列）。

`diff runall_pre.log runall.log`（出艙·⛔ 入判）⇒ `58` 列·`4478` B·異列（`<`／`>`）`30`：`k*` 之二項 `6` 列；對帳之名目數與「現況有而凍存無」之列 `4` 列；其餘 `20` 列皆為 traceback 中 `verify/run_verification.py` 之列號，逐對增 `3`（`1087 → 1090`、`1138 → 1141`、`1204 → 1207`、`1271 → 1274`、`1470 → 1473`·各見於本體與對帳段二處）＝ 塊 `RV1` 所增之註三列 ⇒ `#59`〜`#62`、`#64` 之「本體異」唯此。

二跑跑畢時 `<P>` 之 `git status --porcelain`（`run_all` 之既知副作用·⛔ 入倉·`<P>` 隨即移除）二態同：`M` `verify/out/probe_ruling_K4_s_origin.log`、`verify/out/probe_ruling_K8_baseline_pairing.log`、`verify/out/probe_ruling_K8_sideline_pairing.log`、`verify/out/probe_ruling_N_e1_touch.log`；`??` `verify/out/E系列實測快照_退縮0m.csv`、`verify/out/E系列實測快照_退縮3.5m.csv`（＝ `CLAUDE.md` 所載 Windows 之 `4` 檔＋`2` 檔）。

工項二之 `push`（驗皆符之後·分開之呼叫）：`c4820a0..aa94de3`·首推即成。

## ⑥　八塊之實得與四簿

| 塊 | 圍欄（`1` 起算·開列–閉列） | bytes | `sha256` | 列 | 判 |
|---|---|---|---|---|---|
| `F23t` | `246`–`301`（`diff`） | `3348` | `8ebfba37deb3968fdab69a02165c87badc763312d0fad8835250ee68f8e4a102` | `54` | ＝ `§五-1` 項 `2`（施後 blob `de0a7e06…` 亦符） |
| `RV1` | `305`–`325`（`diff`） | `2026` | `1befaa1165eb92b725f500811eb9766a01ad4deb84b7e8be1d0ffe992aa06f25` | `19` | ＝ 項 `3`（施後 blob `f5b896e5…` 亦符） |
| `MA` | `329`–`343`（`diff`） | `873` | `6a0c90c5c100e34a5279e0d787b5b9ae3f9ebcc62aa2e752742c968da0181177` | `13` | ＝ 項 `4`（唯拋棄式 worktree） |
| `MB` | `347`–`361`（`diff`） | `929` | `7035d637595a0ba9e2230c8a4a7599842c55310621ae07151d2f8ce5f191c96c` | `13` | ＝ 項 `5`（唯拋棄式 worktree） |
| `K9` | `365`–`376`（`markdown`） | `2844` | `10911b5c7dcaec870a441a7d37fc20775512b815e4764949d2faccf1651de00a` | `10` | ＝ 項 `6` |
| `G8` | `380`–`401`（`markdown`） | `3353` | `229cf527fb692c75af76e48975658619aaeb358e57415bd0be6271a166f70e97` | `20` | ＝ 項 `7` |
| `E10` | `405`–`518`（`markdown`） | `13966` | `5b7f6a6366d42b038deec58629593a571884d2f01db2b5578ff37b0df97ffa14` | `112` | ＝ 項 `8` |
| `P18` | `522`–`548`（`markdown`） | `5137` | `fef7be7b3937c3b18d92785c70da3f6c2911fa87c8f9cd036e91274a6e85e0f4` | `25` | ＝ 項 `9` |

（八塊之 CR 皆 `0`。）

| 簿 | 改前（`cb5490a` 之 blob） | 改後（工項三之 blob） | 改後 `sha256` | 增／刪 | 嚴格前綴 |
|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `475428` B | `478272` B | `d312b69f6680c34c6e34728afea265ef6a25d9c68943e5fe521b00f74920eae6` | `10`／`0` | 真 |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1038971` B | `1042324` B | `9a1691dd84175609c57a583b8f57773f18097371fe336b005f233e2940c6c86e` | `20`／`0` | 真 |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1105341` B | `1119307` B | `f81124265b85bb3f05f235188b477a7be72fc50e26cde9bf72567858fa9d6863` | `112`／`0` | 真 |
| `CLAUDE.md` | `328972` B | `334109` B | `a7a53c3a5fdf259c678dcef012ae868783e87c911e08cf30ca11e309f150d709` | `25`／`0` | 真 |

（四簿改前皆以換行結尾·CR `0`；附加器 `append3.py` 先乾跑、全符後方寫；改後之 bytes 為倉側 blob 之 `cat-file -s`。工項三之 `push` 前另以 `probe_WG9270_closegate.py 577 566 .` 預量 ⇒ `rc 0`·`✅ 二閘皆過`〔自誤 相異 `562`／`MAX` `577`、`GB` `194`／`201`、`VR` `80`／`95`、`K-9` `52`／`55`〕；正式之閘 `6` 於對話出艙。）

## ⑦　`§二` 之放行

KL 貼本單之同一訊息內逐字答：「問二之答：是。」（該訊全文逐字：「請依 W-G.9-364_中量單.md（81543 B·sha256 99d6b5a8…bd2f2）辦理。問二之答：是。」）⇒ 依 `§二`，視為工項零′（主線快轉）、工項二（`verify/run_verification.py` 之期值之更·🔴）與工項五（主 checkout 之同步）之放行。所答之【要你判斷】逐字 ＝ 「是否同意將手冊先行併入主線、更新驗證用的參考數字，並請 CC 同步您本機的程式資料夾（併於 364 辦理）？（是／否）」。快轉於前置皆符之後、以分開之呼叫行之；工項二之 `push` 於其驗皆符之後、以分開之呼叫行之。

## ⑧　CC 之自捕與自解

**本批之自解清單**：無（本批⛔ 以 `作業常規之追加五` 之自解款續辦任何疑義）。

1. **來源檔之取處**：依單首 🔑 之序，施工樹之根無 `W-G.9-364_中量單.md`；取自第二處（KL 主 checkout 之根）·二進位複製（`cmp` 逐位同）。⛔ 取自第三處 ⇒ 工項五之撞檔前置⛔ 因此觸發（其乾跑之預覽見下 `5`）。
2. **KL 之訊之 `sha256` 為縮寫**：KL 之訊載「`81543 B·sha256 99d6b5a8…bd2f2`」——bytes 相符；`sha256` 唯首 `8` 碼與末 `5` 碼，與實算之首末逐碼相符。依 `§零-0` 項 `4`（「照實具名而以 `SELF_SHA256` 為據」）以 `SELF_SHA256` 為全 `64` 碼之據（相符）·⛔ 停機。照實具名於此。
3. **長跑期間⛔ 動受測物**：工項一之四態跑於背景（一殼依序），期間⛔ 動施工樹之 `app.py` 與 `verify/`（唯讀之 `append3.py --dry` 與 `git apply --check` 除外）；工項二之二 `run_all` 皆於倉外之 `<P>`（前後同一路徑·跑畢即移除），塊 `RV1` 於前置之 `run_all` 跑畢之後方施（其 `--check` 於前置跑時行之·唯讀）。
4. **`py_compile` 之副產物**：殼設 `PYTHONDONTWRITEBYTECODE=1` 仍由 `py_compile` 寫 `.pyc`（該環境變數唯管 import）；所生之 `verify/__pycache__/` 於 `commit` 前去之（`git status --porcelain --ignored` 於 `commit` 前為空·見 ⑤）。
5. **工項五之乾跑之預覽**：工項一推後，以倉外 `step5.py --dry`（⛔ 移檔·⛔ `checkout`·⛔ `merge`）於 KL 主 checkout 預量撞檔前置：`HEAD` ＝ `cb5490a…`、追蹤檔無變動、`A`（當時之 `origin/wip/s1-endpart` ＝ 工項一之端）＝ `docs/orders/W-G.9-364_中量單.md` 一檔、`U` ＝ `102` 檔（含其根之本單）、`A ∩ U` ＝ 空。該預覽之 `git fetch origin` 唯更遠端追蹤 ref（主 checkout 與施工樹同一 `.git`）。正式之工項五於收工閘皆符之後行之，其出艙於對話。
6. **報告之自指**：本報告⛔ 內嵌取號器之原樣出艙列（上 ② 以散文轉述其數）；⛔ 書次一單號與本批以外之新號。
7. **heredoc 之守門器**：本批一切 Python 皆以 `Write` 落檔後以路徑呼叫（`W-G.9-360R`／`-362R` 所記之形·本批未觸）。
8. 本報告之 `git check-ignore` 於 `commit` 前實查（結果於對話出艙）。

## ⑨　各段耗時（本機 Windows·時刻為本機 `+0800`）

| 段 | 起 | 耗 |
|---|---|---|
| 開場（讀單・讀前窗之交接・`fetch`・態錨器・`SELF_SHA256`・八塊之抽取・pre-flight・取號） | `04:13` | 約 `3` 分（態錨器 `04:14:14`·抽取 `04:14:44`·pre-flight `04:14:51`·取號 `04:15:28`／`04:15:52`） |
| 工項零′（前置 ＋ 快轉 ＋ 出艙） | `04:16:1x` | `< 1` 分（前置 `04:16:13`·快轉 `04:16:21`·出艙 `04:16:41`） |
| 工項零（入倉・`commit`・`push`） | `04:17:00` | `< 1` 分 |
| 工項一（施塊・四態・`commit`・`push`） | `04:17:3x` | 約 `2` 分（`selftest` `4` s·`wiring` `39` s·必破三態各 `4` s·`commit` `04:19:05`） |
| 工項二 前置（`run_all`） | `04:19:17` | `1708` s |
| 工項二 施（塊 `RV1`・`py_compile`・AST 之比・`commit`） | `04:47:5x` | `< 1` 分（`commit` `04:48:24`） |
| 工項二 驗（`run_all`） | `04:48:3x` | `1958` s |
| 工項二 之比對與 `push` | `05:21:08` | `< 1` 分（`push` `05:21:35`） |
| 工項三（附加・`commit`・閘 `6` 之預量・`push`） | `05:21:40` | `< 1` 分（`commit` `05:21:48`·`push` `05:22:01`） |
| 工項四（本報告） | `05:22` | （時戳見其 `commit`） |
