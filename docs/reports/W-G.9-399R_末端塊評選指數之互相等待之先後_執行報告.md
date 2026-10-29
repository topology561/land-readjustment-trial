# `W-G.9-399R` 末端塊評選指數之互相等待之先後——執行報告（規格單 ＋ 補令一 ＋ 補令二）

> 執行端（CC·雲端）·`2026-10-29`〜`30`（Asia/Taipei）·effort=high。受單 ＝ `ops/queue` 之 `orders/W-G.9-399_補令二.md`（`75373` B·`sha256` `d7199ace80a0b7e833487a360bdae374eb1608759a32b3e110a232e09d17ce42` ＝ `STATE.json`·`SELF_SHA256` `def7ecd2a031f07c549ec6b246748a1e5e092086ddc92478398f92a52c53b2a5` 依 `P-5` 自驗合）。
> 前趟：原單 `W-G.9-399_規格單`（停機款 `12`·`ops/queue` 之 `reports/W-G.9-399_規格單_回報.md`）；補令一（停機款 `12″`·`reports/W-G.9-399_補令一_回報.md`·其差異 `reports/W-G.9-399_補令一_回報_app.diff`）。本趟（補令二）：**完成**·本案配地⛔ 變；主線 `wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`（⛔ 動）。
> 收工閘之實測值出艙於 `ops/queue` 之 `reports/W-G.9-399_補令二_回報.md`（⛔ 寫入本檔·自指）。`<O>` ＝ `/tmp/claude-0/-home-user-land-readjustment-trial/fc9017ca-1ce2-5e31-ba5f-d185f5a0defe/scratchpad/o399p2`（倉外·容器暫存）。

## ① 逐 `commit` 之 hash 與工項（新側支 `verify/W-G.9-399-k960x`·皆快轉）

| 單 | 工項 | `commit` | 內容（增／刪） |
|---|---|---|---|
| 原單 | 零 | `6b159e2` | 原單入倉（前趟） |
| 原單 | 一 | `23f3fc8` | 塊 `Fy57` 之 `16` 器（前趟） |
| 補令一 | 零″ | `31887d94b981e162842b2547de3b9b2e050059ab` | 補令一入倉（前趟） |
| 補令一 | 一″ | `1612750ff6291af48a98f46a44667e414af06968` | 塊 `Fy58`（前趟） |
| 補令二 | 零‴ | `bfdba99f8739a66ae2239dd3368e810ec5077d92` | `docs/orders/W-G.9-399_補令二.md` `418`／`0`（blob 之 `sha256` ＝ `d7199ace…`） |
| 補令二 | 一‴ | `9e0eeb1040aa29c4563d2a816d45ac8aa2b4b58a` | `verify/probes/probe_WG9399_k960x.py` `36`／`0`（blob `63a196f805334d1e193e05545c2a4e1b2f8c5006`·`51657` B） |
| 補令二 | 二‴ | `0c35403cf144cff9627e80c9309d94fb2f169a17` | `app.py` `373`／`14`（對 `9e0eeb1`）·blob **`101a7a6a860522dd24b460e54aa8af48de84badd`**（`1929211` B）；對 `<O>/app_R0.py`（`1158f83e…`）`18`／`4` |
| 補令二 | 三‴ | `4c77eee3629e9231b28d9699cafe3bec344c6af5` | `K-6` 典 `154`／`0`、`待落地清單.md` `45`／`0`、自誤簿 `26`／`0` |
| 補令二 | 四‴ | （本檔所在之 `commit`） | 本報告 ＋ `W-G.9-399R_末端塊評選指數之互相等待之先後_差異.diff` |

原單之工項二（`915bcd1`）與補令一之工項二″（`7f7ad7c`）皆⛔ 推（其停機）；本趟之工項二‴ ＝ 補令一之原趟之差異之重施（`R-0‴`）＋ `R-1‴`、`R-2‴`。

## ② 停機款之三值

### 補令二之 `1‴`〜`13‴`

| # | 期 | 實 |
|---|---|---|
| `1‴` | 主線 `bd7da4d`、新側支 `1612750`、heads（濾後）`57`；追蹤檔無變動；`§零-0‴` 項 `3` `rc 0` 與四簿；旗標 `[None×5]`；環境可匯入 | 皆合：`bd7da4d…`、`1612750…`、`57`（`<O>/heads_before_399p2.txt`）；`status` 空；`app.py` `ca9f917e…`、`F42` `a9a34667…`；`rc 0`·自誤 `629`／`644`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；`[None, None, None, None, None]`；裝後匯入 `rc 0` |
| `2‴` | `SELF_SHA256`、bytes／`sha256`、入倉之 blob | 皆合（`def7ecd2…`；`75373`／`d7199ace…`；`git cat-file blob HEAD:docs/orders/W-G.9-399_補令二.md` 之 `sha256` ＝ `d7199ace…`） |
| `3‴` | 塊與 `rep399p1.diff` 之 bytes／`sha256`／列數；`apply --check`；施後 blob | 皆合：`Fy59` `5109`／`b3f64ace…`／`61`；`K50` `6894`／`826d46ae…`／`37`；`P61` `2513`／`c099e82e…`／`14`；`E47` `2897`／`08cda66d…`／`13`；`K48` `15358`／`1a1f8a17…`／`72`；`P59` `2902`／`c533677d…`／`16`；`K49` `9098`／`1e9a151f…`／`45`；`P60` `2930`／`d5bdb8fe…`／`15`；`E46` `3386`／`591ec9a0…`／`13`；`rep399p1.diff` `40810`／`16c561ff…`／`509`（補令一之回報 `56195`／`69fa76ca…`）；`Fy59`、`rep399p1.diff` 之 `--check` 皆過；`F42` ＝ `63a196f8…`；`R-0‴` 施後 ＝ `1158f83e060600a71bd9ff28c66d7ebdb9d6aa16` |
| `4‴` | 前置‴ 之期 | 皆合（③） |
| `5‴` | 規格無歧義而涉域；⛔ 須改禁改 | 撰碼中未遇 |
| `6‴` | `V-1‴`〜`V-9‴` 皆合；本案配地⛔ 變 | 皆合（③）；本案配地⛔ 變 |
| `7‴` | 推之目標唯新側支／`ops/queue`；⛔ 被拒；主線⛔ 推進 | 合（四推皆至新側支·快轉；主線 `bd7da4d`） |
| `8‴` | 工項三‴ 之三檔與 `checkidx`／`gen_fa_index` | 合（④、⑨） |
| `9‴` | 收工閘 | 見回報（自指） |
| `10‴` | ⛔ 自判正典、⛔ 改塊／器／命令 | 合 |
| `11‴` | 新檔⛔ 為 `check-ignore` 所命中 | 合（本補令 `rc 1`） |
| `12‴` | 唯讀獨立審查之發現⛔ 涉域上判斷或規格之漏載 | 合（總判 PASS·(b) 類 `0`·⑥） |
| `13‴` | 存取⛔ 被拒；寫入⛔ 為分類器所拒 | 合 |

### 補令一之 `1″`〜`13″`、原單之 `1`〜`13`

前趟之停機：原單 ⇒ 款 `12`（唯讀審查之 W-1〜W-5）；補令一 ⇒ 款 `12″`（WARNING-1·其回報之 ⑥）。本趟於補令二之下續之：其餘之款之受詞皆由補令二之同號之款代之（補令二單首「原單之 `§三`〜`§五` 與補令一之 `§三″`〜`§五″` 除本補令明改者外照舊適用」），其實值見上表；未成就者無。

## ③ 前置‴ 與驗之出艙

### ③-0 開場（`§零-0‴`）

- `nproc` ＝ `4`；context 餘量約 `14.9` M tokens。
- 環境：初無 `shapely`（匯入 `rc 1`·`pip freeze` `7eef2a92…`）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ `9ad34edc…`（異於基準）⇒ 原單 `§零-0` 項 `5` 之命令逐字釘回（`rc 0`）＋ `pip uninstall -y tzdata`（`rc 0`）⇒ **`ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`** ＝ 基準；`Python 3.11.17` ＝ 基準；匯入 `rc 0`。
- pre-flight（`1612750` 之器·`rc 0`）：🔴 `0`；🟡 `1`（`P-4` `:191`·`§五‴` 項 `9` 所具名豁免）；ℹ️ `P-5` ✅（受詞 `75295` B）、`P-3` ＝ `24044`–`31788`（＝ 項 `9`）。
- 取號：`自誤 646` `0` 檔、`自誤 645` `1`；`Fy59`／`P61`／`E47` 二框皆 `0`；`` 塊 `K50` `` `0`、`` `K50` `` `4`；對照 `` 塊 `Fy58` ``／`K49`／`P60`／`E46` 各 `1`；追蹤檔 `2948`（皆 ＝ `§零-1‴`）。

### ③-1 前置‴（工項一‴ 之端 `9e0eeb1`·施工樹 `/tmp/w`·殼無 `WV_`）

- **(甲)(乙)**：`51` 呼叫（原單前置 `1` 之 `45` ＋ 前置 `2` 之 `6`）·`21:40:59`→`22:38:27`·並行 `2`（撰碼之自跑之間降為 `1`·下之 ⑥-1）·耗時之和 `6735` s：`rc`／`stderr`／末列 ＝ 期，**不符 `0`**；`#95` ⇒ `rc 1`·末列 ＝ 補令二「項 `8` 之表」之工項一‴ 之端之列（含 `P13`〜`P18`）；`#96` ⇒ `⇒ 紅 ['W1', 'W2', 'W3', 'W4']；rc 1`；`#97` ⇒ `⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`；`stderr` 合計 `0` B；`f8_pre_35.json` ＝ `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、`f8_pre_00.json` ＝ `186b090b68836f0ece2c0d23dad5573941995bf5`。
- **(丙)**：主線之端 ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434` ＝ 基準之 sha；`Python 3.11.17` ＝；`pip freeze` `ae1438da…` ＝ ⇒ **沿用** `基準/bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434.md` 之 `46` 呼叫之值（⛔ 重跑）。
- **項 `4`**：`git diff --name-status 1612750 9e0eeb1` ＝ 恰 `2` 列：`A	"docs/orders/W-G.9-399_\350\243\234\344\273\244\344\272\214.md"`（＝ `docs/orders/W-G.9-399_補令二.md`·工項零‴ 之一筆·有意含之）、`M	verify/probes/probe_WG9399_k960x.py`；`git grep -c -F` 「k960_idx_first」「END_BLOCK_IDX_W_AREA」「end_block_end_geom」 ⇒ 各無出艙、`rc 1`。

### ③-2 驗（工項二‴ `0c35403`·推前·殼無 `WV_`·從頭整套照跑 `97` 呼叫·⛔ 沿用·並行 `2`·`22:39:05`→`00:33:04`·耗時之和 `13598` s·⛔ 容器重啟·⛔ 重跑）

| # | 實 |
|---|---|
| `V-1‴` | `45` 呼叫皆 `rc 0`·末列 ＝ 施後之列；`F42 selftest` `P0 判式自驗 79／79`（`P13`〜`P18` ✅）、`F42 wiring` `W1`〜`W6` ✅、`F42 run` `R1`〜`R3`（二退縮）✅ |
| `V-2‴` | `46` 呼叫皆 `rc 0`·末列 ＝ 施後之列；`F23 selftest` `✅ P0 逐項擾動恰該項紅 75／75` |
| `V-3‴` | 塊 `Fy57` 之 `15` 器之 blob ＝ 原單 `§五-1` 項 `5`（逐一 `hash-object`·`15`／`15`）；`F42` ＝ `63a196f8…`；`verify/probes/` 對 `9e0eeb1` 相異 `0` |
| `V-4‴` | `run`（`#56`、`#57`）皆 `rc 0`；`python3 verify/probes/probe_WG9392_k980g.py diff <O>/pre/k6s3_pre_35.json <O>/post/k6s3_post_35.json` ⇒ `rc 0`·`stderr` `0` B·出艙全文 `全比相異 0 項`；同 `00` ⇒ 同；`… probe_WG9344_k6s3.py cmp <O>/pre/k6s3_pre_35.json <O>/post/k6s3_post_35.json` ⇒ `rc 0`·`stderr` `0` B·出艙全文 `相異 0 項 ⇒ ✅ 同`；同 `00` ⇒ 同（對照組：`diff <O>/pre/k6s3_pre_35.json <O>/pre/k6s3_pre_00.json` ⇒ `全比相異 43 項`）——**本案之配地⛔ 變** |
| `V-5‴` | `parity`（`#60`、`#61`）皆 `rc 0`·`⇒ rc 0（不符 0 項）`；落檔與 `stdout` 對前置‴：以 `<HEAD>` 代 `HEAD` 之全值（前 `9e0eeb1040aa…`、後 `0c35403cf144…`·各恰一見）後**逐位同**（`parity35` `8682` B、`parity00` `284` B、`#60` `1586` B、`#61` `1584` B）；對照：⛔ 代之則四者皆異 |
| `V-6‴` | `run`（`#58`、`#59`）皆 `⇒ 紅 []；rc 0`；`git hash-object` 3.5 m 二列皆 `4aca01db5292d8c55588c7fae7d9f4fa1e217b86`、0 m 二列皆 `186b090b68836f0ece2c0d23dad5573941995bf5` |
| `V-7‴` | 生產碼 `34` 檔對 `9e0eeb1` 相異唯 `M app.py`（`373`／`14`·blob `101a7a6a…`）；`verify/` 相異 `0`；`git diff --no-index <O>/app_R0.py /tmp/w/app.py` 之 hunk 三（下表·皆在 `end_block_pick`·`R-1‴`／`R-2‴`）；ast 頂層節點：對 `app_R0.py` 增減 `0`、相異 ＝ `{end_block_pick}`；對 `bd7da4d` 增恰九（`END_BLOCK_IDX_W_AREA`、`END_BLOCK_IDX_W_LINE`、`END_BLOCK_LINE_TOL`、`end_block_end_geom`、`end_block_end_line`、`end_block_end_segs`、`k960_idx_first`、`k960_idx_key`、`k960_idx_rank`）、減 `0`、相異之既有節點恰六（`end_block_apply`、`end_block_eval_rows`、`end_block_host`、`end_block_merge_run`、`end_block_pick`、`k6b_stage3_run`）＝ 十五 |
| `V-8‴` | 「k960_idx_first」`6`、「END_BLOCK_IDX_W_AREA」`2`、「end_block_end_geom」`7`；`` `W-G.9-399` 補令一 ″ `` `5`；`` `W-G.9-399` 補令二 ‴ `` ⇒ **`2`**（判別力：`<O>/app_R0.py` ⇒ `0`） |
| `V-9‴` | 諸器之 `stderr` 合計 `0` B（`97` 呼叫 ＋ `V-4‴` 之四呼叫） |

| hunk（`app_R0.py` → `app.py`） | 所屬函式 | 條 |
|---|---|---|
| `@@ -11827,6 +11827,7 @@` | `end_block_pick` | `R-1‴`（`unary_union` 之區域之匯入） |
| `@@ -11837,8 +11838,20 @@` | `end_block_pick` | `R-1‴`（多邊形之部、開運算之形、頂點之集）＋ `R-2‴` 之註 |
| `@@ -11853,8 +11866,9 @@` | `end_block_pick` | `R-1‴`（歸屬之判用開運算之形）＋ `R-2‴` 之註 |

`V-7‴` 之 `git diff --no-index` 之全文：

