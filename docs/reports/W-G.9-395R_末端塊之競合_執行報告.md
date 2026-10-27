# `W-G.9-395R`　末端塊之競合（`K-9-60` ①③·取得即鎖定·互相等待之被延後者之位）——執行報告（規格單＋補令一）

- 執行端（CC·雲端·Linux `4` 核·`nproc` ＝ `4`）·`2026-10-25` 19:24〜（+08:00）·effort=high·context 餘量 ≈ 14.9M tokens（開場時）。
- 單：原單 `docs/orders/W-G.9-395_規格單.md`（新側支 `880b8ef` 入倉）＋ 補令一 `docs/orders/W-G.9-395_補令一.md`（`82262` B·`sha256` `65fc0656a101ab8a92170a3951af745e0ef9dccec48c008965b2eda86b23c268`·`SELF_SHA256` `130ac7d6f9e04c78193ee8a4ab1c841c2f1640fa999505dbd5f79110f56af209` 自驗合 `P-5` 口徑〔受詞 `82184` B〕）。
- 倉外之輸出目錄 `<O>` ＝ `/tmp/o395p1`；施工樹 ＝ `/tmp/w`；前置″ 之樹 ＝ 工項一″ 之端之拋棄式 worktree `/tmp/wpre`。
- **本案之配地⛔ 變**（`V-4″`〜`V-6″`·下之 ③）。
- 原趟（原單之執行·停機款 `12`）：`ops/queue` 之 `reports/W-G.9-395_規格單_回報.md`（`13075` B·`sha256` `e0824975fffe4a1b5aeaf8a95dbbac517cb6f231293bce10ae3f4e715b0a1a65`）——工項零 `880b8ef`、一 `db0d0d0` 已推，工項二 `d000be0` ⛔ 推（其差異 ＝ 本批 `R-0″` 之底）。

## ① 逐 `commit` 之 hash 與工項（新側支 `verify/W-G.9-395-k960`·皆快轉）

| 工項 | `commit` | 內容 |
|---|---|---|
| 原單工項零 | `880b8efba0149758b8250ba9d651e26db3bf23fa` | 原單原封入倉（原趟·⛔ 變） |
| 原單工項一 | `db0d0d065c221b9e402cc119eb3c3a9cbab0bd8e` | 塊 `Fy52`（`6` 器·原趟·⛔ 變） |
| 工項零″ | `d509a1c5e5305154ccc6e556f7abc6ee9ec032f7` | 補令一原封入倉（`docs/orders/W-G.9-395_補令一.md`·新檔·`git cat-file blob` 與來源逐位同） |
| 工項一″ | `19dc0a7347eac5fee80ed7312493ba88611b046c` | 塊 `Fy53`（`F39` 之 `V9`〜`V13`·`probe_WG9395_k960.py` ＝ `c56e1b6e347b2bf92d80f31cd38afa87aab6838d`·`45439` B） |
| 工項二″ | `c84a48feb78ea3edba30fbda32ba7f32eb77771b` | `app.py`（`R-0″`＋`R-3″`＋`R-4″`）＝ `07dfd835c9c93fbec6a23a14791334879edb58cb`（對工項一″ 之端 `+163`／`−49`） |
| 工項三″ | `5fd7eb9d95b0fe59b4d3db513813dab815849c53` | 塊 `K43`＋`K44`、`P54`＋`P55`、`E43`、`G19` 之純末端追加 |
| 工項四″ | （本檔之 `commit`·回報載之） | 本報告與差異 |

`commit` 訊息之首列皆 ＝ 單所令逐字，其後空一列、附環境之尾列二列（`git commit -F`）。

## ② 停機款之三值（款·期·實）

### 補令一之款（`1″`〜`13″`）

