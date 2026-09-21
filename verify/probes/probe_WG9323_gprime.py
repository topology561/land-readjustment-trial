# -*- coding: utf-8 -*-
r"""`W-G.9-323` 工項一：造 **`γ′`** 之補測（`W` 軸·**未捨入**·取 `W_far_raw`）。

受詞（逐字·單 `§二` 工項一 `一`）：
  「理論側 `_select_pool_slot` 所餵之 `widths` 向量，於造 **`γ′`**（`W` 軸·**未捨入**·取 `W_far_raw`）下
   重算其 `table[k*]` 之 `ΣRw_L`／`ΣRw_R`，並與既有之 `α₀`／`α`／`γ`／`β` 四造及**實跑側**同
   （態·情境·街廓·側）之階段 `1` 負擔和對拍。」

🔒 **`γ′` 之來源與粒度（`恆常附款 m④`：每一造須以碼面之產生式逐字定之）**
   `app.py:10359` 逐字 `'W_far_raw': W_conv,                                # 未捨入之本宗遠側 W`
   ——與既有 `γ` 所取之 `'W'`（`app.py:10353` 逐字 `'W': round(W_conv, 2)`）**同一 `return` 字典**、相距六列。
   ⇒ 該來源**結構上能**產出未捨入之值（其自證 ＝ 自證閘 `3` ＋ 判別力[必非零]）。
🛑 **`_宗地寬度` 軸：本波⛔ 測**（其未捨入值須經框內省取 `_cos_dn` 並以 `S_raw` 重成）
   ——**⛔ 寫為「碼面不存在」**（`m④`）。

🔒 **復用（`恆常附款 k②`·⛔ 重寫第二份判準）**：`theo`／`real`／`build_vectors`／`ENV`／`CASES`／`NEED`
   一律自 `probe_WG9320_stageb` **`import` 並呼叫**；本器**⛔ 動該檔一字**。
🔒 **`drive2()` ＝ 其 `drive()` 之逐字複本 ＋ 恰一處增補**（`pairs[...]` 多一鍵 `"W_raw"`）；
   其逐行差於 `main()` 內**機械比對並出艙**，差之集合⛔ 為 {函式名列, 該鍵列} 即 `rc=5`。
🔒 **落檔之字樣紀律（`k③`）**：本檔與其落檔**⛔ 含 `W-G.9-323` 以外之任何取號字樣**；
   自檢於 `main()` 末逐類出艙（樣式**執行期組出**·⛔ 使其字面落入落檔）。

🛑 **出艙即止**——⛔ 判孰為正典、⛔ 判「捨入即 `Δ` 之成因」、⛔ 判「捨入⛔ 為 `Δ` 之成因」、
   ⛔ 提修法主張、⛔ 判任何阻塞項應否解除。

`rc`：`0` 全綠／`2` 自證閘破／`3` 判定集為空／`4` `ns[...]` 取不得／`5` `drive2()` 之逐行差超出。
🛑 `rc ≠ 0` **⛔ 等同「受詞紅」**。

用法：`PYTHONIOENCODING=utf-8 python verify/probes/probe_WG9323_gprime.py`
"""
import contextlib
import difflib
import inspect
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "verify"))
sys.path.insert(0, HERE)

import probe_WG9320_stageb as S                                      # noqa: E402

ENV = S.ENV
CASES = S.CASES
NEED = S.NEED
OUT = os.path.join(REPO, "verify", "out", "WG9323_gprime.md")
PREV_LOG = os.path.join(REPO, "verify", "out", "WG9320_stageb.md")
_BUF = []

# ── 常數因子之逐字（單 `§二` 工項一 `六`·**每表必載**）────────────────────────
CONST = ("🛑 **式之形在全部造中仍為常數**：理論側 `R(b + Σw) − R(b)`（telescoping）／"
         "實跑側 `Σ_宗 max(0, R(W_i) − R(W_{i−1}))`（逐宗鉗零後求和）"
         "⇒ **任何造之數⛔ 讀為殘差之全部歸因**。")


def say(s=""):
    print(s)
    _BUF.append(s)


def flush():
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(_BUF) + "\n")


def drive2(sb, mode):
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
                        "W_raw": res.get("W_far_raw"),
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


