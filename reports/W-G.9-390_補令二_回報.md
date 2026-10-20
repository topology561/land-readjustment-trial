# `W-G.9-390` 補令二　執行端回報（停機上呈·停機款 `12‴`）

- 受單：`orders/W-G.9-390_補令二.md`（`110496` B·`sha256` `42b3891a0a47748fc84320be96a5e50948228ccdd484d6e52ce16f4c79f1ef1b`·與 `STATE.json` 合；`SELF_SHA256` 依 `P-5` 原口徑自驗 ＝ `f8e16e6a5d7fecc15450dde8ae1a527a5929969c669839997ede5481e61f9ba0`·合）。
- 結果：**停機上呈**（停機款 `12‴`：工項二‴ 之唯讀獨立審查揭一形，**⛔ 在 `§三-4‴` 之已知之形 ①〜⑤ 之列**，審查者判其「涉域上判斷或規格之漏載」之候選）。
- **工項二‴ 之 `commit` `3f51658`（`app.py` blob `0502e193e318cbe65786d123e23762b1976b7c00`）⛔ 推**（單：「驗與審查皆符後」方推）；其全文差異載於本回報之附錄甲（次輪可二進位重施）。新側支 ＝ `6d1e994`（工項一‴ 之端）；主線 `2aa6302` ⛔ 動；heads `50`。
- 驗 `V-1‴`〜`V-9‴` **皆合期**（本案配地⛔ 變：`k6s3 cmp` 二退縮相異 `0`、`F8` 落檔逐位同、`parity` 代 `HEAD` 後逐位同）。停機之由唯審查之 (D)。
- 停機之內容**涉土地後果**（合成之例之形：同一街廓之一端先已回原狀一次，其後同一次所施之二成者皆未保留而依新序所擇之一端恰為該端 ⇒ 新碼停機「還原後仍出現」；他讀則配地續行）——本案⛔ 觸（本案競合之列 `0`、回原狀之列 `0`）。
- 時程（Asia/Taipei）：接單 `15:50:17`（`0bedea8`）→ 開場畢 `15:55` → 工項零‴ `320f967`、一‴ `6d1e994` 推 `15:55`〜`15:56` → 前置‴ (甲)(乙) `15:56`〜`16:42` → 工項二‴ `commit` `16:44` → 施後之驗 `16:47`〜`18:25` → 唯讀審查 `18:27`〜`18:36` → 停機 `18:37`；`effort=high`。
- `<O>` ＝ `/tmp/O`（倉外）；施工樹 ＝ `/tmp/w`（雲端完整複本）；撰碼用之拋棄式 worktree `/tmp/dev`、突變自驗用 `/tmp/mut`（皆 `git worktree`·⛔ 推·⛔ 入倉）。

## 一、停機款之三值

| 款 | 期（本補令之文·逐字節錄） | 實 |
|---|---|---|
| `12‴` | 「**唯讀獨立審查之發現涉域上判斷或規格之漏載**（⛔ 自裁·`§三-4‴` 之已知之形除外）」；`§三-4‴`：「…或唯讀獨立審查揭他形之二讀 ⇒ 停機款 `5‴`／`12‴`」 | 審查之 (D) 揭一形（見下）而列為停機款 `12‴` 之候選；該形⛔ 在 `§三-4‴` 之 ①〜⑤ |

**審查之 (D)（審查者之原文·節錄）**：

> **新形**：組中依新序被選為還原者，其端於本次之前已回原狀一次（每端至多一次）。新碼因而走到「還原後仍出現 ⇒ 停機」；改前之碼還原者為組中段二序在後之一端，其端未曾回原狀，故照常配地。
> 例三（例一加 NA 左端之首名 Z1）：Z1 屬他地主 h5，以 ① 併 Z2 得 160 而成，但未保留，於是先回原狀，NA 左端已用掉其一次。重試時，P1 與 Q1 切半同一次皆成而皆未保留，新序選中 P（NA 左端）。**改後之碼**停機，訊息為「還原後仍出現：NA 左端之成者 P1(1) 於試算⛔ 保留，而該端前已回原狀（候選 Z1(1)）——程式錯誤 ⇒ 停機」。**改前之碼**還原 Q，最終 P1 為 346。
> 依 R-2‴ 之字面（其後「還原後仍出現」之判照原單），停機乃字面之果；但亦有他讀，例如於組中改取其端未曾回原狀者，或改還原他端。二讀之土地後果不同，且此形不在 ①〜⑤ 之內。
> 另：此種情形乃合法之地況，非程式之錯，而停機訊息卻稱「程式錯誤」，與實情不符。此項亦交 KL 一併裁示。

**倉內與此形相關之文（執行端照錄·⛔ 判其孰為正典）**：

1. 本補令 `R-2‴`（`:118`）：「…改取該組之未保留者中題一 3 之序之最後者為回原狀之成者（其餘本次⛔ 回原狀）；其後之一切（「還原後仍出現」之判、回原狀之端與組合之記、重試、…）照原單 `R-2`、`R-3`。」
2. 補令一 `§一″` 項 `7`（發單端之唯讀審查·`docs/orders/W-G.9-390_補令一.md:78`）：「記而⛔ 改：所擇之後者之端已曾回原狀 ⇒ 停機（合 ④ 末句與原單【工】丁）」。
3. 原單 塊 `K33` 之二之丁（`docs/orders/W-G.9-390_規格單.md:1070`）：「**丁 還原後仍出現**：某一端已回原狀一次，其後之試再查得該端之成者之宗未保留 ⇒ 停機（程式錯誤·⛔ 再回原狀）。…⇒ 每一端至多回原狀一次、重試之次數 ≤ 端之數。」
4. `K-9-61` ④（KL `2026-10-06 01:29`·原單 `:111`）：「…還原後仍出現者屬程式錯誤而停機。」
5. 本補令 `§三-4‴` 之已知之形 ①〜⑤（`:132`）：此形（所擇之一端已曾回原狀）**⛔ 列**。

**執行端之所見（⛔ 裁）**：新碼之行為 ＝ 上列 1 之字面（選定後照原單之「還原後仍出現」之判 ⇒ 停機），與上列 2〜4 一致；然本補令之已知之形⛔ 列此形、審查者以之為停機款 `12‴` 之候選，其是否屬「已知而⛔ 停機之形」或須 KL 另裁（例：組中改取其端未曾回原狀者），執行端⛔ 判——依單首 🔴 與停機款 `12‴` 停下。若發單端判其屬已知（上列 2 已記之），則次輪可重施附錄甲之差異（⛔ 改碼）、重驗後逕推。

## 二、已做之工項（皆依單·逐字之首列）

