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
- **E2 7-5**：逃生門/梯2/E1 溢入群，R4 優先→R3→R5（後價最低，tie 字典序）；
  配額=max(G(a′),MinA)；增配面積=配額−G(a′)、差額地價×後價（§52-1）、§53-2 放棄改領標旗；
  增配>0 標「意思決定・試分配預設自動」。
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

MINA_QU = 114.07
SNAP_WAVG = 72058.60964443642          # 快照 重劃後平均地價（等式閘基準；乘數用現算值）
COMP_EXPECT = {"G013", "G024", "G028"}  # ½ 輪0 <½ 具名錨（相異＝停查再定錨）
E0_EXPECT = {"628-49(1)": "628-48(1)", "628-30(2)": "628-45(2)", "628-42(1)": "628-42(2)"}
F1_REVERIFY = {"0m": "628-37(1)", "3.5m": "628-36(1)"}   # E3 R1 楔形標的複驗（F.1 錨）
E2_NAMED = {"G004": "628-52(1)", "G018": "628-51(1)", "G020": "628-50(1)",
            "G014": "628-29(1)", "G033": "628-46(1)"}    # 第2梯類 5 源宗（由旗標規則導出後對拍）
POST_LOW = ["R3", "R5"]                # 後價最低（67996 並列，字典序）
MAX_ROUNDS = 12
TOL = 0.05


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
        try:
            return float(self.rows()[pid]["G(㎡)"])
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


