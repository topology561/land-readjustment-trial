# W-G.4 run_all 紅：working xlsx（07-19 未 commit·−900KB）致 F.0 錨破·§3 held·上呈 KL

> ❌ **KL 2026-07-21 更正·本上呈誤判·勿據行動**：F.0 紅 `G007 359.43≠362.08` 係**過期錨**——錨 362.08 由 `0c9b7e7`（07-17·註明「不動錨」）設，而 **W脫鉤(07-19)＋S0d(07-20) 之後改了 G 之 W/S 輸入項 → 359.43 係預期新值**。**非資料壞、非 regression、非施工可致**。committed xlsx（blob `80f75ee`·12.38MB）完好、整波未變。**勿動 data/xlsx、勿追此紅**；錨待波末重烤（含 KL UI 錨）更新。branch `wip/s1-endpart` ＝**准紅碼**。

- 日期：2026-07-21；branch `wip/s1-endpart`（`b7ecbbd` ＋ **未 commit** 之 wf_f4 §3 edit）
- 事件：§3（rebake 註解·zero-behavior）施工後跑 `run_all` → **RESULT: FAIL** → **§3 held（不綠不推）**。
- 性質：**環境/資料阻斷**（非設計、非碼）——與 prior 🚩「data xlsx 本機異動未入 commit」同源。

---

## 一、失敗（`verify/out/run_all_rebake.log`）

- **F.0 六格錨破**：`G007 G(Σa)=359.43 ≠ 錨 362.08（0m）` → 級聯 F.1–F.4（存在性守衛逐級跳過）→ **G.2** `_f0["0m"]["sgB_rows"]` `NoneType`（F.0 掛 → _f0 None）。
- run_all 自身診斷：`嫌犯序：快照漏參 > dtype 1.5（法人統編 '.0'）> driver orchestration 漂移 > 引擎（勿動 app）`。

## 二、證非本次 edit（§3）

1. **docs 改**（recon.md／plan／上呈）＝無 runtime。
2. **wf_f4 §3 edit** ＝ E3 段註解 ＋ raise 訊息文字；**本 run F.4 被跳過**（F.3 fail → F.4 skip·**我改的碼未執行**）；且 **F.0／G007 在上游**、與 E3 帳對閘無關。→ §3 edit **不可能**致此紅。

## 三、根因＝working xlsx（資料·時間軸坐實）

| 時點 | xlsx | F.0 G007 | run_all |
|---|---|---|---|
| 07-16 21:30（`run_all_Y2.log`）| committed（12,380,156 B）| **362.08** ✅ | ALL GREEN |
| 07-19 23:04 | **modified**（11,482,185 B·**−897,971·−7%**·未 commit）| — | — |
| 07-21 17:37（`run_all_rebake.log`·本 run）| modified | **359.43** 🔴 | FAIL |

- `harvest()` 讀 **live xlsx** 供 F.0；碼硬錨 `362.08`（＝committed xlsx 資料·07-16 綠佐證）；**modified xlsx → 359.43 → 錨破**。
- **modified 檔 −900KB** ＋ `.tmp.driveupload/`（dir mtime 今 17:37·Google Drive 活躍）→ 高度疑 **Drive 同步遺留之部分/截斷檔** → 缺列/缺欄 → run_all 診斷「快照漏參」。
- ⇒ F.0 之 359.43 係**資料驅動**（committed→362.08；modified→359.43）·非碼變。

## 四、影響

- `run_all` **無法取綠** → **§3 held**（edit 完成·py_compile OK·zero-behavior 已證·**留 working tree 未 commit·ready**）。
- **所有碼-push 之 green-gating 阻斷** until 資料穩定（純 docs push 不受影響·如 `b7ecbbd`／本檔）。

## 五、請 KL 裁（其資料·CC 不擅動）

1. **還原 committed xlsx**（`git checkout HEAD -- "data/…xlsx"`·穩定 run_all·棄 07-19 modified）——若 modified 係 Drive 遺留/非有意；**抑或**
2. **07-19 modified 係有意新資料** → commit ＋ **重定 F.0 六格錨**（362.08→359.43…·連帶下游）；**抑或**
3. **Drive 同步遺留** → 停同步／還原完整檔後再跑。

> CC **不自動裁·不擅動 KL 資料**（xlsx 係 prior 🚩 escalated）。裁 1/2/3 後：xlsx 穩定 → run_all 綠 → §3 commit+push（wf_f4 edit 已在 working tree ready）。

**引用**：`verify/out/run_all_rebake.log`（本 run·未入倉）·`verify/out/run_all_Y2.log`（07-16·committed·G007 362.08 綠）·git status（`M data/…xlsx`）。
