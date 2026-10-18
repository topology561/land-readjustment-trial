# `W-G.9-388_規格單` 之回報（執行端·**停機上呈**·停機款 `12`）

- 受單：`2026-10-18T14:06:50+08:00`；停機：`2026-10-18T20:26+08:00`。單檔 `148474` B·`606428c4…`·`SELF_SHA256` `5eb47045…`，三者皆合。
- **結果 ＝ 停機上呈**。依據：停機款 `12`（工項二之唯讀獨立 reviewer 之發現涉規格之漏載），且合 `§三-4`（「`R-6` 之（一）之受詞於某形有二讀」）。執行端⛔ 自裁。
- 工項零、一已推新側支，⛔ 撤；**工項二已 `commit` 而⛔ 推**（審查未符）；工項三、四⛔ 做。主線⛔ 動。

## 一、停機之由（請發單端裁）

### 單中兩處對同一受詞之寫法不同

**甲 ＝ 單之 `§三-1` `R-6`（`:127`·執行端依之撰碼者）**：
> 以既有之 `_road_halves` 切之，每一半之所臨之街廓 ＝ 其 `_nbr_blocks`（以該半與該道路片之所屬街廓呼之）之鍵；所臨⛔ 含 `x` 之所屬街廓之半（遠半）之所臨之街廓之中 ∈ `B` 者 ⇒ 該街廓記 `_recv_of(該街廓, 該道路片)`

此句**未扣**近半亦臨之街廓。

**乙 ＝ 扣之。**
- 單之 `§四-1` 唯讀獨立審查之段（`:193`）：「`R-6` 之（一）〜（四）之次序（……遠半扣近半；……）」。
- 塊 `K30`（附錄乙·`:1073`·本單令其入 `K-6` 典）四之戊 (ii)：「該群之道路片之中與之共邊者，其遠半所臨之 B 內街廓（**扣近半亦臨者**）」。
- 塊 `K30` 三：「其近半另臨他配得街廓者〔道路之端〕，該近半依 (b) 歸之」。
- `§一` 項 `6`（四）：「道路之端之街廓被當作另一側 ⇒ 唯計遠半」。
- F32 之 docstring：「K19 道路片之端所臨之街廓⛔ 為另一側」。

### 何形會分歧（reviewer 之例四b·執行端自重跑之·harvest 實跑 `k6b_stage3_run`·`2ba27a7`）

形如下：
- 分不到之建地 Y 所鄰之已配得街廓為零。
- 其相鄰之同地主道路片 D1 位於道路之端；道路之端之街廓 BE 同時與 D1 之遠半、近半共邊。
- BE 內有同地主之已配得之宗 E1。

結果：
- 照**甲**（現碼）：`('Y(1)', '後處理(a)', '成', 'E1(1)')`、`('D1(1)', '後處理(b)', '成', 'E1(1)')`——BE 被當作道路之「另一側」。
- 照**乙**：BE 應扣去；若無他側，則 Y 依第 5 項之輪。

二讀之土地後果相異，惟**本案⛔ 觸此形**：`V-4`〜`V-6` 二退縮皆配地⛔ 變。`F32` 之 `K19` 唯測「BE 唯臨近半」之形，未覆「同臨二半」之形，故二讀於現器皆綠。

### 若裁定為乙，reviewer 所擬之最小修法（⛔ 施·僅供參）

於 `R-6`（一）之每一道路片：先求含 `x` 之所屬街廓之半（近半）之 `_nbr_blocks` 之鍵集，於遠半之迴圈中，自 `set(_nb388) & set(B)` 減去之。是否須同時補 F32 之例，由發單端定。

## 二、`commit` 與推送

| 工項 | `commit` | 推送 |
|---|---|---|
| 零 | `347b3b4c7feb42bb3183e6e5c0fb21f0504182bb`（`docs/orders/W-G.9-388_規格單.md` `1192`／`0`·blob 與來源逐位同） | `HEAD:refs/heads/verify/W-G.9-388-k961s3`（新立）；推後 heads `48`；`wip/s1-endpart` ＝ `fd88f64…` |
| 一 | `9977c86f43da97270c78d6cf11dc979b8d716ac2`（`6` 器·增刪 ＝ 閘 `1` 之期：`10`/`5`、`16`/`5`、`4`/`2`、`3`/`1`、`2`/`1`、`504`/`0`） | `347b3b4..9977c86 → verify/W-G.9-388-k961s3`（快轉） |
| 二 | `2ba27a7d6ac4e463edfa551fa177ae10e2ac9575`（`app.py` `+101`／`-39`·施後 blob `7c27fb35be5d5315db501dcddf1d4e9d736812da`·`1848892` B） | **⛔ 推**（審查未符·停機款 `12`）；其全文差異見本檔第十節 |
| 三、四 | ⛔ 做 | — |

- 遠端 heads 之現值為 `48`：較開工多新側支一列，其端 ＝ `9977c86`。主線 ＝ `fd88f64793a373ab921999fbe5b325c44f0c2a4c`，⛔ 變。
- 其餘 `46` 列（除 `ops/queue` 外）⛔ 動。
- `ops/queue` 於本批中另推二列進度（`b91c124`、`114681b`），以免他輪誤判逾時（見第七節）。

