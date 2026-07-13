# W-G app 接線波 收官總報告（G.0 → G.3）

> 目標：§7 七級調配引擎（活於 `verify/wf_f0~f4.py`）接入 app UI，使 **app live 終態 == 已驗證 baseline**。
> 單一真相源＝wf 引擎；app 接線＝live ctx 注入呼叫同一模組，**禁 fork、禁在 app 重寫調配邏輯**。

## 子波總覽

| 子波 | commit | 要旨 | 閘 |
|---|---|---|---|
| G.0 | d57275f | Tab 編號→分頁名 81 文案·步驟K軟化·回報紀律入 CLAUDE.md | 153 |
| G.1 | cd7ad6d | §7 引擎接線（`_build_wf_ctx` live 注入 wf_f0→f4·ns=globals() 禁 harvest 再入·禁 fork）＋KL 兩裁（UC9898 複現·β混源＋誠實圍欄）＋率鋪底 | 154 |
| G.1 補丁+G.2 補 | 79a4a81 | ctx-builder 合約缺口修（率主動鋪底）＋GIS 濾 ghost＋圍欄區段列 | 155 |
| G.2 | 059418d | GIS 終態顯示（純呈現層·世代切換·五表聯動·10/10 PNG）＋引擎純加性補曝第四例 | 155 |
| GIS 點選跳位修 | 024915b | 步驟D 非靶 cn 丟棄＋渲染/判定集同源 | 155 |
| **v3 區段價期日勘誤重烤** | **b288446** | 前價期日勘誤 2024/01/01·全鏈 baseline 重烤·舊凍存 PRE勘誤_期日 | 155 |
| **G.3 雙路同源終驗** | （本收官 commit·`verify/wg_g3.py`） | app live §7 == 重烤後 baseline byte-perfect＋逐格·**W-G 收官** | 155+**G.3 45/45** |

## 一、G.3 雙路同源終驗（收官王牌）

**真同源（非前輪共錯綠）**：v3 勘誤重烤前，app-path 與 baseline 皆用**錯**區段價 → 二路共錯而綠（假同源）；
勘誤後二路皆**正解**價（快照 財務接線_v3 正解·baseline 重烤自同快照）→ 真同源對拍。

**方法**（`verify/wg_g3.py`）：app 接線路徑（harness native 種子 → harvested `_build_wf_ctx` → wf_f0→f4·
雙情境）之全代表，對拍重烤後 baseline（b288446）：**逐格（diff_rows·2dp·key 對齊）＋ byte-perfect
（LF 正規化內容·免 autocrlf 假象）**。app-path 唯一異於 native＝ctx 由 session_state 經 `_build_wf_ctx`
重組（G.1 +1 gate 已證欄同源）；G.3 端到端證**輸出**亦零 diff。

**驗收（`python verify/wg_g3.py` → exit 0）**：
- **G.3 ALL GREEN·45/45 閘**＝(f0:6＋f1:3＋f2:3＋f3:4＋f4:6)＝22 表 × 雙情境(0m/3.5m)＝44 ＋ 圍欄段價 1。
- **雙路 byte-perfect ✅**：app-path 每代表序列化（LF 正規化）逐 byte == 重烤 baseline（非僅逐格·更強）。
- **全代 baseline 零 diff ✅**：f0~f4 × 雙情境 × 各表 逐格（diff_rows·key 對齊）＋byte 雙證全綠。
- **155 + G.3 閘全綠**：run_all 155（b288446 重烤後·additive 新增 wg_g3 不觸）＋G.3 45/45。
- **圍欄區段列**：快照段價＝正解（a=43909.2308486259·b=37322.846221332016）·A 逐宗吃之（headless proxy 綠）；
  live 視覺圍欄（pre_zone_results vs 快照）localhost KL 驗（材質 1.087% 漂移已消滅）。

**同源真偽之機器證明**：G.3 唯一異於 run_all native 路徑＝ctx 由 app `_build_wf_ctx`（harvested·由 session_state
忠實重組）而非 native `_ctx` 直建。byte-perfect 成立 ⟹ 二 ctx 對 wf 引擎**輸出等價**（非僅 G.1 +1 gate 之
欄同源·而係端到端輸出同一）。sb_rows 經查 wf/stepg 皆內部自 road_data(cad+snapshot) 現算、不吃 ctx 值 →
接線層 ctx 差異對引擎輸出零影響·佐證「接線純加性、引擎唯一真相源」。

## 二、W-G 鐵律沉澱（入 CLAUDE.md §7 引擎接線鐵律）

- 單一真相源＝`verify/wf_f0~f4`；app 接線＝live ctx 注入呼叫同一引擎模組·禁 fork·禁重寫調配。
- ns=`globals()` 取 13 真符號·**非 harvest()**（app 內 harvest 會 exec(app.py) 再入）。
- 引擎 UC9898-凍結（67 raise＋硬寫錨）·接線區 `_is_uc9898` 圍欄·非本案不硬跑·通用化列泛化波 backlog。
- 財務 ctx＝β 混源（live 幾何/宗地/Step-G ＋ 快照財務）＋誠實圍欄（凍結值清單＋live-vs-快照差異·禁靜默混源）。
- 接線層純加性（session 曝值/新函式不動既有碼路徑）；harvest 保留 main() 但從不呼叫 → tab body 新碼零 baseline diff。

## 三、待 KL 裁（承 v3 勘誤重烤·報告 W-G_v3勘誤重烤.md §七）

1. **E2 7-5 最優指派翻**（0m G004→R4·G012→R1；3.5m G015↔G031·G012→R1）＝校正價真最優·超「金額」字面·追認？
2. **CLAUDE.md 親鎖定錨 G015「1.89㎡/142792元」→「2.45㎡/185100元」**（HOLD 待首肯改憲）。
3. **F.1 容差 0.05→0.10＋圍欄段價 1e-6 sub-cent**（二判斷項）。

## 四、次步

**W-G 收官** → claude.ai 驗畢 → 遞**泛化波偵察交辦**（引擎去 UC9898 硬錨·通用化；見 §二 backlog）。