````diff
diff --git a<O>/app_R0.py b/tmp/w/app.py
index 1158f83e..101a7a6a 100644
--- a<O>/app_R0.py
+++ b/tmp/w/app.py
@@ -11827,6 +11827,7 @@ def end_block_pick(side, geom, entries, corner_range_polys, trial, _label='', al
     _got399 = {}
     if _es399:
         from shapely import get_coordinates as _gc399
+        from shapely.ops import unary_union as _uu399
         _cuts399 = []
         for _e399 in entries:
             _cs399 = _e399['tp'].get('polygon_coords') or []
@@ -11837,8 +11838,20 @@ def end_block_pick(side, geom, entries, corner_range_polys, trial, _label='', al
                 _pg399 = _pg399.buffer(0)
             if float(_pg399.intersection(_r_end).area) <= END_BLOCK_CROSS_MIN_AREA:
                 continue
-            _cuts399.append((id(_e399), _r_end.intersection(_pg399)))
-        _vx399 = [tuple(_v) for _g399 in [_r_end] + [_ct399 for _, _ct399 in _cuts399] for _v in _gc399(_g399)]
+            # 🔧 `W-G.9-399` 補令二 ‴（R-1‴·塊 `K50` 之二之甲′·WARNING-1）：「臨」以該宗之土地判之——取該宗 ∩ R_end 之多邊形之部
+            #   （Polygon／MultiPolygon 之成分之聯集·線段、點等無面積之成分⛔ 入·無者⛔ 入此分配）與其開運算之形（先內縮 1e-05 m、
+            #   再外擴 1e-05 m·皆斜接·塊 `K50` 之二之甲′ 之數值之界·⛔ 域之參數）⇒ 零寬之折返、寬不及 0.02 mm 之刺⛔ 臨；
+            #   切點仍取多邊形之部之頂點。
+            _ix399 = _r_end.intersection(_pg399)
+            if _ix399.geom_type.endswith('Polygon'):
+                _pp399 = _ix399
+            else:
+                _pp399 = [_g399 for _g399 in getattr(_ix399, 'geoms', []) if _g399.geom_type.endswith('Polygon')]
+                if not _pp399:
+                    continue
+                _pp399 = _pp399[0] if len(_pp399) == 1 else _uu399(_pp399)
+            _cuts399.append((id(_e399), _pp399, _pp399.buffer(-1e-05, join_style=2).buffer(1e-05, join_style=2)))
+        _vx399 = [tuple(_v) for _g399 in [_r_end] + [_ct399 for _, _ct399, _ in _cuts399] for _v in _gc399(_g399)]
         for _a399, _b399 in _es399:
             _dx399, _dy399 = float(_b399[0]) - float(_a399[0]), float(_b399[1]) - float(_a399[1])
             _l2399 = _dx399 * _dx399 + _dy399 * _dy399
@@ -11853,8 +11866,9 @@ def end_block_pick(side, geom, entries, corner_range_polys, trial, _label='', al
                 _sl399 = (_t1 - _t0) * (_l2399 ** 0.5)
                 if not (_sl399 > 0.0) or not (_boundary_len_on_line(_r_end, _p399, _q399) > 0.5 * _sl399):
                     continue
-                for _i399, _ct399 in _cuts399:
-                    if _boundary_len_on_line(_ct399, _p399, _q399) > 0.5 * _sl399:
+                # 🔧 `W-G.9-399` 補令二 ‴（R-1‴·塊 `K50` 之二之甲′）：歸屬之判用該宗之開運算之形之外框（逾小段之長之半）
+                for _i399, _, _op399 in _cuts399:
+                    if _boundary_len_on_line(_op399, _p399, _q399) > 0.5 * _sl399:
                         _got399[_i399] = _got399.get(_i399, 0.0) + _sl399
                         break
     rows = []
````

`97` 呼叫之表見附錄甲；`V-1‴` 之 `45` 呼叫之出艙全文見附錄乙。

## ④ 塊之實得與三檔之改前改後

塊之實得見 ② `3‴`。三檔（工項三‴ `4c77eee`）：`K-6_街角地分配程序與可分配判準.md` `1025082` → `1056432`·blob `38571c5af27da6062a06d631bbf0263eae8ba35c`；`待落地清單.md` `49281` → `57626`·blob `c2b98093b93e889b2a23845d5d411868a53640bb`；`W-G.9波_claude.ai側自誤登記.md` `1249001` → `1255284`·blob `5166afa5da77ea018d964536b764fa3755c8e93e`；三者之改前皆為改後之嚴格前綴、尾 ＝ 塊（`K48`＋`K49`＋`K50`；`P59`＋`P60`＋`P61`；`E46`＋`E47`）、刪除欄 `0`（皆 ＝ `§五‴` 項 `5`）。塊 `CK` `1539`／`00cd3949…`／`31`、`GF` `2445`／`b11edb77…`／`47`（＝ 項 `7`）。

## ⑤ 推送之目標與推後之遠端分支之列

四推（工項零‴〜三‴）皆 `git push origin HEAD:verify/W-G.9-399-k960x`（快轉）：`1612750..bfdba99`、`bfdba99..9e0eeb1`、`9e0eeb1..0c35403`、`0c35403..4c77eee`。遠端分支之列之母體 ＝ `git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`：工項三‴ 推後 `57` 列；除 `ops/queue` 與新側支外之 `55` 列逐列 ＝ `<O>/heads_before_399p2.txt`；主線 ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`。

## ⑥ 自捕與自解；唯讀獨立審查之發現與處置

### ⑥-1 執行端之自捕與自解

1. **接單時之 `STATE.json` 之格式**：接單之 `commit`（`ops/queue` `598a422`）以 Python 寫回 `STATE.json` 時未保其原之縮排（`indent=1`）而成單列；即以次一 `commit`（`cd4ac5f`）復原其格式（內容⛔ 變·⛔ 改寫歷史）。另：該二步（讀單之前）之腳本以 heredoc 傳之；讀單後（單首「Bash 命令⛔ 含 heredoc」）一律以檔案之寫入為之。
2. **並行**：撰碼中之自跑（`F42 selftest`、`#5`、`#6`、`#96` 之等價於倉外之複本 `/tmp/wdev`·皆綠）期間，前置‴ 之跑之並行上限降為 `1`（跑表器每啟一呼叫前讀之）、待在跑者降至 `1` 方自跑（合計 ≤ `2`），自跑畢復 `2`。驗之 `97` 呼叫期間⛔ 他負載；審查之期間唯審查者之程序（≤ `2`）。
3. **字面之錨**：多邊形之部以 `geom_type.endswith('Polygon')` 判（`§三-3‴`·⛔ 用 `('Polygon', 'MultiPolygon')` 之字面）；撰後即自跑 `#5`、`#6` 確認 `F23 wiring` `W8`、`F24 wiring` `W7` 綠。
4. 佇列之發單端之他輪（`21:11` 之接手者）於本趟中另推一進度列（`ops/queue` `1641917`·`verifying` 之擬）；本趟之狀態 ＝ `running`，⛔ 涉之。

### ⑥-2 唯讀獨立審查（`redistribution-reviewer`·一輪·⛔ 改檔、⛔ `commit`·其實跑於 `/tmp/rv399p2/`）

- **總判：PASS**；(a) 純實作之瑕 `0`；(b) 規格之漏載或涉域上判斷 `0` ⇒ 停機款 `12‴` ⛔ 成就。
- 項一：審查者自重產之 `--no-index` 與 `<O>/post/v7_noindex.diff` 逐位同；hunk 三皆在 `end_block_pick`；ast 頂層節點 `429`／`429`、相異唯 `end_block_pick`；巢狀 def／lambda 新舊皆 `0`；新增之字面無 `('Polygon', 'MultiPolygon')`（全檔仍恰一見）；`R-2‴` 之字樣 `2`／`0`。
- 項二：多邊形之部、開運算（`buffer(-1e-05, join_style=2).buffer(1e-05, join_style=2)`·`mitre_limit` 預設）、切點取多邊形之部（⛔ 開運算之形）、歸屬之判用開運算之形，皆合塊 `K50` 之二之甲′；`R-1″` 之餘照舊。「Σ ≤ `end_len`」之證仍成（切點含 `R_end` 之一切頂點之投影 ⇒ 合格之邊於小段非全蓋即不蓋；本補令唯縮受者之集）；未取位 `2500` 例最大超出 `7.1e-15`。`F42 selftest` 之復現：新碼 `79／79`、`app_R0` `77／79`（紅 `['P13', 'P15']`）。NOTE：「無多邊形之部」之支因面積之門檻（`1 ㎡`）實不可達（無害）。
- 項三（自撰之生成器·TWD97 之尺度·旋轉·鏡射 `50%`；族：voronoi、沿端線之帶、零寬之折返〔fold〕、寬 `0.005`〜`0.015 mm` 之刺〔spikeU：繞條片〕〔finger：伸入鄰宗〕·各含等寬／漸細／觸端線之變體）：

| 測 | 例數 | 新碼 | `app_R0` |
|---|---|---|---|
| （甲）Σ臨端線 ≤ `end_len ＋ n × 0.005` | `2500` | 不合 `0` | 不合 `0` |
| （甲）Σ評選指數 ≤ `1 ＋ n × 5e-7` | `2500` | 不合 `0` | 不合 `0` |
| （丙）座標系之不變性·混族 | `3000` | 不合 **`0`**·最大差 `0.0` | 不合 **`155`**（fold `144`、spikeU `4`、finger `7`）·最大 `22.77 m` |
| （丙）同·聚焦 fold／spikeU／finger | `2000` | 不合 **`0`**·最大差 `0.01`（二位之取位之邊界·≤ 容差） | 不合 **`153`**·最大 `25.88 m` |
| （丙）未取位 ＞ `1e-6 m` 之例 | `5000` | `6` 例·最大 `3.24e-5 m` | `598` 例·最大 `25.88 m` |

  生成之覆蓋：一宗之有效性於二座標系之間翻者 `954` 例（本地有效而 TWD97 失效 `393`·`§三-4‴` ⑥ 之情境）、`R_end` 非單一 `Polygon` 者 `462` 例（⑦ 之情境）——新碼皆在 `0.01 m` 之內。
- NOTE（皆 (c)·已知之形）：① 未取位之評選指數之和 `1 ＋ 1.48e-7` 一例（`buffer(0)` 之修之面積之浮點·④·新舊同）；② 未取位之臨端線之二座標系之差 `3e-6`〜`3.24e-5 m` 六例（`buffer(0)` 之修之頂點隨座標系微移·⑤／⑥·二宗之和守恆）；③ 刺之族之判別力有限（`1e-5 m` 遠大於 TWD97 之 ULP），不變性之判別力主由 fold 族；④ 生成器之 fold／spike 族唯直端線、宗無洞。
- **審查者之自首**：其首次 `py_compile` 誤以 cwd ＝ `/tmp/w` 覆寫 `/tmp/w/__pycache__/app.cpython-311.pyc`（被 `.gitignore` 所忽略之快取·`git status` 無變動·`app.py` 之 blob 仍 `101a7a6a…`）——違其指示之「⛔ 於施工樹生檔」；執行端⛔ 刪之（僅快取·⛔ 涉追蹤檔與驗之受詞），記於此。
- **處置**：⛔ 改碼；推工項二‴。

## ⑦ 設計說明（`§三-5‴`·工項二‴ `0c35403`）

- **原單 `§三-5`、補令一 `§三-5″` 之各項**：照前趟（`reports/W-G.9-399_規格單_回報.md` 之 ⑦、`reports/W-G.9-399_補令一_回報.md` 之 ⑦·碼 ＝ `rep399p1.diff`·⛔ 改）；其上唯 `R-1‴`、`R-2‴`。
- **`R-0‴` 之 blob 之對證**：`git apply --check <O>/rep399p1.diff` 過 ⇒ 施於 `9e0eeb1` 之 `app.py`（`ca9f917e…`）⇒ `1158f83e060600a71bd9ff28c66d7ebdb9d6aa16`（`1927970` B）＝ 期；即複製為 `<O>/app_R0.py`。
- **`R-1‴`**（`end_block_pick`·評選之迴圈之前之分配）：跨占之判（頂點 ≥ `3`·無效者 `buffer(0)`·`∩ R_end` 之面積 ＞ `END_BLOCK_CROSS_MIN_AREA`）照舊；`_ix399 ＝ R_end ∩ 宗`：其 `geom_type` 以 `Polygon` 結尾（`Polygon`／`MultiPolygon`）者即為多邊形之部；否則（`GeometryCollection` 等）取其 `geoms` 中以 `Polygon` 結尾之成分——無者 `continue`（⛔ 入分配·列之臨端線 `0.0`）、一者即其本身、多者 `unary_union`；`_cuts399` 之每項 ＝ `(id(entry), 多邊形之部, 多邊形之部.buffer(-1e-05, join_style=2).buffer(1e-05, join_style=2))`；頂點之集 ＝ `R_end` 與諸多邊形之部之頂點（⛔ 開運算之形之頂點）；小段之切、`_boundary_len_on_line(R_end, p, q) ＞ 半` 之判照舊；歸屬 ＝ `entries` 之序最先之「`_boundary_len_on_line(開運算之形, p, q) ＞ 半`」之宗（`break`）。`1e-05` 以字面書、註其所據（塊 `K50` 之二之甲′）；⛔ 新頂層名、⛔ 新巢狀函式（`unary_union` 以區域之匯入名 `_uu399`）。
- **「諸列之和 ≤ `end_len`」之仍成**：每小段至多歸一宗，且唯 `R_end` 之外框逾其半者得歸；切點含 `R_end` 之一切頂點之投影 ⇒ `R_end` 之合格之邊於小段非全蓋即不蓋 ⇒ 得歸之小段之長之和 ≤ `end_len`；本補令唯改受者之判（縮其集），⛔ 及此證。
- **`R-2‴`**：所改之二處各附註（所據 ＝ 塊 `K50` 之二之甲′·WARNING-1），各載 `` `W-G.9-399` 補令二 ‴ ``（計 `2`）。
- **本案之量**（`F42 run`·二退縮同·`<O>/post/run/97.out`）：`R2` 右 端線 `44.12 m`·`628-34(1)` `10.42`／`0.372619`；`R3` 左 `43.91`·`628-34(2)` `34.94`／`0.799606`；`R5` 右 `47.95`·`628-23(2)` `0.0`／`0.023134`；`R6` 左 `47.71`·`628-23(1)` `0.0`／`0.114893`、`628-4(1)` `0.0`／`0.056826`（＝ 原單塊 `K48` 之四）；當選 ＝ 主線（`R2` 右 `628-34(1)`、`R3` 左 `628-34(2)`、`R5` 右 `628-23(2)`、`R6` 左 `628-4(1)`）；合併再試之標的 `[]`、競合 無。

## ⑧ 全文差異

同目錄之 `W-G.9-399R_末端塊評選指數之互相等待之先後_差異.diff`（`git diff bd7da4d 0c35403 -- app.py`·`42067` B·`523` 列·`373`／`14`）。

## ⑨ 工項三‴ 之 `checkidx`、`gen_fa_index`

- `python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`·末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md` ⇒ `rc 0`·`則 124；加註節 14；列 158`；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同（`cmp` 無出艙）。

## ⑩ 各段耗時（Asia/Taipei·並行之數）

接單 `21:32`；`§零-0‴`〜工項一‴ `21:33`〜`21:40`；前置‴ `21:40:59`〜`22:38:27`（並行 `2`·撰碼之自跑時 `1`）；撰碼與自跑 `21:41`〜`21:45`；工項二‴ 之 `commit` `22:38`；驗 `22:39:05`〜`00:33:04`（並行 `2`）；`V-3‴`〜`V-8‴` 之比 `00:33`〜`00:35`；審查 `00:35`〜`00:46`（≤ `2`）；工項二‴ 之推 `00:47`；工項三‴ `00:48`〜`00:50`；工項四‴ `00:50`。

## 附錄甲　`97` 呼叫之表（前置‴·驗）

格 ＝ `rc`／`stderr` B／末列（耗時 s）。(甲)(乙) ＝ 本趟實跑於 `9e0eeb1`；(丙) ＝ 沿用基準。驗 ＝ 本趟實跑於 `0c35403`。`<O>/<態>/` ＝ `<O>/pre/`／`<O>/post/`。

| # | 命令 | 工項一‴ 之端（前置‴） | 施後（驗） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（119） | `0`／`0`／`⇒ 紅 []；rc 0`（120） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（393） | `0`／`0`／`⇒ 紅 []；rc 0`（405） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（37） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（39） | `0`／`0`／`⇒ 紅 []；rc 0`（39） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（40） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（15） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（240） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（68） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（430） | `0`／`0`／`⇒ 紅 []；rc 0`（448） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（592） | `0`／`0`／`⇒ 紅 []；rc 0`（606） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | (甲)(乙) `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（9） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（67） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（364） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1607） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（25） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（21） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（238） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（304） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（36） | `0`／`0`／`⇒ 紅 []；rc 0`（44） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（38） | `0`／`0`／`⇒ 紅 []；rc 0`（40） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（27） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（17） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（174） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（47） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（792） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（155） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（117） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（297） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`selftest 9/9 ⇒ ✅`（1） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`selftest 13/13 ⇒ ✅`（1） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（3） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`紅項 [] 器紅 0`（11） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（304） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/<態>/k6s3_<態>_35.json` | (甲)(乙) `0`／`0`／`（JSON 之摘要列·略）`（173） | `0`／`0`／`（JSON 之摘要列·略）`（177） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/<態>/k6s3_<態>_00.json` | (甲)(乙) `0`／`0`／`（JSON 之摘要列·略）`（130） | `0`／`0`／`（JSON 之摘要列·略）`（128） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/<態>/f8_<態>_35.json` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（174） | `0`／`0`／`⇒ 紅 []；rc 0`（180） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/<態>/f8_<態>_00.json` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（126） | `0`／`0`／`⇒ 紅 []；rc 0`（128） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/<態>/parity35_<態>.json` | (甲)(乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（383） | `0`／`0`／`⇒ rc 0（不符 0 項）`（368） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/<態>/parity00_<態>.json` | (甲)(乙) `0`／`0`／`⇒ rc 0（不符 0 項）`（281） | `0`／`0`／`⇒ rc 0（不符 0 項）`（264） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（312） | `0`／`0`／`⇒ 紅 []；rc 0`（294） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1061） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`⇒ 紅 []；rc 0`（1038） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（121） | `0`／`0`／`⇒ 紅 []；rc 0`（118） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（423） | `0`／`0`／`⇒ 紅 []；rc 0`（378） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（314） | `0`／`0`／`⇒ 紅 []；rc 0`（285） |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（44） | `0`／`0`／`⇒ 紅 []；rc 0`（52） |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（616） | `0`／`0`／`⇒ 紅 []；rc 0`（566） |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（6） |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（316） | `0`／`0`／`⇒ 紅 []；rc 0`（281） |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（6） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（295） | `0`／`0`／`⇒ 紅 []；rc 0`（281） |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（297） | `0`／`0`／`⇒ 紅 []；rc 0`（278） |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（5） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（299） | `0`／`0`／`⇒ 紅 []；rc 0`（275） |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（9） | `0`／`0`／`⇒ 紅 []；rc 0`（8） |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（316） | `0`／`0`／`⇒ 紅 []；rc 0`（284） |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（2） |
| `92` | `python3 verify/probes/probe_WG9398_rw25.py selftest <repo>` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `93` | `python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf` | (甲)(乙) `0`／`0`／`⇒ 紅 []；rc 0`（4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `94` | `python3 tests/test_pool_slot.py` | (丙) 沿用基準 `bd7da4d…`（⛔ 重跑） | `0`／`0`／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）`（1） |
| `95` | `python3 verify/probes/probe_WG9399_k960x.py selftest <repo>` | (甲)(乙) `1`／`0`／`⇒ 紅 ['E1', 'E1′', 'E1″', 'E2', 'E3', 'E4', 'E5', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E6', 'E7', 'E8', 'E8′', 'E9', 'E10', 'E11', 'E11', 'E11′', 'E11′', 'E11′', 'E11′', 'E12', 'E12', 'E13', 'E13′', 'E14', 'E15', 'E15', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17', 'P18', '丙·例外', '丁·例外', 'M1', 'M2', 'M4', 'M6', 'M8', 'M10']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `96` | `python3 verify/probes/probe_WG9399_k960x.py wiring <repo> bd7da4d` | (甲)(乙) `1`／`0`／`⇒ 紅 ['W1', 'W2', 'W3', 'W4']；rc 1`（21） | `0`／`0`／`⇒ 紅 []；rc 0`（20） |
| `97` | `python3 verify/probes/probe_WG9399_k960x.py run <repo>` | (甲)(乙) `1`／`0`／`⇒ 紅 ['R1@3.5', 'R1@0.0']；rc 1`（316） | `0`／`0`／`⇒ 紅 []；rc 0`（284） |

## 附錄乙　`V-1‴` 之 `45` 呼叫之出艙全文（驗·`0c35403`）

### `#1`　`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ K1：{'front': 3.75, 'left': 1.0}／[]／[]
  ✅ K2：{'B1': {'front': 2.25}}／{'B1': {'front': 3.75}}
  ✅ K3：{'B1': {'front': 3.0}}
  ✅ K4：{'B1': {'front': 1.75}}／{'B1': {'front': 1.75}}／[]
  ✅ K5：{'B1': {'front': 1.75}}
  ✅ K6：{'B1': {'front': 3.75}}
  ✅ K7：{'B1': {'front': 3.15}}／[('RE', 0.4), ('RW', 0.6)]
  ✅ K8：{'B1': {'front': 0.0}}／['B1 正面道路勾選新闢，但未偵測到道路 BLOCK']／[]
  ✅ K9：{'B1': {'front': 3.75}}／['B1 正面：中心線垂距 × 2 ＝ 12.00 m，與輸入路寬 15.00 m 相差逾 0.5 m，請確認']
  ✅ K10：{'B1': {'front': 3.0882352941176467}}／{'B1': {'front': 2.625}}
  ✅ K11：['道路 BLOCK RA 未繪 CENTERLINE（B1 正面臨之），請補畫']
  ✅ K12：{'抵充地': {'100-1': 1.0, '100-3': 0.5, '100-4': 0.5}, '第33條排除': {}, 'errors': []}／['填列錯誤：甲段 100-2「第33條排除」欄填「是」，但該地號非公有地（U_LAND 公私別）', '填列錯誤：甲段 100-2「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）', '填列錯誤：甲段 100-1「第33條排除」欄填「Y」，僅得填「是」或空白', '填列錯誤：甲段 100-9「抵充地」欄填「是」，但 U_LAND 無對應資料']／['填列錯誤：地號 100-1 於 甲段、乙段 皆有，「抵充地」無從對應宗地']／{'抵充地': {}, '第33條排除': {}, 'errors': []}
  ✅ K13：[[(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]]
  ✅ K14：2.25／0.0／0.0
  ✅ K15：{'B1': {'front': 3.75}}
  ✅ K16：{'B1': {'front': 3.75}}／['尚無宗地資料（地籍），中心線是否為重劃區界⛔ 判（以輸入之路寬計）']
  ✅ K17：{'抵充地': {'100-3': 0.5}, '第33條排除': {}, 'errors': ['填列錯誤：甲段 100-1「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數', '填列錯誤：甲段 100-2「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數']}
  ✅ K18：{'B1': {'front': 0.0}}／['道路 BLOCK RA 內抵充地之面積大於扣除路口後之面積（宗地之片重疊），請檢查地籍（B1 正面臨之）']
  ✅ K19：[('壞檔', True, ['地籍資料來源讀取失敗（BadZipFile）：File is not a zip file']), ('缺欄', True, ["地籍資料來源讀取失敗（KeyError）：'段小段'"])]
  ✅ K20：前提（浮點之負）6／60；不符 []（0）
  ✅ K21：[True, True]
  ✅ K22：[True, True]
⇒ 紅 []；rc 0
````

### `#2`　`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 頂層之新名與⛔ 案件字面：[True, True, True, True]／K974_PARAMS True／字面 []
  ✅ W2 main() 恰一處呼之：['k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)']
  ✅ W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）：
  ✅ W4 JUNCTION 存 session：
  ✅ W5 步驟 H 之段以假 st 實跑：[{'label': 'B1', 'front_width': 15.0, 'front_length': 0.0, 'front_new': False, 'left_side_width': 0.0, 'left_side_length': 0.0, 'left_side_new': False, 'right_side_width': 0.0, 'right_side_length': 0.0, 'right_side_new': False, 'front_scale': 2.25, 'left_side_scale': 0.5}]／[('warning', '⚠️ 警示甲')]／[('error', '⛔ 錯甲'), ('error', '⛔ 錯乙')]／停 False/True
  ✅ W6 verify/ 之生產碼⛔ 呼之：[]
  ✅ W7 main／calc 唯增列（具名之換列三）·頂層之相異：相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k962_land_marks', 'k967_pool_less', 'k967_pool_out', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']／刪列 5
⇒ 紅 []；rc 0
````

### `#3`　`python3 verify/probes/probe_WG9385_k974.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  各面之尺度：R4 front 0.0／left 1.0／right 1.0；R6 front 2.0／left None／right 1.0；R5 front 2.0／left 1.0／right None；R2 front 2.0／left 1.0／right None；R3 front 2.0／left None／right 1.0；R1 front 0.0／left 1.0／right 1.0
  ✅ R1 尺度 ＝ 快照之負擔尺度_輸入：不符 []／警示 []／錯誤 []
  ✅ R2 calc 之列給尺度與否逐值同：741.76／741.76
  ✅ R3 抵充地之模擬（628-34·RD1）：RD1 1082.2651／628-34 之片 131.6000／比例 0.878403／負擔路寬 7.0272／期 1.513613、0.756806／得 1.513616、0.756808
  ✅ R4 私有地填「是」⇒ 填列錯誤：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']
  ✅ R6 二欄之結果之存與換檔：['填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）']／[]
  ✅ R5 JUNCTION 之模擬（RD1 之一端）：框內 89.6652／比例 0.867420／期 1.469679／得 1.469679
⇒ 紅 []；rc 0
````

### `#4`　`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
── 手冊先行（K-9-53 ①）之各支 ──
  ✅ K1 跨分配線（所鄰之已配得之宗恰一）⇒ 整筆併入、出 build、帶 段三併出
  ✅ K2 跨分配線（所鄰之已配得之宗分處二街廓）⇒ 併入應分配面積（G）較大者
  ✅ K3 （K-9-67）二者之 G 並列 ⇒ 重劃前面積同（300）⇒ 暫編地號小者 E1(1)；E1 之重劃前面積 250 ⇒ X1(2)
  ✅ K4 建地片與同街廓之已配得之宗相鄰 ⇒ 依手冊整筆併入之（K-9-58 ③·W-G.9-380）
  ✅ K5 道路·兩側皆有 ⇒ 依中心線切分、各半併入該側之宗（a′ × 半之面積比）
  ✅ K6 道路·唯一側有 ⇒ 整筆往該側（所鄰之街廓依中心線分側）
  ✅ K7 道路·兩側皆無 ⇒ 未併、帶 段三餘量 ＝ a（視同無同歸戶）
  ✅ K8 道路片全在無已配得之側（⛔ 鄰有之側之街廓）⇒ 仍整筆往有之側
  ✅ K9 隔道路之分不到之建地 ⇒ 隨道路片往另一側之宗
  ✅ K10 公設地 ⇒ 平分於其合併群所及之已配得之街廓（群外之已配得之宗⛔ 與）
  ✅ K11 公設地不相連於任何已配得之宗 ⇒ 未併、帶 段三餘量 ＝ a
  ✅ K12 路口之道路片（鄰三街廓以上、含公設地）⇒ 比照公設地平分
  ✅ K13 落點四層瀑布：① 同原地號者先於較近者；② 皆非同原地號 ⇒ 質心距近者；③ 等距 ⇒ G 大者；④ 皆同 ⇒ 暫編地號
  ✅ K14 （K-9-66）整批不過 ⇒ 建地整筆不過 ⇒ 按比例部分併入 10；剩下 50 依 K-9-51（他街廓之已配得之宗·距離近者先）
  ✅ K15 可拆分之片之最大面積（0.01 ㎡ 之格）；其餘 ⇒ K-9-51 皆無 ⇒ 入合併單位、帶 段三部分併出／段三餘量
  ✅ K16 併入後配地中止 ⇒ 不過（記其由·⛔ 停機）
  ✅ K17 帶段三之鍵之片⛔ 受理
  ✅ K18 無任何配得土地之地主：同號之連通分量之再試未成 ⇒ 回輸入之同一物件、紀錄唯再試之列（K-9-73 ④）
  ✅ K19 入池閘之合併單元：取代後之配地全同 ⇒ 取代；相異 ⇒ ⛔ 取代（記之）
  ✅ K20 調配之輸入（⛔ 改·沿用段三之鍵）：併出 ⇒ 原位次配地（所屬單元『段三併入 …』）；餘量 ⇒ 入合併單位；待同歸戶併入 ＝ 空
  ✅ K21 公設地調配之 temp（⛔ 改·沿用段三之鍵）：併出而無餘量 ⇒ 去之；部分併出 ⇒ 依餘量之比縮之
  ✅ K22 a′ 之折算（街廓之地價比）
  ✅ K23 （K-9-66）整批不過時：建地先（全入）、道路次（按比例）、公設地未試；剩下之列於諸輪之後
  ✅ K24 旗標 WV_K953：未設／on ⇒ 真；off ⇒ 偽；他值 ⇒ 停機
  ✅ K25 可為受詞之片之歸戶於 build 皆無片（例：歸戶表為空）⇒ ⛔ 試算配地、回輸入之同一物件、紀錄 ＝ []
  ✅ K26 試算之摘要：抵費地之形放不下最小建築面積之矩形 ⇒ 配餘地不合格一處；保留 ⇒ 保留宗與其 G；餘⛔ 計
  ✅ K27 入池閘之單元：成員（缺 ⇒ 自身）；成員 ≥ 2 者為單元（深拷貝）
  ✅ K28 K-9-51 之候選含 x 之本街廓之已配得之宗（與 x ⛔ 相連·距離 0）⇒ 先試併之、過 ⇒ 併入、出 build（K-9-55）；其檢核不過 ⇒ 記未成、續試他宗；皆不行 ⇒ 入合併單位（補令二·乙案）
  ✅ K29 入池閘之旗標 off（WV_K929_6）⇒ 手冊先行不辦（harness 與畫面皆回輸入之同一物件、紀錄 []、畫面⛔ 呼叫 st）；二旗標皆判（WV_K953 off 而 WV_K929_6 非法 ⇒ 停機）
  ✅ K30 畫面：旗標值非法（WV_K953 或 WV_K929_6）⇒ f3_k6b_stage3_error ＝ （手冊先行）…、st.error ＋ st.stop、⛔ 寫紀錄
  ✅ K31 入池閘之單元之取代後：build ⊂ temp（同物件）、temp 中之標的 ＝ 單元（帶入池閘併入）、他成員仍在 temp 而⛔ 在 build
  ✅ K32 K-9-51 之候選同距離（0）：本街廓之宗居先於他街廓之宗（G 較大者亦然·K-9-55 之二）；本街廓無之、或其檢核不過 ⇒ 他街廓之宗
  ✅ K33 K-9-51 之本街廓之候選與 x 相連（C0 之後始為已配得）、⛔ 相連 ⇒ 皆本街廓之宗居先、併入之（W-G.9-380）
  ✅ K34 K-9-51 之本街廓之候選之成員取當下之試算：其單元於 C0 之後始含與 x 相接之片、該片⛔ 與 x 相接 ⇒ 皆併入之（W-G.9-380）；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K35 本街廓之候選：G 較小者（H2(1)）與 x 相接 ⇒ 相接者（距離 0）先、併入之（K-9-51·W-G.9-380）；後者⛔ 與 x 相接 ⇒ 併入 G 較大者
  ✅ K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入
  ✅ K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入其計畫之受併宗
  ✅ K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片——⛔ 停機、依計畫併入（W-G.9-380）；⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ 併入（⛔ 取聯集）
  ✅ K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、他歸戶（BD 之 D9(1)）⇒ 皆停機（程式自我檢查·K-9-57 ⑧）
  ✅ K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）
  ✅ K41 跨二街廓之小片 S(1) 唯與已配得之宗 R(1) 之成員 Q(1)（⛔ R(1) 之自身之形）相連 ⇒ 手冊先行連同成員看之、依手冊整筆併入 R(1)（巳 ③）
  ✅ K42 計畫之同街廓相鄰之已配得之宗（Q1(1)·X1(2) 為他地號 ⇒ ⛔ 第 31 條第 3 款）之併入之檢核不過（BA 之容量 0）⇒ 記未成、依 K-9-51 併入他街廓之宗（X1(2)）
  ✅ K43 同街廓相鄰（Q1(1)）與他街廓之同一原地號（X1(2)）並存 ⇒ 第 31 條第 3 款先（K-9-73）：X1(2) 之 G 400 ⇒ X1(2)；Q1(1) 之 G 400 ⇒ 仍 X1(2)
  ✅ K44 同街廓相鄰之已配得之宗二（A1(1) G 300、A2(1) G 200）⇒ 應分配面積大者 A1(1)（K-9-61 ①⑦·K-9-67）
  ✅ K45 （K-9-73 ⑤）與他街廓之已配得之宗（X1(2)·他地號）相連而無同一原地號者 ⇒ ⛔ 依手冊併入（計畫無受併宗·未併）
  ✅ K46 （K-9-73 ③⑤⑦）分不到之 C1(1) 與他街廓之同一原地號 C1(2) 及他地號 G1(1)（G 較大）皆相連、且隔自己之道路片 R1(1) ⇒ 第 31 條第 3 款（唯同一原地號）先 ⇒ C1(2)
  ✅ K47 （K-9-73 ⑥·手冊道路用地分配原則 1）分不到之 C1(1) 隔自己之道路片 R1(1)（另一側 X1(2)），而同街廓有已配得之C9(1) 與之相連 ⇒ 道路兩側皆有己地（道路片依中心線切分·⛔ 隨道路往另一側）⇒ 併入同街廓相鄰之 C9(1)
  ✅ K48 （K-9-73 ⑤）分不到之 X1(1) 與同街廓之 Q1(1) 及他街廓之他地號 X1(2)（G 400·較大）皆相連 ⇒ 他地號之相連⛔ 入比較 ⇒ 併入同街廓相鄰之 Q1(1)
  ✅ K49 （K-9-73 ④）X1(1)（BA 60）與 X1(2)（BB 300）皆不配地 ⇒ X1(1) 整筆併入 G 大之 X1(2)；併後 X1(2)（360）配地 ⇒ 成：X1(1) 出 build、帶 段三併出 ['X1(2)']；X1(2) 之 面積_m2 60、帶 第31條第3款併入 ['X1(1)']
  ✅ K50 （K-9-75）受併之片依應分配面積（不配地紀錄之 G）：X1(1) 之 G 500 ＞ X1(2) 之 300 ⇒ X1(2) 併入 X1(1)（⛔ 依面積）
  ✅ K51 （K-9-75·K-9-67）G 並列（皆 100）⇒ 重劃前面積大者（X1(2) 300 ＞ X1(1) 60）受併（⛔ 暫編地號之序）
  ✅ K52 （K-9-29）再試之併入量依 a′（BA 之地價 2 倍）⇒ 120
  ✅ K53 （K-9-75 ②）同一原地號跨三街廓（X1(1)·BA ─ X1(2)·BB ─ Z1(1)·BD·X1(1) 與 Z1(1) ⛔ 直接相接）皆不配地 ⇒ 餘二片皆併入 G 最大之 Z1(1)（400）；併後 760 配地 ⇒ 成
  ✅ K54 （K-9-75 ②）三街廓之同號之連通分量而 Z1(1) 已配得 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1)（⛔ 與 Z1(1) 直接相接）亦併入 Z1(1)
  ✅ K55 （K-9-73 ⑥）同一原地號而隔道路之 C1(1)（BC）⛔ 入同號之連通分量 ⇒ 再試唯 X1(1) → X1(2)
  ✅ K56 再試之受詞存在而試算未回 dropped ⇒ 停機（⛔ 以空代之）
  ✅ K57 同號之片 X1(2) 為已配得之宗 Y1(1) 之成員 ⇒ ⛔ 再試；第 31 條第 3 款：X1(1) 併入 Y1(1)
  ✅ K58 （K-9-75）同一原地號之公設地之片（P1(1)·PK·與 X1(2) 相接）⛔ 入同號之連通分量 ⇒ 再試照行（X1(1) → X1(2)）
  ✅ K59 （K-9-73 ⑨）受併之片配地而「不影響原位次」之檢核不過（BB 之配餘地不合格）⇒ 未成（⛔ 施）
  ✅ K60 再試成而受併之片 X1(2) 為同地主之 Y1(1)（宿主）之單元之成員 ⇒ 單元之取代（X1(2) 出 build）之後，Y1(1) 之單元帶 第31條第3款併入 ['X1(1)']（⛔ 失）
  ✅ K61 （K-9-71）BC 之使用分區（商業區）異於片之所屬街廓 BA ⇒ 五級排後：剩下 50 併入 BD 之 Z1(1)（⛔ 距離近之 C1(1)）
  ✅ K62 （K-9-71）五級皆同而 BC 較深（40）⇒ 排後 ⇒ Z1(1)；BC 深 30.1（同深之容差 0.1 m 內）⇒ 依距離 ⇒ C1(1)
  ✅ K63 （K-9-71）BD 之最小建築面積往大（100）⇒ 排後而⛔ 淘汰：C1(1)（BC 容 0）不過 ⇒ 續試 Z1(1) 成
  ✅ K64 他街廓之候選二以上（BC、BD）而⛔ 給五級之屬性 ⇒ 停機（⛔ 以距離代之）
  ✅ K65 他街廓之候選唯一（BB·C1 去之）⇒ ⛔ 比五級：⛔ 給其屬性亦照行（K42 之形）
  ✅ K66 五級之屬性缺片之所屬街廓（BA）⇒ 停機
  ✅ K67 五級之屬性之回呼唯於須比時呼之、且一次（K61 之形 ⇒ 1；Z1 非 g1 ⇒ 他街廓唯一 ⇒ 0）
  ✅ K68 k971_key5 ＝ adj_candidate_lists 之建地軌之八鍵之前六（合成之屬性三組·七街廓·逐對 126）
  ✅ K69 再試成而受併之片 X1(2) 為 Y1(1) 之單元之成員；取代後之配地相異（未取代）⇒ 當下之態⛔ 變：X1(2) 仍在 build 且帶標記、宿主 Y1(1)⛔ 帶鍵
  ✅ K70 他街廓唯一（BC）而其候選二宗（C1(1)、C9(1)·皆 g1）⇒ ⛔ 比五級：⛔ 給其屬性亦照行 ⇒ C1(1)
  ✅ K71 五級與深度皆同之他街廓 BC（距 10）、BD（距 20）、BZ（距 1·名序最後）⇒ 依距離 ⇒ BZ 之 Z9(1)（⛔ 依街廓名）
  ✅ K72 （K-9-71）正面路寬：BA 8、BC 15（往寬）、BD 6（往窄）⇒ 二者皆異、級距 BD 先（往窄先於往寬）⇒ Z1(1)
  ✅ K73 （K-9-71）正面道路：BC 臨他路（RX）⇒ 排後 ⇒ Z1(1)
  ✅ K74 五級之屬性之回呼回非 dict ⇒ 停機
  ✅ K75 （K-9-71）道路之片 R1(1)（RD）之北半部分併入 X1(2)（BB 容 33.333）後，剩下 16.67 之他街廓之候選 ＝ C1(1)（BC·距 0·使用分區 商業區）、Z1(1)（BD·距 10）⇒ 道路之片照距離 ⇒ C1(1)（⛔ 依五級排 Z1(1) 先）
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 75／75
⇒ 紅 []；rc 0
````

### `#5`　`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（605）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
````

### `#6`　`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（607）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
````

### `#7`　`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
````

### `#13`　`python3 verify/probes/probe_WG9367_adj4.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
── 規格步 4 乙（K-9-53 ②·第一趟）之各支 ──
  ✅ K1 旗標：未設／空／' On ' ⇒ True；off／OFF ⇒ False；他值 ⇒ 停機
  ✅ K2 無受詞 ⇒ 回輸入之同一物件、紀錄 []、⛔ 試算；build 片不在 temp ⇒ 停機（受詞為空亦然）
  ✅ K3 整體成：名單首 BA 無其已配得之宗 ⇒ 略過；BB 之受併宗 X1(2)（同原地號）；三片皆併、建地片自 build 去、輸入⛔ 改、build ⊆ temp（同物件）
  ✅ K4 整體不過（BB 之容量 150）⇒ 逐片：建地整筆成、道路片取最大面積（0.01 之格）、公設片未成；剩下續往名單之下一街廓 BD（整體成·受併宗 Z1(1)）
  ✅ K4b 整體不過之列記其由（配餘地不合格）
  ✅ K5 名單盡而有剩下 ⇒ 剩下之列（留於合併單位）；部分併出者之三鍵（段三部分併出·段三餘量）
  ✅ K6 全不容 ⇒ 每街廓整體＋三逐片皆未成、剩下 ＝ 全部；⛔ 改宗地（建地片仍在 build·無鍵·無增）
  ✅ K7 受併宗之序（同街廓有二宗）：① 同原地號居先（距離較遠亦然）② 距離近 ③ 同距離 ⇒ G 大 ④ 同 G ⇒ 重劃前面積大（K-9-67）⑤ 再同 ⇒ 暫編地號小
  ✅ K8 前已有段三之三鍵之片：其剩下 ＝ 段三餘量；全併 ⇒ 段三併出合之、去部分二鍵；部分 ⇒ 段三部分併出合之、段三餘量 ＝ 新剩下
  ✅ K9 建地片於當下之試算已為已配得之宗 ⇒ 停機（程式自我檢查·K-9-57 ⑧·`W-G.9-370` 之訊息）
  ✅ K10 現態之配地中止 ⇒ 停機
  ✅ K11 受詞：同歸戶原位次配地之街廓非空者；序 ＝ (建地軌先, 原有面積大, 歸戶)；片 ＝ 建築街廓內不能分配 ＋ 共同負擔用地（相異）；無名單 ⇒ 停機；名單重複 ⇒ 停機
  ✅ K12 GB-199：受併宗之序之距離取 slice_geom 之原形（temp 之形縱異亦然）；片之原形缺 ⇒ 停機
  ✅ K13 a′ 折算（K-9-45 二）：併入量 ＝ 來源面積 × p(來源) ÷ p(受併宗)；最大面積之格取來源面積；三鍵之部分併出記來源面積
  ✅ K14 「不影響原位次」：併入使同街廓原保留之宗不保留 ⇒ 不過（整體與逐片皆然）
  ✅ K15 GB-201（手冊先行）：計畫之受併宗於當下之試算未保留 ⇒ 停機（可拆分之片／整筆之建地片）
  ✅ K16 三旗標（WV_ADJ4／WV_K953／WV_K929_6）之任一 off ⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 呼叫 st
  ✅ K17 三旗標之任一其值非法 ⇒ harness 停機；畫面 ⇒ f3_k6b_stage3_error ＝ （第一趟）…、st.error、st.stop、⛔ 寫紀錄
  ✅ K18 adj4_plan：無受詞 ⇒ []；唯公設軌 ⇒ 正面道路之缺以佔位代之、名單依距離；建地軌 ⇒ 停機（正面道路無識別符）
  ✅ K19 adj4_depth_of：取 f3_alloc_depth_by_label（缺 ⇒ {}）；回新 dict
  ✅ K20 adj4_trial_state：摘要 ＋ err ＋ 成員與單元（成員 ≥ 2 者為單元·深拷貝）
  ✅ K21 adj4_possible（先篩）：歸戶非空、為 build 之某宗之歸戶、temp 中（殘料除外）其片 ≥ 2 者存在 ⇒ True
  ✅ K22 三旗標皆 on 而先篩偽（歸戶表空）⇒ harness 與畫面皆回輸入（同物件）、紀錄 []、⛔ 試算、⛔ 呼叫 st
  ✅ K23 R-8 之止：整體不過（他街廓之原保留之宗失·非單調之玩具）而逐片皆成 ⇒ 諸片皆無剩下 ⇒ 止於本街廓（⛔ 往名單之次街廓 BD）
  ✅ K24 （K-9-66）T 含建地片之所屬街廓：全數併出使 BA 之 Q1 失 ⇒ 整體與建地之全併皆不過；按比例 59.99（留 build）⇒ 過；道路、公設地未試
  ✅ K25 （K-9-66）同類按比例：建地全入後道路容 190 ⇒ R9 126.67、R1 63.33（各乘 190／300）；列依剩下大者先
  ✅ K26 R-12：併入後之配地中止 ⇒ 不過（記其由）；整體不過 ⇒ 逐片（公設片取最大面積）
  ✅ K27 R-10′（K-9-57 ⑧·程式自我檢查）：同一輪中併入某街廓之前，以當下之試算查其所受之建地片——前一街廓之併入使之已為已配得之宗（依既定機制不會發生·玩具以非單調之回呼造之）⇒ 停機（⛔ 靜默併出）；對照 ⇒ 二街廓皆整體成
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 28／28
⇒ 紅 []；rc 0
````

### `#17`　`python3 verify/probes/probe_WG9363_k953.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.51／ΣG 之變 2934.46（和 ≤ 0.1）True
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.90／ΣG 之變 3663.84（和 ≤ 0.1）True
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

### `#18`　`python3 verify/probes/probe_WG9367_adj4.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@3.5：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@3.5：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6600（和 +0.0200·≤ 0.1）
  ✅ R4@3.5：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@3.5：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
  ✅ R1@0.0：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@0.0：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@0.0：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6700（和 +0.0100·≤ 0.1）
  ✅ R4@0.0：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@0.0：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
⇒ 紅 []；rc 0
````

### `#19`　`python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ M00 —·基準（⛔ 突變）：錨 1 見；紅 []；所指 []
  ✅ M20 R-12·原保留之宗之判去之：錨 1 見；紅 ['K14', 'K23', 'K24']；所指 ['K14']
  ✅ M21 R-12·配餘地不合格之判去之：錨 1 見；紅 ['K4', 'K4b', 'K5', 'K6', 'K8', 'K13', 'K25']；所指 ['K4b']
  ✅ M23 R-12·併入後之配地中止改為過：錨 1 見；紅 ['K26']；所指 ['K26']
  ✅ M24 R-13·段三併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M25 R-13·段三部分併出⛔ 合既有：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M26 R-13·全併⛔ 去部分二鍵：錨 1 見；紅 ['K8']；所指 ['K8']
  ✅ M27 R-13·段三餘量之值誤：錨 1 見；紅 ['K5', 'K8', 'K13']；所指 ['K8']
  ✅ M30 R-16·GB-201 之判恆過：錨 1 見；紅 ['K15']；所指 ['K15']
⇒ 突變 8（另基準一）；紅 []；rc 0
````

### `#34`　`python3 verify/probes/probe_WG9352_endblock.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
── 合成對照（AST 抽出之 end_block_*／solve_G_binary／_select_pool_slot）──
  ✅ S1 左端觸發（未臨正街 45·s_back 3·末端帶 105·R_end 150）：得 (True, 45.0, 3.0, 150.0, 105.0)　期 (True, 45.0, 3.0, 150.0, 105.0)
  ✅ S2 右端觸發（鏡像）：得 (True, 45.0, 3.0, 150.0, 105.0)　期 (True, 45.0, 3.0, 150.0, 105.0)
  ✅ S3 未臨正街 0 ⇒ 亦觸發（左端鉛直·R_end ＝ 末端帶·W-G.9-393）：得 (True, 0.0, 0.0, 105.0, 105.0)　期 (True, 0.0, 0.0, 105.0, 105.0)
  ✅ S4 往後找·等號當選（A 未達、B ＝ 150 當選）：得 ('B(1)', ['未達', '當選'])　期 ('B(1)', ['未達', '當選'])
  ✅ S5 跨占 ≤ 門檻者非候選（T 跨占 0.49 ㎡）：得 'C(1)'　期 'C(1)'
  ✅ S6 跨占街角規定範圍者歸街角側（⛔ 候選）：得 [('B(1)', '跨占街角規定範圍·歸街角側'), ('C(1)', '當選')]　期 [('B(1)', '跨占街角規定範圍·歸街角側'), ('C(1)', '當選')]
  ✅ S7 皆未達 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S8 落位（左）：當選者移至首·餘者原序：得 [('C(1)', True), ('A(1)', False), ('B(1)', False), ('D(1)', False)]　期 [('C(1)', True), ('A(1)', False), ('B(1)', False), ('D(1)', False)]
  ✅ S9 落位（右）：當選者移至末：得 ['A(1)', 'C(1)', 'D(1)', 'B(1)']　期 ['A(1)', 'C(1)', 'D(1)', 'B(1)']
  ✅ S10 落位：當選者為入池閘合併單元之成員 ⇒ 移該單元：得 ['U(1)', 'A(1)']　期 ['U(1)', 'A(1)']
  ✅ S10b 落位：當選者為街角第 1 宗 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S11 首趟評選、次趟沿用（⛔ 重評）：得 ('B(1)', 2, 'B(1)', 0, 3.0, 'B(1)', None)　期 ('B(1)', 2, 'B(1)', 0, 3.0, 'B(1)', None)
  ✅ S11b 二源不一致 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S12 首趟未觸發而本趟觸發 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S13 選槽之 pin（左 pin ⇒ k≥1；右 pin ⇒ k≤n−1）：得 (1, 2, 0)　期 (1, 2, 0)
  ✅ S14 顯示（值皆字串·未觸發之端具名）：得 {'lines': ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；當選 B(1)', 'BX 右端（無側街）：未臨正街 0.0 ㎡ ⇒ 未觸發'], 'rows': [{'街廓': 'BX', '端': '左', '暫編地號': 'A(1)', '試算G(㎡)': '—'}]}　期 {'lines': ['BX 左端（無側街）：未臨正街 45.0 ＋ 末端帶 105.0 ＝ R_end 150.0 ㎡；當選 B(1)', 'BX 右端（無側街）：未臨正街 0.0 ㎡ ⇒ 未觸發'], 'rows': [{'街廓': 'BX', '端': '左', '暫編地號': 'A(1)', '試算G(㎡)': '—'}]}
  ✅ S15 定案趟之檢：首宗非當選者 ⇒ 停機；是 ⇒ 過：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
  ✅ S15b 定案趟之檢：首宗為當選者 ⇒ 過：得 '過'　期 '過'
  ✅ S16 s_back：宗地 ＝ 未臨正街 ∪ [0,S]；G 之 S 只計正街段：得 (True, True, 0.0, -3.0, True)　期 (True, True, 0.0, -3.0, True)
  ✅ S17 s_back＝0 ⇒ 逐位同：得 (True, True, True)　期 (True, True, True)
  ✅ S18 s_back 與 side_mid 並存 ⇒ 停機：得 ('例外', 'RuntimeError')　期 ('例外', 'RuntimeError')
── 判別力（AST 抽出 ＋ 突變·每一突變須使至少一例轉紅）──
  ✅ M0 未突變之抽出版：紅 []（期 []）
  ✅ M1 當選改為嚴格大於：轉紅 ['S4 往後找·等號當選（A 未達、B ＝ 150 當選）', 'S11 首趟評選、次趟沿用（⛔ 重評）']
  ✅ M2 首筆跨占者即當選（⛔ 往後找）：轉紅 ['S4 往後找·等號當選（A 未達、B ＝ 150 當選）', 'S7 皆未達 ⇒ 停機', 'S11 首趟評選、次趟沿用（⛔ 重評）']
  ✅ M3 跨占街角規定範圍者⛔ 排除：轉紅 ['S6 跨占街角規定範圍者歸街角側（⛔ 候選）']
  ✅ M4 落位⛔ 移至首：轉紅 ['S8 落位（左）：當選者移至首·餘者原序', 'S10 落位：當選者為入池閘合併單元之成員 ⇒ 移該單元', 'S11 首趟評選、次趟沿用（⛔ 重評）']
  ✅ M5 未臨正街計入臨街：轉紅 ['S16 s_back：宗地 ＝ 未臨正街 ∪ [0,S]；G 之 S 只計正街段']
  ✅ M6 首趟評選⛔ 沿用：轉紅 ['S11 首趟評選、次趟沿用（⛔ 重評）', 'S12 首趟未觸發而本趟觸發 ⇒ 停機']
  ✅ M7 選槽⛔ 理 pin：轉紅 ['S13 選槽之 pin（左 pin ⇒ k≥1；右 pin ⇒ k≤n−1）']
⇒ 紅 []；rc 0
````

### `#35`　`python3 verify/probes/probe_WG9352_endblock.py wiring <repo>`（`rc 0`·`stderr` `0` B）

````text
── 接線（AST／字樣·app.py ＋ verify/stepg_pipeline.py）──
  ✅ W1 模組層之常數與七函式、函式內⛔ 案件字面（案件字面 []）
  ✅ W2 二宿主於 `_ov2_idx` 前恰一次呼叫 end_block_host（solve_one=_solve_one）
  ✅ W3 左鏈一處、右鏈二處之 `_solve_one` 帶 `_s_back`（二宿主）
  ✅ W4 定案趟呼叫 end_block_assert_head（二宿主）
  ✅ W5 選槽之 pin 與 _kmin_c／_kmax_c（二宿主）
  ✅ W6 非試算趟先清 SS_END_BLOCK_EVAL（二宿主）
  ✅ W7 入池閘之畫面入口於復原之後帶出評選；鍵 ∈ K6B_SCREEN_TRIAL_KEYS 且末項 ＝ f3_k929_6_log
  ✅ W8 _WF_NS_NAMES 含 end_block_host／end_block_assert_head／SS_END_BLOCK_EVAL
  ✅ W9 solve_G_binary／_solve_G_one 之 s_back 與 fallback 停機
  ✅ W10 main() 之顯示（end_block_eval_rows 讀 SS_END_BLOCK_EVAL）
── 判別力（每一突變須使至少一項由綠轉紅）──
  ✅ N1 harness 左鏈去 _s_back：轉紅 ['W3']
  ✅ N2 入池閘之畫面入口⛔ 帶出評選：轉紅 ['W7']
  ✅ N3 畫面選槽去 pin：轉紅 ['W5']
  ✅ N4 harness 非試算趟⛔ 清評選：轉紅 ['W6']
⇒ 紅 []；rc 0
````

### `#62`　`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
── 合成對照（AST 抽出之 adj_intake 等）──
  ✅ K1 G 之加總較大者：得 'B2'　期 'B2'
  ✅ K2 G 相同 ⇒ 重劃前面積之合計較大者：得 'B1'　期 'B1'
  ✅ K3 G 以 0.01 ㎡ 為單位相同 ⇒ 重劃前面積：得 'B2'　期 'B2'
  ✅ K4 G 以 0.01 ㎡ 為單位相異 ⇒ G：得 'B1'　期 'B1'
  ✅ K5 G、重劃前面積皆同 ⇒ 最小之暫編地號較小者：得 'B1'　期 'B1'
  ✅ K6 G 逐街廓加總（⛔ 逐筆）：得 'B1'　期 'B1'
  ✅ K7 合併單元之 G 只計一次：得 'B2'　期 'B2'
  ✅ K8 合併單元之重劃前面積計其諸成員：得 'B1'　期 'B1'
  ✅ K9 重劃前面積 ＝ 原有面積（部分併出之剩下·⛔ 分攤登記面積）：得 'B2'　期 'B2'
  ✅ K10 三街廓：二者並列 ⇒ 其後之鍵：得 'B3'　期 'B3'
  ✅ K11 皆同 ⇒ ⛔ 停機：得 True　期 True
  ✅ K12 原街廓之據 ＝ 各街廓之 G 之加總：得 {'B1': 35.0, 'B2': 30.0}　期 {'B1': 35.0, 'B2': 30.0}
  ✅ K13 暫編地號以字典序比：得 'B1'　期 'B1'
  ✅ K14 單一街廓：得 'B2'　期 'B2'
  ✅ K15 街廓內之最小之暫編地號亦以字典序：得 'B1'　期 'B1'
  ✅ K16 重劃前面積先加後捨：得 'B1'　期 'B1'
  ✅ K17 重劃前面積以 0.01 ㎡ 為單位相同 ⇒ 暫編地號：得 'B2'　期 'B2'
  ✅ K18 重劃前面積 ＝ 原有面積（入池閘之帳之剩下）：得 'B2'　期 'B2'
⇒ 紅 []；rc 0
````

### `#63`　`python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 adj_intake 呼叫 k967_rank（呼叫 1）
  ✅ X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise（[]）
  ✅ X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}（增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'rw_pct_2dp', 'rw_width_mm']／去 []／相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']）
  ✅ X4 adj_intake 內⛔ 案件字面（[]）
  ✅ X5 生產碼 app.py 以外之 33 檔對基準相異 0（相異 []）
⇒ 紅 []；rc 0
````

### `#64`　`python3 verify/probes/probe_WG9387_k961h.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 92.46｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.25｜外部錨 R5
     G030｜原街廓 R3｜據 R2 27.54、R3 28.34｜外部錨 R3
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 88.63｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.25｜外部錨 R5
     G030｜原街廓 R2｜據 R2 27.54、R3 24.88｜外部錨 R2
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
⇒ 紅 []；rc 0
````

### `#65`　`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
── selftest（合成·K-9-61 ①②③⑥）──
  ✅ K1 二受併宗皆與道路片相鄰 ⇒ 應分配面積大者（D1 ⇒ A1）
  ✅ K2 道路片唯與其一相鄰 ⇒ 該宗（D2 ⇒ A2·縱 G 140 ＜ 160）
  ✅ K3 應分配面積以 0.01 ㎡ 相同 ⇒ 重劃前面積大者（D1 ⇒ A2）
  ✅ K4 再同 ⇒ 暫編地號小者（D1 ⇒ A1）
  ✅ K5 無本段受併宗之街廓之原位次配得之宗二以上 ⇒ 相鄰者先 → G（D1 ⇒ A1／S2；D3 ⇒ S3）
  ✅ K6 有受併宗之街廓內另有原位次配得之宗 ⇒ 照配、與 D2 相鄰而承受之（D1 ⇒ A1·D2 ⇒ K）
  ✅ K7 所鄰之配得街廓二 ⇒ 承受之宗之 G 大之一側（X ⇒ C1·170 ＞ 160）
  ✅ K8 二側之 G 以 0.01 ㎡ 相同 ⇒ 重劃前面積大之一側（X ⇒ C1）
  ✅ K9 所鄰二以上而其一為本街廓 ⇒ 本街廓之宗（X ⇒ X9）
  ✅ K10 所鄰為零而經同一地主之道路片臨道路另一側之配得街廓 ⇒ 併入該側之宗（Y、D1 ⇒ A1）
  ✅ K11 所鄰為零而無同一地主之道路片相鄰 ⇒ 第 5 項之輪（Y ⇒ A1）
  ✅ K12 所鄰為零而本街廓另有已配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Z）
  ✅ K13 二受併宗之一於現態未保留 ⇒ 停機（取得即鎖定·⛔ 還原）
  ✅ K14 公設片平分，每街廓之一份由擇定之一宗整份承受（P ⇒ A1／S3）
  ✅ K15 承受之宗唯一者⛔ 須 G
  ✅ K16 須擇而 alloc_state 未回 G ⇒ 停機
  ✅ K17 相鄰以宗連同其於本段整筆併入之片判之（P5 ⇒ A1）
  ✅ K18 經道路片而臨者隨該道路片之受者（Y、D1 ⇒ K；D9 ⇒ A1）
  ✅ K19 道路片之端所臨之街廓⛔ 為道路之另一側（Y ⇒ A1·⛔ E1）
  ✅ K20 本街廓有同一地主之他群之配得之宗 ⇒ 第 5 項·本街廓先（Y ⇒ Q）
  ✅ K21 所鄰為零而依第 5 項者其來源量為整筆、整筆併出（A1 130·Y 出 build）
  ✅ K22 重劃前面積扣段三部分併出（D1 ⇒ A1）
  ✅ K23 重劃前面積扣同一試算之入池閘之帳（D1 ⇒ A1）
  ✅ K24 經道路片之判以該建地與道路片共邊為準（Y ⇒ 第 5 項；Y2 ⇒ A1）
  ✅ K25 已為街角之合併所併出之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ E1）
  ✅ K26 同一街廓經二道路片而其受者異 ⇒ `k967_rank`（Y ⇒ K）
  ✅ K27 經道路片而臨二側 ⇒ 各側以其經道路片之受者比（Y ⇒ F1）
  ✅ K28 穿越之道路片⛔ 經之（Y ⇒ 第 5 項 ⇒ A1；C ⇒ (c)）
  ✅ K29 近半、遠半皆臨之街廓（路衝）⛔ 為道路之另一側（Y ⇒ 第 5 項 ⇒ E1；D1 ⇒ (b) E1）
  ✅ K30 第 5 項之本街廓之同一地主之配得之宗二以上 ⇒ 應分配面積大者（Y ⇒ Q·⛔ 近之 Q2）
  ✅ K31 路衝之扣以道路片為單位（Y ⇒ 經 D5 ⇒ E2）
  ✅ P0 逐項擾動恰該項紅 31／31
⇒ 紅 []；rc 0
````

### `#66`　`python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`（`rc 0`·`stderr` `0` B）

````text
── 接線（工作樹之 app.py 對基準 fd88f64）──
  ✅ X1 四停機之字樣皆去（殘 []）
  ✅ X2 `_recv_of(b, y)` 之形與其 5 呼叫皆二引數
  ✅ X3 頂層之相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X4 ⛔ 案件字面（[]）
  ✅ X5 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#69`　`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ K1 程式之停機：回 RuntimeError·登記全文（⛔ 截）
  ✅ K2 ⛔ 帶號 ⇒ 停機、⛔ 登記
  ✅ K3 號之邊界（前接英數或連字號者⛔ 號；無數字者⛔ 號）
  ✅ K4 新登記 零／一／二 ⇒ ⛔ 拋／拋其全文／拋其首者
  ✅ K5 巢狀之試算以長度分之
  ✅ K6 入池閘之併入後之試算立程式之停機 ⇒ 上拋
  ✅ K7 對照：配地中止（⛔ 帶號）⇒ 照舊為不過
  ✅ K8 基底（無停機）：X 依手冊併入街角第 1 宗 C
  ✅ K9 換名：K6／K7／K8 之果除名稱外同
  ✅ K10 鏡射：K6／K7／K8 之果除名稱外同
  ✅ K11 旋轉 37°·TWD97：K6／K7／K8 之果除名稱外同
  ✅ K12 鏡射 ＋ 旋轉 213°·TWD97·換名：K6／K7／K8 之果除名稱外同
  ✅ K13 末端塊合併再試之試算立程式之停機 ⇒ 上拋
  ✅ K14 對照：末端塊之試算之配地中止 ⇒ 照舊記試算中止
  ✅ K15 試算之前之登記⛔ 波及（K7 於 K1〜K5 之登記之後）
  ✅ K16 上拋之訊息為全文（號在 1500 字之後）
  ✅ P0 判式自驗 16／16
⇒ 紅 []；rc 0
````

### `#70`　`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 11（基準之帶號 10·k980_acq_check 1·end_block_apply 0）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'rw_pct_2dp', 'rw_width_mm']／去 []／相異 ['_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'iterate_G_S', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12', 'solve_G_binary']／不合 ['end_block_merge_run：刪列非 raise RuntimeError：[\'      建地之片之他街廓之候選依五級與深度再排·見其 docstring）。"""\', \'    _dup = {p: tg for p, tg in _cand_of.items() if len(tg) >= 2}\']']）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
````

### `#71`　`python3 verify/probes/probe_WG9389_trialstop.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
````

### `#72`　`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ L1 合併再試（①）所得之宗⛔ 保留 ⇒ 停機（⛔ 還原）
  ✅ L2 經道路片（②）所得者⛔ 保留 ⇒ 停機
  ✅ L3 二端皆⛔ 保留 ⇒ 停機（訊息具二者）
  ✅ L4 先成者保留而後成之右端者⛔ 保留 ⇒ 停機（訊息具後者、⛔ 具保留者）
  ✅ L5 競合（題二）之所取之一端⛔ 保留 ⇒ 停機
  ✅ L6 競合（題一·切半二端各配一宗）而皆⛔ 保留 ⇒ 停機
  ✅ L7 皆保留 ⇒ 同改前、鎖定之宗受併入、試算 3（步驟 10 沿用其查之試算）
  ✅ L8 有成者而該群無待後處理之土地 ⇒ 仍查（試算 1）
  ✅ L9 查之試算中止 ⇒ 停機（無從判定）
  ✅ L10 無成者 ⇒ ⛔ 查（試算 0）
  ✅ L11 L7 之換名、左右鏡射、旋轉並移至 TWD97 之尺度 ⇒ 同 L7
  ✅ L12 成者皆保留而非成者之宗⛔ 保留 ⇒ ⛔ 停機
  ✅ L13 紀錄⛔ 含回原狀之列
  ✅ L14 題一 4 之照配（後處理之成）⛔ 為鎖定之受詞 ⇒ ⛔ 停機
  ✅ P0 判式自驗 14／14
⇒ 紅 []；rc 0
````

### `#73`　`python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302`（`rc 0`·`stderr` `0` B）

````text
── 接線（工作樹之 app.py 對基準 2aa6302）──
  ✅ X1 舊停機之字樣去之（殘 0）、還原之字樣去之（{'回原狀': 0, '還原後仍出現': 0}）、鎖定之查之字樣 3（期 ≥ 1）
  ✅ X2 頂層之相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'end_block_apply', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'end_block_trial_G', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'select_corner_lots_both_sides_v12', 'solve_G_binary']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X3 ⛔ 案件字面（[]）
  ✅ X4 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#74`　`python3 verify/probes/probe_WG9390_k961r.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 1·回原狀之列 0·其檢核 0·段三之成者 3·G 值列 35）
  ✅ R1@0.0：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 0·回原狀之列 0·其檢核 0·段三之成者 0·G 值列 36）
  ✅ R0 諸退縮之段三之成者之和 3（[3, 0]·期 ≥ 1·其查已行）
