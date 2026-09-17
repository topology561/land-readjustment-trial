# `W-G.9-307`　交接註（**舊窗收工**）

> 本註之每列同格載其**產生指令**；逐項**自跑當場重得**（⛔ 轉引補令之數）。
> 🛑 本註**⛔ 載任何判**。

---

## `1`　主線 ref

**產生指令** ＝ `git ls-remote origin refs/heads/wip/s1-endpart`（**`push` 前之值**）

```
e2d26b1ac6c15391d6dc4001811184754d6f6d52	refs/heads/wip/s1-endpart
```

---

## `2`　`app.py` 之 blob

**產生指令** ＝ `git rev-parse HEAD:app.py`

```
4379108a4856714078c410ff4e6291ecfdf6d2c1
```

---

## `3`　凍存 `p3a` 之祖先關係

**產生指令** ＝ `git cat-file -t 05a11bd665f6c2790ff821c9e3a1606651e345d4` ⇒ `git merge-base --is-ancestor 05a11bd665f6c2790ff821c9e3a1606651e345d4 HEAD`

```
cat-file -t  ⇒ rc = 0（commit）
is-ancestor  ⇒ rc = 1
```

---

## `4`　四簿（**器之輸出**·含缺號）

**產生指令** ＝ `python verify/probes/probe_WG9267_issuer_measurers.py registry`（`rc = 0`）

```
自誤 : {'相異': 406, 'MAX': 416, 'MIN': 7, '缺號': [106, 355, 356, 357]}
GB   : {'相異': 168, 'MAX': 170, 'MIN': 1, '缺號': [12, 87]}
VR   : {'相異': 80,  'MAX': 95,  'MIN': 14, '缺號': [73, 75]}
K-9  : {'相異': 29,  'MAX': 30,  'MIN': 2,  '缺號': []}
```

---

## `5`　生產碼母體（**正面列舉**）

**產生指令** ＝ `git ls-tree HEAD --name-only -z verify/` ⋂ `*.py` ＋ `app.py`　⇒ **`34`** 檔

```
app.py
verify/app_harvest.py                     verify/b6_isomorphism.py
verify/fixture_baseline_candidates.py     verify/fixture_block_depth_n19p.py
verify/fixture_cad_binding_order.py       verify/fixture_corner_range_k8.py
verify/fixture_e2e_termination.py         verify/fixture_end_fallback.py
verify/fixture_end_reserve.py             verify/fixture_end_winner.py
verify/fixture_g3_static_guards.py        verify/fixture_klui_t2diag.py
verify/fixture_midlayer_6items.py         verify/fixture_n14_feed_chain.py
verify/fixture_n14_min_width.py           verify/fixture_wf_ns_wiring.py
verify/fixture_yi_construction.py         verify/run_all.py
verify/run_verification.py                verify/selection_pipeline.py
verify/stepg_pipeline.py                  verify/test_corner_first_lot_G.py
verify/wd3_fragment_geom.py               verify/wd4_tier_list.py
verify/wf_f0.py                           verify/wf_f1.py
verify/wf_f2.py                           verify/wf_f3.py
verify/wf_f4.py                           verify/wg_g1_smoke.py
verify/wg_g2_smoke.py                     verify/wg_g3.py
verify/wv_reconcile.py
```

**產生指令** ＝ `git ls-tree -r HEAD --name-only -z verify/` ⋂ `*.py` ∖ 頂層　⇒ 子層 `*.py` ＝ **`327`** 檔
（須 `> 0`·**⛔ 定值**：`W-G.9-305R` 時 `322`／`W-G.9-306R` 時 `324`／`W-G.9-307R` 開工時 `325`）

---

## `6`　`verify/baselines`

**產生指令** ＝ `git ls-tree -r HEAD verify/baselines | sha256sum`；`… --name-only | wc -l`

```
sha256 ＝ a898f4e1bba8f8d230a9e279044f529175beb9186915aed1fa5590c1878a7ec9
檔數   ＝ 298
```

---

## `7`　`refs/heads/verify/*`

**產生指令** ＝ `git ls-remote origin 'refs/heads/verify/*'`

```
該族                     ＝ 20 支
W-G.9-299-gb170 命中     ＝ 0
W-G.9-269-p3a   命中     ＝ 1
```

---

## `8`　`§一` 之態與其框之**全量輸出**

**框甲** ＝ `git log --format='%H %s' e2d26b1ac6c15391d6dc4001811184754d6f6d52..HEAD`