## 三、停機款之三值（款·期·實）

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 `fd88f64`、heads `47`、⛔ 含新側支、施工樹乾淨、四簿之值、旗標 `[None×5]`、裝後可匯入 | 皆合（四簿：自誤 `608`／`623`／缺號 `[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`；`VR` `80`／`95`；`K-9` `76`／`79`·缺號皆合）；首驗時 `shapely` 缺 ⇒ 依 README 六之 2 裝之（`pip_install.txt`）後 `rc 0` |
| `2` | 單之三值合、入倉之 blob 同 | 合 |
| `3` | 四塊之 bytes／`sha256`／列數；`git apply --check`；`6` 器之 blob | 合（`Fy39` `50320`／`b4fd3a73…`／`678`；`K30` `15147`／`fd1a3255…`／`97`；`E31` `7578`／`2a990ab2…`／`40`；`P41` `5392`／`eac88e2d…`／`30`；`CK` `1539`／`00cd3949…`／`31`；`GF` `2445`／`b11edb77…`／`47`；`6` 器之 blob ＝ `§五-1` 項 `5`） |
| `4` | 前置 `1`〜`4` | 合（第四節） |
| `5` | 撰碼中之域上歧義 | 撰碼中未察；**審查揭之**（第一節） |
| `6` | `V-1`〜`V-9` ＝ 期；⛔ 改器；配地⛔ 變 | 皆合（第五節） |
| `7` | 推送之目標唯新側支／佇列；⛔ 被拒、⛔ `--force` | 合（佇列之接單之推曾因發單端同時推出而被拒一次 ⇒ 依 README 五重取、`rebase` 後再推·⛔ `--force`） |
| `8` | 工項三之三檔 | ⛔ 及（停於工項二） |
| `9` | 收工閘 | ⛔ 及 |
| `10` | ⛔ 自判正典、⛔ 改塊／器／命令 | 合（⛔ 改；第一節之二讀交發單端） |
| `11` | 新檔⛔ 為 `check-ignore` 所命中 | 合（本單之入倉檔、`probe_WG9388_k961s3.py` 皆 `rc 1`·無命中） |
| **`12`** | 審查之發現⛔ 涉域上判斷或規格之漏載 | **成就**（第一節） |
| `13` | 存取⛔ 被拒 | 合 |

## 四、前置（工項一之端 `9977c86`·倉外之 worktree `/tmp/wpre`·殼無 `WV_`）

- 前置 `1`：六呼叫之 `rc` 與末列逐字合期，見下表之 `#26`、`#38`、`#39`、`#65`、`#66`、`#67`。
- 前置 `2`：其餘呼叫皆 `rc 0`，末列合期。
- 前置 `3`：`#56`〜`#61` 皆 `rc 0`，落檔於 `<O>` ＝ `/tmp/o388`。F8 落檔：`3.5 m` ＝ `8be0160bc14dd92a5331f86eecc995cae0507376`、`0 m` ＝ `6fb86647807f9744594071be25c522b6b506c230`，與 README 六之 5 之雲端之值同。
- 前置 `4`：七字樣各恰 `app.py:1`。
- 68 呼叫：不符 `0`、`stderr` 合計 `0` B。
- 🩸 **首趟為工具之 2 小時時限所斷**（`06:12Z`〜`08:12Z`）：已畢之 `13` 呼叫（`#3`、`#17`、`#18`、`#23`、`#25`、`#33`、`#43`、`#49`、`#55`、`#60`、`#61`、`#67`、`#68`）照其趟取用；中途被斷者⛔ 計，其餘 `55` 呼叫以脫離之行程重跑（`08:12Z`〜`08:47Z`）。每一呼叫唯一趟完整之出艙，皆照實載於下表。

（逐呼叫之表見第九節之甲）

## 五、驗（`2ba27a7`·施工樹 `/tmp/w`·殼無 `WV_`）

- **V-1、V-2**：68 呼叫對「項 8 之表」之施後之列，不符 `0`、`stderr` 合計 `0` B（第九節之乙）。
  - `F32 selftest` 之 K1〜K28 與 P0 `28／28` 皆 ✅；`F32 wiring` 之 X1〜X5 皆 ✅。
  - `F23 selftest`（`#4`）之 `P0 逐項擾動恰該項紅 75／75`。
- **V-3**：`6` 器之 blob ＝ `§五-1` 項 `5`；`verify/` 對工項一之端相異 `0`。
- **V-4**：`k6s3 cmp` 二退縮皆 `rc 0`、末列 `相異 0 項 ⇒ ✅ 同`。
- **V-5**：`parity` 二退縮皆 `⇒ rc 0（不符 0 項）`。以同一字樣 `<HEAD>` 代 `HEAD` 之全值後，落檔與 `stdout` 皆逐位同；對照（⛔ 代之）則皆相異。相異者唯落檔之第 `1` 列（`"head"`）與 `stdout` 之第 `0` 列。
- **V-6**：二 `hash-object` 各二列相等（`8be0160b…`／`8be0160b…`；`6fb86647…`／`6fb86647…`）；`run` 皆 `⇒ 紅 []；rc 0`。
- **V-7**：生產碼 `34` 檔相異唯 `app.py`（`+101`／`-39`·blob `7c27fb35…`）；`verify/` 相異 `0`；頂層之名之集同；相異之節點 ＝ `['k6b_stage3_run']`。
- **V-8**：
  - 「有二受併宗」「承受之宗未定」「§三-2 未定」「所鄰之 B 內街廓 ＝」「def _recv_of(b):」⇒ 各無出艙、`rc 1`。
  - 「於現態未保留」「'後處理(a)'」「def _recv_of(b, y):」「R = _mem - merged_out - _rcv388 - L - _t14_done」「R = R - _stay」⇒ 各 `app.py:1`。
- **V-9**：`stderr` 合計 `0` B。
- **⇒ 本案配地⛔ 變。**

## 六、唯讀獨立審查（`redistribution-reviewer`·⛔ 改檔·⛔ `commit`）之發現與處置

- 逐條 1〜10 皆判「合」：
  - 承受之宗之集；題一之先；唯一者⛔ 須 G；序鍵二層與「宗連同其所併」；重劃前面積之表。
  - R-5 逐受併宗；R-6 之次序（唯第一節之點）；R-7 之列與引數、位置；帳⛔ 另寫；`§三-3` 五款與 R-9。