⇒ 紅 []；rc 0
````

### `#75`　`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ C1 未輸入 ⇒ 100.5
  ✅ C2 輸入 0 ⇒ 逐位同 C1
  ✅ C3 輸入 100 ⇒ 逐位同 C1
  ✅ C4 輸入恰 100.5 ⇒ 逐位同 C1
  ✅ C5 輸入 150 ⇒ 面積∈[150,150.01]·遠側 x＝5.15·∥SIDE_LINE·含 C1
  ✅ C6 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ C7 輸入 −1 ⇒ 停機
  ✅ C8 C5 之旋轉 37°·鏡射·TWD97 ⇒ 面積同 C5
  ✅ C9 側街斜交（∦ 宗地分配線）輸入 200 ⇒ 面積∈[200,200.01]·遠側界線 ∥ SIDE_LINE（Δx＝6）
  ✅ E1 未輸入 ⇒ R_end 255·內側界 13.5（buf 3.5）
  ✅ E2 輸入恰 255 ⇒ 逐位同 E1
  ✅ E3 輸入 300 ⇒ R_end∈[300,300.01]·內側界 x＝15
  ✅ E4 輸入 2000 ⇒ 停機（K-9-80 ⑥）
  ✅ E5 E3 之旋轉·鏡射·TWD97 ⇒ R_end 同 E3
  ✅ E6 _end_region_R 之未輸入與 0 ⇒ R_end 逐位同（255）；end_block_band_width 之 0 ⇒ 停機
  ✅ T1 距 0.02 ⇒ ⛔ 停
  ✅ T2 距恰 0.01 ⇒ 停
  ✅ T3 距 0.005 ⇒ 停
  ✅ T4 重疊 ⇒ 停（訊息具二範圍之名）
  ✅ T5 唯一範圍或含 None ⇒ ⛔ 停
  ✅ T6 三範圍而唯其中二者相接 ⇒ 停
  ✅ K1 有效值之序（K-9-1 ⑨）：街廓覆寫 → 分區底 → 0；session 無鍵或 None ⇒ 0
  ✅ P0 判式自驗 22／22
