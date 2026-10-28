# `W-G.9-398R1`　街角地側面道路負擔之寬度先取至公釐·跳處取較接近者　執行報告（補令一〔經補令二之代換〕之工項零‴〜四″）

> **單** ＝ `docs/orders/W-G.9-398_補令一.md`（`146863` B·`3c1e6621…`·`SELF_SHA256` `7c0d3516…`）＋ `docs/orders/W-G.9-398_補令二.md`（`31655` B·`a10c4f83…`·`SELF_SHA256` `8acda597…`·本報告依補令二 `D-11` 之載）。原單 ＝ `docs/orders/W-G.9-398_規格單.md`。
> **執行端** ＝ 雲端之排程「市地重劃·執行端」（`effort=high`）；施工樹 ＝ `/tmp/w`（雲端之完整複本）；撰碼之樹 ＝ `/tmp/w2`（同倉之 `git worktree`·倉外·⛔ 入倉）；`<O>` ＝ `/tmp/O`（倉外）。
> **結果** ＝ 工項零‴、二″、三″、四″ 皆畢、皆快轉推至新側支 `verify/W-G.9-398-rw25`；前置″ 皆合期；`V-1″`〜`V-9″` 皆合期；**本案配地之改變 ＝ 補令一 `§一″` 項 `5`（＝ 請示表戊欄·3.5 m `3` 項／0 m `7` 項·逐字同）**；唯讀獨立審查無擋者（其發現與處置見 ⑥-2）；停機款 `0` 款成就。主線⛔ 動。收工閘之實測值見 `ops/queue` 之 `reports/W-G.9-398_補令二_回報.md`（⛔ 寫入本檔·自指）。
> **補令一之停機**：前輪之執行端於補令一工項二″ 之前置″ 項 `4` 停機（停機款 `4″`·期書「恰 `18` 列」而實 `19` 列）；其回報 ＝ `ops/queue` 之 `reports/W-G.9-398_補令一_回報.md`；其已推之工項零″ `ce6912d`、一″ `8bc2add` 由本輪承之（補令二 `D-1`·⛔ 重做）。

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 父 | 推送（快轉） | 首列（逐字·其後空列＋環境之尾列二列） |
|---|---|---|---|---|
| 零″（前輪） | `ce6912dc8d044db3d5bb5449420a3c1708357ca1` | `f748370` | 前輪 | `W-G.9-398 工項零″：補令一原封入倉（新側支）⛔ 零生產碼` |
| 一″（前輪） | `8bc2add56c7f7201219db0064e3cdfedc30681fe` | `ce6912d` | 前輪 | `W-G.9-398 工項一″：量測器（F41 之公釐之取位與跳處之例·既有之器之增許與更錨）（新側支）⛔ 零生產碼` |
| **零‴** | `d3b6a7eefa3675310e89e6c58c0ddbcfad710e82` | `8bc2add` | `8bc2add..d3b6a7e` | `W-G.9-398 工項零‴：補令二原封入倉（新側支）⛔ 零生產碼` |
| **二″** | `7c819b53038f14109693ce8c572a029f361e97e7` | `d3b6a7e` | `d3b6a7e..7c819b5`（驗與審查皆符後） | `W-G.9-398 工項二″：街角地側面道路負擔之寬度先四捨五入至公釐再依附表 25 內插·跳處取較接近者（KL 2026-10-27 23:29 採戊·2026-10-28 10:48）🔴 生產碼（新側支）` |
| **三″** | `c112df1b7c937c3e4a2fc3c764b165161066e0d1` | `7c819b5` | `7c819b5..c112df1` | `W-G.9-398 工項三″：寬度取至公釐與跳處之甲之入典·自誤 642〜644·待落地清單之更新（新側支）⛔ 零生產碼`（補令二 `D-4`） |
| **四″** | 本報告之 `commit`（自指·見回報） | `c112df1` | 見回報 | `W-G.9-398 工項四″：執行報告入倉（新側支）⛔ 零生產碼` |

`git show --numstat`：零‴ ＝ `docs/orders/W-G.9-398_補令二.md` `137`／`0`（唯此）；二″ ＝ `app.py` `78`／`12`、`verify/stepg_pipeline.py` `1`／`1`（唯此二）；三″ ＝ `K-6` 典 `81`／`0`、自誤簿 `35`／`0`、`docs/待落地清單.md` `16`／`0`（唯此三）。施後之生產碼之 blob：`app.py` ＝ `ca9f917e15a036922889783bff1b1049edb388f6`（`1900538` B）、`verify/stepg_pipeline.py` ＝ `c9d347c28d41d8a9d59ce3367748e9ae783430ee`（`125864` B）。

## ② 停機款之三值

### 補令二之 `1‴`〜`4‴`

| 款 | 期 | 實 |
|---|---|---|
| `1‴` | 主線 `20e03bf`；側支 `8bc2add`；heads（濾後）`56`；追蹤檔無變動；三 blob；`issuer_anchor … 641 640` `rc 0`·四簿 ＝ 期；旗標 `[None×5]`；環境可匯入 | 主線 `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`；側支 `8bc2add56c7f7201219db0064e3cdfedc30681fe`；heads `56`（`<O>/heads_before_398p2.txt`）；`git status --porcelain --untracked-files=no` 空；`app.py` `87e784a3…`（`1895636` B）、`verify/stepg_pipeline.py` `0cd22fc9…`（`125864` B）、`probe_WG9398_rw25.py` `61465423…`（`32318` B）；`rc 0`·自誤 `626`／`641`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；旗標 `[None, None, None, None, None]`；匯入 `rc 0`（裝後）⇒ ⛔ 成就 |
| `2‴` | 本補令之 `SELF_SHA256`、bytes／`sha256`；補令一之值；入倉 blob | 本補令 `31655` B·`a10c4f839dfe9fcb0b6a29888056f4eb6bda573958627151ea568ee8ed1b7923`（＝ `STATE.json`）·`SELF_SHA256` 自驗 `8acda5975c1bd16134b9e54fa1111ffa69db7a8196fccdda5a62993e4528b491`（合·受詞 `31577` B）；補令一（`git cat-file blob 8bc2add:…`）`146863` B·`3c1e6621ccbd4721c613ebda5311214e0ce16a88e3462a03aefce57259391f89`·`SELF_SHA256` `7c0d3516ed6e8ac97b358c29ca8ec61e4535a73f2fc18ade853c7be5cf739037`（合）；入倉後 `git cat-file blob HEAD:docs/orders/W-G.9-398_補令二.md` 與來源 `cmp` 逐位同 ⇒ ⛔ 成就 |
| `3‴` | 塊 `E45` 與補令一之四塊 | `E45` `2371` B·`0fcf0358…`·`13` 列；`Fy56` `49904` B·`89d49c8b…`·`695` 列；`K47` `15535` B·`cc11da14…`·`81` 列；`E44` `3868` B·`e46c6b16…`·`22` 列；`P58` `3018` B·`302bad90…`·`16` 列 ⇒ 皆合 ⇒ ⛔ 成就 |
| `4‴` | 補令一 `3″`〜`13″` | 見下表 ⇒ ⛔ 成就 |