- 其自重跑諸器皆 `rc 0`；`k6s3` 前後態逐位同。
- 獨立合成之例：
  - 例一（同一街廓二受併宗 ＋ 一照配之宗·相鄰各異）：手算與實得逐值同。
  - 例二（所鄰為零而經二道路片臨二側·F1 之 G 取 `150`／`170`／`160.004` 三值）：逐值同。
  - 例三b（經道路片之受者 K 與自身之相鄰所擇 A1 異）：實得 Y、D1 ⇒ K，同期。
  - 例四b：見第一節。
- **(甲) 純實作之瑕：無。**
- **(乙)**：
  - 1. 第一節 ⇒ 停機款 `12`。
  - 2.（低）③ 之 `min` 對每一候選皆算序鍵，即使相鄰之一層已能定之，試算未回 G 仍停機。reviewer 判其合塊 `K30` 乙之「須擇而……未回 G ⇒ 停機」之讀；真之 `alloc_state` 恆回 G。執行端照實轉呈，⛔ 自判。
- **(丙) NOTE**：
  - 設計說明之 R-9 一句「推導式與 lambda 之變數亦皆以 388 為尾」不實。`R-7` 之 `for x in _p5x388:` 與其推導式重用既有之 `x`；`_key388(p)`、`_ra388(x, b, rof)` 之參數亦用既有之名。其後於函式層⛔ 再讀 `x`，無功能之影響。是否須改為新名，請發單端於次單定之。執行端⛔ 自改（審查已終、已停機）。
  - `補令二 裁五 2` 之舊註「或某受併宗之街廓 ∉ B」與 R-5 之新判已不符；因 R-9 禁動，僅記之。
  - 塊 `K30` 庚之形（題一之已取得之一端另有照配之宗）未另造例。
- reviewer 自承：曾於 `/tmp/w` 跑 `py_compile` 一次，改寫了已存之 `__pycache__/app.cpython-311.pyc`（受 `.gitignore`）；`/tmp/w` 之 `git status` 唯原有之未追蹤之單（執行端.md 丙 3 之複本）。

## 七、自捕與自解

1. **環境**：`shapely` 等缺 ⇒ 依 README 六之 2 以 `python3 -m pip install -r requirements.txt --break-system-packages` 裝之，其後之匯入 `rc 0`。
2. **前置首趟為工具之 2 小時時限所斷** ⇒ 已畢者照用，其餘以脫離之行程重跑（第四節）；施後之 68 呼叫一開始即以脫離之行程跑之，一趟畢。
3. **逾時之防**：本輪自接單至工項二之驗畢逾 5 小時，而佇列與側支逾 3 小時無 `commit` 即視中斷（README 五）⇒ 於 `ops/queue` 之 `log.md` 推進度二列（`16:13`、`18:21`）。
4. **工項一之 `git status --porcelain`**：唯 `6` 器，另有執行端.md 丙 3 所令之施工樹之根之單之複本（未追蹤·⛔ 入倉）。
5. **撰碼中之自查**（於前置跑畢之後·並行 ≤ `2`）：`F32 selftest`／`wiring`、`F23 wiring 7d8e954`、`F24 wiring d7a5ea4`、`F13 wiring`、`F17 wiring` 皆 `rc 0`。撰碼中另將推導式與 lambda 之變數改為以 `388` 為尾之名（`R-7` 之迴圈與參數之名未及·見第六節之丙）。

## 八、耗時（並行 `2`）

| 段 | 時（UTC） | 備 |
|---|---|---|
| 開場、取號、pre-flight、四塊之抽取 | `06:06`〜`06:11` | — |
| 工項零、一（推） | `06:11`〜`06:12` | — |
| 前置 68 呼叫 | `06:12`〜`08:47` | 首趟於 `08:12` 被斷；諸呼叫之耗時之和 `17993` s |
| 撰碼（與前置並行·⛔ 跑器） | `06:20`〜`06:40` | — |
| 自查、工項二之 `commit` | `08:47`〜`08:50` | — |
| 施後 68 呼叫（V-1〜V-6） | `08:50`〜`11:33` | 諸呼叫之耗時之和 `19594` s |
| 唯讀獨立審查 | `11:36`〜`12:26` | — |

主 checkout 之同步由 KL 自行為之（README 六之 6）。

## 九、逐呼叫之表（`rc`·`stderr` B·耗時·末列）

### 甲　前置（工項一之端 `9977c86`）

