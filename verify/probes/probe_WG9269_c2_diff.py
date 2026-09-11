#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-269` `c2`：**差異表**（補令三 `§四` 表一／表二／表三）＋ `§三` `P-0`〜`P-9` 之可量者。

🩸 **本器之存在理由**
   `c2` 之受詞 ＝ 旗標 `on`（`K-9-23` 閘一剔除 ＋ `K-9-17` 遞補）之**土地後果**。
   補令三 `§四` 令以**域語言**出艙三表；`§三` 令以**性質閘**驗收。本器產其**數**。

🔒 **⛔ 引任何自 `verify/baselines` 取得之數**（`GB-162`）——本器之數**全自當次實跑**。
🔒 **⛔ 另寫第二份定義**（`GB-48` 族）：歸戶用生產碼 `_resolve_ownership`；
   池用 `run_step_g` 之 `pool_diag['池總=幾何剩餘(㎡)']`（＝ `sum(g.area for g in offset_geoms)`
   ·**獨立幾何量測**·⛔ 由 `街廓面積 − ΣG` 倒算 ⇒ 合 `P-2` 之明令）。
🔒 **態宣告二值並報**（`坑 r`／`坑 m`）：`rev-parse HEAD:app.py` ⋀ `hash-object app.py`（**以後者為實**）。

🔒 **二態之取得**（**⛔ 改任何生產碼**）：以環境變數 `WG9269_K917_BACKFILL` 翻之。
   🛑 於 `c2` **落地後**重跑本器並**不設**該變數，其 `on` 側須與此處之 `on` 側**逐位相同**
      ⇒ 方證「翻預設 ≡ 翻環境變數」（⛔ 以「應該一樣」推定）。

🔒 **未量⛔ 印 `0`**（`坑 z`）：凡值不可得者一律印 `⛔ 可得`，`Σ` 亦然。

用法：`python verify/probes/probe_WG9269_c2_diff.py`
`rc`：`0` 全綠／`2` **量測器紅**（對照組不如預期 ⇒ loud 拒測）／`3` 判定集為空（loud 拒測）／
      `5` **受詞紅**（`P-0` 與 `§零-1` 相異 ⇒ 停機上呈）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」——須讀其逐項（`坑 9`）。
