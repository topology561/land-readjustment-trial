# `W-G.9-399_規格單` 執行端回報：**停機上呈**（停機款 `12`）

> 執行端（CC·雲端）·`2026-10-29`·effort=high。單 ＝ `ops/queue` 之 `orders/W-G.9-399_規格單.md`（`182866` B·`8cfb1582e13b…` ＝ `STATE.json`·`SELF_SHA256` `a4957106…` 依 `P-5` 自驗合）。
> **結論**：工項零、一已推新側支；工項二已撰、`commit`（`915bcd1`·**⛔ 推**）且其驗 `V-1`〜`V-9` 皆合期（`97` 呼叫皆合「施後」之列·本案配地⛔ 變）；唯**唯讀獨立審查之發現涉規格之漏載與域上之判斷**（下之 ⑥ W-1〜W-5）⇒ **停機款 `12`**（⛔ 自裁）。依 `§零-2` 末：已推之 `commit` ⛔ 撤；工項二⛔ 推、工項三／四⛔ 為。主線 `bd7da4d` ⛔ 動。

## ① `commit` 與推送

| 工項 | `commit` | 推送 |
|---|---|---|
| 零 | `6b159e2`（`docs/orders/W-G.9-399_規格單.md` 新·blob 之 `sha256` ＝ `8cfb1582…`） | `git push origin HEAD:refs/heads/verify/W-G.9-399-k960x`（新立）·推後 heads（濾後之母體）`57`、主線 `bd7da4d…` |
| 一 | `23f3fc84a294ce3c48d8c89cfbb8602c71b2b379`（`16` 檔·blob 皆 ＝ `§五-1` 項 `5`） | 快轉 `6b159e2..23f3fc8` |
| 二 | `915bcd1d1ecf6fba90a27290acd6544e5a099d3f`（`app.py` 唯一·`288`／`14`·施後 blob `95047cb9ae9cacb10f28ef7294fcf2f94c6dfe20`·`1922322` B） | **⛔ 推**（審查未符·`§四-1`「推（驗與審查皆符後）」）。其全文差異 ＝ 同目錄之 `W-G.9-399_規格單_回報_app.diff`（`34949` B·`sha256` `7f3b769fb6ffca44e0b030d5d491905eadf7eb9ea7308e5d1323a1ccc50c517b`·＝ `git diff 23f3fc8 915bcd1 -- app.py`；施於 `23f3fc8` 之 `app.py` 即得 blob `95047cb9…`）——雲端之容器為暫存，`915bcd1` 唯存於本輪之施工樹，故以此檔保其全文 |
| 三、四 | ⛔ 為 | — |

遠端（本回報時）：`verify/W-G.9-399-k960x` ＝ `23f3fc8`；主線 `wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`（⛔ 動）；heads（`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`）`57`（開工 `56` ＋ 新側支）。

## ② 停機款之三值（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `bd7da4d`；heads `56`、無新側支；追蹤檔無變動；`§零-0` 項 `3` `rc 0` 與四簿；旗標 `[None×5]`；環境可匯入 | 皆合：`bd7da4d…`；`56`（`<O>/heads_before_399.txt`）、新側支 `0` 列；`status` 空；`rc 0`·自誤 `629`／`644`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；`[None, None, None, None, None]`；裝後 `rc 0` |
| `2` | `SELF_SHA256`、bytes／`sha256`、入倉之 blob | 皆合（`a4957106…`；`182866`／`8cfb1582…`；`git cat-file blob` 之 `sha256` ＝ `8cfb1582…`） |
| `3` | 塊 `Fy57`／`K48`／`P59` 之 bytes／`sha256`／列數；`apply --check`；寫出後之 blob | 皆合：`Fy57` `80859`／`65629732…`／`1152`；`K48` `15358`／`1a1f8a17…`／`72`；`P59` `2902`／`c533677d…`／`16`；`--check` 過；`16` 檔之 blob ＝ 項 `5`、`status` 唯此 `16` 檔 |
| `4` | 前置 (甲)(乙) 合期；(丙) 沿用之前提；前置 `4` | 皆合（下之 ③） |
| `5` | 規格無歧義而涉域；⛔ 須改禁改 | 撰碼中未遇（R-8 之一處讀法見 ⑥ 之自捕 1·純顯示·⛔ 土地後果） |
| `6` | `V-1`〜`V-9` 皆合；本案配地⛔ 變 | 皆合（下之 ③）；本案配地⛔ 變 |
| `7` | `push` 之目標唯新側支／`ops/queue`；⛔ 被拒；主線⛔ 推進 | 合（二推皆至新側支·快轉；回報至 `ops/queue` 之推送被拒一次〔非快轉·他輪之門鈴之列〕⇒ `pull --rebase` 後成·⛔ `--force`） |
| `8` | 工項三之二檔 | **未及**（⛔ 為）；其預算（倉外）：`K-6` 典 `1025082` → `1040440`·blob `768b9e24…`、`待落地清單.md` `49281` → `52183`·blob `b89d9f85…`（＝ `§五-1` 項 `5`） |
| `9` | 收工閘 | **未及** |
| `10` | ⛔ 自判正典、⛔ 改塊／器／命令 | 合（⛔ 改之；R-8 之讀法見 ⑥） |
| `11` | 新檔⛔ 為 `check-ignore` 所命中 | 合（本單、新器皆 `rc 1`） |
| **`12`** | **唯讀獨立 reviewer 之發現⛔ 涉域上判斷或規格之漏載** | **成就**：W-1〜W-5（⑥）。執行端已自重現 W-1、W-2（實值同 reviewer） |
| `13` | 存取⛔ 被拒；寫入⛔ 為分類器所拒 | 合 |

