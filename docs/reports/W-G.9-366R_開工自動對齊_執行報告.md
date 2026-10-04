# `W-G.9-366R`　開工自動對齊　執行報告 ⛔ 零生產碼

> 受單 ＝ CC（工作樹 `.claude/worktrees/wg9-366-lightweight-form-63e90b`·開場後 detached 於主線）·`2026-10-04`。
> 單 ＝ `docs/orders/W-G.9-366_輕量單.md`（`67373` B·`sha256` `6c5b4f5d70cde1f9526f70ed95fa302b957ca103eea781bc938d2c5090ee0c9d`·`SELF_SHA256` 自驗相符）。
> 級 ＝ 輕（⛔ 跑 `run_verification.py`／`run_all`）。
> 本檔載工項零〜二與開場；收工閘之實測值、工項四、五之出艙及停機款 `8`、`12` 之實，依單 `§三` 工項三於對話補報（⛔ 寫入本檔·自指）。

## ① 逐 `commit`

| 工項 | `commit` | 異動（`git diff --name-only` 前後） | 生產碼四檔命中 |
|---|---|---|---|
| 零 | `2ce8af27c04f38bf47a0cf8d444c63e8e3d95137` | `A docs/orders/W-G.9-366_輕量單.md` | `0`（空） |
| 一 | `04a8187fac236020386f4fbbea412de8c621969c` | `A verify/tools/wg9366_session_sync.py` | `0`（空） |
| 二 | `902cd11dfca5d3487931f818e8aabd4ac37a9c7f` | `M .claude/rules/常設規則索引.md`、`M CLAUDE.md` | `0`（空） |
| 三 | 本檔所在之 `commit`（自指·於對話報其 hash） | `A docs/reports/W-G.9-366R_開工自動對齊_執行報告.md` | — |

各 `commit` 之訊息首列 ＝ 單令逐字；其後依前批（`W-G.9-365` 四 `commit`）之體例附空列與 `Co-Authored-By` 列（見 ⑥ 自解 `1`）。各 `push` 皆 `git push origin HEAD:wip/s1-endpart`、快轉、首推即成（⛔ `--force`）。

## ② 停機款之三值

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `3c0c59c`；追蹤檔無變動；heads `35`；`§零-0` 項 `3` `rc 0`、四簿 ＝ `562`/`577`、`194`/`201`、`80`/`95`、`52`/`55` | `git rev-parse origin/wip/s1-endpart` ＝ `3c0c59c078e13e12a06df31576741f537c5dc8a6`；`git checkout --detach` 後 `status --porcelain --untracked-files=no` 列數 `0`；`ls-remote --heads` `35` 列；`probe_WG9321_issuer_anchor.py` `rc 0`，項4′ 正典框：自誤 `562`／`577`、GB `194`／`201`、VR `80`／`95`、K-9 `52`／`55` ⇒ 未成就 |
| `2` | `SELF_SHA256` 相符；bytes／`sha256` ＝ KL 之訊；來源檔存；入倉 blob 逐位 ＝ 來源 | 來源取自 KL 主 checkout 之根（施工樹之根無此檔）；`67373` B、`sha256` `6c5b4f5d…0c9d` ＝ KL 之訊；`SELF_SHA256` 載＝算 `b86104257c3b5457a344a31901d70903eb59f000ec1f99cdd83c92a76ce8cbf3`（受詞 `67295` B）；`git cat-file blob :docs/orders/W-G.9-366_輕量單.md \| cmp - <來源>` 無差 ⇒ 未成就 |
| `3` | 塊之 bytes／`sha256`／列數 ＝ `§五-1`；`git apply --check` 過；施後 blob ＝ 項 `8` | 見 ③；`--check` `rc 0`；施後三檔之 `git hash-object` 與 bytes 逐檔 ＝ `§五-1` 項 `8` ⇒ 未成就 |
| `4` | `CLAUDE.md` 刪除 `0`、改前為改後之嚴格前綴、尾 ＝ 塊 `P20`；索引 numstat `1`／`0` | `git diff --numstat`：`CLAUDE.md` `8`／`0`、索引 `1`／`0`；改後前 `336749` B 與 `3c0c59c:CLAUDE.md` `cmp` 無差；末 `2285` B 與塊 `P20` `cmp` 無差；`git apply --numstat` ＝ `1`／`0` ⇒ 未成就 |
| `5` | 工項一、二之驗 ＝ 期 | 見 ④ ⇒ 未成就 |
| `6` | 收工閘 ＝ 期 | 於對話補報（自指） |
| `7` | `push` 目標 ＝ `wip/s1-endpart`、未被拒、⛔ force | 三次皆 `HEAD -> wip/s1-endpart` 快轉（`3c0c59c..2ce8af2`、`2ce8af2..04a8187`、`04a8187..902cd11`）⇒ 未成就 |
| `8` | 工項四 | 於對話補報 |
| `9` | ⛔ 判正典、⛔ 改塊／器／命令 | 塊皆原樣抽出寫入；未判正典；塊之文字與倉之事實未見不符 ⇒ 未成就 |
| `10` | 新檔 ⛔ 為 `git check-ignore` 所命中 | 本單、`verify/tools/wg9366_session_sync.py` 之 `check-ignore -v` 皆 `rc 1`（無命中）；報告於收工閘 `2` 再驗 ⇒ 未成就 |
| `11` | KL 之訊逐字答問一「是」 | 見 ⑤ ⇒ 未成就 |
| `12` | 工項五 | 於對話補報 |

