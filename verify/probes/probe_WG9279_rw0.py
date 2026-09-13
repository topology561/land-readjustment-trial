# -*- coding: utf-8 -*-
"""`W-G.9-279` `§四-1`／`§四-2`／`§四-3`：**`R(W_0)` 之性質量測** ＋ 情形乙三格與
`K-9-5-12（四）` 之對拍 ＋ 態乙 `R4 right` 之歸屬。

🛑 **本器⛔ 施任何替身、⛔ 做任何反事實**（單 `§七-2`）——**純量測**。
🔒 **底本** ＝ `verify/probes/probe_WG9278_w0zero.py` 之 `drive`（**替身一律關閉**·⛔ 另寫第二份判準）。
🔒 **受詞改繫於 `R(W_0)`**（＝ **性質**）而⛔ `W_0`（＝ **代理量**）——發單側之裁（單 `§零′`）。
🔒 **`R(·)` 一律以 `ns["rw_from_width"]` 取值**；**`W(·)` 一律以 `ns["k956_W_from_mp"]` 取值**——⛔ 器內另算。

🛑 **坑之攔法**：`bb`（框內省 `sys._getframe(depth + 1)` ＋ 自我驗證閘）／
   `bd`（必為零之哨兵**執行期組出**·字面⛔ 出艙）／`be`（生產碼母體**正面列舉**·⛔ pathspec glob）。

🛑 **⛔ 判任何側是否違反 `K-9-5-12`、⛔ 判 `（四）` 之射程、⛔ 提修法主張**——**出艙即止**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9279_rw0.py [倉根]`
`rc`：`0`／`5` **器紅**（框內省閘不過／判別力二造同色）。
"""
import contextlib
import csv
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
    rwi, bufs = [], []
    _o_rwi = ns["rw_increment"]
    _o_cbs = ns["_corner_buffer_S"]

    def _climb(names, upto=16):
        out = {k: None for k in names}
        for d in range(1, upto + 1):
            try:
                f = sys._getframe(d + 1)        # 🔒 +1 ＝ 補本函式自身之一層（坑 `bb`）
            except ValueError:
                break
            for k in names:
                if out[k] is None and k in f.f_locals:
                    out[k] = f.f_locals[k]
        return out

    def _spy_rwi(W_prev, W_cur):
        out = _o_rwi(W_prev, W_cur)             # 🛑 ⛔ 替身·逐位原樣
        # 🔒 `_side_mid_*`／`*_cum_S`／`baseline_pt` 一律**於此處**取——其於
        #    `_corner_buffer_S` 之呼叫時點**尚未賦值**（在同一街廓迴圈之後段）
        #    ⇒ 於彼處取必得**前一街廓**之值（本批自捕之量測器紅）。
        # 🔒 **一律取 `solve_G_binary` 之<u>參數本身</u>**（`baseline_pt`／`side_mid`／
        #    `allocation_dir`／`d_hat`）——⛔ 取外層之 `allocation_dir_block`／`_side_mid_*`：
        #    `app.py:10194`–`:10196` 逐字載「**街角第 1 宗之 `allocation_dir` 已換為
        #    `_first_corner_alloc_dir(side_mid)`**」⇒ 外層之值於**鏈頭**恰為錯者（本批自捕）。
        #    `_climb` 自內層起取 ⇒ 其所得即該次呼叫**實際所用**者。
        p = _climb(["is_corner", "is_chain_head", "blk_label", "side", "tp",
                    "baseline_pt", "side_mid", "allocation_dir", "d_hat",
                    "left_cum_S", "right_cum_S", "corner_pt"])
        tp = p.get("tp") or {}
        rwi.append({"W_prev": float(W_prev), "W_cur": float(W_cur), "out": float(out),
                    "is_corner": p.get("is_corner"), "is_chain_head": p.get("is_chain_head"),
                    "blk": p.get("blk_label"), "side": _ns(p.get("side")),
                    "lot": (tp.get("暫編地號") if isinstance(tp, dict) else None),
                    "mp": p.get("side_mid"), "alloc": p.get("allocation_dir"),
                    "cumL": p.get("left_cum_S"), "cumR": p.get("right_cum_S"),
                    "baseline_pt": p.get("baseline_pt"), "corner_pt": p.get("corner_pt"),
                    "d_hat": p.get("d_hat")})
        return out

    def _spy_cbs(block_poly, d_hat, front_p1, allocation_dir, range_area, side, **kw):
        out = _o_cbs(block_poly, d_hat, front_p1, allocation_dir, range_area, side, **kw)
        p = _climb(["blk_label", "_side_mid_left", "_side_mid_right"])
        bufs.append({"blk": p.get("blk_label"), "side": _ns(side), "buf": float(out),
                     "d_hat": d_hat, "corner_pt": front_p1, "alloc": allocation_dir,
                     "range": float(range_area),
                     "mp_left": p.get("_side_mid_left"), "mp_right": p.get("_side_mid_right")})
        return out

    ns["rw_increment"] = _spy_rwi
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
    n0 = len(rwi)
    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                       params, build_p, wins, forced, sb, eff_min_build_by_blk={})
    except RuntimeError as e:
        err = str(e).split("\n")[0][:170]
    fo = (fake_st.session_state.get("f3L_forced_offset", {}) or {})
    fo_tab = {b: (bool((fo.get(b) or {}).get("left_forced_offset", False)),
                  bool((fo.get(b) or {}).get("right_forced_offset", False)))
              for b in BLKS}
    return {"rwi": rwi, "from_stepg": n0, "bufs": bufs, "off": list(_off or []),
            "fo": fo_tab, "err": err,
            "R": ns["rw_from_width"], "K": ns["k956_W_from_mp"], "np": ns["np"]}