⇒ 紅 []；rc 0
````

### `#76`　`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`（`rc 0`·`stderr` `0` B）

````text
── 接線（工作樹對基準 a8657c4）──
  ✅ W1 _build_corner_range_v3 之呼叫 4（期 ≥ 4）皆傳 min_build_area：皆傳
  ✅ W2 諸呼叫之數 [('end_block_side_geom', 1), ('end_block_host', 2), ('_place_pool_parcels', 2)]（期 ≥ 1、≥ 2、≥ 2）皆傳 min_build_area：皆傳
  ✅ W3 末端帶之單一真相源 {'_place_pool_parcels→_end_region_R': 1, '_place_pool_parcels→_end_band': 0, '_end_region_R→end_block_band_width': 1, 'end_block_band_width 之呼叫（全檔）': 1}（期 1、0、1、1）
  ✅ W4 min_build_area 之值皆為 k980_mba（呼叫 8·期 ≥ 8·不合 []）、v12 之 _mba_pk 之賦值 True、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（4／基準 4）、k980_mba 之分區之引數為字面者 []（期無）
  ✅ W5 k980_range_touch_check 之呼叫 [('select_corner_lots_both_sides_v12', 1), ('f3_screen_stepg_run', 1), ('stepg:_run_step_g_impl', 1)]·app.py 全檔 2（期各 1·app.py 全 2）、其範圍之名齊全 [True, True, True]（期三真）
  ✅ W6 頂層之名之增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', 'end_block_band_width', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_trial_G', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'rw_pct_2dp', 'rw_width_mm']（期 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']）、減 []
  ✅ W7 新增或改之頂層節點（43）內新增之案件字面 []
  ✅ W8 逐層照傳 min_build_area 皆照傳
  ✅ W9 引擎經 ns 取之新名 ['k980_mba', 'k980_range_touch_check'] ⊆ _WF_NS_NAMES（漏 []）
