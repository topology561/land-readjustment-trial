# -*- coding: utf-8 -*-
"""W-G.9-344 量測器：段三（K-6 §二 段三 ＋ K-9-48）之落地驗收。

子命令（一律 python verify/probes/probe_WG9344_k6s3.py <子命令> …）：
  run     <repo> <退縮> <on|off|unset|legacy> <out.json>
          on／off／unset：設（或清）環境變數 WV_K6B_STAGE3 後，走 harness 之段三入口
          selection_pipeline.run_corner_pk_k6b → stepg_pipeline.run_step_g，落檔逐宗結果。
          legacy：⛔ 走段三入口，改走 run_corner_pk（段三落地前之路徑·供改前態）。
  oracle  <repo> <退縮> <out.json>
          期望之改後態（⛔ 呼叫任何段三碼）：以 legacy 路徑，對逐宗面積依本案之併入表手動改寫後重跑。
          併入表 ＝ KL 於發單側窗三十九放行之改後配地（本案專用·受測例·⛔ 生產碼）。
  cmp     <a.json> <b.json>        逐宗（面積／分配面積／判／宗序）、抵費地、街角得標、強制旗標；容差 0.01
  noaff   <pre.json> <post.json> <街廓,…>   「不影響原位次」（K-9-48 其三）：（甲）改前保留者改後仍保留（扣本步被併出者）；（乙）容不下內接矩形之配餘地片數不增
  table   <pre.json> <post.json>   改前改後之土地影響（街角、地主宗、抵費地）
  selftest                         必綠／必紅之合成對照（⛔ 讀倉）
rc：0 ＝ 期／同；1 ＝ 相異或檢核不合；2 ＝ 用法錯；3 ＝ 受詞缺（無從量測·⛔ 等同不合）。
"""
import contextlib, copy, io, json, os, sys, time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01
ENV = "WV_K6B_STAGE3"
NUM_KEYS = ("a 面積(㎡)", "G(㎡)")
STR_KEYS = ("驗_總判", "驗_宗序", "推進側別")


def _boot(repo, sb):
    os.environ["WV_K6_STEP0"] = os.environ.get("WV_K6_STEP0", "") or "off"
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    import run_verification as rv
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
        rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        tp, bp, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snap)
        params = rv.build_param_table(ns, fake_st, cb_by, cad, snap, sb)
    return ns, fake_st, snap, cb_by, cad, tp, bp, params


def _materialize(ns, fake_st, snap, cb_by, cad, params, tp, bp, wins, forced, sb):
    from stepg_pipeline import run_step_g
    from shapely.geometry import Polygon
    ns["K917_DROPPED"].clear()
    err = None
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snap, params, bp, wins, forced, sb,
                            eff_min_build_by_blk={})
            rows = sg["g_rows"]
        except RuntimeError as e:
            err = str(e).split("\n")[0][:300]
            rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    own = fake_st.session_state.get("t8_ownership_map", {}) or {}
    orig = {t["暫編地號"]: t.get("原地號") for t in tp}
    pools = []
    for r in rows:
        if "抵費地" in str(r.get("暫編地號")) and r.get("cut_coords") and not isinstance(r.get("cut_coords"), str):
            P = Polygon(r["cut_coords"]).buffer(0)
            blk = r["所屬街廓"]
            prow = [p for p in params if p["街廓"] == blk][0]
            ms = ns["get_min_lot_size"](cb_by[blk].get("category", ""), float(prow.get("正面路寬(m)", 0) or 0))
            ok = bool(ns["_rect_fits_free_pose"](P, float(ms["min_width"]), float(ms["min_depth"]))) if P.area > 0 else None
            pools.append({"池": r["暫編地號"], "所屬街廓": blk, "面積": round(P.area, 2), "容納內接矩形": ok})
    out_rows = [{**{k: r.get(k) for k in ("暫編地號", "所屬街廓") + NUM_KEYS + STR_KEYS},
                 "歸戶": own.get(orig.get(r.get("暫編地號")), "")} for r in rows]
    dropped = {f"{k[0]}/{k[1]}": sorted({d["暫編地號"] for d in v}) for k, v in ns["K917_DROPPED"].items()}
    return {"SB": sb, "err": err, "rows": out_rows, "pools": pools, "dropped": dropped,
            "wins": {k: {kk: v.get(kk) for kk in ("p1_end", "p2_end")} for k, v in wins.items()},
            "forced": {k: {kk: bool(v.get(kk)) for kk in ("left_forced_offset", "right_forced_offset")}
                       for k, v in forced.items()}}