| 款 | 期 | 實 |
|---|---|---|
| `1″` | 開工態之錨皆合 | 主線 `d4928d4845513a42fb1ac826a63167a38c78d4fb`、新側支 `db0d0d065c221b9e402cc119eb3c3a9cbab0bd8e`、heads（濾後之母體）`55`、樹淨、`app.py` `b39dfc45…`、`F39` `7f5ff1f5…`、`issuer_anchor 640 637` `rc 0`·四簿 ＝ 期（自誤 `625`／`640`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]`）、旗標 `[None, None, None, None, None]`、裝後匯入 `rc 0` ⇒ ⛔ 成就 |
| `2″` | 自驗與對拍合 | `SELF_SHA256`、bytes／`sha256` ＝ `STATE.json`；入倉後 blob 與來源逐位同 ⇒ ⛔ 成就 |
| `3″` | 塊與原趟之差異之 bytes／`sha256`／列數 ＝ `§五″`；`apply --check` 過；施後 blob ＝ 期 | 皆合（見 ④）⇒ ⛔ 成就 |
| `4″` | 前置″ 之期皆合 | (甲)(乙) `18`／`18` 合、(丙) 沿用、前置″ 項 `4` 合 ⇒ ⛔ 成就 |
| `5″` | ⛔ 規格之歧義而涉域上判斷 | ⛔ 見 ⇒ ⛔ 成就 |
| `6″` | `V-1″`〜`V-9″` 皆合；⛔ 改器；本案之配地⛔ 變 | 皆合 ⇒ ⛔ 成就 |
| `7″` | `push` 之目標唯新側支與 `ops/queue`、⛔ 被拒、⛔ `--force`、主線⛔ 推進 | 皆合（新側支之推五次皆快轉；`ops/queue` 之推一次被拒〔非快轉·他端之進度列〕⇒ `pull --rebase` 後推·⛔ `--force`；主線 ＝ `d4928d4`）⇒ ⛔ 成就 |
| `8″` | 四檔之嚴格前綴、尾 ＝ 塊、刪 `0`、blob ＝ 期；`checkidx`／`gen_fa_index` ＝ 期 | 皆合（見 ④、⑨）⇒ ⛔ 成就 |
| `9″` | 收工閘皆合 | 收工閘於本檔之 `commit` 推後量之（其實值出艙於 `ops/queue` 之回報·⛔ 寫入本檔·自指） |
| `10″` | ⛔ 「孰為正典」之判、⛔ 改器／塊／命令 | ⛔ 為之 ⇒ ⛔ 成就 |
| `11″` | 新檔⛔ 為 `check-ignore` 所命中 | 本補令之入倉時 `rc 1`（⛔ 命中）；餘見收工閘 `2″` ⇒ ⛔ 成就 |
| `12″` | 唯讀獨立審查⛔ 揭涉域上判斷或規格之漏載 | ⛔ 揭（見 ⑥）⇒ ⛔ 成就 |
| `13″` | 存取⛔ 被拒、寫入⛔ 為分類器所拒 | ⛔ 見 ⇒ ⛔ 成就 |

### 原單之款（`1`〜`13`·原趟之停機與本批之續）

| 款 | 期 | 實 |
|---|---|---|
| `1`〜`4`、`8`、`11` | 原趟之開場、工項零一、前置之期 | 原趟皆⛔ 成就（`ops/queue` 之 `reports/W-G.9-395_規格單_回報.md`）；本批由 `1″`〜`4″`、`8″`、`11″` 承之 |
| `5`、`6`、`7`、`9`、`10`、`13` | 同其文 | 本批由 `5″`、`6″`、`7″`、`9″`、`10″`、`13″` 承之 ⇒ ⛔ 成就 |
| `12` | 唯讀獨立 reviewer ⛔ 揭域上判斷或規格之漏載 | **原趟成就**（A-1 照 `R-3` ④ 之字面 ⇒ 無限迴圈；A-2 同位之先後未定）⇒ 停機上呈（原趟）；其讀 ＝ 補令一塊 `K44`（自誤 `641`）；本批之審查⛔ 再揭 ⇒ 本批⛔ 成就 |

## ③ 前置″ 與驗之出艙

### 開場（`§零-0″`）

- `git fetch origin`；`origin/wip/s1-endpart` ＝ `d4928d4845513a42fb1ac826a63167a38c78d4fb`；`origin/verify/W-G.9-395-k960` ＝ `db0d0d065c221b9e402cc119eb3c3a9cbab0bd8e`；heads（母體之式 ＝ `git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`）＝ `55`（全列存 `<O>/heads_before_395p1.txt`）；`checkout --detach origin/verify/W-G.9-395-k960` 後 `git status --porcelain --untracked-files=no` 空；`app.py` ＝ `b39dfc4598f48d4fa829df2b92ed023707bcd285`；`probe_WG9395_k960.py` ＝ `7f5ff1f52488bdff799db8cdfe3201531ec45b46`；殼無 `WV_`、旗標之出艙 `[None, None, None, None, None]`。
- 環境：初匯入失敗（`No module named 'shapely'`）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ 依原單 `§零-0` 項 `5` 之命令逐字釘回（`rc 0`）、移除 `tzdata`（`rc 0`）⇒ 匯入 `rc 0`（出艙 `<O>/pip_install.txt`、`pip_pin.txt`、`pip_untz.txt`）。
- 版本之比對：`Python 3.11.17`；`pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（`64` 列·`1114` B）＝ `基準/d4928d4845513a42fb1ac826a63167a38c78d4fb.md` 之「一、環境之指紋」；主線之端 ＝ 基準之 sha ⇒ **前置″ (丙) 沿用基準**（`73` 呼叫·⛔ 重跑）。
- pre-flight（`probe_order_preflight.py <本補令>`·`19dc0a7` 之前之器 ＝ `db0d0d0` 之器）：`rc 0`·🔴 `0`／🟡 `3`（`P-4` `:187`〔收工閘之表之首〕；`P-7` `:148`〔前置″ 項 `4`〕、`:189`〔閘 `1″`〕）——皆 ＝ `§五″` 項 `9` 之具名豁免；`P-5` ✅；`P-3` ＝ `23826`-`31569`。
- 原趟之差異：`<O>/rep395.diff` ＝ `23072` B·`sha256` `7dc5e10515de148952cd5c3ce89d5ccb5ce8119f934792cb40e1774cf0d91452`·`294` 列（＝ `§五″` 項 `3`）。

### 前置″ 項 `4` 之出艙（於工項一″ 之端 `19dc0a7`）

```
$ git diff --stat db0d0d0 HEAD
 ....9-395_\350\243\234\344\273\244\344\270\200.md" | 522 +++++++++++++++++++++
 verify/probes/probe_WG9395_k960.py                 | 108 +++++
 2 files changed, 630 insertions(+)
$ git grep -c -F "W-G.9-395" -- app.py        ⇒ （無出艙）rc 1
$ git grep -c -F "GB-207" -- app.py           ⇒ app.py:4  rc 0
```

（首列之路徑 ＝ `docs/orders/W-G.9-395_補令一.md`·`--stat` 之截寫。）

### 前置″ (甲)(乙)（`/tmp/wpre`·`19dc0a7`·並行 `2`·耗時之和 `1937` s）

`18`／`18` 合「工項一″ 之端」之期（`#38`、`#81`、`#82`、`#88`、`#89` ⇒ `rc 1`·末列 ＝ 期〔`#88` ＝ 補令一之表之列〕；其餘 `rc 0`）；`stderr` 合計 `0` B；`f8_pre_35.json` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、`f8_pre_00.json` ＝ `884e91714a79288406faa4def6518847de36de39`。（前置″ 之 `<repo>` ＝ `/tmp/wpre`；`parity` 之落檔與 `stdout` ⛔ 含倉之路徑〔`V-5″` 之代後逐位同證之〕。）

### 驗（`/tmp/w`·`c84a48f`·⛔ 推之前·殼無 `WV_`·從頭整套照跑·並行 `2`·19:48〜21:47·耗時之和 `14286` s）

- **`V-1″`**：(甲) `12` 呼叫皆 `rc 0`·末列 ＝ 施後之列（`#88` ＝ `⇒ 紅 []；rc 0`）；`F39 selftest` `28` 例（`T1`〜`T11`、`T7b`、`U1`〜`U2`、`V0`〜`V13`）皆 ✅；`F39 wiring` `W1`〜`W6` ✅；`F39 run` `R1@3.5`、`R2@3.5`、`R1@0.0`、`R2@0.0` ✅。⇒ 合。
- **`V-2″`**：其餘 `73` 呼叫皆 `rc 0`·末列 ＝ 原單之表之施後之列（`#56`／`#57` ＝ JSON 之摘要列）；`F23 selftest`（`#4`）之 `✅ P0 逐項擾動恰該項紅 75／75`。⇒ 合（`91`／`91`·`<O>/tools/check.py` 對原單之表與補令一之表機械比之）。
- **`V-3″`**：`probe_WG9354_endcontest.py` `88880f5a…`、`probe_WG9389_trialstop.py` `acc6f571…`、`probe_WG9393_endall.py` `40009fb9…`、`probe_WG9394_k9615.py` `14fcea02…`、`probe_order_preflight.py` `a014a525…`（＝ 原單 `§五-1` 項 `5`）；`probe_WG9395_k960.py` `c56e1b6e…`（＝ `§五″` 項 `5`）；`verify/probes/` 對工項一″ 之端相異 `0`。⇒ 合。
- **`V-4″`**：`k6s3 run` 二退縮 `rc 0`（`#56`、`#57`）；

