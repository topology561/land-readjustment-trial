# -*- coding: utf-8 -*-
"""
W-F F.0 — 前置與級0/0'（同街廓同歸戶合併）＋梯3 二群釋池。行為波第一子波。

**架構＝雙 trunk**（KL 裁定 2026-07-10、reviewer 複審後）：
  trunk A（v3 錨）：原 build_parcels → run_step_g，對拍 baselines/v3/（證基礎引擎零漂移）。
  trunk B（F.0 終態）：deepcopy build_parcels → F.0 變換 → run_step_g，對拍 baselines/wf/f0/。
本檔 additive-only：**不改 app.py、不改 stepg_pipeline 推進機、不碰 build_ownership 指紋**。
解算一律走 app 真函式 run_step_g（F.0 僅為 Step G 前之 parcels 資料變換）。

**KL 正典（位相不變＝原位次序不變，2026-07-10）**：集中合併時，標的宗於原位次原地變寬，
變寬面積以調配池結算；標的宗左右毗鄰不變；全體剩餘宗相對位次序不變。同街廓合併中被併宗消失
使其原鄰居重新接鄰＝幾何必然、非違規；判準只看標的宗鄰居＋全體位次序（**投影序**，k*-無關）。
§8：斜交街廓＋solve_G_binary 幾何驅動下平移致不動點微移（0.01–1.02㎡）為法定公式內生、非 bug；
逐宗 G 凍結閘刪除（reviewer BLOCKED#1）。

**級0/0'（先併再判，不停機）**：
  達標宗 = G_i ≥ MinA_blk 且無畸零旗標。
  有達標宗 → 級0：標的=達標宗 G 最大者；被併=全部未達標宗。
  無達標宗 → 級0'：標的=全格 G 最大者；被併=其餘。
  合併＝標的宗.面積_m2 += Σ(被併宗 a)（a′ 累加器；分攤登記面積_m2 唯讀）→ run_step_g 對 Σa 重解。
  合併後仍不達標＝標旗轉出（G009→F.2、G014→F.4；停機#4「下一級」＝§7 全鏈），不停機。
tie-break：標的=G 最大者，並列取暫編地號字典序最小（決定性）。

**梯3 二群釋池**：G025（628-53(1)@R6、628-53(2)@R5）＋G030（628-27(1)@R2、628-27(2)@R3）＝57.48㎡，
  不配地、自 parcels 移除、G 全額由池吸收。
"""
import os
import sys
import csv
import json
import copy

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from app_harvest import harvest                    # noqa: E402
import run_verification as rv                       # noqa: E402
from selection_pipeline import (                    # noqa: E402
    build_ownership, build_build_parcels, run_corner_pk)
from stepg_pipeline import run_step_g, build_step_g_tables  # noqa: E402

OUTDIR = os.path.join(HERE, "out")
F0DIR = os.path.join(HERE, "baselines", "wf", "f0")

# 梯3 二群（F.0-pre 定；ΣG=57.48㎡，唯一釋池對象）
TIER3_LOTS = ["628-53(1)", "628-53(2)", "628-27(1)", "628-27(2)"]

