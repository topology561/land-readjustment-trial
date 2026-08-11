# `W-G.9-4b`：`W` 單一產生者之**接線修復** ＋ 接線閘之**射程補齊**

**產出**：CC／2026-08-11　**分支**：`wip/s1-endpart`（本地支 `wg94b-wiring`）
**基準**：`1041874`　**事前登記**：`docs/reports/W-G.9-4b_前置登記.md`（commit `4356467`）

> # 🔴 **一句話**：`W-G.9-4` 只做了「引擎側取用」，**沒做 app 側登錄**
> ⇒ app 之七級調配 **`KeyError` 於 `stepg_pipeline.py:334`**。本批補上登錄，並立一道
> **不寄生於死閘**之守護夾具。
>
> ⚠️ **同時具名一項既有另案**：即使接線修好，`run_step_g` 仍於**兩情境皆** raise
> （結構閘「理論＝實跑」破·街廓 R1）⇒ **七級調配依然不可完成**。該項 ⛔ 本批不修（§3）。

---

## §1 `F1`〜`F5` 逐項結果

| # | 預測 | 判 | 殘差／依據 |
|---|---|---|---|
| **F1** | 命題 **P** 為真 | ✅ **成立** | AST：`ns["k956_W_from_mp"]` 落於 `run_step_g` 函式體、祖先鏈條件性節點 **(無)** ⇒ 無條件執行；實呼：受限 ns **實拋** `KeyError: 'k956_W_from_mp'` @ `stepg_pipeline.py:334` |
| **F2** | 修復後反向閘差集為**空** | ✅ **成立** | 差集 `1041874` ＝ `['k956_W_from_mp']` → HEAD ＝ **（空）**；引擎消費 **24** 名、清單 **25 → 26** |
| **F3** | 修復後 app 路徑七級調配**可完成**且輸出與 `6ab9e86` 相同 | 🔴 **前半破**（成因＝既有另案）<br>✅ **後半成立**（可達範圍內） | 「可完成」**不可能成立**——見 §2；「輸出相同」＝ 逐桶 md5 全等、`.raw` **逐位元相同**（`77ab60c36cca551528acde91ffa32c54` 兩端一致、`diff rc=0`） |
| **F4** | `run_all` 判定層與 `WG94_runall.log` 相同、唯一容許差 ＝ 新夾具之列 | ✅ **成立** | 判定行 `diff` **rc=0**；全檔 23 差異行中 **22 行**含 worktree 路徑，**唯一非路徑差異** ＝ 新夾具之列。`PASS 12／FAIL 22`（與基準同值） |
| **F5** | 竄改自檢具鑑別力 | ✅ **成立** | 靜態：抽 `F3_CATEGORY_BURDEN` ⇒ 該名**新出現**於差集；動態：抽 `get_min_lot_size`（`stepg:279`·AST 證無條件）⇒ `KeyError @ :279`。**對真缺陷態**（`1041874`）實跑 ⇒ **rc=1** |

### 1-1 `F1` 之雙證（⛔ 非僅 grep）

```
【A 層·AST】verify/stepg_pipeline.py
  `ns["k956_W_from_mp"]` 取用點數 ＝ 1
    :334  所屬函式 ＝ `run_step_g`
           祖先鏈上之條件性節點（函式體內）＝ (無)      ⇒ 無條件執行

【B 層·實呼】ns 由 `_wf_ns()` 建出（⛔ 非 harvest 全 globals）
  harvest 全 globals ＝ 227 名；`_wf_ns()` 受限 ns ＝ 25 名
  `k956_W_from_mp` ∈ _wf_ns() ⇒ False ／ ∈ harvest() ⇒ True   ← 二路徑分岔即缺陷所在
  [B-2·受詞]   實拋 KeyError    @ stepg_pipeline.py:334   鍵 'k956_W_from_mp'
  [B-0·對照組] 實拋 RuntimeError @ stepg_pipeline.py:1362  ＝ 既有另案
  ⇒ :334 < :1362 ⇒ **KeyError 先發**
```

