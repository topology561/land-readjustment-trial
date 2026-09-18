# -*- coding: utf-8 -*-
"""`W-G.9-315` `§三`／`§四`：`K-9-5-12` 反事實之**態乙**驅動（二替身·🛑 **⛔ 落地**）。

🔒 **底本** ＝ `verify/probes/probe_WG9278_w0zero.py`（框內省 `_climb`／鏈頭判準／自我驗證閘／
   坑 `bb`／坑 `bd` 之攔法**逐字沿用**·⛔ 另寫第二份判準）。
🔒 `理論@k*`／`實跑(階段1)` 之取法 ＝ **直接 import** `probe_WG9273_delta_locate` 之 `theo`／`real`
   （⛔ 另寫第二份判準·`GB-168` 之 CC 當場復現節逐字所定之同一取法）。

🛑 **替身之定義（發單側定·單 `§三` 逐字·⛔ CC 自訂）**
   · **替身 `α`**：凡 `rw_increment` 之呼叫端經**框內省**判定為鏈頭
     （判準一律取碼面之同一運算式 `is_corner or is_chain_head`·自呼叫端之區域名取值）者，
     以 **`rw_increment(0.0, W_cur)`** 代之（**`W_cur` ⛔ 改**）。
   · **替身 `β`**：同一判定下，以 **`rw_increment(0.0, W_cur - W_prev)`** 代之。
   · 🛑 **⛔ 寫入倉之生產碼**；⛔ 於框內省**不可判**之處施加（一律跳過並 loud 計數）。

🛑 **驅動母體 ＝ 態乙**（`WV_K6_STEP0=off`·＝ `K-9-29 二` 所令之態）；情境 ＝ `0m` ⋀ `3.5m`。
🛑 **情形之分（⛔ 混同·`W-G.9-278` `§七-5` 逐字沿用）**
   · **甲** ＝ 該側之街角**非**強制抵費地 ⇒ **可模擬**。
   · **乙** ＝ 該側之街角**為**強制抵費地 ⇒ 🛑 **⛔ 模擬**，出艙**第三種碼**。

🛑 **判別力三造（單 `§三` 逐字·三造之值皆自 `GB-168` 一次／二次精化逐字取·⛔ 人造之數）**
   造甲[必有差·**純函式層**·⛔ 驅動管線]：`rw_increment` 之三實參兩兩相異（`|差| > TOL0`）。
   造乙[必無差]：`W_prev ≤ 0` 之鏈頭 ⇒ 替身 `α` 之 `|ΔRw| ≤ TOL0`
     （由：`rw_from_width` 於 `W ≤ 0` 逐字 `return 0.0`）。其格數須 `> 0`，逐格具名。
   造丙[替身確已生效·反空操作]：替身之「**咬到**」計數須 `> 0`，逐段逐格具名；
     「不可判」之計數一律 loud 出艙。
   🛑 **造甲 🔴 有差 ⋀ 造乙 🟢 無差 ⋀ 造丙 `> 0`** ⇒ 器非紅；**任二造同色 ⇒ 器紅 `rc = 5`**
     ⇒ **⛔ 出艙任何反事實之數**。⛔ 以「反正都是 `0`」頂替。

🛑 **⛔ 落地、⛔ 稱本器為「落地」、⛔ 判 `K-9-5-12` 應否落地、⛔ 判孰為正確之 `W`、
   ⛔ 判理論側與實跑側何者為是、⛔ 提修法主張、⛔ 判結構閘應否放寬或停用。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9315_k95_12_stateB.py <倉根> <alpha|beta>`
`rc`：`0`／`2` 用法錯／`5` **器紅**（自證閘不過／判別力三造不成立）。
"""
import contextlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

MODE = (sys.argv[2] if len(sys.argv) > 2 else "").strip().lower()

ENV = "WV_K6_STEP0"
STATE_B = "off"                 # 🔒 態乙（`K-9-29 二` 所令之態）
W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
TOL0 = 1e-6                     # 🔒 零之判準 ＝ 具名常數（⛔ 字面）
IFACE_TOL = 0.1                 # 🔒 ＝ 生產碼 `_IFACE_TOL`（⛔ 器內另定·僅供出艙之判讀）
REF_LOG = "verify/out/WG9277R_wchain.log"
FOCUS = ("R4", "right")         # 🔒 單 `§四` 項 `1` 之受詞

