# -*- coding: utf-8 -*-
r"""`W-G.9-319` `§二-1` 階段 `a`：**二寬度之量差**（觀測·⛔ 替身·忠實）。

受詞（逐宗）：`_宗地寬度`（未捨入）／`W`（未捨入）／`R(_宗地寬度)`／`R(W)`／
`R(W) − R(_宗地寬度)`／`_宗地寬度 ÷ W`。

母體：二態（甲 ＝ `WV_K6_STEP0` 未設·**現行預設**／乙 ＝ `=off`）× 二情境（`0m`／`3.5m`）。
🩸 態乙之管線於 `R4` 後中止（`GB-168`）⇒ 母體必小於態甲；**該相異具名·⛔ 判二態可比**（`恆常附款 o`）。

🛑 **⛔ 判孰為 `K-9-41 ②` 所指之寬度、⛔ 判二軸孰為正典、⛔ 提修法主張**——出艙即止。
🔒 **取法（`§零-5`·⛔ 器內另算第二份）**：`R(·)` ＝ `ns["rw_from_width"]`；
   `widths` ＝ 間諜錄 `ns["_select_pool_slot"]` 之實參（沿 `probe_WG9277_width.py`）；
   `W` ＝ **碼面 `g_row` 之 `W(m)` 欄**（所擇者具名於出艙·⛔ 與 `k956_W_from_mp` 混用）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9319_widths.py [--keys]`
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 128


def drive(sb, mode):
    """mode ＝ None（態甲·現行預設）／'off'（態乙）。"""
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline", "stepg_pipeline"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    slots, solved = [], []
    _o = ns["_select_pool_slot"]

    def _peek(depth, keys):
        f = sys._getframe(depth + 1).f_locals
        return {k: f.get(k) for k in keys}

    def _spy(widths, left, right):
        out = _o(widths, left, right)
        p = _peek(1, ["blk_label"])
        slots.append({"blk": p.get("blk_label"), "widths": list(widths or [])})
        return out
    ns["_select_pool_slot"] = _spy

    # 🔒 `_res` 之取值點 ＝ `ns["_solve_G_one"]` 之**回傳**（`stepg_pipeline.py:517` 之受委派者）
    #    ——其 `W` 為**未捨入**；其 `_宗地寬度` 於**賦值處**即 `round(·, 2)`（`app.py:22036`）。
    _sg1 = ns["_solve_G_one"]

    def _spy_solve(*a, **kw):
        out = _sg1(*a, **kw)
        # 🩸 **自捕**：`_solve_G_one` 之回傳係 **`(res, solver_label)` 之 tuple**
        #    （`stepg_pipeline.py:823` 逐字 `res, solver_label = _solve_one(...)`），
        #    ⛔ dict。首版之 `isinstance(res, dict)` 恆偽 ⇒ 錄得 `0` 筆。
        #    **對齊自證閘於此時報 `0`／`56` 而非靜默出錯** ⇒ 該閘生效一次。
        res = out[0] if isinstance(out, tuple) and out and isinstance(out[0], dict) else out
        # 🩸 **自捕二**：`_宗地寬度` 係於 `_solve_G_one` **回傳之後**才被寫入**同一 dict**
        #    （`verify/stepg_pipeline.py:737` 逐字 `_res['_宗地寬度'] = round(_pw, 2)`）
        #    ⇒ 當下取值恆得 `None`。改**存參照**，於出艙時方讀 ⇒ 讀得其終值。
        if isinstance(res, dict):
            solved.append(res)
        return out
    ns["_solve_G_one"] = _spy_solve

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
    err, g_rows = None, []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:200]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    return {"ns": ns, "slots": slots, "solved": solved, "g_rows": g_rows,
            "err": err, "forced": forced}


def align(g_rows, solved):
    """把 `_solve_G_one` 之回傳逐列對齊 `g_rows`。

    🔒 **自證閘**（探針還原內部量之必設閘）：對齊之唯一判準 ＝
       `round(spy['W'], 2) == g_row['W(m)']` **且** `round(spy['G'], 2) == g_row['G(㎡)']`。
       ⇒ 全列命中方採信；未命中者逐列具名，⛔ 以近似或順序充之。
    """
    out, j, skipped = [], 0, 0
    for row in g_rows:
        w2, g2 = row.get("W(m)"), row.get("G(㎡)")
        hit = None
        k = j
        while k < len(solved):
            s = solved[k]
            if (s.get("W") is not None and s.get("G") is not None
                    and round(float(s["W"]), 2) == w2
                    and round(float(s["G"]), 2) == g2):
                hit = s
                skipped += k - j
                j = k + 1
                break
            k += 1
        out.append(hit)
    return out, skipped


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    keys_only = "--keys" in sys.argv
    print("=" * W)
    print("【`W-G.9-319` `§二-1` 階段 `a`】二寬度之量差（**觀測·忠實·⛔ 替身**）")
    print("=" * W)
    print("🛑 ⛔ 判孰為 `K-9-41 ②` 所指之寬度、⛔ 判二軸孰為正典、⛔ 提修法主張——出艙即止。")

    CASES = [("甲", None, 0.0), ("甲", None, 3.5), ("乙", "off", 0.0), ("乙", "off", 3.5)]
    store = {}
    for tag, mode, sb in CASES:
        r = drive(sb, mode)
        store[(tag, sb)] = r
        if keys_only and r["g_rows"]:
            print("\n── `g_rows` 之鍵（態%s·%.1fm·第 `1` 列）──" % (tag, sb))
            for k in sorted(r["g_rows"][0].keys()):
                print("   %-28s = %r" % (k, r["g_rows"][0][k]))
            return
        print("\n" + "─" * W)
        print("【態%s（`%s`）·退縮 `%.1f` m】母體 ＝ `g_rows` **`%d`** 列／`_select_pool_slot` 呼叫 **`%d`** 次"
              % (tag, "未設·現行預設" if mode is None else ENV + "=off", sb,
                 len(r["g_rows"]), len(r["slots"])))
        if r["err"]:
            print("🩸 **管線中止**（逐字）：%s" % r["err"])
        blks = []
        for row in r["g_rows"]:
            b = row.get("所屬街廓")
            if b not in blks:
                blks.append(b)
        print("   可達街廓（出現序）＝ %s" % blks)

    # ── 逐宗出艙 ──
    RW = None
    for (tag, sb), r in store.items():
        if RW is None:
            RW = r["ns"]["rw_from_width"]
    print("\n" + "=" * W)
    print("【逐宗之六量】`R(·)` ＝ `ns[\"rw_from_width\"]`（⛔ 器內另算第二份）")
    print("=" * W)
    print("🔒 **所擇之 `W`（`§二-1` 令二者擇一並具名）** ＝ **碼面 `_res['W']` 之未捨入值**")
    print("   （取值點 ＝ `ns[\"_solve_G_one\"]` 之回傳·即 `stepg_pipeline.py:492` 所 `round` 之同一物）；")
    print("   **⛔ 與 `k956_W_from_mp` 混用**。")
    print("🔴 **`_宗地寬度` 之「未捨入」於碼面<u>結構上不存在</u>**——其**賦值處**即")
    print("   `_res['_宗地寬度'] = round(_pw, 2)`（`app.py:22036`／`verify/stepg_pipeline.py:737`）")
    print("   ⇒ 本表該欄之值即**碼面之值**（`2dp`），⛔ 以任何外算之 `S × |cos|` 充其未捨入值"
          "（`§零-5`：⛔ 器內另算第二份）。")
    summary = {}
    for tag, mode, sb in CASES:
        r = store[(tag, sb)]
        rows = r["g_rows"]
        pair, skipped = align(rows, r["solved"])
        nhit = sum(1 for p in pair if p is not None)
        print("\n" + "─" * W)
        print("【態%s·`%.1f` m】`g_rows` `%d` 列／`_solve_G_one` 回傳 `%d` 次"
              % (tag, sb, len(rows), len(r["solved"])))
        print("🔒 **對齊自證閘**（判準 ＝ `round(W,2)` ⋀ `round(G,2)` 皆相符）："
              "命中 **`%d`／`%d`**（跳過 `%d` 次非列之回傳）%s"
              % (nhit, len(rows), skipped, "🟢" if nhit == len(rows) else "🔴 **⛔ 採信未命中列**"))
        print("─" * W)
        print("%-5s %-14s %13s %15s %14s %14s %14s %10s"
              % ("街廓", "宗名", "宗地寬度(2dp)", "W(未捨入)", "R(宗地寬度)", "R(W)", "R(W)-R(寬)", "寬÷W"))
        acc, accabs, n = 0.0, 0.0, 0
        for x, s in zip(rows, pair):
            nm = x.get("暫編地號") or x.get("原地號") or "?"
            if s is None:
                print("%-5s %-14s  🩸 **對齊未命中** ⇒ 本列⛔ 出艙其未捨入 `W`"
                      % (x.get("所屬街廓"), str(nm)[:14]))
                continue
            w1, w2 = num(s.get("_宗地寬度")), num(s.get("W"))
            if w1 is None or w2 is None:
                print("%-5s %-14s  🩸 二量非數：寬=%r／W=%r"
                      % (x.get("所屬街廓"), str(nm)[:14], s.get("_宗地寬度"), s.get("W")))
                continue
            r1, r2 = RW(w1), RW(w2)
            d = r2 - r1
            acc += d
            accabs += abs(d)
            n += 1
            print("%-5s %-14s %13.2f %15.10f %14.6f %14.6f %+14.6f %10s"
                  % (x.get("所屬街廓"), str(nm)[:14], w1, w2, r1, r2, d,
                     ("%.6f" % (w1 / w2)) if w2 else "—"))
        print("  🔒 出艙 `%d` 宗｜`Σ(R(W)−R(寬))`（**帶號**）＝ **%+0.6f**／"
              "`Σ|·|`（**絕對值**）＝ **%0.6f**" % (n, acc, accabs))
        summary[(tag, sb)] = (len(rows), n, acc, accabs, nhit)

    # ── 自我驗證閘（二造·須異色）──
    print("\n" + "=" * W)
    print("【自我驗證閘】二造·須異色")
    print("=" * W)
    r = store[("乙", 0.0)]
    tgt = [x for x in r["g_rows"]
           if x.get("所屬街廓") == "R4" and "628-1(1)" in str(
               x.get("地號") or x.get("暫編地號") or "")]
    print("[必相符] `0m` 態乙 `R4` 之 `628-1(1)`（`GB` 簿 `:7359`–`:7360` 逐字："
          "`宗地寬度(m)` `14.01` ⇒ `R` `87.835000`；`W(m)` `14.20` ⇒ `R` `88.500000`）")
    if not tgt:
        print("   🩸 **該宗於本次實跑之 `g_rows` 內⛔ 可得** ⇒ 逐項具名其成因（⛔ 以空集充相符）")
        for x in r["g_rows"]:
            if x.get("所屬街廓") == "R4":
                print("      · `R4` 之列：%s" % (x.get("地號") or x.get("暫編地號")))
    else:
        x = tgt[0]
        w1, w2 = num(x.get("宗地寬度(m)")), num(x.get("W(m)"))
        print("   實得：`宗地寬度(m)` ＝ %r ⇒ `R` ＝ %.6f｜`W(m)` ＝ %r ⇒ `R` ＝ %.6f"
              % (x.get("宗地寬度(m)"), RW(w1), x.get("W(m)"), RW(w2)))
        ok = (round(w1, 2) == 14.01 and round(w2, 2) == 14.20
              and abs(RW(w1) - 87.835) < 5e-7 and abs(RW(w2) - 88.5) < 5e-7)
        print("   ⇒ **逐位相符（`2dp` 顯示層）：%s** %s" % (ok, "🟢" if ok else "🔴 **停一**"))
    z = RW(14.20) - RW(14.20)
    print("[必為零] 任一宗之 `R(W) − R(W)` ＝ **%.10f**（須 `0.0000000000`）%s"
          % (z, "🟢" if z == 0.0 else "🔴"))

    # ── 母體之可比性（恆常附款 o）──
    print("\n" + "=" * W)
    print("【母體與可比性判】（`恆常附款 o`）")
    print("=" * W)
    print("%-12s %9s %9s %9s %16s %16s"
          % ("態·情境", "g_rows", "對齊命中", "出艙宗", "Σ帶號", "Σ絕對值"))
    for k in [("甲", 0.0), ("乙", 0.0), ("甲", 3.5), ("乙", 3.5)]:
        n, h, a, b, hit = summary[k]
        print("%-12s %9d %9d %9d %+16.6f %16.6f" % ("態%s·%.1fm" % k, n, hit, h, a, b))
    for sb in (0.0, 3.5):
        na, nb = summary[("甲", sb)][0], summary[("乙", sb)][0]
        print("  `%.1fm`：態甲 `%d` 列 vs 態乙 `%d` 列 ⇒ 母體%s ⇒ **%s**"
              % (sb, na, nb, "相同" if na == nb else "**相異**",
                 "🟢 可比" if na == nb else "🛑 **⛔ 可比**（其差⛔ 出艙為後果·僅得為附帶量）"))


if __name__ == "__main__":
    main()
