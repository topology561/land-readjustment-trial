# W-G Y 波 dump 對拍摘要（sub-cent 定位器）

- 產出：verify\out\y_dump\y_dump_diff_摘要.md
- 工具：`verify/tools/y_dump_diff.py`
- Live 種子：`verify/out/y_dump/f3_G_values_退縮{0m|3.5m}_livedump.json`（KL localhost dump·步驟 G 完成後·Patch B-2 尚未觸發）
- Harness 種子：`case_params_UC9898.json` + `V6.dxf` + `地籍資料來源_匿名版.xlsx` → `run_step_g`

## 退縮 0m

- 列數：live=70 / harness=68 / 交集=68
- 僅 live 有（app 端獨有·多為 ghost）：2
- 僅 harness 有（若非 0 屬異常）：0
- 總欄差異數（列 × 欄）：**495**

**僅 live 有之列**：
  - _GHOST_(R1)
  - _GHOST_(R4)

**分類統計**：

- ①迭代/收斂：40 欄差異
- ②area_geom：64 欄差異
- ③Patch B-2：0 欄差異
- ④ghost：0 欄差異
- ⑤其他：391 欄差異

**欄別 top 差異**：

| 欄 | 分類 | 差異列數 | max abs diff |
|---|---|---|---|
| 幾何面積(㎡) | ②area_geom | 64 | 109.5 |
| A 地價比 | ⑤其他 | 59 | 0.1857 |
| 負擔比率 | ⑤其他 | 59 | 0.0291 |
| 累積S(m) | ⑤其他 | 58 | 1.26 |
| G(㎡) | ⑤其他 | 57 | 32.05 |
| S(m) | ⑤其他 | 50 | 0.69 |
| 宗地寬度(m) | ⑤其他 | 50 | 0.69 |
| 迭代次數 | ①迭代/收斂 | 40 | 7 |
| W(m) | ⑤其他 | 34 | 1.15 |
| Rw(%) | ⑤其他 | 24 | 1.82 |

## 退縮 3.5m

- 列數：live=72 / harness=70 / 交集=70
- 僅 live 有（app 端獨有·多為 ghost）：2
- 僅 harness 有（若非 0 屬異常）：0
- 總欄差異數（列 × 欄）：**491**

**僅 live 有之列**：
  - _GHOST_(R1)
  - _GHOST_(R4)

**分類統計**：

- ①迭代/收斂：45 欄差異
- ②area_geom：63 欄差異
- ③Patch B-2：0 欄差異
- ④ghost：0 欄差異
- ⑤其他：383 欄差異

**欄別 top 差異**：

| 欄 | 分類 | 差異列數 | max abs diff |
|---|---|---|---|
| 幾何面積(㎡) | ②area_geom | 63 | 109.5 |
| A 地價比 | ⑤其他 | 59 | 0.1857 |
| 負擔比率 | ⑤其他 | 59 | 0.0291 |
| G(㎡) | ⑤其他 | 57 | 32.05 |
| 累積S(m) | ⑤其他 | 56 | 1.26 |
| S(m) | ⑤其他 | 50 | 0.69 |
| 宗地寬度(m) | ⑤其他 | 50 | 0.69 |
| 迭代次數 | ①迭代/收斂 | 45 | 7 |
| W(m) | ⑤其他 | 32 | 1.15 |
| Rw(%) | ⑤其他 | 20 | 1.82 |

## 判讀重點（Y 波 sub-cent 靶）

① **迭代/收斂 差異 > 0**：solve_G_binary tol=0.01 之收斂路徑於 live vs harness 分岔；重點查 fake_st vs 真 st 差、B/C 精度差、W_prev thread 差；
② **area_geom 差異 > 0**：shapely `buffer(0)` 版本／`_res['area_geom'] = round(S × avg_depth, 2)` 之來源差；
③ **A 地價比整體性偏移**（若集中在特定歸戶）：post_price/pre_price 快照 vs live 分岔（非 sub-cent·屬財務同源性問題）；
④ **ghost 列 only-live**：預期（Y.0 拿掉 stepg L228-232 後對齊）；
⑤ **其他 sub-cent**：逐欄查 tol/round 鏈條。
