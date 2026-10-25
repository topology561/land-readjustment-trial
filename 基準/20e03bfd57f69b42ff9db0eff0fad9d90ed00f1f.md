# 基準 `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`

- 立者 ＝ 發單端（`發單端.md` 乙 4之一）·`W-G.9-395` 補令二（入主線之短單）之復驗之輪；主線 `wip/s1-endpart` ＝ `20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`（前值 `d4928d4845513a42fb1ac826a63167a38c78d4fb`·快轉·執行端 2026-10-26 01:3x 推·快轉前之記 `ops/queue` 之 `924e73f`）。
- 樹 ＝ 倉外之拋棄式 worktree（`git worktree add --detach <wt> 20e03bfd57f69b42ff9db0eff0fad9d90ed00f1f`）；殼無 `WV_` 之變數；`PYTHONIOENCODING=utf-8`、`PYTHONUTF8=1`；並行 `2`；雲端 Linux `4` 核。
- 呼叫 ＝ `W-G.9-395` 規格單 `§五-1` 之「項 `8` 之表」之 `91` 呼叫（其序與命令同之；`<repo>` ＝ 該 worktree 之絕對路徑；`<O>` ＝ 倉外之輸出目錄；`<態>` ＝ `post`）。其 `#1`〜`#87` ＝ `基準/d4928d4845513a42fb1ac826a63167a38c78d4fb.md` 之呼叫（命令逐字同）；`#88`〜`#90` ＝ `F39`（`probe_WG9395_k960.py`）之 `selftest`／`wiring <repo> d4928d4`／`run`；`#91` ＝ `probe_order_preflight.py --selftest`。`W-G.9-395` 補令二之收工閘 `8‴` 之 `36` 呼叫皆含於其中。
- 期 ＝ 該表之「施後」之欄（`rc`／`stderr`／末列·`#56`／`#57` 之末列為 JSON 之摘要·⛔ 比）；合期 `91`／`91`；`stderr` 合計 `0` B；耗時之和 `14602` s（並行 `2`·耗時⛔ 為期）。
- 主線之生產碼（`app.py` 與 `verify/*.py`）與 `W-G.9-395` 補令一工項二″ 之 `c84a48f` 逐位同（`git diff --name-only c84a48f 20e03bf -- app.py ':(glob)verify/*.py' verify/` 空）；`app.py` ＝ `07dfd835c9c93fbec6a23a14791334879edb58cb`。

## 一、環境之指紋

- `python3 --version` ＝ `Python 3.11.17`
- `python3 -m pip freeze` 之 `sha256` ＝ `ae1438da0be1d9753bab4c5d73ea5886daf2706f768be67be52b94334786f1ac`（`1114` B·`64` 列）；全文見本檔之末。依 `requirements.txt` 裝後須釘回之八處同前基準（`certifi==2026.10.18 pandas==3.0.6 pillow==12.3.0 python-dateutil==2.9.0.post0 streamlit==1.66.0 websockets==17.2 starlette==1.9.0`·`pip uninstall -y tzdata`）。

## 二、呼叫（`rc`／`stderr` B／末列·耗時 s）

