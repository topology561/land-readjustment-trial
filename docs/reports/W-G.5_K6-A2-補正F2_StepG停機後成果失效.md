# W-G.5 — **K-6-A2 補正 F-2：Step G 停機後舊成果殘留**

> **基準**：`dd02b5b`　**分支**：`wip/s1-endpart`
> **性質**：**單項·家族修**。有行為變更（重算起點清產物鍵），本案不改任何分配結果。
> ⚠️ 本單所引行號**全部當場重 grep**；差異見 §七（**本單零差異**）。

---

## 一、問題（**已逐項查證·非推測**）

Step G 之兩個產物寫在**最末**：

```
grep -n "st.session_state\['f3_G_values'\] = "  app.py
grep -n "st.session_state\['f3_G_trace'\] = "   app.py
```

若 Step G 中途 raise，二者**不被覆寫、也不被清除**。

而 `f3_G_values` 之**唯一失效路徑**為 `_f3L_invalidate_g_cache`
（`grep -n "def _f3L_invalidate_g_cache" app.py`），
其**只綁「街角地退縮距離」與「街廓分配深度」二 widget 之 `on_change`**
⇒ **改屁股線指派不會觸發**。

⇒ 使用者若：**成功跑過一次 → 改屁股線指派 → 重跑 Step G → 被 K-9-4 閘擋下**
（`grep -n "k94_assert_baseline_touch(_k94_touch)" app.py`），
則成果區與下載鈕（`grep -n "if st.session_state.get('f3_G_values'):" app.py`）
**照樣渲染並提供舊的 `f3_G_values`**。

🔴 **土地後果**：可能交付一份**與現行屁股線設定不符**之分配成果表
——**而這正是 K-9-4 最想防之情境**。

### 1-0 🔬 殘留之精確機制（**本批實查·補施工單所述之時序**）

施工單謂「被擋下 → 成果區照樣渲染」。**結論正確，惟時序須說明白**——
`main()` 之呼叫（`grep -n "^    main()" app.py`）**不被任何 `try` 包住**（`ast` 確證）
⇒ raise **會傳到 Streamlit**。故：

| 時點 | 發生什麼 |
|---|---|
| **失敗之該次 rerun** | raise 傳出 → Streamlit 顯示例外並**中止本次渲染** ⇒ 成果區**不**渲染 |
| **下一次 rerun**（使用者點任何其他控制項） | 按鈕未按、`_auto_recalc` 為假 ⇒ **Step G 分支不執行**，流程直接走到成果區 ⇒ 讀到**未被清除之舊 `f3_G_values`** ⇒ **照常渲染並提供下載** |

⇒ **殘留之危害發生在「下一次 rerun」，不是失敗當次。**
本修法（在**進入重算之當下**即 pop）對兩者皆有效：
舊值於 raise **之前**即已消滅 ⇒ 下一次 rerun 讀不到 ⇒ 成果區不渲染。

### 1-1 非本批引入·故採家族修（**AST 確證**）

Step G 計算分支（`if _btn_clicked or _auto_recalc:` 起至 `f3_G_values` 寫入止）內之 raise：

```
Step G 計算分支 17621–18761 內之 raise：[17909]
  第 17909 行 raise ← 位於 try-body 內之 Try：無 ✅（不被吞）
```

（K-9-4 閘於 `18759` 係**經函式呼叫** raise，非字面 `raise` 敘述，故不列於上表；
其不被 `try` 吞已於段二-1(c) §六-3 以 `ast` 確證。）

⇒ **既有 raise 與 K-9-4 閘皆暴露此風險** ⇒ 本單採**家族修**：
於**重算分支起點**失效，一次覆蓋 Step G 內**現有與日後所有**之 raise，
而非逐個 raise 前補清除。

---

## 二、辦理

於 `g_rows = []`／`detail_trace = {}` 之後（`grep -n "K-6-A2 補正 F-2" app.py`）加入：

```python
st.session_state.pop('f3_G_values', None)
st.session_state.pop('f3_G_trace', None)
st.session_state['f3_g_needs_rerun'] = True
```

