# -*- coding: utf-8 -*-
r"""`W-G.9-319` `§三` 工項二：`GB-170` 三釘紅格於**現態**之現查（唯讀）。

受詞 ＝ `GB` 簿 `:7773`–`:7775` 之三格——`R4/left@0.0m`（`range_area` `116.08`）／
`R2/left@3.5m`（`308.17`）／`R4/left@3.5m`（`226.01`）——於開工態是否**仍為強制抵費地**。

🛑 **⛔ 判本工項對 `GB-170` 失效條件之影響、⛔ 解除、⛔ 收窄、⛔ 提修法主張**——**出艙即止**。
🛑 **停四**：三格中任一格於二態皆不可得（管線未達）⇒ **loud 具名「結構上不可得」及其分項成因**，
   ⛔ 以空集充「已不存在」（`恆常附款 j`／`GB-132` 族之空集假綠）。
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
W = 124
CELLS = [("R4", "left", 0.0, "116.08"), ("R2", "left", 3.5, "308.17"),
         ("R4", "left", 3.5, "226.01")]


def drive(sb, mode):
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
        err = str(e).split("\n")[0][:190]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    return {"forced": forced, "wins": wins, "g_rows": g_rows, "err": err}


def fval(forced, blk, side):
    """自 `forced_map` 取該街廓該側之 `forced` 旗標。

    🩸 **自捕**：其鍵逐字為 `<side>_forced_offset`（**當場出艙其形**·⛔ 推定）；
       首版以 `side` 為鍵 ⇒ 回傳整個 dict，致判別力二造皆讀為「相異」。
    """
    if not isinstance(forced, dict):
        return "⛔ 非 dict：%r" % type(forced)
    d = forced.get(blk)
    if not isinstance(d, dict):
        return "【⛔ 可得·`%s` ⛔ 在 forced_map 內】" % blk
    k = "%s_forced_offset" % side
    if k not in d:
        return "【⛔ 可得·鍵 `%s` ⛔ 在】" % k
    return d[k]


def farea(forced, blk, side):
    d = forced.get(blk) if isinstance(forced, dict) else None
    return d.get("%s_corner_min_area" % side) if isinstance(d, dict) else None


def main():
    print("=" * W)
    print("【`W-G.9-319` `§三`】`GB-170` 三釘紅格於現態之現查（唯讀）")
    print("=" * W)
    print("🛑 ⛔ 判其對 `GB-170` 失效條件之影響、⛔ 解除、⛔ 收窄、⛔ 提修法主張——出艙即止。")

    store = {}
    for tag, mode in (("甲", None), ("乙", "off")):
        for sb in (0.0, 3.5):
            store[(tag, sb)] = drive(sb, mode)

    # ── forced_map 之形（⛔ 推定）──
    r0 = store[("甲", 0.0)]
    print("\n── `forced_map` 之形（當場出艙·⛔ 推定）──")
    print("   type ＝ %s；鍵數 ＝ %s" % (type(r0["forced"]).__name__,
                                        len(r0["forced"]) if hasattr(r0["forced"], "__len__") else "—"))
    if isinstance(r0["forced"], dict):
        for k in list(r0["forced"])[:8]:
            print("   · %r → %r" % (k, r0["forced"][k]))

    # ── 三格逐格 ──
    for blk, side, sb, area in CELLS:
        print("\n" + "─" * W)
        print("【格】`%s/%s@%.1fm`（`GB` 簿所載 `range_area` ＝ `%s`）" % (blk, side, sb, area))
        print("─" * W)
        for tag in ("甲", "乙"):
            r = store[(tag, sb)]
            rows = [x for x in r["g_rows"] if x.get("所屬街廓") == blk]
            reach = bool(rows)
            print("  態%s：管線%s該街廓（`g_rows` 內 `%s` 之列 ＝ `%d`）"
                  % (tag, "**達**" if reach else "**未達**", blk, len(rows)))
            if r["err"]:
                print("        🩸 中止（逐字）：%s" % r["err"])
            if not reach:
                print("        🛑 **結構上不可得**（管線未達該街廓）"
                      "⇒ ⛔ 以空集充「已不存在」（`恆常附款 j`）")
                continue
            fv, fa = fval(r["forced"], blk, side), farea(r["forced"], blk, side)
            print("        **`%s_forced_offset` ＝ %r**（⇒ %s）／`%s_corner_min_area` ＝ **%r**"
                  % (side, fv, "🔴 **仍為強制抵費地**" if fv is True
                     else ("🟢 **已⛔ 為強制抵費地**" if fv is False else "【⛔ 可判】"),
                     side, fa))
            print("        `right_forced_offset` ＝ %r（併出·⛔ 本格之受詞）"
                  % fval(r["forced"], blk, "right" if side == "left" else "left"))
            sd = "左側" if side == "left" else "右側"
            lot = [x for x in rows if x.get("街角側別") == sd]
            print("        該側 `_lot_gate` 之筆數（`街角側別` ＝ `%s` 之列）＝ **`%d`**" % (sd, len(lot)))
            first = [x for x in lot if x.get("第1筆街角") == "是"]
            if first:
                x = first[0]
                print("        街角第 `1` 宗 ＝ `%s`／`驗_宗序` ＝ `%s`／`G(㎡)` ＝ `%s`"
                      % (x.get("暫編地號"), x.get("驗_宗序"), x.get("G(㎡)")))
            else:
                print("        街角第 `1` 宗 ＝ 【該側⛔ 有 `第1筆街角` ＝ `是` 之列】")
            di = [x for x in rows if "抵費地" in str(x.get("暫編地號", ""))]
            print("        該街廓之**抵費地**列 ＝ `%d` 筆：%s"
                  % (len(di), [(x.get("暫編地號"), x.get("G(㎡)"), x.get("街角側別")) for x in di]))

    # ── 判別力二造 ──
    print("\n" + "=" * W)
    print("【判別力二造】")
    print("=" * W)
    r = store[("甲", 0.0)]
    v = fval(r["forced"], "R4", "left")
    print("[必非零] 態甲 `R4 left` 之 `forced`（`GB` 簿 `:8293` 逐字「態甲 `R4` 左 ＝ ⚠️ 強制抵費地」）")
    print("         實得 ＝ **%r**（期 `True`）%s"
          % (v, "🟢" if v is True else "🩸 **相異·具名·⛔ 追改**"))
    # [必為零]：先列舉候選並具名選法
    corner_blocks = sorted({x.get("所屬街廓") for x in r["g_rows"]
                            if x.get("街角地") == "是"})
    allb = []
    for x in r["g_rows"]:
        if x.get("所屬街廓") not in allb:
            allb.append(x.get("所屬街廓"))
    cands = [(b, s) for b in allb for s in ("left", "right")
             if not any(y.get("所屬街廓") == b and y.get("街角地") == "是"
                        and y.get("街角側別") == ("左側" if s == "left" else "右側")
                        for y in r["g_rows"])]
    print("[必為零] **選法之具名**：候選 ＝ 態甲 `0m` 之全部 `(街廓, 側)` 對 "
          "**`%d`** 個；濾去該側有 `街角地 ＝ 是` 之列者 ⇒ **非街角側 `%d`** 個"
          % (len(allb) * 2, len(cands)))
    print("         候選之列舉（前 `6`）＝ %s" % cands[:6])
    print("         （街廓之全體 ＝ %s；其中有街角地者 ＝ %s）" % (allb, corner_blocks))
    if cands:
        b, s = cands[0]
        v2 = fval(r["forced"], b, s)
        print("         **所選（取候選之首·⛔ 以「看起來不是街角」充之）** ＝ `%s/%s` ⇒ `forced` ＝ **%r**"
              % (b, s, v2))
        print("         ⇒ 期 `False`／實得 %s %s"
              % (v2, "🟢" if v2 is False else "🩸 **相異·具名**"))
    else:
        print("         🛑 **⛔ 有非街角側可選** ⇒ 本造**不可作**·loud 具名（⛔ 以空集充綠）")


if __name__ == "__main__":
    main()