⇒ 紅 []；rc 0
````

### `#77`　`python3 verify/probes/probe_WG9391_k980x.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@3.5 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}·不合 []）
  ✅ R1@0.0 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@0.0 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 124.94, 'R2': 164.49, 'R3': 163.8, 'R4': 126.08, 'R5': 177.54, 'R6': 262.28}·不合 []）
⇒ 紅 []；rc 0
````

### `#78`　`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ G1 D 15·l₂ 6：二上界 × 二座標系之 G ＝ round(G*, 2)
  ✅ G2 D 25·l₂ 2：同 G1
  ✅ G3 邊界：G* 於半分之上 2e-5 ⇒ 進、之下 2e-5 ⇒ 捨（四解皆同）
  ✅ G4 常數：K980_G_TOL ≤ 1e-6、K980_G_MAX_ITER ≥ 100
  ✅ H1 二值同 ⇒ 過（回 None·登記⛔ 增）
  ✅ H2 二值異 ⇒ 停（GB-206·K-9-80 ③·宗·二值·登記增恰一而全文同）
  ✅ H3 取至 2 位同 ⇒ 過
  ✅ H4 取至 2 位恰差 0.01 ⇒ 停
  ✅ H5 末端塊·右 ⇒ 停（訊息含末端塊、right）
  ✅ E1 左端之引數
  ✅ E2 右端：方向 −d̂、起點 p1 ＋ S·d̂
  ✅ E3 S ＝ 0.05 ⇒ 上界 0.1
  ✅ E4 側別非 left／right ⇒ 停機
  ✅ E5 回 (G, S_raw)
  ✅ J1 右側之街角第 1 宗：評選之式 ＝ 實配之鏈首（SIDE_LINE 偏 δ·二座標系·二 a）
  ✅ J2 左側之街角第 1 宗：同 J1
  ✅ J3 判別之前提：比之數 40·δ 0.3 之幾何之起算點異其 G
  ℹ️ G1 量 290·略 10；G2 量 288·略 12
  ✅ P0 判式自驗 17／17