**語意**：**進入重算的那一刻，前一輪成果即作廢**。
成功時末端寫回二產物、並清 `f3_g_needs_rerun`（`grep -n "pop('f3_g_needs_rerun', None)" app.py`）
⇒ **狀態機自然閉合**。

---

## 三、實作紅線之遵循（§三·**與直覺相反者**）

### 3-A ⛔ 未照抄 `_f3L_invalidate_g_cache` 之鍵名清單

該函式另 pop `f3_corner_winners` 與 `f3L_corner_winners`。
**該二鍵是 Step G 之上游輸入、不是它的產物**：

| 鍵 | 寫（步驟 L） | 讀（Step G） |
|---|---|---|
| `f3_corner_winners` | `grep -n "st.session_state\['f3_corner_winners'\] = " app.py` | `grep -n "_step_l_winners = " app.py`；另一處於 Step G 內 |
| `f3L_corner_winners` | `grep -n "st.session_state\['f3L_corner_winners'\] = " app.py` | — |

⇒ 於重算起點 pop 之即**當場毀掉 Step G 自己的輸入**。
**本單只清 `f3_G_values` 與 `f3_G_trace` 兩把。**

**前提已逐一確認**——二者於重算區間內**只被寫、不被讀**：

```
$ grep -n "f3_G_values\|f3_G_trace" app.py | awk -F: '$1>=17624 && $1<=18762'
18741:  （本批之註解行）
18761:  st.session_state['f3_G_values'] = g_rows      ← 寫
18762:  st.session_state['f3_G_trace'] = detail_trace ← 寫
```

⇒ 區間內**無任何讀取** ⇒ 於起點 pop **不影響 Step G 自身運算**。

### 3-B ⛔ 未碰 `f3_g_needs_recalc`

`f3_g_needs_rerun`（橫幅旗標·讀於 `grep -n "if st.session_state.get('f3_g_needs_rerun'):" app.py`）
與 `f3_g_needs_recalc`（自動重算觸發·消費於 `grep -n "_auto_recalc = bool" app.py`）
**是兩把不同的鍵**。本單**只碰前者**。

**自查**：

```
$ git diff -- app.py | grep -E "^\+" | grep -E "f3_corner_winners|f3L_corner_winners|f3_g_needs_recalc"
（僅命中三行**註解**，無任何可執行敘述）
```

⇒ 碰 `f3_g_needs_recalc` 會造成「失敗後自動重跑、再失敗」之迴圈——**未犯**。

---

## 四、驗證（合成·**不改生產碼**）

實料：`verify/out/F2_stepg_invalidate.log`

🔒 **非套套邏輯**：本驗證**不重寫**失效邏輯，而是**自 `app.py` 原始碼抽出那幾行敘述**
並 `exec` 之 ⇒ 驗的是**倉內真正那幾行**；任何人改了那幾行，結論就會跟著變。
K-9-4 閘亦直接呼叫 `app.k94_assert_baseline_touch` 真符號。
擾動沿用段二-1(c) §四 之 **(i) 案**（後緣頂點沿 BASELINE 法向推 `0.5m`），未新造。

**自 `app.py` 抽出之敘述**（本驗證所執行者即此六行）：

```
【失效區塊】 st.session_state.pop('f3_G_values', None)
             st.session_state.pop('f3_G_trace', None)
             st.session_state['f3_g_needs_rerun'] = True
【成功區塊】 st.session_state['f3_G_values'] = g_rows
             st.session_state['f3_G_trace'] = detail_trace
             st.session_state.pop('f3_g_needs_rerun', None)
```

| # | 驗證 | 結果 |
|---|---|---|
| **1** | **成功路徑不變**：閘未 raise；`f3_G_values` 存在且**為新成果**（非舊）；`f3_g_needs_rerun` 不存在 | ✅ 三項皆 OK |
| **2** | **失敗路徑清乾淨**：閘 raise（`【未配到屁股線】1 宗 R1/628-37(1) 差 0.500m`）；`f3_G_values`／`f3_G_trace` **皆不存在**；`f3_g_needs_rerun` 為 `True` | ✅ 三項皆 OK |
| **3** | **紅線反向對照**：同一次失敗後 `f3_corner_winners`／`f3L_corner_winners` **仍在** | ✅ 二項皆 OK |

