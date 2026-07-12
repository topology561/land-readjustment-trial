# W-F F.5 汰換收官波（PROVENANCE）— 舊機制廢除＋汰換對照表（零行為變更）

> 本檔＝W-F 收官（F.5）之汰換紀錄。**零行為變更**＝對 F.4 harness 終態（wf/f4 六表×2）逐格零 diff。
> app.py commit（刪碼前）＝`b2166b7`；刪碼後 commit 待填。reviewer 獨立驗證邊界（py_compile＋harvest＋grep）。

## 一、刪除清單（app.py，864 行，reviewer 驗證邊界）

| 標的 | 刪除行範圍（刪碼前 1-indexed）| 性質 |
|---|---|---|
| `_inflate_a_for_orphan`＋`_polylabel_inscribed_diameter`＋`_geometric_carve_from_side`＋`_TIER1_APRIME_INJECT_ENABLED`＋`_allocate_three_tier_v1`＋`_allocate_tier2_tier3_geometric` | **6534–7028** | 函式群＋gate 常數（含 2 孤兒 helper：polylabel 零呼叫、carve 僅三廢②內用） |
| `calc_a_prime` | **7337–7364** | 函式 |
| Tier1 UI 呼叫塊（try/except 全段） | **12081–12178** | 含 `temp_parcels=_alloc_result['updated_parcels']`（gate-False 下僅濾 ghost） |
| Tier2/3 UI 呼叫塊（try/except 全段） | **15619–15687** | — |
| Patch D-6 三層調配明細 expander | **15707–15740** | 死碼（3 writer 已刪→guard 恆 False） |
| 步驟 K UI 塊（`if f3_J_cross_block_needed:` 自足） | **16486–16625** | 含 `calc_a_prime` 呼叫端 16584 |

**保留（reviewer 裁定 graceful）**：W-C 白縫診斷（16017 `_t3log=.get('f3_tier3_log',[])`）＝多用途唯讀診斷，
非 Tier3 專屬，`.get` graceful default→空、零風險；外科式切 Tier3 段風險高（易留 dangling），故留。

**harness 零影響（結構保證）**：app_harvest 為 AST harvest（只 exec top-level def/const、跳過 UI 語句
`If/With/Try`）；全部呼叫端在 tab UI→harvest 本就不執行。靜態閘（run_verification 819-948）檢 `wf_*.py`
原始碼字串、非 app.py。舊機制 session_state 鍵消費者全 `.get(k,default)` graceful（無 NameError 下標）。
刪碼後：harvest kept 147→140（少 6 def＋1 const）、golden 0.6685/0.3315 不變、run_all 對 wf/f4 逐格零 diff。

## 二、汰換對照表（舊機制節點 → 新 §7 節點）

| 舊機制節點（app.py，已刪） | 新 §7 節點（verify/，沿用；規格 §7） |
|---|---|
| `_allocate_three_tier_v1` Tier1 同Ri同歸戶 a 注入（gate 關已 dormant） | **§7-1 級0/0'（wf_f0）＋級1-3（wf_f2）**；a′ 模式一 `run_step_g` 重解（a 基、非 G 直加，§142） |
| `_allocate_tier2_tier3_geometric` Tier2/3 幾何切割 | **§7-4 無同歸戶 3 級調配（wf_f4 E1）＋§7-5 增配雙出口（wf_f4 E2 批次最佳化）** |
| `calc_a_prime`（`a×p_o/p_t`，呼叫端餵 G 違 §142、docstring 模式混淆） | **§7-4 a′ 雙模式**：模式一（wf_f2，有同歸戶目標地）／模式二（wf_f4，p_avg 幾何權重）；a 基 `run_step_g` 重解 |
| `_inflate_a_for_orphan`（孤立公設地虛胖 a） | **§7-2/7-3 公設地 a′ 併入同歸戶建地（wf_f3）／§7-4 調配（wf_f4）** |
| 步驟 K UI（跨街廓 a′ 換算、Tab 8 讀） | **§7-4 距離法＋模式二（wf_f4 E1）**，KL 質心起迄法 |
| **E-0.4 ghost 排除**（`_allocate_three_tier_v1` app.py 6748 `[tp for tp if not _is_ghost_sliver]`）| **ghost 零面積不變量閘（run_verification 355-365，沿用）**——ghost 幾何面積=0 不入 G/守恆，新 §7 引擎不排除、靠零面積成立（[H-ghost] 定讞，PROVENANCE_v2） |
| `_TIER1_APRIME_INJECT_ENABLED` gate（Patch D-3 舊機制節點） | 無（新 §7 直接實作、無 gate；F.3 已廢棄非翻 True） |

