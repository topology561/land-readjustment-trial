# W-P.005 回報（出圖線·執行端）

- **單**：`出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md`（71084 bytes·sha256 `710a0b9b1324a0e24a9b309349c45e94eadf17d2776389905bba683fc5fe3659` 相符）
- **結果**：完成
- **許可**：`分支許可.md` N＝393；核心線 `order` ＝ `W-G.9-398_補令三`（398 ≥ 393）
- **耗時**：接單 01:49 → 回報約 02:12（Asia/Taipei·2026-10-29）；其中 `alloc_state` 8 分 39 秒

## 工項 1　與主線同步

- 側支 `verify/W-P.005-post-maps` 自 `origin/wip/plots` ＝ `9a3cb61bd5397ecaca62ca30b5c32d57a03b8fd8` 出。
- `git merge --no-edit origin/wip/s1-endpart`（主線 ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`）⇒ 無衝突，合併之 commit `6b6231a667a7af2617c7dab3c8cf6c0ee7106b26`。

## 工項 2　程式（附錄逐位元組）

| 附錄 | 檔 | bytes | sha256 |
|---|---|---|---|
| 甲 | `verify/plots/check_W-P005.py` | 20390 | `2927307e…fe06` 相符 |
| 乙 | `verify/plots/mutate_W-P005.py` | 5077 | `6f19c48d…1db2` 相符 |
| 丙 | `verify/plots/preview_W-P005.py` | 4581 | `2d0bc1c5…ee66` 相符 |
| 丁 | `plots/alloc_state.py` | 6807 | `e91241e9…21ab` 相符 |
| 戊 | `plots/post_maps.py` | 17742 | `f8e4ac41…bdf34` 相符 |
| 己 | `docs/出圖/W-P.005_重劃後三圖層與地號對照表.md` | 3005 | `9dfeb30a…41ca8` 相符 |

- 五 `.py` 之 `python -m py_compile` 皆過。
- commit `9deaad28ca37bd24c4c02ddc86d65da3b7a9d574`（「W-P.005：重劃後三圖層…＋暫編→正式地號對照表」）。

## 工項 3　量測（venv：`python3 -m venv --system-site-packages`＋`pip install -r requirements.txt 'numpy<2.3'` ⇒ numpy 2.2.6·倉外）

- `fetch_moedict.py` ⇒ `dict-revised.json` 63298941 bytes·sha256 `f68fc3df…a7ad` 合。
- `prelim_maps.py --out <P> --moedict` ⇒ 出五檔（重劃前圖.dxf、顏色對照表、附表 02、03、26）。
- `alloc_state.py --out <O> --setback 0 --setback 3.5`（8 分 39 秒·結束碼 0）：
  ```
  退縮 0 m：宗 35（分配地 29、抵費地 6）；略 ['R1-抵費地-2']
  退縮 3.5 m：宗 34（分配地 28、抵費地 6）；略 ['R1-抵費地-2']
  ```
  ＝ §二 7。
- `post_maps.py`（二退縮·結束碼皆 0）：
  - 3.5 m：分配地 28、抵費地 6、公設 5；地號 R1-05→1 … R1-01→5、R2-01→6 … R2-07→12、R3-01→13 … R3-06→18、R4-01→19 … R4-03→21、R5-07→22 … R5-01→28、R6-06→29 … R6-01→34、RD1→35、RD2→36、RD4→37、RD3→38、G1→39 ⇒ **逐項 ＝ §二 7**。
  - 0 m：分配地 29、抵費地 6、公設 5；地號 1〜40（R3-01→13 … R3-07→19，其後各號 +1；G1→40）⇒ ＝ §二 7（R3 有 7 宗）。
  - 重劃後地價三值 68621.38、72433.68、76245.98（R1、R4＝76245.98；R2、R6＝68621.38；R3、R5＝72433.68）＝ §二 7。
- `check_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json 0 3.5`（約 61 秒）⇒ V0〜V7 於 0 m、3.5 m 皆 PASS，「全過（16/16）」，結束碼 0。
- 既有之輸出未受擾（主線合併後）：
  - `check_W-P001.py` ⇒ 12/12 通過
  - `check_W-P002.py`（`synth_W-P002a.py` 出示範附表 26）⇒ 8/8 PASS（Q6 分頁符 [43, 83]）·結束碼 0
  - `appx_tables.py` ＋ `check_W-P003.py` ⇒ 8/8（Σ面積 22803.33、Σ總價 1643176255.06）
  - `burden_tables.py` ＋ `check_W-P004.py` ⇒ 8/8（上漲率 1.871619；B 0.171043、C 0.091319）

## 工項 4　故意錯誤之測

`mutate_W-P005.py`（約 84 秒·結束碼 0·末行「合」）：

| 變異 | 結果 | 所紅之項 |
|---|---|---|
| 成果 | 綠 | — |
| Ⓐ 公告分配地籍線漏一宗 | 紅 | V2、V3、V4、V5、V6、V7（@3.5） |
| Ⓑ 二宗同號 | 紅 | V3、V4 |
| Ⓒ S 型不交替 | 紅 | V4 |
| Ⓓ 歸戶之色錯位 | 紅 | V5 |
| Ⓔ 重劃後地價圖用重劃前地價 | 紅 | V6 |

＝ §二 7 之原型所記。

## 工項 5　差異閘

- `git diff --name-status bd7da4d 9deaad2` ⇒ 30 列，皆 `A`，皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下 ⇒ **綠**。
- `git diff --name-status 9a3cb61 9deaad2 -- plots verify/plots docs/出圖` ⇒ 唯 §二 之六新檔（皆 `A`）。
- 對照組（拋棄式複本改 `app.py` 首行一字並 commit）⇒ 31 列，不合 `M app.py` ⇒ **紅**。

## 工項 6　預覽 PNG（入 `出圖線/成果/`）

- `W-P.005_重劃後三圖層_退縮0m.png`（648687 bytes·sha256 `60518eee…51ba`）
- `W-P.005_重劃後三圖層_退縮3.5m.png`（641527 bytes·sha256 `f09dd428…9873`）
- 二者與 `出圖線/待KL/W-P.005_原型預覽_退縮{0m,3.5m}.png` 逐位元組同（`cmp`）。

## 工項 7　推送與快轉

- `verify/W-P.005-post-maps`：新建 ⇒ `9deaad28ca37bd24c4c02ddc86d65da3b7a9d574`
- `wip/plots`：`9a3cb61bd5397ecaca62ca30b5c32d57a03b8fd8` → `9deaad28ca37bd24c4c02ddc86d65da3b7a9d574`（快轉·未 `--force`；推前驗 `9a3cb61` 為其祖）
- `git ls-remote` 實測二分支皆 ＝ `9deaad2`；主線 `wip/s1-endpart` 仍 `bd7da4d`。

## 自捕與自解

1. **`.gitignore` 之 `*對照表*` 涵蓋附錄己之檔名**（`docs/出圖/W-P.005_重劃後三圖層與地號對照表.md`）：一般之 `git add` 會略過之。以 `git add -f` 加入該一檔（⛔ 改 `.gitignore` 或他檔）；差異閘證其為 `A` 且唯六新檔。輸出檔（`地號對照表_*.xlsx` 等）照舊不入倉。請發單端復核此法；其後之單之檔名含「對照表」者同此。
2. 無他。

## 須核心線辦理

無新增（numpy 版本之事同 §二 7·唯於倉外之 venv）。
