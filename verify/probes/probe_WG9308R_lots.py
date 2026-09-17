"""`W-G.9-308` `§六`：**逐宗基線之重量**（`run_verification` 全量**一次**）。

🔒 授權（單 `§六` 首段逐字·射程⛔ 逾之）：
   ① 新增本器（**底本 ＝ `probe_WG9307R_prepin.py`**·**⛔ 動該既有探針一字**），
      驅動 `run_verification` 全量**一次**（**⛔ 改生產碼一字**·其執行期間**⛔ 動受測物**）；
   ② **於行程內包裝**（⛔ 動任何檔·**冪等**）：`ns` 之二鍵 `_corner_buffer_S`／`_solve_G_one`；
      模組 `verify/stepg_pipeline.py` 之屬性 `_run_step_g_impl`（計進入序號·**持其回傳物件**·
      例外**原樣再拋**）；模組 `wf_f0` 之屬性 `compute`（**僅於進入時唯讀檢查**·原樣呼叫·
      例外原樣再拋）。**各觸發數須出艙且 `≥ 1`**；
   ③ **唯讀**讀取同一次跑所寫之 `verify/out/got_G值_退縮<tag>.csv`
      （以 `run_verification._read_csv`／`_norm` 讀與正規化·**⛔ 另寫第二份**）。

🛑 ⛔ 改生產碼一字、⛔ 為求反事實而呼叫任何生產函式、⛔ 自寫第二套幾何、⛔ 重建幾何、⛔ 補算。
🛑 ⛔ 判改法、⛔ 判可施與否、⛔ 擬任何 diff、⛔ 判任何宗之合格與否。

🩸 **單內互斥之逐字回報（`常規二`·取保守項續辦）**
   單 `§六-2` 之 `jsonl` 欄載「**未捨入之 `G` 與 `area_geom` 之 `float.hex`**」，
   而其同節之 🔒 **取法**逐字令取 `res['G']`／`res['area_geom']`。
   **自 blob 實查其建構式**（`自誤 418` 攔法 ①）＝ `app.py` 之 `_solve_G_one` 之 `return`：
       `'G': round(G_conv, 2)`　／　`'area_geom': round(area_conv, 2)`
   ⇒ 二者**皆為 `round(·, 2)` 之值**，該 `res` **⛔ 持未捨入之 `G`／`area_geom`**
     （未捨入者僅 `S_raw`／`W_far_raw`／`Rw_raw`／`W_rw_start_raw` 四鍵）。
   ⇒ **取保守項**：逐字依**取法**取 `res['G']`／`res['area_geom']` 之 `float.hex`，
     欄名改記為 `G_回傳時_float_hex`／`area_geom_回傳時_float_hex`，並逐筆附
     `捨入態 = 'round(·,2)·⛔ 未捨入'`；**⛔ 補算、⛔ 反事實**。

用法：`python verify/probes/probe_WG9308R_lots.py`
"""
import copy
import hashlib
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", newline="\n")

_BUF = io.StringIO()
_REAL = sys.stdout


class _Tee(object):
    """🩸 受測物（如 `verify/wf_f0.py`）於 `import` 時呼叫 `sys.stdout.reconfigure(...)`
    ⇒ 本代理須**委派其餘一切屬性予真 `stdout`**（⛔ 只實作 `write`／`flush`）。"""

    def write(self, s):
        _REAL.write(s)
        _BUF.write(s)

    def flush(self):
        _REAL.flush()

    def __getattr__(self, name):
        return getattr(_REAL, name)


sys.stdout = _Tee()

HERE = os.path.dirname(os.path.abspath(__file__))
VERIFY = os.path.dirname(HERE)
REPO = os.path.dirname(VERIFY)
sys.path.insert(0, VERIFY)
assert "WV_BAKE" not in os.environ, "🛑 `WV_BAKE` 已設 ⇒ 停"

BAR = "=" * 116
TAGS = ("0m", "3.5m")
REG_KEY = "f3_cad_side_lines_by_side"      # 工項三 `(d1)` 所得之登記表鍵（逐字）
MID_KEY = "mid"
SIDE_MAP = {"left": "L", "right": "R", "左側": "L", "右側": "R"}
BLK_KEYS = ["blk_label", "_lbl", "blk", "lbl", "label", "_blk"]
LG_KEYS = ("驗_宗序", "驗_B藍影", "驗_B_G", "驗_B_藍影面積")

TRIG = {"cbs": 0, "sgo": 0, "impl": 0, "f0": 0}
ENTRIES = []          # 逐進入
CUR_ENTRY = [None]    # 現行進入之 dict（`None` ＝ 在 `impl` 外）
LOUD = []
F0_REC = []


def canon(s):
    """🔒 承 `probe_WG9307R_prepin.py` 之 `canon` 逐字（⛔ 另寫第二份）。"""
    return SIDE_MAP.get(str(s).strip(), "?<%r>" % (s,))


def find_blk():
    """🔒 承 `probe_WG9307R_prepin.py` 之 `find_blk` 逐字（⛔ 另寫第二份）。"""
    f = sys._getframe(2)
    while f is not None:
        L = f.f_locals
        for k in BLK_KEYS:
            if k in L and isinstance(L[k], str) and L[k]:
                return (L[k], k, [x for x in BLK_KEYS if x in L and x != k], f.f_code.co_name)
        f = f.f_back
    return (None, None, [], None)


def fhex(v):
    try:
        return float(v).hex()
    except Exception:                                         # noqa: BLE001
        return None


def coord_fp(cc):
    """🔒 座標串指紋（⛔ `shapely`·⛔ 重建幾何）——單 `§六-2` 之式逐字。"""
    try:
        pts = []
        for p in (cc or []):
            if len(p) != 2:
                LOUD.append("頂點非二維：%r" % (p,))
                return None, None
            pts.append([float(p[0]).hex(), float(p[1]).hex()])
        s = json.dumps(pts, separators=(",", ":"))
        return hashlib.sha256(s.encode("utf-8")).hexdigest(), len(pts)
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("coord_fp 例外：%r" % (e,))
        return None, None


