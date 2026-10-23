# `W-G.9-393_補令一` 回報（執行端·雲端）——**完成**

- 受單：`2026-10-23T21:10+08:00`（接單之 `commit` `db15465`·`ops/queue`）；回報：`2026-10-23T21:21+08:00`。耗時約 `11` 分（其中閘 `8″` 之 `31` 呼叫·耗時之和 `750` s·並行 `2`）。
- effort ＝ `high`（`$CLAUDE_CODE_EFFORT_LEVEL`）；單之建議等級 ＝ `medium`。

## 一、結果之要

| 項 | 值 |
|---|---|
| 工項零″ 之 `commit`（`<C>`） | `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`（首列逐字 `W-G.9-393 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼`） |
| 側支 `verify/W-G.9-393-endall` | `b40d838dd6f168e88ba02398807f5b9d8504f97d` → `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`（快轉） |
| 快轉前之記 | `ops/queue` `0e1d909`（`ops: 執行端快轉前之記 W-G.9-393_補令一`·先於快轉推成） |
| **主線 `wip/s1-endpart`** | **`cf1b41545dc0228a01102e1052d79b1184bff3fc` → `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7`**（快轉·`cf1b415..5d2a283`·⛔ `--force`） |
| 遠端 heads（濾後） | 前 `53`／後 `53`（未濾亦 `53`／`53`·本輪無出圖線之分支） |
| 主 checkout 之同步 | 省之（README 第六節第 6 款·由 KL 自行為之） |

## 二、`§零″` 開場

1. context 餘量充足（約 `14.9` M tokens）；`nproc` ＝ `4`。
2. `origin/wip/s1-endpart` ＝ `cf1b41545dc0228a01102e1052d79b1184bff3fc` ✅；`origin/verify/W-G.9-393-endall` ＝ `b40d838dd6f168e88ba02398807f5b9d8504f97d` ✅；heads 濾後 `53` ✅（全列存 `<O>/heads_before_393p1.txt`、未濾 `<O>/heads_all_before_393p1.txt`）；`checkout --detach` 後 `status --porcelain --untracked-files=no` 空 ✅；旗標 `[None, None, None, None, None]` ✅。
3. `probe_WG9321_issuer_anchor.py /tmp/w <O>/anchor_before.txt 637 636` ⇒ `rc 0`·`stderr` `0` B；項4′ 四簿：自誤 `622`／`637`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `77`／`80`／`[44, 47]` ✅（皆合期）。
4. bytes `22246`、`sha256` `b8943a42311e18e8ba997aaeaf2dfa4788150b0f3a4768c3f60c9d14dd55b634` ＝ `STATE.json` ✅；`SELF_SHA256`（`P-5` 原口徑·受詞 `22168` B）實算 `0b99ce6ded2f42446b4ecaed2b279f4f5dad2ac4392cce31d815e71157d6eb30` ＝ 單載 ✅。
5. 環境：初驗 `rc 1`（`No module named 'shapely'`）⇒ 依 README 第六節第 2 款 `python3 -m pip install -r requirements.txt --break-system-packages` ⇒ 再驗 `rc 0` ✅。Python `3.11.17`；`pip freeze` 之 `sha256` ＝ `6d88554e…`（≠ 發單端之 `ae1438da…`；本補令⛔ 沿用基準、⛔ 以 freeze 為閘，唯記之）。
6. pre-flight `probe_order_preflight.py` ⇒ `rc 0`·`stderr` `0` B：🔴 機械 `0` 項／🟡 提示 `0` 項／ℹ️ 記錄 `2` 項（`P-5` ✅ 相符·受詞 `22168` B；`P-3` `def main` 區間 `23812`–`31555`·本補令⛔ 用）＝ `§五″` 項 `3` ✅。施工樹之根之複本以 `.git/info/exclude`（`/W-G.9-393_補令一.md`）免於 `git status`。

## 三、工項

### 工項零″
- `docs/orders/W-G.9-393_補令一.md`（新檔·自來源二進位複製）；`git cat-file blob HEAD:…` 與來源 `cmp` 逐位同 ✅；`status --porcelain --untracked-files=no` 唯 `A` 此 `1` 檔 ✅；`git check-ignore -v --no-index` 無命中（`rc 1`）✅。
- `git push origin HEAD:verify/W-G.9-393-endall` ⇒ `b40d838..5d2a283`（快轉）✅。

### 工項一″ 前置（皆合期）
1. `origin/verify/W-G.9-393-endall` ＝ `<C>`；`origin/wip/s1-endpart` ＝ `cf1b415…` ✅。
2. `merge-base --is-ancestor` `rc 0`；`rev-list --count cf1b415..<C>` ＝ `6`；反向 `0`；`--merges` 空 ✅。
3. 逐筆 `git diff --name-only <c>^ <c> -- app.py ":(glob)verify/*.py"`：`5d2a283` `0`、`b40d838` `0`、`078fc27` `0`、`df2ba326d14a8d0c7ad9df7f72b03744a9b0643c` **`1`（`app.py`）**、`9f825b3` `0`、`0e4cc73` `0`（出艙存 `<O>/pre3_<c>.txt`）✅。
4. `<C>:app.py` ＝ `d91f6ee81f25eed01551e60774f26105c3186c45`；對 `df2ba32` 之 `app.py`／`:(glob)verify/*.py`／`verify/` 相異空 ✅。

