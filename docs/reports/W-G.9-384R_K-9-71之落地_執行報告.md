# `W-G.9-384R`　`K-9-71` 之落地　執行報告

> 單 ＝ `docs/orders/W-G.9-384_規格單.md`（規格單·建議等級 `high`·級 中）。受單 ＝ CC（Claude Code·Windows 11·施工樹 ＝ 桌面版之 worktree `claude/wg9-384-spec-016888`〔`detach` 於 `origin/wip/s1-endpart`〕）。
> 新側支 ＝ `verify/W-G.9-384-k971`（起點 ＝ 主線之端 `fffa397`）。**主線 `wip/s1-endpart` ⛔ 動**（仍 ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`）。
> 本機：Python `3.13.11`、`numpy 2.4.4`、`shapely 2.1.2`（發單側 ＝ `3.13.16`／`2.4.6`／`2.2.0`·照實載）；殼無 `WV_`（出艙 `[None, None, None, None, None]`）。
> `<O>` ＝ `C:\Users\admin\wg384O`（倉外·非任何 git 工作樹〔`git -C C:\Users\admin rev-parse --show-toplevel` ⇒ `fatal: not a git repository`〕）。前置之量於拋棄式 worktree `C:\Users\admin\wg384W`（`detach` 於工項一之端 `b47efbc`）、驗之量於 `C:\Users\admin\wg384P`（`detach` 於工項二之 `commit` `8ce1a18`），皆短路徑（`自誤 479`·`MAX_PATH`）；二者之 `git status --porcelain` 於量畢皆空。
> 收工閘之實測值出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 首列 | 推 |
|---|---|---|---|
| 零 | `288a0d522611881ca0866c8c48d4318dccd4fcd2` | `W-G.9-384 工項零：本單原封入倉（新側支）⛔ 零生產碼` | `git push origin HEAD:refs/heads/verify/W-G.9-384-k971`（新立·`* [new branch]`） |
| 一 | `b47efbcb111633959d708bc1722eaabb83b0185d` | `W-G.9-384 工項一：量測器之期之更新（F23 之 K61〜K74 與 W1／W9；F16 之 K23〜K32；F14、F15、F9、F24、F25 之許與期）（新側支）⛔ 零生產碼` | 快轉 `288a0d5..b47efbc` |
| 二 🔴 | `8ce1a1828ee8b0a9991d05c91ef3b48c06fee401` | `W-G.9-384 工項二：K-9-71 之落地（段三後處理之第 5 項之輪與手冊先行之 K-9-51 之輪：建地之片之候選依本街廓 → 五級與深度 → 距離；五級之屬性 ＝ 調配之名單之同一處·blk5 與六入口）🔴 生產碼（新側支）` | 驗 `V-1`〜`V-9` 與唯讀審查皆符後 快轉 `b47efbc..8ce1a18` |
| 三 | `d358f218ec3662f96106341ed9e037f840e729a1` | `W-G.9-384 工項三：W-G.9-383 之入主線·K-9-78 之立·K-9-71 之落地之讀法入典 ＋ 自誤 620 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` | 快轉 `8ce1a18..d358f21` |
| 四 | （本檔所在之 `commit`·自指 ⇒ 見對話） | `W-G.9-384 工項四：執行報告入倉（新側支）⛔ 零生產碼` | 快轉 |

各 `commit` 之訊息 ＝ 所令之首列逐字、空一列、`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`（`git commit -F`）。逐 `commit` 之生產碼判（`git diff --name-only <父> <子> -- app.py verify/stepg_pipeline.py verify/run_all.py verify/run_verification.py`）：工項零、一、三 ＝ 空輸出；工項二 ＝ `app.py`。

## ② 停機款 `1`〜`12`（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `fffa397`；heads `43`、⛔ 含新側支；施工樹追蹤檔無變動；`§零-0` 項 `3` 之 `rc` 與四簿；殼之旗標 | `git rev-parse origin/wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`；`git ls-remote --heads origin` ＝ `43` 列（存 `<O>\heads_before.txt`）、含 `W-G.9-384` 之列 `0`；`git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空；`probe_WG9321_issuer_anchor.py … 619 615` ⇒ `rc 0`·「項4′」：自誤 `604`／`619`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `74`／`77`／`[44, 47]`；旗標 `[None, None, None, None, None]` ⇒ 未成就 |
| `2` | `SELF_SHA256` 自驗、bytes／`sha256`、來源、入倉 blob | 來源 ＝ **第二處**（KL 主 checkout 之根 `C:\Users\admin\Desktop\land-readjustment-trial\W-G.9-384_規格單.md`；施工樹之根無之）；`126432` B·`sha256` `42668484a2f3cde92816021a46f8cf2364d4c39620b5aeb85cb38d881f356082`·`1040` 列·CR `0`；`SELF_SHA256`（`P-5` 原口徑·受詞 `126354` B）實算 ＝ 單載 ＝ `5ac5dd16e7a1283643c8a99536b5d225da20d22a0a92c5b918ae710ef8017bfa`。KL 之訊唯附本單之檔、**未載 bytes／`sha256`** ⇒ 依 `§零-0` 項 `4` 以 `SELF_SHA256` 為據（⛔ 停機）。入倉後 `git cat-file blob HEAD:docs/orders/W-G.9-384_規格單.md` 與來源 `cmp` 逐位同 ⇒ 未成就 |
| `3` | 四塊之三數、`git apply --check`、施後 blob | 見 ④；`git apply --check` `rc 0`；`7` 器之施前／施後 blob 皆 ＝ `§五-1` 項 `2`／`5`；`git diff --numstat` 唯此 `7` 檔 ⇒ 未成就 |
| `4` | 工項二前置 `1`〜`4` | 全符（③-1） ⇒ 未成就 |
| `5` | 規格之歧義涉域上判斷 | 無 ⇒ 未成就 |
| `6` | `V-1`〜`V-9`；本案配地之變 | 全符（③-2）；配地⛔ 變（`V-4`〜`V-6`） ⇒ 未成就 |
| `7` | `push` 之目標、被拒、主線之推進 | 四推之目標皆 `verify/W-G.9-384-k971`、皆首推即成、⛔ `--force`；主線始終 `fffa397` ⇒ 未成就 |
| `8` | 三簿之附加、`checkidx`、`gen_fa_index` | 見 ④、⑨ ⇒ 未成就 |
| `9` | 收工閘 | 於工項四之推後量之（出艙於對話） |
| `10` | CC 之「孰為正典」之判、改塊／器／命令 | 無（器一字未改；`<repo>` 依單首之形傳入） ⇒ 未成就 |
| `11` | 新檔之 `git check-ignore -v --no-index` | 本單：`rc 1`·無命中（工項零）；報告二檔：收工閘 `2` ⇒ 未成就 |
| `12` | 唯讀審查之發現涉域上判斷或規格之漏載 | 無（⑥-2：十條皆符·(甲) `0`·(乙) `0`·(丙) `9`） ⇒ 未成就 |

**本批之自解清單**：無。

## ③ 前置與驗之出艙

### ③-1 工項二前置（於工項一之端 `b47efbc`·拋棄式 worktree `C:\Users\admin\wg384W`）

**前置 `1`**（紅·末列逐字皆 ＝ 單）：

- `python verify/probes/probe_WG9363_k953.py selftest C:\Users\admin\wg384W` ⇒ `rc 1`·`stderr` `0` B·末列 `⇒ 紅 ['K61', 'K62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68', 'K70', 'K72', 'K73', 'K74']；rc 1`
- `python verify/probes/probe_WG9363_k953.py wiring C:\Users\admin\wg384W 7d8e954` ⇒ `rc 1`·`stderr` `0` B·末列 `⇒ 紅 ['W1', 'W9']；rc 1`
- `python verify/probes/probe_WG9357_k948.py selftest C:\Users\admin\wg384W` ⇒ `rc 1`·`stderr` `0` B·末列 `⇒ 紅 ['K23', 'K24', 'K25', 'K26', 'K27', 'K28', 'K29', 'K30', 'K31', 'K32']；rc 1`
- `python verify/probes/probe_WG9355_screenmerge.py selftest C:\Users\admin\wg384W` ⇒ `rc 1`·`stderr` `0` B·末列 `⇒ 紅 ['T6a']；rc 1`
- `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring C:\Users\admin\wg384W` ⇒ `rc 1`·`stderr` `0` B·末列 `⇒ 紅 ['W3']；rc 1`
- `python verify/probes/probe_WG9373_k966.py mutate C:\Users\admin\wg384W` ⇒ `rc 3`·`stderr` `0` B·末列 `⇒ 突變 57（另基準一）；紅 []；無從判定 ['N00']；rc 3`

`probe_WG9373p1_partrem.py selftest`（`F28`）⇒ `rc 0`·`P0 逐項擾動恰該項紅 29／29`。

**前置 `2`**（綠）：其餘之呼叫皆 `rc 0`、末列 ＝ 開工態之同器之末列（表見 ③-3 之前置之欄）。

**前置 `3`**：`k6s3 run`（`3.5`／`0.0`·`on`）、`F8 run`（`3.5`／`0.0`）、`parity`（`3.5`／`0.0`·`on`）六呼叫皆 `rc 0`·`stderr` `0` B；落檔 `<O>\pre\k6s3_pre_35.json`、`k6s3_pre_00.json`、`f8_pre_35.json`、`f8_pre_00.json`、`parity35_pre.json`、`parity00_pre.json`。

**前置 `4`**（於 `C:\Users\admin\wg384W`）：

````text
rc=1
app.py:1
rc=0
rc=1
````

（`def k971_key5` ⇒ 無出艙·`rc 1`；舊依據之字面 ⇒ `app.py:1`；`blk5=callbacks['blk5']` ⇒ 無出艙·`rc 1`·皆 ＝ 期。）

### ③-2 工項二之驗（於 `8ce1a18`·拋棄式 worktree `C:\Users\admin\wg384P`·殼無 `WV_`）

| # | 實 |
|---|---|
| `V-1` | 十呼叫皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；`F23 selftest` `P0 逐項擾動恰該項紅 74／74`；`F16 selftest` `P0 逐項擾動恰該項紅 35／35`；`F23 wiring` `W1`〜`W9` 皆 ✅（全文見下） |
| `V-2` | 其餘 `42` 呼叫皆 `rc 0`；`F27 mutate` ＝ `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`；`F25 mutate` ＝ `⇒ 突變 8（另基準一）；紅 []；rc 0`；`F4 wiring` ＝ `⇒ rc 0（不符 0·器紅 0）`；`k6s3 selftest` ＝ `selftest 9/9 ⇒ ✅`；`pooltemp selftest` ＝ `selftest 13/13 ⇒ ✅`；`synth` ＝ `ε ＝ 0.0002｜rc 0`；`main_synth` ＝ `紅項 [] 器紅 0`；餘皆 `⇒ 紅 []；rc 0`。`P0`：`F29` `74／74`、`F27` `31／31`、`F28` `29／29`、`F24` `28／28`、`F14` `86／86`；`F29 wiring` `Y1`〜`Y11` ✅、`F27 wiring` `Y1`〜`Y9` ✅ |
| `V-3` | `7` 器之 blob ＝ `§五-1` 項 `5`（見下） |
| `V-4` | `k6s3 run` 二退縮皆 `rc 0`；`cmp` 二者皆 `rc 0`·末列 `相異 0 項 ⇒ ✅ 同` |
| `V-5` | `parity` 二退縮皆 `rc 0`·末列 `⇒ rc 0（不符 0 項）`；配地列 harness `35`／畫面 `34`（`3.5 m`）、`36`／`35`（`0 m`）·不符格 `0`；手冊先行 session 鍵 `f3_k953_log` `37`／`46` 列；落檔與 `stdout` 以同一字樣代 `HEAD` 之全值後逐位同、⛔ 代之則相異（見下） |
| `V-6` | `F8 run` 二退縮皆 `rc 0`·末列 `⇒ 紅 []；rc 0`；`hash-object` 施前施後相等（見下） |
| `V-7` | 生產碼 `34` 檔對工項一之端相異恰 `2`（`M app.py`、`M verify/selection_pipeline.py`）；`verify/` 之他檔相異 `0`；`app.py` `+126`／`-10`·blob `261c5ac99f2b3b6e19152a689156378242d4c3a7`（`1818878` B）；`verify/selection_pipeline.py` `+15`／`-5`·blob `d197f222076529c700a770915248790e316ce259`（`60273` B）；頂層之名：`app.py` `383` → `385`（新 ＝ `{k971_blk5, k971_key5}`·去 ＝ `{}`·改 ＝ `{end_block_merge_run, f3_screen_end_block_merge, f3_screen_k6b_stage3, f3_screen_k953, k6b_screen_callbacks, k6b_stage3_run, k953_manual_run}`）；`verify/selection_pipeline.py` 之名之集⛔ 變（改 ＝ `{_k6b_callbacks, run_corner_pk_k6b, run_end_block_merge, run_k953}`） |
| `V-8` | 見下（皆 ＝ 期） |
| `V-9` | `V-1`〜`V-6` 之諸器（`52` 呼叫 ＋ `k6s3`／`F8`／`parity` 六呼叫 ＋ `k6s3 cmp` 二呼叫）之 `stderr` 合計 `0` B |

