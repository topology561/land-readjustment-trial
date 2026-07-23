# -*- coding: utf-8 -*-
"""
W-F F.4 — 無同歸戶 3 級調配（7-4）＋7-5 雙出口＋終態遞補整形＋總決算（收斂波，trunk E）。

母體＝trunk D（F.3 終態）。執行序**嚴守規格 §7 依賴鏈**：E0(7-1 級1 殘餘) → E1(7-4) → E2(7-5)
→ E3(終態遞補整形，2bis) → E4(終態全域斷言) → E5(總決算 33 群)。

- **合成宗機制**：9 群公設歸戶（＋7-5 重定位戶）於目標塊無既有宗 → 每 (歸戶,塊) 一筆合成宗
  （分攤登記=0／幾何=0／面積_m2=a″ 累加器；四欄鐵律：G 分子=0+Σa′）。模式二前價以
  **deepcopy 快照加合成 zone 鍵** `74avg·{blk}`（單價=p_avg）→ run_step_g 原生 A=post/p_avg，
  **stepg 推進機零修改**。B-1 窮舉閘：每筆合成宗 A 地價比==round(post/p_avg,4)（缺鍵之
  靜默 fallback A=1.0 必被咬出）。
- **a′ 雙模式**（§7-4:418-420）：E0 模式一（有同歸戶目標地）；E1/E2 模式二
  p_avg 母體＝**原始 build_parcels**（重劃前全集；trunk 現態會退化，PROVENANCE 三變體對照）。
- **距離＝KL 質心起迄法**：起點＝群公設宗分攤登記面積最大宗質心；迄點＝E1 開始時各塊最大池片
  質心（一次定錨）。級別：相鄰＝錨所在公設塊共邊 R 塊（RD）或 G1 隔 RD 相望（F.3 裁定③）；
  鄰近＝起迄距≤全表中位；非鄰近＝其餘。
- **R4 非常規靶**（KL 政策「R4 池專供第2梯類」操作化）：R4 剔除於 7-4 常規候選；
  窮盡無塊可規配之 ≥½ 群 → 併入 E2 第2梯類佇列（增配出口）。
- **½線測試**（規格 F.4 第3點）：輪0 solo 假設落位 G(a′) → 2×G<114.07 → 補償＝Σa×公設後價
  （＝後街廓面積加權平均，**現算**；等式閘綁快照 72058.60964443642±1e-6；§53-1 本文式＋
  估價師公會第 11 號公報 P.4，KL 裁定 2026-07-11）→ 退場不配地。終態複驗，翻轉＝停機。
- **池三則**（禁中間態）：cap＝池−MinA；「吃光歸零」僅限塊內無 S=0 殘片（strip 幾何不可達）；
  同級多歸戶比例分攤（分母綁該輪該塊請求集）；剩餘需求以源面積逆折算記帳；收斂 0.05。
- **E2 7-5 批次全域最佳化**（KL 裁定 2026-07-12）：逃生門/梯2/E1 溢入群聯合最佳化，
  目標 min Σ 增配面積×目標後價；資格＝§31-1-2 **比較級**（深度淺於原街廓 ∪ 後價低於原街廓；
  公設軌無原街廓→全塊，手冊(三)）；**Q3 禁超額**（配額＝max(G(a′),MinA)、增配＝max(0,MinA−G(a′))）；
  池三則以容量約束；窮舉可證最優（tie：Σ增配面積→Σ質心起迄距→暫編字典序）。
  差額地價×後價（§52-1）、§53-2 放棄改領標旗；增配>0 標「意思決定・試分配預設自動」。
- **E3**：純幾何等 G 重切＋前移（wf_f1 機制通用化任意塊×側；池總量不變）；整形後池落 (0,MinA)
  ＝停機上呈（無自動補灌）。
- additive-only：不改 app.py／stepg／wf_f0／wf_f1／wf_f2（wf_f3 僅加性暴露 f3_parcels 等）。
  禁呼叫 calc_a_prime／三廢（靜態閘）。
"""
import os
import sys
import csv
import copy
import collections
from decimal import Decimal, ROUND_HALF_UP

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np                                    # noqa: E402
from shapely.geometry import Polygon, Point           # noqa: E402
from shapely.ops import unary_union                   # noqa: E402
from stepg_pipeline import run_step_g, build_step_g_tables  # noqa: E402
import wf_f0                                           # noqa: E402
import wf_f1                                           # noqa: E402
import wf_f2                                           # noqa: E402

# MinA_區（½線補償口徑）不再字面硬編：改 compute() 內 `mina_qu = min(mina.values())` 推導
#   （修正一·claude.ai 2026-07-23）。舊 `MINA_QU` 常數二處引用（½輪0／½終態翻轉閘）退場後成
#   孤兒故刪，避免日後被誤引為權威。**CSV 欄名字串 "2×G vs 114.07"（:471/:1074）與本檔 docstring
#   為 baseline 欄位/文件、本波凍結不動**（改欄名＝重烤假紅·污染 V11 零差靶）；欄名參數化列波後 backlog。
SNAP_WAVG = 72058.60964443642          # 快照 重劃後平均地價（等式閘基準；乘數用現算值）
COMP_EXPECT = {"G013", "G024", "G028"}  # ½ 輪0 <½ 具名錨（相異＝停查再定錨）
E0_EXPECT = {"628-49(1)": "628-48(1)", "628-30(2)": "628-45(2)", "628-42(1)": "628-42(2)"}
F1_REVERIFY = {"0m": "628-37(1)", "3.5m": "628-36(1)"}   # E3 R1 楔形標的複驗（F.1 錨）
E2_NAMED = {"G004": "628-52(1)", "G018": "628-51(1)", "G020": "628-50(1)",
            "G014": "628-29(1)", "G033": "628-46(1)"}    # 第2梯類 5 源宗（由旗標規則導出後對拍）
MAX_ROUNDS = 12
TOL = 0.05
POS_SLACK_AREA = 2.0                   # E2 成本帶：位置相依 G 誤差保守上界（㎡/宗）；band 外免引擎重評
CAP_EVAL = 500                         # E2 引擎重評候選上限（超出＝停機；本案 0m band 遠小於此）
WIDTH_MARGIN = 0.03                    # 合法基地寬目標＝min_width＋此餘裕（引擎旗標用未捨入 S×cos，
                                       #   宗地寬度欄已捨入 2dp；rounded≥min_width+0.03 保未捨入>min_width）
E1_MARGIN = 5.0                        # E1 灌配保留餘裕：可達殘池 ≥ MinA+MARG（中央殘池寬>min_width，避浮點邊界）


