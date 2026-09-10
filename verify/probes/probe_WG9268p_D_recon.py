# -*- coding: utf-8 -*-
"""補令四 `§二`／`§三`：`D-1`／`D-2`／`D-3` **三分表** ＋ 二殘留之對帳（唯讀）。

🔒 **三表⛔ 同表**（補令四 `§二` 明令）——`D-1` 係**靜態錨位移**（模型量·對未改之基準）、
   `D-2` 係**實跑最終態之位置變動**（級聯 ＋ 重解 `S` 後）、`D-3` 係**鏈頭之對位**（⛔ 上游可級聯）。
🔒 母體逐表分列；粒度框逐表分列。⛔ 以 `D-1` 之列數與 `D-2` 之列數相比（`自誤 340`）。
"""
# 🩸 **⛔ 硬編絕對路徑**（承 `W-G.9-268pR c0-5` 自捕 `1`：倉內探針硬編他窗 worktree 路徑
#    ⇒ 靜默量到他窗產物）。**快照基底目錄由 `argv[1]` 給定**；其下須有 `D_off/`／`D_on/` 二子目錄。
import csv
import io
import os
import sys

SCR = (sys.argv[1] if len(sys.argv) > 1
       else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out"))
OFF = os.path.join(SCR, "D_off")
ON = os.path.join(SCR, "D_on")
W = 124
TOL = 0.01                      # `累積S(m)` 之 2dp 捨入


def load(d, scen):
    """回 {暫編地號: row}。off 態中止 ⇒ 讀 `_partial`；on 態跑完 ⇒ 讀完整檔。"""
    for suf in ("_partial", ""):
        p = os.path.join(d, "got_G值_退縮%s%s.csv" % (scen, suf))
        if os.path.exists(p):
            with io.open(p, encoding="utf-8-sig", newline="") as f:
                rows = list(csv.DictReader(f))
            return {r["暫編地號"]: r for r in rows}, os.path.basename(p), len(rows)
    return {}, "⛔ 無", 0


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


FAIL = []
print("=" * W)
print("【補令四 `§二`／`§三`】`D-1`／`D-2`／`D-3` 三分表 ＋ 二殘留對帳（唯讀）")
print("=" * W)
print()

DATA = {}
for scen in ("0m", "3.5m"):
    o, on_f, on_n = load(ON, scen)
    b, off_f, off_n = load(OFF, scen)
    DATA[scen] = (b, o)
    print("  情境 %-5s  off 落檔 %-32s %3d 列  ／  on 落檔 %-26s %3d 列"
          % (scen, off_f, off_n, on_f, on_n))
print()

# ── D-2：Δ累積S（off vs on·共同鍵）────────────────────────────
print("=" * W)
print("【`D-2`】最終態之位置變動（**級聯**）：`Δ累積S` ＝ on − off（**共同鍵** ＝ 同情境同暫編地號）")
print("=" * W)
print("  🔒 母體 ＝ 二態**皆有**之格；粒度框 ＝ **長度（公尺）**。")
print("  🛑 **⛔ 以本表之列數與 `D-1` 相比**——二者係不同之量（`自誤 340`）。")
print()
print("  %-6s %-16s %-10s %11s %11s %11s %s"
      % ("情境", "暫編地號", "驗_宗序", "off 累積S", "on 累積S", "Δ累積S", "|Δ|>0.01"))
D2 = {}
for scen in ("0m", "3.5m"):
    b, o = DATA[scen]
    common = [k for k in b if k in o]
    for k in sorted(common, key=lambda x: f(b[x].get("累積S(m)")) or 0):
        a, c = f(b[k].get("累積S(m)")), f(o[k].get("累積S(m)"))
        if a is None or c is None:
            continue
        d = c - a
        D2[(scen, k)] = (a, c, d, (o[k].get("驗_宗序") or "").strip(),
                         (o[k].get("推進側別") or "").strip(),
                         (o[k].get("所屬街廓") or "").strip())
        if abs(d) > TOL:
            print("  %-6s %-16s %-10s %11.4f %11.4f %+11.4f %s"
                  % (scen, k, (o[k].get("驗_宗序") or "")[:8], a, c, d, "🔴 是"))
big2 = [kk for kk, v in D2.items() if abs(v[2]) > TOL]
print("  母體基數（共同鍵）＝ %d 格；`|Δ累積S| > %.2f` 者 ＝ **%d** 格"
      % (len(D2), TOL, len(big2)))
sd = sum(v[2] for v in D2.values())
print("  **Σ Δ累積S（帶號）＝ %+.4f m** ／ **Σ|Δ累積S| ＝ %.4f m**"
      % (sd, sum(abs(v[2]) for v in D2.values())))
print()

# ── D-3：鏈頭之對位 ──────────────────────────────────────────
print("=" * W)
print("【`D-3`】**鏈頭之對位**（`驗_宗序 == '街角第1宗'` ＝ `j = 0`·**⛔ 上游可級聯**）")
print("=" * W)
print("  🔒 判準（補令四 `§二`）：鏈頭格之 `Δ累積S` 須**等於**該格 `D-1` 之 `δ`（容差 %.2f m）。" % TOL)
print("  🔑 **本表即 `自誤 340` 通則所稱之「不受級聯影響之子母體」**。")
print()
heads = {kk: v for kk, v in D2.items() if v[3] == "街角第1宗"}
print("  %-6s %-16s %-6s %-6s %11s %11s %11s"
      % ("情境", "暫編地號", "街廓", "側", "off 累積S", "on 累積S", "Δ累積S"))
for kk in sorted(heads, key=lambda x: (x[0], heads[x][5], heads[x][4])):
    a, c, d, _o, side, blk = heads[kk]
    print("  %-6s %-16s %-6s %-6s %11.4f %11.4f %+11.4f"
          % (kk[0], kk[1], blk, side, a, c, d))
print("  鏈頭母體基數 ＝ %d 格（`D-3` 之判定集）" % len(heads))
print()

# ── 二殘留 ─────────────────────────────────────────────────
print("=" * W)
print("【`§三`】二殘留之現查")
print("=" * W)
for tag, scen, lot in (("殘-1", "3.5m", "628(1)+"), ("殘-2", "0m", None)):
    if lot:
        kk = (scen, lot)
        if kk in D2:
            a, c, d, o, side, blk = D2[kk]
            print("  %-6s %s·%s·%s `%s`（%s）：%.4f → %.4f ⇒ **Δ ＝ %+.4f**"
                  % (tag, scen, blk, side, lot, o, a, c, d))
        else:
            print("  %-6s %s `%s` ⛔ 在共同鍵內（off 態⛔ 產出該格）" % (tag, scen, lot))
print()

json_out = os.path.join(SCR, "D_recon.json")
import json
with io.open(json_out, "w", encoding="utf-8") as fh:
    json.dump({("%s|%s" % k): list(v) for k, v in D2.items()}, fh,
              ensure_ascii=False, indent=1)
print("  🔒 `D-2` 之全表已落檔（供 `D-1` 對位）：%s" % os.path.basename(json_out))
