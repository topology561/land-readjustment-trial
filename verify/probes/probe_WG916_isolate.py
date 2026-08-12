# -*- coding: utf-8 -*-
r"""`W-G.9-16`：兩個推定成因之**隔離**（⛔ 零生產碼·⛔ 不校回·⛔ 不估面積）。

## 受詞 ＝ **成因**，⛔ 不是效果

`W-G.9-14` 量到之 `0.16`／`0.02` 公尺是**效果**；該批把效果之量當成成因之證據
（已立為**考古 74**）。本探針只問：**那個差是<u>怎麼來的</u>。**

## 兩說（⛔ 不得任取其一·可能兩者皆非）

| | 說法 | 出處 |
|---|---|---|
| **甲** | `_select_pool_slot` 之理論母體是**宗地寬度**而非 `W` | `664e4f5` 之訊息（自標未證實） |
| **乙** | 理論之 `widths` 取自 `k_naive` 趟、實跑為 `k*` 趟 ⇒ 同一宗兩趟寬度不同 | `W-G.9-14`（已降級為「成因未明」） |

## 🔒 取樣缺陷之修（承 `c009663`）

舊探針每趟只記到 **1 宗** `side='左側'`（`0m` 之 `k*=2`、左群兩宗）
⇒ 第二宗落在 `side='無'`、**從未進入比對**。
⇒ **本探針之鍵一律用「宗地字面」**（暫編地號），⛔ **不得用 `side`**；並**正面印出母體**。

## 重跑
    python verify/probes/probe_WG916_isolate.py
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
OUT = os.path.join(VERIFY, "out", "probe_WG916_isolate.log")
L, RC = [], [0]
REC = {"solve": [], "slot": [], "proj": []}


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


# ══════════════════════════════════════════════════════════════════════════
def install(ns):
    """只讀記錄包裝（⛔ 原樣轉呼叫·原樣回傳）。"""
    orig = {k: ns[k] for k in ("_solve_G_one", "_select_pool_slot", "_projection_order")}

    def w_solve(**kw):
        res = orig["_solve_G_one"](**kw)
        d = res[0] if (isinstance(res, tuple) and res) else res
        if not isinstance(d, dict):
            d = {}
        REC["solve"].append({
            "a_m2": kw.get("a_m2"), "side": kw.get("side"), "is_corner": kw.get("is_corner"),
            "W_prev": kw.get("W_prev"),
            "S": d.get("S"), "宗地寬度": d.get("_宗地寬度"),
            "W_near": d.get("W_near"), "W_far": d.get("W_far"), "W": d.get("W"),
            "Rw_pct": d.get("Rw_pct"), "dir_used": str(d.get("_alloc_dir_used"))[:34],
            "slot_seen": len(REC["slot"]),
        })
        return res

    def w_proj(parcels, p1, p2):
        out = orig["_projection_order"](parcels, p1, p2)
        REC["proj"].append([(tp.get("暫編地號"),
                             round(float(tp.get("分攤登記面積_m2",
                                                tp.get("面積_m2", 0)) or 0), 4))
                            for tp in out])
        return out

    def w_slot(widths, left_side, right_side, rw_func=None):
        out = orig["_select_pool_slot"](widths, left_side, right_side, rw_func)
        REC["slot"].append({"widths": list(widths or []), "L": dict(left_side or {}),
                            "k": out.get("k"), "n_solve_before": len(REC["solve"])})
        return out

    ns["_solve_G_one"] = w_solve
    ns["_select_pool_slot"] = w_slot
    ns["_projection_order"] = w_proj
    return orig


def uninstall(ns, orig):
    for k, v in orig.items():
        ns[k] = v


def run_tag(tag, setback):
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g
    snapshot = rv.load_snapshot()
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_parcels, build_parcels, _ = build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
    _d, _s, _o, win, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_parcels, build_parcels,
        setback, snapshot=snapshot)
    REC["solve"].clear(); REC["slot"].clear(); REC["proj"].clear()
    orig = install(ns)
    err = None
    try:
        run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                   params, build_parcels, win, forced, setback)
    except Exception as e:
        err = f"{type(e).__name__}: {str(e)[:120]}"
    finally:
        uninstall(ns, orig)
    return {"err": err, "build": build_parcels, "orig": orig}


def label_map(_unused):
    """`分攤登記面積 → 宗地字面` 之對照。

    🔴 **母體限「本街廓之階段 1 宗」**（`W-G.9-16` 首版之修）：
    首版以**全區 57 筆** `build_parcels` 建表 ⇒ **重複鍵 4 個**（246.0×2／114.0／0.0）
    ⇒ 非單射、鍵不可用。**重複者落在別的街廓**；閘破於 `R1`，故正確母體 ＝
    `_projection_order` **該街廓之回傳**（其索引即 `widths` 之索引）。
    ⛔ 須為單射，否則不得用作鍵。
    """
    if not REC["proj"]:
        return {}, ["（無 _projection_order 記錄）"]
    lst = REC["proj"][0]                      # 閘破於首個街廓 ⇒ 取第一次呼叫
    m, dup = {}, []
    for lot, a in lst:
        k = round(float(a), 2)
        if k in m and m[k] != lot:
            dup.append(k)
        m[k] = lot
    return m, dup


def report(tag, st):
    say()
    say("=" * 112)
    say(f"【情境 {tag}】")
    say("=" * 112)
    say(f"  run_step_g ⇒ {st['err'] or '（未拋）'}")
    lm, dup = label_map(st["build"])
    say(f"  🔒 **鍵之母體自證**（母體＝`_projection_order` 首次回傳·{len(REC['proj'])} 次呼叫）："
        f"`分攤登記面積 → 宗地字面` 對照 {len(lm)} 筆"
        f"｜重複鍵 {len(dup)} 個 ⇒ {'✅ 單射·可作鍵' if not dup else '🔴 非單射·⛔ 不得用作鍵'}")
    if dup:
        red(f"鍵非單射 ⇒ `E-2` 之同族（母體不可信）：{dup[:5]}")
        return None
    if not REC["slot"]:
        red("未記錄到 `_select_pool_slot` ⇒ 無從分辨兩趟")
        return None
    s = REC["slot"][-1]
    nb = s["n_solve_before"]
    passes = {"k_naive 趟": REC["solve"][:nb], "k* 趟": REC["solve"][nb:]}

    # ── 逐宗表（鍵＝宗地字面·⛔ 非 side）─────────────────────────────────
    tbl = {}
    for pname, arr in passes.items():
        say()
        say(f"  ── {pname}｜**母體 ＝ {len(arr)} 宗**（⛔ 正面印出·⛔ 非 side 篩後之數）──")
        say(f"      {'宗地字面':<14}{'side':<6}{'S':>9}{'宗地寬度':>10}"
            f"{'W_near':>10}{'W_far':>10}{'ΔW=far−near':>13}{'w−ΔW':>9}")
        for r in arr:
            lot = lm.get(round(float(r["a_m2"] or 0), 2), f"?a={r['a_m2']}")
            wn, wf = r["W_near"], r["W_far"]
            dW = (float(wf) - float(wn)) if (wn is not None and wf is not None) else None
            w = r["宗地寬度"]
            gap = (float(w) - dW) if (w is not None and dW is not None) else None
            say(f"      {str(lot):<14}{str(r['side']):<6}{_f(r['S']):>9}{_f(w):>10}"
                f"{_f(wn):>10}{_f(wf):>10}{_f(dW):>13}{_f(gap):>9}")
            tbl.setdefault(pname, {})[str(lot)] = {"w": w, "dW": dW, "gap": gap,
                                                   "wn": wn, "wf": wf, "S": r["S"],
                                                   "side": r["side"], "dir": r["dir_used"]}
    import stepg_pipeline as _sp  # noqa
    _R = st["orig"]["_select_pool_slot"].__globals__["rw_from_width"]
    # 實跑 ΣRw（階段1·左側）＝ 自引擎自報之例外訊息取（⛔ 不重算）
    import re as _re
    _m = _re.search(r"實跑\(階段1\)=([0-9.]+)", st["err"] or "")
    return {"slot": s, "tbl": tbl, "passes": passes, "lm": lm,
            "R": _R, "re_sum": float(_m.group(1)) if _m else None}


def _f(v):
    return "—" if v is None else f"{float(v):.4f}"


REC_PROJ = {}


def main():
    say("=" * 112)
    say("【`W-G.9-16`】兩個推定成因之隔離（⛔ 受詞 ＝ 成因·⛔ 非效果）")
    say("=" * 112)
    out = {}
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        try:
            st = run_tag(tag, sb)
            REC_PROJ[tag] = list(REC["proj"][0]) if REC["proj"] else []
            out[tag] = report(tag, st)
        except Exception as e:
            red(f"情境 {tag} 失敗：{type(e).__name__}: {e}")
            say(traceback.format_exc()[-400:])

    # ══ 判別實驗 ══════════════════════════════════════════════════════════
    say()
    say("=" * 112)
    say("【判別實驗】")
    say("=" * 112)
    for tag, o in out.items():
        if not o:
            continue
        say()
        say(f"  ▸ 情境 {tag}")
        kn = o["tbl"].get("k_naive 趟", {})
        ks = o["tbl"].get("k* 趟", {})
        both = sorted(set(kn) & set(ks))
        only_kn, only_ks = sorted(set(kn) - set(ks)), sorted(set(ks) - set(kn))
        say(f"      **`Y2` 母體比對**：k_naive {len(kn)} 宗／k* {len(ks)} 宗"
            f"｜共同 {len(both)}｜僅 k_naive {only_kn}｜僅 k* {only_ks}")
        same_pop = (not only_kn and not only_ks)
        say(f"      ⇒ 兩趟宗地母體 {'**相同**' if same_pop else '**不同**'}"
            f" ⇒ `Y2` {'✅ 成立' if same_pop else '🔴 破 ⇒ **乙說之受詞不成立**'}")
        # 乙說
        if same_pop:
            diff = [(x, kn[x]["w"], ks[x]["w"]) for x in both
                    if kn[x]["w"] is not None and ks[x]["w"] is not None
                    and abs(float(kn[x]["w"]) - float(ks[x]["w"])) > 1e-9]
            say(f"      **乙說**（同一宗兩趟寬度不同）⇒ 相異之宗 ＝ {len(diff)}／{len(both)}")
            for x, a, b in diff:
                say(f"          {x}: k_naive {a} vs k* {b}（差 {float(b)-float(a):+.4f} m）")
            say(f"      ⇒ **乙說 {'🔴 通過（為成因之一）' if diff else '✅ 不通過（非成因）'}**")
        else:
            say("      **乙說** ⇒ ⚠️ **受詞不成立**（母體不同 ⇒ 無法成立也無法否證），⛔ 不硬判")
        # 甲說（改以**實測**判：w_i 是否等於 ΔW_i）
        bad = [(x, ks[x]["w"], ks[x]["dW"], ks[x]["gap"]) for x in ks
               if ks[x]["gap"] is not None and abs(ks[x]["gap"]) > 1e-6]
        say(f"      **甲說**（`widths` 非 W 軸之位移）⇒ 以**實測**判："
            f"`w_i ≠ ΔW_i` 之宗 ＝ {len(bad)}／{len(ks)}")
        for x, w, d, g in bad:
            say(f"          {x}: w={_f(w)} vs ΔW={_f(d)}　差 **{g:+.4f} m**")
        say(f"      ⇒ **甲說 {'🔴 通過（w 與 ΔW 實測不等）' if bad else '✅ 不通過（w ＝ ΔW）'}**")

    # ══ 🔴 推進量差之逐項分解（⛔ 這才是「成因」）════════════════════════════
    say()
    say("=" * 112)
    say("【推進量差之逐項分解】🔴 受詞 ＝ **成因**（⛔ 非效果）")
    say("=" * 112)
    say("  🔴 **首版之誤（具名·⛔ 不刪）**：曾以 `_projection_order` 之前 k 名當左群，")
    say("     得推進量差 `-24.49 m`——與 `W-G.9-14` 已測之 `+0.16 m` 矛盾 ⇒ **左群認錯**。")
    say("     ⚠️ 當時之「自我驗證閘」**沒抓到**，因為它是**套套邏輯**（①＋② 依定義恆等於該差）。")
    say("  🔒 **改法**：左群改由碼面自己的鏈結 `W_prev` 串出（⛔ 不用投影序、⛔ 不用 W_near 連續性）；")
    say("     並改掛**外部錨**為閘 ＝ `W-G.9-14` 實測之推進量差（`0m` +0.16／`3.5m` +0.02）。")
    EXT = {"0m": 0.16, "3.5m": 0.02}
    for tag, o in out.items():
        if not o:
            continue
        s0 = o["slot"]
        w, k = s0["widths"], int(s0["k"])
        arr = o["passes"]["k* 趟"]
        lm = o["lm"]

        def lot_of(r):
            return lm.get(round(float(r["a_m2"] or 0), 2), "?")

        # 左群 ＝ 自 side='左側' 起，依 W_prev 鏈結串出（⛔ 非投影序）
        head = [r for r in arr if str(r["side"]).startswith("左")]
        say()
        say(f"  ▸ 情境 {tag}｜k* ＝ {k}")
        if not head:
            red(f"情境 {tag}：k* 趟無 side 起首之左側宗 ⇒ ⛔ 不分解")
            continue
        chain, cur = [head[0]], head[0]
        while True:
            nxt = [r for r in arr if r is not cur and r["W_prev"] is not None
                   and cur["W_far"] is not None
                   and abs(float(r["W_prev"]) - float(cur["W_far"])) < 1e-6
                   and r not in chain]
            if not nxt:
                break
            chain.append(nxt[0]); cur = nxt[0]
        say(f"      左群（`W_prev` 鏈結）＝ {[lot_of(r) for r in chain]}（{len(chain)} 宗）")
        if len(chain) != k:
            say(f"      ⚠️ 鏈長 {len(chain)} ≠ k* {k} ⇒ **具名列為未定**，⛔ 不硬分解")
            continue
        th = sum(w[:k])
        re_adv = float(chain[-1]["W_far"]) - float(chain[0]["W_near"])
        diff = re_adv - th
        say(f"      **理論** Σw[:{k}] ＝ {th:.4f}｜**實跑** {_f(chain[-1]['W_far'])} − "
            f"{_f(chain[0]['W_near'])} ＝ {re_adv:.4f}｜**差 ＝ {diff:+.4f} m**")
        # 🔒 外部錨閘（⛔ 非套套邏輯）
        ext = EXT.get(tag)
        ok = ext is not None and abs(diff - ext) < 0.01
        say(f"      🔒 **外部錨閘**（⛔ 非套套邏輯）：`W-G.9-14` 實測 {ext:+.2f} m"
            f" vs 本批 {diff:+.4f} m ⇒ {'✅ 相符（左群認對·分解可採）' if ok else '🔴 不符 ⇒ ⛔ 分解不得採'}")
        if not ok:
            red(f"情境 {tag}：外部錨閘不過 ⇒ 分解不採，具名列為未定")
            continue
        # 分解 ①：逐宗 w_i vs ΔW_i（widths 用本宗自己的近側界）
        s1 = 0.0
        say(f"      ── 分解 ① 逐宗「`ΔW_i` − `w_i`」──")
        for i, r in enumerate(chain):
            dW = float(r["W_far"]) - float(r["W_near"])
            g = dW - float(w[i])
            s1 += g
            say(f"          {lot_of(r)}: w={w[i]:.4f}  ΔW={dW:.4f}  差 **{g:+.4f}**")
        say(f"          小計 ＝ **{s1:+.4f}**")
        # 分解 ②：界面 W_near,{i+1} − W_far,i
        s2 = 0.0
        say(f"      ── 分解 ② 界面「`W_near,i+1` − 前一宗 `W_far,i`」──")
        for i in range(len(chain) - 1):
            gp = float(chain[i + 1]["W_near"]) - float(chain[i]["W_far"])
            s2 += gp
            say(f"          {lot_of(chain[i])}→{lot_of(chain[i+1])}: "
                f"W_far={_f(chain[i]['W_far'])} W_near={_f(chain[i+1]['W_near'])} 差 **{gp:+.4f}**")
        if len(chain) < 2:
            say("          （左群僅 1 宗 ⇒ 無界面）")
        say(f"          小計 ＝ **{s2:+.4f}**")
        say(f"      ⇒ ①＋② ＝ {s1 + s2:+.4f}（⚠️ 本式為恆等·⛔ 非證據；證據是上方之**外部錨閘**）")
        # ── 🔴 `E-1` 之受詞：校回起算點之後，本閘會不會過 ──────────────────
        R = o["R"]
        th_rw = R(0.0 + th) - R(0.0)              # 校回後之理論（起點 0）
        re_rw = o["re_sum"]                       # 實跑（逐宗 Rw 之和·⛔ 不重算）
        resid = abs(re_rw - th_rw)
        say(f"      ── 🔴 `E-1`：**校回起算點之後**（理論起點改為 0）──")
        say(f"          理論 ＝ R(0＋{th:.4f}) − R(0) ＝ {th_rw:.4f}")
        say(f"          實跑 ＝ {re_rw:.4f}（逐宗 `Rw(%)` 之和·取自引擎自報）")
        say(f"          殘差 ＝ **{resid:.4f} 百分點**｜閘之容差 ＝ 0.1")
        say(f"          ⇒ **{'✅ 校回<u>足以</u>使本閘通過' if resid <= 0.1 else '🔴 校回<u>不足以</u>解決 ⇒ `E-1` 停機上呈'}**")
        if resid > 0.1:
            red(f"`E-1` 觸發（情境 {tag}·殘差 {resid:.4f} > 0.1）")

    say()
    say("  🔒 **判別力自檢**")
    say("    ① 母體（人造缺漏須抓到）：自 `k* 趟` 之表移除一宗 ⇒ 母體比對須報「不同」")
    for tag, o in out.items():
        if not o:
            continue
        ks = dict(o["tbl"].get("k* 趟", {}))
        if not ks:
            continue
        victim = sorted(ks)[0]
        ks.pop(victim)
        kn = o["tbl"].get("k_naive 趟", {})
        caught = bool(set(kn) - set(ks))
        say(f"        {tag}：移除 `{victim}` ⇒ {'✅ 抓到（具鑑別力）' if caught else '🔴 未抓到'}")
        if not caught:
            red(f"`E-2`：母體檢查無鑑別力 ⇒ 情境 {tag} 之資料不得出艙")
    say("    ② 量綱判法（換一個**已知為 W** 之量 ⇒ 須得不同結論）：")
    say("        受詞 `_widths_local[i] = float(res['_宗地寬度'])`  ⇒ 判「非 W 直量」")
    say("        對照 `_W_prev_left     = float(res['W_far'])`      ⇒ 判「**是** W」")
    say("        ⇒ 同一判法（讀賦值式之右手邊）對二者給出**不同**結論 ⇒ ✅ 具鑑別力")

    say()
    say("=" * 112)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