# 🔒 造甲之三實參（**逐字**自 `GB-168` 一次／二次精化·⛔ 人造之數）
CA_ARGS = [(0.1775004071, 14.1988975422),
           (0.0, 14.1988975422),
           (0.0, 14.0213971351)]
# 🔒 外部錨（⛔ 重測甲態）：`GB-168` 原節所載之**態乙**配地宗數
GB168_LOTS_B = {"0m": 20, "3.5m": 22}
# 🔒 外部錨：`GB-170` 三格之 `抵費地面積＝range(㎡)`
GB170 = [("0m", "R4", "左", 116.08), ("3.5m", "R2", "左", 308.17),
         ("3.5m", "R4", "左", 226.01)]


def say(s=""):
    print(s)


def _norm_side(s):
    if s is None:
        return None
    t = str(s)
    if "左" in t or t.lower().startswith("l"):
        return "left"
    if "右" in t or t.lower().startswith("r"):
        return "right"
    return None


def drive(sb, shim_set, mode):
    """一情境一次驅動。`shim_set` ＝ `None`（替身**關**）或 `set of (blk, side)`（替身**開**）。

    🔒 **態乙**：`WV_K6_STEP0=off`（⛔ 於父行程持久設定——本器之行程即驅動之行程）。
    """
    os.environ[ENV] = STATE_B
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import probe_WG9269_c4_gamma as G4

    ns, fake_st = harvest()
    rwi, solved, pool, slots = [], [], {}, []
    stat = {"hit": 0, "skip_b": 0, "skip_unknown": 0, "head_calls": 0,
            "hit_pk": 0, "hit_sg": 0}
    phase = {"v": "pk"}
    _o_rwi = ns["rw_increment"]
    _o_solve = ns["_solve_G_one"]
    _o_pool = ns["_pool_strips_for_block"]
    _o_slot = ns["_select_pool_slot"]

    def _climb(names, upto=16):
        out = {k: None for k in names}
        for d in range(1, upto + 1):
            try:
                f = sys._getframe(d + 1)       # 🔒 +1 ＝ 補本函式自身之一層（坑 `bb`）
            except ValueError:
                break
            for k in names:
                if out[k] is None and k in f.f_locals:
                    out[k] = f.f_locals[k]
        return out

    def _spy_rwi(W_prev, W_cur):
        p = _climb(["is_corner", "is_chain_head", "blk_label", "side", "tp"])
        # 🔒 鏈頭之判準 ＝ 碼面之同一運算式（自呼叫端之區域名取值·⛔ 第二份判準）
        is_head = bool(p.get("is_corner")) or bool(p.get("is_chain_head"))
        blk = p.get("blk_label")
        sd = _norm_side(p.get("side"))
        used_prev, used_cur = float(W_prev), float(W_cur)
        if is_head:
            stat["head_calls"] += 1
            if shim_set is not None:
                if blk is None or sd is None:
                    stat["skip_unknown"] += 1          # 🛑 loud·⛔ 靜默
                elif (blk, sd) not in shim_set:
                    stat["skip_b"] += 1                # 情形乙 或 非受詞側
                else:
                    if mode == "alpha":
                        used_prev, used_cur = 0.0, float(W_cur)
                    elif mode == "beta":
                        used_prev, used_cur = 0.0, float(W_cur) - float(W_prev)
                    else:                              # 🛑 ⛔ 靜默退路
                        raise RuntimeError("未知之替身模式：%r" % (mode,))
                    stat["hit"] += 1
                    stat["hit_pk" if phase["v"] == "pk" else "hit_sg"] += 1
        out = _o_rwi(used_prev, used_cur)
        tp = p.get("tp") or {}
        rwi.append({"W_prev_orig": float(W_prev), "W_prev_used": used_prev,
                    "W_cur_orig": float(W_cur), "W_cur_used": used_cur,
                    "out": float(out), "is_head": is_head, "blk": blk, "side": sd,
                    "lot": (tp.get("暫編地號") if isinstance(tp, dict) else None),
                    "phase": phase["v"]})
        return out

    def _spy_solve(**kw):
        res = _o_solve(**kw)
        p = _climb(["blk_label", "side", "tp"])
        tp = p.get("tp") or {}
        try:
            r = res[0] if isinstance(res, tuple) else res
        except Exception:                                       # noqa: BLE001
            r = res
        if isinstance(r, dict):
            solved.append({
                "blk": p.get("blk_label"), "side": _norm_side(p.get("side")),
                "lot": (tp.get("暫編地號") if isinstance(tp, dict) else None),
                "G": r.get("G"), "area_geom": r.get("area_geom"),
                "Rw_pct": r.get("Rw_pct"), "S": r.get("S"),
                "width": r.get("_宗地寬度"),
                "W": r.get("W"), "W_far": r.get("W_far"),
                "W_rw_start": r.get("W_rw_start"), "phase": phase["v"]})
        return res

    def _spy_pool(*a, **kw):
        out = _o_pool(*a, **kw)
        p = _climb(["blk_label"])
        b = p.get("blk_label")
        try:
            areas = [float(g.area) for g in (out or [])]
        except Exception:                                       # noqa: BLE001
            areas = None
        pool.setdefault(b, []).append(areas)
        return out

    def _spy_slot(widths, left, right):
        out = _o_slot(widths, left, right)
        lab = None
        try:
            lab = sys._getframe(1).f_locals.get("blk_label")     # 🔒 唯讀內省
        except Exception:                                       # noqa: BLE001
            raise                                               # 🛑 ⛔ 靜默吞
        slots.append({"blk": lab, "widths": list(widths or []),
                      "left": dict(left or {}), "right": dict(right or {}),
                      "res": out})
        return out                                              # 🛑 逐位原樣回傳

    ns["rw_increment"] = _spy_rwi
    ns["_solve_G_one"] = _spy_solve
    ns["_pool_strips_for_block"] = _spy_pool
    ns["_select_pool_slot"] = _spy_slot

    snapshot = rv.load_snapshot()
    cb_by, cad = rv.build_pipeline(ns, fake_st, snapshot)
    rv.build_ownership(ns, fake_st, rv.ANON_XLSX)
    with open(rv.V6DXF, "rb") as f:
        v6 = f.read()
    temp_p, build_p, _ = rv.build_build_parcels(
        ns, fake_st, v6, list(cb_by.values()), snapshot)
    params = rv.build_param_table(ns, fake_st, cb_by, cad, snapshot, sb)
    _d, _s, _off, wins, forced = run_corner_pk(
        ns, fake_st, list(cb_by.values()), cad, params, temp_p, build_p,
        sb, snapshot=snapshot)
    phase["v"] = "sg"
    err, g_rows = None, []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb, eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e)
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    reached = []
    for r in g_rows:
        b = r.get("所屬街廓")
        if b and b not in reached:
            reached.append(b)
    return {"off": list(_off or []), "rwi": rwi, "solved": solved, "pool": pool,
            "g_rows": g_rows, "rows": rows, "build_p": build_p, "slots": slots,
            "err": err, "reached": reached, "stat": stat, "skipped": _sk}