| # | 命令 | rc | stderr B | 末列 | s |
|---|---|---|---|---|---|
| `1` | `python3 verify/probes/probe_WG9385_k974.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `2` | `python3 verify/probes/probe_WG9385_k974.py wiring <repo> 158f7fe` | `0` | `0` | `⇒ 紅 []；rc 0` | 131 |
| `3` | `python3 verify/probes/probe_WG9385_k974.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 422 |
| `4` | `python3 verify/probes/probe_WG9363_k953.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `5` | `python3 verify/probes/probe_WG9363_k953.py wiring <repo> 7d8e954` | `0` | `0` | `⇒ 紅 []；rc 0` | 32 |
| `6` | `python3 verify/probes/probe_WG9367_adj4.py wiring <repo> d7a5ea4` | `0` | `0` | `⇒ 紅 []；rc 0` | 34 |
| `7` | `python3 verify/probes/probe_WG9370_adj4mut.py wiring <repo> 3b35daa` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `8` | `python3 verify/probes/probe_WG9357_k948.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `9` | `python3 verify/probes/probe_WG9355_screenmerge.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `10` | `python3 verify/probes/probe_WG9356_screenmerge_wiring.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 38 |
| `11` | `python3 verify/probes/probe_WG9350_frontroad.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 16 |
| `12` | `python3 verify/probes/probe_WG9350_frontroad.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 249 |
| `13` | `python3 verify/probes/probe_WG9367_adj4.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `14` | `python3 verify/probes/probe_WG9375_k965.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `15` | `python3 verify/probes/probe_WG9375_k965.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `16` | `python3 verify/probes/probe_WG9375_k965.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 70 |
| `17` | `python3 verify/probes/probe_WG9363_k953.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 453 |
| `18` | `python3 verify/probes/probe_WG9367_adj4.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 643 |
| `19` | `python3 verify/probes/probe_WG9370_adj4mut.py mutate <repo>` | `0` | `0` | `⇒ 突變 8（另基準一）；紅 []；rc 0` | 9 |
| `20` | `python3 verify/probes/probe_WG9373_k966.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `21` | `python3 verify/probes/probe_WG9373_k966.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `22` | `python3 verify/probes/probe_WG9373_k966.py mutate <repo>` | `0` | `0` | `⇒ 突變 57（另基準一）；紅 []；無從判定 []；rc 0` | 68 |
| `23` | `python3 verify/probes/probe_WG9373_k966.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 395 |
| `24` | `python3 verify/probes/probe_WG9373p1_partrem.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `25` | `python3 verify/probes/probe_WG9355_screenmerge.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 1694 |
| `26` | `python3 verify/probes/probe_WG9358_k948_wiring.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 36 |
| `27` | `python3 verify/probes/probe_WG9349_k9296.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `28` | `python3 verify/probes/probe_WG9349_k9296.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 6 |
| `29` | `python3 verify/probes/probe_WG9345_screen.py wiring <repo>` | `0` | `0` | `⇒ rc 0（不符 0·器紅 0）` | 23 |
| `30` | `python3 verify/probes/probe_WG9350_frontroad.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `31` | `python3 verify/probes/probe_WG9351_intake.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 23 |
| `32` | `python3 verify/probes/probe_WG9351_intake.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 260 |
| `33` | `python3 verify/probes/probe_WG9351_intake.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 329 |
| `34` | `python3 verify/probes/probe_WG9352_endblock.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 37 |
| `35` | `python3 verify/probes/probe_WG9352_endblock.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 39 |
| `36` | `python3 verify/probes/probe_WG9353_endmerge.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 8 |
| `37` | `python3 verify/probes/probe_WG9353_endmerge.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 22 |
| `38` | `python3 verify/probes/probe_WG9354_endcontest.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 17 |
| `39` | `python3 verify/probes/probe_WG9354_endcontest.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 12 |
| `40` | `python3 verify/probes/probe_WG9357_k948.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 192 |
| `41` | `python3 verify/probes/probe_WG9359_cand.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `42` | `python3 verify/probes/probe_WG9359_cand.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 51 |
| `43` | `python3 verify/probes/probe_WG9360_cand_mut.py mut <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 872 |
| `44` | `python3 verify/probes/probe_WG9361_k954.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `45` | `python3 verify/probes/probe_WG9361_k954.py wiring <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 1 |
| `46` | `python3 verify/probes/probe_WG9361_k954.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 158 |
| `47` | `python3 verify/probes/probe_WG9362_k954_mut.py mut <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 115 |
| `48` | `python3 verify/probes/probe_WG9372_ww.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 1 |
| `49` | `python3 verify/probes/probe_WG9372_ww.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 337 |
| `50` | `python3 verify/probes/probe_WG9344_k6s3.py selftest` | `0` | `0` | `selftest 9/9 ⇒ ✅` | 0 |
| `51` | `python3 verify/probes/probe_WG9344p1_pooltemp.py selftest` | `0` | `0` | `selftest 13/13 ⇒ ✅` | 0 |
| `52` | `python3 verify/probes/probe_WG9348_harvest_key.py <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `53` | `python3 verify/probes/probe_WG9341_synth.py <repo>` | `0` | `0` | `ε ＝ 0.0002｜rc 0` | 2 |
| `54` | `python3 verify/probes/probe_WG9340_main_synth.py <repo>` | `0` | `0` | `紅項 [] 器紅 0` | 11 |
| `55` | `python3 verify/probes/probe_WG9346_failclosed.py run <repo> 3.5` | `0` | `0` | `⇒ 紅 []；rc 0` | 342 |
| `56` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 3.5 on <O>/k6s3_<態>_35.json` | `0` | `0` | `（JSON 之摘要列·略）` | 186 |
| `57` | `python3 verify/probes/probe_WG9344_k6s3.py run <repo> 0.0 on <O>/k6s3_<態>_00.json` | `0` | `0` | `（JSON 之摘要列·略）` | 142 |
| `58` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 3.5 <O>/f8_<態>_35.json` | `0` | `0` | `⇒ 紅 []；rc 0` | 184 |
| `59` | `python3 verify/probes/probe_WG9349_k9296.py run <repo> 0.0 <O>/f8_<態>_00.json` | `0` | `0` | `⇒ 紅 []；rc 0` | 140 |
| `60` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 3.5 on <O>/parity35_<態>.json` | `0` | `0` | `⇒ rc 0（不符 0 項）` | 413 |
| `61` | `python3 verify/probes/probe_WG9345_screen.py parity <repo> 0.0 on <O>/parity00_<態>.json` | `0` | `0` | `⇒ rc 0（不符 0 項）` | 303 |
| `62` | `python3 verify/probes/probe_WG9387_k961h.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 4 |
| `63` | `python3 verify/probes/probe_WG9387_k961h.py wiring <repo> 34736ab` | `0` | `0` | `⇒ 紅 []；rc 0` | 3 |
| `64` | `python3 verify/probes/probe_WG9387_k961h.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 343 |
| `65` | `python3 verify/probes/probe_WG9388_k961s3.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `66` | `python3 verify/probes/probe_WG9388_k961s3.py wiring <repo> fd88f64` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `67` | `python3 verify/probes/probe_WG9353_endmerge.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 1175 |
| `68` | `python3 verify/probes/probe_WG9354_endcontest.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 1174 |
| `69` | `python3 verify/probes/probe_WG9389_trialstop.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `70` | `python3 verify/probes/probe_WG9389_trialstop.py wiring <repo> 929ea20` | `0` | `0` | `⇒ 紅 []；rc 0` | 131 |
| `71` | `python3 verify/probes/probe_WG9389_trialstop.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 432 |
| `72` | `python3 verify/probes/probe_WG9390_k961r.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `73` | `python3 verify/probes/probe_WG9390_k961r.py wiring <repo> 2aa6302` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `74` | `python3 verify/probes/probe_WG9390_k961r.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 330 |
| `75` | `python3 verify/probes/probe_WG9391_k980x.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `76` | `python3 verify/probes/probe_WG9391_k980x.py wiring <repo> a8657c4` | `0` | `0` | `⇒ 紅 []；rc 0` | 40 |
| `77` | `python3 verify/probes/probe_WG9391_k980x.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 669 |
| `78` | `python3 verify/probes/probe_WG9392_k980g.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 7 |
| `79` | `python3 verify/probes/probe_WG9392_k980g.py wiring <repo> 56c77fd` | `0` | `0` | `⇒ 紅 []；rc 0` | 4 |
| `80` | `python3 verify/probes/probe_WG9392_k980g.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 345 |
| `81` | `python3 verify/probes/probe_WG9393_endall.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `82` | `python3 verify/probes/probe_WG9393_endall.py wiring <repo> cf1b415` | `0` | `0` | `⇒ 紅 []；rc 0` | 4 |
| `83` | `python3 verify/probes/probe_WG9393_endall.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 345 |
| `84` | `python3 verify/probes/probe_WG9352_endblock.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 340 |
| `85` | `python3 verify/probes/probe_WG9394_k9615.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `86` | `python3 verify/probes/probe_WG9394_k9615.py wiring <repo> 5d2a283` | `0` | `0` | `⇒ 紅 []；rc 0` | 4 |
| `87` | `python3 verify/probes/probe_WG9394_k9615.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 337 |
| `88` | `python3 verify/probes/probe_WG9395_k960.py selftest <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 2 |
| `89` | `python3 verify/probes/probe_WG9395_k960.py wiring <repo> d4928d4` | `0` | `0` | `⇒ 紅 []；rc 0` | 9 |
| `90` | `python3 verify/probes/probe_WG9395_k960.py run <repo>` | `0` | `0` | `⇒ 紅 []；rc 0` | 334 |
| `91` | `python3 verify/probes/probe_order_preflight.py --selftest` | `0` | `0` | `判別力造：✅ 全數成立 ⇒ 本器非恆綠亦非恆紅` | 2 |

## 三、`#56`〜`#61` 之落檔（`git hash-object`）

