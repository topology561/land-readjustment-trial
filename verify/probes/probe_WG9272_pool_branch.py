# -*- coding: utf-8 -*-
"""`W-G.9-272` `§三-1`：**池片產生分支之歸屬**（零生產碼·**本批主檢**·出艙即止）。

🔒 **器之底本** ＝ `verify/probes/probe_WG9271_s_frame.py` 之 `drive_spy`
   （⛔ 另寫第二份判準、**⛔ 器內重算 `pool_iv`**——重算即第二份判準）。

🔒 **分支之判準（發單側定·⛔ CC 自訂·`自解款` 黑名單）**
   · **包裹 `ns["_block_strip"]`**，錄其每次呼叫之**回傳幾何**（逐情境·逐街廓）。
   · 對每一**最終回傳之池片**：若其幾何與**某次 `_block_strip` 回傳**逐位相同
     （判準 ＝ `equals_exact(tol=0)`；**⛔ 以面積代幾何**），判為 **步驟 `5`**；
     否則判為 **「⛔ 步驟 `5`」**。
   · 🛑 **⛔ 逕稱其為「步驟 `5b`」**——本器只證其⛔ 為步驟 `5`；
     「是否為 `5b`」須另證，本批**⛔ 斷**（⛔ 以二分法充窮舉）。
   · 既⛔ 等於任何 `_block_strip` 回傳、亦⛔ 可歸因者 ⇒ **第三種出艙碼**
     （⛔ 與「判定為偽」共用）。

🔒 **判別力二造**
   甲[必為步驟 `5`] ＝ `R3` 之唯一片（二情境皆一片）須判為 **步驟 `5`**；
   乙[必⛔ 步驟 `5`] ＝ `R1-池#2`（`0.0046 ㎡`）須判為 **⛔ 步驟 `5`**。
   **二造同判 ⇒ `rc = 5` loud 拒測。**

🛑 **⛔ 判其為缺陷、⛔ 判 `p6` 之結論、⛔ 提任何處置主張**——**出艙即止**。
🛑 **⛔ 動生產碼一字**（本器之包裹逐位原樣回傳）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9272_pool_branch.py [倉根]`
`rc`：`0`／`3` 母體為 `0`／`5` **量測器紅**。
🛑 `rc != 0` ⛔ 等同「受詞紅」。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
VERIFY = os.path.join(REPO, "verify")
sys.path.insert(0, VERIFY)
sys.path.insert(0, HERE)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402
import probe_WG9269_c4_gamma as G4                                  # noqa: E402
import probe_WG9271_s_frame as SF                                   # noqa: E402

W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
# 🔒 生產碼註解所載之實測（**照實並列**·🛑 ⛔ 判孰誤、⛔ 追改該註解一字）
CODE_NOTE = "實測 `0m/3.5m R4` 各 `58.4792㎡`、`3.5m R1` `5.3881㎡`"


def say(s=""):
    print(s)


def drive(sb):
    """承 `SF.drive_spy`，**另包裹 `ns["_block_strip"]`** 以錄其每次回傳之幾何。"""
    ns, fake_st = harvest()
    rec = {}
    strips = []                      # [(幾何, 面積)]·全域（⛔ 分街廓——其呼叫者不具 label）
    _orig_pool = ns["_pool_strips_for_block"]
    _orig_strip = ns["_block_strip"]

    def _spy_strip(block_poly, d_hat, baseline_pt, S, allocation_dir=None, n_hat_far=None):
        out = _orig_strip(block_poly, d_hat, baseline_pt, S,
                          allocation_dir=allocation_dir, n_hat_far=n_hat_far)
        try:
            g = out[0]
            if g is not None and not g.is_empty:
                strips.append(g)
        except Exception:                                           # noqa: BLE001
            raise                       # 🛑 ⛔ 靜默吞（`no-silent-fallback`）
        return out                      # 🛑 逐位原樣回傳（⛔ 改一字）

    def _spy_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                  _label="", _depth=None, _verbose=True):
        n0 = len(strips)
        out = _orig_pool(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                         _label=_label, _depth=_depth, _verbose=_verbose)
        rec.setdefault(str(_label), []).append(
            {"block_poly": block_poly, "d_hat": d_hat, "corner_pt": corner_pt,
             "alloc": allocation_dir, "biz": list(biz_polys or []),
             "pieces": list(out), "strips": list(strips[n0:])})
        return out                      # 🛑 逐位原樣回傳

    ns["_block_strip"] = _spy_strip
    ns["_pool_strips_for_block"] = _spy_pool

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


def branch_of(piece, strips):
    """`equals_exact(tol=0)` ⇒ 步驟 `5`；否則「⛔ 步驟 `5`」。⛔ 以面積代幾何。"""
    for k, g in enumerate(strips):
        try:
            if piece.equals_exact(g, 0.0):
                return "步驟 5", k
        except Exception:                                           # noqa: BLE001
            raise                       # 🛑 ⛔ 靜默吞
    return "⛔ 步驟 5", None


def main():
    say("=" * W)
    say("【`W-G.9-272` `§三-1`】**池片產生分支之歸屬**（本批主檢·**出艙即止**）")
    say("=" * W)
    say("🛑 **⛔ 判其為缺陷、⛔ 判 `p6` 之結論、⛔ 提任何處置主張。**")
    say("🛑 **⛔ 逕稱「⛔ 步驟 `5`」者為「步驟 `5b`」**——本器只證其⛔ 為步驟 `5`。")
    say("🔒 判準 ＝ `equals_exact(tol=0)`（**⛔ 以面積代幾何**）；"
        "包裹 ＝ `ns[\"_block_strip\"]` 之每次回傳。")

    verdicts = {}       # (tag, blk, 名) -> 判
    tot_not5 = {}
    rc = 0
    for sb in SBS:
        tag = "%gm" % sb
        say("")
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        ns, rec, rows = drive(sb)
        ssr = ns["_strip_s_range"]
        bstrip = ns["_block_strip"]     # ⚠️ 已被包裹；其回傳仍逐位原樣（末欄取法用之）
        say("🔒 間諜所錄之 `_label` ＝ **%d** 個：%s｜`g_rows` ＝ **%d** 列"
            % (len(rec), "／".join(sorted(rec)), len(rows)))
        if not rec:
            say("🛑 母體 `0` ⇒ **loud 拒測**")
            return 3
        s_not5 = 0.0
        for blk in BLKS:
            if blk not in rec:
                say("   🛑 `%s` ⛔ 在間諜所錄之母體 ⇒ 其量 **⛔ 可得**" % blk)
                continue
            d = rec[blk][-1]
            strips = d["strips"]
            cut = SF.cut_polys(rows, blk)
            C, badc = SF.sranges(ssr, cut, d)
            say("")
            say("   ══ `%s` ══  池片 %d｜本次呼叫內之 `_block_strip` 回傳 %d｜配地宗 %d（`s` 不可得 %d）"
                % (blk, len(d["pieces"]), len(strips), len(C), badc))
            say("   | 池片 | 面積(㎡) | `s` 起 | `s` 迄 | **分支判** | 其所落入之宗 | 該宗之 `s` 帶全深度面積 − 其多邊形面積 (㎡) |")
            say("   |---|---|---|---|---|---|---|")
            for i, g in enumerate(d["pieces"]):
                nm = "%s-池#%d" % (blk, i + 1)
                r = ssr(g, d["d_hat"], d["corner_pt"], d["alloc"])
                if r is None:
                    say("   | `%s` | %.4f | —— | —— | 🛑 **第三種出艙碼：`s` 不可得** | —— | —— |"
                        % (nm, float(g.area)))
                    verdicts[(tag, blk, nm)] = "⛔ 可歸因"
                    continue
                p0, p1 = float(r[0]), float(r[1])
                v, k = branch_of(g, strips)
                verdicts[(tag, blk, nm)] = v
                host, delta = "——", "——"
                if v != "步驟 5":
                    s_not5 += float(g.area)
                    # 其所落入之宗 ＝ `s` 區間重疊長最大者
                    best, bo = None, 0.0
                    for cn, c0, c1, ca in C:
                        o = SF.ov(p0, p1, c0, c1)
                        if o > bo:
                            best, bo = (cn, c0, c1, ca), o
                    if best is None:
                        host = "🛑 **第三種出艙碼：⛔ 可歸因**"
                        verdicts[(tag, blk, nm)] = "⛔ 可歸因"
                    else:
                        cn, c0, c1, ca = best
                        # 末欄：以 `_block_strip`（**同一組切線**）切該宗 `s` 帶之全深度帶
                        import numpy as _np
                        bp = (_np.asarray(d["corner_pt"], dtype=float)
                              + c0 * _np.asarray(d["d_hat"], dtype=float))
                        bg, _ar = bstrip(d["block_poly"], d["d_hat"], bp, c1 - c0,
                                         allocation_dir=d["alloc"])
                        if bg is None or bg.is_empty:
                            host, delta = "`%s`" % cn, "🛑 **帶不可得**"
                        else:
                            host = "`%s`" % cn
                            delta = "**%+.4f**" % (float(bg.area) - ca)
                say("   | `%s` | %.4f | %.6f | %.6f | **%s** | %s | %s |"
                    % (nm, float(g.area), p0, p1, v, host, delta))
        tot_not5[tag] = s_not5

    # ── 判別力二造（**事後**施於實測之判·二造同判 ⇒ 器紅）──────────────
    say("")
    say("─" * W)
    say("【判別力二造】（單 `§三-1`·二造同判 ⇒ `rc = 5` loud 拒測）")
    say("─" * W)
    a = [v for (t, b, n), v in verdicts.items() if b == "R3"]
    bb = [v for (t, b, n), v in verdicts.items() if n == "R1-池#2"]
    say("   造甲[必為步驟 `5`] ＝ `R3` 之片（二情境）⇒ 判 %s ⇒ %s"
        % (a, "✅" if a and all(x == "步驟 5" for x in a) else "🔴"))
    say("   造乙[必⛔ 步驟 `5`] ＝ `R1-池#2`（二情境）⇒ 判 %s ⇒ %s"
        % (bb, "✅" if bb and all(x != "步驟 5" for x in bb) else "🔴"))
    ok = (a and all(x == "步驟 5" for x in a)) and (bb and all(x != "步驟 5" for x in bb))
    if not ok:
        say("   🛑 **二造同判／不如預期 ⇒ 器紅** ⇒ loud 拒測")
        return 5
    say("   ⇒ **器非紅**（二造異判）✅")

    # ── 併出艙：「⛔ 步驟 `5`」之片之面積合計 ─────────────────────────
    say("")
    say("─" * W)
    say("【「⛔ 步驟 `5`」之片之面積合計】（🛑 **⛔ 判孰誤、⛔ 追改生產碼註解一字**）")
    say("─" * W)
    say("   | 情境 | 「⛔ 步驟 `5`」之片數 | 面積合計(㎡) |")
    say("   |---|---|---|")
    for tag in ("0m", "3.5m"):
        cnt = sum(1 for (t, b, n), v in verdicts.items() if t == tag and v != "步驟 5")
        say("   | `%s` | **%d** | **%.4f** |" % (tag, cnt, tot_not5.get(tag, 0.0)))
    say("")
    say("   🔒 **生產碼註解所載（逐字·照實並列）**：%s" % CODE_NOTE)
    say("   🛑 **受詞可能相異** ⇒ **⛔ 判孰誤、⛔ 追改該註解一字**；照實具名。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
