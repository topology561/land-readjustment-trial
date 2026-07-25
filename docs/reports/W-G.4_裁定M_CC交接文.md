# W-G.4 裁定 M — **新 CC session 交接文**

> 交接時點：`origin/wip/s1-endpart` == `HEAD` == **`5e04b38`**（已 push·local==origin）。
> 分支 `wip/s1-endpart`。**本波尚未收官**（P-F/P-G/P-H 未做）。
> ⚠️ **未 push 不得報收官**（CLAUDE.md 最高紀律）；**收官前置＝`git rev-parse origin/wip/s1-endpart` 已含該 commit**。

---

## 〇、一分鐘定位：現在在哪

裁定 M 波之施工序：`P-0a → P-0b → P-0c → P-A → P-B → P-C → P-D/E → **P-F → P-G → P-H**`
**已完成到 P-D/E ＋ F-1~F-9c 修補批次；下一步＝P-F。**

**M-5 機制已落地且首要目標達成**：`W-F F.4`（3.5m E2「7 < 9」不可行）**已解**、`W-G G.2` 連帶轉綠。

---

## 一、必讀（依序·勿跳）

| # | 檔 | 為何 |
|---|---|---|
| 1 | `CLAUDE.md` | 專案總則·回報鐵律·守恆鐵律·泛用四約束 |
| 2 | `docs/specs/W-G.4_KL域裁M_原位次小往大_街角winner更正.md` **§七（裁定 M-5）** | canonical。§7.1 KL 原文／§7.2 技術詮釋／**§7.3 驗收預測閘 a~d**／§7.4 歸因分列 |
| 3 | `docs/specs/W-G.4_裁定M_plan_v4.md` | 現行施工 plan（P-F/P-G/P-H 條文在此） |
| 4 | `docs/reports/W-G.4_裁定M_重錨登記.md` | **R-1~R-9 ＋ BK-1~BK-4**。P-H 之強制輸入 |
| 5 | `docs/reports/W-G.4_裁定M_F1-F5_完成報告.md` | F-1~F-9c 全紀錄（§十一 F-7／**§十二 F-8/F-9**） |
| 6 | `docs/reports/W-G.4_裁定M_P0c_S1重烤_歸因表.md` | P-0c 之 **S1** 歸因（**禁與 M-5 混算**） |
| 7 | `.claude/skills/failure-archaeology/SKILL.md` | 尤其 #20 #25 #26 #27 |

---

## 二、當前讀數（**兩份·效力不同級**）

| 模式 | 讀數 | log | **效力** |
|---|---|---|---|
| **非 BAKE**（權威） | **56 PASS ／ 14 FAIL** | `verify/out/M_F9_nobake.log` | 真比對 |
| **WV_BAKE**（側錄） | **160 PASS ／ 1 FAIL** | `verify/out/M_F9_bake.log` | 🔴 **不可當品質證據** |

**🔴 BAKE 讀數之陷阱（務必內化）**：`run_verification.py:279-284` 於 `WV_BAKE` 下
`_bake_csv(...); return True, []` ＝ **不比對即回綠**（該次烤 69 檔）；且 `wf_f0` 之 GSA 硬閘降為 `print`。
**reviewer 實測：那 69 列結構性綠中，有 30 列若真比對會紅。**

**非 BAKE 之 14 FAIL 組成**：3.5m baseline 7 列（R-7）＋ `k*3.5m` ＋ `W-F F.0~F.4` 五列 raise 級聯 ＋ `W-G G.2`。
**「0m 零紅」須加限定**：0m tag 之閘零紅，但 **F.4 之 0m 六閘因上游 F.0 raise 未被執行**（非通過）。

---

## 三、下一步：P-F → P-G → P-H

### P-F（M-4 交互驗證·**實測非 prose**）
plan v4 §七。六項 F-1~F-6，BEFORE 錨：
- `fixture_end_reserve.py` **12 檢核項**（左6+右6）／`fixture_end_fallback.py` **左右各 5 項**
- 3.5m 末端保留**唯 R6 左端**·未臨正街 **85.706㎡**·末端帶 `s∈[-0.0000, 3.5114]`
  （`docs/reports/W-G.4_§4_P2_兩階段落位_f到g.md:102`）
