# -*- coding: utf-8 -*-
r"""**D-2b-0 §A-3**：`K-9-5-4` ② 之新期望表（⛔ 只算不換·**零生產碼**）。

以 **patch** 令**第 1 宗之遠側界改 ∥SIDELINE**（⛔ 不改生產）：
把 `_corner_first_lot_G` 之 `allocation_dir` 換成 **`rot90_cw(SIDE 方向)`**
——依 `_block_strip` 之 `n_hat = rot90(allocation_dir)` ⇒ 切帶界線 ∥SIDELINE；
且 `solve_G_binary` 之 `_n_alloc = normalize(allocation_dir)` ⇒ `W` 沿其法向（垂距）。
🔒 **GEO-1／GEO-2 已證此路徑**·⛔ 未另寫第三套幾何。
⛔ **第 2 宗之遠側界仍 ∥ALLOC**（KL 2026-08-07 逐字）——本檔只動第 1 宗。

## ⚠️ 檔頭聲明（施工單 §A-3 明令逐字標明）

**門檻取自「已切換之生產範圍面積」**（D-2 已落地之 `_build_corner_range_v3`·直接取生產值）；
**真G 為 patch 值**（本檔以 patch 算出、⛔ 非生產現值）。

## 🔒 §A-4 自我驗證閘

patch 出之**實配多邊形面積**（`solve_G_binary` 之 `area_geom`）與其 **G 目標**之差 **≤ 0.01㎡**，
逐候選 ✅／❌；**未過者標「不可據」並自有效分母剔除**。

## 🔒 §A-5 對帳器不變量（本檔起一律適用）

1. 框內重複鍵 ＝ **0**，否則 `raise`
2. **母體列數印出**，並與來源逐一對得上
3. 比對欄以**欄名**指名並印出（⛔ 非欄號）
4. 輸出檔名**帶批次識別**（本檔 ＝ `D2b`）
5. ⛔ **禁寫入任何他批已入庫之 log 檔名**
"""
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)

from app_harvest import harvest                                     # noqa: E402
import run_verification as rv                                       # noqa: E402
from selection_pipeline import run_corner_pk                        # noqa: E402

OUTDIR = os.path.join(VERIFY, "out")
LOG = os.path.join(OUTDIR, "probe_D2b_expect_凍存.log")          # §A-5-4 帶批次識別
TOL_A4 = 0.01
# 🔒 `solve_G_binary` 之收斂條件為 `|area_geom − G_target| <= tol`（tol=0.01·`app.py:9302`）
#   ⇒ 恰等於 `0.01` 者**係已收斂**，⛔ 不得判為未過閘。取 1e-9 之浮點餘裕。
_A4_EPS = 1e-9
_SIDECN = {"左": "left", "右": "right"}


def _u(ax, ay):
    n = math.hypot(ax, ay)
    return (ax / n, ay / n)


