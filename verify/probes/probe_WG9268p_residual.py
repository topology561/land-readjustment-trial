# -*- coding: utf-8 -*-
"""補令四 `§三`：二殘留之**成因**（機械·⛔ 推定）＋ 其歸類（甲／乙／丙）。

歸類（單 `§三` 逐字）：`(甲)` `c0-5` 器之射程界限／`(乙)` `c1` 實作與 `c0-5` 模型之語意差／
`(丙)` 級聯與重解 `S` 之交互作用。🛑 判為 `(乙)` ⇒ 停機上呈。
"""
# 🩸 **⛔ 硬編絕對路徑**（承 `W-G.9-268pR c0-5` 自捕 `1`：倉內探針硬編他窗 worktree 路徑
#    ⇒ 靜默量到他窗產物）。**快照基底目錄由 `argv[1]` 給定**；其下須有 `D_off/`／`D_on/` 二子目錄。
import ast
import csv
import io
import math
import os
import sys

SCR = (sys.argv[1] if len(sys.argv) > 1
       else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out"))
OFF = os.path.join(SCR, "D_off")
ON = os.path.join(SCR, "D_on")
W = 122
TOL_PARA = 1e-6


def rows(p):
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _u(dx, dy):
    L = math.hypot(dx, dy)
    return (dx / L, dy / L) if L > 1e-12 else None


def edges(pts):
    o = []
    for i in range(len(pts) - 1):
        v = _u(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
        if v:
            o.append((pts[i], pts[i + 1], v,
                      math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])))
    return o


def a180(v):
    return math.degrees(math.atan2(v[1], v[0])) % 180.0


def para(a, b):
    return abs(a[0] * b[1] - a[1] * b[0]) < TOL_PARA


print("=" * W)
print("【補令四 `§三`】二殘留之成因（機械·⛔ 推定）")
print("=" * W)
print()

# ── 殘-1 ──────────────────────────────────────────────────
print("── `殘-1`：`3.5m·R4·left` 鏈頭 `628(1)+` `68.92 → 70.50`（`+1.58`）而 `c0-5` **無**該格之 `δ` ──")
R = [r for r in rows(os.path.join(OFF, "got_G值_退縮3.5m_partial.csv"))
     if r["所屬街廓"] == "R4" and r["推進側別"] == "left"]
print("   `c0-5` 之母體（off 態落檔）中，`3.5m·R4·left` 之**宗數 ＝ %d**" % len(R))
for r in R:
    print("      · `%s`（`%s`）　`累積S ＝ %s`" % (r["暫編地號"], r["驗_宗序"], r["累積S(m)"]))
print("   🔒 `c0-5` 之框標定需**相鄰二宗之共用 ∥ALLOC 界線** ⇒ **宗數 `1` ⇒ ⛔ 有相鄰對**")
print("      ⇒ 該組於 `c0-5` 之逐字判為「**⚠️ ⛔ 可標定：⛔ 偵得任何共用邊（宗數 1）**」")
print("      ⇒ 🔴 **`c0-5` 從未<u>產出</u>該格之 `δ`**——⛔ 「判其 `|δ| ≤ 0.01`」。")
print("   🩸 **單 `§三` 之表述須更正（照實·⛔ 頂替）**：其逐字「而 `c0-5` 判該格 `|δ| ≤ 0.01`」")
print("      ——`c0-5` **⛔ 判之**，其為**母體外**（`⛔ 可標定`）。")
print("   ⇒ **歸類 ＝ `(甲)` `c0-5` 器之射程界限**（⛔ `(乙)`：與 `c1` 之語意無涉）")
print()

# ── 殘-2 ──────────────────────────────────────────────────
print("── `殘-2`：`c0-5` 預測 `0m·R1·right j=1` `δ ＝ +0.3969`，而最終態之 `Δ累積S` 未逾 `0.01` ──")
R2 = [r for r in rows(os.path.join(OFF, "got_G值_退縮0m_partial.csv"))
      if r["所屬街廓"] == "R1" and r["推進側別"] == "right"]
