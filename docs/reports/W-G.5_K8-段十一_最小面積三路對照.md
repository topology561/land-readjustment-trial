# W-G.5 · K-8 段十一 —— **U-K9-3 結案 ＋ 「街角最小面積」三路對照**（只量不判）

**分支**：`wip/s1-endpart`　**起點 HEAD**：`e477b38`
**⛔ 不提假說、不下結論、不改任何一行判準碼、不調參。只以 `data/V6_1.dxf` 跑。未跑 `run_all`。**

> 本報告為本批之**唯一本體**。實料：`verify/out/probe_ruling_K9_corner_width_V6_1.log`【段十一】。

---

## 〇、一句話結論

**`226.88` 與 `232.7931` 不是 live 之「同名兩值」——是「凍結 baseline vs live」之落差。**
`live 參數表` 與 `live PK` **十六格逐格相等（③−② ＝ +0.0000）**；
而 `baseline CSV` 與 live **十六格全部不同**（`+4.63` ～ `+78.31`，另 R6 為負）。
⇒ **交辦文 (4) 之前提（兩路傳入不同）不成立，故未開 GB 條目。**

---

## 一、交付格式證明

基準 commit `e477b38`。

| 檔 | `byteΔ` | `A1` | 說明 |
|---|---|---|---|
| `verify/probes/probe_ruling_K9_corner_width.py` | True | **False** | 本項為真變更（新增段十一量測） |
| **其餘既有 `.py`** | **False（0 檔異動）** | **⇒ `A1` 全為 `True`** | 見 §六 |

**`app.py` 一行未動**；`verify/run_verification.py` 零異動；`V6` 那輪輸出保留未動。

---

## 二、U-K9-3 結案登記（**依 KL 2026-08-03 裁示**）

**U-K9-3 標「判準誤訂·非缺陷」結案。**

- 對稱差實測（段十）：`街角規定範圍(右)` 與 `628(5)` **六頂點中四個逐位相同**，
  只有一條邊沿 `s` 平移 `0.1529m`、**兩端同量** ⇒ **形狀無異常**。
- 溢出 `5.067860㎡` 係**面積差之算術後果**，**與 `628-34(3)` 無關**。
- ⇒ **claude.ai 之「包含關係」判準訂錯**——比的是**多邊形**，
  而程式閘比的是 **`G` vs `226.88`**（純量門檻）。
- 🔴 **記為 claude.ai 之施工單缺陷**（與 U-K9-1 同型：**方法錯了，量得再準也沒用**）。

---

## 三、(1) `226.88` 之產生鏈追查

### 3-a live 產生鏈（逐段·附 `file:line` ＋原始 grep 輸出）

```
$ grep -rn "第 1 宗街角地指配結果" --include="*.py" .
./verify/run_verification.py:636:  ok_s, v_s = diff_rows(sel, os.path.join(BASELINES, f"第 1 宗街角地指配結果_退縮{tag}.csv"),
./app.py:16788:  st.markdown("##### 🥇 第 1 宗街角地指配結果（左右側獨立）")

$ grep -rn "最小面積" --include="*.py" verify/ | grep -v "probes/"
verify/run_verification.py:252:  "【左】街角最小面積(㎡)": (rng("left")  if has_l else None),
verify/run_verification.py:253:  "【右】街角最小面積(㎡)": (rng("right") if has_r else None),
verify/selection_pipeline.py:378:  _l_min_val = _row.get('【左】街角最小面積(㎡)')
verify/selection_pipeline.py:379:  _r_min_val = _row.get('【右】街角最小面積(㎡)')
verify/selection_pipeline.py:542:  '【左】最小面積(㎡)': _l_disp_min,
verify/selection_pipeline.py:543:  '【右】最小面積(㎡)': _r_disp_min,
```

```
verify/run_verification.py:236   chi = ns["_make_chamfer_tri_wb"](b, which)
verify/run_verification.py:237   r = ns["_build_corner_range_v3"](…, chi, …)
verify/run_verification.py:241   return round(float(r.area), 2) if r is not None else None
verify/run_verification.py:252/253   "【左/右】街角最小面積(㎡)": rng(side)
        ↓
verify/selection_pipeline.py:378/379   _l_min_val / _r_min_val = _row.get('【左/右】街角最小面積(㎡)')
verify/selection_pipeline.py:384/385   _min_p1 / _min_p2 = float(_l_min_val / _r_min_val)
verify/selection_pipeline.py:509/510   _l_disp_min / _r_disp_min = f"{round(_min_p1 / _min_p2, 2)}"
verify/selection_pipeline.py:542/543   '【左/右】最小面積(㎡)': _l_disp_min / _r_disp_min
        ↓
verify/run_verification.py:636   diff_rows(sel, BASELINES/"第 1 宗街角地指配結果_退縮{tag}.csv")
```