### 補令一之 `1″`〜`13″`（受詞依補令二 `§三‴` 之代換）

| 款 | 實 |
|---|---|
| `1″`、`2″` | 由 `1‴`、`2‴` 代之（上表） |
| `3″` | 四塊之 bytes／`sha256`／列數皆合（`3‴`）；`Fy56` 之施⛔ 重做（`D-1`）；其 `18` 檔之 blob 由 `V-3″` 量之（`18／18`） ⇒ ⛔ 成就 |
| `4″` | 前置″ 皆合期（③-1〜③-3） ⇒ ⛔ 成就 |
| `5″` | 規格無涉域之歧義；⛔ 須改禁改 ⇒ ⛔ 成就 |
| `6″` | `V-1″`〜`V-9″` 皆合期；⛔ 改器；本案配地之改變 ＝ `§一″` 項 `5` ⇒ ⛔ 成就 |
| `7″` | 推送之目標唯 `verify/W-G.9-398-rw25`（四次快轉·含工項四″）與 `ops/queue`；⛔ 被拒；⛔ `--force`；主線⛔ 動 ⇒ ⛔ 成就 |
| `8″` | 三檔之改前為改後之嚴格前綴、刪除欄 `0`、其尾 ＝ 塊（自誤簿之尾 ＝ `E44`＋`E45`·`D-4`）、blob ＝ 期；`checkidx`／`gen_fa_index` ＝ 期（④、⑨） ⇒ ⛔ 成就 |
| `9″` | 收工閘見回報 |
| `10″` | ⛔ 改單、塊、器、命令一字；⛔ 作孰為正典之判 ⇒ ⛔ 成就 |
| `11″` | 新檔（補令二、報告二檔）之 `git check-ignore -v --no-index` 皆 `rc 1` ⇒ ⛔ 成就 |
| `12″` | 審查之發現⛔ 為本補令之域判之未定（⑥-2） ⇒ ⛔ 成就 |
| `13″` | 存取與寫入皆⛔ 被拒 ⇒ ⛔ 成就 |

## ③ 前置″ 與驗之出艙

### ③-0 開場（`§零-0‴`）

- context 餘量充足（約 `14.8M` tokens）；`nproc` ＝ `4`。
- 環境：初 `No module named 'shapely'` ⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ 原單之七釘、去 `tzdata`、`narwhals==2.27.1 fonttools==4.67.0`（`rc 0`）⇒ 六模組匯入 `rc 0`；`pip check` ⇒ `No broken requirements found.`
- 版本之比對：`Python 3.11.17`；`pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（＝ 基準 `20e03bf` 所載）。開工之端 ≠ 主線之端、`基準/` ⛔ 存其 sha 之檔 ⇒ 前置″ (丙) **整份照跑**（單首 🔑）。
- pre-flight：本補令 ⇒ `rc 0`·🔴 `0`／🟡 `0`／ℹ️ `2`（`P-5` ✅ 受詞 `31577` B；`P-3` `def main` ＝ `23979`-`31722`）＝ 補令二 `§五‴` 項 `5`；補令一（唯記錄）⇒ `rc 0`·🔴 `0`／🟡 `7`（`[P-1] :1064`、`[P-4] :69`、`:123`、`:180`、`:211`、`:1062`、`:1064` ＝ 補令一 `§五″` 項 `9` 之具名豁免）。

### ③-1 前置″ 項 `4`（補令二 `D-3`·於工項零‴ 之端 `d3b6a7e`）

（甲）`git -c core.quotepath=false diff --name-status f748370 8bc2add56c7f7201219db0064e3cdfedc30681fe` ⇒ **`19` 列**（逐字 ＝ 補令二 `§五‴` 項 `4` 之（甲）·以程式自單之文抽出而比 ⇒ `True`）：

```
A	docs/orders/W-G.9-398_補令一.md
M	tests/test_pool_slot.py
M	verify/probes/probe_WG9352_endblock.py
M	verify/probes/probe_WG9363_k953.py
M	verify/probes/probe_WG9367_adj4.py
M	verify/probes/probe_WG9370_adj4mut.py
M	verify/probes/probe_WG9373_k966.py
M	verify/probes/probe_WG9375_k965.py
M	verify/probes/probe_WG9385_k974.py
M	verify/probes/probe_WG9387_k961h.py
M	verify/probes/probe_WG9388_k961s3.py
M	verify/probes/probe_WG9389_trialstop.py
M	verify/probes/probe_WG9390_k961r.py
M	verify/probes/probe_WG9391_k980x.py
M	verify/probes/probe_WG9392_k980g.py
M	verify/probes/probe_WG9393_endall.py
M	verify/probes/probe_WG9394_k9615.py
M	verify/probes/probe_WG9395_k960.py
M	verify/probes/probe_WG9398_rw25.py
```

（乙）`git -c core.quotepath=false diff --name-status 8bc2add56c7f7201219db0064e3cdfedc30681fe d3b6a7eefa3675310e89e6c58c0ddbcfad710e82` ⇒ **`1` 列**：

```
A	docs/orders/W-G.9-398_補令二.md
```

三字樣（`git grep -c -F "<字樣>" -- app.py`·於 `d3b6a7e`）：`rw_width_mm`、`rw_pct_2dp`、`jump398` ⇒ 各無出艙、`rc 1`。

### ③-2 `94` 呼叫之表（前置″ ＝ 工項零‴ 之端；驗 ＝ 工項二″ 之 `commit`·二態皆從頭整份照跑·⛔ 沿用·並行 `2`·殼無 `WV_`·其期 ＝ 補令一 `§五″` 項 `8`〔原單之表之施後之列·補令一之改之八列〕）

「段」：甲 ＝ 前置″ (甲) 之 `50` 呼叫；乙 ＝ (乙) 之 `6` 呼叫（`#56`〜`#61`）；丙 ＝ (丙) 之 `38` 呼叫。合期之判 ＝ `rc` ＝ 期、末列逐字 ＝ 期（`#56`／`#57` 之 JSON 之摘要列與前置″ `#94` 之空列⛔ 比字）、`stderr` 之有無 ＝ 期。重跑：無（皆一趟合期）。