- 🔴 **本行原載行號錨已作廢**（原寫 `_cond1`＝`wf_f4.py:1325`／`_end_gate`＝`:1338`·「勿信 1467/1480」）。
  `ebe24fe` 實 grep：`_cond1`＝**1338**／`_end_gate`＝**1351**／末端 winner＝**1363**，`1467/1480` **皆存在**（檔 1588 行）。
  一律改引符號名：`grep -n "_cond1 = not bool" verify/wf_f4.py`／`grep -n "_end_gate = _cond1" verify/wf_f4.py`
- ⚠️ reviewer 指出：`_cond1` 斷言 **by construction 近恆真**、鑑別力≈0 ⇒ **應改對
  `_end_gate` 之 `_unfront_area` ＋ `wf_f4:1350` 之末端 winner 前後集合**斷言

### P-G（容量拆解重跑）
`WV_CAPDECOMP=1 python verify/probes/probe_capacity_decomp.py`
BEFORE：3.5m 需求群 **9**／甲現況上界 **7**（短 2）／乙釋三端 12／丙釋碎片 7。
⚠️ log 自述 `窮舉=space 559872>300000·未窮舉` ⇒ **上界達標 ≠ 可行**；須另以建構指派或真窮舉證。
**措辭鐵律**：「forced 街角解鎖 → **面積回歸中央調配池** → 可及容量上升」；**禁「釋回／減少抵費地」**。

### P-H（重烤·**最大件**）
1. **必須逐列消化 `重錨登記.md` R-1~R-9**（缺一即紅·閘見該檔 §三）。
2. **歸因分列**：M-5（本波）vs S1（P-0c）**嚴禁混算**。
3. **目標名目數**：F-7 後 WV_BAKE 為 **161 行／161 唯一**（P-0c 為 132 行／131 唯一）。
   拆解：改名 4 對／真消失 1（`W-F F.4` 解鎖為 24 個 F.4 細名）／真新增 3（M-5 三閘）／＋3（0m 三閘）。
4. 烤源＝**committed xlsx**（blob `80f75ee`·`git worktree` 乾淨樹）；**禁改 `skip_cols`／`_exp_gd`**。
5. **禁**把 P-0c 與 P-H 併為一次重烤（隔離鐵律）。

---

## 四、🚩 待裁（CC 不拍板）

| # | 題 | 出處 |
|---|---|---|
| **BK-4** | `wf/f4` 12 檔（含 **0m 六閘**）之**波次歸屬**——S1 遺留（F.4 當年 E2 死掉沒烤到）vs M-5 使 F.4 復活才曝出。**兩表皆無登記**係客觀事實 | 登記表 R-9／§四 |
| — | `W-F F.4` 3.5m E2「上界 7 < 需求 9」殘紅是否為預期中間態 | 沿用未裁 |
| — | `F2_GROUPS` 為何排除 G006／G007（規則本意） | plan v4 §十一 |
| — | `data/地籍資料來源_匿名版.xlsx` **modified-not-committed**（reviewer 逐 sheet 證內容逐格全等·僅容器重存 ⇒ cosmetic）——commit 或 revert？ | N-5 |

---

## 五、🔴 本波最重要的教訓（**新 session 請先讀這段**）

### 5.1 「宣稱已修而未觀測輸出」——**同型犯三次**
| # | 事件 |
|---|---|
| **B-1** | F-5「有意義紅字」**完全沒生效**（`_f2` UnboundLocalError）；**我 commit 的 log 第 327 行就有該 traceback，報告卻寫已修** |
| **F-7-1** | 「歸戶 a 總量守恆」註解**碼中零實作**（我 B-2 改寫時刪了實作留下註解），且我據此對外稱「今日全綠」——**它根本沒跑** |
| **BLOCKED-C** | 宣稱 tag-strip 改為 lookaround，reviewer grep 證**碼未動**（`sed` 字串未命中卻照樣寫進 commit message） |

**⇒ 硬規（已入本波紀律）**：凡宣稱「已修／已驗／已咬合」，**必附實際輸出行**（log 檔名:行號 或原文貼出）；
**無輸出即視為未驗、不得標綠**。**先 grep／先跑，後宣稱。**

### 5.2 閘要「咬得到」才算閘
- **套套邏輯閘**：我的結算閘曾兩邊跑同一 list、加同一 `a_prime` ⇒ diff 恆 0、`apply_plan` 換 no-op 照 PASS。
  ⇒ **凡新立閘，必造反例證其會紅**（本波每個閘都有咬合實證，見 §十二）。
