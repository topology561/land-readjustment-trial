# `W-G.9-393R`　末端塊之認定之更正——執行報告（執行端·雲端）

> 受單 ＝ 執行端（雲端之排程「市地重劃·執行端」）·`2026-10-23`。單 ＝ `docs/orders/W-G.9-393_規格單.md`（`134050` B·`sha256` `23aee54d2f4ea9a3e2764499d43598c2b159d166c0b510b3b542bad12962de8f`·`SELF_SHA256` `36e01148f7fd31cae0d1f2389da79fde9c41ec95be1880147e63ac932910435d` 自驗相符）。
> 施工樹 ＝ `/tmp/w`（主倉之完整複本）；`<repo>` ＝ `/tmp/w`；`<O>` ＝ `/tmp/o393`（倉外·⛔ 在任何 git 工作樹之內）。前置 (甲)(乙) 於 `/tmp/pre`（`git worktree add --detach /tmp/pre 9f825b3`·倉外·工項一之端）照跑，`<repo>` ＝ `/tmp/pre`。
> 量測之殼：`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；`WV_*` 皆未設（出艙 `[None, None, None, None, None]`·環境之 `WV_` 變數 `0` 個）。並行 `2`。
> 收工閘之實測值 ⇒ `ops/queue` 之 `reports/W-G.9-393_規格單_回報.md`（⛔ 寫入本檔·自指）。

## ① 逐 `commit`

| 工項 | `commit` | 首列（逐字·單之所令） | 推送 |
|---|---|---|---|
| 零 | `0e4cc73` | `W-G.9-393 工項零：本單原封入倉（新側支）⛔ 零生產碼` | `refs/heads/verify/W-G.9-393-endall`（新立） |
| 一 | `9f825b34fcd0fbca0230a9ebc614b5deb695db86` | `W-G.9-393 工項一：量測器（F37 之新器·F11 之 S3 與 run 之 R1 之更·F33 之 X1 之增許·F35 之 run 之入口）（新側支）⛔ 零生產碼` | 快轉 |
| 二 | `df2ba326d14a8d0c7ad9df7f72b03744a9b0643c` | `W-G.9-393 工項二：無側面道路之端一律為末端塊（KL 07:39（二）·K-9-31）·二端之同時跨占 ⇒ GB-207 🔴 生產碼（新側支）` | 快轉（驗與審查皆符後） |
| 三 | `078fc27630723bcd7b27ad8ef397cf0d3ec6bd48` | `W-G.9-393 工項三：末端塊之認定之更正之讀法入典·自誤 637·GB-207 之立·待落地清單之更新（新側支）⛔ 零生產碼` | 快轉 |
| 四 | （本 `commit`） | `W-G.9-393 工項四：執行報告入倉（新側支）⛔ 零生產碼` | 快轉 |

各 `commit` 之訊息 ＝ 首列 ＋ 空列 ＋ 受單側之環境所附之尾列（`Co-Authored-By`、`Claude-Session`）·`git commit -F`。

## ② 停機款之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `cf1b415`、heads `52`、⛔ 含新側支、追蹤檔無變動、`§零-0` 項 `3` `rc 0` 與四簿之值、旗標 `[None×5]`、環境可匯入 | 主線 `cf1b41545dc0228a01102e1052d79b1184bff3fc`；heads `52`（`<O>/heads_before_393.txt`）；新側支之列 `0`；`git status --porcelain --untracked-files=no` 空；`probe_WG9321_issuer_anchor.py … 636 634` ⇒ `rc 0`·自誤 `621`／`636`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `198`／`206`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；旗標 `[None, None, None, None, None]`；匯入：初 `rc 1`（無 `shapely`）⇒ 依 README 第六節第 `2` 款裝之 ⇒ `rc 0` ⇒ **未成就** |
| `2` | `SELF_SHA256`、bytes／`sha256` 與 `STATE.json` 同、入倉之 blob 逐位同 | 三者皆同（`git cat-file blob HEAD:docs/orders/W-G.9-393_規格單.md` 與來源 `cmp` 同）⇒ 未成就 |
| `3` | 五塊之 bytes／`sha256`／列數 ＝ `§五-1`；`git apply --check` 過；寫出後之 blob ＝ `§五-1` 項 `5` | 皆同（見 ④）⇒ 未成就 |
| `4` | 前置 (甲)(乙)(丙)、前置 `4` 皆合期 | (甲) `14`／`14`、(乙) `6`／`6` 合期·`stderr` `0` B；(丙) 比對皆同 ⇒ 沿用；前置 `4` 三字樣皆 `rc 1`·無出艙 ⇒ 未成就 |
| `5` | 規格之歧義而涉域上判斷；須改 `§三-3` 之禁改 | 無 ⇒ 未成就 |
| `6` | `V-1`〜`V-9` 皆合期；本案之配地⛔ 變 | 皆合期（見 ③）⇒ 未成就（審查 (A-1) 之處置見 ⑥） |
| `7` | `push` 之目標唯新側支（與 `ops/queue`）；⛔ 被拒；主線⛔ 推進 | 四推皆至 `verify/W-G.9-393-endall`、皆快轉而⛔ 被拒；主線仍 `cf1b415` ⇒ 未成就 |
| `8` | 四檔之刪除欄 `0`、前綴、尾 ＝ 塊、blob；`checkidx`／`gen_fa_index` 合期 | 皆合（見 ④、⑨）⇒ 未成就 |
| `9` | 收工閘 | 見回報（⛔ 自指） |
| `10` | ⛔ 作正典之判、⛔ 改塊／器／命令 | 無 ⇒ 未成就 |
| `11` | 新檔⛔ 為 `git check-ignore -v --no-index` 所命中 | 本單、新器皆 `rc 1`·無出艙（報告二檔見回報之閘 `2`）⇒ 未成就 |
| `12` | 審查之發現涉域上判斷或規格之漏載 | 審查者標 (A-1)、(C-1)、(C-2) 為「涉域上判斷」——執行端對照單之文：(A-1) 為單 `§一` 項 `7` 與塊 `K40` 之三所已載之形（見 ⑥），(C-1)／(C-2) 為 `R-5` ② 之字面 ⇒ 未成就（其證據全載 ⑥·供發單端復驗） |
| `13` | 存取被拒、寫入為分類器所拒 | 無 ⇒ 未成就 |

## ③ 前置與驗之全部出艙

### 前置 (丙) 之版本之比對（`執行端.md` 丙 4之一）

- 主線之端 ＝ `cf1b41545dc0228a01102e1052d79b1184bff3fc` ＝ 基準之 sha ✅
- `python3 --version` ＝ `Python 3.11.17` ✅
- `python3 -m pip freeze` 之 `sha256`：依 `requirements.txt` 裝後 ＝ `eda6d909715479793ca24d442965516921e9240341656ed580a5b9e7d4d13869`（異於基準·其異 ＝ 單 `§零-0` 項 `5` 所載之七處：`certifi` `2026.10.19`、`pandas` `3.1.0`、`pillow`、`python-dateutil` `3.0.0`、`streamlit` `1.66.1`、`tzdata` `2026.5`、`websockets` `17.3`）⇒ 依該項釘回（`python3 -m pip install certifi==2026.10.18 pandas==3.0.6 pillow==12.3.0 python-dateutil==2.9.0.post0 streamlit==1.66.0 websockets==17.2 --break-system-packages`、`python3 -m pip uninstall -y tzdata --break-system-packages`·皆 `rc 0`·出艙 `<O>/pip_pin.txt`、`<O>/pip_uninstall_tzdata.txt`）⇒ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（`64` 列·`1114` B）＝ 基準 ✅
- ⇒ (丙) 之 `64` 呼叫**沿用** `ops/queue` 之 `基準/cf1b41545dc0228a01102e1052d79b1184bff3fc.md` 之值（⛔ 重跑）；下表之「工項一之端」欄標「沿用基準」者即之。

### 前置 `4`（`git grep -c -F "<字樣>" -- app.py`·工項一之端）

`GB-207` ⇒ 無出艙 `rc 1`；`K-9-60 ①` ⇒ 無出艙 `rc 1`；`W-G.9-393` ⇒ 無出艙 `rc 1`。

### `pre-flight`（`§零-3`）

`python3 verify/probes/probe_order_preflight.py <本單>` ⇒ `rc 0`：🔴 `0` 項；🟡 `3` 項——`P-2` `:1111`、`P-4` `:219`、`P-4` `:403`（＝ 單 `§五-1` 項 `9` 所具名豁免之三處·逐項同）；ℹ️ `P-5` 相符、`P-3` `def main` ＝ `23759`–`31502`。

### `84` 呼叫之表（`rc`／`stderr` B／末列·耗時 s）

`#56`／`#57` 之末列為 JSON 之摘要（⛔ 比·單之例）。前置之「照跑」＝ `/tmp/pre`（工項一之端 `9f825b3`）；施後 ＝ `/tmp/w`（工項二之 `commit` `df2ba32`·`push` 前·從頭整套照跑·⛔ 沿用）。逐呼叫皆 ＝ 單 `§五-1` 項 `8` 之同欄之期（以 `<O>/compare.py` 機械比對：前置 `20`／`20`、施後 `84`／`84`·不合 `[]`）；⛔ 有逾時或重跑之趟。