⇒ **live 鏈自始至終只有一個來源：`_build_corner_range_v3(...).area`。
鏈上無第二個算式、無再乘除、無另行扣減。**

### 3-b 「分家的那一點」

**不在碼裡——在檔案。** `226.88` 係**凍結 baseline CSV 之內容**，非 live 算出：

```
$ git log -1 --format="%h %ad %s" --date=short -- "verify/baselines/第 1 宗街角地指配結果_退縮3.5m.csv"
1b290e4 2026-07-05 初始遷移:市地重劃試分配系統(淨土倉,零歷史)

$ git log -1 --format="%h %ad %s" --date=short 56b345a
56b345a 2026-07-31 K-8 段三 commit C: GSA_EXPECT 重錨解封 ＋ 146.50㎡ 舊基準退場

$ git merge-base --is-ancestor <baseline 最後異動 commit> 56b345a
  ✅ 成立 ⇒ **baseline 早於 K-8 §三〜§五 落地 26 日**
```

⇒ **`226.88` ＝ 舊構造（K-8 §三〜§五 之前）之凍結值；
`232.79` ＝ 新構造之 live 值。**

**左側 `226.18`（對照）**：同一鏈、同一檔、同一 commit ⇒ live 為 `230.81`，差 `+4.63`。

---

## 四、(2) 各路傳入之 `chamfer_tri`（**據實列出·不判斷哪一支對**）

```
$ grep -rn "_build_corner_range_v3" --include="*.py" .   （扣除 docstring／harvest 清單／夾具說明）
app.py:9237      def _build_corner_range_v3(…, chamfer_tri=None, …)      ← **簽名預設值**
app.py:9656      _build_corner_range_v3(…, _cham_wb, …)
app.py:16339     _build_corner_range_v3(…, _make_chamfer_tri_wb(b, _wh_cr), …)
verify/run_verification.py:237   ns["_build_corner_range_v3"](…, chi, …)
verify/probes/probe_ruling_K9_corner_width.py:451   ns["_build_corner_range_v3"](**kw)  （kw["chamfer_tri"]）
```

| 呼叫點 | 傳入之 `chamfer_tri` | 走哪一支（`app.py:9416-9417`） |
|---|---|---|
| `app.py:9656` | `_cham_wb` ＝ `_make_chamfer_tri_wb(_blk_meta_wb, side)`（`app.py:9638-9639`） | **`rng.difference(chamfer_tri)`** |
| `app.py:16339` | `_make_chamfer_tri_wb(b, _wh_cr)` | **`rng.difference(chamfer_tri)`** |
| `verify/run_verification.py:237` | `chi` ＝ `ns["_make_chamfer_tri_wb"](b, which)`（`:236`） | **`rng.difference(chamfer_tri)`** |
| 本探針 `_build_range` | `ns["_make_chamfer_tri_wb"](b, side)` | **`rng.difference(chamfer_tri)`** |

⇒ **四路皆傳入截角三角形；無一走 `chamfer_tri=None`。**
`app.py:9239` 之 `chamfer_tri=None` **僅為簽名預設值，無任何呼叫點採用**。

⇒ **交辦文 (2) 所設想之「兩路傳入不同」不成立。**

---

## 五、(3) 三路對照（**八街角 × 兩情境 ＝ 16 格·只列數字·不判定何者為真值**）

⚠️ 交辦文寫「六街廓 × 兩情境（12 格）」；**實際街角側為 8 個**（R1 左右／R2 左／R3 右／
R4 左右／R5 左／R6 右）⇒ **16 格**。

