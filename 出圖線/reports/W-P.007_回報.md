# W-P.007 回報　附表 13 之版面照手冊範本（KL 2026-10-31 08:32·17:14）

- 單：`出圖線/orders/W-P.007_附表13之版面.md`（102322 bytes·sha256 `d947d7137c5ec52b470b68d4c530020f64f0beb07cd48e696b13b5a3ce1aca02` 相符）
- 結果：**完成**（無停機款之觸發）。唯預覽 PNG 之 sha256 與單 §二 7 不同（單明定「記之、⛔ 停」·見工項 6）。
- 接單：2026-10-31 21:50（+08:00）；完工：約 22:30；耗時約 40 分鐘（`alloc_state` 6 分 30 秒、`mutate_W-P006` 11 分 14 秒〔首跑被本端之指令逾時中斷·重跑·見自捕〕、`check_W-P006` 成果與對照組並行 3 分 12 秒為大宗）。
- 環境：倉外 venv（`python3 -m venv --system-site-packages /tmp/venv`＋`pip install -r requirements.txt 'numpy<2.3'`）；numpy 2.2.6、matplotlib 3.11.2、openpyxl 3.1.5。

## 工項 1　與主線同步

- 側支 `verify/W-P.007-table13-layout` 自 `origin/wip/plots` ＝ `15935e2d608def08db9bf3dc69fe0b1a75e5981e` 出（推送前遠端無此分支）。
- `git merge --no-edit origin/wip/s1-endpart`（主線 ＝ `9fd34275770b7fc53103b9eb42ba21925f823f9a`·未前進）⇒ **Already up to date**（無合併之 commit）。

## 工項 2　程式（附錄照錄）

| 附錄 | 檔 | bytes | sha256（前 12） | 合 |
|---|---|---|---|---|
| 甲 | `verify/plots/check_W-P007.py` | 13437 | `b9ac2f5cad4c` | ✓ |
| 乙 | `verify/plots/mutate_W-P007.py` | 4034 | `c856e6963228` | ✓ |
| 丙 | `verify/plots/preview_W-P007.py` | 6732 | `298dcceaad1c` | ✓ |
| 丁 | `plots/post_tables.py` | 31432 | `60c01cf0043c` | ✓ |
| 戊 | `verify/plots/check_W-P006.py` | 29461 | `a9a9e535da58` | ✓ |
| 己 | `docs/出圖/W-P.007_附表13版面.md` | 2838 | `9da8bf40e6c1` | ✓ |

- 五 `.py` 之 `py_compile` 皆過。
- commit：`83576c7ab7047f03769cb9ee2c91c6ee738a148c`「W-P.007：附表 13 之版面照手冊範本（KL 2026-10-31 08:32·17:14）」。

## 工項 3　量測

- `fetch_moedict.py` ⇒ `dict-revised.json` 63298941 bytes·sha256 `f68fc3df…a7ad`；`prelim_maps.py` 照出。
- `alloc_state.py --setback 0 --setback 3.5`：退縮 0 m 宗 35（分配地 29、抵費地 6）、退縮 3.5 m 宗 34（分配地 28、抵費地 6）；皆略 `['R1-抵費地-2']`（同 `W-P.006_補令一`）。
- `post_maps.py` 二退縮照出。
- **舊版之輸出**（`git worktree` 於 `15935e2`、`<OLD>` 為 `<O>` 之複本）與新版之 `post_tables.py` 之印出：二退縮**除「輸出」列外逐字同**（`diff` 無差）。新版之印出：
  - 0 m：「附表 13 戶 33（有分配地 16、取配面積可填 14、現金補償 0）＋縣有 11；附表 24 張 29（Σa 可填 14）」
  - 3.5 m：「附表 13 戶 33（有分配地 16、取配面積可填 14、現金補償 0）＋縣有 11；附表 24 張 28（Σa 可填 14）」——皆 ＝ 單 §二 7。
  - 另印程式之提示「歸戶表另有重劃前地籍所無之號（不用）：['628-0', '713-0', '715-0', '717-0', '718-0', '719-0']」，照錄（同前單）。
- `check_W-P007.py <O> <OLD> 0 3.5` ⇒ **14/14 PASS**（二退縮各 L0〜L6）·結束碼 0。
- **對照組** `check_W-P007.py <OLD> <OLD> 0 3.5` ⇒ **紅**·結束碼 1：二退縮皆 L0 綠、L1〜L6 紅（＝ 單 §二 7）。所紅之首例：L1／L5「量測中止：歸戶號1 之附註 0 處」；L2 合併多 `(1,1,1,24)` 等、少 `(3,1,3,24)`、`(4,1,5,7)` 等；L3 A3 為「土地所有權人（首列登記人）姓名」≠ 題；L4 直書少 `(4,11)`、`(8,24)`、`(9,1)`；L6 欄寬之比差 0.0289、紙張之列印標題 `$1:$7`。
- `check_W-P006.py <O> <P> <M>/dict-revised.json 0 3.5` ⇒ **14/14 PASS**（二退縮各 V0〜V6）·結束碼 0。
- **對照組**（`<OLD>` 之副本以新 `check_W-P006` 量之）⇒ **紅**·結束碼 1：二退縮皆 **V1、V2、V3 紅**（V0、V4、V5、V6 綠·＝ 單 §二 7）。首例：V1「歸戶號1 之題；列 8〜10 之表頭」；V2「歸戶號1 之重劃前 0／1 列不合」；V3「之重劃後之列不合」。
- 照舊：`check_W-P005` 18/18；`check_W-P001` 12/12；`check_W-P002`（`synth_W-P002a.py` 出示範附表 26）8/8；`appx_tables.py`＋`check_W-P003` 8/8；`burden_tables.py`＋`check_W-P004` 8/8。

