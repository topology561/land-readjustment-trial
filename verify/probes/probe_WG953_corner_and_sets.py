#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""【W-G.9-53】§C-1 街角規定範圍之矩形容納 ＋ §E-1／E-2／E-3（⛔ 零生產碼）

**三組受詞（⛔ 不互代）**：
- **C-1**：`K-9-5-2 ③` 之構造保證（「該街角最小規定範圍**一定**最小深度 ≥ 畸零地深、
  最小寬度 ≥ 畸零地寬」）於**新判準**下是否仍成立 ⇒ 取**街角最小規定範圍多邊形本身**
  跑 `K-9-12` 之矩形容納（**自由姿態**·沿用 `-49` 已驗收之侵蝕＋Lipschitz 證書）。
  🔒 **⛔ 須用現行構造** `_build_corner_range_v3`（`K-9-5-4` ∥SIDELINE·`f8b42fc`），
  ⛔ **不得**用 `K-9-5-2 ①` 之舊構造。
- **E-1**：`-43` D-1 名單（零條合格垂線）vs `-49` B-6（矩形不進 ∪ 面積分流）之**對稱差**。
  🔴 ⛔ **不得寫成「等價」**——KL 逐字：「26 宗的一樣可能真的只是巧合」。
- **E-2**：`MinA = round(D_avg,2) × min_width` 逐宗算出，與二集合作**三向交叉表**。⛔ 不推論法源關係。
- **E-3**：街角單調性（`cut_coords` 是否恆為截角前形狀之子集）
  ⚠️ **射程已縮**（`K-9-13 B-3` 令街角走 `K-9-5-2`）⇒ 本項降為**佐證**、⛔ 非判定依據。

