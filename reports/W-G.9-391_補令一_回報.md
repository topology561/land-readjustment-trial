# `W-G.9-391_補令一` 回報（執行端·**完成**）

- **受單**：`ops/queue` 之 `orders/W-G.9-391_補令一.md`；bytes `25718`、`sha256` `ca7d777ca189fbc2fa27f08dd083a6009dda14ce2df99c3832d4872dd85380fe` ＝ `STATE.json` 之 `order_bytes`／`order_sha256`；`SELF_SHA256`（`P-5` 原口徑·受詞 `25640` B）實算 `acb99fd38776a34669a3330edfd365662ba82ecb2d0f7ed4c87f085b717eddda` ＝ 單載；`CR` `0`。
- **主線**：`wip/s1-endpart` **`a8657c4012d961eccebd77cd812c0ab6aeab030f` → `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`**（快轉·⛔ `--force`）。
- **側支**：`verify/W-G.9-391-k980x` `b95b44d9c352ae951492d9acca28b8f3e0260f00` → `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（快轉·保留）。
- **本案配地**：⛔ 變（本補令零生產碼；新主線之生產碼 `34` 檔 ≡ `a65e3c7`）。

## `§零″` 開場

1. context 餘量：充裕（約 `14.9M` tokens）；`nproc` ＝ `4`；`effort=high`。
2. `origin/wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`；`origin/verify/W-G.9-391-k980x` ＝ `b95b44d9c352ae951492d9acca28b8f3e0260f00`；遠端 heads ＝ `51`（全列存 `<O>/heads_before_391p1.txt`·`<O>` ＝ `/tmp/O`）；`git checkout --detach origin/verify/W-G.9-391-k980x` 後 `git status --porcelain --untracked-files=no` ＝ 空；旗標之出艙 ＝ `[None, None, None, None, None]`。
3. `probe_WG9321_issuer_anchor.py /tmp/w /tmp/O/anchor_open.txt 634 629` ⇒ `rc 0`（`stderr` `0` B）；「項4′ 四簿·正典框」：自誤 `619`／`634`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]` ＝ 期。
4. bytes／`sha256`／`SELF_SHA256` 皆符（見上）。
5. 環境：首驗 `import shapely…` 失敗（`ModuleNotFoundError: shapely`）⇒ 依 README 第六節第 2 款 `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ 再驗 `rc 0`；Python `3.11.17`。
6. `probe_order_preflight.py`（本補令之施工樹根之複本）⇒ `rc 0`、`stderr` `0` B；🔴 `0` 項／🟡 `0` 項／ℹ️ `2` 項（`P-5` ✅ 相符·受詞 `25640` B；`P-3` `def main` ＝ `23691`–`31434`）＝ `§五″` 項 `3`。
   - 施工樹根之複本以 `.git/info/exclude` 之 `/W-G.9-391_補令一.md` 免之（`git status --porcelain` 全空）。

## 工項零″（側支·零生產碼）

- `docs/orders/W-G.9-391_補令一.md` 二進位複製；`git check-ignore -v --no-index` ⇒ `rc 1`（無命中）；`git status --porcelain --untracked-files=no` 唯 `A  docs/orders/W-G.9-391_補令一.md`。
- `commit` **`56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`**，首列逐字 `W-G.9-391 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼`（其後空一列·環境之尾列二）；`git cat-file blob HEAD:docs/orders/W-G.9-391_補令一.md` 與來源 `cmp` 逐位同。
- `git push origin HEAD:verify/W-G.9-391-k980x` ⇒ `b95b44d..56c77fd`（快轉）。

## 工項一″（主線快轉）

**前置**（`<C>` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`·出艙存 `/tmp/O/pre1.out`、`pre3_*.txt`、`pre4_diff.txt`）：
1. `fetch` 後 `origin/verify/W-G.9-391-k980x` ＝ `<C>`；`origin/wip/s1-endpart` ＝ `a8657c4012d961eccebd77cd812c0ab6aeab030f`。
2. `merge-base --is-ancestor a8657c4 <C>` ⇒ `rc 0`；`rev-list --count a8657c4..<C>` ＝ `6`；反向 ＝ `0`；`--merges` ＝ 空。
3. 逐筆 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`：`56c77fd` `0`、`b95b44d` `0`、`54812a4` `0`、**`a65e3c78bdc2ab06328ce442358245ddb236f831` `3`**（`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）、`a749c78` `0`、`65b1f25` `0` ⇒ 命中恰 `1` 筆。
4. `<C>:app.py` ＝ `b591d7605b932b42c9dc205bb8589ef04505045b`；`<C>:verify/run_verification.py` ＝ `ef043da43e69f236550d0f420f6684f2edd271e4`；`<C>:verify/stepg_pipeline.py` ＝ `b2f6622351d1bcdcdf7b603c7412a8f902aa2edc`；`git diff --name-only a65e3c7 <C> -- app.py ":(glob)verify/*.py" verify/` ＝ 空。
- 快轉前 `git branch -r --contains a65e3c7` ＝ 唯 `origin/verify/W-G.9-391-k980x`。

**快轉前之記**：`ops/queue` `log.md` 增一列、`STATE.json` `history` 增一筆（`running` → `running`·「主線 `a8657c4012d961eccebd77cd812c0ab6aeab030f` → `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81`（將快轉）」）⇒ `commit` `74e88cd`（首列 `ops: 執行端快轉前之記 W-G.9-391_補令一`）⇒ 推送 `1a502c8..74e88cd`。

**快轉**：`git push origin 56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81:refs/heads/wip/s1-endpart` ⇒ `a8657c4..56c77fd`（⛔ `--force`·未被拒）。

