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

## 三、0m 重驗結果（決定性·殘差全 0）

在 **sgE**（=0m F.4 g_tab 來源）逐街廓驗：

| 街廓 | net(sgE) | net(CSV) | buf_leak | sliver | gap_union | Σ三機制 | **殘差(第四源)** |
|---|---|---|---|---|---|---|---|
| R1 | +0.181 | +0.170 | +0.356 | +0.120 | +0.294 | +0.181 | **−0.0000** |
| R2 | +0.692 | +0.690 | +0.635 | +0.146 | +0.089 | +0.692 | **+0.0000** |
| R3 | +0.044 | +0.050 | +0.308 | +0.174 | +0.438 | +0.044 | **−0.0000** |
| R4 | +0.119 | +0.120 | +0.092 | +0.000 | −0.026 | +0.119 | **−0.0000** |
| R5 | +0.269 | +0.260 | +0.367 | +0.111 | +0.209 | +0.269 | **+0.0000** |
| R6 | +0.176 | +0.170 | +0.321 | +0.095 | +0.240 | +0.176 | **−0.0000** |

### 結論（0m）

1. **net(sgE) ≈ net(CSV)**（含 **R2 +0.692≈+0.690**·完全命中 claude.ai 所指 0m R2 大漏）→ **坐實 sgE ＝ 0m F.4 g_tab 來源**。
2. **恆等式殘差（第四源）＝ 0 全部 6 街廓** → **三機制窮盡於 0m F.4 終態·無第四源**（與 3.5m 同）。
3. R4 之 gap_union ＝ −0.026（唯一負值·strip 銜接反向）——恆等式仍精確成立（殘差 0），證恆等式為代數精確·不受各項符號影響。

### ⚠️ 誠實糾正（前一版本報告之「效能限」誤述）

本報告前版稱「0m 因 E2 窮舉資源限跑不出」——**該定論錯誤**。真因是 CC 診斷用之 `print` 語法 bug（key 誤寫 `"'sgE'"` 帶引號·致 `KeyError`），crash 於 f4 **完成之後**的 print 行（此 crash 恰反證 0m f4 已完整跑完、sgE 已 captured）。修正 key 後 0m 完整跑出（本 §三·殘差全 0）。**教訓**：「跑不出」不得逕歸因效能·須先驗診斷碼本身（no-silent-fallback 之延伸——診斷 bug 亦不得掩蓋為環境限）。

## 四、S0a 結論 → 放行 S0b

- **無第四隱藏漏源**：**3.5m 6/6 ＋ 0m 6/6 共 12/12 街廓恆等式殘差 0**（雙情境決定性實證）＋讀碼證 g_tab=sgE 且 E3/F.1 不進 g_tab 池 → F.1/E3 排除。
- net(sgE)≈net(CSV) 於兩情境全數命中（含 0m R2 +0.692）→ 坐實 sgE ＝ F.4 g_tab 唯一來源。
- 三機制（buf_leak / sliver / gap_union）**窮盡解釋 F.4 終態幾何漏**（兩情境）。
- **§N3-0 之 T2 主修法（`_block_strip` 精確鋪滿）針對此三機制·無遺漏標的** → **S0a 補洞完成（雙情境全驗）·放行 S0b**。

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
