"""`W-G.9-306` `§五`：可達性二根集之**重測**（走訪規則依**協定**重立·根型別**先自證**）。

🔒 底本 ＝ `verify/probes/probe_WG9305R_reach.py`（單 `§五` ② 明文授權「得以其碼為底本另存新檔」）；
   **⛔ 動該既有探針一字**。
🔒 授權三手段（單 `§五` 首段逐字）：① `run_verification` 全量**一次**；② 於 `verify/probes/` 新增量測器＋落檔；
   ③ **於行程內包裝**（⛔ 動任何檔·**冪等**）`ns` 之三鍵 `_corner_buffer_S`／`_solve_G_one`／`_first_corner_alloc_dir`，
   及模組 `verify/stepg_pipeline.py` 之屬性 `_run_step_g_impl`（**僅供計其進入序號**）。
🛑 ⛔ 改生產碼一字、⛔ 自寫第二套幾何（**只比對既有之值**·⛔ 重算任何向）、⛔ 判落點、⛔ 判可施。
🛑 `id(·)` **僅准**作單次走訪內之已訪集合（⛔ 出艙·⛔ 作錨）。

🆕 **本器與底本之別**（`自誤 415` 之攔法 ①②④）
   `R0`〜`R7` **依序判定·先中者即止**；容器一律**依協定**界定：
     `R4` 映射協定 ＝ **`type(o)`** 同具屬性 `keys` ⋀ `__getitem__`（🔒 **以 `type(o)` 檢·⛔ 以實例屬性**
          ——實例之 `__getattr__` 可對任何名回傳可呼叫物，`verify/app_harvest.py` 之 `_FakeStreamlit` 即其形）；
     `R7` **殘餘**一律以 `gc.get_referents` 穿越；其結果為空者方登記「**不透明**」
          （型別名·次數·**首見路徑**·**所屬根集**），**⛔ 靜默判為葉**。
   🔑 **根型別自證**（`§五-3`·`T1`〜`T5`）於**長跑前**以**同一直譯器之真實同型物**實跑；
      任一不命中 ⇒ **停、⛔ 啟動長跑**。[必命中] 造**⛔ 僅以合成 `dict`** 充之。
🛑 **二根集⛔ 合併**——不透明登記與走訪例外一律**分列**（底本之缺漏）。
"""
import os
import sys
import types
import gc
import collections

sys.stdout.reconfigure(encoding="utf-8", newline="\n")      # 坑 `bn`：`newline` ⛔ 可省

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
SELF = os.path.abspath(__file__)
sys.path.insert(0, VERIFY)
assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停"

import numpy as np                                           # noqa: E402

NODE_CAP = 400000                    # 🔒 節點上限（沿用 `W-G.9-305R` 之值·器內明文·出艙）
SIDE_VOCAB = {"left", "right", "左側", "右側", "L", "R"}
SIDE_L = {"left", "左側", "L"}
SIDE_R = {"right", "右側", "R"}
SIDE_MAP = {"left": "L", "right": "R", "左側": "L", "右側": "R", "無": "無"}
BLK_KEYS = ["blk_label", "_lbl", "blk", "lbl", "label", "_blk"]

SEQ = [0]
ENTRY = [0]                          # `_run_step_g_impl` 之進入序號
TRIG = {"cbs": 0, "sgo": 0, "fcad": 0, "impl": 0}
P = []                               # 產出集
CALLS = []                           # 強制呼叫逐次
ROWS = []                            # 逐次判定
LOUD = []


class _ProbeMark:
    """🔑 器所擁有之物之標記——用以機驗『命中路徑經過器之物者』欄**⛔ 恆為 `0`**。"""

    def __init__(self, payload):
        self.payload = payload


class _SlotBox:
    """🔑 `T3` 之根：具 `__slots__` 而**⛔ 有 `__dict__`** 之器內類 ⇒ 其走訪須經 `R6`。"""

    __slots__ = ("payload",)

    def __init__(self, payload):
        self.payload = payload


def canon(s):
    return SIDE_MAP.get(str(s).strip(), "?<%r>" % (s,))


def chain(depth=40):
    out, f = [], sys._getframe(2)
    while f is not None and len(out) < depth:
        c = f.f_code
        rel = os.path.relpath(c.co_filename, REPO).replace("\\", "/") \
            if os.path.abspath(c.co_filename).startswith(REPO) else c.co_filename
        out.append((rel, c.co_name, c.co_firstlineno))
        if rel.endswith("verify/run_verification.py"):
            break
        f = f.f_back
    return out


def find_blk():
    f = sys._getframe(2)
    while f is not None:
        L = f.f_locals
        for k in BLK_KEYS:
            if k in L and isinstance(L[k], str) and L[k]:
                return (L[k], k, [x for x in BLK_KEYS if x in L and x != k], f.f_code.co_name)
        f = f.f_back
    return (None, None, [], None)


def vec2(o):
    """`R0` ①② 之候選葉 ⇒ 回 (hex0, hex1)；否則 None。"""
    try:
        if isinstance(o, (tuple, list)) and len(o) == 2 \
                and all(isinstance(x, float) for x in o):
            return (o[0].hex(), o[1].hex())
        if isinstance(o, np.ndarray) and o.size == 2 and o.dtype.kind == "f":
            a = o.reshape(-1)
            return (float(a[0]).hex(), float(a[1]).hex())
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("vec2 例外：%r" % (e,))
    return None


