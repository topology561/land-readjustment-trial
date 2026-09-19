# -*- coding: utf-8 -*-
"""`W-G.9-318 補令一` `§三`（工項二）：`_b_*0` 與鏈頭 `W_0` 之**對帳**（唯讀·一次·⛔ 全量）。

🛑 **唯讀**——⛔ 改任何生產碼一字、⛔ 寫 `verify/baselines`、⛔ 設 `WV_BAKE`、⛔ 施替身
   （三 spy 一律**原樣回傳**上游之回傳值·⛔ 改其實參）。⛔ 匯入即驅動。

🔒 **受詞（補令 `§三` 逐字）**：`0m`／`3.5m` **態甲** `R4 left` ——
   ① `_b_L0`（未捨入）／② 改前之鏈頭 `W_0`（`_W_near`·未捨入）／
   ③ `W(遠側)`（以 `ns["k956_W_from_mp"]` 取）／④ `R(①) − R(②)`／⑤ `R(②) − R(③)`。

🔒 **取法（⛔ 器內另算·一律取碼面之同一物）**
   · ① ＝ `_mp_base_W0` 之回傳 —— 以 `ns["k956_W_from_mp"]` 之 spy 取其**最末一次**回傳值，
     且僅採**其直接呼叫端之 `co_name == '_mp_base_W0'`** 者（⇒ 其回傳即 `_b_L0`／`_b_R0`）。
   · ② ＝ `rw_increment` 之**第一實參** `W_prev`（＝ `_rw_start`）於**鏈頭**之呼叫
     （鏈頭判準 ＝ 碼面同一運算式 `is_corner or is_chain_head`·自呼叫端之區域名取值）。
     🔒 本器跑於 `c7′` 之態（forced 側傳 `None` ⇒ 覆寫**不觸發**）⇒ 該值即**改前之值**。
   · ③ ＝ `probe_WG9279_rw0.py` `§四-2` 之**逐字**構造（⛔ 另寫第二份判準）：
     `far_pt = corner_pt + buf · d̂_單位`，再 `ns["k956_W_from_mp"](far_pt, mp, alloc, d_hat)`——
     🔑 其 `mp`／`alloc`／`d_hat`／`corner_pt` **一律取自<u>鏈頭那一筆</u> `solve_G_binary` 之實參**
     （⛔ 取 `_mp_base_W0` 之實參）。🩸 **本器首版誤取後者** ⇒ `③` 差 `0.77`、判別力甲不過
     ⇒ **器紅**（CC 自捕）。**二者之別 ＝ 量測軸**：`_mp_base_W0` 用**街廓軸**
     `allocation_dir_block`；鏈頭用 `K-9-5-4 ②` 之**換軸** `_first_corner_alloc_dir(side_mid)`。
   · `R(·)` 一律 `ns["rw_from_width"]`。

🔒 **自我驗證閘（碼面自身之保證·⛔ 不過不得據以下任何結論）**
   `(i)` 凡 `_select_pool_slot` 被呼叫之街廓，其實參 `left['b']`／`right['b']` 須與本器
        自 `_mp_base_W0` spy 所捕之 ①**逐位相符**（`_fo_*` 為 `False` 之側其 `b` ＝ `0.0`·⛔ 呼叫）。
   `(ii)` 承 `probe_WG9279_rw0.py` 之同一閘：以
        `ns["k956_W_from_mp"](baseline_pt, mp, alloc, d_hat)`（實參皆取鏈頭那一筆）
        重建之 `W` 須與碼面之 `W_0`（＝ ②）**逐位相符**。

🛑 **⛔ 解除、⛔ 收窄 `GB-170`；⛔ 判孰誤。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9318p_bl0_recon.py [<倉根>]`
`rc`：`0` 正常／`5` **器紅**（自我驗證閘或判別力不成立）。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
SBS = (0.0, 3.5)
W = 126
NA = "【⛔ 可得】"
FOCUS = ("R4", "left")

# 🔒 外部錨（**【倉】**·⛔ 器內重算）
GB170 = {"0m": 4.955250038496402, "3.5m": 4.265999999999998}          # R(W_0) − R(S1_perp)
GB170_S1PERP = {"0m": 3.6954999940774775}                              # 款 6 之逐字（僅 0m 載）
GB169 = {("0m", "R4", "left"): (4.4997522400, 4.4804447558, 4.4804447558),
         ("3.5m", "R4", "left"): (7.8185635189, 7.7850157181, 7.7850157181)}  # buf／W(遠側)／W_0


def say(s=""):
    print(s)


def _norm_side(s):
    if s is None:
        return None
    t = str(s)
    if "左" in t or t.lower().startswith("l"):
        return "left"
    if "右" in t or t.lower().startswith("r"):
        return "right"
    return None


def _climb(names, upto=20):
    out = {k: None for k in names}
    seen = {k: False for k in names}
    for d in range(1, upto + 1):
        try:
            f = sys._getframe(d + 1)
        except ValueError:
            break
        for k in names:
            if not seen[k] and k in f.f_locals:
                out[k] = f.f_locals[k]
                seen[k] = True
    return out, seen


def drive(sb):
    """一情境一次驅動（**態甲** ＝ `WV_K6_STEP0` 未設）。"""
    os.environ.pop(ENV, None)
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    _o_k956 = ns["k956_W_from_mp"]
    _o_rwi = ns["rw_increment"]
    _o_slot = ns["_select_pool_slot"]
    R = ns["rw_from_width"]
    npmod = ns["np"]

    mp_calls = {}          # (blk, which) -> dict
    heads = {}             # (blk, side) -> W_prev（鏈頭·未捨入）
    head_kw = {}           # (blk, side) -> 鏈頭那一筆 solve_G_binary 之實參
    slots = []
    _o_sgb = ns["solve_G_binary"]

    def _spy_sgb(*a, **kw):
        out = _o_sgb(*a, **kw)
        if bool(kw.get("is_corner")) or bool(kw.get("is_chain_head")):
            p, _ = _climb(["blk_label", "side", "corner_pt"])
            b, sd = p.get("blk_label"), _norm_side(p.get("side"))
            if b is not None and sd is not None:
                head_kw[(b, sd)] = {
                    "baseline_pt": kw.get("baseline_pt"), "mp": kw.get("side_mid"),
                    "alloc": kw.get("allocation_dir"), "d_hat": kw.get("d_hat"),
                    "corner_pt": p.get("corner_pt"),
                }
        return out

    def _spy_k956(*a, **kw):
        out = _o_k956(*a, **kw)
        try:
            caller = sys._getframe(1).f_code.co_name
        except ValueError:
            caller = None
        if caller == "_mp_base_W0":
            p, _ = _climb(["blk_label", "_gs", "_buf", "_dv", "_mp", "_adir",
                           "corner_pt", "_end_pt_o", "_side_mid_left", "_side_mid_right",
                           "allocation_dir_block", "d_hat",
                           "_left_buffer_S", "_right_buffer_S", "_fo_left", "_fo_right"])
            gs = p.get("_gs")
            cp = p.get("corner_pt")
            which = "L" if (cp is not None and gs is not None
                            and float(npmod.linalg.norm(npmod.asarray(gs, dtype=float)
                                                        - npmod.asarray(cp, dtype=float))) < 1e-12) else "R"
            mp_calls[(p.get("blk_label"), which)] = {
                "ret": float(out), "buf": p.get("_buf"),
                "gs": gs, "mp": p.get("_mp"), "adir": p.get("_adir"), "dv": p.get("_dv"),
                "left_buffer_S": p.get("_left_buffer_S"),
                "right_buffer_S": p.get("_right_buffer_S"),
                "fo_left": p.get("_fo_left"), "fo_right": p.get("_fo_right"),
            }
        return out

    def _spy_rwi(W_prev, W_cur):
        out = _o_rwi(W_prev, W_cur)
        p, _ = _climb(["is_corner", "is_chain_head", "blk_label", "side"])
        if bool(p.get("is_corner")) or bool(p.get("is_chain_head")):
            b, sd = p.get("blk_label"), _norm_side(p.get("side"))
            if b is not None and sd is not None:
                heads[(b, sd)] = float(W_prev)
        return out

    def _spy_slot(widths, left, right):
        out = _o_slot(widths, left, right)
        p, _ = _climb(["blk_label"])
        slots.append({"blk": p.get("blk_label"),
                      "bL": (left or {}).get("b"), "bR": (right or {}).get("b")})
        return out

    ns["k956_W_from_mp"] = _spy_k956
    ns["rw_increment"] = _spy_rwi
    ns["_select_pool_slot"] = _spy_slot
    ns["solve_G_binary"] = _spy_sgb

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _off, wins, forced = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
    err = None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, build_p,
                       wins, forced, sb, eff_min_build_by_blk={})
    except RuntimeError as e:
        err = str(e).split("\n")[0]
    return {"mp": mp_calls, "heads": heads, "head_kw": head_kw, "slots": slots, "err": err,
            "R": R, "K": _o_k956, "np": npmod, "forced": forced or {}}


def main():
    say("=" * W)
    say("【`W-G.9-318 補令一` `§三`】`_b_*0` 與鏈頭 `W_0` 之對帳（唯讀·態甲·⛔ 全量）")
    say("=" * W)
    say("\U0001f6d1 **唯讀**：⛔ 改生產碼一字·⛔ 替身·⛔ 反事實；三 spy 逐位原樣回傳")
    say("\U0001f512 本器跑於 `c7′` 之態（forced 側傳 `None` ⇒ 覆寫**不觸發**）⇒ ② 即**改前之值**")
    say("\U0001f512 `R(·)` 一律 `ns[\"rw_from_width\"]`；`W(·)` 一律 `ns[\"k956_W_from_mp\"]`（⛔ 器內另算）")
    say("")

    rc = 0
    for sb in SBS:
        tag = "%gm" % sb
        d = drive(sb)
        R, K, npm = d["R"], d["K"], d["np"]
        say("─" * W)
        say("▍情境 %s ｜ 態甲（`%s` 未設）｜中止閘 ＝ %s" % (tag, ENV, d["err"] or "（無·跑完）"))
        say("─" * W)

        # ── 自我驗證閘 (i) ───────────────────────────────────────────
        say("🔒 **自我驗證閘 `(i)`**（碼面自身之保證：`_select_pool_slot` 之實參 `b` ＝ 本器所捕之 ①）")
        g1 = True
        for s in d["slots"]:
            b = s["blk"]
            for which, key in (("L", "bL"), ("R", "bR")):
                got = s[key]
                cap = d["mp"].get((b, which))
                exp = cap["ret"] if cap else 0.0
                ok = (got is not None and abs(float(got) - float(exp)) < 1e-12)
                g1 = g1 and ok
                if not ok:
                    say("   🔴 %s·%s：slot 實參 %r ≠ 本器所捕 %r" % (b, which, got, exp))
        say("   ⇒ 逐格相符 ＝ **%s**（受檢 %d 街廓 × 2 側）" % (g1, len(d["slots"])))
        if not g1:
            rc = 5

        # ── 受詞 R4 left ────────────────────────────────────────────
        cap = d["mp"].get(("R4", "L"))
        head = d["heads"].get(FOCUS)
        say("")
        if cap is None:
            say("① `_b_L0`（`R4` left）＝ %s —— 其由 ＝ `_fo_left` 為 `False` ⇒ `_mp_base_W0` ⛔ 被呼叫" % NA)
            continue
        one = cap["ret"]
        two = head
        hk = d["head_kw"].get(FOCUS) or {}
        # ── 🔒 自我驗證閘 (ii)（承 `probe_WG9279_rw0.py` 之同一閘）──────────
        g2 = None
        if all(hk.get(k) is not None for k in ("baseline_pt", "mp", "alloc", "d_hat")) and two is not None:
            wr = float(K(hk["baseline_pt"], hk["mp"], hk["alloc"], hk["d_hat"]))
            g2 = ("%.10f" % wr) == ("%.10f" % two)
            say("🔒 **自我驗證閘 `(ii)`**：以鏈頭實參重建之 `W` ＝ `%.10f`／碼面 `W_0` ＝ `%.10f` ⇒ %s"
                % (wr, two, "✅ 逐位相符" if g2 else "🔴 **⛔ 相符**"))
        else:
            say("🔒 **自我驗證閘 `(ii)`** ⇒ %s（鏈頭實參不全）" % NA)
        if g2 is not True:
            say("🛑 **閘 `(ii)` 不過 ⇒ loud 拒測**——⛔ 據 ③／⑤ 下任何結論。")
            rc = 5
        far = None
        # 🩸 ⛔ 用 `None not in (...)`——numpy 陣列之 `in` 走逐元素比較 ⇒ `ValueError`（CC 自捕）
        # 🔑 實參一律取**鏈頭那一筆**（⛔ `_mp_base_W0` 之實參·首版之誤）
        if g2 is True and all(hk.get(k) is not None for k in ("corner_pt", "mp", "alloc", "d_hat")) \
                and cap["buf"] is not None:
            dv = npm.asarray(hk["d_hat"], dtype=float)
            dn = float(npm.linalg.norm(dv))
            du = dv / dn if dn > 1e-9 else dv
            far_pt = npm.asarray(hk["corner_pt"], dtype=float) + float(cap["buf"]) * du
            far = float(K(far_pt, hk["mp"], hk["alloc"], hk["d_hat"]))
        say("**五量（`R4` left·未捨入）**")
        say("| # | 量 | 值 | `R(·)` (%) |")
        say("|---|---|---|---|")
        say("| ① | `_b_L0`（`_mp_base_W0` 之回傳） | `%.10f` | `%.10f` |" % (one, R(one)))
        say("| ② | 改前之鏈頭 `W_0`（`_W_near`·`rw_increment` 之 `W_prev`） | %s | %s |"
            % (("`%.10f`" % two) if two is not None else NA,
               ("`%.10f`" % R(two)) if two is not None else NA))
        say("| ③ | `W(遠側)`（`corner_pt + buf·d̂` → `k956_W_from_mp`·`probe_WG9279:282` 逐字） | %s | %s |"
            % (("`%.10f`" % far) if far is not None else NA,
               ("`%.10f`" % R(far)) if far is not None else NA))
        say("")
        say("　併記（生產實參）：`_left_buffer_S` ＝ `%.10f`／`_fo_left` ＝ `%s`"
            % (float(cap["left_buffer_S"]) if cap["left_buffer_S"] is not None else float("nan"),
               cap["fo_left"]))
        # 🔑 二軸之別（①／③ 之唯一相異源·⛔ 判孰誤）
        if cap.get("adir") is not None and hk.get("alloc") is not None:
            a1 = npm.asarray(cap["adir"], dtype=float)
            a2 = npm.asarray(hk["alloc"], dtype=float)
            n1 = float(npm.linalg.norm(a1))
            n2 = float(npm.linalg.norm(a2))
            cs = abs(float(npm.dot(a1 / n1, a2 / n2))) if n1 > 1e-9 and n2 > 1e-9 else float("nan")
            say("　🔑 **二軸之別**：① 之量測軸 ＝ `_mp_base_W0` 之 `_adir`（＝ `allocation_dir_block`）"
                "／②③ 之量測軸 ＝ 鏈頭之 `allocation_dir`（`K-9-5-4 ②` 之換軸）"
                "⇒ `|cos|` ＝ `%.10f`（⛔ 判孰誤）" % cs)
        gb = GB169.get((tag, "R4", "left"))
        if gb:
            say("　對拍 `GB-169 §三`【倉】：`buf` `%.10f`／`W(遠側)` `%.10f`／`W_0`（碼面）`%.10f`"
                % gb)
            say("　　· 本器之 `_left_buffer_S` vs 其 `buf` ⇒ Δ ＝ `%+.3e`"
                % (float(cap["left_buffer_S"]) - gb[0]))
            if far is not None:
                say("　　· 本器之 ③ vs 其 `W(遠側)` ⇒ Δ ＝ `%+.3e`" % (far - gb[1]))
            if two is not None:
                say("　　· 本器之 ② vs 其 `W_0`（碼面） ⇒ Δ ＝ `%+.3e`" % (two - gb[2]))
        if two is not None:
            four = R(one) - R(two)
            say("")
            say("| ④ | `R(①) − R(②)` | **`%.10f`** 個百分點 |" % four)
            five = None
            if far is not None:
                five = R(two) - R(far)
                say("| ⑤ | `R(②) − R(③)` | **`%.10f`** 個百分點 |" % five)
            else:
                say("| ⑤ | `R(②) − R(③)` | %s（閘 (ii) 不過或實參不全） |" % NA)
            say("")
            say("🔒 **判（補令 `§三`）**：④ 與 `GB-170` 之 `R(W_0) − R(S1_perp)`（【倉】 `%.15f`）" % GB170[tag])
            say("   ⇒ |④| ＝ `%.10f`／倉載 ＝ `%.10f`／**Δ ＝ `%+.10f`**"
                % (abs(four), GB170[tag], abs(four) - GB170[tag]))
            say("   ⇒ **%s** ——⛔ 判孰誤（單 `§三` 明令）"
                % ("逐位相符 ⇒ 同一量" if abs(abs(four) - GB170[tag]) < 1e-9
                   else "⛔ 逐位相符 ⇒ 具名其差如上"))
            say("")
            say("🔒 **判別力二造**")
            if five is None:
                say("   甲[必為零] ⑤ ⇒ %s ⇒ 🛑 **無從判**（⛔ 等同判為偽）" % NA)
            else:
                say("   甲[必為零] ⑤（依 `GB-169 §三` 應 ＝ `0`）⇒ 實得 `%.10f` ⇒ %s"
                    % (five, "✅ 為零" if abs(five) < 1e-9 else "🔴 **非零**"))
            say("   乙[必非零] ④ ⇒ 實得 `%.10f` ⇒ %s"
                % (four, "✅ 非零" if abs(four) > 1e-9 else "🔴 **為零**"))
            same = None if five is None else ((abs(five) < 1e-9) == (abs(four) < 1e-9))
            say("   ⇒ 二造**%s** ⇒ %s" % ("無從判" if same is None else ("同色" if same else "異色"),
                                        "🛑 拒測" if same is None else ("🔴 **器紅**" if same else "✅ 器非紅")))
            if same is not False:
                rc = 5
        say("")
    return rc


if __name__ == "__main__":
    sys.exit(main())
