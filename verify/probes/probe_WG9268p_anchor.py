# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令二 `c0-5`：起算垂線之錨——現行 vs 幾何，及其重疊後果（**唯讀探針**）。

🔒 **唯讀**：只讀 `verify/out/got_G值_退縮{0m,3.5m}_partial.csv`（harness 落檔）
   與 `verify/out/probe_WG985_grouphead_*.log`（既有落檔·僅取 `S_req` 三格為外錨），
   ⛔ 寫入任何 tracked 檔、⛔ import 生產模組、⛔ 動 `app.py` 與 `verify/` 生產路徑。

【本器之存在理由（補令二 `§四-2` 逐字）】
   `probe_WG985_grouphead.py` 之 `A-4` shim **已停用**（`GB-157`）——其原錨模型
   （`w40.eval_lot` 之 `st[0]` ＝ 前一宗遠側界之 **FRONTLINE 截距**）與生產碼之錨
   （`corner_pt + cum_S·d̂` ＝ 起算點 ＋ **標稱 `S`**）為**不同之量**，其自我驗證閘
   （`n_old == n_now`）於現態不過。**新器之存在理由即在過此閘。**

【框之來源（逐項具名·⛔ 自擬者一律標明）】
  · `cut_coords → shapely.Polygon`（`is_valid` 否則 `buffer(0)`）
    ＝ **沿用** `probe_WG9265_coverage_account.py` 之逐字（⛔ 另寫第二份幾何原語）。
  · **宗序** ＝ 同一 `(情境,街廓,側)` 內以 `累積S(m)` 昇冪之 `0-based` 位次 ＝ **正典逐字**（`K-9-15 二`）。
  · `d̂` ＝ **FRONT_LINE 之單位向量**、`corner_pt` ＝ 其 `p1`
    （生產碼逐字 ＝ `app.py`〔`d_hat = _np_d.array([_dx_fl / _L_fl, _dy_fl / _L_fl])`〕，
     其上二列註解逐字「**FRONT_LINE 為 d_hat + corner_pt 之主來源**」）。
  · `allocation_dir` ＝ `rot90(f3_cad_alloc_dir)` ⇒ `_block_strip` 之 `n_hat` **∥ 地界線**
    （生產碼註解逐字）⇒ 本器之 `n̂` 取 **ALLOC 方向之法向**、`h(P) = dot(P, n̂)` 於 ∥ALLOC 線上為常數。
  · `s_錨_現行(j+1)` ＝ `累積S(j)` ＝ **生產碼之錨**
    （`baseline_pt = corner_pt + left_cum_S * d_hat`／`end_pt + right_cum_S * d_hat_rev`·二檔四處）。
  · `s_錨_幾何(j)` ＝ 宗 `j` 沿**帶軸框**之極值 ＝ 其遠側界離開街廓之點 ＝ `W-G.9-84` 之 `S_req`
    （**框乙**·⛔ 框甲）。
  · **平移之方向** ＝ `d̂`；平移 `δ` 使帶軸框座標增 `δ`。
  · `重疊` 之判準 ＝ 逐對 `p1.intersection(p2).area > TOL_OVL`（`1e-6`）＝ **自擬**
    （同 `probe_WG9265` 之 `Σarea − area(∪) > 1e-6` 之逐對形）。

🛑 **判準在否證對照**：人造相疊／相離矩形／**閘甲**（框之標定殘差）／**閘乙**（現行錨 ＝ `S-6` 覆蓋帳）／
   **閘丙**（`s_錨_幾何` ＝ 倉內既有落檔之 `S_req`·**外錨**）／**兩造對照**。
   任一不如預期 ⇒ **量測器紅、該次輸出⛔ 出艙（`rc ≠ 0`）**。
