"""`W-G.9-305` `§六`：已算之向於強制呼叫點之**可達性**現查（二根集·值空間·`run_verification` 全量一次）。

🔒 授權三手段（單 `§六` 首段逐字）：① `run_verification` 全量**一次**；② 於 `verify/probes/` 新增量測器＋落檔；
   ③ **於行程內包裝**（⛔ 動任何檔·**冪等**）`ns` 之三鍵 `_corner_buffer_S`／`_solve_G_one`／`_first_corner_alloc_dir`，
   及模組 `verify/stepg_pipeline.py` 之屬性 `_run_step_g_impl`（**僅供計其進入序號**）。
🛑 ⛔ 改生產碼一字、⛔ 自寫第二套幾何（**只比對既有之值**·⛔ 重算任何向）、⛔ 判落點、⛔ 判可施。
🛑 `id(·)` **僅准**作單次走訪內之已訪集合（⛔ 出艙·⛔ 作錨）。
🛑 未列於穿越／⛔穿越／葉 三表之型別 ⇒ **「未穿越」登記**（型別名·次數·首見路徑）——此即本款之構造上窮舉。
"""
import os
import sys
import types

sys.stdout.reconfigure(encoding="utf-8", newline="\n")      # 坑 `bn`：`newline` ⛔ 可省

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
SELF = os.path.abspath(__file__)
sys.path.insert(0, VERIFY)
assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停"

import numpy as np                                           # noqa: E402

NODE_CAP = 400000                    # 🔒 節點上限（器內明文·出艙）
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
    """候選葉 ⇒ 回 (hex0, hex1)；否則 None。"""
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


SKIP_T = (types.ModuleType, type, types.FunctionType, types.BuiltinFunctionType,
          types.MethodType, types.CodeType, types.FrameType, types.GeneratorType)
LEAF_T = (str, bytes, bytearray, int, float, bool, complex, type(None))


def walk_roots(roots, targets, cap=NODE_CAP):
    """走訪二根集之一；回 (hits, truncated, unvisited, skipped, nodes)。

    `targets` ＝ [{'key':(blk,side_norm),'hex':(h0,h1),'p':P筆}]；比對於四變換下**逐分量位元相等**。
    """
    hits, unvis, skipped = [], {}, {}
    seen = set()                     # 🔒 `id(·)` 僅用於本次走訪之已訪集合（⛔ 出艙）
    nodes = [0]
    trunc = [False]
    # 預建 hex → (target, 變換名) 之索引（四變換各存其 hex 對）
    idx = {}
    for t in targets:
        for tn, (a, b) in transforms(t["hex"]).items():
            idx.setdefault((a.hex(), b.hex()), []).append((t, tn))

    def rec(o, path, marked):
        if nodes[0] >= cap:
            trunc[0] = True
            return
        nodes[0] += 1
        if isinstance(o, _ProbeMark):
            marked = True
        v = vec2(o)
        if v is not None:
            for t, tn in idx.get(v, []):
                hits.append({"path": list(path), "tf": tn, "p": t["p"],
                             "key": t["key"], "marked": marked})
            return
        if isinstance(o, LEAF_T):
            return
        if isinstance(o, np.ndarray) and o.dtype.kind != "O":
            return
        if type(o).__module__.startswith("shapely"):
            return
        if isinstance(o, SKIP_T):
            skipped[type(o).__name__] = skipped.get(type(o).__name__, 0) + 1
            return
        if id(o) in seen:
            return
        seen.add(id(o))
        try:
            if isinstance(o, dict):
                for k, val in list(o.items()):
                    rec(k, path + ["<key:%r>" % (k,)], marked)
                    rec(val, path + [repr(k)], marked)
                return
            if isinstance(o, (list, tuple, set, frozenset)):
                for n, val in enumerate(list(o)):
                    rec(val, path + ["[%d]" % n], marked)
                return
            if isinstance(o, types.SimpleNamespace):
                rec(vars(o), path + [".__dict__"], marked)
                return
            if isinstance(o, np.ndarray) and o.dtype.kind == "O":
                for n, val in enumerate(o.reshape(-1).tolist()):
                    rec(val, path + ["[obj%d]" % n], marked)
                return
            tn = type(o).__name__
            mod = type(o).__module__ or ""
            if mod.startswith("pandas") and tn in ("DataFrame", "Series"):
                for n, val in enumerate(list(o.to_numpy().reshape(-1))):
                    rec(val, path + ["<pd[%d]>" % n], marked)
                return
            if isinstance(o, _ProbeMark):
                rec(o.payload, path + [".payload"], True)
                return
            d = getattr(o, "__dict__", None)
            if isinstance(d, dict):
                rec(d, path + [".__dict__"], marked)
                return
            key = "%s.%s" % (mod, tn)
            if key not in unvis:
                unvis[key] = [0, list(path)]
            unvis[key][0] += 1
        except Exception as e:                                # noqa: BLE001
            LOUD.append("走訪例外 @ %s：%r" % ("/".join(map(str, path[:6])), e))

    for nm, r in roots:
        rec(r, [nm], False)
    return hits, trunc[0], unvis, skipped, nodes[0]