def cmd_run(repo, sb, mode, out):
    if mode not in ("on", "off", "unset", "legacy"):
        return _usage()
    if mode in ("on", "off"):
        os.environ[ENV] = mode
    else:
        os.environ.pop(ENV, None)
    t0 = time.time()
    ns, fst, snap, cb_by, cad, tp, bp, params = _boot(repo, sb)
    import selection_pipeline as sp
    log = None
    if mode == "legacy":
        with contextlib.redirect_stdout(io.StringIO()):
            _d, _s, _o, wins, forced = sp.run_corner_pk(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb,
                                                         snapshot=snap)
        bp2 = bp
    else:
        if not hasattr(sp, "run_corner_pk_k6b"):
            print("🔴 受詞缺：verify/selection_pipeline.py 無 run_corner_pk_k6b（段三入口未落地）⇒ 無從量測")
            return 3
        with contextlib.redirect_stdout(io.StringIO()):
            _d, _s, _o, wins, forced, _tp2, bp2 = sp.run_corner_pk_k6b(
                ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
        log = fst.session_state.get("f3_k6b_stage3_log")
    res = _materialize(ns, fst, snap, cb_by, cad, params, tp, bp2, wins, forced, sb)
    res["mode"] = mode
    res["env"] = os.environ.get(ENV)
    res["stage3_log"] = log
    res["sec"] = round(time.time() - t0, 1)
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    print(json.dumps({"mode": mode, "SB": sb, "err": res["err"], "n": len(res["rows"]), "wins": res["wins"],
                      "stage3_log_rows": (len(log) if isinstance(log, list) else log), "sec": res["sec"]},
                     ensure_ascii=False))
    return 0


# 本案之併入表（KL 放行·發單側窗三十九）：目標宗 ← 整筆併入者；道路片依其所在道路街廓之中心線切分；公設地上土地（含路口片）二街廓平分
ORACLE_WHOLE = {"628-45(2)": ["628-30(3)", "628-30(2)"], "628-45(1)": ["628-20(2)", "628-30(1)"],
                "628-41(1)": ["628-41(2)", "628-41(3)"]}
ORACLE_ROAD_SPLIT = ["628-45(5)", "628-30(4)"]           # 依中心線切分，入 628-45(2)（R3 側）／628-45(1)（R5 側）
ORACLE_PUB_HALF = ["628-45(4)", "628-45(3)"]             # 平分入二者
ORACLE_SIDE = {"628-45(2)": "R3", "628-45(1)": "R5"}


def cmd_oracle(repo, sb, out):
    os.environ.pop(ENV, None)
    ns, fst, snap, cb_by, cad, tp, bp, params = _boot(repo, sb)
    import selection_pipeline as sp
    from shapely.geometry import Polygon, LineString
    from shapely.ops import split
    if sb == 0.0:
        tpm, bpm, plan = tp, bp, {}
    else:
        tpm = copy.deepcopy(tp)
        by = {t["暫編地號"]: t for t in tpm}
        bpm = [by[b["暫編地號"]] for b in bp]
        a = lambda k: float(by[k]["分攤登記面積_m2"])
        add = {k: sum(a(m) for m in ms) for k, ms in ORACLE_WHOLE.items()}
        plan = {"whole": ORACLE_WHOLE, "road": {}, "pub": {}}
        blk_poly = {k: Polygon(v["vertices"]).buffer(0) for k, v in cb_by.items()}
        for k in ORACLE_ROAD_SPLIT:
            poly = Polygon(by[k]["polygon_coords"]).buffer(0)
            cl = cad["centerlines"][by[k]["所屬街廓"]]
            (x1, y1), (x2, y2) = cl[0], cl[-1]
            dx, dy = x2 - x1, y2 - y1
            L = (dx * dx + dy * dy) ** 0.5
            ux, uy = dx / L, dy / L
            line = LineString([(x1 - ux * 500, y1 - uy * 500), (x2 + ux * 500, y2 + uy * 500)])
            parts = list(split(poly, line).geoms)
            if len(parts) != 2:
                print(f"🔴 oracle：{k} 經中心線切分得 {len(parts)} 片（期 2）⇒ 量測器紅")
                return 3
            for q in parts:
                tgt = [t for t, b in ORACLE_SIDE.items() if q.distance(blk_poly[b]) < 0.05]
                if len(tgt) != 1:
                    print(f"🔴 oracle：{k} 之半片鄰接目標街廓數 {len(tgt)}（期 1）⇒ 量測器紅")
                    return 3
                share = a(k) * q.area / poly.area
                add[tgt[0]] += share
                plan["road"].setdefault(k, {})[tgt[0]] = round(share, 4)
        for k in ORACLE_PUB_HALF:
            for t in ORACLE_SIDE:
                add[t] += a(k) / 2
                plan["pub"].setdefault(k, {})[t] = round(a(k) / 2, 4)
        rm = {m for ms in ORACLE_WHOLE.values() for m in ms}
        for t, v in add.items():
            by[t]["分攤登記面積_m2"] = round(a(t) + v, 2)
        bpm = [b for b in bpm if b["暫編地號"] not in rm]
        plan["a_after"] = {t: by[t]["分攤登記面積_m2"] for t in add}
    with contextlib.redirect_stdout(io.StringIO()):
        _d, _s, _o, wins, forced = sp.run_corner_pk(ns, fst, list(cb_by.values()), cad, params, tpm, bpm, sb,
                                                     snapshot=snap)
    res = _materialize(ns, fst, snap, cb_by, cad, params, tpm, bpm, wins, forced, sb)
    res["mode"] = "oracle"
    res["plan"] = plan
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    print(json.dumps({"mode": "oracle", "SB": sb, "err": res["err"], "n": len(res["rows"]),
                      "a_after": plan.get("a_after") if plan else None}, ensure_ascii=False))
    return 0


def _load(p):
    return json.load(open(p, encoding="utf-8"))


def _cmp(A, B):
    diffs = []
    ia = {(r["所屬街廓"], r["暫編地號"]): r for r in A["rows"]}
    ib = {(r["所屬街廓"], r["暫編地號"]): r for r in B["rows"]}
    for k in sorted(set(ia) | set(ib)):
        ra, rb = ia.get(k), ib.get(k)
        if ra is None or rb is None:
            diffs.append(f"宗 {k} 僅見於 {'b' if ra is None else 'a'}")
            continue
        for f in NUM_KEYS:
            va, vb = float(ra.get(f) or 0), float(rb.get(f) or 0)
            if abs(va - vb) > TOL:
                diffs.append(f"宗 {k} {f} {va} ≠ {vb}")
        for f in STR_KEYS:
            if (ra.get(f) or "") != (rb.get(f) or ""):
                diffs.append(f"宗 {k} {f} {ra.get(f)} ≠ {rb.get(f)}")
    pa = {p["池"]: p for p in A["pools"]}
    pb = {p["池"]: p for p in B["pools"]}
    for k in sorted(set(pa) | set(pb)):
        x, y = pa.get(k), pb.get(k)
        if x is None or y is None or abs(x["面積"] - y["面積"]) > TOL or x["容納內接矩形"] != y["容納內接矩形"]:
            diffs.append(f"抵費地 {k} {x} ≠ {y}")
    for f in ("wins", "forced", "dropped", "err"):
        if A.get(f) != B.get(f):
            diffs.append(f"{f} {A.get(f)} ≠ {B.get(f)}")
    return diffs


def cmd_cmp(a, b):
    d = _cmp(_load(a), _load(b))
    for x in d:
        print("  ", x)
    print(f"相異 {len(d)} 項 ⇒ {'✅ 同' if not d else '🔴 異'}")
    return 0 if not d else 1


def _noaff(pre, post, blks):
    """回 (判, 列)：判 ∈ {'ok','bad','undecidable'}。
    （甲）改前保留者（扣本步被併出者）改後仍保留；（乙）面積 > 0 而容不下內接矩形之配餘地片數，改後 ≤ 改前。
    改前或改後之配地中止（err）⇒ 'undecidable'（無從判定·⛔ 與「不合」共用出艙碼）。"""
    rm = set()
    for t in (post.get("stage3_log") or []):
        if isinstance(t, dict) and t.get("結果") == "成":
            rm |= set(t.get("整筆併入") or [])
    rm |= {m for ms in ((post.get("plan") or {}).get("whole") or {}).values() for m in ms}
    rm -= {m for ms in ((pre.get("plan") or {}).get("whole") or {}).values() for m in ms}
    kept = lambda d, b: {r["暫編地號"] for r in d["rows"] if r["所屬街廓"] == b and r.get("驗_總判") == "保留"}
    nbad = lambda d, b: sum(1 for p in d["pools"] if p["所屬街廓"] == b and p["面積"] > 0 and p["容納內接矩形"] is False)
    ok, lines = True, []
    for b in blks:
        lost = sorted((kept(pre, b) - rm) - kept(post, b))
        b0, b1 = nbad(pre, b), nbad(post, b)
        okp = b1 <= b0
        ok &= (not lost) and okp
        pl = [(p["池"], p["面積"], p["容納內接矩形"]) for p in post["pools"] if p["所屬街廓"] == b and p["面積"] > 0]
        lines.append(f"  {b}（甲）失 {lost} ⇒ {'✅' if not lost else '🔴'}；（乙）容不下之配餘地 改前 {b0}／改後 {b1} "
                     f"{pl} ⇒ {'✅' if okp else '🔴'}")
    lines.append(f"  err 改前 {pre.get('err')}｜改後 {post.get('err')}")
    if pre.get("err") is not None or post.get("err") is not None:
        return "undecidable", lines
    return ("ok" if ok else "bad"), lines


def cmd_noaff(pre, post, blks):
    st, lines = _noaff(_load(pre), _load(post), blks.split(","))
    print("\n".join(lines))
    print({"ok": "⇒ ✅ 不影響原位次", "bad": "⇒ 🔴 影響原位次", "undecidable": "⇒ 🔴 無從判定（配地中止）"}[st])
    return {"ok": 0, "bad": 1, "undecidable": 3}[st]


def cmd_table(pre, post):
    A, B = _load(pre), _load(post)
    for blk in sorted({r["所屬街廓"] for r in A["rows"]} | {r["所屬街廓"] for r in B["rows"]}):
        f = lambda d: {s: v for s, v in (d["wins"].get(blk) or {}).items()}
        ia = {r["暫編地號"]: r for r in A["rows"] if r["所屬街廓"] == blk and "抵費地" not in r["暫編地號"]}
        ib = {r["暫編地號"]: r for r in B["rows"] if r["所屬街廓"] == blk and "抵費地" not in r["暫編地號"]}
        pa = [p["面積"] for p in A["pools"] if p["所屬街廓"] == blk]
        pb = [p["面積"] for p in B["pools"] if p["所屬街廓"] == blk]
        ch = []
        for k in sorted(set(ia) | set(ib)):
            ra, rb = ia.get(k), ib.get(k)
            sa = "—" if ra is None else f"{ra['G(㎡)']}{'' if ra['驗_總判'] == '保留' else ' 未達'}"
            sb = "—" if rb is None else f"{rb['G(㎡)']}{'' if rb['驗_總判'] == '保留' else ' 未達'}"
            if sa != sb or (ra and rb and ra.get("驗_宗序") != rb.get("驗_宗序")):
                own = (ra or rb).get("歸戶", "")
                ch.append(f"     {k}〔{own}〕 {sa}（{(ra or {}).get('驗_宗序')}） ⇒ {sb}（{(rb or {}).get('驗_宗序')}）")
        print(f"  ── {blk}　街角 改前 {f(A)} → 改後 {f(B)}｜抵費地片 改前 {pa}（計 {round(sum(pa), 2)}）"
              f"→ 改後 {pb}（計 {round(sum(pb), 2)}）")
        print("\n".join(ch) if ch else "     （逐宗不變）")
    return 0


def cmd_selftest():
    base = {"SB": 3.5, "err": None, "wins": {"X": {"p1_end": "a", "p2_end": None}},
            "forced": {"X": {"left_forced_offset": False, "right_forced_offset": False}}, "dropped": {},
            "rows": [{"暫編地號": "a", "所屬街廓": "X", "a 面積(㎡)": 100.0, "G(㎡)": 60.0, "驗_總判": "保留",
                      "驗_宗序": "街角第1宗", "推進側別": "left", "歸戶": "G1"},
                     {"暫編地號": "b", "所屬街廓": "X", "a 面積(㎡)": 50.0, "G(㎡)": 30.0, "驗_總判": "保留",
                      "驗_宗序": "其後", "推進側別": "left", "歸戶": "G2"},
                     {"暫編地號": "c", "所屬街廓": "X", "a 面積(㎡)": 40.0, "G(㎡)": 24.0, "驗_總判": "保留",
                      "驗_宗序": "其後", "推進側別": "right", "歸戶": "G1"}],
            "pools": [{"池": "X-抵費地", "所屬街廓": "X", "面積": 500.0, "容納內接矩形": True}]}
    res = []
    b2 = copy.deepcopy(base)
    res.append(("cmp 同物（必綠）", len(_cmp(base, b2)) == 0))
    b3 = copy.deepcopy(base); b3["rows"][1]["G(㎡)"] = 30.02
    res.append(("cmp 分配面積差 0.02（必紅）", len(_cmp(base, b3)) == 1))
    b4 = copy.deepcopy(base); b4["rows"][1]["G(㎡)"] = 30.005
    res.append(("cmp 差 0.005 在容差內（必綠）", len(_cmp(base, b4)) == 0))
    b5 = copy.deepcopy(base); b5["wins"]["X"]["p1_end"] = None
    res.append(("cmp 街角得標異（必紅）", len(_cmp(base, b5)) == 1))
    post = copy.deepcopy(base)
    post["rows"] = [r for r in post["rows"] if r["暫編地號"] != "c"]
    post["stage3_log"] = [{"結果": "成", "整筆併入": ["c"]}]
    res.append(("noaff 本步被併出者⛔ 計失（必綠）", _noaff(base, post, ["X"])[0] == "ok"))
    p2 = copy.deepcopy(post); p2["rows"][1]["驗_總判"] = "剔除"
    res.append(("noaff 原保留者改後未達（必紅）", _noaff(base, p2, ["X"])[0] == "bad"))
    p3 = copy.deepcopy(post); p3["pools"][0]["容納內接矩形"] = False
    res.append(("noaff 配餘地改為容不下內接矩形（必紅）", _noaff(base, p3, ["X"])[0] == "bad"))
    b6 = copy.deepcopy(base); b6["pools"][0]["容納內接矩形"] = False
    res.append(("noaff 改前已容不下、改後同（必綠·相對判）", _noaff(b6, p3, ["X"])[0] == "ok"))
    p4 = copy.deepcopy(post); p4["err"] = "閘破"
    res.append(("noaff 改後中止 ⇒ 無從判定（⛔ 判為合）", _noaff(base, p4, ["X"])[0] == "undecidable"))
    for n, ok in res:
        print(f"  {'✅' if ok else '🔴'} {n}")
    bad = sum(1 for _, ok in res if not ok)
    print(f"selftest {len(res) - bad}/{len(res)} ⇒ {'✅' if not bad else '🔴 量測器紅'}")
    return 0 if not bad else 1


def _usage():
    print(__doc__)
    return 2


def main(argv):
    if len(argv) < 2:
        return _usage()
    c = argv[1]
    try:
        if c == "run" and len(argv) == 6:
            return cmd_run(argv[2], float(argv[3]), argv[4], argv[5])
        if c == "oracle" and len(argv) == 5:
            return cmd_oracle(argv[2], float(argv[3]), argv[4])
        if c == "cmp" and len(argv) == 4:
            return cmd_cmp(argv[2], argv[3])
        if c == "noaff" and len(argv) == 5:
            return cmd_noaff(argv[2], argv[3], argv[4])
        if c == "table" and len(argv) == 4:
            return cmd_table(argv[2], argv[3])
        if c == "selftest" and len(argv) == 2:
            return cmd_selftest()
    except (KeyError, IndexError, FileNotFoundError, json.JSONDecodeError) as e:
        print(f"🔴 受詞缺：{type(e).__name__}: {e}")
        return 3
    return _usage()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