```
 1 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
 2 ✅ rc 0 err 0 206s | ⇒ 紅 []；rc 0
 3 ✅ rc 0 err 0 541s | ⇒ 紅 []；rc 0
 4 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
 5 ✅ rc 0 err 0 36s | ⇒ 紅 []；rc 0
 6 ✅ rc 0 err 0 37s | ⇒ 紅 []；rc 0
 7 ✅ rc 0 err 0 5s | ⇒ 紅 []；rc 0
 8 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
 9 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
10 ✅ rc 0 err 0 57s | ⇒ 紅 []；rc 0
11 ✅ rc 0 err 0 23s | ⇒ 紅 []；rc 0
12 ✅ rc 0 err 0 363s | ⇒ 紅 []；rc 0
13 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
14 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
15 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
16 ✅ rc 0 err 0 112s | ⇒ 紅 []；rc 0
17 ✅ rc 0 err 0 755s | ⇒ 紅 []；rc 0
18 ✅ rc 0 err 0 1054s | ⇒ 紅 []；rc 0
19 ✅ rc 0 err 0 13s | ⇒ 突變 8（另基準一）；紅 []；rc 0
20 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
21 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
22 ✅ rc 0 err 0 104s | ⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0
23 ✅ rc 0 err 0 646s | ⇒ 紅 []；rc 0
24 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
25 ✅ rc 0 err 0 2806s | ⇒ 紅 []；rc 0
26 ✅ rc 1 err 0 4s | ⇒ 紅 ['W6']；rc 1
27 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
28 ✅ rc 0 err 0 9s | ⇒ 紅 []；rc 0
29 ✅ rc 0 err 0 33s | ⇒ rc 0（不符 0·器紅 0）
30 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
31 ✅ rc 0 err 0 29s | ⇒ 紅 []；rc 0
32 ✅ rc 0 err 0 393s | ⇒ 紅 []；rc 0
33 ✅ rc 0 err 0 541s | ⇒ 紅 []；rc 0
34 ✅ rc 0 err 0 58s | ⇒ 紅 []；rc 0
35 ✅ rc 0 err 0 53s | ⇒ 紅 []；rc 0
36 ✅ rc 0 err 0 11s | ⇒ 紅 []；rc 0
37 ✅ rc 0 err 0 36s | ⇒ 紅 []；rc 0
38 ✅ rc 1 err 0 22s | ⇒ 紅 ['P2 公設片平分須由 BW 承受而其配得之宗二筆 ⇒ 相鄰者先 → G → 重劃前面積 → 暫編地號（W5）']；rc 1
39 ✅ rc 1 err 0 17s | ⇒ 紅 ['W5', 'N4']；rc 1
40 ✅ rc 0 err 0 307s | ⇒ 紅 []；rc 0
41 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
42 ✅ rc 0 err 0 83s | ⇒ 紅 []；rc 0
43 ✅ rc 0 err 0 1346s | ⇒ 紅 []；rc 0
44 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
45 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
46 ✅ rc 0 err 0 261s | ⇒ 紅 []；rc 0
47 ✅ rc 0 err 0 168s | ⇒ 紅 []；rc 0
48 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
49 ✅ rc 0 err 0 541s | ⇒ 紅 []；rc 0
50 ✅ rc 0 err 0 0s | selftest 9/9 ⇒ ✅
51 ✅ rc 0 err 0 0s | selftest 13/13 ⇒ ✅
52 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
53 ✅ rc 0 err 0 2s | ε ＝ 0.0002｜rc 0
54 ✅ rc 0 err 0 16s | 紅項 [] 器紅 0
55 ✅ rc 0 err 0 567s | ⇒ 紅 []；rc 0
56 ✅ rc 0 err 0 316s | {"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)
57 ✅ rc 0 err 0 248s | {"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)
58 ✅ rc 0 err 0 306s | ⇒ 紅 []；rc 0
59 ✅ rc 0 err 0 236s | ⇒ 紅 []；rc 0
60 ✅ rc 0 err 0 681s | ⇒ rc 0（不符 0 項）
61 ✅ rc 0 err 0 505s | ⇒ rc 0（不符 0 項）
62 ✅ rc 0 err 0 7s | ⇒ 紅 []；rc 0
63 ✅ rc 0 err 0 5s | ⇒ 紅 []；rc 0
64 ✅ rc 0 err 0 535s | ⇒ 紅 []；rc 0
65 ✅ rc 1 err 0 2s | ⇒ 紅 ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16', 'K17', 'K18', 'K19', 'K20', 'K21', 'K22', 
66 ✅ rc 1 err 0 4s | ⇒ 紅 ['X1', 'X2', 'X3']；rc 1
67 ✅ rc 1 err 0 1879s | ⇒ 紅 ['X1@甲']；rc 1
68 ✅ rc 0 err 0 1965s | ⇒ 紅 []；rc 0
不符 0 ／ 合計 stderr 0 B ／ 呼叫 68
```

### 乙　施後（`2ba27a7`）

