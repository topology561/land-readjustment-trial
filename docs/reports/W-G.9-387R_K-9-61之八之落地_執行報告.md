# `W-G.9-387R` 執行報告：`K-9-61` ⑧ 之落地（原單 `W-G.9-387` 規格單之工項四·由 `W-G.9-387` 補令一之工項一″ 補之）

> 受單 ＝ 執行端（雲端之排程「市地重劃·執行端」·Linux·`nproc` ＝ `4`·Python `3.11.17`·`shapely 2.2.0`）。
> 所據 ＝ `docs/orders/W-G.9-387_規格單.md`（原單·工項四）與 `docs/orders/W-G.9-387_補令一.md`（補令·工項一″ 之 `4`）。
> `<O>` ＝ `/tmp/o387p1`（倉外·在任何 git 工作樹之外）；施工樹 ＝ `/tmp/w`（雲端之完整複本）。
> 工項二″（主線快轉）之出艙與收工閘之實值載於 `ops/queue` 之回報（⛔ 寫入本檔·自指）。

---

## ①　`commit`（全 `40` 碼·首列·作者欄）

| 工項 | `commit` | 首列 | 作者欄 | 增／刪 |
|---|---|---|---|---|
| 原單 零 | `789cccb49e9a771add83b33dc91534f27875bbdd` | `W-G.9-387 工項零：本單原封入倉（新側支）⛔ 零生產碼` | `Claude <noreply@anthropic.com>` | `docs/orders/W-G.9-387_規格單.md` `979`／`0` |
| 原單 一 | `160c3f48608cdc2cd782dfeecdab0c370658ebd8` | `W-G.9-387 工項一：量測器（F31 之新器·F10、F17、F18、F30 之改）（新側支）⛔ 零生產碼` | `Claude <noreply@anthropic.com>` | `probe_WG9351_intake.py` `35`／`4`、`probe_WG9358_k948_wiring.py` `2`／`1`、`probe_WG9359_cand.py` `3`／`1`、`probe_WG9385_k974.py` `2`／`1`、`probe_WG9387_k961h.py` `409`／`0` |
| 原單 二 | `d2c4f65da03f04130e1d125f1beee317a2d4c3fa` | `W-G.9-387 工項二：K-9-61 ⑧ 之落地（合併單位之原街廓：應分配面積之加總 → 重劃前面積之合計 → 最小之暫編地號·k967_rank·⛔ 停機）🔴 生產碼（新側支）` | `Claude <noreply@anthropic.com>` | `app.py` `12`／`7` |
| 原單 三 | `6dae569e97b3f58ba4a6128783c9eaaf26a38bba` | `W-G.9-387 工項三：K-9-61 ⑧ 之 KL 補裁與段三後處理 (a) 之受詞入典·⑧ 之落地之讀法·ops/queue 規則檔之登記 ＋ 待落地清單之更新（新側支）⛔ 零生產碼` | `diag <diag@local>`（KL 本機之 Claude Code 代行） | `CLAUDE.md` `27`／`0`、`K-6` 典 `64`／`0` |
| 補令一 零″ | `405cb7499ae5c18cc195c3c1754793d1a1c7f1c6` | `W-G.9-387 補令一 工項零″：本補令原封入倉（側支）⛔ 零生產碼` | `Claude <noreply@anthropic.com>` | `docs/orders/W-G.9-387_補令一.md` `132`／`0` |

工項零″ 推送：`git push origin HEAD:verify/W-G.9-387-k961h` ⇒ `6dae569..405cb74  HEAD -> verify/W-G.9-387-k961h`（快轉）。
`git cat-file blob HEAD:docs/orders/W-G.9-387_補令一.md` 與來源（`ops/queue` 之 `orders/W-G.9-387_補令一.md`）`cmp` 逐位同。

## ②　原單之停機之事由與工項三之代行

- 引 `ops/queue` 之 `reports/W-G.9-387_規格單_回報.md`（本輪取得時 `3042` B·`git hash-object` ＝ `30d97407b5e5b126e21daceaa387fd6a364a2147`）：原趟之執行端於工項三之第一步（附塊 `P40` 於 `CLAUDE.md`）為雲端環境之權限分類器所拒 ⇒ 停機上呈；工項三由 KL 本機之 Claude Code 代行（KL `2026-10-17 22:42` 同意·作者欄 `diag <diag@local>`）；工項四未做。
- 原趟之 `V-1`〜`V-9` 之出艙在倉外之附件（交 KL）、⛔ 入倉；本報告⛔ 重述其數。發單端之獨立重跑見 `docs/orders/W-G.9-387_補令一.md` 之 `§一″` 項 `2`（隨工項零″ 入倉）。