全文：`verify/out/probe_WG94b_wiring_PRE.log`（修復前）／`verify/out/probe_WG94b_wiring.log`（修復後）。
修復後同一探針：**B-2 與 B-0 落於同一點**（`RuntimeError @ :1362`）
⇒ 受限 ns **已足供引擎**。

### 1-2 `F3` 之對拍方法（鍵 ＝ **情境 × 街廓 × 側別**·⛔ 不用宗序號）

- **兩端**：`6ab9e86`（scratchpad detached worktree）vs 修復後 HEAD。⛔ 未於本工作樹 checkout、⛔ 未用 `reset --hard`。
- **取值路徑**：ns 一律 `ns_full["_wf_ns"]()`。⛔ `harvest()` 全 globals 之結果**未**充作證據。
- **觀測量**：`run_step_g` 之全部 stdout ＋ 終止例外，正規化（去絕對路徑、去行號）後逐桶 md5。
  該輸出含真實生產數：`理論@k*`／`實跑`／`Δ`／逐界面 `W_far`/`W_near`/`W_start`／
  `[T2-DIAG]` 池帶面積與覆蓋殘差／`[配餘]` 入抵費地量。
- **結果**：**6 桶全等**（`0m`／`3.5m` × `R1` × `left`/`right`/`—`），`.raw` `diff rc=0`。

⚠️ **覆蓋率之誠實界定（⛔ 非靜默截斷）**：可觀測範圍**僅 `R1`**——既有另案於 **R1 即中斷**
`run_step_g` ⇒ **R2–R6 完全未進入觀測**。⛔ **不得記為「全街廓已驗」。**

⚠️ **另附由構造之論證**（非替代實測，僅補強）：本批之碼面變更為
**在一個 list 字面加一個字串**，`_wf_ns()` 對之只做 `ns[n] = g[n]`
（`grep -n "def _wf_ns" app.py` ⇒ `:12434`）⇒ **不可能改變任何算式**。

---

## §2 🔴 `F3` 前半破之成因：**既有另案**（⛔ 非本批引入·⛔ 本批不修）

`run_step_g` 於 **`0m` 與 `3.5m` 兩情境皆** raise：

```
RuntimeError @ stepg_pipeline.py:1362
  🔴 結構閘 理論＝實跑 破：街廓 R1 left 側 理論@k*=97.18 ≠ 實跑(階段1)=100.02（Δ=2.837 >0.1）   ← 0m
  🔴 結構閘 理論＝實跑 破：街廓 R1 left 側 理論@k*=96.30 ≠ 實跑(階段1)=98.75（Δ=2.446 >0.1）   ← 3.5m
```

**其為既有**：`verify/out/WG94_runall.log`（本批之前）已列
`🔴 FAIL v3·StepG0m（結構閘/看守觸發）` 與 `🔴 FAIL v3·StepG3.5m（…）`，訊息與上開**同值**。

**其與 `W-G G.1` 之 `KeyError: '0m'` 為同一根**：`run_step_g` 兩情境皆 raise
⇒ native `_ctx` 從未取得 `"0m"` 鍵 ⇒ G.1 閘首行 `_ctx["0m"]` 即崩。

🔒 **對施工單 `F3` 措辭之具名回報**：`F3` 寫「修復後 app 路徑之七級調配**可完成**」——
該子句在本倉態下**不可能為真**，且其不可能**先於本批存在**。
⇒ 本報告**不宣稱** `F3` 全條成立，改為**前半破／後半成立**之二分判定，並具名成因。
⚠️ 此屬**施工單之前提與倉態不符**，⛔ 非本批之施工結果。

---

## §3 反向閘之**修復前後差集對照**（施工單 §7 指定）

以 `verify/run_verification.py` W-8 反向閘之**原式**（正則 ＋ 6 檔）現算：

```
1041874(修復前)   清單=25  引擎消費=24  差集=['k956_W_from_mp']
HEAD(修復後)      清單=26  引擎消費=24  差集=（空）
```