# 六格 G(Σa) 期望錨（雙情境；步2 自檢「烤值==錨」±0.01）
# W-G Y 波比率更新（KL 裁定 2026-07-14，第 3 版街廓相對比率 R6 100→90·R2 95→90·R3/R5 90→95）：
#   六格再重算·舊錨（PRE-比率更新·凍存於 baselines/PRE-比率更新_凍存）：
#     0m G006 376.97/G007 373.85/G009 147.54/G010 288.47/G014 131.02/G017 413.61
#     3.5m G006 376.97/G007 380.63/G009 147.54/G010 292.23/G014 133.22/G017 413.61
# 更早：W-G v3 勘誤重烤（KL 2026-07-13，前價期日勘誤 2024/01/01·per-zone）·凍存 baselines/PRE勘誤_期日。
# 🆕 P-0c（裁定M·S1 波末重烤·claude.ai 2026-07-25）：G007/G010/G014 重定錨——
#   成因＝W脫鉤(07-19)＋S0d(07-20) 改 trunk A 之 W/S 輸入項（G007@R5 628-20(2)：
#   W 20.05→18.41／Rw 20.52→27.51（W脫鉤）·S 8.21→8.15（S0d）→ G 362.08→359.43）。
#   G006/G009/G017 不動。歸因表見 docs/reports/…P0c_S1重烤_歸因表.md。
# 🆕 **K-6-A2 段三(c) 重錨（claude.ai 裁 2026-08-04）：`3.5m` 之 G010／G007 兩格**——
#   **成因（統一）**＝**K-9-7 接生產**：街角規定範圍改依 **K-9-6-b 之帶深**
#   （＝範圍**自身**之最小深度 `D(t*)`，非街廓平均深度）與 **K-9-7 之 `(c − k·m)` 斜率**定位
#   ⇒ **三側強制留設抵費地（forced_offset）之面積變動** ⇒ 其後各宗之 s 帶／W／Rw 隨之微移。
#   實料：`verify/out/probe_k97_r5_attribution.log`（新舊皆由本檔 `compute` 產出·
#         舊輪以 `_t_override` 注入 `t_star_legacy`）。
#
#   ── 逐 gid 因果歸因表（**六格全列·含未動者及其未動之理由**）──────────────────
#   gid   標的宗        街廓  該側 forced？ 範圍面積(舊→新)      ΔG      處置
#   G010  628-40(1)     R2   ✅(R2左)     382.85→384.15 (+1.30)  **+0.05**  **重錨 301.12→301.17**
#         └ 逾錨檢容差（`abs>0.01`）⇒ **破錨**（本次 run_all 之唯一破錨格）。
#   G007  628-20(2)     R5   ✅(R5左)     378.47→371.17 (−7.30)  **−0.01**  **重錨 370.02→370.01**
#         └ **未破錨**——錨檢為**嚴格**不等式，`0.01 > 0.01` 為 False ⇒ 恰落容差邊界。
#           **惟實值已變** ⇒ **主動重錨**（claude.ai 裁）。理由：若留 370.02，
#           段四 K-9-8／波末換 V6_1 之任何再一個 0.01 微擾即使其變 0.02 而爆，
#           **屆時歸因會指向那一批、真正成因卻在 K-9-7** ⇒ 正是 F-7-3「禁打地鼠」所防之形狀。
#           傳導佐證：`628-20(2)` 於 R5 之**累積S ＝ 28.78**，遠在抵費地（S=0）**之後**
#           ⇒ 屬機制所及之「其後各宗」（實料同上 log【3】段）。
#   G014  628-29(1)     R3   ✅(R3右)     383.67→383.67 ( 0.00)   +0.00    不重錨
#   G006  628-48(1)     R3   ✅(R3右)     383.67→383.67 ( 0.00)   +0.00    不重錨
#         └ G006／G014 同屬 R3；R3右 雖 forced，但其範圍面積**未變**（分支 ①·`k≥0` ⇒ 深度不影響）。
#   G009  628-1(2)      R6   ❌(R6右非)   298.14→298.14 ( 0.00)   +0.00    不重錨
#   G017  628-21(1)     R6   ❌(R6右非)   298.14→298.14 ( 0.00)   +0.00    不重錨
#         └ G009／G017 同屬 R6；R6右 `forced=False` **且**範圍面積未變（分支 ①）⇒ 雙重不受影響。
#
#   ── `"0m"` 全組不動之理由 ────────────────────────────────────────────────
#   0m **僅 R3右 forced**，而 R3右 範圍面積 `226.91→226.91` **未變** ⇒ 抵費地帳零變動。
#   ⚠️ 0m 之 **R2左／R5左 範圍面積確有變動**（`+1.42`／`−7.27`），惟該二側 **`forced=False`**
#     ⇒ **不生抵費地帳** ⇒ 不影響任何 gid。（＝「0m 面積沒變」之說法**不正確**，勿沿用。）
#   實測：0m 六格 ΔG 皆 `+0.00`。
#
#   ── ⚠️ 一項「記錄、不解釋」之觀察（claude.ai 明令勿編成因）──────────────────
#   兩格之敏感度差 **27 倍**：R2 `+1.30㎡ ⇒ +0.05`、R5 `−7.30㎡ ⇒ −0.01`。
#   **本批如實記下此不對稱，⛔ 未為其編造未經量測之成因。** 段四或波末如需，屆時再查。
#
#   ── 🔴 粒度限制（見 GB-27）──────────────────────────────────────────────
#   被比欄 `G(㎡)` 於來源即 `round(..., 2)`（`grep -n "'G(㎡)': round" verify/stepg_pipeline.py`）
#   ⇒ 上表之 ΔG **粒度為 0.01**；「+0.00」只能讀作「**2dp 下未變**」，
#   **不得**讀作「真值未變」。
#   ⤷ 該代之值（**本代之前一代·凍存於註解**）：
#       0m   G006 365.84／G007 359.43／G009 153.19／G010 **293.72**／G014 **127.05**／G017 433.68
#       3.5m G006 365.84／G007 **369.41**／G009 153.19／G010 **298.61**／G014 **129.20**／G017 433.68
#
# 🆕 **K-8 §三〜§五 街角規定範圍新構造**（KL 裁 2026-07-31·**K-8 §五-1** 已確認面積歸屬變動）：
#   五格重定錨（0m 二格／3.5m 三格）。**重錨 ≠ 重烤**——baseline CSV 一律不動（U-K8-1＝乙 照舊）；
#   重錨之唯一目的係讓 F.0 不再 raise，使被截斷之 68 個名目重新產生、baseline 該紅的照紅且看得見。
#   ⚠️ 五格之移動**全部**追得出因果鏈（禁「跑出什麼就寫什麼」）：
#     · **0m G010@R2**（標的宗 628-40(1)·級0·Σa 513.93 **不變**）293.72→**283.87**（−9.85）
#       ＝R2 左街角規定面積 151.44→225.69 ⇒ 門檻升 ⇒ 原 winner G023(628-41(1)) 失格
#       ⇒ **PK 翻盤 G023→G010**，標的宗**自身**成為該側街角第 1 宗
#       （`街角地 否→是`／`第1筆街角 否→是`／`街角側別 —→左側`）⇒ 改吃側街負擔
#       （`W 10.61→6.44`／`Rw 35.58→52.51%`／`負擔比率 0.4285→0.4476`）⇒ G 降。
#       **PK 翻盤宗 == GSA 移動宗 == 628-40(1)**，因果鏈閉合。
#     · **0m G014@R3**（標的宗 628-29(1)·級0'·Σa 228.0 **不變**）127.05→**128.63**（+1.58）
#       ＝R3 右 winner G007(628-45(2)) → **強制留設抵費地**（合格候選 1→0）⇒ 該側無街角第 1 宗
#       ⇒ 推進序起點重排（`累積S 10.86→16.21`）⇒ `W 9.13→14.45` ⇒ `Rw 15.19→11.16%`
#       ⇒ 負擔降 ⇒ G 升。**同街廓連坐**（該宗自身非翻盤宗、`街角地` 欄未動）。
#     · **3.5m G007@R5 369.41→370.02（+0.61）／G010@R2 298.61→301.12（+2.51）／
#        G014@R3 129.20→129.74（+0.54）**——3.5m **winner 全部不變**，成因係三側**強制留設
#       抵費地面積上升**（R5左 300.52→378.47／R2左 309.05→382.85／R3右 308.93→383.67）
#       ⇒ 抵費地佔用之 s 帶加寬 ⇒ 其後各宗 `累積S` 外推 +1.7〜+1.8m ⇒ `W` 同幅增大
#       ⇒ `Rw` 降（R5 1.52→0.00／R2 23.07→16.66／R3 9.69→8.31%）⇒ 負擔比率降 ⇒ G 微升。
#   🔒 **未移動之三格係「被評估過且相符」、非「沒被評估」**：F-1 覆蓋率硬閘
#     （`grep -n "_uncov" verify/wf_f0.py`）於雙情境**皆無【未被評估】輸出**
#     ⇒ 六 gid 全數進入 `gsa` 被實際比對（G006/G009/G017 逐格相符）。
#   🔒 **`平均深度(m)` 欄之變動屬 commit A（深度兩路同源）、非本代**——commit A 已實測
#     「G 閘 442 列違規 100% 只在該顯示欄、G 值 delta＝0」⇒ 兩個 delta 源可分離歸因。
#   歸因表全文：docs/reports/W-G.5_K8-段三_commitC_重錨解封.md
GSA_EXPECT = {
    "0m":   {"G006": 365.84, "G007": 359.43, "G009": 153.19,
             "G010": 283.87, "G014": 128.63, "G017": 433.68},
    "3.5m": {"G006": 365.84, "G007": 370.01, "G009": 153.19,
             "G010": 301.17, "G014": 129.74, "G017": 433.68},
}
# 合併後不達標之標旗轉出（KL (A) 追認）
ROUTE_OUT = {"G009": "轉F.2(同歸戶R4有達標宗·級1相鄰街廓)",
             "G014": "轉F.4(逃生門·2×G≥MinA_區·7-5≥½增配)"}
