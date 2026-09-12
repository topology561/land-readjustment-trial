# -*- coding: utf-8 -*-
"""`W-G.9-270` `p2`：`GB-160` 之**逐側處置判**（⛔ 逐側之修·單 `§三` 明令）。

🛑 **本器⛔ 調 `QK` 或任何容差**（放寬既有之閘 ＝ 黑名單·恆停機）；
🛑 **本器⛔ 改 `V1` 一字**、**⛔ 改任何生產碼一字**。

**須答之二（單 `§三` 之表·逐字）**
  `R6·right`：其退化宗 `628-53(1)` 是否**繫於 `K-9-12`**（若矩形容納轉主動，該宗是否離開配地母體）？
              **以碼面／落檔之機械依據答**，⛔ 推定。
  `R5·left` ：其失敗對**共用頂點 `0`** 之成因：係幾何上確無共用頂點，抑或 `QK` 容差之故？
              **出艙該對之二宗頂點集與其最近點距**，並判 `(甲)` 器之容差界／`(乙)` 幾何之實。

🔒 **判準之來源** ＝ 倉內既有 `V1.shared_edge`／`V1.QK`（**逐字·⛔ 另寫第二份定義**·`GB-48` 族）。
🔒 **資料源**
  `R5·left` 之幾何 ＝ **記憶體側**生產管線（同 `probe_WG9269_c4_gamma.py`·⛔ baseline·`GB-162`）。
  `R6·right` 之 `K-9-12` 欄 ＝ **當次實跑**之 `got_*` 落檔（⛔ `verify/baselines`·`GB-162` 三禁令）。

🔒 **坑之攔法（逐條施行）**
  坑 `al`：⛔ 以「檔在」推「欄在」——先印該欄之**在否與非空列數**；母體 `0` ⇒ **loud 拒測**。
  坑 `ao`：凡以某判定欄推生產之處置，須先證**該欄即驅動該處置之欄**——
           ① 印該欄之**全體值分布**；② 查該鏈於正典之**落地狀態**。
  坑 `ai`：⛔ 憑字形猜鍵——自落檔之表頭**逐字取其碼點**。
  坑 `z` ：未量⛔ 印 `0`，一律印 `⛔ 可得`。
  坑 `y` ：⛔ 憑欄名之語意猜其值之形——先印值分布再定框。

用法：`python verify/probes/probe_WG9270_p2_gb160.py [倉根]`
`rc`：`0` 二答皆出艙／`3` 母體為 `0`（loud 拒測）／`5` **量測器紅**（判別力二造不如預期）。
"""
import contextlib
import csv
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
import probe_WG9266_V1prime_3groups as V1                           # noqa: E402
import probe_WG9269_c4_gamma as G4                                  # noqa: E402

BT = chr(96)
W = 116
# 🔒 受詞（單 `§三` 之表·逐字）
R5_SIDE = ("R5", "left")
R5_PAIR = ("628-45(1)+", "628-18(2)")
R6_SIDE = ("R6", "right")
R6_LOT = "628-53(1)"


def say(s=""):
    print(s)


def drive(sb):
    """同 `probe_WG9269_c4_gamma_diag.drive`（逐字沿用·⛔ 另寫第二份驅動）。"""
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
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        p = getattr(e, "partial", None) or {}
        g_rows = p.get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return rows


def seg_pt_dist(p, a, b):
    """點到線段之距（⛔ 依賴 shapely·純算術·可逐步復算）。"""
    ax, ay = a
    bx, by = b
    px, py = p
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    if L2 == 0.0:
        return ((px - ax) ** 2 + (py - ay) ** 2) ** 0.5
    t = ((px - ax) * dx + (py - ay) * dy) / L2
    t = max(0.0, min(1.0, t))
    qx, qy = ax + t * dx, ay + t * dy
    return ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5


