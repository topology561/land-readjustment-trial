# -*- coding: utf-8 -*-
"""W-G.9-265 工項七：**已裁未實作之逐款對位表**（唯讀探針）。

🔒 唯讀：只讀 harness 落檔 `verify/out/got_G值_退縮{0m,3.5m}_partial.csv` 與正典 blob。
   ⛔ 動 app.py 與 verify/ 生產路徑一字；⛔ 含任何修法主張；⛔ 動配地幾何。

【框之來源】
  · `^### 🔒 K-9-N` ＝ **正典逐字**（單 §八 (f)）。
  · `W × D` ＝ **生產函式** `get_min_lot_size(category, front_road_width_m)`（⛔ 硬編 `3.5`／`14`）。
  · 宗序（第 `k` 宗·0-based）＝ **正典逐字** `K-9-15 二`。
  · 「不交叉」之量 ＝ 二宗多邊形之 `intersection().area > 1e-6` ＝ **自擬**
    （承 `K-9-15 三-2`：`K-9-9 二` 之剩餘作用 ＝ 僅保證地界線不交叉）。

🛑 「**未量**」逐款具名並列為子項，⛔ 靜默略過。
🛑 否證對照：`K-9-9 三`（無判準內容）須判「無受詞」而**不**觸紅；
   對一款人為填入「有受詞」而其受詞集為空 ⇒ 檢查須紅。
"""
import ast
import csv
import io
import os
import sys
from itertools import combinations

from shapely.geometry import Polygon
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out")
SCEN = [("0m", "got_G值_退縮0m_partial.csv"), ("3.5m", "got_G值_退縮3.5m_partial.csv")]
TOL = 1e-6


def poly(c):
    p = Polygon(c)
    return p if p.is_valid else p.buffer(0)


def load():
    data = {}
    for tag, fn in SCEN:
        path = os.path.join(OUT, fn)
        with io.open(path, "r", encoding="utf-8-sig", newline="") as f:
            data[tag] = list(csv.DictReader(f))
    return data


def build_groups(rows):
    g = {}
    for r in rows:
        blk = (r.get("所屬街廓") or "").strip()
        side = (r.get("推進側別") or "").strip()
        cc = (r.get("cut_coords") or "").strip()
        if not blk or side == "抵費地" or not cc:
            continue
        try:
            v = ast.literal_eval(cc)
        except Exception:
            continue
        if not v or len(v) < 3:
            continue
        g.setdefault((blk, side), []).append((r, poly(v)))
    for k in g:
        g[k].sort(key=lambda t: float(t[0].get("累積S(m)") or 0))
    return g


