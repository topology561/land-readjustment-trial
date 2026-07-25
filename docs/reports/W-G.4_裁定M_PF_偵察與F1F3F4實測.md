# W-G.4 裁定 M — **P-F 偵察 ＋ F-1／F-3／F-4 實測**

> 基準 `c057a32`（`HEAD == origin/wip/s1-endpart`）。**本文為 P-F 之偵察＋可實測項落地，尚未動 F-2／F-5／F-6**。
> 紀律：凡「已驗／已咬合」之宣稱，**均附實際輸出行**（log 檔:命中數 或原文貼出）。無輸出者一律標「未驗」。

---

## 〇、一句話

**P-F 六項中，F-3／F-4 續綠、F-1 值錨三項全中**；但 F-1 之真資料**在非 BAKE 下結構性量不到**
（F.0 raise ⇒ `wf_f4` 不跑 ⇒ 零階段2宗 ⇒ `_place_pool_parcels` 零呼叫），
**plan v4 之 P-F→P-H 排序與此相依倒置**（§四）。另查獲 `wf_f4` 行號錨**三處全過期**（§三），
F-2 之施工靶即掛在其上，**須先更正**。

---

## 一、倉態與讀數復現

| 項 | 值 | 出處 |
|---|---|---|
| `HEAD` == `origin/wip/s1-endpart` | `c057a32` | `git rev-parse` 二值相同 |
| working tree | 僅 `data/地籍資料來源_匿名版.xlsx` modified（歷次刻意排除） | `git status --porcelain` |
| **非 BAKE `run_all`** | **56 PASS ／ 14 FAIL** | `verify/out/M_0725_PF_nobake.log` |

> ⚠️ **log 命名撞車已避開**：倉內既有 `verify/out/M_PF_runall_{nobake,bake}.log`（`1a1cb00` 加入，
> 係 **F-1~F-5 修補批次**之 log·讀數 53 PASS/14 FAIL 與 157 PASS/1 FAIL，**非 P-F**）。
> 本波之 log 一律改用 `M_0725_PF_*` 前綴，勿與之混引。

**FAIL 組成逐列復現交接文 §二**（14 列，無增無減）：

```
v3·診斷3.5m（全欄逐格·無豁免）
率接線無串聯3.5m（vs v1 原錨，豁免 G估 後逐格全等）
指配3.5m
抵費地3.5m
v3·G值3.5m
v3·滑池槽3.5m
v3·J表3.5m
k* 六塊經驗錨3.5m {'R1': 1, 'R2': 8, 'R3': 7, 'R4': 1, 'R5': 7, 'R6': 6}
W-F F.0 / W-F F.1 / W-F F.2 / W-F F.3 / W-F F.4
W-G G.2 世代幾何曝出契約
```

即 3.5m baseline 7 列（R-7）＋ `k*3.5m`（R-4/R-5）＋ F.0~F.4 五列 raise 級聯 ＋ G.2。**獨立復現成立**。

F.0 之 raise 原文（`M_0725_PF_stage2diag.log`）：

```
[F.0] 🔴 GSA 錨檢破（3.5m）——**一次列出全部**（F-7-3：禁首個即 raise 致打地鼠）：
  【值不符 1 項】G014 G(Σa)=128.07 ≠ 錨 129.2
  【未被評估】錨鍵 ['G007'] **未被任何一次比對評估**（其決策現況：G007→[R3:全達標·無須併(無target)]）
```

⇒ 即登記表之 **R-2**（G014 129.20→128.07）與 **R-3**（G007 待 P-H 刪鍵或改值），**與登記表逐字對得上**。

---

## 二、P-F 各項現況

### F-3 `fixture_end_reserve.py` — **12/12 ✅**（`verify/out/M_0725_PF_end_reserve.log`·exit=0）

```
[left]  驗0 末端帶 s 區間：實測 (0.0000, 3.5000)  手算 (0.0000, 3.5000)  Δ=0.00e+00  ✅
[left]  驗1 窗起點 gate關/開：0.0000 / 3.5000     窗寬 gate關/開：40.0000 / 36.5000  ✅×4
[left]  驗1 窗寬縮減 ＝ 3.5000（＝MW ＝ 3.5000）  ✅
[right] 驗0 末端帶 s 區間：實測 (36.5000, 40.0000) 手算 (36.5000, 40.0000) Δ=0.00e+00  ✅
[right] 驗1 窗起點 gate關/開：0.0000 / 0.0000     窗寬 gate關/開：44.0000 / 36.5000  ✅×4
[right] 驗1 窗寬縮減 ＝ 7.5000（＝F+MW ＝ 7.5000）  ✅
RESULT: PASS
```