- `f8_post_00.json` ＝ `884e91714a79288406faa4def6518847de36de39`（`8249` B）
- `f8_post_35.json` ＝ `47683d1cb284ad814034d7ac7f3cd464d66c6e3f`（`8109` B）
- `k6s3_post_00.json` ＝ `8a2b470aeb8a8d587cf69bd57cbbb370a2c44442`（`9869` B）
- `k6s3_post_35.json` ＝ `ee317f112337888fb90b9590eab03fe6ffc1c41d`（`18053` B）
- `parity00_post.json` ＝ `896854f7c12f9a1cf42a2c02268344744c0db535`（`284` B）
- `parity35_post.json` ＝ `cdf18d228738b580cf7201bf320973f1af2f5964`（`8683` B）

`F8` 之落檔 ＝ 前基準 `d4928d4…` 之值（3.5 m `47683d1c…`、0 m `884e9171…`·逐位同）⇒ 本案配地⛔ 變。`k6s3` 之二落檔之 `F36 diff`：`post_35` 對 `post_00` ⇒ `全比相異 44 項`（對照組·＝ 前基準）、`post_35` 對自身 ⇒ `全比相異 0 項`。`k6s3` 之檔含耗時之欄（`hash-object` ⛔ 比）；`parity` 之落檔含 `HEAD` 之值（⛔ 比）。`P0` 之列（`W-G.9-395` 補令二閘 `8‴` 之受詞）：`75／75`、`74／74`、`35／35`、`31／31`（二）、`29／29`、`16／16`、`14／14`、`22／22`、`17／17` 皆見。