## 工項 4　故意錯誤之測

`mutate_W-P007.py <O> <OLD> <M>/dict-revised.json <拋棄式目錄>`（約 2 分）·結束碼 0：

| 變異體 | 說明 | 結果 |
|---|---|---|
| 成果 | — | 綠 |
| Ⓐ | 住址之標籤未跨四列 | 紅 L2 |
| Ⓑ | 欄名改用他名（取配面積→分配面積） | 紅 L3 |
| Ⓒ | 鄉鎮市區漏直書 | 紅 L4 |
| Ⓓ | 外框未加粗 | 紅 L5 |
| Ⓔ | 首列登記人之姓名與統編錯格 | 紅 L1 |

`mutate_W-P006.py <O> <P> <M>/dict-revised.json <另一拋棄式目錄>`（11 分 14 秒）·結束碼 0：成果綠；Ⓐ 紅 V5、Ⓑ 紅 V4 V5、Ⓒ 紅 V4、Ⓓ 紅 V3、Ⓔ 紅 V6、Ⓕ 紅 V2、Ⓖ 紅 V4 V5、Ⓗ 紅 V4、Ⓘ 紅 V1、Ⓙ 紅 V5（＝ `W-P.006_補令一` 之所紅）。

結論：成果綠、變異體皆紅。

## 工項 5　差異閘

- `git diff --name-status 9fd3427 83576c7`：43 列，皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下（不合 0）⇒ **綠**。
- `git diff --name-status 15935e2 83576c7`：`A docs/出圖/W-P.007_附表13版面.md`、`M plots/post_tables.py`、`M verify/plots/check_W-P006.py`、`A verify/plots/check_W-P007.py`、`A verify/plots/mutate_W-P007.py`、`A verify/plots/preview_W-P007.py` —— 合單。
- 對照組（拋棄式複本改 `app.py` 首列一字並 commit）：44 列、不合 1（`M app.py`）⇒ **紅**（閘非恆綠）。

## 工項 6　預覽 PNG（`preview_W-P007.py <O> <PNG> 0 3.5`）

| 檔（入 `出圖線/成果/`） | 所取 | bytes | sha256 |
|---|---|---|---|
| `W-P.007_附表13版面_退縮0m.png` | 歸戶號29、縣有（抵費地） | 270468 | `53a945fdd29bf383d8ce9d313ab9814bed5ad239240e345d2e6e6a8c2d2837e4` |
| `W-P.007_附表13版面_退縮3.5m.png` | 歸戶號29、縣有（抵費地） | 270653 | `10538a9bf6750796159b43446d3b901b8672f66d77833519d11c0edfb94887ef` |

- 二檔之 sha256 **與單 §二 7（`eaa2985b…93c2`、`a9b5f15f…02a6`）不同**；所取之表同（二表皆「歸戶號29」「縣有（抵費地）」）。單明言「他環境之字形或致 sha256 異·記之、⛔ 停」⇒ 記之、未停。目視：表名與冊頁在框外、所有權人與管理人四列、住址直書跨四列、表頭直書、外框粗線、附註與簽欄緊接框下，如範本。表之內容另由 L0、L1（與舊版逐值同）證之。

## 工項 7　快轉 `wip/plots`

- 側支推送：`verify/W-P.007-table13-layout` ＝ `83576c7ab7047f03769cb9ee2c91c6ee738a148c`（新建）。
- `wip/plots`：`15935e2d608def08db9bf3dc69fe0b1a75e5981e` → `83576c7ab7047f03769cb9ee2c91c6ee738a148c`（快轉·⛔ `--force`）；`git ls-remote` 復核二分支皆 ＝ `83576c7`；主線 `wip/s1-endpart` 仍 ＝ `9fd3427`。

## 自捕與自解

- `mutate_W-P006` 之首跑與 `mutate_W-P007` 並行於同一指令，該指令達本端之 10 分鐘上限而被中斷（已跑至 Ⓘ·皆如期）；改以背景重跑全程，結果如工項 4。非程式之誤，記之。
- 差異閘之首算未設 `core.quotepath=false`，中文路徑被引號包住而誤計 10 列「不合」；設之重算為 0。非程式之誤，記之。
- 未建 PR：併入主線⛔ 由本線為之（README 第三節第 4 款）⇒ 照前例⛔ 建。
- 叫醒發單端：本端無 `fire_trigger` 之授權工具可用（前例亦被拒）⇒ 待其定時之輪。