# MinA_區（重劃區內最小分配面積標準）之**施加路徑**＝本檔之 `_mina_by_block()`
#   （`grep -n "def _mina_by_block" verify/wf_f0.py`）→ `wf_f4` 取 `min(mina.values())`
#   （`grep -n "mina_qu = min" verify/wf_f4.py`）→ ½線補償。
#   🔴 **舊註曾寫「正典＝`wd4_tier_list._mina_by_block()`」——不成立·已更正**：
#     · `wf_f4` **全檔零呼叫** `wd4_tier_list`（`grep -n "wd4_tier_list" verify/wf_f4.py` ⇒ 0 命中）；
#     · `run_verification` 明寫「單一真相源＝`wf_f0._mina_by_block`」
#       （`grep -n "單一真相源" verify/run_verification.py`）；
#     · 兩支**簽章不同、不可互代**：本支收 3 參數回 `dict`；`wd4` 收 4 參數回 `(dict, min)` 2-tuple
#       （`grep -n "def _mina_by_block" verify/wf_f0.py verify/wd4_tier_list.py`）。
#     ⇒ `wd4` 那支係**清單／回歸**路徑；**本支才是土地後果路徑**。
#   本檔原有之區標準字面常數為**孤兒**（僅定義、零讀取、全倉無 import）已刪，避免日後被誤引
#   為權威（失敗考古 #26 型）。本檔一切比較用 `mina[blk]`＝**配地可行性**口徑（`grep -n "mina\[" verify/wf_f0.py`），
#   與 ½線補償之 **MinA_區** 口徑係二事、勿混（見 plan v3 §9.2 🔒 二口徑註記）。


