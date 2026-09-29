# -*- coding: utf-8 -*-
"""W-G.9-355 量測器（發單側窗五十一擬·檔 F14·⛔ 由受單側改一字）：末端塊之合併再試（含 `K-9-50`）之**畫面路徑**。

受詞（`app.py` 模組層·`W-G.9-355` 規格單 `§三` 之介面）：
  f3_screen_end_block_merge(st, *, pk_kwargs, g_kwargs)  合併再試之畫面入口（段三之畫面入口之各正常出口呼之）
  k6b_screen_callbacks(st, *, pk_kwargs, g_kwargs)       段三與合併再試共用之四注入物
                                                          （回 {'a_prime', 'trial_winner', 'alloc_state', 'alloc_eval'}）
  end_block_merge_rows(rec, log)                         成果區之顯示（純函式·回 {'lines': [...], 'rows': [...]}）
  ＋ 既有 `f3_screen_k6b_stage3`（回傳之宗地 ＝ 合併再試後）、`k6b_stage3_selected`、`k6b_screen_build_for_g`、
    `K6B_SCREEN_TRIAL_KEYS`（含 `SS_END_BLOCK_MODE` 之值·末項仍 `f3_k929_6_log`）。

子命令（一律 python verify/probes/probe_WG9355_screenmerge.py <子命令> …）：
  selftest <repo>
           以樁（stub）代畫面二段（`f3_screen_corner_pk_run`／`f3_screen_stepg_run`）、段三本體（`k6b_stage3_run`）與
           合併再試本體（`end_block_merge_run`），⛔ 讀本案資料，量畫面入口之編排（期值出自規格單 `§三`·⛔ 呼叫受測碼求期）：
           T1 段三「段二序為空」之出口 × 合併再試無變／T2 段三旗標 off × 合併再試有變／T3 段三實辦且有變 × 合併再試有變／
           T9 段三實辦且有變 × 合併再試無變／T4 合併再試停機（RuntimeError）／T5 合併再試中斷（非 RuntimeError·旗標 off）／
           T8 段三停機 ⇒ 合併再試⛔ 辦／T6 四注入物（a′、試算選位、試算配地之 `'trial'`、中止即 RuntimeError）／
           T7 顯示／TK 試算隔離之鍵／TS 介面之簽名。P0 ＝ 判式自驗（期值記錄須全綠、逐項擾動須恰該項紅）。
  run      <repo> [<退縮> …]
           畫面路徑實跑本案（預設退縮 `3.5`、`0.0`）與合成案甲乙丙（退縮 `3.5`）：載入 F13
           （`verify/probes/probe_WG9354_endcontest.py`），以本器之畫面管線替其 `_pipeline`，逕用 F13 `run` 之全部判式
           （R1／C／F／X·外部錨由 F13 另寫·⛔ 呼叫受測函式）；注入（末端帶之寬、上鎖、假設跨占街角）同 F13。
           另 E1 試算旗標（`SS_END_BLOCK_MODE`）⛔ 外洩／E2 配地所用之宗地 ＝ 合併再試後／E3 正常出口無停機訊息。
rc：0 相符／1 不符／2 用法錯／3 無從判定（執行中止·⛔ 等同相符）。
"""
import contextlib, copy, importlib.util, inspect, io, os, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001
    pass

NEW = ("f3_screen_end_block_merge", "k6b_screen_callbacks", "end_block_merge_rows")
SB = 3.5


def _load(repo, rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(repo, *rel.split("/")))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _harvest(repo):
    sys.path.insert(0, os.path.join(repo, "verify"))
    from app_harvest import harvest
    with contextlib.redirect_stdout(io.StringIO()):
        ns, fake_st = harvest(os.path.join(repo, "app.py"))
    return ns, fake_st


def _report(cases):
    red = []
    for name, got, exp in cases:
        ok = got == exp
        print(("  ✅ " if ok else "  🔴 ") + f"{name}：得 {got!r}　期 {exp!r}")
        if not ok:
            red.append(name.split()[0])
    return red


# ── 啞 st（selftest 用）──
class _Stop(Exception):
    pass


class _Rerun(Exception):
    pass


class _CM:
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __call__(self, *a, **k):
        return _CM()

    def __getattr__(self, n):
        return _CM()

    def __iter__(self):
        return iter(())


class _St:
    def __init__(self, ss):
        object.__setattr__(self, "session_state", ss)
        object.__setattr__(self, "msgs", [])

    def stop(self):
        raise _Stop("st.stop")

    def rerun(self, *a, **k):
        raise _Rerun("st.rerun")

    def columns(self, spec, *a, **k):
        return [_CM() for _ in range(spec if isinstance(spec, int) else len(spec))]

    def tabs(self, names, *a, **k):
        return [_CM() for _ in names]

    def __getattr__(self, name):
        def _f(*a, **k):
            self.msgs.append((name, str(a[0])[:300] if a else ""))
            return _CM()
        return _f


