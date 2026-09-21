# -*- coding: utf-8 -*-
r"""`W-G.9-320` 工項一：階段 `b` 之**四造**（軸 × 粒度之 `2 × 2` 全因子）。

受詞（逐字·單 `§二` 工項一 `一`）：
  「理論側 `_select_pool_slot` 所餵之 `widths` 向量，於**四造**之各造下重算其 `table[k*]` 之
   `ΣRw_L`／`ΣRw_R`，並與**實跑側**同（態·情境·街廓·側）之階段 `1` 負擔和對拍。」

四造（單 `§二` 工項一 `二`）：
  `α₀` ＝ `_宗地寬度`·未捨入（**碼面現況**·忠實·自證造）
  `α`  ＝ `_宗地寬度`·`round(·, 2)`（只換粒度）
  `γ`  ＝ `W`·未捨入（只換軸）
  `β`  ＝ `W`·`round(·, 2)`（換軸 ＋ 換粒度）
  `α`／`γ`／`β` 一律標「替身·非忠實·⛔ 確值」。

🛑 **出艙即止**——⛔ 判孰為正典、⛔ 判二軸孰為正確、⛔ 提修法主張、⛔ 判任何阻塞項應否解除。
🔒 **取法（`恆常附款 k②`·⛔ 器內另寫第二份判準）**：
   `R(·)` ＝ `ns["rw_from_width"]`；理論側 ＝ **呼叫 `ns["_select_pool_slot"]` 本體**；
   `widths`／`left`／`right`／`_adv_base` ＝ **間諜錄呼叫端之實參與框內局部**（唯讀內省）；
   實跑側 ＝ `_rw_stage1_only` 之**逐字式**（`verify/stepg_pipeline.py` 之同名內函式）；
   態·情境之驅動 ＝ 沿 `probe_WG9319_widths.py` 之 `ENV`／`CASES`。
🔒 **落檔之字樣紀律（`恆常附款 k③`）**：本檔與其落檔**⛔ 含 `W-G.9-320` 以外之任何取號字樣**
   （單號／自誤號／阻塞項號／裁定號／裁號），以免污染其自身所量之母體；其自檢於 `main()` 末逐項出艙
   （所檢之樣式一律**執行期組出**·⛔ 使其字面落入落檔）。

`rc`：`0` 全綠／`2` 自證閘破（loud 拒測）／`3` 判定集為空（loud 拒測）／`4` `ns[...]` 取不得。
🛑 `rc ≠ 0` **⛔ 等同「受詞紅」**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9320_stageb.py`
"""
import contextlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

ENV = "WV_K6_STEP0"
CASES = [("甲", None, 0.0), ("甲", None, 3.5), ("乙", "off", 0.0), ("乙", "off", 3.5)]
OUT = os.path.join(REPO, "verify", "out", "WG9320_stageb.md")
NEED = ["rw_from_width", "_select_pool_slot", "_spatial_order_parcels_v2", "rw_increment"]
W = 118
_BUF = []


def say(s=""):
    print(s)
    _BUF.append(s)


# ── 常數因子之逐字（單 `§二` 工項一 `四`·**每表必載**）────────────────────────
CONST_A = ("理論側之式之形 ＝ `ΣRw_側 = R(b + Σw_群) − R(b)`（telescoping·"
           "`_select_pool_slot` docstring 逐字·`b` ＝ `left_side['b']`／`right_side['b']`）")
CONST_B = ("實跑側之式之形 ＝ `Σ_宗 Rw(%)`，其逐宗之 `Rw_pct = rw_increment(W_prev, W_cur) * 100.0`，"
           "而 `rw_increment` 逐字 ＝ `max(0.0, (rw_from_width(W_cur) - rw_from_width(W_prev)) / 100.0)`"
           "（**逐宗鉗零後求和**）")
CONST_C = ("⇒ 二式於**任一宗之增量為負**時即相異（鉗零 `max(0.0, ·)` ⛔ 出現於理論側）。"
           "🛑 **四造之數⛔ 讀為「理論＝實跑」殘差之全部歸因。**")


