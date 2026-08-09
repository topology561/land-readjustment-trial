# -*- coding: utf-8 -*-
r"""**D-2b-14 §b1′-1**：量出 shapely 於「界線近 ∥ 推進向」區帶開始**自我矛盾**之夾角。

🔒 **⛔ 不得先挑門檻再驗**——本檔之唯一目的是**先量出區帶邊界**，門檻於 §b1′-2 才依此導出。

## 兩種**獨立**量法（⛔ 不得由其一推導另一）

| 量法 | 內容 |
|---|---|
| **甲 逐步不變量** | 每步之 `片_i ∩ 新餘塊_i` 面積；且餘塊面積鏈自洽：`\|rem_{i−1} − 片_i − rem_i\|` |
| **乙 事後兩兩** | 收齊全部片後之**兩兩**交集面積 |

甲之逐步鏈以**生產原語** `_strip_halfplane`（`ns` harvest）重建——與 `_block_partition`
內之構造**同一函式**；⛔ 未複刻其鋪滿閘與回傳結構，僅取「餘塊逐次二分」之逐步中間態
（`_block_partition` 只回最終片與彙總 diag，取不到逐步量）。

**判不一致** ＝ 甲說乾淨（逐步交集與鏈殘差皆 ≤1e-6）而乙說有重疊（>1e-6），或反之。
⇒ 兩法矛盾 ⇒ **量測本身不可信** ⇒ 閘不得建於其上。
"""
import io
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, os.environ.get("WV_GUARD_LOG", "probe_D2b14_guard.log"))
CASES = os.path.join(OUTDIR, "probe_D2b14_cases.json")
SEED = 20260809_14
TOL = 1e-6
W = 200


def _u(v):
    n = math.hypot(v[0], v[1])
    return (v[0] / n, v[1] / n)


def _polys(rng, k=10):
    from shapely.geometry import Polygon
    out = []
    while len(out) < k:
        cx, cy = rng.uniform(-180.3, 320.7), rng.uniform(-90.1, 240.9)
        n = rng.randint(6, 12)
        pts, a = [], rng.uniform(0, 2 * math.pi)
        for _ in range(n):
            a += (2 * math.pi / n) * rng.uniform(0.45, 1.55)
            r = rng.uniform(33.1, 141.7) * (0.4 if rng.random() < 0.3 else 1.0)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        p = Polygon(pts)
        if not p.is_valid:
            p = p.buffer(0)
        if p.is_empty or p.geom_type != "Polygon" or p.area < 400.0:
            continue
        out.append(p)
    return out


def _carve(ns, poly, d_hat, lines):
    """以**生產** `_strip_halfplane` 逐步削餘；回傳 (pieces, 甲之逐步量測)。"""
    import numpy as np
    hp = ns["_strip_halfplane"]
    b = poly.bounds
    big = max(b[2] - b[0], b[3] - b[1]) * 4.0 + 100.0
    dh = np.asarray(d_hat, dtype=float)
    dh = dh / float(np.linalg.norm(dh))
    rem = poly
    pieces, step = [], []
    for i, (q, g) in enumerate(lines[1:], start=1):
        _q = np.asarray(q, dtype=float)
        _g = np.asarray(g, dtype=float)
        _g = _g / float(np.linalg.norm(_g))
        lo = hp(_q, _g, -1.0, dh, big)
        hi = hp(_q, _g, +1.0, dh, big)
        if lo is None or hi is None:
            return None, None
        _prev_area = float(rem.area)
        pc = rem.intersection(lo)
        rm = rem.intersection(hi)
        step.append({
            'i': i,
            'ov': float(pc.intersection(rm).area) if (not pc.is_empty and not rm.is_empty) else 0.0,
            'chain': abs(_prev_area - float(pc.area) - float(rm.area)),
        })
        pieces.append(pc)
        rem = rm
    pieces.append(rem)
    return pieces, step