| # | 命令 | 工項一之端（前置） | 施後（工項二 `df2ba32`·驗） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·145） | `0`／`0`／`⇒ 紅 []；rc 0`（134） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·421） | `0`／`0`／`⇒ 紅 []；rc 0`（431） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／`⇒ 紅 []；rc 0`（31） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／`⇒ 紅 []；rc 0`（31） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·42） | `0`／`0`／`⇒ 紅 []；rc 0`（38） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·16） | `0`／`0`／`⇒ 紅 []；rc 0`（14） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·273） | `0`／`0`／`⇒ 紅 []；rc 0`（291） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·85） | `0`／`0`／`⇒ 紅 []；rc 0`（72） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·596） | `0`／`0`／`⇒ 紅 []；rc 0`（492） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·837） | `0`／`0`／`⇒ 紅 []；rc 0`（660） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（沿用基準·10） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（沿用基準·75） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（71） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·503） | `0`／`0`／`⇒ 紅 []；rc 0`（411） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2282） | `0`／`0`／`⇒ 紅 []；rc 0`（2122） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·37） | `0`／`0`／`⇒ 紅 []；rc 0`（38） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·6） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（沿用基準·25） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（21） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·25） | `0`／`0`／`⇒ 紅 []；rc 0`（23） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·295） | `0`／`0`／`⇒ 紅 []；rc 0`（313） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·438） | `0`／`0`／`⇒ 紅 []；rc 0`（348） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['S3 未臨正街 0 ⇒ 亦觸發（左端鉛直·R_end ＝ 末端帶·W-G.9-393）']；rc 1`（33） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（37） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（41） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（32） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·9） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·26） | `0`／`0`／`⇒ 紅 []；rc 0`（23） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·18） | `0`／`0`／`⇒ 紅 []；rc 0`（16） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·12） | `0`／`0`／`⇒ 紅 []；rc 0`（11） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·232） | `0`／`0`／`⇒ 紅 []；rc 0`（193） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·59） | `0`／`0`／`⇒ 紅 []；rc 0`（54） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·954） | `0`／`0`／`⇒ 紅 []；rc 0`（931） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·194） | `0`／`0`／`⇒ 紅 []；rc 0`（160） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·124） | `0`／`0`／`⇒ 紅 []；rc 0`（113） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·434） | `0`／`0`／`⇒ 紅 []；rc 0`（355） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／`selftest 9/9 ⇒ ✅`（沿用基準·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／`selftest 13/13 ⇒ ✅`（沿用基準·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／`ε ＝ 0.0002｜rc 0`（沿用基準·2） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（2） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／`紅項 [] 器紅 0`（沿用基準·10） | `0`／`0`／`紅項 [] 器紅 0`（10） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·440） | `0`／`0`／`⇒ 紅 []；rc 0`（347） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（197） 照跑 | `0`／`0`／`（JSON 之摘要列·略）`（215） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（150） 照跑 | `0`／`0`／`（JSON 之摘要列·略）`（153） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（197） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（214） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（162） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（153） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（414） 照跑 | `0`／`0`／`⇒ rc 0（不符 0 項）`（444） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（298） 照跑 | `0`／`0`／`⇒ rc 0（不符 0 項）`（314） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·5） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·432） | `0`／`0`／`⇒ 紅 []；rc 0`（347） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·1589） | `0`／`0`／`⇒ 紅 []；rc 0`（1519） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·1558） | `0`／`0`／`⇒ 紅 []；rc 0`（1249） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（2） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（127） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（143） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（479） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（464） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·428） | `0`／`0`／`⇒ 紅 []；rc 0`（362） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（3） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／`⇒ 紅 []；rc 0`（37） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（693） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（712） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·8） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·5） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（沿用基準·428） | `0`／`0`／`⇒ 紅 []；rc 0`（361） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['T1', 'T2', 'T3a', 'T3b', 'T6', 'T7', 'T8', 'T9', 'T9b', 'T12', 'T12b', 'T10', 'T10b', 'T11']；rc 1`（2） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4', 'W5', 'W9']；rc 1`（4） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | `1`／`0`／`⇒ 紅 ['R1@3.5', 'R2@3.5', 'R3@3.5', 'R1@0.0', 'R2@0.0', 'R3@0.0']；rc 1`（435） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（348） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | `1`／`0`／`⇒ 紅 ['R1@3.5:R2right', 'R1@3.5:R3left', 'R1@3.5:R5right', 'R1@0.0:R2right', 'R1@0.0:R3left', 'R1@0.0:R5right']；rc 1`（441） 照跑 | `0`／`0`／`⇒ 紅 []；rc 0`（347） |

前置之照跑 `20` 呼叫：耗時之和 `3777` s；施後 `84` 呼叫：耗時之和 `15293` s（並行 `2`）；`stderr` 合計：前置 `0` B、施後 `0` B。

### `V-1`〜`V-9`

| # | 期 | 實 |
|---|---|---|
| `V-1` | `14` 呼叫皆 `rc 0`、末列 ＝ 施後之列 | 皆合（全文見附錄）；`F37 selftest` `T1`〜`T12c` ✅、`F37 wiring` `W1`〜`W9` ✅、`F37 run` `R1`〜`R4`（二退縮）✅、`9352 run` `R1`〜`R5`（二退縮·四端）✅ |
| `V-2` | 其餘 `64` 呼叫皆 `rc 0`、末列 ＝ 施後之列；`F23 selftest` 之 `P0 逐項擾動恰該項紅 75／75` | 皆合；`#4`（`probe_WG9363_k953.py selftest`）之出艙含 `  ✅ P0 逐項擾動恰該項紅 75／75` |
| `V-3` | `4` 器之 blob ＝ `§五-1` 項 `5` | `263ddaaf…`、`ac92e2d8…`、`278d85a2…`、`82cafc8f…` ✅ |
| `V-4` | `F36 diff`、`cmp` | 下節 ✅ |
| `V-5` | `parity` `rc 0`·代 `HEAD` 後逐位同 | 下節 ✅ |
| `V-6` | `F8` 之落檔前後同 | 下節 ✅ |
| `V-7` | 生產碼相異恰 `app.py`；`verify/` 相異 `0`；頂層之名與相異之節點 | `git diff --name-only 9f825b3 df2ba32` ＝ `app.py` 唯一；`--numstat` ＝ `73`／`20`；`verify/` 相異 `0`；`app.py` 之施後 blob ＝ `d91f6ee81f25eed01551e60774f26105c3186c45`（`1879692` B）；頂層之名之增減 `[]`／`[]`、相異之節點 ＝ `['_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_side_geom']`（`F37 wiring` `W5`·審查者以 AST 另驗：`417` 節點中相異恰此五） |
| `V-8` | 三字樣皆 ≥ `1` | `git grep -c -F`：`GB-207` ⇒ `app.py:4`；`K-9-60 ①` ⇒ `app.py:5`；`W-G.9-393` ⇒ `app.py:15` |
| `V-9` | `V-1`〜`V-6` 之 `stderr` 合計 `0` B | `0` B（`84` 呼叫與 `V-4` 之四呼叫） |