🔴 **但該閘於兩態下皆<u>不會亮</u>**——它寄生於 `W-G G.1` 之 `try`，
而該項於首行 `_ctx["0m"]` 即崩、`except` 接走 ⇒ 差集檢查**從未執行**；
且 `W-G G.1` 早在期望 FAIL 名單上 ⇒ **它紅、名單說它該紅、對帳為綠**。

⇒ 新夾具 `verify/fixture_wf_ns_wiring.py` **不寄生於任何前置**（獨立 subprocess），
故上開差集**真的會被檢查**。

---

## §4 新夾具之三層與其自證

| 層 | 內容 | 自證 |
|---|---|---|
| **靜態** | AST 取 `ns[<字面字串>]`，與 `_WF_NS_NAMES` 取差集 | 抽 `F3_CATEGORY_BURDEN` ⇒ 差集新增該名 ⇒ 紅；還原 ⇒ 綠 |
| **動態** | 以 **`_wf_ns()`** 建 ns、**實跑** `run_step_g` | 抽 `get_min_lot_size` ⇒ `KeyError @ stepg:279` ⇒ 紅；正常態 ⇒ ns 解包段通過 |
| **對真缺陷** | 於 `1041874` 全跑 | 靜態 `['k956_W_from_mp']`＋動態 `KeyError @ :334` ⇒ **rc=1** |

### 4-1 靜態層自述之三項射程（⛔ 夾具自身輸出即印）

- **【目錄射程】** 硬判 6 檔：`wf_f0.py, wf_f1.py, wf_f2.py, wf_f3.py, wf_f4.py, stepg_pipeline.py`
  （相對 `verify/`·⛔ 不含 `.claude/worktrees/`）。
- **【字樣射程】** **任何** `ns[<字面字串>]`——⛔ **不預設符號名**、⛔ 不列舉已知名單
  （否則新加的名正好是抓不到的那個）。
- **【連接方式】** AST `Subscript(Name('ns'), Constant(str))` **結構匹配**
  ——⛔ 非正則、⛔ **無固定距離窗** `.{0,N}`。

**射程外之列示**（⛔ 不靜默截斷）：import 遞移閉包 **11 檔**，硬判範圍外 **5 檔**
（`app_harvest.py, run_verification.py, selection_pipeline.py, wd3_fragment_geom.py, wd4_tier_list.py`），
其「消費但未列」之名共 **24** 個 —— ⚠️ **僅列示不判紅**（走 harness 全 harvest 路徑、
非 `_wf_ns()` 路徑；此為既有反向閘已記之理由）。

### 4-2 判準為何**不是**「`run_step_g` 是否成功」

在既有另案下該判準**恆假** ⇒ 夾具永紅、失去意義。
故動態層之判準寫成**受詞本身之命題**：**ns 解包段是否通過**
（＝有無 `KeyError` 落於 `run_step_g` 內之 `ns[...]` 行號集）。
⛔ 這**不是** `try/except` 吞例外——例外之型別、鍵名、落點、訊息**一律印出**。

### 4-3 情境射程

⚠️ 動態層**僅跑 `0m`**（施工單 §2-3 之「至少一次」）——夾具自身輸出**正面標示**，⛔ 非靜默截斷。

---

## §5 🔴 **本批未做之事**（施工單 §7 指定·⛔ 逐項）

1. **`W-G G.1` 之上游 `KeyError: '0m'` 未修**（＝ §2 之結構閘另案）
   ⇒ **現行 W-8 反向閘仍為死閘**。🔒 **新夾具是<u>繞過</u>它，不是修好它。**
2. **七級調配於 app 內仍不可完成**——接線已通，但撞既有結構閘。
3. **族②③ 之生產消費未切換**（`_W_prev_left/right`、`_select_pool_slot` 之 `'b'`
   仍取舊式 `buf · _cos_dn`）⇒ `GB-47` **本體不關閉**。屬 `W-G.9-5`。
4. **未重烤任何基準**；未設 `WV_BAKE`；未改期望 FAIL 名單。
5. **`verify/wf_f*.py` 與 `verify/stepg_pipeline.py` 零觸**（`git diff --numstat` 皆空輸出）。
6. **`F3` 之覆蓋僅 `R1`**（見 §1-2 之誠實界定）。