| 工項 | `commit` | 推送 | 內容 |
|---|---|---|---|
| 零‴ | `320f967` | `verify/W-G.9-390-k961r`：`ddddfb8` → `320f967`（快轉） | `docs/orders/W-G.9-390_補令二.md`（新檔·二進位複製·`git cat-file blob` 與來源 `cmp` 逐位同；`git check-ignore -v --no-index` 無命中 `rc 1`）·`725`／`0` |
| 一‴ | `6d1e994` | `verify/W-G.9-390-k961r`：`320f967` → `6d1e994`（快轉） | 塊 `Fy44`（`23118` B·`ea0e1180…`·`260` 列）：`git apply --check` 過；施後 `probe_WG9390_k961r.py` ＝ `31e1a662ae92886fe01244b41a437b34a6df9dd6`（`54500` B）、`probe_WG9354_endcontest.py` ＝ `066261c86675fdb2d7b49c8715fd6015b63617ca`（`55924` B）；`git status --porcelain --untracked-files=no` 唯此二檔 |
| 二‴ | `3f51658`（**⛔ 推**·本機） | — | `R-0″`（`rep390.diff` 施後 ＝ `7b4c626bf832737b9192163899ef0166755aa892`·逐位 ＝ `<O>/app_R0.py`）＋ `R-2‴`／`R-9‴`／`R-8″`／`R-5‴`；`py_compile` 過；`app.py` ＝ `0502e193e318cbe65786d123e23762b1976b7c00`（`1861280` B）；對工項一‴ 之端 `123`／`16`、對 `app_R0.py` `52`／`15` |
| 三‴、四‴ | ⛔ 做 | — | 停機 |

推後 `git ls-remote --heads origin`：`50` 列；主線 `2aa63021da38632704519e05d53ced9f56e22659`；`verify/W-G.9-390-k961r` ＝ `6d1e994893983b56b6c954d2d9e4033258076522`。

## 三、`§零‴` 之實值

1. context 充足；`nproc` ＝ `4`。
2. `origin/wip/s1-endpart` ＝ `2aa63021…`；`origin/verify/W-G.9-390-k961r` ＝ `ddddfb85…`；heads `50`（存 `<O>/heads_before_390p2.txt`）；`checkout --detach` 後 `status` 空；旗標 `[None, None, None, None, None]`（殼之 `WV_*` `0` 個）。
3. `probe_WG9321_issuer_anchor.py … 629 623` ⇒ `rc 0`；項4′ 正典框：自誤 `614`／`629`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`（皆合）。
4. bytes／`sha256`／`SELF_SHA256` 皆合（見首）。
5. 初 `import shapely…` ⇒ `ModuleNotFoundError`；依 README 第六節第 2 款 `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`·出艙 `<O>/pip_install.txt`）後 `rc 0`。
6. `Python 3.11.17`；裝後 `pip freeze` ＝ `80716bfb…`，對基準唯 `certifi`（`2026.10.19`）、`pillow`（`10.2.0`）、`websockets`（`17.3`）三列異 ⇒ 依本項之 🔎 `python3 -m pip install pillow==12.3.0 websockets==17.2 certifi==2026.10.18 --break-system-packages`（`rc 0`）⇒ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（`1114` B·`64` 列）＝ 基準。
7. pre-flight：🔴 `0`／🟡 `5`（`:99`、`:114`、`:159`、`:181`、`:194`·皆 `P-4`·＝ `§五‴` 項 `9` 之具名豁免）／ℹ️ `2`（`P-5` 相符；`P-3` `23466`–`31208`）。
8. `<O>/rep390.diff`：`10258` B·`1553968da127…`·`135` 列（＝ `§五‴` 項 `3`）。塊 `K35` `9883`／`8f290c37…`／`56`、`E35` `3727`／`f24cc0ae…`／`22`、`P46` `2136`／`1a358814…`／`16`（＝ 項 `4`）；倉內抽之 `K33` `9617`／`45cf74b9…`／`60`、`P44` `2512`／`5f747163…`／`18`、`K34` `7536`／`31924524…`／`47`、`E34` `3665`／`d77f4158…`／`22`、`P45` `1619`／`9abf2141…`／`15`、`CK` `1539`／`00cd3949…`／`31`、`GF` `2445`／`b11edb77…`／`47`（皆合）。

## 四、前置‴ 與驗之實值

- 前置‴ (甲)(乙)：`20` 呼叫皆合期（`#36`、`#38`、`#65`、`#72`、`#73` 之 `rc 1` 與末列逐字 ＝ 期）；`stderr` 合計 `0` B。(丙)：`§零-0‴` 項 `6` 之比對皆同（主線 ＝ `2aa63021…` ＝ 基準之 sha、`Python 3.11.17`、`pip freeze` `ae1438da…`）⇒ `54` 呼叫**沿用** `基準/2aa63021da38632704519e05d53ced9f56e22659.md`。
- 前置‴ 項 `4`（逐字）：`A⇥docs/orders/W-G.9-390_補令二.md`、`M⇥verify/probes/probe_WG9354_endcontest.py`、`M⇥verify/probes/probe_WG9390_k961r.py`（恰三列）；`38⇥5⇥verify/probes/probe_WG9354_endcontest.py`、`81⇥19⇥verify/probes/probe_WG9390_k961r.py`（恰二列）。項 `5`：前四字樣各無出艙 `rc 1`；「於現態未保留」⇒ `app.py:1`。
- `V-1‴`／`V-2‴`：施後 `74` 呼叫一律從頭照跑，皆 `rc 0`、末列 ＝ 施後之列；`F34 selftest` `K1`〜`K27` ✅ 與 `P0 判式自驗 27／27`；`F34 wiring` `X1`〜`X4` ✅；`F34 run` `R1@3.5`（段三之呼叫 `1`·回原狀之列 `0`·其檢核 `0`·成者 `3`）、`R1@0.0`、`R0` ✅；`F13 selftest` 全例與 `M0`〜`M16` ✅；`F23 selftest` `P0 逐項擾動恰該項紅 75／75`。
- `V-3‴`：`verify/` 對工項一‴ 之端相異 `0`；`probe_WG9353_endmerge.py` `8a9d11c2…`、`probe_WG9388_k961s3.py` `0ed194da…`、`probe_WG9389_trialstop.py` `0decb955…`（＝ 原單 `§五-1` 項 `5`）；`probe_WG9390_k961r.py` `31e1a662…`、`probe_WG9354_endcontest.py` `066261c8…`（＝ `§五‴` 項 `5`）。
- `V-4‴`：`k6s3 cmp` `3.5`：`rc 0`·`相異 0 項 ⇒ ✅ 同`；`0.0`：`rc 0`·`相異 0 項 ⇒ ✅ 同`（`stderr` 皆 `0` B）；對照組 `k6s3_pre_35` 對 `k6s3_post_00` ⇒ `rc 1`·`相異 18 項 ⇒ 🔴 異`。**本案之配地⛔ 變**。
- `V-5‴`（`HEAD`：前 `6d1e994893983b56b6c954d2d9e4033258076522`、後 `3f51658c2a1a4ce1de04fe028045bb4b2260db52`·以同一字樣代其全值與短值後比）：

