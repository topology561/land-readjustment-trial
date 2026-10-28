# W-P.005　重劃後三圖層（公告分配地籍線·分配後歸戶圖·重劃後地價圖）＋ 暫編→正式地號對照表

- **題**：依 KL 2026-10-28 23:31、23:37 之答（`出圖線/KL答覆/2026-10-28_2331.md`、`2026-10-28_2337.md`），於 DXF 加重劃後之三圖層（合重劃前三圖層為一檔六圖層）、出「暫編 → 正式地號對照表」（程式依 S 型自動編預設、承辦人得改、重號或缺號即停）與重劃後之顏色對照表。
- **發單端改分**（記於 `出圖線/交接.md`）：附表 13、24 移 `W-P.006`（以本單之對照表之正式地號為據；KL 23:31 問二、問三之答屆時納之）。
- **範圍**：唯新增 `plots/alloc_state.py`、`plots/post_maps.py`、`verify/plots/check_W-P005.py`、`verify/plots/mutate_W-P005.py`、`verify/plots/preview_W-P005.py`、`docs/出圖/W-P.005_重劃後三圖層與地號對照表.md`；⛔ 改任何既有之檔（含本線既有之 `plots/*.py`·唯 `import`）；⛔ 改 `requirements.txt`；⛔ 新套件。
- **授權（逐字）**：
  - KL 2026-10-23 17:31「1. 是　2. 以手冊（拾參）所附的圖例為主」；17:48「圖就出DXF或DWG(圖層含重劃前地籍線、公告分配地籍線、重劃前歸化圖、分配後歸戶圖、地價圖)即可，所有的標題及排版由使用者編輯。…」（README 第一節）。
  - KL 2026-10-28 10:48「是」（W-P.004 定版·下一批須調配終態者先做格式）。
  - KL 2026-10-28 23:31「1. 問1：重劃範圍有可能會跨區，…故A、C 2區內的分配後土地都會是同一個地段名，S型先看大範圍，例如C區範圍位置若比A區更往東北方，則新地段1地號於C區內依程式自動依 S 型編定，編定後再至C區內部依S型編列」「4. 問4：乙」「5. 乙，加原地主分得之地照一般歸戶上色」。
  - KL 2026-10-28 23:37「保留「暫編 → 正式地號對照表」」。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `bd7da4dab47ae3dc7eb5249c1a9828eefd6f9434`（自 `20e03bf` 前進·含 `W-G.9-398`）；`wip/plots` ＝ `9a3cb61bd5397ecaca62ca30b5c32d57a03b8fd8`（未含 `bd7da4d` ⇒ 工項 1 之合併必做；發單端試併無衝突·得 `e22c2dc`〔本地〕）。
- **側支**：`verify/W-P.005-post-maps`（自 `wip/plots` 出）。單號 `W-P.005` 經 `git grep -F` 證未占用為單或分支（主倉 `bd7da4d`＋`9a3cb61` 無；佇列唯見請示與答覆之文字）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具·核心線 `order` ＝ `W-G.9-398_補令三`）。

## §一　所據

1. **手冊**（`參考/市地重劃作業手冊.txt`）第 3833〜3857 列：作業圖「按分配之位置及面積…劃定坵塊，加註分配寬度及深度後編定重劃後地號」；「以調整後之段界為範圍，用整數連續編列」；「重劃後之地號僅編列母號，不編子號，必須編子號時，應依照「地籍測量實施規則」之規定編列」；「每一段之地號，應自右而左，從上而下，依「S」型順序，自 1 起依序編列之，其起迄以不超過五位數為原則，並注意其中不得重號」。
2. **KL 之答**：見引言。問五之監看窗之讀（KL 未異議）：抵費地自成一色並註「抵費地」；道路、公園不填色、只畫界線；縣、國以原所有權人身分分得之地照一般地主之歸戶號與歸戶色。
3. **配地結果之來源**（發單端實查）：核心線之階段二（調配之新模組·`進度表.md` 2-3〜2-6）⬜ 未成；舊七級調配引擎（`verify/wf_f0`〜`f4`）於主線現態之 `wf_f0.compute` 報「GSA 錨檢破」而停（`G006` 等錨鍵未被評估·K-6 段三之後未重錨·發單端於 `20e03bf` 與 `bd7da4d` 皆實測）。⇒ 本單取**階段一之終**（段三後·調配之前）：依 `verify/run_verification.py` 之 `main` 之序呼叫既有之管線（`load_snapshot → harvest → build_pipeline → build_param_table → build_ownership → build_build_parcels → run_corner_pk_k6b → run_step_g〔eff_min_build_by_blk＝{}〕`），取 `g_rows`（含 `cut_coords`）。「推進側別」＝「抵費地」者為抵費地（同 `app.py` 之 `export_allocated_dxf`），調配池於此階段即以抵費地示之。新模組入主線後，唯改 `plots/alloc_state.py`（本線之後單）。
4. **既有之函式**（唯讀·`import`）：`plots/prelim_maps.py` 之 `load_cadastre`、`households`、`household_members`、`distinct_palette`、`landno_key`、`LAYERS`、`TEXT_STYLE`、`TEXT_HEIGHT`、`CASE_PARAMS`、`SourceError`；`plots/owner_index.py` 之 `load_strokes`、`number_households`；`verify/case_params_UC9898.json` 之 `財務接線_v3.後街廓_面積單價`。
5. **內容之判斷**（依手冊、KL 之答或資料；未經 KL 逐項確認者於第一版併呈）：
   - 暫編：可分配之街廓之宗，沿正面臨路線由起點（左·p1）而迄點（右·p2）編「街廓-兩位序號」（R1-01…·抵費地居其位·問一乙原述之式）；道路、公園以其圖上之編號（RD1、G1…）。
   - 預設地號（S 型·問一甲之通式）：區 ＝ 全部街廓之多邊形外擴 0.01 m 之相連者；區依形心先北後南（同者先東）；區內之可分配之街廓依形心先北後南（同者先東），第 1、3、5…個自東而西、第 2、4、6…個自西而東（正面臨路線正東西向者以先北後南代之）；街廓內之序依各宗之代表點沿正面臨路線之投影；道路、公園續編於全部之宗之後（依區之序，區內依形心先北後南、同者先東）。**區內 S 型之列之讀法未經 KL 逐項確認 ⇒ 第一版附編號之示意請 KL 確認**（`2026-10-28_2331.md` 監看窗之讀第 1 點、`_2337.md` 第 3 點）。
   - 對照表之檢查（KL 23:37）：暫編之集合不符、正式地號空白、非「1〜5 位之母號」或「母號-子號」、重號 ⇒ 停止產出（⛔ 自補）。
   - 公告分配地籍線之註記（問四乙）：分配地 ＝ 地號／面積（二位）／「寬」＋引擎之宗地寬度（二位·垂直於宗地分配線·判畸零所用之 W）／「深」＋面積 ÷ 寬（二位）；抵費地與道路、公園 ＝ 地號／面積。寬與深之量法於第一版併呈。
   - 面積二位四捨五入為 0.00 之列（本案 `R1-抵費地-2`·0.0046 ㎡）不成宗，列於配地結果之「略」並印之。
   - 分配後歸戶圖（問五乙＋）：分配地之填色與歸戶號 ＝ 其原地號於重劃前歸戶圖之色與號；抵費地填灰（160,160,160）並註「抵費地」；道路、公園唯畫界線。
   - 重劃後地價圖：分配地與抵費地依其街廓之重劃後單價（全精度存值·註二位·同附表 19）填色，一價一色；道路、公園不填色、不註。
   - 對土地之影響：無（唯圖面之呈現）。

## §二　規格

