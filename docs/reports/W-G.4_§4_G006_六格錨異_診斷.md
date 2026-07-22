# W-G.4 §4 波末重烤前置：G006 六格錨異診斷（查清·勿改錨/引擎）

## 結論（先講）

- **verify harness G006 ＝ 365.84（＝錨·雙情境·逐位·NOT 222.45）**。KL UI 之 **222.45 係 APP-side**（app-live-ctx 引擎），**非 verify harness**。
- **錨 365.84 正確·無需更新**（verify harness 逐位坐實）。**引擎（run_step_g）不動**。
- **222.45 之根因＝APP 之 步驟J（Patch B-2 寬度驗證·壓 width<法定最小之 G→48.99）**——`harness run_step_g 無此壓縮`（`app.py:8708` 明載）→ **app-live-ctx 之 G006（壓值/步驟J-觸發併宗）與 harvest-ctx（harness）分岔**。
- **非域邊界**：628-49 於兩路皆判畸零（harness bake 旗標消長：`628-49(2) 因移除消失·畸零 有`）·**非「該否算畸零」爭議** → **不停機**。222.45 係 **APP-wiring 技術缺**（另波修·非本查清·非引擎·非錨）。

---

## 一、任務1：WV_BAKE 六格 dump（harness·雙情境）

`WV_BAKE=<dir> python verify/run_verification.py`（working tree b4ba9d3）·六格 G(Σa)（trunk B·run_step_g·對 `GSA_EXPECT`）：

| 格 | 0m G(Σa) | 錨 0m | 3.5m G(Σa) | 錨 3.5m | 判 |
|---|---|---|---|---|---|
| **G006** | **365.84** | 365.84 | **365.84** | 365.84 | **逐位符** ✅ |
| G009 | 153.19 | 153.19 | 153.19 | 153.19 | 逐位符 ✅ |
| G017 | 433.68 | 433.68 | 433.68 | 433.68 | 逐位符 ✅ |
| G007 | 359.43 | 362.08 | 369.41 | 369.05 | 微差 −2.65/+0.36（比率更新噪）|
| G010 | 293.72 | 294.81 | 298.61 | 298.63 | 微差 −1.09/−0.02 |
| G014 | 127.05 | 127.06 | 129.20 | 129.21 | 微差 −0.01/−0.01 |

- harness `F.0_合併決策` G006（雙情境逐字）：`標的 628-48(1)·併 628-47(1);628-49(2)·Σa=627.61·G(Σa)=365.84·達標✅·留置原位`。
- committed（worktree b4ba9d3·xlsx **12.38MB**）：**確認 G006 ＝ 365.84（雙情境·與 working −900KB 逐字同：同併宗 628-48(1)+628-47(1);628-49(2)·Σa=627.61）**；六格錨異亦逐字同（G007/G010/G014 同值）→ **−900KB working xlsx 對六格零影響**（working ≡ committed）。
- **⇒ 任務1 答：harness G006 ＝ 365.84（≠222·committed＝working）。222.45 非純引擎/verify harness·係 APP-side。** G007/G010/G014 之微差係 W-G Y 比率更新（錨 PRE-比率·`wf_f0:51`）·與 G006 無關·且 committed≡working（非 xlsx）。

## 二、任務2：bisect 前提 REFUTED

- KL 前提「把 G006 從 ~365 移到 ~222 的那一個 commit」**不成立**：**verify harness G006 現＝365.84（從未移）**。`a118dbe..b4ba9d3` 內**無 commit 把 harness G006 移到 222**（bisect 無標的）。222.45 係 APP·非 harness → 不需 bisect harness。

## 三、任務3：628-49 步驟J 機制（坐實）

- **步驟J**（`app.py:16717-16732`·Patch B-2 寬度驗證）：對「寬<法定最小」宗**就地壓 G ＝ `round(min(orig_G, min_area−0.01),2)`**（KL 觀察之 48.99）·`以觸發合併`；原 G 存 `_G_before_width_violation`。
- **harness `run_step_g` 無此壓縮**（`app.py:8708` 逐字：「harness run_step_g 無此壓縮·故 live gA 須還原否則 GSA 錨破（G014 131.79 vs 133.22）」）。
- 628-49 於 harness bake **亦判畸零**（旗標消長 `628-49(2) 因移除消失·畸零 有`）→ **兩路皆畸零·非分岔源**。
- ⇒ 628-49 於 **app 被步驟J 壓**、於 **harness 用原值** → app G006 用壓值/步驟J-觸發併宗、harness 用原值併 3 宗 R3 → **分岔**。

## 四、任務4：app-vs-harness 對齊

- **三數**：`錨/verify harness = 365.84`（run_step_g·harvest-ctx·併 628-48(1)+628-47(1)+628-49(2)·Σa=627.61·原 G）｜`app-engine「trunk B」= 222.45`（KL UI·app-live-ctx·六格 gate 停機）｜`app trunk A′ = 527.28`（逐宗 post-步驟J）。
- **verify harness（365.84）＝正確參照**（＝錨）。**app-engine（222.45）分岔**：app `_build_wf_ctx`（`app.py:8710`）**還原 `_G_before_width_violation`** 供引擎；222.45 表示 app-live-ctx 之 G006 仍帶步驟J 效應（**壓值還原不全 或 步驟J-觸發之併宗異於 harness**）。
- **精確 app-path 機制**（為何 8710 還原後 app-engine 仍得 222.45·而非 365.84）**需 headless app-path 追**（harvest-ctx 不含步驟J·無法從 harness 復現 app-live-ctx；需 app UI-flow 之 ss 或 KL app 資料）。→ 列**次波追**。
- ⇒ **222.45 係 stage/wiring 分岔**（步驟J 壓值/併宗未對齊 harness）·**非合理位移·係 bug（app-side·非引擎·非錨）**。

## 五、裁示／次步（勿改錨/引擎·本輪只查清）

1. **錨 365.84 不動**（verify harness 逐位坐實正確）。**引擎不動**（harness G006=365.84 正確）。
2. **222.45 ＝ APP-wiring bug**（步驟J 壓值/併宗未對齊 harness）→ **次波修 app-path**（追 `_build_wf_ctx` 之 628-49 步驟J 還原/併宗·對齊 harness），**非本查清·非域裁**。
3. **非域邊界**（628-49 兩路皆畸零·非「該否算畸零」）→ **不停機**。
4. 波末重烤：**G006 錨無需更新**（harness 逐位符）；G007/G010/G014 之微差（W-G Y 比率更新·PRE-比率錨）是否重烤更新·**另裁**（與本 G006 查清無關）。

**引用**：`verify/wf_f0.py:55`（GSA_EXPECT 錨）·`:182-195`（六格 gate·WV_BAKE print/raise）；`app.py:8706-8712`（`_build_wf_ctx` 步驟J 還原）·`:16717-16732`（步驟J 壓 G）；bake `wf/f0/F.0_合併決策_退縮*.csv`（G006 逐字）。