def main():                                                        # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    import json
    import numpy as np

    ns, _ = harvest()
    rng = random.Random(SEED)
    polys = _polys(rng)
    L = []
    L.append("=" * W)
    L.append(f"【D-2b-14 §b1′-1】shapely 自我矛盾區帶之邊界實測（seed={SEED}）")
    L.append("=" * W)
    L.append("  🔒 **⛔ 先量再定門檻**——本節不挑門檻，只量「兩法開始不一致」之夾角。")
    L.append("  甲 ＝ 逐步不變量（每步 `片∩新餘塊` ＋ 餘塊面積鏈自洽）")
    L.append("  乙 ＝ 事後兩兩交集　　（兩法獨立·⛔ 未由其一推導另一）")
    L.append(f"  難幾何母體 ＝ **{len(polys)}** 個（⛔ 非空）")
    if not polys:
        raise RuntimeError("🔴 母體為空 ⇒ 失敗")

    ANGLES = [90.0, 60.0, 30.0, 15.0, 10.0, 6.0, 4.0, 3.0, 2.5, 2.3, 2.0,
              1.5, 1.0, 0.7, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01]
    L.append(f"  掃描夾角（界線 vs 推進向）：{ANGLES}（度）　解析度見清單")
    L.append("")
    L.append(f"  {'θ(deg)':>8}{'sin θ':>12}{'例數':>6}{'甲 max 逐步∩':>16}{'甲 max 鏈殘差':>16}"
             f"{'乙 max 兩兩∩':>16}{'不一致例':>9}  判定")
    L.append("-" * W)

    _first_bad = None
    _bad_cases = []
    for th_deg in ANGLES:
        th = math.radians(th_deg)
        n_ok = 0
        m_a_ov = m_a_ch = m_b = 0.0
        n_bad = 0
        for pi, poly in enumerate(polys):
            b = poly.bounds
            base = np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0])
            for _t in range(3):
                ang = rng.uniform(0, 2 * math.pi)
                d_hat = np.array(_u((math.cos(ang), math.sin(ang))))
                # 界線方向 ĝ 與 d̂ 夾角 ＝ th（⇒ `_wn = |d̂ − (d̂·ĝ)ĝ| = sin th`）
                gdir = _u((math.cos(ang + th), math.sin(ang + th)))
                k = rng.randint(4, 6)
                svals = sorted(rng.uniform(-150.0, 150.0) for _ in range(k + 1))
                # 界線方向逐條微擾（仍在同一夾角量級）
                dirs = [_u((math.cos(ang + th * rng.uniform(0.85, 1.15)),
                            math.sin(ang + th * rng.uniform(0.85, 1.15))))
                        for _ in range(k + 1)]
                dirs[0] = gdir
                qs = [base + s * d_hat for s in svals]
                lines = list(zip([tuple(map(float, q)) for q in qs], dirs))
                pieces, step = _carve(ns, poly, d_hat, lines)
                if pieces is None:
                    continue
                n_ok += 1
                a_ov = max((s['ov'] for s in step), default=0.0)
                a_ch = max((s['chain'] for s in step), default=0.0)
                bmax = 0.0
                bpair = None
                for i in range(len(pieces)):
                    for j in range(i + 1, len(pieces)):
                        if pieces[i].is_empty or pieces[j].is_empty:
                            continue
                        x = float(pieces[i].intersection(pieces[j]).area)
                        if x > bmax:
                            bmax, bpair = x, (i, j)
                m_a_ov = max(m_a_ov, a_ov); m_a_ch = max(m_a_ch, a_ch); m_b = max(m_b, bmax)
                _clean_a = (a_ov <= TOL and a_ch <= TOL)
                _clean_b = (bmax <= TOL)
                if _clean_a != _clean_b:
                    n_bad += 1
                    if len(_bad_cases) < 2:
                        _bad_cases.append({
                            'theta_deg': th_deg, 'poly': [list(map(float, c))
                                                          for c in poly.exterior.coords[:-1]],
                            'd_hat': [float(d_hat[0]), float(d_hat[1])],
                            'lines': [[list(map(float, q)), list(map(float, g))]
                                      for q, g in lines],
                            'measure_A_max_step_overlap': a_ov,
                            'measure_A_max_chain_resid': a_ch,
                            'measure_B_max_pair_overlap': bmax,
                            'measure_B_pair': list(bpair) if bpair else None,
                            'note': '甲說乾淨、乙說重疊（或反之）⇒ 量測自我矛盾',
                        })
        _verdict = ("✅ 一致" if n_bad == 0 else f"🔴 **不一致 {n_bad}**")
        if n_bad and _first_bad is None:
            _first_bad = th_deg
        L.append(f"  {th_deg:>8.2f}{math.sin(th):>12.6f}{n_ok:>6}"
                 f"{m_a_ov:>16.6e}{m_a_ch:>16.6e}{m_b:>16.6e}{n_bad:>9}  {_verdict}")

    # ══ 補掃：界線**順序未排序**（施工單所述 `片2∩片4 == 片4 全部面積` 之候選觸發）══
    L.append("")
    L.append("【補掃】界線**順序未排序**（⛔ 上表全為已排序·此為另一維度）")
    L.append("-" * W)
    L.append("  由來：施工單所述矛盾為 `片2∩片4 = 924.201867`（**恰等於片4 全部面積**）")
    L.append("  ⇒ 片4 **整個**落在片2 內。依序削餘下 `片_j ⊆ rem_i`（j>i）且 `片_i ∩ rem_i = 0`")
    L.append("  ⇒ 構造上不可能 —— **除非 rem 非單調**，而 rem 非單調之最直接成因 ＝ **界線未依序**。")
    _uns_bad, _uns_n, _uns_max = 0, 0, 0.0
    for pi, poly in enumerate(polys):
        b = poly.bounds
        base = np.array([(b[0] + b[2]) / 2.0, (b[1] + b[3]) / 2.0])
        for _t in range(8):
            ang = rng.uniform(0, 2 * math.pi)
            d_hat = np.array(_u((math.cos(ang), math.sin(ang))))
            th = math.radians(rng.uniform(55.0, 125.0))
            k = rng.randint(4, 6)
            svals = [rng.uniform(-150.0, 150.0) for _ in range(k + 1)]   # ⛔ **未排序**
            dirs = [_u((math.cos(ang + th * rng.uniform(0.9, 1.1)),
                        math.sin(ang + th * rng.uniform(0.9, 1.1)))) for _ in range(k + 1)]
            qs = [base + s * d_hat for s in svals]
            lines = list(zip([tuple(map(float, q)) for q in qs], dirs))
            pieces, step = _carve(ns, poly, d_hat, lines)
            if pieces is None:
                continue
            _uns_n += 1
            a_ov = max((s['ov'] for s in step), default=0.0)
            a_ch = max((s['chain'] for s in step), default=0.0)
            bmax, bpair = 0.0, None
            for i in range(len(pieces)):
                for j in range(i + 1, len(pieces)):
                    if pieces[i].is_empty or pieces[j].is_empty:
                        continue
                    x = float(pieces[i].intersection(pieces[j]).area)
                    if x > bmax:
                        bmax, bpair = x, (i, j)
            _uns_max = max(_uns_max, bmax)
            if (a_ov <= TOL and a_ch <= TOL) != (bmax <= TOL):
                _uns_bad += 1
                if len(_bad_cases) < 2:
                    _bad_cases.append({
                        'theta_deg': math.degrees(th), 'order': 'UNSORTED',
                        'poly': [list(map(float, c)) for c in poly.exterior.coords[:-1]],
                        'd_hat': [float(d_hat[0]), float(d_hat[1])],
                        'lines': [[list(map(float, q)), list(map(float, g))] for q, g in lines],
                        'measure_A_max_step_overlap': a_ov,
                        'measure_A_max_chain_resid': a_ch,
                        'measure_B_max_pair_overlap': bmax,
                        'measure_B_pair': list(bpair) if bpair else None,
                        'note': '界線未依序 ⇒ 甲說乾淨而乙說重疊（量測自我矛盾）',
                    })
    L.append(f"  未排序母體 ＝ **{_uns_n}** 例　**不一致 {_uns_bad}** 例"
             f"　乙 max 兩兩∩ ＝ **{_uns_max:.6e}**")
    L.append("  ⇒ " + ("🔑 **未排序即可觸發兩法矛盾** ⇒ 區帶之真正述詞可能是"
                       "「**界線未依序**」而非「界線 ∥ 推進向」"
                       if _uns_bad else "✅ 未排序亦未觸發矛盾"))

    L.append("")
    L.append("【區帶邊界】")
    L.append("-" * W)
    if _first_bad is None:
        L.append(f"  🛑 **掃不到兩法不一致** ——掃描範圍 {min(ANGLES)}°–{max(ANGLES)}°、"
                 f"級距 {len(ANGLES)} 檔、每檔 ≤{len(polys) * 3} 例。")
        L.append("     ⇒ 區帶邊界**無從導出**、門檻**無依據** ⇒ **停機上呈**（§六）。")
        L.append("     ⛔ **不得**以「沒觀察到不一致」當作區帶不存在。")
    else:
        L.append(f"  **兩法開始不一致之最大夾角 ＝ {_first_bad}°**"
                 f"（`sin θ = {math.sin(math.radians(_first_bad)):.6f}`）")
        _ortho = [a for a in ANGLES if a >= 45.0]
        _bad_ortho = _first_bad >= 45.0
        L.append(f"  近 ⊥ 端（≥45°）是否受影響：{'🛑 **是 ⇒ 停機**' if _bad_ortho else '✅ 否'}")
        if _bad_ortho:
            L.append("     ⇒ UC9898 六街廓（分配線近 ⊥ 推進向）亦落在不可信區帶 ⇒ "
                     "**T2 驗收基礎須重估·停機上呈**")
    with io.open(CASES, "w", encoding="utf-8") as f:
        json.dump(_bad_cases, f, ensure_ascii=False, indent=1)
    L.append(f"  🔒 矛盾組態已存 **{len(_bad_cases)}** 例之**座標實體**"
             f"（⛔ 非亂數種子）⇒ `verify/out/{os.path.basename(CASES)}`")

    L.append("")
    L.append("=" * W)
    txt = "\n".join(L)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(txt)
    print(f"\n[written] {LOG}")


if __name__ == "__main__":
    main()
