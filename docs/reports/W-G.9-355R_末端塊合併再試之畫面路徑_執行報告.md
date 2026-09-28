# `W-G.9-355R`　末端塊之合併再試（含 `K-9-50`）之畫面路徑：執行報告

> **單** ＝ `docs/orders/W-G.9-355_規格單.md`（規格單流程之首張）。**受單** ＝ CC（新窗）。
> **分支** ＝ 一切 `commit` 推至側支 `verify/W-G.9-353-endmerge`（皆快轉·承 `f55935c`）；主線 `wip/s1-endpart` ⛔ 動（仍 `0b05925374f2de46c2493f5f56ef64667a2fed1d`）。
> **態** ＝ 開工 `f55935cb95b5e6c058231ee89d5dd19e3a291456`；本報告撰寫時側支之端 ＝ `b1d3d3b7977d455f0239bc4768975137f30ce2e0`（工項三）。
> **量測環境** ＝ Windows 11·Python 3.13.11·Git Bash；殼⛔ 設 `WV_K6_STEP0`／`WV_K6B_STAGE3`／`WV_K929_6`（出艙 `[None, None, None]`）；`core.autocrlf`：system `true`／local `false`（有效 `false`）。
> **收工閘**（`§四-3`）之實測值出艙於對話（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 異動（`git show --numstat`） |
|---|---|---|
| 零　本單原封入倉 | `31f03d3d01902462409a20058f95d78a8fe7604e` | `docs/orders/W-G.9-355_規格單.md` 增 `1136`／刪 `0`（新檔） |
| 一　量測器入倉 | `167e475d480c657fa3d0ff27189b16ee278dbb2d` | `verify/probes/probe_WG9355_screenmerge.py` 增 `736`／刪 `0`（新檔）；`verify/probes/probe_WG9345_screen.py` 增 `15`／刪 `4` |
| 二　生產碼（🔴 `app.py`） | `f173a4e2a54d1ae036e14ecc35e88d0a9befdf31` | `app.py` 增 `214`／刪 `43`；blob `dc3e52bea4b9b28a2bd2e9dc28e79030914b5548`（`1589495` B）→ **`e11232a6569bf33c7b2b7f15da989873a06ff28c`（`1601188` B）** |
| 三　登記 | `b1d3d3b7977d455f0239bc4768975137f30ce2e0` | `CLAUDE.md` 增 `22`／刪 `0`；`docs/reports/W-G.9波_claude.ai側自誤登記.md` 增 `12`／刪 `0`；`docs/reports/W-G.9波_恆常附款登記表.md` 增 `31`／刪 `0` |
| 四　本報告 | （本檔所在之 `commit`·自指 ⇒ 見對話） | 本檔（新檔） |

## ② 停機款 `1`〜`11` 之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `0b05925`、側支 ＝ `f55935c`、施工樹追蹤檔無變動、遠端 heads ＝ `31` | 主線 `0b05925374f2de46c2493f5f56ef64667a2fed1d`；側支 `f55935cb95b5e6c058231ee89d5dd19e3a291456`；`git status --porcelain --untracked-files=no` 空；heads `31` ⇒ ⛔ 觸 |
| `2` | 本單 bytes／`sha256` ＝ `§五-1`；來源存在；入倉 blob 與來源逐位同 | 來源取於第二處（KL 主 checkout 之根·施工樹之根無）；`93407` B·`sha256` `8d9ec31837f1666db3ef442e210328067950c5b2ea4bf40c994f98cc3ad509a3`·`CR` `0`；`SELF_SHA256`（`P-5` 原口徑·受詞 `93329` B）單載 ＝ 實算 ＝ `d26d5120682792893d36cc1a8f32662f4008b252660cf31c028376d3f1b53f48`；`git cat-file blob HEAD:docs/orders/W-G.9-355_規格單.md` 與來源 `==` ⇒ ⛔ 觸 |
| `3` | 五塊之 bytes／`sha256` ＝ `§五-1` | 見 ④，五塊皆逐位同 ⇒ ⛔ 觸 |
| `4` | `git apply --check` 過；施後 blob ＝ `92f9dc4d…`；前置 `1`〜`6` 皆如期 | `--check` `rc 0`；施後 `probe_WG9345_screen.py` ＝ `92f9dc4d979e37b2967f2a144c5752ee871ee921`（`49785` B）、`probe_WG9355_screenmerge.py` ＝ `3648cd6c6cd13e8b5c6f73ecb95fd2a1feb5d29c`（`35946` B）；前置見 ③-1 ⇒ ⛔ 觸 |
| `5` | 規格無涉域上判斷之歧義；⛔ 須改 `§三-3` | 未遇 `D-1`〜`D-3`（實作細節之選擇見 ⑦-2）⇒ ⛔ 觸 |
| `6` | `V-1`〜`V-6` 皆 ＝ 期；⛔ 改量測器；本案配地⛔ 變 | 見 ③-2；`V-3` 之二 `diff` 空、`V-5` 相異項 `0` ⇒ ⛔ 觸 |
| `7` | `push` 目標恆 ＝ 側支；皆快轉；主線⛔ 推進 | `31f03d3`／`167e475`／`f173a4e`／`b1d3d3b` 皆 `HEAD:verify/W-G.9-353-endmerge` 快轉（⛔ `--force`）；主線仍 `0b05925…` ⇒ ⛔ 觸 |
| `8` | 工項三三檔之刪除欄 ＝ `0`、改前為改後之嚴格前綴 | 刪除欄 `0`／`0`／`0`；嚴格前綴三檔皆 `True` ⇒ ⛔ 觸 |
| `9` | `§四-3` 收工閘皆 ＝ 期 | 於工項四之 `commit` 推後量——出艙於對話（⛔ 本檔） |
| `10` | ⛔ 作「孰為正典」之判；⛔ 改塊、器、命令一字 | 未作；塊與器皆逐位原封；命令逐字 |
| `11` | 新檔⛔ 為 `git check-ignore` 所命中 | `docs/orders/W-G.9-355_規格單.md` `rc 1`；`verify/probes/probe_WG9355_screenmerge.py` `rc 1`；本檔 `rc 1`（入倉前驗）⇒ ⛔ 觸 |

## ③ 工項二之前置與驗之全部出艙

**內嵌之 log**：由落檔以程式直接嵌入（⛔ 手抄）；Windows 下 Python 之 stdout 重導為文字模式 ⇒ 落檔之行尾為 `CRLF`（孤 `CR` ＝ `0`），嵌入時一律正規化為 `LF`（本檔 `CR` ＝ `0`·收工閘 `3`）；`V-3`／`V-5` 之 `diff` 係於同平台之原落檔間為之（⛔ 正規化）。
**命令之形**：`<repo>` ＝ `C:\Users\admin\Desktop\land-readjustment-trial\.claude\worktrees\w-g-9-351-weight-unit-6d2b00`（施工樹·detached）；`<O>` ＝ 倉外之目錄；`<P>` ＝ `C:\Users\admin\AppData\Local\Temp\wgP355`（前置與驗之 `run_all` **同一路徑**·各自 `git worktree add --detach` 後跑、跑畢 `git worktree remove --force`）。

### ③-1　前置（態 ＝ 工項一之端 `167e475`）

| # | 受詞 | 期 | 實 |
|---|---|---|---|
| `1` | `F14 selftest` | `rc 1`·末列 ＝ `§一` 項 `8` | `rc 1`；末列與 `§一` 項 `8` 逐字相同（字串比較 `LASTLINE_MATCH`）；✅ 列 `36`（含 `P0` 列）／🔴 列 `40`（含「受詞缺」列）；`P0` `74／74` |
| `2` | `F14 run` | `rc 1`·末列 `⇒ 紅 ['受詞缺']；rc 1` | 同（全文見下） |
| `3` | `F4 parity` `3.5`／`0.0` | 皆 `rc 1`·紅項恰「合併再試 session 鍵」二列 | 皆 `rc 1`（「不符 2 項」）；🔴 列恰 `f3_end_block_merge`／`f3_end_block_merge_log` 二列（末十列見 ③-3） |
| `4` | `F8 run` `3.5`／`0.0` | 皆 `rc 0` | 皆 `rc 0`·末列 `⇒ 紅 []；rc 0`（`2988` B／`3318` B） |
| `5` | `F6 run` `3.5` | `rc 0` | `rc 0`（C0〜C6 皆 ✅） |
| `6` | `run_all`（`<P>`） | 落檔 | `rc 1`（准紅碼之既存 FAIL）·`runall_pre.log` `238132` B（其 bytes 平台與路徑相依·⛔ 入判） |

`F14 selftest`（前置）全文：

