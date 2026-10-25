# W-P.002_補令一　附表 26 之兩組改為每頁先左欄由上而下、再右欄

- **題**：依 KL 2026-10-25 10:22 之答，將附表 26「土地所有權人索引表」之左右兩組之排列，自「由左而右、再由上而下」改為「每頁先左組由上而下排滿、再右組由上而下；次頁接續」。附表 26 之內容（姓名、歸戶號、序）、表頭、簽欄、DXF、顏色對照表、附表 2、3 ⛔ 變。
- **範圍**：唯 `plots/owner_index.py`（本線所建）與 `verify/plots/`、`docs/出圖/` 之下；⛔ 改任何既有之檔；⛔ 改 `requirements.txt`。
- **授權（逐字）**：
  - KL 2026-10-23 17:31「1. 是　2. 以手冊（拾參）所附的圖例為主」；17:48「…還有產製手冊表目錄裡面所有的報表（配合匯入的地籍資料）」（README 第一節）。
  - KL 2026-10-25 10:22「是，索引表改為先左欄由上而下、再右欄」（`出圖線/KL答覆/2026-10-25_1022.md`；監看窗之讀：每頁各自先左後右、排滿一頁之左欄後再右欄；跨頁者次頁接續；附表 2 照舊）。
- **開工態**（發單時 `git ls-remote` 實測）：主線 `wip/s1-endpart` ＝ `d4928d4845513a42fb1ac826a63167a38c78d4fb`；`wip/plots` ＝ `9c0b51c295345eed9d2b4798f37eaff9f5121485`（W-P.002 之端·已含 `d4928d4`）。
- **側支**：`verify/W-P.002a-index-columns`（自 `wip/plots` 出）。
- **推分支之許可**：`出圖線/分支許可.md` 之 `N` ＝ `393`（已具）。

## §一　所據

1. 手冊第 4080〜4094 列附表 26 之表樣（左右二組·W-P.002 §一 1）；排列之方向手冊未載 ⇒ 依 KL 10:22。
2. 「一頁」之定義：本表之列印為 A4 直式、寬度縮為一頁（W-P.002 §二 3）；為使「每頁先左後右」於列印時成立，**程式定每頁每組之列數並置手動分頁符**。每頁每組之列數為版面之事（KL 17:48：版面由使用者編輯）⇒ ⛔ 問；本單取 **40**（A4 直式、列高預設、表頭三列之下可容），以常數 `APPX26_PER_PAGE` 置於 `plots/owner_index.py`，使用者得改之。
3. 示範資料 67 組 ＜ 80 ⇒ 一頁：左組 1〜40（列 4〜43）、右組 41〜67（列 4〜30）；無分頁符。跨頁之排列以示範之 170 筆（`示範001`〜`示範170`·非實案資料）驗之：三頁 80、80、10；分頁符在列 43、83 之後；末頁唯左組 10 筆（列 84〜93）。

## §二　規格

1. **改 `plots/owner_index.py`**（唯此三處；他處⛔ 動）：
   - 於 `APPX26_SIGN` 之下加常數 `APPX26_PER_PAGE = 40` 與函式 `appx26_slot(i, per)`：第 i 筆（0 起）⇒ `p, k = divmod(i, 2*per)`；列 ＝ `4 + p*per + k % per`；組 ＝ `k // per`（0 左、1 右）。
   - `write_appx26`：資料之填寫改用 `appx26_slot(i, APPX26_PER_PAGE)`（呼叫時讀模組之常數，供故意錯誤之測掛換）；`r` ＝ 資料之末列（各筆之列之最大）；頁數 ＝ ⌈筆數 ÷ (2×per)⌉；第 1〜(頁數−1) 頁之末列（`3 + p×per`）之後各加一手動分頁符（`openpyxl.worksheet.pagebreak.Break(id=3 + p*per)`·`ws.row_breaks.append`）。
   - 框線、簽欄（資料末列之後空一列）、列印標題 1〜3、A4 直式、寬一頁照舊。
   - 發單端之原型之差異（供對照·`git diff` 之實物）：
     ```
     +APPX26_PER_PAGE = 40   # 每頁每欄之列數（W-P.002_補令一·KL 2026-10-25 10:22：每頁先左欄由上而下、再右欄）
     +def appx26_slot(i, per):
     +    p, k = divmod(i, 2 * per)
     +    return 4 + p * per + k % per, k // per
     ...
     -        r, j = 4 + i // 2, i % 2
     +        rr_, j = appx26_slot(i, per)
     +        r = max(r, rr_)
     +    n_pages = (len(rows) + 2 * per - 1) // (2 * per)
     +    for p in range(1, n_pages):
     +        ws.row_breaks.append(Break(id=3 + p * per))
     ```
