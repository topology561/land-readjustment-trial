# -*- coding: utf-8 -*-
"""`W-G.9-278` `§四-1`：**`W_0 → 0` 之反事實量測**（🛑 **⛔ 落地**·替身僅於本器之驅動中生效）。

🔒 **底本** ＝ `verify/probes/probe_WG9277_wchain.py` 之 `drive`（⛔ 另寫第二份判準）。

🛑 **替身之定義（發單側定·⛔ CC 自訂·單 `§四-1` 逐字）**
   · 包裹 `ns["rw_increment"]`；凡其呼叫端經**框內省**判定為**鏈頭**者，
     以 `rw_increment(0.0, W_cur)` 代之。
   · 「鏈頭」之判準**一律取碼面之同一運算式** `is_corner or is_chain_head`
     （自呼叫端之區域名取值），**⛔ 器內另寫第二份判準**。
   · 🛑 **⛔ 寫入倉之生產碼**。

🛑 **情形之分（⛔ 混同）**
   · **甲** ＝ 該側之街角**非**強制抵費地 ⇒ **可模擬**。
   · **乙** ＝ 該側之街角**為**強制抵費地 ⇒ 依 `K-9-5-12（四）` 其起算為
     「該抵費地之遠側境界線」、**⛔ 為 `0`** ⇒ 🛑 **⛔ 模擬**，出艙**第三種碼**。
   · 判別以 `run_corner_pk` 之**第三回傳**（`_off`·即 `verify/out/got_抵費地_退縮*.csv`
     之**同一產生者**）之 `指配` 欄為據；並與該 CSV **逐列對拍**。

🛑 **坑之攔法**：坑 `bb`（框內省 `sys._getframe(depth + 1)` ＋ 自我驗證閘）／
   坑 `bd`（**必為零之哨兵一律執行期組出·字面⛔ 出艙**）。

🛑 **判別力二造（單 `§四-1`）**
   甲[必有差] ＝ 任一 `|W_0| > TOL0` 之側 ⇒ 其 `Rw` 須變；
   乙[必無差] ＝ `|W_0| ≤ TOL0` 之側 ⇒ 其 `|ΔRw| ≤ TOL0`。**二造同色 ⇒ 器紅 `rc = 5`。**

🛑 **⛔ 判其為正確或錯誤、⛔ 提落地與否之主張、⛔ 稱其為「落地」。**

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9278_w0zero.py [倉根]`
`rc`：`0`／`5` **器紅**（自證閘不過／框內省閘不過／判別力二造同色）。
"""
import contextlib
import csv
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
W = 132
SBS = (0.0, 3.5)
BLKS = ["R1", "R2", "R3", "R4", "R5", "R6"]
TOL0 = 1e-6                     # 🔒 零之判準 ＝ 具名常數（承 `W-G.9-277` 之自捕·⛔ 字面）
REF_LOG = "verify/out/WG9277R_wchain.log"


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


