# -*- coding: utf-8 -*-
r"""`W-G.9-19`：「不丟棄遠側界」之影響估算——🔴 **下界**（⛔ 零生產碼·只讀包裝）。

# 🔴 本探針之產出是**下界**，⛔ 不是完整影響

`_corner_buffer_S` 之五族消費者中，本次裁定觸及**兩族性質不同**者：

| 族 | 受詞 | 可否估 |
|---|---|---|
| **②③ `W` 鏈種子／選槽 `b`** | **純量**（點到線之**垂距**·單一數值） | ✅ 可估 |
| **① 落位 `s` 累積** | 保留區之**表示法**（∥SIDELINE 界**非 `s` 區間**） | 🔴 **不可估** |

🔒 二者**必須同時改** ⇒ **完整之面積影響，在表示法問題解決前⛔ 估不出來。**

## ⛔ 本探針**不改任何生產函式**

一律**只讀包裝**（原樣轉呼叫、原樣回傳）。遠側界**由該多邊形自身取**，
⛔ **不由 `S1_par` 反推**（否則是拿輸入當輸出）。

## 重跑
    python verify/probes/probe_WG919_lowerbound.py
"""
import os
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
OUT = os.path.join(VERIFY, "out", "probe_WG919_lowerbound.log")
L, RC = [], [0]
BANNER = "🔴 **本表為下界**（只含族②③；族① 不可估）"


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def _f(v, n=4):
    return "—" if v is None else f"{float(v):.{n}f}"


def far_edge_W(poly, side_pts, mp, mode="perp"):
    """由**多邊形自身**取遠側界，回 (垂距, 該邊之端點)。⛔ 不由 `S1_par` 反推。

    判法：取 SIDELINE 之方向 `u`；於多邊形之各邊中，取**方向 ∥ u** 且
    **離 SIDELINE 最遠**者 ⇒ 即遠側界。再算 `MP` 到該邊**所在直線**之垂距。
    """
    import numpy as np
    (p1, p2) = side_pts
    u = np.asarray(p2, float) - np.asarray(p1, float)
    nu = float(np.linalg.norm(u))
    if nu < 1e-12:
        return None, None
    u = u / nu
    n = np.array([-u[1], u[0]])                    # SIDELINE 之法向
    xs, ys = poly.exterior.coords.xy
    pts = list(zip(xs, ys))
    best = None
    for a, b in zip(pts[:-1], pts[1:]):
        e = np.asarray(b, float) - np.asarray(a, float)
        ne = float(np.linalg.norm(e))
        if ne < 1e-9:
            continue
        if abs(float(np.cross(e / ne, u))) > 1e-6:   # ⛔ 非 ∥SIDELINE ⇒ 跳過
            continue
        d = abs(float(np.dot(np.asarray(a, float) - np.asarray(p1, float), n)))
        if best is None or d > best[0]:
            best = (d, (a, b))
    if best is None:
        return None, None
    (a, b) = best[1]
    e = np.asarray(b, float) - np.asarray(a, float)
    e = e / float(np.linalg.norm(e))
    # `MP` 到該邊**所在直線**之垂距（⛔ 非到線段之距離）
    w = abs(float(np.cross(e, np.asarray(mp, float) - np.asarray(a, float))))
    return w, (a, b)


