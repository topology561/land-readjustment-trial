# W-P.006 回報　附表 13、24（先做格式與可填之欄）

- 單：`出圖線/orders/W-P.006_附表13-24.md`（90128 bytes·sha256 `b25be2cdefb5cf5ec748f2a6a7131219488d35d5b8dcba1c64c303cdecf8c31c` 相符）
- 結果：**完成**（一處記之、⛔ 停：預覽 PNG 之 sha256 與單 §二 8 不同，見工項 6）
- 接單：2026-10-30 21:49（+08:00）；完工：約 22:25；耗時約 36 分鐘（`alloc_state` 6 分 43 秒、`mutate_W-P006` 6 分 56 秒、`check_W-P006` 3 分 10 秒為大宗）。
- 環境：倉外 venv（`python3 -m venv --system-site-packages`＋`pip install -r requirements.txt 'numpy<2.3'`）；matplotlib 3.11.2、openpyxl 3.1.5、Pillow 12.3.0。

## 工項 1　與主線同步

- 側支 `verify/W-P.006-tables-13-24` 自 `origin/wip/plots` ＝ `351e8548b88bf58993966f59bda6b821ae573d6b` 出。
- `git merge --no-edit origin/wip/s1-endpart`（主線 ＝ `9fd34275770b7fc53103b9eb42ba21925f823f9a`，未前進）⇒ **Already up to date**（無合併之 commit）。

## 工項 2　程式（附錄照錄）

| 附錄 | 檔 | bytes | sha256 | 合 |
|---|---|---|---|---|
| 甲 | `verify/plots/check_W-P006.py` | 26177 | `04cd3db2…1958` | ✓ |
| 乙 | `verify/plots/mutate_W-P006.py` | 4266 | `25854029…5858` | ✓ |
| 丙 | `verify/plots/preview_W-P006.py` | 4054 | `8f6a8573…f2cb` | ✓ |
| 丁 | `plots/alloc_state.py` | 11655 | `6ab75de5…9260` | ✓ |
| 戊 | `plots/post_tables.py` | 24041 | `3ce914e8…dd8d` | ✓ |
| 己 | `docs/出圖/W-P.006_附表13-24.md` | 3826 | `9683f80f…01bf` | ✓ |

- 五 `.py` 之 `py_compile` 皆過。
- commit：`1c9caf5e8d3202c420c738e23b5fa43b89baf8c4`「W-P.006：附表 13 重劃前後土地分配清冊、附表 24 土地分配計算表（先做格式與可填之欄）」。

## 工項 3　量測

- `fetch_moedict.py` ⇒ `dict-revised.json` 63298941 bytes·sha256 `f68fc3df…a7ad`；`prelim_maps.py` 照出。
- `alloc_state.py --setback 0 --setback 3.5`（6 分 43 秒）：
  - 退縮 0 m：宗 35（分配地 29、抵費地 6）；略 `['R1-抵費地-2']`
  - 退縮 3.5 m：宗 34（分配地 28、抵費地 6）；略 `['R1-抵費地-2']`
  - 檔內「財務」：B ＝ 0.17104255833716267、C ＝ 0.0913189310870504；重劃前單價 a 43909.2308486259、b 37322.846221332016；「歸戶表」59 項；「現金補償」`[]` —— 皆 ＝ 單 §二 8。
- `post_maps.py` 二退縮：照出（公告圖、地號對照表、重劃後顏色對照表）；地號之序由 `check_W-P005` 驗之（18/18）。
- `post_tables.py` 二退縮（各約 22 秒）：
  - 0 m：附表 13 戶 33（有分配地 16、現金補償 0）＋縣有 11；附表 24 張 29
  - 3.5 m：附表 13 戶 33（有分配地 16、現金補償 0）＋縣有 11；附表 24 張 28
  - 例（3.5 m 地號 5·歸戶號 32）：G 638.61、Σ 1047.00（947.97＋99.03）、① 64.18、② 344.21、③ 33321、負擔額 4893467＋11469421＝16362888、差額 0 —— ＝ 單 §二 8。
  - 另印「歸戶表另有重劃前地籍所無之號（不用）：['628-0', '713-0', '715-0', '717-0', '718-0', '719-0']」（程式之提示，照錄）。