**`V-1` 十呼叫之全文**：

`python verify/probes/probe_WG9363_k953.py selftest C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`6.3` s

````text
── 手冊先行（K-9-53 ①）之各支 ──
  ✅ K1 跨分配線（所鄰之已配得之宗恰一）⇒ 整筆併入、出 build、帶 段三併出
  ✅ K2 跨分配線（所鄰之已配得之宗分處二街廓）⇒ 併入應分配面積（G）較大者
  ✅ K3 （K-9-67）二者之 G 並列 ⇒ 重劃前面積同（300）⇒ 暫編地號小者 E1(1)；E1 之重劃前面積 250 ⇒ X1(2)
  ✅ K4 建地片與同街廓之已配得之宗相鄰 ⇒ 依手冊整筆併入之（K-9-58 ③·W-G.9-380）
  ✅ K5 道路·兩側皆有 ⇒ 依中心線切分、各半併入該側之宗（a′ × 半之面積比）
  ✅ K6 道路·唯一側有 ⇒ 整筆往該側（所鄰之街廓依中心線分側）
  ✅ K7 道路·兩側皆無 ⇒ 未併、帶 段三餘量 ＝ a（視同無同歸戶）
  ✅ K8 道路片全在無已配得之側（⛔ 鄰有之側之街廓）⇒ 仍整筆往有之側
  ✅ K9 隔道路之分不到之建地 ⇒ 隨道路片往另一側之宗
  ✅ K10 公設地 ⇒ 平分於其合併群所及之已配得之街廓（群外之已配得之宗⛔ 與）
  ✅ K11 公設地不相連於任何已配得之宗 ⇒ 未併、帶 段三餘量 ＝ a
  ✅ K12 路口之道路片（鄰三街廓以上、含公設地）⇒ 比照公設地平分
  ✅ K13 落點四層瀑布：① 同原地號者先於較近者；② 皆非同原地號 ⇒ 質心距近者；③ 等距 ⇒ G 大者；④ 皆同 ⇒ 暫編地號
  ✅ K14 （K-9-66）整批不過 ⇒ 建地整筆不過 ⇒ 按比例部分併入 10；剩下 50 依 K-9-51（他街廓之已配得之宗·距離近者先）
  ✅ K15 可拆分之片之最大面積（0.01 ㎡ 之格）；其餘 ⇒ K-9-51 皆無 ⇒ 入合併單位、帶 段三部分併出／段三餘量
  ✅ K16 併入後配地中止 ⇒ 不過（記其由·⛔ 停機）
  ✅ K17 帶段三之鍵之片⛔ 受理
  ✅ K18 無任何配得土地之地主：同號之連通分量之再試未成 ⇒ 回輸入之同一物件、紀錄唯再試之列（K-9-73 ④）
  ✅ K19 入池閘之合併單元：取代後之配地全同 ⇒ 取代；相異 ⇒ ⛔ 取代（記之）
  ✅ K20 調配之輸入（⛔ 改·沿用段三之鍵）：併出 ⇒ 原位次配地（所屬單元『段三併入 …』）；餘量 ⇒ 入合併單位；待同歸戶併入 ＝ 空
  ✅ K21 公設地調配之 temp（⛔ 改·沿用段三之鍵）：併出而無餘量 ⇒ 去之；部分併出 ⇒ 依餘量之比縮之
  ✅ K22 a′ 之折算（街廓之地價比）
  ✅ K23 （K-9-66）整批不過時：建地先（全入）、道路次（按比例）、公設地未試；剩下之列於諸輪之後
  ✅ K24 旗標 WV_K953：未設／on ⇒ 真；off ⇒ 偽；他值 ⇒ 停機
  ✅ K25 可為受詞之片之歸戶於 build 皆無片（例：歸戶表為空）⇒ ⛔ 試算配地、回輸入之同一物件、紀錄 ＝ []
  ✅ K26 試算之摘要：抵費地之形放不下最小建築面積之矩形 ⇒ 配餘地不合格一處；保留 ⇒ 保留宗與其 G；餘⛔ 計
  ✅ K27 入池閘之單元：成員（缺 ⇒ 自身）；成員 ≥ 2 者為單元（深拷貝）
  ✅ K28 K-9-51 之候選含 x 之本街廓之已配得之宗（與 x ⛔ 相連·距離 0）⇒ 先試併之、過 ⇒ 併入、出 build（K-9-55）；其檢核不過 ⇒ 記未成、續試他宗；皆不行 ⇒ 入合併單位（補令二·乙案）
  ✅ K29 入池閘之旗標 off（WV_K929_6）⇒ 手冊先行不辦（harness 與畫面皆回輸入之同一物件、紀錄 []、畫面⛔ 呼叫 st）；二旗標皆判（WV_K953 off 而 WV_K929_6 非法 ⇒ 停機）
  ✅ K30 畫面：旗標值非法（WV_K953 或 WV_K929_6）⇒ f3_k6b_stage3_error ＝ （手冊先行）…、st.error ＋ st.stop、⛔ 寫紀錄
  ✅ K31 入池閘之單元之取代後：build ⊂ temp（同物件）、temp 中之標的 ＝ 單元（帶入池閘併入）、他成員仍在 temp 而⛔ 在 build
  ✅ K32 K-9-51 之候選同距離（0）：本街廓之宗居先於他街廓之宗（G 較大者亦然·K-9-55 之二）；本街廓無之、或其檢核不過 ⇒ 他街廓之宗
  ✅ K33 K-9-51 之本街廓之候選與 x 相連（C0 之後始為已配得）、⛔ 相連 ⇒ 皆本街廓之宗居先、併入之（W-G.9-380）
  ✅ K34 K-9-51 之本街廓之候選之成員取當下之試算：其單元於 C0 之後始含與 x 相接之片、該片⛔ 與 x 相接 ⇒ 皆併入之（W-G.9-380）；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K35 本街廓之候選：G 較小者（H2(1)）與 x 相接 ⇒ 相接者（距離 0）先、併入之（K-9-51·W-G.9-380）；後者⛔ 與 x 相接 ⇒ 併入 G 較大者
  ✅ K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入
  ✅ K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入其計畫之受併宗
  ✅ K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片——⛔ 停機、依計畫併入（W-G.9-380）；⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（程式自我檢查·K-9-57 ⑧）
  ✅ K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）
  ✅ K41 跨二街廓之小片 S(1) 唯與已配得之宗 R(1) 之成員 Q(1)（⛔ R(1) 之自身之形）相連 ⇒ 手冊先行連同成員看之、依手冊整筆併入 R(1)（巳 ③）
  ✅ K42 計畫之同街廓相鄰之已配得之宗（Q1(1)·X1(2) 為他地號 ⇒ ⛔ 第 31 條第 3 款）之併入之檢核不過（BA 之容量 0）⇒ 記未成、依 K-9-51 併入他街廓之宗（X1(2)）
  ✅ K43 同街廓相鄰（Q1(1)）與他街廓之同一原地號（X1(2)）並存 ⇒ 第 31 條第 3 款先（K-9-73）：X1(2) 之 G 400 ⇒ X1(2)；Q1(1) 之 G 400 ⇒ 仍 X1(2)
  ✅ K44 同街廓相鄰之已配得之宗二（A1(1) G 300、A2(1) G 200）⇒ 應分配面積大者 A1(1)（K-9-61 ①⑦·K-9-67）
  ✅ K45 （K-9-73 ⑤）與他街廓之已配得之宗（X1(2)·他地號）相連而無同一原地號者 ⇒ ⛔ 依手冊併入（計畫無受併宗·未併）
  ✅ K46 （K-9-73 ③⑤⑦）分不到之 C1(1) 與他街廓之同一原地號 C1(2) 及他地號 G1(1)（G 較大）皆相連、且隔自己之道路片 R1(1) ⇒ 第 31 條第 3 款（唯同一原地號）先 ⇒ C1(2)
  ✅ K47 （K-9-73 ⑥·手冊道路用地分配原則 1）分不到之 C1(1) 隔自己之道路片 R1(1)（另一側 X1(2)），而同街廓有已配得之C9(1) 與之相連 ⇒ 道路兩側皆有己地（道路片依中心線切分·⛔ 隨道路往另一側）⇒ 併入同街廓相鄰之 C9(1)
  ✅ K48 （K-9-73 ⑤）分不到之 X1(1) 與同街廓之 Q1(1) 及他街廓之他地號 X1(2)（G 400·較大）皆相連 ⇒ 他地號之相連⛔ 入比較 ⇒ 併入同街廓相鄰之 Q1(1)
  ✅ K49 （K-9-73 ④）X1(1)（BA 60）與 X1(2)（BB 300）皆不配地 ⇒ X1(1) 整筆併入 G 大之 X1(2)；併後 X1(2)（360）配地 ⇒ 成：X1(1) 出 build、帶 段三併出 ['X1(2)']；X1(2) 之 面積_m2 60、帶 第31條第3款併入 ['X1(1)']
  ✅ K50 （K-9-75）受併之片依應分配面積（不配地紀錄之 G）：X1(1) 之 G 500 ＞ X1(2) 之 300 ⇒ X1(2) 併入 X1(1)（⛔ 依面積）
  ✅ K51 （K-9-75·K-9-67）G 並列（皆 100）⇒ 重劃前面積大者（X1(2) 300 ＞ X1(1) 60）受併（⛔ 暫編地號之序）
  ✅ K52 （K-9-29）再試之併入量依 a′（BA 之地價 2 倍）⇒ 120
  ✅ K53 （K-9-75 ②）同一原地號跨三街廓（X1(1)·BA ─ X1(2)·BB ─ Z1(1)·BD·X1(1) 與 Z1(1) ⛔ 直接相接）皆不配地 ⇒ 餘二片皆併入 G 最大之 Z1(1)（400）；併後 760 配地 ⇒ 成
  ✅ K54 （K-9-75 ②）三街廓之同號之連通分量而 Z1(1) 已配得 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1)（⛔ 與 Z1(1) 直接相接）亦併入 Z1(1)
  ✅ K55 （K-9-73 ⑥）同一原地號而隔道路之 C1(1)（BC）⛔ 入同號之連通分量 ⇒ 再試唯 X1(1) → X1(2)
  ✅ K56 再試之受詞存在而試算未回 dropped ⇒ 停機（⛔ 以空代之）
  ✅ K57 同號之片 X1(2) 為已配得之宗 Y1(1) 之成員 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1) 併入 Y1(1)
  ✅ K58 （K-9-75）同一原地號之公設地之片（P1(1)·PK·與 X1(2) 相接）⛔ 入同號之連通分量 ⇒ 再試照行（X1(1) → X1(2)）
  ✅ K59 （K-9-73 ⑨）受併之片配地而「不影響原位次」之檢核不過（BB 之配餘地不合格）⇒ 未成（⛔ 施）
  ✅ K60 再試成而受併之片 X1(2) 為同地主之 Y1(1)（宿主）之單元之成員 ⇒ 單元之取代（X1(2) 出 build）之後，Y1(1) 之單元帶 第31條第3款併入 ['X1(1)']（⛔ 失）
  ✅ K61 （K-9-71）BC 之使用分區（商業區）異於片之所屬街廓 BA ⇒ 五級排後：剩下 50 併入 BD 之 Z1(1)（⛔ 距離近之 C1(1)）
  ✅ K62 （K-9-71）五級皆同而 BC 較深（40）⇒ 排後 ⇒ Z1(1)；BC 深 30.1（同深之容差 0.1 m 內）⇒ 依距離 ⇒ C1(1)
  ✅ K63 （K-9-71）BD 之最小建築面積往大（100）⇒ 排後而⛔ 淘汰：C1(1)（BC 容 0）不過 ⇒ 續試 Z1(1) 成
  ✅ K64 他街廓之候選二以上（BC、BD）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）
  ✅ K65 他街廓之候選唯一（BB·C1 去之）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（K42 之形）
  ✅ K66 五級之屬性缺片之所屬街廓（BA）⇒ 停機
  ✅ K67 五級之屬性之回呼唯於須比時呼之、且一次（K61 之形 ⇒ 1；Z1 非 g1 ⇒ 他街廓唯一 ⇒ 0）
  ✅ K68 k971_key5 ＝ adj_candidate_lists 之建地軌之八鍵之前六（合成之屬性三組·七街廓·逐對 126）
  ✅ K69 再試成而受併之片 X1(2) 為 Y1(1) 之單元之成員；取代後之配地相異（未取代）⇒ 當下之態⛔ 變：X1(2) 仍在 build 且帶標記、宿主 Y1(1)⛔ 帶鍵
  ✅ K70 他街廓唯一（BC）而其候選二宗（C1(1)、C9(1)·皆 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行 ⇒ C1(1)
  ✅ K71 五級與深度皆同之他街廓 BC（距 10）、BD（距 20）、BZ（距 1·名序最後）⇒ 依距離 ⇒ BZ 之 Z9(1)（⛔ 依街廓名）
  ✅ K72 （K-9-71）正面路寬：BA 8、BC 15（往寬）、BD 6（往窄）⇒ 二者皆異、級距 BD 先（往窄先於往寬）⇒ Z1(1)
  ✅ K73 （K-9-71）正面道路：BC 臨他路（RX）⇒ 排後 ⇒ Z1(1)
  ✅ K74 五級之屬性之回呼回非 dict ⇒ 停機
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 74／74
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9363_k953.py wiring C:\Users\admin\wg384P 7d8e954` ⇒ `rc 0`·`stderr` `0` B·`44.2` s