def transforms(h):
    """四變換（座標分量之逐字式·⛔ 以「左轉／右轉」代之）。"""
    x, y = float.fromhex(h[0]), float.fromhex(h[1])
    return {"(x,y)": (x, y), "(-x,-y)": (-x, -y), "(-y,x)": (-y, x), "(y,-x)": (y, -x)}


# `R2` ⛔ 穿越（數出艙）
SKIP_T = (types.ModuleType, type, types.FunctionType, types.BuiltinFunctionType,
          types.MethodType, types.CodeType, types.FrameType, types.GeneratorType)
# `R1` 葉
LEAF_T = (str, bytes, bytearray, int, float, bool, complex, type(None))


def _slots_of(tp):
    """`type(o)` 之 MRO 上各 `__slots__` 所列之槽（逐字·保序·去重）。"""
    out = []
    for c in tp.__mro__:
        s = c.__dict__.get("__slots__")
        if not s:
            continue
        if isinstance(s, str):
            s = [s]
        for nm in s:
            if nm not in out:
                out.append(nm)
    return out


def walk_roots(roots, targets, cap=NODE_CAP, rootset="?"):
    """走訪一根集；回 dict（hits／trunc／opaque／skipped／excs／nodes／root_rules）。

    🔒 規則 `R0`〜`R7` **依序判定·先中者即止**（單 `§五-2`）。
    `targets` ＝ [{'key':(blk,side_norm),'hex':(h0,h1),'p':P筆}]；比對於四變換下**逐分量位元相等**。
    """
    hits, opaque, skipped, excs = [], {}, {}, []
    seen = set()                     # 🔒 `id(·)` 僅用於本次走訪之已訪集合（⛔ 出艙）
    nodes = [0]
    trunc = [False]
    idx = {}
    for t in targets:
        for tn, (a, b) in transforms(t["hex"]).items():
            idx.setdefault((a.hex(), b.hex()), []).append((t, tn))

    def emit(vpair, path, marked):
        for t, tn in idx.get(vpair, []):
            hits.append({"path": list(path), "tf": tn, "p": t["p"],
                         "key": t["key"], "marked": marked, "rootset": rootset})

    def rec(o, path, marked):
        """回其所**適用之規則**（字串）——供根型別自證出艙。"""
        if nodes[0] >= cap:
            trunc[0] = True
            return "cap"
        nodes[0] += 1
        if isinstance(o, _ProbeMark):
            marked = True

        # ── `R0` 候選葉 ①② ────────────────────────────────────────────
        v = vec2(o)
        if v is not None:
            emit(v, path, marked)
            return "R0①②"
        # ── `R0` ③ 浮點 `ndarray` 之 `ndim ≥ 2` ⋀ `shape[-1] == 2` ────
        if isinstance(o, np.ndarray) and o.dtype.kind == "f" \
                and o.ndim >= 2 and o.shape[-1] == 2:
            try:
                rows = o.reshape(-1, 2)
                for i in range(rows.shape[0]):
                    emit((float(rows[i, 0]).hex(), float(rows[i, 1]).hex()),
                         path + ["<列%d>" % i], marked)
            except Exception as e:                            # noqa: BLE001
                excs.append({"path": "/".join(map(str, path[:6])),
                             "exc": repr(e), "rootset": rootset})
            return "R0③"

        # ── `R1` 葉 ──────────────────────────────────────────────────
        if isinstance(o, LEAF_T):
            return "R1"
        if isinstance(o, np.ndarray) and o.dtype.kind != "O":
            return "R1"
        if (type(o).__module__ or "").startswith("shapely"):
            return "R1"

        # ── `R2` ⛔ 穿越（數出艙）─────────────────────────────────────
        if isinstance(o, SKIP_T):
            skipped[type(o).__name__] = skipped.get(type(o).__name__, 0) + 1
            return "R2"

        if id(o) in seen:
            return "已訪"
        seen.add(id(o))

        try:
            tp = type(o)
            mod = tp.__module__ or ""
            tnm = tp.__name__

            # ── `R3` `pandas` ────────────────────────────────────────
            if mod.startswith("pandas") and tnm in ("DataFrame", "Series"):
                for n, val in enumerate(list(o.to_numpy().reshape(-1))):
                    rec(val, path + ["<pd[%d]>" % n], marked)
                return "R3"

            # ── `R4` 映射協定（🔒 以 `type(o)` 檢·⛔ 以實例屬性）──────
            if hasattr(tp, "keys") and hasattr(tp, "__getitem__"):
                for k in list(o.keys()):
                    rec(k, path + ["<key:%r>" % (k,)], marked)
                    rec(o[k], path + [repr(k)], marked)
                return "R4"

            # ── `R5` 迭代容器 ────────────────────────────────────────
            if isinstance(o, (list, tuple, set, frozenset, collections.deque)):
                for n, val in enumerate(list(o)):
                    rec(val, path + ["[%d]" % n], marked)
                return "R5"
            if isinstance(o, np.ndarray) and o.dtype.kind == "O":
                for n, val in enumerate(o.reshape(-1).tolist()):
                    rec(val, path + ["[obj%d]" % n], marked)
                return "R5"

            # ── `R6` 屬性（`__dict__` ＋ MRO 上之 `__slots__`）────────
            touched = False
            d = getattr(o, "__dict__", None)
            if isinstance(d, dict):
                rec(d, path + [".__dict__"], marked)
                touched = True
            for nm in _slots_of(tp):
                try:
                    val = getattr(o, nm)
                except AttributeError:
                    continue                                  # 缺槽略之
                rec(val, path + ["." + nm], marked)
                touched = True
            if touched:
                return "R6"

            # ── `R7` 殘餘 ⇒ `gc.get_referents`（唯讀）─────────────────
            refs = gc.get_referents(o)
            if not refs:
                key = "%s.%s" % (mod, tnm)
                if key not in opaque:
                    opaque[key] = [0, list(path), rootset]
                opaque[key][0] += 1
                return "R7-不透明"
            for i, val in enumerate(refs):
                rec(val, path + ["<ref:%d>" % i], marked)
            return "R7"
        except Exception as e:                                # noqa: BLE001
            excs.append({"path": "/".join(map(str, path[:6])),
                         "exc": repr(e), "rootset": rootset})
            return "例外"

    root_rules = {}
    for nm, r in roots:
        root_rules[nm] = rec(r, [nm], False)
    return {"hits": hits, "trunc": trunc[0], "opaque": opaque, "skipped": skipped,
            "excs": excs, "nodes": nodes[0], "root_rules": root_rules}