- `check_W-P006.py <O> <P> <M> 0 3.5` ⇒ **14/14 PASS**（二退縮各 V0〜V6）·結束碼 0（3 分 10 秒）。
- 照舊：`check_W-P005` 18/18；`check_W-P001` 12/12；`check_W-P002`（`synth_W-P002a.py` 出示範附表 26）8/8；`appx_tables.py`＋`check_W-P003` 8/8；`burden_tables.py`＋`check_W-P004` 8/8。

## 工項 4　故意錯誤之測（`mutate_W-P006.py`·退縮 3.5 m·6 分 56 秒·結束碼 0）

| 變異體 | 說明 | 結果 |
|---|---|---|
| 成果 | — | 綠 |
| Ⓐ | 抵費地負擔面積漏 ÷(1−C) | 紅 V5 |
| Ⓑ | 附表 24 漏一宗 | 紅 V4、V5 |
| Ⓒ | 地價比 A 以個位之重劃前單價計 | 紅 V4 |
| Ⓓ | 抵費地與公設之備註互換 | 紅 V3 |
| Ⓔ | 現金補償之備註漏寫 | 紅 V6 |

結論：成果綠、變異體皆紅（＝ 單 §二 8）。

## 工項 5　差異閘

- `git diff --name-status 9fd3427 1c9caf5`：37 列，皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下（不合 0）⇒ **綠**。
- `git diff --name-status 351e854 1c9caf5`：`M plots/alloc_state.py`＋`A` 五檔（`docs/出圖/W-P.006_附表13-24.md`、`plots/post_tables.py`、`verify/plots/check_W-P006.py`、`mutate_W-P006.py`、`preview_W-P006.py`）—— 合單。
- 對照組（拋棄式複本改 `app.py` 首列一字並 commit）：38 列、不合 1（`M app.py`）⇒ **紅**（閘非恆綠）。

## 工項 6　預覽 PNG（入 `出圖線/成果/`）

- `W-P.006_附表13-24_退縮0m.png`（191662 bytes·sha256 `7880765823b33a100b951f680f34af098db3420a7adac8c4873f8b27cc766416`·歸戶號 32、地號 2）
- `W-P.006_附表13-24_退縮3.5m.png`（192033 bytes·sha256 `9e1558411729d07c56184ff9bc06631f05521def74c57a6f5d454ebb7f71ad3f`·歸戶號 32、地號 5）
- **與單 §二 8 之 sha256 不同**（單：0 m `72c0af1e…2307`、3.5 m `438ccaaa…69d`）——依單「不同者記之、⛔ 停」：
  - 本環境重出二次逐位元組同（確定性）。
  - 與 `待KL/W-P.006_原型預覽_退縮3.5m.png`（sha256 ＝ `438ccaaa…69d`）比：尺寸同（2080×1600），相異之像素唯在文字之筆畫（逐列之字帶），格線與版位同；目視二圖之字與數逐一相同（地號 5、G 638.61、①64.18、②344.21、負擔額 16,362,888 等）。判為字形繪製之環境差（matplotlib 等版本），非內容之差。
  - 表之內容由 `check_W-P006` 14/14 獨立驗之。

## 工項 7　快轉 `wip/plots`

- 側支 `verify/W-P.006-tables-13-24` 推至 `1c9caf5`（新分支）。
- `wip/plots`：`351e8548b88bf58993966f59bda6b821ae573d6b` → `1c9caf5e8d3202c420c738e23b5fa43b89baf8c4`（快轉·無 `--force`）。
- 主線 `wip/s1-endpart` 未動（`9fd3427`）。

## 自捕與自解

- 差異閘之首試以 `git diff` 之預設輸出比對，中文路徑被引號跳脫致比對式誤判（非成果之誤）；改以 `core.quotepath=false` 重做，結果如工項 5。
- 未開 PR：本線之併入主線依 README 第三節第 4 款由 KL 另定，本線⛔ 為之。
