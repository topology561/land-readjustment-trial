# W-B 細部 plan：街角規定範圍構造（SIDE_LINE 中點垂線平移法）

> 給 Claude Code。依 CLAUDE.md 與 docs/配地計算總規格_v3.md 第四節。
> **開新對話、模型 Sonnet。** 套用前先盤點回報 KL、確認後動工。
> 套用後 py_compile + grep 驗證 + 異動清單 + commit/push。
> 行號基於 app.py（W-A.2 後版，約 16,300 行），實際以 grep 為準。

## W-B 目標

把街角規定範圍從「憑空鋪矩形」改成 v3 第四節定稿的「SIDE_LINE 中點垂線平移」
五邊形構造法，使其與 DXF 預埋的 R5 左側 146.50㎡ 對齊。
這是 W-D 街角評點、W-C 遞進解 G 的幾何地基。

舊構造法（`_build_corner_polygon_B4`，line ~7806）整個廢除。

## 三個前置盤點（動工前回報 KL）

1. `_cad_layers`（line ~11888 寫 side_lengths 入 session 處）的對外變數名確認。
2. `classified_blocks` 元素取多邊形：用 `b.get('vertices')`（line 1213 已見此用法）
   建 shapely Polygon、`.centroid` 取質心。確認街角函式內可取到 classified_blocks
   或等價的「該街廓 vertices」。
3. 街廓分類欄位 key（住宅區/商業區判定），與 W-A 一致確認。

> 註：本 plan 採 KL 定案的「FRONT_LINE 方向約定」（p1=左、p2=右）自動判定
> 左右側街角，廢除舊複雜配對演算法。詳見 §1。

---

## §1 左右側判定：改用 FRONT_LINE 方向約定（取代複雜配對演算法）

### 繪圖規範（已正式定為系統規範，寫入 CAD SOP）

**FRONT_LINE 起點(p1) = 街廓左側、迄點(p2) = 街廓右側。**
SIDE_LINE 的一個端點會與 FRONT_LINE 的 p1 或 p2 重合（該點正面側面皆臨路 = 街角）：
- SIDE_LINE 端點接 FRONT_LINE p1 → 該 SIDE_LINE 屬**左側**街角
- 接 p2 → **右側**街角
- FRONT_LINE 某端無 SIDE_LINE 相接 → 該側非街角（單側街角）
- p1、p2 各有 SIDE_LINE 相接 → 雙側街角
道路截角斜邊正對的頂點 = FRONT_LINE × SIDE_LINE 交點。

### 現況可用資料

`result['front_lines'][blk]` 已存 `{'p1','p2','angle_deg','length'}`（line ~1371），
方向完整保留。`_side_line_buffer[li]['pts']` 有 SIDE_LINE 座標。

### 1-1. 廢除舊配對演算法，改用方向約定

廢除 line ~1399-1542 的「階段 1-4 配對 + swap 校正」整段
（`_line_best_block`、cross product 分左右、極角差異、`_corner_marks_by_block`、
swap log 等）。改為：

```python
# 🚨 W-B：以 FRONT_LINE 方向約定判定 SIDE_LINE 左右側
result.setdefault('side_lines_by_side', {})
TOL = 0.5  # 端點重合容差（m），1/500 圖解區
for _li, sl in enumerate(_side_line_buffer):
    _spts = sl.get('pts') or []
    if len(_spts) < 2:
        continue
    _s_ends = [(_spts[0][0], _spts[0][1]), (_spts[-1][0], _spts[-1][1])]
    # 對每個可建築街廓的 FRONT_LINE，看此 SIDE_LINE 哪端接到 p1/p2
    for _blk, _fl in result['front_lines'].items():
        _p1 = _fl['p1']; _p2 = _fl['p2']
        _hit = None
        for _se in _s_ends:
            if _dist(_se, _p1) < TOL: _hit = 'left'; break
            if _dist(_se, _p2) < TOL: _hit = 'right'; break
        if _hit:
            result['side_lines_by_side'].setdefault(_blk, {})[_hit] = {
                'p1': (float(_spts[0][0]), float(_spts[0][1])),
                'p2': (float(_spts[-1][0]), float(_spts[-1][1])),
                'mid': (float(sl['mid_x']), float(sl['mid_y'])),
                'length': float(sl['length']),
            }
            break
```
`_dist` = 兩點歐氏距離。side_lengths_by_side 仍可同步由此填（length 欄）。
方向約定直接定左右側，**不再需要 swap 校正**（swap 是舊配對的補丁，一併廢除）。

### 1-1b. 端點吻合一致性警示（防呆，KL 要求）