### F-4 `fixture_end_fallback.py` — **左右各 5 項 ✅**（`verify/out/M_0725_PF_end_fallback.log`·exit=0）

```
[left]  0直測band∧frag∧R_end:✅  ①抵費地末=R_end:✅  ②帳池==幾何池:✅  ③非疊:✅  ④G守恆:✅
[right] 0直測band∧frag∧R_end:✅  ①抵費地末=R_end:✅  ②帳池==幾何池:✅  ③非疊:✅  ④G守恆:✅
RESULT: ALL GREEN ✅（左右雙向）
```

⇒ **M-5 落地未打到兩 fixture**。二者現為末端機制**唯一活的證據**（見 §四）。

### F-1 3.5m 末端保留 — **值錨三項全中**（量法見 §四）

`verify/out/M_0725_PF_bake_diag.log`（3,173,676 bytes）：

```
=== 末端保留 命中 21 ===
   21x  街廓 R6｜末端保留 left: 未臨正街 85.706㎡·末端帶 s∈[-0.0000,3.5114]
```

| 對拍項 | BEFORE 錨（`W-G.4_§4_P2_兩階段落位_f到g.md:102`） | 本次實測 | |
|---|---|---|---|
| 觸發塊 | 唯 R6 左 | 唯 R6 左 | ✅ |
| 未臨正街面積 | 85.706㎡ | 85.706㎡ | ✅ |
| 末端帶 s 區間 | `[-0.0000, 3.5114]` | `[-0.0000,3.5114]` | ✅ |
| 觸發次數 | 10 | **21** | ⚠️ 見下 |

**覆蓋率咬合實證**（防「沒人檢查≠相符」）——六塊全被 `_place_pool_parcels` 走過，只 R6 觸發：

```
844x R1   846x R2   850x R3   469x R4   844x R5   21x R6
```

R6 之 21 次呼叫 **21/21 觸發**；R1~R5 之 3853 次呼叫**零觸發**。

⚠️ **次數 10→21 不作「已解釋」宣稱**：本趟在 `WV_BAKE` 下跑，**控制流本身已不同**
（GSA 硬閘由 raise 降為 print ⇒ F.1~F.4 得以執行，而 `_place_pool_parcels` 之絕大多數呼叫來自
`wf_f4` E1/E2 之 `_trial` 逐 gid×blk 探針·見 `app.py:7559-7560` 註）。
⇒ **次數與 BEFORE 不可直比**，非「值變」。F-1 所斷言者為三項**值**錨，該三項逐字全中。

### F-2／F-5／F-6 — **未動**（F-2 之靶須先更正，見 §三）

---

## 三、🔴 `wf_f4` 行號錨**三處全過期**（F-2 施工前必更正）

`verify/wf_f4.py` 共 **1588 行**。當場 grep ＋ 二法覆核（ripgrep／PowerShell 陣列索引）：

| 引用處 | 宣稱 | **實測** | 該行實際內容 |
|---|---|---|---|
| `plan_v4.md:341`／交接文 §三 | `_cond1` ＝ `wf_f4:1325` | **1338** | 1325 ＝ `return cut, float(area)` |
| 同上 | `_end_gate` ＝ `:1338` | **1351** | 1338 正是 `_cond1` |
| `plan_v4.md:342` | 末端 winner 前後集合 ＝ `:1350` | **1363** | 1350 ＝ `_unfront_area` 運算式續行 |
| 同上 | 「`1467/1480` 不存在」 | **兩行皆存在** | 1467 ＝ 畸零寬檢查；1480 ＝ `G_E(㎡)` 組列 |
| `stepg_pipeline.py:816` 註 | 「同 wf_f4 `_reshape_block` :1311」 | **1337-1338** | 1311 ＝ `corner = p1 + _smax_f4 * d_hat` |

位移一致為 **+13**。成因：plan v4 之 BEFORE 錨為 `df9834c`，而 `556bf8e`（F-6）在該區塊上方增行；
交接文寫於 `5e04b38`（`556bf8e` 之後）**照抄舊數而未重 grep**，並冠以「三輪 grep 定讞」。

> **教訓（延伸交接文 §5.4／§5.5）**：`檔:行` 之保鮮期＝**下一次該檔被改**。
> ⇒ 修法不是「再 grep 一次填新數」，而是**引符號名、不引行號**（行號僅作輔助且標註取數 commit）。
> 本文所有位置引用皆同時給符號名。