- **收單時**（`HEAD` ＝ `e2d26b1ac6c15391d6dc4001811184754d6f6d52`）之全量輸出 ＝ **（空）**
- **現時**（本補令入倉後）之全量輸出 ＝ **`1`** 列：

```
1d519572765e0acd774123534325745876bddabb W-G.9-307 補令一：本補令原封入倉（docs/orders/·⛔ 改一字·作業常規追加四 款一）⛔ 零生產碼
```

**框乙** ＝ `git ls-tree -r --name-only -z HEAD docs/orders/` ⋂ 檔名前綴 `W-G.9-308`（**取 bytes**）

```
命中 ＝ 0（空）
```

**併查**（補令 `§一` 末段所令）：`docs/orders/` 內檔名含 `K-9-30依據之更正` 之 `W-G.9-308` ⇒ **命中 `0`（無）**

**態之記述（⛔ 判）**
- 依框甲於**收單時**之全量輸出（空）＋ 框乙（空）⇒ **態甲**之條件於收單時成立。
- 依框甲於**現時**之全量輸出（`1` 列）⇒ 其唯一列係**本補令自身之入倉 `commit`**；
  框乙仍為空，且 `W-G.9-308` 之工項 `commit` 與檔案**皆 `0`**。
- 🔒 **本窗未辦 `W-G.9-308` 之任何工項**（已辦者 ＝ `W-G.9-307` 之十 `commit`·見項 `9`；未辦者 ＝ `W-G.9-308` 之全部）。

---

## `9`　`W-G.9-307` 之全部 `commit`（全 `40` 碼·題逐字）

**產生指令** ＝ `git log --format='%H %s' da9ca62eb2d007d13c08eaa9a066031228932e8a..HEAD`　⇒ **`10`** 列

```
247b1a1d22b80655edf6b9376d7833d4ecef0b9b W-G.9-307 §二 工項零：本單原封入倉（docs/orders/·⛔ 改一字）⛔ 零生產碼
a22b5870cd7bc273809ff204d4414bf1f6271acb W-G.9-307 §三 段一：自誤 416 之鑄（檔末追加·嚴格 append-only）⛔ 零生產碼
78a97155bc0b121b58ce4cb35ffa3a9a3ff45af6 W-G.9-307 §三 段二：坑 bp 之鑄（檔末追加·嚴格 append-only）⛔ 零生產碼
cdbee6cf94f2c3e80e8f5a8351cbc7fa3677b8c9 W-G.9-307 §三 段三：ALPHA_LABELS 擴至 bp（僅新增一列·⛔ 改既有列一字）⛔ 零生產碼
c4a8a95f31203884fa64d82433c06ca4ab883d14 W-G.9-307 §四 工項二：GB-170 之末端追加（KL 放行射程之釐清·⛔ 鑄號·⛔ 解除·⛔ 收窄）⛔ 零生產碼
56da144a5a29ac9713012ac7be3dc76eee7a7bc0 W-G.9-307 §五 工項三：七處之在域現查（AST 為框·靜態·量測器與落檔）⛔ 零生產碼
0340e096f194a3d6f981c17381faebf170d98dee W-G.9-307 §六 工項四：改前之釘紅與逐宗基線（landeffect 全檔逐位相同·逐宗基線 115 筆·款 3 全量 21 次）⛔ 零生產碼
9bce9e3b4195e85357f7b7c8c1e977144ff96091 W-G.9-307R 執行報告入倉（工項零／開工閘十四項／工項一／工項二／工項三／工項四）⛔ 零生產碼
e2d26b1ac6c15391d6dc4001811184754d6f6d52 W-G.9-307R §七〜§九 收工閘之實測（報告入倉後量·嚴格末端追加·含逐款回掃與標籤對照）⛔ 零生產碼
1d519572765e0acd774123534325745876bddabb W-G.9-307 補令一：本補令原封入倉（docs/orders/·⛔ 改一字·作業常規追加四 款一）⛔ 零生產碼
```

**本批（補令一）之報告** ＝ `docs/reports/W-G.9-307R2_補令一_舊窗收工_執行報告.md`（於本註入倉後另行入倉）。
**`W-G.9-307` 之執行報告** ＝ `docs/reports/W-G.9-307R_自誤416坑bp與七處在域現查_執行報告.md`。

---

## `10`　本窗之環境事實（逐項具名其出處·**⛔ 判**）