⇒ 紅 []；rc 0
````

### `#79`　`python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 _solve_G_one 之 solve_G_binary 以 K980_G_TOL／K980_G_MAX_ITER（呼叫 1·全檔 1）
  ✅ W2 取得之宗之自我檢查之四處（[('app.py', 4), ('verify/stepg_pipeline.py', 4)]）
  ✅ W3 end_block_host 之評選經 end_block_trial_G（1）·solve_one 之直呼 0
  ✅ W4 引擎經 ns 取之新名 ['end_block_trial_G', 'k980_acq_check'] ⊆ _WF_NS_NAMES（漏 []）
  ✅ W5 頂層之名之增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'RW_TABLE_25', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_trial_G', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'k980_acq_check', 'rw_pct_2dp', 'rw_width_mm']·減 []
  ✅ W6 k980_acq_check 經 k6_program_stop 立 GB-206 之停機
  ✅ W7 新增或改之頂層節點（36）內新增之案件字面 []
  ✅ W8 _corner_first_lot_G 之 _solve_G_one 以 is_corner=True、w0_start=0.0（呼叫 1）
⇒ 紅 []；rc 0
````

### `#80`　`python3 verify/probes/probe_WG9392_k980g.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 自我檢查 567 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@3.5 本案之錨（KL 05:22 所核之甲）不合 []
  ✅ R1@0.0 自我檢查 432 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@0.0 本案之錨（KL 05:22 所核之甲）不合 []
⇒ 紅 []；rc 0
````

### `#81`　`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ T1 左端無三角地 ⇒ 末端塊（R_end ＝ 末端帶 105·s_back 0·buf 3.5）
  ✅ T2 右端無三角地 ⇒ 同 T1
  ✅ T3a 門檻之下：三角地 0.0005 ㎡ ⇒ 無三角地之讀（s_back 0·R_end ＝ 末端帶）
  ✅ T3b 門檻之下：三角地 0.000999 ㎡ ⇒ 無三角地之讀（s_back 0·R_end ＝ 末端帶）
  ✅ T4a 門檻之上：三角地 0.001001 ㎡ ⇒ 有三角地（s_back ＝ δ·R_end − 末端帶 ＝ 未臨正街）
  ✅ T4b 門檻之上：三角地 0.002 ㎡ ⇒ 有三角地（s_back ＝ δ·R_end − 末端帶 ＝ 未臨正街）
  ✅ T5 有三角地（外斜 3 m）⇒ 舊之形（未臨正街 45·s_back 3·R_end 150·末端帶 105）
  ✅ T6 端之界線內斜（後緣較短）⇒ 末端塊（R_end ＝ 末端帶 ＝ 75）
  ✅ T7 最小建築面積 150 ⇒ R_end ＝ 末端帶 ∈ [150, 150＋容差]·帶寬 5
  ✅ T8 鏡射、旋轉 37°、TWD97 之尺度 ⇒ T1／T2／T6／T7 之量同
  ✅ T9 end_block_apply：左無側街 ⇒ 左觸發·R_end 105·當選 B(1)（A 未達）·落位首；右有側街 ⇒ 無紀錄
  ✅ T9b 二端皆無側街 ⇒ 二端皆觸發（右：E(1) 未達、D(1) 當選而移至末）
  ✅ T12 二端皆無側街而一筆同時跨占二端之 R_end（長 20·A 寬 18）⇒ 過（右之 B(1) 先當選·A(1) 歸左·W-G.9-395）
  ✅ T12b 一宗之街廓（長 20）⇒ A(1) 歸左；右除之重選而無他宗·⛔ 准強制 ⇒ 停（各筆單獨試算皆未達·right·登記⛔ 增）
  ✅ T12c 長 20 而無一筆同時跨占（A 寬 10、B 寬 10）⇒ 過（二端各當選）
  ✅ T10 末端保留（無三角地）：左無側街 ⇒ 池窗起點 0 → 3.5；有側街 ⇒ 0
  ✅ T10b 末端保留（無三角地）：右無側街 ⇒ 池窗寬 40 → 36.5；有側街 ⇒ 40
  ✅ T11 短街廓（長 6）二端之末端帶相疊 ⇒ 停機（K-9-80 ⑥）；長 40 ⇒ 過
⇒ 紅 []；rc 0
````