```text
── 受詞：['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows'] ⇒ 缺 ['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows'] ──
── 合成對照（樁·期值出自規格單 §三）──
  ✅ T1a 段二序為空之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  🔴 T1b 合併再試恰一次、段三本體⛔ 呼：得 (0, 0)　期 (1, 0)
  ✅ T1c 無變 ⇒ 回傳之宗地 ＝ 輸入（同一物件）：得 (True, True)　期 (True, True)
  🔴 T1d 紀錄與逐列入 session：得 ({'舊紀錄': 1}, ['舊紀錄'])　期 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])
  ✅ T1e 無變 ⇒ 段三之結果⛔ 存（k6b_stage3_selected ＝ None）、無停機訊息：得 (None, None)　期 (None, None)
  ✅ T1f 無變 ⇒ 真 st 之街角選位⛔ 重跑（恰一）：得 1　期 1
  🔴 T1g 合併再試之輸入：宗地 ＝ 段三之出（此出口 ＝ 原宗地）：得 (False, False)　期 (True, True)
  🔴 T1h 合併再試之輸入：上鎖 ＝ 末一次真 st 街角選位之段一上鎖、街角第 1 宗 ＝ 其 winners、街廓／中心線／退縮／歸戶：得 (None, None, None, None, None, None)　期 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})
  🔴 T1i alloc_eval 回試算配地之評選（深拷貝）：得 (None, None)　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)
  ✅ T1c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T1c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T1c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  🔴 T1c4 試算配地皆 'trial'（其數 ≥ 1）：得 (False, [])　期 (True, ['trial'])
  ✅ T2a 段三旗標 off 之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  🔴 T2b 合併再試恰一次、段三本體⛔ 呼：得 (0, 0)　期 (1, 0)
  🔴 T2c 有變 ⇒ 回傳之宗地 ＝ 合併再試之出（同一物件）：得 (False, False)　期 (True, True)
  🔴 T2d 紀錄與逐列入 session：得 ({'舊紀錄': 1}, ['舊紀錄'])　期 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])
  🔴 T2e 配地所用之宗地 ＝ 合併再試之出（k6b_stage3_selected·同一物件）：得 (False, False)　期 (True, True)
  🔴 T2f 所存之結果繫於段三前之宗地與退縮（他 build 或他退縮 ⇒ loud）：得 (None, None)　期 (('raise', True), ('raise', True))
  🔴 T2g 有變 ⇒ 真 st 之街角選位重跑一次、所用 ＝ 合併再試之出：得 (1, False)　期 (2, True)
  ✅ T2h 無停機訊息：得 None　期 None
  ✅ T2c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T2c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T2c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  🔴 T2c4 試算配地皆 'trial'（其數 ≥ 1）：得 (False, [])　期 (True, ['trial'])
  ✅ T3a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  🔴 T3b 段三本體與合併再試各恰一次：得 (1, 0)　期 (1, 1)
  🔴 T3c 段三之試算配地亦 'trial'：得 [None]　期 ['trial']
  ✅ T3d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}
  🔴 T3e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (False, False, None)　期 (True, True, {'C(1)'})
  🔴 T3f 回傳之宗地 ＝ 末態（同一物件）：得 (False, False)　期 (True, True)
  🔴 T3g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (False, False)　期 (True, True)
  🔴 T3h 紀錄入 session：得 {'舊紀錄': 1}　期 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}
  🔴 T3i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (1, False)　期 (2, True)
  ✅ T3j 無停機訊息：得 None　期 None
  ✅ T3c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T3c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T3c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  🔴 T3c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, [None])　期 (True, ['trial'])
  ✅ T9a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  🔴 T9b 段三本體與合併再試各恰一次：得 (1, 0)　期 (1, 1)
  🔴 T9c 段三之試算配地亦 'trial'：得 [None]　期 ['trial']
  ✅ T9d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}
  🔴 T9e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (False, False, None)　期 (True, True, {'C(1)'})
  ✅ T9f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T9g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  🔴 T9h 紀錄入 session：得 {'舊紀錄': 1}　期 {'退縮': 3.5, '標的': [], '皆未達': {}}
  ✅ T9i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (1, True)　期 (1, True)
  ✅ T9j 無停機訊息：得 None　期 None
  ✅ T9c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T9c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T9c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  🔴 T9c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, [None])　期 (True, ['trial'])
  🔴 T4a 合併再試停機 ⇒ 畫面 st.error ＋ st.stop：得 (None, False)　期 ('_Stop', True)
  🔴 T4b 停機訊息入 session（含合併再試之原訊息）：得 False　期 True
  🔴 T4c 其後之配地 loud（k6b_stage3_selected raise「請重跑」；k6b_screen_build_for_g ⇒ st.stop）：得 (None, '未擋')　期 (('raise', True), 'st.stop')
  🔴 T4d 前次之紀錄已去、本次⛔ 寫：得 ({'舊紀錄': 1}, ['舊紀錄'])　期 ('<缺>', '<缺>')
  ✅ T4c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T4c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  🔴 T4c4 試算配地皆 'trial'（其數 ≥ 1）：得 (False, [])　期 (True, ['trial'])
  🔴 T5a 合併再試中斷（KeyError）⇒ 例外上拋：得 None　期 'KeyError'
  🔴 T5b 未完成之標記留存（其文含「末端塊合併再試」）：得 False　期 True
  🔴 T5c 其後之配地 loud（k6b_stage3_selected raise「請重跑」）：得 None　期 ('raise', True)
  🔴 T5d 前次之紀錄已去：得 {'舊紀錄': 1}　期 '<缺>'
  ✅ T5c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T5c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  🔴 T5c4 試算配地皆 'trial'（其數 ≥ 1）：得 (False, [])　期 (True, ['trial'])
  ✅ T8a 段三停機 ⇒ st.stop；合併再試⛔ 辦：得 ('_Stop', 0)　期 ('_Stop', 0)
  🔴 T8b 前次之紀錄已去（⛔ 殘留舊紀錄）：得 ({'舊紀錄': 1}, ['舊紀錄'])　期 ('<缺>', '<缺>')
  ✅ T8c 停機訊息含段三之原訊息：得 True　期 True
  ✅ T8c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T8c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  🔴 T8c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, [None])　期 (True, ['trial'])
  🔴 TK 試算隔離之鍵含 SS_END_BLOCK_MODE 之值、末項仍 f3_k929_6_log：得 (False, True)　期 (True, True)
  🔴 受詞缺：['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows']（T6／T7／TS 無從量）
── P0 判式自驗（期值記錄須全綠；逐項擾動須恰該項紅）──
  ✅ P0 期值記錄全綠 True；逐項擾動恰該項紅 74／74
⇒ 紅 ['T1b', 'T1d', 'T1g', 'T1h', 'T1i', 'T1c4', 'T2b', 'T2c', 'T2d', 'T2e', 'T2f', 'T2g', 'T2c4', 'T3b', 'T3c', 'T3e', 'T3f', 'T3g', 'T3h', 'T3i', 'T3c4', 'T9b', 'T9c', 'T9e', 'T9h', 'T9c4', 'T4a', 'T4b', 'T4c', 'T4d', 'T4c4', 'T5a', 'T5b', 'T5c', 'T5d', 'T5c4', 'T8b', 'T8c4', 'TK', '受詞缺']；rc 1
```

`F14 run`（前置）全文：

```text
  🔴 受詞缺：['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows']
⇒ 紅 ['受詞缺']；rc 1
```

### ③-2　驗（態 ＝ 工項二之 `commit` `f173a4e`·`push` 前·殼無 `WV_`）

| # | 期 | 實 |
|---|---|---|
| `V-1` | `selftest`／`run` 皆 `rc 0`、末列 `⇒ 紅 []；rc 0`；諸項 ✅；`run` 之數 ＝ `§一` 項 `6`；`E` 五列 ✅ | `selftest` `rc 0`（✅ `87` 列·含 `P0`；`P0` `86／86`）；`run` `rc 0`（`1167` s）；`R1` 二退縮之紀錄 ＝ `{'退縮': x, '標的': [], '皆未達': {}}`、逐列 `0`；甲乙丙之交面積、`351.7`、鏈首宗與 `G`、切半之量皆 ＝ `§一` 項 `6`；`E` 五列皆 ✅（全文見下） |
| `V-2` | `parity` 二退縮 `rc 0`；配地列 `35`／`34`、`36`／`35`、不符格 `0`；`Z` ＝ `[('harness', 'R1-抵費地-2')]`；合併再試二鍵 ✅ | 皆 `rc 0`（「不符 0 項」）；數全同期（末十列見 ③-3） |
| `V-3` | `F8 run` 二退縮 `rc 0`；與前置之二份 `diff` 皆空 | 皆 `rc 0`；`diff` 皆空（`DIFF35_EMPTY`／`DIFF00_EMPTY`） |
| `V-4` | 十器皆 `rc 0`；`wfns_ast` `48／48／47`；`main_synth` 宿主 ＝ `f3_screen_stepg_run`；`F4 wiring` `W0`〜`W8` ✅、四突變轉紅 | `F6 run` `rc 0`（C0〜C6 ✅）；`F4 wiring` `rc 0`（「不符 0·器紅 0」·`W0`〜`W8` ✅·`m1`〜`m4` 皆轉紅）；`F4 selftest` `rc 0`（`10/10`）；`wfns_ast` `rc 0`（`48`／`48`／`47`）；`main_synth` `rc 0`（「app 側宿主 ＝ f3_screen_stepg_run」）；`F9`／`F10`／`F11`／`F12`／`F13 wiring` 皆 `rc 0`·末列 `⇒ 紅 []；rc 0` |
| `V-5` | 項 `64`；PASS `28 → 28`；相異 `0`；末端夾具／golden `21／21`；對帳段 `22／36 → 22／36` | 皆如期（對拍全文見下）；`runall_post.log` `238132` B；二份之 `diff` **空**（逐位相同·同一 `<P>` 路徑） |
| `V-6` | 生產碼 `34` 檔對工項一之端相異恰 `1`（`app.py`）；`verify/` 相異 `0` | 受檢 `34` 檔（`app.py` ＋ `verify/` 頂層 `*.py` `33`）·相異 `1` ＝ `app.py`（`dc3e52be…` → `e11232a6…`·增 `214`／刪 `43`）；`verify/` 全檔相異 `0` |

`F14 selftest`（驗）全文：