# ══ `drive2()` 與既有 `drive()` 之逐行差（停機款 `4`）══════════════════════
def drive_diff():
    """回 (差之集合, 正規化後之差數, 原始差數)。

    🔒 **正規化之逐字**：僅把 `def drive2(` 換為 `def drive(`——函式名之別係**命名**、
       ⛔ 受詞之別。**二數並報**（原始／正規化），⛔ 只報其一。
    """
    a = inspect.getsource(S.drive).split("\n")
    b = inspect.getsource(drive2).split("\n")
    raw = [x for x in difflib.unified_diff(a, b, lineterm="", n=0)
           if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    bn = [x.replace("def drive2(", "def drive(") for x in b]
    norm = [x for x in difflib.unified_diff(a, bn, lineterm="", n=0)
            if x[:1] in "+-" and x[:3] not in ("+++", "---")]
    return raw, len(norm), len(raw)


# ══ 既有落檔之 `γ` 之抽取（自證閘 `2`）════════════════════════════════════
def prev_gamma():
    """自 `WG9320_stageb.md` 抽 (態, 退縮, 街廓, 側) → `γ` 之 `ΣRw`（逐字·⛔ 重算）。"""
    out = {}
    if not os.path.exists(PREV_LOG):
        return out
    tag, side = None, None
    rx_h = re.compile(r"^### 態(.)·`([0-9.]+)` m·街廓 `([^`]+)`")
    rx_s = re.compile(r"^#### 側 `([a-z]+)`")
    rx_g = re.compile(r"^\| `γ` \|[^|]*\|[^|]*\| `([0-9.\-]+)` \|")
    for ln in io.open(PREV_LOG, encoding="utf-8"):
        m = rx_h.match(ln)
        if m:
            tag = (m.group(1), float(m.group(2)), m.group(3))
            continue
        m = rx_s.match(ln)
        if m:
            side = m.group(1)
            continue
        m = rx_g.match(ln)
        if m and tag and side:
            out[(tag[0], tag[1], tag[2], side)] = float(m.group(1))
    return out


def main():
    rc = 0
    say("# `W-G.9-323` 工項一／二：造 `γ′` 之補測（**唯讀·零生產碼**）")
    say()
    say("> 🛑 **出艙即止**——本檔⛔ 判孰為正典、⛔ 判「捨入即 `Δ` 之成因」或其否定、⛔ 提修法主張。")
    say("> 🔒 `α`／`γ`／`γ′`／`β` 一律為**替身·非忠實·⛔ 確值**；`α₀` 為**碼面現況·忠實**之自證造。")
    say("> 🛑 **`_宗地寬度` 軸：本波⛔ 測**（⛔ 寫為「碼面不存在」）。")
    say()

    # ── `§零` 態之宣告 ──
    say("## `§零`　態之宣告（二值並報·以 `hash-object` 為實）")
    try:
        h1 = subprocess.run(["git", "rev-parse", "HEAD:app.py"], cwd=REPO,
                            capture_output=True, check=True).stdout.decode().strip()
        h2 = subprocess.run(["git", "hash-object", "app.py"], cwd=REPO,
                            capture_output=True, check=True).stdout.decode().strip()
        p1 = subprocess.run(["git", "rev-parse", "HEAD:verify/probes/probe_WG9320_stageb.py"],
                            cwd=REPO, capture_output=True, check=True).stdout.decode().strip()
        p2 = subprocess.run(["git", "hash-object", "verify/probes/probe_WG9320_stageb.py"],
                            cwd=REPO, capture_output=True, check=True).stdout.decode().strip()
    except (OSError, subprocess.CalledProcessError) as e:               # noqa: BLE001
        say("🔴 態之宣告取不得：%r（⛔ 靜默回空）" % (e,))
        flush()
        return 4
    say()
    say("| 量 | 值 |")
    say("|---|---|")
    say("| `git rev-parse HEAD:app.py` | `%s` |" % h1)
    say("| `git hash-object app.py`（**以此為實**） | `%s` |" % h2)
    say("| 二值相符 | %s |" % ("🟢 是" if h1 == h2 else "🔴 否"))
    say("| **被復用之器** `probe_WG9320_stageb.py`（`HEAD`／工作區） | `%s` ／ `%s` |" % (p1, p2))
    say("| 其二值相符（⛔ 動一字） | %s |" % ("🟢 是" if p1 == p2 else "🔴 否·**停機款 `2`**"))
    say()

    # ── `§一` `drive2()` 之逐行差 ──
    raw, n_norm, n_raw = drive_diff()
    say("## `§一`　`drive2()` 與既有 `drive()` 之逐行差（停機款 `4`·**二數並報**）")
    say()
    say("| 量 | 值 |")
    say("|---|---|")
    say("| **原始**逐行差 | **`%d`** |" % n_raw)
    say("| **正規化後**（僅把 `def drive2(` 換為 `def drive(`）逐行差 | **`%d`** |" % n_norm)
    say()
    say("差之逐列（逐字）：")
    say()
    say("```")
    for x in raw:
        say(x)
    say("```")
    say()
    want = {'-    """一（態·情境）之驅動。回 dict。`mode` ＝ None（態甲·現行預設）／\'off\'（態乙）。"""'}
    body = [x for x in raw if "def drive" not in x]
    ok_diff = (n_norm == 1 and len(body) == 1
               and body[0].strip().startswith('+') and '"W_raw"' in body[0])
    say("🔒 **判**：正規化後之差 ＝ **`%d`** 處，且其唯一之差為 `pairs[...]` 多一鍵 "
        "`\"W_raw\": res.get(\"W_far_raw\")` ⇒ %s"
        % (n_norm, "🟢 合單 `§二` 工項一 `四`" if ok_diff else "🔴 **`rc=5`**"))
    say()
    if not ok_diff:
        flush()
        return 5
    del want

    # ── `§二` `max|R'|` 之當態重跑 ──
    say("## `§二`　`max|R'|` 之**當態重跑**（`恆常附款 w②`：⛔ 引他態落檔之數）")
    say()
    d0 = drive2(0.0, None)
    RW = d0["ns"]["rw_from_width"]
    mx, at, w = 0.0, 0.0, 0.0
    while w < 18.0:
        s = (RW(w + 1e-6) - RW(w)) / 1e-6
        if s > mx:
            mx, at = s, w
        w += 0.001
    say("| 量 | **本態重跑** | 既有落檔所載（**繫其態**·⛔ 引為本態之值） | 判 |")
    say("|---|---|---|---|")
    say("| `max\\|R'\\|` | **`%.4f` %%/m**（@`W≈%.3f` m·數值掃描 `1e-3` 步長） | `17.4000` %%/m | %s |"
        % (mx, at, "🟢 相符" if abs(mx - 17.4) < 5e-5 else "🩸 相異·二值並列"))
    say("| `ΣA`／`ΣB`（全鏈） | **本批⛔ 重跑**——其母體為他批之全鏈（`150` 筆） | `+0.024831`／`−0.469168` | ⚪ **母體相異 ⇒ ⛔ 判可比** |")
    say()
    say("🔒 **上界式（復用其驗法·⛔ 引其數）**：")
    say("`|ΣRw − [R(W_n) − R(W_0)]| ≤ (n−1)·0.005·max|R'| ＋ n·0.005`")
    say("（前項 ＝ 交棒降精度／後項 ＝ `Rw` 之 `2dp`）")
    say()
    say("🔒 **候選 `B` 之定義（逐字復用）**：`|R(W_far_raw) − R(round(W_far_raw,2))|`。")
    say()

    PG = prev_gamma()
    say("🔒 **自證閘 `2` 之對照來源**：`verify/out/WG9320_stageb.md`，"
        "自其抽得 `γ` 之格 **`%d`** 個（⛔ 重算·逐字抽取）。" % len(PG))
    say()

    # ── `§三` 逐（態·情境·街廓·側）──
    tot, self_fail, empty = 0, [], []
    agg = {"咬γ′": 0, "idx": 0, "粒度≠0": [], "g2_fail": [], "g2_ok": 0}
    for ci, (tag, mode, sb) in enumerate(CASES):
        d = d0 if (ci == 0) else drive2(sb, mode)
        say("## `§三`　態%s（`%s`）·退縮 `%.1f` m"
            % (tag, "未設·現行預設" if mode is None else ENV + "=off", sb))
        say()
        blks = []
        for r in d["g_rows"]:
            if r.get("所屬街廓") not in blks:
                blks.append(r.get("所屬街廓"))
        say("母體：`g_rows` **`%d`** 列／可達街廓（出現序）＝ `%s`／理論側之呼叫 **`%d`** 次"
            % (len(d["g_rows"]), blks, len(d["slots"])))
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
            s = by_blk[blk][-1]
            vecs, diag = S.build_vectors(s)                # 🔒 復用·⛔ 重寫
            n = diag["n"]
            gp = list(vecs["α₀"])
            hit, miss, dsum = [], [], 0.0
            for i in range(n):
                p = s["pairs"].get(i) or {}
                v = p.get("W_raw")
                if v is None:
                    miss.append(i)
                    continue
                gp[i] = float(v)
                hit.append(i)
            vecs["γ′"] = gp
            nb = sum(1 for x, y in zip(vecs["γ"], gp) if x != y)
            for i in hit:
                dsum += abs(float(gp[i]) - round(float(gp[i]), 2))
            agg["咬γ′"] += nb
            agg["idx"] += n
            rec = s["res"] or {}
            rec_k = rec.get("k")
            rec_t = {x.get("k"): x for x in (rec.get("table") or [])}.get(rec_k) or {}
            say("### 態%s·`%.1f` m·街廓 `%s`" % (tag, sb, blk))
            say()
            say("- 母體：宗數 **`%d`**／`k*` ＝ `%s`／`_adv_base` 可得 ＝ `%s`"
                % (n, rec_k, s["adv_ok"]))
            say("- 宗序（`_ov2_idx` → 暫編地號）：`%s`"
                % [(s["pairs"].get(i) or {}).get("id") for i in range(n)])
            say("- `W_far_raw` 可得之索引 **`%d`**／⛔ 可得 **`%d`**（逐項 ＝ `%s`·其值沿 `α₀`）"
                % (len(hit), len(miss), miss))
            say()
            # 自證閘 `1`
            L0, R0, k0 = S.theo(d["orig_slot"], vecs["α₀"], s["left"], s["right"])
            okL = (L0 is not None and rec_t.get("ΣRw_L") is not None
                   and float(rec_t["ΣRw_L"]) == L0)
            okR = (R0 is not None and rec_t.get("ΣRw_R") is not None
                   and float(rec_t["ΣRw_R"]) == R0)
            g1 = bool(okL and okR and k0 == rec_k)
            say("**自證閘 `1`**（`α₀` vs 未施替身之當次實跑所錄之 `table[k*]`·**逐位**·⛔ 容差）："
                "`k*` `%s`／`%s`·`ΣRw_L` `%s`／`%s`·`ΣRw_R` `%s`／`%s` ⇒ %s"
                % (rec_k, k0, rec_t.get("ΣRw_L"), L0, rec_t.get("ΣRw_R"), R0,
                   "🟢" if g1 else "🔴"))
            say()
            if not g1:
                self_fail.append("態%s·%.1fm·%s（閘 1）" % (tag, sb, blk))
                say("🔴 **自證閘 `1` 破 ⇒ `rc=2` loud 拒測**·**⛔ 據 `γ′` 之任何數**。")
                say()
                continue
            res = {}
            for nm in ("α₀", "α", "γ", "γ′", "β"):
                res[nm] = S.theo(d["orig_slot"], vecs[nm], s["left"], s["right"])
            # 自證閘 `3` ＋ 判別力
            say("**自證閘 `3`**（`γ′` 對 `γ` 之咬到索引數須 **> `0`**）：咬到 **`%d`**／`%d` ⇒ %s"
                % (nb, n, "🟢" if nb > 0 else "🔴"))
            say()
            say("**判別力[必非零]**：咬到之索引上 `Σ|W_far_raw − round(W_far_raw,2)|` ＝ "
                "**`%.10f`** m ⇒ %s" % (dsum, "🟢" if dsum > 0 else "🔴 **器紅**·⛔ 判為「該軸無粒度」"))
            say()
            if nb == 0 or dsum <= 0:
                self_fail.append("態%s·%.1fm·%s（閘 3／判別力）" % (tag, sb, blk))
                say("🔴 ⇒ **`rc=2` loud 拒測**。")
                say()
                continue
            say("| `_ov2_idx` | 暫編地號 | `α₀`（＝`α`） | `γ`（＝`β`·`2dp`） | **`γ′`（`W_far_raw`）** | `γ′ − γ` |")
            say("|---|---|---|---|---|---|")
            for i in range(n):
                say("| `%d` | `%s` | `%.10f` | `%.10f` | `%.10f` | `%+.10f` |"
                    % (i, (s["pairs"].get(i) or {}).get("id"), vecs["α₀"][i],
                       vecs["γ"][i], gp[i], gp[i] - vecs["γ"][i]))
            say()
            for side, key in (("left", 0), ("right", 1)):
                has = bool((s["left"] if side == "left" else s["right"]).get("has"))
                rv_, used = S.real(d, blk, side)
                # 自證閘 `2`
                pv = PG.get((tag, sb, blk, side))
                gv = res["γ"][key]
                g2 = (pv is not None and gv is not None and abs(pv - gv) < 5e-11)
                if pv is None:
                    agg["g2_fail"].append("態%s·%.1fm·%s·%s（對照格缺）" % (tag, sb, blk, side))
                elif g2:
                    agg["g2_ok"] += 1
                else:
                    agg["g2_fail"].append("態%s·%.1fm·%s·%s" % (tag, sb, blk, side))
                say("#### 側 `%s`（`has` ＝ `%s`）" % (side, has))
                say()
                say("**自證閘 `2`**（本器之 `γ` vs 既有落檔同格之 `γ`·**逐位**）："
                    "本器 `%s`／落檔 `%s` ⇒ %s"
                    % ("%.10f" % gv if gv is not None else "—",
                       "%.10f" % pv if pv is not None else "**缺**",
                       "🟢" if g2 else ("🛑 對照格缺" if pv is None else "🔴")))
                say()
                say("| 造 | 來源·粒度 | 標 | `ΣRw_%s` | `k*` | 實跑(階段1) | `Δ(造)` |"
                    % ("L" if side == "left" else "R"))
                say("|---|---|---|---|---|---|---|")
                d_a0 = d_g = d_gp = None
                for nm, src in (("α₀", "`_宗地寬度`·未捨入"), ("α", "`_宗地寬度`·`round(·,2)`"),
                                ("γ", "`W`（`app.py:10353` ＝ `round(W_conv,2)`）"),
                                ("γ′", "**`W_far_raw`（`app.py:10359`）·未捨入**"),
                                ("β", "`W`·`round(·,2)`")):
                    v = res[nm][key]
                    mark = "**忠實·自證造**" if nm == "α₀" else "替身·非忠實·⛔ 確值"
                    if v is None:
                        say("| `%s` | %s | %s | 🔴 鍵缺 | `%s` | `%.2f` | — |"
                            % (nm, src, mark, res[nm][2], rv_))
                        continue
                    dd = v - rv_
                    if nm == "α₀":
                        d_a0 = dd
                    elif nm == "γ":
                        d_g = dd
                    elif nm == "γ′":
                        d_gp = dd
                    say("| `%s` | %s | %s | `%.10f` | `%s` | `%.2f` | `%+.10f` |"
                        % (nm, src, mark, v, res[nm][2], rv_, dd))
                say()
                if d_a0 is not None and d_gp is not None and d_g is not None:
                    f_gran = d_gp - d_g
                    f_axis = d_gp - d_a0
                    if f_gran:
                        agg["粒度≠0"].append("態%s·%.1fm·%s·%s" % (tag, sb, blk, side))
                    say("**因子之分離**")
                    say()
                    say("| 因子 | 式 | 值 |")
                    say("|---|---|---|")
                    say("| **`W` 軸之粒度**（同軸） | `Δ(γ′) − Δ(γ)` | `%+.10f` |" % f_gran)
                    say("| 軸 ＋ 粒度 | `Δ(γ′) − Δ(α₀)` | `%+.10f` |" % f_axis)
                    say()
                nn = len(used)
                ub = (max(nn - 1, 0) * 0.005 * mx + nn * 0.005) if nn else 0.0
                say("| 量 | 值 |")
                say("|---|---|")
                say("| 本格之宗數 `n`（實跑側之受詞宗） | **`%d`** |" % nn)
                say("| 上界式之值 `(n−1)·0.005·max\\|R'\\| ＋ n·0.005` | **`%.4f` %%** |" % ub)
                say("| `Δ(γ′)` | %s |" % ("`%+.10f`" % d_gp if d_gp is not None else "—"))
                say("| `Δ(α₀)` | %s |" % ("`%+.10f`" % d_a0 if d_a0 is not None else "—"))
                say("| `\\|Δ(α₀)\\| ≤ 上界`？ | `%s` |"
                    % (abs(d_a0) <= ub if d_a0 is not None else "—"))
                say("| `\\|Δ(γ′)\\| ≤ 上界`？ | `%s` |"
                    % (abs(d_gp) <= ub if d_gp is not None else "—"))
                say()
                say("- 實跑側之受詞宗 ＝ `%s`" % [(a, round(b, 4)) for a, b in used])
                say("- %s" % CONST)
                say()
                tot += 1
            say()

    # ── `§四` 結語 ──
    say("## `§四`　結語（**⛔ 判**）")
    say()
    say("- 出艙之（態·情境·街廓·側）格數 ＝ **`%d`**" % tot)
    say("- 自證閘 `1`／`3` 破之格 ＝ **`%d`**（逐項 ＝ `%s`）" % (len(self_fail), self_fail or "[]"))
    say("- **自證閘 `2`** 過之格 ＝ **`%d`**／破或缺 ＝ **`%d`**（逐項 ＝ `%s`）"
        % (agg["g2_ok"], len(agg["g2_fail"]), agg["g2_fail"] or "[]"))
    say("- 判定集為空之（態·情境）＝ **`%d`**（逐項 ＝ `%s`）" % (len(empty), empty or "[]"))
    say("- **`W` 軸之粒度因子 ≠ `0`** 之格 ＝ **`%d`**（逐項 ＝ `%s`）"
        % (len(agg["粒度≠0"]), agg["粒度≠0"] or "[]"))
    say("- **`γ′` 對 `γ` 之咬到（全母體之和）** ＝ **`%d`**／`%d`" % (agg["咬γ′"], agg["idx"]))
    say()
    if self_fail or agg["g2_fail"]:
        rc = 2
    elif tot == 0:
        rc = 3
    say("- `rc` ＝ **`%d`**（`0` 全綠／`2` 自證閘破／`3` 判定集為空／`4` `ns[...]` 取不得／"
        "`5` `drive2()` 之逐行差超出）" % rc)
    say("🛑 `rc ≠ 0` **⛔ 等同「受詞紅」**。")
    say()
    say("🛑 **出艙即止**——本檔⛔ 判「捨入即 `Δ` 之成因」、⛔ 判其否定、⛔ 判二軸孰為正典、"
        "⛔ 提修法主張、⛔ 判任何阻塞項應否解除。")
    say()

    # ── `k③` 落檔之字樣自檢 ──
    body = "\n".join(_BUF)
    pats = [("單號", "W-G.9-" + r"(\d{1,4})"),
            ("自" + "誤號", "自" + "誤 " + r"`?(\d{1,4})"),
            ("阻塞項號", "G" + "B-" + r"(\d{1,4})"),
            ("裁定號", "V" + "R-" + r"(\d{1,4})"),
            ("裁號", "K-" + "9-" + r"(\d{1,3})")]
    say("- **落檔之字樣自檢**（`k③`·樣式執行期組出·⛔ 使其字面落入本檔）")
    say()
    say("| 類 | 相異命中 | 判 |")
    say("|---|---|---|")
    for lab, p in pats:
        st = sorted(set(re.findall(p, body)))
        allowed = (lab == "單號" and st == ["323"])
        say("| %s | `%s` | %s |"
            % (lab, st, "🟢 僅本單之號" if allowed else ("🟢 空" if not st else "🩸 非空·須具名")))
    say()
    flush()
    return rc


if __name__ == "__main__":
    sys.exit(main())