````text
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', '_k929_6_screen_gate', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'end_block_merge_run', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（618）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9357_k948.py selftest C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`6.1` s

````text
── 段三後處理之七項 3〜6 與第 5 項之序（K-9-51）──
  ✅ K1 整批通過 ⇒ 一列、二受併宗各 100、⛔ 新鍵
  ✅ K2 最大面積 60 ＋ 第 5 項併入 Y1（距 0·G 大者）⇒ 全數併出
  ✅ K3 第 5 項依距離：B5 之 Y1 部分 20、Y2 未成 ⇒ B7 之 Z1 收 20
  ✅ K4 餘 15 轉調配：段三併出＋段三部分併出＋段三餘量
  ✅ K5 同距離者 G 大者先 ⇒ Y2 收 40
  ✅ K6 （K-9-66）建地整筆不過 ⇒ 按比例部分併入 X1 30；剩下 20 第 5 項併入 Y1；W1 全數併出 ⇒ 出 build
  ✅ K7 （K-9-66）部分併入 30 後他處皆不過 ⇒ 轉調配；W1 留 build、帶 段三併出／段三部分併出
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
  ✅ K17 （K-9-66）題一 4 不過 ⇒ 建地 Y1 按比例收 20、其半 X3 未併；第 2 輪同到 Z1 ⇒ Y1 70、X3 40 一起成（⛔ 停機）
  ✅ K18 （K-9-66）第 2 輪 B7 只容 100 ⇒ Y1 70 全入、X3 按比例 30 ⇒ 餘 10 轉調配：X3 段三部分併出 {X1: 40, Z1: 30}、段三餘量 10
  ✅ K19 （K-9-66）第 2 輪 B7 只容 50 ⇒ Y1 按比例 50、X3 未併 ⇒ 皆轉調配（即終局·Y1 恰三列、轉調配各一列）；Y1 留 build
  ✅ K20 差 0.00003（四位小數為 0）⇒ 視為全收：二列皆成、⛔ 第 5 項、⛔ 餘量之鍵
  ✅ K20′ 同上之調配之輸入：P1 歸原位次配地、⛔ 入合併單位（對照）
  ✅ K21 距離 0.125 四捨五入 ⇒ 0.13 ＝ Z9 ⇒ G 大者 Z9 先；紀錄之距離 ＝ 0.13；G 取該輪之試算
  ✅ K22 候選為空 ⇒ alloc_state 未回 G 亦⛔ 停機：W1 未成 ⇒ 轉調配
  ✅ K23 （K-9-71）B5 之使用分區（商業區）異於 W1 之所屬街廓 BW ⇒ 五級排後：剩下 20 併入 B7 之 Z1（⛔ 距離近之 B5）
  ✅ K24 （K-9-71）本街廓之候選恆先：BW 之 W2(1)（G 20）先於 BU 之 U1(1)（距離同為 0·G 500）
  ✅ K25 他街廓之候選二以上（B5、B7）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）
  ✅ K26 他街廓之候選唯一（B5·Z1 非 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（同 K6）
  ✅ K27 公設地之片（P1(1)·K3 之形）照距離（B5 之五級雖異）、⛔ 呼其回呼
  ✅ K28 五級之屬性之回呼唯呼一次（K23 之形）
  ✅ K29 段三之關鍵字參數 blk5 之缺省 ＝ None
  ✅ K30 （K-9-71）正面路寬：BW 8、B5 15（往寬）、B7 6（往窄）⇒ 二者皆異、級距 B7 先 ⇒ Z1
  ✅ K31 （K-9-71）正面道路：B5 臨他路（RX）⇒ 排後 ⇒ Z1
  ✅ K32 五級之屬性之回呼回非 dict ⇒ 停機
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 35／35
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9355_screenmerge.py selftest C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`5.6` s

````text
── 受詞：['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows'] ⇒ 缺 [] ──
── 合成對照（樁·期值出自規格單 §三）──
  ✅ T1a 段二序為空之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  ✅ T1b 合併再試恰一次、段三本體⛔ 呼：得 (1, 0)　期 (1, 0)
  ✅ T1c 無變 ⇒ 回傳之宗地 ＝ 輸入（同一物件）：得 (True, True)　期 (True, True)
  ✅ T1d 紀錄與逐列入 session：得 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])　期 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])
  ✅ T1e 無變 ⇒ 段三之結果⛔ 存（k6b_stage3_selected ＝ None）、無停機訊息：得 (None, None)　期 (None, None)
  ✅ T1f 無變 ⇒ 真 st 之街角選位⛔ 重跑（恰一）：得 1　期 1
  ✅ T1g 合併再試之輸入：宗地 ＝ 段三之出（此出口 ＝ 原宗地）：得 (True, True)　期 (True, True)
  ✅ T1h 合併再試之輸入：上鎖 ＝ 末一次真 st 街角選位之段一上鎖、街角第 1 宗 ＝ 其 winners、街廓／中心線／退縮／歸戶：得 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})　期 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})
  ✅ T1i alloc_eval 回試算配地之評選（深拷貝）：得 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)
  ✅ T1c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T1c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T1c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T1c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T2a 段三旗標 off 之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  ✅ T2b 合併再試恰一次、段三本體⛔ 呼：得 (1, 0)　期 (1, 0)
  ✅ T2c 有變 ⇒ 回傳之宗地 ＝ 合併再試之出（同一物件）：得 (True, True)　期 (True, True)
  ✅ T2d 紀錄與逐列入 session：得 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])　期 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])
  ✅ T2e 配地所用之宗地 ＝ 合併再試之出（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T2f 所存之結果繫於段三前之宗地與退縮（他 build 或他退縮 ⇒ loud）：得 (('raise', True), ('raise', True))　期 (('raise', True), ('raise', True))
  ✅ T2g 有變 ⇒ 真 st 之街角選位重跑一次、所用 ＝ 合併再試之出：得 (2, True)　期 (2, True)
  ✅ T2h 無停機訊息：得 None　期 None
  ✅ T2c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T2c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T2c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T2c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T3a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  ✅ T3b 段三本體與合併再試各恰一次：得 (1, 1)　期 (1, 1)
  ✅ T3c 段三之試算配地亦 'trial'：得 ['trial']　期 ['trial']
  ✅ T3d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}
  ✅ T3e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (True, True, {'C(1)'})　期 (True, True, {'C(1)'})
  ✅ T3f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T3g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T3h 紀錄入 session：得 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}　期 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}
  ✅ T3i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (2, True)　期 (2, True)
  ✅ T3j 無停機訊息：得 None　期 None
  ✅ T3c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T3c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T3c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T3c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T9a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  ✅ T9b 段三本體與合併再試各恰一次：得 (1, 1)　期 (1, 1)
  ✅ T9c 段三之試算配地亦 'trial'：得 ['trial']　期 ['trial']
  ✅ T9d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}
  ✅ T9e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (True, True, {'C(1)'})　期 (True, True, {'C(1)'})
  ✅ T9f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T9g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T9h 紀錄入 session：得 {'退縮': 3.5, '標的': [], '皆未達': {}}　期 {'退縮': 3.5, '標的': [], '皆未達': {}}
  ✅ T9i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (1, True)　期 (1, True)
  ✅ T9j 無停機訊息：得 None　期 None
  ✅ T9c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T9c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T9c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T9c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T4a 合併再試停機 ⇒ 畫面 st.error ＋ st.stop：得 ('_Stop', True)　期 ('_Stop', True)
  ✅ T4b 停機訊息入 session（含合併再試之原訊息）：得 True　期 True
  ✅ T4c 其後之配地 loud（k6b_stage3_selected raise「請重跑」；k6b_screen_build_for_g ⇒ st.stop）：得 (('raise', True), 'st.stop')　期 (('raise', True), 'st.stop')
  ✅ T4d 前次之紀錄已去、本次⛔ 寫：得 ('<缺>', '<缺>')　期 ('<缺>', '<缺>')
  ✅ T4c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T4c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T4c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T5a 合併再試中斷（KeyError）⇒ 例外上拋：得 'KeyError'　期 'KeyError'
  ✅ T5b 未完成之標記留存（其文含「末端塊合併再試」）：得 True　期 True
  ✅ T5c 其後之配地 loud（k6b_stage3_selected raise「請重跑」）：得 ('raise', True)　期 ('raise', True)
  ✅ T5d 前次之紀錄已去：得 '<缺>'　期 '<缺>'
  ✅ T5c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T5c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T5c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T8a 段三停機 ⇒ st.stop；合併再試⛔ 辦：得 ('_Stop', 0)　期 ('_Stop', 0)
  ✅ T8b 前次之紀錄已去（⛔ 殘留舊紀錄）：得 ('<缺>', '<缺>')　期 ('<缺>', '<缺>')
  ✅ T8c 停機訊息含段三之原訊息：得 True　期 True
  ✅ T8c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T8c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T8c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ TK 試算隔離之鍵含 SS_END_BLOCK_MODE 之值、末項仍 f3_k929_6_log：得 (True, True)　期 (True, True)
  ✅ T6a 注入物之名（四 ＋ blk5）：得 ['a_prime', 'alloc_eval', 'alloc_state', 'blk5', 'trial_winner']　期 ['a_prime', 'alloc_eval', 'alloc_state', 'blk5', 'trial_winner']
  ✅ T6b a′ ＝ a(src) × p(src) ÷ p(dst)（100 × 1000 ÷ 500）：得 200.0　期 200.0
  ✅ T6c 試算選位回 (winner, 真G, 門檻)：得 ('A(1)', 123.45, 100.0)　期 ('A(1)', 123.45, 100.0)
  ✅ T6d 試算配地（alloc_state）之出與其 'trial'：得 ({'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}, ['trial'])　期 ({'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None, 'G': {'A(1)': 0.0}, 'members': {'A(1)': ['A(1)'], 'B(1)': ['B(1)'], 'C(1)': ['C(1)']}, 'pool_out': {}}, ['trial'])
  ✅ T6e 試算配地（alloc_eval）回評選之深拷貝、其 'trial'：得 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False, ['trial'])　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False, ['trial'])
  ✅ T6f 試算配地中止（st.stop）⇒ alloc_eval 拋 RuntimeError：得 'RuntimeError'　期 'RuntimeError'
  ✅ T7a 逐列 ＝ 紀錄之列（值一律字串·None ⇒ —）：得 [{'序': '1', '街廓': 'RB', '端': '右', '候選': 'P(3)', '結果': '成', '檢核': '—'}, {'序': '後處理', '街廓': 'RB', '端': '右', '候選': 'P(4)', '結果': '成', '檢核': '通過'}]　期 [{'序': '1', '街廓': 'RB', '端': '右', '候選': 'P(3)', '結果': '成', '檢核': '—'}, {'序': '後處理', '街廓': 'RB', '端': '右', '候選': 'P(4)', '結果': '成', '檢核': '通過'}]
  ✅ T7b 行內載標的之街廓與端、競合之候選與交面積、皆未達 ⇒ 強制抵費地、退縮：得 []　期 []
  ✅ T7c 無標的 ⇒ 行含「無標的」、逐列空：得 (True, [])　期 (True, [])
  ✅ T7d 試算中止 ⇒ 行含「試算中止」與其訊息：得 (True, True)　期 (True, True)
  ✅ T7e 無紀錄 ⇒ 空：得 {'lines': [], 'rows': []}　期 {'lines': [], 'rows': []}
  ✅ TS 三介面之簽名：得 [(['st'], ['g_kwargs', 'pk_kwargs']), (['st'], ['g_kwargs', 'pk_kwargs']), (['rec', 'log'], [])]　期 [(['st'], ['g_kwargs', 'pk_kwargs']), (['st'], ['g_kwargs', 'pk_kwargs']), (['rec', 'log'], [])]
