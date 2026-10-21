# -*- coding: utf-8 -*-
"""W-G.9-387 量測器（發單端擬·檔 F31·⛔ 由受單側改一字）：`K-9-61` ⑧ 之落地——合併單位之原街廓之擇
（KL 補裁 `2026-10-17 14:55` 第 1 點·`15:23`「甲」）。

所量之性質：同一歸戶之建築街廓內不能分配之土地分處二以上之街廓者，其原街廓 ＝
  ① 各街廓之分不到之土地之應分配面積（原投影位置之 G·入池閘之合併單元只計一次）之加總較大者；
  ② ① 以 `0.01 ㎡` 為單位相同者，各街廓之分不到之土地之重劃前面積（`原有面積`·部分併出者為其剩下）之合計較大者；
  ③ 再相同者，各街廓之分不到之土地中最小之暫編地號（字典序）較小者；
  ⛔ 停機（三鍵之後必有唯一者）。

子命令（一律 python verify/probes/probe_WG9387_k961h.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·以 AST 自 `app.py` 抽出 `ADJ_*` 常數、`adj_intake`、`adj_intake_rows`、`k967_rank`、
           `adj_q2`）：K1〜K18（各例之期值皆依上開 ①〜③ 手算·見各例之註）。
  wiring   <repo> <基準 commit>
           AST 查接線：X1 `adj_intake` 呼叫 `k967_rank`（`K-9-67` 之序之單一真相源）；X2 `adj_intake` 內⛔ 有其訊息及於
           原街廓之 `raise`；X3 `app.py` 之頂層節點之名之集對基準⛔ 變、其相異之節點 ⊆ {`adj_intake`}；X4 `adj_intake` 內⛔
           案件字面；X5 生產碼 `34` 檔中 `app.py` 以外者（`verify/` 頂層之 `*.py`）對基準相異 `0`。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 盤點⛔ 停機；R2 每一建地軌之單位之原街廓 ＝ 本器另寫之三鍵之擇
           （⛔ 呼叫 `k967_rank`／`adj_q2`）；R3 每一合併單位之原街廓 ＝ 外部錨 `EXPECT_RUN`（主線 `34736ab` 之
           `probe_WG9351_intake.py run` 之出艙·發單端實跑·舊碼之值）——本案⛔ 遇並列 ⇒ 原街廓⛔ 變。
🔧 `W-G.9-388`（⛔ 上列一字不刪）：X3 之許增 `k6b_stage3_run`（`K-9-61` ①②③⑥ 之落地·其行為由 F32 量之）。
🔧 `W-G.9-389`（⛔ 上列一字不刪）：X3 之許增試算內之程式之停機之上拋之五新名（名之集唯增之）與十一函式；X5 之許增
  `verify/selection_pipeline.py`（其增列·其行為與接線由 F33 量之）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, io, os, re, subprocess, sys
from decimal import Decimal, ROUND_HALF_UP

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

FN_AI = "adj_intake"
EXTRACT_FUNCS = [FN_AI, "adj_intake_rows", "k967_rank", "adj_q2"]
# 🔧 `W-G.9-389`：其後之單之新名與所改之頂層節點（試算內之程式之停機之上拋·F33 量之）
NEW389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since")
W389 = ("K6_PROGRAM_STOPS", "K6_PROGRAM_STOP_RE", "k6_program_stop", "k6_trial_mark", "k6_trial_raise_since",
            "evaluate_parcel_width_n14", "k917_should_drop", "k929_6_fixpoint", "end_block_merge_run", "adj_intake",
            "k967_pool_out", "k967_pool_less", "k953_manual_run", "k6b_screen_callbacks", "f3_screen_k953", "f3_screen_adj4")
# 🔧 `W-G.9-391`：其後之單之新名與所改之頂層節點、harness 二檔（範圍依最小建築面積之擴大、短街廓之警示停止·F35 量之）
NEW391 = ("K980_AREA_TOL", "K980_AREA_EPS", "K980_TOUCH_TOL", "end_block_band_width", "k980_range_touch_check", "k980_mba")
W391 = NEW391 + ("_build_corner_range_v3", "_end_region_R", "_place_pool_parcels", "end_block_apply", "end_block_host",
                 "end_block_side_geom", "f3_screen_stepg_run", "main", "select_corner_lots_both_sides_v12", "_WF_NS_NAMES")
F391 = ("verify/stepg_pipeline.py", "verify/run_verification.py")
CASE_LIT_RE = re.compile(r"^(R|RD|G)\d+$|^G\d{3}$|^\d{3}(-\d+)*(\(\d+\))?$")
# 外部錨（R3）：主線 `34736ab` 之 `probe_WG9351_intake.py run <repo>` 之「單位」列之原街廓（發單端 2026-10-17 實跑）
EXPECT_RUN = {
    3.5: {"G003": None, "G004": "R2", "G011": "R3", "G012": None, "G013": None, "G014": "R3", "G015": None,
          "G016": None, "G018": "R2", "G020": "R2", "G024": None, "G025": "R5", "G028": None, "G030": "R3",
          "G031": None, "G032": "R6", "G033": "R3"},
    0.0: {"G003": None, "G004": "R2", "G011": "R3", "G012": None, "G013": None, "G014": "R3", "G015": None,
          "G016": None, "G018": "R2", "G020": "R2", "G024": None, "G025": "R5", "G028": None, "G030": "R2",
          "G031": None, "G032": "R6", "G033": "R3"},
}


def _read(repo, rel):
    with open(os.path.join(repo, rel), encoding="utf-8") as f:
        return f.read()


def _extract_ns(src):
    tree = ast.parse(src)
    parts, got = [], set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in EXTRACT_FUNCS:
            parts.append(ast.get_source_segment(src, node))
            got.add(node.name)
        elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                and (node.targets[0].id.startswith("ADJ_") or node.targets[0].id.startswith("SS_ADJ_")):
            parts.append(ast.get_source_segment(src, node))
    miss = [f for f in EXTRACT_FUNCS if f not in got]
    if miss:
        raise KeyError(f"受詞缺 {miss}")
    ns = {}
    exec(compile("\n\n".join(parts), "<k961h_extract>", "exec"), ns)
    return ns


def _t(pid, blk, a, **kw):
    d = {"暫編地號": pid, "原地號": "L" + pid, "所屬街廓": blk, "分攤登記面積_m2": a, "面積_m2": 0.0,
         "重劃前地價區段": "z"}
    d.update(kw)
    return d


BUR = {"B1": "可建築土地", "B2": "可建築土地", "B3": "可建築土地", "C1": "共同負擔"}


def _case(I, spec, merged=None, extra_temp=(), alloc=()):
    """spec ＝ [(暫編, 街廓, 原有面積, G)]（G 為 None ⇒ 該片為合併單元之他成員·⛔ 自有不配地紀錄）；皆同一歸戶 GA。
    merged ＝ {單元: [成員…]}；extra_temp ＝ 另加之切片（配地）；alloc ＝ 配地之 build 單元。回 adj_intake 之結果。"""
    temp = [_t(p, b, a) for p, b, a, _g in spec] + [dict(x) for x in extra_temp]
    own = {t["原地號"]: "GA" for t in temp}
    mem_of = {}
    for u, ms in (merged or {}).items():
        for m in ms:
            mem_of[m] = u
    build, drops = [], {}
    for p, b, a, g in spec:
        if mem_of.get(p, p) != p:
            continue
        u = dict(_t(p, b, a))
        if p in (merged or {}):
            u["入池閘併入"] = list(merged[p])
        build.append(u)
        drops.setdefault((b, "left"), []).append({"暫編地號": p, "G(㎡)": g, "不配地由": "內接矩形"})
    for x in extra_temp:
        build.append(dict(x))
    rows = [{"暫編地號": p, "推進側別": "left"} for p in alloc] + [{"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]
    return I(temp, build, rows, drops, own, BUR)


def _home(I, *a, **k):
    us = [u for u in _case(I, *a, **k)["units"] if u["歸戶"] == "GA"]
    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))


def _cases(ns):
    I = ns[FN_AI]
    out = []

    def run(name, fn, exp):
        try:
            got = fn()
        except Exception as e:  # noqa: BLE001
            got = ("例外", type(e).__name__)
        out.append((name, got, exp))

    # K1 ①：G 之加總 10 對 25 ⇒ B2（G 大者·⛔ 重劃前面積〔100 對 40〕）
    run("K1 G 之加總較大者", lambda: _home(I, [("u1", "B1", 100.0, 10.0), ("v1", "B2", 40.0, 25.0)]), "B2")
    # K2 ②：G 逐位相同（25／25）⇒ 重劃前面積 100 對 40 ⇒ B1（舊碼 ⇒ 停機）
    run("K2 G 相同 ⇒ 重劃前面積之合計較大者", lambda: _home(I, [("u1", "B1", 100.0, 25.0), ("v1", "B2", 40.0, 25.0)]), "B1")
    # K3 ②：G 25.004 對 24.996 ⇒ 以 0.01 ㎡ 為單位皆 25.00（相同）⇒ 重劃前面積 40 對 100 ⇒ B2（逐位比 ⇒ B1）
    run("K3 G 以 0.01 ㎡ 為單位相同 ⇒ 重劃前面積",
        lambda: _home(I, [("u1", "B1", 40.0, 25.004), ("v1", "B2", 100.0, 24.996)]), "B2")
    # K4 ①：G 25.006（⇒ 25.01）對 25.004（⇒ 25.00）⇒ 以 0.01 ㎡ 為單位相異 ⇒ B1（以「差 ≤ 0.01 即同」讀之 ⇒ B2）
    run("K4 G 以 0.01 ㎡ 為單位相異 ⇒ G", lambda: _home(I, [("u1", "B1", 40.0, 25.006), ("v1", "B2", 100.0, 25.004)]), "B1")
    # K5 ③（請示之圖一之形）：G 皆 0；重劃前面積 B1 30＋10 ＝ 40、B2 40 ⇒ 相同；最小之暫編地號 B1 p5 對 B2 p7 ⇒ B1
    #   （以重劃前面積最大之一筆代表〔p9 對 p7〕⇒ B2）
    run("K5 G、重劃前面積皆同 ⇒ 最小之暫編地號較小者",
        lambda: _home(I, [("p9", "B1", 30.0, 0.0), ("p5", "B1", 10.0, 0.0), ("p7", "B2", 40.0, 0.0)]), "B1")
    # K6 ①（請示之圖三之形·KL 答「甲」）：B1 G 20＋15 ＝ 35、B2 G 30 ⇒ B1（逐筆之最大〔20 對 30〕⇒ B2）
    run("K6 G 逐街廓加總（⛔ 逐筆）",
        lambda: _home(I, [("x1", "B1", 50.0, 20.0), ("x2", "B1", 50.0, 15.0), ("y1", "B2", 50.0, 30.0)]), "B1")
    # K7 ①：入池閘之合併單元（m1＋m2·G 40）只計一次；B2 G 50 ⇒ B2（重計 ⇒ 80 ⇒ B1）
    run("K7 合併單元之 G 只計一次",
        lambda: _home(I, [("m1", "B1", 60.0, 40.0), ("m2", "B1", 30.0, None), ("k1", "B2", 70.0, 50.0)],
                      merged={"m1": ["m1", "m2"]}), "B2")
    # K8 ②：G 皆 40；重劃前面積 B1 ＝ 合併單元之諸成員 60＋30 ＝ 90、B2 70 ⇒ B1（唯計單元之自身之片 60 ⇒ B2）
    run("K8 合併單元之重劃前面積計其諸成員",
        lambda: _home(I, [("m1", "B1", 60.0, 40.0), ("m2", "B1", 30.0, None), ("k1", "B2", 70.0, 40.0)],
                      merged={"m1": ["m1", "m2"]}), "B1")
    # K9 ②：B1 之 p 分攤登記面積 100、段三部分併出 70（受併宗 r·B3·配地）⇒ 原有面積（剩下）30；B2 之 q 50；G 皆 10
    #   ⇒ B2（以分攤登記面積 100 比 ⇒ B1）
    run("K9 重劃前面積 ＝ 原有面積（部分併出之剩下·⛔ 分攤登記面積）", lambda: _k9(I), "B2")
    # K10 ③：B1 G 10；B2、B3 G 30、重劃前面積 40（相同）；最小之暫編地號 B2 q2、B3 q1 ⇒ B3
    run("K10 三街廓：二者並列 ⇒ 其後之鍵",
        lambda: _home(I, [("q0", "B1", 90.0, 10.0), ("q2", "B2", 40.0, 30.0), ("q1", "B3", 40.0, 30.0)]), "B3")
    # K11 ⛔ 停機：G、重劃前面積皆同之二街廓（K5）⇒ 得一街廓（⛔ 例外）
    run("K11 皆同 ⇒ ⛔ 停機", lambda: isinstance(_home(I, [("a1", "B1", 40.0, 0.0), ("a2", "B2", 40.0, 0.0)]), str), True)
    # K12 原街廓之據（顯示）⛔ 變：仍為各街廓之 G 之加總
    run("K12 原街廓之據 ＝ 各街廓之 G 之加總",
        lambda: _case(I, [("x1", "B1", 50.0, 20.0), ("x2", "B1", 50.0, 15.0), ("y1", "B2", 50.0, 30.0)])["units"][0]["原街廓之據"],
        {"B1": 35.0, "B2": 30.0})
    # K13 ③：字典序（K-9-61 ⑧「暫編地號字典序小者」·`k967_rank` 之 str）：p10 對 p9 ⇒ "p10" < "p9" ⇒ B1
    run("K13 暫編地號以字典序比", lambda: _home(I, [("p10", "B1", 40.0, 0.0), ("p9", "B2", 40.0, 0.0)]), "B1")
    # K14 單一街廓 ⇒ 該街廓
    run("K14 單一街廓", lambda: _home(I, [("s1", "B2", 10.0, 0.0), ("s2", "B2", 5.0, 0.0)]), "B2")
    # K15 ③：街廓內之最小亦以字典序：B1 {p10, p2} ⇒ "p10"、B2 {p11} ⇒ "p11"；G 皆 0、重劃前面積皆 40 ⇒ B1
    #   （街廓內以數值取最小 ⇒ B1 之代表 p2 ⇒ "p11" < "p2" ⇒ B2）
    run("K15 街廓內之最小之暫編地號亦以字典序",
        lambda: _home(I, [("p10", "B1", 20.0, 0.0), ("p2", "B1", 20.0, 0.0), ("p11", "B2", 40.0, 0.0)]), "B1")
    # K16 ②（【工】甲：先加後捨）：G 皆 0；B1 之重劃前面積 10.004＋10.004 ＝ 20.008 ⇒ 20.01、B2 20.004 ⇒ 20.00 ⇒ B1
    #   （逐筆先捨後加 ⇒ 20.00 對 20.00 ⇒ 最小暫編地號 a1 ⇒ B2）
    run("K16 重劃前面積先加後捨",
        lambda: _home(I, [("b1", "B1", 10.004, 0.0), ("b2", "B1", 10.004, 0.0), ("a1", "B2", 20.004, 0.0)]), "B1")
    # K17 ②（0.01 ㎡ 為單位）：G 皆 0；重劃前面積 40.004 對 39.996 ⇒ 皆 40.00（相同）⇒ 最小暫編地號 c2 對 c1 ⇒ B2
    #   （逐位比 ⇒ B1）
    run("K17 重劃前面積以 0.01 ㎡ 為單位相同 ⇒ 暫編地號",
        lambda: _home(I, [("c2", "B1", 40.004, 0.0), ("c1", "B2", 39.996, 0.0)]), "B2")
    # K18 ②（【工】乙）：B1 之 p 分攤登記面積 100、入池閘部分併出 70（受併宗 r·B3·配地）⇒ 原有面積（剩下）30；
    #   B2 之 q 50；G 皆 10 ⇒ B2（以分攤登記面積 100 比 ⇒ B1）
    run("K18 重劃前面積 ＝ 原有面積（入池閘之帳之剩下）", lambda: _k18(I), "B2")
    return out


def _k9(I):
    p = _t("p", "B1", 100.0, 段三部分併出={"r": 70.0}, 段三併出=["r"])
    q = _t("q", "B2", 50.0)
    r = _t("r", "B3", 200.0)
    temp = [p, q, r]
    own = {t["原地號"]: "GA" for t in temp}
    build = [dict(p), dict(q), dict(r)]
    drops = {("B1", "left"): [{"暫編地號": "p", "G(㎡)": 10.0, "不配地由": "內接矩形"}],
             ("B2", "left"): [{"暫編地號": "q", "G(㎡)": 10.0, "不配地由": "內接矩形"}]}
    rows = [{"暫編地號": "r", "推進側別": "left"}, {"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]
    us = [u for u in I(temp, build, rows, drops, own, BUR)["units"] if u["歸戶"] == "GA"]
    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))


def _k18(I):
    p = _t("p", "B1", 100.0)
    q = _t("q", "B2", 50.0)
    r = _t("r", "B3", 200.0)
    temp = [p, q, r]
    own = {t["原地號"]: "GA" for t in temp}
    build = [dict(p, 入池閘部分併出={"r": 70.0}), dict(q), dict(r)]
    drops = {("B1", "left"): [{"暫編地號": "p", "G(㎡)": 10.0, "不配地由": "內接矩形"}],
             ("B2", "left"): [{"暫編地號": "q", "G(㎡)": 10.0, "不配地由": "內接矩形"}]}
    rows = [{"暫編地號": "r", "推進側別": "left"}, {"暫編地號": "B1-抵費地", "推進側別": "抵費地"}]
    us = [u for u in I(temp, build, rows, drops, own, BUR)["units"] if u["歸戶"] == "GA"]
    return us[0]["原街廓"] if len(us) == 1 else ("單位數", len(us))


def _report(cases):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def selftest(repo):
    try:
        ns = _extract_ns(_read(repo, "app.py"))
    except Exception as e:  # noqa: BLE001
        print(f"  🔴 K0 受詞：{type(e).__name__}: {e}")
        print("⇒ 紅 ['K0']；rc 1")
        return 1
    print("── 合成對照（AST 抽出之 adj_intake 等）──")
    red = _report(_cases(ns))
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _top(src):
    out = {}
    for n in ast.parse(src).body:
        k = n.name if isinstance(n, (ast.FunctionDef, ast.ClassDef)) else (
            n.targets[0].id if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
            else None)
        if k:
            out[k] = ast.dump(n)
    return out


def wiring(repo, base):
    res = []
    src = _read(repo, "app.py")
    tree = ast.parse(src)
    top = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    ai = top.get(FN_AI)
    if ai is None:
        print(f"  🔴 X0 受詞缺：{FN_AI}")
        print("⇒ 紅 ['X0']；rc 1")
        return 1
    calls = [n for n in ast.walk(ai) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "k967_rank"]
    res.append(("X1 adj_intake 呼叫 k967_rank", len(calls) >= 1, f"呼叫 {len(calls)}"))
    word = "".join(["原", "街廓"])
    rz = [ast.unparse(n)[:80] for n in ast.walk(ai) if isinstance(n, ast.Raise) and word in ast.unparse(n)]
    res.append(("X2 adj_intake 內⛔ 有其訊息及於原街廓之 raise", not rz, f"{rz}"))
    lits = sorted({n.value for n in ast.walk(ai)
                   if isinstance(n, ast.Constant) and isinstance(n.value, str) and CASE_LIT_RE.match(n.value)})
    res.append(("X4 adj_intake 內⛔ 案件字面", not lits, f"{lits}"))
    try:
        bsrc = subprocess.run(["git", "-C", repo, "show", f"{base}:app.py"], capture_output=True,
                              check=True).stdout.decode("utf-8")
        bt, ct = _top(bsrc), _top(src)
        dif = sorted(k for k in set(bt) | set(ct) if bt.get(k) != ct.get(k))
        ok3 = set(bt) == set(ct) and set(dif) <= {FN_AI} | {"k6b_stage3_run"}    # 🔧 `W-G.9-388`：其後之單所改者亦許（F32 量之）
        ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) and set(bt) <= set(ct)
                      and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389))   # 🔧 `W-G.9-389`：同（F33 量之）
        ok3 = ok3 or (set(ct) - set(bt) == set(NEW389) | set(NEW391) and set(bt) <= set(ct)
                      and set(dif) <= {FN_AI} | {"k6b_stage3_run"} | set(W389) | set(W391))   # 🔧 `W-G.9-391`：同（F35 量之）
        res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", ok3,
                    f"增 {sorted(set(ct) - set(bt))}／去 {sorted(set(bt) - set(ct))}／相異 {dif}"))
        ls = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", base, "verify/"], capture_output=True,
                            check=True).stdout.decode("utf-8").split()
        prod = sorted(p for p in ls if re.match(r"^verify/[^/]+\.py$", p))
        chg = []
        for p in prod:
            b = subprocess.run(["git", "-C", repo, "show", f"{base}:{p}"], capture_output=True, check=True).stdout
            try:
                with open(os.path.join(repo, p), "rb") as f:
                    c = f.read()
            except OSError:
                c = None
            if b != c:
                chg.append(p)
        chg = [p for p in chg if p != "verify/selection_pipeline.py"]   # 🔧 `W-G.9-389`：其增列（F33 之 X4 量之）
        chg = [p for p in chg if p not in F391]   # 🔧 `W-G.9-391`：harness 二檔之增列（F35 量之）
        res.append((f"X5 生產碼 app.py 以外之 {len(prod)} 檔對基準相異 0", not chg and len(prod) >= 1, f"相異 {chg}"))
    except Exception as e:  # noqa: BLE001
        res.append(("X3 頂層之名之集⛔ 變·相異之節點 ⊆ {adj_intake}", False, f"基準讀不到：{type(e).__name__}"))
    red = []
    for name, ok, note in sorted(res, key=lambda r_: r_[0].split()[0]):
        print(("  ✅ " if ok else "  🔴 ") + f"{name}（{note}）")
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def _q2(x):
    return Decimal(repr(float(x))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def _indep_home(unit):
    """外部錨：本器另寫之三鍵之擇（⛔ 呼叫 k967_rank／adj_q2）。"""
    g, a, m, seen = {}, {}, {}, set()
    for r in unit["建築街廓內不能分配"]:
        b = r["所屬街廓"]
        if r["所屬單元"] not in seen:
            seen.add(r["所屬單元"])
            g[b] = g.get(b, 0.0) + float(r["應分配面積"])
        a[b] = a.get(b, 0.0) + float(r["原有面積"])
        m[b] = min(m.get(b, str(r["暫編地號"])), str(r["暫編地號"]))
    best = None
    for b in sorted(g):
        k = (_q2(g[b]), _q2(a[b]))
        if best is None or k > best[0] or (k == best[0] and m[b] < best[1]):
            best = (k, m[b], b)
    return best[2] if best else None


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    cwd = os.getcwd()
    os.chdir(repo)
    red = []
    try:
        from app_harvest import harvest
        with contextlib.redirect_stdout(io.StringIO()):
            ns, fake_st = harvest(os.path.join(repo, "app.py"))
        if FN_AI not in ns:
            print(f"  🔴 R0 受詞缺：{FN_AI}")
            print("⇒ 紅 ['R0']；rc 1")
            return 1
        import run_verification as rv
        from selection_pipeline import run_corner_pk_k6b
        from stepg_pipeline import run_step_g
        for sb in sbs:
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
                print(f"🔴 執行中止（退縮 {sb}）：{str(e).splitlines()[0][:300]} ⇒ 無從判定")
                return 3
            k9 = sg.get("k929_6")
            if k9 is None:
                print(f"🔴 退縮 {sb}：run_step_g 無 k929_6 ⇒ 無從判定")
                return 3
            drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
            own = dict(fake_st.session_state.get("t8_ownership_map") or {})
            bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
            print(f"══ 退縮 {sb} ══")
            try:
                it = ns[FN_AI](tp3, k9["build"], sg["g_rows"], drops, own, bur)
            except RuntimeError as e:
                print(f"  🔴 R1 盤點停機：{str(e)[:300]}")
                red.append(f"R1@{sb}")
                continue
            print("  ✅ R1 盤點⛔ 停機")
            bad2 = []
            for u in it["units"]:
                if not u["建築街廓內不能分配"]:
                    continue
                ind = _indep_home(u)
                blks = sorted({r["所屬街廓"] for r in u["建築街廓內不能分配"]})
                if len(blks) >= 2:
                    print(f"     {u['歸戶']}｜原街廓 {u['原街廓']}｜據 "
                          + "、".join(f"{b} {u['原街廓之據'].get(b, 0.0):.2f}" for b in blks) + f"｜外部錨 {ind}")
                if ind != u["原街廓"]:
                    bad2.append((u["歸戶"], u["原街廓"], ind))
            print(("  ✅" if not bad2 else "  🔴") + f" R2 建地軌之原街廓 ＝ 本器之三鍵之擇：相異 {bad2}")
            if bad2:
                red.append(f"R2@{sb}")
            exp = EXPECT_RUN.get(sb)
            got = {u["歸戶"]: u["原街廓"] for u in it["units"]}
            if exp is None:
                print(f"  🔴 R3 退縮 {sb} 無外部錨")
                red.append(f"R3@{sb}")
                continue
            dif3 = sorted(g for g in set(exp) | set(got) if exp.get(g, "缺") != got.get(g, "缺"))
            print(("  ✅" if not dif3 else "  🔴") + f" R3 合併單位（{len(got)}）之原街廓 ＝ 外部錨（{len(exp)}）：相異 {dif3}")
            if dif3:
                red.append(f"R3@{sb}")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3 or argv[1] not in ("selftest", "wiring", "run"):
        print(__doc__)
        return 2
    repo = os.path.abspath(argv[2])
    if argv[1] == "selftest":
        return selftest(repo)
    if argv[1] == "wiring":
        if len(argv) != 4:
            print(__doc__)
            return 2
        return wiring(repo, argv[3])
    sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
    return run(repo, sbs)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