R2.sort(key=lambda r: float(r["累積S(m)"] or 0))
print("   `0m·R1·right` 之宗序（off 態）：")
for j, r in enumerate(R2):
    print("      j=%d `%s`（`%s`）　`S ＝ %s`／`累積S ＝ %s`"
          % (j, r["暫編地號"], r["驗_宗序"], r["S(m)"], r["累積S(m)"]))

# 標定之受限度：相鄰共用 ∥ALLOC 界線之數 ＋ 帶狀宗（二條 ∥ALLOC 邊）之數
P = [[(float(x), float(y)) for x, y in ast.literal_eval(r["cut_coords"])] for r in R2]
votes = {}
for a, b in zip(P, P[1:]):
    best = None
    for p1, _q1, u1, L1 in edges(a):
        for p2, _q2, u2, L2 in edges(b):
            if not para(u1, u2):
                continue
            if abs((p2[0] - p1[0]) * u1[1] - (p2[1] - p1[1]) * u1[0]) > 1e-6:
                continue
            if best is None or min(L1, L2) > best[0]:
                best = (min(L1, L2), u1)
    if best:
        votes[round(a180(best[1]), 4)] = votes.get(round(a180(best[1]), 4), 0.0) + best[0]
a_alloc = max(votes.items(), key=lambda kv: kv[1])[0]
u_alloc = (math.cos(math.radians(a_alloc)), math.sin(math.radians(a_alloc)))
n_hat = (-u_alloc[1], u_alloc[0])
print("   ALLOC 方向（共用邊眾數）＝ %.4f°；共用邊之投票 ＝ %s"
      % (a_alloc, {k: round(v, 3) for k, v in votes.items()}))

known = 0
for a, b in zip(P, P[1:]):
    for p1, _q1, u1, L1 in edges(a):
        for p2, _q2, u2, L2 in edges(b):
            if para(u1, u2) and abs((p2[0] - p1[0]) * u1[1] - (p2[1] - p1[1]) * u1[0]) <= 1e-6 \
                    and para(u1, u_alloc):
                known += 1
                break
        else:
            continue
        break
slopes = 0
for r, pts in zip(R2, P):
    if (r.get("驗_宗序") or "").strip() == "街角第1宗":
        continue
    hs = [p[0] * n_hat[0] + p[1] * n_hat[1] for p, _q, u, _L in edges(pts) if para(u, u_alloc)]
    if len(hs) >= 2:
        slopes += 1
print("   🔴 **標定之約束數：已知點 ＝ %d ／ 斜率約束 ＝ %d**" % (known, slopes))
print("      ⇒ `A` 由**候選方向唯一決定**、`B` 由該**單點**定 ⇒ **`r_pt` 恆為 `0`（vacuous）**、")
print("        **⛔ 受任何第二個約束檢驗** ⇒ 其框之選擇**⛔ 可由資料判別**。")

# 判別力：逐候選方向之 s_錨_幾何（j=1）
cands = {}
for pts in P:
    for _p, _q, u, L in edges(pts):
        if para(u, u_alloc):
            continue
        cands[round(a180(u), 4)] = cands.get(round(a180(u), 4), 0.0) + L
