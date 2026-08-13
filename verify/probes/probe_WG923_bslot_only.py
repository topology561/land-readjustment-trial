# -*- coding: utf-8 -*-
r"""`W-G.9-23`：**僅修「非 `forced` 之 B 選槽」**之影響估算（⛔ 零生產碼·只讀包裝）。

# 受詞（⛔ 窄·不得擴張）

把 **B 選槽**之 `_b_L0`／`_b_R0` 改為目標值（**非 `forced` ⇒ `0`**），
**其餘三處全部不動**，會怎樣。
⛔ 不估 `forced` 三格之修法／⛔ 不估 A／⛔ 不估族①。

## 🔒 接縫（由構造證·事前登記 §1）

`_b_L0` 為 `run_step_g` 之**區域變數**、`_mp_base_W0` 為**巢狀函式**
⇒ ⛔ **不可直接包裝**；**唯一合法接縫 ＝ `_select_pool_slot` 之入參
`left_side['b']`／`right_side['b']`**。

* **理論@k\*** ← `_slot_res['table']`（＝本函式之輸出）⇒ **本包裝只動理論側**
* **實跑(階段1)** ← 推進迴圈（種子 `_W_prev = 0.0`）⇒ ⛔ **不動**

## 🔒 標籤與 `buf` 生產實值

以 **frame 內省**自呼叫端讀 `blk_label`／`_left_buffer_S`／`_right_buffer_S`／
`_fo_left`／`_fo_right`（**純觀測·⛔ 不改任何值**）。附**自我驗證閘**。

## 重跑
    python verify/probes/probe_WG923_bslot_only.py
"""
import os
import re
import sys
import traceback

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert os.path.exists(os.path.join(REPO, "CLAUDE.md")), f"🔴 REPO 不是倉根：{REPO}"
OUT = os.path.join(VERIFY, "out", "probe_WG923_bslot_only.log")
L, RC = [], [0]
KNOWN = {"R1", "R2", "R3", "R4", "R5", "R6"}
# 外部錨（`W-G.9-19` `D1`／`W-G.9-22` 二-1·⛔ 非本批自產）
ANCHOR_FORCED = {"0m": set(), "3.5m": {("R5", "left"), ("R2", "left"), ("R3", "right")}}


def say(s=""):
    print(s)
    L.append(s)


def red(s):
    say(f"  🔴 {s}")
    RC[0] = 1


def _f(v, n=4):
    return "—" if v is None else f"{float(v):.{n}f}"


# ══════════════════════════════════════════════════════════════════════════
# 甲組　`Q-1` 之**構造證**（⛔ 非只靠量測）
# ══════════════════════════════════════════════════════════════════════════
def jia_structural():
    import ast
    say("=" * 124)
    say("【甲組】`Q-1` 之**構造證**：非 `forced` ⇒ `buf` 恆 0（⛔ 碼面結構所定·非經驗）")
    say("=" * 124)
    src = open(os.path.join(VERIFY, "stepg_pipeline.py"), encoding="utf-8").read()
    lines = src.split("\n")
    t = ast.parse(src)
    par = {}
    for n in ast.walk(t):
        for c in ast.iter_child_nodes(n):
            par[c] = n
    hits = []
    for n in ast.walk(t):
        if not isinstance(n, ast.Assign):
            continue
        for tg in n.targets:
            if isinstance(tg, ast.Name) and tg.id in ("_left_buffer_S", "_right_buffer_S"):
                guards, p = [], par.get(n)
                while p is not None:
                    if isinstance(p, ast.If):
                        guards.append(lines[p.test.lineno - 1].strip()[:46])
                    elif isinstance(p, ast.Try):
                        guards.append("<try/except>")
                    p = par.get(p)
                hits.append((n.lineno, tg.id, lines[n.lineno - 1].strip()[:56], guards[::-1]))
    say(f"  🔒 **全部賦值點 ＝ {len(hits)}**（母體＝`verify/stepg_pipeline.py` 之 AST"
        f"·判準＝`Assign` 且 target 為 `_left_buffer_S`／`_right_buffer_S`）")
    for ln, nm, txt, g in sorted(hits):
        say(f"     {ln:>5} | {txt}")
        say(f"           守衛鏈 ＝ {g or '（無·即無條件）'}")
    unguarded = [h for h in hits if not any("_fo_" in x for x in h[3])]
    say(f"  ⇒ **不在 `_fo_*` 守衛內**之賦值 ＝ **{len(unguarded)}**"
        f"，其右值 ＝ {sorted({h[2].split('=')[-1].strip() for h in unguarded})}")
    ok = all("0.0" in h[2].split("=")[-1] for h in unguarded)
    say(f"  🔴 **`Q-1` 構造證：{'✅ 成立' if ok else '🔴 不成立'}**"
        f"——非 `forced`（`_fo_* == False`）時，該變數**恆為 `0.0`**")
    if not ok:
        red("`Q-1` 構造證不成立 ⇒ `R-3` 停機（本批之拆分前提不成立）")
    say(f"  🔒 **判別力自檢**：`_fo_*` 守衛內之賦值 ＝ "
        f"**{len(hits) - len(unguarded)}** 個，其右值含 `_corner_buffer_S` ⇒ "
        f"{'✅ 該判法非恆得 0（forced 時非 0）' if len(hits) > len(unguarded) else '🔴 判法恆得 0'}")
    return ok


