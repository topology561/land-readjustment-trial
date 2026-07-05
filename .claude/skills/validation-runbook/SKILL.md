---
name: validation-runbook
description: 每個 diff 提交前、每波驗收時執行。可直接跑的驗證命令與預期輸出：py_compile、golden、grep 清單、凍結 diff、守恆閘、算術不變量、UC9898 oracle 值。
---

# 驗證 Runbook（命令＋預期輸出）

## 每個 diff 必跑
```bash
python -m py_compile app.py            # 預期 exit 0、無輸出
python tests/test_corner_priority_golden.py   # 預期 exit 0（0.6685/0.3315/winner=1地號）
```
- golden 以 AST 抽 app.py 實體 `_pk_one_side_v12` exec（**不 import app**——模組級 `st.set_page_config` 會炸）；輸出避免 emoji（Windows cp950）。

## grep 清單
```bash
# 刪除零殘留（依當波刪的名字）：預期全部 0 命中
grep -n "_calculate_corner_pk\|select_corner_lot_priority" app.py
grep -nE "\bselect_corner_lots_both_sides\b" app.py   # 非 _v12 版本應 0
# 猜側模式應 0（-c.1 後鐵律）
grep -n "_dp1 < _dp2\|_d_p1 < _d_p2" app.py
# 無新孤兒：被刪函式的專屬 helper 應同刪；共用 helper 應仍有活 caller
```
- 順序判定用**呼叫圖**不用行號；孤兒判定＝「def 之外零出現」。

## 雙情境（強制，單情境會遮蔽 bug）
退縮 **0m 與 3.5m** 都跑診斷＋指配。單情境「全綠」不可信——15m 框在 3.5m 被 G-gate 遮蔽的教訓。

## 凍結逐格 diff
拿本波 CSV 對前一波 CSV，凍結欄逐格比（key＝街廓+端+候選）：
候選名單、真交集、整筆幾何、範圍面積、G估、門檻、達標——**任何一格不同＝停**（除非該欄在本波可變清單＋預先武裝的裁決規則內）。

## 守恆與結構閘
- ΣG＋池＝街廓面積，差 <1㎡；Tier3=0；白縫≈0。
- 診斷「範圍=門檻?」逐列 ✅（項三分母＝G-gate 門檻＝同一顆 range）。
- 算術不變量：項一∈[0,0.4]、項二∈[0,0.2]、項三比≤1；每端 Σ臨截角≤截角邊、Σ臨側街≤側街邊。
- 全覆蓋錨：R1右 628 0m 總分＝1.0、R4 兩筆≈0.99——掉到 0.x＝臨長判定壞。

## UC9898 oracle（`docs/案例空間基準_UC9898.md/.json`）
- 面：R1 2893.54／R2 4368.57／R3 4206.83／R4 3207.87／R5 4150.17／R6 3976.35／G1 7464.65（㎡）。
- R1左（json 鍵＝T＝退縮＋3.5）：0m winner 628-37=0.574、臨側街 8.209/12.417/8.952 和=29.579；3.5m winner 628-36。
- 各側 tc 截角面積＝參數表：R1 左6.71/右5.77、R4 左6.86/右6.25、R2 左6.28、R3 右6.2、R5 左6.14、R6 右5.77。
- 抵費地端（3.5m）：R5左 300.52／R2左 309.05／R3右 308.93＝各端 range 面積。

## 環境
- 每次 patch 後：清 `__pycache__`；KL 端清 session_state 快取再跑。
- commit 只 stage 自己的檔（勿夾帶 KL 未追蹤資料）；push 後回報 hash。