## 四、`pip freeze` 之全文

````text
altair==6.3.0
anyio==4.15.1
argcomplete==3.1.4
attrs==26.1.0
blinker==1.7.0
certifi==2026.10.18
charset-normalizer==3.5.2
click==8.5.0
cryptography==41.0.7
dbus-python==1.3.2
distro==1.9.0
et_xmlfile==2.0.0
ezdxf==1.4.5
fonttools==4.67.0
geopandas==1.2.0
h11==0.16.0
httplib2==0.20.4
idna==3.20
itsdangerous==2.2.0
Jinja2==3.1.6
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
launchpadlib==1.11.0
lazr.restfulclient==0.14.6
lazr.uri==1.0.6
MarkupSafe==3.0.4
narwhals==2.27.1
numpy==2.4.6
oauthlib==3.2.2
openpyxl==3.1.5
packaging==24.0
pandas==3.0.6
pillow==12.3.0
plotly==7.1.0
protobuf==7.36.2
pyarrow==26.0.0
pydeck==0.9.3
PyGObject==3.48.2
PyJWT==2.7.0
pyogrio==0.13.0
pyparsing==3.1.1
pyproj==3.7.2
python-apt==2.7.7+ubuntu5.3
python-dateutil==2.9.0.post0
python-multipart==0.0.32
PyYAML==6.0.1
referencing==0.37.0
requests==2.34.2
rpds-py==2026.9.1
shapely==2.2.0
six==1.16.0
starlette==1.9.0
streamlit==1.66.0
streamlit-plotly-events==0.0.6
toml==0.10.2
typing_extensions==4.16.0
urllib3==2.8.0
uvicorn==0.54.0
wadllib==1.3.6
watchdog==6.0.0
websockets==17.2
xlrd==2.0.2
xmltodict==0.13.0
yq==3.1.0
````