```text
── 受詞：['f3_screen_end_block_merge', 'k6b_screen_callbacks', 'end_block_merge_rows'] ⇒ 缺 [] ──
── 合成對照（樁·期值出自規格單 §三）──
  ✅ T1a 段二序為空之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  ✅ T1b 合併再試恰一次、段三本體⛔ 呼：得 (1, 0)　期 (1, 0)
  ✅ T1c 無變 ⇒ 回傳之宗地 ＝ 輸入（同一物件）：得 (True, True)　期 (True, True)
  ✅ T1d 紀錄與逐列入 session：得 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])　期 ({'退縮': 3.5, '標的': [], '皆未達': {}}, [])
  ✅ T1e 無變 ⇒ 段三之結果⛔ 存（k6b_stage3_selected ＝ None）、無停機訊息：得 (None, None)　期 (None, None)
  ✅ T1f 無變 ⇒ 真 st 之街角選位⛔ 重跑（恰一）：得 1　期 1
  ✅ T1g 合併再試之輸入：宗地 ＝ 段三之出（此出口 ＝ 原宗地）：得 (True, True)　期 (True, True)
  ✅ T1h 合併再試之輸入：上鎖 ＝ 末一次真 st 街角選位之段一上鎖、街角第 1 宗 ＝ 其 winners、街廓／中心線／退縮／歸戶：得 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})　期 ({'D(1)'}, {'A(1)'}, {'B1': {'category': '住宅區'}, 'RD': {'category': '道路'}}, {'RD': [(0.0, -5.0), (50.0, -5.0)]}, 3.5, {'A': 'g1', 'B': 'g2', 'C': 'g3', 'D': 'g1'})
  ✅ T1i alloc_eval 回試算配地之評選（深拷貝）：得 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False)
  ✅ T1c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T1c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T1c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T1c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T2a 段三旗標 off 之出口：正常結束、ran False：得 (True, False)　期 (True, False)
  ✅ T2b 合併再試恰一次、段三本體⛔ 呼：得 (1, 0)　期 (1, 0)
  ✅ T2c 有變 ⇒ 回傳之宗地 ＝ 合併再試之出（同一物件）：得 (True, True)　期 (True, True)
  ✅ T2d 紀錄與逐列入 session：得 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])　期 ({'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}, [{'序': 1, '街廓': 'B1', '端': '右', '候選': 'B(1)', '結果': '成'}])
  ✅ T2e 配地所用之宗地 ＝ 合併再試之出（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T2f 所存之結果繫於段三前之宗地與退縮（他 build 或他退縮 ⇒ loud）：得 (('raise', True), ('raise', True))　期 (('raise', True), ('raise', True))
  ✅ T2g 有變 ⇒ 真 st 之街角選位重跑一次、所用 ＝ 合併再試之出：得 (2, True)　期 (2, True)
  ✅ T2h 無停機訊息：得 None　期 None
  ✅ T2c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T2c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T2c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T2c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T3a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  ✅ T3b 段三本體與合併再試各恰一次：得 (1, 1)　期 (1, 1)
  ✅ T3c 段三之試算配地亦 'trial'：得 ['trial']　期 ['trial']
  ✅ T3d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}
  ✅ T3e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (True, True, {'C(1)'})　期 (True, True, {'C(1)'})
  ✅ T3f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T3g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T3h 紀錄入 session：得 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}　期 {'標的': [['B1', 'right']], '皆未達': {}, '退縮': 3.5}
  ✅ T3i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (2, True)　期 (2, True)
  ✅ T3j 無停機訊息：得 None　期 None
  ✅ T3c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T3c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T3c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T3c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T9a 段三實辦之出口：正常結束、ran True、段三紀錄：得 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])　期 (True, True, [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'序': 1, '街廓': 'B1', '端': '左', '候選': 'A(1)', '結果': '成'}], [{'最終序位': 1, '街廓': 'B1', '端': '左', '暫編地號': 'A(1)'}])
  ✅ T9b 段三本體與合併再試各恰一次：得 (1, 1)　期 (1, 1)
  ✅ T9c 段三之試算配地亦 'trial'：得 ['trial']　期 ['trial']
  ✅ T9d 段三之 alloc_state 之出：得 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}　期 {'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}
  ✅ T9e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位：得 (True, True, {'C(1)'})　期 (True, True, {'C(1)'})
  ✅ T9f 回傳之宗地 ＝ 末態（同一物件）：得 (True, True)　期 (True, True)
  ✅ T9g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）：得 (True, True)　期 (True, True)
  ✅ T9h 紀錄入 session：得 {'退縮': 3.5, '標的': [], '皆未達': {}}　期 {'退縮': 3.5, '標的': [], '皆未達': {}}
  ✅ T9i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）：得 (1, True)　期 (1, True)
  ✅ T9j 無停機訊息：得 None　期 None
  ✅ T9c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T9c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T9c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫：得 'real'　期 'real'
  ✅ T9c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T4a 合併再試停機 ⇒ 畫面 st.error ＋ st.stop：得 ('_Stop', True)　期 ('_Stop', True)
  ✅ T4b 停機訊息入 session（含合併再試之原訊息）：得 True　期 True
  ✅ T4c 其後之配地 loud（k6b_stage3_selected raise「請重跑」；k6b_screen_build_for_g ⇒ st.stop）：得 (('raise', True), 'st.stop')　期 (('raise', True), 'st.stop')
  ✅ T4d 前次之紀錄已去、本次⛔ 寫：得 ('<缺>', '<缺>')　期 ('<缺>', '<缺>')
  ✅ T4c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T4c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T4c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T5a 合併再試中斷（KeyError）⇒ 例外上拋：得 'KeyError'　期 'KeyError'
  ✅ T5b 未完成之標記留存（其文含「末端塊合併再試」）：得 True　期 True
  ✅ T5c 其後之配地 loud（k6b_stage3_selected raise「請重跑」）：得 ('raise', True)　期 ('raise', True)
  ✅ T5d 前次之紀錄已去：得 '<缺>'　期 '<缺>'
  ✅ T5c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T5c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T5c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ T8a 段三停機 ⇒ st.stop；合併再試⛔ 辦：得 ('_Stop', 0)　期 ('_Stop', 0)
  ✅ T8b 前次之紀錄已去（⛔ 殘留舊紀錄）：得 ('<缺>', '<缺>')　期 ('<缺>', '<缺>')
  ✅ T8c 停機訊息含段三之原訊息：得 True　期 True
  ✅ T8c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）：得 False　期 False
  ✅ T8c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）：得 (['SENT_G'], {'SENT': 1}, {'SENT': 1})　期 (['SENT_G'], {'SENT': 1}, {'SENT': 1})
  ✅ T8c4 試算配地皆 'trial'（其數 ≥ 1）：得 (True, ['trial'])　期 (True, ['trial'])
  ✅ TK 試算隔離之鍵含 SS_END_BLOCK_MODE 之值、末項仍 f3_k929_6_log：得 (True, True)　期 (True, True)
  ✅ T6a 四注入物之名：得 ['a_prime', 'alloc_eval', 'alloc_state', 'trial_winner']　期 ['a_prime', 'alloc_eval', 'alloc_state', 'trial_winner']
  ✅ T6b a′ ＝ a(src) × p(src) ÷ p(dst)（100 × 1000 ÷ 500）：得 200.0　期 200.0
  ✅ T6c 試算選位回 (winner, 真G, 門檻)：得 ('A(1)', 123.45, 100.0)　期 ('A(1)', 123.45, 100.0)
  ✅ T6d 試算配地（alloc_state）之出與其 'trial'：得 ({'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}, ['trial'])　期 ({'kept': {'B1': {'A(1)'}}, 'bad_pools': {}, 'err': None}, ['trial'])
  ✅ T6e 試算配地（alloc_eval）回評選之深拷貝、其 'trial'：得 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False, ['trial'])　期 ({'B1': {'left': {'觸發': True, 'R_end(㎡)': 50.0, '候選': [], '當選': 'A(1)'}}}, False, ['trial'])
  ✅ T6f 試算配地中止（st.stop）⇒ alloc_eval 拋 RuntimeError：得 'RuntimeError'　期 'RuntimeError'
  ✅ T7a 逐列 ＝ 紀錄之列（值一律字串·None ⇒ —）：得 [{'序': '1', '街廓': 'RB', '端': '右', '候選': 'P(3)', '結果': '成', '檢核': '—'}, {'序': '後處理', '街廓': 'RB', '端': '右', '候選': 'P(4)', '結果': '成', '檢核': '通過'}]　期 [{'序': '1', '街廓': 'RB', '端': '右', '候選': 'P(3)', '結果': '成', '檢核': '—'}, {'序': '後處理', '街廓': 'RB', '端': '右', '候選': 'P(4)', '結果': '成', '檢核': '通過'}]
  ✅ T7b 行內載標的之街廓與端、競合之候選與交面積、皆未達 ⇒ 強制抵費地、退縮：得 []　期 []
  ✅ T7c 無標的 ⇒ 行含「無標的」、逐列空：得 (True, [])　期 (True, [])
  ✅ T7d 試算中止 ⇒ 行含「試算中止」與其訊息：得 (True, True)　期 (True, True)
  ✅ T7e 無紀錄 ⇒ 空：得 {'lines': [], 'rows': []}　期 {'lines': [], 'rows': []}
  ✅ TS 三介面之簽名：得 [(['st'], ['g_kwargs', 'pk_kwargs']), (['st'], ['g_kwargs', 'pk_kwargs']), (['rec', 'log'], [])]　期 [(['st'], ['g_kwargs', 'pk_kwargs']), (['st'], ['g_kwargs', 'pk_kwargs']), (['rec', 'log'], [])]
── P0 判式自驗（期值記錄須全綠；逐項擾動須恰該項紅）──
  ✅ P0 期值記錄全綠 True；逐項擾動恰該項紅 86／86
⇒ 紅 []；rc 0
```

`F14 run`（驗）全文：

```text
── F13 之判式施於畫面路徑（R1 本案·C／F／X 合成案甲乙丙）──
  ✅ R1 退縮 3.5：合併再試紀錄 {'退縮': 3.5, '標的': [], '皆未達': {}}（⛔ 載競合）；逐列 0
  ✅ R1 退縮 0.0：合併再試紀錄 {'退縮': 0.0, '標的': [], '皆未達': {}}（⛔ 載競合）；逐列 0
══ 合成案甲（退縮 3.5·注入 末端帶寬 [8.0, 16.0]、上鎖 0、假設跨占街角 []·咬到 {'host': 0, 'merge': 0, 'geo': 90}）══
  ✅ C甲 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 237.57]]}]；外部錨之交面積 R3 左 66.49／R5 右 237.57
  ✅ F甲 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X甲：逐列 [('628(4)', '②', '未成', '—'), ('628(3)', '②', '未成', '—'), ('628-34(2)', '—', '未成', '—'), ('628-23(2)', '①', '成', '免'), ('628-22(2)', '—', '略·已定案', '—')]；後處理 [('628-23(3)', '後處理(b)', '成', '628-23(2)'), ('628-22(3)', '後處理(b)', '成', '628-23(2)')]；二片皆全在中心線之一側 True；R5 右鏈首宗 628-23(2) G 1422.89 ＝ 外部錨 1422.89；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案乙（退縮 3.5·注入 末端帶寬 [8.0, 5.5]、上鎖 6、假設跨占街角 ['628-23(2)']·咬到 {'host': 48, 'merge': 1, 'geo': 96}）══
  ✅ C乙 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 217.29]]}]；外部錨之交面積 R3 左 66.49／R5 右 217.29
  ✅ F乙 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X乙：逐列 [('628(3)', '②', '成', '通過'), ('628(4)', '②', '未成', '—'), ('628-34(2)', '—', '未成', '—')]；後處理 [('628(4)', '後處理(a)', '成', '628(3)')]；R5 右鏈首宗 628(3) G 408.48 ＝ 外部錨 408.48；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
══ 合成案丙（退縮 3.5·注入 末端帶寬 [8.0, 5.0]、上鎖 6、假設跨占街角 ['628-23(2)']·咬到 {'host': 45, 'merge': 1, 'geo': 90}）══
  ✅ C丙 競合 ＝ [{'形': '一', '列': [['R3', '左', '628(4)', 66.49], ['R5', '右', '628(3)', 207.25]]}]；外部錨之交面積 R3 左 66.49／R5 右 207.25
  ✅ F丙 R3 左強制抵費地 R3-抵費地-2（351.7·外部錨末端帶 351.70）；宗地 ∩ 帶 0.000000；聯集 △ 街廓 0.0001、兩兩疊 0.0000
  ✅ X丙：逐列 [('628(3)', '②半', '成', '通過'), ('628(4)', '②半', '未成', '—'), ('628-34(2)', '—', '未成', '—')]；後處理 [('628(4)', '題一 4', '成', '628(3)')]；切半之量 {'628(6)': 170.7953}／{'628(6)': 170.9947} ＝ 外部錨 170.7953／170.9947（R5 側之比 0.4997）；R5 右鏈首宗 628(3) G 408.48 ＝ 外部錨 408.48；R5 聯集 △ 街廓 0.0000、兩兩疊 0.0000
⇒ 紅 []；rc 0
── E：畫面路徑之專項 ──
  ✅ E@3.5：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@0.0：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@3.5·甲：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@3.5·乙：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
  ✅ E@3.5·丙：試算旗標⛔ 外洩 True；配地所用之宗地 ＝ 合併再試後 True；無停機訊息 True
⇒ 紅 []；rc 0
```