## ③ 前置與驗之出艙（`<O>` ＝ `/tmp/claude-0/-home-user-land-readjustment-trial/f98ea94e-49be-56fb-9150-f8ef08266f3c/scratchpad/o399`·倉外·容器暫存）

- **`§零-0`**：`nproc` ＝ `4`；context 餘量充足（約 `14.9` M tokens）。環境：依 `requirements.txt` 裝後 `pip freeze` 之 `sha256` ＝ `9ad34edc…`（異於基準）⇒ 依 `§零-0` 項 `5` 之命令釘回（`rc 0`）＋ `pip uninstall -y tzdata`（`rc 0`）⇒ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（＝ 基準）；`Python 3.11.17`。pre-flight（`bd7da4d` 之器·`rc 0`）：🔴 `0`；🟡 `3`（`P-4` `:102`〔`§二` KL 之語之首〕、`:221`〔`§四-3` 之表之首〕、`:1534`〔塊 `K48` 之一之首〕——皆 `§五-1` 項 `9` 所具名豁免者；單之所記為 `4` 處〔另 `§一` 項 `5` 之突變之表之首〕而本定稿實出 `3` 處，其差唯在單所述之「定稿之前一版」·照實記之）；ℹ️ `P-5` ✅、`P-3` `24044`–`31788`。`§零-1` 之名皆 `0`（對照甲 `4`／`2`／`2`）、`docs/orders/W-G.9-399` 起首 `0`。
- **前置 (甲)(乙)**（工項一之端 `23f3fc8`·施工樹 `/tmp/w`·並行 `2`·`05:24:02`→`06:40:44`·耗時之和 `9199` s）：`51` 呼叫之 `rc`／`stderr`／末列 ＝ 「項 `8` 之表」之「工項一之端」之列，**不符 `0`**（`#95`／`#96`／`#97` ＝ `rc 1`·末列逐字同表）；`stderr` 合計 `0` B；`f8_pre_35.json` ＝ `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、`f8_pre_00.json` ＝ `186b090b68836f0ece2c0d23dad5573941995bf5`。
- **前置 (丙)**：主線之端 ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434` ＝ 基準之 sha；`Python 3.11.17` ＝；`pip freeze` `ae1438da…` ＝ ⇒ **沿用** `基準/bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434.md` 之 `46` 呼叫之值（⛔ 重跑）。
- **前置 `4`**：「k960_idx_first」「END_BLOCK_IDX_W_AREA」「end_block_end_geom」皆無出艙、`rc 1`。
- **驗**（`915bcd1`·`push` 前·殼無 `WV_`·並行 `2`·從頭整套照跑 `97` 呼叫·`06:58:52` 起；**容器於 `07:23`〜`07:28` 之間重啟一次**〔其時已完 `#67` 一呼叫·`rc 0`·`1446` s〕⇒ 逐呼叫落檔之器於 `07:28:12` 自未完者續跑〔已完之 `#67` 之落檔沿用·同一 `commit`·同一樹〕·`09:45:30` 畢·耗時之和 `17926` s）：
  - `V-1`／`V-2`：`97` 呼叫之 `rc`／`stderr`／末列 ＝ 「項 `8` 之表」之「施後」之列，**不符 `0`**；`F42 selftest` `P0 判式自驗 51／51`、`F42 wiring` `W1`〜`W6` ✅、`F42 run` `R1`〜`R3`（二退縮）✅；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`。
  - `V-3`：`16` 器之 blob ＝ `§五-1` 項 `5`（⛔ 改）。
  - `V-4`：`F36 diff` 3.5 m／0 m 皆 `rc 0`·`全比相異 0 項`；`cmp` 皆 `相異 0 項 ⇒ ✅ 同`。
  - `V-5`：`parity` 皆 `rc 0`·`⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置：`diff` 唯落檔之 `"head"` 列與 `stdout` 首列之態（`23f3fc84…` → `915bcd1d…`）；以同一字樣代 `HEAD` 之全值後逐位同（對照：⛔ 代之則 `head` 異）。
  - `V-6`：`run` 皆 `⇒ 紅 []；rc 0`；`hash-object` 3.5 m 二列皆 `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、0 m 二列皆 `186b090b68836f0ece2c0d23dad5573941995bf5`。
  - `V-7`：對 `23f3fc8` 相異唯 `M app.py`（`288`／`14`）；`verify/` 相異 `0`；頂層之名之增恰九、相異之節點恰十五（`F42 wiring` `W1`／`W2`·reviewer 以 AST 另驗同）。
  - `V-8`：「k960_idx_first」`6`、「END_BLOCK_IDX_W_AREA」`2`、「end_block_end_geom」`6`。
  - `V-9`：諸器之 `stderr` 合計 `0` B。
- `97` 呼叫之逐列之表（前置·驗二態之 `rc`／`stderr` B／末列／耗時 s）見附錄甲。

## ④ 塊之實得

`Fy57` `80859` B·`65629732a73cf3dd245133eeeb1c18c94ffeec4d8981d15156b5047d0f4e9536`·`1152` 列；`K48` `15358` B·`1a1f8a17a7befd877babec00359ad24e9a90458fde4458169c0dc0c9806d9886`·`72` 列；`P59` `2902` B·`c533677d2cb458c1aa069125075ac32bf0038c59b8ac3bd0b05f8a9cd60aafbc`·`16` 列；`CK` `1539` B·`00cd3949…`·`31` 列；`GF` `2445` B·`b11edb77…`·`47` 列（皆 ＝ `§五-1`）。工項三之二檔未寫入倉（⛔ 為）。

## ⑤ 推送之目標與 heads

見 ①。heads 之式：`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`；工項零推後 `57`。

## ⑥ 唯讀獨立審查之發現（停機之由）與執行端之自捕

**審查**（`redistribution-reviewer`·唯讀·受詞 ＝ `git diff 23f3fc8 915bcd1 -- app.py` 與 `§三`／塊 `K48`）之總判：R-1〜R-13 之實作皆合條文、無 BLOCKED；`§三-3` 各款以 AST 自驗皆合（頂層增九、相異十五、`main`／`end_block_side_geom` ⛔ 動、簽名唯 `end_block_apply` 增 `baseline_pts=None`、案件字面之增 `{}`）；獨立重算本案四端之端線 `R2` 右 `44.124`、`R3` 左 `43.914`、`R5` 右 `47.953`、`R6` 左 `47.706`（＝ 塊 `K48` 之四）。其列為**規格之漏載或域上之判斷**者五（⛔ 自裁·呈發單端）：

- **W-1　諸宗之臨端線之和得逾端線之長（分子之量法之容差所致）**。`R-6` 所定之分子 ＝ `_boundary_len_on_line(該宗 ∩ R_end, a, b)`（`perp_tol 0.05 m`·`ang_tol 2°`）——該宗於 `R_end` 內、距端線 5 cm 以內之平行之內邊亦被計入。例（reviewer `ex3.py`·**執行端自重現同值**）：`60 × 40` 之街廓、左之端線 `40`、`R_end 140`；寬 `0.03 m` 之條片 `S(1)`（跨占 `1.2` ㎡ ＞ 門檻 `1`）之臨端線 `80.0`、指數 `0.805143`；鄰宗 `A(1)` `40.0`／`0.737714`；`B(1)` `0.0`／`0.257143` ⇒ Σ臨端線 `120` ＞ 端線 `40`、Σ指數 `1.8` ＞ `1`，條片居第 1 名。`§三-5` 所令之「`R_end` 之端線之長 ＝ 諸宗之臨端線之長之和之上界」之證於此不成立。本案 Σ ≤ 1（`F42 run` 之 `R1`）⇒ 本案⛔ 受影響；他案之互相等待之先後可受影響。其改（如分子改取交集之外框與 `R_end` 之外框於端線上之公共部分）係改量之定義 ⇒ 屬規格。
- **W-2　BASELINE 之微小角差使端線靜默延至屁股線**。`R-2` ④ 之觸點 ＝ 交點 ∪ 距直線未逾 `0.05 m` 之頂點：BASELINE 過 `(20,30)` 而偏 `0.2°` 者（reviewer `ex1c.py`·**執行端自重現同值**）：`40 × 30` 矩形之左端線 `(0,29.93)–(0,0)` 長 `29.93`（可）；右端之角點 `(40,30)` 距直線 `≈ 0.07 m`（逾容差）⇒ 端線 `(40,0)→(40,30)→(20,30)` 長 `50.0`、`end_len` ＝ `33.5`（應 `30`）且⛔ 停機。本案 BASELINE 之源為 CAD 且與外框重合（遠端之距 `0.000`）⇒ 本案⛔ 受影響；畫面上手設之 BASELINE 有此險。
- **W-3　停機之面之擴大**。BASELINE 有給者，每一無側街之端於每一趟皆算端線（無互相等待亦然）⇒ FRONT 之端點距外框逾 `0.05 m`、或 BASELINE 畫於屁股線外逾 `0.05 m`（「無觸點」）者，**全案之配地即停**（合併再試之試算中止、定案再遇同一錯）——與塊 `K48` 之三之甲「BASELINE 未給 ⇒ 端線⛔ 算·列之指數為空」不對稱。`R-2`／`R-4` 之文確令停機；唯「僅供先後之量（及顯示）者阻全案」是否為本意，待裁。本案⛔ 觸發。
- **W-4　四位以上之環恆用不到評選指數**。每一競合恰二端 ⇒ 四環之不相鄰之二位無共同之端 ⇒ 「兩兩皆先者」恆不存 ⇒ 必依序鍵。合塊 `K48` 之三之戊之文；是否合 KL `22:42` 第 4 點「兩端、三端用同一規則」之本意，待確認。
- **W-5　（知悉）新序可較舊序生強制抵費地**：reviewer `ex2.py` 甲例——改前（序鍵）丁先 ⇒ 丁得 E、戊得 F、無強制；改後（評選指數·丁、戊各一端第 1 名 ⇒ 面積 戊 `80` ＞ 丁 `72`）戊先 ⇒ 戊得 E、F 皆未達 ⇒ 強制抵費地 `180` ㎡（＝ 附錄丁之形·KL 所定之規則之果·非瑕）。同例另證非共同之端（BG 右·丁第 1 名）⛔ 計入（計之則丁二端第 1 而先）。

純實作之瑕（NOTE·⛔ 擋·⛔ 修）：手造之異常輸入（二位之環之競合之 `'面積表'` 為 `None`、街廓為 `MultiPolygon`、`baseline_pts` 不可取長度）拋 `TypeError`／`AttributeError` 而非 `RuntimeError`（生產路徑皆⛔ 至）；`f3_manual_baseline` 之 `enabled` 未檢（`n19p_depth_info_by_label` 亦然·同源）；指數之和用內建 `round` 而面積用 `adj_q2`（同街角之慣例）。reviewer 另註：二位之競合結構上無「非共同之目標端」（三個以上之目標端即停機·`ex2.py` 乙例改前改後皆「三個以上之末端塊」停機）⇒ 塊 `K48` 之五 `#140` 於二位時唯及非目標端；名次之單位取合併群係塊 `K48` 之三之丙之讀法。