## ③ 塊之實得（抽取式 ＝ `§五-1` 末·圍欄開列次列至閉列前一列·`\n` 相接末附 `\n`）

| 塊 | 來源圍欄開列 | bytes | `sha256` | 列 | 首位元組 | 對 `§五-1` |
|---|---|---|---|---|---|---|
| `SS` | 本單 `:193` | `22256` | `f8167ea421d3500c67b0cae1c3a0ae703efefed1979bfa555198a1f2f768d980` | `422` | `#` | 相符 |
| `IX` | 本單 `:620` | `1974` | `75ff8ca5169538b3148ac7de4773f49f5e06a279e9b1150d9a2755b203cac8d8` | `12` | `d` | 相符 |
| `P20` | 本單 `:637` | `2285` | `0b05909d641e2e5d12fb4245394b76c8d4f022daa914e70103532d048cdf0a70` | `8` | `\n` | 相符 |
| `US` | 本單 `:650` | `4886` | `e5967bd4ffdd8ada58a580e136ca0bc4d75b24da8da914f0c107ea21adfe7b20` | `104` | `#` | 相符 |
| `CK` | `W-G.9-365` 單 `:807`（附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | `#` | 相符 |
| `GF` | `W-G.9-365` 單 `:755`（附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | `#` | 相符 |

`CLAUDE.md`：改前（`3c0c59c`）`336749` B → 改後 `339034` B（差 `2285` ＝ 塊 `P20`）。常設規則索引：`24624` B → `25053` B。新檔 `verify/tools/wg9366_session_sync.py` `22256` B。施後之 blob 三檔 ＝ `§五-1` 項 `8`（逐檔相符·值見單）。

## ④ 驗之出艙

### 工項一

`python verify\tools\wg9366_session_sync.py --selftest` ⇒ `rc 0`、`16` 列、stderr 空：

```
  ✅ T1 act=ff head=tip state=stale
  ✅ T2 act=current
  ✅ T3 act=notice
  ✅ T4 act=notice
  ✅ T5 act=skip
  ✅ T6 act=skip
  ✅ T7 act=skip
  ✅ T8 res=[True, True]
  ✅ T9 act=ff
  ✅ T10a act=current（⛔ fetch ⇒ 不知落後·對照）
  ✅ T10 act=ff head=D
  ✅ T11 act=current
  ✅ T12 act=notice/notice
  ✅ T13 resume=True startup(子目錄)=True compact=True clear=True compact′=True detached=True
  ✅ T14 act=error
⇒ 紅 []；rc 0
```

`--selftest-mutant` ⇒ `rc 1`；紅三列 `🔴 T3 act=error`、`🔴 T4 act=ff`、`🔴 T12 act=ff/ff`；末列 `⇒ 紅 ['T3', 'T4', 'T12']；rc 1`。

`--cwd <施工樹之反斜線絕對路徑>` ⇒ `（無訊息·skip）`；其後 `git rev-parse HEAD` ＝ `2ce8af27c04f38bf47a0cf8d444c63e8e3d95137`（工項零·未變）。

`git status --porcelain --untracked-files=all`（`add` 前）＝ 唯 `?? verify/tools/wg9366_session_sync.py`。

### 工項二