2. **新增 `verify/plots/synth_W-P002a.py`**：逐位元組 ＝ 附錄乙。
3. **改 `verify/plots/check_W-P002.py`**：全文換為附錄甲（Q3 改依新排列逐格比對＋分頁符；新增 Q6 驗示範多頁；共 8 項；命令列加第三參數）。
4. **改 `verify/plots/mutate_W-P002.py`**：全文換為附錄丙（Ⓒ 依新排列重填；新增 Ⓕ Ⓖ Ⓗ；命令列加第四參數）。
5. `verify/plots/preview_W-P002.py` ⛔ 改（其右表依格繪之，新排列自現）。
6. 發單端之原型（暫存·⛔ 入倉）已依上式實作：附錄甲 8/8 綠；附錄丙之成果綠、8 種皆紅；`check_W-P001` 12/12；DXF 之 318 圖元、顏色對照表、附表 2、3 與 `9c0b51c` 之輸出逐格同；附錄甲對 `9c0b51c` 之舊輸出 Q3 紅（對照組）。預覽見 `出圖線/待KL/W-P.002_補令一_原型預覽.png`。

## §三　驗收

工項：
1. **與主線同步**：自 `origin/wip/plots` 出側支 `verify/W-P.002a-index-columns`；`git merge --no-edit origin/wip/s1-endpart`（主線未前進者即無事）；有衝突即停機。
2. **程式**：§二 1〜4。附錄甲、乙、丙之取用法：自本單擷取該附錄之 ```` ```python ```` 與 ```` ``` ```` 間之文字，末尾一換行；sha256 與 bytes 須合：
   - 甲 `verify/plots/check_W-P002.py`：13033 bytes·`a8f9420743d9c9dcc0a12e62f3afdf62434c797da07791bceb04e42856705a87`
   - 乙 `verify/plots/synth_W-P002a.py`：744 bytes·`5d56a63968814c6c189eb974f89b3ab62f78afe4715caa0823e743ad4d18d270`
   - 丙 `verify/plots/mutate_W-P002.py`：8020 bytes·`761a76c4ade5e41c689b7ba19852584945140615343bc6d5850fea27c08a05a3`
   不合即停機上呈；⛔ 改一字。
3. **量測**：
   - `python plots/fetch_moedict.py <倉外之目錄>`；`python plots/prelim_maps.py --out <out> --moedict <json>`；`python verify/plots/synth_W-P002a.py <倉外>/示範多頁之附表26.xlsx`。
   - `python verify/plots/check_W-P002.py <out> <json> <示範多頁之附表26.xlsx>` ⇒ Q0、Q1、Q1b、Q2〜Q6 共 8 項皆 PASS、結束碼 0；Q3 之訊息須為「資料末列 43、簽欄列 45」、Q6 之「分頁符 [43, 83]」。
   - `python verify/plots/check_W-P001.py <out>/重劃前圖.dxf <out>/附表03_重劃前土地清冊.xlsx` ⇒ 12/12。
   - 對照組：以 `9c0b51c` 之 `plots/` 出之舊輸出跑附錄甲 ⇒ Q3 紅（記其訊息）。
4. **故意錯誤之測**：`python verify/plots/mutate_W-P002.py <out> <拋棄式之工作目錄> <json> <示範多頁之附表26.xlsx>` ⇒ 成果綠；Ⓐ〜Ⓗ 皆紅（原型實測：Ⓐ Q1、Q3、Q5；Ⓑ Q1；Ⓒ Q3；Ⓓ Q1、Q3、Q5；Ⓔ Q4；Ⓕ 回舊式 Q3；Ⓖ 每頁 30 列 Q6；Ⓗ 無分頁符 Q6）；約 1 分鐘。`verify/plots/mutate_W-P001.py <out> <工作目錄>` 照舊成果綠、14 種皆紅（約 3 分鐘）。
5. **差異閘**（README 第四節）：`git diff --name-status d4928d4845513a42fb1ac826a63167a38c78d4fb <側支之端>`（主線若前進，以實際併入之主線之 sha 代之）每列皆在 `plots/`、`verify/plots/`、`docs/出圖/` 之下；另 `git diff --name-status 9c0b51c <側支之端>` 唯 `plots/owner_index.py`、`verify/plots/check_W-P002.py`、`verify/plots/mutate_W-P002.py`、`verify/plots/synth_W-P002a.py`、`docs/出圖/` 之下者（主線前進所帶入者除外）；對照組（拋棄式複本改 `app.py` 一字）必紅。
6. **其餘輸出⛔ 變**：DXF 之圖元（類、圖層、文字、座標、顏色）、顏色對照表、附表 2、3 之逐格值與 `9c0b51c` 之輸出同（記比對之法與結果）。
7. **預覽 PNG**：`python verify/plots/preview_W-P002.py <out> <PNG 目錄>`，其輸出改名為 `W-P.002_補令一_附表26先左後右.png` 入佇列之 `出圖線/成果/`。
8. **docs**：新增 `docs/出圖/W-P.002_補令一_附表26排列.md`：KL 10:22 之逐字、排列之規則、每頁每組 40 列之常數與其為版面之事（使用者得改）、量測與故意錯誤之表。
9. **快轉 `wip/plots`** 至側支之端（⛔ `--force`），前後值記於 `出圖線/log.md` 與 `STATE.json` 之 `history`。
10. **回報**：`出圖線/reports/W-P.002_補令一_回報.md`（各工項之實測、量測之全輸出、對照組、故意錯誤之表、差異閘、`wip/plots` 前後值）；`STATE` 設 `reported`。