# ── 玩具（⛔ 本案資料）──
PPZ = {"Z1": 1000.0, "Z2": 500.0}
CL = {"RD": [(0.0, -5.0), (50.0, -5.0)]}
OWN = {"A": "g1", "B": "g2", "C": "g3", "D": "g1"}
CB = [{"label": "B1", "category": "住宅區"}, {"label": "RD", "category": "道路"}]
EV = {"B1": {"left": {"觸發": True, "R_end(㎡)": 50.0, "候選": [], "當選": "A(1)"}}}
ORDER = [{"最終序位": 1, "街廓": "B1", "端": "左", "暫編地號": "A(1)"}]
L3 = {"序": 1, "街廓": "B1", "端": "左", "候選": "A(1)", "結果": "成"}
LOGM = [{"序": 1, "街廓": "B1", "端": "右", "候選": "B(1)", "結果": "成"}]
RECM = {"標的": [["B1", "right"]], "皆未達": {}}


def _tp(pid, blk, zone, a):
    return {"暫編地號": pid, "原地號": pid.split("(")[0], "所屬街廓": blk, "街廓分類": "住宅區",
            "分攤登記面積_m2": float(a), "面積_m2": 0.0, "重劃前地價區段": zone,
            "polygon_coords": [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]}


def _world():
    t = [_tp("A(1)", "B1", "Z1", 100), _tp("B(1)", "B1", "Z1", 80), _tp("C(1)", "B1", "Z2", 60),
         _tp("D(1)", "RD", "Z2", 30)]
    return t, [t[0], t[1], t[2]]


def _kw(t, b):
    pk = dict(B_value=0.3, C_for_calc=0.1, _build_blocks=[], _corner_rows_init=[{"街廓": "B1", "正面路寬(m)": 8.0}],
              _pd=None, build_parcels=b, post_price_by_block={"B1": 2000.0}, pre_price_by_zone=dict(PPZ),
              sb_rows_by_label={}, temp_parcels=t)
    g = dict(_param_key="p_key", B_value=0.3, C_for_calc=0.1, _tab6_burden=0.4, block_meta_by_label={},
             sb_rows_by_label={}, post_price_by_block={"B1": 2000.0}, pre_price_by_zone=dict(PPZ),
             classified_blocks=copy.deepcopy(CB))
    return pk, g


def _reset(ns, ss):
    ss.clear()
    ss.update({"f3L_setback_default": SB, "t8_ownership_map": dict(OWN), "f3_manual_road_centerlines": copy.deepcopy(CL),
               "p_key": {}, "f3_G_values": ["SENT_G"], ns["SS_END_BLOCK_EVAL"]: {"SENT": 1},
               ns["SS_END_BLOCK_MERGE"]: {"舊紀錄": 1}, "f3_end_block_merge_log": ["舊紀錄"]})
    ns["K917_DROPPED"].clear()
    ns["K917_DROPPED"]["SENT"] = 1