---

## 四、🔴 P-F F-1 與 P-H 之**相依倒置**（排序問題·CC 不自裁）

**鏈條（逐環實測·非推論）**：

| # | 事實 | 出處 |
|---|---|---|
| 1 | 階段2宗＝`wf_f4` 注入之池內遞補合成宗，唯一標記 `"配地階段": "池內"` | `verify/wf_f4.py:201`（`add_syn`） |
| 2 | `_stage2_parcels = [tp for tp in parcels_in_blk if '配地階段' in tp]` | `verify/stepg_pipeline.py:359` |
| 3 | `if _stage2_parcels:` 才呼叫 `_place_pool_parcels` | `verify/stepg_pipeline.py:793` |
| 4 | F.0 raise（R-2／R-3）⇒ F.1~F.4 全被存在性守衛跳過 | `M_0725_PF_nobake.log` |

⇒ 非 BAKE 下 `wf_f4` 不跑 ⇒ **零階段2宗** ⇒ `_place_pool_parcels` **零呼叫** ⇒ `[P2-STAGE2]` 命中 **0**。

**⚠️ 差點誤判之處（存記）**：首跑 grep `末端保留` 得 0，若照字面收下會寫成
「M-5 落地後末端機制不再觸發」——**是錯的**。`app.py:7563` 之診斷**預設關閉**
（`if _verbose and _diag and os.environ.get('WV_STAGE2_DIAG') == '1'`），沉默是預期、不是證據。
補跑 `WV_STAGE2_DIAG=1` 後兩 log **SHA256 逐位相同**（`6E5C12BE…`），證確實無事件可印
（env 傳遞另以 `python -c` 驗為 `'1'`，且 `run_all.py` 係 in-process `import run_verification`、無子行程遮蔽）。
＝倉內已付學費之「**log 沉默 ≠ 事件未發生**」再現。

**量法（本次採用·誠實聲明）**：以 `WV_BAKE=<scratch>` 作**執行致能器**——BAKE 下 GSA 硬閘降為 print，
F.0~F.4 得以跑完、逼出真 diag。**明確不取本趟任何 PASS 數當品質證據**
（`run_verification.py:279-285` 於 BAKE 下 `_bake_csv(...); return True, []` ＝不比對即回綠）。
倉內 baseline **零異動**（`git status --porcelain verify/baselines` 空），69 檔全落 scratch。

**⇒ 排序結論**：plan v4 §一 把 **P-F 排在 P-H 之前**，但 F-1「實測非 prose」之**原生**可量測性
繫於 R-2/R-3 重錨後 F.0 轉綠（＝P-H）。目前 F-1 只能以 BAKE 致能法取得，該法**足以坐實值錨**，
但**不能**同時作為「harness 真比對下亦然」之證據。

🚩 **上呈（CC 不拍板）**：F-1 是否接受「BAKE 致能法」為 P-F 之終局證據，
抑或 F-1 須於 P-H 後以非 BAKE 重測一次（則 P-F 拆為 P-F(前) ／ P-F′(後)）。

---

## 五、次步（待 KL 確認後動工）

1. **F-2**：依 §三 更正三處行號錨並改為引符號名；斷言靶改為 `_end_gate` 之 `_unfront_area`
   ＋ `wf_f4.py:1363`（`_qual and (not _end_gate or G ≥ _area_rend)`）之末端 winner 前後集合。
   **凡新立閘必造反例證其會紅**（交接文 §5.2）。
2. **F-5** E3 latent／**F-6** 被消費源宗為末宗時之 `_end_band` 窗重列（左右各驗）。
3. §四之 🚩 待裁；交接文 §四之四項待裁（含 BK-4）仍未裁。

---

## 六、本次新增之 log（皆入 `verify/out/`）

| 檔 | 內容 |
|---|---|
| `M_0725_PF_end_reserve.log` | F-3 fixture·12/12 PASS |
| `M_0725_PF_end_fallback.log` | F-4 fixture·左右各 5 項 ALL GREEN |
| `M_0725_PF_nobake.log` | 非 BAKE `run_all`·56 PASS/14 FAIL（權威讀數） |
| `M_0725_PF_stage2diag.log` | 同上＋`WV_STAGE2_DIAG=1`·與前者 SHA256 相同（證沉默非旗標失效） |
| `M_0725_PF_bake_diag.log` | BAKE 致能＋diag·F-1 三項值錨＋六塊覆蓋率（**PASS 數不可採信**） |
