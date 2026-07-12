# W-G G.1 收官報告：§7 七級調配引擎接線（app live 注入，零引擎改動）

- 波次：W-G 子波 G.1；日期：2026-07-12；基準 HEAD 前＝`2d2265d`（G.1 偵察上呈）
- 裁定（KL 2026-07-12）：①範圍＝**UC9898 複現**（非本案旗標告知不硬跑；泛化波入 backlog）；
  ②財務 ctx＝**方案 β**（live 幾何/宗地/Step-G ＋ 快照 財務接線_v3）＋**誠實圍欄**（明示凍結值清單＋live-vs-快照差異表、禁靜默混源）。
- 核心鐵律：單一真相源＝`verify/wf_f0~f4`；app 接線＝以 live session ctx 注入呼叫**同一引擎模組**（禁 fork、禁重寫調配邏輯）。

## 一、驗收（全數達標）

| 閘 | 結果 | 錨 |
|---|---|---|
| run_all | **154 `✅ PASS`**，`W-V run_all: ALL GREEN` | 前 153 ＋1＝新 G.1 gate |
| wf/f0~f4 baseline 逐格零 diff | ✅ F.0~F.4 全 baseline 對拍 PASS | 引擎零擾動之機器證明 |
| +1 gate | `✅ PASS W-G G.1 接線層 ctx-builder 同源（cb_by/cad+centerlines/gA/winners/β財務/blocks欄名/指紋）` | run_verification.py |
| app smoke（headless engine-run） | `✅ SMOKE PASS：app _build_wf_ctx → wf_f0→f4 全鏈跑通（0m，無崩）` | verify/wg_g1_smoke.py |
| 引擎/baseline/stepg/selection/harvest/run_all/tests | **一律未觸** | git status |
| app.py diff | **+232／0 刪除**（純加性接線層） | git numstat |

**smoke 日誌（verbatim）**：
```
… _is_uc9898(seed) = True
… _build_wf_ctx OK：cb_by 11 塊、snap.blocks 6 塊、cad.centerlines 4、gA 68 列、β財務源＝快照:True
✅ SMOKE PASS：app `_build_wf_ctx` → wf_f0→f4 全鏈跑通（0m，無崩）
   7-4三級調配 conv=17｜7-5雙出口 exit=10｜池終態 pool=6｜終態整形 reshape=24｜33群總決算 ledger=33
```

## 二、實作（純加性，禁 fork）
1. **純加性 session 曝值**（供 UI 區跨 rerun 組 ctx）：Step H 後 `f3_sb_rows=sb['rows']`、Step G 後 `f3_build_parcels=build_parcels`。
   零 diff 為機械必然——`app_harvest._filter_module` 只 harvest def/import/class，`main()` 被保留但**從不呼叫**（harness 走 stepg，非 app main）。
2. **ctx-builder（module 級，harvestable）**：`_build_wf_ctx(ss, tag)`＋`_wf_ns`／`_WFSessionShim`／`_wf_load_snapshot`／`_wf_tag_of`／`_is_uc9898`。
   - **ns＝app 真符號 13 個**（`{n:globals()[n]}`，**禁 harvest()**——會 re-exec app.py 再入）；引擎經 ns 跑 app 真函式＝禁 fork。
   - cad：7 鍵 `f3_cad_*` → 引擎單一 dict，**含 `centerlines←f3_manual_road_centerlines`**（否則 wf_f3 STRADDLE 崩）。
   - snap：β 混源＝快照 `財務接線_v3`/`global`（凍結）＋ live `blocks`（sb_rows 之 尺度/長度/面積、深度、最小寬）。
   - fake_st：`_WFSessionShim`（淺拷貝隔離 st.session_state；引擎唯一觸及 `.session_state`，另備 no-op `__getattr__`）。
3. **「七級調配」UI 區**（Step G 後）：範圍圍欄（`_is_uc9898` 非本案→warning 不硬跑）＋誠實圍欄（凍結值清單＋live-vs-快照差異表）＋按鈕 live 呼叫 wf_f0→f4 全鏈＋f4 五表（7-4/7-5/池/整形/33群）＋意思決定項照旗標呈現不自動裁。
4. **+1 gate**（run_verification）：seed＝native `_ctx["0m"]` 反投影＋合成 sb 列（測 snap.blocks 欄名、去循環）→ 呼叫 harvested `_build_wf_ctx` → 斷言 cb_by(list→dict)/cad.centerlines/gA/winners/β財務源==快照/blocks 欄名/指紋。全鏈 f0→f4 終態對拍留 **G.3**。
5. **smoke**（verify/wg_g1_smoke.py，獨立、不入 run_all）：複用 harness 建置→重建真 sb（負擔尺度 C-無關，禁改 stepg）→ `_build_wf_ctx`→ wf_f0→f4 全鏈→印終態。證 app 路徑 runtime 無崩。

## 三、plan reviewer 逮之隱患（已修）
- **BLOCKED#1 cad 漏 centerlines**（wf_f3 STRADDLE `LineString(cls[label])` KeyError）→ 修：cad 組裝加 `centerlines←f3_manual_road_centerlines`。smoke 實證 `cad.centerlines=4`、f0→f4 無崩。
- **BLOCKED#2 +1 gate 無法 seed 真 sb**（sb 為 run_step_g 區域變數、未回傳）→ 修：gate 用**合成 sb 列**測欄名映射（去循環）；smoke 另以 snapshot blocks 重建真 sb 跑引擎。
- **WARNING 三**：`_build_wf_ctx(ss,tag)` 定為 ss-as-arg（app 傳 st.session_state、gate 傳 seed）；snap.blocks 路寬改採 `f3_sb_rows`（非 bid-keyed f3_block_road）；sb 欄名精確化（正街尺度/左側尺度/右側尺度、正/左/右面長度(m)、正/左/右面積(㎡)）。

## 四、上呈 claude.ai 收波判讀
1. **+1 gate 界線（透明揭露）**：本 gate 證「ctx-builder 同源」（結構＋值：cb_by/cad+centerlines/gA/winners/β財務/欄名/指紋），
   **不**跑全鏈 f0→f4 終態對拍——後者為 **G.3 雙路同源終驗**（本波不搶）。snap.blocks 用合成列測欄名（避免 reviewer 所指
   「真 sb→快照 負擔尺度」之循環，該循環另由 stepg 條件① 斷言涵蓋）。engine-run 之 runtime 無崩由**獨立 smoke**（非 run_all gate）補證。
2. **smoke 之 sb 重建**：由 snapshot blocks＋cad 複刻（負擔尺度 C-無關、忠實複現 app live sb 之 尺度），**未改 stepg**；此為 smoke-only、不入 baseline/gate。
3. **誠實圍欄之 live 值**：app live 財務值取自 session（pre_land_price_sqm/weighted_price_sqm/b_cost/k_cost/c_cost 等），
   差異表明示與快照凍結值之落差（尤 34949.888 反推總面積 app 無 live 源、利息 NPV 精度較粗、均價成熟度覆寫風險），非阻斷。
4. **G.2/G.3 分工**：逐代圖層／池·碎片·雙出口 GIS 視覺化＝G.2；app live 終態 vs wf/f4 baseline 逐格對拍＝G.3。
