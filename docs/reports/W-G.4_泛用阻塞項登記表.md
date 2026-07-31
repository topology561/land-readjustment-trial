# W-G.4 — **已掛名之泛用阻塞項 登記表**

> 立於 KL 交辦（2026-07-25·丁）。**與普通 backlog 分離**：本表所列係
> **「本案（UC9898）不觸發、但換一個案子會硬停或算錯」之已知結構性阻塞**，
> 每項須有**倉內出處**與**觸發條件**；解除多半需**泛化波**，部分尚須 **KL 域裁**。
>
> 判準（入表 vs 入 backlog）：
> - **入本表**＝換案即**硬停／錯值**（非「可以再優化」）。
> - **入 backlog**＝品質改善、容差調校、報告措辭等。
>
> ⚠️ 本表**不得**寫成「已驗過」——凡未被真資料走過之分支，一律於「真資料覆蓋」欄標明。

---

## 一、登記

| # | 阻塞項 | 觸發條件（換案） | 現況處置 | 倉內出處 | 真資料覆蓋 | 需 KL 域裁？ |
|---|---|---|---|---|---|---|
| **GB-1** 🆕 | **E3「往後找」分支必觸楔形相鄰守衛** ——末端 gate 開時以「G ≥ area(R_end)」往後找標的，但 `_reshape_block` 要求標的與楔形相鄰；跨過被跳過之宗後距離必 ≥0.05 ⇒ raise「楔形與標的不相鄰」 | 末端 gate 開（無 SIDELINE ∧ 未臨正街半平面>ε）**∧** 首個合格宗 `G < area(R_end)` | **硬停**（loud raise） | 實測：`verify/fixture_end_winner.py` 驗2 之 A 欄（`M_0725_F2_end_winner.log`）——**左右兩側皆然**；碼：`grep -n "楔形與標的" verify/wf_f4.py`／`grep -n "往後找" verify/wf_f4.py` | ❌ 本案未觸及（F-5 證 fallback latent、R1/R6 皆有 winner 且 G≫area(R_end)） | ✅ **可能需**——「往後找之標的**是否必須**與楔形相鄰」係分配原則問題（位相不變 vs 末端保留孰先），非純技術。**本批未問** |
| **GB-2** | **M-5 階段② 未實作**（餘額他併至 MinA） | ①補足後源仍有餘 **∧** 同 gid 尚有其他「較大但未達 MinA」之宗 | **loud 停機**（禁靜默轉③） | `grep -n "②" verify/m_rescue.py`；`W-G.4_裁定M_CC交接文.md` §六 | ❌ 本案母體為空 | — |
| **GB-3** | **`wf_f1` 右支架未建**（該檔硬釘 `lbl="R1"`＋結構左向） | R1 右側成為 forced 端 | **loud raise**（碼內留 KL 裁語 TODO） | `W-G.4_S1_band_N0-20_recon＋side參數化approach.md` §18① | ❌ R1 兩情境皆非 forced | — |
| **GB-4** | **全倉無「部分面積拆分併入」機制**（裁定A 之拆分僅列 plan、未實作） | 需以**部分面積**併入（`wf_f0._transform` 為整筆、`wf_f2` 為全搬單一 `tgt_blk`） | **缺口**（無守衛） | `W-G.4_裁定M_盤點表.md` §「部分拆分」列 | ❌ | 待泛化波盤 |
| **GB-5** | **引擎 UC9898 硬錨**（`GSA_EXPECT`／`E0_EXPECT`／`E2_NAMED`／`COMP_EXPECT`／`F1_TARGET`／`F1_REVERIFY` 等＋67 raise 斷言） | 任何非 UC9898 案 | `_is_uc9898` 圍欄·非本案不硬跑 | `CLAUDE.md` §7 引擎接線鐵律；`W-G_收官總報告.md` §二 | — | — |
| **GB-6** | **`wf_f0.ROUTE_OUT` 決策常數未刪**（驅動控制流·且 E-1 導出式吃其產出 ⇒ 循環相依） | 換案（去錨） | 本波不刪·`F2_GROUPS` 已改導出式 | `docs/specs/W-G.4_裁定M_plan_v4.md` §六 E-2／§九 | — | — |
| **GB-7** 🆕 | **per-block MinA 之 round 位置與正典不符**——**三份實作**（`wf_f0._mina_by_block`／`wd4_tier_list._mina_by_block`／**`app.py` 之 `_min_alloc_area_by_blk`**·見 GB-8）皆實作 `round(D×w, 2)`（先乘後捨），而正典 **K-8 §二-1** 明訂 `round(D,2)×w` 且「**`round()` 只在輸出層**」⇒ **輸出層以外多捨一次** | 任何使 `min(MinA_i)` **落在乘積非 2dp 之街廓**的案子（＝`round(D,2)` 之第二位小數為奇數 × `min_width=3.5` 時必生第三位）。本案 min 落在 **R4**（`33.10×3.5=115.85` 恰 2dp）故兩形同值 | **不改**（本波只登記）。今日 0.005㎡ 之差落在下游 `−0.01`／`−0.5` 容差內、**零翻盤** | 實測（w=3.5·現行注入深度）：R1 `116.025`/`116.02`、R2 `155.645`/`155.64`、R5 `159.985`/`159.99`、R6 `159.285`/`159.28` **四塊真分歧各 0.005㎡**；R3/R4 等值。碼：`grep -rn "_mina_by_block" --include="*.py" .`；正典：`grep -n "K-8 §二-1" docs/rulings/K-6_街角地分配程序與可分配判準.md` | ⚠️ **本案零後果係「min 恰落在 R4」之巧合**、非結構保證 ⇒ 視同**未被真資料走過** | ❌ 不需——正典已明訂（K-8 §二-1），屬**碼面未依裁定**之技術修正。**K-6-A2 拆除 per-block MinA 達標角色時一併收** |
| **GB-7b** 🆕 | **GB-7 之第二觸發條件：生產側之「等值前提」根本不成立**——GB-7 今日零後果之前提為「深度已 2dp 且乘積恰 2dp」，但**生產側深度可非 2dp**：逐街廓覆寫格 `f3L_depth_ov_*`（`grep -n "深度覆寫（m）" app.py`）為 `st.number_input`，**未限小數位、未 `format=`、取值後亦未 `round`**（`grep -n "_depth_use_by_blk\[_lbl\] = float(_ov)" app.py`）⇒ KL 手填任意小數即繞過 2dp 鏈 | **KL 於畫面填入非 2dp 覆寫值**。實例：填 `33.157` ⇒ 正典形 `round(33.157,2)×3.5 = 116.06`、碼面形 `round(33.157×3.5,2) = 116.05`，**Δ = −0.01**（恰在下游 `mina[blk] − 0.01` 容差邊緣）。🔴 **更劣者已實測可【超出】容差**：填 `44.473` ⇒ `155.645` vs `155.66`，**Δ = +0.015 > 0.01** | **只登記·不動 widget、不動算式**（動之即非零行為，屬**波末批**） | widget：`grep -n "深度覆寫（m）" app.py`；取值：`grep -n "float(_ov) if _ov > 0" app.py`；容差錨：`grep -n "mina\[blk\] - 0.01" verify/wf_f4.py`（5 命中） | ❌ **未被真資料走過**（今日六街廓皆用自動量測值·`_dinfo['D_avg']` 已 2dp） | ❌ 不需——正典已明訂 round 位置（K-8 §二-1） |
| **GB-8** 🆕 | **per-block MinA 有【三份】實作、無一致性看守**——① `wf_f0._mina_by_block`（3 參數→`dict`·**引擎土地後果路徑**：`wf_f0`/`wf_f2`/`wf_f3`/`wf_f4` 與 harness 皆用之）② `wd4_tier_list._mina_by_block`（4 參數→`(dict, min)`·**清單／回歸路徑**）③ **`app.py` 之 `_min_alloc_area_by_blk`**（`grep -n "_min_alloc_area_by_blk\[" app.py`·**生產 UI 路徑**·寫入 `f3_min_alloc_area_by_label`）。三者皆 `round(D×w, 2)` 先乘後捨，**全倉無任何閘比對之** | 任一份被改（去錨／K-6-A2 拆除達標角色／換 round 位置）而其餘未同步 ⇒ **靜默分歧**。🔴 **第三份在生產 UI 側**——與引擎側分歧時**不只影響清單與回歸斷言，是 KL 螢幕上看到的數字**（`f3_min_alloc_area_by_label` 供畫面顯示與下游消費） | **不改**（本波只登記）。三份簽章／宿主皆不同**不可互代**，非「刪兩份」即可了事 | ①②`grep -rn "_mina_by_block" --include="*.py" .`；③`grep -n "_min_alloc_area_by_blk\[" app.py`＋`grep -rn "f3_min_alloc_area_by_label" --include="*.py" .`；一致性看守之不存在：前者 grep 加 `\| grep -i "assert\|==\|一致\|同源"` ⇒ **僅命中註解、無斷言** | ❌ **從未被看守**（今日相同係三者碼面巧合一致，非機器保證） | ❌ 不需——屬 #20「避第三份抄寫」之未竟部分（**第三份即在 app**）。**K-6-A2 拆除 per-block MinA 達標角色時一併收** |
| **GB-9** 🆕 | **`f3_pk_legal_min_width` 之「單一真相源·app==engine」宣稱逾實證**——註解見 `grep -n "單一真相源·app==engine" app.py`。**前半屬實**（兩路皆走 `get_min_lot_size` 查表、已廢 v12 內硬編 3.5）；**後半逾實證**：兩寫入點之**輸入取自不同來源**——engine `verify/selection_pipeline.py` 之 `正面路寬(m)` 溯源至**快照** `blocks[*].正面.路寬_m`（`grep -n 'fw = float(blk\["正面"\]' verify/run_verification.py`），app 溯源至 **live `sb['rows']`**（`grep -n "_sb_row = sb_rows_by_label.get" app.py` → `grep -n "sb_rows_by_label = " app.py`）；且**全倉無閘比對二者** | 兩來源脫鉤（改快照而未重跑 Step-F／app 側臨街負擔表算法變動／換案時二者不同步）⇒ `min_width` 分歧 ⇒ **PK 前置篩選與街角規定範圍門檻同時偏移** | **不改**（本波只登記）；註解已同批降級為「兩路同式、**惟輸入來源不同且無看守**」 | 註解：`grep -n "單一真相源·app==engine" app.py`；寫入點：`grep -n "f3_pk_legal_min_width'\] = " app.py verify/selection_pipeline.py` | ❌ **從未被看守**（今日相符係二來源同案） | ❌ 不需——與 GB-8 同形態（無看守之等值宣稱）。**K-6-A2／G.3 雙路同源批一併收** |