## 三、真實 app 行為變更（harness 無法驗；上呈 KL 以真跑 app 確認）

1. **ghost 排除新落點**：舊 UI 12120 `temp_parcels=updated_parcels` 使下游取濾 ghost 後 parcels；刪後
   下游保留 ghost sliver。**無害**（ghost 零面積、不入 G/守恆）；刪後**真 app 與 harness 一致**（皆靠零面積）。
   reviewer §5 實證：gate-False 下 `_allocate_three_tier_v1` 對 parcels **僅濾 ghost、無任何 a 值修改**
   （a 注入段 6823-6831 包在 `if _TIER1_APRIME_INJECT_ENABLED:` 內、恆跳過）。
2. **Tab 3 失去 Tier1/2/3＋步驟 K UI＋現金補償列**（`f3_cash_compensation_list` writer 已刪→readers 得 []）。
   新 §7 引擎僅在 verify/（harness），**未接 app.py UI**——真 app 之「跨街廓調配／三層調配」UI 步驟消失，
   待未來波接 §7 引擎入 app.py（本波不做）。
3. **殘留 cosmetic（reviewer NOTE，上呈 KL）**：步驟 J 提示（app 內 `st.info("...請執行步驟 K")`）指向已刪步驟；
   純顯示、在 KL 刪 K 範圍內，KL 確認是否軟化。

## 四、baseline v4（規格 F.5.2）＋規格內部矛盾（上呈 KL）

- **v4 語意**：wf/f4 trunk E 終態六表×2＝W-F 終態全表；F.5 刪碼後 run_all 對其**逐格零 diff**＝零行為變更之
  機器證明（v4 錨）。**本波未另立 `v4/` 目錄**（避免與 wf/f4 重複）；PROVENANCE 記「零 diff 閘＝v4 語意」。
- **規格版號矛盾（reviewer §7 發現）**：規格 `docs/W-F_細部規格.md:213`「baseline 升 **v4**」vs
  `PROVENANCE_F4.md:119` F.5 預告「升 **v5**」。v2→v3→v4 才連號，v5 疑誤記。**上呈 KL 釐清版號＋
  是否要獨立 baseline 目錄快照**（文件/架構層，非 CC 定）。

## 五、五代凍存

v3／wf/f0／f1／f2／f3／f4 baseline byte 不動（git diff 空證）。F.5 additive-刪除（只刪 app.py 死/舊碼，
harness 零觸）。CLAUDE.md 已鎖入裁示1(a) governs＋Q3 修正式（F.4 收官）。

## 六、W-G G.2 補曝附記（KL 裁定 2026-07-12）

G.2 補曝＝**純加性曝值第四例**（承 sgB_rows／sgD_rows／f0_parcels 先例）：wf_f2 `sgC_rows`、
wf_f4 `sgE_rows`＋`reshape_polys`、wf_f1 `reshape_polys`＋`wedge_coords`（皆深拷貝/tuple 凍結、
該代計算完成後曝、baseline CSV 不吃 out 鍵）——**run_all 全代零 diff 為證**；「只寫不讀」靜態圍欄
入 run_verification G.2 閘（每檔恰 1 寫點、他檔零越界）。供 app G.2 純呈現層（禁重算）消費。
