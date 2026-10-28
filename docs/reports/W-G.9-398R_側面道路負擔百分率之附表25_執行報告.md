# `W-G.9-398R`　執行報告：街角地側面道路負擔百分率（`Rw`）改照手冊附表 25（新側支 `verify/W-G.9-398-rw25`·**本案配地改變·⛔ 入主線·待 KL 核**）

> **受單** ＝ 執行端（雲端排程「市地重劃·執行端」·Linux·`nproc` ＝ `4`·Python `3.11.17`）。**單** ＝ `docs/orders/W-G.9-398_規格單.md`（`150064` B·`sha256` `beb469830bda6218299a0e0b7ea24c3794765bc079441235c43a959f1d052d18`·`SELF_SHA256` `8229402e08566a9a55ce8e1c96fa592e5d9565c102646abb8fbc35ed98f64e76`）。
> **開工態** ＝ 主線 `wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`（全程⛔ 動）。施工樹 ＝ `/tmp/w`（雲端之完整複本）；`<O>` ＝ `/tmp/claude-0/-home-user-land-readjustment-trial/cc1a1df7-ac5a-5b58-9247-98c0d49e58f0/scratchpad/O`（倉外·⛔ 在任何 git 工作樹之內·`git rev-parse --show-toplevel` ⇒ `fatal: not a git repository`）。
> **結果** ＝ 工項零〜四皆畢、皆推至新側支；`V-1`〜`V-9` 皆合期；**本案配地之改變 ＝ 單 `§一` 項 `5`**（3.5 m `7` 項／0 m `12` 項·逐字同）；唯讀獨立審查無擋者（其 (A) 一項已修而重驗）；停機款 `0` 款成就。收工閘之實測值見 `ops/queue` 之回報（⛔ 寫入本檔·自指）。

---

## ① 逐 `commit` 之 hash 與工項

| 工項 | `commit` | 首列（逐字＝單 `§四-1` 所令） | 推送 |
|---|---|---|---|
| 零 | `96c06e9a1e5e048ffa38e41d0e49f146dec36fcf` | `W-G.9-398 工項零：本單原封入倉（新側支）⛔ 零生產碼` | `HEAD:refs/heads/verify/W-G.9-398-rw25`（新立·`* [new branch]`） |
| 一 | `07d12028d99b3a178c2a87edaea0b70ae8a754ac` | `W-G.9-398 工項一：量測器（F41 之新器·既有之器之增許與更錨）（新側支）⛔ 零生產碼` | `96c06e9..07d1202`（快轉） |
| 二 | `c35d32a3cd43da5bdcb1c197d16b5757a1b39861` | `W-G.9-398 工項二：街角地側面道路負擔百分率改照手冊附表 25（KL 2026-10-26 09:53）🔴 生產碼（新側支）` | `07d1202..c35d32a`（快轉·驗與審查皆符後） |
| 三 | `0dad1a006eb4d58d2be6268047ae0838e64592e8` | `W-G.9-398 工項三：側面道路負擔百分率之附表 25 之入典·待落地清單之更新（新側支）⛔ 零生產碼` | `c35d32a..0dad1a00`（快轉） |
| 四 | 本檔所在之 `commit`（自指·其 hash 見回報） | `W-G.9-398 工項四：執行報告入倉（新側支）⛔ 零生產碼` | 快轉 |

各 `commit` 之訊息 ＝ 首列（逐字）＋ 空一列 ＋ 受單側之環境所附之尾列（`Co-Authored-By`、`Claude-Session` 二列）·以 `git commit -F` 為之。

🔎 **工項二之 `commit` 之更替（推前·⛔ 改寫已推之史）**：工項二首撰 ＝ `a18efd9d56c051fc03633f8a1a61fd350be11707`（`app.py` `+49`／`−12`·blob `ec346de63179b1d8538ed71354c042c2741b4f7c`），其 `V-1`〜`V-9` 首趟皆合期；唯讀獨立審查揭 (A) 一項（⑥ 之 `A-1`）⇒ 依單「純實作之瑕 ⇒ 執行端修之、重驗 `V-1`〜`V-9`、於報告具名」修之，以 `git commit --amend`（**未推之本地 `commit`**）成 `c35d32a`（`app.py` `+51`／`−12`·blob `87e784a3865242519e770d376b65ebe7e89493ec`），其 `V-1`〜`V-9` 從頭重跑（次趟）皆合期而後推。`a18efd9` 從未推送（遠端之史無之）。

---

## ② 停機款 `1`〜`13` 之三值

| 款 | 期 | 實 |
|---|---|---|
| `1` | 主線 ＝ `20e03bf`；濾後之列 ＝ `55` 而⛔ 含 `verify/W-G.9-398-rw25`；追蹤檔無變動；`§零-0` 項 `3` `rc 0` 而四簿之值 ＝ 期；殼之旗標 ＝ `[None×5]`；環境可匯入 | 主線 `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`；列數 `55`、`398` 之列 `0`；`git status --porcelain --untracked-files=no` 空；`probe_WG9321_issuer_anchor.py … 641 640` ⇒ `rc 0`、四簿 ＝ 自誤 `626`／`641`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`、`GB` `199`／`207`／`[12, 87, 179, 181, 183, 184, 185, 203]`、`VR` `80`／`95`／`[73, 75]`、`K-9` `77`／`80`／`[44, 47]`；旗標 `[None, None, None, None, None]`；匯入 `rc 0`（裝後）⇒ ⛔ 成就 |
| `2` | `SELF_SHA256` 自驗符；`STATE.json` 之 bytes／`sha256` 符；入倉之 blob ＝ 來源 | 自驗 `8229402e08566a9a…` 符；`150064` B／`beb469830bda…` 符；`git cat-file blob HEAD:docs/orders/W-G.9-398_規格單.md` 與 `ops/queue` 之 `orders/` 之檔 `cmp` 同 ⇒ ⛔ 成就 |
| `3` | 三塊之 bytes／`sha256`／列數 ＝ `§五-1`；`git apply --check` 過；寫出後之 blob ＝ 項 `5` | 見 ④；`--check` `rc 0`；`17` 檔之 blob 皆 ＝ 項 `5` ⇒ ⛔ 成就 |
| `4` | 工項二前置之期皆符 | (甲) `47`、(乙) `6` 呼叫皆合；(丙) 沿用（前提皆同）；前置 `4` 之二字樣皆無出艙、`rc 1` ⇒ ⛔ 成就 |
| `5` | ⛔ 有規格之歧義而涉域判；⛔ 須改禁改 | 無 ⇒ ⛔ 成就 |
| `6` | `V-1`〜`V-9` 皆合期；⛔ 改器；本案配地之改變 ＝ `§一` 項 `5` | 首趟（`a18efd9`）、次趟（`c35d32a`）皆合；器⛔ 改；改變 ＝ `§一` 項 `5`（逐字·程式比）⇒ ⛔ 成就 |
| `7` | 推送之目標唯新側支／`ops/queue`；⛔ 被拒、⛔ `--force`；主線⛔ 推進 | 目標皆合；皆快轉而成；主線 `20e03bf`（⛔ 變）⇒ ⛔ 成就 |
| `8` | 二檔之刪除欄 `0`、嚴格前綴、尾 ＝ 塊、blob ＝ 項 `5`；`checkidx` `rc 0` 而末列 ＝ 期；`gen_fa_index` ＝ 期而逐位同 | 皆合（見 ④、⑨）⇒ ⛔ 成就 |
| `9` | 收工閘皆合 | 見 `ops/queue` 之回報（自指·⛔ 入本檔） |
| `10` | ⛔ 作正典之判、⛔ 改塊／器／命令以求過；塊之文與倉之事實相符 | ⛔ 為之；塊與倉之事實無不符之處 ⇒ ⛔ 成就 |
| `11` | 新檔⛔ 為 `git check-ignore -v --no-index` 所命中 | 本單 `rc 1`、`probe_WG9398_rw25.py` `rc 1`（無命中）；報告二檔見閘 `2` ⇒ ⛔ 成就 |
| `12` | 審查之發現⛔ 涉域判或規格之漏載 | 審查之 (B) 二項皆非本單之域判之未定（見 ⑥ 之 `B-1`、`B-2`）⇒ ⛔ 成就 |
| `13` | 存取⛔ 被拒；寫入⛔ 為分類器所拒 | 無 ⇒ ⛔ 成就 |

---

## ③ 前置與驗之出艙

### ③-0　`§零-0` 之開場

1. context 餘量：足（約 `14.9 M` tokens）；`nproc` ＝ `4`。
2. 見 ② 款 `1`；`<O>/heads_before_398.txt` ＝ 開工時之濾後之 `55` 列。
3. `probe_WG9321_issuer_anchor.py /tmp/w <O>/pre/issuer_anchor_0.txt 641 640` ⇒ `rc 0`·`stderr` `0` B；項4′ 之「四簿期末復查」：

```
   簿      框之出處                                                 相異       MAX      缺號集
   自誤     VR-091 補款二 ① ＋ 範圍框                                   626      641      [106, 355, 356, 357, 489, 492, 499, 511, 519]
   GB     VR-093（GB-116 三框聯集·扣哨兵 997）                          199      207      [12, 87, 179, 181, 183, 184, 185, 203]
   VR     VR-092 就地加註所引（扣哨兵 999）                               80       95       [73, 75]
   K-9    W-G.9-266 工項四 四-1                                    77       80       [44, 47]
```

4. 見 ② 款 `2`。
5. 環境：初 `import shapely…` ⇒ `ModuleNotFoundError: No module named 'shapely'`（`rc 1`）⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`）⇒ 所裝之版異於基準（`certifi-2026.10.23`、`pandas-3.1.0`、`python-dateutil-3.0.0`、`starlette-1.10.0`、`streamlit-1.66.1`、`websockets-17.3`、`tzdata-2026.5` 等）⇒ 依 `§零-0` 項 `5` 釘回：`python3 -m pip install certifi==2026.10.18 pandas==3.0.6 pillow==12.3.0 python-dateutil==2.9.0.post0 streamlit==1.66.0 websockets==17.2 starlette==1.9.0 --break-system-packages`（`rc 0`）、`python3 -m pip uninstall -y tzdata --break-system-packages`（`rc 0`）；其後匯入 `rc 0`。殼之旗標之出艙 `[None, None, None, None, None]`。
6. 版本之比對：`python3 --version` ＝ `Python 3.11.17`；`python3 -m pip freeze` 之全文（`1114` B·`64` 列）之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac` ＝ 基準 `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f.md` 之所載；主線之端 ＝ 基準之 sha ⇒ **三者皆同**。

### ③-1　pre-flight（`§零-3`）

`python3 verify/probes/probe_order_preflight.py /tmp/w/W-G.9-398_規格單.md` ⇒ `rc 0`：

```
── 🔴 機械·停機款：0 項 ──

── 🟡 提示·須逐項處置：4 項 ──
  [P-2] :231  🟡 框⛔ 無 `^` 錨而同段未依 `CLAUDE.md:725` 二數並報：| # | 受詞 | 值（發單端擬本單時以程式重算） |
  [P-4] :74   🟡 方向性轉引而同段⛔ 未具名座標系：| # | 項 | 值 |
  [P-4] :179  🟡 方向性轉引而同段⛔ 未具名座標系：| # | 受詞 | 期 |
  [P-4] :212  🟡 方向性轉引而同段⛔ 未具名座標系：| 閘 | 受詞 | 期 |

── ℹ️ 記錄：2 項 ──
  [P-5] :1266 SELF_SHA256 ✅ 相符（取檔內**最末**一個·受詞 149986 B）｜實算 8229402e08566a9a…／單載 8229402e08566a9a…
  [P-3] :-    `app.py` 之 `def main` 區間（AST 實查）＝ `23940`-`31683`
```

逐項再處置：🟡 四項 ＝ 單 `§五-1` 項 `9` 之具名豁免（`P-2` `:231`、`P-4` `:74`、`:179`、`:212`）逐列同 ⇒ 豁免；`P-5` ✅；`P-3` 為記錄（施前 `app.py` 之 `main` 之區間）；`P-1`／`P-6`／`P-7` 無出艙。

### ③-2　工項二之前置

- **(甲)** `47` 呼叫、**(乙)** `6` 呼叫：於工項一之端（`07d1202`·施工樹 `/tmp/w`）照跑·並行 `2`（二工作者以「認領」分之·逐呼叫落檔）；**皆合期**：`#17`、`#18`、`#23`、`#16`、`#80`、`#92`、`#93`、`#94` ⇒ `rc 1` 而末列 ＝ 表之工項一之端之列；其餘 `rc 0` 而末列 ＝ 表之列；`stderr` 合計（`#94` 除外）`0` B；`#94` 之 `stderr` `516` B（發單端 `522` B·其差 ＝ 路徑之長·單已預告），其末列 `AssertionError: app.py 缺 module 級常數 ['RW_TABLE_25']——被改名或刪除？`（含「RW_TABLE_25」）。(乙) 之 `f8_pre_35.json`、`f8_pre_00.json` 之 `git hash-object` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`、`884e91714a79288406faa4def6518847de36de39`（＝ 期）。逐呼叫之 `rc`／`stderr`／耗時／末列見 ③-6 之表；(甲)(乙) 之 `stdout` 之全文見附錄子。
- **(丙)** `41` 呼叫：`§零-0` 項 `6` 之比對三者皆同（③-0 項 `6`）⇒ **沿用** `ops/queue` 之 `基準/20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f.md` 之值、⛔ 重跑（③-6 之表中標「沿用」）。
- **前置 `4`**：`git grep -c -F "RW_TABLE_25" -- app.py` ⇒ 無出艙、`rc 1`；`git grep -c -F "附表 25" -- app.py` ⇒ 無出艙、`rc 1`。

### ③-3　驗（`V-1`〜`V-9`·次趟 `c35d32a` 為準；首趟 `a18efd9` 並載）

| # | 期 | 實（次趟 `c35d32a`） | 首趟 `a18efd9` |
|---|---|---|---|
| `V-1` | `47` 呼叫皆 `rc 0`、末列 ＝ 施後之列；`F41` `T1`〜`T9`、`P0 9／9`、`X1`〜`X7` ✅ | 皆合（`#92` `⇒ 紅 []；rc 0`·`P0 判式自驗 9／9`；`#93` `X1`〜`X7` ✅） | 皆合 |
| `V-2` | 其餘 `41` 呼叫皆 `rc 0`、末列 ＝ 施後之列；`F23 selftest` `P0 逐項擾動恰該項紅 75／75` | 皆合（`#4` 之 `✅ P0 逐項擾動恰該項紅 75／75`） | 皆合 |
| `V-3` | `17` 檔之 blob ＝ 項 `5` | 皆 ＝（程式比 `True`） | 同 |
| `V-4` | `run` 皆 `rc 0`；`F36 diff` `rc 0`、全文 ＝ `§一` 項 `5`；`cmp` ＝ 所載 | 見 ③-4（與首趟逐位同） | 同 |
| `V-5` | `parity` `rc 0`·`⇒ rc 0（不符 0 項）`；落檔與 `stdout` 之差唯所載 | 見 ③-5 | 同 |
| `V-6` | `run` `rc 0`·`⇒ 紅 []；rc 0`；施後 `13c04b45…`／`f27849f5…`；逐欄之差唯所載 | 見 ③-5 | 同 |
| `V-7` | 生產碼相異恰 `1`（`app.py`）；`verify/` 相異 `0`；頂層 ＝ `§三-3` 第 `4` 款 | `M app.py`（唯此）·`+51`／`−12`·blob `87e784a3865242519e770d376b65ebe7e89493ec`（`1895636` B）；`verify/` 相異 `0`；AST：頂層之名之增 `['RW_TABLE_25']`、減 `[]`、相異之節點 `['RW_TABLE_25', 'rw_from_width']` | `+49`／`−12`·blob `ec346de6…`；餘同 |
| `V-8` | 「RW_TABLE_25」≥ `2`；「附表 25」≥ `1` | `app.py:6`；`app.py:5` | `5`；`4` |
| `V-9` | `V-1`〜`V-6` 之 `stderr` 合計 `0` B | `0` B（`94` 呼叫 ＋ `V-4` 之 `diff`／`cmp` 四呼叫） | `0` B |

`V-3` 之出艙（次趟·`git hash-object` 與 bytes）：

```
tests/test_pool_slot.py 576ad6ded57db688f8d1f4fa7901050785ee0591 6187
verify/probes/probe_WG9363_k953.py dc7c4cac35c0165e93f5b2b3fb101ca913cc34a6 130814
verify/probes/probe_WG9367_adj4.py 6fb7c2fd183815100b40e7a131140d122aa62eef 76318
verify/probes/probe_WG9370_adj4mut.py 059732c791293ec034e44c1fdc1a58ff41a262b9 22388
verify/probes/probe_WG9373_k966.py 6a453659b4868d56504c36f9510308ea9380ada3 77853
verify/probes/probe_WG9375_k965.py 1b9d4c4c0321d9ff5afc36fc70e0a6c25bed4c37 109549
verify/probes/probe_WG9385_k974.py cb70ecbf383ae3e713edce224c793ad8d9f16143 45479
verify/probes/probe_WG9387_k961h.py c3fabfd3ac3193e20966aca1176ec2f29a63de24 25698
verify/probes/probe_WG9388_k961s3.py 649c7693bcbe252ff9c87269e21c7c68746e8150 43772
verify/probes/probe_WG9389_trialstop.py f3ca8fba45880e88e9a8280311ba7153b040b658 37799
verify/probes/probe_WG9390_k961r.py 613a31d94b4f1313e87f86fd37df721791e75201 31399
verify/probes/probe_WG9391_k980x.py a3e7f8eb6dc6c0200b06102e937d3b04cf414266 34074
verify/probes/probe_WG9392_k980g.py 73dccdcd0eeb84a0d02c336b26ab266ed7e57a39 33749
verify/probes/probe_WG9393_endall.py 845057258ba9f1d789f401d170f0efbfcc8818de 29867
verify/probes/probe_WG9394_k9615.py 400fe847681a9ef67400597302da3f246268c4c1 35530
verify/probes/probe_WG9395_k960.py a4a7600af16ca6ddcc27967199a28ddc492dd85b 45745
verify/probes/probe_WG9398_rw25.py dd5a6038d1e8408493c92b72702cc5ac5825c90d 21248
```

`V-7`／`V-8` 之出艙（次趟）：

```
## V-7
$ git diff --name-status 07d1202 c35d32a3cd43da5bdcb1c197d16b5757a1b39861 -- app.py verify/
M	app.py
$ git diff --numstat 07d1202 c35d32a3cd43da5bdcb1c197d16b5757a1b39861 -- app.py
51	12	app.py
$ git diff --name-only 07d1202 c35d32a3cd43da5bdcb1c197d16b5757a1b39861 -- verify/ | wc -l
0
$ git rev-parse c35d32a3cd43da5bdcb1c197d16b5757a1b39861:app.py
87e784a3865242519e770d376b65ebe7e89493ec
AST（對 20e03bf）頂層之名之增 ['RW_TABLE_25'] 減 [] 相異之節點 ['RW_TABLE_25', 'rw_from_width']
## V-8
$ git grep -c -F "RW_TABLE_25" -- app.py
app.py:6
rc=0
$ git grep -c -F "附表 25" -- app.py
app.py:5
rc=0
```

### ③-4　`V-4` 之全文（次趟·與首趟逐位同·`cmp` 驗）

`python3 verify/probes/probe_WG9392_k980g.py diff <O>/pre/k6s3_pre_35.json <O>/post/k6s3_post_35.json` ⇒ `rc 0`·`stderr` `0` B：

```
  宗 R1·628(5)·right G(㎡) 376.12 → 376.11
  宗 R1·628-37(1)·right G(㎡) 285.21 → 285.22
  宗 R2·628-39(1)·left G(㎡) 289.43 → 289.42
  宗 R2·628-40(1)·left G(㎡) 359.59 → 359.6
  宗 R2·628-41(1)·left G(㎡) 313.51 → 313.5
  宗 R5·628-45(1)·left G(㎡) 525.28 → 525.27
  宗 R6·628-7(1)·right G(㎡) 1007.91 → 1007.92
全比相異 7 項
```

同 `00` ⇒ `rc 0`·`stderr` `0` B：

```
  宗 R1·628(5)·right G(㎡) 376.12 → 376.11
  宗 R1·628-35(2)·left G(㎡) 730.81 → 730.82
  宗 R1·628-36(1)·right G(㎡) 662.1 → 662.11
  宗 R1·628-37(1)·left G(㎡) 272.83 → 272.82
  宗 R2·628-39(1)·left G(㎡) 289.43 → 289.42
  宗 R2·628-40(1)·left G(㎡) 359.59 → 359.6
  宗 R2·628-41(1)·left G(㎡) 313.51 → 313.5
  宗 R3·628-30(3)·right G(㎡) 562.01 → 562.02
  宗 R3·628-45(2)·right G(㎡) 343.46 → 343.45
  宗 R5·628-20(2)·left G(㎡) 534.47 → 534.48
  宗 R6·628-7(1)·right G(㎡) 1007.91 → 1007.92
  抵費地 R3-抵費地 面積 1651.4 → 1651.39
全比相異 12 項
```

程式比（單 `§一` 項 `5` 之列抽出之項 ＋ 末列 `全比相異 N 項` 對出艙之列）：3.5 m `7` 項 ⇒ `True`；0 m `12` 項 ⇒ `True`。

`python3 verify/probes/probe_WG9344_k6s3.py cmp <O>/pre/k6s3_pre_35.json <O>/post/k6s3_post_35.json` ⇒ `rc 1`·`stderr` `0` B：

```
   宗 ('R1', '628-37(1)') G(㎡) 285.21 ≠ 285.22
   宗 ('R2', '628-40(1)') G(㎡) 359.59 ≠ 359.6
相異 2 項 ⇒ 🔴 異
```

同 `00` ⇒ `rc 1`·`stderr` `0` B：

```
   宗 ('R1', '628-35(2)') G(㎡) 730.81 ≠ 730.82
   宗 ('R2', '628-40(1)') G(㎡) 359.59 ≠ 359.6
相異 2 項 ⇒ 🔴 異
```

（＝ `§一` 項 `5` 之所載：3.5 m `628-37(1)`、`628-40(1)`；0 m `628-35(2)`、`628-40(1)`；末列逐字 `相異 2 項 ⇒ 🔴 異`。）

### ③-5　`V-5`／`V-6` 之比與其出艙（次趟）

比之式：`python3 <O>/../tools/jdiff.py <前> <後> [<前之 HEAD> <後之 HEAD>]`——讀二檔（給 HEAD 者先以同一字樣 `<HEAD>` 代其全值）、遞迴比其鍵與值（`dict` 逐鍵、`list` 逐位與長、葉 `!=`），出艙每差一列與末列「相異 N 欄」。`V-5` 之 `stdout` 之比：首列各載其態之 `HEAD`（`07d1202…`／`c35d32a…`），以 `cmp <(tail -n +2 前) <(tail -n +2 後)` 驗首列以外逐位同。