1. **新增 `plots/alloc_state.py`**：逐位元組 ＝ 附錄丁。`python plots/alloc_state.py --out <O> --setback 0 --setback 3.5`（約 10 分鐘）⇒ `配地結果_退縮0m.json`、`配地結果_退縮3.5m.json`。
2. **新增 `plots/post_maps.py`**：逐位元組 ＝ 附錄戊。`python plots/post_maps.py --state <O>/配地結果_退縮<t>m.json --pre-dxf <P>/重劃前圖.dxf --moedict <json> --out <O> [--map <xlsx>]`（約 45 秒）⇒ `公告圖_退縮<t>m.dxf`（六圖層）、`地號對照表_退縮<t>m.xlsx`、`顏色對照表_重劃後_退縮<t>m.xlsx`。
3. **新增 `verify/plots/check_W-P005.py`**：逐位元組 ＝ 附錄甲（V0〜V7·獨立於 `plots/`·S 型以形心之異法重導）。
4. **新增 `verify/plots/mutate_W-P005.py`**：逐位元組 ＝ 附錄乙（Ⓐ〜Ⓔ）。
5. **新增 `verify/plots/preview_W-P005.py`**：逐位元組 ＝ 附錄丙。
6. **新增 `docs/出圖/W-P.005_重劃後三圖層與地號對照表.md`**：逐位元組 ＝ 附錄己。
7. 發單端之原型（暫存·⛔ 入倉·於 `9a3cb61` 試併 `bd7da4d` 之上）已依附錄實作，實得：
   - `alloc_state`：退縮 0 m 宗 35（分配地 29、抵費地 6）、退縮 3.5 m 宗 34（28、6）；二者之略皆 `['R1-抵費地-2']`；單跑 `--setback 3.5` 之 JSON 與合跑者逐位元組同。
   - `post_maps`（3.5 m）：公設 5；地號 1〜39（R1-05→1 … R1-01→5、R2-01→6 … R2-07→12、R3-01→13 … R3-06→18、R4-01→19 … R4-03→21、R5-07→22 … R5-01→28、R6-06→29 … R6-01→34、RD1→35、RD2→36、RD4→37、RD3→38、G1→39）；0 m 地號 1〜40（R3 有 7 宗）；重劃後地價三值 68621.38、72433.68、76245.98。
   - `check_W-P005` 16/16（二退縮各 V0〜V7）；`mutate_W-P005` 成果綠、Ⓐ 紅（V2〜V7）、Ⓑ 紅（V3、V4）、Ⓒ 紅（V4）、Ⓓ 紅（V5）、Ⓔ 紅（V6）；另於拋棄式之複本刪 `read_map` 之重號之檢查 ⇒ V7 紅（判別力）。
   - 環境：系統之 numpy 2.5 使 `verify/stepg_pipeline.py` 之 `np.cross`（二維）報錯 ⇒ 以 `python3 -m venv --system-site-packages <venv>`、`<venv>/bin/pip install -r requirements.txt 'numpy<2.3'`（得 2.2.6）跑之（倉外·⛔ 改 `requirements.txt`）。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.005-post-maps`；`git merge --no-edit origin/wip/s1-endpart`（本單出時主線 `bd7da4d`·必有合併之 commit）；有衝突即停機。
2. **程式**：§二 1〜6。附錄之取用法：自本單擷取該附錄之開欄（甲〜戊為三個反引號加 `python`；己為四個反引號加 `markdown`）與其閉欄（同數之反引號）間之文字，末尾一換行；bytes 與 sha256 須合：
   - 甲 `verify/plots/check_W-P005.py`：20390 bytes·`2927307e0bcf37199a81537a11139a865aa057e1f85a672de2db8ecb8462fe06`
   - 乙 `verify/plots/mutate_W-P005.py`：5077 bytes·`6f19c48d3a377335dc512e495dfdf4904a927599888b0f71db62a44affda1db2`
   - 丙 `verify/plots/preview_W-P005.py`：4581 bytes·`2d0bc1c522e0ba7f249ac83f24eafd9d74aa8543db375a190f5dcea6a142ee66`
   - 丁 `plots/alloc_state.py`：6807 bytes·`e91241e9d29890e72523ca583f4582ec5319e5b47b2060f50678c69ed62321ab`
   - 戊 `plots/post_maps.py`：17742 bytes·`f8e4ac4143519480a54f82588885789a61a8789bf531bbfba6d3fa42253bdf34`
   - 己 `docs/出圖/W-P.005_重劃後三圖層與地號對照表.md`：3005 bytes·`9dfeb30a1c154c228f69e988cb98d2cc6513ff8d470b78e809f52c6475441ca8`
   不合即停機上呈；⛔ 改一字。`python -m py_compile` 五 `.py` 皆過。
3. **量測**（`<py>` ＝ §二 7 之 venv 之直譯器）：
   - `<py> plots/fetch_moedict.py <M>`；`<py> plots/prelim_maps.py --out <P> --moedict <M>/dict-revised.json`；
   - `<py> plots/alloc_state.py --out <O> --setback 0 --setback 3.5`（印如 §二 7）；
   - 二退縮各 `<py> plots/post_maps.py --state <O>/配地結果_退縮<t>m.json --pre-dxf <P>/重劃前圖.dxf --moedict <M>/dict-revised.json --out <O>`（印之地號之序須 ＝ §二 7）；
   - `<py> verify/plots/check_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json 0 3.5` ⇒ 16 項皆 PASS、結束碼 0。
   - 另照舊：`check_W-P001.py`（12/12）、`check_W-P002.py`（8/8）、`check_W-P003.py`（8/8）、`check_W-P004.py`（8/8）——證既有之輸出未受擾（主線合併後亦然）。
4. **故意錯誤之測**：`<py> verify/plots/mutate_W-P005.py <O> <P>/重劃前圖.dxf <M>/dict-revised.json <拋棄式之工作目錄>` ⇒ 成果綠；Ⓐ〜Ⓔ 皆紅（所紅之項記之）；結束碼 0。
5. **差異閘**（README 第四節）：`git diff --name-status <實際併入之主線之 sha（應為 bd7da4d…）> <側支之端>` 每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status 9a3cb61 <側支之端> -- plots verify/plots docs/出圖` 唯 §二 之六新檔（皆 `A`）；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **預覽 PNG**：`<py> verify/plots/preview_W-P005.py <O> <PNG 目錄> 0 3.5`，其二輸出入佇列之 `出圖線/成果/`。
7. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
8. **回報**：`出圖線/reports/W-P.005_回報.md`（各工項之實測、量測之全輸出、故意錯誤之表、差異閘與對照組、合併之 sha、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲〜己之 bytes 或 sha256 不合；或 V0〜V7 於成果不過而非程式之誤；或 §二 7 之地號之序不合（主線前進致配地變者亦停·記其差）。
3. `plots/alloc_state.py` 或 `plots/post_maps.py` 報 `SourceError` 或配地流程之 `RuntimeError`——⛔ 自擬填法、⛔ 設 `WV_BAKE`。
4. 須改任何既有之檔、或須新套件（numpy 之版本唯限於倉外之 venv）。
5. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P005.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005：重劃後三圖層與地號對照表之量測。
獨立於 plots/：⛔ import 之（V7 唯以子行程呼叫 plots/post_maps.py 之命令列）；期望取自 配地結果_退縮*.json
（plots/alloc_state.py 之輸出·即配地流程之 g_rows）、重劃前圖.dxf（W-P.001／002 定版之三圖層）、
verify/case_params_UC9898.json、KL 2026-10-28 23:31、23:37 之答。

命令列：python verify/plots/check_W-P005.py <成果目錄> <重劃前圖.dxf> <dict-revised.json> <退縮…>
  成果目錄 ＝ plots/alloc_state.py 與 plots/post_maps.py 之 --out（同一目錄）。
任一不過 ⇒ 結束碼 1。
V0 各檔皆在、可讀；V1 圖層（恰六＋系統二）、重劃前三圖層之圖元與重劃前圖逐一同；
V2 公告分配地籍線之宗（數、形、面積、各街廓密接而無重疊、略之列皆 0）；
V3 地號與註記（每宗恰一地號、無重號、＝ 對照表之正式地號；面積、寬、深之值）；
V4 S 型之預設編定（異法重導：形心·區·街廓之序·交替·公設續編於後；1〜N 連號）；
V5 分配後歸戶圖（原地主之地 ＝ 其重劃前之歸戶色與歸戶號；抵費地一色並註「抵費地」；公設不填色、只畫界線）；
V6 重劃後地價圖（街廓之價·二位；一價一色；公設不填色）；
V7 對照表之用（改號即帶入圖；重號、空白 ⇒ 停止而無輸出）與顏色對照表。
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CASE = os.path.join(REPO, "verify", "case_params_UC9898.json")
POST_MAPS = os.path.join(REPO, "plots", "post_maps.py")
PRE_LAYERS = ("重劃前地籍線", "重劃前歸戶圖", "重劃前地價圖")
L_CAD, L_OWN, L_PRICE = "公告分配地籍線", "分配後歸戶圖", "重劃後地價圖"
SYS_LAYERS = {"0", "Defpoints"}
OFFSET_WORD = "抵費地"
MAP_SHEET = "地號對照表"
MAP_HEAD = ("暫編", "街廓", "類別", "配地之暫編地號", "預設地號（S 型）", "正式地號", "面積（㎡）")
NO_RE = re.compile(r"^\d+(-\d+)?$")
TOL_SHAPE = 1e-4      # 多邊形之對稱差（㎡）
TOL_TILE = 0.05       # 一街廓之宗之和與街廓面積（㎡）
FMT = {"dxf": "公告圖_退縮{}m.dxf", "map": "地號對照表_退縮{}m.xlsx",
       "color": "顏色對照表_重劃後_退縮{}m.xlsx", "state": "配地結果_退縮{}m.json"}


def rhu(x, nd=2):
    return Decimal(repr(float(x))).quantize(Decimal(1).scaleb(-nd), rounding=ROUND_HALF_UP)


def s2(x):
    return f"{rhu(x):.2f}"


def nkey(s):
    a = str(s).split("-")
    return (int(a[0]), int(a[1]) if len(a) > 1 else 0)


class Ctx:
    pass


def load(out, pre_dxf, tag):
    import ezdxf
    import openpyxl
    from shapely.geometry import Polygon
    c = Ctx()
    c.tag = tag
    c.p = {k: os.path.join(out, v.format(tag)) for k, v in FMT.items()}
    c.state = json.load(open(c.p["state"], encoding="utf-8"))
    c.doc = ezdxf.readfile(c.p["dxf"])
    c.pre = ezdxf.readfile(pre_dxf)
    ws = openpyxl.load_workbook(c.p["map"], data_only=True)[MAP_SHEET]
    rows = list(ws.iter_rows(values_only=True))
    c.map_head = tuple(rows[0][:len(MAP_HEAD)])
    c.map = [r for r in rows[1:] if r and r[0] is not None and r[1] is not None]
    c.color = openpyxl.load_workbook(c.p["color"], data_only=True)
    c.msp = c.doc.modelspace()

    def polys(msp, layer):
        return [(Polygon([(p[0], p[1]) for p in e.get_points("xy")]), e)
                for e in msp.query(f'LWPOLYLINE[layer=="{layer}"]')]

    def texts(msp, layer):
        from shapely.geometry import Point
        return [(Point(e.dxf.align_point[0], e.dxf.align_point[1]), e.dxf.text)
                for e in msp.query(f'TEXT[layer=="{layer}"]')]

    def hatches(msp, layer):
        out_ = []
        for e in msp.query(f'HATCH[layer=="{layer}"]'):
            if len(e.paths) != 1:
                raise AssertionError("HATCH 之邊界非一")
            out_.append((Polygon([(v[0], v[1]) for v in e.paths[0].vertices]), tuple(e.rgb)))
        return out_
    c.polys, c.texts, c.hatches = polys, texts, hatches
    blocks = c.state["街廓"]
    c.alloc = {k for k, v in blocks.items() if "宗地分配線方向" in v}
    c.public = sorted(k for k in blocks if k not in c.alloc)
    c.lots = c.state["宗"]
    c.post_price = {b: d["單價_元每m2"] for b, d in
                    json.load(open(CASE, encoding="utf-8"))["財務接線_v3"]["後街廓_面積單價"].items()}
    return c