def drive(sb, shim_set):
    """`shim_set` ＝ `None`（替身**關**）或 `set of (blk, side)`（替身**開**·只對該集合生效）。"""
    os.environ.pop(ENV, None)                 # 🔒 態甲（生產態·`WV_K6_STEP0` 未設）
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g

    ns, fake_st = harvest()
    rwi, solved, pool = [], [], {}
    stat = {"hit": 0, "skip_b": 0, "skip_unknown": 0, "head_calls": 0,
            "hit_pk": 0, "hit_sg": 0}
    phase = {"v": "pk"}
    _o_rwi = ns["rw_increment"]
    _o_solve = ns["_solve_G_one"]
    _o_pool = ns["_pool_strips_for_block"]

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
        used_prev = float(W_prev)
        if is_head:
            stat["head_calls"] += 1
            if shim_set is not None:
                if blk is None or sd is None:
                    stat["skip_unknown"] += 1          # 🛑 loud·⛔ 靜默
                elif (blk, sd) not in shim_set:
                    stat["skip_b"] += 1                # 情形乙 或 非受詞側
                else:
                    used_prev = 0.0
                    stat["hit"] += 1
                    stat["hit_pk" if phase["v"] == "pk" else "hit_sg"] += 1
        out = _o_rwi(used_prev, W_cur)
        tp = p.get("tp") or {}
        rwi.append({"W_prev_orig": float(W_prev), "W_prev_used": used_prev,
                    "W_cur": float(W_cur), "out": float(out),
                    "is_head": is_head, "blk": blk, "side": sd,
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

    ns["rw_increment"] = _spy_rwi
    ns["_solve_G_one"] = _spy_solve
    ns["_pool_strips_for_block"] = _spy_pool

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
        err = str(e).split("\n")[0][:180]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    reached = []
    for r in g_rows:
        b = r.get("所屬街廓")
        if b and b not in reached:
            reached.append(b)
    return {"off": list(_off or []), "rwi": rwi, "solved": solved, "pool": pool,
            "g_rows": g_rows, "err": err, "reached": reached, "stat": stat,
            "wins": wins}


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


def _parse_ref_w0(txt):
    """自 `W-G.9-277` 落檔解其 `W_0` 表之**態甲**二欄（`0m`／`3.5m`）。"""
    out = {}
    for ln in txt.split("\n"):
        m = re.match(r"^\s*\|\s*`(R\d)`\s*\|\s*(left|right)\s*\|(.*)\|\s*$", ln)
        if not m:
            continue
        cells = [c.strip() for c in m.group(3).split("|")]
        if len(cells) != 4:
            continue
        for idx, tag in ((0, "0m"), (2, "3.5m")):        # 態甲 ＝ 第 1／第 3 欄
            mm = re.match(r"^`(-?[0-9.]+)`", cells[idx])
            if mm:
                out[(tag, m.group(1), m.group(2))] = float(mm.group(1))
    return out


def main():
    say("=" * W)
    say("【`W-G.9-278` `§四-1`】`W_0 → 0` 之**反事實量測**"
        "（態甲 × 二情境 × 替身關／開 ＝ 四次）")
    say("=" * W)
    say("\U0001f6d1 **⛔ 判其為正確或錯誤、⛔ 提落地與否"
        "之主張、⛔ 稱其為「落地」**——出舱即止。")
    say("\U0001f512 零之判準 ＝ 具名常數 `TOL0 = %g`" % TOL0)

    OFF, ON = {}, {}
    # ── 前置：替身**關**（亦即 `W-G.9-277` 之態）────────────────────
    for sb in SBS:
        OFF["%gm" % sb] = drive(sb, None)

    # ── 情形甲／乙之判別（`_off` 之 `指配` 欄）──────────────────────
    say("")
    say("─" * W)
    say("【項 `1`】情形甲／乙之判別（源 ＝ `run_corner_pk` "
        "之第三回傳 `_off`·即 `got_抵費地_退縮*.csv` 之同一產生者）")
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
    say("")
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

    # ── 與 `got_抵費地_退縮*.csv` 逐列對拍 ────────────────────────
    say("")
    say("   · 與 `verify/out/got_抵費地_退縮*.csv` 之逐列對拍：")
    for tag in ("0m", "3.5m"):
        p = os.path.join(REPO, "verify", "out",
                         "got_抵費地_退縮%s.csv" % tag)
        if not os.path.exists(p):
            say("     - `%s` ⇒ \U0001f7e1 **檔不存在** ⇒ 【**⛔ 可得**】"
                "（第三種碼·⛔ 以「相符」頂替）" % p)
            continue
        with io.open(p, encoding="utf-8-sig", newline="") as fh:
            crows = list(csv.DictReader(fh))
        say("     - `%s` ⇒ %d 列｜逐列 ＝ %r" % (os.path.basename(p), len(crows), crows))
        say("       → 與 `_off`（%d 列）之列數 %s"
            % (len(OFF[tag]["off"]),
               "**相同** ✅" if len(crows) == len(OFF[tag]["off"]) else "\U0001f534 **相異**"))

    # ── 自證閘（先決）：替身關 vs `W-G.9-277` 落檔 ────────────────
    say("")
    say("─" * W)
    say("【自證閘·先決】替身**關**之輸出 vs `%s`" % REF_LOG)
    say("─" * W)
    refp = os.path.join(REPO, REF_LOG)
    if not os.path.exists(refp):
        say("   \U0001f6d1 參照落檔不存在 ⇒ loud 拒測")
        return 5
    ref = _parse_ref_w0(io.open(refp, encoding="utf-8").read())
    say("   · 所比對之欄 ＝ **鏈頭之 `W_0`**"
        "（`W-G.9-277R` 落檔之 `W_0` 表之**態甲**二欄）")
    say("   · 參照之格數 ＝ **%d**" % len(ref))
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
        say("   \U0001f6d1 **自證閘不過** ⇒ loud 拒測（`rc = 5`）"
            "，**⛔ 出舱任何反事實之數**。")
        return 5
    say("   ⇒ **逐位相同** ✅")
    fake = "%.10f" % 123456.789
    say("   \U0001f512 **判別力**：一人造值（**執行期組出**）"
        "與參照任一格比 ⇒ %s"
        % ("相異 ✅（該檢非恆綠）"
           if fake not in {"%.10f" % v for v in ref.values()} else "\U0001f534 相符"))

    # ── 替身**開** ────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【驅動】替身**開**（受詞 ＝ 情形甲之側）")
    say("─" * W)
    for sb in SBS:
        tag = "%gm" % sb
        allow = {(b, sd) for b in BLKS for sd in ("left", "right")} - FORCED[tag]
        ON[tag] = drive(sb, allow)
        st = ON[tag]["stat"]
        say("   · `%s`｜鏈頭呼叫 ＝ **%d**｜**咬到 ＝ %d**"
            "（pk 段 %d／stepG 段 %d）｜跳過（情形乙或非受詞）＝ %d"
            "｜\U0001f7e1 跳過（**不可判**）＝ **%d**"
            % (tag, st["head_calls"], st["hit"], st["hit_pk"], st["hit_sg"],
               st["skip_b"], st["skip_unknown"]))
    say("   \U0001f512 **反靜默退路之計數**：咬到為 `0` 而結論為"
        "「無變化」者，一律先當作替身未生效。")

    # ── 判別力二造 ────────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【判別力二造】甲[必有差] `|W_0| > TOL0`｜"
        "乙[必無差] `|W_0| ≤ TOL0`（二造同色 ⇒ 器紅）")
    say("─" * W)
    say("   \U0001f6d1 **單內二處互斥（常規二·逐字回報）**："
        "單 `§四-1` 之判準逐字作 **`W_0 > 1e-6`**（**帶號**），"
        "而其括弧內所引之「已知 `14` 格」係 "
        "`W-G.9-277R` 之 **`|W_0| > 1e-6`** 之計數 ⇒ **二者相異**。")
    say("   ⇒ 本器**二讀法並報**：**帶號**（單之逐字）與"
        "**絕對值**（其所引之計數），並取**較嚴者**為判。")
    say("   | 情境 | 街廓 | 側 | `W_0` | 類（帶號） | 類（絕對值） | "
        "`Rw`(關) | `Rw`(開) | `ΔRw` | 判（帶號） |")
    say("   |---|---|---|---|---|---|---|---|---|---|")
    cls_a, cls_b = [], []
    cls_a_abs, cls_b_abs = [], []
    for tag in ("0m", "3.5m"):
        w0 = _w0_by_side(OFF[tag]["rwi"])
        fo = _final(OFF[tag]["solved"])
        fn = _final(ON[tag]["solved"])
        for (b, sd), v in sorted(w0.items()):
            if (b, sd) in FORCED[tag]:
                continue
            # 取該側之鏈頭宗（`solved` 中同 (blk, side) 之首宗）
            ka = [k for k in fo if k[0] == b and k[1] == sd]
            if not ka:
                continue
            k0 = ka[0]
            r_off = fo.get(k0)
            r_on = fn.get(k0)
            typ = "甲" if v > TOL0 else "乙"                    # 🔒 單之逐字：**帶號**
            typ_abs = "甲" if abs(v) > TOL0 else "乙"           # 其所引之計數：絕對值
            if r_off is None or r_on is None or r_off.get("Rw_pct") is None \
                    or r_on.get("Rw_pct") is None:
                say("   | `%s` | `%s` | %s | `%.10f` | %s | %s | — | — | 【**⛔ 可得**】 | \U0001f7e1 |"
                    % (tag, b, sd, v, typ, typ_abs))
                continue
            d = float(r_on["Rw_pct"]) - float(r_off["Rw_pct"])
            ok = (abs(d) > TOL0) if typ == "甲" else (abs(d) <= TOL0)
            (cls_a if typ == "甲" else cls_b).append(abs(d) > TOL0)
            (cls_a_abs if typ_abs == "甲" else cls_b_abs).append(abs(d) > TOL0)
            say("   | `%s` | `%s` | %s | `%.10f` | %s | %s | `%.10f` | `%.10f` | `%+.10f` | %s |"
                % (tag, b, sd, v, typ, typ_abs, float(r_off["Rw_pct"]),
                   float(r_on["Rw_pct"]), d, "✅" if ok else "\U0001f534"))
    say("")
    say("   · **帶號讀法**（單之逐字 `W_0 > TOL0`）："
        "造甲格數 ＝ **%d**｜其 `|ΔRw| > TOL0` 者 ＝ **%d**｜"
        "造乙格數 ＝ **%d**｜其 `|ΔRw| > TOL0` 者 ＝ **%d**"
        % (len(cls_a), sum(1 for x in cls_a if x), len(cls_b), sum(1 for x in cls_b if x)))
    say("   · **絕對值讀法**（其所引之計數 `|W_0| > TOL0`）："
        "造甲格數 ＝ **%d**｜其 `|ΔRw| > TOL0` 者 ＝ **%d**｜"
        "造乙格數 ＝ **%d**｜其 `|ΔRw| > TOL0` 者 ＝ **%d**"
        % (len(cls_a_abs), sum(1 for x in cls_a_abs if x),
           len(cls_b_abs), sum(1 for x in cls_b_abs if x)))
    say("")
    verdicts = []
    for nm, ca, cb in (("帶號", cls_a, cls_b), ("絕對值", cls_a_abs, cls_b_abs)):
        if not ca:
            verdicts.append((nm, "empty"))
            say("   \U0001f7e1 **%s讀法**：造甲之母體**為空** ⇒ "
                "【**⛔ 可得**】——**⛔ 以飽和者頂替、"
                "⛔ 逐稱器非紅**（`CLAUDE.md` 逐字）。" % nm)
        elif all(ca) and not any(cb):
            verdicts.append((nm, "green"))
            say("   ✅ **%s讀法**：二造异色 ⇒ 器非紅。" % nm)
        else:
            verdicts.append((nm, "red"))
            say("   \U0001f6d1 **%s讀法**：二造**同色** ⇒ **器紅**。" % nm)
    # 🔒 常規二：取**較嚴者**為判（red > empty > green）
    order = {"red": 2, "empty": 1, "green": 0}
    worst = max(verdicts, key=lambda x: order[x[1]])
    say("")
    say("   \U0001f512 **取較嚴者為判（常規二）** ＝ **%s讀法·%s**"
        % (worst[0], {"red": "器紅", "empty": "⛔ 可得", "green": "器非紅"}[worst[1]]))
    if worst[1] != "green":
        say("   \U0001f6d1 ⇒ **⛔ 出舱任何反事實之數**（`rc = 5`）。")
        say("   \U0001f50d **成因之碼面逐字**（`app.py` `rw_from_width`）："
            "`if W <= 0:` → `return 0.0` ⇒ **`R(W_0) ≡ 0` 對一切 `W_0 ≤ 0`**")
        say("     ⇒ `rw_increment(W_0, W_cur) ≡ rw_increment(0.0, W_cur)` 當 `W_0 ≤ 0`"
            " ⇒ 本反事實於該等側**結構上為空操作**。")
        return 5

    # ── 項 2：逐宗 Δ ──────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `2`】**逐宗** `ΔRw`／`ΔG`／`Δ幾何面積`（**未捨入**）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        fo, fn = _final(OFF[tag]["solved"]), _final(ON[tag]["solved"])
        keys = sorted(set(fo) | set(fn), key=lambda k: (k[0], str(k[1]), str(k[2])))
        say("   · `%s`｜宗數 關 ＝ %d／開 ＝ %d｜只在一側者 ＝ %d"
            % (tag, len(fo), len(fn), len(set(fo) ^ set(fn))))
        say("     | 街廓 | 側 | 宗 | `ΔRw`(%) | `ΔG`(㎡) | `Δ幾何面積`(㎡) |")
        say("     |---|---|---|---|---|---|")
        for k in keys:
            a, b2 = fo.get(k), fn.get(k)
            if a is None or b2 is None:
                say("     | `%s` | %s | `%s` | 【**⛔ 可得**】 | 【**⛔ 可得**】 | "
                    "【**⛔ 可得**】（只在%s側）|"
                    % (k[0], k[1], k[2], "關" if a else "開"))
                continue

            def _d(f):
                x, y = a.get(f), b2.get(f)
                return None if (x is None or y is None) else float(y) - float(x)
            drw, dg, dar = _d("Rw_pct"), _d("G"), _d("area_geom")
            say("     | `%s` | %s | `%s` | %s | %s | %s |"
                % (k[0], k[1], k[2],
                   ("`%+.10f`" % drw) if drw is not None else "【⛔ 可得】",
                   ("`%+.10f`" % dg) if dg is not None else "【⛔ 可得】",
                   ("`%+.10f`" % dar) if dar is not None else "【⛔ 可得】"))

    # ── 項 3：逐街廓 Δ抵費地 之逐片面積 ──────────────────────────
    say("")
    say("─" * W)
    say("【項 `3`】逐街廓 **`Δ抵費地` 之逐片面積**"
        "（源 ＝ `_pool_strips_for_block` 之回傳·**未捨入**）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        po, pn = OFF[tag]["pool"], ON[tag]["pool"]
        say("   · `%s`：" % tag)
        for b in BLKS:
            la = (po.get(b) or [[]])[-1] if po.get(b) else None
            lb = (pn.get(b) or [[]])[-1] if pn.get(b) else None
            if la is None or lb is None:
                say("     - `%s` ⇒ 【**⛔ 可得**】（關=%s／開=%s）"
                    % (b, "有" if la is not None else "無",
                       "有" if lb is not None else "無"))
                continue
            say("     - `%s` 關 ＝ %r" % (b, [round(x, 10) for x in la]))
            say("       `%s` 開 ＝ %r" % (b, [round(x, 10) for x in lb]))
            say("       Σ 關 ＝ `%.10f`｜Σ 開 ＝ `%.10f`｜**`ΔΣ` ＝ `%+.10f`**"
                % (sum(la), sum(lb), sum(lb) - sum(la)))

    # ── 項 4：守恆式 ─────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `4`】**守恆式**（`Σ配地幾何 ＋ Σ抵費地` vs `街廓面積`）"
        "·替身關／開 **各自**逐街廓")
    say("─" * W)
    say("   \U0001f6d1 源 ＝ `g_rows` 之 `幾何面積(㎡)`／`街廓面積(㎡)`"
        "（**已 `2dp` 捨入**·故殘差之量級受捨入層限制）")
    say("   | 情境 | 替身 | 街廓 | `Σ配地` | `Σ抵費地` | `合` | `街廓面積` | `殘差` |")
    say("   |---|---|---|---|---|---|---|---|")
    for tag in ("0m", "3.5m"):
        for lab, D2 in (("關", OFF[tag]), ("開", ON[tag])):
            agg = {}
            for r in D2["g_rows"]:
                b = r.get("所屬街廓")
                if not b:
                    continue
                e = agg.setdefault(b, {"a": 0.0, "p": 0.0, "blk": 0.0})
                ar = float(r.get("幾何面積(㎡)", 0.0) or 0.0)
                if "抵費地" in str(r.get("暫編地號", "")):
                    e["p"] += ar
                else:
                    e["a"] += ar
                e["blk"] = float(r.get("街廓面積(㎡)", 0.0) or 0.0)
            for b in BLKS:
                if b not in agg:
                    continue
                e = agg[b]
                say("   | `%s` | %s | `%s` | `%.4f` | `%.4f` | `%.4f` | `%.4f` | `%+.4f` |"
                    % (tag, lab, b, e["a"], e["p"], e["a"] + e["p"], e["blk"],
                       e["a"] + e["p"] - e["blk"]))

    # ── 項 5：六街廓之到達與否 ───────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `5`】六街廓之**到達與否**（反事實可能觸發別閘"
        " ⇒ **第三種碼**·⛔ 視為紅或綠）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        for lab, D2 in (("關", OFF[tag]), ("開", ON[tag])):
            say("   · `%s` 替身%s ⇒ 到達 ＝ %r｜中止 ＝ %s"
                % (tag, lab, D2["reached"], D2["err"]))

    # ── 項 6：Σ 層 ───────────────────────────────────────────────
    say("")
    say("─" * W)
    say("【項 `6`】`Σ` 層：全案 `ΔΣG`／`ΔΣ抵費地面積`"
        "（**帶號合計與絕對值合計並列**·`CLAUDE.md`）")
    say("─" * W)
    for tag in ("0m", "3.5m"):
        fo, fn = _final(OFF[tag]["solved"]), _final(ON[tag]["solved"])
        ks = sorted(set(fo) & set(fn))
        dG = [float(fn[k]["G"]) - float(fo[k]["G"]) for k in ks
              if fo[k].get("G") is not None and fn[k].get("G") is not None]
        po = sum(sum(v[-1]) for v in OFF[tag]["pool"].values() if v and v[-1])
        pn = sum(sum(v[-1]) for v in ON[tag]["pool"].values() if v and v[-1])
        say("   · `%s`｜共有之宗 ＝ **%d**｜**`ΔΣG` ＝ `%+.10f`**"
            "｜**`Σ|ΔG|` ＝ `%.10f`**" % (tag, len(ks), sum(dG), sum(abs(x) for x in dG)))
        say("     **`ΔΣ抵費地面積` ＝ `%+.10f`**（關 `%.10f` → 開 `%.10f`）"
            % (pn - po, po, pn))
    say("")
    say("RESULT=OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