class _Rig:
    """樁：畫面二段、段三本體、合併再試本體。逐次呼叫記錄於 `calls`。"""
    def __init__(self, ns, ss, cfg):
        self.ns, self.ss, self.cfg = ns, ss, cfg
        self.calls, self.merge_n, self.s3_n = [], 0, 0
        self.merge_args = self.merge_ret = self.s3_ret = self.s3_state = None
        self.ev_got = self.ev_same_obj = None
        self.in_s3 = False

    def _real(self, st):
        return not isinstance(st, self.ns["_K6BTrialSt"])

    def pk(self, st, **kw):
        ss = st.session_state
        ids = [t["暫編地號"] for t in kw["temp_parcels"]]
        bids = [b["暫編地號"] for b in kw["build_parcels"]]
        real = self._real(st)
        self.calls.append(("pk", real, ids, bids, kw["temp_parcels"], kw["build_parcels"]))
        ss["f3_corner_winners"] = {"B1": {"p1_end": ids[0], "p2_end": None}}
        ss["f3L_corner_winners"] = {"B1": {"p1_end": ids[0]}}
        ss["f3_corner_cand_diag"] = [{"街廓": "B1", "端": "左", "候選地號": ids[0], "真G(㎡)": 123.45, "門檻(㎡)": 100.0}]
        ss["f3L_forced_offset"] = {}
        ss["f3_corner_range_polys"] = {}
        ss["f3_k6b_stage1_locked_by_block"] = {"B1": [ids[-1]]}
        ss["f3_k6b_stage2_order"] = copy.deepcopy(self.cfg.get("order", []))
        ss["f3_pk_alloc_depth"] = ("real" if real else "trial", len(self.calls), tuple(ids))
        return None

    def g(self, st, **kw):
        ss = st.session_state
        ids = [b["暫編地號"] for b in kw["build_parcels"]]
        self.calls.append(("g", ss.get(self.ns["SS_END_BLOCK_MODE"]), ids, self._real(st), self.in_s3))
        if self.cfg.get("g_stop"):
            st.stop()
        ss["f3_G_values"] = [{"暫編地號": ids[0], "所屬街廓": "B1", "驗_總判": "保留"}]
        ss[self.ns["SS_END_BLOCK_EVAL"]] = copy.deepcopy(EV)
        self.ns["K917_DROPPED"]["X"] = 1
        st.rerun()

    def s3(self, order, locked, own_map, temp_parcels, build_parcels, blocks, centerlines, a_prime, trial_winner,
           alloc_state, *, log_print=print, contests=None):
        self.s3_n += 1
        self.in_s3 = True
        try:
            self.s3_state = alloc_state(temp_parcels, build_parcels)
        finally:
            self.in_s3 = False
        m = self.cfg.get("s3", "same")
        if m == "raise_rt":
            raise RuntimeError("🔴 [K-6-B 段三] 樁之停機 Q8")
        if m == "same":
            self.s3_ret = (temp_parcels, build_parcels)
            return temp_parcels, build_parcels, [dict(L3)]
        t2 = copy.deepcopy(temp_parcels)[:-1]
        by = {x["暫編地號"]: x for x in t2}
        b2 = [by[b["暫編地號"]] for b in build_parcels]
        self.s3_ret = (t2, b2)
        return t2, b2, [dict(L3)]

    def merge(self, temp_parcels, build_parcels, own_map, locked, corner_lots, blocks, centerlines, a_prime,
              alloc_eval, alloc_state, *, setback=None, log_print=print):
        self.merge_n += 1
        self.merge_args = dict(temp=temp_parcels, build=build_parcels, own=dict(own_map or {}), locked=set(locked or ()),
                               corner=set(corner_lots or ()), blocks=copy.deepcopy(blocks),
                               cl=copy.deepcopy(centerlines), setback=setback)
        self.ev_got = alloc_eval(temp_parcels, build_parcels)
        self.ev_same_obj = self.ev_got is self.ss.get(self.ns["SS_END_BLOCK_EVAL"])
        m = self.cfg.get("merge", "same")
        if m == "raise_rt":
            raise RuntimeError("🔴 [末端塊合併再試] 樁之停機 Q9")
        if m == "raise_key":
            raise KeyError("樁之中斷 Q7")
        if m == "same":
            return temp_parcels, build_parcels, [], {"退縮": setback, "標的": [], "皆未達": {}}
        t2 = copy.deepcopy(temp_parcels)
        by = {x["暫編地號"]: x for x in t2}
        b2 = [by[b["暫編地號"]] for b in build_parcels][:-1]
        self.merge_ret = (t2, b2)
        return t2, b2, copy.deepcopy(LOGM), dict(RECM, 退縮=setback)


STUBS = ("f3_screen_corner_pk_run", "f3_screen_stepg_run", "k6b_stage3_run", "end_block_merge_run")


@contextlib.contextmanager
def _rigged(ns, ss, cfg, env):
    rig = _Rig(ns, ss, cfg)
    saved = {k: ns[k] for k in STUBS}
    old_env = os.environ.get("WV_K6B_STAGE3")
    os.environ["WV_K6B_STAGE3"] = env
    ns["f3_screen_corner_pk_run"], ns["f3_screen_stepg_run"] = rig.pk, rig.g
    ns["k6b_stage3_run"], ns["end_block_merge_run"] = rig.s3, rig.merge
    try:
        yield rig
    finally:
        ns.update(saved)
        if old_env is None:
            os.environ.pop("WV_K6B_STAGE3", None)
        else:
            os.environ["WV_K6B_STAGE3"] = old_env


def _enter(ns, ss, pk, g):
    st = _St(ss)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ret = ns["f3_screen_k6b_stage3"](st, pk_kwargs=pk, g_kwargs=g)
        return st, ret, None
    except BaseException as e:  # noqa: BLE001  （含 _Stop）
        return st, None, e


def _selected(ns, ss, b, sb=SB):
    try:
        r = ns["k6b_stage3_selected"](ss, b, sb)
    except RuntimeError as e:
        return ("raise", "請重跑" in str(e))
    if r is None:
        return None
    return ("tuple", r[0], r[1])


def _common(ns, ss, rig, tag):
    """各正常／停機出口共通之期：試算旗標不外洩、試算所改之鍵復原、試算配地一律 'trial'。"""
    gs = [c for c in rig.calls if c[0] == "g"]
    reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
    return [
        (f"{tag}c1 試算旗標⛔ 外洩（SS_END_BLOCK_MODE 不在 session）", ns["SS_END_BLOCK_MODE"] in ss, False),
        (f"{tag}c2 試算所改之鍵復原（f3_G_values／SS_END_BLOCK_EVAL／K917_DROPPED）",
         (ss.get("f3_G_values"), ss.get(ns["SS_END_BLOCK_EVAL"]), dict(ns["K917_DROPPED"])),
         (["SENT_G"], {"SENT": 1}, {"SENT": 1})),
        (f"{tag}c3 f3_pk_alloc_depth ＝ 末一次真 st 之街角選位所寫",
         (ss.get("f3_pk_alloc_depth") or ("<缺>",))[0], "real" if reals else "<缺>"),
        (f"{tag}c4 試算配地皆 'trial'（其數 ≥ 1）", (len(gs) >= 1, sorted({c[1] for c in gs}, key=str)), (True, ["trial"])),
    ]