⇒ 驗證 3 正是「**未照抄** `_f3L_invalidate_g_cache` 之鍵名清單」之反向證明
——若照抄，該二鍵會被一併 pop、本項必翻。

---

## 五、`run_all`

實料：`verify/out/K6A2_F2_runall.log`（`EXIT=1`·一般模式·未用 `WV_BAKE`）
⇒ `132 名目／86 PASS／46 FAIL`。

### 5-1 名目集合 diff 之實際輸出行（靶＝`verify/out/K8_seg3_C.log`）

```
$ diff <(K8_seg3_C 靶 FAIL 名目 sort) <(F-2 輪 FAIL 名目 sort)
  (無輸出)
$ diff <(K8_seg3_C 靶 PASS 名目 sort) <(F-2 輪 PASS 名目 sort)
  (無輸出)
$ diff <(段二-1c 輪 FAIL 名目 sort) <(F-2 輪 FAIL 名目 sort)
  (無輸出)
$ diff <(段二-1c 輪 PASS 名目 sort) <(F-2 輪 PASS 名目 sort)
  (無輸出)
```

⇒ **四組皆空**、逐字零進零出。

### 🔴 5-2 **但 `run_all` 對本修法之覆蓋＝零**（**同 GB-24 之形狀·不得誤讀上表**）

本修法之三行落在 `main()` 之 Step G **UI 分支**內；`harvest()` 以 AST 跳過 UI、
harness 走 `verify/stepg_pipeline.run_step_g`（另一套 Step G）
⇒ **`run_all` 從不執行這三行**。

⇒ 上表之「零進零出」證明的是「**本修法未波及其他任何名目**」，
**不是**「失效機制已被驗過」。
**本修法之正確性全部由 §四 三項驗證承擔**（該驗證直接 `exec` 倉內真敘述）。
（此為 **GB-24** 已登記之制度性缺口在本批之再現——app 端之 UI 狀態機
**結構上不在 `run_all` 射程內**。）

---

## 六、登記：**GB-25**

- **本項**：Step G 之產物鍵無「進入重算即失效」之機制；`_f3L_invalidate_g_cache`
  只綁二街角 widget 之 `on_change`，改 DXF／屁股線指派均不觸發。**處置＝本單修。**
- **併記**：`f3_corner_winners`／`f3L_corner_winners` 屬 Step G **上游輸入**，
  **不得**納入該失效集合；`f3_g_needs_rerun` 與 `f3_g_needs_recalc` 係兩把不同的鍵。
- **⬜ 待查（登記不改）**：其餘步驟（A〜F、H〜L）是否有同型之
  「產物鍵不隨重算失效」，**本單未掃**，留**泛化波**。

---

## 七、施工單與倉內實況之差異（§六-4）

| 施工單所載 | 倉內實況（`dd02b5b` 當場 grep） | 處置 |
|---|---|---|
| `f3_G_values` `:18761`／`f3_G_trace` `:18762` | 屬實 | — |
| `_f3L_invalidate_g_cache` `:16472-16482` | 屬實（`def` 於 `:16472`·pop 於 `:16476-16479`·旗標於 `:16480`） | — |
| K-9-4 閘 `:18759` | 屬實 | — |
| 成果區 `:18876`／下載鈕 `:18913` | 屬實（皆讀 `f3_G_values`） | — |
| 既有 raise `:17909`·不在任何 `try` 內 | **屬實**（本批以 `ast` 獨立複驗） | — |
| 計算分支 `:17621`／`g_rows=[]` `:17624`／`detail_trace={}` `:17625` | 屬實 | 落點如令 |
| `f3_corner_winners` 寫 `:17126`·讀 `:17630`／`:17929` | 屬實 | 未碰 |
| `f3L_corner_winners` 寫 `:17174` | 屬實 | 未碰 |
| `f3_g_needs_rerun` 讀 `:16491`／`f3_g_needs_recalc` 讀 `:17617` | 屬實（確為兩把不同鍵） | 只碰前者 |
| 成功時清旗標 `:18764` | 屬實 | 狀態機閉合 |

⇒ **本單所載與倉內實況逐項相符，無差異。**
