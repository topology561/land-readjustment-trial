# W-G.4 S1 plan **v3**：reviewer **PASS**（無 BLOCKED·無假綠）＋六施工 WARNING＋一 stale 已修

- 日期：2026-07-18；plan v3＝`docs/specs/W-G.4_S1_plan.md`（`c38f118`）；**未動工**
- reviewer＝redistribution-reviewer·獨立·**真 harness／自寫探針復現**·不採信 plan／CC 任一數字
- **總判：PASS（作為 plan）**——v1/v2 各 BLOCKED×5·v3 首次過
- **一句話**：**BLOCKED×5 逐條碼面/算術真解·所有事實錨（行號／78.24／δ／2298.80／守恆）reviewer 全數獨立復現屬實·py_compile 過·未違鎖定鐵則·無假綠**。剩餘皆施工待驗 WARNING（plan 已誠實標旗）。**唯歸因閘非套套邏輯屬施工待證之最高風險·須下輪 reviewer 獨立復現·不得自評綠替代。**

---

## 1. 逐項 CONFIRMED（reviewer 實跑證據·摘）

| # | 審點 | 判 | reviewer 證據 |
|---|---|---|---|
| 1 | **行號全驗**（v2 死於 6821 stale） | ✅ CONFIRMED | `app:7147/7148/7209/7239-7240/7252/7267/7652/15291/15298/15475`＋`stepg:421/428/451/533/545/551/573/576/636/642/770/801-812`＋`wf_f1:216`＋`wf_f4:1121/1128/1124-1126`（BLOCKED-4 第三處實在）全 `awk` 逐一坐實。**一非承重 stale**：`app:5127`（docstring）→真碼 **5134**（同函式·no-change ref·**已修**） |
| 2 | **δ 發現真偽** | ✅ CONFIRMED | reviewer 重寫 `rev_probe.py`（複用 `build_pipeline` 真 ctx）逐位復現報告：`δ_true` 六塊 R6+3.4749/R1+2.8728/R3−1.7506/R2+1.6939/R5+1.6403/R4+0.8115（|Δ|≤0.006）；`δ_literal` R6=**+0.0000**（鑑別案·SIDE_R6∥ALLOC）。「literal 不對上·真式已驗」屬實非自欺 |
| 3 | **歸因閘非套套邏輯** | ⚠️ WARNING（非 BLOCKED） | plan 未宣稱「已綠」·而**新設待建閘＋明列反模式**（禁重跑引擎 Rw）＋路由 reviewer＝**正確姿態**（v1閘②/v2閘③'是宣稱通過之恆綠閘·v3 反增自查段）。惟機制僅到概念層·**施工必守：預測 ΔRw 由幾何直量獨立·禁讀引擎 `rw_increment`** |
| 4 | **閘③' 78.24 鑑別力** | ✅ CONFIRMED | `rev_probe.py` 實算現行倉態 R3 p2 楔形(s≥amp)=**78.2363**·R1/R6 p2=0；s_min/s_max/amp 逐位對 v2。副證 R1 p1 楔形 5.3255／R6 85.7064 對 F.4 CSV。病灶在時=78.24·修後→0＝有鑑別力 |
| 5 | **#25 side 參數化** | ✅ CONFIRMED | side 真參數化 #25 漏維度（left `[max(s_min,0),buf]`／right `[amp−buf,s_max]` 逐側不同 s 區間）·非掛名；閘③ 錨逐項避 #25 五陷阱·明文承認「R2左 8.7157 對 side 零舉證力」。副證 `wf_f1` 確無 right 鷹架（grep=0） |
| 6 | **BLOCKED×5 真解** | ✅ CONFIRMED | B-1：`actual_max_proj`(15475) 定義於左組迴圈(15403→15462)後、`if`(15467)內·消費僅右組(15512/15513)→step0 物理不觸左組·R1/R6 p1 楔形歸 N0-20 碼面坐實。B-2~B-5 全處置成立 |
| 7 | **查表化窮盡性** | ✅ CONFIRMED | `f3L_sb_rows_by_label` 全庫**無寫入**(唯 7636 讀)→`app:7652` 3.5 fallback 確在效；`get_min_lot_size` 回 key=`min_width`(7276/7286/7294)；reviewer 自 grep 全庫 `3.5`·**無漏掃 live 消費點** |
| 8 | **ΔΣ池 2298.80** | ✅ CONFIRMED | `F.4_G值_退縮3.5m.csv` Σ抵費地=**2298.80**(11 列)／0m=**2378.01**(9 列)·推翻 2299.26 |
| 9 | **守恆＋波鎖** | ✅ CONFIRMED | F.4 baseline 逐街廓 Σ幾何=DXF 面積·worst|Δ|=0.02㎡<1；未違四欄唯讀／守恆式／同名不同量／位相不變／裁示1(a)；§6 是廢靜默 fallback（改 loud）非新增 |

**gate② 錨鑑別力副證**（reviewer 加驗）：forced band pool 212.84/233.79/389.85 皆與 range 300.52/309.05/308.93 差 >1㎡ → 現在就紅 → 有鑑別力·非套套邏輯。

## 2. 六施工 WARNING（施工／下輪 reviewer 必獨立復現·非 BLOCKED）

1. **🔴 歸因閘非套套邏輯（最高）**：施工須證預測 ΔRw 由幾何直量獨立得出·非讀引擎 Rw；下輪 reviewer 逐宗實跑對拍（v1/v2 正死於此型）。
2. **buffer_S′ 右側錨**：重烤後 `_pool_strips_for_block` 真實產物實測·**禁硬釘 5.2719/8.7290**；`wf_f1` 補 right 全鷹架（非只加變數）。
3. **W 脫鉤落點**：施工用**直量 mp→遠側**（intrinsic）·勿賭 `−δ_block` literal 式（R6 literal=0 會錯）；plan §1/§10 已傾向直量·守住即可。
4. **帳對幾何 tol 收緊（S0d）**：`n×0.005`(E3) 須驗殘差不因 `W_far=round(W_conv,2)` 量化翻紅（W-4·重烤實測）。
5. **N0-20 標記制→通式**：R3/R6 由零幾何動作改通式·**動 W-D.4 遞補錨**（#24 CC 錯#1 同型）·須跑 W-D.4 遞補錨回歸閘證不越權。
6. **app:5127 stale → 5134**：**已修**（本 commit）。

## 3. 域外·上呈 KL（reviewer 明言非其值域·plan §10 已路由）

δ 精確式參照點（p2→群起點）／R4 單街角宗 ΣRw<100% 之 N0-20 吸收／N0-20「未臨正街土地」幾何源／退縮查表與 UC9898 耦合（`app:8524`＋`run_verification:838`）／`verify:108` 單一 global 法定最小寬是否逐塊查表。

## 4. CC 處置與次步

- **app:5127→5134 stale 已修**（plan §1.3·本 commit）；其餘 WARNING 皆施工待驗·非 plan 級缺陷·不動 plan 主體。
- **plan v3 未動工**——波紀律＝reviewer PASS → **claude.ai 獨立複驗** → **KL 確認才動工**（生產碼零觸）。
- 施工時 six WARNING 逐一守·**歸因閘施工產物必回送下輪 reviewer 獨立復現**（自評綠不可替代）。
- 上呈 KL 域裁 4 題（§3）並行。