def _stopc(ns, ss, rig, tag):
    """停機出口之共通期（⛔ 含 c3：停機出口未必有真 st 之街角選位）。"""
    c = _common(ns, ss, rig, tag)
    return [c[0], c[1], c[3]]


def _t1(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], merge="same"), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
        a = rig.merge_args or {}
        out = [
            ("T1a 段二序為空之出口：正常結束、ran False", (exc is None, (ret or {}).get("ran")), (True, False)),
            ("T1b 合併再試恰一次、段三本體⛔ 呼", (rig.merge_n, rig.s3_n), (1, 0)),
            ("T1c 無變 ⇒ 回傳之宗地 ＝ 輸入（同一物件）", (ret is not None and ret["temp"] is t0, ret is not None and ret["build"] is b0),
             (True, True)),
            ("T1d 紀錄與逐列入 session", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             ({"退縮": SB, "標的": [], "皆未達": {}}, [])),
            ("T1e 無變 ⇒ 段三之結果⛔ 存（k6b_stage3_selected ＝ None）、無停機訊息",
             (_selected(ns, ss, b0), ss.get("f3_k6b_stage3_error")), (None, None)),
            ("T1f 無變 ⇒ 真 st 之街角選位⛔ 重跑（恰一）", len(reals), 1),
            ("T1g 合併再試之輸入：宗地 ＝ 段三之出（此出口 ＝ 原宗地）",
             (a.get("temp") is t0, a.get("build") is b0), (True, True)),
            ("T1h 合併再試之輸入：上鎖 ＝ 末一次真 st 街角選位之段一上鎖、街角第 1 宗 ＝ 其 winners、街廓／中心線／退縮／歸戶",
             (a.get("locked"), a.get("corner"), a.get("blocks"), a.get("cl"), a.get("setback"), a.get("own")),
             ({"D(1)"}, {"A(1)"}, {"B1": {"category": "住宅區"}, "RD": {"category": "道路"}}, CL, SB, OWN)),
            ("T1i alloc_eval 回試算配地之評選（深拷貝）", (rig.ev_got, rig.ev_same_obj), (EV, False)),
        ]
        out += _common(ns, ss, rig, "T1")
    return out


def _t2(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=ORDER, merge="change"), "off") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
        mr = rig.merge_ret or (None, None)
        sel = _selected(ns, ss, b0)
        _, b_other = _world()
        out = [
            ("T2a 段三旗標 off 之出口：正常結束、ran False", (exc is None, (ret or {}).get("ran")), (True, False)),
            ("T2b 合併再試恰一次、段三本體⛔ 呼", (rig.merge_n, rig.s3_n), (1, 0)),
            ("T2c 有變 ⇒ 回傳之宗地 ＝ 合併再試之出（同一物件）",
             (ret is not None and ret["temp"] is mr[0], ret is not None and ret["build"] is mr[1]), (True, True)),
            ("T2d 紀錄與逐列入 session", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             (dict(RECM, 退縮=SB), LOGM)),
            ("T2e 配地所用之宗地 ＝ 合併再試之出（k6b_stage3_selected·同一物件）",
             (sel is not None and sel[0] == "tuple" and sel[1] is mr[0], sel is not None and sel[0] == "tuple" and sel[2] is mr[1]),
             (True, True)),
            ("T2f 所存之結果繫於段三前之宗地與退縮（他 build 或他退縮 ⇒ loud）",
             (_selected(ns, ss, b_other[:2]), _selected(ns, ss, b0, 0.0)), (("raise", True), ("raise", True))),
            ("T2g 有變 ⇒ 真 st 之街角選位重跑一次、所用 ＝ 合併再試之出",
             (len(reals), bool(reals) and reals[-1][4] is mr[0] and reals[-1][5] is mr[1]), (2, True)),
            ("T2h 無停機訊息", ss.get("f3_k6b_stage3_error"), None),
        ]
        out += _common(ns, ss, rig, "T2")
    return out