```
F36 diff k6s3_pre_35 k6s3_post_35  ⇒ rc 0·全出艙 1 列：全比相異 0 項
F36 diff k6s3_pre_00 k6s3_post_00  ⇒ rc 0·全出艙 1 列：全比相異 0 項
k6s3 cmp k6s3_pre_35 k6s3_post_35  ⇒ rc 0·末列：相異 0 項 ⇒ ✅ 同
k6s3 cmp k6s3_pre_00 k6s3_post_00  ⇒ rc 0·末列：相異 0 項 ⇒ ✅ 同
F36 diff k6s3_pre_35 k6s3_pre_00（對照）⇒ rc 0·末列：全比相異 44 項
```

  ⇒ **本案之配地⛔ 變**。
- **`V-5″`**：`parity` 二退縮 `rc 0`·末列 `⇒ rc 0（不符 0 項）`；落檔（`parity35`／`parity00`）與 `stdout`（`#60`／`#61`）對前置″：⛔ 代 ⇒ 皆**異**（`"head"` 欄 `19dc0a7…` 對 `c84a48f…`、`stdout` 首列之 `態`）；以同一字樣代二態之 `HEAD`（全值與短值）之後 ⇒ 四者皆**逐位同**。⇒ 合。
- **`V-6″`**：`F8 run` 二退縮 `rc 0`·末列 `⇒ 紅 []；rc 0`；`git hash-object`：3.5 m 前後 `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`／`47683d1cb284ad814034d7ac7f3cd464d66c6e3f`；0 m `884e91714a79288406faa4def6518847de36de39`／`884e91714a79288406faa4def6518847de36de39`。⇒ 合。
- **`V-7″`**：生產碼 `34` 檔對工項一″ 之端相異恰 `1`（`app.py`·`+163`／`−49`·blob `07dfd835c9c93fbec6a23a14791334879edb58cb`）；`verify/` 相異 `0`；`app.py` 對 `<O>/app_R0.py`：`+29`／`−7`、`6` hunk（下之出艙·逐 hunk 之所屬見 ⑦ 與 ⑥）；`ast` 頂層節點之相異：對 `app_R0.py` ＝ `['end_block_apply', 'k6b_stage3_run']`、對 `d4928d4` ＝ `['end_block_apply', 'end_block_merge_run', 'k6b_stage3_run']`；頂層節點 `417` 逐序同。⇒ 合。
- **`V-8″`**：「W-G.9-395」⇒ `app.py:11`（≥ `1`）；「GB-207」⇒ `app.py:2`（＜ `4`）；「補令一 ″」⇒ `app.py:3`（≥ `1`·判別力：`<O>/app_R0.py` 之同計 `0`）。⇒ 合。
- **`V-9″`**：`V-1″`〜`V-6″` 之諸器之 `stderr` 合計 `0` B。⇒ 合。

### `V-7″` 之 `git diff --no-index <O>/app_R0.py <repo>/app.py` 之出艙（全文）

| hunk | 新檔之行 | 所屬 | 條 |
|---|---|---|---|
| `1` | `11508`–`11509`（增） | 模組層之註（原趟所增之 `🔧 W-G.9-395` 之列之下·⛔ AST 之節點） | `R-4″` |
| `2` | `11663`–`11665`（`−1`／`+3`） | `end_block_apply` 之 docstring 之末 | `R-4″` |
| `3` | `11685`（增） | `end_block_apply` 之註（`_pre395` 之上） | `R-4″` |
| `4` | `14988`–`14993`（`−3`／`+6`） | `k6b_stage3_run` 之 docstring | `R-4″` |
| `5` | `15492`–`15508`（`−2`／`+16`） | `_k950_rows` 之註與 `_ps395` | `R-3″`（＋註 `R-4″`） |
| `6` | `15547`（`−1`／`+1`） | `_k950_rows._ring395` 之延後之記 | `R-3″` |

