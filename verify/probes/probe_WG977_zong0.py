# -*- coding: utf-8 -*-
r"""**W-G.9-77 §二 A 組**：`宗0` 之 `cut_coords` **構造定位**（⛔ **只量不修**）。

## 受詞（施工單 `W-G.9-77` §二）
- **A-1** `宗0` 之 `cut_coords` 由**哪一行**產生 ⇒ 一條**無斷鏈**之逐行鏈；
  併以**三路互證** `宗0` 是否為**街角第 1 宗**（⛔ 不以單一路推定）。
- **A-2** 六塊 × 兩情境，逐宗出艙 `i`／`暫編地號`／`s_min`／`s_max`／`s 跨距`／
  `與宗0之s區間是否重疊`／`面積`；並出艙 `宗0 跨距 ÷ 其餘各宗跨距中位數` 之**倍數**，
  以及 `宗0` 之 s 區間**含住幾宗**（完全含／部分含·逐宗列名）。
  🔒 **判別力對照**：未破閘之塊其倍數**須顯著較小**；若不然 ⇒ **具名**。
- **A-3** 若 `宗0` 為街角第 1 宗 ⇒ 其 `cut_coords` 與**街角規定範圍多邊形**之幾何關係
  （`範圍 ⊆ 宗0`？`宗0 ⊆ 範圍`？交集／各自／對稱差面積）。⚠️ **係觀察·⛔ 非判準**。

## 🔒 A-0　錯誤方向之**事前選定**（施工單 §二 A-0·節 98·⛔ 寫碼前先寫下）
本探針係**歸因**工具 ⇒ 其瑕疵若往「**把 `宗0` 說得比實際正常**」錯，會使成因看起來已被解釋。
⇒ 🔒 **事前選定：偏向「多報異常」**——凡量得之量與其他宗**不同型**者一律列出並具名，
   ⛔ 不得以「可能是正常的」為由略過；⛔ 不設任何「差異太小就不列」之門檻。

## 🔒 量法：**三個唯讀 spy**（⛔ 原樣轉呼叫、原樣回傳·⛔ 不改任何值）
| spy | 記什麼 | 為何是它 |
|---|---|---|
| `_solve_G_one` | **以回傳 dict 之 `id()` 為鍵**記 `is_corner` 實參／`side`／`side_mid` 有無／傳入 `allocation_dir`／回傳 `_alloc_dir_used`／`solver_label`／`len(cut_coords)` | 🔒 `id()` 使「哪一次呼叫 → 哪一宗」**精確對應**，⛔ 非按序猜配 |
| `_build_corner_range_v3` | 以 `(_label, _side)` 記回傳之**街角規定範圍多邊形** | A-3 之受詞；⛔ 不自行重建（重建即另一套參數） |
| `_pool_strips_for_block` | 最終 `_biz` ＋ 自呼叫端 frame 取 `left_results`／`right_results` 以對齊**暫編地號**與 `_res` 物件 | 與 `W-G.9-76` 同法（該法已驗「✅ 逐位對齊」12/12） |

## 🔒 「宗之序」與 s 之原語（承 `W-G.9-76`·⛔ 不另立第二種）
- 序 ＝ `left_results + right_results` **分組串接**（⛔ 非空間序）。
- s ＝ `ns['_strip_s_range']`（`_strip_axis` 斜交切線軸）；恆等式 `s(corner_pt + s0·d̂) ≡ s0`。

## ⛔ 本檔不做
⛔ 零 `app.py` 變更；⛔ 不修 `②-宗` 閘、不調上界、不改任何容差；
⛔ 不改任何 `cut_coords` 產生端；⛔ **不對成因下「這是 bug」之結論**（施工單 §七-3）；
⛔ 不接入 `run_all`；⛔ 不覆寫任何既有 log（檔名含產生它之 commit 短碼）。
"""
import contextlib
import io
import math
import os
import statistics
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402
from stepg_pipeline import run_step_g                               # noqa: E402

from shapely.geometry import Polygon as SPoly                       # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
W = 200
ANG_TOL_DEG = 0.05          # 🔒 「方向相同」之事前定義（度）——⛔ 看結果前寫下