def _sig(e):
    t = e.dxftype()
    if t == "LWPOLYLINE":
        return (t, e.dxf.layer, tuple((round(p[0], 6), round(p[1], 6)) for p in e.get_points("xy")))
    if t == "TEXT":
        return (t, e.dxf.layer, e.dxf.text, round(e.dxf.align_point[0], 6), round(e.dxf.align_point[1], 6))
    if t == "HATCH":
        return (t, e.dxf.layer, tuple(e.rgb),
                tuple((round(v[0], 6), round(v[1], 6)) for v in e.paths[0].vertices))
    return (t, e.dxf.layer)


def _match(c):
    """配地結果之每宗（與公設之區塊）⇒ 公告分配地籍線之多邊形（對稱差 ≤ TOL_SHAPE）。"""
    from shapely.geometry import Polygon
    ps = c.polys(c.msp, L_CAD)
    want = [(x["配地暫編"], x, Polygon(x["多邊形"])) for x in c.lots]
    want += [(b, None, Polygon(c.state["街廓"][b]["多邊形"])) for b in c.public]
    got = {}
    used = set()
    for key, x, wp in want:
        hit = [i for i, (p, _) in enumerate(ps) if p.symmetric_difference(wp).area <= TOL_SHAPE]
        if len(hit) != 1 or hit[0] in used:
            return None, f"{key} 於 {L_CAD} 之多邊形 {len(hit)} 個"
        used.add(hit[0])
        got[key] = (x, ps[hit[0]][0])
    if len(used) != len(ps):
        return None, f"{L_CAD} 有多出之多邊形 {len(ps) - len(used)} 個"
    return got, None


def v0(c):
    return []


def v1(c):
    bad = []
    names = {ly.dxf.name for ly in c.doc.layers}
    want = SYS_LAYERS | set(PRE_LAYERS) | {L_CAD, L_OWN, L_PRICE}
    if names != want:
        bad.append(f"圖層 {sorted(names ^ want)}")
    for ly in PRE_LAYERS:
        a = sorted(_sig(e) for e in c.msp if e.dxf.layer == ly)
        b = sorted(_sig(e) for e in c.pre.modelspace() if e.dxf.layer == ly)
        if a != b or not a:
            bad.append(f"{ly} 之圖元與重劃前圖不同（{len(a)}／{len(b)}）")
    for e in c.msp:
        if e.dxf.layer in SYS_LAYERS:
            bad.append(f"系統圖層 {e.dxf.layer} 上有圖元")
            break
    return bad


def v2(c):
    from shapely.ops import unary_union
    from shapely.geometry import Polygon
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    n = len(c.polys(c.msp, L_CAD))
    if n != len(c.lots) + len(c.public):
        bad.append(f"宗數 {n} ≠ {len(c.lots)}＋{len(c.public)}")
    for x in c.lots:
        if s2(Polygon(x["多邊形"]).area) != s2(x["面積"]):
            bad.append(f"{x['配地暫編']} 之面積 {x['面積']} ≠ 圖 {Polygon(x['多邊形']).area:.4f}")
    for b in sorted(c.alloc):
        ps = [got[x["配地暫編"]][1] for x in c.lots if x["街廓"] == b]
        bp = Polygon(c.state["街廓"][b]["多邊形"])
        s = sum(p.area for p in ps)
        u = unary_union(ps)
        if abs(s - bp.area) > TOL_TILE or u.symmetric_difference(bp).area > TOL_TILE:
            bad.append(f"{b}：宗之和 {s:.3f}、聯集之差 {u.symmetric_difference(bp).area:.4f}、街廓 {bp.area:.3f}")
    for d in c.state["略"]:
        if s2(d["幾何面積"]) != "0.00":
            bad.append(f"略之列 {d['配地暫編']} 之面積非 0")
    return bad


def _map_rows(c):
    if c.map_head != MAP_HEAD:
        raise AssertionError(f"對照表之表頭 {c.map_head}")
    return {r[3] if r[3] is not None else r[0]: r for r in c.map}


def v3(c):
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    try:
        mr = _map_rows(c)
    except AssertionError as ex:
        return [str(ex)]
    if len(mr) != len(got):
        bad.append(f"對照表 {len(mr)} 列 ≠ {len(got)} 宗")
    tx = c.texts(c.msp, L_CAD)
    seen = {}
    for key, (x, poly) in got.items():
        inside = [s for pt, s in tx if poly.contains(pt)]
        nos = [s for s in inside if NO_RE.match(s)]
        if len(nos) != 1:
            bad.append(f"{key} 之地號之註記 {nos}")
            continue
        no = nos[0]
        if no in seen:
            bad.append(f"地號 {no} 重號：{seen[no]}、{key}")
        seen[no] = key
        r = mr.get(key)
        if r is None or str(r[5]) != no:
            bad.append(f"{key} 之地號 {no} ≠ 對照表 {None if r is None else r[5]}")
        area = x["面積"] if x else rhu(poly.area)
        want = [no, s2(area)]
        if x and x["類別"] == "分配地":
            w = rhu(x["宗地寬度"])
            d = (Decimal(repr(float(x["面積"]))) / w).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            want += [f"寬{w:.2f}", f"深{d:.2f}"]
        if sorted(inside) != sorted(want):
            bad.append(f"{key} 之註記 {inside} ≠ {want}")
    if len(tx) != sum(4 if (x and x["類別"] == "分配地") else 2 for x, _ in got.values()):
        bad.append(f"{L_CAD} 之文字數不合（{len(tx)}）")
    return bad


