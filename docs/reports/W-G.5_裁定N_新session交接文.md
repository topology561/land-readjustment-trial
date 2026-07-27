# W-G.5 裁定 N — **新 CC session 交接文**

> 基準 `HEAD == origin/wip/s1-endpart == f105f3a`（本文寫入時）。
> 紀律：凡「已修／已驗／已量」之宣稱**均附實測輸出**；無輸出即視為未驗。
> **行號一律當場 grep 復驗**——本文只給符號名（`CLAUDE.md` 🔒 行號衛生）。

---

## 〇、一分鐘定位

裁定 N（分配起算點）已由 KL 三輪定案：
**乙案**（起算點不動、迭代式加常數項）＋ **N-12′～N-19** ＋ **C-1～C-12** ＋ **K-1～K-3** ＋ **E 系列**。

**U7 已裁「丙」**：本波只做**不改分配幾何**之項；**P-2／P-4／P-6 延後**；**P-H baseline 續凍**。
⇒ 上一 session 共 11 枚 commit（`25342cd..f105f3a`），**run_all 全程維持
56 PASS／14 FAIL、FAIL 名目與基準逐字全等**。

**你這批＝續做剩餘丙案項**（見 §四），非重啟。

---

## 一、必讀（依序·勿跳）

1. `CLAUDE.md`（尤其 🔒 未 push 不得報收官／🔒 行號衛生／回報鐵律）
2. `.claude/skills/cad-layer-semantics/SKILL.md` —— **本波正典主場**，
   含 BASELINE 1:N、FRONT/SIDE 綁定、C-5 三分支＋eps 公式、四件套、**K-1/K-2/K-3**、
   **可達宗地形狀集合**
3. `.claude/skills/failure-archaeology/SKILL.md` **#28／#29**（本波新增）
4. `docs/reports/W-G.5_裁定N_第二批_必辦實測與連動清查.md`（N-16(d) 連動 11 點）
5. `docs/specs/W-G.5_裁定N_乙案_plan_v3.md`（P-1～P-10 之 plan·delta over v2）

---

## 二、倉態

- `HEAD == origin/wip/s1-endpart == f105f3a`
- **既有 🚩·勿動勿 commit**：`data/地籍資料來源_匿名版.xlsx` 未 commit 異動
- 既存 untracked（**本波未動**）：`.agents/`／`.codex/`／`.tmp.driveupload/`／
  `AGENTS.md`／`data/r3.dxf`／大量 `verify/out/*.log`
- 環境：`pip install --break-system-packages -r requirements.txt`
- `python verify/run_all.py` 約 15 分鐘 ⇒ **背景跑＋等通知**，勿前景阻塞

---

## 三、本波已完成（11 commit·逐項可查）

| commit | 內容 |
|---|---|
| `effc29d` | 偵察：s 域全量測＋試算＋守恆＋家族清查（**甲案**·後由乙案取代） |
| `ff2f504` | plan v1→v3 二輪 reviewer 審查鏈＋P-8 實測；U7 上呈 |
| `f2aa653` | N-12′／N-19／N-2′ 三必辦實測 |
| `6e64169` | 必辦實測報告＋N-16(d) 連動 11 點清查 |
| `3653494` | **C-1~C-4** BASELINE 配對改結構性 1:N |
| `81e98ca` | **C-6/C-7/C-11/C-12** 線層綁定改共線＋重疊最長；歧義改 UI 承接 |
| `d390251` | **C-5 補件** 多候選三分支 |
| `27af2ba` | **C-5 收尾** 分支①改「量測值等價」 |
| `5233293` | **C-5 結案** eps 改法定粒度＋DXF 實測 q 之公式 |
| `ee615fc` | **D-1~D-7＋N-13＋N-15** |
| `f105f3a` | **E-1′~E-5＋E-7＋K 鎖典** |

**新增夾具（皆入 `run_all`·現 6 枚 rc=0）**：
`fixture_cad_binding_order.py`（順序不變性）／`fixture_baseline_candidates.py`（C-5 三分支）／
`fixture_n14_min_width.py`（N-14 可達形狀九格）＋既有三枚 end 夾具。

**新增探針（零注入·唯讀）**：`verify/probes/probe_ruling_N_recon.py`／`probe_ruling_N_p8.py`／
`probe_ruling_N_depth.py`／`probe_ruling_N_c7_sideline.py`。

---

## 四、🔴 你這批要做的（優先序·KL 指定）

### 4.1 E-6 跨層自檢（新格·掛 run_all）
以 UC9898 實資料，對所有**中間宗地**斷言
`|parcel_min_width_n14(...) − 由 cut_coords 量得之臨街邊長| ≤ 1e-6`。
⚠️ 比對對象是**幾何量得之臨街邊長**，**不是** `f3_G_values` 的 `S(m)` 欄。
**已知可用**：非街角宗 51/51 通過 `parcel_min_width_n14`（街角宗 8 筆依 E-7 跳過）。

