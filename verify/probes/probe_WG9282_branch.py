#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""`W-G.9-282` `§三`／`§四`：分支判準之**重立**（`b1`／`b2` ⇒ `A1`／`A2`／`B1`／`B2`）
＋ `forced` 側起算點之倉態對拍（執行期之款 `2`／`3`／`4`）。

🛑 **本器⛔ 施任何替身、⛔ 做任何反事實、⛔ 改生產碼一字**（單 `§七`）——**純量測**。
🔒 **底本** ＝ `verify/probes/probe_WG9281_w0chain.py` 之 `drive`（⛔ 另寫第二份判準）。
🔒 CJK 一律**逐字字面**（坑 `9` 之攔法）——⛔ 以反斜線 u 轉義寫鍵名。

🛑 **⛔ 判任何側是否違反 `K-9-5-12`／`K-9-5-13`、⛔ 判碼註為誤、⛔ 判「替身線」之所指、
   ⛔ 提修法主張、⛔ 解除或收窄 `GB-168`／`GB-169`**——**出艙即止**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9282_branch.py [倉根]`
`rc`：`0`／`5` **器紅**（自我驗證閘不過／判別力造丙不成立）。
"""
import contextlib
import inspect
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
M_A = "甲"
M_B = "乙"


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
    bufs = []
    _o_sgb = ns["solve_G_binary"]
    _o_cbs = ns["_corner_buffer_S"]
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
        out = _o_sgb(*a, **kw)          # 🛑 先原樣呼叫·⛔ 改回傳一位元
        try:
            ba = SIG.bind(*a, **kw)
            ba.apply_defaults()
            P = dict(ba.arguments)
            c = _climb(["blk_label", "corner_pt", "end_pt", "d_hat_rev",
                        "left_cum_S", "right_cum_S", "allocation_dir_block",
                        "actual_max_proj", "tp", "side"])
            tp = c.get("tp") or {}
            recs.append({
                "p_baseline_pt": P.get("baseline_pt"),
                "p_side_mid": P.get("side_mid"),
                "p_allocation_dir": P.get("allocation_dir"),
                "p_d_hat": P.get("d_hat"),
                "p_is_corner": P.get("is_corner"),
                "p_is_chain_head": P.get("is_chain_head"),
                "p_W_prev": P.get("W_prev"),
                "c_blk": c.get("blk_label"),
                "c_corner_pt": c.get("corner_pt"),
                "c_end_pt": c.get("end_pt"),
                "c_d_hat_rev": c.get("d_hat_rev"),
                "c_left_cum_S": c.get("left_cum_S"),
                "c_right_cum_S": c.get("right_cum_S"),
                "c_alloc_dir_block": c.get("allocation_dir_block"),
                "c_actual_max_proj": c.get("actual_max_proj"),
                "c_side": _ns(c.get("side")),
                "lot": (tp.get("暫編地號") if isinstance(tp, dict) else None),
                "r_W_rw_start_raw": (out or {}).get("W_rw_start_raw"),
            })
        except Exception as e:                                  # noqa: BLE001
            errs.append(repr(e))
        return out

    def _spy_cbs(block_poly, d_hat, front_p1, allocation_dir, range_area, side, **kw):
        o = _o_cbs(block_poly, d_hat, front_p1, allocation_dir, range_area, side, **kw)
        try:
            c = _climb(["blk_label"])
            bufs.append({"blk": c.get("blk_label"), "side": _ns(side),
                         "buf": float(o), "range_area": float(range_area),
                         "front_p1": front_p1, "d_hat": d_hat,
                         "allocation_dir": allocation_dir})
        except Exception as e:                                  # noqa: BLE001
            errs.append(repr(e))
        return o

    ns["solve_G_binary"] = _spy_sgb
    ns["_corner_buffer_S"] = _spy_cbs

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
    sl = (fake_st.session_state.get("f3_cad_side_lines_by_side", {}) or {})
    return {"recs": recs, "from_stepg": n0, "off": list(_off or []),
            "fo": fo_tab, "err": err, "spy_err": errs, "bufs": bufs,
            "sidelines": sl, "R": ns["rw_from_width"], "np": ns["np"]}


def _heads(d):
    out = {}
    for r in d["recs"][d["from_stepg"]:]:
        if not (bool(r["p_is_corner"]) or bool(r["p_is_chain_head"])):
            continue
        if r["c_blk"] is None or r["c_side"] is None:
            continue
        out[(r["c_blk"], r["c_side"])] = r
    return out


def _ahat(npm, d_hat, allocation_dir):
    if allocation_dir is None or d_hat is None:
        return None
    na = npm.asarray(allocation_dir, dtype=float)
    nn = float(npm.linalg.norm(na))
    if nn <= 1e-9:
        return None
    n_alloc = na / nn
    dh = npm.asarray(d_hat, dtype=float)
    dhn = float(npm.linalg.norm(dh))
    dhu = (dh / dhn) if dhn > 1e-9 else dh
    return n_alloc if float(npm.dot(dhu, n_alloc)) >= 0.0 else -n_alloc


def _xy(p):
    if p is None:
        return None
    try:
        return (float(list(p)[0]), float(list(p)[1]))
    except Exception:                                           # noqa: BLE001
        return None


def _v(p):
    t = _xy(p)
    return "None" if t is None else "[" + repr(t[0]) + ", " + repr(t[1]) + "]"


def main():
    say("=" * W)
    say("【`W-G.9-282` `§三`／`§四`】分支判準之**重立**（`b1`／`b2`）"
        "＋ `forced` 起算點之倉態對拍（執行期款）")
    say("=" * W)
    say("🛑 **出艙即止**：⛔ 判違反、⛔ 判碼註為誤、⛔ 判「替身線」之所指、⛔ 提修法主張。")
    say("🔒 `b1`／`b2` 皆 `float ==` 之**逐位**相等——**⛔ 容差、⛔ 門檻**。")

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in ((M_A, None), (M_B, "off")):
            D[(tag, lab)] = drive(sb, mode)
    os.environ.pop(ENV, None)
    R = D[("0m", M_A)]["R"]
    NP = D[("0m", M_A)]["np"]

    # ── 自我驗證閘 ────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【自我驗證閘】框內省所錄之 `blk_label` ＋ 包裹器之錯誤計數（⛔ 不過即 loud 拒測）")
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
        say("   · `%s` 態%s｜`solve_G_binary` 呼叫 %d 次｜`_corner_buffer_S` 呼叫 %d 次"
            "｜鏈頭所錄之 `blk` = %s｜包裹器錯誤 %d ⇒ %s"
            % (k[0], k[1], len(d["recs"]), len(d["bufs"]), bl, se,
               "✅" if (ok and not se) else "🔴"))
        for e in d["spy_err"][:3]:
            say("       🔴 " + e)
    tot = sum(len(D[k]["recs"]) for k in D)
    say("   [判別力必非零] 四態合計 `solve_G_binary` 呼叫 = " + str(tot)
        + "（期 > 0） ⇒ " + ("✅" if tot > 0 else "🔴"))
    if bad or tot <= 0:
        say("   🛑 **不過**（%s）⇒ loud 拒測。" % bad)
        return 5
    say("   ⇒ **器非紅** ✅")

    # ── 情形甲／乙 ────────────────────────────────────────────────────
    FORCED = {}
    say("")
    say("─" * W)
    say("【情形甲／乙】源 = `run_corner_pk` 之第三回傳 `_off` 之 `指配` 欄（乙 = 強制抵費地）")
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
    _nf = sum(len(FORCED[k]) for k in FORCED)
    _noff = sum(len(D[k]["off"]) for k in D)
    say("   [判別力必命中] 四態之乙格合計 = " + str(_nf) + "｜`_off` 列合計 = " + str(_noff)
        + " ⇒ " + ("✅" if _nf > 0 else "🔴"))
    if _noff > 0 and _nf == 0:
        say("   🛑 **`_off` 有列而乙格為零 ⇒ 先判量測器紅**（鍵名／字樣不符）⇒ loud 拒測。")
        return 5

    # ── §三　新判準 ──────────────────────────────────────────────────
    say("")
    say("=" * W)
    say("【`§三-2`／`§三-3`】新判準之逐格歸類（母體 = 同一有值鏈頭格·**本批於現母體重量**）")
    say("=" * W)
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
                anchor_name = "corner_pt" if sd == "left" else "end_pt"
                anchor = r["c_corner_pt"] if sd == "left" else r["c_end_pt"]
                cum_name = "left_cum_S" if sd == "left" else "right_cum_S"
                cum = r["c_left_cum_S"] if sd == "left" else r["c_right_cum_S"]
                sl = ((d["sidelines"].get(b) or {}).get(sd) or {})
                p1 = _xy(sl.get("p1"))
                p2 = _xy(sl.get("p2"))
                a_xy = _xy(anchor)
                if p1 is None or p2 is None or a_xy is None:
                    b1 = None
                    e1 = e2 = None
                else:
                    e1 = (a_xy == p1)
                    e2 = (a_xy == p2)
                    b1 = bool(e1 or e2)
                b2 = None if cum is None else (float(cum) == 0.0)
                W0 = (None if (ah is None or r["p_baseline_pt"] is None
                               or r["p_side_mid"] is None)
                      else float(NP.dot(
                          NP.asarray(r["p_baseline_pt"], dtype=float)
                          - NP.asarray(r["p_side_mid"], dtype=float), ah)))
                if b1 is None or b2 is None:
                    br = "🛑 不可得"
                else:
                    br = ("A1" if (b1 and b2) else "A2" if (b1 and not b2)
                          else "B1" if ((not b1) and b2) else "B2")
                dot_p = (None if (ah is None or p1 is None or p2 is None)
                         else float(ah[0] * (p2[0] - p1[0]) + ah[1] * (p2[1] - p1[1])))
                dot_a = (None if (ah is None or p1 is None or a_xy is None)
                         else float(ah[0] * (a_xy[0] - p1[0]) + ah[1] * (a_xy[1] - p1[1])))
                crs = (None if (p1 is None or p2 is None or a_xy is None)
                       else float((a_xy[0] - p1[0]) * (p2[1] - p1[1])
                                  - (a_xy[1] - p1[1]) * (p2[0] - p1[0])))
                fo = d["fo"].get(b, (None, None))
                ROWS.append({
                    "sit": k[0], "mode": k[1], "blk": b, "side": sd, "rec": r,
                    "ah": ah, "W0": W0, "R": (None if W0 is None else float(R(W0))),
                    "anchor_name": anchor_name, "anchor": a_xy, "p1": p1, "p2": p2,
                    "e1": e1, "e2": e2, "b1": b1, "cum_name": cum_name,
                    "cum": cum, "b2": b2, "br": br,
                    "dot_p": dot_p, "dot_a": dot_a, "crs": crs,
                    "fo": (fo[0] if sd == "left" else fo[1]),
                    "forced": ((b, sd) in FORCED[k]),
                })
    say("   母體之列數 = " + str(n_cells) + "（期 48）｜**有值格 = " + str(len(ROWS))
        + "**　🛑 本批於現母體重量·⛔ 轉引前批之 `22`")
    say("")
    for r in ROWS:
        say("┌" + "─" * (W - 1))
        say("│ `%s` 態%s　**%s / %s**　暫編地號 = %s　情形 = %s　**支 = %s**"
            % (r["sit"], r["mode"], r["blk"], r["side"], r["rec"]["lot"],
               "乙（forced）" if r["forced"] else "甲", r["br"]))
        say("│   錨之符號名 = " + r["anchor_name"] + "　錨 = " + _v(r["anchor"]))
        say("│   p1 = " + _v(r["p1"]) + "　p2 = " + _v(r["p2"]))
        say("│   錨 == p1 ? " + repr(r["e1"]) + "　錨 == p2 ? " + repr(r["e2"])
            + "　**b1 = " + repr(r["b1"]) + "**")
        say("│   " + r["cum_name"] + " = " + repr(r["cum"])
            + "　**b2 = " + repr(r["b2"]) + "**")
        say("│   W_0 = " + repr(r["W0"]) + "　R(W_0) = " + repr(r["R"])
            + "　is_corner = " + repr(r["rec"]["p_is_corner"])
            + "　_fo = " + repr(r["fo"]))
        say("│   â·(p2 − p1) = " + repr(r["dot_p"])
            + "　â·(錨 − p1) = " + repr(r["dot_a"])
            + "　(錨 − p1) × (p2 − p1) = " + repr(r["crs"])
            + "　🛑 末三欄**出艙即止**")
    say("└" + "─" * (W - 1))

    # 支之分布
    say("")
    say("【支之分布（全母體）】")
    dist = {}
    for r in ROWS:
        dist[r["br"]] = dist.get(r["br"], 0) + 1
    for kk in sorted(dist):
        say("   · " + kk + " = " + str(dist[kk]) + " 格")
    nd = [r for r in ROWS if r["b1"] is None or r["b2"] is None]
    if nd:
        say("   🛑 **不可得之格 = " + str(len(nd)) + "**（⛔ 以偽代之）：")
        for r in nd:
            say("      · `%s` 態%s %s/%s｜錨 = %s｜p1 = %s｜p2 = %s"
                % (r["sit"], r["mode"], r["blk"], r["side"],
                   _v(r["anchor"]), _v(r["p1"]), _v(r["p2"])))

    # ── §三-4　判別力三造 ────────────────────────────────────────────
    say("")
    say("=" * W)
    say("【`§三-4`】判別力三造")
    say("=" * W)
    t1 = [r for r in ROWS if r["b1"] is True]
    f1 = [r for r in ROWS if r["b1"] is False]
    say("【造甲·必命中】`b1` 為**真**之格數 = **" + str(len(t1)) + "**（期 ≥ 1）")
    if not t1:
        say("   🛑 **為 `0` ⇒ loud 明載**（⛔ 停機·⛔ 以空集充任何結論）；逐格三座標：")
        for r in ROWS:
            say("      · `%s` 態%s %s/%s｜錨(%s) = %s｜p1 = %s｜p2 = %s"
                % (r["sit"], r["mode"], r["blk"], r["side"], r["anchor_name"],
                   _v(r["anchor"]), _v(r["p1"]), _v(r["p2"])))
    else:
        for r in t1:
            say("   · `%s` 態%s %s/%s（支 %s）" % (r["sit"], r["mode"], r["blk"],
                                                  r["side"], r["br"]))
    say("【造乙·必命中】`b1` 為**偽**之格數 = **" + str(len(f1)) + "**（期 ≥ 1）")
    if not f1:
        say("   🛑 **為 `0` ⇒ loud 明載**（⛔ 停機）；逐格三座標：")
        for r in ROWS:
            say("      · `%s` 態%s %s/%s｜錨(%s) = %s｜p1 = %s｜p2 = %s"
                % (r["sit"], r["mode"], r["blk"], r["side"], r["anchor_name"],
                   _v(r["anchor"]), _v(r["p1"]), _v(r["p2"])))
    # 造丙：人造點（執行期組出·字面⛔ 出艙）
    FAKE = (float(10 ** 7) + 0.5, float(2 * 10 ** 7) + 0.25)
    c1 = c2 = False
    for r in ROWS:
        if r["p1"] is not None and FAKE == r["p1"]:
            c1 = True
        if r["p2"] is not None and FAKE == r["p2"]:
            c2 = True
    say("【造丙·必偽】人造點（**執行期組出**·字面⛔ 出艙）vs p1／p2 ⇒ "
        + repr(c1) + "／" + repr(c2) + "（期 False／False） ⇒ "
        + ("✅" if not (c1 or c2) else "🔴"))
    if c1 or c2:
        say("   🛑 造丙不成立 ⇒ 判器紅、停。")
        return 5

    # ── §三-5　情形甲 ∧ R(W_0) > 0 之格 ──────────────────────────────
    say("")
    say("=" * W)
    say("【`§三-5`】情形甲 ∧ `R(W_0) > 0` 之格：依**新判準**逐格歸類")
    say("=" * W)
    sel = [r for r in ROWS if (not r["forced"]) and r["R"] is not None
           and float(r["R"]) > 0.0]
    say("   **當場重得之成員 = " + str(len(sel)) + " 格**　🛑 ⛔ 轉引前批之 `4`")
    for r in sel:
        say("   · `%s` 態%s **%s/%s**｜(b1, b2) = (%s, %s)｜**支 = %s**"
            % (r["sit"], r["mode"], r["blk"], r["side"],
               repr(r["b1"]), repr(r["b2"]), r["br"]))
        say("     錨(%s) = %s｜p1 = %s｜p2 = %s｜%s = %s"
            % (r["anchor_name"], _v(r["anchor"]), _v(r["p1"]), _v(r["p2"]),
               r["cum_name"], repr(r["cum"])))
        say("     W_0 = %s｜R(W_0) = %s｜is_corner = %s｜_fo = %s｜暫編地號 = %s"
            % (repr(r["W0"]), repr(r["R"]), repr(r["rec"]["p_is_corner"]),
               repr(r["fo"]), r["rec"]["lot"]))
        say("     â·(p2 − p1) = %s｜â·(錨 − p1) = %s｜外積 = %s"
            % (repr(r["dot_p"]), repr(r["dot_a"]), repr(r["crs"])))
    brs = sorted({r["br"] for r in sel})
    say("   ⇒ 該 " + str(len(sel)) + " 格所落之支 = " + repr(brs)
        + "（" + str(len(brs)) + " 支）")

    # ── §四　forced 側之執行期款（2／3／4）─────────────────────────────
    say("")
    say("=" * W)
    say("【`§四`】`forced` 側起算點之倉態對拍——執行期之款 `2`／`3`／`4`（**出艙即止**）")
    say("=" * W)
    fr = [r for r in ROWS if r["forced"]]
    say("  ── 款 `2`（後半）：`cum_S` 於 forced 側鏈頭格之**當場值**")
    for r in fr:
        say("     · `%s` 態%s %s/%s｜%s = %s｜b2 = %s｜W_0 = %s｜R(W_0) = %s"
            % (r["sit"], r["mode"], r["blk"], r["side"], r["cum_name"],
               repr(r["cum"]), repr(r["b2"]), repr(r["W0"]), repr(r["R"])))
        say("       錨(%s) = %s｜p1 = %s｜p2 = %s｜b1 = %s｜支 = %s"
            % (r["anchor_name"], _v(r["anchor"]), _v(r["p1"]), _v(r["p2"]),
               repr(r["b1"]), r["br"]))
    if not fr:
        say("     🛑 **無 forced 之鏈頭格**（loud 明載·⛔ 以空集充結論）")
    say("")
    say("  ── 款 `3`（後半）：`_corner_buffer_S` 之**回傳**逐次出艙")
    for k in sorted(D):
        d = D[k]
        say("     · `%s` 態%s ⇒ 呼叫 %d 次" % (k[0], k[1], len(d["bufs"])))
        for bb in d["bufs"]:
            say("       - blk=%s side=%s buf=%s range_area=%s front_p1=%s"
                % (bb["blk"], bb["side"], repr(bb["buf"]), repr(bb["range_area"]),
                   _v(bb["front_p1"])))
    say("")
    say("  ── 款 `4`：該側 `_off` 之原列（見上「情形甲／乙」段·已逐列出艙）")

    say("")
    say("=" * W)
    say("【終止態】逐態之 `run_step_g` 中止閘（照實·⛔ 列為新紅）")
    say("=" * W)
    for k in sorted(D):
        say("   · `%s` 態%s ⇒ %s" % (k[0], k[1], D[k]["err"] or "（未拋出）"))
    say("=" * W)
    return 0


if __name__ == "__main__":
    sys.exit(main())
