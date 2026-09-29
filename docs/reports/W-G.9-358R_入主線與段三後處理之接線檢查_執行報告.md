# `W-G.9-358R`　入主線與段三後處理之接線檢查：執行報告

> **單** ＝ `docs/orders/W-G.9-358_輕量單.md`（`90856` B·`sha256` `b077096513f486030c0b020cde8a71cb6e6553530f9bfaa73ac142c86669fbae`·`SELF_SHA256` `564daf683158a9b028b9dc836714063688dde5b1ca30e7da83ff5194565695ac` 經 `P-5` 原口徑自驗相符）。
> **受單** ＝ CC（施工樹 ＝ `.claude/worktrees/wg-9-340-lightweight-7b2698`·detached）。**級** ＝ 輕（零生產碼·本批⛔ 跑 `run_all`）。
> **量測環境** ＝ Windows 11·Git Bash（`git version 2.53.0.windows.1`）·`Python 3.13.11`；殼之 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6` ＝ `[None, None, None]`；出艙目錄 `<O>` ＝ 倉外之 scratchpad。
> 🔒 本檔⛔ 載收工閘之實測值與工項四之出艙（自指）——二者於對話出艙。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 刪除欄 | 備 |
|---|---|---|---|
| 零′ 主線快轉 | （無 `commit`） | — | 遠端 `refs/heads/wip/s1-endpart`：`17624a19c48715bcb1bcfd6af1a851d756d6d473` → `4716f202bfd9368d960b942025b2bb8da34c6dd6`（`push` 之出艙逐字 `17624a1..4716f20  4716f202bfd9368d960b942025b2bb8da34c6dd6 -> wip/s1-endpart`·⛔ `--force`） |
| 零 本單原封入倉 | `0afa6a80f74cf8f47dc997c16f7a09fbb4926993` | `0`（`1026	0	docs/orders/W-G.9-358_輕量單.md`） | 入倉 blob `aa58a352ae3e6c61a635facd77bac9a179fc3023` ＝ 來源檔之 `git hash-object`；`git cat-file blob` 對來源 `cmp` 逐位同 |
| 一 量測器 `F17` | `a36f76646449f265d0eba10f76cf14ba72da2464` | `0`（`609	0	verify/probes/probe_WG9358_k948_wiring.py`） | 新檔 blob `755631288349fb04fd7b6d2b7cc1ad35ae14da0f`（＝ `§五-1` 項 `2`） |
| 二 攢批登記 ＋ 待落地 ＋ 續行 | `9fca83c5933b4578c4bf6a99b922405f13fc5baa` | `0`（`21	0	CLAUDE.md`／`24	0	docs/reports/W-G.9波_claude.ai側自誤登記.md`／`48	0	docs/reports/W-G.9波_恆常附款登記表.md`） | 三簿皆純末端追加 |
| 三 執行報告 | 本檔之 `commit`（自指·其 hash 於對話） | — | — |

各 `commit` 之生產碼判法（`CLAUDE.md` `常規一` 補款·`git diff --name-only <前> <本> | grep -xE 'app\.py|verify/stepg_pipeline\.py|verify/run_all\.py|verify/run_verification\.py'`）：工項零／一／二 皆命中 `0` 行（`grep` 之 `rc 1`·空輸出）。訊息首段皆單所令之逐字，末附 `Co-Authored-By` 一列（同前批之體例）。

---

## ② 停機款 `1`〜`13` 之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `17624a1`；側支 `verify/W-G.9-357-k948` `4716f20`；施工樹追蹤檔無變動；遠端 heads `32` | `origin/wip/s1-endpart` ＝ `17624a19c48715bcb1bcfd6af1a851d756d6d473`；`origin/verify/W-G.9-357-k948` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`；`git ls-remote --heads origin` `32` 列；`checkout --detach` 後 `status --porcelain --untracked-files=no` `0` 列 ⇒ 未觸 |
| `2` | 本單 bytes／`sha256` ＝ `§五-1`；來源檔可得；入倉 blob 與來源逐位同 | `SELF_SHA256` 所載 ＝ 實算（受詞 `90778` B·判別力：全檔之 `sha256` ≠ 所載 ⇒ `True`）；來源 ＝ **第二處**（KL 主 checkout 之根·第一處與第三處皆無）；入倉 blob 對來源 `cmp` 同 ⇒ 未觸 |
| `3` | 工項零′ 前置 `1`〜`3` 皆符 | 見 ③ ⇒ 未觸 |
| `4` | `push` ⛔ 被拒、⛔ 須 `--force` | 快轉一次即成 ⇒ 未觸 |
| `5` | 快轉後 ①〜④ 皆符 | 見 ③ ⇒ 未觸 |
| `6` | 六塊之 bytes／`sha256` ＝ `§五-1` | 見 ⑤ ⇒ 未觸 |
| `7` | 工項一：必過 `rc 0`、必破 `rc 1` 且末列逐字、二態全文與 `T1`／`T2` 逐列同 | 見 ④ ⇒ 未觸 |
| `8` | 三簿刪除欄 `0`、改前為改後之嚴格前綴 | 見 ⑤ ⇒ 未觸 |
| `9` | 收工閘皆符 | 於本檔入倉後量·其值於對話（自指·⛔ 入本檔） |
| `10` | 工項四之諸項 | 於收工閘之後辦·其出艙於對話 |
| `11` | 工項零〜三之 `push` 目標皆 `wip/s1-endpart`；⛔ 推側支 | 工項零′ `4716f20…:refs/heads/wip/s1-endpart`；工項零〜二 `HEAD:wip/s1-endpart`；⛔ 任何側支之 `push` ⇒ 未觸 |
| `12` | CC ⛔ 作「孰為正典」之判、⛔ 改塊／器／命令一字 | 六塊皆機械抽取後原樣使用；`F17` 未改一字；`<repo>` 以反斜線之絕對路徑傳入 ⇒ 未觸 |
| `13` | 本批新檔⛔ 為 `git check-ignore` 所命中 | 本單、`F17`、本檔三路徑之 `git check-ignore -v` 皆 `rc 1`（無命中） ⇒ 未觸 |