**快轉後即出艙**：
- ① `git ls-remote origin refs/heads/wip/s1-endpart` ＝ `56c77fd10f8cc35e8e02d7f7b86a75d9b0b40d81` ✅
- ② 遠端 heads ＝ `51` ✅
- ③ 生產碼 `34` 檔（`app.py` ＋ `verify/*.py` `33` 檔）新主線 vs `a65e3c7` 相異 `0` ✅；判別力 vs `a8657c4` 相異 `3`（`app.py`、`verify/run_verification.py`、`verify/stepg_pipeline.py`）✅
- ④ `git branch -r --contains a65e3c7` ＝ `origin/verify/W-G.9-391-k980x`、`origin/wip/s1-endpart` ✅

## `§三-1″` 收工閘（於主線之端 `56c77fd`）

| 閘 | 實值 | 判 |
|---|---|---|
| `1″` | `git show --numstat`：`119`␉`0`␉`docs/orders/W-G.9-391_補令一.md`·唯此一檔；首列逐字合 | ✅ |
| `2″` | `diff --name-status b95b44d HEAD` 恰 `A`␉`docs/orders/W-G.9-391_補令一.md`；生產碼與 `verify/` 對 `b95b44d` 相異 `0`；判別力：生產碼對 `a8657c4` `3`、`verify/` 對 `a8657c4` `14`（`M` `13`·`A` `1`）；本補令 `check-ignore` `rc 1`；判別力 `verify/__pycache__/x.pyc` ⇒ `rc 0`·`.gitignore:18:__pycache__/` | ✅ |
| `3″` | 本補令 blob 之 `CR` ＝ `0`（判別力 `data/V6.dxf` ＝ `12308`） | ✅ |
| `4″` | 全樹對 `b95b44d` 唯本補令一檔之異 ⇒ 四簿、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md` 相異 `0`；`CLAUDE.md` `00e627af607baecde4f0138c1f706c851d320350`、`K-6` 典（`docs/rulings/K-6_街角地分配程序與可分配判準.md`）`0fad1dafd3c6236b571969b1538170f8662d9ee6`、自誤簿（`docs/reports/W-G.9波_claude.ai側自誤登記.md`）`c5406d05c024dae897beb3c1175934ece7c0819b`、`docs/待落地清單.md` `48b50c3da80dff7143b82fc9eeba00673750a158` ＝ 期 | ✅ |
| `5″` | 遠端 heads `51`；主線 ＝ 側支 ＝ `56c77fd`；其餘 `48` 列（除主線、側支、`ops/queue`）與 `heads_before_391p1.txt` 逐列同（`cmp` 同） | ✅ |
| `6″` | `probe_WG9270_closegate.py 634 629 .` ⇒ `rc 0`·末列 `✅ 二閘皆過`·`stderr` `0` B；判別力 `635 634 .` ⇒ `rc 7` | ✅ |
| `7″` | `probe_WG9321_issuer_anchor.py /tmp/w /tmp/O/anchor_close.txt 634 629` ⇒ `rc 0`·`stderr` `0` B；四簿 ＝ `§零″` 項 `3`（⛔ 變） | ✅ |
| `8″` | `25` 呼叫（並行 `2`·牆鐘 `246` s）皆 `rc 0`、末列皆 `⇒ 紅 []；rc 0`、`stderr` 合計 `0` B；`P0`：`k953` `75／75`、`k965` `74／74`、`k948` `35／35`、`k966` `31／31`、`partrem` `29／29`、`k961s3` `31／31`、`trialstop` `16／16`、`k961r` `14／14`、`k980x` `22／22`；`k961s3 selftest` `K1`〜`K31`、`trialstop selftest` `K1`〜`K16`、`k961r selftest` `L1`〜`L14`、`k961r wiring` `X1`〜`X4`、`k980x selftest` `C1`〜`C9`／`E1`〜`E6`／`T1`〜`T6`／`K1`、`k980x wiring` `W1`〜`W9` 皆 ✅；全出艙 `❌` `0` 處 | ✅ |

`8″` 逐呼叫之耗時（s）：`01` 3·`02` 117·`03` 2·`04` 34·`05` 35·`06` 3·`07` 2·`08` 2·`09` 2·`10` 1·`11` 4·`12` 3·`13` 20·`14` 2·`15` 2·`16` 1·`17` 130·`18` 6·`19` 23·`20` 17·`21` 12·`22` 2·`23` 2·`24` 2·`25` 29（編號依單列之序）。

收工後施工樹 `git status --porcelain` 全空（量測器⛔ 留追蹤檔之變動）。

## 自捕與自解

1. 環境首驗缺 `shapely` ⇒ 依 README 第六節第 2 款裝之（`python3 -m pip`）後再驗 `rc 0`（停機款 `1″` ⛔ 成就）。
2. 單之 `8″` 以 `F23`…`F35` 書 `P0` 之號；各器出艙未印其 `F` 號（唯 `partrem` 之文中帶 `F28`），本回報以器名對之，其值與單列之序逐一同。⛔ 作他判。

## 平台事項（README 第六節）

- 主 checkout 之同步由 KL 自行為之（第 `6` 款）。
- `<O>` ＝ `/tmp/O`；路徑一律 Linux 正斜線絕對路徑。
- 執行報告⛔ 另立（`§二″` `(g)`）；⛔ 動生產碼、`verify/`、帳本、`CLAUDE.md`、`.claude/`。

## 耗時

接單 `01:03` → 回報推送 `01:13`（Asia/Taipei·`2026-10-22`）；約 `10` 分。