def _t3(ns, ss, merge):
    tag = "T3" if merge == "change" else "T9"
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=ORDER, s3="change", merge=merge), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        reals = [c for c in rig.calls if c[0] == "pk" and c[1]]
        s3r = rig.s3_ret or (None, None)
        fin = (rig.merge_ret or (None, None)) if merge == "change" else s3r
        a = rig.merge_args or {}
        gs3 = [c for c in rig.calls if c[0] == "g" and c[4]]
        sel = _selected(ns, ss, b0)
        out = [
            (f"{tag}a 段三實辦之出口：正常結束、ran True、段三紀錄", (exc is None, (ret or {}).get("ran"), (ret or {}).get("log"),
                                                         ss.get("f3_k6b_stage3_log"), ss.get("f3_k6b_stage3_order_used")),
             (True, True, [L3], [L3], ORDER)),
            (f"{tag}b 段三本體與合併再試各恰一次", (rig.s3_n, rig.merge_n), (1, 1)),
            (f"{tag}c 段三之試算配地亦 'trial'", [c[1] for c in gs3], ["trial"]),
            (f"{tag}d 段三之 alloc_state 之出", rig.s3_state, {"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None,
                                                           "G": {"A(1)": 0.0}}),
            (f"{tag}e 合併再試之輸入 ＝ 段三之出（同一物件）；上鎖取自段三終趟之真 st 街角選位",
             (a.get("temp") is s3r[0], a.get("build") is s3r[1], a.get("locked")), (True, True, {"C(1)"})),
            (f"{tag}f 回傳之宗地 ＝ 末態（同一物件）", (ret is not None and ret["temp"] is fin[0], ret is not None and ret["build"] is fin[1]),
             (True, True)),
            (f"{tag}g 配地所用之宗地 ＝ 末態（k6b_stage3_selected·同一物件）",
             (sel is not None and sel[0] == "tuple" and sel[1] is fin[0], sel is not None and sel[0] == "tuple" and sel[2] is fin[1]),
             (True, True)),
            (f"{tag}h 紀錄入 session", ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"),
             dict(RECM, 退縮=SB) if merge == "change" else {"退縮": SB, "標的": [], "皆未達": {}}),
            (f"{tag}i 真 st 之街角選位：段三終趟一次 ＋（有變 ⇒ 再一次·所用 ＝ 末態）",
             (len(reals), bool(reals) and reals[-1][4] is fin[0]), (2 if merge == "change" else 1, True)),
            (f"{tag}j 無停機訊息", ss.get("f3_k6b_stage3_error"), None),
        ]
        out += _common(ns, ss, rig, tag)
    return out


def _t4(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], merge="raise_rt"), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        err = str(ss.get("f3_k6b_stage3_error") or "")
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ns["k6b_screen_build_for_g"](_St(ss), b0)
            bfg = "未擋"
        except _Stop:
            bfg = "st.stop"
        except BaseException as e:  # noqa: BLE001
            bfg = type(e).__name__
        out = [
            ("T4a 合併再試停機 ⇒ 畫面 st.error ＋ st.stop", (type(exc).__name__ if exc else None,
                                                   any(n == "error" and "Q9" in m for n, m in st.msgs)), ("_Stop", True)),
            ("T4b 停機訊息入 session（含合併再試之原訊息）", "Q9" in err, True),
            ("T4c 其後之配地 loud（k6b_stage3_selected raise「請重跑」；k6b_screen_build_for_g ⇒ st.stop）",
             (_selected(ns, ss, b0), bfg), (("raise", True), "st.stop")),
            ("T4d 前次之紀錄已去、本次⛔ 寫", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             ("<缺>", "<缺>")),
        ]
        out += _stopc(ns, ss, rig, "T4")
    return out


def _t5(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], merge="raise_key"), "off") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        err = str(ss.get("f3_k6b_stage3_error") or "")
        out = [
            ("T5a 合併再試中斷（KeyError）⇒ 例外上拋", type(exc).__name__ if exc else None, "KeyError"),
            ("T5b 未完成之標記留存（其文含「末端塊合併再試」）", "末端塊合併再試" in err, True),
            ("T5c 其後之配地 loud（k6b_stage3_selected raise「請重跑」）", _selected(ns, ss, b0), ("raise", True)),
            ("T5d 前次之紀錄已去", ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), "<缺>"),
        ]
        out += _stopc(ns, ss, rig, "T5")
    return out


def _t8(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=ORDER, s3="raise_rt", merge="same"), "on") as rig:
        st, ret, exc = _enter(ns, ss, pk, g)
        out = [
            ("T8a 段三停機 ⇒ st.stop；合併再試⛔ 辦", (type(exc).__name__ if exc else None, rig.merge_n), ("_Stop", 0)),
            ("T8b 前次之紀錄已去（⛔ 殘留舊紀錄）", (ss.get(ns["SS_END_BLOCK_MERGE"], "<缺>"), ss.get("f3_end_block_merge_log", "<缺>")),
             ("<缺>", "<缺>")),
            ("T8c 停機訊息含段三之原訊息", "Q8" in str(ss.get("f3_k6b_stage3_error") or ""), True),
        ]
        out += _stopc(ns, ss, rig, "T8")
    return out


