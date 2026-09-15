# -*- coding: utf-8 -*-
"""`W-G.9-298` `§三`：閘 `(iii)` **重設造**之機驗 ＋ `A′`／`B′` 之**當場重得**。

🔑 **重設之造**（`§一` 裁 `5`）——原造「`W_0′` 須與生產錄逐位相同」於三格中二格**結構上不可成立**
   （`_mp_base_W0` 之定義與呼叫皆在 `not _degenerate_order and _N > 1` 內·該二格 `_N` ＝ `1`）
   ⇒ 改驗**可於三格皆成立**之二事：
   ① **同一性**：器所調用之 `k956_W_from_mp` 與 `ns["k956_W_from_mp"]` **係同一物件**（`is`·**`id(·)` ⛔ 作錨**）；
   ② **可得之格**（`3.5 R2/left`）其輸出與**生產錄**逐位相同。

🔒 **母體⛔ 含器自身之輸出**：生產錄一律限 `drive()` 期間之**前綴** `d["K956"][:n0]`。
🔒 **原語一律委派 `ns`**（`_block_strip`／`_strip_s_range`／`_corner_buffer_S`／`k956_W_from_mp`／`rw_from_width`）；
   帶之構造復用 `probe_WG9292_pathC.band_poly`、`W_0` 之重建式復用 `probe_WG9295_joint._w0`
   （**⛔ 動該二檔一字**·⛔ 自寫第二套幾何或第二份 `W` 之定義·`GB-48` 族）。
🔒 **設計驗算之射程**（單 `§三` 款 `4` 明文授權）＝ **於 `forced` 消費端以 `_first_corner_alloc_dir(side_mid)`
   取代當場之 `allocation_dir` 複算路丙之帶**，**⛔ 逾此一處**；其出艙一律冠 `【設計驗算·⛔ 非實測】`。

`rc`：`0` 全綠／`5` **量測器紅**（判別力四造任一不成立）。
用法：python verify/probes/probe_WG9298_gate3.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import probe_WG9292_pathC as P                      # noqa: E402
import probe_WG9295_joint as J                      # noqa: E402

W = 132
TAG = "【設計驗算·⛔ 非實測】"
_LOG = []
RED = [0]


def say(s=""):
    print(s)
    _LOG.append(s)


def red(s):
    RED[0] = 5
    say("🔴 **量測器紅**：" + s)


def _t(v):
    if v is None:
        return None
    try:
        return tuple(float(x) for x in v)
    except Exception:                                # noqa: BLE001
        return repr(v)


def drive_traced(sb):
    """`settrace` 攔 `solve_G_binary`（locals ＋ **回傳 dict**）／`_mp_base_W0`／`_advance_block_with_split`。"""
    JIA, YI, GUARD = [], [], []

    def _loc(frame, event, arg):
        if event != "return":
            return _loc
        cn, fl, bk = frame.f_code.co_name, frame.f_locals, frame.f_back
        bl = bk.f_locals if bk is not None else {}
        if cn == "solve_G_binary":
            bl2, depth = {}, None
            _f = bk
            for _i in range(1, 16):
                if _f is None:
                    break
                if "blk_label" in _f.f_locals:
                    bl2, depth = _f.f_locals, _i
                    break
                _f = _f.f_back
            out = arg if isinstance(arg, dict) else {}
            JIA.append({"blk": bl2.get("blk_label"), "blk_key_exists": (depth is not None),
                        "blk_depth": depth, "side_label": fl.get("side_label"),
                        "is_corner": fl.get("is_corner"), "is_chain_head": fl.get("is_chain_head"),
                        "side_mid": _t(fl.get("side_mid")),
                        "_W_near_out": fl.get("_W_near_out"), "_rw_start": fl.get("_rw_start"),
                        "ad_out": _t(out.get("allocation_dir")),
                        "cut": out.get("cut_coords") or []})
        elif cn == "_mp_base_W0":
            YI.append({"blk": bl2_get(bl), "side": _side_of(fl.get("_buf"), bl),
                       "_buf": fl.get("_buf"), "out": arg})
        return _loc

    def bl2_get(bl):
        return bl.get("blk_label")

    def _side_of(buf, bl):
        for nm, tag in (("_left_buffer_S", "left"), ("_right_buffer_S", "right")):
            try:
                if buf is not None and bl.get(nm) is not None and float(buf) == float(bl.get(nm)):
                    return tag
            except Exception:                        # noqa: BLE001
                pass
        return None

    def _glob(frame, event, arg):
        if event != "call":
            return None
        cn = frame.f_code.co_name
        if cn == "_advance_block_with_split":
            bk = frame.f_back
            bl = bk.f_locals if bk is not None else {}
            GUARD.append({"blk": bl.get("blk_label"), "blk_key_exists": ("blk_label" in bl),
                          "_degenerate_order": bl.get("_degenerate_order"),
                          "_deg_key_exists": ("_degenerate_order" in bl),
                          "_N": bl.get("_N"), "_N_key_exists": ("_N" in bl),
                          "lineno": bk.f_lineno if bk is not None else None})
            return None
        return _loc if cn in ("solve_G_binary", "_mp_base_W0") else None

    old = sys.gettrace()
    sys.settrace(_glob)
    try:
        d = P.drive(sb)
    finally:
        sys.settrace(old)
    d["JIA"], d["YI"], d["GUARD"] = JIA, YI, GUARD
    d["n_k956_0"] = len(d["K956"])
    return d


def called_code(ns, fn, *a):
    """回傳 `fn(*a)` 期間**所見之全部 `code` 物件**（`settrace` 之 `call` 事件·⛔ `id(·)` 作錨）。

    🩸 **自捕（v1）**：首版只取**第一個** `call` 事件，而 `J._w0` 於呼 `k956_W_from_mp` **之前**
       先呼 `numpy` 之 `asarray`／`linalg.norm` ⇒ 攔到的是 `numpy`、**⛔ 受詞** ⇒ 三格皆偽 `False`。
       ⇒ 改**蒐集全部**，以 `is` 判受詞之 `code` **是否在其中**（⛔ 以順序為準）。
    """
    seen = []

    def _g(frame, event, arg):
        if event == "call":
            seen.append(frame.f_code)
        return None

    old = sys.gettrace()
    sys.settrace(_g)
    try:
        out = fn(*a)
    finally:
        sys.settrace(old)
    return out, seen


def analyse(sb, d):
    ns, crp = d["ns"], d["crp"]
    R = ns["rw_from_width"]
    n0 = d["n_k956_0"]
    say("")
    say("=" * W)
    say("【`SB` ＝ %s m·態甲】**逐閘執行次數**：`solve_G_binary` **%d**／`_mp_base_W0` **%d**／"
        "`_advance_block_with_split` **%d**／`_build_corner_range_v3` **%d**（段 **%d**）／"
        "`_corner_buffer_S` **%d**（段內 **%d**）／`k956_W_from_mp` 生產錄 **%d**"
        % (repr(sb), len(d["JIA"]), len(d["YI"]), len(d["GUARD"]), len(d["RNG"]),
           len(d["RNG"]) - d["n_rng0"], len(d["BUF"]), len(d["BUF"]) - d["n_buf0"], n0))
    say("　`run_step_g` 終局 ＝ %s；`(甲)` 上溯命中率 ＝ `%d`／`%d`；`blk_label` 存在率：守衛 `%d`／`%d`"
        % (d["err"] or "（未拋）",
           sum(1 for r in d["JIA"] if r["blk_depth"] is not None), len(d["JIA"]),
           sum(1 for r in d["GUARD"] if r["blk_key_exists"]), len(d["GUARD"])))
    say("=" * W)

    grids = []
    for b in P.BLKS:
        L, Rt = d["fo"][b]
        if L:
            grids.append((b, "left"))
        if Rt:
            grids.append((b, "right"))
    say("🔒 `forced` 格 ＝ **%d**（%s）" % (len(grids), "、".join("%s/%s" % g for g in grids)))

    rows = []
    for blk, side in grids:
        say("")
        say("─" * W)
        say("### `%s`／`%s`＠`SB = %s`" % (blk, side, repr(sb)))
        br, nb = P._pick(d["BUF"], blk, side)
        rr, nr = P._pick(d["RNG"], blk, side)
        cp = crp.get((blk, side))
        if br is None or rr is None or cp is None:
            red("`%s/%s`：錄 `_corner_buffer_S` %d／`_build_corner_range_v3` %d／`crp` %s ⇒ loud 拒測"
                % (blk, side, nb, nr, cp is not None))
            continue
        loc = rr["loc"]
        S1_perp = float(loc.get("S1_perp"))
        Tp = tuple(float(x) for x in loc.get("_Tp"))
        su = (float(loc.get("sux")), float(loc.get("suy")))
        bp_, dh_, fp_ = br["block_poly"], br["d_hat"], br["front_p1"]
        ad1, ra, tol, buf1 = br["allocation_dir"], float(br["range_area"]), br["tol"], br["buf"]
        sl = ((d["st"].session_state.get("f3_cad_side_lines_by_side", {}) or {})
              .get(blk, {}) or {}).get(side, {}) or {}
        sm = _t(sl.get("mid"))

        # ══ 款 2：守衛之各分項 ════════════════════════════════════════════════
        gs = [r for r in d["GUARD"] if r["blk"] == blk]
        say("  **款 `2`**　守衛 `not _degenerate_order and _N > 1` 之**各分項**（⛔ 只報合取·⛔ 轉引前批）")
        for g in gs:
            _d2, _n2 = g["_degenerate_order"], g["_N"]
            say("      `_degenerate_order` ＝ `%r`（鍵存在 %s）／`_N` ＝ `%r`（鍵存在 %s）／呼叫列 `%r`"
                " ⇒ `not _deg` ＝ **%s**／`_N > 1` ＝ **%s** ⇒ 合取 ＝ **%s**"
                % (_d2, g["_deg_key_exists"], _n2, g["_N_key_exists"], g["lineno"],
                   (None if _d2 is None else not _d2), (None if _n2 is None else _n2 > 1),
                   (None if (_d2 is None or _n2 is None) else ((not _d2) and (_n2 > 1)))))
        if not gs:
            say("      🟡 **不可得（loud）**——本街廓無 `_advance_block_with_split` 之錄")

        # ══ 款 3：可得之格之逐位對拍 ═════════════════════════════════════════
        w0_cur, code_used = called_code(ns, J._w0, ns, fp_, buf1, dh_, sl.get("mid"), ad1)
        import numpy as _np
        _du = _np.asarray(dh_, dtype=float)
        _du = _du / float(_np.linalg.norm(_du))
        _bp0 = _np.asarray(fp_, dtype=float) + float(buf1) * _du
        hit = [r for r in d["K956"][:n0]
               if float(_np.max(_np.abs(_np.asarray(r["point"], dtype=float)[:2] - _bp0[:2]))) <= 1e-12]
        say("  **款 `3`**　可得之格之逐位對拍（母體 ＝ `drive()` 期間之**前綴**·⛔ 含器自身之輸出）")
        say("      生產錄 ＝ **%d** 筆／器自身已追加 ＝ **%d** 筆（**後者⛔ 入母體**）"
            % (n0, len(d["K956"]) - n0))
        say("      器以**現行 `buf`** 重建之 `W_0` ＝ `%r`" % w0_cur)
        if hit:
            dv = min(abs(float(r["out"]) - w0_cur) for r in hit)
            say("      本格之生產錄命中 **%d** 筆·最小差 ＝ `%r` ⇒ %s"
                % (len(hit), dv, "✅ **逐位相同**" if dv == 0.0 else "🔴 **相異**"))
            ok3 = (dv == 0.0)
        else:
            say("      🟡 **結構上不可得（loud）**——本格無生產錄；其**分項成因**見款 `2`"
                "（`_N > 1` 為偽）·**⛔ 判為 `0`、⛔ 判為「回測不過」**")
            ok3 = None

        # ══ 款 4：A′／B′ 之當場重得（設計驗算）════════════════════════════════
        ad2 = ns["_first_corner_alloc_dir"](sl.get("mid"))
        buf2 = ns["_corner_buffer_S"](bp_, dh_, fp_, ad2, ra, side, tol=tol,
                                      _label="WG9298設計驗算·" + blk)
        g2, dom2, ar2 = P.band_poly(ns, bp_, dh_, fp_, ad2, buf2, side)
        w0_new = J._w0(ns, fp_, buf2, dh_, sl.get("mid"), ad2)
        dW = abs(w0_new - S1_perp)
        L_su, L_edge = J._span(cp, su), None
        er, dr = P.far_range_edge(cp, Tp, su)
        if er is not None:
            L_edge = P._elen(er)
        L = max(x for x in (L_su, L_edge) if x is not None)
        A_lim, B_lim = 0.005 / L, 0.005
        jy = float(cp.difference(g2).area) if g2 is not None else None
        yj = float(g2.difference(cp).area) if g2 is not None else None
        sym2 = None if jy is None else jy + yj
        g1, dom1, ar1 = P.band_poly(ns, bp_, dh_, fp_, ad1, buf1, side)
        sym1 = None if g1 is None else float(cp.difference(g1).area) + float(g1.difference(cp).area)
        sym0 = float(cp.difference(cp).area) + float(cp.difference(cp).area)
        say("  **款 `4`**　%s `A′`／`B′` 之當場重得（⛔ 轉引 `W-G.9-295`）" % TAG)
        say("      `buf′` ＝ `%r`（現行 `buf` ＝ `%r`·差 帶號 `%r`／絕對值 `%r`）"
            % (buf2, buf1, buf2 - buf1, abs(buf2 - buf1)))
        say("      `W_0′` ＝ `%r`／`S1_perp` ＝ `%r`／**`|W_0′ − S1_perp|` ＝ `%r`**" % (w0_new, S1_perp, dW))
        say("      跨距：`L_su` ＝ `%r`／`L_edge` ＝ `%r` ⇒ **取較大者 ＝ `%r`**" % (L_su, L_edge, L))
        say("      `A′` 界 ＝ `0.005 ÷ %r` ＝ `%r`；實測 `%r`；比值 `%r` ⇒ %s"
            % (L, A_lim, dW, dW / A_lim, "✅" if dW <= A_lim else "🛑 **逾界**"))
        say("      對稱差（甲 ＝ 範圍多邊形／乙 ＝ 路丙之帶）：`甲∖乙` `%r`／`乙∖甲` `%r` ⇒ **`B′` 實測 `%r`**"
            % (jy, yj, sym2))
        say("      `B′` 界 ＝ `%r`；比值 `%r` ⇒ %s"
            % (B_lim, None if sym2 is None else sym2 / B_lim,
               "✅" if (sym2 is not None and sym2 <= B_lim) else "🛑 **逾界**"))
        say("      判別力：現行之帶之對稱差[必非零] ＝ `%r`／範圍多邊形自比[必為零] ＝ `%r`" % (sym1, sym0))

        # ══ 款 5：切向之釘槽機驗 ═════════════════════════════════════════════
        want = "左" if side == "left" else "右"
        ja = [r for r in d["JIA"] if r["blk"] == blk and want in str(r["side_label"] or "")]
        ja2 = [r for r in d["JIA"] if sm is not None and r["side_mid"] == sm]
        pick = [r for r in (ja or ja2) if (r["is_corner"] or r["is_chain_head"])]
        say("  **款 `5`**　切向之**釘槽**機驗（⛔ 報「向量之夾角」而不釘其槽·以**實邊**）")
        say("      二鍵並報：鍵甲（`blk_label`＋`side_label`）＝ **%d**／鍵乙（`side_mid` 逐位）＝ **%d**·一致 ＝ %s"
            % (len(ja), len(ja2), len(ja) == len(ja2)))
        cos_a = None
        if not pick:
            say("      🟡 **無鏈頭之錄（loud）**——⛔ 判為 `0`")
        else:
            h = pick[0]
            ad_u = h["ad_out"]
            cut = h["cut"]
            if ad_u is None or len(cut) < 3:
                say("      🟡 **不可得（loud）**——`allocation_dir`（碼註逐字「實際使用之臨街向」）＝ `%r`／"
                    "`cut_coords` 頂點數 ＝ `%d`" % (ad_u, len(cut)))
            else:
                want_v = P._unit(P._rot90(P._unit(ad_u)))
                best, bc = None, -1.0
                pts = [tuple(p) for p in cut]
                for i in range(len(pts) - 1):
                    e = (pts[i], pts[i + 1])
                    c = P._cos(P._edir(e), want_v) or 0.0
                    if c > bc:
                        best, bc = e, c
                say("      槽 ＝ `rot90(allocation_dir)`（法向槽·`allocation_dir` ＝ `%r`）；"
                    "該宗 `cut_coords` 之**實邊**（%d 邊）最大 `|cos|` ＝ `%r`（與 `1` 之差 `%r`）"
                    % (ad_u, len(pts) - 1, bc, abs(bc - 1.0)))
                cos_a = bc
        if er is not None:
            c2 = P._cos(P._edir(er), su)
            say("      槽 ＝ `su`（SIDE 之**線向**）；範圍多邊形之遠側境界線**實邊**之 `|cos|` ＝ `%r`"
                "（與 `1` 之差 `%r`·長 `%r`）" % (c2, abs(c2 - 1.0), P._elen(er)))
        else:
            say("      🟡 遠側境界線**實邊**⛔ 尋得（loud）")

        rows.append({"sb": sb, "blk": blk, "side": side, "ok3": ok3, "w0_cur": w0_cur,
                     "buf1": buf1, "buf2": buf2, "w0_new": w0_new, "S1": S1_perp,
                     "dW": dW, "L": L, "A_lim": A_lim, "sym2": sym2, "sym1": sym1,
                     "sym0": sym0, "cos_a": cos_a, "code_used": code_used})
    return rows, d


def main():
    allrows, last = [], None
    for sb in P.SBS:
        d = drive_traced(sb)
        r, _ = analyse(sb, d)
        allrows += r
        last = d

    ns = last["ns"]
    say("")
    say("=" * W)
    say("## 款 `1`　**同一性**（`is` 比對·🛑 **`id(·)` ⛔ 作錨**）與 `ns` 之來源")
    say("=" * W)
    f_ns = ns["k956_W_from_mp"]
    say("   `ns[\"k956_W_from_mp\"]` 之 `__name__` ＝ `%r`／`__qualname__` ＝ `%r`"
        % (getattr(f_ns, "__name__", None), getattr(f_ns, "__qualname__", None)))
    _c_ns = getattr(f_ns, "__code__", None)
    same_code = [any(c is _c_ns for c in (r["code_used"] or [])) for r in allrows]
    say("   **器所調用者**（`settrace` 之 `call` 事件·**全部**·⛔ 只取第一個）其中是否含 "
        "`ns[\"k956_W_from_mp\"].__code__`（`is`）⇒ 逐格 %r（`%d`／`%d` 為真）"
        % (same_code, sum(1 for x in same_code if x), len(same_code)))
    for r in allrows:
        nm = [c.co_name for c in (r["code_used"] or [])]
        k9 = [c for c in (r["code_used"] or []) if c.co_name == "k956_W_from_mp"]
        say("      `%s/%s`：呼叫鏈之 `co_name`（序·節略 `8`）＝ %r；其中 `co_name == 'k956_W_from_mp'` "
            "者 ＝ **%d** 個%s"
            % (r["blk"], r["side"], nm[:8], len(k9),
               ("（`co_filename` ＝ %r）" % os.path.basename(k9[0].co_filename)) if k9 else ""))
    say("   🔒 **照實併記**：`ns[\"k956_W_from_mp\"]` 現為 `drive.<locals>._spy_k`——**本器（`P.drive`）之包裹**；"
        "其**委派**至原函式（上列 `k956_W_from_mp` 之 `code` 即其證）。⇒ 同一性之受詞係**該包裹**，"
        "而該包裹與原函式之關係由呼叫鏈機驗、**⛔ 推定**。")
    ok_t = (f_ns is ns["k956_W_from_mp"])
    _wrap = (lambda *a, **k: f_ns(*a, **k))          # **執行期組出**之同式包裝物·字面⛔ 出艙
    ok_f = (_wrap is ns["k956_W_from_mp"])
    say("   判別力[必為真]：`ns` 之項與其自身 `is` ⇒ **%s**" % ok_t)
    say("   判別力[必為偽]：一**執行期組出**之同式包裝物 `is` `ns` 之項 ⇒ **%s**（須 False）" % ok_f)
    if not all(same_code):
        say("   🟡 **loud**：同一性於 `%d`／`%d` 格未成立 ⇒ 依 `§一` 裁 `5` 之重設造 ①，"
            "該格之機制依據**⛔ 成立**（⛔ 自加停機款·單 `§三` 款 `6` 之四造⛔ 含本項）"
            % (len(same_code) - sum(1 for x in same_code if x), len(same_code)))
    say("   🔒 **`ns` 之來源**：`type(ns)` ＝ `%r`；`ns is globals()` ⇒ **%s**；"
        "`sys.modules` 中 `__dict__ is ns` 之模組數 ＝ **%d**（須 `0` ⇒ **⛔ 任何模組之 `__globals__`**）"
        % (type(ns).__name__, ns is globals(),
           sum(1 for m in list(sys.modules.values())
               if getattr(m, "__dict__", None) is ns)))

    say("")
    say("=" * W)
    say("## 款 `6`　判別力四造之判")
    say("=" * W)
    say("   | 造 | 判準 | 實測 | 判 |")
    say("   |---|---|---|---|")
    say("   | **[必為真]** | 款 `1` 之 `ns` 項與其自身 `is` | **%s** | %s |" % (ok_t, "✅" if ok_t else "🔴"))
    say("   | **[必為偽]** | 款 `1` 之人造包裝物 `is` | **%s** | %s |" % (ok_f, "✅" if not ok_f else "🔴"))
    s1 = [r["sym1"] for r in allrows if r["sym1"] is not None]
    okn = bool(s1) and all(x > 0 for x in s1)
    say("   | **[必非零]** | 現行 `buf` 之對稱差 `> 0`（判定組 **%d**／%d） | %s | %s |"
        % (len(s1), len(allrows), "／".join(repr(x) for x in s1) or "（空）", "✅" if okn else "🔴"))
    s0 = [r["sym0"] for r in allrows if r["sym0"] is not None]
    okz = bool(s0) and all(x == 0.0 for x in s0)
    say("   | **[必為零]** | 範圍多邊形自比 ＝ `0`（判定組 **%d**／%d·**先自證可滿足**） | %s | %s |"
        % (len(s0), len(allrows), "／".join(repr(x) for x in s0) or "（空）", "✅" if okz else "🔴"))
    if not (ok_t and (not ok_f) and okn and okz):
        red("判別力四造未全數成立 ⇒ **判器紅、停、上呈**")

    say("")
    say("=" * W)
    say("## 總表（%s 之欄已具名·⛔ 與實測混列）" % TAG)
    say("=" * W)
    say("   | `SB` | 格 | 款 `3` 逐位對拍 | 現行 `buf` | %s `buf′` | %s `W_0′` | `S1_perp` | "
        "`\\|W_0′−S1\\|` | 跨距 | `A′` 界 | `A′` | `B′` 實測 | `B′` | 切向 `\\|cos\\|` |" % (TAG, TAG))
    say("   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in allrows:
        v3 = {True: "✅ 逐位相同", False: "🔴 相異", None: "🟡 結構上不可得"}[r["ok3"]]
        say("   | `%s` | `%s/%s` | %s | `%r` | `%r` | `%r` | `%r` | `%r` | `%r` | `%r` | %s | `%r` | %s | `%r` |"
            % (repr(r["sb"]), r["blk"], r["side"], v3, r["buf1"], r["buf2"], r["w0_new"], r["S1"],
               r["dW"], r["L"], r["A_lim"], "✅" if r["dW"] <= r["A_lim"] else "🛑",
               r["sym2"], "✅" if (r["sym2"] is not None and r["sym2"] <= 0.005) else "🛑", r["cos_a"]))
    say("")
    say("🛑 **出艙即止**：本器⛔ 判路丙成立與否、⛔ 判受領、⛔ 擬實作、⛔ 改碼一字、⛔ 開分支、")
    say("   ⛔ 動用 KL 之放行、⛔ 解除或收窄 `GB-170`、⛔ 調任何界、⛔ 呈 KL。")
    say("🔒 `rc` ＝ `%d`（`5` ＝ **量測器紅**）" % RED[0])
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9298R_gate3.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