# ─────────────────────────────────────────────────────────────────────
#  包裝（骨架承 `probe_WG9307R_prepin.py`·**冪等**）
# ─────────────────────────────────────────────────────────────────────
def wrap(ns):
    if getattr(ns.get("_corner_buffer_S"), "_wg9308", False):
        return ns
    cbs, sgo = ns["_corner_buffer_S"], ns["_solve_G_one"]

    def sgo2(*a, **kw):
        TRIG["sgo"] += 1
        r = sgo(*a, **kw)
        e = CUR_ENTRY[0]
        if e is not None:
            _r0 = r[0] if isinstance(r, tuple) else r
            if isinstance(_r0, dict):
                blk, _k, _o, _fn = find_blk()
                e["solves"].append({
                    "ref_cut": _r0.get("cut_coords"),          # 🔒 **參照**（⛔ 以 `id` 為錨）
                    "G_hex": fhex(_r0.get("G")),
                    "area_geom_hex": fhex(_r0.get("area_geom")),
                    "S_raw_hex": (fhex(_r0["S_raw"]) if "S_raw" in _r0 else None),
                    "S_raw_缺": ("S_raw" not in _r0),
                    "S_hex": (fhex(_r0["S"]) if "S" in _r0 else None),
                    "S_缺": ("S" not in _r0),
                    "is_corner": bool(kw.get("is_corner")),
                    "side": canon(kw.get("side")),
                    "blk": blk,
                    "lg_cols": {k2: str((_r0.get("_lg_cols") or {}).get(k2, "—"))
                                for k2 in LG_KEYS},
                    "lg_缺": ("_lg_cols" not in _r0),
                })
                if "S_raw" not in _r0:
                    LOUD.append("`_solve_G_one` 之回傳⛔ 含鍵 `S_raw`")
                if "S" not in _r0:
                    LOUD.append("`_solve_G_one` 之回傳⛔ 含鍵 `S`")
        return r
    sgo2._wg9308 = True

    def cbs2(*a, **kw):
        TRIG["cbs"] += 1
        f = sys._getframe(1)
        L = f.f_locals
        lab = kw.get("_label", a[7] if len(a) > 7 else "")
        side_raw = kw.get("side", a[5] if len(a) > 5 else None)
        blk_f, key, others, _fn = find_blk()
        blk = blk_f or str(lab).split("·")[0]
        side = canon(side_raw)
        assert "ss" in L, "🛑 呼叫端框無 `ss` 鍵 ⇒ 鍵須自證存在"
        assert "blk_label" in L, "🛑 呼叫端框無 `blk_label` 鍵（第二鍵之自證）"
        ss = L["ss"]
        # 🔒 `(丁′)` 本輪之登記值 ＝ `W-G.9-307R` 款 `3` `(甲)` 之鍵鏈逐字
        reg = (ss.get(REG_KEY, {}) or {})
        item_l = ((reg.get(blk, {}) or {}).get("left", {}) or {})
        item_r = ((reg.get(blk, {}) or {}).get("right", {}) or {})
        reg_now = {
            "_side_mid_left": fhex_pt(item_l.get(MID_KEY)),
            "_side_mid_right": fhex_pt(item_r.get(MID_KEY)),
            "_has_left_corner": item_l.get(MID_KEY) is not None,
            "_has_right_corner": item_r.get(MID_KEY) is not None,
        }
        ding = {}
        for nm in ("_side_mid_left", "_side_mid_right",
                   "_has_left_corner", "_has_right_corner"):
            if nm not in L:
                ding[nm] = ("未存在", None, reg_now[nm])
            else:
                v = L[nm]
                vv = fhex_pt(v) if nm.startswith("_side_mid") else bool(v)
                ding[nm] = (("存在且與本輪之登記值逐位相等" if vv == reg_now[nm]
                             else "存在而相異"), vv, reg_now[nm])
        e = CUR_ENTRY[0]
        rec = {"entry": (e["idx"] if e else None), "tag": (e["tag"] if e else None),
               "blk": blk, "side": side, "label": lab, "blk_key": key,
               "blk_others": others, "丁": ding}
        (e["calls"] if e is not None else OUTSIDE_CALLS).append(rec)
        return cbs(*a, **kw)
    cbs2._wg9308 = True

    ns["_corner_buffer_S"], ns["_solve_G_one"] = cbs2, sgo2
    return ns


OUTSIDE_CALLS = []
REG_SNAP = {}         # 進入序號 → 該進入之 `ss` 之 `f3_cad_side_lines_by_side`（唯讀參照）


def fhex_pt(v):
    if v is None:
        return None
    try:
        import numpy as _np
        a = _np.asarray(v, dtype=float).reshape(-1)
        return (float(a[0]).hex(), float(a[1]).hex())
    except Exception as e:                                    # noqa: BLE001
        LOUD.append("fhex_pt 例外：%r" % (e,))
        return None


import run_verification as RV                                 # noqa: E402
import stepg_pipeline as SP                                   # noqa: E402
import wf_f0 as F0                                            # noqa: E402

_impl = SP._run_step_g_impl


def _chain_of():
    """呼叫鏈之分類（**`co_name` ＋ `co_filename` 之相對路徑**·**`id(·)` ⛔ 作錨**）。"""
    out = []
    f = sys._getframe(2)
    while f is not None:
        rel = os.path.relpath(f.f_code.co_filename, REPO).replace("\\", "/")
        out.append((rel, f.f_code.co_name))
        f = f.f_back
    return out


def impl2(*a, **kw):
    TRIG["impl"] += 1
    chain = _chain_of()
    kind = "其他"
    tag = None
    if len(chain) >= 2 and chain[0][1] == "run_step_g" \
            and chain[0][0] == "verify/stepg_pipeline.py" \
            and chain[1][1] == "main" and chain[1][0] == "verify/run_verification.py":
        kind = "主幹（`run_step_g` ⇐ `verify/run_verification.py :: main`）"
        f = sys._getframe(2)          # ＝ `main` 之框
        L = f.f_locals
        assert "tag" in L, "🛑 `main` 之 `f_locals` 無 `tag` 鍵 ⇒ 鍵須自證存在"
        assert "cad" in L, "🛑 `main` 之 `f_locals` 無 `cad` 鍵（第二鍵之自證）"
        tag = L["tag"]
    e = {"idx": TRIG["impl"], "kind": kind, "tag": tag,
         "chain": chain[:4], "solves": [], "calls": [], "ret": None,
         "exc": None, "dropped_pre": None, "dropped_post": None}
    ENTRIES.append(e)
    prev = CUR_ENTRY[0]
    CUR_ENTRY[0] = e
    ns0 = a[0] if a else kw.get("ns")
    _fs = a[1] if len(a) > 1 else kw.get("fake_st")
    try:                                                      # 🔒 **唯讀參照**（⛔ 複製、⛔ 改）
        REG_SNAP[e["idx"]] = (getattr(_fs, "session_state", {}) or {}).get(REG_KEY, {}) or {}
    except Exception as ex:                                   # noqa: BLE001
        LOUD.append("`ss` 之側界線登記表取用例外：%r" % (ex,))
        REG_SNAP[e["idx"]] = {}
    try:
        e["dropped_pre"] = copy.deepcopy(ns0.get("K917_DROPPED", {})) \
            if isinstance(ns0, dict) else None
    except Exception as ex:                                   # noqa: BLE001
        LOUD.append("K917_DROPPED 期初深複本例外：%r" % (ex,))
    try:
        r = _impl(*a, **kw)
    except BaseException as ex:                               # noqa: BLE001
        e["exc"] = "%s: %s" % (type(ex).__name__, str(ex)[:200])
        # 🩸 **回傳物件不存在時之照實處置（⛔ 補算·⛔ 反事實）**
        #   `run_step_g` 之 docstring 逐字：「`_pcap` 之 `g_rows` 掛的是 `_run_step_g_impl` 內
        #   `g_rows = []` 之**同一 list 物件**（掛引用·⛔ 複製）」⇒ 取之，並 **loud 具名**
        #   其為 **partial**、⛔ 回傳物件。
        _pc = kw.get("_pcap")
        if isinstance(_pc, dict) and isinstance(_pc.get("g_rows"), list):
            e["ret"] = {"g_rows": _pc["g_rows"]}
            e["ret_是partial"] = True
            LOUD.append("進入 %d（情境 %r）以例外離開 ⇒ 受詞改取 `_pcap['g_rows']`"
                        "（**同一 list 物件**·**partial**·⛔ 回傳物件）" % (e["idx"], e["tag"]))
        else:
            LOUD.append("進入 %d 以例外離開且 `_pcap` ⛔ 可取 ⇒ `g_rows` 為空"
                        % (e["idx"],))
        raise                                                 # 🔒 **原樣再拋**
    finally:
        try:
            e["dropped_post"] = copy.deepcopy(ns0.get("K917_DROPPED", {})) \
                if isinstance(ns0, dict) else None
        except Exception as ex:                               # noqa: BLE001
            LOUD.append("K917_DROPPED 期末深複本例外：%r" % (ex,))
        CUR_ENTRY[0] = prev
    e["ret"] = r                                              # 🔒 **持其回傳物件**
    return r