`python verify/probes/probe_WG9343_step0_flag.py runall <O>\runall_pre.log <O>\runall_post.log`（`rc 0`）全文：

```text
【runall】項 64／64·PASS 28 → 28·FAIL 36 → 36
  相異項 0；其餘 64 項之名目、狀態、違規數與本體逐項同
  末端夾具／golden 列：21／21·相異 0
  對帳段（【對帳】起·⛔ 入本體）：名目 凍存／現況 22／36 → 22／36；含「對帳 FAIL」True → True
  末列：W-V run_all: FAIL ｜ W-V run_all: FAIL
```

`diff <O>\runall_pre.log <O>\runall_post.log` ⇒ `rc 0`、輸出 `0` 列（空）。

### ③-3　`parity` 四份之末十列

```text
=== parity35_pre.log（末十列）===
  🔴 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（57／57）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 1（不符 2 項）
=== parity00_pre.log（末十列）===
  🔴 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（61／61）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 1（不符 2 項）
=== parity35_post.log（末十列）===
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（57／57）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
=== parity00_post.log（末十列）===
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（61／61）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
```

## ④ 五塊之實得與三檔之改前改後

| 塊 | bytes | `sha256` | 列 | 落點 |
|---|---|---|---|---|
| `F14` | `35946` | `324a15099b6e5cbe75872e3f6e426d47877f955748d921b30d33358b80cd38a1` | `736` | 新檔 `verify/probes/probe_WG9355_screenmerge.py`（blob `3648cd6c…`） |
| `F4p` | `4752` | `afbe07170647acbd624788dab2d0e49930a9c96d259cfa5216945467584c400b` | `59` | `git apply` 於 `verify/probes/probe_WG9345_screen.py`（`790060dc…`·`48501` B → `92f9dc4d…`·`49785` B） |
| `E5` | `1957` | `51c97be27c199c6f2bab0642fba54a9f6b1972de9e1cc40ceafb12fc729fb500` | `12` | 自誤簿之末 |
| `P9` | `4110` | `42e0521fd381e9670a1b4e38582e8bb5efc31215b99c8fd3aa0d08671c76ee59` | `22` | `CLAUDE.md` 之末 |
| `H1` | `3065` | `ce0956460049bfe456c54a2c1ef4e6f0f0aa7588a70ddaec3e324736ca60cfdc` | `31` | 恆常附款登記表之末 |

抽取 ＝ 依圍欄之逐列索引（開列之次列至閉列之前一列，`\n` 相接、末附 `\n`、UTF-8）；圍欄於本單之列：`F14` `253`–`990`、`F4p` `994`–`1054`、`E5` `1058`–`1071`、`P9` `1075`–`1098`、`H1` `1102`–`1134`。

| 檔 | 改前 B | 改後 B | 嚴格前綴 | `CR` |
|---|---|---|---|---|
| `docs/reports/W-G.9波_claude.ai側自誤登記.md` | `1075505` | `1077462` | ✅ | `0` |
| `CLAUDE.md` | `291243` | `295353` | ✅ | `0` |
| `docs/reports/W-G.9波_恆常附款登記表.md` | `59311` | `62376` | ✅ | `0` |

併驗：塊 `P9` 之自載「`⬜` 字樣 ＝ `10`（子字串框）·列 ＝ `8`（列框）」——實算 `10`／`8` ✅。工項三 `commit` 後 `python verify/probes/probe_WG9270_closegate.py 548 547 .` ⇒ `rc 0`（新號 `548` ∈ 定義框·`MAX` ＝ `548`·缺號集同開工態）。

## ⑤ 推送之目標與推後之遠端 heads

| 工項 | 目標 | 推送 |
|---|---|---|
| 零 | `HEAD:verify/W-G.9-353-endmerge` | `f55935c..31f03d3`（快轉） |
| 一 | 同 | `31f03d3..167e475`（快轉） |
| 二 | 同（`V-1`〜`V-6` 皆符之後·與驗為分開之呼叫） | `167e475..f173a4e`（快轉） |
| 三 | 同 | `f173a4e..b1d3d3b`（快轉） |
| 四 | 同 | 見對話 |

工項三推後之 `git ls-remote --heads origin`（`31` 列）：

```text
a18bb57064a308c8eddaa8b6d2a354681a67b844	refs/heads/claude/wg9-95z-v3-resume-hgpzfs
6cb77b7f0c08e2edf62f8e9cd239efa774a98d95	refs/heads/main
b772f8aa09820f01312081588fd8c8d718c8ac86	refs/heads/verify/W-G.9-198R-c1
a1107a17825c37430f69349afaceef4d09c6f5f8	refs/heads/verify/W-G.9-198R-c2
6e677223e4ab2823f1a2d276bc5635472b4d51a7	refs/heads/verify/W-G.9-198R-c3
8b0534c451a45a8d066e7bbc98a6ee7d67323432	refs/heads/verify/W-G.9-219R2-c1
20b04ac8caa137108b24ecc0d27253076f43adcb	refs/heads/verify/W-G.9-229-c1
845d08db3cb63fa6562ebdf6459c56629de5f6b4	refs/heads/verify/W-G.9-243-c1
6b5fe718a0d53d07b86a460d520037affa555a1b	refs/heads/verify/W-G.9-244-c1
1a6a357aa797e06cfd8f60db9fa6a6a032a221f8	refs/heads/verify/W-G.9-244-c2
29ebc141aab5e1fa49d1712dbb8322c54109497e	refs/heads/verify/W-G.9-246-c1
910d5e785a301c0e6564bab30c9b376b8bda5143	refs/heads/verify/W-G.9-247-c1
2709504b2aad9f4924d4182ef37e3d47d861767e	refs/heads/verify/W-G.9-248-c1
3242e962f52aa1f170cb69c6b2db28a666c2994f	refs/heads/verify/W-G.9-255-c1
e9d1b9c3e6e46580da28392e1ed7495d5b34638f	refs/heads/verify/W-G.9-261-c1
36385ef061591b5366b3295061efaa15f3a18b21	refs/heads/verify/W-G.9-268p-c1
95a530c187ca8f6b15581a1250e2a72dcfe7eb6d	refs/heads/verify/W-G.9-268p-c2
363602b874992e30aaea72576e536cf1cedba657	refs/heads/verify/W-G.9-268p-c3
2f1292748d1326f1590ae20d5d18dd8f5364af5b	refs/heads/verify/W-G.9-269-c1
dc373d018fa04a2a2538d04b6b194a1dfb4dcd3d	refs/heads/verify/W-G.9-269-c2
ce06622f2caa8e0f3bac03c347c7e041e84b73b4	refs/heads/verify/W-G.9-269-c3
05a11bd665f6c2790ff821c9e3a1606651e345d4	refs/heads/verify/W-G.9-269-p3a
488c4858da63ebe370ed950788947aa742eb44ad	refs/heads/verify/W-G.9-299-gb170
be5108d0067e63e23a397fdcbe43358800381470	refs/heads/verify/W-G.9-333-gb168
2ec1eb2bf43616ce662d95dc633b4c71f366eb15	refs/heads/verify/W-G.9-338-origin
d0add71ff85e62c2afb1f2f5d327c4488624c4a1	refs/heads/verify/W-G.9-341-gb182
14e022265bd1c190d7d6f9c1a0c6900bcec120db	refs/heads/verify/W-G.9-343-k929b
b1d3d3b7977d455f0239bc4768975137f30ce2e0	refs/heads/verify/W-G.9-353-endmerge
886645475b60f790c06d52333501e917596c28be	refs/heads/wip/W-G.4-S0b-S0c
c286a79cc6a699c57c7763306c4beae9ef7b60a3	refs/heads/wip/W-G.9-318-preserve
0b05925374f2de46c2493f5f56ef64667a2fed1d	refs/heads/wip/s1-endpart
```

## ⑥ CC 之自捕與自解

**自捕**

1. **開場自報 context 餘量（`§零-0` 項 `1`）未先於工項零於對話出艙**——開場時工具之計數器示 `14,782,697` tokens 餘；本項照實補記於此。
2. **本機之 heredoc 守門器**（`verify/tools/wg9237_heredoc_guard.py`·PreToolUse hook）擋下首版之抽取命令（其以 heredoc 內聯 Python）⇒ 改以檔案落地再以路徑呼叫；同一被擋之命令內含 `mkdir` ⇒ 次次抽取因輸出目錄不在而拋 `FileNotFoundError`（**未寫出任何檔**）⇒ 建目錄後重跑。抽取結果與 `§五-1` 逐位同。
3. **`V-4` 之殼迴圈（試跑·`commit` 前）** 對 `probe_WG9330_wfns_ast.py`／`probe_WG9340_main_synth.py` 二器以其第一引數（`<repo>` 之絕對路徑）組成輸出檔名 ⇒ 重導失敗、二器**未執行**而印 `rc=1` ⇒ **量測器（本機之殼）紅、⛔ 受詞紅**；改以固定檔名單獨重跑 ⇒ 皆 `rc 0`。正式之 `V-4`（於 `commit`）以固定檔名跑。
4. **`run_all` 之 `rc 1`**：本分支為准紅碼（`CLAUDE.md` 分支狀態宣告）⇒ 其 `rc` 恆 `1`；驗收以 `V-5` 之逐項對拍為之（相異 `0`）。
5. **開發中之試跑**：`commit` 前以同一內容先跑 `F14 selftest`（`rc 0`）與 `F14 run`（`rc 0`·`916` s）；`commit` 後之正式 `V-1` `run` 輸出與試跑**逐位相同**（`diff` 空）。
6. **本報告 ⑧ 之「內嵌 ＝ `git diff` 原檔」之驗**：首版驗式以圍欄開列之長度少算 `1`（`8` 應為 `9`）⇒ 印 `False` ＝ **量測器紅**；改以 `len(開列)` 取界後 ⇒ `True`（`20521` B 逐位同），另以擾動一位元組之對照 ⇒ 不等（驗式非恆綠）。