def _short_head():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=REPO).decode().strip()
    except Exception:                                               # noqa: BLE001
        return "UNKNOWN"


COMMIT = _short_head()
LOG = os.path.join(OUTDIR, "probe_WG977_zong0_%s.log" % COMMIT)


# ── 原語 ────────────────────────────────────────────────────────────────
def _ang(u, v):
    """兩向量之**無向**夾角（度）·0〜90。None ⇒ nan。"""
    if u is None or v is None:
        return float("nan")
    a = np.asarray(u, dtype=float)[:2]
    b = np.asarray(v, dtype=float)[:2]
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na < 1e-12 or nb < 1e-12:
        return float("nan")
    c = abs(float(np.dot(a, b)) / (na * nb))
    return math.degrees(math.acos(min(1.0, c)))


def _poly(coords):
    try:
        if coords is None or len(coords) < 3:
            return None
        p = SPoly([(float(c[0]), float(c[1])) for c in coords])
        if not p.is_valid:
            p = p.buffer(0)
        return None if (p is None or p.is_empty) else p
    except Exception:                                               # noqa: BLE001
        return None


def _rot90cw(v):
    a = np.asarray(v, dtype=float)[:2]
    n = float(np.linalg.norm(a))
    if n < 1e-12:
        return None
    a = a / n
    return (float(a[1]), float(-a[0]))


# ── 【0】量測器自檢 ─────────────────────────────────────────────────────
def selfcheck(P, srange):
    P("")
    P("【0】量測器自檢（⛔ 先自檢後量測·各項皆附**已知真／已知偽**對照）")
    P("-" * W)
    ok = True

    # ① 夾角：已知真（垂直 90°／同向 0°）／已知偽（rot90cw 之逆不為 0）
    a1 = _ang((1, 0), (0, 1))
    a2 = _ang((1, 0), (1, 0))
    a3 = _ang((1, 0), (-1, 0))          # 無向 ⇒ 0（反向亦同向）
    r1 = abs(a1 - 90) < 1e-9 and abs(a2) < 1e-9 and abs(a3) < 1e-9
    ok &= r1
    P("  ① 夾角(無向)  ⊥=%.9f(期望90)／同向=%.9f(期望0)／反向=%.9f(期望0·無向) ⇒ %s"
      % (a1, a2, a3, "PASS" if r1 else "🔴 FAIL"))
    P("     對照(已知偽)：45° 之量 = %.9f（期望 45·若量得 0 或 90 表示式子錯）"
      % _ang((1, 0), (1, 1)))

    # ② rot90cw：已知真（(1,0)→(0,-1)）＋ 與原向量夾角須 90°
    rv_ = _rot90cw((1, 0))
    r2 = rv_ is not None and abs(rv_[0]) < 1e-12 and abs(rv_[1] + 1) < 1e-12 \
        and abs(_ang((1, 0), rv_) - 90) < 1e-9
    ok &= r2
    P("  ② rot90cw((1,0)) = %s（期望 (0,-1)）·與原向量夾角 = %.6f（期望 90）⇒ %s"
      % (rv_, _ang((1, 0), rv_), "PASS" if r2 else "🔴 FAIL"))

    # ③ 多邊形集合運算：已知真（重疊 10×4 與 +5 平移）
    A = SPoly([(0, 0), (10, 0), (10, 4), (0, 4)])
    B = SPoly([(5, 0), (15, 0), (15, 4), (5, 4)])
    ix = float(A.intersection(B).area)
    sd = float(A.symmetric_difference(B).area)
    r3 = abs(ix - 20) < 1e-12 and abs(sd - 40) < 1e-12 and (not A.contains(B))
    ok &= r3
    P("  ③ 交集=%.6f(期望20)／對稱差=%.6f(期望40)／A⊇B=%s(期望 False) ⇒ %s"
      % (ix, sd, A.contains(B), "PASS" if r3 else "🔴 FAIL"))
    C = SPoly([(1, 1), (2, 1), (2, 2), (1, 2)])
    r3b = A.contains(C)
    ok &= r3b
    P("     對照(已知真·含)：A ⊇ 小方 = %s（期望 True）⇒ %s"
      % (r3b, "PASS" if r3b else "🔴 FAIL"))

    # ④ s 區間：平移 δ·d̂ ⇒ s 恰移 δ（承 W-G.9-76 之恆等式）
    d = np.array([0.675686, 0.737190]); d = d / np.linalg.norm(d)
    al = np.array([0.726019, 0.687675])
    cp = np.array([0.0, 0.0])
    P0 = SPoly([(0, 0), (7, 0), (7, 2.5), (0, 2.5)])
    b0 = srange(P0, d, cp, al)
    from shapely.affinity import translate as _tr
    b1 = srange(_tr(P0, xoff=0.005 * float(d[0]), yoff=0.005 * float(d[1])), d, cp, al)
    r4 = abs((b1[0] - b0[0]) - 0.005) < 1e-12
    ok &= r4
    P("  ④ s 平移恆等 Δs=%.12f（期望 0.005）⇒ %s" % (b1[0] - b0[0], "PASS" if r4 else "🔴 FAIL"))

    P("  ⇒ 量測器自檢：%s" % ("PASS" if ok else "🔴 FAIL（⛔ 以下量測結果不得採信）"))
    return ok