print()
print("   🔑 **判別力（框敏感度）**：逐候選 FRONT 方向重算 `j=1` 之 `s_錨_幾何` 與 `δ`")
print("      %-12s %-10s %13s %13s %11s" % ("候選方向°", "邊長合計", "A", "s_錨_幾何", "δ"))
cum1 = float(R2[1]["累積S(m)"])
out = []
for a_deg, L in sorted(cands.items(), key=lambda kv: -kv[1]):
    v = (math.cos(math.radians(a_deg)), math.sin(math.radians(a_deg)))
    dn = v[0] * n_hat[0] + v[1] * n_hat[1]
    if abs(dn) < 1e-9:
        continue
    for sign in (1.0, -1.0):
        A = sign / dn
        # B 由單一已知點定：取 j=0/j=1 之共用 ∥ALLOC 界線上一點，其 strip ＝ 累積S(0)
        pb = None
        for p1, _q1, u1, _L1 in edges(P[0]):
            for p2, _q2, u2, _L2 in edges(P[1]):
                if para(u1, u2) and para(u1, u_alloc) and \
                        abs((p2[0] - p1[0]) * u1[1] - (p2[1] - p1[1]) * u1[0]) <= 1e-6:
                    pb = p1
                    break
            if pb:
                break
        if pb is None:
            continue
        B = float(R2[0]["累積S(m)"]) - A * (pb[0] * n_hat[0] + pb[1] * n_hat[1])
        sg = max(A * (p[0] * n_hat[0] + p[1] * n_hat[1]) + B for p in P[1])
        # 次序約束 r_ord
        r_ord = 0.0
        for r, pts in zip(R2, P):
            mx = max(A * (p[0] * n_hat[0] + p[1] * n_hat[1]) + B for p in pts)
            r_ord = max(r_ord, max(0.0, float(r["累積S(m)"]) - mx))
        if r_ord > 0.010:
            continue
        out.append((a_deg, L, A, sg, sg - cum1))
        print("      %-12.4f %-10.3f %13.6f %13.4f %+11.4f"
              % (a_deg, L, A, sg, sg - cum1))
if out:
    ds = [o[4] for o in out]
    print("      ⇒ **過次序約束之候選 ＝ %d 個；其 `δ` ∈ [%+.4f, %+.4f]，跨距 ＝ %.4f m**"
          % (len(out), min(ds), max(ds), max(ds) - min(ds)))
    print("      🔴 **跨距 > `0.01`** ⇒ 該格之 `δ` **由框之選擇決定**，⛔ 由資料決定"
          if max(ds) - min(ds) > 0.01 else
          "      🟢 跨距 ≤ `0.01` ⇒ 框之選擇⛔ 決定該格之 `δ`")
print("   ⇒ **歸類 ＝ `(甲)` `c0-5` 器之射程界限**（弱標定 ⇒ 其 `δ` 之可信度結構上低）")
print()

# ── D-1b 之結構性不可得 ────────────────────────────────────
print("=" * W)
print("【`D-1b`】於 **on 態落檔**重量 `δ` ⇒ 🔴 **結構上不可得**")
print("=" * W)
for tag, p in (("off（`_partial`）", os.path.join(OFF, "got_G值_退縮0m_partial.csv")),
               ("on（完整）", os.path.join(ON, "got_G值_退縮0m.csv"))):
    rs = rows(p)
    cols = list(rs[0].keys())
    n = sum(1 for r in rs if (r.get("cut_coords") or "").strip())
    print("  %-18s 欄數 %2d ／ 列數 %2d ／ **有 `cut_coords` 之列 ＝ %2d**"
          % (tag, len(cols), len(rs), n))
print("  🔒 **完整落檔⛔ 含 `cut_coords` 欄**（`50` 欄 vs `_partial` 之 `53` 欄）")
print("     ⇒ `c0-5` 之器（其框全由 `cut_coords` 之幾何導出）於 on 態落檔上**母體為 `0` 組**。")
print("  🛑 ⇒ 依 `CLAUDE.md`「無從回測 ⛔ 等同回測不過」，`D-1b` 之判為 **「無從驗」**，⛔ 「驗不過」。")
print("  🔒 **`D-1a`（於 `c1` 之態、以 off 態落檔重量）已足**：其 `|δ| > 0.01` 之三列與")
print("     `c0-5` 於 `5b05da0` 所得**逐格相同**（`+3.3879`／`+3.3222`／`+0.3969`）。")