```
$ git hash-object <O>/pre/f8_pre_35.json <O>/post/f8_post_35.json
47683d1cb284ad814034d7ac7f3cd464d66c6e3f
13c04b456f98a3ea39c553e2ca6bd257a351e3b1
$ git hash-object <O>/pre/f8_pre_00.json <O>/post/f8_post_00.json
884e91714a79288406faa4def6518847de36de39
f27849f58c08e7d60b6474b6b353e24dd6d7cd83
### JSON 逐欄比 f8 35（jdiff.py）
/dropped/R2/left[1]/G(㎡): 27.55 → 27.54
/rows[2]/G(㎡): 376.12 → 376.11
/rows[3]/G(㎡): 285.21 → 285.22
/rows[13]/G(㎡): 1007.91 → 1007.92
/rows[15]/G(㎡): 525.28 → 525.27
/rows[22]/G(㎡): 313.51 → 313.5
/rows[23]/G(㎡): 359.59 → 359.6
/rows[24]/G(㎡): 289.43 → 289.42
相異 8 欄
### JSON 逐欄比 f8 00（jdiff.py）
/dropped/R2/left[1]/G(㎡): 27.55 → 27.54
/dropped/R3/right[1]/G(㎡): 24.88 → 24.89
/rows[0]/G(㎡): 272.83 → 272.82
/rows[1]/G(㎡): 730.81 → 730.82
/rows[2]/G(㎡): 376.12 → 376.11
/rows[3]/G(㎡): 662.1 → 662.11
/rows[13]/G(㎡): 1007.91 → 1007.92
/rows[16]/G(㎡): 534.47 → 534.48
/rows[22]/G(㎡): 313.51 → 313.5
/rows[23]/G(㎡): 359.59 → 359.6
/rows[24]/G(㎡): 289.43 → 289.42
/rows[32]/G(㎡): 343.46 → 343.45
/rows[33]/G(㎡): 562.01 → 562.02
相異 13 欄
### parity 00：代 HEAD 後
相異 0 欄
### parity 00：對照（⛔ 代）
/head: "07d12028d99b3a178c2a87edaea0b70ae8a754ac" → "c35d32a3cd43da5bdcb1c197d16b5757a1b39861"
相異 1 欄
### parity 35：代 HEAD 後
/stage3_log[2]/試算G: 313.51 → 313.5
/stage3_log[4]/試算G: 346.18 → 346.17
相異 2 欄
### parity 35：對照（⛔ 代）
/head: "07d12028d99b3a178c2a87edaea0b70ae8a754ac" → "c35d32a3cd43da5bdcb1c197d16b5757a1b39861"
/stage3_log[2]/試算G: 313.51 → 313.5
/stage3_log[4]/試算G: 346.18 → 346.17
相異 3 欄
### parity stdout #60：首列
【F4 parity】態 07d12028d99b3a178c2a87edaea0b70ae8a754ac·退縮 3.5·WV_K6B_STAGE3=on·擾動 False
【F4 parity】態 c35d32a3cd43da5bdcb1c197d16b5757a1b39861·退縮 3.5·WV_K6B_STAGE3=on·擾動 False
首列以外逐位同
### parity stdout #61：首列
【F4 parity】態 07d12028d99b3a178c2a87edaea0b70ae8a754ac·退縮 0.0·WV_K6B_STAGE3=on·擾動 False
【F4 parity】態 c35d32a3cd43da5bdcb1c197d16b5757a1b39861·退縮 0.0·WV_K6B_STAGE3=on·擾動 False
首列以外逐位同
```

⇒ `V-6`：施後之 hash ＝ 3.5 m `13c04b456f98a3ea39c553e2ca6bd257a351e3b1`、0 m `f27849f58c08e7d60b6474b6b353e24dd6d7cd83`（＝ 期）；逐欄之差 3.5 m `8` 欄、0 m `13` 欄（＝ 期·逐欄同）。`V-5`：`parity` 二退縮 `rc 0`·末列 `⇒ rc 0（不符 0 項）`；`stdout` 唯首列之 `HEAD` 異；0 m 之落檔代 `HEAD` 後相異 `0` 欄；3.5 m 之落檔代 `HEAD` 後唯 `/stage3_log[2]/試算G` `313.51 → 313.5`、`/stage3_log[4]/試算G` `346.18 → 346.17`（＝ 期）；對照（⛔ 代）則另 `/head` 異。

### ③-6　`94` 呼叫之表（前置與驗·`rc`／`stderr` B／耗時 s／末列）

前置之 (甲)(乙) 為實跑（`07d1202`）；(丙) 為**沿用**（基準之值·⛔ 重跑）。驗之首趟（`a18efd9`）已為次趟（`c35d32a`·**為準**）所代；二趟皆從頭整套照跑。並行 `2`。無逾時、無重跑之呼叫（單首 🔑 之「重跑一次」⛔ 觸發）。

| # | 命令（`<repo>` ＝ `/tmp/w`） | 前置（工項一之端 `07d1202`）rc／stderr B／耗時 s／末列 | 驗·首趟（`a18efd9`·已為次趟所代） | 驗·次趟（`c35d32a`·**為準**） |
|---|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0`／`0`／2.1／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／2.0／`⇒ 紅 []；rc 0` | `0`／`0`／2.0／`⇒ 紅 []；rc 0` |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0`／`0`／109.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／100.4／`⇒ 紅 []；rc 0` | `0`／`0`／105.1／`⇒ 紅 []；rc 0` |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0`／`0`／359.8／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／331.5／`⇒ 紅 []；rc 0` | `0`／`0`／361.8／`⇒ 紅 []；rc 0` |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.8／`⇒ 紅 []；rc 0` | `0`／`0`／1.8／`⇒ 紅 []；rc 0` |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0`／`0`／34.1／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／34.0／`⇒ 紅 []；rc 0` | `0`／`0`／33.6／`⇒ 紅 []；rc 0` |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0`／`0`／35.4／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／34.2／`⇒ 紅 []；rc 0` | `0`／`0`／33.7／`⇒ 紅 []；rc 0` |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0`／`0`／3.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／2.6／`⇒ 紅 []；rc 0` | `0`／`0`／2.7／`⇒ 紅 []；rc 0` |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.8／`⇒ 紅 []；rc 0` | `0`／`0`／1.7／`⇒ 紅 []；rc 0` |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.6／`⇒ 紅 []；rc 0` |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／31.6／`⇒ 紅 []；rc 0` | `0`／`0`／32.6／`⇒ 紅 []；rc 0` |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／12.4／`⇒ 紅 []；rc 0` | `0`／`0`／11.6／`⇒ 紅 []；rc 0` |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／202.4／`⇒ 紅 []；rc 0` | `0`／`0`／219.4／`⇒ 紅 []；rc 0` |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0`／`0`／1.7／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.7／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.6／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0`／`0`／2.1／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.9／`⇒ 紅 []；rc 0` | `0`／`0`／2.0／`⇒ 紅 []；rc 0` |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `1`／`0`／62.0／`⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1`（(甲)） | `0`／`0`／58.2／`⇒ 紅 []；rc 0` | `0`／`0`／61.2／`⇒ 紅 []；rc 0` |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `1`／`0`／389.6／`⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1`（(甲)） | `0`／`0`／348.4／`⇒ 紅 []；rc 0` | `0`／`0`／372.0／`⇒ 紅 []；rc 0` |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `1`／`0`／537.8／`⇒ 紅 ['R3@0.0']；rc 1`（(甲)） | `0`／`0`／501.4／`⇒ 紅 []；rc 0` | `0`／`0`／529.9／`⇒ 紅 []；rc 0` |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0`／`0`／8.0／`⇒ 突變 8（另基準一）；紅 []；rc 0`（(甲)） | `0`／`0`／7.9／`⇒ 突變 8（另基準一）；紅 []；rc 0` | `0`／`0`／7.3／`⇒ 突變 8（另基準一）；紅 []；rc 0` |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0`／`0`／2.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／2.3／`⇒ 紅 []；rc 0` | `0`／`0`／2.3／`⇒ 紅 []；rc 0` |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0`／`0`／62.5／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0`（(甲)） | `0`／`0`／57.8／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` | `0`／`0`／61.0／`⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `1`／`0`／321.2／`⇒ 紅 ['R2@0.0']；rc 1`（(甲)） | `0`／`0`／294.5／`⇒ 紅 []；rc 0` | `0`／`0`／313.6／`⇒ 紅 []；rc 0` |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.6／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1413.6／`⇒ 紅 []；rc 0` | `0`／`0`／1432.4／`⇒ 紅 []；rc 0` |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／27.3／`⇒ 紅 []；rc 0` | `0`／`0`／26.7／`⇒ 紅 []；rc 0` |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.4／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／5.3／`⇒ 紅 []；rc 0` | `0`／`0`／4.6／`⇒ 紅 []；rc 0` |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0`／`0`／—／`⇒ rc 0（不符 0·器紅 0）`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／22.9／`⇒ rc 0（不符 0·器紅 0）` | `0`／`0`／22.8／`⇒ rc 0（不符 0·器紅 0）` |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.7／`⇒ 紅 []；rc 0` | `0`／`0`／1.7／`⇒ 紅 []；rc 0` |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／18.6／`⇒ 紅 []；rc 0` | `0`／`0`／18.3／`⇒ 紅 []；rc 0` |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／212.6／`⇒ 紅 []；rc 0` | `0`／`0`／224.6／`⇒ 紅 []；rc 0` |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／264.7／`⇒ 紅 []；rc 0` | `0`／`0`／298.7／`⇒ 紅 []；rc 0` |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／29.3／`⇒ 紅 []；rc 0` | `0`／`0`／30.5／`⇒ 紅 []；rc 0` |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／34.1／`⇒ 紅 []；rc 0` | `0`／`0`／32.4／`⇒ 紅 []；rc 0` |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／6.7／`⇒ 紅 []；rc 0` | `0`／`0`／5.9／`⇒ 紅 []；rc 0` |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／22.0／`⇒ 紅 []；rc 0` | `0`／`0`／21.0／`⇒ 紅 []；rc 0` |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／14.0／`⇒ 紅 []；rc 0` | `0`／`0`／13.6／`⇒ 紅 []；rc 0` |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／9.7／`⇒ 紅 []；rc 0` | `0`／`0`／9.7／`⇒ 紅 []；rc 0` |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／145.7／`⇒ 紅 []；rc 0` | `0`／`0`／152.3／`⇒ 紅 []；rc 0` |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.6／`⇒ 紅 []；rc 0` | `0`／`0`／1.4／`⇒ 紅 []；rc 0` |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／42.4／`⇒ 紅 []；rc 0` | `0`／`0`／43.2／`⇒ 紅 []；rc 0` |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／708.9／`⇒ 紅 []；rc 0` | `0`／`0`／719.5／`⇒ 紅 []；rc 0` |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.6／`⇒ 紅 []；rc 0` | `0`／`0`／1.4／`⇒ 紅 []；rc 0` |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.1／`⇒ 紅 []；rc 0` | `0`／`0`／1.1／`⇒ 紅 []；rc 0` |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／120.3／`⇒ 紅 []；rc 0` | `0`／`0`／123.2／`⇒ 紅 []；rc 0` |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／97.3／`⇒ 紅 []；rc 0` | `0`／`0`／102.2／`⇒ 紅 []；rc 0` |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.4／`⇒ 紅 []；rc 0` |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／260.3／`⇒ 紅 []；rc 0` | `0`／`0`／270.9／`⇒ 紅 []；rc 0` |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0`／`0`／—／`selftest 9/9 ⇒ ✅`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／0.0／`selftest 9/9 ⇒ ✅` | `0`／`0`／0.0／`selftest 9/9 ⇒ ✅` |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0`／`0`／—／`selftest 13/13 ⇒ ✅`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／0.0／`selftest 13/13 ⇒ ✅` | `0`／`0`／0.0／`selftest 13/13 ⇒ ✅` |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／2.1／`⇒ 紅 []；rc 0` | `0`／`0`／2.4／`⇒ 紅 []；rc 0` |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0`／`0`／—／`ε ＝ 0.0002｜rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.6／`ε ＝ 0.0002｜rc 0` | `0`／`0`／1.6／`ε ＝ 0.0002｜rc 0` |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0`／`0`／—／`紅項 [] 器紅 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／8.8／`紅項 [] 器紅 0` | `0`／`0`／9.1／`紅項 [] 器紅 0` |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／257.1／`⇒ 紅 []；rc 0` | `0`／`0`／271.8／`⇒ 紅 []；rc 0` |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0`／`0`／175.4／`（JSON 之摘要列·略）`（(乙)） | `0`／`0`／152.1／`（JSON 之摘要列·略）` | `0`／`0`／163.8／`（JSON 之摘要列·略）` |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0`／`0`／120.6／`（JSON 之摘要列·略）`（(乙)） | `0`／`0`／109.9／`（JSON 之摘要列·略）` | `0`／`0`／108.3／`（JSON 之摘要列·略）` |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0`／`0`／172.4／`⇒ 紅 []；rc 0`（(乙)） | `0`／`0`／152.0／`⇒ 紅 []；rc 0` | `0`／`0`／165.0／`⇒ 紅 []；rc 0` |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0`／`0`／117.2／`⇒ 紅 []；rc 0`（(乙)） | `0`／`0`／112.2／`⇒ 紅 []；rc 0` | `0`／`0`／116.2／`⇒ 紅 []；rc 0` |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0`／`0`／355.5／`⇒ rc 0（不符 0 項）`（(乙)） | `0`／`0`／326.8／`⇒ rc 0（不符 0 項）` | `0`／`0`／340.7／`⇒ rc 0（不符 0 項）` |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0`／`0`／248.3／`⇒ rc 0（不符 0 項）`（(乙)） | `0`／`0`／234.1／`⇒ rc 0（不符 0 項）` | `0`／`0`／250.3／`⇒ rc 0（不符 0 項）` |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0`／`0`／3.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／3.1／`⇒ 紅 []；rc 0` | `0`／`0`／3.7／`⇒ 紅 []；rc 0` |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0`／`0`／3.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／3.2／`⇒ 紅 []；rc 0` | `0`／`0`／2.9／`⇒ 紅 []；rc 0` |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0`／`0`／281.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／258.9／`⇒ 紅 []；rc 0` | `0`／`0`／291.1／`⇒ 紅 []；rc 0` |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.4／`⇒ 紅 []；rc 0` |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0`／`0`／2.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／2.7／`⇒ 紅 []；rc 0` | `0`／`0`／2.2／`⇒ 紅 []；rc 0` |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／973.0／`⇒ 紅 []；rc 0` | `0`／`0`／990.7／`⇒ 紅 []；rc 0` |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／959.3／`⇒ 紅 []；rc 0` | `0`／`0`／939.0／`⇒ 紅 []；rc 0` |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0`／`0`／1.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.8／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0`／`0`／119.4／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／107.4／`⇒ 紅 []；rc 0` | `0`／`0`／109.1／`⇒ 紅 []；rc 0` |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0`／`0`／369.7／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／339.9／`⇒ 紅 []；rc 0` | `0`／`0`／358.5／`⇒ 紅 []；rc 0` |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0`／`0`／1.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.2／`⇒ 紅 []；rc 0` |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0`／`0`／2.1／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.8／`⇒ 紅 []；rc 0` | `0`／`0`／1.9／`⇒ 紅 []；rc 0` |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0`／`0`／282.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／257.3／`⇒ 紅 []；rc 0` | `0`／`0`／286.6／`⇒ 紅 []；rc 0` |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0`／`0`／1.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.6／`⇒ 紅 []；rc 0` | `0`／`0`／1.6／`⇒ 紅 []；rc 0` |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0`／`0`／34.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／34.6／`⇒ 紅 []；rc 0` | `0`／`0`／35.6／`⇒ 紅 []；rc 0` |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0`／`0`／561.2／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／521.0／`⇒ 紅 []；rc 0` | `0`／`0`／562.9／`⇒ 紅 []；rc 0` |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `0`／`0`／5.3／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／5.8／`⇒ 紅 []；rc 0` | `0`／`0`／5.8／`⇒ 紅 []；rc 0` |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `0`／`0`／4.4／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／4.6／`⇒ 紅 []；rc 0` | `0`／`0`／4.1／`⇒ 紅 []；rc 0` |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `1`／`0`／279.7／`⇒ 紅 ['R2@0.0']；rc 1`（(甲)） | `0`／`0`／262.2／`⇒ 紅 []；rc 0` | `0`／`0`／281.2／`⇒ 紅 []；rc 0` |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | `0`／`0`／1.4／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `0`／`0`／4.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／4.2／`⇒ 紅 []；rc 0` | `0`／`0`／3.6／`⇒ 紅 []；rc 0` |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | `0`／`0`／285.6／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／263.9／`⇒ 紅 []；rc 0` | `0`／`0`／290.2／`⇒ 紅 []；rc 0` |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | `0`／`0`／—／`⇒ 紅 []；rc 0`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／251.5／`⇒ 紅 []；rc 0` | `0`／`0`／284.0／`⇒ 紅 []；rc 0` |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | `0`／`0`／1.5／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.6／`⇒ 紅 []；rc 0` | `0`／`0`／1.6／`⇒ 紅 []；rc 0` |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | `0`／`0`／4.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／4.3／`⇒ 紅 []；rc 0` | `0`／`0`／3.8／`⇒ 紅 []；rc 0` |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | `0`／`0`／287.0／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／255.7／`⇒ 紅 []；rc 0` | `0`／`0`／278.6／`⇒ 紅 []；rc 0` |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | `0`／`0`／1.6／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／1.5／`⇒ 紅 []；rc 0` | `0`／`0`／1.6／`⇒ 紅 []；rc 0` |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | `0`／`0`／7.9／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／7.9／`⇒ 紅 []；rc 0` | `0`／`0`／7.0／`⇒ 紅 []；rc 0` |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | `0`／`0`／273.7／`⇒ 紅 []；rc 0`（(甲)） | `0`／`0`／263.1／`⇒ 紅 []；rc 0` | `0`／`0`／285.7／`⇒ 紅 []；rc 0` |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | `0`／`0`／—／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅`（(丙)·**沿用**基準 `20e03bf`·⛔ 重跑） | `0`／`0`／1.6／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅` | `0`／`0`／1.5／`判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅` |
| `92` | `python3 verify/probes/probe_WG9398_rw25.py selftest <repo>` | `1`／`0`／1.6／`⇒ 紅 ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T8', 'T9']；rc 1`（(甲)） | `0`／`0`／1.8／`⇒ 紅 []；rc 0` | `0`／`0`／1.5／`⇒ 紅 []；rc 0` |
| `93` | `python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf` | `1`／`0`／2.6／`⇒ 紅 ['X1', 'X2', 'X3', 'X5']；rc 1`（(甲)） | `0`／`0`／2.6／`⇒ 紅 []；rc 0` | `0`／`0`／2.5／`⇒ 紅 []；rc 0` |
| `94` | `python3 tests/test_pool_slot.py` | `1`／`516`／0.7／`（空·stderr 末列：AssertionError: app.py 缺 module 級常數 ['RW_TABLE_25']——被改名或刪除？）`（(甲)） | `0`／`0`／0.6／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）` | `0`／`0`／0.5／`✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）` |


---

## ④ 塊之實得與二檔之改前改後

| 塊 | 實得（圍欄內全文·末附換行） | 期（`§五-1`） |
|---|---|---|
| `Fy55` | `49064` B·`sha256` `e1c4ceaac02bbdd7fdb970512c7ebe7694685da99c96ee47991dda2523269c1e`·`777` 列 | 同 |
| `K46` | `14847` B·`c33c8fb69656f13d77a5d93eb7edba9f7d7bcee092f1ae1c252d41a195979d6b`·`86` 列 | 同 |
| `P57` | `2486` B·`586b2130a0fdc702b058e1eab9cab1dee1c2a9855431e91361501d72d1ba1bf9`·`15` 列 | 同 |
| `CK`（`W-G.9-365_輕量單.md` 附錄午） | `1539` B·`00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d`·`31` 列 | 同 |
| `GF`（同·附錄巳） | `2445` B·`b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc`·`47` 列 | 同 |

塊 `Fy55` 所施之 `17` 檔之施前 blob 皆 ＝ `§五-1` 項 `2`（`probe_WG9398_rw25.py` 施前⛔ 存）；施後皆 ＝ 項 `5`（見 ③-3 之 `V-3` 之出艙）；`git status --porcelain` 唯此 `17` 檔（`16` `M`·`1` `??`）；工項一之 `numstat` ＝ 閘 `1` 之期之列（見回報）。

| 檔 | 改前 | 改後 | 嚴格前綴／尾 ＝ 塊 |
|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `9872c2b1351a783c8be3ff2779ebffc2859f3430`（`994700` B） | `967fc8843805ac57b0ea1a01e20a9c5b7339b8aa`（`1009547` B） | `True`／`True` |
| `docs/待落地清單.md` | `1edf59f42a5c9b5aebdeeeda6249ddbe0dfdd875`（`43777` B） | `7809da2bac7e35854540df798075e094922d2eba`（`46263` B） | `True`／`True` |

工項三之 `numstat`：`86`／`0`、`15`／`0`（唯此二檔）。

---

## ⑤ 推送之目標與推後之遠端分支之列

濾後之母體之式 ＝ `git ls-remote --heads origin | grep -v -E "refs/heads/(wip/plots|verify/W-P\.)"`。開工時 `55` 列（`<O>/heads_before_398.txt`）；工項零推後 `56` 列（`verify/W-G.9-398-rw25` ＝ `96c06e9…`、主線 ＝ `20e03bf…`）。一切推送之目標：新側支 `verify/W-G.9-398-rw25`（工項零〜四·皆快轉）與 `ops/queue`（`STATE.json`／`log.md`／`reports/`·接單、進度列、回報）。收工閘 `5` 之實測（`56` 列·逐列比）見回報。

---

## ⑥ 自捕與自解；唯讀獨立審查之發現與處置

### ⑥-1　執行端之自捕與自解

1. **`F23`／`F24` 之字樣之錨之撞**（撰碼中·`dev` 之拷貝）：首稿之 docstring 之 `④ 1m ≤ W < 18m` 含子字串 `'m ≤ '`（基準之 `app.py` 恰一見之錨）⇒ `F23 wiring`（`W8`）、`F24 wiring`（`W7`）紅（`錨之異 [('m ≤ ', 2)]`）⇒ 改書 `④ 1 ≤ W < 18（公尺）` ⇒ 二者綠。施於倉前即已解（倉內之一切 `commit` 無此字）。
2. **撰碼中之快掃**（retro 之法·⛔ 為驗）：生產碼定稿前於倉外之拷貝（`07d1202` ＋ 新 `app.py`）跑 `selftest`／`wiring` 之 `57` 呼叫（含耗時 ＞ `100` s 之 `#2`、`#12`、`#32`、`#70`）⇒ 皆合施後之期。
3. **⚠️ 單首 🔑 通則「Bash 命令⛔ 含 heredoc」之違**（自捕）：執行端於倉外之暫存目錄寫自用之輔助之腳本（逐呼叫之跑器 `runner.py`、比之器 `compare.py`／`jdiff.py`、塊之抽取 `extract.py` 等）與數處臨時之 `python3 -`，以 Bash 之 heredoc 為之。其皆⛔ 入倉、⛔ 為量測器、⛔ 改倉內任何檔（倉內之檔之寫入一律為 `cp`／`cat >>`／`git apply` 之二進位操作，三塊之抽取亦以檔案管線依圍欄之逐列索引為之、其 bytes／`sha256` 皆 ＝ `§五-1`）。發覺後（工項四之撰）改以檔案工具寫檔。對倉之產物無影響；照實記之。
4. **`#94` 前置之 `stderr` 之 bytes**：`516` B（發單端 `522` B）——單已載「其 bytes 依路徑之長而異」；其末列含「RW_TABLE_25」⇒ 合期。

### ⑥-2　唯讀獨立審查（一 reviewer·⛔ 改檔、⛔ `commit`·其一切實跑在其自建之拷貝·`/tmp/w` 全程 `git status --porcelain` 空）

