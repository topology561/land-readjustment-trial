# 市地重劃試分配系統 — Skill 蒸餾（Fable 5 Skill Distillation）

W-D.1.3 全波收官後，由 claude.ai 將 W-A→W-D.1.3 累積之判斷蒸餾為 8 個 durable skills（KL 選 A、三輪 review：factual/doctrine/usability）。目的：讓 CC 每個新 session 不必重建判斷、不重踩已付學費的坑。

## 索引（何時讀哪個）
| Skill | 觸發時機 |
|---|---|
| `cad-layer-semantics` | 動任何 CAD/DXF/SVMAP 幾何、圖層配對、左右側判定前 |
| `g-formula-rules` | 動 G 值、負擔、池、ΣRw 前 |
| `corner-selection-rules` | 動 §1 街角三指數、range、E-1.7、tiebreaker 前 |
| `failure-archaeology` | 診斷異常、審修法、「數字不對但不知為何」時 |
| `no-silent-fallback` | 寫錯誤處理/預設值/except/刪舊碼前 |
| `wave-discipline` | 開始任何實作波前 |
| `validation-runbook` | 每個 diff 提交前、每波驗收時（可直接跑的命令） |
| `stop-conditions` | 驗收不符靶、不確定「bug 還是預期」時 |

## 維護規則
1. **KL 域裁示即鎖**：新裁示 → 當波更新對應 skill（域規則 3 檔優先）。
2. **新失敗模式**：付過學費就進 `failure-archaeology`（症狀→根因→通則格式）。
3. **行號永不入 skill**：一律符號名（行號每波漂移）。
4. **數值錨要有出處**：參數表值/UC9898 基準/golden——與 `docs/案例空間基準_UC9898.md`、`tests/test_corner_priority_golden.py` 互為表裡。
5. 與 `CLAUDE.md`/memory 分工：CLAUDE.md＝專案入口與環境；memory＝進度與 hash；**skills＝判斷與規則**（跨波不變的部分）。

## 已知後續 hook（勿失）
- W-D §2 落地 → tiebreaker 改吃正典原位次（corner-selection-rules）。
- W-D.2 §3 → `left/right_corner_min_area` 守恆接線（g-formula-rules）。
- 未來案例聚合線（折線）→ 配對/量測通用化（cad-layer-semantics）。