def _final(solved, phase="sg"):
    d = {}
    for r in solved:
        if r["phase"] != phase or r["blk"] is None or r["lot"] is None:
            continue
        d[(r["blk"], r["side"], r["lot"])] = r
    return d


def _w0_by_side(rwi, phase="sg"):
    """鏈頭之 `W_0`（＝替身**未**介入之原實參）·每 (blk, side) 取其最末一筆。"""
    d = {}
    for r in rwi:
        if r["phase"] != phase or not r["is_head"] or r["blk"] is None or r["side"] is None:
            continue
        d[(r["blk"], r["side"])] = r["W_prev_orig"]
    return d


def _parse_ref_w0_B(txt):
    """自 `W-G.9-277` 落檔解其 `W_0` 表之**態乙**二欄（`0m` 態乙 ＝ 第 `2` 欄／`3.5m` 態乙 ＝ 第 `4` 欄）。

    🔒 底本 `probe_WG9278_w0zero.py` 之 `_parse_ref_w0` 取 `(0, 2)`（**態甲**）；
       本器之驅動母體為**態乙** ⇒ 取 `(1, 3)`。⛔ 其餘一字未動。
    """
    import re as _re
    out = {}
    for ln in txt.split("\n"):
        m = _re.match(r"^\s*\|\s*`(R\d)`\s*\|\s*(left|right)\s*\|(.*)\|\s*$", ln)
        if not m:
            continue
        cells = [c.strip() for c in m.group(3).split("|")]
        if len(cells) != 4:
            continue
        for idx, tag in ((1, "0m"), (3, "3.5m")):        # 🔒 態乙 ＝ 第 2／第 4 欄
            mm = _re.match(r"^`(-?[0-9.]+)`", cells[idx])
            if mm:
                out[(tag, m.group(1), m.group(2))] = float(mm.group(1))
    return out