reviewer 之自首：其曾於 `/tmp/w` 跑 `py_compile` 而生 `__pycache__/`（gitignored）⇒ 即刪；`git status --porcelain` 空、`HEAD` 仍 `915bcd1`。

**執行端之自捕與自解**：
1. **R-8 之讀**：撰碼初以「`端線(m)` 為 `None` 或缺鍵 ⇒ 『端線 — m；』」實作，撰碼中自跑 `F12 selftest`（`S14`）、`F13 selftest`（`S8`）轉紅——二器之手造紀錄無 `端線(m)` 之鍵而期改前之原句（二器非塊 `Fy57` 所改·`V-2` 之期 `rc 0`）。⇒ 改為「有鍵而值 `None` ⇒ `—`；無鍵（改前之紀錄）⇒ ⛔ 列此段」（生產碼之紀錄恆寫此鍵）。純顯示·⛔ 土地後果；reviewer 判之合規格之整體。請發單端知悉（`§三-1` R-8 之「缺 ⇒ —」之讀）。
2. **`§三-3` 第 `1` 款之錨**：撰碼中自跑 `F23 wiring` `W8` 紅——錨「`trial=_trial, cache=_cache, allow_forced=_allow)`」（`end_block_host`）因 `baseline_pts=` 置其後而失 ⇒ 移 `baseline_pts=_bl399` 於其前；另以自寫之掃描（各所改之函式內，器之字串常數之計數之增）去三處可疑之增（`k6_merge_groups(_pk, own_map)` 之二見〔改為於既有之求群之迴圈內錄單位之表·⛔ 再呼〕、docstring 中之「`跨占R_end(㎡)`」「互相等待 ⇒ 先處理」）。其後 `F23`／`F24 wiring` 皆綠。
3. **並行之限**：前置之跑中，執行端於另一工作樹（`/tmp/wdev`）自跑撰碼中之查（`F42 selftest`／`wiring`／`run`、`F39`、`F23`／`F24 wiring`）⇒ 一時同時之程序 `3`〜`4`（逾 README 第六節第 `3` 款之 `2`）——前置之 `#18`／`#77` 之耗時因之約倍（`781`／`818` s）；前置之 `51` 呼叫之結果皆合期（⛔ 逾時）。其後之自跑皆於前置畢後、驗前為之（並行 `2`）。驗之 `97` 呼叫期間⛔ 他負載。
4. **heredoc**：單首 🔑 令「Bash 命令⛔ 含 heredoc」；執行端於倉外之工具（`STATE.json` 之改、暫存之腳本之寫與改）曾以 heredoc 為之（⛔ 及量測之命令·⛔ 及倉內之檔）。照實記之。
5. **容器之重啟**：驗之中途一次（見 ③）；逐呼叫落檔之器自未完者續跑（已完之 `#67` 沿用）。
6. 本機之耗時約為單之所載之 `2` 倍（前置 `9199` s 對單之 (甲) `3573` ＋ (乙) 基準 `837`；驗 `17926` s 對 `9163` s），非負載所致者亦然（驗之期間⛔ 他負載）。

