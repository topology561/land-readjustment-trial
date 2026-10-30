# W-P.005_補令一　回報（執行端）

- 結果：**完成**
- 單：`出圖線/orders/W-P.005_補令一_寬深之註記.md`（88425 bytes·sha256 `0ec9ac826bd83bf334823233bd2e1df0b857b4e10cbc02cde617c0008b6480c4` 相符）
- 接單：2026-10-30 09:48（+08:00）；完工：約 10:15；耗時約 27 分鐘（`alloc_state` 8 分 11 秒、`mutate_W-P005` 3 分 05 秒為大宗）。
- 環境：倉外 venv（`python3 -m venv --system-site-packages`＋`pip install -r requirements.txt 'numpy<2.3'` ⇒ numpy 2.2.6、ezdxf 1.4.5、shapely 2.2.0）。

## 工項 1　與主線同步

- 側支 `verify/W-P.005a-width-depth` 自 `origin/wip/plots` ＝ `9deaad28ca37bd24c4c02ddc86d65da3b7a9d574` 出。
- `git merge --no-edit origin/wip/s1-endpart`（主線 ＝ `9fd34275770b7fc53103b9eb42ba21925f823f9a`）⇒ 合併之 commit `68ef3bebcba278a32efcb92fd9f7943bff6be045`，**無衝突**。

## 工項 2　程式（附錄甲〜己）

| 附錄 | 檔 | bytes | sha256 |
|---|---|---|---|
| 甲 | `verify/plots/check_W-P005.py` | 25303 | `bc02ed38…0404` 相符 |
| 乙 | `verify/plots/mutate_W-P005.py` | 7620 | `d18e4f40…90b8` 相符 |
| 丙 | `verify/plots/preview_W-P005a.py` | 4160 | `ccc1f179…8c8e` 相符 |
| 丁 | `plots/alloc_state.py` | 8433 | `a1212c6a…dbf7` 相符 |
| 戊 | `plots/post_maps.py` | 20692 | `0bd89669…b00d` 相符 |
| 己 | `docs/出圖/W-P.005_補令一_寬深之註記.md` | 2287 | `9bff9e11…f83e` 相符 |

- 五 `.py` 之 `python -m py_compile` 皆過。
- commit `351e8548b88bf58993966f59bda6b821ae573d6b`（「W-P.005_補令一：公告分配地籍線之寬改顯示 S、深＝面積÷W、街角第 1 宗之深納道路截角」）。

## 工項 3　量測

- `fetch_moedict.py` ⇒ `dict-revised.json` 63298941 bytes·sha256 `f68fc3df…a7ad`。
- `prelim_maps.py --out <P> --moedict` ⇒ 出五檔（結束碼 0）。
- `alloc_state.py --out <O> --setback 0 --setback 3.5`（8 分 11 秒·結束碼 0）：
  ```
  退縮 0 m：宗 35（分配地 29、抵費地 6）；略 ['R1-抵費地-2']
  退縮 3.5 m：宗 34（分配地 28、抵費地 6）；略 ['R1-抵費地-2']
  ```
  ＝ §二 7。
- `post_maps.py`（二退縮·結束碼皆 0）：
  - 3.5 m：分配地 28、抵費地 6、公設 5；地號 R1-05→1 … R1-01→5、R2-01→6 … R2-07→12、R3-01→13 … R3-06→18、R4-01→19 … R4-03→21、R5-07→22 … R5-01→28、R6-06→29 … R6-01→34、RD1→35、RD2→36、RD4→37、RD3→38、G1→39 ⇒ ＝ W-P.005 §二 7。
  - 0 m：分配地 29、抵費地 6、公設 5；地號 1〜40（R3-01→13 … R3-07→19、G1→40）⇒ ＝ W-P.005 §二 7。
  - 重劃後地價三值 68621.38、72433.68、76245.98。
- `check_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json 0 3.5`（約 56 秒）⇒ V0〜V8 於 0 m、3.5 m 皆 PASS，「全過（18/18）」，結束碼 0。
- 註記之抽驗（3.5 m·`公告分配地籍線` 圖層讀回）：地號 5 ＝ `5`、`638.61`、`寬19.46`、`深33.26`；地號 4 ＝ `4`、`741.92`、`寬22.22`、`深33.50` ⇒ ＝ §二 7。
- 照舊之檢查（主線合併後）：`check_W-P001.py` ⇒ 12/12 通過；`check_W-P002.py`（`synth_W-P002a.py` 出示範附表 26）⇒ 8/8 PASS（Q6 分頁符 [43, 83]）·結束碼 0；`appx_tables.py`＋`check_W-P003.py` ⇒ 8/8；`burden_tables.py`＋`check_W-P004.py` ⇒ 8/8。

