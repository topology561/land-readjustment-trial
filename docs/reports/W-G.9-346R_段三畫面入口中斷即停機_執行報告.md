# `W-G.9-346R`　段三畫面入口之「中斷即停機」——執行報告

> **受單** ＝ CC（施工樹 `.claude/worktrees/weight-unit-w-g-9-341-a317f1`·detached）。**單** ＝ `docs/orders/W-G.9-346_重量單.md`（本批工項零入倉）。
> **級** ＝ 重（生產碼 `app.py`）。**側支** ＝ `verify/W-G.9-343-k929b`；**主線 `wip/s1-endpart` 未動**（期末 `git ls-remote` ＝ `6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`）。
> **倉外出艙之所在** ＝ CC 之 scratchpad `…/scratchpad/wg9346/`（⛔ 入倉·本報告所引之數皆為當場所量，其全文或摘要逐字載於本檔）。
> **倉外拋棄式 worktree** ＝ `<P>` ＝ `C:\Users\admin\wg346p`（`run_all` 改前、改後同一路徑）；`C:\Users\admin\wg346q`（工項一之 `commit`·供改前態之 `F6`／`parity` 對照）。二者跑畢皆已 `git worktree remove --force`。

---

## ①　逐 `commit`

| 工項 | `commit` | 父 | 異動（`git show --numstat`） | 推送 |
|---|---|---|---|---|
| 零 | `0f52a186879fa6dabcf28a5973cd1d875b42534d` | `4a633d0` | `docs/orders/W-G.9-346_重量單.md`（新·`A`） | ✅ 側支 |
| 一 | `2adf07ef13ac85100f16f4368552dd34c7f47080` | `0f52a18` | `CLAUDE.md` `+13/−0`；`verify/probes/probe_WG9346_failclosed.py`（新）`+211/−0` | ✅ 側支 |
| 三 | `6cca376561b2e4222ce3587e0ec466d23632f76c` | `2adf07e` | `app.py` `+21/−0` | ✅ 側支（工項四全過後·分開之呼叫） |
| 五 | 本報告之 `commit` | `6cca376` | 本檔（新） | 側支 |

`commit` 訊息之首列皆逐字依單；另附 `Co-Authored-By` 尾列（同側支既有 `4a633d0`／`b0c9edc`／`877cbed` 之體例·見 ⑧ 自解 `3`）。

---

## ②　停機款 `1`〜`10`

| # | 期 | 實得 | 判 |
|---|---|---|---|
| `1` | 側支 `4a633d0`·主線 `6090a7f`·追蹤檔變動 `0` | `git fetch origin` 後 `4a633d0fae4960109b6a892691ab14b5f3738a09`／`6090a7f8b7e37452fa118aec1ec446ecc5e9c6bc`；`git checkout --detach origin/verify/W-G.9-343-k929b` 後 `git status --porcelain --untracked-files=no` ＝ 空 | 🟢 未觸發 |
| `2` | 本單／`F6` 之 bytes·`sha256` 符 `§五-1`；入倉 blob 逐位同 | 本單 `24841` B·`dd9076dc…02a7`·CR `0`（`SELF_SHA256` 依 `P-5` 原口徑實算 `d103932a…fafb0` ＝ 單載）；`F6` `9352` B·`407df5ad99dad61152fbd95dd7836b9cdc5bf5c95b8ef6be5a8f33d17eb7cdab`·CR `0`；`git cat-file blob` 之 `sha256`：本單 `dd9076dc…02a7`、`F6` `407df5ad…cdab` ＝ 來源 | 🟢 未觸發 |
| `3` | 塊 `D1`／`P1` 符 `§五-1` | `P1`（圍欄列 `120`–`134`）`1170` B·`6b585f6efc3532cc6ccdf5bc66afd987bb37447a60d2f371eeec062135ce6655`；`D1`（圍欄列 `197`–`275`）`4078` B·`456a49bb7864ab0cb61195dbc361ffdeb1c3e0d709897b12471fd889673473f7`；皆 CR `0` | 🟢 未觸發 |
| `4` | 工項二：`F6` 紅集 ＝ `{C1, C2, C3, C4, C6}`；`run_all` `rc 1`·`64`（`30`／`34`） | 紅集 `['C1', 'C2', 'C3', 'C4', 'C6']`·`rc 1`；`run_all` `rc 1`·`✅ PASS 30`／`🔴 FAIL 34` | 🟢 未觸發 |
| `5` | 工項三只動 `app.py`；期末 blob ＝ `f4c47af6…` | `git diff --name-only` ＝ `app.py`；`git hash-object app.py` ＝ `f4c47af6b864de683b99985597310d36b1f43d23` | 🟢 未觸發 |
| `6` | 工項四之閘全過 | `VC-1`〜`VC-8` 全 ✅（見 ④） | 🟢 未觸發 |
| `7` | `run_all` 二態 ✅→🔴 `0`·相異 `0` | `64／64`·`30→30`·`34→34`·相異 `0`；全 log `diff` `0` 列 | 🟢 未觸發 |
| `8` | ⛔ 作「孰為正典」之判；⛔ 改 `F4`／`F6`／塊／命令 | 未改 `F4`／`F6`／塊一字；**`<repo>` 引數之字面由正斜線改為反斜線**（同一目錄）——見 ⑧ 自解 `2`，**請發單側覆核其是否觸本款** | 🟡 見 ⑧-2 |
| `9` | 無 `commit` 推主線；工項一之父 ＝ 工項零；工項三之父 ＝ 工項一 | 主線期末 ＝ `6090a7f`；`2adf07e^` ＝ `0f52a18`；`6cca376^` ＝ `2adf07e` | 🟢 未觸發 |
| `10` | 新檔⛔ 為 `git check-ignore` 所命中 | 本單、`F6`、本報告：`git check-ignore -v` 皆 `rc 1`（無命中） | 🟢 未觸發 |

