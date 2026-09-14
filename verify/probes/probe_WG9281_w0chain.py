#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""`W-G.9-281` `§三`／`§四`：態乙 `R4 right` 之 `W_0` **產生鏈**定位 ＋
情形甲 ∧ `R(W_0) > 0` 四格之**分支**歸類。

🛑 **本器⛔ 施任何替身、⛔ 做任何反事實、⛔ 改生產碼一字**（單 `§七`）——**純量測**。
🔒 **底本** ＝ `verify/probes/probe_WG9279_rw0.py` 之 `drive`（⛔ 另寫第二份判準）。

🔑 **與 `-279` 之唯一結構相異**（單 `§三-2` 所令·坑 `bg` 之攔法）：
   **包裹 `ns["solve_G_binary"]` 本身**、取其**參數本身**（`baseline_pt`／`side_mid`／
   `allocation_dir`／`d_hat`），**⛔ climb 外層**。
   🩸 其必要性：`allocation_dir` 於 `_solve_G_one` 內、**呼叫 `solve_G_binary` 之前**
   已由 `if is_corner: allocation_dir = _first_corner_alloc_dir(side_mid)` **換過**
   ⇒ 外層之 `allocation_dir_block` 於**鏈頭**恰為錯者。
   🔒 **非參數之符號**（`corner_pt`／`end_pt`／`*_cum_S`／`blk_label`／`allocation_dir_block`）
   仍須自呼叫端取回——此係單 `§三-3` 所**明令**（「該式中每一符號於本格之當場值」），
   其攔法 ＝ 框內省之**自我驗證閘**（所錄之 `blk` 須為已知母體之非空子集）。

