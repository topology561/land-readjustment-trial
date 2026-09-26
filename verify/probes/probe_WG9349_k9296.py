# -*- coding: utf-8 -*-
"""W-G.9-349 量測器（發單側窗四十五擬·檔 F8·⛔ 由受單側改一字）：`K-9-29 六`（入池閘）＋ 閘二之接線（`K-9-12`／`K-9-13`／`K-9-33`）。

子命令（一律 python verify/probes/probe_WG9349_k9296.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·只 harvest `app.py`）：`k929_6_enabled` 之解析、`k929_6_unbuildable` 之四項、
           `k917_should_drop` 之旗標二態、`k929_6_fixpoint` 之九例（合併·標的·佔位·a′·入池·三停機·不收斂·判別力）。
  run      <repo> <退縮> [<out.json>]
           harness 生產入口（`run_corner_pk_k6b` → `run_step_g`）跑一情境；旗標取自環境（`WV_K929_6`）。出艙：
           合併紀錄、不配地（含其由）、逐街廓之配地宗數與 ΣG；並驗：
             R1 旗標 on ⇒ 配地列中非街角第 1 宗者，⛔ 有內接矩形／最小建築面積不合格、⛔ 有 S(m) < 畸零地寬 − 0.006；
                旗標 off ⇒ 同一量出艙其數（判別力：須 > 0 方證 R1 非恆綠·本案 3.5 m 為 25）；
             R2 旗標 on ⇒ 不配地紀錄皆含「不配地由」且非「—」；off ⇒ 皆⛔ 含該鍵；
             R3 旗標 on ⇒ 回傳含 `k929_6`；合併紀錄之「結果」∈ {留置, 入池, 續併}；留置者之標的在配地列、其 a 面積 ＝ 「a 合計」（±0.01）；
                off ⇒ 回傳⛔ 含 `k929_6`。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import contextlib, copy, io, json, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _rect(x0, x1, y0=0.0, y1=30.0):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]


def selftest(repo):
    ns, _ = _harvest(repo)
    red = []
    _need = ["k929_6_enabled", "k929_6_unbuildable", "k929_6_fixpoint", "k917_should_drop"]
    _miss = [n for n in _need if n not in ns]
    if _miss:
        print(f"  🔴 受詞缺：{_miss}")
        print(f"⇒ 紅 ['受詞缺']；rc 1")
        return 1

    def chk(name, got, exp):
        ok = (got == exp)
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name)

    def chk_raise(name, fn, frag):
        try:
            fn()
        except RuntimeError as e:
            ok = frag in str(e)
            print(("  ✅ " if ok else "  🔴 ") + f"{name}：停機 {'含' if ok else '⛔ 含'}「{frag}」")
            if not ok:
                red.append(name)
            return
        print(f"  🔴 {name}：未停機（期含「{frag}」）")
        red.append(name)

    # ── 旗標 ──
    env0 = os.environ.get("WV_K929_6")
    for v, exp in ((None, True), ("", True), ("on", True), ("ON", True), ("off", False)):
        if v is None:
            os.environ.pop("WV_K929_6", None)
        else:
            os.environ["WV_K929_6"] = v
        chk(f"旗標 {v!r}", ns["k929_6_enabled"](), exp)
    os.environ["WV_K929_6"] = "x"
    chk_raise("旗標 'x'", ns["k929_6_enabled"], "只接受 on／off")
    os.environ.pop("WV_K929_6", None)

    # ── 不能建築項 ──
    U = ns["k929_6_unbuildable"]
    lg = lambda **k: {"_lg_cols": dict({"驗_A幾何": "合格", "驗_C面積": "不適用", "驗_A_W": 3.5}, **k)}
    chk("U1 內接矩形不合格", U(dict(lg(驗_A幾何="不合格"), S_raw=5.0)), ["內接矩形"])
    chk("U2 S 3.49 < W 3.5", U(dict(lg(), S_raw=3.49)), ["臨正街寬"])
    chk("U3 S ＝ W 合格（題三）", U(dict(lg(), S_raw=3.5)), [])
    chk("U4 W 取不到 ⇒ 臨正街寬⛔ 判", U(dict(lg(驗_A_W="—"), S_raw=1.0)), [])
    chk("U5 最小建築面積不合格", U(dict(lg(驗_C面積="不合格"), S_raw=5.0)), ["最小建築面積"])
    chk("U6 無從判定⛔ 當不合格", U(dict(lg(驗_A幾何="無從判定"), S_raw=5.0)), [])
    chk("U7 S_raw 缺 ⇒ 取 S", U(dict(lg(), S=2.0)), ["臨正街寬"])

    # ── k917_should_drop 之二態 ──
    SD = ns["k917_should_drop"]
    rA = {"_lg_cols": {"驗_B藍影": "合格", "驗_A幾何": "不合格", "驗_A_W": 3.5}, "S_raw": 5.0}
    rB = {"_lg_cols": {"驗_B藍影": "不合格", "驗_A幾何": "合格", "驗_A_W": 3.5}, "S_raw": 5.0}
    chk("D1 on·A 不合格·有後繼", SD(rA, False, True, "left", "B", "x")[0], True)
    chk("D2 on·A 不合格·末位", SD(rA, False, False, "left", "B", "x")[0], True)
    chk("D3 on·A 不合格·街角第 1 宗", SD(rA, True, True, "left", "B", "x")[0], False)
    chk("D4 on·藍影不合格·末位", SD(rB, False, False, "left", "B", "x")[0], True)
    os.environ["WV_K929_6"] = "off"
    chk("D5 off·A 不合格", SD(rA, False, True, "left", "B", "x")[0], False)
    chk_raise("D6 off·藍影不合格·末位（本批前之 loud）", lambda: SD(rB, False, False, "left", "B", "x"), "K-9-9 六")
    os.environ.pop("WV_K929_6", None)

    # ── k929_6_fixpoint ──
    FP = ns["k929_6_fixpoint"]
    FL = {"B": {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}}
    PRICE = {"z1": 1000.0, "z2": 2000.0}

    def P(pid, x0, x1, a, zone="z1", lot=None):
        return {"暫編地號": pid, "原地號": lot or pid, "所屬街廓": "B", "分攤登記面積_m2": a, "面積_m2": 0.0,
                "重劃前地價區段": zone, "polygon_coords": _rect(x0, x1)}

    def mk_trial(rule, side="left", corner=()):
        """rule(build) -> set(不配地之暫編)；G ＝ a × 0.6；其餘入配地列。"""
        def trial(b):
            dropped = rule(b)
            rows, dl = [], []
            for t in b:
                a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
                if t["暫編地號"] in dropped:
                    dl.append({"暫編地號": t["暫編地號"], "G(㎡)": round(a * 0.6, 4)})
                else:
                    rows.append({"暫編地號": t["暫編地號"], "推進側別": side, "G(㎡)": a * 0.6,
                                 "驗_宗序": "街角第1宗" if t["暫編地號"] in corner else "其後"})
            return rows, ({("B", side): dl} if dl else {}), None
        return trial

    own = {"L1": "G1", "L2": "G1", "L3": "G1", "L4": "G2", "L5": "G1"}
    small = lambda b: {t["暫編地號"] for t in b if float(t["分攤登記面積_m2"]) + float(t["面積_m2"]) < 150}

    # F1：X1(300·過)｜X2(60·不過)｜X3(40·不過) 同歸戶相鄰（左推進）⇒ 併入 X1、佔 X1 之位（投影最小）、留置
    b1 = [P("X1", 0, 10, 300, lot="L1"), P("X2", 10, 12, 60, lot="L2"), P("X3", 12, 13, 40, lot="L3")]
    bf, out, log = FP(b1, mk_trial(small), own, PRICE, FL)
    chk("F1 合併一次", len(log), 1)
    chk("F1 標的 ＝ 個別 G 最大", log[0]["標的"] if log else None, "X1")
    chk("F1 佔位（左·投影最小）", log[0]["佔位"] if log else None, "X1")
    chk("F1 a 合計", log[0]["a 合計"] if log else None, 400.0)
    chk("F1 結果", log[0]["結果"] if log else None, "留置")
    chk("F1 末態 build", sorted(t["暫編地號"] for t in bf), ["X1"])
    chk("F1 入參⛔ 改寫", [t["面積_m2"] for t in b1], [0.0, 0.0, 0.0])
    # F2：同 F1 而右推進 ⇒ 佔位 ＝ 投影最大（X3）；標的仍 X1
    bf2, _, log2 = FP(copy.deepcopy(b1), mk_trial(small, side="right"), own, PRICE, FL)
    chk("F2 佔位（右·投影最大）", log2[0]["佔位"] if log2 else None, "X3")
    chk("F2 單元之名 ＝ 標的", [t["暫編地號"] for t in bf2], ["X1"])
    chk("F2 單元之位 ＝ 佔位者之幾何", bf2[0]["polygon_coords"] if bf2 else None, _rect(12, 13))
    # F3：皆不過、合併仍不過 ⇒ 入池（無停機）
    b3 = [P("Y1", 0, 2, 60, lot="L1"), P("Y2", 2, 4, 50, lot="L2")]
    _, out3, log3 = FP(b3, mk_trial(lambda b: {t["暫編地號"] for t in b}), own, PRICE, FL)
    chk("F3 結果 ＝ 入池", log3[0]["結果"] if log3 else None, "入池")
    # F4：a′ 之折算（Y2 於 z2·標的 Y1 於 z1 ⇒ a′ ＝ 50 × 2000 ÷ 1000 ＝ 100）
    b4 = [P("Y1", 0, 2, 60, lot="L1"), P("Y2", 2, 4, 50, zone="z2", lot="L2")]
    _, _, log4 = FP(b4, mk_trial(small), own, PRICE, FL)
    chk("F4 併入量 a′", log4[0]["併入量(a′)"] if log4 else None, 100.0)
    # F5：異歸戶相鄰（L4）與同歸戶不相鄰（L5）⇒ 皆⛔ 合併
    b5 = [P("Z1", 0, 2, 60, lot="L1"), P("Z2", 2, 4, 300, lot="L4"), P("Z3", 20, 22, 300, lot="L5")]
    _, _, log5 = FP(b5, mk_trial(small), own, PRICE, FL)
    chk("F5 無合併", len(log5), 0)
    # F6：合併組含街角第 1 宗 ⇒ 停機
    chk_raise("F6 含街角第 1 宗", lambda: FP(copy.deepcopy(b1), mk_trial(small, corner=("X1",)), own, PRICE, FL),
              "含街角第 1 宗")
    # F7：跨左右推進 ⇒ 停機
    def trial7(b):
        rows, dl = [], []
        for t in b:
            a = float(t["分攤登記面積_m2"]) + float(t["面積_m2"])
            if a < 150:
                dl.append({"暫編地號": t["暫編地號"], "G(㎡)": a * 0.6})
            else:
                rows.append({"暫編地號": t["暫編地號"], "推進側別": "right", "G(㎡)": a * 0.6, "驗_宗序": "其後"})
        return rows, {("B", "left"): dl}, None
    chk_raise("F7 跨左右推進", lambda: FP(copy.deepcopy(b1), trial7, own, PRICE, FL), "非單一")
    # F8：含原位可配者之合併單元終不配地 ⇒ 停機
    chk_raise("F8 一達一未達之反例",
              lambda: FP(copy.deepcopy(b1), mk_trial(lambda b: small(b) | {"X1"} if len(b) == 1 else small(b)),
                         own, PRICE, FL), "一達一未達")
    # F9：輪數上限
    chk_raise("F9 逾輪", lambda: FP(copy.deepcopy(b1), mk_trial(small), own, PRICE, FL, max_rounds=1), "未收斂")
    # 判別力：無不配地 ⇒ 無合併、build 原物件
    bf0, _, log0 = FP(b1, mk_trial(lambda b: set()), own, PRICE, FL)
    chk("判別力 無不配地 ⇒ 無合併", (len(log0), bf0 == b1), (0, True))
    if env0 is None:
        os.environ.pop("WV_K929_6", None)
    else:
        os.environ["WV_K929_6"] = env0
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def run(repo, sb, out=None):
    ns, fake_st = _harvest(repo)
    import run_verification as rv
    from selection_pipeline import run_corner_pk_k6b
    from stepg_pipeline import run_step_g
    on = ns["k929_6_enabled"]()
    with contextlib.redirect_stdout(io.StringIO()):
        snapshot = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
        rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _d, _s, _o, wins, forced, tp3, bp3 = run_corner_pk_k6b(
                ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p, sb, snapshot=snapshot)
            ns["K917_DROPPED"].clear()
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot, params, bp3, wins, forced, sb,
                            eff_min_build_by_blk={})
    except RuntimeError as e:
        print(f"🔴 執行中止：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
        return 3
    rows = sg["g_rows"]
    drops = {f"{k[0]}/{k[1]}": v for k, v in ns["K917_DROPPED"].items()}
    red = []
    print(f"【F8 run】退縮 {sb}·WV_K929_6 ＝ {os.environ.get('WV_K929_6')!r}（啟用 {on}）")
    # R1
    bad = []
    for r in rows:
        pid = str(r.get("暫編地號"))
        if "抵費地" in pid or r.get("第1筆街角") == "是" or r.get("推進側別") not in ("left", "right"):
            continue
        why = []
        if str(r.get("驗_A幾何", "")).strip() == "不合格":
            why.append("內接矩形")
        if str(r.get("驗_C面積", "")).strip() == "不合格":
            why.append("最小建築面積")
        try:
            if float(r.get("S(m)")) < float(r.get("驗_A_W")) - 0.006:
                why.append("臨正街寬")
        except (TypeError, ValueError):
            pass
        if why:
            bad.append((r.get("所屬街廓"), pid, why))
    print(f"  R1 配地列中不能建築（非街角第 1 宗）之宗數 ＝ {len(bad)}")
    for b in bad:
        print(f"     {b}")
    if on and bad:
        red.append("R1")
    if not on and not bad:
        print("  🔴 R1 判別力：off 態之數為 0 ⇒ R1 可能恆綠")
        red.append("R1 判別力")
    # R2
    recs = [e for v in drops.values() for e in v]
    has = [("不配地由" in e) for e in recs]
    if on:
        ok2 = all(has) and all(e.get("不配地由") not in (None, "—") for e in recs)
    else:
        ok2 = not any(has)
    print(("  ✅" if ok2 else "  🔴") + f" R2 不配地紀錄 {len(recs)} 筆之「不配地由」")
    for k in sorted(drops):
        for e in drops[k]:
            print(f"     {k} {e.get('暫編地號')} G {e.get('G(㎡)')} 由 {e.get('不配地由', '（無此鍵）')}")
    if not ok2:
        red.append("R2")
    # R3
    k = sg.get("k929_6")
    if on:
        ok3 = k is not None
        rowby = {str(r.get("暫編地號")): r for r in rows}
        for L in (k or {}).get("log", []):
            print(f"     合併 {L}")
            if L.get("結果") not in ("留置", "入池", "續併"):
                ok3 = False
            if L.get("結果") == "留置":
                r = rowby.get(L["標的"])
                if r is None or abs(float(r.get("a 面積(㎡)") or 0) - float(L["a 合計"])) > 0.01:
                    ok3 = False
    else:
        ok3 = k is None
    print(("  ✅" if ok3 else "  🔴") + f" R3 入池閘之回傳（{'有' if k is not None else '無'}）與合併紀錄")
    if not ok3:
        red.append("R3")
    blk = {}
    for r in rows:
        pid = str(r.get("暫編地號"))
        if "抵費地" in pid or r.get("推進側別") not in ("left", "right"):
            continue
        d = blk.setdefault(r.get("所屬街廓"), [0, 0.0])
        d[0] += 1
        d[1] += float(r.get("G(㎡)") or 0)
    print("  逐街廓（配地宗數·ΣG）：" + "；".join(f"{b} {v[0]}·{v[1]:.2f}" for b, v in sorted(blk.items())))
    if out:
        json.dump({"rows": [{kk: r.get(kk) for kk in ("暫編地號", "所屬街廓", "推進側別", "a 面積(㎡)", "G(㎡)")}
                            for r in rows], "dropped": drops, "k929_6": (k or {}).get("log")},
                  open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _wiring_checks(app_src, stepg_src):
    """回 {檢名: bool}（AST·⛔ 執行）。"""
    import ast
    out = {}
    A = ast.parse(app_src)
    fns = {n.name: n for n in A.body if isinstance(n, ast.FunctionDef)}
    out["W1 模組層四函式"] = all(k in fns for k in
                              ("k929_6_enabled", "k929_6_unbuildable", "k929_6_fixpoint", "_k929_6_screen_gate"))
    f = fns.get("f3_screen_stepg_run")
    ok2 = False
    if f is not None:
        kw = [a.arg for a in f.args.kwonlyargs]
        dft = dict(zip(kw, f.args.kw_defaults))
        has_kw = "_k929_6_inner" in dft and isinstance(dft["_k929_6_inner"], ast.Constant) \
            and dft["_k929_6_inner"].value is False
        calls = [n for n in ast.walk(f) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                 and n.func.id == "_k929_6_screen_gate"]
        ok2 = has_kw and len(calls) == 1
    out["W2 配地本體之首呼叫入池閘（_k929_6_inner 預設 False·呼叫恰一）"] = ok2
    ok3 = False
    if f is not None:
        src_f = ast.get_source_segment(app_src, f) or ""
        ok3 = ("st.session_state['f3_k929_6_log'] = _k929_6_log" in src_f
               and "st.session_state.pop('f3_k929_6_log', None)" in src_f)
    out["W3 配地本體寫／去 f3_k929_6_log"] = ok3
    keys = None
    for n in A.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "K6B_SCREEN_TRIAL_KEYS"
                                             for t in n.targets):
            keys = ast.literal_eval(n.value)
    out["W4 f3_k929_6_log ∈ K6B_SCREEN_TRIAL_KEYS"] = bool(keys) and "f3_k929_6_log" in keys
    m = fns.get("main")
    ok5 = False
    if m is not None:
        src_m = ast.get_source_segment(app_src, m) or ""
        ok5 = "st.session_state.get('f3_k929_6_log')" in src_m and "K-9-29 六" in src_m
    out["W5 main() 之成果區顯示合併紀錄"] = ok5
    names = None
    for n in A.body:
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "_WF_NS_NAMES" for t in n.targets):
            names = ast.literal_eval(n.value)
    out["W6 _WF_NS_NAMES 納三名"] = bool(names) and all(
        k in names for k in ("k929_6_enabled", "k929_6_fixpoint", "K917_DROPPED"))
    S = ast.parse(stepg_src)
    rg = next((n for n in S.body if isinstance(n, ast.FunctionDef) and n.name == "run_step_g"), None)
    ok7 = False
    if rg is not None:
        a = [x.arg for x in rg.args.args]
        src_r = ast.get_source_segment(stepg_src, rg) or ""
        ok7 = "_k929_6_inner" in a and 'ns["k929_6_fixpoint"]' in src_r and 'ns["k929_6_enabled"]()' in src_r
    out["W7 harness run_step_g 之入池閘"] = ok7
    sd = fns.get("k917_should_drop")
    ok8 = False
    if sd is not None:
        src_s = ast.get_source_segment(app_src, sd) or ""
        ok8 = "k929_6_unbuildable(res)" in src_s and src_s.count("k929_6_enabled()") == 2
    out["W8 k917_should_drop 之二處接線"] = ok8
    return out


def wiring(repo):
    app_src = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    stepg_src = open(os.path.join(repo, "verify", "stepg_pipeline.py"), encoding="utf-8").read()
    res = _wiring_checks(app_src, stepg_src)
    red = [k for k, v in res.items() if not v]
    for k, v in res.items():
        print(("  ✅ " if v else "  🔴 ") + k)
    # 突變（判別力）：本部全綠時，四種突變須各使其所守之檢轉紅
    muts = [
        ("M1 去 K6B_SCREEN_TRIAL_KEYS 之 f3_k929_6_log", "app",
         "    'f3_k929_6_log',\n)", "\n)", "W4 f3_k929_6_log ∈ K6B_SCREEN_TRIAL_KEYS"),
        ("M2 配地本體之入池閘呼叫改名", "app",
         "build_parcels, _k929_6_log = _k929_6_screen_gate(st, dict(",
         "build_parcels, _k929_6_log = _k929_6_screen_gate_X(st, dict(",
         "W2 配地本體之首呼叫入池閘（_k929_6_inner 預設 False·呼叫恰一）"),
        ("M3 main() 之顯示去之", "app",
         "_k929_6_log_v = st.session_state.get('f3_k929_6_log')", "_k929_6_log_v = None",
         "W5 main() 之成果區顯示合併紀錄"),
        ("M4 harness 之入池閘去之", "stepg",
         'if not _k929_6_inner and ns["k929_6_enabled"]():', "if False:",
         "W7 harness run_step_g 之入池閘"),
    ]
    if not red:
        for name, which, old, new, target in muts:
            a2, s2 = app_src, stepg_src
            if which == "app":
                if a2.count(old) != 1:
                    print(f"  🔴 {name}：突變錨命中 {a2.count(old)}（須 1）⇒ 器紅")
                    red.append(name)
                    continue
                a2 = a2.replace(old, new)
            else:
                if s2.count(old) != 1:
                    print(f"  🔴 {name}：突變錨命中 {s2.count(old)}（須 1）⇒ 器紅")
                    red.append(name)
                    continue
                s2 = s2.replace(old, new)
            r2 = _wiring_checks(a2, s2)
            ok = (r2.get(target) is False)
            print(("  ✅ " if ok else "  🔴 ") + f"{name} ⇒ 「{target}」{'轉紅' if ok else '⛔ 轉紅'}")
            if not ok:
                red.append(name)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "selftest":
        sys.exit(selftest(a[1]))
    if len(a) >= 3 and a[0] == "run":
        sys.exit(run(a[1], float(a[2]), a[3] if len(a) > 3 else None))
    if len(a) >= 2 and a[0] == "wiring":
        sys.exit(wiring(a[1]))
    print(__doc__)
    sys.exit(2)