**受審**：首審 ＝ `a18efd9`（`git diff 07d1202 a18efd9 -- app.py`）；增審 ＝ `a18efd9 → c35d32a`。

| # | 發現 | 分類 | 處置 |
|---|---|---|---|
| `C-1` | `R-1`〜`R-3`、`§三-3` 第 `1`〜`6` 款皆守（自窮舉量測器之字串常數 `26948` 個：基準恰一而施後不恰一者唯 `'2.68'`、`'99.75'`〔單明除〕；函式名之唯一性無破；`F23`／`F24`／`F41` 實跑綠；突變之器 `#19`、`#22`、`#43`、`#47` 綠） | C | — |
| `C-2` | `RW_TABLE_25` 之 `170` 格對手冊原文（第 `4053`、`4062`〜`4077` 列·以 `ast.get_source_segment` 取每格之原字面·字串對字串）⇒ 不符 `0`；第 `4078` 列 `18 100.00` ⇒ `18 m` ＝ `100`；嚴格遞增（相鄰差 `0.25`〜`0.72`）；整數公尺之 `17` 格以 `ROUND_HALF_UP` 取一位 ＝ 簡表（第 `3031`〜`3034` 列） | C | — |
| `C-3` | 行為：格點 `i ＝ 10`〜`180` 以四法生之 `W` 皆 ＝ 格值；`0.1*53`、`2.7+2.6` ⇒ `45.85`；`5.3 ± 1e-12`／`± 1e-10` ⇒ 吸附；`± 1e-8` ⇒ 內插（＝ `Fraction` 之精確模型）；`17.9`〜`18`、`0`〜`1 m`、`≤ 0`、`None`、`''`、`±inf` 皆合；隨機 `20` 萬點與格點之鄰 ⇒ 不減違例 `0`、對精確模型之差 ≤ `7.2e-11`；`rw_increment` 之鏈 `2` 萬條 ⇒ `|Σ − 100|` ≤ `2.8e-14`；NaN ⇒ `ValueError`（改前同） | C | — |
| `A-1` | `_rw25_cell_398(k)` 於 `k ＜ 10` 以負索引**靜默**取第 `17` 列（如 `k ＝ 9` ⇒ `99.75`）；現行之路（`W ≥ 1` ⇒ `k ≥ 10`）不可達 | **A** | **修之**：其首增「`10 ≤ k ≤ 10 × (len(RW_TABLE_25) + 1)` 以外 ⇒ `raise ValueError`」；docstring ① 補「NaN 則拋 ValueError（與改前同）」⇒ `c35d32a`；增審：`k ＝ −1, 0, 9, 181, 190, 1e6` 皆拋、`10`／`179`／`180` ⇒ `17.36`／`99.75`／`100.0`；現行之路之 `302964` 點與 `a18efd9` 逐位同（`==` 與 `repr`）；`X3`／`F23`／`F24`／`F41` 綠 ⇒ `V-1`〜`V-9` 從頭重跑（次趟）皆合 |
| `C-4` | `Rw` 之他之產生處（生產碼 `34` 檔）窮查：無（`rw_from_width` 之消費者 ＝ `rw_increment`、`_select_pool_slot` 之 `R`、`main` 之檢核、`verify/stepg_pipeline.py` 之 `ns["rw_from_width"]`；`rw_increment` 之消費者 ＝ `iterate_G_S`、`solve_G_binary`；表之數之 `grep` 唯命中 `app.py:194`〔物價指數 `99.75`·無關〕與 `main` 內之畫面之字） | C | — |
| `C-5` | 合成之例（⛔ 用 `F41` 之玩具）：二表之差之最大之格（`±0.05` 個百分點·每格之增量差最大於 `15.0`〜`15.1 m`）；一側之鏈三宗 `0→9.0→15.8→24` ⇒ 舊 `66.30／27.48／6.22`、新 `66.25／27.58／6.17`（和皆 `100`）；右側之街角 `0→3.0→5.4→20` ⇒ 舊 `31.30／15.10／53.60`、新 `31.25／15.20／53.55`；強制抵費地之起點 `1.8` ⇒ 和 `77.00` → `76.95`（＝ `100 − R(1.8)`）；`solve_G_binary`（矩形之玩具）之 `ΔG` ≤ `0.04 ㎡`、`ΣG` 不變；本案之二退縮之實跑之逐葉比 ＝ `§一` 項 `5`；各宗之 `W` 前後同、配地之宗之最小 `W` `7.12 m`（3.5 m）／`6.07 m`（0 m）；各街廓之 `ΣG ＋ Σ池` 前後之差 ≤ `0.01 ㎡`（二位各自捨入之殘·單已預告） | C | — |
| `B-1` | reviewer 之章程（`.claude/agents/` 之 reviewer 之定義）載「法定 Rw 表（`W=4=37.8` 等）為常數，不可改」；改後 `rw_from_width(4.0)` ＝ `37.78`。佐證新表之合：`CLAUDE.md` 之驗收錨「Rw 累積：47.64+23.47+23.33+5.56 = 100.00%」於新表下逐位成立（舊表得 `47.6`／`23.5`／`23.3`／`5.6`）。 | B（規則文之修訂） | **⛔ 停機**：本單之行為已有 KL `2026-10-26 09:53`「是」之裁（`K-9-41` ⑥ 之細化）；此為規則文（`.claude/`·本單⛔ 及）之舊述之更新，屬帳本之登錄（README 第二節自動處理第 `3` 款·發單端）⛔ 為本單之域判之未定 ⇒ **呈發單端**登錄、改章程之述 |
| `B-2` | 強制抵費地之側之配地之宗之合計 ＝ `100 − R(W0)`，換表後 `R(W0)` 微變（如 `R(1.8)` `23.0 → 23.05`）⇒ 側街負擔於「配地之宗」與「抵費地／池」之分界微移（本案 0 m `R3-抵費地` `−0.01 ㎡`）；監看窗之請示之【對土地的影響】「抵費地、總負擔不變」與實測不全合 | B（告知） | **⛔ 停機**：單 `§一` 項 `5` 與塊 `K46` 之三已載此（`R3-抵費地` `1651.40 → 1651.39`·「應分配面積與抵費地各自取至 2 位」）⇒ 預期之內；**請發單端於呈 KL 核時明告「抵費地亦微變」** |
| `C-6` | `main` 內之畫面之字（`app.py` 之 `main` 內「104 版作業手冊 P.103 累積表（W=1→17.4…）線性內插」）仍載簡表 | C | 單明令⛔ 動（待落地序 `41`） |
| `C-7` | `app.py` 之 `solve_G_binary` 附近之歷史注釋「`W₀ = 6.98 而其 Rw = 55.59 ≈ R(6.98)`」為改前之實測值（新表 `55.58`） | C | 屬他之頂層節點（⛔ 動·`§三-3` 第 `4` 款）；記之 |
| `C-8` | 增審（`a18efd9 → c35d32a`）：`§三-1`〜`§三-3` 守（新之數之常數 `10`、`1`、`10`·非表值；新字串 `'附表 25 之格點越界：k='` ⛔ 撞錨）；現行之路逐位同；域外 loud | C | — |

---

## ⑦ 設計說明（`§三-5`）

**`R-1`**：`app.py` 之頂層、`RW_SATURATION_WIDTH_M = 18.0` 之後、`def rw_from_width` 之前，增常數 `RW_TABLE_25`（`tuple` 之 `tuple`·`17` 列 × `10` 欄·每格二位小數之字面〔`18.80`、`50.00`、`80.00` 等保留二位〕·各列尾注 `# 1 m`〜`# 17 m`）；其上之注釋載其身分（手冊附表 25「街角地側面道路負擔百分率累積表」·頁 `119`·表末註「本表係由前面負擔百分率簡表推演而來」·附件二之簡表之細化）、列欄之義、`18 m` 以上 ＝ `100`（不入表）、⛔ 以式生之／⛔ 自檔讀之之由、所據（`W-G.9-398`·KL `2026-10-26 09:53`「是」·`K-9-41` ⑥ 之細化）。

**`R-2`**：`rw_from_width` 之簽名 `(W: float) -> float`、單位（百分比）照舊。其行為：① `W = float(W or 0.0)`；`W <= 0` ⇒ `0.0`（照舊之二句）；② `W >= RW_SATURATION_WIDTH_M` ⇒ `100.0`（照舊）；③ `W < 1.0` ⇒ `RW_TABLE_25[0][0] * W`；④ 巢狀函式 `_rw25_cell_398(k)`（格點 `k`〔`W ＝ k／10`〕之格值：`k` 須 `10 ≤ k ≤ 180`〔以 `10 × (len(RW_TABLE_25) + 1)` 書之〕，否則 `raise ValueError`；`k // 10 > len(RW_TABLE_25)`〔唯 `k ＝ 180`〕⇒ `100.0`；否則 `RW_TABLE_25[k // 10 - 1][k % 10]`）；`x10 = W * 10.0`、`k_near = round(x10)`；`abs(x10 - k_near) <= 1e-9` ⇒ 格點 ⇒ `_rw25_cell_398(k_near)`；否則 `k_lo = int(x10)`（`x10 ≥ 10 ＞ 0` 故 ＝ `⌊x10⌋`）⇒ `r_lo + (_rw25_cell_398(k_lo + 1) - r_lo) * (x10 - k_lo)`（`17.9 ＜ W ＜ 18` 之次格點 ＝ `k ＝ 180` ⇒ `100`）。舊表（`table = [0.0, 17.4, …, 100.0]`）已刪；函式內無二表之值之數之常數（`X3` 綠·其數之常數唯 `0`、`0.0`、`100.0`、`1.0`、`10.0`、`1e-09`、`10`、`1`）。docstring 改述附表 25 與 ①〜④ 與所據（`W-G.9-398`）。
- **格點之判與浮點之鄰**：判式以 `10W` 與其最近之整數之距 ≤ `1e-9`（即 `W` 距格點 ≤ `1e-10 m`）為格點 ⇒ 直取格值（⛔ 經內插而生之殘差）——`0.1 × 53`（＝ `5.300000000000001`）、`2.7 ＋ 2.6`、`5.3 ± 1e-12` 皆得 `45.85`；距格點 ＞ `1e-10 m` 者依其所在之格間內插（於吸附之界有 ≤ 斜率 × `2e-10` 之微跳·方向不減）。`round` 為 Python 之偶數捨入，然唯用以求「最近之整數」之距，於距 ≤ `1e-9` 之判無涉偶數之歧。

**`R-3`**：`rw_increment`、`RW_SATURATION_WIDTH_M`、`main` 與一切他之頂層節點、`verify/` 之一切 `*.py` 一字⛔ 動（`V-7`／`F41 X1`、`X4`、`X7`）；新增之巢狀函式名 `_rw25_cell_398`（帶 `398`·全檔恰一見）；`tests/test_pool_slot.py` 之改唯塊 `Fy55`。

**`rw_from_width` 之一切呼叫處**（`grep -n rw_from_width -- app.py verify/*.py`·生產碼 `34` 檔·次趟之樹）：

```
## grep -n rw_from_width -- app.py verify/*.py（生產碼 34 檔：app.py ＋ verify/ 頂層 *.py 33 檔）
app.py:6117:#   ⇒ 做成**單一具名常數**（`rw_from_width` 與 `_build_burden_range` 共用），
app.py:6154:def rw_from_width(W: float) -> float:
app.py:6194:    本筆側街負擔比率 = (R(W_cur) − R(W_prev)) / 100，R = rw_from_width（累積表，W≥18→100）。
app.py:6195:    clamp 內建於 rw_from_width → W_prev≥18 之後各筆自動為 0。
app.py:6199:    return max(0.0, (rw_from_width(W_cur) - rw_from_width(W_prev)) / 100.0)
app.py:8340:      rw_func      R(W) 累積函數（%）；預設 rw_from_width
app.py:8350:    R = rw_func if rw_func is not None else rw_from_width
app.py:11080:    中央池宗之 W ≫ 18m ⇒ `rw_from_width(W)=100%`；若誤走「先查 W→Rw 再看跨占」，
app.py:12379:        #   `rw_from_width` 之斜率**放大**後進入 ΣRw。歸因須逐位比對，故曝未捨入值。
app.py:20430:    "solve_G_binary", "iterate_G_S", "rw_from_width", "get_min_lot_size",
app.py:30268:                            _expect = rw_from_width(wlast) - rw_from_width(_w_start)
verify/app_harvest.py:160:        "_boundary_len_on_line", "rw_from_width",
verify/stepg_pipeline.py:421:    _rw_from_width = ns["rw_from_width"]      # 結構閘 telescoping 用
verify/stepg_pipeline.py:1504:                        'delta': _rw_from_width(_wstart) - _rw_from_width(_prev_far),
verify/stepg_pipeline.py:1506:                        'delta_self': _rw_from_width(_wnear) - _rw_from_width(_prev_far),
verify/stepg_pipeline.py:1643:            _tele_exp = _rw_from_width(_sd_Wf) - _rw_from_width(_sd_W0)
verify/stepg_pipeline.py:1653:        #   ⚠️ **刻意不採**「ΣRw_階段2 ≤ 100 − 理論@k*」之不等式版——`rw_from_width` 於 W≥18
verify/stepg_pipeline.py:1677:            _exp_s2 = _rw_from_width(_Wf_t2) - _rw_from_width(_W1_end_t2)     # §四(a)：回原式
```

**`RW_TABLE_25` 之逐格與手冊原文之對拍**（執行端自手冊之原文解析·以二進位讀檔、`split(b'\n')` 使列號 ＝ `grep -n`；每格以 `Decimal(手冊之字面) == Decimal(repr(表之值))` 比；整數公尺之格以 `Decimal` 之 `ROUND_HALF_UP` 取一位比簡表）：

```
手冊之列（附表 25·grep -n 之列號） {1: 4053, 2: 4062, 3: 4063, 4: 4064, 5: 4065, 6: 4066, 7: 4067, 8: 4068, 9: 4069, 10: 4070, 11: 4071, 12: 4072, 13: 4073, 14: 4074, 15: 4075, 16: 4076, 17: 4077}
逐格對拍（手冊字面之 Decimal 對 RW_TABLE_25 之字面）：格數 170 不符 0
18 m 之列: [(4078, '18 100.00 註：本表係由前面負擔百分率簡表推演而來。')]
簡表（手冊第 3029〜3037 列）:
   3029 Ｒw 表示街角地側面道路負擔百分率，即重劃後分配於土地寬度為Ｗ
   3030 公尺時，所應分攤之側面道路負擔百分比。其計算表如下：
   3031 W(公尺) 1 2 3 4 5 6 7 8 9
   3032 Rw(％) 17.4 24.4 31.3 37.8 44.0 50.0 55.7 61.1 66.3
   3033 W(公尺) 10 11 12 13 14 15 16 17 18
   3034 Rw(％) 71.1 75.7 80.0 84.0 87.8 91.3 94.4 97.4 100
   3035 Ｆ表示街角第一筆土地面臨側面道路之長度
   3036 Ｓ表示宗地面臨正街之實際分配寬度
   3037 l1 表示側面道路負擔尺度
整數公尺之 17 格以 ROUND_HALF_UP 取一位 對簡表 之不符: []
Python round 異於 ROUND_HALF_UP 之格: ['31.25', '66.25', '91.25']
170 格＋18 m 嚴格遞增: True
```

**對 `§三-3` 各款之自查**：第 `1` 款 ＝ `#5`（`F23 wiring 7d8e954`）、`#6`（`F24 wiring d7a5ea4`）於撰碼中與二趟之驗皆綠（⑥-1 項 `1` 之撞已於倉前解）；第 `2` 款 ＝ 突變之器（`#19`、`#22`、`#43`、`#47` 等）綠·新碼⛔ 照抄既有之句；第 `3` 款 ＝ `main` 之節點⛔ 變（`V-7` 之 AST·`#54` 等綠）；第 `4` 款 ＝ `V-7` 之 AST（增 `['RW_TABLE_25']`、減 `[]`、相異 `['RW_TABLE_25', 'rw_from_width']`）、`verify/` 相異 `0`；第 `5` 款 ＝ `F41 X6` 綠；第 `6` 款 ＝ 簽名、回傳之形照舊（`raise` 唯於域外·現行之路不可達）。

---

## ⑧ `app.py` 之全文差異

同目錄之 `W-G.9-398R_側面道路負擔百分率之附表25_差異.diff`（＝ `git diff 07d12028d99b3a178c2a87edaea0b70ae8a754ac c35d32a3cd43da5bdcb1c197d16b5757a1b39861 -- app.py`·`+51`／`−12`）。

---

## ⑨ 工項三之 `checkidx`、`gen_fa_index` 之出艙

- 二塊寫後：`python3 <O>/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列 ``索引列數 124；內部字樣 122；外部指標 9；不合 0``。
- `python3 <O>/gen_fa_index.py /tmp/w <O>/FX_regen.md` ⇒ `rc 0`；出艙 ``則 124；加註節 14；列 158``；`<O>/FX_regen.md` 與 `.claude/skills/failure-archaeology-index/SKILL.md` `cmp` 逐位同。

---

## ⑩ 各段耗時（UTC·並行之數）

| 段 | 起 → 迄 | 並行 | 備 |
|---|---|---|---|
| 接單（`ops/queue`） | `08:23` | — | `cb55620` |
| `§零-0`、pre-flight、工項零、工項一 | `08:23` → `08:26` | 1 | 依賴之裝與釘回含之 |
| 前置 (甲)(乙) `53` 呼叫 | `08:27` → `09:16`（約 `50` 分） | `2` | 耗時之和 `5951` s；撰碼與倉外之快掃並行於另一拷貝（快掃之時至多 `3` 程序） |
| 驗·首趟（`a18efd9`·`94` 呼叫） | `09:17` → `10:54`（約 `97` 分） | `2` | 耗時之和 `11659` s |
| 唯讀獨立審查（首審） | `10:55` → `11:22` | reviewer 自起之程序 ≤ `2` | — |
| 修（`A-1`）與增審 | `11:24` → `11:31` | — | — |
| 驗·次趟（`c35d32a`·`94` 呼叫） | `11:26` → `13:08`（約 `102` 分） | `2` | 耗時之和 `12198` s |
| 工項二之推、工項三 | `13:08` → `13:10` | 1 | — |
| 工項四（本報告） | `13:10` → | 1 | — |

---

## 附錄子　前置 (甲)(乙) 之 `stdout` 之全文（`07d1202`·逐呼叫）

### `#4`　`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

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

### `#5`　`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`（`rc 0`·`stderr` `0` B·`34.1` s）

````text
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（604）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
````

### `#17`　`python3 verify/probes/probe_WG9363_k953.py run <repo>`（`rc 1`·`stderr` `0` B·`389.6` s）

````text
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  🔴 R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.51／ΣG 之變 2934.51（和 ≤ 0.1）False
      ('628-37(1)', ('R1', 'right', 285.21), ('R1', 'right', 285.22))
      ('628-40(1)', ('R2', 'left', 359.59), ('R2', 'left', 359.6))
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  🔴 R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.87／ΣG 之變 3663.87（和 ≤ 0.1）False
      ('628-35(2)', ('R1', 'left', 730.81), ('R1', 'left', 730.82))
      ('628-40(1)', ('R2', 'left', 359.59), ('R2', 'left', 359.6))
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 ['R3@3.5', 'R3@0.0']；rc 1
````

### `#6`　`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`（`rc 0`·`stderr` `0` B·`35.4` s）

````text
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（606）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
````

### `#13`　`python3 verify/probes/probe_WG9367_adj4.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.7` s）

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

### `#18`　`python3 verify/probes/probe_WG9367_adj4.py run <repo>`（`rc 1`·`stderr` `0` B·`537.8` s）

````text
  ✅ R1@3.5：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@3.5：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  ✅ R3@3.5：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6600（和 +0.0200·≤ 0.1）
  ✅ R4@3.5：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@3.5：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
  ✅ R1@0.0：第一趟之紀錄 1 列 ＝ 本器所載（off 之紀錄 ＝ []：True）
  ✅ R2@0.0：街角第 1 宗 ＝ off 之實跑 True（8 宗）
  🔴 R3@0.0：配地之變 1 宗·抵費地之變 1 街廓 ＝ 本器所載；ΣΔG +7.6800（Σ|ΔG| 7.6800）／ΣΔ抵費地 -7.6600（和 +0.0200·≤ 0.1）
      得 ({'628-34(2)': (250.24, 257.91)}, {'R3': (1659.06, 1651.4)})
  ✅ R4@0.0：調配之輸入之類·合併單位數 17·去者 ['G001'] ＝ 本器所載
  ✅ R5@0.0：受詞之片之段三之三鍵 ＝ 本器所載（1 片）
⇒ 紅 ['R3@0.0']；rc 1
````

### `#7`　`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`（`rc 0`·`stderr` `0` B·`3.0` s）

````text
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
````

### `#19`　`python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>`（`rc 0`·`stderr` `0` B·`8.0` s）

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

### `#20`　`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