## §四　停機款

1. 合併主線有衝突。
2. 附錄甲、乙、丙之 sha256 或 bytes 不合；tarball 或 JSON 之 sha256 不合；或 Q0〜Q6 於成果不過而非程式之誤。
3. 須改 `plots/owner_index.py` 以外之出圖程式、或任何既有之檔。
4. 任一內容之判斷本單未定者 ⇒ 停，⛔ 自定。

## 附錄甲　`verify/plots/check_W-P002.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.002（含補令一）：歸戶號（重劃前歸戶圖之註記）、顏色對照表之歸戶號、附表 26 土地所有權人索引表之量測。
獨立於 plots/：⛔ import 之；期望取自倉內原始資料、教育部筆劃之資料（dict-revised.json）、手冊與 KL 之答。

命令列：python verify/plots/check_W-P002.py <成果目錄> <dict-revised.json> <示範多頁之附表26.xlsx>
  成果目錄 ＝ plots/prelim_maps.py --out 之目錄（讀 重劃前圖.dxf、顏色對照表_重劃前.xlsx、附表26_土地所有權人索引表.xlsx）。
  示範多頁之附表26.xlsx ＝ verify/plots/synth_W-P002a.py 之輸出（170 筆之示範名·驗跨頁之排列）。
任一不過 ⇒ 結束碼 1。Q0 筆劃之資料；Q1/Q1b 歸戶圖之歸戶號；Q2〜Q4 附表 26；Q5 顏色對照表；Q6 跨頁之排列。
排序之所據：KL 2026-10-23 21:18（單獨在前）、2026-10-25 02:30（一甲 二乙 三甲 四可·甲）、02:33（共有戶以自然人為主）。
排列之所據（W-P.002_補令一）：KL 2026-10-25 10:22「是，索引表改為先左欄由上而下、再右欄」——每頁先左組由上而下排滿
  A26_PER 列、再右組由上而下；次頁接續；每頁之末一列之後置手動分頁符。