── P0 判式自驗（期值記錄須全綠；逐項擾動須恰該項紅）──
  ✅ P0 期值記錄全綠 True；逐項擾動恰該項紅 86／86
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9356_screenmerge_wiring.py wiring C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`81.8` s

````text
── 接線與合成案（AST·工作樹之 app.py）──
  ✅ W0 受詞在模組層（缺 []）
  ✅ W1 R-1 三出口（三出口皆經 _end_merge → f3_screen_end_block_merge(st, …)）
  ✅ W2 R-1 單一真相源（end_block_merge_run：呼叫 1（期 1）·在合併再試之入口 1·非呼叫之引用列 []；f3_screen_end_block_merge 之呼叫 1（期 1）·在段三之畫面入口 1）
  ✅ W3 R-5 四注入物之單一真相源（巢狀 ['a_prime', 'alloc_eval', 'alloc_state', 'trial_winner']；回四鍵 True；他處同名 []；段三：['a_prime', 'trial_winner', 'alloc_state']；合併再試：['a_prime', 'alloc_eval', 'alloc_state']）
  ✅ W4 R-3／R-4 試算 'trial'（{'alloc_state': True, 'alloc_eval': True}）
  ✅ W5 R-6 隔離（SS_END_BLOCK_MODE＝'f3_end_block_mode' ∈ 鍵 True；try 前存 True；finally 復 True；K917 ['K917_DROPPED.clear', 'K917_DROPPED.update']）
  ✅ W6 R-7 紀錄（try 後寫 rec True／log True；try 內或其前寫 False；段三之畫面入口之首去 rec True／log True）
  ✅ W7 R-12 失效之二鍵（去 SS_END_BLOCK_MERGE True；去 f3_end_block_merge_log True）
  ✅ W8 R-12 顯示之接線（if 之式 True；end_block_merge_rows(X, …get('f3_end_block_merge_log')) True；位置 True）
  ✅ S1 自誤517 顯示區塊之合成案（三情形皆符）
  ✅ S2 自誤517 失效函式之合成案（未去 []；他鍵留 True；f3_g_needs_rerun True）
── 判別力（每一突變須使其所指之項轉紅）──
  ✅ M1 出口①⛔ 辦合併再試：轉紅 ['W1']（須含 W1）
  ✅ M2 出口③以段三前之宗地辦合併再試：轉紅 ['W1']（須含 W1）
  ✅ M3 以別名呼叫單一真相源：轉紅 ['W2', 'W3', 'W5', 'W6']（須含 W2）
  ✅ M4 合併再試另寫 alloc_eval：轉紅 ['W3']（須含 W3）
  ✅ M5 合併再試之注入物錯位：轉紅 ['W3']（須含 W3）
  ✅ M6 段三之試算配地⛔ 設 'trial'：轉紅 ['W4']（須含 W4）
  ✅ M7 合併再試之試算配地⛔ 設 'trial'：轉紅 ['W4']（須含 W4）
  ✅ M8 試算旗標⛔ 入隔離之鍵：轉紅 ['W5']（須含 W5）
  ✅ M9 合併再試之 finally ⛔ 復原：轉紅 ['W5']（須含 W5）
  ✅ M10 逐列紀錄⛔ 寫：轉紅 ['W6']（須含 W6）
  ✅ M11 段三之畫面入口之首⛔ 去前次之紀錄：轉紅 ['W6']（須含 W6）
  ✅ M12 失效函式⛔ 去紀錄：轉紅 ['W7', 'S2']（須含 S2）
  ✅ M13 顯示⛔ 傳逐列：轉紅 ['W8', 'S1']（須含 S1）
  ✅ M14 顯示⛔ 出逐列表：轉紅 ['S1']（須含 S1）
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9350_frontroad.py selftest C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`36.2` s

````text
── 合成對照（harvest 之 app.py）──
  ✅ S1 全長臨一道路 ⇒ 成功：得 ('成功', ['A'])　期 ('成功', ['A'])
  ✅ S2 無候選 ⇒ 區外：得 ('區外', [])　期 ('區外', [])
  ✅ S3 沿線 30% ⇒ 區外：得 ('區外', [])　期 ('區外', [])
  ✅ S4 沿線恰 50% ⇒ 區外（嚴格大於）：得 ('區外', [])　期 ('區外', [])
  ✅ S5 沿線 50.5% ⇒ 成功：得 ('成功', ['A'])　期 ('成功', ['A'])
  ✅ S6 二候選各過半 ⇒ 歧義（重疊長降冪）：得 ('歧義', ['B2', 'A'])　期 ('歧義', ['B2', 'A'])
  ✅ S7 折線：只臨首段（50／100）⇒ 區外：得 ('區外', [])　期 ('區外', [])
  ✅ S8 折線：臨二段 ⇒ 成功：得 ('成功', ['A'])　期 ('成功', ['A'])
  ✅ S9 候選含自身 ⇒ 排除：得 ('區外', [])　期 ('區外', [])
  ✅ S10 頂點不足 ⇒ loud：得 ('例外', 'ValueError')　期 ('例外', 'ValueError')
  ✅ S11 線長為 0 ⇒ loud：得 ('例外', 'ValueError')　期 ('例外', 'ValueError')
  ✅ I1 推導有值 ⇒ 採推導、使用者所填不採：得 ('RD1', True)　期 ('RD1', True)
  ✅ I2 區外 ⇒ 採正規化後之名稱：得 '中正 路'　期 '中正 路'
  ✅ I3 區外而未填 ⇒ None：得 None　期 None
  ✅ I4 無推導 ⇒ 無正面線：得 ('無正面線', None)　期 ('無正面線', None)
  ✅ I5 全形 ＲＤ１ ⇒ 與推導之 RD1 同組：得 {'RD1': ['P', 'Q'], '中正路': ['R']}　期 {'RD1': ['P', 'Q'], '中正路': ['R']}
  ✅ I6 未填者列入 missing：得 ['R', 'Z']　期 ['R', 'Z']
  ✅ I7 一覽各欄皆字串：得 True　期 True
  ✅ I8 說明句三態：得 (True, True, True)　期 (True, True, True)
── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──
  ✅ M0 未突變之抽出版：紅 []（期 []）
  ✅ M1 `>` → `>=`：轉紅 ['S4 沿線恰 50% ⇒ 區外（嚴格大於）', 'S7 折線：只臨首段（50／100）⇒ 區外']
  ✅ M2 折線改取二端點：轉紅 ['S7 折線：只臨首段（50／100）⇒ 區外']
  ✅ M3 推導有值仍採使用者所填：轉紅 ['I1 推導有值 ⇒ 採推導、使用者所填不採']
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9350_frontroad.py wiring C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`64.4` s

````text
── 接線（AST·app.py ＋ 生產碼他檔 33 檔）──
  ✅ W1 具名常數 R3_FRONT_ROAD_MAJORITY ＝ 0.5、推導之預設引用之、R3 函式內⛔ 字面 0.5（字面 0.5 之列 []）
  ✅ W2a 解析之回傳初值含 'front_road_derive'
  ✅ W2b FRONT_LINE 綁定迴圈內留存全部頂點（_front_pts_chosen[...] ＝ …）
  ✅ W2c result['front_road_derive'] ＝ r3_front_road_derive(_front_pts_chosen, …)
  ✅ W2d 候選集 ＝ 非 _buildable_blocks 之補集
  ✅ W3a main()：st.session_state[SS_FRONT_ROAD_DERIVE] ＝ _cad_layers.get('front_road_derive', …)
  ✅ W3b main()：呼叫 r3_front_road_caption
  ✅ W3c main()：呼叫 r3_front_road_rows
  ✅ W4 消費端：生產碼他檔（33 檔）命中 0；app.py 只在許可之函式內（他檔 {}；app.py 非許可函式 []）
  ✅ W5 畫面路徑之合成案：main() 之一覽區塊與卡片說明句以假 st 實際執行（不符 []）
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 刪推導之賦值：轉紅 ['W2c', 'W2d']
  ✅ N2 main() 改寫他鍵：轉紅 ['W3a']
  ✅ N3 注入 harness 消費者：轉紅 ['W4']
  ✅ N4 一覽只出首列：轉紅 ['W5']
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9367_adj4.py selftest C:\Users\admin\wg384P` ⇒ `rc 0`·`stderr` `0` B·`5.1` s

````text
── 規格步 4 乙（K-9-53 ②·第一趟）之各支 ──
  ✅ K1 旗標：未設／空／' On ' ⇒ True；off／OFF ⇒ False；他值 ⇒ 停機
  ✅ K2 無受詞 ⇒ 回輸入之同一物件、紀錄 []、⛔ 試算；build 片不在 temp ⇒ 停機（受詞為空亦然）
  ✅ K3 整體成：名單首 BA 無其已配得之宗 ⇒ 略過；BB 之受併宗 X1(2)（同原地號）；三片皆併、建地片自 build 去、輸入⛔ 改、build ⊆ temp（同物件）
  ✅ K4 整體不過（BB 之容量 150）⇒ 逐片：建地整筆成、道路片取最大面積（0.01 之格）、公設片未成；剩下續往名單之下一街廓 BD（整體成·受併宗 Z1(1)）
  ✅ K4b 整體不過之列記其由（配餘地不合格）
  ✅ K5 名單盡而有剩下 ⇒ 剩下之列（留於合併單位）；部分併出者之三鍵（段三部分併出·段三餘量）
  ✅ K6 全不容 ⇒ 每街廓整體＋三逐片皆未成、剩下 ＝ 全部；⛔ 改宗地（建地片仍在 build·無鍵·無增）
  ✅ K7 受併宗之序（同街廓有二宗）：① 同原地號居先（距離較遠亦然）② 距離近 ③ 同距離 ⇒ G 大 ④ 同 G ⇒ 重劃前面積大（K-9-67）⑤ 再同 ⇒ 暫編地號小
  ✅ K8 前已有段三之三鍵之片：其剩下 ＝ 段三餘量；全併 ⇒ 段三併出合之、去部分二鍵；部分 ⇒ 段三部分併出合之、段三餘量 ＝ 新剩下
  ✅ K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（程式自我檢查·K-9-57 ⑧·`W-G.9-370` 之訊息）
  ✅ K10 現態之配地中止 ⇒ 停機
  ✅ K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ 共同負擔用地（相異）；無名單 ⇒ 停機；名單重複 ⇒ 停機
  ✅ K12 GB-199：受併宗之序之距離取 slice_geom 之原形（temp 之形縱異亦然）；片之原形缺 ⇒ 停機
  ✅ K13 a′ 折算（K-9-45 二）：併入量 ＝ 來源面積 × p(來源) ÷ p(受併宗)；最大面積之格取來源面積；三鍵之部分併出記來源面積
  ✅ K14 「不影響原位次」：併入使同街廓原保留之宗不保留 ⇒ 不過（整體與逐片皆然）
  ✅ K15 GB-201（手冊先行）：計畫之受併宗於當下之試算未保留 ⇒ 停機（可拆分之片／整筆之建地片）
  ✅ K16 三旗標（WV_ADJ4／WV_K953／WV_K929_6）之任一 off ⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 呼叫 st
  ✅ K17 三旗標之任一其值非法 ⇒ harness 停機；畫面 ⇒ f3_k6b_stage3_error ＝ （第一趟）…、st.error、st.stop、⛔ 寫紀錄
  ✅ K18 adj4_plan：無受詞 ⇒ []；唯公設軌 ⇒ 正面道路之缺以佔位代之、名單依距離；建地軌 ⇒ 停機（正面道路無識別符）
  ✅ K19 adj4_depth_of：取 f3_alloc_depth_by_label（缺 ⇒ {}）；回新 dict
  ✅ K20 adj4_trial_state：摘要 ＋ err ＋ 成員與單元（成員 ≥ 2 者為單元·深拷貝）
  ✅ K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True
  ✅ K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st
  ✅ K23 R-8 之止：整體不過（他街廓之原保留之宗失·非單調之玩具）而逐片皆成 ⇒ 諸片皆無剩下 ⇒ 止於本街廓（⛔ 往名單之次街廓 BD）
  ✅ K24 （K-9-66）T 含建地片之所屬街廓：全數併出使 BA 之 Q1 失 ⇒ 整體與建地之全併皆不過；按比例 59.99（留 build）⇒ 過；道路、公設地未試
  ✅ K25 （K-9-66）同類按比例：建地全入後道路容 190 ⇒ R9 126.67、R1 63.33（各乘 190／300）；列依剩下大者先
  ✅ K26 R-12：併入後之配地中止 ⇒ 不過（記其由）；整體不過 ⇒ 逐片（公設片取最大面積）
  ✅ K27 R-10′（K-9-57 ⑧·程式自我檢查）：同一輪中併入某街廓之前，以當下之試算查其所受之建地片——前一街廓之併入使之已為已配得之宗（依既定機制不會發生·玩具以非單調之回呼造之）⇒ 停機（⛔ 靜默併出）；對照 ⇒ 二街廓皆整體成
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 28／28
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9367_adj4.py wiring C:\Users\admin\wg384P d7a5ea4` ⇒ `rc 0`·`stderr` `0` B·`41.2` s