def _expected_order(c):
    """異法：形心；街廓之序 ＝ 形心之 y 降、x 降；第奇個街廓自東而西（形心 x 降）、第偶個自西而東；公設續後。"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    blocks = c.state["街廓"]
    P = {k: Polygon(v["多邊形"]) for k, v in blocks.items()}
    u = unary_union([p.buffer(0.01) for p in P.values()])
    regs = list(getattr(u, "geoms", [u]))
    regs.sort(key=lambda g: (-g.centroid.y, -g.centroid.x))
    seq, pubs = [], []
    for g in regs:
        mem = [k for k in P if g.contains(P[k].centroid) or g.contains(P[k].representative_point())]
        al = sorted([k for k in mem if k in c.alloc], key=lambda k: (-P[k].centroid.y, -P[k].centroid.x))
        for i, k in enumerate(al):
            lots = [x for x in c.lots if x["街廓"] == k]
            lots.sort(key=lambda x: Polygon(x["多邊形"]).centroid.x, reverse=(i % 2 == 0))
            seq += [x["配地暫編"] for x in lots]
        pubs += sorted([k for k in mem if k not in c.alloc], key=lambda k: (-P[k].centroid.y, -P[k].centroid.x))
    return seq + pubs


def v4(c):
    bad = []
    try:
        mr = _map_rows(c)
    except AssertionError as ex:
        return [str(ex)]
    exp = _expected_order(c)
    dflt = {k: r[4] for k, r in mr.items()}
    want = {k: str(i) for i, k in enumerate(exp, start=1)}
    if {k: str(v) for k, v in dflt.items()} != want:
        diff = [(k, dflt.get(k), want.get(k)) for k in exp if str(dflt.get(k)) != want[k]][:6]
        bad.append(f"預設地號 ≠ S 型之序：{diff}")
    got, err = _match(c)
    if err:
        return bad + [err]
    tx = c.texts(c.msp, L_CAD)
    on_map = {}
    for key, (_x, poly) in got.items():
        nos = [s for pt, s in tx if poly.contains(pt) and NO_RE.match(s)]
        on_map[key] = nos[0] if len(nos) == 1 else None
    if c.with_default and on_map != want:
        bad.append("圖上之地號 ≠ S 型之預設（未給對照表者）")
    return bad


def v5(c):
    from shapely.geometry import Polygon
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    pre = c.pre.modelspace()
    pre_poly = {}
    for p, _e in c.polys(pre, PRE_LAYERS[0]):
        labs = [s for pt, s in c.texts(pre, PRE_LAYERS[0]) if p.contains(pt)]
        if len(labs) == 1:
            pre_poly[labs[0]] = p
    pre_h = c.hatches(pre, PRE_LAYERS[1])
    pre_t = c.texts(pre, PRE_LAYERS[1])
    hh = c.hatches(c.msp, L_OWN)
    ht = c.texts(c.msp, L_OWN)
    outl = c.polys(c.msp, L_OWN)
    owner_colors = set()
    offs = set()
    n_h = 0
    for key, (x, poly) in got.items():
        mine = [col for hp, col in hh if hp.symmetric_difference(poly).area <= TOL_SHAPE]
        labs = [s for pt, s in ht if poly.contains(pt)]
        if x is None:
            if mine or labs:
                bad.append(f"公設 {key} 有填色或註記")
            if len([1 for p, _ in outl if p.symmetric_difference(poly).area <= TOL_SHAPE]) != 1:
                bad.append(f"公設 {key} 於 {L_OWN} 無界線")
            continue
        n_h += 1
        if len(mine) != 1 or len(labs) != 1:
            bad.append(f"{key} 之填色 {len(mine)}、註記 {labs}")
            continue
        if x["類別"] == "抵費地":
            offs.add(mine[0])
            if labs[0] != OFFSET_WORD:
                bad.append(f"{key} 之註記 {labs[0]}")
            continue
        pp = pre_poly.get(x["原地號"])
        if pp is None:
            bad.append(f"{key} 之原地號 {x['原地號']} 不在重劃前圖")
            continue
        pc = [col for hp, col in pre_h if hp.symmetric_difference(pp).area <= TOL_SHAPE]
        pl = [s for pt, s in pre_t if pp.contains(pt)]
        if pc != [mine[0]] or pl != [labs[0]]:
            bad.append(f"{key}（原 {x['原地號']}）：色 {mine[0]}／歸戶號 {labs[0]} ≠ 重劃前 {pc}／{pl}")
        owner_colors.add(mine[0])
    if len(offs) > 1:
        bad.append(f"抵費地之色不一：{offs}")
    if offs & owner_colors or offs & {col for _, col in pre_h}:
        bad.append("抵費地之色與某戶之色同")
    if len(hh) != n_h or len(ht) != n_h:
        bad.append(f"{L_OWN} 之填色 {len(hh)}、註記 {len(ht)} ≠ {n_h}")
    # 相鄰之不同戶異色
    lots = [(x, poly) for x, poly in got.values() if x and x["類別"] == "分配地"]
    for i, (a, pa) in enumerate(lots):
        for b, pb in lots[i + 1:]:
            if a["歸戶"] != b["歸戶"] and pa.buffer(0.05).intersects(pb):
                ca = [col for hp, col in hh if hp.symmetric_difference(pa).area <= TOL_SHAPE]
                cb = [col for hp, col in hh if hp.symmetric_difference(pb).area <= TOL_SHAPE]
                if ca == cb:
                    bad.append(f"相鄰之異戶 {a['配地暫編']}、{b['配地暫編']} 同色")
    return bad


def v6(c):
    bad = []
    got, err = _match(c)
    if err:
        return [err]
    hh = c.hatches(c.msp, L_PRICE)
    ht = c.texts(c.msp, L_PRICE)
    col_of = {}
    n = 0
    for key, (x, poly) in got.items():
        mine = [col for hp, col in hh if hp.symmetric_difference(poly).area <= TOL_SHAPE]
        labs = [s for pt, s in ht if poly.contains(pt)]
        if x is None:
            if mine or labs:
                bad.append(f"公設 {key} 有填色或註記")
            continue
        n += 1
        want = s2(c.post_price[x["街廓"]])
        if len(mine) != 1 or labs != [want]:
            bad.append(f"{key} 之填色 {len(mine)}、註記 {labs} ≠ {want}")
            continue
        col_of.setdefault(want, set()).add(mine[0])
    if any(len(v) != 1 for v in col_of.values()):
        bad.append(f"同價異色：{col_of}")
    cols = [next(iter(v)) for v in col_of.values()]
    if len(set(cols)) != len(cols):
        bad.append("異價同色")
    if len(hh) != n or len(ht) != n:
        bad.append(f"{L_PRICE} 之填色 {len(hh)}、註記 {len(ht)} ≠ {n}")
    return bad


def v7(c):
    bad = []
    # 顏色對照表 ＝ 圖
    ws = c.color[L_OWN]
    rows = list(ws.iter_rows(values_only=True))[1:]
    got, err = _match(c)
    if err:
        return [err]
    hh = c.hatches(c.msp, L_OWN)
    ht = c.texts(c.msp, L_OWN)
    tx = c.texts(c.msp, L_CAD)
    tab = {}
    for _ly, no, col, nos in rows:
        for s in str(nos).split("、"):
            tab[s] = (str(no), col)
    for key, (x, poly) in got.items():
        if x is None:
            continue
        no = [s for pt, s in tx if poly.contains(pt) and NO_RE.match(s)][0]
        col = [cc for hp, cc in hh if hp.symmetric_difference(poly).area <= TOL_SHAPE][0]
        lab = [s for pt, s in ht if poly.contains(pt)][0]
        if tab.get(no) != (lab, "{},{},{}".format(*col)):
            bad.append(f"顏色對照表之 {no} {tab.get(no)} ≠ 圖 {lab}／{col}")
    if c.run_map:
        bad += _map_runs(c)
    return bad


def _map_runs(c):
    """以子行程跑 plots/post_maps.py：①二宗之正式地號互換 ⇒ 圖隨之；②重號、③空白 ⇒ 結束碼非 0 且無輸出。"""
    import openpyxl
    bad = []
    tmp = tempfile.mkdtemp(prefix="wp005_map_")
    try:
        base = [sys.executable, POST_MAPS, "--state", c.p["state"], "--pre-dxf", c.pre_path,
                "--moedict", c.moedict]
        lots = [r for r in c.map if r[2] == "分配地"]
        a, b = lots[0], lots[-1]

        def edited(name, fn):
            wb = openpyxl.load_workbook(c.p["map"])
            ws = wb[MAP_SHEET]
            for row in ws.iter_rows(min_row=2):
                fn(row)
            p = os.path.join(tmp, name)
            wb.save(p)
            return p

        def swap(row):
            if row[0].value == a[0]:
                row[5].value = b[5]
            elif row[0].value == b[0]:
                row[5].value = a[5]

        def dup(row):
            if row[0].value == a[0]:
                row[5].value = b[5]

        def blank(row):
            if row[0].value == a[0]:
                row[5].value = None
        for name, fn, ok_expected in (("swap.xlsx", swap, True), ("dup.xlsx", dup, False),
                                      ("blank.xlsx", blank, False)):
            o = os.path.join(tmp, name + ".out")
            r = subprocess.run(base + ["--out", o, "--map", edited(name, fn)], capture_output=True, text=True)
            made = os.path.exists(os.path.join(o, FMT["dxf"].format(c.tag)))
            if ok_expected:
                if r.returncode != 0 or not made:
                    bad.append(f"改號之對照表未能產出（{r.returncode}）：{r.stderr[-300:]}")
                    continue
                import ezdxf
                from shapely.geometry import Polygon
                d2 = ezdxf.readfile(os.path.join(o, FMT["dxf"].format(c.tag)))
                m2 = d2.modelspace()
                tx = c.texts(m2, L_CAD)
                for row, want in ((a, b[5]), (b, a[5])):
                    x = next(x for x in c.lots if x["配地暫編"] == row[3])
                    poly = Polygon(x["多邊形"])
                    nos = [s for pt, s in tx if poly.contains(pt) and NO_RE.match(s)]
                    if nos != [str(want)]:
                        bad.append(f"改號後 {row[0]} 之地號 {nos} ≠ {want}")
            elif r.returncode == 0 or made:
                bad.append(f"{name} 未停止（結束碼 {r.returncode}、輸出 {made}）")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return bad


CHECKS = [("V0", v0), ("V1", v1), ("V2", v2), ("V3", v3), ("V4", v4), ("V5", v5), ("V6", v6), ("V7", v7)]


def run(out, pre_dxf, moedict, tags, quiet=False, run_map=True, with_default=True):
    fails = []
    for tag in tags:
        try:
            c = load(out, pre_dxf, tag)
        except Exception as ex:   # noqa: BLE001  （V0：缺檔、不可讀）
            if not quiet:
                print(f"FAIL V0 退縮{tag}m：{ex}")
            fails.append(f"V0@{tag}")
            continue
        c.pre_path, c.moedict = pre_dxf, moedict
        c.run_map, c.with_default = run_map, with_default
        for name, fn in CHECKS:
            try:
                bad = fn(c)
            except Exception as ex:   # noqa: BLE001
                bad = [f"{type(ex).__name__}: {ex}"]
            if not quiet:
                print(f"{'PASS' if not bad else 'FAIL'} {name} 退縮{tag}m" + ("" if not bad else "：" + "；".join(bad[:5])))
            if bad:
                fails.append(f"{name}@{tag}")
    return fails


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) < 4:
        print(__doc__)
        return 2
    out, pre_dxf, moedict, *tags = argv
    fails = run(out, pre_dxf, moedict, tags)
    print(f"{'全過' if not fails else '不過 ' + str(fails)}（{len(CHECKS) * len(tags) - len(fails)}/{len(CHECKS) * len(tags)}）")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄乙　`verify/plots/mutate_W-P005.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005 之故意錯誤之測（單 §三 4）：成果須綠、Ⓐ〜Ⓔ 共 5 種變異體須各紅（量測 ＝ check_W-P005.py 之 V0〜V7）。

命令列：python verify/plots/mutate_W-P005.py <成果目錄> <重劃前圖.dxf> <dict-revised.json> <拋棄式之工作目錄>
  成果目錄 ＝ plots/alloc_state.py 與 plots/post_maps.py 之 --out（⛔ 改之；變異體皆寫於工作目錄）。
  唯驗退縮 3.5 m（量測之 V7 之子行程略之·以省時；V7 之判別力另以 Ⓔ 之外之成果之量測證之）。
  Ⓒ、Ⓓ、Ⓔ 掛換 plots/post_maps.py 之函式後重出（於本行程之記憶體中·⛔ 改檔）；Ⓐ、Ⓑ 改成果之複本。
結束碼：成果綠且 5 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P005", os.path.join(HERE, "check_W-P005.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)
TAG = "3.5"


def _copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def _plots():
    sys.path.insert(0, os.path.join(REPO, "plots"))
    import post_maps
    return post_maps


def _dxf(d):
    import ezdxf
    p = os.path.join(d, chk.FMT["dxf"].format(TAG))
    return p, ezdxf.readfile(p)


def mA_drop_lot(d, env):
    """公告分配地籍線漏一宗（刪其界線）。"""
    p, doc = _dxf(d)
    msp = doc.modelspace()
    e = next(iter(msp.query(f'LWPOLYLINE[layer=="{chk.L_CAD}"]')))
    msp.delete_entity(e)
    doc.saveas(p)


def mB_dup_number(d, env):
    """二宗同號（改一宗之地號之註記為他宗之號）。"""
    p, doc = _dxf(d)
    msp = doc.modelspace()
    nos = [t for t in msp.query(f'TEXT[layer=="{chk.L_CAD}"]') if chk.NO_RE.match(t.dxf.text)]
    nos[0].dxf.text = nos[1].dxf.text
    doc.saveas(p)


def _regen(d, env, attr, val):
    pm = _plots()
    orig = getattr(pm, attr)
    setattr(pm, attr, val)
    try:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)
        st = os.path.join(env["out"], chk.FMT["state"].format(TAG))
        shutil.copy(st, d)
        pm.main(["--state", st, "--pre-dxf", env["pre"], "--moedict", env["moe"], "--out", d])
    finally:
        setattr(pm, attr, orig)


def mC_no_alternation(d, env):
    """S 型不交替（每一街廓皆自東而西）。"""
    pm = _plots()
    orig = pm.s_order

    def s_order(doc, ents):
        from shapely.geometry import Polygon
        o = orig(doc, ents)
        pos = {t: i for i, t in enumerate(o)}
        by = {}
        for e in ents:
            by.setdefault(e["街廓"], []).append(e)
        blocks = [b for b in dict.fromkeys(e["街廓"] for e in sorted(ents, key=lambda e: pos[e["暫編"]]))
                  if "宗地分配線方向" in doc["街廓"][b]]
        out = []
        for b in blocks:
            out += [e["暫編"] for e in sorted(by[b], key=lambda e: -Polygon(e["多邊形"]).centroid.x)]
        return out + [t for t in o if t not in set(out)]
    _regen(d, env, "s_order", s_order)


def mD_owner_shift(d, env):
    """原地主之地之色錯一戶（歸戶之色依序錯位）。"""
    pm = _plots()
    orig = pm.owner_scheme

    def owner_scheme(moedict, ents):
        key_of, hh_color, hh_no = orig(moedict, ents)
        ks = list(hh_color)
        cols = [hh_color[k] for k in ks]
        return key_of, dict(zip(ks, cols[1:] + cols[:1])), hh_no
    _regen(d, env, "owner_scheme", owner_scheme)


def mE_pre_price(d, env):
    """重劃後地價圖改用重劃前之區段地價（b 區段 37323）。"""
    pm = _plots()

    def post_prices():
        return {f"R{i}": 37323.0 for i in range(1, 7)}
    _regen(d, env, "post_prices", post_prices)


MUTANTS = [
    ("Ⓐ 公告分配地籍線漏一宗", mA_drop_lot, True),
    ("Ⓑ 二宗同號", mB_dup_number, True),
    ("Ⓒ S 型不交替", mC_no_alternation, False),
    ("Ⓓ 歸戶之色錯位", mD_owner_shift, False),
    ("Ⓔ 重劃後地價圖用重劃前地價", mE_pre_price, False),
]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 4:
        print(__doc__)
        return 2
    out, pre, moe, work = argv
    env = {"out": out, "pre": pre, "moe": moe}
    base = chk.run(out, pre, moe, [TAG], quiet=True, run_map=False)
    print(f"成果：{'綠' if not base else '紅 ' + str(base)}")
    ok = not base
    for i, (name, fn, from_copy) in enumerate(MUTANTS):
        d = os.path.join(work, f"m{i}")
        if from_copy:
            _copy(out, d)
        fn(d, env)
        fails = chk.run(d, pre, moe, [TAG], quiet=True, run_map=False)
        print(f"{name}：{'紅 ' + str(fails) if fails else '綠（未捕）'}")
        ok = ok and bool(fails)
    print("合" if ok else "不合")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄丙　`verify/plots/preview_W-P005.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005 之預覽 PNG（單 §三 6）：自輸出之 DXF 讀回而繪（非自程式之內部資料）。

命令列：python verify/plots/preview_W-P005.py <成果目錄> <PNG 之輸出目錄> <退縮…>
輸出：每一退縮一檔 W-P.005_重劃後三圖層_退縮<t>m.png（左上：公告分配地籍線；右上：重劃後地號之 S 型之序〔示意〕；
      左下：分配後歸戶圖；右下：重劃後地價圖）。
預覽之標題與箭線唯供 KL 一眼辨圖層與編號之序，⛔ 屬 DXF 之內容（DXF 無標題·KL 17:48）。
"""
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