def _heads(d):
    """鏈頭之筆（每 (blk, side) 取其最末）——`run_step_g` 段。"""
    out = {}
    for r in d["rwi"][d["from_stepg"]:]:
        if not (bool(r["is_corner"]) or bool(r["is_chain_head"])):
            continue
        if r["blk"] is None or r["side"] is None:
            continue
        out[(r["blk"], r["side"])] = r
    return out


def main():
    say("=" * W)
    say("【`W-G.9-279` `§四`】`R(W_0)` 之性質量測"
        "（**替身一律關閉·⛔ 反事實**）")
    say("=" * W)
    say("\U0001f6d1 **⛔ 判任何側是否違反 `K-9-5-12`、"
        "⛔ 判（四）之射程、⛔ 提修法主張**——出舱即止。")

    D = {}
    for sb in SBS:
        tag = "%gm" % sb
        for lab, mode in ((M_A, None), (M_B, "off")):
            D[(tag, lab)] = drive(sb, mode)
    os.environ.pop(ENV, None)
    R = D[("0m", M_A)]["R"]

    # ── 框內省之自我驗證閘 ────────────────────────────────────────
    say("")
    say("─" * W)
    say("【自我驗證閘】框內省所錄之 `blk_label`"
        "（⛔ 不過即 loud 拒測·坑 `bb`）")
    say("─" * W)
    bad = []
    for k in sorted(D):
        h = _heads(D[k])
        bl = sorted({b for b, _ in h})
        ok = bool(bl) and all(b in BLKS for b in bl)
        if not ok:
            bad.append(k)
        say("   · `%s` 態%s｜鏈頭所錄之 `blk` ＝ %s ⇒ %s"
            % (k[0], k[1], bl, "✅" if ok else "\U0001f534"))
    if bad:
        say("   \U0001f6d1 **不過**（%s）⇒ loud 拒測。" % bad)
        return 5
    say("   ⇒ **器非紅** ✅")

    # ── 情形甲／乙（逐情境 × 逐態·源 ＝ `_off` 之 `指配`）──────────
    FORCED = {}
    say("")
    say("─" * W)
    say("【情形甲／乙】源 ＝ `run_corner_pk` 之第三回傳 `_off` 之 `指配` 欄")
    say("─" * W)
    for k in sorted(D):
        s = set()
        for r in D[k]["off"]:
            b = str(r.get("街廓", ""))
            sd = _ns(r.get("端"))
            if "強制抵費地" in str(r.get("指配", "")) and b and sd:
                s.add((b, sd))
        FORCED[k] = s
        say("   · `%s` 態%s ⇒ `_off` %d 列｜乙之格 ＝ %s"
            % (k[0], k[1], len(D[k]["off"]), sorted(s) or "（無）"))
        for r in D[k]["off"]:
            say("     - %r" % (r,))

    # ── `§四-1` 主表：24 格 ──────────────────────────────────────
    say("")
    say("─" * W)
    say("【`§四-1` 主表】`R(W_0)` 之性質"
        "（母體 ＝ `W-G.9-278` 之**同一** `24` 格定義·逐格一列）")
    say("─" * W)
    say("   | 情境 | 態 | 街廓 | 側 | `W_0`（未捨入·帶號） | "
        "**`R(W_0)`** | `R(W_0) > 0`？ | 情形 | `_fo` | `is_corner` | `is_chain_head` |")
    say("   |---|---|---|---|---|---|---|---|---|---|---|")
    ROWS = []
    for sb in SBS:
        tag = "%gm" % sb
        for lab in (M_A, M_B):
            h = _heads(D[(tag, lab)])
            for b in BLKS:
                for sd in ("left", "right"):
                    r = h.get((b, sd))
                    cls = "乙" if (b, sd) in FORCED[(tag, lab)] else "甲"
                    fo = D[(tag, lab)]["fo"][b][0 if sd == "left" else 1]
                    if r is None:
                        say("   | `%s` | %s | `%s` | %s | — | — | 【**⛔ 可得**】 | %s | %s | — | — |"
                            % (tag, lab, b, sd, cls, fo))
                        continue
                    w0 = r["W_prev"]
                    rw0 = float(R(w0))
                    ROWS.append({"tag": tag, "lab": lab, "blk": b, "sd": sd, "w0": w0,
                                 "R": rw0, "cls": cls, "fo": fo, "lot": r["lot"]})
                    say("   | `%s` | %s | `%s` | %s | `%.10f` | **`%.10f`** | %s | %s | %s | %s | %s |"
                        % (tag, lab, b, sd, w0, rw0,
                           "**是**" if rw0 > 0 else "否", cls, fo,
                           r["is_corner"], r["is_chain_head"]))
    say("   ⇒ 有值之格 ＝ **%d**｜其中 `R(W_0) > 0` 者 ＝ **%d**"
        % (len(ROWS), sum(1 for x in ROWS if x["R"] > 0)))

    # ── `§四-1` 判別力二造 ──────────────────────────────────────
    say("")
    say("─" * W)
    say("【`§四-1` 判別力二造】甲[必為零] `W_0 ≤ 0` ⇒ `R(W_0) == 0`｜"
        "乙[必非零] `W_0 > 0` ⇒ `R(W_0) > 0`")
    say("─" * W)
    a = [x for x in ROWS if x["w0"] <= 0]
    b2 = [x for x in ROWS if x["w0"] > 0]
    a_ok = all(x["R"] == 0.0 for x in a)
    b_ok = all(x["R"] > 0 for x in b2)
    say("   · 造甲（`W_0 ≤ 0`）格數 ＝ **%d**｜其 `R(W_0) == 0` 者 ＝ **%d** ⇒ %s"
        % (len(a), sum(1 for x in a if x["R"] == 0.0), "✅" if a_ok else "\U0001f534"))
    say("   · 造乙（`W_0 > 0`）格數 ＝ **%d**｜其 `R(W_0) > 0` 者 ＝ **%d** ⇒ %s"
        % (len(b2), sum(1 for x in b2 if x["R"] > 0), "✅" if b_ok else "\U0001f534"))
    for x in b2:
        say("     - `%s` 態%s `%s` %s｜`W_0` ＝ `%.10f`｜`R(W_0)` ＝ **`%.10f`**｜情形 %s｜宗 `%s`"
            % (x["tag"], x["lab"], x["blk"], x["sd"], x["w0"], x["R"], x["cls"], x["lot"]))
    if not a or not b2:
        say("   \U0001f7e1 **二造之一為空** ⇒ 【**⛔ 可得**】"
            "，**⛔ 以其綿充器非紅**。")
        return 5
    if not (a_ok and b_ok):
        say("   \U0001f6d1 **二造同色 ⇒ 器紅** ⇒ `rc = 5`")
        return 5
    say("   ⇒ **器非紅** ✅（二造异色）")

    # ── `§四-2` 情形乙三格與 `K-9-5-12（四）` 之對拍 ────────────
    say("")
    say("─" * W)
    say("【`§四-2`】情形乙與 `K-9-5-12（四）` 之對拍"
        "（`W(·)` 一律以 `ns[\"k956_W_from_mp\"]` 取值·⛔ 器內另算）")
    say("─" * W)
    say("   \U0001f512 **帶之構造逐字**（`app.py` `_corner_buffer_S` docstring）：")
    say("     `side='left'`  → 帶 `s ∈ [max(s_min, 0), buf]`   ← **上界＝`buf`**")
    say("     消費端 `left_cum_S = buf` ⇒ 首宗自 `s=buf` 起 ⇒ 保留區恒為 `[s_min, buf]`")
    say("   ⇒ 抵費地之**遠側**境界線上之點 ＝ `corner_pt + buf · d̂_單位`"
        "（**座標系 ＝ 沿推進向 `d̂` 自 `corner_pt` 量起**·⛔ 時序）")
    np = D[("0m", M_A)]["np"]
    K = D[("0m", M_A)]["K"]

    # ── 🔒 還原之自我驗證閘（`CLAUDE.md`：探針還原內部幾何須以碼面自身之保證為閘）──
    say("")
    say("   \U0001f512 **還原之自我驗證閘**（⛔ 該閘不過不准據以下任何結論）")
    say("     碼面之保證 ＝ `_W_near = float(np.dot(_bp_w - _mp_w, _ahat))`"
        "（`solve_G_binary`），其 `_bp_w` ＝ `baseline_pt`、`_mp_w` ＝ `side_mid`")
    say("     ⇒ 以 `ns[\"k956_W_from_mp\"](baseline_pt, mp, alloc, d_hat)` 重建之 `W`"
        "須與碼面之 `W_0` **逐位相符**。")
    say("     | 情境 | 態 | 街廓 | 側 | 重建 `W` | 碼面 `W_0` | 判 |")
    say("     |---|---|---|---|---|---|---|")
    gate_n = gate_ok = 0
    for k in sorted(D):
        for (b, sd), r in sorted(_heads(D[k]).items()):
            mp = r["mp"]
            if r["baseline_pt"] is None or mp is None or r["alloc"] is None or r["d_hat"] is None:
                say("     | `%s` | %s | `%s` | %s | 【**⛔ 可得**】 | `%.10f` | \U0001f7e1 |"
                    % (k[0], k[1], b, sd, r["W_prev"]))
                continue
            gate_n += 1
            wr = float(K(r["baseline_pt"], mp, r["alloc"], r["d_hat"]))
            same = ("%.10f" % wr) == ("%.10f" % r["W_prev"])
            gate_ok += same
            say("     | `%s` | %s | `%s` | %s | `%.10f` | `%.10f` | %s |"
                % (k[0], k[1], b, sd, wr, r["W_prev"], "✅" if same else "\U0001f534"))
    say("     ⇒ 所驗之格 ＝ **%d**｜逐位相符 ＝ **%d**" % (gate_n, gate_ok))
    if gate_n == 0 or gate_ok != gate_n:
        say("     \U0001f6d1 **還原之自我驗證閘不過** ⇒ loud 拒測"
            "（`rc = 5`），**⛔ 據以下任何結論**。")
        return 5
    say("     ⇒ **閘過** ✅")

    say("")
    say("   | 情境 | 態 | 街廓 | 側 | `buf` | `range(㎡)` | "
        "`W(遠側)`（`k956`） | `W_0`（碼面） | `Δ` | 判 |")
    say("   |---|---|---|---|---|---|---|---|---|---|")
    farv = []
    for k in sorted(D):
        d = D[k]
        h = _heads(d)
        for bf in d["bufs"]:
            b, sd = bf["blk"], bf["side"]
            if (b, sd) not in FORCED[k]:
                continue
            r = h.get((b, sd))
            if r is None:
                say("   | `%s` | %s | `%s` | %s | `%.10f` | `%.4f` | 【**⛔ 可得**】 | "
                    "— | — | 【**⛔ 可得**】（該側無鏈頭之記錄）|"
                    % (k[0], k[1], b, sd, bf["buf"], bf["range"]))
                continue
            mp = r["mp"]
            dh = np.asarray(r["d_hat"], dtype=float)
            dn = float(np.linalg.norm(dh))
            dhu = dh / dn if dn > 1e-9 else dh
            cp = np.asarray(r["corner_pt"], dtype=float)
            far_pt = cp + float(bf["buf"]) * dhu
            w_far = float(K(far_pt, mp, r["alloc"], r["d_hat"]))
            w_near = float(K(cp, mp, r["alloc"], r["d_hat"]))
            farv.append(w_far)
            w0 = r["W_prev"]
            say("   | `%s` | %s | `%s` | %s | `%.10f` | `%.4f` | `%.10f` | `%.10f` | `%+.3e` | %s |"
                % (k[0], k[1], b, sd, bf["buf"], bf["range"], w_far, w0, w_far - w0,
                   "**逐位相符**" if ("%.10f" % w_far) == ("%.10f" % w0)
                   else "**⛔ 相符**"))
            say("     · 併錄：該側之 `%s_cum_S` ＝ `%r`｜`buf` ＝ `%.10f`"
                "｜二者 %s"
                % ("left" if sd == "left" else "right",
                   r["cumL"] if sd == "left" else r["cumR"], bf["buf"],
                   "**逐位相同**" if (
                       "%.10f" % float(r["cumL"] if sd == "left" else r["cumR"])
                       == "%.10f" % bf["buf"]) else "**相異**"))
            say("     · 判別力 甲[必不符] 同片之**近側**境界線"
                "（`corner_pt`·`s≈0`）⇒ `W` ＝ `%.10f` ⇒ %s"
                % (w_near, "**⛔ 相符** ✅"
                   if ("%.10f" % w_near) != ("%.10f" % w0) else "\U0001f534 **逐位相符**"))
            say("     · 判別力 乙[必相符] `W_0` 與其自身 ⇒ **逐位相符** ✅")
    if not farv:
        say("   \U0001f7e1 **情形乙之格為空** ⇒ 【**⛔ 可得**】")

    # ── `§四-3` 態乙 `R4 right` 之歸屬 ──────────────────────────
    say("")
    say("─" * W)
    say("【`§四-3`】態乙（`WV_K6_STEP0=off`）之全母體"
        "｜並具名 `R4 right`")
    say("─" * W)
    say("   | 情境 | 街廓 | 側 | 情形 | `W_0` | **`R(W_0)`** | `R(W_0) > 0`？ | `_fo` | `is_chain_head` |")
    say("   |---|---|---|---|---|---|---|---|---|")
    yi = [x for x in ROWS if x["lab"] == M_B]
    for x in yi:
        h = _heads(D[(x["tag"], M_B)])
        r = h.get((x["blk"], x["sd"]))
        say("   | `%s` | `%s` | %s | %s | `%.10f` | **`%.10f`** | %s | %s | %s |"
            % (x["tag"], x["blk"], x["sd"], x["cls"], x["w0"], x["R"],
               "**是**" if x["R"] > 0 else "否", x["fo"],
               (r or {}).get("is_chain_head")))
    r4 = [x for x in yi if x["blk"] == "R4" and x["sd"] == "right"]
    say("")
    if r4:
        x = r4[0]
        h = _heads(D[(x["tag"], M_B)])
        r = h.get(("R4", "right"))
        for x in r4:
            say("   \U0001f511 **`R4 right`（態乙·`%s`）之四項**："
                "情形 ＝ **%s**｜`_fo_right` ＝ **%s**｜"
                "**`R(W_0)` ＝ `%.10f`**｜`is_chain_head` ＝ **%s**｜"
                "（`W_0` ＝ `%.10f`·宗 `%s`）"
                % (x["tag"], x["cls"], x["fo"], x["R"],
                   (_heads(D[(x["tag"], M_B)]).get(("R4", "right")) or {}).get("is_chain_head"),
                   x["w0"], x["lot"]))
    else:
        say("   \U0001f7e1 **態乙之 `R4 right` ⛔ 在母體** ⇒ 【**⛔ 可得**】")
    vals = {("%.10f" % x["R"]) for x in yi}
    say("   \U0001f512 **判別力**：態乙各格之 `R(W_0)` 相異值數 ＝ **%d**"
        "（若全同值 ⇒ 先判器紅）⇒ %s"
        % (len(vals), "✅ 非全同" if len(vals) > 1 else "\U0001f534 全同"))
    if len(vals) <= 1:
        say("   \U0001f6d1 ⇒ `rc = 5`")
        return 5

    # ── got_抵費地 CSV 之逐列（`§四-2` 項 1）────────────────────
    say("")
    say("─" * W)
    say("【`§四-2` 項 `1`】`verify/out/got_抵費地_退縮*.csv` 之逐列逐字")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        p = os.path.join(REPO, "verify", "out",
                         "got_抵費地_退縮%s.csv" % tag)
        if not os.path.exists(p):
            say("   · `%s` ⇒ \U0001f7e1 **檔不存在** ⇒ 【**⛔ 可得**】" % p)
            continue
        with io.open(p, encoding="utf-8-sig", newline="") as fh:
            rows = list(csv.DictReader(fh))
        say("   · `%s` ⇒ **%d** 列" % (os.path.basename(p), len(rows)))
        for r in rows:
            say("     - %r" % (r,))
        say("     → 與態甲 `_off`（%d 列）之列數 %s"
            % (len(D[(tag, M_A)]["off"]),
               "**相同** ✅" if len(rows) == len(D[(tag, M_A)]["off"])
               else "\U0001f534 **相異**"))

    say("")
    say("─" * W)
    say("【終止態】")
    say("─" * W)
    for k in sorted(D):
        say("   · `%s` 態%s ⇒ %s" % (k[0], k[1], D[k]["err"]))
    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