def _mina_by_block(ns, snap, cb_by):
    """per-block MinA_i ＝ `round(D_avg_i, 2) × min_width_i`（**正典寫法**·K-8 §二-1）。

    🔴 **本支為「土地後果」路徑**（孿生之 `wd4_tier_list._mina_by_block` 為**清單／回歸**路徑）：
    本函式之輸出經 `wf_f4` 之 `mina = wf_f0._mina_by_block(...)`
    （`grep -n "wf_f0._mina_by_block" verify/wf_f4.py`）成為 `mina[blk]`，
    消費於 E1/E2 落位、增配與遞補之各判準（`grep -n "mina\\[" verify/wf_f4.py`）；
    另經 `mina_qu = min(mina.values())`（`grep -n "mina_qu = min" verify/wf_f4.py`）
    供 **½線補償**判定（`grep -n "mina_qu" verify/wf_f4.py`）。
    亦為 `wf_f2`／`wf_f3`／`run_verification` 之同一來源
    （`grep -rn "_mina_by_block" --include="*.py" .`）。
    ⇒ **改本函式＝改面積歸屬**；孿生那支改了只動清單與回歸斷言。

    ⚠️ **二口徑分明**（見本檔 `mina_qu` 註）：`mina[blk]`＝**配地可行性**（各街廓）；
    `mina_qu`＝**½線補償**口徑（重劃區內標準）。**勿混。**

    ⚠️ **round 位置與正典有落差**：碼面實作為 `round(D_avg_i × min_width_i, 2)`（先乘後捨），
    正典 K-8 §二-1 為 `round(D_avg_i, 2) × min_width_i` 且「`round()` 只在輸出層」。
    **等值前提＝乘積本身已 ≤2dp**，「深度已 2dp」**並不充分**（2dp 深度 ×3.5，
    深度第二位小數為奇數時必生第三位）。本案六街廓**四個真分歧、各 0.005㎡**
    （R1/R2/R5/R6），`mina_qu` 因 min 落在 R4（乘積恰 2dp）而兩形相同 ⇒ **今日零後果**，
    惟係**案件相依之巧合**。已登記：泛用阻塞項登記表 **GB-7**
    （`grep -n "GB-7" docs/reports/W-G.4_泛用阻塞項登記表.md`）；
    **K-6-A2 拆除 per-block MinA 之達標角色時一併收**。

    🗄️ 其**達標判定角色已由 K-6 §零-4 廢除**（改寬深雙檢·K-6 §零-1）——
    **已裁定、K-6-A2 尚未實作**，故本函式現仍為碼面實際走的路徑。

    回傳 `{label: MinA_i}`（僅可建築土地）。
    """
    fcb = ns["F3_CATEGORY_BURDEN"]
    m = {}
    for b in cb_by.values():
        if fcb.get(b.get("category", ""), "") == "可建築土地":
            lbl = b["label"]
            d = float(snap["blocks"][lbl]["街廓分配深度_m"])
            mw = float(ns["get_min_lot_size"](
                b["category"], float(snap["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
            m[lbl] = round(d * mw, 2)
    return m


def _decide(ns, snap, cb_by, omap, g_rows_A, mina):
    """級0/0' 決策（吃 trunk A 之 g_rows）。回傳 decisions[list]。
    每筆＝{gid, blk, kind, target, merged[list], zones[set]}。"""
    g = lambda p: omap.get(p, "")
    A = {r["暫編地號"]: r for r in g_rows_A if r.get("推進側別") in ("left", "right")}
    zone_of = snap["財務接線_v3"]["原地號_區段"]
    cell = {}
    for r in A.values():
        cell.setdefault((g(r["原地號"]), r["所屬街廓"]), []).append(r)
    decisions = []
    for (gid, blk), lots in sorted(cell.items()):
        if len(lots) < 2:
            continue
        zones = {zone_of[l["原地號"]] for l in lots}

        def _key(r):   # G 最大；並列取暫編字典序最小
            return (-float(r["G(㎡)"]), r["暫編地號"])
        qual = [l for l in lots
                if float(l["G(㎡)"]) >= mina[blk] and not l["畸零地旗標"].strip()]
        unq = [l for l in lots if l not in qual]
        if not unq:
            kind, target, merged = "全達標·無須併", None, []
        elif qual:
            kind = "級0"
            target = sorted(qual, key=_key)[0]
            merged = unq
        else:
            kind = "級0'"
            target = sorted(lots, key=_key)[0]
            merged = [l for l in lots if l is not target]
        decisions.append({
            "gid": gid, "blk": blk, "kind": kind,
            "target": (target["暫編地號"] if target else None),
            "merged": [l["暫編地號"] for l in merged],
            "zones": sorted(zones),
        })
    return decisions


def _transform(build_parcels, decisions):
    """F.0 變換（deepcopy）：標的宗吞被併宗 a → 面積_m2；移除被併宗＋梯3 4 宗。
    回傳 (f0_parcels, removed_set)。"""
    f0 = copy.deepcopy(build_parcels)
    by_id = {tp["暫編地號"]: tp for tp in f0}
    for d in decisions:
        if not d["target"]:
            continue
        add = 0.0
        for m in d["merged"]:
            add += (float(by_id[m].get("分攤登記面積_m2", 0) or 0)
                    + float(by_id[m].get("面積_m2", 0) or 0))
        t = by_id[d["target"]]
        t["面積_m2"] = round(float(t.get("面積_m2", 0) or 0) + add, 2)
    removed = set(TIER3_LOTS) | {m for d in decisions for m in d["merged"]}
    f0 = [tp for tp in f0 if tp["暫編地號"] not in removed]
    return f0, removed


def _proj_order(ns, cad, parcels, blk):
    """該街廓之投影序（暫編地號 list）。"""
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pib = [tp for tp in parcels if tp["所屬街廓"] == blk
           and not tp.get("_is_ghost_sliver")]
    return [tp["暫編地號"] for tp in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]


def compute(ctx_by_tag):
    """F.0 逐情境。ctx_by_tag[tag] = {ns, fake_st, cb_by, cad, snap, build,
    params, winners, forced, setback, gA(trunk A g_rows)}。
    回傳 {tag: {...tables, anchors}}。"""
    out = {}
    for tag, c in ctx_by_tag.items():
        ns, snap, cb_by, cad = c["ns"], c["snap"], c["cb_by"], c["cad"]
        omap = c["omap"]
        mina = _mina_by_block(ns, snap, cb_by)
        decisions = _decide(ns, snap, cb_by, omap, c["gA"], mina)

        # 停機閘（決策層；破即 RuntimeError）
        for d in decisions:
            if d["target"] and len(d["zones"]) != 1:
                raise RuntimeError(
                    f"🔴 停機#2 區段不一致：{d['gid']}/{d['blk']} zones={d['zones']}"
                    "（A 折算係數≠1，須域裁 7-4 雙模式）")
        # 停機#3：被併宗 ∩ 街角 winners / forced 保留地
        win_set = {v for w in c["winners"].values()
                   for v in (w.get("p1_end"), w.get("p2_end")) if v}
        forced_set = set()
        for lbl, fo in (c["forced"] or {}).items():
            pass   # forced 保留地為「街廓端」概念，被併宗非保留地本體；winner 交集為主閘
        all_merged = {m for d in decisions for m in d["merged"]}
        _wconf = sorted(all_merged & win_set)
        if _wconf:
            raise RuntimeError(f"🔴 停機#3 被併宗為街角 winner：{_wconf}")

        f0_parcels, removed = _transform(c["build"], decisions)

        # trunk B：F.0 終態（結構不變量永久閘於 run_step_g 內自動適用）
        sgB = run_step_g(ns, c["fake_st"], list(cb_by.values()), cad, snap,
                         c["params"], f0_parcels, c["winners"], c["forced"], c["setback"])
        B = {r["暫編地號"]: r for r in sgB["g_rows"] if r.get("推進側別") in ("left", "right")}
        g_tab, diag_tab, slot_tab = build_step_g_tables(sgB)

        # 六格 G(Σa) 自檢（±0.01；避 #14 刀口）
        # 🆕 F-7-3（claude.ai 2026-07-25）：**收集全部不符後一次 raise**。
        #   舊碼於**首個**值不符即 raise ⇒ 覆蓋率閘（下方）在**非 BAKE 永不執行**
        #   （實證：非 BAKE log grep「GSA 覆蓋率」零命中·只有 BAKE 有；而 §11.3 明定 BAKE
        #   **僅側錄、不可認證** ⇒ 我原稱「F-1 fired on the real case」須限定為 BAKE 側錄）。
        #   更實際之害：P-H 會被迫**打地鼠**（改 G014→才看見 G007→再改→才看見下一個）。
        #   ⇒ 值不符與覆蓋率不符**各自收集**，迴圈後**合併單一 raise**，帶出完整重錨清單。
        gsa = {}
        _val_bad = []
        for d in decisions:
            if not d["target"]:
                continue
            G = float(B[d["target"]]["G(㎡)"])
            gsa[d["gid"]] = G
            exp = GSA_EXPECT[tag].get(d["gid"])
            if exp is not None and abs(G - exp) > 0.01:
                _val_bad.append(f"{d['gid']} G(Σa)={G:.2f} ≠ 錨 {exp}")
        # 🆕 F-1（claude.ai 2026-07-25）：**GSA 覆蓋率硬閘**——修「錨消失即靜默放行」。
        #   舊碼 `if not d["target"]: continue` ＋「僅走 decisions」⇒ 某 gid 若**無合併決策**，
        #   其 `GSA_EXPECT` 鍵**永不被評估** ⇒ **沒人檢查 ≠ 相符**。
        #   ⚠️ NOTE-2（reviewer）：**不得在此斷言單一成因**——`_decide` 有**兩條**路徑使 gid 不進
        #   `gsa`（`_decide` 之 `len(lots)<2` ／ `全達標·無須併`→target=None·`grep -n "len(lots) < 2" verify/wf_f0.py`），實例 G007@3.5m
        #   **兩條都涉及**（R5 因源宗移出剩 1 宗走前者·R3 走後者被報）⇒ 訊息一律**印實際決策**（見下）。
        _uncov = sorted(set(GSA_EXPECT[tag]) - set(gsa))
        if _uncov:
            # W-3（reviewer）：**禁斷言未查證之成因**。舊訊息寫死「該歸戶宗數<2」，但 gid 不進 `gsa`
            #   有**兩條**路徑：`_decide` 之 `len(lots)<2 → continue`／`全達標·無須併`（target=None
            #   → 本迴圈 `if not d["target"]: continue`）。實例 G007@3.5m 走的是**後者**（R3 有 2 宗、
            #   級別＝全達標·無須併），舊訊息對之為**錯**。改為**印實際逐塊決策**、不猜原因。
            _detail = []
            for _g in _uncov:
                _ds = [f"{d['blk']}:{d['kind']}"
                       f"{'(target=' + str(d['target']) + ')' if d.get('target') else '(無target)'}"
                       for d in decisions if d["gid"] == _g]
                _detail.append(f"{_g}→[{'；'.join(_ds) if _ds else '該情境無任何決策列'}]")
            _cov_msg = (f"錨鍵 {_uncov} **未被任何一次比對評估**"
                    f"（其決策現況：{'｜'.join(_detail)}）⇒ **沒人檢查≠相符**。"
                    f"成因請依上列決策自行研判（如：被併宗遭上游消費移出→標的宗回復單獨→"
                    f"改判『全達標·無須併』或該塊宗數<2）；確認係合法連動"
                    f"（如 **K-6 §二 段三**之跨街廓同歸戶集中——K-6 起一律歸七級調配 F.0／F.2；"
                    f"⚠️ 舊指標『M-5 街角救援』已於 K-6 §四作廢並封存至 `verify/archive/`，"
                    f"**勿再據以研判**）"
                    f"則於 P-H 重錨（刪鍵或改值），否則係上游漏配之 bug。已評估鍵＝{sorted(gsa)}")
        else:
            _cov_msg = ""
        # ── 合併單一 raise（值不符 ＋ 覆蓋率不符·一次帶出 P-H 完整重錨清單） ──
        if _val_bad or _cov_msg:
            _parts = [f"🔴 GSA 錨檢破（{tag}）——**一次列出全部**（F-7-3：禁首個即 raise 致打地鼠）："]
            if _val_bad:
                _parts.append(f"【值不符 {len(_val_bad)} 項】" + "；".join(_val_bad))
            if _cov_msg:
                _parts.append(f"【未被評估】{_cov_msg}")
            _msg = "\n  ".join(_parts)
            if os.environ.get("WV_BAKE"):
                print(f"⚠️ [WV_BAKE] {_msg}")
            else:
                raise RuntimeError(_msg)

        # 合併決策表（含 verdict/去向；診斷 Δ 非閘）
        A = {r["暫編地號"]: r for r in c["gA"] if r.get("推進側別") in ("left", "right")}
        dec_rows = []
        for d in decisions:
            if not d["target"]:
                dec_rows.append({"情境": tag, "歸戶": d["gid"], "街廓": d["blk"],
                                 "級別": d["kind"], "標的宗": "—", "被併宗": "",
                                 "Σa(㎡)": "", "G(Σa)(㎡)": "", "MinA_街廓": mina[d["blk"]],
                                 "達標": "—", "去向": "全達標·留置原位", "Δ非線性(㎡)": ""})
                continue
            G = gsa[d["gid"]]
            sa = round(float(B[d["target"]]["a 面積(㎡)"]), 2)
            sG_naive = round(float(A[d["target"]]["G(㎡)"])
                             + sum(float(A[m]["G(㎡)"]) for m in d["merged"]), 2)
            ok = G >= mina[d["blk"]]
            dest = ("達標·留置原位" if ok else ROUTE_OUT.get(d["gid"], "🔴無下一級·停機"))
            dec_rows.append({
                "情境": tag, "歸戶": d["gid"], "街廓": d["blk"], "級別": d["kind"],
                "標的宗": d["target"], "被併宗": ";".join(d["merged"]),
                "Σa(㎡)": sa, "G(Σa)(㎡)": round(G, 2), "MinA_街廓": mina[d["blk"]],
                "達標": ("✅" if ok else "🔴"), "去向": dest,
                "Δ非線性(㎡)": round(abs(G - sG_naive), 2),
            })
            # 停機#4：不達標且無去向
            if not ok and d["gid"] not in ROUTE_OUT:
                raise RuntimeError(
                    f"🔴 停機#4：{d['gid']} 合併後 G(Σa)={G:.2f}<MinA 且無下一級可走（§7 全鏈窮盡）")

        # 旗標消長歸因
        fa = {k for k, r in A.items() if r["畸零地旗標"].strip()}
        fb = {k for k, r in B.items() if r["畸零地旗標"].strip()}
        flag_rows = []
        for k in sorted(fa | fb):
            if k in fa and k in removed:
                cat = "因移除消失"
            elif k in fa and k not in fb:
                cat = "因合併脫旗"
            elif k in fb and k not in fa:
                cat = "新生"
            else:
                cat = "沿用"
            flag_rows.append({"情境": tag, "暫編地號": k, "歸因": cat,
                              "trunkA旗標": ("有" if k in fa else ""),
                              "trunkB旗標": ("有" if k in fb else "")})

        # 位次序不變（投影序，k*-無關；gate#9）＋標的宗毗鄰（KL 具名原則，gate#10）。
        #   毗鄰於**約簡序**（oA 去 block-wide 移除宗）上取——非原序 i±1 濾除（後者丟空、漏 i-2）。
        #   gate#9（oB==約簡序）為序不變之強式，數學上蘊含毗鄰；gate#10 為 KL「標的宗左右毗鄰不變」之具名複述。
        pos_viol, adj_viol = [], []
        blocks = sorted({r["所屬街廓"] for r in A.values()})

        def _nbrs(seq, x):
            k = seq.index(x)
            return seq[max(0, k-1):k] + seq[k+1:k+2]
        for blk in blocks:
            oA = _proj_order(ns, cad, c["build"], blk)
            oB = _proj_order(ns, cad, f0_parcels, blk)
            exp = [x for x in oA if x not in removed]   # 約簡序
            if oB != exp:
                pos_viol.append((blk, exp, oB))
            for d in decisions:
                if d["blk"] != blk or not d["target"]:
                    continue
                nb_exp = _nbrs(exp, d["target"])         # 標的宗於約簡序之左右鄰
                nb_B = _nbrs(oB, d["target"])
                if nb_exp != nb_B:
                    adj_viol.append((d["target"], nb_exp, nb_B))

        # 池差（釋池量＝area_geom；真閘＝池差 baseline）
        poolB = {lbl: round(float(v["池總=幾何剩餘(㎡)"]), 2)
                 for lbl, v in sgB["pool_diag"].items()}
        poolA = {lbl: round(float(v["池總=幾何剩餘(㎡)"]), 2)
                 for lbl, v in c["poolA"].items()}
        pool_rows = [{"情境": tag, "街廓": lbl,
                      "池_v3(㎡)": poolA[lbl], "池_F.0(㎡)": poolB[lbl],
                      "池差(㎡)": round(poolB[lbl] - poolA[lbl], 2)}
                     for lbl in sorted(poolB)]

        kstar = {lbl: v["k*"] for lbl, v in sgB["pool_diag"].items()}
        verd = {lbl: v["判定"] for lbl, v in sgB["pool_diag"].items()}
        out[tag] = {
            "g_tab": g_tab, "diag_tab": diag_tab, "slot_tab": slot_tab,
            "sgB_rows": sgB["g_rows"],   # 🆕 F.1 消費（原始列含 cut_coords；純加性，12 檔 f0 baseline byte 不動）
            "f0_parcels": f0_parcels,    # 🆕 F.2 消費（trunk B parcels＝跨街廓搬 a′ 之母體；純加性）
            "poolB_diag": {lbl: sgB["pool_diag"][lbl] for lbl in sgB["pool_diag"]},
            "dec_rows": dec_rows, "flag_rows": flag_rows, "pool_rows": pool_rows,
            "decisions": decisions, "removed": sorted(removed), "gsa": gsa,
            "kstar": kstar, "verdict": verd,
            "pos_viol": pos_viol, "adj_viol": adj_viol,
            "n_flag_A": len(fa), "n_flag_B": len(fb),
            "mina": mina,
        }
    return out