## ③　補令 `§零″` 之出艙與停機款之三值

### `§零″` 之出艙

| 項 | 出艙 |
|---|---|
| `1` | context 餘量充足（約 `14.9 M` tokens）；`nproc` ＝ `4` |
| `2` | `origin/wip/s1-endpart` ＝ `34736ab959e3d6915abf94bda3977063bf2711e5`；`origin/verify/W-G.9-387-k961h` ＝ `6dae569e97b3f58ba4a6128783c9eaaf26a38bba`；`git ls-remote --heads origin` ＝ `47` 列（存 `<O>/heads_before_387p1.txt`）；`git checkout --detach origin/verify/W-G.9-387-k961h` 後 `git status --porcelain --untracked-files=no` ＝ 空；旗標之出艙 ＝ `[None, None, None, None, None]`（殼之 `WV_` 變數 `0` 個） |
| `3` | `probe_WG9321_issuer_anchor.py /tmp/w /tmp/o387p1/z3_anchor_out.txt 623 622` ⇒ `rc 0`·`stderr` `0` B；項4′ 四簿·正典框：自誤 `608`／`623`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`；落檔 `sha256` `b8abbacc20c4cbae64194c3a6328f79b34d1d1e8d0c790e864ed0f865d9d349c` |
| `4` | 補令 `25221` B·`sha256` `f87b02d13794b0fcd636ea6fb29e09e5be2813499a9db245f7376cd9c74e087d`（＝ `STATE.json` 之 `order_bytes`／`order_sha256`）；`SELF_SHA256` 自驗（受詞 `25143` B）＝ `b503caee9b75b14420ee4399537b969d43f97028c079052beaaf53a79fc78e1c`（＝ 單載）；`CR` `0` |
| `5` | 初驗 `ModuleNotFoundError: No module named 'shapely'`（`rc 1`）⇒ 依 README 第六節第 `2` 款 `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`·出艙 `<O>/z0_pip.txt`）⇒ 再驗 `rc 0`（`shapely 2.2.0`） |
| `6` | pre-flight ⇒ 見 ⑦ |

### 停機款（唯工項一″ 之 `commit` 前可量者）

| 款 | 期 | 實 |
|---|---|---|
| `1″` | 主線 `34736ab`、側支 `6dae569`、heads `47`、追蹤檔無變動、項 `3` `rc 0` 且四簿 ＝ 期、旗標 ＝ 五 `None`、環境可匯入 | 皆符（環境於安裝後可匯入）⇒ 未觸 |
| `2″` | `SELF_SHA256` 相符；`STATE.json` 之 bytes／`sha256` 相符；入倉後 blob 與來源逐位同 | 皆符 ⇒ 未觸 |
| `3″` | 工項一″ 之重量 ＝ 期；差異檔之 blob ＝ `a1d0e389…` | 皆符（見 ④）⇒ 未觸 |
| `4″`〜`6″` | 工項二″ 之前置與快轉 | 工項一″ 之 `commit` 後方可量 ⇒ 見回報 |
| `7″` | 工項零″ 之 `push` 目標 ＝ `verify/W-G.9-387-k961h` | 符（`6dae569..405cb74`）⇒ 未觸；工項一″、二″ 見回報 |
| `8″` | 收工閘 | 工項二″ 後方可量 ⇒ 見回報 |
| `9″` | ⛔ 自判、⛔ 改器／命令；新檔⛔ 為 `check-ignore` 所命中 | 未作任何判、未改器一字；本補令、差異檔之 `git check-ignore -v --no-index` 皆 `rc 1`（無命中）⇒ 未觸 |
| `10″` | 存取與寫入⛔ 被拒 | 至此無被拒 ⇒ 未觸 |

## ④　工項一″ 之 `2`、`3` 之全部出艙

### 差異檔（工項一″ 之 `1`）

`git diff --no-color --no-ext-diff 160c3f48608cdc2cd782dfeecdab0c370658ebd8 d2c4f65da03f04130e1d125f1beee317a2d4c3fa -- app.py` ⇒ `docs/reports/W-G.9-387R_K-9-61之八之落地_app差異.diff`：`4082` B·`44` 列·`git hash-object` ＝ `a1d0e389268dcf6612272d208c63e048bc6a993f`·`sha256` ＝ `1db8c9bc12ad67d47674d866fc86215a1860e1031e3d9606b4c67f91560fe07c`（＝ 補令 `§五″` 項 `4`）。

### `2`　檢索之重跑（於側支之端 `405cb74`）

- 塊之抽取（自 `docs/orders/W-G.9-365_輕量單.md`·原單 `§五-1` 末之抽取式）：`CK`（`## 附錄午`·圍欄開列 `807`·閉列 `839`）`1539` B·`sha256` `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列；`GF`（`## 附錄巳`·開列 `755`·閉列 `803`）`2445` B·`sha256` `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列 ⇒ 皆 ＝ 原單 `§五-1` 項 `7`。寫為 `<O>/checkidx.py`、`<O>/gen_fa_index.py`（⛔ 入倉）。
- `python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`·`stderr` `0` B·末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md` ⇒ `rc 0`·`stderr` `0` B·出艙 `則 124；加註節 14；列 158`；`cmp <O>/FX_regen.md .claude/skills/failure-archaeology-index/SKILL.md` ⇒ 逐位同。

### `3`　重量（並行 `2`：甲、乙同時）

| 組 | 呼叫 | `rc` | `stderr` | 耗時 | 末列 |
|---|---|---|---|---|---|
| 甲（`/tmp/w`·側支之端 `405cb74`） | `probe_WG9387_k961h.py selftest /tmp/w` | `0` | `0` B | `4` s | `⇒ 紅 []；rc 0` |
| 甲 | `probe_WG9387_k961h.py wiring /tmp/w 34736ab` | `0` | `0` B | `4` s | `⇒ 紅 []；rc 0` |
| 甲 | `probe_WG9351_intake.py selftest /tmp/w` | `0` | `0` B | `16` s | `⇒ 紅 []；rc 0` |
| 乙［必紅］（`<S>` ＝ `/tmp/s387`·`git worktree add --detach` 於 `160c3f48608cdc2cd782dfeecdab0c370658ebd8`） | `probe_WG9387_k961h.py selftest /tmp/s387` | `1` | `0` B | `4` s | `⇒ 紅 ['K2', 'K3', 'K5', 'K8', 'K9', 'K10', 'K11', 'K13', 'K15', 'K16', 'K17', 'K18']；rc 1` |
| 乙 | `probe_WG9387_k961h.py wiring /tmp/s387 34736ab` | `1` | `0` B | `4` s | `⇒ 紅 ['X1', 'X2']；rc 1` |
| 乙 | `probe_WG9351_intake.py selftest /tmp/s387` | `1` | `0` B | `16` s | `⇒ 紅 ['S6 應分配面積並列 ⇒ 重劃前面積較大者']；rc 1` |

乙之末列皆逐字 ＝ 原單 `§四-1` 工項二前置 `1` 之三列；其後 `git worktree remove --force /tmp/s387`（`git worktree list` 唯 `/tmp/w`）。

丙：`git grep -c -F "<字樣>" <commit> -- app.py`（出艙之前綴 `<commit>:` 為 git 以樹為受詞時之固有形；計數值如下）：

| 字樣 | `d2c4f65`（施後） | `160c3f4`（施前） |
|---|---|---|
| `之原街廓：應分配面積並列` | 無出艙·`rc 1` | `app.py:1`·`rc 0` |
| `float(_r['原有面積'])` | `app.py:1` | `app.py:1` |
| `float(_r['應分配面積'])` | `app.py:1` | `app.py:1` |
| `if _pool or (_cm and not _al):` | `app.py:1` | `app.py:1` |
| `if '段三併出' in t:` | `app.py:1` | `app.py:1` |

⇒ ＝ 補令 `§一″` 項 `2` 之值。

## ⑤　設計說明（原單 `§三-5`·依差異檔逐條·**撰碼者 ＝ 原趟之執行端**）

- `R-1`（`adj_intake` 之原街廓之擇·差異檔第三段 `@@ -12577,12 +12580,14 @@`）：去既有之四句——`_top = max(_basis.values())`、`_cands = sorted(...)`、`if len(_cands) != 1: raise RuntimeError(...應分配面積並列...)`、`_home = _cands[0]`；代以：
  - `_pre387, _pid387 = {}, {}`；
  - 迴圈 `for _r387 in _pool:`——`_pre387[_b387] += float(_r387['原有面積'])`（街廓之重劃前面積·每一池列皆計·⛔ 依 `所屬單元` 去重）；`_pid387[_b387] = min(_pid387.get(_b387, _r387['暫編地號']), _r387['暫編地號'])`（街廓之最小暫編地號·字串之比）；
  - `_home = min((k967_rank(_v, _pre387[_b], _pid387[_b]), _b) for _b, _v in _basis.items())[1]`——`k967_rank` 直呼（⛔ 另寫）；`_basis` 之建之迴圈（`_seen`、`float(_r['應分配面積'])` 之累加）⛔ 動；`原街廓之據` 仍 ＝ `_basis`；⛔ 增 `raise`。
  - 新之區域名皆以 `387` 為尾（`_pre387`、`_pid387`、`_r387`、`_b387`）；字面 `float(_r['原有面積'])` 未出現於新碼（新碼用 `float(_r387['原有面積'])`·`§三-3` 之 `2`）。
- `R-2`（docstring·差異檔第一、二段）：「停機」之列舉之末去「原街廓之應分配面積並列（【未裁】）」（`殘料之原有面積 \`> 0\`；` ⇒ `殘料之原有面積 \`> 0\`。`）；增 `🔧 \`W-G.9-387\`（\`K-9-61\` ⑧·KL 補裁 \`2026-10-17 14:55\` 第 1 點、\`15:23\`「甲」）` 之註三列，載三鍵與「三鍵之後必唯一 ⇒ ⛔ 停機」。
- `R-3`（其餘）：差異之三段皆在 `adj_intake` 之內（行 `12344`〜`12593` 之間）；他處⛔ 動（`app.py` `+12`／`-7`）。