for _f in ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",):
    if os.path.exists(_f):
        font_manager.fontManager.addfont(_f)
        plt.rcParams["font.family"] = font_manager.FontProperties(fname=_f).get_name()

L_CAD, L_OWN, L_PRICE = "公告分配地籍線", "分配後歸戶圖", "重劃後地價圖"
NO_RE = re.compile(r"^\d+(-\d+)?$")


def _key(s):
    a = s.split("-")
    return (int(a[0]), int(a[1]) if len(a) > 1 else 0)


def _draw(ax, msp, layer, outlines, fs):
    for e in msp:
        if e.dxf.layer != layer:
            continue
        if e.dxftype() == "HATCH":
            for p in e.paths:
                xs = [v[0] for v in p.vertices]
                ys = [v[1] for v in p.vertices]
                ax.fill(xs, ys, color=tuple(c / 255 for c in e.rgb), linewidth=0)
        elif e.dxftype() == "TEXT":
            ax.text(e.dxf.align_point[0], e.dxf.align_point[1], e.dxf.text, ha="center", va="center", fontsize=fs)
    for pts in outlines:
        xs = [p[0] for p in pts] + [pts[0][0]]
        ys = [p[1] for p in pts] + [pts[0][1]]
        ax.plot(xs, ys, color="black", linewidth=0.6)


def maps_png(dxf_path, out_png, title):
    import ezdxf
    from shapely.geometry import Point, Polygon
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    outlines = [[(p[0], p[1]) for p in e.get_points("xy")]
                for e in msp if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == L_CAD]
    fig, axes = plt.subplots(2, 2, figsize=(24, 24))
    _draw(axes[0][0], msp, L_CAD, outlines, 5)
    axes[0][0].set_title(L_CAD + "（每宗：地號／面積／寬／深）", fontsize=16)
    # S 型之序之示意：每宗之地號之註記之位置，依地號之序連以箭線
    pts = []
    for pl in outlines:
        poly = Polygon(pl)
        nos = [t for t in msp.query(f'TEXT[layer=="{L_CAD}"]')
               if NO_RE.match(t.dxf.text) and poly.contains(Point(t.dxf.align_point[0], t.dxf.align_point[1]))]
        if len(nos) != 1:
            raise SystemExit(f"一宗之地號之註記非一（{len(nos)}）")
        c = poly.representative_point()
        pts.append((_key(nos[0].dxf.text), nos[0].dxf.text, c.x, c.y))
    pts.sort()
    ax = axes[0][1]
    for pl in outlines:
        xs = [p[0] for p in pl] + [pl[0][0]]
        ys = [p[1] for p in pl] + [pl[0][1]]
        ax.plot(xs, ys, color="0.6", linewidth=0.6)
    for (_, _, x0, y0), (_, _, x1, y1) in zip(pts, pts[1:]):
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", color="tab:red", linewidth=1.2))
    for _, s, x, y in pts:
        ax.text(x, y, s, ha="center", va="center", fontsize=11, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="tab:red", lw=0.8))
    ax.set_title("重劃後地號之序（S 型·示意）", fontsize=16)
    _draw(axes[1][0], msp, L_OWN, outlines, 9)
    axes[1][0].set_title(L_OWN + "（歸戶號／抵費地）", fontsize=16)
    _draw(axes[1][1], msp, L_PRICE, outlines, 7)
    axes[1][1].set_title(L_PRICE + "（元／㎡）", fontsize=16)
    for a in axes.flat:
        a.set_aspect("equal")
        a.axis("off")
    fig.suptitle(title, fontsize=20)
    fig.tight_layout()
    fig.savefig(out_png, dpi=90)
    plt.close(fig)


def main(argv):
    src, out, *tags = argv
    os.makedirs(out, exist_ok=True)
    rc = 0
    for t in tags:
        p = os.path.join(out, f"W-P.005_重劃後三圖層_退縮{t}m.png")
        maps_png(os.path.join(src, f"公告圖_退縮{t}m.dxf"), p, f"W-P.005　重劃後三圖層（退縮 {t} m·示範資料）")
        sz = os.path.getsize(p)
        print(f"{p}\t{sz} bytes")
        rc |= int(sz == 0)
    return rc


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```

## 附錄丁　`plots/alloc_state.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005　配地結果之取出（重劃後三圖層與地號對照表之輸入）。