---

## ③ 工項零′：前置之全部出艙與快轉後之出艙

**前置 `1`〜`3`**（含逐筆判之空輸出·原樣）：

````text
## 前置 1
is-ancestor rc=0
count 17624a1..4716f20 = 8
count 4716f20..17624a1 = 0
## 前置 2
app.py
verify/selection_pipeline.py
lines=2
4716f20:app.py = d8938792ab09e71636dc6916b61432c522c847e5
## 前置 3（逐筆）
4716f202bfd9368d960b942025b2bb8da34c6dd6  命中 0 列
    （空輸出）
2009a786a1e09d8c7c053a54e4fe50126e336cce  命中 0 列
    （空輸出）
898c31fc6c18db156eb0eafe14366d3fb6f7ae30  命中 2 列
    app.py
    verify/selection_pipeline.py
3816a2f75cb857b5bd25c0119f0a3eabf129227d  命中 0 列
    （空輸出）
b41f305b82211e2dd13ee75c4e5e06dcfefc7692  命中 0 列
    （空輸出）
47207e94c6a5ac273e588e6c452ca0b4eb4d5122  命中 0 列
    （空輸出）
7165c229368188ee06c5143141a74adcbadf4a81  命中 0 列
    （空輸出）
84e5134399c31ef0aec76263b53edfc77838dad9  命中 0 列
    （空輸出）
````

**快轉後 ①〜④**（原樣；③ 之生產碼 `34` 檔 ＝ `app.py` ＋ `4716f20` 之 `verify/` 頂層 `*.py` `33` 檔）：

````text
① 4716f202bfd9368d960b942025b2bb8da34c6dd6	refs/heads/wip/s1-endpart
② heads=32
生產碼檔數 = 34
③ 新主線 vs 4716f20 相異 = 0
③ 新主線 vs 17624a1 相異 = 2：app.py verify/selection_pipeline.py 
④   origin/verify/W-G.9-357-k948   origin/wip/s1-endpart 
````