繪圖未遵守約定（SIDE_LINE 端點沒接到任一 FRONT_LINE 端點）時，自動判定會失靈。
對每條 SIDE_LINE，若其兩端到所有 FRONT_LINE 的 p1/p2 最近距離都 > TOL：
```python
st.warning(f"⚠️ SIDE_LINE（中點 {mid}）兩端均未接到任何 FRONT_LINE 端點"
           f"（最近 {dmin:.2f}m > {TOL}m）——可能繪圖未遵守『SIDE_LINE 端點接 "
           f"FRONT_LINE 端點』規範，左右側街角判定可能失準，請檢查 DXF 或於街角"
           f"側別覆寫處手動指定。")
```
收集所有未吻合的 SIDE_LINE 列成清單供 UI 顯示。

### 1-2. 寫入 session（line ~11888 同區塊）

```python
st.session_state['f3_cad_side_lines_by_side'] = _cad_layers.get('side_lines_by_side', {})
```

### 1-3. 讀「宗地分配線」圖層（v3.1 新增，W-B 補做）

W-A.3 圖層盤點未含此新圖層，W-B 補讀。宗地分配線定義該街廓所有地界線方向。
解析（類似 SIDE_LINE 讀法，在 parse 階段）：
```python
# 讀宗地分配線圖層（圖層名待 §0 盤點確認，暫定 '宗地分配線' / 'ALLOC_LINE'）
# 每條宗地分配線 → 取方向單位向量，歸屬到所在/最近的可建築街廓
result.setdefault('alloc_dir_by_block', {})
for 線 in 宗地分配線圖層:
    p_start, p_end = 線兩端點
    ux, uy = 單位向量(p_end - p_start)
    blk = 線所在的可建築街廓（用中點落在哪個 BLOCK 判定）
    result['alloc_dir_by_block'][blk] = (ux, uy)   # 只存方向，位置不取
```
寫入 session：`st.session_state['f3_cad_alloc_dir'] = _cad_layers.get('alloc_dir_by_block', {})`
- 每可建築街廓應有一條宗地分配線；若某街廓缺 → 警示「街廓 X 缺宗地分配線，
  無法定地界線方向」。
- 方向正負無所謂（線段兩端哪頭畫都行，取的是方向軸）。

> §0 盤點補一項：確認宗地分配線圖層在 DXF 的實際圖層名、以及 V6.dxf 是否已含
>（R1-R6 各一條）。若 V6.dxf 尚無此圖層，需 KL 在 CAD 補畫後重出 DXF 測試。

---

## §2 補 f3_current_pk_block 寫入（零寫入 bug）

`f3_current_pk_block` 全檔僅 line 7788 讀取、零寫入 → 街角構造永遠抓不到當前街廓。
PK 主迴圈 line ~13573 `for _row in _corner_rows_init:` 內、
呼叫 `select_corner_lots_both_sides_v12`（line ~13660）之前，加：
```python
st.session_state['f3_current_pk_block'] = _row.get('街廓') or _row.get('label') or ''
```
確認 `_row` 內街廓 label 的實際 key（grep `_corner_rows_init.append` line ~13513 看欄位名）。

---

## §3 新構造函式 `_build_corner_range_v2`（取代 _build_corner_polygon_B4）

廢除 line ~7806 的 `_build_corner_polygon_B4` 整個 def 與其 ref_inside_point 邏輯。
新建：

```python
def _build_corner_range_v2(side_mid, block_vertices, block_centroid,
                            alloc_dir, shift_distance, chamfer_tri=None):
    """🚨 W-B：街角規定範圍 = SIDE_LINE 中點沿宗地分配線方向平移 ∩ BLOCK，扣道路截角

    side_mid        : SIDE_LINE 中點 (x,y)
    block_vertices  : 該可建築街廓 BLOCK 頂點 [(x,y),...]
    block_centroid  : BLOCK 質心 (x,y)，定平移正負（朝質心側=可建築側）
    alloc_dir       : 宗地分配線方向單位向量 (ux,uy)（見 §1-3 讀取）
    shift_distance  : 退縮 + 畸零地最小寬
    chamfer_tri     : 道路截角三角形 shapely Polygon（可None）
    回傳：街角規定範圍 shapely Polygon 或 None
    """
```