# ── spy ────────────────────────────────────────────────────────────────
SOLVE = {}          # id(res_dict) -> dict
RANGES = {}         # (label, side) -> [polygon, ...]
CAP = []            # _pool_strips_for_block 之攔截
CUR = {"setback": None, "phase": ""}


def spy_solve(orig):
    def _s(**kw):
        res, label = orig(**kw)
        try:
            SOLVE[id(res)] = {
                "is_corner": bool(kw.get("is_corner")),
                "side": kw.get("side"),
                "side_mid_given": kw.get("side_mid") is not None,
                "alloc_in": kw.get("allocation_dir"),
                "alloc_used": res.get("_alloc_dir_used"),
                "near_dir": kw.get("near_dir"),
                "solver": label,
                "ncut": len(res.get("cut_coords") or []),
                "phase": CUR["phase"], "setback": CUR["setback"],
            }
        except Exception:                                           # noqa: BLE001
            pass
        return res, label
    return _s


def spy_range(orig):
    def _s(*a, **kw):
        out = orig(*a, **kw)
        try:
            k = (kw.get("_label", ""), kw.get("_side", ""))
            g = out[0] if isinstance(out, tuple) else out
            RANGES.setdefault((CUR["setback"], k[0], k[1]), []).append(g)
        except Exception:                                           # noqa: BLE001
            pass
        return out
    return _s


def spy_pool(orig):
    def _s(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
           _label='', _depth=None, _verbose=True):
        names, ress, align = None, None, "🔴 未對上"
        try:
            lv = sys._getframe(1).f_locals
            lr, rr = lv.get('left_results'), lv.get('right_results')
            ap = lv.get('allocated_polys')
            if isinstance(lr, list) and isinstance(rr, list):
                nm, rs = [], []
                for _entry, _res in (lr + rr):
                    _coords = (_res or {}).get('cut_coords') or []
                    _p = None
                    if len(_coords) >= 3:
                        try:
                            _p = SPoly(_coords)
                            if not _p.is_valid:
                                _p = _p.buffer(0)
                        except Exception:                           # noqa: BLE001
                            _p = None
                    if _p is not None and not _p.is_empty:
                        nm.append(((_entry or {}).get('tp') or {}).get('暫編地號', '?'))
                        rs.append(_res)
                if len(nm) == len(list(biz_polys or [])):
                    names, ress = nm, rs
                    align = "✅ 逐位對齊" if ap is biz_polys else "⚠️ 數相等但非同一物件"
        except Exception as e:                                      # noqa: BLE001
            align = "🔴 未對上（%s）" % type(e).__name__
        CAP.append({"setback": CUR["setback"], "label": _label,
                    "biz": list(biz_polys or []), "depth": _depth,
                    "d_hat": d_hat, "corner_pt": corner_pt, "alloc": allocation_dir,
                    "block": block_poly, "names": names, "ress": ress,
                    "align": align, "exc": None})
        try:
            return orig(block_poly, d_hat, corner_pt, allocation_dir, biz_polys,
                        _label=_label, _depth=_depth, _verbose=_verbose)
        except Exception as e:                                      # noqa: BLE001
            CAP[-1]["exc"] = "%s: %s" % (type(e).__name__, e)
            raise
    return _s


