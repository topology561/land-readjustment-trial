# -*- coding: utf-8 -*-
"""W-G.9-363 量測器（發單側窗六十四擬·檔 F23·⛔ 由受單側改一字）：規格步 4 甲（`K-9-53` ①·手冊先行）——地主已有
配得土地者，其分不到之建地、道路與公設地上之土地依手冊併入其已配得之宗（`app.py` 之 `k953_manual_run`）。

子命令（一律 python verify/probes/probe_WG9363_k953.py <子命令> …）：
  selftest <repo>
           合成對照（⛔ 讀本案資料·`harvest(app.py)` 取 `k953_manual_run`／`k953_enabled`／`k953_alloc_summary`／
           `k953_units_of`／`adj_intake`；`verify/selection_pipeline.py` 取 `k6b_stage3_pool_temp`）。玩具之回呼：
           `alloc_state` 以 build 之全部（`drop` 除外）為保留；街廓內受併之累加（`面積_m2` 之和）`>` 該街廓之容量 ⇒ 該街廓
           之配餘地不合格一處；`err_cap` 逾者 ⇒ 配地中止；`G` ＝ 分攤登記面積 ＋ 面積（`gmap` 覆寫）；`units` ＝ 入池閘之
           合併單元（`unit_g` ⇒ 取代後之 G 異）；`a_prime` ＝ a(src) × p(src 之街廓) ÷ p(dst 之街廓）。
           K1〜K27 ＝ 各支；P0 ＝ 判式自驗（逐項擾動其期須恰該項紅）。
           🔧 `W-G.9-363` 補令一（發單側窗六十四·⛔ 上列一字不刪）：K28 ＝ `K-9-51` 之候選含 x 之本街廓之宗 ⇒ 先試併之
           （`K-9-55`）、其檢核不過 ⇒ 記未成、續試（補令二·乙案）（裁二）；K29 ＝ 入池閘之旗標 off ⇒ 手冊先行不辦（harness 與畫面·二旗標皆判·裁一）；K30 ＝ 畫面之旗標值非法 ⇒
           走停機之路（`f3_k6b_stage3_error`·`st.error`·`st.stop`·裁五）；K31 ＝ 入池閘之單元之取代後 build ⊂ temp（同物件）
           且 temp 中之標的 ＝ 單元（裁三）。P0 隨之 31 項。
           🔧 補令二（⛔ 上列一字不刪）：K32 ＝ `K-9-51` 之候選同距離（0）而本街廓之宗與他街廓之宗（G 較大）並存 ⇒ 本街廓
           之宗居先（KL `2026-10-03` 採乙案·`K-9-55` 之二）；K33 ＝ 本街廓之候選與 x 相連（`C0` 之後始為已配得）⇒ 停機
           （入池閘之射程）。P0 隨之 33 項。
           🔧 補令三（⛔ 上列一字不刪）：K34 ＝ 本街廓之候選之成員取當下之試算（其單元於 `C0` 之後始含與 x 相接之片 ⇒
           停機）；K35 ＝ 整筆者於候選之迴圈之前全檢本街廓之候選（G 較大而⛔ 相接之宗居先亦停機）；K36 ＝ x 於當下之試算
           已自為已配得之宗或為其成員 ⇒ 停機（`K-9-51` 之「剩餘土地」不立）。P0 隨之 36 項。
           🔧 補令四（⛔ 上列一字不刪）：K37 ＝ 逐片之整筆之主併入（其檢核過）之前，x 於當下之試算已自為已配得之宗或為
           其成員 ⇒ 停機（`K-9-53` ① 之「分不到」不立）；K38 ＝ 同時點，本街廓之已配得之宗（同歸戶·當下之試算）之成員
           與 x 相連 ⇒ 停機（入池閘之射程·`R-6` (a) 之同街廓之例）——成員與宗皆取當下之試算、全檢、⛔ 取聯集。P0 隨之 38 項。
           🔧 `W-G.9-364`（⛔ 上列一字不刪）：K39 ＝ 同時點，x 於當下之試算為他街廓之已配得之宗（同歸戶、他歸戶）之成員
           ⇒ 停機；K40 ＝ 同時點，x 為本街廓之他歸戶之已配得之宗之成員 ⇒ 停機——K37 之 (ii) 之廣度（一切街廓·一切歸戶）。
           P0 隨之 40 項。
           🔧 `W-G.9-370`（⛔ 上列一字不刪）：K36／K37／K39／K40 之停機之期改為 `S219` 之新訊息（`K-9-57` ⑧·程式自我檢查·
           `S219_PH`）；項數⛔ 變。
           🔧 `W-G.9-373`（⛔ 上列一字不刪）：K3 之期改依 `K-9-67`（應分配面積並列 ⇒ 重劃前面積大者 ⇒ 暫編地號小者·⛔ 停機）；
           K14／K23／K28／K32〜K36 之期改依 `K-9-66`／`K-9-68`（整批不過 ⇒ 逐受併之街廓：建地可按比例部分併入〔留 build·
           `面積_m2` 減其量〕；剩下依 `K-9-51` 逐輪、同一輪到達同一街廓者一起；剩下之列於諸輪之後）。玩具之受併之累加唯計
           正之 `面積_m2`（建地之部分併出之負值⛔ 計）；K28／K32 之「本街廓之宗之檢核不過」改以其容量 `0` 造之。項數⛔ 變。
           wiring：W6 之受詞去本單所改之六函式（`k6b_stage3_run`、`k929_6_fixpoint`、`adj_intake`、`k6b_screen_callbacks`、
           `_k6b_callbacks`、`k6b_stage3_pool_temp`）；W7 之許增本單之新名與所改者；W8 之錨⛔ 計 `ANC_SKIP373`（本單之生產碼
           必增其見者）、函式名許 `FN_GONE373`（本單所去之巢狀 def）為 `0`。
  wiring   <repo> <基準 commit>
           接線（AST·字樣·工作樹對基準）：W1 模組層之新名與簽名；W2 harness 之入口（`run_k953`）與 `run_corner_pk_k6b`
           之序（末端塊合併再試之後、以 winners／forced 呼叫、其後⛔ 重跑街角選位）；W3 畫面之入口（`f3_screen_k953`·
           ⛔ 呼叫街角選位）；W4 畫面 `f3_screen_k6b_stage3` 之序；W5 新碼⛔ 案件字面；W6 既有函式（段三、末端塊合併再試、
           地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、main 等）對基準一字未動；W7 頂層節點之相異 ⊆ 本單之許；
           W8 既有量測器之錨（其字串常數〔長 ≥ 4〕於基準之 app.py／selection_pipeline.py 恰一見者）於工作樹仍恰一見；
           基準中恰一之函式名（含巢狀）於工作樹仍恰一（新碼⛔ 同名）。
  run      <repo> [<退縮> …]
           harness 實跑本案（預設退縮 `3.5`、`0.0`）：R1 手冊先行之紀錄逐列 ＝ 本器所載；R2 街角第 1 宗之宗 ＝ 旗標 off 之
           實跑（街角定案·`v3` §8）；R3 配地之全部（各宗之街廓·推進側·G）與各街廓之抵費地 ＝ 本器所載（容差 `0.01`）且
           Σ抵費地之減 ＝ ΣG 之增（容差 `0.1`）；R4 調配之輸入之類（切片數·原有面積）＝ 本器所載、待同歸戶併入 ＝ 空。
           🔧 `W-G.9-367`（⛔ 上列一字不刪）：本子命令於行程內設 `WV_ADJ4=off`（本器量手冊先行之果；規格步 4 乙之果
           另由 F24 之 run 量之）。
  offsnap  <repo> <out.json> [<退縮> …]
           於行程內設 WV_K953=off，harness 實跑本案（預設退縮 `3.5`、`0.0`），以 sha256 摘要其街角、宗地（暫編地號·
           段三之三鍵·面積二欄）、build、段三紀錄、末端塊紀錄、配地列、入池閘紀錄、不配地紀錄、調配之輸入，寫 out。
  offcmp   <a.json> <b.json>
           二 offsnap 之摘要逐項同（手冊先行之紀錄之列數唯出艙·⛔ 入判）。
  gatesnap <repo> <out.json> [<退縮> …]
           🔧 補令一：同 offsnap，唯於行程內設 WV_K929_6=off 並去 WV_K953（入池閘 off·手冊先行之旗標未設）；二份以
           offcmp 比之（入池閘 off ⇒ 逐位同開工態之同設定·`R-17′`）。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import ast, contextlib, copy, importlib.util, io, os, re, subprocess, sys, warnings

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

TOL = 0.01
FN = "k953_manual_run"
SIG = ["temp_parcels", "build_parcels", "own_map", "blocks", "centerlines", "a_prime", "alloc_state"]
RK_SIG = ["ns", "fake_st", "cb", "cad", "param_rows", "temp_parcels", "build_parcels", "setback"]
RK_KW = ["snapshot", "callbacks", "winners", "forced"]
# 🆕 `W-G.9-370`（K-9-57 ⑧）：`S219`（`_wpre953`·整筆之主併入之前之查）之停機訊息之期（程式自我檢查）
S219_PH = ("程式自我檢查", "依既定機制不會發生", "觸之即程式有錯")


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _report(cases, verbose=True):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        if verbose:
            print(f"  ✅ {name}" if ok else f"  🔴 {name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


def _run(out, name, fn, exp):
    try:
        got = fn()
    except Exception as ex:  # noqa: BLE001
        got = ("例外", type(ex).__name__, str(ex)[:160])
    out.append((name, got, exp))


# ── 玩具（⛔ 本案資料）──
H, PK, RDC = "住宅區", "鄰里公園", "道路"


def _R(x0, x1, y0, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


def _tp(pid, blk, cat, poly, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "polygon_coords": [list(c) for c in poly],
            "所屬街廓": blk, "街廓分類": cat, "分攤登記面積_m2": float(a), "面積_m2": 0.0}


def _a(t):
    return float(t.get("分攤登記面積_m2", 0) or 0) + float(t.get("面積_m2", 0) or 0)


def _cbs(cap=None, price=None, drop=(), gmap=None, err_cap=None, units=None, unit_g=None):
    """玩具之回呼。`units` ＝ `{標的: [成員…]}`（入池閘之合併單元·其成員⛔ 單列）；`unit_g` ＝ 取代後之 G（覆寫·造相異）。"""
    cap, price, gmap, err_cap, units = cap or {}, price or {}, gmap or {}, err_cap or {}, units or {}

    def a_prime(src, dst):
        return _a(src) * price.get(src["所屬街廓"], 1.0) / price.get(dst["所屬街廓"], 1.0)

    def alloc_state(temp, build):
        kept, bad, G, acc, mem, uu = {}, {}, {}, {}, {}, {}
        ids = {b["暫編地號"] for b in build}
        for b in build:
            # 🔧 `W-G.9-373`：受併之累加唯計正之 面積_m2（建地之部分併出之負值⛔ 計）
            acc[b["所屬街廓"]] = acc.get(b["所屬街廓"], 0.0) + max(0.0, float(b.get("面積_m2", 0) or 0))
        for blk, v in acc.items():
            if v > err_cap.get(blk, 1e18) + 1e-9:
                return {"kept": {}, "bad_pools": {}, "err": f"玩具之配地中止（{blk}）", "G": {}, "members": {},
                        "units": {}}
        mat = set()
        for b in build:
            p = b["暫編地號"]
            if p in units and "入池閘併入" in b:
                mat.add(p)
        for b in build:
            p = b["暫編地號"]
            if p in drop or any(p in m and h != p for h, m in units.items()):
                continue
            kept.setdefault(b["所屬街廓"], set()).add(p)
            G[p] = gmap.get(p, _a(b))
            if p in units:
                G[p] = gmap.get(p, sum(_a(next(t for t in temp if t["暫編地號"] == m)) for m in units[p]))
                if p in mat and unit_g is not None:
                    G[p] = unit_g
                mem[p] = list(units[p])
                u = copy.deepcopy(b)
                u["入池閘併入"] = sorted(units[p])
                uu[p] = u
            else:
                mem[p] = [p]
        for blk, v in acc.items():
            if v > cap.get(blk, 1e18) + 1e-9:
                bad[blk] = 1
        return {"kept": kept, "bad_pools": bad, "err": None, "G": G, "members": mem, "units": uu}
    return a_prime, alloc_state


def _w1():
    """世界一（跨分配線·道路·公設地）：BA x∈[0,20]、BB x∈[20,40]、BD x∈[40,60]（y∈[0,30]·分配線相接）；
    道路 RD（y∈[-10,0]·x∈[0,60]·中心線 y＝-5）；BC（y∈[-40,-10]·x∈[0,60]）；公園 PK（y∈[30,50]·x∈[20,40]）。"""
    t = [_tp("X1(1)", "BA", H, _R(10, 20, 0, 30), 60), _tp("X1(2)", "BB", H, _R(20, 30, 0, 30), 300),
         _tp("Y1(1)", "BB", H, _R(30, 40, 0, 30), 200), _tp("Z1(1)", "BD", H, _R(40, 50, 0, 30), 400),
         _tp("Q1(1)", "BA", H, _R(0, 10, 0, 30), 300), _tp("Q2(1)", "BD", H, _R(50, 60, 0, 30), 300),
         _tp("R1(1)", "RD", RDC, _R(20, 30, -10, 0), 100), _tp("R9(1)", "RD", RDC, _R(0, 20, -10, 0), 200),
         _tp("R8(1)", "RD", RDC, _R(30, 60, -10, 0), 300),
         _tp("C1(1)", "BC", H, _R(20, 30, -40, -10), 300), _tp("C9(1)", "BC", H, _R(0, 20, -40, -10), 300),
         _tp("C8(1)", "BC", H, _R(30, 60, -40, -10), 300),
         _tp("P1(1)", "PK", PK, _R(20, 30, 30, 50), 200), _tp("P9(1)", "PK", PK, _R(30, 40, 30, 50), 200)]
    own = {"X1": "g1", "Y1": "gY", "Z1": "gZ", "Q1": "gQ", "Q2": "gQ2", "R1": "g1", "R9": "gR", "R8": "gR8",
           "C1": "g1", "C9": "gC", "C8": "gC8", "P1": "g1", "P9": "gP"}
    blocks = {"BA": {"category": H}, "BB": {"category": H}, "BD": {"category": H}, "RD": {"category": RDC},
              "BC": {"category": H}, "PK": {"category": PK}}
    return t, own, blocks, {"RD": [(-10.0, -5.0), (70.0, -5.0)]}


def _go(world, *, own_upd=None, a_upd=None, drop=("X1(1)",), cap=None, price=None, gmap=None, err_cap=None,
        units=None, unit_g=None, pre=None, extra=None, rm=(), blk_upd=None, geom_upd=None, cl_upd=None):
    t, own, blocks, cl = world()
    for e in (extra or []):
        t.append(copy.deepcopy(e))
    t = [x for x in t if x["暫編地號"] not in rm]
    own = dict(own, **(own_upd or {}))
    blocks = dict(blocks, **{k: {"category": v} for k, v in (blk_upd or {}).items()})
    cl = dict(cl, **(cl_upd or {}))
    for pid, a in (a_upd or {}).items():
        next(x for x in t if x["暫編地號"] == pid)["分攤登記面積_m2"] = float(a)
    for pid, poly in (geom_upd or {}).items():
        next(x for x in t if x["暫編地號"] == pid)["polygon_coords"] = [list(c) for c in poly]
    for pid, kv in (pre or {}).items():
        next(x for x in t if x["暫編地號"] == pid).update(kv)
    build = [x for x in t if x["街廓分類"] == H]
    ap, st = _cbs(cap, price, drop, gmap, err_cap, units, unit_g)
    return _NS["fn"](t, build, own, blocks, cl, ap, st, log_print=lambda *x: None), t, build


_NS = {}


def _rows(res):
    """手冊之列（序 ＝ 手冊／K-9-51）之 (片, 類, 受併宗, ((受併宗, 併入量 2 位)…), 結果)。"""
    t2, b2, log = res[0]
    out = []
    for r in log:
        if r.get("序") not in ("手冊", "K-9-51"):
            continue
        rv = r.get("受併宗")
        rv = rv if isinstance(rv, str) else tuple(rv)
        q = tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))
        out.append((r.get("序"), r.get("片"), r.get("類"), rv, q, r.get("結果")))
    return out


def _keys(res):
    t2 = res[0][0]
    out = {}
    for x in t2:
        d = {}
        for k in ("段三併出", "段三部分併出", "段三餘量"):
            if k in x:
                v = x[k]
                d[k] = (round(float(v), 2) if not isinstance(v, (list, dict))
                        else (tuple(v) if isinstance(v, list) else tuple(sorted((a, round(b, 2)) for a, b in v.items()))))
        if d:
            out[x["暫編地號"]] = d
    return out


def _acc(res):
    return {x["暫編地號"]: round(float(x.get("面積_m2", 0) or 0), 2) for x in res[0][0]
            if float(x.get("面積_m2", 0) or 0)}


def _halt(fn, phrase):
    try:
        fn()
    except RuntimeError as e:
        return ("停機", phrase in str(e))
    return ("無停機",)


def _sel(res, pid):
    return [r for r in _rows(res) if r[1] == pid]


def _cases(ns, sp):
    out = []
    _NS["fn"] = ns[FN]
    W = _w1
    G1 = {"C1": "gC1"}          # 地主 g1 之已配得唯 BB 之 X1(2)
    BE = {"blk_upd": {"BE": H}, "extra": [_tp("E1(1)", "BE", H, _R(10, 20, 30, 50), 300)]}
    _run(out, "K1 跨分配線（所鄰之已配得之宗恰一）⇒ 整筆併入、出 build、帶 段三併出",
         lambda: (lambda r: (_rows(r), _keys(r)["X1(1)"], "X1(1)" in [b["暫編地號"] for b in r[0][1]]))(_go(W, own_upd=G1)),
         ([("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 60.0),), "成"),
           ("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 100.0),), "成"),
           ("手冊", "P1(1)", "c", "X1(2)", (("X1(2)", 200.0),), "成")],
          {"段三併出": ("X1(2)",)}, False))
    _run(out, "K2 跨分配線（所鄰之已配得之宗分處二街廓）⇒ 併入應分配面積（G）較大者",
         lambda: _sel(_go(W, own_upd=dict(G1, E1="g1"), a_upd={"E1(1)": 500}, **BE), "X1(1)"),
         [("手冊", "X1(1)", "a", "E1(1)", (("E1(1)", 60.0),), "成")])
    # 🔧 `W-G.9-373`（`K-9-67`·KL 裁 `2026-10-08 04:47`）：並列 ⇒ 重劃前面積大者 ⇒ 暫編地號小者（⛔ 停機）
    _run(out, "K3 （K-9-67）二者之 G 並列 ⇒ 重劃前面積同（300）⇒ 暫編地號小者 E1(1)；E1 之重劃前面積 250 ⇒ X1(2)",
         lambda: (_sel(_go(W, own_upd=dict(G1, E1="g1"), **BE), "X1(1)"),
                  _sel(_go(W, own_upd=dict(G1, E1="g1"), a_upd={"E1(1)": 250}, gmap={"E1(1)": 300.0}, **BE), "X1(1)")),
         ([("手冊", "X1(1)", "a", "E1(1)", (("E1(1)", 60.0),), "成")],
          [("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 60.0),), "成")]))
    _run(out, "K4 建地片與同街廓之已配得之宗相鄰 ⇒ 停機（入池閘之射程）",
         lambda: _halt(lambda: _go(W, own_upd={"Q1": "g1"}, rm=("X1(2)",)), "入池閘之射程"), ("停機", True))
    _run(out, "K5 道路·兩側皆有 ⇒ 依中心線切分、各半併入該側之宗（a′ × 半之面積比）",
         lambda: _sel(_go(W), "R1(1)"),
         [("手冊", "R1(1)", "b", ("C1(1)", "X1(2)"), (("C1(1)", 50.0), ("X1(2)", 50.0)), "成")])
    _run(out, "K6 道路·唯一側有 ⇒ 整筆往該側（所鄰之街廓依中心線分側）",
         lambda: _sel(_go(W, own_upd=G1), "R1(1)"),
         [("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 100.0),), "成")])
    _run(out, "K7 道路·兩側皆無 ⇒ 未併、帶 段三餘量 ＝ a（視同無同歸戶）",
         lambda: (lambda r: (_sel(r, "S1(1)"), _keys(r).get("S1(1)")))(_go(
             W, own_upd={"S1": "g1"}, blk_upd={"RE": RDC, "BF": H}, cl_upd={"RE": [(65.0, -20.0), (65.0, 60.0)]},
             extra=[_tp("S1(1)", "RE", RDC, _R(60, 70, 0, 30), 150), _tp("F1(1)", "BF", H, _R(70, 90, 0, 30), 300)])),
         ([("手冊", "S1(1)", "b", "—", (), "未併")], {"段三餘量": 150.0}))
    _run(out, "K8 道路片全在無已配得之側（⛔ 鄰有之側之街廓）⇒ 仍整筆往有之側",
         lambda: _sel(_go(W, own_upd=G1, a_upd={"R1(1)": 50}, geom_upd={"R1(1)": _R(20, 30, -10, -5)},
                          extra=[_tp("R0(1)", "RD", RDC, _R(20, 30, -5, 0), 50)]), "R1(1)"),
         [("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 50.0),), "成")])
    _run(out, "K9 隔道路之分不到之建地 ⇒ 隨道路片往另一側之宗",
         lambda: [r for r in _rows(_go(W, drop=("X1(1)", "C1(1)"))) if r[1] in ("C1(1)", "R1(1)")],
         [("手冊", "C1(1)", "a", "X1(2)", (("X1(2)", 300.0),), "成"),
          ("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 100.0),), "成")])
    _run(out, "K10 公設地 ⇒ 平分於其合併群所及之已配得之街廓（群外之已配得之宗⛔ 與）",
         lambda: _sel(_go(W, own_upd={"Z1": "g1"}), "P1(1)"),
         [("手冊", "P1(1)", "c", ("C1(1)", "X1(2)"), (("C1(1)", 100.0), ("X1(2)", 100.0)), "成")])
    _run(out, "K11 公設地不相連於任何已配得之宗 ⇒ 未併、帶 段三餘量 ＝ a",
         lambda: (lambda r: (_sel(r, "P1(1)"), _keys(r).get("P1(1)")))(
             _go(W, rm=("X1(2)",), own_upd={"Z1": "g1"})),
         ([("手冊", "P1(1)", "c", "—", (), "未併")], {"段三餘量": 200.0}))
    _run(out, "K12 路口之道路片（鄰三街廓以上、含公設地）⇒ 比照公設地平分",
         lambda: _sel(_go(W, own_upd={"Z1": "g1", "R8": "g1"}, rm=("C8(1)",), blk_upd={"PQ": PK},
                          extra=[_tp("V1(1)", "PQ", PK, _R(30, 60, -40, -10), 900)]), "R8(1)"),
         [("手冊", "R8(1)", "c", ("C1(1)", "X1(2)", "Z1(1)"),
           (("C1(1)", 100.0), ("X1(2)", 100.0), ("Z1(1)", 100.0)), "成")])
    _run(out, "K13 落點四層瀑布：① 同原地號者先於較近者；② 皆非同原地號 ⇒ 質心距近者；③ 等距 ⇒ G 大者；④ 皆同 ⇒ 暫編地號",
         lambda: _k13(W), ("C8(1)", "C1(1)", "C9(1)", "C8(1)"))
    # 🔧 `W-G.9-373`（`K-9-66`）：建地整筆不過 ⇒ 按比例部分併入 10；剩下 50 依 K-9-51
    _run(out, "K14 （K-9-66）整批不過 ⇒ 建地整筆不過 ⇒ 按比例部分併入 10；剩下 50 依 K-9-51（他街廓之已配得之宗·距離近者先）",
         lambda: _rows(_go(W, own_upd={"Z1": "g1"}, cap={"BB": 10.0}, rm=("R1(1)", "P1(1)"))),
         [("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 10.0),), "部分成"),
          ("K-9-51", "X1(1)", "a", "C1(1)", (("C1(1)", 50.0),), "成")])
    _run(out, "K15 可拆分之片之最大面積（0.01 ㎡ 之格）；其餘 ⇒ K-9-51 皆無 ⇒ 入合併單位、帶 段三部分併出／段三餘量",
         lambda: (lambda r: (_rows(r), _keys(r).get("R1(1)")))(
             _go(W, own_upd=G1, rm=("X1(1)", "P1(1)"), drop=(), cap={"BB": 33.333})),
         ([("手冊", "R1(1)", "b", "X1(2)", (("X1(2)", 33.33),), "部分成"),
           ("K-9-51", "R1(1)", "b", "—", (), "入合併單位")],
          {"段三併出": ("X1(2)",), "段三部分併出": (("X1(2)", 33.33),), "段三餘量": 66.67}))
    _run(out, "K16 併入後配地中止 ⇒ 不過（記其由·⛔ 停機）",
         lambda: (lambda r: ([x for x in r[0][2] if x["序"] == "整批"][0]["結果"],
                             "配地中止" in [x for x in r[0][2] if x["序"] == "整批"][0].get("不過之由", ""),
                             [(x[1], x[-1]) for x in _rows(r)]))(
             _go(W, own_upd=G1, rm=("P1(1)",), err_cap={"BB": 100.0})),
         ("未成", True, [("X1(1)", "成"), ("R1(1)", "部分成"), ("R1(1)", "入合併單位")]))
    _run(out, "K17 帶段三之鍵之片⛔ 受理",
         lambda: [r[1] for r in _rows(_go(W, pre={"R1(1)": {"段三併出": ["X1(2)"]}, "P1(1)": {"段三餘量": 200.0}}))],
         ["X1(1)"])
    _run(out, "K18 無任何配得土地之地主⛔ 受理（無受詞 ⇒ 回輸入之同一物件、紀錄 ＝ []）",
         lambda: (lambda r, t, b: (r[0] is t, r[1] is b, r[2]))(*_go(W, drop=("X1(1)", "X1(2)", "C1(1)"))),
         (True, True, []))
    _run(out, "K19 入池閘之合併單元：取代後之配地全同 ⇒ 取代；相異 ⇒ ⛔ 取代（記之）",
         lambda: (_unit_rows(_go(W, units={"X1(2)": ["X1(2)", "Y1(1)"]}, own_upd={"Y1": "g1"})),
                  _unit_rows(_go(W, units={"X1(2)": ["X1(2)", "Y1(1)"]}, own_upd={"Y1": "g1"}, unit_g=1.0))),
         ([("X1(2)", "取代")], [("X1(2)", "未取代（取代後之配地相異）")]))
    _run(out, "K20 調配之輸入（⛔ 改·沿用段三之鍵）：併出 ⇒ 原位次配地（所屬單元『段三併入 …』）；餘量 ⇒ 入合併單位；待同歸戶併入 ＝ 空",
         lambda: _k20(ns, W), ("原位次配地", "段三併入 X1(2)", "共同負擔用地·入合併單位", 0))
    _run(out, "K21 公設地調配之 temp（⛔ 改·沿用段三之鍵）：併出而無餘量 ⇒ 去之；部分併出 ⇒ 依餘量之比縮之",
         lambda: _k21(sp), (["Q", "R"], 25.0))
    _run(out, "K22 a′ 之折算（街廓之地價比）",
         lambda: _rows(_go(W, rm=("Z1(1)", "R1(1)", "P1(1)"), price={"BA": 2.0, "BB": 1.0}))[0][4],
         (("X1(2)", 120.0),))
    # 🔧 `W-G.9-373`（`K-9-66`／`K-9-68`）：建地全入、道路按比例（1／100）、公設地未試；入合併單位之列於諸輪之後
    _run(out, "K23 （K-9-66）整批不過時：建地先（全入）、道路次（按比例）、公設地未試；剩下之列於諸輪之後",
         lambda: [(r[1], r[5]) for r in _rows(_go(W, own_upd=G1, cap={"BB": 61.0}))],
         [("X1(1)", "成"), ("R1(1)", "部分成"), ("P1(1)", "未成"), ("R1(1)", "入合併單位"), ("P1(1)", "入合併單位")])
    _run(out, "K24 旗標 WV_K953：未設／on ⇒ 真；off ⇒ 偽；他值 ⇒ 停機",
         lambda: _k24(ns), (True, True, False, "停機"))
    _run(out, "K25 可為受詞之片之歸戶於 build 皆無片（例：歸戶表為空）⇒ ⛔ 試算配地、回輸入之同一物件、紀錄 ＝ []",
         lambda: _k25(W), (True, True, [], 0))
    _run(out, "K26 試算之摘要：抵費地之形放不下最小建築面積之矩形 ⇒ 配餘地不合格一處；保留 ⇒ 保留宗與其 G；餘⛔ 計",
         lambda: _k26(ns), ({"B1": ["A(1)"]}, {"B1": 1}, {"A(1)": 123.4}))
    _run(out, "K27 入池閘之單元：成員（缺 ⇒ 自身）；成員 ≥ 2 者為單元（深拷貝）",
         lambda: _k27(ns), ({"A(1)": ["A(1)", "A(2)"], "B(1)": ["B(1)"]}, ["A(1)"], False))
    # 🔧 補令一（⛔ 上列一字不刪）
    _run(out, "K28 K-9-51 之候選含 x 之本街廓之已配得之宗（與 x ⛔ 相連·距離 0）⇒ 先試併之、過 ⇒ 併入、出 build（K-9-55）；"
              "其檢核不過 ⇒ 記未成、續試他宗；皆不行 ⇒ 入合併單位（補令二·乙案）",
         lambda: _k28(W),
         # 🔧 `W-G.9-373`（`K-9-66`）：X1(2) 按比例收 10；剩下 50 ⇒ Q1（本街廓）；Q1 不容（BA 之容量 0）⇒ 未成 ⇒ 入合併單位
         ([("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 10.0),), "部分成"),
           ("K-9-51", "X1(1)", "a", "Q1(1)", (("Q1(1)", 50.0),), "成")], False,
          [("手冊", "X1(1)", "a", "X1(2)", (("X1(2)", 10.0),), "部分成"), ("K-9-51", "X1(1)", "a", "Q1(1)", (), "未成"),
           ("K-9-51", "X1(1)", "a", "—", (), "入合併單位")]))
    _run(out, "K29 入池閘之旗標 off（WV_K929_6）⇒ 手冊先行不辦（harness 與畫面皆回輸入之同一物件、紀錄 []、畫面⛔ 呼叫 st）；"
              "二旗標皆判（WV_K953 off 而 WV_K929_6 非法 ⇒ 停機）",
         lambda: _k29(ns, sp), ((True, True, []), "停機", (True, True, [], [], [])))
    _run(out, "K30 畫面：旗標值非法（WV_K953 或 WV_K929_6）⇒ f3_k6b_stage3_error ＝ （手冊先行）…、st.error ＋ st.stop、"
              "⛔ 寫紀錄",
         lambda: _k30(ns), (("停機", ["error", "stop"], True, False), ("停機", ["error", "stop"], True, False)))
    _run(out, "K31 入池閘之單元之取代後：build ⊂ temp（同物件）、temp 中之標的 ＝ 單元（帶入池閘併入）、他成員仍在 temp 而⛔ 在 build",
         lambda: _k31(W), (True, 1, True, ["X1(2)", "Y1(1)"], True, False))
    # 🔧 補令二（⛔ 上列一字不刪）
    _run(out, "K32 K-9-51 之候選同距離（0）：本街廓之宗居先於他街廓之宗（G 較大者亦然·K-9-55 之二）；本街廓無之、或其檢核不過 ⇒ "
              "他街廓之宗",
         lambda: _k32(W),
         # 🔧 `W-G.9-373`（`K-9-66`）：X1(2) 按比例收 10 ⇒ 剩下 50（本街廓之不容 ⇒ BA 之容量 0）
         ([("K-9-51", "X1(1)", "a", "Q1(1)", (("Q1(1)", 50.0),), "成")],
          [("K-9-51", "X1(1)", "a", "E1(1)", (("E1(1)", 50.0),), "成")],
          [("K-9-51", "X1(1)", "a", "Q1(1)", (), "未成"), ("K-9-51", "X1(1)", "a", "E1(1)", (("E1(1)", 50.0),), "成")]))
    _run(out, "K33 K-9-51 之本街廓之候選與 x 相連（C0 之後始為已配得）⇒ 停機（入池閘之射程）；⛔ 相連 ⇒ 本街廓之宗居先、併入之",
         # 🔧 `W-G.9-373`（`K-9-66`）：X(1) 先按比例併入 B1(1) 10 ⇒ 剩下 290
         lambda: _k33(),
         (("停機", True), [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 290.0),), "成")]))
    # 🔧 補令三（⛔ 上列一字不刪）
    _run(out, "K34 K-9-51 之本街廓之候選之成員取當下之試算：其單元於 C0 之後始含與 x 相接之片 ⇒ 停機（入池閘之射程）；"
              "該片⛔ 與 x 相接 ⇒ 併入之；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ ⛔ 停機（⛔ 取聯集）",
         # 🔧 `W-G.9-373`（`K-9-66`）：X(1) 先按比例併入 B1(1) 10 ⇒ 剩下 290
         lambda: _k34(),
         (("停機", True), [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 290.0),), "成")],
          [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 290.0),), "成")]))
    _run(out, "K35 整筆者於候選之迴圈之前全檢本街廓之候選：G 較大而⛔ 與 x 相接之宗居先、G 較小者與 x 相接 ⇒ 停機；"
              "後者⛔ 與 x 相接 ⇒ 併入 G 較大者",
         # 🔧 `W-G.9-373`（`K-9-66`）：X(1) 先按比例併入 B1(1) 10 ⇒ 剩下 290
         lambda: _k35(),
         (("停機", True), [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 290.0),), "成")]))
    _run(out, "K36 x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入",
         # 🔧 `W-G.9-373`（`K-9-66`）：X(1) 先按比例併入 B1(1) 10 ⇒ 剩下 290
         lambda: _k36(),
         (("停機", True), ("停機", True), [("K-9-51", "X(1)", "a", "A1(1)", (("A1(1)", 290.0),), "成")]))
    # 🔧 補令四（⛔ 上列一字不刪）
    _run(out, "K37 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算已自為已配得之宗、或為已配得之宗之成員 ⇒ 停機"
              "（程式自我檢查·K-9-57 ⑧）；皆非 ⇒ 併入其計畫之受併宗",
         lambda: _k37(),
         (("停機", True), ("停機", True), [("手冊", "X(1)", "a", "B1(1)", (("B1(1)", 300.0),), "成")]))
    _run(out, "K38 逐片之整筆之主併入（其檢核過）之前：本街廓之已配得之宗（同歸戶·當下之試算）之成員與 x 相連 ⇒ 停機"
              "（入池閘之射程）——C0 之後始為已配得之宗（G 較小）、或已配得之宗之單元於 C0 之後始含與 x 相接之片，皆停機；"
              "⛔ 相接 ⇒ 併入；C0 之 members 所載之舊單元含與 x 相接之片而當下之單元⛔ 含 ⇒ ⛔ 停機（⛔ 取聯集）",
         lambda: _k38(),
         (("停機", True), ("停機", True), [("手冊", "X(1)", "a", "B1(1)", (("B1(1)", 300.0),), "成")],
          [("手冊", "X(1)", "a", "B1(1)", (("B1(1)", 300.0),), "成")]))
    # 🔧 W-G.9-364（⛔ 上列一字不刪）
    _run(out, "K39 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為他街廓之已配得之宗之成員——同歸戶（BD 之 D1(1)）、"
              "他歸戶（BD 之 D9(1)）⇒ 皆停機（程式自我檢查·K-9-57 ⑧）",
         lambda: _k39(),
         (("停機", True), ("停機", True)))
    _run(out, "K40 逐片之整筆之主併入（其檢核過）之前：x 於當下之試算為本街廓之他歸戶之已配得之宗（BA 之 O1(1)）之成員 ⇒ "
              "停機（程式自我檢查·K-9-57 ⑧）",
         lambda: _k40(),
         ("停機", True))
    return out


def _k32(W):
    def one(q_owner, cap):
        r = _go(W, own_upd={"Q1": q_owner, "C1": "gC1", "E1": "g1", "E9": "gE"}, geom_upd={"Q1(1)": _R(0, 8, 0, 30)},
                cap=cap, rm=("R1(1)", "P1(1)"), blk_upd={"BE": H},
                extra=[_tp("E9(1)", "BE", H, _R(10, 20, 30, 40), 100), _tp("E1(1)", "BE", H, _R(10, 20, 40, 50), 500)])
        return [x for x in _rows(r) if x[0] == "K-9-51"]
    # 🔧 `W-G.9-373`：本街廓之宗之不容以 BA 之容量 0 造之（受併之累加唯計正值）
    return one("g1", {"BB": 10.0}), one("gQ", {"BB": 10.0}), one("g1", {"BB": 10.0, "BA": 0.0})


def _w2(a1_adjacent=True):
    """世界二（K33）：BA x∈[0,30]、BB x∈[30,60]、BC x∈[60,90]、BD x∈[90,120]（y∈[0,30]）。地主 g1 之 X(1)〔BA·[20,30]·
    分不到〕與 BB 之 B1(1) 相接（跨分配線·BB 之容量小 ⇒ 不過）；Y(1)〔BC·[75,90]·分不到·面積大 ⇒ 先〕併入 BD 之 D1(1)；
    A1(1)〔BA〕於 Y(1) 併出之後始為已配得（玩具之回呼以之造「C0 之後始為已配得」）。"""
    a1, o1 = ((10, 20), (0, 10)) if a1_adjacent else ((0, 10), (10, 20))
    t = [_tp("A1(1)", "BA", H, _R(a1[0], a1[1], 0, 30), 300), _tp("O1(1)", "BA", H, _R(o1[0], o1[1], 0, 30), 300),
         _tp("X(1)", "BA", H, _R(20, 30, 0, 30), 300), _tp("B1(1)", "BB", H, _R(30, 40, 0, 30), 300),
         _tp("B9(1)", "BB", H, _R(40, 60, 0, 30), 300), _tp("C9(1)", "BC", H, _R(60, 75, 0, 30), 300),
         _tp("Y(1)", "BC", H, _R(75, 90, 0, 30), 450), _tp("D1(1)", "BD", H, _R(90, 100, 0, 30), 300),
         _tp("D9(1)", "BD", H, _R(100, 120, 0, 30), 300)]
    own = {"A1": "g1", "O1": "gO", "X": "g1", "B1": "g1", "B9": "gB", "C9": "gC", "Y": "g1", "D1": "g1", "D9": "gD"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BC", "BD")}
    return t, own, blocks


def _k33():
    def one(adj):
        t, own, blocks = _w2(adj)
        build = list(t)
        ap, st = _cbs(cap={"BB": 10.0}, drop=("X(1)", "Y(1)"))

        def st2(temp, build_):
            r = st(temp, build_)
            if "Y(1)" in {b["暫編地號"] for b in build_}:          # Y(1) 併出之前 ⇒ A1(1) 尚非已配得
                r = dict(r, kept={k: set(v) - {"A1(1)"} for k, v in r["kept"].items()})
            return r
        return _NS["fn"](t, build, own, blocks, {}, ap, st2, log_print=lambda *x: None), t, build
    return (_halt2(lambda: one(True), ("入池閘之射程", "K-9-55")),
            [x for x in _rows(one(False)) if x[0] == "K-9-51"])


# 🔧 補令三（⛔ 上列一字不刪）
def _w3(extra=()):
    """世界三（K34〜K36）：BA x∈[0,30]、BB x∈[30,60]、BC x∈[60,90]、BD x∈[90,120]（y∈[0,30]）；BA 另可有 y∈[30,40] 之片
    （extra）。地主 g1 之 X(1)〔BA·[20,30]·分不到〕與 BB 之 B1(1) 相接（跨分配線·BB 之容量小 ⇒ 不過 ⇒ K-9-51）；
    O1(1)〔BA·[10,20]·他地主〕隔 A1(1)〔BA·[0,10]·g1·已配得〕與 X(1)；Y(1)〔BC·[75,90]·分不到·面積大 ⇒ 先〕併入 BD 之
    D1(1)。M1(1) ⛔ 入 build（唯 temp）；H2(1) 入 build 而現態⛔ 保留。"""
    t = [_tp("A1(1)", "BA", H, _R(0, 10, 0, 30), 300), _tp("O1(1)", "BA", H, _R(10, 20, 0, 30), 300),
         _tp("X(1)", "BA", H, _R(20, 30, 0, 30), 300), _tp("B1(1)", "BB", H, _R(30, 40, 0, 30), 300),
         _tp("B9(1)", "BB", H, _R(40, 60, 0, 30), 300), _tp("C9(1)", "BC", H, _R(60, 75, 0, 30), 300),
         _tp("Y(1)", "BC", H, _R(75, 90, 0, 30), 450), _tp("D1(1)", "BD", H, _R(90, 100, 0, 30), 300),
         _tp("D9(1)", "BD", H, _R(100, 120, 0, 30), 300)] + [copy.deepcopy(e) for e in extra]
    own = {"A1": "g1", "O1": "gO", "X": "g1", "B1": "g1", "B9": "gB", "C9": "gC", "Y": "g1", "D1": "g1", "D9": "gD",
           "M1": "g1", "H2": "g1"}
    blocks = {b: {"category": H} for b in ("BA", "BB", "BC", "BD")}
    return t, own, blocks


def _go3(extra, after):
    """玩具之回呼：Y(1) 併出之後之試算以 after(r) 改之（造「C0 之後」之態·其前 ＝ 現態）。"""
    t, own, blocks = _w3(extra)
    build = [x for x in t if x["暫編地號"] != "M1(1)"]
    ap, st = _cbs(cap={"BB": 10.0}, drop=("X(1)", "Y(1)", "H2(1)"))

    def st3(temp, build_):
        r = st(temp, build_)
        if "Y(1)" not in {b["暫編地號"] for b in build_}:
            r = after(r)
        return r
    return _NS["fn"](t, build, own, blocks, {}, ap, st3, log_print=lambda *x: None), t, build


def _k34():
    def one(m1x):
        def after(r):
            return dict(r, members=dict(r["members"], **{"A1(1)": ["A1(1)", "M1(1)"]}))
        return _go3([_tp("M1(1)", "BA", H, _R(m1x[0], m1x[1], 30, 40), 100)], after)
    return (_halt2(lambda: one((20, 30)), ("入池閘之射程", "K-9-55")),
            [x for x in _rows(one((0, 10))) if x[0] == "K-9-51"], _k34s())


def _k34s():
    """C0 之 members 載 H2(1)〔現態⛔ 保留〕之舊單元 [H2(1), M1(1)]（M1 與 x 相接）；Y(1) 併出之後 H2(1) 始為已配得、
    其單元唯 [H2(1)]（H2 ＝ [10,20]×[30,40]·⛔ 與 x 相接）⇒ ⛔ 停機；本街廓之候選 A1(1)〔G 300〕、H2(1)〔G 100〕⇒ 併入 A1。"""
    t, own, blocks = _w3([_tp("H2(1)", "BA", H, _R(10, 20, 30, 40), 100),
                          _tp("M1(1)", "BA", H, _R(20, 30, 30, 40), 100)])
    build = [x for x in t if x["暫編地號"] != "M1(1)"]
    ap, st = _cbs(cap={"BB": 10.0}, drop=("X(1)", "Y(1)", "H2(1)"))

    def st4(temp, build_):
        r = st(temp, build_)
        if "Y(1)" in {b["暫編地號"] for b in build_}:
            return dict(r, members=dict(r["members"], **{"H2(1)": ["H2(1)", "M1(1)"]}))
        k = {b: set(v) for b, v in r["kept"].items()}
        k.setdefault("BA", set()).add("H2(1)")
        return dict(r, kept=k, G=dict(r["G"], **{"H2(1)": 100.0}), members=dict(r["members"], **{"H2(1)": ["H2(1)"]}))
    res = _NS["fn"](t, build, own, blocks, {}, ap, st4, log_print=lambda *x: None), t, build
    return [x for x in _rows(res) if x[0] == "K-9-51"]


def _k35():
    def one(h2x):
        def after(r):
            k = {b: set(v) for b, v in r["kept"].items()}
            k.setdefault("BA", set()).add("H2(1)")
            return dict(r, kept=k, G=dict(r["G"], **{"H2(1)": 100.0}), members=dict(r["members"], **{"H2(1)": ["H2(1)"]}))
        return _go3([_tp("H2(1)", "BA", H, _R(h2x[0], h2x[1], 30, 40), 100)], after)
    return (_halt2(lambda: one((20, 30)), ("入池閘之射程", "K-9-55")),
            [x for x in _rows(one((10, 20))) if x[0] == "K-9-51"])


def _k36():
    def one(mode):
        def after(r):
            if mode == "kept":
                k = {b: set(v) for b, v in r["kept"].items()}
                k.setdefault("BA", set()).add("X(1)")
                return dict(r, kept=k, G=dict(r["G"], **{"X(1)": 300.0}), members=dict(r["members"], **{"X(1)": ["X(1)"]}))
            if mode == "member":
                return dict(r, members=dict(r["members"], **{"A1(1)": ["A1(1)", "X(1)"]}))
            return r
        return _go3((), after)
    return (_halt2(lambda: one("kept"), S219_PH), _halt2(lambda: one("member"), S219_PH),
            [x for x in _rows(one("none")) if x[0] == "K-9-51"])


# 🔧 補令四（⛔ 上列一字不刪）
def _go4(extra, after, before=None):
    """世界三之變（K37／K38）：BB 之容量⛔ 設 ⇒ X(1) 之主併入（B1(1)）之檢核過。玩具之回呼：Y(1) 併出之前之試算以
    before(r) 改之（缺 ⇒ 不改）；Y(1) 併出之後之試算，BB 之配餘地不合格一處（Y(1) 之檢核之 T ＝ {BD, BC} 不及之 ⇒ Y(1)
    成；整批之 T 含 BB 而現態為 0 ⇒ 整批不過 ⇒ 逐片；X(1) 之主併入之前後皆 1 ⇒ ⛔ 增），再以 after(r) 改之（造
    「C0 之後」之態）。"""
    t, own, blocks = _w3(extra)
    build = [x for x in t if x["暫編地號"] != "M1(1)"]
    ap, st = _cbs(drop=("X(1)", "Y(1)", "H2(1)"))

    def st5(temp, build_):
        r = st(temp, build_)
        if "Y(1)" in {b["暫編地號"] for b in build_}:
            return before(r) if before else r
        return after(dict(r, bad_pools=dict(r["bad_pools"], BB=1)))
    return _NS["fn"](t, build, own, blocks, {}, ap, st5, log_print=lambda *x: None), t, build


def _k37():
    def one(mode):
        def after(r):
            if mode == "kept":
                k = {b: set(v) for b, v in r["kept"].items()}
                k.setdefault("BA", set()).add("X(1)")
                return dict(r, kept=k, G=dict(r["G"], **{"X(1)": 300.0}), members=dict(r["members"], **{"X(1)": ["X(1)"]}))
            if mode == "member":
                return dict(r, members=dict(r["members"], **{"A1(1)": ["A1(1)", "X(1)"]}))
            return r
        return _go4((), after)
    return (_halt2(lambda: one("kept"), S219_PH), _halt2(lambda: one("member"), S219_PH),
            _sel(one("none"), "X(1)"))


def _k38():
    def h2(h2x):
        def after(r):
            k = {b: set(v) for b, v in r["kept"].items()}
            k.setdefault("BA", set()).add("H2(1)")
            return dict(r, kept=k, G=dict(r["G"], **{"H2(1)": 100.0}), members=dict(r["members"], **{"H2(1)": ["H2(1)"]}))
        return _go4([_tp("H2(1)", "BA", H, _R(h2x[0], h2x[1], 30, 40), 100)], after)

    def m1():
        def after(r):
            return dict(r, members=dict(r["members"], **{"A1(1)": ["A1(1)", "M1(1)"]}))
        return _go4([_tp("M1(1)", "BA", H, _R(20, 30, 30, 40), 100)], after)

    def old():
        def before(r):
            return dict(r, members=dict(r["members"], **{"H2(1)": ["H2(1)", "M1(1)"]}))

        def after(r):
            k = {b: set(v) for b, v in r["kept"].items()}
            k.setdefault("BA", set()).add("H2(1)")
            return dict(r, kept=k, G=dict(r["G"], **{"H2(1)": 100.0}), members=dict(r["members"], **{"H2(1)": ["H2(1)"]}))
        return _go4([_tp("H2(1)", "BA", H, _R(10, 20, 30, 40), 100), _tp("M1(1)", "BA", H, _R(20, 30, 30, 40), 100)],
                    after, before)
    return (_halt2(lambda: h2((20, 30)), ("入池閘之射程", "R-6 (a)")), _halt2(m1, ("入池閘之射程", "R-6 (a)")),
            _sel(h2((10, 20)), "X(1)"), _sel(old(), "X(1)"))


# 🔧 W-G.9-364（⛔ 上列一字不刪）
def _mem4(host):
    """世界三之變（_go4）：Y(1) 併出之後之試算，已配得之宗 host 之成員增 X(1)（造「C0 之後」之態）。"""
    def after(r):
        return dict(r, members=dict(r["members"], **{host: [host, "X(1)"]}))
    return _go4((), after)


def _k39():
    ph = S219_PH
    return (_halt2(lambda: _mem4("D1(1)"), ph), _halt2(lambda: _mem4("D9(1)"), ph))


def _k40():
    return _halt2(lambda: _mem4("O1(1)"), S219_PH)


def _k28(W):
    kw = dict(own_upd={"Q1": "g1", "C1": "gC1"}, geom_upd={"Q1(1)": _R(0, 8, 0, 30)}, rm=("R1(1)", "P1(1)"))
    r = _go(W, cap={"BB": 10.0}, **kw)
    # 🔧 `W-G.9-373`：本街廓之宗之不容以 BA 之容量 0 造之（受併之累加唯計正值）
    return (_rows(r), "X1(1)" in [b["暫編地號"] for b in r[0][1]], _rows(_go(W, cap={"BB": 10.0, "BA": 0.0}, **kw)))


def _halt2(fn, phrases):
    try:
        fn()
    except RuntimeError as e:
        return ("停機", all(p in str(e) for p in phrases))
    return ("無停機",)


class _FakeSt:
    """畫面之假 st：`session_state` ＝ dict；方法之呼叫依序記其名（`error`／`stop`／其他）。"""

    def __init__(self):
        self.session_state = {}
        self.calls = []

    def error(self, *a, **k):
        self.calls.append("error")

    def stop(self):
        self.calls.append("stop")

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)

        def _f(*a, **k):
            self.calls.append(name)
            return contextlib.nullcontext()
        return _f


def _setenv2(v953, v9296):
    for k, v in (("WV_K953", v953), ("WV_K929_6", v9296)):
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


def _k29(ns, sp):
    keep = (os.environ.get("WV_K953"), os.environ.get("WV_K929_6"))
    t, own, blocks, cl = _w1()
    b = [x for x in t if x["街廓分類"] == H]
    out = []
    try:
        _setenv2(None, "off")
        fst = _FakeSt()
        r = sp.run_k953(ns, fst, None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None, forced=None)
        out.append((r[0] is t, r[1] is b, fst.session_state.get("f3_k953_log")))
        _setenv2("off", "maybe")
        try:
            sp.run_k953(ns, _FakeSt(), None, None, None, t, b, 0.0, snapshot=None, callbacks=None, winners=None,
                        forced=None)
            out.append("無停機")
        except RuntimeError:
            out.append("停機")
        _setenv2(None, "off")
        st = _FakeSt()
        rr = ns["f3_screen_k953"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={})
        out.append((rr["temp"] is t, rr["build"] is b, rr["log"], st.session_state.get("f3_k953_log"), st.calls))
    finally:
        _setenv2(*keep)
    return tuple(out)


def _k30(ns):
    keep = (os.environ.get("WV_K953"), os.environ.get("WV_K929_6"))
    t, own, blocks, cl = _w1()
    b = [x for x in t if x["街廓分類"] == H]
    out = []
    try:
        for v953, v9296 in (("maybe", None), (None, "maybe")):
            _setenv2(v953, v9296)
            st = _FakeSt()
            st.session_state["f3_k6b_stage3_error"] = "前之標記"
            try:
                ns["f3_screen_k953"](st, pk_kwargs={"temp_parcels": t, "build_parcels": b}, g_kwargs={})
                how = "無停機"
            except RuntimeError:
                how = "停機"
            except Exception as e:  # noqa: BLE001
                how = type(e).__name__
            out.append((how, st.calls, str(st.session_state.get("f3_k6b_stage3_error", "")).startswith("（手冊先行）"),
                        "f3_k953_log" in st.session_state))
    finally:
        _setenv2(*keep)
    return tuple(out)


def _k31(W):
    r = _go(W, units={"X1(2)": ["X1(2)", "Y1(1)"]}, own_upd={"Y1": "g1"})
    t2, b2, _log = r[0]
    ids = {id(x) for x in t2}
    ht = [x for x in t2 if x["暫編地號"] == "X1(2)"]
    hb = [x for x in b2 if x["暫編地號"] == "X1(2)"]
    return (all(id(x) in ids for x in b2), len(ht), bool(ht and hb and ht[0] is hb[0]),
            (ht[0].get("入池閘併入") if ht else None), "Y1(1)" in [x["暫編地號"] for x in t2],
            "Y1(1)" in [x["暫編地號"] for x in b2])


def _k13(W):
    # BC 之 C9(1)〔x∈[0,20]〕、C1(1)〔[20,30]〕、C8(1)〔[30,60]〕皆 g1 之已配得；BB 無 ⇒ 道路片唯一側有 ⇒ 整筆依瀑布
    def recv(pid, **kw):
        kw.setdefault("own_upd", {})
        kw["own_upd"] = dict({"C9": "g1", "C8": "g1"}, **kw["own_upd"])
        r = _go(W, drop=(), rm=("X1(1)", "X1(2)", "P1(1)") + tuple(kw.pop("rm", ())), **kw)
        rr = _sel(r, pid)
        return rr[0][3] if rr else None
    a = recv("C8(2)", rm=("R1(1)",), extra=[_tp("C8(2)", "RD", RDC, _R(20, 30, -10, 0), 100)])
    b = recv("R1(1)")
    c = recv("R1(1)", rm=("C1(1)",), geom_upd={"C8(1)": _R(30, 50, -40, -10)}, gmap={"C9(1)": 900.0})
    d = recv("R1(1)", rm=("C1(1)",), geom_upd={"C8(1)": _R(30, 50, -40, -10)})
    return a, b, c, d


def _unit_rows(res):
    return [(r["片"], r["結果"]) for r in res[0][2] if r.get("序") == "單元"]


def _k20(ns, W):
    res = _go(W, own_upd={"C1": "gC1"}, rm=("Z1(1)",), cap={"BB": 160.0})
    t2, b2, log = res[0]
    bur = {"BA": "可建築土地", "BB": "可建築土地", "BD": "可建築土地", "BC": "可建築土地", "RD": "共同負擔",
           "PK": "共同負擔"}
    own = {"X1": "g1", "Y1": "gY", "Z1": "gZ", "Q1": "gQ", "Q2": "gQ2", "R1": "g1", "R9": "gR", "R8": "gR8",
           "C1": "gC1", "C9": "gC", "C8": "gC8", "P1": "g1", "P9": "gP"}
    rows = [{"暫編地號": b["暫編地號"], "推進側別": "left", "G(㎡)": _a(b)} for b in b2]
    it = ns["adj_intake"](t2, b2, rows, {}, own, bur)
    sl = {s["暫編地號"]: s for s in it["slices"]}
    return (sl["X1(1)"]["類"], sl["X1(1)"]["所屬單元"], sl["P1(1)"]["類"], len(it["step4"]))


def _k21(sp):
    t = [{"暫編地號": "Q", "分攤登記面積_m2": 10.0, "面積_m2": 0.0},
         {"暫編地號": "W", "分攤登記面積_m2": 10.0, "面積_m2": 0.0, "段三併出": ["X"]},
         {"暫編地號": "R", "分攤登記面積_m2": 50.0, "面積_m2": 0.0, "段三併出": ["X"], "段三餘量": 25.0}]
    out = sp.k6b_stage3_pool_temp(t)
    return ([x["暫編地號"] for x in out], round(out[1]["分攤登記面積_m2"], 2))


def _k25(W):
    t, own, blocks, cl = W()
    build = [x for x in t if x["街廓分類"] == H]
    n = [0]

    def st(temp, build_):
        n[0] += 1
        raise AssertionError("alloc_state 被呼叫")
    r = _NS["fn"](t, build, {}, blocks, cl, lambda a, b: 0.0, st, log_print=lambda *x: None)
    return (r[0] is t, r[1] is build, r[2], n[0])


def _k26(ns):
    sq = lambda w: [(0, 0), (w, 0), (w, w), (0, w)]  # noqa: E731
    r = ns["k953_alloc_summary"](
        [{"所屬街廓": "B1", "暫編地號": "B1-抵費地-1", "cut_coords": sq(1)},
         {"所屬街廓": "B1", "暫編地號": "B1-抵費地-2", "cut_coords": sq(50)},
         {"所屬街廓": "B1", "暫編地號": "A(1)", "驗_總判": "保留", "G(㎡)": 123.4},
         {"所屬街廓": "B1", "暫編地號": "C(1)", "驗_總判": "不配地", "G(㎡)": 5.0},
         {"所屬街廓": "B2", "暫編地號": "B2-抵費地-1", "cut_coords": "—"}],
        {"B1": H}, {"B1": {"正面路寬(m)": 8.0}})
    return ({k: sorted(v) for k, v in r["kept"].items()}, r["bad_pools"], r["G"])


def _k27(ns):
    b = [{"暫編地號": "A(1)", "入池閘併入": ["A(1)", "A(2)"]}, {"暫編地號": "B(1)"}]
    m, u = ns["k953_units_of"](b)
    return (m, sorted(u), u["A(1)"] is b[0])


def _k24(ns):
    env = os.environ.get("WV_K953")
    res = []
    try:
        for v in (None, "on", "off"):
            if v is None:
                os.environ.pop("WV_K953", None)
            else:
                os.environ["WV_K953"] = v
            res.append(ns["k953_enabled"]())
        os.environ["WV_K953"] = "maybe"
        try:
            ns["k953_enabled"]()
            res.append("無停機")
        except RuntimeError:
            res.append("停機")
    finally:
        if env is None:
            os.environ.pop("WV_K953", None)
        else:
            os.environ["WV_K953"] = env
    return tuple(res)


def _perturb(v):
    if isinstance(v, bool):
        return not v
    if isinstance(v, (int, float)):
        return v + 1
    if isinstance(v, str):
        return v + "′"
    if isinstance(v, tuple):
        return (v + ("′",)) if not v else (_perturb(v[0]),) + v[1:]
    if isinstance(v, list):
        return v + ["′"]
    if isinstance(v, dict):
        return dict(v, **{"′": 0})
    return ("′", v)


def selftest(repo):
    ns, _ = _harvest(repo)
    import selection_pipeline as sp
    need = [n for n in (FN, "k953_enabled", "k953_alloc_summary", "k953_units_of", "adj_intake", "f3_screen_k953",
                        "k929_6_enabled") if n not in ns]
    if need or not hasattr(sp, "k6b_stage3_pool_temp") or not hasattr(sp, "run_k953"):
        print(f"  🔴 受詞缺：{need}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    cases = _cases(ns, sp)
    print("── 手冊先行（K-9-53 ①）之各支 ──")
    red = _report(cases)
    print("── P0 判式自驗（逐項擾動其期 ⇒ 恰該項紅）──")
    hits = 0
    for i in range(len(cases)):
        pert = [(n, g, (_perturb(e) if j == i else e)) for j, (n, g, e) in enumerate(cases)]
        r = _report(pert, verbose=False)
        base = set(red)
        code = cases[i][0].split()[0]
        if (set(r) - base) == {code} or (code in base and set(r) == base):
            hits += 1
    ok0 = hits == len(cases)
    print(("  ✅" if ok0 else "  🔴") + f" P0 逐項擾動恰該項紅 {hits}／{len(cases)}")
    if not ok0:
        red.append("P0")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── wiring ──
CASE_LIT_RE = re.compile(r"^(R\d+|RD\d+|G\d+|G0\d\d|\d{3}(-\d+)?(\(\d+\))?|left|right|左|右|住宅區|商業區)$")


def _git_show(repo, rev, rel):
    return subprocess.run(["git", "-C", repo, "show", f"{rev}:{rel}"], capture_output=True, check=True).stdout.decode("utf-8")


def _defs(src):
    tree = ast.parse(src)
    return {n.name: n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}, tree


def _seg(src, node):
    return ast.get_source_segment(src, node) or ""


def _calls(node):
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            f = n.func
            nm = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)
            if isinstance(f, ast.Subscript) and isinstance(f.slice, ast.Constant):
                nm = str(f.slice.value)
            out.append((nm, n.lineno, n.col_offset, n))
    return sorted(out, key=lambda x: (x[1], x[2]))


def _wiring_checks(repo, base):
    chk = []
    app = open(os.path.join(repo, "app.py"), encoding="utf-8").read()
    spp = open(os.path.join(repo, "verify", "selection_pipeline.py"), encoding="utf-8").read()
    ad, atree = _defs(app)
    sd, stree = _defs(spp)
    # W1 新名與簽名
    f = ad.get(FN)
    ok = f is not None and [a.arg for a in f.args.args] == SIG and [a.arg for a in f.args.kwonlyargs] == ["log_print"]
    consts = {}
    for n in atree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) \
                and isinstance(n.value, ast.Constant):
            consts.setdefault(n.targets[0].id, []).append(n.value.value)
    fsig = {nm: ([a.arg for a in ad[nm].args.args] if nm in ad else None) for nm in NEW_FNS}
    okc = consts.get("K953_ENV") == ["WV_K953"] and fsig == NEW_FNS
    chk.append(("W1 模組層之新名與簽名（k953_manual_run·k953_enabled·k953_alloc_summary·k953_units_of·f3_screen_k953·"
                "K953_ENV）", ok and okc, f"k953_manual_run {ok}／其餘 {okc}"))
    # W2 harness 之入口與序
    rk = sd.get("run_k953")
    crk = _calls(rk) if rk is not None else []
    okr = (rk is not None and [a.arg for a in rk.args.args] == RK_SIG
           and [a.arg for a in rk.args.kwonlyargs] == RK_KW
           and sum(1 for c in crk if c[0] == FN) == 1
           and all(any(c[0] == nm for c in crk) for nm in ("k953_alloc_summary", "k953_units_of", "k953_enabled"))
           and not any(c[0] in ("run_corner_pk", "run_corner_pk_k6b") for c in crk))
    pk = sd.get("run_corner_pk_k6b")
    cs = _calls(pk) if pk is not None else []
    i_end = max([c[1] for c in cs if c[0] == "run_end_block_merge"], default=-1)
    i_k = [c for c in cs if c[0] == "run_k953"]
    i_pk_after = [c for c in cs if c[0] == "run_corner_pk" and i_k and c[1] > i_k[0][1]]
    okw = (len(i_k) == 1 and i_k[0][1] > i_end > 0 and not i_pk_after
           and {k.arg for k in i_k[0][3].keywords} >= {"winners", "forced", "callbacks", "snapshot"})
    chk.append(("W2 harness：run_k953（簽名）恰一處呼叫 k953_manual_run、以 k953_alloc_summary／k953_units_of 摘要試算、"
                "⛔ 呼叫街角選位；run_corner_pk_k6b 恰一處呼叫 run_k953、於末端塊合併再試之後、其後⛔ 再呼叫 run_corner_pk",
                okr and okw, f"入口 {okr}／序 {okw}"))
    # W3 畫面之入口
    fs = ad.get("f3_screen_k953")
    cfs = _calls(fs) if fs is not None else []
    ok3 = (fs is not None and [a.arg for a in fs.args.args] == ["st"]
           and [a.arg for a in fs.args.kwonlyargs] == ["pk_kwargs", "g_kwargs"]
           and sum(1 for c in cfs if c[0] == FN) == 1
           and all(any(c[0] == nm for c in cfs) for nm in ("k953_alloc_summary", "k953_units_of", "k953_enabled",
                                                          "f3_screen_stepg_run", "k6b_screen_callbacks"))
           and not any(c[0] in ("f3_screen_corner_pk_run", "f3_screen_k6b_stage3") for c in cfs))
    chk.append(("W3 畫面：f3_screen_k953（簽名）恰一處呼叫 k953_manual_run、以 f3_screen_stepg_run 試算並以 "
                "k953_alloc_summary／k953_units_of 摘要、⛔ 呼叫街角選位", ok3, ""))
    # W4 畫面之序
    s5n = ad.get("f3_screen_k6b_stage3")
    c5 = _calls(s5n) if s5n is not None else []
    i5e = [c[1] for c in c5 if c[0] == "f3_screen_end_block_merge"]
    i5k = [c[1] for c in c5 if c[0] == "f3_screen_k953"]
    ok4 = len(i5e) == 1 and len(i5k) == 1 and i5k[0] > i5e[0]
    chk.append(("W4 畫面：f3_screen_k6b_stage3 恰一處呼叫 f3_screen_k953、於 f3_screen_end_block_merge 之後", ok4, ""))
    # W5 新碼⛔ 案件字面
    lits = []
    for nm in NEW_FNS:
        n = ad.get(nm)
        if n is None:
            continue
        for x in ast.walk(n):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
                lits.append((nm, x.value))
    for x in ast.walk(rk) if rk is not None else []:
        if isinstance(x, ast.Constant) and isinstance(x.value, str) and CASE_LIT_RE.match(x.value):
            lits.append(("run_k953", x.value))
    chk.append(("W5 新碼⛔ 案件字面", not lits, str(lits)))
    try:
        bapp = _git_show(repo, base, "app.py")
        bsp = _git_show(repo, base, "verify/selection_pipeline.py")
    except Exception as e:  # noqa: BLE001
        chk.append(("W6 既有函式對基準一字未動", False, f"基準讀不到：{type(e).__name__}"))
        return chk
    # W6 既有函式對基準一字未動
    bd, _ = _defs(bapp)
    bsd, _ = _defs(bsp)
    same = [(nm, ad.get(nm) is not None and bd.get(nm) is not None and ast.dump(ad[nm]) == ast.dump(bd[nm]))
            for nm in KEEP_APP]
    same += [(nm, sd.get(nm) is not None and bsd.get(nm) is not None and ast.dump(sd[nm]) == ast.dump(bsd[nm]))
             for nm in KEEP_SP]
    bad = [n for n, s_ in same if not s_]
    chk.append(("W6 既有函式對基準一字未動（段三、末端塊合併再試、地籍相連、入池閘、二回呼、調配之輸入、公設地調配之 temp、"
                "main 等）", not bad, f"相異 {bad}"))
    # W7 頂層之相異 ⊆ 本單之許
    for nm_, cur_, old_, allow_ in (("app.py", atree, ast.parse(bapp), APP_ALLOW),
                                    ("verify/selection_pipeline.py", stree, ast.parse(bsp), SP_ALLOW)):
        a_, b_ = _top_dump(cur_), _top_dump(old_)
        diff = sorted(k for k in set(a_) | set(b_) if a_.get(k) != b_.get(k))
        chk.append((f"W7 {nm_} 之頂層節點對基準相異者 ⊆ 本單之許", set(diff) <= allow_,
                    f"相異 {diff}；逾 {sorted(set(diff) - allow_)}"))
    # W8 既有量測器之錨（其字串常數於基準恰一見者）於工作樹仍恰一見（新碼⛔ 複製錨、⛔ 去錨）
    lits8 = set()
    pdir = os.path.join(repo, "verify", "probes")
    for p8 in sorted(os.listdir(pdir)):
        if not p8.endswith(".py") or p8 == SELF_NAME:
            continue
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                t8 = ast.parse(open(os.path.join(pdir, p8), encoding="utf-8").read())
        except Exception:  # noqa: BLE001
            continue
        for x in ast.walk(t8):
            if isinstance(x, ast.Constant) and isinstance(x.value, str) and len(x.value) >= 4:
                lits8.add(x.value)
    for nm_, cur_s, old_s in (("app.py", app, bapp), ("verify/selection_pipeline.py", spp, bsp)):
        anc = [x for x in lits8 if old_s.count(x) == 1 and x not in ANC_SKIP373]
        moved = sorted((x[:60], cur_s.count(x)) for x in anc if cur_s.count(x) != 1)
        fb, fc = _fn_names(old_s), _fn_names(cur_s)
        dup = sorted((k, fc.get(k, 0)) for k, v in fb.items() if v == 1 and fc.get(k, 0) != 1
                     and not (k in FN_GONE373 and fc.get(k, 0) == 0))
        chk.append((f"W8 {nm_}：既有量測器之錨（{len(anc)}）於工作樹皆恰一見；基準中恰一之函式名（含巢狀·"
                    f"{sum(1 for v in fb.values() if v == 1)}）仍恰一", not moved and not dup,
                    f"錨之異 {moved[:6]}；函式名之異 {dup[:8]}"))
    return chk


def _fn_names(src):
    out = {}
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[n.name] = out.get(n.name, 0) + 1
    return out


SELF_NAME = "probe_WG9363_k953.py"
NEW_FNS = {"k953_enabled": [], FN: SIG, "k953_alloc_summary": ["g_rows", "cat_of", "front_rows"],
           "k953_units_of": ["build_final"], "f3_screen_k953": ["st"]}
KEEP_APP = ("k6b_stage3_run", "end_block_merge_run", "k6_shares_segment", "k6_merge_groups", "k929_6_fixpoint",
            "adj_intake", "adj_candidate_lists", "adj_block_ctx", "adj_pool_anchor", "f3_screen_end_block_merge",
            "k6b_screen_callbacks", "f3_screen_stepg_run", "f3_screen_corner_pk_run", "_k929_6_screen_gate", "main")
KEEP_SP = ("run_end_block_merge", "run_corner_pk", "_k6b_callbacks", "k6b_stage3_pool_temp")
# 🔧 `W-G.9-373`（`K-9-66`／`K-9-67`／`K-9-68`）：本單所改之六函式出 W6 之受詞（其接線另由 F27 量之）
CHG373_APP = ("k6b_stage3_run", "k929_6_fixpoint", "adj_intake", "k6b_screen_callbacks", "k953_manual_run",
              "adj4_pass1_run")
CHG373_SP = ("_k6b_callbacks", "k6b_stage3_pool_temp")
NEW373_APP = ("K966_CLASSES", "K966_GRID", "k966_block_merge", "k967_rank", "k967_pre_area")
KEEP_APP = tuple(x for x in KEEP_APP if x not in CHG373_APP)
KEEP_SP = tuple(x for x in KEEP_SP if x not in CHG373_SP)
# 🔧 `W-G.9-373`：W8 之錨⛔ 計者（本單之生產碼必增其見：`k6b_stage3_pool_temp` 之建地之部分併出原樣入之、
#   二 `alloc_state` 之回傳增 `members`）；W8 之函式名許為 0 者（本單所去之巢狀 def）
ANC_SKIP373 = ("_out.append(tp)", "member", "members")
FN_GONE373 = ("_k951", "_max357", "_split357", "_try", "_fill953", "_probe953", "_remain953")
APP_ALLOW = {"K953_ENV", "k953_enabled", "k953_alloc_summary", "k953_units_of", FN, "f3_screen_k953",
             "f3_screen_k6b_stage3"}
SP_ALLOW = {"run_k953", "run_corner_pk_k6b"}
# 🔧 `W-G.9-367`（發單側窗六十八）：規格步 4 乙之新名亦許（本批之頂層之限另由 F24 之 W5 量之）
APP_ALLOW |= {"ADJ4_ENV", "ADJ4_IDENT_UNUSED", "adj4_enabled", "adj4_possible", "adj4_subject_units", "adj4_subjects",
              "adj4_depth_of", "adj4_trial_state", "adj4_plan", "adj4_pass1_run", "f3_screen_adj4"}
SP_ALLOW |= {"run_adj4"}
# 🔧 `W-G.9-373`：本單之新名與所改者亦許（本單之頂層之限另由 F27 之 wiring 量之）
APP_ALLOW |= set(NEW373_APP) | set(CHG373_APP)
SP_ALLOW |= set(CHG373_SP)


def _top_dump(tree):
    out = {}
    for i, n in enumerate(tree.body):
        if isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
            k = n.name
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            k = n.targets[0].id
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            k = n.target.id
        else:
            k = f"<{type(n).__name__}>"
        out.setdefault(k, []).append(ast.dump(n))
    return out



def wiring(repo, base):
    chk = _wiring_checks(repo, base)
    red = []
    for name, ok, note in chk:
        print(("  ✅ " if ok else "  🔴 ") + name + (f"（{note}）" if note else ""))
        if not ok:
            red.append(name.split()[0])
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：本案（harness）──
# 手冊先行之紀錄（序 ＝ 單元／整批／手冊／K-9-51）之 (序, 片, 類, 受併宗, ((受併宗, 併入量 2 位)…), 結果)
#   ——發單側窗六十四之原型實跑（態 7d8e954 ＋ 原型·harness）
R1_EXPECT = {
    3.5: [
        ('單元', '628-21(1)', '—', '—', (), '未取代（取代後之配地相異）'),
        ('單元', '628-40(1)', '—', '—', (), '取代'),
        ('單元', '628-47(1)', '—', '—', (), '取代'),
        ('整批', '29 片', '—', '—', (), '成'),
        ('手冊', '628(3)', 'a', '628(1)', (('628(1)', 236.68),), '成'),
        ('手冊', '628-1(2)', 'a', '628-1(1)', (('628-1(1)', 227.41),), '成'),
        ('手冊', '628-34(3)', 'a', '628-34(1)', (('628-34(1)', 152.34),), '成'),
        ('手冊', '628-49(1)', 'a', '628-47(1)', (('628-47(1)', 109.39),), '成'),
        ('手冊', '628-35(1)', 'a', '628-35(2)', (('628-35(2)', 98.54),), '成'),
        ('手冊', '628(4)', 'a', '628(5)', (('628(5)', 71.69),), '成'),
        ('手冊', '628-31(1)', 'a', '628-31(3)', (('628-31(3)', 18.34),), '成'),
        ('手冊', '628(2)', 'a', '628(1)', (('628(1)', 11.49),), '成'),
        ('手冊', '628-32(1)', 'a', '628-32(3)', (('628-32(3)', 5.39),), '成'),
        ('手冊', '628-7(4)', 'b', '628-7(1)', (('628-7(1)', 404.63),), '成'),
        ('手冊', '628(6)', 'b', ('628(1)', '628(5)'), (('628(1)', 170.8), ('628(5)', 170.99)), '成'),
        ('手冊', '628-1(3)', 'b', '628-1(1)', (('628-1(1)', 191.67),), '成'),
        ('手冊', '628-4(2)', 'b', '628-4(1)', (('628-4(1)', 141.0),), '成'),
        ('手冊', '628-32(5)', 'b', '628-32(2)', (('628-32(2)', 132.19),), '成'),
        ('手冊', '628-34(4)', 'b', '628-34(1)', (('628-34(1)', 131.03),), '成'),
        ('手冊', '628-32(4)', 'b', '628-32(3)', (('628-32(3)', 130.17),), '成'),
        ('手冊', '628-31(5)', 'b', '628-31(2)', (('628-31(2)', 122.59),), '成'),
        ('手冊', '628-31(4)', 'b', '628-31(3)', (('628-31(3)', 120.86),), '成'),
        ('手冊', '628-35(3)', 'b', '628-35(2)', (('628-35(2)', 117.46),), '成'),
        ('手冊', '628-43(2)', 'b', '628-40(1)', (('628-40(1)', 108.55),), '成'),
        ('手冊', '628-37(2)', 'b', '628-37(1)', (('628-37(1)', 106.24),), '成'),
        ('手冊', '628-36(2)', 'b', '628-36(1)', (('628-36(1)', 99.03),), '成'),
        ('手冊', '628-18(3)', 'b', '628-18(2)', (('628-18(2)', 96.82),), '成'),
        ('手冊', '628-39(2)', 'b', '628-39(1)', (('628-39(1)', 93.85),), '成'),
        ('手冊', '628-3(1)', 'b', '—', (), '未併'),
        ('手冊', '628-23(3)', 'b', '628-23(2)', (('628-23(2)', 12.11),), '成'),
        ('手冊', '628-44(1)', 'b', '628-40(1)', (('628-40(1)', 3.71),), '成'),
        ('手冊', '628-40(2)', 'b', '628-40(1)', (('628-40(1)', 2.52),), '成'),
        ('手冊', '628-22(3)', 'b', '628-22(2)', (('628-22(2)', 0.68),), '成'),
        ('手冊', '628-7(3)', 'c', ('628-7(1)', '628-7(2)'), (('628-7(1)', 784.36), ('628-7(2)', 784.36)), '成'),
    ],
    0.0: [
        ('單元', '628-20(2)', '—', '—', (), '取代'),
        ('單元', '628-21(1)', '—', '—', (), '未取代（取代後之配地相異）'),
        ('單元', '628-40(1)', '—', '—', (), '取代'),
        ('單元', '628-47(1)', '—', '—', (), '取代'),
        ('整批', '37 片', '—', '—', (), '成'),
        ('手冊', '628(3)', 'a', '628(1)', (('628(1)', 236.68),), '成'),
        ('手冊', '628-1(2)', 'a', '628-1(1)', (('628-1(1)', 227.41),), '成'),
        ('手冊', '628-34(3)', 'a', '628-34(1)', (('628-34(1)', 152.34),), '成'),
        ('手冊', '628-30(2)', 'a', '628-30(3)', (('628-30(3)', 150.3),), '成'),
        ('手冊', '628-49(1)', 'a', '628-47(1)', (('628-47(1)', 109.39),), '成'),
        ('手冊', '628-35(1)', 'a', '628-35(2)', (('628-35(2)', 98.54),), '成'),
        ('手冊', '628(4)', 'a', '628(5)', (('628(5)', 71.69),), '成'),
        ('手冊', '628-31(1)', 'a', '628-31(3)', (('628-31(3)', 18.34),), '成'),
        ('手冊', '628(2)', 'a', '628(1)', (('628(1)', 11.49),), '成'),
        ('手冊', '628-32(1)', 'a', '628-32(3)', (('628-32(3)', 5.39),), '成'),
        ('手冊', '628-7(4)', 'b', '628-7(1)', (('628-7(1)', 404.63),), '成'),
        ('手冊', '628(6)', 'b', ('628(1)', '628(5)'), (('628(1)', 170.8), ('628(5)', 170.99)), '成'),
        ('手冊', '628-45(5)', 'b', ('628-20(2)', '628-45(2)'), (('628-20(2)', 105.03), ('628-45(2)', 101.19)), '成'),
        ('手冊', '628-41(2)', 'b', '628-41(1)', (('628-41(1)', 205.52),), '成'),
        ('手冊', '628-1(3)', 'b', '628-1(1)', (('628-1(1)', 191.67),), '成'),
        ('手冊', '628-4(2)', 'b', '628-4(1)', (('628-4(1)', 141.0),), '成'),
        ('手冊', '628-32(5)', 'b', '628-32(2)', (('628-32(2)', 132.19),), '成'),
        ('手冊', '628-34(4)', 'b', '628-34(1)', (('628-34(1)', 131.03),), '成'),
        ('手冊', '628-32(4)', 'b', '628-32(3)', (('628-32(3)', 130.17),), '成'),
        ('手冊', '628-31(5)', 'b', '628-31(2)', (('628-31(2)', 122.59),), '成'),
        ('手冊', '628-31(4)', 'b', '628-31(3)', (('628-31(3)', 120.86),), '成'),
        ('手冊', '628-35(3)', 'b', '628-35(2)', (('628-35(2)', 117.46),), '成'),
        ('手冊', '628-43(2)', 'b', '628-40(1)', (('628-40(1)', 108.55),), '成'),
        ('手冊', '628-37(2)', 'b', '628-37(1)', (('628-37(1)', 106.24),), '成'),
        ('手冊', '628-30(4)', 'b', ('628-20(2)', '628-30(3)'), (('628-20(2)', 48.76), ('628-30(3)', 51.66)), '成'),
        ('手冊', '628-36(2)', 'b', '628-36(1)', (('628-36(1)', 99.03),), '成'),
        ('手冊', '628-18(3)', 'b', '628-18(2)', (('628-18(2)', 96.82),), '成'),
        ('手冊', '628-39(2)', 'b', '628-39(1)', (('628-39(1)', 93.85),), '成'),
        ('手冊', '628-20(3)', 'b', '628-20(1)', (('628-20(1)', 42.15),), '成'),
        ('手冊', '628-41(3)', 'b', '628-41(1)', (('628-41(1)', 36.18),), '成'),
        ('手冊', '628-3(1)', 'b', '—', (), '未併'),
        ('手冊', '628-23(3)', 'b', '628-23(2)', (('628-23(2)', 12.11),), '成'),
        ('手冊', '628-44(1)', 'b', '628-40(1)', (('628-40(1)', 3.71),), '成'),
        ('手冊', '628-40(2)', 'b', '628-40(1)', (('628-40(1)', 2.52),), '成'),
        ('手冊', '628-22(3)', 'b', '628-22(2)', (('628-22(2)', 0.68),), '成'),
        ('手冊', '628-7(3)', 'c', ('628-7(1)', '628-7(2)'), (('628-7(1)', 784.36), ('628-7(2)', 784.36)), '成'),
        ('手冊', '628-45(3)', 'c', ('628-20(1)', '628-20(2)', '628-45(2)'), (('628-20(1)', 91.03), ('628-20(2)', 91.03), ('628-45(2)', 91.03)), '成'),
        ('手冊', '628-45(4)', 'c', ('628-20(1)', '628-20(2)', '628-45(2)'), (('628-20(1)', 74.87), ('628-20(2)', 74.87), ('628-45(2)', 74.87)), '成'),
    ],
}
# 配地之全部（推進側別 ＝ left／right 之列）：{暫編地號: (所屬街廓, 推進側別, G 2 位)}；各街廓之抵費地（幾何面積之和·2 位）
R3_EXPECT = {
    3.5: ({
        '628(1)': ('R4', 'left', 1788.69), '628(5)': ('R1', 'right', 376.12), '628-1(1)': ('R4', 'right', 721.79),
        '628-18(1)': ('R6', 'right', 307.78), '628-18(2)': ('R5', 'left', 268.33), '628-20(1)': ('R6', 'left', 466.36),
        '628-21(1)': ('R6', 'left', 433.74), '628-21(2)': ('R5', 'right', 471.39), '628-22(2)': ('R5', 'right', 520.82),
        '628-23(2)': ('R5', 'right', 430.68), '628-31(2)': ('R2', 'left', 465.05), '628-31(3)': ('R3', 'right', 464.95),
        '628-32(2)': ('R2', 'right', 516.09), '628-32(3)': ('R3', 'left', 500.43), '628-34(1)': ('R2', 'right', 601.64),
        '628-34(2)': ('R3', 'left', 250.24), '628-35(2)': ('R1', 'left', 741.92), '628-36(1)': ('R1', 'left', 638.61),
        '628-37(1)': ('R1', 'right', 285.21), '628-39(1)': ('R2', 'left', 289.43), '628-4(1)': ('R6', 'left', 779.93),
        '628-40(1)': ('R2', 'left', 359.59), '628-41(1)': ('R2', 'left', 313.51), '628-45(1)': ('R5', 'left', 525.28),
        '628-45(2)': ('R3', 'right', 902.52), '628-47(1)': ('R3', 'left', 429.59), '628-7(1)': ('R6', 'right', 1007.91),
        '628-7(2)': ('R5', 'left', 712.26),
    }, {'R1': 851.68, 'R2': 1823.3, 'R3': 1659.06, 'R4': 697.4, 'R5': 1221.44, 'R6': 980.59}),
    0.0: ({
        '628(1)': ('R4', 'left', 1788.69), '628(5)': ('R1', 'right', 376.12), '628-1(1)': ('R4', 'right', 721.79),
        '628-18(1)': ('R6', 'right', 307.78), '628-18(2)': ('R5', 'left', 259.13), '628-20(1)': ('R6', 'left', 466.36),
        '628-20(2)': ('R5', 'left', 534.47), '628-21(1)': ('R6', 'left', 433.74), '628-21(2)': ('R5', 'right', 471.39),
        '628-22(2)': ('R5', 'right', 520.82), '628-23(2)': ('R5', 'right', 430.68), '628-30(3)': ('R3', 'right', 562.01),
        '628-31(2)': ('R2', 'left', 465.05), '628-31(3)': ('R3', 'right', 461.99), '628-32(2)': ('R2', 'right', 516.09),
        '628-32(3)': ('R3', 'left', 500.43), '628-34(1)': ('R2', 'right', 601.64), '628-34(2)': ('R3', 'left', 250.24),
        '628-35(2)': ('R1', 'left', 730.81), '628-36(1)': ('R1', 'right', 662.1), '628-37(1)': ('R1', 'left', 272.83),
        '628-39(1)': ('R2', 'left', 289.43), '628-4(1)': ('R6', 'left', 779.93), '628-40(1)': ('R2', 'left', 359.59),
        '628-41(1)': ('R2', 'left', 313.51), '628-45(2)': ('R3', 'right', 343.46), '628-47(1)': ('R3', 'left', 429.59),
        '628-7(1)': ('R6', 'right', 1007.91), '628-7(2)': ('R5', 'left', 712.26),
    }, {'R1': 851.67, 'R2': 1823.3, 'R3': 1659.05, 'R4': 697.4, 'R5': 1221.47, 'R6': 980.59}),
}
# 調配之輸入之類（切片數, 原有面積合計 ㎡）
R4_EXPECT = {
    3.5: {'共同負擔用地·入合併單位': (32, 7116.89), '原位次配地': (73, 26311.71), '建築街廓內不能分配': (13, 1432.13), '無地號之殘料': (8, 0.0)},
    0.0: {'共同負擔用地·入合併單位': (32, 7116.89), '原位次配地': (73, 26311.71), '建築街廓內不能分配': (13, 1432.13), '無地號之殘料': (8, 0.0)},
}


def _pipeline(ns, fst, rv, sp, sb):
    with contextlib.redirect_stdout(io.StringIO()):
        snap = rv.load_snapshot()
        cb_by, cad = rv.build_pipeline(ns, fst, snap)
        rv.build_ownership(ns, fst, rv.ANON_XLSX)
        v6 = open(rv.V6DXF, "rb").read()
        tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
        params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
        res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
        log = copy.deepcopy(fst.session_state.get("f3_k953_log") or [])
        from stepg_pipeline import run_step_g
        ns["K917_DROPPED"].clear()
        sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                        eff_min_build_by_blk={})
    drops = {k: list(v) for k, v in ns["K917_DROPPED"].items()}
    own = dict(fst.session_state.get("t8_ownership_map") or {})
    bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
    it = ns["adj_intake"](res[5], sg["k929_6"]["build"], sg["g_rows"], drops, own, bur)
    return log, sg["g_rows"], it


def _norm(log):
    out = []
    for r in log or []:
        if r.get("序") not in ("手冊", "K-9-51", "單元", "整批"):
            continue
        rv_ = r.get("受併宗")
        rv_ = rv_ if isinstance(rv_, str) else tuple(rv_)
        q = tuple(sorted((k, round(float(v), 2)) for k, v in (r.get("併入量") or {}).items()))
        out.append((r.get("序"), r.get("片"), r.get("類"), rv_, q, r.get("結果")))
    return out


def run(repo, sbs):
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    if FN not in ns or not hasattr(sp, "run_k953"):
        print("  🔴 受詞缺")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    os.environ["WV_ADJ4"] = "off"   # 🔧 `W-G.9-367`（發單側窗六十八）：本器量手冊先行之果 ⇒ 規格步 4 乙於行程內 off
    red = []
    for sb in sbs:
        env = os.environ.get("WV_K953")
        try:
            os.environ["WV_K953"] = "off"
            _l0, rows0, _it0 = _pipeline(ns, fst, rv, sp, sb)
            if env is None:
                os.environ.pop("WV_K953", None)
            else:
                os.environ["WV_K953"] = env
            log, rows, it = _pipeline(ns, fst, rv, sp, sb)
        except Exception as e:  # noqa: BLE001
            print(f"  ⚠️ {sb}：執行中止 {type(e).__name__}：{str(e).splitlines()[0][:200] if str(e) else ''}")
            print("⇒ rc 3（無從判定）")
            return 3
        finally:
            if env is None:
                os.environ.pop("WV_K953", None)
            else:
                os.environ["WV_K953"] = env
        got = _norm(log)
        exp = R1_EXPECT.get(sb)
        ok1 = exp is not None and got == exp
        print(("  ✅" if ok1 else "  🔴") + f" R1@{sb}：手冊先行之紀錄 {len(got)} 列 ＝ 本器所載 {ok1}")
        if not ok1:
            red.append(f"R1@{sb}")
            if exp is not None:
                for a_, b_ in zip(got + [None] * max(0, len(exp) - len(got)), exp + [None] * max(0, len(got) - len(exp))):
                    if a_ != b_:
                        print(f"      得 {a_!r}\n      期 {b_!r}")
        c0 = sorted((r["所屬街廓"], r["推進側別"], str(r["暫編地號"])) for r in rows0 if r.get("驗_宗序") == "街角第1宗")
        c1 = sorted((r["所屬街廓"], r["推進側別"], str(r["暫編地號"])) for r in rows if r.get("驗_宗序") == "街角第1宗")
        ok2 = c0 == c1 and len(c0) > 0
        print(("  ✅" if ok2 else "  🔴") + f" R2@{sb}：街角第 1 宗 ＝ 旗標 off 之實跑 {ok2}（{len(c1)} 宗）")
        if not ok2:
            red.append(f"R2@{sb}")
        g0 = {str(r["暫編地號"]): float(r["G(㎡)"]) for r in rows0 if r.get("推進側別") in ("left", "right")}
        g1 = {str(r["暫編地號"]): (r["所屬街廓"], r["推進側別"], float(r["G(㎡)"])) for r in rows
              if r.get("推進側別") in ("left", "right")}
        p0, p1 = {}, {}
        for rr, pp in ((rows0, p0), (rows, p1)):
            for r in rr:
                if r.get("推進側別") == "抵費地":
                    pp[r["所屬街廓"]] = pp.get(r["所屬街廓"], 0.0) + float(r.get("幾何面積(㎡)") or 0)
        dpool = sum(p1.values()) - sum(p0.values())
        dg = sum(v[2] for v in g1.values()) - sum(g0.values())
        e3 = R3_EXPECT.get(sb)
        bad3 = []
        if e3 is None:
            bad3.append("無期")
        else:
            for k in sorted(set(g1) | set(e3[0])):
                a_, b_ = g1.get(k), e3[0].get(k)
                if a_ is None or b_ is None or a_[:2] != b_[:2] or abs(a_[2] - b_[2]) > TOL:
                    bad3.append((k, a_ if a_ is None else (a_[0], a_[1], round(a_[2], 2)), b_))
            for k in sorted(set(p1) | set(e3[1])):
                if k not in p1 or k not in e3[1] or abs(p1[k] - e3[1][k]) > TOL:
                    bad3.append((k, round(p1.get(k, -1.0), 2), e3[1].get(k)))
        ok3 = not bad3 and abs(dpool + dg) <= 0.1
        print(("  ✅" if ok3 else "  🔴") + f" R3@{sb}：配地 {len(g1)} 宗之街廓·推進側·G 與抵費地 {len(p1)} 街廓 ＝ 本器所載；"
              f"Σ抵費地之變 {dpool:.2f}／ΣG 之變 {dg:.2f}（和 ≤ 0.1）{ok3}")
        if not ok3:
            red.append(f"R3@{sb}")
            for x_ in bad3[:12]:
                print(f"      {x_}")
        tot = {k: (v[0], round(v[1], 2)) for k, v in sorted(it["totals"].items())}
        e4 = R4_EXPECT.get(sb)
        ok4 = e4 is not None and tot == e4 and it["step4"] == []
        print(("  ✅" if ok4 else "  🔴") + f" R4@{sb}：調配之輸入之類 ＝ 本器所載、待同歸戶併入 ＝ 空 {ok4}")
        if not ok4:
            red.append(f"R4@{sb}")
            print(f"      {tot}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── offsnap／offcmp：旗標 off ⇒ 逐位同開工態（R-17）──
def _canon(x):
    import hashlib
    import json
    b = json.dumps(x, sort_keys=True, ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha256(b).hexdigest(), len(b)


def offsnap(repo, out, sbs, gate=False):
    import json
    os.environ["WV_K953"] = "off"           # 行程內自設（開工態無此旗標 ⇒ 無作用）
    if gate:                                # 🔧 補令一：入池閘 off、手冊先行之旗標未設（R-17′）
        os.environ["WV_K929_6"] = "off"
        os.environ.pop("WV_K953", None)
    ns, fst = _harvest(repo)
    import run_verification as rv
    import selection_pipeline as sp
    from stepg_pipeline import run_step_g
    snap_out = {}
    for sb in sbs:
        ns["K917_DROPPED"].clear()
        with contextlib.redirect_stdout(io.StringIO()):
            snap = rv.load_snapshot()
            cb_by, cad = rv.build_pipeline(ns, fst, snap)
            rv.build_ownership(ns, fst, rv.ANON_XLSX)
            v6 = open(rv.V6DXF, "rb").read()
            tp, bp, _ = rv.build_build_parcels(ns, fst, v6, list(cb_by.values()), snap)
            params = rv.build_param_table(ns, fst, cb_by, cad, snap, sb)
            res = sp.run_corner_pk_k6b(ns, fst, list(cb_by.values()), cad, params, tp, bp, sb, snapshot=snap)
            ss = fst.session_state
            s3log = copy.deepcopy(ss.get("f3_k6b_stage3_log"))
            eblog = copy.deepcopy(ss.get("f3_end_block_merge_log"))
            k953 = ss.get("f3_k953_log", "<缺>")
            ns["K917_DROPPED"].clear()
            sg = run_step_g(ns, fst, list(cb_by.values()), cad, snap, params, res[6], res[3], res[4], sb,
                            eff_min_build_by_blk={})
        drops = {f"{k}": list(v) for k, v in ns["K917_DROPPED"].items()}
        own = dict(fst.session_state.get("t8_ownership_map") or {})
        bur = {b["label"]: ns["F3_CATEGORY_BURDEN"].get(b.get("category", ""), "") for b in cb_by.values()}
        if "k929_6" in sg:
            it = ns["adj_intake"](res[5], sg["k929_6"]["build"], sg["g_rows"], ns["K917_DROPPED"], own, bur)
            k9log, itp = sg["k929_6"].get("log"), {"totals": it["totals"], "units": it["units"], "step4": it["step4"]}
        else:                               # 🔧 補令一：入池閘 off ⇒ 無其回傳；調配之輸入以 build 為之（停機 ⇒ 記其首列）
            k9log = "<入池閘 off>"
            try:
                it = ns["adj_intake"](res[5], res[6], sg["g_rows"], ns["K917_DROPPED"], own, bur)
                itp = {"totals": it["totals"], "units": it["units"], "step4": it["step4"]}
            except RuntimeError as e:
                itp = ["停機", str(e).splitlines()[0][:300] if str(e) else ""]
        part = {
            "街角": [res[3], res[4]],
            "宗地": [[t.get("暫編地號"), t.get("段三併出"), t.get("段三部分併出"), t.get("段三餘量"),
                     t.get("面積_m2"), t.get("分攤登記面積_m2")] for t in res[5]],
            "build": [b.get("暫編地號") for b in res[6]],
            "段三紀錄": s3log, "末端塊紀錄": eblog,
            "配地": sg["g_rows"], "入池閘": k9log, "不配地": drops,
            "調配之輸入": itp,
        }
        snap_out[str(sb)] = {k: _canon(v) for k, v in part.items()}
        snap_out[str(sb)]["手冊先行之紀錄"] = (k953 if k953 == "<缺>" else len(k953))
        print(f"  {sb}：" + "；".join(f"{k} {v[0][:12]}" for k, v in snap_out[str(sb)].items() if isinstance(v, tuple))
              + f"；手冊先行之紀錄 {snap_out[str(sb)]['手冊先行之紀錄']}")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(snap_out, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print(f"⇒ 寫 {out}；rc 0")
    return 0


def offcmp(a, b):
    import json
    A, B = json.load(open(a, encoding="utf-8")), json.load(open(b, encoding="utf-8"))
    red = []
    for sb in sorted(set(A) | set(B)):
        for k in sorted(set(A.get(sb, {})) | set(B.get(sb, {}))):
            if k == "手冊先行之紀錄":
                continue
            ok = A.get(sb, {}).get(k) == B.get(sb, {}).get(k)
            print(("  ✅ " if ok else "  🔴 ") + f"{sb}·{k}")
            if not ok:
                red.append(f"{sb}·{k}")
        kb = B.get(sb, {}).get("手冊先行之紀錄")
        print(f"  ℹ️ {sb}·手冊先行之紀錄：{A.get(sb, {}).get('手冊先行之紀錄')} → {kb}")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], os.path.abspath(argv[2])
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "wiring" and len(argv) == 4:
        return wiring(repo, argv[3])
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    if cmd == "offsnap" and len(argv) >= 4:
        return offsnap(repo, os.path.abspath(argv[3]), [float(x) for x in argv[4:]] or [3.5, 0.0])
    if cmd == "gatesnap" and len(argv) >= 4:
        return offsnap(repo, os.path.abspath(argv[3]), [float(x) for x in argv[4:]] or [3.5, 0.0], gate=True)
    if cmd == "offcmp" and len(argv) == 4:
        return offcmp(os.path.abspath(argv[2]), os.path.abspath(argv[3]))
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
