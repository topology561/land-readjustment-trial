# W-P.002_補令一　回報（執行端）

- 單：`出圖線/orders/W-P.002_補令一_附表26先左後右.md`（30539 bytes·sha256 `4d7b1b05fde315a1988111a9d747c492eefc6ed2d5df2ac954d49ff0552db14b`·接單時驗之相符）
- 結果：**完成**
- 接單：2026-10-25T13:48:30+08:00（佇列 `79a181b`）；回報：2026-10-25T13:58:53+08:00；耗時約 11 分（其中 `mutate_W-P001` 4 分 29 秒）

## 一、工項之實測

1. **與主線同步**：自 `origin/wip/plots` ＝ `9c0b51c295345eed9d2b4798f37eaff9f5121485` 出側支 `verify/W-P.002a-index-columns`；`git merge --no-edit origin/wip/s1-endpart`（主線 ＝ `d4928d4845513a42fb1ac826a63167a38c78d4fb`·未前進）⇒「Already up to date.」，無衝突。
2. **程式**：
   - 附錄甲 `verify/plots/check_W-P002.py`：13033 bytes·sha256 `a8f94207…5a87` 相符。
   - 附錄乙 `verify/plots/synth_W-P002a.py`：744 bytes·sha256 `5d56a639…d270` 相符。
   - 附錄丙 `verify/plots/mutate_W-P002.py`：8020 bytes·sha256 `761a76c4…05a3` 相符。
   - `plots/owner_index.py` 唯單 §二 1 之三處：加 `APPX26_PER_PAGE = 40` 與 `appx26_slot`；`write_appx26` 之填寫改用 `appx26_slot(i, APPX26_PER_PAGE)`（`per` 於呼叫時讀模組之常數）、`r` 取各筆之列之最大；第 1〜(頁數−1) 頁之末列之後加 `Break(id=3 + p*per)`（`from openpyxl.worksheet.pagebreak import Break` 置函式內之 import）。框線、簽欄、列印標題、紙張照舊。與單之原型差異同式。
   - commit：`cb55e0b396f15179b48f24170bc37683383d4c75`（側支之端）。
3. **量測**（倉外之目錄；`fetch_moedict` 之 JSON 63298941 bytes·sha256 `f68fc3df…a7ad` 合）：
   - `prelim_maps.py` 出五檔（約 20 秒）；`synth_W-P002a.py` 出示範多頁之附表 26。
   - `check_W-P002.py` ⇒ 8/8 PASS、結束碼 0：
     ```
     PASS Q0 sha256 f68fc3df140a…；筆劃 {'草': 10, '花': 8, '蓮': 15, '連': 11, '進': 12, '葉': 13, '蔡': 15, '鄭': 15, '邱': 8, '郭': 11, '阮': 7, '余': 7, '沈': 7}
     PASS Q1 註記 53（期望 53）；不符 []；落宗外 []
     PASS Q1b 錨 {'628-26': 1, '628': 2, '628-2': 3, '628-51': 19, '713': 20, '628-3': 21, '628-35': 22, '628-39': 23, '628-40': 24, '628-15': 33}
     PASS Q2 題 '土地所有權人索引表'；併格差 []；列印標題 $1:$3；欄數 8
     PASS Q3 筆 67；不符 0 []；資料末列 43、簽欄列 45（期望 45）；分頁符 []（期望 []）
     PASS Q4 末列 ['承辦:', '股長:', '科長:', '製表日期: 年 月 日']
     PASS Q5 表頭 ['圖層', '歸戶號', '顏色 R,G,B', '所有權人', '地號']；歸戶號 [1, 2, 3]…[32, 33]（33）；地號合 True；色與圖不符 []
     PASS Q6 筆 170；不符 0 []；資料末列 93、簽欄列 95（期望 95）；分頁符 [43, 83]（期望 [43, 83]）；列印標題 $1:$3
     ```
     （Q2 之列 2、列 3 之內容同單之期望，此處略。）Q3「資料末列 43、簽欄列 45」、Q6「分頁符 [43, 83]」合單 §三 3。
   - `check_W-P001.py` ⇒ 12/12 通過（M0〜M7、T1〜T6）。
   - **對照組**：`9c0b51c` 之 `plots/`（拋棄式 worktree）出之舊輸出跑附錄甲 ⇒ 結束碼 1，唯 Q3 紅：「筆 67；不符 67 …；資料末列 43、簽欄列 39（期望 45）；分頁符 []」（餘 7 項綠）。