---

## §6 §5 驗收逐閘（採前置登記 §5·＝施工單 §6）

| # | 閘 | 判 |
|---|---|---|
| 1 | 命題 **P** 由 AST ＋ 實際呼叫**雙證**，⛔ 非僅 grep | ✅ §1-1 |
| 2 | `F3` 以 (情境 × 街廓 × 側別) 為鍵，列對拍方法與殘差 | ✅ §1-2（6 桶·殘差 0·`diff rc=0`） |
| 3 | `F3` 之證據來自 `_wf_ns()` 路徑 | ✅ 探針內 `ns_full["_wf_ns"]()`；⛔ 未用 harvest 全 globals 充證 |
| 4 | `F4` 逐項對照，新夾具之列正面標示為本批新增 | ✅ §1 之 `F4` 列；⛔ 未用「逐字相同」之措辭 |
| 5 | 竄改自檢**兩態**皆印入夾具自身輸出 | ✅ `verify/out/fixture_wf_ns_wiring.log` |
| 6 | 靜態層自述三項射程；字樣語意窮舉、⛔ 不預設符號名、⛔ 無距離窗 | ✅ §4-1 |
| 7 | 每一出艙之數，其指令於落筆當次重跑且並列 | ✅ §7 |
| 8 | `wf_f*` numstat 空輸出；文件刪除欄 0 | ✅ §7 |
| 9 | 凡書「正典」就地標權威序層級 | ✅ 本文未書「正典」二字；碼註中之引用已標**第 1 級**（`app.py` 新增註解） |
| 10 | 施工單 §2-4 之三處加註皆落地、原句一字未刪 | ✅ §8 |

---

## §7 出艙之數（⛔ 指令與輸出並列·**皆本報告落筆當次重跑**）

```
$ python -c "<讀 app.py 之 _WF_NS_NAMES 字面·印(名目數, 是否含 k956_W_from_mp)>"
26 True

$ <以 run_verification W-8 反向閘之原式現算差集>
  1041874(修復前)   清單=25  引擎消費=24  差集=['k956_W_from_mp']
  HEAD(修復後)      清單=26  引擎消費=24  差集=（空）

$ md5sum verify/out/probe_WG94b_f3_parity_6ab9e86.raw verify/out/probe_WG94b_f3_parity_HEAD.raw
77ab60c36cca551528acde91ffa32c54 *verify/out/probe_WG94b_f3_parity_6ab9e86.raw
77ab60c36cca551528acde91ffa32c54 *verify/out/probe_WG94b_f3_parity_HEAD.raw

$ wc -l verify/out/WG94_runall.log verify/out/WG94b_runall.log
  319 verify/out/WG94_runall.log
  320 verify/out/WG94b_runall.log

$ diff <(grep -E "✅ PASS|🔴 FAIL" WG94_runall.log) <(… WG94b_runall.log); echo rc=$?
rc=0

$ diff 全檔 | grep "^[<>]" | grep -v worktrees
>   ✅ 末端夾具 fixture_wf_ns_wiring.py（🆕 W-G.9-4b app 接線清單↔引擎 ns[] 消費（AST 靜態＋_wf_ns() 實跑＋竄改自檢））rc=0
$ diff 全檔 | grep -c "^[<>]"        ⇒ 23
$ diff 全檔 | grep "^[<>]" | grep -c worktrees   ⇒ 22

$ grep -c '✅ PASS' verify/out/WG94b_runall.log ⇒ 12
$ grep -c '🔴 FAIL' verify/out/WG94b_runall.log ⇒ 22

$ git -c core.quotePath=false diff --numstat        （commit B′ 之前態）
76      0       .claude/skills/failure-archaeology/SKILL.md
8       0       app.py
1       0       docs/reports/W-G.4_泛用阻塞項登記表.md
69      0       docs/reports/W-G.9-4_expand報告.md
9       1       verify/run_all.py

$ git diff --numstat -- verify/wf_f0.py … verify/wf_f4.py   ⇒ （空輸出）
$ git diff --numstat -- verify/stepg_pipeline.py            ⇒ （空輸出）
```