## ⑥　二簿之改前改後（`34736ab` → `6dae569`）

| 簿 | 改前 bytes／blob | 改後 bytes／blob |
|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `829153`／`6f502cd8cca1f617beb5b9345325aef22a75b251` | `837880`／`a880ba93f826ad3ce3bf79c4dfe910fd16c43b0c` |
| `CLAUDE.md` | `415049`／`0b36e0d292941ea380d1b5dc40718081680ec6d5` | `419752`／`66e9c07af114da5cbe3eaff30c78008540c2836f` |

本補令⛔ 動二簿（零″、一″ 皆唯新檔）。

## ⑦　pre-flight 之出艙與處置

`python3 verify/probes/probe_order_preflight.py /tmp/w/W-G.9-387_補令一.md` ⇒ `rc 0`·`stderr` `0` B：

- 🔴 機械 `0` 項。
- 🟡 提示 `1` 項：`[P-4] :48` 方向性轉引而同段⛔ 未具名座標系（`§一″` 項 `1`）——處置：＝ 補令 `§五″` 項 `3` 之**具名豁免**（其「反向」與「→」唯 git 之 `commit` 之範圍與二簿之 bytes 之改前改後，座標系即 git 之祖孫之序）；照單豁免，⛔ 自判。
- ℹ️ 記錄 `2` 項：`[P-5] :132` `SELF_SHA256` ✅ 相符（受詞 `25143` B）；`[P-3]` `app.py` 之 `def main` 區間 ＝ `23356`-`31098`（本補令⛔ 用）。