實作要點（對應 v3.1 第四節五步，基準改宗地分配線方向）：
1. 建 `block_poly = Polygon(block_vertices)`（無效則 buffer(0)）。
2. **平移方向（宗地分配線方向的法向，v3.1 定案）**：
   宗地分配線方向 = 地界線方向（該街廓所有地界線平行它）。街角範圍的平移線
   **平行宗地分配線**、往可建築側平移；平移量沿其法向量（= W_eval 深度方向）。
   ```python
   ux, uy = alloc_dir                  # 宗地分配線（地界線）方向單位向量
   nx, ny = -uy, ux                    # 宗地分配線法向（平移深度方向）
   # 以質心定正負：法向應指向可建築側
   test = (side_mid[0] + nx, side_mid[1] + ny)
   if _dist(test, block_centroid) > _dist((side_mid[0]-nx, side_mid[1]-ny), block_centroid):
       nx, ny = -nx, -ny
   shifted_pt = (side_mid[0] + nx*shift_distance, side_mid[1] + ny*shift_distance)
   ```
   （不再用 FRONT_LINE 的 d_hat 法向——弧形街廓 FRONT_LINE/BASELINE 彎曲、
    無唯一法向；宗地分配線是使用者畫的固定方向，是地界線方向的唯一基準，見 v3.1 概念 5。）
3. **平移線**：過 shifted_pt、方向 = 宗地分配線方向 (ux,uy)，
   往兩端延長 ≥ block bbox 對角線，確保穿越 BLOCK。
4. **切 BLOCK 取靠 SIDE_LINE 側**：
   ```python
   from shapely.ops import split
   pieces = split(block_poly, shifted_line)
   target = min(pieces.geoms, key=lambda g: g.centroid.distance(Point(side_mid)))
   ```
5. **扣道路截角**：`if chamfer_tri: target = target.difference(chamfer_tri)`
   （chamfer_tri 來源見 §4；無則跳過，標記面積未扣截角）。
6. 回傳 target（buffer(0) 修正、空則 None）。

> split 失敗 fallback：用平移線與 block_poly.exterior 的 2 交點連線 +
>  靠 SIDE_LINE 側的 BLOCK 邊頂點手動組 polygon。

---

## §4 道路截角三角形（W-B 當場扣，KL 定案）

道路截角斜邊 = FRONT_LINE 與 SIDE_LINE 被截角切斷後兩端點連線（v3 六-2）。
截角三角形 = 斜邊兩端點 + FRONT_LINE×SIDE_LINE 理論尖角點 圍成。

**來源**：DXF 無專屬截角圖層，但 `geom_restore['theoretical_corners']` 現成可推。
**W-B 當場扣截角**（不延後）——理由：材料現成；驗收基準 146.50 是扣截角後的值，
當場扣才能直接對拍、不必換算；不留「未扣截角」尾巴汙染 W-C/W-D。

### 動工前盤點（唯一須回報 KL 的 §4 事項）

先印出 `geom_restore['theoretical_corners']` 的實際結構（key、每個值是什麼點），
判定它存的是：
- (a) 理論尖角點（無截角時 FRONT×SIDE 交點）→ 斜邊兩端從 BLOCK 街角轉角頂點取。
- (b) 截角斜邊兩端點 → 尖角點從 FRONT_LINE/SIDE_LINE 延伸求交。
- (c) 兩者都有 → 直接組三角形。
回報結構後，依實際情形組 chamfer_tri，再傳入 `_build_corner_range_v2`：
```python
target = target.difference(chamfer_tri)
```
扣截角後四邊形 → 五邊形，面積應 ≈ 146.50㎡。

---

## §5 改呼叫處（line ~7862）

廢除 `_corner_poly_p1_B4 / _corner_poly_p2_B4` 兩次舊呼叫，改為按 SIDE_LINE
左右側各建一次：
```python
_slbs = _st_B4.session_state.get('f3_cad_side_lines_by_side', {}) or {}
_adir = _st_B4.session_state.get('f3_cad_alloc_dir', {}) or {}
_this_blk = _st_B4.session_state.get('f3_current_pk_block', '')
_side_this = _slbs.get(_this_blk, {})
_alloc_this = _adir.get(_this_blk)         # 該街廓宗地分配線方向 (ux,uy)
_shift_B = _setback_B4 + _legal_min_width_B4
# 取 block vertices + centroid（從 classified_blocks 找 label==_this_blk）
... 建 _blk_verts, _blk_cen ...
if _alloc_this is None:
    _st_B4.warning(f"街廓 {_this_blk} 缺宗地分配線，街角範圍無法構造")
_corner_range_left = None; _corner_range_right = None
if 'left' in _side_this and _alloc_this:
    _corner_range_left = _build_corner_range_v2(
        _side_this['left']['mid'], _blk_verts, _blk_cen, _alloc_this, _shift_B, _chamfer_left)
if 'right' in _side_this and _alloc_this:
    _corner_range_right = _build_corner_range_v2(
        _side_this['right']['mid'], _blk_verts, _blk_cen, _alloc_this, _shift_B, _chamfer_right)
```
下游交集判定（line ~7866 起 `_corner_inter_area_p1/p2`）的
`_corner_poly_p1_B4 / p2` 換成 `_corner_range_left / right`。