**自解清單**（`作業常規之追加五`·五項齊備）

| # | 疑義逐字 | 讀法 | 所取 | 機械證據 | 所棄之由 |
|---|---|---|---|---|---|
| `1` | `R-11`「段三實辦者，段三之未完成標記延至合併再試正常完成始撤」 | 甲：session 鍵 `f3_k6b_stage3_error` 於段三開始至合併再試正常完成之間**恆在**（段三成後其文由 `K6B_STAGE3_PENDING` 換為 `K6B_ENDMERGE_PENDING`）；乙：其**文**亦須保持段三之標記至合併再試完成 | 甲 | 單鍵只容一文，乙與同條前段「合併再試開始前…其文含『末端塊合併再試』」**互斥**；甲兩者皆滿足。二讀法之後果皆為「其後之配地 loud」（`k6b_stage3_selected` 見非空即拋），**僅訊息文字相異 ⇒ 零土地後果**。`F14 selftest` `T3j`／`T9j`／`T5b` ✅；`F6 run` C0〜C6 ✅ | 乙與同條前段互斥（白名單 `6`：單內二處自相矛盾而二讀法皆不動土地 ⇒ 取較嚴者；甲之「鍵恆在」即 fail-closed 之較嚴者） |
| `2` | `P-4` 提示 `4` 項（pre-flight） | — | 採單 `§五-1` 項 `9` 之具名豁免（`:69`／`:178`／`:201`／`:1083`） | 本機實跑 `rc 0`·🔴 `0`／🟡 `4`／ℹ️ `2`，與單載逐項同 | —（發單側已具名豁免） |

## ⑦ 設計說明（`§三-5`）

### ⑦-1　逐 `R-1`〜`R-13`：落於何函式、何處

| # | 落點 | 要旨 |
|---|---|---|
| `R-1` | `f3_screen_k6b_stage3` 之內層 `_end_merge`（三出口共用之末段）→ `f3_screen_end_block_merge` → `end_block_merge_run` | 三個正常出口（① 旗標 off ／ ② 段二序為空 ／ ③ 段三實辦而成）皆於其真 st 之 `f3_screen_corner_pk_run(st, …)` 之後 `return _end_merge(…)`；`end_block_merge_run` 以模組層之名呼叫（⛔ 別名、⛔ 預綁；其解析經函式之 `__globals__` ＝ harvest 之 `ns`，故 `F14 run` 之包裹得以咬到）。輸入之宗地：① ② ＝ `temp0`／`build0`（入口之輸入）；③ ＝ `temp2`／`build2`（段三之出）。段三停機（`except RuntimeError` 之 `st.stop()`）與任何上拋皆先於 `_end_merge` ⇒ 合併再試⛔ 辦 |
| `R-2` | `f3_screen_end_block_merge` 之首段 | 上鎖 ＝ `f3_k6b_stage1_locked_by_block` 各值之聯集；街角第 1 宗 ＝ `f3_corner_winners` 各值（dict）之值中之非空者（`str`）；街廓 ＝ `{label: {'category': …}}`（`g_kwargs['classified_blocks']`）；中心線 ＝ `f3_manual_road_centerlines`；歸戶 ＝ `t8_ownership_map`；`setback=` ＝ `f3L_setback_default`。皆於該函式之首（＝ 呼叫端之真 st 街角選位之後、任何試算之前）讀之——與 harness `run_end_block_merge` 逐式同構 |
| `R-3` | `k6b_screen_callbacks` 之內層 `alloc_eval` | 代理 st（`_K6BTrialSt`）跑 `f3_screen_corner_pk_run` → 無 winners 表 ⇒ `RuntimeError` → 設 `SS_END_BLOCK_MODE ＝ 'trial'` → `f3_screen_stepg_run`；`_K6BTrialDone` ⇒ 成；`_K6BTrialStop` ⇒ 轉拋 `RuntimeError`；`RuntimeError` 直接上拋；另於配地後驗 `f3_G_values` 在（配地本體於其首 `pop`、於其末寫，故「在」＝ 配地跑畢）——⛔ 在 ⇒ `RuntimeError`。回 `SS_END_BLOCK_EVAL` 之 `deepcopy`（試算前先 `pop` 之，使⛔ 讀到前次之殘值） |
| `R-4` | `k6b_screen_callbacks` 之內層 `alloc_state` | 於街角選位之後、`f3_screen_stepg_run` 之前加一句 `_ss[SS_END_BLOCK_MODE] = 'trial'`（位置同 harness `_k6b_callbacks`） |
| `R-5` | 🆕 模組層 `k6b_screen_callbacks(st, *, pk_kwargs, g_kwargs)` | `_p_of`／`a_prime`／`_copy_pair`／`trial_winner`／`_cat_of`／`_prow`／`alloc_state` 自本批前之 `f3_screen_k6b_stage3` 之「5. 三注入物」段**原封搬出**；對拍（自原段之 `_ppz = …` 起至 `alloc_state` 之 `return` 止）之差 ＝ **恰 `R-4` 之一列**（⑧ 之 `@@ -19454` 一塊）。段三（`f3_screen_k6b_stage3` 之 5.）與合併再試（`f3_screen_end_block_merge`）各呼此工廠一次 |
| `R-6` | `f3_screen_end_block_merge` 之 `try／finally`；`K6B_SCREEN_TRIAL_KEYS` | 試算前存 `K6B_SCREEN_TRIAL_KEYS` 之鍵（`deepcopy`）與 `K917_DROPPED`，`finally` 中復原（原無之鍵 ⇒ `pop`）——與段三之隔離逐式同構。`K6B_SCREEN_TRIAL_KEYS` 增字串字面 `'f3_end_block_mode'`（插於 `# 🆕 W-G.9-349` 註與 `'f3_k929_6_log',` 之前） |
| `R-7` | `f3_screen_end_block_merge`（`finally` 之後）；`f3_screen_k6b_stage3` 之「1.」 | 復原之後寫 `SS_END_BLOCK_MERGE ＝ rec`、`'f3_end_block_merge_log' ＝ log`。入口之首去前次之二鍵；`f3_screen_end_block_merge` 之首亦去之（其單獨被呼時亦⛔ 殘留） |
| `R-8` | `f3_screen_end_block_merge` 之末；`_end_merge` 之 `return` | `temp3 is not temp_in` ⇒ 以真 st 再跑一次 `f3_screen_corner_pk_run`（所用 ＝ 合併再試之出）；無變 ⇒ ⛔ 重跑。入口之回傳 `temp`／`build` ＝ `_em['temp']`／`_em['build']`（無變即該出口之宗地之同一物件）；鍵仍 `temp／build／log／order／ran`、`log` ＝ 段三之紀錄 |
| `R-9` | `_end_merge` | `ran or _em['temp'] is not temp_x` ⇒ 存 `f3_k6b_stage3_temp`／`_build` ＝ 末態、`f3_k6b_stage3_fp ＝ k6b_stage3_fingerprint(build0, _ss['f3L_setback_default'])`（`build0` ＝ 入口之輸入 ＝ 段三前）；二者皆無 ⇒ ⛔ 存 ⇒ `k6b_stage3_selected` 回 `None`。`k6b_stage3_selected`／`k6b_screen_build_for_g` 本身⛔ 動 |
| `R-10` | `f3_screen_end_block_merge` 之 `except RuntimeError` | `f3_k6b_stage3_error ＝ '（末端塊合併再試）' ＋ 原訊息之首列`（首列截 `500` 字）；`st.error(原訊息)` ＋ `st.stop()` ＋ `raise`（同段三之停機）；`finally` 仍復原。其後 `k6b_stage3_selected` 見停機訊息 ⇒ `RuntimeError`「請重跑」；`k6b_screen_build_for_g` ⇒ `st.stop()` |
| `R-11` | 模組層常數 `K6B_ENDMERGE_PENDING ＝ '「末端塊合併再試」未完成（執行中斷）'`；`_end_merge` | `_end_merge` 之首設 `f3_k6b_stage3_error ＝ K6B_ENDMERGE_PENDING`，唯合併再試正常返回且末態已存之後 `pop` 之。段三實辦者，段三之 `K6B_STAGE3_PENDING` 於段三正常完成之後**⛔ 撤**，而由本標記**接替**（標記鍵自段三開始至合併再試正常完成恆在）。非 `RuntimeError` 之例外（含真 st 之 `st.stop`）⇒ 上拋、標記留存 |
| `R-12` | 🆕 模組層 `end_block_merge_rows(rec, log)`（置於 `end_block_eval_rows` 之後）；`main()` 成果區；`main()` 之 `_f3L_invalidate_g_cache` | 見 ⑦-2；`main()` 之顯示置於「🧱 末端塊之評選」之 `if` 句之後、`# 🆕 W-G.9-351` 註與 `_adj351_bf =` 之前（`rec is None` ⇒ ⛔ 顯示）；失效函式於段三鍵之迴圈之後增 `pop(SS_END_BLOCK_MERGE)`、`pop('f3_end_block_merge_log')` |
| `R-13` | — | `verify/**` 一字未動（`V-6`：相異 `0`）；`end_block_*`（既有）／`k6b_stage3_run`／`k6_merge_groups`／`solve_G_binary`／`_solve_G_one`／`k929_6_fixpoint`／`f3_screen_corner_pk_run`／`f3_screen_stepg_run`／`_k929_6_screen_gate` 皆不在 ⑧ 之 hunk 內 |

### ⑦-2　`§三-4` 末之實作細節之選擇及其由