def _step_pool_floor(eng, pid, blk, floor, tol=0.1, max_iter=25):
    """單調自下方逼近池 floor（吃池歸零/rule1 用）：每步吃掉 90% 缺口、永不越
    「strip 吃盡」之守恆殘差牆。回傳 a″。"""
    r_est = 0.95                                  # 高估起步（步幅偏小＝安全；量測後更新）
    for _ in range(max_iter):
        pl = eng.pool(blk)
        if pl <= floor + tol:
            return float(eng.by_id()[pid]["面積_m2"])
        a_now = float(eng.by_id()[pid]["面積_m2"])
        g_now = float(eng.rows()[pid]["G(㎡)"]) if a_now > 0.01 else 0.0
        step = (pl - floor) * 0.9 / r_est
        eng.set_area(pid, a_now + step)
        g_new = float(eng.rows()[pid]["G(㎡)"])
        if step > 0.01 and g_new > g_now:
            r_est = min(max(((g_new - g_now) / step) * 1.15, 0.3), 0.98)  # ×1.15 安全係數防越牆
    raise RuntimeError(f"🔴 _step_pool_floor 不收斂：{pid}@{blk} floor={floor} 池={eng.pool(blk):.2f}")


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
            raise RuntimeError(f"🔴 [{tag}] E0 規則導出 ≠ 具名錨：{ {k: v[2]['暫編地號'] for k, v in e0_pairs.items()} }（期 {E0_EXPECT}）")
        if sorted(x[1]["暫編地號"] for x in e2_class) != sorted(E2_NAMED.values()):
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
            half_r0[gid] = (G0, 2 * G0 >= MINA_QU)
        comp_groups = {g for g, (_, ok) in half_r0.items() if not ok}
        if comp_groups != COMP_EXPECT:
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
                              "目標塊": "—", "意思決定": "§53-3 他項權利協調旗(本案空)"})
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

        def _usable(g, blk):
            """blk 可供 g 再灌一片 ≥MinA？回傳 (可用, demG_est, full_eat可行)。"""
            pool_now = eng.pool(blk)
            no_s0 = unreach.get(blk, 0.0) < 0.01
            demG = a_rem[g] * _conv(g, blk) * _ratio(g, blk)
            can_full = no_s0 and demG >= pool_now - 1.0 and pool_now >= mina[blk] - 0.5
            can_norm = (pool_now - mina[blk]) >= mina[blk] - 0.5
            if not (can_norm or can_full):
                return False, demG, can_full
            if demG < mina[blk] - 0.5:               # 小片：概念4 以引擎 solo 實測
                G, a2, a2p = _trial(g, blk, a_rem[g])
                if G is None or a2p < a2 - 0.01 or G < mina[blk] - 0.01:
                    return False, demG, can_full
            return True, demG, can_full

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
                    ok, _, _ = _usable(gid, blk)
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
                no_s0 = unreach.get(blk, 0.0) < 0.01
                demG = {g: a_rem[g] * _conv(g, blk) * _ratio(g, blk) for g in gs}
                full_eat = no_s0 and sum(demG.values()) >= eng.pool(blk) - 1.0
                budget = eng.pool(blk) - (0.0 if full_eat else mina[blk])
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
                                and eng.pool(b) - mina[b] >= mina[b] - 0.5]
                        if nxts:
                            b2 = nxts[0]
                            need = (mina[b2] + 0.5) / (_conv(g, b2) * _ratio(g, b2))
                            if rem_after < need:
                                a_used = max(0.0, a_rem[g] - need)
                        else:
                            a_used = a_rem[g]        # 無次塊：全塞，池 floor 校正把關
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
                # 池 floor 校正：實跑後若落中間態 → 對末灌宗調整、差額進出 a_rem
                pl = eng.pool(blk)
                filled = [g for g in gs if placed.get((g, blk), 0) > 0]
                if filled and 0.5 < pl < mina[blk] - 0.05:
                    last_g = filled[-1]
                    key = (last_g, blk)
                    pid = syn_ids[key]
                    a2_old = placed[key]
                    if full_eat:                 # rule1：末灌宗補吃至歸零（單調下逼近，不越牆）
                        a2fix = _step_pool_floor(eng, pid, blk, 0.45)
                    else:                        # rule3：縮末灌宗使池回 MinA（G 目標內域二分）
                        g_now = float(eng.rows()[pid]["G(㎡)"])
                        a2fix = _bisect_G(eng, pid, g_now - (mina[blk] - pl), TOL)
                    placed[key] = a2fix
                    d_a = (a2_old - a2fix) / _conv(last_g, blk)
                    a_rem[last_g] = max(a_rem[last_g] + d_a, 0.0)
                    ratio_est.pop((last_g, blk), None)

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

        # ══ E2：7-5 第2梯類雙出口 ══
        rm2 = sorted(x[1]["暫編地號"] for x in e2_class)
        if set(rm2) & win_set:
            raise RuntimeError(f"🔴 [{tag}] E2 移除宗為街角 winner：{sorted(set(rm2) & win_set)}")
        q75 = []
        for gid, r in e2_class:                       # 逃生門＋梯2（建地軌，源宗移除）
            q75.append({"gid": gid, "kind": "建地軌·第2梯類", "a": float(r["a 面積(㎡)"]),
                        "zone": zof[r["原地號"]], "src": r["暫編地號"], "src_blk": r["所屬街廓"]})
        for gid, why in spill_75:                     # E1 溢入之公設軌增配出口
            q75.append({"gid": gid, "kind": "公設軌·增配出口", "a": a_rem[gid],
                        "zone": ginfo[gid]["zone"], "src": f"公設群餘量", "src_blk": ginfo[gid]["anchor"]["blk"]})
        eng.remove(rm2)
        eng.invalidate()
        q75.sort(key=lambda q: (-(q["a"] * pre_price[q["zone"]]), q["gid"]))
        for q in q75:
            gid = q["gid"]
            placed_blk = None
            for blk in ["R4"] + POST_LOW:
                a2_ent = q["a"] * pre_price[q["zone"]] / p_avg[blk]     # a′ 權利量（模式二）
                pid = syn_ids.get((gid, blk))
                base_a2 = placed.get((gid, blk), 0.0)
                fresh = pid is None
                if fresh:
                    anc = _cur_pool_anchor(eng, blk)
                    if anc is None:
                        continue                      # 該塊池已空
                    off = len([1 for (gg, bb) in syn_ids if bb == blk]) * 0.6
                    cenb = (anc[0] + off * float(d_off[blk][0]),
                            anc[1] + off * float(d_off[blk][1]))
                    pid = eng.add_syn(gid, blk, _zone_key(blk), cenb)
                    syn_ids[(gid, blk)] = pid

                def _drop():
                    if fresh:
                        eng.remove([pid])
                        del syn_ids[(gid, blk)]
                    else:
                        eng.set_area(pid, base_a2)
                G_base = (float(eng.rows()[pid]["G(㎡)"]) if base_a2 > 0 else 0.0)
                pl = eng.pool(blk)
                # 量測邊際 G(a′)：probe 上限＋撞牆安全（r=G/a″<1 ⟹ G_probe < a″_probe ≤ 池−2）
                a2_probe = min(a2_ent, max(1.0, pl - unreach.get(blk, 0.0) - 2.0))
                eng.set_area(pid, base_a2 + a2_probe)
                G_read = eng.try_G(pid)
                eng.set_area(pid, base_a2)            # 還原試探
                if G_read is None or a2_probe < a2_ent - 0.01:   # 撞牆/蓋帽＝塞不進 → 轉次塊
                    _drop()
                    continue
                G_ent = G_read - G_base
                quota = max(G_ent, mina[blk])
                # 池規則：灌 quota 後池 ≥ MinA → 配；否則 池餘≥max(G(a′),MinA) 且無 S=0 片
                #   → 末戶吃池歸零（增配吸收）；否則轉次塊
                mode = None
                if pl - quota >= mina[blk] - TOL:
                    mode = "normal"                    # 灌後池仍 ≥ MinA
                elif (unreach.get(blk, 0.0) < 0.01 and pl >= G_ent - TOL
                      and pl >= mina[blk] - TOL):
                    mode = "eat_zero"                  # 末戶吃池歸零（增配吸收）
                else:
                    _drop()
                    continue
                if mode == "normal":
                    if quota - G_ent <= TOL:           # 配 G(a′)：a″=a′ 直灌（§142 原生）
                        eng.set_area(pid, base_a2 + a2_ent)
                    else:                              # 增配至 MinA（內域二分：池餘裕 ≥MinA）
                        _bisect_G(eng, pid, G_base + quota, TOL)
                else:                                  # 吃池歸零：單調下逼近（不越守恆牆）
                    eng.set_area(pid, base_a2 + a2_ent)
                    _step_pool_floor(eng, pid, blk, 0.45)
                G_fin = float(eng.rows()[pid]["G(㎡)"]) - G_base
                zeng = round(G_fin - G_ent, 2) if G_fin > G_ent + TOL else 0.0
                if zeng < 0:
                    raise RuntimeError(f"🔴 [{tag}] {gid} 負增配 {zeng}（規則矛盾）")
                placed[(gid, blk)] = float(eng.by_id()[pid]["面積_m2"])
                exit_rows.append({"情境": tag, "歸戶": gid, "類": q["kind"],
                                  "出口": ("增配§31-1-2" if zeng > 0 else "≥½ 配地 G(a′)"),
                                  "G(a′)輪0(㎡)": round(G_ent, 2),
                                  "2×G vs 114.07": "≥", "Σa(㎡)": round(q["a"], 2),
                                  "配額G(㎡)": round(G_fin, 2), "增配面積(㎡)": zeng,
                                  "差額地價(元)§52-1": (_money(zeng * post_price[blk]) if zeng > 0 else ""),
                                  "放棄改領(元)§53-2": _money(G_ent * post_price[blk]),
                                  "補償_本文式(元)§53-1": "", "補償_但書式(元)": "",
                                  "目標塊": blk,
                                  "意思決定": ("增配>0·試分配預設自動" if zeng > 0 else "")})
                conv_rows.append({"情境": tag, "段": "E2·7-5", "歸戶": gid, "源": q["src"],
                                  "源塊": q["src_blk"], "目標宗": pid, "目標塊": blk,
                                  "級別": "7-5(R4優先→R3→R5)", "起迄距(m)": "",
                                  "a源(㎡)": round(q["a"], 2), "模式一a′(㎡)": "—",
                                  "模式二a′(㎡)": round(a2_ent, 2),
                                  "a″引擎(㎡)": round(placed[(gid, blk)], 2),
                                  "配額G(㎡)": round(G_fin, 2),
                                  "處置": ("7-5 增配" if zeng > 0 else "7-5 配地")})
                events[gid].append(f"E2 7-5 {blk} G={G_fin:.2f}" + (f" 增配{zeng}" if zeng else ""))
                placed_blk = blk
                break
            if placed_blk is None:
                _diag = {b: round(eng.pool(b), 2) for b in sorted(mina)}
                _pl75 = [(r["歸戶"], r["目標塊"], r["配額G(㎡)"], r["增配面積(㎡)"])
                         for r in exit_rows if r.get("配額G(㎡)")]
                _e1 = {f"{g}@{b}": round(a2, 2) for (g, b), a2 in sorted(placed.items())
                       if a2 > 0.01}
                raise RuntimeError(
                    f"🔴 [{tag}] {gid}(a={q['a']:.2f}) 7-5 三塊(R4/R3/R5)皆無法落位——停機上呈｜"
                    f"池態={_diag}｜MinA={mina}｜7-5已落位={_pl75}｜"
                    f"E1/E2 a″帳={_e1}｜溢入={sorted({s[0] for s in spill_75})}｜"
                    f"unreach={ {k: round(v, 2) for k, v in unreach.items()} }")

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
            if GE > 0 and 2 * GE < MINA_QU:
                raise RuntimeError(f"🔴 [{tag}] ½ 判終態翻轉：{gid} 2×{GE:.2f}<114.07")
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

        # 整形後池複驗（三則＋無 S=0 殘留）
        pool_final = dict(poolE)
        for blk, npolys in new_polys_by_blk.items():
            bpoly = Polygon(cb_by[blk]["vertices"])
            if not bpoly.is_valid:
                bpoly = bpoly.buffer(0)
            au = unary_union(list(npolys.values())).buffer(0.001)
            pool_g = bpoly.difference(au)
            if not pool_g.is_valid:
                pool_g = pool_g.buffer(0)
            pieces = ([g for g in pool_g.geoms if g.area >= 1.0]
                      if pool_g.geom_type == "MultiPolygon"
                      else ([pool_g] if pool_g.area >= 1.0 else []))
            fl = (cad.get("front_lines") or {}).get(blk) or {}
            fseg = wf_f1._seg(fl)
            for g in pieces:
                if wf_f1._front_len_of(g, fseg, bpoly) < 0.5:
                    fm = (c["forced"] or {}).get(blk, {}) or {}
                    if fm.get("left_forced_offset") or fm.get("right_forced_offset"):
                        continue                     # forced 角落鎖定片（3.5m 情境豁免）
                    raise RuntimeError(f"🔴 [{tag}] E3 後 {blk} 仍有 S=0 池片 {g.area:.2f}㎡")
            newp = sum(g.area for g in pieces)
            if abs(newp - poolE[blk]) > 0.05 + 0.05:
                raise RuntimeError(f"🔴 [{tag}] E3 {blk} 池差 {newp - poolE[blk]:+.2f} >0.1（整形應池不變）")
            pool_final[blk] = newp
        mid = [l for l in pool_final if 0.5 < pool_final[l] < mina[l] - 0.05]
        if mid:
            raise RuntimeError(f"🔴 [{tag}] 終態池落 (0,MinA)：{ {l: round(pool_final[l],2) for l in mid} }——停機上呈")

        # ══ E4：終態全域斷言 ══
        flag_end = [k for k, r in E.items() if r["畸零地旗標"].strip()]
        if flag_end:
            raise RuntimeError(f"🔴 [{tag}] 終態殘餘畸零旗標：{flag_end}")
        e4_viol = []
        alloc_dirs = cad.get("alloc_dir_by_block", {}) or {}
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
            ad = ns["alloc_normal_axis"](alloc_dirs.get(blk))
            if ad is not None:
                cs = list(poly.exterior.coords)
                depth = (max(p[0] * ad[0] + p[1] * ad[1] for p in cs)
                         - min(p[0] * ad[0] + p[1] * ad[1] for p in cs))
                if depth < float(snap["global"]["法定最小深_m"]) - 0.05:
                    e4_viol.append(f"{k}: 深 {depth:.2f} < 最小深")
            g_ok = float(r["G(㎡)"]) >= mina[blk] - TOL
            if not g_ok:
                e4_viol.append(f"{k}: G={r['G(㎡)']} < MinA_{blk} 且不在增配/補償帳")
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
            "flags_end": 0, "pos_viol": [], "b1_ok": True,
            "med_dist": round(med, 1),
            "verdict_all_green": all("🔴" not in str(v["判定"]) for v in sgE["pool_diag"].values()),
        }
        out[tag] = {"conv_rows": conv_rows, "exit_rows": exit_rows, "g_tab": g_tab,
                    "pool_rows": pool_rows, "reshape_rows": reshape_rows,
                    "ledger_rows": ledger_rows, "anchors": anchors}
    return out