def _t6(ns, ss):
    t0, b0 = _world()
    pk, g = _kw(t0, b0)
    out = []
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[]), "on") as rig:
        st = _St(ss)
        cb = ns["k6b_screen_callbacks"](st, pk_kwargs=pk, g_kwargs=g)
        out.append(("T6a 四注入物之名", sorted(cb), ["a_prime", "alloc_eval", "alloc_state", "trial_winner"]))
        out.append(("T6b a′ ＝ a(src) × p(src) ÷ p(dst)（100 × 1000 ÷ 500）", round(cb["a_prime"](t0[0], t0[2]), 9), 200.0))
        with contextlib.redirect_stdout(io.StringIO()):
            tw = cb["trial_winner"](t0, b0, "B1", "左", "A(1)")
        out.append(("T6c 試算選位回 (winner, 真G, 門檻)", tw, ("A(1)", 123.45, 100.0)))
        n0 = len(rig.calls)
        with contextlib.redirect_stdout(io.StringIO()):
            stt = cb["alloc_state"](t0, b0)
        gs = [c for c in rig.calls[n0:] if c[0] == "g"]
        out.append(("T6d 試算配地（alloc_state）之出與其 'trial'", (stt, [c[1] for c in gs]),
                    ({"kept": {"B1": {"A(1)"}}, "bad_pools": {}, "err": None, "G": {"A(1)": 0.0}}, ["trial"])))
        n0 = len(rig.calls)
        with contextlib.redirect_stdout(io.StringIO()):
            ev = cb["alloc_eval"](t0, b0)
        gs = [c for c in rig.calls[n0:] if c[0] == "g"]
        out.append(("T6e 試算配地（alloc_eval）回評選之深拷貝、其 'trial'",
                    (ev, ev is ss.get(ns["SS_END_BLOCK_EVAL"]), [c[1] for c in gs]), (EV, False, ["trial"])))
    _reset(ns, ss)
    with _rigged(ns, ss, dict(order=[], g_stop=True), "on") as rig:
        cb = ns["k6b_screen_callbacks"](_St(ss), pk_kwargs=pk, g_kwargs=g)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                cb["alloc_eval"](t0, b0)
            got = "無例外"
        except RuntimeError:
            got = "RuntimeError"
        except BaseException as e:  # noqa: BLE001
            got = type(e).__name__
        out.append(("T6f 試算配地中止（st.stop）⇒ alloc_eval 拋 RuntimeError", got, "RuntimeError"))
    _reset(ns, ss)
    return out


REC_D = {"退縮": 3.5, "標的": [["RA", "left"], ["RB", "right"]], "皆未達": {"RA": ["left"]},
         "競合": [{"形": "一", "列": [["RA", "左", "P(4)", 66.49], ["RB", "右", "P(3)", 237.57]]}]}
LOG_D = [{"序": 1, "街廓": "RB", "端": "右", "候選": "P(3)", "結果": "成", "檢核": None},
         {"序": "後處理", "街廓": "RB", "端": "右", "候選": "P(4)", "結果": "成", "檢核": "通過"}]


def _t7(ns):
    f = ns["end_block_merge_rows"]
    v = f(copy.deepcopy(REC_D), copy.deepcopy(LOG_D))
    txt = "\n".join(v.get("lines") or [])
    need = ["RA", "RB", "左", "右", "P(4)", "P(3)", "66.49", "237.57", "強制抵費地", "3.5"]
    v2 = f({"退縮": 0.0, "標的": [], "皆未達": {}}, [])
    v3 = f({"退縮": 3.5, "標的": None, "皆未達": {}, "試算中止": "🔴 樁之中止 Q6"}, [])
    t3 = "\n".join(v3.get("lines") or [])
    return [
        ("T7a 逐列 ＝ 紀錄之列（值一律字串·None ⇒ —）", v.get("rows"),
         [{k: ("—" if x is None else str(x)) for k, x in r.items()} for r in LOG_D]),
        ("T7b 行內載標的之街廓與端、競合之候選與交面積、皆未達 ⇒ 強制抵費地、退縮", [s for s in need if s not in txt], []),
        ("T7c 無標的 ⇒ 行含「無標的」、逐列空", (any("無標的" in s for s in (v2.get("lines") or [])), v2.get("rows")),
         (True, [])),
        ("T7d 試算中止 ⇒ 行含「試算中止」與其訊息", ("試算中止" in t3, "Q6" in t3), (True, True)),
        ("T7e 無紀錄 ⇒ 空", f(None, None), {"lines": [], "rows": []}),
    ]


def _tk(ns):
    keys = tuple(ns.get("K6B_SCREEN_TRIAL_KEYS") or ())
    return [("TK 試算隔離之鍵含 SS_END_BLOCK_MODE 之值、末項仍 f3_k929_6_log",
             (ns["SS_END_BLOCK_MODE"] in keys, keys[-1:] == ("f3_k929_6_log",)), (True, True))]