| # | 事實 | 出處 |
|---|---|---|
| `a` | `sys.version` ＝ `3.13.11 \| packaged by Anaconda, Inc. \| (main, Dec 10 2025, 21:21:58) [MSC v.1929 64 bit (AMD64)]` | 本註撰寫時當場跑 `python -c "import sys; print(sys.version)"`；併見 `W-G.9-306R §一` 閘 `0`、`W-G.9-307R §一` 閘 `0` |
| `b` | `git config core.autocrlf` **三層分列**：`--system` `rc=0` `'true'`／`--global` `rc=1` `''`（**未設**）／`--local` `rc=0` `'false'` ⇒ **有效值 `false`** | 本註撰寫時當場跑 `git config <scope> --get core.autocrlf`；併見 `CLAUDE.md` 之「`core.autocrlf` 之**記述更正**」節 |
| `c` | **子程序 `stdout` 之換行轉譯**：以 `subprocess` 捕獲**未設** `reconfigure(newline="\n")` 之 Python 器，其 `stdout` 於本機帶 `CRLF`。實測 `probe_WG9287_landeffect.py` ⇒ 原捕獲 `86404` B／`CR` `692`；施 `b"\r\n"→b"\n"` 後 `85712` B／`CR` `0`（差 `692` ＝ `CR` 數） | `W-G.9-307R §六` 款 `1` |
| `d` | **`ast` 之 `col_offset`／`end_col_offset` 係 UTF-8 <u>位元組</u>偏移**（⛔ 字元）⇒ 自建之原始碼切片須**先 `encode` 再切**（同 `ast.get_source_segment` 之作法） | `W-G.9-307R §五`；其 `seg` 之自我驗證閘（vs `ast.get_source_segment`·抽樣）⇒ 相同 `837`／相異 `0` |
| `e` | **`id(·)` 作快取鍵之失效**：CPython 於原物件被回收後**重用同一 `id`** ⇒ 以 `id(src)` 為鍵之列快取取到**他檔之列**；其捕獲者為該器之自我驗證閘（由 `837`／`0` 轉紅） | `W-G.9-307R §八-1` 自捕 `2` |
| `f` | **`bash` 之雙引號內反引號仍行命令替換** ⇒ 其所夾之檔案路徑會被**當作腳本逐列執行**（文件內之 `>` 成重導向、行首指令名真被呼叫）；且該命令經 harness 逾時移入背景後**持續執行** | `W-G.9-306R §八`／`§九` |
| `g` | **各器之牆鐘**（本機）：`probe_WG9269_pit_index.py` 約 `5`–`8` 分；`probe_WG9307R_prepin.py`（含 `run_verification` 全量一次）`202.3` 秒；`probe_WG9307R_sites.py` `22.4` 秒；`probe_WG9287_landeffect.py` `51.7` 秒；`probe_WG9306R_reach.py`（含 `run_verification`）`901.9` 秒 | 各該批之報告 |
| `h` | **repo hook `wg9237_heredoc_guard`**（`.claude/settings.json` 之 `PreToolUse`·`matcher` ＝ `Bash`）擋含 heredoc 之 Bash 命令；其所揭之解 ＝ 「以 `Write` 落檔，再以**路徑**呼叫」 | 本窗實遇（`W-G.9-306R` 撰寫期） |

---

## `11`　本窗工作區內未入倉之物

**產生指令** ＝ `git status --porcelain --ignored -z`　⇒ 條目數 ＝ **`20`**

```
!! verify/__pycache__/
!! verify/out/got_G值_退縮0m.csv
!! verify/out/got_G值_退縮3.5m.csv
!! verify/out/got_W-D.4_清單_退縮0m.csv
!! verify/out/got_W-D.4_清單_退縮3.5m.csv
!! verify/out/got_W-D.4_跨占_退縮0m.csv
!! verify/out/got_W-D.4_跨占_退縮3.5m.csv
!! verify/out/got_W-D.4_遞補_退縮0m.csv
!! verify/out/got_W-D.4_遞補_退縮3.5m.csv
!! verify/out/got_抵費地_退縮0m.csv
!! verify/out/got_抵費地_退縮3.5m.csv
!! verify/out/got_指配_退縮0m.csv
!! verify/out/got_指配_退縮3.5m.csv
!! verify/out/got_滑池槽診斷_退縮0m.csv
!! verify/out/got_滑池槽診斷_退縮3.5m.csv
!! verify/out/got_診斷_退縮0m.csv
!! verify/out/got_診斷_退縮3.5m.csv
!! verify/out/got_逐槽J表_退縮0m.csv
!! verify/out/got_逐槽J表_退縮3.5m.csv
!! verify/probes/__pycache__/
```