> **關於 KL 所引之「E-3 批次迭代未實作」**：交辦文以之為同級參照，惟**倉內以該名稱查無條目**
> （`rg -n '批次迭代|E-3.*未實作' .` ⇒ **扣除本檔自身後 0 命中**·於 `e45bbb2` 工作樹實跑）。
> 最接近之既有條目為 **GB-2／GB-4**。
> **不臆測、不代填**——出處待補；若係他處用語，請指出對應條目後併入。

---

## 二、真資料覆蓋之誠實登記（**禁寫成「已驗過」**）

| 機制 | 紅向（會不會咬） | 正向（真資料是否走過） |
|---|---|---|
| **F-10-3**（M-5 三列可證偽） | ✅ 由 `WV_BITE=1` 注入偽 forced 端證其會紅（`M_0725_F10_bite.log`·3 列全紅） | ❌ **從未被真資料走過**——0m 無 forced 端（＝**空真綠**）、3.5m 走 award 分支。正向僅由 claude.ai grep `m_rescue` 之「維持強制抵費地」log 格式**坐實格式相符**，**非**實跑覆蓋 |
| **F-10-1 (A′)** | ✅ 由 `WV_BITE=1` 注入 `_BITE_A0ONLY_` 證其會紅 | ❌ 本案無「原 a==0 且自 parcels₁ 消失」之宗 |
| **§4 無勝者 fallback** | ✅ `fixture_end_fallback.py` 左右各 5 項 | ❌ latent（69 個 bake 檔全掃「抵費地末」命中 0） |
| **末端保留窗** | ✅ `fixture_end_reserve.py` 12/12 | ✅ R6 左·21/21 觸發（惟係 **BAKE 致能之條件式讀數**·待 P-H 後非 BAKE 重現） |

---

## 三、維護

- 新增阻塞項時：**先給倉內出處與觸發條件**，再入表；無出處者不得入表。
- 解除時：於該列註記解除 commit，**不刪列**（保留歷史）。
- 本表由各波報告引用，**不重述數字**——數字一律引 log 檔名。