````text
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K966_CLASSES', 'K966_GRID', '_k929_6_screen_gate', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'end_block_merge_run', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k929_6_fixpoint', 'k953_manual_run', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（620）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
````

`python verify/probes/probe_WG9370_adj4mut.py wiring C:\Users\admin\wg384P 3b35daa` ⇒ `rc 0`·`stderr` `0` B·`17.2` s

````text
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['K966_CLASSES', 'K966_GRID', '_k929_6_screen_gate', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'end_block_merge_run', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k929_6_fixpoint', 'k953_manual_run', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
````

**`V-2` 之 `F27 mutate` 之全文**：

````text
  ✅ N00 —·基準（⛔ 突變）：錨 1 見；所指 []；紅 []
  ✅ N01 K-9-66 ①·整體成而⛔ 回：錨 1 見；所指 ['F27:A3']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K2', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K9', 'F23:K14', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K37', 'F23:K38', 'F23:K39', 'F23:K40', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F24:K13', 'F24:K27', 'F24:K3', 'F24:K4', 'F24:K8', 'F27:A3', 'F27:T1', 'F27:T2', 'F27:T5', 'F27:V2']
  ✅ N02 K-9-66 ②·唯一類者亦以該類之全量再試：錨 1 見；所指 ['F27:A4']；紅 ['F27:A4']
  ✅ N03 K-9-66 ②·類之序反之：錨 1 見；所指 ['F27:A2', 'F27:A6']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21', 'F23:K16', 'F23:K20', 'F23:K23', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F27:A1', 'F27:A2', 'F27:A6', 'F27:A7', 'F28:D3', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S4', 'F28:S6']
  ✅ N04 K-9-66 通知 2·格改 0.1：錨 1 見；所指 ['F27:A5']；紅 ['F23:K15', 'F24:K24', 'F27:A5']
  ✅ N05 K-9-66 ②·按比例之後仍試次類：錨 1 見；所指 ['F27:A1', 'F27:A7']；紅 ['F24:K24', 'F27:A1', 'F27:A7']
  ✅ N06 K-9-66·回傳輸入之態（⛔ 末次通過之態）：錨 1 見；所指 ['F27:A9']；紅 ['F16:K10', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K20', 'F23:K28', 'F24:K13', 'F24:K23', 'F24:K4', 'F24:K5', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N07 K-9-66 ②·二分法之支反之：錨 1 見；所指 ['F27:A1']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N08 K-9-66·要求之類之停機去之：錨 1 見；所指 ['F27:A8']；紅 ['F27:A8']
  ✅ N09 K-9-66 ②·二分法⛔ 記通過之態：錨 1 見；所指 ['F27:A9']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N10 K-9-66 ②·試之量與所記之量不一：錨 1 見；所指 ['F27:A1']；紅 ['F16:K10', 'F16:K10′', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F24:K13', 'F24:K14', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N11 K-9-66 ②·類之全量成而⛔ 承接其態：錨 1 見；所指 ['F27:A2', 'F27:A6']；紅 ['F16:K18', 'F23:K16', 'F23:K20', 'F24:K13', 'F24:K23', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F27:A2', 'F27:A6']
  ✅ N12 K-9-67·去重劃前面積之鍵：錨 1 見；所指 ['F27:C1']；紅 ['F23:K3', 'F23:K51', 'F24:K7', 'F27:C1', 'F27:C2', 'F28:Q1', 'F28:Q2']
  ✅ N13 K-9-67·應分配面積⛔ 以 0.01 ㎡ 量化：錨 1 見；所指 ['F27:C2']；紅 ['F27:C2']
  ✅ N14 K-9-67·重劃前面積之序反之：錨 1 見；所指 ['F27:B1', 'F27:C1']；紅 ['F23:K3', 'F23:K51', 'F24:K7', 'F27:B1', 'F27:C1', 'F27:C2', 'F28:Q1', 'F28:Q2']
  ✅ N15 K-9-67·重劃前面積先於應分配面積：錨 1 見；所指 ['F27:B1']；紅 ['F23:K50', 'F27:B1']
  ✅ N16 K-9-67·成員缺⛔ 取自身：錨 1 見；所指 ['F27:B3']；紅 ['F27:B3']
  ✅ N17 K-9-68·段三：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:U1']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S4', 'F28:S6']
  ✅ N18 K-9-51·段三：第 5 項之候選⛔ 扣已試而未全收之街廓：錨 1 見；所指 ['F27:U2']；紅 ['F16:K17', 'F16:K19', 'F16:K2', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N19 K-9-51·段三：第 5 項之候選之序以 k967_rank 先於距離：錨 1 見；所指 ['F16:K3']；紅 ['F16:K27', 'F16:K3', 'F16:K4', 'F16:K7']
  ✅ N20 K-9-66·段三：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:U1']；紅 ['F27:U1', 'F27:U2']
  ✅ N21 K-9-68·段三：第 5 項之輪之剩下⛔ 減其所併：錨 1 見；所指 ['F16:K2']；紅 ['F16:K10', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K2', 'F16:K21', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K9']
  ✅ N22 R-17″·段三：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L6']；紅 ['F28:D3', 'F28:L6']
  ✅ N23 R-17″·段三：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L1', 'F28:L6']；紅 ['F28:L1', 'F28:L6']
  ✅ N24 R-17″·段三：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L1']；紅 ['F28:D3', 'F28:L1', 'F28:L6']
  ✅ N25 R-19″·段三：第 5 項之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L6']；紅 ['F28:D3', 'F28:L6']
  ✅ N26 K-9-66·段三：試施之受併宗之量⛔ 乘 κ：錨 1 見；所指 ['F16:K10']；紅 ['F16:K10', 'F16:K10′']
  ✅ N27 K-9-68·段三：第 1 輪⛔ 記已試而未全收之街廓：錨 1 見；所指 ['F27:U2']；紅 ['F16:K17', 'F16:K19', 'F16:K2', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N28 R-7 ③·段三：題一 4 之半之片⛔ 入第 5 項之輪：錨 1 見；所指 ['F16:K17']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21']
  ✅ N29 K-9-66·段三：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:U1']；紅 ['F16:K10', 'F16:K10′', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F27:U1', 'F28:D3', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N30 R-7 ②·段三步驟 10：第 1 輪之來源量⛔ 除 κ：錨 1 見；所指 ['F16:K10']；紅 ['F16:K10', 'F16:K10′']
  ✅ N31 R-7 ②·段三步驟 10：非建地之片之剩下⛔ 記：錨 1 見；所指 ['F27:U1']；紅 ['F16:K10′', 'F16:K13', 'F16:K14', 'F16:K14′', 'F16:K4', 'F16:K8', 'F27:U1']
  ✅ N32 R-7 ②·段三步驟 10：剩下⛔ 入第 5 項之輪：錨 1 見；所指 ['F27:U2']；紅 ['F16:K10', 'F16:K11', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K2', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K25', 'F16:K26', 'F16:K27', 'F16:K28', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K32', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:S3', 'F28:S5']
  ✅ N33 K-9-66 R-5 (a)·段三：建地之部分併出⛔ 留 build：錨 1 見；所指 ['F16:K19', 'F16:K7']；紅 ['F16:K19', 'F16:K7', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N34 K-9-68·手冊先行：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:T1']；紅 ['F23:K16', 'F23:K20', 'F23:K23', 'F23:K42', 'F23:K65', 'F24:K15', 'F27:T1', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L2', 'F28:L4']
  ✅ N35 K-9-51·手冊先行：候選⛔ 扣已試而未全收之街廓：錨 1 見；所指 ['F27:T2']；紅 ['F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K42', 'F23:K61', 'F23:K63', 'F23:K65', 'F23:K67', 'F23:K70', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L2', 'F28:L4']
  ✅ N36 K-9-66·手冊先行：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:T1']；紅 ['F27:T1', 'F27:T3', 'F27:T5']
  ✅ N37 K-9-68·手冊先行：K-9-51 之輪之剩下⛔ 減其所併：錨 1 見；所指 ['F27:T1']；紅 ['F23:K14', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K42', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K65', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F27:T1', 'F27:T5']
  ✅ N38 R-17″·手冊先行：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L4']；紅 ['F28:D1', 'F28:L4']
  ✅ N39 R-17″·手冊先行：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L4']；紅 ['F28:L4']
  ✅ N40 R-17″·手冊先行：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L2']；紅 ['F28:D1', 'F28:L2', 'F28:L4']
  ✅ N41 R-19″·手冊先行：K-9-51 之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L4']；紅 ['F28:D1', 'F28:L4']
  ✅ N42 K-9-66 R-5·手冊先行：第 1 輪之來源量⛔ 除 κ：錨 1 見；所指 ['F27:T5']；紅 ['F27:T5']
  ✅ N43 R-18″·手冊先行：趟末之前帳取當下之態：錨 1 見；所指 ['F27:T1']；紅 ['F27:T1', 'F27:T3', 'F27:T5']
  ✅ N44 K-9-66·手冊先行：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:T1']；紅 ['F23:K20', 'F23:K28', 'F23:K33', 'F23:K35', 'F23:K36', 'F23:K37', 'F23:K39', 'F23:K40', 'F24:K15', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L4']
  ✅ N45 K-9-68·第一趟：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K14', 'F24:K23', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K3', 'F24:K4', 'F24:K5', 'F24:K6', 'F27:V1', 'F28:L3']
  ✅ N46 R-17″·第一趟：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L5']；紅 ['F28:D2', 'F28:L5']
  ✅ N47 R-17″·第一趟：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L5']；紅 ['F28:L5']
  ✅ N48 R-17″·第一趟：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L3']；紅 ['F28:D2', 'F28:L3', 'F28:L5']
  ✅ N49 R-19″·第一趟：各輪之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L5']；紅 ['F28:D2', 'F28:L5']
  ✅ N50 K-9-66·第一趟：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:V1']；紅 ['F27:V1']
  ✅ N51 K-9-68·第一趟：剩下⛔ 減其所併（記為 0）：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K6', 'F24:K8', 'F27:V1', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N52 K-9-68·第一趟：受詞每輪沿名單⛔ 止於首一有其宗之街廓：錨 1 見；所指 ['F27:V2']；紅 ['F24:K23', 'F24:K3', 'F24:K4', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N53 K-9-66·第一趟：同類之片之序（剩下大者先）反之：錨 1 見；所指 ['F24:K25']；紅 ['F24:K25']
  ✅ N54 K-9-67·第一趟：受併宗之序去 k967_rank：錨 1 見；所指 ['F24:K7']；紅 ['F24:K7', 'F28:D2', 'F28:L5']
  ✅ N55 R-18″·第一趟：趟末之前帳取當下之態：錨 1 見；所指 ['F27:V1']；紅 ['F27:V1', 'F27:V2']
  ✅ N56 K-9-66·第一趟：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K23', 'F24:K27', 'F24:K3', 'F24:K4', 'F24:K5', 'F27:V1', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N57 K-9-66 通知 3·調配之輸入：建地之部分併出之原有面積⛔ 依剩下之比：錨 1 見；所指 ['F27:W1', 'F27:W2']；紅 ['F27:W1', 'F27:W2', 'F28:I1', 'F28:I2', 'F28:I3']
⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0
````

**`V-2` 之 `F25 mutate` 之全文**：

````text
  ✅ M00 —·基準（⛔ 突變）：錨 1 見；紅 []；所指 []
  ✅ M20 R-12·原保留之宗之判去之：錨 1 見；紅 ['K14', 'K23', 'K24']；所指 ['K14']
  ✅ M21 R-12·配餘地不合格之判去之：錨 1 見；紅 ['K4', 'K4b', 'K5', 'K6', 'K8', 'K13', 'K25']；所指 ['K4b']
  ✅ M23 R-12·併入後之配地中止改為過：錨 1 見；紅 ['K26']；所指 ['K26']
  ✅ M24 R-13·段三併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M25 R-13·段三部分併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M26 R-13·全併⛔ 去部分二鍵：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M27 R-13·段三餘量之值誤：錨 1 見；紅 ['K5', 'K8', 'K13']；所指 ['K8']
  ✅ M30 R-16·GB-201 之判恆過：錨 1 見；紅 ['K15']；所指 ['K15']
⇒ 突變 8（另基準一）；紅 []；rc 0
````

**`V-3`／`V-4`／`V-5`／`V-6` 之比對之出艙**（`<O>\tools\v456.py`·`V-5` 之正規化 ＝ 施前之檔以 `b47efbc` 之全 `40` 碼、施後之檔以 `8ce1a18` 之全 `40` 碼各代以同一字樣 `<HEAD>` 後逐位比；`raw_equal False` 即「⛔ 代之則相異」之對照）：

````text
== V-3 blobs of 7 probes
probe_WG9350_frontroad 5689c92ed891c95b09f5450ad3c443383b4f6ce1
probe_WG9355_screenmerge 776cddce3b0ec99468ce1a6c33cc71deb5241d57
probe_WG9356_screenmerge_wiring f38120402ece474a69dcbdfdc726a2d14347a4a2
probe_WG9357_k948 e5a867a2eede82090e5889842d450a026481e139
probe_WG9363_k953 abe2f7fabe818bda5b71ef41a8b59aa3335be85b
probe_WG9367_adj4 2992e4ff721e642b913bd86416177daad6ae2271
probe_WG9370_adj4mut 396bdcf6368be58119e812ba2885d6c3ab56bde7
== V-4 k6s3 cmp
35 rc 0 stderr 0 | last: 相異 0 項 ⇒ ✅ 同
00 rc 0 stderr 0 | last: 相異 0 項 ⇒ ✅ 同
== V-5 parity normalized compare
35 json raw_equal False | pre_head_count 1 post_head_count 1 | normalized_equal True | bytes 9216 9216
35 stdout raw_equal False | pre_head_count 1 post_head_count 1 | normalized_equal True | bytes 1612 1612
  post json keys ['Z', 'bad', 'head', 'mode', 'n_rows', 'perturb', 's3_ret_keys', 'sb', 'stage3_log'] head 8ce1a1828ee8b0a9991d05c91ef3b48c06fee401
00 json raw_equal False | pre_head_count 1 post_head_count 1 | normalized_equal True | bytes 308 308
00 stdout raw_equal False | pre_head_count 1 post_head_count 1 | normalized_equal True | bytes 1610 1610
  post json keys ['Z', 'bad', 'head', 'mode', 'n_rows', 'perturb', 's3_ret_keys', 'sb', 'stage3_log'] head 8ce1a1828ee8b0a9991d05c91ef3b48c06fee401
== V-6 f8 hash-object
35 ['6b0d558fc16e581a92c8a6fc6db95561bfa70b53', '6b0d558fc16e581a92c8a6fc6db95561bfa70b53'] equal True
00 ['8daf7e0e4d71dd7863e0ab45ec5820930863e8aa', '8daf7e0e4d71dd7863e0ab45ec5820930863e8aa'] equal True
````

🔧 `F8 run` 之落檔之 blob（`3.5 m` `6b0d558f…`、`0 m` `8daf7e0e…`）與 `§一` 項 `5` 之發單側之值（`8be0160b…`／`6fb86647…`·本機 Linux）相異——`V-6` 之判準（施前 ＝ 施後）全符；其異係平台之落檔（本機 Windows），⛔ 涉本單之碼（施前之落檔亦同此值）。

**`V-8`**（`C:\Users\admin\wg384P`·`git grep -c -F "<字樣>" -- <檔>`）：

````text
[def k971_key5] app.py:1
rc=0
[def k971_blk5] app.py:1
rc=0
[未給五級之屬性] app.py:2
rc=0
[K-9-51（剩餘土地·距離近者先）] rc=1
[contests=None)] app.py:1
rc=0
[contests=(_ct or None))] app.py:1
rc=0
[正面道路無識別符] app.py:1
rc=0
[blk5=callbacks['blk5']] verify/selection_pipeline.py:2
rc=0
[blk5=_cbk['blk5']] verify/selection_pipeline.py:1
rc=0
[試算中止] verify/selection_pipeline.py:1
rc=0
````

