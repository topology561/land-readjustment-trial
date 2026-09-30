# -*- coding: utf-8 -*-
"""W-G.9-360 量測器（發單側窗五十八擬·檔 F19·⛔ 由受單側改一字）：調配之候選街廓名單（`W-G.9-359` ＋ 補令一、二）之
以程式字樣為錨之突變——量測器 `F18`（`verify/probes/probe_WG9359_cand.py`）之判別力。

緣由：`W-G.9-359 §四-2`（逐字）「發單側讀 CC 之碼後補寫、另以零生產碼之單入倉：以程式字樣為錨之接線檢查（`R-2` 之二
條件、`R-7` 之八鍵與同深之判、`R-9` 之資料來源、`X-2` 之字樣）及其突變之判別力（`§一` 項 `8` 之十三突變之形）；併入主線
之請示。」——接線與行為已由 `F18` 之 `wiring`（`W1`〜`W6`）與 `selftest`（`C1`〜`C26`·`30` 例）量之；本器補其判別力：
於記憶體中對工作樹之 `app.py`／`verify/run_verification.py` 之文字施以字樣為錨之突變（⛔ 寫檔、⛔ 符號連結），以 `F18`
之判式（`_extract_ns`／`_cases`／`_report`／`_wiring_checks`）量之。突變之形 ＝ 原單 `§一` 項 `8` 之十三、補令一 `§二`
末之四、補令二 `§二` 末之十，另加 `F18 wiring` 各項之突變與 `Z2` 之突變。

子命令（一律 python verify/probes/probe_WG9360_cand_mut.py mut <repo>）：
  本部
    Z0  受詞在：<repo>/verify/probes/probe_WG9359_cand.py 可載，其 _extract_ns／_cases／_report／_wiring_checks 皆在；
        <repo>/app.py、<repo>/verify/run_verification.py 可讀。
    Z1  未突變之態全綠：`F18` 之例（經 _extract_ns 自 app.py 之文字抽出受詞）皆 ✅（`30` 例）；`F18` 之 W1〜W6 皆 ✅。
    Z2  補令二 `R-6″` ①（「閱畢全部所取之列後」一次列出）：所取之列 ＝ [含 NaN 之列（QA／壞一）, 混維之環之列（QM／混維·
        其首二元皆有限·其多邊形之建置拋非 RuntimeError）] ⇒ adj_pool_anchor 拋 RuntimeError，其訊息含 QA、壞一，⛔ 含 QM。
  判別力：本部全綠時另施 `41` 種突變（_muts），每一突變須使其所指之項轉紅（所指 ⊆ 轉紅）；突變之錨於其檔須恰命中 `1`。
    所指之項唯含 C／P0 者 ⇒ 唯量 selftest（與 Z2）；含 W 者 ⇒ 另量 wiring。
rc：0 相符／1 不符（含受詞缺、器紅）／2 用法錯。
"""
import contextlib, importlib.util, io, os, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

FA, FR = "app.py", "verify/run_verification.py"
F18_REL = "verify/probes/probe_WG9359_cand.py"
NEED = ("_extract_ns", "_cases", "_report", "_wiring_checks")


def _read(repo, rel):
    with open(os.path.join(repo, *rel.split("/")), encoding="utf-8") as f:
        return f.read()


def _load_f18(repo):
    p = os.path.join(repo, *F18_REL.split("/"))
    spec = importlib.util.spec_from_file_location("probe_WG9359_cand_for_f19", p)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _selftest_red(f18, app_src):
    """F18 之例經 _extract_ns 量之 ⇒ 紅項之名（抽出失敗 ⇒ ['抽出']）。"""
    try:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ns = f18._extract_ns(app_src)
            miss = [n for n in f18.FUNCS + f18.CONSTS if n not in ns]
            if miss:
                return ["受詞缺"], None
            cases = f18._cases(ns)
            red = f18._report(cases, verbose=False)
        return list(red), ns
    except Exception as ex:  # noqa: BLE001
        return [f"抽出:{type(ex).__name__}"], None


