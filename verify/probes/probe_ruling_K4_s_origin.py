# -*- coding: utf-8 -*-
"""W-G.5 K-4 第 5 條 — **街角第 1 宗之 S 起算點**（未截角理論角 vs 街廓頂點極值）。

## 題（KL 交辦·任務 1）

K-4 第 5 條：「計算街角地第 1 宗 G 時，**S 須自『未截角之 FRONTLINE × SIDELINE 交點』起算**」。

現況 `_corner_first_lot_G`（`grep -n "def _corner_first_lot_G" app.py`）：
  · 左側 `baseline_pt = corner_pt`（＝FRONT p1）
  · 右側 `baseline_pt = corner_pt + s_max_right·d̂`，而呼叫端之 `s_max_right`
    ＝ `_oblique_s_max(**街廓頂點**, …)` ⇒ 取街廓多邊形頂點極值。
若街廓頂點已被**截角**，該極值會**短於**理論角，起算點即落在截角斜邊上。

## 本探針只回答三件事（**只量不改**）

1. **FRONT_LINE 端點是否即未截角理論角**：逐側算 FRONT 與 SIDE 之**無限直線交點**，
   與 FRONT 對應端點比距離。（KL 稱八側全 0.000000 m——**本探針自行重算，不抄**。）
2. **六塊全表**：`_oblique_s_max` vs `|FRONT_LINE|`（二者同軸可比：由
   `_strip_axis` 之恆等式 `s(corner_pt + s₀·d̂) ≡ s₀` ⇒ `s(p2) ≡ |FRONT|`）。
   併印左端之 `s_min`（＝街廓頂點於同軸之最小 s·對照左側是否亦短）。
3. **Δ 是否 ＝ 該側截角腿長**（若是，即坐實「頂點極值落在截角點」之歸因）。

⚠️ **ALLOC 定向一律取管線自己的** `cad['alloc_dir_by_block']`（KL 自算之 500~825 異常值不採）。

## 重跑
    python verify/probes/probe_ruling_K4_s_origin.py     # rc=0 綠／1 紅

⚠️ **零注入·唯讀**。輸出 `verify/out/probe_ruling_K4_s_origin.log`。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

import numpy as np                                                  # noqa: E402
from shapely.geometry import Polygon                                # noqa: E402
from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402

LOG = os.path.join(VERIFY, "out", "probe_ruling_K4_s_origin.log")


def _fail(msg):
    raise RuntimeError(f"🔴 probe_ruling_K4_s_origin：{msg}（no-silent-fallback）")


def _line_intersect(a1, a2, b1, b2):
    """兩條**無限直線**之交點（a1→a2 與 b1→b2）。平行 → None。"""
    a1 = np.asarray(a1, float)[:2]; a2 = np.asarray(a2, float)[:2]
    b1 = np.asarray(b1, float)[:2]; b2 = np.asarray(b2, float)[:2]
    u = a2 - a1
    v = b2 - b1
    M = np.array([[u[0], -v[0]], [u[1], -v[1]]], dtype=float)
    det = float(np.linalg.det(M))
    if abs(det) < 1e-12:
        return None
    t, _s = np.linalg.solve(M, b1 - a1)
    return a1 + t * u


def main():
    for _st in (sys.stdout, sys.stderr):
        try:
            _st.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    L = []
    bad = []
    snapshot = json.load(open(rv.SNAPSHOT, encoding="utf-8"))
    ns, fake_st = harvest()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    fls = cad.get("front_lines") or {}
    alloc = cad.get("alloc_dir_by_block") or {}
    slbs = fake_st.session_state.get("f3_cad_side_lines_by_side", {}) or {}
    _oblique = ns["_oblique_s_max"]
    _strip_axis = ns["_strip_axis"]

    L.append("=" * 118)
    L.append("【K-4 第 5 條】街角第 1 宗之 S 起算點 —— `_oblique_s_max`（街廓頂點極值）"
             " vs `|FRONT_LINE|`（理論角）")
    L.append("=" * 118)

    # ── 【1】FRONT_LINE 端點是否即「未截角之 FRONT×SIDE 理論交點」────────────────────
    L.append("")
    L.append("【1】FRONT_LINE 端點 vs FRONT×SIDE **無限直線**交點（KL 稱八側全 0——本表自行重算）")
    L.append("-" * 118)
    L.append(f"  {'街廓':6}{'側':6}{'|交點−FRONT端點|(m)':>22}{'該端':>8}  判")
    _n_side_seen = 0
    for blk in sorted(cb_by):
        fl = fls.get(blk) or {}
        if not (fl.get("p1") and fl.get("p2")):
            continue
        p1 = np.asarray(fl["p1"], float)[:2]
        p2 = np.asarray(fl["p2"], float)[:2]
        for _sd, _end, _endname in (("left", p1, "p1"), ("right", p2, "p2")):
            _s = (slbs.get(blk) or {}).get(_sd)
            if not _s:
                continue
            _n_side_seen += 1
            _sp1 = _s.get("p1"); _sp2 = _s.get("p2")
            if not (_sp1 and _sp2):
                _fail(f"{blk}·{_sd} SIDE_LINE 缺端點")
            _x = _line_intersect(p1, p2, _sp1, _sp2)
            if _x is None:
                L.append(f"  {blk:6}{_sd:6}{'∥（無交點）':>22}{_endname:>8}  🔴")
                bad.append(f"{blk}·{_sd} FRONT∥SIDE")
                continue
            _d = float(np.linalg.norm(_x - _end))
            _ok = _d <= 1e-6
            L.append(f"  {blk:6}{_sd:6}{_d:22.9f}{_endname:>8}  {'✅' if _ok else '🔴'}")
            if not _ok:
                bad.append(f"{blk}·{_sd} |交點−{_endname}| = {_d:.6f} > 1e-6")
    L.append(f"  ⇒ 共 {_n_side_seen} 側有 SIDE_LINE")

    # ── 【2】六塊全表：_oblique_s_max vs |FRONT| ────────────────────────────────
    L.append("")
    L.append("【2】`_oblique_s_max`（街廓頂點極值·斜交軸）vs `|FRONT_LINE|`（＝理論角之 s）")
    L.append("    同軸可比之依據：`_strip_axis` 恆等式 `s(corner_pt + s₀·d̂) ≡ s₀` ⇒ `s(p2) ≡ |FRONT|`")
    L.append("-" * 118)
    L.append(f"  {'街廓':6}{'|FRONT|':>11}{'s(p2)覆核':>12}{'oblique_s_max':>15}"
             f"{'Δ右=|F|−smax':>14}{'s_min(左端)':>13}{'右截角腿':>10}{'左截角腿':>10}")
    _rows = []
    for blk in sorted(cb_by):
        fl = fls.get(blk) or {}
        b = cb_by[blk]
        verts = b.get("vertices") or []
        _ad = alloc.get(blk)
        if not (fl.get("p1") and fl.get("p2")) or len(verts) < 3 or not _ad:
            L.append(f"  {blk:6}  （缺 FRONT_LINE／vertices／alloc_dir ⇒ 非分配街廓·跳過）")
            continue
        p1 = np.asarray(fl["p1"], float)[:2]
        p2 = np.asarray(fl["p2"], float)[:2]
        Lf = float(np.linalg.norm(p2 - p1))
        d_hat = (p2 - p1) / Lf
        _axis = ns["alloc_normal_axis"](_ad)
        m_hat, denom = _strip_axis(d_hat, _axis)
        _s_of = lambda P: float(np.dot(np.asarray(P, float)[:2] - p1, m_hat)) / float(denom)  # noqa: E731
        _s_p2 = _s_of(p2)
        _smax = _oblique(verts, d_hat, p1, _axis)
        _svals = [_s_of(v) for v in verts]
        _smin = min(_svals)
        # 截角腿：theoretical_corners 之 corner → cutoff edge 兩端點之距（取最長腿）
        _legs = {"left": None, "right": None}
        _gr = (b.get("geom_restore") or {})
        _edges = ((_gr.get("classification") or {}).get("edges") or [])
        for tc in (_gr.get("theoretical_corners") or []):
            _sd = tc.get("side")
            _ci = tc.get("cutoff_idx", -1)
            if _sd not in _legs or _ci < 0 or _ci >= len(_edges):
                continue
            _e = _edges[_ci]
            _c = np.asarray(tc.get("corner"), float)[:2]
            _legs[_sd] = max(float(np.linalg.norm(np.asarray(_e["p1"], float)[:2] - _c)),
                             float(np.linalg.norm(np.asarray(_e["p2"], float)[:2] - _c)))
        _d_right = Lf - float(_smax)
        _rows.append((blk, Lf, _s_p2, float(_smax), _d_right, _smin, _legs))
        L.append(f"  {blk:6}{Lf:11.4f}{_s_p2:12.4f}{float(_smax):15.4f}{_d_right:14.4f}"
                 f"{_smin:13.4f}"
                 f"{(f'{_legs['right']:.4f}' if _legs['right'] else '—'):>10}"
                 f"{(f'{_legs['left']:.4f}' if _legs['left'] else '—'):>10}")
        if abs(_s_p2 - Lf) > 1e-6:
            bad.append(f"{blk} 恆等式破：s(p2)={_s_p2:.6f} ≠ |FRONT|={Lf:.6f}")

    # ── 【3】Δ 是否 ＝ 該側截角腿長 ──────────────────────────────────────────────
    L.append("")
    L.append("【3】歸因檢：Δ右（＝|FRONT|−oblique_s_max）是否 ≈ **右側截角腿長**？")
    L.append("    （若是 ⇒ 坐實「頂點極值落在截角點上」；若否 ⇒ 另有成因，勿逕行改碼）")
    L.append("-" * 118)
    L.append(f"  {'街廓':6}{'Δ右':>11}{'右截角腿':>12}{'|Δ−腿|':>12}  判讀")
    for blk, Lf, _s_p2, _smax, _d_right, _smin, _legs in _rows:
        _leg = _legs.get("right")
        if _leg is None:
            L.append(f"  {blk:6}{_d_right:11.4f}{'—':>12}{'—':>12}  該側無截角"
                     f"（{'Δ≈0·一致' if abs(_d_right) < 1e-3 else '🚩 Δ≠0 卻無截角·待查'}）")
            if abs(_d_right) >= 1e-3:
                bad.append(f"{blk} 右側無截角但 Δ={_d_right:.4f}")
            continue
        _gap = abs(_d_right - _leg)
        L.append(f"  {blk:6}{_d_right:11.4f}{_leg:12.4f}{_gap:12.6f}  "
                 f"{'✅ Δ＝截角腿（歸因成立）' if _gap <= 1e-3 else '🚩 Δ≠截角腿·另有成因'}")

    # ── 【4】左端對照 ────────────────────────────────────────────────────────────
    L.append("")
    L.append("【4】左端對照：`s_min`（街廓頂點極小 s）vs 0（＝corner_pt/FRONT p1）")
    L.append("    左側 baseline_pt 直接取 corner_pt ⇒ **不受頂點極值影響**；本欄僅供對稱性判讀。")
    L.append("-" * 118)
    for blk, Lf, _s_p2, _smax, _d_right, _smin, _legs in _rows:
        _leg = _legs.get("left")
        L.append(f"  {blk:6} s_min = {_smin:9.4f}"
                 f"（左截角腿 {(f'{_leg:.4f}' if _leg else '—')}）"
                 f"{'  ⇒ 左端頂點極值亦短於理論角，惟左側未用之' if _smin > 1e-3 else ''}")

    # ── 【5】三變體之 winner／forced 衝擊（KL 任務 1(b)(c)：**兩消費者分開評估**）────────
    #   A ＝ 現況：`baseline_pt = cp + s_max_right·d̂`、`S_max = s_max_right`
    #   B ＝ **只改起算點**：`baseline_pt = cp + s_max_left·d̂`（＝FRONT p2·K-4 第5條）、`S_max` 不動
    #   C ＝ 兩者皆改：`baseline_pt`／`S_max` 皆用 `s_max_left`
    #   作法：patch `ns['_corner_first_lot_G']`（app 真 globals ⇒ `_corner_block_true_G` 會取到），
    #        **內部仍呼原 `_solve_G_one`**（Q-M4 同 solve 路徑·非另寫平行式）。
    #   🔒 自檢：以 patch 機制重現「A ＝ 未 patch」之值，證明本比較之載具忠實。
    L.append("")
    L.append("【5】三變體衝擊：winner 集合／強制抵費地側（**兩情境**）")
    L.append("-" * 118)
    import numpy as _np5
    from selection_pipeline import run_corner_pk as _pk                      # noqa: E402
    _orig_first_lot = ns["_corner_first_lot_G"]
    _solve_one = ns["_solve_G_one"]

    def _make_variant(bp_from_left, smax_from_left):
        def _f(*, a_m2, A_ratio, B, C, l_front, l_side, F, block_poly, d_hat,
               corner_pt, s_max_left, s_max_right, side, allocation_dir, side_mid,
               avg_depth, tab6_burden, front_p2, _label=''):
            # 🔒 與生產 `_corner_first_lot_G` **同簽名**——K-4 第 5 條之 `front_p2` 前提
            #   斷言於此**照樣驗**（變體只換錨之取法，不豁免前提）。
            _dp2 = float(_np5.linalg.norm(_np5.asarray(front_p2, dtype=float)[:2]
                                          - _np5.asarray(corner_pt, dtype=float)[:2]))
            if abs(_dp2 - float(s_max_left)) > 1e-9:
                raise RuntimeError(
                    f"🔴 probe 變體：s_max_left {float(s_max_left):.9f} ≠ "
                    f"‖front_p2−corner_pt‖ {_dp2:.9f}")
            _side_cn = {'左': '左側', '右': '右側'}.get(side, side)
            _dh = _np5.asarray(d_hat, dtype=float)
            _cp = _np5.asarray(corner_pt, dtype=float)
            if _side_cn == '左側':
                _bp, _dh_use, _sm = _cp, _dh, float(s_max_left)
            else:
                _anchor = float(s_max_left) if bp_from_left else float(s_max_right)
                _sm = float(s_max_left) if smax_from_left else float(s_max_right)
                _bp, _dh_use = _cp + _anchor * _dh, -_dh
            _res, _ = _solve_one(
                a_m2=a_m2, A=A_ratio, l_front=l_front, l_side=l_side, F=F,
                blk_poly=block_poly, d_hat=_dh_use, baseline_pt=_bp,
                S_max=max(0.1, _sm), is_corner=True, side=_side_cn, avg_depth=avg_depth,
                B=B, C=C, tab6_burden=tab6_burden,
                allocation_dir=allocation_dir, side_mid=side_mid, W_prev=0.0)
            return float(_res.get('G', 0.0) or 0.0)
        return _f

    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as _f6:
        _v6 = _f6.read()
    _tp, _bp_all, _ = rv.build_build_parcels(ns, fake_st, _v6, list(cb_by.values()), snapshot)

    def _run(tag_setback, variant_fn):
        if variant_fn is None:
            ns["_corner_first_lot_G"] = _orig_first_lot
        else:
            ns["_corner_first_lot_G"] = variant_fn
        try:
            _params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, tag_setback)
            _diag, _sel, _off, _win, _fo = _pk(
                ns, fake_st, list(cb_by.values()), cad, _params,
                _tp, _bp_all, tag_setback, snapshot=snapshot)
        finally:
            ns["_corner_first_lot_G"] = _orig_first_lot
        # winner ＝ 指配表之「【左/右】第1宗指配」欄（`第 1 宗街角地指配結果_*.csv` 之欄名）
        _w = {}
        for r in _sel:
            for _e, _col in (("左", "【左】第1宗指配"), ("右", "【右】第1宗指配")):
                _v = str(r.get(_col, "") or "").strip()
                if _v and _v not in ("—", "-", "無"):
                    _w[(r.get("街廓"), _e)] = _v
        _f = {(r.get("街廓"), r.get("端")) for r in _off}
        _g = {(r.get("街廓"), r.get("端"), r.get("候選地號")): r.get("真G(㎡)") for r in _diag}
        return _w, _f, _g

    # 🆕 K-4 第 5 條落地**後**之變體集（基準已是 p2 錨）：
    #   A  ＝ 現況（未 patch·K-4 後：bp=FRONT p2、S_max=s_max_right）
    #   A′ ＝ **patch 載具自檢**：以 patch 重現現況語意 ⇒ 必須與 A 逐格全等
    #   OLD＝ **K-4 前**之舊語意（bp 錨 `s_max_right`）⇒ 差量即 K-4 之衝擊（留檔備查）
    #   C  ＝ 起算點＋S_max 皆改 ⇒ 證 `S_max` 為惰性消費者（KL 任務 1(b) 分開評估）
    _VAR = (("A 現況（K-4 後·FRONT p2 錨）", None),
            ("A′ patch 載具自檢（同 A 語意）", _make_variant(True, False)),
            ("OLD K-4 前（smax_right 錨）", _make_variant(False, False)),
            ("C 起算點＋S_max 皆改", _make_variant(True, True)))
    for _sb, _tag in ((0.0, "0m"), (3.5, "3.5m")):
        L.append("")
        L.append(f"  ── 情境 {_tag} ──")
        _base_w = _base_f = _base_g = None
        for _name, _fn in _VAR:
            _w, _f, _g = _run(_sb, _fn)
            if _base_w is None:
                _base_w, _base_f, _base_g = _w, _f, _g
                L.append(f"    {_name:32} winner {len(_w)} 側｜強制抵費地 {len(_f)} 側｜（基準）")
                continue
            _dw = sorted(k for k in set(_base_w) | set(_w) if _base_w.get(k) != _w.get(k))
            _df = sorted(_base_f ^ _f)
            _dg = [(k, _base_g.get(k), _g.get(k)) for k in sorted(set(_base_g) | set(_g))
                   if _base_g.get(k) != _g.get(k)]
            L.append(f"    {_name:32} winner {len(_w)} 側｜強制抵費地 {len(_f)} 側｜"
                     f"winner 異動 {len(_dw)}｜forced 異動 {len(_df)}｜真G 異動 {len(_dg)} 格")
            for k in _dw[:12]:
                L.append(f"        🚩 winner {k}: {_base_w.get(k)!r} → {_w.get(k)!r}")
            for k in _df[:12]:
                L.append(f"        🚩 forced {k}: {'退出' if k in _base_f else '新增'}")
            for k, v0, v1 in _dg[:12]:
                L.append(f"        · 真G {k}: {v0} → {v1}")
            if _name.startswith("A′") and (_dw or _df or _dg):
                bad.append(f"[{_tag}] patch 載具自檢失敗：A′ 應與 A 逐格全等")

    L.append("")
    L.append("-" * 118)
    if bad:
        L.append(f"RESULT: FAIL（{len(bad)} 違例）")
        for x in bad[:20]:
            L.append("  " + x)
    else:
        L.append("RESULT: PASS（結構斷言全綠·判讀見上表）")
    L.append("=" * 118)
    txt = "\n".join(L)
    print(txt)
    with open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