def _money(x):
    return int(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def _zone_key(blk):
    return f"74avg·{blk}"


def _wavg_post(snap):
    """公設地後價＝可供分配建築街廓面積加權平均（第 11 號公報 P.4，KL 裁定 2026-07-11）。"""
    bp = snap["財務接線_v3"]["後街廓_面積單價"]
    num = sum(float(v["面積_m2"]) * float(v["單價_元每m2"]) for v in bp.values())
    den = sum(float(v["面積_m2"]) for v in bp.values())
    if den <= 0:
        raise RuntimeError("🔴 公設後價：後街廓面積和 ≤0")
    w = num / den
    if abs(w - SNAP_WAVG) > 1e-6:
        raise RuntimeError(f"🔴 公設後價等式破：現算 {w!r} ≠ 快照 {SNAP_WAVG!r}（>1e-6）")
    return w


def _pub_adjacency(cb_by):
    """公設塊 → 相鄰 R 塊集合。RD＝共邊(<0.5m)；G1＝隔單一 RD 相望（F.3 裁定③）。"""
    polys = {b["label"]: Polygon(b["vertices"]).buffer(0) for b in cb_by.values()}
    R = [l for l in polys if l.startswith("R") and not l.startswith("RD")]
    RD = [l for l in polys if l.startswith("RD")]
    adj = {}
    for pb in list(RD) + [l for l in polys if l.startswith("G")]:
        if pb.startswith("RD"):
            adj[pb] = {r for r in R if polys[pb].distance(polys[r]) < 0.5}
        else:
            adj[pb] = {r for r in R if any(
                polys[rd].distance(polys[pb]) < 0.5 and polys[rd].distance(polys[r]) < 0.5
                for rd in RD)}
    return adj


def _poly_of_temp(temp, pid):
    for t in temp:
        if t["暫編地號"] == pid and t.get("polygon_coords") and len(t["polygon_coords"]) >= 3:
            p = Polygon(t["polygon_coords"])
            return p if p.is_valid else p.buffer(0)
    return None


def _poly_of_row(r):
    cs = r.get("cut_coords") or []
    if len(cs) < 3:
        return None
    p = Polygon(cs)
    return p if p.is_valid else p.buffer(0)


class _Eng:
    """trunk E 演化引擎包裝：parcels 可變、run_step_g 惰性重跑（結構永久閘內建）。"""

    def __init__(self, c, snapE, parcels):
        self.c = c
        self.snapE = snapE
        self.parcels = parcels
        self._sg = None

    def invalidate(self):
        self._sg = None

    def sg(self):
        if self._sg is None:
            c = self.c
            self._sg = run_step_g(c["ns"], c["fake_st"], list(c["cb_by"].values()), c["cad"],
                                  self.snapE, c["params"], self.parcels,
                                  c["winners"], c["forced"], c["setback"])
        return self._sg

    def rows(self):
        return {r["暫編地號"]: r for r in self.sg()["g_rows"]
                if r.get("推進側別") in ("left", "right")}

    def pool(self, blk):
        return float(self.sg()["pool_diag"][blk]["池總=幾何剩餘(㎡)"])

    def by_id(self):
        return {p["暫編地號"]: p for p in self.parcels}

    def set_area(self, pid, a2):
        self.by_id()[pid]["面積_m2"] = round(float(a2), 2)
        self.invalidate()

    def remove(self, pids):
        pids = set(pids)
        self.parcels[:] = [p for p in self.parcels if p["暫編地號"] not in pids]
        self.invalidate()

    def try_G(self, pid):
        """probe 安全讀取：撞守恆牆（strip 幾何吃盡而 G 目標超出）→ None＝該態不可容納。
        僅供試探評估；commit 路徑一律直讀 rows() 保 fail-loud。"""
        r = self.try_rows()
        return float(r[pid]["G(㎡)"]) if (r is not None and pid in r) else None

    def try_rows(self):
        """probe 安全全讀：撞守恆牆 → None（候選不可行）。僅供 _actual 試評；commit 直讀 rows()。"""
        try:
            return self.rows()
        except RuntimeError as e:
            if "守恆破" in str(e):
                self._sg = None
                return None
            raise

    def add_syn(self, gid, blk, zone_key, anchor_xy, a2=0.0):
        pid = f"74·{gid}@{blk}"
        x, y = anchor_xy
        self.parcels.append({
            "暫編地號": pid, "原地號": f"74·{gid}", "所屬街廓": blk, "街廓分類": "住宅區",
            "分攤登記面積_m2": 0.0, "幾何面積_m2": 0.0, "面積_m2": round(float(a2), 2),
            "重劃前地價區段": zone_key,
            "polygon_coords": [(x - 0.25, y - 0.25), (x + 0.25, y - 0.25),
                               (x + 0.25, y + 0.25), (x - 0.25, y + 0.25)],
        })
        self.invalidate()
        return pid


def _bisect_G(eng, pid, target_G, tol=0.05, max_iter=40):
    """對合成宗 pid 之 面積_m2 二分至 G==target_G（G 隨 a″ 嚴格遞增、內域安全——
    呼叫端保證 target_G 距池牆 ≥MinA 級餘裕，G−area 殘差不會觸守恆閘）。回傳 a″。"""
    def G_of():
        return float(eng.rows()[pid]["G(㎡)"])
    a_now = float(eng.by_id()[pid]["面積_m2"])
    g_now = G_of() if a_now > 0.01 else 0.0
    if abs(g_now - target_G) <= tol:
        return a_now
    lo, hi = (0.0, a_now) if g_now > target_G else (a_now, 0.0)
    if g_now < target_G:                     # 上界：r=G/a″<1 ⟹ hi=a_now+ΔG/0.4 必括住
        hi = a_now + (target_G - g_now) / 0.4
        eng.set_area(pid, hi)
        if G_of() < target_G - tol:
            raise RuntimeError(f"🔴 _bisect_G 上界不足：{pid} target={target_G:.2f}")
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        eng.set_area(pid, mid)
        g = G_of()
        if abs(g - target_G) <= tol:
            return mid
        if g < target_G:
            lo = mid
        else:
            hi = mid
    raise RuntimeError(f"🔴 _bisect_G 不收斂：{pid} target={target_G:.2f} 得 {g:.2f}")


def _valid_G(G, width, mw, mina):
    """達「合法最小建築基地」所需 G＝max(MinA, (min_width＋WIDTH_MARGIN) 對應之 G)。
    裁示1(a) 宗地寬度≥min_width 為終態必要；深度>名目時 area 微增至 min_width×depth_local
    （§8 型幾何、非政策增配）。width>0 時對應 G＝G×寬目標/width（線性：area∝width @固定深）。"""
    gw = ((mw + WIDTH_MARGIN) * G / width) if width > 1e-6 else mina
    return max(mina, gw)


def _bisect_valid(eng, pid, blk, mw, mina, max_iter=48):
    """增配至合法基地（宗地寬度≥min_width＋WIDTH_MARGIN 且 G≥MinA）之**最小** a″
    （二者皆隨 a″ 單調增）。回傳 a″。裁示1(a)＋終極驗收＝合法可建築最小基地（非僅 area 達標）。"""
    wt = mw + WIDTH_MARGIN
    def _wg():
        r = eng.rows()[pid]
        return float(r["宗地寬度(m)"]), float(r["G(㎡)"])
    a = float(eng.by_id()[pid]["面積_m2"])
    w, g = _wg()
    if w >= wt - 1e-6 and g >= mina - TOL:
        return a
    hi = max(a, 1.0)
    for _ in range(14):                       # 上界擴張至滿足
        hi = hi * 1.3 + 5.0
        eng.set_area(pid, hi)
        w, g = _wg()
        if w >= wt and g >= mina:
            break
    else:
        raise RuntimeError(f"🔴 _bisect_valid 上界擴張失敗 {pid}@{blk}")
    lo = a
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        eng.set_area(pid, mid)
        w, g = _wg()
        if w >= wt - 1e-9 and g >= mina - 1e-9:
            hi = mid
        else:
            lo = mid
        if hi - lo < 0.005:
            break
    eng.set_area(pid, hi)                      # hi 為已知滿足之最小
    return hi


def _cur_pool_anchor(eng, blk):
    """當下最大池片質心（合成宗錨點用；池隨灌入位移，錨點須跟隨免插入他宗投影帶）。"""
    best = None
    for r in eng.sg()["g_rows"]:
        if r.get("推進側別") == "抵費地" and r["所屬街廓"] == blk:
            p = _poly_of_row(r)
            if p is not None and (best is None or p.area > best.area):
                best = p
    return (best.centroid.x, best.centroid.y) if best is not None else None


def _s0_unreachable(ns, snap, cb_by, cad, eng, forced):
    """各塊 strip 不可達池量（S=0 碎片＋forced 角落鎖定片）＝吃池歸零之幾何禁區。"""
    frags = wf_f1._classify_fragments(ns, snap, cb_by, cad, eng.sg()["g_rows"], forced)
    out = collections.defaultdict(float)
    for f in frags:
        if f["三分類"] in ("碎片", "forced角落鎖定"):
            out[f["街廓"]] += f["面積"]
    return dict(out)


def compute(ctx_by_tag, f0_out, f2_out, f3_out):
    """F.4 逐情境。回傳 {tag: {conv_rows, exit_rows, g_tab, pool_rows, reshape_rows,
    ledger_rows, anchors}}。停機一律 RuntimeError。"""
    out = {}
    for tag, c in ctx_by_tag.items():
        ns, snap, cb_by, cad = c["ns"], c["snap"], c["cb_by"], c["cad"]
        omap = c["omap"]
        gof = lambda p: omap.get(p, "")
        temp = c["temp"]
        fcb = ns["F3_CATEGORY_BURDEN"]
        zof = snap["財務接線_v3"]["原地號_區段"]
        pre_price = {z: float(v["單價_元每m2"]) for z, v in
                     snap["財務接線_v3"]["重劃前區段_面積單價"].items()}
        post_price = {l: float(v["單價_元每m2"]) for l, v in
                      snap["財務接線_v3"]["後街廓_面積單價"].items()}
        mina = wf_f0._mina_by_block(ns, snap, cb_by)
        # MinA_區（重劃區內最小分配面積標準）＝推導正典，取代舊字面常數（修正一·claude.ai 2026-07-23）。
        #   ⚠️ 必須用上行之【真 snap】版 mina；禁用下方 :305 deepcopy 之 snapE 重算
        #      （snapE 注入合成 zone 鍵，會污染 MinA_區）。
        #   🔒 二口徑分明：mina[blk]＝**配地可行性**（各街廓·E1/E2 落位用·勿混）；
        #      mina_qu＝**½線補償**口徑（重劃區內標準·手冊「重劃區內最小分配面積標準」·
        #      run_verification:654 正典閘／:701 reverse-test 隨動）。
        mina_qu = min(mina.values())
        wavg = _wavg_post(snap)
        # 模式二分母 p_avg：重劃前全集＝原始 build_parcels（PROVENANCE 三變體對照）
        p_avg = wf_f2._block_pre_avg(snap, c["build"], pre_price)

        # 合成 zone 鍵（deepcopy 快照；真快照零污染、既有宗 A 不受影響——reviewer A-2 實證）
        snapE = copy.deepcopy(snap)
        for blk in mina:
            snapE["財務接線_v3"]["重劃前區段_面積單價"][_zone_key(blk)] = {
                "單價_元每m2": p_avg[blk], "_note": "F.4 合成 zone（§7-4 模式二 p_avg）"}

        parcels = copy.deepcopy(f3_out[tag]["f3_parcels"])
        eng = _Eng(c, snapE, parcels)
        D_rows = {r["暫編地號"]: r for r in f3_out[tag]["sgD_rows"]
                  if r.get("推進側別") in ("left", "right")}
        poolD = {l: float(v["池總=幾何剩餘(㎡)"])
                 for l, v in f3_out[tag]["poolD_diag"].items()}
        win_set = {v for w in c["winners"].values()
                   for v in (w.get("p1_end"), w.get("p2_end")) if v}

        conv_rows, exit_rows, events = [], [], collections.defaultdict(list)

        # ══ E0：殘餘同歸戶級1 sweep（§7-1 級1＋裁示2；F.2 _decide 同規則） ══
        flagged = [r for r in D_rows.values() if r["畸零地旗標"].strip()]
        byg = collections.defaultdict(lambda: collections.defaultdict(list))
        for r in D_rows.values():
            byg[gof(r["原地號"])][r["所屬街廓"]].append(r)
        e0_pairs, e2_class = {}, []          # e2_class＝第2梯類（7-5）源宗
        for r in sorted(flagged, key=lambda x: x["暫編地號"]):
            gid = gof(r["原地號"])
            qual = {}
            for blk, rows in byg[gid].items():
                if any(float(x["G(㎡)"]) >= mina[blk] and not x["畸零地旗標"].strip()
                       and x["暫編地號"] != r["暫編地號"] for x in rows):
                    qual[blk] = sum(float(x["G(㎡)"]) for x in rows)
            if qual:
                tb = max(sorted(qual), key=qual.get)
                tr = sorted([x for x in byg[gid][tb]
                             if float(x["G(㎡)"]) >= mina[tb] and not x["畸零地旗標"].strip()],
                            key=lambda x: (-float(x["G(㎡)"]), x["暫編地號"]))[0]
                e0_pairs[r["暫編地號"]] = (gid, r, tr)
            else:
                e2_class.append((gid, r))
        if {k: v[2]["暫編地號"] for k, v in e0_pairs.items()} != E0_EXPECT:
            if os.environ.get("WV_BAKE"):
                print(f"⚠️ [WV_BAKE·{tag}] E0 規則導出 ≠ 具名錨：{ {k: v[2]['暫編地號'] for k, v in e0_pairs.items()} }（期 {E0_EXPECT}）")
            else:
                raise RuntimeError(f"🔴 [{tag}] E0 規則導出 ≠ 具名錨：{ {k: v[2]['暫編地號'] for k, v in e0_pairs.items()} }（期 {E0_EXPECT}）")
        if sorted(x[1]["暫編地號"] for x in e2_class) != sorted(E2_NAMED.values()):
            if os.environ.get("WV_BAKE"):
                print(f"⚠️ [WV_BAKE·{tag}] 第2梯類源宗 ≠ 具名錨：{sorted(x[1]['暫編地號'] for x in e2_class)}")
            else:
                raise RuntimeError(f"🔴 [{tag}] 第2梯類源宗 ≠ 具名錨：{sorted(x[1]['暫編地號'] for x in e2_class)}")
        _rm0 = set(e0_pairs)
        if _rm0 & win_set:
            raise RuntimeError(f"🔴 [{tag}] E0 移除宗為街角 winner：{sorted(_rm0 & win_set)}")
        for pid, (gid, r, tr) in sorted(e0_pairs.items()):
            z_s, z_t = zof[r["原地號"]], zof[tr["原地號"]]
            a_src = float(r["a 面積(㎡)"])
            ap = round(a_src * pre_price[z_s] / pre_price[z_t], 2)
            bid = eng.by_id()
            bid[tr["暫編地號"]]["面積_m2"] = round(
                float(bid[tr["暫編地號"]].get("面積_m2", 0) or 0) + ap, 2)
            events[gid].append(f"E0級1殘餘併入 {pid}→{tr['暫編地號']}")
            conv_rows.append({"情境": tag, "段": "E0級1", "歸戶": gid, "源": pid,
                              "源塊": r["所屬街廓"], "目標宗": tr["暫編地號"],
                              "目標塊": tr["所屬街廓"], "級別": "級1(同歸戶)",
                              "起迄距(m)": "", "a源(㎡)": round(a_src, 2),
                              "模式一a′(㎡)": ap,
                              "模式二a′(㎡)": round(a_src * pre_price[z_s] / p_avg[tr["所屬街廓"]], 2),
                              "a″引擎(㎡)": ap, "配額G(㎡)": "", "處置": "併入(§7-1級1)"})
            if abs(ap - a_src) > 0.01 and z_s == z_t:
                raise RuntimeError(f"🔴 [{tag}] E0 同區段恆等破：{pid} a′={ap}≠a={a_src}")
        eng.remove(_rm0)
        eng.invalidate()
        _ = eng.sg()                          # E1 錨定態（含 E0 效果）

        # ══ E1：7-4 九群三級調配 ══
        # 母體＝F.3 轉7-4 表（24 筆 9 群）
        pub74 = collections.defaultdict(list)
        for row in f3_out[tag]["to74_rows"]:
            pid = row["公設筆"]
            tp = next(t for t in temp if t["暫編地號"] == pid)
            p = _poly_of_temp(temp, pid)
            pub74[gof(tp["原地號"])].append({
                "pid": pid, "blk": tp["所屬街廓"], "zone": zof[tp["原地號"]],
                "a": float(tp.get("分攤登記面積_m2", 0) or 0),
                "cen": (p.centroid.x, p.centroid.y)})
        if sum(len(v) for v in pub74.values()) != 24 or len(pub74) != 9:
            raise RuntimeError(f"🔴 [{tag}] 7-4 母體 ≠ 24筆/9群")
        ginfo = {}
        for gid, lots in pub74.items():
            anchor = max(lots, key=lambda x: (x["a"], x["pid"]))
            zz = {x["zone"] for x in lots}
            if len(zz) != 1:
                raise RuntimeError(f"🔴 [{tag}] {gid} 公設宗跨 zone {zz}（Σ地價需分 zone，未建模）")
            ginfo[gid] = {"a": sum(x["a"] for x in lots),
                          "value": sum(x["a"] * pre_price[x["zone"]] for x in lots),
                          "zone": zz.pop(), "anchor": anchor}
        # 距離表（E1 開始時一次定錨：各塊最大池片質心）
        pool_cen = {}
        for r in eng.sg()["g_rows"]:
            if r.get("推進側別") != "抵費地":
                continue
            p = _poly_of_row(r)
            blk = r["所屬街廓"]
            if p is not None and (blk not in pool_cen or p.area > pool_cen[blk][1]):
                pool_cen[blk] = ((p.centroid.x, p.centroid.y), p.area)
        adj_pub = _pub_adjacency(cb_by)
        d_off = {}                                    # 合成宗錨點偏移方向（沿 FRONT d_hat 保序）
        for blk in mina:
            _fl = (cad.get("front_lines") or {}).get(blk) or {}
            _v = np.array(_fl["p2"], float) - np.array(_fl["p1"], float)
            d_off[blk] = _v / (float(np.linalg.norm(_v)) or 1.0)
        dists, med_all = {}, []
        for gid, gi in ginfo.items():
            ax, ay = gi["anchor"]["cen"]
            for blk in mina:
                d = ((ax - pool_cen[blk][0][0]) ** 2 + (ay - pool_cen[blk][0][1]) ** 2) ** 0.5
                dists[(gid, blk)] = d
                med_all.append(d)
        med = float(np.median(med_all))

        def _level(gid, blk):
            if blk in adj_pub.get(ginfo[gid]["anchor"]["blk"], set()):
                return 0
            return 1 if dists[(gid, blk)] <= med else 2
        LV = {0: "級1相鄰", 1: "級2鄰近", 2: "級3非鄰近"}
        border = {gid: sorted(mina, key=lambda b: (_level(gid, b), dists[(gid, b)], b))
                  for gid in ginfo}

        # 不可達池量（S=0 碎片＋forced 鎖定；吃池歸零之幾何禁區）
        unreach = _s0_unreachable(ns, snapE, cb_by, cad, eng, c["forced"])

        # solo 試算（½ 輪0＋feasibility＋ratio；即時態、不快取——池態隨輪演化）
        def _trial(gid, blk, a_amt, zone=None):
            """solo 落位試算（暫置 74T· 宗、量測後即移除）。回傳 (G_probe, a″_full, a″_probe)。"""
            z = zone or ginfo[gid]["zone"]
            a2 = a_amt * pre_price[z] / p_avg[blk]
            eatable = max(eng.pool(blk) - unreach.get(blk, 0.0) - 1.0, 1.0)
            a2p = min(a2, max(1.0, eatable - 5.0))           # probe 防夾擠（G=r·a″，r<1 恆成立）
            cen_t = (pool_cen[blk][0][0] - 1.2 * float(d_off[blk][0]),   # 錨點前置防投影序 tie
                     pool_cen[blk][0][1] - 1.2 * float(d_off[blk][1]))
            pid = eng.add_syn(f"T·{gid}", blk, _zone_key(blk), cen_t)
            eng.set_area(pid, a2p)
            G = eng.try_G(pid)                               # 撞牆＝None（該塊此刻容不下 probe）
            eng.remove([pid])
            if G is None:
                return None, a2, a2p
            return G, a2, a2p

        # ── ½ 輪0（solo 於最近塊，含 R4 純量測） ──
        near_any = {gid: sorted(mina, key=lambda b: (dists[(gid, b)], b))[0] for gid in ginfo}
        half_r0 = {}
        for gid in sorted(ginfo):
            G0, _a2f, _a2p = _trial(gid, near_any[gid], ginfo[gid]["a"])
            # probe 夾擠時 G0 為保守下界（大群 2×G0 遠越線，判定不受影響；小群 probe==full）
            if G0 is None:
                raise RuntimeError(f"🔴 [{tag}] ½ 輪0 {gid}@{near_any[gid]} probe 撞守恆牆（開波池態不應發生）")
            half_r0[gid] = (G0, 2 * G0 >= mina_qu)     # ½線＝MinA_區（區內標準·非 mina[blk]）
        comp_groups = {g for g, (_, ok) in half_r0.items() if not ok}
        if comp_groups != COMP_EXPECT:
            if os.environ.get("WV_BAKE"):
                print(f"⚠️ [WV_BAKE·{tag}] ½ 輪0 <½ 群 {sorted(comp_groups)} ≠ 具名錨 {sorted(COMP_EXPECT)}")
            else:
                raise RuntimeError(f"🔴 [{tag}] ½ 輪0 <½ 群 {sorted(comp_groups)} ≠ 具名錨 "
                                   f"{sorted(COMP_EXPECT)}——停查再定錨")
        for gid in sorted(comp_groups):
            gi = ginfo[gid]
            comp = _money(gi["a"] * wavg)
            exit_rows.append({"情境": tag, "歸戶": gid, "類": "公設軌", "出口": "<½ 現金補償",
                              "G(a′)輪0(㎡)": round(half_r0[gid][0], 2),
                              "2×G vs 114.07": "<", "Σa(㎡)": round(gi["a"], 2),
                              "配額G(㎡)": "", "增配面積(㎡)": "", "差額地價(元)§52-1": "",
                              "放棄改領(元)§53-2": "",
                              "補償_本文式(元)§53-1": comp,
                              "補償_但書式(元)": "—(不適用·非申請分割)",
                              "目標塊": "—", "資格款": "—(公設軌·無原街廓)",
                              "意思決定": "§53-3 他項權利協調旗(本案空)"})
            events[gid].append(f"E1 ½測試<½→現金補償 {_money(ginfo[gid]['a'] * wavg)} 元")

        # ── 配地輪（≥½；R4 非常規靶；同級比例分攤；池三則；收斂 0.05） ──
        alloc = {g for g in ginfo if g not in comp_groups}
        a_rem = {g: ginfo[g]["a"] for g in alloc}
        placed = collections.defaultdict(float)     # (gid,blk) → a″ 累計
        syn_ids = {}
        spill_75 = []                                # 窮盡無塊可規配 → E2 第2梯類佇列
        ratio_est = {}                               # (gid,blk) → G/a″ 估（trial 更新）

        def _conv(g, blk):                           # 源面積 → a″（模式二折算）
            return pre_price[ginfo[g]["zone"]] / p_avg[blk]

        def _ratio(g, blk):
            if (g, blk) not in ratio_est:
                G, _, a2p = _trial(g, blk, max(a_rem[g], 50.0))
                ratio_est[(g, blk)] = (max(G / a2p, 0.05) if (G is not None and a2p > 0)
                                       else 0.55)
            return ratio_est[(g, blk)]

        def _reach(blk):                             # 可達池＝池總量 − 不可達(楔形/forced)
            return eng.pool(blk) - unreach.get(blk, 0.0)

        def _budget(blk):                            # 可灌量＝可達池 − 保留有效殘池(MinA+餘裕)
            return _reach(blk) - (mina[blk] + E1_MARGIN)

        def _usable(g, blk):
            """blk 可供 g 再灌一片 ≥MinA 且留 ≥MinA+餘裕 可達殘池？回傳 (可用, demG_est)。"""
            demG = a_rem[g] * _conv(g, blk) * _ratio(g, blk)
            if _budget(blk) < mina[blk] - 0.5:       # 容不下一片 ≥MinA 且保殘池
                return False, demG
            if demG < mina[blk] - 0.5:               # 小片：概念4 以引擎 solo 實測
                G, a2, a2p = _trial(g, blk, a_rem[g])
                if G is None or a2p < a2 - 0.01 or G < mina[blk] - 0.01:
                    return False, demG
            return True, demG

        rounds = 0
        while True:
            spset = {s[0] for s in spill_75}
            act = [g for g in sorted(alloc - spset, key=lambda g: (-ginfo[g]["value"], g))
                   if a_rem[g] > TOL]
            if not act:
                break
            rounds += 1
            if rounds > MAX_ROUNDS:
                raise RuntimeError(f"🔴 [{tag}] E1 配地輪 >{MAX_ROUNDS} 不收斂（Δ>0.05）")
            requests = collections.defaultdict(list)
            for gid in act:
                pick = None
                for blk in border[gid]:
                    if blk == "R4":                  # R4 非常規靶（KL 政策：專供第2梯類）
                        continue
                    ok, _ = _usable(gid, blk)
                    if ok:
                        pick = blk
                        break
                if pick is None:
                    spill_75.append((gid, "E1窮盡無塊可規配(概念4/R4政策)"))
                    events[gid].append("E1 無塊可規配 → E2 第2梯類增配佇列")
                else:
                    requests[pick].append(gid)
            if not requests:
                break
            for blk in sorted(requests):
                gs = sorted(requests[blk], key=lambda g: (-ginfo[g]["value"], g))
                demG = {g: a_rem[g] * _conv(g, blk) * _ratio(g, blk) for g in gs}
                budget = _budget(blk)            # 可灌量＝可達池 − (MinA+餘裕)；rule3 保有效殘池
                # 同級比例分攤（分母＝本輪本塊請求集）；share<MinA 者退出本塊（自小值序）
                while True:
                    tot = sum(demG[g] for g in gs)
                    shares = ({g: demG[g] for g in gs} if tot <= budget + TOL
                              else {g: budget * demG[g] / tot for g in gs})
                    small = [g for g in gs if shares[g] < mina[blk] - 0.01
                             and shares[g] < demG[g] - 0.01]
                    if not small or len(gs) == 1:
                        break
                    gs.remove(sorted(small, key=lambda g: (ginfo[g]["value"], g))[0])
                for g in gs:
                    shG = min(shares[g], demG[g])
                    if shG <= TOL:
                        continue
                    a_used = min(shG / (_conv(g, blk) * _ratio(g, blk)), a_rem[g])
                    # 剩餘感知：灌後剩餘若落 (0, 次一可行塊 MinA 需求)，縮灌保剩餘可落位
                    rem_after = a_rem[g] - a_used
                    if rem_after > 0.01:
                        nxts = [b for b in border[g] if b not in (blk, "R4")
                                and _budget(b) >= mina[b] - 0.5]
                        if nxts:
                            b2 = nxts[0]
                            need = (mina[b2] + 0.5) / (_conv(g, b2) * _ratio(g, b2))
                            if rem_after < need:
                                a_used = max(0.0, a_rem[g] - need)
                        # 無次塊：不強塞（保 blk 有效殘池；剩餘 → E2 溢入佇列由 rule3 收）
                    if a_used <= TOL:
                        continue
                    key = (g, blk)
                    if key not in syn_ids:
                        anc = _cur_pool_anchor(eng, blk)
                        if anc is None:
                            continue                 # 池已空（不應至此；防衛）
                        off = len([1 for (gg, bb) in syn_ids if bb == blk]) * 0.6
                        cenb = (anc[0] + off * float(d_off[blk][0]),
                                anc[1] + off * float(d_off[blk][1]))
                        syn_ids[key] = eng.add_syn(g, blk, _zone_key(blk), cenb)
                    placed[key] += a_used * _conv(g, blk)
                    eng.set_area(syn_ids[key], placed[key])
                    a_rem[g] -= a_used
                # 池 floor 校正（rule3）：實跑後可達殘池若落 < MinA+餘裕 → 縮末灌宗回補、差額退還
                reach = _reach(blk)
                filled = [g for g in gs if placed.get((g, blk), 0) > 0]
                if filled and reach < mina[blk] + E1_MARGIN - 0.05:
                    last_g = filled[-1]
                    key = (last_g, blk)
                    pid = syn_ids[key]
                    a2_old = placed[key]
                    g_now = float(eng.rows()[pid]["G(㎡)"])
                    a2fix = _bisect_G(eng, pid, g_now - (mina[blk] + E1_MARGIN - reach), TOL)
                    placed[key] = a2fix
                    d_a = (a2_old - a2fix) / _conv(last_g, blk)
                    a_rem[last_g] = max(a_rem[last_g] + d_a, 0.0)
                    ratio_est.pop((last_g, blk), None)

        # E1 valid-width pass（裁示1(a)）：7-4 落位宗須達合法基地（寬≥min_width）。深度>名目致
        #   area 達標但寬<min_width 之邊界宗（如 74·G012@R2）微增至合法基地（§8 型幾何、非政策增配）。
        _mw_e1 = {b: float(ns["get_min_lot_size"](cb_by[b]["category"],
                  float(snap["blocks"][b]["正面"]["路寬_m"]))["min_width"]) for b in mina}
        for (gid, blk), pid in list(syn_ids.items()):
            if eng.rows()[pid]["畸零地旗標"].strip():       # 引擎旗標（未捨入 S×cos<min_width）
                placed[(gid, blk)] = _bisect_valid(eng, pid, blk, _mw_e1[blk], mina[blk])
                if _reach(blk) < mina[blk] - 0.05:
                    raise RuntimeError(f"🔴 [{tag}] E1 valid-width 後 {blk} 可達殘池<MinA（餘裕不足）")

        # E1 終態調整帳（conv_rows）
        for (gid, blk), a2 in sorted(placed.items()):
            if a2 <= 0.01:
                continue
            a_src_used = a2 * p_avg[blk] / pre_price[ginfo[gid]["zone"]]
            r = eng.rows()[syn_ids[(gid, blk)]]
            conv_rows.append({"情境": tag, "段": "E1·7-4", "歸戶": gid,
                              "源": f"公設群({len(pub74[gid])}筆)", "源塊": ginfo[gid]["anchor"]["blk"],
                              "目標宗": syn_ids[(gid, blk)], "目標塊": blk,
                              "級別": LV[_level(gid, blk)],
                              "起迄距(m)": round(dists[(gid, blk)], 1),
                              "a源(㎡)": round(a_src_used, 2),
                              "模式一a′(㎡)": "—(無同歸戶目標地)",
                              "模式二a′(㎡)": round(a2, 2), "a″引擎(㎡)": round(a2, 2),
                              "配額G(㎡)": round(float(r["G(㎡)"]), 2),
                              "處置": "7-4 配地(模式二)"})
            events[gid].append(f"E1 7-4 配地 {blk} G={float(r['G(㎡)']):.2f}")

        # ══ E2：7-5 第2梯類雙出口（批次全域最佳化；KL 裁定 2026-07-12）══
        #   目標式 min Σ 增配面積×目標後價；資格＝§31-1-2 比較級集（深度較淺 ∪ 後價較低；
        #   公設軌無原街廓→全可建築塊）；Q3 禁超額（配額＝max(G(a′),MinA)）；池三則以容量約束；
        #   窮舉可證最優（非啟發式）。E1（7-4 距離法）結果不重開。
        rm2 = sorted(x[1]["暫編地號"] for x in e2_class)
        if set(rm2) & win_set:
            raise RuntimeError(f"🔴 [{tag}] E2 移除宗為街角 winner：{sorted(set(rm2) & win_set)}")
        E_pre2 = eng.rows()
        hh75 = []
        for gid, r in e2_class:                       # 建地軌（逃生門＋梯2；源宗移除、原街廓可比）
            hh75.append({"gid": gid, "kind": "建地軌·第2梯類", "a": float(r["a 面積(㎡)"]),
                         "zone": zof[r["原地號"]], "src": r["暫編地號"], "src_blk": r["所屬街廓"],
                         "orig": r["所屬街廓"],
                         "anchor_cen": _row_centroid(E_pre2.get(r["暫編地號"]))
                         or ginfo.get(gid, {}).get("anchor", {}).get("cen", (0.0, 0.0))})
        for gid, why in spill_75:                     # 公設軌（E1 溢入；無原街廓→全塊合格）
            hh75.append({"gid": gid, "kind": "公設軌·增配出口", "a": a_rem[gid],
                         "zone": ginfo[gid]["zone"], "src": "公設群餘量",
                         "src_blk": ginfo[gid]["anchor"]["blk"], "orig": None,
                         "anchor_cen": ginfo[gid]["anchor"]["cen"]})
        eng.remove(rm2)
        eng.invalidate()
        depth_by = {b: float(snap["blocks"][b]["街廓分配深度_m"]) for b in mina}
        e2_opt = _e2_optimal(tag, ns, eng, hh75, mina, depth_by, p_avg, pre_price, post_price,
                             snapE, cb_by, cad, c["forced"], pool_cen, d_off,
                             syn_ids, placed, conv_rows, exit_rows, events)
        if not e2_opt.get("feasible"):
            raise RuntimeError(f"🔴 [{tag}] E2 7-5 批次全域最佳化不可行——停機上呈｜{e2_opt}")

        # ── trunk E 定稿＋B-1 窮舉閘＋池三則＋½ 終態複驗 ──
        sgE = eng.sg()
        E = eng.rows()
        b1_bad = []
        for (gid, blk), pid in syn_ids.items():
            if pid not in E:
                continue
            exp_A = round(post_price[blk] / p_avg[blk], 4)
            if _zone_key(blk) not in snapE["財務接線_v3"]["重劃前區段_面積單價"]:
                b1_bad.append(f"{pid}: 合成 zone 鍵缺")
            elif abs(float(E[pid]["A 地價比"]) - exp_A) > 1e-9:
                b1_bad.append(f"{pid}: A={E[pid]['A 地價比']} ≠ post/p_avg={exp_A}")
        if b1_bad:
            raise RuntimeError(f"🔴 [{tag}] B-1 窮舉閘咬出（靜默 fallback / 鍵漏）：{b1_bad[:4]}")
        poolE = {l: float(v["池總=幾何剩餘(㎡)"]) for l, v in sgE["pool_diag"].items()}
        for gid in sorted(alloc):
            GE = sum(float(E[p]["G(㎡)"]) for (g2, b2), p in syn_ids.items()
                     if g2 == gid and p in E)
            if GE > 0 and 2 * GE < mina_qu:            # ½線＝MinA_區（同 :458）
                raise RuntimeError(f"🔴 [{tag}] ½ 判終態翻轉：{gid} 2×{GE:.2f}<{mina_qu}")
        for (gid, blk), pid in sorted(syn_ids.items()):
            if pid in E and float(E[pid]["G(㎡)"]) < mina[blk] - TOL:
                raise RuntimeError(f"🔴 [{tag}] 概念4 破：{pid} G={E[pid]['G(㎡)']}<MinA_{blk}")

        # ══ E3：終態遞補整形（純幾何、池不變） ══
        reshape_rows, resh_targets, new_polys_by_blk = [], {}, {}
        frags = wf_f1._classify_fragments(ns, snapE, cb_by, cad, sgE["g_rows"], c["forced"])
        s0 = [f for f in frags if f["三分類"] == "碎片"]
        per_blk = collections.defaultdict(list)
        for f in s0:
            per_blk[f["街廓"]].append(f)
        for blk in sorted(per_blk):
            if len(per_blk[blk]) != 1:
                raise RuntimeError(f"🔴 [{tag}] {blk} S=0 碎片 {len(per_blk[blk])} 片 >1，通用整形未支援——停機")
            f = per_blk[blk][0]
            rrows, npolys, tgt = _reshape_block(ns, snapE, cb_by, cad, c["forced"],
                                                sgE["g_rows"], blk, f, tag, mina)
            reshape_rows.extend(rrows)
            new_polys_by_blk[blk] = npolys
            resh_targets[blk] = tgt
        if "R1" in resh_targets and resh_targets["R1"] != F1_REVERIFY[tag]:
            raise RuntimeError(f"🔴 [{tag}] R1 楔形標的 {resh_targets['R1']} ≠ F.1 複驗錨 {F1_REVERIFY[tag]}")

        # 整形後複驗：①整形守恆總配地面積（buffer-free、逐宗 Δ~0.001）→ 池總量不變；
        #   ②無 S=0 池片殘留（臨街長判、不受 buffer 皮膚影響）。池差以 Σ面積 守恆計，
        #   非「block−union.buffer(0.001)」（後者 1mm 皮膚隨宗數/周長變、非真面積漏，
        #   R3/R6 多宗致 −0.45/+0.14 假影）。
        pool_final = dict(poolE)
        for blk, npolys in new_polys_by_blk.items():
            # 🆕 §4 fallback（[B]·補丁十 §一 §8-1·KL 完整恆等式旗）：抵費地(末) 為 **new key（不在 E）**
            #   → 池重定位·排除帳對閘宗和；`pool_final=poolE−area(R_end)`。winner 時 _new_abate={}
            #   （npolys 全在 E）→ pool_final=poolE·**零行為**。守恆完整式＝
            #   `ΣG＋pool_final＋抵費地街角＋抵費地末＝街廓`（frag 只在 poolE、不雙計·KL 旗）。
            _new_abate = {k: p for k, p in npolys.items() if k not in E}
            _in_E = {k: p for k, p in npolys.items() if k in E}
            old_area = sum(_poly_of_row(E[k]).area for k in _in_E)
            new_area = sum(p.area for p in _in_E.values())      # 只核既有宗（抵費地末=池·排除）
            _end_abate_area = sum(p.area for p in _new_abate.values())
            # §N3-0 帳對幾何閘·E3 整形級（KL 2026-07-16 裁·補丁三 §三-1）
            #   閘寬＝`_acct_geom_tol_block(整形宗數, 深度, with_tol=False)`＝**整形宗數 × 0.005**
            #   （`_G_ROUND_HALF`·G 面積捨入半量子）；**無 tol 項**（with_tol=False·整形重切既有宗、不經 bisect）。
            #   ⚠️ 舊述「× (0.005×深度 ＋ 0.005)」**S0d 後作廢**（補丁四 §二·#24）：舊 `_S_ROUND_HALF×深度`
            #     量子項因 S 回復未捨入全精度、量化退出計算路徑而歸零（`depth` 僅存簽名相容）——
            #     權威式＋理由見 `app.py _acct_geom_tol_per_lot` docstring（勿於此重述致漂移·#20）。
            _e3_depth = float(snap["blocks"][blk]["街廓分配深度_m"])
            _e3_tol = ns["_acct_geom_tol_block"](len(_in_E), _e3_depth, False)
            if abs(new_area - old_area) > _e3_tol:
                raise RuntimeError(
                    f"🔴 [{tag}] E3 {blk} 整形未守恆：Σ新形 {new_area:.2f} ≠ Σ原 {old_area:.2f}"
                    f"（Δ={abs(new_area - old_area):.4f} > 上界 {_e3_tol:.4f}＝整形宗數{len(_in_E)}×0.005）")
            pool_final[blk] = poolE[blk] - _end_abate_area      # 🆕 抵費地(末) 由池重定位（fallback；winner=0→不變）
            bpoly = Polygon(cb_by[blk]["vertices"])
            if not bpoly.is_valid:
                bpoly = bpoly.buffer(0)
            fl = (cad.get("front_lines") or {}).get(blk) or {}
            # ── §N3-0 T2（第四處病灶·plan §1.4）：池片改用同機制·同切線 ──
            #   ⚠️ 舊式 `unary_union(list(npolys.values())).buffer(0.001)` → `difference`
            #      → `area>=1.0` **已廢**（與 stepg/app/wf_f1 同族之抄寫複本·#20）。
            #   **為何仍須改（縱使現 pieces 僅供下方 S=0 診斷、不進 g_tab）**：§N5 令 reshape
            #      回寫 g_tab 後 E3 幾何即進終態、此漏原路返回 → #20「修一次到位」。
            _p1 = np.array(fl["p1"], float)
            _p2 = np.array(fl["p2"], float)
            _dh = (_p2 - _p1) / float(np.linalg.norm(_p2 - _p1))
            _ad = ns["alloc_normal_axis"]((cad.get("alloc_dir_by_block") or {}).get(blk))
            pieces = ns["_pool_strips_for_block"](
                bpoly, _dh, _p1.copy(), _ad, list(npolys.values()),
                _label=f"{blk}·E3[{tag}]", _depth=_e3_depth)
            fseg = wf_f1._seg(fl)
            for g in pieces:
                if wf_f1._front_len_of(g, fseg, bpoly) < 0.5:
                    fm = (c["forced"] or {}).get(blk, {}) or {}
                    if fm.get("left_forced_offset") or fm.get("right_forced_offset"):
                        continue                     # forced 角落鎖定片（3.5m 情境豁免）
                    raise RuntimeError(f"🔴 [{tag}] E3 後 {blk} 仍有 S=0 池片 {g.area:.2f}㎡")
        mid = [l for l in pool_final if 0.5 < pool_final[l] < mina[l] - 0.05]
        if mid:
            raise RuntimeError(f"🔴 [{tag}] 終態池落 (0,MinA)：{ {l: round(pool_final[l],2) for l in mid} }——停機上呈")

        # ══ E4：終態全域斷言 ══
        #   旗標=0 嚴格（裁示1(a) 宗地寬度≥min_width）——E1/E2 合成宗皆 _bisect_valid 至合法基地，
        #   終態不應殘旗標；殘留＝真畸零、停機（不再以 area≥MinA 放行寬<min_width 之宗，reviewer#6）。
        min_depth = float(snap["global"]["法定最小深_m"])
        alloc_dirs = cad.get("alloc_dir_by_block", {}) or {}
        flag_end = [k for k, r in E.items() if r["畸零地旗標"].strip()]
        if flag_end:
            raise RuntimeError(f"🔴 [{tag}] 終態殘餘畸零旗標（寬<min_width，裁示1(a)）：{flag_end}")
        e4_viol = []
        for k, r in E.items():
            blk = r["所屬街廓"]
            poly = (new_polys_by_blk.get(blk, {}).get(k)) or _poly_of_row(r)
            if poly is None:
                e4_viol.append(f"{k}: 無幾何")
                continue
            fl = (cad.get("front_lines") or {}).get(blk) or {}
            bpoly = Polygon(cb_by[blk]["vertices"])
            if not bpoly.is_valid:
                bpoly = bpoly.buffer(0)
            if wf_f1._front_len_of(poly, wf_f1._seg(fl), bpoly) < 0.5:
                e4_viol.append(f"{k}: 不臨 FRONT")
            adir = alloc_dirs.get(blk)                 # 深＝沿 raw alloc_dir（wd3 碎片判準同源）
            if adir:
                ax, ay = float(adir[0]), float(adir[1])
                nrm = (ax * ax + ay * ay) ** 0.5 or 1.0
                ax, ay = ax / nrm, ay / nrm
                cs = list(poly.exterior.coords)
                depth = (max(p[0] * ax + p[1] * ay for p in cs)
                         - min(p[0] * ax + p[1] * ay for p in cs))
                if depth < min_depth - 0.05:
                    e4_viol.append(f"{k}: 深 {depth:.2f} < 最小深 {min_depth}")
            if float(r["G(㎡)"]) < mina[blk] - TOL:
                e4_viol.append(f"{k}: G={r['G(㎡)']} < MinA_{blk}")
        if e4_viol:
            raise RuntimeError(f"🔴 [{tag}] E4 終態全域斷言破：{e4_viol[:6]}")
        # 位次序（投影序）：oE == oD 約簡序 ∪ 合成宗插入
        pos_viol = []
        for blk in sorted(mina):
            oD = _proj_order(ns, cad, f3_out[tag]["f3_parcels"], blk)
            oE = _proj_order(ns, cad, eng.parcels, blk)
            removed_all = _rm0 | set(rm2)
            exp = [x for x in oD if x not in removed_all]
            got = [x for x in oE if not x.startswith("74·")]
            if got != exp:
                pos_viol.append((blk, exp, got))
        if pos_viol:
            raise RuntimeError(f"🔴 [{tag}] 位次序破：{pos_viol[:2]}")
        cons = abs(sum(float(r["G(㎡)"]) for r in E.values()) + sum(pool_final.values())
                   - sum(float(cb_by[l].get("area_m2", 0) or 0) for l in pool_final))
        # §N3-0 全區級帳對幾何閘（補丁三 §二）＝逐街廓加總；舊 `<6` 廢（殘餘定閘·N0-17）
        cons_tol = sum(
            ns["_acct_geom_tol_block"](
                sum(1 for _r in E.values() if _r.get("所屬街廓") == l),
                float(snap["blocks"][l]["街廓分配深度_m"]))
            for l in pool_final)

        # ══ E5：總決算（33 群 應走 vs 實走） ══
        ledger_rows, unattr = _ledger(tag, HERE, omap, E, mina, events,
                                      f0_out[tag], f2_out[tag], f3_out[tag])
        if unattr:
            raise RuntimeError(f"🔴 [{tag}] 總決算不可歸因：{unattr}——停機上呈")

        # ── 表 ──
        g_tab, _, _ = build_step_g_tables(sgE)
        pool_rows = [{"情境": tag, "街廓": l, "池_D(㎡)": round(poolD[l], 2),
                      "池_E引擎(㎡)": round(poolE[l], 2), "池_E3整形後(㎡)": round(pool_final[l], 2),
                      "MinA": mina[l],
                      "三則": ("歸零" if pool_final[l] < 1 else "≥MinA")}
                     for l in sorted(pool_final)]
        anchors = {
            "wavg": wavg, "comp_groups": sorted(comp_groups),
            "comp_amounts": {g: _money(ginfo[g]["a"] * wavg) for g in sorted(comp_groups)},
            "e0_targets": {k: v[2]["暫編地號"] for k, v in e0_pairs.items()},
            "n_syn": len([p for p in syn_ids.values() if p in E]),
            "rounds": rounds, "spill_75": sorted({s[0] for s in spill_75}),
            "pool_final": {l: round(v, 2) for l, v in sorted(pool_final.items())},
            "resh_targets": dict(resh_targets), "cons_resid": round(cons, 2),
            "cons_tol": round(cons_tol, 4),      # §N3-0 全區閘寬（逐街廓加總·補丁三 §二）
            "flags_end": 0, "pos_viol": [], "b1_ok": True,
            "med_dist": round(med, 1),
            "e2_opt": {k: e2_opt[k] for k in ("assign", "opt_cost", "opt_inc", "opt_dist",
                                              "second_cost", "tie_count", "space", "n_feasible",
                                              "n_actual_eval", "canon_best", "capped", "max_err")},
            "e2_cost_matrix": e2_opt["cost_matrix"], "e2_eligible": e2_opt["eligible"],
            "verdict_all_green": all("🔴" not in str(v["判定"]) for v in sgE["pool_diag"].values()),
        }
        out[tag] = {"conv_rows": conv_rows, "exit_rows": exit_rows, "g_tab": g_tab,
                    "pool_rows": pool_rows, "reshape_rows": reshape_rows,
                    "ledger_rows": ledger_rows, "anchors": anchors,
                    # 🆕 G.2 消費（trunk E 原始列含 cut_coords＋E3 整形新形；純加性·深拷貝/tuple 凍結防 UI 反灌）
                    "sgE_rows": copy.deepcopy(sgE["g_rows"]),
                    "reshape_polys": {blk: {pid: tuple(map(tuple, p.exterior.coords))
                                            for pid, p in polys.items()}
                                      for blk, polys in new_polys_by_blk.items()}}
    return out


def _proj_order(ns, cad, parcels, blk):
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pib = [{"暫編地號": tp["暫編地號"], "polygon_coords": tp.get("polygon_coords")}
           for tp in parcels if tp["所屬街廓"] == blk and not tp.get("_is_ghost_sliver")]
    return [x["暫編地號"] for x in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]


def _row_centroid(row):
    """g_row 之 cut_coords 質心（起迄距離之起點；建地軌源宗移除前擷取）。"""
    if not row:
        return None
    cs = row.get("cut_coords") or []
    if len(cs) < 3:
        return None
    p = Polygon(cs)
    if not p.is_valid:
        p = p.buffer(0)
    return (p.centroid.x, p.centroid.y)


def _e2_optimal(tag, ns, eng, households, mina, depth_by, p_avg, pre_price, post_price,
                snapE, cb_by, cad, forced, pool_cen, d_off,
                syn_ids, placed, conv_rows, exit_rows, events):
    """7-5 第2梯類批次全域最佳化（KL 裁定 2026-07-12；就地 commit、回傳 opt_meta）。

    - 資格＝§31-1-2 比較級（頓號讀「或」）：{深度淺於原街廓} ∪ {後價低於原街廓}；
      公設軌無原街廓 → 全可建築塊（達標門檻用區標準、手冊(三)）。
    - **兩階段可證最優**（非啟發式）：①canonical 窮舉快篩（合成宗 solo G 近似）＋容量剪枝 →
      成本帶（±SLACK 覆蓋位置相依 G 誤差）；②帶內候選以**引擎實際 G** 重評（全額 a′ 一次 run
      讀 G/寬）取真最優。band-sufficiency 閘：max|canon−actual|<SLACK ⟹ 帶外候選不可能勝出。
    - **Q3＋裁示1(a)**：配額＝合法最小建築基地（寬≥min_width 且 G≥MinA）；增配＝max(0,該目標−G(a′))；
      深度>名目致寬<min_width 時 area 微增至 min_width×depth_local（§8 型幾何、非政策超額）。
    - 池三則以容量約束（每塊 Σconsume ≤ reachable−MinA，留 ≥MinA 可達殘池；S=0 片入 unreach）。
    - 目標 min Σ增配金額(×後價) → tie Σ增配面積 → Σ質心起迄距 → 塊指派字典序（gid 序、決定性）。
    """
    import itertools
    blocks = sorted(mina)
    unreach = _s0_unreachable(ns, snapE, cb_by, cad, eng, forced)
    reachable = {b: max(eng.pool(b) - unreach.get(b, 0.0), 0.0) for b in blocks}
    mw_by = {b: float(ns["get_min_lot_size"](cb_by[b]["category"],
             float(snapE["blocks"][b]["正面"]["路寬_m"]))["min_width"]) for b in blocks}

    def _elig(h):
        if h["orig"] is None:
            return list(blocks), {b: "公設軌·全塊(手冊(三))" for b in blocks}
        do, po = depth_by[h["orig"]], post_price[h["orig"]]
        out, why = [], {}
        for b in blocks:
            sh, ch = depth_by[b] < do - 1e-9, post_price[b] < po - 1e-9
            if sh or ch:
                out.append(b)
                why[b] = "＋".join(x for x in ("深度較淺" if sh else "",
                                               "後價較低" if ch else "") if x)
        return out, why

    def _canon_G(h, b):
        """canonical (G, width)(a′)：solo 置合成宗於池錨（同 commit-first 位置）、全額 a′、讀引擎。
        位置固定＝決定性、可重現。回傳 (G, width, a′_full) 或 (None, None, a′_full)。"""
        a_full = h["a"] * pre_price[h["zone"]] / p_avg[b]
        if reachable[b] < mina[b] - 0.5:
            return None, None, a_full
        anc = _cur_pool_anchor(eng, b) or pool_cen[b][0]
        pid = eng.add_syn(f"K·{h['gid']}", b, _zone_key(b), (anc[0], anc[1]))
        eng.set_area(pid, a_full)                          # 全額 a′（撞牆則退回 probe 外插）
        rows = eng.try_rows()
        if rows is not None and pid in rows:
            G = float(rows[pid]["G(㎡)"]); W = float(rows[pid]["宗地寬度(m)"])
        else:
            ap = min(a_full, max(3.0, reachable[b] * 0.5))
            eng.set_area(pid, ap)
            r2 = eng.try_rows()
            if r2 is not None and pid in r2 and ap > 0:
                G = float(r2[pid]["G(㎡)"]) / ap * a_full
                W = float(r2[pid]["宗地寬度(m)"]) / ap * a_full
            else:
                G = W = None
        eng.remove([pid])
        return G, W, a_full

    cost, elig_map, why_map = {}, {}, {}
    for h in households:
        el, why = _elig(h)
        why_map[h["gid"]] = why
        feas = []
        for b in el:
            G, W, a_full = _canon_G(h, b)
            if G is None:
                continue
            gt = _valid_G(G, W, mw_by[b], mina[b])         # 合法基地目標 G（含 min_width）
            inc = max(0.0, gt - G)
            consume = max(G, gt)
            if consume > reachable[b] - mina[b] + 0.5:      # solo 已超容
                continue
            cx, cy = h["anchor_cen"]
            px, py = (pool_cen[b][0] if pool_cen.get(b) else (cx, cy))
            cost[(h["gid"], b)] = {
                "a_prime": a_full, "G": G, "inc": inc, "consume": consume,
                "cost": inc * post_price[b], "dist": ((cx - px) ** 2 + (cy - py) ** 2) ** 0.5,
                "why": why.get(b, "")}
            feas.append(b)
        if not feas:
            return {"feasible": False, "reason": f"{h['gid']} 無合格且可行落位塊",
                    "eligible": el, "reachable": {b: round(reachable[b], 2) for b in blocks}}
        elig_map[h["gid"]] = feas

    gids = [h["gid"] for h in households]
    opts = [elig_map[g] for g in gids]
    space = 1
    for o in opts:
        space *= len(o)
    # ── 階段一：canonical 窮舉快篩（G=k·a′ 位置無關近似；供容量剪枝＋成本帶）──
    feas = []                                            # (canon_cost, canon_inc, dist, combo)
    for combo in itertools.product(*opts):
        by_blk = collections.defaultdict(float)
        for g, b in zip(gids, combo):
            by_blk[b] += cost[(g, b)]["consume"]
        if any(cs > reachable[b] - mina[b] + 0.5 for b, cs in by_blk.items()):
            continue
        tc = sum(cost[(g, b)]["cost"] for g, b in zip(gids, combo))
        ti = sum(cost[(g, b)]["inc"] for g, b in zip(gids, combo))
        td = sum(cost[(g, b)]["dist"] for g, b in zip(gids, combo))
        feas.append((round(tc, 2), round(ti, 3), round(td, 2), combo))
    if not feas:
        return {"feasible": False, "reason": "窮舉無可行指派（容量約束）", "space": space,
                "reachable": {b: round(reachable[b], 2) for b in blocks},
                "cost_matrix": {f"{g}@{b}": {"G": round(v['G'], 2), "inc": round(v['inc'], 2)}
                                for (g, b), v in sorted(cost.items())}}
    feas.sort()
    canon_best = feas[0][0]
    # ── 階段二：成本帶內候選以引擎實際 G 重評（位置相依之嚴格化，證真最優非近似）──
    #   G 經局部塊深位置相依（多戶同塊之後置戶落較淺處，實測 canonical 誤差 ≤~1㎡/宗）。
    #   SLACK 保守覆蓋：band 外候選 actual ≥ canon−SLACK > actual_best，數學上不可能勝出 → 免評。
    SLACK = len(gids) * POS_SLACK_AREA * max(post_price.values())
    in_band = [f for f in feas if f[0] <= canon_best + SLACK]
    capped = len(in_band) > CAP_EVAL
    if capped:                                          # 截斷＝band-sufficiency 證明不完整 → 停機
        return {"feasible": False, "reason": f"成本帶內候選 {len(in_band)} > CAP_EVAL {CAP_EVAL}"
                f"（截斷則最優性不保，須提高 CAP_EVAL 或加緊剪枝）", "space": space}
    band = in_band

    def _actual(combo):
        """引擎實際成本：全額 a′ 置各宗、一次 run、讀 G、算 Σ(inc×price)；回滾。
        回傳 (cost, inc, dist, combo) 或 None（撞牆/超容）。"""
        pids = []
        for g, b in zip(gids, combo):
            anc = _cur_pool_anchor(eng, b) or pool_cen[b][0]
            k = sum(1 for (_g, _b, _p) in pids if _b == b)
            cen = (anc[0] + k * 0.6 * float(d_off[b][0]), anc[1] + k * 0.6 * float(d_off[b][1]))
            pid = eng.add_syn(f"A·{g}", b, _zone_key(b), cen)
            eng.set_area(pid, cost[(g, b)]["a_prime"])
            pids.append((g, b, pid))
        rows = eng.try_rows()
        res = None
        if rows is not None:
            tc = ti = td = 0.0
            csm = collections.defaultdict(float)
            ok = all(p in rows for _, _, p in pids)
            for g, b, pid in pids:
                if not ok:
                    break
                G = float(rows[pid]["G(㎡)"]); W = float(rows[pid]["宗地寬度(m)"])
                gt = _valid_G(G, W, mw_by[b], mina[b])     # 合法基地目標（含 min_width）
                inc = max(0.0, gt - G)
                tc += inc * post_price[b]
                ti += inc
                td += cost[(g, b)]["dist"]
                csm[b] += max(G, gt)
            if ok and all(csm[b] <= reachable[b] - mina[b] + 0.5 for b in csm):
                res = (round(tc, 2), round(ti, 3), round(td, 2), tuple(combo))
        eng.remove([p for _, _, p in pids])
        eng.invalidate()
        return res

    canon_by_combo = {f[3]: f[0] for f in band}
    actual = [r for r in (_actual(f[3]) for f in band) if r is not None]
    if not actual:
        return {"feasible": False, "reason": "成本帶內候選皆引擎不可行（超容/撞牆）",
                "n_band": len(band), "reachable": {b: round(reachable[b], 2) for b in blocks}}
    # band-sufficiency 閘（證 band 外候選不可能勝出）：max|canon−actual| < SLACK ⟹
    #   任一 band 外候選 actual ≥ canon−SLACK > canon_best ≥ actual_best（∵ actual_best≤canon_best）。
    #   實測 max_err << SLACK 即放行；逼近 SLACK＝位置誤差超估、band 可能漏 → 停機上呈。
    max_err = max(abs(canon_by_combo[r[3]] - r[0]) for r in actual)
    if max_err >= SLACK:
        return {"feasible": False, "reason": f"band-sufficiency 破：max|canon−actual|={max_err:.0f} "
                f"≥ SLACK={SLACK:.0f}（位置誤差超 band，最優性不保，停機上呈）"}
    actual.sort()
    best = actual[0]                                     # (cost, inc, dist, combo)
    combo = list(best[3])
    assign = dict(zip(gids, combo))
    a_distinct = sorted({r[0] for r in actual})
    second = a_distinct[1] if len(a_distinct) > 1 else None
    tie_ct = sum(1 for r in actual if r[0] == a_distinct[0])
    hby = {h["gid"]: h for h in households}

    for g in gids:                                        # commit 真最優（bisect 增配至 MinA）
        b = assign[g]
        cm = cost[(g, b)]
        anc = _cur_pool_anchor(eng, b) or pool_cen[b][0]
        off = len([1 for (gg, bb) in syn_ids if bb == b]) * 0.6
        cen = (anc[0] + off * float(d_off[b][0]), anc[1] + off * float(d_off[b][1]))
        pid = eng.add_syn(g, b, _zone_key(b), cen)
        syn_ids[(g, b)] = pid
        eng.set_area(pid, cm["a_prime"])                  # 先置全額 a′，讀實際 G(a′)、寬
        _r_ap = eng.rows()[pid]                           # fail-loud（撞牆＝真 bug）
        G_ap = float(_r_ap["G(㎡)"]); W_ap = float(_r_ap["宗地寬度(m)"])
        if W_ap >= mw_by[b] + WIDTH_MARGIN - 1e-6 and G_ap >= mina[b] - TOL:  # 已達合法基地：全額
            G_fin, zeng = G_ap, 0.0
        else:                                             # 增配至合法基地（寬≥min_width 且 G≥MinA）
            _bisect_valid(eng, pid, b, mw_by[b], mina[b])
            G_fin = float(eng.rows()[pid]["G(㎡)"])
            zeng = round(G_fin - G_ap, 2)
        placed[(g, b)] = float(eng.by_id()[pid]["面積_m2"])
        if eng.rows()[pid]["畸零地旗標"].strip() or G_fin < mina[b] - TOL:
            return {"feasible": False, "reason": f"{g}@{b} 概念4/裁示1(a) 破：G={G_fin:.2f} 寬 "
                    f"{float(eng.rows()[pid]['宗地寬度(m)']):.2f}（仍畸零）"}
        if zeng < 0:
            return {"feasible": False, "reason": f"{g}@{b} 負增配 {zeng}"}
        cm["G"] = G_ap                                    # 以實際 G(a′) 回填帳表
        h = hby[g]
        exit_rows.append({"情境": tag, "歸戶": g, "類": h["kind"],
                          "出口": ("增配§31-1-2" if zeng > 0 else "≥½ 配地 G(a′)"),
                          "G(a′)輪0(㎡)": round(cm["G"], 2), "2×G vs 114.07": "≥",
                          "Σa(㎡)": round(h["a"], 2), "配額G(㎡)": round(G_fin, 2),
                          "增配面積(㎡)": zeng,
                          "差額地價(元)§52-1": (_money(zeng * post_price[b]) if zeng > 0 else ""),
                          "放棄改領(元)§53-2": _money(cm["G"] * post_price[b]),
                          "補償_本文式(元)§53-1": "", "補償_但書式(元)": "",
                          "目標塊": b, "資格款": cm["why"],
                          "意思決定": ("增配>0·試分配預設自動" if zeng > 0 else "")})
        conv_rows.append({"情境": tag, "段": "E2·7-5", "歸戶": g, "源": h["src"],
                          "源塊": h["src_blk"], "目標宗": pid, "目標塊": b,
                          "級別": "7-5批次最佳化", "起迄距(m)": round(cm["dist"], 1),
                          "a源(㎡)": round(h["a"], 2), "模式一a′(㎡)": "—",
                          "模式二a′(㎡)": round(cm["a_prime"], 2),
                          "a″引擎(㎡)": round(placed[(g, b)], 2), "配額G(㎡)": round(G_fin, 2),
                          "處置": ("7-5 增配" if zeng > 0 else "7-5 配地")})
        events[g].append(f"E2 7-5批次 {b} G={G_fin:.2f}" + (f" 增配{zeng}" if zeng else ""))

    return {"feasible": True, "assign": assign, "opt_cost": round(best[0], 2),
            "opt_inc": round(best[1], 2), "opt_dist": round(best[2], 1),
            "second_cost": second, "tie_count": tie_ct, "space": space,
            "n_feasible": len(feas), "n_actual_eval": len(actual),
            "canon_best": canon_best, "capped": capped, "max_err": round(max_err, 0),
            "eligible": {g: elig_map[g] for g in gids},
            "reachable": {b: round(reachable[b], 2) for b in blocks},
            "cost_matrix": {f"{g}@{b}": {"G": round(v["G"], 2), "inc": round(v["inc"], 2),
                                         "金額": _money(v["cost"]), "why": v["why"]}
                            for (g, b), v in sorted(cost.items())}}


def _reshape_block(ns, snap, cb_by, cad, forced, rows_E, blk, frag, tag, mina):
    """域裁 (B) 等 G 幾何重切＋前移——wf_f1 R1 機制通用化（任意塊×左右側）。
    回傳 (reshape_rows, new_polys, target_id)。停機條款全同 F.1。"""
    lots = [r for r in rows_E if r["所屬街廓"] == blk and r.get("推進側別") in ("left", "right")]
    gm = ns["get_min_lot_size"]
    blkm = cb_by[blk]
    block_poly = Polygon(blkm["vertices"])
    if not block_poly.is_valid:
        block_poly = block_poly.buffer(0)
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    p1, p2 = np.array(fl["p1"], float), np.array(fl["p2"], float)
    L_fl = float(np.linalg.norm(p2 - p1))
    d_hat = (p2 - p1) / L_fl
    alloc_dir = ns["alloc_normal_axis"]((cad.get("alloc_dir_by_block") or {}).get(blk))
    if alloc_dir is None:
        raise RuntimeError(f"🔴 [{tag}] {blk} 缺宗地分配線，E3 停")
    cos_dn = abs(float(np.dot(d_hat, np.asarray(alloc_dir, float))))
    mw = float(gm(blkm["category"], float(snap["blocks"][blk]["正面"]["路寬_m"]))["min_width"])
    avg_depth = float(snap["blocks"][blk]["街廓分配深度_m"])
    _block_strip = ns["_block_strip"]
    side = "left" if (frag["s"] is not None and frag["s"] < 0.5) else "right"
    fo = (forced or {}).get(blk, {}) or {}
    # 🆕 §3（plan v3 §3·補丁九）：buf 廢矩形近似 `range ÷ avg_depth` → `_corner_buffer_S` 幾何 bisect。
    #   ⚠️ **方位契約**：`_corner_buffer_S` 一律傳 **FRONT p1（`p1`）＋ `+d̂`（`d_hat`）**、端由 `side` 定——
    #      **禁**傳本 scope 之 reversed 對（`corner`／`dh`），否則帶跑到街廓另一端＝#25 全額重演（BLOCKED-2）。
    if side == "left":
        corner = p1.copy()
        dh = d_hat
        buf = (ns["_corner_buffer_S"](block_poly, d_hat, p1, alloc_dir,
                                      float(fo.get("left_corner_min_area", 0.0) or 0.0),
                                      'left', _label=f"{blk}·E3")
               if fo.get("left_forced_offset") else 0.0)
    else:
        # 🆕 step 0（正交→斜交 s_max·plan v3 §2·#20 四處同源 _oblique_s_max）
        _smax_f4 = ns["_oblique_s_max"](blkm["vertices"], d_hat, p1, alloc_dir)
        if _smax_f4 is None:
            raise RuntimeError(f"🔴 step0：_oblique_s_max 回 None（{blk} 右·退化幾何）·no-silent-fallback")
        corner = p1 + _smax_f4 * d_hat
        dh = -d_hat
        buf = (ns["_corner_buffer_S"](block_poly, d_hat, p1, alloc_dir,
                                      float(fo.get("right_corner_min_area", 0.0) or 0.0),
                                      'right', _label=f"{blk}·E3")
               if fo.get("right_forced_offset") else 0.0)

    def strip_at(cum_S, S):
        cut, area = _block_strip(block_poly, dh, corner + (buf + cum_S) * dh, S,
                                 allocation_dir=alloc_dir)
        if cut is None or cut.is_empty:
            return None, 0.0
        if cut.geom_type != "Polygon":
            raise RuntimeError(f"🔴 [{tag}] E3 {blk} strip 非單一 Polygon，停")
        return cut, float(area)

    grp = sorted([r for r in lots if r["推進側別"] == side],
                 key=lambda x: float(x.get("累積S(m)", 0) or 0))
    other = [r for r in lots if r["推進側別"] != side]
    flagged = {r["暫編地號"] for r in lots if str(r.get("畸零地旗標", "")).strip()}
    wedge = frag["poly"]
    # ── 🆕 §4 末端塊 gate（補丁十 §一·**二條件皆真**才觸發末端 winner 門檻/fallback；缺一走現邏輯，如 R3 街角）──
    #   條件1：無 SIDELINE 那側（`has_side==False`·資料驅動）；條件2：block∩{s<0} 半平面 >ε（判別語意·**非**「有 frag」）。
    #   condition2（該側有未臨正街·補丁十 §一 **side-parametrized**·claude.ai 定稿）＝該側「未臨正街半平面」>ε：
    #     left ：`block∩{s<0}`（rel p1·s(p1)=0）；right：`block∩{s>s(p2)}`（s(p2)＝p2 於 ALLOC 切線軸 rel p1 之 s）。
    #     末端邊∥ALLOCLINE ⇒ 該側半平面≈0 ⇒ 無·跳過。右式鏡像左式（`_endpt=p2` 對稱）。
    _has_side_key = "left_has_side" if side == "left" else "right_has_side"
    _cond1 = not bool(fo.get(_has_side_key))
    _sdom = ns["_strip_s_range"](block_poly, d_hat, p1, alloc_dir)
    _smin0, _smax0 = (float(_sdom[0]), float(_sdom[1])) if _sdom else (0.0, 0.0)
    if side == "left":                                       # block∩{s<0}
        _unfront_area = (float(_block_strip(block_poly, d_hat, p1 + _smin0 * d_hat, -_smin0,
                                            allocation_dir=alloc_dir)[1] or 0.0)
                         if _smin0 < -1e-6 else 0.0)
    else:                                                    # block∩{s>s(p2)}（右鏡像·claude.ai 補式）
        _mh, _den = ns["_strip_axis"](d_hat, alloc_dir)
        _s_p2 = float(np.dot(p2 - p1, _mh) / _den)
        _unfront_area = (float(_block_strip(block_poly, d_hat, p1 + _s_p2 * d_hat, _smax0 - _s_p2,
                                            allocation_dir=alloc_dir)[1] or 0.0)
                         if _smax0 > _s_p2 + 1e-6 else 0.0)
    _end_gate = _cond1 and (_unfront_area > 1e-3)                 # ε＝1e-3㎡
    _area_rend = None
    if _end_gate:                                                # 缺 cad_alloc → loud（winner 純加性·不打紅綠案·靶c）
        _endpt = p1 if side == "left" else p2                    # 未臨正街端之 FRONT 端點（frag["s"] 側）
        _, _, _area_rend = ns["_end_region_R"](
            block_poly, (cad.get("alloc_dir_by_block") or {}).get(blk), _endpt, mw, wedge,
            _label=f"{blk}·E3[{tag}]")
    target_row, skipped = None, []
    for r in grp:
        _qual = (float(r.get("S(m)", 0) or 0) > 0.01               # 得以分配（保 `寬≥mw`·#1.6-3·與現候選集同）
                 and float(r.get("宗地寬度(m)", 0) or 0) >= mw
                 and r["暫編地號"] not in flagged)
        if _qual and (not _end_gate or float(r.get("G(㎡)", 0) or 0) >= _area_rend):
            target_row = r                                        # gate 真：首個 G≥area(R_end)·**往後找**（補丁十 §8-2）
            break
        skipped.append(r["暫編地號"])
    if target_row is None:
        if _end_gate:
            # ── 🆕 無勝者 fallback（補丁十 §一·§8-1 甲·池重定位·latent；UC9898 winner G≫area(R_end)→不觸發）──
            #   抵費地(末)＝R_end（frag∪末端帶）·占末端位·**new key**（E3 caller 以「不在 E」判之→池重定位·
            #   排除帳對閘宗和·pool_final=poolE−area(R_end)）；候選（得以分配建地）內移·G 不變·排 R_end 內側·非疊；
            #   守恆 ΣG＋pool_final＋抵費地街角＋抵費地末＝街廓（frag 只在 poolE、不雙計——見 plan §2/KL 旗）。
            _, _rend_poly, _rend_area = ns["_end_region_R"](
                block_poly, (cad.get("alloc_dir_by_block") or {}).get(blk), _endpt, mw, wedge,
                _label=f"{blk}·E3[{tag}]·fb")
            if _rend_poly.geom_type != "Polygon":
                _rend_poly = _rend_poly.buffer(0)
            _abate_key = f"{blk}-抵費地末"
            fb_polys = {_abate_key: _rend_poly}
            fb_rows = [{"情境": tag, "街廓": blk, "暫編地號": _abate_key,
                        "角色": f"抵費地(末)(無勝者·池重定位·{side})", "G_E(㎡)": 0.0,
                        "新形面積(㎡)": round(float(_rend_area), 2), "S_E(m)": 0.0,
                        "S_new(m)": 0.0, "宗地寬度_new(m)": 0.0,
                        "Δ面積(㎡)": round(float(_rend_area), 2)}]
            _rd = ns["_strip_s_range"](_rend_poly, dh, corner, alloc_dir)
            cum = (float(_rd[1]) - buf) if _rd else 0.0        # 候選自 R_end 之 s-max 起（排 R_end 內側·非疊）
            for r in grp:
                G_i, S_i_B = float(r["G(㎡)"]), float(r["S(m)"])
                S_i, a_i = wf_f1._bisect_area(lambda S, _c=cum: strip_at(_c, S)[1], G_i, 0.0, S_i_B + 2.0)
                if abs(a_i - G_i) > 0.01:
                    raise RuntimeError(f"🔴 [{tag}] E3 {blk} fallback 內移宗 {r['暫編地號']} G 全等破：{a_i:.3f}≠{G_i}")
                cut_i, _ = strip_at(cum, S_i)
                if cut_i is None or cut_i.is_empty:
                    raise RuntimeError(f"🔴 [{tag}] E3 {blk} fallback 內移宗 {r['暫編地號']} strip 空——退化")
                fb_polys[r["暫編地號"]] = cut_i
                fb_rows.append({"情境": tag, "街廓": blk, "暫編地號": r["暫編地號"], "角色": "內移(fallback)",
                                "G_E(㎡)": G_i, "新形面積(㎡)": round(float(cut_i.area), 2),
                                "S_E(m)": S_i_B, "S_new(m)": round(S_i, 2),
                                "宗地寬度_new(m)": round(S_i * cos_dn, 2),
                                "Δ面積(㎡)": round(float(cut_i.area) - G_i, 3)})
                cum += S_i
            for r in other:
                fb_polys[r["暫編地號"]] = _poly_of_row(r)
                fb_rows.append({"情境": tag, "街廓": blk, "暫編地號": r["暫編地號"], "角色": "對側·未動",
                                "G_E(㎡)": float(r["G(㎡)"]),
                                "新形面積(㎡)": round(float(_poly_of_row(r).area), 2),
                                "S_E(m)": float(r["S(m)"]), "S_new(m)": float(r["S(m)"]),
                                "宗地寬度_new(m)": float(r["宗地寬度(m)"]), "Δ面積(㎡)": ""})
            for _k, _p in fb_polys.items():                    # 非疊複驗：抵費地末 vs 內移宗（KL/reviewer②）
                if _k == _abate_key:
                    continue
                _ov = float(_rend_poly.intersection(_p).area)
                if _ov > 0.01:
                    raise RuntimeError(f"🔴 [{tag}] E3 {blk} fallback 抵費地末與 {_k} 疊 {_ov:.3f}㎡")
            def _order_fb(polys):                              # 位次序不變（排除抵費地末·新增於末端位）
                pseudo = [{"暫編地號": k, "polygon_coords": list(v.exterior.coords)}
                          for k, v in polys.items()]
                return [t["暫編地號"] for t in ns["_projection_order"](pseudo, fl["p1"], fl["p2"])]
            _oE = _order_fb({r["暫編地號"]: _poly_of_row(r) for r in lots})
            _oN = [k for k in _order_fb(fb_polys) if k != _abate_key]
            if _oE != _oN:
                raise RuntimeError(f"🔴 [{tag}] E3 {blk} fallback 位次序變動：{_oE}→{_oN}")
            return fb_rows, fb_polys, None
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 往前搜尋窮盡無有效宗（跳過 {skipped}）")
    tgt_poly = _poly_of_row(target_row)
    if wedge.distance(tgt_poly) >= 0.05:
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 楔形與標的 {target_row['暫編地號']} 不相鄰"
                           f"（dist={wedge.distance(tgt_poly):.3f}），停")
    S_B, G_B = float(target_row["S(m)"]), float(target_row["G(㎡)"])
    area_B = float(target_row["幾何面積(㎡)"])
    S_chk, _ = wf_f1._bisect_area(lambda S: strip_at(0.0, S)[1], area_B, 0.0, S_B + 2.0)
    if abs(S_chk - S_B) > 0.01:
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 原語自檢破：S_chk={S_chk:.4f}≠{S_B}")

    def _fuse(a, b):
        # **補償-2 已拆（plan §4.2）**；縫之處置一律走 wf_f1._fuse_strict（單一真相源·防 #20）
        return wf_f1._fuse_strict(a, b, tag, f"E3 {blk}（side={side}·tgt={target_row['暫編地號']}）")

    def union_area(S):
        cut, _ = strip_at(0.0, S)
        return wedge.area if cut is None else float(_fuse(cut, wedge).area)
    S_new, a_new = wf_f1._bisect_area(union_area, G_B, 0.0, S_B)
    w_new = S_new * cos_dn
    if abs(a_new - G_B) > 0.01:
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 標的 G 全等破：{a_new:.3f}≠{G_B}")
    if w_new < mw:
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 整形後寬 {w_new:.2f}<{mw}（不得製造新畸零）")
    cut_new, _ = strip_at(0.0, S_new)
    tgt_shape = _fuse(cut_new, wedge)
    if tgt_shape.geom_type != "Polygon":
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 標的新形非單一 Polygon，停")
    new_polys = {target_row["暫編地號"]: tgt_shape}
    rows = [{"情境": tag, "街廓": blk, "暫編地號": target_row["暫編地號"],
             "角色": f"標的(吞楔形·{side})", "G_E(㎡)": G_B,
             "新形面積(㎡)": round(float(tgt_shape.area), 2), "S_E(m)": S_B,
             "S_new(m)": round(S_new, 2), "宗地寬度_new(m)": round(w_new, 2),
             "Δ面積(㎡)": round(float(tgt_shape.area) - G_B, 3)}]
    cum = S_new
    for r in grp:
        if r["暫編地號"] == target_row["暫編地號"]:
            continue
        G_i, S_i_B = float(r["G(㎡)"]), float(r["S(m)"])
        S_i, a_i = wf_f1._bisect_area(lambda S, _c=cum: strip_at(_c, S)[1], G_i, 0.0, S_i_B + 2.0)
        if abs(a_i - G_i) > 0.01:
            raise RuntimeError(f"🔴 [{tag}] E3 {blk} 前移宗 {r['暫編地號']} G 全等破")
        w_i = S_i * cos_dn
        if w_i < mw and r["暫編地號"] not in flagged:
            raise RuntimeError(f"🔴 [{tag}] E3 {blk} 前移宗 {r['暫編地號']} 新生畸零 寬{w_i:.2f}")
        cut_i, _ = strip_at(cum, S_i)
        new_polys[r["暫編地號"]] = cut_i
        rows.append({"情境": tag, "街廓": blk, "暫編地號": r["暫編地號"], "角色": "前移",
                     "G_E(㎡)": G_i, "新形面積(㎡)": round(float(cut_i.area), 2),
                     "S_E(m)": S_i_B, "S_new(m)": round(S_i, 2),
                     "宗地寬度_new(m)": round(w_i, 2),
                     "Δ面積(㎡)": round(float(cut_i.area) - G_i, 3)})
        cum += S_i
    for r in other:
        new_polys[r["暫編地號"]] = _poly_of_row(r)
        rows.append({"情境": tag, "街廓": blk, "暫編地號": r["暫編地號"], "角色": "對側·未動",
                     "G_E(㎡)": float(r["G(㎡)"]),
                     "新形面積(㎡)": round(float(_poly_of_row(r).area), 2),
                     "S_E(m)": float(r["S(m)"]), "S_new(m)": float(r["S(m)"]),
                     "宗地寬度_new(m)": float(r["宗地寬度(m)"]), "Δ面積(㎡)": ""})
    # 位次序不變（塊內）
    def _order(polys):
        pseudo = [{"暫編地號": k, "polygon_coords": list(v.exterior.coords)}
                  for k, v in polys.items()]
        return [t["暫編地號"] for t in ns["_projection_order"](pseudo, fl["p1"], fl["p2"])]
    oE = _order({r["暫編地號"]: _poly_of_row(r) for r in lots})
    oN = _order(new_polys)
    if oE != oN:
        raise RuntimeError(f"🔴 [{tag}] E3 {blk} 位次序變動：{oE}→{oN}")
    return rows, new_polys, target_row["暫編地號"]