| # | 段 | 命令 | 前置″（工項零‴ 之端 `d3b6a7e`）rc／stderr B／s／末列／合期 | 驗（工項二″ `7c819b5`）rc／stderr B／s／末列／合期 |
|---|---|---|---|---|
| `1` | 甲 | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／2.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.5／`⇒ 紅 []；rc 0`／✅ |
| `2` | 甲 | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／117.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／112.3／`⇒ 紅 []；rc 0`／✅ |
| `3` | 甲 | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／392.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／378.9／`⇒ 紅 []；rc 0`／✅ |
| `4` | 甲 | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.0／`⇒ 紅 []；rc 0`／✅ |
| `5` | 甲 | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／34.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／37.1／`⇒ 紅 []；rc 0`／✅ |
| `6` | 甲 | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／36.4／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／37.6／`⇒ 紅 []；rc 0`／✅ |
| `7` | 甲 | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／3.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／3.4／`⇒ 紅 []；rc 0`／✅ |
| `8` | 丙 | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ |
| `9` | 丙 | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ |
| `10` | 丙 | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／35.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／37.9／`⇒ 紅 []；rc 0`／✅ |
| `11` | 丙 | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／14.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／15.0／`⇒ 紅 []；rc 0`／✅ |
| `12` | 丙 | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／214.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／230.2／`⇒ 紅 []；rc 0`／✅ |
| `13` | 甲 | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ |
| `14` | 甲 | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.2／`⇒ 紅 []；rc 0`／✅ |
| `15` | 甲 | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／2.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.2／`⇒ 紅 []；rc 0`／✅ |
| `16` | 甲 | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `1`／`0`／66.7／`⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1`／✅ | `0`／`0`／71.6／`⇒ 紅 []；rc 0`／✅ |
| `17` | 甲 | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `1`／`0`／426.0／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`／✅ | `0`／`0`／427.9／`⇒ 紅 []；rc 0`／✅ |
| `18` | 甲 | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `1`／`0`／594.7／`⇒ 紅 ['R3@0.0']；rc 1`／✅ | `0`／`0`／595.8／`⇒ 紅 []；rc 0`／✅ |
| `19` | 甲 | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／9.1／`⇒ 突變 8（另基準一）；紅 []；rc 0`／✅ | `0`／`0`／9.3／`⇒ 突變 8（另基準一）；紅 []；rc 0`／✅ |
| `20` | 甲 | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ |
| `21` | 甲 | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／3.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／3.1／`⇒ 紅 []；rc 0`／✅ |
| `22` | 甲 | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／67.3／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`／✅ | `0`／`0`／71.1／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`／✅ |
| `23` | 甲 | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `1`／`0`／364.6／`⇒ 紅 ['R2@0.0']；rc 1`／✅ | `0`／`0`／365.8／`⇒ 紅 []；rc 0`／✅ |
| `24` | 丙 | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／2.3／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ |
| `25` | 丙 | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／1679.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1610.5／`⇒ 紅 []；rc 0`／✅ |
| `26` | 丙 | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／30.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／32.8／`⇒ 紅 []；rc 0`／✅ |
| `27` | 丙 | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ |
| `28` | 丙 | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／6.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／5.4／`⇒ 紅 []；rc 0`／✅ |
| `29` | 丙 | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／23.7／`⇒ rc 0（不符 0·器紅 0）`／✅ | `0`／`0`／25.6／`⇒ rc 0（不符 0·器紅 0）`／✅ |
| `30` | 丙 | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／2.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.3／`⇒ 紅 []；rc 0`／✅ |
| `31` | 丙 | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／19.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／20.4／`⇒ 紅 []；rc 0`／✅ |
| `32` | 丙 | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／223.8／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／239.4／`⇒ 紅 []；rc 0`／✅ |
| `33` | 丙 | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／307.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／314.5／`⇒ 紅 []；rc 0`／✅ |
| `34` | 甲 | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／31.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／37.2／`⇒ 紅 []；rc 0`／✅ |
| `35` | 甲 | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／34.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／37.7／`⇒ 紅 []；rc 0`／✅ |
| `36` | 丙 | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／7.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／7.7／`⇒ 紅 []；rc 0`／✅ |
| `37` | 丙 | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／23.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／25.1／`⇒ 紅 []；rc 0`／✅ |
| `38` | 丙 | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／15.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／16.5／`⇒ 紅 []；rc 0`／✅ |
| `39` | 丙 | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／12.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／12.2／`⇒ 紅 []；rc 0`／✅ |
| `40` | 丙 | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／173.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／169.4／`⇒ 紅 []；rc 0`／✅ |
| `41` | 丙 | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ |
| `42` | 丙 | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／46.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／51.0／`⇒ 紅 []；rc 0`／✅ |
| `43` | 丙 | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／785.4／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／781.8／`⇒ 紅 []；rc 0`／✅ |
| `44` | 丙 | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ |
| `45` | 丙 | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／1.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.4／`⇒ 紅 []；rc 0`／✅ |
| `46` | 丙 | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／135.8／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／142.7／`⇒ 紅 []；rc 0`／✅ |
| `47` | 丙 | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／116.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／120.9／`⇒ 紅 []；rc 0`／✅ |
| `48` | 丙 | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ |
| `49` | 丙 | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／294.3／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／309.7／`⇒ 紅 []；rc 0`／✅ |
| `50` | 丙 | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／0.0／`selftest 9/9 ⇒ ✅`／✅ | `0`／`0`／0.0／`selftest 9/9 ⇒ ✅`／✅ |
| `51` | 丙 | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／0.0／`selftest 13/13 ⇒ ✅`／✅ | `0`／`0`／0.0／`selftest 13/13 ⇒ ✅`／✅ |
| `52` | 丙 | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／2.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.7／`⇒ 紅 []；rc 0`／✅ |
| `53` | 丙 | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／1.6／`ε ＝ 0.0002｜rc 0`／✅ | `0`／`0`／1.6／`ε ＝ 0.0002｜rc 0`／✅ |
| `54` | 丙 | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／10.9／`紅項 [] 器紅 0`／✅ | `0`／`0`／11.0／`紅項 [] 器紅 0`／✅ |
| `55` | 丙 | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／295.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／307.7／`⇒ 紅 []；rc 0`／✅ |
| `56` | 乙 | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/pre/k6s3_pre_35.json` | `0`／`0`／177.0／`（JSON 之摘要列·略）`／✅ | `0`／`0`／181.4／`（JSON 之摘要列·略）`／✅ |
| `57` | 乙 | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/pre/k6s3_pre_00.json` | `0`／`0`／124.8／`（JSON 之摘要列·略）`／✅ | `0`／`0`／130.7／`（JSON 之摘要列·略）`／✅ |
| `58` | 乙 | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/pre/f8_pre_35.json` | `0`／`0`／177.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／178.1／`⇒ 紅 []；rc 0`／✅ |
| `59` | 乙 | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/pre/f8_pre_00.json` | `0`／`0`／125.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／128.5／`⇒ 紅 []；rc 0`／✅ |
| `60` | 乙 | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/pre/parity35_pre.json` | `0`／`0`／387.1／`⇒ rc 0（不符 0 項）`／✅ | `0`／`0`／391.8／`⇒ rc 0（不符 0 項）`／✅ |
| `61` | 乙 | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/pre/parity00_pre.json` | `0`／`0`／262.9／`⇒ rc 0（不符 0 項）`／✅ | `0`／`0`／275.4／`⇒ rc 0（不符 0 項）`／✅ |
| `62` | 甲 | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／3.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／3.7／`⇒ 紅 []；rc 0`／✅ |
| `63` | 甲 | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／3.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／3.4／`⇒ 紅 []；rc 0`／✅ |
| `64` | 甲 | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／300.2／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／307.3／`⇒ 紅 []；rc 0`／✅ |
| `65` | 甲 | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／2.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.0／`⇒ 紅 []；rc 0`／✅ |
| `66` | 甲 | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／2.4／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.5／`⇒ 紅 []；rc 0`／✅ |
| `67` | 丙 | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／1158.8／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1124.1／`⇒ 紅 []；rc 0`／✅ |
| `68` | 丙 | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／1090.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1079.3／`⇒ 紅 []；rc 0`／✅ |
| `69` | 甲 | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ |
| `70` | 甲 | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／120.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／120.5／`⇒ 紅 []；rc 0`／✅ |
| `71` | 甲 | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／412.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／417.3／`⇒ 紅 []；rc 0`／✅ |
| `72` | 甲 | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／1.9／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.6／`⇒ 紅 []；rc 0`／✅ |
| `73` | 甲 | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／2.4／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／2.3／`⇒ 紅 []；rc 0`／✅ |
| `74` | 甲 | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／304.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／301.3／`⇒ 紅 []；rc 0`／✅ |
| `75` | 甲 | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／1.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.6／`⇒ 紅 []；rc 0`／✅ |
| `76` | 甲 | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／38.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／46.5／`⇒ 紅 []；rc 0`／✅ |
| `77` | 甲 | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／612.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／603.1／`⇒ 紅 []；rc 0`／✅ |
| `78` | 甲 | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `0`／`0`／6.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／7.3／`⇒ 紅 []；rc 0`／✅ |
| `79` | 甲 | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `0`／`0`／4.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／4.9／`⇒ 紅 []；rc 0`／✅ |
| `80` | 甲 | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `1`／`0`／310.1／`⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1`／✅ | `0`／`0`／317.6／`⇒ 紅 []；rc 0`／✅ |
| `81` | 甲 | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.6／`⇒ 紅 []；rc 0`／✅ |
| `82` | 甲 | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `0`／`0`／4.1／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／4.3／`⇒ 紅 []；rc 0`／✅ |
| `83` | 甲 | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | `0`／`0`／300.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／302.7／`⇒ 紅 []；rc 0`／✅ |
| `84` | 甲 | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | `0`／`0`／293.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／307.9／`⇒ 紅 []；rc 0`／✅ |
| `85` | 甲 | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.8／`⇒ 紅 []；rc 0`／✅ |
| `86` | 甲 | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | `0`／`0`／4.5／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／4.9／`⇒ 紅 []；rc 0`／✅ |
| `87` | 甲 | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | `0`／`0`／297.6／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／314.6／`⇒ 紅 []；rc 0`／✅ |
| `88` | 甲 | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／1.6／`⇒ 紅 []；rc 0`／✅ |
| `89` | 甲 | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | `0`／`0`／9.0／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／9.0／`⇒ 紅 []；rc 0`／✅ |
| `90` | 甲 | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | `0`／`0`／304.3／`⇒ 紅 []；rc 0`／✅ | `0`／`0`／293.0／`⇒ 紅 []；rc 0`／✅ |
| `91` | 丙 | `python3 verify/probes/probe_order_preflight.py --selftest` | `0`／`0`／1.8／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`／✅ | `0`／`0`／1.8／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`／✅ |
| `92` | 甲 | `python3 verify/probes/probe_WG9398_rw25.py selftest <repo>` | `1`／`0`／1.4／`⇒ 紅 ['受詞缺']；rc 1`／✅ | `0`／`0`／2.0／`⇒ 紅 []；rc 0`／✅ |
| `93` | 甲 | `python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf` | `1`／`0`／3.2／`⇒ 紅 ['X1', 'X3', 'X7', 'X8', 'X9']；rc 1`／✅ | `0`／`0`／3.9／`⇒ 紅 []；rc 0`／✅ |
| `94` | 甲 | `python3 tests/test_pool_slot.py` | `1`／`514`／0.6／`（空）`／✅ | `0`／`0`／0.6／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`／✅ |