def wrap(ns):
    if getattr(ns.get("_corner_buffer_S"), "_wg9305", False):
        return ns
    cbs, sgo, fcad = ns["_corner_buffer_S"], ns["_solve_G_one"], ns["_first_corner_alloc_dir"]
    ORIG["cbs"] = cbs
    ORIG["ns"] = ns

    def fcad2(side_mid):
        TRIG["fcad"] += 1
        SEQ[0] += 1
        r = fcad(side_mid)
        # ① 之側與 is_corner 取其所在之 `_solve_G_one` 呼叫之實參本身（⛔ climb f_locals）
        sd, ic = CUR_SGO.get("side"), CUR_SGO.get("is_corner")
        blk, key, others, fn = find_blk()
        h = vec2(tuple(float(x) for x in np.asarray(r, dtype=float).reshape(-1)[:2]))
        P.append({"src": "①_first_corner_alloc_dir", "seq": SEQ[0], "entry": ENTRY[0] or "外",
                  "blk": blk, "key": key, "others": others, "fn": fn,
                  "side_raw": sd, "side": canon(sd), "is_corner": ic,
                  "hex": h, "ctx": chain()})
        return r
    fcad2._wg9305 = True

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
    sgo2._wg9305 = True

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
    cbs2._wg9305 = True

    ns["_corner_buffer_S"], ns["_solve_G_one"], ns["_first_corner_alloc_dir"] = cbs2, sgo2, fcad2
    return ns