### `#82`　`python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 end_block_side_geom 之 'gate': False 之回傳 0
  ✅ W2 _place_pool_parcels 之「_unfront 之判 ⇒ continue」0·引 END_BLOCK_UNFRONT_EPS True·寫死 1e-3 0
  ✅ W3 _end_region_R／end_block_band_width 之「frag_poly 空」之停機 []
  ✅ W4 end_block_apply 之 'gate' 之字面 0
  ✅ W5 頂層之名之增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'RW_TABLE_25', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'rw_pct_2dp', 'rw_width_mm']·減 []·相異之節點 ['_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'end_block_side_geom', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'main', 'rw_from_width', 'solve_G_binary']
  ✅ W6 新增或改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 ['verify/stepg_pipeline.py']
  ✅ W8 END_BLOCK_UNFRONT_EPS ＝ 0.001
  ✅ W9 end_block_apply 之 `raise k6_program_stop(…GB-207…)` 0（期 0·W-G.9-395 去之）
⇒ 紅 []；rc 0
````

### `#83`　`python3 verify/probes/probe_WG9393_endall.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 末端塊之紀錄：觸發 [('R2', 'right'), ('R3', 'left'), ('R5', 'right'), ('R6', 'left')]·未觸發 []
  ✅ R2@3.5 R_end 之錨不合 []
  ✅ R3@3.5 當選者之錨不合 []
  ✅ R4@3.5 觸發之端之鏈首 ＝ 當選者（不合 []·err None）
  ✅ R1@0.0 末端塊之紀錄：觸發 [('R2', 'right'), ('R3', 'left'), ('R5', 'right'), ('R6', 'left')]·未觸發 []
  ✅ R2@0.0 R_end 之錨不合 []
  ✅ R3@0.0 當選者之錨不合 []
  ✅ R4@0.0 觸發之端之鏈首 ＝ 當選者（不合 []·err None）
⇒ 紅 []；rc 0
````

### `#84`　`python3 verify/probes/probe_WG9352_endblock.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
══ 退縮 3.5 ══
  ✅ R1 R2 right：未臨正街 0.00＋末端帶 154.49＝R_end 154.49（紀錄 0.0／154.49／154.49）
  ✅ R2 R2 right：候選與試算 [('628-34(1)', '當選', 601.64)] ＝ 外部錨 [('628-34(1)', '當選', 601.64)]
  ✅ R3 R2 right：鏈首宗 628-34(1)（G 601.64·試算 601.64）⊇ R_end（差 0.000000）
  ✅ R4 R2 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R2：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R3 left：未臨正街 0.00＋末端帶 153.77＝R_end 153.77（紀錄 0.0／153.77／153.77）
  ✅ R2 R3 left：候選與試算 [('628-34(2)', '當選', 257.91)] ＝ 外部錨 [('628-34(2)', '當選', 257.91)]
  ✅ R3 R3 left：鏈首宗 628-34(2)（G 257.91·試算 257.91）⊇ R_end（差 0.000000）
  ✅ R4 R3 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R3：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R5 right：未臨正街 0.00＋末端帶 167.54＝R_end 167.54（紀錄 0.0／167.54／167.54）
  ✅ R2 R5 right：候選與試算 [('628-23(2)', '當選', 430.68)] ＝ 外部錨 [('628-23(2)', '當選', 430.68)]
  ✅ R3 R5 right：鏈首宗 628-23(2)（G 430.68·試算 430.68）⊇ R_end（差 0.000000）
  ✅ R4 R5 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R5：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R6 left：未臨正街 85.71＋末端帶 166.57＝R_end 252.28（紀錄 85.71／166.57／252.28）
  ✅ R2 R6 left：候選與試算 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)] ＝ 外部錨 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)]
  ✅ R3 R6 left：鏈首宗 628-4(1)（G 779.93·試算 779.93）⊇ R_end（差 0.000000）
  ✅ R4 R6 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R6：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
══ 退縮 0.0 ══
  ✅ R1 R2 right：未臨正街 0.00＋末端帶 154.49＝R_end 154.49（紀錄 0.0／154.49／154.49）
  ✅ R2 R2 right：候選與試算 [('628-34(1)', '當選', 601.64)] ＝ 外部錨 [('628-34(1)', '當選', 601.64)]
  ✅ R3 R2 right：鏈首宗 628-34(1)（G 601.64·試算 601.64）⊇ R_end（差 0.000000）
  ✅ R4 R2 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R2：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R3 left：未臨正街 0.00＋末端帶 153.77＝R_end 153.77（紀錄 0.0／153.77／153.77）
  ✅ R2 R3 left：候選與試算 [('628-34(2)', '當選', 257.91)] ＝ 外部錨 [('628-34(2)', '當選', 257.91)]
  ✅ R3 R3 left：鏈首宗 628-34(2)（G 257.91·試算 257.91）⊇ R_end（差 0.000000）
  ✅ R4 R3 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R3：宗地與抵費地之聯集 △ 街廓 0.0001 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R5 right：未臨正街 0.00＋末端帶 167.54＝R_end 167.54（紀錄 0.0／167.54／167.54）
  ✅ R2 R5 right：候選與試算 [('628-23(2)', '當選', 430.68)] ＝ 外部錨 [('628-23(2)', '當選', 430.68)]
  ✅ R3 R5 right：鏈首宗 628-23(2)（G 430.68·試算 430.68）⊇ R_end（差 0.000000）
  ✅ R4 R5 right：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R5：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
  ✅ R1 R6 left：未臨正街 85.71＋末端帶 166.57＝R_end 252.28（紀錄 85.71／166.57／252.28）
  ✅ R2 R6 left：候選與試算 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)] ＝ 外部錨 [('628-23(1)', '未達', 73.76), ('628-4(1)', '當選', 779.93)]
  ✅ R3 R6 left：鏈首宗 628-4(1)（G 779.93·試算 779.93）⊇ R_end（差 0.000000）
  ✅ R4 R6 left：抵費地 ∩ 未臨正街 ＝ 0.000000 ㎡
  ✅ R5 R6：宗地與抵費地之聯集 △ 街廓 0.0000 ㎡、兩兩疊 0.0000 ㎡
⇒ 紅 []；rc 0
````

### `#85`　`python3 verify/probes/probe_WG9394_k9615.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ T1 新登記唯 GB-205 ⇒ None
  ✅ T1b 新登記唯 GB-205 而 adopted ⇒ 上拋 GB-205
  ✅ T1c adopted 而無新登記 ⇒ None
  ✅ T2 GB-205 繼以 GB-104 ⇒ 上拋 GB-104
  ✅ T3 GB-104 繼以 GB-205 ⇒ 上拋 GB-104
  ✅ T4 GB-2050 ⇒ 上拋
  ✅ T5 【未裁】⇒ 上拋
  ✅ T6 無新登記 ⇒ None
  ✅ T7 mark 之前之登記⛔ 計 ⇒ None
  ✅ T8 入池閘之 GB-205 於候選之試算之殼 ⇒ 中止之訊息含 GB-205·登記增一·殼⛔ 上拋
  ✅ T9 段三：A1(1) 之 ② 之併入後之試算以 GB-205 中止 ⇒ A1(1) 未成（不過）、B1(1) 成
  ✅ T9b 其中止為 GB-104 ⇒ 停機
  ✅ T9c 其中止無號 ⇒ 停機（無從判定·照舊）
  ✅ T9d 併入前之試算以 GB-205 中止 ⇒ 停機（無從判定）
  ✅ T9e 併入前、後之試算皆以 GB-205 中止 ⇒ 停機（無從判定·⛔ 判為不過）
  ✅ T10 末端塊合併再試之現態之試算以 GB-205 中止 ⇒ 停機
  ✅ T10b 其中止無號 ⇒ 記試算中止而回（照舊）
  ✅ T11 T9 之換名、鏡射、旋轉 37°、TWD97 ⇒ 同 T9
  ✅ T12 題一 4 之「連同其半併入已取得之一端」之試算以 GB-205 中止 ⇒ 不過 ⇒ K-9-66 按比例（⛔ 停機）
  ✅ T12b T12 之換名、鏡射、旋轉 37°、TWD97 ⇒ 同 T12
  ✅ T13 段三後處理 (b) 之道路片之併入以 GB-205 中止 ⇒ 不過 ⇒ K-9-66 按比例 20
  ✅ T13b 觸發 ＝ G ＞ 200（全併恰在門檻上）⇒ 全併 40
  ✅ T13c 觸發 ＝ G ＞ 160（任一格即觸）⇒ 未成
  ✅ T14 手冊先行之候選之併入後之試算以 GB-205 中止 ⇒ 不過 ⇒ K-9-66（＝ F27 K16 之形·⛔ 停機）
⇒ 紅 []；rc 0
````

### `#86`　`python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 頂層之名之增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'RW_TABLE_25', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'rw_pct_2dp', 'rw_width_mm']·減 []·相異之節點 ['end_block_apply', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'f3_screen_stepg_run', 'iterate_G_S', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'main', 'rw_from_width', 'solve_G_binary']
  ✅ W2 k6_trial_raise_since 內之號之字面 ['GB-205']
  ✅ W3 _noaff 之二試算之間之 mark 與「新登記 ⇒ return False」（_noaff 有）
  ✅ W4 end_block_merge_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W8 k953_manual_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W5 k929_6_fixpoint 之 `raise k6_program_stop(…GB-205…)` 1（期 1）·對基準⛔ 變 True
  ✅ W6 所改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 ['verify/stepg_pipeline.py']
⇒ 紅 []；rc 0
````

### `#87`　`python3 verify/probes/probe_WG9394_k9615.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@3.5 受併宗 25·最後之配地⛔ 保留者 []
  ✅ R1@0.0 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@0.0 受併宗 26·最後之配地⛔ 保留者 []
⇒ 紅 []；rc 0
````

### `#88`　`python3 verify/probes/probe_WG9395_k960.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
── 甲 end_block_apply（K-9-60 ①）──
  ✅ T1 X 跨二端（交 左 45／右 75）而唯左拿得下 ⇒ X 歸左、右強制、右之 X「歸他端」
  ✅ T2 二端皆拿得下、右交大（45／75）⇒ 歸右；左除 X 重選 ⇒ 強制
  ✅ T3 二端皆拿得下、交相等（75／75）⇒ 歸左（p1 側）
  ✅ T4 二端皆拿得下、左交大（75／45）⇒ 歸左
  ✅ T5 二端皆拿不下 ⇒ 二端皆強制·X 之列皆「未達」
  ✅ T6 左之 A 先當選（X 未試）、右 X 當選 ⇒ 二端各一
  ✅ T7 一宗之街廓·准強制 ⇒ X 歸左、右強制
  ✅ T7b 一宗之街廓·⛔ 准強制 ⇒ 停機（訊息含「各筆單獨試算皆未達」與 right）
  ✅ T8 同一原地號之二片：X(1) 歸右（交 25／35）；左重選 ⇒ X(2)（⛔ 以原地號除）；右之 X(2)「歸他端」
  ✅ T9 換名·旋轉 37°·鏡射·TWD97 ⇒ T1〜T4、T8 同
  ✅ T10 左右互換（FRONT 反向）⇒ T1、T2、T8 之結果（譯回原向）同；T3 之並列歸 p1（原向之右）
  ✅ T11 無同時跨占（長 40·A [0,10]、C [10,30]、B [30,40]）⇒ 二端各當選、「歸他端」0
── 乙 end_block_merge_run（K-9-60 ①③·取得即鎖定）──
  ✅ U1 一筆 Z1 為二端之未達候選 ⇒ 題二之競合：二端皆以 Z2 拿得下、右交大 ⇒ 歸右、左皆未達
  ✅ U2 取得即鎖定：右之當選 Z2 與左之未達候選 Z1 同群相連 ⇒ 左⛔ 併 Z2 ⇒ 左皆未達
  ✅ V0 一端屬二競合而順序一致（E、F 皆丁先）⇒ 依原位次：丁得 E（整片）、戊得 F（整片）
  ✅ V1 順序相反 ⇒ 互相等待 ⇒ 評選指數（戊於二端皆第 1 名）⇒ 戊先：戊得 E、F 強制
  ✅ V2 戊於二端皆第 1 名（G 之和 戊 72、最大之一片 丁 50）⇒ 戊先
  ✅ V3 各一端第 1 名 ⇒ 面積（共同之端之片之重劃前面積）大者（戊 72 ＞ 丁 62·道路片⛔ 計）先：戊得 E、丁得 F
  ✅ V4 各一端第 1 名、面積與指數之和皆相等 ⇒ 最小之暫編地號小者（D1(1)）先：丁得 E、戊得 F
  ✅ V5 三位地主互相等待成環（G 之和 丁 40／戊 60／己 50·評選指數兩兩亦戊先）⇒ 戊先、其餘依原位次（己、丁）
  ✅ V6 換名（街廓名之序反之·地號改名）⇒ V1 之結果除名稱外同（逐列之集·定案之端·皆未達）
  ✅ V7 互相等待而先處理者（丁·於二端皆第 1 名）在 F 端之前尚有第三人庚 ⇒ 庚照原位次先試而得 F；丁之競合消滅、丁得 E
  ✅ V8 環成即處理：V1 之環成於 F 端之末列，其後之他街廓之列（T）於其處理之後
  ✅ V9 夥伴之列已被延後過（E 戊己丁·F 丁己戊·G 戊 60／己 50／丁 40）⇒ 依其現位而退、⛔ 無限迴圈
  ✅ V10 二首列退至同一夥伴之列之後而退之先後與原位次相反（E 己丁戊·F 丁戊己）⇒ 依原位次（J1 先於 D1）
  ✅ V11 退至已被延後之夥伴之列（J1）之緊後（E 丁己辛戊·F 戊辛己丁·G 戊 80／己 70／丁 60／辛 50）⇒ D1 先於 K1
  ✅ V13 被延後者之夥伴之列其後自身又被延後（E 己辛戊丁·F 戊己丁辛·G 丁 90／辛 50／戊 30／己 20）⇒ 己之 J1 隨戊之 U1 而移
  ✅ V12 換名與換端：V11 之街廓改名（A7、B2·序同）、地號改名、二端皆為右端 ⇒ 除名稱外同 V11
⇒ 紅 []；rc 0
````

### `#89`　`python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 end_block_apply 內⛔ 有 GB-207 之字面、⛔ 有 k6_program_stop 之呼叫
  ✅ W2 end_block_merge_run：⛔ 有「同時跨占二以上末端塊」「屬二以上之競合」之停機；仍有「三個以上之末端塊」之停機
  ✅ W3 _k950_rows：⛔ 有「屬二以上之競合」之停機、仍有「列數 ≠ 2」之停機
  ✅ W4 頂層之名之增減 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'RW_TABLE_25', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'rw_pct_2dp', 'rw_width_mm']（期 []）；頂層節點之相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'RW_TABLE_25', 'end_block_apply', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'f3_screen_stepg_run', 'iterate_G_S', 'k6b_stage3_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'solve_G_binary']（期 ['end_block_apply', 'end_block_merge_run', 'k6b_stage3_run']）
  ✅ W5 所改之三節點內新增案件字面 []（期 []）
  ✅ W6 verify/ 頂層之 *.py 對基準相異 ['verify/stepg_pipeline.py']（期 []）
⇒ 紅 []；rc 0
````

### `#90`　`python3 verify/probes/probe_WG9395_k960.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ R1@3.5 觸發之端 4（期 4）、有當選 4（期 4）、「歸他端」之列 []（期 []）、err None
  ✅ R2@3.5 合併再試之標的 []（期 []）、競合 None（期 無）
  ✅ R1@0.0 觸發之端 4（期 4）、有當選 4（期 4）、「歸他端」之列 []（期 []）、err None
  ✅ R2@0.0 合併再試之標的 []（期 []）、競合 None（期 無）
⇒ 紅 []；rc 0
````