**`F23 run`／`F16 run`／`F29 run` 之末十四列**：

`F23_run`（`rc 0`）

````text
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.47／ΣG 之變 2934.53（和 ≤ 0.1）True
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.83／ΣG 之變 3663.88（和 ≤ 0.1）True
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

`F16_run`（`rc 0`）

````text
  ✅ R1@3.5：保留集 harness ＝ 畫面 True（28 宗）；G 之鍵 ＝ 保留集 True；逐宗差 max 0.0（≤ 0.01）True
  ✅ R2@3.5：段三紀錄 19 列 ＝ 開工態 True；新鍵之片 []；新結果 []
  ✅ R1@0.0：保留集 harness ＝ 畫面 True（29 宗）；G 之鍵 ＝ 保留集 True；逐宗差 max 0.0（≤ 0.01）True
  ✅ R2@0.0：段三紀錄 0 列 ＝ 開工態 True；新鍵之片 []；新結果 []
⇒ 紅 []；rc 0
````

`F29_run`（`rc 0`）

````text
  ✅ R1@3.5：build 51 宗·單元 7 ＝ 本器所載 True
  ✅ R2@3.5：配地 28 宗·不配地 21 宗 ＝ 本器所載 True
  ✅ R3@3.5：入池閘之紀錄 7 列 ＝ 本器所載 True
  ✅ R1@0.0：build 52 宗·單元 6 ＝ 本器所載 True
  ✅ R2@0.0：配地 29 宗·不配地 21 宗 ＝ 本器所載 True
  ✅ R3@0.0：入池閘之紀錄 6 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

**`k6s3 cmp` 之全文**：

`35`

````text
相異 0 項 ⇒ ✅ 同
````

`00`

````text
相異 0 項 ⇒ ✅ 同
````

**`parity` 之末十五列**：

`parity35`（`rc 0`）

````text
  ✅ 段三 session 鍵 f3_k6b_stage3_log（19 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（13 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 3.5, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（37 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（45／45）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

`parity00`（`rc 0`）

````text
  ✅ 段三 session 鍵 f3_k6b_stage3_log（0 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（0 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 0.0, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（46 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（46／46）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

### ③-3 `52` 呼叫（＋前置 `3` 之六呼叫）之 `rc`／`stderr`／耗時／末列

並行：重器（單首 🔑「並行之限」所列者）同時 ≤ `2`、他器 ≤ `6`（`<O>\tools\runner.py`）。末列 ＝ `stdout` 之末一非空列（去行尾之 `\r`）。

| # | 呼叫 | 前置（`b47efbc`）rc／stderr B／s | 前置之末列 | 驗（`8ce1a18`）rc／stderr B／s | 驗之末列 |
|---|---|---|---|---|---|
| `1` | `python verify/probes/probe_WG9363_k953.py selftest <repo>` | `1`／`0`／`8.4` | `⇒ 紅 ['K61', 'K62', 'K63', 'K64', 'K65', 'K66', 'K67', 'K68', 'K70', 'K72', 'K73', 'K74']；r…` | `0`／`0`／`6.3` | `⇒ 紅 []；rc 0` |
| `2` | `python verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `1`／`0`／`59.1` | `⇒ 紅 ['W1', 'W9']；rc 1` | `0`／`0`／`44.2` | `⇒ 紅 []；rc 0` |
| `3` | `python verify/probes/probe_WG9357_k948.py selftest <repo>` | `1`／`0`／`7.9` | `⇒ 紅 ['K23', 'K24', 'K25', 'K26', 'K27', 'K28', 'K29', 'K30', 'K31', 'K32']；rc 1` | `0`／`0`／`6.1` | `⇒ 紅 []；rc 0` |
| `4` | `python verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `1`／`0`／`7.7` | `⇒ 紅 ['T6a']；rc 1` | `0`／`0`／`5.6` | `⇒ 紅 []；rc 0` |
| `5` | `python verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `1`／`0`／`8.2` | `⇒ 紅 ['W3']；rc 1` | `0`／`0`／`81.8` | `⇒ 紅 []；rc 0` |
| `6` | `python verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`44.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`36.2` | `⇒ 紅 []；rc 0` |
| `7` | `python verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`79.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`64.4` | `⇒ 紅 []；rc 0` |
| `8` | `python verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`7.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`5.1` | `⇒ 紅 []；rc 0` |
| `9` | `python verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`59.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`41.2` | `⇒ 紅 []；rc 0` |
| `10` | `python verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`21.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`17.2` | `⇒ 紅 []；rc 0` |
| `11` | `python verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`6.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`5.5` | `⇒ 紅 []；rc 0` |
| `12` | `python verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`4.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`3.4` | `⇒ 紅 []；rc 0` |
| `13` | `python verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`147.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`105.5` | `⇒ 紅 []；rc 0` |
| `14` | `python verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`1162.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`563.5` | `⇒ 紅 []；rc 0` |
| `15` | `python verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`1420.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`718.6` | `⇒ 紅 []；rc 0` |
| `16` | `python verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`24.6` | `⇒ 突變 8（另基準一）；紅 []；rc 0` | `0`／`0`／`20.2` | `⇒ 突變 8（另基準一）；紅 []；rc 0` |
| `17` | `python verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`6.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.9` | `⇒ 紅 []；rc 0` |
| `18` | `python verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`16.3` | `⇒ 紅 []；rc 0` | `0`／`0`／`13.4` | `⇒ 紅 []；rc 0` |
| `19` | `python verify/probes/probe_WG9373_k966.py mutate <repo>` | `3`／`0`／`162.5` | `⇒ 突變 57（另基準一）；紅 []；無從判定 ['N00']；rc 3` | `0`／`0`／`139.6` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` |
| `20` | `python verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`612.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`426.7` | `⇒ 紅 []；rc 0` |
| `21` | `python verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`7.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.9` | `⇒ 紅 []；rc 0` |
| `22` | `python verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`2064.3` | `⇒ 紅 []；rc 0` | `0`／`0`／`1756.3` | `⇒ 紅 []；rc 0` |
| `23` | `python verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`105.8` | `⇒ 紅 []；rc 0` | `0`／`0`／`88.1` | `⇒ 紅 []；rc 0` |
| `24` | `python verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`6.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.7` | `⇒ 紅 []；rc 0` |
| `25` | `python verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`24.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`20.2` | `⇒ 紅 []；rc 0` |
| `26` | `python verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`64.1` | `⇒ rc 0（不符 0·器紅 0）` | `0`／`0`／`52.6` | `⇒ rc 0（不符 0·器紅 0）` |
| `27` | `python verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`5.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.1` | `⇒ 紅 []；rc 0` |
| `28` | `python verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`29.3` | `⇒ 紅 []；rc 0` | `0`／`0`／`25.0` | `⇒ 紅 []；rc 0` |
| `29` | `python verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`75.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`61.8` | `⇒ 紅 []；rc 0` |
| `30` | `python verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`504.9` | `⇒ 紅 []；rc 0` | `0`／`0`／`350.5` | `⇒ 紅 []；rc 0` |
| `31` | `python verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／`44.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`36.9` | `⇒ 紅 []；rc 0` |
| `32` | `python verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`166.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`132.5` | `⇒ 紅 []；rc 0` |
| `33` | `python verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`38.7` | `⇒ 紅 []；rc 0` | `0`／`0`／`32.9` | `⇒ 紅 []；rc 0` |
| `34` | `python verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`114.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`89.1` | `⇒ 紅 []；rc 0` |
| `35` | `python verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`81.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`65.9` | `⇒ 紅 []；rc 0` |
| `36` | `python verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`70.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`60.9` | `⇒ 紅 []；rc 0` |
| `37` | `python verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`195.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`191.6` | `⇒ 紅 []；rc 0` |
| `38` | `python verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`5.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` |
| `39` | `python verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`47.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`39.3` | `⇒ 紅 []；rc 0` |
| `40` | `python verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`516.0` | `⇒ 紅 []；rc 0` | `0`／`0`／`497.7` | `⇒ 紅 []；rc 0` |
| `41` | `python verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`5.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.4` | `⇒ 紅 []；rc 0` |
| `42` | `python verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`4.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`3.4` | `⇒ 紅 []；rc 0` |
| `43` | `python verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`157.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`155.5` | `⇒ 紅 []；rc 0` |
| `44` | `python verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`353.3` | `⇒ 紅 []；rc 0` | `0`／`0`／`355.1` | `⇒ 紅 []；rc 0` |
| `45` | `python verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`5.4` | `⇒ 紅 []；rc 0` | `0`／`0`／`4.5` | `⇒ 紅 []；rc 0` |
| `46` | `python verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`352.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`356.3` | `⇒ 紅 []；rc 0` |
| `47` | `python verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`0.1` | `selftest 9/9 ⇒ ✅` | `0`／`0`／`0.1` | `selftest 9/9 ⇒ ✅` |
| `48` | `python verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`0.1` | `selftest 13/13 ⇒ ✅` | `0`／`0`／`0.1` | `selftest 13/13 ⇒ ✅` |
| `49` | `python verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`9.5` | `⇒ 紅 []；rc 0` | `0`／`0`／`8.4` | `⇒ 紅 []；rc 0` |
| `50` | `python verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`4.6` | `ε ＝ 0.0002｜rc 0` | `0`／`0`／`4.5` | `ε ＝ 0.0002｜rc 0` |
| `51` | `python verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`51.4` | `紅項 [] 器紅 0` | `0`／`0`／`35.6` | `紅項 [] 器紅 0` |
| `52` | `python verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`366.1` | `⇒ 紅 []；rc 0` | `0`／`0`／`362.6` | `⇒ 紅 []；rc 0` |
| `53` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on C:\Users\admin\wg384O\post\k6s3_post_35.json` | `0`／`0`／`206.8` | `{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_en…` | `0`／`0`／`217.3` | `{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_en…` |
| `54` | `python verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on C:\Users\admin\wg384O\post\k6s3_post_00.json` | `0`／`0`／`148.6` | `{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_en…` | `0`／`0`／`161.2` | `{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_en…` |
| `55` | `python verify/probes/probe_WG9349_k9296.py run <repo> 3.5 C:\Users\admin\wg384O\post\f8_post_35.json` | `0`／`0`／`210.2` | `⇒ 紅 []；rc 0` | `0`／`0`／`210.2` | `⇒ 紅 []；rc 0` |
| `56` | `python verify/probes/probe_WG9349_k9296.py run <repo> 0.0 C:\Users\admin\wg384O\post\f8_post_00.json` | `0`／`0`／`151.6` | `⇒ 紅 []；rc 0` | `0`／`0`／`148.5` | `⇒ 紅 []；rc 0` |
| `57` | `python verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on C:\Users\admin\wg384O\post\parity35_post.json` | `0`／`0`／`457.4` | `⇒ rc 0（不符 0 項）` | `0`／`0`／`462.6` | `⇒ rc 0（不符 0 項）` |
| `58` | `python verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on C:\Users\admin\wg384O\post\parity00_post.json` | `0`／`0`／`321.6` | `⇒ rc 0（不符 0 項）` | `0`／`0`／`326.6` | `⇒ rc 0（不符 0 項）` |