🔒 輸出檔名含產生它之 commit 短碼；⛔ 不覆寫任何既有 log。
"""
import io
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
from probe_WG941_bandbase import st_frame                           # noqa: E402
from probe_WG947_rect_fit import _poly_st                           # noqa: E402
# 🔒 沿用 `-49` 已驗收之自由姿態實作（⛔ 不另寫第二份·`GB-8`）
from probe_WG949_free_pose import scan, witness, STEPS              # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
WID = 172
SB = 0.0
LOG43 = os.path.join(OUTDIR, "probe_WG943_parallel_recount_8c8f223.log")


def _short_sha():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                       cwd=VERIFY, capture_output=True, text=True, timeout=20)
    return (r.stdout or "").strip() or "nogit"


def main():                                                         # noqa: C901
    L = []

    def P(s=""):
        L.append(s)

    sha = _short_sha()
    P("=" * WID)
    P("【W-G.9-53】§C-1 街角規定範圍之矩形容納 ＋ §E-1／E-2／E-3")
    P("=" * WID)
    P(f"  產生於 commit：{sha}")
    P("")

    ns, fake_st = harvest()
    eps_touch = float(ns["_EPS_TOUCH_FRONT"])
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, SB)
    _d, _s, _o, winners, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        SB, snapshot=snapshot)
    BLKS = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in BLKS:
            BLKS.append(_l)
    g_rows, ERR = [], {}
    for lbl in BLKS:
        try:
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params,
                             [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                             winners, forced, SB)
            g_rows.extend(_sg["g_rows"])
        except Exception as e:                                       # noqa: BLE001
            ERR[lbl] = f"{type(e).__name__}: {str(e).splitlines()[0][:120]}"
    rows = [r for r in g_rows if str(r.get("推進側別")) in ("left", "right")]

    WD = {}
    for lbl in sorted({str(r.get("所屬街廓")) for r in rows}):
        mw = ns["get_min_lot_size"](cb_by[lbl]["category"],
                                    float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))
        WD[lbl] = (float(mw["min_width"]), float(mw["min_depth"]))
    w0, d0 = WD[sorted(WD)[0]]
    R = math.sqrt(w0 * w0 + d0 * d0) / 2.0

    # ══════════════════════════════════════════════════════════════════
    # §C-1　街角最小規定範圍多邊形本身之矩形容納
    # ══════════════════════════════════════════════════════════════════
    P("=" * WID)
    P("【C-1】`K-9-5-2 ③` 之構造保證於新判準下是否仍成立")
    P("=" * WID)
    P("  🔒 **受詞 ＝ 街角最小規定範圍<u>多邊形本身</u>**（⛔ 非街角宗地）")
    P(f"  🔒 構造來源 ＝ `_build_corner_range_v3`（`K-9-5-4` ∥SIDELINE·現行）"
      f"；`W`／`D` ＝ {w0}／{d0}（`get_min_lot_size`）")
    fn = ns.get("_build_corner_range_v3")
    P(f"  harvest 取得 `_build_corner_range_v3`：{callable(fn)}")
    P("")
    P(f"  {'街廓':<5}{'側':<7}{'面積㎡':>11}{'矩形容納':>10}{'見證θ':>11}"
      f"{'四角皆在內':>11}{'Δθ':>9}{'證書':>6}")
    CR, CRERR = [], []
    # 🔒 **引數之組裝⛔ 不自創**——逐字沿用倉內既有之
    #   `verify/fixture_corner_range_k8.py` 之 `_build(lbl, which, setback)`
    #   （錨 `grep -n "kw = dict(" verify/fixture_corner_range_k8.py`）。
    sides = cad.get("side_lines_by_side", {}) or {}

    def _build_range(lbl, which, setback=SB):
        b = cb_by[lbl]
        mb = cad["baselines"][lbl]
        fl = cad["front_lines"][lbl]
        sd = cad["side_lines_by_side"][lbl][which]
        mw = float(ns["get_min_lot_size"](
            b["category"], float(snapshot["blocks"][lbl]["正面"]["路寬_m"]))["min_width"])
        kw = dict(
            block_vertices=b["vertices"], block_centroid=b["centroid"],
            front_pts=[fl["p1"], fl["p2"]],
            baseline_pts=ns["_baseline_pts_from_manual"](mb, b["vertices"]),
            side_line_pts=[sd["p1"], sd["p2"]],
            alloc_dir=cad["alloc_dir_by_block"][lbl],
            block_depth=float(snapshot["blocks"][lbl]["街廓分配深度_m"]),
            setback=setback, min_width=mw,
            chamfer_tri=ns["_make_chamfer_tri_wb"](b, which),
            dxf_quantum=(mb.get("_match") or {}).get("q_detected"),
            _label=lbl, _side=which)
        return ns["_build_corner_range_v3"](**kw)

    TARGETS = [(lbl, wch) for lbl in sorted(WD) for wch in ("left", "right")
               if wch in (sides.get(lbl) or {})]
    P(f"  受測街角位置 ＝ **{len(TARGETS)}** 個（⛔ 由 `side_lines_by_side` 現查·非硬編）："
      + "／".join(f"{a}/{b}" for a, b in TARGETS))
    P("")
    for lbl, wch in TARGETS:
        w, d = WD[lbl]
        try:
            rng = _build_range(lbl, wch)
        except Exception as e:                                       # noqa: BLE001
            CRERR.append((lbl, wch, f"{type(e).__name__}: {str(e).splitlines()[0][:90]}"))
            P(f"  {lbl:<5}{wch:<7}{'—':>11}   🔴 構造 raise：{str(e).splitlines()[0][:70]}")
            continue
        pst = _poly_st([(float(x), float(y)) for x, y in list(rng.exterior.coords)])
        cvx = abs(pst.area - pst.convex_hull.area) <= 1e-9
        th, dth, mmax, npt, cert = scan(pst, w, d, R=R)
        wit = witness(pst, w, d, th) if th is not None else None
        CR.append((lbl, wch, float(pst.area), th is not None, th, wit, dth, cert, cvx))
        P(f"  {lbl:<5}{wch:<7}{pst.area:>11.4f}"
          f"{('進' if th is not None else '不進'):>10}"
          f"{(f'{th:.4f}' if th is not None else '—'):>11}"
          f"{('✅ 4/4' if (wit and wit['all_in']) else '—'):>11}"
          f"{dth:>9.1e}{('—' if th is not None else ('✅' if cert else '🔴')):>6}"
          f"　{'凸' if cvx else '🔴 非凸'}")
    P("-" * WID)
    _nin = sum(1 for x in CR if x[3])
    P(f"  ⇒ **{_nin}／{len(CR)}** 個街角規定範圍**可容納** `W×D` 矩形")
    if CR and _nin == len(CR):
        P("  🔒 ⇒ `K-9-5-2 ③` 之構造保證於**新判準**下**於本案仍成立**")
        P("     ⚠️ ⛔ **不得推論為「一定成立」**——③ 之「一定」係**構造性**主張，")
        P("     而本項僅為**本案 4 個位置**之實測；R2／R4／R5 未量。")
    elif CR:
        # 🩸 **`W-G.9-56` §D-5 修**：本句首版印「`K-9-5-2 ③` 之保證**不成立**」，
        #   與同批報告之「③ 之保證 **⇏ 矩形容納**」**受詞不同、且較之過寬**
        #   ——③ 之字面為「最小**深度** ≥ 畸零地深 ∧ 最小**寬度** ≥ 畸零地寬」（**兩個一維量**），
        #     本測所量者為**二維之矩形容納** ⇒ **本測未量 ③ 之字面** ⇒ ⛔ 不得稱其「不成立」。
        #   （同族：結論句較其所據之量測為寬·`GB-71`）
        P("  🔴 ⇒ **有街角規定範圍容納不下 `W×D` 矩形**")
        P("     🔒 ⇒ 本測所證者僅為 **「`K-9-5-2 ③` 之保證 ⇏ 矩形容納」**；")
        P("     ⛔ **不得**寫成「③ 之保證**不成立**」——③ 之字面為**兩個一維量**")
        P("     （最小深度 ≥ 畸零地深 ∧ 最小寬度 ≥ 畸零地寬），**本測未量該二量**。")
        for x in CR:
            if not x[3]:
                P(f"      🛑 {x[0]}/{x[1]}　面積 {x[2]:.4f}　證書 ＝ {'成立' if x[7] else '🔴 不成立'}")
    if CRERR:
        P("  🛑 構造 raise 之位置（⛔ 逐項具名）：")
        for lbl, wch, msg in CRERR:
            P(f"      {lbl}/{wch}：{msg}")

    # ══════════════════════════════════════════════════════════════════
    # §E-1　集合對稱差
    # ══════════════════════════════════════════════════════════════════
    P("")
    P("=" * WID)
    P("【E-1】`A` ＝ `-43` D-1 名單（零條合格垂線） vs `B` ＝ `-49` B-6（不進 ∪ 面積分流）")
    P("=" * WID)
    A = set()
    if os.path.exists(LOG43):
        txt = io.open(LOG43, encoding="utf-8", newline="").read()
        seg = txt.split("【D-1】")[1].split("【D-3】")[0] if "【D-1】" in txt else ""
        for m in re.finditer(r"^\s+R\d\s+\S+\s+(\S+)\s", seg, re.M):
            A.add(m.group(1))
    P(f"  `A` 之來源 ＝ `{os.path.basename(LOG43)}` 之【D-1】段 ⇒ **{len(A)}** 宗")
    P("      " + "／".join(sorted(A)))

    # B：重算（⛔ 不抄 log）
    from probe_WG947_rect_fit import rect_fits                        # noqa: F401
    B, Bsmall, Bnofit, ALL = set(), set(), set(), []
    for r in rows:
        lbl = str(r.get("所屬街廓") or "")
        gid = str(r.get("暫編地號") or "")
        cc = r.get("cut_coords") or []
        if len(cc) < 3 or lbl not in WD:
            continue
        area = float(r.get("幾何面積(㎡)") or 0.0)
        w, d = WD[lbl]
        fl = fl_by.get(lbl) or {}
        p1, p2 = fl.get("p1"), fl.get("p2")
        if not (p1 and p2):
            continue
        dx, dy = float(p2[0]) - float(p1[0]), float(p2[1]) - float(p1[1])
        Lf = math.hypot(dx, dy)
        dh = (dx / Lf, dy / Lf)
        ALL.append((lbl, gid, area))
        if area < w * d:
            B.add(gid); Bsmall.add(gid)
            continue
        try:
            ring, t_lo, sg, dd, nn, fe = st_frame(cc, dh, p1, eps_touch)
        except Exception:                                            # noqa: BLE001
            continue
        pst = _poly_st(ring)
        th, dth, mmax, npt, cert = scan(pst, w, d, R=R)
        if th is None:
            B.add(gid); Bnofit.add(gid)
    P(f"  `B` ＝ **{len(B)}** 宗（面積分流 {len(Bsmall)} ＋ 自由姿態不進 {len(Bnofit)}）"
      "　🔒 **重算·⛔ 未抄 log**")
    P("      " + "／".join(sorted(B)))
    P("")
    P(f"  🔴 **`A \\ B` ＝ {len(A - B)} 宗**" + ("：" + "／".join(sorted(A - B)) if (A - B) else "（空）"))
    P(f"  🔴 **`B \\ A` ＝ {len(B - A)} 宗**" + ("：" + "／".join(sorted(B - A)) if (B - A) else "（空）"))
    P("")
    P("  🔒 **⛔ 不得寫成「二判準等價」**（KL 逐字：「26 宗的一樣可能真的只是巧合」）：")
    P("     對稱差為空**只證本案 26 宗上二集合相同**，⛔ 不證二規則邏輯等價。")
    P("     **分岔反例之構造（⛔ 非本案宗地·係合成）**：`-47` 自檢 ①② 已各造一例——")
    P("     ① 寬足深不足（20×6）：矩形**不進** ∧ 帶內 min 寬 20 **≥ W** ⇒ 舊寬度判準**過**；")
    P("     ② 前窄後寬凸梯形：矩形**進** ∧ 帶內 min 寬 1.5 **< W** ⇒ 舊寬度判準**不過**。")
    P("     ⇒ **二判準確可分岔** ⇒ 本案之同集**係資料所致**，⛔ 非邏輯蘊含。")
    P("     ⚠️ 惟上二例之對照者為**舊寬度判準**；與 `A`（**合格垂線**）之分岔反例")
    P("     **⛔ 本批未構造** ⇒ 具名為未辦，⛔ 不以前者冒充。")

    # ══════════════════════════════════════════════════════════════════
    # §E-2　MinA 三向交叉表
    # ══════════════════════════════════════════════════════════════════
    P("")
    P("=" * WID)
    P("【E-2】`MinA = round(D_avg,2) × min_width` 之三向交叉（⛔ 不推論法源關係）")
    P("=" * WID)
    # 🩸 **首版取 `ns["f3_min_alloc_area_by_label"]` ⇒ `None`（⛔ 具名）**：該符號係
    #   **`session_state` 之鍵**、⛔ 非 module 級符號 ⇒ `harvest()` 之 `ns` 取不到。
    #   ⇒ 改**自快照現算**：`MinA = round(街廓分配深度_m, 2) × min_width`
    #     （`CLAUDE.md`「舊 per-block MinA」之式·⛔ 非自創）。
    mina = {}
    _f3 = ns.get("f3_min_alloc_area_by_label")
    P(f"  `ns['f3_min_alloc_area_by_label']` 取得：{_f3 is not None}"
      "（⇒ 係 `session_state` 鍵·⛔ 非 module 級符號）")
    for lbl in sorted(WD):
        _dep = float(snapshot["blocks"][lbl]["街廓分配深度_m"])
        mina[lbl] = round(round(_dep, 2) * WD[lbl][0], 2)
    P("  🔒 **現算**：`MinA = round(街廓分配深度_m, 2) × min_width` ⇒ "
      + "／".join(f"{k} 深度 {float(snapshot['blocks'][k]['街廓分配深度_m']):.4f}"
                 f" ⇒ MinA {v:.2f}" for k, v in sorted(mina.items())))
    P("")
    P(f"  {'街廓':<5}{'暫編地號':<14}{'面積㎡':>10}{'MinA':>10}{'面積<MinA?':>11}"
      f"{'∈A?':>6}{'∈B?':>6}")
    for lbl, gid, area in ALL:
        ma = mina.get(lbl)
        P(f"  {lbl:<5}{gid:<14}{area:>10.2f}"
          f"{(f'{ma:.2f}' if ma is not None else '—'):>10}"
          f"{('是' if (ma is not None and area < ma) else '否'):>11}"
          f"{('✅' if gid in A else '—'):>6}{('✅' if gid in B else '—'):>6}")
    if mina:
        n_lt = sum(1 for lbl, gid, a in ALL if mina.get(lbl) is not None and a < mina[lbl])
        P(f"  ⇒ 面積 < `MinA` 者 ＝ **{n_lt}** 宗；`A` ＝ {len(A)}；`B` ＝ {len(B)}")
        P("  🔒 ⛔ **不推論法源關係**——三者受詞各異（`MinA` ＝ 面積門檻／"
          "`A` ＝ 合格垂線／`B` ＝ 矩形容納）。")

    # ══════════════════════════════════════════════════════════════════
    # §E-3　街角單調性（⛔ 佐證·非判定依據）
    # ══════════════════════════════════════════════════════════════════
    P("")
    P("=" * WID)
    P("【E-3】街角單調性：`cut_coords`（截角後）是否為截角前形狀之子集")
    P("=" * WID)
    P("  ⚠️ **射程已縮**（`K-9-13 B-3` 令街角走 `K-9-5-2`）⇒ 本項為**佐證**、⛔ 非判定依據。")
    P("  🛑 **⛔ 未辦**：`K-9-6-h ⑤`（截角前形狀）**未實作** ⇒ 倉內**無**截角前多邊形之產生途徑")
    P("     ⇒ `P₀`（截角前）取不到 ⇒ `P₁.difference(P₀).area ≤ 1e-9` 之左右兩側**皆無從構成**。")
    P("     ⛔ **不以「街廓多邊形」或「街角規定範圍」冒充 `P₀`**——二者皆非截角前之宗地形狀。")
    P("     ⇒ 出艙碼 ＝ **「無從判定（附所缺）」**；所缺 ＝ 截角前形狀之產生途徑（`K-9-6-h ⑤`）。")

    for lbl in BLKS:
        if lbl in ERR:
            P(f"  ⛔ 街廓 {lbl}：`run_step_g` raise ⇒ **未量**")
    P("=" * WID)
    return L, sha


if __name__ == "__main__":
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    _L, _sha = main()
    os.makedirs(OUTDIR, exist_ok=True)
    _log = os.path.join(OUTDIR, f"probe_WG953_corner_and_sets_{_sha}.log")
    with io.open(_log, "w", encoding="utf-8") as f:
        f.write("\n".join(_L) + "\n")
    print("\n".join(_L))
    print(f"\n→ {_log}", file=sys.stderr)