def _chain_cat(c):
    """實走鏈元素 → 歸因類別（None＝不可歸因）。"""
    for pref, cat in (("F.0梯3", "F0釋池"), ("F.0全達標", "全達標"), ("F.0級0", "F0併"),
                      ("F.2跨併", "F2跨併"), ("F.3併入", "F3併入"), ("F.3轉7-4", "F3轉74"),
                      ("E0級1", "E0級1"), ("E1 ½測試<½", "E1補償"), ("E1 7-4 配地", "E1配地"),
                      ("E1 無塊可規配", "E1溢入"), ("E2 7-5", "E2七五"),
                      ("零動作", "零動作")):
        if c.startswith(pref):
            return cat
    return None


# 白名單：應走(軌別,梯次) → 實走鏈合法類別集（E5 總決算；不可歸因＝停機上呈）
#   梯0：F.0 同街廓併／F.2 跨併／逃生門(E2七五)／殘旗標宗 E0 級1／F.3 公設併入／全達標留置
#   梯1：零動作達標留置（另斷言群內宗 trunk E 全達標）＋ F.3 公設併入
#   梯2：E2 增配(G004/G033)／E0 級1(G011)／F.3 併入達標(G032)
#   梯3：F.0 釋池補償；G025 另有公設宗走 E1 7-4（合法複線）
#   公設軌：F.3 轉7-4 → E1 配地/補償/溢入 → E2 增配
_WL = {
    ("建地軌", "0"): {"F0併", "全達標", "F2跨併", "F3併入", "E0級1", "E2七五"},
    ("建地軌", "1"): {"零動作", "F3併入", "全達標"},
    ("建地軌", "2"): {"F3併入", "E0級1", "E2七五", "全達標"},
    ("建地軌", "3"): {"F0釋池", "F3轉74", "E1配地", "E1補償", "E1溢入", "E2七五"},
    ("公設軌", "—"): {"F3轉74", "E1配地", "E1補償", "E1溢入", "E2七五"},
}