1. **合併再試之呼叫以入口之內層 `_end_merge` 為之**（三出口共用一段末段）——由：三出口之「立標記 → 合併再試 → 存末態 → 撤標記」完全相同，寫三次即三處可漂移；內層函式⛔ 含 `k6b_stage3_run(` 字樣（`X-5`）。
2. **未完成之標記由呼叫端（`_end_merge`）立、撤；`f3_screen_end_block_merge` 只於 `RuntimeError` 時寫停機訊息**——由：「撤」須在「末態已存」之後方為 fail-closed（撤而未存之間若中斷，其後之配地將靜默取段三前之宗地）；而末態之存（指紋須段三前之 `build0`、及「段三是否實辦」）只有入口知道。故標記之生命週期置於入口，與段三之 `K6B_STAGE3_PENDING` 同處。
3. **「有變」之判 ＝ `temp` 之物件同一性**（`temp3 is not temp_in`）——由：同 harness `run_corner_pk_k6b` 之 `if temp3 is not temp2`（`F4 parity` 之對拍前提）；`end_block_merge_run` 無變時回其輸入之同一物件（二者同）。
4. **有變之真 st 重跑置於 `f3_screen_end_block_merge` 之末**（其出即合併再試之出）；入口之 `_end_merge` 於其返回之後方存末態、撤標記 ⇒ 重跑中止（真 st 之 `st.stop`）亦使標記留存。
5. **`alloc_eval` 加驗「配地跑畢」**（`'f3_G_values' in session`）——由：`end_block_merge_run` 之契約為「配地中止 ⇒ `raise`」；配地本體若未以 `st.rerun()` 結束而返回，則其評選不可信 ⇒ loud（體例同 `_k929_6_screen_gate._trial`）。本案實跑⛔ 觸之。
6. **`alloc_eval` 試算前 `pop(SS_END_BLOCK_EVAL)`**——由：使回傳之評選必為本趟所寫（配地本體之非入池閘試算趟亦於其首 `pop` 之，二者同向）；該鍵 ∈ `K6B_SCREEN_TRIAL_KEYS` ⇒ 復原後回到試算前之值。
7. **合併再試之「未處置」訊息（`log_print`）**：收集後於復原之後以 `st.error` 逐條顯示——體例同段三之 `_unhandled`。
8. **停機訊息之措辭**：`R-10` 之 session 值前綴「（末端塊合併再試）」——由：合併再試內部亦經 `k6b_stage3_run`（其訊息以「[K-6-B 段三]」起首），前綴使 `k6b_stage3_selected` 之「前次…停機：…」可辨其出處；原訊息之首列全文保留（「含原訊息」）。`alloc_eval` 之訊息以「🔴 [末端塊合併再試·畫面]」起首。
9. **`end_block_merge_rows` 之行之形**：首行 `退縮 <值> m`；有 `試算中止` ⇒ 一行「試算中止：<訊息>（…）」；`標的` 非 `None` ⇒ 空則一行「無標的（…）」、否則一行「標的（…）：<街廓> 左端、…」；競合逐組一行「競合 i（形<形>）：<街廓> <端>端 候選 <候選> 交 <x.xx> ㎡ ／ …」；皆未達逐端一行「<街廓> <端>端：合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）」。顯示之 expander 於有逐列時預設展開（同 `f3_k929_6_log` 之體例）。
10. **`end_block_merge_rows` 之位置 ＝ 緊接 `end_block_eval_rows` 之後**（末端塊顯示二純函式相鄰）；新函式⛔ 改任何既有 `end_block_*` 之一字。

### ⑦-3　對 `§三-3` 各款之自查

| 款 | 判 | 據 |
|---|---|---|
| `X-1` | 未觸 | ⑧ 無 `main()` 二按鈕 `If` 之 hunk；`F4 wiring` `W1`／`W2` ✅、突變 `m1`／`m2` 轉紅 |
| `X-2` | 未觸（增列） | 失效函式之 `K6B_SCREEN_STAGE3_KEYS + ('f3_k6b_stage3_error',)` 一字未動、其後增二 `pop`；`F4 wiring` `W3` ✅、`m4` 轉紅 |
| `X-3` | 未觸 | 新鍵為字串字面 `'f3_end_block_mode'`、插於 `'f3_k929_6_log',` 之前（其前另有 `# 🆕 W-G.9-349` 註列）；`'f3_k929_6_log',` 與 `)` 二列一字未動；`F9 wiring` `W4` ✅（突變 `M1` 錨 `"    'f3_k929_6_log',\n)"` 仍唯一）、`F10 wiring` `W3` ✅、`F11 wiring` `W7` ✅；`F14 selftest` `TK` ✅ |
| `X-4` | 未觸 | `_eb352 = …`／`end_block_eval_rows(_eb352)` 二句一字未動；新區塊插於 `# 🆕 W-G.9-351` 註之前，`_adj351_bf =` 與其次句 `if` 仍相鄰；`F11 wiring` `W10` ✅、`F10 wiring` `W5` ✅ |
| `X-5` | 未觸 | 入口之 docstring 與內層 `_end_merge` 皆⛔ 含 `k6b_stage3_run(` 字樣 ⇒ 首個即段三之呼叫；其後至 `finally:` 之間⛔ 含 `contests`；`F13 wiring` `W3` ✅ |
| `X-6` | 未觸 | 三新函式與入口⛔ 引 `SS_ADJ_BUILD_FINAL`／`SS_ADJ_DROPPED`／`adj_intake`／`adj_intake_rows`／`'f3_k929_6_build'`／`'f3_k929_6_dropped'`；`F10 wiring` `W4` ✅ |
| `X-7` | 未觸 | `_WF_NS_NAMES` 無 hunk；`wfns_ast` `48`／`48`／`47` |
| `X-8` | 未觸 | `R-13` 之函式無 hunk；`F9`〜`F13 wiring` 全綠且其突變皆轉紅；`main_synth` `rc 0` |

## ⑧ `app.py` 之全文差異

`git diff 167e475d480c657fa3d0ff27189b16ee278dbb2d f173a4e2a54d1ae036e14ecc35e88d0a9befdf31 -- app.py`（`336` 列·`20521` B）：

````diff
diff --git a/app.py b/app.py
index dc3e52b..e11232a 100644
--- a/app.py
+++ b/app.py
@@ -10768,6 +10768,32 @@ def end_block_eval_rows(ev):
     return {'lines': lines, 'rows': rows}
 
 
+def end_block_merge_rows(rec, log):
+    """🆕 `W-G.9-355`：末端塊合併再試（`end_block_merge_run` 之 `rec`／`log`）之顯示（純函式）。
+    回 `{'lines': [...], 'rows': [...]}`：`rows` ＝ `log` 之逐列（鍵同 `log`、值一律字串·`None` ⇒ `'—'`）；
+    `lines` 載退縮、標的逐端、競合逐組、皆未達逐端；`rec` 為 `None` ⇒ 皆空。"""
+    if rec is None:
+        return {'lines': [], 'rows': []}
+    _nm = {'left': '左', 'right': '右'}
+    lines = [f"退縮 {rec.get('退縮')} m"]
+    if rec.get('試算中止') is not None:
+        lines.append(f"試算中止：{rec.get('試算中止')}（未取得標的；定案之配地遇各筆單獨皆未達之端將停機）")
+    _tg = rec.get('標的')
+    if _tg is not None:
+        if _tg:
+            lines.append("標的（各筆單獨皆未達之末端塊）：" + "、".join(f"{_b} {_nm.get(_s, _s)}端" for _b, _s in _tg))
+        else:
+            lines.append("無標的（無各筆單獨皆未達之末端塊）")
+    for _i, _c in enumerate(rec.get('競合') or [], 1):
+        lines.append(f"競合 {_i}（形{_c.get('形')}）：" + " ／ ".join(
+            f"{_b} {_e}端 候選 {_p} 交 {float(_a):.2f} ㎡" for _b, _e, _p, _a in (_c.get('列') or [])))
+    for _b in sorted(rec.get('皆未達') or {}):
+        for _s in (rec['皆未達'][_b] or []):
+            lines.append(f"{_b} {_nm.get(_s, _s)}端：合併再試皆未達 ⇒ 強制抵費地（面積 ＝ R_end）")
+    rows = [{_k: ('—' if _v is None else str(_v)) for _k, _v in _r.items()} for _r in (log or [])]
+    return {'lines': lines, 'rows': rows}
+
+
 def end_block_assert_head(blk_label, eb_info, left_results, right_results):
     """`W-G.9-352`：定案趟之檢——觸發之端，其鏈之首宗須為末端塊之當選者（含入池閘合併單元）；否則停機。"""
     for _sd, _res in (('left', left_results), ('right', right_results)):
@@ -19243,6 +19269,9 @@ K6B_SCREEN_TRIAL_KEYS = (
     'f3_k929_6_build', 'f3_k929_6_dropped',
     # 🆕 `W-G.9-352`：末端塊之評選（配地本體之首趟所寫·`SS_END_BLOCK_EVAL`；入池閘之畫面入口於復原之後帶出）
     'f3_end_block_eval',
+    # 🆕 `W-G.9-355`：試算旗標（`SS_END_BLOCK_MODE`·段三與末端塊合併再試之試算配地所設）——復原即去之，
+    #   使定案之配地⛔ 見 `'trial'`
+    'f3_end_block_mode',
     # 🆕 `W-G.9-349`：入池閘之合併紀錄（配地本體所寫）
     'f3_k929_6_log',
 )
@@ -19254,6 +19283,8 @@ K6B_SCREEN_READBACK_KEYS = (
     'f3_k6b_stage2_order', 'f3_k6b_stage1_locked_by_block',
 )
 K6B_STAGE3_PENDING = '「街角合併重試」未完成（執行中斷）'
+# 🆕 `W-G.9-355`：末端塊合併再試之未完成標記（合併再試開始前立之，唯其正常完成且末態已存始撤）
+K6B_ENDMERGE_PENDING = '「末端塊合併再試」未完成（執行中斷）'
 
 
 class _K6BTrialStop(Exception):
@@ -19352,47 +19383,20 @@ def k6b_screen_build_for_g(st, build_parcels):
     return _s3[1]
 
 
-def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
-    """段三之畫面入口（`W-G.9-345 §三-2`）。`pk_kwargs` ＝ `f3_screen_corner_pk_run` 之 10 名；
-    `g_kwargs` ＝ `f3_screen_stepg_run` 之 13 名去 `build_parcels`／`_new_params`／`_btn_clicked`／`_auto_recalc`。
-    回 `{'temp', 'build', 'log', 'order', 'ran'}`。"""
+def k6b_screen_callbacks(st, *, pk_kwargs, g_kwargs):
+    """🆕 `W-G.9-355`：段三與末端塊合併再試之**畫面**試算所注入之四物（單一真相源·體例同 harness
+    `verify/selection_pipeline.py` 之 `_k6b_callbacks`）。回 `{'a_prime', 'trial_winner', 'alloc_state', 'alloc_eval'}`。
+    `pk_kwargs` ＝ `f3_screen_corner_pk_run` 之 10 名；`g_kwargs` ＝ 同段三之畫面入口。
+    試算一律以畫面自身之二段（`f3_screen_corner_pk_run`／`f3_screen_stepg_run`·代理 st `_K6BTrialSt`）為之，吃畫面
+    即時之地價；⛔ 借用 harness。`a_prime`／`trial_winner`／`alloc_state` 原位於 `f3_screen_k6b_stage3` 內（`W-G.9-345`），
+    本批抽出以供二者共用——其本體唯 `alloc_state` 之配地改於 `SS_END_BLOCK_MODE` ＝ `'trial'` 下為之（同 harness），
+    餘逐字未改。`alloc_state`／`alloc_eval` 所寫之 session 鍵（含 `SS_END_BLOCK_MODE`）由呼叫端之隔離
+    （`K6B_SCREEN_TRIAL_KEYS` 與 `K917_DROPPED`·試算前存、試算後復）去之。"""
     import copy as _cp_s3
     import contextlib as _cl_s3
     import io as _io_s3
     from shapely.geometry import Polygon as _Pg_s3
     _ss = st.session_state
