# -*- coding: utf-8 -*-
"""W-G.9-385 量測器（發單側窗八十七擬·檔 F30·⛔ 由受單側改一字）：`K-9-74`／`K-9-79`（臨街地特別負擔之路寬）
與 `K-9-62` 之「第33條排除」「抵充地」二欄。

子命令（一律 python verify/probes/probe_WG9385_k974.py <子命令> …）：
  selftest <repo>
           合成之例（⛔ 讀本案資料·只 harvest `app.py`·期值皆發單側手算·各例之註）：
             K1 全寬新闢（正面 15 m ⇒ 3.75；左側 8 m ⇒ 1.0）；K2 未勾新闢·抵充地占道路 40% ⇒ 2.25；
             K3 公私共有（公有持分 1/2）之抵充地占 40% ⇒ 比例 0.8 ⇒ 3.0；K4 中心線即區界（半寬 7.5 m）
             ⇒ 未勾／勾皆 1.75、⛔ 警示；K5 另一側之小碎塊平均寬 0.4 m ⇒ 仍為區界 1.75；K6 平均寬 0.6 m
             ⇒ ⛔ 區界 3.75；K7 一面臨二段（60 m 比例 1·40 m 比例 0.6）⇒ 加權 3.15（`K-9-79` ①）；
             K8 勾新闢而無道路 BLOCK ⇒ 0 ＋ 警示之字樣（`K-9-79` ②）、未勾 ⇒ 0 ⛔ 警示；K9 垂距 × 2 ＝ 12 m
             與輸入 15 m 不符 ⇒ 警示之字樣、尺度仍以輸入計 3.75；K10 `JUNCTION` 框內⛔ 計 ⇒ 比例
             1050／1275 ⇒ 3.0882352941…；K11 道路 BLOCK 無中心線 ⇒ 錯誤之字樣；K12 二欄之讀取與檢核
             （是／空白／否／他值·公有／私有／公私共有·U_LAND 無之·同一所有權人之重複列〔持分 1/2 二列 ⇒ 1/2〕·註記之地號見於
             二地段〔他地段者未註記亦然〕）；
             K13 `JUNCTION` 圖層之讀取；K14 `calc_special_burden_total` 之呼叫端之尺度；K15 取樣之容差
             （首一取樣點距道路 BLOCK 0.005 m ⇒ 仍計）；K16 無宗地 ⇒ 區界⛔ 判 ＋ 警示。
           🔧 `W-G.9-385` 補令一（停機上呈之 #1、#2 與審查之 #6·⛔ 上列一字不刪）：K17 公有所有權人之權利範圍缺漏或分母為 0
           ⇒ 填列錯誤；K18 道路 BLOCK 內之片重疊而抵充地之面積大於其面積 ⇒ 錯誤、該段⛔ 計；K19 地籍資料來源之讀取之例外
           （壞檔、U_LAND 缺欄）⇒ 錯誤一則（「地籍資料來源讀取失敗（」起首）、⛔ 拋。
           🔧 `W-G.9-385` 補令二（補令一之停機上呈 #1 與審查 #6·⛔ 上列一字不刪）：K20 實座標之旋轉之道路 BLOCK 恰為一筆全公有之
           抵充地 ⇒ 尺度 0、⛔ 錯誤（前提：諸角之中浮點之比例 ＜ 0 者 ≥ 1）；K21 片之重疊之超出 0.005 ㎡ ⇒ 比例取 0、⛔ 錯誤，0.02 ㎡
           ⇒ 錯誤；K22 缺二表之一 ⇒ 錯誤一則。
           （新碼之突變之判別力：發單側於原型施之〔`W-G.9-385` 規格單 `§一` 項 `6`〕；以受單側之碼之字樣為錨之突變另單補寫。）
  wiring   <repo> <基準>
           AST 查接線（其式以 `ast.unparse` 比之）：W1 頂層之新名 ＝ `K974_PARAMS`、`k962_land_marks`、`k974_read_junctions`、
           `k974_burden_scales`、`k974_screen_scales`，且其內⛔ 案件字面（街廓名、地號）；W2 `main()` 恰一處呼
           `k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)`、其值賦予 `_k974`；
           W3 `main()` 含 `road_data` 之三鍵 `front_scale`／`left_side_scale`／`right_side_scale`；
           W4 `JUNCTION` 存 session 鍵 `f3_cad_junctions`（恰一賦值）；W5 抽出 `main()` 之步驟 H 之該段（自 `_k974` 之賦值之列
           至既有之 `sb = calc_special_burden_total(road_data, C_for_calc)` 之列）以假 st 實際執行（警示 ⇒ `st.warning`、
           尺度入列〔唯回傳所有之面〕、錯誤 ⇒ 逐則 `st.error` 後 `st.stop()`）；W6 `verify/` 之生產碼⛔ 呼四新函式（harness 照舊消費快照之負擔尺度）；
           W7 `main`、`calc_special_burden_total` 對基準唯增列——刪去之列唯步驟 E 之說明與步驟 H 之公式說明之三列
           （以其 sha256 比之·⛔ 載其字面）；`app.py` 之他頂層節點之相異 ⊆ 四新函式 ∪ `K974_PARAMS`。
  run      <repo>
           harness 之圖資與地籍（本案）實跑 `k974_screen_scales`：R1 各面之尺度 ＝ 快照之 `負擔尺度_輸入`
           （無其線之面⛔ 列）、警示與錯誤皆 `0`；R2 `calc_special_burden_total` 給尺度與否之列逐值同；
           R3 模擬：資料檔之複本之「重劃區地籍」增「抵充地」欄、`628-34`（公有·位 `RD1`）填「是」、臨 `RD1` 之二面改未勾新闢
           ⇒ 其尺度 ＝ 外部錨（`RD1` 之 BLOCK 面積與該宗之幾何面積之比）；R4 模擬：私有地填「是」⇒ 填列錯誤；
           R5 模擬：`JUNCTION` 框疊於 `RD1` 之一端 ⇒ 比例之母體扣除之（外部錨）；R6 二欄之結果依檔之 sha256 存 session
           （同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）。
🔧 `W-G.9-388`（⛔ 上列一字不刪）：W7 之頂層之相異之許增 `k6b_stage3_run`（`K-9-61` ①②③⑥·其行為由 F32 量之）。
🔧 `W-G.9-389`（⛔ 上列一字不刪）：W7 之頂層之相異之許增試算內之程式之停機之上拋之五新名與十一函式（其行為與接線由 F33 量之）。
🔧 `W-G.9-391`（`K-9-34`·`K-9-80` ④⑥·⛔ 上列一字不刪）：W7 之頂層之相異之許增範圍之擴大之六新名與九函式（`main` 之唯增列照舊·其行為與接線由 F35 量之）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

NEW_FUNCS = ["k962_land_marks", "k974_read_junctions", "k974_burden_scales", "k974_screen_scales"]
NEW_NAMES = ["K974_PARAMS"] + NEW_FUNCS
# 🔧 `W-G.9-389`：其後之單之新名與所改之頂層節點（試算內之程式之停機之上拋·其行為與接線由 F33 量之）
W389_APP = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
                "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
                "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
# 🔧 `W-G.9-392`：其後之單之新名與所改之頂層節點（每宗之應分配面積之試算至穩定·取得之宗之自我檢查·F36 量之）
NEW392 = ("K980_G_TOL", "K980_G_MAX_ITER", "end_block_trial_G", "k980_acq_check")
W392 = NEW392 + ("_solve_G_one", "end_block_host", "f3_screen_stepg_run", "_WF_NS_NAMES")
W392 = W392 + ("_corner_first_lot_G",)   # 🔧 `W-G.9-392` 補令一：評選之式之起算點（K-9-41 ①·F36 W8 量之）
# 🔧 `W-G.9-398`（側面道路負擔百分率之附表 25·KL `2026-10-26 09:53`·⛔ 上列一字不刪）：W7 之頂層之相異之許增其新常數與所改之函式（F41 量之）。
W398 = ("RW_TABLE_25", "rw_from_width")
# 🔧 `W-G.9-398` 補令一（KL `2026-10-27 23:29`「採戊」·`2026-10-28 10:48`·⛔ 上列一字不刪）：W7 之頂層之相異之許增其二新函式與所改之二函式；
#   `main` 之刪列另許二（`W(m)` 之格式之列、`Rw` 之說明之列·補令一 `R-7″` ①②·其行為由 F41 之 X1／X8 量之）。
W398B = ("rw_width_mm", "rw_pct_2dp", "iterate_G_S", "solve_G_binary")
W399 = ("END_BLOCK_LINE_TOL", "END_BLOCK_IDX_W_LINE", "END_BLOCK_IDX_W_AREA", "end_block_end_line", "end_block_end_segs",
        "end_block_end_geom", "k960_idx_rank", "k960_idx_key", "k960_idx_first", "end_block_pick", "end_block_apply",
        "end_block_host", "end_block_eval_rows", "end_block_merge_run", "k6b_stage3_run")   # 🔧 `W-G.9-399`（末端塊評選指數·KL `2026-10-26 22:09`／`22:42`／`22:57`·⛔ 上列一字不刪）：W7 之許（F42 量之）
REPL398 = ("733c23a3cc3a541829de2a7de17731597bb658b21f7170fb1e07637ec6a7efff",
           "b69a464b93b9bf554a9a1831dc4dbbf2645017ecfaca98f4f317f6a37cd5fd83")
TOL = 1e-9


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _piece(no, blk, x0, y0, x1, y1):
    return {"原地號": no, "所屬街廓": blk, "polygon_coords": _rect(x0, y0, x1, y1)}


def _toy(road_y1=15.0, far=True, cl_y=None, extra=(), roads=None, cls=None):
    """街廓 B1 ＝ x∈[0,100]、y∈[−40,0]；正面線 y＝0（(0,0)→(100,0)）；正面之道路 RA ＝ y∈[0,road_y1]。"""
    cl_y = road_y1 / 2 if cl_y is None else cl_y
    build = {"B1": _rect(0, -40, 100, 0)}
    rd = {"RA": _rect(0, 0, 100, road_y1)} if roads is None else roads
    cl = {"RA": [(0.0, cl_y), (100.0, cl_y)]} if cls is None else cls
    fl = {"B1": {"p1": (0.0, 0.0), "p2": (100.0, 0.0)}}
    pcs = [_piece("1", "B1", 0, -40, 100, 0)]
    if roads is None:
        pcs += [_piece("10", "RA", 0, 0, 60, road_y1), _piece("11", "RA", 60, 0, 100, road_y1)]
    if far:
        pcs.append(_piece("2", "O1", 0, road_y1, 100, road_y1 + 40))
    pcs += list(extra)
    return build, rd, cl, fl, pcs


def _call(ns, toy, share, inputs, sides=None, junctions=()):
    build, rd, cl, fl, pcs = toy
    return ns["k974_burden_scales"](build, rd, cl, fl, sides or {}, pcs, share, inputs, junctions=junctions)


def _close(a, b):
    return a is not None and b is not None and abs(float(a) - float(b)) <= TOL


def _ul(rows):
    import pandas as pd
    cols = ["段小段", "地號", "所有權統一編號", "姓名", "公私別", "權利範圍分子", "權利範圍分母"]
    return pd.DataFrame([dict(zip(cols, r)) for r in rows], columns=cols)


def _rz(rows, cols=("第33條排除", "抵充地")):
    import pandas as pd
    base = ["鄉鎮市", "地段", "地號"] + list(cols)
    return pd.DataFrame([dict(zip(base, r)) for r in rows], columns=base)


def _cases(ns):
    """回 [(名, 是否相符, 實得之述)]。期值皆手算（各例之註）。"""
    out = []
    W = "B1 正面道路勾選新闢，但未偵測到道路 BLOCK"
    # K1：正面 15 m 新闢 ⇒ 15／4 ＝ 3.75；左側 8 m 新闢（道路 x∈[−8,0]·中心線 x＝−4）⇒ 8／4 ÷ 2 ＝ 1.0
    b, rd, cl, fl, pcs = _toy()
    rd = dict(rd, RL=_rect(-8, -40, 0, 0))
    cl = dict(cl, RL=[(-4.0, -40.0), (-4.0, 0.0)])
    pcs = pcs + [_piece("12", "RL", -8, -40, 0, 0), _piece("3", "O2", -48, -40, -8, 0)]
    sides = {"B1": {"left": {"p1": (0.0, -40.0), "p2": (0.0, 0.0)}}}
    r = _call(ns, (b, rd, cl, fl, pcs), {}, {"B1": {"front": (15.0, True), "left": (8.0, True)}}, sides)
    s = r["scales"].get("B1", {})
    out.append(("K1", _close(s.get("front"), 3.75) and _close(s.get("left"), 1.0) and not r["warnings"] and not r["errors"],
                f"{s}／{r['warnings']}／{r['errors']}"))
    # K2：未勾·抵充地（宗地 11 ＝ x∈[60,100]·占 RA 之 40%·公有持分 1）⇒ 比例 0.6 ⇒ 9 m ⇒ 9／4 ＝ 2.25；
    #     同面勾新闢 ⇒ 比例 1 ⇒ 3.75
    r = _call(ns, _toy(), {"11": 1.0}, {"B1": {"front": (15.0, False)}})
    r2 = _call(ns, _toy(), {"11": 1.0}, {"B1": {"front": (15.0, True)}})
    out.append(("K2", _close(r["scales"]["B1"]["front"], 2.25) and _close(r2["scales"]["B1"]["front"], 3.75),
                f"{r['scales']}／{r2['scales']}"))
    # K3：公私共有（公有持分 1/2）⇒ 抵充地 ＝ 600 × 0.5 ＝ 300 ⇒ 比例 0.8 ⇒ 12 m ⇒ 3.0
    r = _call(ns, _toy(), {"11": 0.5}, {"B1": {"front": (15.0, False)}})
    out.append(("K3", _close(r["scales"]["B1"]["front"], 3.0), f"{r['scales']}"))
    # K4：區界在中心線（RA ＝ y∈[0,7.5]·中心線 y＝7.5·另一側無地籍）⇒ 基寬 ＝ 垂距 7.5 ⇒ (7.5−4)／2 ＝ 1.75；
    #     勾新闢亦然；垂距 × 2 ＝ 15 ＝ 輸入 ⇒ ⛔ 警示
    t4 = _toy(road_y1=7.5, far=False, cl_y=7.5)
    r = _call(ns, t4, {}, {"B1": {"front": (15.0, False)}})
    r2 = _call(ns, t4, {}, {"B1": {"front": (15.0, True)}})
    out.append(("K4", _close(r["scales"]["B1"]["front"], 1.75) and _close(r2["scales"]["B1"]["front"], 1.75)
                and not r["warnings"] and not r2["warnings"], f"{r['scales']}／{r2['scales']}／{r['warnings']}"))
    # K5：另一側之碎塊 y∈[7.5,7.9]（100 × 0.4 ⇒ 平均寬 0.4 ＜ 0.5）⇒ 仍為區界 ⇒ 1.75
    r = _call(ns, _toy(road_y1=7.5, far=False, cl_y=7.5, extra=[_piece("4", "O1", 0, 7.5, 100, 7.9)]), {},
              {"B1": {"front": (15.0, True)}})
    out.append(("K5", _close(r["scales"]["B1"]["front"], 1.75), f"{r['scales']}"))
    # K6：碎塊 y∈[7.5,8.1]（平均寬 0.6 ≥ 0.5）⇒ ⛔ 區界 ⇒ 基寬 15 ⇒ 3.75
    r = _call(ns, _toy(road_y1=7.5, far=False, cl_y=7.5, extra=[_piece("4", "O1", 0, 7.5, 100, 8.1)]), {},
              {"B1": {"front": (15.0, True)}})
    out.append(("K6", _close(r["scales"]["B1"]["front"], 3.75), f"{r['scales']}"))
    # K7：一面臨二段：RW ＝ x∈[0,60]（比例 1）、RE ＝ x∈[60,160]（宗地 21 ＝ x∈[120,160] 抵充地 ⇒ 600／1500 ⇒ 比例 0.6）；
    #     未勾 15 m ⇒ RW 3.75、RE 9 m ⇒ 2.25；臨接 60／40 ⇒ 0.6 × 3.75 ＋ 0.4 × 2.25 ＝ 3.15
    roads7 = {"RW": _rect(0, 0, 60, 15), "RE": _rect(60, 0, 160, 15)}
    cls7 = {"RW": [(0.0, 7.5), (60.0, 7.5)], "RE": [(60.0, 7.5), (160.0, 7.5)]}
    t7 = _toy(roads=roads7, cls=cls7, extra=[_piece("20", "RW", 0, 0, 60, 15), _piece("22", "RE", 60, 0, 120, 15),
                                             _piece("21", "RE", 120, 0, 160, 15), _piece("5", "O3", 100, 15, 160, 55)])
    r = _call(ns, t7, {"21": 1.0}, {"B1": {"front": (15.0, False)}})
    rows7 = sorted((d["道路"], d["臨接比"]) for d in r["detail"])
    out.append(("K7", _close(r["scales"]["B1"]["front"], 0.6 * 3.75 + 0.4 * 2.25) and rows7 == [("RE", 0.4), ("RW", 0.6)],
                f"{r['scales']}／{rows7}"))
    # K8：無道路 BLOCK：勾新闢 ⇒ 0 ＋ 警示（字樣逐字）；未勾 ⇒ 0、⛔ 警示
    t8 = _toy(roads={}, cls={})
    r = _call(ns, t8, {}, {"B1": {"front": (12.0, True)}})
    r2 = _call(ns, t8, {}, {"B1": {"front": (12.0, False)}})
    out.append(("K8", r["scales"]["B1"]["front"] == 0.0 and r["warnings"] == [W] and not r["errors"]
                and r2["scales"]["B1"]["front"] == 0.0 and r2["warnings"] == [],
                f"{r['scales']}／{r['warnings']}／{r2['warnings']}"))
    # K9：道路寬 12（中心線 y＝6）而輸入 15 ⇒ 警示（字樣逐字）；尺度以輸入 15 ⇒ 3.75
    r = _call(ns, _toy(road_y1=12.0), {}, {"B1": {"front": (15.0, True)}})
    w9 = "B1 正面：中心線垂距 × 2 ＝ 12.00 m，與輸入路寬 15.00 m 相差逾 0.5 m，請確認"
    out.append(("K9", _close(r["scales"]["B1"]["front"], 3.75) and r["warnings"] == [w9] and not r["errors"],
                f"{r['scales']}／{r['warnings']}"))
    # K10：JUNCTION 框 x∈[85,100]（225 ㎡）⛔ 計；抵充地 ＝ 宗地 13 ＝ x∈[70,100]（450 ㎡·其 225 在框內）
    #      ⇒ 母體 1275、抵充地 225 ⇒ 比例 1050／1275 ⇒ 15 × 0.82352941… ＝ 12.3529… ⇒ ÷4 ＝ 3.0882352941…
    t10 = _toy(roads={"RA": _rect(0, 0, 100, 15)}, cls={"RA": [(0.0, 7.5), (100.0, 7.5)]},
               extra=[_piece("10", "RA", 0, 0, 70, 15), _piece("13", "RA", 70, 0, 100, 15)])
    r = _call(ns, t10, {"13": 1.0}, {"B1": {"front": (15.0, False)}}, junctions=[_rect(85, 0, 100, 15)])
    r0 = _call(ns, t10, {"13": 1.0}, {"B1": {"front": (15.0, False)}})
    out.append(("K10", _close(r["scales"]["B1"]["front"], 15 * (1050 / 1275) / 4)
                and _close(r0["scales"]["B1"]["front"], 15 * 0.7 / 4), f"{r['scales']}／{r0['scales']}"))
    # K11：道路 BLOCK 無中心線 ⇒ 錯誤（字樣逐字）
    r = _call(ns, _toy(cls={}), {}, {"B1": {"front": (15.0, True)}})
    out.append(("K11", r["errors"] == ["道路 BLOCK RA 未繪 CENTERLINE（B1 正面臨之），請補畫"], f"{r['errors']}"))
    # K12：二欄之讀取與檢核
    ul = _ul([("0001甲段", 1000001, "A1", "某縣", "公", 1, 1),
              ("0001甲段", 1000002, "P1", "王某", "私", 1, 1),
              ("0001甲段", 1000003, "A1", "某縣", "公", 1, 2), ("0001甲段", 1000003, "P2", "李某", "私", 1, 2),
              ("0001甲段", 1000004, "A1", "某縣", "公", 1, 2), ("0001甲段", 1000004, "A1", "某縣", "公", 1, 2),
              ("0002乙段", 1000001, "A2", "某鄉", "公", 1, 1)])
    mk = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1", None, "是"), ("某市", "甲段", "100-3", "", "是"),
                                    ("某市", "甲段", "100-4", "否", " 是 ")]), ul)
    ok_a = mk["抵充地"] == {"100-1": 1.0, "100-3": 0.5, "100-4": 0.5} and mk["第33條排除"] == {} and mk["errors"] == []
    mk2 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-2", "是", "是"), ("某市", "甲段", "100-1", "Y", ""),
                                     ("某市", "甲段", "100-9", "", "是")]), ul)
    e2 = ["填列錯誤：甲段 100-2「第33條排除」欄填「是」，但該地號非公有地（U_LAND 公私別）",
          "填列錯誤：甲段 100-2「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）",
          "填列錯誤：甲段 100-1「第33條排除」欄填「Y」，僅得填「是」或空白",
          "填列錯誤：甲段 100-9「抵充地」欄填「是」，但 U_LAND 無對應資料"]
    mk3 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1", "", "是"), ("某市", "乙段", "100-1", "", "")]), ul)
    e3 = ["填列錯誤：地號 100-1 於 甲段、乙段 皆有，「抵充地」無從對應宗地"]
    mk4 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1")], cols=()), ul)
    out.append(("K12", ok_a and mk2["errors"] == e2 and mk2["抵充地"] == {} and mk3["errors"] == e3 and mk3["抵充地"] == {}
                and mk4 == {"抵充地": {}, "第33條排除": {}, "errors": []},
                f"{mk}／{mk2['errors']}／{mk3['errors']}／{mk4}"))
    # K13：JUNCTION 圖層（四點之多節線一；二點者、他圖層者⛔ 取）
    import ezdxf
    doc = ezdxf.new()
    msp = doc.modelspace()
    msp.add_lwpolyline(_rect(0, 0, 10, 10), close=True, dxfattribs={"layer": "JUNCTION"})
    msp.add_lwpolyline([(0, 0), (5, 5)], dxfattribs={"layer": "junction"})
    msp.add_lwpolyline(_rect(20, 0, 30, 10), close=True, dxfattribs={"layer": "BLOCK"})
    jr = ns["k974_read_junctions"](doc)
    out.append(("K13", jr == [[(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]], f"{jr}"))
    # K14：calc_special_burden_total：給 front_scale 者用之（⛔ 依新闢）；未給者照舊
    row = {"label": "B1", "front_width": 15.0, "front_length": 100.0, "front_new": False,
           "left_side_width": 8.0, "left_side_length": 40.0, "left_side_new": True}
    a = ns["calc_special_burden_total"]([dict(row, front_scale=2.25)], 0.0)["rows"][0]
    b0 = ns["calc_special_burden_total"]([row], 0.0)["rows"][0]
    c = ns["calc_special_burden_total"]([dict(row, left_side_scale=0.0)], 0.0)["rows"][0]
    out.append(("K14", a["正街尺度"] == 2.25 and a["左側尺度"] == 1.0 and b0["正街尺度"] == 0.0 and b0["左側尺度"] == 1.0
                and c["左側尺度"] == 0.0, f"{a['正街尺度']}／{b0['正街尺度']}／{c['左側尺度']}"))
    # K15：取樣點之容差：道路 BLOCK 之一端退縮 0.13 m（x∈[0.13,100]）⇒ 首一取樣點（x＝0.125）距之 0.005 ⇒ 仍計 ⇒ 3.75
    t15 = _toy(roads={"RA": _rect(0.13, 0, 100, 15)}, cls={"RA": [(0.0, 7.5), (100.0, 7.5)]},
               extra=[_piece("10", "RA", 0.13, 0, 100, 15)])
    r = _call(ns, t15, {}, {"B1": {"front": (15.0, True)}})
    out.append(("K15", r["scales"]["B1"]["front"] == 3.75, f"{r['scales']}"))
    # K16：無宗地（pieces 空）⇒ 中心線之區界⛔ 判 ⇒ 基寬 ＝ 輸入 15 ⇒ 3.75 ＋ 警示一則（字樣逐字）
    b16, rd16, cl16, fl16, _ = _toy()
    r = ns["k974_burden_scales"](b16, rd16, cl16, fl16, {}, [], {}, {"B1": {"front": (15.0, True)}})
    out.append(("K16", r["scales"]["B1"]["front"] == 3.75
                and r["warnings"] == ["尚無宗地資料（地籍），中心線是否為重劃區界⛔ 判（以輸入之路寬計）"],
                f"{r['scales']}／{r['warnings']}"))
    out += _cases385(ns)
    return out


def _cases385(ns):
    """🆕 `W-G.9-385` 補令一：K17〜K19；補令二：K20〜K22（各例之例外 ⇒ 該例紅·⛔ 中止他例）。"""
    out = []
    for nm, f in (("K17", _k17), ("K18", _k18), ("K19", _k19), ("K20", _k20), ("K21", _k21), ("K22", _k22)):
        try:
            out.append(f(ns))
        except Exception as e:
            out.append((nm, False, f"例外 {type(e).__name__}: {e}"))
    return out


def _k17(ns):
    # 🔧 `W-G.9-385` 補令一（停機上呈之 #1）：公有所有權人之權利範圍缺漏（分子空白）或分母為 0 ⇒ 填列錯誤（字樣逐字）、⛔ 入註記
    ul17 = _ul([("0001甲段", 1000001, "A1", "某縣", "公", None, 1),
                ("0001甲段", 1000002, "A1", "某縣", "公", 1, 0),
                ("0001甲段", 1000003, "A1", "某縣", "公", 1, 2), ("0001甲段", 1000003, "P1", "王某", "私", None, None)])
    mk17 = ns["k962_land_marks"](_rz([("某市", "甲段", "100-1", "", "是"), ("某市", "甲段", "100-2", "", "是"),
                                      ("某市", "甲段", "100-3", "", "是")]), ul17)
    e17 = ["填列錯誤：甲段 100-1「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數",
           "填列錯誤：甲段 100-2「抵充地」欄填「是」，但其公有所有權人之權利範圍（U_LAND 分子／分母）缺漏或分母非正數"]
    return (("K17", mk17["errors"] == e17 and mk17["抵充地"] == {"100-3": 0.5}, f"{mk17}"))


def _k18(ns):
    # 🔧 補令一（審查之 #6）：道路 BLOCK 內之宗地之片重疊而抵充地之面積大於其面積 ⇒ 錯誤（字樣逐字）、該段⛔ 計
    t18 = _toy(roads={"RA": _rect(0, 0, 100, 15)}, cls={"RA": [(0.0, 7.5), (100.0, 7.5)]},
               extra=[_piece("10", "RA", 0, 0, 100, 15), _piece("11", "RA", 0, 0, 100, 15)])
    r = _call(ns, t18, {"10": 1.0, "11": 1.0}, {"B1": {"front": (15.0, False)}})
    return (("K18", r["errors"] == ["道路 BLOCK RA 內抵充地之面積大於扣除路口後之面積（宗地之片重疊），請檢查地籍（B1 正面臨之）"]
                and r["scales"]["B1"]["front"] == 0.0, f"{r['scales']}／{r['errors']}"))


def _k19(ns):
    # 🔧 補令一（停機上呈之 #2）：地籍資料來源之讀取之例外（非 xlsx 之 bytes；U_LAND 缺「段小段」之欄）⇒ 錯誤一則（字首逐字）、⛔ 拋
    import pandas as pd
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine="openpyxl") as w:
        _ul([("0001甲段", 1000001, "A1", "某縣", "公", 1, 1)]).drop(columns=["段小段"]).to_excel(w, sheet_name="U_LAND", index=False)
        _rz([("某市", "甲段", "100-1", "", "是")]).to_excel(w, sheet_name="重劃區地籍", index=False)
    got19 = []
    for nm19, bb in (("壞檔", b"not an xlsx"), ("缺欄", bio.getvalue())):
        ss19 = {"f7_saved": ("x.xlsx", bb)}
        try:
            r19 = ns["k974_screen_scales"](ss19, [], [], "ROADK")
            e19 = r19["errors"]
            got19.append((nm19, len(e19) == 1 and e19[0].startswith("地籍資料來源讀取失敗（"), e19[:1]))
        except Exception as e:
            got19.append((nm19, False, f"拋 {type(e).__name__}"))
    return (("K19", all(x[1] for x in got19), f"{got19}"))


def _k20(ns):
    # 🔧 `W-G.9-385` 補令二（補令一之停機上呈 #1）：實座標（TWD97 之量級）之旋轉之道路 BLOCK 恰為一筆全公有之抵充地之片
    #   （片 ＝ 道路之多邊形·持分 1·未勾）⇒ 真比例 0 ⇒ 尺度 0、⛔ 錯誤（浮點之誤差 ≤ overlap_tol_m2 ⇒ 比例取 0）；
    #   前提（判別力）：諸角之中至少一角之 (A − B) ÷ A 之浮點值 ＜ 0（以 shapely 另算）
    import math
    from shapely.geometry import Polygon
    neg, bad = 0, []
    for k in range(60):
        th = math.radians(k * 7.3 + 0.37)
        c, s_ = math.cos(th), math.sin(th)
        X0, Y0 = 310123.457, 2652345.679

        def T(pts):
            return [(X0 + x * c - y * s_, Y0 + x * s_ + y * c) for x, y in pts]
        road = T(_rect(0, 0, 100, 15))
        A = Polygon(road).area
        if (A - Polygon(road).intersection(Polygon(road)).area) / A < 0:
            neg += 1
        build = {"B1": T(_rect(0, -40, 100, 0))}
        fl = {"B1": {"p1": T([(0.0, 0.0)])[0], "p2": T([(100.0, 0.0)])[0]}}
        pcs = [{"原地號": "1", "所屬街廓": "B1", "polygon_coords": T(_rect(0, -40, 100, 0))},
               {"原地號": "10", "所屬街廓": "RA", "polygon_coords": road},
               {"原地號": "2", "所屬街廓": "O1", "polygon_coords": T(_rect(0, 15, 100, 55))}]
        r = ns["k974_burden_scales"](build, {"RA": road}, {"RA": T([(0.0, 7.5), (100.0, 7.5)])}, fl, {}, pcs,
                                     {"10": 1.0}, {"B1": {"front": (15.0, False)}})
        if r["errors"] or r["scales"]["B1"]["front"] != 0.0:
            bad.append((k, r["scales"]["B1"]["front"], r["errors"][:1]))
    return ("K20", neg > 0 and not bad, f"前提（浮點之負）{neg}／60；不符 {bad[:3]}（{len(bad)}）")


def _k21(ns):
    # 🔧 補令二：片之重疊之超出 ＝ 0.005 ㎡（≤ 0.01）⇒ 比例取 0、⛔ 錯誤 ⇒ 尺度 0；超出 0.02 ㎡（＞ 0.01）⇒ 錯誤（字樣同 K18）
    out = []
    for w, want_err in ((0.005 / 15, False), (0.02 / 15, True)):
        t = _toy(roads={"RA": _rect(0, 0, 100, 15)}, cls={"RA": [(0.0, 7.5), (100.0, 7.5)]},
                 extra=[_piece("10", "RA", 0, 0, 50 + w / 2, 15), _piece("11", "RA", 50 - w / 2, 0, 100, 15)])
        r = _call(ns, t, {"10": 1.0, "11": 1.0}, {"B1": {"front": (15.0, False)}})
        e = ["道路 BLOCK RA 內抵充地之面積大於扣除路口後之面積（宗地之片重疊），請檢查地籍（B1 正面臨之）"]
        out.append((r["errors"] == (e if want_err else [])) and r["scales"]["B1"]["front"] == 0.0)
    return ("K21", all(out), f"{out}")


def _k22(ns):
    # 🔧 補令二（補令一之審查 #6）：地籍資料來源缺「重劃區地籍」（或「U_LAND」）之表 ⇒ 錯誤一則（字樣逐字）、⛔ 靜默
    import pandas as pd
    got = []
    for keep in ("U_LAND", "重劃區地籍"):
        bio = io.BytesIO()
        with pd.ExcelWriter(bio, engine="openpyxl") as w:
            if keep == "U_LAND":
                _ul([("0001甲段", 1000001, "A1", "某縣", "公", 1, 1)]).to_excel(w, sheet_name="U_LAND", index=False)
            else:
                _rz([("某市", "甲段", "100-1", "", "是")]).to_excel(w, sheet_name="重劃區地籍", index=False)
        r = ns["k974_screen_scales"]({"f7_saved": ("x.xlsx", bio.getvalue())}, [], [], "ROADK")
        got.append(r["errors"] == ["地籍資料來源缺「U_LAND」或「重劃區地籍」工作表"])
    return ("K22", all(got), f"{got}")


def selftest(repo):
    ns, _ = _harvest(repo)
    miss = [n for n in NEW_NAMES if n not in ns]
    if miss:
        print(f"  ❌ 新名缺 {miss}")
        print(f"⇒ 紅 ['K0']；rc 1")
        return 1
    red = []
    for nm, ok, got in _cases(ns):
        print(f"  {'✅' if ok else '❌'} {nm}：{got}")
        if not ok:
            red.append(nm)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


CASE_LIT = ("R1", "R2", "R3", "R4", "R5", "R6", "RD1", "RD2", "RD3", "RD4", "628-", "G1", "UC9898", "德安")


def _mainfn(tree):
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            return node
    return None


def _step_h_snippet(src):
    a = src.index("        _k974 = k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)\n")
    end_s = "        sb = calc_special_burden_total(road_data, C_for_calc)\n"
    b = src.index(end_s, a) + len(end_s)
    return src[a:b]


class _Stop(Exception):
    pass


class _FakeSt:
    def __init__(self, ss):
        self.session_state = ss
        self.msgs = []

    def warning(self, m):
        self.msgs.append(("warning", m))

    def error(self, m):
        self.msgs.append(("error", m))

    def stop(self):
        raise _Stop()


def _run_snippet(snip, scales, warnings, errors):
    import textwrap
    st = _FakeSt({"ROADK": {"b1": {"front_width": 15.0, "front_new": False}}})
    called = []

    def _k(ss, bb, tp, key):
        called.append((ss is st.session_state, [b["label"] for b in bb], tp, key))
        return {"scales": scales, "detail": [], "warnings": list(warnings), "errors": list(errors)}

    g = {"st": st, "k974_screen_scales": _k, "build_blocks": [{"id": "b1", "label": "B1"}], "temp_parcels": ["TP"],
         "SS_ROAD": "ROADK", "C_for_calc": 0.0,
         "calc_special_burden_total": lambda rd, c: {"rows": rd}}
    stopped = False
    try:
        exec(compile(textwrap.dedent(snip), "<snip>", "exec"), g)
    except _Stop:
        stopped = True
    return called, st.msgs, stopped, g.get("road_data"), g.get("sb")


def wiring(repo, base):
    src = _read(repo, "app.py")
    tree = ast.parse(src)
    res = []
    top = {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
    assigns = {t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    lits = []
    for nm in NEW_FUNCS:
        if nm in top:
            for x in ast.walk(top[nm]):
                if isinstance(x, ast.Constant) and isinstance(x.value, str) and any(c in x.value for c in CASE_LIT):
                    lits.append((nm, x.value[:40]))
    ok1 = all(n in top for n in NEW_FUNCS) and "K974_PARAMS" in assigns and not lits
    res.append(("W1 頂層之新名與⛔ 案件字面", ok1, f"{[n in top for n in NEW_FUNCS]}／K974_PARAMS {'K974_PARAMS' in assigns}／字面 {lits}"))
    mn = _mainfn(tree)
    calls = [x for x in ast.walk(mn) if isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
             and x.func.id == "k974_screen_scales"] if mn else []
    want = "k974_screen_scales(st.session_state, build_blocks, temp_parcels, SS_ROAD)"
    ok2 = len(calls) == 1 and ast.unparse(calls[0]) == want
    seg = ast.get_source_segment(src, mn) if mn else ""
    asg = [x for x in ast.walk(mn) if isinstance(x, ast.Assign) and isinstance(x.value, ast.Call)
           and isinstance(x.value.func, ast.Name) and x.value.func.id == "k974_screen_scales"] if mn else []
    ok2 = ok2 and len(asg) == 1 and ast.unparse(asg[0].targets[0]) == "_k974"
    res.append(("W2 main() 恰一處呼之", ok2, f"{[ast.unparse(c) for c in calls]}"))
    kst = {x.value for x in ast.walk(mn) if isinstance(x, ast.Constant) and isinstance(x.value, str)} if mn else set()
    ok3 = {"front_scale", "left_side_scale", "right_side_scale"} <= kst
    res.append(("W3 main() 之 road_data 之尺度之鍵（front_scale／left_side_scale／right_side_scale）", ok3, ""))
    ok4 = sum(1 for x in ast.walk(mn) if isinstance(x, ast.Assign) and ast.unparse(x) ==
              "st.session_state['f3_cad_junctions'] = k974_read_junctions(_doc_cad_p7)") == 1 if mn else False
    res.append(("W4 JUNCTION 存 session", ok4, ""))
    try:
        snip = _step_h_snippet(src)
        c1, m1, s1, rd1, _ = _run_snippet(snip, {"B1": {"front": 2.25, "left": 0.5}}, ["警示甲"], [])
        c2, m2, s2, rd2, sb2 = _run_snippet(snip, {}, [], ["錯甲", "錯乙"])
        ok5 = (c1 == [(True, ["B1"], ["TP"], "ROADK")] and m1 == [("warning", "⚠️ 警示甲")] and not s1
               and rd1 and rd1[0].get("front_scale") == 2.25 and rd1[0].get("left_side_scale") == 0.5
               and "right_side_scale" not in rd1[0] and rd1[0]["front_width"] == 15.0
               and s2 and m2 == [("error", "⛔ 錯甲"), ("error", "⛔ 錯乙")] and rd2 is None and sb2 is None)
        res.append(("W5 步驟 H 之段以假 st 實跑", ok5, f"{rd1}／{m1}／{m2}／停 {s1}/{s2}"))
    except Exception as e:
        res.append(("W5 步驟 H 之段以假 st 實跑", False, f"{type(e).__name__}: {e}"))
    others = []
    vdir = os.path.join(repo, "verify")
    for fn in sorted(os.listdir(vdir)):
        if fn.endswith(".py"):
            t = _read(repo, os.path.join("verify", fn))
            if any(n in t for n in NEW_NAMES):
                others.append(fn)
    res.append(("W6 verify/ 之生產碼⛔ 呼之", others == [], f"{others}"))
    try:
        import subprocess
        bsrc = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True, check=True).stdout.decode("utf-8")
        btree = ast.parse(bsrc)
        btop = {}
        for n in btree.body:
            k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
                n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) else None)
            if k:
                btop[k] = ast.get_source_segment(bsrc, n)
        ctop = {}
        for n in tree.body:
            k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
                n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) else None)
            if k:
                ctop[k] = ast.get_source_segment(src, n)
        dif = sorted(k for k in set(btop) | set(ctop) if btop.get(k) != ctop.get(k))
        import difflib, hashlib
        dels = []
        for k in ("main", "calc_special_burden_total"):
            for ln in difflib.ndiff((btop.get(k) or "").split("\n"), (ctop.get(k) or "").split("\n")):
                if ln.startswith("- "):
                    dels.append((k, hashlib.sha256(ln[2:].encode("utf-8")).hexdigest()))
        # 🔧 `W-G.9-387`：其後之單所改之頂層節點亦許（`adj_intake`·`K-9-61` ⑧·其行為由 F31 量之）
        # 🔧 `W-G.9-388`：同（`k6b_stage3_run`·`K-9-61` ①②③⑥·其行為由 F32 量之）
        # 🔧 `W-G.9-389`：同（試算內之程式之停機之上拋·F33 量之）
        # 🔧 `W-G.9-391`：同（範圍依最小建築面積之擴大·F35 量之）
        # 🔧 `W-G.9-392`：同（試算至穩定與取得之宗之自我檢查·F36 量之）
        ok7 = (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
               | set(W389_APP) | set(W391) | set(W392)
               and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))
        ok7 = ok7 or (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
               | set(W389_APP) | set(W391) | set(W392) | set(W398)
               and sorted(h for _, h in dels) == sorted(REPL385) and all(k == "main" for k, _ in dels))   # 🔧 `W-G.9-398`：同（F41 量之）
        ok7 = ok7 or (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
               | set(W389_APP) | set(W391) | set(W392) | set(W398) | set(W398B)
               and sorted(h for _, h in dels) == sorted(REPL385 + REPL398) and all(k == "main" for k, _ in dels))   # 🔧 `W-G.9-398` 補令一：同（F41 量之）
        ok7 = ok7 or (set(dif) <= set(NEW_NAMES) | {"main", "calc_special_burden_total"} | {"adj_intake"} | {"k6b_stage3_run"}
               | set(W389_APP) | set(W391) | set(W392) | set(W398) | set(W398B) | set(W399)
               and sorted(h for _, h in dels) == sorted(REPL385 + REPL398) and all(k == "main" for k, _ in dels))   # 🔧 `W-G.9-399`：同（F42 量之）
        res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", ok7, f"相異 {dif}／刪列 {len(dels)}"))
    except Exception as e:
        res.append(("W7 main／calc 唯增列（具名之換列三）·頂層之相異", False, f"{type(e).__name__}: {e}"))
    red = []
    for nm, ok, got in res:
        print(f"  {'✅' if ok else '❌'} {nm}：{got}")
        if not ok:
            red.append(nm.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# 基準之 `main` 之三列（步驟 E 之說明「……不計道路截角。僅新闢……」與步驟 H 之公式說明之正面、側面之二列）之 sha256
REPL385 = ("0bc0330faf15a1f5543f5c9b9147da2ec7b73d04d15dbf03c0857ae07605345e",
           "7dbfbc005f4c147f0de70d370597bf7de038fc5bf22adb8dd145bdf3cef87db5",
           "217d50a6c215b275aa66e89ea33b87d0ad51bde2e3e7a4d75bf8202b5051e13e")


def _case(repo):
    os.environ["WV_K6_STEP0"] = os.environ.get("WV_K6_STEP0", "") or "off"
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    import run_verification as rv
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fake_st, snap)
        v6 = open(rv.V6DXF, "rb").read()
        tp, _, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snap)
    return ns, snap, cb_by, cad, tp, rv.ANON_XLSX


def _ss(cb_by, cad, snap, xbytes, junctions=(), unchecked=()):
    road = {}
    blds = []
    for lb, b in cb_by.items():
        if b.get("burden_type") != "可建築土地":
            continue
        blds.append(b)
        bs = snap["blocks"][lb]

        def _w(k):
            v = bs[k]["路寬_m"]
            return float(v) if isinstance(v, (int, float)) else 0.0
        road[b["id"]] = {"front_width": _w("正面"), "front_new": float(bs["正面"]["負擔尺度_輸入"]) > 0 and (lb, "front") not in unchecked,
                         "left_side_width": _w("左側"), "left_side_new": float(bs["左側"]["負擔尺度_輸入"]) > 0 and (lb, "left") not in unchecked,
                         "right_side_width": _w("右側"), "right_side_new": float(bs["右側"]["負擔尺度_輸入"]) > 0 and (lb, "right") not in unchecked}
    ss = {"f3_classified_blocks": list(cb_by.values()), "f3_manual_road_centerlines": cad["centerlines"],
          "f3_cad_front_lines": cad["front_lines"], "f3_cad_side_lines_by_side": cad["side_lines_by_side"],
          "f3_cad_junctions": list(junctions), "f7_saved": ("x.xlsx", xbytes), "ROADK": road}
    return ss, blds


def _xlsx_with(path, marks):
    """資料檔之複本（記憶體）：「重劃區地籍」增「第33條排除」「抵充地」二欄，依 marks ＝ {(欄, 地號): 值} 填之。"""
    import pandas as pd
    xl = pd.ExcelFile(path, engine="openpyxl")
    ul = pd.read_excel(xl, "U_LAND", header=0, engine="openpyxl")
    rz = pd.read_excel(xl, "重劃區地籍", header=0, engine="openpyxl")
    for col in ("第33條排除", "抵充地"):
        rz[col] = [marks.get((col, str(n).strip()), None) for n in rz["地號"]]
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine="openpyxl") as w:
        ul.to_excel(w, sheet_name="U_LAND", index=False)
        rz.to_excel(w, sheet_name="重劃區地籍", index=False)
    return bio.getvalue()


def run(repo):
    ns, snap, cb_by, cad, tp, xpath = _case(repo)
    miss = [n for n in NEW_NAMES if n not in ns]
    if miss:
        print(f"  ❌ 新名缺 {miss}")
        print("⇒ 紅 ['R0']；rc 1")
        return 1
    xb = open(xpath, "rb").read()
    res = []
    ss, blds = _ss(cb_by, cad, snap, xb)
    r = ns["k974_screen_scales"](ss, blds, tp, "ROADK")
    bad = []
    for b in blds:
        lb = b["label"]
        for sd, k in (("front", "正面"), ("left", "左側"), ("right", "右側")):
            exp = float(snap["blocks"][lb][k]["負擔尺度_輸入"])
            got = r["scales"].get(lb, {}).get(sd)
            has_line = (sd == "front" and lb in cad["front_lines"]) or (sd != "front" and sd in (cad["side_lines_by_side"].get(lb) or {}))
            if (got is None) == has_line or (got is not None and got != exp):
                bad.append((lb, sd, exp, got))
    print("  各面之尺度：" + "；".join(f"{b['label']} " + "／".join(f"{sd} {r['scales'].get(b['label'], {}).get(sd)}"
                                                                    for sd in ("front", "left", "right")) for b in blds))
    res.append(("R1 尺度 ＝ 快照之負擔尺度_輸入", not bad and not r["warnings"] and not r["errors"],
                f"不符 {bad}／警示 {r['warnings']}／錯誤 {r['errors']}"))
    rd = []
    for b in blds:
        x = ss["ROADK"][b["id"]]
        rd.append({"label": b["label"], "front_width": x["front_width"], "front_length": cad["front_lengths"].get(b["label"], 0.0),
                   "front_new": x["front_new"], "left_side_width": x["left_side_width"], "left_side_length": 10.0,
                   "left_side_new": x["left_side_new"], "right_side_width": x["right_side_width"], "right_side_length": 10.0,
                   "right_side_new": x["right_side_new"]})
    rd2 = []
    for row in rd:
        s = r["scales"].get(row["label"], {})
        row2 = dict(row)
        for sd, ky in (("front", "front_scale"), ("left", "left_side_scale"), ("right", "right_side_scale")):
            if sd in s:
                row2[ky] = s[sd]
        rd2.append(row2)
    a = ns["calc_special_burden_total"](rd, 0.1)
    b2 = ns["calc_special_burden_total"](rd2, 0.1)
    res.append(("R2 calc 之列給尺度與否逐值同", a == b2, f"{a['special_total']}／{b2['special_total']}"))
    # R3：628-34（公有·RD1 內）填「是」；臨 RD1 之二面（R1 左側、R2 正面）改未勾新闢
    #     外部錨：RD1 之 BLOCK 面積（area_m2）、628-34 於 RD1 之片之幾何面積（幾何面積_m2）⇒ 比例 ⇒ 8 × 比例 ⇒ 尺度表
    rd1 = float(cb_by["RD1"]["area_m2"])
    a34 = sum(float(t["幾何面積_m2"]) for t in tp if t["所屬街廓"] == "RD1" and str(t["原地號"]) == "628-34")
    ratio = (rd1 - a34) / rd1
    bw = 8.0 * ratio
    fsc = ns["calc_frontage_burden_scale"](bw)
    ss3, _ = _ss(cb_by, cad, snap, _xlsx_with(xpath, {("抵充地", "628-34"): "是"}),
                 unchecked={("R1", "left"), ("R2", "front")})
    r3 = ns["k974_screen_scales"](ss3, blds, tp, "ROADK")
    g1, g2 = r3["scales"]["R1"]["left"], r3["scales"]["R2"]["front"]
    others_same = all(r3["scales"][lb][sd] == r["scales"][lb][sd] for lb in r["scales"] for sd in r["scales"][lb]
                      if (lb, sd) not in (("R1", "left"), ("R2", "front")))
    # 容差 1e-4：外部錨之「幾何面積_m2」捨入至 0.01 ㎡（⇒ 比例之差 ≤ 0.005／RD1 ≈ 5e-6 ⇒ 尺度之差 ≤ 2e-5）
    ok3 = (abs(g2 - fsc) <= 1e-4 and abs(g1 - fsc / 2) <= 1e-4 and 0 < a34 < rd1 and others_same
           and not r3["errors"] and not r3["warnings"])
    res.append(("R3 抵充地之模擬（628-34·RD1）", ok3,
                f"RD1 {rd1:.4f}／628-34 之片 {a34:.4f}／比例 {ratio:.6f}／負擔路寬 {bw:.4f}／期 {fsc:.6f}、{fsc / 2:.6f}"
                f"／得 {g2:.6f}、{g1:.6f}"))
    # R4：私有地填「是」⇒ 填列錯誤（628-37 ＝ 私有·RD1 內）；第33條排除填於公有地（628-34）⇒ 無錯
    ss4, _ = _ss(cb_by, cad, snap, _xlsx_with(xpath, {("抵充地", "628-37"): "是", ("第33條排除", "628-34"): "是"}))
    r4 = ns["k974_screen_scales"](ss4, blds, tp, "ROADK")
    e4 = ["填列錯誤：德安段 628-37「抵充地」欄填「是」，但該地號非公有地（U_LAND 公私別）"]
    res.append(("R4 私有地填「是」⇒ 填列錯誤", r4["errors"] == e4, f"{r4['errors']}"))
    # R6：二欄之結果依檔之 sha256 存 session（同檔再呼 ⇒ 用之；換檔 ⇒ 重讀）
    import hashlib
    h4 = hashlib.sha256(ss4["f7_saved"][1]).hexdigest()
    r6a = ns["k974_screen_scales"](ss4, blds, tp, "ROADK")
    c6 = ss4.get("f3_k962_marks_cache")
    ss4["f7_saved"] = ("x.xlsx", xb)
    r6b = ns["k974_screen_scales"](ss4, blds, tp, "ROADK")
    ok6 = (r6a["errors"] == e4 and isinstance(c6, tuple) and c6[0] == h4 and r6b["errors"] == []
           and ss4["f3_k962_marks_cache"][0] == hashlib.sha256(xb).hexdigest())
    res.append(("R6 二欄之結果之存與換檔", ok6, f"{r6a['errors']}／{r6b['errors']}"))
    # R5：JUNCTION 框 ＝ RD1 之頂點之外接矩形與 RD1 之一端 10 m 之交（外部錨：框內之 RD1 面積以 shapely 另算）
    from shapely.geometry import Polygon, box
    p = Polygon(cb_by["RD1"]["vertices"])
    x0, y0, x1, y1 = p.bounds
    jb = box(x0, y0, x0 + 10.0, y1)
    jpoly = [tuple(c) for c in list(jb.exterior.coords)[:-1]]
    inj = float(p.intersection(jb).area)
    a34j = sum(float(Polygon(t["polygon_coords"]).intersection(p.difference(jb)).area) for t in tp
               if t["所屬街廓"] == "RD1" and str(t["原地號"]) == "628-34")
    ratio5 = ((float(p.area) - inj) - a34j) / (float(p.area) - inj)
    ss5, _ = _ss(cb_by, cad, snap, _xlsx_with(xpath, {("抵充地", "628-34"): "是"}), junctions=[jpoly],
                 unchecked={("R1", "left"), ("R2", "front")})
    r5 = ns["k974_screen_scales"](ss5, blds, tp, "ROADK")
    f5 = ns["calc_frontage_burden_scale"](8.0 * ratio5)
    ok5 = abs(r5["scales"]["R2"]["front"] - f5) <= 1e-6 and inj > 0 and not r5["errors"]
    res.append(("R5 JUNCTION 之模擬（RD1 之一端）", ok5, f"框內 {inj:.4f}／比例 {ratio5:.6f}／期 {f5:.6f}／得 {r5['scales']['R2']['front']:.6f}"))
    red = []
    for nm, ok, got in res:
        print(f"  {'✅' if ok else '❌'} {nm}：{got}")
        if not ok:
            red.append(nm.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if not ((len(argv) == 3 and argv[1] in ("selftest", "run")) or (len(argv) == 4 and argv[1] == "wiring")):
        print(__doc__)
        return 2
    try:
        if argv[1] == "wiring":
            return wiring(argv[2], argv[3])
        return {"selftest": selftest, "run": run}[argv[1]](argv[2])
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"⇒ 無從判定（{type(e).__name__}）；rc 3")
        return 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))
