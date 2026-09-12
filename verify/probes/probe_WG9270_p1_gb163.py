# -*- coding: utf-8 -*-
"""`W-G.9-270` `p1`：`GB-163` 之結清——`P-3` 判定集自 `6／56`・`5／59` **擴至全部留存宗**。

🛑 **`GB-163` 逐字之受詞**：`P-3`（「**每一留存宗同時臨 FRONTLINE 與 BASELINE，臨接長 `> 0`**」）
   之判定集現僅 `6／56`（`0m`）與 `5／59`（`3.5m`）；餘宗之二臨接長為 `—`（**第一關未評估**）
   ⇒ **無從回測** ⇒ ⛔ 引其為「每一留存宗皆臨二線」之證。

🔑 **本器之作法（單 `§二` 逐條）**
  `1` **另備臨接長之量測**：⛔ 自 `驗_B_臨正街`／`驗_B_臨屁股` 欄取（**該二欄正為 `—` 之來源**）；
      改以**生產碼之單一真相源** `_k923_touch_len`（`app.py`·`#20`）**逐宗直算**。
      🔒 **輸入以間諜法取自生產**——包裹 `ns['_lot_gate']`，逐次錄其實參
      （`res['cut_coords']` ⋀ `blk_ctx` 之 `front_p1`／`front_p2`／`baseline_pts`），
      **⛔ 於器內重導任何幾何**。
      🔒 **其線即第一關所用之線**（機械依據·`app.py` `_blue_shadow_tri` 之
      `_o = front_p1`／`_d = û(front_p2 − front_p1)`／`_bp = base_pt`／`_bd = û(base_dir)`，
      而 `_lot_gate` 以 `_bp[0]` ⋀ `_bp[1]-_bp[0]` 餵之）⇒ **二線皆街廓級、⛔ 繫於街角**。
  `2` **自我驗證閘（硬）**：於**第一關已評估**之宗，新器所得之二臨接長須與既有欄**逐位相同**。
      🔒 **容差之具名**：既有欄經 `_n6`（`round(x, 6)`）落檔 ⇒ 比較端一律取 `round(mine, 6)`，
      判準為**相等**（容差 `0`）。**⛔ 放寬。不過 ⇒ loud 拒測·停機上呈。**
  `3` **判別力二造**：人造一宗使其一臨接長為 `0` ⇒ 須紅；人造一宗二者皆 `> 0` ⇒ 須綠。
      **二造同色 ⇒ 閘失能·停機。**
  `4` **出艙**：逐情境之判定集基數（期 ＝ **全部留存宗**）／**成立・不成立・⛔ 可量**三分類
      （三者和須 ＝ 留存宗數）／不成立者**逐宗具名其地號與歸戶**。

🛑 **本器⛔ 作成 `GB-163` 之結清裁**（裁歸發單側·單 `§二` 明令）。
🔒 坑之攔法：`z`（未量⛔ 印 `0`·印「⛔ 可量」）／`ai`（⛔ 憑字形猜鍵·自實物取碼點）／
   `u`（對照組全零 ⇒ 先判量測器紅）／`al`（⛔ 以「檔在」推「欄在」）。

用法：`python verify/probes/probe_WG9270_p1_gb163.py [倉根]`
`rc`：`0`／`3` 母體為 `0`（loud 拒測）／`4` **自我驗證閘不過**（loud 拒測·停機）／
     `5` **量測器紅**（判別力二造同色）。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, os.path.join(VERIFY, "fixtures"))
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
import probe_WG9269_c4_gamma as G4                                  # noqa: E402

BT = chr(96)
W = 118
SBS = (0.0, 3.5)


def say(s=""):
    print(s)


def drive_spy(sb):
    """驅動生產管線一次，並以**間諜法**錄 `_lot_gate` 之逐次實參（⛔ 改生產碼一字）。

    🔒 **間諜之用⛔ 為母體**——其錄 `91` 次呼叫而留存宗僅 `56`（含被 `K-9-17` 剔除者
    ⋀ 二呼叫點之重複）⇒ **母體取 `g_rows`**（＝留存宗），間諜只供**二線之實參**
    （逐 `(街廓, 側)` 之 `front_p1`／`front_p2`／`baseline_pts`）。
    """
    ns, fake_st = harvest()
    rec = []
    _orig = ns["_lot_gate"]

    def _spy(res, tp, blk_ctx, *a, **kw):
        out = _orig(res, tp, blk_ctx, *a, **kw)
        rec.append({"res": res, "tp": tp, "ctx": blk_ctx,
                    "kw": dict(kw), "out": out})
        return out

    ns["_lot_gate"] = _spy

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
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, skipped = G4.to_csv_like(g_rows)
    return ns, rec, rows, skipped


def owner_map(sb):
    """`暫編地號 → 歸戶鍵Gxxx`（自**當次實跑**之 `got_W-D.4_清單_*.csv`·⛔ baseline）。

    🔒 坑 `al`：⛔ 以「檔在」推「欄在」——回 `(map, 診斷字串)`，欄不在即具名。
    """
    tag = "0m" if abs(sb) < 1e-9 else "3.5m"
    p = os.path.join(REPO, "verify", "out", "got_W-D.4_清單_退縮%s.csv" % tag)
    if not os.path.exists(p):
        return {}, "🛑 `%s` ⛔ 存在 ⇒ 歸戶一律印「⛔ 可得」" % os.path.basename(p)
    import csv as _csv
    with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
        rr = list(_csv.DictReader(f))
    if not rr:
        return {}, "🛑 `%s` 無列 ⇒ 歸戶一律印「⛔ 可得」" % os.path.basename(p)
    hdr = list(rr[0].keys())
    k_g = next((h for h in hdr if "歸戶" in h), None)
    k_l = next((h for h in hdr if "宗清單" in h), None)
    if not k_g or not k_l:
        return {}, ("🛑 `%s` 缺欄（歸戶鍵 ＝ %r／宗清單 ＝ %r）⇒ 歸戶一律印「⛔ 可得」"
                    % (os.path.basename(p), k_g, k_l))
    m = {}
    for r in rr:
        g = (r.get(k_g) or "").strip()
        for lot in (r.get(k_l) or "").split(";"):
            lot = lot.strip()
            if lot:
                m[lot] = g
    return m, ("✅ 自 `%s` 取得 `%s`→`%s` 映射 **%d** 筆（非空列 %d／%d）"
               % (os.path.basename(p), k_l, k_g, len(m), len(rr), len(rr)))


def lines_of(ctx):
    """自 `blk_ctx` 取二線（**間諜法所得·⛔ 器內重導**）。回 `(fp1, fdir, bp0, bdir)` 或 `None`。"""
    f1 = ctx.get("front_p1")
    f2 = ctx.get("front_p2")
    bp = list(ctx.get("baseline_pts") or [])
    if f1 is None or f2 is None or len(bp) < 2:
        return None
    fdir = (float(f2[0]) - float(f1[0]), float(f2[1]) - float(f1[1]))
    bdir = (float(bp[1][0]) - float(bp[0][0]), float(bp[1][1]) - float(bp[0][1]))
    return (f1, fdir, bp[0], bdir)


def measure(ns, coords, ln):
    """以**生產碼**之 `_k923_touch_len` 直算二臨接長（⛔ 器內另寫第二份定義）。"""
    from shapely.geometry import Polygon as _P
    p = _P(coords)
    if not p.is_valid:
        p = p.buffer(0)
    f1, fdir, bp0, bdir = ln
    lf = float(ns["_k923_touch_len"](p, f1, fdir))
    lb = float(ns["_k923_touch_len"](p, bp0, bdir))
    return lf, lb


def pick_key(d, want):
    """⛔ 憑字形猜鍵（坑 `ai`）——自實物之鍵集取含 `want` 者，並回其逐字與碼點。"""
    for k in d.keys():
        if want in k:
            return k
    return None


def main():
    rc = 0
    say("=" * W)
    say("【`W-G.9-270` `p1`】`GB-163`：`P-3` 判定集**擴至全部留存宗**")
    say("=" * W)
    say("🔒 真相源 ＝ 生產碼 `_k923_touch_len`（`app.py`）｜輸入以**間諜法**取自 `ns['_lot_gate']`")
    say("🔒 ⛔ 自 `驗_B_臨正街`／`驗_B_臨屁股` 欄取（該二欄正為 `—` 之來源·單 `§二-1`）")
    say("")

    summary = []
    for sb in SBS:
        tag = "%gm" % sb
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        ns, rec, prows, skipped = drive_spy(sb)
        say("🔒 間諜所錄 `_lot_gate` 呼叫 ＝ **%d** 次（**⛔ 母體**——含被 `K-9-17` 剔除者"
            " ⋀ 二呼叫點之重複）" % len(rec))
        say("🔒 **母體 ＝ 留存宗** ＝ `to_csv_like(g_rows)` ＝ **%d** 列（靜默丟列 %d ⇒ %s）"
            % (len(prows), skipped, "✅" if skipped == 0 else "🔴 須究"))
        if not prows:
            say("🛑 母體 `0` ⇒ **loud 拒測**（⛔ 靜默綠·坑 `al`）")
            sys.exit(3)

        # ── 二線之實參（間諜法·逐 `(街廓, 側)`）─────────────────────────
        ctx_by = {}
        for r in rec:
            kw = r["kw"] or {}
            key = (str(kw.get("_label") or ""), str(kw.get("chain_side") or ""))
            if key not in ctx_by:
                ln = lines_of(r["ctx"] or {})
                if ln is not None:
                    ctx_by[key] = ln
        say("🔒 二線之實參（間諜法自 `blk_ctx` 取·⛔ 器內重導）＝ **%d** 組 `(街廓, 側)`：%s"
            % (len(ctx_by), "／".join("%s·%s" % k for k in sorted(ctx_by))))

        # ── 🔑 **二線係街廓級**之機械驗證（⛔ 推定）────────────────────
        #    其據：`app.py` `_blue_shadow_tri` 之 `_o = front_p1`／`_d = û(front_p2−front_p1)`／
        #    `_bp = base_pt`／`_bd = û(base_dir)`，而 `_lot_gate` 逐側皆自**同一 `blk_ctx`** 餵之。
        #    ⇒ 若同街廓左右側之二線**逐位相同**，則其為街廓級，抵費地得用同一線量之。
        blk_ln, same_all, cmp_n = {}, True, 0
        for (b, s), ln in sorted(ctx_by.items()):
            if b in blk_ln:
                cmp_n += 1
                if repr(blk_ln[b]) != repr(ln):
                    same_all = False
                    say("   🔴 `%s` 之 `%s` 側二線與前側**不同** ⇒ ⛔ 得視為街廓級" % (b, s))
            else:
                blk_ln[b] = ln
        say("   🔑 **街廓級之驗**：可比之左右對 **%d** 組 ⇒ 逐位相同 %s"
            % (cmp_n, "✅（⇒ 二線係街廓級·抵費地得用同一線量之）" if same_all
               else "🔴（⇒ ⛔ 得視為街廓級）"))
        say("      判別力：`repr` 比對之非恆真 ⇒ 對一人造之擾動須轉紅——"
            "實測 `%s` 之線加 `+1.0` ⇒ %s"
            % (sorted(blk_ln)[0],
               "相異 ✅" if repr(blk_ln[sorted(blk_ln)[0]]) != repr(
                   ((blk_ln[sorted(blk_ln)[0]][0][0] + 1.0,
                     blk_ln[sorted(blk_ln)[0]][0][1]),) + blk_ln[sorted(blk_ln)[0]][1:])
               else "🔴 恆真"))

        # ── 歸戶之映射（坑 `ai`：⛔ 憑字形猜鍵）────────────────────────
        omap, odiag = owner_map(sb)
        say("🔒 歸戶之取：%s" % odiag)

        # ── 逐宗量測（母體 ＝ 留存宗）───────────────────────────────────
        import ast as _ast
        rows = []
        for r in prows:
            lot = (r.get("暫編地號") or "").strip() or "?"
            blk = (r.get("所屬街廓") or "").strip() or "?"
            side = (r.get("推進側別") or "").strip()
            own = omap.get(lot, "")
            cc = (r.get("cut_coords") or "").strip()
            try:
                coords = [(float(a), float(b)) for a, b in _ast.literal_eval(cc)] if cc else []
            except Exception:                                   # noqa: BLE001
                coords = []
            # 🔒 先取該 `(街廓, 側)`；無則**退為街廓級**（僅於上開驗證為 ✅ 時·⛔ 無條件退）
            ln = ctx_by.get((blk, side))
            via = "側"
            if ln is None and same_all:
                ln = blk_ln.get(blk)
                via = "街廓級"
            if len(coords) < 3:
                rows.append((blk, side, lot, own, None, None, "⛔ 可量", r,
                             "cut_coords 不足 3 點"))
                continue
            if ln is None:
                rows.append((blk, side, lot, own, None, None, "⛔ 可量", r,
                             ("間諜未錄該街廓之 blk_ctx 二線" if same_all
                              else "間諜未錄該 (街廓,側) 之二線，且街廓級之驗未過 ⇒ ⛔ 得退")))
                continue
            _ = via
            lf, lb = measure(ns, coords, ln)
            verdict = "成立" if (lf > 0.0 and lb > 0.0) else "不成立"
            rows.append((blk, side, lot, own, lf, lb, verdict, r, ""))

        # ── `2` 自我驗證閘（硬）──────────────────────────────────────────
        say("")
        say("   ── `§二-2` **自我驗證閘（硬）**：於第一關**已評估**之宗，新器須與既有欄逐位相同 ──")
        say("      🔒 容差之具名：既有欄經 `_n6` ＝ `round(x, 6)` ⇒ 比較端取 `round(mine, 6)`，"
            "判準 ＝ **相等**（容差 `0`·⛔ 放寬）")
        chk = []
        for row in rows:
            _blk, _sd, lot, _own, lf, lb, _v, r, _w = row
            ef = (r.get("驗_B_臨正街") or "").strip()
            eb = (r.get("驗_B_臨屁股") or "").strip()
            if ef in ("", "—") or eb in ("", "—"):
                continue
            if lf is None:
                chk.append((lot, ef, eb, "⛔ 可量", "⛔ 可量", False))
                continue
            mf, mb = round(lf, 6), round(lb, 6)
            ok = (mf == float(ef)) and (mb == float(eb))
            chk.append((lot, ef, eb, mf, mb, ok))
        say("      判定集（第一關已評估者）＝ **%d** 宗" % len(chk))
        say("      %-18s %-16s %-16s %-16s %-16s %s"
            % ("宗", "既有 臨正街", "既有 臨屁股", "新器 臨正街", "新器 臨屁股", "逐位"))
        for lot, ef, eb, mf, mb, ok in chk:
            say("      %-18s %-16s %-16s %-16s %-16s %s"
                % (lot, ef, eb, mf, mb, "✅" if ok else "🔴"))
        if not chk:
            say("      🛑 判定集為 `0` ⇒ **loud 拒測**（⛔ 靜默綠·坑 `u`：對照組全零先判量測器紅）")
            sys.exit(4)
        if not all(o for *_x, o in chk):
            say("      🛑 **自我驗證閘不過** ⇒ loud 拒測·**停機上呈**（單 `§二-2` 明令）")
            sys.exit(4)
        say("      ⇒ **%d／%d 逐位相同** ✅ ⇒ 新器之量與第一關**同源可比**" % (len(chk), len(chk)))

        # ── `3` 判別力二造 ──────────────────────────────────────────────
        say("")
        say("   ── `§二-3` **判別力二造**（二造同色 ⇒ 閘失能·停機）──")
        base = None
        for row in rows:
            if row[6] == "成立":
                base = row
                break
        if base is None:
            say("      🛑 ⛔ 可得一「二者皆 `> 0`」之實宗 ⇒ **loud 拒測**")
            sys.exit(5)
        b_blk, b_sd, b_lot, _bo, lf0, lb0, _bv, b_r, _bw = base
        cc = (b_r.get("cut_coords") or "").strip()
        coords = [(float(a), float(b)) for a, b in _ast.literal_eval(cc)]
        ln = ctx_by[(b_blk, b_sd)]
        say("      造甲［二者皆 `> 0`·取實宗 `%s`＠`%s·%s`］⇒ 臨正街 %.9f ／ 臨屁股 %.9f ⇒ %s"
            % (b_lot, b_blk, b_sd, lf0, lb0, "🟢 綠" if (lf0 > 0 and lb0 > 0) else "🔴 紅"))
        # 造乙：平移該宗使其遠離 FRONTLINE（必然使臨正街長 ＝ 0）
        SHIFT = 1000.0
        f1, fdir, _bp0, _bdir = ln
        ux = fdir[0] / ((fdir[0] ** 2 + fdir[1] ** 2) ** 0.5)
        uy = fdir[1] / ((fdir[0] ** 2 + fdir[1] ** 2) ** 0.5)
        nx, ny = -uy, ux                       # FRONTLINE 之法向 ⇒ 平移必離開該線
        moved = [(x + nx * SHIFT, y + ny * SHIFT) for x, y in coords]
        lf1, lb1 = measure(ns, moved, ln)
        say("      造乙［同宗沿 FRONTLINE **法向**平移 `+%.0f m`］⇒ 臨正街 %.9f ／ 臨屁股 %.9f ⇒ %s"
            % (SHIFT, lf1, lb1, "🟢 綠" if (lf1 > 0 and lb1 > 0) else "🔴 紅"))
        c_a = (lf0 > 0 and lb0 > 0)
        c_b = (lf1 > 0 and lb1 > 0)
        if c_a == c_b:
            say("      🛑 **二造同色** ⇒ 閘失能 ⇒ **停機**（單 `§二-3` 明令）")
            sys.exit(5)
        say("      ⇒ **器非紅**（一造綠、一造紅 ⇒ 本判⛔ 恆綠亦⛔ 恆紅）✅")

        # ── `4` 三分類出艙 ──────────────────────────────────────────────
        say("")
        say("   ── `§二-4` **三分類**（三者和須 ＝ 留存宗數）──")
        n_ok = sum(1 for x in rows if x[6] == "成立")
        n_no = sum(1 for x in rows if x[6] == "不成立")
        n_na = sum(1 for x in rows if x[6] == "⛔ 可量")
        say("      留存宗數（＝ `g_rows` 之列數）＝ **%d**" % len(rows))
        say("      成立 **%d** ／ 不成立 **%d** ／ ⛔ 可量 **%d**   ⇒ 和 ＝ **%d** %s"
            % (n_ok, n_no, n_na, n_ok + n_no + n_na,
               "✅ ＝ 留存宗數" if n_ok + n_no + n_na == len(rows) else "🔴 ≠ 留存宗數"))
        say("      🔑 **判定集基數 ＝ %d／%d**（＝ 成立 ＋ 不成立·⛔ 含「⛔ 可量」）"
            % (n_ok + n_no, len(rows)))
        # 🔒 **二類分列**（⛔ 併計）：`留存宗` 含**配地宗**與**抵費地**二類；
        #    「抵費地是否落於 `P-3` 之受詞內」係**域問題** ⇒ **⛔ CC 自裁**，只分列出艙。
        say("")
        say("      ── 二類分列（🛑 「抵費地是否落於 `P-3` 之受詞內」＝ **域問題**·⛔ CC 自裁）──")
        for cls, pred in (("配地宗", lambda x: x[1] != "抵費地"),
                          ("抵費地", lambda x: x[1] == "抵費地")):
            sub = [x for x in rows if pred(x)]
            s_ok = sum(1 for x in sub if x[6] == "成立")
            s_no = sum(1 for x in sub if x[6] == "不成立")
            s_na = sum(1 for x in sub if x[6] == "⛔ 可量")
            say("      %-8s 母體 %-4d ｜ 成立 %-4d 不成立 %-4d ⛔ 可量 %-4d ｜ 判定集 %d／%d"
                % (cls, len(sub), s_ok, s_no, s_na, s_ok + s_no, len(sub)))
        if n_no:
            say("")
            say("      ── **不成立者逐宗具名**（地號 ⋀ 歸戶·單 `§二-4` 明令）──")
            say("      %-6s %-7s %-20s %-10s %-18s %-18s"
                % ("街廓", "側", "暫編地號", "歸戶", "臨正街(m)", "臨屁股(m)"))
            for blk, sd, lot, own, lf, lb, v, _r, _w in rows:
                if v == "不成立":
                    say("      %-6s %-7s %-20s %-10s %-18.9f %-18.9f"
                        % (blk, sd, lot, own if own else "⛔ 可得", lf, lb))
        if n_na:
            say("")
            say("      ── **⛔ 可量者逐宗具名其不可量之由**（單 `§二` 之 🛑 明令）──")
            for blk, sd, lot, own, _lf, _lb, v, _r, why in rows:
                if v == "⛔ 可量":
                    say("      %-6s %-7s %-20s %-10s  由 ＝ %s"
                        % (blk, sd, lot, own if own else "⛔ 可得", why))
        summary.append((tag, len(rows), n_ok, n_no, n_na, len(chk)))
        say("")

    say("=" * W)
    say("【總結】逐情境")
    say("   %-8s %-10s %-8s %-10s %-12s %-16s %s"
        % ("情境", "留存宗", "成立", "不成立", "⛔ 可量", "自我驗證閘", "判定集"))
    for tag, n, a, b, c, k in summary:
        say("   %-8s %-10d %-8d %-10d %-12d %-16s %d／%d"
            % (tag, n, a, b, c, "%d／%d ✅" % (k, k), a + b, n))
    say("")
    say("🛑 **本器⛔ 作成 `GB-163` 之結清裁**——判定集達全部留存宗 ⋀ 不成立為 `0` 方得判其**可結清**，")
    say("   而**其結清之裁歸發單側**（單 `§二` 逐字·⛔ CC 自裁）。")
    sys.exit(rc)


if __name__ == "__main__":
    main()
