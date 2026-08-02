# -*- coding: utf-8 -*-
"""V6_1.dxf 驗收 — **舊/新 DXF 之幾何集合比對**（只驗不改·不進判定鏈）。

## 為什麼禁用 handle（**本批血訓·入 PROVENANCE**）

DXF **重存後 entity handle 會全部重編** ⇒ 逐 handle 比對會得出**全假差異**
（本案實測：275 個「差異」全為假）。
⇒ **比對圖檔一律用幾何集合**（座標四捨五入後之 multiset），**不得用 handle**。

## 修圖之內容（KL·2026-08-02）

成因（段五 (G) 已定讞）：R4／RD3 共用頂點 `(310582.658400, 2651871.934270)`
位於 FRONT_LINE 外側 `0.014826m`，**CAD 圖面既有**。
KL 之修法：**移動 FRONT_LINE／SIDE_LINE 端點使其通過該街廓頂點**
——**非**移動街廓頂點（街廓多邊形係**地籍事實**，街線係**規劃線**；令線就地籍）。

## 六項驗收

1. 各圖層實體數：舊新一致
2. BLOCK POLYLINE 幾何集合：12 個完全相同（**地籍未動**）
3. BASELINE／ALLOC_LINE／CENTERLINE／CADASTRAL_BOUND：完全相同
4. FRONT_LINE／SIDE_LINE 端點變動：逐條列出 舊→新 與位移量
5. **街廓頂點對 FRONT_LINE 之最大偏差**：舊 `0.014826m` → 新應 `≤1e-5m`
6. **FRONT_LINE 端點 ↔ SIDE_LINE 端點**：`<0.5m` 之組合數與其最大距
   （街角理論交點是否被拆開）

⚠️ 第 6 項刻意採**端點對端點**之局部判準（只看 `<0.5m` 之組合）——
**不**採「無限直線交點 vs 端點」，因後者會把**相隔上百公尺之非相鄰線**配成一組
而得出假警報（KL 第一版即踩此坑）。**診斷端點重合，不可用會把非相鄰線配對之方法。**

## 重跑
    python verify/tools/verify_dxf_v6_1.py [舊dxf] [新dxf]
"""
import hashlib
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)

import ezdxf                                            # noqa: E402

OLD = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "data", "V6.dxf")
NEW = sys.argv[2] if len(sys.argv) > 2 else os.path.join(REPO, "data", "V6_1.dxf")

Q = 6           # 座標比對之四捨五入位數（1e-6 m ＝ µm·遠低於 DXF 量化步長 1e-5）
EPS_ON = 0.05   # 「貼線」之收案半徑（僅為**列舉母體**之用·非判準閾）
EPS_NEAR = 0.5  # 第 6 項之局部配對半徑（只看相鄰之端點對）


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def load(path):
    doc = ezdxf.readfile(path, encoding="cp950")
    ents = {}
    for e in doc.modelspace():
        lay, typ = e.dxf.layer, e.dxftype()
        ents.setdefault((lay, typ), []).append(e)
    return doc, ents


def pts_of(e):
    """實體之幾何（座標 tuple）——**不含 handle、不含樣式屬性**。"""
    t = e.dxftype()
    if t == "LINE":
        return ((round(e.dxf.start[0], Q), round(e.dxf.start[1], Q)),
                (round(e.dxf.end[0], Q), round(e.dxf.end[1], Q)))
    if t == "POLYLINE":
        return tuple((round(v.dxf.location[0], Q), round(v.dxf.location[1], Q))
                     for v in e.vertices)
    if t == "LWPOLYLINE":
        return tuple((round(p[0], Q), round(p[1], Q)) for p in e.get_points())
    if t == "TEXT":
        return ((round(e.dxf.insert[0], Q), round(e.dxf.insert[1], Q)),
                str(e.dxf.text))
    if t == "INSERT":
        return ((round(e.dxf.insert[0], Q), round(e.dxf.insert[1], Q)),
                str(e.dxf.name))
    return ("?" + t,)