if not getattr(SP._run_step_g_impl, "_wg9308", False):
    impl2._wg9308 = True
    SP._run_step_g_impl = impl2

_f0 = F0.compute


def f0_2(ctx_by_tag):
    TRIG["f0"] += 1
    try:                                                      # 🔒 **僅於進入時唯讀檢查**
        for _t, c in (ctx_by_tag or {}).items():
            reg_cad = ((c.get("cad") or {}).get("side_lines_by_side"))
            reg_ss = ((getattr(c.get("fake_st"), "session_state", {}) or {})
                      .get(REG_KEY))
            F0_REC.append({
                "tag": _t,
                "is_same": (reg_cad is reg_ss),
                "cad_型": type(reg_cad).__name__,
                "ss_型": type(reg_ss).__name__,
                "cad_街廓數": (len(reg_cad) if hasattr(reg_cad, "__len__") else None),
                "ss_街廓數": (len(reg_ss) if hasattr(reg_ss, "__len__") else None),
            })
    except Exception as ex:                                   # noqa: BLE001
        LOUD.append("`wf_f0.compute` 之唯讀檢查例外：%r" % (ex,))
    try:
        return _f0(ctx_by_tag)                                # 🔒 **原樣呼叫**
    except BaseException as ex:                               # noqa: BLE001
        F0_REC.append({"tag": "<例外>", "exc": "%s: %s"
                       % (type(ex).__name__, str(ex)[:200])})
        raise                                                 # 🔒 **原樣再拋**


if not getattr(F0.compute, "_wg9308", False):
    f0_2._wg9308 = True
    F0.compute = f0_2

_orig_h = RV.harvest


def harvest2():
    ns, fs = _orig_h()
    return wrap(ns), fs


RV.harvest = harvest2

print(BAR)
print("【`W-G.9-308` `§六`　逐宗基線之重量】`run_verification` 全量**一次**")
print(BAR)
sys.stdout.flush()

try:
    rc = RV.main()
except SystemExit as e:
    rc = e.code
except Exception as e:                                        # noqa: BLE001
    rc = "EXC: %r" % (e,)

print("\n" + BAR)
print("`run_verification.main()` 之 `rc` ＝ %r" % (rc,))
print("四包裝之觸發數[必非零]：`_corner_buffer_S` %d ／ `_solve_G_one` %d ／ "
      "`_run_step_g_impl` %d ／ `wf_f0.compute` %d"
      % (TRIG["cbs"], TRIG["sgo"], TRIG["impl"], TRIG["f0"]))
_zero = [k for k, v in TRIG.items() if v == 0]
if _zero:
    print("🔴 **器紅**：包裝之觸發數為 `0` 者 ＝ %r ⇒ 停、上呈" % (_zero,))
print(BAR)

# ═════════════════════════════════════════════════════════════════════
#  停十四（現態漂移）
# ═════════════════════════════════════════════════════════════════════
import re                                                     # noqa: E402

print("\n── `§六-8`　停十四（現態漂移）──")
print("🔒 框（逐字·`§零-1`）＝ `\\[v3·G值(0m|3\\.5m)\\] 缺列.*`")
FR = re.compile(r"\[v3·G值(0m|3\.5m)\] 缺列.*")
this_out = _BUF.getvalue()
set_now = sorted(FR.findall(this_out) and [m.group(0) for m in FR.finditer(this_out)])
anchor_p = os.path.join(VERIFY, "out", "WG9307R_prepin.log")
set_anchor = []
if os.path.exists(anchor_p):
    with open(anchor_p, "rb") as fh:
        at = fh.read().decode("utf-8", "replace")
    set_anchor = sorted(m.group(0) for m in FR.finditer(at))
else:
    LOUD.append("錨落檔不存在：%s" % anchor_p)
print("   本次輸出之缺列字樣集 ＝ **%d** 列｜錨（`verify/out/WG9307R_prepin.log`）＝ **%d** 列"
      % (len(set_now), len(set_anchor)))
same_set = (set_now == set_anchor)
print("   二集逐列相同 ＝ **%s**" % same_set)
if not same_set:
    print("   🔴 僅本次有 ＝ %r" % (sorted(set(set_now) - set(set_anchor))[:12],))
    print("   🔴 僅錨有   ＝ %r" % (sorted(set(set_anchor) - set(set_now))[:12],))
stop14 = (rc != 1) or (not same_set)
print("**停十四** ⇒ %s" % ("🔴 **成就 ⇒ 停、⛔ 出艙款 `2`〜`5` 之判、上呈**"
                           if stop14 else "✅ **不成就**"))

