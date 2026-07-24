# -*- coding: utf-8 -*-
"""容量拆解探針之**離線指派求解器**（姊妹腳本·純算術·秒級·可獨立重跑）。

## 為何分離

`probe_capacity_decomp.py` 內建之窮舉以 `itertools.product` 為之，本案 3.5m 之
`space=559872` 超其保護上限 `cap_space=300000` → **未窮舉、僅出可容上界**。
本求解器讀該探針 dump 之 log，以 **DFS＋塊剩餘容量剪枝（MRV 序）** 重解——
無 product 之組合爆炸，秒級證出「可行 or 不可行＋一組指派」。

## 取數

**不重跑引擎**、不碰治理碼——純讀 `verify/out/probe_capacity_decomp.log`（探針 dump）：
逐塊表（pool／碎片／forced鎖定／reachable／MinA）＋完整 consume matrix。
故其結論之時效與探針同（基線波前產物·待重烤·§探針 docstring）。

## 三情境 reachable（與探針一致）
    甲現況 = reachable（＝ pool − 碎片 − forced鎖定）
    乙釋forced = pool − 碎片
    丙釋碎片 = pool − forced鎖定

容量 `cap(b) = reachable(b) − MinA(b) + 0.5`（治理碼 `wf_f4._e2_optimal` :1102/:1126 同式）。
consume 沿用探針之現況 canonical G（**一階近似**：反事實僅放大容量、不重算幾何）。

## 重跑
    python verify/probes/probe_capacity_decomp_solve.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
LOG = os.path.join(VERIFY, "out", "probe_capacity_decomp.log")


def _parse(path):
    """回傳 {tag: {"blocks":[...], "pool/frag/lock/reach/mina": {b:v}, "cost": {(g,b):v},
    "gids": [...]}}。"""
    txt = open(path, encoding="utf-8").read()
    out = {}
    # 以 [CAPDECOMP] tag=... 切區塊
    parts = re.split(r"\[CAPDECOMP\] tag=", txt)
    for part in parts[1:]:
        tag = part.split()[0]
        d = {"pool": {}, "frag": {}, "lock": {}, "reach": {}, "mina": {}, "cost": {}}
        # 逐塊表行：R1  pool  碎片  forced  unreach  reachable  MinA  容量  最小cons  上界
        for m in re.finditer(r"^(R\d)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+[\d.]+\S*\s+"
                             r"([\d.]+)\s+([\d.]+)\s+", part, re.M):
            b = m.group(1)
            d["pool"][b] = float(m.group(2)); d["frag"][b] = float(m.group(3))
            d["lock"][b] = float(m.group(4)); d["reach"][b] = float(m.group(5))
            d["mina"][b] = float(m.group(6))
        # consume matrix
        mm = re.search(r"完整 consume matrix.*?\n\s+(.*)", part)
        if mm:
            for tok in mm.group(1).split("；"):
                tok = tok.strip()
                mt = re.match(r"([A-Za-z0-9]+)@(R\d)=([\d.]+)", tok)
                if mt:
                    d["cost"][(mt.group(1), mt.group(2))] = float(mt.group(3))
        d["blocks"] = sorted(d["pool"])
        d["gids"] = sorted({g for (g, b) in d["cost"]})
        out[tag] = d
    return out


def _solve(cost, cap, gids, blocks):
    """DFS＋塊剩餘容量剪枝（MRV：候選最少之戶先排）。回傳 (可行, 指派dict or None)。"""
    opts = {g: sorted([b for b in blocks
                       if (g, b) in cost and cost[(g, b)] <= cap[b] + 1e-9],
                      key=lambda b: cost[(g, b)]) for g in gids}
    order = sorted(gids, key=lambda g: len(opts[g]))
    rem = dict(cap)
    assign = {}

    def dfs(i):
        if i == len(order):
            return True
        g = order[i]
        for b in opts[g]:
            if cost[(g, b)] <= rem[b] + 1e-9:
                rem[b] -= cost[(g, b)]; assign[g] = b
                if dfs(i + 1):
                    return True
                rem[b] += cost[(g, b)]; del assign[g]
        return False

    ok = dfs(0)
    return ok, (dict(assign) if ok else None)


def _upper_bound(cost, cap, gids, blocks):
    tot = 0
    per = {}
    for b in blocks:
        items = sorted(v for (g, bb), v in cost.items() if bb == b)
        s = n = 0
        for x in items:
            if s + x <= cap[b] + 1e-9:
                s += x; n += 1
            else:
                break
        per[b] = n; tot += n
    return per, tot


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if not os.path.exists(LOG):
        print(f"🔴 缺 {LOG}——先跑 probe_capacity_decomp.py")
        return 1
    data = _parse(LOG)
    print("=" * 92)
    print("容量拆解 · 離線指派求解（DFS 剪枝·三情境）")
    print("=" * 92)
    for tag, d in data.items():
        need = len(d["gids"])
        blocks = d["blocks"]
        reach_fns = {
            "甲現況": {b: d["reach"][b] for b in blocks},
            "乙釋forced": {b: max(d["pool"][b] - d["frag"][b], 0.0) for b in blocks},
            "丙釋碎片": {b: max(d["pool"][b] - d["lock"][b], 0.0) for b in blocks},
        }
        print(f"\n■ tag={tag}  需求群={need}  戶={d['gids']}")
        for nm, reach in reach_fns.items():
            cap = {b: reach[b] - d["mina"][b] + 0.5 for b in blocks}
            per, ub = _upper_bound(d["cost"], cap, d["gids"], blocks)
            ok, assign = _solve(d["cost"], cap, d["gids"], blocks)
            print(f"  [{nm}] 可容上界 {per}｜和={ub} vs 需求={need}｜"
                  f"窮舉={'✅可行' if ok else '🔴不可行'}")
            if assign:
                by = {}
                for g, b in sorted(assign.items()):
                    by.setdefault(b, []).append(g)
                print(f"        指派：{ {b: by[b] for b in sorted(by)} }")
    print("=" * 92)
    return 0


if __name__ == "__main__":
    sys.exit(main())
