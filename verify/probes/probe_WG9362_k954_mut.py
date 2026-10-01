# -*- coding: utf-8 -*-
"""W-G.9-362 量測器（發單側窗六十三擬·檔 F22·⛔ 由受單側改一字）：地籍相連之判之座標容差（`W-G.9-361` ＋ 補令一、二·
`K-9-54`）之以程式字樣為錨之接線檢查與突變——量測器 `F21`（`verify/probes/probe_WG9361_k954.py`）之判別力。

緣由：`W-G.9-361 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之精確先、
重判後；`R-2` ④ 之二向取小、相距之先篩；`R-2` ⑤ 之例外 ⇒ 不相連）及其突變之判別力」；補令一、二所增之 ④″-0〜④″-3、④‴-0′
（型之檢·⛔ 恃例外）、片之環（各多邊形部分之 exterior 與 interiors）、Hausdorff 之四端，一併及之。接線與行為已由 `F21` 之
`wiring`（`W1`〜`W5`）與 `selftest`（`A1`〜`A27`·`28` 例）量之；本器補 (一) 以 CC 之碼（`f74f95e`·`app.py` blob
`deaf07f7…`）之字樣為錨之接線（`V1`〜`V6`）、(二) `F21` 之例未及之行為（`B1`〜`B4`）、(三) 其判別力：於記憶體中對工作樹之
`app.py` 之文字施以字樣為錨之突變（⛔ 寫檔、⛔ 符號連結），以 `F21` 之判式（`_cases`／`_report`／`_wiring_checks`）與本器之
`V`／`B` 量之。

子命令（一律 python verify/probes/probe_WG9362_k954_mut.py mut <repo>）：
  本部
    Z0  受詞在：<repo>/verify/probes/probe_WG9361_k954.py 可載，其 _cases／_report／_wiring_checks／FUNCS／CONSTS 皆在；
        <repo>/verify/app_harvest.py 之 _install_fake_streamlit／_filter_module 皆在；<repo>/app.py 可讀。
    Z1  未突變之態全綠：`F21` 之例（於記憶體中 harvest 之 app.py）皆 ✅（`28` 例）；`F21` 之 W1〜W4 皆 ✅；本器之
        V1〜V6、B1〜B4 皆 ✅。
  接線（字樣·各錨於其函式之源須恰命中 `1`）
    V1  精確先、重判後：k6_shares_segment 內 `_it = _ba.intersection(_bb)` → `if _tot >= _ml: return (True, _tot)` →
        `_tol = float(K6_SHARE_COORD_TOL)` → `try:` 之序。
    V2  重判之序（④‴-0′ → ④″-0 → ④″-1 → ④″-2 → ⑤ → ④″-3）：型之檢（`_k954_areal`·任一為 None ⇒ (False, _tot)）→
        有限性之檢（`_k954_all_finite`）→ 相距（`poly_a.distance(poly_b) > _tol`）→ `_k954_vtx_len` →
        `except Exception: return (False, _tot)` → `if _l >= _ml: return (True, _l)` → `return (False, _tot)`。
    V3  型之檢（④‴-0′·⛔ 恃例外）：`_k954_areal` 以 `geom_type` 屬 ('Polygon', 'MultiPolygon') 與 `is_empty` 判之，
        其內⛔ try。
    V4  四長取小：`_k954_vtx_len` 以二軸（`_axis(_SA, _SB)`、`_axis(_SB, _SA)`）得四長，回其最小者。
    V5  Hausdorff 之四端：`_h` ＝ s′ 之二端至 t′、t′ 之二端至 s′ 之距之最大者；`_h <= tol` 者計入。
    V6  片之環：`_k954_all_finite` 與 `_k954_vtx_len` 皆逐多邊形部分取 `[exterior] + interiors`。
  行為（`F21` 之例未及者·合成·⛔ 本案資料）
    B1  ④″-2 之運算拋例外（平方下溢之極短邊 ⇒ ZeroDivisionError）⇒ (False, 精確之長〔此形 1e-05〕)（⑤·⛔ 靜默改判相連）。
    B2  含洞之 MultiPolygon：洞之環與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 4。
    B3  MultiPolygon 之一部之洞之坐標含 NaN、其外環與他片微米錯位而共線 ⇒ 二向皆不相連（④″-0 及於 interiors）。
    B4  片之環含重複之相鄰頂點（長 0 之邊）、與他片微米錯位而共線 ⇒ 相連、其長 ≈ 1（長 0 之邊略）。
  判別力：本部全綠時另施 `21` 種突變（_muts），每一突變須使其所指之項轉紅（所指 ⊆ 轉紅）；突變之錨於 app.py 須恰命中 `1`。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import ast, contextlib, importlib.util, io, math, os, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FA = "app.py"
F21_REL = "verify/probes/probe_WG9361_k954.py"
NEED21 = ("_cases", "_report", "_wiring_checks", "FUNCS", "CONSTS")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


def _load(repo, rel, name):
    p = os.path.join(repo, *rel.split("/"))
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _harvest_src(ah, src):
    """app_harvest.harvest 之記憶體版（同其 _install_fake_streamlit／_filter_module·⛔ 快取·⛔ 寫檔）。"""
    with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ah._install_fake_streamlit()
        mod, _, _ = ah._filter_module(src)
        ns = {"__name__": "app_harvested_f22", "__file__": "<app.py:f22>"}
        exec(compile(mod, "<app.py:f22>", "exec"), ns)
    return ns


def _seg(src, name):
    tree = ast.parse(src)
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
    if len(fns) != 1:
        return None, None
    return ast.get_source_segment(src, fns[0]) or "", fns[0]


# ── 接線（字樣）──
_V1 = ["_it = _ba.intersection(_bb)",
       "    if _tot >= _ml:\n        return (True, _tot)",
       "    _tol = float(K6_SHARE_COORD_TOL)",
       "    try:\n        _pa, _pb = _k954_areal(poly_a), _k954_areal(poly_b)"]
_V2 = ["        _pa, _pb = _k954_areal(poly_a), _k954_areal(poly_b)\n        if _pa is None or _pb is None:\n"
       "            return (False, _tot)",
       "        if not (_k954_all_finite(_pa) and _k954_all_finite(_pb)):\n            return (False, _tot)",
       "        if poly_a.distance(poly_b) > _tol:\n            return (False, _tot)",
       "        _l = _k954_vtx_len(_pa, _pb, _tol)",
       "    except Exception:\n        return (False, _tot)",
       "    if _l >= _ml:\n        return (True, _l)\n    return (False, _tot)"]
_V4 = ["    _la_a, _lb_a = _axis(_SA, _SB)", "    _lb_b, _la_b = _axis(_SB, _SA)",
       "    return min(_la_a, _lb_a, _lb_b, _la_b)"]
_V5 = ["                _h = max(_pt_seg(_s0[0], _s0[1], _t0, _t1), _pt_seg(_s1[0], _s1[1], _t0, _t1),\n"
       "                         _pt_seg(_t0[0], _t0[1], _s0, _s1), _pt_seg(_t1[0], _t1[1], _s0, _s1))",
       "                if _h <= tol:"]
_RING = "for _r in [_q.exterior] + list(_q.interiors):"


def _ordered(seg, anchors):
    """各錨恰命中 1 且依序 ⇒ (True, 位置)；否則 (False, 註)。"""
    pos = []
    for a in anchors:
        n = seg.count(a)
        if n != 1:
            return False, f"錨命中 {n}：{a.strip().splitlines()[0][:40]!r}"
        pos.append(seg.find(a))
    return pos == sorted(pos), f"位置 {pos}"


def _wiring_v(src):
    chk = []
    seg, _ = _seg(src, "k6_shares_segment")
    if seg is None:
        return [(f"V{i} k6_shares_segment 缺", False, "") for i in range(1, 7)]
    ok, note = _ordered(seg, _V1)
    chk.append(("V1 精確先、重判後", ok, note))
    ok, note = _ordered(seg, _V2)
    chk.append(("V2 重判之序（型之檢 → 有限性 → 相距 → 界址點之共線長 → 例外 ⇒ 不相連 → 門檻）", ok, note))
    s3, f3 = _seg(src, "_k954_areal")
    ok3, n3 = False, "無 _k954_areal"
    if s3 is not None:
        has_try = any(isinstance(x, ast.Try) for x in ast.walk(f3))
        ok3 = (s3.count("('Polygon', 'MultiPolygon')") == 1 and "geom_type" in s3 and "is_empty" in s3
               and not has_try)
        n3 = f"try {has_try}"
    chk.append(("V3 型之檢以 geom_type／is_empty（⛔ 恃例外）", ok3, n3))
    s4, _ = _seg(src, "_k954_vtx_len")
    ok4, n4 = (False, "無 _k954_vtx_len") if s4 is None else _ordered(s4, _V4)
    chk.append(("V4 四長取小（二軸 × 二片）", ok4, n4))
    ok5, n5 = (False, "無 _k954_vtx_len") if s4 is None else _ordered(s4, _V5)
    chk.append(("V5 Hausdorff 之四端", ok5, n5))
    s6, _ = _seg(src, "_k954_all_finite")
    n_fin = -1 if s6 is None else s6.count(_RING) + s6.count("    for _q in parts:\n")
    n_edg = -1 if s4 is None else s4.count(_RING) + s4.count("        for _q in _parts:\n")
    chk.append(("V6 片之環 ＝ 各多邊形部分之 exterior 與 interiors（有限性之檢、邊）", n_fin == 2 and n_edg == 2,
                f"有限性 {n_fin}／邊 {n_edg}（期 2／2）"))
    return chk


# ── 行為（合成·⛔ 本案資料）──
def _bt(res, nd=3):
    return (bool(res[0]), round(float(res[1]), nd))


def _cases_b(ns):
    from shapely.geometry import Polygon, MultiPolygon
    sh = ns["k6_shares_segment"]
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as ex:  # noqa: BLE001
            got = ("例外", type(ex).__name__)
        out.append((name, got, exp))

    # B1：極短邊（長 1e-170·其平方下溢為 0）⇒ ZeroDivisionError ⇒ ⑤
    a1 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0.5), (1e-170, 0.5)])
    b1 = Polygon([(1 + 1e-5, 0), (2, 0), (2, 1), (1 - 1e-5, 1)])
    run("B1 ④″-2 之運算拋例外（平方下溢之極短邊）⇒ 二向皆 (False, 精確之長)",
        lambda: (_bt(sh(a1, b1), 6), _bt(sh(b1, a1), 6)), ((False, 1e-05), (False, 1e-05)))
    # B2：含洞之 MultiPolygon，洞之上緣與他片之上緣微米錯位而共線（共線長 4）
    hole = Polygon([(0, 0), (10, 0), (10, -5), (0, -5)], [[(2, -1), (8, -1), (8, -4), (2, -4)]])
    far = Polygon([(20, 0), (25, 0), (25, -5), (20, -5)])
    mp2 = MultiPolygon([hole, far])
    inner = Polygon([(3, -1 - 1e-5), (7, -1 + 1e-5), (7, -3), (3, -3)])
    run("B2 含洞之 MultiPolygon：洞之環與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 4",
        lambda: (_bt(sh(mp2, inner)), _bt(sh(inner, mp2))), ((True, 4.0), (True, 4.0)))
    # B3：MultiPolygon 之一部之洞含 NaN；他部之外環與他片微米錯位而共線
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        bad = Polygon([(20, 0), (25, 0), (25, -5), (20, -5)], [[(21, -1), (22, -1), (float("nan"), -2), (21, -2)]])
        mp3 = MultiPolygon([Polygon([(0, 0), (1, 0), (1, -1), (0, -1)]), bad])
    nb3 = Polygon([(0, 1e-5), (1, -1e-5), (1, 1), (0, 1)])
    run("B3 MultiPolygon 之一部之洞之坐標含 NaN（他部之外環微米錯位而共線）⇒ 二向皆不相連",
        lambda: (bool(sh(mp3, nb3)[0]), bool(sh(nb3, mp3)[0])), (False, False))
    # B4：重複之相鄰頂點（長 0 之邊）
    a4 = Polygon([(0, 0), (1, 0), (1, 0), (1, 1), (0, 1)])
    b4 = Polygon([(0, -1), (1, -1), (1, 1e-5), (0, -1e-5)])
    run("B4 片之環含重複之相鄰頂點、與他片微米錯位而共線 ⇒ 二向皆相連、其長 ≈ 1",
        lambda: (_bt(sh(a4, b4)), _bt(sh(b4, a4))), ((True, 1.0), (True, 1.0)))
    return out


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def _all_red(f21, ah, src, verbose=False):
    red = []
    try:
        ns = _harvest_src(ah, src)
    except Exception as ex:  # noqa: BLE001
        return [f"harvest:{type(ex).__name__}"]
    miss = [n for n in list(f21.FUNCS) + list(f21.CONSTS) if n not in ns]
    if miss:
        red.append("受詞缺")
    if not [n for n in miss if n in f21.FUNCS]:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cases = f21._cases(ns)
        if verbose:
            print("── F21 之例（記憶體中 harvest 之 app.py）──")
        red += f21._report(cases, verbose=verbose)
        if verbose:
            print(f"  （{len(cases)} 例）")
        if verbose:
            print("── 本器之行為（B）──")
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            red += _report(_cases_b(ns), verbose=verbose)
    try:
        w21 = f21._wiring_checks(src, None)
    except Exception as ex:  # noqa: BLE001
        w21 = [(f"W:{type(ex).__name__}", False, "")]
    wv = _wiring_v(src)
    if verbose:
        print("── F21 之接線（W1〜W4）與本器之接線（V1〜V6）──")
        for name, ok, note in w21 + wv:
            print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
    red += [n.split()[0] for n, ok, _ in w21 + wv if not ok]
    return red


# ── 突變 ── 各為 (名, 所指之項, [(錨, 代)])
_EARLY = "    if _tot >= _ml:\n        return (True, _tot)          # 精確之長達門檻 ⇒ 相連·其長 ＝ 精確之長（同本批前）\n"
_TYPE = "        if _pa is None or _pb is None:\n            return (False, _tot)\n"
_FIN = "        if not (_k954_all_finite(_pa) and _k954_all_finite(_pb)):\n            return (False, _tot)\n"
_DIST = "        if poly_a.distance(poly_b) > _tol:\n            return (False, _tot)\n"
_AREAL = ("    _gt = getattr(poly, 'geom_type', None)\n    if _gt not in ('Polygon', 'MultiPolygon') or poly.is_empty:\n"
          "        return None\n    return [poly] if _gt == 'Polygon' else list(poly.geoms)\n")
_FIN_LOOP = ("    for _q in parts:\n        for _r in [_q.exterior] + list(_q.interiors):\n"
             "            for _c in _r.coords:\n")
_EDG_LOOP = ("        for _q in _parts:\n            for _r in [_q.exterior] + list(_q.interiors):\n"
             "                _cs = [(float(_c[0]), float(_c[1])) for _c in _r.coords]\n")
_H4 = _V5[0]
_H2 = "                _h = max(_pt_seg(_s0[0], _s0[1], _t0, _t1), _pt_seg(_s1[0], _s1[1], _t0, _t1))"
_PRE = "                if (_gx * _gx + _gy * _gy) ** 0.5 > tol:\n                    continue\n"
_EXC = "    except Exception:\n        return (False, _tot)\n    if _l >= _ml:\n"
_TAIL = "    if _l >= _ml:\n        return (True, _l)\n    return (False, _tot)\n"


def _muts():
    return [
        ("M1 去精確之判之早返（一律重判）", ["V1"], [(_EARLY, "")]),
        ("M2 型之檢改恃例外", ["V3"],
         [(_AREAL, "    return [poly] if poly.geom_type == 'Polygon' else list(poly.geoms)\n")]),
        ("M3 去型之檢之判（None ⇒ 例外）", ["V2"], [(_TYPE, "")]),
        ("M4 去有限性之檢", ["A19", "A24", "V2"], [(_FIN, "")]),
        ("M5 有限性之檢唯及第一部", ["A24", "V6"],
         [(_FIN_LOOP, _FIN_LOOP.replace("    for _q in parts:\n", "    for _q in parts[:1]:\n"))]),
        ("M6 有限性之檢唯及 exterior", ["B3", "V6"],
         [(_FIN_LOOP, _FIN_LOOP.replace("[_q.exterior] + list(_q.interiors)", "[_q.exterior]"))]),
        ("M7 去相距之檢", ["V2"], [(_DIST, "")]),
        ("M8 相距之檢先於型之檢與有限性之檢", ["V2"],
         [(_TYPE + _FIN + _DIST, _DIST + _TYPE + _FIN)]),
        ("M9 邊唯取第一部", ["A23", "V6"],
         [(_EDG_LOOP, _EDG_LOOP.replace("        for _q in _parts:\n", "        for _q in _parts[:1]:\n"))]),
        ("M10 邊唯取 exterior", ["B2", "V6"],
         [(_EDG_LOOP, _EDG_LOOP.replace("[_q.exterior] + list(_q.interiors)", "[_q.exterior]"))]),
        ("M11 長 0 之邊⛔ 略", ["B4"],
         [("                    if _cs[_i] != _cs[_i + 1]:\n", "                    if True:\n")]),
        ("M12 四長取大", ["V4"],
         [("    return min(_la_a, _lb_a, _lb_b, _la_b)", "    return max(_la_a, _lb_a, _lb_b, _la_b)")]),
        ("M13 唯一軸（二長取小）", ["V4"],
         [("    return min(_la_a, _lb_a, _lb_b, _la_b)", "    return min(_la_a, _lb_a)")]),
        ("M14 Hausdorff 唯 s′ 之二端", ["V5"], [(_H4, _H2)]),
        ("M15 H 之門檻減半", ["A21", "V5"],
         [("                if _h <= tol:\n", "                if _h <= tol / 2:\n")]),
        ("M16 先篩過嚴（外接矩形相離即略）", ["A27"], [(_PRE, _PRE.replace("> tol:", "> 0.0:"))]),
        ("M17 例外 ⇒ 相連", ["B1", "V2"],
         [(_EXC, "    except Exception:\n        return (True, _tot)\n    if _l >= _ml:\n")]),
        ("M18 重判相連而回精確之長", ["A4", "V2"],
         [(_TAIL, "    if _l >= _ml:\n        return (True, _tot)\n    return (False, _tot)\n")]),
        ("M19 重判不相連而回界址點之共線長", ["A6", "V2"],
         [(_TAIL, "    if _l >= _ml:\n        return (True, _l)\n    return (False, _l)\n")]),
        ("M20 容差以字面", ["W2", "W3", "V1"],
         [("    _tol = float(K6_SHARE_COORD_TOL)\n", "    _tol = 0.0001\n")]),
        ("M21 相距之檢之容差改 0", ["A27", "V2"],
         [(_DIST, _DIST.replace("> _tol:", "> 0.0:"))]),
    ]


def mut(repo):
    red = []
    print("── 本部 ──")
    try:
        src = _read(repo, FA)
        f21 = _load(repo, F21_REL, "probe_WG9361_k954_for_f22")
        sys.path.insert(0, os.path.join(repo, "verify"))
        ah = _load(repo, "verify/app_harvest.py", "app_harvest_for_f22")
        miss = [n for n in NEED21 if not hasattr(f21, n)] + \
               [n for n in ("_install_fake_streamlit", "_filter_module") if not hasattr(ah, n)]
    except Exception as ex:  # noqa: BLE001
        print(f"  🔴 Z0 受詞缺：{type(ex).__name__}: {ex}")
        print("⇒ 紅 ['Z0']；rc 1")
        return 1
    if miss:
        print(f"  🔴 Z0 受詞缺：{miss}")
        print("⇒ 紅 ['Z0']；rc 1")
        return 1
    print("  ✅ Z0 受詞在（F21 之判式、app_harvest 之二函式、app.py）")
    base = _all_red(f21, ah, src, verbose=True)
    ok1 = not base
    print(("  ✅" if ok1 else "  🔴") + f" Z1 未突變之態全綠（紅 {base}）")
    if not ok1:
        red.append("Z1")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（突變 ⇒ 所指之項轉紅）──")
    for name, want, edits in _muts():
        s = src
        bad = None
        for anc, rep in edits:
            n = s.count(anc)
            if n != 1:
                bad = f"錨命中 {n}"
                break
            s = s.replace(anc, rep)
        if bad:
            print(f"  🔴 {name}：{bad}")
            red.append(name.split()[0])
            continue
        got = _all_red(f21, ah, s)
        ok = set(want) <= set(got)
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：所指 {want}；轉紅 {got}")
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) == 3 and argv[1] == "mut":
        return mut(os.path.abspath(argv[2]))
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
