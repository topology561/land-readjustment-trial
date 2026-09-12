# -*- coding: utf-8 -*-
"""`W-G.9-270` 補令三 `§二-2`：**`p6` 沿 `s` 軸之交錯檢**（零生產碼）。

🔒 **受詞（補令三逐字）**：逐街廓，將**池片**與**配地宗**依其 `s` 區間排序，
   查**有無配地宗之 `s` 區間落於二池片之 `s` 區間<u>之間</u>**。

🔒 **款 `1`　識別鍵一律取 `s` 區間**（`N0-19`）——**⛔ 以連通分量、⛔ 以名稱、⛔ 以序號為鍵**。
🔒 **款 `2`　幾何與 `s` 皆自生產碼取**，**輸入以間諜法取自生產**：
   · 池片 ＝ `ns["_pool_strips_for_block"]` 之**回傳**（`stepg_pipeline.py:385` 所宣告之單一真相源）；
   · `s` 區間 ＝ `ns["_strip_s_range"](geom, d_hat, corner_pt, allocation_dir)`
     （`app.py:9201`·其 docstring 逐字「geom 全部頂點於**切線座標**（`_strip_axis`）上之 `(s_min, s_max)`」）；
     🔒 其 `d_hat`／`corner_pt`／`allocation_dir` **逐位取自間諜所錄之<u>同一次</u>呼叫實參**
     ⇒ **與 `_pool_strips_for_block` 內部所用之切線座標逐位同源**（⛔ 器內重導）。
   · 配地宗 ＝ `g_rows` 之 `推進側別 ∈ {left, right}` 者，其 `cut_coords`（生產所寫）。
🔒 **款 `3`　出艙**：逐街廓之 `s` 軸序列（逐項載**種類**〔池片／配地宗／角落抵費地〕、`s` 起訖、面積）。
🔒 **款 `4`　判別力二造**：人造一序列使配地宗**夾於二池片之間** ⇒ 須判**有交錯**；
   人造一序列使池片**全部相鄰** ⇒ 須判**無交錯**。**二造同色 ⇒ 閘失能·停機**（`rc = 5`）。
🛑 **款 `5`　⛔ 判其為缺陷、⛔ 作任何處置主張**——**應然係 KL 所述**，量得之事實候發單側與 KL。
🛑 **款 `6`　⛔ 動生產碼一字**（本器之包裹逐位原樣回傳）。

🔒 **「角落抵費地」之識別**（沿用 `p5`·⛔ 推定）：池片全集中，面積**唯一相符**於**正典落檔**
   `got_抵費地_*.csv`（其 `指配` 欄逐字 `強制抵費地`）者；容差**具名** ＝ `0.005 ㎡`（`2dp` 之半個單位）。
   🛑 `0` 或 `≥2` 候選 ⇒ **loud 拒測**（`rc = 4`）。

🔒 **二框並報（⛔ 自裁其一）**：`交錯` 之判同時以二框出艙——
   `框甲` ＝ **全部池片**（含角落抵費地）之間；`框乙` ＝ **僅中央池之片**之間。

用法：`python verify/probes/probe_WG9270R4_p6_interleave.py [倉根]`
`rc`：`0`／`3` 母體為 `0`／`4` 角落抵費地之相符非唯一／`5` **量測器紅**。
"""
import ast as _ast
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
import probe_WG9269_c4_gamma as G4                                  # noqa: E402

BT = chr(96)
W = 122
SBS = (0.0, 3.5)
TOL_AREA = 0.005
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]


def say(s=""):
    print(s)


def drive_spy(sb):
    """驅動一次；錄 `_pool_strips_for_block` 之**實參 ＋ 回傳**，並回 `g_rows` 之 CSV 形。"""
    ns, fake_st = harvest()
    rec = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label="", _depth=None, _verbose=True):
        out = _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                    _label=_label, _depth=_depth, _verbose=_verbose)
        rec[str(_label)] = {"d_hat": d_hat, "corner_pt": corner_pt,
                            "alloc": allocation_dir, "pieces": list(out)}
        return out                      # 🛑 逐位原樣回傳（⛔ 改一字）

    ns["_pool_strips_for_block"] = _spy

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
    g_rows = []
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
    return ns, rec, rows