合期：前置″ 94／94、驗 94／94；stderr 合計：前置″ 514 B（唯 #94）、驗 0 B；耗時之和：前置″ 13540 s、驗 13593 s（並行 2）。

### ③-3 驗 `V-1″`〜`V-9″`（於工項二″ `7c819b5`·推前）

| # | 期 | 實 |
|---|---|---|
| `V-1″` | (甲) `50` 呼叫皆 `rc 0`·末列 ＝ 施後；`F41 selftest` `T1`〜`T13`（含 `T2′`、`T7′`、`T9′`）與 `P0 16／16`、`F41 wiring` `X1`〜`X9` 皆 ✅ | 皆合（③-2）；`#92` 之 ✅ 列：`T1`、`T2`、`T2′`、`T3`〜`T7`、`T7′`、`T8`、`T9`、`T9′`、`T10`〜`T13`、`P0 判式自驗 16／16`；`#93`：`X1`、`X2`、`X3`、`X4`、`X5`、`X6`、`X7′`、`X8`、`X9` 皆 ✅·`⇒ 紅 []；rc 0` |
| `V-2″` | 其餘皆 `rc 0`·末列 ＝ 施後；`F23 selftest` `P0 75／75` | 皆合（③-2）；`#4`（`probe_WG9363_k953.py selftest`）出艙含 `✅ P0 逐項擾動恰該項紅 75／75` |
| `V-3″` | `Fy56` 之 `18` 檔之 blob ＝ 補令一 `§五″` 項 `5`；`verify/probes/`、`tests/` 對工項一″ 之端相異 `0` | `18／18`（`git hash-object` 與 bytes）；`git diff --stat 8bc2add 7c819b5 -- verify/probes tests` 空 |
| `V-4″` | `run` `rc 0`；`F36 diff` `rc 0` 而其全文 ＝ `§一″` 項 `5`；`cmp` ＝ 所載 | `run`（`#56`／`#57`）`rc 0`；`diff` 二退縮 `rc 0`（`stderr` `0` B）·全文見下（＝ `§一″` 項 `5` 逐字）；`cmp` 二退縮 `rc 1`·3.5 m：`宗 ('R1', '628-37(1)') G(㎡) 285.22 ≠ 285.21`／`相異 1 項 ⇒ 🔴 異`；0 m：`宗 ('R1', '628-35(2)') G(㎡) 730.82 ≠ 730.81`／`相異 1 項 ⇒ 🔴 異`（＝ 所載） |
| `V-5″` | `parity` `rc 0`·`⇒ rc 0（不符 0 項）`；落檔與 `stdout` 唯 `head` 異 | 二退縮 `rc 0`·末列 `⇒ rc 0（不符 0 項）`；以同一字樣（`<HEAD>`）代 `HEAD` 之全值後：落檔二退縮 `cmp` 逐位同、JSON 逐欄比 `相異 0 欄`；`stdout` 二退縮 `cmp` 逐位同。對照（⛔ 代之）：落檔 JSON 逐欄比唯 `/head` `"d3b6a7e…" → "7c819b5…"`（`相異 1 欄`）；`stdout` 唯首列之態之 sha 異 |
| `V-6″` | `run` `rc 0`·`⇒ 紅 []；rc 0`；`hash-object` 前後相異而施後 ＝ `4aca01db…`／`186b090b…`；JSON 逐欄之差 ＝ 所載 | `run`（`#58`／`#59`）合；3.5 m `13c04b456f98a3ea39c553e2ca6bd257a351e3b1` → `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`；0 m `f27849f58c08e7d60b6474b6b353e24dd6d7cd83` → `186b090b68836f0ece2c0d23dad5573941995bf5`；逐欄之差見下（3.5 m `3` 欄、0 m `7` 欄 ＝ 所載） |
| `V-7″` | 生產碼 `34` 檔相異恰 `2`；`stepg` 之差唯一列；AST ＝ `§三-2″` | `git diff --name-only 8bc2add 7c819b5 -- app.py verify/*.py` ＝ `app.py`、`verify/stepg_pipeline.py`；`app.py` `78`／`12`（blob `ca9f917e…`）；`stepg` `git diff -U0` ＝ `-` `1`／`+` `1`（`'W(m)': round(_res.get('W', 0.0), 2),` → `… 3),`·blob `c9d347c2…`）；AST 對 `f748370`：增 `['rw_pct_2dp', 'rw_width_mm']`·減 `[]`·相異 `['f3_screen_stepg_run', 'iterate_G_S', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'solve_G_binary']`；對 `20e03bf`：增 `['RW_TABLE_25', 'rw_pct_2dp', 'rw_width_mm']`·減 `[]`·相異 恰八（上七 ∪ `RW_TABLE_25`） |
| `V-8″` | 「rw_width_mm」≥ `4`；「rw_pct_2dp」≥ `3`；「jump398」≥ `1` | `10`、`5`、`5` |
| `V-9″` | 諸器之 `stderr` 合計 `0` B | 驗之 `94` 呼叫 `0` B；`V-4″` 之 `diff`／`cmp` 四呼叫 `0` B ⇒ `0` B |

