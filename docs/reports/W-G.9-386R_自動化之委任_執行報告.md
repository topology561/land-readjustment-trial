# `W-G.9-386R` 執行報告：自動化之委任入典 ＋ `W-G.9-385` 入主線之登記 ＋ 待落地清單之更新（零生產碼）

> **受單** ＝ 執行端（雲端排程「市地重劃·執行端」·自動化之第一輪）。**單** ＝ `docs/orders/W-G.9-386_規格單.md`（`23646` B·`sha256` `54dcae1cd3993b3472c584e725803fd813edfa954ed300b85eb5fe018fac16d3`）。
> **施工樹** ＝ `/tmp/w`（完整複本）；**`<O>`** ＝ `/tmp/o386`（任何 git 工作樹之外）。
> **開工時刻** ＝ `2026-10-17T08:59:34+08:00`（`ops/queue` 接單）。

---

## ① 逐 `commit`

| 工項 | `commit` | 首列 | 推送目標 | 推送 |
|---|---|---|---|---|
| 零 | `c9d3723bee75e2553b9e3e57048af6af861bcbe6` | `W-G.9-386 工項零：本單原封入倉 ⛔ 零生產碼` | `wip/s1-endpart` | `eb9bc66..c9d3723`（快轉） |
| 一 | `9344f26d04e23073b9a605bc4bdeb5ebb324c51c` | `W-G.9-386 工項一：自動化之委任入典（K-6 典）＋ W-G.9-385 入主線之登記 ＋ 待落地清單之更新（CLAUDE.md）⛔ 零生產碼` | `wip/s1-endpart` | `c9d3723..9344f26`（快轉） |
| 二 | 本報告之 `commit`（其 hash 載於 `ops/queue` 之 `reports/W-G.9-386_規格單_回報.md`·自身之 hash ⛔ 可自載） | `W-G.9-386 工項二：執行報告入倉 ⛔ 零生產碼` | `wip/s1-endpart` | 同上回報檔載之 |

推後之 `git ls-remote origin refs/heads/wip/s1-endpart`：工項一推後 ＝ `9344f26d04e23073b9a605bc4bdeb5ebb324c51c`；工項二推後之值載於 `ops/queue` 回報。

## ② 停機款之三值（款·期·實）

| # | 期 | 實 |
|---|---|---|
| `1` | 主線 `eb9bc66`、heads `46` 含 `ops/queue`、追蹤檔無變動、`issuer_anchor` `rc 0` 且四簿 ＝ 期 | `eb9bc66cbaf1c764a4000a86bc63f7307fdc63ca`；`46`；含 `1`；`git status --porcelain --untracked-files=no` 空；`rc 0`；四簿 ＝ 期（見 ③）⇒ ⛔ 觸 |
| `2` | `SELF_SHA256` 相符、`STATE.json` bytes／`sha256` 相符、入倉 blob 逐位同 | `f7f1386e…4193` 相符（受詞 ＝ 末列前之 `23568` B）；`23646` B／`54dcae1c…16d3` 相符；`git cat-file blob HEAD:docs/orders/W-G.9-386_規格單.md` 對來源 `cmp` 同 ⇒ ⛔ 觸 |
| `3` | 環境於安裝後能匯入 | 初 `rc 1`（無 `shapely`）；安裝後 `rc 0`（見 ③ 之自捕）⇒ ⛔ 觸 |
| `4` | 塊之值 ＝ `§五` 項 `2`／`7`；附後 `0` 刪、嚴格前綴、blob／bytes ＝ 項 `3`；`checkidx`／`gen_fa_index` ＝ 期 | 全 ＝ 期（見 ④⑤）⇒ ⛔ 觸 |
| `5` | `push` 目標唯 `wip/s1-endpart`／`ops/queue`、無須 `--force` | 二次 `wip/s1-endpart` 皆快轉、`ops/queue` 一次（接單）快轉 ⇒ ⛔ 觸 |
| `6` | 收工閘皆 ＝ 期 | 工項二前之預量見 ⑦；收工後之實量載 `ops/queue` 回報 |
| `7` | ⛔ 自判、⛔ 改器、新檔 ⛔ 為 `check-ignore` 命中 | 未作判；器與命令未改；本單之 `check-ignore -v --no-index` `rc 1` ⇒ ⛔ 觸 |
| `8` | 存取倉庫 | 取佇列、取主倉、推送皆成（未須 `add_repo`）⇒ ⛔ 觸 |

## ③ `§零` 之出艙