"""
import functools
import hashlib
import json
import os
import sys
import unicodedata
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
XLSX_SRC = os.path.join(REPO, "data", "地籍資料來源_匿名版.xlsx")
MOE_SHA = "f68fc3df140a64d8de6eb905ff6576bfd9d260eed0bbf5cc9c41aba5a131a7ad"
# 教育部標準字體之筆劃（KL 2026-10-24 11:43「甲」；大陸之值：草 9、蓮 13、葉 12、蔡 14、鄭 14、邱 7、阮 6）
STROKE_ANCHORS = {"草": 10, "花": 8, "蓮": 15, "連": 11, "進": 12, "葉": 13, "蔡": 15, "鄭": 15,
                  "邱": 8, "郭": 11, "阮": 7, "余": 7, "沈": 7}
# 發單端依 KL 之答手排之錨（地號 → 歸戶號）
HH_ANCHORS = {"628-26": 1, "628": 2, "628-2": 3, "628-51": 19, "713": 20, "628-3": 21,
              "628-35": 22, "628-39": 23, "628-40": 24, "628-15": 33}
FILE_DXF = "重劃前圖.dxf"
FILE_COLOR = "顏色對照表_重劃前.xlsx"
FILE_A26 = "附表26_土地所有權人索引表.xlsx"
L_CAD, L_OWN = "重劃前地籍線", "重劃前歸戶圖"
A26_MERGES = {"A1:H1", "A2:A3", "B2:C2", "D2:D3", "E2:E3", "F2:G2", "H2:H3"}
A26_ROW2 = ["所有權人姓名", "分配清冊", None, "附註"] * 2
A26_ROW3 = [None, "第 冊", "第 頁", None] * 2
A26_SIGN = ["承辦:", "股長:", "科長:", "製表日期: 年 月 日"]
COLOR_HEAD = ["圖層", "歸戶號", "顏色 R,G,B", "所有權人", "地號"]
N_HH, N_INDEX = 33, 67
A26_PER = 40                       # 每頁每欄之列數（W-P.002_補令一 §二 1）
SYNTH = [(f"示範{i:03d}", i) for i in range(1, 171)]   # synth_W-P002a.py 之輸入（170 筆 ⇒ 3 頁：80、80、10）


def a26_slot(i, per=A26_PER):
    p, k = divmod(i, 2 * per)
    return 4 + p * per + k % per, k // per


def a26_layout(ws, seq, per=A26_PER):
    """附表 26 之資料區（列 4 起）之逐格比對、簽欄之列、手動分頁符。⇒ (ok, 訊息)"""
    want = {}
    for i, (nm, no) in enumerate(seq):
        want[a26_slot(i, per)] = (nm, no)
    body_last = max(r for r, _ in want)
    last = _last_row(ws)
    bad = []
    for r in range(4, last):
        for j in range(2):
            got = tuple(ws.cell(r, 1 + 4 * j + d).value for d in range(4))
            if (r, j) in want:
                nm, no = want[(r, j)]
                ok = str(got[0]) == nm and got[3] == no and _blank(got[1]) and _blank(got[2])
            else:
                ok = all(_blank(v) for v in got)
            if not ok:
                bad.append(((r, j), got[0], got[3], want.get((r, j))))
    n_pages = (len(seq) + 2 * per - 1) // (2 * per)
    brk_want = [3 + p * per for p in range(1, n_pages)]
    brk_got = sorted(b.id for b in ws.row_breaks.brk)
    ok = not bad and last == body_last + 2 and brk_got == brk_want
    return ok, (f"筆 {len(seq)}；不符 {len(bad)} {bad[:3]}；資料末列 {body_last}、簽欄列 {last}（期望 {body_last + 2}）；"
                f"分頁符 {brk_got}（期望 {brk_want}）")


def _blank(v):
    return v is None or (isinstance(v, str) and v.strip() in ("", "null"))


def lkey(s):
    p = str(s).split("-")
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0)


@functools.lru_cache(maxsize=None)
def moe(path):
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    rad_no = {}
    for i in range(214):
        rad_no[unicodedata.normalize("NFKC", chr(0x2F00 + i))] = i + 1
    rad_no["青"] = 174
    tab = {}
    for e in json.loads(raw):
        t = e.get("title", "")
        if len(t) == 1:
            tab[t] = (int(e["stroke_count"]), rad_no[e["radical"].strip()])
    return sha, tab


def ckey(c, tab):
    if unicodedata.name(c, "").startswith(("CJK UNIFIED IDEOGRAPH", "CJK COMPATIBILITY IDEOGRAPH")):
        s, r = tab[c]          # 缺 ⇒ KeyError ⇒ 量測不過（⛔ 補值）
        return (0, s, r, ord(c))
    return (1, ord(c), 0, 0)


def nkey(name, tab):
    return tuple(ckey(c, tab) for c in name)


def grp(kind, pub):
    kind, pub = str(kind).strip(), str(pub).strip()
    if pub == "公":
        return 2
    if pub == "私":
        return {"1": 0, "7": 1}[kind]
    raise KeyError((kind, pub))


@functools.lru_cache(maxsize=None)
def truth(moe_path):
    import openpyxl
    _, tab = moe(moe_path)
    wb = openpyxl.load_workbook(XLSX_SRC, read_only=True)
    rows = list(wb["重劃區地籍"].iter_rows(values_only=True))
    il = rows[0].index("地號")
    lots = sorted((str(r[il]).strip() for r in rows[1:] if not _blank(r[il])), key=lkey)
    ls = set(lots)
    own = defaultdict(dict)       # 地號 → 登記次序 → (統編, 姓名, 群)
    for r in wb["U_LAND"].iter_rows(values_only=True):
        if r[0] != "0013德安段" or _blank(r[1]):
            continue
        m, s = divmod(int(r[1]), 10000)
        ln = f"{m}" if s == 0 else f"{m}-{s}"
        if ln in ls:
            own[ln].setdefault(int(r[23]), (str(r[32]), str(r[33]), grp(r[37], r[38])))
    hh_lots = defaultdict(list)
    hh_mem = {}
    for ln in lots:
        k = frozenset(own[ln].values())
        hh_lots[k].append(ln)
        hh_mem[k] = sorted(k)
    singles, joints = [], []
    for k, mem in hh_mem.items():
        first = min(lkey(x) for x in hh_lots[k])
        if len(mem) == 1:
            _, nm, g = mem[0]
            singles.append(((g, nkey(nm, tab), first), k))
        else:
            heads = [nkey(nm, tab) for _, nm, g in mem if g == 0]
            if not heads:
                raise ValueError(f"共有戶無自然人 {mem}")
            joints.append(((len(mem), min(heads), first), k))
    seq = [k for _, k in sorted(singles)] + [k for _, k in sorted(joints)]
    no_of_hh = {k: i + 1 for i, k in enumerate(seq)}
    no_of_lot = {ln: no_of_hh[k] for k, v in hh_lots.items() for ln in v}
    idx = sorted(((g, nkey(nm, tab), no_of_hh[k]), nm) for k, mem in hh_mem.items() for _, nm, g in mem)
    index = [(nm, key[2]) for key, nm in idx]
    lots_of_no = {no_of_hh[k]: sorted(v, key=lkey) for k, v in hh_lots.items()}
    return lots, no_of_lot, index, lots_of_no


def _last_row(ws):
    return max(r for r in range(1, ws.max_row + 1)
               if any(not _blank(ws.cell(r, c).value) for c in range(1, ws.max_column + 1)))


def run(out_dir, moe_path, synth_path):
    import openpyxl
    res = []

    def rec(n, ok, msg=""):
        res.append((n, bool(ok), msg))
        print(f"{'PASS' if ok else 'FAIL'} {n} {msg}")

    sha, tab = moe(moe_path)
    got = {c: tab.get(c, (None,))[0] for c in STROKE_ANCHORS}
    rec("Q0", sha == MOE_SHA and got == STROKE_ANCHORS, f"sha256 {sha[:12]}…；筆劃 {got}")
    lots, no_of_lot, index, lots_of_no = truth(moe_path)
    anc = {ln: no_of_lot.get(ln) for ln in HH_ANCHORS}

    # Q1 歸戶圖之歸戶號
    try:
        import ezdxf
        from shapely.geometry import Point, Polygon
        msp = ezdxf.readfile(os.path.join(out_dir, FILE_DXF)).modelspace()
        polys = [Polygon([(p[0], p[1]) for p in e.get_points("xy")])
                 for e in msp if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == L_CAD and e.closed]
        lot_poly = {}
        for e in msp:
            if e.dxftype() == "TEXT" and e.dxf.layer == L_CAD:
                pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
                hit = [i for i, pg in enumerate(polys) if pg.contains(pt)]
                if len(hit) == 1:
                    lot_poly[e.dxf.text] = hit[0]
        on = defaultdict(list)
        stray = []
        for e in msp:
            if e.dxftype() == "TEXT" and e.dxf.layer == L_OWN:
                pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
                hit = [ln for ln, i in lot_poly.items() if polys[i].contains(pt)]
                if len(hit) == 1:
                    on[hit[0]].append(e.dxf.text)
                else:
                    stray.append(e.dxf.text)
        wrong = [(ln, on.get(ln), no_of_lot[ln]) for ln in lots if on.get(ln) != [str(no_of_lot[ln])]]
        rec("Q1", set(lot_poly) == set(lots) and not wrong and not stray
            and sorted(set(no_of_lot.values())) == list(range(1, N_HH + 1)),
            f"註記 {sum(len(v) for v in on.values())}（期望 {len(lots)}）；不符 {wrong[:4]}；落宗外 {stray[:3]}")
    except Exception as e:  # noqa: BLE001
        rec("Q1", False, f"DXF 讀取失敗 {type(e).__name__}: {e}")
    rec("Q1b", anc == HH_ANCHORS, f"錨 {anc}")

    # Q2〜Q4 附表 26
    try:
        wb = openpyxl.load_workbook(os.path.join(out_dir, FILE_A26))
        if len(wb.worksheets) != 1:
            raise ValueError(f"工作表數 {len(wb.worksheets)}≠1")
        ws = wb.worksheets[0]
        merges = {str(m) for m in ws.merged_cells.ranges}
        r2 = [ws.cell(2, c).value for c in range(1, 9)]
        r3 = [ws.cell(3, c).value for c in range(1, 9)]
        rec("Q2", ws["A1"].value == "土地所有權人索引表" and merges == A26_MERGES and r2 == A26_ROW2
            and r3 == A26_ROW3 and str(ws.print_title_rows).replace("$", "") == "1:3" and ws.max_column == 8,
            f"題 {ws['A1'].value!r}；併格差 {sorted(merges ^ A26_MERGES)}；列2 {r2}；列3 {r3}；列印標題 {ws.print_title_rows}；欄數 {ws.max_column}")
        last = _last_row(ws)
        ok3, msg3 = a26_layout(ws, index)
        rec("Q3", ok3 and len(index) == N_INDEX, msg3)
        vals = [ws.cell(last, c).value for c in range(1, ws.max_column + 1) if not _blank(ws.cell(last, c).value)]
        rec("Q4", vals == A26_SIGN, f"末列 {vals}")
    except Exception as e:  # noqa: BLE001
        rec("Q2", False, f"附表 26 讀取失敗 {type(e).__name__}: {e}")

    # Q5 顏色對照表之歸戶號
    try:
        import ezdxf
        from shapely.geometry import Polygon
        wb = openpyxl.load_workbook(os.path.join(out_dir, FILE_COLOR), read_only=True)
        rows = list(wb["重劃前歸戶圖"].iter_rows(values_only=True))
        head, body = list(rows[0]), [r for r in rows[1:] if any(not _blank(v) for v in r)]
        nos = [r[1] for r in body]
        lot_ok = all(sorted(str(r[4]).split("、"), key=lkey) == lots_of_no.get(r[1]) for r in body)
        hcol = {}
        for e in msp:
            if e.dxftype() == "HATCH" and e.dxf.layer == L_OWN:
                rp = Polygon([(v[0], v[1]) for v in e.paths[0].vertices]).representative_point()
                hit = [ln for ln, i in lot_poly.items() if polys[i].contains(rp)]
                if len(hit) == 1:
                    hcol[hit[0]] = "{},{},{}".format(*e.rgb)
        col_bad = [r[1] for r in body if any(hcol.get(ln) != r[2] for ln in str(r[4]).split("、"))]
        rec("Q5", head == COLOR_HEAD and nos == list(range(1, N_HH + 1)) and lot_ok and not col_bad,
            f"表頭 {head}；歸戶號 {nos[:3]}…{nos[-2:]}（{len(nos)}）；地號合 {lot_ok}；色與圖不符 {col_bad[:3]}")
    except Exception as e:  # noqa: BLE001
        rec("Q5", False, f"顏色對照表讀取失敗 {type(e).__name__}: {e}")

    # Q6 跨頁之排列（示範 170 筆·synth_W-P002a.py）
    try:
        ws = openpyxl.load_workbook(synth_path).worksheets[0]
        ok6, msg6 = a26_layout(ws, SYNTH)
        vals = [ws.cell(_last_row(ws), c).value for c in range(1, 9) if not _blank(ws.cell(_last_row(ws), c).value)]
        rec("Q6", ok6 and vals == A26_SIGN and str(ws.print_title_rows).replace("$", "") == "1:3",
            f"{msg6}；末列 {vals}；列印標題 {ws.print_title_rows}")
    except Exception as e:  # noqa: BLE001
        rec("Q6", False, f"示範多頁之附表 26 讀取失敗 {type(e).__name__}: {e}")
    return res


N_Q = 8

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    r = run(*sys.argv[1:4])
    sys.exit(0 if len(r) == N_Q and all(x[1] for x in r) else 1)
```

## 附錄乙　`verify/plots/synth_W-P002a.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.002_補令一：以示範之 170 筆（示範001〜示範170·歸戶號 1〜170）出附表 26，供 check_W-P002.py 之 Q6 驗跨頁之排列。
命令列：python verify/plots/synth_W-P002a.py <輸出之 .xlsx>（⛔ 在倉內）
示範之名非實案資料；唯驗 plots/owner_index.write_appx26 之排列與分頁符。
"""
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, "plots"))
import owner_index  # noqa: E402

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    owner_index.write_appx26(sys.argv[1], [(f"示範{i:03d}", i) for i in range(1, 171)])
    print("輸出", sys.argv[1])