- **prose gate（N0-17-b）**：註解說有閘、碼中沒有 ⇒ 同 5.1。
- **覆蓋率洞**：「沒人檢查 ≠ 相符」。GSA 錨曾因 gid 無決策而**永不被評估**；我的 M-5 閘也曾只審 award gid
  （reviewer 對非 award gid 偷加 +50㎡ ⇒ 全 harness 零咬）。

### 5.3 「哪些要重錨」之判準
**應為「若跑會不會紅」，非「現在紅不紅」。**
我曾據「現在紅不紅」把 `wf/f0~f3` 自登記表刪除——它們不紅是因為 **F.0 raise 級聯使其根本沒跑**。

### 5.4 reviewer 亦不可盡信
二審 reviewer 稱 `_cond1`→`wf_f4:1467`，本文原駁為「實 grep ＝ 1325（該檔無 1467）」——
🔴 **該駁詞本身兩處皆錯**（`ebe24fe` 覆核）：真值 **1338**，且 `1467` **存在**（檔 1588 行）。
**真教訓比「照抄舊數」更利**：「該檔無某行」係**否定性存在主張**（N0-17-c 變體），
在活躍支上**須綁 commit 才成立**——`556bf8e` 之後該檔就長了 13 行。
⇒ **行號在 wip 支是易腐資產**：一律引符號名＋可自癒 grep；非用行號不可者，同列記下其成立之 commit。

### 5.5 數字錨引倉檔
R-9 之「公設調配0m 3」係我憑記憶寫的，實測 **34**。**禁憑記憶出艙**。

---

## 六、機制速查（P-F/P-H 會用到）

**M-5（`verify/m_rescue.py`）**：同歸戶合併規劃·帶優先序 ①街角補足為度 →②餘額他併至 MinA →③餘額回街角。
- **兩趟定點**：趟0(無 rescue)→trunk A₀→`build_plan`→物化 `parcels₁`→趟1 PK 重跑。
  物化後真 G 自然過閘、F.0 級0 自然重排（源宗已移出）⇒ **非「自 F.0 拿回」**。
- **本案實測（3.5m·唯一 award）**：R3右 winner `628-45(2)`·真G 205.27<308.93·
  ①需 a′=**179.32**（供給 270.00）→ G=**308.93**（恰達）·③餘額 **90.68** 回街角 ⇒ a 362.38→**632.38**；
  源 3 宗全額消費移除（`628-30(2)@R2`／`628-45(1)@R5`／`628-30(1)@R5`）。
  `R2左`／`R5左` 池∅ ⇒ **維持強制抵費地**（canonical 最後手段·guard 非 raise）。
- **② 未實作**：本案母體空；碼中為 **loud 停機**（禁靜默轉③）。他案觸發即停機上呈。
- **稽核帳**：`verify/out/got_M5合併帳_退縮3.5m.csv`（4 列）。

**M-5 三閘**（`run_verification.py`·皆有咬合實證）：定點閘／無新生閘／結算閘
（跨物化真檢 (i)target 實增==Σa′ (ii)源殘量==原a−consumed (iii)獨立讀 `a_src` 驗換算
＋**歸戶重劃前地價守恆**·tol＝量化上界 `(存活宗數+alloc數+1)×0.005×p_max(gid)`＝**1,679.53**）。

**關鍵環境變數**：`WV_BAKE=<dir>`（側錄·降 raise 為 print）／`WV_CAPDECOMP=1`／`WV_JKSTAR=1`／`WV_CORNER_TRUEG=1`。

---

## 七、倉態

- `HEAD` == `origin/wip/s1-endpart` == **`5e04b38`**
- working tree：僅 `data/地籍資料來源_匿名版.xlsx` modified（**歷次 commit 皆刻意排除**·見 §四）
- `py_compile` 全綠：`app.py`／`verify/{run_verification,wf_f0,wf_f2,wf_f4,m_rescue,selection_pipeline,stepg_pipeline}.py`
- 近 7 commit：`1a1cb00`(F-1~F-5)→`556bf8e`(F-6)→`5d7eae9`(F-7)→`52f7d39`(F-8)→`8189aea`(F-9)→`845e828`(F-9b)→`5e04b38`(F-9c)