1. context 餘量：充足（約 `1490` 萬 tokens 餘）；`nproc` ＝ **`4`**（README 第六節第 3 款所稱「約 2 核」與實異；並行仍守 ≤ `2`）。
2. `git rev-parse origin/wip/s1-endpart` ＝ `eb9bc66cbaf1c764a4000a86bc63f7307fdc63ca`；`git ls-remote --heads origin` ＝ `46` 列、含 `refs/heads/ops/queue`（存 `<O>/heads_before_386.txt`·取於執行端接單推送之後，故其 `ops/queue` 列為接單後之值）；`git checkout --detach origin/wip/s1-endpart` 後 `git status --porcelain --untracked-files=no` ＝ 空；`git ls-tree -r` ＝ `2878` 列；`app.py` ＝ `cfd66e88…`、`CLAUDE.md` ＝ `6a2ff2ce…`、`K-6` 典 ＝ `e8639d46…`（皆 ＝ `§一` 項 `1`）。
3. `probe_WG9321_issuer_anchor.py /tmp/w /tmp/o386/issuer_anchor_0.txt 623 622` ⇒ `rc 0`（落檔 `sha256` `c4da03caad411f5fa6ca982f78e767c889796ba0859bb1e8153157e33ee045a9`）；「項4′ 四簿·正典框」：自誤 `608`／`623`／`[106, 355, 356, 357, 489, 492, 499, 511, 519]`；`GB` `197`／`205`／`[12, 87, 179, 181, 183, 184, 185, 203]`；`VR` `80`／`95`／`[73, 75]`；`K-9` `76`／`79`／`[44, 47]`；末 `✅ 二閘皆過`。
4. 本單 `23646` B／`54dcae1c…16d3` ＝ `STATE.json`；`SELF_SHA256` 依 `P-5`（取檔內最末一個、受詞 ＝ 其列之前之全部 bytes）實算 `f7f1386ea4a175cdefe4e855af1a6ef7250f7d71781dc04338c54152d3394193` ＝ 單載。
5. pre-flight：見 ⑥。
6. 環境：`python3 -c "import shapely,streamlit,pandas,openpyxl,ezdxf,geopandas"` 初 `rc 1`（`ModuleNotFoundError: No module named 'shapely'`·`<O>/env_import.txt`）⇒ `pip install -r requirements.txt --break-system-packages`（`rc 0`·`<O>/pip_install.txt`）後仍 `rc 1`（`<O>/env_import2.txt`）⇒ 見 ⑧ 自捕一 ⇒ `python3 -m pip install -r requirements.txt --break-system-packages`（`rc 0`·`<O>/pip_install2.txt`）⇒ `rc 0`（`<O>/env_import3.txt`）。

## ④ 塊之實得與二檔之改前改後

| 塊 | 出處 | bytes | `sha256` | 列 |
|---|---|---|---|---|
| `K28` | 本單 附錄甲（圍欄 `:114`–`:157`） | `4923` | `d88116c34e745d3349862f31f0a56acddab3ef60c825ec94677d4003e33ba973` | `42`（首列空） |
| `P39` | 本單 附錄乙（`:161`–`:176`） | `1758` | `c0746956156107cb1d31df947511864ea308d3bf2624b4098dde025f8c546d33` | `14`（首列空） |
| `CK` | `W-G.9-365_輕量單.md` 附錄午（`:807`–`:839`） | `1539` | `00cd3949ba1559583d6e4eb7177cb55055fa1689518e860335dd0cbbd22e554d` | `31` |
| `GF` | 同單 附錄巳（`:755`–`:803`） | `2445` | `b11edb77b044a883f6cb35b2eb2adfb1f205c26ab307f4bffda5420988ce10cc` | `47` |

| 檔 | 改前 bytes | 改後 bytes | 改後 blob | `numstat` | 嚴格前綴 |
|---|---|---|---|---|---|
| `docs/rulings/K-6_街角地分配程序與可分配判準.md` | `824230` | `829153` | `6f502cd8cca1f617beb5b9345325aef22a75b251` | `42`／`0` | ✅（`cmp -n 824230`） |
| `CLAUDE.md` | `413291` | `415049` | `0b36e0d292941ea380d1b5dc40718081680ec6d5` | `14`／`0` | ✅（`cmp -n 413291`） |

## ⑤ `checkidx`／`gen_fa_index`

- `python3 /tmp/o386/checkidx.py /tmp/w /tmp/w/.claude/rules/常設規則索引.md` ⇒ `rc 0`；末列 `索引列數 124；內部字樣 122；外部指標 9；不合 0`。
- `python3 /tmp/o386/gen_fa_index.py /tmp/w /tmp/o386/FX_regen.md` ⇒ `rc 0`；`則 124；加註節 14；列 158`；`cmp` 對 `.claude/skills/failure-archaeology-index/SKILL.md` 逐位同。