def geoms(ents, layer, typ=None):
    out = []
    for (lay, tp), lst in ents.items():
        if lay != layer or (typ and tp != typ):
            continue
        out.extend(pts_of(e) for e in lst)
    return out


def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def perp(pt, s, t):
    """點至 (s,t) **無限直線**之垂距 ＋ 其沿線之參數 u（0..1 為段內）。"""
    vx, vy = t[0] - s[0], t[1] - s[1]
    L2 = vx * vx + vy * vy
    if L2 <= 0:
        return float("inf"), 0.0
    u = ((pt[0] - s[0]) * vx + (pt[1] - s[1]) * vy) / L2
    px, py = s[0] + u * vx, s[1] + u * vy
    return dist(pt, (px, py)), u


def main():
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    L = []

    def P(x=""):
        L.append(x)
        print(x)

    P("=" * 108)
    P("【V6_1.dxf 驗收】舊/新 DXF **幾何集合**比對（⛔ 禁用 handle·重存後全部重編）")
    P("=" * 108)
    P(f"舊 = {os.path.relpath(OLD, REPO) if OLD.startswith(REPO) else OLD}")
    P(f"    md5 = {md5(OLD)}   bytes = {os.path.getsize(OLD)}")
    P(f"新 = {os.path.relpath(NEW, REPO) if NEW.startswith(REPO) else NEW}")
    P(f"    md5 = {md5(NEW)}   bytes = {os.path.getsize(NEW)}")

    _do, eo = load(OLD)
    _dn, en = load(NEW)

    # ── (1) 各圖層實體數 ────────────────────────────────────────────────
    P()
    P("【1】各圖層×型別 實體數")
    P("-" * 108)
    keys = sorted(set(eo) | set(en))
    ok1 = True
    P(f"  {'圖層':22}{'型別':14}{'舊':>6}{'新':>6}  判")
    for k in keys:
        a, b = len(eo.get(k, [])), len(en.get(k, []))
        same = a == b
        ok1 &= same
        P(f"  {k[0]:22}{k[1]:14}{a:>6}{b:>6}  {'✅' if same else '🔴'}")
    P(f"  ⇒ {'✅ 舊新一致' if ok1 else '🔴 有差異'}")

    # ── (2)(3) 幾何集合完全相同之圖層 ──────────────────────────────────
    P()
    P("【2】【3】應**完全相同**之圖層（幾何 multiset 比對）")
    P("-" * 108)
    ok23 = True
    for lay in ("BLOCK", "BASELINE", "ALLOC_LINE", "CENTERLINE", "CADASTRAL_BOUND"):
        for typ in sorted({k[1] for k in keys if k[0] == lay}):
            go = sorted(geoms(eo, lay, typ))
            gn = sorted(geoms(en, lay, typ))
            same = go == gn
            ok23 &= same
            _extra = ""
            if not same:
                _only_o = [g for g in go if g not in gn]
                _only_n = [g for g in gn if g not in go]
                _extra = f"  舊獨有 {len(_only_o)}／新獨有 {len(_only_n)}"
            P(f"  {lay:20}{typ:14}n={len(go):>4}  "
              f"{'✅ 完全相同' if same else '🔴 有差異'}{_extra}")
    P(f"  ⇒ {'✅ 地籍與其餘規劃線未動' if ok23 else '🔴 有非預期變動'}")

    # ── (4) FRONT_LINE／SIDE_LINE 之端點變動 ───────────────────────────
    P()
    P("【4】FRONT_LINE／SIDE_LINE 端點變動（舊→新·逐條）")
    P("-" * 108)
    n_changed = {}
    for lay in ("FRONT_LINE", "SIDE_LINE"):
        go = sorted(geoms(eo, lay, "LINE"))
        gn = sorted(geoms(en, lay, "LINE"))
        # 以「兩端點集合之最近配對」對上舊新（同一條線之身分由幾何鄰近決定·非 handle）
        used, pairs = set(), []
        for a in go:
            best, bj = None, None
            for j, b in enumerate(gn):
                if j in used:
                    continue
                dd = min(dist(a[0], b[0]) + dist(a[1], b[1]),
                         dist(a[0], b[1]) + dist(a[1], b[0]))
                if best is None or dd < best:
                    best, bj = dd, j
            used.add(bj)
            pairs.append((a, gn[bj], best))
        ch = [p for p in pairs if p[2] > 0]
        n_changed[lay] = len(ch)
        P(f"  ── {lay}（共 {len(go)} 條·變動 {len(ch)} 條）")
        for a, b, dd in pairs:
            if dd <= 0:
                continue
            for i in (0, 1):
                if a[i] != b[i]:
                    P(f"     端點{i + 1}  舊 ({a[i][0]:.6f}, {a[i][1]:.6f})"
                      f"  →  新 ({b[i][0]:.6f}, {b[i][1]:.6f})"
                      f"   位移 {dist(a[i], b[i]):.9f} m")
            _la = dist(a[0], a[1])
            _lb = dist(b[0], b[1])
            P(f"     線長 舊 {_la:.6f} → 新 {_lb:.6f}   Δ {_lb - _la:+.9f} m")
    P(f"  ⇒ FRONT_LINE 變動 {n_changed['FRONT_LINE']} 條／"
      f"SIDE_LINE 變動 {n_changed['SIDE_LINE']} 條")

    # ── (5) 街廓頂點對 FRONT_LINE 之最大偏差 ───────────────────────────
    P()
    P(f"【5】街廓頂點對 FRONT_LINE 之偏差（貼線母體＝垂距 ≤ {EPS_ON}m 且投影落段內）")
    P("-" * 108)
    for tag, ee in (("舊", eo), ("新", en)):
        fl = geoms(ee, "FRONT_LINE", "LINE")
        bv = [p for g in geoms(ee, "BLOCK", "POLYLINE") for p in g]
        hits = []
        for v in bv:
            for s, t in fl:
                dd, u = perp(v, s, t)
                if dd <= EPS_ON and -0.001 <= u <= 1.001:
                    hits.append((dd, v))
        mx = max((h[0] for h in hits), default=0.0)
        _worst = max(hits, default=(0.0, None))[1]
        P(f"  {tag}：貼線頂點 **{len(hits)} 個**／最大偏差 **{mx:.9f} m**"
          f"{'' if _worst is None else f'  @ ({_worst[0]:.6f}, {_worst[1]:.6f})'}")

    # ── (6) FRONT_LINE 端點 ↔ SIDE_LINE 端點 ───────────────────────────
    P()
    P(f"【6】FRONT_LINE 端點 ↔ SIDE_LINE 端點（**只看 <{EPS_NEAR}m 之相鄰組合**）")
    P("-" * 108)
    P("  ⚠️ 刻意不採「無限直線交點 vs 端點」——該法會把相隔上百公尺之非相鄰線配成一組。")
    for tag, ee in (("舊", eo), ("新", ee_ := en)):
        fe = [p for g in geoms(ee, "FRONT_LINE", "LINE") for p in g]
        se = [p for g in geoms(ee, "SIDE_LINE", "LINE") for p in g]
        near = [(dist(a, b), a, b) for a, b in itertools.product(fe, se)
                if dist(a, b) < EPS_NEAR]
        mx = max((n[0] for n in near), default=0.0)
        P(f"  {tag}：<{EPS_NEAR}m 之組合 **{len(near)} 組**／最大距 **{mx:.9f} m**"
          f"  {'（街角理論交點未被拆開）' if mx == 0.0 else '（有被拆開者）'}")

    P()
    P("=" * 108)
    P("RESULT: 只驗不改（本工具不進任何判定鏈·rc 恆 0）")
    P("=" * 108)

    out = os.path.join(VERIFY, "out", "verify_dxf_v6_1.log")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n→ {os.path.relpath(out, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
