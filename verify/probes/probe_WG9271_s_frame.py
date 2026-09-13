# -*- coding: utf-8 -*-
"""`W-G.9-271` `§二-2`：**`s` 框之同源性**（零生產碼·本批之主檢）。

🔒 **器之底本** ＝ `verify/probes/probe_WG9270R4_p6_interleave.py` 之 `drive_spy`
   （⛔ 另寫第二份判準、⛔ 器內重導切線座標）。
   其 `d_hat`／`corner_pt`／`allocation_dir` 逐位取自**間諜所錄之同一次呼叫實參**。

🔒 **三組對拍**（單 `§二-2` 逐字）

   | 組 | 池側 | 宗側 |
   |---|---|---|
   | 甲 | 間諜所錄之**回傳** pieces | **同一次呼叫所錄之 `biz_polys`** |
   | 乙 | 同上 | `g_rows` 之 `cut_coords`（＝ `p6` 之取法） |
   | 丙 | — | **同宗之二形**（`biz_polys` vs `cut_coords`）逐宗對拍其 `s` 區間之差 |

🔒 **準據（發單側定·⛔ CC 自訂·`自解款` 黑名單）**
   · 重疊長 ＝ `max(0, min(b, y) - max(a, x))`；
   · 容差**取 `app.py` 之 `_S_EPS`**（**自 `ns` 取值**·⛔ 器內另定常數）；
   · **組甲之逐片重疊長須全為 `0`**（＝ 池片確為 `biz_polys` 之 `s` 區間聯集之補區間·
     `_pool_strips_for_block` 步驟 `4` 逐字）；
   · 組甲⛔ 全為 `0` ⇒ **逐片具名**其重疊長與重疊之宗，**⛔ 判其孰誤**。

🔒 **判別力二造**（施於重疊式本身）
   甲[必重疊] 任一宗之區間與**其自身**對拍 ⇒ 重疊長 ＝ 其長（`>0`）；
   乙[必不重疊] 一**人造區間**（**執行期組出**·字面⛔ 出艙）置於 `s` 域之外 ⇒ `0`。
   ⇒ **二造異色方為器非紅**；不如預期 ⇒ `rc = 5` loud 拒測。

🛑 **⛔ 判 `p6` 之結論作廢、⛔ 判「交錯」之有無**——**出艙即止**。
🛑 **⛔ 動生產碼一字**（本器之包裹逐位原樣回傳）。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9271_s_frame.py [倉根]`
`rc`：`0` 量測成立／`3` 母體為 `0`／`5` **量測器紅**。
🛑 `rc != 0` ⛔ 等同「受詞紅」（本機坑 `9`）。
"""
import ast as _ast
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

BT = chr(96)
W = 124
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]


def say(s=""):
    print(s)


def ov(a, b, x, y):
    """重疊長 ＝ `max(0, min(b, y) - max(a, x))`（單 `§二-2` 準據·逐字）。"""
    return max(0.0, min(b, y) - max(a, x))


def drive_spy(sb):
    """驅動一次；錄 `_pool_strips_for_block` 之**全部**呼叫（實參 ＋ `biz_polys` ＋ 回傳）。

    🔒 底本之 `rec[str(_label)] = {...}` 會**覆寫**重複呼叫 ⇒ 本器改錄 **list**，
      使「一街廓一情境被呼叫 `>1` 次」可見（單 `§二-2` 末款所令）。
    """
    ns, fake_st = harvest()
    rec = {}
    _orig = ns["_pool_strips_for_block"]

    def _spy(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
             _label="", _depth=None, _verbose=True):
        out = _orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                    _label=_label, _depth=_depth, _verbose=_verbose)
        rec.setdefault(str(_label), []).append(
            {"block_poly": block_poly,
             "d_hat": d_hat, "corner_pt": corner_pt, "alloc": allocation_dir,
             "biz": list(biz_polys or []), "pieces": list(out)})
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


def cut_polys(rows, blk):
    """`g_rows` 之 `cut_coords` ⇒ [(名, Polygon)]（＝ `p6` 之取法）。"""
    from shapely.geometry import Polygon as _P
    out = []
    for r0 in rows:
        if (r0.get("所屬街廓") or "").strip() != blk:
            continue
        if (r0.get("推進側別") or "").strip() not in ("left", "right"):
            continue
        cc = (r0.get("cut_coords") or "").strip()
        try:
            v = [(float(a), float(b)) for a, b in _ast.literal_eval(cc)] if cc else []
        except Exception:                                           # noqa: BLE001
            v = []
        if len(v) < 3:
            continue
        pp = _P(v)
        if not pp.is_valid:
            pp = pp.buffer(0)
        out.append(((r0.get("暫編地號") or "?").strip(), pp))
    return out