### `#92`　`python3 verify/probes/probe_WG9398_rw25.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ T1 格點 171（1.0〜18.0 m 每 0.1 m）＝ 附表 25
  ✅ T2 格間 170 × 3 處 ＝ 二端之線性內插（公分以下用內插法）
  ✅ T2′ 格間 170 × 3 處 ＝ hb_Rq（公釐值）
  ✅ T3 請示表：5.30 ⇒ 45.85、5.35 ⇒ 46.15、7.00 ⇒ 55.69
  ✅ T4 起點 0 與 0〜1 m（自 (0, 0) 至 (1.0, 17.36) 線性）
  ✅ T5 飽和：≥ 18 m ＝ 100；17.95 ⇒ 99.875
  ✅ T6 格點之浮點之鄰（5.3 ± 1e-12、0.1×53、2.7＋2.6）⇒ 45.85
  ✅ T7 0〜18.5 m 每 0.0007 m：不減、相鄰之差 ≤ 0.02
  ✅ T7′ 0〜18.5 m 每 0.0007 m ＝ hb_Rq（逐點）·不減·相鄰之差 ≤ 0.0174
  ✅ T8 累積差額之鏈 0→4.2→9.7→13.05→18.3 與倒退
  ✅ T9 玩具街廓之街角第 1、2 宗（左右 × 二座標系 × 二 a）＝ HB 之自解；舊表之自解至少一異；自解距半分 ≥ 0.001
  ✅ T9′ 同上（第 2 宗起於第 1 宗之寬之公釐值·hb_Rq）：自解之寬距半公釐之跳 ≥ 1e-4 m
  ✅ T10 公釐之四捨五入（十例·十進位·二進位之 round 異者七）＝ hb_Rq
  ✅ T11 回傳之 W ＝ W_far ＝ q(W_far_raw)·W_near 公釐·Rw_pct ＝ 十進位四捨五入
  ✅ T12 跳處（甲）：1／4 ⇒ 進、3／4 ⇒ 捨（G 與 Rw_pct、W_far、jump398、converged）·左右 × 二座標系
  ✅ T13 非有限值 ⇒ ValueError；rw_pct_2dp(22.214999999999996) ＝ 22.22
  ℹ️ T9 之解（HB）[48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14]
  ℹ️ T9 之解（舊表）[48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16]
  ✅ P0 判式自驗 16／16
⇒ 紅 []；rc 0
````

### `#93`　`python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf`（`rc 0`·`stderr` `0` B）

````text
  ✅ X1 頂層之名之增 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'RW_TABLE_25', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'rw_pct_2dp', 'rw_width_mm']·減 []·相異之節點 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'RW_TABLE_25', 'end_block_apply', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'f3_screen_stepg_run', 'iterate_G_S', 'k6b_stage3_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank', 'main', 'rw_from_width', 'rw_pct_2dp', 'rw_width_mm', 'solve_G_binary']
  ✅ X2 RW_TABLE_25 ＝ 17 × 10 之字面而逐格 ＝ 附表 25（列 17）
  ✅ X3 rw_from_width 讀 RW_TABLE_25／RW_SATURATION_WIDTH_M·其內表之值之數之常數 []
  ✅ X4 rw_increment、RW_SATURATION_WIDTH_M 之節點⛔ 變
  ✅ X5 RW_TABLE_25 以外之表之數之串（生產碼 34 檔）[]
  ✅ X6 新增或改之頂層節點內新增之案件字面 []
  ✅ X7′ verify/ 頂層之 *.py 對基準之相異 ['verify/stepg_pipeline.py']·其差之列 2
  ✅ X8 分配計算表之 W(m)：二列 round(…, 3)·畫面之格式 '{:.3f}'
  ✅ X9 回傳之 W／W_far／W_near 經 rw_width_mm·Rw_pct 經 rw_pct_2dp []
⇒ 紅 []；rc 0
````

### `#95`　`python3 verify/probes/probe_WG9399_k960x.py selftest <repo>`（`rc 0`·`stderr` `0` B）

````text
  ✅ 甲 E1 矩形·左之端線長 30
  ✅ 甲 E1′ 矩形·右之端線長 30
  ✅ 甲 E1″ 矩形·左之 R_end 105
  ✅ 甲 E2 左之未臨正街三角 ⇒ √925
  ✅ 甲 E3 左端線內斜 ⇒ R_end 之端線長 13.5836（⛔ 全邊 31.0483）
  ✅ 甲 E4 左端線二折 ⇒ 2√229
  ✅ 甲 E5 右端有截角而 p2 為理論角 ⇒ 左仍 30
  ✅ 甲 E6 E1 旋轉 37°·鏡射·TWD97
  ✅ 甲 E6 E1 FRONT 反向
  ✅ 甲 E6 E2 旋轉 37°·鏡射·TWD97
  ✅ 甲 E6 E2 FRONT 反向
  ✅ 甲 E6 E3 旋轉 37°·鏡射·TWD97
  ✅ 甲 E6 E3 FRONT 反向
  ✅ 甲 E6 E4 旋轉 37°·鏡射·TWD97
  ✅ 甲 E6 E4 FRONT 反向
  ✅ 甲 E6 E1′ 旋轉 37°·鏡射·TWD97
  ✅ 甲 E6 E1′ FRONT 反向
  ✅ 甲 E7 BASELINE 未給 ⇒ end_segs／end_len 皆 None
  ✅ 甲 E8 該端點距外框 0.049 ⇒ 可
  ✅ 甲 E8′ 該端點距外框 0.051 ⇒ 停機
  ✅ 甲 E9 BASELINE 不觸外框 ⇒ 停機
  ✅ 甲 E10 BASELINE 過該端點 ⇒ 停機
  ✅ 甲 E11 偏 0.5° ⇒ 右 30（⛔ 33.5）
  ✅ 甲 E11 偏 0.5° ⇒ 左 30 − 10·tan0.5°
  ✅ 甲 E11′ 偏 0.5°·right·旋轉 37°·鏡射·TWD97
  ✅ 甲 E11′ 偏 0.5°·right·FRONT 反向
  ✅ 甲 E11′ 偏 0.5°·left·旋轉 37°·鏡射·TWD97
  ✅ 甲 E11′ 偏 0.5°·left·FRONT 反向
  ✅ 甲 E12 偏 −0.5° ⇒ 左 30
  ✅ 甲 E12 偏 −0.5° ⇒ 右 30 − 10·tan0.5°
  ✅ 甲 E13 偏 1.9°（未逾 2°）⇒ 右 30
  ✅ 甲 E13′ 偏 2.1°（逾 2°·依字面）⇒ 右 33.5
  ✅ 甲 E14 端之外框有與 BASELINE 平行而遠之折 ⇒ 端線 33（⛔ 止於其折）
  ✅ 甲 E15 BASELINE ∥ 屁股線而外移 0.049 ⇒ 30
  ✅ 甲 E15 BASELINE ∥ 屁股線而外移 0.051 ⇒ 停機
  ✅ 乙 P1 A 臨端線 30、指數 0.742857；X 0、0.257143
  ✅ 乙 P2 依深切分 ⇒ A1 10／0.333333、A2 20／0.666667
  ✅ 乙 P3 紀錄之端線(m) ＝ 30.0
  ✅ 乙 P4 旋轉 37°·鏡射·TWD97 ⇒ P1 之值同
  ✅ 乙 P5 未給 BASELINE ⇒ 列之臨端線、評選指數皆 None
  ✅ 乙 P6 條片 S 居端 ⇒ S 30／0.406857、A 0／0.593143
  ✅ 乙 P7 P6 之旋轉 37°·鏡射·TWD97 ⇒ 同
  ✅ 乙 P8 條片 0.9 ㎡（⛔ 跨占）⇒ A 30／0.994857
  ✅ 乙 P9 P6 之臨端線之和 30、指數之和 1.0（≤ 端線 30、≤ 1）
  ✅ 乙 P10 FRONT 之端點距外框 0.08 ⇒ 照行·端線 None·載其由·指數 None·結果與當選同未給 BASELINE
  ✅ 乙 P11 BASELINE 畫於屁股線外 0.08 ⇒ 同 P10
  ✅ 乙 P12 顯示：端線不可定 ⇒「端線 — m（無從定：」；可定 ⇒「端線 30.0 m；」
  ✅ 乙 P13 A 之刺寬 0.01 mm ⇒ A 0／0.589715、S 30／0.410286
  ✅ 乙 P14 A 之刺寬 0.03 mm ⇒ A 10／0.723049、S 20／0.276952
  ✅ 乙 P15 P13 之旋轉 37°·鏡射·TWD97 ⇒ 同
  ✅ 乙 P16 P14 之旋轉 37°·鏡射·TWD97 ⇒ 同
  ✅ 乙 P17 淺角楔形（0.5°）之尖屬原位次先之 W1 ⇒ W1 10／0.331334、W2 20／0.668666（⛔ W1 9.9、W2 20.1）
  ✅ 乙 P18 P17 之旋轉 37°·鏡射·TWD97 ⇒ 同
  ✅ 丙 R1 合併群合計（g1 0.3＋0.2 ＝ 0.5 ＞ B 0.45）
  ✅ 丙 R2 平手（4 位同 0.40001／0.40004）⇒ 首列先者先（⛔ 依暫編地號：z 在前）
  ✅ 丙 R3 非未達之列（歸街角側、歸他端）⛔ 計
  ✅ 丙 R4 無歸戶之片自成一單位（同群之 a、c 合計 0.5 ＞ 單 d 0.45）
  ✅ 丙 R5 未達之列之指數 None ⇒ 停機
  ✅ 丁 K1 有第 1 名者（X：1、3）先於皆無者（Y：2、2·名次和 4 ＝ X·面積 Y 大）
  ✅ 丁 K2 第 1 名之端數多者先（X 二端、Y 一端·面積 Y 大）
  ✅ 丁 K3 皆一端第 1 ⇒ 面積大者（Y 60 ＞ X 20）先
  ✅ 丁 K4 面積同（60）⇒ 指數之和大者（X 1.3 ＞ Y 0.6）先
  ✅ 丁 K5 皆同 ⇒ 暫編地號小者（x1）先（⛔ 置暫編地號於面積之前：y 面積大而後）
  ✅ 丁 K6 皆無第 1 名 ⇒ 名次之和小者（X 2＋2 ＜ Y 2＋3）先（⛔ 先比面積：Y 大）
  ✅ 丁 K7 唯計共同之端（X 於 G 第 1 而 G 非共同 ⇒ ⛔ 計；E、F 皆無第 1 ⇒ 名次和 X 6 ＞ Y 5 ⇒ Y 先）
  ✅ 丁 K8 同一片 x1 見於二共同之端 ⇒ 面積計一次（X 10 ＜ Y 15 ⇒ Y 先）
  ✅ 丁 K9 缺評選 ⇒ 停機
  ✅ 丁 K10 無共同之端 ⇒ 停機
  ✅ 戊 M1 V1 之地（G 之和 戊 81 ＞ 丁 63）而丁於二端皆第 1 ⇒ 丁先：丁得 E、戊得 F
  ✅ 戊 M2 V4 之地（G、重劃前面積皆同·丁之暫編地號小）而戊於二端皆第 1 ⇒ 戊先：戊得 E、F 皆未達
  ✅ 戊 M3 各一端第 1、G 同（72）、丁之重劃前面積 66 ＜ 戊 72 ⇒ 戊先
  ✅ 戊 M4 換名（街廓名之序反之·地號改名）⇒ M1 之結果除名稱外同
  ✅ 戊 M5 順序一致（E、F 皆丁先·⛔ 互相等待）而列無評選指數 ⇒ 照原位次（丁得 E、戊得 F）
  ✅ 戊 M6 互相等待而列無評選指數 ⇒ 停機
  ✅ 戊 M7 三位輪流互等·戊兩兩皆先（亦序鍵之先者）⇒ 戊先、其餘依原位次
  ✅ 戊 M8 三位輪流互等·丁兩兩皆先（序鍵之先者為戊）⇒ 丁先
  ✅ 戊 M9 三位輪流互等·兩兩比較成圈 ⇒ 序鍵之先者（戊）先（⛔ 依暫編地號）
  ✅ 戊 M10 互相等待而 BE 左之端線不可定 ⇒ 停機（載「端線無從定」）
  ✅ 戊 M11 順序一致（⛔ 互相等待）而 BE 左之端線不可定 ⇒ 照原位次（＝ M5）
  P0 判式自驗 79／79
⇒ 紅 []；rc 0
````

### `#96`　`python3 verify/probes/probe_WG9399_k960x.py wiring <repo> bd7da4d`（`rc 0`·`stderr` `0` B）

````text
  ✅ W1 新之頂層名 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank']（期 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank']）、去者 []（期 []）
  ✅ W2 頂層節點之相異 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'end_block_apply', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'k6b_stage3_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank']（期 ['END_BLOCK_IDX_W_AREA', 'END_BLOCK_IDX_W_LINE', 'END_BLOCK_LINE_TOL', 'end_block_apply', 'end_block_end_geom', 'end_block_end_line', 'end_block_end_segs', 'end_block_eval_rows', 'end_block_host', 'end_block_merge_run', 'end_block_pick', 'k6b_stage3_run', 'k960_idx_first', 'k960_idx_key', 'k960_idx_rank']）
  ✅ W3 `_ring395` 呼 k960_idx_first True、取 序鍵 True
  ✅ W4 `end_block_host` 取 f3_manual_baseline True、呼 _baseline_pts_from_manual True
  ✅ W5 所改、所增之節點內新增之案件字面 {}（期 {}）
  ✅ W6 verify/ 頂層之 *.py 對基準相異 []（期 []）
⇒ 紅 []；rc 0
````

### `#97`　`python3 verify/probes/probe_WG9399_k960x.py run <repo>`（`rc 0`·`stderr` `0` B）

````text
     R2 right：端線 44.12 m；列 [('628-34(1)', 10.42, 0.372619)]
     R3 left：端線 43.91 m；列 [('628-34(2)', 34.94, 0.799606)]
     R5 right：端線 47.95 m；列 [('628-23(2)', 0.0, 0.023134)]
     R6 left：端線 47.71 m；列 [('628-23(1)', 0.0, 0.114893), ('628-4(1)', 0.0, 0.056826)]
  ✅ R1@3.5 觸發之端 4（期 4）、端線或指數之不合 []（期 []）、err None
  ✅ R2@3.5 各端之當選 {'R2': {'right': '628-34(1)'}, 'R3': {'left': '628-34(2)'}, 'R5': {'right': '628-23(2)'}, 'R6': {'left': '628-4(1)'}}（期 {'R2': {'right': '628-34(1)'}, 'R3': {'left': '628-34(2)'}, 'R5': {'right': '628-23(2)'}, 'R6': {'left': '628-4(1)'}}）
  ✅ R3@3.5 合併再試之標的 []（期 []）、競合 None（期 無）
     R2 right：端線 44.12 m；列 [('628-34(1)', 10.42, 0.372619)]
     R3 left：端線 43.91 m；列 [('628-34(2)', 34.94, 0.799606)]
     R5 right：端線 47.95 m；列 [('628-23(2)', 0.0, 0.023134)]
     R6 left：端線 47.71 m；列 [('628-23(1)', 0.0, 0.114893), ('628-4(1)', 0.0, 0.056826)]
  ✅ R1@0.0 觸發之端 4（期 4）、端線或指數之不合 []（期 []）、err None
  ✅ R2@0.0 各端之當選 {'R2': {'right': '628-34(1)'}, 'R3': {'left': '628-34(2)'}, 'R5': {'right': '628-23(2)'}, 'R6': {'left': '628-4(1)'}}（期 {'R2': {'right': '628-34(1)'}, 'R3': {'left': '628-34(2)'}, 'R5': {'right': '628-23(2)'}, 'R6': {'left': '628-4(1)'}}）
  ✅ R3@0.0 合併再試之標的 []（期 []）、競合 None（期 無）
⇒ 紅 []；rc 0
````