```
parity35_pre.json: 8683 B sha256 c33407a22a9a7f498679355da2e45d76bda95236a1eb7904bab32eabb4d5ca70；全值見 1、短值見 1
parity35_post.json: 8683 B sha256 d9963d55c7b73bdf46c6b0a3132f83df0a3d902b1649d6b99268d35364fdd87e；全值見 1、短值見 1
⛔ 代之對照：逐位同？ False
代之後：逐位同？ True（25810ad8b1fb88662b419585631b4614b3f11749a6fe905cbf81bfc5c9c90639 ／ 25810ad8b1fb88662b419585631b4614b3f11749a6fe905cbf81bfc5c9c90639）
rc=0
parity00_pre.json: 284 B sha256 7a4e6056be9f817ceab4fe0e674e6cbbe726db8b3ffaa8eae32b40af982b09a2；全值見 1、短值見 1
parity00_post.json: 284 B sha256 2c3da8076e3c0cf648ece73015baaf92ad12bc725362c11ff0108ede7cb9c43c；全值見 1、短值見 1
⛔ 代之對照：逐位同？ False
代之後：逐位同？ True（58a3d9e85d265d1592efba323d0078e426f8757c5f70e3ef3733026183102cc7 ／ 58a3d9e85d265d1592efba323d0078e426f8757c5f70e3ef3733026183102cc7）
rc=0
run_pre/60.out: 1586 B sha256 124e4692945b2701c7f78f14be0a60bb7b1e101122fc79f84a902add25e99ffd；全值見 1、短值見 1
run_post/60.out: 1586 B sha256 4cac3135c26b1c38ab3b42be0c4bcac135657933d243d6c9ad3fa3900a2ab183；全值見 1、短值見 1
⛔ 代之對照：逐位同？ False
代之後：逐位同？ True（73ba729fc44a775ea86d8b831dfdc1a28459b1366edfe8a1121630cb2a38c07a ／ 73ba729fc44a775ea86d8b831dfdc1a28459b1366edfe8a1121630cb2a38c07a）
rc=0
run_pre/61.out: 1584 B sha256 8a358c5a2e587c984eb00a9130aa9cefbc61a899f836d4cdb52571c959ad03b2；全值見 1、短值見 1
run_post/61.out: 1584 B sha256 8a8e11769ab0ac3dff522520f55a9258f16844a82755922a6797a44fc0b44391；全值見 1、短值見 1
⛔ 代之對照：逐位同？ False
代之後：逐位同？ True（b2f8709d925ec91340aef4141a52dc525451f00b55029a084dccacc48cad74cc ／ b2f8709d925ec91340aef4141a52dc525451f00b55029a084dccacc48cad74cc）
rc=0
```

  `parity` `3.5` 之 `stdout` 之末十五列（施後）：

```
  ✅ 段三 session 鍵 f3_k6b_stage3_log（19 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（13 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 3.5, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（37 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（45／45）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 35／畫面 34；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
```

- `V-6‴`：`git hash-object <O>/f8_pre_35.json <O>/f8_post_35.json <O>/f8_pre_00.json <O>/f8_post_00.json` ⇒ `8be0160bc14dd92a5331f86eecc995cae0507376` ×2、`6fb86647807f9744594071be25c522b6b506c230` ×2（逐位同·＝ 基準）。
- `V-7‴`：生產碼 `34` 檔對 `6d1e994` 相異唯 `app.py`；頂層之名之集同（`395`／`395`）；相異之節點 ＝ `['k6b_stage3_run']`；`verify/` 相異 `0`；題二之二行於 `app.py` 各 `1`（皆在 `k6b_stage3_run` 之 `_ct_pick`）；`_ct_pick(A, B, '二')` `1`。`git diff --no-index <O>/app_R0.py <repo>/app.py`（`rc 1`）之全文 ＝ 附錄甲。
- `V-8‴`：`app.py:2`、`app.py:2`、`app.py:2`、`app.py:3`（各 `rc 0`）；「於現態未保留」無出艙 `rc 1`。
- `V-9‴`：諸器之 `stderr` 合計 `0` B。
- 撰碼中之自跑（`/tmp/dev`）：`F23 wiring 7d8e954`、`F24 wiring d7a5ea4`、`F34 wiring 2aa6302` 皆 `rc 0`；自設之突變（倉外·⛔ 為期）`N1`、`N3`、`N6`、`N7`、`N8`、`N9`、`N10` 於 `F34 selftest` 皆轉紅（`N7` ⇒ `K26`、`N9` ⇒ `K25`、`N10` ⇒ `K27`、餘 ⇒ `K18`〜`K22`、`K24`、`K27`）。

**`74` 呼叫之表**（前置‴ 與驗·格 ＝ `rc`／`stderr` B／末列／耗時 s）：

