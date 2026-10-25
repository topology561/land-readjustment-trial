# W-P.003 回報（出圖線·執行端）

- 單：`出圖線/orders/W-P.003_附表4-14-15-18-19-21-25.md`（53863 bytes·sha256 `2f236497…1cebe` 與 STATE 相符）
- 結果：**完成**
- 接單：2026-10-25 17:49（`ops/queue` `a56d165`）；完工約 18:05（耗時約 16 分）

## 工項之實測

1. **與主線同步**：側支 `verify/W-P.003-tables-a` 自 `origin/wip/plots`（`cb55e0b`）出；`git merge --no-edit origin/wip/s1-endpart` ⇒ 「Already up to date.」（主線仍 `d4928d4`·無衝突）。
2. **程式**（自單擷取，bytes 與 sha256 皆合）：
   - 甲 `verify/plots/check_W-P003.py`：18454 bytes·`73e62201…85ef` 相符
   - 乙 `verify/plots/mutate_W-P003.py`：4339 bytes·`0e0b4b4a…04bd` 相符
   - 丙 `verify/plots/preview_W-P003.py`：3126 bytes·`39693f9d…5381` 相符
   - 丁 `plots/appx_tables.py`：16978 bytes·`cc5c59f8…61c6` 相符
   - `docs/出圖/W-P.003_附表4-14-15-18-19-21-25.md`：授權逐字、§一 4 之判斷與所據、附表 20／22／23 移 W-P.004 之由、附表 25 與程式現行 Rw 之差（唯記）、量測與故意錯誤之表。
   - commit：`1670550`（`16705506114aa13d67a346eb20173694dd7a23bf`）
3. **量測**：
   - `appx_tables.py --out`（約 18 秒）：
     ```
     附表4 抵充 0 ㎡；附表14 0 列；附表15 0 列
     附表18 53 列（區段 ['a', 'b']·{'a': 43909, 'b': 37323}）
     附表19 6 列；附表21 6 列·Σ面積 22803.33·Σ總價 1643176255.06
     附表25 171 格
     ```
   - `check_W-P003.py`（約 19 秒）⇒ 結束碼 0：
     ```
     PASS P0 七檔皆在、可讀、非空
     PASS P1 表頭 10 欄、無列、三合計 0 ㎡（case_params 抵充地_m2＝0）、簽欄列 7
     PASS P2 表頭三層 21 欄合手冊、無列（現存他項權利 0）、附註與簽欄
     PASS P3 表頭三層 23 欄合手冊、無列（匯入資料無限制登記之欄）、附註與簽欄
     PASS P4 53 列＝53 宗、序（區段→地號）、區段地價 a 43909×5、b 37323×48、評議欄空
     PASS P5 6 列 R1〜R6、單價全精度（|差|≤1e-6）、顯示二位
     PASS P6 6 列；Σ面積 22803.33、Σ總價 1643176255.06（＝KL 之錨）；簽欄列 13
     PASS P7 171 格合手冊（sha256 3ddefae4…）、嚴格遞增、表頭與註
     8/8
     ```
   - 既有之輸出未受擾：`fetch_moedict.py` 之 JSON 63298941 bytes·sha256 `f68fc3df…a7ad` 合；`prelim_maps.py --out --moedict` 出五檔；`synth_W-P002a.py` 出 170 筆；`check_W-P001.py` ⇒ 12/12 通過、結束碼 0；`check_W-P002.py` ⇒ 8/8 PASS、結束碼 0（Q6 分頁符 [43, 83]）。
4. **故意錯誤之測**（`mutate_W-P003.py`·結束碼 0·「合」）：
   | 變異 | 結果 |
   |---|---|
   | 成果 | 綠 |
   | Ⓐ 附表 18 漏一宗 | 紅 P4 |
   | Ⓑ 區段地價未取個位 | 紅 P4 |
   | Ⓒ 附表 21 總價以取整之單價計 | 紅 P6 |
   | Ⓓ 附表 25 用程式現行之 Rw | 紅 P7 |
   | Ⓔ 附表 19 R2、R3 單價互換 | 紅 P5 |
   | Ⓕ 附表 14 漏「權利價值」 | 紅 P2 |
   | Ⓖ 附表 4 為空檔 | 紅 P0、P1 |
   （與單 §二 6 之原型同。）
5. **差異閘**：
   - `git diff --name-status d4928d4 1670550` ⇒ 19 列，皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下 ⇒ **綠**。
   - `git diff --name-status cb55e0b 1670550` ⇒ 唯五新檔（皆 `A`）：`docs/出圖/W-P.003_附表4-14-15-18-19-21-25.md`、`plots/appx_tables.py`、`verify/plots/check_W-P003.py`、`verify/plots/mutate_W-P003.py`、`verify/plots/preview_W-P003.py`。
   - 對照組（拋棄式複本於 `app.py` 末加一行並 commit）⇒ 20 列、`M app.py` 越界 ⇒ **紅**。
6. **預覽 PNG**：`出圖線/成果/W-P.003_附表4-14-15-18-19-21-25.png`（376389 bytes）；目視七表皆在、表頭與值合單。
7. **快轉 `wip/plots`**：`cb55e0b` → `1670550`（快轉·無 `--force`）；`verify/W-P.003-tables-a` ＝ `1670550`（新建）；主線 `wip/s1-endpart` ＝ `d4928d4`（未動）。

## 自捕與自解

- 自捕 1：首次之差異閘以 awk 判路徑，git 預設將中文路徑加引號跳脫（`"docs/\345…"`），致 `docs/出圖/` 之列誤判越界而紅。改以 `git -c core.quotePath=false` 重跑 ⇒ 綠；對照組亦重跑 ⇒ 紅（唯 `app.py` 越界）。純屬驗之命令之誤，程式與成果未改。
- 雲端環境初無 `shapely` 等依賴 ⇒ 依核心線 README 第六節第 2 款 `python3 -m pip install -r requirements.txt --break-system-packages`（⛔ 改 `requirements.txt`）。

## 停機款之檢

§四 1〜5 皆未觸：合併無衝突；附錄甲〜丁皆合；`appx_tables.py` 未報 `SourceError`；未改既有之檔、未加新套件；無單未定之內容判斷。
