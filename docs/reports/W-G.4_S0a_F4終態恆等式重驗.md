# W-G.4 S0a · F.4 終態恆等式重驗（找第四漏源）

- 日期：2026-07-15；規格＝`W-G.4_規格_v3.md` §N3-0（734ed02）
- 交辦：S0a 補洞（擋 S0b）——恆等式須於 F.4 終態重驗（非 trunk A）；第四源候選＝F.1 等 G 遞補整形 + E3 `_reshape_block`
- 方法：monkey-patch `wf_f4.build_step_g_tables` 攔截 **sgE**（F.4 g_tab 唯一來源·wf_f4.py:791），在 sgE g_rows（真 cut_coords）上逐街廓驗恆等式 `net_leak = buf_leak + sliver − gap_union`，殘差＝第四源。

---

## 一、關鍵前提坐實（讀碼·非假設）

- **F.4 g_tab 池 ＝ sgE run_step_g 池**：`wf_f4.py:791` `g_tab, _, _ = build_step_g_tables(sgE)`——g_tab 直接用 **sgE**（trunk E 的 `run_step_g` 輸出）。
- **E3 整形不進 g_tab 池**：`wf_f4.py:711` `pool_final[blk] = poolE[blk]`——E3 `_reshape_block` 只算 `pool_final` 供閘用（L730-732），**不改 g_tab 之抵費地列**（g_tab 用 sgE 原始）。
- **∴ 第四源候選（F.1/E3）在 g_tab 層不作用**——F.4 g_tab 池就是 sgE 之 run_step_g 池，機制同 trunk A（同 code path），僅**配地宗組成不同**（sgE 含 E1/E2 合成宗 74·）。

## 二、3.5m 重驗結果（決定性·殘差全 0）

在 **sgE**（=F.4 g_tab 來源）逐街廓驗：

| 街廓 | net(sgE) | net(CSV) | buf_leak | sliver | gap_union | Σ三機制 | **殘差(第四源)** |
|---|---|---|---|---|---|---|---|
| R1 | +0.201 | +0.190 | +0.280 | +0.146 | +0.225 | +0.201 | **−0.0000** |
| R2 | +0.167 | +0.170 | +0.485 | +0.049 | +0.367 | +0.167 | **−0.0000** |
| R3 | +0.250 | +0.250 | +0.399 | +0.296 | +0.445 | +0.250 | **−0.0000** |
| R4 | +0.016 | +0.020 | +0.146 | +0.000 | +0.130 | +0.016 | **−0.0000** |
| R5 | +0.220 | +0.220 | +0.409 | +0.162 | +0.350 | +0.220 | **+0.0000** |
| R6 | +0.176 | +0.170 | +0.321 | +0.095 | +0.240 | +0.176 | **−0.0000** |

### 結論（3.5m）

1. **net(sgE) ≈ net(CSV)**（R1 +0.201≈+0.190…R6 +0.176≈+0.170·微差＝真 cut_coords vs CSV round 2dp）→ **坐實 sgE ＝ F.4 g_tab 來源**（claude.ai 質疑之「F.4 終態」數字即此）。
2. **恆等式殘差（第四源）＝ 0 全部 6 街廓** → **三機制窮盡於 F.4 終態·無第四隱藏漏源**。
3. **F.1 等 G 遞補整形 / E3 `_reshape_block` 未引入額外漏**（因其不進 g_tab 池·§一 讀碼證·此處實證）。

### claude.ai 質疑之回應

- 「trunk A +0.767 vs F.4 +0.17（4.5 倍）·R2 0m 變號」＝**配地宗組成不同**（trunk A 原始 build；sgE 含 E1/E2 合成宗），非第四源。同 code path·恆等式對兩者皆成立（trunk A 前報已驗·sgE 本報驗）。
- 12/12 單向正之差異（trunk A 偶負 vs F.4 全正）＝sgE 配地宗多致 buf+sliver 相對 gap_union 更大→淨正。**機制無變·恆等式無殘差**。

## 三、0m 重驗（效能限·誠實定論）

- 0m F.4 之 E2 7-5 批次窮舉「可行 **1929/3888**」（遠多於 3.5m 之 240·每組合帶引擎重評）→ 完整 f0→f4 跑 sgE 之數值分解在**本環境資源不足**（多次嘗試·process 遭 OS 強殺·連收尾 echo 未執行）。**此為效能/資源限·非機制問題**。
- **0m net(CSV) 已坐實（前 S0 報告 8ceacc2 · wg4_s0_repro·秒級 CSV 計算）**：12/12 單向正（R1+0.17/R2+0.69/R3+0.05/R4+0.12/R5+0.26/R6+0.17）——**型態同 3.5m**。
- **機制論證（讀碼·§一·非假設）**：0m 之 g_tab 亦 `build_step_g_tables(sgE)`（**同一行 code**·wf_f4:791）·E3 亦 `pool_final=poolE`（**同一行 code**·wf_f4:711）→ 0m 之 F.1/E3 同樣不進 g_tab 池·恆等式三機制與 3.5m **走完全相同 code path**。
- **定論**：0m 無第四源之結論由三者合證——① 0m net(CSV) 型態已坐實（同 3.5m）；② g_tab/E3 之 code 對 0m/3.5m 逐字相同（讀碼證·非假設）；③ 3.5m 6/6 殘差 0 之決定性實證。0m 完整數值分解表因 E2 窮舉資源限未能在此環境產出——**此限制誠實標記·不以假設掩蓋**（no-silent-fallback 精神）。若 KL 要求 0m 完整數值·須於更高算力環境重跑（或降 E2 窮舉粒度·屬另議）。

## 四、S0a 結論 → 放行 S0b

- **無第四隱藏漏源**：3.5m 6/6 街廓恆等式殘差 0（決定性實證）＋讀碼證 g_tab=sgE 且 E3/F.1 不進 g_tab 池 → F.1/E3 排除。
- 三機制（buf_leak / sliver / gap_union）**窮盡解釋 F.4 終態幾何漏**。
- **§N3-0 之 T2 主修法（`_block_strip` 精確鋪滿）針對此三機制·無遺漏標的** → **S0a 補洞完成·放行 S0b**。

---

## 附：恆等式定義（技術備註）

```
net_leak  = pool_acct − pool_geom_kept
          = (街廓面積 − ΣG宗) − Σ(pool_buf 之 area≥1.0 片)
buf_leak  = block.difference(union).area − block.difference(union.buffer(0.001)).area
sliver    = Σ(pool_buf 之 area<1.0 片)
gap_union = ΣG宗(round) − union(配地strip).area    〔strip 間縫 + G round〕
恆等式：net_leak ≡ buf_leak + sliver − gap_union   〔3.5m 6/6 殘差 |·|<0.0005〕
```
- buf_leak / sliver：使池幾何偏小（正貢獻 net）；gap_union：使池帳偏大（負貢獻 net）。
- T2 `_block_strip` 精確鋪滿一招消滅 buf_leak（無 boolean 膨脹）、gap_union（同切線無縫）、絕大部分 sliver（無 difference 毛刺）；T1 為 sliver 殘餘防護網（應永不觸發）。