def trusted(hits, blk, side):
    """鍵口徑可信 ＝ 路徑之鍵鏈同時具該街廓與該側之字樣。"""
    n = 0
    voc = SIDE_L if side == "L" else SIDE_R if side == "R" else set()
    for h in hits:
        ks = [str(x).strip("'\"<>key: ") for x in h["path"]]
        if any(x == blk for x in ks) and any(any(w == x for w in voc) for x in ks):
            n += 1
    return n


ORIG = {}
CUR_SGO = {}


def wrap(ns):
    if getattr(ns.get("_corner_buffer_S"), "_wg9306", False):
        return ns
    cbs, sgo, fcad = ns["_corner_buffer_S"], ns["_solve_G_one"], ns["_first_corner_alloc_dir"]
    ORIG["cbs"] = cbs
    ORIG["ns"] = ns

    def fcad2(side_mid):
        TRIG["fcad"] += 1
        SEQ[0] += 1
        r = fcad(side_mid)
        sd, ic = CUR_SGO.get("side"), CUR_SGO.get("is_corner")
        blk, key, others, fn = find_blk()
        h = vec2(tuple(float(x) for x in np.asarray(r, dtype=float).reshape(-1)[:2]))
        P.append({"src": "①_first_corner_alloc_dir", "seq": SEQ[0], "entry": ENTRY[0] or "外",
                  "blk": blk, "key": key, "others": others, "fn": fn,
                  "side_raw": sd, "side": canon(sd), "is_corner": ic,
                  "hex": h, "ctx": chain()})
        return r
    fcad2._wg9306 = True

    def sgo2(*a, **kw):
        TRIG["sgo"] += 1
        SEQ[0] += 1
        prev = dict(CUR_SGO)
        CUR_SGO["side"], CUR_SGO["is_corner"] = kw.get("side"), kw.get("is_corner")
        try:
            r = sgo(*a, **kw)
        finally:
            CUR_SGO.clear()
            CUR_SGO.update(prev)
        if kw.get("is_corner"):
            SEQ[0] += 1
            used = None
            try:
                used = r[0].get("_alloc_dir_used") if isinstance(r, tuple) else None
            except Exception as e:                            # noqa: BLE001
                LOUD.append("讀 `_alloc_dir_used` 例外：%r" % (e,))
            blk, key, others, fn = find_blk()
            h = None
            if used is not None:
                h = vec2(tuple(float(x) for x in used[:2]))
            P.append({"src": "②_solve_G_one._alloc_dir_used", "seq": SEQ[0],
                      "entry": ENTRY[0] or "外", "blk": blk, "key": key, "others": others,
                      "fn": fn, "side_raw": kw.get("side"), "side": canon(kw.get("side")),
                      "is_corner": True, "hex": h, "ctx": chain()})
        return r
    sgo2._wg9306 = True

    def cbs2(*a, **kw):
        TRIG["cbs"] += 1
        SEQ[0] += 1
        seq = SEQ[0]
        f = sys._getframe(1)
        c = f.f_code
        rel = os.path.relpath(c.co_filename, REPO).replace("\\", "/")
        blk_f, key, others, fn = find_blk()
        lab = kw.get("_label", a[7] if len(a) > 7 else "")
        side_raw = kw.get("side", a[5] if len(a) > 5 else None)
        rec = {"seq": seq, "entry": ENTRY[0] or "外", "label": lab,
               "blk_frame": blk_f, "key": key, "others": others,
               "side_raw": side_raw, "side": canon(side_raw),
               "caller": (rel, c.co_name, c.co_firstlineno)}
        if c.co_name != "_run_step_g_impl":
            LOUD.append("強制呼叫端之 `co_name` ≠ `_run_step_g_impl`：%r（seq %d）"
                        % (c.co_name, seq))
        CALLS.append(rec)
        _measure(seq, rec, a, kw, f)
        return cbs(*a, **kw)
    cbs2._wg9306 = True

    ns["_corner_buffer_S"], ns["_solve_G_one"], ns["_first_corner_alloc_dir"] = cbs2, sgo2, fcad2
    return ns