**p1/p2 端 與 left/right 側的對應（已由 §1 方向約定解決）**：
現行 front_line p1/p2 端分流，現在 p1=左、p2=右是繪圖規範定義，
直接對應 `_corner_range_left / right`，**不需再盤點猜測**。
全面改用 left/right 命名，移除 p1/p2 混用。

## §7 街角左右側點選功能：降級為「保險絲 + 驗證顯示」（KL 定案）

方向約定成為主判定後，原人工點選左右側功能不刪除，改為兩個角色：

7-1. **驗證顯示**：自動判定後，圖面標註各街廓判定結果
（「左側街角／右側街角／雙側街角」），供使用者一眼確認。

7-2. **覆寫保險**：保留手動翻轉左右側的入口。當 §1-1b 警示觸發
（繪圖未遵守約定）、或使用者發現判定錯誤時，可手動指定/翻轉，
不必回 CAD 重畫。手動覆寫後寫入 `f3_cad_side_manual_override`，
§1 自動判定讀此覆寫優先。

平常使用者不需點選（自動判定）；僅在警示或判定錯誤時才介入。

---

## §6 UI 對拍表（驗收用）

街角 PK 結果區加 expander，列各街廓各側街角規定範圍面積：
```python
with st.expander("📐 街角規定範圍面積（W-B SIDE_LINE 中點垂線構造）", expanded=False):
    # 每街廓 left/right：面積、平移量、是否扣截角
    # R5 左側預期 ≈ 146.50㎡（DXF R5左側街角地最小面積 圖層）
```

---

## 驗收（冷啟動：停 app → 重啟 → 新分頁 → Tab1 匯入 → Tab4 重跑步驟C → 跑街角PK）

| 驗收點 | 預期 |
|---|---|
| py_compile | 通過 |
| 舊函式清除 | grep `_build_corner_polygon_B4` 無結果；舊配對演算法（`_line_best_block`、`_corner_marks_by_block`、swap log）無結果 |
| 新函式 | grep `_build_corner_range_v2` 有 def + 呼叫 |
| SIDE_LINE 座標 | `f3_cad_side_lines_by_side` 有值、每街廓 left/right 含 p1/p2/mid |
| 左右側判定 | 依 FRONT_LINE p1=左/p2=右 約定；雙街角街廓 left/right 皆有、單街角僅一側 |
| 端點吻合警示 | 故意把某條 FRONT_LINE 反向繪製測試 → 觸發警示或左右判反（驗證防呆有效）|
| f3_current_pk_block | PK 時有值（非空字串）|
| **R5 左側街角範圍面積** | 扣截角後 ≈ 146.50㎡（未扣截角則略大、標記）|
| 退縮 0m 左右對稱 | 不再出現某街廓單側「達資格 0 筆」（除非真無候選）|
| 628-7(2) 是否仍為 R5 左側 winner | 對拍——若改變，回報 KL 判斷是否幾何修正使然 |

驗收通過、回報 R5 左側街角範圍實際面積數字後，進 W-C（遞進解 G + Rw 累積）。

## 紀律
- `_build_corner_polygon_B4` 與舊 SIDE_LINE 配對演算法（階段 1-4 + swap）整段刪、不留 fallback。
- §3 平移方向用**宗地分配線方向的法向**（=地界線方向，使用者畫的固定方向）+ 質心定正負。
  不再用 FRONT_LINE d_hat 法向（弧形街廓無唯一法向）。見 v3.1 概念 5、第四節。
- §1-3 補讀宗地分配線圖層：動工前 §0 盤點確認圖層名、V6.dxf 是否已含
  （R1-R6 各一條）；若無，KL 需在 CAD 補畫後重出 DXF。
- §4 截角：動工前先印 `geom_restore['theoretical_corners']` 結構、回報 KL，
  確認建法後當場扣截角，不留「未扣截角」尾巴。
- 點選功能降級為保險絲，勿刪除（§7）。
- 守恆式不受 W-B 影響（W-B 只動街角範圍幾何，不動面積分配）。

## 動工前 §0 盤點（回報 KL 再動工）
1. 宗地分配線圖層在 DXF 的實際圖層名；V6.dxf 是否已含（R1-R6 各一條）。
   ← **這是 W-B 能否驗收的前提**：無宗地分配線則街角範圍無法構造。
2. `geom_restore['theoretical_corners']` 結構（§4 截角建法）。
3. classified_blocks 取 vertices/centroid 的方法、街廓 label 對應。