4. **故意錯誤之測**：
   - `mutate_W-P002.py`（約 57 秒）：成果綠；Ⓐ Q1、Q3、Q5；Ⓑ Q1；Ⓒ Q3；Ⓓ Q1、Q3、Q5；Ⓔ Q4；Ⓕ 回舊式 Q3；Ⓖ 每頁 30 列 Q6；Ⓗ 無分頁符 Q6——8 種皆紅、皆合期望（同原型）。
   - `mutate_W-P001.py`（4 分 29 秒）：成果綠；①〜⑦、⑧′、⓪、⑨〜⑬ 14 種皆紅、皆合期望。
5. **差異閘**：
   - `git diff --name-status d4928d4 cb55e0b` ⇒ 14 列，皆為 `plots/`、`verify/plots/`、`docs/出圖/` 之下（A：docs 3、plots 3、verify/plots 8）；他處 0 列 ⇒ 綠。
   - `git diff --name-status 9c0b51c cb55e0b` ⇒ 唯 `docs/出圖/W-P.002_補令一_附表26排列.md`（A）、`plots/owner_index.py`（M）、`verify/plots/check_W-P002.py`（M）、`verify/plots/mutate_W-P002.py`（M）、`verify/plots/synth_W-P002a.py`（A）。
   - 對照組：拋棄式複本於側支之端改 `app.py`（附一行）並 commit ⇒ 他處 1 列（`M app.py`）⇒ 紅。
6. **其餘輸出⛔ 變**：新輸出與 `9c0b51c` 之輸出比對（倉外之腳本：DXF 之模型空間圖元以〔類、圖層、幾何〔TEXT 之文字與插入點、LWPOLYLINE 之頂點、HATCH 之邊界頂點，皆取 6 位小數〕、true_color、ACI〕排序後全等；xlsx 逐表逐格之值與併格之集合全等）：
   - DXF 圖元 318 ＝ 318，同。
   - 顏色對照表 185 格同；附表 2 152 格同；附表 3 1530 格同。
7. **預覽 PNG**：`preview_W-P002.py` 之輸出改名 `出圖線/成果/W-P.002_補令一_附表26先左後右.png`（369267 bytes）；目視：左組 40 列（丁…許）、右組 27 列（郭…測試團體182），簽欄在其下。
8. **docs**：`docs/出圖/W-P.002_補令一_附表26排列.md`（KL 10:22 之逐字、排列之規則、40 列之常數為版面之事、量測與故意錯誤之表）。
9. **快轉 `wip/plots`**：`9c0b51c295345eed9d2b4798f37eaff9f5121485` → `cb55e0b396f15179b48f24170bc37683383d4c75`（快轉·⛔ `--force`）；側支 `verify/W-P.002a-index-columns` 新建 ＝ `cb55e0b`。`git ls-remote` 實測二者皆 `cb55e0b`。

## 二、推送

| 目標 | 前 | 後 |
|---|---|---|
| `verify/W-P.002a-index-columns` | （無） | `cb55e0b` |
| `wip/plots` | `9c0b51c` | `cb55e0b` |
| `ops/queue` | 接單 `79a181b` | 本回報之 commit |

主線 `wip/s1-endpart` 與核心線之分支⛔ 動。

## 三、自捕與自解

- 雲端初無 `ezdxf` 等 ⇒ 依核心線 README 第六節第 2 款 `python3 -m pip install -r requirements.txt --break-system-packages`（⛔ 改檔）。
- 差異閘之初跑，`git diff` 未設 `core.quotepath=off` ⇒ 中文路徑被引號包而誤入「他處」之濾；改設 `-c core.quotepath=off` 重跑 ⇒ 0 列。係量測之法之誤，非成果之誤。
- 他無。