def _measure(seq, rec, a, kw, frame):
    blk = rec["blk_frame"] or str(rec["label"]).split("·")[0]
    side = rec["side"]
    same = [p for p in P if p["seq"] < seq and p["hex"] is not None
            and p["blk"] == blk and p["side"] == side]
    other = [p for p in P if p["seq"] < seq and p["hex"] is not None
             and not (p["blk"] == blk and p["side"] == side)]
    tg_same = [{"key": (p["blk"], p["side"]), "hex": p["hex"], "p": p} for p in same]
    tg_other = [{"key": (p["blk"], p["side"]), "hex": p["hex"], "p": p} for p in other]

    orig = ORIG["cbs"]
    g_is_ns = orig.__globals__ is ORIG["ns"]
    params = ["block_poly", "d_hat", "front_p1", "allocation_dir", "range_area",
              "side", "tol", "_label"]
    body_roots = [("(體)形參[%d]%s" % (i, params[i]), a[i]) for i in range(len(a))]
    for k, v in kw.items():
        body_roots.append(("(體)形參kw:%s" % k, v))
    body_roots.append(("(體)__globals__", orig.__globals__))
    end_roots = [("(端)f_locals", frame.f_locals), ("(端)f_globals", frame.f_globals)]

    out = {}
    for tag, roots in (("體", body_roots), ("端", end_roots)):
        rs = walk_roots(roots, tg_same, rootset=tag)
        ro = walk_roots(roots, tg_other, rootset=tag)
        opq = dict(rs["opaque"])
        for k, v in ro["opaque"].items():
            if k not in opq:
                opq[k] = v
            else:
                opq[k] = [opq[k][0] + v[0], opq[k][1], opq[k][2]]
        out[tag] = {
            "same": rs["hits"], "other": ro["hits"],
            "trunc": bool(rs["trunc"] or ro["trunc"]),
            "opaque": opq,
            "excs": rs["excs"] + ro["excs"],
            "skipped": {k: rs["skipped"].get(k, 0) + ro["skipped"].get(k, 0)
                        for k in set(list(rs["skipped"]) + list(ro["skipped"]))},
            "nodes": rs["nodes"] + ro["nodes"],
            "root_rules": rs["root_rules"],
        }

    ROWS.append({
        "seq": seq, "entry": rec["entry"], "blk": blk, "side": side,
        "side_raw": rec["side_raw"],
        "P同": {"同進入序號": len([p for p in same if p["entry"] == rec["entry"]]),
                "前進入序號": len([p for p in same if p["entry"] != rec["entry"] and p["entry"] != "外"]),
                "外": len([p for p in same if p["entry"] == "外"])},
        "體": {"同": len(out["體"]["same"]), "他": len(out["體"]["other"]),
               "可信": trusted(out["體"]["same"], blk, side),
               "截斷": out["體"]["trunc"], "例外": len(out["體"]["excs"]),
               "不透明": out["體"]["opaque"], "nodes": out["體"]["nodes"],
               "hits": out["體"]["same"], "skipped": out["體"]["skipped"]},
        "端": {"同": len(out["端"]["same"]), "他": len(out["端"]["other"]),
               "可信": trusted(out["端"]["same"], blk, side),
               "截斷": out["端"]["trunc"], "例外": len(out["端"]["excs"]),
               "不透明": out["端"]["opaque"], "nodes": out["端"]["nodes"],
               "hits": out["端"]["same"], "skipped": out["端"]["skipped"]},
        "器自身": len([h for h in out["體"]["same"] + out["端"]["same"] if h["marked"]]),
        "端根規則": out["端"]["root_rules"],
        "g_is_ns": g_is_ns,
    })


import run_verification as RV                                 # noqa: E402
import stepg_pipeline as SP                                   # noqa: E402

_impl = SP._run_step_g_impl


def impl2(*a, **kw):
    TRIG["impl"] += 1
    ENTRY[0] = TRIG["impl"]
    try:
        return _impl(*a, **kw)
    finally:
        ENTRY[0] = 0


if not getattr(SP._run_step_g_impl, "_wg9306", False):
    impl2._wg9306 = True
    SP._run_step_g_impl = impl2

_orig_h = RV.harvest


def harvest2():
    ns, fs = _orig_h()
    return wrap(ns), fs


RV.harvest = harvest2

BAR = "=" * 116
print(BAR)
print("【`W-G.9-306` `§五` 可達性二根集之重測】`run_verification` 全量**一次**")
print("節點上限（器內明文·沿用 `W-G.9-305R`）＝ %d／走訪" % NODE_CAP)
print("走訪規則 ＝ `R0`〜`R7`（**依序判定·先中者即止**）；容器**依協定**；殘餘以 `gc.get_referents` 穿越")
print(BAR)
sys.stdout.flush()