# ── 主 ──────────────────────────────────────────────────────────────────
def main():                                                         # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:                                           # noqa: BLE001
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []

    def P(s=""):
        L.append(s)
        print(s, file=sys.stderr)

    P("=" * W)
    P("【W-G.9-77 §二 A 組】`宗0` 之 `cut_coords` 構造定位（⛔ 只量不修）")
    P("=" * W)
    import shapely
    P("  產生於 commit：%s" % COMMIT)
    P("  環境：shapely %s | GEOS %s" % (shapely.__version__, shapely.geos_version))
    P("  🔒 A-0 錯誤方向**事前選定**：偏向**多報異常** ⇒ 與他宗不同型者一律列出、⛔ 無門檻。")
    P("  🔒 「方向相同」**事前定義** ＝ 無向夾角 ≤ %.2f°。" % ANG_TOL_DEG)
    P("  🔒 序 ＝ `left_results + right_results` 分組串接（承 W-G.9-76·⛔ 非空間序）。")

    ns, fake_st = harvest()
    srange = ns["_strip_s_range"]
    if not selfcheck(P, srange):
        with open(LOG, "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        return 1

    snapshot = rv.load_snapshot()
    o_solve = ns["_solve_G_one"]
    o_range = ns["_build_corner_range_v3"]
    o_pool = ns["_pool_strips_for_block"]

    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    cb_all = list(cb_by.values())
    blks = []
    for tp in build_p:
        _l = tp.get("所屬街廓")
        if _l and _l not in blks:
            blks.append(_l)

    P("")
    P("【驅動】R1–R6 × 兩情境全跑（⛔ 不只 R2／R5）——街廓母體 = %s" % blks)
    P("-" * W)
    ns["_solve_G_one"] = spy_solve(o_solve)
    ns["_build_corner_range_v3"] = spy_range(o_range)
    ns["_pool_strips_for_block"] = spy_pool(o_pool)
    WINS = {}
    try:
        for setback in (0.0, 3.5):
            CUR["setback"] = setback
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            CUR["phase"] = "corner_pk"
            _d0, _s2, _o2, wins, forced = run_corner_pk(
                ns, fake_st, cb_all, cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            WINS[setback] = wins
            CUR["phase"] = "step_g"
            for lbl in blks:
                with contextlib.redirect_stdout(io.StringIO()):
                    try:
                        run_step_g(ns, fake_st, cb_all, cad, snapshot, params,
                                   [tp for tp in build_p if tp.get("所屬街廓") == lbl],
                                   wins, forced, setback)
                    except Exception:                               # noqa: BLE001
                        pass
                print("    [%gm] %s 完畢" % (setback, lbl), file=sys.stderr)
    finally:
        ns["_solve_G_one"] = o_solve
        ns["_build_corner_range_v3"] = o_range
        ns["_pool_strips_for_block"] = o_pool

    P("  攔截：`_pool_strips_for_block` %d 筆／`_solve_G_one` 回傳登記 %d 筆／"
      "`_build_corner_range_v3` %d 個 (情境,街廓,側) 鍵"
      % (len(CAP), len(SOLVE), len(RANGES)))

    # 側界方向（供三路互證之路②）
    slbs = (fake_st.session_state.get('f3_cad_side_lines_by_side', {}) or {})

    def side_dirs(lbl):
        out = {}
        for w in ('left', 'right'):
            sd = (slbs.get(lbl) or {}).get(w)
            if sd and sd.get('p1') is not None and sd.get('p2') is not None:
                v = np.asarray(sd['p2'], dtype=float)[:2] - np.asarray(sd['p1'], dtype=float)[:2]
                out[w] = (v, _rot90cw(v))
        return out

    def side_degenerate(lbl, alloc):
        """🔒 路② 之**判別力前提**：`⊥SIDE` 與街廓 `ALLOC` 須**可分辨**。
        二者夾角 ≤ 門檻 ⇒ 「∥SIDE」對該塊之每一宗恆為真 ⇒ **路② 無判別力**
        （【倉】`verify/out/probe_D2b8_guard.log:23`：R6 之 `SIDE ∥ ALLOC` 退化）。
        ⛔ 退化時不得把路②之「是」當證據，須標**不可判**。"""
        sd = side_dirs(lbl)
        if not sd:
            return (True, float("nan"), None)      # 無 SIDE_LINE ⇒ 路② 不適用
        best = None
        for w, (v, rc) in sd.items():
            a = _ang(rc, alloc)
            if a == a and (best is None or a < best[0]):
                best = (a, w)
        if best is None:
            return (True, float("nan"), None)
        return (best[0] <= ANG_TOL_DEG, best[0], best[1])

    # ── §C  A-1 逐宗鏈 ─────────────────────────────────────────────────
    P("")
    P("【A-1】`cut_coords` 之逐宗鏈 ＋ 三路互證（⛔ 不以單一路推定）")
    P("-" * W)
    P("  🔒 逐行鏈（本批現查·行號成立於 commit %s）：" % COMMIT)
    P("     `solve_G_binary` def@9648 → 回傳 dict `'cut_coords': cut_coords` **@9897**")
    P("       ↑ 由 `_solve_G_one` def@12013 之 @12045 呼叫（`幾何二分法`）；")
    P("         其 fallback `iterate_G_S` 路徑於 **@12072** 令 `_r['cut_coords'] = []`（`代數迭代(fallback)`）")
    P("       ↑ `_solve_G_one` @12034-12035：**唯一決定點** `is_corner=True ⇒ "
      "allocation_dir = _first_corner_alloc_dir(side_mid)`（def@11975·回 `rot90_cw(SIDE)`）")
    P("       ↑ 驗證路徑：`verify/stepg_pipeline.py` `_solve_one` def@387 薄殼 → @393 `ns['_solve_G_one']`；")
    P("         呼叫端 @655（左組）／@729・@743（右組·area_geom<0.5 之重試）")
    P("       ↓ `_advance_block_with_split`（app def@19699）產 `left_results`／`right_results`")
    P("       ↓ `main` @20102 `for _entry, _res in (left_results + right_results)` → @20103 取 `cut_coords`")
    P("         → `allocated_polys` → `_pool_strips_for_block`（app @20130／stepg @951）")
    P("     ⛔ `_corner_first_lot_G` def@12077 **不在本鏈上**——其 @12167 `return float(_res.get('G',0.0))`，")
    P("        **只回 G、不回 `cut_coords`**（＝『假設第 1 宗』樂觀口徑·供資格閘）。")
    P("")
    P("  %-6s %-5s %-4s %-16s %-10s %-8s %-8s %10s %10s %-10s"
      % ("情境", "街廓", "i", "暫編地號", "solver", "路①is_corner", "路②∥SIDE", "∠(用,ALLOC)",
         "∠(用,⊥SIDE)", "路③winner"))
    A1 = {}
    for rec in CAP:
        sd = side_dirs(rec["label"])
        wins = WINS.get(rec["setback"])
        for i, nm in enumerate(rec["names"] or []):
            r = (rec["ress"] or [None] * (i + 1))[i]
            info = SOLVE.get(id(r)) if r is not None else None
            au = (info or {}).get("alloc_used")
            a_alloc = _ang(au, rec["alloc"])
            best_w, a_side = None, float("nan")
            for w, (v, rc) in sd.items():
                aa = _ang(au, rc)
                if aa == aa and (a_side != a_side or aa < a_side):
                    a_side, best_w = aa, w
            p1 = (info or {}).get("is_corner")
            p2 = (a_side == a_side and a_side <= ANG_TOL_DEG)
            p3 = None
            try:
                p3 = (nm in str(wins))
            except Exception:                                       # noqa: BLE001
                p3 = None
            A1[(rec["setback"], rec["label"], i)] = {
                "p1": p1, "p2": p2, "p3": p3, "solver": (info or {}).get("solver"),
                "a_alloc": a_alloc, "a_side": a_side, "side_w": best_w,
                "info": info, "name": nm}
            if i == 0 or p1 or p2:      # A-0 多報：宗0 與任何一路判街角者全列
                P("  %-6s %-5s %-4d %-16s %-10s %-8s %-8s %10.4f %10.4f %-10s"
                  % ("%gm" % rec["setback"], rec["label"], i, nm,
                     (info or {}).get("solver") or "🔴 未對上",
                     ("是" if p1 else ("否" if info else "🔴 未對上")),
                     ("是" if p2 else "否"), a_alloc, a_side,
                     ("是" if p3 else ("否" if p3 is not None else "—"))))
    # 🔒 路② 之判別力前提：逐塊先驗（退化塊之路② 一律標不可判·⛔ 不當證據）
    P("")
    P("  🔒 路② 之**判別力前提**（⛔ 先驗後用）：`∠(ALLOC, ⊥SIDE)` 須 > %.2f°，否則路② 恆真、無判別力"
      % ANG_TOL_DEG)
    P("     %-6s %-5s %14s %-10s %-24s" % ("情境", "街廓", "∠(ALLOC,⊥SIDE)", "最近側", "路② 判別力"))
    DEGEN = {}
    for rec in CAP:
        dg, a, w = side_degenerate(rec["label"], rec["alloc"])
        DEGEN[(rec["setback"], rec["label"])] = dg
        P("     %-6s %-5s %14.6f %-10s %-24s"
          % ("%gm" % rec["setback"], rec["label"], a, w or "—",
             "🔴 **退化·無判別力**" if dg else "✅ 有判別力"))

    # 三路一致性彙總（退化塊之路② 不計入一致／不一致，改計不可判）
    agree = dis = unk = deg = 0
    for k, v in A1.items():
        if v["info"] is None:
            unk += 1
            continue
        if DEGEN.get((k[0], k[1])):
            deg += 1
            continue
        if bool(v["p1"]) == bool(v["p2"]):
            agree += 1
        else:
            dis += 1
    P("  ⇒ 分母 %d 宗：路①vs路② **一致 %d ／ 不一致 %d ／ 路②退化不可判 %d ／ 未對上 %d**"
      % (len(A1), agree, dis, deg, unk))
    if dis:
        P("  🔴 路①②**真**不一致者逐項具名（⛔ 不取多數決·已排除退化塊）：")
        for k, v in A1.items():
            if (v["info"] is not None and not DEGEN.get((k[0], k[1]))
                    and bool(v["p1"]) != bool(v["p2"])):
                P("     [%gm] %-4s 宗%-3d %-16s 路①=%s 路②=%s ∠(用,⊥SIDE)=%.4f°"
                  % (k[0], k[1], k[2], v["name"], v["p1"], v["p2"], v["a_side"]))
    else:
        P("  ✅ 路①②**真**不一致 ＝ 0（⛔ 退化塊已另計為不可判、未當作一致）")
    # 路① vs 路③
    d13 = [(k, v) for k, v in A1.items()
           if v["info"] is not None and v["p3"] is not None and bool(v["p1"]) != bool(v["p3"])]
    P("  ⇒ 路①vs路③（winner 名單）不一致 = %d 宗%s"
      % (len(d13), "" if not d13 else "：" + str([(k[1], k[2], v["name"]) for k, v in d13])))

    # ── §D  A-2 s 區間 ─────────────────────────────────────────────────
    P("")
    P("【A-2】s 區間逐宗並列（六塊 × 兩情境·⛔ 不只 R2／R5）")
    P("-" * W)
    SUM = []
    for rec in CAP:
        n = len(rec["biz"])
        srs = []
        for p in rec["biz"]:
            r = srange(p, rec["d_hat"], rec["corner_pt"], rec["alloc"])
            srs.append((r[0], r[1]) if r else (float("nan"), float("nan")))
        broke = "🔴 破閘" if (rec["exc"] and "②-宗" in (rec["exc"] or "")) else "未破閘"
        P("")
        P("  ── [%gm] %s ── n=%d　%s　地號對齊：%s"
          % (rec["setback"], rec["label"], n, broke, rec["align"]))
        if n == 0:
            P("     ⚠️ n=0 ⇒ 本格不適用·具名")
            continue
        z0 = srs[0]
        span0 = z0[1] - z0[0]
        others = [srs[k][1] - srs[k][0] for k in range(1, n)]
        med = statistics.median(others) if others else float("nan")
        mult = (span0 / med) if (med == med and med > 0) else float("nan")
        full, part = [], []
        for k in range(1, n):
            lo, hi = srs[k]
            if lo >= z0[0] - 1e-9 and hi <= z0[1] + 1e-9:
                full.append(k)
            elif not (hi <= z0[0] + 1e-9 or lo >= z0[1] - 1e-9):
                part.append(k)
        P("     %-4s %-16s %12s %12s %10s %-10s %12s"
          % ("i", "暫編地號", "s_min", "s_max", "s 跨距", "與宗0重疊?", "面積㎡"))
        for k in range(n):
            lo, hi = srs[k]
            ov = "—（自身）" if k == 0 else (
                "完全被含" if k in full else ("部分重疊" if k in part else "否"))
            P("     %-4d %-16s %12.4f %12.4f %10.4f %-10s %12.4f"
              % (k, (rec["names"] or ["?"] * n)[k], lo, hi, hi - lo, ov,
                 float(rec["biz"][k].area)))
        P("     🔴 `宗0` 跨距 = %.4f　其餘 %d 宗跨距中位數 = %.4f　⇒ **倍數 = %.3f×**"
          % (span0, len(others), med, mult))
        P("     🔴 `宗0` 之 s 區間：**完全含住** %d 宗 %s ／ **部分重疊** %d 宗 %s"
          % (len(full), [(rec["names"] or [])[k] for k in full] or "（無）",
             len(part), [(rec["names"] or [])[k] for k in part] or "（無）"))
        SUM.append((rec["setback"], rec["label"], broke, n, span0, med, mult,
                    len(full), len(part)))

    P("")
    P("【A-2 判別力對照】破閘 vs 未破閘之倍數（🔒 期望：未破閘者**顯著較小**）")
    P("-" * W)
    P("  %-6s %-5s %-8s %4s %10s %12s %10s %8s %8s"
      % ("情境", "街廓", "破閘?", "n", "宗0跨距", "其餘中位數", "倍數", "完全含", "部分疊"))
    for sb, lb, br, n, s0, md, mu, nf, np_ in SUM:
        P("  %-6s %-5s %-8s %4d %10.4f %12.4f %10.3f %8d %8d"
          % ("%gm" % sb, lb, br, n, s0, md, mu, nf, np_))
    brk = [x[6] for x in SUM if "破閘" in x[2] and x[2].startswith("🔴")]
    unb = [x[6] for x in SUM if not x[2].startswith("🔴")]
    P("  ⇒ 破閘格（%d）倍數：%s" % (len(brk), ["%.3f" % v for v in brk]))
    P("  ⇒ 未破閘格（%d）倍數：min=%.3f 中位=%.3f max=%.3f"
      % (len(unb), min(unb), statistics.median(unb), max(unb)) if unb else "  ⇒ 未破閘格：無")
    if brk and unb:
        P("  🔒 判（施工單 `P4` 之受詞 ＝ **倍數**）：破閘格最小倍數 = %.3f vs 未破閘格最大倍數 = %.3f ⇒ %s"
          % (min(brk), max(unb),
             "✅ 可區辨（破閘者全部較大）" if min(brk) > max(unb)
             else "🔴 **不可區辨** ⇒ 「跨距倍數」⛔ 非破閘之充分特徵·具名"))
    # 🔒 補充欄（⛔ **非施工單所令**）：以「完全含住之宗數」重看同一組資料
    bf = [x[7] for x in SUM if x[2].startswith("🔴")]
    uf = [x[7] for x in SUM if not x[2].startswith("🔴")]
    P("  🔒 **補充（⛔ 非施工單所令）**：改以「`宗0` **完全含住**之宗數」看同一組資料——")
    P("     破閘格 %s ／ 未破閘格 %s" % (bf, uf))
    P("     ⇒ %s" % ("🔒 於本 12 格**完全分離**（破閘者皆 ≥1、未破閘者皆 0）"
                     if (bf and uf and min(bf) >= 1 and max(uf) == 0)
                     else "未完全分離"))
    P("     ⚠️ **⛔ 不得據此宣稱判準**：正例僅 %d 格，樣本過小；且本批⛔ 不對成因下結論"
      "（施工單 §七-3）。此欄僅為**觀察**。" % len(bf))

    # ── §E  A-3 街角規定範圍 ───────────────────────────────────────────
    P("")
    P("【A-3】`宗0` 與**街角規定範圍**之幾何關係（⚠️ **觀察**·⛔ 非判準·見 `U-K9-3`）")
    P("-" * W)
    P("  🔒 `U-K9-3`（KL 裁 2026-08-03）逐字併記【倉】`docs/reports/W-G.4_泛用阻塞項登記表.md:162`：")
    P("     「claude.ai 之『包含關係』判準**訂錯**……程式閘比的是 `G` vs 純量門檻」")
    P("     ⇒ ⚠️ 本節係**觀察**、⛔ 不得據以宣告任何「不合格」。")
    P("  🔒 **進入本節之門檻 ＝ 路① ∧ 路③ 皆判「是」**（⛔ 不用路②：R6 之路② 已先驗為退化）。")
    P("  🔒 `contains` 對**共邊**者回 `False` ⇒ 另出艙 `範圍∖宗0`／`宗0∖範圍` 之**殘量面積**"
      "（⛔ 布林欄單獨看會誤導）。")
    P("  %-6s %-5s %-16s %-6s %11s %11s %11s %11s %11s %11s"
      % ("情境", "街廓", "宗0 地號", "側", "範圍面積", "宗0面積", "交集",
         "範圍∖宗0", "宗0∖範圍", "對稱差"))
    done = 0
    for rec in CAP:
        k0 = (rec["setback"], rec["label"], 0)
        v = A1.get(k0)
        if not v or not (v["p1"] and v["p3"]):
            P("  %-6s %-5s %-16s %-6s %s"
              % ("%gm" % rec["setback"], rec["label"],
                 (rec["names"] or ["?"])[0] if rec["names"] else "?", "—",
                 "⚠️ 宗0 **非**街角第 1 宗（路①=%s 路②=%s%s 路③=%s）⇒ 本節略過·具名"
                 % ((v or {}).get("p1"), (v or {}).get("p2"),
                    "〔退化·不可用〕" if DEGEN.get((rec["setback"], rec["label"])) else "",
                    (v or {}).get("p3"))))
            continue
        # 🔒 側別鍵 ＝ 生產端之 `_side` 實參（`'left'`／`'right'`·app.py:11524 具名傳入）
        #    ⇒ 與路② 幾何比對所得之 `side_w` **同一組字面**，⛔ 不做中英轉換（轉換即製造不匹配）。
        wside = v["side_w"] or "?"
        cand = [g for (sb, lb, sdl), gs in RANGES.items()
                if sb == rec["setback"] and lb == rec["label"]
                and str(sdl) == str(wside) for g in gs if g is not None]
        z0 = rec["biz"][0] if rec["biz"] else None
        if not cand or z0 is None:
            P("  %-6s %-5s %-16s %-8s %s"
              % ("%gm" % rec["setback"], rec["label"],
                 (rec["names"] or ["?"])[0], wside,
                 "⚠️ 取不到街角範圍多邊形（鍵 %s·候選 %d）⇒ **不可判·具名**"
                 % (list({k for k in RANGES if k[0] == rec['setback'] and k[1] == rec['label']}),
                    len(cand))))
            continue
        areas = sorted({round(float(g.area), 6) for g in cand})
        rg = cand[0]
        if len(areas) > 1:
            P("     ⚠️ [%gm] %s/%s 之範圍多邊形有 **%d 種相異面積** %s ⇒ 取第一個並**具名**"
              % (rec["setback"], rec["label"], wside, len(areas), areas))
        ix = float(rg.intersection(z0).area)
        P("  %-6s %-5s %-16s %-6s %11.4f %11.4f %11.4f %11.6f %11.4f %11.4f"
          % ("%gm" % rec["setback"], rec["label"], (rec["names"] or ["?"])[0], wside,
             float(rg.area), float(z0.area), ix,
             float(rg.difference(z0).area), float(z0.difference(rg).area),
             float(rg.symmetric_difference(z0).area)))
        done += 1
    P("  ⇒ 本節實得 %d 格（分母 = %d 攔截格）" % (done, len(CAP)))

    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("\n→ %s" % LOG, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