````diff
diff --git a/tmp/o395p1/app_R0.py b/app.py
index a0d4477..07dfd83 100644
--- a/tmp/o395p1/app_R0.py
+++ b/app.py
@@ -11505,6 +11505,8 @@ def _end_region_R(block_poly, cad_alloc, end_pt, min_width, frag_poly, _label=''
 #    ≤ `END_BLOCK_UNFRONT_EPS`（無三角地）⇒ `R_end` ＝ 末端帶、`s_back` ＝ `0`；二端皆為末端塊而一筆同時跨占二端之
 #    `R_end` ⇒ 停機（`GB-207`·`K-9-60 ①` 未落地·`end_block_apply`）。
 #    🔧 `W-G.9-395`（`K-9-60 ①`·KL 裁 `2026-10-05 22:59`）：上開之停機去之——二端各依原位次試（`end_block_apply` 之二端預選）。
+#      KL `2026-10-25 03:58` 之答（其請示之通知一·KL 未示異議）：只一端拿得下 ⇒ 歸該端；二端皆拿得下 ⇒ 歸交面積大之一端、
+#      相同 ⇒ p1 側；二端皆拿不下 ⇒ 二端皆不歸；「一筆」＝ 一個暫編地號之宗。
 #  R_end ＝ 未臨正街 ∪ 末端帶（`_end_region_R`·帶寬 ＝ 畸零地寬）。
 #  候選 ＝ 本街廓原位次序列之宗，其重劃前多邊形 ∩ R_end ＞ `END_BLOCK_CROSS_MIN_AREA`；
 #    跨占本街廓任一街角規定範圍（＞ 同門檻）者⛔ 為候選（`K-9-49 ③`：同時跨占二者之土地歸街角側）。
@@ -11658,7 +11660,9 @@ def end_block_apply(ordered, *, blk_label, block_poly, d_hat, corner_pt, front_p
     他端視為未被此筆跨占：除該宗（以暫編地號比·⛔ 以原地號）之序重行 `end_block_pick`，其所回之列於原評選之列中該宗之位插入
     該宗之列（其值同原列而 `結果` ＝ `'歸他端'`）；二端之最終之當選既定之後，一端之當選於他端之列而為 `'未達'` 者 ⇒
     `'歸他端'`（合併再試⛔ 以之為候選）。其後之紀錄、落位（先左後右）、回傳照舊；非二端預選之街廓（一端有側街、或有
-    `cache`）逐位同改前。重選而皆未達且⛔ 准強制 ⇒ `end_block_pick` 之既有之停機（其訊息之列 ＝ 重選之列）。"""
+    `cache`）逐位同改前。重選而皆未達且⛔ 准強制 ⇒ `end_block_pick` 之既有之停機（其訊息之列 ＝ 重選之列）。
+    所據之讀：KL `2026-10-25 03:58` 之答（其請示之通知一·KL 未示異議）——這筆土地在兩端各依原位次試一次；只一端拿得下
+    ⇒ 歸該端；兩端皆拿得下 ⇒ 歸落於範圍內面積（取至 2 位）較大之一端、相同歸 p1 側；兩端皆拿不下 ⇒ 兩端皆不歸。"""
     _info = {'left': None, 'right': None}
     _cached = cache.get(blk_label)
     _rec = {}
@@ -11678,6 +11682,7 @@ def end_block_apply(ordered, *, blk_label, block_poly, d_hat, corner_pt, front_p
     #   （左之序 ＝ `_out`、右之序 ＝ 其反序）；衝突（二端之當選為同一暫編地號）⇒ 交面積大者／相同 ⇒ 左端得之，他端除之而
     #   重選並於原列之該宗之位插入其「歸他端」之列；其後一端之當選於他端之列之「未達」⇒「歸他端」。下之迴圈取其結果
     #   （⛔ 再評選）。准強制之否之取與評選之先後同改前（左之取 → 左之評選 → 右之取 → 右之評選）。
+    #   所據之讀 ＝ KL `2026-10-25 03:58` 之答（其請示之通知一·KL 未示異議）。
     _pre395 = {}
     if 'left' in _geo393 and 'right' in _geo393 and _cached is None:
         _al395, _tr395 = {}, {}
@@ -14980,9 +14985,12 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
       消滅：一競合處理之後、或一列使其端定案之後，凡停候之競合之首列之端或其夥伴之端已定案者 ⇒ 消滅（首列與候列皆回列）。
       回列：與列中之餘依其排序之位（`最終序位`；延後之首列依其新位）合排（升序）。互相等待：每取一列之前（含列空之時），以
       「停候之競合 → 其夥伴之列所在之候列之競合」為邊，有環 ⇒ 環中 `'序鍵'`（`end_block_merge_run` 所載·`k967_rank`）最小之
-      競合（先處理者）仍停候，持其夥伴之列之競合之停候消滅（⛔ 為其競合之畢），其首列（被延後之地主之列）之排序之位改為
-      該夥伴之列之 `最終序位` ＋ `0.5`、首列與候列皆回列——夾於夥伴之列之前之他人照原位次先試；記一列（`層級` ＝
-      `'K-9-60 ③'`、`結果` ＝ `'互相等待 ⇒ 先處理'`）；再判之。環中有缺 `'序鍵'` 之競合 ⇒ 停機。各端至多一競合之輸入逐位同改前。
+      競合（先處理者）仍停候，持其夥伴之列之競合之停候消滅（⛔ 為其競合之畢），其首列（被延後之地主之列）記其夥伴之列而
+      退至該夥伴之列之現位之緊後（補令一 ″·塊 `K44`：排序之位 ＝ 一串數——未延後之列 ＝（其 `最終序位`）、延後之首列 ＝
+      其夥伴之列之當時之排序之位接其自身之 `最終序位`；每次排序時依夥伴之鏈求之 ⇒ 夥伴之列其後再移者隨之；逐項比、前綴者
+      在前；同退於一列之後者依其 `最終序位`；再延後者改記新之夥伴之列；夥伴之鏈成環 ⇒ 停機），首列與候列皆回列——夾於
+      夥伴之列之前之他人照原位次先試；記一列（`層級` ＝ `'K-9-60 ③'`、`結果` ＝ `'互相等待 ⇒ 先處理'`）；再判之。環中有缺
+      `'序鍵'` 之競合 ⇒ 停機。各端至多一競合之輸入逐位同改前（無延後 ⇒ 一切位皆一項之串 ⇒ 其序 ＝ `最終序位` 之序）。
     """
     import copy as _cp
     from shapely.geometry import Polygon as _Pg, LineString as _Ls
@@ -15481,9 +15489,23 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             _pt[_k] = [tuple(e[:3]) for e in contests[_ci]['列'] if tuple(e[:3]) != _k][0]
         _cdone, _susp = set(), {}
         _q = _dq(rows)
-        # 🔧 `W-G.9-395`（R-3 ②③④·`K-9-60 ③`）：回列 ＝ 依排序之位合排（_np395 ＝ 延後之首列之新位）；消滅；互相等待之環
+        # 🔧 `W-G.9-395`（R-3 ②③④·`K-9-60 ③`）：回列 ＝ 依排序之位合排（_np395 ＝ 延後之首列 → 其夥伴之列）；消滅；互相等待之環
+        #   補令一 ″（塊 `K44`）：排序之位 ＝ 一串數——未延後之列 ＝（其最終序位）；延後之首列 ＝ 其夥伴之列之當時之排序之位，
+        #   其後接其自身之最終序位（每次排序時依夥伴之鏈求之·夥伴之列其後再移者隨之）；逐項比、前綴者在前 ⇒ 恆在夥伴之列之
+        #   緊後、原排其後之一切列之前；同退於一列之後者依其最終序位。夥伴之鏈成環 ⇒ 停機（程式之錯）。
         _np395 = {}
-        _ps395 = lambda r: _np395.get(_kf(r), r['最終序位'])
+
+        def _ps395(r):
+            _k395, _seen395, _rk395 = _kf(r), [], [r['最終序位']]
+            while _k395 in _np395:
+                _seen395.append(_k395)
+                _y395 = _np395[_k395]
+                _k395 = _kf(_y395)
+                if _k395 in _seen395:
+                    raise RuntimeError(
+                        f"🔴 [K-6-B 段三 K-9-60 ③] 延後之首列之夥伴之鏈成環 {_seen395 + [_k395]}（程式之錯·停機款 9）")
+                _rk395.append(_y395['最終序位'])
+            return tuple(reversed(_rk395))
 
         def _back395(lst):
             nonlocal _q
@@ -15522,7 +15544,7 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                 _pk395 = _pt[_kf(_susp[_fr395][0])]
                 _lst395 = _susp.pop(_dl395)
                 _pr395 = [_x395 for _x395 in _lst395[1:] if _kf(_x395) == _pk395][0]
-                _np395[_kf(_lst395[0])] = _pr395['最終序位'] + 0.5
+                _np395[_kf(_lst395[0])] = _pr395            # 補令一 ″：退至夥伴之列之現位之緊後·隨之而移（再延後 ⇒ 改記新者）
                 _back395(_lst395)
                 _f395, _d395 = _susp[_fr395][0], _lst395[0]
                 _row(序=_f395['最終序位'], 街廓=_f395['街廓'], 端=_f395['端'], 候選=_f395['暫編地號'],
````

### 前置″ 與驗之 `91` 呼叫之表（`rc`／`stderr` B／末列·耗時 s）

前置″ 之欄：(甲)(乙) ＝ 於 `/tmp/wpre`（`19dc0a7`）照跑；(丙) ＝ 沿用 `基準/d4928d4845513a42fb1ac826a63167a38c78d4fb.md`（版本之比對皆同·⛔ 重跑）。施後之欄：於 `/tmp/w`（`c84a48f`）從頭照跑（並行 `2`·⛔ 沿用）。逾時或 `rc` ≠ 期而重跑者 ＝ `0`。`#56`〜`#61` 之落檔：前置″ ⇒ `<O>/pre/…_pre`、施後 ⇒ `<O>/post/…_post`。

| # | 命令（`<repo>` ＝ 施工樹） | 工項一″ 之端（前置″） | 施後（驗·`c84a48f`） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（118） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（380） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（39） | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（39） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（37） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（15） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（231） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（73） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（452） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（654） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（73） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（397） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1705） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（23） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（22） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（244） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（315） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（36） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（22） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | (甲) `1`／`0`／`⇒ 紅 ['H2 一筆土地為同一街廓二端之未達候選 ⇒ 題二之競合：二端皆拿不下 ⇒ 皆⛔ 併', 'H3 一末端塊屬二競合而順序一致 ⇒ 依原位次（甲之競合先、K 之競合後）·皆不成']；rc 1`（81） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（12） | `0`／`0`／`⇒ 紅 []；rc 0`（11） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（176） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（53） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（844） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（144） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（118） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（328） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`紅項 [] 器紅 0`（8） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（333） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on /tmp/o395p1/post/k6s3_post_35.json` | (乙) `0`／`0`／`（JSON 之摘要列·略）`（249） | `0`／`0`／`（JSON 之摘要列·略）`（180） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on /tmp/o395p1/post/k6s3_post_00.json` | (乙) `0`／`0`／`（JSON 之摘要列·略）`（143） | `0`／`0`／`（JSON 之摘要列·略）`（141） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 /tmp/o395p1/post/f8_post_35.json` | (乙) `0`／`0`／`⇒ 紅 []；rc 0`（171） | `0`／`0`／`⇒ 紅 []；rc 0`（181） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 /tmp/o395p1/post/f8_post_00.json` | (乙) `0`／`0`／`⇒ 紅 []；rc 0`（124） | `0`／`0`／`⇒ 紅 []；rc 0`（140） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on /tmp/o395p1/post/parity35_post.json` | (乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（374） | `0`／`0`／`⇒ rc 0（不符 0 項）`（430） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on /tmp/o395p1/post/parity00_post.json` | (乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（264） | `0`／`0`／`⇒ rc 0（不符 0 項）`（274） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（303） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1192） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1169） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（122） | `0`／`0`／`⇒ 紅 []；rc 0`（123） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（441） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（299） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（34） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（698） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（333） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | (甲) `1`／`0`／`⇒ 紅 ['T12', 'T12b']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | (甲) `1`／`0`／`⇒ 紅 ['W9']；rc 1`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（330） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（344） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | (丙) 沿用 `基準/d4928d48….md`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（315） |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | (甲) `1`／`0`／`⇒ 紅 ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T7b', 'T8', 'T9', 'T10', 'U1', 'U2', 'V0', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V13', 'V12']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | (甲) `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4']；rc 1`（7） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（303） | `0`／`0`／`⇒ 紅 []；rc 0`（305） |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | (甲) `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（1） | `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（1） |

## ④ 塊之實得與四檔之改前改後

| 塊 | bytes | `sha256` | 列 |
|---|---|---|---|
| `Fy53` | `8756` | `fbac3aaa0c0d5abb273071edc57530f171bafd99bfedb18fc958f5b72562a2a9` | `129` |
| `K44` | `7130` | `7d2adc62e3da18e74af7a548edc2f6b210d5275429ccc03f3b957f304ee29ede` | `39` |
| `P55` | `991` | `29c5b703eb4cf4f652e6603b273990be484d1840ff248e29800dfa8b6f07a97a` | `14` |
| `E43` | `3119` | `360cf8b9f41161b92e356e4462a701663a13305acc328fbda91e9cbc200a8d68` | `12` |
| 原單 `K43` | `13994` | `c4fed84db9a24a8e3fc303d5725674ec93aa83addfb920c848d7409963d0d61a` | `66` |
| 原單 `P54` | `4022` | `7bdbc205efc94d765819bfcc91cf40a303831d7e9f196911caf934bcef4f196d` | `20` |
| 原單 `G19` | `1833` | `24a9e63249792d8a81e75f2a7e38e555a61d9085ca96ebccb2a8b2cffa244e1c` | `10` |
| `CK`（`checkidx`） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` |
| `GF`（`gen_fa_index`） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` |

皆 ＝ `§五″` 項 `2`、`4`、`7`（原單之塊自倉內之原單依其抽取式取之）。`Fy53` 之施前 blob `7f5ff1f5…`（`38281` B）、`git apply --check` 過、施後 `c56e1b6e…`（`45439` B）。

| 檔 | 改前 B | 改後 B | 改後之 blob | 增／刪 | 尾 |
|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `973576` | `994700` | `9872c2b1351a783c8be3ff2779ebffc2859f3430` | `105`／`0` | `K43` ＋ `K44` |
| `docs/待落地清單.md` | `38764` | `43777` | `1edf59f42a5c9b5aebdeeeda6249ddbe0dfdd875` | `34`／`0` | `P54` ＋ `P55` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1239643` | `1242762` | `0764bf9ed9d3c4559aad186c55082dd4c3524101` | `12`／`0` | `E43` |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1068693` | `1070526` | `2a07e78d81c65d9144fe80316e66965aa45f5022` | `10`／`0` | `G19` |

改前皆為改後之嚴格前綴（二進位之附加·`<O>/tools/append.py` 斷言之）；四檔之 blob ＝ `§五″` 項 `5`。

## ⑤ 推送之目標與推後之遠端分支之列

- 母體之式：`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`。
- 工項零″：`db0d0d0..d509a1c`（推後 heads `55`、主線 `d4928d4`）；工項一″：`d509a1c..19dc0a7`；工項二″：`19dc0a7..c84a48f`（驗與審查皆符後·與驗為分開之呼叫）；工項三″：`c84a48f..5fd7eb9`；工項四″：本檔之 `commit`。皆 `git push origin HEAD:verify/W-G.9-395-k960`（快轉·⛔ `--force`）。主線 `wip/s1-endpart` ⛔ 動。

## ⑥ 自捕與自解、唯讀獨立審查

### 自捕與自解

1. **單首 🔑「Bash 命令⛔ 含 heredoc」**：接單之時（讀單之前）`ops/queue` 之 `STATE.json` 之轉移以 heredoc 之 Python 為之——違本補令之通則（其物 ＝ `ops/queue` 之狀態檔·⛔ 及倉與驗）。讀單之後一切輔助腳本皆以檔案之寫入為之（`<O>/tools/`）。
2. 前置″ 之初啟：命令之鏈之末之 `&` 使全鏈入背景，其中 `mkcmds.py` 誤抽收工閘之表之列（含 `<repo 絕對路徑>`）而斷言失敗 ⇒ 未起任何呼叫；改為唯自「項 `8` 之表」之標題起抽之後重啟（其趟之一切出艙皆自重啟起）。
3. 前置″ 與驗之間，倉外之輔助器 `runner.py`（依所給之序跑·長者先）與 `check.py`（`#56`／`#57` 之「JSON 之摘要列·略」⇒ 末列⛔ 比）改之——皆倉外之量之工具·⛔ 及量測器。
4. `ops/queue` 之推一次被拒（發單端之門鈴之記先推）⇒ `pull --rebase`（`log.md` 之衝突以二側之列皆留解之）後推。
5. `ops/queue` 之 `log.md` 之 `21:47` 之進度列書「已畢 `91`……餘續跑」——其時 `91` 呼叫已皆畢、「餘續跑」之字誤（⛔ 涉值）。
6. 驗之諸器於 `verify/` 下生 `__pycache__/`（`.gitignore:18` 所忽·⛔ 入 `git status`）。

### 唯讀獨立審查（一輪·派一唯讀之 reviewer·⛔ 改檔、⛔ `commit`·其腳本在倉外 `/tmp/rev395p1/`·`21:52`〜`22:19`）

- **① hunk**：`git diff --no-index -U0` 之 `7` hunk（`-U3` 之 `6`）——模組層之註、`end_block_apply` 之 docstring 與註、`k6b_stage3_run` 之 docstring（`R-4″`）；`_k950_rows` 之註、`_ps395`、`_ring395` 之延後之記（`R-3″`）；他處一字⛔ 動。對 `app_R0` 之頂層相異 `['end_block_apply', 'k6b_stage3_run']`、對 `d4928d4` 三節點、頂層之名 `417` 逐序同；`R-0″` 自行重施得 `a0d44774`；`F39 wiring` 綠。✅
- **② `R-3″` 與塊 `K44` 之二之甲〜丙**：`_ps395` 沿 `_np395` 之鏈收諸列之 `最終序位` 而逆之 ＝「夥伴之列之當時之位串接自身之最終序位」；每次 `sorted` 重求（隨之而移）；`tuple` 之比 ＝ 逐項·前綴者在前；同退者依最終序位；再延後 ⇒ 覆寫；成環 ⇒ 停機（AST 抽 `_ps395` 之單元測：鏈 a→b→c ⇒ `(3,2,1)`；c→a ⇒ 停機·訊息載鏈 `[a, b, c, a]`）；⛔ 迭代上限、⛔ `try`／`except`；各端至多一競合之輸入 `5000` 例本次之碼、`19dc0a7` 之碼、原趟之碼之事件序逐位同（環 `0`）。✅
- **③ `F39` `V9`〜`V13` 之期值**：依附錄戊″ 逐步手算 `V9`、`V10`、`V11`、`V13` ⇒ 與 `F39` 之 `V9_13` 逐項同；`V12` ＝ `V11` 之換名換端（實跑覆之）；獨立之模型與本次之碼（AST 注入）亦皆 ＝ 期值；`F39 selftest` `28`／`28`。另見：原趟之碼於 `V9`、`V10`、`V11`、`V13` 之四玩具皆不止（環 ＞ `200`）。✅
- **④ 隨機測**（AST 抽 `_k950_rows` 注入模擬之 `contests`／`won`／`_skip`／`merged_out`／`_row`／`_contest`；每例時限 `3` s 且環事件 ＞ `3000` ⇒ 不止；獨立之模型照塊 `K44` 之文以「依附之林之先序走訪」表位）：
  - 主測 `40000` 例（二〜八端、二〜八位地主、每端之列相連、競合之二列分屬二端）：有延後 `25658`、延後 ≥ `2` 次 `8893`、夥伴之列於延後之後再移 `954`、環事件 `101292`；**本次之碼：不止 `0`／成環之停機 `0`／他停機 `0`／失列 `0`／重列 `0`**；與獨立之模型逐事件一致 `40000`／`40000`；**原趟之碼不止 `6692`／`40000`**（前 `300` 例以 `5` 萬環、`20` s 重跑仍不止 `300`／`300`）、止而事件序異 `2338`、無環之例原趟 ＝ 本次 `14342`／`14342`。
  - 加測（二〜十二位地主）：相連形 `10000` 例（延後 ≥ `2` 次 `3149`·一致 `10000`·本次零異常·最大環數 `47`·原趟不止 `2411`）；不相連形 `10000` 例（延後 ≥ `2` 次 `3130`、再移 `609`·一致 `10000`·零異常·原趟不止 `2512`）。
  - 判別力（突變·各 `5000` 例）：「同退者反序」與模型相異 `1653`；「延後時定其位」（初稿之讀）相異 `115`。✅
- **⑤ 其他**：本案 `F39 run`（審查者於倉外之拷貝）二退縮 `R1`／`R2` 綠·合併再試之標的 `[]`·競合 `None` ⇒ 本案走 `if not contests:` 之支、本批之差皆在其後或註 ⇒ 本案之配地⛔ 變（與 `V-4″`〜`V-6″` 合）。
- **涉域上判斷或規格之漏載**：**無**（記：塊 `K44` 之二之丁之終止與「成環⛔ 可達」唯實測、⛔ 證明——塊 `K44` 已載）。
- **純實作之瑕**：**無**。NOTE（⛔ 擋）：模組層之註書「交面積大」而⛔ 載「取至 2 位」（`end_block_apply` 之 docstring 載之）；`F39` 無一例觸「夥伴之鏈成環」之停機（審查以 AST 之單元測補證）；本次之 blob `07dfd835`（`+163`）異於發單端之原型 `736592ad`（`+153`）——單⛔ 要求同。
- ⇒ 停機款 `12″` ⛔ 成就；執行端⛔ 修（純實作之瑕 `0`）。

## ⑦ 設計說明（原單 `§三-5`·補令一 `§三-5″`）

### 〇、`R-0″` 之 blob 之對證

- `<O>/rep395.diff`（＝ `ops/queue` 之 `reports/W-G.9-395_規格單_工項二未推之差異.diff`·二進位複製）：`23072` B·`sha256` `7dc5e10515de148952cd5c3ce89d5ccb5ce8119f934792cb40e1774cf0d91452`·`294` 列（＝ `§五″` 項 `3`）。
- 於工項一″ 之端（`19dc0a7`·`app.py` ＝ `b39dfc4598f48d4fa829df2b92ed023707bcd285`）`git apply --check` 過、`git apply` ⇒ `app.py` ＝ **`a0d44774cf51004feae81654dd76a47d92651ae0`**（`+141`／`−49`）＝ 期；即二進位複製為 `<O>/app_R0.py`。其上唯依 `R-3″`、`R-4″` 改之 ⇒ 工項二″ 之 `app.py` ＝ `07dfd835c9c93fbec6a23a14791334879edb58cb`（對工項一″ 之端 `+163`／`−49`；對 `app_R0.py` `+29`／`−7`）。

### 一、原單 `R-1`〜`R-4` 之各條（原趟之碼·照實）

原趟之設計說明草（`ops/queue` 之 `reports/W-G.9-395_規格單_設計說明草.md`）之 `R-1`、`R-2`、`R-3` ①②⑤、`R-4`、`§三-3` 之自查照舊適用（其碼本補令⛔ 改）。唯 `R-3` ③④ 之「排序之位」依 `R-3″` 更之（下之二）。

- `R-1`（`end_block_apply`）：`GB-207` 之停機之段整段去之，代以「二端預選」（`_pre395`·條件 ＝ 二端皆無側街且 `cache` 無本街廓）；衝突 ⇒ 交面積大者／相同 ⇒ 左端得之，他端除該宗（以暫編地號比）重選並於原列之該宗之位插入「歸他端」之列；二端之最終之當選既定之後，一端之當選於他端之列之「未達」⇒「歸他端」；迴圈中 `_sd in _pre395` ⇒ 取其結果（⛔ 再評選）。等價之證（非衝突之輸入）：改前左端落位後再評右端之序與改後之右之序之差唯左之當選之位；改前可跑通之輸入，左之當選⛔ 跨占右之 `R_end` ⇒ ⛔ 入右之列 ⇒ 右之列與當選逐位同。
- `R-2`（`end_block_merge_run`）：`_dup` 之停機（同時跨占二以上末端塊）、`_tgc` 與「屬二以上之競合」之停機去之；每競合增 `'序鍵'` ＝ `k967_rank(ΣG, ΣA, p)`（受詞 ＝ 二標的之首次之試算之列中 `未達` 而屬本群者·一宗於二端皆有列者 G 各計；ΣA ＝ `k967_pre_area`·表 ＝ 分攤登記面積 − 段三部分併出）；`_L` 增首次之試算之各端之當選（取得即鎖定）；「三個以上之末端塊」之停機照舊。
- `R-3`（`_k950_rows`）：停機之全列——去：「一端屬二以上之競合」；留：「列數 ≠ 2」「同一列見於二競合」（訊息改）、「不在 order」「候其夥伴而夥伴未至」；增：「互相等待之環 … 缺序鍵」與本補令之「延後之首列之夥伴之鏈成環」（下）。② 消滅（`_gone395`）、④ 互相等待之環之判（`_ring395`·每取一列之前·含列空之時）照原趟。
- `R-4`：新增之區域名皆帶 `395`。

### 二、`R-3″`（補令一·塊 `K44` 之二之甲〜丙）

- **落處**：`k6b_stage3_run` 之巢狀 `_k950_rows` 之內，原趟之 `_ps395`（`lambda`）改為巢狀函式；`_np395` 之值由「新位之數」改為「夥伴之列（列之 `dict`）」。
- **排序之位之表示**：`_ps395(r)` 自 `r` 起循 `_np395` 之鏈（`r` → 其夥伴之列 → 該列之夥伴之列 → …）至一未被延後之列止，回「鏈之諸列之 `最終序位` 之逆序之 `tuple`」——即「夥伴之列之當時之排序之位，其後接自身之 `最終序位`」之遞迴之展開。未被延後之列 ⇒ `(最終序位,)`。每次 `_back395` 之 `sorted(…, key=_ps395)` 皆重求 ⇒ 夥伴之列其後自身又被延後者，被延後之首列之位隨之（甲之二）。
- **比較**：Python 之 `tuple` 之比 ＝ 逐項比、前一項相同者比次項、一串為他串之前綴者在前（升序）⇒ `R-3″` ③。
- **延後之記**：`_ring395` 中 `_np395[_kf(_lst395[0])] = _pr395`（被延後之首列記其夥伴之列）；一列再被延後者覆寫之（改記新者）。`競合` 之字串之「退至 X 之後」之 X ＝ `_pr395['暫編地號']`（照原趟）。
- **④ 之證**：設被延後之首列 `d` 之夥伴之列為 `p`，`pos(d) ＝ pos(p) + (fs(d),)`。(i) `pos(p)` 為 `pos(d)` 之真前綴 ⇒ `p` 先於 `d`。(ii) 原排於 `p` 之後之任一列 `x`：`pos(x) > pos(p)` 且 `pos(x)` 非以 `pos(p)` 為前綴者 ⇒ 於 `pos(p)` 之長度內之某項已大 ⇒ `pos(x) > pos(d)`；`pos(x)` 以 `pos(p)` 為前綴者 ＝ 亦退於 `p` 之後之他列（同退者）⇒ 其與 `d` 之先後依次項 ＝ 其自身之 `最終序位`（乙·⛔ 依退之先後·⛔ 依列中之餘先）。⇒ `d` 恆在 `p` 之緊後（同退者之間依 `最終序位`）、原排其後之一切列之前。(iii) `最終序位` 各異 ⇒ 鏈不同之二列之位必異（⛔ 同位）。
- **成環之停機**：循鏈時已見之鍵再見 ⇒ `RuntimeError`（訊息「延後之首列之夥伴之鏈成環 <鏈>（程式之錯·停機款 9）」·載其鏈）；⛔ 以他法代之。
- **⑥**：迭代⛔ 設上限、⛔ 以例外之攔截代排序（`_ps395` 之例外唯成環之停機）。

### 三、原單 `R-3` ⑤ 之等價之證（各端至多一競合之輸入）

原趟之證（設計說明草 `R-3` ⑤ (i)〜(iii)）：各端至多一競合 ⇒ 互相等待之邊⛔ 有 ⇒ `_ring395` 恆無所施 ⇒ `_np395` 恆空 ⇒ 一切列之 `_ps395` ＝ `(最終序位,)`（一項之串）⇒ `sorted` 之序 ＝ 依 `最終序位` 之升序 ＝ 原趟之 `_np395.get(鍵, 最終序位)` 之序（亦 ＝ 改前之 `appendleft` 之序·原趟之證）。⇒ 逐列之序與紀錄逐位同改前（`F39` 之 `T*`／`U*`、`F13` 之諸例、本案二退縮之 `V-4″`〜`V-6″` 實證之）。

### 四、終止之實測（塊 `K44` 之二之丁·⛔ 為證明）

見報告 ⑥ 之唯讀獨立審查之隨機測（倉外·`F39` 之外）。

### 五、`R-4″`（註）

- `k6b_stage3_run` 之 docstring：「其首列……之排序之位改為該夥伴之列之 `最終序位` ＋ `0.5`」改述為 `R-3″` 之義（載「補令一 ″·塊 `K44`」）；`_k950_rows` 內 `_np395` 之上之註三列與延後之記之列之行尾註亦載「補令一 ″」。
- `end_block_apply`：docstring 之末增二列、`_pre395` 之上之註增一列、模組層之註（原趟所增之 `🔧 W-G.9-395` 之列之下）增二列——皆載 KL `2026-10-25 03:58` 之答（其請示之通知一·KL 未示異議）。
- `R-3″`、`R-4″` 以外之一字⛔ 動（`V-7″`）。

### 六、`§三-3` 與 `§三-3″` 之自查

- `app.py` 對 `<O>/app_R0.py` 之 `ast` 頂層節點之相異 ＝ `['end_block_apply', 'k6b_stage3_run']`（⊆ 許）；對 `d4928d4` ＝ `['end_block_apply', 'end_block_merge_run', 'k6b_stage3_run']`（恰三）；頂層節點 `417`（具名 `405`·逐序同）。
- 新增之區域名 `_k395`、`_seen395`、`_rk395`、`_y395`：於 `app.py` 與 `verify/` 皆 `0` 見（`grep -w`·改前）。
- 字樣之錨（`F23`／`F24 wiring`）、突變之錨（`F13`）、`main`、案件字面、簽名：驗之 `#5`、`#6`、`#38`、`#39`、`#29`、`#89`、`#70` 證之（下之 ③）。

## ⑧ `app.py` 之全文差異

同目錄之 `W-G.9-395R_末端塊之競合_差異.diff`（`git diff d4928d4 c84a48f -- app.py`·`25435` B·`316` 列·`sha256` `18bde736f63331bd15793341af0b41249decfd95fe04e8a1f142d86a3ecd5f01`·`+163`／`−49`）。

## ⑨ 工項三″ 之 `checkidx`、`gen_fa_index`

```
$ python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md   ⇒ rc 0
索引列數 124；內部字樣 122；外部指標 9；不合 0
$ python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md                    ⇒ rc 0
則 124；加註節 14；列 158
$ cmp <O>/FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md ⇒ 逐位同
```

## ⑩ 各段耗時（並行 `2`）

| 段 | 時（+08:00） | 量 |
|---|---|---|
| 接單、開場、工項零″、一″ | 19:24〜19:28 | ≈ `5` 分 |
| 前置″ (甲)(乙) `18` 呼叫 | 19:28〜19:47 | 耗時之和 `1937` s |
| 撰碼（`R-3″`、`R-4″`）與自跑（`F39 selftest`） | 19:30〜19:40（與前置″ 並行） | ≈ `10` 分 |
| 驗 `91` 呼叫 | 19:48〜21:47 | 耗時之和 `14286` s |
| `V-4″`〜`V-8″` 之比 | 21:48〜21:52 | — |
| 唯讀獨立審查 | 21:52〜22:19 | ≈ `32` 分 |
| 工項二″ 之推、工項三″、四″ | 22:20〜 | — |

收工閘之實測值出艙於 `ops/queue` 之 `reports/W-G.9-395_補令一_回報.md`（⛔ 寫入本檔·自指）。