````text
── K-9-66／K-9-67／K-9-68 之各支 ──
  ✅ A1 KL 例一（街廓 B 能再容 130）：建地全部一次不過 ⇒ 按比例 52／43.33／34.67（130 × 60／150 等）；道路未試
  ✅ A2 KL 例二（能再容 170）：建地 150 全入；剩 20 按 30：20：10 分給道路 10／6.67／3.33
  ✅ A3 一次全部即過 ⇒ 全入、唯整體一步
  ✅ A4 唯一類（道路 30／20·容 25）⇒ 整體即該類之全部（⛔ 重試全部）⇒ 按比例 15／10；全量之試恰一次
  ✅ A5 格 ＝ 該類之合計每 0.01 ㎡：容 60.005 ⇒ 60.00；容 59.999 ⇒ 59.99
  ✅ A6 建地、道路皆全入；公設地 200 唯容 10 ⇒ 0.05
  ✅ A7 建地之比例步亦全不容 ⇒ 未成（比例 0）、其後之類未試、⛔ 併入
  ✅ A8 類非三類之一 ⇒ 停機；來源量 ≤ 0 ⇒ 停機
  ✅ A9 回傳之態 ＝ 末次通過之試所回之物件；全不過 ⇒ 輸入之態（同一物件）
  ✅ B1 k967_rank：應分配面積以 0.01 ㎡ 比（100.004 ＝ 100.00·100.006 ＝ 100.01）；同 ⇒ 重劃前面積大者先
  ✅ B2 k967_rank：再同（重劃前面積 69.996 ＝ 70.00）⇒ 暫編地號小者先
  ✅ B3 k967_pre_area：成員之分攤登記面積之和；成員缺 ⇒ 自身；取不到 ⇒ 停機
  ✅ B4 k967_pool_out：單元自身之片取入池閘部分併出之和、他成員之片取入池閘成員部分併出［片］之和；無帳者（缺或空）⛔ 列
  ✅ B5 k967_pool_out：同一片之帳見於二處（二單元·或自身與成員）⇒ 停機；量 ≤ 0 ⇒ 停機
  ✅ B6 k967_pool_less：表減其量（新表·原表⛔ 動）；None／空 ⇒ 同值；表外之片 ⇒ 停機；非 dict ⇒ 停機
  ✅ C1 入池閘之代表宗：G 並列（60.00）⇒ 重劃前面積大者 Y2（100 ＞ 80）
  ✅ C2 G 差 0.004（0.01 ㎡ 為同）⇒ 並列 ⇒ 重劃前面積大者 Y2
  ✅ C3 G 差 0.006（60.01 ＞ 60.00）⇒ G 大者 Y1
  ✅ C4 G 與重劃前面積皆同 ⇒ 暫編地號小者 Y1
  ✅ T1 手冊先行·三位地主之建地同到 BB（容 130）⇒ K-9-66 之列、按比例 52／43.33／34.67；甲之剩下 8 依距離併入 A2；乙丙之剩下入合併單位；部分併出者留 build（面積_m2 減其量·段三部分併出·⛔ 段三餘量）
  ✅ T2 手冊先行·K-9-68：甲之 80 第 1 輪全入 BB；乙之 60 第 1 輪試 BC 不過、第 2 輪轉 BB 唯得剩下之 20（⛔ 重分）
  ✅ T3 手冊先行·第 2 輪（K-9-51）二位地主之剩下同到 BD（容 25）⇒ 亦依 K-9-66 按比例 15／10；餘入合併單位
  ✅ T5 手冊先行·第 1 輪之來源量 ＝ 計畫之量 ÷ κ（BB 之 κ ＝ 2）⇒ 比例 0.433333：A1 52／B1 43.33／C1 34.67；甲之剩下 34 全入 A2；帳以來源量計（Y 21.67／Z 17.33）
  ✅ U0 段三後處理·對照：整批即過 ⇒ 二列皆成（⛔ K-9-66 之列）
  ✅ U1 段三後處理·二位地主之公設地同到 B3（剩下能容 50）⇒ K-9-66 之列、按比例 30／20；剩下轉調配
  ✅ U2 段三後處理·第 2 輪二位地主之剩下同到 B5（容 25）⇒ 亦依 K-9-66 按比例 15／10
  ✅ V1 第一趟·二受詞之建地同到 BB（容 50）⇒ K-9-66 之列、按比例 30／20；剩下留於合併單位；部分併出者留 build
  ✅ V2 第一趟·K-9-68：g1 之 80 第 1 輪全入 BB；g2 之 60 第 1 輪於 BC 不過、第 2 輪至 BB 唯得剩下之 20（⛔ 重分）
  ✅ W1 調配之輸入·部分併出之建地（其單元不配地）⇒ 建築街廓內不能分配：原有面積 ＝ 50 × 30／50 ＝ 30、已併出 20 計入原位次配地、應分配面積 ＝ 該趟之 G（原位·剩下之面積）；守恆
  ✅ W2 調配之輸入·部分併出之建地（其單元配地）⇒ 原位次配地（配地街廓含受併宗之街廓）；守恆
  ✅ W3 公設地調配之 temp：部分併出之建地（⛔ 段三餘量）原物件入之；全數併出之建地去之；餘同一物件
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 31／31
⇒ 紅 []；rc 0
````

### `#21`　`python3 verify/probes/probe_WG9373_k966.py wiring <repo>`（`rc 0`·`stderr` `0` B·`2.5` s）

````text
  ✅ Y1 模組層之新名與簽名（簽名之異 []；K966_CLASSES ('建地', '道路', '公設地')；K966_GRID 0.01）
  ✅ Y2 k966_block_merge 之呼叫恰在四處各一（三處 ＋ 入池閘·W-G.9-375）（四處 {'k953_manual_run': 1, 'k6b_stage3_run': 1, 'adj4_pass1_run': 1, 'k929_6_fixpoint': 1}；全檔 4）
  ✅ Y3 k967_rank 之呼叫（入池閘 ≥ 1·手冊先行 ≥ 3·段三 ≥ 1·第一趟 ≥ 1）（{'k929_6_fixpoint': 2, 'k953_manual_run': 4, 'k6b_stage3_run': 3, 'adj4_pass1_run': 1}）
  ✅ Y4 新碼⛔ 案件字面（[]）
  ✅ Y5 已去之巢狀 def ⛔ 見（[]）
  ✅ Y6 擇宗⛔ 以「並列 ⇒ 停機」（[]）
  ✅ Y7 三處之 k966_block_merge 皆以 state 為前態、以其回傳之態承接（state, … ＝ …(state, …)）（{'k953_manual_run': [True], 'k6b_stage3_run': [True], 'adj4_pass1_run': [True]}）
  ✅ Y8 五處之試算（段三·手冊先行之 harness 與畫面、第一趟之共用）皆以同一 build 回 members 與 pool_out（k967_pool_out 之呼叫直書為 return 之鍵 pool_out 之值）（k953_units_of 之呼叫 [('app.py', 'adj4_trial_state', True), ('app.py', '_trial953s', True), ('app.py', 'alloc_state', True), ('selection_pipeline.py', '_trial_k', True), ('selection_pipeline.py', 'alloc_state', True)]；k967_pool_out 之呼叫 5）
  ✅ Y9 調配之輸入之 build ＝ 末次入池閘之出：SS_ADJ_BUILD_FINAL 恰一寫於 f3_screen_stepg_run 之入池閘之後；畫面與 harness 之段三（含手冊先行·第一趟）皆先於 step G（寫 [(23108, 'f3_screen_stepg_run')]·入池閘 [21568]；畫面 段三 [29569] ＜ step G [29946]；harness run_corner_pk_k6b [611] ＜ run_step_g 692（build ＝ s3_by_tag[tag]['build']））
⇒ 紅 []；rc 0
````

### `#22`　`python3 verify/probes/probe_WG9373_k966.py mutate <repo>`（`rc 0`·`stderr` `0` B·`62.5` s）

````text
  ✅ N00 —·基準（⛔ 突變）：錨 1 見；所指 []；紅 []
  ✅ N01 K-9-66 ①·整體成而⛔ 回：錨 1 見；所指 ['F27:A3']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K2', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K9', 'F23:K14', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K37', 'F23:K38', 'F23:K39', 'F23:K40', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K27', 'F24:K3', 'F24:K4', 'F24:K8', 'F27:A3', 'F27:T1', 'F27:T2', 'F27:T5', 'F27:V2']
  ✅ N02 K-9-66 ②·唯一類者亦以該類之全量再試：錨 1 見；所指 ['F27:A4']；紅 ['F27:A4']
  ✅ N03 K-9-66 ②·類之序反之：錨 1 見；所指 ['F27:A2', 'F27:A6']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21', 'F23:K16', 'F23:K20', 'F23:K23', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F27:A1', 'F27:A2', 'F27:A6', 'F27:A7', 'F28:D3', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S4', 'F28:S6']
  ✅ N04 K-9-66 通知 2·格改 0.1：錨 1 見；所指 ['F27:A5']；紅 ['F23:K15', 'F23:K75', 'F24:K24', 'F27:A5']
  ✅ N05 K-9-66 ②·按比例之後仍試次類：錨 1 見；所指 ['F27:A1', 'F27:A7']；紅 ['F24:K24', 'F27:A1', 'F27:A7']
  ✅ N06 K-9-66·回傳輸入之態（⛔ 末次通過之態）：錨 1 見；所指 ['F27:A9']；紅 ['F16:K10', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K20', 'F23:K28', 'F24:K13', 'F24:K23', 'F24:K4', 'F24:K5', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N07 K-9-66 ②·二分法之支反之：錨 1 見；所指 ['F27:A1']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N08 K-9-66·要求之類之停機去之：錨 1 見；所指 ['F27:A8']；紅 ['F27:A8']
  ✅ N09 K-9-66 ②·二分法⛔ 記通過之態：錨 1 見；所指 ['F27:A9']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N10 K-9-66 ②·試之量與所記之量不一：錨 1 見；所指 ['F27:A1']；紅 ['F16:K10', 'F16:K10′', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K14', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N11 K-9-66 ②·類之全量成而⛔ 承接其態：錨 1 見；所指 ['F27:A2', 'F27:A6']；紅 ['F16:K18', 'F23:K16', 'F23:K20', 'F24:K13', 'F24:K23', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F27:A2', 'F27:A6']
  ✅ N12 K-9-67·去重劃前面積之鍵：錨 1 見；所指 ['F27:C1']；紅 ['F23:K3', 'F23:K51', 'F24:K7', 'F27:C1', 'F27:C2', 'F28:Q1', 'F28:Q2']
  ✅ N13 K-9-67·應分配面積⛔ 以 0.01 ㎡ 量化：錨 1 見；所指 ['F27:C2']；紅 ['F27:C2']
  ✅ N14 K-9-67·重劃前面積之序反之：錨 1 見；所指 ['F27:B1', 'F27:C1']；紅 ['F23:K3', 'F23:K51', 'F24:K7', 'F27:B1', 'F27:C1', 'F27:C2', 'F28:Q1', 'F28:Q2']
  ✅ N15 K-9-67·重劃前面積先於應分配面積：錨 1 見；所指 ['F27:B1']；紅 ['F23:K50', 'F27:B1']
  ✅ N16 K-9-67·成員缺⛔ 取自身：錨 1 見；所指 ['F27:B3']；紅 ['F27:B3']
  ✅ N17 K-9-68·段三：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:U1']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S4', 'F28:S6']
  ✅ N18 K-9-51·段三：第 5 項之候選⛔ 扣已試而未全收之街廓：錨 1 見；所指 ['F27:U2']；紅 ['F16:K17', 'F16:K19', 'F16:K2', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N19 K-9-51·段三：第 5 項之候選之序以 k967_rank 先於距離：錨 1 見；所指 ['F16:K3']；紅 ['F16:K27', 'F16:K3', 'F16:K4', 'F16:K7']
  ✅ N20 K-9-66·段三：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:U1']；紅 ['F27:U1', 'F27:U2']
  ✅ N21 K-9-68·段三：第 5 項之輪之剩下⛔ 減其所併：錨 1 見；所指 ['F16:K2']；紅 ['F16:K10', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K2', 'F16:K21', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K9']
  ✅ N22 R-17″·段三：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L6']；紅 ['F28:D3', 'F28:L6']
  ✅ N23 R-17″·段三：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L1', 'F28:L6']；紅 ['F28:L1', 'F28:L6']
  ✅ N24 R-17″·段三：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L1']；紅 ['F28:D3', 'F28:L1', 'F28:L6']
  ✅ N25 R-19″·段三：第 5 項之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L6']；紅 ['F28:D3', 'F28:L6']
  ✅ N26 K-9-66·段三：試施之受併宗之量⛔ 乘 κ：錨 1 見；所指 ['F16:K10']；紅 ['F16:K10', 'F16:K10′']
  ✅ N27 K-9-68·段三：第 1 輪⛔ 記已試而未全收之街廓：錨 1 見；所指 ['F27:U2']；紅 ['F16:K17', 'F16:K19', 'F16:K2', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N28 R-7 ③·段三：題一 4 之半之片⛔ 入第 5 項之輪：錨 1 見；所指 ['F16:K17']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21']
  ✅ N29 K-9-66·段三：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:U1']；紅 ['F16:K10', 'F16:K10′', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F27:U1', 'F28:D3', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N30 R-7 ②·段三步驟 10：第 1 輪之來源量⛔ 除 κ：錨 1 見；所指 ['F16:K10']；紅 ['F16:K10', 'F16:K10′']
  ✅ N31 R-7 ②·段三步驟 10：非建地之片之剩下⛔ 記：錨 1 見；所指 ['F27:U1']；紅 ['F16:K10′', 'F16:K13', 'F16:K14', 'F16:K14′', 'F16:K4', 'F16:K8', 'F27:U1']
  ✅ N32 R-7 ②·段三步驟 10：剩下⛔ 入第 5 項之輪：錨 1 見；所指 ['F27:U2']；紅 ['F16:K10', 'F16:K11', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K2', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K25', 'F16:K26', 'F16:K27', 'F16:K28', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K32', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:S3', 'F28:S5']
  ✅ N33 K-9-66 R-5 (a)·段三：建地之部分併出⛔ 留 build：錨 1 見；所指 ['F16:K19', 'F16:K7']；紅 ['F16:K19', 'F16:K7', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N34 K-9-68·手冊先行：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:T1']；紅 ['F23:K16', 'F23:K20', 'F23:K23', 'F23:K42', 'F23:K65', 'F24:K15', 'F27:T1', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L2', 'F28:L4']
  ✅ N35 K-9-51·手冊先行：候選⛔ 扣已試而未全收之街廓：錨 1 見；所指 ['F27:T2']；紅 ['F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K42', 'F23:K61', 'F23:K63', 'F23:K65', 'F23:K67', 'F23:K70', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L2', 'F28:L4']
  ✅ N36 K-9-66·手冊先行：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:T1']；紅 ['F27:T1', 'F27:T3', 'F27:T5']
  ✅ N37 K-9-68·手冊先行：K-9-51 之輪之剩下⛔ 減其所併：錨 1 見；所指 ['F27:T1']；紅 ['F23:K14', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K42', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K65', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F27:T1', 'F27:T5']
  ✅ N38 R-17″·手冊先行：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L4']；紅 ['F28:D1', 'F28:L4']
  ✅ N39 R-17″·手冊先行：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L4']；紅 ['F28:L4']
  ✅ N40 R-17″·手冊先行：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L2']；紅 ['F28:D1', 'F28:L2', 'F28:L4']
  ✅ N41 R-19″·手冊先行：K-9-51 之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L4']；紅 ['F28:D1', 'F28:L4']
  ✅ N42 K-9-66 R-5·手冊先行：第 1 輪之來源量⛔ 除 κ：錨 1 見；所指 ['F27:T5']；紅 ['F27:T5']
  ✅ N43 R-18″·手冊先行：趟末之前帳取當下之態：錨 1 見；所指 ['F27:T1']；紅 ['F27:T1', 'F27:T3', 'F27:T5']
  ✅ N44 K-9-66·手冊先行：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:T1']；紅 ['F23:K20', 'F23:K28', 'F23:K33', 'F23:K35', 'F23:K36', 'F23:K37', 'F23:K39', 'F23:K40', 'F24:K15', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L4']
  ✅ N45 K-9-68·第一趟：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K14', 'F24:K23', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K3', 'F24:K4', 'F24:K5', 'F24:K6', 'F27:V1', 'F28:L3']
  ✅ N46 R-17″·第一趟：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L5']；紅 ['F28:D2', 'F28:L5']
  ✅ N47 R-17″·第一趟：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L5']；紅 ['F28:L5']
  ✅ N48 R-17″·第一趟：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L3']；紅 ['F28:D2', 'F28:L3', 'F28:L5']
  ✅ N49 R-19″·第一趟：各輪之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L5']；紅 ['F28:D2', 'F28:L5']
  ✅ N50 K-9-66·第一趟：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:V1']；紅 ['F27:V1']
  ✅ N51 K-9-68·第一趟：剩下⛔ 減其所併（記為 0）：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K6', 'F24:K8', 'F27:V1', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N52 K-9-68·第一趟：受詞每輪沿名單⛔ 止於首一有其宗之街廓：錨 1 見；所指 ['F27:V2']；紅 ['F24:K23', 'F24:K3', 'F24:K4', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N53 K-9-66·第一趟：同類之片之序（剩下大者先）反之：錨 1 見；所指 ['F24:K25']；紅 ['F24:K25']
  ✅ N54 K-9-67·第一趟：受併宗之序去 k967_rank：錨 1 見；所指 ['F24:K7']；紅 ['F24:K7', 'F28:D2', 'F28:L5']
  ✅ N55 R-18″·第一趟：趟末之前帳取當下之態：錨 1 見；所指 ['F27:V1']；紅 ['F27:V1', 'F27:V2']
  ✅ N56 K-9-66·第一趟：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K23', 'F24:K27', 'F24:K3', 'F24:K4', 'F24:K5', 'F27:V1', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N57 K-9-66 通知 3·調配之輸入：建地之部分併出之原有面積⛔ 依剩下之比：錨 1 見；所指 ['F27:W1', 'F27:W2']；紅 ['F27:W1', 'F27:W2', 'F28:I1', 'F28:I2', 'F28:I3']
⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0
````

### `#23`　`python3 verify/probes/probe_WG9373_k966.py run <repo>`（`rc 1`·`stderr` `0` B·`321.2` s）

````text
  ✅ R1@3.5：段三後處理 6 列皆成、⛔ K-9-66／第 5 項 True；手冊先行之整批 ['成']、⛔ K-9-66／K-9-51 True；第一趟 1 列皆整體成 True
  ✅ R2@3.5：入池閘之代表宗（街廓, 成員, 標的, 並列之 G, 並列之重劃前面積）[('R3', ['628-28(1)', '628-29(1)'], '628-28(1)', 69.2, 114.0), ('R6', ['628-21(1)', '628-22(1)', '628-23(1)'], '628-21(1)', None, None)]
  ✅ R3@3.5：段三之試算之 members harness ＝ 畫面 True（51 宗）；R3 之單元 ['628-28(1)', '628-29(1)']
  ✅ R1@0.0：段三後處理 0 列皆成、⛔ K-9-66／第 5 項 True；手冊先行之整批 ['成']、⛔ K-9-66／K-9-51 True；第一趟 1 列皆整體成 True
  🔴 R2@0.0：入池閘之代表宗（街廓, 成員, 標的, 並列之 G, 並列之重劃前面積）[('R3', ['628-28(1)', '628-29(1)'], '628-28(1)', 65.75, 114.0), ('R6', ['628-21(1)', '628-22(1)', '628-23(1)'], '628-21(1)', None, None)]
  ✅ R3@0.0：段三之試算之 members harness ＝ 畫面 True（52 宗）；R3 之單元 ['628-28(1)', '628-29(1)']
⇒ 紅 ['R2@0.0']；rc 1
````

### `#14`　`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

````text
  ✅ K1 弱弱聯合·大者在前 ⇒ X2 併入 X、於 X 之位；乙照原位
  ✅ K2 弱弱聯合·大者在後 ⇒ X 併入 X2；乙遞補而不配地
  ✅ K3 同街廓先（弱弱聯合）·他街廓之己宗（他地號）⛔ 依手冊併入（K-9-73·改 K-9-64）
  ✅ K4 他街廓之己宗相連（他地號）⇒ 入池閘⛔ 處（K-9-73）
  ✅ K5 合併後反不能配 ⇒ 回原狀、併入原可配之宗之原位（K-9-58 ③）
  ✅ K6 街角第 1 宗⛔ 合併、依手冊併入（K-9-58 ①）
  ✅ K7 跨左右推進 ⇒ 併向應分配面積較大之一側（K-9-58 ②）
  ✅ K8 第 3 步：併入同街廓不相連之已配得之宗（其位）
  ✅ K9 N0-9 之片亦先判同街廓（K-9-73·改 K-9-64 ③）
  ✅ K10 重排後遞補者從第 1 步起處理
  ✅ K11 弱弱聯合之宗其後配不到 ⇒ ⛔ 再弱弱聯合
  ✅ K12 第 3 步併入後反不配地 ⇒ 回原狀
  ✅ K13 經同地主之道路片相連 ⇒ 入池閘⛔ 處（交手冊先行·K-9-73）
  ✅ K14 輸入之單元之成員之形與成員之列（NOTE 5）
  ✅ K15 單元之成員之切片取不到 ⇒ 停機
  ✅ K16 入池閘⛔ 判經道路片之相連 ⇒ 切片未給亦⛔ 停機（K-9-73）
  ✅ K17 檢核之輸入未給 ⇒ 停機
  ✅ K18 調配之輸入：宿主在他街廓 ⇒ 配地街廓 ＝ 宿主之街廓
  ✅ K19 調配之輸入：入池閘之帳之部分併出
  ✅ K20 重劃前面積取輸入之 build 之帳（K-9-67·補令一 R-16′）
  ✅ K21 重劃前面積減入池閘之部分併出（入池閘部分併出·輸入之帳）
  ✅ K22 K-9-58 ③ 二次皆不配地 ⇒ 收斂（⛔ 空轉·⛔ 往他街廓）
  ✅ K23 部分併出之帳隨剩下入單元（調配之輸入⛔ 重計）
  ✅ K24 第 1 步之相連以其自身之地（他街廓併入之片⛔ 計）
  ✅ K25 受併宗最後不配地 ⇒ 已併入者回原狀（K-9-61 ⑤）
  ✅ K26 調配之輸入：受併宗為他單元之成員
  ✅ K27 經同地主之連續道路片相連 ⇒ 入池閘⛔ 處（交手冊先行·K-9-73）
  ✅ K28 部分併入後之剩下⛔ 再試他街廓（續第 3 步起）
  ✅ K29 地主於本街廓已有配得之宗 ⇒ ⛔ 弱弱聯合（K-9-57 ④）
  ✅ K30 N0-9 之片亦依手冊併入街角第 1 宗（K-9-73·K-9-58 ①）
  ✅ K31 第 3 步：街角第 1 宗依手冊併入
  ✅ K32 回原狀後各併入原可配之宗中應分配面積最大者（K-9-76 ②·⛔ 相鄰者先）
  ✅ K33 單元之部分併入 ⇒ 各成員乘同一百分比（巳 ①·K-9-66）
  ✅ K34 合併之宗終不配地 ⇒ 回原狀（K-9-58 ③·收斂時）
  ✅ K35 已試之帳以成員為準
  ✅ K36 調配之輸入：配地街廓含宿主之街廓
  ✅ K37 合併之列其後同一標的再受同街廓之併入 ⇒ 前列「續併」、末列「留置」
  ✅ K38 受併宗之相連⛔ 藉他街廓併入之片
  ✅ K39 回溯由最近之一次施起
  ✅ K40 不相連而併入之片⛔ 為相連
  ✅ K41 他街廓之併入之回溯由最近之一次起（K-9-61 ⑤）
  ✅ K42 回原狀之組合⛔ 再施（跨回溯）
  ✅ K43 回原狀後之併入⛔ 取已試之組合
  ✅ K44 回原狀後之併入逐宗（其一不配地⛔ 連帶其他）
  ✅ K45 回原狀之帳跨回溯而存
  ✅ K46 調配之輸入：段三之受併宗未配地 ⇒ 停機
  ✅ K47 N0-9 之片之回原狀後之併入
  ✅ K48 回原狀之帳之序定於回原狀之時（依其時之應分配面積·K-9-76 ②）
  ✅ K49 回原狀之帳之分不到之宗 ①′ 先於 ①
  ✅ K50 回原狀之帳之序以該次合併時之應分配面積定
  ✅ K51 成員之地價區段相異 ⇒ 各以其來源量計
  ✅ K52 合併之單元之部分併入之調配之輸入
  ✅ K53 成員之剩下之合與宗之面積不符（含非成員之土地）⇒ 停機
  ✅ K54 k965_part_split 之純函式
  ✅ K55 含非成員之土地而部分併入皆不過檢核 ⇒ ⛔ 停機·記未成（停機待檢核過後）
  ✅ K56 單片含非其成員之土地（面積_m2 淨 ≤ 0）而部分併入過檢核 ⇒ 停機（GB-205）
  ✅ K57 單片之帳相合 ⇒ 部分併入照常（其帳為全量）
  ✅ K58 單片含非其成員之土地而部分併入皆不過檢核 ⇒ ⛔ 停機·記未成
  ✅ K59 街角第 1 宗之應分配面積小於他宗 ⇒ 併入應分配面積大者（K-9-73 ①）
  ✅ K60 N0-9 之片亦入弱弱聯合（K-9-73 ②）
  ✅ K61 街角第 1 宗之依手冊之併入部分成／未成 ⇒ 其餘續依第 3 步併入次大之已配得之宗（K-9-73 ①）
  ✅ K62 同街廓相連之合併含可配得之宗 ⇒ 標的 ＝ 可配得之最大一塊（其側其位·K-9-76 ①）
  ✅ K63 回原狀之帳之序 ＝ 可配得之宗之應分配面積大者先（⛔ 相連者先·K-9-76 ②）
  ✅ K64 宗之成員帶「第31條第3款併入」⇒ ⛔ 併入同街廓之已配得之宗；弱弱聯合不以已配得之宗之有無為限（K-9-75 ①）
  ✅ K65 他宗之分量⛔ 含帶標記之宗（K-9-75 ①）
  ✅ K66 帶標記之宗之分量⛔ 含已配得之宗 ⇒ 與相連之配不到者依第 4 步合併（K-9-75 ①）
  ✅ K67 帶標記之宗之相連之合併不配地 ⇒ 續與不相連之配不到之宗弱弱聯合（全部·K-9-77）
  ✅ K68 同歸戶之他宗在推進序之前 ⇒ 帶標記之宗與其相連之宗先合併（K-9-77）
  ✅ K69 他街廓之帶標記之宗⛔ 先之（K-9-77）
  ✅ K70 他歸戶之帶標記之宗⛔ 先之（K-9-77）
  ✅ K71 帶標記之宗二 ⇒ 依 k967_rank 之序先之（K-9-77）
  ✅ K72 帶標記之宗已配得 ⇒ 相連之配不到之宗依第 3 步併入之（K-9-77）
  ✅ K73 帶標記之宗二·推進序之首⛔ 帶標記 ⇒ 依 k967_rank 之序（K-9-77）
  ✅ K74 推進序之首為帶標記而序次之宗 ⇒ 序首之帶標記之宗先之（K-9-77）
  ✅ P0 判式自驗 74／74
⇒ 紅 []；rc 0
````

### `#15`　`python3 verify/probes/probe_WG9375_k965.py wiring <repo>`（`rc 0`·`stderr` `0` B·`2.1` s）

````text
  ✅ Y1 簽名：五位置參數 ＋ 關鍵字 max_rounds／temp_parcels／cat_of／front_rows（預設 None）
  ✅ Y2 harness 之 run_step_g：入池閘之呼叫恰一、注入三參數、切片取 session 之 f3_k965_temp
  ✅ Y3 畫面之 _k929_6_screen_gate：注入三參數（f3_temp_parcels·classified_blocks·sb_rows_by_label）
  ✅ Y4 harness 之 build_build_parcels 寫 session 之 f3_k965_temp
  ✅ Y5 k929_6_fixpoint 內：k966_block_merge 恰一（得 1）·k953_alloc_summary／k967_rank／_projection_order 皆呼
  ✅ Y6 adj_intake 讀「入池閘部分併出」與「入池閘成員部分併出」
  ✅ Y7 k929_6_fixpoint 之字串常數⛔ 含案件字面（命中 []）
  ✅ Y8 三【未裁】之停機已去（K-9-58 ①②③）·未收斂之停機仍在
  ✅ Y9 畫面對拍器之畫面之 session 寫 f3_temp_parcels（同 main()）
  ✅ Y10 k965_part_split 之簽名·k929_6_fixpoint 內呼之恰一（得 1）·_pre965 呼 _src965·巳 ① 之停機已去
  ✅ Y11 GB-205 之停機⛔ 在 k965_part_split（得 0）·在 _try965 之 _chk965 之後（_chk965 [10420]·停機 [10425]）
⇒ 紅 []；rc 0
````

### `#16`　`python3 verify/probes/probe_WG9375_k965.py run <repo>`（`rc 1`·`stderr` `0` B·`62.0` s）

````text
  ✅ R1@3.5：build 51 宗·單元 7 ＝ 本器所載 True
  🔴 R2@3.5：配地 28 宗·不配地 21 宗 ＝ 本器所載 False
  ✅ R3@3.5：入池閘之紀錄 7 列 ＝ 本器所載 True
  ✅ R1@0.0：build 52 宗·單元 6 ＝ 本器所載 True
  🔴 R2@0.0：配地 29 宗·不配地 21 宗 ＝ 本器所載 False
  ✅ R3@0.0：入池閘之紀錄 6 列 ＝ 本器所載 True
⇒ 紅 ['R2@3.5', 'R2@0.0']；rc 1
````

### `#1`　`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`（`rc 0`·`stderr` `0` B·`2.1` s）

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

### `#2`　`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`（`rc 0`·`stderr` `0` B·`109.0` s）

````text
  ✅ W1 頂層之新名與⛔ 案件字面：[True, True, True, True]／K974_PARAMS True／字面 []
  ✅ W2 main() 恰一處呼之：['k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)']
  ✅ W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）：
  ✅ W4 JUNCTION 存 session：
  ✅ W5 步驟 H 之段以假 st 實跑：[{'label': 'B1', 'front_width': 15.0, 'front_length': 0.0, 'front_new': False, 'left_side_width': 0.0, 'left_side_length': 0.0, 'left_side_new': False, 'right_side_width': 0.0, 'right_side_length': 0.0, 'right_side_new': False, 'front_scale': 2.25, 'left_side_scale': 0.5}]／[('warning', '⚠️ 警示甲')]／[('error', '⛔ 錯甲'), ('error', '⛔ 錯乙')]／停 False/True
  ✅ W6 verify/ 之生產碼⛔ 呼之：[]
  ✅ W7 main／calc 唯增列（具名之換列三）·頂層之相異：相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k967_pool_less', 'k967_pool_out', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']／刪列 3
⇒ 紅 []；rc 0
````

### `#3`　`python3 verify/probes/probe_WG9385_k974.py run <repo>`（`rc 0`·`stderr` `0` B·`359.8` s）

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

### `#62`　`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`（`rc 0`·`stderr` `0` B·`3.5` s）

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

### `#63`　`python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`（`rc 0`·`stderr` `0` B·`3.0` s）

````text
  ✅ X1 adj_intake 呼叫 k967_rank（呼叫 1）
  ✅ X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise（[]）
  ✅ X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']）
  ✅ X4 adj_intake 內⛔ 案件字面（[]）
  ✅ X5 生產碼 app.py 以外之 33 檔對基準相異 0（相異 []）
⇒ 紅 []；rc 0
````

### `#64`　`python3 verify/probes/probe_WG9387_k961h.py run <repo>`（`rc 0`·`stderr` `0` B·`281.5` s）

````text
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 92.46｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R3｜據 R2 27.55、R3 28.34｜外部錨 R3
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 88.63｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R2｜據 R2 27.55、R3 24.88｜外部錨 R2
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
⇒ 紅 []；rc 0
````

### `#65`　`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

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

### `#66`　`python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`（`rc 0`·`stderr` `0` B·`2.0` s）

````text
── 接線（工作樹之 app.py 對基準 fd88f64）──
  ✅ X1 四停機之字樣皆去（殘 []）
  ✅ X2 `_recv_of(b, y)` 之形與其 5 呼叫皆二引數
  ✅ X3 頂層之相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X4 ⛔ 案件字面（[]）
  ✅ X5 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#69`　`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#70`　`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`（`rc 0`·`stderr` `0` B·`119.4` s）

````text
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 11（基準之帶號 10·k980_acq_check 1·end_block_apply 0）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'main', 'select_corner_lots_both_sides_v12']／不合 ['end_block_merge_run：刪列非 raise RuntimeError：[\'      建地之片之他街廓之候選依五級與深度再排·見其 docstring）。"""\', \'    _dup = {p: tg for p, tg in _cand_of.items() if len(tg) >= 2}\']']）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
````

