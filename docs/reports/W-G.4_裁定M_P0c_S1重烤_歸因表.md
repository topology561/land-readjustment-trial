# W-G.4 裁定 M · P-0c — S1 波末重烤**逐錨歸因表**（Q-S2②）

> claude.ai 裁 Q-S1/S2/S3（2026-07-25）：完整 S1 波末重烤升格 P-0c·先於一切 M-5 碼·單獨 commit·
> 歸因一律標 **S1**（W脫鉤 07-19＋S0d 07-20）。**烤源＝committed xlsx**（blob `80f75ee`）。
> 本表＝Q-S2②「每錨一列（舊→新→成因→倉內證據指標）」；**禁 S1+M 混因**·M-5 相關格此輪禁動（留 P-H）。
> 基準 `7857059`。

## 〇、重烤後狀態與 provenance

| 項 | 值 | 證據 |
|---|---|---|
| 重烤後 run_all | **130 PASS ／ 2 FAIL** | `verify/out/M_P0c_main_verify.log`（主樹）＝worktree（committed xlsx）逐位同 |
| 殘 2 FAIL | `W-F F.4`（3.5m E2 7<9 不可行）＋`W-G G.2`（`_f4` cascade） | **genuine pre-M-5 死因·M-5(P-D/E) 之靶·非 baseline staleness·同 BEFORE 名目** ⇒ **「不新增名目」成立** |
| **全綠不可達之誠實聲明** | F.4 3.5m E2 係 M-5 **待解之死因**（成因既有·非 S1·非本波引入）⇒ **P-0c 無法達全綠**·最佳達成即 130/2 | `wg4-628-37-3.5m-pinpoint`／memory |
| provenance | **committed xlsx == modified xlsx**（39 家族全同·非僅 F.0） | 主樹(modified) 130/2 == worktree(committed) 130/2 ⇒ xlsx 🚩 對 baseline 無影響 |
| 烤源潔淨 | worktree HEAD `7857059`·xlsx blob `80f75ee` | `git -C <wt> hash-object data/…xlsx` == index blob |

## 一、碼字面錨（4 項·逐錨）

| # | 錨（檔:行） | 舊 → 新 | 成因（S1） | 倉內證據指標 |
|---|---|---|---|---|
| A-1 | `wf_f0.py GSA_EXPECT` 0m G007 | **362.08 → 359.43** | 628-20(2)@R5：**W 20.05→18.41／Rw 20.52→27.51**（W脫鉤）·**S 8.21→8.15**（S0d）→ G。〔reviewer NOTE 更正：前版誤把 W 稱 Rw、Rw 稱 S·CLAUDE.md W≠Rw≠S 禁混〕 | `wf/f0/F.0_G值_退縮0m.csv` 628-20(2) 列／`M_P0c_provenance.log` |
| A-1 | 同 0m G010／G014 | 294.81→293.72／127.06→127.05 | 同上（trunk A G） | `F.0_G值_退縮0m.csv` |
| A-1 | 3.5m G007／G010／G014 | 369.05→369.41／298.63→298.61／129.21→129.20 | 同上 | `F.0_G值_退縮3.5m.csv` |
| A-1 | 0m/3.5m G006／G009／G017 | **不動**（365.84／153.19／433.68） | 未涉 W/S 變之宗 | 同檔 |
| **A-2** | `run_verification.py K_STAR_EXPECT` → **per-tag** | 單 dict `{R1:2,…}` → `{"0m":{R1:2…},"3.5m":{R1:1…}}` | S0d 改 S → R1 3.5m 最優切點 2→1；**跨情境不變係 S0d 前巧合非設計不變量**（註解已更正） | **`probe_jkstar_legitimacy.py`／`M_P0c_jkstar.log`**（J(k*)≥J(naive) 雙情境 PASS·永久閘背書） |
| A-3 | `run_verification.py:691` F.0 釋池 G030 | **55.18 → 55.09** | W脫鉤+S0d 改 trunk A → 梯3 釋池 ΣG 微降 | `M_P0c_main_verify.log`（F.0 釋池列綠） |
| **A-4** | `run_verification.py:845` F.1 標記制 0m | **期 2 → 1** | S1 改 trunk A 幾何：R3 0m BEFORE＝池主體 1713.77＋**碎片 78.24**(寬3.44<3.5·標記待F.4)；S1 後＝**單一池主體 1795.17**(寬40.36·旗標全空)·碎片併入·不再標記。〔reviewer 更正：BEFORE 係**碎片**非楔形；forced 角落鎖定只在 3.5m〕 | `F.1_碎片處置_退縮0m.csv`（R3-78.24 標記列移除）＋`wd3_fragment_geom.csv`（0m R3 單列 1795.17） |

## 二、CSV baseline 家族（39 檔·逐家族代表錨）