# ══════════════════════════════════════════════════════════════════════
# `§五-3`　款 `3'`：**根型別自證**（🛑 長跑**前**·任一不命中 ⇒ 停、⛔ 啟動長跑）
# ══════════════════════════════════════════════════════════════════════
print("\n── `§五-3`　款 `3'`　根型別自證（**長跑前**·同一直譯器·**真實同型物**）──")
print("直譯器 ＝ %s" % sys.version.replace("\n", " "))
SELFTEST = []
_V = (1.0 / 3.0, -2.0 / 7.0)     # 🔒 **合成之浮點對**（執行期算出·⛔ 取自 baseline·⛔ 任何域值）
_TG = [{"key": ("R4", "L"), "hex": (_V[0].hex(), _V[1].hex()), "p": {"seq": -1, "entry": "自證",
                                                                    "blk": "R4", "side": "L"}}]


def _t_report(name, root_desc, res, need_hit, want_rule):
    hs = res["hits"]
    ok = (len(hs) >= 1) if need_hit else (len(hs) == 0)
    rule = list(res["root_rules"].values())[0] if res["root_rules"] else "—"
    if want_rule is not None and need_hit:
        ok = ok and (rule == want_rule)
    SELFTEST.append((name, ok))
    print("   %-4s 根型別 ＝ `%s`｜所經規則 ＝ `%s`（期 `%s`）｜同命中 %d（期 %s）⇒ %s"
          % (name, root_desc, rule, want_rule if want_rule else "—",
             len(hs), "≥ 1" if need_hit else "0", "✅" if ok else "🔴"))
    for h in hs[:3]:
        print("        命中路徑 ＝ %s｜變換 ＝ %s" % ("/".join(map(str, h["path"])), h["tf"]))


_T1_TYPE = [None]


def _t1(targets, val):
    """`T1`：器內一函式執行中之 `sys._getframe().f_locals`（**真實框**·⛔ 合成 `dict`）。"""
    _planted_candidate_value = val                            # 該函式之區域名綁一候選值
    fl = sys._getframe().f_locals
    _T1_TYPE[0] = type(fl).__name__
    print("   `T1`／`T5` 之根 `type(·).__name__` ＝ `%s`（`isinstance(·, dict)` ＝ %s）"
          % (type(fl).__name__, isinstance(fl, dict)))
    return walk_roots([("(自證)T1_f_locals", fl)], targets, rootset="自證")


_t1res = _t1(_TG, _V)
_t_report("T1", _T1_TYPE[0], _t1res, True, "R4")

# `T2`：`verify/app_harvest.py` 之 `_FakeStreamlit` 之一新實例
from app_harvest import _FakeStreamlit                        # noqa: E402
_fs = _FakeStreamlit()
_fs.session_state["__wg9306_probe_key__"] = _V
_tp = type(_fs)
print("   `T2` 之 `type(o)` 檢：`hasattr(type,'keys')` ＝ %s／`hasattr(type,'__getitem__')` ＝ %s"
      "　｜**實例**屬性之對照：`hasattr(inst,'keys')` ＝ %s／`hasattr(inst,'__getitem__')` ＝ %s"
      % (hasattr(_tp, "keys"), hasattr(_tp, "__getitem__"),
         hasattr(_fs, "keys"), hasattr(_fs, "__getitem__")))
_t2res = walk_roots([("(自證)T2_FakeStreamlit", _fs)], _TG, rootset="自證")
_t2rule = list(_t2res["root_rules"].values())[0]
print("   🔑 `T2` **須證其⛔ 誤入 `R4`**：所經規則 ＝ `%s` ⇒ %s"
      % (_t2rule, "✅ ⛔ 誤入" if _t2rule != "R4" else "🔴 **誤入 `R4`**"))
SELFTEST.append(("T2-⛔誤入R4", _t2rule != "R4"))
_t_report("T2", type(_fs).__name__, _t2res, True, "R6")

# `T3`：一具 `__slots__`（⛔ 有 `__dict__`）之器內類之實例
_sb = _SlotBox(_V)
print("   `T3` 之根 `hasattr(o,'__dict__')` ＝ %s（須 `False`）｜`__slots__` ＝ %s"
      % (hasattr(_sb, "__dict__"), _slots_of(type(_sb))))
_t_report("T3", type(_sb).__name__, walk_roots([("(自證)T3_SlotBox", _sb)], _TG, rootset="自證"),
          True, "R6")

# `T4`：一 `shape == (3, 2)` 之浮點 `ndarray`，植入其第 `2` 列
_arr = np.zeros((3, 2), dtype=float)
_arr[1, 0], _arr[1, 1] = _V[0], _V[1]
print("   `T4` 之根 `shape` ＝ %s／`dtype.kind` ＝ `%s`／`ndim` ＝ %d（植於第 `2` 列 ＝ index `1`）"
      % (_arr.shape, _arr.dtype.kind, _arr.ndim))
_t_report("T4", "ndarray(3,2)", walk_roots([("(自證)T4_ndarray", _arr)], _TG, rootset="自證"),
          True, "R0③")