### `#71`　`python3 verify/probes/probe_WG9389_trialstop.py run <repo>`（`rc 0`·`stderr` `0` B·`369.7` s）

````text
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
````

### `#72`　`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#73`　`python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302`（`rc 0`·`stderr` `0` B·`2.1` s）

````text
── 接線（工作樹之 app.py 對基準 2aa6302）──
  ✅ X1 舊停機之字樣去之（殘 0）、還原之字樣去之（{'回原狀': 0, '還原後仍出現': 0}）、鎖定之查之字樣 3（期 ≥ 1）
  ✅ X2 頂層之相異 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'f3_screen_stepg_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X3 ⛔ 案件字面（[]）
  ✅ X4 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#74`　`python3 verify/probes/probe_WG9390_k961r.py run <repo>`（`rc 0`·`stderr` `0` B·`282.0` s）

````text
  ✅ R1@3.5：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 1·回原狀之列 0·其檢核 0·段三之成者 3·G 值列 35）
  ✅ R1@0.0：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 0·回原狀之列 0·其檢核 0·段三之成者 0·G 值列 36）
  ✅ R0 諸退縮之段三之成者之和 3（[3, 0]·期 ≥ 1·其查已行）
⇒ 紅 []；rc 0
````

### `#75`　`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#76`　`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`（`rc 0`·`stderr` `0` B·`34.0` s）

````text
── 接線（工作樹對基準 a8657c4）──
  ✅ W1 _build_corner_range_v3 之呼叫 4（期 ≥ 4）皆傳 min_build_area：皆傳
  ✅ W2 諸呼叫之數 [('end_block_side_geom', 1), ('end_block_host', 2), ('_place_pool_parcels', 2)]（期 ≥ 1、≥ 2、≥ 2）皆傳 min_build_area：皆傳
  ✅ W3 末端帶之單一真相源 {'_place_pool_parcels→_end_region_R': 1, '_place_pool_parcels→_end_band': 0, '_end_region_R→end_block_band_width': 1, 'end_block_band_width 之呼叫（全檔）': 1}（期 1、0、1、1）
  ✅ W4 min_build_area 之值皆為 k980_mba（呼叫 8·期 ≥ 8·不合 []）、v12 之 _mba_pk 之賦值 True、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（4／基準 4）、k980_mba 之分區之引數為字面者 []（期無）
  ✅ W5 k980_range_touch_check 之呼叫 [('select_corner_lots_both_sides_v12', 1), ('f3_screen_stepg_run', 1), ('stepg:_run_step_g_impl', 1)]·app.py 全檔 2（期各 1·app.py 全 2）、其範圍之名齊全 [True, True, True]（期三真）
  ✅ W6 頂層之名之增 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'end_block_trial_G', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']（期 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']）、減 []
  ✅ W7 新增或改之頂層節點（26）內新增之案件字面 []
  ✅ W8 逐層照傳 min_build_area 皆照傳
  ✅ W9 引擎經 ns 取之新名 ['k980_mba', 'k980_range_touch_check'] ⊆ _WF_NS_NAMES（漏 []）
⇒ 紅 []；rc 0
````

### `#77`　`python3 verify/probes/probe_WG9391_k980x.py run <repo>`（`rc 0`·`stderr` `0` B·`561.2` s）

````text
  ✅ R1@3.5 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@3.5 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}·不合 []）
  ✅ R1@0.0 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@0.0 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 124.94, 'R2': 164.49, 'R3': 163.8, 'R4': 126.08, 'R5': 177.54, 'R6': 262.28}·不合 []）
⇒ 紅 []；rc 0
````

### `#78`　`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`（`rc 0`·`stderr` `0` B·`5.3` s）

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

### `#79`　`python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd`（`rc 0`·`stderr` `0` B·`4.4` s）

````text
  ✅ W1 _solve_G_one 之 solve_G_binary 以 K980_G_TOL／K980_G_MAX_ITER（呼叫 1·全檔 1）
  ✅ W2 取得之宗之自我檢查之四處（[('app.py', 4), ('verify/stepg_pipeline.py', 4)]）
  ✅ W3 end_block_host 之評選經 end_block_trial_G（1）·solve_one 之直呼 0
  ✅ W4 引擎經 ns 取之新名 ['end_block_trial_G', 'k980_acq_check'] ⊆ _WF_NS_NAMES（漏 []）
  ✅ W5 頂層之名之增 ['K980_G_MAX_ITER', 'K980_G_TOL', 'end_block_trial_G', 'k980_acq_check']·減 []
  ✅ W6 k980_acq_check 經 k6_program_stop 立 GB-206 之停機
  ✅ W7 新增或改之頂層節點（18）內新增之案件字面 []
  ✅ W8 _corner_first_lot_G 之 _solve_G_one 以 is_corner=True、w0_start=0.0（呼叫 1）
⇒ 紅 []；rc 0
````

### `#80`　`python3 verify/probes/probe_WG9392_k980g.py run <repo>`（`rc 1`·`stderr` `0` B·`279.7` s）

````text
  ✅ R1@3.5 自我檢查 567 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@3.5 本案之錨（KL 05:22 所核之甲）不合 []
  ✅ R1@0.0 自我檢查 432 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  🔴 R2@0.0 本案之錨（KL 05:22 所核之甲）不合 [('R3-抵費地', 1651.4, 1651.39)]
⇒ 紅 ['R2@0.0']；rc 1
````

### `#81`　`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.4` s）

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

### `#82`　`python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415`（`rc 0`·`stderr` `0` B·`4.0` s）