-    temp0, build0 = pk_kwargs['temp_parcels'], pk_kwargs['build_parcels']
-    # 1. 先去前次之段三結果與停機訊息
-    for _k in K6B_SCREEN_STAGE3_KEYS + ('f3_k6b_stage3_error',):
-        _ss.pop(_k, None)
-    # 2. 旗標 off ⇒ 逕以真 st 跑街角選位
-    if not k6b_stage3_enabled():
-        f3_screen_corner_pk_run(st, **pk_kwargs)
-        _order = list(_ss.get('f3_k6b_stage2_order') or [])
-        _ss['f3_k6b_stage3_log'] = []
-        _ss['f3_k6b_stage3_order_used'] = _order
-        return {'temp': temp0, 'build': build0, 'log': [], 'order': _order, 'ran': False}
-    # 🆕 `W-G.9-346`：段三啟用 ⇒ 先立「未完成」（唯正常出口撤之）；任何中斷皆使其後之配地 loud
-    _ss['f3_k6b_stage3_error'] = K6B_STAGE3_PENDING
-    _ss.pop('f3_k6b_stage2_order', None)
-    # 3. 首趟（代理·寫真 session）；中止 ⇒ 以真 st 再跑一次使畫面現其訊息後重拋
-    _px0 = _K6BTrialSt(st)
-    try:
-        with _cl_s3.redirect_stdout(_io_s3.StringIO()):
-            f3_screen_corner_pk_run(_px0, **pk_kwargs)
-    except _K6BTrialStop:
-        f3_screen_corner_pk_run(st, **pk_kwargs)
-        raise
-    # 4. 段二序
-    order = list(_ss.get('f3_k6b_stage2_order') or [])
-    if not order:
-        f3_screen_corner_pk_run(st, **pk_kwargs)
-        _ss['f3_k6b_stage3_log'] = []
-        _ss['f3_k6b_stage3_order_used'] = order
-        _ss.pop('f3_k6b_stage3_error', None)
-        return {'temp': temp0, 'build': build0, 'log': [], 'order': order, 'ran': False}
-
-    # 5. 三注入物
     _ppz = pk_kwargs['pre_price_by_zone']
 
     def _p_of(tp):
@@ -19454,6 +19458,7 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
                 f3_screen_corner_pk_run(_px, **dict(pk_kwargs, temp_parcels=_t, build_parcels=_b))
                 if 'f3_corner_winners' not in _ss:
                     raise RuntimeError('試算（街角選位）未產出 winners 表（停機款 9）')
+                _ss[SS_END_BLOCK_MODE] = 'trial'   # 🆕 `W-G.9-355`：試算（同 harness·`W-G.9-353`）
                 f3_screen_stepg_run(_px, **dict(
                     g_kwargs, _auto_recalc=False, _btn_clicked=True, build_parcels=_b,
                     _new_params=dict(_ss.get(g_kwargs['_param_key']) or {})))
@@ -19482,6 +19487,160 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
                 _kept.setdefault(_blk, set()).add(_pid)
         return {'kept': _kept, 'bad_pools': _bad, 'err': _err}
 
+    def alloc_eval(temp, build):
+        """🆕 `W-G.9-355`：以所給之宗地試算街角選位與配地（`SS_END_BLOCK_MODE` ＝ `'trial'`），回配地首趟之
+        末端塊評選（`SS_END_BLOCK_EVAL`）之深拷貝。試算中止（代理 st 之 `st.stop`、`RuntimeError`、街角選位
+        未產出 winners 表、配地未產出 G 值表）⇒ `raise RuntimeError`（⛔ 以空評選代之·`end_block_merge_run` 之契約）。"""
+        _t, _b = _copy_pair(temp, build)
+        K917_DROPPED.clear()
+        _px = _K6BTrialSt(st)
+        for _k_rb in K6B_SCREEN_READBACK_KEYS:
+            _ss.pop(_k_rb, None)
+        _ss.pop(SS_END_BLOCK_EVAL, None)
+        try:
+            with _cl_s3.redirect_stdout(_io_s3.StringIO()):
+                f3_screen_corner_pk_run(_px, **dict(pk_kwargs, temp_parcels=_t, build_parcels=_b))
+                if 'f3_corner_winners' not in _ss:
+                    raise RuntimeError('🔴 [末端塊合併再試·畫面] 試算（街角選位）未產出 winners 表')
+                _ss[SS_END_BLOCK_MODE] = 'trial'
+                f3_screen_stepg_run(_px, **dict(
+                    g_kwargs, _auto_recalc=False, _btn_clicked=True, build_parcels=_b,
+                    _new_params=dict(_ss.get(g_kwargs['_param_key']) or {})))
+        except _K6BTrialDone:
+            pass
+        except _K6BTrialStop as _e_ae:
+            raise RuntimeError(
+                f"🔴 [末端塊合併再試·畫面] 試算（配地）中止（st.stop）：{_px.msgs[-1:]}") from _e_ae
+        if 'f3_G_values' not in _ss:
+            raise RuntimeError('🔴 [末端塊合併再試·畫面] 試算（配地）未產出 G 值表')
+        return _cp_s3.deepcopy(_ss.get(SS_END_BLOCK_EVAL) or {})
+
+    return {'a_prime': a_prime, 'trial_winner': trial_winner, 'alloc_state': alloc_state,
+            'alloc_eval': alloc_eval}
+
+
+def f3_screen_end_block_merge(st, *, pk_kwargs, g_kwargs):
+    """🆕 `W-G.9-355`：末端塊之合併再試（`K-9-49 ②`·`K-9-36 ③`·`K-9-50`）之**畫面**入口——同 harness
+    `verify/selection_pipeline.py` 之 `run_end_block_merge`；單一真相源 ＝ `end_block_merge_run`。
+    呼叫端 ＝ `f3_screen_k6b_stage3` 之三個正常出口（皆於其真 st 之街角選位之後）。
+    `pk_kwargs` ＝ `f3_screen_corner_pk_run` 之 10 名（其 `temp_parcels`／`build_parcels` ＝ 合併再試之輸入）；
+    `g_kwargs` ＝ 同段三之畫面入口。回 `{'temp', 'build', 'log', 'rec'}`（無變 ⇒ `temp`／`build` 為輸入之同一物件）。
+      ① 輸入（其時之 session）：上鎖 ＝ `f3_k6b_stage1_locked_by_block` 各值之聯集；街角第 1 宗 ＝ `f3_corner_winners`
+         各值中之非空者；街廓 ＝ `classified_blocks` 之類別；道路中心線 ＝ `f3_manual_road_centerlines`；
+         歸戶 ＝ `t8_ownership_map`；退縮 ＝ `f3L_setback_default`。
+      ② 試算 ＝ `k6b_screen_callbacks`（配地一律 `'trial'`）；隔離 ＝ 試算前存 `K6B_SCREEN_TRIAL_KEYS` 與
+         `K917_DROPPED`、試算後（含例外）復原。
+      ③ 復原之後寫紀錄：`SS_END_BLOCK_MERGE` ＝ `rec`、`'f3_end_block_merge_log'` ＝ `log`。
+      ④ 有變（回傳之宗地非輸入之同一物件）⇒ 以真 st 再跑一次街角選位（所用 ＝ 合併再試之出）。
+    停機（`RuntimeError`）⇒ `f3_k6b_stage3_error` ＝ 其訊息之首列、`st.error` ＋ `st.stop()`（其後之配地 loud）；
+    非 `RuntimeError` 之例外 ⇒ 上拋。未完成之標記（`K6B_ENDMERGE_PENDING`）由呼叫端立之、存末態後撤之。"""
+    import copy as _cp_ebm
+    _ss = st.session_state
+    temp_in, build_in = pk_kwargs['temp_parcels'], pk_kwargs['build_parcels']
+    # 先去前次之紀錄（停機時⛔ 殘留）
+    _ss.pop(SS_END_BLOCK_MERGE, None)
+    _ss.pop('f3_end_block_merge_log', None)
+    _locked = set()
+    for _v in (_ss.get('f3_k6b_stage1_locked_by_block') or {}).values():
+        _locked |= set(_v or [])
+    _corner = set()
+    for _w in (_ss.get('f3_corner_winners') or {}).values():
+        for _pid in (_w or {}).values():
+            if _pid:
+                _corner.add(str(_pid))
+    _blocks = {b['label']: {'category': b.get('category', '')} for b in g_kwargs['classified_blocks']}
+    _cb = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)
+    _saved = {k: _cp_ebm.deepcopy(_ss[k]) for k in K6B_SCREEN_TRIAL_KEYS if k in _ss}
+    _k917_saved = _cp_ebm.deepcopy(K917_DROPPED)
+    _unhandled = []
+    try:
+        temp3, build3, log, rec = end_block_merge_run(
+            temp_in, build_in, _ss.get('t8_ownership_map', {}) or {}, _locked, _corner, _blocks,
+            _ss.get('f3_manual_road_centerlines') or {}, _cb['a_prime'], _cb['alloc_eval'], _cb['alloc_state'],
+            setback=_ss.get('f3L_setback_default'), log_print=_unhandled.append)
+    except RuntimeError as _e_ebm:
+        _ss['f3_k6b_stage3_error'] = '（末端塊合併再試）' + str(_e_ebm).split("\n")[0][:500]
+        st.error(str(_e_ebm))
+        st.stop()
+        raise
+    finally:
+        for _k in K6B_SCREEN_TRIAL_KEYS:
+            if _k in _saved:
+                _ss[_k] = _saved[_k]
+            else:
+                _ss.pop(_k, None)
+        K917_DROPPED.clear()
+        K917_DROPPED.update(_k917_saved)
+    _ss[SS_END_BLOCK_MERGE] = rec
+    _ss['f3_end_block_merge_log'] = log
+    for _m in _unhandled:
+        st.error(_m)
+    if temp3 is not temp_in:
+        f3_screen_corner_pk_run(st, **dict(pk_kwargs, temp_parcels=temp3, build_parcels=build3))
+    return {'temp': temp3, 'build': build3, 'log': log, 'rec': rec}
+
+
+def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
+    """段三之畫面入口（`W-G.9-345 §三-2`）。`pk_kwargs` ＝ `f3_screen_corner_pk_run` 之 10 名；
+    `g_kwargs` ＝ `f3_screen_stepg_run` 之 13 名去 `build_parcels`／`_new_params`／`_btn_clicked`／`_auto_recalc`。
+    回 `{'temp', 'build', 'log', 'order', 'ran'}`。
+    🆕 `W-G.9-355`：三個正常出口（旗標 off／段二序為空／段三實辦而成）皆於其真 st 之街角選位之後辦末端塊之
+    合併再試（`f3_screen_end_block_merge`·同 harness `run_corner_pk_k6b`）；回傳之 `temp`／`build` ＝ 末態，
+    `log` 仍 ＝ 段三之紀錄。段三實辦或合併再試有變 ⇒ 末態存於 `K6B_SCREEN_STAGE3_KEYS`（指紋 ＝ 段三前之
+    build ＋ 退縮）；二者皆無 ⇒ ⛔ 存。合併再試之前立其未完成之標記（`K6B_ENDMERGE_PENDING`·段三實辦者即以之
+    接替段三之標記），存末態之後撤之。段三停機 ⇒ 合併再試⛔ 辦。"""
+    import copy as _cp_s3
+    import contextlib as _cl_s3
+    import io as _io_s3
+    _ss = st.session_state
+    temp0, build0 = pk_kwargs['temp_parcels'], pk_kwargs['build_parcels']
+    # 1. 先去前次之段三結果與停機訊息（🆕 `W-G.9-355`：併去前次之末端塊合併再試之紀錄）
+    for _k in K6B_SCREEN_STAGE3_KEYS + ('f3_k6b_stage3_error',):
+        _ss.pop(_k, None)
+    _ss.pop(SS_END_BLOCK_MERGE, None)
+    _ss.pop('f3_end_block_merge_log', None)
+
+    def _end_merge(temp_x, build_x, log_x, order_x, ran):
+        """🆕 `W-G.9-355`：正常出口之末段——末端塊之合併再試、存末態、撤未完成之標記。"""
+        _ss['f3_k6b_stage3_error'] = K6B_ENDMERGE_PENDING
+        _em = f3_screen_end_block_merge(
+            st, pk_kwargs=dict(pk_kwargs, temp_parcels=temp_x, build_parcels=build_x), g_kwargs=g_kwargs)
+        if ran or _em['temp'] is not temp_x:
+            _ss['f3_k6b_stage3_temp'] = _em['temp']
+            _ss['f3_k6b_stage3_build'] = _em['build']
+            _ss['f3_k6b_stage3_fp'] = k6b_stage3_fingerprint(build0, _ss['f3L_setback_default'])
+        _ss.pop('f3_k6b_stage3_error', None)
+        return {'temp': _em['temp'], 'build': _em['build'], 'log': log_x, 'order': order_x, 'ran': ran}
+
+    # 2. 旗標 off ⇒ 逕以真 st 跑街角選位
+    if not k6b_stage3_enabled():
+        f3_screen_corner_pk_run(st, **pk_kwargs)
+        _order = list(_ss.get('f3_k6b_stage2_order') or [])
+        _ss['f3_k6b_stage3_log'] = []
+        _ss['f3_k6b_stage3_order_used'] = _order
+        return _end_merge(temp0, build0, [], _order, False)
+    # 🆕 `W-G.9-346`：段三啟用 ⇒ 先立「未完成」（唯正常出口撤之）；任何中斷皆使其後之配地 loud
+    _ss['f3_k6b_stage3_error'] = K6B_STAGE3_PENDING
+    _ss.pop('f3_k6b_stage2_order', None)
+    # 3. 首趟（代理·寫真 session）；中止 ⇒ 以真 st 再跑一次使畫面現其訊息後重拋
+    _px0 = _K6BTrialSt(st)
+    try:
+        with _cl_s3.redirect_stdout(_io_s3.StringIO()):
+            f3_screen_corner_pk_run(_px0, **pk_kwargs)
+    except _K6BTrialStop:
+        f3_screen_corner_pk_run(st, **pk_kwargs)
+        raise
+    # 4. 段二序
+    order = list(_ss.get('f3_k6b_stage2_order') or [])
+    if not order:
+        f3_screen_corner_pk_run(st, **pk_kwargs)
+        _ss['f3_k6b_stage3_log'] = []
+        _ss['f3_k6b_stage3_order_used'] = order
+        return _end_merge(temp0, build0, [], order, False)
+
+    # 5. 三注入物（🆕 `W-G.9-355`：由 `k6b_screen_callbacks` 供之·與末端塊合併再試共用）
+    _cb = k6b_screen_callbacks(st, pk_kwargs=pk_kwargs, g_kwargs=g_kwargs)
+
     # 6. 隔離：試算前存、試算後復
     _locked = set()
     for _v in (_ss.get('f3_k6b_stage1_locked_by_block') or {}).values():