---

## ③　二來源檔與塊

- **二來源檔**：施工樹之根無之（`ls` 實查）⇒ 依單首之 🔑 取 KL 主 checkout 之根（`C:\Users\admin\Desktop\land-readjustment-trial\`），**二進位複製**（`cp -p`），`cmp` 相同；數值見 ② 款 `2`。
- **塊 `P1`**：以單之抽取式（`` ````markdown `` 之次列至 `` ```` `` 之前一列，`\n` 相接末附 `\n`）抽出，`1170` B 符；附於 `CLAUDE.md`（`259916` B）之末 ⇒ `261086` B（倉側 `git cat-file -s` 同）；改前全檔為改後之嚴格前綴（`b == a + p1` 為 `True`）；`numstat` `13`／`0`。
- **塊 `D1`**：同法抽出，`4078` B 符；`git apply --check` 過、`git apply` 後 `git hash-object app.py` ＝ `f4c47af6b864de683b99985597310d36b1f43d23`（＝ `§五-1` 項 `6`）；`python -m py_compile app.py` 過。

### pre-flight（`§零-3`）

`python verify/probes/probe_order_preflight.py docs/orders/W-G.9-346_重量單.md` ⇒ `rc 0`：🔴 機械 `0` 項；🟡 `P-4` `1` 項（`:161`·`| 閘 | 受詞 | 期 |`）；ℹ️ `P-5` 相符（受詞 `24763` B）、`P-3` `def main` 區間 ＝ `18033`-`25612`。與 `§五-1` 項 `7` 逐項同。`P-4` 採單所載之**具名豁免**（`VC-7` 之「`30→30`」係計數之改前改後、⛔ 方向性轉引）。

### 取號（`§零-1`）

`python verify/probes/wg9268_gate6_occupancy.py 4a633d0 W-G.9-346 W-G.9-345 W-G.9-396` ⇒ `rc 0`；母體 ＝ 全 `docs/` `893` 檔（讀不到 `20` ＝ git 失敗 `0` ＋ 解碼失敗 `20`）；`W-G.9-346` 嚴格／寬式六數 ＝ `[0, 0, 0, 0, 0, 0]`·鬆框 `0`／`0`；`W-G.9-345` `2`／`3`／`4`·列框 `7`·檔框 `2`·鬆框 `2`／`23`；`W-G.9-396` 宣告框 `0`·鬆框 `1`／`1`；`W-G.9-963` 六數 `0`·鬆框 `2`／`2`——與單 `§零-1` 之表逐格同。本批⛔ 鑄號。

### 開工錨（`§零-0` 項 `3`）

`python verify/probes/probe_WG9321_issuer_anchor.py <repo> <檔> 523 522` ⇒ `rc 0`；遠端 heads `30`（`verify/` `25`·`wip/` `3`·`claude/` `1`·`main` `1`）；`app.py` blob `550ba546f2ef172f9029c284e1323e426438f0bc`；正典器二閘皆過（自誤 MAX `523`）。工項四期末（`6cca376`）重跑亦 `rc 0`。

---

## ④　工項二、四之全部出艙

### 工項二　改前態（生產碼 ＝ 開工態·`app.py` blob `550ba546…`）

**`F6 run <repo> 3.5`**（於 `2adf07e`·`rc 1`·全文）：

```
【F6 run】態 2adf07ef13ac85100f16f4368552dd34c7f47080·退縮 3.5
  ✅ C0 正常：ran=True·停機訊息=None·selected=tuple·段二序 13 列
  🔴 C1 段三本體丟 KeyError：例外=KeyError·selected=None·訊息=''
  🔴 C2 終趟中止：例外=_Stop·selected=None·訊息=''
  🔴 C3 無歸戶＋殘留段二序：k6b_stage3_run 呼叫 1·ran=None·例外=_Injected·selected=None
  🔴 C4 試算趟無產出：代理趟 14·例外=None·停機訊息=''·selected=tuple
  ✅ C5 旗標 off：ran=False·停機訊息=None·指紋=False·selected=None
  🔴 C6 首趟中止：例外=_Stop·selected=None·訊息=''