"""
import ast
import csv
import glob
import io
import math
import os
import re
import sys
from itertools import combinations

from shapely.geometry import Polygon
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(REPO, "verify", "out")

SCEN = [("0m", "got_G值_退縮0m_partial.csv"), ("3.5m", "got_G值_退縮3.5m_partial.csv")]
TOL_OVL = 1e-6
TOL_PARA = 1e-6
# 🔒 `TOL_FIT` 之由（⛔ 任意）：`累積S(m)` 於落檔為 **2dp** ⇒ 其捨入誤差上界 `0.005 m`；
#    取其 **2 倍**為殘差上界。⛔ 以「跑得過」回頭調之。
TOL_FIT = 0.010
TOL_CONSIST = 2e-3      # `|A·dot(d̂,n̂)| − 1` 之上界（同源於上開捨入）
TOL_SREQ = 0.02         # 閘丙：`s_錨_幾何` vs 倉內 `S_req` 之上界（公尺）
DP = 4                  # 「逐位相符」之位數（`S-6` 出艙為 4dp）

# 🔒 閘乙之靶（補令二 `§四-2` 逐字·來源 ＝ `S-6` 覆蓋帳之實測·**⛔ 本器所生**）
GATE_B_TARGET = {
    ("0m", "R2", "left"): [19.8142, 26.1624],
    ("3.5m", "R5", "left"): [56.8186],
}
SIDE_CN = {"left": "左", "right": "右"}


# ── 幾何原語（沿用 probe_WG9265 之逐字）──────────────────────────────
def poly(coords):
    p = Polygon(coords)
    if not p.is_valid:
        p = p.buffer(0)
    return p


def parse_coords(s):
    if not s or not s.strip():
        return None
    try:
        v = ast.literal_eval(s)
    except Exception:                                               # noqa: BLE001
        return None
    return v if v and len(v) >= 3 else None


def load(fn):
    path = os.path.join(OUT, fn)
    with io.open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f)), os.path.getsize(path)


def controls():
    ok = True
    a = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    b = poly([(1, 0), (3, 0), (3, 1), (1, 1)])
    v = (a.area + b.area) - unary_union([a, b]).area
    good = abs(v - 1.0) < 1e-9
    print("  [必紅] 人造相疊矩形 Σ−∪ ＝ %.10f（須 ＝ 1.0）%s" % (v, "✅" if good else "🔴"))
    ok &= good
    c = poly([(0, 0), (2, 0), (2, 1), (0, 1)])
    d = poly([(5, 0), (6, 0), (6, 1), (5, 1)])
    v2 = (c.area + d.area) - unary_union([c, d]).area
    good2 = abs(v2) < 1e-12
    print("  [必綠] 人造相離矩形 Σ−∪ ＝ %.10f（須 ＝ 0.0）%s" % (v2, "✅" if good2 else "🔴"))
    return ok and good2


# ── 向量小工具 ────────────────────────────────────────────────────
def _u(dx, dy):
    L = math.hypot(dx, dy)
    return (dx / L, dy / L) if L > 1e-12 else None


def _edges(pts):
    out = []
    for i in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        u = _u(x2 - x1, y2 - y1)
        if u:
            out.append((pts[i], pts[i + 1], u, math.hypot(x2 - x1, y2 - y1)))
    return out


def _ang180(u):
    return math.degrees(math.atan2(u[1], u[0])) % 180.0


def _para(u1, u2):
    return abs(u1[0] * u2[1] - u1[1] * u2[0]) < TOL_PARA


# ── 框之標定（自我驗證閘甲）────────────────────────────────────────
def calibrate(lots):
    """回 (u_alloc, d_hat, A, B, diag)。`strip(P) = A·dot(P, n̂) + B`。

    🔒 **標定之受詞 ＝ 帶軸機自身之保證**（⛔ 自擬）：相鄰二宗之**共用 ∥ALLOC 界線**
       即生產碼之錨所在之線，其 `strip` ＝ `累積S(j)`。
    🩸 **⛔ 以「各宗臨街段之端點」標定**——街角第 1 宗之範圍由 `_build_corner_range_v3` 造，
       其實際臨街段⛔ 等於其標稱 `[累積S − S, 累積S]`（實測 `0m·R2·left`：宗 `0` `t∈[0,4.0554]`
       而宗 `2` `t∈[1.989,2.636]`·**內含⛔ 相接**）⇒ 該式之殘差達 `10.75 m`。
    """
    votes, shared = {}, []
    for i, (a, b) in enumerate(zip(lots, lots[1:])):
        best = None
        for p1, _q1, u1, L1 in _edges(a["pts"]):
            for p2, _q2, u2, L2 in _edges(b["pts"]):
                if not _para(u1, u2):
                    continue
                if abs((p2[0] - p1[0]) * u1[1] - (p2[1] - p1[1]) * u1[0]) > 1e-6:
                    continue
                sc = min(L1, L2)
                if best is None or sc > best[0]:
                    best = (sc, p1, u1)
        if best:
            k = round(_ang180(best[2]), 4)
            votes[k] = votes.get(k, 0.0) + best[0]
            shared.append((i, best[1], best[2]))
    if not votes:
        return None, None, None, None, {"why": "⛔ 偵得任何共用邊（宗數 %d）" % len(lots)}
    a_alloc = max(votes.items(), key=lambda kv: kv[1])[0]
    u_alloc = (math.cos(math.radians(a_alloc)), math.sin(math.radians(a_alloc)))
    n_hat = (-u_alloc[1], u_alloc[0])

    def h(P):
        return P[0] * n_hat[0] + P[1] * n_hat[1]

    known = [(h(p), lots[i]["cum"]) for i, p, u in shared if _para(u, u_alloc)]
    slopes = []
    for lt in lots:
        # 🩸 街角第 1 宗之範圍由 `_build_corner_range_v3` 造 ⇒ 其二條 ∥ALLOC 邊
        #    ⛔ 為「標稱 `S` 之二界」（實測 `0m·R1·right` `r_sl ＝ 0.4015 m`）⇒ 排除之。
        if lt["ord"] == "街角第1宗":
            continue
        hs = [h(p) for p, _q, u, _L in _edges(lt["pts"]) if _para(u, u_alloc)]
        if len(hs) >= 2 and lt["S"] > 1e-9:
            dh = max(hs) - min(hs)
            if dh > 1e-9:
                slopes.append((dh, lt["S"]))

    if not known:
        return u_alloc, None, None, None, {
            "why": "⛔ 標定：⛔ 共用 ∥ALLOC 界線（已知點 0／斜率約束 %d）" % len(slopes)}

    # 🔒 `A` 由**候選 FRONTLINE 方向**定：`A·dot(v̂, n̂) ＝ ±1` **恆成立**（構造保證）
    #    ⇒ `consist` ⛔ 再為判別者；判別者改為**殘差**（公尺·⛔ 無因次）。
    cands = {}
    for lt in lots:
        for _p, _q, u, L in _edges(lt["pts"]):
            if _para(u, u_alloc):
                continue
            k = round(_ang180(u), 4)
            cands[k] = cands.get(k, 0.0) + L
    if not cands:
        return u_alloc, None, None, None, {"why": "⛔ 偵得任何⛔ ∥ALLOC 之邊方向"}

    def fit_for(a_deg, sign):
        v = (math.cos(math.radians(a_deg)), math.sin(math.radians(a_deg)))
        dn = v[0] * n_hat[0] + v[1] * n_hat[1]
        if abs(dn) < 1e-9:
            return None
        Av = sign / dn
        Bv = sum(y - Av * x for x, y in known) / len(known)
        r_pt = max(abs(Av * x + Bv - y) for x, y in known)
        r_sl = max([abs(abs(Av) * dh - S) for dh, S in slopes], default=0.0)
        # 🔒 次序約束：**每宗之 `max strip` 須 ≥ 其 `累積S`**（其遠側界至少及於標稱終點）。
        #    ⇒ `A` 取錯符號者（`strip` 對已知點鏡射）於此必然巨大。
        r_ord = 0.0
        for lt in lots:
            mx = max(Av * h(Pv) + Bv for Pv in lt["pts"])
            r_ord = max(r_ord, max(0.0, lt["cum"] - mx))
        return {"A": Av, "B": Bv, "v": v, "a": a_deg, "r_pt": r_pt, "r_sl": r_sl,
                "r_ord": r_ord, "res": max(r_pt, r_sl, r_ord)}

    fits = [f for a_deg in cands for s in (1.0, -1.0)
            for f in [fit_for(a_deg, s)] if f]
    fits.sort(key=lambda f: f["res"])
    if not fits:
        return u_alloc, None, None, None, {"why": "🔴 全部候選皆退化"}
    best = fits[0]
    second = next((f for f in fits[1:] if round(f["a"], 4) != round(best["a"], 4)), None)
    A, B, d_hat = best["A"], best["B"], best["v"]
    diag = {
        "a_alloc": a_alloc, "a_front": best["a"], "n_pts": len(known),
        "n_slope": len(slopes), "mode": "候選方向＋共用界線＋斜率約束",
        "res_max": best["res"], "r_pt": best["r_pt"], "r_sl": best["r_sl"],
        "r_ord": best["r_ord"],
        "A": A, "B": B,
        "consist": A * (d_hat[0] * n_hat[0] + d_hat[1] * n_hat[1]),
        "d_err1": best["res"], "d_err2": second["res"] if second else float("inf"),
        "why": None,
    }
    return u_alloc, d_hat, A, B, diag


# ── 閘丙之外錨：倉內既有落檔之 `S_req`（⛔ 本器所生）────────────────
def read_sreq():
    """自 `probe_WG985_grouphead_*.log` 之 `A-4` 表讀 `S_req`（僅 `0m`·⛔ 引其他數）。

    🔒 補令二 `§三-3` 逐字：**`S_req` 本身未動**——其於 `67cd1a4` 與 `bf1d92f` 二落檔逐位相同
       ⇒ **⛔ 在作廢之列**（作廢者係 `5／5`／`3／5`／`3／3` 與由 `0.2163` 導出之差）。
    """
    out, srcs = {}, []
    pat = re.compile(r"^\s{2}(R\d)\s+([左右])\s+(\d+)\s+"
                     r"([-\d.eE+]+)\s+([-\d.eE+]+)\s+([-\d.eE+naN]+)\s")
    for p in sorted(glob.glob(os.path.join(OUT, "probe_WG985_grouphead_*.log"))):
        try:
            txt = io.open(p, encoding="utf-8").read()
        except Exception:                                           # noqa: BLE001
            continue
        seg = txt.split("【F／A-4】")
        if len(seg) < 2:
            continue
        srcs.append(os.path.basename(p))
        for ln in seg[1].split("\n"):
            m = pat.match(ln)
            if not m:
                continue
            blk, side, j, _lo, _ln2, sreq = m.groups()
            try:
                v = float(sreq)
            except ValueError:
                continue
            if math.isfinite(v):
                out.setdefault((os.path.basename(p), blk, side, int(j)), v)
    return out, srcs


def pairs_of(polys):
    out = []
    for (i, p1), (j, p2) in combinations(list(enumerate(polys)), 2):
        a = p1.intersection(p2).area
        if a > TOL_OVL:
            out.append((i, j, a))
    return out


def shift(pts, vec):
    return [(x + vec[0], y + vec[1]) for x, y in pts]


def main():                                                         # noqa: C901
    W = 132
    print("=" * W)
    print("【W-G.9-268′ 補令二 c0-5】起算垂線之錨：現行 vs 幾何　（唯讀探針·⛔ 動生產碼）")
    print("=" * W)
    print()
    print("── 否證對照（幾何原語·人造·先跑·不如預期即 abort）──")
    if not controls():
        print("🔴 量測器紅 ⇒ 本次輸出⛔ 出艙")
        return 2
    print()

    hard_fail = []
    all_groups = []
    for tag, fn in SCEN:
        rows, nbytes = load(fn)
        print("【情境 %s】落檔 %s／%d B／%d 資料列" % (tag, fn, nbytes, len(rows)))
        groups = {}
        for r in rows:
            c = parse_coords(r.get("cut_coords"))
            if c is None:
                continue
            k = (tag, (r.get("所屬街廓") or "").strip(),
                 (r.get("推進側別") or "").strip())
            groups.setdefault(k, []).append({
                "row": r, "pts": [(float(x), float(y)) for x, y in c],
                "cum": float(r.get("累積S(m)") or 0), "S": float(r.get("S(m)") or 0),
                "id": (r.get("暫編地號") or "").strip(),
                "ord": (r.get("驗_宗序") or "").strip(),
            })
        for k in sorted(groups):
            lots = sorted(groups[k], key=lambda t: t["cum"])
            for lt in lots:
                lt["poly"] = poly(lt["pts"])
            all_groups.append((k, lots))
    print("  組數（母體基數）＝ %d" % len(all_groups))
    print()

    # ── 【一】框之標定 ＋ 閘甲 ────────────────────────────────────
    print("=" * W)
    print("【一】框之標定 ＋ 🛑 **閘甲**（殘差 ≤ %.3f m·⛔ 無因次）" % TOL_FIT)
    print("=" * W)
    print("  %-22s %5s %9s %9s %7s %9s %9s %9s %9s %9s %s"
          % ("組", "宗數", "ALLOC°", "FRONT°", "點/斜", "r_pt(m)", "r_sl(m)",
             "r_ord(m)", "殘差max", "次佳", "判"))
    cal = {}
    for k, lots in all_groups:
        u_alloc, d_hat, A, B, diag = calibrate(lots)
        cal[k] = (u_alloc, d_hat, A, B, diag)
        name = "%s·%s·%s" % k
        if A is None or d_hat is None:
            print("  %-22s %5d  ⚠️ ⛔ 可標定：%s" % (name, len(lots), diag["why"]))
            continue
        okg = diag["res_max"] <= TOL_FIT
        print("  %-22s %5d %9.4f %9.4f %3d/%-3d %9.2e %9.2e %9.2e %9.2e %9.2e %s"
              % (name, len(lots), diag["a_alloc"], diag["a_front"], diag["n_pts"],
                 diag["n_slope"], diag["r_pt"], diag["r_sl"], diag["r_ord"],
                 diag["res_max"], diag["d_err2"], "✅" if okg else "🔴"))
        if not okg:
            hard_fail.append("閘甲：%s（殘差 %.3e／一致性 %.9f）"
                             % (name, diag["res_max"], diag["consist"]))
    print("  🔒 `A` 由候選方向定（`A·dot(d̂,n̂) ＝ ±1` **構造保證**）⇒ `consist` 恆 ±1、⛔ 為判別者；"
          "判別者 ＝ **殘差**（`r_pt` ＝ 共用界線／`r_sl` ＝ 斜率約束·皆以公尺計）。")
    print("  🔒 `TOL_FIT ＝ %.3f m` 之由：`累積S(m)`／`S(m)` 於落檔為 **2dp** ⇒ 捨入上界 `0.005 m`，取其 2 倍。"
          % TOL_FIT)
    print("  🩸 `d誤2`（次佳候選之殘差）係**診斷**：FRONTLINE 與 BASELINE 夾角僅 `~0.56°` ⇒ 二者同量級；"
          "`d̂` 之選擇只影響平移之橫向分量（`δ×sin(0.56°)` ≈ `δ×0.0098`），"
          "**⛔ 影響帶軸座標之位移量**（其恆為 `δ`）。")

    # ── 【二】逐 (組, j) ─────────────────────────────────────────
    print()
    print("=" * W)
    print("【二】逐 `(情境, 街廓, 側, j)`：錨之現行／幾何／`δ` ＋ 重疊")
    print("=" * W)
    print("  %-18s %-3s %-14s %11s %11s %10s %-22s %-22s"
          % ("組", "j", "暫編地號", "s_錨_現行", "s_錨_幾何", "δ(m)", "現況重疊", "新錨後重疊"))
    n_pop = n_pr = 0
    delta_all, geo_all = [], {}
    for k, lots in all_groups:
        u_alloc, d_hat, A, B, diag = cal[k]
        name = "%s·%s·%s" % k
        pr_now = pairs_of([lt["poly"] for lt in lots])
        if k[2] not in ("left", "right"):
            # 🩸 抵費地組：`累積S(m)` 恆 `0` ⇒ ⛔ 具推進語意 ⇒ ⛔ 適用本器之錨語意。
            print("  %-18s %-3s %-14s %11s %11s %10s %-22s %-22s"
                  % (name, "—", "（抵費地）", "—", "—", "—",
                     "%d 對" % len(pr_now), "⛔ 適用（非配地鏈）"))
            continue
        n_pop += max(0, len(lots) - 1)
        if A is None or d_hat is None:
            continue
        n_hat = (-u_alloc[1], u_alloc[0])

        def strip(P, _A=A, _B=B, _n=n_hat):
            return _A * (P[0] * _n[0] + P[1] * _n[1]) + _B

        sgn = 1.0 if diag["consist"] > 0 else -1.0
        adv = (d_hat[0] * sgn, d_hat[1] * sgn)
        for j in range(len(lots) - 1):
            s_now = lots[j]["cum"]
            s_geo = max(strip(P) for P in lots[j]["pts"])
            d = s_geo - s_now
            delta_all.append((k, j, d))
            geo_all[(k, j)] = s_geo
            moved = [poly(shift(lt["pts"], (adv[0] * d, adv[1] * d))) if i > j
                     else lt["poly"] for i, lt in enumerate(lots)]
            pr_new = pairs_of(moved)
            f = lambda pr: ("%d 對｜%s" % (len(pr), "／".join("%d×%d %.4f" % p for p in pr))
                            if pr else "0 對")
            print("  %-18s %-3d %-14s %11.4f %11.4f %10.4f %-22s %-22s"
                  % (name, j, lots[j]["id"], s_now, s_geo, d, f(pr_now), f(pr_new)))
            n_pr += 1
    print("  POPULATION=%d PRINTED=%d SUPPRESSED=%d  # 逐 (組,j)（⛔ 可標定之組已具名於【一】）"
          % (n_pop, n_pr, n_pop - n_pr))

    # ── 【三】閘乙 ───────────────────────────────────────────────
    print()
    print("=" * W)
    print("【三】🛑 **閘乙**：以**現行錨**（`δ=0`）重建之重疊 ＝ `S-6` 覆蓋帳之實測（對數 ⋀ 逐對面積·%ddp）" % DP)
    print("=" * W)
    print("  🔒 靶之來源 ＝ 補令二 `§四-2` 逐字（其源 ＝ `S-6` 覆蓋帳·**⛔ 本器所生**）")
    print("  🩸 **本閘之界（照實）**：`S-6` 與本器讀**同一落檔**；其獨立性在**算法**"
          "（`Σarea − area(∪)` vs **逐對** `intersection`），⛔ 在資料來源。")
    print("  %-22s %6s %-32s %-32s %s" % ("組", "宗數", "本器（逐對·%ddp）" % DP, "S-6 之靶", "判"))
    for k, lots in all_groups:
        pr = pairs_of([lt["poly"] for lt in lots])
        got = sorted(round(a, DP) for _i, _j, a in pr)
        want = sorted(round(a, DP) for a in GATE_B_TARGET.get(k, []))
        ok = (got == want)
        print("  %-22s %6d %-32s %-32s %s"
              % ("%s·%s·%s" % k, len(lots), str(got), str(want), "✅" if ok else "🔴"))
        if not ok:
            hard_fail.append("閘乙：%s 本器 %s ≠ 靶 %s" % ("%s·%s·%s" % k, got, want))

    # ── 【四】閘丙：`s_錨_幾何` vs 倉內 `S_req`（外錨）──────────────
    print()
    print("=" * W)
    print("【四】🛑 **閘丙**（外錨）：`s_錨_幾何` ＝ 倉內既有落檔之 `S_req`（|Δ| ≤ %.2f m）" % TOL_SREQ)
    print("=" * W)
    sreq, srcs = read_sreq()
    print("  來源落檔（⛔ 本器所生·⛔ 本批重跑）＝ %s" % (srcs or "🔴 無"))
    print("  🔒 補令二 `§三-3` 逐字：**`S_req` 本身未動**（二落檔逐位相同）⇒ ⛔ 在作廢之列")
    print("  %-14s %-22s %-3s %13s %13s %11s %s"
          % ("落檔", "組", "j", "本器 s_錨_幾何", "倉內 S_req", "|Δ|(m)", "判"))
    n_c = 0
    for (src, blk, side_cn, j), v in sorted(sreq.items()):
        side = "left" if side_cn == "左" else "right"
        kk = (("0m", blk, side), j)
        if kk[0] not in [g[0] for g in all_groups] or kk not in geo_all:
            continue
        got = geo_all[kk]
        dv = abs(got - v)
        ok = dv <= TOL_SREQ
        n_c += 1
        print("  %-14s %-22s %-3d %13.4f %13.4f %11.2e %s"
              % (src[-11:-4], "%s·%s·%s" % kk[0], j, got, v, dv, "✅" if ok else "🔴"))
        if not ok:
            hard_fail.append("閘丙：%s j=%d 本器 %.4f vs 倉內 S_req %.4f（Δ %.4f）"
                             % ("%s·%s·%s" % kk[0], j, got, v, dv))
    if n_c == 0:
        hard_fail.append("閘丙之判定集為空 ⇒ loud 拒測（⛔ 靜默綠）")
        print("  🔴 **判定集為空** ⇒ loud 拒測（⛔ 靜默綠）")
    else:
        print("  判定集基數 ＝ %d" % n_c)
        # 判別力：對同一組注入 +1 m 之偏移，本閘須轉紅
        (src0, blk0, sc0, j0), v0 = sorted(sreq.items())[0]
        s0 = "left" if sc0 == "左" else "right"
        if (("0m", blk0, s0), j0) in geo_all:
            g0 = geo_all[(("0m", blk0, s0), j0)]
            print("  🔑 **判別力**（人造·⛔ 動任何檔）：對 `%s·%s·%s j=%d` 之本器值注入 `+1.0 m`"
                  " ⇒ |Δ| ＝ %.4f > %.2f ⇒ **須紅** %s"
                  % ("0m", blk0, s0, j0, abs(g0 + 1.0 - v0), TOL_SREQ,
                     "✅" if abs(g0 + 1.0 - v0) > TOL_SREQ else "🔴"))

    # ── 【五】兩造對照 ───────────────────────────────────────────
    print()
    print("=" * W)
    print("【五】兩造對照（自證⛔ 恆綠亦⛔ 恆紅）")
    print("  🔒 **母體之界定**（⛔ 全掃 `j`）：限**該平移能波及重疊對**者——"
          "∃ 重疊對 `(a, b)` 使 `a ≤ j < b`。")
    print("  🩸 **由**：平移只動 `j+1..n`；若重疊對之二端**同在** `j+1..n`（或同在 `0..j`），"
          "其相對位置⛔ 變 ⇒ 陰性必等於現況 ⇒ **偽紅**（本器首版即如此·自捕）。")
    print("=" * W)
    DPOS = 2.0
    print("  %-22s %-3s %-20s %-20s %-20s %s"
          % ("組", "j", "陽性（錨回移 %.1fm）" % DPOS, "現況（δ=0）", "陰性（錨移至幾何）", "判"))
    n_disc = 0
    for k, lots in all_groups:
        u_alloc, d_hat, A, B, diag = cal[k]
        if A is None or d_hat is None:
            continue
        pr0 = pairs_of([lt["poly"] for lt in lots])
        if not pr0:
            continue
        span_j = sorted({jj for (a, b, _ar) in pr0 for jj in range(a, b)})
        n_hat = (-u_alloc[1], u_alloc[0])

        def strip(P, _A=A, _B=B, _n=n_hat):
            return _A * (P[0] * _n[0] + P[1] * _n[1]) + _B

        sgn = 1.0 if diag["consist"] > 0 else -1.0
        adv = (d_hat[0] * sgn, d_hat[1] * sgn)
        for j in span_j:
            d = max(strip(P) for P in lots[j]["pts"]) - lots[j]["cum"]
            if d <= 0:
                continue

            def at(delta, _j=j, _lots=lots, _adv=adv):
                mv = [poly(shift(lt["pts"], (_adv[0] * delta, _adv[1] * delta)))
                      if i > _j else lt["poly"] for i, lt in enumerate(_lots)]
                p = pairs_of(mv)
                return len(p), sum(a for _a, _b, a in p)

            cp, ap = at(-DPOS)
            c0, a0 = at(0.0)
            cn, an = at(d)
            same = abs(ap - an) < 1e-12
            good = (ap > a0 + 1e-9) and (an < a0 - 1e-9) and not same
            n_disc += 1
            print("  %-22s %-3d %-20s %-20s %-20s %s"
                  % ("%s·%s·%s" % k, j, "%d 對 Σ%.4f" % (cp, ap),
                     "%d 對 Σ%.4f" % (c0, a0), "%d 對 Σ%.4f" % (cn, an),
                     "✅" if good else "🔴"))
            if same:
                hard_fail.append("兩造同值：%s j=%d ⇒ 器無鑑別力" % ("%s·%s·%s" % k, j))
            elif not good:
                hard_fail.append("兩造未如期：%s j=%d（陽 %.4f／現 %.4f／陰 %.4f）"
                                 % ("%s·%s·%s" % k, j, ap, a0, an))
    if n_disc == 0:
        hard_fail.append("兩造對照之判定集為空 ⇒ loud 拒測（⛔ 靜默綠）")
        print("  🔴 **判定集為空** ⇒ loud 拒測")
    else:
        print("  判定集基數 ＝ %d" % n_disc)

    # ── 【六】新靶 ───────────────────────────────────────────────
    print()
    print("=" * W)
    print("【六】🔴 **新靶**：以幾何終點為錨（**逐 j 累積套用**）後，全部可達組之重疊")
    print("=" * W)
    print("  %-22s %6s %-28s %-28s %s"
          % ("組", "宗數", "現況（對數｜Σ面積）", "新錨累積後（對數｜Σ面積）", "判"))
    tgt_ok = True
    for k, lots in all_groups:
        u_alloc, d_hat, A, B, diag = cal[k]
        pr_now = pairs_of([lt["poly"] for lt in lots])
        s_now = sum(a for _a, _b, a in pr_now)
        name = "%s·%s·%s" % k
        if k[2] not in ("left", "right") or A is None or d_hat is None:
            why = ("⛔ 適用（非配地鏈）" if k[2] not in ("left", "right")
                   else "⛔ 可標定")
            print("  %-22s %6d %-28s %-28s %s"
                  % (name, len(lots), "%d 對｜%.4f" % (len(pr_now), s_now),
                     why, "⚠️" if pr_now else "—（現況本即 0）"))
            if pr_now:
                tgt_ok = False
                hard_fail.append("新靶：%s %s 而現況有重疊" % (name, why))
            continue
        n_hat = (-u_alloc[1], u_alloc[0])

        def strip(P, _A=A, _B=B, _n=n_hat):
            return _A * (P[0] * _n[0] + P[1] * _n[1]) + _B

        sgn = 1.0 if diag["consist"] > 0 else -1.0
        adv = (d_hat[0] * sgn, d_hat[1] * sgn)
        cur = [list(lt["pts"]) for lt in lots]
        for j in range(len(lots) - 1):
            d = max(strip(P) for P in cur[j]) - min(strip(P) for P in cur[j + 1])
            if d <= 0:
                continue
            for i in range(j + 1, len(cur)):
                cur[i] = shift(cur[i], (adv[0] * d, adv[1] * d))
        pr_new = pairs_of([poly(c) for c in cur])
        s_new = sum(a for _a, _b, a in pr_new)
        ok = (len(pr_new) == 0)
        print("  %-22s %6d %-28s %-28s %s"
              % (name, len(lots), "%d 對｜%.4f" % (len(pr_now), s_now),
                 "%d 對｜%.4f" % (len(pr_new), s_new), "✅" if ok else "🔴"))
        if not ok:
            tgt_ok = False
            hard_fail.append("新靶：%s 新錨後仍有 %d 對（Σ %.4f）" % (name, len(pr_new), s_new))

    # ── 【七】δ 之彙總 ──────────────────────────────────────────
    print()
    print("=" * W)
    print("【七】`δ` 之彙總（＝ 原單 `§四` 差異表量級之來源·**帶號合計與絕對值合計並列**）")
    print("=" * W)
    if delta_all:
        ds = [d for _k, _j, d in delta_all]
        print("  🔒 **母體 ＝ 配地鏈**（`推進側別 ∈ {left, right}`）之 `(組, j)`；"
              "**抵費地組⛔ 在母體內**（其 `累積S` 恆 `0`·⛔ 具推進語意·已於【二】逐組具名）。")
        print("  母體基數 ＝ %d 個 `(組, j)`" % len(ds))
        print("  **Σδ（帶號）＝ %+.4f m** ／ **Σ|δ| ＝ %.4f m**"
              % (sum(ds), sum(abs(x) for x in ds)))
        print("  min ＝ %+.4f ／ max ＝ %+.4f ／ 中位 ＝ %+.4f"
              % (min(ds), max(ds), sorted(ds)[len(ds) // 2]))
        print("  δ > 0 ＝ %d ／ |δ| ≤ 1e-9 ＝ %d ／ δ < 0 ＝ %d"
              % (sum(1 for x in ds if x > 1e-9), sum(1 for x in ds if abs(x) <= 1e-9),
                 sum(1 for x in ds if x < -1e-9)))
        for sd in ("left", "right"):
            v = [d for kk, _j, d in delta_all if kk[2] == sd]
            if v:
                print("     %-6s n ＝ %-3d Σδ ＝ %+10.4f ／ Σ|δ| ＝ %10.4f ／ |δ| 最大 ＝ %+.4f"
                      % (sd, len(v), sum(v), sum(abs(x) for x in v), max(v, key=abs)))
        print()
        big = [(kk, jj, d) for kk, jj, d in delta_all if abs(d) > 0.01]
        print("  ── `|δ| > 0.01 m` 之逐列（%d 列／%d·**⛔ 只出合計**）──" % (len(big), len(ds)))
        for kk, jj, d in sorted(big, key=lambda x: -abs(x[2])):
            print("     %-22s j=%-2d δ ＝ %+10.4f m" % ("%s·%s·%s" % kk, jj, d))
        print("  🔒 **其餘 %d 列之 `|δ| ≤ 0.01 m`** ＝ `累積S(m)` 之 2dp 捨入量級（`0.005 m`）"
              "⇒ 🔴 **錨之偏差實質上集中於 `j = 0`（街角第 1 宗）**。" % (len(ds) - len(big)))
        print()
        print("  ── 現況有重疊之組，其 `δ`（逐格）──")
        for k, j, d in delta_all:
            if k in GATE_B_TARGET:
                print("     %-22s j=%d  δ ＝ %+.4f m" % ("%s·%s·%s" % k, j, d))
    print()

    print("=" * W)
    if hard_fail:
        print("🔴 **閘紅 ＝ %d 項** ⇒ 本次輸出⛔ 出艙（`rc ≠ 0`）：" % len(hard_fail))
        for x in hard_fail:
            print("   · %s" % x)
        print("=" * W)
        return 3
    print("✅ 全閘綠：否證對照 ⋀ 閘甲 ⋀ 閘乙 ⋀ 閘丙 ⋀ 兩造對照 ⋀ 新靶 ＝ %s"
          % ("全部可達組之重疊皆為 0" if tgt_ok else "🔴"))
    print("=" * W)
    return 0


if __name__ == "__main__":
    sys.exit(main())