## ⑥ pre-flight

`python3 verify/probes/probe_order_preflight.py /tmp/w/W-G.9-386_規格單.md` ⇒ `rc 0`：🔴 `0` 項／🟡 `0` 項／ℹ️ `2` 項（`P-5` 相符·受詞 `23568` B；`P-3` `def main` ＝ `23351`–`31093`·本單⛔ 用）＝ `§五` 項 `5`。無須處置之項。

## ⑦ 收工閘之預量（於 `9344f26`·工項二前；收工後之實量載 `ops/queue` 回報）

閘 `6`：`probe_WG9270_closegate.py 623 622 .` ⇒ `rc 0`·末 `✅ 二閘皆過`；判別力 `624 623 .` ⇒ `rc 7`。

閘 `7`（並行 `2`）：

| 呼叫 | `rc` | 耗時 | `stderr` | 末列 | `P0` |
|---|---|---|---|---|---|
| `probe_WG9385_k974.py selftest` | `0` | `2.5` s | `0` B | `⇒ 紅 []；rc 0` | — |
| `probe_WG9385_k974.py wiring 158f7fe` | `0` | `84.9` s | `0` B | `⇒ 紅 []；rc 0` | — |
| `probe_WG9363_k953.py selftest` | `0` | `2.1` s | `0` B | `⇒ 紅 []；rc 0` | `75／75` |
| `probe_WG9363_k953.py wiring 7d8e954` | `0` | `25.9` s | `0` B | `⇒ 紅 []；rc 0` | — |
| `probe_WG9367_adj4.py wiring d7a5ea4` | `0` | `26.5` s | `0` B | `⇒ 紅 []；rc 0` | — |
| `probe_WG9370_adj4mut.py wiring 3b35daa` | `0` | `3.2` s | `0` B | `⇒ 紅 []；rc 0` | — |
| `probe_WG9375_k965.py selftest` | `0` | `1.6` s | `0` B | `⇒ 紅 []；rc 0` | `74／74` |
| `probe_WG9357_k948.py selftest` | `0` | `1.7` s | `0` B | `⇒ 紅 []；rc 0` | `35／35` |
| `probe_WG9373_k966.py selftest` | `0` | `1.3` s | `0` B | `⇒ 紅 []；rc 0` | `31／31` |
| `probe_WG9373p1_partrem.py selftest` | `0` | `1.2` s | `0` B | `⇒ 紅 []；rc 0` | `29／29` |

## ⑧ 自捕與自解

1. **`pip` 與 `python3` 異直譯器**：`/usr/bin/pip` 屬 Python `3.13`，`python3`（`/usr/local/bin/python3`）為 `3.11`；README 第六節第 2 款之 `pip install …` 裝入他直譯器、匯入仍敗。⇒ 以 `python3 -m pip install -r requirements.txt --break-system-packages` 為其等價（屬平台事項，⛔ 改單）。
2. **接單之 `STATE.json` 改寫用了 heredoc**：本單之通則「Bash 命令⛔ 含 heredoc」；接單（`執行端.md` 乙之第 2 步·`ops/queue`）時以 heredoc 之 Python 改 `STATE.json`。其後主倉之一切命令改以落檔之腳本（`<O>/extract.py`、`<O>/gate7.sh`）與 `printf`／`git commit -F` 為之。所改之物唯 `STATE.json` 之狀態轉移，結果無異。
3. **`<O>/heads_before_386.txt` 之 `ops/queue` 列**：取於接單推送之後；收工閘 `5` 本即除 `ops/queue` 而比，⛔ 影響。

## ⑨ 各段耗時

接單至工項一推送約 `5.5` 分（含二度安裝依賴）；閘 `7` 預量約 `151` s（並行 `2`·牆鐘約 `120` s，以 `k974 wiring` 之 `84.9` s 為主）。

## ⑩ 雲端執行之所見

- 取佇列（`clone --depth 1 --branch ops/queue`）、取主倉（完整 `clone`）、推送（`ops/queue` 一次、`wip/s1-endpart` 三次）皆成，未遇代理之拒；未須 `add_repo`。
- 本機 `nproc` ＝ `4`（非 `2`）；README 第六節第 3 款之並行 ≤ `2` 照守。
- 本機無預裝之依賴；`pip` 指向 `3.13`、`python3` 為 `3.11` ⇒ 建議 README 第六節第 2 款改書 `python3 -m pip install -r requirements.txt --break-system-packages`（供發單端酌；執行端⛔ 改之）。
- 主 checkout 之同步由 KL 自行為之（README 第六節第 6 款）。
