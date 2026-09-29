# `W-G.9-357R`　執行報告：段三後處理之 `K-9-48` 七項 `3`〜`6` 與 `K-9-51`（剩餘土地之去處）＋ 補令一

> **單** ＝ `docs/orders/W-G.9-357_規格單.md`（原單）＋ `docs/orders/W-G.9-357_補令一.md`（補令一·二者相牴以補令一為準）。
> **側支** `verify/W-G.9-357-k948`（本批新立·起於主線 `17624a19c48715bcb1bcfd6af1a851d756d6d473`）；**主線⛔ 動**。
> **流程** ＝ 規格單（試行之次輪）：生產碼由 CC 依原單 `§三` 與補令一 `§二` 撰寫。
> **首輪之停機** ＝ `docs/reports/W-G.9-357R_工項二停機上呈_題一4候選之再處置.md`（停機款 `5`·已由補令一裁之·見 ⑪）。
> **命令之形**：`<repo>` ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\w-g-9-352-weight-unit-25ec45`（施工樹·detached）；`<O>` ＝ `C:\Users\admin\AppData\Local\Temp\wgO357`（首輪）／`<O>\s1`（補令一）；`<P>` ＝ `C:\Users\admin\AppData\Local\Temp\wgP357`（前置與驗之 `run_all` 同一路徑·各自 `git worktree add --detach` 後跑、跑畢 `git worktree remove --force`）。殼⛔ 設 `WV_`（`[None, None, None]`）；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`。
> **收工閘之實測值出艙於對話**（⛔ 寫入本檔·自指）。

---

## ①　逐 `commit` 之 hash 與工項（本側支之八筆）

| # | `commit` | 工項 | 生產碼判法（`app.py`／`verify/stepg_pipeline.py`／`verify/run_all.py`／`verify/run_verification.py`） |
|---|---|---|---|
| `1` | `84e5134399c31ef0aec76263b53edfc77838dad9` | 原單工項零：本單原封入倉 | 命中 `0` |
| `2` | `7165c229368188ee06c5143141a74adcbadf4a81` | 原單工項一：`F16` 入倉 ＋ `F14p` | 命中 `0` |
| `3` | `47207e94c6a5ac273e588e6c452ca0b4eb4d5122` | 首輪工項二之停機上呈（報告 ＋ 差異檔） | 命中 `0` |
| `4` | `b41f305b82211e2dd13ee75c4e5e06dcfefc7692` | 補令一工項零′：本補令原封入倉 | 命中 `0` |
| `5` | `3816a2f75cb857b5bd25c0119f0a3eabf129227d` | 補令一工項一′：`F16p` | 命中 `0` |
| `6` | `898c31fc6c18db156eb0eafe14366d3fb6f7ae30` | 工項二：生產碼（`app.py`、`verify/selection_pipeline.py`） | 🔴 `app.py`（生產碼·依原單推側支） |
| `7` | `2009a786a1e09d8c7c053a54e4fe50126e336cce` | 工項三：塊 `K4′` 入 `K-6` 典、塊 `P11` 入 `CLAUDE.md` | 命中 `0` |
| `8` | 本報告之 `commit` | 工項四：執行報告入倉 | 命中 `0`（其 hash 出艙於對話） |

首輪之工項二 `f099d04f9df1c33301ba15f3ad776b7099b842f3` ⛔ 推（本地 ref `hold/W-G.9-357-c2`·本批工項二以之為起點再施補令一 `§二`）。

## ②　停機款之三值（原單 `§零-2` 之 `1`〜`11`；`1′`〜`4′` 代原單同號）

| # | 期 | 實 | 判 |
|---|---|---|---|
| `1` | 原單開工：主線 `17624a1`、heads `31`、⛔ 側支、追蹤檔無變動 | `17624a1…`、`31`、`0`、`0` 列 | 未觸 |
| `1′` | 補令一開工：主線 `17624a1`、側支 `47207e9`、heads `32`、追蹤檔無變動 | `17624a1…`、`47207e94…`、`32`、`0` 列；`hold/W-G.9-357-c2` ＝ `f099d04…`（存） | 未觸 |
| `2` | 原單 bytes／`sha256`、來源可得、入倉逐位同 | 來源 ＝ KL 主 checkout 之根；`92860` B·`7055ae0d975a4063b2a58f9bdb78f72ebfd9a98d1078bdbe86d9e681c7b23203`；`SELF_SHA256` 實算 ＝ 單載 ＝ `233e0a31…`；`git cat-file blob` ＝ 來源（`cmp`） | 未觸 |
| `2′` | 補令一 bytes／`sha256`、來源可得、入倉逐位同 | 來源 ＝ KL 主 checkout 之根；`42689` B·`becbb5654493aaf085739ef0ed0103aa75b3846c314fff5f07c304ee98e927bf`·`CR` `0`；`SELF_SHA256` 實算 ＝ 單載 ＝ `bd32922d6a1e29d16869a0efd32002023894bb58934b893100f8062ab21f0a87`（受詞 `42611` B）；`git cat-file blob` ＝ 來源（`cmp`） | 未觸 |
| `3` | 原單四塊 ＝ `§五-1`；`F14p` `--check` 過；施後 `F14` blob ＝ `a78216…` | 皆 ＝（④）；`a78216399a6a5c708cff4d0b9f8bf14fa462f841` | 未觸 |
| `3′` | 補令一二塊 ＝ `§五`；`F16p` `--check` 過；施後 `F16` blob ＝ `c7515d3…`；`P11` ＝ 原單 | 皆 ＝（④）；`c7515d3ecc2f8413899fb18affdee6b3cdec1228`（`38161` B·增 `72`／刪 `1`） | 未觸 |
| `4` ／ `4′` | 前置皆 ＝ 期 | 皆 ＝ 期（③-1） | 未觸 |
| `5` | 規格無涉域上判斷之歧義；⛔ 須改 `§三-3` | 首輪 🛑 **觸發**（題一 `4` 之候選之再處置·停機上呈 `47207e9`）；補令一裁之（`R-7′`／`X-3′`）⇒ 本批未觸 | 首輪觸發·本批未觸 |
| `6` | `V-1′`〜`V-8` ＝ 期；本案配地⛔ 變 | 皆 ＝ 期（③-2） | 未觸 |
| `7` | `push` 唯至側支、⛔ 被拒、⛔ `--force`、主線⛔ 推進 | 八推皆首推即成（新立 `1`＋快轉 `7`）、⛔ `--force`；主線仍 `17624a1…` | 未觸 |
| `8` | 工項三之二檔嚴格前綴 | `K-6` 典 `427954 → 435812`、`CLAUDE.md` `299948 → 303630`；皆嚴格前綴、所增 ＝ 塊（④） | 未觸 |
| `9` | 收工閘 ＝ 期 | 出艙於對話 | — |
| `10` | ⛔ 作「孰為正典」「應改為」之判；⛔ 改塊、器、命令 | ⛔ 作（首輪停機上呈而⛔ 自裁）；諸塊、諸器一字未改 | 未觸 |
| `11` | 新檔⛔ 為 `git check-ignore` 所命中 | 原單、補令一、`F16`、停機報告、其差異檔、本報告 ⇒ 皆 `rc 1` | 未觸 |

## ③　工項二之前置與驗之全部出艙
### ③-1　前置
**首輪**（於原單工項一之端 `7165c22`）：`F16 selftest` ⇒ `rc 1`·末列 `⇒ 紅 ['K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K10′', 'K11', 'K12', 'K13', 'K14', 'K14′', 'K17', 'K18']；rc 1`；`F16 run` ⇒ `rc 1`·末列 `⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`；`F14 selftest` ⇒ `rc 1`·末列 `⇒ 紅 ['T3d', 'T9d', 'T6d']；rc 1`；`k6s3 run` 二退縮 `rc 0`（`<O>\k6s3_pre_35.json`／`_00.json`）；`F8 run` 二退縮 `rc 0`（`<O>\f8_pre_35.log`／`_00.log`）；`run_all`（`<P>` 於 `7165c22`）`rc 1`·`238132` B·`stderr` `0` B（`<O>\runall_pre.log`）。

**補令一**（於工項一′ 之端 `3816a2f`）：

| # | 命令 | 實得 |
|---|---|---|
| `1` | `python verify/probes/probe_WG9357_k948.py selftest <repo>` | `rc 1`；`P0` `25／25`；末列 `⇒ 紅 ['K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K10′', 'K11', 'K12', 'K13', 'K14', 'K14′', 'K17', 'K18', 'K19', 'K20', 'K20′', 'K21', 'K22']；rc 1` |
| `2` | `python verify/probes/probe_WG9357_k948.py run <repo>` | `rc 1`；末列 `⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1` |
| `2′` | `python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `rc 1`；末列 `⇒ 紅 ['T3d', 'T9d', 'T6d']；rc 1` |
| `3` | `git diff --quiet 7165c22 HEAD -- app.py ":(glob)verify/*.py"` | `rc 0`（對照：同式於 `verify/probes/probe_WG9357_k948.py` ⇒ `rc 1`）；首輪之 `<O>` 三組猶在（`k6s3_pre_35.json` `18437` B／`_00.json` `10571` B、`f8_pre_35.log` `2988` B／`_00.log` `3318` B、`runall_pre.log` `238132` B）⇒ **沿用** |

### ③-2　驗（於工項二之 `commit` `898c31f`）

**`V-1′`** `python verify/probes/probe_WG9357_k948.py selftest <repo> > <O>\s1\f16_self_post.log`（`rc 0`）之全文：

````text
── 段三後處理之七項 3〜6 與第 5 項之序（K-9-51）──
  ✅ K1 整批通過 ⇒ 一列、二受併宗各 100、⛔ 新鍵
  ✅ K2 最大面積 60 ＋ 第 5 項併入 Y1（距 0·G 大者）⇒ 全數併出
  ✅ K3 第 5 項依距離：B5 之 Y1 部分 20、Y2 未成 ⇒ B7 之 Z1 收 20
  ✅ K4 餘 15 轉調配：段三併出＋段三部分併出＋段三餘量
  ✅ K5 同距離者 G 大者先 ⇒ Y2 收 40
  ✅ K6 整筆不過 ⇒ 未成；第 5 項整筆併入 Y1；W1 出 build
  ✅ K7 整筆皆不過 ⇒ 轉調配；W1 留 build
  ✅ K8 一分未併 ⇒ 段三餘量 200、⛔ 段三併出
  ✅ K9 0.01 ㎡ 之格：容 60.005 ⇒ 收 60.00
  ✅ K10 a′ 折算：X1 收 120（源 60）、Y1 收 200＋80
  ✅ K10′ a′ 折算之餘：B5／B7 亦滿 ⇒ 段三部分併出 {X1: 60, Y1: 100}（源）、段三餘量 40
  ✅ K11 alloc_state 未回 G ⇒ 停機
  ✅ K12 舊之 段三餘量 於全數併出後去之
  ✅ K13 k6b_stage3_pool_temp：P1 以 15 入（新物件）、X2 去、餘同一物件
  ✅ K14 adj_intake：P1 之餘 15 入合併單位（公設軌）；守恆
  ✅ K14′ adj_intake：一分未併之 P1（200）入合併單位
  ✅ K15 對照：整批通過 ⇒ P1 ⛔ 入公設地調配之 temp；adj_intake 歸原位次配地
  ✅ K16 題一 4 對照：Y1 連同其半併入 X1 通過 ⇒ 一列
  ✅ K17 題一 4 不過 ⇒ Y1 整筆經第 5 項入 Z1；其半 X1 收 20、餘 20 入 Z1（⛔ 停機）
  ✅ K18 題一 4 之餘 10 轉調配：X3 段三部分併出 {X1: 60, Z1: 10}、段三餘量 10
  ✅ K19 題一 4 之 Y1 轉調配即終局 ⇒ Y1 恰三列、轉調配恰一列；X3 之餘 20 入 Z1
  ✅ K20 差 0.00003（四位小數為 0）⇒ 視為全收：二列皆成、⛔ 第 5 項、⛔ 餘量之鍵
  ✅ K20′ 同上之調配之輸入：P1 歸原位次配地、⛔ 入合併單位（對照）
  ✅ K21 距離 0.125 四捨五入 ⇒ 0.13 ＝ Z9 ⇒ G 大者 Z9 先；紀錄之距離 ＝ 0.13
  ✅ K22 候選為空 ⇒ alloc_state 未回 G 亦⛔ 停機：W1 未成 ⇒ 轉調配
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 25／25
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9357_k948.py run <repo> > <O>\s1\f16_run_post.log`（`rc 0`）之全文：