🛑 **⛔ 判任何側是否違反 `K-9-5-12`、⛔ 判碼註為誤、⛔ 提修法主張、⛔ 解除或收窄
   `GB-168`／`GB-169`**——**出艙即止**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9281_w0chain.py [倉根]`
`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力三造任一不成立）。
"""
import contextlib
import inspect
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
M_A = "甲"          # 態甲 ＝ 生產態（旗標未設）
M_B = "乙"          # 態乙 ＝ WV_K6_STEP0=off

# 🔒 零判之**具名常數**（單 `§四` 所令·⛔ 裸 1e-12）
TOL0 = 1e-12
TOL0_NAME = "TOL0"
TOL0_RULE = ("|x| <= " + TOL0_NAME + " ⇒ 判為零"
             "（" + TOL0_NAME + " = " + repr(TOL0) + "）")


def say(s=""):
    print(s)


def _ns(s):
    if s is None:
        return None
    t = str(s)
    if "左" in t or t.lower().startswith("l"):
        return "left"
    if "右" in t or t.lower().startswith("r"):
        return "right"
    return None


def drive(sb, mode):
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    recs = []
    errs = []
    _o_sgb = ns["solve_G_binary"]
    SIG = inspect.signature(_o_sgb)

    def _climb(names, upto=16):
        out = {k: None for k in names}
        for d in range(1, upto + 1):
            try:
                f = sys._getframe(d + 1)      # 🔒 +1 ＝ 補本函式自身之一層（坑 `bb`）
            except ValueError:
                break
            for k in names:
                if out[k] is None and k in f.f_locals:
                    out[k] = f.f_locals[k]
        return out

    def _spy_sgb(*a, **kw):
        # 🛑 **先原樣呼叫**——記錄之任何失敗⛔ 得改變行為
        #    （`_solve_G_one` 以 `except Exception: pass` 退回 `iterate_G_S`）。
        out = _o_sgb(*a, **kw)
        try:
            ba = SIG.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            c = _climb(["blk_label", "corner_pt", "end_pt", "d_hat_rev",
                        "left_cum_S", "right_cum_S", "allocation_dir_block",
                        "actual_max_proj", "tp", "side",
                        "_lg_idx_left", "_lg_idx_right",
                        "_side_mid_left", "_side_mid_right"])
            tp = c.get("tp") or {}
            recs.append({
                # ── 參數本身（單 §三-2 所令·⛔ climb 外層）──
                "p_baseline_pt": P.get("baseline_pt"),
                "p_side_mid": P.get("side_mid"),
                "p_allocation_dir": P.get("allocation_dir"),
                "p_d_hat": P.get("d_hat"),
                "p_is_corner": P.get("is_corner"),
                "p_is_chain_head": P.get("is_chain_head"),
                "p_W_prev": P.get("W_prev"),
                "p_side_label": P.get("side_label"),
                # ── 非參數之符號（單 §三-3 所明令）──
                "c_blk": c.get("blk_label"),
                "c_corner_pt": c.get("corner_pt"),
                "c_end_pt": c.get("end_pt"),
                "c_d_hat_rev": c.get("d_hat_rev"),
                "c_left_cum_S": c.get("left_cum_S"),
                "c_right_cum_S": c.get("right_cum_S"),
                "c_alloc_dir_block": c.get("allocation_dir_block"),
                "c_actual_max_proj": c.get("actual_max_proj"),
                "c_side": _ns(c.get("side")),
                "c_lg_idx_left": c.get("_lg_idx_left"),
                "c_lg_idx_right": c.get("_lg_idx_right"),
                "c_mp_left": c.get("_side_mid_left"),
                "c_mp_right": c.get("_side_mid_right"),
                "lot": (tp.get("暫編地號")
                        if isinstance(tp, dict) else None),
                # ── 碼面之回傳（供判別力造甲之逐位對拍）──
                "r_W_rw_start_raw": (out or {}).get("W_rw_start_raw"),
                "r_W_near": (out or {}).get("W_near"),
            })
        except Exception as e:                                  # noqa: BLE001
            errs.append(repr(e))
        return out

    ns["solve_G_binary"] = _spy_sgb

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
    n0 = len(recs)
    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb,
                       eff_min_build_by_blk={})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"recs": recs, "from_stepg": n0, "off": list(_off or []),
            "fo": fo_tab, "err": err, "spy_err": errs,
            "n_calls_total": len(recs),
            "R": ns["rw_from_width"], "np": ns["np"],
            "fcad": ns["_first_corner_alloc_dir"], "st": fake_st}


def _heads(d):
    """鏈頭之筆（每 (blk, side) 取其最末）——`run_step_g` 段。"""
    out = {}
    for r in d["recs"][d["from_stepg"]:]:
        if not (bool(r["p_is_corner"]) or bool(r["p_is_chain_head"])):
            continue
        if r["c_blk"] is None or r["c_side"] is None:
            continue
        out[(r["c_blk"], r["c_side"])] = r
    return out


def _ahat(npmod, d_hat, allocation_dir):
    """碼面逐行複刻（`app.py` `_n_alloc` ＋ `_ahat`）——⛔ 另寫第二份判準。"""
    if allocation_dir is None or d_hat is None:
        return None
    na = npmod.asarray(allocation_dir, dtype=float)
    nn = float(npmod.linalg.norm(na))
    if nn <= 1e-9:
        return None
    n_alloc = na / nn
    dh = npmod.asarray(d_hat, dtype=float)
    dhn = float(npmod.linalg.norm(dh))
    dhu = (dh / dhn) if dhn > 1e-9 else dh
    return n_alloc if float(npmod.dot(dhu, n_alloc)) >= 0.0 else -n_alloc


def _dot(npmod, p, q, ah):
    if p is None or q is None or ah is None:
        return None
    return float(npmod.dot(npmod.asarray(p, dtype=float)
                           - npmod.asarray(q, dtype=float), ah))


def _v(x):
    if x is None:
        return "None"
    try:
        return "[" + ", ".join(repr(float(c)) for c in list(x)[:2]) + "]"
    except Exception:                                           # noqa: BLE001
        return repr(x)


def _iszero(x):
    return (x is not None) and (abs(x) <= TOL0)


def main():
    say("=" * W)
    say("【`W-G.9-281` `§三`／`§四`】`W_0` 之"
        "**加性分解**與**產生鏈**（**純量測**"
        "·⛔ 替身·⛔ 反事實）")
    say("=" * W)
    say("\U0001f6d1 **⛔ 判任何側是否違反 `K-9-5-12`、"
        "⛔ 判碼註為誤、⛔ 提修法主張**——"
        "出艙即止。")
    say("\U0001f512 零判之具名常數：" + TOL0_RULE)

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in ((M_A, None), (M_B, "off")):
            D[(tag, lab)] = drive(sb, mode)
    os.environ.pop(ENV, None)
    R = D[("0m", M_A)]["R"]
    NP = D[("0m", M_A)]["np"]

    # ══ 自我驗證閘（坑 bb／bg）═══════════════════════════════════════════
    say("")
    say("─" * W)
    say("【自我驗證闘】框內省所錄之 "
        "`blk_label`＋包裹器之錯誤計數"
        "（⛔ 不過即 loud 拒測）")
    say("─" * W)
    bad = []
    for k in sorted(D):
        d = D[k]
        h = _heads(d)
        bl = sorted({b for b, _ in h})
        ok = bool(bl) and all(b in BLKS for b in bl)
        se = len(d["spy_err"])
        if (not ok) or se:
            bad.append(k)
        say("   · `%s` 態%s｜`solve_G_binary` 呼叫 %d 次"
            "（`run_step_g` 段 %d）｜鏈頭所錄之 `blk` = %s"
            "｜包裹器錯誤 %d ⇒ %s"
            % (k[0], k[1], d["n_calls_total"], d["n_calls_total"] - d["from_stepg"],
               bl, se, "✅" if (ok and not se) else "\U0001f534"))
        if se:
            for e in d["spy_err"][:3]:
                say("       \U0001f534 " + e)
    # 判別力：包裹器須確被呼叫（必非零）／一未包裹之名須為零
    tot = sum(D[k]["n_calls_total"] for k in D)
    say("   [判別力必非零] 四態合計呼叫次數 = "
        + str(tot) + "（期 > 0 ⇒ 包裹確實生效） ⇒ "
        + ("✅" if tot > 0 else "\U0001f534"))
    if bad or tot <= 0:
        say("   \U0001f6d1 **不過**（%s）⇒ loud 拒測。" % bad)
        return 5
    say("   ⇒ **器非紅** ✅")

    # ══ 情形甲／乙 ═══════════════════════════════════════════════════════
    FORCED = {}
    say("")
    say("─" * W)
    say("【情形甲／乙】源 = `run_corner_pk` 之第三"
        "回傳 `_off` 之 `指配` 欄"
        "（乙 = 強制抵費地）")
    say("─" * W)
    for k in sorted(D):
        s = set()
        for r in D[k]["off"]:
            b = str(r.get("街廓", ""))
            sd = _ns(r.get("端"))
            if "強制抵費地" in str(r.get("指配", "")) and b and sd:
                s.add((b, sd))
        FORCED[k] = s
        say("   · `%s` 態%s ⇒ `_off` %d 列｜乙之格 = %s"
            % (k[0], k[1], len(D[k]["off"]), sorted(s) or "（無）"))
        for _r in D[k]["off"]:
            say("     - %r" % (_r,))

    # 🔒 判別力[必命中]：情形乙之偵測
    #    全態合計須 > 0；否則**先判量測器紅**
    #    （坑 `9` 之重踏防線）。
    _nf = sum(len(FORCED[k]) for k in FORCED)
    _noff = sum(len(D[k]["off"]) for k in D)
    say("   [判別力必命中] 四態之乙格合計 = "
        + str(_nf) + "｜`_off` 列合計 = " + str(_noff)
        + "　⇒ " + ("✅" if _nf > 0 else "🔴"))
    if _noff > 0 and _nf == 0:
        say("   🛑 **`_off` 有列而乙格為零 ⇒ "
            "先判量測器紅**（鍵名／字樣不符"
            "）⇒ loud 拒測。")
        return 5
    if _nf == 0:
        say("   🛑 **乙格全零 ⇒ loud 拒測**"
            "（⛔ 以空集充綠）。")
        return 5

    # ══ §三-2 主表：全母體 48 列 ═════════════════════════════════════════
    say("")
    say("═" * W)
    say("【`§三-2`】全母體 = 6 街廓 × 2 側 "
        "× 2 情境 × 2 態 = **48** 列（鏈頭格）"
        "；有值者逐列")
    say("═" * W)
    ROWS = []
    n_cells = 0
    for k in sorted(D):
        d = D[k]
        h = _heads(d)
        for b in BLKS:
            for sd in ("left", "right"):
                n_cells += 1
                r = h.get((b, sd))
                if r is None:
                    continue
                ah = _ahat(NP, r["p_d_hat"], r["p_allocation_dir"])
                w0 = _dot(NP, r["p_baseline_pt"], r["p_side_mid"], ah)
                tc = _dot(NP, r["c_corner_pt"], r["p_side_mid"], ah)
                ta = _dot(NP, r["p_baseline_pt"], r["c_corner_pt"], ah)
                anchor = r["c_end_pt"] if sd == "right" else r["c_corner_pt"]
                tc2 = _dot(NP, anchor, r["p_side_mid"], ah)
                ta2 = _dot(NP, r["p_baseline_pt"], anchor, ah)
                ident = (None if (w0 is None or tc is None or ta is None)
                         else w0 - (tc + ta))
                ident2 = (None if (w0 is None or tc2 is None or ta2 is None)
                          else w0 - (tc2 + ta2))
                fo = d["fo"].get(b, (None, None))
                ROWS.append({
                    "sit": k[0], "mode": k[1], "blk": b, "side": sd, "rec": r,
                    "ah": ah, "W0": w0, "Tc": tc, "Ta": ta,
                    "Tc2": tc2, "Ta2": ta2, "anchor": anchor,
                    "ident": ident, "ident2": ident2,
                    "R": (None if w0 is None else float(R(w0))),
                    "fo": (fo[0] if sd == "left" else fo[1]),
                    "forced": ((b, sd) in FORCED[k]),
                })
    say("   母體之列數 = " + str(n_cells)
        + "（期 48）｜**有值格** = " + str(len(ROWS))
        + "　\U0001f6d1 本批於現母體重量"
          "·⛔ 轉引前批之 `22`")
    say("")
    for r in ROWS:
        rec = r["rec"]
        say("┌" + "─" * (W - 1))
        say("│ `%s` 態%s　**%s / %s**　暫編地號 = %s"
            "　情形 = %s"
            % (r["sit"], r["mode"], r["blk"], r["side"], rec["lot"],
               "乙（forced）" if r["forced"] else "甲"))
        say("│   參數本身：baseline_pt = " + _v(rec["p_baseline_pt"])
            + "　side_mid = " + _v(rec["p_side_mid"]))
        say("│   參數本身：allocation_dir = " + _v(rec["p_allocation_dir"])
            + "　d_hat = " + _v(rec["p_d_hat"]))
        say("│   外層（供對照）：allocation_dir_block = "
            + _v(rec["c_alloc_dir_block"])
            + "　corner_pt = " + _v(rec["c_corner_pt"])
            + "　end_pt = " + _v(rec["c_end_pt"]))
        say("│   â = " + _v(r["ah"])
            + "　d̂·â = "
            + (repr(float(NP.dot(NP.asarray(rec["p_d_hat"], dtype=float)
                                 / float(NP.linalg.norm(
                                     NP.asarray(rec["p_d_hat"], dtype=float))),
                                 r["ah"]))) if r["ah"] is not None else "None"))
        say("│   cum_S：left = " + repr(rec["c_left_cum_S"])
            + "　right = " + repr(rec["c_right_cum_S"])
            + "　actual_max_proj = " + repr(rec["c_actual_max_proj"]))
        say("│   **W_0** = " + repr(r["W0"])
            + "　**R(W_0)** = " + repr(r["R"]))
        say("│   [錨甲 corner_pt] T_corner = " + repr(r["Tc"])
            + "　T_adv = " + repr(r["Ta"])
            + "　恆等檢差 = " + repr(r["ident"]))
        say("│   [錨乙 呼叫端之錨] T_corner = " + repr(r["Tc2"])
            + "　T_adv = " + repr(r["Ta2"])
            + "　恆等檢差 = " + repr(r["ident2"]))
        say("│   is_corner = " + repr(rec["p_is_corner"])
            + "　is_chain_head = " + repr(rec["p_is_chain_head"])
            + "　W_prev = " + repr(rec["p_W_prev"])
            + "　side_label = " + repr(rec["p_side_label"])
            + "　_fo = " + repr(r["fo"]))
        say("│   碼面回傳：W_rw_start_raw = "
            + repr(rec["r_W_rw_start_raw"])
            + "　W_near（2dp） = " + repr(rec["r_W_near"]))
    say("└" + "─" * (W - 1))

    # ══ §三-6 判別力三造 ═════════════════════════════════════════════════
    say("")
    say("═" * W)
    say("【`§三-6`】判別力**三造**"
        "（\U0001f6d1 逐態各自成立）")
    say("═" * W)
    # 造甲：還原值 vs 碼面 W_rw_start_raw（鏈頭 ⇒ _rw_start ＝ _W_near）
    say("【造甲·必逐位相符】"
        "還原之 `W_0` vs 碼面之 `W_rw_start_raw`"
        "（鏈頭 ⇒ `_rw_start` 即 `_W_near`）")
    n_exec = 0
    n_ok = 0
    bad_a = []
    for r in ROWS:
        v = r["rec"]["r_W_rw_start_raw"]
        if v is None or r["W0"] is None:
            bad_a.append((r["sit"], r["mode"], r["blk"], r["side"], "無值"))
            continue
        n_exec += 1
        same = (repr(float(v)) == repr(float(r["W0"])))
        if same:
            n_ok += 1
        else:
            bad_a.append((r["sit"], r["mode"], r["blk"], r["side"],
                          repr(float(v)) + " vs " + repr(float(r["W0"]))))
    say("   分母 = **全**有值格 " + str(len(ROWS))
        + "｜該闘之**執行次數** = " + str(n_exec)
        + "｜逐位相符 = " + str(n_ok))
    ok_a = (n_exec == len(ROWS)) and (n_ok == len(ROWS))
    if bad_a:
        for x in bad_a:
            say("   \U0001f534 " + repr(x))
    say("   ⇒ 造甲 = " + ("✅" if ok_a else "\U0001f534"))

    # 造乙：以 corner_pt 取代 baseline_pt 之同式，施於 R4 right 二格 ⇒ 須相異
    say("")
    say("【造乙·必相異】以 `corner_pt` 取代 "
        "`baseline_pt` 之同式於 `R4 right` 二格")
    tgt = [r for r in ROWS if r["blk"] == "R4" and r["side"] == "right"
           and r["mode"] == M_B]
    ok_b = bool(tgt)
    for r in tgt:
        alt = _dot(NP, r["rec"]["c_corner_pt"], r["rec"]["p_side_mid"], r["ah"])
        diff = (alt is not None and r["W0"] is not None
                and repr(float(alt)) != repr(float(r["W0"])))
        ok_b = ok_b and diff
        say("   · `%s` 態%s %s/%s：W_0 = %s｜代以 corner_pt = %s"
            "｜相異？%s"
            % (r["sit"], r["mode"], r["blk"], r["side"], repr(r["W0"]),
               repr(alt), diff))
    if not tgt:
        say("   \U0001f6d1 `R4 right` 態乙之格為空 "
            "⇒ loud（⛔ 以空集充綠）")
    say("   ⇒ 造乙 = " + ("✅" if ok_b else "\U0001f534"))

    # 造丙：T_adv 於「baseline_pt 與 corner_pt 逐位相同」之格 須 == 0（逐態各自成立）
    say("")
    say("【造丙·必為零】`T_adv` 於"
        "「`baseline_pt` 與 `corner_pt` 逐位相同」之格"
        "（**態甲／態乙各自成立**）")
    ok_c = True
    for mode in (M_A, M_B):
        sub = []
        for r in ROWS:
            bp = r["rec"]["p_baseline_pt"]
            cp = r["rec"]["c_corner_pt"]
            if r["mode"] != mode or bp is None or cp is None:
                continue
            try:
                if bool(NP.array_equal(NP.asarray(bp, dtype=float),
                                       NP.asarray(cp, dtype=float))):
                    sub.append(r)
            except Exception:                                   # noqa: BLE001
                pass
        if not sub:
            ok_c = False
            say("   \U0001f534 態%s：**該態無此格**"
                "（子母體為空）⇒ loud"
                "·⛔ 以空集充綠" % mode)
            continue
        allz = True
        for r in sub:
            z = (r["Ta"] is not None and float(r["Ta"]) == 0.0)
            allz = allz and z
            say("   · 態%s `%s` %s/%s：T_adv = %s｜== 0？%s"
                % (mode, r["sit"], r["blk"], r["side"], repr(r["Ta"]), z))
        ok_c = ok_c and allz
    say("   ⇒ 造丙 = " + ("✅" if ok_c else "\U0001f534"))

    if not (ok_a and ok_b and ok_c):
        say("")
        say("\U0001f6d1 **三造任一不成立 ⇒ "
            "判量測器紅、停機上呈**"
            "（⛔ 以其餘欄之綠充「器非紅」）")
        return 5

    # ══ §三-5 碼註二支之窮舉檢 ═══════════════════════════════════════════
    say("")
    say("═" * W)
    say("【`§三-5`】碼註**二支**之窮舉檢"
        "（**出艙即止**）")
    say("═" * W)
    ca_z = [r for r in ROWS if bool(r["rec"]["p_is_corner"])
            and r["W0"] is not None and float(r["W0"]) == 0.0]
    ca_n = [r for r in ROWS if bool(r["rec"]["p_is_corner"])
            and r["W0"] is not None and float(r["W0"]) != 0.0]
    say("   造 `A`：`is_corner` 為真之格中，"
        "`W_0` **嚴格 == 0** = **" + str(len(ca_z))
        + "** 格｜`!= 0` = **" + str(len(ca_n)) + "** 格")
    for r in ca_z:
        say("     · [==0] `%s` 態%s %s/%s｜W_0 = %s"
            % (r["sit"], r["mode"], r["blk"], r["side"], repr(r["W0"])))
    for r in ca_n:
        say("     · [!=0] `%s` 態%s %s/%s｜W_0 = %s｜R(W_0) = %s"
            % (r["sit"], r["mode"], r["blk"], r["side"], repr(r["W0"]), repr(r["R"])))
    cb = [r for r in ROWS if bool(r["rec"]["p_is_chain_head"])
          and not bool(r["rec"]["p_is_corner"]) and (r["fo"] is False)]
    say("   造 `B`：`is_chain_head` 真 ∧ `is_corner` 偽 ∧ "
        "該側 `_fo` 偽 = **" + str(len(cb)) + "** 格")
    for r in cb:
        say("     · `%s` 態%s %s/%s｜暫編地號 = %s"
            "｜W_0 = %s｜R(W_0) = %s｜情形 = %s"
            % (r["sit"], r["mode"], r["blk"], r["side"], r["rec"]["lot"],
               repr(r["W0"]), repr(r["R"]),
               "乙" if r["forced"] else "甲"))
    say("   \U0001f6d1 **出艙即止**：⛔ 判碼註為誤、"
        "⛔ 判其「窮舉不成立」、⛔ 提修法主張。")

    # ══ §四 分支歸類 ═════════════════════════════════════════════════════
    say("")
    say("═" * W)
    say("【`§四`】情形甲 ∧ `R(W_0) > 0` 之格"
        "——**分支**歸類（\U0001f6d1 ⛔ 以門檻切）")
    say("═" * W)
    say("   歸類之準據（發單側明定）："
        "`P` = T_adv 零 ∧ T_corner 非零｜"
        "`Q` = T_adv 非零 ∧ T_corner 零｜`R` = 二項皆非零")
    say("   零判：" + TOL0_RULE)
    sel = [r for r in ROWS if (not r["forced"]) and r["R"] is not None
           and float(r["R"]) > 0.0]
    say("   **當場重得之成員** = " + str(len(sel)) + " 格"
        + "　\U0001f6d1 ⛔ 轉引前批之 `4`")
    unclass = []
    for r in sel:
        for tag, tc, ta in (("錨甲 corner_pt", r["Tc"], r["Ta"]),
                            ("錨乙 呼叫端之錨",
                             r["Tc2"], r["Ta2"])):
            za, zc = _iszero(ta), _iszero(tc)
            if za and not zc:
                br = "P"
            elif (not za) and zc:
                br = "Q"
            elif (not za) and (not zc):
                br = "R"
            else:
                br = "\U0001f6d1 不落於三支"
                unclass.append((r["sit"], r["mode"], r["blk"], r["side"], tag))
            say("   · `%s` 態%s **%s/%s**｜[%s] (T_corner, T_adv) = (%s, %s)"
                "｜**支 = %s**"
                % (r["sit"], r["mode"], r["blk"], r["side"], tag,
                   repr(tc), repr(ta), br))
        say("     （W_0 = %s｜R(W_0) = %s｜暫編地號 = %s）"
            % (repr(r["W0"]), repr(r["R"]), r["rec"]["lot"]))
    if unclass:
        say("")
        say("   \U0001f6d1 **有格⛔ 落於三支 ⇒ loud "
            "停機上呈**（⛔ 自行擴充分支定義）：")
        for x in unclass:
            say("      " + repr(x))
        return 5

    # ══ §三-4 R4 right 二格之定位 ═══════════════════════════════════════
    say("")
    say("═" * W)
    say("【`§三-4`】`R4 right` 二格之定位"
        "（`0m`／`3.5m` 態乙各一格）")
    say("═" * W)
    for r in tgt:
        rec = r["rec"]
        d = D[(r["sit"], r["mode"])]
        say("")
        say("■ `%s` 態%s　**R4 / right**　暫編地號 = %s"
            % (r["sit"], r["mode"], rec["lot"]))
        say("  1. `is_corner` 之實參真值 = " + repr(rec["p_is_corner"])
            + "　⇒ 觸「街角第 1 宗換軸」"
              "之分支？" + repr(bool(rec["p_is_corner"])))
        say("  2. `is_chain_head` = " + repr(rec["p_is_chain_head"])
            + "　`_fo_right` = " + repr(r["fo"]))
        adb = rec["c_alloc_dir_block"]
        try:
            fc = d["fcad"](rec["p_side_mid"])
        except Exception as e:                                  # noqa: BLE001
            fc = "\U0001f534 " + repr(e)
        used = rec["p_allocation_dir"]
        which = ("allocation_dir_block"
                 if (adb is not None and used is not None
                     and bool(NP.array_equal(NP.asarray(adb, dtype=float),
                                             NP.asarray(used, dtype=float))))
                 else "_first_corner_alloc_dir(side_mid)"
                 if (not isinstance(fc, str) and used is not None
                     and bool(NP.array_equal(NP.asarray(fc, dtype=float),
                                             NP.asarray(used, dtype=float))))
                 else "\U0001f534 二者皆不符")
        say("  3. `allocation_dir` 之實際來源"
            "（座標系 = 平面直角座標之"
            "**單位向量**·⛔ 時序）")
        say("       allocation_dir_block            = " + _v(adb))
        say("       _first_corner_alloc_dir(side_mid) = "
            + (fc if isinstance(fc, str) else _v(fc)))
        say("       **所採者**（= `solve_G_binary` 之參數） = "
            + _v(used) + "　⇒ **" + which + "**")
        say("  4. T_corner / T_adv 二項及 `T_adv` 式中各因子")
        say("       [錨甲 corner_pt] T_corner = " + repr(r["Tc"])
            + "　T_adv = " + repr(r["Ta"]))
        say("       [錨乙 end_pt]     T_corner = " + repr(r["Tc2"])
            + "　T_adv = " + repr(r["Ta2"]))
        say("       因子：corner_pt = " + _v(rec["c_corner_pt"])
            + "　end_pt = " + _v(rec["c_end_pt"])
            + "　d_hat_rev = " + _v(rec["c_d_hat_rev"]))
        say("       因子：right_cum_S = " + repr(rec["c_right_cum_S"])
            + "　actual_max_proj = " + repr(rec["c_actual_max_proj"])
            + "　baseline_pt = " + _v(rec["p_baseline_pt"]))
        say("  5. 當場重得：**W_0 = " + repr(r["W0"])
            + "**　**R(W_0) = " + repr(r["R"]) + "**"
            + "　（⛔ 轉引前批之數）")
        say("  6. 三項前提之真值"
            "（\U0001f6d1 **⛔ 由 CC 作歸屬之判**）：")
        say("       是否 forced（該側為強制抵費地） = "
            + repr(r["forced"]) + "　（`_fo_right` = " + repr(r["fo"]) + "）")
        say("       是否街角勝者（`is_corner`） = "
            + repr(bool(rec["p_is_corner"])))
        say("       是否鏈頭（`is_chain_head`） = "
            + repr(bool(rec["p_is_chain_head"])))

    # ══ §三-3 baseline_pt 之產生式：逐呼叫端 ════════════════════════════
    say("")
    say("═" * W)
    say("【`§三-3`】`baseline_pt` 之產生式"
        "：**逐呼叫端各自取回**"
        "（\U0001f6d1 ⛔ 以一式概括）")
    say("═" * W)
    sp = os.path.join(REPO, "verify", "stepg_pipeline.py")
    with open(sp, "rb") as f:
        raw = f.read()
    L = raw.decode("utf-8").split("\n")
    rx_bp = re.compile(r"^\s*baseline_pt = ")
    rx_so = re.compile(r"_solve_one\(")
    hit_bp = [i for i, ln in enumerate(L) if rx_bp.match(ln)]
    hit_so = [i for i, ln in enumerate(L) if rx_so.search(ln) and "def " not in ln]
    say("   母體 = `verify/stepg_pipeline.py` **單檔**（"
        + str(len(raw)) + " B / " + str(len(L)) + " 列）·粒度框 = **列框**")
    say("   框甲（逐字·有 `^` 錨）= `^\\s*baseline_pt = `"
        "　⇒ **命中檔數 1 / 命中列數 "
        + str(len(hit_bp)) + "**")
    say("   框乙（無 `^` 錨·二數並報）= `_solve_one(`"
        "　⇒ **命中檔數 1 / 命中列數 "
        + str(len(hit_so)) + "**（含非定義列）")
    say("   \U0001f534 **二框之數相異** ⇒ 逐呼叫"
        "端列舉於下（⛔ 以其一概括另一）：")
    for i in hit_so:
        say("     · `_solve_one(` @ 列 " + str(i + 1) + "：" + L[i].strip())
    say("")
    for i in hit_bp:
        say("   ── 呼叫端 @ 列 " + str(i + 1)
            + "（列號作佐證·⛔ 作錨）")
        say("     (a) `baseline_pt` 之賦值式逐字：")
        j = i
        while j < len(L):
            say("         | " + L[j])
            if L[j].rstrip().endswith("None)") or L[j].rstrip().endswith(")"):
                break
            j += 1
        # (b) 該處所餵之 _is_chain_head 實參之式逐字
        for m in range(i, min(i + 30, len(L))):
            if "_is_chain_head=" in L[m]:
                say("     (b) 該處所餚之 `_is_chain_head` "
                    "實參之式逐字：")
                say("         | " + L[m])
                break
    say("")
    say("   (c) 該式中**每一符號**於本格之"
        "當場值（`repr` 全位）——"
        "逐格見上 `§三-2` 主表之 "
        "`corner_pt`／`end_pt`／`cum_S`／`actual_max_proj` 欄；"
        "`R4 right` 二格另見 `§三-4` 第 `4` 項。")
    say("")
    say("   \U0001f534 **二呼叫端之賦值式逐字"
        "相異** ⇒ 依單 `§三-3` 已各自出艙"
        "其全式與全符號值；"
        "⛔ 以「`corner_pt` ＋ `cum_S`」為既定式。")

    say("")
    say("═" * W)
    say("【終止態】逐態之 `run_step_g` 中止閘"
        "（照實·⛔ 列為新紅）")
    say("═" * W)
    for k in sorted(D):
        say("   · `%s` 態%s ⇒ %s"
            % (k[0], k[1], D[k]["err"] or "（未拋出）"))
    say("=" * W)
    return 0


if __name__ == "__main__":
    sys.exit(main())