命令列：python plots/alloc_state.py --out <目錄> --setback <退縮公尺> [--setback …]
輸出（皆寫至 --out，⛔ 入倉）：配地結果_退縮<退縮>m.json（每一退縮一檔）。

所據：出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md（§一 3、§二 1）。
  來源 ＝ 既有之無畫面之配地流程（verify/ 之管線·唯呼叫·⛔ 改），依 verify/run_verification.py 之 main
  之序：load_snapshot → harvest → build_pipeline → build_param_table → build_ownership →
  build_build_parcels → run_corner_pk_k6b → run_step_g（eff_min_build_by_blk＝{}）。
  所取者 ＝ 階段一之終（段三後·調配〔核心線階段二〕之前）之 g_rows；調配之新模組入主線後，唯改本檔之來源。
  「推進側別」＝「抵費地」之列 ⇒ 類別「抵費地」（同 app.py export_allocated_dxf）；他列 ⇒「分配地」。
  面積二位四捨五入為 0.00 之列不成宗，列於「略」（印之·⛔ 靜默）。
缺值一律報錯停止（⛔ 靜默補值）。
"""
import argparse
import contextlib
import io
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "verify"))

SOURCE_NOTE = "階段一之終（段三後·未經調配）：verify/stepg_pipeline.run_step_g 之 g_rows"
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_SIDE = "抵費地"
OUT_FMT = "配地結果_退縮{}m.json"


class SourceError(RuntimeError):
    """資料與單之所據不符 ⇒ 停機上呈。"""


def q2(x):
    return float(Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def tag_of(setback):
    s = f"{setback:g}"
    return s


def run_pipeline(setbacks):
    """⇒ (cb_by, cad, omap, {退縮: g_rows})。管線之印出一律收於記憶體（⛔ 擾本程式之輸出）。"""
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        snapshot = rv.load_snapshot()
        ns, fake_st = harvest()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        build_ownership(ns, fake_st, rv.ANON_XLSX)
        with open(rv.V6DXF, "rb") as f:
            v6 = f.read()
        temp, build, _sw = build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        rows = {}
        for sb in setbacks:
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            _d, _s, _o, win, forced, _tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snapshot)
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3,
                            win, forced, sb, eff_min_build_by_blk={})
            rows[sb] = sg["g_rows"]
        omap = dict(fake_st.session_state["t8_ownership_map"])
    return cb_by, cad, omap, rows


def blocks_of(cb_by, cad):
    alloc = cad.get("alloc_dir_by_block") or {}
    front = cad.get("front_lines") or {}
    out = {}
    for lbl in sorted(cb_by):
        b = cb_by[lbl]
        vs = b.get("vertices") or []
        if len(vs) < 3:
            raise SourceError(f"街廓 {lbl} 之頂點不足")
        cat = b.get("category")
        if not cat:
            raise SourceError(f"街廓 {lbl} 無分類")
        d = {"分類": cat, "面積": float(b["area_m2"]), "多邊形": [[float(x), float(y)] for x, y in vs]}
        if lbl in alloc:
            if lbl not in front:
                raise SourceError(f"街廓 {lbl} 有宗地分配線而無正面臨路線")
            d["宗地分配線方向"] = [float(v) for v in alloc[lbl]]
            d["正面臨路線"] = [[float(v) for v in front[lbl]["p1"]], [float(v) for v in front[lbl]["p2"]]]
        out[lbl] = d
    return out


def lots_of(g_rows, blocks, omap):
    lots, dropped = [], []
    seen = set()
    for r in g_rows:
        pid = r.get("暫編地號")
        if not pid or pid in seen:
            raise SourceError(f"配地之列之暫編地號缺或重複：{pid!r}")
        seen.add(pid)
        blk = r.get("所屬街廓")
        if blk not in blocks or "宗地分配線方向" not in blocks[blk]:
            raise SourceError(f"{pid} 之街廓 {blk!r} 非可分配之街廓")
        cs = r.get("cut_coords") or []
        if len(cs) < 3:
            raise SourceError(f"{pid} 無多邊形")
        area = q2(r["幾何面積(㎡)"])
        kind = KIND_OFFSET if r.get("推進側別") == OFFSET_SIDE else KIND_LOT
        if area == 0:
            dropped.append({"配地暫編": pid, "街廓": blk, "類別": kind, "幾何面積": float(r["幾何面積(㎡)"])})
            continue
        d = {"配地暫編": pid, "街廓": blk, "類別": kind, "面積": area,
             "多邊形": [[float(x), float(y)] for x, y in cs]}
        if kind == KIND_LOT:
            ln = r.get("原地號")
            if not ln or ln not in omap:
                raise SourceError(f"{pid} 之原地號 {ln!r} 不在歸戶表")
            w = r.get("宗地寬度(m)")
            if w is None or float(w) <= 0:
                raise SourceError(f"{pid} 之宗地寬度缺")
            d.update({"原地號": ln, "歸戶": omap[ln], "G": q2(r["G(㎡)"]), "宗地寬度": q2(w)})
        lots.append(d)
    return lots, dropped


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 配地結果之取出")
    ap.add_argument("--out", required=True)
    ap.add_argument("--setback", type=float, action="append", required=True)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    cb_by, cad, omap, rows = run_pipeline(a.setback)
    blocks = blocks_of(cb_by, cad)
    for sb in a.setback:
        lots, dropped = lots_of(rows[sb], blocks, omap)
        doc = {"退縮_m": sb, "來源": SOURCE_NOTE, "街廓": blocks, "宗": lots, "略": dropped}
        p = os.path.join(a.out, OUT_FMT.format(tag_of(sb)))
        with open(p, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
            f.write("\n")
        n_off = sum(1 for x in lots if x["類別"] == KIND_OFFSET)
        print(f"退縮 {tag_of(sb)} m：宗 {len(lots)}（分配地 {len(lots) - n_off}、抵費地 {n_off}）；"
              f"略 {[x['配地暫編'] for x in dropped]}")
        print(f"輸出 {p}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄戊　`plots/post_maps.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.005　重劃後三圖層（公告分配地籍線·分配後歸戶圖·重劃後地價圖）＋ 暫編→正式地號對照表
＋ 顏色對照表（重劃後）。

命令列：python plots/post_maps.py --state <配地結果_退縮*.json> --pre-dxf <重劃前圖.dxf>
          --moedict <dict-revised.json> --out <目錄> [--map <地號對照表.xlsx>]
  --state   ＝ plots/alloc_state.py 之輸出。
  --pre-dxf ＝ plots/prelim_maps.py 之「重劃前圖.dxf」（三圖層·W-P.001／002 定版）；本程式讀之、加三圖層、另存（⛔ 改原檔）。
  --map     ＝ 承辦人改過之地號對照表（本程式前次之輸出）；無 ⇒ 依 S 型自動編定之預設。
輸出（皆寫至 --out，⛔ 入倉）：公告圖_退縮<t>m.dxf（六圖層）、地號對照表_退縮<t>m.xlsx、顏色對照表_重劃後_退縮<t>m.xlsx。

所據：出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md（§一、§二）。
  KL 2026-10-28 23:31：問一 甲（程式依 S 型自動編定；全範圍同一地段；先排區〔東北先〕、再區內 S 型）；
  問四 乙（每宗註記地號、面積、分配寬度、深度）；問五 乙（抵費地自成一色並註「抵費地」；道路、公園不填色、
  只畫界線；原地主分得之地照一般歸戶上色）。KL 23:37：保留「暫編 → 正式地號對照表」（重號或缺號即停）。
缺值一律報錯停止（⛔ 靜默補值）。
"""
import argparse
import json
import os
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "plots"))

import prelim_maps as PM  # noqa: E402  （重劃前之歸戶、顏色、歸戶號·W-P.001／002）
import owner_index  # noqa: E402

LAYER_POST_CAD = "公告分配地籍線"
LAYER_POST_OWN = "分配後歸戶圖"
LAYER_POST_PRICE = "重劃後地價圖"
POST_LAYERS = (LAYER_POST_CAD, LAYER_POST_OWN, LAYER_POST_PRICE)
KIND_LOT, KIND_OFFSET = "分配地", "抵費地"
OFFSET_TEXT = "抵費地"
OFFSET_COLOR = (160, 160, 160)
LINE_GAP = 1.4                       # 多列註記之行距（× 字高）
REGION_TOL = 0.01                    # 區之相接之容差（公尺）
NO_RE = re.compile(r"^[1-9]\d{0,4}(-[1-9]\d*)?$")   # 母號（不超過五位數）或「母號-子號」（手冊第 3849〜3854 列）
MAP_SHEET = "地號對照表"
MAP_HEAD = ("暫編", "街廓", "類別", "配地之暫編地號", "預設地號（S 型）", "正式地號", "面積（㎡）")
MAP_NOTE = "「正式地號」得由承辦人改之（例：段界另有調整）；重號或空白者，本程式即停止產出（KL 2026-10-28 23:37）。"


def q2(x):
    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def f2(x):
    return f"{q2(x):.2f}"


# ---------------------------------------------------------------- 讀取
def load_state(path):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    for k in ("退縮_m", "街廓", "宗", "略"):
        if k not in doc:
            raise PM.SourceError(f"配地結果缺 {k}")
    if not doc["宗"]:
        raise PM.SourceError("配地結果無宗")
    return doc


def tag_of(doc):
    return f"{float(doc['退縮_m']):g}"