**逐項具名其生成之批**
- `verify/out/got_*.csv`（**`18`** 檔）＝ `W-G.9-307R §六` 之 `run_verification` 全量一次所寫
  （`_dump_csv` 逐張傾印；其 `got_G值_退縮<tag>.csv` 即該報告款 `2` 之受詞來源）。
  🔒 其族係 `.gitignore` **刻意忽略**者（`CLAUDE.md`：`verify/out/got_*` ⛔ 列為缺失）。
- `verify/__pycache__/`／`verify/probes/__pycache__/` ＝ 本窗各次 `python -m py_compile` 與器之執行所生。
- 🛑 **⛔ 刪、⛔ 入倉**（補令 `§二` 項 `11` 明文）。

---

## `12`　本窗於**倉外**所為之寫入

| # | 路徑 | 要旨 |
|---|---|---|
| `a` | `C:/Users/admin/.claude/projects/C--Users-admin-Desktop-land-readjustment-trial/memory/MEMORY.md` | 其 `wg9143-handoff-entry` 之**索引列**於 `W-G.9-306R`／`W-G.9-307R` 收工後各更新一次（主線 `commit`、四簿、末標籤、要旨）。**列數維持 `16`**·索引列唯一。 |
| `b` | 同上目錄之 `wg9143-handoff-entry.md` | `W-G.9-306R`／`W-G.9-307R` 之收工態各**末端追加**一節（嚴格前綴機驗 ＝ `True`）。 |
| `c` | 同上目錄之 `grep-multibyte-charclass-trap.md` | 追加二節：`bash` 雙引號內反引號之命令替換（`W-G.9-306R`）；`id()` 之重用與表列解析之靜默漏列（`W-G.9-307R`）。 |
| `d` | `…/scratchpad/`（本 session 之暫存目錄） | 本窗各次之抽取器、對拍器、追加器與其中間輸出（`wg9306_*`／`wg9307*_*`）。**⛔ 入倉**。 |

🔒 上列 `a`〜`c` 係**受單側自身之記憶檔**（倉外）；`d` 係 session 暫存。**⛔ 倉內物件。**

---

## `13`　本窗自捕之全部

### `13-甲`　`W-G.9-306R` 所載（`3` 則）

| # | 形 | 徵候 | 根因 | 攔法 |
|---|---|---|---|---|
| `1` | 閘 `6'` 之捕獲器**只留末 `12` 列** | 該閘所繫之二數（合計 `93`／`93`、末標籤 `bo`）未落入任何可出艙之載體 ⇒ **量測已跑而結果滅失** | 捕獲之切片寫成 `print` 之 `[-12:]`；恆常附款之「⛔ `\| tail -N`」之重踩 | 重跑並改 **`rev` 釘死** ＋ **全量落檔**（`open(p,'wb')`）；釘死使其母體固定為該 `commit` 之樹 ⇒ 其後之 `commit` **結構上⛔ 能污染之** |
| `2` | 報告撰寫之**臨時**解析式漏一列（`rows[2:]` 跳表頭） | 得「強制呼叫總數 `20`」而器自印為 `21` | 以固定切片跳表頭，而該表之表頭與分隔列數與假設不符 | **同格有器之自印值可對** ⇒ 二數不符當場暴露；改以逐列判後得 `21`／相異 entry `15`，與器自印逐項相符 |
| `3` | `bash` **雙引號**內反引號行**命令替換**，把 `.md` 當腳本執行 | `stderr` 出現「以**文件名**為前綴之 `line N: … command not found`」；工作區生出以文件內文為名之 `0` B 雜散檔（全程至少 `7` 個相異名）；該命令經 harness 逾時移入背景後**持續執行**（刪後 `15`–`25` 秒復現；`TaskStop` 之成功回覆後 `ps -ef` 仍見其行程） | `python -c "…"` 之碼內以反引號作 markdown 標記，而 `bash` 之雙引號**⛔ 抑制**反引號 | ① 凡碼含反引號者**落檔後以路徑呼叫**；② 見該徵候一律當作「該文件已被執行」並**逐項實測傷害面**；③ 清除副作用後**間隔再掃一次**；④ **⛔ 以任務之停止回覆充行程已死**，須 `ps` 實查。**傷害面重驗 ＝ 倉內零異動** |

### `13-乙`　`W-G.9-307R` 所載（`4` 則）

