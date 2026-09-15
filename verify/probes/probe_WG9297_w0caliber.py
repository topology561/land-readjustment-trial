# -*- coding: utf-8 -*-
"""`W-G.9-297` `§三`：`W_0` 之**口徑釘死**（`(甲)` vs `(乙)`）與**負擔計算之實際消費者**。

🔑 **受詞**
   `(甲)` ＝ `app.py` `solve_G_binary` 內之 **`_W_near_out`**（＝ `_W_near`·本宗**近側**界線之 KL `W`）。
   `(乙)` ＝ `verify/stepg_pipeline.py` `_mp_base_W0`（**純委派** `k956_W_from_mp`）所得之 `_b_L0`／`_b_R0`。
   🛑 本器**只釘口徑並指名消費者**——⛔ 判孰是、⛔ 判 `A′` 應繫於何者（單 `§三-1`／`§六`）。

🔒 **取法 ＝ 單一 `sys.settrace`**（`co_name` 比對·**⛔ 改生產碼一字**），掛於 `P.drive(sb)` 期間：
   `solve_G_binary`  之 `return` ⇒ `(甲)`：locals `_W_near_out`／`_rw_start`／`W`／`Rw`／`S_conv`
                                    ＋ args `is_corner`／`is_chain_head`／`side_label`／`W_prev`；
   `_mp_base_W0`     之 `return` ⇒ `(乙)`：args `_gs`／`_buf`／`_dv`／`_mp`／`_adir` ＋ 回傳；
   `_advance_block_with_split` 之 `call` ⇒ **守衛之各分項**：自 `f_back` 取 `_degenerate_order`／`_N`。

🔒 **`f_locals` 之鍵須先自證存在**（`§零` 新附款·`W-G.9-296` 自捕一）：
   凡以變數名為鍵者，同格出艙 `'<名>' in f_locals`；`(乙)` 另以 `_buf` 之逐位相等為**第二鍵**，
   **二鍵並報**、不一致即 **loud**。

🔒 **母體⛔ 含本器自身之輸出**：`settrace` 僅於 `drive()` 期間掛載 ⇒ 其後之任何呼叫⛔ 入母體。
🔒 **`R(·)` 一律取 `ns["rw_from_width"]`**（⛔ 器內另算·`GB-48` 族：`W` 之定義只留一份）。

`rc`：`0` 全綠／`5` **量測器紅**（判別力三造不成立／二鍵不一致／消費處 `0`）。
🛑 `rc ≠ 0` ⛔ 等同「受詞紅」。
用法：python verify/probes/probe_WG9297_w0caliber.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import probe_WG9292_pathC as P                      # noqa: E402

W = 132
_LOG = []
RED = [0]

WATCH = ("solve_G_binary", "_mp_base_W0", "_advance_block_with_split")


def say(s=""):
    print(s)
    _LOG.append(s)


def red(s):
    RED[0] = 5
    say("🔴 **量測器紅**：" + s)


def _t(v):
    """座標／向量之安全轉元組（`repr` 全位）。"""
    if v is None:
        return None
    try:
        return tuple(float(x) for x in v)
    except Exception:                                # noqa: BLE001
        return repr(v)


def drive_traced(sb):
    JIA, YI, GUARD = [], [], []

    def _loc(frame, event, arg):
        if event != "return":
            return _loc
        cn = frame.f_code.co_name
        fl = frame.f_locals
        bk = frame.f_back
        bl = bk.f_locals if bk is not None else {}
        if cn == "solve_G_binary":
            # 🩸 **自捕（v1·`rc = 5`）**：`solve_G_binary` **⛔ 由 `_run_step_g_impl` 直接呼叫**
            #    ⇒ 其 `f_back` 無 `blk_label`（存在率 `0`／`149`）。⇒ **逐層上溯**至首個持有該名之 frame，
            #    並同格出艙其**深度**與**呼叫鏈**；另以 `side_mid` 之逐位相等為**第二鍵**（`§零` 新附款）。
            bl2, depth, chain = {}, None, []
            _f = bk
            for _i in range(1, 16):
                if _f is None:
                    break
                chain.append(_f.f_code.co_name)
                if "blk_label" in _f.f_locals:
                    bl2, depth = _f.f_locals, _i
                    break
                _f = _f.f_back
            JIA.append({
                "blk": bl2.get("blk_label"), "blk_key_exists": (depth is not None),
                "blk_depth": depth, "chain": tuple(chain),
                "side_label": fl.get("side_label"),
                "is_corner": fl.get("is_corner"), "is_chain_head": fl.get("is_chain_head"),
                "W_prev": fl.get("W_prev"),
                "_W_near_out": fl.get("_W_near_out"), "_rw_start": fl.get("_rw_start"),
                "W": fl.get("W"), "Rw": fl.get("Rw"), "S_conv": fl.get("S_conv"),
                "side_mid": _t(fl.get("side_mid")), "caller": bk.f_code.co_name if bk else None})
        elif cn == "_mp_base_W0":
            buf = fl.get("_buf")
            side = None
            for nm, tag in (("_left_buffer_S", "left"), ("_right_buffer_S", "right")):
                try:
                    if buf is not None and bl.get(nm) is not None and float(buf) == float(bl.get(nm)):
                        side = tag
                except Exception:                    # noqa: BLE001
                    pass
            YI.append({"blk": bl.get("blk_label"), "blk_key_exists": ("blk_label" in bl),
                       "side": side, "_gs": _t(fl.get("_gs")), "_buf": buf,
                       "_dv": _t(fl.get("_dv")), "_mp": _t(fl.get("_mp")),
                       "_adir": _t(fl.get("_adir")), "out": arg,
                       "caller": bk.f_code.co_name if bk else None})
        return _loc

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
                          "_commit": frame.f_locals.get("_commit"),
                          "lineno": bk.f_lineno if bk is not None else None})
            return None
        return _loc if cn in WATCH else None

    old = sys.gettrace()
    sys.settrace(_glob)
    try:
        d = P.drive(sb)
    finally:
        sys.settrace(old)
    d["JIA"], d["YI"], d["GUARD"] = JIA, YI, GUARD
    return d


def analyse(sb, d):
    ns, crp = d["ns"], d["crp"]
    R = ns["rw_from_width"]
    say("")
    say("=" * W)
    say("【`SB` ＝ %s m·態甲】**逐閘執行次數**：`solve_G_binary` **%d** 次／`_mp_base_W0` **%d** 次／"
        "`_advance_block_with_split` **%d** 次"
        % (repr(sb), len(d["JIA"]), len(d["YI"]), len(d["GUARD"])))
    say("　`_build_corner_range_v3` **%d** 次（段 **%d**）／`_corner_buffer_S` **%d** 次（段內 **%d**）／"
        "`run_step_g` 終局 ＝ %s"
        % (len(d["RNG"]), len(d["RNG"]) - d["n_rng0"], len(d["BUF"]),
           len(d["BUF"]) - d["n_buf0"], d["err"] or "（未拋）"))
    ks = sorted({r["side_label"] for r in d["JIA"]})
    say("　`solve_G_binary` 所見之 `side_label` 相異值 ＝ %r" % (ks,))
    _dep = sorted({r["blk_depth"] for r in d["JIA"]}, key=lambda x: (x is None, x))
    say("　`(甲)` 之上溯：深度相異值 ＝ %r（`None` ＝ `15` 層內查無）；命中率 ＝ `%d`／`%d`；"
        "呼叫鏈（首筆·節略 8 層）＝ %r"
        % (_dep, sum(1 for r in d["JIA"] if r["blk_depth"] is not None), len(d["JIA"]),
           (d["JIA"][0]["chain"][:8] if d["JIA"] else None)))
    say("　`f_locals` 鍵之自證（`§零` 新附款）：`blk_label` 存在率 ＝ `%d`／`%d`（甲）·`%d`／`%d`（乙）·"
        "`%d`／`%d`（守衛）；`_degenerate_order` ＝ `%d`／`%d`；`_N` ＝ `%d`／`%d`"
        % (sum(1 for r in d["JIA"] if r["blk_key_exists"]), len(d["JIA"]),
           sum(1 for r in d["YI"] if r["blk_key_exists"]), len(d["YI"]),
           sum(1 for r in d["GUARD"] if r["blk_key_exists"]), len(d["GUARD"]),
           sum(1 for r in d["GUARD"] if r["_deg_key_exists"]), len(d["GUARD"]),
           sum(1 for r in d["GUARD"] if r["_N_key_exists"]), len(d["GUARD"])))
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

        # ══ 款 4：守衛之各分項（⛔ 只報合取之結果）═══════════════════════════
        gs = [r for r in d["GUARD"] if r["blk"] == blk]
        say("  **款 `4`**　`_mp_base_W0` 之守衛 `not _degenerate_order and _N > 1` 之**各分項**")
        if not gs:
            say("      🟡 **不可得（loud）**——本街廓無 `_advance_block_with_split` 之錄")
        for g in gs:
            say("      `_degenerate_order` ＝ `%r`（鍵存在 %s）／`_N` ＝ `%r`（鍵存在 %s）／"
                "`_commit` ＝ `%r`／呼叫列 ＝ `%r`"
                % (g["_degenerate_order"], g["_deg_key_exists"], g["_N"], g["_N_key_exists"],
                   g["_commit"], g["lineno"]))
            _d, _n = g["_degenerate_order"], g["_N"]
            if _d is not None and _n is not None:
                say("      ⇒ 分項：`not _degenerate_order` ＝ **%s**／`_N > 1` ＝ **%s** ⇒ 合取 ＝ **%s**"
                    % (not _d, _n > 1, (not _d) and (_n > 1)))

        # ══ 款 1：(甲) ══════════════════════════════════════════════════════
        want = "左" if side == "left" else "右"
        sl = ((d["st"].session_state.get("f3_cad_side_lines_by_side", {}) or {})
              .get(blk, {}) or {}).get(side, {}) or {}
        sm = _t(sl.get("mid"))
        ja = [r for r in d["JIA"] if r["blk"] == blk and want in str(r["side_label"] or "")]
        ja2 = [r for r in d["JIA"] if sm is not None and r["side_mid"] == sm]   # 第二鍵
        say("  **款 `1`**　**`(甲)`** `_W_near_out`（`app.py` `solve_G_binary`）")
        say("      **二鍵並報**：鍵甲（上溯之 `blk_label`＋`side_label`）＝ **%d** 筆／"
            "鍵乙（`side_mid` 逐位相等·`%r`）＝ **%d** 筆·一致 ＝ %s"
            % (len(ja), sm, len(ja2), len(ja) == len(ja2)))
        if len(ja) != len(ja2):
            say("      🟡 **二鍵不一致（loud）**——採**交集**；上溯深度之相異值 ＝ %r"
                % sorted({r["blk_depth"] for r in d["JIA"]}, key=lambda x: (x is None, x)))
            ja = [r for r in ja if r in ja2] or ja2
        heads = [r for r in ja if r["is_corner"] or r["is_chain_head"]]
        say("      本格之 `solve_G_binary` 錄 ＝ **%d** 筆（其中鏈頭 `is_corner ∨ is_chain_head` ＝ **%d** 筆）"
            % (len(ja), len(heads)))
        jia_v = None
        if not heads:
            say("      🟡 **無鏈頭之錄（loud）**——⛔ 判其為 `0`")
        else:
            h = heads[0]
            jia_v = h["_W_near_out"]
            say("      鏈頭：`is_corner` ＝ `%r`／`is_chain_head` ＝ `%r`／`W_prev` ＝ `%r`／`side_label` ＝ `%r`"
                % (h["is_corner"], h["is_chain_head"], h["W_prev"], h["side_label"]))
            say("      **`(甲)` `_W_near_out` ＝ `%r`**；其 `_rw_start` ＝ `%r`／`W`（遠側）＝ `%r`／`Rw` ＝ `%r`"
                % (jia_v, h["_rw_start"], h["W"], h["Rw"]))
            say("      🔑 **消費之賦值鏈（逐字·`app.py` `solve_G_binary`）**：")
            say("         `_W_near = float(np.dot(_bp_w - _mp_w, _ahat))` → `_W_near_out = _W_near`")
            say("         `_rw_start = _W_near if (is_corner or is_chain_head) else float(W_prev)`")
            say("         `Rw = rw_increment(_rw_start, W)` → `Rw_pct = Rw * 100.0`")
            say("         `G_target = max(0.0, (a * (1.0 - A * B) - Rw * F * l_side …`")
            say("      ⇒ **本格之 `Rw`／`G` 實際所取者 ＝ `_rw_start` ＝ `%s`**"
                % ("`(甲)` `_W_near`（鏈頭）" if (h["is_corner"] or h["is_chain_head"])
                   else "`W_prev`（非鏈頭）"))

        # ══ 款 2：(乙) ══════════════════════════════════════════════════════
        by_lbl = [r for r in d["YI"] if r["blk"] == blk and r["side"] == side]
        say("  **款 `2`**　**`(乙)`** `_mp_base_W0` → `k956_W_from_mp`（`verify/stepg_pipeline.py`）")
        yi_v = None
        if not by_lbl:
            say("      🟡 **不可得（loud）**——本格於生產路徑**⛔ 呼叫** `_mp_base_W0`"
                "（其定義與呼叫皆在 `not _degenerate_order and _N > 1` 之分支內）·**⛔ 判為 `0`**")
        else:
            y = by_lbl[-1]
            yi_v = float(y["out"])
            by_buf = [r for r in d["YI"] if r["_buf"] is not None and r["_buf"] == y["_buf"]]
            say("      **二鍵並報**：鍵甲（`blk_label`＋側）＝ **%d**／鍵乙（`_buf` 逐位相等）＝ **%d**·一致 ＝ %s"
                % (len(by_lbl), len(by_buf), len(by_lbl) == len(by_buf)))
            if len(by_lbl) != len(by_buf):
                red("`%s/%s`：二鍵不一致 ⇒ 該格之 `(乙)` ⛔ 出艙" % (blk, side))
                yi_v = None
            else:
                say("      **`(乙)` ＝ `%r`**；實參 `_gs` ＝ `%r`／`_buf` ＝ `%r`／`_dv` ＝ `%r`／`_mp` ＝ `%r`"
                    % (yi_v, y["_gs"], y["_buf"], y["_dv"], y["_mp"]))
                say("      產生式（逐字）＝ `_bp0 = _gs + _buf·_du`；"
                    "`return float(_k956_W_from_mp(_bp0, _mp, _adir, _dv))`")

        # ══ 款 6：R(·) 與二組差 ══════════════════════════════════════════════
        rr, nr = P._pick(d["RNG"], blk, side)
        s1 = None if rr is None else float(rr["loc"].get("S1_perp"))
        say("  **款 `6`**　`R(·)`（一律取 `ns[\"rw_from_width\"]`·⛔ 器內另算）與二組差（**帶號／絕對值並列**）")
        say("      `S1_perp` ＝ `%r`（`_build_corner_range_v3` 錄 %d 筆）" % (s1, nr))
        r_j = None if jia_v is None else float(R(jia_v))
        r_y = None if yi_v is None else float(R(yi_v))
        r_s = None if s1 is None else float(R(s1))
        say("      `R((甲))` ＝ `%r`／`R((乙))` ＝ `%r`／`R(S1_perp)` ＝ `%r`" % (r_j, r_y, r_s))
        d_js = None if (r_j is None or r_s is None) else r_j - r_s
        d_ys = None if (r_y is None or r_s is None) else r_y - r_s
        say("      `R((甲)) − R(S1_perp)` ＝ 帶號 `%r`／絕對值 `%r`"
            % (d_js, None if d_js is None else abs(d_js)))
        say("      `R((乙)) − R(S1_perp)` ＝ 帶號 `%r`／絕對值 `%r`"
            % (d_ys, None if d_ys is None else abs(d_ys)))
        dv_jy = None if (jia_v is None or yi_v is None) else jia_v - yi_v
        say("      `(甲) − (乙)` ＝ 帶號 `%r`／絕對值 `%r`"
            % (dv_jy, None if dv_jy is None else abs(dv_jy)))

        rows.append({"sb": sb, "blk": blk, "side": side, "jia": jia_v, "yi": yi_v,
                     "S1": s1, "rj": r_j, "ry": r_y, "rs": r_s, "djs": d_js, "dys": d_ys,
                     "n_head": len(heads), "n_yi": len(by_lbl),
                     "consume": (heads[0]["_rw_start"] if heads else None)})
    return rows


def main():
    allrows = []
    consumers = []
    for sb in P.SBS:
        d = drive_traced(sb)
        allrows += analyse(sb, d)
        consumers += [r for r in d["JIA"] if r["_rw_start"] is not None]

    say("")
    say("=" * W)
    say("## 款 `3`　負擔計算之**實際消費者**（逐處具名 `檔:函式`·⛔ 推定）")
    say("=" * W)
    say("   | # | `檔:函式` | 賦值（逐字） | 受詞 |")
    say("   |---|---|---|---|")
    say("   | `1` | `app.py:solve_G_binary` | `_rw_start = _W_near if (is_corner or is_chain_head) "
        "else float(W_prev)` | **鏈頭取 `(甲)` `_W_near`**；非鏈頭取 `W_prev`（＝前一宗之 `W_far`） |")
    say("   | `2` | `app.py:solve_G_binary` | `Rw = rw_increment(_rw_start, W)` | `Rw` 之**唯一**產生處 |")
    say("   | `3` | `app.py:solve_G_binary` | `G_target = max(0.0, (a * (1.0 - A * B) - Rw * F * l_side …` "
        "| `G` 消費 `Rw` |")
    say("   | `4` | `verify/stepg_pipeline.py:_run_step_g_impl` | `_b_L0 = _mp_base_W0(corner_pt, "
        "_left_buffer_S, d_hat, _side_mid_left, allocation_dir_block) if _fo_left else 0.0` | "
        "**`(乙)` 之唯一消費端 ＝ `_select_pool_slot` 之 `'b'` 槽**（選槽理論·⛔ `Rw`／`G` 之鏈） |")
    say("   | `5` | `verify/stepg_pipeline.py:_run_step_g_impl` | `_slot_res = _select_pool_slot(…, "
        "{'has': …, 'F': …, 'l1': …, 'b': _b_L0}, …)` | 同上 |")
    say("   ⇒ **消費處數 ＝ `5`**（`(甲)` 之鏈 `3` 處／`(乙)` 之鏈 `2` 處）·`solve_G_binary` 之 `_rw_start`"
        " 實際賦值次數（全情境）＝ **%d**" % len(consumers))

    say("")
    say("=" * W)
    say("## 款 `7`　判別力三造之判")
    say("=" * W)
    n = len(allrows)
    say("   | 造 | 判準 | 實測 | 判 |")
    say("   |---|---|---|---|")
    say("   | （母體） | `forced` 格數 `≥ 1` | **%d** | %s |" % (n, "✅" if n >= 1 else "🔴"))
    pair = [r for r in allrows if r["jia"] is not None and r["yi"] is not None]
    if not pair:
        ok1 = False
        v1 = "🟡 **不可判（loud）**——判定組為空（無一格二者皆可得）·⛔ 以「全數成立」充綠"
    else:
        ok1 = any(r["jia"] != r["yi"] for r in pair)
        v1 = "%s ⇒ %s（判定組 **%d**／%d 格）" % (
            "／".join("%r vs %r" % (r["jia"], r["yi"]) for r in pair),
            "✅ 至少一格相異" if ok1 else "🔴 全同", len(pair), n)
    say("   | **[必相異]** | `(甲)` 與 `(乙)` 於至少一格須相異（證二者⛔ 同物） | %s | %s |"
        % (v1, "✅" if ok1 else "🔴"))
    ok2 = len(consumers) >= 1
    say("   | **[必非零]** | 款 `3` 之消費處數 `≥ 1` | 消費處 `5` 處·`_rw_start` 賦值 **%d** 次 | %s |"
        % (len(consumers), "✅" if ok2 else "🔴"))
    zs = [r["jia"] - r["jia"] for r in allrows if r["jia"] is not None]
    ok3 = bool(zs) and all(x == 0.0 for x in zs)
    say("   | **[必為零]** | 同一量自比之差 ＝ `0`（**先自證可滿足**） | %s（判定組 **%d**） | %s |"
        % ("／".join(repr(x) for x in zs) or "（空）", len(zs), "✅" if ok3 else "🔴"))
    if not (n >= 1 and ok1 and ok2 and ok3):
        red("判別力三造未全數成立 ⇒ **判器紅、停、上呈**")

    say("")
    say("=" * W)
    say("## 總表")
    say("=" * W)
    say("   | `SB` | 格 | **`(甲)`** `_W_near_out` | **`(乙)`** `_b_L0` | `S1_perp` | `R((甲))` | `R((乙))` | "
        "`R(S1_perp)` | `R((甲))−R(S1)` | `R((乙))−R(S1)` |")
    say("   |---|---|---|---|---|---|---|---|---|---|")
    for r in allrows:
        f = lambda x: "🟡 不可得" if x is None else "`%r`" % x          # noqa: E731
        say("   | `%s` | `%s/%s` | %s | %s | %s | %s | %s | %s | %s | %s |"
            % (repr(r["sb"]), r["blk"], r["side"], f(r["jia"]), f(r["yi"]), f(r["S1"]),
               f(r["rj"]), f(r["ry"]), f(r["rs"]), f(r["djs"]), f(r["dys"])))
    say("")
    say("🛑 **出艙即止**：本器⛔ 判 `A′` 應繫於何者、⛔ 判路丙成立與否、⛔ 判前批呈 KL 之數孰是、")
    say("   ⛔ 擬實作、⛔ 改碼一字、⛔ 開分支、⛔ 動用 KL 之放行、⛔ 解除或收窄 `GB-170`、⛔ 呈 KL。")
    say("🔒 `rc` ＝ `%d`（`5` ＝ **量測器紅**）" % RED[0])
    say("=" * W)

    out = os.path.join(REPO, "verify", "out", "WG9297R_w0caliber.log")
    with open(out, "w", encoding="utf-8", newline="\n") as f2:
        f2.write("\n".join(_LOG) + "\n")
    print("\n落檔 ⇒ %s" % out)
    return RED[0]


if __name__ == "__main__":
    sys.exit(main())