### 4.2 N-16(c) 廢止**三條** MinA 計算線
`f3_min_alloc_area_by_label`（寫 1／讀 1）／`_min_area_by_block`（算＋**else 分支**）
——**三條缺一不可**。自癒 grep：
`grep -n "f3_min_alloc_area_by_label\|_min_area_by_block" app.py`。
連動 11 點見 `docs/reports/W-G.5_裁定N_第二批_必辦實測與連動清查.md` §五。

### 4.3 N-17 ＋ K-2 三物件分家（**合併施作**）
`_build_corner_range_v2` **七處呼叫已定位**（`grep -rn "_build_corner_range_v2(" --include=*.py .`）：
- **(Ⅰ) 街角規定範圍**（傳 `shift`＋`chamfer`）：`app.py` 8921／8925／15549／15556
- **(Ⅱ) 18m 負擔範圍**（`chamfer=None`）：8008（傳 `burden_shift`）／15565／15570（**硬編 18.0**）
- **(Ⅲ) 量測用虛擬範圍**＝**新增物件**（實配街角宗補回截角）
**先分家再改，勿一改兩壞**。函式內 **三處 bare except** 一併改 loud raise
（`grep -n "except Exception" app.py` 於該函式段）。
夾具錨：`verify/run_verification.py` 之 `_build_corner_range_v2` 相關閘。

### 4.4 E-7 接上 (Ⅲ)
N-17 落地後**立即**把街角宗之寬深量測接到 (Ⅲ)。
**接上之前，街角宗不得輸出寬度合格與否之結論**（現況已如此：`實際寬度(m)=None` ＋
`_width_chamfer_pending=True`）。

### 4.5 2dp 取位範圍限縮
**只改回饋進比較／閘者**：MinA、實際寬度。
⚠️ **禁全庫替換 `round(`**；⚠️ `Decimal(float).quantize` 仍錯，須 `Decimal(repr(v))` 或純 `Decimal`。
**現況查核（KL 已驗·勿動）**：全庫已無天真 `Decimal(float)`；
`wd4_tier_list._half_display` 用 `Decimal(str)` **正確**；真正的閘是 `2×ΣG ≥ MinA`（無除法）
⇒ **此二處維持原樣**。

### 4.6 P-1／P-5／P-7／P-9／P-10
- **P-1** 規格定稿入 `docs/specs/W-G.5_裁定N_分配起算點.md`（N-2′／N-9～N-19 全文＋原 N-1 作廢眉批）
- **P-5** UI「街廓最小建築面積」欄（每街廓一格·**可空白＝無規定**·**禁以 0 當無規定**）
  ＋ **子項**：C-11 持久化須讓 **headless 可讀**已記錄之消歧選擇
  （否則較粗圖資會直接卡住夾具）；**持久化禁存 DXF handle**（重匯出會變），須存幾何
- **P-7** `wf_f1` 死碼常數 `TARGET_ANCHOR`／`WEDGE_AREA_ANCHOR` 及其 5 處消費點整段刪
- **P-9** 更正登記（B-1 `_corner_buffer_S` **7 個呼叫點**／B-4 78.24 結旗）
- **P-10** N-6 明確延後之記帳

**延後**：P-2／P-4／P-6。**P-H baseline 續凍。**

---

## 五、🚩 上呈 KL·未裁（施工前確認）

| # | 題 | 現況暫採 |
|---|---|---|
| **U-A** | **E-1′ 容差偏離 KL 字面 `1e-6`** | 取 **法定粒度 0.01m**。理由：實測 59 筆業主宗中 **45 筆**距 FRONT 僅 **4µm～247µm**（BLOCK 邊 vs FRONT_LINE 之圖層精度差），而倉內正典早已點名「**1e-6 會漏量**」。若堅持 1e-6，該閘會對 45/59 正確宗地誤報 |
| **U-B** | N-16(b) 之 `min_width` 取「全區最小」抑或「最淺街廓自身」 | UC9898 六塊皆 3.5 ⇒ **兩讀同值·本案無法區辨**，泛用化前須釐清 |
| **U-C** | 池不變式「池 ∈ {0}∪[MinA,∞)」在「該街廓**未輸入**最小建築面積」時如何成立 | 退化為恆真（容許任意碎池）抑或改掛 N-16(b) 區內值——**法律效果不同** |
| **U-D** | N-19／N-16(b) 之定值 | **暫定 115.87／½ 線 57.94**（最淺 R4 33.1046，惟**只贏 R1 4.15cm**）。⚠️ **KL 令：尚未寫入任何錨或閘**；現行錨仍為 114.07／57.04 |

**已裁畢·勿再問**：U7（丙）／U1（solo G）／U2·U3·U9（N-12′ 取代）／U8（N-18 五段）／
K-1·K-2·K-3。**K-2 末段 winner 權值併查已完成 ⇒ 不需停機**（見 §六.4）。

---

## 六、🔑 本波血訓（新 session 先讀·**都是實際踩過的**）