# ═════════════════════════════════════════════════════════════════════
#  款 `1`　主幹之二進入
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-1`　款 `1`　主幹之二進入──")
print("🔒 判法 ＝ `co_name` ＋ `co_filename` 之**相對路徑**（**`id(·)` ⛔ 作錨**）")
MAIN = [e for e in ENTRIES if e["kind"].startswith("主幹")]
print("`_run_step_g_impl` 之進入總數 ＝ **%d**｜其中主幹 ＝ **%d**（期 `2`）"
      % (len(ENTRIES), len(MAIN)))
print("| 進入 | 類 | 情境標籤（`main` 之 `f_locals` 之 `tag`）| 鏈（前 `4` 層）|")
print("|---|---|---|---|")
for e in ENTRIES:
    print("| `%d` | %s | `%r` | `%r` |" % (e["idx"], e["kind"], e["tag"], e["chain"]))
_other = {}
for e in ENTRIES:
    if not e["kind"].startswith("主幹"):
        k = tuple(e["chain"][:2])
        _other[k] = _other.get(k, 0) + 1
print("\n其餘進入之呼叫鏈逐類之數（⛔ 靜默略過）＝ **%d** 類" % len(_other))
for k, v in sorted(_other.items(), key=str):
    print("   · %r ⇒ %d" % (k, v))
k1_red = (len(MAIN) != 2)

# ═════════════════════════════════════════════════════════════════════
#  款 `2`　逐宗基線（第二版）
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-2`　款 `2`　逐宗基線（第二版）──")
print("🔒 **受詞** ＝ 款 `1` 之二進入之**回傳物件**之 `['g_rows']` 之**每一列**（含抵費地之列）")
print("\n**同一物之證（靜態·逐字）**")
print("   `verify/run_verification.py`：")
print("     `_sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,`")
print("     `g_tab, diag_tab, slot_tab = build_step_g_tables(_sg)`")
print("   `verify/stepg_pipeline.py`：")
print("     `return _run_step_g_impl(`")
print("     `g_rows = [{k: r.get(k, '') for k in _cols} for r in res['g_rows']]`（**保序**）")

print("\n🩸 **單內互斥之逐字回報（`常規二`·取保守項）**")
print("   單 `§六-2` 之欄載「**未捨入之 `G` 與 `area_geom` 之 `float.hex`**」，"
      "而其 🔒 **取法**令取 `res['G']`／`res['area_geom']`。")
print("   **自 blob 實查之建構式**（`app.py` :: `_solve_G_one` 之 `return`·逐字）：")
print("     `'G': round(G_conv, 2),`")
print("     `'area_geom': round(area_conv, 2),`")
print("   ⇒ 二者**皆已捨入**；該 `res` **⛔ 持未捨入之 `G`／`area_geom`**"
      "（未捨入者僅 `S_raw`／`W_far_raw`／`Rw_raw`／`W_rw_start_raw`）。")
print("   ⇒ **取保守項**：逐字依取法取之，欄名記為 `G_回傳時_float_hex`／"
      "`area_geom_回傳時_float_hex`，逐筆附 `捨入態`；**⛔ 補算、⛔ 反事實**。")

OUT = os.path.join(VERIFY, "out")
JL = os.path.join(OUT, "WG9308R_lots_pre.jsonl")
recs, per_tag = [], {}
pair_stat = {"唯一": 0, "零": 0, "多": 0}
zero_hits, multi_hits = [], []
csv_meta = {}
dyn_bad = []

for e in MAIN:
    tag = e["tag"]
    rows = (e["ret"] or {}).get("g_rows", [])
    per_tag[tag] = len(rows)
    # ③ 唯讀讀同一次跑之 CSV（以 `RV._read_csv`／`RV._norm`·⛔ 另寫第二份）
    p = os.path.join(OUT, "got_G值_退縮%s.csv" % tag)
    crows, hdr = [], []
    if os.path.exists(p):
        crows = RV._read_csv(p)
        with open(p, "rb") as fh:
            cb = fh.read()
        hdr = list(crows[0].keys()) if crows else []
        csv_meta[tag] = {"bytes": len(cb), "sha256": hashlib.sha256(cb).hexdigest(),
                         "CR": cb.count(b"\r"), "資料列數": len(crows), "表頭": hdr}
    else:
        LOUD.append("同一次跑之 CSV 不存在：%s" % p)
        csv_meta[tag] = None
    for i, r in enumerate(rows):
        # 動態同一物之證
        if i < len(crows):
            for k in hdr:
                if k == "cut_coords":
                    continue
                a1, b1 = RV._norm(r.get(k, "")), RV._norm(crows[i].get(k, ""))
                if a1 != b1:
                    dyn_bad.append((tag, i, k, a1, b1))
        # 配對（**`is`**·⛔ 以 `id` 為錨）
        cc = r.get("cut_coords")
        hits = [s for s in e["solves"] if s["ref_cut"] is cc] if cc is not None else []
        if len(hits) == 1:
            pair_stat["唯一"] += 1
            st = "唯一命中"
        elif len(hits) == 0:
            pair_stat["零"] += 1
            st = "零命中"
            zero_hits.append((tag, i, r.get("暫編地號", ""), r.get("第1筆街角", ""),
                              r.get("推進側別", "")))
        else:
            pair_stat["多"] += 1
            st = "多命中"
            multi_hits.append((tag, i, r.get("暫編地號", ""), len(hits)))
        s0 = hits[0] if hits else None
        fp, nv = coord_fp(cc)
        recs.append({
            "情境": tag, "列序": i,
            "所屬街廓": r.get("所屬街廓", ""),
            "暫編地號": r.get("暫編地號", ""),
            "原地號": r.get("原地號", ""),
            "推進側別": r.get("推進側別", ""),
            "第1筆街角": r.get("第1筆街角", ""),
            "CSV_G原字串": (crows[i].get("G(㎡)", "") if i < len(crows) else None),
            "CSV_幾何面積原字串": (crows[i].get("幾何面積(㎡)", "") if i < len(crows) else None),
            "G_回傳時_float_hex": (s0["G_hex"] if s0 else None),
            "area_geom_回傳時_float_hex": (s0["area_geom_hex"] if s0 else None),
            "捨入態": "round(·,2)·⛔ 未捨入（`常規二` 取保守項·見報告 §六-2）",
            "座標串指紋": fp, "頂點數": nv,
            "配對之態": st,
        })

with open(JL, "wb") as fh:
    for r in recs:
        fh.write((json.dumps(r, ensure_ascii=False) + "\n").encode("utf-8"))
jb = open(JL, "rb").read()
print("\n逐情境筆數 ＝ %r｜合計 %d" % (per_tag, len(recs)))
print("落檔 ＝ `verify/out/WG9308R_lots_pre.jsonl`｜%d B｜`sha256` %s｜`CR` %d"
      % (len(jb), hashlib.sha256(jb).hexdigest(), jb.count(b"\r")))

print("\n**同一次跑之 CSV（🛑 ⛔ 入倉·`.gitignore` 已列 `verify/out/got_*`）**")
for tag in TAGS:
    m = csv_meta.get(tag)
    if m is None:
        print("   `%s` ⇒ 🛑 **不存在**" % tag)
        continue
    print("   `%s` ⇒ %d B｜`sha256` %s｜`CR` %d｜資料列數 %d"
          % (tag, m["bytes"], m["sha256"], m["CR"], m["資料列數"]))
    print("      表頭逐字 ＝ %r" % (m["表頭"],))