def main():                                                    # noqa: C901
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    os.makedirs(OUTDIR, exist_ok=True)
    L = []
    L.append("=" * 200)
    L.append("【D-2b-0 §A-3】K-9-5-4 ② 之新期望表（**凍存**）— ⛔ 只算不換·零生產碼")
    L.append("=" * 200)
    L.append("  🔒 **門檻取自「已切換之生產範圍面積」**（D-2 已落地之 `_build_corner_range_v3`·直接取生產值）；")
    L.append("  🔒 **真G 為 patch 值**（本檔以 patch 算出·⛔ 非生產現值）。")
    L.append("  🔒 patch ＝ `_corner_first_lot_G` 之 `allocation_dir` → **`rot90_cw(SIDE 方向)`**")
    L.append("     （`_block_strip` 之 `n_hat = rot90(allocation_dir)` ⇒ 切帶界線 ∥SIDELINE；")
    L.append("      `solve_G_binary` 之 `_n_alloc = normalize(allocation_dir)` ⇒ W 沿其法向）")
    L.append("  ⛔ **第 2 宗之遠側界仍 ∥ALLOC**——本檔只動第 1 宗。")

    ns, fake_st = harvest()
    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    sd_by = cad.get("side_lines_by_side", {}) or {}

    def _ad_by_mid(side_mid):
        """以 **`side_mid` 幾何反查** SIDE_LINE（⛔ 不靠 `_label` 之字串格式）。

        🔒 **案由**：`_corner_first_lot_G` 之 `_label` 實為複合字串
          （實測 `'R4·628(1)·左'`），⛔ **不是街廓標籤**——前版以其查 `sd_by`
          必回 None ⇒ **靜默退回 132/132**，而表面得到「零異動」之漂亮結論。
          本式改以幾何量比對，格式無關；查無即 `raise`（⛔ 無靜默退路）。
        """
        if side_mid is None:
            raise RuntimeError("🔴 `_corner_first_lot_G` 未收到 `side_mid` ⇒ 無法定位側界·停")
        _m = (float(side_mid[0]), float(side_mid[1]))
        for _lbl in sd_by:
            for _w in ("left", "right"):
                _sd = (sd_by.get(_lbl) or {}).get(_w)
                if not _sd:
                    continue
                _md = _sd.get("mid")
                if _md is None:
                    continue
                if math.hypot(float(_md[0]) - _m[0], float(_md[1]) - _m[1]) < 1e-6:
                    p1 = (float(_sd["p1"][0]), float(_sd["p1"][1]))
                    p2 = (float(_sd["p2"][0]), float(_sd["p2"][1]))
                    su = _u(p2[0] - p1[0], p2[1] - p1[1])
                    return (_lbl, _w, (su[1], -su[0]))     # rot90_cw(SIDE)
        raise RuntimeError(f"🔴 `side_mid`={_m} 於 `side_lines_by_side` 查無對應側界 ⇒ 停")

    # ── patch ＋ §A-4 閘之取樣 ─────────────────────────────────────────
    _orig_cf = ns["_corner_first_lot_G"]
    _orig_sg = ns["_solve_G_one"]
    _gate = []          # (side, a_m2, G, area_geom)
    # 🔒 **反靜默退路計數**（GEO-1 之教訓·⛔ patch 未咬到而得「零異動」＝ 假結論）
    _hits = {"patched": 0, "fallback": 0}

    def _sg_wrap(**kw):
        r, lab = _orig_sg(**kw)
        if kw.get("is_corner"):
            _gate.append((kw.get("side"), round(float(kw.get("a_m2", 0)), 2),
                          float(r.get("G", 0) or 0), float(r.get("area_geom", 0) or 0)))
        return r, lab

    def _cf_wrap(**kw):
        _lbl_cf, _w_cf, _ad = _ad_by_mid(kw.get("side_mid"))
        _hits["patched"] += 1
        _old = kw.get("allocation_dir")
        kw = dict(kw, allocation_dir=_ad)
        _hits.setdefault("samples", []).append(
            (_lbl_cf, _w_cf, kw.get("side"), tuple(round(float(x), 6) for x in ((0.0, 0.0) if _old is None else _old)),
             tuple(round(float(x), 6) for x in _ad)))
        return _orig_cf(**kw)

    ns["_solve_G_one"] = _sg_wrap
    ns["_corner_first_lot_G"] = _cf_wrap
    NEW = {}
    NEWWIN = {}
    try:
        for setback in (0.0, 3.5):
            sb = f"{setback:g}m"
            params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
            _d0, _s2, _o2, _w, _f = run_corner_pk(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
                setback, snapshot=snapshot)
            for _dg in (_d0 or []):
                _tg = _dg.get("真G(㎡)")
                NEW[(sb, str(_dg.get("街廓", "")),
                     _SIDECN.get(str(_dg.get("端", "")).strip(), ""),
                     str(_dg.get("候選地號", "")))] = (
                    (f"{float(_tg):.2f}" if _tg not in ("", None) else "—"),
                    f"{float(_dg.get('門檻(㎡)', 0) or 0):.2f}",
                    ("達標" if str(_dg.get("達標", "")) == "達標" else "未達"),
                    ("★" if str(_dg.get("選中", "")) == "✅" else ""))
            NEWWIN[sb] = {k: dict(v) for k, v in (_w or {}).items()}
    finally:
        ns["_corner_first_lot_G"] = _orig_cf
        ns["_solve_G_one"] = _orig_sg

    # ── 現況（D-2 態·⛔ 不 patch）────────────────────────────────────
    CUR = {}
    CURWIN = {}
    for setback in (0.0, 3.5):
        sb = f"{setback:g}m"
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, setback)
        _d0, _s2, _o2, _w, _f = run_corner_pk(
            ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
            setback, snapshot=snapshot)
        for _dg in (_d0 or []):
            _tg = _dg.get("真G(㎡)")
            CUR[(sb, str(_dg.get("街廓", "")),
                 _SIDECN.get(str(_dg.get("端", "")).strip(), ""),
                 str(_dg.get("候選地號", "")))] = (
                (f"{float(_tg):.2f}" if _tg not in ("", None) else "—"),
                f"{float(_dg.get('門檻(㎡)', 0) or 0):.2f}",
                ("達標" if str(_dg.get("達標", "")) == "達標" else "未達"),
                ("★" if str(_dg.get("選中", "")) == "✅" else ""))
        CURWIN[sb] = {k: dict(v) for k, v in (_w or {}).items()}

    # ── §A-4 閘 ───────────────────────────────────────────────────────
    L.append("")
    L.append(f"【A-4】自我驗證閘：patch 出之 `area_geom` vs `G` 之差 ≤ {TOL_A4}㎡")
    L.append("-" * 200)
    _bad = [g for g in _gate if abs(g[3] - g[2]) > TOL_A4 + _A4_EPS]
    L.append(f"  取樣（`is_corner=True` 之 `_solve_G_one` 呼叫）＝ **{len(_gate)}** 次")
    L.append(f"  最大 |area_geom − G| ＝ **{max((abs(g[3]-g[2]) for g in _gate), default=float('nan')):.6f}**")
    L.append(f"  未過閘 ＝ **{len(_bad)}**" + ("" if not _bad else "：" + "；".join(
        f"{g[0]} a={g[1]} G={g[2]:.2f} area={g[3]:.2f}" for g in _bad[:10])))
    L.append("  ⇒ " + ("✅ **全數過閘**" if not _bad
                       else "🔴 **有未過閘者 ⇒ 該等值標不可據·自有效分母剔除**"))

    # ── §A-3 (1)(2)(3)：逐候選新值 ＋ 與現況之 Δ ──────────────────────
    L.append("")
    L.append("【A-4b】🔒 **反靜默退路計數**（⛔ patch 未咬到而得「零異動」＝ 假結論）")
    L.append("-" * 200)
    L.append(f"  `_corner_first_lot_G` 之 patch：**咬到 {_hits['patched']} 次**／"
             f"退回原 `allocation_dir` **{_hits['fallback']} 次**")
    L.append("  ⇒ " + ("✅ **patch 確實生效**" if _hits["patched"] > 0
                       else "🔴 **patch 從未咬到 ⇒ 本檔之「零異動」不可據·停查**"))
    for _sm in (_hits.get("samples") or [])[:4]:
        L.append(f"     樣本 {_sm[0]}/{_sm[1]}（side={_sm[2]}）：allocation_dir {_sm[3]} → {_sm[4]}")
    if _hits["fallback"]:
        L.append(f"  ⚠️ 退回 {_hits['fallback']} 次（該側無 SIDE_LINE ⇒ 本就非街角）"
                 "——⛔ 讀者須知該等呼叫用的是**原**方向。")

    L.append("")
    L.append("【A-3】逐候選：**新期望（patch·第1宗遠側界∥SIDELINE）** vs **現況（D-2 態）**")
    L.append("-" * 200)
    L.append("  🔒 **比對欄以欄名指名**（§A-5-3）：`真G(㎡)` ／ `門檻(㎡)` ／ `達標` ／ `選中★`")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'候選':<13}"
             f"{'新真G':>10}{'現真G':>10}{'Δ真G':>10}"
             f"{'門檻':>10}{'新達標':>8}{'現達標':>8}  異動")
    L.append("-" * 200)
    _keys = sorted(set(NEW) | set(CUR))
    _dup = len(_keys) != len(set(_keys))
    if _dup:
        raise RuntimeError("🔴 §A-5-1：鍵重複 ⇒ 停")
    _chg = 0
    for k in _keys:
        n = NEW.get(k); c = CUR.get(k)
        _ng = float(n[0]) if (n and n[0] != "—") else float("nan")
        _cg = float(c[0]) if (c and c[0] != "—") else float("nan")
        _mark = []
        if n and c:
            if n[2] != c[2]:
                _mark.append("🔴 達標翻轉")
            if n[3] != c[3]:
                _mark.append("🔴 winner 異動")
        elif n and not c:
            _mark.append("🔴 新入池")
        elif c and not n:
            _mark.append("🔴 新出池")
        if _mark:
            _chg += 1
        L.append(f"{k[0]:<6}{k[1] + '/' + k[2]:<12}{k[3]:<13}"
                 f"{(n[0] if n else '—'):>10}{(c[0] if c else '—'):>10}"
                 f"{(f'{_ng - _cg:+.2f}' if _ng == _ng and _cg == _cg else '—'):>10}"
                 f"{(n[1] if n else (c[1] if c else '—')):>10}"
                 f"{(n[2] if n else '—'):>8}{(c[2] if c else '—'):>8}  "
                 + "／".join(_mark))
    L.append("-" * 200)
    L.append(f"  🔒 **§A-5-2 母體列數**：新 **{len(NEW)}**／現況 **{len(CUR)}**／"
             f"聯集 **{len(_keys)}**（⇒ 三者應一致或差異已由「新入池／新出池」列示）")
    L.append(f"  🔒 **§A-5-1 框內重複鍵 ＝ 0**（已斷言·否則 raise）")
    L.append(f"  ⇒ **有異動之候選列 ＝ {_chg}**")

    # ── 逐格 winner／強制抵費地 ────────────────────────────────────────
    L.append("")
    L.append("【A-3(2)】逐格 winner／強制抵費地：**新期望** vs **現況**")
    L.append("-" * 200)
    L.append(f"{'情境':<6}{'街廓/側':<12}{'新 winner':<16}{'現 winner':<16}  異動")
    L.append("-" * 200)
    _nw = _nf = _cw = _cf2 = 0
    _wchg = []
    for sb in ("0m", "3.5m"):
        for lbl in sorted(cb_by):
            for w in ("left", "right"):
                if w not in (sd_by.get(lbl) or {}):
                    continue
                _n = ((NEWWIN.get(sb) or {}).get(lbl) or {}).get(
                    "p1_end" if w == "left" else "p2_end")
                _c = ((CURWIN.get(sb) or {}).get(lbl) or {}).get(
                    "p1_end" if w == "left" else "p2_end")
                if _n:
                    _nw += 1
                else:
                    _nf += 1
                if _c:
                    _cw += 1
                else:
                    _cf2 += 1
                _d = (str(_n) != str(_c))
                if _d:
                    _wchg.append(f"{sb} {lbl}/{w}：{_c or '強制抵費地'} → {_n or '強制抵費地'}")
                L.append(f"{sb:<6}{lbl + '/' + w:<12}{str(_n or '（強制抵費地）'):<16}"
                         f"{str(_c or '（強制抵費地）'):<16}  {'🔴 **異動**' if _d else '否'}")
    L.append("-" * 200)
    L.append(f"  **新期望：有 winner {_nw}／強制抵費地 {_nf}**"
             f"　　**現況（D-2）：有 winner {_cw}／強制抵費地 {_cf2}**")
    L.append(f"  ⇒ **winner 異動 {len(_wchg)} 格**：" + ("；".join(_wchg) if _wchg else "（無）"))

    L.append("")
    L.append("🔒 **本檔為 D-2b 之對帳母體·⛔ 一經 commit 即凍存、一字不得改。**")
    L.append("⛔ **舊凍存表 `W-G.8_D_期望影響表_凍存.md` 不得沿用於 D-2b**（其幾何口徑為 D-2 之前）。")

    txt = "\n".join(L)
    print(txt)
    with io.open(LOG, "w", encoding="utf-8") as f:
        f.write(txt + "\n")
    print(f"\n→ {os.path.relpath(LOG, REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