`V-4″` 之 `F36 diff` 之全文（`python3 verify/probes/probe_WG9392_k980g.py diff <O>/pre/k6s3_pre_35.json <O>/post/k6s3_post_35.json`；同 `00`）：

```
  宗 R1·628-37(1)·right G(㎡) 285.22 → 285.21
  宗 R6·628-7(1)·right G(㎡) 1007.92 → 1007.91
  抵費地 R1-抵費地-1 面積 851.69 → 851.7
全比相異 3 項
```

```
  宗 R1·628-35(2)·left G(㎡) 730.82 → 730.81
  宗 R1·628-36(1)·right G(㎡) 662.11 → 662.1
  宗 R5·628-20(2)·left G(㎡) 534.48 → 534.49
  宗 R6·628-7(1)·right G(㎡) 1007.92 → 1007.91
  抵費地 R1-抵費地-1 面積 851.69 → 851.7
  抵費地 R3-抵費地 面積 1651.39 → 1651.4
  抵費地 R5-抵費地 面積 1221.46 → 1221.45
全比相異 7 項
```

`V-6″` 之 JSON 逐欄比（倉外之器 `<O>/tools/jdiff.py`：讀二檔、遞迴比其鍵與值·列「路徑 前值 → 後值」）：

```
/dropped/R6/right[0]/G(㎡)	0.26 → 0.25
/rows[3]/G(㎡)	285.22 → 285.21
/rows[13]/G(㎡)	1007.92 → 1007.91
相異 3 欄
```

```
/dropped/R3/right[1]/G(㎡)	24.89 → 24.88
/dropped/R3/right[2]/G(㎡)	130.42 → 130.41
/dropped/R6/right[0]/G(㎡)	0.26 → 0.25
/rows[1]/G(㎡)	730.82 → 730.81
/rows[3]/G(㎡)	662.11 → 662.1
/rows[13]/G(㎡)	1007.92 → 1007.91
/rows[16]/G(㎡)	534.48 → 534.49
相異 7 欄
```

**本案之配地之改變 ＝ 補令一 `§一″` 項 `5`（＝ 請示表戊欄）**：3.5 m `3` 項、0 m `7` 項，多一項、少一項、值異者皆無。

## ④ 塊之實得與三檔之改前改後