def post_prices():
    v = json.load(open(PM.CASE_PARAMS, encoding="utf-8"))["財務接線_v3"]
    if "後街廓_面積單價" not in v:
        raise PM.SourceError("case_params 之 財務接線_v3 缺 後街廓_面積單價")
    return {b: float(d["單價_元每m2"]) for b, d in v["後街廓_面積單價"].items()}


# ---------------------------------------------------------------- 宗之整理
def entries_of(doc):
    """⇒ 重劃後之各宗（分配地、抵費地、公設之區塊），各附暫編（街廓-序號；公設 ＝ 其編號）。"""
    from shapely.geometry import Polygon
    blocks = doc["街廓"]
    ents = []
    by_blk = {}
    for x in doc["宗"]:
        by_blk.setdefault(x["街廓"], []).append(x)
    for lbl in sorted(blocks):
        b = blocks[lbl]
        if "宗地分配線方向" not in b:
            continue
        lots = by_blk.get(lbl, [])
        if not lots:
            raise PM.SourceError(f"可分配之街廓 {lbl} 無宗")
        (x1, y1), (x2, y2) = b["正面臨路線"]
        L = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        ux, uy = (x2 - x1) / L, (y2 - y1) / L

        def t_of(x):
            p = Polygon(x["多邊形"]).representative_point()
            return (p.x - x1) * ux + (p.y - y1) * uy
        for i, x in enumerate(sorted(lots, key=t_of), start=1):
            e = dict(x)
            e["暫編"] = f"{lbl}-{i:02d}"
            ents.append(e)
    for lbl in sorted(blocks):
        b = blocks[lbl]
        if "宗地分配線方向" in b:
            continue
        if lbl in by_blk:
            raise PM.SourceError(f"非可分配之街廓 {lbl} 有配地之宗")
        ents.append({"暫編": lbl, "配地暫編": None, "街廓": lbl, "類別": b["分類"],
                     "面積": float(q2(Polygon(b["多邊形"]).area)), "多邊形": b["多邊形"]})
    return ents


def regions(blocks):
    """⇒ [[街廓…]]：重劃範圍之相連之各區（各街廓之多邊形外擴 REGION_TOL 後之相連者）。"""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    polys = {k: Polygon(v["多邊形"]) for k, v in blocks.items()}
    u = unary_union([p.buffer(REGION_TOL) for p in polys.values()])
    parts = list(getattr(u, "geoms", [u]))
    out = []
    for part in parts:
        mem = sorted(k for k, p in polys.items() if part.contains(p.representative_point()))
        out.append((part, mem))
    if sorted(k for _, m in out for k in m) != sorted(polys):
        raise PM.SourceError("街廓之分區不全或重複")
    return out


def _ne_key(geom):
    c = geom.centroid
    return (-round(c.y, 3), -round(c.x, 3))


def s_order(doc, ents):
    """重劃後地號之預設編定（KL 23:31 問一 甲）⇒ [暫編]（依地號 1、2、3…之序）。
    區：依其形心先北後南（同者先東）；區內之可分配之街廓：依形心先北後南（同者先東），
    第 1、3、5…個街廓之宗自東而西、第 2、4、6…個自西而東（S 型）；正東西向之正面臨路線則以先北後南代東西。
    各區之宗編畢，公設之區塊（道路、公園）續編於後（依區之序，區內依形心先北後南、同者先東）。"""
    from shapely.geometry import Polygon
    blocks = doc["街廓"]
    by_blk = {}
    for e in ents:
        by_blk.setdefault(e["街廓"], []).append(e)
    regs = sorted(regions(blocks), key=lambda pm: _ne_key(pm[0]))
    order, publics = [], []
    for _part, mem in regs:
        alloc = [k for k in mem if "宗地分配線方向" in blocks[k]]
        pub = [k for k in mem if "宗地分配線方向" not in blocks[k]]
        alloc.sort(key=lambda k: _ne_key(Polygon(blocks[k]["多邊形"])))
        for i, k in enumerate(alloc):
            (x1, y1), (x2, y2) = blocks[k]["正面臨路線"]
            dx, dy = x2 - x1, y2 - y1
            L = (dx * dx + dy * dy) ** 0.5
            ux, uy = dx / L, dy / L
            west = (-ux > 1e-9) or (abs(ux) <= 1e-9 and uy < 0)
            if not west:
                ux, uy = -ux, -uy          # u 指向西（正東西向者指向南）
            if i % 2 == 1:
                ux, uy = -ux, -uy          # 第 2、4、6…個街廓：自西而東

            def t_of(e):
                p = Polygon(e["多邊形"]).representative_point()
                return p.x * ux + p.y * uy
            order.extend(e["暫編"] for e in sorted(by_blk[k], key=t_of))
        pub.sort(key=lambda k: _ne_key(Polygon(blocks[k]["多邊形"])))
        publics.extend(pub)
    order.extend(publics)
    if sorted(order) != sorted(e["暫編"] for e in ents):
        raise PM.SourceError("S 型之編定漏宗或重複")
    return order


# ---------------------------------------------------------------- 地號對照表
def default_numbers(order):
    return {t: str(i) for i, t in enumerate(order, start=1)}


def write_map(path, ents, order, numbers, default):
    import openpyxl
    from openpyxl.styles import Alignment
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = MAP_SHEET
    ws.append(list(MAP_HEAD))
    pos = {t: i for i, t in enumerate(order)}
    for e in sorted(ents, key=lambda e: pos[e["暫編"]]):
        ws.append([e["暫編"], e["街廓"], e["類別"], e.get("配地暫編"), default[e["暫編"]],
                   numbers[e["暫編"]], float(q2(e["面積"]))])
    ws.append([])
    ws.append([MAP_NOTE])
    for c in ws[1]:
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    wb.save(path)


def read_map(path, ents):
    """承辦人之對照表 ⇒ {暫編: 正式地號}。暫編之集合不符、正式地號空白、格式不合、重號 ⇒ SourceError（停止）。"""
    import openpyxl
    ws = openpyxl.load_workbook(path, data_only=True)[MAP_SHEET]
    rows = list(ws.iter_rows(values_only=True))
    if tuple(rows[0][:len(MAP_HEAD)]) != MAP_HEAD:
        raise PM.SourceError(f"對照表之表頭不符：{rows[0]}")
    want = {e["暫編"] for e in ents}
    got = {}
    for r in rows[1:]:
        t = r[0]
        if t is None or str(t).strip() == "" or str(t) == MAP_NOTE:
            continue
        t = str(t).strip()
        if t not in want:
            raise PM.SourceError(f"對照表之暫編 {t} 非本次配地之宗")
        if t in got:
            raise PM.SourceError(f"對照表之暫編 {t} 重複")
        v = r[5]
        if v is None or str(v).strip() == "":
            raise PM.SourceError(f"對照表之暫編 {t} 之正式地號空白（缺號）")
        s = str(int(v)) if isinstance(v, (int, float)) and float(v).is_integer() else str(v).strip()
        if not NO_RE.match(s):
            raise PM.SourceError(f"對照表之暫編 {t} 之正式地號 {v!r} 非整數之母號（或母號-子號）")
        got[t] = s
    miss = sorted(want - set(got))
    if miss:
        raise PM.SourceError(f"對照表缺暫編：{miss}")
    seen = {}
    for t, s in sorted(got.items()):
        if s in seen:
            raise PM.SourceError(f"正式地號 {s} 重號：{seen[s]}、{t}")
        seen[s] = t
    return got


# ---------------------------------------------------------------- 歸戶（照重劃前之歸戶號與顏色）
def owner_scheme(moedict, ents):
    strokes = owner_index.load_strokes(moedict)
    lots, owners, area = PM.load_cadastre()
    key_of, hh_order = PM.households(lots, owners)
    hh_color = dict(zip(hh_order, PM.distinct_palette(len(hh_order))))
    hh_lots, members = PM.household_members(owners, key_of)
    hh_no = owner_index.number_households(hh_lots, members, strokes, PM.landno_key)
    if OFFSET_COLOR in hh_color.values():
        raise PM.SourceError("抵費地之色與某戶之色同")
    g_of = {}
    for e in ents:
        if e["類別"] != KIND_LOT:
            continue
        ln = e["原地號"]
        if ln not in key_of:
            raise PM.SourceError(f"{e['暫編']} 之原地號 {ln} 不在重劃前之地籍")
        k = key_of[ln]
        if g_of.setdefault(e["歸戶"], k) != k:
            raise PM.SourceError(f"配地之歸戶 {e['歸戶']} 與重劃前之歸戶不一（{ln}）")
    if len(set(g_of.values())) != len(g_of):
        raise PM.SourceError("重劃前之一戶對應配地之數歸戶")
    return key_of, hh_color, hh_no


# ---------------------------------------------------------------- DXF
def _texts(msp, layer, lines, p):
    from ezdxf.enums import TextEntityAlignment
    n = len(lines)
    for i, s in enumerate(lines):
        y = p.y + ((n - 1) / 2 - i) * PM.TEXT_HEIGHT * LINE_GAP
        t = msp.add_text(s, height=PM.TEXT_HEIGHT, dxfattribs={"layer": layer, "style": PM.TEXT_STYLE})
        t.set_placement((p.x, y), align=TextEntityAlignment.MIDDLE_CENTER)


def cad_lines(e, no):
    if e["類別"] == KIND_LOT:
        w = q2(e["宗地寬度"])
        d = (Decimal(repr(float(e["面積"]))) / w).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return [no, f2(e["面積"]), f"寬{w:.2f}", f"深{d:.2f}"]
    return [no, f2(e["面積"])]


