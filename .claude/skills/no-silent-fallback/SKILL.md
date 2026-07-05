---
name: no-silent-fallback
description: 寫任何錯誤處理、預設值、except 分支、刪除舊函式、或處理缺圖層/缺參數情形之前必讀。本專案的無靜默鐵律：缺值必警示、舊碼整段刪、fallback 即藏 bug。
---

# 禁止靜默 fallback（鐵律）

## 核心原則
**系統寧可大聲停下，不可安靜地編造。** 每一次靜默替換（預設值、歸零、退舊演算法）都是把 bug 藏進「看起來正常」的輸出裡——本專案兩度因靜默歸零延誤根因（-a W1、-c 側別）。

## 規則
1. **缺圖層 → 停機警告＋跳過該塊**，不得退用其他演算法。範本（V12 刪除案）：
   `st.error(f"街廓 {lbl}：缺 FRONT_LINE 圖層（p1左 p2右）→ 無法執行街角地優先權選位。請至 CAD 補畫 FRONT_LINE 後重跑。")` ＋ `continue`（不 append 假結果）。
2. **警示訊息面向縣府同仁（§10 受眾裁示）**：中文明講「缺什麼、去哪補、補完做什麼」；**禁止丟 traceback**。
3. **案例/街廓級參數（退縮、法定最小寬…）禁止靜默預設**——它們不是系統常數。`or 3.5` 這種 falsy-zero 寫法把合法的 0 吃掉，一律 `x if x is not None else …` 並在缺值時警示。
4. **幾何解析失敗 → 具名警示**：街角端有 range 但截角線解析 None/分母≈0 → warn 指名街廓＋端；禁止安靜給 0 分。
5. **裸 `except:` 收窄**為具體例外元組（如 `(KeyError, IndexError, TypeError, ValueError, AttributeError)`）；`except → return None` 若不搭警示＝靜默 fallback。
6. **舊函式/舊路徑整段刪，不留 stub、不留 fallback 分支**——留 fallback＝把剛修掉的 bug 藏回去（-c.1 刪猜側時明令不留）。刪後 grep 名稱＝0、確認無新孤兒。
7. **資料結構缺新欄（舊快取）→ 不猜**：warn＋None，提示清 session cache；禁止退回舊推導法。
8. 診斷表也適用：**診斷說謊會誤導未來偵錯**（我們靠診斷表抓 bug）——診斷欄的來源同樣禁止猜側/猜值。

## 自查清單（每個 diff）
- [ ] 新增的 except 都有具名警示或明確窄化理由？
- [ ] 有沒有 `or 常數` 吃掉合法 0/空值？
- [ ] 刪除的舊路徑 grep＝0？有沒有偷留 fallback 分支？
- [ ] 缺圖層/缺欄位路徑走到的是「中文停機警告」還是安靜的 0/None？