@@ -19493,8 +19652,8 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
     try:
         temp2, build2, log = k6b_stage3_run(
             order, _locked, _ss.get('t8_ownership_map', {}) or {}, temp0, build0, _blocks,
-            _ss.get('f3_manual_road_centerlines') or {}, a_prime, trial_winner, alloc_state,
-            log_print=_unhandled.append)
+            _ss.get('f3_manual_road_centerlines') or {}, _cb['a_prime'], _cb['trial_winner'],
+            _cb['alloc_state'], log_print=_unhandled.append)
     except RuntimeError as _e_s3r:
         # 7. 段三停機 ⇒ 記其訊息（配地由 `k6b_screen_build_for_g` 擋下）
         _ss['f3_k6b_stage3_error'] = str(_e_s3r).split("\n")[0][:500]
@@ -19521,11 +19680,8 @@ def f3_screen_k6b_stage3(st, *, pk_kwargs, g_kwargs):
             st.caption("（本次無紀錄）")
     _ss['f3_k6b_stage3_log'] = log
     _ss['f3_k6b_stage3_order_used'] = order
-    _ss['f3_k6b_stage3_temp'] = temp2
-    _ss['f3_k6b_stage3_build'] = build2
-    _ss['f3_k6b_stage3_fp'] = k6b_stage3_fingerprint(build0, _ss['f3L_setback_default'])
-    _ss.pop('f3_k6b_stage3_error', None)
-    return {'temp': temp2, 'build': build2, 'log': log, 'order': order, 'ran': True}
+    # 9. 🆕 `W-G.9-355`：末端塊之合併再試（段三之後）；段三之未完成標記延至其正常完成始撤
+    return _end_merge(temp2, build2, log, order, True)
 
 
 def _k929_6_screen_gate(st, g_kwargs):
@@ -24801,6 +24957,9 @@ def main():
                             # 🆕 `W-G.9-345`：段三（街角合併重試）之結果與停機訊息一併失效
                             for _k_s3inv in K6B_SCREEN_STAGE3_KEYS + ('f3_k6b_stage3_error',):
                                 _st_inv.session_state.pop(_k_s3inv, None)
+                            # 🆕 `W-G.9-355`：末端塊合併再試之紀錄一併失效
+                            _st_inv.session_state.pop(SS_END_BLOCK_MERGE, None)
+                            _st_inv.session_state.pop('f3_end_block_merge_log', None)
                             _st_inv.session_state['f3_g_needs_rerun'] = True
                         except Exception:
                             pass
@@ -25644,6 +25803,18 @@ def main():
                                 st.dataframe(_pd.DataFrame(_eb352_v['rows']),
                                              use_container_width=True, hide_index=True)
 
+                    # 🆕 `W-G.9-355`：末端塊之合併再試（`K-9-49 ②`·`K-9-36 ③`·`K-9-50`）——標的、競合、皆未達與逐列紀錄
+                    _ebm355 = st.session_state.get(SS_END_BLOCK_MERGE)
+                    if _ebm355 is not None:
+                        _ebm355_v = end_block_merge_rows(_ebm355, st.session_state.get('f3_end_block_merge_log'))
+                        with st.expander("🔗 末端塊之合併再試（K-9-49 ②／K-9-36 ③／K-9-50）",
+                                         expanded=bool(_ebm355_v['rows'])):
+                            for _ebm355_l in _ebm355_v['lines']:
+                                st.caption(_ebm355_l)
+                            if _ebm355_v['rows']:
+                                st.dataframe(_pd.DataFrame(_ebm355_v['rows']),
+                                             use_container_width=True, hide_index=True)
+
                     # 🆕 `W-G.9-351`：調配階段之輸入（步 1 之尾〜步 2·`K-9-45`／`K-9-46`）——僅盤點·⛔ 調配
                     _adj351_bf = st.session_state.get(SS_ADJ_BUILD_FINAL)
                     if _adj351_bf is not None:
````

## ⑨ 各段耗時（規格單流程之試行評估）

時刻取自倉外落檔之修改時間與 `commit` 時間（`+0800`·約數）。

| 段 | 起訖 | 約 |
|---|---|---|
| 讀單・開場閘（refs、態錨器、本單與五塊之對拍、取號現查、pre-flight） | 起時未錄（態錨器之落檔 `22:13`）–`22:16` | 約 `5`〜`10` 分 |
| 工項零・一（入倉·推） | `22:16`–`22:17` | `1` 分 |
| 前置 `1`〜`5`（`F14` 二子命令、`parity` 二、`F8` 二、`F6`） | `22:17`–`22:26` | `9` 分 |
| 前置 `6`（`run_all`·背景·與讀碼、撰碼並行） | `22:17`–`22:32` | `15` 分（`902` s） |
| 讀碼・撰碼（含設計；至首次 `F14 selftest`） | `22:18`–`22:35` | `17` 分 |
| 試跑（`selftest` 綠、十器接線、`F14 run`） | `22:35`–`22:51` | `16` 分 |
| 驗 `V-1`〜`V-6`（`commit` 後·`run_all` 與 `F14 run` 背景並行） | `22:51`–`23:27` | `36` 分（`run_all` `1141` s、`F14 run` `1167` s） |
| 推・登記（工項三） | `23:27`–`23:28` | `1` 分 |
| 報告 | `23:28`– | 見對話 |

🔒 **評估**：撰碼本身（`17` 分）短於量測（前置 `9`＋`15` 並行、試跑 `16`、驗 `36`）；耗時之主項為 `F14 run`（畫面路徑之真資料試算·單趟 `15`〜`20` 分）與 `run_all`。規格（`§三`）之 `R-1`〜`R-13` 與介面（`§三-2`）足以一次寫成——首次 `F14 selftest` 即 `rc 0`，其後⛔ 改碼。