### `V-4` 之全文

```
$ python3 verify/probes/probe_WG9392_k980g.py diff <O>/k6s3_pre_35.json <O>/k6s3_post_35.json   ⇒ rc 0·stderr 0 B
全比相異 0 項
$ python3 verify/probes/probe_WG9392_k980g.py diff <O>/k6s3_pre_00.json <O>/k6s3_post_00.json   ⇒ rc 0·stderr 0 B
全比相異 0 項
$ python3 verify/probes/probe_WG9344_k6s3.py cmp <O>/k6s3_pre_35.json <O>/k6s3_post_35.json      ⇒ rc 0·stderr 0 B
相異 0 項 ⇒ ✅ 同
$ python3 verify/probes/probe_WG9344_k6s3.py cmp <O>/k6s3_pre_00.json <O>/k6s3_post_00.json      ⇒ rc 0·stderr 0 B
相異 0 項 ⇒ ✅ 同
```

### `V-5` 之比（以 `<HEAD>` 代二態之 `HEAD` 之全值後逐位比·`<O>/v5.py`）

```
parity35_pre.json vs parity35_post.json: 代後逐位同 True（代之次數 1/1·sha256 25810ad8b1fb8866／25810ad8b1fb8866）；對照 ⛔ 代之 ⇒ 同 False
parity00_pre.json vs parity00_post.json: 代後逐位同 True（代之次數 1/1·sha256 58a3d9e85d265d15／58a3d9e85d265d15）；對照 ⛔ 代之 ⇒ 同 False
pre/60_pre.out vs post/60_post.out: 代後逐位同 True（代之次數 1/1·sha256 73ba729fc44a775e／73ba729fc44a775e）；對照 ⛔ 代之 ⇒ 同 False
pre/61_pre.out vs post/61_post.out: 代後逐位同 True（代之次數 1/1·sha256 b2f8709d925ec913／b2f8709d925ec913）；對照 ⛔ 代之 ⇒ 同 False
```

二態之 `parity` 之末列皆 `⇒ rc 0（不符 0 項）`。

### `V-6` 之比

`git hash-object`：`f8_pre_35.json` ＝ `f8_post_35.json` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`；`f8_pre_00.json` ＝ `f8_post_00.json` ＝ `884e91714a79288406faa4def6518847de36de39`（README 第六節第 `5` 款之值）；`run` 之末列皆 `⇒ 紅 []；rc 0`。

## ④ 塊之實得與四檔

| 塊 | bytes | `sha256` | 列 | 圍欄（標題／開／閉之列） |
|---|---|---|---|---|
| `Fy49` | `36873` | `536faf9226865d7a2609c36519c727ee100cfc765556a64be04e11d4ef766810` | `632` | `352`／`354`／`987` |
| `K40` | `11272` | `e711c2f464af160050fcc06431d2f72b531671aa7ab24c94700c7af4ea8cef33` | `65` | `989`／`991`／`1057` |
| `P51` | `4901` | `e2b4ca6c42c5ff7a6db762712d4022552e650a91bb3ecb1aa13c25fd3f0a74a2` | `23` | `1059`／`1061`／`1085` |
| `E39` | `2854` | `8b50fd5b3c93da5d88c33ca470a4339ef81c54e3b6ef6e1fd9c9012d4e42cce5` | `13` | `1087`／`1089`／`1103` |
| `G17` | `2030` | `fd98cef288c23ee6e8040a4bc7cf0a3a8641d2483af99c0129d9c72baa8e3d7d` | `12` | `1105`／`1107`／`1120` |
| `CK`（`W-G.9-365` 附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` | `805`／`807`／`839` |
| `GF`（`W-G.9-365` 附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` | `753`／`755`／`803` |

工項一：施前 blob `207e73ff…`、`42f6cdb0…`、`d99f637c…`（`probe_WG9393_endall.py` 施前⛔ 存）＝ `§五-1` 項 `2`；`git apply --check` 過；施後 blob `263ddaafac22a573216f4a1df579bec6fa97da0f`（`35266`）、`ac92e2d814fc50198dbe02fbaefbf1a2030b1961`（`36331`）、`278d85a2550505acf01327983553992496f57eb1`（`33837`）、`82cafc8f1a7ef9b944c026c0285cc2650a6a3d9d`（`28191`）；`git status --porcelain` 唯此 `4` 檔；增刪 `9`／`8`、`8`／`2`、`5`／`3`、`532`／`0`。

工項三（四檔·皆純末端追加·刪除欄 `0`·改前為改後之嚴格前綴·其尾 ＝ 塊·`CR` `0`）：

| 檔 | 改前 B | 改後 B | 施後 blob | 增／刪 |
|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `938251` | `949523` | `e875bf61786023642b196567c1fade2803b11932` | `65`／`0` |
| `docs/待落地清單.md` | `28734` | `33635` | `5d98124c70c59abd4bca3cae0af735636552826e` | `23`／`0` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1230576` | `1233430` | `88a438f1f0bdb3c33a116dfcac7af1bcbd4eadfb` | `13`／`0` |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `1065227` | `1067257` | `f5b77fd507b30f9e40708629896d0c3c83389341` | `12`／`0` |

## ⑤ 推送

- 工項零 ⇒ `* [new branch] HEAD -> verify/W-G.9-393-endall`；推後 `git ls-remote --heads origin` ＝ `53` 列；主線 `cf1b41545dc0228a01102e1052d79b1184bff3fc`。
- 工項一 ⇒ `0e4cc73..9f825b3`；工項二 ⇒ `9f825b3..df2ba32`（推後 `ls-remote`：新側支 `df2ba326…`、主線 `cf1b4154…`）；工項三 ⇒ `df2ba32..078fc27`；工項四 ⇒ 見回報。
- 推後之 `git ls-remote --heads origin` 之全列與 `heads_before_393.txt` 之逐列比 ⇒ 回報（收工閘 `5`）。
- 主 checkout 之同步由 KL 自行為之（README 第六節第 `6` 款）。

## ⑥ 自捕與自解；唯讀獨立審查

### 自捕與自解

1. **heredoc**：單首 🔑 令「Bash 命令⛔ 含 heredoc」；執行端於讀畢全單之前（接單之段·`ops/queue` 之 `STATE.json` 之更、本單之 `SELF_SHA256` 之自驗）用 heredoc 二次（皆唯讀或 `ops/queue` 之 `STATE.json`·⛔ 涉主倉）。其後一律以檔案（`<O>/*.py`、`<O>/msg*.txt`）為之。
2. **依賴**：雲端之殼初無 `shapely` ⇒ 依 README 第六節第 `2` 款裝 `requirements.txt`，其版異於基準七處 ⇒ 依單 `§零-0` 項 `5` 釘回 ⇒ `pip freeze` 之 `sha256` ＝ 基準。
3. **呼叫之表之抽取**：`<O>/runner.py` 以正規式抽單之「項 `8` 之表」之命令，其式亦命中 `§四-3` 之閘 `6`／`7` 之列（號 `6`、`7`），然其後之「項 `8` 之表」之 `#6`／`#7` 覆之（dict 之後寫者勝）——已以 `#6` 之出艙（`probe_WG9367_adj4.py wiring`·`⇒ 紅 []；rc 0`）證其所跑 ＝ 項 `8` 之 `#6`。
4. **撰碼中之自跑**（單首 🔑 所許·⛔ 改器）：工項二之 `commit` 前於 `/tmp/w` 跑 `#81`、`#82`、`#34`、`#35`、`#5`、`#6`、`#69`、`#70`、`#75`、`#76` ⇒ 皆 ＝ 施後之列（`<O>/chk/`）。
5. **折行之字樣**（`§三-3` 第 `1` 款）：新增之 docstring 之折行原有以「四空白 ＋ 全形之『（』」與「四空白 ＋ 中文」起首者二列 ⇒ 撰碼中即改其折行使以反引號起首；`git diff` 之新增列以 `^\+ {4,}[\p{Han}（「]` 掃之 ⇒ `0`。