| # | 命令 | 工項一‴ 之端 | 施後（工項二‴ `3f51658`） |
|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·137） | `0`／`0`／`⇒ 紅 []；rc 0`（123） |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·439） | `0`／`0`／`⇒ 紅 []；rc 0`（370） |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·33） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·34） | `0`／`0`／`⇒ 紅 []；rc 0`（31） |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·43） | `0`／`0`／`⇒ 紅 []；rc 0`（35） |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·17） | `0`／`0`／`⇒ 紅 []；rc 0`（13） |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·262） | `0`／`0`／`⇒ 紅 []；rc 0`（232） |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·77） | `0`／`0`／`⇒ 紅 []；rc 0`（68） |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·515） | `0`／`0`／`⇒ 紅 []；rc 0`（430） |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·700） | `0`／`0`／`⇒ 紅 []；rc 0`（612） |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | 沿用基準：`0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（基準·10） | `0`／`0`／`⇒ 突變 8（另基準一）；紅 []；rc 0`（8） |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | 沿用基準：`0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（基準·72） | `0`／`0`／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（66） |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·417） | `0`／`0`／`⇒ 紅 []；rc 0`（370） |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·1868） | `0`／`0`／`⇒ 紅 []；rc 0`（1788） |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·37） | `0`／`0`／`⇒ 紅 []；rc 0`（30） |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·7） | `0`／`0`／`⇒ 紅 []；rc 0`（5） |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（基準·23） | `0`／`0`／`⇒ rc 0（不符 0·器紅 0）`（22） |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·23） | `0`／`0`／`⇒ 紅 []；rc 0`（20） |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·260） | `0`／`0`／`⇒ 紅 []；rc 0`（245） |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·363） | `0`／`0`／`⇒ 紅 []；rc 0`（340） |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·38） | `0`／`0`／`⇒ 紅 []；rc 0`（33） |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·35） | `0`／`0`／`⇒ 紅 []；rc 0`（29） |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['S10b ① 同街廓成（⛔ 驗不影響原位次）', 'S10c ② 道路成且驗不影響原位次']；rc 1`（8） | `0`／`0`／`⇒ 紅 []；rc 0`（7） |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（21） | `0`／`0`／`⇒ 紅 []；rc 0`（20） |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['TI 題一 整片二端皆成 ⇒ G 大者（A 240 ＞ B 220·交面積 B 30 ＞ A 15 ⛔ 用）', 'TT 題一 整片二端皆成·G 相同 ⇒ 重劃前面積大者（補令二）', 'TU 題一 整片二端皆成·G 與重劃前面積皆相同 ⇒ 暫編地號小者（補令二）', 'M3', 'M15', 'M16']；rc 1`（16） | `0`／`0`／`⇒ 紅 []；rc 0`（15） |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（10） | `0`／`0`／`⇒ 紅 []；rc 0`（11） |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·203） | `0`／`0`／`⇒ 紅 []；rc 0`（175） |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·60） | `0`／`0`／`⇒ 紅 []；rc 0`（48） |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·893） | `0`／`0`／`⇒ 紅 []；rc 0`（818） |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·183） | `0`／`0`／`⇒ 紅 []；rc 0`（145） |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·130） | `0`／`0`／`⇒ 紅 []；rc 0`（103） |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·2） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·375） | `0`／`0`／`⇒ 紅 []；rc 0`（345） |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | 沿用基準：`0`／`0`／`selftest 9/9 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 9/9 ⇒ ✅`（0） |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | 沿用基準：`0`／`0`／`selftest 13/13 ⇒ ✅`（基準·0） | `0`／`0`／`selftest 13/13 ⇒ ✅`（0） |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | 沿用基準：`0`／`0`／`ε ＝ 0.0002｜rc 0`（基準·2） | `0`／`0`／`ε ＝ 0.0002｜rc 0`（1） |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | 沿用基準：`0`／`0`／`紅項 [] 器紅 0`（基準·10） | `0`／`0`／`紅項 [] 器紅 0`（9） |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·375） | `0`／`0`／`⇒ 紅 []；rc 0`（349） |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／`（JSON 之摘要列·略）`（200） | `0`／`0`／`（JSON 之摘要列·略）`（188） |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／`（JSON 之摘要列·略）`（136） | `0`／`0`／`（JSON 之摘要列·略）`（137） |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／`⇒ 紅 []；rc 0`（194） | `0`／`0`／`⇒ 紅 []；rc 0`（187） |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／`⇒ 紅 []；rc 0`（135） | `0`／`0`／`⇒ 紅 []；rc 0`（139） |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（409） | `0`／`0`／`⇒ rc 0（不符 0 項）`（393） |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／`⇒ rc 0（不符 0 項）`（299） | `0`／`0`／`⇒ rc 0（不符 0 項）`（296） |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·4） | `0`／`0`／`⇒ 紅 []；rc 0`（4） |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·3） | `0`／`0`／`⇒ 紅 []；rc 0`（3） |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | 沿用基準：`0`／`0`／`⇒ 紅 []；rc 0`（基準·376） | `0`／`0`／`⇒ 紅 []；rc 0`（330） |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['K13']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／`⇒ 紅 []；rc 0`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1232） | `0`／`0`／`⇒ 紅 []；rc 0`（1278） |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1227） | `0`／`0`／`⇒ 紅 []；rc 0`（1206） |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／`⇒ 紅 []；rc 0`（128） | `0`／`0`／`⇒ 紅 []；rc 0`（126） |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（431） | `0`／`0`／`⇒ 紅 []；rc 0`（415） |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `1`／`0`／`⇒ 紅 ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20', 'K21', 'K22', 'K23', 'K24', 'K25', 'K26', 'K27']；rc 1`（1） | `0`／`0`／`⇒ 紅 []；rc 0`（1） |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `1`／`0`／`⇒ 紅 ['X1', 'X2']；rc 1`（2） | `0`／`0`／`⇒ 紅 []；rc 0`（2） |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／`⇒ 紅 []；rc 0`（331） | `0`／`0`／`⇒ 紅 []；rc 0`（342） |

- pre：實跑 20 呼叫；≠期 []；stderr 合計 0 B；耗時之和 4784 s（並行 2）

- post：實跑 74 呼叫；≠期 []；stderr 合計 0 B；耗時之和 12029 s（並行 2）

## 五、唯讀獨立審查（全文要旨）

- (A) 改配地或違裁示：**無**。差異之九塊皆在 `k6b_stage3_run` 之內，分屬 `R-5‴`／`R-2‴`／`R-8″`①②／`R-9‴`；頂層之名之集同、`k967_rank`／`k967_pre_area` ⛔ 動；成者之寫入唯 `_ct_commit` 與逐列二處，`_ct_commit` 之八呼叫中施二端者恰題一之三形；`R-2‴`、`R-9‴` 同呼 `_rk390`（內呼頂層之 `k967_rank`、`k967_pre_area`）、表 ＝ 施前之 `state` 之「分攤登記面積 − 段三部分併出」（⛔ 減入池閘之帳）；重試時 `_grp390` 去之；題二之二行與 `_ct_pick(A, B, '二')` 改前改後各恰一見、題二之真值表全同。新區域名 `17` 皆帶 `390` 而⛔ 撞；案件字面 `0`；新折行之「四空白＋中文」`0`；量測器之錨（長 ≥ `4`）改前恰一見者改後仍恰一見。
- 合成之例（`F34`、`F13` 之外）：例一（題一切半二端皆成而皆未保留·`G` P `168` ＜ Q `178` 而交面積 P `35` ＞ Q `15`）：手算 ⇒ 保留 Q、還原 P、題一 4「其半併之」⇒ Q1 `178`、P1 `138`；改後 ＝ 手算；改前 ⇒ P1 `346`（Q1 併入）。例二（題一整片二端皆成·`G` 同 `240`·重劃前面積 A `220`／F `240`）：手算 ⇒ 歸 F；改後 ＝ 手算；改前（交面積）⇒ 歸 A。附例二b（`G` 差 `0.004`·二位同 ⇒ 仍 F）、二c（A `241` ⇒ 歸 A·`G` 先於重劃前面積）皆合。
- (B) 純實作之瑕：無能改配地者；微：`_rk390` 中 `_f390` 一名用於二互不相干之推導式（作用域隔離·無害·⛔ 改）。
- (C) 記而⛔ 改：`_ct_pick(…, '一')` 未傳 `rk390` 則拋 `TypeError`（唯一呼叫點已傳）；題二之 `'左'` 一行去其 `if form == '二':` 之縮排（錨恰一·行為等價）；已知之形 ①〜⑤ 之碼皆合（③ 不成組、⑤ `K25` 綠、④ 不計切分併入〔例一 P `120`〕、① dict 二以上通用、② 題二唯施一端）。
- (D) ⇒ 見「一」（停機之由）。
- 審查者之自報之越界：初於 `/tmp/w` 跑 `py_compile` 生 `__pycache__/`（`.gitignore:18` 所忽）即刪之；事後 `git status --porcelain` 空、該目錄⛔ 存。執行端復核：`/tmp/w` 之 `status --porcelain` 空、`HEAD` 仍 `3f51658`、`app.py` blob 仍 `0502e193…`。

