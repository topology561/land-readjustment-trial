# -*- coding: utf-8 -*-
"""`W-G.9-268′` 補令九 序 `1′`：`§三-2` 人造擾動之判別力驗 ＋ `§三-3` 款 `(2)` 逐側鏈序。

🔒 **判準之來源 ＝ 倉內既有** `probe_WG9266_V1prime_3groups`（下稱 `V1`）——**只換資料源**，
   `shared_edge`／`s_of_line`／`measure`／`gates`／`run`（含五款判準與 `1e-6`）**一字不動**。
🛑 **⛔ 調框以就結果**（`VR-094` 二）；擾動之量**固定 `1e-3 m`**（補令九 `§三-2` 明令）。

────────────────────────────────────────────────────────────────────────
🩸 **補令九 `§三-2` 之字面與本器之二處結構性不相容（`常規二`·逐字回報·⛔ 靜默改）**

單之字面：「將其**一宗**之 `cut_coords` 沿 `d̂` 平移 `1e-3 m` …… `(1b)` 與 `(3)` 須轉紅、`(5)` 須 `> 0`」。

`(甲)` **閘 `γ` 必先不過**：`V1.shared_edge` 以 `QK = 1e-6` 認共用頂點；
      單獨平移一宗 `1e-3 m`（`> QK` 三個量級）⇒ 該宗與其鄰宗**⛔ 再有共用頂點**
      ⇒ 閘 `γ` 由 `n/n` 轉為缺 `1`〜`2` 對 ⇒ `V1.run` **回 `refuse`（⛔ 回紅）**。
      ⇒ 「不轉紅 ⇒ 閘失能」之判**⛔ 適用**——其未轉紅之因係**拒測**、⛔ 不敏感。
`(乙)` **`(5)` 結構上⛔ 可能 `> 0`**：`(5)` 之受詞為 `ΔG ＝ B['G(㎡)'] − A['G(㎡)']`，
      取自**列之欄位**；而剛體平移**⛔ 動該欄** ⇒ `ΔG ≡ 0` ⇒ `(5) ≡ 0`。

🔒 **本器之處置（`常規二`：取保守項續辦 ＋ 逐字回報）**
   **二式並跑、二式皆出艙**，量級**固定 `1e-3 m`**、判準**一字不動**：
   **式 `甲`（單之字面）**：單獨平移一宗 ⇒ 照實出艙其結果（預期：閘 `γ` 拒測）。
   **式 `乙`（保守項）**：平移**一條共用界線之二頂點**（於**相鄰二宗內同步**移動，使共用邊仍恰 `2` 頂點）
     ＋ 將該二宗之 `G(㎡)` 欄改設為其**擾動後之多邊形面積**（使閘 `β` 仍過、且 `ΔG ≠ 0`）。
     ⇒ 其為「**本器看得見之 `1e-3 m` 擾動**」，⛔ 調判準、⛔ 調容差、⛔ 調量級。
   🛑 **式 `乙` 係<u>擾動之施加方式</u>之更改，⛔ 判準之更改**；其是否採為正式判別力，**候發單側**。
────────────────────────────────────────────────────────────────────────

用法：`python verify/probes/probe_WG9268p_c2_v1prime_pert.py [倉根]`
"""
import contextlib
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from shapely.geometry import Polygon                                # noqa: E402

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

import probe_WG9266_V1prime_3groups as V1                           # noqa: E402

FLAG = "WG9268P_ANCHOR_GEOM"
SCEN = (("0m", 0.0), ("3.5m", 3.5))
PERT = 1e-3                 # 🛑 固定（補令九 §三-2）·⛔ 調至恰好轉紅
GRP = ("R2", "left")        # `V-1′-a` 三組之一（`3.5m·R2·left`）
ROWS = {}
FAIL = []


def _load(root):
    return ROWS[root]


def to_csv_like(g_rows):
    out = []
    for r in g_rows:
        cc = r.get("cut_coords")
        s = cc if isinstance(cc, str) else (repr([[float(a), float(b)] for a, b in cc]) if cc else "")
        out.append({k: (s if k == "cut_coords" else ("" if v is None else str(v)))
                    for k, v in r.items()})
    return out