### 6.1 「宣告 ≠ 成立」——同一份文件裡的自相矛盾
- 我寫「**非**以觀測殘差反推閘寬(N0-17)」，**下一行**就是「較實測最大 5.795e-6 留 17 倍餘裕」。
- 我建了新 eps 公式，卻沒清掉舊符號引用 ⇒ 正典**上半用舊閘、下半用新公式**；
  而該檔往上三行正是「`_extract_cad_lines` 是過期名」的警語。
⇒ **改依據時，要一併搜出所有引用該依據的地方**。

### 6.2 「異常偵測正確 ≠ 歸因正確」（失敗考古 **#28**）
我量到 R2 深度發散 0～1414m（正確），卻歸因為「R2 畫錯圖層」「R1/R5 圖沒畫」，
並**請 KL 補圖**。真因是**配對器 1:1 貪婪耗盡 ＋ 端點座標完全重合**。
⇒ **歸因為「請人補資料」之前，先證「程式在資料完整時會對」**——舉證責任在提出者。

### 6.3 「修主路徑漏支路 ＝ 沒修」
C-1/C-2 修好 1:N 與端點重合，卻讓決勝仍是「垂距最小靜默取」——
而 **唯一薄的那個綁定（R1 勝差 0.05m）正是唯一沒有閘的**。
⇒ **建了歧義機制後，要回頭盤點所有同類決勝點是否都接上。**

### 6.4 「自標風險點 ≠ 真風險點」（連續兩輪）
plan v1 我把旗插在定點迭代斷言（reviewer 驗後：沒事）；
v2 插在 union 對池片之衝擊（又沒事）。真 BLOCKED 兩輪都在沒插旗處
（重烤授權／`try` 邊界／PK 側別／取樣產物）。
⇒ **reviewer 之全部價值＝獨立復現**；自評 gate 綠不可自我採信。

### 6.5 取樣 min 是陷阱
「沿某軸取 min」若用等距取樣，**值會隨取樣密度飄**（實測 40.2776→1.9943→0.1994）。
⇒ 分段線性者**只在斷點取值**（`parcel_min_width_n14` 即如此）；
非分段線性者須有**排除帶定義**，且該定義須有法源。

### 6.6 容差之**身分**要對
`perp_tol`（繪圖誤差·公尺級）≠ 數值等價容差（微米級）≠ 法定粒度（0.01m）。
量綱同為公尺、意義完全不同 ⇒ 借用即 **N0-17(a) 跨來源借用**。
**每個門檻都要能說出它的法源或物理來源**，「實測留 N 倍餘裕」不算依據。

### 6.7 夾具期望值本身會錯
我在夾具註解寫 `L/ℓ = 1.33335`（只算了一個候選），碼取各候選**最大** ⇒ 實為 `1.612452`。
⇒ **夾具裡的錯誤手算值最會誤導後人**；手算要跟碼的聚合方式一致。

### 6.8 `; echo "EXIT=$?"` 會吞掉退出碼
背景任務回報 exit 0 而 python 實已 traceback。
⇒ 一律 `rc=$?; …; exit $rc`。（此即交接文既有 §8.1「紅著卻報綠」之工具鏈版。）

---

## 七、機制速查（符號名·**用前當場 grep**）

| 概念 | 查法 |
|---|---|
| N-14 宗地最小寬度 | `grep -n "def parcel_min_width_n14" app.py` |
| DXF 坐標量化 q | `grep -n "def _detect_dxf_quantum" app.py` |
| 線層↔街廓重疊原語 | `grep -n "def _line_block_overlap" app.py` |
| 綁定歧義例外／UI | `grep -n "class CadBindingAmbiguity\|def render_cad_binding_confirm" app.py` |
| CAD 線層綁定總成 | `grep -n "def parse_cad_precision_layers" app.py`（⚠️ `_extract_cad_lines` 是**過期名**） |
| 街角 winner 三指數母體 | `grep -n "_corner_poly_p1_B4 = " app.py` → `_corner_range_left`（＝(Ⅰ)） |
| 街角規定範圍／負擔範圍 | `grep -rn "_build_corner_range_v2(" --include=*.py .`（七處·見 §4.3 分類） |
| 寬度旗標 | `grep -n "_below_min_width\|_width_chamfer_pending" app.py` |

---

## 八、驗收與停機

**每枚 commit 前跑 `run_all`**，須維持 **56 PASS／14 FAIL** 且 **FAIL 名目逐字全等**：

```bash
python verify/run_all.py > verify/out/<tag>.log 2>&1; rc=$?; echo "REAL_EXIT=$rc" >> verify/out/<tag>.log; exit $rc
```

比對：`grep "🔴 FAIL" verify/out/<tag>.log` 對 `verify/out/M_0725_F10_after.log` 之 FAIL 集合 **diff 須空**。
另須：**禁寫死絕對路徑閘 0 命中**、**六夾具 rc=0**。

**停機準則**：只有**真觸及域邊界**（法規解釋、土地分配後果、需 KL 裁定之新機制）才停機上呈；
純技術項一路 plan→reviewer→施工→push 做完，**不要回問**。
