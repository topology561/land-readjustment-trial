---
name: wave-discipline
description: 開始任何實作波（新功能、修 bug、清理）之前必讀。涵蓋分工、波循環、驗收靶先行、凍結欄框架、-a求一致與-b求變動的相反尺標、偏離計畫的記帳規則。
---

# 波段紀律（W-A→W-D 全程驗證有效的工作法）

## 分工（不可越界）
- **claude.ai**：規格、細部 plan、診斷、判斷層裁示。**不寫 production code**。
- **CC（本 agent）**：一切 code 變更。plan mode → reviewer 審計畫 → 實作 → per-diff reviewer → commit。
- **KL**：域權威（法規裁示即鎖）、跑 app、雙情境驗收。
- 判斷題**上呈**（claude.ai 裁或 KL 裁），不逕自擴大範圍、不逕自調參湊靶。

## 波循環（每波必走）
1. **規格先行**：claude.ai 更新細部 plan → KL commit 進 repo（規格＝跨 session 真相源；動工前先確認讀到最新版）。
2. **驗收靶先行**：動工前從資料推出**具名靶**（哪塊該變、變成什麼值、哪些凍結）——不是做完再看。
3. plan mode 寫施工計畫 → **reviewer 獨立審計畫**（自己 grep/實跑、不採信宣稱）→ 折入訂正。
4. 實作（bottom-up 編輯免重錨；整段函式當 old_string 天然限 scope）。
5. **per-diff reviewer**：grep/py_compile/守恆/actual-vs-planned；敏感字（inter/G/守恆/面積_m2/Tier/a'）diff 0 命中。
6. commit+push（清 `__pycache__`、只 stage 自己的檔）→ KL 跑**雙情境**（0m＋3.5m）→ claude.ai 逐格判。

## 凍結欄框架（驗收的骨幹）
- 每波先宣告：**凍結欄**（不許動的一切）＋**可變欄**（本波唯一允許變的）。驗收＝凍結欄與前一波**逐格 diff 全同**＋可變欄命中具名靶。
- **兩種相反尺標，別拿錯尺**：
  - **行為保持波（求一致）**：如 -a 幾何切換、-d 清理——winner/數值逐格不變、僅指定欄可動。「不變」證明沒污染，**不代表舊值正確**（-a 後的 winner 仍是待 -b 糾正的錯 winner）。
  - **糾正波（求變動）**：如 -b/-c——winner **該**在具名靶翻、且逐塊驗證是「糾正」非 regression；沒變的塊也要驗其本就正確。
- **錨**：全覆蓋候選 ≈1.0（災難性歸零偵測器）；參數表當診斷欄裁決器。**預先武裝可判定規則**（新值==參數表→糾正放行；≠→bug）勝過裸「停下來問」。

## 偏離計畫的記帳
- 實作中裁定偏離核准計畫（如把刪除延到下波）→ **記入 actual-vs-planned＋回頭改規格**，否則下個 session 誤判漏做。
- 一波一事：無關的刪除/重構延到清理波（-d 型）。

## 交接
- 新 session 開工序：CLAUDE.md → memory → 規格細部 plan → 基準檔 → **重錨行號**（行號必漂移，錨用符號名）→ 才動工。
- 波收官：更新 memory（進度＋commit hash）、規格標收官、golden/基準檔留給下波。