def _wiring_red(f18, app_src, rv_src):
    try:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = f18._wiring_checks(app_src, rv_src)
        return [n.split()[0] for n, ok, _ in res if not ok]
    except Exception as ex:  # noqa: BLE001
        return [f"W:{type(ex).__name__}"]


def _z2(ns):
    """補令二 R-6″ ①：壞損之一次列出⛔ 為他列之多邊形之建置所奪。"""
    if ns is None or "adj_pool_anchor" not in ns:
        return False, "受詞缺"
    rows = [{"推進側別": ns["ADJ_POOL_SIDE"], "所屬街廓": "QA", "暫編地號": "壞一",
             "cut_coords": [[10, -1], [12, -1], [float("nan"), float("nan")], [12, 1], [10, 1]]},
            {"推進側別": ns["ADJ_POOL_SIDE"], "所屬街廓": "QM", "暫編地號": "混維",
             "cut_coords": [[0, 0], [2, 0, 5], [2, 2], [0, 2]]}]
    try:
        with contextlib.redirect_stdout(io.StringIO()), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ns["adj_pool_anchor"](rows)
        return False, "未停"
    except RuntimeError as ex:
        m = str(ex)
        return ("QA" in m and "壞一" in m and "QM" not in m), f"RuntimeError：{m[:80]}"
    except Exception as ex:  # noqa: BLE001
        return False, f"非 RuntimeError 穿出：{type(ex).__name__}"


def _all_red(f18, app_src, rv_src, with_wiring):
    red, ns = _selftest_red(f18, app_src)
    ok2, _ = _z2(ns)
    if not ok2:
        red = red + ["Z2"]
    if with_wiring:
        red = red + _wiring_red(f18, app_src, rv_src)
    return red


# ── 突變 ── 各為 (名, 所指之項, [(檔, 錨, 代)])
_POOL_TWO = (
    "    _bad = [f\"{_r.get('所屬街廓')}／{_r.get('暫編地號')}\" for _r in _taken if _coords_bad(_r.get('cut_coords'))]\n"
    "    if _bad:\n"
    "        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值（非數、無窮大或缺·資料之瑕·\"\n"
    "                           \"位置無從定）：%s ⇒ 停機\" % '、'.join(_bad))\n"
    "    # ②③\n"
    "    _best = {}\n"
    "    for _r in _taken:\n"
    "        _p = Polygon(_r.get('cut_coords'))\n")
_POOL_ONE = (
    "    _bad = []\n"
    "    _best = {}\n"
    "    for _r in _taken:\n"
    "        if _coords_bad(_r.get('cut_coords')):\n"
    "            _bad.append(f\"{_r.get('所屬街廓')}／{_r.get('暫編地號')}\")\n"
    "            continue\n"
    "        _p = Polygon(_r.get('cut_coords'))\n")
_POOL_END = "    _out = {}\n    for _b, (_k, _p) in _best.items():\n"
_POOL_END_ONE = ("    if _bad:\n"
                 "        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片之坐標含非數值：%s ⇒ 停機\" % '、'.join(_bad))\n"
                 + _POOL_END)
_POOL_EXC = "        except (TypeError, ValueError, OverflowError, IndexError, KeyError):\n            return True\n\n    _taken"
_POOL_FIN = ("        # 補令二 `R-6″` ①（與 `adj_candidate_lists` 之錨點之坐標之檢同一式）\n        try:\n"
             "            return not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)")
_BAD = "    _bad = [f\"{_r.get('所屬街廓')}／{_r.get('暫編地號')}\" for _r in _taken if _coords_bad(_r.get('cut_coords'))]\n"
_ANCH = ("        if _coords_bad(_cs):\n"
         "            raise RuntimeError(f\"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之坐標含非數值\"")
_AREA = "        if adj_q2(_p.area) == 0:\n            continue\n"
_ANCH_POLY = ("        _p = Polygon(_cs)\n        if not _p.is_valid:\n            _p = _p.buffer(0)\n        if _p.is_empty:\n"
              "            raise RuntimeError(f\"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之多邊形為空 ⇒ 停機\")\n")