| # | 形 | 徵候 | 根因 | 攔法 |
|---|---|---|---|---|
| `1` | `§六` 款 `2` **自證 ① 之錨取錯** | 該閘印 🔴，致 `§六-4` 之「器紅」成就 | 誤以 `verify/baselines/v3/…` 之**全量 baseline** 列數（`67`／`70`）為錨，而該錨之受詞**⛔ 本次之 `g_tab`**；於**既存之准紅碼**下二者本即不等 | 單之文字為「獨立於**本傾印**（＝本 `jsonl`）」，**⛔「獨立於本次之跑」** ⇒ 改錨為**同一次跑所傾印之 CSV**（`verify/out/got_G值_退縮<tag>.csv`）之列數 ⇒ `56`／`56`、`59`／`59`。🛑 **⛔ 二度驅動 `run_verification`**（授權「全量**一次**」）⇒ 以**同一次跑之產物後算** |
| `2` | `seg` 之列快取**以 `id(src)` 為鍵** | 該器之自我驗證閘（vs `ast.get_source_segment`）由 `837`／`0` **轉紅** | CPython 於原字串被回收後**重用同一 `id`** ⇒ 取到**他檔之列** | 併存該字串本身並以 `is` 覆核（兼使其不被回收）——即本倉 `id(·)` ⛔ 作錨之戒。🔑 **該閘之存在即其價值**：重建須自證 ＝ 現況，**⛔ 以器綠代之** |
| `3` | 逆溯之**止點**三版 | ① 止於 `_sl_left.get('mid')` 之 `'mid'` ⇒ `§五-3` 之 [必命中甲] 誤紅；② 改判準後 `ss`（**形參**）被認作「本函式內有綁定」⇒ 止點**永不觸發**（`7676` 次深度截斷） | 單之止點為「以字面鍵取自**登記表**之式」，⛔ 任一字面鍵；而「登記表」之構造上界定須含**形參**（其值由呼叫端所供 ⇒ 於本函式內即界外） | 終以「**無綁定 ⋁ 其綁定全為形參** ⇒ 界外」界定之。**三版皆由 `§五-3` 之預查造當場判別** |
| `4` | `§七-4` 之**表列數解析式靜默漏列** | 首算得「單 `14`／報告 `14`」之**偽相等**（真值 `14`／`19`） | 框 `` ^\| *`?([^`\|]+?)`? *\| `` 於**標籤帶後綴**之列（`` \| `1`證 \| ``）必失配——捕獲後之 `` `? `` 已食去收尾反引號，`` \| `` 遂需匹配 `證` | 改以「**逐列切格、去表頭與分隔列**」計之，**⛔ 以樣式篩標籤**。🔴 **偽相等比偽相異更難察覺** |

### `13-丙`　本批（補令一）所增

**`0` 則**　🛑 **⛔ 讀為「本批無誤」**。

---

## `14`　🔴 本窗已辦與未辦之工項（承補令 `§一` 態乙之令·**照實**）

| 項 | 狀態 |
|---|---|
| `W-G.9-306`（全部工項） | 已辦·其報告與落檔在倉（`da9ca62` 及其前） |
| `W-G.9-307`（工項零／一／二／三／四 ＋ 收工閘） | 已辦·見項 `9` 之十 `commit` |
| `W-G.9-307` 補令一（本批） | 已辦 |
| **`W-G.9-308`（任何版本·任何工項）** | 🔴 **未辦**（`commit` `0`／檔 `0`）——補令 `§零`／`§四-1` 明令本窗⛔ 辦 |

---

## `15`　🛑 交接予新窗之**未決項**（**照實轉錄·⛔ 判**）

以下二項係 `W-G.9-307R` 出艙時**已具名而裁屬發單側**者，於本窗**未獲裁**：

1. **`§五` 處 `5`〜`7`**（`verify/wf_f1.py :: compute`／`verify/wf_f4.py :: _reshape_block` ×2）之
   `(d1)`／`(e1)`／`(e3)` **皆空** ⇒ 逐處具名「**⛔ 在域**」。
2. **`§六` 款 `3`** 之 `R2`/`L`（`6` 次）：`(甲)` **判定組為空**（其後同一進入序號內無同 (街廓,側) 之
   `_first_corner_alloc_dir`）；`(丙)` ＝ **`False`**。

併：`§六-2` 之 `baseline` 列數差（`0m` `67` vs `56`／`3.5m` `70` vs `59`·**各 `11`**），
其逐列具名者係 harness 自印之 `v3·G值<tag>` 之 `缺列`；本窗**未以 `run_all` 跑 `verify/wv_reconcile.py` 之對帳**。
