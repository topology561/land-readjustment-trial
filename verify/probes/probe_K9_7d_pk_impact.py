# -*- coding: utf-8 -*-
r"""K-9-7-d 第二層分支之 **PK 影響評估**（K-6-A2 段四(c)-2(a) 立·段四(c) 切換後語意反轉）。

## 為何不能只換 `min_corner_area_p*`

改街角規定範圍會**同時**改變三條路徑（體例同 `probe_ruling_K9_7_pk_impact.py`）：

| # | 路徑 | 錨 |
|---|---|---|
| **(a)** | **候選資格**——宗地與範圍多邊形之相交面積 `> 1.0㎡` 才入候選 | `grep -n "_has_p1 = _inter_p1_area > 1.0" app.py` |
| **(b)** | **優先權指數三分項**——**三項之分母皆取自範圍多邊形** | `grep -n "score_corner_cut = 0.4" app.py` |
| **(c)** | **G 值門檻**——`min_area_to_apply` ＝ `min_corner_area_p1/p2` | `grep -n "cand_p1\['min_area_to_apply'\]" app.py` |

⇒ 本檔以**同一支 `select_corner_lots_both_sides_v12` 跑兩次**，
唯一變因＝**其內部所建之街角規定範圍多邊形**。

## 手法

🔄 **K-6-A2 段四(c) 切換後·語意已反轉**：
**新**輪＝生產原樣（**生產已走第二層**·零 patch）；
**舊**輪＝於 harvest 命名空間把 `_build_corner_range_v3` 換成
「注入**第一層 `t*`**」之包裝（只多傳 `_t_override=`·段三(a) 已入庫之純加性參數）。
⇒ **生產碼一字未改**。
⛔ 若沿用切換前之寫法（注入 `t_star`），兩輪同源 ⇒ 全表恆同、驗不到東西。

⛔ **禁只換 `min_corner_area_p*` 而沿用舊範圍多邊形**——那只測了 (c)。

## 重跑

    python verify/probes/probe_K9_7d_pk_impact.py

**rc 恆 0**（診斷·不作為閘）。輸出 `verify/out/probe_K9_7d_pk_impact.log`。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_K9_7d_pk_impact.log")

SIDE_ZH = {"left": "左", "right": "右"}

# diag 之欄名（實跑結構·勿臆造——前例：欄名錯致 16 格全讀 0、險以假「零翻盤」結案）
K_INT = "真交集(㎡)"      # (a) 宗地 ∩ 範圍多邊形
K_RNG = "範圍面積(㎡)"    # (b) 指數項三分母
K_R3 = "項三比(≤1)"       # (b) 項三比
K_TOT = "總分"            # (b) 優先權指數總分


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 128)
    L.append("【K-9-7-d 第二層分支之 PK 影響評估】第一層 vs 第二層（**生產已為第二層**）")
    L.append("三條路徑同時比較：(a) 候選資格 1.0㎡ / (b) 優先權指數三分項 / (c) G 值門檻")
    L.append("🔄 切換後語意反轉：新＝生產原樣（**第二層**·零 patch）；舊＝patch 注入**第一層** t*")
    L.append("=" * 128)

    ns, fake_st = harvest()
    for _s in ("k97_solve_alloc_t", "_build_corner_range_v3",
               "select_corner_lots_both_sides_v12", "_make_chamfer_tri_wb"):
        if not callable(ns.get(_s)):
            raise RuntimeError(f"🔴 harvest 未取得 {_s}")
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_parcels, build_parcels, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    fl_by = cad.get("front_lines", {}) or {}
    sd_by = cad.get("side_lines_by_side", {}) or {}
    al_by = cad.get("alloc_dir_by_block", {}) or {}
    bl_by = cad.get("baselines", {}) or {}
    legal_w = float(snapshot["global"]["法定最小寬_m"])

    # ── 1) 先算各 (街廓, 側, 情境) 之**第一層** t*（**舊**輪由 patch 注入）──────────
    T_OLD, DT = {}, {}
    for setback in (0.0, 3.5):
        for lbl in sorted(cb_by):
            b = cb_by[lbl]
            for side in ("left", "right"):
                if side not in (sd_by.get(lbl) or {}):
                    continue
                fl = fl_by.get(lbl) or {}
                if not (fl.get("p1") and fl.get("p2")):
                    continue
                r = ns["k97_solve_alloc_t"](
                    b.get("centroid"), [fl["p1"], fl["p2"]],
                    ns["_baseline_pts_from_manual"](bl_by.get(lbl), b.get("vertices")),
                    [sd_by[lbl][side]["p1"], sd_by[lbl][side]["p2"]],
                    al_by.get(lbl), setback, legal_w,
                    chamfer_tri=ns["_make_chamfer_tri_wb"](b, side),
                    block_depth=float(snapshot["blocks"][lbl]["街廓分配深度_m"]),
                    _label=lbl, _side=side, block_vertices=b.get("vertices"))
                # 🔴 **K-6-A2 段四(c) 語意反轉**（切換後）：生產已走第二層 ⇒
                #   需 patch 注入者為 **第一層**之 `t*`（「舊」輪）；「新」輪＝生產原樣。
                #   ⛔ 若沿用切換前之寫法（注入 `t_star`），兩輪同源 ⇒ 全表恆同、驗不到東西。
                T_OLD[(lbl, side, setback)] = r["t_star_layer1"]
                DT[(lbl, side, setback)] = r["t_star"] - r["t_star_layer1"]
    # **位移組／對照組由實算之 Δt* 定**（⛔ 不硬寫死格名·換圖即自動重分組）
    MOVED = {(l, s) for (l, s, _sb), d in DT.items() if abs(d) > 1e-12}
    L.append(f"位移組（|Δt*| > 0）＝ {sorted(MOVED)}｜"
             f"最大 |Δt*| ＝ {max(abs(v) for v in DT.values()):.9f} m")

    # ── 2) patch 機制 ──────────────────────────────────────────────────────
    _orig_range = ns["_build_corner_range_v3"]
    _v12_calls = []
    _orig_v12 = ns["select_corner_lots_both_sides_v12"]
    STATE = {"setback": None, "use_new": False, "patched_hits": 0}

    def _patched_range(*a, **kw):
        # 🔄 切換後：**舊**輪才需 patch（注入第一層 `t*`）；新輪＝生產原樣（第二層）。
        if not STATE["use_new"]:
            key = (kw.get("_label"), kw.get("_side"), STATE["setback"])
            if key in T_OLD and T_OLD[key] is not None:
                kw = dict(kw)
                kw["_t_override"] = T_OLD[key]
                STATE["patched_hits"] += 1
        return _orig_range(*a, **kw)

    def _spy_v12(**kw):
        _v12_calls.append({
            "use_new": STATE["use_new"], "setback": STATE["setback"],
            "min_p1": kw.get("min_corner_area_p1"), "min_p2": kw.get("min_corner_area_p2"),
            "base_front": kw.get("base_front_len_m"),
            "base_s1": kw.get("base_side_len_m_p1"), "base_s2": kw.get("base_side_len_m_p2"),
            "cut1": kw.get("cutoff_p1_end"), "cut2": kw.get("cutoff_p2_end"),
            "require_g": kw.get("require_g_map"),
            "n_cand": len(kw.get("candidates") or []),
            "g_map_n": len(kw.get("g_values_map") or {}),
        })
        return _orig_v12(**kw)

    ns["_build_corner_range_v3"] = _patched_range
    ns["select_corner_lots_both_sides_v12"] = _spy_v12

    def _run(setback, use_new):
        STATE["setback"] = setback
        STATE["use_new"] = use_new
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        diag, sel, off, winners, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params,
            temp_parcels, build_parcels, setback, snapshot=snapshot)
        return {"params": {r["街廓"]: r for r in params}, "diag": diag,
                "winners": winners, "forced": forced}

    RES = {}
    for setback in (0.0, 3.5):
        RES[(setback, False)] = _run(setback, False)
        RES[(setback, True)] = _run(setback, True)

    ns["_build_corner_range_v3"] = _orig_range
    ns["select_corner_lots_both_sides_v12"] = _orig_v12
    L.append(f"patch 命中次數（**舊**輪注入第一層 t* 之呼叫）＝ {STATE['patched_hits']}"
             f"｜新輪＝生產原樣（第二層）、零 patch")

    # ── 3) 逐格對照 ────────────────────────────────────────────────────────
    def _pick(res, lbl, side):
        """自 diag rows 取該街廓該側之候選／達標／winner／指數／forced。

        🔒 **欄名以實跑結構為準**：`端`（值 `左`／`右`）與 `候選地號`；
          winner 取自 `winners[lbl]['p1_end'|'p2_end']`（`左`→p1、`右`→p2）；
          `forced` 取自 `forced[lbl]['left_forced_offset'|'right_forced_offset']`。
        """
        zh = SIDE_ZH[side]
        rows = [d for d in res["diag"]
                if str(d.get("街廓")) == lbl and str(d.get("端")) == zh]
        cand = {str(d.get("候選地號")) for d in rows}
        qual = {str(d.get("候選地號")) for d in rows if str(d.get("達標")) == "達標"}
        _w = (res["winners"] or {}).get(lbl) or {}
        _wp = _w.get("p1_end" if side == "left" else "p2_end")
        win = {str(_wp)} if _wp else set()
        idx = {str(d.get("候選地號")): d.get("總分") for d in rows}
        _f = (res["forced"] or {}).get(lbl) or {}
        forced = bool(_f.get("left_forced_offset" if side == "left"
                             else "right_forced_offset"))
        return cand, qual, win, idx, forced

    CORNERS = [(lbl, side) for lbl in sorted(cb_by)
               for side in ("left", "right") if side in (sd_by.get(lbl) or {})]

    L.append("")
    L.append("【A】逐格對照（第一層範圍 vs 第二層範圍·唯一變因＝範圍多邊形）")
    L.append("-" * 128)
    _any_change = []
    for setback in (0.0, 3.5):
        old, new = RES[(setback, False)], RES[(setback, True)]
        for lbl, side in CORNERS:
            co, qo, wo, io, fo = _pick(old, lbl, side)
            cn, qn, wn, inw, fn = _pick(new, lbl, side)
            grp = "位移組" if (lbl, side) in MOVED else "對照組"
            _mo = old["params"][lbl].get(f"【{SIDE_ZH[side]}】街角最小面積(㎡)")
            _mn = new["params"][lbl].get(f"【{SIDE_ZH[side]}】街角最小面積(㎡)")
            chg = []
            if co != cn:
                chg.append(f"候選 進{sorted(cn - co)} 出{sorted(co - cn)}")
            if qo != qn:
                chg.append(f"合格 進{sorted(qn - qo)} 出{sorted(qo - qn)}")
            if wo != wn:
                chg.append(f"winner {sorted(wo) or '—'}→{sorted(wn) or '—'}")
            if fo != fn:
                chg.append(f"🔴forced_offset {fo}→{fn}")
            # 🔒 **決定性欄位**（候選／合格／winner／forced_offset）與**指數分數**分開記——
            #   前者變動＝**PK 翻盤**（土地後果）；後者變動可能只是小數位擾動、**不必然翻盤**。
            #   ⛔ 但**也不得逕自視為無事**：名次是否易位須由下方「指數前二」欄自行判讀。
            _decisive = bool(chg)
            if io != inw:
                _d = {k: (io.get(k), inw.get(k)) for k in set(io) | set(inw)
                      if io.get(k) != inw.get(k)}
                chg.append(f"指數分數變動（非決定性欄）{_d}")
            if chg:
                _any_change.append((setback, lbl, side, chg, _decisive))

            def _top2(d):
                def _num(v):
                    try:
                        return float(v)
                    except (TypeError, ValueError):
                        return float("-inf")
                return [(kk, d[kk]) for kk in
                        sorted(d, key=lambda kk: (_num(d[kk]), kk), reverse=True)[:2]]

            L.append(f"  {setback:g}m {lbl}/{side:<5} [{grp}] 門檻 {_mo}→{_mn}"
                     f"｜候選 {len(co)}→{len(cn)}｜合格 {len(qo)}→{len(qn)}"
                     f"｜winner {sorted(wo) or '—'}→{sorted(wn) or '—'}"
                     f"｜forced {fo}→{fn}"
                     f"｜{'🔴 ' + '；'.join(chg) if chg else '✅ 全同'}")
            L.append(f"        指數前二（舊）{_top2(io)}　（新）{_top2(inw)}")
    L.append("-" * 128)

    # ── 3b) 三條路徑「確實被走到」之佐證 ───────────────────────────────────
    L.append("")
    L.append("【A2】三條路徑確實被走到之佐證（若只換 (c)，下列 (a)(b) 欄必逐格不變）")
    L.append("-" * 128)
    L.append(f"  {'情境':<6}{'街廓/端':<12}{'候選地號':<14}"
             f"{'(a)真交集(㎡)':>20}{'(b)範圍面積(㎡)':>20}{'(b)項三比':>14}{'(b)總分':>12}")
    L.append("-" * 128)
    _n_a = _n_b = 0
    for setback in (0.0, 3.5):
        old, new = RES[(setback, False)], RES[(setback, True)]
        _o = {(str(d.get("街廓")), str(d.get("端")), str(d.get("候選地號"))): d
              for d in old["diag"]}
        _n = {(str(d.get("街廓")), str(d.get("端")), str(d.get("候選地號"))): d
              for d in new["diag"]}
        for key in sorted(set(_o) & set(_n)):
            a, b = _o[key], _n[key]
            _da = a.get(K_INT) != b.get(K_INT)
            _db = (a.get(K_RNG) != b.get(K_RNG)
                   or a.get(K_R3) != b.get(K_R3)
                   or a.get(K_TOT) != b.get(K_TOT))
            if not (_da or _db):
                continue
            _n_a += int(_da)
            _n_b += int(_db)
            L.append(f"  {setback:g}m{'':<3}{key[0] + '/' + key[1]:<10}{key[2]:<13}"
                     f"{f'{a.get(K_INT)}→{b.get(K_INT)}':>22}"
                     f"{f'{a.get(K_RNG)}→{b.get(K_RNG)}':>20}"
                     f"{f'{a.get(K_R3)}→{b.get(K_R3)}':>16}"
                     f"{f'{a.get(K_TOT)}→{b.get(K_TOT)}':>16}")
    L.append("-" * 128)
    L.append(f"  ⇒ (a) 真交集 有變之列 {_n_a}；(b) 範圍面積／項三比／總分 有變之列 {_n_b}")
    L.append("     **二者皆 > 0 ⇒ (a)(b) 路徑確實隨新範圍變動、非僅換 (c) 門檻。**"
             if (_n_a or _n_b) else
             "     ⚠️ 二者皆 0 ⇒ 於本圖上第二層對 (a)(b) 之數值影響低於其列印精度；"
             "**須另以【A】之門檻欄與 probe_K9_7d_layer2【B】之面積欄佐證 patch 確有生效**。")

    # ── 4) 結論 ────────────────────────────────────────────────────────────
    L.append("")
    L.append("【B】結論（PK 十六格）")
    _dec = [x for x in _any_change if x[4]]
    _nondec = [x for x in _any_change if not x[4]]
    if not _dec:
        L.append("  ✅ **決定性欄位零翻盤**：十六格之**候選集合、合格集合、winner、"
                 "`forced_offset` 皆逐格相同**。")
    else:
        L.append(f"  🔴 **決定性欄位有變動：{len(_dec)} 格 ⇒ PK 翻盤·須停機上呈**")
        for sb, lbl, side, chg, _ in _dec:
            L.append(f"     {sb:g}m {lbl}/{side}：" + "；".join(chg))
    if _nondec:
        L.append(f"  ⚠️ **指數分數有變動（非決定性欄）：{len(_nondec)} 格**"
                 "——⛔ 不得逕自視為無事，名次是否易位請對照上表「指數前二」欄：")
        for sb, lbl, side, chg, _ in _nondec:
            L.append(f"     {sb:g}m {lbl}/{side}：" + "；".join(chg))
    else:
        L.append("  ✅ 指數分數亦逐格相同。")

    # ── 5) 受控比較之佐證 ──────────────────────────────────────────────────
    L.append("")
    L.append("【C】受控比較佐證：v12 實際傳入引數（舊輪 vs 新輪·除門檻外應逐項相同）")
    L.append("-" * 128)
    _by = {}
    for c in _v12_calls:
        _by.setdefault((c["setback"], c["use_new"]), []).append(c)
    for setback in (0.0, 3.5):
        o = _by.get((setback, False), [])
        n = _by.get((setback, True), [])
        L.append(f"  ── {setback:g}m｜v12 呼叫次數 舊 {len(o)} / 新 {len(n)} ──")
        for i, (a, b) in enumerate(zip(o, n)):
            _diff = [kk for kk in ("base_front", "base_s1", "base_s2", "cut1", "cut2",
                                   "require_g", "n_cand", "g_map_n")
                     if a[kk] != b[kk]]
            L.append(f"     #{i}: 門檻 p1 {a['min_p1']}→{b['min_p1']}"
                     f"／p2 {a['min_p2']}→{b['min_p2']}"
                     f"｜其餘引數 {'✅ 逐項相同' if not _diff else '🔴 有差:' + str(_diff)}"
                     f"（require_g={a['require_g']}·候選 {a['n_cand']}·gmap {a['g_map_n']}）")
    L.append("-" * 128)
    L.append("")
    L.append("【D】註記")
    L.append("  · 🔴 **段四(c) 後生產已走第二層**（`grep -n -A4 \"_k97 = k97_solve_alloc_t\" app.py`"
             " 之四行內含 `block_vertices`）；patch 僅存在於本行程、生產碼一字未改。")
    L.append("  · 三條路徑皆隨範圍多邊形變動——patch 的是 v12 內部所呼叫之 "
             "`_build_corner_range_v3`，")
    L.append("    故 (a) 候選資格、(b) 指數三分項分母、(c) G 值門檻 同時改用新範圍。")
    L.append("  · 位移組／對照組**由實算之 Δt* 定**，⛔ 非硬寫死格名。")

    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