````text
  ✅ R1@3.5：保留集 harness ＝ 畫面 True（28 宗）；G 之鍵 ＝ 保留集 True；逐宗差 max 0.0（≤ 0.01）True
  ✅ R2@3.5：段三紀錄 18 列 ＝ 開工態 True；新鍵之片 []；新結果 []
  ✅ R1@0.0：保留集 harness ＝ 畫面 True（29 宗）；G 之鍵 ＝ 保留集 True；逐宗差 max 0.0（≤ 0.01）True
  ✅ R2@0.0：段三紀錄 0 列 ＝ 開工態 True；新鍵之片 []；新結果 []
⇒ 紅 []；rc 0
````

**`V-2`** `probe_WG9344_k6s3.py run` 二退縮皆 `rc 0`；`cmp`（前置之 json vs 驗之 json）二份皆 `rc 0`：

````text
── 3.5
相異 0 項 ⇒ ✅ 同
── 0.0
相異 0 項 ⇒ ✅ 同
````

**`V-3`** `probe_WG9349_k9296.py run` 二退縮皆 `rc 0`·末列 `⇒ 紅 []；rc 0`／`⇒ 紅 []；rc 0`；與前置 `4` 之 `diff` 二份皆 `rc 0`、`0`／`0` B（空）。

**`V-4`** `probe_WG9345_screen.py parity` 二退縮皆 `rc 0`；末十列：

````text
── 3.5
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（57／57）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
── 0.0
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（61／61）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

**`V-5`** `<P>` 於 `898c31f`：`python verify/run_all.py > <O>\s1\runall_post.log`（`rc 1`·`238132` B·`stderr` `0` B）；`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\s1\runall_post.log`（`rc 0`）之全文：

````text
【runall】項 64／64·PASS 28 → 28·FAIL 36 → 36
  相異項 0；其餘 64 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／36 → 22／36；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
````

`diff <O>\runall_pre.log <O>\s1\runall_post.log` ⇒ `rc 0`、全文 ＝ 空（`0` B）。

**`V-6`** 生產碼 `34` 檔對工項一′ 之端 `3816a2f`（倉外工具 `v6.py`·對照：二態同 ⇒ `0`／`0`）：

````text
生產碼母體：3816a2f 34 檔／898c31f 34 檔；同集 True
生產碼相異 2：['app.py', 'verify/selection_pipeline.py']
  app.py：e11232a6569bf33c7b2b7f15da989873a06ff28c → d8938792ab09e71636dc6916b61432c522c847e5；numstat（增 刪）['297', '27']
  verify/selection_pipeline.py：8bb4592047a74cd7efc502dcdef1efb8b5a0c966 → 8d38e55013bec51ab81978336fe04e928f5baf98；numstat（增 刪）['23', '4']
verify/ 全檔（聯集 1782）相異 1：['verify/selection_pipeline.py']
````

**`V-7`** 原單 `§四-3` 閘 `8`〜`22` 之諸器（於 `898c31f`·`34` 命令·三流並行〔諸器⛔ 寫施工樹·先證〕·皆 `rc 0`）：

| 閘 | 命令 | `rc` | 秒 | 末列（逐字） |
|---|---|---|---|---|
| `8` | `f16_selftest` | `rc 0` | 4s | `⇒ 紅 []；rc 0` |
| `8` | `f16_run` | `rc 0` | 166s | `⇒ 紅 []；rc 0` |
| `9` | `wfns_ast` | `rc 0` | 3s | `引擎經 ns 取用之相異名 ＝ 47` |
| `10` | `main_synth` | `rc 0` | 23s | `紅項 [] 器紅 0` |
| `11` | `synth9341` | `rc 0` | 4s | `ε ＝ 0.0002｜rc 0` |
| `12` | `failclosed` | `rc 0` | 188s | `⇒ 紅 []；rc 0` |
| `13` | `harvest_key` | `rc 0` | 6s | `⇒ 紅 []；rc 0` |
| `13` | `k9296_selftest` | `rc 0` | 3s | `⇒ 紅 []；rc 0` |
| `13` | `k9296_wiring` | `rc 0` | 11s | `⇒ 紅 []；rc 0` |
| `14` | `fr_selftest` | `rc 0` | 20s | `⇒ 紅 []；rc 0` |
| `14` | `fr_wiring` | `rc 0` | 34s | `⇒ 紅 []；rc 0` |
| `14` | `fr_run` | `rc 0` | 4s | `⇒ 紅 []；rc 0` |
| `15` | `in_selftest` | `rc 0` | 14s | `⇒ 紅 []；rc 0` |
| `15` | `in_wiring` | `rc 0` | 34s | `⇒ 紅 []；rc 0` |
| `15` | `in_run` | `rc 0` | 124s | `⇒ 紅 []；rc 0` |
| `16` | `eb_selftest` | `rc 0` | 21s | `⇒ 紅 []；rc 0` |
| `16` | `eb_wiring` | `rc 0` | 78s | `⇒ 紅 []；rc 0` |
| `16` | `eb_run` | `rc 0` | 125s | `⇒ 紅 []；rc 0` |
| `17` | `em_selftest` | `rc 0` | 20s | `⇒ 紅 []；rc 0` |
| `17` | `em_wiring` | `rc 0` | 54s | `⇒ 紅 []；rc 0` |
| `17` | `em_run` | `rc 0` | 622s | `⇒ 紅 []；rc 0` |
| `18` | `ec_selftest` | `rc 0` | 37s | `⇒ 紅 []；rc 0` |
| `18` | `ec_wiring` | `rc 0` | 33s | `⇒ 紅 []；rc 0` |
| `18` | `ec_run` | `rc 0` | 567s | `⇒ 紅 []；rc 0` |
| `19` | `sm_selftest` | `rc 0` | 4s | `⇒ 紅 []；rc 0` |
| `19` | `sm_run` | `rc 0` | 902s | `⇒ 紅 []；rc 0` |
| `20` | `smw_wiring` | `rc 0` | 42s | `⇒ 紅 []；rc 0` |
| `21` | `parity35` | `rc 0` | 167s | `⇒ rc 0（不符 0 項）` |
| `21` | `parity00` | `rc 0` | 62s | `⇒ rc 0（不符 0 項）` |
| `21` | `f4_wiring` | `rc 0` | 28s | `⇒ rc 0（不符 0·器紅 0）` |
| `21` | `f4_selftest` | `rc 0` | 0s | `selftest 10/10 ⇒ ✅` |
| `22` | `pooltemp_run` | `rc 0` | 71s | `⇒ rc 0` |
| `22` | `pooltemp_self` | `rc 0` | 0s | `selftest 13/13 ⇒ ✅` |
| `22` | `k6s3_selftest` | `rc 0` | 0s | `selftest 9/9 ⇒ ✅` |

閘之期之逐項對照：閘 `9` 全出艙 ＝ `_WF_NS_NAMES 成員數（AST）＝ 48 ／相異 ＝ 48`、`引擎經 ns 取用之相異名 ＝ 47` ✅；閘 `10` 含 `ℹ️ app 側宿主 ＝ f3_screen_stepg_run` ✅；閘 `15` 之 `selftest` 突變 `M1`〜`M4` 皆「轉紅」✅（`X-4`）；閘 `21` 之 `parity` ＝ `V-4` 之數 ✅。驗畢施工樹 `git status --porcelain` ＝ `0` 列。

**`V-8`** `git diff f099d04 898c31f -- app.py verify/selection_pipeline.py`（`<O>\s1\delta_c2.diff`·`8935` B·`154` 列·`CR` `0`·`sha256` `78b008f9241164c266bda334cab56cf1fb75cab32dca6bd530dce06fe9a6d3a5`）：`@@` `13` 段·皆於 `k6b_stage3_run`·逐段之歸屬見 ⑦-2；`verify/selection_pipeline.py` 無差（與首輪逐位同）；全文見 ⑩。

## ④　塊之實得與二檔之改前改後 bytes

| 塊 | 出處之圍欄（1 起之列） | bytes | 列 | `sha256` | 用 |
|---|---|---|---|---|---|
| `F16` | 原單 `254`–`802` | `32592` | `549` | `5e321d797997c70d465905dbfd4c813b978207b3de9412dee47c8e97ef6fe8ed` | 新檔 `verify/probes/probe_WG9357_k948.py`（blob `c77be87a1b2a0d094cb5ff1aee4edad43ad2c726`） |
| `F14p` | 原單 `808`–`830` | `1819` | `23` | `95d5614e0833c29b5c3f580d2b355e4e37ad9de9206b6af65ca8cdf87b9ee62c` | `verify/probes/probe_WG9355_screenmerge.py` `3648cd6… → a78216…`（`35946 → 36045` B·增 `3`／刪 `2`） |
| `K4` | 原單 `836`–`898` | `7291` | `63` | `e9eee06922ca6c1f0f3a81f545dea7d92d6eb9766e5c1b4dffa26afec38ddfbf` | ⛔ 附（補令一：由 `K4′` 代之） |
| `P11` | 原單 `904`–`925` | `3682` | `22` | `a23f8d3b80aa20ae423c8abdc60577dd817725dfcef96cc10705463005ddc640` | 附 `CLAUDE.md` 之末 |
| `F16p` | 補令一 `195`–`292` | `7537` | `98` | `ab40643d4958bead8c8fe3460bc1cc8c9ef3aea73a5bbc4e8f6943d51d540f52` | `verify/probes/probe_WG9357_k948.py` `c77be87… → c7515d3…`（`32592 → 38161` B·增 `72`／刪 `1`） |
| `K4′` | 補令一 `298`–`360` | `7858` | `63` | `313e6f932c8ed662a66c56a9cf655ca141a411b9aec8562d984679da9207e2a9` | 附 `K-6` 典之末 |