⇒ 紅 ['C1', 'C2', 'C3', 'C4', 'C6']；rc 1
```

（本器於施工樹以正斜線 `<repo>` 跑一次、於 `wg346q`〔同 `2adf07e`〕以反斜線 `<repo>` 再跑一次，二 log `cmp` **逐位相同**。）

**`run_all` 改前**（`<P>` @ `2adf07e`·`10:54:39`–`11:04:41`）：`rc 1`；框 `^\s*✅ PASS ` ＝ `30`、`^\s*🔴 FAIL ` ＝ `34`（`64` 項）；log `1233` 列。跑畢 `git worktree remove --force`，`<P>` 保留為工項四之同一路徑。

### 工項四　改後態（`6cca376`·`app.py` blob `f4c47af6…`·殼之旗標 `None None`）

| 閘 | 期 | 實得 | 判 |
|---|---|---|---|
| `VC-1` | 恰 `app.py`；`21`／`0`；blob ＝ `f4c47af6…` | `git diff --name-only 2adf07e 6cca376` ＝ `app.py`；`--numstat` ＝ `21	0	app.py`；`git rev-parse 6cca376:app.py` ＝ `f4c47af6b864de683b99985597310d36b1f43d23` | ✅ |
| `VC-2` | `rc 0`；七列全 ✅；末列 `⇒ 紅 []；rc 0` | `rc 0`；七列全 ✅；末列逐字 `⇒ 紅 []；rc 0`（全文見下） | ✅ |
| `VC-3` | 五態皆 `rc 0`；`60／59`、`63／62`、`68／67`、`68／67`、`63／62`；不符格 `0`；`Z` ＝ `[('harness', 'R1-抵費地-2')]`；`3.5 on` 紀錄 `18` 列 | `3.5 on`／`0.0 on`／`3.5 s3off`／`3.5 off`／`0.0 off` 皆 `rc 0`；`json` 之 `n_rows` 依序 `[60, 59]`／`[63, 62]`／`[68, 67]`／`[68, 67]`／`[63, 62]`，`bad` 皆 `0`；`Z` 皆 `[('harness', 'R1-抵費地-2')]`；`stage3_log` `18`／`0`／`0`／`0`／`0` 列 | ✅ |
| `VC-4` | `rc 1` | `rc 1`（配地列不符格 `273`·不符 `3` 項） | ✅ |
| `VC-5` | 三者皆 `rc 0`；`W0`〜`W8` 全 ✅；丙部四突變皆 ✅ | `wiring` `rc 0`（`W0`〜`W8` `14` 列 ✅·丙 `m1`〜`m4` 皆 ✅·🔴 行 `0`）；`wfctx 3.5` `rc 0`；`wfctx 0.0` `rc 0` | ✅ |
| `VC-6` | 五器皆 `rc 0`；`wfns_ast` `40`／`40`／`39`；`F5`「app 側宿主 ＝ f3_screen_stepg_run」 | `issuer_anchor` `0`；`closegate 523 522 .` `0`（二閘皆過）；`wfns_ast` `0`（`40`／相異 `40`·引擎相異名 `39`）；`F5` `0`（`ℹ️ app 側宿主 ＝ f3_screen_stepg_run（W-G.9-345）`·丙1〜丙4 ✅）；`probe_WG9341_synth` `0`（戊1〜戊3 ✅·`ε ＝ 0.0002`） | ✅ |
| `VC-7` | `run_all` `rc 1`；`runall` `rc 0`；`64／64`·`30→30`·`34→34`；相異 `0`；全 log `diff` `0` 列 | `run_all`（`<P>` @ `6cca376`·`11:05:08`–`11:15:04`）`rc 1`；`runall` `rc 0`；全文見下；`diff runall_before.log runall_after.log` ＝ **`0` 列** | ✅ |
| `VC-8` | `+` 列以 `§三-2` regex 篩 ⇒ `0` | `+` 列 `21`（扣 `+++`）；命中 `0`。判別力：同 regex 於全 `app.py` ＝ `88`（⇒ 框非恆空） | ✅ |

**`VC-2`　`F6 run <repo> 3.5`（於 `6cca376`·全文）**：

```
【F6 run】態 6cca376561b2e4222ce3587e0ec466d23632f76c·退縮 3.5
  ✅ C0 正常：ran=True·停機訊息=None·selected=tuple·段二序 13 列
  ✅ C1 段三本體丟 KeyError：例外=KeyError·selected=raise·訊息='🔴 [K-6-B 段三·畫面] 前次「街角合併重試」停機：「街角合併重試」未完成（執行中斷）——請重跑「街角地優先權選位」'
  ✅ C2 終趟中止：例外=_Stop·selected=raise·訊息='🔴 [K-6-B 段三·畫面] 前次「街角合併重試」停機：「街角合併重試」未完成（執行中斷）——請重跑「街角地優先權選位」'
  ✅ C3 無歸戶＋殘留段二序：k6b_stage3_run 呼叫 0·ran=False·例外=None·selected=None
  ✅ C4 試算趟無產出：代理趟 2·例外=_Stop·停機訊息='🔴 [K-6-B 段三·畫面] 試算（街角選位）未產出 winners 表：R5／左／628-18(2)（停機款 9）'·selected=raise
  ✅ C5 旗標 off：ran=False·停機訊息=None·指紋=False·selected=None
  ✅ C6 首趟中止：例外=_Stop·selected=raise·訊息='🔴 [K-6-B 段三·畫面] 前次「街角合併重試」停機：「街角合併重試」未完成（執行中斷）——請重跑「街角地優先權選位」'