| 情境 | 街廓/側 | ① baseline CSV | ② live 參數表 | ③ live PK | ②−① | ③−② | 截角△(㎡) |
|---|---|---|---|---|---|---|---|
| 0m | R1/left | 109.79 | 114.76 | 114.76 | +4.9700 | **+0.0000** | 6.7104 |
| 0m | R1/right | 110.56 | 116.84 | 116.84 | +6.2800 | **+0.0000** | 5.7711 |
| 0m | R2/left | 151.44 | 225.69 | 225.69 | +74.2500 | **+0.0000** | 6.2802 |
| 0m | R3/right | 152.82 | 226.91 | 226.91 | +74.0900 | **+0.0000** | 6.2014 |
| 0m | R4/left | 109.2 | 135.17 | 135.17 | +25.9700 | **+0.0000** | 6.8578 |
| 0m | R4/right | 109.7 | 137.02 | 137.02 | +27.3200 | **+0.0000** | 6.2797 |
| 0m | R5/left | 146.93 | 225.24 | 225.24 | +78.3100 | **+0.0000** | 6.1431 |
| 0m | R6/right | 146.38 | 145.88 | 145.88 | **−0.5000** | **+0.0000** | 5.7664 |
| 3.5m | R1/left | 226.18 | 230.81 | 230.81 | +4.6300 | **+0.0000** | 6.7104 |
| **3.5m** | **R1/right** | **226.88** | **232.79** | **232.79** | **+5.9100** | **+0.0000** | 5.7711 |
| 3.5m | R2/left | 309.05 | 382.85 | 382.85 | +73.8000 | **+0.0000** | 6.2802 |
| 3.5m | R3/right | 308.93 | 383.67 | 383.67 | +74.7400 | **+0.0000** | 6.2014 |
| 3.5m | R4/left | 225.25 | 251.1 | 251.1 | +25.8500 | **+0.0000** | 6.8578 |
| 3.5m | R4/right | 225.67 | 252.87 | 252.87 | +27.2000 | **+0.0000** | 6.2797 |
| 3.5m | R5/left | 300.52 | 378.47 | 378.47 | +77.9500 | **+0.0000** | 6.1431 |
| 3.5m | R6/right | 299.13 | 298.14 | 298.14 | **−0.9900** | **+0.0000** | 5.7664 |

**數字事實**：

- **`③−② ＝ +0.0000` 十六格全中** ⇒ live 參數表與 live PK **無落差**。
- **`②−①` 十六格全部非零**，範圍 `−0.99` ～ `+78.31`。
- **R1/right 之 `+5.91` 在十六格中屬最小之列**（僅大於 R1/left `+4.63` 與 R6 之兩負值）。
- **R6 為唯一之負差**（0m `−0.50`／3.5m `−0.99`）。
- 截角三角形面積 `5.7664` ～ `6.8578㎡`；**與 `②−①` 之各格差值無一相等**
  （R1/right：`5.9100` vs `5.7711`，差 `0.1389`）。**本表不據此推論。**

---

## 六、(4) GB 條目：**未開**（條件不成立）

交辦文 (4) 之條件為「**若 (2) 顯示兩路傳入不同**」。
**(2) 實查結果：四路皆傳入 `_make_chamfer_tri_wb(...)`、無一走 `None` 預設**
⇒ **條件不成立，故未開 GB 條目。**

`①` 與 `②/③` 之落差**非 live 之同名兩值**，而係**凍結 baseline 未重烤**——
該情形**倉內已有登記**，不另立新條目：

- `CLAUDE.md`「現行驗收基線」：**46 紅 ＝ 2 既有 ＋ 22（門檻源）＋ 22（街角幾何源），
  全數已歸因、待波末重烤消化**。
- **GB-16**（換圖＝重烤觸發·段六）：換圖與換快照須併入**波末批同一次重烤**。

---

## 七、本批未做

- **未提假說、未下結論、未判定何者為真值**（交辦文明令）。
- **未開 GB 條目**（條件不成立·見 §六）。
- 未改判準、未設門檻、未調參、未掛 `run_all`、**未動 `app.py` 一行**。
- **未重跑 `V6` 那輪**（其輸出保留）。

---

## 八、段十一之後

1. **K-6-A2**：K-9 全八則之實作（GB-13／14／18／19）。
2. **波末批**：換圖＋換快照＋**重烤（含本表 ① 之 16 格）**——同一次烤完（GB-16）。
3. **泛化波**：GB-17 全倉資產校驗碼掃描、恆真閘家族（GB-10）、去錨。