def write_dxf(pre_path, path, ents, numbers, key_of, hh_color, hh_no, price, price_color):
    import ezdxf
    from shapely.geometry import Polygon
    doc = ezdxf.readfile(pre_path)
    for name in PM.LAYERS:
        if name not in doc.layers:
            raise PM.SourceError(f"重劃前圖缺圖層 {name}")
    for name in POST_LAYERS:
        if name in doc.layers:
            raise PM.SourceError(f"重劃前圖已有圖層 {name}")
        doc.layers.add(name)
    msp = doc.modelspace()
    for e in sorted(ents, key=lambda e: e["暫編"]):
        coords = [(float(x), float(y)) for x, y in e["多邊形"]]
        if coords[0] == coords[-1]:
            coords = coords[:-1]
        rp = Polygon(coords).representative_point()
        no = numbers[e["暫編"]]
        msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": LAYER_POST_CAD})
        _texts(msp, LAYER_POST_CAD, cad_lines(e, no), rp)
        if e["類別"] in (KIND_LOT, KIND_OFFSET):
            h = msp.add_hatch(dxfattribs={"layer": LAYER_POST_OWN})
            if e["類別"] == KIND_LOT:
                k = key_of[e["原地號"]]
                h.set_solid_fill(rgb=hh_color[k])
                lab = str(hh_no[k])
            else:
                h.set_solid_fill(rgb=OFFSET_COLOR)
                lab = OFFSET_TEXT
            h.paths.add_polyline_path(coords, is_closed=True)
            _texts(msp, LAYER_POST_OWN, [lab], rp)
            v = price[e["街廓"]]
            h2 = msp.add_hatch(dxfattribs={"layer": LAYER_POST_PRICE})
            h2.set_solid_fill(rgb=price_color[v])
            h2.paths.add_polyline_path(coords, is_closed=True)
            _texts(msp, LAYER_POST_PRICE, [f2(v)], rp)
        else:
            msp.add_lwpolyline(coords, close=True, dxfattribs={"layer": LAYER_POST_OWN})
    doc.saveas(path)


def write_color_table(path, ents, numbers, key_of, hh_color, hh_no, price, price_color):
    import openpyxl
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    ws = wb.create_sheet(LAYER_POST_OWN)
    ws.append(["圖層", "歸戶號", "顏色 R,G,B", "正式地號"])
    by_hh = {}
    for e in ents:
        if e["類別"] == KIND_LOT:
            by_hh.setdefault(key_of[e["原地號"]], []).append(numbers[e["暫編"]])
    for k in sorted(by_hh, key=lambda kk: hh_no[kk]):
        ws.append([LAYER_POST_OWN, hh_no[k], "{},{},{}".format(*hh_color[k]),
                   "、".join(sorted(by_hh[k], key=PM.landno_key))])
    offs = sorted((numbers[e["暫編"]] for e in ents if e["類別"] == KIND_OFFSET), key=PM.landno_key)
    if offs:
        ws.append([LAYER_POST_OWN, OFFSET_TEXT, "{},{},{}".format(*OFFSET_COLOR), "、".join(offs)])
    ws2 = wb.create_sheet(LAYER_POST_PRICE)
    ws2.append(["圖層", "顏色 R,G,B", "重劃後地價（元/㎡）", "街廓", "正式地號"])
    for v in sorted(price_color):
        blks = sorted(b for b, p in price.items() if p == v)
        nos = sorted((numbers[e["暫編"]] for e in ents
                      if e["類別"] in (KIND_LOT, KIND_OFFSET) and price[e["街廓"]] == v), key=PM.landno_key)
        ws2.append([LAYER_POST_PRICE, "{},{},{}".format(*price_color[v]), f2(v), "、".join(blks), "、".join(nos)])
    wb.save(path)


OUT_FMT = {"dxf": "公告圖_退縮{}m.dxf", "map": "地號對照表_退縮{}m.xlsx", "color": "顏色對照表_重劃後_退縮{}m.xlsx"}


def main(argv=None):
    ap = argparse.ArgumentParser(description="W-P.005 重劃後三圖層＋地號對照表＋顏色對照表")
    ap.add_argument("--state", required=True)
    ap.add_argument("--pre-dxf", required=True)
    ap.add_argument("--moedict", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map")
    a = ap.parse_args(argv)
    doc = load_state(a.state)
    tag = tag_of(doc)
    ents = entries_of(doc)
    order = s_order(doc, ents)
    default = default_numbers(order)
    numbers = read_map(a.map, ents) if a.map else dict(default)
    key_of, hh_color, hh_no = owner_scheme(a.moedict, ents)
    price_all = post_prices()
    blks = sorted({e["街廓"] for e in ents if e["類別"] in (KIND_LOT, KIND_OFFSET)})
    miss = [b for b in blks if b not in price_all]
    if miss:
        raise PM.SourceError(f"case_params 之 後街廓_面積單價 缺：{miss}")
    price = {b: price_all[b] for b in blks}
    vals = sorted(set(price.values()))
    price_color = dict(zip(vals, PM.distinct_palette(len(vals))))
    os.makedirs(a.out, exist_ok=True)
    p = {k: os.path.join(a.out, v.format(tag)) for k, v in OUT_FMT.items()}
    write_map(p["map"], ents, order, numbers, default)
    write_dxf(a.pre_dxf, p["dxf"], ents, numbers, key_of, hh_color, hh_no, price, price_color)
    write_color_table(p["color"], ents, numbers, key_of, hh_color, hh_no, price, price_color)
    n = {k: sum(1 for e in ents if e["類別"] == k) for k in (KIND_LOT, KIND_OFFSET)}
    print(f"退縮 {tag} m：分配地 {n[KIND_LOT]}、抵費地 {n[KIND_OFFSET]}、公設 {len(ents) - sum(n.values())}；"
          f"略 {[x['配地暫編'] for x in doc['略']]}")
    print("地號：" + "、".join(f"{t}→{numbers[t]}" for t in order))
    print(f"重劃後地價 {[f2(v) for v in vals]}（街廓 {price}）")
    for k, v in p.items():
        print(f"輸出 {v}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
```

## 附錄己　`docs/出圖/W-P.005_重劃後三圖層與地號對照表.md`（逐位元組照錄）

````markdown
# W-P.005　重劃後三圖層與地號對照表

單：`ops/queue` 之 `出圖線/orders/W-P.005_重劃後三圖層與地號對照表.md`。

## 產出之法

```
python plots/alloc_state.py --out <O> --setback 0 --setback 3.5        # 約 10 分鐘（跑配地流程至段三後之 G 值）
python plots/prelim_maps.py --out <P> --moedict <dict-revised.json>    # 重劃前三圖層（W-P.001／002）
python plots/post_maps.py --state <O>/配地結果_退縮3.5m.json --pre-dxf <P>/重劃前圖.dxf \
       --moedict <dict-revised.json> --out <O> [--map <改過之地號對照表.xlsx>]
```

輸出：`公告圖_退縮<t>m.dxf`（六圖層：重劃前地籍線、重劃前歸戶圖、重劃前地價圖〔照錄重劃前圖〕＋ 公告分配地籍線、分配後歸戶圖、重劃後地價圖）、`地號對照表_退縮<t>m.xlsx`、`顏色對照表_重劃後_退縮<t>m.xlsx`。

## 依據（KL）

- 2026-10-28 23:31：問一 甲（程式依 S 型自動編定；全範圍同一地段；先排區〔東北先〕、再區內 S 型）；問四 乙（每宗註記地號、面積、分配寬度、深度）；問五 乙（抵費地自成一色並註「抵費地」；道路、公園不填色、只畫界線；原地主分得之地照一般歸戶上色）。
- 2026-10-28 23:37：保留「暫編 → 正式地號對照表」；承辦人得改正式地號；重號或缺號即停。

## 規則之要

- 配地結果之來源：階段一之終（段三後·核心線之階段二〔調配〕之新模組未成）。新模組入主線後，唯改 `plots/alloc_state.py` 之來源。面積二位為 0.00 之列不成宗（列於「略」）。
- 暫編：可分配之街廓之宗沿正面臨路線由起點（左）而迄點（右）編「街廓-兩位序號」（抵費地居其位）；公設之區塊以其編號。
- 預設地號（S 型）：區依形心先北後南（同者先東）；區內之可分配之街廓依形心先北後南（同者先東）；第 1、3、5…個街廓自東而西、第 2、4、6…個自西而東；各宗之序依其位置沿正面臨路線之投影；公設之區塊續編於後。
- 對照表：「正式地號」預設 ＝ 預設地號；以 `--map` 讀承辦人之表；暫編不符、空白、非整數之母號（或母號-子號·五位數以內）、重號 ⇒ 停止產出。
- 公告分配地籍線：分配地註 地號／面積／寬（引擎之宗地寬度·垂直於宗地分配線）／深（面積 ÷ 寬）；抵費地與公設註 地號／面積。
- 分配後歸戶圖：分配地之色與歸戶號 ＝ 其原地號於重劃前歸戶圖者；抵費地灰（160,160,160）並註「抵費地」；公設只畫界線。
- 重劃後地價圖：分配地與抵費地依其街廓之重劃後單價（`財務接線_v3.後街廓_面積單價`·註二位）；一價一色；公設不填。

## 量測與故意錯誤

`verify/plots/check_W-P005.py`（V0〜V7）；`verify/plots/mutate_W-P005.py`（Ⓐ〜Ⓔ）；`verify/plots/preview_W-P005.py`（預覽）。
````