def forced_offsets(tag):
    p = os.path.join(REPO, "verify", "out", "got_抵費地_退縮%s.csv" % tag)
    if not os.path.exists(p):
        return {}, "🛑 `%s` ⛔ 存在" % os.path.basename(p)
    with io.open(p, "r", encoding="utf-8-sig", newline="") as f:
        rr = list(csv.DictReader(f))
    hdr = list(rr[0].keys()) if rr else []
    kb = next((h for h in hdr if "街廓" in h), None)
    ka = next((h for h in hdr if "面積" in h), None)
    m = {}
    for r in rr:
        m.setdefault((r.get(kb) or "").strip(), []).append(float(r.get(ka) or 0.0))
    return m, "✅ 自 `%s` 取得 **%d** 列" % (os.path.basename(p), len(rr))


def interleave(items, pool_kinds):
    """`items` ＝ [(s0, s1, kind, name, area)]（已依 `s0` 升冪）。

    判「**有交錯**」⇔ 在 `s` 序中，**二屬 `pool_kinds` 之項之間夾有至少一個 `配地宗`**。
    回 `(是否交錯, [被夾之配地宗之名])`。
    """
    pos = [i for i, it in enumerate(items) if it[2] in pool_kinds]
    if len(pos) < 2:
        return False, []
    lo, hi = pos[0], pos[-1]
    sand = [items[i][3] for i in range(lo + 1, hi) if items[i][2] == "配地宗"]
    return (len(sand) > 0), sand