ORIG = {}
CUR_SGO = {}


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
        hs, tr, uv, sk, nd = walk_roots(roots, tg_same)
        ho, tro, uvo, sko, ndo = walk_roots(roots, tg_other)
        out[tag] = {"same": hs, "other": ho, "trunc": tr or tro,
                    "unvis": uv, "skipped": sk, "nodes": nd + ndo}

    def trusted(hits, blk, side):
        n = 0
        voc = SIDE_L if side == "L" else SIDE_R if side == "R" else set()
        for h in hits:
            ks = [str(x).strip("'\"<>key: ") for x in h["path"]]
            has_b = any(x == blk for x in ks)
            has_s = any(any(w == x for w in voc) for x in ks)
            if has_b and has_s:
                n += 1
        return n

    ROWS.append({
        "seq": seq, "entry": rec["entry"], "blk": blk, "side": side,
        "side_raw": rec["side_raw"],
        "P同": {"同進入序號": len([p for p in same if p["entry"] == rec["entry"]]),
                "前進入序號": len([p for p in same if p["entry"] != rec["entry"] and p["entry"] != "外"]),
                "外": len([p for p in same if p["entry"] == "外"])},
        "體同": len(out["體"]["same"]), "體他": len(out["體"]["other"]),
        "端同": len(out["端"]["same"]), "端他": len(out["端"]["other"]),
        "鍵可信": trusted(out["體"]["same"], blk, side) + trusted(out["端"]["same"], blk, side),
        "器自身": len([h for h in out["體"]["same"] + out["端"]["same"] if h["marked"]]),
        "截斷": out["體"]["trunc"] or out["端"]["trunc"],
        "未穿越": sorted(set(list(out["體"]["unvis"]) + list(out["端"]["unvis"]))),
        "skipped": {k: out["體"]["skipped"].get(k, 0) + out["端"]["skipped"].get(k, 0)
                    for k in set(list(out["體"]["skipped"]) + list(out["端"]["skipped"]))},
        "nodes": out["體"]["nodes"] + out["端"]["nodes"],
        "g_is_ns": g_is_ns,
        "hits體": out["體"]["same"][:4], "hits端": out["端"]["same"][:4],
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


if not getattr(SP._run_step_g_impl, "_wg9305", False):
    impl2._wg9305 = True
    SP._run_step_g_impl = impl2

_orig_h = RV.harvest


def harvest2():
    ns, fs = _orig_h()
    return wrap(ns), fs


RV.harvest = harvest2

BAR = "=" * 116
print(BAR)
print("【`W-G.9-305` `§六` 可達性量測器】`run_verification` 全量**一次**")
print("節點上限（器內明文）＝ %d／走訪" % NODE_CAP)
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

print("\n── 款 `1`　產出集 `P`（全量 %d 筆）──" % len(P))
n1 = len([p for p in P if p["src"].startswith("①")])
n2 = len([p for p in P if p["src"].startswith("②")])
print("   ① `_first_corner_alloc_dir` 之回傳 ＝ **%d** 筆／② `_solve_G_one` 之 `_alloc_dir_used`（`is_corner` 真）＝ **%d** 筆"
      % (n1, n2))
print("   ①⊆② 之歸屬分布（⛔ 預設其關係）：① 之 (街廓,側) 集 = %s ／ ② 之 = %s"
      % (sorted({(p["blk"], p["side"]) for p in P if p["src"].startswith("①")}, key=str),
         sorted({(p["blk"], p["side"]) for p in P if p["src"].startswith("②")}, key=str)))
print("   `hex` 為 `None` 者 ＝ %d 筆（⛔ 入比對之 targets）"
      % len([p for p in P if p["hex"] is None]))
print("   街廓之命中鍵分布 ＝ %s ／ 第二鍵 ＝ %s"
      % (sorted({p["key"] for p in P if p["key"]}),
         sorted({x for p in P for x in p["others"]})))
print("\n   （前 6 筆·全量見下表之引用）")
for p in P[:6]:
    print("   seq=%-5s entry=%-4s %-30s blk=%-6r side=%r⇒%s hex=%s"
          % (p["seq"], p["entry"], p["src"], p["blk"], p["side_raw"], p["side"], p["hex"]))
    print("        ctx=%s" % (p["ctx"][:4],))

print("\n── 款 `2`　逐次強制呼叫（全量 %d 次·⛔ 抽樣）──" % len(CALLS))
print("| seq | entry | `_label` 逐字 | 呼叫端框之街廓鍵 | side 實參 | 呼叫端 (檔, co_name, co_firstlineno) |")
print("|---|---|---|---|---|---|")
for c in CALLS:
    print("| %d | %s | %r | %r（鍵 `%s`） | %r | %r |"
          % (c["seq"], c["entry"], c["label"], c["blk_frame"], c["key"], c["side_raw"], c["caller"]))

print("\n── 款 `4`　逐次判定表（全量 %d 列）──" % len(ROWS))
print("| seq | entry | 街廓 | 側 | `\\|P同\\|` 同/前/外 | (體)同/他 | (端)同/他 | 鍵可信 | 器自身 | 截斷 | 未穿越型別數 | nodes |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in ROWS:
    print("| %d | %s | %s | %s | %d/%d/%d | %d/%d | %d/%d | %d | %d | %s | %d | %d |"
          % (r["seq"], r["entry"], r["blk"], r["side"],
             r["P同"]["同進入序號"], r["P同"]["前進入序號"], r["P同"]["外"],
             r["體同"], r["體他"], r["端同"], r["端他"], r["鍵可信"], r["器自身"],
             r["截斷"], len(r["未穿越"]), r["nodes"]))

print("\n   `__globals__ is ns`（以 `is` 判·⛔ 出艙 `id`）⇒ %s"
      % sorted({r["g_is_ns"] for r in ROWS}))
allun = {}
for r in ROWS:
    for t in r["未穿越"]:
        allun[t] = allun.get(t, 0) + 1
print("   未穿越之型別（全量·型別名·出現於幾次走訪）⇒ %s" % dict(sorted(allun.items())))
allsk = {}
for r in ROWS:
    for k, v in r["skipped"].items():
        allsk[k] = allsk.get(k, 0) + v
print("   ⛔穿越之型別計數（module／type／函式・方法・code・frame・generator）⇒ %s"
      % dict(sorted(allsk.items())))

print("\n── 命中之路徑（全量·逐次·鍵鏈逐字）──")
anyhit = False
for r in ROWS:
    for tag in ("hits體", "hits端"):
        for h in r[tag]:
            anyhit = True
            print("   seq=%d %s 變換=%s 路徑=%s ⇒ 命中 P 筆(seq=%s, entry=%s, blk=%r, side=%s)"
                  % (r["seq"], tag, h["tf"], "/".join(map(str, h["path"])),
                     h["p"]["seq"], h["p"]["entry"], h["p"]["blk"], h["p"]["side"]))
if not anyhit:
    print("   🛑 **loud：全量走訪之同命中 ＝ `0`**")

print("\n── 款 `5`　判別力五造 ──")
o, _ = (None, None)
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
    syn_root = {q["blk"]: {("left" if q["side"] == "L" else "right"):
                           tuple(float.fromhex(x) for x in q["hex"])},
                "__probe_record__": _ProbeMark({q["blk"]: {("left" if q["side"] == "L" else "right"):
                                                           tuple(float.fromhex(x) for x in q["hex"])}})}
    tg = [{"key": (q["blk"], q["side"]), "hex": q["hex"], "p": q}]
    hs, tr, uv, sk, nd = walk_roots([("(合成根)", syn_root)], tg)
    voc = SIDE_L if q["side"] == "L" else SIDE_R
    tn = 0
    for h in hs:
        ks = [str(x).strip("'\"<>key: ") for x in h["path"]]
        if any(x == q["blk"] for x in ks) and any(w in ks for w in voc):
            tn += 1
    print("   [必命中] 合成根 ⇒ 同命中 %d（須 ≥ 1）／鍵口徑可信 %d（須 ≥ 1）⇒ %s"
          % (len(hs), tn, "✅" if (hs and tn) else "🔴"))
    print("   [器自身之判別力] 合成根內刻意置入器之記錄容器 ⇒ marked 命中 %d（須 ≥ 1）⇒ %s"
          % (len([h for h in hs if h["marked"]]),
             "✅" if [h for h in hs if h["marked"]] else "🔴"))
    x0 = float.fromhex(q["hex"][0])
    pert = np.nextafter(x0, np.inf)
    tg2 = [{"key": (q["blk"], q["side"]), "hex": (float(pert).hex(), q["hex"][1]), "p": q}]
    hs2, _, _, _, _ = walk_roots([("(合成根)", syn_root)], tg2)
    print("   [必為零] `numpy.nextafter` 擾動一分量 ⇒ 同命中 %d（須 0）⇒ %s"
          % (len(hs2), "✅" if not hs2 else "🔴"))
print("   [必非零] 三包裝與進入序號計數器之觸發數 ⇒ %s ⇒ %s"
      % (dict(TRIG), "✅" if min(TRIG.values()) >= 1 else "🔴"))
print("   [器自身須 `0`] 實測各次之 marked 命中合計 ⇒ %d" % sum(r["器自身"] for r in ROWS))

print("\n── 款 `3`／`6-3`　停九／停十／不可判款（**逐次分列**）──")
print("| seq | 街廓 | 側 | (體)∪(端) 同命中 | 鍵可信 | 截斷 | 未穿越型別數 | **停九** | **停十** | **不可判** |")
print("|---|---|---|---|---|---|---|---|---|---|")
s9 = s10 = und = []
s9, s10, und = [], [], []
for r in ROWS:
    tot = r["體同"] + r["端同"]
    trunc_or_unv = bool(r["截斷"]) or len(r["未穿越"]) > 0
    _s9 = (tot == 0) and (not r["截斷"]) and len(r["未穿越"]) == 0
    _s10 = (tot >= 1) and (r["鍵可信"] == 0)
    _un = (tot == 0) and trunc_or_unv
    if _s9:
        s9.append(r["seq"])
    if _s10:
        s10.append(r["seq"])
    if _un:
        und.append(r["seq"])
    print("| %d | %s | %s | %d | %d | %s | %d | %s | %s | %s |"
          % (r["seq"], r["blk"], r["side"], tot, r["鍵可信"], r["截斷"], len(r["未穿越"]),
             "🔴 成就" if _s9 else "✅", "🔴 成就" if _s10 else "✅",
             "🔴 成就" if _un else "✅"))
print("\n🛑 **停九**（(體)∪(端) 同命中 `0` ⋀ 截斷 `0` ⋀ 未穿越 `0`）⇒ 成就之次 = %s ⇒ **%s**"
      % (s9, "🔴 成就 ⇒ 停、上呈" if s9 else "✅ 不成就"))
for q in s9:
    r = [x for x in ROWS if x["seq"] == q][0]
    tot_same = sum(r["P同"].values())
    print("   seq=%d 之分項成因：%s" % (q, "(i) `|P同| = 0`（全程尚無此產出）" if tot_same == 0
                                   else "(ii) `|P同| = %d ≥ 1` 而未被任何可及物持存" % tot_same))
print("🛑 **停十**（同命中 ≥ 1 ⋀ 鍵口徑可信 ＝ 0）⇒ 成就之次 = %s ⇒ **%s**"
      % (s10, "🔴 成就 ⇒ 停、上呈" if s10 else "✅ 不成就"))
print("🛑 **不可判款**（同命中 `0` ⋀（截斷 `>0` 或 未穿越 `>0`））⇒ 成就之次 = %s ⇒ **%s**"
      % (und, "🔴 成就 ⇒ loud、停、上呈" if und else "✅ 不成就"))

print("\n── 🛑 loud 之全量 ──")
if not LOUD:
    print("   （無記錄）⛔ 讀為「無異常」")
for m in sorted(set(LOUD)):
    print("   - %s   ×%d" % (m, LOUD.count(m)))

print("\n" + BAR)
print("【本器⛔ 判落點·⛔ 判可施與否·⛔ 擬任何改法或 diff】")
print(BAR)