## ⑦ 設計說明（`§三-5`·工項二 `915bcd1`）

- **R-1**：`SS_END_BLOCK_MERGE` 之定義之次列起，三句之賦值 `END_BLOCK_LINE_TOL = 0.05`、`END_BLOCK_IDX_W_LINE = 0.4`、`END_BLOCK_IDX_W_AREA = 0.6`，各附註其義與所據。
- **R-2 `end_block_end_line`**（置 `end_block_side_geom` 之後）：缺件／`baseline_pts` 非二點／二點重合 ⇒ 停；`end_pt` 距外框（`LineString(exterior)` 之 `distance`）＞ 容差 ⇒ 停（「距街廓外框」）；`end_pt` 距 BASELINE 之無限直線 ≤ 容差 ⇒ 停（「已觸 BASELINE」）。觸點之候選 ＝ 外框與該直線（延至涵蓋外框之長之線段）之交（`Point` 取之；`LineString`〔共線〕取其二端；集合者逐其子）∪ 外框之頂點之距直線 ≤ 容差者；無 ⇒ 停（「未觸 BASELINE」）。向：`s0 ＝ project(end_pt)`、`so ＝ project(other_pt)`（他端點⛔ 驗其距）；順向 ＝ `(s − s0) mod L`、逆向 ＝ `(s0 − s) mod L`；各取至觸點之最小者與至他端點者；「前者 ＜ 後者」之向恰一 ⇒ 該向，否則停。段：以 `shapely.ops.substring` 取 `[a, b]`；跨外框之始末者（`b ＞ L` 或 `a ＜ 0`）分二段取之後以 `linemerge` 合之；長 ≤ 容差 ⇒ 停。
- **R-3 `end_block_end_segs`**：逐 `LineString`（`MultiLineString` 逐其子）之相鄰二點為一段，⛔ 取長 0 者。
- **R-4 `end_block_end_geom`**：`baseline_pts is None` ⇒ 即回 `{'end_segs': None, 'end_len': None}`（⛔ 觸他新名·`F12` 唯抽此函式）；否則端點：左 ＝ `corner_pt`、右 ＝ `corner_pt ＋ (d̂·(front_p2 − corner_pt))·d̂`（同 `end_block_side_geom`），他端點為其另一；`end_len ＝ Σ _boundary_len_on_line(r_end, a, b)`；≤ 容差 ⇒ 停。
- **R-5 `end_block_apply`**：增 `baseline_pts=None`；`_geo393[端]` ＝ `dict(end_block_side_geom 之所回, **end_block_end_geom(…, r_end, baseline_pts))`；首趟之紀錄於 `R_end(㎡)` 之次增 `端線(m)`（2 位／`None`）。
- **R-6 `end_block_pick`**：跨占之列於 `跨占R_end(㎡)` 之次增二欄：`geom.get('end_segs')` 真 ⇒ `臨端線(m)` ＝ `Σ _boundary_len_on_line(R_end ∩ 該宗, a, b)`（2 位）、`評選指數` ＝ `0.4 × 未取位之臨端線 ÷ end_len ＋ 0.6 × 未取位之跨占 ÷ r_end_area`（6 位）；否則皆 `None`；歸街角側之列亦增之（其後之 `update` 照舊）。同源之證：分子、分母皆以同一 `end_segs` 經同一 `_boundary_len_on_line` 量之；分子之受詞 ⊂ `R_end` ⇒ 其外框之落於端線者，於「無距端線 5 cm 內之內邊」之形為 `R_end` 之外框之落於端線者之子集 ⇒ 和 ≤ 分母（本案四端皆然：`R2` 右 `10.42` ≤ `44.12`…）；**其反例 ＝ W-1**（規格層）。
- **R-7 `end_block_host`**：`_baseline_pts_from_manual((session.get('f3_manual_baseline') or {}).get(街廓), list(blk_poly.exterior.coords))` ⇒ `baseline_pts`（置於錨句「`trial=_trial, cache=_cache, allow_forced=_allow)`」之前）。
- **R-8 `end_block_eval_rows`**：「＝ R_end … ㎡；」之次增「端線 <值> m；」（值 `None` ⇒ `—`；無鍵 ⇒ ⛔ 列·見 ⑥ 自捕 1）。
- **R-9 `k960_idx_rank`**：唯 `未達`；單位 ＝ `group_of.get(p, ('單', p))`；`評選指數` 為 `None` ⇒ 停（「評選指數取不到」）；鍵 ＝ `(−round(和, 4), 首列之索引)`；回 `{單位: {'名次','指數'(6 位),'片'}}`。
- **R-10 `k960_idx_key`／`k960_idx_first`**：鍵 ＝ `(0, −第1名之端數)` 或 `(1, 名次之和)` ＋ `(−adj_q2(k967_pre_area(p, 共同之端之片之集〔排序·一片一次〕, area_of)), −round(指數之和, 4), str(p))`；`first`：任一 `評選` 非 `dict` ⇒ 停（「缺末端塊評選指數」＋其 `評選之誤`）；共同之端 ＝ 二者之鍵之交（排序）·空 ⇒ 停（「無共同跨占之端」）；`key(Y) ＜ key(X)` ⇒ `(Y, X, 共同)`，否則 `(X, Y, 共同)`。
- **R-11 `end_block_merge_run`**：單位之表之源 ＝ 既有之求群之迴圈（`for _g in k6_merge_groups(_pk, own_map)`·⛔ 再呼）之每一群錄 `{暫編地號: ('群', 群之最小索引)}`；有競合者每一競合載 `p` ＝ `序鍵[2]`、`面積表` ＝ 序鍵之表、`評選` ＝ `{(街廓, 端): k960_idx_rank(該端之首次之試算之候選之列, 表)[本群之單位]}`；`RuntimeError` ⇒ `評選` ＝ `None`、`評選之誤` ＝ 首列。`rec['競合']` 之形照舊。
- **R-12 `_ring395`**：環長 `2` ⇒ `k960_idx_first`（其先者之索引）；`≥ 3` ⇒ 任一 `評選` 非 `dict` ⇒ 停；依環之序，對其餘每一位皆「有共同之端且 `k960_idx_first(其, 彼)[0] is 其`」之首見者 ⇒ 先；無之 ⇒ 既有之「缺序鍵」之停與 `min(序鍵)`（原句照留）。列之 `競合` ＝「先處理 X（<由>）；延後 Y 退至 Z 之後」，由 ＝「評選指數之序（共同之端 …）」／「三位以上 ⇒ 兩兩之評選指數皆先」／「三位以上·兩兩比較成圈 ⇒ 序鍵 …」。
- **R-13**：諸新函式與所改之函式之 docstring 載 KL `2026-10-26` 之時刻與 `W-G.9-399`；新巢狀之名 `_off399`、`_collect399` 全檔各一見。
- **本案之量**（`F42 run`·二退縮同）：`R2` 右 端線 `44.12`·`628-34(1)` `10.42`／`0.372619`；`R3` 左 `43.91`·`628-34(2)` `34.94`／`0.799606`；`R5` 右 `47.95`·`628-23(2)` `0.0`／`0.023134`；`R6` 左 `47.71`·`628-23(1)` `0.0`／`0.114893`、`628-4(1)` `0.0`／`0.056826`（＝ 塊 `K48` 之四）。
- **`§三-3` 之自查**：第 `1` 款 `F23`／`F24 wiring` 綠（⑥ 自捕 2）；第 `2` 款 突變之器（`#19`、`#22`、`#43`、`#47`）皆合期；第 `3` 款 `main`／`end_block_side_geom` ⛔ 動；第 `4` 款 `F42 wiring` `W1`／`W2`；第 `5` 款 `W5` `{}`；第 `6` 款 簽名唯 `end_block_apply` 增 `baseline_pts=None`。