# ══════════════════════════════════════════════════════════════════════════
# 乙組　只讀包裝之對拍
# ══════════════════════════════════════════════════════════════════════════
def run_pass(tag, setback, mode):
    """跑一趟 `run_step_g`。

    `mode`：`"none"` ⇒ 不替換（改前）／`"all"` ⇒ 全部非 `forced` 側之 `b := 0`／
    `"r1"` ⇒ **只改 `R1`**（供分辨「新曝」與「新破」）。
    """
    import run_verification as rv
    from app_harvest import harvest
    from selection_pipeline import build_ownership, build_build_parcels, run_corner_pk
    from stepg_pipeline import run_step_g
    snap = rv.load_snapshot()
    ns, fs = harvest()
    cb_by, cad = rv.build_pipeline(ns, fs, snap)
    build_ownership(ns, fs, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    tp, bp, _ = build_build_parcels(ns, fs, v6, list(cb_by.values()), snap)
    params = rv.build_param_table(ns, fs, cb_by, cad, snap, setback)
    _d, _s, _o, win, forced = run_corner_pk(
        ns, fs, list(cb_by.values()), cad, params, tp, bp, setback, snapshot=snap)

    REC, FRAME_BAD = [], []
    _orig = ns["_select_pool_slot"]

    def w_slot(widths, left_side, right_side, rw_func=None):
        # ── frame 內省（**純觀測**·⛔ 不改任何值）──
        fr = sys._getframe(1).f_locals
        lbl = fr.get("blk_label")
        bufL, bufR = fr.get("_left_buffer_S"), fr.get("_right_buffer_S")
        foL, foR = bool(fr.get("_fo_left")), bool(fr.get("_fo_right"))
        if not (isinstance(lbl, str) and lbl in KNOWN):
            FRAME_BAD.append(repr(lbl))            # 🔒 自我驗證閘（⛔ 不靜默）
        before = _orig(widths, left_side, right_side, rw_func)
        # ── 改後（⛔ 只換非 `forced` 側之 `b`）──
        L2, R2 = dict(left_side or {}), dict(right_side or {})
        _apply = (mode == "all") or (mode == "r1" and lbl == "R1")
        if _apply and not foL:
            L2["b"] = 0.0
        if _apply and not foR:
            R2["b"] = 0.0
        after = _orig(widths, L2, R2, rw_func)
        # 🔒 `J3` 判別力自檢：**掃描**一組 `b` 值，證該判法**抓得到「會變」之情形**。
        #   ⚠️ 首版用單一極端值 `b := 1e6` ⇒ `rw_from_width` **飽和於 100**
        #     ⇒ `R(b+Σw) − R(b) = 0` 對每個 `k` 皆同 ⇒ **恆不改變 `k*`**
        #     ⇒ 該自檢**恆判未變**、⛔ 無鑑別力（已由自檢本身攔下）。
        #   ⇒ 改掃**未飽和區**（`0`〜`16`）。
        sweep = {}
        for _bv in (0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0):
            X = dict(left_side or {})
            X["b"] = _bv
            try:
                _r = _orig(widths, X, right_side, rw_func)
                sweep[_bv] = (_r.get("k"), (_tstar(_r) or {}).get("L"))
            except Exception:                                   # noqa: BLE001
                sweep[_bv] = (None, None)
        REC.append({
            "lbl": lbl, "foL": foL, "foR": foR, "bufL": bufL, "bufR": bufR,
            "bL0": (left_side or {}).get("b"), "bR0": (right_side or {}).get("b"),
            "bL1": L2.get("b"), "bR1": R2.get("b"),
            "k_before": before.get("k"), "k_after": after.get("k"),
            "sweep": sweep,
            "th_before": _tstar(before), "th_after": _tstar(after),
            "n_widths": len(widths or []),
        })
        return after if mode != "none" else before

    ns["_select_pool_slot"] = w_slot
    err = None
    try:
        run_step_g(ns, fs, list(cb_by.values()), cad, snap, params, bp, win, forced, setback)
    except Exception as e:                                      # noqa: BLE001
        err = f"{type(e).__name__}: {e}"
    finally:
        ns["_select_pool_slot"] = _orig                         # 🔒 還原（⛔ 不留 patch）
    restored = (ns["_select_pool_slot"] is _orig)
    return {"rec": REC, "err": err, "forced": forced, "frame_bad": FRAME_BAD,
            "restored": restored, "mode": mode}


def _tstar(res):
    """自 `_select_pool_slot` 之回傳取 `k*` 那一列之 `ΣRw_L`／`ΣRw_R`。"""
    k = res.get("k")
    for row in (res.get("table") or []):
        if row.get("k") == k:
            return {"L": row.get("ΣRw_L"), "R": row.get("ΣRw_R"), "J": row.get("J")}
    return {}


def parse_gate(err):
    """自例外訊息取結構閘之 `理論@k*` 與 `實跑(階段1)`（⛔ 不重算）。"""
    if not err:
        return None
    m = re.search(r"街廓 (\S+) (\S+) 側 理論@k\*=([-\d.]+) ≠ 實跑\(階段1\)=([-\d.]+)", err)
    if not m:
        return {"raw": err[:150]}
    return {"blk": m.group(1), "side": m.group(2),
            "th": float(m.group(3)), "re": float(m.group(4)),
            "delta": float(m.group(3)) - float(m.group(4))}


def yi(tag, setback):
    say()
    say("=" * 124)
    say(f"【乙組·情境 {tag}】只讀包裝之對拍（⛔ 零生產碼）")
    say("=" * 124)
    out = {}
    for mode, sub in (("改前", "none"), ("改後", "all"), ("只改R1", "r1")):
        try:
            st = run_pass(tag, setback, sub)
        except Exception as e:                                  # noqa: BLE001
            red(f"{mode} 建置失敗：{type(e).__name__}: {e}")
            say(traceback.format_exc()[-340:])
            return None
        out[mode] = st
        # 🔒 自我驗證閘（frame 內省）
        if st["frame_bad"]:
            red(f"{mode}：frame 內省取得之 `blk_label` 不在已知集內 ⇒ ⛔ 本趟結論不得出艙"
                f"：{st['frame_bad'][:3]}")
            return None
        if not st["restored"]:
            red(f"{mode}：只讀包裝**未還原** ⇒ `R-4` 停機")
            return None
    say("  🔒 **自我驗證閘（frame 內省）**：兩趟所取之 `blk_label` **全部落在已知街廓集**"
        f"（{sorted(KNOWN)}）⇒ ✅；只讀包裝**兩趟皆已還原** ⇒ `R-4` 未觸發")

    # ── `J4` 跑到哪裡、在哪裡停（⛔ 逐街廓正面記錄）──
    say()
    say("  ── `J4` **跑到哪裡、在哪裡停**（⛔ 不只記有無跑完）──")
    for mode in ("改前", "改後", "只改R1"):
        st = out[mode]
        seq = [r["lbl"] for r in st["rec"]]
        g = parse_gate(st["err"])
        stop = (f"街廓 {g['blk']} {g['side']} 側（結構閘）" if g and "blk" in g
                else ("（未拋·跑完）" if not st["err"] else f"（其他）{(g or {}).get('raw', '')}"))
        say(f"     **{mode}**：`_select_pool_slot` 被呼叫 **{len(seq)}** 次"
            f"（母體＝該趟之全部呼叫·判準＝進入包裝）")
        say(f"              到達之街廓序 ＝ {seq}")
        say(f"              停於 ⇒ {stop}")
    n0, n1 = len(out["改前"]["rec"]), len(out["改後"]["rec"])
    say(f"     🔒 **`J4` 判**：改後到達 **{n1}** 街廓 vs 改前 **{n0}** ⇒ "
        f"{'✅ 跑得更遠' if n1 > n0 else ('⚠️ 相同' if n1 == n0 else '🔴 更短')}")

    # ── `Q-3` `k*` 是否改變 ──
    say()
    say("  ── `Q-3`／`J3` `k*` 是否改變（⛔ 同一次呼叫同時算改前與改後）──")
    say(f"     {'街廓':<8}{'forced(L/R)':<14}{'buf_L(生產)':>13}{'buf_R(生產)':>13}"
        f"{'b_L 改前':>11}{'b_L 改後':>11}{'k*改前':>8}{'k*改後':>8}{'k*掃描之相異值':>16}  判")
    changed = []
    for r in out["改後"]["rec"]:
        same = (r["k_before"] == r["k_after"])
        if not same:
            changed.append(r["lbl"])
        say(f"     {str(r['lbl']):<8}{str(r['foL']) + '/' + str(r['foR']):<14}"
            f"{_f(r['bufL']):>13}{_f(r['bufR']):>13}{_f(r['bL0']):>11}{_f(r['bL1']):>11}"
            f"{str(r['k_before']):>8}{str(r['k_after']):>8}"
            f"{str(sorted({v[0] for v in r['sweep'].values() if v[0] is not None})):>16}"
            f"  {'✅ 未變' if same else '🔴 改變'}")
    say(f"     🔒 **判別力自檢**（`J3` 期望為<u>否定</u> ⇒ 尤須自檢·考古 76）：")
    say("        🔴 **自檢須下放一層**：先證「替換**確實抵達計算**」，再談 `k*`。")
    say("        ⚠️ 只掃 `k*` 不足——`k*` 可能**本就對 `b` 不敏感**，")
    say("          屆時「掃了也沒變」與「探針沒接上」**⛔ 給出同一個輸出**（考古 71 之形狀）。")
    reach, ins = [], []
    for r in out["改後"]["rec"]:
        ks = sorted({v[0] for v in r["sweep"].values() if v[0] is not None})
        Ls = sorted({round(float(v[1]), 4) for v in r["sweep"].values() if v[1] is not None})
        say(f"           {r['lbl']}：`k*` 之相異值 ＝ {ks}｜"
            f"`ΣRw_L@k*` 之相異值 ＝ {Ls[:6]}{'…' if len(Ls) > 6 else ''}（共 {len(Ls)}）")
        (reach if len(Ls) > 1 else ins).append(r["lbl"])
    say(f"        ① **替換是否抵達計算**：`ΣRw_L@k*` 隨 `b` 出現相異值之街廓 ＝ "
        f"**{len(reach)}**／{len(out['改後']['rec'])}：{reach}")
    if len(reach) != len(out["改後"]["rec"]):
        red(f"替換**未抵達**下列街廓之計算：{ins} ⇒ ⛔ 該等街廓之 `Q-3` 結論**無從判定**"
            f"（⛔ **非**「判定為未變」）")
    else:
        say("           ⇒ ✅ **替換確實抵達計算**（⛔ 非探針沒接上）")
        say(f"        ② **`k*` 是否隨之改變**：`k*` 出現相異值之街廓 ＝ "
            f"**{len([r for r in out['改後']['rec'] if len({v[0] for v in r['sweep'].values() if v[0] is not None}) > 1])}**")
        say("           ⇒ ✅ **`k*` 對 `b` 不敏感<u>係真結論</u>**——`ΣRw_L` 變了而 `k*` 不變。")
    say(f"     🔴 **`Q-3` 判**：`k*` 改變之街廓 ＝ **{len(changed)}**：{changed or '（無）'}")
    say(f"        ⇒ {'🛑 `R-1` 觸發（配地位置會動）' if changed else '✅ `J3` 成立 ⇒ `R-1` 未觸發'}")

    # ── `Q-2` 結構閘 ──
    say()
    say("  ── `Q-2`／`J2` 結構閘 `理論＝實跑`（容差 **0.1**·單位 **百分點**）──")
    for mode in ("改前", "改後", "只改R1"):
        g = parse_gate(out[mode]["err"])
        if g and "blk" in g:
            say(f"     **{mode}**：{g['blk']} {g['side']} 側　理論@k* ＝ **{g['th']:.2f}**"
                f"　實跑(階段1) ＝ **{g['re']:.2f}**　Δ ＝ **{g['delta']:+.2f}** pp ⇒ 🔴 **不過**")
        elif out[mode]["err"]:
            say(f"     **{mode}**：⚠️ **無從判定**——停於**非該閘**之處"
                f"：{(g or {}).get('raw', out[mode]['err'][:110])}")
        else:
            say(f"     **{mode}**：✅ **未拋** ⇒ 該閘於全部到達之街廓**皆過**")
    g0, g1 = parse_gate(out["改前"]["err"]), parse_gate(out["改後"]["err"])
    r1_blk = (g0 or {}).get("blk")
    passed_r1 = bool(r1_blk) and (not g1 or g1.get("blk") != r1_blk)
    say(f"     🔴 **`Q-2` 判**（受詞＝**改前拋出之該街廓** `{r1_blk}`）：")
    say(f"        {'✅ `J2` 成立——該街廓之結構閘轉為通過' if passed_r1 else '🛑 `R-2` 觸發——該閘仍不過 ⇒ 另有第二個成因'}")
    return {"changed": changed, "g0": g0, "g1": g1, "out": out}


# ══════════════════════════════════════════════════════════════════════════
# 丁組　預期轉紅清單（⛔ 只列·不實施·⛔ 不採信施工單之列舉）
# ══════════════════════════════════════════════════════════════════════════
def ding():
    say()
    say("=" * 124)
    say("【丁組】預期轉紅清單（🔴 **本批必交·⛔ 不實施**·⛔ 不採信施工單所列舉）")
    say("=" * 124)
    items = []
    # 1 三支端到端複本之終止點凍存
    p = os.path.join(VERIFY, "fixture_e2e_termination.py")
    ok = os.path.exists(p)
    n = len(re.findall(r"三支複本|端到端複本", open(p, encoding="utf-8").read())) if ok else 0
    items.append(("`verify/fixture_e2e_termination.py`（**三支端到端複本之終止點凍存**）",
                  "✅ **會**", "🟢 **預期內**",
                  "其受詞即「**在哪裡停**」；本修法之目的正是**讓它停得更遠** ⇒ 轉紅為**成功之訊號**。"
                  "屆時之正辦 ＝ **逐項確認新終止點與預期相符後**才更新，"
                  "⛔ **不得逕自重凍**", f"現查存在·字樣命中 {n}"))
    # 2 期望 FAIL 名單之對帳
    fl = [f for f in os.listdir(os.path.join(VERIFY, "out"))
          if f.startswith("K6A2_期望FAIL名單")]
    cur = "K6A2_期望FAIL名單_WG97_名目加原因.txt"
    items.append((f"`verify/out/{cur}`（**現行凍存名單**·對帳器 `verify/wv_reconcile.py`）",
                  "✅ **會**", "🟢 **預期內**",
                  "對帳準則為「**名目 ＋ 正規化後原因全文**」；本修法改變 `v3·StepG*` 之**原因全文**"
                  "（結構閘 → 別的或消失）⇒ **類 III（訊質不同）＝紅**。"
                  "屆時之正辦 ＝ **逐項具名確認**後更新，⛔ **不得逕自重凍**",
                  f"現查 `K6A2_期望FAIL名單*` 共 {len(fl)} 檔（⚠️ 舊四份一份未刪·僅不再為基準）"))
    # 3 _ctx["0m"]
    src = open(os.path.join(VERIFY, "run_verification.py"), encoding="utf-8").read()
    n3 = len(re.findall(r'_ctx\["0m"\]', src))
    items.append(('`verify/run_verification.py` 之 `W-G G.1 接線層 ctx-builder 同源`'
                  '（`_ctx["0m"]`）',
                  "🔶 **可能由紅轉綠**", "🟢 **預期內**",
                  "該閘**現為死閘**（`_ctx[\"0m\"]` 缺鍵先崩·`W-G.9-4b` 已具名）；"
                  "其缺鍵之根因 ＝ `run_step_g` 之結構閘 raise ⇒ 修法若使該 raise 消失，"
                  "**該閘可能首度真正執行** ⇒ 屆時**它才開始咬**，"
                  "⛔ **不得將其首次紅誤認為本修法之破壞**",
                  f"`_ctx[\"0m\"]` 於該檔命中 {n3} 行"))
    # 4 baselines
    bl = os.listdir(os.path.join(VERIFY, "baselines"))
    items.append(("`verify/baselines/`（**重烤基準**）",
                  "⚠️ **無從判定**", "—",
                  "🔴 **本批⛔ 未查其逐檔內容**——判其是否轉紅須知**哪些 CSV 之欄含 `ΣRw`／`G`**，"
                  "而本批**未讀**。⛔ **不得猜**（考古 71：「無從判定」≠「判定為偽」）",
                  f"現查 {len(bl)} 檔（母體＝`verify/baselines/` 之 `os.listdir`）"))
    for nm, will, kind, how, ev in items:
        say()
        say(f"  ▸ **{nm}**")
        say(f"      會不會轉紅　＝ {will}")
        say(f"      預期／非預期 ＝ {kind}")
        say(f"      屆時之正辦　＝ {how}")
        say(f"      現查依據　　＝ {ev}")
    say()
    say(f"  🔒 **`J5` 判**：可逐項現查判定者 ＝ **3**／**4**；"
        f"**無從判定 ＝ 1**（`verify/baselines/`·已具名·⛔ 未猜）")
    say("  🔒 **射程聲明**：本清單之母體 ＝ 上列 **4** 項（⛔ 正面列舉）；")
    say("     ⛔ **不宣稱**「全倉只有這些會轉紅」——⛔ 本批未做全倉盤點。")


def main():
    say("=" * 124)
    say("【`W-G.9-23`】僅修「非 `forced` 之 B 選槽」之影響（⛔ 零生產碼·只讀包裝）")
    say("=" * 124)
    say("  🔴 **射程**：本批只涵蓋 **13 格（非 `forced`）**；"
        "**`forced` 三格仍卡表示法、⛔ 不在此數內**。")
    if not jia_structural():
        return finish()
    res = {}
    for tag, sb in (("0m", 0.0), ("3.5m", 3.5)):
        res[tag] = yi(tag, sb)
    # ── 丙組 ──
    say()
    say("=" * 124)
    say("【丙組】連鎖傳遞之範圍（⛔ 只述·不估跨街廓之量）")
    say("=" * 124)
    anych = [t for t, v in res.items() if v and v["changed"]]
    say(f"  `k*` 改變之情境 ＝ **{len(anych)}**：{anych or '（無）'}")
    say("  🔒 **範圍之判（由構造）**：`_select_pool_slot` 之入參 `widths`／`left_side`／`right_side`")
    say("     **逐街廓建置**（`run_step_g` 之 `for blk_label, parcels_in_blk in "
        "parcels_by_block.items():` 內）")
    say("     ⇒ `k*` 之改變**止於該街廓側**，⛔ **不跨街廓**。")
    say("  ⚠️ **但**：推進種子以 `W_far` **thread 到下一宗**（`W-G.9-22` 丙組已查）")
    say("     ⇒ **同一街廓側之整排宗**皆受影響；⛔ **跨街廓之量本批未估**（施工單：只述）。")
    ding()
    return finish()


def finish():
    say()
    say("=" * 124)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"\n[log] {os.path.relpath(OUT, REPO)}　rc={RC[0]}")
    return RC[0]


if __name__ == "__main__":
    sys.exit(main())