# 自證
print("\n**自證 ①**（每情境筆數 ＝ 同一次跑之 CSV 資料列數）")
ok1 = True
for tag in TAGS:
    m = csv_meta.get(tag)
    n = m["資料列數"] if m else None
    same = (n == per_tag.get(tag))
    ok1 &= bool(same)
    print("   `%s` ⇒ `g_rows` %s ／ CSV %s ⇒ %s"
          % (tag, per_tag.get(tag), n, "✅" if same else "🔴"))

print("\n**自證 ②**（同一物之動態證：逐欄相異 ＝ `0`）⇒ 相異 ＝ **%d**｜%s"
      % (len(dyn_bad), "✅" if not dyn_bad else "🔴"))
if dyn_bad:
    print("   🛑 **loud 全量**：")
    for x in dyn_bad:
        print("      · 情境 `%s`｜列 `%d`｜欄 `%s`｜`g_rows` `%r` vs CSV `%r`" % x)

s0s = {json.dumps({k: v for k, v in r.items() if k != "情境"},
                  ensure_ascii=False, sort_keys=True)
       for r in recs if r["情境"] == TAGS[0]}
s1s = {json.dumps({k: v for k, v in r.items() if k != "情境"},
                  ensure_ascii=False, sort_keys=True)
       for r in recs if r["情境"] == TAGS[1]}
ok3 = (s0s != s1s)
print("\n**自證 ③**（判別力[必相異]：二情境之紀錄集相異）⇒ %s（僅 `%s` 有 %d／僅 `%s` 有 %d）⇒ %s"
      % (ok3, TAGS[0], len(s0s - s1s), TAGS[1], len(s1s - s0s), "✅" if ok3 else "🔴"))

fake = "F" + chr(65) + "KE-" + str(9) * 4 + "(0)"             # 執行期組出·字面⛔ 出艙
ok4 = not any(fake in (r["暫編地號"] or "") or fake in (r["原地號"] or "") for r in recs)
print("**自證 ④**（判別力[必為零]：一**執行期組出**之人造地號於紀錄集命中）⇒ %d ⇒ %s"
      % (0 if ok4 else 1, "✅" if ok4 else "🔴"))

print("\n**自證 ⑤**（配對之三態逐筆分列）⇒ 唯一 **%d**／零 **%d**／多 **%d**"
      % (pair_stat["唯一"], pair_stat["零"], pair_stat["多"]))
if zero_hits:
    print("   🛑 **零命中之全量（loud 逐筆具名）**：")
    for t, i, k, fc, asd in zero_hits:
        print("      · 情境 `%s`｜列 `%d`｜暫編地號 `%s`｜`第1筆街角` `%s`｜`推進側別` `%s`"
              % (t, i, k, fc, asd))
if multi_hits:
    print("   🔴 **多命中 ⇒ 器紅**：%r" % (multi_hits,))
# 唯一命中者之二檢
bad_round, bad_drift = [], []
for e in MAIN:
    tag = e["tag"]
    rows = (e["ret"] or {}).get("g_rows", [])
    p = os.path.join(OUT, "got_G值_退縮%s.csv" % tag)
    crows = RV._read_csv(p) if os.path.exists(p) else []
    for i, r in enumerate(rows):
        cc = r.get("cut_coords")
        hits = [s for s in e["solves"] if s["ref_cut"] is cc] if cc is not None else []
        if len(hits) != 1:
            continue
        s0 = hits[0]
        if s0["G_hex"] is not None and i < len(crows):
            g = float.fromhex(s0["G_hex"])
            if RV._norm(round(g, 2)) != RV._norm(crows[i].get("G(㎡)", "")):
                bad_round.append((tag, i, r.get("暫編地號", ""), round(g, 2),
                                  crows[i].get("G(㎡)", "")))
        now = fhex(r.get("G(㎡)"))
        if s0["G_hex"] is not None and now is not None and s0["G_hex"] != now:
            bad_drift.append((tag, i, r.get("暫編地號", ""), s0["G_hex"], now))
print("   `round(float(G_回傳時), 2)` vs CSV 之 `G(㎡)` 之 `_norm` 相異 ＝ **%d**%s"
      % (len(bad_round), "" if not bad_round else " 🛑 **loud**"))
for x in bad_round:
    print("      · %r" % (x,))
print("   `G` 於回傳時與進入結束時之 `float.hex` 相異 ＝ **%d**%s"
      % (len(bad_drift), "" if not bad_drift else " 🛑 **loud**"))
for x in bad_drift[:20]:
    print("      · %r" % (x,))

# 自證 ⑥（指紋判別力·⛔ 落檔）
ok6 = None
for e in MAIN:
    rows = (e["ret"] or {}).get("g_rows", [])
    for r in rows:
        cc = r.get("cut_coords")
        if cc and len(cc) > 0 and len(cc[0]) == 2:
            import struct
            c2 = [[float(p[0]), float(p[1])] for p in cc]
            x0 = c2[0][0]
            bits = struct.unpack("<Q", struct.pack("<d", x0))[0] ^ 1
            c2[0][0] = struct.unpack("<d", struct.pack("<Q", bits))[0]
            f1, _ = coord_fp(cc)
            f2, _ = coord_fp(c2)
            ok6 = (f1 != f2)
            break
    if ok6 is not None:
        break
print("\n**自證 ⑥**（指紋判別力[必相異]：記憶體內複製一列之座標串、改其一分量之末位元）⇒ 相異 ＝ %r ⇒ %s"
      % (ok6, "✅" if ok6 else "🔴"))