def sranges(ssr, polys, d):
    """逐幾何取 `s` 區間；`None` 者具名為不可得（⛔ 靜默丟）。"""
    got, bad = [], 0
    for nm, g in polys:
        r = ssr(g, d["d_hat"], d["corner_pt"], d["alloc"])
        if r is None:
            bad += 1
            continue
        got.append((nm, float(r[0]), float(r[1]), float(g.area)))
    return got, bad


def main():
    say("=" * W)
    say("【`W-G.9-271` `§二-2`】**`s` 框之同源性**（本批之主檢·**出艙即止**）")
    say("=" * W)
    say("🛑 **⛔ 判 `p6` 之結論作廢、⛔ 判「交錯」之有無**——量得之事實候發單側。")

    # ── 判別力二造（**先於**任何實測·施於重疊式本身）────────────────────
    say("")
    say("─" * W)
    say("【判別力二造】（單 `§二-2` 所令·二造同色 ⇒ 器紅·`rc = 5`）")
    say("─" * W)
    a0, a1 = 12.5, 37.5
    g_self = ov(a0, a1, a0, a1)
    off = a1 + 1000.0                       # 人造區間（**執行期組出**·字面⛔ 出艙）
    g_off = ov(a0, a1, off, off + 1.0)
    say("   造甲[必重疊] 一宗之區間與**其自身**對拍 ⇒ 重疊長 ＝ %.6f（其長 ＝ %.6f）⇒ %s"
        % (g_self, a1 - a0, "✅" if g_self > 0 else "🔴"))
    say("   造乙[必不重疊] 一人造區間置於 `s` 域外 ⇒ 重疊長 ＝ %.6f ⇒ %s"
        % (g_off, "✅" if g_off == 0.0 else "🔴"))
    if not (g_self > 0 and g_off == 0.0):
        say("   🛑 **二造同色／不如預期 ⇒ 器紅** ⇒ loud 拒測")
        return 5
    say("   ⇒ **器非紅**（一造 `>0`、一造 `= 0`）✅")

    rc = 0
    for sb in SBS:
        tag = "%gm" % sb
        say("")
        say("─" * W)
        say("【情境 `退縮 %s`】" % tag)
        say("─" * W)
        ns, rec, rows = drive_spy(sb)
        eps = float(ns["_S_EPS"])           # 🔒 容差自 `ns` 取值·⛔ 器內另定常數
        ssr = ns["_strip_s_range"]
        say("🔒 容差 ＝ `_S_EPS`（**自 `ns` 取值**）＝ %r" % eps)
        say("🔒 間諜所錄之 `_label` ＝ **%d** 個：%s｜`g_rows` ＝ **%d** 列"
            % (len(rec), "／".join(sorted(rec)), len(rows)))
        if not rec:
            say("🛑 母體 `0` ⇒ **loud 拒測**")
            return 3

        say("")
        say("── 呼叫次數（逐街廓·本情境）")
        say("   | `_label` | 呼叫次數 | 逐次之回傳片數 |")
        say("   |---|---|---|")
        for lb in sorted(rec):
            say("   | `%s` | **%d** | %s |"
                % (lb, len(rec[lb]), ", ".join(str(len(c["pieces"])) for c in rec[lb])))
        multi = [lb for lb in sorted(rec) if len(rec[lb]) > 1]
        if multi:
            say("")
            say("   🔴 **被呼叫 `>1` 次者 ＝ %s** ⇒ 逐次分列其實參：" % multi)
            for lb in multi:
                for k, c in enumerate(rec[lb], 1):
                    say("     · `%s` 第 %d 次｜`corner_pt` ＝ %r｜`d_hat` ＝ %r｜"
                        "`allocation_dir` ＝ %r｜回傳片數 ＝ %d｜`biz_polys` ＝ %d"
                        % (lb, k, c["corner_pt"], c["d_hat"], c["alloc"],
                           len(c["pieces"]), len(c["biz"])))
        else:
            say("   ⇒ 無一街廓被呼叫 `>1` 次。")

        for blk in BLKS:
            if blk not in rec:
                say("")
                say("   🛑 `%s` ⛔ 在間諜所錄之母體 ⇒ 其量 **⛔ 可得**" % blk)
                continue
            d = rec[blk][-1]                # 🔒 取**末一次**；其上已逐次出艙
            pieces = [("%s-池#%d" % (blk, i + 1), g) for i, g in enumerate(d["pieces"])]
            biz = [("%s-biz#%d" % (blk, i + 1), g) for i, g in enumerate(d["biz"])]
            cut = cut_polys(rows, blk)

            P, bp = sranges(ssr, pieces, d)
            B, bb = sranges(ssr, biz, d)
            C, bc = sranges(ssr, cut, d)
            say("")
            say("   ══ `%s` ══  池片 %d（`s` 不可得 %d）／`biz_polys` %d（%d）／`cut_coords` %d（%d）"
                % (blk, len(P), bp, len(B), bb, len(C), bc))

            for grp, Q, qn in (("甲", B, "biz_polys（**同一次呼叫所錄**）"),
                               ("乙", C, "g_rows 之 cut_coords（＝ `p6` 之取法）")):
                pairs = []
                for pn, p0, p1, pa in P:
                    tot = 0.0
                    hit = []
                    for qnm, q0, q1, qa in Q:
                        o = ov(p0, p1, q0, q1)
                        if o > eps:
                            tot += o
                            hit.append((qnm, o))
                    pairs.append((pn, p0, p1, pa, tot, hit))
                nz = [x for x in pairs if x[4] > 0.0]
                say("      ── 組 %s（池側 ＝ 回傳 pieces｜宗側 ＝ %s）" % (grp, qn))
                say("         逐片重疊長 `> _S_EPS` 者 ＝ **%d** ／ %d 片"
                    % (len(nz), len(pairs)))
                if grp == "甲":
                    say("         🔒 **準據：組甲之逐片重疊長須全為 `0`** ⇒ %s"
                        % ("🟢 **成立**" if not nz else "🔴 **⛔ 成立**"))
                if nz:
                    say("         | 池片 | `s` 起 | `s` 迄 | 面積(㎡) | Σ重疊長 | 重疊之宗（名: 重疊長） |")
                    say("         |---|---|---|---|---|---|")
                    for pn, p0, p1, pa, tot, hit in nz:
                        say("         | `%s` | %.6f | %.6f | %.4f | **%.6f** | %s |"
                            % (pn, p0, p1, pa, tot,
                               "; ".join("%s: %.6f" % (h[0], h[1]) for h in hit[:6])))
                    say("         🛑 **⛔ 判其孰誤**——照實具名（單 `§二-2` 明令）。")

            # ── 組丙：同宗之二形逐宗對拍（配對法具名） ────────────────────
            say("      ── 組 丙（`biz_polys` vs `cut_coords` 之同宗二形·逐宗對拍 `s` 區間之差）")
            say("         🔒 **配對法（具名·⛔ 隱含）**：對每一 `cut_coords` 之宗，"
                "取其與各 `biz_polys` 之 `s` 區間**重疊長最大**者為配對；")
            say("            重疊長皆 `<= _S_EPS` 者具名為 **無配對**（⛔ 靜默丟）。")
            used = set()
            say("         | `cut_coords` 之宗 | 配對之 `biz` | Δ`s` 起 | Δ`s` 迄 | Δ面積(㎡) |")
            say("         |---|---|---|---|---|")
            nopair = []
            for cn, c0, c1, ca in C:
                best, bo = None, 0.0
                for i, (bn, b0, b1, ba) in enumerate(B):
                    o = ov(c0, c1, b0, b1)
                    if o > bo:
                        best, bo = i, o
                if best is None or bo <= eps:
                    nopair.append(cn)
                    continue
                used.add(best)
                bn, b0, b1, ba = B[best]
                say("         | `%s` | `%s` | %+.9f | %+.9f | %+.6f |"
                    % (cn, bn, c0 - b0, c1 - b1, ca - ba))
            if nopair:
                say("         🔴 **無配對之 `cut_coords` 宗 ＝ %d**：%s" % (len(nopair), nopair))
            un = [B[i][0] for i in range(len(B)) if i not in used]
            if un:
                say("         🔴 **未被配對之 `biz_polys` ＝ %d**：%s" % (len(un), un))
            if not nopair and not un:
                say("         ⇒ 二形**逐宗一一對應**（無殘餘）。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
