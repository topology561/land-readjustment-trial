# W-G.4 S1 §4 末端塊 fallback 碼側收尾

> **⚠️ 碼完成＋by-construction 驗訖·最終收官待波末重烤**（W1 defer·KL 採 claude.ai 建議）。
> §4 winner diff=0 之 **execution 復現**延波末（F.4 因 F.0 過期錨級聯跳過·現不可達）——**非最終收官**。

- 日期：2026-07-21；branch `wip/s1-endpart`；canonical＝`docs/specs/W-G.4_規格v3補丁十_N0-20末端塊fallback定案.md` §一（KL 域＋claude.ai 規格）。
- commit trail：`dc154cd`（[A]/[B]/[C]＋夾具）→ `35f60ab`（W2 夾具真檢）→ `e5ff7a9`（W3 右式＋左右雙向夾具）。

---

## 一、落地清單（碼＋commit）

| 項 | 內容 | commit |
|---|---|---|
| **[A]** | `_end_region_R`（app.py·未臨正街＝`frag["poly"]`〔補丁十乙〕·末端帶＝⊥ALLOC 平移 min_width·缺 cad_alloc loud）＋gate（**二條件**：無 SIDELINE ＋ 該側未臨正街半平面>ε）＋winner 門檻（`G≥area(R_end)`·往後找·非嚴格首筆）＋**無勝者 fallback**（抵費地末＝R_end 占末端位·候選內移非疊·位次序不變） | `dc154cd` |
| **[B]** | 池重定位（wf_f4 E3 caller）：抵費地末＝new key〔不在 E〕→排除帳對閘宗和·`pool_final=poolE−area(R_end)`·winner 時 `_new_abate={}`→零行為 | `dc154cd` |
| **[C]** | §3 rebake 註解／raise 訊息（S0d 後 `_acct_geom_tol_per_lot(depth,False)=0.005`·深度項歸零＝`n×0.005`·zero-behavior） | `dc154cd` |
| **W2** | 夾具 ② 由 tautology（`end_abate` 相消·恒真·零力）→**真幾何交叉**（驗0 `_end_region_R` 直測手算＋②帳池==幾何池·可 fail） | `35f60ab` |
| **W3** | condition2 **side-parametrized**（`left`＝`block∩{s<0}`／`right`＝`block∩{s>s(p2)}`·claude.ai 補右式）＋**右向合成夾具** | `e5ff7a9` |

## 二、驗證（真檢·左右雙向 byte-exact）

- **合成夾具**（`verify/fixture_end_fallback.py`·獨立單測·`harvest` defs-only·**無 xlsx/pipeline/錨**）**左右雙向 ALL GREEN**：
  - 驗0：`_end_region_R` 直測 `band=35 ∧ frag=40 ∧ R_end=75`（獨立手算·**可 fail**）。
  - ①：抵費地末（經 `_reshape_block`）＝area(R_end)＝75·含 frag **不雙計**（前提 `poolE=街廓−ΣG−街角` 乾淨）。
  - ②：**帳池 == 幾何池**（`pool_final` == `block−實際 union−街角`·**可 fail**·取代舊 tautology）·Δ=0。
  - ③非疊（抵費地末 ∩ 內移宗＝0）·④G 守恆（內移後 area=G）。
- **reviewer 二審**（`dc154cd`）：**無 BLOCKED**（碼於 UC9898 正確守恆·範圍圍欄乾淨·py_compile 過）；W2 夾具②舊 tautology 由 reviewer 活抓·已改真檢；W3 右式已補·右係乾淨鏡像（不觸 claude.ai 停機/loud-raise 保底）。
- **winner diff=0 by-construction（UC9898）**：
  - E3 caller **逐字零行為**：winner 時 npolys 全在 E → `_new_abate={}` → `pool_final=poolE−0=poolE`·`len(_in_E)=len(npolys)`·下游 `npolys`（734/743）未改。
  - **門檻恆真**：R6 winner `628-4(1)` G=**776.72** ≫ area(R_end)=**252.28**（未臨正街 85.71＋末端帶 166.57·baseline 坐實）·R1 272.84≫115 → **選同 target**。
  - R3：cond1=False（街角·有 SIDELINE）→ 短路·走現街角/§3 路徑。

## 三、未竟（W1·defer·KL 採）＝最終收官之關

- winner diff=0 之 **execution 復現**：F.4 因 **F.0 過期錨**（G007 錨 362.08〔`0c9b7e7`·07-17〕；W脫鉤〔07-19〕＋S0d〔07-20〕改 G 之 W/S 輸入 → 新值 359.43≠錨）**級聯被跳過**（存在性守衛）→ F.4 baseline 對拍**當前不可達**（reviewer 於乾淨 committed-xlsx worktree 實測坐實·**非 xlsx 壞、非本波所致**）。
- **defer 至波末重烤**（KL UI 錨·更新 F.0/F.4 錨後 F.4 跑得到 baseline 對拍）→ 屆時 execution 實證 **§3 淨 diff ＋ §4 winner diff=0**。

## 四、CC 下一動作

§4 **無待辦碼**。次動作＝**波末重烤（KL UI 錨）後·F.4 對 `verify/baselines/wf/f4/` 實證**（§3 淨＋§4 winner diff=0）→ **§4 最終收官**（符 CLAUDE.md：自評/推理不可替代獨立復現·未 push 綠不報收官）。