def main():
    rc = 0
    say("=" * W)
    say("【`W-G.9-270` `p2`】`GB-160` 之逐側**處置判**（⛔ 逐側之修）")
    say("=" * W)
    say("🔒 判準來源 ＝ `V1.shared_edge`／`V1.QK` 逐字｜`QK` ＝ %r（**⛔ 調**）" % V1.QK)
    say("")

    # ══════════════════════════════════════════════════════════════════
    # 甲　`R5·left`：共用頂點 `0` 之成因鑑別
    # ══════════════════════════════════════════════════════════════════
    say("─" * W)
    say("【甲】`R5·left` 失敗對之共用頂點 `0` ⇒ `(甲)` 器之容差界 抑或 `(乙)` 幾何之實？")
    say("─" * W)
    rows = drive(3.5)
    say("🔒 母體 ＝ 記憶體側 `g_rows` **%d** 列（情境 `3.5m`·⛔ 落檔·⛔ baseline）" % len(rows))

    sr = V1.side_rows(rows, R5_SIDE[0], R5_SIDE[1])
    say("🔒 `%s·%s` 之宗數 ＝ **%d**（`V1.side_rows` 逐字·已依 `累積S(m)` 排序）"
        % (R5_SIDE[0], R5_SIDE[1], len(sr)))
    if not sr:
        say("🛑 母體 `0` ⇒ **loud 拒測**（⛔ 靜默綠·坑 `al`）")
        sys.exit(3)

    say("   逐宗：" + "／".join(
        "%s" % (r.get("暫編地號") or "").strip() for r, _v, _p in sr))

    idx = {}
    for k, (r, v, p) in enumerate(sr):
        idx[(r.get("暫編地號") or "").strip()] = (k, r, v, p)
    missing = [lot for lot in R5_PAIR if lot not in idx]
    if missing:
        say("🛑 受詞之宗⛔ 在母體內：%s ⇒ **loud 拒測**（⛔ 猜、⛔ 以近似物代之）" % missing)
        sys.exit(3)

    kA, rA, vA, pA = idx[R5_PAIR[0]]
    kB, rB, vB, pB = idx[R5_PAIR[1]]
    say("   受詞對 ＝ `%s`（序 %d） ─ `%s`（序 %d）%s"
        % (R5_PAIR[0], kA, R5_PAIR[1], kB,
           "  ⇒ **相鄰**" if abs(kA - kB) == 1 else "  ⇒ ⚠️ **⛔ 相鄰**"))
    say("")

    say("   ── 宗 A `%s` 之頂點集（`cut_coords` 逐字·%d 點）──" % (R5_PAIR[0], len(vA)))
    for i, (x, y) in enumerate(vA):
        say("      A%-2d  (%.9f, %.9f)" % (i, x, y))
    say("   ── 宗 B `%s` 之頂點集（%d 點）──" % (R5_PAIR[1], len(vB)))
    for i, (x, y) in enumerate(vB):
        say("      B%-2d  (%.9f, %.9f)" % (i, x, y))
    say("")

    # 最近點距（頂點↔頂點）
    best = None
    for i, a in enumerate(vA):
        for j, b in enumerate(vB):
            d = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
            if best is None or d < best[0]:
                best = (d, i, j, a, b)
    dmin, bi, bj, ba, bb = best
    say("   🔑 **頂點↔頂點之最近點距** ＝ **%.12f m**（A%d ↔ B%d）" % (dmin, bi, bj))
    say("       A%d (%.9f, %.9f)   B%d (%.9f, %.9f)" % (bi, ba[0], ba[1], bj, bb[0], bb[1]))
    say("       |Δx| ＝ %.12f ／ |Δy| ＝ %.12f   （`shared_edge` 之判為此二者<u>各自</u> < `QK`）"
        % (abs(ba[0] - bb[0]), abs(ba[1] - bb[1])))

    # 頂點↔對方邊界（區辨「頂點錯位」與「真不相接」）
    bestA2B = min(min(seg_pt_dist(a, vB[j], vB[(j + 1) % len(vB)])
                      for j in range(len(vB))) for a in vA)
    bestB2A = min(min(seg_pt_dist(b, vA[i], vA[(i + 1) % len(vA)])
                      for i in range(len(vA))) for b in vB)
    say("   🔑 **頂點↔對方<u>邊</u>之最近距**：A→B `%.12f m` ／ B→A `%.12f m`" % (bestA2B, bestB2A))
    say("       （其用：區辨「**頂點錯位而邊相接**」與「**二宗真不相接**」——"
        "前者此值近 `0` 而頂點距不近 `0`）")
    say("")

    # 判
    ratio = dmin / V1.QK if V1.QK else float("inf")
    if dmin < V1.QK:
        judge = "🔴 `(甲)` 器之容差界——距 < `QK` 而器判 `0`，自相矛盾 ⇒ 須回查 `shared_edge`"
    elif ratio < 1e3:
        judge = ("🟡 `(甲)` 器之容差界之**鄰域**——距 ＝ `QK` 之 %.3g 倍"
                 "（同數量級 ⇒ 調 `QK` 可改判·🛑 **本批⛔ 調**）" % ratio)
    else:
        judge = ("🟢 `(乙)` **幾何之實**——距 ＝ `QK` 之 **%.3g** 倍，"
                 "**⛔ 任何合理容差可及** ⇒ 二宗於該對確無共用頂點" % ratio)
    say("   ⇒ **判** ＝ %s" % judge)
    say("")

    # 判別力二造（證本距量測非恆大亦非恆小）
    say("   ── 判別力二造（證本距量測**⛔ 恆大**亦**⛔ 恆小**）──")
    pass_pairs = []
    for k in range(len(sr) - 1):
        ca = sr[k][1]
        cb = sr[k + 1][1]
        sh = V1.shared_edge(ca, cb)
        if len(sh) == 2:
            d2 = min(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
                     for a in ca for b in cb)
            pass_pairs.append((sr[k][0].get("暫編地號").strip(),
                               sr[k + 1][0].get("暫編地號").strip(), d2))
    if pass_pairs:
        lo, hi, d2 = pass_pairs[0]
        say("      造甲[已知<u>共用頂點 2</u>之對] `%s` ─ `%s` ⇒ 最近點距 ＝ **%.12f m** "
            "（期 < `QK` ＝ %r）⇒ %s" % (lo, hi, d2, V1.QK, "✅" if d2 < V1.QK else "🔴"))
        ok_a = d2 < V1.QK
    else:
        say("      造甲 ⇒ **⛔ 可得**（本側無共用頂點 `2` 之對）")
        ok_a = None
    say("      造乙[受詞對] `%s` ─ `%s` ⇒ 最近點距 ＝ **%.12f m**（期 ≥ `QK`）⇒ %s"
        % (R5_PAIR[0], R5_PAIR[1], dmin, "✅" if dmin >= V1.QK else "🔴"))
    ok_b = dmin >= V1.QK
    if ok_a is False or not ok_b:
        say("      🛑 二造不如預期 ⇒ **量測器紅** ⇒ ⛔ 出艙上開判")
        rc = 5
    elif ok_a is None:
        say("      🟡 造甲⛔ 可得 ⇒ 本器之判別力**僅單向自證**（照實·⛔ 頂替）")
    else:
        say("      ⇒ **器非紅**（一造 < `QK`、一造 ≥ `QK` ⇒ 本量⛔ 恆大亦⛔ 恆小）✅")
    say("")

    # ══════════════════════════════════════════════════════════════════
    # 乙　`R6·right`：`628-53(1)` 是否繫於 `K-9-12`
    # ══════════════════════════════════════════════════════════════════
    say("─" * W)
    say("【乙】`R6·right` 之退化宗 `%s` 是否**繫於 `K-9-12`**（矩形容納轉主動後是否離開配地母體）？" % R6_LOT)
    say("─" * W)

    # 落檔之在否（⛔ 以「檔在」推「欄在」·坑 `al`）
    cands = []
    outdir = os.path.join(REPO, "verify", "out")
    for fn in sorted(os.listdir(outdir)):
        if fn.startswith("got_") and fn.endswith(".csv") and "G" in fn:
            cands.append(fn)
    say("🔒 **當次實跑**之 `got_*.csv`（⛔ `verify/baselines`·`GB-162`）：%d 支" % len(cands))
    for fn in cands:
        say("   - %s  （%d B·mtime %s）"
            % (fn, os.path.getsize(os.path.join(outdir, fn)),
               __import__("time").strftime(
                   "%Y-%m-%d %H:%M:%S",
                   __import__("time").localtime(os.path.getmtime(os.path.join(outdir, fn))))))

    target = None
    for fn in cands:
        if "3.5m" in fn and "partial" not in fn:
            target = fn
    if target is None:
        say("🛑 `3.5m` 之完整落檔⛔ 存在 ⇒ **loud 拒測**（⛔ 以 `_partial` 代之·坑 `aj`）")
        sys.exit(3)
    say("   ⇒ 取 **%s**" % target)
    say("")

    with io.open(os.path.join(outdir, target), "r", encoding="utf-8-sig", newline="") as f:
        drows = list(csv.DictReader(f))
    hdr = list(drows[0].keys()) if drows else []
    say("🔒 **表頭逐字取自落檔**（坑 `ai`：⛔ 憑字形猜鍵）·共 %d 欄、%d 列" % (len(hdr), len(drows)))
    kcols = [h for h in hdr if h.startswith("驗_")]
    say("   `驗_` 系欄（逐字 ＋ 碼點）：")
    for h in kcols:
        say("      %-22s  U+%s" % (BT + h + BT, " U+".join("%04X" % ord(c) for c in h)))
    if not kcols:
        say("🛑 落檔⛔ 帶任何 `驗_` 欄 ⇒ **loud 拒測**（坑 `al`：欄之缺席）")
        sys.exit(3)

    # 逐欄之非空列數（坑 `al`）
    say("")
    say("   ── 各 `驗_` 欄之**非空列數**（坑 `al`：母體 `0` ⇒ loud 拒測）──")
    for h in kcols:
        ne = sum(1 for r in drows if (r.get(h) or "").strip() not in ("", "—"))
        say("      %-22s 非空 %4d ／ %4d" % (h, ne, len(drows)))

    # 值分布（坑 `ao` 法①·坑 `y`）
    # 🔒 **K-9-12 之欄 ＝ `驗_A幾何`**（機械定位：`app.py` `_lot_gate` 之
    #    「── A 幾何（`K-9-12` 矩形·可旋轉可平移）──」段 ⇒ `_A, _Ad = _k923_gate2(...)`）。
    #    🛑 **`驗_rejected` ⛔ 為受詞**——`app.py:12587` 逐字 `_rejected = any(_v is False for _v in (_A, _B, _C))`，
    #       且 `app.py:9291` 逐字警示其「含 `K-9-12`（閘二·射程外）」⇒ 複合欄⛔ 單獨證繫屬。
    for h in ("驗_A幾何", "驗_B藍影", "驗_C面積", "驗_總判", "驗_rejected"):
        if h not in hdr:
            say("   ⚠️ 欄 %s ⛔ 在 ⇒ 其值分布 **⛔ 可得**（坑 `z`：⛔ 印 `0`）" % (BT + h + BT))
            continue
        dist = {}
        for r in drows:
            v = (r.get(h) or "").strip() or "(空)"
            dist[v] = dist.get(v, 0) + 1
        say("")
        say("   ── 欄 %s 之**全體值分布**（坑 `ao` 法①）──" % (BT + h + BT))
        for v, c in sorted(dist.items(), key=lambda t: -t[1]):
            say("      %-14s %4d 列" % (v, c))

    # 受詞宗之逐欄值
    say("")
    hit = [r for r in drows
           if (r.get("暫編地號") or "").strip() == R6_LOT
           and (r.get("所屬街廓") or "").strip() == R6_SIDE[0]]
    if not hit:
        say("🛑 `%s`＠`%s` ⛔ 在該落檔 ⇒ **loud 拒測**" % (R6_LOT, R6_SIDE[0]))
        sys.exit(3)
    r0 = hit[0]
    say("   ── 受詞 `%s`＠`%s·%s` 之逐欄值 ──" % (R6_LOT, R6_SIDE[0], R6_SIDE[1]))
    for h in ["所屬街廓", "推進側別", "暫編地號", "G(㎡)", "宗地寬度(m)", "街角地"] + kcols:
        if h in hdr:
            v = (r0.get(h) or "").strip()
            say("      %-22s %s" % (h, v if v else "⛔ 可得"))

    # 「若 K-9-12 轉主動，該宗是否離開母體」之機械判
    say("")
    say("   ── 機械判（⛔ 推定）──")
    KCOL = "驗_A幾何"          # 🔒 ＝ `K-9-12` 之欄（機械定位見上註）
    kv = (r0.get(KCOL) or "").strip() if KCOL in hdr else ""
    say("      🔑 **`K-9-12` 之欄 ＝ %s**（⛔ `驗_rejected`——其為 `any(A,B,C)` 之複合）"
        % (BT + KCOL + BT))
    say("      受詞之 %s ＝ **%s**" % (BT + KCOL + BT, kv if kv else "⛔ 可得"))
    for h in ("驗_A_W", "驗_A_D", "驗_A_理由", "驗_A_命中角"):
        if h in hdr:
            v = (r0.get(h) or "").strip()
            say("        %-16s %s" % (h, v if v else "⛔ 可得"))
    if kv:
        n_same = sum(1 for r in drows if (r.get(KCOL) or "").strip() == kv)
        say("      該情境下 %s ＝ %r 之宗數 ＝ **%d** ／ %d"
            % (BT + KCOL + BT, kv, n_same, len(drows)))
        say("      ⇒ **繫屬之判**：其 %s ＝ %r %s"
            % (BT + KCOL + BT, kv,
               "⇒ 🔴 **繫於 `K-9-12`**（閘二判其不合格 ⇒ 矩形容納轉主動後該宗離開配地母體）"
               if kv == "不合格" else
               ("⇒ 🟢 **⛔ 繫於 `K-9-12`**（閘二判其合格 ⇒ 轉主動亦不離開母體）"
                if kv == "合格" else
                "⇒ 🟡 **⛔ 可判**（四態之第三／四態·⛔ 與「判定為偽」共用出艙碼）")))
    else:
        say("      ⇒ **繫屬之判** ＝ **⛔ 可得**（該欄不在或為空·坑 `z`：⛔ 印 `0`）")
    rej = (r0.get("驗_rejected") or "").strip() if "驗_rejected" in hdr else ""
    tot = (r0.get("驗_總判") or "").strip() if "驗_總判" in hdr else ""
    say("      （併陳·⛔ 為受詞）`驗_rejected` ＝ %s ／ `驗_總判` ＝ %s"
        % (rej if rej else "⛔ 可得", tot if tot else "⛔ 可得"))
    say("")
    say("=" * W)
    say("🔒 本器**⛔ 作成 `GB-160` 之結清判**（裁歸發單側·單 `§三` 明令）；亦**⛔ 調任何容差**。")
    sys.exit(rc)


if __name__ == "__main__":
    main()