🔒 **`verify/run_all.py` 之刪除欄 `1` 之具名**：該行為原清單末項之收尾
`("fixture_end_winner.py", …))` → `…),`（加逗號續接新項）。
**該項之內容逐字未變**；⛔ 無任何既有項被刪。文件（`docs/`／`.claude/skills/`）之刪除欄**皆 0**。

---

## §8 §2-4 之三處加註（⛔ 原句一字不刪）

| 處 | 內容 | 偏離 |
|---|---|---|
| `docs/reports/W-G.9-4_expand報告.md` | 新增「🔧 加註（`W-G.9-4b`）」節：撤回 `E3`；`E4` 三分處置；閘 6 之正交性 | ⚠️ **二處與施工單文字不同·已於加註內具名**：① 只撤回 `E3`，`E4` 之**登記原文為真**故不整條撤回（改為措辭更正＋證據力撤回）；② 閘 6 之**目錄射程確含 `app.py`**，洞在**字樣射程之受詞**、非目錄 |
| `docs/reports/W-G.4_泛用阻塞項登記表.md` | `GB-47` 下新增 `↳` 列（`W-G.9-4b` 進度＋覆蓋受限之界定） | — |
| `.claude/skills/failure-archaeology/SKILL.md` | **新增節 65**（五層：用途推定接線範圍／期望 FAIL 名單「包月」／函式體未變≠路徑可走／over-determined 互相遮蔽／CC 同批再犯之自誌） | ⚠️ 根因措辭由 CC 現查後自定（施工單 §2-4 明文允許），⛔ 未照抄 |

---

## §9 上呈事項（⛔ 非本批可裁）

1. 🛑 **既有結構閘另案**（`v3·StepG0m`／`3.5m`）使**七級調配於 app 內兩情境皆不可完成**。
   本批已把接線修好，**但功能仍不可用**。該項受 `K-9-5-10`【裁】1／2 與重烤時點牽制。
2. ⚠️ **期望 FAIL 名單之結構性風險**（考古節 65 第二層）：`W-G G.1` 在名單上
   ⇒ 其所寄生之 **W-8 反向閘**永久失聲。建議通盤複查
   **「名單上每一項原本在守什麼、現在誰接手」**。
3. ⚠️ `verify/wg_g1_smoke.py`（自述為「app `_build_wf_ctx` → wf_f0→f4 全鏈端到端跑通」，
   ＝**真 app 路徑之唯一複本**）**不在任何自動流程內**——三處命中皆僅取其 helper
   `_reconstruct_sb_rows`。⇒ 與 `run_all.py:99` 所指之覆蓋率洞**同族**，本批**未處置**。

---

## 🔧 加註（`W-G.9-6`·CC／2026-08-11·⛔ 上文原句一字未刪）

🔴 **§9-3 之「唯一複本」為誤**（CC 自誤·`W-G.9-6` §2-4 現查）。
真 app 路徑（`_build_wf_ctx` → f0→f4）之端到端複本**實有三支**，且**三支皆不在任何自動流程內**：

| 檔 | `_build_wf_ctx` 命中 | 跑 `wf_f4.compute` | 在 `run_all` 內 |
|---|---|---|---|
| `verify/wg_g1_smoke.py` | 6 | ✅ | 🔴 否 |
| `verify/wg_g2_smoke.py` | 3 | ✅ | 🔴 否 |
| `verify/wg_g3.py`（**W-G 收官王牌**·`CLAUDE.md` 收官判準 ① 之 G.3 終驗工具） | 6 | ✅ | 🔴 否 |

```
$ grep -c "wg_g1_smoke\|wg_g2_smoke\|wg_g3" verify/run_all.py
0
```

⇒ 覆蓋率洞之**規模大於**原述；⛔ 結論方向不變（本批仍未處置），惟**受詞應為三支**。
詳見 `docs/reports/W-G.9-6_期望FAIL名單守備盤點.md` §6。
