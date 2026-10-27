# W-P.004 回報（出圖線·執行端）

- 單：`出圖線/orders/W-P.004_附表20-22.md`（67630 bytes·sha256 `fdf334f8…cff8` 與 STATE 相符）
- 結果：**完成**
- 接單：2026-10-28 01:48（`ops/queue` `702cfb1`）；完工約 01:57（耗時約 12 分）

## 工項之實測

1. **與主線同步**：側支 `verify/W-P.004-burden-tables` 自 `origin/wip/plots`（`1670550`）出；`git merge --no-edit origin/wip/s1-endpart`（`20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`）⇒ 合併之 commit `f53ec43`，無衝突。
2. **程式**（自單擷取，bytes 與 sha256 皆合；`py_compile` 四 `.py` 皆過）：
   - 甲 `verify/plots/check_W-P004.py`：19684 bytes·`bffd0abd…a443` 相符
   - 乙 `verify/plots/mutate_W-P004.py`：4160 bytes·`fdc8af65…aacb` 相符
   - 丙 `verify/plots/preview_W-P004.py`：2814 bytes·`e04c7ee9…2001` 相符
   - 丁 `plots/burden_tables.py`：23181 bytes·`44991167…f8bf3` 相符
   - 戊 `docs/出圖/W-P.004_附表20-22.md`：4161 bytes·`bcf40008…64b5` 相符
   - commit：`9a3cb61`（`9a3cb61bd5397ecaca62ca30b5c32d57a03b8fd8`）
3. **量測**：
   - `burden_tables.py --out`（約 20 秒·結束碼 0）：
     ```
特別負擔 R1.左側 33.25 → RD1
特別負擔 R1.右側 33.27 → RD2
特別負擔 R2.正面 200.05 → RD1
特別負擔 R2.左側 44.95 → RD4
特別負擔 R3.正面 186.81 → RD2
特別負擔 R3.右側 44.9 → RD4
特別負擔 R4.左側 33.27 → RD2
特別負擔 R4.右側 33.08 → RD3
特別負擔 R5.正面 185.6 → RD2
特別負擔 R5.左側 43.53 → RD4
特別負擔 R6.正面 171.71 → RD3
特別負擔 R6.右側 43.38 → RD4
附表20 RD1 1082.27／212.00／870.27；RD2 1035.94／398.87／637.07；RD3 959.67／186.09／773.58；RD4 1604.00／160.62／1443.38；G1 7464.68／0.00／7464.68
附表20 小計 12146.56／957.58／11188.98
附表22 前 1336204754·38500.68；後 1643176255·72058.61；上漲率 1.871619；B 0.171043；C 0.091319；比率 0.4071（0.3475＋0.0596）；人數 63
輸出 /tmp/claude-0/wp4/out/附表20_公共設施用地負擔面積統計表.xlsx
輸出 /tmp/claude-0/wp4/out/附表22_計算負擔總計表.xlsx
     ```
     （與單 §二 6 之原型同。）
   - `check_W-P004.py`（約 21 秒）⇒ 結束碼 0：
     ```
PASS S0 二檔皆在、可讀、非空
PASS S1 題、表頭 6 欄、5 列、小計列 8、簽欄、面積二位
PASS S2 5 列＝圖上之公設區塊（RD1、RD2、RD3、RD4、G1）、合計面積＝圖面面積二位、合計＝特別＋一般
PASS S3 特別負擔 212.00、398.87、186.09、160.62、0.00（未乘之和 1053.80）；小計 12146.56／957.58／11188.98＝錨
PASS S4 實測 34949.89、私 31341.00、公 3365.00、未登記與誤差 0、抵充 0；人數 63（61＋2）；第四項空；第五項 1336204754／38500.68
PASS S5 第六項＝附表 20 小計＝錨；費用 150053099、補助空；第八項 1643176255／72058.61；第九項 22803.33
PASS S6 上漲率 1.871619＝72058.61÷38500.68；B 0.171043、C 0.091319＝錨；比率 0.4071＝0.3475＋0.0596；格式六位與 0.00%
PASS S7 備註（二比率之式、差額 243.89）、簽欄、表下之註（KL 逐字·1,344,405,805／38,498.68）
8/8
     ```
   - 既有之輸出未受擾（主線合併後）：`appx_tables.py` ＋ `check_W-P003.py` ⇒ 8/8、結束碼 0；`fetch_moedict.py` 之 JSON 63298941 bytes·sha256 `f68fc3df…a7ad` 合；`prelim_maps.py --out --moedict` 出五檔；`synth_W-P002a.py` 出示範附表 26；`check_W-P001.py` ⇒ 12/12 通過；`check_W-P002.py` ⇒ 8/8 PASS（Q6 分頁符 [43, 83]）。
4. **故意錯誤之測**（`mutate_W-P004.py`·約 60 秒·結束碼 0·「合」）：
   | 變異 | 結果 |
   |---|---|
   | 成果 | 綠 |
   | Ⓐ 附表 20 漏一區塊 | 紅 S2、S3 |
   | Ⓑ 臨街地特別負擔未乘（1−C） | 紅 S3、S5、S6 |
   | Ⓒ 特別負擔先加總後取位 | 紅 S3 |
   | Ⓓ 第五項用圖面面積之總地價 | 紅 S4、S6 |
   | Ⓔ 上漲率用核心線之重劃前平均地價 | 紅 S6 |
   | Ⓕ 漏表下之註 | 紅 S7 |
   （與單 §二 6 之原型同。）
5. **差異閘**（`core.quotePath=false`）：
   - `git diff --name-status 20e03bf 9a3cb61` ⇒ 24 列，皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下 ⇒ **綠**。
   - `git diff --name-status 1670550 9a3cb61 -- plots verify/plots docs/出圖` ⇒ 唯五新檔（皆 `A`）：`docs/出圖/W-P.004_附表20-22.md`、`plots/burden_tables.py`、`verify/plots/check_W-P004.py`、`verify/plots/mutate_W-P004.py`、`verify/plots/preview_W-P004.py`。
   - 對照組（拋棄式複本於 `app.py` 末加一行並 commit）⇒ 25 列、`app.py` 越界 ⇒ **紅**。
6. **預覽 PNG**：`出圖線/成果/W-P.004_附表20-22.png`（180434 bytes）；與 `出圖線/待KL/W-P.004_第二版原型預覽.png` 逐位元組同（`cmp`）；目視二表、簽欄、表下之註皆在。
7. **快轉 `wip/plots`**：`1670550` → `9a3cb61`（快轉·無 `--force`）；`verify/W-P.004-burden-tables` ＝ `9a3cb61`（新建）；主線 `wip/s1-endpart` ＝ `20e03bf`（未動）。

## 自捕與自解

- 雲端環境初無 `ezdxf` 等依賴 ⇒ 依核心線 README 第六節第 2 款 `pip install -r requirements.txt --break-system-packages`（⛔ 改 `requirements.txt`）。
- 執行所生之 `__pycache__` 於 commit 前刪之（未入倉）。

## 停機款之檢

§四 1〜5 皆未觸：合併無衝突；附錄甲〜戊皆合、S0〜S7 皆過；`burden_tables.py` 未報 `SourceError`；未改既有之檔、未加新套件；無單未定之內容判斷。