def main():
    from shapely.geometry import Polygon as _P
    say("=" * W)
    say("【`W-G.9-270` 補令三 `§二-2`】**`p6` 沿 `s` 軸之交錯檢**")
    say("=" * W)
    say("🛑 **⛔ 判其為缺陷、⛔ 作任何處置主張**——應然係 KL 所述，量得之事實候發單側與 KL。")
    say("🔒 識別鍵一律取 **`s` 區間**（`N0-19`）·⛔ 連通分量／名稱／序號")
    say("")

    # ── 判別力二造（**先於**任何實測）──────────────────────────────────
    say("─" * W)
    say("【判別力二造】（款 `4`·二造同色 ⇒ 閘失能·停機）")
    say("─" * W)
    seq_a = [(0.0, 10.0, "池片", "P1", 10.0),
             (10.0, 20.0, "配地宗", "L1", 10.0),
             (20.0, 30.0, "池片", "P2", 10.0)]
    seq_b = [(0.0, 10.0, "池片", "P1", 10.0),
             (10.0, 20.0, "池片", "P2", 10.0),
             (20.0, 30.0, "配地宗", "L1", 10.0)]
    ia, sa = interleave(seq_a, {"池片"})
    ib, sb_ = interleave(seq_b, {"池片"})
    say("   造甲［配地宗**夾於二池片之間**：`P1 | L1 | P2`］⇒ 判 **%s**（被夾者 %s）⇒ %s"
        % ("有交錯" if ia else "無交錯", sa, "✅" if ia else "🔴"))
    say("   造乙［池片**全部相鄰**：`P1 | P2 | L1`］⇒ 判 **%s**（被夾者 %s）⇒ %s"
        % ("有交錯" if ib else "無交錯", sb_, "✅" if not ib else "🔴"))
    if not (ia and not ib):
        say("   🛑 **二造同色／不如預期 ⇒ 閘失能** ⇒ 停機")
        sys.exit(5)
    say("   ⇒ **器非紅**（一造有交錯、一造無交錯）✅")
    say("")

    for sb in SBS:
        tag = "%gm" % sb
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        ns, rec, rows = drive_spy(sb)
        _ssr = ns["_strip_s_range"]
        say("🔒 間諜所錄之街廓 ＝ **%d**：%s｜`g_rows` ＝ **%d** 列"
            % (len(rec), "／".join(sorted(rec)), len(rows)))
        if not rec:
            say("🛑 母體 `0` ⇒ **loud 拒測**")
            sys.exit(3)
        fo, fdiag = forced_offsets(tag)
        say("🔒 強制抵費地（**正典落檔**）：%s｜%s"
            % (fdiag, "／".join("%s %s" % (b, a) for b, a in sorted(fo.items()))))
        say("")

        for blk in BLKS:
            if blk not in rec:
                say("   🛑 `%s` ⛔ 在間諜所錄之母體 ⇒ 其量 **⛔ 可得**" % blk)
                continue
            d = rec[blk]
            pieces = d["pieces"]
            areas = [float(g.area) for g in pieces]
            # 角落抵費地之識別（唯一相符·⛔ 推定）
            drop = set()
            for fa in fo.get(blk, []):
                cand = [i for i, a in enumerate(areas)
                        if i not in drop and abs(a - fa) <= TOL_AREA]
                if len(cand) != 1:
                    say("   🛑 `%s` 強制抵費地 `%.2f` 之相符候選 ＝ %d（期 `1`）⇒ **loud 拒測**"
                        % (blk, fa, len(cand)))
                    sys.exit(4)
                drop.add(cand[0])

            items = []
            bad = 0
            for i, g in enumerate(pieces):
                r = _ssr(g, d["d_hat"], d["corner_pt"], d["alloc"])
                if r is None:
                    bad += 1
                    continue
                kind = "角落抵費地" if i in drop else "池片"
                items.append((float(r[0]), float(r[1]), kind,
                              "%s-池#%d" % (blk, i + 1), areas[i]))
            for r0 in rows:
                if (r0.get("所屬街廓") or "").strip() != blk:
                    continue
                side = (r0.get("推進側別") or "").strip()
                if side not in ("left", "right"):
                    continue
                cc = (r0.get("cut_coords") or "").strip()
                try:
                    v = [(float(a), float(b)) for a, b in _ast.literal_eval(cc)] if cc else []
                except Exception:                                   # noqa: BLE001
                    v = []
                if len(v) < 3:
                    bad += 1
                    continue
                pp = _P(v)
                if not pp.is_valid:
                    pp = pp.buffer(0)
                r = _ssr(pp, d["d_hat"], d["corner_pt"], d["alloc"])
                if r is None:
                    bad += 1
                    continue
                items.append((float(r[0]), float(r[1]), "配地宗",
                              (r0.get("暫編地號") or "?").strip(), float(pp.area)))
            items.sort(key=lambda t: (t[0], t[1]))

            say("   ── `%s` ──（項 **%d**：池片 %d／角落抵費地 %d／配地宗 %d；`s` 不可得 %d）"
                % (blk, len(items),
                   sum(1 for x in items if x[2] == "池片"),
                   sum(1 for x in items if x[2] == "角落抵費地"),
                   sum(1 for x in items if x[2] == "配地宗"), bad))
            say("      %-4s %-14s %-22s %-14s %-14s %s"
                % ("#", "種類", "名", "s 起", "s 迄", "面積(㎡)"))
            for k, (s0, s1, kind, nm, ar) in enumerate(items, 1):
                say("      %-4d %-14s %-22s %-14.6f %-14.6f %.6f" % (k, kind, nm, s0, s1, ar))
            ia1, sa1 = interleave(items, {"池片", "角落抵費地"})
            ia2, sa2 = interleave(items, {"池片"})
            say("      🔑 **框甲**（全部池片·含角落抵費地）⇒ **%s**%s"
                % ("🔴 有交錯" if ia1 else "🟢 無交錯",
                   "；被夾之配地宗 ＝ %s" % sa1 if sa1 else ""))
            say("      🔑 **框乙**（僅中央池之片）⇒ **%s**%s"
                % ("🔴 有交錯" if ia2 else "🟢 無交錯",
                   "；被夾之配地宗 ＝ %s" % sa2 if sa2 else ""))
            say("")

    say("=" * W)
    say("🛑 **本器⛔ 判其為缺陷、⛔ 作任何處置主張**——量得之事實候發單側與 KL。")
    sys.exit(0)


if __name__ == "__main__":
    main()