施工樹其後 `git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `4716f202bfd9368d960b942025b2bb8da34c6dd6`。

---

## ④ 工項一：二態之全文

**必過之態**（施工樹·`app.py` ＝ `d8938792ab09e71636dc6916b61432c522c847e5`、`verify/selection_pipeline.py` ＝ `8d38e55013bec51ab81978336fe04e928f5baf98`）：`python verify/probes/probe_WG9358_k948_wiring.py wiring <施工樹之反斜線絕對路徑>` ⇒ **`rc 0`**·`stderr` `0` B。全文（去 CR）：

````text
── 接線（AST·工作樹之 app.py ＋ verify/selection_pipeline.py）──
  ✅ W0 受詞在（缺 []；巢狀（名, 全檔, 段三內）之不符 []）
  ✅ W1 R-2 未處置不變（在 `if not _qs:` True；log_print True；continue True；舊字樣 0（期 0））
  ✅ W2 R-5 所施者恆已通過（_try 之 return True；試算於拷貝 True；state＝ 2／受護 True；_t＝_try(s) True；_try 呼 2（期 2）；_tm＝_try(n/100) True；_best 唯取已通過者 True；return _lo/100 True）
  ✅ W3 R-6 候選與序（alloc_state 一呼 True；err ⇒ raise True；篩 1（期 1）；歸戶 1（期 1）；取 G 唯於 `if _pre:` True；未回 G 之 raise 2／皆於其內 True；序之鍵 True；sort 無 key True）
  ✅ W4 R-6′ 距離之取捨（ROUND_HALF_UP 之式 True；round 之呼 0（期 0）；街廓之全部切片 True）
  ✅ W5 R-7／R-7′ 題一 4（舊 raise 之字樣 0（期 0）；_r4＝None 於合併不過 True；_t14_357 一呼於其 else True；_t14_done 唯 set() True；唯 .add(c) 於頂層先於 if True（方法呼 1）；c 不過 ⇒ 第 5 項 True；半之最大面積 1（期 1）；半之剩下 ⇒ 第 5 項 True）
  ✅ W6 X-3′ 步驟 10 之 R（R 之賦值 ['R = R - _stay', 'R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done']）
  ✅ W7 R-15 剩下之判準（_has357 之式 True；_EPS357 0（期 0）；浮點小量之比較 {}；缺判 {}；分之剩下始入已試之街廓 True）
  ✅ W8 R-10 二處同形（保留之支逐 AST 同 True；含 kept 與 G True；_G 之初值 {}／{}；回傳之鍵 app True／harness True）
  ✅ W9 R-11 公設地調配之 temp（缺句 []；無段三併出 ⇒ 原物件 True；無剩下 ⇒ 去 True）
  ✅ W10 R-12 調配之輸入（X-4（字樣, 全檔, adj_intake）皆 1；_s3_ids 之加 2（期 2）；① 之落點 True；ρ True；不成單位者之分 True；另成單位（公設軌） True；總計之面積 True）
  ✅ W11 R-8 片之鍵（序於 段三併出 之後 True；三支 True）
  ✅ W12 R-3／R-4 步驟 10 之逐片（三 if 之序 True；可拆分 ⇒ _split357 True；整筆不過 ⇒ 第 5 項 True）
── 判別力（每一突變須使其所指之項轉紅）──
  ✅ M1 無受併宗之片改記未成：轉紅 ['W1']（須含 W1）
  ✅ M2 無受併宗之片⛔ continue：轉紅 ['W1']（須含 W1）
  ✅ M3 二分法取未通過之格：轉紅 ['W2']（須含 W2）
  ✅ M4 所施者⛔ 受護：轉紅 ['W2']（須含 W2）
  ✅ M5 格值改 n × 0.01：轉紅 ['W2']（須含 W2）
  ✅ M6 序之鍵以 G 先：轉紅 ['W3']（須含 W3）
  ✅ M7 候選⛔ 扣已試之街廓：轉紅 ['W3']（須含 W3）
  ✅ M8 候選為空亦取 G：轉紅 ['W3']（須含 W3）
  ✅ M9 候選⛔ 扣已併出者：轉紅 ['W3']（須含 W3）
  ✅ M10 距離以 round：轉紅 ['W4']（須含 W4）
  ✅ M11 距離以 Decimal(float)：轉紅 ['W4']（須含 W4）
  ✅ M12 距離以 ROUND_HALF_EVEN：轉紅 ['W4']（須含 W4）
  ✅ M13 R-7 之候選⛔ 入已處置之集：轉紅 ['W5']（須含 W5）
  ✅ M14 R-7 之候選於第 5 項後出集：轉紅 ['W5']（須含 W5）
  ✅ M15 題一 4 之合併不過復停機：轉紅 ['W5']（須含 W5）
  ✅ M16 候選之整筆不過⛔ 第 5 項：轉紅 ['W5']（須含 W5）
  ✅ M17 步驟 10 之 R ⛔ 扣已處置之候選：轉紅 ['W6']（須含 W6）
  ✅ M18 有剩下以 1e-6 判：轉紅 ['W7']（須含 W7）
  ✅ M19 分之剩下以 g < s 判：轉紅 ['W7']（須含 W7）
  ✅ M20 鍵之環以 1e-6 判：轉紅 ['W7', 'W11']（須含 W7）
  ✅ M21 畫面之 G 取他欄：轉紅 ['W8']（須含 W8）
  ✅ M22 harness 之 alloc_state ⛔ 回 G：轉紅 ['W8']（須含 W8）
  ✅ M23 公設地調配之 temp 改原物件：轉紅 ['W9']（須含 W9）
  ✅ M24 面積_m2 ⛔ 乘 ρ：轉紅 ['W9']（須含 W9）
  ✅ M25 一分未併者⛔ 入合併單位：轉紅 ['W10']（須含 W10）
  ✅ M26 已併出之量⛔ 計入原位次配地：轉紅 ['W10']（須含 W10）
  ✅ M27 剩下全收者⛔ 去 段三餘量：轉紅 ['W11']（須含 W11）
  ✅ M28 可拆分者⛔ 經 _split357：轉紅 ['W12']（須含 W12）
  ✅ M29 整筆不過⛔ 第 5 項：轉紅 ['W12']（須含 W12）
⇒ 紅 []；rc 0
````

**必破之態**（`git worktree add --detach C:/Users/admin/wt358P 17624a19c48715bcb1bcfd6af1a851d756d6d473`·其 `app.py` ＝ `e11232a6569bf33c7b2b7f15da989873a06ff28c`、`verify/selection_pipeline.py` ＝ `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`；跑畢 `git worktree remove --force`·`rc 0`）⇒ **`rc 1`**·`stderr` `0` B。全文（去 CR）：

````text
── 接線（AST·工作樹之 app.py ＋ verify/selection_pipeline.py）──
  🔴 W0 受詞在（缺 []；巢狀（名, 全檔, 段三內）之不符 [('_has357', 0, 0), ('_res357', 0, 0), ('_max357', 0, 0), ('_dist357', 0, 0), ('_k951', 0, 0), ('_split357', 0, 0), ('_t14_357', 0, 0)]）
  🔴 W1 R-2 未處置不變（結果='未處置' 2（期 1）；`if not _qs:` 1（期 1））
  🔴 W2 R-5 所施者恆已通過（器拋 KeyError: '_max357'）
  🔴 W3 R-6 候選與序（器拋 KeyError: '_k951'）
  🔴 W4 R-6′ 距離之取捨（器拋 KeyError: '_dist357'）
  🔴 W5 R-7／R-7′ 題一 4（器拋 KeyError: '_t14_357'）
  🔴 W6 X-3′ 步驟 10 之 R（R 之賦值 ['R = R - _stay', 'R = _mem - merged_out - set(_recv_by_blk.values()) - L']）
  🔴 W7 R-15 剩下之判準（器拋 KeyError: '_has357'）
  🔴 W8 R-10 二處同形（保留之支逐 AST 同 True；含 kept 與 G False；_G 之初值 None／None；回傳之鍵 app False／harness False）
  🔴 W9 R-11 公設地調配之 temp（缺句 ['_out = []', '_out.append(tp)', "_rem = float(tp.get('段三餘量', 0) or 0)", "_a = float(tp.get('分攤登記面積_m2', 0) or 0) + float(tp.get('面積_m2', 0) or 0)", '_rho = _rem / _a', '_tp = dict(tp)', "_tp['分攤登記面積_m2'] = float(tp.get('分攤登記面積_m2', 0) or 0) * _rho", "_tp['面積_m2'] = float(tp.get('面積_m2', 0) or 0) * _rho", '_out.append(_tp)', 'return _out']；無段三併出 ⇒ 原物件 False；無剩下 ⇒ 去 False）
  🔴 W10 R-12 調配之輸入（X-4（字樣, 全檔, adj_intake）皆 1；_s3_ids 之加 0（期 2）；① 之落點 False；ρ False；不成單位者之分 False；另成單位（公設軌） False；總計之面積 False）
  🔴 W11 R-8 片之鍵（鍵之環 0（期 1））
  🔴 W12 R-3／R-4 步驟 10 之逐片（三 if 之序 False；可拆分 ⇒ _split357 False；整筆不過 ⇒ 第 5 項 False）
── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──
⇒ 紅 ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12']；rc 1
````

**對拍附錄戊之塊 `T1`／`T2`**（去 CR 及列尾空白後逐列比·原樣）：

````text
O/f17_pass.log: 4315 B·CR 45·sha256 e9b1847c366cbd07e718a14023a4d541fa0ee1cc5b6280ef0004e809af075a90·列 45 vs 塊 45·相異列 0 []
   原始位元組逐位同塊？ False
O/f17_break.log: 2094 B·CR 16·sha256 77113816aaa49bda15ff25c7d98b0f86eaecffcfb22dadba6e039200453b54a9·列 16 vs 塊 16·相異列 0 []
   原始位元組逐位同塊？ False
判別力（擾動一列 ⇒ 相異）：True
````

🔒 原始位元組之差恰為 Windows 下 `stdout` 文字模式所加之 CR：`4315 − 4270 ＝ 45`、`2094 − 2078 ＝ 16`，各等於其列數；單 `§三` 工項一已令比對前去 CR。

---

## ⑤ 六塊之實得與三簿之改前改後

**抽取**（抽取式 ＝ `§五-1` 末·圍欄之逐列索引·原樣）：

````text
單 bytes 90856 sha256 b077096513f486030c0b020cde8a71cb6e6553530f9bfaa73ac142c86669fbae CR 0
SELF_SHA256 所載 564daf683158a9b028b9dc836714063688dde5b1ca30e7da83ff5194565695ac
SELF_SHA256 實算 564daf683158a9b028b9dc836714063688dde5b1ca30e7da83ff5194565695ac（受詞 90778 B）⇒ 相符
判別力（全檔之 sha256 ≠ 所載）：True
圍欄 6：['python', 'markdown', 'markdown', 'markdown', 'text', 'text']
F17（python·開列 233·閉列 843）：36220 B·sha256 f1e1ec505f4c7c34a81bedca53637f8f0960ee6c1193f1113cf5a011dd1d5810·609 列·CR 0
E6（markdown·開列 847·閉列 872）：3410 B·sha256 1f1d8465397786ea4591df92efb8104a2ac10768d8d9e6966e72b074a906ad2e·24 列·CR 0
P12（markdown·開列 876·閉列 898）：4878 B·sha256 0182cedff3dac36c5b8320956cab9746193ae2b096ed71316dd13f820099419c·21 列·CR 0
H2（markdown·開列 902·閉列 951）：3552 B·sha256 241ad43186b99874c98d66f4f579730455f292869cf96861dc196d0f98292458·48 列·CR 0
T1（text·開列 957·閉列 1003）：4270 B·sha256 d154545da58dcd38da690f11a1bdbb5690b923af369a228b17267f9c139fb476·45 列·CR 0
T2（text·開列 1007·閉列 1024）：2078 B·sha256 0e1c2fe4765961dedc19618072a6f4ce91c2fd84a660e6a22325bd88b7be44f6·16 列·CR 0
````

與 `§五-1` 項 `2`〜`6` 逐格相符（`F17` `36220`／`609`；`E6` `3410`／`24`；`P12` `4878`／`21`；`H2` `3552`／`48`；`T1` `4270`／`45`；`T2` `2078`／`16`；`sha256` 皆同）。

**三簿之末端追加**（二進位·原樣）：

````text
docs/reports/W-G.9波_claude.ai側自誤登記.md：期初 1077462 B（期 1077462）·末換行 True·CR 0 ⇒ ✅
   + E6 3410 B ⇒ 期末 1080872 B（期 1080872）·嚴格前綴 True·所增 ＝ 塊逐位 True·CR 0·sha256 1b34049c04a3c17583deaae9b1df500e5071e2348f9e21895053c16c17d69024 ⇒ ✅
CLAUDE.md：期初 303630 B（期 303630）·末換行 True·CR 0 ⇒ ✅
   + P12 4878 B ⇒ 期末 308508 B（期 308508）·嚴格前綴 True·所增 ＝ 塊逐位 True·CR 0·sha256 595c5c10504188a4ca3fbef3c7faa01b70785e6337d4df17a567a81fda900059 ⇒ ✅
docs/reports/W-G.9波_恆常附款登記表.md：期初 62376 B（期 62376）·末換行 True·CR 0 ⇒ ✅
   + H2 3552 B ⇒ 期末 65928 B（期 65928）·嚴格前綴 True·所增 ＝ 塊逐位 True·CR 0·sha256 b123a153f4c9ad831046a7c09ed247c4e73336774392a666690bb5235816efa8 ⇒ ✅
⇒ 不符 0；rc 0
````

---

## ⑥ `§二` 之放行

KL 貼本單之同一訊息，其全文逐字（兩列）：

````text
@"C:\Users\admin\Desktop\land-readjustment-trial\W-G.9-358_輕量單.md"
是
````

⇒ 依 `§二`「**KL 貼本單之同一訊息內**逐字答「是」者，視為工項零′（主線快轉）與工項四（主 checkout 之同步）之放行」，放行成立；所答之【要你判斷】逐字 ＝ 問一之「是否同意將 357 併入主線，並請 CC 同步您本機的程式資料夾（併於 358 辦理）？（是／否）」。快轉於前置皆符之後、以分開之呼叫為之。

---

## ⑦ CC 之自捕與自解

**自捕**
1. **工項零之 `push` 與其生產碼判法之量測置於同一命令塊**——違 `W-G.9-199` 常規補款 `一`（閘之量測與其所守護之動作須分開呼叫）。事後查其量測 ＝ 命中 `0` 行（`grep` `rc 1`），該 `push` 合法、⛔ 須回退。工項一、二之判法與 `push` 已改為分開之呼叫。
2. **對拍腳本以 heredoc 傳入而被倉內 hook（`verify/tools/wg9237_heredoc_guard.py`）攔下**——該次呼叫全未執行（含其後之 `git worktree remove`）；改以 `Write` 落檔 `cmp_t.py` 再以路徑呼叫，`worktree remove` 另一呼叫重跑。⛔ 繞過該 hook。

**本批之自解清單**：`0` 項。

**併記（⛔ 自解·依單或無疑義）**
- 意指占用之量測（`§零-1` 後表）：單未具名其器 ⇒ CC 以倉外之腳本（母體 ＝ `git ls-tree -r 4716f20` 之追蹤檔·裸錨定／B 形／C 形並取·列框）實量，出艙逐字如下，與單之表逐格同：

````text
三軸 (1) 4716f20·(2) 追蹤檔 2728（讀不到 24）·(3) 列框
  自誤 549：裸 86／B 0／C 0
  自誤 550：裸 45／B 0／C 0
  自誤 548：裸 65／B 0／C 9
````

- 宣告框之取號（`python verify/probes/wg9268_gate6_occupancy.py 4716f20 W-G.9-358 W-G.9-357 W-G.9-396`·`rc 0`）：六數與 `§零-1` 表逐格同（受詢 `W-G.9-358` 嚴格／寬式皆 `0`；對照甲 `W-G.9-357` `5`／`11`／`3`·列框 `14`·檔框 `6`·鬆框 `6`／`99`；甲′ `W-G.9-396` 宣告框 `0`、鬆框 `4`／`6`；乙（器內人造·其字樣⛔ 入本檔·`GB-147`）嚴格 `0`、寬式 `D3` `2`〔同 `§零-1` 之具名豁免〕）；母體 ＝ `docs/` `920` 檔（讀不到 `20`）。
- `§零-0` 項 `3`（`probe_WG9321_issuer_anchor.py … 548 547`）⇒ `rc 0`；其「項4′ 四簿·正典框」：自誤 `533`／`548`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `187`／`194`／`[12, 87, 179, 181, 183, 184, 185]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `48`／`51`／`[44, 47]`。
- pre-flight（`python verify/probes/probe_order_preflight.py <來源檔>`·`rc 0`）：🔴 `0`／🟡 `4`／ℹ️ `2`，與 `§五-1` 項 `9` 逐項同；🟡 四項（`P-4` `:71`、`P-4` `:188`、`P-6` `:71`、`P-6` `:892`）採發單側之具名豁免。原樣：