| 塊 | bytes | `sha256` | 列 |
|---|---|---|---|
| `Fy56`（補令一·重抽·⛔ 重施） | `49904` | `89d49c8bb35766a4dbc4e1ec551aa42fcf8cce4c091ba66cc485e3eebb1ed19e` | `695` |
| `K47`（補令一） | `15535` | `cc11da141ae2f4619065c30d5852c014be20cbf5b8b5d5f3255ae569be48b8e3` | `81` |
| `E44`（補令一） | `3868` | `e46c6b16946f38054090aca16485bea736422fa6610e10302ccc4b8b51deb3c7` | `22` |
| `P58`（補令一） | `3018` | `302bad900125548f1fb28c97667647bfb8c3846d3eb4b35b7711282b51d6abd5` | `16` |
| `E45`（補令二） | `2371` | `0fcf0358be5e9298e4926996e4f6ad5eaf665afb34181286a1ecda6c6c21bd10` | `13` |
| `CK`（`W-G.9-365_輕量單.md` 附錄午） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` |
| `GF`（同·附錄巳） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` |

| 檔 | 改前 B | 改後 B | 改後 blob | 尾 |
|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `1009547` | `1025082` | `78a2cdee2224c1bb2ac24fe7d7afb375345c770f` | `K47` |
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1242762` | `1249001` | `98815489490f87a32c1989dbf8e706d74c34f7dc` | `E44` ＋ `E45`（依序） |
| `docs/待落地清單.md` | `46263` | `49281` | `cd213761710396c688fcbb306f4bedc0b173f708` | `P58` |

三檔皆以「改前全檔 ＋ 塊」之二進位之接合寫之（改前為改後之嚴格前綴·刪除欄 `0`）。

## ⑤ 推送之目標與推後之遠端分支之列

母體之式：`git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`。開工 `56` 列（`<O>/heads_before_398p2.txt`）。工項零‴、二″、三″ 之推後皆 `56` 列；工項三″ 之推後與開工之差唯二列：`refs/heads/ops/queue`（本輪之接單與進度列）與 `refs/heads/verify/W-G.9-398-rw25`（`8bc2add` → `c112df1`）；主線 `wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`（⛔ 變）。工項四″ 之推後之值見回報（收工閘 `5″`）。

## ⑥ 自捕與自解；唯讀獨立審查之發現與處置

### ⑥-1 執行端之自捕與自解

1. **通則「Bash 命令⛔ 含 heredoc」之違（一次·無作用）**：撰碼中定位 `iterate_G_S` 之回傳列之一 Bash 呼叫，誤附一空之 heredoc（`python3 - <<'X' … X`·其體為空·`|| true`）；其無任何作用（未讀寫任何檔）。其後一律以檔案寫入之工具與 `printf` 為之。
2. **`commit` 之作者**：工項零‴ 首以全域之 `Claude` 為作者 `commit`（`96f80ad`·**未推**），察與前輪之 `Claude (執行端)` 不一 ⇒ 設施工樹之 `user.name` 後以 `--amend --reset-author` 成 `d3b6a7e` 而推（`96f80ad` 從未推送·遠端之史無之）。
3. **撰碼之樹**：前置″ 須於工項零‴ 之端跑而撰碼並行 ⇒ 以 `git worktree add --detach /tmp/w2 d3b6a7e` 撰之（倉外·⛔ 入倉），前置″ 之 `94` 呼叫畢後於 `/tmp/w2` `commit`（`7c819b5`），施工樹 `/tmp/w` 再 `checkout --detach` 至之而跑驗。
4. **撰碼中之自跑**（⛔ 為驗）：於 `/tmp/w2`（未 `commit` 之碼）序跑 `F41 selftest`／`wiring`、`tests/test_pool_slot.py` 與 `wiring` 之 `16` 器、`probe_WG9352_endblock.py selftest`（共 `20` 呼叫·皆合施後之期）。其中 `17` 呼叫與前置″ 之長跑（並行 `2`）同時（瞬時之並行至 `3`）；前置″ 之一切呼叫皆合期·⛔ 逾時。
5. 前置″ 與驗之 `94` 呼叫以倉外之器 `<O>/tools/runner.py` 起之（`setsid nohup`·並行 `2`·逐呼叫落檔）；其命令 ＝ 原單 `§五-1` 項 `8` 之表之命令逐字（自單之文以程式抽出·`<repo>` ＝ `/tmp/w`·`<O>/…_<態>` ＝ `<O>/pre/…_pre`／`<O>/post/…_post`）；其期 ＝ 補令一 `§五″` 項 `8`（程式抽出）。

### ⑥-2 唯讀獨立審查（一 reviewer·⛔ 改檔、⛔ `commit`·其實跑於其自建之 `/tmp/R/`）

**R-1″〜R-7″、專審 ①〜⑤、`§三-3″`：皆合**（擋者 `0`）。其要：

- ① `rw_width_mm`：用語之例 `6.0745 ⇒ 6.075`（二進位 `round` `6.074`）、`7.1975 ⇒ 7.198`（`7.197`）、`5.3004 ⇒ 5.3`、`17.9995 ⇒ 18.0`；合成之 `x.xxx5` `30` 值（含二進位表示略小於字面者 `15` 值·`round(x,3)` 於其上全錯）不符 `0`；隨機 `20` 萬值不符 `0`；`rw_pct_2dp(22.214999999999996) ＝ 22.22`；`rw_increment` `40` 萬組與「`Decimal` 精確表之內插之差再四捨五入」不符 `0`；冪等（`round(·,3)`、`round(·,2)` 施於新值無二次偏移）。
- ② 跳處（審查者自撰·`40 × 20` 矩形·`W ＝ S`）：例一（跳 `6.074｜6.075`·`1／4`）⇒ `jump398 '進'`·`converged` 真·`W 6.075`·所取之 `diff` `+0.02905`；例一b（`3／4`）⇒ `'捨'`·`W 6.074`；例二（`A .3`、`B .4`、`C .1`、`l_front 8`·跳 `9.999｜10.000`）⇒ `'進'`／`'捨'`；例三（跳 `1.000｜1.001`）⇒ `'進'`；**等距**（替身逼二試點之 `diff` 恰 `−0.5`／`+0.5`）⇒ `'進'`·`converged` 真·`W 6.075`。未收斂而非跳處（四例·新舊二版注入同一 `rw_increment` 並跑）⇒ 皆 `converged` 偽、`jump398 None`，`S`、`S_raw`、`G`、`area_geom`、`W_far_raw`、`Rw_raw`、`cut_coords`、`iterations`、`trace` 全同（唯 `W`／`W_far`／`W_near`／`Rw_pct` 之取位異）。
- ③ 讀 `W_far` 之處：`app.py` `11383`、`11388`、`22435`、`22598`；`verify/stepg_pipeline.py` `952`、`1101`、`1512`——字樣逐字未改；`'W_far'` 之生產者唯 `iterate_G_S`（`6971`）、`solve_G_binary`（`12438`）而皆經 `rw_width_mm` ⇒ 起算 ＝ 公釐值。
- ④ `R-7″` 之二段之字以程式自單抽出而比 ⇒ 逐字合；`main` 之差唯 `−2`／`+3`。
- ⑤ `round` 之施於 `W`／`Rw` 者 `63` 列逐一歸類：豁免者（`trace`、`'W_rw_start'`、ΣRw 之檢核表）、顯示／診斷／閘、非側街寬之量——入於配地之計算而⛔ 經 `rw_width_mm` 者 **`0`**。
- `§三-3″`：簽名同；回傳之鍵唯增 `'jump398'`；`solve_G_binary` 之迴圈之舊 `13` 句為新 `14` 句之有序子序列（增唯記錄試點之一句）；`Rw = rw_increment(_rw_start, W)` 仍在其內；逐宗之檢查、`GB-206`、推進之串接⛔ 動。

**發現與處置**（⛔ 自改規格·⛔ 裁）：

| # | 發現（審查者之分類） | 執行端之處置 |
|---|---|---|
| `F-1` | 跳處之判⛔ 有「區間之寬」之守門：以 `max_iter 4`、`tol 0.01` 實跑，二試點 `S 9.375`／`11.25` 即判為跳處（`'捨'`·`converged` 真·所取之 `|diff|` 約 `70 ㎡`）；碼與規格之字面一致；審查者標「涉域上判斷／規格之漏載」，並陳：生產碼之唯一之呼叫處（`app.py:20030`·`tol ＝ K980_G_TOL`〔`1e-6`〕、`max_iter ＝ K980_G_MAX_ITER`〔`200`〕）於區間 ＜ `1e-9 m` 即止，實務上不可達 | **⛔ 停機**（停機款 `12″` ⛔ 成就之由）：本補令之行為（`R-4″` ②）之字面已定此形，碼合之；生產碼中 `solve_G_binary` 之呼叫唯一處（`grep -n "solve_G_binary("`·`app.py:20030`）之二分必止於區間 ＜ `1e-9 m`，其二試點之公釐值相異必含一公釐之界 ⇒ 本案與一切現行之路徑⛔ 生土地之果；其與補令一 `§一″` 項 `7` 所記而⛔ 改之「跳處之判之加強」同族 ⇒ **呈發單端**（次單之併辦與否由發單端定之） |
| `F-2` | 負值之取位遠離 `0`（`rw_width_mm(−6.0745) ＝ −6.075`；`rw_pct_2dp(−0.005) ＝ −0.01`）·`ROUND_HALF_UP` 之 `Decimal` 之語義；唯及於可為負之 `'W_near'` 之顯示與 `W₀` 之閘·`R(W ≤ 0) ＝ 0` ⇒ ⛔ 及配地 | 規格之用語明定「四捨五入（`ROUND_HALF_UP`）」；⛔ 生土地之果 ⇒ ⛔ 停機·**呈發單端**記之 |
| `F-3` | `'jump398'` 未曝於分配計算表（收斂之欄唯讀 `converged`） | 規格⛔ 要求；`main` 唯許 `R-7″` 之三處、`f3_screen_stepg_run` 唯許 `R-6″` 之一列 ⇒ ⛔ 改·呈發單端 |
| `F-4` | `_solve_G_one` 以 `except Exception` 包 `solve_G_binary`，新之 `ValueError`（非有限之 `W`）於某宗或被吞而改走 `iterate_G_S`（其仍於 `rw_width_mm` 處拋出） | 既有之結構（`_solve_G_one` 為本補令之 🛑）⇒ ⛔ 改·呈發單端 |
| `F-5` | `rw_width_mm("6.0745")` 可過、`rw_width_mm(None)` 拋 `TypeError` | 規格唯要求非有限值 ⇒ `ValueError`；⛔ 改 |
| `F-6` | 等距（`§三-4″` 之已知之形）：審查者以替身逼之 ⇒ 取「進」合 `R-4″` ②；合成之大跳之 `|diff|` 約 `0.029 ㎡`（＞ `0.015`）——實案之大跳須以全管線驗 | 本案之全管線（`V-4″`〜`V-6″`）＝ 戊欄、逐宗之檢查⛔ 觸；記於此（`§三-4″`） |

審查者之副作用（自陳）：其 `py_compile` 於 `/tmp/w` 生 `__pycache__/app.cpython-311.pyc` 與 `verify/__pycache__/stepg_pipeline.cpython-311.pyc`（皆為 `.gitignore:18:__pycache__/` 所涵·`git status --porcelain` 空）。

## ⑦ 設計說明（補令一 `§三-5″`）

- **`R-1″`**：`app.py:6154` `def rw_width_mm(W: float) -> float`（`RW_TABLE_25` 之後、`rw_width_mm`、`rw_pct_2dp`、`rw_from_width` 之序）。式：`W = float(W)`；`math.isfinite` 偽 ⇒ `ValueError`；`float(Decimal(repr(W)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))`（`decimal` 於函式內匯入·`math` 為模組級）。docstring 載 KL `2026-10-27 23:29`「採戊」·`W-G.9-398` 補令一·「全檔之取至公釐唯經本函式」。實跑（`<O>/tools/examples.py`·以 AST 抽其二函式）：`rw_width_mm(6.0745) ＝ 6.075`（二進位 `round(x, 3)` ＝ `6.074`）；`(7.1975) ＝ 7.198`（`7.197`）；`(5.3004) ＝ 5.3`；`(17.9995) ＝ 18.0`；`rw_pct_2dp(22.214999999999996) ＝ 22.22`；`nan`、`inf`、`-inf` ⇒ `ValueError`。
- **`R-2″`**：`app.py:6171` `def rw_pct_2dp(x: float) -> float`：非有限 ⇒ `ValueError`；`float(Decimal(repr(round(x, 6))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))`；docstring 載附帶告知 `2`·KL `10:48` 未異議。
- **`R-3″`**：`rw_from_width`：`W = float(W or 0.0)` → `math.isnan` ⇒ `ValueError` → `W ≤ 0` ⇒ `0.0`、`W ≥ RW_SATURATION_WIDTH_M` ⇒ `100.0` → `W = rw_width_mm(W)` → 再判 `≤ 0`／`≥ 18` → 原 ③④（逐列未動）。docstring 增「🔧 W-G.9-398 補令一」之段。函式內⛔ 增數之常數。
- **`R-4″`**：`solve_G_binary`：迴圈前 `_neg398 = None; _pos398 = None`；迴圈內於 `last_W …` 之後增 `if diff < 0: _neg398 = (S_guess, G_target, W, Rw_pct, area_geom, diff)`／`elif diff > 0: _pos398 = (…)`（既有之句⛔ 改、⛔ 移）。迴圈後、既有之「未收斂 ⇒ 中點」之段之後：`not converged` 且二者皆存且 `rw_width_mm(_neg398[2]) != rw_width_mm(_pos398[2])` ⇒ `_pick398 = _neg398 if abs(_neg398[5]) < abs(_pos398[5]) else _pos398`（**等距之判 ＝ 浮點之相等 ⇒ 落 `else` ⇒ 取 `diff ＞ 0` 之一〔進〕**）；`S_conv, G_conv, W_conv, Rw_conv, area_conv = _pick398[:5]`；`converged = True`；`_jump398 = '捨'／'進'`。其後之實切（`_S_cut = S_conv`）與 `area_conv` 之取實切面積照舊。回傳：`'W'`、`'W_far'` ＝ `rw_width_mm(W_conv)`、`'W_near'` ＝ `rw_width_mm(_W_near_out)`、`'Rw_pct'` ＝ `rw_pct_2dp(Rw_conv)`、增 `'jump398': _jump398`；`'W_far_raw'`、`'Rw_raw'`、`'W_rw_start'`、`'W_rw_start_raw'` 之值照舊、其註改述（「公釐值」「顯示值」）；docstring 之回傳之列增 `'jump398'` 並增「🔧 W-G.9-398 補令一」之段。「最末之試點」＝ 區間之二端之由：`S_min` 唯於 `diff ＜ 0` 時更新、`S_max` 唯於 `diff ＞ 0` 時更新（`diff ＝ 0` 必已收斂）。
- **`R-5″`**：`iterate_G_S`：早返之 `'W': rw_width_mm(W_prev)`（`'Rw_pct': 0.0` 照舊）；終返之 `'W'`、`'W_far'` ＝ `rw_width_mm(W_cur)`、`'Rw_pct'` ＝ `rw_pct_2dp(Rw_pct)`；`trace` 照舊。
- **`R-6″`**：`app.py:21806`（`f3_screen_stepg_run`）、`verify/stepg_pipeline.py:531`（`_run_step_g_impl`）之 `'W(m)': round(_res.get('W', 0.0), 3),`（各唯此一列）。
- **`R-7″`**：`main`：① `'F(m)': '{:.2f}', 'W(m)': '{:.3f}', 'Rw(%)': '{:.2f}',`（同列他欄⛔ 動）；② `- **Rw（%）**：依手冊附表 25（街角地側面道路負擔百分率累積表·每 0.1 m 一格·公分以下內插·W ≥ 18 m 為 100）；W 先四捨五入至公釐。`；③ `st.dataframe(_df_g[_display_cols].style.format(_fmt), …)` 之後緊接 `st.caption("註：W(m) 記至公釐；累積百分率（附表 25 內插）不取位，各宗之 Rw(%) ＝ 本宗與前一宗（首宗為起算點）之累積百分率相減後四捨五入至小數二位。")`。`main` 之刪列恰 ①② 之二列。
- **`rw_from_width`、`rw_width_mm`、`rw_pct_2dp` 之一切呼叫處**（`grep -n "rw_from_width\|rw_width_mm\|rw_pct_2dp" app.py verify/*.py`·去註列·除定義、docstring、`raise` 之字串）：`app.py:6205`（`rw_from_width` 內）、`6240`（`rw_increment`）、`6920`、`6971`（`iterate_G_S`）、`8391`（`_select_pool_slot` 之 `rw_func` 之預設）、`12378`、`12438`、`12439`、`12447`（`solve_G_binary`）、`20495`（harvest 之名之列）、`30334`（`main` 之 ΣRw 之檢核）；`verify/app_harvest.py:160`（名之列）；`verify/stepg_pipeline.py:421`（`ns["rw_from_width"]`）、`1504`、`1506`、`1643`、`1677`（結構閘之 telescoping）。
- **推進之串接之讀 `W_far` 之處（⛔ 改）**：`app.py:11383`、`11388`、`22435`、`22598`；`verify/stepg_pipeline.py:952`、`1101`、`1512` ⇒ 其值 ＝ `solve_G_binary`／`iterate_G_S` 之回傳之 `'W_far'` ＝ 公釐值 ⇒ 次宗之起算 ＝ 前宗遠側寬度之公釐值。
- **`§三-3″` 之自查**：1 字樣之錨（`F23`／`F24 wiring` ＝ `#5`／`#6`）二態皆綠；2 迴圈之既有之句⛔ 改、⛔ 移；3 `main` 唯三處（`F30 wiring` `W7` 綠）；4 頂層恰 `§三-2″`（`V-7″`）·`verify/` 頂層唯 `stepg_pipeline.py` 之一列（`X7′` ✅）；5 ⛔ 案件字面（`X6` ✅）；6 簽名、回傳之形（增唯 `'jump398'`）、推進之串接、逐宗之檢查、`GB-206` ⛔ 動。

## ⑧ 全文差異

同目錄之 `W-G.9-398R1_寬度取至公釐與跳處_差異.diff` ＝ `git diff f748370 7c819b53038f14109693ce8c572a029f361e97e7 -- app.py verify/stepg_pipeline.py`（`13554` B·與以 `8bc2add` 為前端者逐位同）。

## ⑨ 工項三″ 之 `checkidx`、`gen_fa_index`

- `python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md` ⇒ `rc 0`；`則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` `cmp` 逐位同。

## ⑩ 各段耗時（UTC·並行之數）

| 段 | 起訖 | 並行 |
|---|---|---|
| 接單 → 開場之核對 → 工項零‴ 之推 | `07:53`〜`07:58` | `1` |
| 前置″ `94` 呼叫 | `07:59:12`〜`09:52:0x`（耗時之和 `13540` s） | `2`（撰碼中之自跑與之重疊約 `11` min） |
| 撰碼（`/tmp/w2`） | `08:00`〜`08:10` | — |
| 驗 `94` 呼叫 | `09:52:26`〜`11:45:42`（耗時之和 `13593` s） | `2` |
| `V-4″`〜`V-8″` 之餘 | `11:46`〜`11:50` | `1` |
| 唯讀獨立審查 | `11:50`〜`12:01`（約 `628` s） | `1` |
| 工項二″、三″ 之推、工項四″ | `12:02`〜 | `1` |