def main():
    if MODE not in ("alpha", "beta"):
        say("🛑 用法：python %s <倉根> <alpha|beta>" % os.path.basename(__file__))
        return 2
    import probe_WG9273_delta_locate as D          # 🔒 theo／real 之單一產生者

    say("=" * W)
    say("【`W-G.9-315`】`K-9-5-12` 反事實之**態乙**驅動｜替身 ＝ **`%s`**" % MODE)
    say("=" * W)
    say("\U0001f6d1 **⛔ 落地、⛔ 稱本器為「落地」、⛔ 判 `K-9-5-12` 應否落地、"
        "⛔ 判孰為正確之 `W`、⛔ 提修法主張、⛔ 判結構閘應否放寬或停用。**")
    say("\U0001f512 零之判準 ＝ 具名常數 `TOL0 = %g`；`_IFACE_TOL` ＝ `%g`（＝ 生產碼之值）" % (TOL0, IFACE_TOL))
    say("\U0001f512 驅動母體 ＝ **態乙**（`%s=%s`）｜情境 ＝ %s" % (ENV, STATE_B, [("%gm" % s) for s in SBS]))
    say("\U0001f512 替身之逐字：`α` ⇒ `rw_increment(0.0, W_cur)`；"
        "`β` ⇒ `rw_increment(0.0, W_cur - W_prev)`")

    OFF, ON = {}, {}
    for sb in SBS:
        OFF["%gm" % sb] = drive(sb, None, None)      # 替身**關**（同次驅動內之未替身基線）

    # ── 情形甲／乙之判別 ──────────────────────────────────────────
    say("")
    say("─" * W)
    say("【前置】情形甲／乙之判別（源 ＝ `run_corner_pk` 之第三回傳 `_off`）")
    say("─" * W)
    FORCED = {}
    for tag in ("0m", "3.5m"):
        rows = OFF[tag]["off"]
        say("   · `%s` 之 `_off` 列數 ＝ **%d**｜逐列逐字：" % (tag, len(rows)))
        for r in rows:
            say("     - %r" % (r,))
            b = str(r.get("街廓", ""))
            sd = _norm_side(r.get("端"))
            if "強制抵費地" in str(r.get("指配", "")) and b and sd:
                FORCED.setdefault(tag, set()).add((b, sd))
        FORCED.setdefault(tag, set())
    say("   | 街廓 | 側 | `0m` 情形 | `3.5m` 情形 |")
    say("   |---|---|---|---|")
    for b in BLKS:
        for sd in ("left", "right"):
            say("   | `%s` | %s | %s | %s |"
                % (b, sd,
                   "乙（強制抵費地·⛔ 模擬）" if (b, sd) in FORCED["0m"] else "甲（可模擬）",
                   "乙（強制抵費地·⛔ 模擬）" if (b, sd) in FORCED["3.5m"] else "甲（可模擬）"))
    say("   \U0001f512 **判別力**：乙 之總數 ＝ `0m` **%d**／`3.5m` **%d**"
        % (len(FORCED["0m"]), len(FORCED["3.5m"])))

    # ── 自證閘（先決） ────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【自證閘·先決】替身**關**之鏈頭 `W_0` vs `%s` 之**態乙**二欄" % REF_LOG)
    say("─" * W)
    refp = os.path.join(REPO, REF_LOG)
    if not os.path.exists(refp):
        say("   \U0001f6d1 參照落檔不存在 ⇒ loud 拒測（`rc = 5`）")
        return 5
    ref = _parse_ref_w0_B(io.open(refp, encoding="utf-8").read())
    say("   · 參照之格數（態乙）＝ **%d**" % len(ref))
    bad, cmp_n = [], 0
    for tag in ("0m", "3.5m"):
        cur = _w0_by_side(OFF[tag]["rwi"])
        for (b, sd), v in sorted(cur.items()):
            k = (tag, b, sd)
            if k not in ref:
                bad.append((k, v, "參照無此格"))
                continue
            cmp_n += 1
            if ("%.10f" % v) != ("%.10f" % ref[k]):
                bad.append((k, v, ref[k]))
    say("   · 所比之格數 ＝ **%d**｜相異 ＝ **%d**" % (cmp_n, len(bad)))
    for x in bad:
        say("     \U0001f534 %r" % (x,))
    if bad or cmp_n == 0:
        say("   \U0001f6d1 **自證閘不過** ⇒ loud 拒測（`rc = 5`），**⛔ 出艙任何反事實之數**。")
        return 5
    say("   ⇒ **逐位相同** ✅")
    fake = "%.10f" % 123456.789                      # 🔒 坑 `bd`：執行期組出·⛔ 字面出艙
    say("   \U0001f512 **判別力**：一人造值（**執行期組出**）與參照任一格比 ⇒ %s"
        % ("相異 ✅（該檢非恆綠）" if fake not in {"%.10f" % v for v in ref.values()}
           else "\U0001f534 相符"))

    # ── 判別力三造 ────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【判別力三造】造甲[必有差·純函式層]／造乙[必無差]／造丙[替身確已生效]")
    say("─" * W)
    os.environ[ENV] = STATE_B
    for m in ("app_harvest",):
        sys.modules.pop(m, None)
    from app_harvest import harvest as _hv
    _ns_pure, _ = _hv()
    _rwi_pure = _ns_pure["rw_increment"]
    say("   · **造甲**（⛔ 驅動管線·三實參逐字自 `GB-168` 一次／二次精化）：")
    vals = []
    for (a, b2) in CA_ARGS:
        v = float(_rwi_pure(a, b2))
        vals.append(v)
        say("     - `rw_increment(%.10f, %.10f)` ＝ **`%.6f`**" % (a, b2, v))
    pairs = [(0, 1), (0, 2), (1, 2)]
    diffs = [(i, j, abs(vals[i] - vals[j])) for i, j in pairs]
    for i, j, d in diffs:
        say("     - `|(%d) − (%d)|` ＝ `%.10f` ⇒ %s"
            % (i + 1, j + 1, d, "相異 ✅" if d > TOL0 else "\U0001f534 **相同**"))
    ca_ok = all(d > TOL0 for _, _, d in diffs)
    say("     ⇒ **造甲** ＝ %s（期：三者兩兩相異）" % ("🔴 有差 ✅" if ca_ok else "🛑 未全相異"))

    say("   · **造乙**（`W_prev ≤ 0` 之鏈頭 ⇒ 替身 `α` 之 `|ΔRw| ≤ TOL0`）：")
    say("     🔒 **本造施於<u>純函式層</u>**（受詞 ＝ 基線所錄之鏈頭實參對）——"
        "⛔ 另跑管線（單 `§四`：驅動次數 ＝ 二）。")
    cb_rows, cb_bad = [], 0
    for tag in ("0m", "3.5m"):
        for r in OFF[tag]["rwi"]:
            if r["phase"] != "sg" or not r["is_head"]:
                continue
            if r["blk"] is None or r["side"] is None:
                continue
            if (r["blk"], r["side"]) in FORCED[tag]:
                continue
            if r["W_prev_orig"] > 0:
                continue
            o = float(_rwi_pure(r["W_prev_orig"], r["W_cur_orig"]))
            n = float(_rwi_pure(0.0, r["W_cur_orig"]))
            d = abs(n - o)
            cb_rows.append((tag, r["blk"], r["side"], r["W_prev_orig"], o, n, d))
            if d > TOL0:
                cb_bad += 1
    say("     | 情境 | 街廓 | 側 | `W_prev` | `Rw`(原) | `Rw`(α) | `|ΔRw|` | 判 |")
    say("     |---|---|---|---|---|---|---|---|")
    for tag, b, sd, w0, o, n, d in cb_rows:
        say("     | `%s` | `%s` | %s | `%.10f` | `%.10f` | `%.10f` | `%.10f` | %s |"
            % (tag, b, sd, w0, o, n, d, "✅" if d <= TOL0 else "\U0001f534"))
    cb_ok = (len(cb_rows) > 0 and cb_bad == 0)
    say("     ⇒ **造乙** 格數 ＝ **%d**（須 `> 0`）｜`|ΔRw| > TOL0` 者 ＝ **%d** ⇒ %s"
        % (len(cb_rows), cb_bad,
           "🟢 無差 ✅" if cb_ok else ("🛑 母體為空 ⇒ 【⛔ 可得】" if not cb_rows else "\U0001f534 有差")))

    # ── 替身**開** ────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【驅動】替身**開**（`%s`）·受詞 ＝ 情形甲之側" % MODE)
    say("─" * W)
    for sb in SBS:
        tag = "%gm" % sb
        allow = {(b, sd) for b in BLKS for sd in ("left", "right")} - FORCED[tag]
        ON[tag] = drive(sb, allow, MODE)
        st = ON[tag]["stat"]
        say("   · `%s`｜鏈頭呼叫 ＝ **%d**｜**咬到 ＝ %d**（pk 段 %d／stepG 段 %d）"
            "｜跳過（情形乙或非受詞）＝ %d｜\U0001f7e1 跳過（**不可判**）＝ **%d**"
            % (tag, st["head_calls"], st["hit"], st["hit_pk"], st["hit_sg"],
               st["skip_b"], st["skip_unknown"]))
    say("   · **造丙**（替身確已生效·反空操作）：逐格具名之咬到：")
    cc_n = 0
    say("     | 情境 | 街廓 | 側 | 段 | `W_prev`(原) | `W_cur`(原) | `W_prev`(用) | `W_cur`(用) |")
    say("     |---|---|---|---|---|---|---|---|")
    for tag in ("0m", "3.5m"):
        for r in ON[tag]["rwi"]:
            if not r["is_head"] or r["W_prev_used"] != 0.0:
                continue
            if r["W_prev_orig"] == 0.0 and r["W_cur_used"] == r["W_cur_orig"]:
                continue        # ⛔ 誤計未被替身改動之格
            cc_n += 1
            say("     | `%s` | `%s` | %s | %s | `%.10f` | `%.10f` | `%.10f` | `%.10f` |"
                % (tag, r["blk"], r["side"], r["phase"], r["W_prev_orig"],
                   r["W_cur_orig"], r["W_prev_used"], r["W_cur_used"]))
    hit_tot = sum(ON[t]["stat"]["hit"] for t in ("0m", "3.5m"))
    unk_tot = sum(ON[t]["stat"]["skip_unknown"] for t in ("0m", "3.5m"))
    cc_ok = hit_tot > 0
    say("     ⇒ **造丙** 咬到總數 ＝ **%d**（須 `> 0`）｜可見之改動格 ＝ **%d**"
        "｜\U0001f7e1 不可判 ＝ **%d** ⇒ %s"
        % (hit_tot, cc_n, unk_tot, "✅" if cc_ok else "\U0001f6d1 **替身未生效**"))
    say("   \U0001f512 **反靜默退路**：咬到為 `0` 而結論為「無變化」者，一律先當作替身未生效。")

    say("")
    say("   \U0001f512 **三造之合判**：造甲 %s ⋀ 造乙 %s ⋀ 造丙 %s"
        % ("🔴 有差" if ca_ok else "🛑", "🟢 無差" if cb_ok else "🛑", "✅" if cc_ok else "🛑"))
    if not (ca_ok and cb_ok and cc_ok):
        say("   \U0001f6d1 **器紅** ⇒ **⛔ 出艙項 `1`〜`5` 任一數**（`rc = 5`）。")
        return 5
    say("   ⇒ **器非紅** ✅")

    # ── 項 1 ─────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `1`】`%s` `%s` 之 `理論@k*`／`實跑(階段1)`／`Δ` ＋ 結構閘破否"
        % (FOCUS[0], FOCUS[1]))
    say("─" * W)
    say("   \U0001f512 取法 ＝ **import** `probe_WG9273_delta_locate` 之 `theo`／`real`（⛔ 第二份判準）")
    say("   | 情境 | 替身 | `理論@k*`（未捨入） | `2dp` | `實跑(階段1)` | `Δ`（未捨入） | `2dp` | 破否 |")
    say("   |---|---|---|---|---|---|---|---|")
    for tag in ("0m", "3.5m"):
        for lab, DD in (("關", OFF[tag]), (MODE, ON[tag])):
            t, k, diag = D.theo(DD, FOCUS[0], FOCUS[1])
            r, used, s2 = D.real(DD, FOCUS[0], FOCUS[1])
            broke = ("結構閘 理論＝實跑 破" in str(DD["err"] or ""))
            if t is None:
                say("   | `%s` | %s | 【**⛔ 可得**】（%s） | — | `%s` | 【**⛔ 可得**】 | — | %s |"
                    % (tag, lab, diag, r, "🔴 破" if broke else "🟢 未破"))
                continue
            d = abs(t - r)
            say("   | `%s` | %s | `%.10f`（`k*`＝%s） | `%.2f` | `%.2f` | `%.10f` | `%.2f` | %s |"
                % (tag, lab, t, k, t, r, d, d, "🔴 破" if broke else "🟢 未破"))
    say("")
    say("   · **結構閘之訊息逐字**（`err` 之首行）：")
    for tag in ("0m", "3.5m"):
        for lab, DD in (("關", OFF[tag]), (MODE, ON[tag])):
            e = (DD["err"] or "").split("\n")[0]
            say("     - `%s`／替身%s ⇒ %s" % (tag, lab, ("`%s`" % e) if e else "**⛔ 中止**（無 `err`）"))

    # ── 項 2 ─────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `2`】六街廓 × 二側之**到達與判**（🟢 已執行且通過／🛑 未執行／🔴 已執行且破／⛔ 可得）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        for lab, DD in (("關", OFF[tag]), (MODE, ON[tag])):
            reached = DD["reached"]
            e = (DD["err"] or "").split("\n")[0]
            say("   · `%s` 替身%s｜到達 ＝ %r｜中止 ＝ %s" % (tag, lab, reached, e or "（無）"))
            say("     | 街廓 | left | right |")
            say("     |---|---|---|")
            for b in BLKS:
                cells = []
                for sd in ("left", "right"):
                    if b not in reached:
                        cells.append("🛑 未執行")
                    elif ("街廓 %s %s 側" % (b, sd)) in (DD["err"] or ""):
                        cells.append("🔴 已執行且破")
                    else:
                        cells.append("🟢 已執行且通過")
                say("     | `%s` | %s | %s |" % (b, cells[0], cells[1]))

    # ── 項 3 ─────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `3`】**配地宗集合之宗數**（框 ＝ `推進側別 ∈ {left, right}`）"
        "·與 `GB-168` 原節之**態乙**值對拍（⛔ 重測甲態）")
    say("─" * W)
    say("   | 情境 | 替身 | 配地宗數 | `GB-168` 態乙 | 判 |")
    say("   |---|---|---|---|---|")
    for tag in ("0m", "3.5m"):
        for lab, DD in (("關", OFF[tag]), (MODE, ON[tag])):
            n = sum(1 for r in DD["rows"]
                    if (r.get("推進側別") or "").strip() in ("left", "right"))
            exp = GB168_LOTS_B[tag]
            say("   | `%s` | %s | **%d** | `%d` | %s |"
                % (tag, lab, n, exp,
                   ("✅ 逐位相符" if n == exp else "\U0001f534 相異 %+d" % (n - exp))
                   if lab == "關" else ("＝ 基線" if n == exp else "**相異 %+d**" % (n - exp))))

    # ── 項 4 ─────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `4`】逐街廓之 **`抵費地面積＝range(㎡)`**（源 ＝ `run_corner_pk` 之第三回傳 `_off`）"
        "·與 `GB-170` 三格對拍")
    say("─" * W)
    say("   | 情境 | 替身 | 街廓 | 端 | `抵費地面積＝range(㎡)` |")
    say("   |---|---|---|---|---|")
    got = {}
    for tag in ("0m", "3.5m"):
        for lab, DD in (("關", OFF[tag]), (MODE, ON[tag])):
            for r in DD["off"]:
                v = r.get("抵費地面積＝range(㎡)")
                say("   | `%s` | %s | `%s` | %s | `%s` |"
                    % (tag, lab, r.get("街廓"), r.get("端"), v))
                got[(tag, lab, str(r.get("街廓")), str(r.get("端")))] = v
    say("")
    say("   · **與 `GB-170` 三格之逐位對拍**（替身**關** ＝ 基線）：")
    say("   | 情境 | 街廓 | 端 | 倉載 | 實得 | 判 |")
    say("   |---|---|---|---|---|---|")
    for tag, b, end, exp in GB170:
        v = got.get((tag, "關", b, end))
        ok = (v is not None and abs(float(v) - exp) < 5e-3)
        say("   | `%s` | `%s` | %s | `%.2f` | %s | %s |"
            % (tag, b, end, exp, ("`%s`" % v) if v is not None else "【**⛔ 可得**】",
               "✅ 逐位相符" if ok else "\U0001f534 相異／⛔ 可得"))

    # ── 項 5 ─────────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `5`】`ΔΣG`／`ΔΣ抵費地面積`（替身開／關之差·關 ＝ **同次驅動內之未替身基線**）")
    say("   🔒 **帶號合計與絕對值合計並列**（`CLAUDE.md`）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        fo, fn = _final(OFF[tag]["solved"]), _final(ON[tag]["solved"])
        ks = sorted(set(fo) & set(fn))
        dG = [float(fn[k]["G"]) - float(fo[k]["G"]) for k in ks
              if fo[k].get("G") is not None and fn[k].get("G") is not None]
        po = sum(sum(v[-1]) for v in OFF[tag]["pool"].values() if v and v[-1])
        pn = sum(sum(v[-1]) for v in ON[tag]["pool"].values() if v and v[-1])
        say("   · `%s`｜共有之宗 ＝ **%d**（關 %d／開 %d·只在一側者 %d）"
            % (tag, len(ks), len(fo), len(fn), len(set(fo) ^ set(fn))))
        say("     **`ΔΣG` ＝ `%+.10f`**｜**`Σ|ΔG|` ＝ `%.10f`**"
            % (sum(dG), sum(abs(x) for x in dG)))
        say("     **`ΔΣ抵費地面積` ＝ `%+.10f`**（關 `%.10f` → 開 `%.10f`）" % (pn - po, po, pn))
    say("")
    say("   · **逐宗 `ΔRw`／`ΔG`（未捨入·僅列非零者）**：")
    say("     | 情境 | 街廓 | 側 | 宗 | `ΔRw`(%) | `ΔG`(㎡) |")
    say("     |---|---|---|---|---|---|")
    nz = 0
    for tag in ("0m", "3.5m"):
        fo, fn = _final(OFF[tag]["solved"]), _final(ON[tag]["solved"])
        for k in sorted(set(fo) & set(fn), key=lambda k: (k[0], str(k[1]), str(k[2]))):
            a, b2 = fo[k], fn[k]

            def _d(f):
                x, y = a.get(f), b2.get(f)
                return None if (x is None or y is None) else float(y) - float(x)
            drw, dg = _d("Rw_pct"), _d("G")
            if (drw is None or abs(drw) <= TOL0) and (dg is None or abs(dg) <= TOL0):
                continue
            nz += 1
            say("     | `%s` | `%s` | %s | `%s` | %s | %s |"
                % (tag, k[0], k[1], k[2],
                   ("`%+.10f`" % drw) if drw is not None else "【⛔ 可得】",
                   ("`%+.10f`" % dg) if dg is not None else "【⛔ 可得】"))
    say("     ⇒ 非零之宗 ＝ **%d**（⛔ 以「反正都是 `0`」頂替·造丙之咬到 ＝ %d）" % (nz, hit_tot))

    say("")
    say("RESULT=OK MODE=%s" % MODE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