```
 1 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
 2 ✅ rc 0 err 0 230s | ⇒ 紅 []；rc 0
 3 ✅ rc 0 err 0 582s | ⇒ 紅 []；rc 0
 4 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
 5 ✅ rc 0 err 0 42s | ⇒ 紅 []；rc 0
 6 ✅ rc 0 err 0 42s | ⇒ 紅 []；rc 0
 7 ✅ rc 0 err 0 6s | ⇒ 紅 []；rc 0
 8 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
 9 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
10 ✅ rc 0 err 0 65s | ⇒ 紅 []；rc 0
11 ✅ rc 0 err 0 29s | ⇒ 紅 []；rc 0
12 ✅ rc 0 err 0 414s | ⇒ 紅 []；rc 0
13 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
14 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
15 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
16 ✅ rc 0 err 0 128s | ⇒ 紅 []；rc 0
17 ✅ rc 0 err 0 801s | ⇒ 紅 []；rc 0
18 ✅ rc 0 err 0 1114s | ⇒ 紅 []；rc 0
19 ✅ rc 0 err 0 14s | ⇒ 突變 8（另基準一）；紅 []；rc 0
20 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
21 ✅ rc 0 err 0 5s | ⇒ 紅 []；rc 0
22 ✅ rc 0 err 0 113s | ⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0
23 ✅ rc 0 err 0 680s | ⇒ 紅 []；rc 0
24 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
25 ✅ rc 0 err 0 2987s | ⇒ 紅 []；rc 0
26 ✅ rc 0 err 0 55s | ⇒ 紅 []；rc 0
27 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
28 ✅ rc 0 err 0 11s | ⇒ 紅 []；rc 0
29 ✅ rc 0 err 0 37s | ⇒ rc 0（不符 0·器紅 0）
30 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
31 ✅ rc 0 err 0 33s | ⇒ 紅 []；rc 0
32 ✅ rc 0 err 0 430s | ⇒ 紅 []；rc 0
33 ✅ rc 0 err 0 581s | ⇒ 紅 []；rc 0
34 ✅ rc 0 err 0 66s | ⇒ 紅 []；rc 0
35 ✅ rc 0 err 0 61s | ⇒ 紅 []；rc 0
36 ✅ rc 0 err 0 13s | ⇒ 紅 []；rc 0
37 ✅ rc 0 err 0 42s | ⇒ 紅 []；rc 0
38 ✅ rc 0 err 0 26s | ⇒ 紅 []；rc 0
39 ✅ rc 0 err 0 18s | ⇒ 紅 []；rc 0
40 ✅ rc 0 err 0 337s | ⇒ 紅 []；rc 0
41 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
42 ✅ rc 0 err 0 94s | ⇒ 紅 []；rc 0
43 ✅ rc 0 err 0 1457s | ⇒ 紅 []；rc 0
44 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
45 ✅ rc 0 err 0 2s | ⇒ 紅 []；rc 0
46 ✅ rc 0 err 0 274s | ⇒ 紅 []；rc 0
47 ✅ rc 0 err 0 186s | ⇒ 紅 []；rc 0
48 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
49 ✅ rc 0 err 0 581s | ⇒ 紅 []；rc 0
50 ✅ rc 0 err 0 0s | selftest 9/9 ⇒ ✅
51 ✅ rc 0 err 0 0s | selftest 13/13 ⇒ ✅
52 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
53 ✅ rc 0 err 0 3s | ε ＝ 0.0002｜rc 0
54 ✅ rc 0 err 0 18s | 紅項 [] 器紅 0
55 ✅ rc 0 err 0 594s | ⇒ 紅 []；rc 0
56 ✅ rc 0 err 0 351s | {"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)
57 ✅ rc 0 err 0 281s | {"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)
58 ✅ rc 0 err 0 352s | ⇒ 紅 []；rc 0
59 ✅ rc 0 err 0 279s | ⇒ 紅 []；rc 0
60 ✅ rc 0 err 0 747s | ⇒ rc 0（不符 0 項）
61 ✅ rc 0 err 0 543s | ⇒ rc 0（不符 0 項）
62 ✅ rc 0 err 0 8s | ⇒ 紅 []；rc 0
63 ✅ rc 0 err 0 6s | ⇒ 紅 []；rc 0
64 ✅ rc 0 err 0 602s | ⇒ 紅 []；rc 0
65 ✅ rc 0 err 0 3s | ⇒ 紅 []；rc 0
66 ✅ rc 0 err 0 4s | ⇒ 紅 []；rc 0
67 ✅ rc 0 err 0 2140s | ⇒ 紅 []；rc 0
68 ✅ rc 0 err 0 2061s | ⇒ 紅 []；rc 0
不符 0 ／ 合計 stderr 0 B ／ 呼叫 68
```

### 丙　V-4〜V-6

```
V-4 cmp 35: rc 0 stderr 0 B 末列 相異 0 項 ⇒ ✅ 同
V-4 cmp 00: rc 0 stderr 0 B 末列 相異 0 項 ⇒ ✅ 同
V-5 parity 35: 正規化後 落檔同 True／stdout 同 True｜對照（⛔ 代）落檔同 False／stdout 同 False｜相異列 落檔 [1]／stdout [0]
   落檔相異列： [' "head": "2ba27a7d6ac4e463edfa551fa177ae10e2ac9575",'] ｜stdout 相異列： ['【F4 parity】態 2ba27a7d6ac4e463edfa551fa177ae10e2ac9575·退縮 3.5·WV_K6B_STAGE3=on·擾動 False']
V-5 parity 00: 正規化後 落檔同 True／stdout 同 True｜對照（⛔ 代）落檔同 False／stdout 同 False｜相異列 落檔 [1]／stdout [0]
   落檔相異列： [' "head": "2ba27a7d6ac4e463edfa551fa177ae10e2ac9575",'] ｜stdout 相異列： ['【F4 parity】態 2ba27a7d6ac4e463edfa551fa177ae10e2ac9575·退縮 0.0·WV_K6B_STAGE3=on·擾動 False']
V-6 hash-object 35: ['8be0160bc14dd92a5331f86eecc995cae0507376', '8be0160bc14dd92a5331f86eecc995cae0507376'] 相等 True
V-6 hash-object 00: ['6fb86647807f9744594071be25c522b6b506c230', '6fb86647807f9744594071be25c522b6b506c230'] 相等 True
```

### 丁　V-8

```
[有二受併宗]  rc=1
[承受之宗未定]  rc=1
[§三-2 未定]  rc=1
[所鄰之 B 內街廓 ＝]  rc=1
[def _recv_of(b):]  rc=1
[於現態未保留] app.py:1
 rc=0
['後處理(a)'] app.py:1
 rc=0
[def _recv_of(b, y):] app.py:1
 rc=0
[R = _mem - merged_out - _rcv388 - L - _t14_done] app.py:1
 rc=0
[R = R - _stay] app.py:1
 rc=0
```

### 戊　V-7

```
生產碼之檔數 34 34 同集 True
生產碼相異 ['app.py']
verify/ 相異 （無）
101	39	app.py | blob 7c27fb35be5d5315db501dcddf1d4e9d736812da
頂層之名之集同 True ｜相異之節點 ['k6b_stage3_run']
```

## 十、`app.py` 之全文差異（`git diff 9977c86 2ba27a7 -- app.py`·⛔ 推·供發單端復驗與次單）

````diff
diff --git a/app.py b/app.py
index efae3a5..7c27fb3 100644
--- a/app.py
+++ b/app.py
@@ -14680,6 +14680,13 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
       唯一 ⇒ 照舊。上文「距離 → `k967_rank`」於建地之片之他街廓之候選不再適用（其為五級與深度同者之序）；道路、公設地之片照舊。
       `blk5` ＝ 五級之街廓屬性之回呼（`blk5() -> adj_block_ctx 之回傳`·`k971_blk5`）：首次須比時呼之一次、存之（同一次之段三
       之內共用）；須比而缺或其回傳非 `dict` ⇒ 停機（⛔ 以距離代之）；⛔ 須比者⛔ 呼之。