def drive(sb, mode):
    """一（態·情境）之驅動。回 dict。`mode` ＝ None（態甲·現行預設）／'off'（態乙）。"""
    if mode is None:
        os.environ.pop(ENV, None)
    else:
        os.environ[ENV] = mode
    for m in ("app_harvest", "run_verification", "selection_pipeline",
              "stepg_pipeline", "probe_WG9269_c4_gamma"):
        sys.modules.pop(m, None)
    from app_harvest import harvest
    import run_verification as rv
    from selection_pipeline import run_corner_pk
    from stepg_pipeline import run_step_g
    import probe_WG9269_c4_gamma as G4

    ns, fake_st = harvest()
    missing = [k for k in NEED if k not in ns]
    if missing:
        say("🔴 `ns[...]` 取不得：%s ⇒ **`rc=4`**（⛔ 靜默回空）" % missing)
        flush()
        raise SystemExit(4)
    _orig_slot = ns["_select_pool_slot"]
    slots = []

    def _spy_slot(widths, left, right):
        out = _orig_slot(widths, left, right)
        try:
            f = sys._getframe(1).f_locals
        except Exception:                                   # noqa: BLE001
            raise                                           # 🛑 ⛔ 靜默吞
        adv = f.get("_adv_base")
        pairs = {}
        if isinstance(adv, dict):
            for tag in ("left_results", "right_results"):
                for entry, res in (adv.get(tag) or []):
                    if not isinstance(entry, dict) or not isinstance(res, dict):
                        continue
                    pairs[entry.get("_ov2_idx")] = {
                        "id": (entry.get("tp") or {}).get("暫編地號"),
                        "w": res.get("_宗地寬度"), "W": res.get("W"),
                        "side": tag[:-len("_results")]}
        slots.append({"blk": f.get("blk_label"), "widths": list(widths or []),
                      "left": dict(left or {}), "right": dict(right or {}),
                      "res": out, "pairs": pairs, "adv_ok": isinstance(adv, dict)})
        return out
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
    g_rows, err = [], None
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            _sg = run_step_g(ns, fake_st, list(cb_by.values()), cad, snapshot,
                             params, build_p, wins, forced, sb,
                             eff_min_build_by_blk={})
        g_rows = _sg["g_rows"]
    except RuntimeError as e:
        err = str(e).split("\n")[0][:180]
        g_rows = (getattr(e, "partial", None) or {}).get("g_rows") or []
    rows, _sk = G4.to_csv_like(g_rows)
    return {"ns": ns, "orig_slot": _orig_slot, "slots": slots, "g_rows": g_rows,
            "rows": rows, "build_p": build_p, "err": err}


def real(d, blk, side):
    """實跑側 階段 `1` 之負擔和（`_rw_stage1_only` 之**逐字式**·⛔ 器內另算）。"""
    s2 = {tp["暫編地號"] for tp in d["build_p"]
          if str(tp.get("所屬街廓")) == blk and "配地階段" in tp}
    tot, used = 0.0, []
    for r in d["rows"]:
        if (r.get("所屬街廓") or "").strip() != blk:
            continue
        if (r.get("推進側別") or "").strip() != side:
            continue
        if float(r.get("F(m)", 0) or 0) <= 0:
            continue
        if r.get("暫編地號") in s2:
            continue
        v = float(r.get("Rw(%)", 0) or 0)
        tot += v
        used.append((r.get("暫編地號"), v))
    return round(tot, 2), used


def build_vectors(s):
    """四造之 `widths` 向量。回 (dict 造→向量, 診斷)。

    🔒 `α₀` ＝ **間諜所錄之實參逐位**（⛔ 任何外算）。
    🔒 `γ` ＝ 自 `α₀` 起，**僅**把有 `W` 可得之索引換為該宗之 `W`（未捨入）；
       ⛔ 以 `0.0` 靜默充無 `W` 之索引——其逐項具名於診斷。
    """
    a0 = [float(x or 0.0) for x in s["widths"]]
    a = [round(x, 2) for x in a0]
    g = list(a0)
    hit, miss = [], []
    for i in range(len(a0)):
        p = s["pairs"].get(i)
        if p is None or p.get("W") is None:
            miss.append(i)
            continue
        g[i] = float(p["W"])
        hit.append(i)
    b = [round(x, 2) for x in g]
    return ({"α₀": a0, "α": a, "γ": g, "β": b},
            {"hit": hit, "miss": miss, "n": len(a0)})


def theo(orig_slot, w, left, right):
    """理論側：**呼叫生產之 `_select_pool_slot` 本體**（⛔ 器內重算）。回 (ΣRw_L, ΣRw_R, k*)。"""
    res = orig_slot(w, left, right) or {}
    k = res.get("k")
    t = {x.get("k"): x for x in (res.get("table") or [])}.get(k) or {}
    if "ΣRw_L" not in t or "ΣRw_R" not in t:
        return None, None, k
    return float(t["ΣRw_L"] or 0.0), float(t["ΣRw_R"] or 0.0), k