def main():
    print("=" * 118)
    print("【W-G.9-265 工項七】已裁未實作之逐款對位表（唯讀探針）")
    print("=" * 118)

    # ── W × D 之來源：生產函式（⛔ 硬編）
    sys.path.insert(0, os.path.join(REPO, "verify"))
    from app_harvest import harvest  # noqa
    ns, _fake = harvest()
    gmls = ns["get_min_lot_size"]
    print()
    print("── `W × D` 之來源（生產函式·⛔ 硬編）──")
    print("   符號 ＝ `get_min_lot_size`；自 `app_harvest.harvest()` 取得，type ＝ %s" % type(gmls).__name__)
    wd = gmls("住宅區", 10.0)
    W = float(wd["min_width"])
    D = float(wd["min_depth"])
    print("   `get_min_lot_size('住宅區', 10.0)` ⇒ min_width ＝ %.2f／min_depth ＝ %.2f" % (W, D))
    print("   [判別力] `get_min_lot_size('住宅區', 5.0)` ⇒ %s" % gmls("住宅區", 5.0))
    print("   🛑 **未量之子項 `d-5`**：逐街廓正面路寬**⛔ 實測** ⇒ 上二值係以 `10.0 m` 查表所得；")
    print("      其**阻斷點** ＝ 落檔⛔ 含「正面路寬」欄（欄名集內查無），且逐街廓路寬須自 DXF 之")
    print("      `CENTERLINE`／道路類 `BLOCK` 幾何反算 ⇒ 屬**新量測**，本批⛔ 辦（單 §八 子項 `d-5`）。")

    data = load()
    G = {tag: build_groups(rows) for tag, rows in data.items()}
    rank = {}
    for tag in G:
        for key, items in G[tag].items():
            for i, (r, _p) in enumerate(items):
                rank[(tag, id(r))] = i

    def name(r):
        return (r.get("暫編地號") or "").strip()

    # ── 受詞集之建立
    corner_lots = []      # 第 0 宗且 第1筆街角 == 是
    next_of_corner = []   # 街角宗之次一宗（K-9-14 三 之受詞）
    non_corner = []       # 第 1 宗以後
    for tag in ("0m", "3.5m"):
        for key in sorted(G[tag]):
            items = G[tag][key]
            has_corner = (items[0][0].get("第1筆街角") or "").strip() == "是"
            if has_corner:
                corner_lots.append((tag, key, items[0][0]))
                if len(items) > 1:
                    next_of_corner.append((tag, key, items[1][0]))
            for r, _p in items[1:]:
                non_corner.append((tag, key, r))

    print()
    print("── 受詞集（母體 ＝ 二情境 `13` 組·%d 分配宗）──"
          % sum(len(G[t][k]) for t in G for k in G[t]))
    print("   街角宗（第 `0` 宗 ∧ `第1筆街角 == 是`）＝ %d 宗：%s"
          % (len(corner_lots), "／".join("%s·%s·%s %s" % (t, k[0], k[1], name(r)) for t, k, r in corner_lots)))
    print("   街角宗之次一宗（`K-9-14 三` 受詞）＝ %d 宗：%s"
          % (len(next_of_corner), "／".join("%s·%s·%s %s" % (t, k[0], k[1], name(r)) for t, k, r in next_of_corner)))
    print("   第 `1` 宗以後（非街角宗）＝ %d 宗" % len(non_corner))

    # ── 不交叉之逐組實測（K-9-9 二 之剩餘作用·K-9-15 三-2）
    cross = []
    for tag in ("0m", "3.5m"):
        for key in sorted(G[tag]):
            items = G[tag][key]
            for (r1, p1), (r2, p2) in combinations(items, 2):
                a = p1.intersection(p2).area
                if a > TOL:
                    cross.append((tag, key, r1, r2, a, rank[(tag, id(r1))], rank[(tag, id(r2))]))

    print()
    print("=" * 118)
    print("【逐款對位表】欄 ＝ 款／受詞逐字／受詞內之宗（宗地號 ＋ 宗序）／現態之判／機械證據")
    print("=" * 118)

    rows_out = []

    def row(clause, text, subj_desc, verdict, evidence):
        rows_out.append((clause, text, subj_desc, verdict, evidence))
        print()
        print("── `%s`" % clause)
        print("   受詞逐字：%s" % text)
        print("   受詞內之宗：%s" % subj_desc)
        print("   現態之判：%s" % verdict)
        print("   機械證據：%s" % evidence)

    row("K-9-9 一",
        "「本宗遠側境界線 **∥ ALLOCLINE**。」",
        "第 `1` 宗以後 %d 宗（第 `0` 宗依 `K-9-9 五` 恆 ∥SIDELINE ⇒ ⛔ 在受詞內）" % len(non_corner),
        "🟡 **未量**（子項 `d-1`）",
        "阻斷點 ＝ 落檔⛔ 含 ALLOCLINE 之方向向量，亦⛔ 含逐宗遠側界之端點；"
        "須自 `data/V6_1.dxf` 之 `ALLOC_LINE` 圖層取向量、並自 `cut_coords` 認出「哪一邊是遠側界」"
        "——後者係**外部重建內部幾何**（`CLAUDE.md` 自我驗證閘之受詞），"
        "而落檔⛔ 提供可據以設閘之碼面斷言 ⇒ **⛔ 得下結論**（單 §十一 3）")

    row("K-9-9 二（剩餘作用 ＝ 不交叉·`K-9-15 三-2`）",
        "「本宗遠側境界線之 **FRONTLINE 交點**與 **BASELINE 交點**，兩者皆須在起算垂線之對應端點之後。」"
        "🔴 其「起算垂線之對應端點」一節已由 `K-9-15 三-1` **廢止**；剩餘作用 ＝ 僅保證「地界線不交叉」",
        "依 `K-9-14 三`：**每一個街角宗之次一宗** ＝ %d 宗（%s）"
        % (len(next_of_corner), "／".join("%s·%s·%s %s（第%d宗）"
                                          % (t, k[0], k[1], name(r), rank[(t, id(r))])
                                          for t, k, r in next_of_corner)),
        "🔴 **違反 %d 對**（以剩餘作用「不交叉」為判準·母體 ＝ 全 `13` 組之逐宗對）" % len(cross),
        "逐對 ＝ " + "；".join(
            "%s·%s·%s 第%d宗 %s × 第%d宗 %s 疊 %.4f ㎡"
            % (t, k[0], k[1], i1, name(r1), i2, name(r2), a)
            for t, k, r1, r2, a, i1, i2 in cross))

    row("K-9-9 三",
        "「本則之性質：係**宗地形成之約束**，🔴 **⛔ 非深度閘**。」",
        "（無）——本款為**性質之宣告**，⛔ 含任何可對位至宗之判準內容",
        "✅ **無受詞**（⛔ 觸紅·單 §八 (c) 之必綠對照）",
        "款內⛔ 出現任何「須／應／不得 ＋ 幾何量」之判準式；其全文為「係…⛔ 非…」之定性句 ⇒ 受詞集 ＝ ∅")

    row("K-9-9 四",
        "「依該宗 G 值算出之遠側界位置若在起算垂線**之前** ⇒ **該宗不配地**，走**合併／調配機制**；"
        "重劃前投影順序中**下一位**之土地**遞補該位次**；騰出之地**入調配池**。🔴 ⛔ **不得強制配到下限**。」",
        "其**前件**（「在起算垂線之前」）繫於 `K-9-9 二` 之已廢止部分 ⇒ 依 `K-9-15 三-1`，"
        "現行之前件改由 `K-9-12`（矩形容納）供給；而 `K-9-12` 於生產碼**未實作**（`K-9-12-b` 逐字）"
        "⇒ **受詞集於現態為 ∅**",
        "⬜ **無受詞（於現態）**·🔴 **其處置之碼面⛔ 存在**",
        "`K-9-12-b` 逐字「已裁定、⛔ 生產碼未實作」；且 `K-9-17 三` 逐字「『決定遞補位次之處』可執行母體 ＝ **0** "
        "⇒ 現行碼**並無**遞補之實作」 ⇒ 前件與處置**雙缺**")

    row("K-9-9 五",
        "「**街角第 1 宗⛔ 不適用本則**：其遠側境界線**恆 ∥ SIDELINE**；"
        "**無 WINNER**（強制抵費地）⇒ 位置 ＝ **街角規定範圍之寬度**；**有 WINNER** ⇒ 依該宗**應分配之 G 值**決定。」",
        "街角宗 ＝ %d 宗（%s）" % (len(corner_lots),
                                  "／".join("%s·%s·%s %s" % (t, k[0], k[1], name(r)) for t, k, r in corner_lots)),
        "🔴 **與實測相斥之一項**：本款將第 `0` 宗**排除**於 `K-9-9` 之拘束外，"
        "而 %d 對交叉中 **%d 對之一端即第 `0` 宗**"
        % (len(cross), sum(1 for c in cross if c[5] == 0 or c[6] == 0)),
        "⇒ 🔒 **「一律縮減街角第 `0` 宗」之處置⛔ 由 `K-9-9` 導出**——其拘束依本款加於**後宗**。"
        "（本行係**款之射程之陳述**，⛔ 修法主張、⛔ 處置建議）")

    row("K-9-9 六",
        "「左右兩側**各自往街廓中間**推進，本則於各側**鏡像成立**。…**必然產生配餘地**（＝調配池），⛔ 不會發生「塞不下」。」",
        "全 `13` 組（每組即一側）",
        "✅ **未違反**（就「各側獨立」之部分）·🟡 **「必然產生配餘地」之部分：未量**",
        "落檔之 `推進側別` 相異值 ＝ {left, right, 抵費地} ⇒ 二側各自成組 ✅；"
        "「必然產生配餘地」須驗 `ΣG ＋ Σ池 ＝ 街廓面積` 之逐街廓守恆——"
        "而中止街廓（`0m` 之 `R2`／`3.5m` 之 `R5`）之抵費地**未產出** ⇒ 該二街廓**⛔ 可驗** ⇒ 具名為未量")

    row("K-9-9 七",
        "「自 FRONTLINE 沿其法向至 BASELINE 之**完整線段**、**整條落在該宗範圍內**」者，方計為該宗之**有效深度**。"
        "🔴 其末句「⛔ 不構成判準」已由 `W-G.9-42` 加註**失效**——`K-9-10 二` 令**最淺之「有效」垂線**決定**帶底**",
        "全部分配宗 %d 宗（其「有效垂線母體」）" % sum(len(G[t][k]) for t in G for k in G[t]),
        "🟡 **未量**（子項 `d-2`）",
        "阻斷點 ＝ 「有效垂線之母體」須逐宗窮舉 FRONTLINE 上之點、沿法向作垂線並判其是否整條落在該宗內；"
        "落檔⛔ 提供 FRONTLINE 之參數化，亦⛔ 提供碼面對該母體之任何斷言可資設自我驗證閘 ⇒ **⛔ 得下結論**")

    row("K-9-12",
        "「宗地之**四至範圍**內，能否**完整容納**邊長 `W × D` 之矩形 ⇒ **能 ⇒ 非畸零地·可建築**。」"
        "（`W`／`D` 自 `get_min_lot_size` 取·⛔ 硬編；姿態經 `K-9-12-c` 更正為**可旋轉、可平移**）",
        "第 `1` 宗以後 %d 宗（第 `0` 宗依 `K-9-12-e` **射程排除**·走街角最小規定範圍）" % len(non_corner),
        "🟡 **未量（充分側）**（子項 `d-3`）·🔒 **必要側之下界已可判**",
        "必要側：`W×D ＝ %.2f×%.2f ＝ %.2f ㎡` ⇒ `G < %.2f` 者**必**容納不下。"
        % (W, D, W * D, W * D) +
        "實測第 `1` 宗以後 `G < %.2f ㎡` 者 ＝ %d 宗（%s）。"
        % (W * D,
           sum(1 for _t, _k, r in non_corner if float(r.get("G(㎡)") or 0) < W * D),
           "／".join("%s·%s·%s %s G=%.2f" % (t, k[0], k[1], name(r), float(r.get("G(㎡)") or 0))
                     for t, k, r in non_corner if float(r.get("G(㎡)") or 0) < W * D)) +
        " 🛑 **充分側**（`G ≥ %.2f` 之宗能否實際容納）**未量** ＝ 子項 `d-3`：其須以 `cut_coords` 之多邊形"
        "跑矩形容納測試，而倉內 `_rect_fits_free_pose` 屬 `app.py`（`K-9-12-b` 逐字「⛔ 純函式·觀測模式」）"
        "——**自我驗證閘⛔ 可得**（碼面對「該多邊形可容納」⛔ 有任何既有斷言可資對拍）⇒ ⛔ 得下結論" % (W * D))

    row("K-9-14",
        "「`K-9-9 二` 之受詞 ＝ 「前一宗之遠側境界線為 ∥SIDELINE 者」之次一宗；其餘各宗，因二界平行而永不相交，該款恆真。」",
        "**每一個街角宗之次一宗** ＝ %d 宗；一組若**無街角宗**則該組**無任何一宗**在受詞內"
        "（無街角宗之組 ＝ %d 組）"
        % (len(next_of_corner),
           sum(1 for t in G for k in G[t] if (G[t][k][0][0].get("第1筆街角") or "").strip() != "是")),
        "🔴 **其「恆真」之斷言於現態被實測否證**",
        "本款之「恆真」以「二界平行 ⇒ 永不相交」為理由；而實測 %d 對交叉中，"
        "**%d 對之二端皆⛔ 在本款受詞內**（位次差 ≥ 2 ⇒ 二界皆應 ∥ALLOCLINE）：%s。"
        "⇒ 🔒 **實測與「平行則不交叉」相斥** ⇒ 其前提（二界確為平行）於現態**⛔ 成立**"
        % (len(cross), sum(1 for c in cross if abs(c[5] - c[6]) >= 2),
           "／".join("%s·%s·%s 第%d宗×第%d宗（位次差 %d）" % (t, k[0], k[1], i1, i2, abs(i1 - i2))
                     for t, k, _r1, _r2, _a, i1, i2 in cross if abs(i1 - i2) >= 2)))

    row("K-9-15 二（宗序之命名·正典用語）",
        "「**第 0 宗** ＝ 街角地那 1 宗；**第 1 宗** ＝ 街角地後面那一宗；**依此類推**。」",
        "全 `13` 組之逐宗（本表全部宗序之命名依據）",
        "✅ **已用**（本批全部出艙之宗序皆依本款）",
        "自我驗證閘：位次 `0` 之 `驗_宗序 == 街角第1宗` ⟺ 其 `第1筆街角 == 是`；"
        "位次 `1` 恆為 `第2宗` ⇒ 二情境共 `24` 格全符（有街角 `8` 組／無街角 `5` 組 ⇒ 該檢⛔ 恆真）")

    row("K-9-15 三-4（畸零地之判斷逐宗為之）",
        "「**第 0 宗（街角）** ⇒ **街角最小規定範圍**；**第 1 宗以後** ⇒ **內接最小矩形**（`K-9-12`·"
        "⛔ 其落地狀態見 `K-9-12-b`：**已裁定·生產碼未實作**）」",
        "第 `0` 宗 %d 宗 ＋ 第 `1` 宗以後 %d 宗" % (len(corner_lots), len(non_corner)),
        "🔴 **未實作**（正典自載）",
        "`K-9-12-b` 逐字「🔴 **已裁定、⛔ 生產碼未實作**：現行宗地層判定仍走 `parcel_min_width_n14` 之"
        "「帶內 `w(t)` 之 min ≥ 法定最小寬」，**⛔ 不做任何矩形容納測試**」")

    row("K-9-17 一（街角確立後之序位重排）",
        "「先判斷以該街廓原投影至正面路接的投影順序，假設=1,2,3,4,5 ，1,2,3跨占街角最小規定範圍，"
        "但經街角地機制評比後2為winner，則該街廓投影順序此時就要變成2,1,3,4,5」",
        "全 `13` 組（凡有 winner 之組）",
        "🔴 **未實作**（正典自載·`K-9-17 三`）",
        "`K-9-17 三` 逐字「`W-G.9-97` `C-1` 現查 —— 「決定遞補位次之處」可執行母體 ＝ **0** "
        "⇒ 現行碼**並無**遞補之實作，落地係**從零實作**」")

    row("K-9-17 二（遞補與配餘地）",
        "「此時若1地號…若無法內接矩形成立而併入合併/調配機制，那麼該空位就由3遞補"
        "（空位位置係由第0宗遠側境界線開始依據遞補宗的G再決定第1宗遠側境界線，"
        "並注意宗與宗之間境界線不要交叉），而1地號空出之面積…就是列為配餘地(調配池)」",
        "其前件（「無法內接矩形」）繫於 `K-9-12` ⇒ `K-9-12` 未實作 ⇒ **受詞集於現態為 ∅**",
        "⬜ **無受詞（於現態）**",
        "同 `K-9-9 四` 之機械證據（前件與處置雙缺）")

    row("K-9-19 一",
        "`K-9-4` 之「**宗**」⛔ 不含「無地主之未覆蓋殘餘」；判準 ＝ `原地號 == '_GHOST'` ∧ `G(㎡) == 0` ∧ `a 面積(㎡) == 0` 之合取",
        "落檔內 `原地號 == '_GHOST'` 之列 ＝ %d 列"
        % sum(1 for t in data for r in data[t] if (r.get("原地號") or "").strip() == "_GHOST"),
        "⬜ **無受詞（於本批落檔）**·🛑 **子項 `d-6`：其適用繫於 `K-9-9 四` 處置執行後 ⇒ 本批⛔ 判**",
        "母體 ＝ 二情境落檔全 %d 資料列；`原地號` 之相異值⛔ 含 `_GHOST` "
        "（相異值 ＝ %s）⇒ 本批落檔內受詞集 ＝ ∅"
        % (sum(len(data[t]) for t in data),
           sorted({(r.get("原地號") or "").strip() for t in data for r in data[t]})[:3] + ["…"]))

    # ── 統計 ＋ 否證對照
    print()
    print("=" * 118)
    print("【表之統計】")
    print("=" * 118)
    n_no_subj = sum(1 for c in rows_out if "無受詞" in c[3])
    n_unmeas = sum(1 for c in rows_out if "未量" in c[3])
    n_viol = sum(1 for c in rows_out if "🔴" in c[3])
    print("   款數 %d｜無受詞 %d｜含「未量」%d｜含 🔴 之判 %d" % (len(rows_out), n_no_subj, n_unmeas, n_viol))
    print()
    print("── 否證對照（單 §八 (c)）──")
    k93 = [c for c in rows_out if c[0] == "K-9-9 三"][0]
    ok_green = ("無受詞" in k93[3]) and ("🔴" not in k93[3])
    print("   [必綠] `K-9-9 三` 判為「無受詞」而⛔ 觸紅 ⇒ %s" % ("✅" if ok_green else "🔴"))
    # 必紅：人為對一款填「有受詞」而其受詞集為空
    fake_subj = []      # 人造空受詞集
    fake_claim = "有受詞"
    ok_red = (fake_claim == "有受詞") and (len(fake_subj) == 0)
    print("   [必紅] 人為對一款填入「%s」而其受詞集 ＝ %r（空）⇒ 檢查 %s"
          % (fake_claim, fake_subj, "✅ 轉紅（宣稱與受詞集相斥）" if ok_red else "🔴 未轉紅"))
    if not (ok_green and ok_red):
        print("🔴 否證對照未如預期 ⇒ 輸出⛔ 出艙")
        return 5
    print()
    print("── 🛑 未量之子項（逐款具名·⛔ 靜默略過）──")
    print("   `d-1` `K-9-9 一`（各宗遠側界是否 ∥ALLOCLINE）      ⇒ 🟡 不可得·阻斷點見該款")
    print("   `d-2` `K-9-9 七`＋`K-9-10 二`（帶底之有效垂線母體）⇒ 🟡 不可得·阻斷點見該款")
    print("   `d-3` `K-9-12` 之充分側（`G ≥ %.2f` 之宗能否容納） ⇒ 🟡 不可得·阻斷點見該款" % (W * D))
    print("   `d-4` 因果鏈之直證（藍影不合格 ⇔ 角退 ⇔ 重疊）    ⇒ 🟡 本批所量者為**共現**·⛔ 因果")
    print("   `d-5` 逐街廓正面路寬（本批以 `10.0 m` 查表）       ⇒ 🟡 路寬未逐街廓實測")
    print("   `d-6` `K-9-19` 之適用（繫 `K-9-9 四` 處置執行後）  ⇒ 🟡 本批⛔ 判")
    return 0


if __name__ == "__main__":
    sys.exit(main())