# ═════════════════════════════════════════════════════════════════════
#  款 `3`　逐情境之強制抵費地與街角第 `1` 宗
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-3`　款 `3`　逐情境之強制抵費地與街角第 `1` 宗（`自誤 417` 攔法 ① 之實施）──")
cells = []
for e in MAIN:
    blks = []
    for r in (e["ret"] or {}).get("g_rows", []):
        b = r.get("所屬街廓", "")
        if b and b not in blks:
            blks.append(b)
    for b in blks:
        for sd in ("left", "right"):
            cells.append((e, b, sd))
print("母體 ＝ 二進入 × 該進入內 `g_rows` 所見之街廓 × `{left, right}` ⇒ **基數 ＝ %d**" % len(cells))
print("\n| 進入 | 情境 | 街廓 | 側 | `(甲′)` 強制呼叫 | `(乙′)` `is_corner` 真 | `(乙″)` `第1筆街角=='是'` 列數 |")
print("|---|---|---|---|---|---|---|")
jia_true, yi_mismatch = [], []
for e, b, sd in cells:
    c = canon(sd)
    jia = any(x["blk"] == b and x["side"] == c for x in e["calls"])
    yi1 = any(s["is_corner"] and s["blk"] == b and s["side"] == c for s in e["solves"])
    yi2 = sum(1 for r in (e["ret"] or {}).get("g_rows", [])
              if r.get("所屬街廓") == b and r.get("推進側別") == sd
              and r.get("第1筆街角") == "是")
    if bool(yi1) != bool(yi2):
        yi_mismatch.append((e["tag"], b, sd, yi1, yi2))
    if jia:
        jia_true.append((e, b, sd, yi1, yi2))
    print("| `%d` | `%s` | `%s` | `%s` | %s | %s | `%d` |"
          % (e["idx"], e["tag"], b, sd, jia, yi1, yi2))
print("\n🔒 `(乙′)` 與 `(乙″)` 之**有無**相異之格 ＝ **%d**%s"
      % (len(yi_mismatch), "" if not yi_mismatch else " 🛑 **loud 全量**"))
for x in yi_mismatch:
    print("   · 情境 `%s`｜街廓 `%s`｜側 `%s`｜`(乙′)` %r｜`(乙″)` %r" % x)
ab = [(e["tag"], b, sd) for e, b, sd, y1, _y2 in jia_true if not y1]
print("\n🔑 **`(甲′) ⋀ ¬(乙′)` 之格之全量** ＝ **%d**" % len(ab))
for x in ab:
    print("   · 情境 `%s`｜街廓 `%s`｜側 `%s`" % x)

# ═════════════════════════════════════════════════════════════════════
#  款 `4`　`(丁′)` 綁定之輪次
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-4`　款 `4`　`(丁′)` 綁定之輪次（**全量**·每一次強制呼叫）──")
allcalls = [c for e in MAIN for c in e["calls"]] + OUTSIDE_CALLS
print("強制呼叫總數（`_corner_buffer_S` 之觸發數）＝ **%d**｜本款之列數 ＝ **%d**"
      % (TRIG["cbs"], len(allcalls)))
print("| # | 進入 | 情境 | 街廓 | 側 | `_side_mid_left` | `_side_mid_right` |"
      " `_has_left_corner` | `_has_right_corner` |")
print("|---|---|---|---|---|---|---|---|---|")
for i, c in enumerate(allcalls, 1):
    d = c["丁"]
    print("| %d | `%r` | `%r` | `%s` | `%s` | %s | %s | %s | %s |"
          % (i, c["entry"], c["tag"], c["blk"], c["side"],
             d["_side_mid_left"][0], d["_side_mid_right"][0],
             d["_has_left_corner"][0], d["_has_right_corner"][0]))
print("\n**「存在而相異」之逐筆全量（本輪之登記值對照）**")
_nd = 0
for i, c in enumerate(allcalls, 1):
    for nm, (st, v, reg) in c["丁"].items():
        if st == "存在而相異":
            _nd += 1
            print("   · #%d｜`%s`/`%s`｜名 `%s`｜框內值 `%r`｜本輪登記值 `%r`"
                  % (i, c["blk"], c["side"], nm, v, reg))
if _nd == 0:
    print("   （無）**⛔ 讀為「無異常」**")
k4_red = (len(allcalls) != TRIG["cbs"])

# ═════════════════════════════════════════════════════════════════════
#  款 `5`　七級調配之 `ctx` 之登記表同一性
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-5`　款 `5`　七級調配之 `ctx` 之登記表同一性──")
print("`wf_f0.compute` 之觸發數 ＝ **%d**" % TRIG["f0"])
if not F0_REC:
    print("🛑 **loud**：`wf_f0.compute` 之進入⛔ 任何紀錄")
for r in F0_REC:
    if "exc" in r:
        print("   🛑 **loud**：`wf_f0.compute` **以例外離開** ⇒ `%s`" % r["exc"])
        print("      ⇒ **七級調配（含末端塊之門檻 `_end_gate`、調配後剩餘之土地之判）"
              "於本次跑⛔ 被驅動**")
    else:
        print("   · 情境 `%r`｜`c[\"cad\"][\"side_lines_by_side\"] is "
              "c[\"fake_st\"].session_state[\"%s\"]` ⇒ **%r**｜"
              "登記表之街廓數 cad %r ／ ss %r｜型 %s ／ %s"
              % (r["tag"], REG_KEY, r["is_same"], r["cad_街廓數"], r["ss_街廓數"],
                 r["cad_型"], r["ss_型"]))
if TRIG["f0"] == 0:
    print("   🛑 **loud 具名**：`wf_f0.compute` **於本次跑⛔ 被呼叫**"
          " ⇒ 七級調配（含末端塊之門檻 `_end_gate`、調配後剩餘之土地之判）**未被驅動**")

# ═════════════════════════════════════════════════════════════════════
#  款 `6`　強制抵費地之側之前二宗
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-6`　款 `6`　強制抵費地之側之前二宗（`K-9-32` 之受詞之現態）──")
print("母體 ＝ 款 `3` 之 `(甲′)` 真之格 ⇒ **%d** 格" % len(jia_true))
for e, b, sd, _y1, _y2 in jia_true:
    rows = [r for r in (e["ret"] or {}).get("g_rows", [])
            if r.get("所屬街廓") == b and r.get("推進側別") == sd]
    print("\n### 情境 `%s`｜街廓 `%s`｜側 `%s`　（該側之列 ＝ **%d**）"
          % (e["tag"], b, sd, len(rows)))
    if len(rows) < 2:
        print("   🛑 **loud 具名**：該側之列**不足 `2`**")
    for j, r in enumerate(rows[:2]):
        cc = r.get("cut_coords")
        hits = [s for s in e["solves"] if s["ref_cut"] is cc] if cc is not None else []
        lg = hits[0]["lg_cols"] if len(hits) == 1 else None
        print("   · 序 `%d`｜`暫編地號` `%s`｜`G(㎡)` `%s`｜`第1筆街角` `%s`｜`街角側別` `%s`"
              % (j, r.get("暫編地號", ""), r.get("G(㎡)", ""),
                 r.get("第1筆街角", ""), r.get("街角側別", "")))
        if lg is None:
            print("      🛑 **loud 具名**：配對 `res` **零命中** ⇒ `_lg_cols` **⛔ 可取**")
        else:
            print("      `_lg_cols` ⇒ %s"
                  % "；".join("`%s` ＝ `%s`" % (k, v) for k, v in lg.items()))
    # `K917_DROPPED` 之該格記錄（**該進入之始與末之深複本之差**·唯讀）
    pre = (e["dropped_pre"] or {})
    post = (e["dropped_post"] or {})
    key = (str(b), str(sd))
    lp, lq = pre.get(key, []), post.get(key, [])
    print("   `ns[\"K917_DROPPED\"]` 之該 (街廓, 側) 新增記錄（**始末深複本之差**）＝ **%d**"
          % max(0, len(lq) - len(lp)))
    for x in lq[len(lp):]:
        print("      · %r" % (x,))
