# `W-G.9-384R`　入主線　執行報告（`W-G.9-384` 補令一）

> 單 ＝ `docs/orders/W-G.9-384_補令一.md`（所補 ＝ `docs/orders/W-G.9-384_規格單.md` 之 `§四-2`）。受單 ＝ CC（Windows 11·施工樹 ＝ 桌面版之 worktree `claude/wg9-384-spec-016888`〔`detach`〕）。`<O>` ＝ `C:\Users\admin\wg384O`（倉外）。
> 結果：主線 `wip/s1-endpart` 快轉 `fffa397` → `663a457`（`W-G.9-384`〔`K-9-71` 之落地〕入主線），其上工項零、一二筆零生產碼之 `commit`。側支 `verify/W-G.9-384-k971` ＝ `663a457`（保留·⛔ 動）。
> 收工閘之實測值與工項二（主 checkout 之同步）之出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 首列 | 推 |
|---|---|---|---|
| 零′ | 無 `commit`（遠端 ref 之改） | — | `git push origin 663a457bb111a27e694038b2cdd22cb5c1dc8807:refs/heads/wip/s1-endpart` ⇒ `fffa397..663a457`；`refs/heads/wip/s1-endpart` 之前值 `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c` → 後值 `663a457bb111a27e694038b2cdd22cb5c1dc8807`（首推即成·⛔ `--force`） |
| 零 | `dcfeb3714523e3601488ead5562ef9de90aec915` | `W-G.9-384 補令一 工項零：本補令原封入倉 ⛔ 零生產碼` | `git push origin HEAD:wip/s1-endpart` ⇒ `663a457..dcfeb37` |
| 一 | （本檔所在之 `commit`·自指 ⇒ 見對話） | `W-G.9-384 補令一 工項一：執行報告入倉 ⛔ 零生產碼` | `git push origin HEAD:wip/s1-endpart` |

各 `commit` 之訊息 ＝ 所令之首列逐字、空一列、`Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`（`git commit -F`）。

## ② 停機款 `1″`〜`9″`（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1″` | 主線 `fffa397`、側支 `663a457`、heads `44`、施工樹乾淨、四簿、旗標 | `git rev-parse origin/wip/s1-endpart` ＝ `fffa397b704bfd96bf8bbdcf6c91de3b1e51d16c`；`origin/verify/W-G.9-384-k971` ＝ `663a457bb111a27e694038b2cdd22cb5c1dc8807`；heads ＝ `44`（全列存 `<O>\heads_before_384p1.txt`）；`git checkout --detach origin/verify/W-G.9-384-k971` 後 `git status --porcelain --untracked-files=no` ＝ 空；`probe_WG9321_issuer_anchor.py … 620 619` ⇒ `rc 0`·自誤 `605`／`620`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `75`／`78`／`[44, 47]`；旗標 `[None, None, None, None, None]` ⇒ 未成就 |
| `2″` | `SELF_SHA256`、bytes／`sha256`、來源、入倉 blob | 來源 ＝ **第二處**（KL 主 checkout 之根·施工樹之根無之）；`22885` B·`sha256` `9c84b754bf33c2381392054b6fc89f64ce855d46495777e8f1576f8a3efa798b`·`146` 列·CR `0`；`SELF_SHA256`（`P-5` 原口徑·受詞 `22807` B）實算 ＝ 單載 ＝ `5b31c50d120c6b77a2bf4395cf115ac975698fcd3ef246e09f40fa196ea63ae8`；KL 之訊唯附本補令之檔、**未載 bytes／`sha256`** ⇒ 以 `SELF_SHA256` 為據（⛔ 停機）；入倉後 `git cat-file blob` 與來源 `cmp` 逐位同 ⇒ 未成就 |
| `3″` | 工項零′ 前置 | 全符（③） ⇒ 未成就 |
| `4″` | 快轉之推 | 首推即成（`fffa397..663a457`·未被權限分類器擋）·⛔ `--force` ⇒ 未成就 |
| `5″` | 快轉後之出艙 ①〜④ | 全符（③） ⇒ 未成就 |
| `6″` | 工項零、一之推之目標 | 皆 `wip/s1-endpart`；⛔ 推側支 ⇒ 未成就 |
| `7″` | 收工閘 | 於工項一之推後量之（出艙於對話） |
| `8″` | 工項二 | 於收工閘皆符之後辦之（出艙於對話） |
| `9″` | CC 之判、改器／命令、新檔之 `check-ignore` | 無；本補令：`git check-ignore -v --no-index` `rc 1`·無命中 ⇒ 未成就 |

**本批之自解清單**：無。

## ③ 工項零′ 之前置與快轉後之出艙

**前置**（`<O>\ff_pre_384p1.txt`·逐字）：

````text
## 1
is-ancestor rc=0
count fwd=5 rev=0
merges=[]
## 2
app.py
verify/selection_pipeline.py
261c5ac99f2b3b6e19152a689156378242d4c3a7
d197f222076529c700a770915248790e316ce259
2bb2f56ecf9423a99c522ddfbdfb55f314854e27
## 3
663a457bb111a27e694038b2cdd22cb5c1dc8807 []
d358f218ec3662f96106341ed9e037f840e729a1 []
8ce1a1828ee8b0a9991d05c91ef3b48c06fee401 [app.py verify/selection_pipeline.py ]
b47efbcb111633959d708bc1722eaabb83b0185d []
288a0d522611881ca0866c8c48d4318dccd4fcd2 []
````