# `T5`：同 `T1`，惟植入值以 `numpy.nextafter` 擾動一分量 ⇒ 同命中須 `0`
_pert = (float(np.nextafter(_V[0], np.inf)), _V[1])
print("   `T5` 之擾動：`x` 由 `%s` ⇒ `%s`（`numpy.nextafter`·一 ULP）"
      % (_V[0].hex(), _pert[0].hex()))
_t5res = _t1(_TG, _pert)
_t_report("T5", _T1_TYPE[0], _t5res, False, None)

_bad = [n for n, ok in SELFTEST if not ok]
print("\n🔑 **根型別自證之判**：%s（%d 造／不如預期 %s）"
      % ("✅ 全綠 ⇒ 准啟動長跑" if not _bad else "🔴 **不綠 ⇒ 停、⛔ 啟動長跑**",
         len(SELFTEST), _bad if _bad else "無"))
if _bad:
    print(BAR)
    print("🛑 **停**：根型別自證未全綠 ⇒ ⛔ 啟動長跑（單 `§五-3` 明文）。⛔ 自擴規則、⛔ 自調上限。")
    print(BAR)
    sys.stdout.flush()
    raise SystemExit(3)
sys.stdout.flush()

# ══════════════════════════════════════════════════════════════════════
# 長跑（`run_verification` 全量**一次**）
# ══════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("根型別自證全綠 ⇒ 啟動長跑（`run_verification.main()`）")
print(BAR)
sys.stdout.flush()

try:
    rc = RV.main()
except SystemExit as e:
    rc = e.code
except Exception as e:                                        # noqa: BLE001
    rc = "EXC: %r" % (e,)

print("\n" + BAR)
print("`run_verification.main()` 之 rc = %r" % (rc,))
print("三包裝與進入序號計數器之觸發數[必非零]：`_corner_buffer_S` %d ／ `_solve_G_one` %d ／ "
      "`_first_corner_alloc_dir` %d ／ `_run_step_g_impl` %d"
      % (TRIG["cbs"], TRIG["sgo"], TRIG["fcad"], TRIG["impl"]))
if min(TRIG.values()) == 0:
    print("🔴 **loud：有包裝之觸發數為 `0` ⇒ 判器紅、停**")
print(BAR)

# ── 五-1 款 `1`（承用·⛔ 改其受詞）────────────────────────────────────
print("\n── 款 `1`　產出集 `P`（全量 %d 筆）──" % len(P))
n1 = len([p for p in P if p["src"].startswith("①")])
n2 = len([p for p in P if p["src"].startswith("②")])
print("   ① `_first_corner_alloc_dir` 之回傳 ＝ **%d** 筆／② `_solve_G_one` 之 `_alloc_dir_used`"
      "（`is_corner` 真）＝ **%d** 筆" % (n1, n2))
print("   ①⊆② 之歸屬分布（⛔ 預設其關係）：① 之 (街廓,側) 集 = %s ／ ② 之 = %s"
      % (sorted({(p["blk"], p["side"]) for p in P if p["src"].startswith("①")}, key=str),
         sorted({(p["blk"], p["side"]) for p in P if p["src"].startswith("②")}, key=str)))
print("   `hex` 為 `None` 者 ＝ %d 筆（⛔ 入比對之 targets）"
      % len([p for p in P if p["hex"] is None]))
print("   街廓之命中鍵分布 ＝ %s ／ 第二鍵 ＝ %s"
      % (sorted({p["key"] for p in P if p["key"]}),
         sorted({x for p in P for x in p["others"]})))
print("\n   （前 4 筆·全量之引用見逐次判定表）")
for p in P[:4]:
    print("   seq=%-5s entry=%-4s %-30s blk=%-6r side=%r⇒%s hex=%s"
          % (p["seq"], p["entry"], p["src"], p["blk"], p["side_raw"], p["side"], p["hex"]))
    print("        ctx=%s" % (p["ctx"][:4],))

# ── 五-1 款 `2`（承用）────────────────────────────────────────────────
print("\n── 款 `2`　逐次強制呼叫（全量 %d 次·⛔ 抽樣）──" % len(CALLS))
print("| seq | entry | `_label` 逐字 | 呼叫端框之街廓鍵 | side 實參 | 呼叫端 (檔, co_name, co_firstlineno) |")
print("|---|---|---|---|---|---|")
for c in CALLS:
    print("| %d | %s | %r | %r（鍵 `%s`） | %r | %r |"
          % (c["seq"], c["entry"], c["label"], c["blk_frame"], c["key"], c["side_raw"], c["caller"]))
_bad_caller = [c for c in CALLS if c["caller"][1] != "_run_step_g_impl"]
print("   `co_name ≠ _run_step_g_impl` 者 ＝ **%d** 次" % len(_bad_caller))