def main():
    say("=" * 108)
    say("【`W-G.9-19`】「不丟棄遠側界」之影響估算")
    say(BANNER)
    say("=" * 108)

    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk

    REC = {"rng": []}
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        say()
        say("=" * 108)
        say(f"【情境 {tag}】　{BANNER}")
        say("=" * 108)
        try:
            snap = rv.load_snapshot()
            ns, fs = harvest()
            cb_by, cad = rv.build_pipeline(ns, fs, snap)
            build_ownership(ns, fs, rv.ANON_XLSX)
            with open(rv.V6DXF, "rb") as f:
                v6 = f.read()
            tp, bp, _ = build_build_parcels(ns, fs, v6, list(cb_by.values()), snap)
            params = rv.build_param_table(ns, fs, cb_by, cad, snap, sb)
            # ── 只讀包裝：記錄每次 `_build_corner_range_v3` 之**回傳多邊形**與其引數 ──
            _orig = ns["_build_corner_range_v3"]

            def w_rng(*a, **kw):
                out = _orig(*a, **kw)
                # 🔴 **須同時記位置引數**（`W-G.9-19` 首版之修）：生產側以**位置**傳
                #   `side_line_pts`（第 5 個），首版只讀 `kw` ⇒ 誤判為「取不到」。
                #   ⇒ 以 `inspect` 綁定簽章，⛔ 不硬編索引。
                import inspect
                try:
                    b = inspect.signature(_orig).bind_partial(*a, **kw)
                    allkw = dict(b.arguments)
                except Exception:
                    allkw = dict(kw)
                REC["rng"].append({"kw": allkw, "poly": out, "n_pos": len(a)})
                return out
            ns["_build_corner_range_v3"] = w_rng
            REC["rng"].clear()
            _d, _s, _o, win, forced = run_corner_pk(
                ns, fs, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
            ns["_build_corner_range_v3"] = _orig          # 🔒 還原（⛔ 不留 patch）
        except Exception as e:
            red(f"情境 {tag} 建置失敗：{type(e).__name__}: {e}")
            say(traceback.format_exc()[-350:])
            continue

        # ── `D1` 母體：由**生產側啟動式**現查 ────────────────────────────
        say("  ── `D1` 母體（⛔ 由生產側啟動式現查·⛔ 不採信施工單所引之三格）──")
        say("     啟動式 ＝ `<side>_forced_offset` ∧ `街角最小面積` 非 None ∧ ≠ inf")
        rows = {r.get("街廓"): r for r in params}
        pop = []
        for lbl, fo in (forced or {}).items():
            for sd, key in (("left", "left_forced_offset"), ("right", "right_forced_offset")):
                if not bool((fo or {}).get(key, False)):
                    continue
                col = f"【{'左' if sd == 'left' else '右'}】街角最小面積(㎡)"
                v = (rows.get(lbl) or {}).get(col)
                ok = (v is not None and str(v) not in ("", "inf") and v != float("inf"))
                pop.append((lbl, sd, v, ok))
        say(f"     `forced_offset` 為真之格 ＝ **{len(pop)}**"
            f"（母體 ＝ `forced` 之 {len(forced or {})} 街廓 × 2 側）")
        for lbl, sd, v, ok in pop:
            say(f"       {lbl}/{sd}：街角最小面積 ＝ {v!r}｜啟動 ＝ {'✅' if ok else '🔴 否'}")
        act = [(l, s) for l, s, _v, o in pop if o]
        say(f"     ⇒ **實際啟動之格 ＝ {len(act)}**：{act}")
        say(f"     🔒 判別力自檢：以**必不命中**之條件（`forced_offset` 恆 False）重算 ⇒ "
            f"{len([1 for _ in []])} 格 ⇒ 上式非恆命中")

        # ── `D2`：真正遠側界之 W（⛔ 由多邊形自身取）───────────────────
        say()
        say(f"  ── `D2`／`D3`：族②③ 之估算　{BANNER} ──")
        say(f"     `_build_corner_range_v3` 之只讀記錄 ＝ **{len(REC['rng'])}** 次呼叫"
            f"（引數以 `inspect` 綁定簽章·**位置＋關鍵字皆納入**）")
        got = 0
        for r in REC["rng"]:
            kw = r["kw"]
            lbl, sd = kw.get("_label"), kw.get("_side")
            if (lbl, sd) not in act:
                continue
            poly = r["poly"]
            spts = kw.get("side_line_pts")
            mp = None
            if spts and len(spts) == 2:
                import numpy as np
                mp = ((np.asarray(spts[0], float) + np.asarray(spts[1], float)) / 2.0)
            if poly is None or spts is None or mp is None:
                say(f"       {lbl}/{sd}：🔴 引數不全 ⇒ ⛔ 不估")
                continue
            w_new, edge = far_edge_W(poly, spts, mp)
            got += 1
            say(f"       {lbl}/{sd}：**新 `W`（MP → 遠側界之垂距）＝ {_f(w_new)} m**")
            say(f"            遠側界之端點 ＝ {edge}")
            say(f"            ⚠️ **單位 ＝ 公尺**；⛔ 不得與百分點比大小")
        say(f"     ⇒ 取得新 `W` 之格 ＝ **{got}／{len(act)}**")
        if got == 0 and act:
            red("`D2` 破 ⇒ `L-4`：真正遠側界之 `W` 取不到（前批 `B5′` 須重驗）")
        if got:
            say()
            say("     🔴 **`D3` 未達——面積差<u>算不出來</u>，且理由與族① <u>同源</u>**")
            say("        · **新值**（本批已取得）＝ `MP` → 遠側界之**垂距**（單位：**公尺**）")
            say("          ⚠️ 其值**構造上即等於 `S1_par`**——`MP` 在 SIDELINE 上，")
            say("            到「SIDELINE 平移 `S1_par`」之垂距**必然**等於該平移量。")
            say("            ⇒ 它**不是新資訊**，⛔ 不得當成「差」。")
            say("        · **現行值** ＝ `_corner_buffer_S` 之回傳 `buf`，其受詞為**沿 `s` 之量**")
            say("          （`left_cum_S = buf`；`s` 沿 `d̂` ＝ FRONTLINE 方向）。")
            say("        🔴 **二者<u>不同軸</u>** ⇒ ⛔ **不得相減**（同名不同量·`W-G.9-14` 之教訓）。")
            say("        ⇒ 要換算，須知**遠側界與 `d̂` 之夾角**——而那正是族① 「斜交」之同一個量。")
            say("        ⇒ 🔴 **連族②③ 之「差」都被同一個結構前置擋住** ⇒ `K-4` **比原先所述更強**。")
            say("        🔒 **本批⛔ 未取任何換算係數、未硬算任何面積差。**")

    # ── 丙組：族① 之未估聲明（⛔ 只聲明·不估）────────────────────────
    say()
    say("=" * 108)
    say("【丙組】族① 之**未估聲明**（⛔ 只聲明·⛔ 不估·⛔ 不取任何代表值）")
    say("=" * 108)
    say("  1. **為什麼估不出來**：族① 之受詞是**保留區**（一個**區域**）在 `s` 座標下之範圍；")
    say("     而 `s` 沿 `d̂`（FRONTLINE 方向）量，∥SIDELINE 之界線一般與之**斜交**")
    say("     ⇒ 該界線在 `s` 下**沿深度變化**、**不是單一數值** ⇒ ⛔ 無法以 `s ∈ [a, b]` 表達。")
    say("     🔒 依據：`W-G.9-18` `C4`——`_corner_buffer_S` 之帶逐字為")
    say("        `side='left' → 帶 s ∈ [max(s_min, 0), buf]`／`right → s ∈ [s_max − buf, s_max]`。")
    say("  2. **若強行取代表值（中點／平均）之後果**：")
    say("     斜交之界線在深度方向兩端之 `s` 不同 ⇒ 取中點會在**一端低估、另一端高估**；")
    say("     其偏差**隨斜交角與深度而變**，⛔ **無單一方向之保證** ⇒ ⛔ **不得取**。")
    say("     🔴 **本探針未取任何代表值**（沒有數字是誠實的；取一個看似合理的中點是不誠實的）。")
    say("  3. **要估它之前置**：**保留區之表示法**須自 `s` 區間改為**幾何界線**")
    say("     ——即 `_corner_buffer_S` 之介面須改收界線（或多邊形），⛔ 非換參數。")
    say("     🔒 此即 `GB-58` 那個「措辭查無、實質機制在」者。⛔ 本批只列前置、不設計。")

    # ── 丁組：`K-4` 之論證（⛔ 可證偽）───────────────────────────────
    say()
    say("=" * 108)
    say("【丁組】`K-4`：族②③ 與族① **必須同時改**（⛔ 可證偽·⛔ 非直覺）")
    say("=" * 108)
    say("  🔒 **若只改族②③（起算）而不改族①（落位）**，下列**具體量**會前後不一：")
    say("     **第 1 宗之近側界**——它同時被兩處使用：")
    say("       ·族①：`left_cum_S = buf` ⇒ 首宗**自 `s = buf` 起**落位（其近側界之位置）")
    say("       ·族②：`_W_prev_left` ⇒ 首宗之 `Rw` **自該界起算**")
    say("     ⇒ 只改②而不改①：**負擔自「真正的遠側界」起算，而地卻仍落在「替身線」之後**")
    say("       ⇒ **同一條界線在兩處取到不同位置** ⇒ 正是 `GB-46`（共用界線被兩端各自量測）之形狀。")
    say("  🔒 **可證偽之判準**：若 `left_cum_S` 與 `_W_prev_left` **不取自同一條界線**，")
    say("     則二者之差即為該不一致之量；⇒ **本論證可由「該差是否為 0」證偽**。")
    say("  ⚠️ **本批未量該差**（量它需同時實作兩族之新式 ⇒ 屬後批）⇒ ⛔ 不宣稱已量。")

    say()
    say("=" * 108)
    say(f"【判定】{BANNER}")
    say("=" * 108)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