+    🔧 `W-G.9-388`（`K-9-61` ①②③⑥·KL 裁 `2026-10-06 01:29`；`2026-10-18 08:03`／`08:14`）：後處理之某街廓之承受之宗 ＝ 該群
+      於該街廓之本段之受併宗（同一街廓之左右兩端可二）∪ 照配之宗（該群之依原位次配得而保留之建地·有受併宗之街廓者亦照配、
+      ⛔ 併入受併宗）；二以上 ⇒ 與所承受之片相鄰（宗連同其於本段整筆併入之片）者先 → `k967_rank`（試算之 G → 重劃前面積
+      〔同第 5 項之表之式〕→ 暫編地號），唯一者⛔ 須 G；題一之未得之一端之候選先（同前）。分不到之建地所鄰之已配得街廓二以上
+      ⇒ 本街廓先，否則其承受之宗之序鍵最小（應分配面積較大）之一側；為零 ⇒ 本街廓有同一地主之已配得之宗者依第 5 項之輪，否則
+      經該群之與之相鄰之道路片（⛔ 已併出·⛔ 穿越）之遠半臨另一側之已配得街廓者向該側併（隨其道路片之受者·手冊道路用地分配
+      原則第 2 點），仍為零 ⇒ 依第 5 項之輪（整筆·於整批試與其諸輪之後另為一輪）。受併宗於試算未保留之停機改以逐受併宗判。
     """
     import copy as _cp
     from shapely.geometry import Polygon as _Pg, LineString as _Ls
@@ -15491,48 +15498,75 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
     # 🔧 `W-G.9-373`（R-7 ①）：諸合併群之計畫皆以步驟 10 之前之一次之試算定之（諸群共用），依群之序併為一表 `_tab`
     _cur = None
     _tab = []
+    # 🔧 `W-G.9-388`（`K-9-61` ⑥·R-6 (二)）：所鄰為零而⛔ 經道路片者之串列（跨群·依處置之序）與經道路片之受者
+    #   （{片: {街廓: [受者…]}}）——其片⛔ 入 (a) 之計畫，於整批試與其第 1 輪、第 5 項之輪之後另為一次第 5 項之輪（R-7）
+    _p5x388, _via388 = [], {}
+
+    def _key388(p):
+        # 🔧 `W-G.9-388`（`K-9-61` ①·R-4）：序鍵 ＝ k967_rank(試算之 G, 重劃前面積〔同第 5 項之表之式〕, p)；試算⛔ 回 G
+        #   或其中無 p ⇒ 停機（⛔ 以 0 代之）
+        _G388 = _cur.get("G")
+        if not isinstance(_G388, dict) or p not in _G388:
+            raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {p}：試算未回 G——承受之宗之序鍵無從定之（停機款 9）")
+        return k967_rank(_G388[p], k967_pre_area(p, _cm388.get(p), _pa388), p)
+
+    def _ra388(x, b, rof):
+        # 🔧 `W-G.9-388`（R-6）：(a) 之受者——x 經道路片而臨 b 者 ⇒ 其經道路片之受者（唯一 ⇒ 之；二以上 ⇒ 序鍵最小者）；
+        #   否則 rof(b, x)（該群之 _recv_of）
+        _vs388 = sorted(set(_via388.get(x, {}).get(b, [])))
+        if not _vs388:
+            return rof(b, x)
+        if len(_vs388) == 1:
+            return _vs388[0]
+        return min(_vs388, key=_key388)
     for _gi in _seen_g:
         _mem = set(_groups[_gi])
+        # 🔧 `W-G.9-388`（`K-9-61` ①·R-1）：同一街廓之受併宗可二以上（左右兩端）⇒ {街廓: [受併宗…]}（依 successes 之序）
         _recv_by_blk = {}
         for _g2, _c2, _b2 in successes:
             if _g2 == _gi:
-                if _b2 in _recv_by_blk and _recv_by_blk[_b2] != _c2:
-                    raise RuntimeError(
-                        f"🔴 [K-6-B 段三 後處理] 群 {sorted(_mem)} 於街廓 {_b2} 有二受併宗"
-                        f"（{_recv_by_blk[_b2]}／{_c2}）⇒ 停機款 9")
-                _recv_by_blk[_b2] = _c2
+                _recv_by_blk.setdefault(_b2, [])
+                if _c2 not in _recv_by_blk[_b2]:
+                    _recv_by_blk[_b2].append(_c2)
+        _rcv388 = {_c388 for _cs388 in _recv_by_blk.values() for _c388 in _cs388}
         _cl0 = _closer.get(_gi)
-        R = _mem - merged_out - set(_recv_by_blk.values()) - L - _t14_done   # 補令一 `X-3′`：扣 `R-7` 所處置之候選
+        R = _mem - merged_out - _rcv388 - L - _t14_done   # 補令一 `X-3′`：扣 `R-7` 所處置之候選
         if not R:
             continue
         if _cur is None:
             _cur = alloc_state(state["temp"], state["build"])
             if _cur.get("err"):
                 raise RuntimeError(f"🔴 [K-6-B 段三 後處理] 現態配地中止：{_cur['err']!r}（停機款 9）")
+            # 🔧 `W-G.9-388`（R-4）：序鍵之表（首次之試算之後各立一次）——試算之 members 與重劃前面積之表（現態之每一片之
+            #   分攤登記面積 − 其段三部分併出之和，再以 k967_pool_less 減試算之 pool_out·同第 5 項之輪之式）
+            _cm388 = _cur.get("members") if isinstance(_cur.get("members"), dict) else {}
+            _pa388 = k967_pool_less(
+                {_q388: float(_u388.get('分攤登記面積_m2', 0) or 0)
+                 - sum(float(_w388) for _w388 in (_u388.get('段三部分併出') or {}).values())
+                 for _q388, _u388 in state["by"].items()}, _cur.get("pool_out"))
         B = sorted({_blk_of[m] for m in _mem
                     if _kind(m) == 'bld' and m in _cur["kept"].get(_blk_of[m], set())})
         # 🆕 `W-G.9-354`（`K-9-48` 其二·讀法 `1` ⑤·`K-9-50` 題一 4）：該群於本段無受併宗之街廓，其依原位次配得之宗
         #   照配（⛔ 動）；分往該街廓之土地由其配得之宗承受（`_recv_of`）
-        _stay = {m for m in _mem if _kind(m) == 'bld' and _blk_of[m] in B and _blk_of[m] not in _recv_by_blk
+        # 🔧 `W-G.9-388`（`K-9-61` ③·R-2）：有受併宗之街廓之依原位次配得之宗亦照配（⛔ 動、⛔ 併入受併宗）、亦為承受之宗
+        _stay = {m for m in _mem if _kind(m) == 'bld' and _blk_of[m] in B and m not in _rcv388
                  and m in _cur["kept"].get(_blk_of[m], set())}
         R = R - _stay
-        _orig = {}
-
-        def _recv_of(b):
-            # 受併宗：本段之受併宗；無 ⇒ 題一未得之一端取其候選（現態配得者），他街廓唯恰一宗配得者；餘 ⇒ 停機
-            if b in _recv_by_blk:
-                return _recv_by_blk[b]
-            if b not in _orig:
-                _kb = sorted(m for m in _stay if _blk_of[m] == b)
-                if _cl0 is not None and b == _cl0['敗']['blk'] and _cl0['敗']['c'] in _kb:
-                    _orig[b] = _cl0['敗']['c']
-                elif len(_kb) == 1:
-                    _orig[b] = _kb[0]
-                else:
-                    raise RuntimeError(
-                        f"🔴 [K-6-B 段三 後處理] 街廓 {b} 有群 {sorted(_mem)} 之保留宗 {_kb} 而無本段之受併宗"
-                        "——承受之宗未定（停機款 9）")
-            return _orig[b]
+
+        def _recv_of(b, y):
+            # 🔧 `W-G.9-388`（`K-9-61` ①②·R-3）：街廓 b 之承受之宗 ＝ 本段之受併宗 ∪ 照配之宗；y ＝ 所承受之片。
+            #   ① b 無本段之受併宗而為題一之未得之一端、其候選為承受之宗 ⇒ 之；② 唯一 ⇒ 之（⛔ 須 G）；③ 二以上 ⇒
+            #   與 y 相鄰（宗連同其於本段整筆併入之片）者先 → 序鍵（應分配面積 → 重劃前面積 → 暫編地號）
+            _hs388 = list(_recv_by_blk.get(b, [])) + sorted(m for m in _stay if _blk_of[m] == b)
+            if b not in _recv_by_blk and _cl0 is not None and b == _cl0['敗']['blk'] and _cl0['敗']['c'] in _hs388:
+                return _cl0['敗']['c']
+            if len(_hs388) == 1:
+                return _hs388[0]
+
+            def _nx388(_e388):
+                _ws388 = [_e388] + sorted(_z388 for _z388 in merged_out if _e388 in marks.get(_z388, set()))
+                return 0 if any(_adj(y, _z388) for _z388 in _ws388) else 1
+            return min(_hs388, key=lambda _e388: (_nx388(_e388), _key388(_e388)))
         if not R:
             continue
         # 🔧 補令二 裁五 2：B 為空、或某受併宗之街廓 ∉ B ⇒ 停機款 9（⛔ 靜默略過·⛔ 除以 0）
@@ -15540,31 +15574,52 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             raise RuntimeError(
                 f"🔴 [K-6-B 段三 後處理] 群 {sorted(_mem)} 之 B 為空（現態無保留之建築成員）"
                 f"而待處置者 {sorted(R)} 非空（停機款 9）")
-        _recv_out = sorted(b for b in _recv_by_blk if b not in B)
+        # 🔧 `W-G.9-388`（`K-9-61` ④ 之防·R-5）：逐受併宗判（同一街廓二受併宗而其一未保留者亦停機）
+        _recv_out = sorted(_c388 for _c388 in _rcv388 if _c388 not in _cur["kept"].get(_blk_of[_c388], set()))
         if _recv_out:
             raise RuntimeError(
-                f"🔴 [K-6-B 段三 後處理] 群 {sorted(_mem)} 之受併宗所在街廓 {_recv_out} ∉ B {B}"
+                f"🔴 [K-6-B 段三 後處理] 群 {sorted(_mem)} 之受併宗 {_recv_out} 於試算⛔ 保留"
                 "（受併宗於現態未保留·停機款 9）")
         _plan = []      # (類, x, [(recv, qty)], whole, 鄰接, 鄰接半片)
         _ga = lambda x: (-float(_by0[x].get('幾何面積_m2', 0) or 0), x)
         _cls = {'a': [], 'b': [], 'c': []}
+        _own388 = own_map or {}
         for x in sorted(R):
             _k = _kind(x)
             if _k == 'bld':
-                _kept_x = x in _cur["kept"].get(_blk_of[x], set())
-                if _blk_of[x] in B and _kept_x:
-                    raise RuntimeError(
-                        f"🔴 [K-6-B 段三 後處理] {x}（{_blk_of[x]}）為 B 內之保留建築片而非受併宗"
-                        "——§三-2 未定（停機款 9）")
                 if _cl0 is not None and _blk_of[x] == _cl0['敗']['blk']:
                     # 🆕 `W-G.9-354`（`K-9-50` 題一 4）：未得之一端之地主土地不能依原位次配地者 ⇒ 併入已取得之一端
                     _cls['a'].append((x, _cl0['勝']['blk']))
                     continue
                 _tb = sorted({b for b in B for m in _mem
                               if _blk_of[m] == b and m != x and _adj(x, m)})
-                if len(_tb) != 1:
-                    raise RuntimeError(
-                        f"🔴 [K-6-B 段三 後處理 (a)] {x} 所鄰之 B 內街廓 ＝ {_tb}（期恰 1）（停機款 9）")
+                # 🔧 `W-G.9-388`（`K-9-61` ⑥·KL `2026-10-18 08:03` 第 2 點·R-6）：所鄰為零 ⇒（一）本街廓無同一地主之已配得
+                #   之宗者，經該群之與之相鄰之道路片（⛔ 已併出·⛔ 穿越）之遠半臨 B 內街廓（手冊道路用地分配原則第 2 點）；
+                #   （二）仍為零 ⇒ 入串列（第 5 項·R-7）；（三）二以上 ⇒ 本街廓先，否則 (a) 之受者之序鍵最小之街廓；（四）恰一
+                if not _tb:
+                    _gx388 = str(_own388.get(str(_by0[x].get('原地號', '') or ''), '') or '')
+                    _same388 = any(
+                        _p388 != x and _p388 not in merged_out and _p388 in state["by"]
+                        and str(_own388.get(str(state["by"][_p388].get('原地號', '') or ''), '') or '') == _gx388
+                        for _p388 in sorted(_cur["kept"].get(_blk_of[x], set())))
+                    if not _same388:
+                        for _d388 in sorted(_mem):
+                            if _kind(_d388) != 'road' or _raw[_d388] is None or _d388 in merged_out \
+                                    or _is_crossing(_d388) or not _adj(x, _d388):
+                                continue
+                            for _h388 in _road_halves(_d388, '後處理·經道路片'):
+                                _nb388 = _nbr_blocks(_h388, _blk_of[_d388])
+                                if _blk_of[x] in _nb388:
+                                    continue
+                                for _b388 in sorted(set(_nb388) & set(B)):
+                                    _via388.setdefault(x, {}).setdefault(_b388, []).append(_recv_of(_b388, _d388))
+                        _tb = sorted(_via388.get(x, {}))
+                if not _tb:
+                    _p5x388.append(x)
+                    continue
+                if len(_tb) >= 2:
+                    _tb = [_blk_of[x]] if _blk_of[x] in _tb else [
+                        min(_tb, key=lambda _t388: _key388(_ra388(x, _t388, _recv_of)))]
                 _cls['a'].append((x, _tb[0]))
             elif _k == 'road' and not _is_crossing(x):
                 _cls['b'].append(x)
@@ -15573,7 +15628,8 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             else:
                 raise RuntimeError(f"🔴 [K-6-B 段三 後處理] {x} 之類別無從歸入 (a)(b)(c)（停機款 9）")
         for x, b in sorted(_cls['a'], key=lambda p: _ga(p[0])):
-            _plan.append(('a', x, [(_recv_of(b), _aprime(state, x, _recv_of(b)))], True,
+            _r388 = _ra388(x, b, _recv_of)    # 🔧 `W-G.9-388`（R-6）：(a) 之受者
+            _plan.append(('a', x, [(_r388, _aprime(state, x, _r388))], True,
                           _nbr_blocks(_raw[x], _blk_of[x]), None))
         for x in sorted(_cls['b'], key=_ga):
             _rb = _blk_of[x]
@@ -15591,16 +15647,16 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
             if not _ones:
                 _plan.append(('b', x, [], False, _nbr_blocks(_raw[x], _rb), _half_log))
             elif len(_ones) == 1:
-                _recv = _recv_of(_ones[0][1][0])
+                _recv = _recv_of(_ones[0][1][0], x)
                 _plan.append(('b', x, [(_recv, _aprime(state, x, _recv))], False,
                               _nbr_blocks(_raw[x], _rb), _half_log))
             else:
-                _qs = [(_recv_of(h[1][0]),
-                        _aprime(state, x, _recv_of(h[1][0])) * (h[0].area / _geo[x].area))
+                _qs = [(_recv_of(h[1][0], x),
+                        _aprime(state, x, _recv_of(h[1][0], x)) * (h[0].area / _geo[x].area))
                        for h in _halves]
                 _plan.append(('b', x, _qs, False, _nbr_blocks(_raw[x], _rb), _half_log))
         for x in sorted(_cls['c'], key=_ga):
-            _recvs = [_recv_of(b) for b in B]
+            _recvs = [_recv_of(b, x) for b in B]
             _plan.append(('c', x, [(r, _aprime(state, x, r) / len(B)) for r in _recvs], False,
                           _nbr_blocks(_raw[x], _blk_of[x]), None))
         _tab.extend(_plan)
@@ -15665,6 +15721,12 @@ def k6b_stage3_run(order, locked, own_map, temp_parcels, build_parcels, blocks,
         for x in _xs10:
             if _kind(x) != 'bld':
                 _left[x] = max(0.0, _rem10.get(x, 0.0))
+    if _p5x388:
+        # 🔧 `W-G.9-388`（`K-9-61` ⑥·R-7）：所鄰為零而⛔ 經道路片者 ⇒ 逐片記一列，再依第 5 項之輪（整筆之來源量）
+        for x in _p5x388:
+            _row(序='後處理', 街廓=_blk_of[x], 候選=x, 層級=_lvl_name['a'], 結果='依第5項',
+                 鄰接街廓=_nbr_blocks(_raw[x], _blk_of[x]))
+        _p5_373(list(_p5x388), {x: _a357(x) for x in _p5x388}, {})
 
     for _pid, _rs in marks.items():
         state["by"][_pid]['段三併出'] = sorted(_rs)
````