def _muts():
    return [
        # 原單 §一 項 8 之十三
        ("M1 同深改嚴格小於", ["C6"], [(FA, "                if abs(_dd) <= _tolq:\n", "                if abs(_dd) < _tolq:\n")]),
        ("M2 較寬者⛔ 排最後", ["C5"],
         [(FA, "_r5 = (0, _j5 - _i5) if _j5 >= _i5 else (1, _i5 - _j5)", "_r5 = (0, abs(_j5 - _i5))")]),
        ("M3 最小建築面積之級反向", ["C2"],
         [(FA, "_r2 = (0, _i2 - _j2) if _j2 <= _i2 else (1, _j2 - _i2)", "_r2 = (0, _j2 - _i2) if _j2 >= _i2 else (1, _i2 - _j2)")]),
        ("M4 原街廓⛔ 居首", ["C12"], [(FA, "            _items += _rest\n", "            _items = _rest + _items\n")]),
        ("M5 正面道路⛔ 比", ["C3"],
         [(FA, "_r3 = 0 if _c['正面道路'] == _s['正面道路'] else 1", "_r3 = 0")]),
        ("M6 較深與較淺同組", ["C6"],
         [(FA, "                    _r6, _dlab = (1, _dd), '較深'\n", "                    _r6, _dlab = (0, abs(_dd)), '較深'\n")]),
        ("M7 錨點取最小", ["C11"],
         [(FA, "_a = min(_sl, key=lambda _r: (-float(_r['原有面積']), str(_r['暫編地號'])))",
           "_a = min(_sl, key=lambda _r: (float(_r['原有面積']), str(_r['暫編地號'])))")]),
        ("M8 迄點取最小之抵費地", ["C14"],
         [(FA, "        _k = (-float(_p.area), str(_r.get('暫編地號')))\n", "        _k = (float(_p.area), str(_r.get('暫編地號')))\n")]),
        ("M9 偶數捨入", ["C17"],
         [(FA, "    from decimal import Decimal, ROUND_HALF_UP\n    return Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)\n",
           "    from decimal import Decimal, ROUND_HALF_EVEN\n    return Decimal(repr(float(x))).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)\n")]),
        ("M10 往大者⛔ 標第二趟排除", ["C2"], [(FA, "'第二趟排除': _r2[0] == 1})", "'第二趟排除': False})")]),
        ("M11 廣場得為正面道路", ["C15", "W2"], [(FA, "    \"廣場\": False,\n    \"綠地\": False,\n", "    \"廣場\": True,\n    \"綠地\": False,\n")]),
        ("M12 公設軌依街廓名", ["C10"], [(FA, "'鍵': (_r7[_t], _t), '使用分區': _dash,", "'鍵': (_t, _r7[_t]), '使用分區': _dash,")]),
        ("M13 深度差⛔ 取二位", ["C18"],
         [(FA, "        _d = _pos_q2((depth_by or {}).get(_l), '深度', _l)\n",
           "        _d = _pos_q2((depth_by or {}).get(_l), '深度', _l)\n        _d = (depth_by or {}).get(_l)\n")]),
        # 補令一 §二 末之四（其一依補令二 裁一改錨：退化 ＝ 面積以 adj_q2 計為 0）
        ("M14 退化之池列仍停機", ["C19", "C23"],
         [(FA, _AREA, "        if adj_q2(_p.area) == 0:\n            raise RuntimeError('🔴 退化之池列')\n")]),
        ("M15 錨點退化改取原多邊形", ["C20"],
         [(FA, _ANCH_POLY, _ANCH_POLY.replace(
             "        if _p.is_empty:\n            raise RuntimeError(f\"🔴 [W-G.9-359 候選街廓名單] 歸戶 {_g!r} 之錨點 {_aid!r} 之多邊形為空 ⇒ 停機\")\n",
             "        if _p.is_empty:\n            _p = Polygon(_cs)\n"))]),
        ("M16 錨點⛔ buffer(0)", ["C21"],
         [(FA, _ANCH_POLY, _ANCH_POLY.replace("        if not _p.is_valid:\n            _p = _p.buffer(0)\n", ""))]),
        ("M17 最小建築面積負值⛔ 停", ["C22"],
         [(FA, "            _ok = _q.is_finite() and _q >= 0\n", "            _ok = _q.is_finite()\n")]),
        # 補令二 §二 末之十
        ("M18 面積之判改 is_empty", ["C23"], [(FA, _AREA, "        if _p.is_empty:\n            continue\n")]),
        ("M19 面積之判改 area < 0.01", ["C23"], [(FA, _AREA, "        if _p.area < 0.01:\n            continue\n")]),
        ("M20 面積之判改 area <= 0.005", ["C23"], [(FA, _AREA, "        if _p.area <= 0.005:\n            continue\n")]),
        ("M21 去池片之坐標之檢", ["C24", "C25"],
         [(FA, "    if _bad:\n        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片",
           "    if False:\n        raise RuntimeError(\"🔴 [W-G.9-359 候選街廓名單] 下列抵費地之片")]),
        ("M22 池片遇首個壞損即停", ["C25"], [(FA, _BAD, _BAD + "    _bad = _bad[:1]\n")]),
        ("M23 去錨點之坐標之檢", ["C26"], [(FA, _ANCH, _ANCH.replace("if _coords_bad(_cs):", "if False:"))]),
        ("M24 池片之檢唯判 NaN", ["C24", "C25"],
         [(FA, _POOL_FIN, _POOL_FIN.replace(
             "not all(_m.isfinite(float(_pt[0])) and _m.isfinite(float(_pt[1])) for _pt in _cs)",
             "any(_m.isnan(float(_pt[0])) or _m.isnan(float(_pt[1])) for _pt in _cs)"))]),
        ("M25 未滿 3 點之列亦檢", ["C25"],
         [(FA, _BAD, _BAD.replace("for _r in _taken if",
                                  "for _r in [_x for _x in (g_rows or []) if _x.get('推進側別') == ADJ_POOL_SIDE] if"))]),
        ("M26 轉換之例外唯攔 TypeError", ["C24"],
         [(FA, _POOL_EXC, _POOL_EXC.replace("(TypeError, ValueError, OverflowError, IndexError, KeyError)", "(TypeError,)"))]),
        ("M27 轉換之例外不攔 OverflowError", ["C24"], [(FA, _POOL_EXC, _POOL_EXC.replace("OverflowError, ", ""))]),
        # CC 依第三輪審查所改之兩段式（補令二 R-6″ ①·本器 Z2）
        ("M28 壞損之檢與多邊形之建置同迴圈", ["Z2"], [(FA, _POOL_TWO, _POOL_ONE), (FA, _POOL_END, _POOL_END_ONE)]),
        # F18 wiring 各項（R-2 之二條件、R-9 之資料來源、X-2 之字樣、具名常數、驗證路徑之名稱檔）
        ("M29 同深之容差改 0.5", ["W1"], [(FA, "\nADJ_DEPTH_TIE_TOL_M = 0.1\n", "\nADJ_DEPTH_TIE_TOL_M = 0.5\n")]),
        ("M30 名單之函式之預設改字面", ["W1"],
         [(FA, "def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=ADJ_DEPTH_TIE_TOL_M):",
           "def adj_candidate_lists(intake, blk_ctx, pool_anchor, slice_coords, tol=0.1):")]),
        ("M31 顯示列之函式之預設改字面", ["W1"],
         [(FA, "def adj_candidate_rows(cand, tol=ADJ_DEPTH_TIE_TOL_M):", "def adj_candidate_rows(cand, tol=0.1):")]),
        ("M32 正面道路推導⛔ 限道路類", ["W3"],
         [(FA, "         if _lr not in _buildable_blocks\n         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})",
           "         if _lr not in _buildable_blocks})")]),
        ("M33 正面道路推導⛔ 限非可建築", ["W3"],
         [(FA, "         if _lr not in _buildable_blocks\n         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})",
           "         if F3_CATEGORY_FRONT_ROAD.get(_br.get('category', ''), False)})")]),
        ("M34 新函式含 session 之字樣", ["W4"], [(FA, "    _dash = '—'\n    _out = []\n", "    _dash = '—'  # session_state\n    _out = []\n")]),
        ("M35 新函式含案件字面", ["W4"],
         [(FA, "    _n = len(cand or [])\n", "    _n = len(cand or []) + 0 * len('R1')\n")]),
        ("M36 名稱以 label 取", ["W5"],
         [(FA, "{b['label']: _adj359_names.get(b['id'], '') for b in _adj359_bb}",
           "{b['label']: _adj359_names.get(b['label'], '') for b in _adj359_bb}")]),
        ("M37 路寬取他欄", ["W5"],
         [(FA, "{_l: (_adj359_sb.get(_l) or {}).get('正面路寬(m)') for _l in _adj359_lbls}",
           "{_l: (_adj359_sb.get(_l) or {}).get('路寬(m)') for _l in _adj359_lbls}")]),
        ("M38 深度取他鍵", ["W5"],
         [(FA, "st.session_state.get('f3_alloc_depth_by_label', {}) or {})\n                                _adj359_view",
           "st.session_state.get('f3_depth_by_label', {}) or {})\n                                _adj359_view")]),
        ("M39 最小建築面積取他鍵", ["W5"],
         [(FA, "st.session_state.get(K91_SS_MBA_EFFECTIVE, {}) or {},\n                                    {_l: _adj359_ident",
           "{},\n                                    {_l: _adj359_ident")]),
        ("M40 驗證路徑之名稱檔改他檔", ["W6"],
         [(FR, "FRONT_ROAD_NAMES = os.path.join(HERE, \"case_front_road_names_UC9898.json\")",
           "FRONT_ROAD_NAMES = os.path.join(HERE, \"case_params_UC9898.json\")")]),
        ("M41 驗證路徑之讀名之函式改名", ["W6"],
         [(FR, "def load_front_road_names():", "def load_front_road_names_v0():")]),
    ]