| 家族 | 檔數 | 代表錨 舊→新 | 成因（S1） | 證據 |
|---|---|---|---|---|
| `v3/滑池槽診斷` | 2 | R1 0m J(naive) 60.3553→55.3577·J(k*) 66.517→65.5805 | W脫鉤 改 W→Rw→J | `M_P0c_jkstar.log`（同 J 值） |
| `v3/逐槽 J 表` | 2 | R1 0m dev(m) 42.15→39.60·3.5m 20.07→17.50 | S0d 改 S→落位 dev | git diff 該檔 |
| `v3/G 值計算結果` | 2 | 抵費地列（R2/R6）·宗 G 微移 | forced/pool 幾何 + trunk A | git diff |
| `v3/W-D.1.2 診斷` | 2 | G估欄隨財務·非 winner | 率鋪底（既往·非本波 Q1） | git diff |
| `v3/W-D.4 四梯/碎片/跨占` | 6 | G001 ΣG 768.94→768.37 | trunk A 下游 | git diff |
| `v3/wd3 碎片幾何/逐邊` | 2 | R3/R2 抵費地碎片幾何 | trunk A 抵費地幾何 | git diff |
| `wf/f0`（trunk B） | 10 | 628-20(2) G 362.08→359.43 | 同 A-1 | `F.0_G值_*` |
| `wf/f1`（碎片/池/整形） | 5 | 碎片處置/池驗證隨 trunk B | trunk B 傳遞 | git diff |
| `wf/f2`（trunk C·跨街廓） | 6 | F.2 G值/池流向隨 trunk B/C | trunk B/C 傳遞 | git diff |
| `wf/f3`（trunk D·公設） | 4 | F.3 G值/池流向/轉7-4 | trunk C/D 傳遞 | git diff |
| `第 1 宗街角地指配`／`退縮參數`／`W-D.1.3` | 4 | 隨 trunk A（達標/選中零翻盤·僅值微移） | trunk A | git diff |

**全 39 檔＋4 碼錨之成因皆 S1（W脫鉤+S0d 及其 trunk A→B→C→D 傳遞）·無一 M-5·無一裁定M 引入。**

## 三、Q-S2 五步之狀態

| 步 | 狀態 |
|---|---|
| ① worktree 重烤（committed xlsx）＋補交三證據腳本/log | ✅ `M_P0c_f0only.log`（22→34）／`M_P0c_provenance.log`（committed==modified）／`probe_jkstar_legitimacy.py`＋`M_P0c_jkstar.log`（J(k*)≥J(naive)） |
| ② 逐錨歸因表（本檔·烤源 committed xlsx） | ✅ 本檔 |
| ③ reviewer 逐錨獨立復現 | **⏳ 送審中**（本 commit 後路由） |
| ④ apply＋push 後停手·不進 P-C | **⏳ reviewer 綠後執行** |
| ⑤ 等 claude.ai 異機重跑 run_all 驗＋抽核 GSA/k*→KL 綠燈 | **⏳** |

## 四、BEFORE log 保留（Q-S2·未覆寫）

`verify/out/M_before_runall.log`（42/22·`706cb17` committed）**原封未動**。P-0c 之新 log 皆新檔名
（`M_P0c_*`）。

## 五、🚩 域旗標（reviewer Q-S2③ 提·**不阻 P-0c·上呈 KL/claude.ai**）

**R3 0m「單一池主體」之域正確性**：S1（W脫鉤+S0d·07-19/20）改 R3 0m 幾何——BEFORE 為
池主體 1713.77 ＋ 碎片 78.24（寬 3.44<3.5·標記待 F.4），S1 後併為**單一池主體 1795.17**（寬 40.36·畸零旗標全空）。
- reviewer 獨立證：此係**引擎 genuinely 產出**（`_exp_m=1` 非硬湊）·byte-reproducible·**非 cover-up、非 regression**（forced 角落鎖定仍在 3.5m·BEFORE 389.85→AFTER 308.93）。
- **旗標點**：R3 0m 該不該有一片待 F.4 之碎片（＝R3 0m 終態幾何是否應含 78.24 碎片）係**域判斷層**問題（CC 與 reviewer 同模型·共盲區）。
- **不阻 P-0c**：R3 幾何由 **S1（早於 P-0c）**決定·P-0c 僅忠實烤既有 S1 引擎輸出；此旗標針對 **S1 引擎本身**、非本重烤。上呈 KL/claude.ai 覆核。

## 六、reviewer Q-S2③ 獨立復現裁決（2026-07-25）

**判：可 commit+push**。決定性雙 byte-identity：
① committed-xlsx 重烤 == 主樹 39 CSV（0 mismatch·非手改）；
② bake@HEAD == bake@`ffc5c17`（抽取前·P-0a 之父）全 57 CSV byte-identical ⇒ **P-0a/0b/A/B 對 got_rows 零改·無 M-5 洩漏**（最強證明）。
守恆全 ≤0.02㎡；k*/GSA/釋池/標記/provenance 皆獨立通過。
**條件**：(1) commit **排除 modified xlsx**（`875d75c8`≠`80f75ee`·硬）；(2) R3 0m 域旗標（§五·不阻）；(3) A-1/A-4 標籤更正（已修）。