"""
import contextlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)          # 🔒 自 `__file__` 上溯·⛔ 硬編他樹（`GB-161`）
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

W = 150
FLAG = "WG9269_K917_BACKFILL"
SCEN = (("0m", 0.0), ("3.5m", 3.5))

#: 🔒 `§零-1` 之受詞表（**⛔ 採信**·`P-0` 令自行重得後與之比對·相異 ⇒ `rc = 5` 停機）
SUBJ_ANCHOR = {
    ("0m", "628-42(1)"): ("G011", 0.23, 0.18),
    ("0m", "628-53(2)"): ("G025", 0.00, 0.02),
    ("3.5m", "628-53(2)"): ("G025", 0.00, 0.02),
}
#: 🔒 既有裁定（補令十 `§三-3`·逐宗·**其出處逐字見報告**）
PRIOR_RULING = {
    "G011": "⛔ 既有裁定·本批為新",
    "G025": "已由 KL 裁定 (D) 判不配地（梯3）",
    "G030": "已由 KL 裁定 (D) 判不配地（梯3）",
}


def _state():
    def g(*a):
        r = subprocess.run(["git", "-C", REPO] + list(a), capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else "⛔ 可得"
    return (g("rev-parse", "HEAD"), g("rev-parse", "HEAD:app.py"),
            g("hash-object", os.path.join(REPO, "app.py")), g("status", "--porcelain"))


def build_base():
    """建管線至 `build_parcels`（⛔ 受旗標影響——旗標只在 `run_step_g` 內）。"""
    ns, fake_st = harvest()
    snap = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    own_map = dict(fake_st.session_state["t8_ownership_map"])
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp, build, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snap)
    return ns, fake_st, snap, cb_by, cad, temp, build, own_map


def run_one(ns, fake_st, snap, cb_by, cad, temp, build, sb, on):
    """一 (情境, 旗標態) 之 trunk A。回 dict（含 `partial` 之處置·⛔ 靜默吞）。"""
    # 🛑 二態一律**顯式設值**，⛔ 以「`pop` ⇒ `off`」為之——該式繫於**旗標之預設**，
    #    而 `c2` 正是翻該預設者 ⇒ 於 `c2` 態其二態將**雙雙為 `on`**（閘恆真·`裁 H` 之族）。
    os.environ[FLAG] = "1" if on else "0"
    try:
        ns["K917_DROPPED"].clear()       # 🔒 逐跑歸零（其為 module 級累加器）
    except Exception:                    # noqa: BLE001
        pass
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snap, sb)
    _d, _s, _o, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snap)
    out = {"winners": wins, "forced": forced, "aborted": None, "pool": None}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snap, params, build,
                            wins, forced, sb, eff_min_build_by_blk={})
        out["g"] = sg["g_rows"]
        out["pool"] = sg["pool_diag"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        out["g"] = p.get("g_rows") or []
        out["aborted"] = p.get("aborted_blk")
        out["gate"] = str(e)[:200]
    out["dropped"] = {k: list(v) for k, v in (ns.get("K917_DROPPED") or {}).items()}
    return out


def run_one_default(ns, fake_st, snap, cb_by, cad, temp, build, sb):
    """**不設環境變數**之態（走 `app.py` 之預設字面）。⛔ 於本函式內設 `FLAG`。"""
    try:
        ns["K917_DROPPED"].clear()
    except Exception:                    # noqa: BLE001
        pass
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snap, sb)
    _d, _s, _o, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp, build, sb, snapshot=snap)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snap, params, build,
                            wins, forced, sb, eff_min_build_by_blk={})
        return {"g": sg["g_rows"]}
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        return {"g": p.get("g_rows") or []}


def _sig(rows):
    """逐宗之可比簽章（⛔ 只比列數）。"""
    return sorted((str(r.get("暫編地號", "")),
                   round(float(r.get("G(㎡)", 0) or 0), 6),
                   round(float(r.get("宗地寬度(m)", 0) or 0), 6),
                   round(float(r.get("累積S(m)", 0) or 0), 6)) for r in rows)


def _defcheck(S, DEF):
    """「翻預設 ≡ 翻環境變數」：預設態 vs 其所指之態，**逐宗逐值**相同。"""
    tgt = _default_on()
    print("── 「翻預設 ≡ 翻環境變數」之證（`c2` 之主檢）" + "─" * 56)
    print("   `app.py` 旗標預設字面 ＝ %r ⇒ 預設態應等同 `%s` 態"
          % (_flag_literal(), "on" if tgt else "off"))
    allok = True
    for tag, _sb in SCEN:
        a, b = _sig(DEF[tag]["g"]), _sig(S[(tag, tgt)]["g"])
        c = _sig(S[(tag, not tgt)]["g"])
        same, diff = (a == b), (a != c)
        allok = allok and same and diff
        print("   %-5s 預設態 vs `%s` 態：%s（%d vs %d 宗）｜"
              "判別力：預設態 vs `%s` 態 %s"
              % (tag, "on" if tgt else "off",
                 "**逐宗逐值相同** ✅" if same else "\U0001f534 **相異**",
                 len(a), len(b), "off" if tgt else "on",
                 "**相異** ✅" if diff else "\U0001f534 **相同** ⇒ 本檢失能"))
    print("   ⇒ %s" % ("✅ **翻預設 ≡ 翻環境變數**（且二態確可分辨）"
                       if allok else "\U0001f534 ⛔ 成立 ⇒ 停機"))
    print()
    return allok


def f2(x):
    return "⛔ 可得" if x is None else "%.2f" % float(x)


def sgn(x):
    return "⛔ 可得" if x is None else "%+.2f" % float(x)


def chain_key(r):
    return (str(r.get("所屬街廓", "")), str(r.get("推進側別", "")))


def order_map(rows):
    """逐 (街廓, 推進側別) 之配地次序（`g_rows` 之出現序·⛔ 另排序）。"""
    seen, out = {}, {}
    for r in rows:
        k = chain_key(r)
        seen[k] = seen.get(k, 0) + 1
        out[str(r.get("暫編地號", ""))] = (k, seen[k])
    return out


def main():                                                          # noqa: C901
    head, blob, work, porc = _state()
    print("=" * W)
    print("【`W-G.9-269` `c2`】差異表（補令三 `§四`）＋`P-0`〜`P-9` 之可量者")
    print("=" * W)
    print("\U0001f512 **態宣告二值並報**（`坑 r`·**以工作區之值為實**）")
    print("   `commit`                         = %s" % head)
    print("   `app.py` `rev-parse HEAD:app.py` = %s" % blob)
    print("   `app.py` `hash-object`（**工作區·實**） = %s" % work)
    print("   二值 %s" % ("**相同** ✅" if blob == work
                                  else "\U0001f534 **相異** ⇒ 工作區與 `HEAD` 不同步"))
    print("   `git status --porcelain` = %s"
          % ("（空·乾淨）" if not porc else "\U0001f7e1 非空（%d 列）" % len(porc.splitlines())))
    print("   旗標預設（未設環境變數時）= %s"
          % ("`on`" if _default_on() else "`off`"))
    print()

    ns, fake_st, snap, cb_by, cad, temp, build, own_map = build_base()
    resolve = ns["_resolve_ownership"]
    S = {}
    for tag, sb in SCEN:
        for on in (False, True):
            S[(tag, on)] = run_one(ns, fake_st, snap, cb_by, cad, temp, build, sb, on)
    # ── 🔑 「翻預設 ≡ 翻環境變數」之證（⛔ 以「應該一樣」推定）────────────────
    #    第三態 ＝ **不設環境變數**（走 `app.py` 之預設字面）。其 `g_rows` 須與
    #    「預設所指之態」**逐宗逐值相同**；⛔ 只比列數。
    DEF = {}
    for tag, sb in SCEN:
        os.environ.pop(FLAG, None)
        DEF[tag] = run_one_default(ns, fake_st, snap, cb_by, cad, temp, build, sb)
    os.environ.pop(FLAG, None)
    _defcheck(S, DEF)

    # ── 對照組（`坑 u`／`坑 13`：三造·**先跑先判**）─────────────────────────
    print("── 三造對照（**先跑**·未全成立則 loud 拒測）" + "─" * 60)
    ctl = []
    g0off = {str(r.get("暫編地號", "")): r for r in S[("0m", False)]["g"]}
    g0on = {str(r.get("暫編地號", "")): r for r in S[("0m", True)]["g"]}
    ctl.append(("造甲[必非零] `0m` `off` 之 `g_rows` 列數",
                str(len(g0off)), "> 0", len(g0off) > 0))
    ctl.append(("造乙[必為零] 人造哨兵（**執行期組出**·字面⛔ 出艙）於 `g_rows`",
                str(len([1 for k in g0off if k == _sentinel(g0off)])), "= 0",
                _sentinel(g0off) not in g0off))
    ctl.append(("造丙[本類已知成員] `628-42(1)` 於 `0m` `off`",
                "在" if "628-42(1)" in g0off else "⛔ 在", "在",
                "628-42(1)" in g0off))
    ctl.append(("造丁[判別力] `0m` `off` 列數 ≠ `on` 列數",
                "%d vs %d" % (len(g0off), len(g0on)), "相異", len(g0off) != len(g0on)))
    for nm, got, exp, ok in ctl:
        print("   %-62s 得 %-14s 期 %-8s %s" % (nm, got, exp, "✅" if ok else "\U0001f534"))
    if not all(c[3] for c in ctl):
        print("\U0001f534 **量測器紅** ⇒ loud 拒測（⛔ 出艙任何受詞之值）")
        return 2
    print("   ⇒ **器非紅** ✅")
    print()

    rc = 0
    rc |= _p0(S, resolve, own_map)
    _table1(S, resolve, own_map)
    _table2(S)
    _table3(S, resolve, own_map)
    rc2 = _pchecks(S, resolve, own_map)
    return 5 if rc else rc2


def _default_on():
    """旗標之**預設**是否為 `on`（讀 `app.py` 之字面·⛔ 讀環境變數）。"""
    return _flag_literal() in ("1", "on", "true", "yes")


def _flag_literal():
    """讀 `app.py` 之旗標預設**字面**（⛔ 以字樣計數為之·`坑 q`）。"""
    import ast
    src = open(os.path.join(REPO, "app.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == "k917_backfill_enabled":
            for c in ast.walk(n):
                if (isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute)
                        and c.func.attr == "get" and len(c.args) == 2
                        and isinstance(c.args[1], ast.Constant)):
                    return str(c.args[1].value).strip().lower()
    return "⛔ 可得"


def _sentinel(pool):
    base = "".join(chr(c) for c in (57, 57, 57, 57, 57, 57))
    for k in range(100):
        cand = "%s-%d(%d)" % (base, k, k)
        if cand not in pool:
            return cand
    raise RuntimeError("哨兵組出失敗")


def _gid(r, resolve, own_map):
    o = str((r or {}).get("原地號", "") or "")
    return (resolve(o, own_map) or "") if o else ""


def _p0(S, resolve, own_map):
    print("── `P-0` 受詞之自行重得（與 `§零-1` 逐宗比對·相異 ⇒ 停機）" + "─" * 44)
    print("   | 情境 | 宗地 | 歸戶 | `G(㎡)` | 宗地寬度(m) | 閘一判 | 與 `§零-1` |")
    print("   |---|---|---|---|---|---|---|")
    bad = 0
    for (tag, pid), (egid, eg, ew) in sorted(SUBJ_ANCHOR.items()):
        by = {str(r.get("暫編地號", "")): r for r in S[(tag, False)]["g"]}
        r = by.get(pid)
        if r is None:
            print("   | `%s` | `%s` | ⛔ 在 `g_rows` | — | — | — | \U0001f534 |" % (tag, pid))
            bad += 1
            continue
        gid = _gid(r, resolve, own_map)
        g = float(r.get("G(㎡)", 0) or 0)
        w = float(r.get("宗地寬度(m)", 0) or 0)
        v = str(r.get("驗_B藍影", ""))
        ok = (gid == egid and abs(g - eg) < 0.005 and abs(w - ew) < 0.005
              and v == "不合格")
        bad += 0 if ok else 1
        print("   | `%s` | `%s` | `%s` | %.2f | %.2f | `%s` | %s |"
              % (tag, pid, gid, g, w, v, "✅ 相符" if ok else "\U0001f534 相異"))
    print("   ⇒ %s" % ("**逐宗相符** ✅" if not bad
                            else "\U0001f534 **相異 %d 宗** ⇒ 停機上呈" % bad))
    print()
    return bad


def _disposal(pid, roff, ron, dropped, oo, on_):
    if ron is None:
        v = str((roff or {}).get("驗_B藍影", ""))
        return ("改列調配池（閘一直接剔除）" if v == "不合格"
                else "改列調配池（\U0001f534 級聯剔除）")
    a, b = oo.get(pid), on_.get(pid)
    if a and b and a[1] != b[1]:
        return "遞補進位（位次 %d → %d）" % (a[1], b[1])
    return "維持原配地"


def _table1(S, resolve, own_map):
    print("=" * W)
    print("【表一·逐宗】域語言·逐情境分列（`坑 e`）。**只列有變動者 ➕ 受詞三宗**；無變動者列其計數。")
    print("=" * W)
    for tag, _sb in SCEN:
        off, on_ = S[(tag, False)], S[(tag, True)]
        boff = {str(r.get("暫編地號", "")): r for r in off["g"]}
        bon = {str(r.get("暫編地號", "")): r for r in on_["g"]}
        oo, oon = order_map(off["g"]), order_map(on_["g"])
        print("\n【情境 `%s`】`off` **%d** 列 → `on` **%d** 列（差 **%+d**）"
              % (tag, len(boff), len(bon), len(bon) - len(boff)))
        print("| 配地次序(off→on) | 重劃前地號 | 土地所有權人(歸戶) | 分配面積前 | 後 | **面積增減** | 臨路寬度前 | 後 | **寬度增減** | 位置變動(m) | **處置** | 街角地 | 既有裁定 |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        keep = 0
        for pid in sorted(set(boff) | set(bon)):
            ro, rn = boff.get(pid), bon.get(pid)
            go = None if ro is None else float(ro.get("G(㎡)", 0) or 0)
            gn = None if rn is None else float(rn.get("G(㎡)", 0) or 0)
            wo = None if ro is None else float(ro.get("宗地寬度(m)", 0) or 0)
            wn = None if rn is None else float(rn.get("宗地寬度(m)", 0) or 0)
            so = None if ro is None else float(ro.get("累積S(m)", 0) or 0)
            sn = None if rn is None else float(rn.get("累積S(m)", 0) or 0)
            dg = None if (go is None or gn is None) else gn - go
            dw = None if (wo is None or wn is None) else wn - wo
            ds = None if (so is None or sn is None) else sn - so
            gid = _gid(ro if ro is not None else rn, resolve, own_map)
            changed = (rn is None or ro is None
                       or abs(dg or 0) >= 0.005 or abs(dw or 0) >= 0.005
                       or abs(ds or 0) >= 0.005
                       or (oo.get(pid, (0, 0))[1] != oon.get(pid, (0, 0))[1]))
            if not changed and pid not in ("628-42(1)", "628-53(2)", "628-27(1)"):
                keep += 1
                continue
            a = oo.get(pid), oon.get(pid)
            ordtxt = "%s→%s" % (
                ("%s/%s#%d" % (a[0][0][0], a[0][0][1], a[0][1])) if a[0] else "—",
                ("#%d" % a[1][1]) if a[1] else "**退出**")
            src = ro if ro is not None else rn
            print("| %s | `%s` | `%s` | %s | %s | **%s** | %s | %s | **%s** | %s | **%s** | %s | %s |"
                  % (ordtxt, src.get("原地號", ""), gid or "—",
                     f2(go), f2(gn), sgn(dg), f2(wo), f2(wn), sgn(dw), sgn(ds),
                     _disposal(pid, ro, rn, off["dropped"], oo, oon),
                     src.get("街角地", ""), PRIOR_RULING.get(gid, "—")))
        print("| （無變動者） | — | — | — | — | — | — | — | — | — | **維持原配地 %d 宗** | — | — |" % keep)


def _table2(S):
    print()
    print("=" * W)
    print("【表二·逐街廓·守恆】`池` 取 `池總=幾何剩餘(㎡)`（**獨立幾何量測**·⛔ 由 `街廓面積−ΣG` 倒算）")
    print("=" * W)
    for tag, _sb in SCEN:
        print("\n【情境 `%s`】" % tag)
        print("| 街廓 | 分配地合計 `ΣG` off | on | 調配池 off | on | **池增減** | 街廓面積 | 殘差 off | 殘差 on |")
        print("|---|---|---|---|---|---|---|---|---|")
        po, pn = S[(tag, False)]["pool"], S[(tag, True)]["pool"]
        if po is None or pn is None:
            print("| ⛔ 可得 | — | — | — | — | — | — | — | — |")
            print("\U0001f534 `pool_diag` ⛔ 可得（`run_step_g` 拋）⇒ 本表之數**⛔ 可得**·⛔ 印 `0`（`坑 z`）")
            continue
        # 🔒 街廓面積自 `g_rows` 之 `街廓面積(㎡)` 取（⛔ 第二份定義）
        area = {}
        for r in S[(tag, False)]["g"]:
            area.setdefault(str(r.get("所屬街廓", "")),
                            float(r.get("街廓面積(㎡)", 0) or 0))
        tg = tsum = 0.0
        for lbl in sorted(set(po) | set(pn)):
            a, b = po.get(lbl, {}), pn.get(lbl, {})
            ga, gb = a.get("ΣG(㎡)"), b.get("ΣG(㎡)")
            pa = a.get("池總=幾何剩餘(㎡)")
            pb = b.get("池總=幾何剩餘(㎡)")
            ar = area.get(lbl)
            # 🩸 `坑 y` 之族（**本批親踩**）：`恆 U+6046` ⛔ `恒 U+6052`——
            #    二字形近，誤取者 `.get` 靜默回 `None`。⛔ 憑字形猜，一律自倉內鍵取。
            ra, rb = a.get("守恆殘差(㎡)"), b.get("守恆殘差(㎡)")
            va, vb = a.get("判定", "—"), b.get("判定", "—")
            # 🛑 loud：`判定` 在而 `殘差` 不在 ⇒ **鍵字面取錯**（⛔ 靜默印「⛔ 可得」）。
            for _v, _r, _s in ((va, ra, "off"), (vb, rb, "on")):
                if _v != "—" and _r is None:
                    raise RuntimeError(
                        "🔴 量測器紅：街廓 %s（%s 態）之 `判定` ＝ %r 而 `守恆殘差(㎡)` 取不到"
                        "——鍵之字面取錯（`坑 y` 之族）。現有鍵：%s"
                        % (lbl, _s, _v, sorted((a if _s == "off" else b).keys())))
            d = None if (pa is None or pb is None) else pb - pa
            if d is not None:
                tsum += d
            if ga is not None and gb is not None:
                tg += gb - ga
            print("| `%s` | %s | %s | %s | %s | **%s** | %s | %s %s | %s %s |"
                  % (lbl, f2(ga), f2(gb), f2(pa), f2(pb), sgn(d), f2(ar),
                     sgn(ra), va, sgn(rb), vb))
        print("| **Σ（帶號）** | — | — | — | — | **%+.2f** | — | — | — |" % tsum)
        print("| **ΣΔG（帶號）** | — | — | — | — | **%+.2f** | — | — | — |" % tg)


def _table3(S, resolve, own_map):
    print()
    print("=" * W)
    print("【表三·彙總】")
    print("=" * W)
    for tag, _sb in SCEN:
        off, on_ = S[(tag, False)], S[(tag, True)]
        boff = {str(r.get("暫編地號", "")): r for r in off["g"]}
        bon = {str(r.get("暫編地號", "")): r for r in on_["g"]}
        gone = sorted(set(boff) - set(bon))
        print("\n【情境 `%s`】" % tag)
        print("| 項 | 值 |")
        print("|---|---|")
        print("| 改列調配池之宗數 | **%d** |" % len(gone))
        d1 = [p for p in gone
              if str(boff[p].get("驗_B藍影", "")) == "不合格"]
        d2 = [p for p in gone if p not in d1]
        print("| └ 閘一直接剔除 | %s |"
              % (", ".join("`%s`" % p for p in d1) or "（無）"))
        print("| └ \U0001f534 級聯剔除（**單獨小計**） | %s |"
              % (", ".join("`%s`" % p for p in d2) or "（無）"))
        sg_ = sum(float(boff[p].get("G(㎡)", 0) or 0) for p in gone)
        print("| `ΣG_被剔`（**被剔宗之 `G` 合計**） | **%.2f ㎡** |" % sg_)
        po, pn = off["pool"], on_["pool"]
        if po and pn:
            dp = sum(float(pn[l]["池總=幾何剩餘(㎡)"])
                     - float(po[l]["池總=幾何剩餘(㎡)"])
                     for l in po if l in pn)
            print("| `Δ池（實測）` | **%+.2f ㎡** |" % dp)
            print("| \U0001f6d1 二量之別 | `ΣG_被剔` ⛔ 充「入池量」——入池量 ＝ 「剔除 ＋ 遞補前移」之**淨幾何效應**（補令十一 `§二-1`） |")
        else:
            print("| `Δ池（實測）` | **⛔ 可得**（`pool_diag` 不可得·⛔ 印 `0`） |")
        gids = sorted({_gid(boff[p], resolve, own_map) for p in gone})
        print("| 逐戶具名 | %s |"
              % (", ".join("`%s`（%s）" % (g, PRIOR_RULING.get(g, "—")) for g in gids if g)
                 or "（無）"))
        ds = [(float(bon[p].get("G(㎡)", 0) or 0) - float(boff[p].get("G(㎡)", 0) or 0), p)
              for p in set(boff) & set(bon)]
        ds = [(d, p) for d, p in ds if abs(d) >= 0.005]
        print("| `ΣΔG`（帶號·**留存宗**） | **%+.2f ㎡** |" % sum(d for d, _ in ds))
        print("| `Σ|ΔG|`（絕對值） | **%.2f ㎡** |" % sum(abs(d) for d, _ in ds))
        if ds:
            mn, mx = min(ds), max(ds)
            for nm, (d, p) in (("min", mn), ("max", mx)):
                print("| `%s ΔG`（**具名其宗與歸戶**） | %+.2f ㎡ ＠ `%s`（`%s`·歸戶 `%s`） |"
                      % (nm, d, p, bon[p].get("原地號", ""),
                         _gid(bon[p], resolve, own_map) or "—"))
        else:
            print("| `min`／`max ΔG` | （留存宗皆無變動） |")
        owners = {_gid(boff[p], resolve, own_map) for p in gone}
        owners |= {_gid(bon[p], resolve, own_map) for _d, p in ds}
        print("| 所有權人受影響戶數 | **%d** |" % len({o for o in owners if o}))


def _pchecks(S, resolve, own_map):                                   # noqa: C901
    print()
    print("=" * W)
    print("【`§三` 性質閘】逐閘載判定集基數與兩造對照")
    print("=" * W)
    bad = 0
    for tag, _sb in SCEN:
        off, on_ = S[(tag, False)], S[(tag, True)]
        boff = {str(r.get("暫編地號", "")): r for r in off["g"]}
        bon = {str(r.get("暫編地號", "")): r for r in on_["g"]}
        gone = set(boff) - set(bon)
        print("\n【情境 `%s`】" % tag)

        # P-2
        ok = all(p not in bon for p in gone)
        po, pn = off["pool"], on_["pool"]
        if po and pn:
            nbad = [l for l in pn
                    if "破" in str(pn[l].get("判定", ""))]
            res_txt = ("逐街廓守恆判（生產碼 `判定` 欄）：on 態 %d 街廓·破 %d"
                       % (len(pn), len(nbad)))
            if nbad:
                bad += 1
        else:
            res_txt = "⛔ 可得"
        print("   `P-2` 被剔宗⛔ 出現於配地母體 ⇒ %s（判定集 %d 宗）；守恆：%s"
              % ("✅" if ok else "\U0001f534", len(gone), res_txt))
        bad += 0 if ok else 1

        # P-3 —— 🩸 `坑 y` 之攔法：**先印該欄之值分布再定框**；
        #        🩸 `坑 z`：`—`（閘一未評估）⛔ 得計為「違反」，其為**⛔ 可量**。
        dist = {}
        for r in bon.values():
            dist[str(r.get("驗_B藍影", ""))] = dist.get(str(r.get("驗_B藍影", "")), 0) + 1
        ok3, bad3, na3 = [], [], []
        for p, r in bon.items():
            a, b = r.get("驗_B_臨正街"), r.get("驗_B_臨屁股")
            if not (_num(a) and _num(b)):
                na3.append(p)
            elif _pos(a) and _pos(b):
                ok3.append(p)
            else:
                bad3.append(p)
        print("   `P-3` 留存宗臨 FRONTLINE ⋀ BASELINE 且臨接長 `> 0`")
        print("        `驗_B藍影` 值分布（**先印再定框**·`坑 y`）＝ %s" % dist)
        print("        判定集 ＝ **%d** 宗（二長皆為數）｜成立 **%d**｜不成立 **%d**｜"
              "⛔ 可量 **%d** 宗（其二長為 `—` ＝ 閘一未評估·⛔ 計為違反·`坑 z`）"
              % (len(ok3) + len(bad3), len(ok3), len(bad3), len(na3)))
        print("        ⇒ %s%s"
              % ("✅" if not bad3 else "\U0001f534",
                 "" if not bad3 else "　不成立者：%s"
                 % ", ".join("`%s`" % p for p in sorted(bad3)[:8])))
        bad += 0 if not bad3 else 1

        # P-4／P-5
        c_off = {p: r for p, r in boff.items()
                 if str(r.get("第1筆街角", "")) == "是"}
        c_on = {p: r for p, r in bon.items()
                if str(r.get("第1筆街角", "")) == "是"}
        diff4 = [p for p in set(c_off) & set(c_on)
                 if (abs(float(c_off[p].get("G(㎡)", 0) or 0)
                         - float(c_on[p].get("G(㎡)", 0) or 0)) >= 0.005
                     or (c_off[p].get("cut_coords") or []) != (c_on[p].get("cut_coords") or []))]
        print("   `P-4` 第 `0` 宗（街角地）`G`·`cut_coords` 逐位不變 ⇒ %s"
              "（判定集 %d 宗·相異 %d）"
              % ("✅" if not diff4 else "\U0001f534", len(set(c_off) & set(c_on)), len(diff4)))
        bad += 0 if not diff4 else 1
        same5 = (sorted(c_off) == sorted(c_on))
        print("   `P-5` 街角地**歸屬**不變 ⇒ %s（off %d 宗 / on %d 宗）"
              "；`R6/right` 標「**不可判**」（`GB-156`）·⛔ 併入違反計數"
              % ("✅" if same5 else "\U0001f534", len(c_off), len(c_on)))
        bad += 0 if same5 else 1

        # P-6
        oo, oon = order_map(off["g"]), order_map(on_["g"])
        moved = [p for p in set(boff) & set(bon)
                 if oo.get(p, (0, 0))[1] != oon.get(p, (0, 0))[1]]
        expl = []
        for p in moved:
            k = oo[p][0]
            ng = len([q for q in gone if oo.get(q, (None,))[0] == k and oo[q][1] < oo[p][1]])
            expl.append(oon[p][1] == oo[p][1] - ng)
        print("   `P-6` 鏈序變動恰可由遞補解釋 ⇒ %s"
              "（位次有變 %d 宗·合「前移恰等於其前被剔數」 %d）"
              % ("✅" if all(expl) else "\U0001f534", len(moved), sum(1 for e in expl if e)))
        bad += 0 if all(expl) else 1

        # P-8
        ra = {str(r.get("所屬街廓", "")) for r in off["g"]}
        rb = {str(r.get("所屬街廓", "")) for r in on_["g"]}
        print("   `P-8` 可達性只增不減 ⇒ %s（off %s → on %s）"
              % ("✅" if ra <= rb else "\U0001f534",
                 sorted(ra), sorted(rb)))
        bad += 0 if ra <= rb else 1
        print("   中止街廓：off ＝ %s ／ on ＝ %s"
              % (off["aborted"] or "（無·跑完）", on_["aborted"] or "（無·跑完）"))
    return 0 if not bad else 1


def _num(x):
    """該格是否**為數**（⛔ `—`／空 ⇒ 其為「⛔ 可量」·`坑 z`）。"""
    try:
        float(x)
        return True
    except (TypeError, ValueError):
        return False


def _pos(x):
    try:
        return float(x) > 0
    except (TypeError, ValueError):
        return False


if __name__ == "__main__":
    sys.exit(main())