## ⑧ `app.py` 之全文差異

同目錄之 `W-G.9-399_規格單_回報_app.diff`（見 ①）。

## ⑨ 工項三之出艙

未及（⛔ 為）。

## ⑩ 各段耗時（並行）

開工 `05:17`（接單）；`§零`〜工項一 `05:17`〜`05:30`；前置 `05:24:02`〜`06:40:44`（並行 `2`·另有撰碼中之自跑·⑥ 自捕 3）；撰碼與自跑 `05:30`〜`06:58`；驗 `06:58:52`〜`09:45:30`（並行 `2`·容器重啟一次）；審查 `09:46`〜`09:59`；回報 `10:0x`。

## 附錄甲　`97` 呼叫之表（前置·驗）

格 ＝ `rc`／`stderr` B／末列（耗時 s）。(甲)(乙) ＝ 本輪實跑於 `23f3fc8`；(丙) ＝ 沿用基準。驗 ＝ 本輪實跑於 `915bcd1`。

| # | 命令 | 工項一之端（前置） | 施後（驗） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（184） | `0`／`0`／`⇒ 紅 []；rc 0`（152） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（430） | `0`／`0`／`⇒ 紅 []；rc 0`（424） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（32） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（34） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（44） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（17） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（286） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（83） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（559） | `0`／`0`／`⇒ 紅 []；rc 0`（539） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（781） | `0`／`0`／`⇒ 紅 []；rc 0`（766） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | (甲) `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（11） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（72） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（470） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2106） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（38） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（26） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（25） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（304） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（407） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（54） | `0`／`0`／`⇒ 紅 []；rc 0`（54） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（51） | `0`／`0`／`⇒ 紅 []；rc 0`（41） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（26） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（17） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（228） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（59） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（982） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（194） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（128） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（416） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`紅項 [] 器紅 0`（11） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（413） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | (乙) `0`／`0`／`（JSON 之摘要列·略）`（251） | `0`／`0`／`（JSON 之摘要列·略）`（233） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | (乙) `0`／`0`／`（JSON 之摘要列·略）`（199） | `0`／`0`／`（JSON 之摘要列·略）`（175） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | (乙) `0`／`0`／`⇒ 紅 []；rc 0`（276） | `0`／`0`／`⇒ 紅 []；rc 0`（235） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | (乙) `0`／`0`／`⇒ 紅 []；rc 0`（195） | `0`／`0`／`⇒ 紅 []；rc 0`（171） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | (乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（514） | `0`／`0`／`⇒ rc 0（不符 0 項）`（502） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | (乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（392） | `0`／`0`／`⇒ rc 0（不符 0 項）`（360） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（436） | `0`／`0`／`⇒ 紅 []；rc 0`（405） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1446） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1443） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（185） | `0`／`0`／`⇒ 紅 []；rc 0`（162） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（537） | `0`／`0`／`⇒ 紅 []；rc 0`（525） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（455） | `0`／`0`／`⇒ 紅 []；rc 0`（407） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（56） | `0`／`0`／`⇒ 紅 []；rc 0`（64） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（818） | `0`／`0`／`⇒ 紅 []；rc 0`（808） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（10） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（455） | `0`／`0`／`⇒ 紅 []；rc 0`（411） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（437） | `0`／`0`／`⇒ 紅 []；rc 0`（405） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（442） | `0`／`0`／`⇒ 紅 []；rc 0`（403） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（476） | `0`／`0`／`⇒ 紅 []；rc 0`（410） |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（11） | `0`／`0`／`⇒ 紅 []；rc 0`（9） |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（411） | `0`／`0`／`⇒ 紅 []；rc 0`（401） |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（2） |
| `92` | `python3 verify/probes/probe_WG9398_rw25.py selftest <repo>` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `93` | `python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf` | (甲) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `94` | `python3 tests/test_pool_slot.py` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`（1） |
| `95` | `python3 verify/probes/probe_WG9399_k960x.py selftest <repo>` | (甲) `1`／`0`／`⇒ 紅 ['E1', 'E1′', 'E1″', 'E2', 'E3', 'E4', 'E5', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E7', 'E8', 'E8′', 'E9', 'E10', 'P1', 'P2', 'P3', 'P4', 'P5', '丙·例外', '丁·例外', 'M1', 'M2', 'M4', 'M6', 'M8']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `96` | `python3 verify/probes/probe_WG9399_k960x.py wiring <repo> bd7da4d` | (甲) `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4']；rc 1`（25） | `0`／`0`／`⇒ 紅 []；rc 0`（19） |
| `97` | `python3 verify/probes/probe_WG9399_k960x.py run <repo>` | (甲) `1`／`0`／`⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`（412） | `0`／`0`／`⇒ 紅 []；rc 0`（404） |

## 附錄乙　reviewer 之重現之腳本（倉外 `/tmp/rv399/`·W-1 ＝ `ex3.py`、W-2 ＝ `ex1c.py`、W-5 ＝ `ex2.py`·其 `new_app.py` ＝ `915bcd1` 之 `app.py`）

### `ex3.py`（W-1）

````python
import sys, io, contextlib
sys.dont_write_bytecode = True
sys.path.insert(0, '/tmp/w/verify')
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns, _ = harvest('/tmp/rv399/new_app.py')
from shapely.geometry import Polygon
import numpy as np
R = lambda x0,x1,y0,y1: [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
blk = Polygon(R(0,60,0,40)); cad = np.array((0.,1.)); dh = np.array((1.,0.))
parts = [("S(1)", R(0,0.03,0,40)), ("A(1)", R(0.03,2,0,40)), ("B(1)", R(2,60,0,40))]
ents = [{"tp": {"暫編地號": p, "原地號": p[0], "polygon_coords": [list(c) for c in co]}, "pre_position": 0,
         "is_corner_winner": False, "side": "中段"} for p, co in parts]
cache = {}
ns['end_block_apply'](ents, blk_label="X", block_poly=blk, d_hat=dh, corner_pt=np.array((0.,0.)), front_p2=np.array((60.,0.)),
    cad_alloc=cad, allocation_dir=ns['alloc_normal_axis'](cad), min_width=3.5,
    has_side_pk={"left": False, "right": False}, has_side_cad={"left": False, "right": False}, corner_range_polys={},
    trial=lambda tp, s, w: (1.0, 5.0), cache=cache, allow_forced=lambda s: True, baseline_pts=[(-50,40),(110,40)])
r = cache['X']['left']
print('端線', r['端線(m)'], 'R_end', r['R_end(㎡)'])
tot_l = tot_i = 0
for x in r['候選']:
    print(x['暫編地號'], x['跨占R_end(㎡)'], x['臨端線(m)'], x['評選指數'], x['結果']); tot_l += x['臨端線(m)']; tot_i += x['評選指數']
print('Σ臨端線', round(tot_l,2), 'Σ指數', round(tot_i,6))
````

出艙（執行端自重現）：`端線 40.0 R_end 140.0`／`S(1) 1.2 80.0 0.805143 未達`／`A(1) 78.8 40.0 0.737714 未達`／`B(1) 60.0 0.0 0.257143 未達`／`Σ臨端線 120.0 Σ指數 1.8`

### `ex1c.py`（W-2）

````python
import sys, io, contextlib, math
sys.dont_write_bytecode = True
sys.path.insert(0, '/tmp/w/verify')
from app_harvest import harvest
with contextlib.redirect_stdout(io.StringIO()):
    ns, _ = harvest('/tmp/rv399/new_app.py')
from shapely.geometry import Polygon
import numpy as np
blk = Polygon([(0,0),(40,0),(40,30),(0,30)])
cad = np.array((0.0,1.0)); dh = np.array((1.0,0.0))
t = math.tan(math.radians(0.2))
bl = [(20-100, 30-100*t), (20+100, 30+100*t)]   # through (20,30), 0.2 deg
for sd in ('left','right'):
    g = ns['end_block_side_geom'](blk, dh, np.array((0.,0.)), np.array((40.,0.)), cad, ns['alloc_normal_axis'](cad), 3.5, sd, _label='X')
    eg = ns['end_block_end_geom'](blk, dh, np.array((0.,0.)), np.array((40.,0.)), sd, g['r_end'], bl, _label='X')
    ln = ns['end_block_end_line'](blk, (0.,0.) if sd=='left' else (40.,0.), (40.,0.) if sd=='left' else (0.,0.), bl)
    print(sd, 'end line', [tuple(round(x,3) for x in c) for c in ln.coords], 'len', round(ln.length,3), 'end_len(R_end)', round(eg['end_len'],3))
    # parcel at right end touching back edge: [36.5,40]x[0,30] single parcel -> its 臨端線
````

出艙（執行端自重現）：`left end line [(0.0, 29.93), (0.0, 0.0)] len 29.93 end_len(R_end) 29.93`／`right end line [(40.0, 0.0), (40.0, 30.0), (20.0, 30.0)] len 50.0 end_len(R_end) 33.5`

### `ex2.py`（W-5）

````python
import sys, io, contextlib, copy, json
sys.dont_write_bytecode = True
sys.path.insert(0, '/tmp/w/verify')
from app_harvest import harvest
path, variant = sys.argv[1], sys.argv[2]
with contextlib.redirect_stdout(io.StringIO()):
    ns, _ = harvest(path)
H = "住宅區"
def tp(pid, blk, cat, poly, a, ap=0.0):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(map(float, c)) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": float(ap)}
R = lambda x0,x1,y0,y1: [(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
# BE: x[0,40] y[0,30]; road RX y[-10,0]; BF: y[-40,-10]; BG: x[-30,0] y[0,30] (left of BE; its RIGHT end touches BE)
T = [tp("D1(1)","BE",H,R(0,5,0,30),36, ap=20.0),     # 丁 G = 56
     tp("U1(1)","BE",H,R(5,10,0,30),40),             # 戊 G = 40
     tp("P(1)","BE",H,R(10,40,0,30),900),
     tp("Dr(1)","RX","道路",R(0,5,-10,0),60), tp("Ur(1)","RX","道路",R(5,10,-10,0),150), tp("R0(1)","RX","道路",R(10,40,-10,0),300),
     tp("D2(1)","BF",H,R(0,5,-40,-10),36),           # 丁 G = 36  => 丁 ΣG(E,F)=92, ΣA=72
     tp("U2(1)","BF",H,R(5,10,-40,-10),40),          # 戊 G = 40  => 戊 ΣG=80, ΣA=80
     tp("Q(1)","BF",H,R(10,40,-40,-10),900),
     tp("Dg(1)","BG",H,R(-5,0,0,30),10),             # 丁 in BG, shares x=0 with D1 -> same 合併群
     tp("W(1)","BG",H,R(-30,-5,0,30),500)]
own = {"D1":"g丁","Dr":"g丁","D2":"g丁","Dg":"g丁","U1":"g戊","Ur":"g戊","U2":"g戊","P":"gP","R0":"gR","Q":"gQ","W":"gW"}
blocks = {"BE":{"category":H},"BF":{"category":H},"BG":{"category":H},"RX":{"category":"道路"}}
cl = {"RX":[(-40.0,-5.0),(50.0,-5.0)]}
targets = {("BE","left"): dict(thr=90, cands=["D1(1)","U1(1)"], idx={"D1(1)":0.6,"U1(1)":0.3}),   # 丁 #1 at E
           ("BF","left"): dict(thr=180, cands=["U2(1)","D2(1)"], idx={"U2(1)":0.6,"D2(1)":0.3})}  # 戊 #1 at F
if variant == "G_winner":     # 丁 also crosses BG right end, idx-first there, but W wins BG (non-target end)
    targets[("BG","right")] = dict(thr=100, cands=["Dg(1)","W(1)"], idx={"Dg(1)":0.9,"W(1)":0.1})
elif variant == "G_target":   # BG right end also all-fail -> 丁's group spans 3 target ends
    targets[("BG","right")] = dict(thr=10**6, cands=["Dg(1)","W(1)"], idx={"Dg(1)":0.9,"W(1)":0.1})
def g(t): return float(t.get("分攤登記面積_m2",0) or 0) + float(t.get("面積_m2",0) or 0)
def a_prime(src, dst): return g(src)
def alloc_eval(temp, build):
    by = {b["暫編地號"]: b for b in build}; out = {}
    for (blk, sd), cfg in targets.items():
        rows, win = [], None
        for c in cfg["cands"]:
            if c not in by: continue
            ok = g(by[c]) >= cfg["thr"]
            rows.append({"暫編地號": c, "原地號": by[c]["原地號"], "跨占R_end(㎡)": 10.0, "評選指數": cfg["idx"].get(c),
                         "試算G(㎡)": round(g(by[c]),2), "臨正街寬(m)": 5.0, "結果": "當選" if ok else "未達"})
            if ok: win = c; break
        out.setdefault(blk, {})[sd] = {"觸發": True, "R_end(㎡)": cfg["thr"], "候選": rows, "當選": win}
    return out
def alloc_state(temp, build):
    kept = {}
    for b in build: kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"])
    return {"kept": kept, "bad_pools": {}, "err": None, "G": {b["暫編地號"]: g(b) for b in build}}
temp = copy.deepcopy(T); build = [t for t in temp if t["街廓分類"] == H]
cap = {}
orig = ns["k6b_stage3_run"]
def spy(*a, **k):
    cap["contests"] = k.get("contests")
    return orig(*a, **k)
ns["end_block_merge_run"].__globals__["k6b_stage3_run"] = spy
try:
    t2, b2, log, rec = ns["end_block_merge_run"](temp, build, own, set(), set(), blocks, cl, a_prime, alloc_eval, alloc_state,
                                                 setback=3.5, log_print=lambda *x: None)
    res = {"rows": [(x.get("候選"), x.get("層級"), x.get("結果"), x.get("競合")) for x in log if x.get("序") != "後處理"],
           "won": sorted({(x["街廓"], x["端"], x["候選"]) for x in log if x.get("結果") == "成" and x.get("序") != "後處理"}),
           "皆未達": rec.get("皆未達"), "rec競合": rec.get("競合"),
           "contests": [{k: (('<tbl>') if k == '面積表' else ({str(kk): vv for kk, vv in v.items()} if (k == '評選' and isinstance(v, dict)) else v)) for k, v in c.items()} for c in (cap.get("contests") or [])]}
except Exception as ex:
    res = {"err": f"{type(ex).__name__}: {str(ex)[:300]}"}
print(json.dumps(res, ensure_ascii=False, indent=1, default=str))
````