## 六、設計說明（`§三-5‴`）

- `R-0″`：`<O>/rep390.diff` 施於 `80d00d86…` ⇒ `7b4c626b…`（`git hash-object`·與 `<O>/app_R0.py` `cmp` 同）。
- 同源之區域函式 `_rk390(e390, res390)`（緊接 `_hit390` 之後）：`k967_rank(res390['G'], k967_pre_area(e390['c'], [候選] ＋ sorted(整筆併入之片), 表), e390['c'])`；表 ＝ 求鍵時之 `state["by"]` 之每片「分攤登記面積 − Σ段三部分併出」；切分併入（`items` 之 `whole` 為假者）⛔ 入成員。
- `R-9‴`：`_ct_cross` 之「整片」支之二端皆成 ⇒ `_two390 = {端鍵: _rk390(端, 該端之整片之試)}`，`_ct_pick(A, B, '一', _two390)`；`_ct_pick` 增第四參數 `rk390=None`：`form == '一'` ⇒ 序鍵小者先（`<`）；其餘（題二）照舊之二行（交面積大者 → 並列 ⇒ `p1` 側）。舊之「題一並列取暫編地號小者」之行去之（⛔ 留死碼）。紀錄之 `競合` 之述改為「題一 3 之序·G …／…·重劃前面積 …／…」。題二之支（`_ct_same_block`·`_ct_pick(A, B, '二')`）⛔ 動。
- `R-2‴`：組之記 ＝ `_ct_commit` 首（`len(pairs) >= 2` ⇒ `_grp390.append({(街廓, 端, 候選): _rk390(端, 其試)})`，於 `state` 換為施後之態之前求之）；最後成者之改取 ＝ `_att390` 中 `_kb390, _ke390, _kc390 = _out390[-1]` 之後：逐組，`_out390[-1]` 屬之且該組之未保留者（`_out390 ∩ 組`）≥ `2` ⇒ 取其序鍵最大者（題一 3 之序之最後者）；其後「還原後仍出現」之判與其餘照原趟之碼；重試時 `_grp390` 入「皆去之」之列（`for _z390 in (…, _t14_done, _grp390)`）。
- `R-8″`：① `_hit390(blk390, end390, cand390, pieces390)`；② 成之列以 `_ys390` 取之，空 ⇒ `raise RuntimeError("🔴 [K-6-B 段三] 回原狀之成者 …之成之列取不到——程式錯誤 ⇒ 停機")`（⛔ 帶 `GB-` 之號與【未裁】）。
- `R-5‴`：docstring 之原單 `R-5` 段之後增 `🔧 \`W-G.9-390\` 補令二` 之段（`7` 列·折行皆以 `` ` `` 或 `→` 起首）。
- `§三-3‴` 之自查：`F23 wiring`／`F24 wiring`／`F34 wiring` 自跑皆綠；題二之二行與 `_ct_pick(A, B, '二')` 各恰一；`k967_rank` 之錨恰一（`F13` `M3`／`M15`／`M16` 皆紅轉 ⇒ 序鍵經頂層之 `k967_rank` 求之）；頂層之名之集同；新名皆帶 `390`。

## 七、自捕與自解

1. 施工樹之根之單之複本以 `.git/info/exclude` 免之時，初書其式為 `W-G.9-390_補令二.md`（無首斜線 ⇒ 任一深度皆命中）⇒ 工項零‴ 之 `git add docs/orders/W-G.9-390_補令二.md` 被拒（「ignored」）；改為 `/W-G.9-390_補令二.md` 後再 `add`／`commit`（被拒之時⛔ 有 `commit`、⛔ 有推送）。`git check-ignore -v --no-index`（不讀 exclude）無命中 `rc 1`（停機款 `11‴` ⛔ 成就）。
2. 數個等待之殼迴圈以 `pgrep -f "runner.py /tmp/q"` 判，其自身之命令列含該字樣 ⇒ 恆真、逾時方止（⛔ 影響量測·唯佔一殼）；其後改以 `kill -0 <pid>` 判。
3. 抽取器初稿之 f-string 含反斜線 ⇒ `SyntaxError`（未出艙任何檔）；改後重跑，諸塊之 bytes／`sha256`／列數皆合。

## 八、待發單端

- 停機款 `12‴` 之 (D) 之處置（屬已知而⛔ 停機之形、抑須 KL 裁）。
- 若續：附錄甲之差異施於 `<O>/app_R0.py`（＝ `7b4c626b…`）⇒ `0502e193e318cbe65786d123e23762b1976b7c00`（本輪之工項二‴）；新側支現於 `6d1e994`（工項零‴、一‴ 已推·⛔ 重做）。主 checkout 之同步由 KL 自行為之。

## 附錄甲　`git diff --no-index /tmp/O/app_R0.py /tmp/w/app.py`（`V-7‴`·工項二‴ 之 `R-2‴`／`R-9‴`／`R-8″`／`R-5‴`）

````diff
diff --git a/app_R0.py b/tmp/w/app.py
index 7b4c626..0502e19 100644
--- a/app_R0.py
+++ b/tmp/w/app.py
@@ -14737,6 +14737,13 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
       `①`／`②` 之合併與該組合同者⛔ 試（檢核記「回原狀（K-9-61 ④）」）；他端照常。重試畢依 `R-1` 再查（每端至多一次）。
       `R-3` 競合（`K-9-50`·`_ct_try`）之一端為回原狀之鍵或其同一端之同一組合 ⇒ 該端之該試不成（⛔ 試算）；他端照舊。
       `R-4` `W-G.9-388` `R-5` 之停機（步驟 10 之受併宗未保留之查）去之，由 `R-1`〜`R-3` 代之。
+    🔧 `W-G.9-390` 補令二（KL `2026-10-20 08:47`「採乙」、`09:02` 之補正、`09:11`「是」）：序鍵 ＝ `k967_rank`（該端之試之
+      `G` → 重劃前面積〔候選 ∪ 該試之整筆併入之片·⛔ 計切分併入·表 ＝ 現態之每一片之分攤登記面積 − 其段三部分併出之和〕
+      → 暫編地號·小者先）；`R-2‴` 與 `R-9‴` 之序鍵由同一區域函式求之。
+      `R-9‴` `K-9-50` 題一第 3 點（整片各試而二端皆成）：歸題一 3 之序之先者（⛔ 以交面積）；題二⛔ 改。
+      `R-2‴` 同一次所施（`_ct_commit`）之二以上之端之成者記為一組（各端之序鍵於施之前之現態求之）。
+      `R-2‴` 未保留者之最後成者屬某組、且該組之未保留者二以上 ⇒ 改取其中題一 3 之序之最後者回原狀；他者照 `R-2`。
+      `R-2‴` 組之記於重試時與前試之他物同去之。
     """
     import copy as _cp
     from shapely.geometry import Polygon as _Pg, LineString as _Ls
@@ -14925,10 +14932,22 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
     #   每端至多一次（第二次 ⇒ 停機）。_hit390 ⇒ 該端之該試⛔ 試（為回原狀之鍵、或同一端之同一組合）
     _RS390, _RC390 = '回原狀（受併宗未保留·K-9-61 ④）', '回原狀（K-9-61 ④）'
     _ban390 = {}
-
-    def _hit390(blk, end, cand, pieces):
-        _b390 = _ban390.get((blk, end))
-        return _b390 is not None and (cand == _b390[0] or ({cand} | set(pieces)) == _b390[1])
+    # 🔧 `W-G.9-390` 補令二（R-2‴）：同一次所施（_ct_commit）之二以上之端之成者之組——每組 {(街廓, 端, 候選): 序鍵}
+    _grp390 = []
+
+    def _hit390(blk390, end390, cand390, pieces390):
+        _b390 = _ban390.get((blk390, end390))
+        return _b390 is not None and (cand390 == _b390[0] or ({cand390} | set(pieces390)) == _b390[1])
+
+    def _rk390(e390, res390):
+        # 🔧 `W-G.9-390` 補令二（R-2‴／R-9‴ 之同源）：一端之試之序鍵 ＝ k967_rank(該試之試算之 G, 重劃前面積, 候選)——
+        #   重劃前面積之成員 ＝ 候選 ∪ 該試之整筆併入之片（切分併入之片⛔ 入）；其表 ＝ 現態之每一片之分攤登記面積 − 其
+        #   段三部分併出之和（同第 5 項之表之式之前半）
+        _pa390 = {_u390: float(_v390.get('分攤登記面積_m2', 0) or 0)
+                  - sum(float(_f390) for _f390 in (_v390.get('段三部分併出') or {}).values())
+                  for _u390, _v390 in state["by"].items()}
+        _m390 = [e390['c']] + sorted(_x390 for _x390, _q390, _f390 in res390['items'] if _f390)
+        return k967_rank(res390['G'], k967_pre_area(e390['c'], _m390, _pa390), e390['c'])
 
     def _ct_try(e, items, lvl):
         # 一端之試算（於現態之深拷貝）；① 免驗、② 驗「不影響原位次」（同逐列之判）
@@ -14953,6 +14972,9 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
     def _ct_commit(pairs):
         # pairs: [(e, res)]——自現態之深拷貝依序施之（各端之片互不相交）
         nonlocal state
+        if len(pairs) >= 2:
+            # 🔧 `W-G.9-390` 補令二（R-2‴）：同一次所施之成者之組——各端之序鍵於施之前之現態求之、記之
+            _grp390.append({(e390['blk'], e390['end'], e390['c']): _rk390(e390, res390) for e390, res390 in pairs})
         _t = _clone(state)
         for e, res in pairs:
             _apply(_t, e['c'], res['items'])
@@ -14977,13 +14999,15 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
              受併宗=(e['c'] if ok else '—'), 試算G=(res or {}).get('G', '—'), 門檻=(res or {}).get('thr', '—'),
              檢核=(res or {}).get('chk', '—'), 競合=note)
 
-    def _ct_pick(A, B, form):
-        # 二端皆拿得下：與 R_end 之交之面積大者；並列 ⇒ 題一取跨占者暫編地號（字典序）小者、題二取前緣線 p1 側
+    def _ct_pick(A, B, form, rk390=None):
+        # 二端皆拿得下：題二 ⇒ 與 R_end 之交之面積大者；並列 ⇒ 前緣線 p1 側
+        # 🔧 `W-G.9-390` 補令二（R-9‴·KL `2026-10-20 09:11`）：題一 ⇒ 題一 3 之序（rk390 ＝ {端之鍵: 序鍵}·小者先）之先者
+        #   （⛔ 以交面積、⛔ 以暫編地號之並列之支）；題二⛔ 改
+        if form == '一':
+            return (A, B) if rk390[A['k']] < rk390[B['k']] else (B, A)
         if round(float(A['area']), 2) != round(float(B['area']), 2):
             return (A, B) if float(A['area']) > float(B['area']) else (B, A)
-        if form == '二':
-            return (A, B) if A['end'] == '左' else (B, A)
-        return (A, B) if A['c'] < B['c'] else (B, A)
+        return (A, B) if A['end'] == '左' else (B, A)
 
     def _ct_same_block(A, B):
         # 題二（`K-9-50` 二·比照 `K-9-24 二`、`K-9-27`）：二端分別以地主相連之土地試（先同街廓，再及道路、公設地）；
@@ -15158,9 +15182,11 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             _ct_log(B, _rw[B['k']], False, _note)
             return [A, B]
         if len(_ow) == 2:
-            W, Lo = _ct_pick(A, B, '一')
-            _why = (f"二端皆成 ⇒ {W['c']}（交面積 {W['area']:.2f} ／ {Lo['area']:.2f}"
-                    + ("·並列 ⇒ 暫編地號小者" if round(float(W['area']), 2) == round(float(Lo['area']), 2) else "") + "）")
+            # 🔧 `W-G.9-390` 補令二（R-9‴）：二端皆成 ⇒ 題一 3 之序（G → 重劃前面積 → 暫編地號）之先者
+            _two390 = {e390['k']: _rk390(e390, _rw[e390['k']]) for e390 in (A, B)}
+            W, Lo = _ct_pick(A, B, '一', _two390)
+            _why = (f"二端皆成 ⇒ {W['c']}（題一 3 之序·G {-_two390[W['k']][0]} ／ {-_two390[Lo['k']][0]}·"
+                    f"重劃前面積 {-_two390[W['k']][1]} ／ {-_two390[Lo['k']][1]}）")
         else:
             W = _ow[0]
             Lo = B if W is A else A
@@ -15543,17 +15569,28 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
                 return
             # R-2：最後成者回原狀；其端已回原狀 ⇒ 停機
             _kb390, _ke390, _kc390 = _out390[-1]
+            # 🔧 `W-G.9-390` 補令二（R-2‴·KL `2026-10-20 08:47`／`09:02`）：最後成者屬同一次所施之成者之組、且該組之未保留者
+            #   二以上 ⇒ 改取該組之未保留者中題一 3 之序之最後者（其餘本次⛔ 回原狀）
+            for _g390 in _grp390:
+                _o2_390 = [_k390 for _k390 in _out390 if _k390 in _g390]
+                if _out390[-1] in _g390 and len(_o2_390) >= 2:
+                    _kb390, _ke390, _kc390 = max(_o2_390, key=lambda _k390: _g390[_k390])
             if (_kb390, _ke390) in _ban390:
                 raise RuntimeError(
                     f"🔴 [K-6-B 段三] 還原後仍出現：{_kb390} {_ke390}端之成者 {_kc390} 於試算⛔ 保留，而該端前已回原狀"
                     f"（候選 {_ban390[(_kb390, _ke390)][0]}）——程式錯誤 ⇒ 停機")
-            _y390 = [_w390 for _w390 in log if _w390['序'] != '後處理' and _w390['結果'] == '成'
-                     and (_w390['街廓'], _w390['端'], _w390['候選']) == (_kb390, _ke390, _kc390)][0]
+            _ys390 = [_w390 for _w390 in log if _w390['序'] != '後處理' and _w390['結果'] == '成'
+                      and (_w390['街廓'], _w390['端'], _w390['候選']) == (_kb390, _ke390, _kc390)]
+            if not _ys390:
+                # 🔧 `W-G.9-390` 補令一（R-8″ ②）：回原狀之成者之成之列取不到 ⇒ 停機（⛔ 以索引取首）
+                raise RuntimeError(
+                    f"🔴 [K-6-B 段三] 回原狀之成者 {_kc390}（{_kb390} {_ke390}端）之成之列取不到——程式錯誤 ⇒ 停機")
+            _y390 = _ys390[0]
             _ban390[(_kb390, _ke390)] = (
                 _kc390, {_kc390} | set(_y390['整筆併入']) | set(_y390['切分併入']),
                 {'層級': _y390['層級'], '整筆併入': list(_y390['整筆併入']), '試算G': _y390['試算G'], '門檻': _y390['門檻']})
             state = _st0_390
-            for _z390 in (merged_out, marks, won, _closer, _skip, _part, _left, _t14_done):
+            for _z390 in (merged_out, marks, won, _closer, _skip, _part, _left, _t14_done, _grp390):
                 _z390.clear()
             del successes[:], log[:]
             _cur390 = None
````

## 附錄乙　審查者之合成之例之腳本（倉外 `/tmp/rv/scripts/`·⛔ 入倉·供重現）

`synth.py`：

````python
# -*- coding: utf-8 -*-
# 獨立合成之例（審查員自設）：題一 切半二端皆成而皆未保留（例一）、題一 整片各試二端皆成·G 同而重劃前面積異（例二）
import sys, os, io, contextlib, json
H, RDC = "住宅區", "道路"
BLOCKS = {"NA": {"category": H}, "SB": {"category": H}, "RX": {"category": RDC}}
CL = {"RX": [(-30.0, -5.0), (100.0, -5.0)]}
def R(x0, x1, y0, y1): return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
def g(t): return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)
def harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    import importlib
    if "app_harvest" in sys.modules: del sys.modules["app_harvest"]
    from app_harvest import harvest as hv
    with contextlib.redirect_stdout(io.StringIO()):
        ns, _ = hv(os.path.join(repo, "app.py"))
    sys.path.pop(0)
    return ns
def run(ns, parcels, own, order, thr, dropf, contests):
    temp = [{"暫編地號": p, "原地號": p.split("(")[0], "polygon_coords": [list(q) for q in poly], "所屬街廓": b,
             "街廓分類": c, "分攤登記面積_m2": float(a), "面積_m2": float(m)} for p, b, c, poly, a, m in parcels]
    build = [t for t in temp if t["街廓分類"] == H]
    calls = [0]
    def a_prime(src, dst): return g(src)
    def alloc_state(temp_, build_):
        calls[0] += 1
        gm = {b["暫編地號"]: g(b) for b in build_}
        kept, G = {}, {}
        for b in build_:
            if dropf(b["暫編地號"], gm): continue
            kept.setdefault(b["所屬街廓"], set()).add(b["暫編地號"]); G[b["暫編地號"]] = g(b)
        return {"kept": kept, "bad_pools": {}, "err": None, "G": G}
    def trial_winner(temp_, build_, blk, end, cand):
        by = {b["暫編地號"]: b for b in build_}
        gg = g(by[cand]) if cand in by else 0.0
        return (cand if gg >= thr else None), round(gg, 2), thr
    od = [{"最終序位": i, "街廓": b, "端": e, "暫編地號": c} for i, (b, e, c) in enumerate(order, 1)]
    try:
        t2, b2, log = ns["k6b_stage3_run"](od, set(), own, temp, build, BLOCKS, CL, a_prime, trial_winner, alloc_state,
                                           log_print=lambda *x: None, blk5=lambda: {}, contests=contests)
    except RuntimeError as e:
        return {"停機": str(e)}
    return {"rows": [(r["序"], r["候選"], r["結果"], r.get("層級"), r.get("檢核")) for r in log if r["序"] != "後處理"],
            "post": [(r["候選"], r["層級"], r["結果"], r["受併宗"]) for r in log if r["序"] == "後處理"],
            "G": {t["暫編地號"]: round(g(t), 2) for t in t2 if t["街廓分類"] == H},
            "build": sorted(b["暫編地號"] for b in b2), "calls": calls[0],
            "競合": [r.get("競合") for r in log if r.get("競合")][:1]}
# ── 例一：題一 切半二端各配一宗、二者皆未保留；G：Q 178 ＞ P 168；交面積：P 35 ＞ Q 15；段二序 P 先；另有 E 端後成且保留
P1 = [("P1(1)", "NA", H, R(0, 8, 0, 30), 90, 0), ("P2(1)", "NA", H, R(8, 16, 0, 30), 30, 0),
      ("Mx(1)", "NA", H, R(16, 44, 0, 30), 600, 0), ("E2(1)", "NA", H, R(44, 52, 0, 30), 60, 0),
      ("E1(1)", "NA", H, R(52, 60, 0, 30), 100, 0),
      ("R(1)", "RX", RDC, R(0, 12, -10, 0), 96, 0),
      ("Q1(1)", "SB", H, R(0, 12, -40, -10), 130, 0), ("Ny(1)", "SB", H, R(12, 60, -40, -10), 600, 0)]
OWN1 = {"P1": "h1", "P2": "h1", "R": "h1", "Q1": "h1", "Mx": "h9", "Ny": "h8", "E1": "h4", "E2": "h4"}
ORD1 = [("NA", "左", "P1(1)"), ("SB", "左", "Q1(1)"), ("NA", "右", "E1(1)")]
CT1 = [{"形": "一", "列": [("NA", "左", "P1(1)", 35.0), ("SB", "左", "Q1(1)", 15.0)]}]
def drop1(pid, gm): return pid in ("P1(1)", "Q1(1)") and gm.get("P1(1)", 0) > 160 and gm.get("Q1(1)", 0) > 160
# ── 例二：題一 整片各試二端皆成（切半皆不成）；G 皆 240；重劃前面積 A 220 ＜ F 240；交面積 A 30 ＞ F 20；段二序 A 先
P2 = [("A1(1)", "NA", H, R(0, 10, 0, 30), 100, 0), ("A2(1)", "NA", H, R(10, 20, 0, 30), 40, 20),
      ("M(1)", "NA", H, R(20, 60, 0, 30), 600, 0),
      ("D(1)", "RX", RDC, R(0, 10, -10, 0), 80, 0),
      ("F1(1)", "SB", H, R(0, 10, -40, -10), 100, 0), ("F2(1)", "SB", H, R(10, 20, -40, -10), 60, 0),
      ("N(1)", "SB", H, R(20, 60, -40, -10), 600, 0)]
OWN2 = {"A1": "g1", "A2": "g1", "D": "g1", "F1": "g1", "F2": "g1", "M": "g9", "N": "g8"}
ORD2 = [("NA", "左", "A1(1)"), ("SB", "左", "F1(1)")]
CT2 = [{"形": "一", "列": [("NA", "左", "A1(1)", 30.0), ("SB", "左", "F1(1)", 20.0)]}]
# ── 例二b：例二之 G 差 0.004（adj_q2 至 0.01 ⇒ 視為同）——F2 面積_m2 −0.004 ⇒ F 239.996、仍重劃前面積大 ⇒ 仍 F
P2b = [r if r[0] != "F2(1)" else ("F2(1)", "SB", H, R(10, 20, -40, -10), 60, -0.004) for r in P2]
# ── 例二c：例二之 G 不同：A2 面積_m2 21 ⇒ A 241 ＞ F 240 ⇒ A（G 先於重劃前面積）
P2c = [r if r[0] != "A2(1)" else ("A2(1)", "NA", H, R(10, 20, 0, 30), 40, 21) for r in P2]
def nodrop(pid, gm): return False
if __name__ == "__main__":
  for tag, repo in (("改前R0", "/tmp/rv/repo0"), ("改後", "/tmp/rv/repo1")):
    ns = harvest(repo)
    print("=====", tag, repo)
    for nm, args in (("例一", (P1, OWN1, ORD1, 150.0, drop1, CT1)), ("例二", (P2, OWN2, ORD2, 220.0, nodrop, CT2)),
                     ("例二b", (P2b, OWN2, ORD2, 220.0, nodrop, CT2)), ("例二c", (P2c, OWN2, ORD2, 220.0, nodrop, CT2))):
        r = run(ns, *args)
        print("--", nm); print(json.dumps(r, ensure_ascii=False, default=str, indent=None))
````

`synth3.py`（例三·停機之形）：

````python
import sys, json
sys.path.insert(0, "/tmp/rv/scripts")
from synth import harvest, run, R, H, RDC, P1, OWN1, CT1
# 例三：NA 左端之段二序首名 Z1（他地主 h5·① 併 Z2 成而未保留）先回原狀（ban NA左）；重試中同端之競合之候選 P1 與 Q1 切半同一次皆成而皆未保留
P3 = [r for r in P1 if r[0] != "Mx(1)"] + [("Z1(1)", "NA", H, R(16, 24, 0, 30), 100, 0), ("Z2(1)", "NA", H, R(24, 32, 0, 30), 60, 0),
                                           ("Mx(1)", "NA", H, R(32, 44, 0, 30), 600, 0)]
OWN3 = dict(OWN1, Z1="h5", Z2="h5")
ORD3 = [("NA", "左", "Z1(1)"), ("NA", "左", "P1(1)"), ("SB", "左", "Q1(1)"), ("NA", "右", "E1(1)")]
def drop3(pid, gm):
    if pid == "Z1(1)": return gm[pid] > 150
    return pid in ("P1(1)", "Q1(1)") and gm.get("P1(1)", 0) > 160 and gm.get("Q1(1)", 0) > 160
for tag, repo in (("改前R0", "/tmp/rv/repo0"), ("改後", "/tmp/rv/repo1")):
    ns = harvest(repo)
    print("=====", tag); print(json.dumps(run(ns, P3, OWN3, ORD3, 150.0, drop3, CT1), ensure_ascii=False, default=str))
````

`synth3.py` 之出艙：

````
===== 改前R0
{"rows": [[1, "Z1(1)", "回原狀（受併宗未保留·K-9-61 ④）", "①", "—"], [2, "P1(1)", "成", "②半", "通過"], [3, "Q1(1)", "未成", "②半", "回原狀（K-9-61 ④）"], [4, "E1(1)", "成", "①", "免"]], "post": [["Q1(1)", "題一 4", "成", "P1(1)"]], "G": {"P1(1)": 346.0, "P2(1)": 30.0, "E2(1)": 60.0, "E1(1)": 160.0, "Q1(1)": 130.0, "Ny(1)": 600.0, "Z1(1)": 100.0, "Z2(1)": 60.0, "Mx(1)": 600.0}, "build": ["E1(1)", "Mx(1)", "Ny(1)", "P1(1)", "Z1(1)", "Z2(1)"], "calls": 15, "競合": ["題一｜①：P1(1) 未成／Q1(1) —；切半：P1(1) 成／Q1(1) 未成｜只一端成 ⇒ P1(1)；Q1(1) 不能依原位次配地 ⇒ 連同其半併入 P1(1)"]}
===== 改後
{"停機": "🔴 [K-6-B 段三] 還原後仍出現：NA 左端之成者 P1(1) 於試算⛔ 保留，而該端前已回原狀（候選 Z1(1)）——程式錯誤 ⇒ 停機"}
````