抽取 ＝ 倉外工具 `order_check.py`／`supp_check.py`（圍欄開列之次列至閉列之前一列，`\n` 相接、末附 `\n`、UTF-8）。

| 檔 | 改前 | 改後 | 增／刪 |
|---|---|---|---|
| `app.py`（blob） | `e11232a6569bf33c7b2b7f15da989873a06ff28c`·`1601188` B | `d8938792ab09e71636dc6916b61432c522c847e5`·`1617196` B | `297`／`27` |
| `verify/selection_pipeline.py`（blob） | `8bb4592047a74cd7efc502dcdef1efb8b5a0c966`·`47216` B | `8d38e55013bec51ab81978336fe04e928f5baf98`·`48339` B | `23`／`4` |
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `427954` B | `435812` B（嚴格前綴·所增 ＝ `K4′`） | `63`／`0` |
| `CLAUDE.md` | `299948` B | `303630` B（嚴格前綴·所增 ＝ `P11`） | `22`／`0` |

## ⑤　推送之目標與推後之 `git ls-remote --heads origin`

推送一律 `git push origin HEAD:verify/W-G.9-357-k948`（首次 `HEAD:refs/heads/verify/W-G.9-357-k948` 新立），皆首推即成、⛔ `--force`：
`84e5134`（新立）→ `7165c22` → `47207e9` → `b41f305` → `3816a2f` → `898c31f` → `2009a78` → 本報告之 `commit`（其推後之實查出艙於對話）。

工項三推後之 `git ls-remote --heads origin`（`32` 列·逐字）：

````text
a18bb57064a308c8eddaa8b6d2a354681a67b844	refs/heads/claude/wg9-95z-v3-resume-hgpzfs
6cb77b7f0c08e2edf62f8e9cd239efa774a98d95	refs/heads/main
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
2009a786a1e09d8c7c053a54e4fe50126e336cce	refs/heads/verify/W-G.9-357-k948
886645475b60f790c06d52333501e917596c28be	refs/heads/wip/W-G.4-S0b-S0c
c286a79cc6a699c57c7763306c4beae9ef7b60a3	refs/heads/wip/W-G.9-318-preserve
17624a19c48715bcb1bcfd6af1a851d756d6d473	refs/heads/wip/s1-endpart
````

## ⑥　CC 之自捕與自解

### ⑥-1　自捕（皆出艙前）