def _proj_order(ns, cad, parcels, blk):
    fl = (cad.get("front_lines") or {}).get(blk) or {}
    pib = [{"暫編地號": tp["暫編地號"], "polygon_coords": tp.get("polygon_coords")}
           for tp in parcels if tp["所屬街廓"] == blk and not tp.get("_is_ghost_sliver")]
    return [x["暫編地號"] for x in ns["_projection_order"](pib, fl.get("p1"), fl.get("p2"))]


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
    if side == "left":
        corner = p1.copy()
        dh = d_hat
        buf = (float(fo.get("left_corner_min_area", 0.0) or 0.0) / avg_depth
               if fo.get("left_forced_offset") and avg_depth > 0 else 0.0)
    else:
        proj = [float(np.dot(np.array([v[0] - p1[0], v[1] - p1[1]]), d_hat))
                for v in blkm["vertices"]]
        corner = p1 + max(proj) * d_hat
        dh = -d_hat
        buf = (float(fo.get("right_corner_min_area", 0.0) or 0.0) / avg_depth
               if fo.get("right_forced_offset") and avg_depth > 0 else 0.0)

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
    target_row, skipped = None, []
    for r in grp:
        if (float(r.get("S(m)", 0) or 0) > 0.01
                and float(r.get("宗地寬度(m)", 0) or 0) >= mw
                and r["暫編地號"] not in flagged):
            target_row = r
            break
        skipped.append(r["暫編地號"])
    if target_row is None:
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
        u = unary_union([a, b])
        if u.geom_type != "Polygon":
            u = u.buffer(0.0011).buffer(-0.0011)
        return u

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