````text
====================================================================================================================
【order pre-flight】W-G.9-358_輕量單.md（90856 B／1026 列）
====================================================================================================================

── 🔴 機械·停機款：0 項 ──

── 🟡 提示·須逐項處置：4 項 ──
  [P-4] :71   🟡 方向性轉引而同段⛔ 未具名座標系：| # | 項 | 值 |
  [P-4] :188  🟡 方向性轉引而同段⛔ 未具名座標系：| 閘 | 受詞 | 期 |
  [P-6] :71   🟡 停機款所繫之數⛔ 未具名實測出處：| # | 項 | 值 |
  [P-6] :892  🟡 停機款所繫之數⛔ 未具名實測出處：🔒 **前節之更新**（⛔ 追改前節一字）：`W-G.9-357` 節序 `1`〜`4` ⇒ ✅（本表序 `1`）；序 `5` ⇒ ✅（本表序 `2`）；序 `6` ⇒ ✅（本批）

── ℹ️ 記錄：2 項 ──
  [P-5] :1026 SELF_SHA256 ✅ 相符（取檔內**最末**一個·受詞 90778 B）｜實算 564daf683158a9b0…／單載 564daf683158a9b0…
  [P-3] :-    `app.py` 之 `def main` 區間（AST 實查）＝ `20014`-`27686`