def _ts(ns):
    def sig(fn):
        p = inspect.signature(ns[fn]).parameters.values()
        return ([x.name for x in p if x.kind in (x.POSITIONAL_ONLY, x.POSITIONAL_OR_KEYWORD)],
                sorted(x.name for x in p if x.kind == x.KEYWORD_ONLY))
    return [("TS 三介面之簽名", [sig(f) for f in NEW],
             [(["st"], ["g_kwargs", "pk_kwargs"]), (["st"], ["g_kwargs", "pk_kwargs"]), (["rec", "log"], [])])]


def _perturb(v):
    if isinstance(v, bool):
        return not v
    return ("<擾>", repr(v)[:40])


def selftest(repo):
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        ns, fake_st = _harvest(repo)
        ss = fake_st.session_state
        miss = [n for n in NEW if n not in ns]
        print(f"── 受詞：{list(NEW)} ⇒ 缺 {miss} ──")
        cases = []
        for tag, fn in (("T1", _t1), ("T2", _t2), ("T3", lambda a, b: _t3(a, b, "change")),
                        ("T9", lambda a, b: _t3(a, b, "same")), ("T4", _t4), ("T5", _t5), ("T8", _t8)):
            try:
                cases += fn(ns, ss)
            except Exception as e:  # noqa: BLE001
                cases.append((f"{tag}例外", ("例外", type(e).__name__, str(e)[:160]), "無例外"))
        cases += _tk(ns)
        if not miss:
            try:
                cases += _t6(ns, ss)
            except Exception as e:  # noqa: BLE001
                cases.append(("T6 例外", ("例外", type(e).__name__, str(e)[:160]), "無例外"))
            try:
                cases += _t7(ns)
            except Exception as e:  # noqa: BLE001
                cases.append(("T7 例外", ("例外", type(e).__name__, str(e)[:160]), "無例外"))
            cases += _ts(ns)
        print("── 合成對照（樁·期值出自規格單 §三）──")
        red = _report(cases)
        if miss:
            print(f"  🔴 受詞缺：{miss}（T6／T7／TS 無從量）")
            red.append("受詞缺")
        print("── P0 判式自驗（期值記錄須全綠；逐項擾動須恰該項紅）──")
        p0 = [n for n, g, e in cases if e != e]                        # 期值自身須自等
        flips = 0
        for i, (n, g, e) in enumerate(cases):
            alt = [(m, (_perturb(ee) if j == i else ee), ee) for j, (m, gg, ee) in enumerate(cases)]
            bad = [m for m, gg, ee in alt if gg != ee]
            flips += (bad == [n])
        ok0 = not p0 and flips == len(cases)
        print(("  ✅" if ok0 else "  🔴") + f" P0 期值記錄全綠 {not p0}；逐項擾動恰該項紅 {flips}／{len(cases)}")
        if not ok0:
            red.append("P0")
    finally:
        os.chdir(cwd)
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