def drive(setback, mode, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p):
    os.environ[FLAG] = "1" if mode == "on" else "0"
    try:
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d, _s, _off, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        g_rows, aborted = [], None
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                                 params, build_p, wins, forced, setback,
                                 eff_min_build_by_blk={})
            g_rows = _sg["g_rows"]
        except RuntimeError as e:
            p = getattr(e, "partial", None) or {}
            g_rows = p.get("g_rows") or []
            aborted = p.get("aborted_blk")
    finally:
        os.environ.pop(FLAG, None)
    return g_rows, aborted


def dhat(fl, blk):
    p1, p2 = fl[blk]["p1"], fl[blk]["p2"]
    L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    return ((p2[0] - p1[0]) / L, (p2[1] - p1[1]) / L)


def side_idx(rows, blk, side):
    ix = [i for i, r in enumerate(rows)
          if (r.get("所屬街廓") or "").strip() == blk
          and (r.get("推進側別") or "").strip() == side
          and (r.get("cut_coords") or "").strip()]
    ix.sort(key=lambda i: float(rows[i].get("累積S(m)") or 0))
    return ix


def cc_of(row):
    import ast
    return [(float(a), float(b)) for a, b in ast.literal_eval(row["cut_coords"])]


def main():                                                         # noqa: C901
    print("=" * 118)
    print("【`W-G.9-268′` 補令九 序 `1′`】人造擾動之判別力 ＋ 款 `(2)` 逐側鏈序")
    print("=" * 118)
    print("🔒 判準來源 ＝ 倉內既有 `V1`（只換資料源·五款與 `1e-6` 一字不動）")
    print("🔒 `V1.TOL_K1` ＝ %g／`V1.TOL_K3` ＝ %g（自該模組現讀）｜擾動量固定 ＝ %g m"
          % (V1.TOL_K1, V1.TOL_K3, PERT))
    print()

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl = cad["front_lines"]

    ST = {}
    for tag, sb in SCEN:
        for mode in ("off", "on"):
            g, ab = drive(sb, mode, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p)
            ST[(tag, mode)] = (to_csv_like(g), ab)
            print("🔒 [%-4s／%-3s] `g_rows` **%d** 列（母體基數）／中止 %s"
                  % (tag, mode, len(ST[(tag, mode)][0]), ab or "無"))
    print()
    V1.load = _load
    # 🔑 `V-1′` 三組之受詞逐字皆為 `3.5m` ⇒ 其比較端之 `OFF` 亦取 `3.5m`（⛔ 混情境）
    ROWS["OFF"] = ST[("3.5m", "off")][0]
    print("🔒 `V-1′` 之比較端 `OFF` ＝ `3.5m`／`off`（**%d** 列）⇒ ⛔ 混入 `0m` 之列"
          % len(ROWS["OFF"]))
    print()

    # ══ §三-3　款 `(2)` 逐側鏈序 ═══════════════════════════════════
    print("=" * 118)
    print("【`§三-3`】`V-1′-b` 款 `(2)`：逐側**鏈序不變**（⛔ 需共用邊框·直接比對序列）")
    print("=" * 118)
    print("🔒 **已動／未動之判⛔ 用 `cut_coords` 逐位相異**（`§三-1` 明令：末位浮點差⛔ 真實位移）")
    print("   改用**無框可得**之二量：全側 `|ΔG|max` 與 `max|Δ累積S|`（皆 `> 1e-6` 方判已動）")
    print()
    tot = moved = 0
    only_on = []
    for tag, _sb in SCEN:
        ro, _ao = ST[(tag, "off")]
        rn, _an = ST[(tag, "on")]
        so = {}
        sn = {}
        for src, dst in ((ro, so), (rn, sn)):
            for r in src:
                k = ((r.get("所屬街廓") or "").strip(), (r.get("推進側別") or "").strip())
                if k[1] == "抵費地" or not (r.get("cut_coords") or "").strip():
                    continue
                dst.setdefault(k, []).append(r)
        for k in sorted(set(so) | set(sn)):
            if k not in so or k not in sn:
                only_on.append((tag, k))
                continue
            a = sorted(so[k], key=lambda r: float(r.get("累積S(m)") or 0))
            b = sorted(sn[k], key=lambda r: float(r.get("累積S(m)") or 0))
            ida = [(r.get("暫編地號") or "").strip() for r in a]
            idb = [(r.get("暫編地號") or "").strip() for r in b]
            qa = [(r.get("驗_宗序") or "").strip() for r in a]
            qb = [(r.get("驗_宗序") or "").strip() for r in b]
            A = {(r.get("暫編地號") or "").strip(): r for r in a}
            dg = max([abs(float(r["G(㎡)"]) - float(A[i]["G(㎡)"]))
                      for i, r in zip(idb, b) if i in A] or [0.0])
            ds = max([abs(float(r["累積S(m)"]) - float(A[i]["累積S(m)"]))
                      for i, r in zip(idb, b) if i in A] or [0.0])
            mv = (dg > 1e-6) or (ds > 1e-6)
            tot += 1
            moved += 1 if mv else 0
            ok = (ida == idb) and (qa == qb)
            if not ok:
                FAIL.append("款(2) 鏈序改變 %s·%s·%s" % (tag, k[0], k[1]))
            print("   %-4s %-4s %-6s 宗 %2d｜`|ΔG|max` %8.4f｜`max|Δ累積S|` %8.4f｜%s｜鏈序 %s"
                  % (tag, k[0], k[1], len(idb), dg, ds,
                     "🔴 已動" if mv else "✅ 未動",
                     "✅ 不變" if ok else "🛑 **改變**"))
    print()
    print("   🔒 母體基數（二態共有之側）＝ **%d**｜其中**已動** ＝ **%d**" % (tot, moved))
    if only_on:
        print("   🟡 **僅 `on` 有之側**（新可達·⛔ 判·loud）＝ %d：%s"
              % (len(only_on), ["%s·%s·%s" % (t, k[0], k[1]) for t, k in only_on]))
    print()

    # ══ §三-2　人造擾動 ═══════════════════════════════════════════
    print("=" * 118)
    print("【`§三-2`】人造擾動之判別力（組 ＝ `3.5m`·`%s`·`%s`）" % GRP)
    print("=" * 118)
    blk, side = GRP
    dh = dhat(fl, blk)
    base = ST[("3.5m", "on")][0]
    ix = side_idx(base, blk, side)
    print("   `d̂`（生產解析器之 `FRONT_LINE` `p1→p2`）＝ (%.9f, %.9f)" % dh)
    print("   該側宗數 ＝ %d｜擾動量 ＝ %g m（**固定**·⛔ 調）" % (len(ix), PERT))
    print()

    # ── 陰性：未擾動 ──
    print("── 輪 `1`〔**陰性**·未擾動〕──")
    ROWS["ON_N"] = base
    r_neg = V1.run("OFF", "ON_N", blk, side, fl, "陰性·未擾動")
    print()

    # ── 式 甲：單之字面（單獨平移一宗）──
    print("── 輪 `2`〔式 `甲`·**單之字面**：單獨平移一宗 `%g m`〕──" % PERT)
    tgt = ix[1]                      # 一個**非鏈頭**宗
    rows_a = [dict(r) for r in base]
    cc = cc_of(rows_a[tgt])
    rows_a[tgt]["cut_coords"] = repr([[x + PERT * dh[0], y + PERT * dh[1]] for x, y in cc])
    print("   受擾之宗 ＝ `%s`（非鏈頭）｜⛔ 動其 `G(㎡)` 欄（剛體平移）"
          % rows_a[tgt].get("暫編地號"))
    ROWS["ON_A"] = rows_a
    r_a = V1.run("OFF", "ON_A", blk, side, fl, "式 甲·單之字面")
    print()

    # ── 式 乙：保守項（共用界線之二頂點·同步移動 ＋ G := 擾動後面積）──
    print("── 輪 `3`〔式 `乙`·**保守項**：一條共用界線之二頂點同步移 `%g m`〕──" % PERT)
    i1, i2 = ix[1], ix[2]
    c1, c2 = cc_of(base[i1]), cc_of(base[i2])
    sh = V1.shared_edge(c1, c2)
    print("   受擾之界 ＝ `%s` ↔ `%s`｜共用頂點數 ＝ **%d**（須 `2`）"
          % (base[i1].get("暫編地號"), base[i2].get("暫編地號"), len(sh)))
    if len(sh) != 2:
        print("   🛑 共用頂點⛔ 為 `2` ⇒ **loud 拒測**（⛔ 靜默改選）")
        FAIL.append("式乙 共用頂點≠2")
    else:
        def shift(c):
            out = []
            for x, y in c:
                if any(abs(x - s[0]) < 1e-6 and abs(y - s[1]) < 1e-6 for s in sh):
                    out.append([x + PERT * dh[0], y + PERT * dh[1]])
                else:
                    out.append([x, y])
            return out
        rows_b = [dict(r) for r in base]
        for i, c in ((i1, c1), (i2, c2)):
            nc = shift(c)
            rows_b[i]["cut_coords"] = repr(nc)
            p = Polygon(nc)
            p = p if p.is_valid else p.buffer(0)
            old = float(rows_b[i]["G(㎡)"])
            rows_b[i]["G(㎡)"] = str(round(p.area, 2))
            print("        `%s`　`G` %.4f → %.4f（＝ 擾動後多邊形面積·使閘 `β` 仍過）"
                  % (rows_b[i].get("暫編地號"), old, p.area))
        ROWS["ON_B"] = rows_b
        r_b = V1.run("OFF", "ON_B", blk, side, fl, "式 乙·保守項")
    print()

    # ══ 判 ════════════════════════════════════════════════════════
    print("=" * 118)
    print("【判】")
    print("=" * 118)

    def line(nm, r):
        if r.get("refuse"):
            print("   %-22s 🛑 **loud 拒測**（`n` ＝ %d·閘不過或判定集為空）" % (nm, r.get("n", 0)))
            return
        print("   %-22s n ＝ %d｜`(1b)` %s｜`(3)` %s｜`(5)` %d 宗"
              % (nm, r["n"], "✅ 綠" if r["k1b"] else "🔴 紅",
                 "✅ 綠" if r["k3"] else "🔴 紅", r["n5"]))
    line("輪 1〔陰性〕", r_neg)
    line("輪 2〔式 甲〕", r_a)
    if "r_b" in dir():
        line("輪 3〔式 乙〕", r_b)
    print()

    neg_green = (not r_neg.get("refuse")) and r_neg["k1b"] and r_neg["k3"] and r_neg["n5"] == 0
    print("   陰性（未擾動）須全綠 ⇒ %s" % ("✅" if neg_green else "🔴"))
    if not neg_green:
        FAIL.append("陰性未全綠")

    print("   式 `甲`（單之字面）⇒ %s"
          % ("🟡 **loud 拒測**（閘 `γ`）——⛔ 讀為「不敏感」（本器 docstring `(甲)`）"
             if r_a.get("refuse") else
             ("✅ 轉紅" if (not r_a["k1b"] and not r_a["k3"]) else "🔴 **未轉紅**")))

    ok_b = False
    if "r_b" in dir() and not r_b.get("refuse"):
        ok_b = (not r_b["k1b"]) and (not r_b["k3"]) and (r_b["n5"] > 0)
        print("   式 `乙`（保守項）須 `(1b)`／`(3)` 轉紅 ⋀ `(5) > 0` ⇒ %s"
              % ("✅" if ok_b else "🔴 **未如期**"))
        same = (r_neg["k1b"] == r_b["k1b"]) and (r_neg["k3"] == r_b["k3"])
        print("   二輪（陰性 vs 式 `乙`）同色？ %s ⇒ %s"
              % (same, "🔴 **閘失能**" if same else "✅ **閘⛔ 失能**"))
        if same:
            FAIL.append("式乙 二輪同色")
        if not ok_b:
            FAIL.append("式乙 未如期轉紅")
    print()
    print("=" * 118)
    if FAIL:
        print("🛑 **停機上呈** %d 項：" % len(FAIL))
        for t in sorted(set(FAIL)):
            print("   🛑 %s" % t)
        return 1
    print("✅ 款 `(2)` 逐側鏈序不變 ⋀ 陰性全綠 ⋀ 式 `乙` 轉紅且二輪⛔ 同色")
    print("🟡 式 `甲`（單之字面）之結果見上——其**⛔ 讀為閘失能**（成因 ＝ 閘 `γ` 拒測·⛔ 不敏感）")
    print("=" * 118)
    return 0


if __name__ == "__main__":
    sys.exit(main())