⇒ 紅 []；rc 0
```

（附：`F6 run <repo> 0.0` ⇒ `rc 3`：`🔴 C0 之段三未執行（ran=False·段二序 0 列）⇒ 本退縮無從量段三之中斷 ⇒ 無從判定`——與單 `VC-2` 之註同·**⛔ 作為閘**、僅記錄。）

**`VC-7`　`runall_cmp.txt`（全文）**：

```
【runall】項 64／64·PASS 30 → 30·FAIL 34 → 34
  相異項 0；其餘 64 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／34 → 22／34；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
```

全 log `diff` ＝ `0` 列（改前 `1233` 列·改後同）。

---

## ⑤　`§二` 之放行

KL 於貼本單之同一訊息內逐字：

> KL 放行：是（工項三之生產碼 commit 只推側支 verify/W-G.9-343-k929b；主線不動）。

⇒ 工項四全過後，以**分開之呼叫**先驗快轉（`git merge-base --is-ancestor origin/verify/W-G.9-343-k929b HEAD` ⇒ 真；遠端側支 ＝ `2adf07e` ＝ `6cca376^`），再 `git push origin HEAD:verify/W-G.9-343-k929b`（`2adf07e..6cca376`）。推後 `git ls-remote`：側支 `6cca376…`、主線 `6090a7f…`（未動）。主線之快轉⛔ 在本放行內（`§二 (c)`）。

---

## ⑥　reviewer 之出艙（已送·`redistribution-reviewer`·唯讀·於 `6cca376`）

**結論**：⛔ 無 BLOCKED；`§三-1` 之甲〜丁四項逐一坐實。其要點（行號 ＝ `6cca376` 之 `app.py`·易腐）：

1. **甲**：`K6B_SCREEN_READBACK_KEYS` 之 `6` 鍵皆在 `K6B_SCREEN_TRIAL_KEYS`（`23` 鍵）內——**確認**（reviewer 係目視逐鍵對；其 AST 子集檢為倉之 heredoc 守門器所擋、未跑）。
2. **丙**：立 `K6B_STAGE3_PENDING` 之後之出口逐一列舉；撤之者唯「段二序為空」與步驟 `8` 之成二處；`k6b_stage3_run` 之 `RuntimeError` 以自身訊息覆寫；其餘（首趟中止、非 `RuntimeError`、終趟中止、步驟 `8` 內之例外）皆留之——**確認**。旗標 off 之路徑（立之前即 `return`）**一字未動**——**確認**。
3. **消費端**：`k6b_stage3_selected` 見停機訊息即 `raise`（訊息止於「請重跑「街角地優先權選位」」）；`k6b_screen_build_for_g`／步驟 M 皆 `st.error`＋`st.stop()`＋`raise`；`_build_wf_ctx` 經七級調配鈕之 `except` 以 `🔴 七級調配停機` 顯示——**確認 loud**。
4. **丁**：試算中之去鍵僅於 `trial_winner`／`alloc_state` 內、由 `finally` 以 `K6B_SCREEN_TRIAL_KEYS` 全數復原 ⇒ ⛔ 外洩；首趟前去 `f3_k6b_stage2_order` ⛔ 破首趟（首趟⛔ 先讀之）——**確認**。
5. 🟡 **單 `§三-1` 之一句經 reviewer 判為「字面不成立、結論仍成立」**：「二抽出函式可達之模組層函式對街角選位產物之讀唯 `f3_corner_range_areas` 與 `f3_pk_alloc_depth`」——`f3_screen_stepg_run` 本身即讀 `6` 鍵中之 `3` 鍵（`f3_corner_winners`／`f3L_forced_offset`／`f3_corner_range_polys`）；惟於 `alloc_state` 內其讀皆在同一 `try` 之街角選位**之後**，而街角選位先寫之（winners 由本批之閘守）⇒「去此 `6` 鍵⛔ 改街角選位本身之算」之結論成立。另：街角選位所跳過之街廓（無 FRONT_LINE）於試算中⛔ 再承襲殘留之 `polys` 條目——reviewer 判為「loud 或中性、⛔ 靜默」。
6. 🟡 **WARNING（屬 `W-G.9-345`·⛔ 本 `commit` 所致·候人裁）**：`_f3L_invalidate_g_cache` 於退縮／深度變更時一併去 `f3_k6b_stage3_error` 與指紋 ⇒ 其後 `k6b_stage3_selected` 回 `None`，配地／七級調配／步驟 M 以段三前之宗地配出。此非 `f3_screen_k6b_stage3` 之出口、⛔ 在丙之射程內；**是否可接受之中間態，CC ⛔ 判**（單 `§零` 之 🔴）。
7. NOTE（⛔ 本 `commit` 所致·旗標 off 亦同）：首趟前僅去段二序；若首趟全⛔ 寫（歸戶空等），「段二序為空」之出口撤停機訊息，而前次之 `f3_corner_winners`／`f3L_forced_offset` 可能殘留供配地。

reviewer 另自驗：`git hash-object app.py` ＝ `6cca376:app.py` ＝ `f4c47af6…`；`numstat` `21 0`；`git diff -w` 之刪除 `0`；`py_compile` 過。

---

## ⑦　執行時間

本機時間（`+0800`）`2026-09-26` 約 `10:52` 開工 → `11:04:41` 改前 `run_all` 畢 → `11:15:04` 改後 `run_all` 畢 → 其後工項三推送與本報告。工項四之器（反斜線版）合計約 `8` 分（逐器秒數見 `gates_bs/_rc.txt`：`F6 3.5` `78` s·`parity 3.5 on` `86` s·`--perturb` `86` s·餘各 `1`–`53` s）。

---

## ⑧　CC 之自捕與自解清單

| # | ① 疑義逐字 | ② 讀法 | ③ 所取 | ④ 機械證據 | ⑤ 所棄之由 |
|---|---|---|---|---|---|
| `1` | 「二來源檔（KL 置於 **CC 之施工樹之根**）」 | (a) 本施工樹之根；(b) KL 主 checkout 之根 | (b)（單首 🔑 明文之退路） | 施工樹之根 `ls` 無二檔；主 checkout 之根二檔 bytes／`sha256` 與 `§五-1` 逐位符 | (a) 無檔可取 |
| `2` 🩸 **自捕（量測器紅）** | 單之命令形 `F4 parity <repo> …`／`F6 run <repo> …`，`<repo>` 未定字面 | (a) 正斜線 `C:/…`（首跑所用·`pwd -W`）；(b) 反斜線 `C:\…`（`cygpath -w`） | (b) | **首跑（正斜線）**：`parity` 五態與 `--perturb` 皆 `rc 3`、`wfctx 3.5`／`0.0` 皆 `rc 1`，訊息同為 `K-9-5-4②：side_mid=(310506.137745, 2651928.673455) 於 f3_cad_side_lines_by_side 查無對應側界`。**同一現象於改前態（`2adf07e`）完全重現** ⇒ ⛔ 本改動所致。**成因**（倉外除錯器實測）：`verify/app_harvest.py` 之 `_CACHE` 以**路徑字串**為鍵，`F2._boot` 以 `os.path.join(<repo>, "app.py")`（正斜線）harvest、`run_verification` 以其自身之 `APP_PY`（反斜線）再 harvest ⇒ **二次 harvest**，第二個 fake `streamlit` 取代 `sys.modules['streamlit']`；`_first_corner_alloc_dir` 內 `import streamlit` 取得後者（其 session 無 `f3_cad_side_lines_by_side`），而 harness 所傳之 `fst.session_state` 中 `R4 left` 之 `mid` 與所求者距離 `0.0`（`fst is sys.modules['streamlit']` ＝ `False`）。**反斜線重跑**：改前態 `parity 3.5 on` `rc 0`（`60／59`·不符 `0`）；改後態全部閘如期（④）。`F6` 與 `wiring`／`closegate` 等不經該路之器二式結果相同（改前 `F6` 二 log `cmp` 逐位同；改後 `VC-2` 二式皆 `rc 0`）。同族前例 ＝ 記憶所載「harvest 類探針 repo 路徑須反斜線（自誤 479）」 | (a) 使 harvest 雙載而量到空 session，**量測器紅**。🟡 **請發單側覆核**：本項係「命令之 `<repo>` 引數字面」之選取（同一目錄之二寫法），CC 判其⛔ 屬停機款 `8` 之「改命令一字以求其過」；若發單側判屬之，本批之工項三推送即須回議 |
| `3` | `commit` 訊息「逐字」 | (a) 單列之一行；(b) 單列之一行 ＋ `Co-Authored-By` 尾列 | (b) | 側支既有 `4a633d0`／`b0c9edc`／`877cbed` 皆為首列逐字 ＋ 空列 ＋ 該尾列 | (a) 與側支之既有體例相異 |
| `4` | 工項二「於工項一之 `commit` 之施工樹」跑 `F6` | (a) 施工樹本身；(b) 另一同 `commit` 之倉外樹 | 首跑取 (a)；反斜線之重跑取 (b)（`wg346q` @ `2adf07e`·施工樹其時已在 `6cca376`） | 二者 `HEAD` 皆 `2adf07ef…`、`app.py` blob 皆 `550ba546…`；二 log 逐位同 | — |
| `5` | `VC-2` 之「⛔ 以 `0.0` 代之」 | — | 另跑 `0.0` 一次**僅作記錄**（`rc 3`），⛔ 以之代 `3.5` | 見 ④ 之附 | — |
| `6` | pre-flight `P-4`（`:161`） | 採／不採單之具名豁免 | 採 | 該列為 `§五` 工項四表之表頭，其轄之 `30→30` 係計數之改前改後 | — |

🔒 本批⛔ 改 `F4`／`F6`／塊 `D1`／`P1` 一字；⛔ 動 `def main()`；⛔ 動主線；⛔ 鑄號；⛔ 動 `K-6` 典／`GB` 簿／自誤簿／`VR` 簿。
