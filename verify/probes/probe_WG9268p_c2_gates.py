# -*- coding: utf-8 -*-
"""`W-G.9-268′` `c2` 之性質閘與差異表（施工單 `§三` `P-5`／`P-6`／`P-8` ＋ `§四` 表一〜表三）。

🔒 **三態**（⛔ 二態）
  `off`  ＝ 顯式 `WG9268P_ANCHOR_GEOM='0'`
  `on`   ＝ 顯式 `'1'`
  `dflt` ＝ **環境變數不設**（⇒ 取碼內預設）——**用以驗 `c2` 之預設是否真的生效**。
  🩸 **⛔ 以 `pop` 取 `off`**：`c2` 後預設為 `'1'`，`pop` 所得者為 `on` 而器⛔ 報錯（自毀式）。

🔑 **`P-5` 之比較端 ＝ `cut_coords` <u>全多邊形</u>逐位**（⛔ 自定義「遠側境界線」）
  施工單 `P-5` 之受詞為「`G`、分配範圍面積、**遠側境界線**改前改後逐位相同」。
  本器**⛔ 另寫「遠側境界線」之第二份定義**（重導即開第二份定義·`GB-48` 族），
  改比**整個 `cut_coords`**：其逐位相同 ⇒ 其任一邊（含遠側境界線）**a fortiori** 相同。
  🔒 該法**只會更嚴**，⛔ 更寬。

🔑 **鍵**：`(情境, 暫編地號)`（⛔ 幾何鍵·坑 `4`）；並當場證**相異鍵數 ＝ 宗數**。

用法：`python verify/probes/probe_WG9268p_c2_gates.py [倉根]`
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
import wg9268p_selector_liveness as _LIVE                          # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

FLAG = "WG9268P_ANCHOR_GEOM"
SCEN = (("0m", 0.0), ("3.5m", 3.5))
POOL = "抵費地"
W = 122
FAIL = []


def drive(setback, mode, ns, fake_st, snapshot, cb_by, cad, build_p, temp_p):
    """mode ∈ {'off','on','dflt'}；回 (g_rows, aborted, winners)。"""
    if mode == "on":
        os.environ[FLAG] = "1"
    elif mode == "off":
        os.environ[FLAG] = "0"
    else:
        os.environ.pop(FLAG, None)          # 🔑 dflt：**不設** ⇒ 取碼內預設
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
    return g_rows, aborted, wins


def f2(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def by_key(g_rows):
    """{暫編地號: row}；並回相異鍵數與宗數以供 坑 4 之自證。"""
    d = {}
    dup = []
    n = 0
    for r in g_rows:
        if (r.get("推進側別") or "").strip() == POOL:
            continue
        n += 1
        k = (r.get("暫編地號") or "").strip()
        if k in d:
            dup.append(k)
        d[k] = r
    return d, n, dup


def owner_of(fake_st, landno):
    """土地所有權人 ＝ 歸戶群組（`Gxxx`·匿名化之所有權人身分）。⛔ 靜默略過。"""
    ss = getattr(fake_st, "session_state", None)
    if not ss:
        return "⛔ 不可得（無 session_state）"
    m = ss.get("t8_ownership_map") or {}
    if not m:
        return "⛔ 不可得（map 空）"
    for k in (landno, str(landno).strip()):
        if k in m:
            v = m[k]
            if isinstance(v, dict):
                return v.get("group") or v.get("歸戶群組") or repr(v)[:40]
            return str(v)
    return "⛔ 查無此鍵"


def main():                                                         # noqa: C901
    print("=" * W)
    print("【`W-G.9-268′` `c2`】性質閘 `P-5`／`P-6`／`P-8` ＋ 差異表 表一〜表三")
    print("=" * W)
    print()

    ns, fake_st = harvest()
    if not _LIVE.assert_live(ns, "probe_WG9268p_c2_gates.py"):
        print("🔴 選擇器活體檢不過 ⇒ 本次輸出⛔ 出艙（⛔ 判綠·⛔ 靜默續跑）")
        return 4
    print()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    print("🔒 管線已建：街廓 `%d`／宗 `%d`" % (len(cb_by), len(build_p)))
    print()

    ST = {}
    for tag, sb in SCEN:
        for mode in ("off", "on", "dflt"):
            g, ab, wins = drive(sb, mode, ns, fake_st, snapshot,
                                cb_by, cad, build_p, temp_p)
            ST[(tag, mode)] = (g, ab, wins)
            d, n, dup = by_key(g)
            print("🔒 [%-4s ／ %-4s] `g_rows` **%d** 列（母體基數）／中止 %s"
                  "／分配宗 %d ／相異鍵 %d %s"
                  % (tag, mode, len(g), ab or "無", n, len(d),
                     "✅" if len(d) == n else ("🛑 碰撞 %r" % dup)))
            if len(d) != n:
                FAIL.append("鍵碰撞 %s/%s" % (tag, mode))
    print()

    # ── c2 之預設生效檢 ───────────────────────────────────────────
    print("=" * W)
    print("【`c2` 預設生效檢】`dflt`（環境變數**不設**）須與 `on` **逐位相同**、且與 `off` **相異**")
    print("=" * W)
    for tag, _sb in SCEN:
        go, _a1, _w1 = ST[(tag, "off")]
        gn, _a2, _w2 = ST[(tag, "on")]
        gd, _a3, _w3 = ST[(tag, "dflt")]
        s_off, s_on, s_d = repr(go), repr(gn), repr(gd)
        ok1 = (s_d == s_on)
        ok2 = (s_d != s_off)
        print("   %-5s dflt ＝ on ？ **%s** %s ／ dflt ≠ off ？ **%s** %s"
              % (tag, "是" if ok1 else "否", "✅" if ok1 else "🛑",
                 "是" if ok2 else "否", "✅" if ok2 else "🛑"))
        if not ok1:
            FAIL.append("dflt≠on %s" % tag)
        if not ok2:
            FAIL.append("dflt==off %s（⇒ 預設未生效）" % tag)
    print()
    print("   🔑 **判別力**：上二問若同為「是」則自相矛盾 ⇒ 本檢⛔ 恆綠；")
    print("      `off` 與 `on` 之 `g_rows` 於本批確有實質相異（見表一之增減格數）。")
    print()

    # ── P-8 可達性只增不減 ───────────────────────────────────────
    print("=" * W)
    print("【`P-8`】harness 可達性**只增不減**")
    print("=" * W)
    for tag, _sb in SCEN:
        bo = {(r.get("所屬街廓") or "").strip() for r in ST[(tag, "off")][0]}
        bn = {(r.get("所屬街廓") or "").strip() for r in ST[(tag, "on")][0]}
        lost = sorted(bo - bn)
        print("   %-5s off ＝ %s ／ on ＝ %s ／**轉不可達** ＝ %s %s"
              % (tag, sorted(bo), sorted(bn), lost or "無",
                 "✅" if not lost else "🛑 停機款"))
        if lost:
            FAIL.append("P-8 %s 轉不可達 %r" % (tag, lost))
    print()

    # ── P-5 / P-6 街角地 ─────────────────────────────────────────
    print("=" * W)
    print("【`P-5`】街角第 `1` 宗之 `G`／範圍面積／**`cut_coords` 全多邊形**改前改後逐位相同")
    print("【`P-6`】街角地**歸屬**改前改後不變")
    print("=" * W)
    print("   🔑 `P-5` 之比較端 ＝ `cut_coords` **全多邊形**（⛔ 自定義「遠側境界線」）")
    print("      其逐位相同 ⇒ 遠側境界線 **a fortiori** 相同（只會更嚴·⛔ 更寬）")
    print()
    n5 = 0
    for tag, _sb in SCEN:
        do, _n, _d = by_key(ST[(tag, "off")][0])
        dn, _n2, _d2 = by_key(ST[(tag, "on")][0])
        corners_o = {k: r for k, r in do.items()
                     if str(r.get("驗_宗序")).strip() == "街角第1宗"}
        corners_n = {k: r for k, r in dn.items()
                     if str(r.get("驗_宗序")).strip() == "街角第1宗"}
        # P-6：歸屬 ＝ (街廓, 側) → 暫編地號
        own_o = {((r.get("所屬街廓") or "").strip(),
                  (r.get("推進側別") or "").strip()): k
                 for k, r in corners_o.items()}
        own_n = {((r.get("所屬街廓") or "").strip(),
                  (r.get("推進側別") or "").strip()): k
                 for k, r in corners_n.items()}
        print("── 情境 `%s` ── 街角第 1 宗：off `%d` 側／on `%d` 側"
              % (tag, len(corners_o), len(corners_n)))
        both = sorted(set(own_o) & set(own_n))
        if not both:
            print("   🟡 **判定集為空** ⇒ loud 拒測（⛔ 判綠）")
            FAIL.append("P-5/P-6 %s 判定集為空" % tag)
            continue
        for k in both:
            ko, kn = own_o[k], own_n[k]
            ro, rn = corners_o[ko], corners_n[kn]
            same_owner = (ko == kn)
            gsame = (repr(ro.get("G(㎡)")) == repr(rn.get("G(㎡)")))
            asame = (repr(ro.get("驗_C_街角範圍面積"))
                     == repr(rn.get("驗_C_街角範圍面積")))
            csame = (repr(ro.get("cut_coords")) == repr(rn.get("cut_coords")))
            n5 += 1
            ok = same_owner and gsame and asame and csame
            if not ok:
                FAIL.append("P-5/P-6 %s %s" % (tag, k))
            print("   %-14s 歸屬 %-14s→%-14s %s ｜ G %s ｜ 範圍面積 %s ｜ 多邊形 %s %s"
                  % (str(k), ko, kn, "同" if same_owner else "🛑 變",
                     "同" if gsame else "🛑 變", "同" if asame else "🛑 變",
                     "同" if csame else "🛑 變", "✅" if ok else "🛑"))
        only_n = sorted(set(own_n) - set(own_o))
        if only_n:
            print("   🟡 **僅 `on` 有之街角側**（新可達·⛔ 判為歸屬變動）：%s" % only_n)
    print()
    print("   判定集基數（`P-5`／`P-6` 共有街角側）＝ **%d**" % n5)
    if n5 == 0:
        print("   🛑 判定集為空 ⇒ loud 拒測")
    print()

    # ── 表一：逐宗 ───────────────────────────────────────────────
    print("=" * W)
    print("【表一】街角地後續配地位置更正前後對照（逐宗·**全宗母體**）")
    print("=" * W)
    summ = {}
    for tag, _sb in SCEN:
        do, _n, _d = by_key(ST[(tag, "off")][0])
        dn, _n2, _d2 = by_key(ST[(tag, "on")][0])
        keys = sorted(set(do) | set(dn))
        rows = []
        for k in keys:
            ro, rn = do.get(k), dn.get(k)
            if ro is None:
                disp = "新入可分配"
            else:
                dpos = (f2(rn.get("累積S(m)")) - f2(ro.get("累積S(m)"))
                        if rn is not None else None)
                disp = ("位置外移" if (dpos or 0) > 0.005 else "維持原位")
            if rn is None:
                disp = "🛑 消失（off 有而 on 無）"
                FAIL.append("表一 %s %s 消失" % (tag, k))
            src = rn if rn is not None else ro
            ga = f2(ro.get("G(㎡)")) if ro else None
            gb = f2(rn.get("G(㎡)")) if rn else None
            wa = f2(ro.get("宗地寬度(m)")) if ro else None
            wb = f2(rn.get("宗地寬度(m)")) if rn else None
            pa = f2(ro.get("累積S(m)")) if ro else None
            pb = f2(rn.get("累積S(m)")) if rn else None
            rows.append({
                "blk": (src.get("所屬街廓") or "").strip(),
                "side": (src.get("推進側別") or "").strip(),
                "seq": pb if pb is not None else (pa or 0),
                "暫編": k,
                "原地號": src.get("原地號"),
                "所有權人": owner_of(fake_st, src.get("原地號")),
                "Ga": ga, "Gb": gb,
                "dG": (None if (ga is None or gb is None) else gb - ga),
                "Wa": wa, "Wb": wb,
                "dW": (None if (wa is None or wb is None) else wb - wa),
                "dPos": (None if (pa is None or pb is None) else pb - pa),
                "處置": disp,
                "街角": src.get("街角地"),
            })
        rows.sort(key=lambda r: (r["blk"], r["side"], r["seq"]))
        print("── 情境 `%s` ── 宗數 off `%d` ／ on `%d` ／聯集 `%d`"
              % (tag, len(do), len(dn), len(keys)))
        print("   %-4s %-6s %-14s %-9s %-8s %10s %10s %9s %8s %8s %8s %9s %s"
              % ("街廓", "側", "暫編地號", "重劃前地號", "所有權人",
                 "前 G", "後 G", "ΔG", "前寬", "後寬", "Δ寬", "位置變動", "處置"))
        for r in rows:
            def s(v, f="%10.2f"):
                return ("%10s" % "—") if v is None else (f % v)
            print("   %-4s %-6s %-14s %-9s %-8s %s %s %s %s %s %s %s %s"
                  % (r["blk"], r["side"], r["暫編"], r["原地號"], r["所有權人"],
                     s(r["Ga"]), s(r["Gb"]), s(r["dG"], "%+9.2f"),
                     s(r["Wa"], "%8.2f"), s(r["Wb"], "%8.2f"), s(r["dW"], "%+8.2f"),
                     s(r["dPos"], "%+9.2f"), r["處置"]))
        summ[tag] = rows
        print()

    # ── 表三：彙總 ───────────────────────────────────────────────
    print("=" * W)
    print("【表三】彙總（**帶號與絕對值並列**·`CLAUDE.md` 鐵律）")
    print("=" * W)
    for tag, _sb in SCEN:
        rows = summ[tag]
        dG = [r["dG"] for r in rows if r["dG"] is not None and abs(r["dG"]) > 0.005]
        dP = [r["dPos"] for r in rows if r["dPos"] is not None and r["dPos"] > 0.005]
        newp = [r for r in rows if r["處置"] == "新入可分配"]
        owners = sorted({r["所有權人"] for r in rows
                         if (r["dG"] is not None and abs(r["dG"]) > 0.005)
                         or (r["dPos"] is not None and r["dPos"] > 0.005)})
        newblk = sorted({r["blk"] for r in newp})
        med = (sorted(dP)[len(dP) // 2] if dP else None)
        print("── 情境 `%s`" % tag)
        print("   街角地面積有變動之街廓　　＝ %s（預期 ＝ 無·`P-5`）"
              % (sorted({f for f in FAIL if "P-5" in f}) or "無"))
        print("   位置外移之宗數　　　　　　＝ %d ／最大外移 %s m ／中位 %s m"
              % (len(dP),
                 ("%.2f" % max(dP)) if dP else "—",
                 ("%.2f" % med) if med is not None else "—"))
        print("   面積增減宗數　　　　　　　＝ %d ／`ΣΔ` ＝ %+.2f ／`Σ|Δ|` ＝ %.2f"
              % (len(dG), sum(dG), sum(abs(v) for v in dG)))
        print("   所有權人受影響戶數　　　　＝ %d ／%s" % (len(owners), owners))
        print("   因本批而首次可分配之街廓　＝ %s（宗數 %d）" % (newblk or "無", len(newp)))
        print()

    print("=" * W)
    if FAIL:
        print("🛑 **停機款候選** %d 項：" % len(FAIL))
        for t in sorted(set(FAIL)):
            print("   🛑 %s" % t)
        return 1
    print("✅ `P-5`／`P-6`／`P-8` ⋀ `c2` 預設生效檢 ⋀ 鍵之唯一性　**全綠**")
    print("=" * W)
    return 0


if __name__ == "__main__":
    sys.exit(main())