合計：前置 `58` 呼叫·`stderr` `0` B·耗時之和 `10839.1` s；驗 `58` 呼叫·`stderr` `0` B·耗時之和 `8645.8` s（`52` 呼叫之和 ＝ `7119.4` s）。`k6s3 run` 之末列為其 JSON 摘要（截 90 字）。

## ④ 塊之實得與三簿

| 塊 | bytes | `sha256` | 列 | 抽取（標題列·圍欄開列·閉列） |
|---|---|---|---|---|
| `Fy34` | `46859` | `81f226d08f34062f06b13002c217897fb23c6f92e0e0aca257f8984035edc914` | `657` | `:251`·`:253`·`:911` |
| `K24` | `10586` | `4877110c41cef76e73c7383b4b63e4d991ff5bd6edb9f8cdbe7afb67af1d5939` | `74` | `:913`·`:915`·`:990` |
| `E27` | `2427` | `fdb529d57d1fb06c2bdc51111b98a53f63278472e79910099dcfd330b18b0ba0` | `13` | `:992`·`:994`·`:1008` |
| `P37` | `4044` | `2ef301c41dc215f1830ede09320fb1fb4a2850cf2a6273a1d26fa7308037928f` | `25` | `:1010`·`:1012`·`:1038` |
| `CK`（`W-G.9-365_輕量單.md` 附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | `:805`·`:807`·`:839` |
| `GF`（同 附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | `:753`·`:755`·`:803` |

皆 ＝ `§五-1` 項 `2`／`4`／`7`。

`Fy34` 之 `7` 器（施前 blob → 施後 blob·B）：

| 器 | 施前 | 施後 | 增／刪 |
|---|---|---|---|
| `probe_WG9350_frontroad.py` | `20580605…`（`25272`） | `5689c92e…`（`25956`） | `5`／`0` |
| `probe_WG9355_screenmerge.py` | `413978d7…`（`37500`） | `776cddce…`（`38127`） | `8`／`3` |
| `probe_WG9356_screenmerge_wiring.py` | `c489e887…`（`30405`） | `f3812040…`（`30819`） | `5`／`1` |
| `probe_WG9357_k948.py` | `5efb835e…`（`41687`） | `e5a867a2…`（`50175`） | `141`／`3` |
| `probe_WG9363_k953.py` | `083e8a0b…`（`108036`） | `abe2f7fa…`（`125317`） | `221`／`4` |
| `probe_WG9367_adj4.py` | `903249f3…`（`71535`） | `2992e4ff…`（`72408`） | `9`／`1` |
| `probe_WG9370_adj4mut.py` | `b6a65f26…`（`19070`） | `396bdcf6…`（`19733`） | `6`／`0` |

三簿（工項三·二進位附加·改前全檔為改後之嚴格前綴·其尾 ＝ 塊）：

| 簿 | 改前 B | 改後 B | 改後 blob | 增／刪 |
|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `790469` | `801055` | `78a4892a810b81d516ea176f3dfb85b38de47775` | `74`／`0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1194351` | `1196778` | `3f06cffaccc5db2a1be036bd2815941c91e920ed` | `13`／`0` |
| `CLAUDE.md` | `404646` | `408690` | `d1b1a1f2a6ee56fcdb7c9f65fd288be38b73e86c` | `25`／`0` |

## ⑤ 推送之目標與推後之 heads

四推（工項零〜三）之目標皆 `verify/W-G.9-384-k971`；皆首推即成（工項零 `* [new branch]`；其後皆快轉）；⛔ `--force`。工項零之推後：`git ls-remote --heads origin` ＝ `44` 列；`refs/heads/verify/W-G.9-384-k971` ＝ `288a0d5…`、`refs/heads/wip/s1-endpart` ＝ `fffa397…`。工項三之推後：新側支 ＝ `d358f218ec3662f96106341ed9e037f840e729a1`、主線 ＝ `fffa397…`。工項四之推後之全列見收工閘 `5`（對話）。

## ⑥ 自捕與自解；唯讀獨立審查

### ⑥-1 CC 之自捕

1. **跑器之出艙之編碼**（零土地後果）：初版之跑器（`<O>\tools\runner.py`）以主控台之 cp950 印逐呼叫之摘要，遇 emoji 之末列即拋 `UnicodeEncodeError`，其 `rc` 之紀錄隨之失（器之 log 仍在）。⇒ 以 `Win32_Process` 終止其行程樹（子 python 二·`TaskStop` 留孤兒之戒），清 `<O>\pre`，跑器改 `sys.stdout.reconfigure(encoding='utf-8')` 並逐呼叫另落 `*.rc.json`，**前置之 `58` 呼叫全數重跑**（③ 所載皆重跑之值）。初跑之 `C:\Users\admin\wg384W` 之 `git status --porcelain` 前後皆空。
2. **`W8`／`W7` 之錨**（撰碼中自跑·⛔ 改器）：初稿之 `k971_key5` 以 `_wide` 為變數名 ⇒ `F23 wiring` 之 `W8`、`F24 wiring` 之 `W7` 紅，`錨之異 [('wide', 5)]`——某器之字串常數 `'wide'` 於基準之 `app.py` 恰一見（子字串計）。⇒ 改名 `_wstep`（`app.py` 之 `wide` 之列數 ＝ `fffa397` 之 `1`），二者轉綠。屬 `§三-3` 之 `2` 之同類（發單側之原型所遇者之外之一例·其字面未載於單）。
3. **來源檔取自第二處**（施工樹之根無之）·KL 之訊未載 bytes／`sha256` ⇒ 以 `SELF_SHA256` 為據（②）。
4. **器之 log 之行尾**：本機 Windows 之文字模式之 `stdout` ⇒ 諸 log 之列尾帶 `\r`；末列之比對皆先去之（③-3）。本報告所嵌之出艙皆已去 `\r`（本檔 CR `0`）。

### ⑥-2 唯讀獨立審查（附則丙·驗皆符後、推前）