```

## 附錄丙　`verify/plots/mutate_W-P002.py`（逐位元組照錄）

```python
# -*- coding: utf-8 -*-
"""
W-P.002 之故意錯誤之測（單 §三 4·補令一 §三 4）：成果須綠、Ⓐ〜Ⓗ 共 8 種變異體須各紅（量測 ＝ check_W-P002.py 之 8 項）。

命令列：python verify/plots/mutate_W-P002.py <成果目錄> <拋棄式之工作目錄> <dict-revised.json> <示範多頁之附表26.xlsx>
  成果目錄 ＝ plots/prelim_maps.py --out 之目錄（⛔ 改之；變異體皆寫於工作目錄）。
  示範多頁之附表26.xlsx ＝ verify/plots/synth_W-P002a.py 之輸出（⛔ 改之；複製入各工作目錄）。
  Ⓐ、Ⓓ、Ⓖ 掛換 plots/owner_index 之函式或常數後重出（於本行程之記憶體中·⛔ 改檔）；Ⓑ、Ⓒ、Ⓔ、Ⓕ、Ⓗ 改成果之複本。
結束碼：成果綠且 8 種皆紅 ⇒ 0；否則 1。
"""
import importlib.util
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("check_W_P002", os.path.join(HERE, "check_W-P002.py"))
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)