print("\n**同一暫編地號於同一進入內出現於二側，或 `街角側別` 與 `推進側別` 相異者（逐筆·⛔ 判其當否）**")
_dup = 0
for e in MAIN:
    seen = {}
    for r in (e["ret"] or {}).get("g_rows", []):
        k = r.get("暫編地號", "")
        seen.setdefault(k, set()).add(r.get("推進側別", ""))
    for k, sds in seen.items():
        if len({x for x in sds if x in ("left", "right")}) > 1:
            _dup += 1
            print("   · 情境 `%s`｜暫編地號 `%s`｜出現於側 %r" % (e["tag"], k, sorted(sds)))
    for r in (e["ret"] or {}).get("g_rows", []):
        cs, asd = r.get("街角側別", ""), r.get("推進側別", "")
        if cs not in ("", "—") and canon(cs) != canon(asd):
            _dup += 1
            print("   · 情境 `%s`｜暫編地號 `%s`｜`街角側別` `%s` ≠ `推進側別` `%s`"
                  % (e["tag"], r.get("暫編地號", ""), cs, asd))
if _dup == 0:
    print("   （無）**⛔ 讀為「無異常」**")

# ═════════════════════════════════════════════════════════════════════
#  款 `7`　逐宗之臨正街寬度與畸零地寬
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-7`　款 `7`　逐宗之臨正街寬度與畸零地寬之現態（**⛔ 判合格與否**）──")
print("🔒 **該側有無側街之取法**（逐字·`verify/stepg_pipeline.py`·⛔ 另立判準）：")
print("     `_sl_left = _side_lines_blk.get('left') or {}`")
print("     `_side_mid_left = _sl_left.get('mid')`")
print("     `_has_left_corner = _side_mid_left is not None`")
print("   （右側同形）")

k7 = []
other_side = {}
for e in MAIN:
    rows = (e["ret"] or {}).get("g_rows", [])
    p = os.path.join(OUT, "got_G值_退縮%s.csv" % e["tag"])
    crows = RV._read_csv(p) if os.path.exists(p) else []
    # 該進入之 `ss` 之登記表（唯讀·於 `impl2` 之進入時取其參照）
    reg = REG_SNAP.get(e["idx"], {})
    kseq = {}
    for i, r in enumerate(rows):
        sd = r.get("推進側別", "")
        if sd not in ("left", "right"):
            other_side[sd] = other_side.get(sd, 0) + 1
            continue
        b = r.get("所屬街廓", "")
        kk = (b, sd)
        kseq[kk] = kseq.get(kk, -1) + 1
        cc = r.get("cut_coords")
        hits = [s for s in e["solves"] if s["ref_cut"] is cc] if cc is not None else []
        s0 = hits[0] if len(hits) == 1 else None
        _sl = ((reg.get(b, {}) or {}).get(sd, {}) or {})
        has_side = (_sl.get(MID_KEY) is not None)
        k7.append({
            "情境": e["tag"], "所屬街廓": b, "推進側別": sd, "序k": kseq[kk],
            "暫編地號": r.get("暫編地號", ""), "第1筆街角": r.get("第1筆街角", ""),
            "該側有無側街": has_side,
            "甲′真": any(x["blk"] == b and x["side"] == canon(sd) for x in e["calls"]),
            "S_raw_hex": (s0["S_raw_hex"] if s0 else None),
            "S_hex": (s0["S_hex"] if s0 else None),
            "CSV_S原字串": (crows[i].get("S(m)", "") if i < len(crows) else None),
            "驗_A_W": r.get("驗_A_W", "—"),
            "驗_A幾何": r.get("驗_A幾何", "—"),
            "驗_B藍影": r.get("驗_B藍影", "—"),
            "驗_B_臨正街": r.get("驗_B_臨正街", "—"),
            "_entry": e["idx"],
        })

print("\n母體（`推進側別` ∈ `{left, right}`）**基數 ＝ %d**" % len(k7))
print("其餘之列依 `推進側別` 之值逐值計數（⛔ 靜默略過）＝ %r" % (other_side,))

# 畸零地寬 `W` 之取法
Wmap, Wbad = {}, []
for r in k7:
    key = (r["情境"], r["所屬街廓"])
    v = str(r["驗_A_W"]).strip()
    if v and v != "—":
        Wmap.setdefault(key, set()).add(v)
for key, s in Wmap.items():
    if len(s) != 1:
        Wbad.append((key, sorted(s)))
print("\n**畸零地寬 `W` 之取法**（同進入同街廓之列中 `驗_A_W` ≠ `'—'` 之值集·須恰為單一值）")
for key in sorted(Wmap, key=str):
    print("   · `%s`／`%s` ⇒ %r%s" % (key[0], key[1], sorted(Wmap[key]),
                                       "" if len(Wmap[key]) == 1 else " 🛑 **loud**"))
missW = sorted({(r["情境"], r["所屬街廓"]) for r in k7} - set(Wmap))
if missW:
    print("   🛑 **loud**：⛔ 任何 `驗_A_W` ≠ `'—'` 之列者 ＝ %r ⇒ 其 `S_raw − W` 出艙「不可判」"
          % (missW,))

print("\n**逐宗之全量**")
print("| 情境 | 街廓 | 側 | `k` | 暫編地號 | `第1筆街角` | 有側街 | `(甲′)` |"
      " `S_raw`(hex) | `S`(hex) | CSV `S(m)` | `驗_A_W` | `驗_A幾何` | `驗_B藍影` |"
      " `驗_B_臨正街` | `S_raw − W`(帶號) | `\\|S_raw − W\\|` |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in k7:
    key = (r["情境"], r["所屬街廓"])
    wv = sorted(Wmap.get(key, []))
    d, ad = "不可判", "不可判"
    if len(wv) == 1 and r["S_raw_hex"]:
        dd = float.fromhex(r["S_raw_hex"]) - float(wv[0])
        d, ad = "%.6f" % dd, "%.6f" % abs(dd)
    print("| `%s` | `%s` | `%s` | `%d` | `%s` | `%s` | %s | %s | `%s` | `%s` | `%s` |"
          " `%s` | `%s` | `%s` | `%s` | `%s` | `%s` |"
          % (r["情境"], r["所屬街廓"], r["推進側別"], r["序k"], r["暫編地號"],
             r["第1筆街角"], r["該側有無側街"], r["甲′真"], r["S_raw_hex"], r["S_hex"],
             r["CSV_S原字串"], r["驗_A_W"], r["驗_A幾何"], r["驗_B藍影"],
             r["驗_B_臨正街"], d, ad))

print("\n**分類計數表**（以程式自資料列計數·逐情境分列）")
print("| 情境 | 類 | 列數 | `S_raw < W` 之列數 | `驗_A幾何` 各值之數 |")
print("|---|---|---|---|---|")
cls_rows = {}
for r in k7:
    if r["序k"] == 0 and r["該側有無側街"]:
        c = "類① `k=0` ⋀ 有側街"
    elif r["序k"] == 0 and not r["該側有無側街"]:
        c = "類② `k=0` ⋀ 無側街"
    elif r["序k"] == 1 and r["該側有無側街"]:
        c = "類③ `k=1` ⋀ 有側街"
    else:
        c = "類④ 其餘"
    cls_rows.setdefault((r["情境"], c), []).append(r)
lt = []
for (tg, c) in sorted(cls_rows, key=str):
    rs = cls_rows[(tg, c)]
    n_lt = 0
    for r in rs:
        wv = sorted(Wmap.get((r["情境"], r["所屬街廓"]), []))
        if len(wv) == 1 and r["S_raw_hex"] and float.fromhex(r["S_raw_hex"]) < float(wv[0]):
            n_lt += 1
            lt.append(r)
    geo = {}
    for r in rs:
        geo[str(r["驗_A幾何"])] = geo.get(str(r["驗_A幾何"]), 0) + 1
    print("| `%s` | %s | `%d` | `%d` | %r |" % (tg, c, len(rs), n_lt, geo))
print("\n**`S_raw < W` 之列之全量** ＝ **%d**" % len(lt))
for r in lt:
    wv = sorted(Wmap.get((r["情境"], r["所屬街廓"]), []))
    print("   · 情境 `%s`｜街廓 `%s`｜側 `%s`｜`k` `%d`｜`%s`｜`S_raw` `%.6f` < `W` `%s`"
          % (r["情境"], r["所屬街廓"], r["推進側別"], r["序k"], r["暫編地號"],
             float.fromhex(r["S_raw_hex"]), wv[0]))

# 款 `7` 自證
print("\n**自證 ①**（款 `3` 之 `(甲′)` 真之格，其「該側有無側街」皆 ＝ 有）")
s1_bad = [r for r in k7 if r["甲′真"] and not r["該側有無側街"]]
print("   不合者 ＝ **%d** ⇒ %s" % (len(s1_bad), "✅" if not s1_bad else "🛑 **loud 具名**"))
print("**自證 ②**（母體列數 ＋ 其餘之列數 ＝ 款 `2` 之每情境筆數）")
ok_s2 = (len(k7) + sum(other_side.values()) == len(recs))
print("   %d ＋ %d ＝ %d ／ 款 `2` 合計 %d ⇒ %s"
      % (len(k7), sum(other_side.values()), len(k7) + sum(other_side.values()),
         len(recs), "✅" if ok_s2 else "🔴"))
c1 = {t: 0 for t in TAGS}
c2 = {t: 0 for t in TAGS}
for r in k7:
    if r["序k"] == 0 and r["該側有無側街"]:
        c1[r["情境"]] = c1.get(r["情境"], 0) + 1
    if r["序k"] == 0 and not r["該側有無側街"]:
        c2[r["情境"]] = c2.get(r["情境"], 0) + 1
ok_s3 = all(c1.get(t, 0) > 0 and c2.get(t, 0) > 0 for t in per_tag)
print("**自證 ③**（判別力[必非空]：類① 與類② 於每一情境皆 `> 0`）⇒ 類① %r／類② %r ⇒ %s"
      % (c1, c2, "✅" if ok_s3 else "🔴"))
s4_bad = []
for e in MAIN:
    rows = (e["ret"] or {}).get("g_rows", [])
    p = os.path.join(OUT, "got_G值_退縮%s.csv" % e["tag"])
    crows = RV._read_csv(p) if os.path.exists(p) else []
    for i, r in enumerate(rows):
        cc = r.get("cut_coords")
        hits = [s for s in e["solves"] if s["ref_cut"] is cc] if cc is not None else []
        if len(hits) != 1 or hits[0]["S_hex"] is None or i >= len(crows):
            continue
        if RV._norm(round(float.fromhex(hits[0]["S_hex"]), 2)) \
                != RV._norm(crows[i].get("S(m)", "")):
            s4_bad.append((e["tag"], i, r.get("暫編地號", ""),
                           round(float.fromhex(hits[0]["S_hex"]), 2),
                           crows[i].get("S(m)", "")))
print("**自證 ④**（配對 `res` 之 `S` 之 `round(·, 2)` 與 CSV 之 `S(m)` 之 `_norm` 相等）"
      "⇒ 相異 ＝ **%d** ⇒ %s" % (len(s4_bad), "✅" if not s4_bad else "🛑 **loud 全量**"))
for x in s4_bad:
    print("   · %r" % (x,))

print("\n🛑 **⛔ 判**：`S` 是否為截角前之寬、任一宗之合格與否、類④ 之列是否屬 `K-9-33` 之受詞。")

# ═════════════════════════════════════════════════════════════════════
#  器紅
# ═════════════════════════════════════════════════════════════════════
print("\n" + BAR)
print("── `§六-8`　器紅之判──")
red = []
if min(TRIG.values()) == 0:
    red.append("包裝或進入計數之任一觸發數 ＝ `0`（%r）" % (TRIG,))
if k1_red:
    red.append("款 `1` ≠ `2`（實得 %d）" % len(MAIN))
if not (ok1 and not dyn_bad and ok4):
    red.append("款 `2` 自證 ①②④ 有不過者")
if multi_hits:
    red.append("款 `2` ⑤ 有多命中")
if k4_red:
    red.append("款 `4` 之列數 ≠ 強制呼叫總數")
if not (ok_s2 and not s4_bad):
    red.append("款 `7` 自證 ②④ 有不過者")
print("🛑 **器紅** ⇒ %s"
      % ("🔴 **成就 ⇒ 停、上呈**：" + "；".join(red) if red else "✅ **不成就**"))
print("🔒 款 `2` ⑤ 之零命中、款 `3`〜`7` 之任何結果——**⛔ 停**，逐項照實具名，**裁屬發單側**。")

print("\n── 🛑 loud 之全量 ──")
if not LOUD:
    print("   （無記錄）**⛔ 讀為「無異常」**")
for m in sorted(set(LOUD)):
    print("   - %s   ×%d" % (m, LOUD.count(m)))

print("\n" + BAR)
print("【本器⛔ 判改法·⛔ 判可施與否·⛔ 擬任何 diff·⛔ 開分支·⛔ 動用 KL 之放行】")
print(BAR)

_dst = os.path.join(OUT, "WG9308R_lots.log")
_data = _BUF.getvalue().encode("utf-8")
with open(_dst, "wb") as _fh:
    _fh.write(_data)
sys.stdout = _REAL
print("\n落檔 ＝ `verify/out/WG9308R_lots.log`｜%d B｜`sha256` %s｜`CR` %d"
      % (len(_data), hashlib.sha256(_data).hexdigest(), _data.count(b"\r")))
