# -*- coding: utf-8 -*-
"""`W-G.9-269` `c4` `§三-(b)` 之**另診**：閘 `γ` 仍不過之成因（`GB-160` 所令）。

🛑 `GB-160` 逐字：「**仍不過 ⇒ 成因⛔ 在退化幾何，須另診並具名**」
   ⇒ 本器之受詞 ＝ **成因之鑑別**，⛔ 閘之判（該判已由 `probe_WG9269_c4_gamma.py` 出艙）。

🔑 **鑑別之法（⛔ 只看受詞二側·否則⛔ 有對照）**：掃**全 `6` 街廓 × `2` 側 ＝ `12` 側**，
   逐失敗對具名其二宗之 `街角地`／`第1筆街角`／`G`／`宗地寬度`，
   使「退化幾何」與「街角界面」二假說**可被資料分開**：
     `H1` 退化幾何 ⇒ 失敗對必含一**近乎零**之宗；
     `H2` 街角界面 ⇒ 失敗對必含一**街角地**（第 `0` 宗 ↔ 第 `1` 宗之界面）。
   🛑 二假說**⛔ 互斥** ⇒ 須逐對判其各自之在否，**⛔ 擇一而不言其二**。

🔒 判準之來源 ＝ 倉內既有 `V1.side_rows`／`V1.shared_edge`（逐字·⛔ 改一字）。
🔒 資料源 ＝ **記憶體側**生產管線（同 `probe_WG9269_c4_gamma.py`·⛔ 落檔·⛔ baseline）。

用法：`python verify/probes/probe_WG9269_c4_gamma_diag.py [倉根]`
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
import probe_WG9266_V1prime_3groups as V1                           # noqa: E402
import probe_WG9269_c4_gamma as G4                                  # noqa: E402

BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
SIDES = ["left", "right"]
NEAR_ZERO = 5.0          # 🔒 「近乎零」之界：`GB-159` 受詞二宗為 `0.23`／`0.00`；
                         #    `GB-160` 所疑之 `628-53(1)` 為 `0.26` ⇒ 取 `5.0 ㎡` 為寬界（**保守**）


def drive(sb):
    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return rows


def attrs(rows, blk, side, lot):
    for r in rows:
        if ((r.get("所屬街廓") or "").strip() == blk
                and (r.get("推進側別") or "").strip() == side
                and (r.get("暫編地號") or "").strip() == lot):
            return {"街角": (r.get("街角地") or "").strip(),
                    "第1筆街角": (r.get("第1筆街角") or "").strip(),
                    "G": float(r.get("G(㎡)") or 0),
                    "W": (r.get("宗地寬度(m)") or "").strip()}
    return None


def main():
    print("=" * 118)
    print("【`W-G.9-269` `c4` `§三-(b)` 另診】閘 `γ` 仍不過之**成因鑑別**（全 `12` 側·情境 `3.5m`）")
    print("=" * 118)
    rows = drive(3.5)
    print("🔒 母體 ＝ 記憶體側 `g_rows` **%d** 列（⛔ 落檔·⛔ baseline·`GB-162`）" % len(rows))
    print("🔒 判準 ＝ `V1.shared_edge`（逐字）｜「近乎零」之界 ＝ `G < %.1f ㎡`（保守·具名）" % NEAR_ZERO)
    print()
    print("── 全 `12` 側之閘 `γ` ──")
    print("   %-14s %-8s %-10s %-10s %s" % ("側", "宗數", "相鄰對數", "閘 γ", "判"))
    fails = []
    npass = nfail = nempty = 0
    for b in BLKS:
        for s in SIDES:
            ng, npair, detail, nlot = G4.gamma(rows, b, s)
            if npair == 0:
                nempty += 1
                tag = "🛑 母體 0（⛔ 靜默綠）"
            elif ng == npair:
                npass += 1
                tag = "✅ 過"
            else:
                nfail += 1
                tag = "🔴 不過"
                for a, c, n in detail:
                    if n != 2:
                        fails.append((b, s, a, c, n))
            print("   %-14s %-8d %-10d %-10s %s"
                  % ("%s·%s" % (b, s), nlot, npair, "%d/%d" % (ng, npair), tag))
    print()
    print("   ⇒ 全過 **%d** 側／不過 **%d** 側／母體 `0` **%d** 側（合計 %d）"
          % (npass, nfail, nempty, npass + nfail + nempty))
    print("   🔒 判別力：**⛔ 恆紅**（有 %d 側全過）亦**⛔ 恆綠**（有 %d 側不過）" % (npass, nfail))
    print()

    print("── 失敗對之逐對具名（`H1` 退化幾何 vs `H2` 街角界面）──")
    print("   %-12s %-20s %-20s %-6s %-26s %-26s %s"
          % ("側", "宗 A", "宗 B", "共用", "A（街角／G／寬）", "B（街角／G／寬）", "假說"))
    h1 = h2 = both = neither = 0
    for b, s, a, c, n in fails:
        pa, pb = attrs(rows, b, s, a), attrs(rows, b, s, c)
        def fmt(p):
            if p is None:
                return "⛔ 可得"
            return "%s／%.2f／%s" % (p["街角"] or "否", p["G"], p["W"])
        isH1 = any(p is not None and p["G"] < NEAR_ZERO for p in (pa, pb))
        isH2 = any(p is not None and p["街角"] == "是" for p in (pa, pb))
        if isH1 and isH2:
            lab = "H1 ⋀ H2"; both += 1
        elif isH1:
            lab = "**H1**（退化）"; h1 += 1
        elif isH2:
            lab = "**H2**（街角）"; h2 += 1
        else:
            lab = "🔴 **皆⛔**"; neither += 1
        print("   %-12s %-20s %-20s %-6d %-26s %-26s %s"
              % ("%s·%s" % (b, s), a, c, n, fmt(pa), fmt(pb), lab))
    print()
    print("   ⇒ 失敗對 **%d** 個：僅 `H1` **%d**／僅 `H2` **%d**／`H1 ⋀ H2` **%d**／**皆⛔** **%d**"
          % (len(fails), h1, h2, both, neither))
    print()
    print("── 反面對照（⛔ 只看失敗對·否則假說⛔ 可否證）──")
    ncorner_ok = nzero_ok = 0
    for b in BLKS:
        for s in SIDES:
            _ng, _np, detail, _nl = G4.gamma(rows, b, s)
            for a, c, n in detail:
                if n != 2:
                    continue
                pa, pb = attrs(rows, b, s, a), attrs(rows, b, s, c)
                if any(p is not None and p["街角"] == "是" for p in (pa, pb)):
                    ncorner_ok += 1
                if any(p is not None and p["G"] < NEAR_ZERO for p in (pa, pb)):
                    nzero_ok += 1
    print("   含**街角地**而 `γ` **通過**之對 ＝ **%d** ⇒ %s"
          % (ncorner_ok, "🔴 `H2` 之「街角必敗」被否證" if ncorner_ok else "✅ `H2` 未被否證"))
    print("   含**近乎零之宗**而 `γ` **通過**之對 ＝ **%d** ⇒ %s"
          % (nzero_ok, "🔴 `H1` 之「退化必敗」被否證" if nzero_ok else "✅ `H1` 未被否證"))
    print("=" * 118)
    return 0


if __name__ == "__main__":
    sys.exit(main())