FILES = (chk.FILE_DXF, chk.FILE_COLOR, chk.FILE_A26)
SYNTH_NAME = "示範多頁之附表26.xlsx"
SYNTH_SRC = None   # main 設之
MAINLAND = {"草": 9, "蓮": 13, "葉": 12, "邱": 7, "阮": 6}   # 大陸之筆劃（單 §三 4 Ⓐ）


def _copy(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for f in FILES:
        shutil.copy2(os.path.join(src, f), os.path.join(dst, f))
    shutil.copy2(SYNTH_SRC, os.path.join(dst, SYNTH_NAME))


def _fresh(dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    shutil.copy2(SYNTH_SRC, os.path.join(dst, SYNTH_NAME))


def _prelim():
    sys.path.insert(0, os.path.join(REPO, "plots"))
    sys.path.insert(0, os.path.join(REPO, "verify"))
    import prelim_maps
    return prelim_maps


def _regen(d, moe_path, attr, repl):
    pm = _prelim()
    oi = pm.owner_index
    orig = getattr(oi, attr)
    setattr(oi, attr, repl(orig))
    try:
        _fresh(d)
        pm.main(["--out", d, "--moedict", moe_path])
    finally:
        setattr(oi, attr, orig)


def mA_mainland_strokes(d, moe_path):
    def repl(orig):
        def load(path):
            tab = dict(orig(path))
            for c, s in MAINLAND.items():
                tab[c] = (s, tab[c][1])
            return tab
        return load
    _regen(d, moe_path, "load_strokes", repl)


def mB_wrong_number(d, moe_path):
    import ezdxf
    from shapely.geometry import Point, Polygon
    p = os.path.join(d, chk.FILE_DXF)
    doc = ezdxf.readfile(p)
    msp = doc.modelspace()
    polys = [Polygon([(q[0], q[1]) for q in e.get_points("xy")])
             for e in msp if e.dxftype() == "LWPOLYLINE" and e.dxf.layer == chk.L_CAD]
    target = None
    for e in msp:
        if e.dxftype() == "TEXT" and e.dxf.layer == chk.L_CAD and e.dxf.text == "628-26":
            pt = Point(e.dxf.align_point[0], e.dxf.align_point[1])
            target = [pg for pg in polys if pg.contains(pt)][0]
    hit = [e for e in msp if e.dxftype() == "TEXT" and e.dxf.layer == chk.L_OWN
           and target.contains(Point(e.dxf.align_point[0], e.dxf.align_point[1]))]
    if len(hit) != 1 or hit[0].dxf.text != "1":
        raise RuntimeError(f"628-26 之歸戶號之註記非恰一個「1」：{[e.dxf.text for e in hit]}")
    hit[0].dxf.text = "2"
    doc.saveas(p)


def _read_seq(ws):
    """依補令一之排列（每頁先左組、再右組）讀回附表 26 之序。"""
    last = chk._last_row(ws)
    seq, i = [], 0
    while True:
        r, j = chk.a26_slot(i)
        if r >= last:
            break
        nm = ws.cell(r, 1 + 4 * j).value
        if not chk._blank(nm):
            seq.append((nm, ws.cell(r, 4 + 4 * j).value))
        i += 1
    return seq, last


def _rewrite(ws, seq, last, slot):
    for r in range(4, last):
        for j in range(2):
            ws.cell(r, 1 + 4 * j).value = None
            ws.cell(r, 4 + 4 * j).value = None
    for i, (nm, no) in enumerate(seq):
        r, j = slot(i)
        ws.cell(r, 1 + 4 * j, nm)
        ws.cell(r, 4 + 4 * j, no)


def mC_drop_index_row(d, moe_path):
    import openpyxl
    p = os.path.join(d, chk.FILE_A26)
    wb = openpyxl.load_workbook(p)
    ws = wb.worksheets[0]
    seq, last = _read_seq(ws)
    hits = [i for i, (nm, _) in enumerate(seq) if nm == "沈昌穎"]
    if len(hits) < 2:
        raise RuntimeError(f"沈昌穎 之列不足二：{hits}")
    del seq[hits[1]]
    _rewrite(ws, seq, last, chk.a26_slot)
    wb.save(p)


def mF_row_major(d, moe_path):
    """舊式：由左而右、再由上而下（KL 10:22 前之排列）。"""
    import openpyxl
    p = os.path.join(d, chk.FILE_A26)
    wb = openpyxl.load_workbook(p)
    ws = wb.worksheets[0]
    seq, last = _read_seq(ws)
    if len(seq) != chk.N_INDEX:
        raise RuntimeError(f"讀回 {len(seq)} 筆≠{chk.N_INDEX}")
    _rewrite(ws, seq, last, lambda i: (4 + i // 2, i % 2))
    wb.save(p)


def mG_per_page_30(d, moe_path):
    """每頁每欄之列數錯（30）：掛換常數後重出示範多頁之附表 26。"""
    sys.path.insert(0, os.path.join(REPO, "plots"))
    import owner_index as oi
    orig = oi.APPX26_PER_PAGE
    oi.APPX26_PER_PAGE = 30
    try:
        oi.write_appx26(os.path.join(d, SYNTH_NAME), list(chk.SYNTH))
    finally:
        oi.APPX26_PER_PAGE = orig


def mH_no_breaks(d, moe_path):
    """示範多頁之附表 26 刪去手動分頁符。"""
    import openpyxl
    p = os.path.join(d, SYNTH_NAME)
    wb = openpyxl.load_workbook(p)
    ws = wb.worksheets[0]
    if not ws.row_breaks.brk:
        raise RuntimeError("示範之附表 26 本無分頁符")
    ws.row_breaks.brk = []
    wb.save(p)


def mD_no_groups(d, moe_path):
    _regen(d, moe_path, "group_of", lambda orig: (lambda row: 0))


def mE_no_section_chief(d, moe_path):
    import openpyxl
    p = os.path.join(d, chk.FILE_A26)
    wb = openpyxl.load_workbook(p)
    ws = wb.worksheets[0]
    for row in ws.iter_rows():
        for c in row:
            if c.value == "股長:":
                c.value = None
                wb.save(p)
                return
    raise RuntimeError("找不到「股長:」")


MUTANTS = [
    ("Ⓐ 大陸筆劃（草 9、蓮 13、葉 12、邱 7、阮 6）", mA_mainland_strokes, False),
    ("Ⓑ 歸戶圖 628-26 之歸戶號 1→2", mB_wrong_number, True),
    ("Ⓒ 附表 26 漏沈昌穎之第二戶", mC_drop_index_row, True),
    ("Ⓓ 不分群（group_of 恆 0）", mD_no_groups, False),
    ("Ⓔ 附表 26 簽欄缺「股長:」", mE_no_section_chief, True),
    ("Ⓕ 附表 26 回舊式（逐列由左而右）", mF_row_major, True),
    ("Ⓖ 每頁每欄 30 列（示範多頁）", mG_per_page_30, True),
    ("Ⓗ 示範多頁之附表 26 無分頁符", mH_no_breaks, True),
]


def verdict(d, moe_path):
    res = chk.run(d, moe_path, os.path.join(d, SYNTH_NAME))
    ok = len(res) == chk.N_Q and all(x[1] for x in res)
    return ok, [x[0] for x in res if not x[1]]


def main(argv):
    global SYNTH_SRC
    src, work, moe_path, SYNTH_SRC = argv
    rows = []
    base = os.path.join(work, "base")
    _copy(src, base)
    print("== 成果 ==")
    ok, fails = verdict(base, moe_path)
    rows.append(("成果", "綠" if ok else "紅", fails, ok))
    for name, fn, from_copy in MUTANTS:
        d = os.path.join(work, f"mut{len(rows)}")
        if from_copy:
            _copy(src, d)
        fn(d, moe_path)
        print(f"== {name} ==")
        ok, fails = verdict(d, moe_path)
        rows.append((name, "綠" if ok else "紅", fails, not ok))
    print("\n| 對象 | 判 | 不過之量測 | 合期望 |")
    print("|---|---|---|---|")
    for n, v, f, good in rows:
        print(f"| {n} | {v} | {'、'.join(f) or '—'} | {'是' if good else '否'} |")
    return 0 if all(r[3] for r in rows) else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
```