# ── `§五-4`　款 `4` 判定表（全量·逐次·**二根集分列**）────────────────
print("\n── `§五-4`　款 `4`　逐次判定表（全量 %d 列·**二根集分列**）──" % len(ROWS))
print("| seq | entry | 街廓 | 側 | `\\|P同\\|` 同/前/外 | (體)同/他 | (體)可信 | (體)截斷 | (體)例外 | (體)不透明 |"
      " (端)同/他 | (端)可信 | (端)截斷 | (端)例外 | (端)不透明 | 器自身 | nodes |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in ROWS:
    b, e = r["體"], r["端"]
    print("| %d | %s | %s | %s | %d/%d/%d | %d/%d | %d | %s | %d | %d | %d/%d | %d | %s | %d | %d | %d | %d |"
          % (r["seq"], r["entry"], r["blk"], r["side"],
             r["P同"]["同進入序號"], r["P同"]["前進入序號"], r["P同"]["外"],
             b["同"], b["他"], b["可信"], b["截斷"], b["例外"], len(b["不透明"]),
             e["同"], e["他"], e["可信"], e["截斷"], e["例外"], len(e["不透明"]),
             r["器自身"], b["nodes"] + e["nodes"]))

print("\n   `__globals__ is ns`（以 `is` 判·⛔ 出艙 `id`）⇒ %s"
      % sorted({r["g_is_ns"] for r in ROWS}))
print("   (端) 根之所經規則（逐次·**⛔ 合併**）⇒ %s"
      % sorted({(k, v) for r in ROWS for k, v in r["端根規則"].items()}))

# ── 不透明登記（**全量·二根集分列**）─────────────────────────────────
print("\n── 🛑 **不透明登記**（`R7` 之 `gc.get_referents` 為空者·**二根集分列**·型別名／次數／首見路徑）──")
for tag in ("體", "端"):
    agg = {}
    for r in ROWS:
        for k, v in r[tag]["不透明"].items():
            if k not in agg:
                agg[k] = [0, v[1]]
            agg[k][0] += v[0]
    print("   **(%s)** 不透明型別數 ＝ %d" % (tag, len(agg)))
    for k, v in sorted(agg.items()):
        print("      - `%s`　次數 %d　首見路徑 ＝ %s" % (k, v[0], "/".join(map(str, v[1]))))
    if not agg:
        print("      （無）⛔ 讀為「無異常」")

# ── 走訪例外（**全量·二根集分列**）───────────────────────────────────
print("\n── 🛑 **走訪例外**（**二根集分列**·路徑／例外逐字）──")
for tag in ("體", "端"):
    tot = sum(r[tag]["例外"] for r in ROWS)
    print("   **(%s)** 走訪例外合計 ＝ %d" % (tag, tot))
if sum(r["體"]["例外"] + r["端"]["例外"] for r in ROWS) == 0:
    print("   （二根集皆無走訪例外）⛔ 讀為「無異常」")

# ── ⛔穿越之型別計數（`R2`）──────────────────────────────────────────
allsk = {}
for r in ROWS:
    for tag in ("體", "端"):
        for k, v in r[tag]["skipped"].items():
            allsk[k] = allsk.get(k, 0) + v
print("\n   `R2` ⛔穿越之型別計數（module／type／函式・方法・code・frame・generator）⇒ %s"
      % dict(sorted(allsk.items())))

# ── 命中之路徑（凡同命中 ≥ 1 者·**全部**逐字·⛔ 截取）────────────────
print("\n── 命中之路徑（凡同命中 `≥ 1` 者，其**全部**命中逐字·⛔ 截取）──")
anyhit = False
for r in ROWS:
    for tag in ("體", "端"):
        for h in r[tag]["hits"]:
            anyhit = True
            print("   seq=%d (%s) 變換=%s 路徑=%s ⇒ 命中 P 筆(seq=%s, entry=%s, blk=%r, side=%s)"
                  % (r["seq"], tag, h["tf"], "/".join(map(str, h["path"])),
                     h["p"]["seq"], h["p"]["entry"], h["p"]["blk"], h["p"]["side"]))
if not anyhit:
    print("   🛑 **loud：全量走訪之同命中 ＝ `0`（二根集皆然）**")

# ── 五-1 款 `5` 判別力造（承用）───────────────────────────────────────
print("\n── 款 `5`　判別力造（承用 `W-G.9-305 §六-2` 款 `5`）──")
import subprocess                                             # noqa: E402
cp = subprocess.run(["git", "ls-tree", "HEAD", "--name-only", "verify/"],
                    capture_output=True, cwd=REPO)
prod = [x for x in cp.stdout.decode("utf-8", "surrogateescape").splitlines()
        if x.endswith(".py")] + ["app.py"]
print("   [必為 `34`] 外部錨（坑 `bj`）⇒ %d ⇒ %s" % (len(prod), "✅" if len(prod) == 34 else "🔴"))

cand = [p for p in P if p["hex"] is not None and p["blk"]]
if not cand:
    print("   🛑 **loud：`P` 中無可用之筆 ⇒ 合成根與 nextafter 二造之判定組為空 ⇒ 拒測**")
else:
    q = cand[0]
    _sd = "left" if q["side"] == "L" else "right"
    _pay = {q["blk"]: {_sd: tuple(float.fromhex(x) for x in q["hex"])}}
    syn_root = {q["blk"]: {_sd: tuple(float.fromhex(x) for x in q["hex"])},
                "__probe_record__": _ProbeMark(_pay)}
    tg = [{"key": (q["blk"], q["side"]), "hex": q["hex"], "p": q}]
    rr = walk_roots([("(合成根)", syn_root)], tg, rootset="造")
    hs = rr["hits"]
    tn = trusted(hs, q["blk"], q["side"])
    print("   [必命中] 合成根 ⇒ 同命中 %d（須 ≥ 1）／鍵口徑可信 %d（須 ≥ 1）⇒ %s"
          % (len(hs), tn, "✅" if (hs and tn) else "🔴"))
    print("   [器自身之判別力] 合成根內刻意置入器之記錄容器 ⇒ marked 命中 %d（須 ≥ 1）⇒ %s"
          % (len([h for h in hs if h["marked"]]),
             "✅" if [h for h in hs if h["marked"]] else "🔴"))
    x0 = float.fromhex(q["hex"][0])
    pert = np.nextafter(x0, np.inf)
    tg2 = [{"key": (q["blk"], q["side"]), "hex": (float(pert).hex(), q["hex"][1]), "p": q}]
    hs2 = walk_roots([("(合成根)", syn_root)], tg2, rootset="造")["hits"]
    print("   [必為零] `numpy.nextafter` 擾動一分量 ⇒ 同命中 %d（須 0）⇒ %s"
          % (len(hs2), "✅" if not hs2 else "🔴"))
print("   [必非零] 三包裝與進入序號計數器之觸發數 ⇒ %s ⇒ %s"
      % (dict(TRIG), "✅" if min(TRIG.values()) >= 1 else "🔴"))
print("   [器自身須 `0`] 實測各次之 marked 命中合計 ⇒ %d" % sum(r["器自身"] for r in ROWS))

# ── `§五-5`　停機款與不可判款（**逐次·逐根集分列**）──────────────────
print("\n── `§五-5`　停九（體）／停九（端）／停十／不可判款（**逐次·逐根集分列**）──")
print("| seq | 街廓 | 側 | **停九（體）** | **停九（端）** | **停十（體）** | **停十（端）** | **不可判（體）** | **不可判（端）** |")
print("|---|---|---|---|---|---|---|---|---|")
S9 = {"體": [], "端": []}
S10 = {"體": [], "端": []}
UND = {"體": [], "端": []}
for r in ROWS:
    cell = {}
    for tag in ("體", "端"):
        x = r[tag]
        s9 = (not x["截斷"]) and (x["例外"] == 0) and (x["同"] == 0)
        s10 = (x["同"] >= 1) and (x["可信"] == 0)
        un = (x["同"] == 0) and (bool(x["截斷"]) or x["例外"] > 0)
        if s9:
            S9[tag].append(r["seq"])
        if s10:
            S10[tag].append(r["seq"])
        if un:
            UND[tag].append(r["seq"])
        cell[tag] = (s9, s10, un)
    print("| %d | %s | %s | %s | %s | %s | %s | %s | %s |"
          % (r["seq"], r["blk"], r["side"],
             "🔴 成就" if cell["體"][0] else "✅",
             "🔴 成就" if cell["端"][0] else "✅",
             "🔴 成就" if cell["體"][1] else "✅",
             "🔴 成就" if cell["端"][1] else "✅",
             "🔴 成就" if cell["體"][2] else "✅",
             "🔴 成就" if cell["端"][2] else "✅"))

print("\n🛑 **停九（體）**（(體) 截斷 `0` ⋀ 走訪例外 `0` ⋀ 同命中 `0`）⇒ 成就之次 ＝ %s ⇒ **%s**"
      % (S9["體"], "🔴 成就" if S9["體"] else "✅ 不成就"))
print("🛑 **停九（端）**（受詞為 (端)·🔒 **資訊性**·`§零-2` 裁 `4`）⇒ 成就之次 ＝ %s ⇒ **%s**"
      % (S9["端"], "🔴 成就" if S9["端"] else "✅ 不成就"))
for tag in ("體", "端"):
    print("🛑 **停十（%s）**（同命中 `≥ 1` ⋀ 鍵口徑可信 `0`）⇒ 成就之次 ＝ %s ⇒ **%s**"
          % (tag, S10[tag], "🔴 成就" if S10[tag] else
             ("✅ 不成就（判定組為空：無一次之同命中 ≥ 1）"
              if not any(r[tag]["同"] >= 1 for r in ROWS) else "✅ 不成就")))
for tag in ("體", "端"):
    print("🛑 **不可判款（%s）**（同命中 `0` ⋀（截斷 `>0` ⋁ 走訪例外 `>0`））⇒ 成就之次 ＝ %s ⇒ **%s**"
          % (tag, UND[tag], "🔴 成就 ⇒ 該根集該次⛔ 判停九" if UND[tag] else "✅ 不成就"))
print("🔒 **不透明登記非空者⛔ 阻停九之判定**（單 `§五-5` 逐字）——其逐型別具名見上；"
      "其型別可否持有候選值**由發單側裁**（⛔ CC 自判）。")

print("\n── 🛑 loud 之全量 ──")
if not LOUD:
    print("   （無記錄）⛔ 讀為「無異常」")
for m in sorted(set(LOUD)):
    print("   - %s   ×%d" % (m, LOUD.count(m)))

print("\n" + BAR)
print("【本器⛔ 判落點·⛔ 判可施與否·⛔ 擬任何改法或 diff·⛔ 判不透明型別可否持值】")
print(BAR)