### 快轉與出艙
- `git push origin 5d2a2836617bc2aea57f0c7513e67d9b2313f7f7:refs/heads/wip/s1-endpart` ⇒ `cf1b415..5d2a283`·`rc 0`（⛔ `--force`）。
- ① `ls-remote refs/heads/wip/s1-endpart` ＝ `5d2a2836617bc2aea57f0c7513e67d9b2313f7f7` ✅；② heads 濾後 `53` ✅；③ 生產碼 `34` 檔（`app.py` ＋ `verify/*.py` `33`）vs `df2ba32` 相異 `0`、vs `cf1b415` 相異 `1`（`app.py`）✅；④ `git branch -r --contains df2ba32` ＝ `origin/verify/W-G.9-393-endall`、`origin/wip/s1-endpart` ✅。

## 四、`§三-1″` 收工閘（於 `<C>`）

| 閘 | 實值 | 判 |
|---|---|---|
| `1″` | `117`／`0`·唯 `docs/orders/W-G.9-393_補令一.md`；首列逐字 | ✅ |
| `2″` | `diff --name-status b40d838 HEAD` 恰 `1` 列 `A␉docs/orders/W-G.9-393_補令一.md`；生產碼與 `verify/` 對 `b40d838` 相異 `0`；生產碼對 `cf1b415` `1`（`app.py`）；`verify/` 對 `cf1b415` `4`（`M` `probe_WG9352_endblock.py`、`probe_WG9389_trialstop.py`、`probe_WG9391_k980x.py`·`A` `probe_WG9393_endall.py`）；本補令 `check-ignore` 無命中（`rc 1`）；判別力 `verify/__pycache__/x.pyc` ⇒ `rc 0`·`.gitignore:18:__pycache__/` | ✅ |
| `3″` | 本補令 `CR` `0`；判別力 `data/V6.dxf` `12308` | ✅ |
| `4″` | 四簿（自誤簿、`GB` 簿、`docs/驗證裁定登記表.md`、`K-6` 典）、`CLAUDE.md`、`.claude/`、`docs/待落地清單.md`、`verify/baselines/` 對 `b40d838` 相異 `0`；blob：`CLAUDE.md` `00e627af…`、`K-6` 典 `e875bf61…`、自誤簿 `88a438f1…`、`GB` 簿 `f5b77fd5…`、待落地清單 `5d98124c…`（皆 ＝ 期） | ✅ |
| `5″` | heads 濾後 `53`；主線 ＝ 側支 ＝ `<C>`；其餘除 `ops/queue` 外之 `50` 列逐列 ＝ `<O>/heads_before_393p1.txt` | ✅ |
| `6″` | `probe_WG9270_closegate.py 637 636 .` ⇒ `rc 0`·末列 `✅ 二閘皆過`·`stderr` `0` B；判別力 `638 637 .` ⇒ `rc 7` | ✅ |
| `7″` | `probe_WG9321_issuer_anchor.py … 637 636` ⇒ `rc 0`·`stderr` `0` B；四簿之框 ＝ `§零″` 項 `3`（逐字 `cmp` 同） | ✅ |
| `8″` | `31` 呼叫皆 `rc 0`；末列皆逐字 `⇒ 紅 []；rc 0`；`stderr` 合計 `0` B；`P0`：`k953` `75／75`、`k965` `74／74`、`k948` `35／35`、`k966` `31／31`、`k961s3` `31／31`、`partrem` `29／29`、`trialstop` `16／16`、`k961r` `14／14`、`k980x` `22／22`、`k980g` `17／17`（皆 ＝ 期）；耗時之和 `750` s（最長 `trialstop wiring` `195` s、`k974 wiring` `188` s）；殼無 `WV_` | ✅ |

## 五、停機款之核

`1″`〜`9″` 皆未觸。本案配地：本補令零生產碼，主線之生產碼 ≡ `df2ba32`（原單已由發單端復驗 `F36 diff` 相異 `0`）——⛔ 變。

## 六、與 README 第六節之對照（平台事項）

- 直譯器 `python3`、路徑為正斜線之絕對路徑（`<repo>` ＝ `/tmp/w`、`<O>` ＝ `/tmp/O`）；並行 ≤ `2`；Git 連線不並發。
- 依賴依第六節第 2 款裝之（見 `§零″` 項 `5`）。

## 七、自捕與自解

1. **heredoc**：寫閘 `8″` 之呼叫清單（`<O>/g8/calls.txt`·倉外之暫存）時，一度於 Bash 命令中用 heredoc，違單首通則「Bash 命令⛔ 含 heredoc」。自解：刪該檔，改以檔案寫入工具重寫同內容後方跑閘 `8″`；該檔非量測之命令、非入倉之物，量測之殼與命令一字未改。
2. `pip freeze` 之 `sha256`（`6d88554e…`）與發單端之 `ae1438da…` 異：本補令⛔ 沿用基準、⛔ 以之為閘，閘 `8″` 皆合期；唯記之供發單端參考。