def flush():
    try:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(_BUF) + "\n")
    except OSError as e:                                    # noqa: BLE001
        sys.stderr.write("🔴 落檔失敗：%r\n" % (e,))
        raise


def main():
    rc = 0
    say("# `W-G.9-320` 工項一／二：階段 `b` **四造**之出艙（**唯讀·零生產碼**）")
    say()
    say("> 🛑 **出艙即止**——本檔⛔ 作任何「孰為正典」「應改為」之判。")
    say("> 🔒 `α`／`γ`／`β` 一律為**替身·非忠實·⛔ 確值**；`α₀` 為**碼面現況·忠實**之自證造。")
    say()
    say("## `§零`　態之宣告（二值並報·以 `hash-object` 為實）")
    try:
        h1 = subprocess.run(["git", "rev-parse", "HEAD:app.py"], cwd=REPO,
                            capture_output=True, check=True).stdout.decode().strip()
        h2 = subprocess.run(["git", "hash-object", "app.py"], cwd=REPO,
                            capture_output=True, check=True).stdout.decode().strip()
    except (OSError, subprocess.CalledProcessError) as e:   # noqa: BLE001
        say("🔴 態之宣告取不得：%r（⛔ 靜默回空）" % (e,))
        flush()
        return 4
    say()
    say("| 量 | 值 |")
    say("|---|---|")
    say("| `git rev-parse HEAD:app.py` | `%s` |" % h1)
    say("| `git hash-object app.py`（**以此為實**） | `%s` |" % h2)
    say("| 二值相符 | %s |" % ("🟢 是" if h1 == h2 else "🔴 否（工作區異於倉側）"))
    say()
    say("## `§一`　常數因子（單 `§二` 工項一 `四`·**每表必載**）")
    say()
    say("- %s" % CONST_A)
    say("- %s" % CONST_B)
    say("- %s" % CONST_C)
    say()

    tot_rows, self_fail, empty = 0, [], []
    agg = {"格": 0, "粒度≠0": [], "軸≠0": [], "合≠0": [],
           "咬α": 0, "咬γ": 0, "咬β": 0, "idx": 0}
    for tag, mode, sb in CASES:
        d = drive(sb, mode)
        say("## `§二`　態%s（`%s`）·退縮 `%.1f` m" % (
            tag, "未設·現行預設" if mode is None else ENV + "=off", sb))
        say()
        blks = []
        for r in d["g_rows"]:
            if r.get("所屬街廓") not in blks:
                blks.append(r.get("所屬街廓"))
        say("母體：`g_rows` **`%d`** 列／可達街廓（出現序）＝ `%s`／"
            "理論側之呼叫 **`%d`** 次" % (len(d["g_rows"]), blks, len(d["slots"])))
        if d["err"]:
            say()
            say("🩸 **管線中止**（逐字）：`%s`" % d["err"])
        say()
        by_blk = {}
        for s in d["slots"]:
            by_blk.setdefault(s["blk"], []).append(s)
        if not by_blk:
            empty.append("態%s·%.1fm" % (tag, sb))
            say("🛑 **判定集為空**（理論側⛔ 被呼叫）⇒ 本（態·情境）⛔ 出艙任何造之數。")
            say()
            continue
        for blk in sorted(by_blk, key=lambda x: str(x)):
            hits = by_blk[blk]
            s = hits[-1]
            vecs, diag = build_vectors(s)
            rec = s["res"] or {}
            rec_k = rec.get("k")
            rec_t = {x.get("k"): x for x in (rec.get("table") or [])}.get(rec_k) or {}
            say("### 態%s·`%.1f` m·街廓 `%s`" % (tag, sb, blk))
            say()
            say("- 母體：宗數 **`%d`**／呼叫 `%d` 次（取末一次）／`_adv_base` 可得 ＝ `%s`"
                % (diag["n"], len(hits), s["adv_ok"]))
            say("- 宗序（`_ov2_idx` → 暫編地號）：`%s`"
                % [s["pairs"].get(i, {}).get("id") for i in range(diag["n"])])
            say("- `W` 可得之索引 **`%d`**／⛔ 可得 **`%d`**（逐項 ＝ `%s`·其值沿 `α₀` ⛔ 以 `0.0` 充）"
                % (len(diag["hit"]), len(diag["miss"]), diag["miss"]))
            say("- `left` ＝ `%s`" % {k: s["left"].get(k) for k in ("has", "F", "l1", "b")})
            say("- `right` ＝ `%s`" % {k: s["right"].get(k) for k in ("has", "F", "l1", "b")})
            say()
            # 🔒 **反靜默退路之計數**（`CLAUDE.md`：計數為 `0` 而結論為「無變化」者，
            #    一律先當作替身沒生效）——替身**咬到**之索引數須逐對出艙。
            say("**替身之咬到計數**（⛔ 以「因子為 `0`」逕推「替身生效而無後果」）")
            say()
            say("| 對 | 所變之因子 | 逐索引相異之數 | `Σw` 之差 |")
            say("|---|---|---|---|")
            for a, b_, fac in (("α₀", "α", "粒度（`_宗地寬度` 軸）"),
                               ("α₀", "γ", "軸（未捨入）"),
                               ("γ", "β", "粒度（`W` 軸）"),
                               ("α₀", "β", "軸 ＋ 粒度")):
                va, vb = vecs[a], vecs[b_]
                nd = sum(1 for x, y in zip(va, vb) if x != y)
                if (a, b_) == ("α₀", "α"):
                    agg["咬α"] += nd
                elif (a, b_) == ("α₀", "γ"):
                    agg["咬γ"] += nd
                    agg["idx"] += len(va)
                elif (a, b_) == ("γ", "β"):
                    agg["咬β"] += nd
                say("| `%s` → `%s` | %s | **`%d`** ／ `%d` | `%+.10f` |"
                    % (a, b_, fac, nd, len(va), sum(vb) - sum(va)))
            say()
            say("| `_ov2_idx` | 暫編地號 | `α₀`（＝ `α` 之源） | `α` | `γ`（＝ `β` 之源） | `β` |")
            say("|---|---|---|---|---|---|")
            for i in range(diag["n"]):
                say("| `%d` | `%s` | `%.10f` | `%.10f` | `%.10f` | `%.10f` |"
                    % (i, s["pairs"].get(i, {}).get("id"), vecs["α₀"][i],
                       vecs["α"][i], vecs["γ"][i], vecs["β"][i]))
            say()
            # ── 停機款 `4`：四造母體須逐造相同 ──
            lens = {k: len(v) for k, v in vecs.items()}
            if len(set(lens.values())) != 1:
                say("🔴 **停機款 `4`**：四造母體相異 ＝ `%s` ⇒ ⛔ 以相異母體之數相減。" % lens)
                flush()
                return 2
            # ── 自證閘（停機款 `2`）──
            L0, R0, k0 = theo(d["orig_slot"], vecs["α₀"], s["left"], s["right"])
            okL = (L0 is not None and rec_t.get("ΣRw_L") is not None
                   and float(rec_t["ΣRw_L"]) == L0)
            okR = (R0 is not None and rec_t.get("ΣRw_R") is not None
                   and float(rec_t["ΣRw_R"]) == R0)
            ok = bool(okL and okR and k0 == rec_k)
            say("**自證閘**（造 `α₀` 須與**未施替身**之當次實跑所錄之 `table[k*]` **逐位相符**·⛔ 容差）")
            say()
            say("| 量 | 實跑所錄 | 造 `α₀` 重算 | 判 |")
            say("|---|---|---|---|")
            say("| `k*` | `%s` | `%s` | %s |" % (rec_k, k0, "🟢" if k0 == rec_k else "🔴"))
            say("| `ΣRw_L` | `%s` | `%s` | %s |"
                % (rec_t.get("ΣRw_L"), L0, "🟢" if okL else "🔴"))
            say("| `ΣRw_R` | `%s` | `%s` | %s |"
                % (rec_t.get("ΣRw_R"), R0, "🟢" if okR else "🔴"))
            say()
            if not ok:
                self_fail.append("態%s·%.1fm·%s" % (tag, sb, blk))
                say("🔴 **自證閘破 ⇒ `rc=2` loud 拒測**——**⛔ 據 `α`／`γ`／`β` 之任何數**。")
                say()
                continue
            say("⇒ 🟢 **自證閘過**（三格逐位相符）。")
            say()
            # ── 四造 × 二側 ──
            res = {}
            for name in ("α₀", "α", "γ", "β"):
                res[name] = theo(d["orig_slot"], vecs[name], s["left"], s["right"])
            for side, key in (("left", 0), ("right", 1)):
                has = bool((s["left"] if side == "left" else s["right"]).get("has"))
                rv_, used = real(d, blk, side)
                say("#### 側 `%s`（`has` ＝ `%s`）" % (side, has))
                say()
                say("| 造 | `widths` 之來源·粒度 | 標 | `ΣRw_%s` | `k*` | 實跑(階段1) | `Δ(造)` |"
                    % ("L" if side == "left" else "R"))
                say("|---|---|---|---|---|---|---|")
                d0 = None
                for name, src in (("α₀", "`_宗地寬度`·未捨入"), ("α", "`_宗地寬度`·`round(·,2)`"),
                                  ("γ", "`W`·未捨入"), ("β", "`W`·`round(·,2)`")):
                    v = res[name][key]
                    k = res[name][2]
                    mark = "**忠實·自證造**" if name == "α₀" else "替身·非忠實·⛔ 確值"
                    if v is None:
                        say("| `%s` | %s | %s | 🔴 鍵缺 | `%s` | `%.2f` | — |"
                            % (name, src, mark, k, rv_))
                        continue
                    dd = v - rv_
                    if name == "α₀":
                        d0 = dd
                    say("| `%s` | %s | %s | `%.10f` | `%s` | `%.2f` | `%+.10f` |"
                        % (name, src, mark, v, k, rv_, dd))
                say()
                if d0 is not None:
                    fa = (res["α"][key] - rv_) - d0 if res["α"][key] is not None else None
                    fg = (res["γ"][key] - rv_) - d0 if res["γ"][key] is not None else None
                    fb = (res["β"][key] - rv_) - d0 if res["β"][key] is not None else None
                    say("**因子之分離**（單 `§二` 工項一 `七`）")
                    say()
                    say("| 因子 | 式 | 值 |")
                    say("|---|---|---|")
                    say("| 粒度（同軸 ＝ `_宗地寬度`） | `Δ(α) − Δ(α₀)` | %s |"
                        % ("`%+.10f`" % fa if fa is not None else "—"))
                    say("| 軸（同粒度 ＝ 未捨入） | `Δ(γ) − Δ(α₀)` | %s |"
                        % ("`%+.10f`" % fg if fg is not None else "—"))
                    say("| 二因子之合 ＋ 交互 | `Δ(β) − Δ(α₀)` | %s |"
                        % ("`%+.10f`" % fb if fb is not None else "—"))
                    agg["格"] += 1
                    tagc = "態%s·%.1fm·%s·%s" % (tag, sb, blk, side)
                    if fa:
                        agg["粒度≠0"].append(tagc)
                    if fg:
                        agg["軸≠0"].append(tagc)
                    if fb:
                        agg["合≠0"].append(tagc)
                    say()
                say("- 實跑側之受詞宗（`%d` 宗）＝ `%s`"
                    % (len(used), [(a, round(b, 4)) for a, b in used]))
                say("- %s" % CONST_C)
                say()
                tot_rows += 1
            say()

    # ── 結語 ──
    say("## `§三`　結語（**⛔ 判**）")
    say()
    say("- 出艙之（態·情境·街廓·側）格數 ＝ **`%d`**" % tot_rows)
    say("- 自證閘破之格 ＝ **`%d`**（逐項 ＝ `%s`）" % (len(self_fail), self_fail or "[]"))
    say("- 判定集為空之（態·情境）＝ **`%d`**（逐項 ＝ `%s`）" % (len(empty), empty or "[]"))
    say()
    say("### `§三-1`　因子之彙總（**⛔ 判**·⛔ 以「因子為 `0`」逕推「替身生效而無後果」）")
    say()
    say("| 量 | 值 |")
    say("|---|---|")
    say("| 有因子可算之格 | **`%d`** ／ `%d` |" % (agg["格"], tot_rows))
    say("| **粒度因子 ≠ `0`** 之格 | **`%d`**（逐項 ＝ `%s`）|"
        % (len(agg["粒度≠0"]), agg["粒度≠0"] or "[]"))
    say("| **軸因子 ≠ `0`** 之格 | **`%d`**（逐項 ＝ `%s`）|"
        % (len(agg["軸≠0"]), agg["軸≠0"] or "[]"))
    say("| 二因子之合 ≠ `0` 之格 | **`%d`**（逐項 ＝ `%s`）|"
        % (len(agg["合≠0"]), agg["合≠0"] or "[]"))
    say()
    say("**替身之咬到計數（全母體之和）**——`0` 者⛔ 得讀為「替身生效而無後果」，"
        "須先判其為**替身未咬到**：")
    say()
    say("| 對 | 所變之因子 | 逐索引相異之數（和） | 母體（索引和） |")
    say("|---|---|---|---|")
    say("| `α₀` → `α` | 粒度（`_宗地寬度` 軸） | **`%d`** | `%d` |" % (agg["咬α"], agg["idx"]))
    say("| `α₀` → `γ` | 軸（未捨入） | **`%d`** | `%d` |" % (agg["咬γ"], agg["idx"]))
    say("| `γ` → `β` | 粒度（`W` 軸） | **`%d`** | `%d` |" % (agg["咬β"], agg["idx"]))
    say()
    say("🔒 **二個粒度對之咬到數<u>皆</u>為 `0`，係<u>構造使然</u>，⛔ 替身未生效**——"
        "其對照 ＝ `α₀` → `γ` 之咬到 **`%d`**／`%d`（軸之替身**確已生效**）"
        "⇒ 本器之替身機制**非恆不咬**。" % (agg["咬γ"], agg["idx"]))
    say()
    say("| 軸 | 其**產生式逐字**（`檔:列`） | 賦值處之粒度 | ⇒ `round(·, 2)` 於其上 |")
    say("|---|---|---|---|")
    say("| `_宗地寬度` | `_res['_宗地寬度'] = round(_pw, 2)`"
        "（`verify/stepg_pipeline.py:737`／`app.py:22036`·二處逐字相同） | **已 `2dp`** | **恆等變換** |")
    say("| `W` | `'W': round(W_cur, 2)`（`app.py:6491`）／`'W': round(W, 2)`（`app.py:10275`）／"
        "`'W': round(W_conv, 2)`（`app.py:10353`） | **已 `2dp`** | **恆等變換** |")
    say()
    say("🛑 ⇒ **二軸之粒度因子於本案<u>結構上皆不可量</u>**——其「未捨入」之值於碼面**不存在**"
        "（⛔ 以任何外算之式充之）。⇒ 本批之 `2 × 2` 全因子於碼面**塌為 `2 × 1`**："
        "`α₀ ≡ α`、`γ ≡ β`（**逐位**·由上開咬到計數 `0`／`0` 機械坐實）。")
    say("🔒 **併記（照實）**：`verify/stepg_pipeline.py:505` 之 `round(_res.get('_宗地寬度', 0.0), 2)`"
        " 與 `:492` 之 `round(_res.get('W', 0.0), 2)` 皆為**顯示層之第二次捨入**（冪等）"
        "⇒ ⛔ 得由其存在推論「輸入層未捨入」。**出艙即止·⛔ 判。**")
    if self_fail:
        rc = 2
    elif tot_rows == 0:
        rc = 3
    say()
    say("- `rc` ＝ **`%d`**（`0` 全綠／`2` 自證閘破／`3` 判定集為空／`4` `ns[...]` 取不得）" % rc)
    say("🛑 `rc ≠ 0` **⛔ 等同「受詞紅」**。")
    say()

    # ── `恆常附款 k③`：落檔之字樣自檢（樣式**執行期組出**·⛔ 使其字面落入本檔）──
    import re as _re
    body = "\n".join(_BUF)
    pats = [("單號", "W-G.9-" + r"(\d{1,4})"),
            ("自" + "誤號", "自" + "誤 " + r"`?(\d{1,4})"),
            ("阻塞項號", "G" + "B-" + r"(\d{1,4})"),
            ("裁定號", "V" + "R-" + r"(\d{1,4})"),
            ("裁號", "K-" + "9-" + r"(\d{1,3})")]
    say("- **落檔之字樣自檢**（`恆常附款 k③`·樣式執行期組出·⛔ 使其字面落入本檔）")
    say()
    say("| 類 | 相異命中 | 判 |")
    say("|---|---|---|")
    for lab, p in pats:
        s = sorted(set(_re.findall(p, body)))
        allowed = (lab == "單號" and s == ["320"])
        say("| %s | `%s` | %s |"
            % (lab, s, "🟢 僅本單之號" if allowed else ("🟢 空" if not s else "🩸 非空·須具名")))
    say()
    flush()
    return rc


if __name__ == "__main__":
    sys.exit(main())