# ── run：畫面路徑之管線（注入同 F13·判式逕用 F13）──
def _screen_pipeline_factory(f13, f4, extra):
    def _pipeline(ns, fake_st, rv, sb, scen=None):
        import numpy as np
        from shapely.geometry import Polygon
        from shapely.ops import unary_union
        saved = {k: ns[k] for k in ("end_block_host", "end_block_merge_run", "end_block_side_geom")}
        cfg = f13.SCEN.get(scen) or dict(wid={}, lock=[], excl=[])
        hits = {"host": 0, "merge": 0, "geo": 0}
        msig = inspect.signature(saved["end_block_merge_run"])

        def geo(block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir, min_width, side, _label=''):
            w = cfg["wid"].get((_label, side))
            if w is None:
                return saved["end_block_side_geom"](block_poly, d_hat, corner_pt, front_p2, cad_alloc, allocation_dir,
                                                    min_width, side, _label=_label)
            hits["geo"] += 1
            p1 = np.asarray(corner_pt, float)[:2]
            dd = np.asarray(d_hat, float)[:2]
            sp2 = float(np.dot(np.asarray(front_p2, float)[:2] - p1, dd))
            e = p1 if side == "left" else p1 + sp2 * dd
            band = ns["_end_band"](block_poly, cad_alloc, e, w, _label=_label)
            rr = ns["_strip_s_range"](band, d_hat, corner_pt, allocation_dir)
            buf = float(rr[1]) if side == "left" else float(sp2 - float(rr[0]))
            return {"gate": True, "unfront": 0.0, "s_back": 0.0, "r_end": band, "r_end_area": float(band.area),
                    "band_area": float(band.area), "buf": buf}

        def host(ordered, **kw):
            if cfg["excl"]:
                crp = dict(kw["corner_range_polys"])
                fake = [Polygon(e["tp"]["polygon_coords"]).buffer(0) for e in ordered
                        if e["tp"].get("暫編地號") in cfg["excl"]]
                if fake:
                    hits["host"] += 1
                    for sd in ("left", "right"):
                        crp[sd] = unary_union(fake + ([crp[sd]] if crp.get(sd) is not None else []))
                kw["corner_range_polys"] = crp
            return saved["end_block_host"](ordered, **kw)

        def merge(*a, **k):
            ba = msig.bind(*a, **k)
            if cfg["lock"]:
                hits["merge"] += 1
                ba.arguments["locked"] = set(ba.arguments["locked"] or ()) | set(cfg["lock"])
            return saved["end_block_merge_run"](*ba.args, **ba.kwargs)
        ns["end_block_host"], ns["end_block_merge_run"], ns["end_block_side_geom"] = host, merge, geo
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                snapshot = rv.load_snapshot()
                cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
                rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
                v6 = open(rv.V6DXF, "rb").read()
                temp_p, build_p, _ = rv.build_build_parcels(ns, fake_st, v6, list(cb_by.values()), snapshot)
                params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
            out = dict(cb_by=cb_by, cad=cad, snapshot=snapshot, params=params, hits=hits, err=None, temp0=temp_p)
            ss = fake_st.session_state
            pk, g = f4._screen_inputs(ns, fake_st, snapshot, list(cb_by.values()), cad, params, temp_p, build_p, sb)
            qs = f4.QuietSt(ss)
            ns["K917_DROPPED"].clear()
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    ret = ns["f3_screen_k6b_stage3"](qs, pk_kwargs=pk, g_kwargs=g)
            except f4._Stop:
                out["err"] = ("畫面·段三／合併再試", str(qs.msgs[-3:])[:400])
                return out
            except RuntimeError as e:
                out["err"] = ("畫面·段三／合併再試", str(e).splitlines()[0][:400])
                return out
            out["rec"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_MERGE"]))
            out["log"] = copy.deepcopy(ss.get("f3_end_block_merge_log") or [])
            out["temp"], out["build"] = ret["temp"], ret["build"]
            e1 = ns["SS_END_BLOCK_MODE"] not in ss
            e3 = "f3_k6b_stage3_error" not in ss
            try:
                sel = ns["k6b_stage3_selected"](ss, build_p, sb)
                bfg = build_p if sel is None else sel[1]
            except RuntimeError:
                bfg = None
            e2 = bfg is not None and bfg is ret["build"]
            extra.append((sb, scen, e1, e2, e3))
            if bfg is None:
                out["err"] = ("畫面·配地前", "k6b_stage3_selected 停機")
                return out
            ns["K917_DROPPED"].clear()
            rows = f4._run_screen_g(ns, qs, g, bfg, lambda s: None)
            if rows is None:
                out["err"] = ("畫面·配地", str(qs.msgs[-3:])[:400])
                return out
            out["ev"] = copy.deepcopy(ss.get(ns["SS_END_BLOCK_EVAL"]) or {})
            out["rows"] = rows
            return out
        finally:
            for k, v in saved.items():
                ns[k] = v
    return _pipeline


def run(repo, sbs):
    sys.path.insert(0, os.path.join(repo, "verify"))
    ns, _ = _harvest(repo)
    miss = [n for n in NEW if n not in ns]
    if miss:
        print(f"  🔴 受詞缺：{miss}")
        print("⇒ 紅 ['受詞缺']；rc 1")
        return 1
    f13 = _load(repo, "verify/probes/probe_WG9354_endcontest.py", "f13_for_f14")
    f4 = _load(repo, "verify/probes/probe_WG9345_screen.py", "f4_for_f14")
    extra = []
    f13._pipeline = _screen_pipeline_factory(f13, f4, extra)
    print("── F13 之判式施於畫面路徑（R1 本案·C／F／X 合成案甲乙丙）──")
    rc13 = f13.run(repo, sbs)
    if rc13 == 3:
        print("⇒ rc 3（F13 之判式無從判定·畫面路徑執行中止）")
        return 3
    red = [] if rc13 == 0 else [f"F13判式 rc {rc13}"]
    print("── E：畫面路徑之專項 ──")
    for sb, scen, e1, e2, e3 in extra:
        tag = f"{sb}{'·' + scen if scen else ''}"
        ok = e1 and e2 and e3
        print(("  ✅" if ok else "  🔴") + f" E@{tag}：試算旗標⛔ 外洩 {e1}；配地所用之宗地 ＝ 合併再試後 {e2}；無停機訊息 {e3}")
        if not ok:
            red.append(f"E@{tag}")
    n_exp = len(sbs) + 3
    if len(extra) != n_exp:
        print(f"  🔴 E 之量 {len(extra)}（期 {n_exp}·畫面入口未全數跑畢）")
        red.append("E量")
    print(f"⇒ 紅 {red}；rc {1 if red else 0}")
    return 1 if red else 0


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, repo = argv[1], argv[2]
    if cmd == "selftest":
        return selftest(repo)
    if cmd == "run":
        sbs = [float(x) for x in argv[3:]] or [3.5, 0.0]
        return run(repo, sbs)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