````text
  ✅ W1 end_block_side_geom 之 'gate': False 之回傳 0
  ✅ W2 _place_pool_parcels 之「_unfront 之判 ⇒ continue」0·引 END_BLOCK_UNFRONT_EPS True·寫死 1e-3 0
  ✅ W3 _end_region_R／end_block_band_width 之「frag_poly 空」之停機 []
  ✅ W4 end_block_apply 之 'gate' 之字面 0
  ✅ W5 頂層之名之增 []·減 []·相異之節點 ['_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_merge_run', 'end_block_side_geom', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run']
  ✅ W6 新增或改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
  ✅ W8 END_BLOCK_UNFRONT_EPS ＝ 0.001
  ✅ W9 end_block_apply 之 `raise k6_program_stop(…GB-207…)` 0（期 0·W-G.9-395 去之）
⇒ 紅 []；rc 0
````

### `#83`　`python3 verify/probes/probe_WG9393_endall.py run <repo>`（`rc 0`·`stderr` `0` B·`285.6` s）

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

### `#85`　`python3 verify/probes/probe_WG9394_k9615.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#86`　`python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283`（`rc 0`·`stderr` `0` B·`4.0` s）

````text
  ✅ W1 頂層之名之增 []·減 []·相異之節點 ['end_block_apply', 'end_block_merge_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run']
  ✅ W2 k6_trial_raise_since 內之號之字面 ['GB-205']
  ✅ W3 _noaff 之二試算之間之 mark 與「新登記 ⇒ return False」（_noaff 有）
  ✅ W4 end_block_merge_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W8 k953_manual_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W5 k929_6_fixpoint 之 `raise k6_program_stop(…GB-205…)` 1（期 1）·對基準⛔ 變 True
  ✅ W6 所改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
⇒ 紅 []；rc 0
````

### `#87`　`python3 verify/probes/probe_WG9394_k9615.py run <repo>`（`rc 0`·`stderr` `0` B·`287.0` s）

````text
  ✅ R1@3.5 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@3.5 受併宗 25·最後之配地⛔ 保留者 []
  ✅ R1@0.0 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@0.0 受併宗 26·最後之配地⛔ 保留者 []
⇒ 紅 []；rc 0
````

### `#88`　`python3 verify/probes/probe_WG9395_k960.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

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
  ✅ V1 順序相反 ⇒ 互相等待 ⇒ 序鍵（G 之和 戊 81 ＞ 丁 63）⇒ 戊先：戊得 E、F 強制
  ✅ V2 G 之和（戊 72 ＞ 丁 63）與最大之一片（丁 50 ＞ 戊 36）異 ⇒ 依和：戊先
  ✅ V3 G 之和相等（72）⇒ 重劃前面積之和大者（戊 72 ＞ 丁 62·道路片⛔ 計）先：戊得 E、丁得 F
  ✅ V4 G 之和與重劃前面積之和皆相等 ⇒ 最小之暫編地號小者（D1(1)）先：丁得 E、戊得 F
  ✅ V5 三位地主互相等待成環（G 之和 丁 40／戊 60／己 50）⇒ 戊先、其餘依原位次（己、丁）
  ✅ V6 換名（街廓名之序反之·地號改名）⇒ V1 之結果除名稱外同（逐列之集·定案之端·皆未達）
  ✅ V7 互相等待而先處理者（丁·G 之和 80 ＞ 戊 72）在 F 端之前尚有第三人庚 ⇒ 庚照原位次先試而得 F；丁之競合消滅、丁得 E
  ✅ V8 環成即處理：V1 之環成於 F 端之末列，其後之他街廓之列（T）於其處理之後
  ✅ V9 夥伴之列已被延後過（E 戊己丁·F 丁己戊·G 戊 60／己 50／丁 40）⇒ 依其現位而退、⛔ 無限迴圈
  ✅ V10 二首列退至同一夥伴之列之後而退之先後與原位次相反（E 己丁戊·F 丁戊己）⇒ 依原位次（J1 先於 D1）
  ✅ V11 退至已被延後之夥伴之列（J1）之緊後（E 丁己辛戊·F 戊辛己丁·G 戊 80／己 70／丁 60／辛 50）⇒ D1 先於 K1
  ✅ V13 被延後者之夥伴之列其後自身又被延後（E 己辛戊丁·F 戊己丁辛·G 丁 90／辛 50／戊 30／己 20）⇒ 己之 J1 隨戊之 U1 而移
  ✅ V12 換名與換端：V11 之街廓改名（A7、B2·序同）、地號改名、二端皆為右端 ⇒ 除名稱外同 V11
⇒ 紅 []；rc 0
````

### `#89`　`python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4`（`rc 0`·`stderr` `0` B·`7.9` s）

````text
  ✅ W1 end_block_apply 內⛔ 有 GB-207 之字面、⛔ 有 k6_program_stop 之呼叫
  ✅ W2 end_block_merge_run：⛔ 有「同時跨占二以上末端塊」「屬二以上之競合」之停機；仍有「三個以上之末端塊」之停機
  ✅ W3 _k950_rows：⛔ 有「屬二以上之競合」之停機、仍有「列數 ≠ 2」之停機
  ✅ W4 頂層之名之增減 []（期 []）；頂層節點之相異 ['end_block_apply', 'end_block_merge_run', 'k6b_stage3_run']（期 ['end_block_apply', 'end_block_merge_run', 'k6b_stage3_run']）
  ✅ W5 所改之三節點內新增案件字面 []（期 []）
  ✅ W6 verify/ 頂層之 *.py 對基準相異 []（期 []）
⇒ 紅 []；rc 0
````

### `#90`　`python3 verify/probes/probe_WG9395_k960.py run <repo>`（`rc 0`·`stderr` `0` B·`273.7` s）

````text
  ✅ R1@3.5 觸發之端 4（期 4）、有當選 4（期 4）、「歸他端」之列 []（期 []）、err None
  ✅ R2@3.5 合併再試之標的 []（期 []）、競合 None（期 無）
  ✅ R1@0.0 觸發之端 4（期 4）、有當選 4（期 4）、「歸他端」之列 []（期 []）、err None
  ✅ R2@0.0 合併再試之標的 []（期 []）、競合 None（期 無）
⇒ 紅 []；rc 0
````

### `#92`　`python3 verify/probes/probe_WG9398_rw25.py selftest <repo>`（`rc 1`·`stderr` `0` B·`1.6` s）

````text
  🔴 T1 格點 171（1.0〜18.0 m 每 0.1 m）＝ 附表 25
       得 (155, [(10, 17.4), (11, 18.099999999999998), (13, 19.5)])
       期 (0, [])
  🔴 T2 格間 170 × 3 處 ＝ 二端之線性內插（公分以下用內插法）
       得 (492, [(1.025, 17.575, 17.54), (1.05, 17.75, 17.72), (1.075, 17.924999999999997, 17.9)])
       期 (0, [])
  🔴 T3 請示表：5.30 ⇒ 45.85、5.35 ⇒ 46.15、7.00 ⇒ 55.69
       得 (False, False, False)
       期 (True, True, True)
  🔴 T4 起點 0 與 0〜1 m（自 (0, 0) 至 (1.0, 17.36) 線性）
       得 (0.0, 0.0, 0.0, False, False, True)
       期 (0.0, 0.0, 0.0, True, True, True)
  🔴 T5 飽和：≥ 18 m ＝ 100；17.95 ⇒ 99.875
       得 (100.0, 100.0, 100.0, 100.0, False, True)
       期 (100.0, 100.0, 100.0, 100.0, True, True)
  🔴 T6 格點之浮點之鄰（5.3 ± 1e-12、0.1×53、2.7＋2.6）⇒ 45.85
       得 (False, False, False, False)
       期 (True, True, True, True)
  ✅ T7 0〜18.5 m 每 0.0007 m：不減、相鄰之差 ≤ 0.02
  🔴 T8 累積差額之鏈 0→4.2→9.7→13.05→18.3 與倒退
       得 ((False, False, False, False), True, 0.0)
       期 ((True, True, True, True), True, 0.0)
  🔴 T9 玩具街廓之街角第 1、2 宗（左右 × 二座標系 × 二 a）＝ HB 之自解；舊表之自解至少一異；自解距半分 ≥ 0.001
       得 (16, [(0, 48.89, 48.87), (3, 40.16, 40.14), (4, 48.89, 48.87), (7, 40.16, 40.14), (8, 48.89, 48.87), (11, 40.16, 40.14), (12, 48.89, 48.87), (15, 40.16, 40.14)], True, True)
       期 (16, [], True, True)
  ℹ️ T9 之解（HB）[48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14]
  ℹ️ T9 之解（舊表）[48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16]
  ✅ P0 判式自驗 9／9
⇒ 紅 ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T8', 'T9']；rc 1
````

### `#93`　`python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf`（`rc 1`·`stderr` `0` B·`2.6` s）

````text
  🔴 X1 頂層之名之增 []·減 []·相異之節點 []
  🔴 X2 RW_TABLE_25 ＝ 17 × 10 之字面而逐格 ＝ 附表 25（缺）
  🔴 X3 rw_from_width 讀 RW_TABLE_25／RW_SATURATION_WIDTH_M·其內表之值之數之常數 [17.4, 24.4, 31.3, 37.8, 44.0]
  ✅ X4 rw_increment、RW_SATURATION_WIDTH_M 之節點⛔ 變
  🔴 X5 RW_TABLE_25 以外之表之數之串（生產碼 34 檔）[('app.py', 6141, 19)]
  ✅ X6 新增或改之頂層節點內新增之案件字面 []
  ✅ X7 verify/ 頂層之 *.py 對基準之相異 []
⇒ 紅 ['X1', 'X2', 'X3', 'X5']；rc 1
````

### `#94`　`python3 tests/test_pool_slot.py`（`rc 1`·`stderr` `516` B·`0.7` s）

````text
（空）
````

`stderr`：

````text
Traceback (most recent call last):
  File "/tmp/w/tests/test_pool_slot.py", line 118, in <module>
    n = run_all_cases()
        ^^^^^^^^^^^^^^^
  File "/tmp/w/tests/test_pool_slot.py", line 61, in run_all_cases
    slot, R = _extract()
              ^^^^^^^^^^
  File "/tmp/w/tests/test_pool_slot.py", line 49, in _extract
    raise AssertionError(f"app.py 缺 module 級常數 {sorted(missing_c)}——被改名或刪除？")
AssertionError: app.py 缺 module 級常數 ['RW_TABLE_25']——被改名或刪除？
````

### `#56`　`python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json`（`rc 0`·`stderr` `0` B·`175.4` s）

````text
{"mode": "on", "SB": 3.5, "err": null, "n": 35, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)"}, "R5": {"p1_end": "628-45(1)", "p2_end": null}, "R2": {"p1_end": "628-41(1)", "p2_end": null}, "R3": {"p1_end": null, "p2_end": "628-45(2)"}, "R1": {"p1_end": "628-36(1)", "p2_end": "628(5)"}}, "stage3_log_rows": 19, "sec": 175.1}
````

### `#57`　`python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json`（`rc 0`·`stderr` `0` B·`120.6` s）

````text
{"mode": "on", "SB": 0.0, "err": null, "n": 36, "wins": {"R4": {"p1_end": "628(1)", "p2_end": "628-1(1)"}, "R6": {"p1_end": null, "p2_end": "628-18(1)"}, "R5": {"p1_end": "628-18(2)", "p2_end": null}, "R2": {"p1_end": "628-41(1)", "p2_end": null}, "R3": {"p1_end": null, "p2_end": "628-45(2)"}, "R1": {"p1_end": "628-37(1)", "p2_end": "628(5)"}}, "stage3_log_rows": 0, "sec": 120.3}
````

### `#58`　`python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json`（`rc 0`·`stderr` `0` B·`172.4` s）

````text
【F8 run】退縮 3.5·WV_K929_6 ＝ None（啟用 True）
  R1 配地列中不能建築（非街角第 1 宗）之宗數 ＝ 0
  ✅ R2 不配地紀錄 12 筆之「不配地由」
     R2/left 628-42(1) G 3.82 由 藍影、內接矩形、臨正街寬
     R2/left 628-27(1) G 27.55 由 藍影、內接矩形、臨正街寬
     R2/right 628-50(1) G 147.18 由 內接矩形、臨正街寬
     R2/right 628-51(1) G 146.58 由 內接矩形、臨正街寬
     R2/right 628-52(1) G 71.59 由 內接矩形、臨正街寬
     R3/left 628-46(1) G 72.78 由 內接矩形、臨正街寬
     R3/right 628-42(2) G 92.46 由 內接矩形、臨正街寬
     R3/right 628-27(2) G 28.34 由 藍影、內接矩形、臨正街寬
     R3/right 628-28(1) G 135.94 由 臨正街寬
     R5/left 628-53(2) G 0.99 由 藍影、內接矩形、臨正街寬
     R6/right 628-53(1) G 0.26 由 內接矩形、臨正街寬
     R6/right 628-38(1) G 117.74 由 內接矩形、臨正街寬
     合併 {'輪': 1, '步': '第4步（相連）', '街廓': 'R3', '推進側': 'right', '歸戶': 'G014', '成員': ['628-28(1)', '628-29(1)'], '標的': '628-28(1)', '佔位': '628-28(1)', '併入量(a′)': 114.0, 'a 合計': 228.0, '含原位可配': False, '結果': '入池'}
     合併 {'輪': 1, '步': '第1步', '街廓': 'R6', '推進側': 'left', '歸戶': 'G017', '成員': ['628-21(1)', '628-22(1)', '628-23(1)'], '標的': '628-21(1)', '佔位': '628-23(1)', '併入量(a′)': 372.32, 'a 合計': 723.48, '含原位可配': True, '結果': '留置'}
  ✅ R3 入池閘之回傳（有）與合併紀錄
  逐街廓（配地宗數·ΣG）：R1 4·2041.86；R2 6·2545.31；R3 5·2555.40；R4 2·2510.48；R5 6·2928.77；R6 5·2995.72
⇒ 紅 []；rc 0
````

### `#59`　`python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json`（`rc 0`·`stderr` `0` B·`117.2` s）

````text
【F8 run】退縮 0.0·WV_K929_6 ＝ None（啟用 True）
  R1 配地列中不能建築（非街角第 1 宗）之宗數 ＝ 0
  ✅ R2 不配地紀錄 12 筆之「不配地由」
     R2/left 628-42(1) G 3.82 由 藍影、內接矩形、臨正街寬
     R2/left 628-27(1) G 27.55 由 藍影、內接矩形、臨正街寬
     R2/right 628-50(1) G 147.18 由 內接矩形、臨正街寬
     R2/right 628-51(1) G 146.58 由 內接矩形、臨正街寬
     R2/right 628-52(1) G 71.59 由 內接矩形、臨正街寬
     R3/left 628-46(1) G 72.78 由 內接矩形、臨正街寬
     R3/right 628-42(2) G 88.63 由 內接矩形、臨正街寬
     R3/right 628-27(2) G 24.88 由 藍影、內接矩形、臨正街寬
     R3/right 628-28(1) G 130.42 由 臨正街寬
     R5/left 628-53(2) G 0.99 由 藍影、內接矩形、臨正街寬
     R6/right 628-53(1) G 0.26 由 內接矩形、臨正街寬
     R6/right 628-38(1) G 117.74 由 內接矩形、臨正街寬
     合併 {'輪': 1, '步': '第4步（相連）', '街廓': 'R3', '推進側': 'right', '歸戶': 'G014', '成員': ['628-28(1)', '628-29(1)'], '標的': '628-28(1)', '佔位': '628-28(1)', '併入量(a′)': 114.0, 'a 合計': 228.0, '含原位可配': False, '結果': '入池'}
     合併 {'輪': 1, '步': '第1步', '街廓': 'R6', '推進側': 'left', '歸戶': 'G017', '成員': ['628-21(1)', '628-22(1)', '628-23(1)'], '標的': '628-21(1)', '佔位': '628-23(1)', '併入量(a′)': 372.32, 'a 合計': 723.48, '含原位可配': True, '結果': '留置'}
  ✅ R3 入池閘之回傳（有）與合併紀錄
  逐街廓（配地宗數·ΣG）：R1 4·2041.86；R2 6·2545.31；R3 6·2555.40；R4 2·2510.48；R5 6·2928.75；R6 5·2995.72
⇒ 紅 []；rc 0
````

### `#60`　`python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json`（`rc 0`·`stderr` `0` B·`355.5` s）

````text
【F4 parity】態 07d12028d99b3a178c2a87edaea0b70ae8a754ac·退縮 3.5·WV_K6B_STAGE3=on·擾動 False
  ✅ 街角選位 session 鍵 f3L_corner_winners
  ✅ 街角選位 session 鍵 f3L_forced_offset
  ✅ 街角選位 session 鍵 f3_corner_winners
  ✅ 街角選位 session 鍵 f3_current_pk_block
  ✅ 街角選位 session 鍵 f3_k6b_dual_side_assign
  ✅ 街角選位 session 鍵 f3_k6b_stage1_locked_by_block
  ✅ 街角選位 session 鍵 f3_k6b_stage1_locks
  ✅ 街角選位 session 鍵 f3_k6b_stage2_order
  ✅ 街角選位 session 鍵 f3_pk_alloc_depth
  ✅ 街角選位 session 鍵 f3_pk_legal_min_width
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
````

### `#61`　`python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json`（`rc 0`·`stderr` `0` B·`248.3` s）

````text
【F4 parity】態 07d12028d99b3a178c2a87edaea0b70ae8a754ac·退縮 0.0·WV_K6B_STAGE3=on·擾動 False
  ✅ 街角選位 session 鍵 f3L_corner_winners
  ✅ 街角選位 session 鍵 f3L_forced_offset
  ✅ 街角選位 session 鍵 f3_corner_winners
  ✅ 街角選位 session 鍵 f3_current_pk_block
  ✅ 街角選位 session 鍵 f3_k6b_dual_side_assign
  ✅ 街角選位 session 鍵 f3_k6b_stage1_locked_by_block
  ✅ 街角選位 session 鍵 f3_k6b_stage1_locks
  ✅ 街角選位 session 鍵 f3_k6b_stage2_order
  ✅ 街角選位 session 鍵 f3_pk_alloc_depth
  ✅ 街角選位 session 鍵 f3_pk_legal_min_width
  ✅ 段三 session 鍵 f3_k6b_stage3_log（0 列）
  ✅ 段三 session 鍵 f3_k6b_stage3_order_used（0 列）
  ✅ 合併再試 session 鍵 f3_end_block_merge（harness {'退縮': 0.0, '標的': [], '皆未達': {}}）
  ✅ 合併再試 session 鍵 f3_end_block_merge_log（harness []）
  ✅ 手冊先行 session 鍵 f3_k953_log（46 列）
  ✅ 第一趟 session 鍵 f3_adj4_log（1 列）
  ✅ 段三後 temp 之暫編地號與「段三併出」逐元素依序（126／126）
  ✅ 段三後 temp 之面積四欄與所屬街廓逐元素
  ✅ 段三後 build 之暫編地號依序（46／46）
  ✅ 段三後 build ⊂ temp（同物件）
  ✅ K917_DROPPED（段三畢·與 harness 同）
  ✅ session 之回復：段三前已有之非街角選位鍵值未變、未新生他鍵
  ✅ 配地列（harness 36／畫面 35；不符格 0）
  ℹ️ Z（一側獨有之零面積池列）＝ [('harness', 'R1-抵費地-2')]
⇒ rc 0（不符 0 項）
````

## 附錄丑　`V-1` 之諸呼叫之 `stdout` 之全文（次趟 `c35d32a`·逐呼叫）

### `#4`　`python3 verify/probes/probe_WG9363_k953.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.8` s）

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

### `#5`　`python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954`（`rc 0`·`stderr` `0` B·`33.6` s）

````text
  ✅ W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·K953_ENV）（k953_manual_run True／其餘 True）
  ✅ W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True）
  ✅ W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位
  ✅ W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後
  ✅ W5 新碼⛔ 案件字面（[]）
  ✅ W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）（相異 []）
  ✅ W7 app.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K953_ENV', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_alloc_summary', 'k953_enabled', 'k953_manual_run', 'k953_units_of', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W7 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W8 app.py：既有量測器之錨（604）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·406）仍恰一（錨之異 []；函式名之異 []）
  ✅ W8 verify/selection_pipeline.py：既有量測器之錨（184）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·18）仍恰一（錨之異 []；函式名之異 []）
  ✅ W9 五級之接線（三函式之 blk5·末端塊合併再試傳之·畫面與 harness 之六入口·二回呼之 blk5·二新函式）（不合 []）
⇒ 紅 []；rc 0
````

### `#17`　`python3 verify/probes/probe_WG9363_k953.py run <repo>`（`rc 0`·`stderr` `0` B·`372.0` s）

````text
  ✅ R1@3.5：手冊先行之紀錄 34 列 ＝ 本器所載 True
  ✅ R2@3.5：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@3.5：配地 28 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -2934.52／ΣG 之變 2934.51（和 ≤ 0.1）True
  ✅ R4@3.5：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@3.5：手冊先行之紀錄之「依據」（類 a·9 列）＝ 本器所載 True
  ✅ R6@3.5：手冊先行之再試之列 3 列 ＝ 本器所載 True
  ✅ R1@0.0：手冊先行之紀錄 43 列 ＝ 本器所載 True
  ✅ R2@0.0：街角第 1 宗 ＝ 旗標 off 之實跑 True（8 宗）
  ✅ R3@0.0：配地 29 宗之街廓·推進側·G 與抵費地 6 街廓 ＝ 本器所載；Σ抵費地之變 -3663.87／ΣG 之變 3663.87（和 ≤ 0.1）True
  ✅ R4@0.0：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 True
  ✅ R5@0.0：手冊先行之紀錄之「依據」（類 a·10 列）＝ 本器所載 True
  ✅ R6@0.0：手冊先行之再試之列 3 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

### `#6`　`python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4`（`rc 0`·`stderr` `0` B·`33.7` s）

````text
  ✅ W1 模組層之新名與簽名（app.py 九函式·二常數；selection_pipeline.run_adj4）（簽名 True／kw True／常數 True／harness True）
  ✅ W2 harness：run_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 run_step_g 試算、⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_adj4、於 run_k953 之後、slices ＝ 其輸入 temp_parcels、其出 ＝ 回傳之末二值、其後⛔ 再呼叫 run_corner_pk（入口 True／序 True／承接 True／回傳 True）
  ✅ W3 畫面：f3_screen_adj4 恰一處呼叫 adj4_pass1_run 與 adj4_plan、三旗標皆呼、以 f3_screen_stepg_run 試算、⛔ 呼叫街角選位；f3_screen_k6b_stage3 恰一處呼叫 f3_screen_adj4、於 f3_screen_k953 之後、slices ＝ temp0（＝ pk_kwargs['temp_parcels']）（入口 True／序 True）
  ✅ W4 新碼⛔ 案件字面（[]）
  ✅ W5 app.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['ADJ4_ENV', 'ADJ4_IDENT_UNUSED', 'K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_depth_of', 'adj4_enabled', 'adj4_pass1_run', 'adj4_plan', 'adj4_possible', 'adj4_subject_units', 'adj4_subjects', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ W5 verify/selection_pipeline.py 之頂層節點對基準相異者 ⊆ 本單之許（其餘既有函式一字未動）（相異 ['_k6b_callbacks', 'build_build_parcels', 'k6b_stage3_pool_temp', 'run_adj4', 'run_corner_pk_k6b', 'run_end_block_merge', 'run_k953']；逾 []）
  ✅ W6 本單所改之三函式（k953_manual_run／f3_screen_k6b_stage3／run_corner_pk_k6b）對基準唯增列（⛔ 改、⛔ 刪既有一列·`W6_REPL` 之列除外）（f3_screen_k6b_stage3 True·增段 1；run_corner_pk_k6b True·增段 2）
  ✅ W7 app.py：既有量測器之錨（606）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·446）仍恰一（錨之異 []；函式名之異 []）
  ✅ W7 verify/selection_pipeline.py：既有量測器之錨（185）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·20）仍恰一（錨之異 []；函式名之異 []）
⇒ 紅 []；rc 0
````

### `#13`　`python3 verify/probes/probe_WG9367_adj4.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#18`　`python3 verify/probes/probe_WG9367_adj4.py run <repo>`（`rc 0`·`stderr` `0` B·`529.9` s）

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

### `#7`　`python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa`（`rc 0`·`stderr` `0` B·`2.7` s）

````text
  ✅ X1 生產碼 34 檔對基準相異者 ⊆ {app.py, verify/selection_pipeline.py}（相異 ['app.py', 'verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']）
  ✅ X2 app.py 之頂層節點對基準相異者 ⊆ {adj4_pass1_run, k953_manual_run} ∪ 本單之許（相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K966_CLASSES', 'K966_GRID', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_k929_6_screen_gate', '_place_pool_parcels', '_solve_G_one', 'adj4_pass1_run', 'adj4_trial_state', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_end_block_merge', 'f3_screen_k6b_stage3', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k965_part_split', 'k966_block_merge', 'k967_pool_less', 'k967_pool_out', 'k967_pre_area', 'k967_rank', 'k971_blk5', 'k971_key5', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']；逾 []）
  ✅ X3 _bpre_a4：定義 1 見、呼叫 1 見、其位 ＝ 與 k966_block_merge 同 for 之內且先之 True
  ✅ X4 verify/selection_pipeline.py 對基準之差（本單所改之二函式之段除外）＝ run_adj4 之二列之 .get 化（差之列 4）
  ✅ X5 三停機訊息（K-9-57 ⑧）之模板：S238 1 見、R-10′ 1 見、S219 1 見；含 TOK 而⛔ 屬模板之 raise []
⇒ 紅 []；rc 0
````

### `#19`　`python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>`（`rc 0`·`stderr` `0` B·`7.3` s）

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

### `#20`　`python3 verify/probes/probe_WG9373_k966.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

````text
── K-9-66／K-9-67／K-9-68 之各支 ──
  ✅ A1 KL 例一（街廓 B 能再容 130）：建地全部一次不過 ⇒ 按比例 52／43.33／34.67（130 × 60／150 等）；道路未試
  ✅ A2 KL 例二（能再容 170）：建地 150 全入；剩 20 按 30：20：10 分給道路 10／6.67／3.33
  ✅ A3 一次全部即過 ⇒ 全入、唯整體一步
  ✅ A4 唯一類（道路 30／20·容 25）⇒ 整體即該類之全部（⛔ 重試全部）⇒ 按比例 15／10；全量之試恰一次
  ✅ A5 格 ＝ 該類之合計每 0.01 ㎡：容 60.005 ⇒ 60.00；容 59.999 ⇒ 59.99
  ✅ A6 建地、道路皆全入；公設地 200 唯容 10 ⇒ 0.05
  ✅ A7 建地之比例步亦全不容 ⇒ 未成（比例 0）、其後之類未試、⛔ 併入
  ✅ A8 類非三類之一 ⇒ 停機；來源量 ≤ 0 ⇒ 停機
  ✅ A9 回傳之態 ＝ 末次通過之試所回之物件；全不過 ⇒ 輸入之態（同一物件）
  ✅ B1 k967_rank：應分配面積以 0.01 ㎡ 比（100.004 ＝ 100.00·100.006 ＝ 100.01）；同 ⇒ 重劃前面積大者先
  ✅ B2 k967_rank：再同（重劃前面積 69.996 ＝ 70.00）⇒ 暫編地號小者先
  ✅ B3 k967_pre_area：成員之分攤登記面積之和；成員缺 ⇒ 自身；取不到 ⇒ 停機
  ✅ B4 k967_pool_out：單元自身之片取入池閘部分併出之和、他成員之片取入池閘成員部分併出［片］之和；無帳者（缺或空）⛔ 列
  ✅ B5 k967_pool_out：同一片之帳見於二處（二單元·或自身與成員）⇒ 停機；量 ≤ 0 ⇒ 停機
  ✅ B6 k967_pool_less：表減其量（新表·原表⛔ 動）；None／空 ⇒ 同值；表外之片 ⇒ 停機；非 dict ⇒ 停機
  ✅ C1 入池閘之代表宗：G 並列（60.00）⇒ 重劃前面積大者 Y2（100 ＞ 80）
  ✅ C2 G 差 0.004（0.01 ㎡ 為同）⇒ 並列 ⇒ 重劃前面積大者 Y2
  ✅ C3 G 差 0.006（60.01 ＞ 60.00）⇒ G 大者 Y1
  ✅ C4 G 與重劃前面積皆同 ⇒ 暫編地號小者 Y1
  ✅ T1 手冊先行·三位地主之建地同到 BB（容 130）⇒ K-9-66 之列、按比例 52／43.33／34.67；甲之剩下 8 依距離併入 A2；乙丙之剩下入合併單位；部分併出者留 build（面積_m2 減其量·段三部分併出·⛔ 段三餘量）
  ✅ T2 手冊先行·K-9-68：甲之 80 第 1 輪全入 BB；乙之 60 第 1 輪試 BC 不過、第 2 輪轉 BB 唯得剩下之 20（⛔ 重分）
  ✅ T3 手冊先行·第 2 輪（K-9-51）二位地主之剩下同到 BD（容 25）⇒ 亦依 K-9-66 按比例 15／10；餘入合併單位
  ✅ T5 手冊先行·第 1 輪之來源量 ＝ 計畫之量 ÷ κ（BB 之 κ ＝ 2）⇒ 比例 0.433333：A1 52／B1 43.33／C1 34.67；甲之剩下 34 全入 A2；帳以來源量計（Y 21.67／Z 17.33）
  ✅ U0 段三後處理·對照：整批即過 ⇒ 二列皆成（⛔ K-9-66 之列）
  ✅ U1 段三後處理·二位地主之公設地同到 B3（剩下能容 50）⇒ K-9-66 之列、按比例 30／20；剩下轉調配
  ✅ U2 段三後處理·第 2 輪二位地主之剩下同到 B5（容 25）⇒ 亦依 K-9-66 按比例 15／10
  ✅ V1 第一趟·二受詞之建地同到 BB（容 50）⇒ K-9-66 之列、按比例 30／20；剩下留於合併單位；部分併出者留 build
  ✅ V2 第一趟·K-9-68：g1 之 80 第 1 輪全入 BB；g2 之 60 第 1 輪於 BC 不過、第 2 輪至 BB 唯得剩下之 20（⛔ 重分）
  ✅ W1 調配之輸入·部分併出之建地（其單元不配地）⇒ 建築街廓內不能分配：原有面積 ＝ 50 × 30／50 ＝ 30、已併出 20 計入原位次配地、應分配面積 ＝ 該趟之 G（原位·剩下之面積）；守恆
  ✅ W2 調配之輸入·部分併出之建地（其單元配地）⇒ 原位次配地（配地街廓含受併宗之街廓）；守恆
  ✅ W3 公設地調配之 temp：部分併出之建地（⛔ 段三餘量）原物件入之；全數併出之建地去之；餘同一物件
── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──
  ✅ P0 逐項擾動恰該項紅 31／31
⇒ 紅 []；rc 0
````

### `#21`　`python3 verify/probes/probe_WG9373_k966.py wiring <repo>`（`rc 0`·`stderr` `0` B·`2.3` s）

````text
  ✅ Y1 模組層之新名與簽名（簽名之異 []；K966_CLASSES ('建地', '道路', '公設地')；K966_GRID 0.01）
  ✅ Y2 k966_block_merge 之呼叫恰在四處各一（三處 ＋ 入池閘·W-G.9-375）（四處 {'k953_manual_run': 1, 'k6b_stage3_run': 1, 'adj4_pass1_run': 1, 'k929_6_fixpoint': 1}；全檔 4）
  ✅ Y3 k967_rank 之呼叫（入池閘 ≥ 1·手冊先行 ≥ 3·段三 ≥ 1·第一趟 ≥ 1）（{'k929_6_fixpoint': 2, 'k953_manual_run': 4, 'k6b_stage3_run': 3, 'adj4_pass1_run': 1}）
  ✅ Y4 新碼⛔ 案件字面（[]）
  ✅ Y5 已去之巢狀 def ⛔ 見（[]）
  ✅ Y6 擇宗⛔ 以「並列 ⇒ 停機」（[]）
  ✅ Y7 三處之 k966_block_merge 皆以 state 為前態、以其回傳之態承接（state, … ＝ …(state, …)）（{'k953_manual_run': [True], 'k6b_stage3_run': [True], 'adj4_pass1_run': [True]}）
  ✅ Y8 五處之試算（段三·手冊先行之 harness 與畫面、第一趟之共用）皆以同一 build 回 members 與 pool_out（k967_pool_out 之呼叫直書為 return 之鍵 pool_out 之值）（k953_units_of 之呼叫 [('app.py', 'adj4_trial_state', True), ('app.py', '_trial953s', True), ('app.py', 'alloc_state', True), ('selection_pipeline.py', '_trial_k', True), ('selection_pipeline.py', 'alloc_state', True)]；k967_pool_out 之呼叫 5）
  ✅ Y9 調配之輸入之 build ＝ 末次入池閘之出：SS_ADJ_BUILD_FINAL 恰一寫於 f3_screen_stepg_run 之入池閘之後；畫面與 harness 之段三（含手冊先行·第一趟）皆先於 step G（寫 [(23147, 'f3_screen_stepg_run')]·入池閘 [21607]；畫面 段三 [29608] ＜ step G [29985]；harness run_corner_pk_k6b [611] ＜ run_step_g 692（build ＝ s3_by_tag[tag]['build']））
⇒ 紅 []；rc 0
````

### `#22`　`python3 verify/probes/probe_WG9373_k966.py mutate <repo>`（`rc 0`·`stderr` `0` B·`61.0` s）

````text
  ✅ N00 —·基準（⛔ 突變）：錨 1 見；所指 []；紅 []
  ✅ N01 K-9-66 ①·整體成而⛔ 回：錨 1 見；所指 ['F27:A3']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K2', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K9', 'F23:K14', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K37', 'F23:K38', 'F23:K39', 'F23:K40', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K27', 'F24:K3', 'F24:K4', 'F24:K8', 'F27:A3', 'F27:T1', 'F27:T2', 'F27:T5', 'F27:V2']
  ✅ N02 K-9-66 ②·唯一類者亦以該類之全量再試：錨 1 見；所指 ['F27:A4']；紅 ['F27:A4']
  ✅ N03 K-9-66 ②·類之序反之：錨 1 見；所指 ['F27:A2', 'F27:A6']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21', 'F23:K16', 'F23:K20', 'F23:K23', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F27:A1', 'F27:A2', 'F27:A6', 'F27:A7', 'F28:D3', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S4', 'F28:S6']
  ✅ N04 K-9-66 通知 2·格改 0.1：錨 1 見；所指 ['F27:A5']；紅 ['F23:K15', 'F23:K75', 'F24:K24', 'F27:A5']
  ✅ N05 K-9-66 ②·按比例之後仍試次類：錨 1 見；所指 ['F27:A1', 'F27:A7']；紅 ['F24:K24', 'F27:A1', 'F27:A7']
  ✅ N06 K-9-66·回傳輸入之態（⛔ 末次通過之態）：錨 1 見；所指 ['F27:A9']；紅 ['F16:K10', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K20', 'F23:K28', 'F24:K13', 'F24:K23', 'F24:K4', 'F24:K5', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N07 K-9-66 ②·二分法之支反之：錨 1 見；所指 ['F27:A1']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N08 K-9-66·要求之類之停機去之：錨 1 見；所指 ['F27:A8']；紅 ['F27:A8']
  ✅ N09 K-9-66 ②·二分法⛔ 記通過之態：錨 1 見；所指 ['F27:A9']；紅 ['F16:K10', 'F16:K10′', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N10 K-9-66 ②·試之量與所記之量不一：錨 1 見；所指 ['F27:A1']；紅 ['F16:K10', 'F16:K10′', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K20′', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F23:K14', 'F23:K15', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F24:K13', 'F24:K14', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K8', 'F27:A1', 'F27:A2', 'F27:A4', 'F27:A5', 'F27:A6', 'F27:A9', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F27:U1', 'F27:U2', 'F27:V1', 'F27:V2', 'F28:D1', 'F28:D2', 'F28:D3', 'F28:L4', 'F28:L5', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N11 K-9-66 ②·類之全量成而⛔ 承接其態：錨 1 見；所指 ['F27:A2', 'F27:A6']；紅 ['F16:K18', 'F23:K16', 'F23:K20', 'F24:K13', 'F24:K23', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F27:A2', 'F27:A6']
  ✅ N12 K-9-67·去重劃前面積之鍵：錨 1 見；所指 ['F27:C1']；紅 ['F23:K3', 'F23:K51', 'F24:K7', 'F27:C1', 'F27:C2', 'F28:Q1', 'F28:Q2']
  ✅ N13 K-9-67·應分配面積⛔ 以 0.01 ㎡ 量化：錨 1 見；所指 ['F27:C2']；紅 ['F27:C2']
  ✅ N14 K-9-67·重劃前面積之序反之：錨 1 見；所指 ['F27:B1', 'F27:C1']；紅 ['F23:K3', 'F23:K51', 'F24:K7', 'F27:B1', 'F27:C1', 'F27:C2', 'F28:Q1', 'F28:Q2']
  ✅ N15 K-9-67·重劃前面積先於應分配面積：錨 1 見；所指 ['F27:B1']；紅 ['F23:K50', 'F27:B1']
  ✅ N16 K-9-67·成員缺⛔ 取自身：錨 1 見；所指 ['F27:B3']；紅 ['F27:B3']
  ✅ N17 K-9-68·段三：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:U1']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S4', 'F28:S6']
  ✅ N18 K-9-51·段三：第 5 項之候選⛔ 扣已試而未全收之街廓：錨 1 見；所指 ['F27:U2']；紅 ['F16:K17', 'F16:K19', 'F16:K2', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N19 K-9-51·段三：第 5 項之候選之序以 k967_rank 先於距離：錨 1 見；所指 ['F16:K3']；紅 ['F16:K27', 'F16:K3', 'F16:K4', 'F16:K7']
  ✅ N20 K-9-66·段三：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:U1']；紅 ['F27:U1', 'F27:U2']
  ✅ N21 K-9-68·段三：第 5 項之輪之剩下⛔ 減其所併：錨 1 見；所指 ['F16:K2']；紅 ['F16:K10', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K2', 'F16:K21', 'F16:K23', 'F16:K24', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K9']
  ✅ N22 R-17″·段三：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L6']；紅 ['F28:D3', 'F28:L6']
  ✅ N23 R-17″·段三：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L1', 'F28:L6']；紅 ['F28:L1', 'F28:L6']
  ✅ N24 R-17″·段三：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L1']；紅 ['F28:D3', 'F28:L1', 'F28:L6']
  ✅ N25 R-19″·段三：第 5 項之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L6']；紅 ['F28:D3', 'F28:L6']
  ✅ N26 K-9-66·段三：試施之受併宗之量⛔ 乘 κ：錨 1 見；所指 ['F16:K10']；紅 ['F16:K10', 'F16:K10′']
  ✅ N27 K-9-68·段三：第 1 輪⛔ 記已試而未全收之街廓：錨 1 見；所指 ['F27:U2']；紅 ['F16:K17', 'F16:K19', 'F16:K2', 'F16:K21', 'F16:K22', 'F16:K23', 'F16:K26', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N28 R-7 ③·段三：題一 4 之半之片⛔ 入第 5 項之輪：錨 1 見；所指 ['F16:K17']；紅 ['F16:K17', 'F16:K18', 'F16:K19', 'F16:K21']
  ✅ N29 K-9-66·段三：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:U1']；紅 ['F16:K10', 'F16:K10′', 'F16:K13', 'F16:K14', 'F16:K17', 'F16:K18', 'F16:K19', 'F16:K2', 'F16:K20', 'F16:K27', 'F16:K3', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K9', 'F27:U1', 'F28:D3', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N30 R-7 ②·段三步驟 10：第 1 輪之來源量⛔ 除 κ：錨 1 見；所指 ['F16:K10']；紅 ['F16:K10', 'F16:K10′']
  ✅ N31 R-7 ②·段三步驟 10：非建地之片之剩下⛔ 記：錨 1 見；所指 ['F27:U1']；紅 ['F16:K10′', 'F16:K13', 'F16:K14', 'F16:K14′', 'F16:K4', 'F16:K8', 'F27:U1']
  ✅ N32 R-7 ②·段三步驟 10：剩下⛔ 入第 5 項之輪：錨 1 見；所指 ['F27:U2']；紅 ['F16:K10', 'F16:K11', 'F16:K12', 'F16:K13', 'F16:K14', 'F16:K2', 'F16:K22', 'F16:K23', 'F16:K24', 'F16:K25', 'F16:K26', 'F16:K27', 'F16:K28', 'F16:K3', 'F16:K30', 'F16:K31', 'F16:K32', 'F16:K4', 'F16:K5', 'F16:K6', 'F16:K7', 'F16:K8', 'F16:K9', 'F27:U1', 'F27:U2', 'F28:S3', 'F28:S5']
  ✅ N33 K-9-66 R-5 (a)·段三：建地之部分併出⛔ 留 build：錨 1 見；所指 ['F16:K19', 'F16:K7']；紅 ['F16:K19', 'F16:K7', 'F28:D3', 'F28:L1', 'F28:L6', 'F28:S1', 'F28:S2', 'F28:S3', 'F28:S4', 'F28:S5', 'F28:S6']
  ✅ N34 K-9-68·手冊先行：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:T1']；紅 ['F23:K16', 'F23:K20', 'F23:K23', 'F23:K42', 'F23:K65', 'F24:K15', 'F27:T1', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L2', 'F28:L4']
  ✅ N35 K-9-51·手冊先行：候選⛔ 扣已試而未全收之街廓：錨 1 見；所指 ['F27:T2']；紅 ['F23:K14', 'F23:K15', 'F23:K16', 'F23:K23', 'F23:K28', 'F23:K42', 'F23:K61', 'F23:K63', 'F23:K65', 'F23:K67', 'F23:K70', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L2', 'F28:L4']
  ✅ N36 K-9-66·手冊先行：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:T1']；紅 ['F27:T1', 'F27:T3', 'F27:T5']
  ✅ N37 K-9-68·手冊先行：K-9-51 之輪之剩下⛔ 減其所併：錨 1 見；所指 ['F27:T1']；紅 ['F23:K14', 'F23:K28', 'F23:K32', 'F23:K33', 'F23:K34', 'F23:K35', 'F23:K36', 'F23:K42', 'F23:K61', 'F23:K62', 'F23:K63', 'F23:K65', 'F23:K70', 'F23:K71', 'F23:K72', 'F23:K73', 'F23:K75', 'F27:T1', 'F27:T5']
  ✅ N38 R-17″·手冊先行：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L4']；紅 ['F28:D1', 'F28:L4']
  ✅ N39 R-17″·手冊先行：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L4']；紅 ['F28:L4']
  ✅ N40 R-17″·手冊先行：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L2']；紅 ['F28:D1', 'F28:L2', 'F28:L4']
  ✅ N41 R-19″·手冊先行：K-9-51 之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L4']；紅 ['F28:D1', 'F28:L4']
  ✅ N42 K-9-66 R-5·手冊先行：第 1 輪之來源量⛔ 除 κ：錨 1 見；所指 ['F27:T5']；紅 ['F27:T5']
  ✅ N43 R-18″·手冊先行：趟末之前帳取當下之態：錨 1 見；所指 ['F27:T1']；紅 ['F27:T1', 'F27:T3', 'F27:T5']
  ✅ N44 K-9-66·手冊先行：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:T1']；紅 ['F23:K20', 'F23:K28', 'F23:K33', 'F23:K35', 'F23:K36', 'F23:K37', 'F23:K39', 'F23:K40', 'F24:K15', 'F27:T1', 'F27:T2', 'F27:T3', 'F27:T5', 'F28:D1', 'F28:L4']
  ✅ N45 K-9-68·第一趟：一輪之要求⛔ 依受併之街廓分組：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K14', 'F24:K23', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K3', 'F24:K4', 'F24:K5', 'F24:K6', 'F27:V1', 'F28:L3']
  ✅ N46 R-17″·第一趟：趟中之帳同一受併宗⛔ 累加（覆寫）：錨 1 見；所指 ['F28:L5']；紅 ['F28:D2', 'F28:L5']
  ✅ N47 R-17″·第一趟：趟中之帳取輸入之帳 ＋ 最末一次：錨 1 見；所指 ['F28:L5']；紅 ['F28:L5']
  ✅ N48 R-17″·第一趟：趟中之帳⛔ 寫：錨 1 見；所指 ['F28:L3']；紅 ['F28:D2', 'F28:L3', 'F28:L5']
  ✅ N49 R-19″·第一趟：各輪之重劃前面積之表取輸入之態：錨 1 見；所指 ['F28:L5']；紅 ['F28:D2', 'F28:L5']
  ✅ N50 K-9-66·第一趟：K-9-66 之列⛔ 記：錨 1 見；所指 ['F27:V1']；紅 ['F27:V1']
  ✅ N51 K-9-68·第一趟：剩下⛔ 減其所併（記為 0）：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K14', 'F24:K24', 'F24:K25', 'F24:K26', 'F24:K4', 'F24:K5', 'F24:K6', 'F24:K8', 'F27:V1', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N52 K-9-68·第一趟：受詞每輪沿名單⛔ 止於首一有其宗之街廓：錨 1 見；所指 ['F27:V2']；紅 ['F24:K23', 'F24:K3', 'F24:K4', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N53 K-9-66·第一趟：同類之片之序（剩下大者先）反之：錨 1 見；所指 ['F24:K25']；紅 ['F24:K25']
  ✅ N54 K-9-67·第一趟：受併宗之序去 k967_rank：錨 1 見；所指 ['F24:K7']；紅 ['F24:K7', 'F28:D2', 'F28:L5']
  ✅ N55 R-18″·第一趟：趟末之前帳取當下之態：錨 1 見；所指 ['F27:V1']；紅 ['F27:V1', 'F27:V2']
  ✅ N56 K-9-66·第一趟：⛔ 以 k966_block_merge 之回傳之態承接：錨 1 見；所指 ['F27:V1']；紅 ['F24:K13', 'F24:K23', 'F24:K27', 'F24:K3', 'F24:K4', 'F24:K5', 'F27:V1', 'F27:V2', 'F28:D2', 'F28:L5']
  ✅ N57 K-9-66 通知 3·調配之輸入：建地之部分併出之原有面積⛔ 依剩下之比：錨 1 見；所指 ['F27:W1', 'F27:W2']；紅 ['F27:W1', 'F27:W2', 'F28:I1', 'F28:I2', 'F28:I3']
⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0
````

### `#23`　`python3 verify/probes/probe_WG9373_k966.py run <repo>`（`rc 0`·`stderr` `0` B·`313.6` s）

````text
  ✅ R1@3.5：段三後處理 6 列皆成、⛔ K-9-66／第 5 項 True；手冊先行之整批 ['成']、⛔ K-9-66／K-9-51 True；第一趟 1 列皆整體成 True
  ✅ R2@3.5：入池閘之代表宗（街廓, 成員, 標的, 並列之 G, 並列之重劃前面積）[('R3', ['628-28(1)', '628-29(1)'], '628-28(1)', 69.2, 114.0), ('R6', ['628-21(1)', '628-22(1)', '628-23(1)'], '628-21(1)', None, None)]
  ✅ R3@3.5：段三之試算之 members harness ＝ 畫面 True（51 宗）；R3 之單元 ['628-28(1)', '628-29(1)']
  ✅ R1@0.0：段三後處理 0 列皆成、⛔ K-9-66／第 5 項 True；手冊先行之整批 ['成']、⛔ K-9-66／K-9-51 True；第一趟 1 列皆整體成 True
  ✅ R2@0.0：入池閘之代表宗（街廓, 成員, 標的, 並列之 G, 並列之重劃前面積）[('R3', ['628-28(1)', '628-29(1)'], '628-28(1)', 65.76, 114.0), ('R6', ['628-21(1)', '628-22(1)', '628-23(1)'], '628-21(1)', None, None)]
  ✅ R3@0.0：段三之試算之 members harness ＝ 畫面 True（52 宗）；R3 之單元 ['628-28(1)', '628-29(1)']
⇒ 紅 []；rc 0
````

### `#14`　`python3 verify/probes/probe_WG9375_k965.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

````text
  ✅ K1 弱弱聯合·大者在前 ⇒ X2 併入 X、於 X 之位；乙照原位
  ✅ K2 弱弱聯合·大者在後 ⇒ X 併入 X2；乙遞補而不配地
  ✅ K3 同街廓先（弱弱聯合）·他街廓之己宗（他地號）⛔ 依手冊併入（K-9-73·改 K-9-64）
  ✅ K4 他街廓之己宗相連（他地號）⇒ 入池閘⛔ 處（K-9-73）
  ✅ K5 合併後反不能配 ⇒ 回原狀、併入原可配之宗之原位（K-9-58 ③）
  ✅ K6 街角第 1 宗⛔ 合併、依手冊併入（K-9-58 ①）
  ✅ K7 跨左右推進 ⇒ 併向應分配面積較大之一側（K-9-58 ②）
  ✅ K8 第 3 步：併入同街廓不相連之已配得之宗（其位）
  ✅ K9 N0-9 之片亦先判同街廓（K-9-73·改 K-9-64 ③）
  ✅ K10 重排後遞補者從第 1 步起處理
  ✅ K11 弱弱聯合之宗其後配不到 ⇒ ⛔ 再弱弱聯合
  ✅ K12 第 3 步併入後反不配地 ⇒ 回原狀
  ✅ K13 經同地主之道路片相連 ⇒ 入池閘⛔ 處（交手冊先行·K-9-73）
  ✅ K14 輸入之單元之成員之形與成員之列（NOTE 5）
  ✅ K15 單元之成員之切片取不到 ⇒ 停機
  ✅ K16 入池閘⛔ 判經道路片之相連 ⇒ 切片未給亦⛔ 停機（K-9-73）
  ✅ K17 檢核之輸入未給 ⇒ 停機
  ✅ K18 調配之輸入：宿主在他街廓 ⇒ 配地街廓 ＝ 宿主之街廓
  ✅ K19 調配之輸入：入池閘之帳之部分併出
  ✅ K20 重劃前面積取輸入之 build 之帳（K-9-67·補令一 R-16′）
  ✅ K21 重劃前面積減入池閘之部分併出（入池閘部分併出·輸入之帳）
  ✅ K22 K-9-58 ③ 二次皆不配地 ⇒ 收斂（⛔ 空轉·⛔ 往他街廓）
  ✅ K23 部分併出之帳隨剩下入單元（調配之輸入⛔ 重計）
  ✅ K24 第 1 步之相連以其自身之地（他街廓併入之片⛔ 計）
  ✅ K25 受併宗最後不配地 ⇒ 已併入者回原狀（K-9-61 ⑤）
  ✅ K26 調配之輸入：受併宗為他單元之成員
  ✅ K27 經同地主之連續道路片相連 ⇒ 入池閘⛔ 處（交手冊先行·K-9-73）
  ✅ K28 部分併入後之剩下⛔ 再試他街廓（續第 3 步起）
  ✅ K29 地主於本街廓已有配得之宗 ⇒ ⛔ 弱弱聯合（K-9-57 ④）
  ✅ K30 N0-9 之片亦依手冊併入街角第 1 宗（K-9-73·K-9-58 ①）
  ✅ K31 第 3 步：街角第 1 宗依手冊併入
  ✅ K32 回原狀後各併入原可配之宗中應分配面積最大者（K-9-76 ②·⛔ 相鄰者先）
  ✅ K33 單元之部分併入 ⇒ 各成員乘同一百分比（巳 ①·K-9-66）
  ✅ K34 合併之宗終不配地 ⇒ 回原狀（K-9-58 ③·收斂時）
  ✅ K35 已試之帳以成員為準
  ✅ K36 調配之輸入：配地街廓含宿主之街廓
  ✅ K37 合併之列其後同一標的再受同街廓之併入 ⇒ 前列「續併」、末列「留置」
  ✅ K38 受併宗之相連⛔ 藉他街廓併入之片
  ✅ K39 回溯由最近之一次施起
  ✅ K40 不相連而併入之片⛔ 為相連
  ✅ K41 他街廓之併入之回溯由最近之一次起（K-9-61 ⑤）
  ✅ K42 回原狀之組合⛔ 再施（跨回溯）
  ✅ K43 回原狀後之併入⛔ 取已試之組合
  ✅ K44 回原狀後之併入逐宗（其一不配地⛔ 連帶其他）
  ✅ K45 回原狀之帳跨回溯而存
  ✅ K46 調配之輸入：段三之受併宗未配地 ⇒ 停機
  ✅ K47 N0-9 之片之回原狀後之併入
  ✅ K48 回原狀之帳之序定於回原狀之時（依其時之應分配面積·K-9-76 ②）
  ✅ K49 回原狀之帳之分不到之宗 ①′ 先於 ①
  ✅ K50 回原狀之帳之序以該次合併時之應分配面積定
  ✅ K51 成員之地價區段相異 ⇒ 各以其來源量計
  ✅ K52 合併之單元之部分併入之調配之輸入
  ✅ K53 成員之剩下之合與宗之面積不符（含非成員之土地）⇒ 停機
  ✅ K54 k965_part_split 之純函式
  ✅ K55 含非成員之土地而部分併入皆不過檢核 ⇒ ⛔ 停機·記未成（停機待檢核過後）
  ✅ K56 單片含非其成員之土地（面積_m2 淨 ≤ 0）而部分併入過檢核 ⇒ 停機（GB-205）
  ✅ K57 單片之帳相合 ⇒ 部分併入照常（其帳為全量）
  ✅ K58 單片含非其成員之土地而部分併入皆不過檢核 ⇒ ⛔ 停機·記未成
  ✅ K59 街角第 1 宗之應分配面積小於他宗 ⇒ 併入應分配面積大者（K-9-73 ①）
  ✅ K60 N0-9 之片亦入弱弱聯合（K-9-73 ②）
  ✅ K61 街角第 1 宗之依手冊之併入部分成／未成 ⇒ 其餘續依第 3 步併入次大之已配得之宗（K-9-73 ①）
  ✅ K62 同街廓相連之合併含可配得之宗 ⇒ 標的 ＝ 可配得之最大一塊（其側其位·K-9-76 ①）
  ✅ K63 回原狀之帳之序 ＝ 可配得之宗之應分配面積大者先（⛔ 相連者先·K-9-76 ②）
  ✅ K64 宗之成員帶「第31條第3款併入」⇒ ⛔ 併入同街廓之已配得之宗；弱弱聯合不以已配得之宗之有無為限（K-9-75 ①）
  ✅ K65 他宗之分量⛔ 含帶標記之宗（K-9-75 ①）
  ✅ K66 帶標記之宗之分量⛔ 含已配得之宗 ⇒ 與相連之配不到者依第 4 步合併（K-9-75 ①）
  ✅ K67 帶標記之宗之相連之合併不配地 ⇒ 續與不相連之配不到之宗弱弱聯合（全部·K-9-77）
  ✅ K68 同歸戶之他宗在推進序之前 ⇒ 帶標記之宗與其相連之宗先合併（K-9-77）
  ✅ K69 他街廓之帶標記之宗⛔ 先之（K-9-77）
  ✅ K70 他歸戶之帶標記之宗⛔ 先之（K-9-77）
  ✅ K71 帶標記之宗二 ⇒ 依 k967_rank 之序先之（K-9-77）
  ✅ K72 帶標記之宗已配得 ⇒ 相連之配不到之宗依第 3 步併入之（K-9-77）
  ✅ K73 帶標記之宗二·推進序之首⛔ 帶標記 ⇒ 依 k967_rank 之序（K-9-77）
  ✅ K74 推進序之首為帶標記而序次之宗 ⇒ 序首之帶標記之宗先之（K-9-77）
  ✅ P0 判式自驗 74／74
⇒ 紅 []；rc 0
````

### `#15`　`python3 verify/probes/probe_WG9375_k965.py wiring <repo>`（`rc 0`·`stderr` `0` B·`2.0` s）

````text
  ✅ Y1 簽名：五位置參數 ＋ 關鍵字 max_rounds／temp_parcels／cat_of／front_rows（預設 None）
  ✅ Y2 harness 之 run_step_g：入池閘之呼叫恰一、注入三參數、切片取 session 之 f3_k965_temp
  ✅ Y3 畫面之 _k929_6_screen_gate：注入三參數（f3_temp_parcels·classified_blocks·sb_rows_by_label）
  ✅ Y4 harness 之 build_build_parcels 寫 session 之 f3_k965_temp
  ✅ Y5 k929_6_fixpoint 內：k966_block_merge 恰一（得 1）·k953_alloc_summary／k967_rank／_projection_order 皆呼
  ✅ Y6 adj_intake 讀「入池閘部分併出」與「入池閘成員部分併出」
  ✅ Y7 k929_6_fixpoint 之字串常數⛔ 含案件字面（命中 []）
  ✅ Y8 三【未裁】之停機已去（K-9-58 ①②③）·未收斂之停機仍在
  ✅ Y9 畫面對拍器之畫面之 session 寫 f3_temp_parcels（同 main()）
  ✅ Y10 k965_part_split 之簽名·k929_6_fixpoint 內呼之恰一（得 1）·_pre965 呼 _src965·巳 ① 之停機已去
  ✅ Y11 GB-205 之停機⛔ 在 k965_part_split（得 0）·在 _try965 之 _chk965 之後（_chk965 [10459]·停機 [10464]）
⇒ 紅 []；rc 0
````

### `#16`　`python3 verify/probes/probe_WG9375_k965.py run <repo>`（`rc 0`·`stderr` `0` B·`61.2` s）

````text
  ✅ R1@3.5：build 51 宗·單元 7 ＝ 本器所載 True
  ✅ R2@3.5：配地 28 宗·不配地 21 宗 ＝ 本器所載 True
  ✅ R3@3.5：入池閘之紀錄 7 列 ＝ 本器所載 True
  ✅ R1@0.0：build 52 宗·單元 6 ＝ 本器所載 True
  ✅ R2@0.0：配地 29 宗·不配地 21 宗 ＝ 本器所載 True
  ✅ R3@0.0：入池閘之紀錄 6 列 ＝ 本器所載 True
⇒ 紅 []；rc 0
````

### `#1`　`python3 verify/probes/probe_WG9385_k974.py selftest <repo>`（`rc 0`·`stderr` `0` B·`2.0` s）

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

### `#2`　`python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe`（`rc 0`·`stderr` `0` B·`105.1` s）

````text
  ✅ W1 頂層之新名與⛔ 案件字面：[True, True, True, True]／K974_PARAMS True／字面 []
  ✅ W2 main() 恰一處呼之：['k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)']
  ✅ W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）：
  ✅ W4 JUNCTION 存 session：
  ✅ W5 步驟 H 之段以假 st 實跑：[{'label': 'B1', 'front_width': 15.0, 'front_length': 0.0, 'front_new': False, 'left_side_width': 0.0, 'left_side_length': 0.0, 'left_side_new': False, 'right_side_width': 0.0, 'right_side_length': 0.0, 'right_side_new': False, 'front_scale': 2.25, 'left_side_scale': 0.5}]／[('warning', '⚠️ 警示甲')]／[('error', '⛔ 錯甲'), ('error', '⛔ 錯乙')]／停 False/True
  ✅ W6 verify/ 之生產碼⛔ 呼之：[]
  ✅ W7 main／calc 唯增列（具名之換列三）·頂層之相異：相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K974_PARAMS', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'calc_special_burden_total', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k962_land_marks', 'k967_pool_less', 'k967_pool_out', 'k974_burden_scales', 'k974_read_junctions', 'k974_screen_scales', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']／刪列 3
⇒ 紅 []；rc 0
````

### `#3`　`python3 verify/probes/probe_WG9385_k974.py run <repo>`（`rc 0`·`stderr` `0` B·`361.8` s）

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

### `#62`　`python3 verify/probes/probe_WG9387_k961h.py selftest <repo>`（`rc 0`·`stderr` `0` B·`3.7` s）

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

### `#63`　`python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab`（`rc 0`·`stderr` `0` B·`2.9` s）

````text
  ✅ X1 adj_intake 呼叫 k967_rank（呼叫 1）
  ✅ X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise（[]）
  ✅ X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']）
  ✅ X4 adj_intake 內⛔ 案件字面（[]）
  ✅ X5 生產碼 app.py 以外之 33 檔對基準相異 0（相異 []）
⇒ 紅 []；rc 0
````

### `#64`　`python3 verify/probes/probe_WG9387_k961h.py run <repo>`（`rc 0`·`stderr` `0` B·`291.1` s）

````text
══ 退縮 3.5 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 92.46｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R3｜據 R2 27.54、R3 28.34｜外部錨 R3
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
══ 退縮 0.0 ══
  ✅ R1 盤點⛔ 停機
     G011｜原街廓 R3｜據 R2 3.82、R3 88.63｜外部錨 R3
     G025｜原街廓 R5｜據 R5 0.99、R6 0.26｜外部錨 R5
     G030｜原街廓 R2｜據 R2 27.54、R3 24.89｜外部錨 R2
  ✅ R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 []
  ✅ R3 合併單位（17）之原街廓 ＝ 外部錨（17）：相異 []
⇒ 紅 []；rc 0
````

### `#65`　`python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.4` s）

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

### `#66`　`python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64`（`rc 0`·`stderr` `0` B·`2.2` s）

````text
── 接線（工作樹之 app.py 對基準 fd88f64）──
  ✅ X1 四停機之字樣皆去（殘 []）
  ✅ X2 `_recv_of(b, y)` 之形與其 5 呼叫皆二引數
  ✅ X3 頂層之相異 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X4 ⛔ 案件字面（[]）
  ✅ X5 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#69`　`python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#70`　`python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20`（`rc 0`·`stderr` `0` B·`109.1` s）

````text
  ✅ X1 帶號之 raise 皆 k6_program_stop·⛔ 他用（帶號 11（基準之帶號 10·k980_acq_check 1·end_block_apply 0）／非者 []／他用 []）
  ✅ X2 吞試算之中止之處皆取 mark 並上拋（app.py 之處 5（基準 5）未合 []；selection_pipeline 之處 3（基準 3）未合 []）
  ✅ X3 頂層：新名 ＝ 五·相異 ⊆ 本單之許·其差唯二形（增 ['K6_PROGRAM_STOPS', 'K6_PROGRAM_STOP_RE', 'K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', 'end_block_band_width', 'end_block_trial_G', 'k6_program_stop', 'k6_trial_mark', 'k6_trial_raise_since', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']／去 []／相異 ['_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'adj_intake', 'end_block_apply', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'evaluate_parcel_width_n14', 'f3_screen_adj4', 'f3_screen_k953', 'f3_screen_stepg_run', 'k6b_screen_callbacks', 'k6b_stage3_run', 'k917_should_drop', 'k929_6_fixpoint', 'k953_manual_run', 'k967_pool_less', 'k967_pool_out', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']／不合 ['end_block_merge_run：刪列非 raise RuntimeError：[\'      建地之片之他街廓之候選依五級與深度再排·見其 docstring）。"""\', \'    _dup = {p: tg for p, tg in _cand_of.items() if len(tg) >= 2}\']']）
  ✅ X4 verify/ 頂層唯 selection_pipeline.py 異·其差唯含 k6_trial_ 之增列（異 ['verify/run_verification.py', 'verify/selection_pipeline.py', 'verify/stepg_pipeline.py']／換 0／增 6）
  ✅ X5 三函式內⛔ 案件字面（[]）
⇒ 紅 []；rc 0
````

### `#71`　`python3 verify/probes/probe_WG9389_trialstop.py run <repo>`（`rc 0`·`stderr` `0` B·`358.5` s）

````text
  ✅ R1@3.5：本案⛔ 觸程式之停機（登記 0·G 值列 35）
  ✅ R1@0.0：本案⛔ 觸程式之停機（登記 0·G 值列 36）
  ✅ R2@3.5：手冊先行之試算內之程式之停機 ⇒ 上拋（上拋：🔴 [試算內之程式之停機·手冊先行·harness 之試算] 🔴 [GB-999 注入] 手冊先行之試算內之程式之停機（合成））
⇒ 紅 []；rc 0
````

### `#72`　`python3 verify/probes/probe_WG9390_k961r.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.2` s）

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

### `#73`　`python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302`（`rc 0`·`stderr` `0` B·`1.9` s）

````text
── 接線（工作樹之 app.py 對基準 2aa6302）──
  ✅ X1 舊停機之字樣去之（殘 0）、還原之字樣去之（{'回原狀': 0, '還原後仍出現': 0}）、鎖定之查之字樣 3（期 ≥ 1）
  ✅ X2 頂層之相異 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', '_WF_NS_NAMES', '_build_corner_range_v3', '_corner_first_lot_G', '_end_region_R', '_place_pool_parcels', '_solve_G_one', 'end_block_apply', 'end_block_band_width', 'end_block_host', 'end_block_merge_run', 'end_block_side_geom', 'end_block_trial_G', 'f3_screen_stepg_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check', 'main', 'rw_from_width', 'select_corner_lots_both_sides_v12']（期 ['k6b_stage3_run']）、名之集同 False
  ✅ X3 ⛔ 案件字面（[]）
  ✅ X4 verify/ 頂層之 *.py 對基準逐位同（異 []）
⇒ 紅 []；rc 0
````

### `#74`　`python3 verify/probes/probe_WG9390_k961r.py run <repo>`（`rc 0`·`stderr` `0` B·`286.6` s）

````text
  ✅ R1@3.5：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 1·回原狀之列 0·其檢核 0·段三之成者 3·G 值列 35）
  ✅ R1@0.0：本案⛔ 停機、⛔ 回原狀（段三等之呼叫 0·回原狀之列 0·其檢核 0·段三之成者 0·G 值列 36）
  ✅ R0 諸退縮之段三之成者之和 3（[3, 0]·期 ≥ 1·其查已行）
⇒ 紅 []；rc 0
````

### `#75`　`python3 verify/probes/probe_WG9391_k980x.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

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

### `#76`　`python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4`（`rc 0`·`stderr` `0` B·`35.6` s）

````text
── 接線（工作樹對基準 a8657c4）──
  ✅ W1 _build_corner_range_v3 之呼叫 4（期 ≥ 4）皆傳 min_build_area：皆傳
  ✅ W2 諸呼叫之數 [('end_block_side_geom', 1), ('end_block_host', 2), ('_place_pool_parcels', 2)]（期 ≥ 1、≥ 2、≥ 2）皆傳 min_build_area：皆傳
  ✅ W3 末端帶之單一真相源 {'_place_pool_parcels→_end_region_R': 1, '_place_pool_parcels→_end_band': 0, '_end_region_R→end_block_band_width': 1, 'end_block_band_width 之呼叫（全檔）': 1}（期 1、0、1、1）
  ✅ W4 min_build_area 之值皆為 k980_mba（呼叫 8·期 ≥ 8·不合 []）、v12 之 _mba_pk 之賦值 True、k91_effective_min_build_area 之他處之呼叫之數⛔ 增（4／基準 4）、k980_mba 之分區之引數為字面者 []（期無）
  ✅ W5 k980_range_touch_check 之呼叫 [('select_corner_lots_both_sides_v12', 1), ('f3_screen_stepg_run', 1), ('stepg:_run_step_g_impl', 1)]·app.py 全檔 2（期各 1·app.py 全 2）、其範圍之名齊全 [True, True, True]（期三真）
  ✅ W6 頂層之名之增 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_G_MAX_ITER', 'K980_G_TOL', 'K980_TOUCH_TOL', 'RW_TABLE_25', 'end_block_band_width', 'end_block_trial_G', 'k980_acq_check', 'k980_mba', 'k980_range_touch_check']（期 ['K980_AREA_EPS', 'K980_AREA_TOL', 'K980_TOUCH_TOL', 'end_block_band_width', 'k980_mba', 'k980_range_touch_check']）、減 []
  ✅ W7 新增或改之頂層節點（28）內新增之案件字面 []
  ✅ W8 逐層照傳 min_build_area 皆照傳
  ✅ W9 引擎經 ns 取之新名 ['k980_mba', 'k980_range_touch_check'] ⊆ _WF_NS_NAMES（漏 []）
⇒ 紅 []；rc 0
````

### `#77`　`python3 verify/probes/probe_WG9391_k980x.py run <repo>`（`rc 0`·`stderr` `0` B·`562.9` s）

````text
  ✅ R1@3.5 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@3.5 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 237.13, 'R2': 318.17, 'R3': 317.79, 'R4': 236.01, 'R5': 309.73, 'R6': 309.13}·不合 []）
  ✅ R1@0.0 未輸入：三源之街角範圍面積同（街角 8·末端塊 {('R6', 'left'): 252.28, ('R5', 'right'): 167.54, ('R2', 'right'): 154.49, ('R3', 'left'): 153.77}·err None）
  ✅ R2@0.0 輸入最小建築面積：諸源之範圍面積 ＝ 輸入值（輸入 {'R1': 124.94, 'R2': 164.49, 'R3': 163.8, 'R4': 126.08, 'R5': 177.54, 'R6': 262.28}·不合 []）
⇒ 紅 []；rc 0
````

### `#78`　`python3 verify/probes/probe_WG9392_k980g.py selftest <repo>`（`rc 0`·`stderr` `0` B·`5.8` s）

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

### `#79`　`python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd`（`rc 0`·`stderr` `0` B·`4.1` s）

````text
  ✅ W1 _solve_G_one 之 solve_G_binary 以 K980_G_TOL／K980_G_MAX_ITER（呼叫 1·全檔 1）
  ✅ W2 取得之宗之自我檢查之四處（[('app.py', 4), ('verify/stepg_pipeline.py', 4)]）
  ✅ W3 end_block_host 之評選經 end_block_trial_G（1）·solve_one 之直呼 0
  ✅ W4 引擎經 ns 取之新名 ['end_block_trial_G', 'k980_acq_check'] ⊆ _WF_NS_NAMES（漏 []）
  ✅ W5 頂層之名之增 ['K980_G_MAX_ITER', 'K980_G_TOL', 'RW_TABLE_25', 'end_block_trial_G', 'k980_acq_check']·減 []
  ✅ W6 k980_acq_check 經 k6_program_stop 立 GB-206 之停機
  ✅ W7 新增或改之頂層節點（20）內新增之案件字面 []
  ✅ W8 _corner_first_lot_G 之 _solve_G_one 以 is_corner=True、w0_start=0.0（呼叫 1）
⇒ 紅 []；rc 0
````

### `#80`　`python3 verify/probes/probe_WG9392_k980g.py run <repo>`（`rc 0`·`stderr` `0` B·`281.2` s）

````text
  ✅ R1@3.5 自我檢查 567 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@3.5 本案之錨（KL 05:22 所核之甲）不合 []
  ✅ R1@0.0 自我檢查 432 次（['末端塊', '街角第1宗']·異 []）；評選對終態之街角第 1 宗 配對 8·異 []；末端塊 配對 0·異 []；err None
  ✅ R2@0.0 本案之錨（KL 05:22 所核之甲）不合 []
⇒ 紅 []；rc 0
````

### `#81`　`python3 verify/probes/probe_WG9393_endall.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

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

### `#82`　`python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415`（`rc 0`·`stderr` `0` B·`3.6` s）

````text
  ✅ W1 end_block_side_geom 之 'gate': False 之回傳 0
  ✅ W2 _place_pool_parcels 之「_unfront 之判 ⇒ continue」0·引 END_BLOCK_UNFRONT_EPS True·寫死 1e-3 0
  ✅ W3 _end_region_R／end_block_band_width 之「frag_poly 空」之停機 []
  ✅ W4 end_block_apply 之 'gate' 之字面 0
  ✅ W5 頂層之名之增 ['RW_TABLE_25']·減 []·相異之節點 ['_end_region_R', '_place_pool_parcels', 'end_block_apply', 'end_block_band_width', 'end_block_merge_run', 'end_block_side_geom', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'rw_from_width']
  ✅ W6 新增或改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
  ✅ W8 END_BLOCK_UNFRONT_EPS ＝ 0.001
  ✅ W9 end_block_apply 之 `raise k6_program_stop(…GB-207…)` 0（期 0·W-G.9-395 去之）
⇒ 紅 []；rc 0
````

### `#83`　`python3 verify/probes/probe_WG9393_endall.py run <repo>`（`rc 0`·`stderr` `0` B·`290.2` s）

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

### `#85`　`python3 verify/probes/probe_WG9394_k9615.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

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

### `#86`　`python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283`（`rc 0`·`stderr` `0` B·`3.8` s）

````text
  ✅ W1 頂層之名之增 ['RW_TABLE_25']·減 []·相異之節點 ['end_block_apply', 'end_block_merge_run', 'k6_trial_raise_since', 'k6b_stage3_run', 'k953_manual_run', 'rw_from_width']
  ✅ W2 k6_trial_raise_since 內之號之字面 ['GB-205']
  ✅ W3 _noaff 之二試算之間之 mark 與「新登記 ⇒ return False」（_noaff 有）
  ✅ W4 end_block_merge_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W8 k953_manual_run 之 `k6_trial_raise_since(…, adopted=True)` 1
  ✅ W5 k929_6_fixpoint 之 `raise k6_program_stop(…GB-205…)` 1（期 1）·對基準⛔ 變 True
  ✅ W6 所改之頂層節點內新增之案件字面 []
  ✅ W7 verify/ 頂層之 *.py（33）對基準相異 []
⇒ 紅 []；rc 0
````

### `#87`　`python3 verify/probes/probe_WG9394_k9615.py run <repo>`（`rc 0`·`stderr` `0` B·`278.6` s）

````text
  ✅ R1@3.5 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@3.5 受併宗 25·最後之配地⛔ 保留者 []
  ✅ R1@0.0 中止之訊 None·k965_part_split 之 None 0·程式之停機之登記之增 0
  ✅ R2@0.0 受併宗 26·最後之配地⛔ 保留者 []
⇒ 紅 []；rc 0
````

### `#88`　`python3 verify/probes/probe_WG9395_k960.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.6` s）

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
  ✅ V1 順序相反 ⇒ 互相等待 ⇒ 序鍵（G 之和 戊 81 ＞ 丁 63）⇒ 戊先：戊得 E、F 強制
  ✅ V2 G 之和（戊 72 ＞ 丁 63）與最大之一片（丁 50 ＞ 戊 36）異 ⇒ 依和：戊先
  ✅ V3 G 之和相等（72）⇒ 重劃前面積之和大者（戊 72 ＞ 丁 62·道路片⛔ 計）先：戊得 E、丁得 F
  ✅ V4 G 之和與重劃前面積之和皆相等 ⇒ 最小之暫編地號小者（D1(1)）先：丁得 E、戊得 F
  ✅ V5 三位地主互相等待成環（G 之和 丁 40／戊 60／己 50）⇒ 戊先、其餘依原位次（己、丁）
  ✅ V6 換名（街廓名之序反之·地號改名）⇒ V1 之結果除名稱外同（逐列之集·定案之端·皆未達）
  ✅ V7 互相等待而先處理者（丁·G 之和 80 ＞ 戊 72）在 F 端之前尚有第三人庚 ⇒ 庚照原位次先試而得 F；丁之競合消滅、丁得 E
  ✅ V8 環成即處理：V1 之環成於 F 端之末列，其後之他街廓之列（T）於其處理之後
  ✅ V9 夥伴之列已被延後過（E 戊己丁·F 丁己戊·G 戊 60／己 50／丁 40）⇒ 依其現位而退、⛔ 無限迴圈
  ✅ V10 二首列退至同一夥伴之列之後而退之先後與原位次相反（E 己丁戊·F 丁戊己）⇒ 依原位次（J1 先於 D1）
  ✅ V11 退至已被延後之夥伴之列（J1）之緊後（E 丁己辛戊·F 戊辛己丁·G 戊 80／己 70／丁 60／辛 50）⇒ D1 先於 K1
  ✅ V13 被延後者之夥伴之列其後自身又被延後（E 己辛戊丁·F 戊己丁辛·G 丁 90／辛 50／戊 30／己 20）⇒ 己之 J1 隨戊之 U1 而移
  ✅ V12 換名與換端：V11 之街廓改名（A7、B2·序同）、地號改名、二端皆為右端 ⇒ 除名稱外同 V11
⇒ 紅 []；rc 0
````

### `#89`　`python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4`（`rc 0`·`stderr` `0` B·`7.0` s）

````text
  ✅ W1 end_block_apply 內⛔ 有 GB-207 之字面、⛔ 有 k6_program_stop 之呼叫
  ✅ W2 end_block_merge_run：⛔ 有「同時跨占二以上末端塊」「屬二以上之競合」之停機；仍有「三個以上之末端塊」之停機
  ✅ W3 _k950_rows：⛔ 有「屬二以上之競合」之停機、仍有「列數 ≠ 2」之停機
  ✅ W4 頂層之名之增減 ['RW_TABLE_25']（期 []）；頂層節點之相異 ['RW_TABLE_25', 'end_block_apply', 'end_block_merge_run', 'k6b_stage3_run', 'rw_from_width']（期 ['end_block_apply', 'end_block_merge_run', 'k6b_stage3_run']）
  ✅ W5 所改之三節點內新增案件字面 []（期 []）
  ✅ W6 verify/ 頂層之 *.py 對基準相異 []（期 []）
⇒ 紅 []；rc 0
````

### `#90`　`python3 verify/probes/probe_WG9395_k960.py run <repo>`（`rc 0`·`stderr` `0` B·`285.7` s）

````text
  ✅ R1@3.5 觸發之端 4（期 4）、有當選 4（期 4）、「歸他端」之列 []（期 []）、err None
  ✅ R2@3.5 合併再試之標的 []（期 []）、競合 None（期 無）
  ✅ R1@0.0 觸發之端 4（期 4）、有當選 4（期 4）、「歸他端」之列 []（期 []）、err None
  ✅ R2@0.0 合併再試之標的 []（期 []）、競合 None（期 無）
⇒ 紅 []；rc 0
````

### `#92`　`python3 verify/probes/probe_WG9398_rw25.py selftest <repo>`（`rc 0`·`stderr` `0` B·`1.5` s）

````text
  ✅ T1 格點 171（1.0〜18.0 m 每 0.1 m）＝ 附表 25
  ✅ T2 格間 170 × 3 處 ＝ 二端之線性內插（公分以下用內插法）
  ✅ T3 請示表：5.30 ⇒ 45.85、5.35 ⇒ 46.15、7.00 ⇒ 55.69
  ✅ T4 起點 0 與 0〜1 m（自 (0, 0) 至 (1.0, 17.36) 線性）
  ✅ T5 飽和：≥ 18 m ＝ 100；17.95 ⇒ 99.875
  ✅ T6 格點之浮點之鄰（5.3 ± 1e-12、0.1×53、2.7＋2.6）⇒ 45.85
  ✅ T7 0〜18.5 m 每 0.0007 m：不減、相鄰之差 ≤ 0.02
  ✅ T8 累積差額之鏈 0→4.2→9.7→13.05→18.3 與倒退
  ✅ T9 玩具街廓之街角第 1、2 宗（左右 × 二座標系 × 二 a）＝ HB 之自解；舊表之自解至少一異；自解距半分 ≥ 0.001
  ℹ️ T9 之解（HB）[48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14, 48.87, 47.91, 73.4, 40.14]
  ℹ️ T9 之解（舊表）[48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16, 48.89, 47.91, 73.4, 40.16]
  ✅ P0 判式自驗 9／9
⇒ 紅 []；rc 0
````

### `#93`　`python3 verify/probes/probe_WG9398_rw25.py wiring <repo> 20e03bf`（`rc 0`·`stderr` `0` B·`2.5` s）

````text
  ✅ X1 頂層之名之增 ['RW_TABLE_25']·減 []·相異之節點 ['RW_TABLE_25', 'rw_from_width']
  ✅ X2 RW_TABLE_25 ＝ 17 × 10 之字面而逐格 ＝ 附表 25（列 17）
  ✅ X3 rw_from_width 讀 RW_TABLE_25／RW_SATURATION_WIDTH_M·其內表之值之數之常數 []
  ✅ X4 rw_increment、RW_SATURATION_WIDTH_M 之節點⛔ 變
  ✅ X5 RW_TABLE_25 以外之表之數之串（生產碼 34 檔）[]
  ✅ X6 新增或改之頂層節點內新增之案件字面 []
  ✅ X7 verify/ 頂層之 *.py 對基準之相異 []
⇒ 紅 []；rc 0
````

### `#94`　`python3 tests/test_pool_slot.py`（`rc 0`·`stderr` `0` B·`0.5` s）

````text
✅ W-D.2 滑池槽 golden 8/8 通過（KL 例 J=1.80/1.50（㎡ 單位）、E1-E7 全過）
````