1. **`cp --preserve=none`**（首輪工項零）：GNU `cp` 不受之引數而失敗；同一命令列之 `git add`／`commit` 皆未成（`HEAD` 仍 `17624a1`）；改以 `cp` 重辦，`cmp` 與 `git cat-file blob` 二度證其逐位相同。
2. **`run_all` 之重導形**（首輪前置 `5`）：首次啟動誤以 `> … 2>&1`；即以 `TaskStop` 止之、以 `Win32_Process` 查無殘留之 `python`、`git worktree remove --force` 後重立 `<P>`，改以 `> runall_pre.log 2> runall_pre.stderr` 重跑（`stderr` `0` B）。其後前置與驗之 `run_all` 一律同形。
3. **heredoc**：倉之 PreToolUse 閘（`wg9237_heredoc_guard`）擋下 heredoc；改為倉外工具檔（`C:\Users\admin\AppData\Local\Temp\wgT357\`·⛔ 入倉）。
4. **獨立 reviewer 之發現 ⇒ 停機款 `5`**（首輪·工項二之驗後、推前）：`R-7` 轉調配之候選於步驟 `10` 再處置——CC 以 `F16` 之 `_go4` 復現，⛔ 自裁，停機上呈（`47207e9`·`docs/reports/W-G.9-357R_工項二停機上呈_題一4候選之再處置.md`）；首輪之工項二 `f099d04` ⛔ 推。發單側以補令一裁之（⑪）。
5. **閘之計數**：首輪對話中曾稱閘 `8`〜`22` 為「`33` 命令」，實為 **`34`**（`§四-3` 之各閘之子命令之和）；報告與落檔皆以 `34` 載。

### ⑥-2　常規二之互斥（首輪·`§六-2`）

`R-8`（`1e-6` 門檻 ＋ 四位小數）與 `R-11`／`R-12`（`＞ 0`）之縫——首輪取保守項（`＞ 0` 為有剩下）並回報；補令一裁二以 `R-15` 一之（有剩下 ⇔ `round(r, 4) ＞ 0`），首輪所取之 `R-11`／`R-12` 之碼由之所涵、⛔ 改（`K20′` 綠）。

### ⑥-3　本批之自解清單（`作業常規之追加五`）

本批⛔ 自解任何疑義。`§三-4` 末之實作細節（⑦-3）係單所授權由 CC 定之者；pre-flight 之 🟡 項（原單 `P-1 :100`、`P-4 :65`／`:174`／`:198`；補令一 `P-4 :138`）皆為發單側所具名豁免者，逐項與實跑之出艙相符。


## ⑦　設計說明（原單 `§三-5` ＋ 補令一 `§二` 五款）

🔒 **態** ＝ 工項二之 `commit` `898c31fc6c18db156eb0eafe14366d3fb6f7ae30`（`app.py` blob `d8938792ab09e71636dc6916b61432c522c847e5`·`1617196` B；`verify/selection_pipeline.py` blob `8d38e55013bec51ab81978336fe04e928f5baf98`·`48339` B）。下開「字樣」皆可於該態 `grep -n -F` 定位（⛔ 以行號為錨）。

### ⑦-1　逐 `R-1`〜`R-14` 之落點（原單）

| # | 落於 | 字樣錨 | 說明 |
|---|---|---|---|
| `R-1` | `k6b_stage3_run` 步驟 10 之逐片之環 | `if not _batch_ok and not _whole:` | 整批通過 ⇒ 此條件恆偽，其後 `if _batch_ok:` 起之碼與現碼逐字同；末之鍵之處置於整批通過之片只 `pop` 二新鍵（入段三時⛔ 帶之者即無作用）⇒ 紀錄之列、`merged_out`、受併宗之 `面積_m2`、片之鍵逐位同現碼（實證 ＝ `V-2`〜`V-5`） |
| `R-2` | 同上 | `未處置：二半片皆不鄰 B 內街廓` | `_plan` 之組成與其序一字未動；`if not _qs:` 之「未處置」列與其 `log_print` 一字未動；整批不過者依 `_plan` 之序逐片交 `R-3`／`R-4` |
| `R-3` | 同上之 `else` | `_k951(x, _a357(x), {_blk_of[r] for r, _ in _qs}, True)` | 整筆之試與其「成」「未成」之列同現碼；「未成」之後接第 5 項（整筆·`F` ＝ 受併宗之街廓）。現碼之「未處置：「不影響原位次」不過」之分支因 `R-4` 而不可達 ⇒ 刪（⛔ 留死碼） |
| `R-4` | 新輔助 `_split357` | `def _split357(x, qs, lvl, extra):` | 逐分（`_plan` 之序）：`s_i ＝ q_i ÷ k(x, r_i)`、`g_i ＝ _max357(…)`、逐分一列；有剩下(`s_i − g_i`)（`R-15`）⇒ 其街廓入 `F`、差累入剩下；剩下有剩下 ⇒ `_k951`（可拆分）；`_left[x]` ＝ 其後之剩下 |
| `R-5` | 新輔助 `_max357` | `def _max357(x, recv, s):` | 先試 `s`（受檢 ＝ `r` 之街廓、被整筆併出者 ＝ 空）；不過 ⇒ `N ＝ max{n : n/100 < s}`，於 `[0, N]` 以二分法求通過之最大 `n`（`n ＝ 0` 視為通過·⛔ 試）；所施者 ＝ 最末一次通過之試算態本身（`state = _best`） |
| `R-6` | 新輔助 `_k951`、`_dist357` | `def _k951(x, s, F, whole):` | ① 現態 `alloc_state`（`err` ⇒ 停機）；② 候選 ＝ `kept` 中同歸戶者，扣 `x`、`merged_out`、`F` 內街廓、不在 `state["by"]` 者（`_pre`）；③ 序 ＝ `(距離, −G, 暫編地號)`；④ 整筆：依序整筆試、首一通過即施並入 `merged_out`；可拆分：依序 `_max357`，⛔ 有剩下即止；⑤ 有剩下 ⇒ 「轉調配」之列（⛔ `raise`·⛔ `log_print`） |
| `R-7` | `_ct_cross` 之題一 `4` 之 `else` 分支、新輔助 `_t14_357` | `_t14_357(W, Lo, X, _frac[Lo['k']], _frac[W['k']], _note)` | 合併之試一字未動；通過 ⇒ 現碼之諸敘述（縮排一層）與「題一 4·成」之列逐字同；不過 ⇒ `_r4 ＝ None`，於原「題一 4·成」之列之處呼叫 `_t14_357`：① `c` 整筆試併入 `w`，不過 ⇒ 第 5 項（整筆·`F ＝ {w 之街廓}`）；② `X` 依暫編地號之序、`f ＞ 0` 者：`a(x) × f` 以 `_max357` 併入 `w`，其差有剩下 ⇒ 第 5 項。競合之二列、`merged_out.update(X)`、`return [Lo]` 同現碼 |
| `R-8` | `k6b_stage3_run` 之末 | `for _pid in sorted(set(marks) \| set(_left)):` | `段三併出` 之寫法同現碼；`_got357` 於 `g > 0` 時記 `marks` 與 `_part`；`R-7` 之已取得之一端先前所併之半（`a(x) × frac_w`）入 `_part`；有剩下 ∧ 有併入 ⇒ `段三部分併出` ＋ `段三餘量`；有剩下 ∧ 無併入 ⇒ 去 `段三部分併出`、`段三餘量 ＝ a(x)`；`marks` 內而⛔ 有剩下 ⇒ 去二鍵；本趟未觸者⛔ 動 |
| `R-9` | 各輔助之 `_row` | `層級='後處理·第5項'`／`結果='轉調配'`／`層級='題一 4'` | ① 逐分之列：`受併宗` ＝ `r_i`、`切分併入` ＝ `併入量` ＝ `{r_i: round(k × g_i, 4)}`（`g_i ＝ 0` ⇒ `{}`）、`整筆併入 ＝ []`、`全量 ＝ round(q_i, 4)`，另附該片於 `_plan` 之 `鄰接街廓`（`鄰接街廓_半片`）；② 第 5 項之列另鍵 `距離` 與 `G`；③ 轉調配之列 `餘量`；④ `R-7` 之列 `街廓`／`端` ＝ 未取得之一端，另附 `競合`。列之序 ＝ 事件之序 |
| `R-10` | `k6b_screen_callbacks`（`app.py`）與 `_k6b_callbacks`（`verify/selection_pipeline.py`）之 `alloc_state` | `_G[_pid] = float(_r.get('G(㎡)', 0) or 0)` | 於同一 `驗_總判 ＝ 保留` 之分支內與 `kept` 同步寫入 ⇒ `G` 之鍵集恆 ＝ `kept` 諸值之聯集（含 `err` 非空者）；`kept`／`bad_pools`／`err` 之計算一字未動；`k6b_stage3_run` 之 docstring 之約定增 `G` |
| `R-11` | `k6b_stage3_pool_temp` | `_rho = _rem / _a` | 無 `段三併出` ⇒ 原物件；有 `段三併出` 而 `段三餘量` 非正（或無）⇒ 去之；有 `段三併出` 且 `段三餘量 ＞ 0` ⇒ 淺拷貝、二面積欄各乘 `ρ`；回新 list |
| `R-12` | `adj_intake` | `_s3_ids = set()` | ① 帶 `段三併出` 且 `段三餘量 ＞ 0` ⇒ `類 ＝ ADJ_DISP_COMMON_UNIT`、`原有面積 ＝ 分攤 × ρ`、`段三併出面積 ＝ 分攤 × (1 − ρ)`；② 帶 `段三餘量` 而無 `段三併出` ⇒ `類 ＝ ADJ_DISP_COMMON_UNIT`；③ 依現碼成單位者（`if _pool or (_cm and not _al):` 一字未動）⇒ 併入；不成單位者（`elif _cm:`）⇒ ①② 之列另成一單位（公設軌）、其餘依現碼入步 4；④ `段三併出面積` 加入 `ADJ_DISP_ALLOC` 之面積。無 ①② 者逐位同現碼 |
| `R-13` | — | — | 本案之段三後處理皆整批通過 ⇒ 實證 ＝ `V-2`〜`V-5` |
| `R-14` | — | — | 畫面路徑經 `k6b_stage3_run`／`k6b_screen_callbacks` 同受之；`def main` ⛔ 動；實證 ＝ `V-4` 與閘 `10`／`20`／`21` |

### ⑦-2　補令一 `§二` 五款之落點（＝ `V-8` 之差異 `13` 段之歸屬）

| 款 | 字樣錨 | `V-8` 之段（`@@` 之序） |
|---|---|---|
| `R-7′` | `_t14_done = set()`（宣告）；`_t14_done.add(c)`（唯 `_t14_357` 內·`R-7` 之路徑唯一呼叫者） | 第 `1`、`10` 段 |
| `X-3′` | `R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done` | 第 `12` 段（`R = R - _stay` 一字未動） |
| `R-15` | `def _has357(r):`（`return round(float(r), 4) > 0`）；其用處 ＝ `_res357`（③）、`_k951` 之 `if not _has357(_rem):`（②）與 `if _has357(_rem):`（⑤）、`_split357` 之 `if _has357(_s - _g):` 與 `if _has357(_rem):`（①）、`_t14_357` 之 `if _has357(_rem):`（④）、末之 `if _has357(_rm) and _pid in marks:`（⑤）；`_EPS357` ＝ 全檔 `0` 處（廢·⛔ 留死碼） | 第 `1`、`2`、`7`、`8`、`9`、`11`、`13` 段 |
| `R-6′` ③ | `return float(_Dec357(repr(_d)).quantize(_Dec357('0.01'), rounding=_HU357))` | 第 `3`、`4` 段 |
| `R-6′` ②③ | `_pre.append((_b, _p))`；`if _pre:` 之內始取 `G` | 第 `5`、`6` 段 |
| `R-5′` | `return _lo / 100.0`（首輪已為 `n / 100`） | ⛔ 改 |

`R-11`／`R-12` 之碼⛔ 改（補令一 `R-15` 之末：「`段三餘量 ＞ 0` 與『有剩下』同義」）；`verify/selection_pipeline.py` 與首輪逐位同（`8d38e55…`）。

### ⑦-3　實作細節之選擇及其由（原單 `§三-4` 末）

1. **輔助之切分與命名**：`_has357`／`_a357`／`_k357`／`_res357`／`_got357`／`_max357`／`_dist357`／`_k951`／`_split357`／`_t14_357` 與集 `_t14_done`，皆定義於 `_k950_rows` 之後、步驟 `1`〜`8` 之環之前（`X-2`：`_ct_cross` 呼叫之）。
2. **二分法**：整數 `n ∈ [0, N]`，`_lo` 唯於試算通過後前移，並保存該次之試算態 `_best`，終了以之為現態（所施者即被驗之態本身）；`N` 以 `int(s × 100)` 起算、二 `while` 校正至 `N/100 < s ≤ (N+1)/100`。
3. **`R-7` 之執行位置**：原「題一 4·成」之列之處（`_ct_log` 二列之後）；紀錄之列序與通過之路徑一致。
4. **非域上之防呆（loud）**：`a(x) ≤ 0`、`k ≤ 0`、候選宗之街廓於段三之輸入中無切片（訊息載「域上之未定·停機上呈」）、`x` 無幾何、`adj_intake` 中帶 `段三餘量` 之片不在共同負擔之街廓、`pool_temp` 中帶 `段三餘量` 之片之面積 `≤ 0` ⇒ 皆 `RuntimeError`（補令一裁四：`a(x) ≤ 0` 准）。
5. **`R-6′` ③ 之 `decimal`**：於 `_dist357` 內以別名匯入（`_Dec357`／`_HU357`·⛔ 動模組層之匯入）。
6. **`RuntimeError` 之措辭**：一律 `🔴 [K-6-B 段三 後處理…]` 起首，`R-6` 之二處皆含「未回 G」。

### ⑦-4　原單 `§三-3` 各款之自查（補令一 `X-3′` 所開之一處除外）

| 款 | 判 | 據 |
|---|---|---|
| `X-1` | 未觸 | 二檔差異之諸 `@@` 所屬之函式 ＝ `adj_intake`／`k6b_stage3_run`／`k6b_screen_callbacks`（`app.py`）、`k6b_stage3_pool_temp`／`_k6b_callbacks`（`verify/selection_pipeline.py`）；閘 `10`／`20`／`21` 綠 |
| `X-2` | 未觸 | 步驟 `1`〜`9` 與所列諸輔助一字未動；唯題一 `4` 之 `else` 分支（`raise` 改為 `if _noaff(…):…else:`）與「題一 4·成」之列之記法改之；新輔助定義於步驟 `1`〜`8` 之環之前；`F13` 之 `W4`（`_road_halves(x, '` ＝ `2`、`_split(` ＝ `1`）、`W5`（`_recv_of(` ＝ `7`）、`M6` 錨 ＝ `1` 皆同；閘 `17`／`18` 綠 |
| `X-3` | 未觸（`X-3′` 之一處外） | `_plan`／`_cls`／`_recv_of`／`_stay`／`B`／各停機、`_doable`／`_chk_blks`／`_removed`／`_batch_ok` 一字未動；`R = _mem - …` 之一式依 `X-3′` 另扣 `_t14_done`；`R = R - _stay` 一字未動 |
| `X-4` | 未觸 | 四字樣於 `adj_intake` 與全檔各恰 `1`；閘 `15` 之 `selftest` 突變 `M1`〜`M4` 皆轉紅 |
| `X-5` | 未觸 | `_WF_NS_NAMES` 不在差異內；閘 `9` ＝ `48`／`48`／`47` |
| `X-6` | 未觸 | `end_block_*`／`k6_merge_groups`／`solve_G_binary`／`_solve_G_one`／`k929_6_*`／`f3_screen_*`／`k6b_stage3_selected`／`adj_intake_rows` 皆不在差異內；`verify/` 唯 `selection_pipeline.py` 之二處（`V-6`） |
| `X-7` | 未觸 | 五函式之字串常數以 `CASE_LIT_RE` 掃之皆 `[]`（判別力：`'R4'`／`'628-45(1)'` 皆命中） |

## ⑧　二檔之全文差異（原單 `§三-5`·`git diff 3816a2f 898c31f -- app.py verify/selection_pipeline.py`·`30517` B·`482` 列·`CR` `0`·`sha256` `f0a5040816ed7e758e0875ae0058a6ab99240d381e00996d49bc3eaaafba2b84`）

````diff
diff --git a/app.py b/app.py
index e11232a..d893879 100644
--- a/app.py
+++ b/app.py
@@ -11520,6 +11520,7 @@ def adj_intake(temp_parcels, build_final, g_rows, dropped, own_map, burden_by_bl
     if _stray:
         raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] G 值列或不配地紀錄之 {_stray} 不在 build ⇒ 停機")
     _rows = []
+    _s3_ids = set()     # 🆕 `W-G.9-357`：段三後處理之剩下（部分併出之餘量·一分未併者）之切片——恆入其歸戶之合併單位
     for t in _real:
         _k, _bl = _pid(t), str(t.get('所屬街廓', ''))
         if _bl not in (burden_by_block or {}) or not (burden_by_block or {}).get(_bl):
@@ -11531,12 +11532,29 @@ def adj_intake(temp_parcels, build_final, g_rows, dropped, own_map, burden_by_bl
         _row = {'暫編地號': _k, '原地號': str(t.get('原地號', '')), '歸戶': _g, '所屬街廓': _bl,
                 '負擔屬性': _bt, '原有面積': _a(t), '重劃前地價區段': str(t.get('重劃前地價區段', '') or ''),
                 '所屬單元': '', '應分配面積': None, '不配地由': '', '配地街廓': []}
+        _rem3 = float(t.get('段三餘量', 0) or 0) if '段三餘量' in t else None
+        if _rem3 is not None and _bt != ADJ_BURDEN_COMMON:
+            raise RuntimeError(f"🔴 [W-G.9-357 調配之輸入] 帶段三餘量之 {_k!r} 位於負擔屬性 {_bt!r} 之街廓 {_bl!r}"
+                               "（段三之剩下唯可拆分之共同負擔用地有之）⇒ 停機")
         if '段三併出' in t:
             _rcv = [str(_x) for _x in (t.get('段三併出') or [])]
             if not _rcv or any(_x not in _alloc for _x in _rcv):
                 raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 段三所併出之 {_k!r} 之受併宗 {_rcv} 未配地 ⇒ 停機")
-            _row.update(類=ADJ_DISP_ALLOC, 所屬單元='段三併入 ' + '、'.join(_rcv),
-                        配地街廓=sorted({str((_by.get(_x) or {}).get('所屬街廓', '')) for _x in _rcv}))
+            if _rem3 is not None and _rem3 > 0:
+                # 🆕 `W-G.9-357`（`K-9-48` 七項 3〜6）：部分併出 ⇒ 其餘量入合併單位；已併出之量計入原位次配地
+                _den = _a(t) + float(t.get('面積_m2', 0) or 0)
+                if not _den > 0:
+                    raise RuntimeError(f"🔴 [W-G.9-357 調配之輸入] 帶段三餘量之 {_k!r} 之面積 {_den!r} ≤ 0 ⇒ 停機")
+                _rho = _rem3 / _den
+                _row.update(類=ADJ_DISP_COMMON_UNIT, 原有面積=_a(t) * _rho, 段三併出面積=_a(t) * (1.0 - _rho))
+                _s3_ids.add(_k)
+            else:
+                _row.update(類=ADJ_DISP_ALLOC, 所屬單元='段三併入 ' + '、'.join(_rcv),
+                            配地街廓=sorted({str((_by.get(_x) or {}).get('所屬街廓', '')) for _x in _rcv}))
+        elif _rem3 is not None:
+            # 🆕 `W-G.9-357`：一分未併之共同負擔用地 ⇒ 入合併單位（`K-9-45`）
+            _row['類'] = ADJ_DISP_COMMON_UNIT
+            _s3_ids.add(_k)
         elif _bt == ADJ_BURDEN_BUILD:
             if _k not in _unit_of:
                 raise RuntimeError(f"🔴 [W-G.9-351 調配之輸入] 可建築土地上之切片 {_k!r} 不在 build ⇒ 停機")
@@ -11591,13 +11609,27 @@ def adj_intake(temp_parcels, build_final, g_rows, dropped, own_map, burden_by_bl
                            '原有面積合計': sum(_r['原有面積'] for _r in _pool + _cm),
                            '同歸戶原位次配地之街廓': _al_blk})
         elif _cm:
-            _step4.append({'歸戶': _g, '共同負擔用地': _cm, '原有面積合計': sum(_r['原有面積'] for _r in _cm),
-                           '同歸戶原位次配地之街廓': _al_blk})
+            # 🆕 `W-G.9-357`：段三之剩下之切片恆入其歸戶之合併單位（`K-9-45`）——依現碼不成單位者另成一單位（公設軌）；
+            #   其餘之共同負擔用地之去處（步 4）同前
+            _s3 = [_r for _r in _cm if _r['暫編地號'] in _s3_ids]
+            _cm = [_r for _r in _cm if _r['暫編地號'] not in _s3_ids]
+            if _s3:
+                _units.append({'歸戶': _g, '軌': ADJ_TRACK_PUBLIC, '原街廓': None, '原街廓之據': {},
+                               '建築街廓內不能分配': [], '共同負擔用地': _s3,
+                               '原有面積合計': sum(_r['原有面積'] for _r in _s3),
+                               '同歸戶原位次配地之街廓': _al_blk})
+            if _cm:
+                _step4.append({'歸戶': _g, '共同負擔用地': _cm, '原有面積合計': sum(_r['原有面積'] for _r in _cm),
+                               '同歸戶原位次配地之街廓': _al_blk})
     _tot = {}
     for _r in _rows:
         _c = _tot.setdefault(_r['類'], [0, 0.0])
         _c[0] += 1
         _c[1] += _r['原有面積']
+    for _r in _rows:
+        if '段三併出面積' in _r:
+            # 🆕 `W-G.9-357`：部分併出之已併出之量計入原位次配地之面積（⛔ 加列數）⇒ 諸類面積之和恆 ＝ all_area
+            _tot.setdefault(ADJ_DISP_ALLOC, [0, 0.0])[1] += _r['段三併出面積']
     _tot[ADJ_DISP_GHOST] = [len(_ghost), sum(_a(t) for t in _ghost)]
     return {'slices': _rows, 'units': _units, 'step4': _step4, 'totals': _tot,
             'all_area': sum(_a(t) for t in _slices), 'all_count': len(_slices),
@@ -13029,8 +13061,9 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                      回 `a(src) × (p(src) ÷ p(dst))`；任一環取不到 ⇒ `raise`。
       trial_winner   `trial_winner(temp, build, 街廓, 端, 候選) -> (winner, 試算G, 門檻)`：
                      以所給之宗地重跑街角選位；`端` ∈ {`左`, `右`}。
-      alloc_state    `alloc_state(temp, build) -> {"kept": {街廓: set}, "bad_pools": {街廓: int}, "err": str|None}`：
-                     以所給之宗地重跑街角選位與配地。
+      alloc_state    `alloc_state(temp, build) -> {"kept": {街廓: set}, "bad_pools": {街廓: int}, "err": str|None,
+                     "G": {暫編地號: float}}`：以所給之宗地重跑街角選位與配地；🆕 `W-G.9-357`：`G` ＝ 保留宗之
+                     應分配面積（`G(㎡)`），其鍵集 ＝ `kept` 諸值之聯集（後處理之第 `5` 項〔`K-9-51`〕之序用之·缺 ⇒ 停機）。
       log_print      未處置之 `🔴` 出艙所用之印出函式。
       contests       🆕 `W-G.9-354`（`K-9-50`）：數末端塊合併再試之競合（唯 `end_block_merge_run` 給之；段三之呼叫恆
                      `None` ⇒ 逐列依序·逐位同本批前）。`list[dict]`：`{'形': '一'|'二', '列': [(街廓, 端, 候選, 交面積),
@@ -13040,7 +13073,12 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
       `order` 為空 ⇒ `(temp_parcels, build_parcels, [])`（同一物件·逐位同輸入）；
       否則 `temp_out` 為深拷貝，被段三「成」所消耗之片加鍵 `段三併出`（受併宗之相異字典序列表·補令一 裁三）；
       `build_out` ⊂ `temp_out`（同物件），整筆併出之建築片自其中移除；`log` 為逐列 `dict`。
-    停機（`RuntimeError`）：步驟 9 之配地中止（無從判定）、後處理之未定情形（原單停機款 `9`）。
+      🆕 `W-G.9-357`（`K-9-48` 七項 `3`〜`6` ＋ `K-9-51`）：後處理之整批不過 ⇒ 逐片——不可拆分者整筆、不過 ⇒ 第 `5` 項；
+      可拆分者逐受併宗以最大面積（`0.01 ㎡` 之格）併之、其餘 ⇒ 第 `5` 項（同一歸戶之保留宗，距離〔至其街廓〕近者先、
+      同距離者 `G` 大者先；都不行 ⇒ 記「轉調配」）；`K-9-50` 題一 `4` 之合併不過者同之（⛔ 停機）。可拆分之片經此而
+      仍有剩下者加鍵 `段三部分併出`（`{受併宗: 所併之來源面積}`·有併入者）與 `段三餘量`（剩下之來源面積）。
+    停機（`RuntimeError`）：步驟 9 之配地中止（無從判定）、後處理之未定情形（原單停機款 `9`）、
+      第 `5` 項之 `alloc_state` 未回 `G`。
     """
     import copy as _cp
     from shapely.geometry import Polygon as _Pg, LineString as _Ls
@@ -13398,24 +13436,30 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                     [(Lo['c'], _aprime(state, Lo['c'], W['c']), True)]
                 _t2 = _clone(state)
                 _apply(_t2, W['c'], _its_W)
-                if not _noaff(state, _t2, {W['blk'], _lb}, {Lo['c']}):
-                    raise RuntimeError(
-                        f"🔴 [K-6-B 段三 K-9-50 題一] {Lo['c']}（{_lb}）連同其半既不能依原位次配地，併入 {W['c']}"
-                        "（已取得之一端）亦不過「不影響原位次」——`K-9-48` 七項 3〜5 未落地（停機款 9）")
-                state = _t2
-                merged_out.add(Lo['c'])
-                for x in list(X) + [Lo['c']]:
-                    marks.setdefault(x, set()).add(W['c'])
-                _to = f"{Lo['c']} 不能依原位次配地 ⇒ 連同其半併入 {W['c']}"
-                _r4 = dict(整筆併入=[Lo['c']],
-                           切分併入={x: round(float(q), 4) for x, q, _w2 in _its_W if not _w2},
-                           併入量={W['c']: round(sum(q for _, q, _w2 in _its_W), 4)}, 受併宗=W['c'], 檢核='通過')
+                if _noaff(state, _t2, {W['blk'], _lb}, {Lo['c']}):
+                    state = _t2
+                    merged_out.add(Lo['c'])
+                    for x in list(X) + [Lo['c']]:
+                        marks.setdefault(x, set()).add(W['c'])
+                    _to = f"{Lo['c']} 不能依原位次配地 ⇒ 連同其半併入 {W['c']}"
+                    _r4 = dict(整筆併入=[Lo['c']],
+                               切分併入={x: round(float(q), 4) for x, q, _w2 in _its_W if not _w2},
+                               併入量={W['c']: round(sum(q for _, q, _w2 in _its_W), 4)}, 受併宗=W['c'], 檢核='通過')
+                else:
+                    # 🆕 `W-G.9-357`：連同其半併入已取得之一端不過 ⇒ 依 `K-9-48` 七項 4／3／5 與 `K-9-51` 處之
+                    #   （於其列之處為之·⛔ 停機）
+                    _to = (f"{Lo['c']} 不能依原位次配地；連同其半併入 {W['c']} 不過 ⇒ "
+                           "K-9-48 七項 4／3／5（K-9-51）")
+                    _r4 = None
             merged_out.update(X)
             _note = "題一｜" + "；".join(_path) + f"｜只一端成 ⇒ {W['c']}；{_to}"
             _ct_log(W, _rh[W['k']], True, _note)
             _ct_log(Lo, _rh[Lo['k']], False, _note)
             # 未得之一端之地主土地之去處（`K-9-50` 題一 4）——列於後處理之序（⛔ 計入定案之端）
-            _row(序='後處理', 街廓=_lb, 端=Lo['end'], 候選=Lo['c'], 層級='題一 4', 結果='成', **_r4, 競合=_note)
+            if _r4 is not None:
+                _row(序='後處理', 街廓=_lb, 端=Lo['end'], 候選=Lo['c'], 層級='題一 4', 結果='成', **_r4, 競合=_note)
+            else:
+                _t14_357(W, Lo, X, _frac[Lo['k']], _frac[W['k']], _note)
             return [Lo]
         # 整片各試
         _rw = {e['k']: _ct_try(e, _ct_whole(e, e['S'] | e['U']), '②') for e in (A, B)}
@@ -13534,6 +13578,214 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             raise RuntimeError(
                 f"🔴 [K-6-B 段三 K-9-50] 競合之列 {[_kf(l[0]) for l in _susp.values()]} 候其夥伴而夥伴未至（停機款 9）")
 
+    # ── 🆕 `W-G.9-357`（`K-9-48` 七項 3〜6 ＋ `K-9-51`）：後處理之整批不過者之逐片處置——步驟 10 與題一 4 呼叫之 ──
+    #   「來源面積」＝ 以 a(x)（段三之輸入之 分攤登記面積 ＋ 面積）計之量；k(x, r) ＝ a′(x, r) ÷ a(x)。
+    _part = {}              # 可拆分之片 → {受併宗: 本趟已併之來源面積（㎡）}
+    _left = {}              # 可拆分之片（本趟經七項 3／5 處置者）→ 剩下之來源面積（㎡）
+    _bunion = {}            # 街廓 → 段三之輸入中該街廓之全部切片之幾何之聯集（第 5 項之距離）
+    _t14_done = set()       # 補令一 `R-7′`：題一 4 之 `R-7` 所處置之候選——步驟 10 ⛔ 再處置之（唯 `_t14_357` 加入）
+
+    def _has357(r):
+        # 補令一 `R-15`：有剩下(r) ⇔ round(r, 4) ＞ 0（與寫出之四位小數同一式；判、寫、讀皆依之）
+        return round(float(r), 4) > 0
+
+    def _a357(x):
+        _v = float(_by0[x].get('分攤登記面積_m2', 0) or 0) + float(_by0[x].get('面積_m2', 0) or 0)
+        if not _v > 0:
+            raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {x} 之面積 {_v!r} ≤ 0——來源面積之折算無從定之（停機款 9）")
+        return _v
+
+    def _k357(x, recv):
+        _k = _aprime(state, x, recv) / _a357(x)
+        if not _k > 0:
+            raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {x} → {recv} 之 a′ 折算 {_k!r} ≤ 0（停機款 9）")
+        return _k
+
+    def _res357(g, s):
+        # 補令一 `R-15` ③：成 ⇔ ⛔ 有剩下(s − g)；部分成 ⇔ 有剩下(s − g) 且 g ＞ 0；未成 ⇔ 有剩下(s − g) 且 g ＝ 0
+        if not _has357(s - g):
+            return '成', '通過'
+        if g > 0:
+            return '部分成', '部分通過'
+        return '未成', '不過'
+
+    def _got357(x, recv, g):
+        # 可拆分之片之併入之帳（來源面積）；有正之併入 ⇒ 記其受併宗（`段三併出`）
+        if g > 0:
+            _part.setdefault(x, {})
+            _part[x][recv] = _part[x].get(recv, 0.0) + g
+            marks.setdefault(x, set()).add(recv)
+
+    def _max357(x, recv, s):
+        # 七項 3（`K-9-51` ②）：最大面積——先試 s；不過 ⇒ 於 {n × 0.01 < s} 中以二分法求通過之最大者；
+        #   所施者恆為已通過檢核之量（通過之試算態逕為現態·⛔ 另施未驗之量）。回所併之來源面積
+        nonlocal state
+        if not s > 0:
+            return 0.0
+        _k = _k357(x, recv)
+        _rb = {_blk_of[recv]}
+
+        def _try(g):
+            _t = _clone(state)
+            _apply(_t, recv, [(x, _k * g, False)])
+            return _t if _noaff(state, _t, _rb, set()) else None
+        _t = _try(s)
+        if _t is not None:
+            state = _t
+            return s
+        _n = int(s * 100.0)
+        while _n > 0 and _n / 100.0 >= s:
+            _n -= 1
+        while (_n + 1) / 100.0 < s:
+            _n += 1
+        _lo, _hi, _best = 0, _n, None
+        while _lo < _hi:
+            _mid = (_lo + _hi + 1) // 2
+            _tm = _try(_mid / 100.0)
+            if _tm is not None:
+                _lo, _best = _mid, _tm
+            else:
+                _hi = _mid - 1
+        if _best is not None:
+            state = _best
+        return _lo / 100.0
+
+    def _dist357(x, blk):
+        # 補令一 `R-6′` ③：四捨五入至 0.01 m（`ROUND_HALF_UP`·⛔ Python `round` 之偶數捨入）
+        from decimal import Decimal as _Dec357, ROUND_HALF_UP as _HU357
+        if blk not in _bunion:
+            from shapely.ops import unary_union as _uu357
+            _gs = [_geo[p] for p in sorted(_geo) if _blk_of[p] == blk and _geo[p] is not None]
+            if not _gs:
+                raise RuntimeError(
+                    f"🔴 [K-6-B 段三 後處理·第5項] 候選宗所在之街廓 {blk} 於段三之輸入中無切片——距離無從定之"
+                    "（域上之未定·停機上呈）")
+            _bunion[blk] = _uu357(_gs)
+        if _geo[x] is None:
+            raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] {x} 無重劃前幾何——距離無從定之（停機款 9）")
+        _d = float(_geo[x].distance(_bunion[blk]))
+        return float(_Dec357(repr(_d)).quantize(_Dec357('0.01'), rounding=_HU357))
+
+    def _k951(x, s, F, whole):
+        # 七項 5（`K-9-51` ①）：剩下之土地（來源面積 s）先併入同一地主另一個已配得土地之街廓（每次須通過檢核）——
+        #   候選 ＝ 現態保留之同歸戶宗（扣 x、已併出者、F 內街廓之宗）；距離近者先 → 配得面積（G）大者先 → 暫編地號小者先；
+        #   整筆者依序整筆試、過即止；可拆分者依序以最大面積併之。都不行 ⇒ 記「轉調配」（⛔ 停機·⛔ 🔴）。回剩下
+        nonlocal state
+        _cur = alloc_state(state["temp"], state["build"])
+        if _cur.get("err"):
+            raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] 現態配地中止：{_cur['err']!r}（停機款 9）")
+        _own = own_map or {}
+        _gx = str(_own.get(str(_by0[x].get('原地號', '') or ''), '') or '')
+        _pre = []
+        if _gx:
+            for _b in sorted(_cur["kept"]):
+                for _p in sorted(_cur["kept"][_b]):
+                    if _p == x or _p in merged_out or _b in F or _p not in state["by"]:
+                        continue
+                    if str(_own.get(str(state["by"][_p].get('原地號', '') or ''), '') or '') != _gx:
+                        continue
+                    _pre.append((_b, _p))
+        # 補令一 `R-6′` ②③：唯有候選通過篩時查 `G`（候選為空 ⇒ ⛔ 查、逕記轉調配）
+        _cands = []
+        if _pre:
+            _G = _cur.get("G")
+            if not isinstance(_G, dict):
+                raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] {x}：alloc_state 未回 G——配得面積之序無從定之（停機款 9）")
+            for _b, _p in _pre:
+                if _p not in _G:
+                    raise RuntimeError(
+                        f"🔴 [K-6-B 段三 後處理·第5項] alloc_state 未回 G 之 {_p}——配得面積之序無從定之（停機款 9）")
+                _cands.append((_dist357(x, _b), -float(_G[_p]), _p, _b))
+        _cands.sort()
+        _rem = s
+        for _d, _ng, _p, _b in _cands:
+            _base = dict(序='後處理', 街廓=_blk_of[x], 候選=x, 層級='後處理·第5項', 受併宗=_p, 距離=_d, G=-_ng)
+            if whole:
+                _q = _aprime(state, x, _p)
+                _t = _clone(state)
+                _apply(_t, _p, [(x, _q, True)])
+                if _noaff(state, _t, {_b, _blk_of[x]}, {x}):
+                    state = _t
+                    merged_out.add(x)
+                    marks.setdefault(x, set()).add(_p)
+                    _row(**_base, 結果='成', 檢核='通過', 整筆併入=[x], 併入量={_p: round(float(_q), 4)})
+                    _rem = 0.0
+                    break
+                _row(**_base, 結果='未成', 檢核='不過')
+            else:
+                if not _has357(_rem):
+                    break
+                _k = _k357(x, _p)
+                _g = _max357(x, _p, _rem)
+                _res, _chk = _res357(_g, _rem)
+                _qq = {_p: round(_k * _g, 4)} if _g > 0 else {}
+                _row(**_base, 結果=_res, 檢核=_chk, 切分併入=dict(_qq), 併入量=dict(_qq))
+                _got357(x, _p, _g)
+                _rem -= _g
+        if _has357(_rem):
+            _row(序='後處理', 街廓=_blk_of[x], 候選=x, 層級='後處理·第5項', 受併宗='—', 結果='轉調配', 檢核='—',
+                 併入量={}, 餘量=round(float(_a357(x) if whole else _rem), 4))
+        return _rem
+
+    def _split357(x, qs, lvl, extra):
+        # 七項 3：可拆分者逐受併宗之分（`_plan` 之序）以最大面積併之；其餘 ⇒ 七項 5（F ＝ 未全收之分之街廓）
+        _rem, _F = 0.0, set()
+        for _recv, _q in qs:
+            _k = _k357(x, _recv)
+            _s = float(_q) / _k
+            _g = _max357(x, _recv, _s)
+            _res, _chk = _res357(_g, _s)
+            _qq = {_recv: round(_k * _g, 4)} if _g > 0 else {}
+            _row(序='後處理', 街廓=_blk_of[x], 候選=x, 層級=lvl, 受併宗=_recv, 結果=_res, 檢核=_chk,
+                 整筆併入=[], 切分併入=dict(_qq), 併入量=dict(_qq), 全量=round(float(_q), 4), **extra)
+            _got357(x, _recv, _g)
+            if _has357(_s - _g):
+                # 補令一 `R-15` ①：有剩下之分始入已試之街廓、累其差（否則視為該分全收）
+                _F.add(_blk_of[_recv])
+                _rem += _s - _g
+        if _has357(_rem):
+            _rem = _k951(x, _rem, _F, False)
+        _left[x] = _rem
+
+    def _t14_357(W, Lo, X, frac_lo, frac_w, note):
+        # `K-9-50` 題一 4 之合併不過 ⇒ ① 未取得之一端之候選整筆試併入已取得之一端之受併宗（七項 4），不過 ⇒ 第 5 項；
+        #   ② 其半之每一片以最大面積併入之（七項 3·已取得之一端先前所併之半計入其帳），其餘 ⇒ 第 5 項（七項 6）
+        nonlocal state
+        c, w = Lo['c'], W['c']
+        _t14_done.add(c)    # 補令一 `R-7′`：`c` 依此處置畢即為其終局（① 之結果不論）——步驟 10 ⛔ 再處置之
+        _base = dict(序='後處理', 街廓=Lo['blk'], 端=Lo['end'], 層級='題一 4', 受併宗=w, 競合=note)
+        _q = _aprime(state, c, w)
+        _t = _clone(state)
+        _apply(_t, w, [(c, _q, True)])
+        if _noaff(state, _t, {W['blk'], _blk_of[c]}, {c}):
+            state = _t
+            merged_out.add(c)
+            marks.setdefault(c, set()).add(w)
+            _row(**_base, 候選=c, 結果='成', 檢核='通過', 整筆併入=[c], 併入量={w: round(float(_q), 4)})
+        else:
+            _row(**_base, 候選=c, 結果='未成', 檢核='不過')
+            _k951(c, _a357(c), {W['blk']}, True)
+        for x in sorted(X):
+            _f = float(frac_lo.get(x, 0.0))
+            if not _f > 0.0:
+                continue
+            _fw = float(frac_w.get(x, 0.0))
+            if _fw > 0.0:
+                _part.setdefault(x, {})
+                _part[x][w] = _part[x].get(w, 0.0) + _a357(x) * _fw
+            _k = _k357(x, w)
+            _s = _a357(x) * _f
+            _g = _max357(x, w, _s)
+            _res, _chk = _res357(_g, _s)
+            _qq = {w: round(_k * _g, 4)} if _g > 0 else {}
+            _row(**_base, 候選=x, 結果=_res, 檢核=_chk, 整筆併入=[], 切分併入=dict(_qq), 併入量=dict(_qq),
+                 全量=round(_k * _s, 4))
+            _got357(x, w, _g)
+            _rem = _s - _g
+            if _has357(_rem):
+                _rem = _k951(x, _rem, {W['blk']}, False)
+            _left[x] = _rem
+
     # ── 步驟 1〜8 ──
     for _r in _k950_rows(sorted(order, key=lambda r: r['最終序位'])):
         _blk, _end, c = _r['街廓'], _r['端'], _r['暫編地號']
@@ -13594,7 +13846,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                         f"（{_recv_by_blk[_b2]}／{_c2}）⇒ 停機款 9")
                 _recv_by_blk[_b2] = _c2
         _cl0 = _closer.get(_gi)
-        R = _mem - merged_out - set(_recv_by_blk.values()) - L
+        R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done   # 補令一 `X-3′`：扣 `R-7` 所處置之候選
         if not R:
             continue
         _cur = alloc_state(state["temp"], state["build"])
@@ -13729,6 +13981,10 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                 _row(**{**_base, '受併宗': '—'}, 結果='未處置', 檢核='—')
                 log_print(f"🔴 [K-6-B 段三 後處理] {x}（{_blk_of[x]}）未處置：二半片皆不鄰 B 內街廓")
                 continue
+            if not _batch_ok and not _whole:
+                # 🆕 `W-G.9-357`（`K-9-48` 七項 3／5·`K-9-51`）：可拆分者逐受併宗以最大面積併之，其餘 ⇒ 第 5 項
+                _split357(x, _qs, _lvl_name[_cl2], _extra)
+                continue
             if _batch_ok:
                 _ok = True
             else:
@@ -13744,14 +14000,27 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                     merged_out.add(x)
                 for _recv in _qty:
                     marks.setdefault(x, set()).add(_recv)
-            elif _whole:
-                _row(**_base, 結果='未成', 檢核='不過')
             else:
-                _row(**_base, 結果='未處置', 檢核='不過')
-                log_print(f"🔴 [K-6-B 段三 後處理] {x}（{_blk_of[x]}）未處置：「不影響原位次」不過")
+                _row(**_base, 結果='未成', 檢核='不過')
+                # 🆕 `W-G.9-357`（`K-9-48` 七項 4／5·`K-9-51`）：不可拆分者整筆不併入 ⇒ 第 5 項（F ＝ 其受併宗之街廓）
+                _k951(x, _a357(x), {_blk_of[r] for r, _ in _qs}, True)
 
     for _pid, _rs in marks.items():
         state["by"][_pid]['段三併出'] = sorted(_rs)
+    # 🆕 `W-G.9-357`：可拆分之片之部分併出與剩下——仍有剩下者：有併入 ⇒ `段三部分併出`（來源面積）＋ `段三餘量`，
+    #   全無併入 ⇒ 唯 `段三餘量` ＝ a(x)；本趟全收或有併入而無剩下者 ⇒ 去此二鍵；本趟未觸者⛔ 動
+    for _pid in sorted(set(marks) | set(_left)):
+        _tp = state["by"][_pid]
+        _rm = float(_left.get(_pid, 0.0))
+        if _has357(_rm) and _pid in marks:
+            _tp['段三部分併出'] = {_r: round(_v, 4) for _r, _v in sorted(_part.get(_pid, {}).items()) if _v > 0}
+            _tp['段三餘量'] = round(_rm, 4)
+        elif _has357(_rm):
+            _tp.pop('段三部分併出', None)
+            _tp['段三餘量'] = round(_a357(_pid), 4)
+        else:
+            _tp.pop('段三部分併出', None)
+            _tp.pop('段三餘量', None)
     return state["temp"], state["build"], log
 
 
@@ -19469,7 +19738,7 @@ def k6b_screen_callbacks(st, *, pk_kwargs, g_kwargs):
         except RuntimeError as _e_as:
             _err = str(_e_as).split("\n")[0][:300]
         _rows = [] if _err else list(_ss.get('f3_G_values') or [])
-        _kept, _bad = {}, {}
+        _kept, _bad, _G = {}, {}, {}
         for _r in _rows:
             _blk = _r.get('所屬街廓')
             _pid = str(_r.get('暫編地號'))
@@ -19485,7 +19754,8 @@ def k6b_screen_callbacks(st, *, pk_kwargs, g_kwargs):
                             _bad[_blk] = _bad.get(_blk, 0) + 1
             elif _r.get('驗_總判') == '保留':
                 _kept.setdefault(_blk, set()).add(_pid)
-        return {'kept': _kept, 'bad_pools': _bad, 'err': _err}
+                _G[_pid] = float(_r.get('G(㎡)', 0) or 0)   # 🆕 `W-G.9-357`：保留宗之應分配面積（`K-9-51` 之序）
+        return {'kept': _kept, 'bad_pools': _bad, 'err': _err, 'G': _G}
 
     def alloc_eval(temp, build):
         """🆕 `W-G.9-355`：以所給之宗地試算街角選位與配地（`SS_END_BLOCK_MODE` ＝ `'trial'`），回配地首趟之
diff --git a/verify/selection_pipeline.py b/verify/selection_pipeline.py
index 8bb4592..8d38e55 100644
--- a/verify/selection_pipeline.py
+++ b/verify/selection_pipeline.py
@@ -632,8 +632,26 @@ def run_corner_pk(ns, fake_st, cb, cad, param_rows, temp_parcels, build_parcels,
 
 def k6b_stage3_pool_temp(temp_parcels):
     """`W-G.9-344` 補令一 裁三：交予公設地調配（F.3／F.4）之 temp——去除段三所併出之片
-    （帶鍵 `段三併出` 者）。回傳**新 list**；⛔ 改其元素。段三不動（無標記）⇒ 元素全同。"""
-    return [tp for tp in (temp_parcels or []) if "段三併出" not in tp]
+    （帶鍵 `段三併出` 者）。回傳**新 list**；⛔ 改其元素。段三不動（無標記）⇒ 元素全同。
+    🆕 `W-G.9-357`（`K-9-48` 七項 3〜6）：帶 `段三併出` 且其 `段三餘量` ＞ 0 之片（部分併出）⇒ 以新 dict（淺拷貝）入之，
+    其 `分攤登記面積_m2`、`面積_m2` 各乘 ρ ＝ `段三餘量` ÷（分攤登記面積 ＋ 面積）；其餘同上。"""
+    _out = []
+    for tp in (temp_parcels or []):
+        if "段三併出" not in tp:
+            _out.append(tp)
+            continue
+        _rem = float(tp.get("段三餘量", 0) or 0)
+        if not _rem > 0:
+            continue
+        _a = float(tp.get("分攤登記面積_m2", 0) or 0) + float(tp.get("面積_m2", 0) or 0)
+        if not _a > 0:
+            raise RuntimeError(f"🔴 [段三 公設地調配之 temp] {tp.get('暫編地號')!r} 帶段三餘量而其面積 {_a!r} ≤ 0 ⇒ 停機")
+        _rho = _rem / _a
+        _tp = dict(tp)
+        _tp["分攤登記面積_m2"] = float(tp.get("分攤登記面積_m2", 0) or 0) * _rho
+        _tp["面積_m2"] = float(tp.get("面積_m2", 0) or 0) * _rho
+        _out.append(_tp)
+    return _out
 
 
 def k6b_f4_ctx(ctx_by_tag, build_pre_by_tag):
@@ -712,7 +730,7 @@ def _k6b_callbacks(ns, fake_st, cb, cad, param_rows, setback, snapshot):
             except RuntimeError as _e:
                 _err = str(_e).split("\n")[0][:300]
                 _rows = (getattr(_e, "partial", None) or {}).get("g_rows") or []
-        _kept, _bad = {}, {}
+        _kept, _bad, _G = {}, {}, {}
         for _r in _rows:
             _blk = _r.get("所屬街廓")
             _pid = str(_r.get("暫編地號"))
@@ -728,7 +746,8 @@ def _k6b_callbacks(ns, fake_st, cb, cad, param_rows, setback, snapshot):
                             _bad[_blk] = _bad.get(_blk, 0) + 1
             elif _r.get("驗_總判") == "保留":
                 _kept.setdefault(_blk, set()).add(_pid)
-        return {"kept": _kept, "bad_pools": _bad, "err": _err}
+                _G[_pid] = float(_r.get("G(㎡)", 0) or 0)   # 🆕 `W-G.9-357`：保留宗之應分配面積（`K-9-51` 之序）
+        return {"kept": _kept, "bad_pools": _bad, "err": _err, "G": _G}
 
     def alloc_eval(temp, build):
         """🆕 `W-G.9-353`：以所給之宗地試算街角選位與配地，回配地首趟之末端塊評選（深拷貝）；
````

## ⑨　各段耗時（規格單流程之試行評估·本機時）

| 段 | 起訖 | 約 |
|---|---|---|
| 首輪：讀單與開場 | （起點未錄）〜`14:07` | — |
| 首輪：工項零、一（入倉·推） | `14:07`〜`14:09` | `2` 分 |
| 首輪：前置（`run_all` `14:09:45`〜`14:24:59`） | `14:09`〜`14:25` | `16` 分（與讀碼、撰碼並行） |
| 首輪：讀碼與撰碼（`F16 selftest` 首跑即 `20／20`） | `14:14`〜`14:26` | `12` 分 |
| 首輪：驗 `V-1`〜`V-6`（`run_all` `14:27:27`〜`14:42:32`） | `14:27`〜`14:43` | `16` 分 |
| 首輪：獨立 reviewer（唯讀·並行） | `14:28`〜`14:46` | `18` 分 |
| 首輪：`V-7`（閘 `8`〜`22`·`34` 命令·單流） | `14:38`〜`15:30` | `52` 分 |
| 首輪：復現與停機報告（推 `47207e9`） | `14:46`〜`15:33` | — |
| 補令一：開場、工項零′、一′ | 〜`16:36` | — |
| 補令一：前置（沿用首輪之 `<O>` 三組·先證生產碼未變） | `16:36`〜`16:38` | `2` 分 |
| 補令一：撰碼（`F16 selftest` 首跑即 `25／25`） | `16:38`〜`16:41` | `3` 分 |
| 補令一：驗（`V-1′`〜`V-8`·`run_all` 與閘三流並行·閘之末 ＝ 流 B `17:04:26`） | `16:42`〜`17:04` | `22` 分（首輪單流之 `V-7` 為 `52` 分） |
| 補令一：推工項二、工項三、組報告 | `17:05`〜 | — |

🔒 **評估之要**：撰碼本身短（首輪 `12` 分、補令一 `3` 分）；耗時在驗（`run_all` `15` 分、閘 `8`〜`22` 單流 `52` 分·本批改三流並行）。規格單之 `F16` 以 `K` 例逐條繫 `R-*` ⇒ 撰碼一次即綠；而 `F16` 之母體所未造之形（題一 `4` 之轉調配）由獨立 reviewer 攔之 ⇒ **量測器之綠⛔ 蘊含規格之完整**（補令一 `§六` 甲之通則）。


## ⑩　`V-8` 之差異全文（`git diff f099d04 898c31f -- app.py verify/selection_pipeline.py`）

````diff
diff --git a/app.py b/app.py
index 63abb4b..d893879 100644
--- a/app.py
+++ b/app.py
@@ -13583,7 +13583,11 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
     _part = {}              # 可拆分之片 → {受併宗: 本趟已併之來源面積（㎡）}
     _left = {}              # 可拆分之片（本趟經七項 3／5 處置者）→ 剩下之來源面積（㎡）
     _bunion = {}            # 街廓 → 段三之輸入中該街廓之全部切片之幾何之聯集（第 5 項之距離）
-    _EPS357 = 1e-6
+    _t14_done = set()       # 補令一 `R-7′`：題一 4 之 `R-7` 所處置之候選——步驟 10 ⛔ 再處置之（唯 `_t14_357` 加入）
+
+    def _has357(r):
+        # 補令一 `R-15`：有剩下(r) ⇔ round(r, 4) ＞ 0（與寫出之四位小數同一式；判、寫、讀皆依之）
+        return round(float(r), 4) > 0
 
     def _a357(x):
         _v = float(_by0[x].get('分攤登記面積_m2', 0) or 0) + float(_by0[x].get('面積_m2', 0) or 0)
@@ -13598,7 +13602,8 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         return _k
 
     def _res357(g, s):
-        if g >= s:
+        # 補令一 `R-15` ③：成 ⇔ ⛔ 有剩下(s − g)；部分成 ⇔ 有剩下(s − g) 且 g ＞ 0；未成 ⇔ 有剩下(s − g) 且 g ＝ 0
+        if not _has357(s - g):
             return '成', '通過'
         if g > 0:
             return '部分成', '部分通過'
@@ -13646,6 +13651,8 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         return _lo / 100.0
 
     def _dist357(x, blk):
+        # 補令一 `R-6′` ③：四捨五入至 0.01 m（`ROUND_HALF_UP`·⛔ Python `round` 之偶數捨入）
+        from decimal import Decimal as _Dec357, ROUND_HALF_UP as _HU357
         if blk not in _bunion:
             from shapely.ops import unary_union as _uu357
             _gs = [_geo[p] for p in sorted(_geo) if _blk_of[p] == blk and _geo[p] is not None]
@@ -13656,7 +13663,8 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             _bunion[blk] = _uu357(_gs)
         if _geo[x] is None:
             raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] {x} 無重劃前幾何——距離無從定之（停機款 9）")
-        return round(float(_geo[x].distance(_bunion[blk])), 2)
+        _d = float(_geo[x].distance(_bunion[blk]))
+        return float(_Dec357(repr(_d)).quantize(_Dec357('0.01'), rounding=_HU357))
 
     def _k951(x, s, F, whole):
         # 七項 5（`K-9-51` ①）：剩下之土地（來源面積 s）先併入同一地主另一個已配得土地之街廓（每次須通過檢核）——
@@ -13666,12 +13674,9 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         _cur = alloc_state(state["temp"], state["build"])
         if _cur.get("err"):
             raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] 現態配地中止：{_cur['err']!r}（停機款 9）")
-        _G = _cur.get("G")
-        if not isinstance(_G, dict):
-            raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] {x}：alloc_state 未回 G——配得面積之序無從定之（停機款 9）")
         _own = own_map or {}
         _gx = str(_own.get(str(_by0[x].get('原地號', '') or ''), '') or '')
-        _cands = []
+        _pre = []
         if _gx:
             for _b in sorted(_cur["kept"]):
                 for _p in sorted(_cur["kept"][_b]):
@@ -13679,10 +13684,18 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                         continue
                     if str(_own.get(str(state["by"][_p].get('原地號', '') or ''), '') or '') != _gx:
                         continue
-                    if _p not in _G:
-                        raise RuntimeError(
-                            f"🔴 [K-6-B 段三 後處理·第5項] alloc_state 未回 G 之 {_p}——配得面積之序無從定之（停機款 9）")
-                    _cands.append((_dist357(x, _b), -float(_G[_p]), _p, _b))
+                    _pre.append((_b, _p))
+        # 補令一 `R-6′` ②③：唯有候選通過篩時查 `G`（候選為空 ⇒ ⛔ 查、逕記轉調配）
+        _cands = []
+        if _pre:
+            _G = _cur.get("G")
+            if not isinstance(_G, dict):
+                raise RuntimeError(f"🔴 [K-6-B 段三 後處理·第5項] {x}：alloc_state 未回 G——配得面積之序無從定之（停機款 9）")
+            for _b, _p in _pre:
+                if _p not in _G:
+                    raise RuntimeError(
+                        f"🔴 [K-6-B 段三 後處理·第5項] alloc_state 未回 G 之 {_p}——配得面積之序無從定之（停機款 9）")
+                _cands.append((_dist357(x, _b), -float(_G[_p]), _p, _b))
         _cands.sort()
         _rem = s
         for _d, _ng, _p, _b in _cands:
@@ -13700,7 +13713,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                     break
                 _row(**_base, 結果='未成', 檢核='不過')
             else:
-                if _rem <= _EPS357:
+                if not _has357(_rem):
                     break
                 _k = _k357(x, _p)
                 _g = _max357(x, _p, _rem)
@@ -13709,7 +13722,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                 _row(**_base, 結果=_res, 檢核=_chk, 切分併入=dict(_qq), 併入量=dict(_qq))
                 _got357(x, _p, _g)
                 _rem -= _g
-        if _rem > _EPS357:
+        if _has357(_rem):
             _row(序='後處理', 街廓=_blk_of[x], 候選=x, 層級='後處理·第5項', 受併宗='—', 結果='轉調配', 檢核='—',
                  併入量={}, 餘量=round(float(_a357(x) if whole else _rem), 4))
         return _rem
@@ -13726,10 +13739,11 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             _row(序='後處理', 街廓=_blk_of[x], 候選=x, 層級=lvl, 受併宗=_recv, 結果=_res, 檢核=_chk,
                  整筆併入=[], 切分併入=dict(_qq), 併入量=dict(_qq), 全量=round(float(_q), 4), **extra)
             _got357(x, _recv, _g)
-            if _g < _s:
+            if _has357(_s - _g):
+                # 補令一 `R-15` ①：有剩下之分始入已試之街廓、累其差（否則視為該分全收）
                 _F.add(_blk_of[_recv])
                 _rem += _s - _g
-        if _rem > _EPS357:
+        if _has357(_rem):
             _rem = _k951(x, _rem, _F, False)
         _left[x] = _rem
 
@@ -13738,6 +13752,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         #   ② 其半之每一片以最大面積併入之（七項 3·已取得之一端先前所併之半計入其帳），其餘 ⇒ 第 5 項（七項 6）
         nonlocal state
         c, w = Lo['c'], W['c']
+        _t14_done.add(c)    # 補令一 `R-7′`：`c` 依此處置畢即為其終局（① 之結果不論）——步驟 10 ⛔ 再處置之
         _base = dict(序='後處理', 街廓=Lo['blk'], 端=Lo['end'], 層級='題一 4', 受併宗=w, 競合=note)
         _q = _aprime(state, c, w)
         _t = _clone(state)
@@ -13767,7 +13782,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                  全量=round(_k * _s, 4))
             _got357(x, w, _g)
             _rem = _s - _g
-            if _rem > _EPS357:
+            if _has357(_rem):
                 _rem = _k951(x, _rem, {W['blk']}, False)
             _left[x] = _rem
 
@@ -13831,7 +13846,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                         f"（{_recv_by_blk[_b2]}／{_c2}）⇒ 停機款 9")
                 _recv_by_blk[_b2] = _c2
         _cl0 = _closer.get(_gi)
-        R = _mem - merged_out - set(_recv_by_blk.values()) - L
+        R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done   # 補令一 `X-3′`：扣 `R-7` 所處置之候選
         if not R:
             continue
         _cur = alloc_state(state["temp"], state["build"])
@@ -13997,10 +14012,10 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
     for _pid in sorted(set(marks) | set(_left)):
         _tp = state["by"][_pid]
         _rm = float(_left.get(_pid, 0.0))
-        if _rm > _EPS357 and _pid in marks:
+        if _has357(_rm) and _pid in marks:
             _tp['段三部分併出'] = {_r: round(_v, 4) for _r, _v in sorted(_part.get(_pid, {}).items()) if _v > 0}
             _tp['段三餘量'] = round(_rm, 4)
-        elif _rm > _EPS357:
+        elif _has357(_rm):
             _tp.pop('段三部分併出', None)
             _tp['段三餘量'] = round(_a357(_pid), 4)
         else:
````

## ⑪　首輪停機報告 `§十一` 四項於本批之處置（逐項對回補令一 `§一`）

| `§十一` 之項 | 補令一之裁 | 本批之處置 | 驗 |
|---|---|---|---|
| `1`（停機款 `5`·讀法甲／乙） | 裁一：**讀法乙**（`R-7′`／`X-3′`） | `_t14_done`：唯 `_t14_357` 加入 `c`；步驟 `10` 之 `R` 另扣之 | `K19` 綠（`Y1` 恰三列、轉調配恰一列、⛔「後處理(a)」）；首輪之碼 ＋ `F16p` ⇒ `K19` 紅（`§五` 項 `5`） |
| `2`（常規二·`段三餘量 ＝ 0.0`） | 裁二：**`R-15`** | `_has357`（`round(r, 4) ＞ 0`）代一切 `1e-6`；`_EPS357` 刪 | `K20`／`K20′` 綠 |
| `3`（CC 側之二偏離） | 裁三：准依字面更正 | `_dist357` 以 `ROUND_HALF_UP`（`R-6′` ③）；`G` 唯候選非空時查（`R-6′` ②③） | `K21`／`K22` 綠；`K11`（候選非空 ⇒ 停機）仍綠 |
| `4`（NOTE 與五事） | 裁四：`n / 100` 准；`_res357` 併入 `R-15`；`a(x) ≤ 0` 准；效能記；五事皆⛔ 改（`2` 增讀法 `3` 之記） | `R-5′` ⛔ 改碼；`_res357` 依 `R-15` ③；五事之碼⛔ 動；讀法 `3` 之增記隨塊 `K4′` 入典（工項三） | `P0` `25／25` |