def mut(repo):
    red = []
    print("── 本部 ──")
    try:
        src = {FA: _read(repo, FA), FR: _read(repo, FR)}
        f18 = _load_f18(repo)
        miss = [n for n in NEED if not hasattr(f18, n)]
    except Exception as ex:  # noqa: BLE001
        src, f18, miss = None, None, [f"{type(ex).__name__}: {ex}"]
    print(("  ✅ " if not miss else "  🔴 ") + f"Z0 受詞在（F18 之 {list(NEED)}；app.py；verify/run_verification.py）"
          + (f"（缺 {miss}）" if miss else ""))
    if miss:
        print("⇒ 紅 ['Z0']；rc 1")
        return 1
    st_red, ns = _selftest_red(f18, src[FA])
    w_red = _wiring_red(f18, src[FA], src[FR])
    ok1 = not st_red and not w_red
    print(("  ✅ " if ok1 else "  🔴 ") + f"Z1 未突變之態全綠（F18 之例之紅 {st_red}；W1〜W6 之紅 {w_red}）")
    if not ok1:
        red.append("Z1")
    ok2, note2 = _z2(ns)
    print(("  ✅ " if ok2 else "  🔴 ") + f"Z2 補令二 R-6″ ①：壞損之一次列出⛔ 為他列之多邊形之建置所奪（{note2}）")
    if not ok2:
        red.append("Z2")
    if red:
        print("── 判別力：本部未全綠 ⇒ ⛔ 施突變 ──")
        print(f"⇒ 紅 {red}；rc 1")
        return 1
    print("── 判別力（每一突變須使其所指之項轉紅·所指 ⊆ 轉紅）──")
    for mname, target, reps in _muts():
        m = dict(src)
        miss = []
        for f, a, b in reps:
            if m[f].count(a) != 1:
                miss.append(m[f].count(a))
                continue
            m[f] = m[f].replace(a, b, 1)
        if miss:
            print(f"  🔴 {mname}：突變錨之命中 {miss}（期 各 1）")
            red.append(mname.split()[0])
            continue
        turned = _all_red(f18, m[FA], m[FR], any(t.startswith("W") for t in target))
        ok = set(target) <= set(turned)
        print(("  ✅ " if ok else "  🔴 ") + f"{mname}：轉紅 {turned}（須含 {target}）")
        if not ok:
            red.append(mname.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) != 3 or argv[1] != "mut":
        print(__doc__)
        return 2
    return mut(os.path.abspath(argv[2]))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