## 工項 4　故意錯誤之測

`mutate_W-P005.py`（3 分 05 秒·結束碼 0·末行「合」）：

| 變異 | 結果 | 所紅之項 |
|---|---|---|
| 成果 | 綠 | — |
| Ⓐ 公告分配地籍線漏一宗 | 紅 | V2、V3、V4、V5、V6、V7（@3.5） |
| Ⓑ 二宗同號 | 紅 | V3、V4 |
| Ⓒ S 型不交替 | 紅 | V4 |
| Ⓓ 歸戶之色錯位 | 紅 | V5 |
| Ⓔ 重劃後地價圖用重劃前地價 | 紅 | V6 |
| Ⓕ 寬仍註 W 而非 S | 紅 | V3 |
| Ⓖ 街角第 1 宗之深未納道路截角 | 紅 | V3 |
| Ⓗ 深以 S 除而非 W | 紅 | V3 |
| Ⓘ 街角第 1 宗之 W 用截角後之寬 | 紅 | V8 |

⇒ 皆 ＝ §二 7 之所期。

## 工項 5　對照組與其餘輸出⛔ 變

- `<C>` 複 `<O>` 之二配地結果；以 `9deaad2` 之 `plots/`（`git worktree`·用畢即除）之 `post_maps.py` 出圖。
- (a) 附錄甲於 `<C>` ⇒ 結束碼 1，「不過 ['V3@0', 'V3@3.5']（16/18）」——**唯 V3 紅**。例：3.5 m「628-36(1) 之註記 ['5', '638.61', '寬19.40', '深32.92'] ≠ ['5', '638.61', '寬19.46', '深33.26']」；0 m「628-37(1) 之註記 ['5', '272.82', '寬8.40', '深32.48'] ≠ ['5', '272.82', '寬8.43', '深33.28']」。
- (b) 附錄辛（倉外·第 2 列之路徑改為 `/tmp/w/verify/plots/check_W-P005.py`·餘未改）：
  - 3.5 m：「非寬深之圖元 576 同 寬深之文字 56 56」；地號對照表、顏色對照表皆「同」。
  - 0 m：「非寬深之圖元 583 同 寬深之文字 58 58」；地號對照表、顏色對照表皆「同」。
  ⇒ ＝ 原型。

## 工項 6　差異閘

- `git diff --name-status 9fd34275770b7fc53103b9eb42ba21925f823f9a 351e8548b88bf58993966f59bda6b821ae573d6b` ⇒ 32 列，**皆**在 `plots/`、`verify/plots/`、`docs/出圖/` 之下（他處 0 列）⇒ 綠。
- `git diff --name-status 9deaad2 351e8548 -- plots verify/plots docs/出圖` ⇒ 唯 `M plots/alloc_state.py`、`M plots/post_maps.py`、`M verify/plots/check_W-P005.py`、`M verify/plots/mutate_W-P005.py`、`A verify/plots/preview_W-P005a.py`、`A docs/出圖/W-P.005_補令一_寬深之註記.md` ⇒ 合。
- 對照組：拋棄式之複本於側支之端改 `app.py` 一列並 commit ⇒ 差異閘列出 `app.py` ⇒ **紅**（非恆綠）；複本已刪。

## 工項 7　預覽 PNG（入 `出圖線/成果/`）

- `W-P.005_重劃後三圖層_退縮0m.png`（648806 bytes·覆舊）、`W-P.005_重劃後三圖層_退縮3.5m.png`（641757 bytes·覆舊）
- `W-P.005_補令一_街角宗之寬深_退縮0m.png`（329059 bytes）、`W-P.005_補令一_街角宗之寬深_退縮3.5m.png`（335731 bytes）
- 目視（3.5 m 街角圖）：八宗各見紅斜線之截角三角形於理論角；各宗之「寬」為 S、「深」之式與標題之式一致。另見：R4 左（地號 19）之四列註記於縮圖中略相疊——唯預覽之排版，⛔ 屬單之事，僅記之。

## 工項 8　快轉 `wip/plots`

- `wip/plots`：`9deaad28ca37bd24c4c02ddc86d65da3b7a9d574` → `351e8548b88bf58993966f59bda6b821ae573d6b`（快轉·⛔ `--force`）；`verify/W-P.005a-width-depth` ＝ `351e8548`（新建）。

## 自捕與自解

- 無。（`echo rc=$?` 曾取到管線末之 `tail` 之碼，改以先存記錄檔再取碼，所記之結束碼皆為程式本身者。）

## 須核心線辦理

- 無新增。