審查者 ＝ 另派之子代理（`redistribution-reviewer`·唯讀·⛔ 改檔、⛔ `commit`·暫存寫 `<O>\review\`）；受詞 ＝ `C:\Users\admin\wg384P`（`8ce1a18`）之全文差異（自倉重產·與 `<O>\app_diff.diff` `cmp` 逐位同）與 `§三`、附錄乙之三。審畢 `git status --short` ＝ `0` 列、`HEAD` 仍 `8ce1a18`。

**結論**：十條（`R-1`〜`R-9`·專審諸點·他瑕）皆**符**；(甲) 純實作之瑕 `0`；(乙) 涉域上判斷或規格之漏載 `0`；(丙) 無害之觀察 `9`。審查者之獨立復現：`py_compile` `rc 0`；`V-1` 十呼叫皆 `rc 0`（`F23` `P0 74／74`、`F16` `P0 35／35`、`W1`〜`W9` ✅）；`F27 mutate` `57` 皆捕；`k6s3 run` 二退縮自跑與施前 `cmp` 皆 `相異 0 項`；`parity` 之正規化之比與其對照；`F8` 之 `hash-object`；頂層 AST。`R-1` 另以隨機之合成案三種子逐對 `4285` 組比 `k971_key5` 與 `adj_candidate_lists` 之鍵之前六（值、型、`repr`）⇒ 相異 `0`；負對照（`r2` 之向改之）⇒ `534`。突變：「相異街廓數」改「候選之數」⇒ `F16` `K26`／`F23` `K70` 紅；鍵內讀 `len(_cands)`（`list.sort` 中暫空）⇒ `F16` 多項紅（實作先算 `_ob384`／`_ob953` 而避之）。未獨立復現者：`V-2` 之其餘約 `38` 呼叫（唯讀實作者之 `post\*.rc.json`）。

(丙) 九項（逐條·處置）：

1. 段三之 `_bk384`（`{_p: str(_b) for _b, _p in _pre}`）隱含「同一宗於 `_cur["kept"]` 唯屬一街廓」——既有之 `alloc_state` 之 `G` 已以宗為單鍵，本改⛔ 新增其假設。處置：⛔ 改。
2. **量測器之覆蓋之缺**（發單側之事）：於倉外之副本令手冊先行之**道路之片**亦再排（`!= 'pub'`）⇒ `F23 selftest` 仍綠；段三之同突變 ⇒ `F16` `K21` 紅；手冊先行令公設亦再排 ⇒ `F23` `K42` 紅。碼之讀（唯 `'bld'` 再排）正確；`F23` 於「手冊先行之道路之片⛔ 再排」無判別力。處置：⛔ 改器（停機款 `10`）；呈發單側（擬於後單補其例）。
3. harness 之 `blk5` 之最小建築面積 ＝ `{}`（⇒ `r2` 恆 `(0, 0)`），畫面取 session 之 `K91_SS_MBA_EFFECTIVE`——照 `run_adj4`（附錄乙之丙明文）；`K-9-71` 於某案觸發且街廓間最小建築面積相異時，畫面與 harness 之序可異；本案⛔ 觸（`R-10`）。屬既有之結構之差之延伸。處置：⛔ 改；呈發單側知悉。
4. harness 用 `cad.get("front_road_derive") or {}`（規格 `R-6` 之字面）、`run_adj4` 用 `cad["front_road_derive"] or {}`——唯鍵缺時停機之形異（`KeyError` 與「無識別符」之停機），皆停機。處置：照規格之字面。
5. 既有 docstring 之摘要句（二回呼之「回 `{'a_prime', 'trial_winner', 'alloc_state', 'alloc_eval'}`」）與 `_p5_373`、手冊先行之 `K-9-51` 段之既有之註（「距離 → …」）已不完整——規格禁改既有之文，新款已載「不再適用」。處置：⛔ 改。
6. `k971_blk5` 以 `F3_CATEGORY_BURDEN[...]` 直取，分類未知 ⇒ `KeyError`（非 `RuntimeError`）——與 `adj4_plan` 同形（「所呼之函式之停機照拋」）。處置：⛔ 改。
7. `k6b_stage3_run` 之新款之「⛔ 須比者⛔ 呼之」係簡寫（＝ 不須比者不呼），⛔ 涉行為。處置：⛔ 改（commit 已成·其後之改即另一生產碼之 commit）。
8. `f3_screen_k953` 多呼一次 `k6b_screen_callbacks` 以取 `blk5`——其建構唯讀 `pk_kwargs`／`g_kwargs`、⛔ 寫 session。處置：規格 `R-7` 之明文之形。
9. 「相異街廓數」與「候選數」之分，段三與手冊先行皆為量測器所捕（`F16` `K26`／`F23` `K70`）。處置：無。

## ⑦ 設計說明（`§三-5`）

**逐條**（行號為 `8ce1a18` 之 `app.py`／`verify/selection_pipeline.py`·僅供本報告之時點）：

- **`R-1`** `k971_key5(blk_ctx, home, t, tol=ADJ_DEPTH_TIE_TOL_M)`：新頂層，置於 `adj_candidate_lists` 之後、`adj_candidate_rows` 之前。級 ＝ `blk_ctx` 全部街廓之最小建築面積之相異值之升序（`_lv_mba`）、正面路寬之相異值之降序（`_lv_wid`）；`_up` ＝ 候選之級 − 原之級（`> 0` ⇒ `(1, _up)`、否則 `(0, −_up)` ＝ `adj_candidate_lists` 之 `(0, _i2 − _j2) if _j2 <= _i2 else (1, _j2 − _i2)`）；`_wstep` ＝ 原之級 − 候選之級（`> 0` 即往寬 ⇒ `(1, _wstep)`、否則 `(0, −_wstep)` ＝ `(0, _j5 − _i5) if _j5 >= _i5 else (1, _i5 − _j5)`）；`r1`／`r3`／`r4` ＝ `int(相異)`（`0`／`1`）；`r6` ＝ `Decimal(repr(float(tol)))` 之容差、`(0, Decimal('0'))`／`(0, −Δ)`／`(1, Δ)`。`home` 或 `t` 不在表 ⇒ `RuntimeError`（「… 無五級之屬性（不在調配之名單之街廓屬性之表）⇒ 停機」）。⛔ 淘汰。字樣：`def k971_key5` `1`。
- **`R-2`** `k971_blk5(...)`：新頂層，置於 `k971_key5` 之後；可建築街廓 ＝ `F3_CATEGORY_BURDEN[category] == ADJ_BURDEN_BUILD`（原序）；正面道路 ＝ `r3_front_road_identifier(<label 之列>, front_derive_by or {}, front_name_by or {})` 之各 `['id']`（⛔ 佔位）；回 `adj_block_ctx(<label 之列>, {label: category}, eff_min_build_by or {}, {label: id}, {label: (width_by or {}).get(label)}, depth_by or {})`——與 `adj4_plan` 之 `_attr_a4` 同式（變數名皆異·避錨）。字樣：`def k971_blk5` `1`。
- **`R-3`** `k6b_stage3_run`：① 簽名 `*, log_print=print, blk5=None, contests=None`；② `_p5_373` 之前立 `_b5s384 = []` 與巢狀 `_b5_384()`（首次 ⇒ `blk5 is None` ⇒ `RuntimeError`「… 建地之片之他街廓之候選二以上而未給五級之屬性（blk5）——候選之序無從定之 ⇒ 停機」；`blk5()` 之回非 `dict` ⇒「… 五級之屬性非 dict（<型>）⇒ 停機」；存於 `_b5s384`，同一次之段三之內共用·`_p5_373` 多次之呼叫亦共用）；③ 既有之 `_cands.sort(key=lambda c_: c_[0])` 之後、`_seq[x] = _cands` 之前：`_kind(x) == 'bld' and _cands` ⇒ `_bk384 = {_p: str(_b) for _b, _p in _pre}`（候選之街廓·`_cands` 之元一一取自 `_pre`）、`_ob384` ＝ 他街廓之相異街廓之集（先算·`list.sort` 中串列暫空）；以 `list.sort`（穩定）再排，鍵 ＝ 本街廓（`_bk384[...] == _blk_of[x]`）⇒ `(0,)`；否則 `len(_ob384) >= 2` ⇒ `(1, k971_key5(_b5_384(), _blk_of[x], <候選之街廓>))`、否則 `(1,)`（條件式惰性·唯 `≥ 2` 支呼 `_b5_384`）。他⛔ 變。
- **`R-4`** `end_block_merge_run`：簽名 `*, setback=None, log_print=print, blk5=None`；呼段三處增獨立之一列 `blk5=blk5,`（附註）於 `contests=(_ct or None))` 之列之前（該列一字未動）。
- **`R-5`** `k953_manual_run`：① 簽名 `*, log_print=print, blk5=None`；② `_why951` 之後立 `_b5s953` 與 `_b5953()`（訊息冠 `_hdr953` ＋「·K-9-51 …未給五級之屬性（blk5）…」／「·K-9-51 五級之屬性非 dict …」）；③ 既有之 `_list.sort(key=lambda _t: _t[0])` 之後、`_seq953[_x] = _list` 之前：`_sort953(_tin953[_x]) == 'bld' and _list` ⇒ `_ob953 = {_t[2] for _t in _list if _t[2] != _blk953[_x]}`，再排之鍵同 `R-3` ③（候選之街廓 ＝ `_t[2]` ＝ `str(_bk)`）；④ `_why951 = 'K-9-51／K-9-71（剩餘土地·本街廓先·建地之他街廓依五級 → 距離）'`。
- **`R-6`** 畫面 `k6b_screen_callbacks`：本體之頂層增 `def blk5():`，其內 `_rn384 = _ss.get(SS_FRONT_ROAD_NAME, {}) or {}`，回 `k971_blk5(g_kwargs['classified_blocks'], _ss.get(K91_SS_MBA_EFFECTIVE, {}) or {}, _ss.get(SS_FRONT_ROAD_DERIVE, {}) or {}, {cb['label']: _rn384.get(cb.get('id'), '') for cb in g_kwargs['classified_blocks']}, {cr['街廓']: cr.get('正面路寬(m)') for cr in pk_kwargs['_corner_rows_init']}, adj4_depth_of(st.session_state))`；回之 dict 增 `'blk5': blk5`。harness `_k6b_callbacks`：增 `def blk5():`（`import run_verification`），回 `ns["k971_blk5"](cb, {}, cad.get("front_road_derive") or {}, run_verification.load_front_road_names(), {r["街廓"]: r.get("正面路寬(m)") for r in param_rows}, ns["adj4_depth_of"](fake_st.session_state))`；回之 dict 增 `'blk5': blk5`。皆於呼叫時取之。
- **`R-7`** 六入口：畫面 `f3_screen_k6b_stage3` ⇒ `…, log_print=_unhandled.append, blk5=_cb['blk5'])`；`f3_screen_end_block_merge` ⇒ `…, log_print=_unhandled.append, blk5=_cb['blk5'])`；`f3_screen_k953` ⇒ 新增之列 `_b5953s = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)['blk5']`（`_a953s` 之列之次·該列⛔ 改）、`…, _a953s, _trial953s, blk5=_b5953s)`；harness `run_corner_pk_k6b` ⇒ `_cbk['alloc_state'], blk5=_cbk['blk5'])`；`run_end_block_merge` ⇒ `…, setback=setback, blk5=callbacks['blk5'])`；`run_k953` ⇒ `…, _trial_k, blk5=callbacks['blk5'])`。皆附於呼叫之末。
- **`R-8`** docstring：`k6b_stage3_run`、`end_block_merge_run`、`k953_manual_run`、`k6b_screen_callbacks`、`_k6b_callbacks` 之末各增一款（``🔧 `W-G.9-384` `` 起首）；段三之款載「上文「距離 → `k967_rank`」於建地之片之他街廓之候選不再適用」、手冊先行之款載「上文「距離 → 本街廓者先」於建地之片之他街廓之候選不再適用」。改處之註皆同起首。既有之 docstring 與註一字未改（唯其末之 `"""` 隨新款移後）。
- **`R-9`** 見 `V-8`。

**對 `§三-3` 各款之自查**：
1. 突變之錨：`_cands.append(((_d, k967_rank(…`、`_cands.sort(key=lambda c_: c_[0])`、`_list.append(((_dv, …`、`_list.sort(key=lambda _t: _t[0])`、`_rnd953`、`_try953k`、`_seq953`、趟末之帳、`adj_candidate_lists` 之八鍵之式皆一字未動（再排附於既有之排序之後；`R-1` 以他名、他式書之）；`F27 mutate` `57` 皆捕、`無從判定 []`；`F19 mut`、`F22 mut`、`F25 mutate` 皆綠。
2. 量測器之字樣之錨：`contests=None)`（`R-3` ① 之序·`blk5` 於前）、`contests=(_ct or None))`（`R-4` 之獨立之列）、`正面道路無識別符`（新書之文⛔ 書之）皆仍 `1`；`adj_candidate_lists` 之 `_r2`／`_r3`／`_r5` 之列⛔ 複製；另遇 `'wide'`（⑥-1 之 `2`）而改名避之。`F23 wiring` `W8`、`F24 wiring` `W7` 綠。
3. 頂層之新名唯 `k971_key5`、`k971_blk5`（`V-7`）。
4. `F17 wiring`、`F25 wiring` 之 `X3`／`X5`、`F10 wiring` 之 `W4`、`F27 wiring` `Y1`〜`Y9`、`F29 wiring` `Y1`〜`Y11`、`F14`／`F15`／`F9` 之接線之項皆綠。

**附則乙之自查**：`R-1` 之式與 `adj_candidate_lists` 之八鍵之前六之同 ＝ `F23` `K68` 之實得 `(126, 0)`（✅·審查者另以 `4285` 組逐對 `0` 相異）；`R-3`／`R-5` 之再排之置處（既有之排序之後）與其鍵之三支（本街廓 `(0,)`·他街廓二以上 `(1, 五級)`·唯一 `(1,)`）＝ `F16` `K23`〜`K26`、`K30`、`K31`、`F23` `K61`〜`K65`、`K70`〜`K73`；五級之屬性之取之一次與二停機 ＝ `F16` `K25`／`K28`／`K32`、`F23` `K64`／`K67`／`K74`；`R-4` 之獨立之列 ＝ `contests=(_ct or None))` 之計數 `1` 與 `W9`；`R-6` 之二回呼之引數之源 ＝ `W9`（逐引數之字樣）與上開之逐一對照（`f3_screen_adj4` 之 `adj4_plan`：`_ssa.get(K91_SS_MBA_EFFECTIVE, {}) or {}`、`_ssa.get(SS_FRONT_ROAD_DERIVE, {}) or {}`、`{_cb['label']: _nm_a4s.get(_cb.get('id'), '') …}`〔`_nm_a4s = _ssa.get(SS_FRONT_ROAD_NAME, {}) or {}`〕、`{_cr['街廓']: _cr.get('正面路寬(m)') for _cr in pk_kwargs['_corner_rows_init']}`、`adj4_depth_of(_ssa)`；`run_adj4`：`cb`、`{}`、`cad["front_road_derive"] or {}`、`_rva4.load_front_road_names()`、`{r["街廓"]: r.get("正面路寬(m)") for r in param_rows}`、`ns["adj4_depth_of"](ss)`）；`R-7` 之六處之式 ＝ `W9`（`ast.unparse` 逐字）。

全文差異 ＝ 同目錄之 `W-G.9-384R_K-9-71之落地_app差異.diff`（`git diff b47efbc 8ce1a18 -- app.py verify/selection_pipeline.py`）。

## ⑧ `app.py`／`verify/selection_pipeline.py` 之全文差異

見同目錄之 `W-G.9-384R_K-9-71之落地_app差異.diff`（`24236` B·`326` 列·`app.py` `+126`／`-10`·`verify/selection_pipeline.py` `+15`／`-5`）。

## ⑨ 工項三之 `checkidx`、`gen_fa_index`

````text
$ python <O>\checkidx.py <repo> <repo>\.claude\rules\常設規則索引.md   ⇒ rc 0
索引列數 124；內部字樣 122；外部指標 9；不合 0
$ python <O>\gen_fa_index.py <repo> <O>\FX_regen.md   ⇒ rc 0
則 124；加註節 14；列 158
$ cmp <O>\FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md   ⇒ rc 0（逐位同）
````

## ⑩ 各段耗時（本機時間 `+0800`）

| 段 | 起 | 迄 | 約 |
|---|---|---|---|
| 開場（fetch、四簿、pre-flight、工項零） | `2026-10-15 ≈ 22:12` | `22:15:52`（工項零之 commit·`heads_before.txt` 寫於 `22:14:36`） | `≈ 4` 分 |
| 工項一（抽塊、apply、commit、推） | — | `22:16:23` | `< 1` 分 |
| 前置（初跑·棄之） | `≈ 22:17` | `≈ 22:25`（終止） | `≈ 8` 分 |
| 撰碼與自跑（`dev1`／`dev2`） | `≈ 22:17` | `≈ 22:30` | `≈ 13` 分 |
| 前置（重跑·`58` 呼叫） | `22:26:26` | `23:46:44` | `≈ 80` 分（諸呼叫耗時之和 `10839.1` s） |
| 工項二之 commit | — | `23:47:02` | — |
| 驗（`58` 呼叫） | `23:47:12` | `00:50:59` | `≈ 64` 分（諸呼叫耗時之和 `8645.8` s） |
| `V-3`〜`V-8` 之比對 | `≈ 00:51` | `≈ 00:52` | `≈ 1` 分 |
| 唯讀獨立審查 | `≈ 00:52` | `≈ 01:10` | `≈ 18` 分 |
| 工項二之推、工項三 | — | `01:10:55`（工項三之 commit） | `≈ 1` 分 |
| 工項四（本報告） | `≈ 01:11` | — | — |