（`## 1`：`git merge-base --is-ancestor fffa397… 663a457…` 之 `rc`、`git rev-list --count` 之正反二向、`git rev-list --merges` 之空；`## 2`：`git diff --name-only fffa397 663a457 -- app.py ":(glob)verify/*.py"` 恰 `2` 列與三 blob；`## 3`：逐筆 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`·`[]` ＝ 空輸出——命中者恰 `8ce1a18…`〔`§二` 之放行清單之 `commit`·`2` 列〕。皆 ＝ 期。）

**快轉**：

````text
To https://github.com/topology561/land-readjustment-trial.git
   fffa397..663a457  663a457bb111a27e694038b2cdd22cb5c1dc8807 -> wip/s1-endpart
````

**快轉後之出艙**（`<O>\ff_post_384p1.txt`·逐字）：

````text
① 663a457bb111a27e694038b2cdd22cb5c1dc8807	refs/heads/wip/s1-endpart
② heads=44
③ prod34=34 vs663a457=[] vsfffa397=[app.py verify/selection_pipeline.py ]
④   origin/verify/W-G.9-384-k971   origin/wip/s1-endpart 
````

（③ ＝ 生產碼 `34` 檔〔`app.py` ＋ `verify/` 頂層 `*.py`〕於新主線對 `663a457` 相異 `0`、對 `fffa397` 相異 `2`；④ ＝ `git branch -r --contains 8ce1a18…` 含 `origin/wip/s1-endpart`。皆 ＝ 期。）其後施工樹 `git fetch origin`；`git checkout --detach origin/wip/s1-endpart` ⇒ `HEAD` ＝ `663a457bb111a27e694038b2cdd22cb5c1dc8807`。

## ④ `§二` 之放行（KL 之逐字）

- 入主線之請示（發單側窗八十七·`2026-10-16`）之條件：「核對無誤的話，請回覆准入主線。我收到後再出補令，把主線快轉到這個版本，並同步你的主 checkout。」
- **KL 之語**（`2026-10-16 11:19`·`Asia/Taipei`·逐字）：「核對無誤」
- 發單側讀為工項零′（主線快轉）與工項二（主 checkout 之同步）之放行（`W-G.9-381` 之前例）；本補令由 KL 貼予 CC。逐筆放行清單：`8ce1a1828ee8b0a9991d05c91ef3b48c06fee401`（原單工項二·`app.py`、`verify/selection_pipeline.py`·本案配地⛔ 變）。

## ⑤ pre-flight

`python verify/probes/probe_order_preflight.py <本補令>`（施工樹 `663a457`）⇒ `rc 0`：

````text
── 🔴 機械·停機款：0 項 ──
── 🟡 提示·須逐項處置：2 項 ──
  [P-2] :43   🟡 框⛔ 無 `^` 錨而同段未依 `CLAUDE.md:725` 二數並報：1. **快轉之受詞**（發單側窗八十七·拋棄式 clone 實算）：…
  [P-4] :43   🟡 方向性轉引而同段⛔ 未具名座標系：1. **快轉之受詞**（發單側窗八十七·拋棄式 clone 實算）：…
── ℹ️ 記錄：2 項 ──
  [P-5] :146  SELF_SHA256 ✅ 相符（取檔內**最末**一個·受詞 22807 B）｜實算 5b31c50d120c6b77…／單載 5b31c50d120c6b77…
  [P-3] :-    `app.py` 之 `def main` 區間（AST 實查）＝ `22986`-`30706`
````

處置：`P-2` `:43`、`P-4` `:43` ＝ 本補令 `§五` 項 `3` 所載之二項，依其**具名豁免**（`P-2`：其計數皆 git 之物件之計數、非號之占用之框；`P-4`：其箭頭之座標系 ＝ 自開工態至快轉後·同段自載）。與發單側之實跑同（🔴 `0`／🟡 `2`／ℹ️ `2`）。

## ⑥ 自捕與自解

1. 來源檔取自第二處（KL 主 checkout 之根）·KL 之訊未載 bytes／`sha256` ⇒ 以 `SELF_SHA256` 為據（②）。
2. 本機之 `python`（`3.13.11`·`numpy 2.4.4`·`shapely 2.1.2`）與發單側（`3.13.16`／`2.4.6`／`2.2.0`）異——本補令之收工閘唯跑量測器之 `selftest`／`wiring`（照實載）。
3. 自解：無。

## ⑦ 各段耗時（本機時間 `+0800`·`2026-10-16`）

| 段 | 迄 | 約 |
|---|---|---|
| 開場（fetch、四簿、自驗、pre-flight·`heads_before_384p1.txt` 寫於 `11:25:45`） | `≈ 11:26` | `≈ 2` 分 |
| 工項零′（前置、快轉、快轉後之出艙·`ff_post_384p1.txt` 寫於 `11:26:44`） | `11:26:44` | `< 1` 分 |
| 工項零（入倉、`commit` `11:26:53`、推） | `≈ 11:27` | `< 1` 分 |
| 工項一（本報告） | — | — |
