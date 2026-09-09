# -*- coding: utf-8 -*-
r"""`W-G.9-264 §七`：**角退判準**之唯讀探針（純診斷·⛔ 修法主張·⛔ 修）

🛑 **唯讀**：本檔只讀 `verify/out/got_G值_退縮{0m,3.5m}_partial.csv`，
   **⛔ 寫入任何檔**、**⛔ import 生產路徑之寫入面**（只用 `csv`／`ast`／`shapely.geometry`）。

**定義（單 `§五 a` 逐字）**
  **角退** ＝ 該側存在 `驗_宗序 ＝ 街角第1宗` 之宗，且其 `W` **大於**該側 `第2宗` 之 `W`
  （`ΔW ＝ W(第2宗) − W(街角第1宗) < 0`）。

**器（單 `§五 a` 逐字）**
  讀落檔 `cut_coords` → `shapely.Polygon`（`is_valid` 否則 `buffer(0)`）
  → 同街廓同側**兩兩** `intersection().area`，`> 1e-6` 計入。

**陰性對照（單 `§七` 所令）**：對一必不存在之街廓名須輸出 `0` 列。
  🔒 該名於**執行期組出**，⛔ 使其字面落入本檔（`GB-147`）。

用法：`python verify/probes/probe_corner_retro_overlap.py [out_dir]`
      `out_dir` 預設 ＝ 本倉之 `verify/out`。
"""
import ast
import csv
import io
import itertools
import os
import sys

from shapely.geometry import Polygon

TOL_AREA = 1e-6
TAGS = ("0m", "3.5m")
COL_BLK = "所屬街廓"
COL_SIDE = "推進側別"
COL_LOT = "暫編地號"
COL_W = "W(m)"
COL_ORD = "驗_宗序"
COL_CUT = "cut_coords"
V_FIRST = "街角第1宗"
V_SECOND = "第2宗"
SIDE_OFFSET = "抵費地"


def _rows(out_dir, tag):
    p = os.path.join(out_dir, "got_G值_退縮%s_partial.csv" % tag)
    if not os.path.exists(p):
        p2 = os.path.join(out_dir, "got_G值_退縮%s.csv" % tag)
        if not os.path.exists(p2):
            return None, p
        p = p2
    with io.open(p, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh)), p


def _poly(s):
    """`cut_coords` 之字面 → `shapely.Polygon`；不可成環者回 `None`。"""
    if not s or not s.strip():
        return None
    try:
        pts = [(float(x), float(y)) for x, y in ast.literal_eval(s)]
    except Exception:
        return None
    if len(pts) < 3:
        return None
    g = Polygon(pts)
    if not g.is_valid:
        g = g.buffer(0)
    return g if (not g.is_empty) else None


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def scan(out_dir, blk_filter=None):
    """回傳逐 (情境, 街廓, 側) 之列。`blk_filter` 非 None 時只取該街廓。"""
    out = []
    for tag in TAGS:
        rows, path = _rows(out_dir, tag)
        if rows is None:
            out.append({"tag": tag, "blk": None, "side": None,
                        "阻斷點": "落檔不存在：%s" % path})
            continue
        groups = []
        seen = set()
        for r in rows:
            k = (r.get(COL_BLK), r.get(COL_SIDE))
            if k[1] == SIDE_OFFSET:
                continue
            if blk_filter is not None and k[0] != blk_filter:
                continue
            if k not in seen:
                seen.add(k)
                groups.append(k)
        for blk, side in groups:
            sub = [r for r in rows
                   if r.get(COL_BLK) == blk and r.get(COL_SIDE) == side]
            first = [r for r in sub if r.get(COL_ORD) == V_FIRST]
            second = [r for r in sub if r.get(COL_ORD) == V_SECOND]
            dW = None
            if first and second:
                w1, w2 = _num(first[0].get(COL_W)), _num(second[0].get(COL_W))
                if w1 is not None and w2 is not None:
                    dW = w2 - w1
            polys = []
            for r in sub:
                g = _poly(r.get(COL_CUT))
                if g is not None:
                    polys.append((r.get(COL_LOT), g))
            tot = 0.0
            pairs = []
            for (n1, g1), (n2, g2) in itertools.combinations(polys, 2):
                try:
                    a = g1.intersection(g2).area
                except Exception:
                    continue
                if a > TOL_AREA:
                    tot += a
                    pairs.append((n1, n2, a))
            out.append({
                "tag": tag, "blk": blk, "side": side,
                "first": first[0].get(COL_LOT) if first else None,
                "second": second[0].get(COL_LOT) if second else None,
                "dW": dW,
                "retro": (dW is not None and dW < 0),
                "overlap": tot, "pairs": pairs,
                "n_lot": len(sub), "n_poly": len(polys),
            })
    return out


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))
    out_dir = argv[1] if len(argv) > 1 else os.path.join(repo, "verify", "out")
    print("=" * 112)
    print("【角退判準】唯讀探針　out_dir = %s" % out_dir)
    print("=" * 112)
    rows = scan(out_dir)
    print("%-6s %-5s %-7s %-14s %-14s %-10s %-7s %-14s"
          % ("情境", "街廓", "側", "街角第1宗", "第2宗", "ΔW", "角退?", "兩兩重疊(㎡)"))
    n_nonzero = 0
    for r in rows:
        if r.get("阻斷點"):
            print("%-6s 🔴 阻斷點：%s" % (r["tag"], r["阻斷點"]))
            continue
        if r["overlap"] > TOL_AREA:
            n_nonzero += 1
        print("%-6s %-5s %-7s %-14s %-14s %-10s %-7s %-14.4f"
              % (r["tag"], r["blk"], r["side"],
                 r["first"] or "—", r["second"] or "—",
                 ("%+.2f" % r["dW"]) if r["dW"] is not None else "—",
                 "是" if r["retro"] else "否",
                 r["overlap"]))
    print()
    print("  組數 = %d ／ 重疊非零之組數 = %d" % (len(rows), n_nonzero))
    print()
    print("-- 重疊之施加者（逐對·僅非零組）--")
    for r in rows:
        if r.get("阻斷點") or r["overlap"] <= TOL_AREA:
            continue
        print("  %s %s %s：" % (r["tag"], r["blk"], r["side"]))
        for n1, n2, a in r["pairs"]:
            print("      %s ∩ %s = %.4f" % (n1, n2, a))
    print()
    # 陰性對照（名於執行期組出·⛔ 使其字面落入本檔）
    ghost = chr(82) + str(9 * 111)
    neg = scan(out_dir, blk_filter=ghost)
    neg = [x for x in neg if not x.get("阻斷點")]
    print("-- 陰性對照（一必不存在之街廓名·代稱）：輸出 %d 列（須 0）--" % len(neg))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