- `git apply --check <O>\IX.diff` ⇒ `rc 0`；`--numstat` ⇒ `1	0	.claude/rules/常設規則索引.md`。
- 必紅（塊 `P20` 未入前）：`checkidx` ⇒ `rc 1`；`L118 命中列數=0: '開工自動對齊'`；末列 `索引列數 124；內部字樣 121；外部指標 9；不合 1`。
- 必綠（塊 `P20` 入後）：`rc 0`；末列 `索引列數 124；內部字樣 121；外部指標 9；不合 0`。
- `gen_fa_index.py <repo> <O>\FX_regen.md` ⇒ `rc 0`、`則 124；加註節 14；列 158`；與 `.claude/skills/failure-archaeology-index/SKILL.md` `cmp` 無差。
- `git status --porcelain --untracked-files=all`（`add` 前）＝ 唯 `M` 二列（常設規則索引、`CLAUDE.md`）。

### 開場之餘

- `§零-1` 重跑 `wg9268_gate6_occupancy.py 3c0c59c W-G.9-366 W-G.9-365 W-G.9-396` ⇒ `rc 0`；母體 `966` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）；`W-G.9-366` 嚴格／寬式六數全 `0`、鬆框 `0`／`0`；`W-G.9-365` `2`／`12`／`6`·列框 `18`·鬆框 `2`／`34`；`W-G.9-396` 宣告框 `0`·鬆框 `18`／`28`；`W-G.9-963` 寬式 `D3` `2`（同單表之具名豁免）——與單 `§零-1` 之表逐格同。
- `§零-3` pre-flight：🔴 `0` 項；🟡 `10` 項（`P-1` `:62`／`:77`／`:100`／`:130`／`:202`／`:488`／`:641`／`:655`／`:672`、`P-4` `:317`）——與 `§五-1` 項 `10` 所列逐項同，依其具名豁免處置；ℹ️ `P-5` 相符、`P-3` `def main` ＝ `21232`–`28952`。

## ⑤ `§二` 之放行（KL 之逐字）

「請依 W-G.9-366_輕量單.md（67373 B·sha256 6c5b4f5d70cde1f9526f70ed95fa302b957ca103eea781bc938d2c5090ee0c9d）辦理。問一之答：是。」

## ⑥ 自捕與自解

**自捕**

1. 工項一首跑 `--selftest` 時，Bash 下未加引號之 `verify\\tools\\…` 被殼吃去反斜線 ⇒ `python` 報檔不存（`rc 2`，器未執行）。改以單引號傳 `verify\tools\wg9366_session_sync.py` 重跑，出艙見 ④。器與命令之文字皆未改。
2. 工項零之首次複製用 `cp --preserve=none`（GNU `cp` 不收此值）⇒ 複製未發生、隨後之 `add`／`cat-file` 皆失敗而無任何寫入；改以 `cp` 重做，blob 逐位驗見 ②-`2`。

**本批之自解清單**

1. `commit` 訊息：首列 ＝ 單令逐字，其後附空列與 `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`（與 `W-G.9-365` 四 `commit` 同體例）。零土地後果、零生產碼、可機驗（`git log -1 --format=%s` ＝ 單令逐字）、可逆（訊息之附列不涉任何檔）。
2. 塊 `CK`／`GF` 之抽取：`W-G.9-365` 單另含 `` ````json `` 圍欄，非本單抽取式所列之三種開列；本批以「開列之列號」（`:807`／`:755`）直接指名附錄午／巳之圍欄，抽取規則本身不變。可機驗：bytes／`sha256`／列數 ＝ `§五-1` 項 `6`（③）。零土地後果、零生產碼、倉外檔。

## ⑦ 各段耗時（本機時鐘）

| 段 | 起訖 |
|---|---|
| 開場（fetch、heads、detach、四簿、`SELF_SHA256`、取號、pre-flight） | `14:09:08`–約 `14:10:15` |
| 工項零（入倉·`commit` `14:10:27`·`push`） | 約 `14:10:15`–`14:10:30` |
| 工項一（寫檔、`--selftest` `14:10:56`–`14:11:09`〔`13` 秒〕、mutant、`--cwd`、`commit` `14:11:29`） | `14:10:49`–`14:11:30` |
| 工項二（`apply`、必紅、追加、必綠、重生成、`commit` `14:11:49`） | 約 `14:11:35`–`14:11:50` |

## ⑧ `<O>`

`C:\Users\admin\AppData\Local\Temp\wg9366_O`（任何 git 工作樹之外；`git -C <O> rev-parse --show-toplevel` ⇒ `fatal: not a git repository`）。內含 `heads_before.txt`（`35` 列）、抽出之塊、`checkidx.py`、`gen_fa_index.py`、`merge_user_settings.py`、`FX_regen.md` 與各驗之出艙。