🛑 `rc` ＝ 紅項數（`P-3`／`P-5` 之機械款）；🟡 提示⛔ 不計入 `rc`（單 `§九（甲）` 逐字）
````

- 工項四之撞檔前置：本單之來源取自**第二處**（主 checkout 之根·路徑 `W-G.9-358_輕量單.md`），⛔ 在快轉將新入之路徑集內（其入倉路徑為 `docs/orders/…`）⇒ 預期⛔ 因本單觸發；實況以工項四之出艙為準。
- 倉內 `verify/tools/wg942_append_audit.py` 之受詞表寫死舊批之段界、⛔ 含本批之受詞形，且本單⛔ 令之 ⇒ ⛔ 用；三簿之嚴格前綴另以附加器自驗（⑤）並於收工閘以 `4716f20` 之 blob 復驗。

---

## ⑧ 各段耗時（本機時刻·`+0800`）

| 段 | 起 | 訖 | 約 |
|---|---|---|---|
| 讀單 | `21:06` | `21:08` | `2` 分 |
| 開工閘（`fetch`〜pre-flight·含 `issuer_anchor`、宣告框、意指占用） | `21:08:26` | `21:10:30` | `2` 分 |
| 工項零′（前置 → 快轉 → 出艙 ①〜④） | `21:10:36` | `21:10:53` | `17` 秒 |
| 工項零 | `21:10:55` | `21:11:16`（`commit`） | `21` 秒 |
| 工項一（寫入 → 必過 `21:11:42`〜`21:13:51` → 必破 → 對拍 → `commit`） | `21:11:20` | `21:14:40` | `3` 分 `20` 秒 |
| 工項二（附加器 → 乾跑 → 實寫 → `commit`） | `21:14:45` | `21:15:29` | `44` 秒 |
| 工項三（本檔） | `21:15:54` | （自指·見對話） | — |