⇒ 與補令 `§五″` 項 `3` 之發單端實跑同。

## ⑧　執行端之自捕與自解

1. 環境初未裝依賴（`shapely` 缺）⇒ 依 README 第六節第 `2` 款以 `python3 -m pip` 裝之，再驗 `rc 0`（`§零″` 項 `5` 所許）。
2. 丙之 `git grep -c` 以 `commit` 為受詞時，出艙帶 `<commit>:` 之前綴（如 `d2c4f65…:app.py:1`）；此為命令之固有形，計數值 ＝ 期；照實載之，⛔ 改命令。
3. 補令之副本於施工樹之根（`/tmp/w/W-G.9-387_補令一.md`·`執行端.md` 丙 `3`）未追蹤、⛔ 入 `commit`（入倉者唯 `docs/orders/` 之一份）。

## ⑨　各段耗時（並行之數）

| 段 | 耗時 | 並行 |
|---|---|---|
| 佇列之取得、驗單、接單（`ops/queue` 推 `341281a..ed619ea`） | 約 `1` 分 | `1` |
| 完整複本之 `clone`、`fetch`、`§零″` 項 `2` | 約 `10` s | `1` |
| 依賴之安裝（`pip`） | 約 `1` 分 | `1` |
| `§零″` 項 `3`（issuer_anchor）、項 `6`（pre-flight） | 約 `30` s | `1` |
| 工項零″（入倉、`commit`、`push`） | 約 `10` s | `1` |
| 工項一″ `1`（差異檔）、`2`（檢索之重跑） | 約 `10` s | `1` |
| 工項一″ `3` 甲＋乙（牆鐘） | `24` s | `2` |
| 工項一″ `3` 丙 | `< 1` s | `1` |
| 本報告之撰 | 約 `2` 分 | — |