def _ledger(tag, here, omap, E_rows, mina, f4_events, f0d, f2d, f3d):
    """E5 總決算：33 群「應走（四梯清單）vs 實走鏈（F.0→F.4 事件）」逐群歸因。
    回傳 (rows, unattributed)。"""
    path = os.path.join(here, "baselines", "v3", f"W-D.4_四梯分級清單_退縮{tag}.csv")
    with open(path, encoding="utf-8-sig") as f:
        groups = [r for r in csv.DictReader(f) if r["情境"] == tag]
    gof = lambda p: omap.get(p, "")
    chain = collections.defaultdict(list)
    for r in f0d["dec_rows"]:
        chain[r["歸戶"]].append(f"F.0{r['級別']}→{r['去向']}" if r["級別"] != "全達標·無須併"
                                else "F.0全達標·無須併")
    for g in ("G025", "G030"):
        chain[g].append("F.0梯3釋池補償(§53兩式已列清單)")
    for r in f2d["conv_rows"]:
        chain[r["歸戶"]].append(f"F.2跨併級1 {r['源宗']}→{r['目標宗']}")
    for r in f3d["conv_rows"]:
        chain[r["歸戶"]].append(f"F.3併入 {r['公設筆']}→{r['目標宗']}")
    seen74 = set()
    for r in f3d["to74_rows"]:
        if r["歸戶"] not in seen74:
            chain[r["歸戶"]].append("F.3轉7-4")
            seen74.add(r["歸戶"])
    for gid, evs in f4_events.items():
        chain[gid].extend(evs)
    lots_by_g = collections.defaultdict(list)
    for k, r in E_rows.items():
        if not k.startswith("74·"):
            lots_by_g[gof(r["原地號"])].append(r)
    rows, unattr = [], []
    for g in groups:
        gid = g["歸戶鍵Gxxx"]
        exp = (g["軌別"], g["梯次"])
        ch = list(chain.get(gid, []))
        if exp == ("建地軌", "1") and not ch:
            ch = ["零動作·達標留置"]
        cats = [_chain_cat(c) for c in ch]
        ok = bool(ch) and all(cc is not None and cc in _WL.get(exp, set()) for cc in cats)
        if exp == ("建地軌", "1"):                    # 梯1 另須實測群內宗全達標
            lots = lots_by_g.get(gid, [])
            ok = ok and bool(lots) and all(
                float(r["G(㎡)"]) >= mina[r["所屬街廓"]] - 0.05
                and not r["畸零地旗標"].strip() for r in lots)
        if not ok:
            unattr.append((gid, exp, ch))
        rows.append({"情境": tag, "歸戶": gid, "軌別": g["軌別"], "梯次": g["梯次"],
                     "應走": g["路徑標註"][:40], "實走鏈": "；".join(ch) if ch else "（無事件）",
                     "歸因": ("✅" if ok else "🔴不可歸因")})
    return rows, unattr


def fixture_mode2_hand(snap, build_parcels):
    """模式二手算 fixture：獨立算式重算 p_avg 與 a′（供 run_verification 抽樣閘）。"""
    pre = {z: float(v["單價_元每m2"]) for z, v in
           snap["財務接線_v3"]["重劃前區段_面積單價"].items() if not z.startswith("74avg")}
    zof = snap["財務接線_v3"]["原地號_區段"]
    acc = collections.defaultdict(lambda: [0.0, 0.0])
    for tp in build_parcels:
        if tp.get("_is_ghost_sliver"):
            continue
        z = zof.get(tp["原地號"], "")
        if z in pre:
            a = float(tp.get("幾何面積_m2", 0) or 0)
            acc[tp["所屬街廓"]][0] += a * pre[z]
            acc[tp["所屬街廓"]][1] += a
    pavg = {b: v[0] / v[1] for b, v in acc.items() if v[1]}
    return pre, pavg