### 唯讀獨立審查（一輪·`redistribution-reviewer`·⛔ 改檔、⛔ `commit`·其暫存在 `/tmp/rv393/`·審查者以 `find -newer` 自證⛔ 動 `/tmp/w`）

審查者之結論：`R-1`〜`R-6` 皆落地；`§三-3` 六款皆過（`verify/probes` 之字串常數 `27078` 個中，改前恰一見者改後仍恰一，破者 `0`；F11 之 M6 之錨於 `end_block_apply` 內與全檔皆 `1`；`main` 之 AST 同；頂層之名⛔ 增減、相異恰五；案件字面 `0`；簽名同）；`GB-207` 於試算之內確上拋（`end_block_merge_run` 之試算內拋之 ⇒ 外層上拋「[試算內之程式之停機·末端塊合併再試·試算] 🔴 [GB-207…」；對照：一般之 `RuntimeError` 則被吞為 `'試算中止': 'plain stop'`；`K6_PROGRAM_STOPS` 恰增 `1`、末項 ＝ 訊息全文）；(B) 純實作之瑕：**無**。

逐條之發現與處置：

- **(A-1)（審查者標「涉域上判斷」）本案 `R2` 之宗地之頂點之微變**：審查者自寫之驅動（`run_corner_pk_k6b` ＋ `run_step_g`·全 `g_rows` 之全欄含 `cut_coords`·二退縮）見三列相異：`628-34(1)`（`cut_coords` 頂點 `6`→`5`、`迭代次數` `26`→`30`）、`628-32(2)`（`cut_coords`）、`R2-抵費地`（`cut_coords`）；對稱差 `1.36e-4`、`1.47e-4`、`9.7e-5 ㎡`；`G(㎡)` 與一切取 2 位之欄、當選者、宗序皆同；`R2` 之未覆蓋面積 `3.0e-5` → `1.02e-4 ㎡`（街廓 `4368.603347 ㎡`·遠小於守恆之 `1 ㎡`）。其由：`R2` 右之未臨正街 `0.0001 ㎡`（≤ ε·s 寬 `3.3e-6 m`）；改後 `_eb_info['right']` 非 `None` ⇒ `app.py` 之右鏈之起點之支（`:22248`；`verify/stepg_pipeline.py:988`）以 FRONT `p2` 為起點；`s_back` ＝ `0` ⇒ 該 ≤ ε 之碎片無宗地承之（左端 `R3` 改前改後皆如此·`1.37e-4 ㎡`）。
  **處置**：單之文已載此形——`§一` 項 `7`「右鏈之起點之取法使宗地之頂點有微米之級之差（面積⛔ 變）」、塊 `K40` 之三「右端為末端塊者（`R2` 右、`R5` 右），其右鏈之起點之取法依末端塊之既有之碼（唯審查所見·`app.py` 之右鏈之起點之支），宗地之頂點或有微米之級之差（發單端前之原型之實量：`R2` 之三宗 ≤ `3.3e-6 m`）——應分配面積與宗地之面積取至 2 位⛔ 變」與 `R-1`（ε 以下之碎片⛔ 計·`s_back` ＝ `0`）；審查者之量（`R2` 之三列·s 寬 `3.3e-6 m`）與之相合，且「本案之配地⛔ 變」之驗（`V-4`〜`V-6`）皆合 ⇒ 執行端判其為**單所已載之形、非新發現**，⛔ 停機；⛔ 作「孰為正典」之判——其量全載於此，供發單端復驗時核之（若發單端認其超出單之所載，則依 README 第二節停止條件 `3`／`4` 處之）。
- **(C-1)（審查者標「涉域上判斷」）`GB-207` 先於 `K-9-80` ⑥**：二端之末端帶相疊之短街廓（審查者之例：`6 × 20`·二宗），`GB-207` 於評選之前即停機而 `k980_range_touch_check` ⛔ 及之；二者皆停機（⛔ 靜默）。**處置**：`R-5` ② 之字面（「二端之評選之前……⇒ raise」）與塊 `K40` 之二之庚（「本單於二端之評選之前查之」）⇒ 照單；記之。
- **(C-2)（審查者標「涉域上判斷」）`GB-207` 之觸發面**：凡與二端之 `R_end` 之交皆 ＞ `1 ㎡` 之宗皆觸發（不限其為候選者·例 `15 m` 之街廓三宗寬 `3`／`9`／`3`，中宗與二端各交 `10 ㎡` ⇒ 停機）。**處置**：`R-5` ② 之字面（「`ordered` 之任一宗」）⇒ 照單；記之。
- **(C-3) 舊之紀錄之殘**：同一 session 中殘留 `{'觸發': False}` 之紀錄 ⇒ `end_block_apply` 停機「首趟未觸發而本趟觸發」（實測）；二宿主皆於首趟先清（`app.py:21438`、`run_step_g`）⇒ ＝ 塊 `K40` 之四 `80` 所載；記之。
- **(C-4) 已不可達之支與過時之註**（`R-1`〜`R-6` 以外一字⛔ 動 ⇒ ⛔ 改）：`end_block_eval_rows` 之「未觸發」之支（＝ 塊 `K40` 之己前之審查所記）；`_place_pool_parcels` 之註「無末端 gate 之側 `_reserve` 為 None」（`app.py:11188`）；`_end_band` 之 docstring 之「需 `area(R_end)`＝含碎片」。
- **(C-5) `p1` 不在街廓上之無側街之端**（`s_min` ＞ `0`）：改前 gate 偽，改後為末端塊、其末端帶為街廓所裁窄；本案無此形（`R2`、`R5` 左之 `s_min` ≈ `0.27` 而二端皆有側街）——記之（候發單端定其是否入待落地）。
- **(C-6) 例外之先後之微變**：二端之幾何改於評選之前取 ⇒ 二端皆將出錯者，改後先拋右端之幾何之錯（改前先拋左端之評選之錯）；二源不一致者之先後照舊（審查者實測）。記之。
- 審查者之合成之例（⛔ 用 `F37` 之例）：例一 `40 × 20`，左端無側街·無三角地，`A`（`G` `30`）、`B`（`150`）、`C` ⇒ 改前序 `A,B,C`（未觸發）；改後 `A` 未達、`B` 當選 ⇒ `B,A,C`（`R_end` `70`·`s_back` `0`）；第一宗即達者二態皆 `A,B,C`；有三角地者（`R_end` `120`·`s_back` `5`）二態逐項同。例二 `15 × 20` 二端皆無側街：一宗跨全長 ⇒ `GB-207`（左 `70.00`、右 `70.00 ㎡`）、`K6_PROGRAM_STOPS` 增 `1` 且末項 ＝ 訊息；二宗各 `7.5` ⇒ 過（二端各當選）；交 `70`／`1.20` ⇒ 停機。

## ⑦ 設計說明（`§三-5`）

### 逐條

- **`R-1`（`end_block_side_geom`）**：`if _w <= 0.0:` 之體由 `return {'gate': False, 'unfront': 0.0}` 改為 `_unf_poly, _unf = None, 0.0`；其 `else` 照舊取 `_block_strip`；`if _unf <= END_BLOCK_UNFRONT_EPS:` 之體由 `return {'gate': False, 'unfront': _unf}` 改為 `_unf_poly, _w = None, 0.0`；其後照舊呼 `_end_region_R(…, _unf_poly, …)`（`None` ⇒ `R_end` ＝ 末端帶·有最小建築面積之輸入者經 `end_block_band_width` 擴之）、`buf` 照舊、回傳之鍵照舊（`s_back` ＝ `float(_w)` ＝ `0.0`）。docstring 增三列（`W-G.9-393`·`gate` 恆真之義）。
- **`R-2`（`_end_region_R`）**：「`frag_poly` 空 ⇒ 停機」去之，代以 `_nofrag393 = frag_poly is None or getattr(frag_poly, 'is_empty', True)`；`_nofrag393` ⇒ `r_end = band`，否則照舊之 `unary_union`。docstring 增二列。
- **`R-3`（`end_block_band_width`）**：「`frag_poly` 空 ⇒ 停機」去之，代以同式之 `_nofrag393`；`_area_at391` 於 `_nofrag393` ⇒ `float(_b391.area)`（與 `R-2` 之 `R_end` ＝ 末端帶同一面積之源），否則照舊。docstring 增一條。
- **`R-4`（`_place_pool_parcels`·P2-f）**：`if _unfront <= 1e-3: continue` 去之，代以 `_frag393 = _unf_strip391[0]`；`if _unfront <= END_BLOCK_UNFRONT_EPS: _frag393 = None`；`_end_region_R` 之未臨正街之引數由 `_unf_strip391[0]` 改為 `_frag393`。缺 `alloc_dir_cad`／`min_width` 之停機照舊（其訊息末追加「（`W-G.9-393`：無 SIDELINE 之側一律末端塊·無三角地者亦及之）」）；`_reserve` 之算、診斷之字串照舊。
- **`R-5`（`end_block_apply`）**：① 於主迴圈之前另一迴圈 `for _sd393 in ('left', 'right')`：二源不一致之端 ⇒ `break`（主迴圈照舊停機·⛔ 先算其後之端·保改前之例外之先後）；無側街之端 ⇒ `_geo393[_sd393] = end_block_side_geom(…)`（每端一次）；主迴圈之 `_g = _geo393[_sd]`（⛔ 再呼）。② `'left' in _geo393 and 'right' in _geo393` ⇒ 逐 `_out`（＝ `list(ordered)`）之宗，取 `polygon_coords`（不足三點略之、無效者 `buffer(0)`·同 `end_block_pick`），其與左、右 `R_end` 之交皆 ＞ `END_BLOCK_CROSS_MIN_AREA` ⇒ `raise k6_program_stop(f"🔴 [GB-207·K-9-60 ①] 街廓 {blk_label}：二端皆無側街（皆為末端塊）而重劃前土地 {暫編地號} 同時跨占左、右二端之末端塊範圍（左 {:.2f} ㎡、右 {:.2f} ㎡）——其處置（K-9-60 ①）未落地 ⇒ 停機（`W-G.9-393`·⛔ 靜默歸一端、⛔ 二端皆當選）")`。③ `if not _g['gate']: … continue` 之支去之。其餘（二源不一致之停機、首趟評選與沿用〔F11 M6 之錨⛔ 動〕、強制抵費地、紀錄與回傳之形）照舊。docstring 增三列。
- **`R-6`**：`_place_pool_parcels` 之「與 wf_f4 `_reshape_block` **同式**」之註之後追加四列（條件2 去之·自此與 wf_f4 ⛔ 同式）；其缺輸入之停機之訊息追加一句；`END_BLOCK_UNFRONT_EPS` 之前之觸發之註（條件 ②）之後追加三列——皆⛔ 刪既有之句。新增之區域名：`_frag393`、`_nofrag393`、`_geo393`、`_sd393`、`_pk393`、`_P393`、`_e393`、`_tp393`、`_cs393`、`_pg393`、`_ovl393`、`_ovr393`（皆帶 `393`·改前全檔皆 `0` 見·審查者驗）。

### 一切呼叫處（`app.py` 與 `verify/` 頂層之 `*.py`·工項二之 `commit`）

- `end_block_side_geom`：`app.py` `end_block_apply` 內一處（`_geo393[_sd393] = end_block_side_geom(…)`）；`verify/` 頂層⛔ 呼（量測器 `verify/probes/` 另呼之）。
- `_end_region_R`：`app.py` `_place_pool_parcels`（P2-f·`_frag393`）、`end_block_side_geom`（`_unf_poly`）；`app.py` 之 `_WF_NS_NAMES` 之列（`"_strip_axis", "_end_region_R",`）；`verify/wf_f4.py:1404`、`:1422`（`_reshape_block`·其閘 `_end_gate = _cond1 and (_unfront_area > 1e-3)` 為真方呼·傳其實之碎片 ⇒ 行為⛔ 變·單 `§二` 之⛔ 及）；`verify/fixture_end_fallback.py:82`、`verify/fixture_end_winner.py:155`／`160`／`195`（夾具·傳實之碎片或替身）。
- `end_block_band_width`：`app.py` `_end_region_R` 內一處（有最小建築面積之輸入者）。
- `end_block_apply`：`app.py` `end_block_host` 內一處（二宿主：`app.py` 之畫面之 `end_block_host(` 呼叫處與 `verify/stepg_pipeline.py:668` 之 `ns["end_block_host"](`）。

### 未臨正街之多邊形為 `None` 之下游之讀之窮查

- `s_back`：`end_block_apply` 傳 `trial(tp, side, s_back)` ⇒ `end_block_host._trial` ⇒ `end_block_trial_G(…, s_back)` ⇒ `solve_one(…, _s_back=s_back)` ⇒ `solve_G_binary`：`s_back == 0` ⇒「原式一字未動」之路徑（`app.py` `solve_G_binary` 之 `W-G.9-352` 之註）；`_eb_info[側]['s_back']` 於二宿主之鏈首（`app.py` 之 `_s_back=(float(_eb_info['left']['s_back']) …`、右同；`verify/stepg_pipeline.py:912` 等）與取得之宗之自我檢查（`end_block_trial_G(…, float(_eb_info[側]['s_back']))`）同值 `0.0`。
- `buf`：由 `R_end`（＝ 末端帶）之 s 域導（左 ＝ 其 s 上界；右 ＝ s(p2) − 其 s 下界）·唯強制抵費地（`end_block_forced_buf`）讀之。
- `未臨正街(㎡)`、`末端帶(㎡)`、`R_end(㎡)`：唯紀錄（`SS_END_BLOCK_EVAL`）與顯示（`end_block_eval_rows`：觸發之支 ⇒「未臨正街 0.0 ＋ 末端帶 … ＝ R_end …」）讀之。
- `r_end`：`_eb_info[側]['r_end']` ⇒ 二宿主之 `k980_range_touch_check`（`'左端末端塊範圍'`／`'右端末端塊範圍'`）與強制抵費地之帶（`end_block_forced_bands`）。
- `_eb_info[側] is not None` 之讀者（審查者之窮查·皆隨「一律為末端塊」而生效）：`app.py` `21842`、`22044`、`22161`、`22196`、`22248`、`22303`、`22323`、`22359`、`22400`、`22482`〜`22505`、`22538`、`22634`；`verify/stepg_pipeline.py` `682`、`857`、`912`、`942`、`988`、`1040`、`1059`、`1091`、`1133`、`1189`〜`1212`、`1252`、`1341`——其中右鏈之起點（`22248`／`988`）與池之 s 之上界（`22538`／`1252`）即 ⑥ (A-1) 之源（單 `§一` 項 `7`、塊 `K40` 之三所載）。
- ⇒ 與「無三角地之讀」⛔ 合者：⛔ 見（`§三-4` 之末款⛔ 成就）。

### `§三-3` 各款之自查

1. 字樣之錨：`#5`（`F23 wiring`）、`#6`（`F24 wiring`）施後皆 `⇒ 紅 []；rc 0`；新增列之「四空白 ＋ 中文」起首 `0`（⑥ 自捕 5）；審查者全量掃之破者 `0`。
2. 突變之錨：`#34`（`F11 selftest`）`⇒ 紅 []；rc 0`（其七突變之錨皆恰一·M6 之錨未動）；他器之突變（`#19`、`#22`、`#43`、`#47` 等）皆 ＝ 施後之列。
3. `main`：⛔ 動（`#2`〔`F30 wiring`·`probe_WG9385_k974.py wiring <repo> 158f7fe`〕之 `W7` ⇒ 施後 `⇒ 紅 []；rc 0`；審查者另以 AST 驗之同）。
4. 頂層：增減 `0`、相異之節點恰五（`F37 wiring` `W5`）；`verify/` 頂層 `*.py` 相異 `0`（`W7`）。
5. 案件字面：`F37 wiring` `W6` `[]`。
6. 簽名、回傳之形：五函式之簽名⛔ 變（審查者驗）；`end_block_side_geom` 之回傳之鍵 ＝ `gate`、`unfront`、`s_back`、`r_end`、`r_end_area`、`band_area`、`buf`（⛔ 增減）。

## ⑧ `app.py` 之全文差異

同目錄之 `W-G.9-393R_末端塊之認定之更正_差異.diff`（＝ `git diff 9f825b3 df2ba32 -- app.py`·`194` 列·`+73`／`−20`）。

## ⑨ 工項三之 `checkidx`、`gen_fa_index`

```
$ python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md   ⇒ rc 0
索引列數 124；內部字樣 122；外部指標 9；不合 0
$ python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md   ⇒ rc 0
則 124；加註節 14；列 158
$ cmp <O>/FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md   ⇒ 同（rc 0）
```

## ⑩ 各段耗時（UTC·並行 `2`）

| 段 | 時 | 耗時 |
|---|---|---|
| 接單（`ops/queue` `b9f7934`）、開場、依賴之裝與釘回、`pre-flight` | `06:48`〜`06:51` | 約 `3` 分 |
| 工項零、一（`0e4cc73`、`9f825b3`） | `06:51` | 約 `1` 分 |
| 前置 (甲)(乙)（`20` 呼叫·並行 `2`）與撰碼（並行之時段） | `06:52`〜`07:25` | 呼叫之耗時之和 `3777` s |
| 撰碼中之自跑（`10` 呼叫） | `07:25`〜`07:27` | 之和 `344` s |
| 工項二之 `commit`（`df2ba32`）→ 驗（`84` 呼叫·二批·並行 `2`）與 `V-4`〜`V-8` | `07:28`〜`09:35` 前後 | 之和 `15293` s |
| 唯讀獨立審查（一輪） | 約 `16` 分 | — |
| 工項二之推、工項三（`078fc27`） | `09:53` | 約 `1` 分 |
| 工項四（本報告） | 其後 | — |

---

## 附錄　`V-1` 之 `14` 呼叫之全文（施後·`/tmp/w`·`df2ba32`）

### `#5`　`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`

```
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（609）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
```

### `#6`　`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`

```
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（611）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
```

### `#34`　`python3 verify/probes/probe_WG9352_endblock.py selftest <repo>`

```
── 合成對照（AST 抽出之 end_block_*／solve_G_binary／_select_pool_slot）──
  ✅ S1 左端觸發（未臨正街 45·s_back 3·末端帶 105·R_end 150）：得 (True, 45.0, 3.0, 150.0, 105.0)　期 (True, 45.0, 3.0, 150.0, 105.0)
  ✅ S2 右端觸發（鏡像）：得 (True, 45.0, 3.0, 150.0, 105.0)　期 (True, 45.0, 3.0, 150.0, 105.0)
  ✅ S3 未臨正街 0 ⇒ 亦觸發（左端鉛直·R_end ＝ 末端帶·W-G.9-393）：得 (True, 0.0, 0.0, 105.0, 105.0)　期 (True, 0.0, 0.0, 105.0, 105.0)
  ✅ S4 往後找·等號當選（A 未達、B ＝ 150 當選）：得 ('B(1)', ['未達', '當選'])　期 ('B(1)', ['未達', '當選'])
  ✅ S5 跨占 ≤ 門檻者非候選（T 跨占 0.49 ㎡）：得 'C(1)'　期 'C(1)'
  ✅ S6 跨占街角規定範圍者歸街角側（⛔ 候選）：得 [('B(1)', '跨占街角規定範圍·歸街角側'), ('C(1)', '當選')]　期 [('B(1)', '跨占街角規定範圍·歸街角側'), ('C(1)', '當選')]
  ✅ S7 皆未達 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S8 落位（左）：當選者移至首·餘者原序：得 [('C(1)', True), ('A(1)', False), ('B(1)', False), ('D(1)', False)]　期 [('C(1)', True), ('A(1)', False), ('B(1)', False), ('D(1)', False)]
  ✅ S9 落位（右）：當選者移至末：得 ['A(1)', 'C(1)', 'D(1)', 'B(1)']　期 ['A(1)', 'C(1)', 'D(1)', 'B(1)']
  ✅ S10 落位：當選者為入池閘合併單元之成員 ⇒ 移該單元：得 ['U(1)', 'A(1)']　期 ['U(1)', 'A(1)']
  ✅ S10b 落位：當選者為街角第 1 宗 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S11 首趟評選、次趟沿用（⛔ 重評）：得 ('B(1)', 2, 'B(1)', 0, 3.0, 'B(1)', None)　期 ('B(1)', 2, 'B(1)', 0, 3.0, 'B(1)', None)
  ✅ S11b 二源不一致 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S12 首趟未觸發而本趟觸發 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S13 選槽之 pin（左 pin ⇒ k≥1；右 pin ⇒ k≤n−1）：得 (1, 2, 0)　期 (1, 2, 0)
  ✅ S14 顯示（值皆字串·未觸發之端具名）：得 {'lines': ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；當選 B(1)', 'BX 右端（無側街）：未臨正街 0.0 ㎡ ⇒ 未觸發'], 'rows': [{'街廓': 'BX', '端': '左', '暫編地號': 'A(1)', '試算G(㎡)': '—'}]}　期 {'lines': ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；當選 B(1)', 'BX 右端（無側街）：未臨正街 0.0 ㎡ ⇒ 未觸發'], 'rows': [{'街廓': 'BX', '端': '左', '暫編地號': 'A(1)', '試算G(㎡)': '—'}]}
  ✅ S15 定案趟之檢：首宗非當選者 ⇒ 停機；是 ⇒ 過：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S15b 定案趟之檢：首宗為當選者 ⇒ 過：得 '過'　期 '過'
  ✅ S16 s_back：宗地 ＝ 未臨正街 ∪ [0,S]；G 之 S 只計正街段：得 (True, True, 0.0, -3.0, True)　期 (True, True, 0.0, -3.0, True)
  ✅ S17 s_back＝0 ⇒ 逐位同：得 (True, True, True)　期 (True, True, True)
  ✅ S18 s_back 與 side_mid 並存 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──
  ✅ M0 未突變之抽出版：紅 []（期 []）
  ✅ M1 當選改為嚴格大於：轉紅 ['S4 往後找·等號當選（A 未達、B ＝ 150 當選）', 'S11 首趟評選、次趟沿用（⛔ 重評）']
  ✅ M2 首筆跨占者即當選（⛔ 往後找）：轉紅 ['S4 往後找·等號當選（A 未達、B ＝ 150 當選）', 'S7 皆未達 ⇒ 停機', 'S11 首趟評選、次趟沿用（⛔ 重評）']
  ✅ M3 跨占街角規定範圍者⛔ 排除：轉紅 ['S6 跨占街角規定範圍者歸街角側（⛔ 候選）']
  ✅ M4 落位⛔ 移至首：轉紅 ['S8 落位（左）：當選者移至首·餘者原序', 'S10 落位：當選者為入池閘合併單元之成員 ⇒ 移該單元', 'S11 首趟評選、次趟沿用（⛔ 重評）']
  ✅ M5 未臨正街計入臨街：轉紅 ['S16 s_back：宗地 ＝ 未臨正街 ∪ [0,S]；G 之 S 只計正街段']
  ✅ M6 首趟評選⛔ 沿用：轉紅 ['S11 首趟評選、次趟沿用（⛔ 重評）', 'S12 首趟未觸發而本趟觸發 ⇒ 停機']
  ✅ M7 選槽⛔ 理 pin：轉紅 ['S13 選槽之 pin（左 pin ⇒ k≥1；右 pin ⇒ k≤n−1）']
⇒ 紅 []；rc 0
```

### `#35`　`python3 verify/probes/probe_WG9352_endblock.py wiring <repo>`

```
── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py）──
  ✅ W1 模組層之常數與七函式、函式內⛔ 案件字面（案件字面 []）
  ✅ W2 二宿主於 `_ov2_idx` 前恰一次呼叫 end_block_host（solve_one=_solve_one）
  ✅ W3 左鏈一處、右鏈二處之 `_solve_one` 帶 `_s_back`（二宿主）
  ✅ W4 定案趟呼叫 end_block_assert_head（二宿主）
  ✅ W5 選槽之 pin 與 _kmin_c／_kmax_c（二宿主）
  ✅ W6 非試算趟先清 SS_END_BLOCK_EVAL（二宿主）
  ✅ W7 入池閘之畫面入口於復原之後帶出評選；鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log
  ✅ W8 _WF_NS_NAMES 含 end_block_host／end_block_assert_head／SS_END_BLOCK_EVAL
  ✅ W9 solve_G_binary／_solve_G_one 之 s_back 與 fallback 停機
  ✅ W10 main() 之顯示（end_block_eval_rows 讀 SS_END_BLOCK_EVAL）
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 harness 左鏈去 _s_back：轉紅 ['W3']
  ✅ N2 入池閘之畫面入口⛔ 帶出評選：轉紅 ['W7']
  ✅ N3 畫面選槽去 pin：轉紅 ['W5']
  ✅ N4 harness 非試算趟⛔ 清評選：轉紅 ['W6']
⇒ 紅 []；rc 0
```

### `#69`　`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`

```
  ✅ K1 程式之停機：回 RuntimeError·登記全文（⛔ 截）
  ✅ K2 ⛔ 帶號 ⇒ 停機、⛔ 登記
  ✅ K3 號之邊界（前接英數或連字號者⛔ 號；無數字者⛔ 號）
  ✅ K4 新登記 零／一／二 ⇒ ⛔ 拋／拋其全文／拋其首者
  ✅ K5 巢狀之試算以長度分之
  ✅ K6 入池閘之併入後之試算立程式之停機 ⇒ 上拋
  ✅ K7 對照：配地中止（⛔ 帶號）⇒ 照舊為不過
  ✅ K8 基底（無停機）：X 依手冊併入街角第 1 宗 C
  ✅ K9 換名：K6／K7／K8 之果除名稱外同
  ✅ K10 鏡射：K6／K7／K8 之果除名稱外同
  ✅ K11 旋轉 37°·TWD97：K6／K7／K8 之果除名稱外同
  ✅ K12 鏡射 ＋ 旋轉 213°·TWD97·換名：K6／K7／K8 之果除名稱外同
  ✅ K13 末端塊合併再試之試算立程式之停機 ⇒ 上拋
  ✅ K14 對照：末端塊之試算之配地中止 ⇒ 照舊記試算中止
  ✅ K15 試算之前之登記⛔ 波及（K7 於 K1〜K5 之登記之後）
  ✅ K16 上拋之訊息為全文（號在 1500 字之後）
  ✅ P0 判式自驗 16／16
⇒ 紅 []；rc 0
```

### `#70`　`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`

```
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 12（基準之帶號 10·k980_acq_check 1·end_block_apply 1）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'main', 'select_corner_lots_both_sides_v12']／不合 []）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
```

### `#71`　`python3 verify/probes/probe_WG9389_trialstop.py run <repo>`

```
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
```

### `#75`　`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`

```
  ✅ C1 未輸入 ⇒ 100.5
  ✅ C2 輸入 0 ⇒ 逐位同 C1
  ✅ C3 輸入 100 ⇒ 逐位同 C1
  ✅ C4 輸入恰 100.5 ⇒ 逐位同 C1
  ✅ C5 輸入 150 ⇒ 面積∈[150,150.01]·遠側 x＝5.15·∥SIDE_LINE·含 C1
  ✅ C6 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ C7 輸入 −1 ⇒ 停機
  ✅ C8 C5 之旋轉 37°·鏡射·TWD97 ⇒ 面積同 C5
  ✅ C9 側街斜交（∦ 宗地分配線）輸入 200 ⇒ 面積∈[200,200.01]·遠側界線 ∥ SIDE_LINE（Δx＝6）
  ✅ E1 未輸入 ⇒ R_end 255·內側界 13.5（buf 3.5）
  ✅ E2 輸入恰 255 ⇒ 逐位同 E1
  ✅ E3 輸入 300 ⇒ R_end∈[300,300.01]·內側界 x＝15
  ✅ E4 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ E5 E3 之旋轉·鏡射·TWD97 ⇒ R_end 同 E3
  ✅ E6 _end_region_R 之未輸入與 0 ⇒ R_end 逐位同（255）；end_block_band_width 之 0 ⇒ 停機
  ✅ T1 距 0.02 ⇒ ⛔ 停
  ✅ T2 距恰 0.01 ⇒ 停
  ✅ T3 距 0.005 ⇒ 停
  ✅ T4 重疊 ⇒ 停（訊息具二範圍之名）
  ✅ T5 唯一範圍或含 None ⇒ ⛔ 停
  ✅ T6 三範圍而唯其中二者相接 ⇒ 停
  ✅ K1 有效值之序（K-9-1 ⑨）：街廓覆寫 → 分區底 → 0；session 無鍵或 None ⇒ 0
  ✅ P0 判式自驗 22／22
⇒ 紅 []；rc 0
```

### `#76`　`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`

```
── 接線（工作樹對基準 a8657c4）──
  ✅ W1 _build_corner_range_v3 之呼叫 4（期 ≥ 4）皆傳 min_build_area：皆傳
  ✅ W2 諸呼叫之數 [('end_block_side_geom', 1), ('end_block_host', 2), ('_place_pool_parcels', 2)]（期 ≥ 1、≥ 2、≥ 2）皆傳 min_build_area：皆傳
  ✅ W3 末端帶之單一真相源 {'_place_pool_parcels→_end_region_R': 1, '_place_pool_parcels→_end_band': 0, '_end_region_R→end_block_band_width': 1, 'end_block_band_width 之呼叫（全檔）': 1}（期 1、0、1、1）
  ✅ W4 min_build_area 之值皆為 k980_mba（呼叫 8·期 ≥ 8·不合 []）、v12 之 _mba_pk 之賦值 True、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（4／基準 4）、k980_mba 之分區之引數為字面者 []（期無）
  ✅ W5 k980_range_touch_check 之呼叫 [('select_corner_lots_both_sides_v12', 1), ('f3_screen_stepg_run', 1), ('stepg:_run_step_g_impl', 1)]·app.py 全檔 2（期各 1·app.py 全 2）、其範圍之名齊全 [True, True, True]（期三真）
  ✅ W6 頂層之名之增 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']（期 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']）、減 []
  ✅ W7 新增或改之頂層節點（22）內新增之案件字面 []
  ✅ W8 逐層照傳 min_build_area 皆照傳
  ✅ W9 引擎經 ns 取之新名 ['k980_mba', 'k980_range_touch_check'] ⊆ _WF_NS_NAMES（漏 []）
⇒ 紅 []；rc 0
```

### `#77`　`python3 verify/probes/probe_WG9391_k980x.py run <repo>`

```
  ✅ R1@3.5 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@3.5 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}·不合 []）
  ✅ R1@0.0 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@0.0 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 124.94, 'R2': 164.49, 'R3': 163.8, 'R4': 126.08, 'R5': 177.54, 'R6': 262.28}·不合 []）
⇒ 紅 []；rc 0
```

### `#81`　`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`

```
  ✅ T1 左端無三角地 ⇒ 末端塊（R_end ＝ 末端帶 105·s_back 0·buf 3.5）
  ✅ T2 右端無三角地 ⇒ 同 T1
  ✅ T3a 門檻之下：三角地 0.0005 ㎡ ⇒ 無三角地之讀（s_back 0·R_end ＝ 末端帶）
  ✅ T3b 門檻之下：三角地 0.000999 ㎡ ⇒ 無三角地之讀（s_back 0·R_end ＝ 末端帶）
  ✅ T4a 門檻之上：三角地 0.001001 ㎡ ⇒ 有三角地（s_back ＝ δ·R_end − 末端帶 ＝ 未臨正街）
  ✅ T4b 門檻之上：三角地 0.002 ㎡ ⇒ 有三角地（s_back ＝ δ·R_end − 末端帶 ＝ 未臨正街）
  ✅ T5 有三角地（外斜 3 m）⇒ 舊之形（未臨正街 45·s_back 3·R_end 150·末端帶 105）
  ✅ T6 端之界線內斜（後緣較短）⇒ 末端塊（R_end ＝ 末端帶 ＝ 75）
  ✅ T7 最小建築面積 150 ⇒ R_end ＝ 末端帶 ∈ [150, 150＋容差]·帶寬 5
  ✅ T8 鏡射、旋轉 37°、TWD97 之尺度 ⇒ T1／T2／T6／T7 之量同
  ✅ T9 end_block_apply：左無側街 ⇒ 左觸發·R_end 105·當選 B(1)（A 未達）·落位首；右有側街 ⇒ 無紀錄
  ✅ T9b 二端皆無側街 ⇒ 二端皆觸發（右：E(1) 未達、D(1) 當選而移至末）
  ✅ T12 二端皆無側街而一筆同時跨占二端之 R_end（長 20·A 寬 18）⇒ 停機（GB-207·K-9-60 ①·登記增恰一）
  ✅ T12b 一宗之街廓（長 20）二端皆無側街 ⇒ 同 T12
  ✅ T12c 長 20 而無一筆同時跨占（A 寬 10、B 寬 10）⇒ 過（二端各當選）
  ✅ T10 末端保留（無三角地）：左無側街 ⇒ 池窗起點 0 → 3.5；有側街 ⇒ 0
  ✅ T10b 末端保留（無三角地）：右無側街 ⇒ 池窗寬 40 → 36.5；有側街 ⇒ 40
  ✅ T11 短街廓（長 6）二端之末端帶相疊 ⇒ 停機（K-9-80 ⑥）；長 40 ⇒ 過
⇒ 紅 []；rc 0
```

### `#82`　`python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415`

```
  ✅ W1 end_block_side_geom 之 'gate': False 之回傳 0
  ✅ W2 _place_pool_parcels 之「_unfront 之判 ⇒ continue」0·引 END_BLOCK_UNFRONT_EPS True·寫死 1e-3 0
  ✅ W3 _end_region_R／end_block_band_width 之「frag_poly 空」之停機 []
  ✅ W4 end_block_apply 之 'gate' 之字面 0
  ✅ W5 頂層之名之增 []·減 []·相異之節點 ['_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_side_geom']
  ✅ W6 新增或改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
  ✅ W8 END_BLOCK_UNFRONT_EPS ＝ 0.001
  ✅ W9 end_block_apply 之 `raise k6_program_stop(…GB-207…)` 1（期 1）
⇒ 紅 []；rc 0
```

### `#83`　`python3 verify/probes/probe_WG9393_endall.py run <repo>`

```
  ✅ R1@3.5 末端塊之紀錄：觸發 [('R2', 'right'), ('R3', 'left'), ('R5', 'right'), ('R6', 'left')]·未觸發 []
  ✅ R2@3.5 R_end 之錨不合 []
  ✅ R3@3.5 當選者之錨不合 []
  ✅ R4@3.5 觸發之端之鏈首 ＝ 當選者（不合 []·err None）
  ✅ R1@0.0 末端塊之紀錄：觸發 [('R2', 'right'), ('R3', 'left'), ('R5', 'right'), ('R6', 'left')]·未觸發 []
  ✅ R2@0.0 R_end 之錨不合 []
  ✅ R3@0.0 當選者之錨不合 []
  ✅ R4@0.0 觸發之端之鏈首 ＝ 當選者（不合 []·err None）
⇒ 紅 []；rc 0
```

### `#84`　`python3 verify/probes/probe_WG9352_endblock.py run <repo>`

```
══ 退縮 3.5 ══
  ✅ R1 R2 right：未臨正街 0.00＋末端帶 154.49＝R_end 154.49（紀錄 0.0／154.49／154.49）
  ✅ R2 R2 right：候選與試算 [('628-34(1)', '當選', 601.64)] ＝ 外部錨 [('628-34(1)', '當選', 601.64)]
  ✅ R3 R2 right：鏈首宗 628-34(1)（G 601.64·試算 601.64）⊇ R_end（差 0.000000）
  ✅ R4 R2 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R2：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R3 left：未臨正街 0.00＋末端帶 153.77＝R_end 153.77（紀錄 0.0／153.77／153.77）
  ✅ R2 R3 left：候選與試算 [('628-34(2)', '當選', 257.91)] ＝ 外部錨 [('628-34(2)', '當選', 257.91)]
  ✅ R3 R3 left：鏈首宗 628-34(2)（G 257.91·試算 257.91）⊇ R_end（差 0.000000）
  ✅ R4 R3 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R3：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R5 right：未臨正街 0.00＋末端帶 167.54＝R_end 167.54（紀錄 0.0／167.54／167.54）
  ✅ R2 R5 right：候選與試算 [('628-23(2)', '當選', 430.68)] ＝ 外部錨 [('628-23(2)', '當選', 430.68)]
  ✅ R3 R5 right：鏈首宗 628-23(2)（G 430.68·試算 430.68）⊇ R_end（差 0.000000）
  ✅ R4 R5 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R5：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R6 left：未臨正街 85.71＋末端帶 166.57＝R_end 252.28（紀錄 85.71／166.57／252.28）
  ✅ R2 R6 left：候選與試算 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)] ＝ 外部錨 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)]
  ✅ R3 R6 left：鏈首宗 628-4(1)（G 779.93·試算 779.93）⊇ R_end（差 0.000000）
  ✅ R4 R6 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R6：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
══ 退縮 0.0 ══
  ✅ R1 R2 right：未臨正街 0.00＋末端帶 154.49＝R_end 154.49（紀錄 0.0／154.49／154.49）
  ✅ R2 R2 right：候選與試算 [('628-34(1)', '當選', 601.64)] ＝ 外部錨 [('628-34(1)', '當選', 601.64)]
  ✅ R3 R2 right：鏈首宗 628-34(1)（G 601.64·試算 601.64）⊇ R_end（差 0.000000）
  ✅ R4 R2 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R2：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R3 left：未臨正街 0.00＋末端帶 153.77＝R_end 153.77（紀錄 0.0／153.77／153.77）
  ✅ R2 R3 left：候選與試算 [('628-34(2)', '當選', 257.91)] ＝ 外部錨 [('628-34(2)', '當選', 257.91)]
  ✅ R3 R3 left：鏈首宗 628-34(2)（G 257.91·試算 257.91）⊇ R_end（差 0.000000）
  ✅ R4 R3 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R3：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R5 right：未臨正街 0.00＋末端帶 167.54＝R_end 167.54（紀錄 0.0／167.54／167.54）
  ✅ R2 R5 right：候選與試算 [('628-23(2)', '當選', 430.68)] ＝ 外部錨 [('628-23(2)', '當選', 430.68)]
  ✅ R3 R5 right：鏈首宗 628-23(2)（G 430.68·試算 430.68）⊇ R_end（差 0.000000）
  ✅ R4 R5 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R5：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R6 left：未臨正街 85.71＋末端帶 166.57＝R_end 252.28（紀錄 85.71／166.57／252.28）
  ✅ R2 R6 left：候選與試算 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)] ＝ 外部錨 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)]
  ✅ R3 R6 left：鏈首宗 628-4(1)（G 779.93·試算 779.93）⊇ R_end（差 0.000000）
  ✅ R4 R6 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R6：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
⇒ 紅 []；rc 0
```
